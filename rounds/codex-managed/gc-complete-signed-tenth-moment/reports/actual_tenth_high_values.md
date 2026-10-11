# Actual tenth high values: centering and positive arithmetic duality

Campaign: `gc-complete-signed-tenth-moment`. Round: 209.
Task: `actual_tenth_high_values`. Role: discovery; candidate evidence only.
Generated: 2026-09-27T23:06:34+08:00.
Starting graph SHA-256: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Effort: 100 percent analytical; no mathematical experiment or new external source.

## 1. Result: two scoped failures, with the complete missing level estimate

Neither mechanism below proves the complete actual tenth-moment gate.
The two mechanisms tested are (i) removing the discrete arithmetic mean
before analyzing high values, and (ii) exploiting the positive arithmetic
measure in weighted duality. They have different first missing steps.

The mean wave can indeed be removed at the pointwise milestone: its
complete block supremum is at most

\[
 T^{13/84+\epsilon}N^{-29/168}
 \le T^{303/4550+\epsilon}=o(T^{83/650}).                 \tag{1}
\]

However, centering does not give the signed fluctuation estimate. Taking
absolute values of the resulting actual ten-frequency expansion costs at
least \(N^2\), strictly too large on every required open-band scale. This
is an obstruction to that absolute closure, not to the actual signed
moment. The proof uses the actual congruence \(r_2(n)\in4\mathbb Z\), not
an adversarial coefficient example.

Positive arithmetic weighted duality has an exact diagonal of order
\(N\) and coefficient energy of order \(N^{-1/2+o(1)}\). If Cauchy and
absolute correlation estimates discard the fixed smooth coefficient
vector and the location of the positive-radius window, the same
one-interval cost survives. A new estimate must keep an anchored
correlation with that vector, or directly estimate the actual level set.
Even complete removal of the diagonal term would leave a second
unpaid contribution on \(\alpha>99/169\).

A precise sufficient missing inequality is (9) below, on *all* its
levels and *all* the required scales. Neither it nor a sufficient
integrated substitute is established here. The full upper-certificate
deficit remains

\[
 d_B(\alpha)=8\omega(\alpha)-83/65+\alpha/2,
 \qquad \max d_B=7\beta-101/130.                         \tag{2}
\]

## 2. Exact statement and hypotheses

Use precisely the fixed real smooth block and mollifier of the supplied
round-208 bridge:

\[
 \begin{split}
 I&=[T/\sqrt2,\sqrt3T],\quad J=[T^2/2,3T^2],\quad T\ge2,\\
 a_n&=r_2(n)f_N(n),\qquad
 f_N(t)=t^{-3/4}\Psi(\sqrt{t/T})v(t/N),\\
 H_N(R)&=\Re\left(e(-3/8)\sum_n a_ne(R\sqrt n)\right).
 \end{split}                                                   \tag{3}
\]

Here \(v\) is a fixed real nonzero smooth function supported in
\([1,4]\); no global positivity of \(v\) is needed below. The mollifier
has \(\Psi(0)=1\), so \(\Psi(\sqrt{t/T})\) is uniformly positive on
these supports for sufficiently large \(T\). Bounded \(T\) is covered
by enlarging constants. Write

\[
 b=83/650,\quad\gamma=10b=83/65,\quad
 N=T^\alpha,\quad 4b<\alpha<1-2b,
 \quad\omega=\min(\alpha/4,\beta,(1-\alpha)/2),
 \quad q=136/13.                                             \tag{4}
\]

The accepted exact \(\beta=2\theta_{LY}-1/2\) is used only through
the supplied accepted pointwise bound and its audited range. The frozen
moment target is

\[
 M_{10}(H_N):=\int_I|H_N(R)|^{10}dR
 \ll_\epsilon U_NT^\epsilon,\qquad
 U_N=T^\gamma N^{-1/2}.                                    \tag{5}
\]

Let \(D_N(V)=|\{R\in I:|H_N(R)|>V\}|\). Known inputs, with
independently adjustable small epsilon losses, are

\[
 D_N(V)\ll T^{1+\epsilon}N^{-1/2}V^{-2}\quad(V>0),\qquad
 D_N(V)\ll T^\epsilon(V^{-2}+TV^{-q})\quad(V\ge1),
 \qquad \|H_N\|_{L^\infty(I)}\ll T^{\omega+\epsilon}.       \tag{6}
\]

