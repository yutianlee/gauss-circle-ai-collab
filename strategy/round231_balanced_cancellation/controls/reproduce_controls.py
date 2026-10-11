"""Bounded exact diagnostics; no asymptotic certification."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import json
out={'diagnostic_only':True,'status':'passed','command':'python strategy/round231_balanced_cancellation/controls/reproduce_controls.py'}
def chi(n): return 0 if n%2==0 else (1 if n%4==1 else -1)
# Gaussian-integer fourth roots of unity, with no floating point.
i4=[(1,0),(0,1),(-1,0),(0,-1)]
rows=[]
for D in [4,8,16,64]:
 for j in [0,1,2,3]:
  re=sum(chi(d)*i4[(j*d)%4][0] for d in range(D+1,2*D+1))
  im=sum(chi(d)*i4[(j*d)%4][1] for d in range(D+1,2*D+1))
  expected=(0,D//2 if j==1 else -D//2 if j==3 else 0)
  assert (re,im)==expected
  rows.append({'D':D,'phase_numerator_over4':j,'sum':[re,im]})
out['exact_quarter_character_sums']=rows
res=[]
for h in [7,16,41]:
 for sign in [-1,1]:
  R2=h*(4*h+sign)
  alpha=F(R2,4*h)
  assert alpha-h==F(sign,4)
  stationary_ratio=F(R2,4*h*h)
  assert F(1,2)<stationary_ratio<F(3,2)
  res.append({'h':h,'sign':sign,'R_squared':R2,'outer_phase':str(alpha),'stationary_m_over_d':str(stationary_ratio)})
out['actual_reciprocal_resonances']=res
hessian=0
for a in range(1,9):
 for b in range(1,9):
  fdd=-F(b,4*a**3); fmm=-F(a,4*b**3); fdm=F(1,4*a*b)
  assert fdd*fmm-fdm**2==0
  hessian+=1
out['rank_one_hessian_exact_cases']=hessian
r2=[0]*129
for a in range(-isqrt(128),isqrt(128)+1):
 for b in range(-isqrt(128),isqrt(128)+1):
  n=a*a+b*b
  if n<=128:r2[n]+=1
ownership=0
for n in range(1,129):
 divisors=[d for d in range(1,n+1) if n%d==0]
 assert r2[n]==4*sum(chi(d) for d in divisors)
 for j in range(1,2*isqrt(n)+2):
  c=F(j,2)
  if c*c>=n:continue
  u=4*sum(chi(d)+chi(n//d) for d in divisors if d<c)
  w=4*sum(chi(d) for d in divisors if d>=c and n//d>=c)
  assert u+w==r2[n]
  ownership+=1
out['exact_actual_hyperbola_ownership_cases']=ownership
profiles=[]
for g in [F(13,125),F(1,8),F(16,125)]:
 a=2*g-F(13,42); lo=4*g; hi=1-2*g
 assert lo<hi and a<0 and a+lo*F(29,84)>0
 assert F(13,84)+a/2==g
 profiles.append({'gamma':str(g),'moment_budget':str(max(F(1),10*g,1+20*g/13)),'lower_norm':str(lo),'upper_norm':str(hi),'T_factor_cutoff':str(a)})
out['combined_owner_profiles']=profiles
nu=F(2,3)
assert nu/4==F(1,8)+nu/16==(1-nu)/2==F(1,6)
out['optimistic_certificate_crossing']={'norm_exponent':'2/3','ceiling_exponent':'1/6','M12_certificate':'5/3'}
out['scope']='Exact finite normalization, factor ownership, resonant character, and rational arithmetic controls only; no actual moment lower bound or numerical asymptotic proof.'
Path(__file__).with_name('finite_controls.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'character_cases':len(rows),'hyperbola_cases':ownership,'hessian_cases':hessian,'profiles':profiles},indent=2))
