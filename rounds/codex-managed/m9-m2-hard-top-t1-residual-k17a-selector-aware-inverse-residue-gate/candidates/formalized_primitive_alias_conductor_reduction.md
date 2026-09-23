# Formalized Round-177 candidate

## Proposed promotion

Promote the exact primitive alias decomposition, the low-reduced-conductor
strict sector, and the scoped positive-energy self-return proved in
(177.K3)--(177.K33) of
"proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_alias_conductor_reduction.md".
Retain (177.K34)--(177.K35) only as explicit sufficient open estimates;
they are not part of the proposed promotion.

For every fixed \(B>0\), the mathematical content is:

\[
 \left|
 \mathfrak C^{\rm rem}_{\rm low\text{-}\kappa,\,
 {\rm alias\text{-}cond}\le(\log(2X))^B}
 \right|
 \ll_{B,\delta,\gamma,\varepsilon}L^2X^\varepsilon.
\tag{177.C9}
\]

The exact complement is the complete literal low-cross-gcd identity after
primitive folding, restricted to

\[
 q=\frac{u/(u,n)}{(\ell,u/(u,n))}>(\log(2X))^B.
\tag{177.C10}
\]

This transform packet contains the physical sector
\(u/(u,n)\le(\log(2X))^B\).

## Proof interfaces to review

1. \(E_u(\pm\bar v n)=E_{u_0}(\pm\bar v n_0)\) with
   \(u_0=u/(u,n)\), and
   \(\sum_{j<(u,n)}c_u(\ell+ju_0)=c_{u_0}(\ell)\).
2. Exact-conductor coefficient mass
   \[
   \sum_{u_0/(\ell,u_0)=q}|c_{u_0}(\ell)|
   \ll(q/u_0)\log(2q).
   \]
3. Fixed-\((\kappa,u,u_0)\) literal atom count \(O(u_0L)\).
4. Fixed-\((\kappa,u)\) divisor sum
   \(O(LQ_B\log(2Q_B)\tau(u)^2)\), followed by
   \(\sum_\kappa O(L/\kappa)\).
5. Exact rank-one \(TT^*\) self-return, alias-Parseval bucket identity,
   one-square-root \(L\sqrt q\) ledger, and failure of the
   complementary-divisor orientation pairing.

## State recommendation

Create one subordinate proved-internal reduction depending only on the
accepted Round-176 cross-gcd alternating-fibre reduction. Update the
Round-176 reduction and its residual parents only by evidence and next
action, and add the new proved reduction as one provenance dependency of
the complete hard-TOP owner. This edge changes no status and creates no
implication. Reject claims that the low-conductor packet proves high conductor,
that one square-root gain suffices, that alias Parseval contracts the
physical block, or that anchor antisymmetry pairs the two literal
orientations.

Leave (177.C10), complete K17a, the complete residual scalar, every parent,
bridge, and theorem open, with no exponent owner or numerical exponent
value changed. Close Round 177 under
"strict_k17a_low_cross_gcd_selector_aware_sector".
