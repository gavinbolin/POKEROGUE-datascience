import pathlib
import prio  # DATA RANK 10/30
import random
import re
import re
#!/usr/bin/env python3
"""PokeRogue farm17 (from farm16: ME top option + watchdog, PP item move targeting, faint vs switch-out, Zacian HP log)
PokeRogue farm15 - UI-state driven (reads the Phaser battle scene via a camera hook).
Zacian Classic farm. Fight only, never Escape, never Endless, stop on Zacian faint.
Fixes vs farm14: no blind Space+Z double-confirm (caused stray party/menu wandering),
real PP + foe types from game objects, reward picked by priority, move rotation."""
import json, asyncio, websockets, urllib.request, pathlib, time, base64, traceback
from datetime import datetime
TGT_PREF = [None]  # TARGETFIX 11/2
TGT_JS = """(names=>{try{const s=window.__pr_cam.scene,h=s.ui.getHandler();const ts=h.targets||[];for(const n of names){const p=s.getEnemyField().find(e=>e&&e.name===n&&!e.isFainted());if(!p)continue;const bi=p.getBattlerIndex();if(ts.includes(bi)){if(h.cursor!==bi)h.setCursor(bi);return {ok:bi,cur:h.cursor}}}return {none:ts,cur:h.cursor}}catch(e){return {err:String(e)}}})"""
from datetime import datetime
HERE = pathlib.Path(__file__).parent
OUT = pathlib.Path(r"C:\Users\gavin\agent-tools")
LOG = OUT / "pokerogue_farm_log.txt"; STATUS = OUT / "pokerogue_farm_status.json"
STOP = OUT / "pokerogue_farm_stop.flag"; SHOT_DIR = OUT / "pokerogue_battle_shots"
FRAMES = OUT / "prframes"  # stall/debug frames; battle shots -> SHOT_DIR
STATE_JS = (HERE / "state.js").read_text(encoding="utf-8")
HOOK_JS = """(()=>{const S=Phaser.GameObjects.Sprite.prototype;if(!S.__g){const so=S.setTexture;S.__g=1;S.setTexture=function(...a){if(!this.scene)return this;return so.apply(this,a)}};const P=Phaser.Cameras.Scene2D.Camera.prototype; if(!P.__hpre){const o=P.preRender;P.__hpre=1;P.preRender=function(...a){window.__pr_cam=this;return o.apply(this,a)}} return !!window.__pr_cam})()"""
GROUND = 4
STEP_JS = """(()=>{try{const L=window.__pr_cam.scene.game.loop;if(document.visibilityState!=='hidden')return {hidden:false,frame:L.frame};
let t=Math.max(L.lastTime||0,L.now||0);const TW=window.__pr_cam.scene.tweens;for(let k=0;k<45;k++){t+=16.7;if(TW)TW.prevTime=Date.now()-16.7;L.step(t)}return {hidden:true,frame:L.frame}}catch(e){return String(e.stack||e)}})()"""
# reward priority (lower index = better). matched case-insensitively as substrings
REWARD_PRI = ["leppa berry", "rare candy", "max revive", "leftovers", "shell bell", "choice band", "life orb", "muscle band",
              "king's rock", "scope lens", "quick claw", "focus band", "soothe bell", "lucky egg", "exp. share",
              "golden", "silk scarf", "pixie plate", "fairy", "metal coat", "berry", "full restore", "max potion",
              "revive", "hyper potion", "max elixir", "elixir", "max ether", "ether", "super potion", "nugget",
              "ultra ball", "great ball", "potion", "poke ball"]
OPT_LABELS_JS = """(()=>{try{const h=window.__pr_cam.scene.ui.getHandler();const c=h.optionsContainer;if(!c)return [];const t=c.list.filter(x=>x.type==='Text'||x.text!==undefined).map(x=>({t:String(x.text),y:x.y}));t.sort((a,b)=>a.y-b.y);return t.map(x=>x.t)}catch(e){return String(e)}})()"""
PICKUP_JS = "(()=>{try{return window.__pr_cam.scene.getPlayerParty().some(p=>{const a=p.getAbility&&p.getAbility();const pa=p.getPassiveAbility&&p.hasPassive&&p.hasPassive()?p.getPassiveAbility():null;return [a,pa].some(x=>x&&(x.id===53||String(x.name).toLowerCase()==='pickup'))})}catch(e){return false}})()"
# ROLES: the two mons the farm keeps alive (match species id, else name)
PRIMARY = ("Zacian", {888})  # AGNOSTIC 10/30: rebound at runtime by resolve_primary() (config "primary" or party slot 1)
PROFILE_DIRS = [pathlib.Path(r"C:\Users\gavin\..PROJECT\pokerogue\profiles"), pathlib.Path(__file__).parent / "profiles"]
PROFILE_DEFAULT = {"name": None, "species": [], "signature_items": [], "learn_moves": False, "protected_moves": [], "wanted_moves": [],
                   "replaceable_moves": [], "replace_normal_type": False, "good_moves": [], "primary_move": None, "spread_moves": [],
                   "decline_moves": [], "max_one_damaging_of_types": [], "avoid_in_battle": []}  # t148u
_PROF = {"key": None, "data": dict(PROFILE_DEFAULT), "src": None}
def profile_for(sp_ids, name, logf=None):
    """Load the profile JSON whose species list matches the primary (hot-reloads on mtime change)."""
    files = []
    for d in PROFILE_DIRS:
        try: files += sorted(d.glob("*.json"))
        except Exception: pass
    for f in files:
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
            if set(int(x) for x in d.get("species", [])) & set(sp_ids) or str(d.get("name", "")).lower() == str(name).lower():
                key = (str(f), f.stat().st_mtime)
                if key != _PROF["key"]:
                    data = dict(PROFILE_DEFAULT); data.update(d)
                    _PROF.update(key=key, data=data, src=str(f))
                    if logf: logf(f"PROFILE loaded {f} for {name}: protected={data['protected_moves']} wanted={data['wanted_moves']} primary_move={data['primary_move']} learn_moves={data['learn_moves']} signature={data['signature_items']}")
                return _PROF["data"]
        except Exception as e:
            if logf: logf(f"PROFILE invalid {f}: {e!r}")
    key = ("default", name)
    if key != _PROF["key"]:
        _PROF.update(key=key, data=dict(PROFILE_DEFAULT, name=name), src=None)
        if logf: logf(f"PROFILE none for {name} {sorted(sp_ids)} -> defaults (decline new moves)")
    return _PROF["data"]
def sec_profile():  # ETERNTEAM t200u: secondary profile (eelektross.json), read fresh each call
    for d in PROFILE_DIRS:
        for f in sorted(d.glob("*.json")) if d.exists() else []:
            try:
                j = json.loads(f.read_text(encoding="utf-8-sig"))
                if set(int(x) for x in j.get("species", [])) & set(SECONDARY[1]) and j.get("role") == "secondary": return j
            except Exception: pass
    return {}
def PROF():
    return profile_for(PRIMARY[1], PRIMARY[0])
def resolve_primary(party, logf=None):
    """Primary = config 'primary' (name or species id) if in party, else first non-secondary mon in party order (slot 1)."""
    global PRIMARY
    want = None
    try: want = json.loads(CONFIG_FILE.read_text(encoding="utf-8-sig")).get("primary")
    except Exception: pass
    pick = None
    if want not in (None, "", "auto"):
        pick = next((p for p in party or [] if str(p.get("sp")) == str(want) or str(p.get("n", "")).lower() == str(want).lower()), None)
    if pick is None and want not in (None, "", "auto"): return None  # MEFIGHT 11-01: configured primary absent (ME-limited party) -> wait, never fall back to a bench mon
    if pick is None:
        pick = next((p for p in party or [] if p.get("sp") not in SECONDARY[1] and p.get("n") not in ("Feebas", "Milotic")), None)
    if pick is None: return None
    sp = {pick["sp"]} | ({pick["fs"]} if pick.get("fs") else set())
    new = (pick["n"], {pick["sp"]})
    if new != PRIMARY or _PROF["key"] is None:
        PRIMARY = new
        if logf: logf(f"PRIMARY resolved: {pick['n']} (species {pick['sp']}, slot {pick.get('i')}) source={'config' if want not in (None, '', 'auto') else 'party slot'}")
        profile_for(PRIMARY[1], PRIMARY[0], logf)
    return pick
# LEARN SCORE (Gavin t141u 10/31): profile "learn_mode": "score" -> every offered move is scored vs the current set
_SE = {1:{0,5,8,14,16},2:{1,6,11},3:{11,17},4:{3,5,8,9,12},5:{2,6,9,14},6:{11,13,16},7:{7,13},8:{5,14,17},9:{6,8,11,14},10:{4,5,9},11:{4,5,10},12:{2,10},13:{1,3},14:{2,4,11,15},15:{15},16:{7,13},17:{1,15,16}}
LEARN_NOTE = [""]
def _cov(ms):
    c = set()
    for m in ms:
        if m.get("cat") != 2 and (m.get("pow") or 0) > 0: c |= _SE.get(m.get("type"), set())
    return c
def move_score(prof, m, others):
    n = m["n"]; sv = prof.get("status_values", {})
    if m.get("cat") == 2 or (m.get("pow") or 0) <= 0:
        return float(sv.get(n, 0)) if m.get("cat") == 2 else float(sv.get(n, 30))  # variable-power/unknown damaging move = 30
    st = prof.get("stats", {}); a = float(st.get("atk", 100)); sa = float(st.get("spatk", 100)); top = max(a, sa)
    acc = m.get("acc"); acc = 100 if acc is None or acc < 0 else acc
    sc = m["pow"] * acc / 100.0 * (1.5 if m.get("type") in set(prof.get("stab_types", [])) else 1.0) * ((sa if m.get("cat") == 1 else a) / top)
    if n in prof.get("recharge_moves", []): sc *= 0.6
    if n in prof.get("self_drop_moves", []): sc *= 0.8
    sc += 8.0 * len(_SE.get(m.get("type"), set()) - _cov(others))
    return round(sc, 1)
_tm_logged = set()
def learn_score(prof, cur, new):
    nm = new["n"]; names = [m["n"] for m in cur]
    if nm in names: LEARN_NOTE[0] = f"already known {nm}"; return None
    _tg = list(prof.get("target_moveset") or [])  # TGTMOVES t205u/t206u: profile-driven convergence on a target final moveset (no-op without the field)
    if _tg:
        _ts = set(_tg); prof = dict(prof, protected_moves=list(set(prof.get("protected_moves", [])) | _ts))
        _dmg = lambda m: m.get("cat") != 2 and (m.get("pow") or 0) > 0
        if nm in _ts:
            if len(cur) < 4: LEARN_NOTE[0] = f"TARGET {nm} (free slot)"; return len(cur)
            _nt = [(i, m) for i, m in enumerate(cur) if m["n"] not in _ts]
            if not _nt: LEARN_NOTE[0] = f"TARGET {nm} but no non-target slot"; return None
            _df = list(prof.get("drop_first", []))
            _nt.sort(key=lambda im: (0, _df.index(im[1]["n"])) if im[1]["n"] in _df else (1, move_score(prof, im[1], [x for j, x in enumerate(cur) if j != im[0]])))
            LEARN_NOTE[0] = f"TARGET {nm} REPLACES non-target {_nt[0][1]['n']}"; return _nt[0][0]
        if _ts <= set(names): LEARN_NOTE[0] = f"decline {nm} (all target moves known)"; return None
        _xt = prof.get("extra_type_caps") or {}
        _ty = str(new.get("type"))
        if _dmg(new) and _ty in _xt and sum(1 for m in cur if m["n"] not in _ts and _dmg(m) and str(m.get("type")) == _ty) >= int(_xt[_ty]):
            LEARN_NOTE[0] = f"decline {nm} (non-target type-{_ty} cap {_xt[_ty]} reached)"; return None
    ns = move_score(prof, new, cur)
    # t148u: decline list + max one damaging move per capped type (Lugia: Psychic=13 -> Lumina Crash only)
    if nm in set(prof.get("decline_moves", [])): LEARN_NOTE[0] = f"decline {nm} (decline_moves)"; return None
    capt = set(prof.get("max_one_damaging_of_types", []))
    dmg = lambda m: m.get("cat") != 2 and (m.get("pow") or 0) > 0
    if capt and dmg(new) and new.get("type") in capt and any(dmg(x) and x.get("type") == new.get("type") for x in cur):
        LEARN_NOTE[0] = f"decline {nm} (already have a damaging type-{new.get('type')} move; capped)"; return None
    if capt and len(cur) >= 4 and ns > 0 and not (dmg(new) and new.get("type") in capt):
        _kp = set(prof.get("protected_moves", []))
        for t in capt:
            same = [(i, x) for i, x in enumerate(cur) if dmg(x) and x.get("type") == t]
            if len(same) >= 2:
                extra = [(move_score(prof, x, [y for j, y in enumerate(cur) if j != i]), i, x["n"]) for i, x in same if x["n"] not in _kp]
                if extra:
                    es, ei, en = min(extra)
                    LEARN_NOTE[0] = f"score new {nm}={ns} REPLACE extra capped-type move {en}={es} (t148u)"; return ei
    if len(cur) < 4:
        LEARN_NOTE[0] = f"score new {nm}={ns} (free slot)"; return len(cur) if ns > 0 else None
    keep = set(prof.get("protected_moves", []))
    stab = set(prof.get("stab_types", []))
    dstab = lambda m: m.get("cat") != 2 and (m.get("pow") or 0) > 0 and m.get("type") in stab
    newstab = dstab(new)
    sc = []
    for i, m in enumerate(cur):
        if m["n"] in keep: continue
        if dstab(m) and not newstab and sum(1 for x in cur if dstab(x)) <= 1: continue  # never drop the last damaging STAB move
        sc.append((move_score(prof, m, [x for j, x in enumerate(cur) if j != i]), i, m["n"]))
    if not sc: LEARN_NOTE[0] = f"score new {nm}={ns} vs none replaceable (protected/last STAB)"; return None
    ws, wi, wn = min(sc)
    # t204u: drop_first moves (Eternatus: Poison Tail) are replaced before the weakest move
    _df = [t for t in sc if t[2] in set(prof.get("drop_first", []))]
    if _df and new.get("cat") != 2 and (new.get("pow") or 0) > 0:
        ws, wi, wn = _df[0]
    ns = move_score(prof, new, [x for j, x in enumerate(cur) if j != wi])
    thr = float(prof.get("replace_margin", 1.10))
    ok = ns > ws * thr and ns > 0
    LEARN_NOTE[0] = f"score new {nm}={ns} vs weakest {wn}={ws} (need >{round(ws*thr,1)}) -> {'REPLACE' if ok else 'keep'}"
    return wi if ok else None
def learn_decide(prof, cur, new):
    """Return moveset index to forget for `new`, or None to decline. cur/new: dicts n,type,pow,cat."""
    LEARN_NOTE[0] = ""
    # slot_replace (MOVES 11/04): {"Night Slash": 0} = force that 0-based slot for that move only; decline all other offers while any slot_replace move is still unknown
    _sr = prof.get("slot_replace") or {}
    if _sr:
        nm = new["n"]; names = [m["n"] for m in cur]
        if nm in _sr:
            if nm in names: LEARN_NOTE[0] = f"SLOT_REPLACE already known {nm}"; return None
            si = int(_sr[nm])
            if 0 <= si < len(cur):
                LEARN_NOTE[0] = f"SLOT_REPLACE {nm} -> slot {si} ({cur[si]['n']})"; return si
            if len(cur) < 4 and si == len(cur):
                LEARN_NOTE[0] = f"SLOT_REPLACE {nm} free slot {si}"; return si
            LEARN_NOTE[0] = f"SLOT_REPLACE {nm} bad slot {si} (len={len(cur)})"; return None
        _pend = [m for m in _sr if m not in names]
        if _pend:
            LEARN_NOTE[0] = f"decline {nm} (waiting slot_replace {_pend})"; return None
    if prof.get("learn_mode") == "fixed":  # t154u/t155u: fixed loadout + one FLEX slot (first non-protected move)
        nm = new["n"]; names = [m["n"] for m in cur]; prot = set(prof.get("protected_moves", []))
        fin = prof.get("flex_final"); ft = set(prof.get("flex_types", []))
        if nm in names: LEARN_NOTE[0] = f"FIXED already known {nm}"; return None
        if fin and fin in names: LEARN_NOTE[0] = f"FIXED decline {nm} ({fin} known; loadout final)"; return None
        if len(cur) < 4: LEARN_NOTE[0] = f"FIXED {nm} free slot"; return len(cur) if (nm == fin or new.get("type") in ft) else None
        flex = [(i, m) for i, m in enumerate(cur) if m["n"] not in prot]
        if not flex: LEARN_NOTE[0] = f"FIXED decline {nm} (no flex slot)"; return None
        fi, fm = flex[0]; oth = [x for j, x in enumerate(cur) if j != fi]
        ns = move_score(prof, new, oth); fs = move_score(prof, fm, oth)
        if nm == fin: LEARN_NOTE[0] = f"FIXED {nm}={ns} REPLACES flex {fm['n']}={fs} (final)"; return fi
        dmg = new.get("cat") != 2 and (new.get("pow") or 0) > 0
        if not (dmg and new.get("type") in ft): LEARN_NOTE[0] = f"FIXED decline {nm}={ns} (not damaging flex type) flex {fm['n']}={fs}"; return None
        thr = float(prof.get("replace_margin", 1.10)); ok = ns > fs * thr
        LEARN_NOTE[0] = f"FIXED flex {nm}={ns} vs {fm['n']}={fs} (need >{round(fs*thr,1)}) -> {'REPLACE' if ok else 'keep'}"
        return fi if ok else None
    if prof.get("learn_mode") == "score" and prof.get("learn_moves"): return learn_score(prof, cur, new)
    if not prof.get("learn_moves"): return None
    nm = new["n"]; names = [m["n"] for m in cur]
    if nm in names: return None
    prot = set(prof["protected_moves"]); wanted = set(prof["wanted_moves"]); good = set(prof["good_moves"]); repl = list(prof["replaceable_moves"])
    if nm not in wanted and nm not in good: return None
    if len(cur) < 4: return len(cur)
    keep = prot | wanted | ({m for m in good} if nm not in wanted else set())
    c = [(i, m) for i, m in enumerate(cur) if m["n"] not in keep]
    if not c: return None
    def key(im):
        i, m = im
        if m["n"] in repl: return (0, repl.index(m["n"]))
        if prof.get("replace_normal_type") and m.get("type") == 0: return (1, m.get("pow") or 0)
        if m.get("cat") == 2: return (2, 0)
        return (3, m.get("pow") or 0)
    i, m = min(c, key=key)
    if nm in wanted: return i
    k = key((i, m))[0]
    if k <= 2 or (m.get("pow") or 0) < 0.8 * (new.get("pow") or 0): return i
    return None
