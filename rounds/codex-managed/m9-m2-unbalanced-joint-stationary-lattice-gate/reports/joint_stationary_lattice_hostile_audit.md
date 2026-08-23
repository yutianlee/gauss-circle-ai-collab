# Hostile audit: joint stationary lattice, selector seam, and norm scope

Campaign: `m9-m2-unbalanced-joint-stationary-lattice-gate`
Round: 124
Role: hostile seam reviewer
Starting graph SHA-256:
`2b60eca238542d4f321a19c90f20163c6dd4cd7c60da6f324910b6db10b638c6`

## 1. Result

The strict-interior algebra in the derivation packet and in
`candidates/conductor_stationary_lattice_involution.md` is substantially
correct, but it does **not** give a transform of the Round-123 near-alias
survivor and it does **not** prove a complete stationary involution or a
norm obstruction.

More precisely:

1. The two character-Poisson signs, the positive odd modes $p,q$, the
   saddles, the Gaussian units, the scalar amplitudes, (124.C15), and the
   Hessian determinant and amplitude (124.C17)--(124.C18) all pass in the
   stated strict-interior, selector-free chart.  For the Fourier kernel
   $e(\Theta-jk-dh)$, the sign in (124.C15) is correct.
   Moreover, for the full **unmasked** flat-smooth row, the first
   character-Poisson/B-process may be performed before the block square:
   its transformed block square differs from the original full
   correlation by (O(1)).  This stronger full-Gram identity still does
   not transport the near-alias mask.
2. The product defect
   $\mathcal N=p(k+h)-qk$ is not the primal alias defect.  The missing
   exact relation at the first two saddles is

$$
     E_*(j)=M(s_*-r_*)-jr_*s_*
           =r_*s_*\{\partial_k\Theta-j\}.
     \tag{124.H1}
$$

   Thus the nonexact near-alias condition is a thin collar about the
   integer-gradient manifolds, whereas a simultaneous $k$-saddle lies
   on $E_*(j)=0$.  Product equality $\mathcal N=0$ is only the much
   smaller set $p=q,h=0$.
3. The fatal seam occurs before the proposed dual-sector analysis.  The
   indicator selecting $j\ne0$, $E\ne0$, and
   $|E|\le X^{1+\rho}/L$ couples $r$ and $s$, has alias-boundary and
   defect-boundary jumps, and is absent from the rowwise Poisson formula.
   It cannot be passed through two independent scalar Poisson/stationary
   transforms by evaluating it at $(r_*,s_*)$.  If instead one
   transforms the full Gram and subtracts the already-safe physical
   packages later, the transforms of those packages spread through all
   $p,q,k,h,d,j$ sectors.  Hence no displayed dual sector is presently
   identified with the required survivor.
4. The nominal strict-interior unsigned capacities $D^2$ for the full
   second stationary lattice and $D^2/L$ for its formal $p=q$ part can
   be reproduced.  They are legitimate **capacity diagnostics**.  They
   are not lower bounds.  In particular, $D^2/L$ has not been shown to
   be the unavoidable positive diagonal of an exact sufficient norm for
   the near-alias-restricted sum.  Calling it a norm obstruction is
   overclaimed.
5. The only target-safe dual diagonal presently certified from the
   principal chart is $p=q,h=0$, counted once under ordered-pair
   conjugation; its absolute principal mass is
   $O(X^{1/2})$.  This is not the complete transformed diagonal, does not
   contain all zero aliases, and supplies no bound for the equal-mode
   shifted or unequal-mode sectors.

Accordingly, the maximal safe result is a strict-interior
principal-symbol chart and a scoped selector-free phase-return no-go.  No
strictly smaller **complete signed** survivor is rigorously obtained.  The
smallest complete survivor remains exactly the Round-123 physical
$V_{M,H_0}$, with both characters, all ordered conjugates, both alias
orientations, the nonzero nonexact near-alias selector, shifted profiles,
zero extension, and endpoint modules retained.

## 2. Exact statement and hypotheses

