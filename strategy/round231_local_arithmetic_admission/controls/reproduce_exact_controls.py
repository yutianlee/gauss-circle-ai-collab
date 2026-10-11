"""Exact finite arithmetic controls, independently reproducing Wolfram output."""
from pathlib import Path
from fractions import Fraction as F
import json

def counts(q):
    out=[0]*q
    for x in range(q):
        for y in range(q):out[(x*x+y*y)%q]+=1
    return out
def conv(a,b):
    q=len(a); out=[0]*q
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[(i+j)%q]+=x*y
    return out
def power(a,n):
    out=[1]+[0]*(len(a)-1)
    while n:
        if n&1:out=conv(out,a)
        n//=2
        if n:a=conv(a,a)
    return out
def ram_p(p,t):return p-1 if t%p==0 else -1
def ram_p2(p,t):return p*(p-1) if t%(p*p)==0 else (-p if t%p==0 else 0)

rows=[]
for p in [3,5,7]:
    q=p*p;n=counts(q);chi=(-1)**((p-1)//2);c=1-F(chi,p)
    j=[q*(n[t] if t else 0)-(q*q-n[0]) for t in range(q)]
    assert sum(j)==0
    coeff=power(j,12)
    aa=c*(F(chi,p)-F(1+chi,p*p));bb=-c*F(1+chi,p*p)
    actual=[F(x,q**35) for x in coeff]
    expected=[aa**12*ram_p(p,t)+bb**12*ram_p2(p,t) for t in range(q)]
    assert actual==expected
    assert n[0]==(3*p*p-2*p if chi==1 else p*p)
    assert all(n[t]==p*p-chi*p for t in range(1,q) if t%p)
    assert all(n[t]==(2*p*(p-1) if chi==1 else 0) for t in range(p,q,p))
    rows.append(dict(p=p,norm_count_zero=n[0],norm_count_units=n[1],norm_count_valuation_one=n[p],A=str(aa),B=str(bb),twelfth_at_zero=str(actual[0]),all_residues_checked=q,passes=True))

n2=counts(8)
assert n2==[8,16,16,0,8,16,0,0]
lp=[F(n2[t],8) if t%4 else F(0) for t in range(8)]
mean=sum(lp)/8
assert mean==F(3,4)
kii=[int(4*(v-mean)) for v in lp]
k12=F(power(kii,12)[0],4**12*8**11)
k6=power(kii,6)
balanced=F(sum(v*v for v in k6),4**12*8**11)
assert k12==F(23511,16777216)
assert balanced==F(31255,16777216)
out=dict(status='passed',diagnostic_only=True,odd_prime_controls=rows,two_adic=dict(raw_counts=n2,squarefree_profile=[str(x) for x in lp],mean=str(mean),signed_twelfth_at_zero=str(k12),balanced_six_against_six=str(balanced),different_quantities=k12!=balanced),limitations='Finite exact controls do not certify any asymptotic theorem or transfer norm congruences to real root near-relations.')
Path(__file__).with_name('local_exact_controls.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
