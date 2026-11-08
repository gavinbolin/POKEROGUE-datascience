Set-Location $env:TEMP\prfarm
Write-Output '=== NR_PICK ==='
python nr_pick.py 800,63,263,401,327
Write-Output '=== PARTY STATUS ==='
python _re2.py status
Write-Output '=== SLOT PROBE VIA GX ==='
python gx.py "js:(()=>{const h=window.__pr_cam.scene.ui.getHandler();return JSON.stringify({h:h.constructor.name,party:h.partyStarterIds,startVis:!!h.startCursorObj?.visible})})()"
Write-Output '=== TRYSTART ==='
python gx.py "js:(()=>{const h=window.__pr_cam.scene.ui.getHandler(); if(h.tryStart){h.tryStart(); return 'tryStart'} return 'no tryStart '+h.constructor.name})()"
Start-Sleep -Seconds 2
python gx.py "js:(()=>{const h=window.__pr_cam.scene.ui.getHandler();return JSON.stringify({h:h.constructor.name,c:h.cursor,o:h.config?.options?.map(o=>o.label)})})()"
Write-Output '=== CONFIRM YES p:5 ==='
python gx.py p:5
Start-Sleep -Seconds 2
python gx.py "js:(()=>{const h=window.__pr_cam.scene.ui.getHandler();const slots=(h.sessionSlots||[]).map(s=>({id:s.slotId,has:!!s.hasData,wave:s.waveIndex,mode:s.gameMode}));return JSON.stringify({h:h.constructor.name,c:h.cursor+ (h.scrollCursor||0),slots:slots})})()"
