# Round222: the complete UNBAL target and a weighted cross-modulus Gram attempt

## 1. Result

**`complete_unbal_vector_attempt_no_new_bound`.** The complete actual inequality

\[
 \mathcal T_{L,K}=\sum_{h\asymp L,k\asymp K}
 \chi_4(h)a_{L,K}(h,k)e(\sqrt{Xhk})
 \ll_\epsilon (LK)^{3/4}X^\epsilon,
 \qquad K=XL/D^2,\quad K/L>16,
 \tag{1}
\]

remains open. This report tests one joint frequency Gram mechanism on the
literal inverse-selector representation, including all modulus and gcd rows
before taking a modulus triangle. It derives the complete weighted output
and prices a short-window closure. The resulting bound is only

\[
 |\mathcal R|\ll_\epsilon R^{3/2}X^\epsilon,
 \qquad R=X/D.                                             \tag{2}
\]

It is worse than the inherited flat envelope and gives no complete-owner
gain. Equation (2) is an upper price of this closure, not a lower bound or
an assertion that the actual sum attains it. This is neither the old143
rowwise Kloosterman Cauchy calculation nor160 Hilbert scalarization.

There is an exact weighted orthogonality control. For
\(F_{g,n}(h)=\widehat\gamma_{g,n}(h)S(N_0,h;n)\), its zero Fourier
coefficient is the original reciprocal row divided by \(n\). Consequently
coprime moduli do **not** make complete correlations of these weighted
rows vanish. Deleting the single residue \(h=0\) also does not remove this
mean. A common-period mean-square replacement retains the unknown target
in its zero-frequency term.

The complete smooth identity supplies the unchanged elementary fallback
\(\min(D,\sqrt{XL/D})+O_W(1)\) for the displayed original smooth block and
its actual sign/shift companions. Thus its uniform active-triangle price
is at most \(X^{3/8+\epsilon}\); the better flat envelope is used only for
the flat owner. No new estimate is asserted for any additional separately
owned correction. The graph's complete UNBAL node, M2, M1, endpoints and
full quarter goal are unchanged.

## 2. Exact statement and hypotheses

All real \(X=N_0+\xi\), \(N_0=\lfloor X\rfloor\), \(0\leq\xi<1\),
are retained. Put

\[
 R=X/D,\quad K=XL/D^2,\quad \Delta=R/K=D/L,\quad M=LK.
 \tag{3}
\]

The original actual smooth positive block in the frozen interface is

\[
 \mathcal B^+=-\frac1\pi\sum_h\frac{\chi_4(h)q_L(h)}h
                 \sum_dW(d/D)e(hX/(4d)),
\quad q_L(h)=\eta(h/L)\Phi(h/(H_D+1)),\quad
 H_D=\lfloor DX^{-1/4}\rfloor.                            \tag{4}
\]

The exact smooth transformation has normalized symbol

\[
 a_{L,K}(h,k)=q_L(h)(LK/(hk))^{3/4}
       W\!\left(\sqrt{hX/(4kD^2)}\right),
\quad
 \mathcal B^+=-\frac{e(1/8)}{2\pi}X^{1/4}M^{-3/4}
                 \mathcal T_{L,K}+O_W(1).                 \tag{5}
\]

The smooth profiles and every literal entry, exit, floor and weight are
those of the packet. Negative frequencies and the two quarter shifts
remain; no estimate of a real part is inverted to estimate its complex
parent. Hard-TOP is outside (5). The complete target (1) additionally
retains all of its assigned transform-boundary modules. No flat formula
below is declared an identity for these extra modules.

For the frozen flat component only, let \(i=(g,n)\), with odd \(g,n\),
\(gn\asymp R\), \(1\leq g\ll K\), and define

\[
 w_i=\chi_4(g)\chi_4(n)W(X/(gnD)),
\quad b_i(j)=\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n).
 \tag{6}
\]

