"""Round232 integer/rational controls. Diagnostic only; no asymptotic inference."""
from pathlib import Path
from fractions import Fraction as Q
from math import gcd
import json
base=Path(__file__).resolve().parent
def chi(n):return 0 if n%2==0 else (1 if n%4==1 else -1)
v=[1,-2,1]
band=sum(v[i]*v[j] for i in range(3) for j in range(3) if abs(i-j)<=1)
assert band==-2 and sum(v)**2==0
count=0;pair_controls=0
for start in [Q(1),Q(7,2),Q(51),Q(201,2)]:
 for U in [Q(1,2),Q(3,2),Q(4),Q(17,2),Q(23),Q(81,2)]:
  ints=[n for n in range(1,160) if start<=n<=start+U]
  for g in range(1,int(U)+4):
   ng=sum(n%g==0 for n in ints)
   assert ng*(ng-1)<=(U/g+1)*(U/g)
   if g>U:assert ng<=1
   count+=1
  for G in [1,2,3,5,11,25]:
   actual=sum(p!=q and gcd(p,q)>=G for p in ints for q in ints)
   enlarged=sum(sum(n%g==0 for n in ints)*(sum(n%g==0 for n in ints)-1) for g in range(G,int(U)+1))
   upper=sum(((U/g+1)*(U/g) for g in range(G,int(U)+1)),Q(0))
   assert actual<=enlarged<=upper
   pair_controls+=1

sign_controls=0
for T in range(101,302,2):
 for u in range(3,34):
  h=T;hp=T+4;q=T+2*u;qp=q-4
  p=h*q;pp=hp*qp;r=pp-p
  assert gcd(h,hp)==1 and r==8*u-16 and r>0
  assert chi(q)*chi(qp)==1
  assert chi(h*hp)*(-1)**((r//2)%2)==1
  sign_controls+=1

lo=Q(1289663519481228134,10**19);hi=Q(1289663519481228135,10**19)
assert ((13762*lo+297)/50)**2<1717<((13762*hi+297)/50)**2
gamma=Q(16,125); b=Q(32,25); a_hi=10*hi-b
near=Q(1,2)-4*gamma;high=1-6*gamma-Q(1,4)
assert near==-Q(3,250) and high==-Q(9,500)
assert -near>a_hi and -high>a_hi
assert 4*gamma-a_hi>Q(1,2)
assert 1-6*gamma+a_hi<Q(1,4)
assert Q(2)*(1-(1-2*gamma)/2)-Q(1,4)==Q(503,500)
result={'status':'passed','evidence_level':'diagnostic_only','counts':{'non_psd_band':1,'multiple_bounds':count,'distinct_gcd_pair_bounds':pair_controls,'actual_small_gcd_character_identity':sign_controls},'exact_exponents':{'near':str(near),'high_gcd':str(high),'near_margin_lower':str(-near-a_hi),'high_gcd_margin_lower':str(-high-a_hi),'same_premise_attempt':2},'parameters':'Real intervals with rational starts1,7/2,51,201/2 and lengths1/2,3/2,4,17/2,23,81/2; odd T101..301 and u3..33 for algebraic separated-product identity.','limitations':'Checks exact finite algebra and budget arithmetic only. The small-gcd construction is not a full-wave upper-tail event. No target A or signed exceptional-set saving is certified.'}
(base/'exact_controls.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
