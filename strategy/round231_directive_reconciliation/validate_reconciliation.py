"""Bounded exact diagnostics and read-only state preservation validation."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal, localcontext
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
PACKET = Path(__file__).resolve().parent

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def envelope(eta):
    return max(F(29,32)+eta/8, F(13,16)+5*eta/16, F(11,18)+2*eta/3)

def saving(eta):
    return min(F(1),F(1,2)+eta)-envelope(eta)

checks = {}
checks['critical_saving'] = str(saving(F(1,2)))
assert saving(F(1,2)) == F(1,32)
assert saving(F(13,28)) == saving(F(7,12)) == 0
assert saving(F(9,20)) < 0 and saving(F(3,5)) < 0
assert saving(F(12,25)) > 0 and saving(F(11,20)) > 0
checks['envelope_boundary_and_interior_checks'] = 'pass'

mask_cases=0
for ncols in range(1,25):
    q=4*ncols+1
    support={k % q for k in range(-ncols,1)}
    for b in range(ncols+1):
        for n in range(1,ncols+1):
            assert ((n-b)%q in support) == (n<=b)
            mask_cases+=1
checks['exact_prefix_selector_cases'] = mask_cases

for gamma,expected in [(F(13,125),F(29,25)),(F(16,125),F(32,25))]:
    moment=max(F(1),10*gamma,1+20*gamma/13)
    assert moment == expected
    checks[f'complement_gamma_{gamma}']=str(moment)
for b,lam,theta in [(F(1),F(0),F(4,13)),(F(29,25),F(2,25),F(102,325)),(F(32,25),F(7,50),F(207,650))]:
    assert (b-1)/2 == lam
    assert (4+lam)/13 == theta
    assert F(1,4)+(b+F(1,2))/26 == theta
    checks[f'moment_b_{b}']={'lambda':str(lam),'pointwise':str(theta)}
with localcontext() as ctx:
    ctx.prec=70
    theta=(Decimal(3292)+25*Decimal(1717).sqrt())/Decimal(13762)
    beta=2*theta-Decimal('0.5')
    checks['decimal_diagnostics']={
        'theta':str(theta),'beta':str(beta),'accepted_b12':str(10*beta),
        'pointwise_b12_threshold':str(13*beta-Decimal('0.5')),
        'sharp_lambda_threshold':str(13*theta-4),
        'central_gamma_threshold':str(Decimal(13)*(13*beta-Decimal('1.5'))/20)
    }

protected=json.loads((PACKET/'starting_hashes.json').read_text(encoding='utf-8-sig'))
protected+=json.loads((PACKET/'protected_tree_hashes.json').read_text(encoding='utf-8-sig'))
for item in protected:
    path=Path(item['path'])
    if not path.is_absolute():
        path=ROOT/path
    assert sha(path)==item['sha256'], f'Protected content changed: {path}'

commands=[]
for args in [['-m','math_collab.validate_state_patch'],['-m','math_collab.campaigns','validate']]:
    done=subprocess.run([sys.executable,*args],cwd=ROOT,capture_output=True,text=True)
    commands.append({'command':[sys.executable,*args],'exit_code':done.returncode,'stdout':done.stdout,'stderr':done.stderr})
    assert done.returncode==0,done.stdout+done.stderr

future=json.loads((ROOT/'state/next_round_plan.yml').read_text(encoding='utf-8-sig'))
assert future['round_index']==231 and future['status']=='pending_design' and future['tasks']==[]
assert future['campaign_id'] is None
previous=json.loads((PACKET/'next_round_plan.before.json').read_text(encoding='utf-8-sig'))
changed_keys={key for key in previous.keys()|future.keys() if previous.get(key)!=future.get(key)}
assert changed_keys <= {'candidate_objective','strategy_reconciliation'}, changed_keys
checks['workflow_keys_changed']=sorted(changed_keys)
result={
    'checked_at':datetime.now(timezone.utc).isoformat(),
    'status':'passed',
    'evidence_level':'diagnostic_only; analytical proofs and source matching remain necessary',
    'checks':checks,'protected_files_verified':len(protected),'validation':commands,
    'graph_sha256':sha(ROOT/'state/proof_obligations.yml'),
    'analytic_campaign_launched':False,'state_patch_applied':False
}
(PACKET/'validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','protected_files':len(protected),'exact_selector_cases':mask_cases,'graph_sha256':result['graph_sha256']}))
