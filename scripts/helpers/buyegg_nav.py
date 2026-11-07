import subprocess,sys,json
def c(*a): return subprocess.run([sys.executable,"cdp.py",*a],capture_output=True,text=True).stdout.strip().splitlines()
def js(e): return json.loads(c("js:"+e)[-1])
H="window.__pr_cam.scene.ui.getHandler()"
NG=js(f"({H}.config.options||[]).map(o=>o.label)").index("New Game")
js(f"(()=>{{{H}.setCursor({NG});return 1}})()");c("z","w1")
assert js(f"({H}.config.options||[]).map(o=>o.label)[{H}.cursor]")=="Classic"
c("z","w2")
idx=js(f"{H}.filteredStarterIds.indexOf(888)"); r,col=divmod(idx,9)
a=js(f"{H}.cursor+{H}.scrollCursor*9"); r0,c0=divmod(a,9)
c(*((["down"]*(r-r0) if r>=r0 else ["up"]*(r0-r))+(["right"]*(col-c0) if col>=c0 else ["left"]*(c0-col))))
print("cur",js(f"{H}.filteredStarterIds[{H}.cursor+{H}.scrollCursor*9]"))
c("z","w1")
print(js(f"[{H}.constructor.name, (window.__pr_cam.scene.ui.handlers.find(x=>x.constructor.name=='OptionSelectUiHandler')?.config?.options||[]).map(o=>o.label)]"))
