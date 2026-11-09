"""Apply guarded JSON changes to an extracted RC1; never use on game installation."""
import json,sys,unicodedata
from pathlib import Path
source=Path(sys.argv[1]);out=Path(sys.argv[2]);records=json.loads(Path(__file__).with_name('changes.json').read_text())
assert source.resolve()!=out.resolve(),'Use a separate output directory'
import shutil
shutil.copytree(source,out,dirs_exist_ok=True)
cache={};n=lambda v:unicodedata.normalize('NFC',v)
for r in records:
 f=r['file'];key=r['key']
 if f not in cache:cache[f]=json.loads((source/f).read_text('utf-8-sig'))
 d=cache[f]
 if isinstance(d,dict) and key in d:parent=d;leaf=key
 else:
  path=str(key).split('/');parent=d
  for part in path[:-1]:parent=parent[int(part)] if isinstance(parent,list) else parent[part]
  leaf=int(path[-1]) if isinstance(parent,list) else path[-1]
 assert n(parent[leaf])==n(r['old']),(f,key,'source differs; stop')
 parent[leaf]=r['new']
for f,d in cache.items():(out/f).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('Applied',len(records),'guarded changes to',len(cache),'JSON files')