LEARN_JS = r"""(()=>{try{const s=window.__pr_cam.scene,ph=s.phaseManager.getCurrentPhase();if(!ph||ph.constructor.name!=='LearnMovePhase')return null;const p=ph.getPokemon();const ms=p.getMoveset();const C=ms[0].constructor;const nm=new C(ph.moveId).getMove();
const f=m=>({n:m.name,type:m.type,pow:m.power,cat:m.category,acc:m.accuracy});return {pi:s.getPlayerParty().indexOf(p),pn:p.name,sp:p.species.speciesId,lt:ph.learnMoveType,cur:ms.map(m=>f(m.getMove())),new:f(nm),canLearn:typeof ph.learnMove==='function'}}catch(e){return {err:String(e)}}})()"""
LEARN_DO_JS = r"""(()=>{try{const s=window.__pr_cam.scene,ph=s.phaseManager.getCurrentPhase();if(!ph||ph.constructor.name!=='LearnMovePhase')return 'nophase';const p=ph.getPokemon();const ms=p.getMoveset();const C=ms[0].constructor;const mv=new C(ph.moveId).getMove();const old=ms[%d]?ms[%d].getName():null;
ph.learnMove(%d,mv,p,old?('1, 2, and... Poof! '+p.name+' forgot '+old+'. And...'):undefined);return 'ok:'+old}catch(e){return 'err:'+String(e)}})()"""
SECONDARY = ("Abra", {63, 64, 65})  # MEWABSOL t207u 11/04: Absol secondary, Mewtwo (150) primary via config
_OLD_SECONDARY = ("Tynamo", {602, 603, 604})  # TYNAMO t199u 11/03: Tynamo/Eelektrik/Eelektross is the secondary (Mudkip/Feebas lines no longer secondary)
LEVITATE_PARTNER = {602, 603, 604}  # TYNAMO t199u: Levitate partner -> Zacian may Earthquake in doubles
def role(party, r):
    return next((p for p in party or [] if p.get("sp") in r[1] or p.get("n") == r[0]), None)
DNA_BASE = {401, 402}; DNA_PARTNER = {263, 264}  # Gavin 10/30 (t132u): Kricketot/Kricketune BASE (first) + Zigzagoon/Linoone PARTNER (second)
def dna_pair(party):
    b = next((p for p in party or [] if p.get("sp") in DNA_BASE and not p.get("fs")), None)
    q = next((p for p in party or [] if p.get("sp") in DNA_PARTNER and not p.get("fs") and p is not b), None)
    return (b, q) if b and q else None
# SHOP (proactive buys on the reward screen, before the free reward)
SHOP_MAX_SPEND_FRAC = 0.25  # max share of money (at screen open) spent per reward screen
SHOP_RESERVE_FRAC = 0.25    # never drop below this share of money at screen open
SHOP_MIN_RESERVE = 0        # absolute money floor
SHOP_HURT = 0.75   # Gavin 10/29 20:12: was 0.85 (chip-damage Potion spam)
SHOP_MIN_MISS_FRAC = 0.15  # non-hard: skip heal buy if missing HP < 15% of max
SHOP_JS = """(()=>{try{const s=window.__pr_cam.scene,h=s.ui.getHandler();const R=h.shopOptionsRows||[],L=R.length,o=[];R.forEach((row,k)=>row.forEach((x,c)=>{const t=x.modifierTypeOption;o.push({r:L-k+1,c,n:t.type.name,cost:t.cost})}));return {money:s.money,items:o}}catch(e){return {err:String(e)}}})()"""
SIG_FILE = pathlib.Path(r"C:\Users\gavin\agent-tools\pokerogue_significant_waves.json")
SIG_JSONL = SIG_FILE.with_suffix(".jsonl")
HARD_WAVES_BASE = {8, 25, 55, 95, 165, 195}
# --- Gavin 10/29: live-config (control app writes CONFIG_FILE; re-read each wave) ---
SECFIELD_FORCE_BENCH = True  # Gavin 20:52: never bring secondary into singles (overrides config)
PARTY_ORDER_FIX = True       # at reward screen, restore order Zacian, secondary, others (JS array reorder, no input)
SEC_ALLOW_PRISM = True    # TEMP (Gavin 20:29): Prism Scale may go to secondary Feebas
SEC_ALLOW_HEAL = True     # Gavin 20:29b: secondary healed like Zacian (potions/Full Heal/pre-heal)
SEC_ALLOW_SOOTHE = True   # Gavin 10/30 01:47: Soothe Bell -> secondary first until max stack, then Zacian
SEC_ALLOW_REVIVE = True   # TEMP (Gavin 20:29): revives may go to a FAINTED secondary
CANDY_TARGET = 'secondary'    # 'secondary' | 'primary' | 'both'  (Soothe Bell / Rare Candy target)
SECONDARY_FIELD = 'auto'      # 'bench' | 'field' | 'auto'  (Secondary in singles: bring secondary onto the field for candy)
CONFIG_FILE = pathlib.Path(r"C:\Users\gavin\agent-tools\pokerogue_farm_config.json")
CFG = {"candy_target": CANDY_TARGET, "secondary_field": SECONDARY_FIELD}
def cfg_reload(logf=None):
    new = {"candy_target": CANDY_TARGET, "secondary_field": SECONDARY_FIELD}
    try:
        d = json.loads(CONFIG_FILE.read_text(encoding="utf-8-sig"))
        if str(d.get("candy_target","")).lower() in ("secondary","primary","both"): new["candy_target"] = str(d["candy_target"]).lower()
        if str(d.get("secondary_field","")).lower() in ("bench","field","auto"): new["secondary_field"] = str(d["secondary_field"]).lower()
    except Exception: pass
    if SECFIELD_FORCE_BENCH: new["secondary_field"] = "bench"
    for k, v in new.items():
        if CFG.get(k) != v:
            if logf: logf(f"CONFIG change {k}: {CFG.get(k)} -> {v}")
            CFG[k] = v
SHOP_HARD_SPEND_FRAC = 0.75
SHOP_HARD_HURT = 0.99
def sig_load():
    try: return json.loads(SIG_FILE.read_text(encoding="utf-8"))
    except Exception: return {"learned_hard": [], "wave_tally": {}, "records": 0}
SIG = sig_load()
HARD_WAVES = HARD_WAVES_BASE | set(int(x) for x in SIG.get("learned_hard", []))
HARD_JS = """(n=>{try{const s=window.__pr_cam.scene,g=s.gameMode;let f=false,t=false;try{f=!!g.isFixedBattle(n)}catch(e){};try{t=!!g.isWaveTrainer(n,s.arena)}catch(e){};return {fixed:f,trainer:t}}catch(e){return {err:String(e)}}})"""
SIG_JS = """(()=>{try{const s=window.__pr_cam.scene,b=s.currentBattle,t=b.trainer;let fx=false;try{fx=!!s.gameMode.isFixedBattle(b.waveIndex)}catch(e){};const nm=t?(t.getName?t.getName(0,true):t.name):null;return {tr:nm,tt:t&&t.config?t.config.trainerType:null,bosses:s.getEnemyParty().filter(e=>e.isBoss&&e.isBoss()).map(e=>e.name),biome:s.arena?s.arena.biomeType:null,fixed:fx,rival:!!(t&&/rival/i.test(String(t.config&&t.config.name||'')+String(nm)))||(fx&&!!t&&[8,25,55,95,145,195].includes(b.waveIndex))}}catch(e){return {err:String(e)}}})()"""
SHOP_SEL_JS = """(nm=>{try{const h=window.__pr_cam.scene.ui.getHandler();if(!h.awaitingActionInput)return 'notready';const R=h.shopOptionsRows||[],L=R.length;for(let k=0;k<L;k++){const c=R[k].findIndex(x=>x.modifierTypeOption.type.name===nm);if(c>=0){const r=L-k+1;if(h.rowCursor!==r)h.setRowCursor(r);h.setCursor(c);const v=R.at(-(h.rowCursor-1));return v&&v[h.cursor]?v[h.cursor].modifierTypeOption.type.name:null}}return null}catch(e){return 'err:'+e}})(%s)"""
RUN_ID = datetime.now().strftime("%Y%m%d-%H%M%S")
PRIM_ORB = [False]  # ORBFIX: primary currently holds Flame/Toxic Orb
PRIM_ORB_JS = "(()=>{try{const s=window.__pr_cam.scene;const z=s.getPlayerParty().find(p=>p.species&&(window.__pr_prim||[888]).includes(p.species.speciesId));return !!(z&&s.findModifier(m=>m.pokemonId===z.id&&/^(FLAME|TOXIC)_ORB$/.test((m.type&&m.type.id)||'')))}catch(e){return false}})()"
def shop_plan(party, z, sec, items, money, budget, hurt=None, skip=()):
    SHOP_HURT_ = hurt or SHOP_HURT
    def heal_amt(n, mx, nocure=False):
        n = n.lower()
        if nocure and n == "full restore": return 0  # ORBMILOTIC: no status-cure item for Milotic
        if n == "potion": return max(20, mx * 0.1)
        if n == "super potion": return max(50, mx * 0.25)
        if n == "hyper potion": return max(200, mx * 0.5)
        if n in ("max potion", "full restore"): return mx
        return 0
    ok = [it for it in items if not orb_banned(it) and 0 < it["cost"] <= budget and it["cost"] <= money]
    for p in sorted([x for x in (z, sec) if x and x["n"] not in skip], key=lambda x: (x["hp"] > 0, x["hp"] / max(1, x.get("mx") or 1))):  # fainted first, then lowest HP%
        if p is sec and not (SEC_ALLOW_HEAL if p["hp"] > 0 else SEC_ALLOW_REVIVE): continue  # secondary gets only candy (+revive exception)
        if p["hp"] <= 0:
            rv = [it for it in items if it["n"].lower() in ("max revive", "revive") and 0 < it["cost"] <= money and (p is z or it["cost"] <= budget)]  # ZREVIVE: fainted Zacian may use all money (no 25% cap)
            if rv: return max(rv, key=lambda it: it["cost"]), p, "revive"
            continue
        mx = p.get("mx") or 1; miss = mx - p["hp"]; r = p["hp"] / mx
        _nc = SEC_NO_STATUS_CURE and p is sec and sec.get("sp") in (349, 350, 602, 603, 604)  # TYNACURE 11/04: Toxic Orb poison on Tynamo line never cured
        if _nc and p.get("stt") and getattr(shop_plan, "_scl", None) != (p["hp"], p["stt"]):
            shop_plan._scl = (p["hp"], p["stt"]); log(f"SHOP SEC STATUS skip: {p['n']} stt={p['stt']} not cured; heal only if HP<{SHOP_HURT_:.0%} (now {r:.0%}) with plain potion")
        _po = bool(p is z and PRIM_ORB[0] and p.get("stt"))  # ORBFIX: orb status on primary -> no Full Heal
        if _po and getattr(shop_plan, "_pol", None) != p["hp"]:
            shop_plan._pol = p["hp"]; log(f"ORBFIX shop: primary holds orb, stt={p['stt']} -> no Full Heal (awaiting transfer); HP heals only")
        if p.get("stt") and not _nc and not _po:
            if r < SHOP_HURT_:
                fr = [it for it in ok if it["n"].lower() == "full restore"]
                if fr: return fr[0], p, "status+hurt"
            fh = [it for it in ok if it["n"].lower() == "full heal"]
            if fh: return fh[0], p, "status"
        if r < SHOP_HURT_ and (hurt or miss >= SHOP_MIN_MISS_FRAC * mx):
            need = miss if r < 0.3 else min(miss, 0.5 * miss + 0.15 * mx)
            pots = sorted([it for it in ok if heal_amt(it["n"], mx, _nc) > 0], key=lambda it: it["cost"])
            good = [it for it in pots if heal_amt(it["n"], mx, _nc) >= need]
            pick = good[0] if good else (pots[-1] if pots else None)
            if pick and heal_amt(pick["n"], mx, _nc) >= min(miss, 0.1 * mx): return pick, p, "hurt"
    return None
KRICK_JS = """(()=>{try{const s=window.__pr_cam.scene;const out={set:[],have:[]};s.getPlayerParty().forEach((p,i)=>{if(p.species&&p.species.speciesId===401){if(!p.pauseEvolutions){p.pauseEvolutions=true;out.set.push(i)}out.have.push(i)}});const ph=s.phaseManager.getCurrentPhase();out.ph=ph?ph.constructor.name:null;try{out.evo=!!(ph&&ph.constructor.name==='EvolutionPhase'&&ph.pokemon&&ph.pokemon.species.speciesId===401)}catch(e){}return out}catch(e){return {err:String(e)}}})()"""
REORDER_JS = """(()=>{try{const s=window.__pr_cam.scene;const ph=s.phaseManager.getCurrentPhase();if(!ph||ph.constructor.name!=='SelectModifierPhase')return {moved:false,why:'phase'};const P=s.getPlayerParty();const b=P.map(p=>p.name);const zi=P.findIndex(p=>p.species&&(window.__pr_prim||[888]).includes(p.species.speciesId));if(zi<0||P[zi].hp<=0)return {moved:false,why:'zacian'};const si=P.findIndex(p=>p.species&&(window.__pr_sec||[63,64,65]).includes(p.species.speciesId));const want=[P[zi]].concat(si>=0?[P[si]]:[]).concat(P.filter((p,i)=>i!==zi&&i!==si));if(want.every((p,i)=>p===P[i]))return {moved:false};P.splice(0,P.length,...want);return {moved:true,before:b,after:P.map(p=>p.name)}}catch(e){return {moved:false,err:String(e)}}})()"""
LURE_JS = "(()=>{try{const s=window.__pr_cam.scene;const m=(s.modifiers||[]).find(x=>x&&x.constructor&&/DoubleBattleChance/.test(x.constructor.name));if(!m)return 0;return (m.getBattleCount?m.getBattleCount():(m.battleCount??m.battlesLeft??1))||0}catch(e){return 0}})()"
VITAMINS = ["hp up", "protein", "iron", "calcium", "zinc", "carbos", "base stat"]
PP_ITEMS = ["max elixir", "elixir", "max ether", "ether"]

ORB_BAN_IDS = ("FLAME_ORB", "TOXIC_ORB")
ORB_BAN_NAMES = ("flame orb", "toxic orb", "poison orb")
def orb_banned(r):
    n = str(r.get("n") or "").lower(); i = str(r.get("id") or "").upper()
    return i in ORB_BAN_IDS or any(k in n for k in ORB_BAN_NAMES)
def orb_key(r):  # ORBMILOTIC 11/01 (Gavin voice): orbs -> Milotic only
    n = str(r.get("n") or "").lower(); i = str(r.get("id") or "").upper()
    return "FLAME_ORB" if ("FLAME" in i or "flame orb" in n or "burn orb" in n) else "TOXIC_ORB"
def orb_for_sec(r, sec):
    """True if this orb may go to Milotic (alive, not already holding that orb)."""
    return bool(sec) and orb_key(r) == "TOXIC_ORB" and sec.get("sp") in (602, 603, 604) and (sec.get("hp") or 0) > 0 and orb_key(r) not in (sec.get("ho") or [])  # ETERNTEAM t200u 11/04: Toxic Orb -> Tynamo line only (Poison Heal); Flame Orb -> nobody
SEC_NO_STATUS_CURE = True  # ORBMILOTIC 11/01: never cure Milotic's burn/poison (Marvel Scale + Flame Orb); HP heals only via plain potions when HP low
SEC_CURE_ITEMS = ("full restore", "full heal", "lum berry", "antidote", "burn heal", "ice heal", "awakening", "paralyze heal")
EGG_LOG_MD = pathlib.Path(r"C:\Users\gavin\..PROJECT\PROJECT CHIE\OTHER\POKEROGUE\Shiny Log.md")  # 10/31 egg log merged into Shiny Log (Method column)
DOUBLES_SHINY_RULE = ("Wild shiny in a double: exactly ONE mon (Zacian) attacks the non-shiny partner, single-target move aimed at the partner. "
    "The other mon must NOT use a damaging move: use a status move (Calm Mind etc.) or switch it out via Pokemon menu. "
    "After the partner faints, no damaging moves at all; throw best ball at the shiny next turn. Never spread moves.")
EGG_COUNTS = pathlib.Path(r"C:\Users\gavin\agent-tools\pokerogue_egg_hatch_counts.json")
EGG_JS = """(()=>{try{const s=window.__pr_cam.scene;const ph=s.phaseManager.getCurrentPhase();const n=ph?ph.constructor.name:null;if(!n||!/EggHatch|EggSummary/.test(n))return null;const out=[];const add=(pk,eg)=>{if(!pk)return;out.push({id:pk.id,sid:(pk.species&&pk.species.speciesId)??null,n:pk.name||(pk.species&&pk.species.name),sh:!!(pk.isShiny&&pk.isShiny()),v:(pk.variant??null),src:eg?(eg.sourceType??null):null,tier:eg?(eg.tier??null):null,eid:eg?(eg.id??null):null})};if(ph.pokemon)add(ph.pokemon,ph.egg);(ph.eggHatchData||ph.eggHatchHandler?.eggHatchData||[]).forEach(d=>add(d.pokemon,d.egg));return {ph:n,list:out}}catch(e){return {err:String(e)}}})()"""
_egg_seen = set()
# HATCH AUDIT (10/30 eggshiny): game-side counters are the ground truth. gameStats.pokemonHatched / shinyPokemonHatched
# and per-species dexData hatchedCount are diffed every few seconds; any hatch the phase poller missed is logged and
# any unaccounted shiny is appended to the Shiny Log (Method Egg) as "audit".
AUDIT_JS = """(()=>{try{const s=window.__pr_cam.scene;const gd=s.gameData;const gs=gd.gameStats;const hc={};const dd=gd.dexData||{};for(const k in dd){const v=dd[k];if(v&&v.hatchedCount)hc[k]=[v.hatchedCount,String(v.caughtAttr??'')]};let nm={};try{for(const k in hc){const sp=(window.__pr_cam.allSpecies||[]).find?.(x=>x&&x.speciesId==k);if(sp)nm[k]=sp.name}}catch(e){};return {h:gs.pokemonHatched,sh:gs.shinyPokemonHatched,eggs:(gd.eggs||[]).map(e=>e.id),hc:hc,nm:nm}}catch(e){return {err:String(e)}}})()"""
_audit = {"base": None, "rec_n": 0, "rec_sh": 0}
SPRITE_DIR = EGG_LOG_MD.parent / "sprites"
def shiny_sprite(sid):
    """Return an Obsidian embed for the shiny icon of species id sid, downloading it once into the vault."""
    if not sid: return ""
    fn = f"pr_{sid}s.png"; out = SPRITE_DIR / fn
    if not out.exists():
        import urllib.request
        SPRITE_DIR.mkdir(parents=True, exist_ok=True)
        for g in range(1, 10):
            try:
                d = urllib.request.urlopen(f"https://raw.githubusercontent.com/pagefaultgames/pokerogue-assets/beta/images/pokemon/icons/{g}/{sid}s.png", timeout=5).read()
                out.write_bytes(d); break
            except Exception: continue
    return f"![[{fn}\\|40]]" if out.exists() else ""
EGG_HDR = "| Date (MDT) | | Pok\u00e9mon | Lv | Variant | Method | Wave | Ball |\n|---|:-:|---|--:|:-:|:-:|--:|---|\n"
EGG_TIER_NAMES = {0: "Common", 1: "Rare", 2: "Epic", 3: "Legendary", 4: "Manaphy"}
def md_insert_top(path, row):
    """Insert row directly under the first table separator (newest-first logs)."""
    L = path.read_text(encoding="utf-8").split("\n")
    for k in range(1, len(L)):
        if L[k-1].startswith("|") and re.match(r"^\|[\s:\-|]+\|\s*$", L[k]):
            L.insert(k+1, row.rstrip("\n")); path.write_text("\n".join(L), encoding="utf-8"); return
    with path.open("a", encoding="utf-8") as f: f.write(row)
