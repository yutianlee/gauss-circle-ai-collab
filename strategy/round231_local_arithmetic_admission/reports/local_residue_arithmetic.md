# Local residue arithmetic: exact formulas and the physical-frequency remainder

## 1. Result and scope

Task: `local_residue_arithmetic`. Role: bounded arithmetic derivation, claimant. Generated: 2026-10-11 UTC. This is Round231 prelaunch admission work; Round230 remains closed. Frozen graph SHA256: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

**Result.** The actual coefficients have the exact local densities, additive Fourier coefficients, prime-power formulas, and uniform lattice remainder proved below. For odd modulus q, the normalized additive coefficient with reduced conductor m is exactly chi_4(m)/m. All phi(m) primitive numerators at conductor m must be restored. Their total absolute coefficient mass is phi(m)/m, and completion over all conductors costs

    sum_(m|q) phi(m)/m = product_(p^k||q) [1+k(1-1/p)],

including a zero mode of size one. A small individual Fourier coefficient does not supply a surviving 1/q saving.

For a smooth physical wave shell n~N, R~T, partial summation pays the variation factor 1+R sqrt(N). At N~T this is T^(3/2). Summing the continuous residue main terms gives exactly the ordinary area mean, which is rapidly oscillatory on each smooth shell. The remaining signed integral is the actual circle discrepancy again. The elementary global bound gives a shell error O(T^(5/4)), before capping it by the stronger trivial shell bound O(T^(1/4)). Summing individual residue errors is worse, by explicit q-dependent costs below.

**Admission conclusion: no new complete estimate.** These exact formulas and their proved elementary errors do not improve the accepted complete twelfth moment. This is a limitation of the stated formula-plus-remainder argument, not a no-go theorem for every use of local arithmetic and not an arithmetic counterexample to the target. The first missing signed remainder inequality is stated in Section 4. No scalar Hecke amplifier is used.

## 2. Exact statements and hypotheses

Write e(t)=exp(2 pi i t). For integers q>=1 and a modulo q define

    nu_q(a) = #{(u,v) in (Z/qZ)^2 : u^2+v^2 = a mod q},
    delta_q(a) = nu_q(a)/q^2,
    D_q(h) = sum_(a mod q) delta_q(a)e(ha/q).

Thus sum_a nu_q(a)=q^2, sum_a delta_q(a)=1, and D_q(0)=1. For real X>=0 set

    A_q(a;X) = sum_(1<=n<=X, n=a mod q) r_2(n),
    E_q(a;X) = A_q(a;X)-pi delta_q(a)X.

The origin is excluded from A_q. In particular the lattice-disk expression for A_q subtracts 1 when a=0; no extra r_2(0) term belongs to the wave.

**Odd-modulus Fourier and density formulas.** If q is odd, h is any residue, d=gcd(h,q), m=q/d, and m=1 when h=0, then

    D_q(h) = chi_4(m)/m,
    delta_q(a) = (1/q) sum_(m|q) [chi_4(m)/m] c_m(a),
    nu_q(a) = q sum_(m|q) [chi_4(m)/m] c_m(a),               (2.1)

where c_m(a)=sum_(u mod m, gcd(u,m)=1)e(ua/m) is the Ramanujan sum. The sign in the Fourier inversion is immaterial for c_m(a), which is real and even. Equivalently, for h=p^t u modulo p^k, t<k and p not dividing u,

    D_(p^k)(h) = chi_4(p)^(k-t) p^(-(k-t)).                 (2.2)

The conductor is p^(k-t), not p^k. This distinction includes every imprimitive mode.

**Odd prime powers.** Let v=min(v_p(a),k), taking v=k for a=0 modulo p^k.

* If p=1 mod 4 and v<k, then nu_(p^k)(a)=(v+1)(p-1)p^(k-1).
* If p=1 mod 4 and v=k, then nu_(p^k)(0)=p^(k-1)[p+k(p-1)].
* If p=3 mod 4 and v<k is odd, then nu_(p^k)(a)=0.
* If p=3 mod 4 and v<k is even, then nu_(p^k)(a)=(p+1)p^(k-1).
* If p=3 mod 4 and v=k, then nu_(p^k)(0)=p^(2 floor(k/2)).

For coprime q_1,q_2, nu_(q_1 q_2)(a)=nu_(q_1)(a)nu_(q_2)(a), with the arguments reduced to the respective factors. The same multiplicativity holds for delta. In particular the zero-norm density is not a generic nonzero density, and a locally forbidden residue has A_q=E_q=0 exactly.

