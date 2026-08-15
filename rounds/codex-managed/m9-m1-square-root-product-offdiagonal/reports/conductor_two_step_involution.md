# 1. Result

The actual smooth fixed-interior square-root-product energy has an exact
two-step B-process involution at the stationary-main level. The first
transform in the difference variable produces a perfect-square phase;
the second transform restores the original signed reciprocal energy,
including both \(\chi_4\) factors and the exact factor \(k/J\). Therefore
iterating Poisson, stationary phase, or an unqualified Hankel transform
supplies no estimate: it is a coefficient-preserving return map. This
statement does not assert a new twice-transformed error ledger.

# 2. Exact statement and hypotheses

Let \(J=\sqrt X\), \(k,q\asymp Q\), and normalize the actual interior
B-process row as

\[
 P_k=\sum_{\substack{q>0\\q\ \mathrm{odd}}}
 \chi_4(q)C(k/q)e(\sqrt{Xkq}),
 \qquad
 C(y)=y^{3/4}\Xi(2\sqrt y),
\tag{2.1}
\]

with fixed smooth ratio cutoffs absorbed into \(C\). Put

\[
 S_k=\sum_{\substack{j>0\\j\ \mathrm{odd}}}
 \chi_4(j)\Xi(j/J)e(Xk/j).
\tag{2.2}
\]

For a fixed smooth \(k/Q\)-weight, let \(\operatorname{SM}_2\) denote
only the complete stationary main obtained from two successive
one-dimensional Poisson/B-process transforms. Then

\[
 \operatorname{SM}_2\!\left[\sum_k w(k/Q)|P_k|^2\right]
 =\sum_k w(k/Q){k\over J}|S_k|^2.
\tag{2.3}
\]

No estimate is asserted here for the aggregate nonstationary,
entry/exit, partition, or endpoint terms created by performing both
transforms. No hard edge or full-cone assertion is made.

# 3. Proof or derivation

Expand the energy, put \(q_1=q+2d\), and use

\[
 \chi_4(q+2d)\chi_4(q)=(-1)^d=e(d/2).
\tag{3.1}
\]

Poisson summation in \(d\) has dual frequency \(\ell\). Set
\(j=2\ell-1\), which is odd. The phase is

\[
 \sqrt{Xk}\{\sqrt{q+2d}-\sqrt q\}-{j\over2}d.
\]

Its unique positive stationary point satisfies

\[
 q_1^*=q+2d^*={4Xk\over j^2},
 \qquad
 |\partial_d^2 f(d^*)|={j^3\over8Xk}.
\tag{3.2}
\]

The Legendre phase is exactly

\[
 {Xk\over j}+{jq\over4}-\sqrt{Xkq}
 =\left(\sqrt{Xk/j}-{1\over2}\sqrt{jq}\right)^2.
\tag{3.3}
\]

The first stationary amplitude is \(\sqrt{8Xk/j^3}\). Evaluating the
first actual ratio symbol at (3.2) gives

\[
 C(k/q_1^*)=\left({j\over2J}\right)^{3/2}\Xi(j/J),
\]

so their product is exactly

\[
 \sqrt{k/J}\,\Xi(j/J).
\tag{3.4}
\]

The remaining sum is over odd \(q\). Write \(q=2v+1\), apply Poisson in
\(v\), and let \(n\) be the dual integer. Set \(s=j-2n\), again odd.
The stationary point and curvature are

\[
 q^*={4Xk\over s^2},
 \qquad
 |\partial_q^2 F(q^*)|={s^3\over32Xk}.
\tag{3.5}
\]

The odd-lattice density contributes \(1/2\). Consequently

\[
 {1\over2}\sqrt{32Xk/s^3}\,\overline{C(k/q^*)}
 =\sqrt{k/J}\,\overline{\Xi(s/J)}.
\tag{3.6}
\]

The two Gaussian factors \(e(-1/8)\) and \(e(1/8)\) cancel. The constant
from \(-nv=-n(q-1)/2\) is

\[
 e(n/2)=(-1)^n=\chi_4(j)\chi_4(s),
\tag{3.7}
\]

and the second Legendre phase is

\[
 {Xk\over j}-{Xk\over s}.
\tag{3.8}
\]

Multiplying (3.4) and (3.6) yields \(k/J\); (3.7)--(3.8) reconstruct
the expansion of \(|S_k|^2\), proving the stationary-main identity
(2.3).

# 4. First doubtful or unproved step

Identity (2.3) is not a bound. After the diagonal is removed, its two
sides are the same unresolved signed energy in dual coordinates. The
first unproved step remains either

\[
 \sum_{k\asymp Q}|P_k|^2_{\rm off}\ll Q^2X^\varepsilon
\]

or equivalently the Round-67 reciprocal off-diagonal bound. A further
application of either one-dimensional B-process simply repeats the
involution.

# 5. Required control test and outcome

- Difference and character algebra: pass by (3.1).
- Cross-residue half-step: retained because all positive odd \(q\) are
  recombined before introducing \(d\).
- First saddle, curvature, and square phase: pass by (3.2)--(3.3).
- Actual symbol: pass by the exact ratio evaluation (3.4).
- Odd-lattice density and character restoration: pass by (3.5)--(3.7).
- Reciprocal return phase and normalization: pass by (3.8) and \(k/J\).
- Hard edges and full cone: not claimed; they remain outside this fixed
  smooth interior calculation.
- Estimate/exponent: fail as a closure; the transform is involutive.

The conductor's bounded constant-symbol computation was diagnostic only
and is not used in this proof.

# 6. Dependencies and exact artifacts used

- `rounds/codex-managed/m9-m1-joint-reciprocal-large-sieve/synthesis.md`;
- `rounds/codex-managed/m9-m1-square-root-product-offdiagonal/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-square-root-product-offdiagonal/actual_symbol_addendum.md`;
- the accepted graph node
  `M9-M1-joint-reciprocal-energy-Bprocess-reduction`.

No external theorem is imported. The algebra and stationary constants
were rederived locally. The complete twice-transformed error ledger is
not listed as a dependency because it has not been proved.

# 7. Recommended state effect

Promote the exact actual ratio-symbol factorization and the scoped
two-step stationary involution as a reduction/no-go. Retain RSLS, the
square-root-product energy, GAR, M9-M1, M9, and the exponent open. Future
work must introduce cancellation not invariant under this reciprocal
duality; repeating Poisson/B-process or citing generic Hankel
self-reciprocity cannot close the target.
