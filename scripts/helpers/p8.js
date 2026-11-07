(()=>{const s=window.__pr_cam.scene;const g=s.game;return {frame:g.loop.frame,now:g.loop.now,time:s.time.now,tw:s.tweens.getTweens().slice(0,3).map(t=>t.progress)}})()