RUN_LOG_MD = EGG_LOG_MD.parent / "Run Log.md"  # RUNLOG 11/01: one row per run end, newest first
RUN_HDR = "| Date (MT) | Slot | Wave | Team | Luck | Primary items | Ended by |\n|---|:-:|--:|---|:-:|---|---|\n"
RUNLOG_JS = """(()=>{try{const s=window.__pr_cam.scene;const cb=s.currentBattle;const P=s.getPlayerParty();const M=s.modifiers||[];const pm=P.find(p=>(window.__pr_prim||[888]).includes(p.species?.speciesId))||P[0];let lk=null;try{lk=P.reduce((a,p)=>a+(p.getLuck?p.getLuck():0),0)}catch(e){}const gl=(window.gameInfo&&window.gameInfo.luck!==undefined)?window.gameInfo.luck:null;const en=(s.getEnemyParty?.()||[]).map(e=>({n:e.name,hp:e.hp,f:!!e.isOnField?.()}));return {slot:s.sessionSlotId,wave:cb?.waveIndex,tr:cb?.trainer?(cb.trainer.getName?.()||'Trainer'):null,luck:(gl!==null?gl:(lk===null?null:Math.min(14,lk))),party:P.map(p=>({n:p.name,lv:p.level,sid:p.species?.speciesId,sh:!!p.shiny,v:p.variant,fn:p.fusionSpecies?p.fusionSpecies.name:null,fsid:p.fusionSpecies?p.fusionSpecies.speciesId:null,fsh:!!p.fusionShiny,fv:p.fusionVariant})),items:M.filter(m=>pm&&m.pokemonId===pm.id).map(m=>[m.type?.name,m.stackCount||1]),en}}catch(e){return {err:String(e)}}})()"""
def mon_sprite(sid, shiny=False, size=24):
    if not sid: return ""
    fn = f"pr_{sid}{'s' if shiny else ''}.png"; out = SPRITE_DIR / fn
    if not out.exists():
        try:
            import urllib.request
            SPRITE_DIR.mkdir(parents=True, exist_ok=True)
            for g in range(1, 10):
                try: out.write_bytes(urllib.request.urlopen(f"https://raw.githubusercontent.com/pagefaultgames/pokerogue-assets/beta/images/pokemon/icons/{g}/{sid}{'s' if shiny else ''}.png", timeout=5).read()); break
                except Exception: continue
        except Exception: pass
    return f"![[{fn}\\|{size}]]" if out.exists() else ""
def runlog_row(r, foes_fallback=None):
    D = "\u2014"
    def mon(p):
        sv = f" \u2605{(p.get('v') or 0)+1}" if p.get("sh") else ""
        fu = f" + {mon_sprite(p.get('fsid'), p.get('fsh'))} {p['fn']}" + (f" \u2605{(p.get('fv') or 0)+1}" if p.get('fsh') else "") if p.get("fn") else ""
        return f"{mon_sprite(p.get('sid'), p.get('sh'))} {p.get('n')} {p.get('lv')}{sv}{fu}"
    team = " \u00b7 ".join(mon(p) for p in r.get("party") or []) or D
    items = ", ".join(f"{n}" + (f" \u00d7{c}" if c and c > 1 else "") for n, c in (r.get("items") or []) if n and not n.endswith(" Berry") and n not in ("HP Up", "Protein", "Iron", "Calcium", "Zinc", "Carbos")) or D
    en = [e["n"] for e in (r.get("en") or []) if (e.get("hp") or 0) > 0 and e.get("f")] or [e["n"] for e in (r.get("en") or []) if (e.get("hp") or 0) > 0] or (foes_fallback or [])
    who = ("Trainer " + r["tr"] if r.get("tr") else "Wild") + (": " + ", ".join(en) if en else "")
    lk = r.get("luck"); slot = r.get("slot")
    return f"| {datetime.now().strftime('%Y-%m-%d %H:%M')} | {slot if isinstance(slot, int) else D} | {r.get('wave') or D} | {team} | {lk if lk is not None else D} | {items} | {who} |\n"
async def runlog_hook(ev, foes_fallback=None):
    try:
        r = await ev(RUNLOG_JS)
        if not isinstance(r, dict) or r.get("err"): log(f"RUN LOG read err {r}"); return
        if not RUN_LOG_MD.exists(): RUN_LOG_MD.write_text("# Pok\u00e9Rogue run log (PHOR, Classic farm)\n\n" + RUN_HDR, encoding="utf-8")
        row = runlog_row(r, foes_fallback); md_insert_top(RUN_LOG_MD, row); log(f"RUN LOG row w{r.get('wave')} slot={r.get('slot')} luck={r.get('luck')} -> Run Log.md")
    except Exception as e: log(f"RUN LOG write err {e}")
def egg_append_md(name, vt, src, tier, wave, note, sid=None):
    try:
        if not EGG_LOG_MD.exists():
            EGG_LOG_MD.write_text("# Pok\u00e9Rogue shiny log (account PHOR)\n\n" + EGG_HDR, encoding="utf-8")
        tn = EGG_TIER_NAMES.get(tier) if isinstance(tier, int) else None
        ball = (tn + " Egg") if tn else "\u2014"
        w = wave if wave is not None else "?"
        md_insert_top(EGG_LOG_MD, f"| {datetime.now().strftime('%Y-%m-%d %H:%M')} | {shiny_sprite(sid)} | {name} | \u2014 | {vt} | Egg | {w} | {ball} |\n")
    except Exception as e: log(f"EGG LOG write err {e}")
def hatch_audit(a, wave):
    if not isinstance(a, dict) or a.get("err") or a.get("h") is None: return
    b = _audit["base"]
    if b is None:
        _audit["base"] = a; _audit["rec_n"] = 0; _audit["rec_sh"] = 0
        log(f"HATCH AUDIT baseline: pokemonHatched={a['h']} shinyHatched={a['sh']} eggs={len(a.get('eggs') or [])}"); return
    dn = a["h"] - b["h"]; ds = a["sh"] - b["sh"]
    gone = len(set(b.get("eggs") or []) - set(a.get("eggs") or []))
    if dn <= 0 and gone == 0: _audit["base"] = a; return
    if dn > 0 and dn == _audit["rec_n"] and ds == _audit["rec_sh"]:
        log(f"HATCH AUDIT ok: {dn} hatched ({ds} shiny), all logged")
    else:
        sp = []
        for k, v in (a.get("hc") or {}).items():
            pv = (b.get("hc") or {}).get(k, [0, ""])
            if v[0] > pv[0]: sp.append(f"{(a.get('nm') or {}).get(k, '#'+k)}x{v[0]-pv[0]}" + ("(new attr)" if v[1] != pv[1] else ""))
        log(f"HATCH AUDIT MISMATCH: game says {dn} hatched/{ds} shiny, eggs gone {gone}, poller logged {_audit['rec_n']}/{_audit['rec_sh']}; dex diff: {', '.join(sp) or '?'}")
        for x in sp: log(f"EGG HATCH (audit) {x}")
        miss = ds - _audit["rec_sh"]
        if miss > 0:
            cand = [x for x in sp if "(new attr)" in x] or sp
            log(f"SHINY EGG HATCH (audit) x{miss} unlogged by poller; candidates: {cand}")
            egg_append_md(f"UNKNOWN x{miss} (candidates: {', '.join(cand) or '?'})", "?", "?", "?", wave, "audit: game shiny counter rose, poller missed it")
    _audit["base"] = a; _audit["rec_n"] = 0; _audit["rec_sh"] = 0
def egg_record(rec, wave):
    key = (rec.get("eid"), rec.get("id"))
    if key in _egg_seen: return
    _egg_seen.add(key)
    try: c = json.loads(EGG_COUNTS.read_text(encoding="utf-8"))
    except Exception: c = {"total": 0, "shiny": 0, "seen": []}
    ks = f"{rec.get('eid')}:{rec.get('id')}"
    if ks in c.setdefault("seen", []): return
    c["seen"] = (c["seen"] + [ks])[-500:]; c["total"] = c.get("total", 0) + 1
    _audit["rec_n"] += 1; _audit["rec_sh"] += 1 if rec.get("sh") else 0
    if rec.get("sh"):
        c["shiny"] = c.get("shiny", 0) + 1
        v = rec.get("v"); vt = (v + 1) if isinstance(v, int) else "?"
        log(f"SHINY EGG HATCH {rec.get('n')} variant {vt}")
        try:
            egg_append_md(rec.get('n'), vt, rec.get('src') if rec.get('src') is not None else '?', rec.get('tier') if rec.get('tier') is not None else '?', wave, "auto", rec.get('sid'))
        except Exception as e: log(f"EGG LOG write err {e}")
    else: log(f"EGG HATCH {rec.get('n')} (not shiny)")
    EGG_COUNTS.write_text(json.dumps(c, indent=1), encoding="utf-8")

def log(msg):
    line = f"{datetime.now().strftime('%H:%M:%S')} {msg}"
    try: print(line, flush=True)
    except UnicodeEncodeError: print(line.encode("ascii", "replace").decode(), flush=True)
    with LOG.open("a", encoding="utf-8") as f: f.write(line + "\n")

def find_page():
    pages = json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list"))
    return next(p for p in pages if p.get("type") == "page" and p.get("url", "").startswith("https://pokerogue.net/"))

EVO_TGT = {}  # EVOITEM 11/01 (Gavin voice): evolution item name -> species id of eligible party member (never primary/secondary)
EVO_PREF = (854, 855)  # Sinistea/Polteageist first
def pick_reward(st, bad=()):
    rew = [r for r in (st.get("rew") or []) if r.get("n") and r["n"] not in bad]
    _sec0 = role(st.get("party") or [], SECONDARY)
    _ob = [r["n"] for r in rew if orb_banned(r) and not orb_for_sec(r, _sec0)]
    _oa = [r["n"] for r in rew if orb_banned(r) and orb_for_sec(r, _sec0)]
    if (_ob or _oa) and getattr(pick_reward, "_obl", None) != (st.get("wave"), tuple(_ob), tuple(_oa)):
        pick_reward._obl = (st.get("wave"), tuple(_ob), tuple(_oa))
        if _ob: log(f"ORB skipped (Milotic absent/fainted/already holds) {', '.join(_ob)} held={_sec0 and _sec0.get('ho')}")
        if _oa: log(f"ORB allowed -> Milotic only: {', '.join(_oa)}")
    rew = [r for r in rew if not orb_banned(r) or orb_for_sec(r, _sec0)]
    if not any((p.get("hp") or 0) <= 0 for p in (st.get("party") or [])):  # REVIVENONE 10/31 18:48: no one fainted -> never pick a revive (game won't apply it; stalled w27)
        _rv = [r for r in rew if any(k in r["n"].lower() for k in ("revive", "sacred ash")) and "reviver seed" not in r["n"].lower()]
        if _rv and len(_rv) < len(rew): rew = [r for r in rew if r not in _rv]
    if not rew: return None, None
    z = role(st["party"], PRIMARY)
    sec = role(st["party"], SECONDARY)
    pp_low = any(m["max"] and m["left"] / m["max"] < 0.4 for m in (st.get("zmoves") or []))
    _dm = [m for m in (st.get("zmoves") or []) if (m.get("pow") or 0) > 0]
    pp_crit = bool(_dm) and (sum(m["left"] for m in _dm) <= 3 or all(m["left"] <= 0 for m in _dm if max(m.get("effs") or [1]) >= 2) and any(max(m.get("effs") or [1]) >= 2 for m in _dm))
    if _dm and sum(1 for m in _dm if m["left"] <= 3 or (m.get("max") and m["left"] / m["max"] < 0.15)) >= 2: pp_crit = True
    if _dm and sum(m.get("max") or 0 for m in _dm) and sum(m["left"] for m in _dm) / sum(m.get("max") or 0 for m in _dm) < 0.3: pp_crit = True  # PPDRY 11/04: total attack PP <30% -> Ether/Elixir top (w115 Eternatus struggled to faint; Big Nugget beat Max Ether at w114)  # EARLYWIPE 10/31: 2+ damaging moves nearly dry -> take Ether/Elixir (w50 wipe: AuraSphere 2/20 + AirCutter 0/25)
    ally_dead = any(p["hp"] <= 0 for p in st["party"])
    zhp_low = z and z.get("mx") and z["hp"] / z["mx"] < 0.5
    w0 = st.get("wave") or 0; nxt = w0 + 1
    zr = (z["hp"] / z["mx"]) if (z and z.get("mx")) else 1.0
    risky_next = nxt % 10 == 0 or bool(st.get("trainer")) or nxt % 10 in (5, 8)
    heal_need = zr < 0.5 or (zr < 0.999 and risky_next) or zr < 0.8
    feebas = sec is not None
    def _r(p): return (p["hp"] / p["mx"]) if (p and p.get("mx")) else 1.0
    role_dead = [p["n"] for p in (z, sec) if p and p["hp"] <= 0]
    role_low = [p["n"] for p in ((z, sec) if SEC_ALLOW_HEAL else (z,)) if p and p["hp"] > 0 and _r(p) < 0.75]
    HEAL = ["full restore", "max potion", "hyper potion", "sitrus berry", "super potion", "potion"]
    # DATA RANK (Gavin 10/30 18:25 MT): ranks come from item_priority.json via prio.py; tier first, then within-tier rank
    _pd = prio.load(log)
    _bt = sum(int(v or 0) for v in (st.get("balls") or {}).values())
    _zdead = bool(z and z["hp"] <= 0)  # REVIVEFIX 10/30: fainted primary is never a heal target
    if _zdead: heal_need = False
    emerg = (not _zdead) and zr < 0.25 and risky_next and any(("full restore" in x["n"].lower() or "max potion" in x["n"].lower()) for x in rew)
    flags = dict(lure_active=(st.get("lure_left") or 0) > 0, out_of_balls=_bt <= 0, holding_balls=_bt > 0, heal_need=bool(heal_need),
                 role_low=bool(role_low), pp_crit=bool(pp_crit), pp_low=bool(pp_low), secondary_in_party=feebas, ally_dead=ally_dead,
                 zhp_low=bool(zhp_low), zacian_fainted=bool(z and z["hp"] <= 0), voucher_crit=emerg, emergency=emerg,
                 dna_pair=bool(dna_pair(st.get("party"))), zacian_in_party=bool(z) and any('sword' in s.lower() for s in PROF()['signature_items']), role_dead=bool(role_dead),
                 secondary_is_feebas=bool(sec and (sec.get("sp") == 349 or sec.get("n") == "Feebas")), mewtwo_in_party=any(p.get("sp") == 150 and (p.get("hp") or 0) > 0 for p in (st.get("party") or [])), absol_in_party=any(p.get("sp") == 359 and (p.get("hp") or 0) > 0 for p in (st.get("party") or [])), eelektross_in_party=any(p.get("sp") == 604 and (p.get("hp") or 0) > 0 for p in (st.get("party") or [])))
    _rk = {id(r): prio.rank_item(r, flags, _pd) for r in rew}
    _pf = PROF(); _zm = [m["n"] for m in (st.get("zmoves") or [])]
    for r in rew:  # AGNOSTIC: profile signature items rank like the sword; profile-approved TMs rank -50 (below candy)
        _n = r["n"].lower()
        if z and any(s.lower() in _n for s in _pf["signature_items"]) and _rk[id(r)][2] != "sword":
            _rk[id(r)] = ((0, _pd["specials"].get("sword", -290), 0), _pd["specials"].get("sword", -290), "signature")
        _mv = r.get("mv"); _tmn = r.get("mvn")
        if z and _mv and _tmn and _pf.get("learn_moves") and _mv in (st.get("ptm") or []) and st.get("zmoves"):
            _ix = learn_decide(_pf, [dict(n=m["n"], type=m.get("type"), pow=m.get("pow"), cat=m.get("cat")) for m in st["zmoves"]], dict(n=_tmn, type=r.get("mvt"), pow=r.get("mvp"), cat=r.get("mvc"), acc=r.get("mva")))
            if LEARN_NOTE[0] and _tmn not in _tm_logged: _tm_logged.add(_tmn); log(f"LEARN TM {_tmn}: {LEARN_NOTE[0]}")
            if _ix is not None:
                _rk[id(r)] = ((1, -_pd["tier_order"].get(prio.TN.get(r.get("t") or 0, ""), 0), -50), -50, "profile_tm"); tm_ok[r["n"]] = _ix
    for r in rew:  # EVOITEM: rank evolution items top when a non-primary/non-secondary party member can use it
        _lcn = r["n"].lower()  # LINKCORD 11/06 fix: game name is "Linking Cord"; evo may be None while Kadabra is secondary
        if r.get("evo") is None and not ("link" in _lcn and "cord" in _lcn and any(p.get("sp") == 64 and (p.get("hp") or 0) > 0 for p in (st.get("party") or []))): continue
        _pt = st.get("party") or []
        _ts = "thunder stone" in r["n"].lower()  # ETERNTEAM t200u: Thunder Stone -> Eelektrik (603) -> Eelektross
        _el = [p for p in _pt if p.get("i") in (r.get("evo") or []) and p is not z and (p is not sec or (_ts and p.get("sp") == 603)) and p.get("sp") not in (349, 350) and (p.get("hp") or 0) > 0]
        if _ts and not _el and sec and sec.get("sp") == 603 and (sec.get("hp") or 0) > 0: _el = [sec]
        _lc = ("link cord" in r["n"].lower() or "linking cord" in r["n"].lower())  # ALAKA t226u: Link Cord -> Kadabra (64) secondary
        if _lc: _el = [p for p in _pt if p.get("sp") == 64 and (p.get("hp") or 0) > 0] or _el
        _el.sort(key=lambda p: p.get("sp") not in EVO_PREF)
        if _el:
            _er = -360 if ((_ts and _el[0].get("sp") == 603) or (_lc and _el[0].get("sp") == 64)) else -280  # Thunder Stone for Eelektrik ranks just under Eelektrossite, far above Nugget
            EVO_TGT[r["n"].lower()] = _el[0].get("sp"); _rk[id(r)] = ((0, _er, 0), _er, "evo_item")
            if getattr(pick_reward, "_evl", None) != (w0, r["n"]): pick_reward._evl = (w0, r["n"]); log(f"EVO ITEM {r['n']} -> {_el[0]['n']} (eligible {[p['n'] for p in _el]})")
        else:
            EVO_TGT.pop(r["n"].lower(), None)
    for r in rew:  # ALAKA t226u: Alakazamite top when Alakazam (65) alive in party
        if "alakazamite" in r["n"].lower() and any(p.get("sp") == 65 and (p.get("hp") or 0) > 0 for p in (st.get("party") or [])): _rk[id(r)] = ((0, -370, 0), -370, "alakazamite")
    for r in rew:  # NECRO t233u: Necrozma (800) form-change items top priority when Necrozma alive
        if any(k in r["n"].lower() for k in ("n-solarizer", "n-lunarizer", "ultranecrozium", "n solarizer", "n lunarizer")) and any(p.get("sp") == 800 and (p.get("hp") or 0) > 0 for p in (st.get("party") or [])): _rk[id(r)] = ((0, -370, 0), -370, "necrozma_form")
    _HSTAT = ("potion", "full restore", "full heal", "berry", "heal", "ether", "elixir", "antidote", "awakening", "burn heal", "ice heal", "paralyze heal")
    _sec_ok = bool(sec and sec["hp"] > 0 and SEC_ALLOW_HEAL and _r(sec) < 0.75)
    if _zdead:
        for r in rew:  # REVIVEFIX: with primary fainted, revive ranks first; heal/berry/status/PP items are junk (unless secondary may take a needed heal)
            _n = r["n"].lower()
            if "revive" in _n or "sacred ash" in _n or "reviver seed" in _n:
                _rk[id(r)] = ((-9, -300, 0), -300, "role_revive")
            elif any(k in _n for k in _HSTAT) and not (_sec_ok and "berry" not in _n and any(k in _n for k in ("potion", "full restore"))):
                _rk[id(r)] = ((9, 99, 0), 99, "fainted_primary_no_heal")
    _dmt = [m for m in (st.get("zmoves") or []) if m.get("max")]
    _pp50 = bool(_dmt) and sum(m["left"] for m in _dmt) / sum(m["max"] for m in _dmt) < 0.5  # XFERLEPPA 11/04
    if (pp_low or _pp50) and not pp_crit and not _zdead:  # XFERLEPPA 11/04: Ether/Elixir beat nuggets/Leppa when primary PP low (Big Nugget beat Ether w67)
        for r in rew:
            if any(k in r["n"].lower() for k in PP_ITEMS) and _rk[id(r)][1] > -30: _rk[id(r)] = ((0, -30, 0), -30, "pp_low_top")
    if pp_crit and not _zdead:  # PPCRIT 11/01: tier-first let ULTRA/GREAT items beat Max Ether while PP was critical (w114-118 Lugia ran all moves to 0 PP)
        for r in rew:
            if any(k in r["n"].lower() for k in PP_ITEMS): _rk[id(r)] = ((0, -60, 0), -60, "pp_crit_top")
    TN = {0: "COMMON", 1: "GREAT", 2: "ULTRA", 3: "ROGUE", 4: "MASTER", 5: "LUXURY"}
    _pu = _pf.get("pp_up_pref") or {}  # TGTMOVES t205u/t206u: profile nudges PP Up/PP Max when a target move has low max PP (no-op without the field)
    if _pu and z and not _zdead:
        _tgs = set(_pf.get("target_moveset") or [m["n"] for m in (st.get("zmoves") or [])])
        _low = [m for m in (st.get("zmoves") or []) if m["n"] in _tgs and m.get("max") and m["max"] <= int(_pu.get("max_pp_at_most", 10))]
        if _low:
            for r in rew:
                _k0 = _rk[id(r)]
                if any(k in r["n"].lower() for k in _pu.get("items", ["pp up", "pp max"])) and TN.get(r.get("t"), "") in set(_pu.get("tiers", ["GREAT", "ULTRA"])) and _k0[0][0] == 1:
                    _b = float(_pu.get("rank_bonus", 3)); _rk[id(r)] = ((1, _k0[0][1], _k0[0][2] - _b), _k0[1] - _b, str(_k0[2]) + "+pp_up_pref")
    def rank(r): return _rk[id(r)][1]
    best = min(rew, key=lambda r: _rk[id(r)][0])
    bn = best["n"].lower()
    _k = (w0, best["n"]); _seen = _k == getattr(pick_reward, "_rl", None); pick_reward._rl = _k
    if not _seen and any(k in bn for k in PP_ITEMS) and pp_crit: log(f"PP item taken (critical) w{w0}: {best['n']}")
    elif not _seen and any(any(k in x["n"].lower() for k in PP_ITEMS) for x in rew): log(f"PP item skipped (pp ok) w{w0} -> {best['n']}")
    if _seen: pass
    elif role_dead and ("revive" in bn or "sacred ash" in bn): log(f"ROLE REVIVE w{w0}: {best['n']} for fainted {role_dead}")
    elif role_low and any(k in bn for k in HEAL): log(f"ROLE HEAL w{w0}: {best['n']} for low {role_low}")
    pick_reward.last_rank = rank(best)
    TN = {0: "COMMON", 1: "GREAT", 2: "ULTRA", 3: "ROGUE", 4: "MASTER", 5: "LUXURY"}
    ranked = [(round(_rk[id(r)][1], 3), r["n"], TN.get(r.get("t"), r.get("t")), _rk[id(r)][2]) for r in sorted(rew, key=lambda r: _rk[id(r)][0])]
    return best["i"], f"{best['n']} tier={TN.get(best.get('t'), best.get('t'))} ranking={ranked} (rank {rank(best)}, pp_low={pp_low}, flags={[k for k, v in flags.items() if v is True]}, heal_need={bool(heal_need)}, zhp={zr:.0%}, risky_next={risky_next}) from {[r['n'] for r in rew]}"