The assigned context establishes the precise shell comparison
\(H_N(R)=R^{-1/2}Z_N(R^2)+E_N(R)\), with
\(E_N\ll T^{-1/2+\epsilon}N^{-1}+O_A(T^{-A})\). It is used
with its complete centered shell, variable width and every shell term;
no separately selected arithmetic arm is substituted.

## 3. Proof and complete cost derivation

### A. The full level ledger before either attempted mechanism

Intersect the two bounds (6) at
\(V_0=N^{13/220}\), retaining the ceiling
\(W=T^{\omega+o(1)}\). Layer cake below \(V_0\) uses the variance
bound down to zero. Above \(V_0\), integrate both terms in the second
bound. This gives exactly

\[
 M_{10}(H_N)\ll T^\epsilon
       \{TN^{-3/110}+T^{8\omega}\}.                         \tag{7}
\]

The two deficits relative to (5) are

\[
 d_A=1-\gamma+(26/55)\alpha,
 \qquad d_B=8\omega-\gamma+\alpha/2.                        \tag{8}
\]

The supplied complete ledger checks \(d_B\ge d_A\) throughout this
band, with maximum (2) at \(\alpha=1-2\beta\). In particular,
\(d_A>0\) precisely when \(\alpha>99/169\). Thus deleting
\(T^{8\omega}\) alone would not prove (5).

There is an explicit complete level version of the missing estimate.
Put \(V_c=T^{9/260}\), so \(V_c^8=T^{\gamma-1}\).
Variance already gives
\(10\int_0^{V_c}V^9D_N(V)dV\ll U_NT^\epsilon\).
A sufficient actual-coefficient input is

\[
 \boxed{D_N(V)\ll_\epsilon U_NT^\epsilon V^{-10}
       \quad\text{for every }V_c\le V\le W,\quad
       T^{166/325}<N<T^{242/325}.}                          \tag{9}
\]

Integrating (9) incurs only \(\log(W/V_c)\); values above \(W\)
are absent. This is a sufficient level estimate, not a claimed necessary
pointwise envelope for the moment. A bound for the weighted integral of
the actual distribution would also suffice.

The two known terms fail (9) in different level ranges. The diagonal
term is small enough only below

\[
 V_d=U_N^{1/8}=T^{83/520}N^{-1/16}.
\]

The bulk term \(TV^{-q}\) is small enough only above

\[
 V_{\rm bulk}=(T/U_N)^{13/6}=T^{-3/5}N^{13/12}.             \tag{10}
\]

When \(\alpha>99/169\), \(V_{\rm bulk}>V_c\) and the
bulk contribution at the variance/bulk crossing \(V_0\) has deficit
\(d_A\). Depending on the scale, \(V_{\rm bulk}\) can exceed
\(W\); its missing part cannot be declared an empty complement.
At the high end of the retained levels the diagonal contribution has
deficit \(d_B\). These formulas price every intermediate level; they
do not assume that actual high values saturate the bounds.

### B. Mechanism one: remove the discrete arithmetic mean

Use the actual identity \(r_2(n)=4\sum_{d\mid n}\chi_4(d)\) and
split

\[
 H_N=M_N+C_N,\qquad
 M_N(R)=\pi\Re\left(e(-3/8)\sum_n f_N(n)e(R\sqrt n)\right),
 \quad
 C_N(R)=\Re\left(e(-3/8)\sum_n(r_2(n)-\pi)f_N(n)e(R\sqrt n)\right).
                                                                  \tag{11}
\]

This retains the fixed arithmetic coefficients and the displaced window
before any generic estimate. For \(R\in I\) one has
\(R\gg T\gg\sqrt N\). The accepted unweighted exponent-pair
estimate from the supplied kernel, followed by partial summation through
the fixed smooth mask, gives

\[
 |M_N(R)|\ll T^\epsilon
 N^{-3/4}T^{13/84}N^{97/168}
 =T^{13/84+\epsilon}N^{-29/168}.
\]

The scaled derivatives and total variation of the mask are uniform for
\(N/T\le1\). Maximizing at \(\alpha=166/325\) gives (1).
This is an allowed reuse of the accepted *unweighted* source estimate;
it is not an exponent-pair assertion for \(r_2(n)-\pi\).

Consequently a proof of (5) with \(C_N\) in place of \(H_N\)
would suffice for the same complete pointwise milestone: local
reproduction applies to \(C_N\), its coefficients have the same
global divisor-bound majorant, and \(M_N\) is already pointwise
smaller than \(T^b\). We do not infer that (1) alone proves a
tenth-moment estimate for \(M_N\), or that a pointwise bound
\(T^b\) would imply (5). The distinction matters because the latter
contains the extra factor \(N^{-1/2}\).

