p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
def R(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
PJS = "(()=>{try{return window.__pr_cam.scene.getPlayerParty().some(p=>{const a=p.getAbility&&p.getAbility();const pa=p.getPassiveAbility&&p.hasPassive&&p.hasPassive()?p.getPassiveAbility():null;return [a,pa].some(x=>x&&(x.id===53||String(x.name).toLowerCase()==='pickup'))})}catch(e){return false}})()"
R('''    def rank(r):
        rank_inner = rank0(r); t = r.get("t")''','''    def rank(r):
        rank_inner = rank0(r); t = r.get("t")
        if "berry" in r["n"].lower() and not r.get("_x"):  # BERRY rule: any higher-tier non-berry beats a berry
            hi = [rank(dict(x, _x=1)) for x in rew if (x.get("t") or 0) > (t or 0) and "berry" not in x["n"].lower()]
            if hi: rank_inner = max(rank_inner, max(hi) + 0.5)''')
R('''                    i, why = pick_reward(st, rew_bad.get(w, set()))''','''                    if pk_w.get("w") != w: pk_w["w"] = w; pk_w["v"] = bool(await ev(PICKUP_JS))
                    i, why = pick_reward(st, rew_bad.get(w, set()))''')
R('''                        if fbi is not None and (("soothe bell"''','''                        if "berry" in lpn and not pk_w.get("v"):
                            pass  # BERRY rule: no Pickup -> berries get no extra lead priority (default target, skip-if-cannot-take unchanged)
                        elif "berry" in lpn:
                            tgt = party.index(z)  # Pickup present -> berries to the lead (transfer filters Pickup finds to mains)
                        if fbi is not None and (("soothe bell"''')
R('''        fb_fall = set()''','''        fb_fall = set(); pk_w = {}
        _pk = await ev(PICKUP_JS)''')
R('''log(f"FEEBAS rules active: feebas_in_party={_fb}")''','''log(f"FEEBAS rules active: feebas_in_party={_fb} berry_rule pickup_present={_pk}")''')
R('''VITAMINS = [''','''PICKUP_JS = %r
VITAMINS = [''' % PJS)
open(p,"w",encoding="utf-8").write(s); print("ok")
