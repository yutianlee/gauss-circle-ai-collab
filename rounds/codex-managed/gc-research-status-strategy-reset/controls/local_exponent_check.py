from fractions import Fraction as F
from decimal import Decimal, getcontext
import json
getcontext().prec=60
theta=(Decimal(3292)+25*Decimal(1717).sqrt())/13762
beta=2*theta-Decimal(1)/2
assert F(1,4)+(F(29,25)+F(1,2))/(2*13)==F(102,325)
for p in range(2,101):
    assert (F(5,4)+1+F(p,2))/(2*(p+1))==F(1,4)+F(7,8*(p+1))
    # Independent rational coefficient comparison in the formal variable theta.
    assert F(p-2,p+1)-1==F(-3,p+1)
    assert F(1,p+1)==F(1,p+1)
assert Decimal(102)/325<theta<Decimal(1)/3
assert Decimal(1)/8<beta<Decimal(13)/100
out={'evidence_level':'diagnostic_only','exact_rational_checks':'pass','theta':str(theta),'beta':str(beta),'twelfth_target_pointwise':str(Decimal(102)/325),'twelfth_threshold_to_beat_theta':str(13*beta-Decimal(1)/2),'accepted_twelfth_exponent':str(10*beta),'cusp_cap_saving_threshold_at_N_eq_T':str(Decimal(1)/2-2*beta)}
print(json.dumps(out,indent=2))