REROLL_CHEAP_FRAC = 0.10  # Gavin t140u: back to 10%
REROLL_CHEAP_MAX = 3
REROLL_MAX = 5  # Gavin t140u
ETERNATUS_STOP_WAVE = int(__import__("os").environ.get("PR_ETERNATUS_STOP_WAVE", "200"))  # Gavin t138u: stop for hand Eternatus catch
REROLL_DECAY = 0.6
PP_CONSERVE_ABS = 5
PP_CONSERVE_FRAC = 0.34
def pick_move(st, hist, dead=()):
    moves = [m for m in (st.get("moves") or []) if m["n"] not in dead]
    _impl = [m for m in moves if not str(m["n"]).endswith("(N)")]  # NMOVE 0340: skip unimplemented "(N)" moves (Bide loop w190)
    if any(m["left"] > 0 and m.get("cat") != 2 for m in _impl): moves = _impl
    doubles = st.get("double")
    _pf = PROF(); _is_p = st.get("user") == PRIMARY[0]
    if _is_p and any(e.get("sh") for e in (st.get("enemy") or [])) and not st.get("trainer"):
        _ns = [m for m in moves if m["n"] not in set(_pf["spread_moves"])]
        if _ns: moves = _ns  # doubles shiny rule: never spread moves while a wild shiny is out
    _av = set(_pf.get("avoid_in_battle", [])) if _is_p else set()
    if _av:  # t148u: skip avoided moves (Future Sight) unless nothing else usable has PP
        _na = [m for m in moves if m["n"] not in _av and m["left"] > 0 and m.get("cat") != 2]
        if _na:
            if any(m["n"] in _av for m in moves): log(f"AVOID skip {[m['n'] for m in moves if m['n'] in _av]}")
            moves = [m for m in moves if m["n"] not in _av]
    pm = _pf.get("primary_move") if _is_p else None
    if pm:
        _p = next((m for m in moves if m["n"] == pm and m["left"] > 0), None)
        if _p and max(_p.get("effs") or [1]) >= 1:
            _lowp = _p["left"] < PP_CONSERVE_ABS or (_p.get("max") and _p["left"] / _p["max"] < PP_CONSERVE_FRAC)
            _better = [m for m in moves if m is not _p and m["left"] > 0 and m.get("cat") != 2 and max(m.get("effs") or [1]) >= 2 * max(_p.get("effs") or [1])]
            if not _lowp and not _better: return _p
    cands = []
    # TYNAMO t199u: doubles + Levitate partner (Tynamo line) alive on field + no wild shiny -> Earthquake allowed/preferred
    _eq_ok = bool(_is_p and doubles and not any(e.get("sh") for e in (st.get("enemy") or [])) and any(p.get("sp") in LEVITATE_PARTNER and p.get("f") and (p.get("hp") or 0) > 0 for p in (st.get("party") or [])))
    for m in moves:
        if m["left"] <= 0 or m.get("cat") == 2: continue
        if doubles and m["type"] == GROUND and m["n"] == "Earthquake" and not _eq_ok: continue
        if m["type"] == GROUND and any((e.get("ab") or "") in ("Levitate", "Lightning Rod_") for e in (st.get("enemy") or [])): continue
        effs = m.get("effs") or [1]
        if max(effs) <= 0: continue
        pw = m["pow"] if m["pow"] and m["pow"] > 0 else 40
        score = pw * max(effs) * (1.5 if m["stab"] else 1.0)
        if m["n"] == "Earthquake": score *= (1.25 if _eq_ok else 0.8)  # soft avoid; TYNAMO t199u: prefer in doubles w/ Levitate partner
        if hist and hist[-1] == m["n"]: score *= 0.85
        cands.append([score, m])
    if not cands:
        # fallback (farm17 patch 09:25): any damaging move with PP, ignoring soft rules, so we never loop Fight<->back
        fb = [m for m in moves if m["left"] > 0 and m.get("cat") != 2]
        if fb:
            fb.sort(key=lambda m: -(max(m.get("effs") or [1]) > 0)); return fb[0]
        return None
    # never same move >2 in a row if any alternative exists
    if len(hist) >= 2 and hist[-1] == hist[-2]:
        alt = [c for c in cands if c[1]["n"] != hist[-1]]
        top = max(cands, key=lambda c: c[0])
        # allow a 3rd repeat only if it is >2x better than any alternative (e.g. 4x vs 0.5x)
        if alt and not (top[1]["n"] == hist[-1] and top[0] > 2 * max(a[0] for a in alt)):
            cands = alt
    cands.sort(key=lambda c: -c[0])
    top = cands[0]; tm = top[1]
    def _low(m): return m["left"] < PP_CONSERVE_ABS or (m.get("max") and m["left"] / m["max"] < PP_CONSERVE_FRAC)
    def _e(m): return max(m.get("effs") or [1])
    if _low(tm):
        alts = [c for c in cands[1:] if not _low(c[1]) and c[0] >= 0.5 * top[0] and _e(c[1]) >= _e(tm) / 2]
        only_se = _e(tm) >= 2 and all(_e(c[1]) < 1 for c in cands[1:])
        if alts and not only_se:
            log(f"PP CONSERVE skip {tm['n']} ({tm['left']}/{tm.get('max')}) -> {alts[0][1]['n']}")
            return alts[0][1]
    return tm

xfer_done = {}
tm_ok = {}  # AGNOSTIC: TM reward name -> slot to forget (approved by profile)
XFER_JS = r"""(()=>{const s=window.__pr_cam.scene;const h=s.ui.handlers.find(x=>x&&x.constructor.name=='ModifierSelectUiHandler');
const wv=s.currentBattle?s.currentBattle.waveIndex:0;const vis=!!(h&&h.transferButtonContainer&&h.transferButtonContainer.visible);const out={wv,vis,moved:[],failed:[]};if(wv%10!==1)return out;out.x1=true;
const party=s.getPlayerParty();const z=party.find(p=>p.species&&(window.__pr_prim||[888]).includes(p.species.speciesId));if(!z){out.err='no zacian';return out}
const SRC=['Linoone','Zigzagoon','Boltund','Yamper'];
const M=party.find(p=>p.species&&(window.__pr_sec||[602,603,604]).includes(p.species.speciesId))||party.find(p=>p.species&&[349,350].includes(p.species.speciesId));out.order='primary>secondary';
try{for(const m of s.findModifiers(m=>m.pokemonId===z.id&&/^(FLAME|TOXIC)_ORB$/.test(m.type.id||''))){const nm=m.type.name;let why=null;if(/FLAME/.test(m.type.id||''))why='flame orb goes to nobody';else if(!M)why='secondary not in party';else if(M.hp<=0)why='secondary fainted';else if(s.findModifier(o=>o.pokemonId===M.id&&/^TOXIC_ORB$/.test((o.type&&o.type.id)||'')))why='secondary already holds toxic orb';
 if(why){(out.porb=out.porb||[]).push('KEPT '+nm+' on primary: '+why);continue}
 let ok=false;try{ok=s.tryTransferHeldItemModifier(m,M,false,m.stackCount,true,true)}catch(e){why=String(e)}(out.porb=out.porb||[]).push(ok?('MOVED '+nm+' primary->secondary'):('KEPT '+nm+' on primary: '+(why||'refused')))}}catch(e){out.porb_err=String(e)}
for(const p of party){if(p===z||p===M||!(SRC.includes(p.species.name)||(p.fusionSpecies&&SRC.includes(p.fusionSpecies.name))))continue;
 const mods=s.findModifiers(m=>m.pokemonId===p.id&&m.isTransferable!==false);
 for(const m of mods){const nm=m.type.name;const q=m.stackCount;let ok=false,to=null;const orb=/^(FLAME|TOXIC)_ORB$/.test(m.type.id||'');
  const T=orb?(/FLAME/.test(m.type.id||'')?[]:[M]):(/lum berry/i.test(nm)?[z]:[z,M]);
  for(const t of T){if(!t){out.failed.push(nm+':no secondary');continue}const tn=t===z?'primary':'secondary';
   try{const mx=m.getMaxStackCount?m.getMaxStackCount():99;const ex=s.findModifier(o=>o.pokemonId===t.id&&o.matchType&&o.matchType(m));
    if(ex&&ex.stackCount>=mx){out.failed.push(nm+':'+tn+' max');continue}
    ok=s.tryTransferHeldItemModifier(m,t,false,q,true,true);}catch(e){out.failed.push(nm+':'+tn+':'+e);continue}
   if(ok){to=tn;break}else out.failed.push(nm+':'+tn+' refused')}
  if(ok)out.moved.push(p.species.name+'>'+nm+' x'+q+'->'+to);}}
try{s.updateModifiers(true)}catch(e){}return out})()"""

