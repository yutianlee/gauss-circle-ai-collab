"""Restore exactly the prelaunch ledger entries after the preservation check detected decoding damage."""
from pathlib import Path
import json
from datetime import datetime,timezone
base=Path('rounds/codex-managed/gc-actual-upper-tail-a')
old=json.loads((base/'controls/prelaunch_state/round_ledger.yml').read_text(encoding='utf-8'))
p=Path('state/round_ledger.yml');current=json.loads(p.read_text(encoding='utf-8'))
assert len(current['rounds'])==len(old['rounds'])+1 and current['rounds'][-1]['round_index']==231
diffs=[{'round_index':a['round_index'],'fields':[k for k in set(a)|set(b) if a.get(k)!=b.get(k)]} for a,b in zip(current['rounds'],old['rounds']) if a!=b]
assert diffs==[{'round_index':70,'fields':['objective']},{'round_index':230,'fields':['closing_assessment']}],diffs
current['rounds']=old['rounds']+[current['rounds'][-1]]
p.write_text(json.dumps(current,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
assert json.loads(p.read_text(encoding='utf-8'))['rounds'][:-1]==old['rounds']
log={'status':'repaired','generated_at':datetime.now(timezone.utc).isoformat(),'cause':'Launch helper read historical UTF-8 ledger through Windows default decoding. Two non-ASCII descriptions changed. Closure preservation check correctly rejected this state.','changed_fields_restored_from_exact_prelaunch_snapshot':diffs,'prior_entries_preserved_after_repair':True,'graph_and_proof_draft_touched':False,'closure_before_failure':'Identity patch validated and applied in memory; matrix gates written; no ledger closure or manifest completion had occurred.','retry':'Closure script permits exact existing gates without duplication; all source reads and writes use explicit UTF-8.'}
(base/'controls/ledger_encoding_recovery.json').write_text(json.dumps(log,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'repaired','historical_entries_preserved':len(old['rounds']),'restored_fields':diffs}))
