s=open('pr_farm16.py',encoding='utf-8').read()
a='''                    else:
                        log(f"stray party UI in {ph} - back"); await X(); await asyncio.sleep(0.3); continue'''
assert a in s
s=s.replace(a,'''                    elif ph == "MysteryEncounterPhase":
                        # ME option asks for a party member: offer a non-Zacian ally (never risk Zacian)
                        tgt = next((p["i"] for p in party if p["hp"] > 0 and p["n"] != "Zacian"), None)
                        want_opt = None
                        if same == 0: log(f"ME party select -> slot {tgt}")
                        if tgt is None: me_noparty.add(w); await X(); await asyncio.sleep(0.3); continue
                    else:
                        log(f"stray party UI in {ph} - back"); await X(); await asyncio.sleep(0.3); continue''')
b='''                        else:
                            k = opts.index(want_opt) if want_opt in opts else None'''
assert b in s
s=s.replace(b,'''                        elif want_opt is None:
                            k = 0 if opts and opts[0] != -1 else None
                        else:
                            k = opts.index(want_opt) if want_opt in opts else None''')
c="return k})()\") or 0"
assert c in s
s=s.replace(c,"return k})()\") or 0\n                    if w in me_noparty and n_opt > 1: n_opt = 1")
s=s.replace('faint_n = 0\n','faint_n = 0; me_noparty = set()\n',1)
open('pr_farm16.py','w',encoding='utf-8').write(s)