The first attempted arithmetic closure is summation by parts against
the centered summatory function

\[
 A(t)=\sum_{n\le t}(r_2(n)-\pi)
     =P(t)-1+\pi\{t\}.
\]

Since the smooth mask vanishes at the exterior support boundaries,

\[
 \sum_n(r_2(n)-\pi)f_N(n)e(R\sqrt n)
   =-\int A(t)\,d\{f_N(t)e(R\sqrt t)\}.                    \tag{12}
\]

The known pointwise \(A(t)\ll N^{\theta_{LY}+\epsilon}\)
therefore gives only

\[
 |C_N(R)|\ll T^\epsilon
 N^{\theta_{LY}-3/4}(1+T\sqrt N).                          \tag{13}
\]

The phase derivative has cost \(T\sqrt N\); it cannot be dropped
because \(R\asymp T\), far from zero. Bound (13) is worse even than
the coefficient \(\ell^1\) bound. Thus the accepted discrepancy
bound in the coefficient variable does not improve the high-value
problem after an absolute partial summation. The required new input
would be cancellation in the oscillatory Stieltjes integral (12),
uniformly in the actual displaced radius window, sufficient for (9)
or its integrated counterpart. Replacing (12) by its variation does
not supply this input.

There is also an actual-coefficient obstruction to closing (11) by
termwise absolute tenth-frequency integration. Every \(r_2(n)\) is
a nonnegative multiple of four, so

\[
 |r_2(n)-\pi|\ge4-\pi>0.                                  \tag{14}
\]

Choose a closed subinterval of the interior of the support on which
\(|v|\) is bounded below. For sufficiently large \(T\), \(\Psi\)
is bounded below there too. On its \(\asymp N\) integers the
absolute centered coefficients \(c_n=|(r_2(n)-\pi)f_N(n)|\)
are \(\gg N^{-3/4}\); hence \(\sum c_n\gg N^{1/4}\).
Form the positive measure of five-root sums with product coefficients.
Its total mass is at least \(cN^{5/4}\), and its support has length
\(O(\sqrt N)\). Partition into intervals of length \(c_0/T\).
There are \(O(T\sqrt N)\) bins, so the sum of squared bin masses is
at least

\[
 c\frac{N^{5/2}}{T\sqrt N}=cN^2/T.                         \tag{15}
\]

For every same-bin pair, the ten-root frequency difference \(\Delta\)
has \(|\Delta|\le c_0/T\). Taking \(c_0\) small relative to the
fixed window constants gives
\(\left|\int_Ie(R\Delta)dR\right|\gg T\), including
\(\Delta=0\). Therefore the *termwise absolute* ten-frequency
integral is \(\gg N^2\). The same selected five-plus/five-minus
part occurs, up to a fixed \(2^{-10}\) factor, in the real cosine
expansion. No within-bin phase is silently replaced in a signed sum.

For the original coefficients the same conclusion holds: the accepted
summatory formula gives \(\sum r_2(n)\asymp N\) on a fixed positive
length subinterval, so the original absolute coefficient mass is also
\(\gg N^{1/4}\). Thus this obstruction applies both before and
after centering. Relative to (5), the absolute method has deficit

\[
 2\alpha-(\gamma-\alpha/2)
   =(5/2)(\alpha-4b)>0,                                  \tag{16}
\]

approaching \(38/65\) at the upper required endpoint. The signed
integral may cancel these terms with other terms. Equations (15)--(16)
are **not** a lower bound for \(M_{10}(H_N)\) or
\(M_{10}(C_N)\).

### C. Mechanism two: positive arithmetic weighted duality

Before replacing coefficients by a generic norm, work in the actual
positive measure \(\mu_n=r_2(n)\) on the full fixed ambient interval
\([N,4N]\). If \(R_j\in I\) are high values of the complex wave
\(F_N=\sum\mu_nf_N(n)e(R\sqrt n)\), choose unit numbers \(z_j\)
to align \(F_N(R_j)\). Weighted Cauchy gives

\[
 J^2V^2\le E_\mu
   \sum_{j,k}z_j\overline{z_k}K_\mu(R_j-R_k),\quad
 E_\mu=\sum_n\mu_n|f_N(n)|^2,
 \quad K_\mu(u)=\sum_{N\le n\le4N}\mu_ne(u\sqrt n).       \tag{17}
\]

The real high-value set in (3) is contained in the complex one, so this
is a legitimate upper-bound attempt. It uses actual positive arithmetic
weights; the phases of the fixed real smooth mask have not been
declared arbitrary. The diagonal is exactly

