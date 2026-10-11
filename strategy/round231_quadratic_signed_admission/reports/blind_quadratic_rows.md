# Round231: blind finite quadratic-transform report

- Campaign/task: round231_quadratic_signed_admission / blind_quadratic_rows.
- Role/status: statement-only independent analyst; finite algebra, with diagnostic-only checks.
- Generated: 2026-10-11.
- Starting graph identifier (provenance only; graph not read): a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
- Exact context: protocol.md; strategy/round231_quadratic_signed_admission/briefs/blind_quadratic_statement.md; coordinator's bounded task message.
- Scope: all odd primes, complete finite-field sums, and the specified finite matrices. No circle-discrepancy or incomplete-sum assertion.

## 1. Result: exact finite lemma and raw-row no-go

Put s = chi_p(-1). The centered arithmetic function is exactly

    f_p(n) = s (1_{n=0} - 1/p).

Define the normalized complete quadratic sum

    A_a(b) = (1/p) sum_n e_p(a n^2 + b n).

Then, for every a,b in F_p,

    Q_(a,b) = (1-s/p) A_a(b) + s/p,
    W_(a,b) = (s/p) (1-A_a(b)).

The complete centered arithmetic rows W_a are not orthogonal and do not become decorrelated as p grows. Their normalized pairwise inner products tend uniformly to 1. Almost all their energy is in a common constant row component. There are two useful, different decompositions:

1. W = C + R with C_a(b)=s/p and R_a(b)=-(s/p)A_a(b). The residual rows R have normalized off-diagonal inner-product magnitude exactly p^(-1/2), but C is not orthogonal to R.
2. W = D + H with D_a(b)=kappa=s(p-1)/p^2 and H_a(b)=-(s/p)(A_a(b)-1/p). Here D is orthogonal to each H row, is the row average across a, and is exactly the n=0 contribution to W. D accounts for the fraction (p-1)/p of every W row's energy. The H rows have normalized off-diagonal inner products O(p^(-1/2)).

Deleting either common term changes the matrix. Its contribution to any subsequent weighted sum must be given a separate zero-residue/common-mean owner, or proved to vanish under the actual weights. Residual decorrelation is not a bound for the original weighted matrix expression without this owner.

## 2. Exact statements and hypotheses

Throughout, p is an arbitrary odd prime, chi=chi_p is the quadratic character on F_p with chi(0)=0, s=chi(-1), and

    epsilon_p = 1 when p=1 (mod 4), and i when p=3 (mod 4).

Square roots of positive real numbers mean their positive square roots. All a,b,c,n and divisions inside e_p are in F_p; 1/(4a) is used only when a is nonzero. The row inner product convention is

    <X_a,X_c> = sum_b X_a(b) conjugate(X_c(b)).

The exact arithmetic count and quadratic transform are

    nu_p(n) = p-s+p s 1_{n=0},

    A_0(0)=1,
    A_0(b)=0                         (b != 0),
    A_a(b)=epsilon_p chi(a)/sqrt(p)
           * e_p(-b^2/(4a))          (a != 0).

Consequently,

    Q_(0,0)=1,              W_(0,0)=0,
    Q_(0,b)=s/p,            W_(0,b)=s/p          (b != 0),

and for a != 0 the formulas in Section 1 together with the displayed A_a(b) are the complete evaluations. In particular, for p=1 (mod 4), Q=(1-1/p)A+1/p and W=(1-A)/p. For p=3 (mod 4), Q=(1+1/p)A-1/p and W=-(1-A)/p.

Write g(d)=A_d(0). Thus g(0)=1 and, for d != 0,

    g(d)=epsilon_p chi(d)/sqrt(p).

The full raw Gram matrix is

    <W_a,W_c> = [p-2+g(a-c)]/p^2.

Every raw row has energy

    E_W = (p-1)/p^2.

For a != c its normalized inner product is

    rho_W(a,c) = [p-2+epsilon_p chi(a-c)/sqrt(p)]/(p-1),

and hence

    |rho_W(a,c)-1| <= [1+p^(-1/2)]/(p-1).

