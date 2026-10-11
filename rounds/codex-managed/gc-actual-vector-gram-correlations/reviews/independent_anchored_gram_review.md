# Round221 final-hash anchored-Gram application review

## 1. Result

**GREEN for the fixed-array average, complete moment transfer and actual-magnitude certificate floor. This is not an actual signed lower bound.**

Campaign: gc-actual-vector-gram-correlations, round221. Task: independent_anchored_gram_review. Date: 2026-09-28. This NONBLIND review binds actual_anchored_gram_attack.md at SHA256 1d6a21dd23a0284e98da6c1d3654b465236b492a78e58a57130d1135359fe08b.

The PSD/spacing estimate is uniform in matrix dimension, row count and every fixed array. Its phase-insensitive certificate cannot reach the target \(T^{29/25+\varepsilon}\). All complements and both inherited high-tail terms are paid. No claimant repair is required within this scope.

I authored the separate finite Gram report; this independently checks its application, not my own abstract proof.

## 2. Exact hypotheses

Use accepted204/216's actual \(\Psi,w\), \(Q=\lfloor T^{2/5}\rfloor\), \(V_0=T^{13/125}\), and \(\beta=(50\sqrt{1717}-297)/13762\). Thus \(1/8<\beta<13/100\).

On \(N<n\le2N\), \(N\le T^{3/2}\), retain
\[
 b_n=r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
       \mathbf1_{\{\operatorname{sf}(n)>Q,\ n\le T^{3/2}\}},
 \quad \lambda_{n,s}=s\sqrt n,\quad c_{n,s}=(b_n/2)e(-3s/8).
\]
For fixed \(|r_j|\le T/8\), \(J\ge1\), set \(A_{j\mu}=e(r_j\lambda_\mu)\), \(H=A^*A\), \(G=AA^*\), \(B=\|c\|^2\), \(D_R=\operatorname{diag}(e(R\lambda_\mu))\), and
\[
 S_m=(D_Rc)^*H^mD_Rc,\qquad D_m=\sum_\mu|c_\mu|^2(H^m)_{\mu\mu}.
\]
The fixed smooth majorant \(w_*(u)\ge w(u+s)\), \(|s|\le1/8\), exists with support \([1/4,9/4]\).

## 3. Independent derivation and cost checks

**Signs and averaging.** Real \(b_n\), including negative \(\Psi\), gives \(c_{n,-}=\overline{c_{n,+}}\), hence \(f_j=(AD_Rc)_j=Z_N(R+r_j)\). Moreover
\[
 H_{\mu\nu}=\sum_j e(r_j(\lambda_\nu-\lambda_\mu)).
\]
Thus the expanded sixth chain has endpoint phase \(R(\lambda_{\mu_6}-\lambda_{\mu_0})\) and internal phase \(\sum_{\ell=1}^6r_{j_\ell}(\lambda_{\mu_\ell}-\lambda_{\mu_{\ell-1}})\), as claimed.

For \(P=H^m\succeq0\), minus-sign Fourier integration gives
\[
 \int w_*(R/T)S_m\,dR
 =T\sum_{\mu,\nu}\overline c_\mu c_\nu P_{\mu\nu}
       \widehat w_*(-T(\lambda_\nu-\lambda_\mu)).
\]
Ordered signed frequencies satisfy \(|\lambda_i-\lambda_k|\gg|i-k|/\sqrt N\), including opposite signs. Therefore, for \(L>1\),
\[
 \sup_i\sum_{k\ne i}|\widehat w_*(T(\lambda_k-\lambda_i))|
 \ll_L(\sqrt N/T)^L.
\]
Use \(|P_{ik}|\le\sqrt{P_{ii}P_{kk}}\) and \(2z_iz_k\le z_i^2+z_k^2\), with \(z_i=|c_i|\sqrt{P_{ii}}\). This proves
\[
 \int w_*S_m=T[\widehat w_*(0)+O_L((\sqrt N/T)^L)]D_m
\]
without dimension or \(J\) loss. The relative error is \(O_L(T^{-L/4})\).

**Transfer and cycle.** The finite inequality \(S_1^6\le B^5S_6\), window majorization after \(x=R+r_j\), and \(\sum_j|f_j|^{12}\le S_1^6\) give
\[
 M_{12}(Z_N)\ll \mathcal C_N(A):=TB^5D_6/J.
\]
The cycle orientation is
\[
 D_6=\sum_{j_1,\ldots,j_6}G_{j_1j_2}\cdots G_{j_5j_6}
             K_2(r_{j_6}-r_{j_1}),\quad
 K_2(u)=\tfrac12\sum_n b_n^2\cos(2\pi u\sqrt n).
\]
Its total is nonnegative; individual terms need not be. No unweighted theorem is applied to the actual \(r_2^2\)-weighted final edge.

