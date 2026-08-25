# Round 147 discovery report: exact shifted Voronoi and the squarefree (H)-resonance gate

## 1. Result

**Result: exact compact-smooth reduction, followed by a rigorous no-go for the presently available termwise menu.**  At graph SHA-256

```text
1dc79cf41e0dea8888341e944c5d0bf025d87f22cfaa282da34fcd10eecd04f5
```

the mandatory (t=1) coefficient admits a direct level-four shifted Voronoi formula for every (C_c^infty(0,infty)) test.  This formula follows from the completed functional equation of

\[
F_z(w)=\zeta(w+z)L(w-z,\chi _4)
\]

and therefore avoids the analytic-test mismatch in the previously audited theorem cards at the level of the identity.  If (H(w,z)=\sum h_z(k)k^{-w}) is the exact squarefree correction, the resulting identity retains the whole (H)-convolution, its single polar term, and the reflected coefficient.  Its exact Mellin-Barnes kernel fixes the conductor-four resonance at

\[
m=kN+O\!\left(k\sqrt{N/M}\right),
\]

not at (kN/4).

There is also a stronger exact Euler factorization.  For imaginary (z),

\[
H(w,z)=
\frac{\mathscr K(w,z)}
{\zeta(2w+2z)\zeta(2w-2z)L(2w,\chi _4)},
\qquad \Re w>\frac13,
\tag{147.1}
\]

as a meromorphic continuation, where \(\mathscr K\) is absolutely convergent in that half-plane.  This repair has the exact two-adic factor

\[
\mathscr K_2(w,z)=(1-2^{-2w+2z})^{-1}.
\tag{147.2}
\]

It does not supply a fixed power saving: a contour shift a fixed distance left of \(\Re w=1/2\) would have to cross possible poles coming from zeros of the three denominator functions.  Known zero-free information gives only a height-dependent shrinking strip, and no cancellation of those possible poles with \(\mathscr K\) has been proved.

Granting the still-unproved uniform analysis of the exact kernel, the strongest termwise primal/dual estimate for one powerful index (k) is

\[
\min\!\left(\frac{M^{1/4}}k,\frac R{\sqrt M}\right).
\tag{147.3}
\]

Summing this over powerful (k) gives

\[
\ll X^\varepsilon
\begin{cases}
M^{1/4},&M\le R^{4/3},\\
R^{1/2}M^{-1/8},&R^{4/3}\le M\le R^2.
\end{cases}
\tag{147.4}
\]

The excess over the weighted target (O(X^\varepsilon)) is (R^{1/3}) at (M=R^{4/3}) and (R^{1/4}) at (M=R^2).  A new bare reciprocal-phase lemma does meet the top-scale capacity before squarefreeness is imposed, but the first literal expansion of \(\mu^2(d)\) already loses (D^{1/2}) on a (d\asymp D) block.  Equivalently, the (H)-convolution produces one target-sized moving band per powerful index.  Disjointness of those bands does not create scalar orthogonality.

Accordingly, this report establishes the method label

\[
\mathsf{squarefree\_H\_resonance\_no\_go}
\]

for any proof that uses only fixed-index Voronoi, absolute values over the (H)-indices, the bare reciprocal-phase divisor count, or the inverse-(L) contour shift.  This is not a lower bound for the actual signed sum.  The (t=1) target, a strict owner-complete top range, (M9\!-!M1), and every downstream exponent claim remain open.

## 2. Exact statement and hypotheses

Let (R=X^{1/4}), (N=\lfloor X\rfloor\), (M\le B_M\le2M\), and let (M\le U\le B_M) be an inherited half-open prefix.  The exact face is

\[
S^{(1)}_{M,N}(U)=
\sum_{\substack{M\le de<U\\
\mu^2(de)=1, e\ {\rm odd}, e>4d}}
(de)^{-3/4}V_{\rm low}(R^2de/N)\chi _4(e)e(+\sqrt{Nde}).
\tag{147.5}
\]

