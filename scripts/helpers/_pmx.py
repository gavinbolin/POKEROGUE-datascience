p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
old='''                    if same == 0: log(f"mystery encounter w{w}: {n_opt} options -> TOP option (0)")
                    await set_cursor(0); await Z()'''
new='''                    meinfo = await ev("""(()=>{const s=window.__pr_cam.scene,me=s.currentBattle.mysteryEncounter;const t=[];const walk=(o,d)=>{if(!o||d>8||o.visible===false)return;if(o.text!==undefined&&String(o.text).trim())t.push(String(o.text));(o.list||[]).forEach(c=>walk(c,d+1))};walk(s.ui,0);return {key:me&&me.localizationKey||'',type:me&&me.encounterType,txt:t.join(' | ')}})()""") or {}
                    mekey_s = str(meinfo.get("key", "")).lower(); metxt = str(meinfo.get("txt", "")).lower()
                    BLOCK_ME = ("weirddream", "weird_dream", "weird dream")
                    XFORM_WORDS = ("transform", "replace your", "change your pok", "changes your pok", "your team will", "swap your")
                    pick = 0
                    if any(b in mekey_s for b in BLOCK_ME) or any(b in metxt for b in BLOCK_ME[2:]):
                        pick = max(0, n_opt - 1); why = "BLOCKLIST party-changing ME"
                    elif any(xw in metxt for xw in XFORM_WORDS):
                        pick = max(0, n_opt - 1); why = "option text mentions transforming team"
                    else:
                        why = "TOP option"
                    if same == 0: log(f"mystery encounter w{w} key={meinfo.get('key')} type={meinfo.get('type')}: {n_opt} options -> {why} ({pick})")
                    await set_cursor(pick); await Z()'''
assert old in s; s=s.replace(old,new); open(p,"w",encoding="utf-8").write(s); print("ok")
