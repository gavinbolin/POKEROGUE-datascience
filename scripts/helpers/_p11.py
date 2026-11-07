p="pr_farm17.py"; L=open(p,encoding="utf-8").read().split("\n")
a=next(k for k,x in enumerate(L) if "hv = br <= -35" in x)
b=next(k for k,x in enumerate(L) if "(cap 20%), best rank" in x)
I=" "*20
new='''ppc = i is not None and br <= -10 and any(k in str((st.get("rew") or [{}]*(i+1))[i].get("n", "")).lower() for k in PP_ITEMS)
hv = br <= -35 or ppc
want = br <= -30 or ppc
no_hi = not any((r_.get("t") or 0) >= 3 for r_ in (st.get("rew") or []))
if i is not None and reroll_n.get(w, 0) < 5 and ((not hv and cheap_n.get(w, 0) < REROLL_CHEAP_MAX) or (no_hi and not want)):
    ri = await ev("(()=>{const s=window.__pr_cam.scene;const h=s.ui.getHandler();const ph=s.phaseManager.getCurrentPhase();let c=h.rerollCost;try{if(c===undefined||c<0)c=ph.getRerollCost(!!s.lockModifierTiers)}catch(e){};return {money:s.money,cost:c}})()") or {}
    money, cost = ri.get("money"), ri.get("cost")
    if isinstance(money, (int, float)) and isinstance(cost, (int, float)) and cost >= 0:
        _m0 = shop_open.setdefault(w, money)
        _floor = max(SHOP_RESERVE_FRAC * _m0, SHOP_MIN_RESERVE)
        _ok = cost <= money and money - cost >= _floor
        _cap = SHOP_MAX_SPEND_FRAC * _m0 - (_m0 - money)
        tag = None
        if _ok and not hv and cheap_n.get(w, 0) < REROLL_CHEAP_MAX and cost < REROLL_CHEAP_FRAC * money:
            cheap_n[w] = cheap_n.get(w, 0) + 1; tag = f"REROLL cheap cost={cost} money={money} ({cost/max(1,money):.0%})"
        elif _ok and no_hi and not want and cost <= _cap:
            tag = f"REROLL nothing>ultra cost={cost} money={money} cap={int(_cap)}"
        if tag:
            reroll_n[w] = reroll_n.get(w, 0) + 1
            log(f"{tag} #{reroll_n[w]} w{w} best was rank {br}: {why[:160]}")
            await ev("(()=>{const h=window.__pr_cam.scene.ui.getHandler();h.setRowCursor(0);h.setCursor(0);})()")
            await asyncio.sleep(0.25); await Z(); await asyncio.sleep(1.0)
            for _ in range(4): await ev(STEP_JS)
            last_rew_wave = None; rew_bad.pop(w, None); continue
        if reroll_log.get(w) != (money, cost):
            reroll_log[w] = (money, cost); log(f"no reroll w{w}: cost {cost} / money {money} floor {int(_floor)} cap {int(_cap)} hv={hv} want={want} no_hi={no_hi}")
        cheap_n[w] = REROLL_CHEAP_MAX; reroll_n[w] = 5  # don't re-query this screen'''
L[a:b+1]=[I+x for x in new.split("\n")]
s="\n".join(L)
s=s.replace('log(f"REROLL cheap: <','log("REROLL nothing>ultra: within SHOP caps, max 5/screen"); log(f"REROLL cheap: <',1)
open(p,"w",encoding="utf-8").write(s); print("ok")
