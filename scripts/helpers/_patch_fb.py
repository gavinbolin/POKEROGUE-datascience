import re
p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
def R(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
R('''        if "lure" in n: return 88  # deprioritised''','''        if "lure" in n and feebas: return -15  # FEEBAS: Lure/Super/Max Lure -> more doubles (below tiers/vouchers/vitamins/leppa)
        if "lure" in n: return 88  # deprioritised''')
R('''    HEAL = ["full restore",''','''    feebas = any(p.get("n") == "Feebas" for p in st.get("party") or [])
    HEAL = ["full restore",''')
R('''                            if "leppa" not in last_pick[0].lower() or w in lep_try:''','''                            fbi = next((j for j, p in enumerate(party) if p["n"] == "Feebas"), None)
                            if fbi is not None and "soothe bell" in last_pick[0].lower() and w not in fb_fall:
                                fb_fall.add(w); party_tries = 0; log("FEEBAS soothe bell failed/max on Feebas -> Zacian"); await set_cursor(party.index(z)); await Z(); continue
                            if "leppa" not in last_pick[0].lower() or w in lep_try:''')
R('''                        if last_pick[0] and "revive" in last_pick[0].lower() and dead is not None:
                            tgt = dead''','''                        if last_pick[0] and "revive" in last_pick[0].lower() and dead is not None:
                            tgt = dead
                        fbi = next((j for j, p in enumerate(party) if p["n"] == "Feebas"), None)
                        lpn = (last_pick[0] or "").lower()
                        if fbi is not None and (("soothe bell" in lpn and w not in fb_fall) or "rare candy" in lpn):
                            tgt = fbi
                            if same == 0: log(f"FEEBAS reward {last_pick[0]} -> Feebas slot {fbi}")''')
R('''                        if same == 0: log(f"release/party-full prompt {olabels} in {st.get('ph')} -> No (keep party)")
                        await set_cursor(olabels.index("No")); await asyncio.sleep(0.15); await Z()''','''                        np_ = len(st.get("party") or [])
                        ans = "Yes" if (0 < np_ < 6 and "Yes" in olabels) else "No"
                        if same == 0: log(f"release/party-full prompt {olabels} in {st.get('ph')} party={np_} -> {ans}")
                        await set_cursor(olabels.index(ans)); await asyncio.sleep(0.15); await Z()''')
R('''        if gi != "Classic": log("ABORT not Classic"); return''','''        if gi != "Classic": log("ABORT not Classic"); return
        fb_fall = set()
        try: _fb = await ev("(()=>{try{return window.__pr_cam.scene.getPlayerParty().some(p=>p.species&&p.species.speciesId===349||p.name==='Feebas')}catch(e){return String(e)}})()")
        except Exception as e: _fb = e
        log(f"FEEBAS rules active: feebas_in_party={_fb}")''')
open(p,"w",encoding="utf-8").write(s); print("ok")
