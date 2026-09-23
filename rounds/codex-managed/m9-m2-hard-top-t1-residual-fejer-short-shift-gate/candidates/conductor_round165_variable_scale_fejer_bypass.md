# Conductor candidate: variable-scale Fejer bypass of the shortest shifts

## 1. Result

The Round-164 sliding-window identity is valid for every integer window
length, not only the minimal diagonal-safe choice \(R=\lceil L\rceil\).
At the opposite choice \(R=M_L\asymp L^2\), the entire range
\(1\le r<\lceil L\rceil\) may be bounded by Cauchy and paid inside the
target square.  Thus the unresolved short-shift estimate

\[
 \Re\mathfrak C_{\lceil L\rceil,J,L}^{\rm rem}
 \ll L^2X^\varepsilon
\]

is sufficient but is not forced by the Fejer method.  A distinct sufficient
frontier is the one-sided aggregate medium/long-shift theorem

\[
 \Re\sum_{\lceil L\rceil\le r<M_L}
 \left(1-{r\over M_L}\right)
 \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right)
 \ll_\varepsilon L^3X^\varepsilon.
\tag{165.V1}
\]

This does not prove the residual scalar.  It proves that failure to reach
the minimal-scale short-shift theorem is not, by itself, a terminal
obstruction to the Fejer route.

## 2. Exact statement and hypotheses

Let a consecutive integer interval of cardinality \(M_L\asymp L^2\)
contain the exact literal \(N\)-shell, and extend
\(c_N^{\rm rem}\) by zero to every integer.  On the positive literal
shell put \(z_N=c_N^{\rm rem}e(J\sqrt N)\), and put \(z_N=0\) at every
other integer.  Also put

\[
 D_L=\sum_N|c_N^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\tag{165.V2}
\]

For every positive integer \(R\), define

\[
 \mathfrak E_R={1\over R}\sum_{s\in\mathbb Z}
 \left|\sum_{j=0}^{R-1}z_{s+j}\right|^2
 =D_L+2\Re\mathfrak C_R,
\tag{165.V3}
\]

where

\[
 \mathfrak C_R=
 \sum_{1\le r<R}\left(1-{r\over R}\right)
 \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right).
\tag{165.V4}
\]

Then

\[
 |\mathcal S_{L,1}^{\rm rem}|^2
 \le {M_L+R-1\over R}\mathfrak E_R.
\tag{165.V5}
\]

For \(\lceil L\rceil\le R\le M_L\), the sufficient one-sided scale is

\[
 \Re\mathfrak C_R
 \ll_\varepsilon {L^3R\over M_L+R}X^\varepsilon
 \asymp LRX^\varepsilon.
\tag{165.V6}
\]

At \(R=M_L\), split \(\mathfrak C_{M_L}\) at
\(R_0=\lceil L\rceil\).  The short part is automatically
\(O_\varepsilon(L^3X^\varepsilon)\), so (165.V1) implies the residual
scalar target.

## 3. Proof or derivation

Expanding the full-line sliding-window square, a pair at positive gap
\(r<R\) occurs in exactly \(R-r\) windows.  This proves (165.V3)--
(165.V4) for every \(R\).  Every coefficient occurs in exactly \(R\)
windows and at most \(M_L+R-1\) windows meet the zero-extended shell.
Cauchy's inequality gives (165.V5) with no endpoint error.

The desired scalar square is \(O_\varepsilon(L^3X^\varepsilon)\).
Combining this with (165.V5) shows that it is sufficient to have

\[
 \mathfrak E_R
 \ll_\varepsilon {L^3R\over M_L+R}X^\varepsilon.
\]

For \(R\ge\lceil L\rceil\), the diagonal (165.V2) fits this budget,
and (165.V6) is sufficient.

Now take \(R=M_L\).  For each fixed shift, zero extension and Cauchy give

\[
 \left|\sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right)\right|
 \le D_L.
\tag{165.V7}
\]

Consequently,

\[
 \sum_{1\le r<R_0}\left(1-{r\over M_L}\right)
 \left|\sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right)\right|
 \le R_0D_L
 \ll_\varepsilon L^3X^\varepsilon.
\tag{165.V8}
\]

The diagonal, (165.V8), and (165.V1) give
\(\mathfrak E_{M_L}\ll_\varepsilon L^3X^\varepsilon\).  Since
\((2M_L-1)/M_L<2\), (165.V5) gives
\(|\mathcal S_{L,1}^{\rm rem}|\ll_\varepsilon
L^{3/2}X^\varepsilon\), after the customary harmless relabelling of
\(\varepsilon\).

## 4. First doubtful or unproved step

Equation (165.V1) is open.  No cancellation for the medium/long aggregate
has been established.  Its literal opening still contains both residual
selectors, squarefree masks, parity branches, hard profiles, endpoints,
and

\[
 d'm'-dm=r,\qquad \lceil L\rceil\le r<M_L.
\]

The point is a change in the sufficient interface, not an estimate for
that interface.

## 5. Required controls and outcomes

- **Endpoint count:** the available containing-interval start range has
  exactly \(M_L+R-1\) sites, and the number of nonzero windows is at most
  this.  Pass.
- **Fejer weights:** exactly \(1-r/R\).  Pass.
- **Diagonal budget:** \(D_L\ll L^2X^\varepsilon\), and the general
  budget first becomes diagonal-safe at \(R\asymp L\).  Pass.
- **Short-shift payment at \(R=M_L\):** (165.V7)--(165.V8) cost exactly
  \(L^3X^\varepsilon\), which is permitted at this scale.  Pass.
- **Phase and actual coefficient:** neither is discarded in the open
  long-shift aggregate.  Pass.
- **Phase-aligned arbitrary array:** on a filled interval, or on a
  permitted support of cardinality \(Q_L\asymp M_L\), its energy is
  \(\asymp RM_L\), while the allowed scale is \(\asymp LR\); it still
  fails by a factor \(M_L/L\asymp L\).  For a general support the exact
  lower bound is \(RQ_L^2/(M_L+R-1)\).  Thus the new frontier remains
  actual-direction.  Pass.
- **Scope:** (165.V1) would close only the residual \(t=1\) scalar via
  (165.V5).  No other channel or downstream claim follows.  Pass.

## 6. Dependencies and exact artifacts used

- `proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/reports/complete_residual_transport_attack.md`;
- `state/active_campaign.yml`.

No external theorem and no numerical experiment is used.

## 7. Recommended state effect

Promote only after independent endpoint, epsilon, and power review.  If
validated, revise the Round-164 reduction so that \(R=\lceil L\rceil\)
is labelled the minimal diagonal-safe choice, not the unique Fejer
continuation.  Retain the Round-165 short-shift theorem as open, and record
(165.V1) as a distinct alternative sufficient theorem for the Round-166
full-strategy review.  Do not change any parent, downstream theorem, or
exponent.
