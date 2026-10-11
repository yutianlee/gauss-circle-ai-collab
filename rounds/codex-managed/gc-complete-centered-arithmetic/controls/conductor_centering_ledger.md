# Round 213 conductor ledger: actual centering and positive kernels

## 1. Result

Campaign: gc-complete-centered-arithmetic. Date: 2026-09-28.
Role: conductor analytical control, not a blind report.
Graph SHA256: 4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.

Scalar centering preserves the complete target up to an already paid cost.
It does not repair either of two explicitly positive radius-kernel
certificates. This is proved on actual r2 coefficients, using their residue
zeros and closed 212's actual mass lemma. Both certificates retain the
scale N/sqrt(Lambda_*), up to epsilon powers. No lower bound for the
actual signed remainder, circle error or signed radius energy is asserted.

The conductor derived the residue-mass dichotomy and discretization before
receiving the isolated analyst's matching interim result. This ledger is
still NONBLIND; a separate final-hash seam must check it before closure.
All reasoning is analytical. No numerical experiment or new source import.

## 2. Exact hypotheses and statements

Use the frozen 213 definitions with b=83/650, actual a_s(n), real W_s,
psi_s, D_s, I_s, and Omega. Put

    Lambda_*=LK/U ~ T^(1-6b)=T^(76/325),
    E_s=D_s-rho_s I_s,
    C_s=sum_n (a_s(n)-rho_s) W_s(n)e(R psi_s(n)).

Here rho_s is any nonnegative constant <<_epsilon T^epsilon; in particular
it may be the candidate rho_loc. It need not be an established integer
mean. Uniform upper statements use the whole frozen band. Lower statements
assume N=T^alpha for each fixed 4b<alpha<1-2b, with sufficiently large T.
Constants in lower statements may depend on that fixed interior scale.

Let w>=0 be fixed smooth, supported inside [1/sqrt(2),sqrt(3)], with
integral one, and hat_w_plus(y)=integral w(t)e(ty)dt. Define

    M_s=sum_n a_s(n)|W_s(n)|,
    M'_s=sum_n |a_s(n)-rho_s||W_s(n)|,
    G'_s=sum_(n,m) |a_s(n)-rho_s||a_s(m)-rho_s|
         |W_s(n)W_s(m)| |hat_w_plus(T(psi_s(n)-psi_s(m)))|,
    P'=(LK)^(-1)sum_Omega sqrt(G'_s).

Alternatively define a real signed measure

    dnu_s(t)=sum_n a_s(n)W_s(n) delta_n(t)-rho_s W_s(t)dt,
    G^nu_s=double_integral |hat_w_plus(T(psi_s(t)-psi_s(u)))|
                          d|nu_s|(t)d|nu_s|(u),
    P^nu=(LK)^(-1)sum_Omega sqrt(G^nu_s).

Both satisfy, at fixed interior scales,

    c N/sqrt(Lambda_*) <= P', P^nu
                         <<_epsilon T^epsilon N/sqrt(Lambda_*).       (1)

Consequently either certificate fails the proposed T^(4b+epsilon) size
when alpha>1/2+b=204/325, for sufficiently small epsilon. The actual
signed remainder is not bounded below by either certificate.

## 3. Proof and complete costs

### A. Scalar subtraction and a uniform sum-integral bridge

The smooth phase derivative is positive and comparable to Lambda_s/N on
the complete support. Its j-th derivative is O_j(Lambda_s N^-j) after
multiplication by R in the fixed window. Repeated continuous integration
by parts, with the compact smooth amplitude, gives

    |I_s(R)| <= C_A N(1+Lambda_s)^(-A).

Product-shift summation therefore gives

    (LK)^(-1)sum_Omega |rho_s I_s|
       <<_epsilon T^epsilon N/Lambda_*
       ~ T^epsilon N T^(6b-1) <= T^(4b+epsilon).                      (2)

Logarithms from the harmonic shift sum are absorbed with a separate
epsilon allocation. Both directions of the triangle inequality show that
the averages of |D_s| and |E_s| on Omega differ by at most (2). The paid
complement from 212 then makes their target-sized upper bounds equivalent.
This equivalence is not an estimate for either of them.

