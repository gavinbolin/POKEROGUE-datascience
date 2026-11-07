(()=>Object.keys(window).filter(k=>k.startsWith("__pr")).map(k=>[k,window[k]?.scene?.sys?.settings?.key||window[k]?.sys?.settings?.key]))()
