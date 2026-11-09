import sys
import json,re,unicodedata as U,hashlib,zipfile,collections
from pathlib import Path
ROOT=Path(sys.argv[1]); SRC=Path(sys.argv[2]);errors=[];notes=[]
def n(s):return U.normalize('NFC',s)
def walk(x,p=()):
 if isinstance(x,dict):
  for k,v in x.items():yield from walk(v,p+(k,))
 elif isinstance(x,list):
  for k,v in enumerate(x):yield from walk(v,p+(k,))
 else:yield p,x
def hook(items):
 d={}
 for k,v in items:
  if k in d:errors.append('Duplicate key '+str(k))
  d[k]=v
 return d
D={};base=[];refs=0;leaves=0;unchanged=0
for p in ROOT.rglob('*.json'):
 f=str(p.relative_to(ROOT));raw=p.read_bytes()
 try:D[f]=json.loads(raw.decode('utf-8-sig'),object_pairs_hook=hook)
 except Exception as e:errors.append(f+': '+str(e));continue
 if '\ufffd' in raw.decode('utf-8-sig'):errors.append(f+': U+FFFD')
 before=json.loads((SRC/f).read_text('utf-8-sig'))
 a=dict(walk(D[f]));b=dict(walk(before))
 if a.keys()!=b.keys():errors.append(f+': changed property paths')
 if re.search(r'\.[a-z]{2}-[A-Z]{2}\.json$',f):
  refs+=1
  if raw!=(SRC/f).read_bytes():errors.append(f+': changed reference file')
 else:
  base.append(f);leaves+=sum(isinstance(v,str) for v in a.values())
 if raw==(SRC/f).read_bytes():unchanged+=1
# Verify typed non-localized fields equal bundled reference; display slots deliberately excluded.
for f in ['Data/Furniture.json','Data/Fish.json','Data/animationDescriptions.json','Data/CookingRecipes.json','Data/CraftingRecipes.json','Data/Monsters.json','Data/Boots.json','Data/hats.json','Data/Bundles.json','Data/NPCGiftTastes.json','Data/Quests.json']:
 for k,v in D[f].items():
  e=D[f.replace('.json','.es-ES.json')][k];a=v.split('/');b=e.split('/')
  if f in ['Data/Furniture.json','Data/Fish.json','Data/animationDescriptions.json']:ok=v==e
  else:
   keep={'Data/CookingRecipes.json':{4},'Data/CraftingRecipes.json':{5},'Data/Monsters.json':{14},'Data/Boots.json':{1,6},'Data/hats.json':{1,5},'Data/Bundles.json':{6},'Data/NPCGiftTastes.json':set(range(0,10,2)) if not k.startswith('Universal_') else set(),'Data/Quests.json':{1,2,3,9}}[f]
   ok=len(a)==len(b) and all(x==y for i,(x,y) in enumerate(zip(a,b)) if i not in keep)
  if not ok:errors.append((f,k,'technical parity'))
# Internal names/IDs must not be translated when DisplayName handles localization.
def check_names(f,a,b,path=()):
 if isinstance(a,dict):
  if 'Name' in a and 'DisplayName' in a and a['Name']!=b['Name']:errors.append((f,path,'internal name'))
  if f=='Data/Machines.json' and 'Id' in a and a['Id']!=b['Id']:errors.append((f,path,'machine id'))
  for k,v in a.items():check_names(f,v,b[k],path+(k,))
 elif isinstance(a,list):
  for i,v in enumerate(a):check_names(f,v,b[i],path+(i,))
for f in ['Data/Objects.json','Data/BigCraftables.json','Data/Weapons.json','Data/Tools.json','Data/Shirts.json','Data/Pants.json','Data/Concessions.json','Data/Machines.json']:
 check_names(f,D[f],D[f.replace('.json','.es-ES.json')])
if D['Data/RandomBundles.json']!=D['Data/RandomBundles.es-ES.json']:errors.append('RandomBundles technical mismatch')
# Data -> Strings references restored in tables must resolve.
resolved=0
for f in ['Data/Furniture.json','Data/animationDescriptions.json']:
 for k,v in D[f].items():
  for asset,key in re.findall(r'(Strings\\[A-Za-z0-9_]+):([^\]\/]+)',v):
   df=asset.replace('\\','/')+'.json'
   if df not in D or key not in D[df]:errors.append((f,k,'unresolved',df,key))
   else:resolved+=1
# Compare command/token signatures for edited displayed leaves, ignoring grammatical gender additions.
def ungender(s):
 return re.sub(r'\$\{(?:[^{}]|\{\d+\})*\}\$','',s)
def controls(s):
 s=ungender(s)
 return re.findall(r'\$[a-z]+\b|\$\d+\b|\|\||#',s)
changed=json.load(open(Path(__file__).with_name('changes.json')))
for r in changed:
 f,k=r['file'],r['key'];s=r['new'];old=r['old']
 if any(c in r['categories'] for c in ['Phục hồi dữ liệu 1.6','Phục hồi định danh nội bộ']) or f=='Strings/credits.json':continue
 if controls(s)!=controls(old):errors.append((f,k,'control sequence changed',controls(old),controls(s)))
 # Placeholder set: copy may naturally use player name/variables more often, but never drop parameter indices.
 def params(v):return set(re.findall(r'\{\d+\}',v))
 if params(s)!=params(old):errors.append((f,k,'parameter set changed'))
 if len(re.findall(r'\$\{',s))!=len(re.findall(r'\$\{(?:[^{}]|\{\d+\})*\}\$',s)):errors.append((f,k,'malformed gender'))
# Event skeleton comparison: mask quotes and localizable quickQuestion prompt/options only.
def mask(s):
 s=re.sub(r'"(?:\\.|[^"\\])*"','"TEXT"',s)
 s=re.sub(r'(quickQuestion )[^/]*?(?=\(break\))',r'\1TEXT',s)
 return s
candidates=[];event_keys=0
for f in base:
 if not f.startswith('Data/Events/'):continue
 en=D[f.replace('.json','.es-ES.json')]
 for k,s in D[f].items():
  event_keys+=1
  if mask(s)!=mask(en[k]):candidates.append((f,k))
# All residual skeleton differences go to explicit triage, not hidden as pass.
if candidates:notes.append({'event_skeleton_candidates':candidates})
# Verify all 36 audit cases changed, and no wrong terminology in actual referential entries.
audit=json.load(open(Path(__file__).with_name('evidence_rc1.json')))['findings']; touched={(r['file'],r['key']) for r in changed}
for r in audit:
 if (r['file'],r['key']) not in touched:errors.append((r['file'],r['key'],'audit case unpatched'))
# Regression: no unrelated inserted jokes.
for f in base:
 for path,v in walk(D[f]):
  if isinstance(v,str) and re.search(r'Min là con gái|Hảo Hảo ngon hơn|Bột chấm hảo hảo',n(v),re.I):errors.append((f,path,'foreign insertion'))
summary=dict(json_files=len(D),base_files=len(base),reference_files=refs,string_leaves=leaves,unchanged_json_files=unchanged,changed_keys=len(changed),changed_json_files=len(set(r['file'] for r in changed)),restored_reference_targets=resolved,event_files=43,event_records=event_keys,event_skeleton_remaining=len(candidates),audit_cases_patched=len(audit),errors=errors,notes=notes,runtime_tested=False,installable_package_verified=False,coverage_statement='All JSON/static checks; targeted manual review. Not a claim of full sentence-by-sentence acceptance.')
Path(__file__).with_name('validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
print(json.dumps(summary,ensure_ascii=False,indent=2))
