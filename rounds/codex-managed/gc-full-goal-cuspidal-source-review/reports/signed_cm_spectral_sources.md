# 1. Result

Round229, campaign `gc-full-goal-cuspidal-source-review`, task
`signed_cm_spectral_sources`, temporary source-auditor role, NONBLIND.
Generated 2026-09-29. Starting graph SHA256:
`a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
Candidate evidence only. Zero experiments.

**No complete signed estimate is imported.** The two selected audits are
Assing--Humphries (AH), Lemma2.4, and Knightly--Li (KL), Theorem7.14.
The first supplies a positive CM majorant, not the exact spectral weight
needed for a signed central-value substitution. The second supplies a
signed Fourier-coefficient trace identity, not a bound for the complete
CM-weighted functional. Its diagonal, continuous term, Kloosterman sum,
test dependence, and Fourier-to-point reconstruction cannot be discarded.

There is a precise no-go for the proposed *inference*: domination of
positive point weights by positive central-value weights does not
transfer cancellation against the surviving complex phase. Class number
one does not repair the missing local identity. This is not a no-go for
Waldspurger, Kuznetsov, spectral reciprocity, or the actual quarter target.

A small useful algebraic audit identity is obtained for the exact oldspace
factor:

\[
 \frac{2}{3+\sqrt2\lambda_f(2)}
   =\sum_{r\ge0}(-1/\sqrt2)^r\lambda_f(2^r).             \tag{1}
\]

Its tail is quantified below. It is not a saving and does not make the
factor interchangeable with one. The first unproved complete inequality
remains (5) below. The report recommends parking the tested direct
CM-majorant import at its first failed premise, rather than declaring a
new complete frontier from an unevaluated trace formula.

# 2. Exact statement, hypotheses, and selected source cards

Use every real \(T\ge2\), \(R\asymp T\), dyadic
\(2\le N\le P<2T^{3/2}\), and the actual fixed signed Schwartz weight.
Put \(A=(1+N/T)^{-J}\),

\[
 g(x)=(x/N)^{-3/4}\Psi(\sqrt{x/T})w(x/N),\quad
 W_h(x)=g(x+h)g(x)e(R(\sqrt{x+h}-\sqrt x)),
\]
\[
 \alpha_h=1-h/(2N),\qquad
 H_h(t)=4\pi\int_0^\infty W_h(hu)P_{-1/2+it}(1+2u)\,du.
                                                               \tag{2}
\]

The smooth zero extension is literal. At \(z_1=i\),
\(z_2=(-1+i)/2\), all cusp functions below have hyperbolic-area norm one.
For \(h=2^kh_0\), \(h_0\) odd, keep

\[
 L_{1,h}=4\sum_{a=0}^{k-2}(-1)^a
       \sqrt{h/2^{a+2}}\lambda(h/2^{a+2}),\qquad
 L_{2,h}=2\varepsilon_k\sqrt{h_0}\lambda(h_0),            \tag{3}
\]

with the first sum empty for \(k<2\), \(\varepsilon_0=1\), and
\(\varepsilon_k=(-1)^{k-1}\) for \(k\ge1\). Define
\(V_q=\sum_{1\le h<2N}\alpha_hL_{q,h}H_h\). The exact primitive form is

\[
 \begin{split}
 D={}&\sum_{f\ {\rm primitive}\ 1,\ {\rm even}}|u_f(i)|^2
       \left(V_{1,f}+\frac{2V_{2,f}^{\rm odd}}
                              {3+\sqrt2\lambda_f(2)}\right)\\
 &+\sum_{f\ {\rm new}\ 2,\ {\rm even},\ W_2=+1}
                  |u_f(z_2)|^2V_{2,f}^{\rm odd}.         \tag{4}
 \end{split}
\]

The complete continuous partner \(E\) has one level-one and two level-two
cusps, width-one incoming normalization, measure \(dt/(4\pi)\), and
\(\eta_t(m)=\sum_{ab=m}(a/b)^{it}\) in (3). The reviewed228 premise is
\(|E|\ll A^2N^{3/2}T^\epsilon\). Consequently the remaining ENTIRE
sufficient one-sided estimate is

\[
 \boxed{\quad 2\Re D\ll_{\epsilon,J}A^2N^{3/2}T^\epsilon.\quad} 
                                                               \tag{5}
\]

It is equivalent, up to a target-sized error, to the original complete
signed remainder bound because
\(D+E=\sum_h\alpha_h(C_h-\rho_hI_h)\). Nothing in this report changes
the already paid partner or its ownership.

**Source card A: the CM premise.**
[AH2607.13518v1, Lemma2.4 and its proof](https://arxiv.org/html/2607.13518v1#S2.SS4).
[Current arXiv record](https://arxiv.org/abs/2607.13518) lists only v1,
submitted 15 July2026; the exact-version HTML separately prints
24 August2026 internally. These dates are not conflated. The theorem
requires fixed level \(q\), negative fundamental \(D_0\), conductor
dividing \(q\), and \(U\le t_\pi\le2U\), in probability normalization.
Primes dividing \(q\) must split or ramify; primes whose square divides
\(q\) must split. It bounds a squared Heegner point value by
\(\sum_\xi L(1/2,\pi\otimes\sigma_\xi)/L(1,\pi,\mathrm{ad})\),
with a constant independent of \(U\). At \(D_0=-4,q=1,2\), its unique
class gives the product of the untwisted and \(\chi_4\)-twisted central
values. The proof's equality retains a local toric product at
\(S=\{\infty,2\}\) and partial L-factors; their exact values are not
provided there. No moving-test, derivative, or strip estimate is stated.
**Verdict:** applicable as a majorant; insufficient as a signed identity.

**Source card B: the signed trace premise.**
[Knightly--Li1202.0189v1, Theorem7.14, Section7.6](https://arxiv.org/html/1202.0189v1#S7.SS6).
[Current arXiv record](https://arxiv.org/abs/1202.0189) lists v1,
1 February2012, without a withdrawal notice. Use trivial character,
level \(Q=1,2\), unramified Hecke index \(\nu\), positive Fourier
indices \(a,b\), and even \(h\) with \(h(iz)\in PW^{12}\).
The norm is \(\psi(Q)^{-1}\int|u|^2d\mu\),
\(\psi(Q)=Q\prod_{p\mid Q}(1+1/p)\). Its spectral summand is
\(\lambda_u(\nu)a_a(u)\overline{a_b(u)}h(t_u)/
(\|u\|^2\cosh\pi t_u)\). The identity includes the complete
Eisenstein integral, a diagonal condition, and all \(c\in Q\mathbb N\)
generalized Kloosterman terms. Their Bessel transform is
\(\int J_{2it}(4\pi\sqrt{\nu ab}/c)h(t)t/\cosh(\pi t)\,dt\).
Paley--Wiener constants depend on the test; the theorem supplies no
uniform growing-height saving. **Verdict:** lawful signed identity in
its stated measure; not (5). Neighboring formulas were inspected only
for normalization/admissibility context, not imported as extra theorems.

# 3. Derivation, matching, and full cost accounting

## Actual CM measure and the failed signed substitution

The reflection and Fricke vanishings, the complete Gram matrix, and all
primitive functional equations are inherited from the two reviewed228
signed-Hecke artifacts. In particular, conductor-one oldforms do not
acquire conductor two. Every surviving primitive form has even parity
and root number plus; for new level two
\(\lambda_f(2)=-1/\sqrt2\). The odd-index depletion remains

\[
 F(m)-\lambda_f(2)F(2m)+\mathbf1_{q=1}F(4m).             \tag{6}
\]

Thus the local lengths \(L,L/2,L/4\), square-root factors, and phases
are retained. The same parameter letter must not stand for both an
ambient oldspace level and a primitive conductor.

Probability normalization converts to area normalization as follows.
The areas are \(v_1=\pi/3\), \(v_2=\pi\). If \(\varphi\) has
probability norm one, then \(u=\varphi/\sqrt{v_q}\) has area norm one;
therefore \(|u(z)|^2=|\varphi(z)|^2/v_q\). This fixed conversion does
not evaluate a toric local factor or remove (4)'s denominator.

For the present class-number-one field, the formal desired central-value
replacement would require a proved equality of the shape

\[
 |u_f(z_q)|^2=C_q(f,t_f)
   \frac{L(1/2,f)L(1/2,f\otimes\chi_4)}{L(1,\mathrm{ad}f)},
                                                               \tag{7}
\]

with the exact archimedean and two-adic factor \(C_q\), correct vector,
norm, and root-sign restrictions. Here (7) is an **unfilled interface**,
not an asserted evaluated formula. The source's local toric expression
explains the interface but does not authorize replacing \(C_q\) by a
constant or by one. The fixed positive upper bound in card A does not
specify the multiplier in (7).

The logical obstruction is elementary. Let \(b=(1,1)\),
\(a=(1,1/2)\), and \(v=(1,-1)\). Then
\(0<a_j\le b_j\), even with uniform two-sided comparability, while
\(\sum b_jv_j=0\) and \(\sum a_jv_j=1/2\). Thus there is no
signed-sum transfer from a majorant of positive weights. This control
does not assert these numbers are CM weights. It refutes exactly the
claimed inference from the information supplied by the majorant.
Using \(\sum b_j|v_j|\) is legal but gives up the proposed cancellation.

No approximate functional equation is used after this failed premise.
Accordingly no supposed degree-four length, product norm, or truncated
central-value polynomial enters any bound in this report. Opening such
a polynomial before proving (7) would not produce a representation of
the quantity under review.

## Exact oldspace resolvent, with all tails

For a primitive level-one form the Hecke recurrence gives
\(\lambda_f(2^{r+1})=\lambda_f(2)\lambda_f(2^r)-
\lambda_f(2^{r-1})\). Hence its generating function is

\[
 \sum_{r\ge0}\lambda_f(2^r)x^r
       =(1-\lambda_f(2)x+x^2)^{-1}.                    \tag{8}
\]

The inherited Satake bound with fixed \(\vartheta<1/2\) implies
\(|\lambda_f(2^r)|\le(r+1)2^{r\vartheta}\). Substitution
\(x=-1/\sqrt2\) is absolutely convergent and proves (1). With
\(\delta=1/2-\vartheta>0\), its tail after \(r=B\) is bounded by
\(C_\delta(B+2)2^{-\delta B}\), uniformly in the primitive form.
This derivation does not apply a conductor-two recurrence to an oldform.

If (1) is inserted into the Hecke factor, the exact multiplication law is

\[
 \lambda_f(2^r)\lambda_f(n)=
   \sum_{j=0}^{\min(r,v_2(n))}\lambda_f(2^rn/2^{2j}).    \tag{9}
\]

All resulting indices must stay. Approximating the multiplier to an
arbitrary fixed inverse power of \(T\) by this series needs
\(B\asymp\log T\), and therefore can introduce indices as large as
\(2^Bn\), a fixed power of \(T\) times \(n\), not a subpower factor.
An infinite weighted treatment may do better; no cost is assigned to it
without a matching estimate. Boundedness of (1) licenses an absolute
estimate, not deletion from a signed trace.

## Matching the signed trace measure

Write \(Q\) for the source's level, to avoid collision with shell \(N\).
For area-normalized cusp forms its norm convention gives
\(\|u\|_{KL}^2=1/\psi(Q)\). Thus dividing the entire KL formula by
\(\psi(Q)\) converts the displayed cusp term to the area convention;
the same division acts on the continuous and geometric terms. The
values are \(\psi(1)=1\), \(\psi(2)=3\), distinct from the surface
areas. No probability/area/Hecke-harmonic convention is interchangeable.

The actual CM measure is a point evaluation squared. By contrast,
card B contains two Fourier coefficients and \(1/\cosh\pi t\).
At \(z=x+iy\), an even primitive form in the K-Bessel convention has

\[
 u_f(z)=2\sqrt y\sum_{a\ge1}a_a(u_f)
                    K_{it_f}(2\pi ay)\cos(2\pi ax).
                                                               \tag{10}
\]

At \(i\) the cosines are one; at \(z_2\) they are \((-1)^a\).
Squaring (10) introduces *both* Fourier sums, both K-Bessel factors,
and their exact signs. One could then try to use card B with a test
containing \(\cosh(\pi t)K_{it}(2\pi ay)K_{it}(2\pi by)\), but this
is a new moving family indexed by \(a,b\). Its admissibility, all
Fourier tails, and the resulting geometric sums require proof. A finite
cutoff followed by absolute convergence at each fixed eigenfunction is
not automatically a uniform spectral interchange.

Also, the selected positive-index formula sums the full parity basis.
It cannot simply be restricted to even forms. An even projector needs
the corresponding opposite-sign trace information or a proved parity
version; replacing the point value by its positive Fourier half on odd
forms is wrong. At level two the Fricke projector and primitive old/new
resolution are further exact operations. Keeping the original complete
level-two basis retains the oldspace automatically; re-expressing it in
primitive level-one terms must reproduce precisely (1). No evaluated
CM-to-harmonic bridge, parity-projected trace, or unpaid Fourier
reconstruction is asserted here.

The level-one Hecke indices are all admissible. The original level-two
indices are odd and therefore unramified. If a primitive conductor-two
dual series has even indices, they must first be resolved by
\(\lambda_f(2^an_0)=(-1/\sqrt2)^a\lambda_f(n_0)\), \(n_0\) odd,
with the changed scale and phase; they are not inserted as unramified
operators on the full oldspace.

Finally, the source continuous integral is in Fourier-coefficient
coordinates. Its removal is licensed by the already paid228 \(E\)
only *after* a complete, normalized reconstruction proves it is that
same \(E\). The source diagonal condition and the complete modulus sum
also remain. A formal trace equality is not an upper estimate for their
joint signed value.

## Height, moving derivatives, and strip costs

On an actual descendant let \(h\asymp M\), \(h=dm\), \(L=M/d\),
\(t\asymp U=TM/\sqrt N\). The inherited exact transformed coefficients
have envelope

\[
 |b_n(t)|\ll_B c_{d,U}\frac L{\sqrt U}(1+n/K)^{-B},\quad
 c_{d,U}=\frac{A^2\sqrt N}{U\sqrt d},\quad
 K=\frac{qt}{\pi^2L}.                                  \tag{11}
\]

The phase retained at leading order is
\(e^{-i\pi/4}X_n^{it}\), \(X_n=qdR^2/n\). On \(n\asymp K\),
\(X_n\asymp T\sqrt N\), independently of the descendant depth.
For the phase factor alone the exact costs are

\[
 (U\partial_t)^kX_n^{it}=(iU\log X_n)^kX_n^{it},\qquad
 \max_{|v|\le\sigma}|X_n^{i(t+iv)}|
        =\max(X_n,X_n^{-1})^\sigma.                    \tag{12}
\]

Thus on the effective band a fixed strip costs
\((T\sqrt N)^\sigma\), and a generic scaled derivative seminorm costs
\((U\log(T\sqrt N))^k\). These are properties of the pure phase,
not lower bounds for the full actual transform or arithmetic sum. On
the entire \(n\)-tail (12), not the effective-band simplification,
must be used.

A smooth compact spectral cutoff times this phase is not holomorphic,
so it does not satisfy card B's Paley--Wiener premise just because it is
smooth on the real axis. Evenizing the test does not fix this. The
original \(H_h\), before a nonanalytic spectral partition, is an even
entire spherical transform of a compact smooth radial test and is a
lawful route to admissibility. Its constants grow, however.

Here is a crude explicit cost derivation, independent of any current
radial-Abel report. In the inherited coordinate
\(\cosh r=1+2x/h\), its support satisfies
\(\log3<r<\log(CN/h)\); its phase is
\(2\pi R\sqrt h e^{-r/2}\). Its fixed radial derivatives cost
\((1+\Lambda_h)^k\), \(\Lambda_h=Rh/\sqrt N\), times \(A^2\).
The spherical integral representation gives, for fixed strip width
\(\sigma\), a bound
\(C_\sigma(1+r)e^{(\sigma-1/2)r}\) for the Legendre function there.
Moving the radial Laplacian onto the compact amplitude \(k\) times
pays \((1+\Lambda_h)^{2k}\) and gains \((1+|t|)^{-2k}\) outside a
fixed bounded \(t\)-interval. On that interval use the direct bound.
Consequently a sufficient strip seminorm bound is

\[
 |H_h(t+iv)|\ll_{\sigma,k,J}
 A^2(N/h)^{1/2+\sigma}\log(2N/h)
 (1+\Lambda_h)^{2k}(1+|t|)^{-2k},\quad |v|\le\sigma.
                                                               \tag{13}
\]

The uniformly bounded interval is absorbed in the displayed constant.
Smooth zero extension eliminates boundary terms; the radial operator
coefficients are bounded because \(r>\log3\). This establishes that a
fixed-test constant must be tracked, not treated as \(T^\epsilon\).
It does not estimate the complete Kloosterman side. No integration by
parts over the discrete eigenvalues follows from (12) or (13).

## Restoring every original power and component

There is no new applicable positive or signed upper bound in this
audit. For comparison only, the reviewed228 procedure supplies

\[
 |D|\ll A^2T^{3/2+\epsilon}N^{5/4}.                    \tag{14}
\]

Its ratio to the quarter raw target is \(T^{3/2}N^{-1/4}\); at
\(N=T\) it misses by \(T^{5/4}\). Its ratio to the original complete
raw cap \(A^2N^2\) is \(T^{3/2}N^{-3/4}\), at least a constant
times \(T^{3/8}\) in the allowed range. These are upper certificates,
not actual lower bounds. Formula (14) is not promoted as this round's
new mechanism.

After adding the already paid entire \(E\), the arithmetic identity
caps the *sum of both cusp levels* by \(A^2N^{2+\epsilon}\). It does
not give this cap separately to each level, descendant, or spectral
band. At \(N=T\), this leaves the genuine sufficient raw saving
\(T^{1/2}\). A complete complex wave exponent \(\gamma\) replaces the
right side of (5) by \(A^2N^{3/2}T^{2\gamma+\epsilon}\), requiring
\(T^{1/2-2\gamma}\) saving over the cap at this shell.

The exact Fejer multiplier is less than two; the diagonal costs
\(A^2N^{1+\epsilon}\), and the full density costs
\(A^2N^{3/2+\epsilon}T^{-1}\log(2N)\). Dividing the squared shell
by \(N^{3/2}\), summing all dyadic scales, retaining the singleton,
and paying the original Schwartz tail leaves the elementary complex
wave cap \(T^{1/4+\epsilon}\), or physical exponent \(3/8\).
This is weaker than the inherited complete complex \(13/56\) and
the inherited complete REAL \(\beta=2\theta_{LY}-1/2\).
No complex block interpretation of \(\beta\) is made. The physical
restoration is \(1/4+\max(\gamma,0)/2\); to beat the real benchmark
by this sufficient complex route requires \(\gamma<\beta\).

Every low/exceptional mode and high spectral tail remains owned by the
reviewed exact kernel bounds. Every descendant retains its own
\(K\asymp qTd/\sqrt N\), both small-dual-index residues, all local
terms (6), and its entire dual tail. The scope is every real radius;
no radius average, single point in a varying CM family, or fixed
coefficient theorem has replaced it.

# 4. First doubtful or unproved step

The first failed direct import is the claim that card A permits (7) with
an explicitly known, trace-compatible weight. It does not. Multiplying
its inequality by the signed complex vector and summing is disproved
as an inference by the two-term control above. The local toric factors
and measure constants are not silently resolved here.

For the separate trace attempt, card B is a valid signed identity, but
the CM-to-Fourier/parity reconstruction, admissible moving test, and a
uniform estimate of **all** resulting diagonal, Kloosterman, and
continuous terms have not been established. A hypothetical cancellation
estimate for \(\sum_f\lambda_f(n)h(t_f)/L(1,\mathrm{ad}f)\) would still
not have the actual CM weight or oldspace denominator.

The first unproved complete arithmetic estimate is exactly (5), with
(2)--(4) and all continuous reconstruction as stated. To make a genuine
new source-based objective, one would first need an evaluated version
of (7) for both primitive conductors **and** a quantitative signed
estimate for the resulting full toric-weighted test family at the power
in (5), including its local series and all geometric partners. Neither
of the two audited statements supplies that new input. This report
therefore chooses the permitted precise-failed-premise outcome; it does
not recommend treating normalization alone as the next analytic gain.

# 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| current_primary_versions | Exact versions and current records inspected; AH submission date and internal document date distinguished. No exhaustive literature claim. |
| exact_source_hypotheses | Two selected audits only; card A is an inequality, card B an identity. No unproved application promoted. |
| actual_coefficients_and_cm_measure | Actual r2, signed Psi, all CM values, areas, conductor1/2, parity, Fricke and oldspace factor retained. |
| growing_test_and_transform_costs | Exact phase costs (12), crude original-test strip bound (13), nonanalytic-cutoff obstruction, and unpaid Fourier reconstruction explicit. |
| complete_cusp_and_continuous_ownership | (4) contains the whole cusp sum; the entire228 continuous partner remains in reconstruction. Source Fourier-continuous terms are not automatically identified with it. |
| all_shifts_endpoints_and_tails | All h, descendants, local arguments, small-index residues, original/spectral/dual tails, smooth endpoints, zero atom and singleton preserved. Empty integer overlap does not remove density. |
| complete_alternative_frontiers | M1 HARD and independent SMOOTH; M2 TOP/BAL/UNBAL; total-M1 GAR lower ownership through159 and separate cross owner; endpoints all remain open. |
| real_complex_and_average_scope | No averaged-point or averaged-radius substitution; inherited beta used only for the complete real wave. |
| full_power_restoration | (14), original cap, quarter target, shell normalization and physical exponent explicitly compared. |
| certificate_not_actual_lower_bound | Two-term control refutes only the majorant inference. Failed norm/strip certificates are not lower bounds for the arithmetic quantity. |
| statement_only_control | NONBLIND source audit; no current sibling, blind statement/report, or root-control artifact read. This is not the isolated control. |
| fixed_unbounded_order_scope | Accepted distribution retains both V^-2 and TV^(-136/13); fixed twelfth29/25 would yield102/325 only. Adequate unbounded FIXED even orders remain a full alternative, not p(T). |

The algebraic controls (8)--(9) are exact identities, not numerical
experiments. The parity control in (10) explains why positive Fourier
indices cannot be used to remove odd modes without the missing trace
projection. No source theorem with arbitrary coefficients or arbitrary
positive CM majorants is asserted to prove the actual signed target.

# 6. Dependencies and exact provenance

Read `protocol.md`, the assigned brief, the active manifest, and relevant
authoritative graph nodes: GC-target, M9-M1, M9-M2,
GC-complete-square-root-large-values-moment-bound, and
GC-complete-distinct-radical-twelfth-reduction. The graph was parsed for
these exact entries; historical evidence paths inside them were not
followed. The graph hash is recorded in Section1.

Permitted local evidence inspected/used:

- `strategy/round229_full_goal_cuspidal_source_review.md` and
  `rounds/codex-managed/gc-full-goal-cuspidal-source-review/briefs/complete_cuspidal_interfaces.md`.
- `strategy/gauss_circle_strategy_review_2026-09-23.md` (pinned source-import and full-goal strategy) and
  `strategy/gauss_circle_strategy_checkpoint_round226_2026-09-28.md`.
- `rounds/codex-managed/gc-signed-heegner-phase/synthesis.md`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.
- `rounds/codex-managed/gc-signed-heegner-phase/reports/signed_hecke_functional_attack.md` and
  `rounds/codex-managed/gc-signed-heegner-phase/reviews/independent_signed_hecke_review.md`.
- `rounds/codex-managed/gc-signed-heegner-phase/reports/complete_eisenstein_pairing.md` and
  `rounds/codex-managed/gc-signed-heegner-phase/reviews/independent_eisenstein_review.md`
  (statement, normalization, complete ownership and reviewed scope).
- `rounds/codex-managed/gc-complete-joint-spectral-remainder/reports/heegner_joint_norm_audit.md`.

The old report's functional equation, gamma, symbol, envelope and point
moments are inherited reviewed evidence, not new primary imports. In
particular AH's defective collective-sieve printing is not repaired or
used. The current review did not independently re-audit its fourth-moment
proof. The complete continuous proof and its Leong premise are likewise
inherited, not a third theorem audit.

Bounded primary screening used searches for CM central values and signed
spectral reciprocity, plus the current primary records of
[Yang2608.23886](https://arxiv.org/abs/2608.23886),
[Humphries--Khan's dihedral random-wave paper](https://link.springer.com/article/10.1007/s00039-020-00526-4),
and the KL record. Those screening hits supplied no imported theorem.
The two selected source cards are AH Lemma2.4 and KL Theorem7.14.
AH's adjacent approximate-functional-equation discussion and KL's
neighboring pre-Kuznetsov/extended-test discussion were inspected only
to locate limits of the chosen application; no extra estimate from
them is used. No paper's full proof is certified by this audit.

The conductor was sent substantive progress on the CM majorant gap and
on the exact oldspace resolvent/trace-test costs. It directed preservation
of the first failed premise and supplied a bibliographic date warning,
which was independently checked in the exact AH HTML. It supplied no
current sibling, blind calculation, or root-control contents.

Only this assigned report was written. No shared graph, draft,
validation matrix, synthesis, closed-round or legacy artifact changed.
Analytical/algebraic work exceeds95 percent; zero experiments.

# 7. Recommended state effect and stopping rule

**Retain** the scoped import obstruction, exact oldspace series, source
cards, and quantitative test-cost ledger as candidate evidence after
nonauthor review. **Reject** only the unsupported signed substitution
from a positive CM majorant and any claim that the displayed trace
identity already proves (5). **No change** to the accepted graph,
complete exponents, moments, or quarter status.

Suggested exit label: `strategy_cuspidal_source_review_no_complete_gain`.
No successor is designed or started. Freeze this report at its externally
recorded SHA256 and stop; only the conductor closes Round229.

Formatting-only repair authorized after initial freeze: four standalone carriage-return bytes in formula (4)'s roman labels were replaced with literal LaTeX roman commands. No mathematical content changed. The pre-repair SHA256 was 0d448af1d3e274c2d2914d64cfdc3776015cecb45ad9566984a8bbc014a8fd01; the replacement final hash is recorded externally.
