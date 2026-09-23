# Conductor Round 192 adjudication

- Campaign: m9-m1-t1-rho-large-bezout-edge-gate
- Round: 192
- Starting graph SHA-256:
  75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13
- Durable kernel SHA-256:
  301e51dc49072ed8541fc1183f00a8cddc3768fba025e33289314004f8c38325
- Closing label: strict_rho_large_farey_covector_sector
- Numerical theorem evidence: none

## 1. Result and conductor decision

Round 192 closes with one proved subordinate reduction and no estimate for
the complete rho-large core.

Retain the exact Round-191 fast hard-M1 \(t=1\) remainder. Write \(U=mq\),
let \(v_0=[v]_U\), and define

\[
 \rho v_0-\beta U=1,\qquad
 T=\min\!\left\{\frac{U-1}{2},
       \left\lfloor\frac{QmU}{Y}\right\rfloor\right\},
 \qquad |\rho|>T.
\]

For fixed \(C_0\ge2\), put

\[
 A=\min\{U-1,\lfloor Q^{C_0}\rfloor\},\qquad
 \mathcal F_A=\{(c,d):1\le c\le A,\ 0\le d\le c,\ (c,d)=1\},
\]

\[
 \ell_{c,d}=c\beta-d\rho.
\]

When \(T\ge1\), the union of rows satisfying
\(|\ell_{c,d}|\le T\) for at least one \((c,d)\in\mathcal F_A\) is
target-safe. When \(T=0\), this new union is empty. Its full outer
contribution is \(O_{B,C_0,\varepsilon}(L^2X^\varepsilon)\).

The exact complement remains open.

## 2. Exact arithmetic and safe-sector proof

For \(1\le c<U\),

\[
 \rho(cv_0-dU)=c+U(c\beta-d\rho)=c+U\ell_{c,d}\ne0.
\]

For fixed \((c,d,\ell)\), every admissible signed inverse \(\rho\) divides
\(c+U\ell\), and a signed least inverse determines at most one canonical
unit class. Hence the fibre has at most
\(2\tau(|c+U\ell|)\) classes. Summing \(|\ell|\le T\), restoring the
\(O(u/U)\) literal repetitions, \(Y\) heights, \(O(\kappa)\) sites, and the
\(O(A^2)\) fixed Farey-family cost gives

\[
 |P_A\mathscr R_{\rm fix}|
 \ll_{B,C_0,\varepsilon}Qm\kappa uX^\varepsilon.
\]

The exact \(m^{-1}c_q(a)\) lift cancels \(m\) before the positive outer
sum; the coefficient mass, projective bands, \(\tau_3(u)\) divisor ledger,
and shell sum give \(O(L^2X^\varepsilon)\). No positive power of \(Y\),
\(U\), or \(L\) is hidden in the epsilon budget.

The fixed-packet decomposition is

\[
 \mathscr J_{\rm safe,192,fix}
 =\mathscr J_{\rm safe,191,fix}+P_A\mathscr R_{\rm fix},
 \qquad
 \mathscr R_{\rm core,fix}=(I-P_A)\mathscr R_{\rm fix}.
\]

It replaces selected terminal and Fejer rows rather than counting them
twice, and the inherited linear outer assembly preserves the single final
real part.

## 3. Exact core and coverage theorem

For \(T\ge1\), every core row satisfies

\[
 |c\beta-d\rho|>T\quad((c,d)\in\mathcal F_A).
\]

With \(r=|\rho|\) and \(b=|\beta|\), circular pigeonhole and primitive
reduction give

\[
 \min_{(c,d)\in\mathcal F_A}|cb-dr|
 \le\left\lfloor\frac r{A+1}\right\rfloor.
\]

Therefore every nonempty core row has

\[
 |\rho|\ge(A+1)(T+1),
\]

and the core is guaranteed empty when

\[
 T\ge1,\qquad
 \left\lfloor\frac{(U-1)/2}{A+1}\right\rfloor\le T,
\]

equivalently \(U\le2(A+1)(T+1)-1\). This criterion is not applied at
\(T=0\), where the new safe projector was deliberately defined to be zero.

## 4. Literal identities and first open relation

