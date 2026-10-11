# Round220 reciprocal-energy source audit

## 1. Result

Campaign `gc-full-goal-arithmetic-source-review`, round220; task
`reciprocal_energy_sources`; source auditor, NONBLIND selected context.
Date: 2026-09-28. Starting graph SHA256:
`a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
Earlier218--219 work in this reused agent is disclosed history.

**No complete source gain.** Two current primary theorem statements
were audited: Blomer--Pascadi2607.24311v1, Theorem1.1, and
Milicevic--Qin--Wu2511.07550v1, Theorem1.1. Exact completion into their
Kloosterman kernels is possible after retaining the real-anchor rounding
factor. The resulting full coefficient norms and lengths, however, do
not prove the complete actual219 energy target.

The rounding factor has bounded product-decomposition mass, uniformly
on the entire truncation. Moving interval stars cost logarithms under
a genuine row/column operator hypothesis. These facts remove a false
objection based only on nonintegral anchors. They do not supply the
missing arithmetic operator hypothesis or upgrade separately factored
j/a coefficient bounds to arbitrary coefficients indexed by (j,a).

For the explicit complete-residue completion below, Blomer--Pascadi
gives a legal but expensive energy bound T^epsilon J^2 A^(32/9), capped
by the complete elementary bound J^2 A^2 K. Milicevic--Qin--Wu fails
its length condition on permitted scale ranges; on eligible primitive
blocks its completed norm estimate is already worse than the relevant
trivial bound. All excluded blocks can be paid, but doing so returns
the same complete elementary cap. Neither is an impossibility theorem
for every conceivable use of those papers.

A separate exact control refutes a stronger proposed uniform COMPLEX
combined-row operator certificate. An integral version has zero sine
rows; a shifted-residue version also refutes the analogous arbitrary
REAL row certificate. Neither refutes the actual signed target. The complete
moment remains T^(10 beta+epsilon), with beta as in Section3.7; the
fixed twelfth target and the full quarter goal both remain open.

## 2. Exact statement and hypotheses

Write e(x)=exp(2 pi i x). The actual219 rectangle has

    1<=D<=N<=T^(3/2),  K=N/D,  U=T sqrt(N),
    A=U/D,  b0=D/sqrt(U),  R_j in[T/2,2T].

N,D are dyadic; k ranges over the positive integers in[K/2,2K).
The R_j are actual maximal N^(-1/2)-separated high points of the
original rectangle H, and sigma_j=sign H(R_j). The retained level is
v>=T^(13/125)/(2L), L=O(log^2 T). Nonempty high rectangles necessarily
satisfy N>>v^4 and

    D >>_eta T^(-13/42-eta) v^2 N^(29/84).               (1)

These are necessary conditions, not existence assertions. The actual
Schwartz weight also restricts nonempty high rectangles to
N<=C_zeta T^(1+zeta) for each fixed zeta>0. No such tail restriction
is needed for the uniform rounding argument below.

The reviewed219 transform defines, on positive odd a in a fixed
enlargement a~A,

    alpha_(j,a)=R_j^2/a,
    omega_(j,a)(k)=sqrt(T/R_j)(K/k)
        Psi(2R_j k/(a sqrt(T))) s_(j,a)(k),
    E=sum_k [sum_(j,a) sigma_j chi4(a) omega_(j,a)(k)
                                      sin(2 pi k alpha_(j,a))]^2. (2)

Here Psi is the actual real mollifier transform, with its sign retained.
The selector s is the literal stationary interval with its endpoint
half-values. It enforces the intersected conditions
D<=4R_j^2 k/a^2<2D and
N<=4R_j^2 k^2/a^2<min(2N,T^(3/2)), with the prescribed stars.
For each (j,a) its support is an interval in k, up to O(1) endpoint
values. The sufficient COMPLETE estimate remains

    E <= J^2 v^2 T K/256 + C_eta T^(rho+eta) J A K,
    rho=208/2625.                                      (3)

Expanding (2) gives difference cosines MINUS sum cosines at
alpha_(j,a)-alpha_(l,b) and alpha_(j,a)+alpha_(l,b), with their
actual signed coefficient product. Every integer alias of both
frequencies belongs to (3). No positive or zero-alias surrogate is
identified with this energy.

The two audited source cards are as follows. They are external theorem
inputs, not proofs of any application claimed here.

**BP, Theorem1.1.** For integer q>=1, 1<=H<=q, intervals I,J of
length at most H, arbitrary complex coefficients, and a unit t mod q,

    sum_(m in I,n in J,(m,n,q)=1) u_m w_n S(tm,n;q)
      << ||u||_2||w||_2 q^(1+o(1)) F_q(H),
    F_q(H)=H^(1/8)q^(-3/32)+H^(5/16)q^(-3/16)
                                      +H^(2/3)q^(-7/18).        (4)

Here S(m,n;q)=sum_(x mod q,unit)e((mx+n xbar)/q) is unnormalized.
For I=J={1,...,H}, the gcd constraint may be removed. There is no
factorability restriction on q. This remains a fixed-modulus theorem.
Source: Valentin Blomer and Alexandru Pascadi,
[*Bilinear forms with Kloosterman sums via quadratic characters*,
2607.24311v1, Theorem1.1](https://arxiv.org/html/2607.24311v1).

**MQW, Theorem1.1.** For integer q>=1, M,H>=1, coefficients supported
on[1,M],[1,H], and (t,q)=1, assume

    1<=M<=H q^(1/4),  M^(7/5)H<q^(3/2),  MH<=q^(5/4).

With Kl2(z;q)=q^(-1/2)sum_(x mod q,unit)e((zx+xbar)/q),

    sum_(m<=M,n<=H) u_m w_n Kl2(tmn;q)
      <<_epsilon q^epsilon ||u||_2||w||_2 sqrt(MH)
        [M^(-1/2)q^(1/6)+M^(-3/25)H^(-3/10)q^(1/5)
                                      +(MH)^(-3/16)q^(11/64)]. (5)

No special factorization of q is required. Source: Djordje Milicevic,
Xinhua Qin and Xiaosheng Wu,
[*Bilinear forms with Kloosterman sums and moments of twisted
L-functions*, 2511.07550v1, Theorem1.1](https://arxiv.org/html/2511.07550v1).
The normalization q^(-1/2) is essential in applying (5).

## 3. Proof or derivation

### 3.1 Exact real-anchor retention and actual weight norms

Choose M_j to be a nearest integer to R_j^2 and put
delta_j=R_j^2-M_j, |delta_j|<=1/2. The identity is

    e(k R_j^2/a)=e(k M_j/a)e(delta_j k/a).               (6)

Since K/A=sqrt(N)/T<=T^(-1/4), the last factor has the exact uniformly
convergent decomposition

    e(delta_j k/a)=sum_(r>=0) (2 pi i K/A)^r/r!
                                (delta_j A/a)^r(k/K)^r.         (7)

The sum of products of the row and column sup norms is at most
exp(C K/A)=O(1). Each term even separates into a j factor, an a factor,
and a k factor. No pointwise error is discarded and no accumulated
J A error is hidden. Rounding is therefore not the obstruction here.

For the smooth part of omega, put x=R_j/T, y=a/A, z=k/K. It is

    x^(-1/2) z^(-1) Psi(2 sqrt(N/T) xz/y).              (8)

On the fixed positive compact x,y,z ranges, all fixed scaled
derivatives are uniformly bounded. Indeed they are combinations of
s^r Psi^(r)(s), uniformly bounded by Schwartz regularity. Extend with
fixed smooth cutoffs to a compact box. Integration by parts in its
three-dimensional Fourier series, to a fixed order greater than the
dimension, yields an exact sum of j/a/k product factors whose product
sup norms have O(1) total mass. This also covers the full N>T range.
It retains the actual Psi, including its sign.

For clarity, the precise mask lemma needed in this use is elementary:
if a matrix W_(r,k) has l2 operator norm at most Lambda, then
W_(r,k)1_(k in I_r), with one arbitrary integer interval I_r per row,
has norm O(log(2K)) Lambda on O(K) consecutive columns. Decompose each
I_r into canonical dyadic intervals. At one scale a row uses at most
two intervals. Split these into two lists. Within either list the row
sets are disjoint and the column intervals are disjoint; Cauchy gives
Lambda||x||_2||z||_2 for that whole scale. Summing the scales proves
the assertion. O(1) separate singleton corrections pay the stars by
the same argument. Thus the actual s masks cost only logarithms when
a genuine uniform row operator estimate is available.

This lemma does NOT say that a theorem for coefficients x_j y_a z_k
is a theorem for arbitrary x_(j,a) z_k. A generic bounded (j,a) mask
can be expanded by j at projective l2 cost J sqrt(A), versus the
combined row norm sqrt(JA); expansion by a gives the analogous
alternative. The safe generic relative cost is therefore as large as
sqrt(min(J,A)). This is a stated available upper cost, not a lower
bound for the special stationary mask. Below a is fixed before each
source call, so the genuine rows are j, and the a summation is paid
explicitly by the triangle inequality. No tensor upgrade is used.

### 3.2 Exact fixed-modulus completion, all gcd strata and norms

For fixed odd a, partition j by g=gcd(M_j,a), put q=a/g, m_j=M_j/g.
Then (m_j,q)=1 and e(M_j k/a)=e(m_j k/q). For q>1 the exact identity

    e(m k/q)=q^(-1) sum_(n mod q) S(k,n;q)e(-n mbar/q)  (9)

holds for every k, including nonunits. Opening S and summing n
forces xbar=mbar, hence x=m, proving (9). The dual variable occupies
all residues. Ordinary division was not identified with inversion.

For an arbitrary row vector x_j in this g stratum, define

    B_g(n)=sum_(j:gcd(M_j,a)=g) x_j e(-n mbar_j/q),
    mu_g=max_r #{j in this stratum:mbar_j=r mod q}.

Finite Parseval gives exactly

    ||B_g||_2^2=q sum_(r mod q)
                      |sum_(j:mbar_j=r) x_j|^2
                 <= q mu_g ||x_g||_2^2.                (10)

In particular ||x_g||_2=sqrt(J_g) for the original signs before
bounded smooth product factors, but ||B_g||_2 is not automatically
sqrt(q J_g): residue multiplicity must be retained. If the k support
exceeds q, group its coefficients modulo q. This costs at most
sqrt(C(1+K/q)) in l2, with a fixed C for the actual cofactor interval.
All sequences are represented on[1,q], using q for residue zero.
The q=1 case is handled directly, with norm at most
sqrt(CK J_g); it need not be assigned a fictitious inverse.

The norm estimates derived from (9)--(10) hold for arbitrary x,z,
and therefore provide the genuine fixed-a row operators required in
Section3.1. Smooth factors cost O(1), stars O(log(2K)). These prices
apply before any actual sign or weight is enlarged in modulus.

### 3.3 Complete application of BP and its restored price

Apply (4) with q as just defined, H=q, I=J=[1,q], t=1, and inputs
the residue-grouped k vector and B_g. These origins are important:
they permit the removal of the gcd(m,n,q)=1 restriction even for
nonunit cofactors and the residue-zero term. Thus no exceptional
gcd contribution is omitted.

At H=q, F_q(q)<<q^(5/18), because its three exponents are
1/32,1/8,5/18. Equations(9)--(10) consequently give

    |sum_(j in g,k) x_j z_k e(m_j k/q)|
      <<_epsilon q^(7/9+epsilon) sqrt(mu_g)
                  sqrt(1+K/q)||x_g||_2||z||_2.          (11)

Every normalization in this cost is explicit: q^(-1) in (9),
q^(1+5/18) in (4), and sqrt(q mu_g) in (10).
As q<=a and K<=C a, q^(7/9)sqrt(1+K/q)<<a^(7/9).
For arbitrary x, summing the g strata costs at most
sqrt(sum_g mu_g)||x||_2<=sqrt(J)||x||_2. For the actual bounded
row factors it costs at most sum_g J_g=J. The q=1 contribution also
fits this bound since sqrt(K)<=C a^(7/9).

The complete, actually weighted fixed-a k vector therefore has l2
norm at most T^epsilon J a^(7/9). Summing the O(A) odd a by triangle
and retaining the real part only after forming the exact vector gives

    E <= ||sum_(j,a) sigma_j chi4(a)omega_(j,a)(k)
                                         e(k R_j^2/a)||_2^2
      <<_epsilon T^epsilon J^2 A^(32/9).               (12)

The enlargement from sine to a complex norm and the triangle over a
are precisely identified losses. Both are legitimate upper bounds;
neither describes a cancellation property of the actual signs.
The elementary complete bound E<<J^2 A^2 K is better than (12), since
A^(14/9)/K>>1 on K/A<=T^(-1/4). Thus this legal BP application gives
no gain after taking the complete cap. It has no failed hypothesis;
its first quantitative failure is the full-residue length and the
completed norm (11), rather than real anchors or unspecified gcds.

This conclusion is about the explicit complete-residue application.
Partitioning the n residues into shorter intervals would introduce
additional norm summations and, away from origin intervals, the gcd
restriction in (4). No free short-variable saving from such an
unperformed application is credited. The paper's other theorems are
outside this bounded two-theorem audit.

### 3.4 Complete attempt for MQW, including every excluded block

When (k,q)=1, a change of unit variable gives
S(k,n;q)=sqrt(q) Kl2(kn;q). Thus (9), on that cofactor subset, becomes

    q^(-1/2)sum_(k,n mod q) z_k B_g(n) Kl2(kn;q).       (13)

The condition (k,q)=1 is essential for this identity. For example,
the alternative completion q^(-1/2)sum_n Kl2(m k n;q)e(-n/q)
equals e(mk/q) on units and equals zero when (mk,q)>1. It cannot
represent the omitted nonunit sector. That sector will be retained
in the complete fallback, not silently declared negligible.

Take q larger than twice the largest cofactor, so that the original
k labels lie in[1,M], M=ceil(2K), without residue folding. Use H=q
and t=1 in (5). With fixed endpoint constants understood, its
conditions include

    K^(7/5) q<q^(3/2),  Kq<=q^(5/4),
    hence K<<q^(1/4).                                  (14)

The latter is the stronger power restriction. Reversing M and H
would instead require K>>q^(3/4) and K<<q^(1/10), so it does not
repair this full-residue application. If q is comparable to or below
K, residue folding to lengths q,q also fails the displayed MQW
hypotheses for large q. Bounded moduli are paid trivially.

For a necessary-condition-compatible example take
N~T^(2/3), D~T^(2/15), v~T^(13/125). Then A~T^(6/5),
K~T^(8/15). A stratum q~A fails (14): 8/15>3/10.
This is a failed hypothesis on a permitted parameter band, not an
assertion of actual high points or unit-anchor density in that band.

Even on the eligible primitive-cofactor sector, inserting (10) and
the q^(-1/2) of (13) in (5) gives the full bound

    <<_epsilon q^epsilon sqrt(mu_g)||x_g||_2||z||_2
       [q^(2/3)+K^(19/50)q^(2/5)+K^(5/16)q^(31/64)].    (15)

For K<<q^(1/4), the first term dominates in power and already exceeds
sqrt(K). In the unexcluded worst residue multiplicity mu_g=J_g,
this is worse than the elementary row estimate
sqrt(J_g K)||x_g||_2||z||_2. A smaller actual multiplicity can improve
a particular norm, but no required uniform actual multiplicity saving
has been established here. Fixed-a masks and smooth factors have the
already proved prices, and do not shorten the full n variable.

To close the entire application honestly, partition into legal
primitive-cofactor blocks, all nonunit-cofactor blocks, q=1, and
all remaining ineligible q/K ranges. For the first group take the
smaller of (15) and its elementary bound. Pay every other group by
the elementary bound. Their gcd strata partition the original j's;
they do not create extra copies of actual coefficients. Summing their
pointwise absolute weights, then all odd a, proves for the WHOLE
energy E<<J^2 A^2 K. No exceptional support is left unpaid. Thus the
complete capped MQW application proves no improvement. The first
failed hypothesis is (14) on general permitted scales; even where
that is met, (15) does not close the uniform signed target.

### 3.5 All aliases and false stronger arbitrary-row certificates

Neither (6) nor (9) deletes a modular alias: both are exact finite
identities, with the residual retained through its entire convergent
series. Bounds (12)--(15) are uniform norms for this exact kernel.
They therefore pay both original sine-product branches, but may lose
their cancellation. In particular, replacing (2) by a stronger
arbitrary-complex-row estimate can be false even when its real sine
restriction is harmless.

The following control was suggested by the conductor and independently
checked here. Set N~T, D~T^(1/4), A~T^(5/4), K~T^(3/4),
v=T^(13/125). Fix one odd a0~A. Choose J~T^(1/2) distinct integers
q_j in a short interval around T^2/a0, and put
M_j=a0 q_j, R_j=sqrt(M_j). There are enough such integers, since
T^2/a0~T^(3/4). These radii lie in[T/2,2T] and their consecutive
spacing is comparable to a0/T~T^(1/4), greater than N^(-1/2).

In the unmasked matrix with rows (j,a) and columns k, the J rows
at a=a0 of e(M_j k/a) are all identically one. Hence its operator
norm squared Lambda^2 is at least c J K. A blanket sufficient
complex-row certificate of the proposed scale

    Lambda^2 <= C_epsilon[T^(rho+epsilon)K
                                      +J v^2 T K/A]            (16)

cannot hold for this separated-anchor class: divide by J K to get
on the right O(T^(rho-1/2+epsilon)+T^(-21/500)), tending to zero.
The construction is exact; no numerical experiment is involved.

At the same selected rows, sin(2 pi M_j k/a0)=0. Moreover the
construction does not establish |H(R_j)|>v or identify the actual
sigma_j, and the actual vector uses every a with its original mask
and character. Thus (16) is refuted ONLY as an enlarged arbitrary-row
complex certificate. It is not a counterexample to (3), to its real
kernel, or to the physical high-point problem. It also explains why
cheap rounding alone is not a sufficient strategy result.

Nor does keeping a sine by itself repair a uniform arbitrary-row
certificate. As a further conductor-suggested algebraic control, take
an integer r nearest a0/(4K) and replace M_j by a0 q_j+r. Separation
and rounding remain as before, while all the selected sine rows are
the identical sequence sin(2 pi r k/a0). On integer k in[K/2,K],
r k/a0=k/(4K)+O(K/A), so their squared sum is at least cK for large
T. The corresponding REAL arbitrary-row norm squared is again at
least c J K, contradicting(16) at the same powers. This still uses
a vector supported at a single a and does not establish the actual
high-point condition. Consequently preserving both the real pairing
AND the full actual character/anchor coefficient vector matters;
pairing alone has not supplied a gain.

### 3.6 Original normalization, all blocks and the better fallback

The reviewed219 identity gives Q=||b0 V+error||_2^2, where E=||V||_2^2.
Its complete squared error is at most
T^(-221/2625+epsilon) times the original absorption allowance
P0=J^2 v^2 N^(3/2)/(64K). Original and transformed diagonals remain
distinct; b0^2 J A K=JN is the correct transformed diagonal scale.
The uniform sharp endpoint transform itself has been independently
reviewed, as recorded in the exact dependency hashes below.

The capped source output restores to

    b0^2 E << J^2 T sqrt(N) K,
    (K/N^(3/2)) b0^2 E << J^2 T K/D.                  (17)

Fixed original constants do not affect the power comparison.
The raw BP output (12), before capping, would instead restore to
T^epsilon J^2 T^(23/9)N^(7/9)D^(-23/9). It is worse throughout
the present range. All factor, norm and reconstruction costs are
therefore included before comparing with v^2.

The already reviewed219 joint modular count is a better complete
fallback than (17):

    E <<_epsilon T^epsilon J^2 A^2 min(D,K),
    b0^2 E <<_epsilon T^epsilon J^2 T sqrt(N) min(D,K),
    restored cost <<_epsilon T^epsilon J^2 T min(D,K)/D. (18)

On D<=sqrt(N), it requires v^2 of order T for absorption, leaving
power99/125 at the retained minimum level. This diagnoses an upper
certificate; it is not a signed-energy lower bound. The separate219
inverse-frequency improvement also remains paid, but its capped
oscillatory remainder is still
J^2 T^epsilon min(sqrt(N),T^(13/55)D^(34/55)); at the compatible
scales in Section3.4 it exceeds v^2 by T^(457/4125+o(1)).
Neither of the new source applications removes that complete remainder.

Every N,D rectangle, partial top interval, K=1 case and actual star
is included above. On the complete physical wave, the high-event
inclusion sums all O(log^2 T) rectangles at level V/(2L). The full
tail n>T^(3/2) is O_M(T^-M) by the actual Schwartz factor. Thus no
unbalanced box, mixed-block event or far tail is silently discarded.

### 3.7 Restored moment and full-goal scope

Without (3), the accepted complete distribution and ceiling give

    M12(B_T) <<_epsilon T^epsilon
       [W^10+T W^(20/13)+V0^10+T V0^(20/13)]
       <<_epsilon T^(10 beta+epsilon),
    W=T^(beta+epsilon), V0=T^(13/125),
    beta=(50 sqrt(1717)-297)/13762.                     (19)

All lower layer-cake boundaries are retained. If (3) were proved,
the existing complete transfer would give exponent
113/125+42rho/13=29/25, and pointwise exponent102/325. The present
source audit proves neither improvement.

All other full-proof frontiers remain separate and open:

| Frontier | Complete obligation still required |
|---|---|
| HARD M1 | Entire original signed chi4 cone, including every small-t/large-G range, at L^(3/2). |
| SMOOTH M1 | Independent original smooth residual with its complete critical saving. |
| M2 TOP | Entire complement with one outer real part at L^2 and literal endpoints. |
| M2 BAL | Full sum over G of G P_G at L^(3/2), with original signs and symbols. |
| M2 UNBAL | Actual chi4(h) joint-symbol phase e(sqrt(X h k)), K=XL/D^2, K/L>16, at (LK)^(3/4). |
| Total-M1 GAR | All M2 inputs and uniform endpoint restoration. |
| Whole moments | A sufficient unbounded sequence of fixed even orders, rather than a single p=12 result. |

The UNBAL row uses the authoritative graph node
M9-M2-smooth-unbalanced-three-quarter-estimate. The checkpoint217
summary table transcribed both K and the phase incorrectly. The
conductor's exact correction artifact, authorized as additional context
after this report's first freeze, supplies the forward reconciliation;
the closed217 checkpoint remains unchanged. This correction introduces
no new estimate or graph change.

These two fixed-modulus theorem applications do not supply the missing
full maps on those parents. For the full quarter goal the retained
sufficient family is, for an unbounded sequence of fixed even p,
Q_p=floor(T^(1/p)) and the one-sided signed estimate
I_p(T,Q_p)<=C_(p,epsilon)T^(5/4+epsilon). With the reviewed same-order
absorption and head cost it yields exponent1/4+7/[8(p+1)]. The
premises remain unproved; p growing with T is not asserted. No finite
twelfth-moment milestone substitutes for that full goal.

## 4. First doubtful or unproved step

The first unproved target step is still the complete real estimate(3),
with actual high-point alignment, both modular signs, all aliases,
literal stars and every rectangle. The exact rounding, completion,
Parseval multiplicity and mask prices above do not prove it.

For BP the explicit application is legal, but (11)--(12) lose too much
after the full n completion and a reconstruction. For MQW the general
complete-residue map first fails its length conditions(14), and its
eligible part has the insufficient norm(15). Claiming a source gain
would require an additional proved estimate for the actual structured
completed coefficients or a different fully costed source application.
None is supplied or assumed. The bounded audit stops at these failures.

The refutation of(16) must not be promoted into a refutation of(3).
It identifies an invalid stronger interface after the actual coefficient
restriction is lost; the shifted version shows that merely retaining
a sine does not rescue arbitrary combined-row coefficients either.

## 5. Required controls and outcomes

- **Current primary versions: checked.** On2026-09-28 the primary
  [BP record](https://arxiv.org/abs/2607.24311v1) identifies v1 dated
  2026-07-27, and the primary
  [MQW record](https://arxiv.org/abs/2511.07550v1) identifies v1 dated
  2025-11-10. The observed histories contain those versions; neither
  selected record is marked withdrawn. The MQW title includes
  “moments of twisted L-functions.” The bounded search covered these
  author/identifier queries and current reciprocal/large-sieve and
  Kloosterman queries. Exactly the two Theorem1.1 statements were
  audited; no claim of exhaustive literature coverage is made.
- **Exact theorem hypotheses and complete kernel map: checked for
  the stated limited conclusions.** BP has an actual legal map with
  H=q, origin intervals, t=1, all gcd strata and residue zero. MQW
  has a legal map only on the specified unit and length sector;
  every complement is explicitly paid by the complete fallback.
- **Coefficient norms: checked.** The norm is(10), including mu_g,
  and not an assumed square-root norm. Rounding and the actual smooth
  coefficient cost O(1) product mass, the row stars logarithms, and
  the a sum its full triangle cost. Separate j/a hypotheses are not
  upgraded to arbitrary combined rows.
- **All aliases and endpoints: checked.** The exact real identity(2)
  keeps difference and sum aliases. The modular completions are exact;
  no n residue, physical tail, singleton or stationary half-value is
  removed for convenience.
- **Actual versus enlarged scope: checked.** The physical sigma_j,
  chi4(a) and Psi occur unchanged before each stated norm enlargement.
  The integral-row construction has vanishing sine rows, while its
  shifted version has identical nonzero sine rows. Both refute only
  an arbitrary-row certificate; actual high-point membership and the
  full actual coefficient vector are not supplied by either control.
- **Statement-only control: not claimed by this NONBLIND report.**
  Section3.1 gives an independently checkable operator statement and
  proof. The separate round220 isolated role is the designated blind
  gate; its report has not been read or used here.
- **All frontiers, complete exponent restoration, unbounded fixed
  order: checked as retained open obligations.** Equations(17)--(19)
  pay all blocks and keep the best supported moment power. Neither
  fixed source theorem nor the conditional29/25 target proves quarter.

All controls here are algebraic or exact source/provenance checks.
Zero mathematical experiments were performed or planned; analytical
effort exceeds95 percent. A GREEN control verdict certifies the
stated limitation and its scope, not the missing signed estimate.

## 6. Dependencies and exact artifacts used

Only the brief's allowed context, the two linked primary sources, and
the subsequently authorized normalization correction artifact below
were read for this task. The conductor supplied both arbitrary-row
diagnostics in Section3.5; their derivations were checked here rather than
treated as an independent source. No current sibling report, isolated
packet, new round, or successor design was read. Existing218--219
history is disclosed reuse, not statement-only isolation.

Exact SHA256 snapshots:

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/active_campaign.yml | a3bbd8a17eeb5e5b492f0bccf115332823dfe4d1a6c748c595dd0fee5b286e2b |
| strategy/round220_full_goal_arithmetic_source_review.md | 043f5629f643064c5597a92b7005b7596de11264bdb9d2a14bdc2d1a20857162 |
| strategy/gauss_circle_strategy_review_2026-09-23.md | 0729f1d9c596867e7a06bdcd096847b32e6747653235706b01275a153bd617c6 |
| strategy/gauss_circle_strategy_checkpoint_round217_2026-09-28.md | 39054e4123c11b85e55d9146794cfdd7453915ebefd8a1286763e08b4ecabcd2 |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| proofs/kernels/gc_complete_distinct_radical_moment_reduction.md | d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee |
| rounds/codex-managed/gc-complete-anchored-divisor-energy/synthesis.md | 4515ccc38fecea9d486df9663f2717c4fcbf508f85a446229467d5a4e31b5711 |
| rounds/codex-managed/gc-complete-anchored-divisor-energy/reports/joint_cofactor_dispersion.md | cbb7e8de456bb37c871eafaf21ffb4ecedeb36e7aac50b1719275d13cb1fef81 |
| rounds/codex-managed/gc-complete-anchored-divisor-energy/reviews/independent_dispersion_review.md | 45f3b7c76a1297730ebc142ec0f98e2fd35635915a84fd278289cfee12e8b184 |
| rounds/codex-managed/gc-full-source-method-review/reports/bilinear_arithmetic_sources.md | 26425644ad0a0473b315a61d7499f82f4f053ebd363c15340032dea873ce2978 |
| rounds/codex-managed/gc-full-goal-arithmetic-source-review/briefs/reciprocal_energy_sources.md | 245e640021967c2051a5b7153a25ba9ab73bbf240e60344aa55e5cc5eee6a1f0 |
| rounds/codex-managed/gc-full-goal-arithmetic-source-review/controls/conductor_frontier_normalization_correction.md | 849601b500059325accaba60a559a3e941bf427b11e8cab0bea008ef46a210d8 |

The old bilinear audit is historical method evidence; its source
judgments are not substituted for today's exact theorem text. The219
transform and endpoint price are used together with their exact-hash
independent review. All asymptotic target promotions remain governed
by the unchanged authoritative graph, not by this report.

## 7. Recommended state effect

**No change** to the accepted graph, draft, complete moment exponent,
or full-proof obligations. Retain the exact residual-factor norm
argument and the two fully priced failed source applications as
candidate method evidence, subject to the assigned seam review.
Reject only the blanket arbitrary-row certificate(16), including its
real-sine analogue, on the enlarged separated-anchor class; retain
the actual real signed target(3) with its full character/anchor vector.

Exit label: `strategy_source_review_no_complete_gain`. This source
role stops after this report; it neither starts a new mechanism nor
designs the next round. Any further application must preserve the
paired real structure and prove its entire missing coefficient bound,
instead of crediting real-anchor rounding or a short Kloosterman
subrange as the complete objective.
