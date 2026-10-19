"""Round231 bounded exact controls; diagnostic only."""
from pathlib import Path
from fractions import Fraction as Q
from math import gcd,isqrt
import json

p=Path(__file__).resolve().parent
def chi(n): return 0 if n%2==0 else (1 if n%4==1 else -1)
counts={'same_two_adic_covariance':0,'mixed_two_adic_alternation':0,'exact_coincidences':0}
for h in range(1,25):
 for hp in range(1,25):
  g=gcd(h,hp); a=h//g; b=hp//g
  for q in range(1,32,2):
   for qp in range(1,32,2):
    r=h*q-hp*qp; rho=r//g
    if a%2 and b%2:
     assert rho%2==0
     assert chi(q)*chi(qp)==chi(a*b)*((-1)**((rho//2)%2))
     counts['same_two_adic_covariance']+=1
    else:
     assert rho%2
     assert chi(q+2*b)*chi(qp+2*a)==-chi(q)*chi(qp)
     counts['mixed_two_adic_alternation']+=1
    if not r:
     assert a%2 and b%2 and q%b==0 and qp%a==0
     k=q//b
     assert qp//a==k and k%2
     assert chi(q)*chi(qp)==chi(a*b)
     counts['exact_coincidences']+=1

for v in range(1,513):
 weighted=sum(chi(v//h) for h in range(1,v+1) if v%h==0 and (v//h)%2)
 literal=0
 for x in range(-isqrt(v),isqrt(v)+1):
  rem=v-x*x
  y=isqrt(rem)
  if y*y==rem: literal+=1 if y==0 else 2
 assert 4*weighted==literal
counts['full_product_character_vs_literal_lattice']=512

units=[(1,0),(0,1),(-1,0),(0,-1)]
for odd in range(-15,16,2):
 for d in range(33):
  re,im=units[(odd*d)%4]
  assert (chi(d)*re,chi(d)*im)==(0,chi(odd) if d%2 else 0)
counts['real_resonance_character_identity']=528

lo=Q(1289663519481228134,10**19);hi=Q(1289663519481228135,10**19)
assert ((13762*lo+297)/50)**2<1717<((13762*hi+297)/50)**2
gamma=Q(16,125); target=Q(32,25)
assert max(Q(1),10*gamma,1+Q(20,13)*gamma)==target
assert 10*hi-Q(1,100)<target
assert 1+Q(20,13)*hi<target
assert Q(12)-Q(136,13)==Q(20,13)
assert (7+target)/26==Q(207,650)
assert 1-Q(110,13)*gamma==-Q(27,325)

result={'status':'passed','evidence_level':'diagnostic_only','counts':counts,'parameters':{'h_and_hprime':'1..24','q_and_qprime':'positive odd1..31','v':'1..512'},'exact_budget':{'gamma':str(gamma),'target':str(target),'A_first_margin_lower_bound':str(target-(10*hi-Q(1,100))),'second_margin_lower_bound':str(target-(1+Q(20,13)*hi))},'limitations':'Exact finite algebra and exponent arithmetic only. Full-product identities do not replace actual partial weighted products. No actual tail estimate or asymptotic covariance bound is certified.'}
(p/'exact_controls.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
