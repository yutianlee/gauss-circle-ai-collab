# Round222 independent joint cross-modulus review

## 1. Result

**GREEN only for the correctly scoped finite identities and failed-certificate evidence.**

This NONBLIND review binds joint_cross_modulus_attack.md at SHA256 89ad041f378592389eec760aedfa9ac7345f4449fed8fd919448e141e8476724. The grouped-frequency argument proves \(R^2X^\varepsilon\) energy after the literal masks, hence \(R^{3/2}X^\varepsilon\) for the reciprocal sum. Neither is a lower bound or a proved minimum cost. The weighted mean survives completion. No claimant repair is required for these scoped claims.

The auxiliary smooth-block fallback is checked algebraically from the claimant's displayed smooth transformation; its separate historical source is not re-audited here.

## 2. Exact hypotheses and scope

Use \(X=N_0+\xi\), \(R=X/D\), \(K=XL/D^2\), \(\Delta=R/K=D/L\). The flat inverse-selector interface has odd \(g,n\), \(gn\asymp R\), \(g\ll K\), literal support \(gj\asymp K\), \((j,n)=1\), and
\[
 w_i=\chi_4(g)\chi_4(n)W(X/(gnD)),\qquad
 b_i(j)=\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n),\quad i=(g,n).
\]
Accepted160 and historical143 supply this flat interface, zero extension and the safe Ramanujan column. In the strict region, \(\delta<1/2\), \(a=\delta-\ell\in(1/4,1/2)\), so \(K/R\to0\).

Let \(F_i(h)=\widehat\gamma_i(h)S(N_0,h;n)\), \(U_i=\sum_jb_i(j)e(N_0j/n)\), and \(\mathcal R=\sum_iw_iU_i\). No primitive-first-argument assumption is made.

## 3. Independent derivation of key estimates

