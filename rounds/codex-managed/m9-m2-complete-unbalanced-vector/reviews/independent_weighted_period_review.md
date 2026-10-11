# Round222 independent weighted-period application review

## 1. Result

**GREEN for the exact weighted Fourier identities, common-period correlations and scoped flat-component binding.**

This NONBLIND post-isolation review binds conductor_weighted_period_control.md at SHA256 3928e5f90f98c95403ba762c68e6f86141efba1e821c29393cbf7a45c2575e32. Deleting the \(h=0\) residue leaves constant Fourier coefficient \((U_n-z_n)/n\); it is not a mean-zero projection. This coefficient can vanish for particular data, but the deletion does not force it to vanish.

The gcd formula, coprime product and aggregate normalization are correct. No actual signed lower bound, target-saving estimate, endpoint transfer or complete UNBAL theorem follows. No claimant repair is required.

## 2. Exact hypotheses

Let \(n,m\ge2\), \(A\in\mathbb Z\), and let \(b_n(j)\) be any finite complex coefficient collection on unit residues modulo \(n\), with repeated residues first combined if necessary. Use \(e(t)=\exp(2\pi it)\) and
\[
 \gamma_n(h)=\frac1n\sum_jb_n(j)e(-h\bar j/n),\quad
 F_n(h)=\gamma_n(h)S(A,h;n),\quad
 U_n=\sum_jb_n(j)e(Aj/n).
\]
Set \(z_n=F_n(0)\), \(V_n=U_n-z_n\), and
\[
 F_n^\circ(h)=F_n(h)-z_n\mathbf1_{\{h=0\bmod n\}}.
\]
All these \(h\)-functions are periodic. Neither \((A,n)=1\) nor positivity of coefficients is assumed. The actual application retains the complete zero-extended moving support and the accepted160 flat strict-UNBAL scope.

## 3. Independent derivation and binding

**Fourier coefficients and the two different zeros.** Expand the product defining \(F_n\). Its frequency is \(t=x-\bar j\bmod n\), so
\[
 F_n(h)=\sum_{t\bmod n}c_n(t)e(ht/n),
\]
\[
 c_n(t)=\frac1n\sum_jb_n(j)
 \mathbf1_{\{(t+\bar j,n)=1\}}
 e\!\left(\frac{A\,\overline{t+\bar j}}n\right).
 \tag{1}
\]
At \(t=0\), the inverse of \(\bar j\) is \(j\); hence
\[
 c_n(0)=U_n/n,\qquad \sum_{h\bmod n}F_n(h)=U_n.
 \tag{2}
\]
On the other hand,
\[
 z_n=\sum_t c_n(t)
     =\frac{c_n^{\rm Ram}(A)}n\sum_jb_n(j),
\]
where \(c_n^{\rm Ram}\) denotes the Ramanujan sum, distinguished from the Fourier coefficient notation in (1).

Since \(\mathbf1_{\{h=0\bmod n\}}=n^{-1}\sum_t e(ht/n)\), the Fourier coefficients of \(F_n^\circ\) are exactly
\[
 d_n(t)=c_n(t)-z_n/n,\qquad d_n(0)=V_n/n.
 \tag{3}
\]
Removing one column subtracts \(z_n/n\) from every Fourier coefficient. Removing the constant mode instead would subtract the constant function \(U_n/n\) from \(F_n\), a different operation that changes the nonzero columns.

**Common period and gcd.** Put \(d=(n,m)\), \(P=\operatorname{lcm}(n,m)\). Orthogonality on \(0\le h<P\) enforces \(t/n=u/m\pmod1\). With \(0\le t<n\), \(0\le u<m\), these pairs are exactly
\[
 (t,u)=(n\ell/d,m\ell/d),\qquad 0\le\ell<d.
\]
For example, writing \(n=dn'\), \(m=dm'\) with \((n',m')=1\), the equality \(m't=n'u\) forces these indices. Therefore
\[
 \sum_{h=0}^{P-1}F_n^\circ(h)\overline{F_m^\circ(h)}
 =P\sum_{\ell=0}^{d-1}
 d_n(n\ell/d)\overline{d_m(m\ell/d)}.
 \tag{4}
\]
This includes every shared frequency, primitive or not. For coprime \(n,m\), \(P=nm\) and (3) yields exactly
\[
 \sum_{h=0}^{nm-1}F_n^\circ(h)\overline{F_m^\circ(h)}
 =V_n\overline{V_m}.
 \tag{5}
\]
Before column deletion, replace \(V\) by \(U\). There is no missing \(n,m\) or period factor. Bare Kloosterman rows use primitive frequencies \(x/n\); multiplication by \(\gamma_n\) replaces them by differences \((x-\bar j)/n\), which include zero and lower-denominator frequencies.

