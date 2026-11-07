p="state.js"; s=open(p,encoding="utf-8").read()
a="sp:p.species?.speciesId,"; assert s.count(a)==1
s=s.replace(a,"sp:p.species?.speciesId,stt:(p.status&&p.status.effect)||0,"); open(p,"w",encoding="utf-8").write(s)
p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
def R(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
R('''VITAMINS = [''','''# SHOP (proactive buys on the reward screen, before the free reward)
SHOP_MAX_SPEND_FRAC = 0.5   # max share of money (at screen open) spent per reward screen
SHOP_RESERVE_FRAC = 0.25    # never drop below this share of money at screen open
SHOP_MIN_RESERVE = 0        # absolute money floor
SHOP_HURT = 0.85            # buy a potion when a role mon is below this HP ratio
SHOP_JS = """(()=>{try{const s=window.__pr_cam.scene,h=s.ui.getHandler();const R=h.shopOptionsRows||[],L=R.length,o=[];R.forEach((row,k)=>row.forEach((x,c)=>{const t=x.modifierTypeOption;o.push({r:L-k+1,c,n:t.type.name,cost:t.cost})}));return {money:s.money,items:o}}catch(e){return {err:String(e)}}})()"""
def shop_plan(party, z, sec, items, money, budget):
    def heal_amt(n, mx):
        n = n.lower()
        if n == "potion": return max(20, mx * 0.1)
        if n == "super potion": return max(50, mx * 0.25)
        if n == "hyper potion": return max(200, mx * 0.5)
        if n in ("max potion", "full restore"): return mx
        return 0
    ok = [it for it in items if 0 < it["cost"] <= budget and it["cost"] <= money]
    for p in [x for x in (z, sec) if x]:
        if p["hp"] <= 0:
            rv = [it for it in ok if it["n"].lower() in ("max revive", "revive")]
            if rv: return max(rv, key=lambda it: it["cost"]), p, "revive"
            continue
        mx = p.get("mx") or 1; miss = mx - p["hp"]; r = p["hp"] / mx
        if p.get("stt"):
            if r < SHOP_HURT:
                fr = [it for it in ok if it["n"].lower() == "full restore"]
                if fr: return fr[0], p, "status+hurt"
            fh = [it for it in ok if it["n"].lower() == "full heal"]
            if fh: return fh[0], p, "status"
        if r < SHOP_HURT:
            need = miss if r < 0.3 else min(miss, 0.5 * miss + 0.15 * mx)
            pots = sorted([it for it in ok if heal_amt(it["n"], mx) > 0], key=lambda it: it["cost"])
            good = [it for it in pots if heal_amt(it["n"], mx) >= need]
            pick = good[0] if good else (pots[-1] if pots else None)
            if pick and heal_amt(pick["n"], mx) >= min(miss, 0.1 * mx): return pick, p, "hurt"
    return None
VITAMINS = [''')
R('''                elif h == "ModifierSelectUiHandler":
''','''                elif h == "ModifierSelectUiHandler":
                    if shop_pend[0]:
                        sp_ = shop_pend[0]; shop_pend[0] = None; shop_tgt[0] = None
                        m2 = await ev("window.__pr_cam.scene.money")
                        if isinstance(m2, (int, float)) and m2 < sp_["money"]:
                            log(f"SHOP BUY (proactive) {sp_['n']} -> {sp_['mon']} cost={sp_['cost']} money={sp_['money']}->{m2} cap={sp_['cap']} ({sp_['why']})")
                        else:
                            shop_fail[w] = shop_fail.get(w, 0) + 1; log(f"SHOP buy {sp_['n']} -> {sp_['mon']} not charged (money {m2}) - fail #{shop_fail[w]}")
                    if shop_fail.get(w, 0) < 2 and shop_n.get(w, 0) < 8:
                        sh = await ev(SHOP_JS) or {}
                        if sh.get("items") is not None and isinstance(sh.get("money"), (int, float)):
                            if w not in shop_open: shop_open[w] = sh["money"]
                            m0 = shop_open[w]; spent = m0 - sh["money"]
                            floor = max(SHOP_RESERVE_FRAC * m0, SHOP_MIN_RESERVE)
                            cap = int(max(0, min(SHOP_MAX_SPEND_FRAC * m0 - spent, sh["money"] - floor)))
                            pl = shop_plan(party, z, role(party, SECONDARY), sh["items"], sh["money"], cap)
                            if pl:
                                it, pm, why_ = pl; shop_n[w] = shop_n.get(w, 0) + 1
                                shop_pend[0] = {"n": it["n"], "mon": pm["n"], "cost": it["cost"], "money": sh["money"], "cap": cap, "why": why_}
                                shop_tgt[0] = pm["i"]; last_pick[0] = it["n"]
                                await ev(f"(()=>{{const h=window.__pr_cam.scene.ui.getHandler();h.setRowCursor({it['r']});h.setCursor({it['c']});}})()")
                                await asyncio.sleep(0.25)
                                chk = await ev("(()=>{const h=window.__pr_cam.scene.ui.getHandler();const v=h.shopOptionsRows.at(-(h.rowCursor-1));return v&&v[h.cursor]&&v[h.cursor].modifierTypeOption.type.name})()")
                                if chk != it["n"]:
                                    log(f"SHOP cursor mismatch {chk} != {it['n']} - skip shop this wave"); shop_pend[0] = None; shop_tgt[0] = None; shop_fail[w] = 9
                                else:
                                    await Z(); await asyncio.sleep(0.6); continue
''')
R('''                    if tgt is None: await X(); continue''','''                    if ph == "SelectModifierPhase" and shop_tgt[0] is not None:
                        tgt = shop_tgt[0]
                        if same == 0: log(f"SHOP target slot {tgt} for {last_pick[0]}")
                    if tgt is None: await X(); continue''')
R('''reroll_n = {}; reroll_log = {};''','''reroll_n = {}; reroll_log = {}; shop_pend = [None]; shop_tgt = [None]; shop_fail = {}; shop_n = {}; shop_open = {};''')
R('''log("SWORD: Rusted''','''log(f"SHOP proactive: spend<={SHOP_MAX_SPEND_FRAC:.0%} reserve>={SHOP_RESERVE_FRAC:.0%} floor={SHOP_MIN_RESERVE} hurt<{SHOP_HURT:.0%}"); log("SWORD: Rusted''')
open(p,"w",encoding="utf-8").write(s); print("ok")
