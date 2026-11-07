(()=>{const o={v:Phaser.VERSION};const hooks=[['cam',Phaser.Cameras?.Scene2D?.Camera?.prototype,'preRender'],['tw',Phaser.Tweens?.TweenManager?.prototype,'update'],['kb',Phaser.Input?.Keyboard?.KeyboardPlugin?.prototype,'update'],['sp',Phaser.Scenes?.ScenePlugin?.prototype,'update']];
for(const [n,P,f] of hooks){ if(P&&P[f]&&!P['__h'+f]){const old=P[f];P['__h'+f]=1;P[f]=function(...a){window['__pr_'+n]=this;return old.apply(this,a)}} }
o.got=Object.keys(window).filter(k=>k.startsWith('__pr'));return o})()
