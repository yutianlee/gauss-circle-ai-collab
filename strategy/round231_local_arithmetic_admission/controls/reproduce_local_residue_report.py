from fractions import Fraction
from math import gcd,isqrt

def fac(n):
    out=[]
    p=2
    while p*p<=n:
        k=0
        while n%p==0: n//=p; k+=1
        if k: out.append((p,k))
        p+=1
    if n>1: out.append((n,1))
    return out

def divs(n): return [d for d in range(1,n+1) if n%d==0]
def mu(n):
    fs=fac(n)
    return 0 if any(k>1 for p,k in fs) else (-1)**len(fs)
def chi(n): return 1 if n%4==1 else -1

def local(p,k,a):
    q=p**k
    a%=q
    if a==0:
        if p==2: return q
        if p%4==1: return p**(k-1)*(p+k*(p-1))
        return p**(2*(k//2))
    v=0
    while a%p==0: a//=p; v+=1
    if p==2:
        if k-v==1: return q
        return 2*q if a%4==1 else 0
    if p%4==1: return (v+1)*(p-1)*p**(k-1)
    return (p+1)*p**(k-1) if v%2==0 else 0

odd=[1,3,5,7,9,15,25,27,45,49,63,81,105]
qs=odd+[2,4,8,16,32,64,12,20,24,36,40,60]
residues=0
for q in qs:
    counts=[0]*q
    for x in range(q):
        for y in range(q): counts[(x*x+y*y)%q]+=1
    assert sum(counts)==q*q
    for a in range(q):
        pred=1
        for p,k in fac(q): pred*=local(p,k,a)
        assert pred==counts[a],(q,a,pred,counts[a])
        if q%2:
            rhs=Fraction(0)
            for m in divs(q):
                ram=sum(d*mu(m//d) for d in divs(gcd(m,a)))
                rhs+=Fraction(q*chi(m)*ram,m)
            assert rhs==counts[a],(q,a,rhs,counts[a])
        residues+=1
    if q%2:
        lhs=sum(Fraction(sum(gcd(u,m)==1 for u in range(m)),m)
                for m in divs(q))
        rhs=Fraction(1)
        for p,k in fac(q): rhs*=1+k*Fraction(p-1,p)
        assert lhs==rhs,(q,lhs,rhs)
print('PASS exact residue formulas, CRT, zero-mode total, odd Ramanujan inversion and odd Fourier L1 product')
print('moduli=',qs)
print('residue_cases=',residues)
print('No floating-point computation; diagnostic_only.')
