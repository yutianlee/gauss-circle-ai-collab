# Round 181 M1/GAR frontier selection

- Role: design selection only; no proof-state mutation
- Starting graph: `6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`
- Candidate owners: direct `M9-M1` and alternative GAR
- Recommendation: retain direct hard M1 for the conductor's final comparison; defer GAR

## 1. Result

Within the M1/GAR portfolio, the smallest exact fresh interface is the
**high-squarefree-radical part of the literal hard M1 product cone**. It
refines `M9-M1-top-endpoint-signed-cone`; it is not a third M1 route and is
not a coefficient-uniform estimate. The unique hard profile is narrower
than either the all-smooth direct parent or the complete GAR lower owner,
and success would close one named analytic parent through the proved top
transform.

The exact Round-181 target should be (181.M1-HR) below, uniformly for every
still-unowned hard residual frequency shell. The complementary
low-squarefree-radical sector has a target-sized divisor-counting ledger.
The unresolved high-radical part has a short square multiplier and retains
the exact conductor-four divisor-cone coefficient.

GAR should be deferred. Its full Round-122 survivor has positive capacity
\(R^2\) against target \(R\) and simultaneously contains all
\(D,d,L,t\) layers plus a cross owner. Rounds 154--159 reduce only the
\(D=d=L=1,t=1\) face to a raw \(M^{3/4}\) variable-mask target; complete
theta inversion and the six Abel pieces self-return to that same wave.
Proving this face would not close GAR, while attacking the complete
Round-122 scalar is too broad for one bounded round without a genuinely
new theorem already specified.

This recommendation is relative to M1/GAR and does not pre-empt the
conductor's comparison with BAL or UNBAL.

## 2. Exact proposed interface

Let

\[
 y=\lfloor\sqrt X\rfloor,\qquad
 q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor,
\]

and let \(L\) be one literal middle or lower residual shell of the unique
hard profile, after deleting the accepted terminal shell and isolated
second-derivative point. Write

\[
 \mathcal T^{M1}_L(X)
 =\sum_{h\asymp L}
   \sum_{\substack{4h<n<16h\\ n\ {\rm odd}}}
   \chi_4(n)a^{\rm lit}_{L,X}(h,n)e(\sqrt{Xhn}).
 \tag{181.M1.1}
\]

The graph-owned symbol \(a^{\rm lit}_{L,X}\) retains the dyadic frequency
cutoff, \(\Phi(h/(H+1))\), \(W(\sqrt{4q_Xh/n})\), the normalized
\(h^{-3/4}n^{-3/4}\) powers, floors, stars, frequency signs, real-\(X\)
support crossings, and the hard endpoint. Extend it by zero off the
literal support. Define the exact product coefficient

\[
 C_{L,X}(r)=
 \sum_{\substack{h\mid r,\ h\asymp L\\
                  r/h\ {\rm odd},\ 4h<r/h<16h}}
 \chi_4(r/h)a^{\rm lit}_{L,X}(h,r/h).
 \tag{181.M1.2}
\]

Then

\[
 \mathcal T^{M1}_L(X)=\sum_r C_{L,X}(r)e(\sqrt{Xr}).
 \tag{181.M1.3}
\]

Write uniquely \(r=st^2\), with \(\mu^2(s)=1\) and \(t\geq1\). The
recommended frozen inequality is

\[
 \boxed{
 \left|
 \sum_{\substack{s>L\\ \mu^2(s)=1}}
 \sum_{t\geq1}C_{L,X}(st^2)e(t\sqrt{Xs})
 \right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.}
 \tag{181.M1-HR}
\]

Literal product support gives \(s\ll L^2\) and
\(t\ll L/\sqrt s\ll\sqrt L\). The absolute value remains outside the
complete high-radical aggregate.

### Low-radical design ledger

This calculation must be independently rederived in the proof round; it
is not yet a graph claim. Since \(hn\asymp L^2\), fixed squarefree \(s\)
allows \(O(1+L/\sqrt s)\) square multipliers. Every product has at most
\(\tau(st^2)\ll_\varepsilon X^\varepsilon\) literal factor incidences,
and the normalized symbol is bounded. Hence

\[
 \sum_{\substack{s\leq L\\ \mu^2(s)=1}}\sum_t|C_{L,X}(st^2)|
 \ll_\varepsilon X^\varepsilon
 \sum_{s\leq L}\left(1+\frac L{\sqrt s}\right)
 \ll_\varepsilon L^{3/2}X^\varepsilon.
 \tag{181.M1.4}
\]

Thus the audited low-radical bound plus (181.M1-HR) is target-equivalent
to the complete hard cone.

### Capacity and plausible mechanism

The full and high-radical coefficient-insensitive capacities are
\(L^2X^\varepsilon\), while the target is
\(L^{3/2}X^\varepsilon\). The missing factor is \(L^{1/2}\), equal at
\(L\asymp X^{1/6}\) to the certified physical deficit \(X^{1/12}\).