Its weighted target is (S^{(1)}_{M,N}(U)\ll X^\varepsilon); equivalently, the corresponding unweighted prefix target is (M^{3/4}X^\varepsilon).

For (|\Re z|<1/4), define

\[
A_z(n)=\sum_{de=n}\chi _4(e)(e/d)^z,
\qquad
B_z(n)=\mu^2(n)A_z(n).
\tag{147.6}
\]

Then

\[
\sum_{n\ge1}A_z(n)n^{-w}=F_z(w)=\zeta(w+z)L(w-z,\chi _4),
\tag{147.7}
\]

and

\[
\sum_{n\ge1}B_z(n)n^{-w}=H(w,z)F_z(w),
\qquad B_z=h_z*A_z.
\tag{147.8}
\]

Let (f\in C_c^\infty(0,\infty)), with Mellin transform

\[
\widehat f(w)=\int_0^\infty f(x)x^{w-1}\,dx.
\]

Put

\[
\begin{aligned}
\mathcal C_z(w)={}&
\pi^{-(w+z)/2}\Gamma\!\left(\frac{w+z}{2}\right)
\left(\frac4\pi\right)^{(w-z+1)/2}
\Gamma\!\left(\frac{w-z+1}{2}\right),\\
\mathcal G_z(w)={}&\frac{\mathcal C_{-z}(1-w)}{\mathcal C_z(w)}\\
={}&2^{1-2w+2z}\pi^{2w-1}
\frac{\Gamma((1-w-z)/2)\Gamma((2-w+z)/2)}
{\Gamma((w+z)/2)\Gamma((w-z+1)/2)},
\end{aligned}
\tag{147.9}
\]

and, on any sufficiently far left vertical line avoiding gamma poles,

\[
(\mathcal V_zf)(y)=\frac1{2\pi i}
\int_{(-a)}\mathcal G_z(w)\widehat f(w)y^{w-1}\,dw.
\tag{147.10}
\]

The exact compact-smooth shifted formula is

\[
\boxed{
\sum_{n\ge1}A_z(n)f(n)
=L(1-2z,\chi _4)\widehat f(1-z)
+\sum_{m\ge1}A_{-z}(m)(\mathcal V_zf)(m).}
\tag{147.11}
\]

The exact (H)-convolution formula is

\[
\boxed{
\begin{aligned}
\sum_{n\ge1}B_z(n)f(n)
={}&L(1-2z,\chi _4)H(1-z,z)\widehat f(1-z)\\
&+\sum_{k\ge1}\frac{h_z(k)}k
\sum_{m\ge1}A_{-z}(m)(\mathcal V_zf)(m/k).
\end{aligned}}
\tag{147.12}
\]

For a test supported on (x\asymp M), only (k\ll M) is physically active before transformation.  For larger (k), the polar and dual terms in (147.12) cancel exactly; they must not be estimated as new physical resonances.

The strict cone is inserted by Perron in the ratio (e/(4d)): its mode is (4^{-z}B_z(n)).  A hard cutoff on a boundary block (d\asymp D), (e\asymp4D), needs height \(\gg D\).  The accepted target-safe alternative removes the collar \(|e-4d|\le\sqrt D\) and uses a smooth ratio transform with

\[
|\Im z|\lesssim D^{1/2}X^\varepsilon.
\tag{147.13}
\]

Formula (147.12) is an exact identity.  The hypotheses not proved here are the estimates, uniform in (147.13), for the oscillatory decomposition of (147.10), the clipped-prefix interpolation, and the ensuing signed (k)-correlation.

## 3. Proof and derivation

### 3.1 Cone coefficient and character sectors

Write (s=2^\nu n), \(\nu\in\{0,1\}\), with (n) odd and squarefree.  Since the prime (2) is forced into (d), direct substitution gives

\[
C(2^\nu n)=
\sum_{\substack{e\mid n\\e>2^{1+\nu/2}\sqrt n}}\chi _4(e).
\tag{147.14}
\]

