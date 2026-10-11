"""Bounded exact diagnostics; no asymptotic conclusion is computed."""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from pathlib import Path
import json

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c
def add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]

# Numerator after a common denominator in H_p(1) * sum_a kappa_(p^a)/kappa p^(-2a).
# (p-1)^2[(p+2)(p^2-1)+2(p+1)] = p(p^2-1)^2.
left=mul([1,-2,1],add(mul([2,1],[-1,0,1]),[2,2]))
right=mul([0,1],mul([-1,0,1],[-1,0,1]))
assert left==right
rows=[]
for p in [5,13,17,29,37,41,53,61]:
    h=(1-F(1,p))**2*(1+F(2,p))
    k=1/(1-F(1,p*p))+2*F(p+1,p+2)*F(1,p*p)/(1-F(1,p*p))**2
    assert h*k==1
    for a in range(8):
        u=F(2*a+2,2*a+1)
        actual=(2*a+1)*(1+u/p)*(1-F(1,p))**2
        predicted=h*(1+2*a*F(p+1,p+2))
        assert actual==predicted
    rows.append({'p':p,'local_product':str(h*k),'exponents_checked':'0..7'})
# e^(-3*pi*i/4)*e^(pi*i/4)=e^(-pi*i/2)=-i, real part exactly zero.
phase_eighth_root_index=(-3+1)%8
assert phase_eighth_root_index==6
with localcontext() as ctx:
    ctx.prec=60
    beta=(50*Decimal(1717).sqrt()-297)/13762
    exponents={
      'beta':str(beta),'accepted_b12':str(10*beta),'target_b12':str(Decimal(29)/25),
      'additional_moment_saving':str(10*beta-Decimal(29)/25),
      'cdf_target_power':str(Decimal(4)/25),
      'repeated_class_error':str(8*beta-Decimal(1)/5),
      'centering_moment_error':str(9*beta-Decimal(11)/10),
      'known_relative_cancellation_power':str(Decimal(5)/2-10*beta),
      'required_relative_cancellation_power':str(Decimal(5)/2-Decimal(29)/25),
    }
out={'status':'passed','diagnostic_only':True,'symbolic_polynomial_identity':left==right,
     'local_euler_controls':rows,'abel_phase_real_part':0,'abel_phase_control':'eighth root index6 = -i',
     'exponents':exponents,'limits':'Exact finite algebra plus high-precision algebraic exponents; neither numerical asymptotics nor proof of the residual arithmetic estimate.'}
Path(__file__).with_name('local_exact_controls.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
