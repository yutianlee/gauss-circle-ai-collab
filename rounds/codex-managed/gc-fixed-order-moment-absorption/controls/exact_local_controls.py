"""Independent integer-polynomial reproduction of the Wolfram finite checks."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
from math import factorial,comb
import json
MAX=16
zero=(0,)*MAX
polys=[{zero:1}]
for n in range(1,MAX+1):
 out=defaultdict(int)
 for j in range(1,n+1):
  factor=(-1)**(j-1)*factorial(n-1)//factorial(n-j)
  for mon,c in polys[n-j].items():
   new=list(mon); new[j-1]+=1; out[tuple(new)]+=factor*c
 polys.append({k:v for k,v in out.items() if v})
def der(n):
 return sum((-1)**j*factorial(n)//factorial(j) for j in range(n+1))
def value(poly,seq):
 ps=[sum(x**j for x in seq) for j in range(1,MAX+1)]
 total=0
 for mon,c in poly.items():
  v=c
  for a,e in zip(ps,mon): v*=a**e
  total+=v
 return total
def direct(m,seq):
 es=[1]+[0]*m
 for x in seq:
  for k in range(m,0,-1): es[k]+=x*es[k-1]
 return factorial(m)*es[m]
rows=[]; seqs=[[],[0],[1],[-3,-1,0,2,5],[1]*3+[-1]*3,[1]*18,list(range(-8,9)),[Fraction(1,3),Fraction(-4,5),2,0]]
count=0
for m in range(2,MAX+1,2):
 rem={k:-v for k,v in polys[m].items()}; singleton=(m,)+(0,)*(MAX-1); rem[singleton]=rem.get(singleton,0)+1; rem={k:v for k,v in rem.items() if v}
 grouped=defaultdict(int)
 for mon,c in rem.items(): grouped[mon[0]]+=abs(c)
 target={m-j:comb(m,j)*der(j) for j in range(2,m+1)}
 assert dict(grouped)==target
 assert sum(grouped.values())==factorial(m)-1
 pair=[0]*MAX; pair[0]=m-2; pair[1]=1
 assert rem[tuple(pair)]==comb(m,2)
 A=factorial(m)-1; C=A*(2*A)**((m-2)//2)
 for seq in seqs:
  E=value(polys[m],seq); assert E==direct(m,seq)
  Z=sum(seq); V=sum(x*x for x in seq)
  assert abs(Z**m-E)<=Fraction(1,2)*abs(Z)**m+C*V**(m//2)
  assert E>=Fraction(1,2)*abs(Z)**m-C*V**(m//2)
  count+=1
 rows.append({'order':m,'monomials':len(rem),'derangement_coefficient_check':True,'total_coefficient_check':True,'one_pair_coefficient':comb(m,2)})
assert direct(6,[1]*3+[-1]*3)==-720
assert 1+(Fraction(12)-Fraction(136,13))/(4*12)==Fraction(161,156)
out={'status':'passed','evidence_level':'diagnostic_only','partition_checks':rows,'finite_sequence_absorption_cases':count,'negative_signed_control_order6':-720,'p12_growing_cutoff_head_exponent':'161/156','limitations':'Exact finite checks only, not a proof for arbitrary p, actual signed integral, or any asymptotic Gauss estimate.'}
Path(__file__).with_name('exact_local_controls.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