Its real part is strictly positive for every odd p and every a != c, so no distinct raw rows are orthogonal.

For the first decomposition W=C+R:

    <C_a,C_c> = 1/p,
    <C_a,R_c> = <R_a,C_c> = -1/p^2,
    <R_a,R_c> = g(a-c)/p^2.

Thus E_C=1/p, E_R=1/p^2, and for a != c

    <R_a,R_c> = epsilon_p chi(a-c)/p^(5/2),
    |<R_a,R_c>|/E_R = 1/sqrt(p).

The a=0 residual row is -s/p at b=0 and zero elsewhere. For each a != 0, every R entry has magnitude p^(-3/2). Neither case is omitted.

For the orthogonal decomposition W=D+H:

    D_a(b)=kappa=s(p-1)/p^2,
    sum_b H_a(b)=0,       sum_a H_a(b)=0,
    <D_a,H_c>=0,

    <D_a,D_c> = (p-1)^2/p^3,
    <H_a,H_c> = [g(a-c)-1/p]/p^2.

Therefore

    E_D=(p-1)^2/p^3,
    E_H=(p-1)/p^3,
    E_D/E_W=(p-1)/p,      E_H/E_W=1/p.

For a != c,

    rho_H(a,c)=[sqrt(p) epsilon_p chi(a-c)-1]/(p-1).

In the p=1 (mod 4) class this is 1/(sqrt(p)+1) when chi(a-c)=1, and -1/(sqrt(p)-1) when chi(a-c)=-1. In the p=3 (mod 4) class its magnitude is sqrt(p+1)/(p-1). These formulas give asymptotic decorrelation only for the residual rows. At p=3 the H normalized off-diagonal magnitude is 1; the exact small-prime degeneracy is retained.

For completeness, the raw Gram eigenvalues are

    (p-1)^2/p^2                 with multiplicity 1,
    2/p^2                      with multiplicity (p-1)/2,
    0                          with multiplicity (p-1)/2.

The H Gram eigenvalues are 2/p^2 with multiplicity (p-1)/2 and 0 with multiplicity (p+1)/2. In particular, the H rows cannot form p nonzero orthogonal rows: their rank is only (p-1)/2. The R Gram eigenvalues are 1/p^2 once, 2/p^2 with multiplicity (p-1)/2, and 0 with multiplicity (p-1)/2.

## 3. Elementary proof and normalization/phase audit

### 3.1. Counting the arithmetic atom

The number of y with y^2=u is 1+chi(u). Hence

    nu_p(n)=p+sum_x chi(n-x^2).

For n != 0, count solutions (x,z) to z^2=x^2-n. Since 2 is invertible, the map

    (x,z) -> (x-z,x+z)

is a bijection onto ordered pairs (u,v) with uv=n. There are p-1 such pairs. Therefore

    p+sum_x chi(x^2-n)=p-1,
    sum_x chi(x^2-n)=-1.

It follows that sum_x chi(n-x^2)=-s. When n=0 the same sum is s(p-1), since every nonzero x has chi(x^2)=1. This proves

    nu_p(n)=p-s+p s 1_{n=0}.

Dividing by p and subtracting 1 yields the exact formula for f. Inserting it in the defining transforms proves Q=(1-s/p)A+s/p and W=(s/p)(1-A). No asymptotic estimate or distributional approximation is used.

### 3.2. Quadratic Gauss sum, including the sign of its phase

Set zeta=e_p(1) and

    G=sum_x zeta^(x^2)=sum_t chi(t) zeta^t.

The second equality follows by counting square roots and using sum_t zeta^t=0. For a != 0, substitution in the character expression gives

    sum_x e_p(a x^2)=chi(a) G.

Also conjugate(G)=sG. To compute the magnitude, use u=t v in the character expression for |G|^2, with u,v nonzero:

    |G|^2
      = sum_(t != 0) chi(t) sum_(v != 0) e_p((t-1)v)
      = (p-1) - sum_(t != 0,1) chi(t)
      = p.

Thus G^2=s p, but this alone leaves the sign undetermined. The following determinant argument fixes it for the specified exponential convention.

