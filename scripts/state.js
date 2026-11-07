(()=>{const bs=window.__pr_cam?.scene; if(!bs||!bs.ui) return {err:'noscene'};
const o={}; try{
const h=bs.ui.getHandler(); o.h=h?.constructor?.name; o.cur=h?.cursor; o.om=h?.optionsMode; o.opts=h?.optionsMode?(h.options||[]).slice(0,12):null;
const ph=bs.phaseManager?.getCurrentPhase?.(); o.ph=ph?.constructor?.name; o.fi=ph?.fieldIndex;
const cb=bs.currentBattle; o.wave=cb?.waveIndex; o.double=!!cb?.double; o.btype=cb?.battleType; o.trainer=!!cb?.trainer||cb?.battleType===1;
const party=bs.getPlayerParty(); o.party=party.map((p,i)=>({i,n:p.name,sp:p.species?.speciesId,stt:(p.status&&p.status.effect)||0,ho:(bs.modifiers||[]).filter(m=>m.pokemonId===p.id&&m.type&&/^(FLAME|TOXIC)_ORB$/.test(m.type.id)).map(m=>m.type.id),hp:p.hp,mx:p.getMaxHp?.(),f:!!p.isOnField?.(),fs:p.fusionSpecies?p.fusionSpecies.speciesId:null}));
const en=(bs.getEnemyField?.()||bs.getEnemyParty()).filter(e=>e&&e.hp>0&&(e.isOnField?.()??true));
o.enemy=en.map(e=>({n:e.name,t:e.getTypes(),sh:!!e.shiny,v:(e.shiny?(e.variant??null):null),lv:e.level,sid:e.species?.speciesId,ab:e.getAbility?.()?.name,gr:e.isGrounded?.()}));
const fi=(o.fi??0); const user=(bs.getPlayerField?.()||[])[fi]||party[0]; o.user=user?.name;
o.moves=(user?.getMoveset?.()||user?.moveset||[]).map((m,i)=>{const mv=m.getMove(); const left=m.getMovePp()-m.ppUsed; let effs=en.map(e=>{let x=1,gm=false;try{x=e.getAttackTypeEffectiveness(mv.type,user)}catch(_){} try{const g=e.getMoveEffectiveness(user,mv,false,true);if(typeof g==='number'&&mv.category!==2){x=g;gm=true}}catch(_){} if(!gm&&mv.id===573&&(e.getTypes?.()||[]).includes(11))x=x*4; if(mv.type===4&&e.isGrounded&&!e.isGrounded())x=0; return x});
 return {i,n:m.getName(),type:mv.type,pow:mv.power,cat:mv.category,left,max:m.getMovePp(),effs,stab:(user.getTypes()||[]).includes(mv.type)}});
if(o.h==='ModifierSelectUiHandler'){o.row=h.rowCursor; const PM=party.find(p=>(window.__pr_prim||[888]).includes(p.species?.speciesId))||party[0];const MC=(PM.getMoveset()[0]||{}).constructor;o.ptm=(PM&&PM.compatibleTms)||[];o.rew=(h.options||[]).map((x,i)=>{const ty=x.modifierTypeOption?.type;const r={i,n:ty?.name,id:ty?.id,t:(ty?.tier??x.modifierTypeOption?.tier??null)};try{if(ty&&ty.evolutionItem!==undefined&&ty.selectFilter){r.evo=party.map((p,k)=>{try{return ty.selectFilter(p)?-1:k}catch(e){return -1}}).filter(k=>k>=0)}}catch(e){};try{if(ty&&ty.moveId!==undefined&&MC){const mv=new MC(ty.moveId).getMove();r.mv=ty.moveId;r.mvn=mv.name;r.mvt=mv.type;r.mvp=mv.power;r.mvc=mv.category}}catch(e){};return r}); o.shop=(h.shopOptionsRows||[]).flat().map((x,i)=>({i,n:x.modifierTypeOption?.type?.name,c:x.modifierTypeOption?.cost})); o.money=bs.money;}
o.balls=bs.pokeballCounts;
}catch(e){o.err=String(e)} return o})()
