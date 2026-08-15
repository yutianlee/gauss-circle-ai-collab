# Round 32 blind report: common physical-height kernel definition obstruction

Task: blind_common_kernel_identity  
Role: statement-only blind rederivation  
Allocation: 100% analytical/algebraic; no computation and no external theorem

## 1. Result: local identity and global definition obstruction

The permitted accepted statements determine an exact regular
physical-height kernel only on a separated \(R_1\) saddle patch:
\[
 K_{R_1}(L,\nu)=
 -{i f_b(L)\over2A\{A+i(L-\nu)/2\}}
 +{f_b(\nu)-f_b(L)\over
 (L-\nu)\{A+i(L-\nu)/2\}}.                         \tag{32.1}
\]
There it has the accepted weighted
\(\lambda^{-2}/\lambda^{-3}\) symbol bounds.

They do not license an exact global \(K_{\rm complete}\). The first
obstruction is definitional. The equality
\[
 R_1=\omega G+(1-\omega)R_1-\omega E_1             \tag{32.2}
\]
holds only after the complete same-mask endpoint image is assigned to its
endpoint ledger. The permitted statements do not display the radial
endpoint and horizontal-side kernels, their orientations, or their
\(\rho\)-Taylor coefficients. They likewise do not give the exact
\(v=0\) axial subtraction. Forming one global kernel would therefore
invent missing terms.

The first missing coefficient is the constant Taylor coefficient of the
ownership defect
\[
 {\cal E}_{\rm own}
 ={\cal H}_G-{\cal H}_{E_1}-{\cal H}_{R_1}           \tag{32.3}
\]
after every endpoint, side, mask, floor, and star is placed on one common
finite contour. Algebra forces (32.3) to vanish when common ownership is
established, but the supplied statements do not define its three terms
globally enough to check this. Its ordinary \(L\)-derivative is the next
missing coefficient.

Thus the global weighted bound is neither proved nor refuted. The rigorous
outcome is an exact definition obstruction, a local kernel derivation, and
a conditional common-kernel lemma.

## 2. Exact statement and hypotheses

### Separated kernel

Fix one signed saddle component with
\[
 \lambda={\pi q\sqrt{Xx}\over D_j},\qquad
 |L|\asymp\lambda,\qquad |A|\asymp\lambda,          \tag{32.4}
\]
separated from \(\rho=0\), \(v=0\), saddle entry and exit, connector
changes, and finite-height faces. Let
\[
 H(L,\nu)={f_b(\nu)\over A+i(L-\nu)/2}.             \tag{32.5}
\]
After the single combined diagonal/log subtraction, define
\[
 K_{R_1}(L,\nu)
 ={H(L,\nu)-H(L,L)\over L-\nu}.                    \tag{32.6}
\]
Its continuous diagonal value is understood. Equation (32.6) equals
(32.1). At fixed \(b>0\), the accepted profile decay gives an integrable
weight \(w_b\) such that
\[
 |K_{R_1}|\ll_b\lambda^{-2}w_b(\nu),\qquad
 |\partial_LK_{R_1}|_{\nu\ {\rm fixed}}
 \ll_b\lambda^{-3}w_b(\nu).                        \tag{32.7}
\]

### Conditional global definition

Let \({\mathscr P}\) be a linear regularization operator that:

1. extracts the \(u=0\) delta trace and constant-numerator face log once;
2. assigns the \(v=0\) residue to a separate axial ledger;
3. retains every radial endpoint, endpoint star, and finite radial side;
4. uses identical masks, domains, and conventions on \(G,E_1,R_1\).

If complete common-contour numerators
\({\cal H}_G,{\cal H}_{E_1},{\cal H}_{R_1}\) are supplied, then the
desired exact definition is
\[
 K_{\rm complete}
 ={\mathscr P}\{\omega{\cal H}_G
 +(1-\omega){\cal H}_{R_1}-\omega{\cal H}_{E_1}\}. \tag{32.8}
\]
This is conditional because the necessary endpoint, side, and axial
inputs to \({\mathscr P}\) are absent from the permitted statements.

If, additionally, the axial profile has an exact split
\[
 f_b(\nu)={c_b\over b+i\nu}+f_b^{\rm reg}(\nu),     \tag{32.9}
\]
the residue is extracted once, the remainder and its required derivatives
have a common \(L^1\) majorant \(w_b\) with polylogarithmic \(b^{-1}\)
loss, and every radial side satisfies
\[
 |K_{\rm side}|\ll X^\varepsilon\lambda^{-2}w_b,\qquad
 |\partial_LK_{\rm side}|\ll
 X^\varepsilon\lambda^{-3}w_b,                    \tag{32.10}
\]
with summable \(U,V,S\) tails, then (32.8) obeys
\[
 |K_{\rm complete}|\ll X^\varepsilon\lambda^{-2}w_b,\qquad
 |\partial_LK_{\rm complete}|_{\nu\ {\rm fixed}}
 \ll X^\varepsilon\lambda^{-3}w_b.                \tag{32.11}
\]
The accepted physical-height finite-section lemma then preserves the
local \(q^{-2}\) normalization. Hypotheses (32.9)-(32.10) are open.

## 3. Proof or derivation

