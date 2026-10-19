"""Round235 bounded exact controls. Diagnostic only, never asymptotic proof."""
from fractions import Fraction as F
from math import isqrt, gcd
from itertools import permutations
from pathlib import Path
import json, hashlib

base=Path(__file__).resolve().parent
def chi(n): return (0,1,0,-1)[n%4]
def divisors(n): return [d for d in range(1,n+1) if n%d==0]
def r2(n): return sum(1 for a in range(-isqrt(n),isqrt(n)+1) for b in range(-isqrt(n),isqrt(n)+1) if a*a+b*b==n)
def hyper(n):
    return 4*sum(chi(d)+chi(n//d) for d in divisors(n) if d<=isqrt(n))-(4*chi(isqrt(n)) if isqrt(n)**2==n else 0)
gamma=F(13,125)
root_upper=(297+13762*F(129,1000))/50
checks={
 'sqrt_threshold_positive':root_upper>0,
 'beta_strictly_below_129_1000':root_upper**2>1717,
 'sixth_exponent':1-6*gamma+F(1,100)==F(193,500),
 'conditional_sharp':(F(29,25)+7)/26==F(102,325),
 'width_endpoints':(1-F(99,250),1-F(26,125))==(F(151,250),F(99,125)),
 'hyperbola_all_256':all(r2(n)==hyper(n) for n in range(1,257)),
 'missing_branch_negative_control':r2(3)==0 and 4*sum(chi(d) for d in divisors(3) if d<=isqrt(3))==4,
 'square_correction_nonzero_control':r2(9)==4 and 4*sum(chi(d)+chi(9//d) for d in divisors(9) if d<=3)==0,
 'character_fourier_residues':tuple(chi(n) for n in range(4))==(0,1,0,-1),
}
# Rational enclosure, no decimal arithmetic needed for the strict margin.
den=10**20; low=isqrt(1717*den*den); lo=F(low,den); hi=F(low+1,den)
assert lo*lo<=1717<hi*hi
beta_lo=(50*lo-297)/13762;beta_hi=(50*hi-297)/13762
margin_lo=F(387,500)-6*beta_hi;margin_hi=F(387,500)-6*beta_lo
checks['strict_positive_margin']=margin_lo>0

# Exact positive-frequency grouping, flat Fourier packet q=1 on [1,2].
# This finite coefficient check uses no claim of smoothness or asymptotics.
H=3;D=19; direct={};expected={}
def add(dst,frequency,real=F(0),imag=F(0)):
    old=dst.get(frequency,(F(0),F(0)));dst[frequency]=(old[0]+real,old[1]+imag)
def active(freq):return 1<=freq*H<=2
for d in range(1,D+1):
    for n in range(1,2*d//H+1):
        freq=F(n,d)
        if active(freq):add(direct,freq,imag=-F(H*chi(d),2*d))
    for k in range(1,8*d//H+1,2):
        freq=F(k,4*d)
        if active(freq):add(direct,freq,real=-F(H*chi(k),4*d))
for q in range(1,4*D+1):
    for a in range(1,2*q//H+1):
        freq=F(a,q)
        if gcd(a,q)!=1 or not active(freq):continue
        if q%2:
            c=sum((F(chi(g),g) for g in range(1,D//q+1)),F(0))
            add(expected,freq,imag=-F(H*chi(q),2*q)*c)
        elif q%4==0:
            c=sum((F(chi(g),g) for g in range(1,4*D//q+1)),F(0))
            add(expected,freq,real=-F(H*chi(a),q)*c)
direct={k:v for k,v in direct.items() if v!=(0,0)}
expected={k:v for k,v in expected.items() if v!=(0,0)}
checks['exact_grouping']=direct==expected
checks['grouped_frequency_count']=len(direct)==136
checks['no_denominator_2_mod_4']=all(q.denominator%4!=2 for q in direct)
checks['partial_chi_harmonic_bounded']=all(0<=sum((F(chi(g),g) for g in range(1,n+1)),F(0))<=1 for n in range(1,257))

# Newton identity for ordered distinct sixfold products; real signed examples.
def p6_formula(v):
    p={k:sum(x**k for x in v) for k in range(1,7)}
    return (p[1]**6-15*p[1]**4*p[2]+40*p[1]**3*p[3]+45*p[1]**2*p[2]**2-90*p[1]**2*p[4]-120*p[1]*p[2]*p[3]+144*p[1]*p[5]-15*p[2]**3+90*p[2]*p[4]+40*p[3]**2-120*p[6])
def product(v):
    z=1
    for x in v:z*=x
    return z
vectors=[[-2,-1,0,1,2,3],[1,-1,1,-1,1,-1,1],[0]*7,[1]*7,[F(1,2),F(-2,3),1,0,2,-1]]
checks['newton_distinct_six']=all(p6_formula(v)==sum(product(t) for t in permutations(v,6)) for v in vectors)
assert all(checks.values()),checks
result={'classification':'diagnostic_only','status':'passed','checks':checks,'exact_margin_interval':[str(margin_lo),str(margin_hi)],'decimal_margin_for_display':float((margin_lo+margin_hi)/2),'grouping_parameters':{'H':H,'D':D,'packet':'indicator of [1,2] for exact coefficient algebra only'},'bounded_hyperbola_range':[1,256],'signed_vectors':[[str(x) for x in v] for v in vectors],'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'limitations':'Finite identities and exponent arithmetic only. No control certifies the unproved actual signed S6 estimate.'}
(base/'exact_local_controls.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
