"""Bounded exact diagnostics only; not an asymptotic proof."""
from itertools import combinations
from fractions import Fraction
from pathlib import Path
import json, math

base=Path(__file__).resolve().parent
def chi4(n): return 0 if n%2==0 else (1 if n%4==1 else -1)
def r2(n):
    return 4*sum(chi4(d) for d in range(1,math.isqrt(n)+1) if n%d==0 for d in ([d] if d*d==n else [d,n//d]))
primes=[2,3,5,7,13]
failures=[]
for p in primes:
    for n in range(1,257):
        lhs=r2(p*n)+chi4(p)*(r2(n//p) if n%p==0 else 0)
        rhs=(1+chi4(p))*r2(n)
        if lhs!=rhs:failures.append([p,n,lhs,rhs])
    if p%4==3:
        assert all(r2(p*p*n)==r2(n) for n in range(1,257))
assert not failures
sets=[list(s) for s in combinations(range(1,13),6) if sum(x*x for x in s)==325]
assert sets==[[1,3,7,8,9,11],[2,4,5,6,10,12]]
s=set(sets[0]); complement=set(range(1,13))-s
delta={k:sum(j**k for j in s)-sum(j**k for j in complement) for k in [0,2,4,6]}
c4=-Fraction(delta[4],8);c6=Fraction(delta[6],16)
assert (c4,c6)==(Fraction(1287,2),-Fraction(342225,4))
assert sum([1]*6+[-1]*6)==0
minors=sorted({a*d-b*c for a in [-1,1] for b in [-1,1] for c in [-1,1] for d in [-1,1]})
assert minors==[-2,0,2]
out=dict(diagnostic_only=True,command='python strategy/round231_admission/controls/reproduce_exact_controls.py',precision='exact Python integers and fractions; no floating point',scope='Finite local coefficient recurrences, balanced-sign phase, 2x2 sign minors and independent Wolfram reproduction; no asymptotic certification.',recurrences=dict(primes=primes,n_range=[1,256],tested=len(primes)*256,failures=failures,inert_square_dilation='pass'),balanced_signs=math.comb(12,6),equal_square_sets=sets,even_power_differences=delta,taylor_coefficients={'z4':str(c4),'z6':str(c6)},sign_matrix_minors=minors,wolfram_reproduction='pass',limitations='The illustrative n_j=m^2+j^2 Taylor identity is not used to claim any squarefree density or asymptotic lower bound. All asymptotic certificate arguments are analytical.')
(base/'local_exact_controls.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
