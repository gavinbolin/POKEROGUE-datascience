"""Start a fresh Classic run with Zacian via cdp.py. Usage: python newrun.py <slot 0-4> --yes
Title(reload) -> New Game -> Classic (idx 0, asserted; never Endless) -> Zacian(888) -> Start -> Yes -> slot -> overwrite Yes."""
import subprocess,sys,json
def c(*a):
    out=subprocess.run([sys.executable,"cdp.py",*a],capture_output=True,text=True).stdout.strip().splitlines(); return out
def js(e): return json.loads(c("js:"+e)[-1])
H="window.__pr_cam.scene.ui.getHandler()"
slot=int(sys.argv[1]); assert "--yes" in sys.argv and 0<=slot<=4
assert js(f"{H}.constructor.name")=="TitleUiHandler", "not at title (reload first)"
NG=js(f"({H}.config.options||[]).map(o=>o.label)").index("New Game")
js(f"(()=>{{{H}.setCursor({NG});return 1}})()");assert js(f"{H}.cursor")==NG;c("w0","shot:frames/newrun_01_title.png");c("z","w1")
assert js(f"({H}.config.options||[]).map(o=>o.label)[{H}.cursor]")=="Classic", "mode cursor not Classic"
c("shot:frames/newrun_02_mode.png","z","w2")
PARTY=[888]
if "--party" in sys.argv: PARTY=[int(x) for x in sys.argv[sys.argv.index("--party")+1].split(",")]
assert PARTY[0]==888, "Zacian must lead"
got=[]
for sp in PARTY:
    idx=js(f"{H}.filteredStarterIds.indexOf({sp})"); r,col=divmod(idx,9)
    a=js(f"{H}.cursor+{H}.scrollCursor*9"); r0,c0=divmod(a,9)
    c(*((["down"]*(r-r0) if r>=r0 else ["up"]*(r0-r))+(["right"]*(col-c0) if col>=c0 else ["left"]*(c0-col))))
    cur=js(f"{H}.filteredStarterIds[{H}.cursor+{H}.scrollCursor*9]")
    if cur!=sp: print("nav fail",sp,cur); continue
    c("z","w1","z","w1")
    p=js(f"{H}.partyStarterIds")
    if p and p[-1]==sp: got.append(sp)
    else:
        print("could not add",sp,"(cost?)"); c("x","w1")
    c("shot:frames/newrun_party_%d.png"%sp)
print("party",js(f"{H}.partyStarterIds"))
assert js(f"{H}.partyStarterIds")[0]==888
for _ in range(12):
    if js(f"{H}.startCursorObj.visible"): break
    c("right")
for _ in range(14):
    if js(f"{H}.startCursorObj.visible"): break
    c("down")
assert js(f"{H}.startCursorObj.visible"), "no Start cursor"
c("shot:frames/newrun_07_start.png","z","w1","z","w2")
assert js(f"{H}.constructor.name")=="SaveSlotSelectUiHandler"
c(*(["down"]*slot)); assert js(f"{H}.cursor+{H}.scrollCursor")==slot
c("shot:frames/newrun_10_slot.png","z","w1")
if js(f"{H}.constructor.name")=="ConfirmUiHandler": c("z")
c("w8","shot:frames/newrun_12_started.png")
print(js("[window.gameInfo.gameMode,window.gameInfo.wave]"))




