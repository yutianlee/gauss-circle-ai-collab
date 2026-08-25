# Round 159 conductor seed: common-profile recombination

## 1. Result: candidate exact compression

The moving trace, both profile-difference remainders, and both outer
endpoints recombine exactly to the original paired-interior
coefficient.  Complete-frequency inversion then removes the artificial
boundary-frozen profiles of the isolated trace and returns one
common-profile residual-mask sum.  This is a candidate finite lemma,
not yet accepted mathematics and not a proof of the target bound.

## 2. Exact statement and hypotheses

Assume the accepted Round 157 coefficient

\[
 B_j(x)=
 \mathbf 1_{x\ge1}\mathbf 1_{-x\le j\le x-1}
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right)
\tag{159.C1}
\]

and all Round 158 half-open block conventions.  Put

\[
 \kappa(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,
 \qquad r(\ell)=\kappa(\ell)^2-N\ell.
\tag{159.C2}
\]

For the full-frequency physical row define

\[
 \mathcal S_U(V)=
 \sum_{V<|j|\le2V}\sum_{x\bmod4N}B_j(x)G_N(x^2-j).
\tag{159.C3}
\]

The candidate identity is

\[
\boxed{
 \mathcal S_U(V)=
 \sum_{\ell\ge1}\chi_4(\ell)w_U(\ell)e(\sqrt{N\ell})
 \mathbf 1_{V<|r(\ell)|\le2V}.}
\tag{159.C4}
\]

The paired-interior matrix equals (159.C4) minus the already closed
zero and Nyquist whole rows.

## 3. Derivation

Equations (K158.7) and (K158.8) are finite Abel identities.  Adding
their outer, moving, and profile-difference lines gives
\(\sum_j\widehat B_j(2dv)K(-v^2,-j;c)\) exactly for every signed block,
odd divisor, and interior frequency.  Thus no endpoint or bulk term is
discarded before complete-frequency inversion.

If \(G_N(x^2-j)\ne0\), write \(x^2-j=N\ell\).  The literal cell mask in
(159.C1) is equivalent to

\[
 x^2-x+1\le N\ell\le x^2+x.
\tag{159.C5}
\]

The integer intervals in (159.C5) partition the positive integers as
\(x\) varies, so \(x=\kappa(\ell)\) uniquely and
\(j=r(\ell)\).  At this selected point,

\[
 w_U\!\left(\frac{x^2-j}{N}\right)=w_U(\ell),
\qquad
 e(\sqrt{x^2-j}-x)=e(\sqrt{N\ell}),
\tag{159.C6}
\]

because \(x\) is an integer.  Finally
\(G_N(x^2-j)=\chi_4(\ell)\), proving (159.C4) under the inherited
physical-lift convention.

## 4. First doubtful or unproved step

The first unproved analytic input is

\[
\left|
 \sum_{\ell\asymp M}\chi_4(\ell)\widetilde w_U(\ell)
 e(\sqrt{N\ell})\mathbf 1_{V<|r(\ell)|\le2V}
\right|
\ll_\varepsilon M^{3/4}X^\varepsilon.
\tag{159.C7}
\]

The profile is now common and the phase is smooth, but the exact
variable residual mask can still have support and variation of order
\(M\).  Neither fact alone proves (159.C7).

## 5. Required controls and preliminary outcomes

- Finite Abel reconstruction: algebraically GREEN, pending independent
  line rederivation.
- Positive and negative endpoints: retained, not paired away.
- Component and zero-extension transitions: retained inside the
  coefficient differences.
- Complete-frequency normalization: inherited, but must be checked
  against subtraction of zero and Nyquist exactly once.
- Nearest-cell partition: exact.
- Boundary profile versus quotient profile: the full recombination
  gives \(w_U(\ell)\); this does not revise the isolated-trace theorem.
- Phase: \(e(-\kappa(\ell))=1\) exactly.
- Target: raw \(M^{3/4}\), not square-root by definition.
- Computation: none used.
- Downstream: quarantined.

## 6. Dependencies and exact artifacts used

- protocol.md
- state/proof_obligations.yml
- proofs/kernels/m9_m1_d1_nonzero_centering_nyquist_fold.md
- proofs/kernels/m9_m1_d1_paired_interior_cell_trace_reduction.md
- Round 158 conductor adjudication and synthesis
- strategy/round159_d1_abel_commutator_recombination_strategy.md

## 7. Recommended state effect

Do not patch the graph yet.  First require an independent blind
rederivation, hostile profile/endpoint review, and analytic method
audit.  If (159.C4) survives, promote only the exact common-profile
recombination.  Promote the paired-interior target or a new strict
range only if (159.C7) is actually proved with every seam and restored
power.
