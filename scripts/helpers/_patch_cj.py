p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
def R(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
R('''        if "voucher" in n:''','''        if "candy jar" in n or "rare candy" in n: return -55  # CANDY priority: just below ROGUE/MASTER, above vouchers
        if "voucher" in n:''')
R('''berry_rule pickup_present={_pk}")''','''berry_rule pickup_present={_pk}"); log("CANDY priority: Candy Jar/Rare Candy top (-55, below Master/Rogue tier, above vouchers)")''')
open(p,"w",encoding="utf-8").write(s); print("ok")
