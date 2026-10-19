"""Exact bounded diagnostics and preservation checks; no theorem certification."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal, localcontext
from datetime import datetime, timezone
import hashlib, json, subprocess, sys

ROOT=Path(__file__).resolve().parents[2]
PACKET=Path(__file__).resolve().parent
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def chi(n): return 0 if n%2==0 else (1 if n%4==1 else -1)
def budget(g): return max(Q(1),10*g,1+Q(20,13)*g)

lo=Q(1289663519481228134,10**19)
hi=Q(1289663519481228135,10**19)
assert ((13762*lo+297)/50)**2 < 1717 < ((13762*hi+297)/50)**2
checks={'beta_rational_enclosure':[str(lo),str(hi)]}
for name,g,a,d,target in [('A',Q(16,125),Q(1,100),Q(0),Q(32,25)),('B',Q(13,125),Q(13,100),Q(1,25),Q(29,25))]:
    assert budget(g)==target
    first=10*hi-a; second=1-d+Q(20,13)*hi
    assert first<target and second<target
    checks[name]={'gamma':str(g),'low_complement':str(target),'first_margin_lower_bound':str(target-first),'second_margin_lower_bound':str(target-second),'pointwise':str((7+target)/26)}
assert 1+Q(20,13)*lo>Q(29,25)
assert 1+Q(20,13)*lo>13*hi-Q(1,2)
assert Q(12)-Q(136,13)==Q(20,13)
checks['unchanged_second_term_blocks_preferred_certificate']=True

units=[(1,0),(0,1),(-1,0),(0,-1)]
cases=0
for odd in range(-15,16,2):
    for n in range(33):
        re,im=units[(odd*n)%4]
        lhs=(chi(n)*re,chi(n)*im)
        rhs=(0,chi(odd) if n%2 else 0)
        assert lhs==rhs
        cases+=1
checks['exact_character_identity_cases']=cases
with localcontext() as context:
    context.prec=65
    beta=(50*Decimal(1717).sqrt()-297)/13762
    checks['diagnostic_decimals']={'beta':str(beta),'accepted_moment':str(10*beta),'second_tail_exponent':str(1+20*beta/13),'A_min_first_saving':str(10*beta-Decimal(32)/25),'B_min_first_saving':str(10*beta-Decimal(29)/25),'B_min_second_saving':str(20*beta/13-Decimal(4)/25)}

before=json.loads((PACKET/'starting_hashes.json').read_text())
for name,expected in before.items():
    if name=='state/next_round_plan.yml': continue
    assert sha(ROOT/name)==expected, f'Protected artifact changed: {name}'
old=json.loads((PACKET/'next_round_plan.before.json').read_text(encoding='utf-8-sig'))
new=json.loads((ROOT/'state/next_round_plan.yml').read_text(encoding='utf-8-sig'))
changed={k for k in old.keys()|new.keys() if old.get(k)!=new.get(k)}
assert changed<={'candidate_objective','design_constraint','upper_tail_strategy_update'},changed
assert new['status']=='pending_design' and new['tasks']==[] and new['campaign_id'] is None
assert new['round_index']==231
results=[]
for args in [['-m','math_collab.validate_state_patch'],['-m','math_collab.campaigns','validate']]:
    result=subprocess.run([sys.executable,*args],cwd=ROOT,capture_output=True,text=True)
    results.append({'command':[sys.executable,*args],'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
    assert result.returncode==0,result.stdout+result.stderr
out={'status':'passed','checked_at':datetime.now(timezone.utc).isoformat(),'evidence_level':'diagnostic_only','exact_checks':checks,'protected_files_verified':len(before)-1,'workflow_changed_keys':sorted(changed),'validators':results,'graph_sha256':sha(ROOT/'state/proof_obligations.yml'),'analytic_campaign_launched':False,'state_patch_applied':False}
(PACKET/'validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','protected_files':len(before)-1,'character_cases':cases,'workflow_changed_keys':sorted(changed)}))