For fixed \(t\), the high-radical support length is
\(S_t\asymp L^2/t^2\). A sufficient, deliberately stronger discovery
target is

\[
 \left|
 \sum_{\substack{s>L\\ \mu^2(s)=1}}
 C_{L,X}(st^2)e(t\sqrt{Xs})
 \right|
 \ll_\varepsilon S_t^{3/4}X^\varepsilon
 \asymp L^{3/2}t^{-3/2}X^\varepsilon,
 \tag{181.M1.5}
\]

because its right sides sum to \(O(L^{3/2}X^\varepsilon)\). This must be
a fixed-actual-direction estimate, not an arbitrary-coefficient theorem.
A plausible route is a joint squarefree-radical/product-fibre estimate
that keeps \(\chi_4\) inside \(C_{L,X}\), or a fixed-centre
\(TT^*\)/spectral formulation that sums the complete actual divisor-cone
direction before applying a norm. The campaign should accept a proof of
the weaker aggregate (181.M1-HR); the stronger layerwise placement is a
discovery target, not a required claim.

The \(t=1\) face remains literal, so the split does not pretend that
averaging in the square multiplier supplies the saving.

## 3. Dependencies and owner effect

The proposed interface uses:

- `M9-M1-top-endpoint-transform` for the exact hard transform and physical
  normalization;
- `M9-M1-top-endpoint-signed-cone` for the owner statement;
- `H4-Phi-regularity` and the audited hard profile for symbol and endpoint
  control;
- `M9-M1-terminal-frequency-divisor-bound`,
  `M9-M1-TTY-exponent-pair-wedge`, and
  `M9-M1-frequency-phase-diagram-R10` for prior-owner deletion;
- `M9-M1-direct-hard-smooth-separate-one-third-minimax` for the exact
  \(L^{1/2}=X^{1/12}\) deficit; and
- `M9-M1-physical-one-count-assembly` for the downstream map.

If (181.M1-HR) and the low-radical seam are proved uniformly for all hard
residual shells, `M9-M1-top-endpoint-signed-cone` closes. The independent
smooth direct parent remains open, so this alone proves neither `M9-M1`,
GAR, `M9`, either bridge, the quarter theorem, nor an exponent improvement.

If only (181.M1.4) is certified, create one strict-sector reduction and
leave the parent open. If the high-radical mechanism self-returns, record a
mechanism-scoped obstruction rather than rejecting the hard cone.

## 4. Why the other M1/GAR choices rank lower

### Direct smooth M1

The smooth parent asks

\[
 B_1(D,L;X)\ll_\varepsilon X^{1/4+\varepsilon}
\]

for every literal smooth label in the whole residual corridor
\(\mathcal U_1\). Its first smooth witness has the same \(X^{1/12}\)
deficit, but its quantifiers include all smooth denominator scales,
profile transitions, crossings, and endpoints. No accepted localization
maps the canonical global Gram or GAR back to this blockwise parent. It is
strictly broader than the unique-profile hard target.

### Complete GAR lower owner

With \(R=X^{1/4}\), GAR requires

\[
 G_X^{\rm low}\ll_\varepsilon X^\varepsilon,
 \qquad\text{equivalently}\qquad
 \mathcal B_{\rm low}\ll_\varepsilon RX^\varepsilon.
 \tag{181.GAR.1}
\]

The Round-122 scalar is a prescribed-centre wavelet over Fourier indices,
low two-adic valuations, residue branches, and full-minus-complement
coefficients. Complementary-divisor inversion, full-circle insertion,
central correction, high-adic deletion, residuewise norms, and
Abel/Fourier reconstruction supply no remaining automatic gain.

The deepest analyzed face is

\[
 \left|
 \sum_{\ell\asymp M}\chi_4(\ell)\widetilde w_U(\ell)e(\sqrt{N\ell})
 \mathbf1_{V<
 |\lfloor\sqrt{N\ell}+1/2\rfloor^2-N\ell|\leq2V}
 \right|
 \ll_\varepsilon M^{3/4}X^\varepsilon.
 \tag{181.GAR.2}
\]

Its raw capacity is \(M\), missing \(M^{1/4}\), but proving it leaves
\(D>1\), \(L>1\), generic \(t=1\), every \(t\geq2\), and the cross
owner. Complete theta inversion, separated Abel terms, and the principal
reciprocal \(B\)-process return to (181.GAR.2). Therefore the full
Round-122 owner is too broad and the Round-159 face has too little immediate
owner leverage for Round 181.

## 5. No-repeat barriers and controls

Freeze these accepted barriers:

1. Frequency-first grouping, the second-derivative row, and the TTY row
   have separate minimax \(1/3\); rescanning them cannot supply
   \(X^{1/12}\).
2. Product-fibre triangle, frozen kernels, and opposite-offset pairing
   retain capacity or reconstruct the original M1 block.
3. Separate resonance cells and a second \(B\)-process return the rank-one
   square-root product wave. The phase \(\sqrt{hn}\) has no nonsingular
   two-variable Hessian.
