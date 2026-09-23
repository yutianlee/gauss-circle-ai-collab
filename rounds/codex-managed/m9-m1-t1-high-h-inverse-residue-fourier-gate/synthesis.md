# Round 187 synthesis

- Campaign: `m9-m1-t1-high-h-inverse-residue-fourier-gate`
- Round: 187
- Generated: 2026-08-29T15:46:47+08:00
- Starting graph:
  `d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a`
- Closing label: `strict_high_h_inverse_residue_fourier_sector`
- Durable kernel:
  `a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2`
- Numerical theorem evidence: none

## Outcome

Round 187 proves a genuine strict transformed sector of the exact
high-height hard-M1 \(t=1\) residual.  The odd-modulus inverse-residue
anchor has the exact Fourier coefficient

\[
 c_U(k)=\frac{2}{U\{1+e(-k/U)\}},
\]

with mean \(1/U\).  The complete \(U=1\) contribution, every exact
conductor \(q_U(k)\le H_B\), every remaining mode with \(U\le4H_B\),
and every ordinary edge mode \(0<|k|_U\le H_B\) for \(U>4H_B\) are
absolutely target-safe at

\[
 O_{B,\varepsilon}(L^2X^\varepsilon).
\]

The exact-conductor gain comes from \(u=gU\), \(n=gh\): literal support
gives \(h\ll U\) and \(O(UL)\) atoms at fixed
\((\kappa,u,U)\), while conductor \(q\) has mass
\(O((q/U)\log(2q))\).

## Exact remaining interface

The exact complement has

\[
 U>4H_B,\qquad q_U(k)>H_B,\qquad |k|_U>H_B,
\]

with all \(h,v,t,k\), both orientations, every selector and endpoint
field, and one outer real part still joint.  Its positive capacity is

\[
 O_\varepsilon(YL^2X^\varepsilon),
\]

so the first open relation still needs the complete factor \(Y\):

\[
 \Re\mathscr R_{Y,H_B}^\sigma
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\]

Centered exact conductors self-return to the original orientation block;
for prime \(U\) this is literal.  The two near-half modes retain
constant Fourier \(\ell^2\)-mass.  Positive Fourier, Poisson, alias, or
conductor energy and bare alternation therefore provide no automatic
gain.  These are mechanism controls, not literal lower bounds and not a
disproof of the open one-sided relation.

## Proof status

The complete high-height relation and exact original-\(t=1\) residual
remain open.  Even their completion would leave every original
\(t\ge2\) small-\(G\) incidence and the large-\(G\) near-resonant
complement open.  Hence the complete hard small-\(t\) owner, the
independent smooth M1 parent, GAR, M9--M1, every M2 parent, endpoint
uniformity, M9, both bridges, and the Gauss circle conjecture remain
open.

There is no global exponent improvement: internally proved \(1/3\),
accepted external \(0.3144831759740614\ldots\), target \(1/4\).

## State decision

The proposed patch creates one proved subordinate reduction and updates
only the still-open hard-M1 small-\(t\) residual owner with that
dependency, its evidence, and the narrower exact complement.  It changes
no complete owner, inherited status, implication, blocker, bridge,
theorem, or exponent.

