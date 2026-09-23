# Conductor Round 192 report reconciliation

## Decision

The three independent reports agree on one promotable strict reduction and
one nonpromotable core. Promote, subject to formalization and seam review, the
exact Farey-covector safe union inside the Round-191 rho-large remainder.
Retain the exact central core as open. Do not promote a complete rho-large,
original-\(t=1\), owner, bridge, theorem, or exponent claim.

The provisional terminal label is
strict_rho_large_farey_covector_sector.

## Reconciled exact lemma

Retain the exact Round-191 remainder with

\[
 U=mq>4Q,\qquad Qm<Y,\qquad
 T=\min\!\left\{\frac{U-1}{2},
   \left\lfloor\frac{QmU}{Y}\right\rfloor\right\},
 \qquad |\rho_U(v)|>T.
\]

For \(v_0=[v]_U\), define the canonical quotient by

\[
 \rho v_0-\beta U=1.
\]

This \(\beta\) is not the literal transport quotient: if
\(v=v_0+nU\), then \(\gamma=\beta+n\rho\). For

\[
 A=\min\{U-1,\lfloor Q^{C_0}\rfloor\},\qquad
 \mathcal F_A=
 \{(c,d):1\le c\le A,\ 0\le d\le c,\ (c,d)=1\},
\]

put \(\ell_{c,d}=c\beta-d\rho\). The common exact identity is

\[
 \rho(cv_0-dU)=c+U\ell_{c,d}\ne0.
\]

For fixed \((c,d,\ell)\), a row injects into a signed divisor
\(\rho\mid c+U\ell\), so there are at most
\(2\tau(|c+U\ell|)\) canonical residue classes.

When \(T\ge1\), define

\[
 \mathcal E_A=
 \{v:\exists(c,d)\in\mathcal F_A,\,
             |c\beta-d\rho|\le T\};
\]

when \(T=0\), define \(\mathcal E_A=\varnothing\). If \(P_A\) is the
single row-union projector on the exact Round-191 remainder, then

\[
 |P_A\mathscr R_{\rm fix}|
 \ll_{B,C_0,\varepsilon}Qm\kappa uX^\varepsilon,
\]

and its exact outer contribution is
\(O_{B,C_0,\varepsilon}(L^2X^\varepsilon)\). The proof uses
\(|\mathcal F_A|\ll A^2\), \(O(TX^\eta)\) residue classes per covector,
\(O(u/U)\) literal repetitions, \(Y\) heights, \(O(\kappa)\) sites, the
exact \(m^{-1}c_q(a)\) lift, and the accepted coefficient, band, divisor,
and shell ledger. No positive power of \(Y\) is absorbed.

The new safe aggregate is the old Round-191 safe aggregate plus
\(P_A\mathscr R\). Hence terminal and Fejer pieces are replaced, not counted
twice. The exact new core is \((I-P_A)\mathscr R\), before the single outer
real part and with every literal field retained.

## Stronger independent coverage theorem

All three reports independently recover the stronger circular-pigeonhole
bound. If \(r=|\rho|\) and \(b=|\beta|\), then

\[
 \min_{(c,d)\in\mathcal F_A}|cb-dr|
 \le \left\lfloor\frac r{A+1}\right\rfloor.
\]

Therefore a \(T\ge1\) core row must satisfy

\[
 r\ge(A+1)(T+1).
\]

The core is guaranteed empty when

\[
 \left\lfloor
 \frac{(U-1)/2}{A+1}
 \right\rfloor\le T,
\]

equivalently

\[
 U\le2(A+1)(T+1)-1.
\]

The zero-covector corollary \(r\le A\) is included. The criterion is never
applied at \(T=0\), because the safe sector is then empty by definition.
The direct inverse-class count already covers \(r\ll AT\) at polylogarithmic
cost; the full Farey union additionally captures scattered large-\(r\) rows.

## Hostile phase, carry, and endpoint audit

For \(v=v_0+nU\), set \(d_v=cn+d\) and
\(\Delta=cv-d_vU=cv_0-dU\). The hostile report derives

\[
 \rho\Delta=c+U\ell,\qquad
 \gamma\Delta=d_v+v\ell,
\]

\[
 z_{\omega,v}^{\Delta}=e(\epsilon_\omega ac/q),
\]

and cumulative carry

\[
 N_\omega(h;\Delta)
 =\theta_{\omega,c}(h)-\epsilon_\omega\ell.
\]

These identities are exact but yield no magnitude gain. The long-step Abel
identity returns to the original row sum. The two endpoint arguments undergo
unequal translations involving the representative-dependent \(d_v\), so
arithmetic masks, literal cells, phases, births, and deaths are not invariant.
The core condition controls neither carry parity nor distance of the retained
phase from one.

Positive covering of a central residue set requires about
\(U/T\asymp Y/(Qm)\) target-sized slices, up to divisor slack, restoring the
original deficit. Bounded zero-extended arrays retain full normalized-Abel
capacity after any static Farey selector. These are method controls only, not
literal lower mass.

## Report discrepancies and repairs

There is no mathematical disagreement.

- The statement-only report retains an explicit divisor maximum until a
  polynomial-size connector is supplied. The selected full context supplies
  \(U\le u\ll L\ll X^{1/4}\), so the elementary divisor bound contributes
  only fresh \(X^\eta\).
- The empty-core condition is recorded only with the standing hypothesis
  \(T\ge1\). It is false as a conclusion from the displayed floor alone when
  \(T=0\), because that sector was deliberately defined empty.
- The strategy's original small-\(U\) observation is superseded by the
  stronger exact circular-pigeonhole criterion.
- Report TeX/control-byte defects were repaired by the assigned authors
  before reconciliation.

## Exact evidence

- discovery report SHA-256:
  c853502a8ae8721b17c3c862a4d9b8865a80e7b2697e15950cd748b05227e2a8;
- hostile report SHA-256:
  9051b23d31cea5eff00a1aece7ef66f26d007c1c750d5ada2e2641808f771008;
- statement-only report SHA-256:
  186081c5acb3896598b36f9edc18e683df1b5f5162261a46dfb4da6ffc00a461.

The WolframScript control checks signs, factorization, divisor fibres, finite
union bounds, circular-pigeonhole coverage, and small-modulus zero covectors.
It reports zero failures and remains diagnostic only.

## First unproved step

The exact remaining core estimate is

\[
 \Re\mathscr R_{\rm core,Y,Q}^{\sigma}
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon,
\]

or the stronger fixed-packet estimate

\[
 |\mathscr R_{\rm core,fix}|
 \ll_{C_0,\varepsilon}Qm\kappa uX^\varepsilon.
\]

No current report proves it. The first missing literal input is a jointly
signed correlation theorem for the unequal endpoint translations, masks,
carry, actual square-root phases, and affine births/deaths. Positive control
still has the exact deficit \(Y/(Qm)\).

## State recommendation

Formalize one new subordinate proved-internal Farey-covector reduction with
the exact safe union, outer ledger, core, coverage theorem, and scoped method
boundary. Add it only as a dependency and inconclusive evidence of the
still-open hard-M1 small-\(t\) owner. Reject the identified overclaims. Keep
M9-M1, M9-M2, endpoint uniformity, M9, both bridges, the target, and every
exponent unchanged.
