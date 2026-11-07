(()=>{const bs=window.__pr_cam?.scene; if(!bs) return 'none'; const o={};
try{o.mode=bs.ui?.mode; o.handler=bs.ui?.getHandler?.()?.constructor?.name; o.cursor=bs.ui?.getHandler?.()?.cursor; o.double=bs.currentBattle?.double; o.wave=bs.currentBattle?.waveIndex; o.phase=bs.phaseManager?.getCurrentPhase?.()?.constructor?.name ?? bs.getCurrentPhase?.()?.constructor?.name;
o.enemy=(bs.getEnemyParty?.()||[]).map(p=>({n:p.name,t:p.getTypes?.(),sh:p.shiny,hp:p.hp,ab:p.getAbility?.()?.name, fly:p.isGrounded?.()}));
o.pp=(bs.getPlayerParty?.()[0]?.moveset||[]).map(m=>({n:m.getName?.(),max:m.getMovePp?.(),used:m.ppUsed}));
const h=bs.ui?.getHandler?.(); o.hkeys=h?Object.keys(h).slice(0,60):null; o.opts=h?.options?.map?.(x=>x?.type?.name||x?.type?.localeKey||x?.type?.constructor?.name);
}catch(e){o.err=String(e)} return o})()