\[
 K_\mu(0)=\sum_{N\le n\le4N}r_2(n)\asymp N,
 \qquad E_\mu\asymp N^{-1/2}                              \tag{18}
\]

for large \(T,N\). Upper estimates follow from the summatory formula
and smooth bounded masks; the lower energy bound follows on a subband
where \(|v|\) and \(\Psi\) are bounded below. In particular the
positive Gram diagonal times energy has size \(N^{1/2}\).
Weighted duality removes no power from the ordinary Gram diagonal.

No estimate for \(K_\mu(u)\) matching the unweighted kernel is assumed.
Granting even perfect offdiagonal control would not remove the positive
diagonal in (17). At separation \(N^{-1/2}\), its one-interval
covering cost has order \(V^{-2}\), exactly the term responsible for
\(T^{8\omega}\). The full number of localization intervals must
still include one when the formal localization length exceeds \(|I|\).

There is a precise informational loss. After Cauchy, (17) depends on
the coefficient vector only through \(E_\mu\), and on the evaluation
points only through their differences. Translating every point by
\(R_*\) leaves the right side unchanged. But the actual wave has a
distinguished unmodulated real coefficient vector and the problem fixes
\(R_j\asymp T\), separated from its origin peak. That distinction
is erased by a difference-kernel argument with only the energy input.

For example, the modulated vector
\(|f_N(n)|e(-R_*\sqrt n)\) has exactly the same energy and difference
kernel and has an aligned peak of order \(N^{1/4}\) at \(R_*\).
The peak has width a fixed small multiple of \(N^{-1/2}\), since
all its positive summands remain aligned to within a fixed angle.
It is not an actual arithmetic counterexample: it merely
demonstrates that the summaries retained after Cauchy cannot distinguish
the forbidden modulation from the actual vector. Positivity of
\(r_2\) in the Hilbert-space measure does not repair the information
discarded from that vector.

A valid improvement would therefore require a bound for the projections
of the *fixed* vector \(f_N\) onto the family
\(e(R_j\sqrt n)\), retaining \(R_j\in I\), rather than only an
operator norm of their translation-invariant Gram matrix. A concrete
complete required projection estimate is exactly the actual level-set
bound (9), or a weaker estimate whose tenth layer-cake integral is
\(O(U_NT^\epsilon)\). That is unproved. An improved difference
kernel alone must also be priced against the bulk obstruction (10);
one cannot stop at deleting the diagonal.

### D. Restored shell, endpoint and sharp reconstruction costs

For either actual block, the supplied bridge gives

\[
 M_{10}(H_N)\ll T^{-6}K_{10}(N)
       +T^{-4+\epsilon}N^{-10}+O_A(T^{-A}),
 \quad
 K_{10}(N)\ll T^6M_{10}(H_N)
       +T^{2+\epsilon}N^{-10}+O_A(T^{-A}).                  \tag{19}
\]

These follow from \(dx=2R\,dR\), \(R\asymp T\), and the full
tenth power of the error; no large supremum is multiplied into it.
Thus (5) corresponds to \(K_{10}\ll T^{473/65+\epsilon}N^{-1/2}\).
For centered blocks, (19) is not asserted with the unmodified shell;
instead, the conditional pointwise route after (11) uses Fourier
reproduction for \(C_N\) and separately the explicit mean bound (1).

Reproduction on the strictly larger window \(I\) retains its exact
factor \(N^{1/20}\), so (5), if proved, gives
\(N^{1/20}U_N^{1/10}=T^b\). The off-window tail uses the global
coefficient bound and the positive distance from
\([T,\sqrt2T]\) to \(I^c\). The lower complementary blocks
\(N\le T^{4b}\) use \(N^{1/4}\), and the upper blocks
\(T^{1-2b}\le N\le T\) use \((T/N)^{1/2}\). Their equality
endpoints, the singleton, the full \(N\ge T\) tail and all logarithmic
block costs are those paid in the supplied bridge. Sharp reconstruction
then costs \(\sqrt R\) and \(O(T^{1/2+\epsilon})\), yielding only
the conditional exponent \(102/325\). Neither attempted mechanism
provides its missing premise.

## 4. First doubtful or unproved step

For mechanism one, the first unproved step is an actual signed bound on
the centered oscillatory Stieltjes integral (12), sufficient uniformly
for all levels (9) or for its integrated version. Its absolute variation
bound is explicitly (13), and termwise absolute tenth-frequency
integration has the actual obstruction (16). The safe pointwise mean
wave is not the missing arithmetic fluctuation estimate.

