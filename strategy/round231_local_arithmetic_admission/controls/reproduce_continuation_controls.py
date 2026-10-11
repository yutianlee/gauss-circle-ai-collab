"""Bounded exact controls. No asymptotic estimation or simulation."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
import json

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def mobius(n):
    out=1; p=2
    while p*p<=n:
        if n%p==0:
            n//=p; out=-out
            if n%p==0:return 0
        p+=1
    return -out if n>1 else out

def ramanujan(d,b):
    return sum(k*mobius(d//k) for k in divisors(gcd(d,b)))

rows=[]
for q in [1,3,5,7,9,15,25,27,45,49,63,81,105]:
    counts=[0]*q
    for x in range(q):
        for y in range(q):counts[(x*x+y*y)%q]+=1
    for b,n in enumerate(counts):
        expect=q*sum((F(1 if d%4==1 else -1,d)*ramanujan(d,b) for d in divisors(q)),F(0))
        assert expect==n,(q,b,n,expect)
    assert sum(counts)==q*q
    rows.append({'q':q,'all_residue_counts_match':True,'zero_norm_count':counts[0]})

# Independently recheck the finite actual-support control found in inherited evidence.
A=[11,22,33,55,110,165,36,18,12,180,90,60]
m=1000; T=36*((180*m)**2+1)
assert sum(A[:6])==sum(A[6:])
assert sum((F(1,a) for a in A[:6]),F(0))==sum((F(1,a) for a in A[6:]),F(0))
bound=F(T,8*m**3)*sum((F(1,a**3) for a in A),F(0))
assert bound==F(643431600019859,2662000000000000)<1
norms=[(a*m)**2+1 for a in A]
signed_norm=sum(norms[:6])-sum(norms[6:]);assert signed_norm%3==1
def factor(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p=3 if p==2 else p+2
    if n>1:out[n]=out.get(n,0)+1
    return out
facts=[factor(n) for n in norms]
assert all(all(e==1 for e in f.values()) for f in facts)
assert 67102**5<=T*T<67103**5
assert len(set(norms))==12 and min(norms)>67102
assert max(norms)*36==T
out={'status':'passed','diagnostic_only':True,'method':'exact integer and rational arithmetic; exhaustive finite norm counts and trial division','odd_modulus_controls':rows,'inherited_actual_support_control':{'T':T,'Q':67102,'T_times_root_difference_upper_bound':str(bound),'signed_norm_sum':signed_norm,'mod3':signed_norm%3,'all_distinct_squarefree':True,'norms':norms,'prime_factorizations':facts},'limitations':'No asymptotic theorem is certified. The finite tuple only falsifies the proposed implication from a real near-root relation to an additive norm congruence.'}
Path(__file__).with_name('continuation_exact_controls.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('PASS:',len(rows),'complete odd-modulus tables and the inherited 12-label finite control. Diagnostic only.')