async def main():
    page = find_page()
    async with websockets.connect(page["webSocketDebuggerUrl"], max_size=50_000_000) as ws:
        n = 0
        async def call(method, params=None):
            nonlocal n; n += 1
            await ws.send(json.dumps({"id": n, "method": method, **({"params": params} if params else {})}))
            while True:
                r = json.loads(await ws.recv())
                if r.get("id") == n: return r
        async def ev(expr):
            r = await call("Runtime.evaluate", {"expression": expr, "returnByValue": True})
            return ((r.get("result") or {}).get("result") or {}).get("value")
        async def key(k, code, kc, h=90):
            d = {"type": "keyDown", "windowsVirtualKeyCode": kc, "code": code, "key": k}
            if len(k) == 1: d["text"] = k
            await call("Input.dispatchKeyEvent", d); await asyncio.sleep(h / 1000)
            await call("Input.dispatchKeyEvent", {"type": "keyUp", "windowsVirtualKeyCode": kc, "code": code, "key": k})
        async def Z(): await key("z", "KeyZ", 90)
        async def UP(): await key("ArrowUp", "ArrowUp", 38)
        async def X(): await key("x", "KeyX", 88)   # cancel / back (never Escape)
        async def set_cursor(i):
            return await ev(f"(()=>{{const h=window.__pr_cam.scene.ui.getHandler();h.setCursor({i});return h.cursor}})()")
        async def shot(dirp, tag, fmt="jpeg"):
            try:
                dirp.mkdir(parents=True, exist_ok=True)
                r = await call("Page.captureScreenshot", {"format": fmt} | ({"quality": 70} if fmt == "jpeg" else {}))
                p = dirp / f"{tag}_{datetime.now():%H%M%S}.{'jpg' if fmt=='jpeg' else 'png'}"
                p.write_bytes(base64.b64decode(r["result"]["data"])); return p.name
            except Exception as e:
                log(f"shot fail {e}")
        async def pump(k=3):
            # PC is locked/occluded -> tab hidden -> no rAF. Each captureScreenshot forces a frame.
            for _ in range(k):
                await call("Page.captureScreenshot", {"format": "jpeg", "quality": 5, "clip": {"x": 0, "y": 0, "width": 8, "height": 8, "scale": 1}})
        await call("Page.bringToFront")
        await ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}})()")
        await ev(HOOK_JS); await asyncio.sleep(0.5)
        gi = await ev("window.gameInfo&&window.gameInfo.gameMode")
        log(f"START farm17 [reroll+vit+balls+tier+zswitch] (UI-state driven) mode={gi}")
        if gi != "Classic": log("ABORT not Classic"); return
        fb_fall = set(); pk_w = {}
        _pk = await ev(PICKUP_JS)
        try: _fb = await ev("(()=>{try{return window.__pr_cam.scene.getPlayerParty().some(p=>p.species&&p.species.speciesId===349||p.name==='Feebas')}catch(e){return String(e)}})()")
        except Exception as e: _fb = e
        log(f"FEEBAS rules active: feebas_in_party={_fb} berry_rule pickup_present={_pk}"); log(f"HARD_WAVES={sorted(HARD_WAVES)} sig={SIG_FILE}"); log(f"REROLL budget: total rerolls <= {REROLL_CHEAP_FRAC:.0%} of money at screen open, max {REROLL_MAX}/screen, shop floor kept"); log("MEGA: Mega Bracelet special -380, Swampertite -370 (Swampert alive) -> Swampert only"); log("MASTER BALL: special rank -400 (top pick); never thrown by farm; ETERNATUS stop at wave 200 (every run, Gavin t140u)"); log(f"REROLL cheap: <{REROLL_CHEAP_FRAC:.0%} of money, max {REROLL_CHEAP_MAX}/screen, respects shop floor"); log(f"PP CONSERVE: low<{PP_CONSERVE_ABS} or <{PP_CONSERVE_FRAC:.0%}"); log(f"SHOP proactive: spend<={SHOP_MAX_SPEND_FRAC:.0%} reserve>={SHOP_RESERVE_FRAC:.0%} floor={SHOP_MIN_RESERVE} hurt<{SHOP_HURT:.0%} minmiss>={SHOP_MIN_MISS_FRAC:.0%} (hard: spend<={SHOP_HARD_SPEND_FRAC:.0%} hurt<{SHOP_HARD_HURT:.0%})"); log("SWORD: Rusted/Ancient Sword rank -290 -> PRIMARY"); log("PRISM SCALE: rank -290 + apply to SECONDARY while Feebas"); log("PP items: rank 94 unless pp_crit (dmg PP<=3 or all SE moves 0)"); log("FREEZE-DRY: game getMoveEffectiveness (+573 vs Water fallback)"); log("EVIOLITE: rank 96 junk (secondary only-candy)"); log(f"ROLES primary={PRIMARY[0]} secondary={SECONDARY[0]}/Milotic"); log(f"SECFIELD forced bench={SECFIELD_FORCE_BENCH} PARTY_ORDER_FIX={PARTY_ORDER_FIX}"); log(f"SECONDARY gets ONLY Rare Candy/Candy Jar; all else -> Zacian. SEC_ALLOW_PRISM={SEC_ALLOW_PRISM} SEC_ALLOW_REVIVE={SEC_ALLOW_REVIVE} SEC_ALLOW_HEAL={SEC_ALLOW_HEAL}"); log("BATTLE ITEMS: X SpAtk/SpDef/Acc rank 96, X Atk/Def/Spd + Dire Hit rank 93, best>=93 -> REROLL junk (shared 10% budget, max 5, decay, reserve)"); log("LURE: rank -15 (secondary in party) if none active, 100.5 (worst of all, below balls/TMs/DNA) while active"); log("SOOTHE target=secondary-first (until max stack, then Zacian) SEC_ALLOW_SOOTHE=True"); log("ENCOUNTER RULES: encounter_rules.json (editor) for non-safety MEs; hardcoded TRADE BLOCK/xform-leave/shady pricey/training leave/chest LEAVE"); log("ME overrides: shadyVitaminDealer -> pricey (opt 2, else leave; never cheap); trainingSession -> leave (never a tier)"); log("DNA SPLICERS: rank -250 only if unfused Kricketot/Kricketune + Zigzagoon/Linoone (base=Kricketot first via Apply, partner second via Splice), else 99"); log("RANKING: data-driven item_priority.json (tier first MASTER>ROGUE>ULTRA>GREAT>COMMON, then rank; junk>=93 regardless of tier; specials sword/prism/role revive/DNA pair/emergency heal on top)"); prio.load(log, force=True); log("CANDY priority: Candy Jar/Rare Candy top (-55, below Master/Rogue tier, above vouchers)"); cfg_reload(); log(f"CANDY_TARGET={CFG['candy_target']} (Rare Candy; Soothe Bell -> secondary-first rank -99.5; default {CANDY_TARGET}) file={CONFIG_FILE}"); log(f"SECONDARY_FIELD={CFG['secondary_field']} (Secondary in singles; default {SECONDARY_FIELD}; auto=wild single, no boss/hard, Feebas>=40% Zacian>=50%, 1/wave, 2 faints->bench)")
        party_tries = 0; stepping_logged = False; rew_bad = {}; last_pick = [None]; skip_yes = [False]
        hist = []; last_sig = None; same = 0; last_wave = None; framed = set(); last_rew_wave = None; shot_w = set(); lep_try = set(); faint_n = 0; me_noparty = set()
        sw_try = {}; sw_turn = set(); reroll_n = {}; reroll_log = {}; cheap_n = {}; hard_w = {}; sig_pend = {}; rr_spent = {}; shop_pend = [None]; shop_tgt = [None]; shop_fail = {}; shop_n = {}; shop_open = {}; dead_moves = {}; me_sig = None; me_t0 = time.time(); last_zlog = None; zmiss = 0; title_cont = [0]; lure_log = {}; shop_skip = {}; reorder_w = {}; shop_monfail = {}
        sf = {"pend": None, "done": set(), "tries": {}, "out": None, "faints": 0, "bench_run": False, "skiplog": set(), "sec_hp": None}; candy_n = [0]
        egg_t = [0.0]; log("TRADE BLOCK: darkDeal/GTS/wonder trade/any trade ME -> leave (last option)"); log("RUN LOG active (run end -> row at top of Run Log.md: party/lv/variant/fusion, luck, primary items, wiper)"); log("ORB active (Toxic Orb -> Tynamo line secondary only; Flame Orb -> nobody)"); log(f"SEC STATUS: SEC_NO_STATUS_CURE={SEC_NO_STATUS_CURE} - Milotic burn/poison never cured (no Full Heal/Full Restore/Lum/cures); shop heals Milotic only when HP<{SHOP_HURT:.0%}, plain potions; status alone buys nothing"); log("EVO ITEM active (evolution item -> eligible non-Lugia/non-Milotic member, Sinistea first; none eligible -> normal rank)"); log("ORBFIX active (transfer waves: primary Flame/Toxic Orb -> Milotic; kept+logged if Milotic absent/fainted/holds orb; no Full Heal for primary while it holds orb)"); log("PICKUP TRANSFER order: primary first, leftovers (max/refused) -> secondary; Toxic Orb -> secondary only, Flame Orb kept"); log(f"EGG HATCH log active -> {EGG_LOG_MD}"); krick_t = [0.0]; log("KRICKETOT evo pause active (species 401 pauseEvolutions=true, EvolutionPhase -> cancel+Yes)")
        while True:
            if STOP.exists(): log("STOP flag"); break
            try:
                if time.time() - egg_t[0] > 1.0:
                    egg_t[0] = time.time()
                    try:
                        eg = await ev(EGG_JS)
                        if isinstance(eg, dict):
                            if eg.get("err") and time.time() - globals().get("_egg_err_t", 0) > 30: globals()["_egg_err_t"] = time.time(); log(f"EGG poll JS err {eg['err'][:120]}")
                            for _r in eg.get("list") or []: egg_record(_r, (st.get("wave") if "st" in dir() and isinstance(st, dict) else None))
                    except Exception as e: log(f"EGG err {e}")
                if time.time() - globals().get("_audit_t", 0) > 3:
                    globals()["_audit_t"] = time.time()
                    try: hatch_audit(await ev(AUDIT_JS), (st.get("wave") if "st" in dir() and isinstance(st, dict) else None))
                    except Exception as e: log(f"HATCH AUDIT err {e}")
                if time.time() - krick_t[0] > 3:
                    krick_t[0] = time.time()
                    try:
                        kr = await ev(KRICK_JS)
                        if isinstance(kr, dict):
                            for _i in kr.get("set") or []: log(f"KRICKETOT evo paused (party idx {_i})")
                            if kr.get("evo"):
                                log("KRICKETOT EvolutionPhase seen -> cancel + pause"); await X(); await asyncio.sleep(0.6); await Z(); await asyncio.sleep(0.4)
                    except Exception as e: log(f"KRICK err {e}")
                if (await ev("window.gameInfo&&window.gameInfo.gameMode")) == "Endless": log("Endless STOP"); break
                # PC locked -> tab hidden -> Chrome stops rAF, Phaser freezes. Drive frames manually.
                adv = await ev(STEP_JS)
                if isinstance(adv, str): log(f"step err {adv[:160]}")
                elif adv and adv.get("hidden") and not stepping_logged:
                    log(f"tab hidden: manual frame stepping on (frame {adv.get('frame')})"); stepping_logged = True
                st = await ev(STATE_JS)
                if not st or st.get("err"):
                    await ev(HOOK_JS); await asyncio.sleep(0.5); continue
                h = st.get("h"); party = st.get("party") or []
                try:
                    _wv = st.get("wave")
                    if sig_pend.get("probe") != _wv and st.get("ph") == "CommandPhase":
                        sig_pend["probe"] = _wv; sj = await ev(SIG_JS) or {}
                        if sj.get("tr") or sj.get("bosses"):
                            _z = role(party, PRIMARY); _s2 = role(party, SECONDARY)
                            sig_pend["rec"] = {"run_id": RUN_ID, "ts": datetime.now().isoformat(), "wave": _wv, "biome": sj.get("biome"), "trainer": sj.get("tr"), "trainer_type": sj.get("tt"), "bosses": sj.get("bosses"), "is_rival": sj.get("rival"), "fixed": sj.get("fixed"), "zacian_before": _z and [_z["hp"], _z.get("mx")], "secondary_before": _s2 and [_s2["hp"], _s2.get("mx")]}
                            log(f"SIG WAVE {_wv} {sj.get('tr') or sj.get('bosses')}")
                    if sig_pend.get("rec"):
                        for _p in (role(party, PRIMARY), role(party, SECONDARY)):
                            if _p and _p.get("mx"): sig_pend["minr"] = min(sig_pend.get("minr", 1), _p["hp"] / _p["mx"])
                except Exception as e: log(f"SIG probe error {e}")
                _wv0 = st.get("wave") or 0
                if party and (globals().get("_prim_w") is None or _wv0 < globals()["_prim_w"] or (role(party, PRIMARY) is None and _wv0 <= 1)):
                    if resolve_primary(party, log) is not None:
                        await ev("window.__pr_prim=" + json.dumps(sorted(PRIMARY[1])) + ";window.__pr_sec=" + json.dumps(sorted(SECONDARY[1])))
                        globals()["_prim_w"] = _wv0
                if party and globals().get("_prim_w") is not None: globals()["_prim_w"] = max(globals()["_prim_w"], _wv0)
                z = role(party, PRIMARY)
                if z is None and h == "TitleUiHandler" and faint_n == 0 and title_cont[0] < 5:
                    # page reloaded mid-run (no faint seen): Continue the saved Classic session (never New Game/Endless)
                    lab = await ev("(()=>{const h=window.__pr_cam.scene.ui.getHandler();return (h.config?.options||[]).map(o=>o.label)[h.cursor]})()")
                    if lab == "Continue":
                        title_cont[0] += 1; log(f"title after reload (no faint) -> Continue #{title_cont[0]}"); await Z(); await asyncio.sleep(4); zmiss = 0; continue
                if z is None:
                    # not in party at all (ME / transient read) - NOT a faint; wait long before giving up
                    zmiss += 1
                    if zmiss in (1, 10): log(f"PRIMARY {PRIMARY[0]} missing from party read (h={h} ph={st.get('ph')}) party={[(p['n'],p['hp']) for p in party]}")
                    me_live = await ev("(()=>{try{const s=window.__pr_cam.scene;return !!(s.currentBattle&&s.currentBattle.mysteryEncounter)}catch(e){return false}})()")
                    if me_live:
                        if zmiss in (1, 40) or zmiss % 200 == 0: log(f"ME battle limits party (Zacian absent) - fighting with active member, h={h} ph={st.get('ph')}")
                        if h in ("CommandUiHandler", "FightUiHandler", "BattleMessageUiHandler", "ModifierSelectUiHandler", "MysteryEncounterUiHandler", "PartyUiHandler") or zmiss % 6 == 0:
                            if h == "FightUiHandler":  # MEFIGHT patch 11-01: pick a move with PP (was blind Z on a 0-PP move -> loop)
                                _mm = pick_move(st, [], ())
                                if _mm is not None:
                                    if globals().get("_me_last") != _mm["n"]: log(f"ME fight {st.get('user')} -> {_mm['n']} PP={[(q['n'], q['left']) for q in st.get('moves') or []]}"); globals()["_me_last"] = _mm["n"]
                                    await set_cursor(_mm["i"]); await asyncio.sleep(0.1)
                            await Z()
                        await asyncio.sleep(1.0); continue
                    if zmiss < 60: await asyncio.sleep(0.5); continue
                    log(f"PRIMARY {PRIMARY[0]} MISSING 30s+ (no ME) - stop"); await shot(FRAMES, "zacian_missing"); break
                zmiss = 0
                if z["hp"] <= 0:
                    faint_n += 1
                    if faint_n < 4: await asyncio.sleep(0.6); continue
                    if any(p["hp"] > 0 for p in party if p is not z):
                        if faint_n == 4:
                            log(f"PRIMARY {PRIMARY[0]} FAINT w{st.get('wave')} - partners alive, keep fighting + revive on rewards")
                            await shot(FRAMES, "zacian_faint")
                        faint_n = 5
                    elif faint_n < 14:
                        if faint_n in (6, 13): log(f"ALL-FAINT read w{st.get('wave')} party={[(p['n'],p['hp']) for p in party]} - rechecking (transient?)")
                        await asyncio.sleep(0.6); continue
                    else:
                        log(f"PRIMARY {PRIMARY[0]} FAINT hp=0/{z.get('mx')} onField={z['f']} w{st.get('wave')} ph={st.get('ph')} foes={[(e['n'],e.get('ab')) for e in st.get('enemy') or []]} lastHP={last_zlog}")
                        await runlog_hook(ev, [e['n'] for e in st.get('enemy') or []])  # RUNLOG 11/01
                        await shot(FRAMES, "zacian_faint"); break
                else: faint_n = 0
                zl = (z["hp"], z.get("mx"), z["f"])
                if zl != last_zlog:
                    if last_zlog and last_zlog[2] and not z["f"]: log(f"PRIMARY {z['n']} switched OUT (alive) - not a faint")
                    log(f"ZHP w{st.get('wave')} {z['hp']}/{z.get('mx')} onField={z['f']} ph={st.get('ph')}"); last_zlog = zl
                    if z["hp"] == 0 and len(party or []) == 1: log(f"SOLO EARLY DEATH: solo primary {z['n']} fainted at w{st.get('wave')} (one-mon party; last run died w22 to wild Mudbray)")
                w = st.get("wave")
                if (w or 0) >= ETERNATUS_STOP_WAVE:
                    log(f"ETERNATUS STOP: wave {w} reached -> no input, stop flag (hand catch; Master Ball reserved)")
                    _bc = await ev("(()=>{try{return window.__pr_cam.scene.pokeballCounts}catch(e){return null}})()")
                    sp = await shot(SHOT_DIR, f"eternatus_w{w}", "png")
                    STATUS.write_text(json.dumps({"ts": datetime.now().isoformat(), "script": "pr_farm17.py", "wave": w, "stopped_reason": "eternatus_catch", "pokeball_counts": _bc, "party": [{k: q.get(k) for k in ("n", "hp", "mx")} for q in (party or [])], "screenshot": str(sp)}, indent=1), encoding="utf-8")
                    STOP.write_text(f"eternatus_catch wave {w}", encoding="utf-8")
                    try: (OUT / "pokerogue_farm_stop_reason.txt").write_text("eternatus_catch - do not restart; hand catch per ETERNATUS_PLAN.md (Gavin t138u)", encoding="utf-8")
                    except Exception: pass
                    return
                if w != last_wave:
                    if last_wave is not None: log(f"WAVE UP {last_wave} -> {w}")
                    cfg_reload(log)
                    try:
                        if sig_pend.get("rec") and sig_pend["rec"]["wave"] == last_wave:
                            rec = sig_pend.pop("rec"); _s2 = role(party, SECONDARY)
                            rec.update(outcome="won" if z and z["hp"] > 0 else "lost", zacian_after=z and [z["hp"], z.get("mx")], secondary_after=_s2 and [_s2["hp"], _s2.get("mx")], min_role_ratio=round(sig_pend.get("minr", 1), 3))
                            with SIG_JSONL.open("a", encoding="utf-8") as fh: fh.write(json.dumps(rec) + "\n")
                            SIG["records"] = SIG.get("records", 0) + 1; tl = SIG.setdefault("wave_tally", {}); tl[str(last_wave)] = tl.get(str(last_wave), 0) + 1
                            if rec.get("trainer") and sig_pend.get("minr", 1) < 0.5 and last_wave not in SIG.setdefault("learned_hard", []):
                                SIG["learned_hard"].append(last_wave); HARD_WAVES.add(last_wave); log(f"SIG learned hard wave {last_wave}")
                            SIG_FILE.write_text(json.dumps(SIG, indent=1), encoding="utf-8")
                    except Exception as e: log(f"SIG write error {e}")
                    sig_pend.clear()
                    last_wave = w
                    STATUS.write_text(json.dumps({"ts": datetime.now().isoformat(), "script": "pr_farm17.py", "wave": w,
                        "zacian": z, "party": party}, indent=1), encoding="utf-8")
                sig = json.dumps([h, st.get("cur"), st.get("om"), st.get("ph"), w, [m["left"] for m in st.get("moves") or []]])
                same = same + 1 if sig == last_sig else 0; last_sig = sig
                if h == "EggSummaryUiHandler" and same >= 4:
                    try:
                        _eg = await ev(EGG_JS)
                        for _r in (_eg or {}).get("list") or []: egg_record(_r, w)
                    except Exception as e: log(f"EGG pre-close poll err {e}")
                    log("EGG SUMMARY -> X (close hatch summary)"); await X()
                if same and same % 25 == 0:
                    log(f"STALL x{same} h={h} ph={st.get('ph')} cur={st.get('cur')} -> shot")
                    await shot(FRAMES, f"stall_{h}")
                    if h == "ModifierSelectUiHandler" and same >= 25:  # SMCB 10/31 18:55: lost onActionInput callback (w27 stall) -> rebuild it and re-show the reward screen
                        _rs = await ev("""(()=>{try{const s=window.__pr_cam.scene,h=s.ui.getHandler(),p=s.phaseManager.getCurrentPhase();if(h.constructor.name!=='ModifierSelectUiHandler'||p.constructor.name!=='SelectModifierPhase'||h.onActionInput)return 'ok';const cb=(e,t)=>{if(e<0||t<0)return false;if(e===0){if(t===0)return p.rerollModifiers();if(t===1)return p.openModifierTransferScreen(cb);if(t===3)return p.toggleRerollLock();return false}if(e===1)return p.selectRewardModifierOption(t,cb);return p.selectShopModifierOption(e,t,cb)};p.resetModifierSelect(cb);return 'reset'}catch(e){return 'ERR '+e}})()"""); log(f"SMCB stall fix: {_rs}")
                if h not in framed and h in ("FightUiHandler", "ModifierSelectUiHandler", "PartyUiHandler", "CommandUiHandler"):
                    framed.add(h); await shot(FRAMES, f"frame_{h}", "png")

                if "Mystery" in str(st.get("ph")) or h == "MysteryEncounterUiHandler":
                    msig = (h, st.get("ph"), st.get("cur"), st.get("om"))
                    if msig != me_sig: me_sig = msig; me_t0 = time.time()
                    elif time.time() - me_t0 > 20:
                        if h in ("SummaryUiHandler", "PokedexPageUiHandler"):
                            log(f"ME watchdog: {msig} stuck 20s in {h} -> X back"); await X(); me_t0 = time.time(); await asyncio.sleep(0.4); continue
                        log(f"ME watchdog: {msig} stuck 20s -> Up x4 + Z"); await shot(FRAMES, "me_watchdog")
                        for _ in range(4): await UP(); await asyncio.sleep(0.1)
                        await Z(); me_t0 = time.time(); await asyncio.sleep(0.4); continue
                else: me_sig = None
                if h != "PartyUiHandler": party_tries = 0
                shiny_en = [(k, e) for k, e in enumerate(st.get("enemy") or []) if e.get("sh")]
                if shiny_en and st.get("trainer"):
                    if globals().get("_tsh_wave") != w:
                        globals()["_tsh_wave"] = w; log(f"trainer shiny ignored: {','.join(x['n'] for _, x in shiny_en)} wave {w}")
                    shiny_en = []
                if shiny_en and h in ("CommandUiHandler", "FightUiHandler", "TargetSelectUiHandler", "BallUiHandler"):
                    k, e = shiny_en[0]
                    log(f"SHINY ENEMY: {e['n']} Lv{e.get('lv')} variant {(e['v']+1) if isinstance(e.get('v'),int) else '?'} wave {w} slot {k} (all={[x['n'] for _, x in shiny_en]}) -> STOP, no input")
                    if st.get("double") and len(st.get("enemy") or []) > 1: log("DOUBLES SHINY RULE: " + DOUBLES_SHINY_RULE)
                    sp = await shot(SHOT_DIR, f"shiny_enemy_w{w}", "png")
                    STATUS.write_text(json.dumps({"ts": datetime.now().isoformat(), "script": "pr_farm17.py", "wave": w,
                        "stopped_reason": "shiny_enemy", "shiny_species": e["n"], "shiny_slot": k, "shiny_variant": ((e["v"]+1) if isinstance(e.get("v"),int) else None), "shiny_level": e.get("lv"), "shiny_sid": e.get("sid"),
                        "shiny_all": [x["n"] for _, x in shiny_en], "trainer": st.get("trainer"), "double": st.get("double"),
                        "doubles_catch_rule": (DOUBLES_SHINY_RULE if st.get("double") and len(st.get("enemy") or []) > 1 else None),
                        "screenshot": str(sp)}, indent=1), encoding="utf-8")
                    STOP.write_text(f"shiny_enemy {e['n']} wave {w}", encoding="utf-8")
                    return
                if h == "CommandUiHandler":
                    wild_shiny = (not st.get("trainer")) and any(e["sh"] for e in st.get("enemy") or [])
                    if wild_shiny and not st.get("double"):
                        log(f"WILD SHINY {[(e['n'], 'variant', (e['v']+1) if isinstance(e.get('v'),int) else '?') for e in st['enemy'] if e['sh']]} -> Ball")
                        await shot(FRAMES, "wild_shiny"); await set_cursor(1); await Z()
                    else:
                        if wild_shiny: log("wild shiny in doubles - deferred (fight)")
                        # SECFIELD (Gavin OK 10/29): bring Feebas onto the field in singles for candy (participantIds)
                        do_sf = False
                        _sec = role(party, SECONDARY); _mode = CFG["secondary_field"]
                        if _sec:
                            if sf["sec_hp"] is not None and sf["sec_hp"] > 0 and _sec["hp"] <= 0 and sf["out"] == w:
                                sf["faints"] += 1; log(f"SECFIELD w{w}: Feebas fainted while fielded (#{sf['faints']})")
                                if _mode == "auto" and sf["faints"] >= 2 and not sf["bench_run"]: sf["bench_run"] = True; log("SECFIELD auto: 2 Feebas faints this run -> bench for rest of run")
                            sf["sec_hp"] = _sec["hp"]
                        if _sec and _mode != "bench" and not wild_shiny and st.get("ph") == "CommandPhase" and not st.get("double") and z["f"] and not _sec["f"] and w not in sf["done"]:
                            why = None
                            zr_ = z["hp"] / max(1, z.get("mx") or 1); sr_ = _sec["hp"] / max(1, _sec.get("mx") or 1)
                            if _mode == "auto" and sf["bench_run"]: why = "auto benched after 2 faints"
                            elif sf["tries"].get(w, 0) >= 2: why = "try cap"
                            elif w in HARD_WAVES: why = "hard wave"
                            elif _sec["hp"] <= 0: why = "Feebas fainted"
                            elif zr_ < 0.5: why = f"Zacian HP {zr_:.0%}"
                            elif sr_ < (0.4 if _mode == "auto" else 0.5): why = f"Feebas HP {sr_:.0%}"
                            elif _mode == "auto" and st.get("trainer"): why = "trainer"
                            elif any(e.get("sh") for e in st.get("enemy") or []): why = "shiny enemy"
                            if why is None:
                                sj2 = await ev(SIG_JS) or {}
                                if sj2.get("bosses"): why = "boss"
                                elif _mode == "auto" and sj2.get("fixed"): why = "fixed wave"
                                else:
                                    try: _tr = await ev("(()=>{try{const s=window.__pr_cam.scene;const f=s.getPlayerField()[0];return !!(f&&f.isTrapped&&f.isTrapped())}catch(e){return false}})()")
                                    except Exception: _tr = False
                                    if _tr: why = "trapped"
                            if why:
                                if (w, why) not in sf["skiplog"]: sf["skiplog"].add((w, why)); log(f"SECFIELD skip w{w} ({why}) mode={_mode}")
                                if why in ("hard wave", "boss", "trainer", "fixed wave", "try cap", "auto benched after 2 faints"): sf["done"].add(w)
                            else:
                                sf["tries"][w] = sf["tries"].get(w, 0) + 1; sf["pend"] = w; do_sf = True
                                log(f"SECFIELD w{w}: Feebas in (mode={_mode} try {sf['tries'][w]} Zacian {z['hp']}/{z.get('mx')} Feebas {_sec['hp']}/{_sec.get('mx')})")
                        if do_sf:
                            await set_cursor(2); await Z(); await asyncio.sleep(0.4); continue
                        if _sec and _sec["f"] and not z["f"] and sf["pend"] == w:
                            sf["done"].add(w); sf["out"] = w; sf["pend"] = None; log(f"SECFIELD w{w}: Feebas on field -> Zacian back next")
                        # ZACIAN SWITCH-IN (Gavin OK 14:21): Zacian alive, off field, healthy -> Pokemon menu
                        do_sw = False
                        if not wild_shiny and z["hp"] > 0 and not z["f"] and st.get("ph") == "CommandPhase" and sw_try.get(w, 0) < 2:
                            fld = [p for p in party if p["f"] and p["hp"] > 0]
                            usr = next((p for p in fld if p["n"] == st.get("user")), fld[0] if fld else None)
                            zr = z["hp"] / max(1, z.get("mx") or 1)
                            ur = (usr["hp"] / max(1, usr.get("mx") or 1)) if usr else 0
                            weakest = (not usr) or len(fld) < 2 or ur <= min(p["hp"] / max(1, p.get("mx") or 1) for p in fld)
                            trapped = await ev("(()=>{try{const s=window.__pr_cam.scene;const f=s.getPlayerField();const u=f[(s.phaseManager.getCurrentPhase().fieldIndex)||0];return !!(u&&u.isTrapped&&u.isTrapped())}catch(e){return false}})()")
                            turn = await ev("window.__pr_cam.scene.currentBattle.turn")
                            tk = (w, turn, st.get("fi"))
                            _zdry = bool([m for m in (st.get("zmoves") or []) if (m.get("pow") or 0) > 0]) and all(m["left"] <= 0 for m in (st.get("zmoves") or []) if (m.get("pow") or 0) > 0)  # PPDRY 11/04: never switch a 0-PP primary in to Struggle
                            if not _zdry and weakest and not trapped and tk not in sw_turn and (zr >= 0.5 or (zr > 0 and ur < 0.25)):
                                sw_turn.add(tk); do_sw = True
                                if any(k[0] == w and k != tk for k in sw_turn): sw_try[w] = sw_try.get(w, 0) + 1
                                log(f"ZACIAN SWITCH-IN w{w} turn {turn}: {usr and usr['n']} {usr and usr['hp']}/{usr and usr.get('mx')} -> Zacian {z['hp']}/{z.get('mx')} (try {sw_try.get(w,0)+1})")
                        if do_sw:
                            await set_cursor(2); await Z()
                        else:
                            if st.get("cur") != 0: await set_cursor(0)
                            await Z()
                elif h == "FightUiHandler":
                    # DISABLE 11/3: Disable/Torment/Taunt/Imprison-restricted moves looped forever (w89 Slowking Disable on Eelektrik Leech Life)
                    try:
                        _rs = await ev('(()=>{try{const s=window.__pr_cam.scene;const f=s.getPlayerField();const u=f[(s.phaseManager.getCurrentPhase().fieldIndex)||0];const tg=(u.summonData&&u.summonData.tags)||[];return u.getMoveset().filter(m=>{if(!m)return false;let r=false;try{r=!!(u.isMoveRestricted&&u.isMoveRestricted(m.moveId,u))}catch(e){};return r||tg.some(t=>t.moveId===m.moveId&&/Disable|Torment|Taunt|Imprison/.test(t.constructor.name))}).map(m=>m.getName())}catch(e){return []}})()') or []
                    except Exception:
                        _rs = []
                    _dead = set(dead_moves.get((w, st.get('user')), ())) | set(_rs)
                    if _rs: log(f"RESTRICTED {st.get('user')}: {_rs} -> skip")
                    m = pick_move(st, hist, _dead)
                    # ENCORE 11/1: Encore locks the user into one move; picking any other loops forever (w114 Rhyperior/Aeroblast)
                    try:
                        _enc = await ev('(()=>{try{const s=window.__pr_cam.scene;const f=s.getPlayerField();const u=f[(s.phaseManager.getCurrentPhase().fieldIndex)||0];const t=u&&u.summonData&&u.summonData.tags&&u.summonData.tags.find(t=>t.constructor.name==="EncoreTag");if(!t)return null;const ms=u.getMoveset();const k=ms.findIndex(m=>m&&m.moveId===t.moveId);return k>=0?{i:k,left:ms[k].getMovePp()-ms[k].ppUsed}:null}catch(e){return null}})()')
                    except Exception:
                        _enc = None
                    if _enc and (_enc.get('left') or 0) > 0 and (m is None or m.get('i') != _enc['i']):
                        _em = next((mm for mm in (st.get('moves') or []) if mm.get('i') == _enc['i']), None)
                        if _em:
                            log(f"ENCORE: locked into {_em['n']} -> use it"); m = _em
                    pps = {mm["n"]: f"{mm['left']}/{mm['max']}" for mm in st.get("moves") or []}
                    foes = [(e["n"], e["t"], e.get("ab")) for e in st.get("enemy") or []]
                    if m is None:
                        _mv = st.get("moves") or []
                        if _mv and all((mm.get("left") or 0) <= 0 for mm in _mv):
                            # STRUGGLE 11/1: all moves 0 PP -> confirming any move makes the game use Struggle (w120 Corviknight loop)
                            log(f"STRUGGLE: all moves 0 PP {pps} foes={foes} -> confirm move 0"); await set_cursor(0); await asyncio.sleep(0.1); await Z(); await asyncio.sleep(1.0)
                        else:
                            _any = [mm for mm in _mv if (mm.get("left") or 0) > 0]  # NOUSABLE 11/5: only status moves left (w89 Linoone Tidy Up vs Wonder Guard Shedinja looped) -> use one so the turn passes
                            if _any:
                                log(f"NOUSABLE: no damaging move {pps} foes={foes} -> use {_any[0]['n']} to pass turn"); await set_cursor(_any[0]["i"]); await asyncio.sleep(0.1); await Z(); await asyncio.sleep(1.0)
                            else:
                                log(f"no usable move {pps} foes={foes} dbl={st.get('double')} - back"); await X()
                    else:
                        if m["n"] == "Freeze-Dry" and max(m.get("effs") or [1]) >= 2: log(f"FREEZE-DRY vs {[e['n'] for e in st.get('enemy') or []]} eff={max(m['effs'])}")
                        log(f"w{w} {st.get('user')} -> {m['n']} eff={m['effs']} stab={m['stab']} PP={pps} foes={foes} dbl={st.get('double')}")
                        if st.get("user") == z["n"]: hist = (hist + [m["n"]])[-6:]
                        try:  # TARGETFIX 11/2: remember best foe for this move (w81 Shedinja Wonder Guard soaked every hit)
                            _en = [e["n"] for e in st.get("enemy") or []]; _ef = list(m.get("effs") or [])
                            TGT_PREF[0] = [n for _, n in sorted([(-(_ef[k] if k < len(_ef) else 1), _en[k]) for k in range(len(_en)) if (_ef[k] if k < len(_ef) else 1) > 0])]
                        except Exception: TGT_PREF[0] = None
                        await set_cursor(m["i"]); await asyncio.sleep(0.1); await Z()
                        # no-PP guard: if fight menu still open / 'no PP' msg after ~2s, mark move dead and try others
                        dk = (w, st.get("user")); tried = {m["n"]}
                        for _ in range(5):
                            stuck = False
                            for _t in range(8):
                                await asyncio.sleep(0.25); await ev(STEP_JS)
                                s2 = await ev(STATE_JS) or {}
                                txt = str(await ev("(()=>{try{return window.__pr_cam.scene.ui.getMessageHandler?.().message?.text||''}catch(e){return ''}})()") or "")
                                if ("PP" in txt and ("no" in txt.lower() or "left" in txt.lower())) or any(k in txt.lower() for k in ("can\u2019t use", "can't use", "cannot use", "prevented from")):  # HEALBLOCK 11/3: Heal Block/Imprison/Disable/etc. block (w114 Bronzong Bitter Blade loop)
                                    stuck = True; break
                                if s2.get("h") != "FightUiHandler": break
                            else:
                                stuck = s2.get("h") == "FightUiHandler"
                            if not stuck: break
                            dead_moves.setdefault(dk, set()).update(tried)
                            log(f"NOPP stuck on {sorted(tried)} (msg={txt[:40]!r}) -> mark 0 PP, retry")
                            for _k in range(3): await Z(); await asyncio.sleep(0.2)  # clear message box
                            s2 = await ev(STATE_JS) or {}
                            if s2.get("h") != "FightUiHandler":
                                if s2.get("h") == "CommandUiHandler":
                                    if s2.get("cur") != 0: await set_cursor(0)
                                    await Z(); await asyncio.sleep(0.4); s2 = await ev(STATE_JS) or {}
                                if s2.get("h") != "FightUiHandler": break
                            m2 = pick_move(s2, hist, dead_moves[dk])
                            if m2 is None:
                                left = [mm for mm in (s2.get("moves") or []) if mm["n"] not in dead_moves[dk]]
                                if not left: log("NOPP no slots left - back"); await X(); break
                                m2 = left[0]
                            tried.add(m2["n"]); log(f"NOPP fallback -> {m2['n']} (slot {m2['i']})")
                            await set_cursor(m2["i"]); await asyncio.sleep(0.1); await Z()
                        if w not in shot_w: shot_w.add(w); await shot(SHOT_DIR, f"w{w}_{m['n'].replace(' ','')}")
                elif h == "TargetSelectUiHandler":
                    if TGT_PREF[0]:
                        _tr = await ev(TGT_JS + "(" + json.dumps(TGT_PREF[0]) + ")")
                        log(f"TARGET pick {TGT_PREF[0]} -> {_tr}"); await asyncio.sleep(0.15)
                    await Z()
                elif h == "BallUiHandler":
                    balls = st.get("balls") or {}
                    best = max([int(k) for k, v in balls.items() if v and int(k) <= 3] or [0])  # never Master Ball (4): reserved for Eternatus
                    await set_cursor(best); await Z()
                elif h == "ModifierSelectUiHandler":
                    if PARTY_ORDER_FIX and reorder_w.get("w") != w:
                        reorder_w["w"] = w
                        try:
                            ro = await ev(REORDER_JS)
                            if ro and ro.get("moved"): log(f"PARTY ORDER w{w}: {ro.get('before')} -> {ro.get('after')}")
                        except Exception as e: log(f"PARTY ORDER err {e}")
                    if shop_pend[0]:
                        sp_ = shop_pend[0]; shop_pend[0] = None; shop_tgt[0] = None
                        m2 = await ev("window.__pr_cam.scene.money")
                        if isinstance(m2, (int, float)) and m2 < sp_["money"]:
                            log(f"SHOP BUY (proactive) {sp_['n']} -> {sp_['mon']} cost={sp_['cost']} money={sp_['money']}->{m2} cap={sp_['cap']} ({sp_['why']})")
                        else:
                            shop_fail[w] = shop_fail.get(w, 0) + 1; _fk = (w, sp_["mon"]); shop_monfail[_fk] = shop_monfail.get(_fk, 0) + 1
                            if shop_monfail[_fk] >= 2: shop_skip.setdefault(w, set()).add(sp_["mon"])
                            log(f"SHOP buy {sp_['n']} -> {sp_['mon']} not charged (money {m2}) - fail #{shop_fail[w]}")
                    if shop_fail.get(w, 0) < 4 and shop_n.get(w, 0) < 8:
                        sh = await ev(SHOP_JS) or {}
                        if sh.get("items") is not None and isinstance(sh.get("money"), (int, float)):
                            if w not in shop_open: shop_open[w] = sh["money"]
                            m0 = shop_open[w]; spent = m0 - sh["money"]
                            floor = max(SHOP_RESERVE_FRAC * m0, SHOP_MIN_RESERVE)
                            if hard_w.get("w") != w:
                                nx = (w or 0) + 1; hj = await ev(HARD_JS + f"({nx})") or {}
                                rs = [x for x, c in (("HARD_WAVES", nx in HARD_WAVES), ("fixed", hj.get("fixed")), ("trainer", hj.get("trainer")), ("x10 gym/boss", nx % 10 == 0)) if c]
                                hard_w.update(w=w, hard=bool(rs))
                                if rs: log(f"HARD WAVE NEXT {nx} ({', '.join(rs)}) -> pre-heal")
                            _hd = hard_w.get("hard")
                            cap = int(max(0, min((SHOP_HARD_SPEND_FRAC if _hd else SHOP_MAX_SPEND_FRAC) * m0 - spent, sh["money"] - floor)))
                            try: PRIM_ORB[0] = bool(await ev(PRIM_ORB_JS))
                            except Exception: PRIM_ORB[0] = False
                            pl = shop_plan(party, z, role(party, SECONDARY), sh["items"], sh["money"], cap, SHOP_HARD_HURT if _hd else None, shop_skip.get(w, ()))
                            if pl and pl[2] == "revive":
                                _lh = await ev("(()=>{try{return window.__pr_cam.scene.getPlayerParty().map(p=>({n:p.name,hp:p.hp}))}catch(e){return null}})()") or []
                                _dj = next((j for j, q in enumerate(_lh) if q.get("n") == pl[1]["n"] and (q.get("hp") or 0) <= 0), None)
                                if _dj is None:
                                    log(f"SHOP revive skipped: {pl[1]['n']} not fainted live"); pl = None
                                else: pl[1]["i"] = _dj
                            if pl:
                                it, pm, why_ = pl; shop_n[w] = shop_n.get(w, 0) + 1
                                shop_pend[0] = {"n": it["n"], "mon": pm["n"], "cost": it["cost"], "money": sh["money"], "cap": cap, "why": why_}
                                shop_tgt[0] = pm["i"]; last_pick[0] = it["n"]
                                chk = None
                                for _try in range(20):  # SHOPWAIT 10/31: 20x0.4s (notready persisted >3s) | SHOPSEL 10/30: locate by NAME in live rows each try (r/c from SHOP_JS can go stale)
                                    chk = await ev(SHOP_SEL_JS % json.dumps(it["n"]))
                                    if chk == it["n"]: break
                                    if chk == "notready":  # SHOPSTEP 10/31: tab hidden -> game loop only advances via STEP_JS; step it so intro anims finish
                                        for _k in range(5): await ev(STEP_JS); await asyncio.sleep(0.05)
                                    await asyncio.sleep(0.4)  # 'notready' = intro anims still running (game resets cursor to shopCursorTarget when they finish)
                                if chk != it["n"]:
                                    log(f"SHOP cursor mismatch {chk} != {it['n']} after 20 tries - skip shop this wave"); shop_pend[0] = None; shop_tgt[0] = None; shop_fail[w] = 9
                                else:
                                    _pi = await ev("(()=>{try{return !!window.__pr_cam.scene.ui.getHandler().processInput(5)}catch(e){return false}})()")  # SHOPJS 10/30: key Z often dropped -> direct ACTION
                                    if not _pi: await Z()
                                    for _k in range(6): await asyncio.sleep(0.2); await ev(STEP_JS)
                                    continue
                    if xfer_done.get("w") != w:
                        xfer_done["w"] = w  # one attempt per wave, never loops
                        try:
                            xr = await ev(XFER_JS)
                            if xr and (xr.get("x1") or xr.get("moved") or xr.get("failed")): log(f"TRANSFER w{w}: {xr}")
                            for _po in (xr or {}).get("porb") or []: log(f"ORBFIX w{w}: {_po}")
                        except Exception as e:
                            log(f"TRANSFER w{w} error {e}")
                    st["zmoves"] = st.get("moves") if st.get("user") == z["n"] else None
                    if st.get("zmoves") is None:
                        st["zmoves"] = (await ev(STATE_JS.replace("(o.fi??0)", "0").replace("[fi]||party[0]", "[0]&&false||party[" + str(int(z.get("i") or 0)) + "]"))).get("moves")  # PPIDX 11/02: read the PRIMARY's PP (party[0] was Milotic -> pp_low missed Lugia at 0-2 PP)
                    if pk_w.get("w") != w: pk_w["w"] = w; pk_w["v"] = bool(await ev(PICKUP_JS))
                    try: st["lure_left"] = int(await ev(LURE_JS) or 0)
                    except Exception: st["lure_left"] = 0
                    if any("lure" in str(r_.get("n", "")).lower() for r_ in (st.get("rew") or [])) and lure_log.get(w) is None:
                        lure_log[w] = 1; log(f"LURE active ({st['lure_left']} left) -> skip" if st["lure_left"] > 0 else "LURE none active -> rank -50 (doubles = secondary on field)")
                    i, why = pick_reward(st, rew_bad.get(w, set()))
                    br = getattr(pick_reward, "last_rank", 0) if i is not None else 999
                    ppc = i is not None and br <= -10 and any(k in str((st.get("rew") or [{}]*(i+1))[i].get("n", "")).lower() for k in PP_ITEMS)
                    hv = br <= -35 or ppc
                    want = br <= -30 or ppc
                    no_hi = not any((r_.get("t") or 0) >= 3 for r_ in (st.get("rew") or []))
                    junk = i is not None and br >= 93  # best option is a battle item / active-lure / balls / TM or worse
                    if i is not None and reroll_n.get(w, 0) < REROLL_MAX and ((not hv and cheap_n.get(w, 0) < REROLL_CHEAP_MAX) or (no_hi and not want) or junk):
                        ri = await ev("(()=>{const s=window.__pr_cam.scene;const h=s.ui.getHandler();const ph=s.phaseManager.getCurrentPhase();let c=h.rerollCost;try{if(c===undefined||c<0)c=ph.getRerollCost(!!s.lockModifierTiers)}catch(e){};return {money:s.money,cost:c}})()") or {}
                        money, cost = ri.get("money"), ri.get("cost")
                        if isinstance(money, (int, float)) and isinstance(cost, (int, float)) and cost >= 0:
                            _m0 = shop_open.setdefault(w, money)
                            _floor = max(SHOP_RESERVE_FRAC * _m0, SHOP_MIN_RESERVE)
                            _ok = cost <= money and money - cost >= _floor
                            _cap = 0.5 * _m0 - (_m0 - money)  # reroll screen cap kept at 50% (shop heal cap now 25%)
                            tag = None
                            _bud = REROLL_CHEAP_FRAC * _m0; _sp = rr_spent.get(w, 0)
                            if _sp + cost > _bud:
                                log(f"REROLL budget stop spent={_sp} next={cost} budget={int(_bud)}"); _ok = False
                            if _ok and not hv and cheap_n.get(w, 0) < REROLL_CHEAP_MAX and cost < REROLL_CHEAP_FRAC * money:
                                cheap_n[w] = cheap_n.get(w, 0) + 1; tag = f"REROLL cheap cost={cost} money={money} ({cost/max(1,money):.0%})"
                            elif _ok and junk:
                                tag = f"REROLL junk(best rank {br}) cost={cost} money={money}"
                            elif _ok and no_hi and not want:
                                tag = f"REROLL nothing>ultra cost={cost} money={money} cap={int(_cap)}"
                            if tag:
                                _n = reroll_n.get(w, 0); _p = REROLL_DECAY ** _n
                                if random.random() >= _p:
                                    log(f"REROLL decay skip n={_n} p={_p:.2f}"); tag = None
                            if tag:
                                reroll_n[w] = reroll_n.get(w, 0) + 1; rr_spent[w] = _sp + cost
                                log(f"{tag} #{reroll_n[w]} w{w} best was rank {br}: {why[:160]}")
                                await ev("(()=>{const h=window.__pr_cam.scene.ui.getHandler();h.setRowCursor(0);h.setCursor(0);})()")
                                await asyncio.sleep(0.25); await Z(); await asyncio.sleep(1.0)
                                for _ in range(4): await ev(STEP_JS)
                                last_rew_wave = None; rew_bad.pop(w, None); continue
                            if reroll_log.get(w) != (money, cost):
                                reroll_log[w] = (money, cost); log(f"no reroll w{w}: cost {cost} / money {money} floor {int(_floor)} cap {int(_cap)} hv={hv} want={want} no_hi={no_hi}")
                            cheap_n[w] = REROLL_CHEAP_MAX; reroll_n[w] = REROLL_MAX  # don't re-query this screen
                    last_pick[0] = (st.get("rew") or [{}]*(i+1))[i].get("n") if i is not None else None
                    if i is None:
                        # no reward cards left (only shop) -> leave the screen; confirm the skip prompt with Yes
                        log("reward screen with no reward options - X + confirm skip"); skip_yes[0] = True
                        await X()
                    else:
                        if last_rew_wave != w: log(f"REWARD pick {why}"); last_rew_wave = w
                        await ev(f"(()=>{{const h=window.__pr_cam.scene.ui.getHandler();h.setRowCursor(1);h.setCursor({i});}})()")
                        await asyncio.sleep(0.25)
                        cur = await ev("window.__pr_cam.scene.ui.getHandler().cursor")
                        if cur != i:
                            log(f"reward cursor {cur} != {i} - re-set"); await ev(f"window.__pr_cam.scene.ui.getHandler().setCursor({i})"); await asyncio.sleep(0.25); continue
                        if any(k in (last_pick[0] or "").lower() for k in ("soothe bell", "rare candy")): candy_n[0] += 1
                        await Z()
                elif h == "PartyUiHandler" and st.get("ph") == "SelectModifierPhase" and "dna splicers" in (last_pick[0] or "").lower():
                    async def dna_bail(why):
                        log(f"DNA bail w{w}: {why} -> cancel back to rewards, DNA junk this wave")
                        rew_bad.setdefault(w, set()).add(last_pick[0]); globals().setdefault("_dna_try", {})[w] = 99
                        for _ in range(4):
                            hn = await ev("window.__pr_cam.scene.ui.getHandler().constructor.name")
                            if hn != "PartyUiHandler": break
                            await X(); await asyncio.sleep(0.4); await ev(STEP_JS); await pump(2)
                        log(f"DNA bail done, handler={await ev('window.__pr_cam.scene.ui.getHandler().constructor.name')}")
                        last_pick[0] = None; last_rew_wave_reset[0] = True
                    DT = globals().setdefault("_dna_try", {}); DT[w] = DT.get(w, 0) + 1
                    last_rew_wave_reset = [False]
                    if DT[w] > 1:
                        await dna_bail(f"re-entered party UI (try {DT[w]})"); last_rew_wave = None; continue
                    LIVE = "(()=>{const s=window.__pr_cam.scene,h=s.ui.getHandler();return {mode:h.partyUiMode,tm:!!h.transferMode,tc:h.transferCursor,cur:h.cursor,om:!!h.optionsMode,party:s.getPlayerParty().map((p,i)=>({i,n:p.name,sp:p.species.speciesId,fs:p.fusionSpecies?p.fusionSpecies.speciesId:null,id:p.id}))}})()"
                    async def dna_opt(want):
                        await asyncio.sleep(0.5); await ev(STEP_JS); await pump(2)
                        lv = await ev(LIVE) or {}
                        labels = await ev(OPT_LABELS_JS); labels = [re.sub(r"\[/?[a-z]+[^\]]*\]", "", str(x)).strip() for x in (labels if isinstance(labels, list) else [])]
                        log(f"DNA options om={lv.get('om')} tm={lv.get('tm')} tc={lv.get('tc')} labels={labels} want={want}")
                        low = [x.lower() for x in labels]
                        if not lv.get("om") or want not in low: return None
                        k = low.index(want)
                        c = await ev(f"(()=>{{const h=window.__pr_cam.scene.ui.getHandler();h.setCursor({k});return h.optionsMode?h.optionsCursor:h.cursor}})()"); log(f"DNA option cursor -> {k} ({labels[k]}) got {c}")
                        if c != k: return None
                        await Z(); return lv
                    lv = await ev(LIVE) or {}
                    lp = lv.get("party") or []
                    log(f"DNA flow w{w} start mode={lv.get('mode')} tm={lv.get('tm')} om={lv.get('om')} party={[(p['i'], p['n'], p['fs']) for p in lp]}")
                    bi = next((p["i"] for p in lp if p["sp"] in DNA_BASE and not p["fs"]), None)
                    qi = next((p["i"] for p in lp if p["sp"] in DNA_PARTNER and not p["fs"] and p["i"] != bi), None)
                    if bi is None or qi is None:
                        await dna_bail("no unfused Kricketot + Zigzagoon/Linoone pair"); last_rew_wave = None; continue
                    if bi < 2 or qi < 2 or any(lp[j]["sp"] in (PRIMARY[1] | {349, 350}) for j in (bi, qi)):
                        await dna_bail(f"pair touches protected slot base={bi} partner={qi}"); last_rew_wave = None; continue
                    if lv.get("om") or lv.get("tm"):
                        await dna_bail("unexpected options/transfer already open"); last_rew_wave = None; continue
                    bid = lp[bi]["id"]
                    log(f"DNA step1 BASE {lp[bi]['n']} slot {bi} -> Z"); c = await set_cursor(bi)
                    if c != bi: await dna_bail(f"cursor {c} != base {bi}"); last_rew_wave = None; continue
                    await Z()
                    if not await dna_opt("apply"): await dna_bail("no Apply option on base"); last_rew_wave = None; continue
                    await asyncio.sleep(0.5); await ev(STEP_JS); await pump(2); lv = await ev(LIVE) or {}
                    log(f"DNA step2 transfer tm={lv.get('tm')} tc={lv.get('tc')} (want tc={bi})")
                    if not lv.get("tm") or lv.get("tc") != bi: await dna_bail("transfer mode not started on base"); last_rew_wave = None; continue
                    log(f"DNA step3 PARTNER {lp[qi]['n']} slot {qi} -> Z"); c = await set_cursor(qi)
                    if c != qi: await dna_bail(f"cursor {c} != partner {qi}"); last_rew_wave = None; continue
                    await Z()
                    if not await dna_opt("splice"): await dna_bail("no Splice option on partner"); last_rew_wave = None; continue
                    ok = {}
                    for _t in range(12):
                        await asyncio.sleep(0.5); await ev(STEP_JS); await pump(2)
                        ok = await ev(f"(()=>{{const s=window.__pr_cam.scene;const p=s.getPlayerParty().find(x=>x.id==={bid});return {{h:s.ui.getHandler().constructor.name,fused:!!(p&&p.fusionSpecies),n:p&&p.name,ab:p&&p.getAbility().name,pa:p&&p.getPassiveAbility().name,party:s.getPlayerParty().map(x=>x.name)}}}})()") or {}
                        if ok.get("fused"): break
                    log(f"DNA result {ok}")
                    if ok.get("fused"):
                        log(f"DNA FUSED {ok.get('n')} ability={ok.get('ab')} passive={ok.get('pa')} party={ok.get('party')}"); last_pick[0] = None; DT[w] = 99
                    else:
                        await dna_bail("no fusion after Splice"); last_rew_wave = None
                    continue
                elif h == "PartyUiHandler":
                    ph = st.get("ph")
                    party_tries += 1
                    if party_tries > 6:
                        if ph == "SelectModifierPhase" and last_pick[0]:
                            fbi = next((j for j, p in enumerate(party) if p is role(party, SECONDARY)), None)
                            if fbi is not None and "rare candy" in last_pick[0].lower() and w not in fb_fall:
                                fb_fall.add(w); party_tries = 0; log(f"CANDY_TARGET {last_pick[0]} failed/max on {party[fbi]['n']} (party UI looped {party_tries}x) -> other role mon"); continue
                            _sb = role(party, SECONDARY)
                            if "leppa" not in last_pick[0].lower() or w in lep_try: rew_bad.setdefault(w, set()).add(last_pick[0])
                            else: lep_try.add(w); party_tries = 0; log("leppa: retry applying to Zacian"); await set_cursor(party.index(z)); await Z(); continue
                            log(f"reward {last_pick[0]} cannot be applied - blacklist for wave {w}, back to rewards")
                            last_rew_wave = None
                        else:
                            log(f"party UI loop in {ph} - X out")
                        for _ in range(3):
                            await X(); await asyncio.sleep(0.25); await ev(STEP_JS)
                        party_tries = 0
                        continue
                    if ph in ("SwitchPhase", "SwitchSummonPhase"):
                        tgt = z["i"] if (z["hp"] > 0 and not z["f"]) else next((p["i"] for p in party if p["hp"] > 0 and not p["f"] and p is not z), None)
                        if tgt is None: tgt = next((p["i"] for p in party if p["hp"] > 0 and not p["f"]), None)
                        party_tries = 0 if party_tries < 3 else party_tries
                        log(f"switch-in {ph}: send slot {tgt}")
                        want_opt = 0  # SEND_OUT
                    elif ph == "CommandPhase" and sf["pend"] == w and role(party, SECONDARY) and not role(party, SECONDARY)["f"] and role(party, SECONDARY)["hp"] > 0:
                        tgt = role(party, SECONDARY)["i"]; want_opt = 0
                        if party_tries == 1: log(f"SECFIELD party: Feebas slot {tgt}")
                        if party_tries >= 4: sf["pend"] = None; sf["done"].add(w); log(f"SECFIELD w{w}: switch stuck -> give up this wave"); await X(); await asyncio.sleep(0.3); continue
                    elif ph == "CommandPhase":
                        if z["hp"] > 0 and not z["f"]:
                            tgt = z["i"]; want_opt = 0; log(f"switch-in CommandPhase party: Zacian slot {tgt}")
                            if sf["out"] == w and party_tries == 1: log(f"SECFIELD w{w}: Zacian back")
                        else:
                            log("party UI in CommandPhase, Zacian not switchable - back"); await X(); await asyncio.sleep(0.3); continue
                    elif ph == "SelectModifierPhase":
                        dead = next((p["i"] for p in party if p["hp"] <= 0), None)
                        tgt = party.index(z)
                        _sec = role(party, SECONDARY)
                        if z and any(k.lower() in (last_pick[0] or "").lower() for k in PROF()["signature_items"]):
                            tgt = party.index(z)
                            if same == 0: log(f"SIGNATURE {last_pick[0]} -> {z['n']} slot {tgt}")
                        if _sec and "prism scale" in (last_pick[0] or "").lower():
                            tgt = party.index(_sec)
                            if same == 0: log(f"PRISM SCALE -> {_sec['n']} slot {tgt}")
                        if _sec and "eviolite" in (last_pick[0] or "").lower():
                            tgt = party.index(_sec)
                            if same == 0: log(f"EVIOLITE -> {_sec['n']} slot {tgt}")
                        if _sec and _sec["hp"] <= 0: dead = party.index(_sec)
                        if z and z["hp"] <= 0: dead = party.index(z)  # primary first
                        _lp = (last_pick[0] or "").lower()
                        if _sec and _sec["hp"] > 0 and _sec.get("mx") and any(k in _lp for k in ("potion", "full restore", "full heal")) and not ("revive" in _lp) and not (SEC_NO_STATUS_CURE and _sec.get("sp") in (349, 350, 602, 603, 604) and any(k in _lp for k in SEC_CURE_ITEMS)):
                            _zr = z["hp"] / z["mx"] if z.get("mx") else 1; _sr = _sec["hp"] / _sec["mx"]
                            if _sr < 0.75 and not (_zr < 0.75 and _zr <= _sr): tgt = party.index(_sec); log(f"ROLE HEAL target secondary {_sec['n']} {_sr:.0%}")
                        if last_pick[0] and "revive" in last_pick[0].lower() and dead is not None:
                            tgt = dead
                        fbi = next((j for j, p in enumerate(party) if p is role(party, SECONDARY)), None)
                        lpn = (last_pick[0] or "").lower()
                        if "berry" in lpn and "leppa" not in lpn:
                            tgt = party.index(z)  # BERRY (Gavin 20:28): held berries -> PRIMARY by default; fallback to secondary on fail
                            if same == 0: log(f"BERRY {last_pick[0]} -> PRIMARY {z['n']} slot {tgt}")
                        if orb_banned({"n": lpn}) and fbi is not None:
                            tgt = fbi
                            if same == 0: log(f"ORB {last_pick[0]} -> secondary slot {tgt} (never primary/helpers)")
                        if "soothe bell" in lpn and SEC_ALLOW_SOOTHE and fbi is not None:
                            _sb = await ev("(()=>{try{const s=window.__pr_cam.scene,p=s.getPlayerParty()[%d];const m=s.modifiers.find(m=>m.type&&m.type.id==='SOOTHE_BELL'&&m.pokemonId===p.id);let mx=3;try{mx=m?m.getMaxStackCount():(p.getHeldItemMaxStack?3:3)}catch(e){};return {n:m?m.stackCount:0,mx}}catch(e){return {n:0,mx:3,err:String(e)}}})()" % fbi) or {}
                            _sbn, _sbm = int(_sb.get("n") or 0), int(_sb.get("mx") or 3)
                            if _sbn < _sbm: tgt = fbi; _m = f"SOOTHE -> secondary {party[fbi]['n']} ({_sbn}/{_sbm})"
                            else: tgt = party.index(z); _m = f"SOOTHE -> Zacian (secondary full {_sbn}/{_sbm})"
                            if same == 0: log(_m)
                        if lpn in EVO_TGT:
                            _ei = next((j for j, p in enumerate(party) if p.get("sp") == EVO_TGT[lpn] and p is not z and (p is not role(party, SECONDARY) or (p.get("sp") == 603 and "thunder stone" in lpn) or (p.get("sp") == 64 and ("link cord" in lpn or "linking cord" in lpn)))), None)
                            if _ei is not None:
                                tgt = _ei
                                if same == 0: log(f"EVO ITEM {last_pick[0]} -> slot {tgt} ({party[tgt]['n']}), never Lugia/Milotic")
                        if "mewtwonite" in lpn:  # t209u: Mewtwonite X/Y -> Mewtwo (150) only
                            _mwi = next((j for j, p in enumerate(party) if p.get("sp") == 150), None)
                            if _mwi is not None:
                                tgt = _mwi
                                if same == 0: log(f"MEWTWONITE -> Mewtwo slot {tgt}")
                        if any(k in lpn for k in ("n-solarizer", "n-lunarizer", "ultranecrozium", "n solarizer", "n lunarizer")):  # NECRO t233u: -> Necrozma (800) only
                            _nzi = next((j for j, p in enumerate(party) if p.get("sp") == 800), None)
                            if _nzi is not None:
                                tgt = _nzi
                                if same == 0: log(f"NECROZMA FORM {last_pick[0]} -> Necrozma slot {tgt}")
                        if "alakazamite" in lpn:  # ALAKA t226u: Alakazamite -> Alakazam (65) only
                            _aki = next((j for j, p in enumerate(party) if p.get("sp") == 65), None)
                            if _aki is not None:
                                tgt = _aki
                                if same == 0: log(f"ALAKAZAMITE -> Alakazam slot {tgt}")
                        if "absolite" in lpn:  # MEWABSOL t207u: Absolite -> Absol (359) only
                            _abi = next((j for j, p in enumerate(party) if p.get("sp") == 359), None)
                            if _abi is not None:
                                tgt = _abi
                                if same == 0: log(f"ABSOLITE -> Absol slot {tgt}")
                        if "eelektrossite" in lpn:  # MEGA t199u: Eelektrossite -> Eelektross (604) only
                            _swi = next((j for j, p in enumerate(party) if p.get("sp") == 604), None)
                            if _swi is not None:
                                tgt = _swi
                                if same == 0: log(f"EELEKTROSSITE -> Eelektross slot {tgt}")
                        if "rare candy" in lpn:
                            cfg_reload(); _ct = CFG["candy_target"]; _zi = party.index(z)  # t168u live config read  # Soothe Bell always secondary-first
                            if _ct == "primary" or fbi is None: _pri = _zi; _alt = fbi
                            elif _ct == "both": _pri, _alt = ((fbi, _zi) if candy_n[0] % 2 == 0 else (_zi, fbi))
                            else: _pri, _alt = fbi, _zi
                            if w in fb_fall and _alt is not None: _pri = _alt
                            tgt = _pri
                            if same == 0: log(f"CANDY_TARGET {_ct}: {last_pick[0]} -> slot {tgt} ({party[tgt]['n']})")
                        want_opt = None
                    elif ph == "MysteryEncounterPhase":
                        # ME option asks for a party member: offer a non-Zacian ally (never risk Zacian)
                        tgt = z["i"] if z else 0
                        if "parttimer" in str(globals().get("_last_mekey", "")):  # EARLYWIPE 10/31: Part-Timer drains the chosen mon's PP (w42 drained Lugia) -> send a bench ally
                            _s4 = role(party, SECONDARY); _bn = [i for i, p in enumerate(party) if p is not z and p is not _s4 and (p.get("hp") or 0) > 0]
                            if _bn: tgt = _bn[0]; log(f"ME partTimer -> bench slot {tgt} ({party[tgt].get('n')}) not primary")
                        want_opt = None
                        if same == 0: log(f"ME party select -> slot {tgt} (Zacian/slot1)")
                    else:
                        log(f"stray party UI in {ph} - back"); await X(); await asyncio.sleep(0.3); continue
                    if ph == "SelectModifierPhase" and shop_tgt[0] is not None and not any(k in (last_pick[0] or "").lower() for k in ("rare candy", "soothe bell", "eelektrossite", "absolite", "mewtwonite", "alakazamite", "link cord", "linking cord", "n-solarizer", "n-lunarizer", "ultranecrozium")):
                        tgt = shop_tgt[0]
                        if same == 0: log(f"SHOP target slot {tgt} for {last_pick[0]}")
                    if ph == "SelectModifierPhase":
                        _lp2 = (last_pick[0] or "").lower(); _s3 = role(party, SECONDARY)
                        if _s3 and tgt == party.index(_s3) and z:
                            _ok3 = ("rare candy" in _lp2 or "candy jar" in _lp2) or (SEC_ALLOW_SOOTHE and "soothe bell" in _lp2) or (SEC_ALLOW_PRISM and "prism scale" in _lp2) or (SEC_ALLOW_REVIVE and _s3["hp"] <= 0 and any(k in _lp2 for k in ("revive", "sacred ash"))) or (SEC_ALLOW_HEAL and _s3["hp"] > 0 and any(k in _lp2 for k in ("potion", "full restore", "full heal")) and not (SEC_NO_STATUS_CURE and _s3.get("sp") in (349, 350, 602, 603, 604) and any(k in _lp2 for k in SEC_CURE_ITEMS))) or orb_banned({"n": _lp2}) or ("swampertite" in _lp2 and _s3.get("sp") == 260) or ("thunder stone" in _lp2 and _s3.get("sp") == 603) or ("eelektrossite" in _lp2 and _s3.get("sp") == 604) or (("link cord" in _lp2 or "linking cord" in _lp2) and _s3.get("sp") == 64) or ("alakazamite" in _lp2 and _s3.get("sp") == 65)  # TSTONE 11/04: evo stone/mega stone may go to Tynamo-line secondary
                            if not _ok3:
                                tgt = party.index(z)
                                if SEC_NO_STATUS_CURE and _s3.get("sp") in (349, 350, 602, 603, 604) and any(k in _lp2 for k in SEC_CURE_ITEMS) and same == 0: log(f"SEC STATUS skip: {last_pick[0]} not used on Milotic (burn/poison kept)")
                                if same == 0: log(f"SECONDARY ONLY-CANDY: {last_pick[0]} -> Zacian slot {tgt} (not secondary)")
                    if ph == "SelectModifierPhase" and tgt is not None:
                        # REVIVEFIX 10/30: re-read live HP by index (party may have been reordered after st was read)
                        _hp = await ev("(()=>{try{return window.__pr_cam.scene.getPlayerParty().map(p=>({n:p.name,hp:p.hp,sp:p.species.speciesId}))}catch(e){return null}})()") or []
                        _lpx = (last_pick[0] or "").lower(); _isrev = any(k in _lpx for k in ("revive", "sacred ash")) and "reviver seed" not in _lpx  # REVIVERSEED 10/31: held item, not a revive
                        if _hp:
                            _dead = [j for j, q in enumerate(_hp) if (q.get("hp") or 0) <= 0]
                            _zj = next((j for j, q in enumerate(_hp) if z and q.get("n") == z["n"]), None)
                            if _isrev:
                                _nt = _zj if _zj in _dead else (_dead[0] if _dead else None)
                                if _nt != tgt and same == 0: log(f"REVIVE target live: {last_pick[0]} -> slot {_nt} ({_hp[_nt]['n'] if _nt is not None else 'none fainted'})")
                                tgt = _nt
                                if _nt is None and last_pick[0]:  # REVIVENONE 10/31 18:45: revive picked but nobody fainted -> blacklist for wave + re-pick (was looping on X)
                                    rew_bad.setdefault(w, set()).add(last_pick[0]); last_rew_wave = None; log(f"REVIVE NONE: blacklist {last_pick[0]} for wave {w}, re-pick")
                            elif tgt < len(_hp) and (_hp[tgt].get("hp") or 0) <= 0:
                                _alive = [j for j, q in enumerate(_hp) if (q.get("hp") or 0) > 0]
                                _sj = next((j for j in _alive if _hp[j].get("sp") in SECONDARY[1]), None)
                                _nt = _sj if _sj is not None else (_alive[0] if _alive else None)
                                if same == 0: log(f"FAINTED TARGET block: {last_pick[0]} not given to fainted {_hp[tgt]['n']} -> slot {_nt}")
                                tgt = _nt
                    if tgt is None: await X(); continue
                    if not st.get("om"):
                        await set_cursor(tgt); await Z()
                    else:
                        opts = st.get("opts") or []
                        if ph == "SelectModifierPhase":
                            labels = await ev(OPT_LABELS_JS)
                            labels = [re.sub(r"\s*\d+/\d+\s*$", "", re.sub(r"\[/?[a-z]+[^\]]*\]", "", str(lb))) for lb in (labels if isinstance(labels, list) else [])]  # strip [shadow] tags + PP suffix
                            zm = (await ev(STATE_JS.replace("(o.fi??0)", "0").replace("[fi]||party[0]", "[0]&&false||party[" + str(party.index(z)) + "]"))).get("moves") or []
                            if last_pick[0] in tm_ok and tgt == party.index(z) and any(lb.strip().lower() == "teach" for lb in labels):
                                k = next(k2 for k2, lb in enumerate(labels) if lb.strip().lower() == "teach")
                                if same == 0: log(f"PROFILE TM {last_pick[0]} -> Teach {z['n']} (forget slot {tm_ok[last_pick[0]]})")
                                await set_cursor(k); await Z(); continue
                            if any(lb.strip().lower() == "teach" for lb in labels) or "memory mushroom" in (last_pick[0] or "").lower():  # MUSHROOM (watch 22:27): relearn list loops too
                                # TM: Zacian never learns (LearnMove prompt is declined) -> loops. Blacklist and leave.
                                if last_pick[0]: rew_bad.setdefault(w, set()).add(last_pick[0])
                                for r0 in (st.get("rew") or []):
                                    if str(r0.get("n","")).lower().startswith("tm"): rew_bad.setdefault(w, set()).add(r0["n"])
                                log(f"TM teach menu for {last_pick[0]} - skip, blacklist for wave {w}"); last_rew_wave = None
                                for _ in range(3):
                                    await X(); await asyncio.sleep(0.25); await ev(STEP_JS)
                                continue
                            names = [m["n"].lower() for m in zm]
                            hit = [(k2, names.index(lb.strip().lower())) for k2, lb in enumerate(labels) if lb.strip().lower() in names]
                            if hit:  # PP item move menu: pick Zacian's lowest-PP-left move (by ratio)
                                k2, mi = min(hit, key=lambda km: zm[km[1]]["left"] / max(1, zm[km[1]]["max"]))
                                _tgp = set(PROF().get("target_moveset") or [])  # TGTMOVES: PP Up/Max -> lowest-max-PP target move
                                if _tgp and any(x in (last_pick[0] or "").lower() for x in ("pp up", "pp max")):
                                    _th = [km for km in hit if zm[km[1]]["n"] in _tgp]
                                    if _th: k2, mi = min(_th, key=lambda km: zm[km[1]]["max"])
                                k = k2 if k2 < len(opts) else mi
                                log(f"PP item -> {zm[mi]['n']} {zm[mi]['left']}/{zm[mi]['max']} (labels={labels})")
                            else:
                                ap = next((k2 for k2, lb in enumerate(labels) if lb.strip().lower() in ("apply", "use")), None)
                                k = ap if ap is not None else (0 if opts and opts[0] != -1 else None)
                                if same == 0: log(f"party opts={opts} labels={labels} -> {k}")
                        elif want_opt is None:
                            k = 0 if opts and opts[0] != -1 else None
                        else:
                            k = opts.index(want_opt) if want_opt in opts else None
                        if k is None: await X()
                        else:
                            await set_cursor(k); await Z()
                            log(f"party {ph}: slot {tgt} option {opts[k] if k < len(opts) else k}")
                elif h == "ConfirmUiHandler":
                    if st.get("ph") in ("MysteryEncounterPhase", "MysteryEncounterOptionSelectedPhase", "PostMysteryEncounterPhase", "MysteryEncounterBattlePhase"):
                        cmsg = str(await ev("(()=>{try{return window.__pr_cam.scene.ui.getMessageHandler().message.text||''}catch(e){return ''}})()") or "").lower()
                        if any(t in cmsg for t in ("teach", "ability", "surge", "learn")):
                            log(f"ME confirm teach/ability prompt -> No ({cmsg[:60]!r})"); await set_cursor(1); await Z()
                        else:
                            await set_cursor(0); await Z()  # ME follow-up prompt: first option
                    elif st.get("ph") == "LearnMovePhase" and (_li := await ev(LEARN_JS)) and not _li.get("err") and _li.get("sp") in PRIMARY[1]:
                        _ix = learn_decide(PROF(), _li["cur"], _li["new"])
                        if _ix is not None and _li.get("canLearn"):
                            r_ = await ev(LEARN_DO_JS % (_ix, _ix, _ix))
                            log(f"LEARN {_li['pn']}: {_li['new']['n']} replaces slot {_ix} ({_li['cur'][_ix]['n'] if _ix < len(_li['cur']) else '-'}) -> {r_} cur={[m['n'] for m in _li['cur']]} {LEARN_NOTE[0]}")
                        else:
                            _cm = str(await ev("(()=>{try{return window.__pr_cam.scene.ui.getMessageHandler().message.text||''}catch(e){return ''}})()") or "").lower()
                            if "stop" in _cm: log(f"LEARN {_li['pn']}: stop teaching {_li['new']['n']} -> Yes"); await set_cursor(0); await Z()
                            else: log(f"LEARN {_li['pn']}: decline {_li['new']['n']} (profile) cur={[m['n'] for m in _li['cur']]} {LEARN_NOTE[0]}"); await X()
                    elif st.get("ph") == "LearnMovePhase" and (_li := await ev(LEARN_JS)) and not _li.get("err") and _li.get("sp") in SECONDARY[1]:  # Absol slot_replace via learn_decide (was replace_on_learn only)
                        _sp = sec_profile(); _cn = [m["n"] for m in _li["cur"]]
                        _ix = learn_decide(_sp, _li["cur"], _li["new"])
                        if _ix is None:
                            _rol = _sp.get("replace_on_learn") or {}
                            _ix = next((_cn.index(o) for o in _rol.get(_li["new"]["n"], []) if o in _cn), None)
                            if _ix is None and len(_cn) < 4 and _li["new"]["n"] in _rol: _ix = len(_cn)
                        if _ix is not None and _li.get("canLearn"):
                            r_ = await ev(LEARN_DO_JS % (_ix, _ix, _ix)); log(f"LEARN SECONDARY {_li['pn']}: {_li['new']['n']} replaces slot {_ix} ({_cn[_ix] if _ix < len(_cn) else '-'}) -> {r_} cur={_cn} {LEARN_NOTE[0]}")
                        else:
                            _cm = str(await ev("(()=>{try{return window.__pr_cam.scene.ui.getMessageHandler().message.text||''}catch(e){return ''}})()") or "").lower()
                            if "stop" in _cm: log(f"LEARN SECONDARY {_li['pn']}: stop teaching {_li['new']['n']} -> Yes"); await set_cursor(0); await Z()
                            else: log(f"LEARN SECONDARY {_li['pn']}: decline {_li['new']['n']} cur={_cn} {LEARN_NOTE[0]}"); await X()
                    elif skip_yes[0] and st.get("ph") == "SelectModifierPhase":
                        skip_yes[0] = False; await set_cursor(0); await Z()
                    elif st.get("ph") == "CheckSwitchPhase" and z["hp"] > 0 and not z["f"] and z["hp"] >= 0.5 * (z.get("mx") or 1):
                        log(f"CheckSwitch prompt w{w} -> Yes (send Zacian)"); await set_cursor(0); await Z()
                    else:
                        await X()  # answer No (e.g. switch prompt / learn move)
                elif h == "MysteryEncounterUiHandler":
                    n_opt = await ev("(()=>{const me=window.__pr_cam.scene.currentBattle.mysteryEncounter;if(!me)return 0;let k=me.options.length;while(k>1&&me.options[k-1].meetsRequirements&&!me.options[k-1].meetsRequirements())k--;return k})()") or 0
                    meinfo = await ev("""(()=>{const s=window.__pr_cam.scene,me=s.currentBattle.mysteryEncounter;const t=[];const walk=(o,d)=>{if(!o||d>8||o.visible===false)return;if(o.text!==undefined&&String(o.text).trim())t.push(String(o.text));(o.list||[]).forEach(c=>walk(c,d+1))};walk(s.ui,0);return {key:me&&me.localizationKey||'',type:me&&me.encounterType,txt:t.join(' | ')}})()""") or {}
                    mekey_s = str(meinfo.get("key", "")).lower(); metxt = str(meinfo.get("txt", "")).lower()
                    BLOCK_ME = ("weirddream", "weird_dream", "weird dream", "globaltradesystem", "darkdeal", "dark_deal", "dark deal", "wondertrade", "wonder_trade", "wonder trade", "trade")
                    XFORM_WORDS = ("trade", "in exchange for your", "give up a pok", "take one of your", "transform", "replace your", "change your pok", "changes your pok", "your team will", "swap your")
                    pick = 0
                    _mo = await ev("(()=>{try{const me=window.__pr_cam.scene.currentBattle.mysteryEncounter;return me.options.map(o=>!o.meetsRequirements||!!o.meetsRequirements())}catch(e){return []}})()") or []
                    _mk = mekey_s.replace("_", "").replace(" ", "")
                    globals()["_last_mekey"] = _mk
                    if "shadyvitamindealer" in _mk:
                        if len(_mo) >= 2 and _mo[1]: pick = 1; why = "ME shady dealer -> pricey"
                        else: pick = len(_mo) - 1 if _mo else max(0, n_opt - 1); why = "ME shady dealer -> leave (pricey unaffordable)"
                        if same == 0: log(why)
                    elif "trainingsession" in _mk:
                        pick = len(_mo) - 1 if _mo else max(0, n_opt - 1); why = "ME training session -> leave"
                        if same == 0: log(why)
                    elif any(b in mekey_s for b in BLOCK_ME) or any(b in metxt for b in BLOCK_ME[2:]):
                        pick = max(0, n_opt - 1); why = "BLOCKLIST party-changing ME"
                    elif any(xw in metxt for xw in XFORM_WORDS):
                        pick = max(0, n_opt - 1); why = "option text mentions transforming team"
                    elif "absoluteavarice" in _mk:  # EARLYWIPE 10/31: Battle It vs boss Greedent wiped w39 -> take a non-battle option
                        _nb = [i for i in range(1, len(_mo) if _mo else n_opt) if (not _mo or _mo[i])]
                        pick = _nb[0] if _nb else 0; why = "ME absolute avarice -> no battle (hardcoded)"
                    elif "mysteriouschest" in _mk:
                        pick = max(0, n_opt - 1); why = "ME mysterious chest -> leave (hardcoded, Gavin t168u)"
                    else:
                        why = "TOP option"
                        try:  # ENCOUNTER RULES (encounter_rules.json via editor); safety branches above always win
                            if globals().get("_ENC_RULES") is None:
                                import sys as _sys, os as _os
                                _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
                                from encounter_rules import EncounterRules as _ER
                                globals()["_ENC_RULES"] = _ER()
                            _R = globals()["_ENC_RULES"]; _ek = str(meinfo.get("key", ""))
                            if _R.ready and _R.encounter(_ek) is not None:
                                _d = _R.choose(_ek, _mo or None); _di = int(_d.index); _np = len(_mo) if _mo else n_opt
                                if 0 <= _di < max(1, _np) and (not _mo or _mo[_di]):
                                    pick = _di; why = f"RULES {_d.reason} [{_d.option_key}]"
                        except Exception as _e:
                            why = f"TOP option (rules error {type(_e).__name__}: {_e})"
                    if same == 0: log(f"mystery encounter w{w} key={meinfo.get('key')} type={meinfo.get('type')}: {n_opt} options -> {why} ({pick})")
                    await set_cursor(pick); await Z()
                elif h == "OptionSelectUiHandler" and (st.get("ph") in ("SelectBiomePhase",
                           "LearnMovePhase", "EggLapsePhase", "EncounterPhase") or "Mystery" in str(st.get("ph"))):
                    olabels = await ev("(()=>{const h=window.__pr_cam.scene.ui.getHandler();return (h.config&&h.config.options||[]).map(o=>o.label)})()") or []
                    if h == "OptionSelectUiHandler" and olabels and olabels[0] == "Summary" and "No" in olabels:
                        np_ = len(st.get("party") or [])
                        ans = "Yes" if (0 < np_ < 6 and "Yes" in olabels) else "No"
                        if same == 0: log(f"release/party-full prompt {olabels} in {st.get('ph')} party={np_} -> {ans}")
                        await set_cursor(olabels.index(ans)); await asyncio.sleep(0.15); await Z()
                    else:
                        clean = [re.sub(r"\[/?[a-z]+(=[^\]]*)?\]", "", str(o)).strip() for o in olabels]
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
                            await Z()
                elif h in ("MenuUiHandler", "SettingsUiHandler", "SummaryUiHandler", "PokedexPageUiHandler",
                           "OptionSelectUiHandler", "GameStatsUiHandler", "AchvsUiHandler", "SettingsDisplayUiHandler"):
                    log(f"stray menu {h} in {st.get('ph')} - back"); await X()
                else:
                    await Z()  # messages / evolution / etc.
                await asyncio.sleep(0.35)
            except Exception as e:
                log(f"ERR {e}"); traceback.print_exc(); await asyncio.sleep(2)
        log("DONE farm17")

if __name__ == "__main__":
    asyncio.run(main())

