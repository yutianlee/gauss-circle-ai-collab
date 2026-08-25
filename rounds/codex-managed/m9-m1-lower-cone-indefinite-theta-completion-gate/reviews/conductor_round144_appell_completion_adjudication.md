# Round 144 conductor adjudication: completed Appell self-return with a sharper arithmetic cell reduction

- Campaign: `m9-m1-lower-cone-indefinite-theta-completion-gate`
- Round: `144`
- Role: conductor adjudication
- Starting graph SHA-256: `179e40fb38e6a5e26623c2584d469b1c4c8d5ae444a70d791298852f2d511204`
- Generated: `2026-08-24T05:54:19+08:00`

## Decision

The repaired conductor candidate is accepted after three independent final
GREEN confirmations.  The round closes under

\[
 \boxed{\mathsf{indefinite\_theta\_completion\_no\_go}}.
\]

This is a no-go for the proposed completion-to-bound mechanism, not for the
desired signed estimate.  Round 144 also proves a genuine strict arithmetic
support reduction: the target-safe displacement window grows from
\(\sqrt M\) to \(M^{3/4}\).

No target bound, M1 or M2 parent, endpoint theorem, M9 theorem, quarter
exponent, or improved global exponent is proved.

## Accepted proof kernel

Let

\[
 C(m)=\sum_{\substack{hr=m\\r\ {m odd}\\r>4h}}\chi _4(r),\qquad
 k_m=\left\lfloor\sqrt{Nm}+\frac12\right\rfloor,\qquad
 j_m=k_m^2-Nm,
\]

on disjoint half-open dyadic blocks \(\mathcal I_M\), with
\(R=X^{1/4}\), \(N=\lfloor X\rfloor\), and fixed
\(0<\rho<1/8\).  The accepted prime-power root bound and a retained gcd
average give, for \(J\geq1\),

\[
 \#\{m\in\mathcal I_M:0<|j_m|\leq J\}
 \ll_\varepsilon JX^\varepsilon.
\]

Indeed,

\[
 \sum_{1\leq |j|\leq J}\sqrt{(N,j)}
 \leq 2J\sum_{d\mid N}d^{-1/2}
 \ll_\varepsilon JN^\varepsilon,
\]

and \(k_m<N\) makes the map from a fixed \(j\) to the relevant root
class injective.  If \(N=Du^2\) with \(D\) squarefree, then the exact
radicals are \(m=Dt^2\) and remain separately target-safe.  Thus, for
all \(J\geq0\),

\[
 \#\{m\in\mathcal I_M:|j_m|\leq J\}
 \ll_\varepsilon (J+\sqrt M+1)X^\varepsilon.
\]

Since \(|C(m)|\leq\tau(m)\), the nonzero \(J\)-window costs
\(M^{-3/4}JX^\varepsilon\).  The largest polynomial window certified
by this absolute ledger is therefore \(J=M^{3/4}\), and

\[
 \mathfrak T_N=
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>M^{3/4}}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 +O_{\varepsilon,\rho,V}(X^\varepsilon).
\]

This replaces the Round-141 \(J^{3/2}\) price and \(\sqrt M\)
exhaustion claim.  It does not estimate the displayed survivor.

The exact completed scalar is

\[
 \mathcal H(\tau)=\frac12\widehat A_4(1/2,-3\tau;2\tau)
 =F(\tau)+\frac14+\sum_{a=0}^{3}\mathcal R_a(\tau),
\]

\[
 \mathcal R_a(\tau)=\frac i4(-1)^a
 \vartheta((2a-3)\tau+3/2;8\tau)
 R_{\rm Zw}(1/2+(3-2a)\tau;8\tau).
\]

For \(\gamma=(\begin{smallmatrix}a&b\\c&d\end{smallmatrix})\in
\Gamma_0(4)\), the internally derived specialization of the audited
completed Jacobi laws gives

\[
 \mathcal H(\gamma\tau)=\chi _4(d)(c\tau+d)\mathcal H(\tau).
\]

The proof retains the residual integral exponential
\(e[-c(d+3b)/4]=1\).  The holomorphic part \(F\) is not modular by
itself, the constant \(1/4\) and all four correction terms are
compulsory, the full modular group acts on a characteristic orbit rather
than on this scalar section, and no harmonic-Maass property is asserted.

After the target-safe cells are restored globally and the exact
character-Poisson identity is applied to a smooth dyadic block, the
positive-\(j\) principal stationary family is

