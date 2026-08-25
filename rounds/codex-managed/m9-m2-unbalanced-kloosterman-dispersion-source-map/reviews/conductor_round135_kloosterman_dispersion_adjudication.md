# Round 135 conductor adjudication: Kloosterman-fraction and dispersion interfaces

Campaign: `m9-m2-unbalanced-kloosterman-dispersion-source-map`

Starting graph SHA-256:
`f9aa6fa43900b9cb73f705405f9a6090e6e84fb5d3c8a9e037ffe3c6911b9ea0`

## 1. Result

Close Round 135 under `source_level_no_go`.

The round produces two promotable results.

1. The exact Bettin--Chandee v1 and Wright v2 source statements, including
   Bettin--Chandee Corollary 1, are source-audited with their frequency,
   coefficient, coprimality, fixed-factor, range, and absolute-value
   hypotheses.
2. Their complete literal interfaces with the frozen flat-smooth
   prescribed-centre M2 UNBAL wave are exhausted at source level. Direct
   (m=1), the sharp (a=m^2) connector, inverse completion, Wright
   dispersion, and fixed-determinant completion either exceed the known
   capacity or return it exactly. None proves a smaller owner-complete
   survivor.

The key repair is positive: a real project centre is not an obstruction.
Writing (X=N_0+\xi) and absorbing (e(\xi k/r)) into the uniformly
smooth flat tensor makes every source frequency integral and leaves all
norms unchanged. A second repair separates two inequivalent completions:
smooth-weight-first completion is Ramanujan and returns (\Delta), while
inverse-selector-first completion is Kloosterman and costs
(R\sqrt\Delta).

The quarter estimate remains open. The result is a no-go for the audited
published source interfaces, not a lower bound for the literal signed wave
and not a no-go for a new coupled-coefficient theorem.

## 2. Exact statement and hypotheses

Let

\[
 D=X^\delta,\qquad L=X^\ell,\qquad R=X/D,\qquad
 K=XL/D^2,\qquad \Delta=R/K=D/L,
\]

with

\[
 \frac14\le\delta<\frac12,\qquad
 0\le\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463.
\tag{135.1}
\]

Put (u=\delta-\ell) and (F=XK/R=X^{1-u}). Then
(1/4<u<1/2), (1<K<R), and the frozen packet is

\[
 \mathscr R_{D,L}(X)=
 \sum_{r\asymp R,\ r\text{ odd}}\chi_4(r)W(X/(rD))
 \sum_{k\asymp K}\frac{q_L(4Xk/r^2)}k e(Xk/r).
\tag{135.2}
\]

The accepted proposition is:

> **Round-135 source-interface proposition.** On a fixed flat smooth cell,
> write (X=N_0+\xi), (N_0=\lfloor X\rfloor). The complete profile,
> including (e(\xi k/r)), admits exact independent Fourier--Mellin
> separation with (O(1)) integrated projective norm. With integral source
> frequency (N_0), the direct (m=1) and coprime (a=m^2) dictionaries
> are legal for every real (X), but every Bettin--Chandee and Wright bound
> exceeds (\Delta) by a fixed power on (135.1). Smooth-weight-first
> completion is an owner-complete Ramanujan calculation of size
> (\Delta X^\varepsilon). Inverse-selector-first completion produces a
> joint Kloosterman coefficient matrix and positive cost
> (R\sqrt\Delta X^\varepsilon). The physical wave does not meet Wright's
> fixed-residue dispersion hypotheses. Bettin--Chandee Corollary 1 accepts
> the exact determinant dictionary, but its main terms aggregate to
> (\Delta X^\varepsilon) and its error is much larger. Consequently these
> sources neither prove the quarter estimate nor improve the accepted
> flat-wave envelope.

Only the flat-smooth principal owner is covered. Sharp, clipped, starred,
hard, arithmetic-owner, stationary-entry, transition, remainder, BAL, TOP,
complete-UNBAL, endpoint, M9-M2, M9-M1, M9, and global packets are excluded.

## 3. Proof or derivation

On (k=Ku,r=Rv), the fractional phase is

\[
 e(\xi k/r)=e\!\left(\xi\Delta^{-1}u/v\right).
\]

