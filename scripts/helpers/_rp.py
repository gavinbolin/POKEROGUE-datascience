import re
p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
a='        if heal_need and any(k in n for k in HEAL):'
assert a in s
s=s.replace(a,'        if z and z["hp"] <= 0 and ("revive" in n or "sacred ash" in n): return -50  # revive patch: Zacian down -> revive tops all\n'+a,1)
old='''                    log(f"ZACIAN FAINT hp=0/{z.get('mx')} onField={z['f']} w{st.get('wave')} ph={st.get('ph')} foes={[(e['n'],e.get('ab')) for e in st.get('enemy') or []]} lastHP={last_zlog}")
                    await shot(FRAMES, "zacian_faint"); break'''
assert old in s
new='''                    if any(p["hp"] > 0 for p in party if p["n"] != "Zacian"):
                        if faint_n == 4:
                            log(f"ZACIAN FAINT w{st.get('wave')} - partners alive, keep fighting + revive on rewards")
                            await shot(FRAMES, "zacian_faint")
                        faint_n = 5
                    else:
                        log(f"ZACIAN FAINT hp=0/{z.get('mx')} onField={z['f']} w{st.get('wave')} ph={st.get('ph')} foes={[(e['n'],e.get('ab')) for e in st.get('enemy') or []]} lastHP={last_zlog}")
                        await shot(FRAMES, "zacian_faint"); break
                else: faint_n = 0'''
s=s.replace(old,new,1)
s=s.replace('''                    await shot(FRAMES, "zacian_faint"); break
                faint_n = 0
''','''                    await shot(FRAMES, "zacian_faint"); break
''',1) if False else s
s=s.replace('''                else: faint_n = 0
                faint_n = 0
''','''                else: faint_n = 0
''',1)
s=s.replace('''                        if last_pick[0] and "revive" in last_pick[0].lower() and dead is not None:''','''                        if z and z["hp"] <= 0: dead = party.index(z)
                        if last_pick[0] and "revive" in last_pick[0].lower() and dead is not None:''',1)
open(p,"w",encoding="utf-8").write(s)
