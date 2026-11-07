p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
a='''                    if same == 0: log(f"option select in {st.get('ph')} - take default")
                    await Z()
'''
b='''                    olabels = await ev("(()=>{const h=window.__pr_cam.scene.ui.getHandler();return (h.config&&h.config.options||[]).map(o=>o.label)})()") or []
                    if h == "OptionSelectUiHandler" and olabels and olabels[0] == "Summary" and "No" in olabels:
                        if same == 0: log(f"release/party-full prompt {olabels} in {st.get('ph')} -> No (keep party)")
                        await set_cursor(olabels.index("No")); await asyncio.sleep(0.15); await Z()
                    else:
                        if same == 0: log(f"option select in {st.get('ph')} opts={olabels} - take default")
                        await Z()
'''
assert a in s; s=s.replace(a,b); open(p,"w",encoding="utf-8").write(s); print("ok")