Let (c_\nu=2^{1+\nu/2}) and

\[
\mathcal B_\nu(n)=
\sum_{\substack{e\mid n\\c_\nu^{-1}\sqrt n<e<c_\nu\sqrt n}}
\chi _4(e).
\]

The boundary equalities cannot occur because (e^2) is odd while (2^{\nu+2}n) is even.  Pairing (e\) with (n/e) gives the exact identity

\[
\sum_{e\mid n}\chi _4(e)
=(1+\chi _4(n))C(2^\nu n)+\mathcal B_\nu(n).
\tag{147.15}
\]

Thus the \(\chi _4(n)=+1\) sector is complete coefficient minus a mandatory central band, whereas the \(\chi _4(n)=-1\) sector has vanishing complete coefficient and survives as an antisymmetric pair of tails.  In particular,

\[
C(p)=\chi _4(p)\quad(p>4),
\qquad C(2p)=\chi _4(p)\quad(p>8),
\tag{147.16}
\]

for odd primes (p), while (C(1)=C(2)=0).  Neither the negative-character tail nor the even sector can be removed by the complete (A_0) model.

### 3.2 Euler product, the (p=2) audit, and the stronger continuation

Before the cone,

\[
\sum_{d,e\ge1}
\frac{\mu^2(de)\mathbf1_{e\ {\rm odd}}\chi _4(e)}
{d^{w+z}e^{w-z}}
=(1+2^{-w-z})
\prod_{p\ {\rm odd}}(1+a_p+b_p),
\tag{147.17}
\]

where

\[
a_p=p^{-w-z},\qquad b_p=\chi _4(p)p^{-w+z}.
\]

Removing the local factors of (F_z) gives

\[
H_2=1-2^{-2w-2z},
\qquad
H_p=(1+a_p+b_p)(1-a_p)(1-b_p)
=1-a_p^2-b_p^2-a_pb_p+a_p^2b_p+a_pb_p^2.
\tag{147.18}
\]

This proves absolute convergence of (H) for \(\Re(w\pm z)>1/2\), and shows that (h_z(k)) is supported on powerful integers.  For imaginary (z), \(|h_z(k)|\ll_\varepsilon k^\varepsilon\).

For odd (p), factor one step further:

\[
H_p=(1-a_p^2)(1-b_p^2)(1-a_pb_p)\mathscr K_p,
\tag{147.19}
\]

where direct formal division gives

\[
\mathscr K_p=1+a_p^2b_p+a_pb_p^2
+O((|a_p|+|b_p|)^4).
\tag{147.20}
\]

Consequently \(\prod_{p\ {\rm odd}}\mathscr K_p\) is absolutely convergent for imaginary (z) and \(\Re w>1/3\).  More generally it converges when both \(\Re(w+z)\) and \(\Re(w-z)\) exceed (1/3).  Multiplying the odd-prime factors in (147.19) gives two incomplete zeta products and one complete (L)-product.  The factor (H_2=1-2^{-2w-2z}) cancels the first missing two-adic zeta factor and leaves exactly (147.2).  This proves (147.1), including all signs and the two-adic normalization.

The refinement is not a lawful fixed-power contour shortcut.  A shift to \(\Re w=1/2-\delta\) meets possible poles at zeros of \(\zeta(2w\pm2z)\) and (L(2w,\chi _4)\).  For fixed \(\delta>0\), excluding such zeros uniformly in the growing imaginary range would require a fixed zero-free strip next to \(\Re s=1\).  No such input is available.  The displayed algebra does not prove that \(\mathscr K\) cancels any of these zeros, so a contour cannot cross them silently.

### 3.3 Direct compact-smooth functional equation

The completed factors of both \(\zeta\) and (L(s,\chi _4)\) have root number (+1).  Therefore

\[
\mathcal C_z(w)F_z(w)=\mathcal C_{-z}(1-w)F_{-z}(1-w).
\tag{147.21}
\]