For mechanism two, the first unproved step is a displaced-window bound
on projections of the fixed smooth coefficient vector, stronger than
what its energy and the difference Gram matrix alone supply. Neither
arithmetic positivity nor an asserted better unweighted kernel proves
that bound. At the existing moment level the full outstanding profile
is (8), with both terms retained; \(d_A>0\) above \(99/169\) and
the dominating deficit is (2).

These failures concern the stated absolute or information-discarding
closures. They do not disprove (5), rule out an arithmetic weighted
large-values theorem retaining the anchor, or supply a lower bound on
the actual signed moment.

## 5. Control tests and outcomes

- **Actual coefficients:** The mean split uses the actual divisor
  identity; (14) uses the exact lattice-valued property of \(r_2\).
  The positive weighted duality uses \(\mu=r_2\). An arbitrary
  modulation appears only as a control for information lost after
  Cauchy and is not represented as an arithmetic example.
- **Complete scales and levels:** The band is exactly
  \(166/325<\alpha<242/325\). Formulas (8)--(10) preserve both
  original distribution terms, the low-level variance range, all
  intermediate levels, and the supremum ceiling. In particular the
  second obstruction \(\alpha>99/169\) remains explicit.
- **Signed versus absolute:** The lower bound \(N^2\) applies only
  to the termwise absolute frequency expansion. No lower bound for
  the actual tenth moment is inferred from it. Both signs of the real
  cosine are present; the five-plus/five-minus sector is a legitimate
  selected part only of the positive majorant.
- **Exact nonpairing relations:** Pairing is not assumed. For integers
  \(m\), the two multisets
  \((m,m,m,m,m+5)\) and \((m+1,m+1,m+1,m+1,m+1)\) have the same
  sum and are distinct. Squaring their entries gives a nonpairing
  ten-root relation with positive actual \(r_2\) coefficients.
  For large \(m\) all entries fit into any fixed interior smooth
  subband around their scale. This is a control against pair-only
  reasoning, not an estimate of the total exact mass. The bin proof
  includes exact and nonexact relations without discarding either.
- **Real endpoints:** All integrals, covering arguments and partial
  summations permit real \(T\) and real radius endpoints. Exterior
  support boundaries vanish for the smooth finite block. The sharp
  reconstruction includes inclusive circle jumps through its stated
  error.
- **All costs restored:** The Stieltjes phase-derivative cost,
  positive diagonal, localization ceiling, \(N^{1/20}\)
  reproduction factor, \(T^6\) shell conversion, every complement
  and sharp error are explicit. No fresh external source is imported.
- **Full-quarter scope:** Even success at (5) gives only
  \(102/325\). This report does not establish it or close M1, M2,
  endpoint uniformity, or the quarter theorem.
- **Statement-only control:** This claimant report does not claim
  independent validation. Its finite statements (14)--(18), mean-wave
  exponent and full level ledger are suitable for the conductor's
  separate seam check. No other task's report or isolated packet was
  read, and no numerical test was used as proof.

## 6. Dependencies and exact artifacts used

Read only the assigned brief and the following permitted context:

- `protocol.md`.
- `state/proof_obligations.yml`, including the accepted
  `GC-complete-square-root-large-values-moment-bound`,
  `GC-external-Li-Yang-theta-star`, its narrow source-audit status,
  and the open statuses of GC-target, M9-M1 and M9-M2.
- `state/active_campaign.yml` (round 209).
- `strategy/round209_complete_signed_tenth_moment_attack.md`.
- `strategy/gauss_circle_strategy_checkpoint_round208_2026-09-27.md`.
- `rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/controls/conductor_sixth_moment_power_ledger.md`.

The conductor's two in-round messages highlighted the threshold
\(\alpha=99/169\) and the elementary property (14); both are
derived explicitly here. No source named inside a permitted artifact
was separately read. The only external estimate used is the already
accepted unweighted exponent-pair specialization in the supplied
kernel. Exact coefficient centering, weighted Cauchy, the positive
binning argument and all displayed algebra are direct derivations.

## 7. Recommended state effect

**No change** to the accepted proof graph, proof draft, pointwise
benchmark or complete moment bound. Retain this report as a scoped
actual-method no-go with precise residual (9), not as an additional
accepted arithmetic estimate. The discrete mean wave is pointwise safe,
but its removal has not priced the centered high values. Positive
arithmetic duality without a bound retaining the fixed coefficient
vector has not repaired either missing contribution. Stop this assigned
task here; no successor or shared-state edits are made.