Let U be the p by p complex matrix

    U_(j,k)=p^(-1/2) zeta^(j k),       0 <= j,k < p.

Finite geometric summation gives U^2=J_ref, where J_ref sends coordinate j to coordinate -j. Consequently U^4=I, U is diagonalizable, and its eigenvalues lie in {1,-1,i,-i}. If their multiplicities are m_1,m_-1,m_i,m_-i, then

    m_1+m_-1=(p+1)/2,
    m_i+m_-i=(p-1)/2,
    tr(U)=G/sqrt(p).

The normalized Vandermonde determinant has phase

    det(U)=i^[p(p-1)/2].

Indeed,

    det(zeta^(j k))=product_(j<k)(zeta^k-zeta^j),

and each difference is

    2i sin(pi(k-j)/p) exp(pi i(k+j)/p),

with strictly positive sine. The sum of k+j over j<k is p(p-1)^2/2, so the accumulated exponential factor is exp(pi i(p-1)^2/2)=1. The remaining phase is i^[p(p-1)/2]. The magnitude is 1 after normalization because U is unitary.

If p=4k+1, write G/sqrt(p)=sigma with sigma in {1,-1}. The trace identities give m_i=m_-i=k and m_-1=k+(1-sigma)/2. Thus

    det(U)=(-1)^[k+(1-sigma)/2].

The Vandermonde value is (-1)^k. Hence sigma=1.

If p=4k+3, write G/sqrt(p)=sigma i with sigma in {1,-1}. Then m_1=m_-1=k+1 and m_-i=k+(1-sigma)/2. Consequently

    det(U)=(-1)^[k+1+(1-sigma)/2] i.

The Vandermonde value is (-1)^(k+1)i, again forcing sigma=1. Therefore G=epsilon_p sqrt(p), with the phase stated in Section 2.

For a != 0, completing the square gives

    a n^2+b n = a(n+b/(2a))^2-b^2/(4a).

Combining this with G fixes the exact phase and normalization of A. When a=0 the finite geometric sum gives the two separate degenerate formulas.

### 3.3. Gram identities

Orthogonality in the b variable gives, for all a,c,

    sum_b A_a(b)=1,

    sum_b A_a(b) conjugate(A_c(b))
      = (1/p) sum_n e_p((a-c)n^2)
      = g(a-c).

The first identity retains only n=0. In the second, the b sum enforces equality of the two n variables, and its factor p cancels one of the two factors 1/p in A.

Since s is real and s^2=1,

    <W_a,W_c>
      = p^(-2) sum_b (1-A_a(b))(1-conjugate(A_c(b)))
      = p^(-2)[p-1-1+g(a-c)].

This proves the full raw Gram formula, including its diagonal. It also immediately proves the C,R formulas. For a != c, the real part of the numerator is at least p-2-p^(-1/2)>0 for p>=3, proving the nonorthogonality claim. Subtracting 1 from rho_W gives the claimed uniform proximity to 1.

### 3.4. The orthogonal common term

The average of W_a over b is

    (1/p)sum_b W_a(b)=s(p-1)/p^2=kappa.

The same constant is the average over a at each b: the a average of A_a(b) is 1/p, since n^2=0 only for n=0. This proves both zero-sum identities for H and the orthogonality to D.

The arithmetic origin of this common term is particularly direct:

    W_a(b)
      = f_p(0)/p -(s/p^2)sum_(n != 0)e_p(a n^2+b n)
      = kappa + H_a(b).

Thus D is exactly the true n=0 contribution. It is not a term generated by an approximation. The Gram identity

    <H_a,H_c> = p^(-2)[g(a-c)-1/p]

follows either by expanding A-1/p or by restricting the preceding b-orthogonality calculation to n != 0. The energies and normalized off-diagonals in Section 2 follow by setting a=c or using the exact nonzero g formula.

To check ranks and eigenvalues, put K_(a,c)=g(a-c). For t in F_p let v_t(a)=e_p(a t) and let m(t) count n with n^2=t. Then

    K_(a,c)=(1/p)sum_t m(t)e_p((a-c)t),
    K v_t=m(t)v_t.