**Fourier coefficients and mean.** Opening both factors gives
\[
 F_i(h)=\sum_{t\bmod n}c_i(t)e(ht/n),\qquad
 c_i(t)=\frac1n\sum_jb_i(j)\mathbf1_{(t+\bar j,n)=1}
                   e(N_0\overline{t+\bar j}/n).
 \tag{1}
\]
Signs and normalization agree. The support has \(O(K/g)\) entries of size \(O(X^\varepsilon/K)\), so
\[
 B_i=\sum_j|b_i(j)|\ll X^\varepsilon/g,\qquad
 |c_i(t)|\le B_i/n,\qquad c_i(0)=U_i/n.
\]
For \(d=(n,m)\), \(P=[n,m]\), frequency equality modulo one gives exactly
\[
 \frac1P\sum_{h\bmod P}F_i(h)\overline{F_{i'}(h)}
 =\sum_{v\bmod d}c_i(nv/d)\overline{c_{i'}(mv/d)}.
 \tag{2}
\]
All shared rational frequencies remain. For coprime moduli, the unnormalized result is \(U_i\overline{U_{i'}}\). Deleting \(h=0\bmod n\) subtracts \(F_i(0)/n\) from every Fourier coefficient, leaving mean \((U_i-F_i(0))/n\), not forced to vanish.

For a common period, the mean of \(\sum_iw_i nF_i(h)\) is \(\mathcal R\). Parseval therefore retains \(|\mathcal R|^2\) itself. This does not estimate the unknown weighted mean.

**Short-window energy.** Choose integer \(H\asymp R\) exceeding all supported \(n\), and \(m_i(h)=\mathbf1_{1\le h<n}\). Then
\[
 \mathcal R^\circ=\sum_{h=1}^H\sum_iw_i m_i(h)F_i(h),
 \qquad |\mathcal R^\circ|^2\le H\mathcal E.
\]
Expanding \(\mathcal E\) gives exactly the kernel
\(D_{\min(n,m)-1}(t/n-s/m)\), not a complete-period delta. Both characters and every \(g,n\) row remain together.

Distinct reduced frequencies of denominator at most \(CR\) have circular separation at least \(cR^{-2}\). Geometric sums and circular ordering bound each absolute Gram row sum by
\[
 H+CR^2\sum_{v\le CR^2}v^{-1}\ll H+R^2\log(2R).
\]
The inequality \(2|z_\theta z_{\theta'}|\le|z_\theta|^2+|z_{\theta'}|^2\) proves the stated frequency bound without importing a large sieve.

For arbitrary \(|r_i|\le1\), group all equal frequencies, including \(0/1\):
\[
 C_{p/q}(r)=\sum_{\substack{i=(g,n)\\q\mid n}}w_i r_i c_i(np/q).
\]
Only now take a coefficient triangle:
\[
 |C_{p/q}(r)|\ll X^\varepsilon
 \sum_{g\ll K}\frac1g\sum_{\substack{n\asymp R/g\\q\mid n}}\frac1n
 \ll\frac{X^\varepsilon(1+\log(2K))}{q}.
 \tag{3}
\]
The inner sum equals \(q^{-1}\sum_{k\asymp R/(gq)}k^{-1}=O(q^{-1})\), including a terminal singleton. Consequently
\[
 \sum_\theta|C_\theta(r)|^2
 \ll X^\varepsilon(1+\log(2K))^2(1+\log(2R)).
 \tag{4}
\]
This uses \(\sum_{q\le CR}\varphi(q)/q^2\ll1+\log(2R)\). Repeated moduli, gcd strata and shared denominators are counted.

**One common mask envelope.** Put \(M_0=2H+1\) and
\[
 a_i(r)=M_0^{-1}\sum_{v=1}^{n-1}e(-rv/M_0),\qquad
 m_i(h)=\sum_{r\bmod M_0}a_i(r)e(rh/M_0).
\]
Uniformly in the cutoff, one may take
\[
 |a_i(0)|\le\lambda_0=1,\quad
 |a_i(r)|\le\lambda_r=\frac1{2\min(r,M_0-r)}\ (r\ne0),\quad
 \sum_r\lambda_r\ll1+\log(2H).
 \tag{5}
\]
Writing \(a_i(r)=\lambda_r r_i(r)\) gives the precise bounded row factors allowed in (3). Apply (3)--(4) separately for each \(r\), then triangle in column \(\ell^2\). The common column phase is unitary; denominators do not inflate. If unit-modulus row factors are desired, each disk-valued factor is the average of two unit phases, with unchanged total envelope.

Thus the Gram logarithm, (4), and squared mask cost prove
\[
 \mathcal E\ll X^\varepsilon R^2
 (1+\log(2K))^2(1+\log(2R))^4,
 \qquad |\mathcal R^\circ|\ll R^{3/2}X^\varepsilon.
 \tag{6}
\]
No hidden power of \(K\) is required for completion.

**Restoration and scope.** At actual \(N_0\asymp X\),
\[
 |F_i(0)|\le(B_i/n)|c_n^{\rm Ram}(N_0)|.
\]
Using \(|c_n^{\rm Ram}(N_0)|\le(n,N_0)\) and
\(\sum_{n\asymp C}(n,N_0)\ll CX^\varepsilon\), the fixed-\(g\) contribution is \(O(X^\varepsilon/g)\). Summing \(g\) restores the safe \(O(X^\varepsilon)\) column once. This safety estimate is not asserted for the artificial choice \(N_0=0\).

The flat physical exponent is \(3(1-\delta)/2\), exceeding the quarter exponent by \(5/4-3\delta/2>1/2\). Its normalized price is
\((LK)^{3/4}X^{-1/4}R^{3/2}X^\varepsilon\). The better inherited flat envelope and its missing-power branches remain unchanged.

Separately, the displayed original smooth sum gives \(O(D)\). Its displayed smooth transformation and \(|a_{L,K}|\ll1\) give \(O(\sqrt{XL/D})+O_W(1)\). Since \(L\ll DX^{-1/4}\), the latter is \(O(X^{3/8+\varepsilon})\), including finite sign/shift channels and logarithmic dyadic summation. This algebra is conditional on that smooth identity; it does not follow from the flat representation. The claimant explicitly excludes hard top and separately owned nonflat, transition, endpoint, BAL and M1 corrections.

## 4. First unproved step

The sufficient certificate \(\mathcal E_{\rm actual}\ll X^{1/2+\varepsilon}/R\) would give the quarter bound for this flat scalar by Cauchy. It is neither proved nor claimed necessary or equivalent to complete UNBAL. Equations (3)--(6) discard arithmetic cancellation and supply only a larger upper price, not actual signed saturation.

Even a future proof must separately close full-owner transformations and endpoint companions. No such transfer is authorized by143/160.

## 5. Controls and outcomes

All checks pass: arbitrary first-argument gcd, inverse representatives, real centre, both characters, all \(g,n\) rows, zero and shared nonprimitive frequencies, repeated moduli, empty prefixes and literal moving-support weights. Large \(h\) is retained. The masks have one common summable envelope; the safe column is restored once.

The common-period mean is not substituted for the physical short window. The \(R^2\) and \(R^{3/2}\) powers are upper prices only. Zero experiments or external-source lookups were performed.

## 6. Exact artifacts and provenance

Campaign: m9-m2-complete-unbalanced-vector, round222. Task: independent_cross_modulus_review. Date: 2026-09-28. Only these files were read for this assignment; hashes were checked:

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| rounds/codex-managed/m9-m2-complete-unbalanced-vector/reports/joint_cross_modulus_attack.md | 89ad041f378592389eec760aedfa9ac7345f4449fed8fd919448e141e8476724 |
| proofs/kernels/m9_m2_unbalanced_inverse_selector_reciprocity_projective_obstruction.md | 584745fb9af72993a4b33eb95dad3421e8924ae5fb64c5b314511b08d4254baf |
| rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/level_four_kloosterman_embedding_attack.md | dea1172e467c6871652eefdc3f55dcc20b1288ea0cb25720b9ede222e4458b82 |

Accepted status is conductor-supplied. No graph, current interface, sibling or source card was reopened. The claimant records graph a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b; this is metadata. The separate frequency-phase transformation source is outside this read scope.

This reused agent retains rounds217--221, its round222 finite report and completed weighted-period review. This audit is NONBLIND, not history-free or independent validation of those authored artifacts. Only this assigned review was written; no claimant, shared-state, historical, sibling or successor edit occurred.

## 7. Recommended state effect

**GREEN for retaining the finite identities and fully priced failed certificate.** No new bound, actual lower bound, universal vector-method obstruction, complete UNBAL closure or quarter-goal progress follows. Keep strict-flat and complete smooth/endpoint scopes separate. No direct state mutation is recommended. Stop after this report and hash.

