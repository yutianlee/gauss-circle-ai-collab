# Round 58 conductor adjudication: the endpoint residual closes, the signed divisor core does not

## 1. Decision

Promote the exact high-shell floor representation, its endpoint zero-mode
ledger, and the target-safe sampled Fejer residual.  Also promote the scoped
fact that Fourierizing the moving hyperbola selector and then taking
absolute values or applying derivative tests branch by branch cannot supply
the missing square root.  Do not promote the signed high-shell estimate.

The apparent discrepancy between the two residual estimates in the reports
is not a contradiction.  The hostile audit proves the crude pointwise bound

\[
 R^\varepsilon+R^3/(T+1)^2,
\]

whereas the discovery report groups near-integer samples arithmetically and
proves the sharper

\[
 X^\varepsilon(R/T+1).
\]

The latter estimate has now been independently routed through the blind and
hostile seams.

## 2. Exact complete-row identity

Let \(Y=R^2\asymp\sqrt X\), let
\(J=[A,B]\cap\mathbb Z\subset[cY,CY]\) have
\(\ell=B-A+1\le R\), and put

\[
 L_h={A+h-1\over2h},\qquad U_h={B+h\over2h},\qquad
 q_h=2\lfloor L_h\rfloor+1,
\]

\[
 \nu_h=\lfloor U_h\rfloor-\lfloor L_h\rfloor\in\{0,1,2\}.
\]

For \(R/4<h\le R/2\), with the exact actual amplitude and every inherited
angular or radial star retained,

\[
 P_J=\sum_h(-1)^{\lfloor L_h\rfloor}
 \left\{I_1(\nu_h)F_h(q_h)-I_2(\nu_h)F_h(q_h+2)\right\},
\tag{58.1}
\]

where

\[
 I_1(v)={v(3-v)\over2},\qquad I_2(v)={v(v-1)\over2},
 \qquad F_h(q)=\widetilde{\mathcal A}_X(h,q)e(\sqrt{Xhq}).
\]

This formula gives exactly the empty, singleton, and adjacent-pair cases.
Artificial window endpoints are full owners.  In particular, when
\(A=B=N\), it returns precisely the divisor incidences
\(h\mid N\), \(N/h\) odd, with no manufactured partner or artificial half
weight.

## 3. Zero modes and sampled Fejer residual

With \(\psi_F(t)=t-\lfloor t\rfloor-1/2\), including
\(\psi_F(n)=-1/2\),

\[
 \nu_h={\ell\over2h}+\psi_F(L_h)-\psi_F(U_h),
\]

while the parity square wave is the difference of two half-scale sawtooths.
The character has zero mean, equivalently

\[
 \chi_4(q)={e(q/4)-e(3q/4)\over2i},
\]

but the geometric count mode \(\ell/(2h)\) remains and may not be dropped.
Finite Abel summation confirms that the constant mode in a character partial
sum cancels only after both boundary values and all differences are kept.

For every endpoint argument

\[
 t_h={N+ch\over dh},\qquad N\asymp R^2,quad d\in\{2,4\},
\]

the Vaaler residual kernel satisfies

\[
 \kappa_T(t)\ll\min\{1,T^{-2}\|t\|^{-2}\}.
\]

If \(\|t_h\|\le\delta\), choose an integer \(k\) and set
\(s=N-(dk-c)h\).  Then \(|s|\ll\delta R\) and
\(h\mid N-s\).  Summing the divisor bound over these integer errors gives

\[
 \#\{h:R/4<h\le R/2,\ \|t_h\|\le\delta\}
 \ll_\varepsilon X^\varepsilon(\delta R+1).
\tag{58.2}
\]

Dyadic shells at distance \(2^j/T\) therefore give

\[
 \sum_h\kappa_T(t_h)
 \ll_\varepsilon X^\varepsilon(R/T+1).
\tag{58.3}
\]

Exact integer samples are the \(s=0\) divisor incidences and are included in
the \(+1\) term.  The exact remainder is a bounded polynomial difference in
four such residuals, so multiplication by the bounded actual symbol
preserves (58.3).  Thus \(T=\lceil\sqrt R\rceil\) makes the complete endpoint
and integer-jump residual \(O_\varepsilon(X^\varepsilon\sqrt R)\).

## 4. What remains after Fourierization

The finite main retains the discontinuous integer

\[
 q_h=2\left\lfloor{A+h-1\over2h}\right\rfloor+1
\]

inside both the actual amplitude and the radial phase.  A fixed-\(q_h\)
branch has only \(O(1)\) values of \(h\), and an actual fixed-\(q\) fibre is
a singleton.  Reindexing by \(n=hq\) gives the exact survivor

\[
 P_J=\sum_{n=A}^{B}e(\sqrt{Xn})
 \sum_{\substack{h\mid n,\ R/4<h\le R/2\\n/h\ {m odd}}}
 \chi_4(n/h)\widetilde{\mathcal A}_X(h,n/h).
\tag{58.4}
\]

Consequently branchwise derivative estimates and termwise Fourier absolute
values retain \(O(X^\varepsilon R)\) capacity.  The strict fourth-power
family already accepted in Round 57 realizes order-\(R\) unmatched
star-free mass, whereas the target is \(O(X^\varepsilon\sqrt R)\).  This is
not a signed lower bound for (58.4).

## 5. Source and hostile controls

The hostile source audit correctly rules out the currently cited black-box
shortcuts.  Vaaler supplies the approximation and its positive residual,
not the signed moving-symbol estimate.  The directly mapped
Robert--Sargos theorem leaves a full-box term of the wrong size, while the
Duke--Friedlander--Iwaniec Kloosterman-fraction theorem requires modular
inverses, coprimality, and smooth weights absent here.  Exact fourth-power
incidences also rule out a universal reciprocal-frequency spacing premise.

The hostile residual \(R^3/T^2\) remains a valid but weaker estimate; it is
superseded for this sampled family by (58.2)--(58.3).

## 6. Controls and evidence

- Exact floor and full endpoint ownership: discovery and blind reports.
- Residual-free finite DFT and exact unmatched zero mode: blind report.
- Sharp divisor-count Fejer residual: discovery report plus the requested
  independent blind and hostile addenda.
- Source applicability and exact reciprocal collision: hostile report.
- Actual-profile absolute-capacity witness: accepted Round 57 synthesis and
  the discovery report's transfer check.
- All work in this round is analytical/algebraic; no numerical evidence is
  used.

## 7. State recommendation

Create one proved reduction/obstruction node containing (58.1)--(58.4).
Record the endpoint residual as closed at height \(T=\sqrt R\), while the
signed short actual-symbol twisted-divisor estimate remains open.  Reject
count-only replacement of the weighted row, deletion of either zero-mode
ledger, modewise absolute closure, branchwise derivative closure, and the
claim that any audited source proves the shell.  Leave the lower shell,
alpha transfer, M9-M1, M9, and the exponent unchanged.