One convenient uniform envelope for odd q is

    nu_q(a) <= q H(q),
    H(q) = product_(p^k||q, p=1 mod4)[1+k(1-1/p)]
           product_(p^k||q, p=3 mod4)[1+1/p] <= tau(q).     (2.3)

**The prime 2.** Modulo 2, nu_2(0)=nu_2(1)=2 and D_2(1)=0. The odd-modulus formula must not be extended by treating 2 as an inert or split odd prime. For completeness, for k>=1:

    nu_(2^k)(0)=2^k.

If a is nonzero modulo 2^k, write a=2^v b with b odd and 0<=v<k. Then

    nu_(2^k)(a) = 2^k,       if k-v=1;
                   2^(k+1), if k-v>=2 and b=1 mod4;
                   0,       if k-v>=2 and b=3 mod4.        (2.4)

For h=2^t u with u odd and reduced conductor 2^ell, ell=k-t, its Fourier coefficient is 0 when ell=1 and 2^(1-ell)i^u when ell>=2; D(0)=1. Thus even-modulus coefficients need not be real. More generally, if h/q reduces to u/m with gcd(u,m)=1, its normalized Gauss-square coefficient is

    chi_4(m)/m       if m is odd;
    0               if m=2 mod4;
    2 i^u/m         if 4 divides m.                       (2.5)

Here u is taken modulo m, so i^u is well-defined in the last case. These statements and CRT specify all even moduli, although the proposed local admission route uses odd q.

**Uniform elementary counting error.** With an absolute implicit constant, for every q,a and real X>=0,

    |E_q(a;X)| <= C nu_q(a)(sqrt(X)/q+1).                 (2.6)

For odd q this is at most C H(q)(sqrt(X)+q). It remains valid for zero-norm residues, real endpoints, and moduli larger than sqrt(X). If nu_q(a)=0 the error is zero. For q=1 it gives the standard elementary discrepancy bound O(sqrt(X)+1).

**Physical shell.** Take a fixed smooth eta supported in a compact subinterval of (0,infinity), with x~N on its rescaling, N>=1, T>=2, R in [T/2,2T], and sign sigma in {+1,-1}. Let

    F(x)=x^(-3/4) Psi(sqrt(x/T)) eta(x/N)e(sigma R sqrt(x)),
    S_(N,q,a)(R)=sum_(n=a modq) r_2(n)F(n).

Put u=sqrt(N/T), and let K_j(u) be the supremum on the fixed interval s~u of sum_(0<=ell<=j)|s^ell Psi^(ell)(s)|, with harmless enlargement to cover eta. Since Psi is fixed Schwartz,

    K_j(u) <<_(j,A) (1+u)^(-A) for every fixed A>=0.

The elementary weighted conclusion is

    S_(N,q,a)(R) = pi delta_q(a) integral F(x) dx + R_(N,q,a)(R),

    |R_(N,q,a)(R)|
      <= C_eta nu_q(a)(sqrt(N)/q+1) N^(-3/4)
                     [K_1(u)+R sqrt(N)K_0(u)].           (2.7)

All constants depend only on the fixed smooth functions and displayed derivative orders, not on q,a,N,T,R. The real cosine shell is the real part of e(-3/8) times the sigma=+1 shell. Both signs in a cosine expansion therefore have the same cost.

## 3. Proof, completion, and restored costs

**Gauss-square derivation.** Let G(h,q)=sum_(x modq)e(hx^2/q). Directly from the definitions,

    D_q(h)=q^(-2)G(h,q)^2.

If d=gcd(h,q), m=q/d and u=h/d, then G(h,q)=dG(u,m). Thus only the reduced conductor enters. For an odd prime p and p not dividing u, the elementary quadratic Gauss identity gives

    G(u,p)^2=chi_4(p)p.

Only its square is needed: write G(u,p)=sum_t (t|p)e(ut/p), change variables to get G(u,p)=(u|p)G(1,p), and note conjugation multiplies this character sum by (-1|p). The direct orthogonality calculation of its absolute square is p, proving the displayed square without choosing a square-root sign. For k>=2, splitting a residue modulo p^k as y+p^(k-1)z and summing z first gives G(u,p^k)=pG(u,p^(k-2)). Consequently G(u,p^k)^2=chi_4(p)^k p^k. CRT, with the inverse factors in the additive characters, gives the same squared identity chi_4(m)m for every odd m. Dividing by m^2 proves (2.1)-(2.2), including m=1. Fourier inversion grouped by reduced conductor gives the Ramanujan expression.