**Aggregate mean.** For arbitrary complex \(\alpha_n\), any finite modulus set and any common period \(P\), let \(G(h)=\sum_n\alpha_n nF_n^\circ(h)\). Then
\[
 \frac1P\sum_{h=0}^{P-1}G(h)=\sum_n\alpha_n V_n,\qquad
 \left|\sum_n\alpha_nV_n\right|^2
 \le\frac1P\sum_{h=0}^{P-1}|G(h)|^2.
 \tag{6}
\]
The factor \(n\) compensates exactly for the mean \(V_n/n\). Parseval places the squared left side itself in the right side as its constant-mode contribution. Formula (6) gives no independent estimate for that mode. It remains valid with an additional finite \(g\)-index, including repeated moduli belonging to different \(g\)-rows.

**Actual flat binding.** Set \(A=N_0=\lfloor X\rfloor\), \(\xi=X-N_0\), and substitute
\[
 b_{g,n}(j)=\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n),
 \qquad
 \alpha_{g,n}=\chi_4(g)\chi_4(n)W(X/(gnD)).
\]
Then
\[
 U_{g,n}=\sum_j
 \frac{q_L(4Xj/(gn^2))}{gj}e(Xj/n),
 \tag{7}
\]
exactly accepted160's self-return. The substitution \(r=gn,\ k=gj\), \((j,n)=1\), gives the same argument, denominator and phase in the stated reciprocal wave, and preserves both character factors. The real-centre phase is retained; no coprimality of \(N_0,n\) is needed.

Literal zero extension preserves every moving endpoint. If folding were necessary, the complete physical coefficients, including \(e(\xi j/n)\), would first be added within each residue; only the integer-\(N_0\) factor is then periodic. In the stated strict asymptotic range, \(j/n\asymp K/R=\Delta^{-1}\to0\), consistently with the supplied short-residue support.

Accepted160, (160.K19)--(160.K20), identifies the single safe Ramanujan column. Its target-safe aggregate removal is an accepted input, not reproved here. Positive \(h\) that is zero modulo another denominator is retained. No enormous common period is priced as a free physical completion. Hard top, nonflat, transition and endpoint companions are not covered by this flat algebra.

## 4. First unsupported application step

The first missing input is a signed estimate for the literal weighted, windowed joint vector. Bare-row orthogonality cannot be substituted for (4), and column deletion cannot remove the constant mode by declaration. A short-window use must retain its full weight transform. These identities neither prove the desired saving nor rule out a coefficient-sensitive theorem providing it.

## 5. Controls and outcomes

For distinct odd primes \(p,q\), choose \(A=0\), \(b_n(1)=1\). Then \(U_n=1\), \(z_n=(n-1)/n\), \(V_n=1/n\), so (5) is \(1/(pq)>0\). This is an exact alternate-vector control, not a lower bound for the actual coefficients.

Empty rows vanish. Equal moduli give Parseval, \(n\sum_t|d_n(t)|^2\), for the same row. Noncoprime moduli retain all \(d\) shared frequencies. Inverse representatives change phases only by integers. Repeated physical residues and repeated moduli introduce no uncounted multiplicity. All controls are algebraic; zero experiments and no source lookup were used.

## 6. Exact dependencies and provenance

Campaign: m9-m2-complete-unbalanced-vector, round222. Task: independent_weighted_period_review. Date: 2026-09-28. Only these files were read; their hashes were independently checked.

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| proofs/kernels/m9_m2_unbalanced_inverse_selector_reciprocity_projective_obstruction.md | 584745fb9af72993a4b33eb95dad3421e8924ae5fb64c5b314511b08d4254baf |
| rounds/codex-managed/m9-m2-complete-unbalanced-vector/reports/blind_cross_modulus.md | 707a618e63169cc0251cdce6efc55dd2ed442e1751d9456649fea0df6be568d2 |
| rounds/codex-managed/m9-m2-complete-unbalanced-vector/briefs/conductor_actual_unbal_interface.md | 7cb7bfd2a69a6cf57e2bdbb0bc90f0f65f09696edbb2a1cf05e09502500045c3 |
| rounds/codex-managed/m9-m2-complete-unbalanced-vector/controls/conductor_weighted_period_control.md | 3928e5f90f98c95403ba762c68e6f86141efba1e821c29393cbf7a45c2575e32 |

The supplied control/interface record graph hash a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b; the graph itself was not read. Accepted160 status is conductor-supplied. Its source cards and the historical143 report were not reopened.

This reused agent retains rounds217--221 and authored the frozen round222 statement-only finite report. The present review is post-isolation and NONBLIND, not history-free and not independent revalidation of that authored proof. No other attack, sibling, shared state, source, new agent or successor was accessed. Only this assigned review was written.

## 7. Recommended state effect

**GREEN: retain the exact weighted-orthogonality scope control.** Reject only the free inference from bare-row orthogonality to the actual weighted rows. No accepted exponent, complete UNBAL bound, parent obligation or quarter-goal status changes. The actual signed vector estimate and endpoint companions remain open. Stop after this bounded report and hash.