The \(j\)-support \(\mathcal J_i\), of length \(O(K/g)\), is the
literal moving support, restricted to \((j,n)=1\) and zero extended.
Its endpoints, including any prescribed fractional endpoint weights,
are never moved. In the strict residual region this support has no
residue collisions, since \(K/g\ll n\) with ratio \(\Delta^{-1}\to0\).
All formulae below still hold by summing coefficients of equal residues
if necessary. Set

\[
 \widehat\gamma_i(h)=\frac1n\sum_j b_i(j)e(-h\bar j_n/n),
\quad S(N_0,h;n)=\sum_{x\bmod n}^{*}e((N_0\bar x_n+hx)/n),
 \tag{7}
\]

\[
 F_i(h)=\widehat\gamma_i(h)S(N_0,h;n),\quad
 U_i=\sum_j b_i(j)e(N_0j/n),\quad
 \mathcal R=\sum_iw_iU_i.                                \tag{8}
\]

There is no assumption \((N_0,n)=1\). The elementary actual coefficient
bounds needed here are

\[
 B_i:=\sum_j|b_i(j)|\ll_\epsilon X^\epsilon/g,
 \qquad |w_i|\ll_W1.                                     \tag{9}
\]

The strict flat comparison region is

\[
 D=X^\delta,\quad L=X^\ell,\quad
 1/4\leq\delta<1/2,\quad0\leq\ell<\delta-1/4,\quad
 178\ell+1638\delta>463.                                  \tag{10}
\]

Here \(a=\delta-\ell\in(1/4,1/2)\). The accepted flat physical envelope
is \(X^\epsilon\min(\Delta,\sqrt{XL/D}+\sqrt{X/(LD)})\), of power
\(\beta(a)=\min(a,(1-a)/2)>1/4\). This upper envelope carries no
actual-sign saturation claim.

## 3. Derivation and complete costs of the one mechanism

**Exact weighted Fourier rows.** Opening both factors in (7) gives the
finite, complete expansion

\[
 F_i(h)=\sum_{t\bmod n}c_i(t)e(ht/n),
\quad c_i(t)=\frac1n\sum_j b_i(j)
 \mathbf1_{(t+\bar j_n,n)=1}
 e\!\left(\frac{N_0\overline{t+\bar j_n}_n}{n}\right).
 \tag{11}
\]

This includes every large frequency and every gcd case. In particular

\[
 c_i(0)=U_i/n,\qquad |c_i(t)|\leq B_i/n
       \ll_\epsilon X^\epsilon/(gn).                     \tag{12}
\]

No derivative is taken across an inverse selector or a moving endpoint.
The residual factor \(e(\xi j/n)\) remains inside \(b_i\); its modulus
one is used only in (9).

For two rows \(i=(g,n)\), \(i'=(g',m)\), let \(d=(n,m)\) and
\(P=[n,m]\). Orthogonality on the **complete** common period gives

