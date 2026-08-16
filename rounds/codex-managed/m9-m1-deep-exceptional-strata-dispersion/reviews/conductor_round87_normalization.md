# Round 87 conductor normalization review

## Accepted row normalization

The bounded physical row is

\[
 \mathcal R_{b,x}(\theta)
 ={1\over M}\sum_n I_b(n)e_M(nx)e(n\theta),
 \qquad
 \|\mathcal R_{b,x}\|_\infty
 \ll_\varepsilon X^\varepsilon TQ^{-5/24}.
\]

For \(P=(x,y)\), \(x\ne y\), the exact ordered-pair function is

\[
 F_{b,P}(\theta)=e_M(K(\bar x-\bar y))
 \mathcal R_{b,x}(\theta)\overline{\mathcal R_{b,y}(\theta)}.
\]

There is no further \(M^{-2}\) in this definition.  Its \(d\)-th Fourier
coefficient already contains the external \(M^{-2}\) in \(Z_b(d)\).
The discovery report's first \(U\asymp B\) calculation used the normalized
row bound on an unnormalized row and was false by \(M^4\).  The corrected
report rejects that calculation.

## Correct group bound

For a full-prime-power active set \(S\), there are at most \(m_S^2\)
active ordered-pair labels and at most \(r_S\) inactive diagonal units,
where \(m_Sr_S=M\).  The sharp deep Fourier projection costs only
\(O(\log J)\) in \(L^\infty\).  Hence

\[
 \sum_\alpha |H_{b,S,\alpha}(\theta)|^2
 \ll_\varepsilon X^\varepsilon M^2T^4Q^{-5/6}.
\]

After summing \(S\), using \(\int_{\mathbb T}|D_U|^2=U\), and summing
\(b\asymp B\),

\[
 \mathcal P_{\rm exc}(D,U)
 \ll_\varepsilon X^\varepsilon UB^3T^4Q^{-5/6}.
\]

Choose the packet-allowed \(U=\lfloor D\rfloor\asymp D\).  The required
signed Fejer budget is \(\asymp(D/B)J^{14/5}\), and

\[
 B^4T^4Q^{-5/6}
 \le J^{3/5+12/5-1/3}
 =J^{8/3}=J^{14/5-2/15}.
\]

Thus the corrected package has \(J^{-2/15}\) power slack.  This is a
symmetric signed Fejer estimate, not the per-shift absolute estimate in
(87.7).

## Decision

The corrected normalization and exponent ledger pass.  The false
\(U\asymp B\) formula is rejected and must not appear in the graph.

