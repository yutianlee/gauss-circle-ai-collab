# Round 176 hyperbola-coordinate post-repair verification

## 1. Overall finding

\[
\boxed{\textbf{GREEN}}
\]

The repaired candidate incorporates the required seam repairs.  Its
promoted statements follow from the literal squarefree product support,
and every capacity obstruction is explicitly limited to a named procedure
followed by positive recombination.  In particular:

- the cross-gcd and blind coordinates agree exactly in both orientations;
- the original divisor gcd is fibre-stable;
- the canonical anchor has the stated primitive Fourier modulus and
  logarithmic normalized algebra norm;
- the hyperbola row count proves the fixed-proportion owner theorem without
  needing individual near-square support;
- the derivative and exponent-pair formulas are restricted to full
  fixed-relative cells; and
- the two-variable transform calculation is only a smooth-cell,
  termwise-positive dual-volume audit, not a lower bound or a global
  impossibility theorem.

The full non-polylogarithmic K17a estimate remains open outside the strict
high-cross-gcd sector.

## 2. Exact coordinate and gcd verification

In the plus orientation the candidate writes

\[
 d=\kappa u,\quad d'=\kappa u+2s,\quad
 m'=\kappa v,\quad m=\kappa v+2w,\quad
 sv-wu=n>0,\quad (u,v)=1.
\]

Then

\[
 d'm'-dm=2\kappa(sv-wu)=2\kappa n.
\]

The primitive equation has exactly the solutions

\[
 s=s_0+ut,\qquad w=w_0+vt,\qquad
 s_0=[\bar v n]_u,\qquad w_0={s_0v-n\over u}.
\]

The opposite orientation gives (uw-sv=n>0) and the canonical residue
\(s_0=[-\bar v n]_u\).  The orientations are disjoint, and the positivity
conditions \(s_t,w_t\ge1\) plus zero extension retain precisely the
original incidences.  Thus multiplicity one in (176.C8)--(176.C10e)
passes.

Both endpoint products advance by

\[
 2\kappa uv.
\]

Since (kappa,u) are odd,

