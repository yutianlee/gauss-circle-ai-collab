"""Exact independent reproduction; no asymptotic conclusion from computation."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb,prod
from collections import Counter,defaultdict
from itertools import permutations,product
import json
NMAX=12;zero=(0,)*NMAX
def iparts(n,cap=None):
 if n==0:yield ();return
 for first in range(min(n,cap or n),1-1,-1):
  for rest in iparts(n-first,first):yield (first,)+rest
def mul(x,y):
 out=defaultdict(int)
 for a,c in x.items():
  for b,d in y.items():out[tuple(i+j for i,j in zip(a,b))]+=c*d
 return dict(out)
def moment(n):
 a=[0]*NMAX;a[n-1]=1;return {tuple(a):1}
kap=[{},moment(1)];checks=[]
for n in range(2,NMAX+1):
 k=defaultdict(int,moment(n))
 for j in range(1,n):
  for mon,c in mul(kap[j],moment(n-j)).items():k[mon]-=comb(n-1,j-1)*c
 k={a:c for a,c in k.items() if c};kap.append(k)
 explicit={}
 for v in iparts(n):
  mult=factorial(n)//(prod(factorial(q) for q in v)*prod(factorial(c) for c in Counter(v).values()))
  mon=tuple(v.count(i) for i in range(1,NMAX+1));explicit[mon]=(-1)**(len(v)-1)*factorial(len(v)-1)*mult
 assert k==explicit and sum(k.values())==0
 checks.append({'order':n,'partition_vs_recurrence':True,'constant_cumulant_zero':True})
costs=[]
for v in iparts(12):
 if len(v)<2 or min(v)<3:continue
 cost=1+sum(max(F(q,4)-1,0) for q in v)
 mon=tuple(v.count(i) for i in range(1,NMAX+1))
 costs.append({'blocks':v,'outer_exponent':str(cost),'coefficient':kap[12][mon]})
assert max(F(x['outer_exponent']) for x in costs)==F(9,4)
balanced=[]
for n in [12,24,48]:
 signed=F(factorial(12)*comb(n//2,6),n**6)
 absolute=F(factorial(n)//factorial(n-12),n**6)
 balanced.append({'labels':n,'signed':str(signed),'absolute':str(absolute)})
assert balanced==[{'labels':12,'signed':'1925/12','absolute':'1925/12'},{'labels':24,'signed':'148225/64','absolute':'1301375075/192'},{'labels':48,'signed':'64774325/12288','absolute':'33527982212725/12288'}]
def setparts(seq):
 if not seq:yield ();return
 x,*tail=seq
 for p in setparts(tail):
  yield ((x,),)+p
  for i in range(len(p)):yield p[:i]+((x,)+p[i],)+p[i+1:]
partitions=list(setparts(list(range(6))));assert len(partitions)==203
nu=[F(1,3),F(2,3)];cases=[]
for vals in [[(j-2,(-1)**j) for j in range(6)],[(1,2)]*3+[(-1,-2)]*3]:
 def block_m(labels):return sum(nu[r]*prod(vals[d][r] for d in labels) for r in range(2))
 direct=sum(block_m(d[:3])*block_m(d[3:]) for d in permutations(range(6)))
 expanded=F(0)
 for pi in partitions:
  coeff=prod((-1)**(len(c)-1)*factorial(len(c)-1) for c in pi)
  integral=F(0)
  for r0,r1 in product(range(2),repeat=2):
   term=F(1)
   for c in pi:term*=sum(prod(vals[d][r0 if pos<3 else r1] for pos in c) for d in range(6))
   integral+=nu[r0]*nu[r1]*term
  expanded+=coeff*integral
 assert direct==expanded
 H2=max(sum(v[r]**2 for v in vals) for r in range(2))
 L=[sum(nu[r]*abs(sum(v[r] for v in vals))**j for r in range(2)) for j in range(4)]
 bound=F(0)
 for pi in partitions:
  singles=[c[0] for c in pi if len(c)==1];k0=sum(s<3 for s in singles);k1=len(singles)-k0
  # Total nonsingleton degree can be odd; use H>=1 and integer H=H2.
  coeff=prod(factorial(len(c)-1) for c in pi)
  bound+=coeff*H2**(6-len(singles))*L[k0]*L[k1]
 assert abs(direct)<=bound
 cases.append({'direct':str(direct),'collision_expansion':str(expanded),'bound_passed':True,'set_partitions':len(partitions)})
harmonic=F(1,2**18)+F(1,3**18)+F(1,4**18)+F(1,5**9)+F(1,8*5**8)
assert harmonic==F(241757181358081099469,51998697814228992000000000)
assert harmonic<F(1,200000) and F(1,2**12)-2*harmonic>F(1,2**13)
assert F(1,4)+3*(F(1,9)+F(1,8))==F(23,24)
assert F(1,4)+(1+2*F(29,25))/(4*13)==F(102,325)
rows=[[1,-2,3,-1,2,0,-3],[2,1,-1,3,-2,4,1]]
direct=sum(prod(rows[0 if j<3 else 1][ds[j]] for j in range(6)) for ds in permutations(range(7),6))
expanded=sum(prod((-1)**(len(c)-1)*factorial(len(c)-1)*sum(prod(rows[0 if j<3 else 1][d] for j in c) for d in range(7)) for c in pi) for pi in partitions)
assert direct==expanded==-68112
out={'status':'passed','evidence_level':'diagnostic_only','cumulant_coefficients':checks,'proper_partitions':costs,'maximum_outer_exponent':'9/4','balanced_constant_controls':balanced,'independent_multiradius_checks':cases,'discovery_report_mixed_radius_control':{'direct':direct,'expanded':expanded,'distinct_assignments':5040},'reviewer_harmonic_control':{'exact_upper':str(harmonic),'less_than_1_over_200000':True,'positive_margin':True,'squarefree_union':'23/24','conditional_restoration':'102/325'},'limitations':'Exact finite identities and budget arithmetic only; no sampled asymptotic or proof of a signed arithmetic bound.'}
Path(__file__).with_name('exact_local_controls.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
