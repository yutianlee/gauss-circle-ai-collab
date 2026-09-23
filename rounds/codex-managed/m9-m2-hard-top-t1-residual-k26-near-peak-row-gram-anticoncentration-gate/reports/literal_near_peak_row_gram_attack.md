# Round 180 literal near-peak divisor-row Gram attack

- Campaign: `m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate`
- Round: 180
- Role: discovery
- Starting graph SHA-256:
  `e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4`
- Exit label: `row_gram_offdiagonal_capacity_or_self_return_no_go`
- Allocation: 100% analytical/algebraic; 0% numerical

## 1. Result

The local divisor-row decomposition gives an exact self-return, not the
missing factor \(L\).

Put

\[
 \mathcal G_\nu:=\frac12\sum_{\epsilon=0}^1
 \mathcal O_{\epsilon,\nu},\qquad
 \mathcal E_\nu:=\frac12\sum_{\epsilon=0}^1
 \int_{I_\nu}|Z_\epsilon(\theta)|^2\,d\theta,
\]

and let the **physical row diagonal** be

\[
 \mathcal D_\nu:=\frac12\sum_{\epsilon=0}^1
 \sum_{d\ {\rm odd}}\int_{I_\nu}
 |R_{\epsilon,d}(\theta)|^2\,d\theta.
\]

Then, before any positive estimate and with the complete literal
coefficient inside the displayed sums,

\[
 \boxed{\mathcal E_\nu=\mathcal D_\nu+\mathcal G_\nu.}
 \tag{180.A1}
\]

The literal incidence ledger and \(O(L)\) cofactor length give

\[
 0\le \mathcal D_\nu\ll_\varepsilon LX^\varepsilon.
 \tag{180.A2}
\]

Consequently, at target strength,

\[
 \boxed{
 \mathcal G_\nu\ll_\varepsilon LX^\varepsilon
 \quad\Longleftrightarrow\quad
 \mathcal E_\nu\ll_\varepsilon LX^\varepsilon,}
 \tag{180.A3}
\]

where the forward implication uses (180.A2), and the reverse implication
uses \(\mathcal G_\nu=\mathcal E_\nu-\mathcal D_\nu\le\mathcal E_\nu\).
Also \(\mathcal G_\nu\ge-\mathcal D_\nu\), so the negative side is already
target-safe; only the displayed one-sided upper estimate is open.
Thus adding the target-safe row diagonal turns (180.G) into the complete
local scalar anti-concentration theorem; it does not create a new row
orthogonality resource.

The exact off-row product diagonal \(dm=d'm'\) is owner-complete and
target-safe:

\[
 \mathcal P_\nu
 =\frac1M\sum_N\left\{(c_N^{\rm rem})^2
       -\sum_{\substack{d\mid N\\d\ {\rm odd}}}\lambda_N(d)^2\right\}
 \ll_\varepsilon X^\varepsilon.
 \tag{180.A4}
\]

After (180.A4), the exact complement consists of every nonzero even
product difference \(0<|dm-d'm'|<M\), with the sinc factor, cell-centre
phase, square-root phase, selectors, both two-adic branches, profiles,
hard values, endpoints, transitions, and zero extensions unchanged. Its
uniform \(O(LX^\varepsilon)\) estimate is unproved.

Coefficient-uniform control of (180.A1) has local capacity
\(L^2X^\varepsilon\), and this order is attained by both a complex
dechirped row array and a real cosine-dechirped row array satisfying the
same incidence energy and row-length ledgers. Arbitrary real signs also
attain this order. These arrays are false controls, not the literal
residual coefficient and not literal lower mass. They prove the scoped
no-go: row positivity, realness, the chirp, row length, energy, parity, or
\(\chi_4\) modulation separately cannot prove (180.G). A continuation
must prove a new property of the complete literal coefficient before any
positive row, shift, cell, mode, or divisor norm.

## 2. Exact statement and hypotheses

Let \(X\) be large,

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,
\]