All normalized derivatives are (O(1)), uniformly in (0\le\xi<1).
Buffered log-Fourier inversion therefore separates the complete profile
with (O(1)) (L^1) spectral mass. A direct fibre has coefficient norms

\[
 \|\alpha\|_2=1,\qquad \|\beta\|_2\asymp R^{1/2},\qquad
 \|\nu\|_2\asymp K^{-1/2}.
\tag{135.3}
\]

For direct (m=1,a=k,n=r,\vartheta=N_0), Bettin--Chandee gives

\[
 F^{1/2}\left(R^{11/10}K^{-3/20}+R\right)X^\varepsilon.
\tag{135.4}
\]

Its exponents are

\[
 E_{\rm BC,1}=\frac{29}{20}+\frac{7\ell}{20}
 -\frac{13\delta}{10},\qquad
 E_{\rm BC,2}=\frac32+\frac\ell2-\frac{3\delta}{2},
\]

and

\[
 E_{\rm BC,1}-u>\frac3{10},\qquad
 E_{\rm BC,2}-u>\frac14.
\tag{135.5}
\]

Wright with fixed factor (R_0=1) gives

\[
 R^{11/8}F^{1/4}X^\varepsilon,
\qquad E_{\rm W}-u>\frac5{16}.
\tag{135.6}
\]

A growing fixed factor is unavailable because the direct source variable
has (M=1), forcing (R_0=O(1)).

For the nonconstant connector, (a=j^2,j=m=k,n=r) and
(m^2\overline m\equiv m\pmod r). The diagonal decomposition

\[
 \mathbf1_{j=m}=\int_0^1e(t(j-m))\,dt,
 \quad \alpha_m=m^{-1/2}e(-tm),
 \quad \nu_{j^2}=j^{-1/2}e(tj)
\tag{135.7}
\]

has sharp projective norm (\asymp1), the nuclear norm of the diagonal
matrix (m^{-1}\mathbf1_{j=m}). At source lengths
((A,M,N)=(K^2,K,R)), Bettin--Chandee gives

\[
 F^{1/2}\left(K^{21/20}R^{11/10}+K^{11/8}R\right),
\tag{135.8}
\]

and Wright gives (F^{1/4}KR^{11/8}). Their three exponent margins over
(u) exceed (3/10,1/4,5/16), respectively.

For completion, first restore every gcd stratum by (r=gn,k=gj). If the
smooth (j)-weight is completed first, its normalized coefficients obey

\[
 |\widehat b_{g,n}(h)|
 \ll_B R^{-1}\left(1+\|h\|_n/\Delta\right)^{-B}.
\tag{135.9}
\]

Inversion permutes units, so the complete inner sum is
(\mathfrak c_n(N_0+h)). Using

\[
 |\mathfrak c_n(q)|\le(n,q),\qquad
 \sum_{n\asymp T}(n,q)/n\ll X^\varepsilon
\]

and summing the (O(\Delta)) effective frequencies and harmonic gcd
strata gives exactly

\[
 |\mathscr R_{D,L}(X)|\ll\Delta X^\varepsilon.
\tag{135.10}
\]

If instead the rough inverse selector is completed in (m), the exact
form is

\[
 \sum_h\widehat g_r(h)S(N_0,h;r),\qquad
 \sum_h|\widehat g_r(h)|^2\ll(rK)^{-1}.
\tag{135.11}
\]

The complete-frequency second moment
(\sum_h|S(N_0,h;r)|^2=r\varphi(r)) yields a row cost
(\sqrt\Delta) and outer positive cost

\[
 R\sqrt\Delta X^\varepsilon
 =X^{1-(\delta+\ell)/2+\varepsilon},
\tag{135.12}
\]

whose exponent exceeds (u) by more than (1/4). The coefficient in
(135.11) depends jointly on ((r,h)), outside both trilinear theorems.

Finally, (s=N_0+t) gives the fixed residue
(t\equiv-N_0\pmod r), but not Wright's independent, uniformly coprime
convolution or its modulus-by-modulus discrepancy. For
(\tau=N_0-dr\ne0), Bettin--Chandee Corollary 1 accepts

\[
 (m_1,n_2,m_2,n_1)=(d,r,1,N_0),\qquad
 m_1n_2-m_2n_1=-\tau.
\tag{135.13}
\]