Let $e(x)=\exp(2\pi i x)$.  Let $X\to\infty$, let
$M\asymp X$ be an integer while every physical amplitude remains frozen
at $X$, and put

$$
 D=X^\delta,\qquad L=X^\ell,\qquad R=X/D,\qquad
 K=XL/D^2,
$$

with

$$
 \frac14\le\delta<\frac12,\qquad
 0\le\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463.
$$

Let $H=H_0=\lceil X^{1/2}/D\rceil$.  Then, for fixed exponents,

$$
 H\sim X^{1/2}/D\longrightarrow\infty,\qquad
 K\sim LH^2,\qquad H/K\longrightarrow0,
 \tag{124.H2}
$$

and

$$
 \frac{DH}{K}\sim\frac{D^2}{X^{1/2}L}\longrightarrow\infty.
 \tag{124.H3}
$$

The conclusions below concerning stationary formulas are restricted to a
fixed nonempty common interior on which

$$
 k,k+h\asymp K,\qquad p,q\asymp L,qquad |h|<H,
 \tag{124.H4}
$$

all transported profiles have the derivative bounds required by ordinary
stationary phase, and no physical alias, profile, block, or support
boundary is crossed.  They do not include a claim about the sum of the
omitted cells or remainders.

Under (124.H2)--(124.H4), the following is the maximal safe theorem.

**Strict-interior stationary-chart lemma.**  After applying ordinary
Poisson summation separately to the two *unrestricted* character rows,
every positive interior $r$-saddle is indexed uniquely by a positive
odd $p$, every positive interior $s$-saddle is indexed uniquely by a
positive odd $q$, and their principal phase and coefficient are

$$
 \Theta_{p,q,h}(k)
 =\sqrt M\{\sqrt{p(k+h)}-\sqrt{qk}\},
 \tag{124.H5}
$$

$$
 \chi_4(p)\chi_4(q)
 \frac{M^{1/2}}
 {(k+h)^{3/4}k^{3/4}p^{3/4}q^{3/4}},
 \tag{124.H6}
$$

before the transported literal profiles and the exact outer Fejer factor
are inserted.  Equivalently, (124.H6) is (124.C3) times (124.C4).
Equations (124.C5)--(124.C14) and (124.C17)--(124.C18) are exact on this
chart.  For the second Poisson convention $e(\Theta-jk-dh)$,
(124.C15) and (124.C16) are exact.

If $j$ is the nearest reciprocal alias at the first saddles, then
(124.H1) is exact.  Hence

$$
 |E_*|\le \frac{X^{1+\rho}}L
 \quad\Longrightarrow\quad
 |\partial_k\Theta-j|\ll \frac{X^\rho}{K},
 \tag{124.H7}
$$

because $r_*s_*\asymp R^2$.  Formula (124.H7) is only the stationary
chart of the selector; it is not an identity transporting the discrete
physical indicator through Poisson summation.

The ordered-pair involution

$$
 (p,q,h,k)\longmapsto(q,p,-h,k+h)
 \tag{124.H8}
$$

conjugates the principal summand, sends
$(\Theta,\mathcal N)$ to $(-\Theta,-\mathcal N)$, and sends the
corresponding $(j,E)$ orientation to $(-j,-E)$.  Its strict-interior
fixed set is $p=q,h=0$, which is counted once, not twice.  Conjugate
pairing proves reality only; it proves no cancellation.

There is also a safe unmasked row statement.  Write the full physical row

$$
 A(k)=\frac1k\sum_{r\ {\rm odd}}\chi_4(r)
 W\!\left(\frac{X}{rD}\right)
 q_L\!\left(\frac{4Xk}{r^2}\right)e(Mk/r),
$$

with its literal zero extension, and define its strict stationary
transform

$$
 \widetilde A(k)=c_+M^{1/4}k^{-3/4}
 \sum_{p>0\ {\rm odd}}\chi_4(p)p^{-3/4}
 W\!\left(\frac{X}{2D}\sqrt{\frac{p}{Mk}}\right)
 q_L((X/M)p)e(\sqrt{Mpk}),
 \tag{124.H9a}