4. Adjacent odd pairing leaves unmatched rows. Profile addition has the
   same physical sign, and profile subtraction is not the physical sum.
5. Angular functional equations and fixed-order Voronoi reflect the
   divisor angle or return the radial owner; pointwise bounds cannot be
   integrated absolutely over the inherited Mellin heights.
6. The canonical Gram is a post-global conductor child with no block-local
   inverse. Coefficient-uniform norms, unitary two-adic convolution, trace
   moments, and positivity give no \(L^{-1/2}\) directional gain.
7. The top M1/M2 cones have the same leading sign, different Vaaler
   coordinates, and an unmatched M1 wing.
8. The squarefree split may not delete \(t=1\), take absolute values over
   high \(s\), or replace \(C_{L,X}\) by arbitrary bounded coefficients.

Required false controls:

- **Perfect-square centre:** for \(X=y^2\), exact-square products can be
  coherent. They must be paid by the low-radical incidence ledger, not by a
  false oscillation claim.
- **High-radical \(t=1\):** any method whose saving comes only from
  \(t\)-averaging fails.
- **Dechirped coefficients:** arbitrary coefficients can cancel
  \(e(t\sqrt{Xs})\) and restore \(L^2\) capacity. The theorem must be
  fixed-actual-direction.
- **Character erasure:** every Cauchy or completion step must identify
  where the literal \(\chi_4\) survives.
- **Endpoint/zero extension:** product grouping must retain strict cone
  edges, stars, support crossings, both frequency signs, floors, and the
  hard sample with multiplicity one.
- **Scope:** a hard-cone theorem is not the smooth parent, `M9-M1`, GAR,
  or an exponent improvement.

## 6. Comparison with exhausted K17a/K26 automatic routes

Round 179 shows that K17a primitive-conductor parity and centering split
off a target-safe trace but make the centered defect reconstruct the
original literal orientation block. One square root still leaves
\(L\sqrt q\), while coefficient-uniform buckets retain \(Lq\) capacity.

Round 180 gives \(E_\nu=D_\nu+G_\nu\) for K26. The physical row diagonal
and equal-product cross-row sector are target-safe, but the unequal-product
complement is target-equivalent to the original local scalar concentration
problem. Row positivity has local \(L^2\) and endpoint \(L^4\) capacity,
one factor \(L\) above target.

The proposed M1 split claims no automatic projector or Gram saving. It pays
a different exact sector by squarefree-kernel counting and leaves a signed
high-radical scalar with the literal conductor-four coefficient. If a
\(TT^*\), completion, or radical large sieve erases that coefficient or
returns (181.M1.1), the round should close as a no-go.

## 7. Three orthogonal Round-181 tasks

1. **Literal reduction and seam proof.** Independently derive
   (181.M1.2)--(181.M1.4), audit all floors, stars, edges, signs, and zero
   extensions, and verify the connector from (181.M1-HR) to the hard parent.
2. **High-radical signed attack.** Work only on (181.M1-HR). Factor the
   actual \(C_{L,X}(st^2)\) without a divisor envelope; test
   (181.M1.5) and a joint-\(t\) alternative. Retain the complete character
   direction before every norm.
3. **Blind hostile/capacity review.** From a statement-only packet,
   rederive the normalization and run the perfect-square, \(t=1\),
   dechirped, endpoint, and character-erased controls. Decide whether the
   mechanism gives \(L^{1/2}\), a strict subrange, or an exact self-return.

## 8. First unproved step and state recommendation

The first unproved step is (181.M1-HR), or the optional stronger
(181.M1.5). Squarefree uniqueness and low-radical counting do not control
the high-radical \(t=1\) face. No accepted graph node currently supplies
the fixed-centre, fixed-actual-direction \(L^{1/2}\) saving.

Recommended state effect of this design report: **no graph change**.
Retain the hard-M1 high-radical gate for final Round-181 comparison, defer
the smooth parent, and park GAR until a theorem covering the complete
Round-122 survivor or all omitted GAR layers is specified. The internal
exponent remains \(1/3\), the audited external benchmark remains
\(0.3144831759740614\ldots\), and the target remains \(1/4\).

## 9. Exact artifacts used

- `protocol.md`
- `state/proof_obligations.yml`
- `state/next_round_plan.yml`
- `strategy/round178_full_proof_strategy_current_literature_review.md`
- `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/reports/full_graph_frontier_reconstruction.md`
- `rounds/codex-managed/m9-combined-top-cones/synthesis.md`
- `rounds/codex-managed/m9-m1-direct-parent-minimax-gate/synthesis.md`
- `rounds/codex-managed/m9-m1-direct-parent-minimax-gate/reviews/conductor_round119_capacity_and_labels.md`
- `rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/synthesis.md`
- `proofs/kernels/m9_m1_d1_full_abel_common_profile_recombination.md`
- `rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/synthesis.md`
- accepted Round-179 and Round-180 K17a/K26 obstruction nodes in the
  authoritative graph