\[
 \frac1P\sum_{h\bmod P}F_i(h)\overline{F_{i'}(h)}
 =\sum_{v\bmod d}c_i(nv/d)\overline{c_{i'}(mv/d)}.          \tag{13}
\]

Indeed \(t/n-s/m\in\mathbb Z\) is equivalent to equality of the two
reduced fractions; their common denominator divides \(d\). If \(d=1\),
the unnormalized correlation in (13) is exactly
\(U_i\overline{U_{i'}}\), since \(P=nm\). This is generally nonzero.

Zeroing the residue \(h=0\pmod n\) replaces
\(F_i\) by \(F_i^\circ=F_i-F_i(0)\mathbf1_{n\mid h}\), and every
coefficient by

\[
 c_i^\circ(t)=c_i(t)-F_i(0)/n.
 \tag{14}
\]

Thus its zero coefficient is \((U_i-F_i(0))/n\), not zero. For coprime
moduli the complete unnormalized correlation becomes
\((U_i-F_i(0))\overline{(U_{i'}-F_{i'}(0))}\). This independently
verifies the conductor's weighted-row control without reading any
current sibling work.

For another direct check, let \(P_*\) be the finite least common multiple
of all row moduli and set \(Q(h)=\sum_iw_i nF_i(h)\). Its mean over
\(P_*\) is exactly \(\mathcal R\). Parseval says

\[
 P_*^{-1}\sum_{h\bmod P_*}|Q(h)|^2
 =|\mathcal R|^2+\sum_{\theta\ne0}|\widehat Q(\theta)|^2.
 \tag{15}
\]

The deleted version has \(\mathcal R^\circ=\sum_iw_i(U_i-F_i(0))\)
in place of \(\mathcal R\). Increasing to this complete period does not
prove a bound for its retained zero mode. No estimate treats \(P_*\) or
the pair period \([n,m]\) as the physical window length.

**The actual short window and its Gram.** Take an integer \(H\asymp R\)
at least every supported \(n\), and retain the literal mask
\(m_i(h)=\mathbf1_{1\leq h<n}\), \(1\leq h\leq H\). Then

\[
 A(h)=\sum_iw_i m_i(h)F_i(h),\qquad
 \mathcal R^\circ=\sum_{h=1}^HA(h),\qquad
 |\mathcal R^\circ|^2\leq H\mathcal E,
\quad \mathcal E=\sum_{h=1}^H|A(h)|^2.                    \tag{16}
\]

For \(D_V(\theta)=\sum_{h=1}^{V}e(h\theta)\), the complete output is

\[
 \mathcal E=\sum_{i,i'}w_i\overline{w_{i'}}
 \sum_{t\bmod n,s\bmod m}c_i(t)\overline{c_{i'}(s)}
 D_{\min(n,m)-1}(t/n-s/m).                                \tag{17}
\]

Equations (6), (11) and (17) retain both characters and all four
\((g,n,j,h)\) coordinates jointly. There is no replacement by products
of independent row coefficients and no omission of the noncoprime
modulus pairs. The kernel in (17) is a short Dirichlet sum, never the
complete-period delta in (13).

Here is a self-contained closure of (17), rather than an unestimated
matrix grant. Distinct reduced frequencies of denominator at most
\(cR\) are separated on the circle by \(\gg R^{-2}\). For arbitrary
coefficients \(z_\theta\), the geometric-series bound and circular
ordering give

\[
 \sum_{h=1}^H\left|\sum_\theta z_\theta e(h\theta)\right|^2
 \ll(H+R^2\log(2R))\sum_\theta|z_\theta|^2.               \tag{18}
\]

To see this without importing a large-sieve theorem, the frequency Gram
has entries bounded by
\(\min(H,(2\|\theta-\theta'\|)^{-1})\). For a fixed row, ordering
the other points in the two circular directions bounds its absolute row
sum by \(H+CR^2\sum_{v\leq CR^2}v^{-1}\). Applying
\(2|z_\theta z_{\theta'}|\leq|z_\theta|^2+|z_{\theta'}|^2\)
proves (18).

Allow any additional row factor \(r_i\) with \(|r_i|\leq1\). At a
reduced fraction \(\theta=p/q\), group **all** equal frequencies:

\[
 C_\theta(r)=\sum_{\substack{i=(g,n)\,;\,q\mid n}}
                 w_i r_i c_i(np/q).
 \tag{19}
\]

The exact characters have not been replaced in this definition. Its
elementary upper bound is

\[
 |C_\theta(r)|\ll X^\epsilon
 \sum_{g\ll K}\frac1g
 \sum_{\substack{n\asymp R/g\\q\mid n}}\frac1n
 \ll\frac{X^\epsilon(1+\log(2K))}{q}.                     \tag{20}
\]

The inner reciprocal sum is \(O(1/q)\), including a terminal single
multiple. Rows with no support contribute zero. The bound includes all
odd gcd strata; allowing extra even terms on the right only enlarges a
positive estimate. The \(q=1\) frequency is included once. Hence

\[
 \sum_\theta|C_\theta(r)|^2
 \ll X^\epsilon(1+\log(2K))^2
       \sum_{q\leq cR}\frac{\varphi(q)}{q^2}
 \ll X^\epsilon(1+\log(2K))^2(1+\log(2R)).                \tag{21}
\]

This is where the grouped character cancellation is discarded and the
mechanism loses the sought arithmetic saving. No lower bound is inferred
from (20) or (21).

The mask in (16) must still be paid. Use the exact finite prefix
decomposition on the cyclic group of order \(2H+1\). For each cutoff
\(n-1\), its prefix indicator is a sum of row factors of modulus one
times common column phases, with the sum of the absolute Fourier
coefficients \(O(1+\log(2H))\). This follows by summing its geometric
Fourier coefficients, bounded by
\(\min(H/(2H+1),1/(2\min(r,2H+1-r)))\). Empty prefixes are allowed.
It is also exactly the prefix part of the allowed220 mask lemma; no
arithmetic all-row bound is assumed from that lemma.

Apply (18)--(21) separately to each term of this exact mask expansion,
then the triangle inequality in the common column \(\ell^2\) space.
The row factors have the precise bounded type already allowed in (19).
For example an explicit, deliberately loose logarithmic ledger is

\[
 \mathcal E\ll X^\epsilon R^2
 (1+\log(2K))^2(1+\log(2R))^4.                            \tag{22}
\]

All logarithms can be absorbed by reselecting \(\epsilon\); the proof
uses no loss in a power of \(K\) for endpoint completion. Equations
(16) and (22) prove (2) for \(\mathcal R^\circ\). The removed
\(h=0\) Ramanujan total is the accepted \(O_\epsilon(X^\epsilon)\)
term, restored exactly once. This prices the whole attempted output.
No unestimated large-frequency or tail term remains in this finite
closure.

**Physical powers and full-owner fallback.** On the flat owner the
stationary physical factor is \(-i/(2\pi)\), so (2) has physical power
\(3(1-\delta)/2\). Relative to a quarter bound its excess power is
\(5/4-3\delta/2>1/2\) throughout (10). Its normalized target price is

\[
 M^{3/4}X^{-1/4}R^{3/2}X^\epsilon,
 \tag{23}
\]

with the flat transformation's inherited target-safe error separately
restored. This is much worse than the inherited flat envelope, which is
therefore retained instead of (23). Its missing power remains
\(a-1/4\) for \(a\leq1/3\), and \((1-2a)/4\) for \(a\geq1/3\).

For the complete explicitly displayed smooth physical block, go back to
(4), not to the flat representation. The actual finite weights satisfy
\(\sum_{h\asymp L}|q_L(h)|/h\ll1\), and the physical \(d\)-sum has
\(O(D)\) terms. Thus \(|\mathcal B^+|\ll D\), retaining the literal
floor and all endpoint conventions. Alternatively \(|a_{L,K}|\ll1\)
on its slanted support gives \(|\mathcal T|\ll M\); (5) gives

\[
 |\mathcal B^+|\ll\sqrt{XL/D}+O_W(1),\qquad
 |\mathcal B^+|\ll\min(D,\sqrt{XL/D})+O_W(1).             \tag{24}
\]

Both quarter shifts and negative/real-sign companions have the same
absolute estimates and cost a fixed factor. This use of finite sums
requires no limiting passage at support crossings. The exact smooth
Poisson error in (5) is \(O_W(1)\); it is not discarded. In exponent
coordinates (24) costs \(X^{\min(\delta,(1-a)/2)+\epsilon}\).
Since \(L\leq DX^{-1/4}\), it is uniformly at most
\(X^{3/8+\epsilon}\). Summing finitely many sign channels and the
\(O((\log X)^2)\) active smooth dyadic labels changes only
\(X^\epsilon\). Known covered subregions in the allowed source retain
their stronger bounds.

The scope of (24) is precisely the actual smooth original block to
which (5) applies. A correction package not represented in (4)--(5)
keeps its inherited bound and owner; this report supplies no new
flat-to-complete extension. In particular the unique physical hard top
band and the separate BAL/M1 parents cannot be restored by pretending
that they are flat UNBAL pieces. Thus neither (22) nor (24) is a new
complete proof of (1), M2 or the pointwise quarter theorem. The accepted
global exponent and accepted full-moment powers are unchanged.

## 4. First doubtful or unproved step

There is no unproved identity or source import in (11)--(22). The exact
first missing estimate for this proposed short-window certificate is

\[
 \mathcal E_{\rm actual}\ll_\epsilon X^{1/2+\epsilon}/R,
 \tag{25}
\]

with the literal coefficients and masks in (17); (16) would then give
the quarter bound for this flat representation. This is only a
sufficient certificate and is not claimed equivalent to the actual
signed target. The proved price (22) is \(R^2X^\epsilon\). Closing that
gap requires actual signed correlation beyond the denominator grouping
and absolute Gram row sums, not a notation change in their norms.

The false shortcut tested and rejected is substituting complete
unweighted Kloosterman orthogonality for (17). First, its physical
windows have length \(\min(n,m)-1\), not \([n,m]\). Second, even on
the complete period the weights change the correlation to (13), with
the retained row-total term. The purported cancellation fails before
any claim about the magnitude of the actual owner is reached.

Even a future proof of (25) would still require the complete actual
UNBAL transformation and all nonflat/endpoint companions at their
stated physical cost. This report does not grant that seam. No further
mechanism or smaller successor objective is proposed here.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Complete target and correct normalization | (1), (3)--(5) use \(K=XL/D^2\) and \(e(\sqrt{Xhk})\). The goal was not replaced by its flat fragment. |
| Both character directions | The full \(\chi_4(g)\chi_4(n)\) is present in (6), (17), (19); its loss is explicitly at (20). No arbitrary-phase bound is credited as actual cancellation. |
| Real centre | The exact \(e(\xi j/n)\) persists in (6), (11). No integer-centre approximation or deletion is made. |
| Arbitrary first-argument gcd and inverse representatives | (11)--(14) require only the explicitly indicated unit inverses. Changing a representative changes an exponent by an integer. No coprimality of \(N_0,n\) is used. |
| All gcd strata and long frequencies | The sums in (17), (19)--(21) include every supported odd \(g,n\), every \(t\bmod n\), and every original \(1\leq h<n\). There is no Linnik-range restriction. |
| Literal supports, floors and stars | They stay in \(b_i\); the separate physical \(h\)-mask is represented exactly at logarithmic cost. Empty rows/prefixes contribute zero; weighted terminal \(j\) entries satisfy (9). |
| Complete versus short period | (13) is used only at its complete period. The physical kernel remains \(D_{\min(n,m)-1}\) in (17), with the full spacing price in (18). |
| Weighted mean and single zero deletion | (12)--(15) prove the surviving reciprocal row totals before and after deletion. The accepted Ramanujan complement is restored once. |
| Fixed vector versus all vectors | (19)--(21) are proved for the actual coefficient family with bounded row multipliers. No separate-product theorem is upgraded to an all-combined-row theorem. |
| Norm and restored powers | (22)--(24) price all frequencies, masks, gcd strata, normalization and dyadic summation. The result loses to the already available flat envelope. |
| Source hypotheses | No new external theorem, spectral formula or current-source audit is used. Equation (18) is proved by finite geometric sums and an elementary Gram bound. |
| Actual versus enlarged obstruction | The report refutes an orthogonality replacement and locates an unproved sufficient estimate. It gives no signed lower bound and no universal impossibility theorem for vector methods. |
| Full goal | Smooth UNBAL, M2 TOP/BAL, M1, endpoint uniformity and the quarter theorem retain their original separate status. |

All controls are algebraic. Numerical experiments: zero. No floating
point, symbolic computation, generated data or empirical pattern is
used as evidence.

## 6. Dependencies and exact artifacts used

This is the selected-context discovery role `joint_cross_modulus_attack`,
campaign `m9-m2-complete-unbalanced-vector`, round222. It is not blind.
Prior authorship/review in218--221, including my221 anchored-Gram report
and shifted-correlation review, is disclosed inherited context, not fresh
isolation. The conductor's in-session weighted-row diagnostic was
independently derived in (11)--(15). No current sibling report was read.

Exact SHA256 inputs read, or retained from their earlier permitted read:

| Artifact | SHA256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b` |
| `state/active_campaign.yml` | `d06e5d01d1d3bd1db8634eba9b7107654215760cce125f3047e5e6feb2f93859` |
| `strategy/round222_complete_unbalanced_vector_attack.md` | `fc7d4efd2f4c740d4817dfc2cfa641f152c1772feb175305c83fe465f97d13b8` |
| `rounds/codex-managed/m9-m2-complete-unbalanced-vector/briefs/joint_cross_modulus_attack.md` | `b2daa38b1b990b6a7ccabac96eba097dd90e2310e4b9a8e7a085902a041e24af` |
| `rounds/codex-managed/m9-m2-complete-unbalanced-vector/briefs/conductor_actual_unbal_interface.md` | `7cb7bfd2a69a6cf57e2bdbb0bc90f0f65f09696edbb2a1cf05e09502500045c3` |
| `strategy/gauss_circle_strategy_checkpoint_round220_2026-09-28.md` | `6fc4b67a5de62a449527f62877933856635a9f6b0501a45f63539f05de6a5460` |
| `rounds/codex-managed/gc-actual-vector-gram-correlations/synthesis.md` | `93413bbc466cd48bc9fe4ebeede40c62bb218bb077f8afda1750c23805fb05dd` |
| `rounds/codex-managed/m9-frequency-phase-diagram/reports/dual_three_quarter_attack.md` | `a97702a1a4608e106d4171a4fd713eca5a2c9693b61ee89ca1eb0eb51621b3c3` |
| `proofs/kernels/m9_m2_unbalanced_inverse_selector_reciprocity_projective_obstruction.md` | `584745fb9af72993a4b33eb95dad3421e8924ae5fb64c5b314511b08d4254baf` |
| `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/level_four_kloosterman_embedding_attack.md` | `dea1172e467c6871652eefdc3f55dcc20b1288ea0cb25720b9ede222e4458b82` |
| `rounds/codex-managed/gc-full-goal-arithmetic-source-review/reports/blind_smooth_mask.md` | `e27659b89c33da6c8216f5817351edfa1a3fd269ffaeb8d8c1e51e6ce180e33b` |
| `rounds/codex-managed/gc-full-goal-arithmetic-source-review/reviews/conductor_smooth_mask_review.md` | `2a32e0d4c4856aad81ff8f219df1bb22b3658946c9281ac0f8b3c180cf65e716` |

The accepted inputs are used only within their scopes: the actual smooth
identity and symbol from the frequency-phase report, the flat
inverse-selector/zero-mode interface and old barriers from143/160, and
the exact prefix-mask algebra from220. The221 synthesis supplies the
closed prior-round and unchanged full-goal status, not an additional
estimate for (1). Effort was100 percent analytical/algebraic; no external
source audit, new agent, shared edit, successor design or experiment.

## 7. Recommended state effect

**No change** to accepted inequalities, the complete UNBAL node or the
full quarter goal. Retain this report as a bounded failed-certificate
record: the actual weighted common-period mean survives, and the fully
priced short-window rational-frequency Gram closure costs
\(R^{3/2}X^\epsilon\), with the better inherited flat fallback retained.

The finite identities and the conditional application boundary may be
retained as infrastructure after review. Do not promote (25), do not
rename a weighted zero-mode self-return as a gain, and do not promote
the flat wave into a complete smooth or hard-endpoint estimate. Only
the assigned report was written. The task stops at this frozen report.