$$

where $c_+=-ie(1/8)$, and every term is zero-extended exactly as in the
physical row.  For flat $C^\infty$ profiles with the inherited scaled
derivative bounds,

$$
 \mathcal F^{\rm full}_{M,H}
 =\frac{J+H-1}{H^2}\sum_{|h|<H}(H-|h|)
   \sum_k\widetilde A(k+h)\overline{\widetilde A(k)}+O(1).
 \tag{124.H9b}
$$

This is a formula for the full unmasked positive block square.  It is not
a formula for $V_{M,H}$, because insertion of the coupled $j,E$ selector
occurs only after the $r,s$ pair is formed.

## 3. Proof and hostile derivation

### 3.1 Character signs, saddles, Gaussian units, and amplitudes

The exact identity

$$
 \chi_4(n)=\frac{e(n/4)-e(-n/4)}{2i}
$$

gives

$$
 \sum_n\chi_4(n)F(n)
 =\frac1{2i}\sum_{\sigma=\pm1}\sigma
   \sum_{m\in\mathbb Z}\int_{\mathbb R}
   F(x)e(-(m-\sigma/4)x)\,dx.
 \tag{124.H9}
$$

On the $r$-leg write $A=M(k+h)>0$.  A positive saddle requires
$\mu=m-\sigma/4<0$.  With

$$
 p=-4\mu=-4m+\sigma,
$$

$p$ is positive odd, $\sigma=\chi_4(p)$, and the phase is
$A/r+pr/4$.  Its unique saddle, critical value, and curvature are

$$
 r_*=2\sqrt{A/p},\qquad
 \phi(r_*)=\sqrt{Ap},\qquad
 \phi''(r_*)=\frac{p^{3/2}}{4A^{1/2}}>0.
$$

With the $e(x)$ convention, its scalar stationary factor is

$$
 e(1/8)|\phi''(r_*)|^{-1/2}
 =2e(1/8)A^{1/4}p^{-3/4}.
$$

Including the character-Poisson coefficient gives

$$
 -i e(1/8)\chi_4(p)A^{1/4}p^{-3/4}.
 \tag{124.H10}
$$

On the $s$-leg, with $B=Mk>0$, a positive saddle requires
$\nu=n-\tau/4>0$.  Put $q=4\nu=4n-\tau$.  Then
$q$ is positive odd, $\chi_4(q)=-\tau$, and the phase is
(-B/s-qs/4).  The corresponding coefficient is

$$
 i e(-1/8)\chi_4(q)B^{1/4}q^{-3/4}.
 \tag{124.H11}
$$

The constants in (124.H10)--(124.H11) multiply to one.  Dividing by
$(k+h)k$ proves (124.H5)--(124.H6).  There is no missing factor two:
$p$ determines $(m,\sigma)$ uniquely and $q$ determines
$(n,\tau)$ uniquely.  At the saddles,

$$
 q_L(4X(k+h)/r_*^2)=q_L((X/M)p),\qquad
 q_L(4Xk/s_*^2)=q_L((X/M)q),
$$

but the $W$-profiles remain moving functions of $p/(k+h)$ and
$q/k$.  They may not be replaced by a rectangular $p,q,k$ box.

The same calculation also shows character persistence under a second
principal transform.  For example, stationary Poisson in the positive
$p$-phase uses the branch $r=4a-\eta>0$, with
$\eta=-\chi_4(r)$, saddle $p_*=4A/r^2$, Gaussian unit $e(-1/8)$,
and inverse Hessian factor (2p_*^{3/4}A^{-1/4}).  Multiplication with
(124.H10) returns exactly $\chi_4(r)e(A/r)$ and the original pulled-back
amplitude at principal-symbol level.  The quarter character restores the
inverse stationary branch; it does not give automatic alternation.

### 3.2 Product defect, alias defect, and multiplicity

Rationalizing (124.H5) proves

$$
 \Theta=\sqrt M\,
 \frac{\mathcal N}
 {\sqrt{p(k+h)}+\sqrt{qk}},\qquad
 \mathcal N=ph-(q-p)k.
