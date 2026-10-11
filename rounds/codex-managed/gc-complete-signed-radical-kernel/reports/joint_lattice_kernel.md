# Round218 joint Gaussian-lattice kernel: complete cost and scoped no-go

Campaign: `gc-complete-signed-radical-kernel`.
Task: `joint_lattice_kernel`. Role: discovery, selected context, NONBLIND.
Generated: 2026-09-28. Starting graph SHA-256:
`a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
This report is candidate evidence only. Analytical/algebraic effort: 100%;
mathematical experiments: zero; new external theorem imports: zero.

## 1. Result: a complete quantitative no-go for one joint-Poisson closure

The actual complete twelfth-moment target remains unproved. Joint Poisson
summation in the twelve Gaussian-integer variables does not supply a
dimension gain merely by raising the ambient dimension to 24 or, with the
common radius, 25. At a stationary point its Hessian has rank 12 with the
radius fixed and rank 14 when the radius is included. Its stationary
manifold then has dimension 11, not zero. All these assertions retain the
actual cosine phases.

More decisively, define the following precise positive certificate. Apply
Gaussian-lattice Poisson to the COMPLETE real series, expand its twelfth
power, integrate each complete dual twelve-tuple over the original radius
window, and only then take its absolute value. For the fixed smooth
extension specified below this certificate, denoted `P_T`, satisfies

    c T^7 <= P_T <<_epsilon T^(7+epsilon).                 (1)

This includes the full original series before any dyadic separation, all
cosine signs, all mixed blocks and its entire Schwartz tail. Thus allowing
cancellation inside each joint oscillatory integral, including cancellation
between its different radial scales and signs, still does not make this
particular absolute dual-tuple closure remotely target-sized. Equation (1)
is not a lower bound on the signed moment or on I12.

For comparison, on an actual smooth lattice annulus |m|~L with
1<=L<=c sqrt(T), the corresponding certificate obeys

    c T^7 L^(-12) <= P_(T,L) <<_epsilon T^(7+epsilon)L^(-12).
                                                               (2)

Its lower bound uses exact integer dual multiplicities, not an assumed
asymptotic for a thin annulus. At L=T^(1/3), its cost is at least T^3.
The already known second-moment improvement to the elementary complete
Poisson closure is reproduced below and gives only T^(7/3+epsilon).
The accepted204 full estimate T^(1+epsilon)+T^(10 beta+epsilon) remains
stronger; none of these calculations improves its exponent.

The claim is deliberately limited to the specified transform followed by
absolute values on complete dual tuples. It does not reject a signed dual
correlation theorem, a different smooth interpolation, the target I12,
or the quarter theorem. In particular, it does not rule out subtracting
the already-paid216 head before a different, correctly justified transform.
The annular result concerns the full actual annular coefficients; no
distinct-squarefree mask is silently inserted into that certificate.

## 2. Exact statement, hypotheses and actual arithmetic binding

Use exactly the mollifier and window in the accepted216 kernel:
rho is a fixed nonnegative real radial smooth function supported in the
unit disk with integral 1; Psi(s)=rho-hat(s e1); and w is nonnegative,
smooth, supported in [1/2,2], and equals 1 on
[1/sqrt(2),sqrt(3)]. Write e(t)=exp(2 pi i t). For real T>=2,

    B_T(R)=sum_(n>=1) r2(n)n^(-3/4)Psi(sqrt(n/T))
                                      cos(2 pi R sqrt(n)-3 pi/4).

Fix once and for all a smooth real chi on [0,infinity) with
0<=chi<=1, chi=0 for r<=1/2, and chi=1 for r>=1. Set

    g_T(x)=chi(|x|)|x|^(-3/2)Psi(|x|/sqrt(T)),
    f_(T,R)(x)=g_T(x) cos(2 pi R|x|-3 pi/4),
    F_T(R,kappa)=integral_(R^2) f_(T,R)(x)e(-k.x)dx,
                                                     where |k|=kappa.

The last expression depends only on kappa and is real. At every nonzero
integer lattice point chi=1. At zero the extension vanishes. Consequently

    B_T(R)=sum_(m in Z^2) f_(T,R)(m)
          =sum_(k in Z^2) F_T(R,|k|).                    (3)

This is the exact identity r2(n)=#{m in Z^2:|m|^2=n}. It makes no
smoothness assumption about r2, a squarefree mask, or a divisor mask.
For each fixed T and R the functions in (3) are Schwartz, so elementary
smooth Poisson applies. On the compact R window the Fourier sums and all
products converge absolutely and uniformly. Define

    K_T(k_1,...,k_12)
      =integral w(R/T) product_(j=1)^12 F_T(R,|k_j|)dR,
    P_T=sum_(k_1,...,k_12 in Z^2) |K_T(k_1,...,k_12)|.

Then, with every tuple ordered,

    M12(B_T)=sum_(k_1,...,k_12) K_T(k_1,...,k_12) <= P_T. (4)

The absolute values in P_T occur AFTER the full R integration and AFTER
the two real cosine branches and all original radial scales have been
combined inside each F_T. Equation (1) concerns exactly this certificate.

For (2), choose a fixed nonzero v>=0 smooth and supported in (1,2), and
replace g_T by

    g_(T,L)(x)=|x|^(-3/2)Psi(|x|/sqrt(T))v(|x|/L).

Define B_(T,L), F_(T,L), K_(T,L) and P_(T,L) in the same way.
The lower bound is uniform for sufficiently large T and
1<=L<=c sqrt(T), where c>0 is a fixed small constant ensuring Psi>=1/2
on the support. Constants may depend on chi, v, rho and w.

The transfer back to I12 uses only the paid216 equivalence. With
Q=floor(T^(2/5)), its head costs T^(15/13+epsilon), and its collectively
repeated-class error costs T^(8 beta-1/5+epsilon), both below T^(29/25).
Thus proving the complete B_T bound would suffice and would be equivalent
at the target power. This report never differentiates the distinct-class
mask. It does not claim that B_T and I12 have an additive approximation
with those same two errors.

## 3. Derivation, all stationary degeneracies, and complete powers

### 3.1 Exact radial transform and the actual odd profile

Angular integration gives, with J0 defined by its angular integral,

    F_T(R,kappa)=2 pi integral_0^infinity
      chi(r)r^(-1/2)Psi(r/sqrt(T))
      cos(2 pi Rr-3 pi/4) J0(2 pi kappa r)dr.             (5)

The elementary angular stationary expansion is

    J0(2 pi kappa r)
       =(pi sqrt(kappa r))^(-1)
                         cos(2 pi kappa r-pi/4)
         + an oscillatory symbol remainder of order (kappa r)^(-3/2).

For completeness, the two stationary angular points are 0 and pi.
Near either, the substitution z=2 sin(theta/2), after translating the
second point, makes cos(theta)=1-z^2/2 exactly. Taylor expansion of the
smooth Jacobian against the damped Gaussian integral gives the two
leading Fresnel factors e(1/8) and e(-1/8), and successive symbol
remainders. On the complement the angular derivative stays away from
zero and repeated integration by parts gives arbitrary decay. Applying
this argument with radial derivatives gives the same symbol estimates
after each fixed number of radial derivatives. It therefore also proves
the uniform, integrated remainder estimates used here; no arithmetic
stationary-phase theorem is imported.

Put

    H_T(u)=integral_0^infinity chi(r)Psi(r/sqrt(T))
                                           sin(2 pi ur)dr/r,
    C_T(u)=integral_0^infinity chi(r)Psi(r/sqrt(T))
                                           cos(2 pi ur)dr/r.

The actual phase shift -3pi/4 is essential. The elementary cosine-product
identity in (5) yields the leading term

    kappa^(-1/2)[H_T(R-kappa)-C_T(R+kappa)],              (6)

not an even positive bump centered at R=kappa. In particular H_T(0)=0.
For R in [T/2,2T] and kappa in [T/4,4T], the full symbol estimates and
radial integration by parts give, for every fixed A,

    F_T(R,kappa)=kappa^(-1/2)H_T(R-kappa)+E_T(R,kappa),
    |E_T(R,kappa)|
      <=C_A T^(-3/2)(1+|R-kappa|)^(-A)+C_A T^(-A).       (7)

In (7) the last arbitrary power can be chosen independently larger than
any subsequently needed power. The counterrotating C_T(R+kappa) is
included in it. To justify the uniform constants, every differentiated
remainder has an integrable radial amplitude bounded by derivatives of
chi(r)r^(-2)Psi(r/sqrt(T)); their L1 norms are uniformly bounded.
The leading counterrotating term has the same property after at least
one integration by parts. Thus the growing smoothing scale incurs no
hidden positive power in (7).

There is also a uniform bound

    |H_T(u)|<=C_A(1+|u|)^(-A).                           (8)

For 0<|u|<1, split the integral at r=1/|u|. On its initial part use
|sin(2pi ur)|<=2pi|u|r. On the remainder integrate once; the boundary
and variation are O(1). In detail, for M>=1,

    integral_M^infinity |d[Psi(r/sqrt(T))/r]| <= C/M,

because |Psi| is bounded and integral|Psi'| is finite. This proves the
uniform tail estimate C/(|u|M). For |u|>=1, repeated integration by
parts proves (8): all positive-order derivatives of chi(r)Psi(r/sqrt(T))/r
have uniformly bounded L1 norm. The same statements hold for negative
u by oddness.

For kappa outside [T/4,4T], radial nonstationary integration gives a
summable bound of arbitrarily small total size. For kappa>=1 one uses
the two angular symbols and |R+-kappa| comparable to T+kappa.
The sole kappa=0 term is handled directly in (5), using J0(0)=1.
All radial derivatives then have uniformly bounded L1 norm after a
sufficient number of differentiations. In particular, for any prescribed B,

    sum_(k:|k| outside [T/4,4T]) |F_T(R,|k|)| <<_B T^(-B)
                                                               (9)

uniformly on the entire R window. The Schwartz tail has not been dropped
at any point.

### 3.2 Stationary geometry before any norm

On arbitrary smooth radial annuli r_j~L_j, expand the original cosine
factors into epsilon_j in {+1,-1}. The joint phase, omitting its constant
cosine multiplier, is

    Phi(R,x_1,...,x_p)
          =R sum_j epsilon_j |x_j| - sum_j k_j.x_j.       (10)

For R>0 and r_j>0, stationarity in x_j requires

    |k_j|=R,     x_j/r_j=epsilon_j k_j/|k_j|.             (11)

Thus no zero dual vector is stationary. All nonzero dual radii must
coincide. At fixed R, each two-dimensional x_j Hessian has one angular
eigenvalue and one radial null direction. Its total rank is p, not 2p.
The ambient fact that the k_j can point in different directions changes
neither rank nor the radial null space; collinearity causes no additional
loss or gain because the x_j occupy separate planes.

Including R adds the equation

    sum_j epsilon_j r_j=0.                               (12)

At a stationary point the angular Hessian is diagonal and nonsingular,
with entries epsilon_j R r_j in angular coordinates. On (R,r_1,...,r_p)
the Hessian has only the R--r entries epsilon_j. It has rank exactly 2.
The full rank is therefore p+2; the nullity in 2p+1 variables is p-1.
At p=12 these numbers are 14 and 11. The stationary value of Phi is zero.
The stationary set is the positive radial hyperplane (12), subject to
the actual annular supports, with the directions fixed by (11).

All-equal signs have no such set. Mixed signs have one only when the
annular intervals permit (12). A uniquely dominant radial scale can make
it empty; comparable scales with six signs of each kind contain full
eleven-dimensional pieces. No saving for the complete moment can be
inferred from the empty sectors while retaining these nonempty ones.
Smooth endpoints have no hard boundary terms; if a stationary set
touches an extremal support endpoint the smooth amplitude vanishes there.

For normalized amplitudes of size product L_j^(-3/2), angular integration
contributes one factor (T L_j)^(-1/2) per variable against its original
area/amplitude factor L_j^(1/2). The remaining size is T^(-p/2).
Integration in the common R and one transverse radial direction costs
at most L_max^(-1), leaving p-1 free radial directions. At equal scales
the joint coefficient size is consequently T^(-p/2)L^(-1), not the
full-rank 2p- or (2p+1)-dimensional guess.

For a nonproduct smooth amplitude on the product annulus, the same
angular proof and independent radial integrations by parts apply. Constants
depend on finitely many derivatives after rescaling x_j by L_j and R by T.
Changing such an amplitude does not change the phase Hessian. This
statement cannot be applied to a squarefree distinctness indicator:
that indicator has no such smooth seminorm bound. The paid216 transfer
is why no such application is needed here.

### 3.3 Complete unblocked certificate: upper bound with integer multiplicity

The number of actual integer dual vectors in
|kappa-R|<=a+1, with kappa~T, is at most

    C_epsilon T^epsilon T(a+1).

Indeed their integer squared norms lie in an interval containing
O(T(a+1)+(a+1)^2+1) integers, and each has multiplicity r2(q)<<q^eta.
Use dyadic distance bands in (7)--(8) and choose the decay order large.
The zero and distant dual terms are paid by (9). This proves

    sum_(k in Z^2)|F_T(R,|k|)| <<_epsilon T^(1/2+epsilon).

Since the actual window has length O(T), Tonelli and the triangle
inequality AFTER each joint integral give

    P_T <=integral w(R/T)(sum_k|F_T(R,|k|)|)^12 dR
         <<_epsilon T^(7+epsilon).                      (13)

The exponent epsilon is renamed after dividing it among twelve factors.
There is no assumption that a thin shell contains its area prediction.

### 3.4 Complete unblocked certificate: lower bound after all sign cancellation

Define the improper integral

    H_infinity(u)=integral_0^infinity chi(r)sin(2pi ur)dr/r,
                                                       u!=0.

The tail bound following (8) proves H_T(u)->H_infinity(u) for every
u!=0. Equations (8) and dominated convergence give convergence in L^12(R).
The limit is not zero. The elementary damped identity

    integral_0^infinity exp(-a r)sin(b r)dr/r=arctan(b/a)

follows by differentiating in b and integrating back from b=0.
Letting a decrease to zero, with the same tail integration by parts,
shows that for u>0

    H_infinity(u)=pi/2-
            integral_0^1 (1-chi(r))sin(2pi ur)dr/r=pi/2+O(u).

Hence A0:=integral H_infinity(u)^12 du is finite and strictly positive.
Translation continuity in L^12, Holder, and H_T->H_infinity imply that
there are fixed delta>0 and T0 such that, for all T>=T0 and all
|h_j|<=delta,

    integral product_(j=1)^12 H_T(u-h_j)du >= A0/2.       (14)

This uses the complete real H_T, including its changing sign. It does
not replace it with a positive bump. To see uniformity explicitly, the
difference between either product and H_infinity(u)^12 is bounded in L1
by the sum of the twelve L^12 differences times uniformly bounded
eleven-fold norm products.

Take twelve actual dual vectors whose radii lie in one half-open interval
of width delta inside [T,3T/2]. Choose one radius kappa0 as origin for
u=R-kappa0. On all bounded u the physical weight is exactly 1 for large T.
Its omitted tails have arbitrarily small integrals by (8), uniformly in
kappa0. Inserting (7) and (14) gives

    K_T(k_1,...,k_12) >= c T^(-6).                       (15)

Every error product has at least one extra T^(-1) relative to the main
product; Holder and the integrable envelopes in (7)--(8) make their total
O(T^(-7)), plus an arbitrarily small tail. Thus (15) is a lower bound for
the exact joint coefficient after all twelve cosine signs have combined.
More explicitly, on the full R window the localized error in (7) has
L^12 norm O(T^(-3/2)), while the leading factor has L^12 norm O(T^(-1/2)).
The uniform O(T^(-A)) remainder has norm O(T^(1/12-A)) and is chosen
smaller. A bare pointwise O(T^(-3/2)) error integrated over a length-T
window would not establish this conclusion; the mismatch decay is used.

Partition [T,3T/2] into O(T) half-open bins of width at most delta.
Let b_l be the EXACT number of integer vectors k in bin l. The elementary
unit-square disk comparison, including the real endpoints, gives

    sum_l b_l = #{k:T<=|k|<=3T/2} as comparable to T^2.

Holder for the nonnegative finite list b_l gives

    sum_l b_l^12 >= (sum_l b_l)^12/(number of bins)^11
                   >> T^13.                            (16)

Each same-bin ordered twelve-tuple has the positive coefficient (15).
Multiplying (15) and (16) proves P_T>=cT^7. No distinctness of dual
vectors is required or imposed by (4), and each integer vector is counted
with its true multiplicity. No unproved short-annulus counting estimate
is hidden in this argument. Equations (13)--(16) prove (1).

The chosen chi specifies a legitimate exact extension; its values between
integer radii are part of the named certificate. The proof does not claim
that every conceivable interpolation or every signed Poisson method has
this same lower bound.

### 3.5 Unequal blocks, annular sharpness and the complete classical fallback

For the annular amplitude, the same calculation gives

    F_(T,L)(R,kappa)
       =kappa^(-1/2) H_(T,L)(L(R-kappa))+E_(T,L),
    H_(T,L)(s)=integral_1^2 t^(-1)v(t)Psi(Lt/sqrt(T))
                                                   sin(2pi st)dt,
    |E_(T,L)| <= C_A T^(-1/2)(TL)^(-1)
                       (1+L|R-kappa|)^(-A)+O_A(T^(-A)). (17)

All seminorms of H_(T,L) are uniform. For L<=c sqrt(T), its derivative
at zero is bounded below by a positive constant, so its L^12 norm is
uniformly bounded below. Smooth bounded support also gives uniform
translation continuity. Thus the proof of (15) now yields

    K_(T,L)(k_1,...,k_12) >= c T^(-6)L^(-1)

when all twelve radii fall in a bin of width delta/L. There are O(TL)
bins and still comparable to T^2 integer dual vectors in total. The
number of same-bin ordered tuples is at least
T^24/(TL)^11=T^13 L^(-11). This proves the lower half of (2).

For unequal scales, and dual radii in [T/4,4T], the product kernel is
bounded by

    C_A T^(-6) integral_R
                       product_j(1+L_j|R-kappa_j|)^(-A)dR.
                                                               (18)

The same bound holds for a nonproduct normalized smooth amplitude,
with its finite rescaled seminorms included in the constant. With i a
largest-scale index, allocate sufficiently many powers in (18) and use
the triangle inequality for |kappa_j-kappa_i|. One obtains

    C_A T^(-6)L_i^(-1)
          product_(j!=i)(1+L_j|kappa_j-kappa_i|)^(-A'),    (19)

for any prescribed A', by initially choosing A large enough. This is a
uniform mismatch estimate; it permits all mixed signs and unequal blocks.
It need not be sharp on sign patterns for which (12) is impossible.

For 1<=L_j<=T^(3/4), integer squared norms give the shell bound

    sum_k(1+L_j||k|-kappa_i|)^(-A')
                         <<_epsilon T^epsilon T/L_j.

There are O(T^2) possible reference vectors k_i in the central range.
Thus summing (19), including the rapidly decaying noncentral terms, gives

    sum_(k_1,...,k_12)|K_(T;L_1,...,L_12)|
          <<_epsilon T^(7+epsilon)/product_j L_j.        (20)

For equal scales, this proves the upper half of (2). The dual-shell
count exactly pays back the apparent saving from the high-dimensional
integral. At the classical transition L=T^(1/3), (2) is T^3.
Equation (1) is stronger as a completeness check: cancellation between
different original blocks is already retained there and still leaves
the named certificate at T^7.

One can improve the elementary complete UPPER estimate by the original
second moment rather than (20). Here are all its costs, to avoid leaving
an unestimated complement. On a smooth dyadic block n~N=L^2,

    sup_(R~T)|B_(T,L)(R)|
          <<_epsilon T^epsilon min(L^(1/2),T^(1/2)L^(-1)).

The first term is the actual lattice L1 bound. The second follows from
(17), actual integer shell multiplicity, and all noncentral errors.
Also

    integral w(R/T)|B_(T,L)(R)|^2dR
                              <<_epsilon T^(1+epsilon)L^(-1)

for L<=T^(3/4). To verify it directly, the coefficient square sum is
O_epsilon(L^(-1)T^epsilon), while distinct frequencies sqrt(n) in this
block are separated by at least c/L. The exact smooth-window Gram
entries decay as T(1+T|sqrt(n)-sqrt(m)|)^(-2). Their row sums are O(T)
because T/L>=T^(1/4). The opposite cosine signs have frequency sums
bounded below and are harmless in the same estimate.
Consequently

    M12(B_(T,L))
       <<_epsilon T^epsilon min(T L^4,T^6 L^(-11)).      (21)

The two expressions meet at L=T^(1/3), with value T^(7/3). For smaller
L the first increases; for larger L the second decreases. A smooth
dyadic partition and the L^12 triangle inequality pay every mixed block
with at most a logarithmic power. The finite n=1 region can be covered
by the same smooth partition at bounded L. Beyond n=T^(3/2), the
Schwartz/divisor L1 estimate is O_A(T^(-A)) for any fixed A. The total
full-series L1 bound is O_epsilon(T^(1/4+epsilon)), so expanding the
difference of twelfth powers pays this omitted tail as O(T^(-B)) after
increasing A. Thus every sign, original harmonic, scale, endpoint and
smoothing tail is included, and (21) gives the complete bound

    M12(B_T) <<_epsilon T^(7/3+epsilon).                 (22)

This reproduces the203 cost and is weaker than accepted204. In particular
the best available complete bound remains

    M12(B_T) <<_epsilon T^(1+epsilon)+T^(10 beta+epsilon),
    beta=2 theta_LY-1/2,

with the inherited qualified theta_LY. Since beta>1/8,
10 beta>5/4>29/25. No complete target power is obtained.

## 4. First doubtful or unproved step

There is no asserted doubtful step in the stated certificate no-go,
subject to independent review of its uniform transform estimates.
The first unproved step toward the research objective is cancellation
BETWEEN distinct complete dual tuples in the exact signed sum (4),
strong enough to reduce its actual moment to T^(29/25+epsilon).
The joint stationary geometry does not estimate that cancellation.

In particular, neither full ambient dimension, angular noncollinearity,
the absence of exact distinct-radical resonances, nor replacing shell
multiplicity by 1 supplies the missing estimate. The last replacement is
plainly false for the actual integer dual lattice. Centering the dual
shell density can make the odd leading profile's area contribution
small, but its complete discrete remainder is still unestimated and may
not be discarded. That would return the already identified203 density
gap. No such free subtraction is made here.

This is a completed diagnosis of one full mechanism, not the proposal
of a smaller unestimated sector. The signed target is retained intact.

## 5. Required controls and outcomes

1. `actual_coefficients`: PASS locally. Equations (3) and (5) use exact
   Gaussian-integer norm multiplicities. The lower certificate uses the
   actual mollifier and actual lattice, with no arbitrary rephasing.
2. `all_distinct_class_masks`: PASS by the paid216 full-moment equivalence.
   Its head and repeated-class errors are explicitly paid in Section2.
   No arithmetic indicator is extended as a smooth differentiable weight.
3. `full_signed_kernel`: PASS for exact identity and scoped failure.
   K_T combines all real cosine signs, all radial scales and the full
   displaced window before its modulus. Its sum is the complete moment.
   P_T is explicitly distinguished from that signed sum and from I12.
4. `joint_stationary_geometry`: PASS analytically, pending independent
   seam review. Fixed-R rank is p; joint rank is p+2; nullity is p-1.
   The actual leading packet is odd and zero at its center. Zero dual
   vectors, all signs, collinearity and common-radius manifolds are priced.
5. `unequal_blocks`: PASS for the stated envelope. Equations (18)--(20)
   retain distinct L_j, reference scale L_max, and all integer shell costs.
   Incompatible radial supports can be better, but the complete bound
   never discards the compatible balanced sectors.
6. `all_harmonics_signs_tails`: PASS. The main no-go uses the untruncated
   B_T. It keeps all harmonics in every squarefree class implicitly through
   the exact lattice identity. Equations (8)--(9) pay the infinite dual
   tails; Section3.5 pays every tail in the fallback estimate.
7. `real_endpoints`: PASS. T is any sufficiently large real number;
   bounded T is absorbed into constants. The actual w is retained.
   Half-open bin conventions make boundary assignment unique. Disk
   comparison is valid at real radii. The floor Q occurs only in the
   accepted216 transfer, with its stated uniform errors.
8. `complete_norm_cost`: PASS. Complete certificate costs are T^7 and,
   annularly, T^7 L^-12; the improved elementary complete moment cost is
   T^(7/3). The accepted stronger exponent 10 beta is still above target.
9. `old_barrier_bypass`: FAIL as a proposed route to a gain, explicitly.
   Joint dimension does not bypass203; full joint dual moduli remain
   expensive. Unlike a bare restatement of scalar Poisson, (1) prices a
   complete joint integral AFTER internal real-sign/block cancellation.
   It adds no estimate to the arithmetic frontier and does not contradict
   the distinct-class certificate obstruction or215 localized-wave limits.
10. `statement_only_control`: PENDING conductor's isolated geometry seam.
    This analyst read no sibling report or isolated packet and claims no
    blind validation. The p=1 fixed-R calculation reproduces the single
    angular curvature and the odd sine packet directly. For joint R,
    p=1 has no positive-radius stationary point; p=2 with opposite signs
    has the required one-dimensional radial stationary manifold.
11. `fixed_order_full_goal_scope`: PASS. Even the unproved twelfth target
    would yield only102/325. No sufficient unbounded-fixed-order moment
    family, M1/M2 parent, GAR parent, endpoint theorem or quarter estimate
    is established here.

These are analytical controls, not numerical tests. The actual positivity
in (15) concerns selected coefficients of a positive upper certificate;
other signed coefficients can cancel them in (4). No lower bound on the
moment follows. No control uses an unsigned-to-signed implication.

## 6. Exact dependencies and artifacts used

Only the assigned context was read:

- `protocol.md`.
- `state/proof_obligations.yml`, inspected particularly for the accepted204,
  accepted216 and accepted217 nodes and the qualified Li--Yang dependency;
  starting SHA-256 as recorded at the head of this report.
- `state/active_campaign.yml`, frozen round218 manifest.
- `strategy/round218_complete_signed_radical_kernel.md`.
- `strategy/gauss_circle_strategy_checkpoint_round217_2026-09-28.md`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.
- `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md`.
- `proofs/kernels/gc_distinct_radical_absolute_certificate_obstruction.md`.
- `rounds/codex-managed/gc-complete-signed-convolution-attack/synthesis.md`.
- `rounds/codex-managed/gc-signed-near-frequency-cancellation/synthesis.md`.
- `rounds/codex-managed/gc-complete-localized-wave-moment/synthesis.md`.
- The task's own generated brief
  `rounds/codex-managed/gc-complete-signed-radical-kernel/briefs/joint_lattice_kernel.md`.

The elementary Gaussian-integer count, r2(q)<<q^eta, smooth Poisson,
angular integral, Gaussian stationary expansion, Holder and integration
by parts are proved or used at their elementary forms above. No new
external arithmetic theorem or unaudited source range is invoked.
The qualified Li--Yang statement enters only through the already
accepted204 comparison and216 transfer, with all its recorded repairs
preserved. This report does not independently reaudit that source.

No sibling report, legacy mutable path, experiment, model assumption,
or successor-round artifact was used. This is the only file written by
this task; proof graph, proof draft, validation matrix and synthesis were
not modified.

## 7. Recommended state effect

`no change` to every open analytic target and accepted exponent. Retain
this as bounded, reviewable evidence for the failed joint-Poisson absolute
closure, subject to an independent exact-hash mathematical/application
seam. Do not promote another reformulation of the original signed target.

The conductor may record the precise certificate limitation after review,
but should not infer that signed Gaussian-lattice methods are impossible.
The full I12 target, its complete equivalent moment, all independent
M1/M2/GAR frontiers and the sufficient unbounded-fixed-order requirement
remain open. This task stops here and designs no successor round.