Write f_s(t)=W_s(t)e(R psi_s(t)), smoothly zero extended. Exactly,

    E_s-C_s=rho_s [sum_n f_s(n)-integral f_s(t)dt].                   (3)

For every integer A>=2, Poisson summation and integration by parts at
the nonzero integer Fourier modes give the elementary uniform bound

    |sum f_s(n)-integral f_s|
       <= C_A N^(1-A)(1+Lambda_s)^A.                                (4)

Indeed ||f_s^(A)||_1<=C_A N^(1-A)(1+Lambda_s)^A and
sum_(m!=0)|m|^-A is finite. On the entire band,
N/(1+Lambda_s) >= c T^(90/325). Since N<=T^(242/325), choosing A
sufficiently large in (4) gives O_B(T^-B) for any prescribed B. This
also absorbs rho_s after a fixed epsilon allocation. Thus (3) is
arbitrarily small uniformly in s,R and real T,N. No cell endpoint,
sharp overlap cutoff or hidden atom is inserted into this argument.

### B. Actual congruence zeros force centered absolute mass

Put S_s=sum_n |W_s(n)| and Z_s=sum_(n=3 mod4)|W_s(n)|. The fixed
nonzero mask has a closed interval on which it is bounded away from zero.
Since h+k=o(N) uniformly and Psi tends uniformly to one on this band,
S_s>=cN for every shift pair once T is large. Also S_s<=CN.

The absolute value of W_s is Lipschitz and its total variation is O(1):
its almost-everywhere derivative is bounded by |W'_s| and the support
length is O(N). Grouping consecutive integers into blocks of four gives

    Z_s=S_s/4+O(1), hence Z_s>=S_s/5                               (5)

for large T, uniformly in all shifts. This does not require |W_s| to be
C-infinity or presume finitely many zeros of the signed mask.

Actual sums of two squares never equal 3 modulo 4, so a_s(n)=0 on
that residue class. Therefore

    M'_s >= rho_s Z_s,            M'_s >= M_s-rho_s S_s.

Combining these inequalities with (5) proves M'_s>=M_s/6, independently
of how rho_s was selected. This is stronger than a claim about a guessed
mean: even optimal nonnegative constant centering cannot remove the
absolute arithmetic mass. Closed 212 proves, for each fixed interior
scale, sum_Omega M_s>=cLKN after both paid sectors are removed. Hence

    sum_Omega M'_s>=c'LKN.                                          (6)

### C. Positive kernel lower bound and its scope

The normalized radius frequency derivative obeys
T psi'_s(t) comparable to Lambda_s/N on [N,4N]. Partition this interval
into at most C(1+Lambda_s) consecutive bins of length at most
cN/(1+Lambda_s). Within each bin the kernel argument is sufficiently
small that |hat_w_plus|>=1/2. If B_j is its M'_s mass, positivity and
Cauchy imply

    G'_s >= (1/2)sum_j B_j^2 >= c (M'_s)^2/(1+Lambda_s).

Since 1<Lambda_s<=Lambda_* on Omega, averaging and (6) give the first
lower bound in (1). All integers lie in exactly one bin. There is no
assumed four-point mean and no deletion of unfavorable coefficient signs.

For the measure version, the atomic and continuous parts are mutually
singular, so exactly

    d|nu_s|=sum_n a_s(n)|W_s(n)|delta_n+rho_s|W_s(t)|dt.

Its positive double integral contains the uncentered atomic-atomic
certificate as a nonnegative summand. The same bin proof with M_s,
and the inherited actual mass bound, supplies the second lower bound.
Unlike the discrete centering proof, this measure argument does not even
need residue zeros: total variation destroys the model subtraction first.

### D. Matching upper cost, including diagonal spacing

Schwartz decay and the derivative lower bound imply for all support
points t,u

    |hat_w_plus(T(psi_s(t)-psi_s(u)))|
       <= C_A (1+Lambda_s |t-u|/N)^(-A).