and let \(M\asymp L^2\) be the exact cardinality of the containing
integer interval. Use \(e(t)=e^{2\pi i t}\). The coefficient
\(\lambda_N(d)\in\mathbb R\) is exactly the Round-180 literal coefficient:
it contains the selected/no-pair field, squarefree and coprimality masks,
both two-adic branches, near-square support, Vaaler and profile factors,
floor and star conventions, hard values, endpoints, transitions, support
births/deaths, and full-line zero extension. No factor is opened or
discarded below.

The permitted kernels give, and the literal support directly rederives,

\[
 \#\{(d,m):d\ {\rm odd},\ \lambda_{dm}(d)\ne0\}
 \ll_\eta L^2X^\eta,
 \qquad |\lambda_{dm}(d)|\ll_\eta X^\eta.
\]

After choosing \(\eta\) in terms of \(\varepsilon\),

\[
 \boxed{
 \Lambda_2:=\sum_{d\ {\rm odd}}\sum_m
 |\lambda_{dm}(d)|^2\ll_\varepsilon L^2X^\varepsilon.}
 \tag{180.A5}
\]

For every fixed odd \(d\), the literal near-square support contains
\(O(L)\) possible cofactors \(m\). Also

\[
 D_L:=\sum_N|c_N^{\rm rem}|^2
 =\|Z_\epsilon\|_{L^2(\mathbb T)}^2
 \ll_\varepsilon L^2X^\varepsilon
 \tag{180.A6}
\]

for either parity branch. These are the only positive input bounds used.

For integer \(|\nu|\le\lceil\sqrt L\rceil\), lift the wrapped half-open
cell to

\[
 \widetilde I_\nu=
 [(\nu-1/2)/M,(\nu+1/2)/M).
\]

Because \(\theta\mapsto e(h\theta)\) is \(1\)-periodic for integer \(h\),
integration over \(I_\nu=\widetilde I_\nu\pmod1\), including the cell
which wraps through \(0\), gives exactly

\[
 K_\nu(h):=\int_{I_\nu}e(h\theta)\,d\theta
 =\begin{cases}
 \displaystyle e(\nu h/M)\frac{\sin(\pi h/M)}{\pi h},&h\ne0,\\[6pt]
 \displaystyle M^{-1},&h=0.
 \end{cases}
 \tag{180.A7}
\]

Half-open endpoint choices do not add a boundary mass.

Expanding (180.4) only after the complete row-pair sum and averaging the
two parity branches gives

\[
\begin{aligned}
 \mathcal G_\nu
 =2\Re\sum_{\substack{d<d'\\d,d'\ {\rm odd}}}
 \sum_{\substack{m,m'\ge1\\m\equiv m'\ ({\rm mod}\ 2)}}
 &\chi_4(d)\chi_4(d')\lambda_{dm}(d)\lambda_{d'm'}(d')\\
 &\times e\!\left(J(\sqrt{dm}-\sqrt{d'm'})\right)
 K_\nu(dm-d'm').
\end{aligned}
 \tag{180.A8}
\]

Indeed

