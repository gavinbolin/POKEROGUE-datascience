import json, urllib.request, importlib.util, os, itertools, time
U="http://127.0.0.1:8766"
def post(p,b):
    r=urllib.request.Request(U+p,data=json.dumps(b).encode(),headers={"Content-Type":"application/json"})
    try: return json.load(urllib.request.urlopen(r))
    except urllib.error.HTTPError as e: return {"HTTP":e.code, **json.load(e)}
g=json.load(urllib.request.urlopen(U+"/api/data")); d=g["data"]
orig=open("orig.json",encoding="utf-8").read()
print("python re-dump identical to file bytes:", json.dumps(json.loads(orig),indent=1,ensure_ascii=False)+"\n"==orig)
body={"ranks":{r["id"]:r["rank"] for r in d["rules"]},"min_tier":{r["id"]:r.get("min_tier") or "" for r in d["rules"]},"specials":d["specials"],"base_mtime":g["mtime"]}
r=post("/api/save",body); print("no-change save:", {k:r.get(k) for k in ("ok","unchanged","error")}); print("file untouched after no-change save:", open("item_priority_copy.json",encoding="utf-8").read()==orig)
# real change: move pri_nugget above pri_leftovers (rank 2.5), lift leppa to ULTRA, then save
b2=json.loads(json.dumps(body)); b2["ranks"]["pri_nugget"]=2.5; b2["min_tier"]["leppa"]="ULTRA"
b2["base_mtime"]=r["mtime"]; r=post("/api/save",b2); print("change save:", r.get("ok"), r.get("backup"), r.get("md"), r.get("error"))
stale=post("/api/save",body); print("stale mtime ->", stale.get("HTTP"), stale.get("error","")[:60])
bad=json.loads(json.dumps(b2)); bad["base_mtime"]=r["mtime"]; bad["ranks"]["pri_nugget"]="abc"; print("bad rank ->", post("/api/save",bad).get("HTTP"))
bad["ranks"]["pri_nugget"]=2.5; bad["min_tier"]["leppa"]="SUPER"; print("bad tier ->", post("/api/save",bad).get("HTTP"))
# revert via backup -> must be byte-identical to original
bk=json.load(urllib.request.urlopen(U+"/api/backups"))["backups"]; print("backups:", bk)
r=post("/api/revert",{"name":bk[-1]}); print("revert:", r.get("ok"), r.get("md"))
now=open("item_priority_copy.json",encoding="utf-8").read(); import difflib; print("".join(list(difflib.unified_diff(orig.splitlines(1),now.splitlines(1)))[:20])); print("after revert byte-identical to original:", now==orig)
# prio.py ranking equivalence on sample screens
spec=importlib.util.spec_from_file_location("p",os.path.expandvars(r"%TEMP%\prfarm\prio.py")); p=importlib.util.module_from_spec(spec); spec.loader.exec_module(p)
A=json.loads(orig); B=json.loads(now)
names=[("Master Ball",4),("Rogue Ball",3),("Sitrus Berry",0),("DNA Splicers",3),("Super Lure",0),("Rare Candy",0),("Rarer Candy",2),("Leftovers",2),("Potion",0),("Full Restore",1),("Nugget",1),("X Attack",1),("Leppa Berry",0),("Ultra Ball",2),("Exp. All",2),("Soothe Bell",1),("Egg Voucher",3),("Max Revive",2),("TM045",2),("Tera Shard",1),("Eviolite",2)]
flagsets=[{},{"lure_active":1},{"holding_balls":1},{"out_of_balls":1},{"heal_need":1},{"role_low":1,"pp_low":1},{"secondary_in_party":1,"holding_balls":1},{"zacian_fainted":1,"role_dead":1}]
same=tot=0
for f in flagsets:
    for scr in itertools.combinations(names,3):
        it=[{"n":n,"t":t} for n,t in scr]
        a=[p.rank_item(x,f,A) for x in it]; b=[p.rank_item(x,f,B) for x in it]; tot+=1; same+= a==b
print(f"prio.rank_item identical on {same}/{tot} sample screens")