The discrete coefficients and rho_s are at most T^epsilon, and masks
are bounded. Summing first over the lattice difference gives

    G'_s <<_epsilon T^epsilon [N+N^2/Lambda_s].                     (7)

The same bound holds for G^nu_s: the atomic-atomic part gives (7),
while each mixed or continuous part is bounded by integrating the same
decaying kernel against densities at most T^epsilon. The lattice
diagonal term N is retained explicitly.

Finally

    (LK)^(-1)sum_(h<L,k<K) Lambda_s^(-1/2)
       <= C sqrt(U/(LK)),

by the two sums of h^(-1/2), k^(-1/2). Thus either certificate is at
most T^epsilon[sqrt(N)+N/sqrt(Lambda_*)]. Throughout this band
Lambda_*<<N, so the second term dominates. This completes (1).

### E. What norm is actually bounded

Normalized radius measure T^-1 w(R/T)dR has mass one. Its exact
mean square of C_s is the double sum with the signed coefficients and
the complex kernel hat_w_plus, without absolute values. Termwise
modulus bounds that mean square above by G'_s. Cauchy in radius gives

    (1/T)integral w(R/T) [(LK)^(-1)sum_Omega |C_s(R)|] dR <= P'.

The measure version gives the analogous inequality for E_s and P^nu.
Equation (3) connects C_s and E_s with negligible error. Neither formula
is a pointwise supremum estimate, and neither reverses its inequality.
The exponent in (1) is alpha-(1-6b)/2. Subtracting 4b gives
alpha-1/2-b, proving the stated certificate obstruction and nothing
stronger about the signed arithmetic quantity.

## 4. First unproved step

No complete estimate of the signed centered arithmetic remainder has
been obtained. Exact residue zeros refute the hope that scalar centering
by itself makes a positive kernel small, but they do not refute
cancellation in the signed double sum. A periodic arithmetic model with
nonconstant values has different residue behavior and is not covered by
the scalar mass lemma without a separate proof. A signed radius-energy
bound still needs an explicit pointwise transfer to solve the target.

## 5. Required controls and outcomes

- Actual r2: the residue zero and inherited positive mass are actual.
- Complete shifts: all of Omega is retained; its removed sectors were
  independently priced in closed 212, whose mass proof subtracts them.
- Masks: real sign changes and nonsmooth absolute values are paid by
  total variation; Poisson is applied only to smooth signed W_s.
- Means: rho_s is an arbitrary bounded scalar; no integer mean is assumed.
- Endpoints: smooth zero extension, exact ceilings and real parameters
  retain all atoms and support boundaries.
- Norms: exact normalized radius mean, supremum and upper certificate
  are distinguished. Mixed terms are retained in the signed identities.
- Exponents: Lambda_*=T^(76/325), root loss 38/325 and threshold
  alpha=204/325 are explicit; lower results are fixed-interior only.
- Full goal: neither the milestone nor quarter or an M1/M2 parent follows.

These are analytical controls. No finite experiment certifies an
asymptotic statement.

## 6. Dependencies and provenance

Read protocol.md, the authoritative current graph and manifest, the
frozen strategy and closed 212 synthesis and reports. The inherited
mass and local candidate statements are from
rounds/codex-managed/gc-complete-four-point-correlation/reports/four_point_oscillatory_attack.md
(SHA256 7c84d41e28c726d39b13cfe6b1e65f6cf8800ff746ca43b56157954908db423f)
and reports/four_point_local_arithmetic.md in that campaign
(SHA256 6ab0a4f40d1304a846a166f3e9cf76659107a94457f32cdd1b1d95a6e3a4605e).
Closed 212's independent reviews and archive were checked before freezing
213. The finite inequalities here are proved directly, without importing
a new theorem. Agent interim messages were used for monitoring; this
ledger claims no statement-only credit. The separate isolated report and
independent seam supply their own precise provenance.

## 7. Recommended state effect

Retain as reviewed scoped evidence if the independent seam passes. Do
not promote a signed correlation, moment, pointwise exponent or parent.
Both named positive certificates are quantitatively insufficient on the
upper subband, even after scalar centering. Actual signed cancellation
remains an open research input. No successor round begins here.