\[
 \chi_4(d')\chi_4(d)=(-1)^s
 =E_u(\pm\bar v n)(-1)^t.
\]

For a nonzero plus atom, squarefreeness of
\((\kappa u+2s)\kappa v\) implies \((\kappa,s)=1\).  Hence

\[
 (d,d')=(\kappa u,\kappa u+2s)
 =(\kappa u,s)=(u,s)=(u,n).
\]

The minus orientation is identical using its other squarefree endpoint.
Therefore (176.C11) is exact and the original cutoff is constant along the
fibre.

To compare with the blind variables, put

\[
 g=(d,d')=(u,n),\qquad u=gu_0,\qquad n=gn_0.
\]

Then in the plus orientation

\[
 a=\kappa u_0,\qquad m_0=\kappa v,\qquad
 k={s\over g},\qquad K={\kappa n\over g}=\kappa n_0,\qquad
 (a,m_0)=\kappa.
\]

For the minus orientation the same formula has \(K=-\kappa n_0\).
Consequently

\[
 2g|K|=2\kappa n,\qquad
 {2gam_0\over(a,m_0)}=2\kappa uv,\qquad
 (-1)^k=(-1)^s,
\]

because (g) is odd.  This verifies (176.C20)--(176.C21) and the exact
cross/blind dictionary.  The reuse of (n) for the cross determinant,
while the blind low complement is denoted (m_0), is consistent.

The even complement branch is also correct.  If (v=2v_1), squarefreeness
forces (v_1) odd and both products to be \(2\pmod4\).  It then forces
(w) even, so (n=sv-wu) or (n=uw-sv) is even.  Since
(w_t=w_0+vt), that branch is fibre-stable, while (s_t=s_0+ut)
changes parity at every step.

## 3. Primitive Fourier modulus and norms

For odd (m), direct geometric summation gives

\[
 \widehat E_m(k)=\sum_{a=0}^{m-1}(-1)^ae(-ka/m)
 ={2\over1+e(-k/m)}
 ={e(k/(2m))\over\cos(\pi k/m)}.
\]

Thus

\[
 {1\over m}\sum_{k\bmod m}|\widehat E_m(k)|
 \ll\log(2m).
\]

If \(c_m(k)=\widehat E_m(k)/m\), Parseval gives

\[
 \sum_{k\bmod m}|c_m(k)|^2=1.
\]

At (k=(m-1)/2),
\(|\widehat E_m(k)|=1/\sin(\pi/(2m))\asymp m\), so
\(\|c_m\|_\infty\asymp1\).  The large near-half alias therefore cannot
be removed by a small-coefficient argument.

For the primitive modulus, let (g=(u,n)), (u=gu_0), and (n=gn_0).
The congruence \(s_0v\equiv\pm n\pmod u\) and ((v,u)=1) imply
\(g\mid s_0\).  Writing (s_0=gs_0') gives

\[
 s_0'=[\pm\bar v n_0]_{u_0}.
\]

Since (g) is odd,

\[
 (-1)^{s_0}=(-1)^{s_0'},\qquad
 E_u(\pm\bar v n)=E_{u_0}(\pm\bar v n_0).
\]

Here the same inverse representative may be reduced modulo (u_0).
Therefore (176.C12)--(176.C13a), including the primitive Fourier modulus
(u/(u,n)), are **PASS**.  They correctly demote the constant-anchor
family to a control against naive determinant pairing rather than a power
obstruction.

## 4. Robust hyperbola count and owner theorem

Fix (kappa) and write \(Y=L/\kappa\).  The inward cross product is below
both positive endpoint products, so literal product support gives

\[
 \kappa^2uv\ll L^2,\qquad uv\ll Y^2.
\]

Also \(2\kappa n<R_0\) gives \(n\ll Y\).  A row advances by
\(D=2\kappa uv\), so a product shell of length (O(L^2)) contains at most

\[
 O\!\left(1+{L^2\over\kappa uv}\right)
\]

sites from that row.  Therefore

\[
 \begin{aligned}
 C_\kappa
 &\ll X^\varepsilon
 \sum_{uv\ll Y^2}\sum_{n\ll Y}
 \left(1+{L^2\over\kappa uv}\right)\\
 &\ll X^\varepsilon\left(
 Y^3\log(2Y)+{L^2Y\over\kappa}\log^2(2Y)
 \right)\\
 &\ll {L^3\over\kappa^2}X^\varepsilon.
 \end{aligned}
\]

This uses only

\[
 \#\{(u,v):uv\ll Y^2\}\ll Y^2\log(2Y),
 \qquad
 \sum_{uv\ll Y^2}{1\over uv}\ll\log^2(2Y),
\]

and remains valid if the stronger atomwise near-square support is not used.
Every literal squarefree, selector, original-gcd, parity, endpoint, and
non-polylogarithmic condition deletes terms, while the Fejer and endpoint
coefficients are bounded.  Both orientations only alter the constant.

Consequently

\[
 \sum_{\kappa\ge K}C_\kappa
 \ll {L^3\over K}X^\varepsilon.
\]

Putting \(K=\delta L\) proves (176.C14), with constant
\(O_{\delta,\gamma,\varepsilon}(1)\), for every fixed
\(0<\delta<1/2\).  If \(delta\ge1/2\), the constraint
\(2\kappa n<R_0\) makes the sector empty up to the stated harmless ceiling
edge.  If (delta) varies, the ledger retains its explicit
(delta^{-1}) cost.  The strict fixed-proportion owner theorem is
therefore **PASS**.

The same hyperbola count shows that a hypothetical \(O(X^\varepsilon)\)
bound per primitive row would have total capacity
\(L^3K^{-2}X^\varepsilon\); this is only an optimistic comparison and is
not asserted as a theorem.

## 5. Derivative-cell and positive-transform scope

On a full fixed-relative fibre, \(T\asymp\kappa\), the shift is
\(r=2\kappa n\), and

\[
 F\asymp {2Jn\kappa\over L},\qquad
 {F\over T^2}\asymp {2Jn\over\kappa L}\gtrsim1.
\]

The last comparison follows at the power scale from
\(2\kappa n<R_0\asymp L\), \(n\ge1\), and \(J\gtrsim L^2\).  The candidate
does not import the previously disputed assertion (L^2=o(J)).

Direct differentiation gives

\[
 \Phi''(t)\asymp {2Jn\over\kappa L},\qquad
 |\Phi'''(t)|\asymp {2Jn\over\kappa^2L}.
\]

The derivative image has length \(\asymp2Jn/L\), and a stationary
coefficient has scale \((\kappa L/(2Jn))^{1/2}=T/\sqrt F\).  Absolute
dual recombination gives

\[
 \sqrt F+{T\over\sqrt F},
\]

which supplies no power saving over the trivial (T) certificate on this
cell.  This verifies (176.C15), (176.C25)--(176.C28) as a rowwise
positive-recombination audit.  It does not estimate the physical sum from
below and does not exclude signed cancellation.

For the two-variable phase

\[
 \Theta(s,w)=J\{\sqrt{\kappa v(\kappa u+2s)}
 -\sqrt{\kappa u(\kappa v+2w)}\}+{s\over2},
\]

the Hessian is diagonal and, on a fixed-relative cell,

\[
 |\det\operatorname{Hess}\Theta|\asymp {J^2\over L^2}.
\]

Because ((u,v)=1), the primitive determinant coordinate and a fibre
coordinate form a unimodular lattice change.  The determinant and fibre
lengths are \(O(L/\kappa)\) and \(O(\kappa)\), so the physical area is
(O(L)).  The gradient-image volume and one saddle size are respectively

\[
 O(J^2/L),\qquad O(L/J).
\]

Their termwise-positive product is (O(J)), while direct physical counting
is (O(L)); the better certificate is (O(L)).  Summing positively over
\((\kappa,u,v)\) gives \(O(L^3X^\varepsilon)\).

The candidate explicitly limits this calculation to smooth fixed-relative
cells followed by termwise positive dual summation.  It does not claim to
have executed Poisson on the discontinuous literal selector and does not
exclude signed dual-mode or orientation cancellation.  Thus
(176.C28a)--(176.C28b) and the route-scoped label (176.C16) are **PASS**.

The \(L^{5/2}X^\varepsilon\) one-saving figure is likewise presented only
as an optimistic positive capacity.  It is not promoted as a bound or as
physical lower mass.

## 6. Literal retention, first open step, and promotion decision

The exact identity (176.C10e) now displays, simultaneously:

- the two disjoint opposing orientations and correct conjugations;
- the Fejer factor and non-polylogarithmic determinant interval;
- the original-gcd indicator \((u,n)<\gamma L\);
- displacement positivity;
- both complement-parity branches;
- the literal squarefree, selector, profile, hard-value, endpoint, and
  zero-extension fields through the two endpoint coefficients; and
- one real part outside the complete incidence sum.

No literal field is silently removed.  The arbitrary-support, dechirped,
constant-anchor, short-progression, and filter-erased examples remain
explicitly quarantined as mechanism controls rather than lower bounds.

The proposed local estimate (176.C29) is correctly identified as unproved.
If it held uniformly, the normalized Fourier \(\ell^1\) cost and

\[
 \sum_{\kappa\ll L}
 \kappa\,\#\{(u,v):uv\ll(L/\kappa)^2\}
 \ll L^2X^\varepsilon
\]

would give the target after absorbing logarithms.  No accepted statement in
the reviewed artifacts supplies this selector-sensitive signed estimate.

Accordingly, the candidate's Section 6 promotion recommendation is
**GREEN** as written:

1. promote the exact two-orientation parametrization and cross/blind
   dictionary;
2. promote the fibre-stable original-gcd identity;
3. promote the primitive and nonminimal Fourier-anchor identities and
   norms;
4. promote the fixed-proportion strict sector (176.C14); and
5. record only the explicitly named positive-recombination route no-go.

Do not promote the full K17a target, the (L^{5/2}) diagnostic ledger, any
adversarial control as literal mass, or any impossibility statement for a
signed joint coefficient-sensitive theorem.

## 7. Dependencies

This verification used only:

- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/briefs/hyperbola_coordinate_post_repair_verification.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/candidates/formalized_cross_gcd_alternating_fibre_reduction.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/blind_statement.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/reports/blind_k17a_variable_determinant_rederivation.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/reports/joint_fibre_capacity_hostile_audit.md`; and
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/reviews/cross_gcd_capacity_seam_review.md`.

No shared state, synthesis, proof draft, validation matrix, control, source
card, or other artifact was edited.
