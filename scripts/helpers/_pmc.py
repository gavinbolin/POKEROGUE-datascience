import re
p="pr_farm17.py";s=open(p,encoding="utf-8").read()
old='''                    else:
                        if same == 0: log(f"option select in {st.get('ph')} opts={olabels} - take default")
                        await Z()'''
new='''                    else:
                        clean = [re.sub(r"\\[/?[a-z]+(=[^\\]]*)?\\]", "", str(o)).strip() for o in olabels]
                        mekey = (st.get("ph"), tuple(clean)); globals().setdefault("_me_loop", {})
                        _ml = globals()["_me_loop"]; _ml[mekey] = _ml.get(mekey, 0) + 1
                        if clean and "Cancel" in clean and ("Mystery" in str(st.get("ph")) or len(clean) >= 3):
                            log(f"option select in {st.get('ph')} opts={clean} -> Cancel (no teach)")
                            await set_cursor(clean.index("Cancel")); await asyncio.sleep(0.15); await Z()
                        elif _ml[mekey] > 3 and clean:
                            log(f"option select loop x{_ml[mekey]} in {st.get('ph')} opts={clean} -> last option")
                            await set_cursor(len(clean) - 1); await asyncio.sleep(0.15); await Z()
                        else:
                            if same == 0: log(f"option select in {st.get('ph')} opts={clean} - take default")
                            await Z()'''
assert old in s; s=s.replace(old,new)
if not re.search(r"^import re\b|^import .*\bre\b",s,re.M): s="import re\n"+s
open(p,"w",encoding="utf-8").write(s)