Here m(0)=1, m(t)=2 for nonzero squares, and m(t)=0 for nonsquares. The all-ones matrix acts by p on v_0 and by zero on all other v_t. Apply this to

    Gram(W)=p^(-2)[(p-2)J_all+K],
    Gram(H)=p^(-2)[K-J_all/p],
    Gram(R)=p^(-2)K

to obtain the asserted spectra.

### 3.5. The extra owner after deleting the common component

For arbitrary complex weights omega_(a,b), define the finite linear functional

    T_W(omega)=sum_(a,b) omega_(a,b) W_a(b).

The exact orthogonal split gives

    T_W(omega)
      = kappa sum_(a,b) omega_(a,b)
        + sum_(a,b) omega_(a,b) H_a(b).

Consequently the newly separated owner is the weighted n=0/common-mean term kappa sum omega. For product weights alpha_a beta_b it is kappa (sum alpha)(sum beta). A complex-conjugate convention on the beta weights only conjugates that factor. The C,R split instead introduces the owner (s/p)sum omega and a residual whose cross term with C is nonzero.

The original arithmetic centering sum_n f_p(n)=0 does not remove either of these terms from a quadratic transform. It guarantees W_(0,0)=0, which uses cancellation between the pieces. For example, at (a,b)=(0,0), the orthogonal split has D=kappa and H=-kappa. Any argument that drops D at this point has changed the answer.

There is an even stronger exact control: with all weights omega=1,

    sum_(a,b) W_a(b)=s(p-1),
    sum_(a,b) H_a(b)=0.

Thus the entire aggregate in this control is carried by the deleted common component. Any use of H decorrelation must separately prove cancellation or an adequate bound for this owner under the actual downstream weights. No such downstream weights or bridge were supplied in this isolated task.

## 4. First doubtful or unproved step

There is no unproved step in the finite identities above. The Gauss-sum sign, the a=0 row, both prime congruence classes, Gram orientation, rank deficiency, and the nonorthogonal versus orthogonal splits are explicitly covered.

The first invalid inference would be to apply the residual-row correlation estimate as an estimate for W after silently deleting its common term. The all-ones weight control disproves that inference. A second unproved inference would be to turn complete finite-field Gram identities into bounds for incomplete arithmetic sums or circle discrepancy. That would require an exact embedding of the relevant sums, their weights and normalizations, and a proof of control for the common component and all completion errors. This report supplies no such bridge.

## 5. Required controls and outcomes

The analytical controls are exact:

- a=0,b=0: A=1,Q=1,W=0, with cancellation of D and H.
- a=0,b!=0: A=0,Q=W=s/p; this tests the sign change between the two prime classes.
- Arithmetic totals: sum_n nu_p(n)=p^2 and sum_n f_p(n)=0.
- Gram diagonal: every W row has (p-1)/p^2 energy, including a=0.
- Hermitian orientation: g(-d)=conjugate(g(d)), since chi(-1)=s and conjugate(epsilon_p)=s epsilon_p.
- Common-mode adversary: all-ones weights give sum W=s(p-1) but sum H=0.
- Smallest-prime degeneracy: at p=3 the H Gram has rank 1 and normalized off-diagonal magnitude 1; no uniform exact orthogonality is claimed.
- Rank control: for every odd p, H has rank (p-1)/2, excluding an accidental claim of p orthogonal nonzero residual rows.

A bounded diagnostic was also executed using Python standard-library binary64 complex arithmetic. Parameters were p in {3,5,7,13}, all a,b,c modulo each p, direct enumeration of nu, and direct complete sums for A,Q,W. No files besides this report were created. Arithmetic counts were tested by exact integer equality; all complex identities were tested by absolute error < 1e-12.

Command: the following source was passed to python - on standard input in PowerShell.