**Uniform certificate floor.** Choose dyadic \(N\asymp T^{4\beta}\). Then \(\Psi\ge1/2\) on the block. Elementary disk counting gives \(\sum_{N<n\le2N}r_2(n)\asymp N\); accepted216 bounds the removed whole-class absolute mass by \(O(Q^{1/4})=O(T^{1/10})=o(N^{1/4})\). Consequently the actual masked \(b_n\ge0\) satisfy \(M_N=\sum b_n\asymp N^{1/4}\).

The conjugate-paired rephasing \(c'_{n,+}=(b_n/2)e(-T\sqrt n)\) produces the real wave
\[
 F'(R)=\sum b_n\cos(2\pi(R-T)\sqrt n).
\]
On \(|R-T|\le c_0N^{-1/2}\), \(c_0\le1/(6\sqrt2)\), every cosine is at least \(1/2\) and \(w=1\). Thus
\[
 M_{12}(F')\gg N^{5/2},\qquad \|F'\|_\infty\le M_N\ll T^\beta.
\]
Its magnitudes, mask, \(B,D_6\) are unchanged. The same uniform transfer for each same array proves \(\mathcal C_N(A)\gg N^{5/2}\asymp T^{10\beta}\). This does not lower-bound the original waveform.

**Restoration.** With \(\Lambda=\|G\|\), \(D_6\le JB\Lambda^5\). For \(J=1\), exactly \(D_6=Bd_N^5\), \(d_N=2\#(N,2N]\). The actual energy estimate gives the complete block price
\[
 M_{12}(Z_N)\ll T^{1+\varepsilon}N^2(1+N/T)^{-M}.
\]
Dyadic summation costs \(T^{3+\varepsilon}\). The fixed-power inequality pays mixed blocks logarithmically; zero extensions handle partial endpoints, and the uniform \(O_A(T^{-A})\) Schwartz tail pays every remaining mixed term.

On a high shell \(v<|f_j|\le2v\), the chain gives only \(Jv^2\le4^{1/5}B\Lambda\). Since \(G(u)=K_N(u)+K_N(-u)\), accepted204 recovers the old distribution with the diagonal and full \(1+T/h\) cover. A valid same-block ceiling gives effective level \(v(v/W)^{1/5}\le v\).

The stronger accepted masked distribution, with \(W\ll T^{\beta+\varepsilon}\), pays the high tail by
\[
 T^\varepsilon[W^{10}+TW^{20/13}+V_0^{10}+TV_0^{20/13}].
\]
The low complement costs \(T+T^{26/25}+T^{29/25}\). Both high exponents, \(10\beta\) and \(1+20\beta/13\), exceed \(29/25\); their difference is \(110\beta/13-1>0\). Finally, the accepted head \(T^{15/13+\varepsilon}\) and repeated-class error \(T^{8\beta-1/5+\varepsilon}\) preserve the inherited complete bound \(T^{10\beta+\varepsilon}\) for both moments and \(|I_{12}|\). The last implication uses the error, not signed positivity.

## 4. First unproved step

The actual target still needs a complete estimate retaining the prescribed endpoint phases through the nonlinear closure. Improving the same phase-insensitive certificate cannot cross its proved floor. An array selected once from actual data is allowed; an array reselected as \(r_j(R)\) invalidates the fixed-\(H\) Fourier expansion and requires a separate estimate.

## 5. Required controls and outcome

All controls pass analytically: original cosine conjugacy; both signed branches; Fourier and cycle signs; actual arithmetic mask; real rephased peak; uniformity under data-selected fixed arrays; singular matrices; repeated offsets; zero coefficients; and singleton arrays. When \(D_m=0\), PSD makes every weighted contribution zero.

Localization retains the trivial measure cap for microscopic regimes and one window when \(h\) exceeds the window. No full-wave ceiling is silently transferred to a block. Complete low/high levels, unequal blocks, tails, head and repeated classes are retained. Zero experiments were performed.

## 6. Exact artifacts and provenance

Only these five files were read for this review; hashes were independently checked.

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| proofs/kernels/gc_complete_distinct_radical_moment_reduction.md | d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee |
| rounds/codex-managed/gc-actual-vector-gram-correlations/reports/blind_anchored_gram.md | c79eb543c4dd1229e8e6b9c6550f9b6df0fb10bed0ed76f386bf08c79d7d2ebd |
| rounds/codex-managed/gc-actual-vector-gram-correlations/reports/actual_anchored_gram_attack.md | 1d6a21dd23a0284e98da6c1d3654b465236b492a78e58a57130d1135359fe08b |

Accepted204/216 status is conductor-supplied; no graph was read. This reused agent retains rounds217--220, its own round221 finite derivation and the completed chain-ceiling review. It is not history-free. No other current artifact, source, sibling attack or shared state was inspected or edited. Only this assigned review was written; no web, new agent or successor work occurred.

## 7. Recommended state effect

**GREEN:** retain the uniform average and narrow certificate obstruction. Reject this averaged fixed-array closure at \(29/25\); retain the actual signed target and full quarter goal as open. Record no actual signed lower bound or improved exponent. No direct state mutation is recommended. Stop after this report and hash.
