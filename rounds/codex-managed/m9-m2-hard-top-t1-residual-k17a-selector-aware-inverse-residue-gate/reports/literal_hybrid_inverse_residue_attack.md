# 1. Result

**Campaign.** m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate  
**Task.** literal_hybrid_inverse_residue_attack  
**Role.** discovery  
**Starting graph.** e3927f0ace0f3d74e9e9f5116a319159e3508838c7f7bd14b086fa851cad82b8

Put

\[
 g=(u,n),\qquad u_0={u\over g},\qquad n_0={n\over g}.
\tag{177.A1}
\]

The primitive modulus of the inverse-residue anchor is $u_0$, not $u$.
After the exact $u$-alias folding, put

\[
 h=(\ell,u_0),\qquad q={u_0\over h}
 \quad(\ell\bmod u_0),
\tag{177.A2}
\]

with $q=1$ when $\ell=0$. Thus $q$ is the reduced conductor of an
individual additive inverse-residue alias. For fixed $B>0$, set

\[
 Q_B=(\log(2X))^B.
\tag{177.A3}
\]

The complete exact Fourier subaggregate of the frozen low-cross-gcd
complement whose aliases have reduced conductor $q\leq Q_B$ is
target-safe:

\[
\boxed{
 \left|
 \mathfrak C^{\rm rem}_{\rm low\text{-}\kappa,\,
 {\rm alias\text{-}cond}\leq Q_B}
 \right|
 \ll_{B,\delta,\gamma,\varepsilon}L^2X^\varepsilon .}
\tag{177.A4}
\]

The notation in (177.A4) means the exact decomposition (177.A18) below,
with all physical atoms and both orientations retained, restricted only
after the exact DFT to $u_0/(\ell,u_0)\leq Q_B$. Its exact remaining
Fourier complement inside the Round-177 target is

\[
 \kappa_*<\delta L,\qquad
 {u_0\over(\ell,u_0)}>Q_B.
\tag{177.A5}
\]

This is an owner-complete strict Fourier sector. It contains, as a
corollary, the entire physical primitive-modulus sector
$u/(u,n)\leq Q_B$, because every alias of such a stratum has reduced
conductor at most $Q_B$.

Two exact identities drive the proof. First, if
$c_m(k)=\widehat E_m(k)/m$, then for $u=gu_0$,

\[
\boxed{
 \sum_{j=0}^{g-1}c_u(\ell+ju_0)=c_{u_0}(\ell)
 \qquad(\ell\bmod u_0).}
\tag{177.A6}
\]

Thus the $g$ original aliases in one class modulo $u_0$ fold without a
factor $g$. Second, if $h=(\ell,u_0)$, $q=u_0/h$, and
$\ell=ha$ with $(a,q)=1$, then

\[
\boxed{
 c_{u_0}(ha)={q\over u_0}c_q(a),\qquad
 \sum_{\substack{\ell\bmod u_0\\u_0/(\ell,u_0)=q}}
 |c_{u_0}(\ell)|
 \ll {q\over u_0}\log(2q).}
\tag{177.A7}
\]

For fixed $(\kappa,u,u_0)$ the literal $v,n,t$ capacity is
$O(u_0L)$. Equation (177.A7) therefore lowers the
coefficient-weighted positive capacity of the reduced-conductor-$q$
aliases to

\[
 \boxed{O\!\left(Lq\log(2q)\right).}
\tag{177.A8}
\]

Writing $u=gu_0=ghq$, summing $g,h$, then $q\leq Q_B$, and finally
$\kappa$ costs only fixed powers of logarithms, proving (177.A4).

The complete target is not proved. In the complementary range
$q>Q_B$, (177.A8) still requires essentially a full factor $q$, naturally
two coupled square-root gains. The exact alias $TT^*$ identity is merely
residue-class energy and does not provide either gain by itself. The
first unavailable input is a contraction for that energy with the actual
selector-dependent, phase-dependent, two-orientation amplitude. This is
not a literal lower bound and leaves a genuinely selector-aware signed
theorem unexcluded.

# 2. Exact statement and hypotheses

Assume

\[
 J=\sqrt X,\qquad 1\ll L\ll H\leq J^{1/2},\qquad
 R_0=\lceil L\rceil,
\tag{177.A9}
\]

fix $0<\delta<1/2$ and $0<\gamma<1$, and set