**Local counting derivation.** For split p choose i modulo p^k with i^2=-1, lifting a root modulo p by the elementary nonzero derivative argument. The invertible map (x,y) to (x+iy,x-iy) changes the equation to uv=a. If v_p(a)=v<k, each possible valuation j=0,...,v of the first coordinate contributes (p-1)p^(k-1) solutions: there are (p-1)p^(k-j-1) choices for it and p^j choices for the other coordinate. If a=0, the valuations j=0,...,k-1 contribute k(p-1)p^(k-1), and the zero first coordinate contributes p^k. This proves the split cases.

For inert p, a primitive pair cannot have norm zero modulo p, since -1 is not a square. Thus, below modulus p^k, a nonzero norm has valuation twice the common valuation of its coordinates. Odd valuation is impossible. At unit norm, (2.1) at p gives p+1 solutions modulo p. At least one coordinate derivative 2x or 2y is a unit, so each solution has exactly p lifts to any specified next digit of the norm. Hence there are (p+1)p^(ell-1) solutions to a unit norm modulo p^ell. For valuation 2s<k, divide both coordinates by p^s and count their p^s independent extra digits each: the result is p^(2s)(p+1)p^(k-2s-1)=(p+1)p^(k-1). Norm zero means both coordinates are divisible by p^ceil(k/2), which gives p^(2 floor(k/2)) pairs. CRT and (2.3) follow.

For 2^k, the assertions at k=1,2 follow by inspection. An odd represented norm is 1 modulo 4. For k>=3 and a=1 mod4, exactly 2^(k-2) choices of the even coordinate make a minus its square equal to 1 modulo 8; each such odd number has exactly four square roots modulo 2^k. This root count follows by the elementary lifting induction from modulus 8, pairing roots separated by 2^(k-1) when lifting one further bit. Choosing which coordinate is odd gives 2^(k+1) representations. If 4 divides the norm, both coordinates are even, giving the recurrence nu_(2^k)(4b)=4nu_(2^(k-2))(b). If the norm is 2b with b odd, the map (u,v) to (u+v,u-v), whose kernel modulo 2^k has size two, gives nu_(2^k)(2b)=2nu_(2^(k-1))(b). These recurrences include the zero-norm formula and prove (2.4).

For the 2-power Fourier formula, G(u,2)=0, G(u,4)=2(1+i^u), and G(u,8)=4e(u/8) for odd u. Splitting into four classes shows G(u,2^ell)=2G(u,2^(ell-2)) for ell>=4. Its square is therefore 2^(ell+1)i^u for every ell>=2. After division by 2^(2ell) this gives the stated coefficients. If m=2^ell s with s odd, CRT multiplies the 2-power coefficient evaluated at u s^(-1) by the odd coefficient evaluated at u (2^ell)^(-1). For ell>=2 the identity chi_4(s)i^(u s^(-1))=i^u reduces this to 2i^u/m. For ell=1 it vanishes. This proves (2.5).

**Lattice remainder.** A residue pair (u,v) determines a translated lattice qZ^2+(u,v). Tile the plane by its centered q-by-q cells. If r=sqrt(X), the difference between the disk and the union of cells whose centers are in the disk lies in an annulus of thickness at most q/sqrt(2), with the inner radius replaced by zero if necessary. Its area is O(qr+q^2). Each cell has area q^2, so this one lattice contributes pi X/q^2+O(r/q+1). Sum over the nu_q(a) allowed pairs and subtract the origin when a=0. That subtraction is absorbed because nu_q(0)>=1. This proves (2.6) with no coprimality, X/q, or endpoint assumption.

For odd q<=sqrt(X), (2.6) is O(H(q)sqrt(X)) per residue. For q>sqrt(X), its O(H(q)q) component must be retained. In particular one cannot extrapolate a small-modulus asymptotic to arbitrary moduli by omitting this term.

**Weighted partial summation.** Stieltjes integration, with F zero at the shell endpoints, gives the exact identity

    R_(N,q,a)(R) = - integral E_q(a;x) F'(x) dx.           (3.1)

