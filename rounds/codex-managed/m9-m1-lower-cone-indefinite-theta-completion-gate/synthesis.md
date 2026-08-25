# Round 144 synthesis: completed Appell self-return, with a sharper \(M^{3/4}\) cell deletion

Campaign: `m9-m1-lower-cone-indefinite-theta-completion-gate`  
Starting graph SHA-256: `179e40fb38e6a5e26623c2584d469b1c4c8d5ae444a70d791298852f2d511204`

## Decision

Round 144 closes under

\[
 \boxed{\mathsf{indefinite\_theta\_completion\_no\_go}}.
\]

The completed Appell route is exact, but after all correction, boundary,
mask, endpoint, and remainder owners are restored it returns the same
reciprocal height--alias scalar.  It does not prove the fixed-centre signed
estimate or produce a smaller automorphic signed owner.

The round nevertheless makes genuine arithmetic progress: the absolute
target-safe displacement window is enlarged from \(\sqrt M\) to
\(M^{3/4}\).

## Sharper displacement theorem

For

\[
 C(m)=\sum_{\substack{hr=m\\r\ {m odd}\\r>4h}}\chi_4(r),\quad
 k_m=\left\lfloor\sqrt{Nm}+\frac12\right\rfloor,\quad
 j_m=k_m^2-Nm,
\]

one has on every active dyadic block

\[
 \#\{m:0<|j_m|\leq J\}\ll_\varepsilon JX^\varepsilon
 \qquad(J\geq1).
\]

The improvement comes from retaining the gcd while averaging the accepted
pointwise congruence bound:

\[
 \sum_{1\leq |j|\leq J}\sqrt{(N,j)}
 \leq 2J\sum_{d\mid N}d^{-1/2}
 \ll_\varepsilon JN^\varepsilon.
\]

Exact radicals are separately target-safe, and the total count is
\(O_\varepsilon((J+\sqrt M+1)X^\varepsilon)\).  With the
\(m^{-3/4}\tau(m)\) weight, the nonzero window costs
\(M^{-3/4}JX^\varepsilon\).  Hence

\[
 \boxed{
 \mathfrak T_N=
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>M^{3/4}}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 +O_{\varepsilon,\rho,V}(X^\varepsilon).}
\]

The exponent \(3/4\) is maximal only for this absolute root-count and
divisor-bound method.  The remaining survivor is not estimated.

## Exact completed scalar

The pole-free completed torsion section

\[
 \mathcal H(\tau)=\frac12\widehat A_4(1/2,-3\tau;2\tau)
 =F(\tau)+\frac14+\sum_{a=0}^{3}\mathcal R_a(\tau)
\]

is a real-analytic scalar of weight one and nebentypus \(\chi_4\) on
\(\Gamma_0(4)\):

\[
 \mathcal H(\gamma\tau)=\chi_4(d)(c\tau+d)\mathcal H(\tau).
\]

This is an internally derived specialization of the audited completed
Jacobi laws.  It is not a new discovery of the Round-63 Appell identity,
not a verbatim source theorem, not a full-group scalar law, and not a
harmonic-Maass assertion.  The holomorphic part \(F\), the separate
constant \(1/4\), and all four nonholomorphic corrections must remain in
the owner ledger.

## Why the transform does not close the bound

After globally restoring the target-safe cells and applying exact
character Poisson to the smooth dyadic test, the positive stationary
principal family has the full factor

\[
 e(1/8)N^{-1/4}\frac{\chi_4(j)}h e(Nh/j),
\]

for \(0<j<\sqrt N\); the equality case belongs to the endpoint/Fresnel
ledger.  Once all owners are reassembled, this is precisely inverse to
the Round-140 \(e(-1/8)N^{1/4}\) map.  Thus the route returns the same
reciprocal scalar.

No audited theorem converts the real-analytic modular covariance into a
bound for the one completed pairing minus four correction pairings with
the literal square-root test.  The Round-142 rational hierarchy is
compatible with level four, but denominator-Abel reconstruction still
returns \(r_2/4\), not \(C\), and leaves the negative-character sector
and moving wedge.

The top cone has absolute capacity \(R^{1/2+o(1)}\), and the reciprocal
stationary family has capacity \(N^{1/4}\asymp R\).  These capacities are
not signed lower bounds.

## Remaining frontier

The first open estimate is now

\[
 \boxed{
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>M^{3/4}}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 \ll_{\varepsilon,V}X^\varepsilon.}
\]

Equivalently, after complete owner restoration,

\[
 \mathcal S_{\rm recip}^{+}
 \ll_{\varepsilon,\rho,V}RX^\varepsilon.
\]

The next viable mechanism must exploit cancellation jointly across the
surviving large-displacement cells; formal modular completion, independent
coefficient extraction, absolute mode summation, or another reciprocal
stationary transform cannot supply the missing gain.

## Full proof status

`M9-M1` remains open: the global lower-radial scalar and its independent
collar-tail cross owner are not proved, and neither direct blockwise M1
parent is closed.  `M9-M2` remains open: hard TOP, BAL, and all required
UNBAL owners are still unresolved.  Endpoint uniformity and `M9` therefore
remain open, so the conditional quarter bridge cannot be discharged.

The strongest theorem proved internally remains exponent \(1/3\).  The
separately audited strongest recorded external exponent remains

\[
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\]

Round 144 proves no global exponent improvement and does not prove the
Gauss circle conjectural exponent \(1/4\).

