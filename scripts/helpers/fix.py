import pathlib
p=pathlib.Path("pr_farm17.py");s=p.read_text(encoding="utf-8")
old="const vis=!!(h&&h.transferButtonContainer&&h.transferButtonContainer.visible);const out={vis,moved:[],failed:[]};if(!vis)return out;"
new="const wv=s.currentBattle?s.currentBattle.waveIndex:0;const vis=!!(h&&h.transferButtonContainer&&h.transferButtonContainer.visible);const out={wv,vis,moved:[],failed:[]};if(wv%10!==1)return out;out.x1=true;"
assert old in s; s=s.replace(old,new)
o2='if xr and (xr.get("vis") or xr.get("moved") or xr.get("failed")):'
assert o2 in s; s=s.replace(o2,'if xr and (xr.get("x1") or xr.get("moved") or xr.get("failed")):')
p.write_text(s,encoding="utf-8")
j=s.split('XFER_JS = r"""')[1].split('"""')[0]
# dry-run version: no transfer, ignore wave gate
d=j.replace("if(wv%10!==1)return out;","").replace("ok=s.tryTransferHeldItemModifier(m,z,false,q,true,true);","ok=s.canTransferHeldItemModifier?true:false;").replace("try{s.updateModifiers(true)}catch(e){}","")
open("xfer_dry.js","w",encoding="utf-8").write(d)