$$

If $p\ne q$, oddness gives $|p-q|\ge2$.  In view of
$K/(LH)\asymp H\to\infty$, the term $(p-q)k$ dominates $ph$
uniformly on fixed interiors.  This proves (124.C7), for all sufficiently
large $X$, and then $\mathcal N=0$ is equivalent to $p=q,h=0$.
This is an asymptotic support assertion, not an all-$X$ identity without
the fixed-interior constants.

Differentiation gives

$$
 \partial_k\Theta=M(1/r_*-1/s_*).
$$

Multiplication by $r_*s_*$ proves (124.H1).  In particular, a
simultaneous $k$-stationary point with integer label $j$ has
$E_*(j)=0$, even when $\mathcal N\ne0$.  Thus exact-gradient
manifolds run through equal-mode shifted and unequal-mode sectors.  They
are not counted by the product diagonal.

The $k$-gradient is strictly monotone on a sufficiently large fixed
interior except on $p=q,h=0$.  Indeed,

$$
 \partial_k^2\Theta
 =\frac{\sqrt M}{4}
 \left(\frac{\sqrt q}{k^{3/2}}
       -\frac{\sqrt p}{(k+h)^{3/2}}\right).
 \tag{124.H12}
$$

For $p\ne q$, the relative contribution of $p-q$, at least
$\asymp1/L$, dominates the $h/k=O(H/K)=o(1/L)$ perturbation.  For
$p=q,h\ne0$, (124.H12) has the sign of $h$.  Hence a fixed
$(p,q,h,j)$ has at most one strict-interior $k$-saddle.  Alias ties,
profile entries and exits, and endpoint saddles are not covered by this
one-count.

### 3.3 Fourier sign, Hessian, and exact scope of the return

Set

$$
 d=\partial_h\Theta=\frac{\sqrt{Mp}}{2\sqrt{k+h}},\qquad
 d-j=\frac{\sqrt{Mq}}{2\sqrt k}.
$$

Then

$$
 \sqrt{Mp(k+h)}=2d(k+h),\qquad
 \sqrt{Mqk}=2(d-j)k.
$$

Therefore

$$
 \Theta=2(dh+jk),
$$

and, for the Fourier phase $\Theta-jk-dh$,

$$
 \Theta-jk-dh=jk+dh.
$$

This independently verifies the sign in (124.C15).  It is also Euler's
identity for a function homogeneous of degree $1/2$ in $(k,h)$.
Moreover

$$
 jk+dh=d(k+h)-(d-j)k
       =\frac{M(k+h)}{r_*}-\frac{Mk}{s_*},
$$

so the returned phase is the primal phase at the ideal continuous
selectors.  This is a Legendre-phase identity.  It is not yet Fourier
inversion of the literal operator: the transported profiles, the
triangular Fejer cusp, all support boundaries, the discrete selector, and
all error terms are still absent.

Writing

$$
 a=\frac{\sqrt{Mp}}{4(k+h)^{3/2}},\qquad
 b=\frac{\sqrt{Mq}}{4k^{3/2}},
$$

the $(k,h)$-Hessian is

$$
 \begin{pmatrix} b-a&-a\\-a&-a\end{pmatrix}.
$$

Consequently

$$
 \det\nabla^2_{k,h}\Theta=-ab
 =-\frac{M\sqrt{pq}}
 {16(k+h)^{3/2}k^{3/2}},
$$

which proves (124.C17).  Its signature is zero, so the two-dimensional
Gaussian unit is (1), and its unit-lattice stationary amplitude is
exactly (124.C18).  Multiplication by (124.C4) gives $16/(pq)$, and
including (124.C3) gives

$$
 \frac{4\chi_4(p)\chi_4(q)}{pq}.
 \tag{124.H13}
$$

Thus the determinant and scalar amplitude pass.  Hessian rank alone does
not provide an estimate: it measures a locally invertible phase map and
does not control the signed sum over its lattice image.

The inverse critical equations are unique:

$$
 k=\frac{Mq}{4(d-j)^2},\qquad
 h=\frac{Mp}{4d^2}-\frac{Mq}{4(d-j)^2}.
 \tag{124.H14}
$$

Together with the unique quarter-channel indexing, (124.H14) establishes
multiplicity one for a strict positive stationary branch.  Ordered-pair
conjugation still supplies the distinct partner (124.H8), except on its
fixed diagonal.

### 3.4 Diagonal and capacity ledgers

For $p=q,h=0$, the principal profile product is a modulus square and
the phase is zero.  Restoring the $h=0$ Fejer weight and the outer
factor gives, for bounded literal profiles,

$$
 \begin{aligned}
 \mathcal D_{\rm prin}
 &\ll \frac KH M^{1/2}
   \sum_{p\asymp L}p^{-3/2}
   \sum_{k\asymp K}k^{-3/2}\\
 &\ll M^{1/2}\frac{K^{1/2}}{HL^{1/2}}
 \asymp X^{1/2}.
 \end{aligned}
 \tag{124.H15}
$$

This validates the nominal diagonal scale and the one-count convention,
but only for the strict-interior principal term.

The advertised later capacities can also be reconstructed as unsigned
principal-symbol ledgers.  From (124.H14), for fixed $p,q,d$,

$$
 \left|\frac{\partial h}{\partial j}\right|
 =\frac{Mq}{2(d-j)^3}\asymp\frac KD.
 \tag{124.H16}
$$

Since $DH/K\to\infty$, a nonempty interior $j$-strip contains many
integer labels, and its Fejer-weighted mass is nominally

$$
 \sum_j(H-|h(d,j)|)_+
 \asymp \frac DK H^2.
 \tag{124.H17}
$$

The exact outer factor is asymptotic to $K/H^2$, so (124.H17) costs
$\asymp D$ for each $p,q,d$.  There are $\asymp D$ admissible
$d$'s.  Using (124.H13),

$$
 D^2\sum_{p,q\asymp L}\frac1{pq}\asymp D^2,
 \tag{124.H18}
$$

whereas formally retaining only $p=q$ gives

$$
 D^2\sum_{p\asymp L}\frac1{p^2}\asymp\frac{D^2}{L}.
 \tag{124.H19}
$$

Thus the arithmetic behind the $D^2$ and $D^2/L$ ledgers is
meaningful on a fixed principal core.  Also

$$
 \frac{D^2/L}{X^{1/2}}
 =X^{2\delta-\ell-1/2}\longrightarrow\infty,
$$

because $\ell<\delta-1/4$.

What fails is the inference from (124.H19) to a no-go theorem.  It is an
absolute coefficient capacity, not an evaluated signed contribution.
The $p=q,h\ne0$ summands are shifted autocorrelations rather than
termwise modulus squares; after the $(k,h)$ transform their phases and
moving profiles remain.  Even when a complete $p$-row block energy is
nonnegative, its off-zero-shift correlations can cancel its $h=0$
term, and no lower bound of order $D^2/L$ has been proved.  After the
physical near-alias restriction, positivity is lost altogether.  No exact
sufficient norm, diagonal readback, or lower bound has been supplied.
Therefore (124.H18)--(124.H19) may diagnose the cost of an unsigned
treatment, but they do not show that every joint signed inequality or
every positive norm is overstrong.

## 4. First doubtful or unproved step

The first unproved step is **not** the Fourier sign in (124.C15) and is
**not** the Hessian calculation.  It occurs before (124.C1), when the
complete Round-123 near-alias survivor is treated as though its two
character rows could be Poisson transformed independently without its
selector.

Writing the physical selector schematically as

$$
 \mathbf 1_{\mathcal V}(r,s)
 =\mathbf1_{\{j(r,s)\ne0\}}
  \mathbf1_{\{E(r,s)\ne0\}}
  \mathbf1_{\{|E(r,s)|\le X^{1+\rho}/L\}},
$$