If \(v=v_0+nU\), then the literal transport quotient is
\(\gamma=\beta+n\rho\), not \(\beta\). For
\(d_v=cn+d\) and \(\Delta=cv-d_vU\),

\[
 \rho\Delta=c+U\ell,\qquad
 \gamma\Delta=d_v+v\ell,\qquad
 z_{\omega,v}^{\Delta}=e(\epsilon_\omega ac/q).
\]

The cumulative carry is

\[
 N_\omega(h;\Delta)=\theta_{\omega,c}(h)-\epsilon_\omega\ell,
\]

with \(\theta_{+,c}\in\{-1,0\}\) and
\(\theta_{-,c}\in\{0,1\}\). The two endpoint number/divisor translations
are exact but unequal and retain the representative-dependent \(d_v\).
Long-step Abel summation is an exact self-return, not a saving.

The first unproved estimate is

\[
 \Re\mathscr R_{\rm core,Y,Q}^{\sigma}
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon,
\]

or its fixed-packet strengthening
\[
 |\mathscr R_{\rm core,fix}|
 \ll_{C_0,\varepsilon}Qm\kappa uX^\varepsilon.
\]

Positive control remains \(Y\kappa uX^\varepsilon\), leaving the exact
factor \(Y/(Qm)\). The missing input is a jointly signed correlation theorem
for the actual unequal endpoint translations, masks, carries, square-root
phases, and affine births and deaths before any positive norm.

## 5. Method controls and independent review

In the explicitly unsaturated prime residue-universe control, a fixed
covector covers only \(O_\eta(TX^\eta)\) classes, so a coefficient-blind
positive cover needs about \(U/T\asymp Y/(Qm)\) pieces and restores the
deficit. Arbitrary bounded zero-extended height arrays retain full
normalized-Abel capacity after a static Farey selector. These controls are
not literal lower-mass results and do not disprove the open core estimate.

The discovery, hostile, and statement-only reports agree on the exact
factorization, fibre count, safe union, coverage theorem, and open core.
The repaired candidate passed blind post-unmask, normalization/divisor/power,
and literal/owner-scope seam review. The final kernel passed:

- candidate/power post-repair review, SHA-256
  3089849e8a4e37bca1c82b63c36c838e0ddb9343524c74a9c208c84c0451878e;
- literal/core/owner-scope review, SHA-256
  a16dc5e673a9ec3023dec4b87791bf46d0f3044ddc96bcf2132e1c3c7cd40316;
- formalization/provenance/hygiene review, SHA-256
  ea24e607ee3dc97e2cc3ebd92222aa00187ee3a7326c08bd28c5be67584dce58.

The finite Wolfram diagnostic checked 158 moduli, 7,804 rows, 365,696
identities, 305,844 fibres, and all recorded finite coverage and union
controls with zero failures. It is diagnostic only.

## 6. Dependencies and downstream scope

The new subordinate node depends directly only on:

- M9-M1-hard-top-t1-fast-signed-inverse-transport-reduction;
- Divisor-bound-elementary.

The complete rho-large core and complete original \(t=1\) residual remain
open. Every original \(t\ge2\) small-\(G\) incidence, the large-\(G\)
near-resonant complement, the remaining small-\(t\) owner, hard and smooth
M1, GAR, every M2 parent, endpoint uniformity, M9, both bridges, and the
quarter target remain open or conditional at their prior scopes.

The internal exponent \(1/3\), accepted external benchmark
\(0.3144831759740614\ldots\), and target \(1/4\) are unchanged.

## 7. State decision

Create one proved-internal subordinate Farey-covector reduction. Add it only
as a dependency and inconclusive evidence item to the still-open hard-M1
small-\(t\) owner. Narrow that owner's next action to the exact strict core,
including the \(T=0\) case and the simultaneous covector inequalities.

Reject canonical/literal quotient conflation, \(c=U\), unqualified
\(T=0\) coverage, overlap double counting, free Farey-family cost, static
Farey cancellation, endpoint invariance, Abel saving, positive-cover
closure, bounded-array literal-mass claims, and any inference to complete
\(t=1\), a parent, bridge, theorem, or exponent.

Round 192 closes under exactly:
strict_rho_large_farey_covector_sector.