~~~python
import cmath, math
P=[3,5,7,13]
for p in P:
    s=1 if p%4==1 else -1
    eps=1 if p%4==1 else 1j
    chi=lambda a: 0 if a%p==0 else (1 if pow(a%p,(p-1)//2,p)==1 else -1)
    e=lambda t: cmath.exp(2j*math.pi*(t%p)/p)
    nu=[sum((x*x+y*y)%p==n for x in range(p) for y in range(p)) for n in range(p)]
    assert all(nu[n]==p-s+p*s*(n==0) for n in range(p))
    A=[[sum(e(a*n*n+b*n) for n in range(p))/p for b in range(p)] for a in range(p)]
    W=[[sum((nu[n]/p-1)*e(a*n*n+b*n) for n in range(p))/p for b in range(p)] for a in range(p)]
    Q=[[sum((nu[n]/p)*e(a*n*n+b*n) for n in range(p))/p for b in range(p)] for a in range(p)]
    af=lambda a,b: (1 if b==0 else 0) if a==0 else eps*chi(a)/math.sqrt(p)*e(-b*b*pow(4*a,-1,p))
    errors=[]
    for a in range(p):
        for b in range(p):
            errors += [abs(A[a][b]-af(a,b)),abs(W[a][b]-s/p*(1-A[a][b])),abs(Q[a][b]-((1-s/p)*A[a][b]+s/p))]
        for c in range(p):
            gram=sum(W[a][b]*W[c][b].conjugate() for b in range(p))
            errors.append(abs(gram-(p-2+A[(a-c)%p][0])/p**2))
            H=[[W[z][b]-s*(p-1)/p**2 for b in range(p)] for z in [a,c]]
            hgram=sum(H[0][b]*H[1][b].conjugate() for b in range(p))
            errors.append(abs(hgram-(A[(a-c)%p][0]-1/p)/p**2))
    err=max(errors)
    assert err<1e-12
    print(f'p={p}: nu exact PASS; transform/Gram/split PASS; max_abs_error={err:.3e}')
~~~

Observed output:

~~~text
p=3: nu exact PASS; transform/Gram/split PASS; max_abs_error=4.228e-16
p=5: nu exact PASS; transform/Gram/split PASS; max_abs_error=1.241e-16
p=7: nu exact PASS; transform/Gram/split PASS; max_abs_error=9.042e-17
p=13: nu exact PASS; transform/Gram/split PASS; max_abs_error=4.389e-16
~~~

These checks are diagnostic_only, not the proof of any prime-uniform statement. Their limitations are floating-point phase evaluation and a finite prime list. The proof is the finite algebra in Section 3. Analytical work formed more than 80 percent of this task; experimentation was one bounded diagnostic run.

## 6. Dependencies and exact artifacts used

Read dependencies, and no others:

1. protocol.md.
2. strategy/round231_quadratic_signed_admission/briefs/blind_quadratic_statement.md.
3. The coordinator's task message assigning the isolated task and output path.

The graph identifier is recorded only as supplied provenance. The graph, active campaign, historical evidence, other briefs, sibling reports, and web literature were not read, as required by the statement-only isolation.

Mathematical dependencies are elementary finite-field square counting, invertibility of 2 modulo odd p, finite geometric-series orthogonality, completion of a square, elementary quadratic-character identities, and the finite Vandermonde determinant/eigenvalue calculation proved or specified in Section 3. No imported analytic theorem or external theorem hypothesis is used.

Sole written artifact: strategy/round231_quadratic_signed_admission/reports/blind_quadratic_rows.md. No state, proof draft, validation matrix, synthesis, or successor-round artifact was changed.

## 7. Scope and recommended state effect

Recommended effect: retain the explicit finite algebraic lemma as independently derived evidence; reject the claim that quadratic demodulation alone makes the original centered W rows orthogonal or parametrically decorrelated. Revise any residual-only mechanism to include its separately owned common/zero-residue contribution.

The conductor may consider the finite identities for promotion only after the required independent seam checks and graph validation. This report itself makes no authoritative graph change. Residual decorrelation is real and quantified, but it concerns R or H after an explicit subtraction. It does not close an incomplete-sum estimate, endpoint uniformity, a signed arithmetic discrepancy estimate, or any circle-discrepancy obligation. No next round is proposed.