the amplitude in the required sum is
(F_{k,h}(r,s)\mathbf1_{\mathcal V}(r,s)), not a product of an
(r)-row and an (s)-row.  Its nearest-alias boundaries, exact-defect
excision, and near-defect edges are coupled curves.  Multiplication by
this selector becomes convolution and boundary terms after Poisson; it
does not become pointwise restriction by
(\partial_k\Theta\) or (mathcal N).

There are only two lawful options, neither completed here:

1. retain a specified smooth/half-open realization of the coupled
   selector inside a genuine two-variable (r,s) transform and price all
   boundary modules; or
2. transform the full correlation and separately transform or otherwise
   control the already-safe (j=0), (E=0), and far-tail packages before
   identifying the difference.

In option 2, their dual transforms are not confined to the product
diagonal or any displayed (p,q,d,j) sector.  A target bound for the full
transformed correlation would still suffice, but none is proved; a
capacity obstruction for the full correlation would not by itself be an
obstruction for its near-alias difference.

The next unproved seam is the complete endpoint and aggregate error
ledger: negative/nonstationary quarter modes, profile entries and exits,
the (q_L) and (W) transition zones, zero extension in (k) and
(k+h), the cusp at (h=0), the Fejer endpoints, nearest-alias ties,
the exact-defect deletion, and every stationary-boundary transition.
Until those are summed at (O(X^{1/2+\varepsilon})), the local Legendre
return cannot be called a complete transform involution.

## 5. Control tests and outcomes

No numerical experiment was used.  Every control was algebraic or
analytic.

| Required control or seam | Verdict | Hostile outcome |
|---|---:|---|
| `literal_Round123_near_alias_survivor` | **FAIL** | (124.D1) is the full Gram.  The coupled (j\ne0,E\ne0,|E|\)-selector is absent from the independent row transforms, and no lawful subtraction in dual variables is supplied. |
| `H0_K_normalization` | **PASS, asymptotic** | (H_0\sim X^{1/2}/D\), (K\sim LH_0^2), (H_0/K\to0), and (DH_0/K\to\infty).  Ceilings preclude treating these as exact equalities. |
| `double_character_Poisson_signs` | **PASS, selector-free** | The Fourier convention, (p=-4m+\sigma), (q=4n-\tau), (chi_4(p)=\sigma), (chi_4(q)=-\tau), and the coefficient (-\sigma\tau/4) are correct. |
| `stationary_points_and_Gaussian_units` | **PASS, strict interior** | (124.C1), curvatures, (e(1/8)), (e(-1/8)), and (124.C4) are correct.  This does not pass the missing aggregate transition/error theorem. |
| Fourier sign in (124.C15) | **PASS** | For (e(\Theta-jk-dh)), (Theta=2(jk+dh)), hence (Theta-jk-dh=jk+dh), the original ideal-selector phase. |
| Hessian determinant and amplitude | **PASS, strict interior** | The determinant is (-M\sqrt{pq}/(16(k+h)^{3/2}k^{3/2})), signature zero, and inverse square-root amplitude is (124.C18). |
| `dual_product_defect` | **PASS, repaired scope** | (124.C5)--(124.C7) hold on fixed interiors for large (X).  They classify product equality only, not alias defect. |
| `dual_gradient_to_primal_alias` | **PASS with required repair** | (124.C8) is exact.  The report adds (E_*=r_*s_*(\Theta_k-j)); this shows why every exact (k)-saddle lies on the continuous exact-alias manifold. |
| `dual_diagonal_one_count` | **PASS only for the principal fixed set** | (p=q,h=0) is fixed by ordered conjugation and has principal mass (O(X^{1/2})).  It is not the complete dual image of all physical (j=0) pairs. |
| `equal_mode_shifted_sector` | **FAIL as an estimate** | The scale (D|h|/K), its nonzero alias crossings, and (\mathcal N=p h\) are correct.  No signed aggregate, endpoint theorem, or lawful near-alias restriction is proved. |
| `unequal_mode_sector` | **FAIL as an estimate** | The scale (D|p-q|/L\gg1) and strict-interior one-saddle multiplicity are correct.  The complete actual-sign sum over its many aliases is untouched. |
| `mode_shift_alias_multiplicity` | **FAIL globally** | Positive (p,q) quarter channels and strict interior ((p,q,d,j)\leftrightarrow(k,h)) saddles have multiplicity one, with conjugate orbits of size two.  Alias ties, selector boundaries, endpoints, and transition modes have no ledger. |
| `character_persistence` | **PASS, principal chart** | The dual coefficient is (chi_4(p)chi_4(q)); a second stationary character transform restores the primal character rather than cancelling it. |
| `stationary_endpoint_and_error_ledger` | **FAIL** | No uniform expansion or summed error is given for nonstationary modes, moving profiles, zero extension, Fejer cusp/endpoints, saddle entry/exit, or selector boundaries. |
| (D^2) and (D^2/L) capacities | **PASS only as unsigned diagnostics** | (124.H18)--(124.H19) follow from the principal gradient-image and Fejer ledger.  They are neither signed lower bounds nor an exact near-alias norm diagonal. |
| `signed_joint_aggregation` | **FAIL** | Conjugate pairing gives (2\Re), not cancellation.  No inequality controls the complete actual-sign (p,q,h,j) aggregate before an outside norm. |
| `transform_involution_and_norm_scope` | **FAIL globally; PASS locally** | The local Legendre phase and principal one-leg character maps self-return.  The literal operator, selector, profiles, endpoints, and errors have not been inverted, and no universal overstrong-norm theorem follows from capacity. |
| `owner_and_downstream_scope` | **PASS for this audit** | Every accepted formula above is restricted to a flat-smooth strict-UNBAL principal interior.  No implication to nonflat UNBAL, hard TOP, BAL, M9-M2, M9, the quarter theorem, or an exponent is asserted. |

