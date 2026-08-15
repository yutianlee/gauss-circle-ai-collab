# Round 55 conductor adjudication: low angular margins close

## 1. Decision

Promote the scoped top-block low-leg theorem.  All three reports prove the
same fixed-leg curvature/trivial-crossover estimate, the statement-only
derivation remained isolated, and the hostile audit found no seam failure.
The result removes every polylogarithmic low-
\(h\) margin from the critical top block.  It does not estimate the
remaining intermediate-\(h\), large-\(q\) core.

## 2. Canonical theorem

Let \(I_Y\subset[cY,CY]\cap\mathbb Z\) be consecutive, with

\[
 Y\asymp \sqrt X,\qquad R\asymp \sqrt Y.
\]

For every consecutive \(J\subseteq I_Y\) of length at most \(R\), retain
the exact active coefficient

\[
 \Omega_X^*(hq,h)=\sum_j {f1}_{h\le H_j}
 \Phi\!\left({h\over H_j+1}\right)
 \left[w_j\!\left(2\sqrt{Xh/q}\right)\right]^*,
 \qquad H_j=\lfloor D_jX^{-1/4}\rfloor,
\]

all height floors and angular stars, and the independent radial endpoint
star.  If the union \(h\le H\) or \(q\le Q\) is owned disjointly by

\[
 \{h\le H\}\ \dot\cup\ \{h>H,\ q\le Q\},
\]

then

\[
 \left|\sum_{n\in J}^{*}A_{X;H,Q}(n)n^{-3/4}e(\sqrt{Xn})\right|
 \ll_\varepsilon X^\varepsilon {H+Q\over\sqrt Y}.
\tag{55.1}
\]

The exact moving-window identity (or a disjoint partition into such
windows) therefore gives

\[
 |S_{Y;H,Q}|\ll_\varepsilon X^\varepsilon(H+Q).
\tag{55.2}
\]

Thus \(H+Q\le(\log(2X))^B\) is target-safe.

## 3. Proof seam audit

For either fixed leg \(\ell=h\) or \(q\), the complementary product
interval has length \(M_\ell\ll R/\ell+1\), while the exact square-root
phase has one-signed curvature

\[
 |f_\ell''|\asymp {\ell^2\over R}.
\]

For \(\ell\le\sqrt R\), the finite second-derivative estimate yields

\[
 M_\ell |f_\ell''|^{1/2}+|f_\ell''|^{-1/2}
 \ll \sqrt R+{\ell\over\sqrt R}+{\sqrt R\over\ell}
 \ll\sqrt R.
\]

For \(\ell>\sqrt R\), the trivial length is already \(O(\sqrt R)\).
After the factor \(n^{-3/4}\asymp Y^{-3/4}\), one fixed leg costs
\(Y^{-1/2}\).

The complete sampled amplitude has uniformly bounded sup-plus-variation
on every product window.  The angular coordinate is monotone and changes
by relative size \(O(R/Y)\), hence encounters only \(O(1)\) dyadic
profiles.  Each fixed profile has bounded normalized variation; a fixed-
\(q\) height factor has one bounded floor jump; the hard top, angular
equality star, radial star, and artificial \(h>H\) edge are separate
bounded owners.  This validates Abel transfer for the actual amplitude,
not merely for a schematic smooth weight.

Splitting odd \(q\) into its two residue classes makes \(\chi_4(q)\)
constant and changes only fixed constants.  Perfect-fourth-power examples
can make the first derivative integral or half-integral, so no derivative
gap is available; the one-signed second derivative remains valid.

## 4. Angular support and exact survivor

Every active profile satisfies

\[
 d=2\sqrt{Xh/q}\le y=\lfloor\sqrt X\rfloor.
\]

Consequently

\[
 q\ge {4X\over y^2}h\ge4h,\qquad q\ge2\sqrt n,
 \qquad h\le {1\over2}\sqrt n.
\tag{55.3}
\]

Hence a polylogarithmic low-\(q\) margin is actually empty.  With
\(H=(\log(2X))^B\), the unresolved critical core is more precisely

\[
 (\log(2X))^B<h\le {1\over2}\sqrt n\asymp\sqrt Y,
 \qquad q={n\over h}\ge2\sqrt n\asymp\sqrt Y.
\tag{55.4}
\]

Calling this range simply “balanced” obscures the actual cone; the next
round should treat it as an intermediate-\(h\), large-\(q\) core.

## 5. Scope

The theorem is a physical radial estimate.  It proves neither the full
signed shifted-correlation theorem nor the connector-completed alpha
transfer.  It does not close GAR, M9-M1, M9, or the Gauss-circle target,
and it proves no new discrepancy exponent by itself.

## 6. Evidence and controls

- Discovery: `reports/low_leg_curvature_attack.md`.
- Strict statement-only rederivation: `reports/blind_fixed_leg_rederivation.md`.
- Independent hostile seam audit: `reports/top_margin_hostile_audit.md`.
- Report hygiene: exactly seven required sections in every report; no
  forbidden control bytes or replacement characters; `git diff --check`
  passes on the campaign directory.
- Effort allocation: 100% analytical/algebraic, 0% numerical.

## 7. State recommendation

Create one proved internal low-leg-margin node containing (55.1)--(55.4).
Add it as partial progress under GAR and refine GAR's next action to the
intermediate-\(h\), large-\(q\) core.  Record that first-derivative-gap
and all-leg summation routes are invalid.  Make no downstream promotion.
