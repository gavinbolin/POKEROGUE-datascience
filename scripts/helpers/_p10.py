p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
def R(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
R('''                    if br >= 80 and reroll_n.get(w, 0) < 5:''','''                    hv = br <= -35 or (i is not None and br <= -10 and any(k in str((st.get("rew") or [{}]*(i+1))[i].get("n", "")).lower() for k in PP_ITEMS))
                    cheap_try = (not hv) and i is not None and cheap_n.get(w, 0) < REROLL_CHEAP_MAX
                    if (br >= 80 and reroll_n.get(w, 0) < 5) or cheap_try:''')
R('''                        if isinstance(money, (int, float)) and isinstance(cost, (int, float)) and 0 <= cost <= 0.2 * money and cost <= money:''','''                        _m0 = shop_open.get(w, money) if isinstance(money, (int, float)) else 0
                        _floor = max(SHOP_RESERVE_FRAC * (_m0 or 0), SHOP_MIN_RESERVE)
                        _ok = isinstance(money, (int, float)) and isinstance(cost, (int, float)) and 0 <= cost <= money and money - cost >= _floor
                        if _ok and br < 80 and cost < REROLL_CHEAP_FRAC * money:
                            cheap_n[w] = cheap_n.get(w, 0) + 1; reroll_n[w] = reroll_n.get(w, 0) + 1
                            log(f"REROLL cheap cost={cost} money={money} ({cost/max(1,money):.0%}) #{cheap_n[w]} best was rank {br}")
                            await ev("(()=>{const h=window.__pr_cam.scene.ui.getHandler();h.setRowCursor(0);h.setCursor(0);})()")
                            await asyncio.sleep(0.25); await Z(); await asyncio.sleep(1.0)
                            for _ in range(4): await ev(STEP_JS)
                            last_rew_wave = None; rew_bad.pop(w, None); continue
                        if br < 80: cheap_n[w] = REROLL_CHEAP_MAX  # not cheap enough: stop trying this screen
                        if br < 80: pass
                        elif _ok and cost <= 0.2 * money:''')
R('''reroll_n = {}; reroll_log = {};''','''reroll_n = {}; reroll_log = {}; cheap_n = {};''')
R('''PP_CONSERVE_ABS = 5''','''REROLL_CHEAP_FRAC = 0.10
REROLL_CHEAP_MAX = 3
PP_CONSERVE_ABS = 5''')
R('''log(f"PP CONSERVE: low''','''log(f"REROLL cheap: <{REROLL_CHEAP_FRAC:.0%} of money, max {REROLL_CHEAP_MAX}/screen, respects shop floor"); log(f"PP CONSERVE: low''')
open(p,"w",encoding="utf-8").write(s); print("ok")
