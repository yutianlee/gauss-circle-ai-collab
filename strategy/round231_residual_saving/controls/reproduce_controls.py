"""Conductor's bounded exact/symbolic diagnostics, never asymptotic certification."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal, localcontext
import json,math

out={'diagnostic_only':True,'status':'passed','command':'python strategy/round231_residual_saving/controls/reproduce_controls.py'}
def atan_recip(n):
    x=Decimal(1)/n;term=x;s=term;k=1
    while abs(term)>Decimal('1e-78'):
        term=-term*x*x;s+=term/(2*k+1);k+=1
    return s
with localcontext() as ctx:
    ctx.prec=80
    pi=16*atan_recip(5)-4*atan_recip(239)
    def tail(z):
        a=sum((F(1,n) if n%4==1 else -F(1,n)) for n in range(1,z,2))
        return pi/4-Decimal(a.numerator)/Decimal(a.denominator)
    rows=[]
    for z in [5,9,17,41]:
        a=tail(z);b=tail(z*z)
        assert Decimal(0)<=a-Decimal(1)/(2*z)<=Decimal(1)/(z*(z+1))
        rows.append({'z':z,'2zA(z)':str(2*z*a),'scaled_zero_phase_mean':str(4*z*(-17*a+18*b)),'scaled_quarter_phase_mean':str(2*z*a)})
    out['chi4_tail_diagnostic']={'precision_digits':80,'rows':rows,'limits':{'scaled_zero_phase_mean':-34,'scaled_quarter_phase_mean':1}}

cases=[]
for p,d in [(5,2),(5,3),(5,4),(7,5),(7,6),(7,2),(7,3),(7,4)]:
    assert p>d
    q=p**d;s=p**(d-1);counts=[0]*q
    for n in range(q):counts[pow(n,d,q)]+=1
    # Exact reduction modulo Phi_(p^d)(X)=sum_(j=0)^(p-1) X^(j*p^(d-1)).
    reduced=[]
    for j in range(p-1):
        for b in range(s):reduced.append(counts[b+j*s]-counts[b+(p-1)*s])
    assert reduced[0]==s and not any(reduced[1:])
    cases.append({'p':p,'degree':d,'modulus':q,'exact_complete_sum':s})
out['inverse_common_exponent_control']=cases
alpha=F(11,50);sigma0=F(52,125)
gamma=F(13,84)+sigma0*(-F(29,168)+alpha/2)
out['exact_exponents']={'strip_sup':str(gamma),'strip_M12':str(10*gamma),'common_C_all_degree_maximum_saving':str(F(7,72)),'conditional_separate_A3_B4_sup':str(F(23,180)),'conditional_separate_A3_B4_M12':str(F(23,18))}
for d in range(2,101):
    val=F(4*d-5,6*d*(d+1))
    assert F(7,72)-val==F((d-3)*(7*d-20),72*d*(d+1))>=0
out['all_degree_identity']='7/72-(4d-5)/(6d(d+1))=(d-3)(7d-20)/(72d(d+1)); nonnegative for integers d>=2'
a=F(26,125)-F(13,42)
assert a==-F(533,5250)
assert F(13,84)+a/2==F(13,125)
assert -F(29,168)+F(29,84)/2==0
assert a+sigma0*F(29,84)==sigma0*F(17,168)>0
assert a+F(29,84)==F(853,3500)<F(1,2)
out['adaptive_factor_cutoff']={'T_exponent':str(a),'x_exponent':'29/84','top_scale_cutoff':'853/3500','supremum':'13/125','M12':'29/25','diagnostic_only':True}
Path(__file__).with_name('finite_controls.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'exact_cyclotomic_cases':len(cases),'exponents':out['exact_exponents']},indent=2))
