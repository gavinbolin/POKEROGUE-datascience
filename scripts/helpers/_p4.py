p="state.js"; s=open(p,encoding="utf-8").read()
a="let x=1;try{x=e.getAttackTypeEffectiveness(mv.type,user)}catch(_){}"
assert s.count(a)==1
s=s.replace(a,"let x=1,gm=false;try{x=e.getAttackTypeEffectiveness(mv.type,user)}catch(_){} try{const g=e.getMoveEffectiveness(user,mv,false,true);if(typeof g==='number'&&mv.category!==2){x=g;gm=true}}catch(_){} if(!gm&&mv.id===573&&(e.getTypes?.()||[]).includes(11))x=x*4;")
open(p,"w",encoding="utf-8").write(s)
p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
a='''                        log(f"w{w} {st.get('user')} -> {m['n']} eff={m['effs']}'''
assert s.count(a)==1, s.count(a)
s=s.replace(a,'''                        if m["n"] == "Freeze-Dry" and max(m.get("effs") or [1]) >= 2: log(f"FREEZE-DRY vs {[e['n'] for e in st.get('enemy') or []]} eff={max(m['effs'])}")
'''+a)
s=s.replace('log("EVIOLITE rule:','log("FREEZE-DRY: game getMoveEffectiveness (+573 vs Water fallback)"); log("EVIOLITE rule:',1)
open(p,"w",encoding="utf-8").write(s); print("ok")
