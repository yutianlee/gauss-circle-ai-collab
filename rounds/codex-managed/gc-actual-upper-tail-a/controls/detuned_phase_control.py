"""Bounded physical real-fibre sign control, not a full-wave lower bound."""
from pathlib import Path
from math import sin,cos,pi,sqrt
import json

def chi(n):
    return 0 if n%2==0 else (1 if n%4==1 else -1)

rows=[]
for dscale in (16,32,64):
    for h in (4093,4095):
        q=h
        for c in (-1/32,0,1/32):
            radius=sqrt(h*q+4*h*c/dscale)
            # These are algebraic fibre weights, not a claim to evaluate full F.
            ds=range(dscale,2*dscale+1)
            direct=-sum(chi(d)*cos(2*pi*(q*d/4+c*d/dscale)) for d in ds)
            sine=chi(q)*sum(sin(2*pi*c*d/dscale) for d in ds if d%2)
            err=abs(direct-sine)
            assert err<2e-8,(dscale,h,c,err)
            if c:
                assert sine*chi(q)*c>0
                count=sum(1 for d in ds if d%2)
                assert abs(sine)>=count*sin(pi/16)-1e-12
            else:
                assert sine==0
            rows.append({'D':dscale,'h':h,'q':q,'c':c,'real_radius':radius,'sine_sum':sine,'direct_error':err})
result={'status':'passed','evidence_level':'diagnostic_only','precision':'Python IEEE754 binary64; absolute tolerance2e-8 for large phase evaluation. Exact phase and sine positivity are proved analytically in the cited seam repair.','controls':'Both chi4 signs; exact resonance; positive and negative physical detuning; no radius restriction to integers.','limitations':'An algebraic leading fibre control only. Does not evaluate complete F or bound any high-value-set moment. No stationary-error lower bound is inferred numerically.','rows':rows}
(Path(__file__).resolve().parent/'detuned_phase_control.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','rows':len(rows),'max_error':max(r['direct_error'] for r in rows)}))