Mellin inversion starts on \(\Re w>1+|\Re z|\).  Shifting to a sufficiently far left line crosses only the pole of \(\zeta(w+z)\) at (w=1-z), with residue

\[
L(1-2z,\chi _4)\widehat f(1-z).
\]

On the new line, use (147.21), expand (F_{-z}(1-w)\), and interchange the rapidly convergent sum and integral.  This proves (147.11) with the exact gamma quotient (147.9).  In particular, no second polar term is present because \(\chi _4\) is nonprincipal.

Now expand (B_z=h_z*A_z) and apply (147.11) to (f(k\cdot)\).  Since

\[
\widehat{f(k\cdot)}(w)=k^{-w}\widehat f(w),
\qquad
\mathcal V_z[f(k\cdot)](m)=k^{-1}(\mathcal V_zf)(m/k),
\tag{147.22}
\]

summing over (k) proves (147.12).  For \(0\le\Re z<1/4\), powerful support makes \(\sum_k|h_z(k)|k^{-1+\Re z}\) convergent.  This also justifies the canceling (k\)-tail beyond the physical support.

At each fixed (z), the Mellin-Barnes kernel (147.10) is the exact level-four (J/Y/K) package.  Its fixed-order oscillatory branches have phase

\[
e(\pm\sqrt{xy}),
\tag{147.23}
\]

because the conductor is (4), equivalently the Bessel argument is (2\pi\sqrt{xy}\).  Thus the negative branch against (e(+\sqrt{Nx})\) has phase (e((\sqrt N-\sqrt y)\sqrt x)\), proving the centre (y=N\).  The positive branch is nonstationary and the (K)-branch is decaying at large argument.  These fixed-order facts identify the geometry; a uniform derivation for growing \(|\Im z|\) is deliberately not asserted.

### 3.4 Polar, cone, and prefix boundaries

For

\[
f(x)=x^{-3/4}W_{M,U}(x)V_{\rm low}(R^2x/N)e(+\sqrt{Nx}),
\tag{147.24}
\]

the polar Mellin integral \(\widehat f(1-z)\) is nonstationary throughout (147.13).  Its radial oscillation scale is

\[
F=\sqrt{NM},
\]

whereas \(|z|^2\ll D X^\varepsilon\le\sqrt M X^\varepsilon\).  Repeated integration by parts makes the polar term target-safe for scale-smooth (W_{M,U}), including the factors (L(1-2z,\chi _4)H(1-z,z)\).

The hard Perron integral cannot be truncated at bounded height: the pair (e=4d+1) forces height \(\gg D\).  On a boundary box (e\asymp4d\), the collar \(|e-4d|\le L\) contains (O(D(L+1)X^\varepsilon)\) pairs.  Since (de\asymp D^2), its weighted cost is

\[
D^{-3/2}D(L+1)X^\varepsilon
\ll (L+1)D^{-1/2}X^\varepsilon.
\tag{147.25}
\]

Taking (L\asymp\sqrt D\) is target-safe and leads to (147.13).  It is an owned target-sized error, not a negligible one.

For a literal half-open prefix, one may choose a (C_c^\infty) interpolation agreeing with the indicator at every integer, so (147.12) remains an exact discrete identity.  Such a unit-scale terminal transition does not have the usual scale-(M) seminorms.  A uniform analysis of its transformed boundary contribution, or a maximal/partial-summation replacement that preserves the inherited profile, is still required.

### 3.5 Resonance, (R,M,k) ledger, and moving-band obstruction

On (x\asymp M), linearizing (147.23) gives

\[
|m/k-N|\ll\sqrt{N/M},
\qquad
m=kN+O\!\left(k\sqrt{N/M}\right).
\tag{147.26}
\]

After the physical factor (x^{-3/4}), one resonant dual term has size (R^{-1}k^{-1}).  The band has (O(k\sqrt{N/M})) terms, so its termwise dual price is

\[
\frac1{Rk}\,k\sqrt{N/M}=\frac R{\sqrt M}.
\tag{147.27}
\]