\[
 R_{\log}=\min\{R_0-1,\lfloor(\log X)^{100}\rfloor\}.
\tag{177.A10}
\]

For every supported endpoint $N=dm\asymp L^2$, retain

\[
 u_L(d,m)=\chi_4(d)\lambda_N(d)e(J\sqrt N),\qquad
 \lambda_N(d)=\omega_L(N)\rho_N(d)A_N(d).
\tag{177.A11}
\]

Here $\omega_L$ contains the normalized half-open shell and squarefree
projector; $A_N$ contains both parity branches, all profiles, floors,
stars, hard values, endpoints, and full-line zero extension; and
$\rho_N$ is exactly the canonical neither/both selector, with
$\rho_N=1$ on a no-pair row. No density, variation, or Fourier estimate
for the selected/no-pair field is assumed. On nonzero atoms,
$|\lambda_N(d)|\ll1$.

Use the exact two orientations from the accepted Round-176 kernel. In the
plus orientation,

\[
 d=\kappa u,\quad d'=\kappa u+2s_t,\quad
 m'=\kappa v,\quad m=\kappa v+2w_t,\quad
 s_tv-w_tu=n,
\tag{177.A12}
\]

where $\kappa,u$ are odd, $(u,v)=1$, and

\[
 s_t=[\bar v n]_u+ut,\qquad
 w_t={[\bar v n]_uv-n\over u}+vt.
\tag{177.A13}
\]

In the minus orientation the inward factors are again
$\kappa u,\kappa v$, now $uw_t-s_tv=n$, with

\[
 s_t=[-\bar v n]_u+ut,\qquad
 w_t={n+[-\bar v n]_uv\over u}+vt.
\tag{177.A14}
\]

In both cases $r=2\kappa n$, the parametrization is multiplicity one, and
on every nonzero squarefree atom