The controls therefore falsify any claim that the complete near-alias
transform or its target estimate has been established.  They do not
falsify the possibility of a genuinely joint signed inequality.

## 6. Dependencies and exact artifacts used

This audit used only the assigned context and the additional untrusted
candidate explicitly sent by the conductor:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/conductor_0821_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-unbalanced-reciprocal-gram-factorization-gate/reviews/hostile_alias_curve_no_go_audit.md`;
- `rounds/codex-managed/m9-m2-dual-square-actual-symbol-transfer/reviews/conductor_round106_dual_character_stationarity.md`;
- `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reviews/conductor_round117_involution_product_and_source.md`;
- `rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/candidates/conductor_stationary_lattice_involution.md`;
- `rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/briefs/joint_stationary_lattice_hostile_audit.md`.

No Round-124 sibling report, web source, external theorem, or numerical
experiment was used.  The exact stationary calculations were reproduced
algebraically rather than accepted from the candidate.

## 7. Recommended state effect

**Recommendation: revise the candidate; no proof-state change.**

Retain as candidate evidence only the exact strict-interior formulas for
the two character saddles, (124.C5)--(124.C14), the corrected alias-defect
identity (124.H1), the sign in (124.C15), (124.C16)--(124.C18), the
ordered-conjugation map, and the diagnostic capacities
(D^2,D^2/L).  Rename the conclusion a **principal-phase return**, not a
complete stationary involution or a norm obstruction.

Reject the following inferences:

- that independent rowwise Poisson transforms represent the
  near-alias-restricted (V_{M,H_0});
- that (mathcal N=0) classifies the live alias or defect diagonal;
- that (p=q) after the second transform is a termwise positive
  (D^2/L) lower bound;
- that the (D^2/L) capacity rules out every admissible joint norm;
- that local Hessian nondegeneracy supplies a saving or a complete
  self-return;
- that either the equal-mode shifted or unequal-mode sector is now
  target-safe.

No strictly smaller complete signed survivor is available.  Keep the
Round-123 (V_{M,H_0}) unchanged as the smallest live object and keep
`M9-M2-smooth-unbalanced-three-quarter-estimate` open.  Even a future
flat-smooth closure would not close sharp, starred, clipped, hard,
arithmetic-owner, or transition UNBAL packages, hard TOP, BAL, M9-M2,
M9, endpoint uniformity, the quarter theorem, or any global exponent.
