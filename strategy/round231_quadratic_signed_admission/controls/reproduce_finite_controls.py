"""Bounded conductor diagnostics; no asymptotic proof is inferred."""
from pathlib import Path
import cmath, math, json
from decimal import Decimal, localcontext
from fractions import Fraction

out = {'status':'passed', 'role':'conductor independent reproduction',
       'diagnostic_only':True, 'command':'python strategy/round231_quadratic_signed_admission/controls/reproduce_finite_controls.py',
       'precision':'finite integer residue counts; complex double with 1e-10 tolerance; 70-digit Decimal radical residual'}
max_error=0.0; cases=0; grams=0
for p in [3,5,7,11,13,17,19,23,29,31]:
    chi=1 if p%4==1 else -1
    nu=[0]*p
    for x in range(p):
        for y in range(p):nu[(x*x+y*y)%p]+=1
    assert nu==[p-chi+p*chi*(n==0) for n in range(p)]
    ep=lambda n: cmath.exp(2j*math.pi*(n%p)/p)
    A=[[sum(ep(a*n*n+b*n) for n in range(p))/p for b in range(p)] for a in range(p)]
    W=[[sum((nu[n]/p-1)*ep(a*n*n+b*n) for n in range(p))/p for b in range(p)] for a in range(p)]
    for a in range(p):
        for b in range(p):
            err=abs(W[a][b]-chi/p*(1-A[a][b]));max_error=max(max_error,err);cases+=1
        for c in range(p):
            direct=sum(W[a][b]*W[c][b].conjugate() for b in range(p))
            expected=(p-2+A[(a-c)%p][0])/p**2
            err=abs(direct-expected);max_error=max(max_error,err);grams+=1
        mean=sum(W[a])/p
        expected_mean=chi*(p-1)/p**2
        max_error=max(max_error,abs(mean-expected_mean))
        energy=sum(abs(z)**2 for z in W[a])
        const_energy=p*abs(mean)**2
        assert abs(const_energy/energy-(p-1)/p)<1e-10
assert max_error<1e-10
out['finite_quadratic_rows']={'primes':[3,5,7,11,13,17,19,23,29,31], 'transform_cases':cases,'gram_cases':grams,'max_absolute_error':max_error,'tolerance':1e-10}

def r2(n):
    s=0
    for d in range(1,math.isqrt(n)+1):
        if n%d==0:
            s += (0 if d%2==0 else (1 if d%4==1 else -1))
            e=n//d
            if e!=d:s += (0 if e%2==0 else (1 if e%4==1 else -1))
    return 4*s
with localcontext() as ctx:
    ctx.prec=70
    m=10**6;k=1;T=8*10**9;h=10
    rows=[];mass=0;real=0
    for j in range(-h,h+1):
        poly=8*k*m*m+4*k*m*j-k*j*j
        error=Decimal(T)*Decimal(m+j).sqrt()-Decimal(poly)
        phase=2*math.pi*float(error)
        count=r2(m+j)
        rows.append({'j':j,'r2':count,'taylor_error':str(error)})
        mass+=count; real+=count*math.cos(phase-3*math.pi/4)
        assert abs(phase)<=math.pi/12
    assert mass>0 and real<=-mass/2
    out['actual_resonant_patch']={'m':m,'k':k,'T':T,'h':h,'mass':mass,'physical_real_unweighted':real,'max_abs_taylor_error':max(abs(Decimal(x['taylor_error'])) for x in rows).__str__(),'rows':rows}
out['rational_exponent_controls']={
 'quadratic_singleton_sigma':str(Fraction(2,5)),
 'quadratic_source_length_sigma':str(Fraction(6,9)),
 'quartic_source_length_sigma':str(Fraction(6,17)),
 'paid_head_sigma':str(Fraction(52,125)),
 'quartic_H_exponent_in_N_at_head':str(Fraction(9,10)-Fraction(1,5)/Fraction(52,125)),
 'quartic_source_margin_at_head':str(Fraction(9,10)-Fraction(1,5)/Fraction(52,125)-Fraction(1,3))}
gamma_s=Fraction(13,84)-Fraction(103,840)*Fraction(52,125)
out['rational_exponent_controls'].update({
 'type_i_gamma':str(gamma_s),
 'type_i_sup_margin':str(Fraction(13,125)-gamma_s),
 'type_i_moment':str(1+Fraction(20,13)*gamma_s),
 'type_i_moment_margin':str(Fraction(29,25)-(1+Fraction(20,13)*gamma_s))})
Path(__file__).with_name('finite_controls.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='actual_resonant_patch'},indent=2))
print('Resonant patch mass',mass,'physical real sum',real)
