(()=>{try{const L=window.__pr_cam.scene.game.loop;if(document.visibilityState!=='hidden')return {hidden:false,frame:L.frame};
let t=Math.max(L.lastTime||0,L.now||0);for(let k=0;k<45;k++){t+=16.7;L.step(t)}return {hidden:true,frame:L.frame}}catch(e){return String(e.stack||e)}})()