Its error per level is

\[
 X^{3/5+\varepsilon}R^{17/20}
 =X^{29/20-17\delta/20+\varepsilon},
\tag{135.14}
\]

with exponent greater than (41/40). Its main term is (O(X^\varepsilon))
per level; the (O(\Delta X^\varepsilon)) effective levels return
(\Delta X^\varepsilon). The zero determinant is divisor-bounded.

## 4. First doubtful or unproved step

There is no remaining source, phase, coefficient-norm, or exponent gap in
the scoped no-go. The first unproved positive step is a new estimate for

\[
 \sum_{k\asymp K}\frac1k\sum_{r\asymp R}
 \chi_4(r)G(k/K,r/R)e(Xk/r),
\tag{135.15}
\]

or the exact fixed-centre divisor form, that preserves the signed modulus
family before every positive norm and beats

\[
 X^\varepsilon\min\!\left(\Delta,
 \sqrt{XL/D}+\sqrt{X/(LD)}\right).
\tag{135.16}
\]

Neither audited source supplies this joint coefficient-matrix theorem. The
round does not show that (135.15) is large, and it does not control omitted
owners.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Primary versions and theorem text | Green. Bettin--Chandee v1 Theorem 1, Remark 1, Corollary 1, and Wright v2 Theorem 2.1 were checked. The withdrawn paper was excluded. |
| Frequency and real centre | Green after repair. Use integral (N_0) and absorb (e(\xi k/r)) into the flat tensor. |
| Moving profile | Green. Exact log-Fourier separation has (O(1)) integrated mass and retains (q_L,W,1/k). |
| Direct source normalization | Green. Literal norm scale is used; all displayed exponents exceed (\Delta). |
| Wright source discrepancy | Green with convention. The printed third term is weaker than the proof's final third term; the common fifth term dominates. |
| Square connector | Green after repair. The identity is exact and the sharp diagonal norm is (\asymp1). |
| Completion order | Green after separation. Smooth-first is Ramanujan and equal-capacity; inverse-first is Kloosterman and rough. |
| Gcd ownership | Green. All strata are restored before the final triangle. |
| Physical residue | Green as a no-go. The exact residue is (-N_0); the remaining Wright hypotheses still fail. |
| Fixed determinant | Green. Source hypotheses, main term, error, and determinant aggregation all match. |
| Character and absolute values | Green. (\chi_4) remains inside the signed source coefficient until a positive source norm is taken. |
| Polytope and owner scope | Green. No endpoint or downstream owner is promoted. |

No numerical experiment was used. The round was 100% analytical,
algebraic, and source-audit work.

## 6. Dependencies and exact artifacts used

The adjudication uses:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/wright_bc_exact_source_card.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/literal_wave_kloosterman_map_attack.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/reports/blind_inverse_congruence_interface_audit.md`;
- all three Round-135 post-unmask reviews;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/candidates/conductor_degenerate_source_capacity.md`;
- `rounds/codex-managed/m9-m2-unbalanced-kloosterman-dispersion-source-map/sources/bettin_chandee_wright_kloosterman.md`.

Primary sources:

- Bettin--Chandee, arXiv:1502.00769v1,
  <https://arxiv.org/html/1502.00769v1>;
- Wright, arXiv:2604.25177v2,
  <https://arxiv.org/html/2604.25177v2>;
- withdrawn negative control, <https://arxiv.org/abs/2601.00292>.

## 7. Recommended state effect

Promote a source-audit node and one scoped internal interface-obstruction
node. Add the round as negative/inconclusive route evidence to the open
flat-wave target and as positive clarification evidence to the exact
prescribed-centre return and curvature-envelope nodes.

Reject the claims that the real centre or moving profile prevents every
source call, that an ordinary fraction cannot have an inverse-phase
encoding, that the (a=m^2) detector costs (K), that every completion is
Kloosterman or every completion is Ramanujan, that the fixed residue is
nonintegral, that Wright's fixed factor can be the growing project modulus,
that Corollary 1 proves the target, or that the scoped source no-go is a
universal lower bound.

Keep M9-M1, M9-M2, endpoint uniformity, M9, the conditional bridge, the
internal one-third theorem, the repaired external Li--Yang exponent, and
the quarter target unchanged.