The nonoscillatory amplitude has supremum O(N^(-3/4)K_0) and integral of its derivative O(N^(-3/4)K_1). The phase derivative is pi i sigma R/sqrt(x). Therefore

    integral |F'(x)|dx
      <= C N^(-3/4)[K_1+R sqrt(N)K_0],

which proves (2.7). A partial shell adds endpoint terms bounded by the same expression. Parametrizing one progression as x=a+qj does not reduce the oscillatory cost: the phase derivative with respect to j is sigma Rq/(2sqrt(x)), over O(N/q) steps. Its total variation is still O(Rsqrt(N)). In particular this derivative is not an O(1) test-function norm at physical frequency.

For odd q, the per-residue estimate can be written

    |R_(N,q,a)| <= C H(q)(sqrt(N)+q)N^(-3/4)
                             [K_1+R sqrt(N)K_0].         (3.2)

At N~T and R~T it is O(H(q)[T^(5/4)+qT^(3/4)]). There is no useful individual-residue oscillatory error saving here.

**Summing residues and all q costs.** Since sum_a nu_q(a)=q^2, summing (2.7) by the triangle inequality gives

    sum_a |R_(N,q,a)|
      <= C (q sqrt(N)+q^2)N^(-3/4)
                         [K_1+R sqrt(N)K_0].             (3.3)

At N~T this is O(qT^(5/4)+q^2T^(3/4)). No factor H(q) is needed in this sharper total because the exact sum of nu_q is known. On the other hand the exact signed sum satisfies

    sum_a E_q(a;x) = A_1(0;x)-pi x,
    sum_a pi delta_q(a) integral F = pi integral F.        (3.4)

Thus using the global disk error before taking absolute values improves (3.3) to

    |sum_a R_(N,q,a)|
      <= C (sqrt(N)+1)N^(-3/4)
                         [K_1+R sqrt(N)K_0],             (3.5)

independent of q. At N~T this is O(T^(5/4)). The direct coefficient-mass bound is stronger:

    |sum_a S_(N,q,a)| <= C N^(1/4)K_0(sqrt(N/T)),         (3.6)

since the number of lattice points with norm O(N) is O(N). At N~T this is O(T^(1/4)). The local formulas do not improve (3.6) by combining them with (2.6).

The continuous main term is small for a different, fully paid reason. Substituting x=Nv^2 gives

    integral F(x)dx
      = 2N^(1/4) integral v^(-1/2)Psi(u v)eta(v^2)
                                  e(sigma R sqrt(N)v)dv,

so ordinary repeated integration by parts yields, for every fixed J,

    |integral F(x)dx|
      <= C_J N^(1/4)K_J(u)(1+R sqrt(N))^(-J).             (3.7)

All derivatives of Psi, including its dependence on N/T, are in K_J. This small main term leaves the arithmetic remainder as the whole substantive problem.

**Fourier numerator completion.** There are exactly phi(m) h modulo q with reduced conductor m. Consequently

    sum_(h modq)|D_q(h)|
      = sum_(m|q)phi(m)/m
      = product_(p^k||q)[1+k(1-1/p)] <= tau(q),            (3.8)

and

    sum_(h modq)|D_q(h)|^2
      = product_(p^k||q)[1+1/p-p^(-k-1)].                 (3.9)

These are exact for odd q. In particular the q-level primitive modes have total absolute mass phi(q)/q, not 1/q; the h=0 mode has mass one. A proposed uniform bound for one additive mode, when used termwise for a density expansion, must multiply by (3.8), or prove actual cancellation between its phi(m) numerators. Cauchy-Schwarz similarly has to pay the norm of the companion mode family, not just (3.9).

For example, define the periodic local model L_q(n)=pi nu_q(n)/q. Its exact finite Fourier expansion is

    L_q(n) = pi sum_(h modq)D_q(h)e(-hn/q)
           = pi sum_(m|q)[chi_4(m)/m]c_m(n).              (3.10)

It is a nonnegative, q-periodic sequence of mean pi, not the exact coefficient r_2(n). For real X,

    sum_(1<=n<=X)L_q(n) = pi X+O(q),

because each residue count differs from X/q by at most one and sum_a nu_q(a)=q^2. Hence the proved cumulative remainder for r_2-L_q is only O(sqrt(X)+q), using the elementary disk error. Partial summation costs

    O((sqrt(N)+q)N^(-3/4)[K_1+R sqrt(N)K_0]),             (3.11)