The primal trivial price for the same index is (M^{1/4}/k), proving (147.3).  The crossover is

\[
k_0=M^{3/4}/R.
\tag{147.28}
\]

Using \(\#\{k\le K:k\ {\rm powerful}\}\ll K^{1/2+\varepsilon}\), the indices below and above (k_0) both contribute (R^{1/2}M^{-1/8}X^\varepsilon) when (k_0\ge1); when (k_0<1), the convergent powerful sum of (1/k) gives (M^{1/4}X^\varepsilon).  This proves (147.4).

At the top (M=R^2), the (k)-bands have width (O(kR)), while adjacent centres are separated by (N\asymp R^4).  They are disjoint for every physically active (k\ll M\).  This does not imply cancellation in a single scalar: after summing over (m), all bands feed the same complex number, and Cauchy over disjoint supports still pays the number of bands.  At (m=kN) the archimedean phase cancels with the same Maslov phase for every (k); nearby offsets (j/(kR)) see essentially the same kernel profile.  Any saving must therefore come from a signed shifted correlation of the form

\[
\sum_{k\ {\rm powerful}}\frac{h_z(k)}k
\sum_{|j|\ll k\sqrt{N/M}}
A_{-z}(kN+j)\,\mathcal W_{k,z}(j),
\tag{147.29}
\]

not from support disjointness.

There is no independent random-sign heuristic at (z=0):

\[
(h_0*A_0)(n)=\mu^2(n)\sum_{e\mid n}\chi _4(e)
=\mu^2(n)\frac{r_2(n)}4\ge0.
\tag{147.30}
\]

The ratio transform has a zero-frequency/Perron component, so this recombination cannot be discarded.  Formula (147.29) is the first genuinely new arithmetic input required after uniform kernel analysis.

### 3.6 Bare reciprocal phase and the first squarefree loss

The one-sided (e)-transform on a box (d\asymp D\), (e\asymp E\), (DE\asymp M\), produces dual length

\[
Q\asymp \frac FE=D\sqrt{N/M},
\qquad D\le\sqrt M,
\tag{147.31}
\]

and the bare reciprocal phase (e(Nd/q)\).  Since (Q\le R^2\ll N\), the following elementary lemma applies:

\[
\sum_{q\asymp Q}\left|\sum_{d\asymp D}e(Nd/q)\right|
\ll_\varepsilon (Q+D)(NQ)^\varepsilon.
\tag{147.32}
\]

Indeed, write (j=N-aq), where (a) is the nearest integer to (N/q).  The inner geometric sum is \(\ll\min(D,q/|j|)\); (j=0) costs (D\tau(N)).  For (j\ne0), each admissible (q) divides (N-j).  Splitting (|j|) dyadically and using the divisor bound gives (O(Q(NQ)^\varepsilon)\).  The hypothesis (Q\ll N) is essential; without it the stated lemma would be false when (q\) is much larger than (N).

The required transformed bound is

\[
|\mathcal T_{D,Q}|\ll RD X^\varepsilon.
\tag{147.33}
\]

At (M=R^2), (Q=RD), so (147.32) exactly meets (147.33).  At smaller (M), its (Q)-term exceeds the target by (R/\sqrt M), reproducing the bare (R^{4/3}) barrier.

The lemma does not survive the literal coefficient by the same proof.  Squarefreeness of (d) alone gives

\[
\mu^2(d)=\sum_{a^2\mid d}\mu(a).
\]

Expanding and applying (147.32) to each (a) yields only

\[
\sum_{q\asymp Q}
\left|\sum_{d\asymp D}\mu^2(d)e(Nd/q)\right|
\ll_\varepsilon QD^{1/2}+D.
\tag{147.34}
\]

Truncating the (a)-sum at (A) does not repair this: the small-square part costs (AQ+D), while the large-square tail costs (QD/A), optimized at (A=D^{1/2}).  Thus the first exact loss occurs before expanding squarefreeness of (e), coprimality, or the cone.  Expanding those conditions puts (e) in progressions of modulus (L); the transformed (q)-range grows to (LQ) while stationary-phase amplitude falls by (L^{-1}), leaving another (Q)-sized contribution for each progression.  The (H)-convolution is the Euler-product packaging of precisely these signed powerful/progression indices.  Recovering (147.32) for the literal coefficient therefore requires joint Möbius/(H)-signed cancellation, not another triangle inequality.

For reference, the full power ledger is

| object | lawful price after the physical weight | ratio to target |
|---|---:|---:|
| primal, fixed powerful (k) | (M^{1/4}/k) | (M^{1/4}/k) |
| dual resonant band, fixed (k) | (R/\sqrt M) | (R/\sqrt M) |
| all powerful (k), (M\le R^{4/3}) | (M^{1/4+\varepsilon}) | same |
| all powerful (k), (R^{4/3}\le M\le R^2) | (R^{1/2+\varepsilon}M^{-1/8}) | same |
| bare reciprocal phase | (Q+D) before the final transform normalization | (Q/(RD)=R/\sqrt M) in (147.33) |
| squarefree-(d) reciprocal phase by Möbius triangle | (QD^{1/2}+D) | (R D^{1/2}/\sqrt M) |

The top balanced boundary box (M=R^2,D\asymp E\asymp R) therefore loses (R^{1/2}) in the direct squarefree reciprocal-phase expansion and (R^{1/4}) in the optimized powerful-convolution Voronoi split.  The latter is the stronger presently lawful menu, but it still misses the target.

## 4. First doubtful or unproved step

The **first doubtful analytic step** is a uniform oscillatory expansion, with derivatives, of the exact gamma kernel (147.10) for

\[
|\Im z|\lesssim D^{1/2}X^\varepsilon
\]

(or height (D) for an unrepaired hard Perron cutoff), simultaneously for the scale-smooth block and the inherited clipped prefix.  The exact functional equation proves the identity, but none of the permitted source audits supplies the required growing-complex-order (J/Y/K) estimates and unit-scale terminal-boundary ledger.  Formally the parameter is favorable, since the Bessel argument is (F=\sqrt{NM}) and \(|z|^2/F\ll R^{-2+\varepsilon}\) in the smoothed range, but that observation is not a proof.

Even if this first seam is granted, the **first missing power** is the signed correlation (147.29), equivalently a squarefree version of (147.32) that avoids (147.34).  The moving bands are phase-aligned at their centres, and (h_z) is not absolutely summable without its physical (1/k) or an additional saving.  No theorem in the permitted Round-141, Round-145, or Round-146 artifacts supplies this joint shifted-divisor/Möbius estimate.

Thus there is no strict owner-complete top-scale reduction: the polar and collar are controllable, but the exact prefix/kernel uniformity is unproved and, after granting it, the best full-(H) top estimate is still (R^{1/4+\varepsilon}) above target.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `t1_exact_extraction_and_prefix_target` | **Pass as an interface.** Equation (147.5) retains the weighted target and every half-open prefix; its uniform transform estimate remains open. |
| `squarefree_coprime_even_odd_character_and_cone` | **Pass.** Equations (147.14)--(147.16) retain squarefreeness, coprimality, parity, \(\chi _4\), and the strict cone. |
| `divisor_pairing_chi4_sector_ledger` | **Pass.** Equation (147.15) exhibits both the complete positive-character sector and the mandatory antisymmetric negative-character tail. |
| `ratio_Mellin_Euler_product_p2_and_H` | **Pass.** The exact (p=2) factor is (1-2^{-2w-2z}); (147.1)--(147.2) give the stronger audited factorization. |
| `target_safe_cone_collar_and_ratio_bandwidth` | **Pass/target-sized.** The \(\sqrt D\)-collar costs (O(X^\varepsilon)); hard Perron still needs height \(\gg D\). |
| `shifted_zeta_L_functional_equations_and_poles` | **Pass.** There is exactly one pole, at (w=1-z), and the polar term in (147.11) is retained. |
| `level_four_generalized_divisor_Voronoi_kernel` | **Pass as an exact Mellin-Barnes identity.** Equations (147.9)--(147.12) fix conductor, reflection, scaling, and the complete (H)-convolution. |
| `uniform_complex_order_and_Bessel_asymptotics` | **Open; first doubtful step.** Fixed-order branch geometry is not a uniform estimate in (147.13). |
| `H_powerful_coefficients_tail_and_signed_aggregation` | **Fail under triangle.** Powerful support proves (147.4), but the signed correlation (147.29) is unproved. |
| `dual_resonance_centre_width_amplitude_and_off_resonance` | **Centre/width/amplitude pass.** The family is (147.26), with amplitude (R^{-1}k^{-1}); uniform nonresonant and transition bounds remain part of the first seam. |
| `all_M_D_E_capacity_and_R4over3_barrier` | **Fail for the target.** The complete ledgers (147.4) and (147.31)--(147.34) retain positive powers and the (R^{4/3}) transition. |
| `clipped_prefix_profile_terminal_endpoint` | **Open.** Exact smooth interpolation is possible, but target-uniform transformed seminorms at the terminal unit transition are not proved. |
| `t1_D1_prime_even_and_slow_family_controls` | **Pass as checks.** Equation (147.16) verifies prime/even signs; (D=1) is a special bare subface and does not remove squarefreeness in the long variable. |
| `individual_positive_direction_and_fixed_centre` | **Pass.** No cosine replacement or centre average is used; (N=\lfloor X\rfloor) and the positive physical branch remain fixed. |
| `Round141_142_144_self_return_and_zero_mode` | **No bypass.** Equation (147.30) records the zero-mode recombination; a second termwise transform would self-return rather than aggregate (k). |
| `Round138_cross_and_downstream_scope` | **Retained open.** This face does not own the Round-138 cross, any (t\ge2) layer, (M9\!-!M1), (M9\!-!M2), endpoints, bridge, quarter target, or global exponent. |

No numerical experiment was used.  The reciprocal-phase lemma was proved symbolically, including its necessary (Q\ll N) hypothesis.

## 6. Dependencies and exact artifacts used

Only the task's permitted context was used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round147_t1_squarefree_cone_strategy.md`;
- `strategy/round147_source_and_method_strategy.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/candidates/conductor_round145_squarefree_kernel_reduction.md`;
- `rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/candidates/conductor_round146_three_variable_unmasking_and_dispersion_no_go.md`;
- `rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/reviews/conductor_round146_three_variable_adjudication.md`;
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/candidates/conductor_round141_cone_nonresonant_reduction.md`;
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/controls/conductor_round141_controls.md`.

No unlisted source, computation, or web result is used as proof input.  The compact-smooth formula, the refined Euler product, and the reciprocal-phase lemma were derived directly in this report.

## 7. Recommended state effect

**Recommendation: retain the (t=1) target open and record this report as a rigorous method no-go; make no graph, proof-draft, campaign, or exponent change.**

The exact identities (147.1), (147.11), and (147.12) are suitable candidate mathematics after independent seam review.  They replace the earlier source-applicability question at the identity level with a sharply localized estimate question.  They do not prove a target-safe range because the first uniform-order/prefix seam is open and the first signed squarefree-(H) saving is absent.

A successor objective, if authorized only after Round 147 closes, should isolate one of the following equivalent arithmetic gates:

\[
\text{a uniform bound for (147.29),}
\qquad\text{or}\qquad
\text{a squarefree/coprime strengthening of (147.32) avoiding (147.34).}
\]

Any such claim must retain the ratio bandwidth, polar term, unit-prefix boundary, conductor-four centre, and all (M,D,E,k) scales.  Until that signed gate and the lower-scale (R/\sqrt M) deficit are both resolved, there is no improvement to the global exponent.
