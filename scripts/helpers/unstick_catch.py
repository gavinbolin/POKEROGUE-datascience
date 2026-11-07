import json, urllib.request, websocket, time, base64, pathlib, sys
OUT = pathlib.Path(r"C:\Users\gavin\agent-tools")
LOG = OUT / "pokerogue_farm_log.txt"

def log(msg):
    line = time.strftime("%H:%M:%S") + " " + msg
    print(line, flush=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")

tabs = json.load(urllib.request.urlopen("http://127.0.0.1:9222/json"))
page = [t for t in tabs if t.get("type")=="page" and "pokerogue.net" in t.get("url","")][0]
ws = websocket.create_connection(page["webSocketDebuggerUrl"], timeout=30)
nid = [0]

def call(method, params=None):
    nid[0] += 1
    msg = {"id": nid[0], "method": method}
    if params is not None:
        msg["params"] = params
    ws.send(json.dumps(msg))
    while True:
        r = json.loads(ws.recv())
        if r.get("id") == nid[0]:
            return r

def ev(expr):
    r = call("Runtime.evaluate", {"expression": expr, "returnByValue": True})
    return ((r.get("result") or {}).get("result") or {}).get("value")

def key(key, code, kc, hold=100):
    kwargs = {"type": "keyDown", "windowsVirtualKeyCode": kc, "code": code, "key": key}
    if len(key) == 1:
        kwargs["text"] = key
    call("Input.dispatchKeyEvent", kwargs)
    time.sleep(hold / 1000.0)
    call("Input.dispatchKeyEvent", {"type": "keyUp", "windowsVirtualKeyCode": kc, "code": code, "key": key})

def z(hold=100):
    key("z", "KeyZ", 90, hold)

def bs(hold=100):
    key("Backspace", "Backspace", 8, hold)

def arrow(d, hold=80):
    m = {"Up": ("ArrowUp", 38), "Down": ("ArrowDown", 40), "Left": ("ArrowLeft", 37), "Right": ("ArrowRight", 39)}
    c, k = m[d]
    key(c, c, k, hold)

def shot(name):
    s = call("Page.captureScreenshot", {"format": "jpeg", "quality": 55})
    (OUT / name).write_bytes(base64.b64decode(s["result"]["data"]))

def state():
    return ev("""(() => {
      const g=window.gameInfo||{};
      return {t:g.playTime,w:g.wave,m:g.gameMode,b:g.biome,luck:g.luck};
    })()""")

call("Page.bringToFront")
ev("(() => { const c=document.querySelector('canvas'); if(c){c.tabIndex=0;c.focus();} return !!c; })()")
box = ev("(() => { const c=document.querySelector('canvas'); const r=c.getBoundingClientRect(); return {x:r.x+r.width/2,y:r.y+r.height/2}; })()")
call("Input.dispatchMouseEvent", {"type": "mousePressed", "x": box["x"], "y": box["y"], "button": "left", "clickCount": 1})
time.sleep(0.05)
call("Input.dispatchMouseEvent", {"type": "mouseReleased", "x": box["x"], "y": box["y"], "button": "left", "clickCount": 1})
time.sleep(0.2)

st = state()
log("UNSTICK_START " + json.dumps(st))
shot("pokerogue_u0.jpg")

# 1) Clear money / text prompts with Z (and Space). No Escape. No Enter mash.
for i in range(8):
    z(110)
    time.sleep(0.45)
# one Space as alt confirm
key(" ", "Space", 32, 100)
time.sleep(0.4)
st = state()
log("AFTER_CLEAR " + json.dumps(st))
shot("pokerogue_u1.jpg")

# 2) Catch shiny: open Ball menu. Fight menu is Fight/Ball/Pokemon/Run.
# Cursor often on Fight; Right or Down to Ball depending on layout.
# PokéRogue command menu is 2x2: Fight | Ball / Pokemon | Run
# So ArrowRight from Fight -> Ball, then Z.
bs(100)  # ensure not in a sub-menu
time.sleep(0.3)
# Get to command menu if mid-text
for _ in range(3):
    z(100)
    time.sleep(0.4)
shot("pokerogue_u2_preball.jpg")

# Navigate to Ball: try Right then Z
arrow("Right", 90)
time.sleep(0.25)
z(120)  # open Ball
time.sleep(0.6)
shot("pokerogue_u3_ball.jpg")

# Select first ball (top) and throw; confirm target if doubles
z(120)
time.sleep(0.5)
z(120)  # target
time.sleep(1.0)
# If catch anim / messages
for _ in range(12):
    z(100)
    time.sleep(0.5)
st = state()
log("AFTER_CATCH_ATTEMPT " + json.dumps(st))
shot("pokerogue_u4_catch.jpg")

# If still in battle (shiny not caught / wrong menu), try Ball path again via Down from Fight
# Fight is top-left; Down = Pokemon; Right = Ball. Retry Right path once more.
for attempt in range(2):
    t0 = ev("window.gameInfo.playTime")
    time.sleep(1.2)
    t1 = ev("window.gameInfo.playTime")
    w = ev("window.gameInfo.wave")
    if t1 != t0 or (w and w > 31):
        log("PROGRESS tick=%s->%s wave=%s" % (t0, t1, w))
        break
    log("RETRY_BALL attempt=%s" % attempt)
    # Back to command: Backspace then Z to Fight menu presence
    for _ in range(3):
        bs(100)
        time.sleep(0.2)
    for _ in range(2):
        z(100)
        time.sleep(0.35)
    arrow("Right", 90)
    time.sleep(0.25)
    z(120)
    time.sleep(0.5)
    # sometimes need Down to pick Ultra/better ball — stay on first
    z(120)
    time.sleep(0.4)
    z(120)
    time.sleep(0.8)
    for _ in range(10):
        z(100)
        time.sleep(0.45)
    shot("pokerogue_u5_retry%s.jpg" % attempt)

st = state()
log("POST_CATCH_STATE " + json.dumps(st))
shot("pokerogue_u6.jpg")

# 3) Confirm playTime advances — keep Z clearing rewards until tick or wave up
advanced = False
start_w = st.get("w") if st else 31
start_t = st.get("t") if st else 1716
for i in range(40):
    z(95)
    time.sleep(0.55)
    if i % 5 == 4:
        bs(90)
        time.sleep(0.2)
    if i % 3 == 0:
        st = state()
        log("PULSE " + json.dumps(st))
        if st and ((st.get("t") or 0) > start_t or (st.get("w") or 0) > start_w):
            advanced = True
            break

st = state()
log("FINAL_UNSTICK advanced=%s %s" % (advanced, json.dumps(st)))
shot("pokerogue_u7_final.jpg")

# Write status snapshot
(OUT / "pokerogue_farm_status.json").write_text(json.dumps({
    "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
    "event": "unstick_catch",
    "advanced": advanced,
    **(st or {})
}, indent=2), encoding="utf-8")

ws.close()
print("DONE_UNSTICK", flush=True)
