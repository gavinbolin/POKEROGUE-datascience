(()=>{const s=window.__pr_cam.scene;const h=s.ui.handlers.find(x=>x&&x.constructor.name=='ModifierSelectUiHandler');
const wv=s.currentBattle?s.currentBattle.waveIndex:0;const vis=!!(h&&h.transferButtonContainer&&h.transferButtonContainer.visible);const out={wv,vis,moved:[],failed:[]};out.x1=true;
const party=s.getPlayerParty();const z=party.find(p=>p.species&&p.species.speciesId===888);if(!z){out.err='no zacian';return out}
const SRC=['Linoone','Zigzagoon','Boltund','Yamper'];
for(const p of party){if(p===z||!SRC.includes(p.species.name))continue;
 const mods=s.findModifiers(m=>m.pokemonId===p.id&&m.isTransferable!==false);
 for(const m of mods){const nm=m.type.name;const q=m.stackCount;let ok=false;
  try{const mx=m.getMaxStackCount?m.getMaxStackCount():99;const ex=s.findModifier(o=>o.pokemonId===z.id&&o.matchType&&o.matchType(m));
   if(ex&&ex.stackCount>=mx){out.failed.push(nm+':zacian max');continue}
   ok=s.canTransferHeldItemModifier?true:false;}catch(e){out.failed.push(nm+':'+e);continue}
  (ok?out.moved:out.failed).push(p.species.name+'>'+nm+' x'+q);}}
return out})()