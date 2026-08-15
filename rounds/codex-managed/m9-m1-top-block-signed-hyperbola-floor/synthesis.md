# Round 58 synthesis: exact endpoint Fourierization isolates a short twisted-divisor core

## 1. Conductor decision

Round 58 closes with a proved floor/Fourier reduction and a target-safe
endpoint residual.  It does not prove the high-shell square-root estimate.
The remaining problem is exactly a signed length-\(R\) twisted-divisor sum
with the actual angular symbol.

## 2. Exact floor reduction

For \(Y=R^2\asymp\sqrt X\), \(J=[A,B]\) of length at most \(R\), and
\(R/4<h\le R/2\), define

\[
 L_h={A+h-1\over2h},\quad U_h={B+h\over2h},\quad
 q_h=2\lfloor L_h\rfloor+1,
\]

\[
 \nu_h=\lfloor U_h\rfloor-\lfloor L_h\rfloor\in\{0,1,2\}.
\]

Then the complete actual row is

\[
 (-1)^{\lfloor L_h\rfloor}
 \{I_1(\nu_h)F_h(q_h)-I_2(\nu_h)F_h(q_h+2)\},
\]

with \(I_1(v)=v(3-v)/2\), \(I_2(v)=v(v-1)/2\).  It handles empty,
singleton, pair, point-window, endpoint, and star cases exactly.

## 3. Fejer residual theorem

The character zero mode cancels only with the full Abel boundary ledger;
the selector mode \(\ell/(2h)\) remains.  For the four endpoint arguments,
a divisor-incidence count proves

\[
 \sum_{R/4<h\le R/2}\kappa_T((N+ch)/(dh))
 \ll_\varepsilon X^\varepsilon(R/T+1).
\]

This includes exact integer jumps.  Hence a floor-compatible Vaaler
expansion at \(T=\lceil\sqrt R\rceil\) has total remainder
\(O_\varepsilon(X^\varepsilon\sqrt R)\), already at the desired shell
scale.  The hostile pointwise bound is valid but weaker.

## 4. Exact survivor

The finite modes retain the discontinuous \(q_h\) in the phase and actual
symbol.  Equivalently,

\[
 P_J=\sum_{n=A}^{B}e(\sqrt{Xn})
 \sum_{\substack{h\mid n,\ R/4<h\le R/2\\n/h\ {m odd}}}
 \chi_4(n/h)\widetilde{\mathcal A}_X(h,n/h).
\]

This short twisted-divisor sum must be
\(O_\varepsilon(X^\varepsilon\sqrt R)\).  Every fixed-floor branch and
every fixed-denominator fibre has only \(O(1)\) samples, so local derivative
tests do not aggregate.  Termwise absolute values retain \(R\) capacity,
sharp on the inherited actual fourth-power family.

## 5. Rejected shortcuts

- The unweighted signed row count is not the actual weighted row.
- Character mean zero does not remove the geometric selector mode.
- The positive Fejer residual cannot be discarded, though it is now bounded.
- A large real reciprocal frequency is not a modulo-one derivative gap.
- Standard modewise large sieve, rectangular monomial sums, and
  Kloosterman-fraction theorems do not match the complete moving symbol.

## 6. State effect

Promote the exact floor identity, zero-mode ledger, sampled Fejer residual,
twisted-divisor return, and scoped capacity no-go.  Retain the signed
high-shell estimate, lower shell, alpha transition, M9-M1, M9, and target
open.  No exponent changes.

## 7. Next strategy

Attack the short twisted-divisor core directly.  Expand the divisibility
constraint or apply a finite quadratic/Poisson completion in the radial
offset before taking absolute values.  The decisive question is whether the
near-fourth-power quadratic phase and \(\chi_4\)-twisted restricted-divisor
symbol yield a genuine \(\sqrt R\) completion, or whether exact reciprocity
returns to the same Hardy/GAR kernel.  All actual profiles and stars must
remain attached.