\[
 \frac12\sum_{\epsilon=0}^1(-1)^{\epsilon(m-m')}
 =\mathbf1_{m\equiv m'\ ({\rm mod}\ 2)}.
\]

Since \(d,d'\) are odd, this is equivalently \(dm\equiv d'm'\pmod2\).
Thus both the odd--odd and squarefree even--even branches remain, while
the mixed branch alone vanishes. Formula (180.A8), not a rowwise
absolute value, is the frozen object.

## 3. Proof or derivation

### 3.1 Physical row diagonal and exact self-return

Let

\[
 r_d=\#\{m:\lambda_{dm}(d)\ne0\}\ll L.
\]

For every \(\epsilon,d,\theta\), Cauchy's inequality applied only inside
the physical row gives

\[
 |R_{\epsilon,d}(\theta)|^2
 \le r_d\sum_m|\lambda_{dm}(d)|^2.
\]

The cell has length \(1/M\), so (180.A5) yields

\[
 \mathcal D_\nu
 \le \frac{\max_d r_d}{M}\Lambda_2
 \ll_\varepsilon \frac{L}{M}L^2X^\varepsilon
 \ll_\varepsilon LX^\varepsilon.
\]

This is the complete physical \(d=d'\) row block, including its own
off-product sinc terms; it is not a fixed diagonal after character or
ordinary Poisson. Expanding the square of the fully recombined
\(Z_\epsilon=\sum_d\chi_4(d)R_{\epsilon,d}\) proves (180.A1), hence
(180.A3). The first positive full norm is therefore taken only after all
literal row signs and the one outer real part have recombined.

### 3.2 Exact product collisions and retained complement

At \(dm=d'm'=N\), oddness of \(d,d'\) makes both cofactors have the same
parity, the square-root and cell-centre phases cancel, and (180.A7) has
value \(1/M\). Therefore

\[
\begin{aligned}
 \mathcal P_\nu
 &=\frac2M\sum_N\sum_{\substack{d<d'\\d,d'\mid N\\d,d'\ {\rm odd}}}
 \chi_4(d)\chi_4(d')\lambda_N(d)\lambda_N(d')\\
 &=\frac1M\sum_N\left\{(c_N^{\rm rem})^2
 -\sum_{\substack{d\mid N\\d\ {\rm odd}}}\lambda_N(d)^2\right\}.
\end{aligned}
 \tag{180.A9}
\]

If \(t_N\) is the number of live odd divisor incidences above \(N\), then

\[
 \left|(c_N^{\rm rem})^2-\sum_d\lambda_N(d)^2\right|
 \le (t_N-1)\sum_d|\lambda_N(d)|^2.
\]

The divisor bound \(t_N\le\tau(N)\ll_\eta X^\eta\), (180.A5), and
\(M\asymp L^2\) prove (180.A4), after epsilon rebudgeting.

The exact retained remainder is

\[
\begin{aligned}
 \mathcal G_\nu-\mathcal P_\nu
 =2\Re\sum_{\substack{d<d'\\d,d'\ {\rm odd}}}
 \sum_{\substack{m\equiv m'\ ({\rm mod}\ 2)\\dm\ne d'm'}}
 &\chi_4(d)\chi_4(d')\lambda_{dm}(d)\lambda_{d'm'}(d')\\
 &\times e\!\left(J(\sqrt{dm}-\sqrt{d'm'})
 +\frac{\nu(dm-d'm')}{M}\right)\\
 &\times\frac{\sin(\pi(dm-d'm')/M)}
 {\pi(dm-d'm')}.
\end{aligned}
 \tag{180.A10}
\]

Both products lie in one \(M\)-site containing interval, so every term in
(180.A10) has \(0<|dm-d'm'|<M\). Thus all nonzero product
near-collisions are retained; none is replaced by an absolute kernel.

For the fixed-shift check, put for \(0<h<M\), \(2\mid h\),

\[
\begin{aligned}
 C_h^{\rm off}:=\sum_N
 e\!\left(J(\sqrt{N+h}-\sqrt N)\right)
 \sum_{\substack{d\mid N+h,\ d'\mid N\\d,d'\ {\rm odd},\ d\ne d'}}
 \chi_4(d)\chi_4(d')
 \lambda_{N+h}(d)\lambda_N(d').
\end{aligned}
 \tag{180.A11}
\]

Zero extension makes (180.A11) endpoint-complete. Conjugate pairing in
(180.A10) gives exactly

\[
 \mathcal G_\nu-\mathcal P_\nu
 =2\Re\sum_{\substack{0<h<M\\2\mid h}}K_\nu(h)C_h^{\rm off}.
 \tag{180.A12}
\]

Adding the \(d=d'\) part reconstructs the complete literal coefficient
correlation at shift \(h\); its total cell contribution is precisely the
target-safe physical row term already separated in (180.A1). Hence
fixed-shift reindexing self-returns to the Round-164 shifted correlation.
Taking \(|C_h^{\rm off}|\) separately would discard the one outer real
part and is not licensed.

### 3.3 Local and endpoint power restoration

Let \(S\le M\) be the number of supported products. Cauchy before
integrating a cell gives the coefficient-uniform bound

\[
 \mathcal E_\nu
 \le \frac{S}{M}D_L
 \ll_\varepsilon L^2X^\varepsilon.
 \tag{180.A13}
\]

Thus the local target is \(L\), while the available local positive
capacity is \(L^2\).

For completeness, assume the still-open bound (180.G). Equations
(180.A1)--(180.A2) then give \(\mathcal E_\nu\ll LX^\varepsilon\) in
every near cell. On \(I_\nu\),

\[
 F_M(\theta)\ll \frac{M}{1+\nu^2}.
\]

Hence the complete near cells cost

\[
 \sum_{|\nu|\le\lceil\sqrt L\rceil}
 \frac{M}{1+\nu^2}\mathcal E_\nu
 \ll_\varepsilon MLX^\varepsilon
 \ll_\varepsilon L^3X^\varepsilon.
 \tag{180.A14}
\]

On \(M\|\theta\|\ge\sqrt L\), (180.8) gives
\(F_M(\theta)\ll M/L\asymp L\); Parseval and (180.A6) give

\[
 \frac12\sum_\epsilon\int_{M\|\theta\|\ge\sqrt L}
 F_M(\theta)|Z_\epsilon(\theta)|^2\,d\theta
 \ll_\varepsilon L^3X^\varepsilon.
 \tag{180.A15}
\]

The character-Poisson ordinary-zero component must be restored only after
all odd character frequencies recombine. The exact reverse-transform
formula is

\[
 Z_{\epsilon,0}(\theta)
 =\sum_{d\ {\rm odd}}\chi_4(d)
   \int_{\mathbb R}\mathcal B_{\epsilon,\theta}(d,y)\,dy.
\]

One integration by parts in \(y\), where the phase derivative is
\(\asymp J\) on every compact cardinal cell, gives

\[
 \sup_{\epsilon,\theta}|Z_{\epsilon,0}(\theta)|
 \ll_\eta \frac{L^2}{J}X^\eta.
\]

Therefore, using \(F_M\le M\), (180.A6), \(M\asymp L^2\), and
\(L^2\le J\),

\[
\begin{aligned}
 \left|\frac12\sum_\epsilon\int F_M
 \left(|Z_{\epsilon,0}|^2
 +2\Re Z_{\epsilon,0}\overline{Z_{\epsilon,*}}\right)\right|
 &\ll M\left(\frac{L^4}{J^2}
 +D_L^{1/2}\frac{L^2}{J}\right)X^{O(\eta)}\\
 &\ll_\varepsilon L^3X^\varepsilon.
\end{aligned}
 \tag{180.A16}
\]

Finally the short physical correction is paid once:

\[
 B_{\rm short}
 =\sum_{\substack{0<r<R_0\\2\mid r}}
 r\left(\frac1{R_0}-\frac1M\right)A_r,
 \qquad |B_{\rm short}|\le R_0D_L
 \ll_\varepsilon L^3X^\varepsilon.
 \tag{180.A17}
\]

Equations (180.A14)--(180.A17) verify the stated implication from
(180.G) to \(Q_M^*\ll L^3X^\varepsilon\), without deleting the ordinary
zero sector or paying the short sector more than once. Without (180.G),
Fejer positivity gives only

\[
 Q_M^*\le M\cdot\frac12\sum_\epsilon
 \|Z_{\epsilon,*}\|_2^2
 \ll_\varepsilon L^4X^\varepsilon.
 \tag{180.A18}
\]

The lower endpoint is independently target-safe:

\[
 0\le Q_{R_0}^*\le R_0\cdot\frac12\sum_\epsilon
 \|Z_{\epsilon,*}\|_2^2
 \ll_\varepsilon L^3X^\varepsilon.
\]

Thus the restored powers are

| scale | target | coefficient-uniform positive capacity |
|---|---:|---:|
| one near cell | \(LX^\varepsilon\) | \(L^2X^\varepsilon\) |
| Fejer endpoint | \(L^3X^\varepsilon\) | \(L^4X^\varepsilon\) |

### 3.4 Sharp false controls

Choose \(\asymp L\) odd rows \(d\asymp L\) and \(\asymp L\) cofactors
\(m\asymp L\) of one fixed parity in a sufficiently narrow product box,
so all \(A\asymp L^2\) incidences lie in one \(M\)-site interval. The
row length is \(O(L)\) and the incidence energy is \(A\asymp L^2\).

For the complex dechirped control, set on this box

\[
 \lambda_{dm}^{\rm cx}(d)=\chi_4(d)e(-J\sqrt{dm}).
\]

Then the complete outer character and square-root phase cancel, and both
parity branches differ only by a global sign. On a fixed subinterval of
\(I_0\) of length \(\asymp1/M\), all product frequencies lie in a fixed
arc, so

\[
 \mathcal E_0^{\rm cx}\gg A^2/M\asymp L^2,
 \qquad \mathcal D_0^{\rm cx}\ll L.
 \tag{180.A19}
\]

This is intentionally complex and therefore nonliteral.

For a real control, write \(\phi_{dm}=2\pi J\sqrt{dm}\) and set

\[
 \lambda_{dm}^{(\alpha)}(d)
 =\chi_4(d)\cos(\phi_{dm}-\alpha).
\]

If

\[
 A(\theta)=\sum_{d,m}e(dm\theta),\qquad
 B(\theta)=\sum_{d,m}e(2J\sqrt{dm}+dm\theta),
\]

then, up to the harmless global parity sign,

\[
 Z^{(\alpha)}(\theta)
 =\frac12\{e^{i\alpha}A(\theta)+e^{-i\alpha}B(\theta)\}.
\]

Averaging over \(\alpha\) gives

\[
 \frac1{2\pi}\int_0^{2\pi}|Z^{(\alpha)}(\theta)|^2\,d\alpha
 =\frac14\{|A(\theta)|^2+|B(\theta)|^2\}.
\]

After integrating over \(I_0\), some \(\alpha\) therefore satisfies

\[
 \mathcal E_0^{(\alpha)}\gg L^2,
 \qquad \mathcal D_0^{(\alpha)}\ll L.
 \tag{180.A20}
\]

So realness and a cosine relation to the actual chirp do not supply the
missing \(L^{-1}\).

There is also an arbitrary-sign control. Choose

\[
 s_{dm}=\operatorname{sgn}\cos(\phi_{dm}-\alpha),\qquad
 \lambda_{dm}^{\rm sign}(d)=\chi_4(d)s_{dm}.
\]

For some \(\alpha\),

\[
 \Re\left(e^{-i\alpha}\sum_{d,m}s_{dm}e^{i\phi_{dm}}\right)
 =\sum_{d,m}|\cos(\phi_{dm}-\alpha)|\ge\frac2\pi A.
\]

The product diameter is \(O(M)\), so this lower bound persists, with a
smaller absolute constant, on a subinterval of length \(\asymp1/M\).
Thus again \(\mathcal E_0^{\rm sign}\gg L^2\) and
\(\mathcal G_0^{\rm sign}\gg L^2\) after subtracting (180.A2).
On the same aligned subinterval \(F_M(\theta)\asymp M\), so the complex,
real-cosine, and sign shadows also attain endpoint order
\(M L^2\asymp L^4\).

These three controls remain after replacing \(\chi_4\) by a constant or
erasing the selector, because the row sign can absorb the displayed
character. They can also be placed on constant-character
\(d\equiv1\pmod4\) shadow rows. In the literal algebra, an allowed
no-pair row whose odd prime factors are all \(1\pmod4\) has
\(\chi_4(d)=+1\) on every surviving divisor. This disproves any formal
rowwise mean-zero identity, but it is not a density claim and gives no
literal lower mass.

At \(\nu=0\), a simultaneous positive transform of the smooth product
phase has the same rank-one product collar as the Round-162 kernel; row
Gramization does not alter its null radial direction. Uniformity includes
this cell, so nondegenerate two-variable stationary phase cannot be
asserted uniformly. This is only a no-repeat check, not a second use of
the product-collar closure.

## 4. First doubtful or unproved step

The first unproved step is exactly the literal estimate

\[
\boxed{
 \mathcal G_\nu-\mathcal P_\nu
 \ll_\varepsilon LX^\varepsilon
 \quad\text{uniformly for }|\nu|\le\lceil\sqrt L\rceil,}
 \tag{180.A21}
\]

with the left side given, without abbreviation, by (180.A10).
Equivalently, by (180.A1)--(180.A4), it is the complete local scalar
theorem

\[
 \mathcal E_\nu\ll_\varepsilon LX^\varepsilon.
 \tag{180.A22}
\]

No accepted relation gives an \(L^{-1}\) contraction for (180.A10).
Specifically, no proved identity correlates the selected/no-pair field,
squarefree/coprimality projectors, two-adic branch, literal profile and
hard boundary values simultaneously with the square-root and cell-centre
phases across distinct divisor rows. Product collisions are safe but do
not control the nonzero near-collision complement. Fixed-shift grouping
returns to the existing signed shifted-divisor correlation; positive
row/cell closure has capacity \(L^2\); character Poisson at \(\nu=0\)
returns to the rank-one product collar. The complex, real-cosine, and
arbitrary-sign controls show that any proposed step which does not use a
strictly more specific literal relation is false.

This report neither proves nor disproves (180.G). It isolates the first
exact self-return and capacity barrier at the row-Gram interface.

## 5. Required control test and outcome

| Control | Exact test | Outcome |
|---|---|---|
| divisor-row identity | expanded the fully recombined \(Z_\epsilon\) and separated only \(d=d'\) after the one outer real part | **PASS**: (180.A1), (180.A8) |
| sinc kernel and wraparound | lifted each half-open modulo-one cell and integrated every integer product difference | **PASS**: exact (180.A7), including \(\nu=0\) wrap |
| both parity branches | averaged \((-1)^{\epsilon(m-m')}\) exactly | **PASS**: both same-parity branches retained; only mixed parity vanishes |
| literal incidence energy | used the literal incidence count and pointwise profile bound | **PASS**: \(\Lambda_2\ll L^2X^\varepsilon\) in (180.A5) |
| row length and physical diagonal | retained all cofactors, hard values, and row cross-products | **PASS**: \(O(L)\) row length gives \(\mathcal D_\nu\ll LX^\varepsilon\) |
| no premature modulus | kept the complete \(d<d'\) sum in one real part through (180.A10) | **PASS**; moduli appear only for the isolated safe collision or diagnostic controls |
| exact product diagonal | evaluated \(dm=d'm'\), including multiplicities and parity | **PASS**: exact (180.A9), \(\mathcal P_\nu\ll X^\varepsilon\) |
| near collisions | retained every \(0<\lvert dm-d'm'\rvert<M\) with its sinc and centre phase | **PASS**: exact complement (180.A10) |
| selector/squarefree/coprime/two-adic/profile/endpoints/zero extension | treated \(\lambda_N(d)\) as the complete literal atom and used no smoothing deletion | **PASS**; the unknown complement remains literal |
| complex dechirped | tested the same row length and incidence-energy interface after exact dechirping | **FAIL as a proof mechanism**: local off-row size is \(\asymp L^2\), not \(L\) |
| real cosine dechirped | averaged the exact cosine control over its phase \(\alpha\) | **FAIL as a proof mechanism**: some real control has local size \(\gg L^2\) |
| arbitrary real signs | aligned signs with one real projection of the chirp | **FAIL as a proof mechanism**: the \(L^2\) capacity persists |
| constant-character and erased-selector shadows | absorbed \(\chi_4\) into row signs and set the Boolean selector to one | **FAIL as proof mechanisms**: neither feature-insensitive argument contracts |
| all-\(1\bmod4\) no-pair row | evaluated the literal row character on such a permitted row | **PASS warning**: it is constant \(+1\); no rowwise orthogonality identity exists, with no density or lower-mass claim |
| one row | set all other rows to zero | **PASS**: \(\mathcal G_\nu=0\); an isolated positive transformed term would be incomplete |
| one site and exact collision | retained one incidence, then all divisor incidences over one product | **PASS**: one incidence gives zero off-row form; multiple incidences give exactly (180.A9) and are target-safe |
| hard boundaries | used half-open support and full-line zero extension throughout | **PASS**: no boundary was smoothed away; an interior theorem would leave an exact complement |
| rank-one product collar | checked the central cell \(\nu=0\) before any positive transform | **SELF-RETURN**: it is the accepted rank-one collar, with no new saving |
| fixed-shift check | grouped the exact complement by even \(h\) | **SELF-RETURN**: (180.A11)--(180.A12) reconstruct the unresolved signed shifted correlation; shiftwise absolute values are forbidden |
| local/endpoint powers | restored exact \(M\asymp L^2\), Parseval, ordinary zero, and short correction | **PASS**: \(L,L^2,L^3,L^4\) ledger verified in (180.A13)--(180.A18) |
| physical versus dual diagonal | separated only the physical \(d=d'\) block | **PASS**: no fixed dual diagonal was deleted |
| owner and exponent quarantine | traced only the K26 endpoint implication | **PASS**: no K17a, other owner, bridge, theorem, or exponent conclusion |

No numerical experiment was run. The controls are exact finite algebraic
tests. The dechirped and shadow arrays falsify coefficient-uniform
mechanisms only; none is asserted to occur with literal selector density.

## 6. Dependencies and exact artifacts used

Only the task-permitted files were used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round180_m2_hard_top_t1_residual_k26_near_peak_row_gram_strategy.md` (repaired Round-180 version);
- `proofs/kernels/m9_m2_hard_top_t1_residual_whole_chain_scale_coboundary_positive_capacity_obstruction.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md`;
- `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md`;
- `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/reviews/dependency_power_selection_seam_review.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/synthesis.md`; and
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k26-near-peak-row-gram-anticoncentration-gate/briefs/literal_near_peak_row_gram_attack.md`.

The authoritative graph hash was verified as the campaign hash. No web
source, external theorem, numerical evidence, sibling report, or excluded
artifact was used. No shared state, proof draft, validation matrix,
synthesis, kernel, strategy, or control file was edited.

## 7. Recommended state effect

**Recommendation: promote.**

Promote only the narrowly scoped lemma
`row_gram_offdiagonal_capacity_or_self_return_no_go`: the complete local
off-row theorem is target-strength equivalent, after its proved
\(O(LX^\varepsilon)\) physical row diagonal, to the full local scalar
energy theorem; the exact product diagonal is \(O(X^\varepsilon)\); and
coefficient-uniform row positivity has sharp local \(L^2\) and endpoint
\(L^4\) capacities, including complex, real-cosine, and arbitrary-sign
controls. This parks row orthogonality, rowwise positivity, shiftwise
absolute values, and a repeated product-collar transform unless a new
literal selector/phase relation is first proved.

Keep (180.G), K26, the residual scalar, complete \(t=1\), all other
hard-TOP channels, hard TOP, BAL, UNBAL, M9--M2, both M1 routes, GAR,
endpoint uniformity, M9, both bridges, the quarter theorem, and every
exponent unchanged. Do not infer literal lower mass from any false
control.