\[
 e(1/8)N^{-1/4}
 \sum_{\substack{h\geq1\\0<j<\sqrt N}}\frac{\chi _4(j)}h
 V_{\rm low}(4R^2h^2/j^2)\psi_M(4Nh^2/j^2)e(Nh/j).
\]

The case \(j=\sqrt N\), when integral, remains in the endpoint/Fresnel
ledger.  The outer \(i/2\) is essential.  After the complete boundary,
subtraction, alias, collar, profile, entry/exit, and remainder ledger is
reassembled, this factor is inverse to the accepted Round-140
\(e(-1/8)N^{1/4}\) map.  Hence completion plus coefficient extraction
returns the same reciprocal owner rather than producing a smaller signed
one.

## Seam adjudication

1. **Arithmetic counting:** GREEN.  The gcd average, squareful centres,
   exact radicals, total count, half-open blocks, and \(k_m<N\) injection
   were independently checked.
2. **Lattice and cone:** GREEN.  The signature-\((1,1)\) lattice,
   level-four signed cosets, strict cone, opposite cone, empty sloping wall,
   and isotropic boundary are exact.
3. **Completion and multiplier:** GREEN.  The separate \(1/4\), four
   \(i/4\) corrections, \(\Gamma_0(4)\) scalar law, and full-group
   limitation all match the audited conventions.
4. **Source hypotheses:** GREEN/no-go.  The completed-Appell theorem
   applies, but no audited harmonic-Maass, Voronoi, or complete-divisor
   theorem estimates the resulting five coefficient pairings for the
   literal square-root test.
5. **Direction and mask:** GREEN.  The individual complex direction is
   retained.  The hard mask is removed only through the proved global
   target-safe restoration before a smooth transform.
6. **Transform constants and endpoints:** GREEN.  The negative-curvature
   Gaussian unit, outer \(i/2\), interior range, and endpoint/Fresnel owner
   are exact.
7. **Round-142 consistency:** GREEN/no-go.  The level-four cusp orbit is
   compatible with the complete \(4\mid q\) hierarchy, while denominator
   Abel reconstruction still returns \(r_2/4\), not \(C\), and preserves
   the negative-character and moving-wedge owners.
8. **Capacity and scope:** GREEN/no-go.  The top cone has absolute capacity
   \(R^{1/2+o(1)}\), and the reciprocal stationary family has capacity
   \(N^{1/4}\asymp R\).  These are upper capacities, not signed lower
   bounds.

The optional numerical observations in the blind primary report are not
used.  The accepted campaign evidence is entirely analytic, algebraic, and
source-based.

## Conflict resolution

The primary reports initially differed on novelty, correction ownership,
the root-count price, the scalar group, and the principal stationary range.
Post-unmask reviews and the final audit chain resolved these differences as
follows:

- Round 63 retains priority for the Appell identity and four-term
  completion; Round 144 contributes the derived scalar specialization and
  its reconciliation with the Round-141/142 owner.
- The gcd is averaged before the displacement sum, replacing the obsolete
  \(J^{3/2}\) price by \(J\).
- The four nonholomorphic corrections are one global owner family; they are
  not assigned termwise to individual Round-140 aliases or remainders.
- The coefficient transform is applied only after global mask restoration,
  and its self-return is only aggregate.
- The stationary formula is a principal family, not an exact full branch;
  \(j=\sqrt N\) remains an endpoint transition.

## First open estimate

The exact frontier after Round 144 is

\[
 \boxed{
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>M^{3/4}}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 \ll_{\varepsilon,V}X^\varepsilon.}
\]

Equivalently, after complete global owner restoration,

\[
 \mathcal S_{\rm recip}^{+}
 \ll_{\varepsilon,\rho,V}RX^\varepsilon.
\]

No accepted source or transform closes either inequality.

## State decision

The State Patch shall:

- create a source-audit node for the internally derived completed scalar
  specialization;
- strengthen the accepted cell reduction to the \(M^{3/4}\) survivor and
  correct the obsolete Round-141 root-count ledger;
- create a scoped completed-Appell self-return obstruction;
- update the Round-63 Poisson, Round-140/141 owner, Round-142 spectrum, and
  global lower-radial nodes with the new evidence;
- correct the two affected Round-141 rejected-claim reasons;
- reject all coefficient-only modularity, harmonicity, correction-dropping,
  hard-mask, cosine, branchwise, slope-separation, capacity-lower-bound, and
  exponent inferences; and
- leave M9-M1, M9-M2, endpoint uniformity, M9, the conditional bridge, the
  internal \(1/3\) theorem, the external Li--Yang theorem, and the quarter
  target unchanged.

