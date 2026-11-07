import re
p="pr_farm17.py"; s=open(p,encoding="utf-8",newline="").read(); s=s.replace("\r\n","\n")
old='                elif h == "ModifierSelectUiHandler":\n                    st["zmoves"]'
new='''                elif h == "ModifierSelectUiHandler":
                    if xfer_done.get("w") != w:
                        xfer_done["w"] = w  # one attempt per wave, never loops
                        try:
                            xr = await ev(XFER_JS)
                            if xr and (xr.get("vis") or xr.get("moved") or xr.get("failed")): log(f"TRANSFER w{w}: {xr}")
                        except Exception as e:
                            log(f"TRANSFER w{w} error {e}")
                    st["zmoves"]'''
assert s.count(old)==1; s=s.replace(old,new)
js='''xfer_done = {}
XFER_JS = r"""(()=>{const s=window.__pr_cam.scene;const h=s.ui.handlers.find(x=>x&&x.constructor.name=='ModifierSelectUiHandler');
const vis=!!(h&&h.transferButtonContainer&&h.transferButtonContainer.visible);const out={vis,moved:[],failed:[]};if(!vis)return out;
const party=s.getPlayerParty();const z=party.find(p=>p.species&&p.species.speciesId===888);if(!z){out.err='no zacian';return out}
const SRC=['Linoone','Zigzagoon','Boltund','Yamper'];
for(const p of party){if(p===z||!SRC.includes(p.species.name))continue;
 const mods=s.findModifiers(m=>m.pokemonId===p.id&&m.isTransferable!==false);
 for(const m of mods){const nm=m.type.name;const q=m.stackCount;let ok=false;
  try{const mx=m.getMaxStackCount?m.getMaxStackCount():99;const ex=s.findModifier(o=>o.pokemonId===z.id&&o.matchType&&o.matchType(m));
   if(ex&&ex.stackCount>=mx){out.failed.push(nm+':zacian max');continue}
   ok=s.tryTransferHeldItemModifier(m,z,false,q,true,true);}catch(e){out.failed.push(nm+':'+e);continue}
  (ok?out.moved:out.failed).push(p.species.name+'>'+nm+' x'+q);}}
try{s.updateModifiers(true)}catch(e){}return out})()"""

'''
i=s.index("\nasync def "); s=s[:i+1]+js+s[i+1:]
open(p,"w",encoding="utf-8",newline="\r\n").write(s)