or O(T^(5/4)+qT^(3/4)) on N~T. Retaining the signed Fourier main terms of this different discrete model therefore does not eliminate the missing arithmetic remainder. Formula (3.10) alone is not an approximation theorem at frequency R~T.

**Whole wave and tails.** A smooth dyadic partition for all n>=1, with bounded overlap and a separately smooth initial piece, has N>=1. The bound (3.6), together with the Schwartz bounds, gives total absolute size O(T^(1/4)). For any fixed delta>0, all shells N>=T^(1+delta) contribute O(T^(-A)) for any prescribed A after choosing a sufficiently strong fixed Schwartz seminorm. The main terms (3.7), summed over all shells, are O(T^(-A)) as well. This pays the infinite far tail but does not bound the complete middle range better than the accepted estimate. Using the trivial bound over an R-window of length O(T) gives at best M_12(B_T)<<T^4. The newly proved local remainder estimate is weaker, not an improvement over the accepted T^(10 beta+epsilon), where 10 beta=1.28966351948... . Neither the target 29/25 nor the strict pointwise-gain gate 13 beta-1/2 is reached.

## 4. First unproved step and exact missing inequality

There is no doubtful algebraic step in Sections 2-3. The first unsupported step in a gain claim would be replacing (3.1) by a quantitatively stronger estimate for the signed oscillatory remainder, or treating (3.10) as the actual arithmetic coefficients without paying (3.11).

To state the missing complete bound exactly, fix a smooth dyadic partition eta_j covering every integer n>=1, including its initial piece, and put

    F_j(x;R)=x^(-3/4)Psi(sqrt(x/T))eta_j(x)e(Rsqrt(x)),
    U_j(R)=-sum_(a mod q_j) integral E_(q_j)(a;x)F_j'(x;R)dx,

where each q_j is any chosen positive odd modulus and the initial support stays away from x=0. The full real remainder is

    U_T(R)=Re[e(-3/8) sum_j U_j(R)].

Equations (3.1), (3.4), and (3.7) give the exact complete identity

    B_T(R)=U_T(R)+O_A(T^(-A)), uniformly R in [T/2,2T].

Thus an actual sufficient missing inequality, with all signs, blocks and mixed terms retained, is

    (integral w(R/T)|U_T(R)|^12 dR)^(1/12)
        <<_epsilon T^(29/300+epsilon).                   (4.1)

As usual epsilon may be rescaled when taking a twelfth root. This is equivalently the original complete target up to a negligible error, not a newly proved estimate or a new admission input. In particular the sum of E_q in this expression is identically the global discrepancy, so merely introducing q_j does not change it.

A stronger, also unproved sufficient route would bound the L^12 norms of the actual real U_j separately at the target scale with a summable shell envelope (or uniformly on the O(log T) retained shells, absorbing their number into T^epsilon), and pay the tail as above. Such a route would explicitly pay all mixed blocks by the norm triangle inequality. No such shell bound has been derived here.

To illustrate the loss in the proved variation argument without asserting necessity: a uniform bound |U_T|<<T^(1/75+epsilon) would suffice for (4.1). On just N~T, obtaining that from an unmodulated discrepancy supremum and the same variation inequality would require a bound of order T^(-221/300+epsilon) for that supremum. The actual cumulative discrepancy has nonzero integer jumps and cannot have such a vanishing supremum. The conclusion is only that this sufficient supremum-plus-total-variation route cannot close the target; it does not obstruct cancellation inside the signed integral or its moment.

This report has not imported the prior cross-label microscopic discrepancy hypothesis as a proved fact, has not claimed that a density identity supplies microscopic cancellation, and has not converted an absolute bound into a signed bound.

## 5. Required controls and outcomes

All controls are `diagnostic_only`; the general formulas are justified by the proofs above. Analytical/algebraic work exceeded 95% of this task; the only numerical work was one bounded exact enumeration, with no asymptotic simulation or floating-point inference.

**Exact enumeration.** Command: the following Python source was supplied through a PowerShell single-quoted here-string to `python -` in the repository directory. It compared every residue against the prime-power/CRT formula, compared the odd-modulus Ramanujan formula using exact rational arithmetic, checked total mass, and checked the completed Fourier L1 product. The source is archived here, the only assigned writable artifact.

```python
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
```

Outcome: PASS for 753 residue cases across the 25 displayed moduli. Exit code 0. This includes split/inert primes, square and higher prime powers, composites, zero residues, every residue at q=2 through 64, and mixed even moduli. The conductor independently communicated the same odd-modulus formula and its successful control for the 13 listed odd moduli; this communication is disclosed, and the calculation was independently rerun and extended locally rather than accepted as proof.

