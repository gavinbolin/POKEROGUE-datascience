(()=>{const sm=window.__prSM; if(!sm) return 'nosm'; const s=sm.scenes.map(x=>x.sys.settings.key); const bs=sm.scenes.find(x=>x.ui||x.currentBattle)||sm.scenes[0];
const o={scenes:s, keys:Object.keys(bs).slice(0,120)}; try{o.mode=bs.ui?.mode; o.handler=bs.ui?.getHandler?.()?.constructor?.name; o.double=bs.currentBattle?.double; o.enemy=(bs.getEnemyParty?.()||[]).map(p=>({n:p.name,t:p.getTypes?.(),sh:p.shiny,hp:p.hp,ab:p.getAbility?.()?.name}));
o.pp=(bs.getPlayerParty?.()[0]?.moveset||[]).map(m=>({n:m.getName?.(),pp:m.getMovePp?.()-m.ppUsed}));}catch(e){o.err=String(e)} return o})()