Subtracting (32.5) at \(\nu=L\) gives
\[
\begin{split}
 {H(L,\nu)-H(L,L)\over L-\nu}
 ={}&{f_b(\nu)-f_b(L)\over
 (L-\nu)\{A+i(L-\nu)/2\}}\\
 &+{f_b(L)\over L-\nu}
 \left\{{1\over A+i(L-\nu)/2}-{1\over A}\right\},
\end{split}
\]
and the last line is the first term of (32.1). The integral divided
difference
\[
 {f_b(\nu)-f_b(L)\over\nu-L}
 =\int_0^1f_b'(L+t(\nu-L))\,dt                   \tag{32.12}
\]
removes the diagonal pole. Differentiating at fixed physical \(\nu\),
not fixed \(\mu=L-\nu\), uses one further profile derivative and the
accepted \(A'(L)\). The fixed-\(b\) decay proves (32.7), as already
licensed by Round 31.

Assume now that every term in (32.8) has common ownership. Then
\[
 {\cal H}_G-{\cal H}_{E_1}-{\cal H}_{R_1}=0.        \tag{32.13}
\]
For any compatible derivative \(D\),
\[
\begin{split}
 D\{\omega{\cal H}_G+(1-\omega){\cal H}_{R_1}
 -\omega{\cal H}_{E_1}\}
 ={}&D{\cal H}_{R_1}\\
 &+(D\omega)({\cal H}_G-{\cal H}_{E_1}
 -{\cal H}_{R_1})\\
 &+\omega D({\cal H}_G-{\cal H}_{E_1}
 -{\cal H}_{R_1})
 =D{\cal H}_{R_1}.                                  \tag{32.14}
\end{split}
\]
The second derivative similarly cancels every \(D\omega,D^2\omega\)
term. Expanding (32.13) in \(\rho\) forces all Taylor coefficients of
(32.3) to vanish. Linearity of \({\mathscr P}\) ensures one combined
diagonal/log subtraction.

If instead one representation still lacks a finite side, write
\[
 {\cal H}_G={\cal H}_{E_1}+{\cal H}_{R_1}
 +{\cal E}_{\rm side}.                              \tag{32.15}
\]
Then (32.14) contains
\[
 (D\omega){\cal E}_{\rm side}
 +\omega D{\cal E}_{\rm side}.                     \tag{32.16}
\]
The constant \(\rho\)-Taylor coefficient of
\({\cal E}_{\rm side}\) is therefore the first missing datum. This proves
why exact endpoint/side ownership must precede any global bound.

Under the conditional hypotheses, (32.7), (32.9)-(32.10), the triangle
inequality, and (32.14) prove (32.11). The accepted stationary numerator
\((D_j/q)\lambda\) then yields
\[
 {D_j\over q\lambda}
 ={D_j\over q^2\theta_j(x)},\qquad
 \theta_j(x)={\pi\sqrt{Xx}\over D_j},              \tag{32.17}
\]
which is the local \(q^{-2}\) ledger.

## 4. First doubtful or unproved step

The first missing exact datum is the common radial endpoint and
horizontal-side numerator needed to replace the symbols in (32.8) by
actual formulas. Equivalently, it is
\[
 {\cal E}_{\rm own}(0;L,\nu),                       \tag{32.18}
\]
the \(\rho^0\) coefficient of the ownership defect with all sides and
endpoint stars present. The next datum needed by (32.11) is
\(\partial_L{\cal E}_{\rm own}(0;L,\nu)\).

After this definition seam, the next missing coefficient is the axial
residue \(c_b\) in (32.9) together with a \(b\)-uniform majorant for the
remainder. No quantitative finite-side or joint \(U,V,S\) tail estimate
is supplied. These gaps precede a full \(h,D_j,x,q\) and external
\(X^{1/4}\) normalization ledger.

## 5. Control tests and outcomes

### Common-kernel-ownership

**Fail globally; pass locally.** Equation (32.1) is exact on a separated
\(R_1\) patch. Equation (32.8) is the correct conditional global
definition, but its endpoint, side, and axial inputs are absent. A more
explicit formula would invent data excluded by the statement-only task.

### Rho-Taylor-and-residue

**Conditional algebraic pass; coefficient audit open.** Common ownership
forces every coefficient of (32.3) and every cutoff derivative to cancel.
Without the endpoint/side ledger, the first unknown is (32.18). The
\(v=0\) axial residue remains separate and is not double-counted as an
artificial \(\rho=0\) residue.

### Physical-height-derivative

**Pass locally; open globally.** Equation (32.7) differentiates at fixed
\(\nu\), avoiding the false fixed-\(\mu\) route. Globally, the unknown
terms are \(\partial_L{\cal E}_{\rm own}\), the derivative of the axial
regular remainder, and the finite-side derivatives. None has an accepted
\(\lambda^{-3}\) bound.

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were read or used:

1. protocol.md;
2. state/active_campaign.yml;
3. rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/synthesis.md;
4. rounds/codex-managed/m9-m1-beta-regular-finite-part-symbol-bv/synthesis.md.

No proof graph, proof draft, excluded conductor review, Round-32 claimant
report, computation, or web source was read or used.

## 7. Recommended state effect

- **Retain the scoped local result:** the separated kernel (32.1), its
  ordinary fixed-\(\nu\) derivative, and the accepted
  \(\lambda^{-2}/\lambda^{-3}\) bounds away from all seams.
- **Promote as conditional algebra only:** with genuinely common endpoint
  and side ownership, all \(\rho\)-Taylor defects and omega-derivative
  terms cancel and one regularization yields (32.8).
- **Record a definition obstruction:** the permitted accepted state omits
  the radial endpoint/horizontal-side and exact axial inputs needed to
  define \(K_{\rm complete}\). The first missing coefficient is
  (32.18), followed by its physical \(L\)-derivative.
- **Retain open:** the axial \(b\)-uniform split, radial-side bounds, joint
  \(U,V,S\) exhaustion, full normalization, complete beta bound, M9-M1,
  M9, and the Gauss-circle target.