**Hand controls and their mathematical outcomes.**

* At odd p, nu_p(0)=p+chi_4(p)(p-1), while nu_p(a)=p-chi_4(p) for a nonzero. Thus nu_3(0)=1, nu_3(1)=4, nu_5(0)=9 and nu_5(1)=4. Treating all residues as equally dense would fail immediately.
* At p=3, k=2, nu_9(3)=0 and nu_9(0)=9, while the primitive conductor-9 Fourier coefficient is +1/9. Assigning the inert sign -1 at every power would fail.
* Modulo 4 the density numerators are (4,8,4,0); D_4(1)=i/2 and D_4(2)=0. This checks both the exceptional conductor 2 and the complex conductor 4 coefficient.
* For every q, summing the density numerator gives q^2 and summing the continuous main terms gives pi integral F. The q=1 specialization is exactly the elementary disk discrepancy. Thus the local formula cannot manufacture a new zero-mode cancellation.
* The lattice proof keeps O(1) for each residue pair and therefore handles X=0, boundary lattice points and q>sqrt(X). The finite computation is not used to certify this uniformity.
* The wave proof retains both derivatives of Psi and the factor R sqrt(N). With N=T and R=T its dominant term is T^(5/4), not T^(-1/4). This dimensional control is analytic, not fitted numerically.
* All coefficients and residues in the derivation are the actual r_2 ones. No adversarial coefficient model was substituted for r_2, and no unsigned obstruction is asserted for the real signed moment.

## 6. Dependencies, exact provenance, and isolation

Files read, with SHA256 at the time of writing:

| Context file | SHA256 |
| --- | --- |
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/active_campaign.yml` | `fd65ce5c6b117aa4ca8ed097f85e2c786621c8054ca81791aa6e5e17006a82fa` |
| `state/proof_obligations.yml` | `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b` |
| `strategy/round231_local_arithmetic_admission/briefs/local_residue_arithmetic.md` | `088a2eda8d89837ac758e8987adadd1e0ddccc4f511260be04fa762589dfeb11` |
| `strategy/round231_local_arithmetic_admission/briefs/complete_target.md` | `4cd95ec7203420e99e51a4dbf3e0de5c3732fe1e589ed9e3344bb0b96b1fd8d6` |
| `strategy/round231_cross_label_admission/briefs/complete_target.md` | `8ee37ee007ff58b8cda6db3d33205c0896639099a44be159ff930a7e86b19809` |

The graph was searched selectively for the two named obligations `GC-complete-square-root-large-values-moment-bound` and `GC-complete-distinct-radical-twelfth-reduction`. The search output incidentally included neighboring lines of the distinct-radical absolute-certificate node because it cites the latter ID; that neighboring material was not used as a dependency. A filename-only search located the two authorized complete-target files. No sibling report, blind statement, old admission report, legacy round, proof kernel, or external source was read. The conductor's one control communication is disclosed in Section 5. No external theorem is needed for the local derivation.

Mathematical dependencies of the new statements are finite Fourier inversion and orthogonality, CRT, elementary quadratic character/Gauss-square algebra, elementary lifting, disk cell geometry, partial summation, and integration by parts. The complete-wave comparison uses only the frozen target packet and the two named accepted graph statements; no stronger moment estimate or attribution is imported. The fixed mollifier supplies real even Schwartz Psi and its fixed seminorms. The pointwise and full-goal conditions are used only to state what this report does not achieve.

Only this assigned report was written. No graph, proof draft, validation matrix, synthesis, campaign file, sibling report, or legacy evidence was edited. The report's final SHA256 is supplied in the completion message rather than embedded self-referentially.

## 7. Recommended state effect and stop

**No change** to either target obligation, to the complete moment frontier, or to any pointwise claim. Retain this report as exact elementary local arithmetic evidence and a cost audit. The density formulas may be useful infrastructure, but they have not passed the admission gate for a new complete signed estimate.

The new bounded result identifies the missing work precisely: prove a strictly stronger oscillatory arithmetic remainder estimate with all numerator completion, q-dependence, physical derivatives, mixed blocks, and tails paid. The present identities reduce the sum of continuous residue main terms to the known area mean and leave (4.1) unproved. No successor round is designed or launched. Assigned task complete; stop after the report hash.