\[
 (d,d')=(u,n),\qquad
 \chi_4(d')\chi_4(d)=E_u(\pm\bar v n)(-1)^t.
\tag{177.A15}
\]

The amplitudes $\Lambda^\pm_{\kappa,u,v,n}(t)$ and phases
$\Psi^\pm_{\kappa,u,v,n}(t)$ are exactly those in
(176.K17)--(176.K20). They retain the Fejer factor,
$R_{\log}<2\kappa n<R_0$, $(u,n)<\gamma L$,
$s_t,w_t\geq1$, both endpoint coefficients with their correct
conjugations, and every zero-extended field in (177.A11). Literal support
gives, with fixed support constants,

\[
 u\asymp U,\qquad v\asymp U,\qquad n\ll U,\qquad
 U={L\over\kappa},\qquad
 \#\{t:\Lambda^\pm(t)\ne0\}\ll1+\kappa.
\tag{177.A16}
\]

For $u_0\mid u$, put $g=u/u_0$. In the stratum $(u,n)=g$, write
$n=gn_0$, so $(n_0,u_0)=1$. Define the complete primitive
two-orientation alias block

\[
\begin{aligned}
 \mathcal H_{\kappa,u,u_0,\ell}
 :=\sum_{\substack{v\asymp U\\(u,v)=1}}
 \sum_{\substack{n=gn_0\ll U\\(n_0,u_0)=1}}
 \sum_{t\in\mathbb Z}\Bigg\{&
 \Lambda^+_{\kappa,u,v,n}(t)
 e\!\left(\Psi^+_{\kappa,u,v,n}(t)+{t\over2}
       +{\ell\bar v n_0\over u_0}\right)\\
 &+\Lambda^-_{\kappa,u,v,n}(t)
 e\!\left(\Psi^-_{\kappa,u,v,n}(t)+{t\over2}
       -{\ell\bar v n_0\over u_0}\right)\Bigg\}.
\end{aligned}
\tag{177.A17}
\]

All displayed ranges in (177.A17) mean the exact literal zero-extended
support, not a rectangular replacement; $\bar v$ in the last phases is
reduced modulo $u_0$. The exact primitive-conductor decomposition is

\[
\boxed{
 \Re\mathfrak C^{\rm rem}_{\rm low\text{-}\kappa}
 =\Re\sum_{\substack{\kappa<\delta L\\\kappa\ {\rm odd}}}
 \sum_{u\asymp U}\sum_{u_0\mid u}
 \sum_{\ell\bmod u_0}c_{u_0}(\ell)
 \mathcal H_{\kappa,u,u_0,\ell}.}
\tag{177.A18}
\]

For $\ell=ha$, $h=(\ell,u_0)$, $q=u_0/h$, the phase in
(177.A17) reduces exactly to

\[
 e\!\left(\pm{a\bar v n_0\over q}\right),
\tag{177.A19}
\]

and the coefficient is (177.A7). Equation (177.A4) is the restriction of
(177.A18) to $q\leq Q_B$.

For the remaining $q>Q_B$ aliases, a sufficient local theorem is

\[
\boxed{
 \sum_{\substack{u_0\mid u\\
                  \ell\bmod u_0\\
                  u_0/(\ell,u_0)>Q_B}}
 c_{u_0}(\ell)\mathcal H_{\kappa,u,u_0,\ell}
 \ll_{\varepsilon} L X^\varepsilon}
\tag{177.A20}
\]

uniformly in supported $(\kappa,u)$, with both orientations already
combined. A stronger reduced-aliaswise form would give, for every
$u_0\mid u$ and $\ell$ of reduced conductor $q$,

\[
 |\mathcal H_{\kappa,u,u_0,\ell}|
 \ll_\varepsilon {u_0\over q}L X^\varepsilon.
\tag{177.A21}
\]

Indeed, multiplying (177.A21) by the conductor-$q$ coefficient mass in
(177.A7) gives $O(L\log(2q))$ per $(u_0,q)$, after which divisor and
logarithmic losses are absorbable. Both (177.A20) and (177.A21) keep the
literal selector and are unproved.

# 3. Proof or derivation

## Primitive-modulus folding

Let $u=gu_0$, $n=gn_0$, $(n_0,u_0)=1$. Since $u$ and $g$ are odd and
$v$ is invertible modulo $u$,

\[
 [\pm\bar v n]_u
 =g[\pm\bar v n_0]_{u_0}.
\tag{177.A22}
\]

Taking parity gives

\[
 E_u(\pm\bar v n)=E_{u_0}(\pm\bar v n_0).
\tag{177.A23}
\]

For $a\bmod u_0$, expansion at the original modulus gives

\[
\begin{aligned}
 E_u(ga)
 &=\sum_{k\bmod u}c_u(k)e(ka/u_0)\\
 &=\sum_{\ell\bmod u_0}
 \left\{\sum_{j=0}^{g-1}c_u(\ell+ju_0)\right\}
 e(\ell a/u_0).
\end{aligned}
\tag{177.A24}
\]

By (177.A23) this is $E_{u_0}(a)$. Uniqueness of Fourier coefficients
modulo $u_0$ proves (177.A6). Applying the identity pointwise in every
gcd stratum of the exact Round-176 two-orientation formula proves
(177.A18). No incomplete interval, endpoint, or selector is changed, and
the $g$ original aliases are combined before absolute values.

## Reduced alias conductor and coefficient mass

Let $h=(\ell,u_0)$ and $q=u_0/h$. For $q>1$, write
$\ell=ha$ with $a\bmod q$ and $(a,q)=1$; for $q=1$ take the unique
zero alias. Directly from

\[
 c_m(k)={2\over m\{1+e(-k/m)\}}
\tag{177.A25}
\]

one obtains, with no phase or sign loss,

\[
 c_{u_0}(ha)
 ={2\over u_0\{1+e(-a/q)\}}
 ={q\over u_0}c_q(a).
\tag{177.A26}
\]

The accepted normalized Fourier bound
$\sum_{a\bmod q}|c_q(a)|\ll\log(2q)$ then gives (177.A7), even after
restricting $a$ to reduced residues. In particular,

\[
 c_{u_0}(0)={1\over u_0}.
\tag{177.A27}
\]

If $\ell=(u_0\pm1)/2$, then $(\ell,u_0)=1$, so $q=u_0$ and
$|c_{u_0}(\ell)|\asymp1$. Thus every constant-size near-half alias lies
in the large reduced-conductor complement whenever $u_0>Q_B$.

## Literal raw capacity

Fix $\kappa,u,u_0$, put $U=L/\kappa$, and let $g=u/u_0$. Every
permitted determinant in this stratum is

\[
 n=gn_0={u\over u_0}n_0,\qquad
 (n_0,u_0)=1,\qquad n\ll U.
\tag{177.A28}
\]

Since $u\asymp U$,

\[
 n_0\ll {Uu_0\over u}\ll u_0,
\tag{177.A29}
\]

so there are $O(u_0)$ possible determinants. There are $O(U)$ possible
$v$ and, for each $v,n$ in either orientation, $O(1+\kappa)$ possible
fibre sites. Hence

\[
 \#\{\text{literal candidate atoms at fixed }\kappa,u,u_0\}
 \ll u_0U(1+\kappa)\ll u_0L.
\tag{177.A30}
\]

The Fejer factor and endpoint coefficients are bounded. Squarefreeness,
both parity branches, the selected/no-pair field, the original-gcd cutoff,
strict opposing inequalities, hard faces, endpoints, and zero extension
only delete or downweight atoms. Thus (177.A30) is an absolute bound for
the complete complex two-orientation block. Multiplication by (177.A7)
proves the weighted capacity (177.A8).

## Summation of low reduced conductors

For a reduced conductor $q$, write $u_0=hq$ and $u=gu_0=ghq$.
At fixed $\kappa,q$, supported $u\asymp U$ arise from

\[
 gh\asymp {U\over q}.
\tag{177.A31}
\]

The elementary divisor-hyperbola count gives

\[
 \#\{(g,h):gh\asymp U/q\}
 \ll \left(1+{U\over q}\right)\log(2U)
 \ll {U\over q}\log(2U)
\tag{177.A32}
\]

for every supported $q$, because support itself gives $q\leq u_0\ll U$
and hence $U/q\gg1$ up to fixed endpoint constants. Combining
(177.A8) and (177.A32) yields, for fixed
$\kappa,q$,

\[
 \ll Lq\log(2q)\,{U\over q}\log(2U)
 \ll LU\log(2q)\log(2U).
\tag{177.A33}
\]

Summing $q\leq Q_B$ and then $\kappa<\delta L$ gives

\[
\begin{aligned}
 \left|\mathfrak C^{\rm rem}_{\rm low\text{-}\kappa,\,
 {\rm alias\text{-}cond}\leq Q_B}\right|
 &\ll LQ_B\log(2Q_B)
 \sum_{\kappa<\delta L}{L\over\kappa}
 \log\!\left(2+{L\over\kappa}\right)\\
 &\ll L^2Q_B\log(2Q_B)\{\log(2L)\}^2.
\end{aligned}
\tag{177.A34}
\]

All parity and divisibility conditions only reduce the tuples counted.
Since $L\leq X^{1/4}$ and $B$ is fixed, the last line is
$O_{B,\varepsilon}(L^2X^\varepsilon)$. This proves (177.A4).

The complete restored ledger is

\[
\begin{array}{c|c}
 \text{level}&\text{positive capacity}\\ \hline
 (\kappa,u,u_0)&
 u_0\cdot U\cdot(1+\kappa)\ll u_0L\\
 (\kappa,u,u_0,q)\text{ after coefficient mass}&
 (q/u_0)\log(2q)\cdot u_0L\ll Lq\log(2q)\\
 (\kappa,q),\ u=ghq\asymp U&
 \ll LU\log(2q)\log(2U)\\
 q\leq Q_B,\ \kappa<\delta L&
 \ll L^2Q_B\log(2Q_B)\{\log(2L)\}^2.
\end{array}
\tag{177.A35}
\]

## Exact alias energy and the live $q$-saving

For fixed $\kappa,u,u_0$, index every plus and minus atom in
(177.A17) by $z$, and put

\[
 A_z=\Lambda_z e(\Psi_z+t_z/2),\qquad
 b_z=\begin{cases}
  \bar v n_0\pmod {u_0},&z\text{ plus},\\
  -\bar v n_0\pmod {u_0},&z\text{ minus}.
 \end{cases}
\tag{177.A36}
\]

Then

\[
 \mathcal H_{\kappa,u,u_0,\ell}
 =\sum_zA_ze(\ell b_z/u_0),
\tag{177.A37}
\]

and Fourier orthogonality gives the exact $TT^*$ ledger

\[
\boxed{
 \sum_{\ell\bmod u_0}|\mathcal H_{\kappa,u,u_0,\ell}|^2
 =u_0\sum_{b\bmod u_0}
 \left|\sum_{z:b_z=b}A_z\right|^2.}
\tag{177.A38}
\]

Both orientations occur inside the same class sums. On expansion, the
diagonal is $u_0\sum_z|A_z|^2$, while the off-diagonal is the complete
set of same-residue pairs, including cross-orientation pairs. Alias
Parseval therefore turns the problem into actual residue-class energy; it
does not contract that energy.

For a fixed reduced alias $\ell=ha$, (177.A37) is

\[
 \mathcal H_{\kappa,u,u_0,ha}
 =\sum_zA_ze(ab_z/q).
\tag{177.A39}
\]

The phase sees only $b_z\bmod q$, while the literal amplitude still
varies over the $h=u_0/q$ lifts. A coefficient-blind completion cannot
identify those lifts. The positive coefficient-weighted capacity
remaining after their exact normalization is (177.A8), namely
$Lq\log(2q)$. A single square-root saving in the inverse-$v$ or
determinant direction leaves $L\sqrt q$ up to logarithms; the target
needs a second coupled square-root saving or an equivalent signed energy
contraction.

Finally, exact Fourier inversion says

\[
 \sum_{\ell\bmod u_0}c_{u_0}(\ell)
 \mathcal H_{\kappa,u,u_0,\ell}
 =\sum_zA_zE_{u_0}(b_z).
\tag{177.A40}
\]

Thus the full alias packet reconstructs the physical anchor rather than
averaging it away. A bounded diagnostic array can saturate this identity:
$A_z=E_{u_0}(b_z)$ makes every term on the right positive. Likewise,
choosing an array dechirped against (177.A39) saturates an individual
large-conductor alias. These controls refute coefficient-uniform
contraction from support and Fourier norms alone; they are not literal
coefficients and assert no K17a lower mass.

# 4. First doubtful or unproved step

The first unproved step is a target-strength estimate for the actual
literal reduced-conductor blocks with
$q>(\log(2X))^B$, such as (177.A20) or (177.A21).

The exact algebra has already paid the original gcd multiplicity, folded
all $u$-aliases, retained the zero and imprimitive aliases, and normalized
the $h=u_0/q$ conductor lifts. The remaining positive capacity is
$Lq\log(2q)$ per $(\kappa,u,u_0,q)$, not $Lu_0$. The missing gain is
therefore exactly $q$ up to a logarithm.

The first unsupported step in a reciprocal large-sieve or $TT^*$ proof
would be to assert cancellation among the class sums in (177.A38) or
(177.A39) after treating

\[
 A_z=\Lambda_z e(\Psi_z+t_z/2)
\tag{177.A41}
\]

as a smooth, factorable, or residue-periodic coefficient. As
$v,n_0,t$ vary, both endpoint products vary, the canonically selected
prime pair can switch, a row can switch between selected and no-pair
status, and either endpoint coefficient can vanish. The permitted
hypotheses give no bounded variation, Fourier norm, factorization, or
correlation estimate for this field in
$b_z=\pm\bar v n_0\bmod q$.

The literal $v$-interval is incomplete. Squarefree openings create odd
progressions but do not make the selector periodic. The plus and minus
orientations have different endpoint products and conjugations, so no
exact identity forces their class sums to cancel. The square-root phase
also does not presently supply the second square-root: the accepted
stationary-mode audit shows that fibrewise completion followed by
absolute dual recombination returns the fibre length, while no supplied
joint modulo-one separation controls the remaining $v,n_0$ modes.

A new selector-aware, phase-aware, two-orientation theorem could still
provide the $q$-saving. The result is therefore the strict alias sector
(177.A4) and the exact next seam above, not a global no-go.

# 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| literal_residual_coefficient | **Pass.** Equations (177.A11), (177.A17), and (177.A36) retain $\omega_L\rho_NA_N$ at both endpoints. No selector or profile is erased. |
| exact_low_cross_gcd_complement | **Pass.** The proof stays inside exactly $\kappa_*<\delta L$. It removes the exact DFT sector $q\leq Q_B$ and leaves precisely (177.A5). |
| both_opposing_orientations | **Pass.** Both signs, endpoint orders, phases, and conjugations occur in (177.A17) and in the same residue classes of (177.A38), before every absolute value. |
| anchor_DFT_and_near_half_alias | **Pass.** Equation (177.A6) folds the original DFT exactly. The near-half aliases are primitive, have $q=u_0$ and constant coefficient, and remain in the open complement when $u_0>Q_B$. |
| hybrid_v_n_t_capacity | **Pass.** Fixed $(\kappa,u,u_0)$ has $O(U)$ values of $v$, $O(u_0)$ determinants, and $O(1+\kappa)$ fibre sites, hence $O(u_0L)$. After exact alias mass the restored capacity is $O(Lq\log(2q))$. |
| primitive_modulus_and_gcd_multiplicity | **Pass.** The primitive modulus is $u_0=u/(u,n)$. Equation (177.A6) removes a false factor $g$, while (177.A31)--(177.A34) restore all $g,h$ multiplicities. |
| k_zero_and_imprimitive_aliases | **Pass.** The zero alias is the $q=1$ term $c_{u_0}(0)=1/u_0$ and is included. Every imprimitive alias is classified by its exact $q=u_0/(\ell,u_0)$; none is discarded. |
| incomplete_v_interval | **Pass for the proved sector; open analytically outside it.** The literal interval is counted as $O(U)$ without completion. No complete-period orthogonality is asserted for large $q$. |
| large_sieve_diagonal_offdiagonal | **Pass as an exact audit.** Equation (177.A38) displays the full diagonal and every same-residue off-diagonal, including cross-orientation pairs. It proves alias-energy self-return absent a new literal class-sum theorem. |
| squarefree_Mobius_progressions | **Pass.** The squarefree projectors remain unopened, so no positive Möbius recombination or progression multiplicity is hidden. Opening them would only partition the atoms already counted. |
| parity_and_two_adic_branches | **Pass.** $u,g,u_0,h,q$ are odd, exactly as required for the parity identity. The odd and squarefree even-even branches, including their restrictions on $v,n,w$, are both retained and only reduce the count. |
| selected_and_no_pair_rows | **Pass for (177.A4); first open seam for cancellation.** Both no-pair rows and literal selected neither/both rows are counted. No density or cancellation between them is assumed. |
| short_cross_gcd_fibres | **Pass.** The uniform $O(1+\kappa)$ count includes $\kappa=O(1)$, where $t$ supplies no long sum. The low-$q$ alias sector remains target-safe. |
| stationary_and_dechirped_modes | **Pass in scope.** The proof of (177.A4) takes the physical phase absolutely. The accepted stationary self-return remains live for large $q$; dechirped arrays are used only as nonliteral coefficient-class controls. |
| endpoints_and_zero_extension | **Pass.** Hard values, endpoint conjugations, displacement inequalities, and zero extension remain inside $\Lambda^\pm$ and introduce no completion boundary term. |
| false_coefficient_controls | **Quarantined.** The arrays following (177.A40) show only that support, DFT norms, and coefficient-blind $TT^*$ cannot force the $q$-saving. They are not literal K17a arrays or physical lower mass. |
| residual_only_owner_scope | **Pass.** Only a strict Fourier sector of the low-$\kappa_*$ K17a residual is closed. Complete K17a and every parent remain open. |
| no_in_round_pivot | **Pass.** The report stays on the frozen selector-aware inverse-residue mechanism and its exact conductor strata. |

No numerical experiment, symbolic computation, web source, or external
theorem was used. The allocation was 100 percent analytical/algebraic.

# 6. Dependencies and exact artifacts used

The argument used exactly the permitted context:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/round177_m2_hard_top_t1_residual_k17a_selector_aware_inverse_residue_strategy.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_k17a_cross_gcd_alternating_fibre_reduction.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md;
- proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/reports/literal_cross_gcd_alternating_fibre_attack.md; and
- rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/reviews/final_kernel_mathematical_review.md.

No sibling Round-177 report, candidate, review, control, synthesis, web
source, or unlisted research artifact was used.

# 7. Recommended state effect

**Recommended effect: promote the exact alias-folding identity (177.A6),
the reduced-conductor coefficient identity (177.A7), the exact
decomposition (177.A18), and the owner-complete strict alias sector
(177.A4); retain complete K17a and every parent open.**

The promoted sector should be recorded with its exact Fourier complement
$u_0/(\ell,u_0)>(\log(2X))^B$ inside $\kappa_*<\delta L$. The whole
physical primitive-modulus sector $u/(u,n)\leq(\log(2X))^B$ follows as a
corollary. The next live estimate is the literal reduced-conductor
$q$-saving (177.A20), equivalently a signed two-orientation residue-class
energy contraction beyond (177.A38).

The appropriate terminal label is
strict_k17a_low_cross_gcd_selector_aware_sector. Full K17a, the complete
residual scalar, full displayed $t=1$, every other hard-TOP channel, hard
TOP, BAL, UNBAL, M9--M2, M9--M1/GAR, endpoint uniformity, M9, both
bridges, the quarter theorem, and every global exponent remain open.
