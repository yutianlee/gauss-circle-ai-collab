# Round 161 synthesis: radical long channels, exact collisions, and the one-column frontier

Round 161 closes under
**hard_top_radical_frequency_coupling_no_go**. The validated State Patch
creates two proved-internal nodes, updates two open hard-TOP parents,
records thirteen rejected overclaims, and preserves fourteen explicit
no-change decisions. The resulting graph is
8d39b06bd12357e337159473da3d4d6ec0c71d0ab3217588e4c6b5b34973b422.

## What was proved

The nonsquare hard-TOP product scalar has the exact radical form

\[
 \mathcal T_L^{\rm ns}
 =\sum_{\substack{D>1\\D\ {\rm squarefree}}}\sum_{t\ge1}
 B_D(t)e(tJ\sqrt D).
\]

The literal product incidence is bijective:

\[
 h=gd_1u^2,\qquad m=gd_2v^2,\qquad
 D=d_1d_2,\qquad t=guv,
\]

with \(d_1,d_2\) squarefree,
\((d_1u,d_2v)=1\), \(g,d_1,u\) odd, and
\(d_2v^2\le d_1u^2\le4d_2v^2\). All profiles, endpoints, support
conditions, parity branches, and zero extension are retained.

The accepted fixed-channel estimate yields, for every fixed \(C>0\),

\[
 \boxed{
 \left|\sum_{\substack{D\le CL\\D>1\ {\rm squarefree}}}
 \sum_tB_D(t)e(tJ\sqrt D)\right|
 \ll_{C,\varepsilon}L^{3/2}X^\varepsilon.}
\]

This owns all fixed \(t\ge\tau\sqrt L\) channels. It is a complete
long-channel sector, not an owner-complete strict polynomial range for the
full scalar.

Square-root independence gives a global exact-collision theorem. At one
fixed centre, at most one channel has \(J\sqrt D\in\mathbb Q\); the base
collision graph \(J(\sqrt{D_1}-\sqrt{D_2})\in\mathbb Z\) has at most one
unequal unordered edge. All exact cross-channel atom relations use that
same possible radical pair and are rational multiples of one primitive
relation. Trivial same-atom loops and nontrivial rational-channel
repetitions are separate, and a rational channel cannot coexist with a
cross-channel relation. The repaired statement passed a fresh blind
review. No near-collision gap follows.

## What was ruled out

The first remaining physical face is already one column:

\[
\begin{aligned}
B_D(1)=\mathbf 1_{D\asymp L^2}
\left(\frac{L^2}{D}\right)^{3/4}
\sum_{\substack{d_1d_2=D\\d_1\ {\rm odd}\\d_2\le d_1\le4d_2}}
&\chi_4(d_1)\eta_L(d_1)
\Phi\!\left(\frac{d_1}{H+1}\right)\\
&\times W\!\left(\sqrt{\frac{q_Xd_1}{4d_2}}\right).
\end{aligned}
\]

On \(Q\asymp L^2\) ambient squarefree rows, the \(t=1\) common-test
evaluation norm is exactly \(Q^{1/2}\asymp L\). A phase-aligned
one-column diagnostic has nuclear norm \(Q^{1/2}\) and evaluation
\(Q\asymp L^2\). Therefore support, accepted energy and channel bounds,
exact-collision sparsity, and a coefficient-uniform common-test,
large-sieve, Bessel, or Hilbert-projective theorem cannot imply the
\(L^{3/2}\) target. Positive Cauchy for the actual coefficient also stops
at \(L^{2+o(1)}\), leaving \(L^{1/2-o(1)}\).

This is not a lower bound for the physical coefficient. The diagnostic
does not have the literal divisor incidence or signs, and close-semiprime
singleton fibres prove no family density or lower mass.

The primary-source audit also closes only named routes. Montgomery--Vaughan
uses one common coefficient vector; Bombieri--Iwaniec is separable and
charges absolute collision forms; Robert--Sargos' four-root theorem is
not the fixed-\(J\) circular collision problem; and Miller requires the
coefficients of one fixed \(\mathrm{GL}(3)\) cusp form. Even granting
Robert--Sargos a fictitious cost-one separation, its direct monomial
theorem restores

\[
 J^{1/4}L^{3/2}+L^{7/4}+L^{3/2}+J^{-1/2}L^{3/2},
\]

whose best combination with triviality remains \(L^2\) for
\(L\ll J^{1/2}\). These checks do not exclude a different or future
coefficient-sensitive theorem.

## Proof status

The exact radical dictionary, fixed-constant long-channel sector, and
exact collision classification are now accepted mathematics in the graph.
The coefficient-uniform common-test and four named source continuations are
parked as a scoped obstruction.

The first open physical statement is

\[
 \boxed{
 \left|\sum_{\substack{D\asymp L^2\\D>1\ {\rm squarefree}}}
 B_D(1)e(J\sqrt D)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.}
\]

A solution must use the actual \(\chi_4\)-weighted close-factor
coefficient, or an equivalent alignment-sensitive theorem that fails on
the adversarial one-column diagnostic. After that, the compatible
\(L\ll D\ll L^2\), \(t\ll\sqrt L\) few-point channels and their
near-collision collars still require control.

Hard TOP remains open. Therefore the hard-TOP density-discrepancy and
signed-cone parents, BAL, UNBAL, M9--M2, M9--M1, endpoint uniformity, M9,
the conditional bridge, and the quarter theorem all remain open.

The strongest internally proved global exponent remains \(1/3\). The
separately audited external benchmark remains

\[
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\]

No global exponent improved in Round 161.

## Reviews and state effect

The statement-only rederivation, repaired post-unmask collision review,
independent projective-power review, primary-source/power seam, downstream
graph-scope review, conductor adjudication, and terminal State Patch audit
are all GREEN. No numerical experiment was used.

The accepted kernel is
proofs/kernels/m9_m2_hard_top_radical_long_channel_collision_common_test_obstruction.md.
The State Patch creates:

- M9-M2-hard-top-radical-long-channel-exact-collision-control;
- M9-M2-hard-top-radical-frequency-common-test-source-obstruction.

It attaches both only to the two open hard-TOP parents as dependencies and
inconclusive parent evidence. No accepted Round-137 node, downstream
theorem, or exponent is promoted.

## Next research interface

Round 162 should freeze the literal \(t=1\) close-factor face itself:

\[
 \sum_{\substack{d_1d_2\asymp L^2\\
 d_1,d_2\ {\rm squarefree},\ (d_1,d_2)=1\\
 d_1\ {\rm odd},\ d_2\le d_1\le4d_2}}
 \chi_4(d_1)\,\mathcal W_X(d_1,d_2)
 e(J\sqrt{d_1d_2}).
\]

The round should test character-preserving two-variable Poisson or
differencing, the rank-one product-phase degeneracy, exact dual
self-return, hard endpoints, squarefree/coprime decomposition costs, and
all restored powers. Its exit must be a target theorem for this face, a
genuinely complete sector beyond \(D\le CL\), or the first exact scoped
character/bilinear/source obstruction.
