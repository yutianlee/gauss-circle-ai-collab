# Conductor review: Fejer dispersion, aliases, and source scope

Campaign: m9-m2-balanced-double-far-shifted-divisor-fork

Decision: pass as a scoped mechanism obstruction; no target estimate.

## 1. Exact Fejer inequality

Let

\[
 b_n=c_B(n)e(R\sqrt n)
\]

be zero-extended to an interval of length \(N_B\asymp L^2\), and set

\[
 \Gamma(r)=\sum_n b_n\overline{b_{n+r}}.
\]

For \(1\le H\le N_B\), sliding-window Cauchy gives

\[
 \left|\sum_n b_n\right|^2
 \le P_H\mathfrak D_H,
\qquad
 P_H={N_B+H-1\over H},
\]

\[
 \mathfrak D_H
 =
 \Gamma(0)+2\Re\sum_{1\le r<H}
 \left(1-{r\over H}\right)\Gamma(r)
 =
 {1\over H}\sum_m
 \left|\sum_{j=1}^H b_{m+j}\right|^2.
\]

The normalization, positivity, and full-product diagonal
\(\Gamma(0)=O_\varepsilon(L^2X^\varepsilon)\) are correct.

## 2. Owner amplification

For \(2\le H\le L\), the available radial-corridor estimate gives the
certified allowance

\[
 P_H\sum_{r<H}|\Gamma(r)|
 \ll_\varepsilon
 {L^2\over H}L^2(H+1)X^\varepsilon
 \ll_\varepsilon L^4X^\varepsilon.
\]

For \(L\le H\le N_B\), restoring either complete Round-114 corridor through
its accepted absolute owner gives only

\[
 P_HL^3X^\varepsilon
 \ll_\varepsilon
 \left({L^5\over H}+L^3\right)X^\varepsilon.
\]

These are upper allowances, not matching lower bounds. They prove exactly
that the existing owners do not certify any fixed-power shortening
\(H\le L^{2-\delta}\). Length
\(H=L^{2-o(1)}\) may absorb the remaining subpower factor into
\(X^\varepsilon\), but then the window still contains the full power range
of shifts. At \(H\asymp N_B\), the dispersion is full-scale and has not
reduced the double-far survivor.

The determinant gate is pair-dependent inside the two divisor fibres and
is not a scalar positive-semidefinite mask in \((n,r)\). Inserting it into
the Fejer square without a new factorization is invalid. Paying its
complement invokes precisely the amplified corridor allowance above.

The two-dimensional \(P\)-by-\(Q\) Fejer window has prefactor
\(\asymp L^2/(PQ)\) and the same conclusion: a target-saturating corridor
can be reused only at full power area \(PQ=L^{2-o(1)}\). A genuinely new
signed local-energy estimate could bypass this no-go; the route itself is
not disproved.

## 3. Poisson and stationary-mode scope

For \(f(x)=R\sqrt x\) on \(x\asymp L^2\),

\[
 f'(x_m)=m,\qquad
 x_m={X\over4m^2},\qquad
 f(x_m)-mx_m={X\over4m},\qquad
 |f''(x)|\asymp1.
\]

Thus the smooth bulk B-process has dual length \(\asymp L^2\), stationary
amplitude \(\asymp1\), and returns a reciprocal phase. This is
capacity-preserving. It is not yet a literal transform theorem for the
arithmetic \(c_B(n)\).

For the shifted smooth scalar phase, the discovery report correctly labels
the \(L^4\) modewise figure as potential bulk capacity only. The
zero-frequency Poisson summand remains present; it merely has no interior
critical point on the double-far bulk. Boundary terms and literal support
crossings remain.

Writing \(p=2s\) changes the character into \(e(s/2)\). It shifts the dual
stationary family by a half lattice and does not remove its nonzero modes.
Likewise, the exact Hessian determinant proves continuous nondegeneracy but
not an integer-alias count, injectivity, lattice discrepancy, or
modulo-one cancellation. These qualifications incorporate the independent
hostile audit of the discovery draft.

## 4. Primary-source fit

Alex Cowan's A twisted additive divisor problem,
https://arxiv.org/abs/2304.12572, has hypotheses incompatible with the
literal self-correlation: prime level, even nontrivial characters with
nontrivial product, nonzero complex powers, and parameters other than the
cutoff fixed. Here the conductor is four, \(\chi_4\) is odd,
\(\chi_4^2\) is principal, the powers are zero, shifts grow through
\(L^2\), and the coefficient has divisor truncation, a gcd mask,
determinant deletion, and a coupled nonlinear weight.

Fernando Chamizo's The Additive Problem for the Number of Representations
as a Sum of Two Squares,
https://doi.org/10.1007/s00009-021-01959-3, proves a nonzero main term and
uniform-shift errors for the complete \(r_2(n)r_2(n+m)\) correlation. It
does not state the literal truncated, slanted, determinant-deleted,
simultaneously oscillatory shift sum. Moreover, at \(m\asymp x\) its
displayed \(x^{17/23+\varepsilon}\) error would cost
\(x^{40/23+\varepsilon}\) after a triangle sum over \(O(x)\) shifts,
larger than the \(x^{3/2}\) energy budget.

Both sources are useful diagnostic controls. Neither is a proof antecedent.

## 5. Smallest lawful continuation

Any continuation of this mechanism must prove, for a fixed
\(\delta>0\) and some \(L\le H\le L^{2-\delta}\),

\[
 \Gamma(0)+2\Re\sum_{1\le r<H}
 \left(1-{r\over H}\right)\Gamma(r)
 \ll_\varepsilon LHX^\varepsilon,
\]

with character, both gcd weights, both slanted symbols, both corridor
projectors, and all crossings retained jointly. Equivalently, it may prove
the target for the oscillatory zero-subtracted remainder. This is a new
signed theorem, not a consequence of Round-114 owner reuse.

## 6. Review decision

Promote only the fixed-power Fejer owner-amplification obstruction and the
capacity-preserving transform audit. Reject claims that zero-frequency
nonstationarity, a half-lattice shift, continuous Hessian nondegeneracy, or
either external source closes the packet. Retain the actual signed
double-far estimate open.

Evidence:

- rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/reports/literal_dispersion_attack.md
- rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/reports/actual_symbol_main_term_hostile.md
- rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/controls/conductor_round115_prechecks.md
