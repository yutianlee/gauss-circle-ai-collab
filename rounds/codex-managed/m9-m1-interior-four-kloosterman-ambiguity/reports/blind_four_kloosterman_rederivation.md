# Blind rederivation of the continuously twisted and \(d\)-A-process interfaces

## 1. Result: an interface-level no-go lemma

**Lemma (no \(B\)-power from the supplied row estimate, and no certified gain from the literal one-step \(d\)-A-process).**  Work classwise with

\[
(g,M,K)\in\{(1,4b,k),(2,2b,2[k\bar4]_b),(4,b,[k\bar4]_b)\},
\qquad b\asymp B,
\]

and let

\[
\mathcal E_b=\{d\in\mathbb Z:D_0<|d|<\Delta_b-E_*\}.
\]

Under exactly the hypotheses in the derivation packet, the following conclusions hold.

1. For every finitely supported multiplier \(w_b(d)\), the physical-row reduction is exactly

   \[
   {1\over M^2}\sum_{d,n}w_b(d)A_{M,K,d}(n)
   I_b(n+d)\overline{I_b(n)}
   =\int_0^1\mathcal G_b(\theta)K_{w_b}(\theta)\,d\theta,
   \tag{1.1}
   \]

   where \(K_{w_b}(\theta)=\sum_dw_b(d)e(-d\theta)\).  The uniform row estimate alone gives, after summing \(b\asymp B\),

   \[
   \ll_\varepsilon X^\varepsilon\Big(\max_{b\asymp B}\|K_{w_b}\|_1\Big)
   {C^3\over TQ^{5/12}}.
   \tag{1.2}
   \]

   If \(w_b(d_*)=1\) at even one retained difference, then

   \[
   \|K_{w_b}\|_1\geq 1.
   \tag{1.3}
   \]

   Consequently the \(L^\infty_\theta\)-row/\(L^1_\theta\)-multiplier interface cannot produce \(B^{-\delta}\) for any fixed \(\delta>0\).  This applies to the exact indicator of \(\mathcal E_b\), to a unit-plateau smoothing of it, and to every nonempty exact middle shell.  The formal ambiguity Parseval interface also gives no \(B\)-power when only the available pointwise size and support of \(I_b\) are inserted.

2. For a middle interval of length \(D\), the literal Fejer inequality has prefactor \((D+U-1)/U\), retains the diagonal, and for \(u\ne0\) opens into the full weighted four-Kloosterman term, both Ramanujan cross terms, and the Ramanujan-square term.  If \(U\leq M\asymp B\), even an ideal estimate reducing every off-diagonal to diagonal size can furnish at most the formal square-root gain \(B^{-1/2}\).  Relative to (1.2), \(B^{-1/2}\) reaches only

   \[
   C\leq J^{56/75}.
   \tag{1.4}
   \]

   At \(C=J^{3/4}\), the required gain is \(B^{-5/9}\), corresponding in a one-step A-process to \(U\asymp B^{10/9}>M\).  Such a shift range contains \(u=M,2M,\ldots\), where the complete ambiguity transform has exact arithmetic self-return.  The packet contains no estimate for those jointly weighted self-returns or for the preceding nonzero-\(u\) four-Kloosterman off-diagonal with its actual stationary symbol.

Thus neither proposed interface proves the target throughout the frozen range, proves a nonempty middle shell, nor isolates a strictly smaller exact signed survivor from the supplied facts.  This is a no-go for these **available estimates**, not a claim that a new weighted four-Kloosterman theorem or a new physical-row correlation estimate is impossible.

## 2. Exact statement and hypotheses

The only scales used are

\[
J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
B=C/T,
\]

with

\[
J^{13/18}<C\leq J^{3/4},\qquad
D_0=\lfloor J^{17/30}\rfloor,\qquad
E_*=\lfloor Q^2J^{-1/20}\rfloor,
\qquad \Delta_b\asymp Q^2.
\]

The desired conductor-block bound is \(X^\varepsilon J^2/T\).  The argument is performed separately for every compatible local class, alias, sign, and reflected orientation.  In particular, it never replaces a unit condition modulo \(M\) by one modulo another member of the three-class list.

On the smooth principal support, define the phase-removed amplitude \(a_b\) exactly by

\[
I_b(q)=H e(-\eta/8)a_b(q)e\!\left(-\eta\lambda_b\sqrt{|q|}\right),
\qquad
H={C\sqrt T\over J},\qquad
\lambda_b=\sqrt X+{\sqrt{\kappa k}\over b},
\tag{2.1}
\]

and extend \(a_b\) by zero outside \(\mathscr N_b\).  The accepted smooth hierarchy and the bound \(|a_b(q)|\ll_\varepsilon X^\varepsilon\) are the only analytic information about this amplitude used below.  No squarefree-modulus, prime-modulus, arbitrary-weight trace, or nonresonance hypothesis is added.

The exact object under discussion is only

\[
\mathfrak Y_{\rm int}
=\sum_{b\asymp B}{1\over M^2}
\sum_{d\in\mathcal E_b}\sum_n
A_{M,K,d}(n)I_b(n+d)\overline{I_b(n)}.
\tag{2.2}
\]

Both signs of \(d\), every nonzero \(d\equiv0\pmod M\), and every prime-power gcd mode remain in (2.2).  Raw Farey transitions, axes, already-owned small differences, already-owned edge differences, entry/exit errors, stationary errors, wrong signs, and exterior tails are not reintroduced.

## 3. Proof and derivation

### 3.1. Exact continuously twisted physical row

From Poisson summation,

\[
\mathcal R_{b,x}(\theta)
={1\over M}\sum_nI_b(n)e_M(nx)e(n\theta).
\]

Therefore, with the Kloosterman convention implicit in the packet,

\[
\mathcal S_b(\theta)
=\sum_{x\bmod M}^{*}e_M(K\bar x)\mathcal R_{b,x}(\theta)
={1\over M}\sum_nS(n,K;M)I_b(n)e(n\theta).
\tag{3.1}
\]

Opening the square and setting the first frequency equal to \(n+d\) gives

\[
|\mathcal S_b(\theta)|^2
={1\over M^2}\sum_{d,n}S(n+d,K;M)\overline{S(n,K;M)}
I_b(n+d)\overline{I_b(n)}e(d\theta).
\tag{3.2}
\]

On the other hand, unit orthogonality gives

\[
\sum_{x\bmod M}^{*}|\mathcal R_{b,x}(\theta)|^2
={1\over M^2}\sum_{d,n}c_M(d)
I_b(n+d)\overline{I_b(n)}e(d\theta).
\tag{3.3}
\]

Subtracting (3.3) from (3.2) proves the exact ambiguity identity and retains the external \(M^{-2}\):

\[
\mathcal G_b(\theta)
={1\over M^2}\sum_{d,n}A_{M,K,d}(n)
I_b(n+d)\overline{I_b(n)}e(d\theta).
\tag{3.4}
\]

Fourier extraction proves (1.1).  Nothing in this derivation distinguishes positive from negative \(d\), and \(d=jM\ne0\) is an ordinary nonzero Fourier coefficient.  In particular, \(c_M(jM)=\varphi(M)\) is subtracted exactly; it is not a reason to delete that difference.

Put \(L=X^\varepsilon TQ^{-5/24}\).  The accepted row bound and \(\varphi(M)\leq M\) give

\[
|\mathcal S_b(\theta)|\leq ML,
\qquad
\sum_{x\bmod M}^{*}|\mathcal R_{b,x}(\theta)|^2\leq ML^2,
\]

so

\[
\|\mathcal G_b\|_\infty
\ll_\varepsilon X^\varepsilon M^2T^2Q^{-5/12}.
\tag{3.5}
\]

The exponent \(Q^{-5/12}\) is exactly the square of the physical-row saving \(Q^{-5/24}\).  Summing \(O(B)\) conductors and using \(M\asymp B\) and \(B=C/T\) turns (3.5) into (1.2):

\[
B\cdot B^2T^2Q^{-5/12}={C^3\over TQ^{5/12}}.
\]

Finally, for any retained \(d_*\), Fourier inversion gives

\[
|w_b(d_*)|
=\left|\int_0^1K_{w_b}(\theta)e(d_*\theta)\,d\theta\right|
\leq\|K_{w_b}\|_1.
\tag{3.6}
\]

Thus a multiplier that equals one anywhere cannot turn (3.5) into a negative power of \(B\).  The fact that the exact middle kernel has zero mean, because \(w_b(0)=0\), does not help without an independent modulus of continuity or a signed pairing estimate for \(\mathcal G_b\).

### 3.2. Exact arithmetic ambiguity and why formal Parseval does not save \(B\)

Opening the two Kloosterman sums and writing the difference of their unit variables as \(h\) gives, for \(h\not\equiv0\pmod M\),

\[
\mathcal C_{M,K}(a,h)
=\sum_{\substack{y\bmod M\\(y(y+h),M)=1}}
e_M\!\left(a(y+h)+K(\overline{y+h}-\bar y)\right),
\tag{3.7}
\]

and

\[
A_{M,K,d}(n)=\sum_{h\ne0}\mathcal C_{M,K}(d,h)e_M(hn).
\tag{3.8}
\]

The omitted \(h=0\) term is exactly \(c_M(d)\).  Completing (3.7) in the \(a\)-variable gives the particularly rigid transform

\[
\widehat{\mathcal C}_{M,K}(v,h)
:=\sum_{a\bmod M}\mathcal C_{M,K}(a,h)e_M(-av)
=M\,1_{(v(v-h),M)=1}
e_M\!\left(K(\bar v-\overline{v-h})\right).
\tag{3.9}
\]

Hence its nonzero complete modes have magnitude \(M\), with the exact local-unit condition still present.  Parseval and translated Parseval yield

\[
\sum_{a\bmod M}|\mathcal C_{M,K}(a,h)|^2=MN_M(h),
\tag{3.10}
\]

\[
\sum_{a\bmod M}\mathcal C_{M,K}(a+u,h)
\overline{\mathcal C_{M,K}(a,h)}
=Me_M(uh)
\sum_{\substack{y\bmod M\\(y(y+h),M)=1}}e_M(uy).
\tag{3.11}
\]

For reference, direct counting at a prime power gives

\[
N_{p^\nu}(h)=
\begin{cases}
p^{\nu-1}(p-1),&p\mid h,\\
p^{\nu-1}(p-2),&p\nmid h,
\end{cases}
\tag{3.12}
\]

with the second line equal to zero when \(p=2\); the general \(N_M(h)\) is obtained classwise by the Chinese remainder theorem.  This makes clear that the complete energy can be of full order.  Moreover, the packet's \(p^{\nu-1/2}\) local modes rule out inserting a uniform coefficientwise square-root estimate in (3.7) or (3.11).

Grouping \(n=r+M\ell\) in (3.8) produces exactly

\[
W_{b,r,d}
=H^2\sum_{\ell}
a_b(r+M\ell+d)\overline{a_b(r+M\ell)}
e\!\left(-\eta\lambda_b
\big(\sqrt{|r+M\ell+d|}-\sqrt{|r+M\ell|}\big)\right).
\tag{3.13}
\]

The formal ambiguity estimate supplied in the packet is

\[
|\mathfrak Y_{E,b}|
\ll\sqrt{D/M}
\left(\sum_{d\in E}\sum_{r\bmod M}|W_{b,r,d}|^2\right)^{1/2}.
\tag{3.14}
\]

Here every middle shell has \(D\geq D_0\gg M\), since \(M\asymp B\leq J^{3/20}\) whereas \(D_0=J^{17/30+o(1)}\).  A residue class meets \(\mathscr N_b\) at most \(O(1+\Delta_b/M)\) times.  Cauchy-Schwarz in (3.13), with no unproved oscillation, therefore gives

\[
\sum_{d\in E}\sum_{r\bmod M}|W_{b,r,d}|^2
\ll_\varepsilon X^\varepsilon
DM(1+\Delta_b/M)^2H^4
\ll_\varepsilon X^\varepsilon{D\Delta_b^2H^4\over M}.
\tag{3.15}
\]

Inserting (3.15) in (3.14) gives

\[
|\mathfrak Y_{E,b}|
\ll_\varepsilon X^\varepsilon {D\Delta_bH^2\over M},
\tag{3.16}
\]

which is exactly the scale obtained by treating the \(\Delta_b/M\) summands in each ambiguity row trivially.  Thus the apparent arithmetic Parseval gain is consumed by the ambiguity energy.  Improving (3.15) would require a new estimate for the actual square-root phase in (3.13), including its exact resonances; it is not a consequence of (3.10).

### 3.3. Literal Fejer step and the full off-diagonal symbol

Let \(E\) be one exact positive or negative middle interval of \(D\) integers, and extend

\[
z_b(d)=1_E(d)Z_b(d)
\]

by zero.  Averaging \(U\) translates and applying Cauchy-Schwarz gives the exact Fejer inequality

\[
\left|\sum_dz_b(d)\right|^2
\leq {D+U-1\over U}
\left[
\sum_d|z_b(d)|^2
+2\Re\sum_{1\leq u<U}\left(1-{u\over U}\right)
\sum_dz_b(d+u)\overline{z_b(d)}
\right].
\tag{3.17}
\]

The indicator factors \(1_E(d+u)1_E(d)\) are retained inside every correlation.  Thus (3.17) does not borrow a difference from an already-owned small or edge range.  The diagonal in (3.17), together with its prefactor, is not discarded.

For \(u\ne0\), the correlation is exactly

\[
{1\over M^4}\sum_{\substack{d:\ d,d+u\in E}}
\sum_{n,m}A_{d+u}(n)\overline{A_d(m)}
\mathcal W_b(d,u,n,m),
\tag{3.18}
\]

where

\[
\mathcal W_b(d,u,n,m)
=I_b(n+d+u)\overline{I_b(n)}
\overline{I_b(m+d)}I_b(m).
\tag{3.19}
\]

The external \(M^{-2}\) has therefore become exactly \(M^{-4}\) before the final square root; no normalization has disappeared.  From (2.1), the complete principal symbol is

\[
\begin{aligned}
\mathcal W_b(d,u,n,m)
={}&H^4a_b(n+d+u)\overline{a_b(n)}
\overline{a_b(m+d)}a_b(m)\\
&\times e\!\left(-\eta\lambda_b\Psi(d,u,n,m)\right),
\end{aligned}
\tag{3.20}
\]

with support

\[
n+d+u,\ n,\ m+d,\ m\in\mathscr N_b
\]

and phase

\[
\Psi(d,u,n,m)
=\sqrt{|n+d+u|}-\sqrt{|n|}
-\sqrt{|m+d|}+\sqrt{|m|}.
\tag{3.21}
\]

The four Gaussian constants cancel exactly in (3.20).  Both reflected orientations and both signs of \(d\) retain the corresponding \(\eta\) and absolute values; no symmetry reduction is needed.

Writing

\[
P=S(n+d+u,K;M)\overline{S(n,K;M)},\qquad
Q=\overline{S(m+d,K;M)}S(m,K;M),
\]

the arithmetic factor in (3.18) is

\[
\begin{aligned}
A_{d+u}(n)\overline{A_d(m)}
={}&PQ
-P\,\overline{c_M(d)}
-c_M(d+u)Q
+c_M(d+u)\overline{c_M(d)}.
\end{aligned}
\tag{3.22}
\]

Thus (3.18) contains one four-Kloosterman term, two distinct Ramanujan cross terms, and one Ramanujan-square term, all with the same cutoff and actual symbol.  In particular, the cross and square terms cannot be silently absorbed into the already-owned two-Kloosterman diagonal.

The phase (3.21) has genuine exact integer resonances.  For any integers \(r\geq1\) and \(v>s\geq1\), take

\[
n=v^2,\qquad m=s^2,\qquad
d=r(2s+r),\qquad u=2r(v-s).
\tag{3.23}
\]

Then \(n+d+u=(v+r)^2\), \(m+d=(s+r)^2\), and \(\Psi=0\).  There are also perfect-fourth-power examples; explicitly,

\[
(n,m,d,u)=(625,1,624,1152)
\]

gives

\[
(n+d+u,n,m+d,m)=(2401,625,625,1)
=(7^4,5^4,5^4,1^4)
\]

and again \(\Psi=0\).  The packet supplies no support condition excluding such algebraic loci.  Hence \(u\ne0\) is not, by itself, a valid nonstationarity hypothesis; any positive estimate must isolate and count these resonances with their arithmetic weights.

### 3.4. Quantitative A-process obstruction and exact self-return

Suppose a gain \(B^{-\beta}\) could be attached to the physical scale (1.2).  Writing \(C=J^\alpha\), the target condition would be

\[
C^3B^{-\beta}\leq J^2Q^{5/12},
\]

or equivalently

\[
(3-\beta)\alpha+{3\beta\over5}\leq {13\over6}.
\tag{3.24}
\]

For \(\beta=1/2\), (3.24) is \(\alpha\leq56/75\).  For \(\alpha=3/4\), it requires \(\beta\geq5/9\).  A one-step Fejer gain is at most \(U^{-1/2}\); staying below the first modulus return means \(U\leq M\asymp B\), hence \(\beta\leq1/2\).  Formally attaining \(\beta=5/9\) requires \(U\asymp B^{10/9}\).

The obstruction beyond \(M\) is exact, not heuristic.  Equation (3.9) implies periodicity in the shifted \(d\)-coefficient, and (3.11) at \(u=jM\) gives

\[
\sum_{a\bmod M}\mathcal C_{M,K}(a+jM,h)
\overline{\mathcal C_{M,K}(a,h)}
=MN_M(h).
\tag{3.25}
\]

Thus a height \(U\asymp B^{10/9}\) contains \(\asymp B^{1/9}\) nonzero self-return shifts.  Their Fejer weights \(1-jM/U\), their Ramanujan companions, and their stationary symbols (3.20) must be estimated jointly.  Deleting them would change the exact correlation.  Taking absolute values loses the desired cancellation, while the packet gives no signed estimate for (3.18).  This is the point at which the literal A-process stops.

## 4. First doubtful or unproved step

For the continuously twisted physical-row route, the first missing step is any estimate stronger than

\[
|\mathcal S_b(\theta)|\leq
\sum_{x\bmod M}^{*}|\mathcal R_{b,x}(\theta)|.
\]

A \(B\)-power would require a genuine correlation estimate in the unit variable \(x\), or a signed \(\theta\)-pairing estimate for \(\mathcal G_b\) against the exact middle kernel.  Neither follows from the uniform individual-row estimate, and an arbitrary-weight trace estimate is not an allowed hypothesis.

For the ambiguity-energy route, the first missing step is a power-saving replacement for (3.15) with the exact phase (3.13).  Parseval identity (3.10) alone does not provide it.

For the literal \(d\)-A-process route, the first missing step is already the nonzero-shift sum (3.18), before absolute values, with (3.20) and all four terms in (3.22).  At the endpoint the required estimate must also include every \(u=jM<U\asymp B^{10/9}\).  No supplied fact bounds this expression, and the exact resonances (3.23) prevent replacing it by a blanket first-derivative estimate.

## 5. Control tests and outcomes

| Required control | Test performed | Outcome |
|---|---|---|
| `external_normalization` | Tracked (3.4) through (3.18). | Pass: \(M^{-2}\) is external in the linear form and \(M^{-4}\) in the squared correlation. |
| `all_class_local_units` | Derived (3.7)--(3.12) modulo the actual \(M\). | Pass: all three classes remain separate; even local factors are retained. |
| `physical_row_energy_factor` | Squared \(TQ^{-5/24}\) in (3.5). | Pass: the inherited factor is exactly \(Q^{-5/12}\). |
| `middle_difference_ownership` | Used \(1_E(d+u)1_E(d)\) and zero extension in (3.17). | Pass: only \(D_0<|d|<\Delta_b-E_*\) is treated. |
| `negative_and_modulus_multiple_differences` | Kept signed intervals separately and noted \(d=jM\ne0\) after (3.4). | Pass: neither family is deleted. |
| `ramanujan_cross_and_square_terms` | Expanded (3.22). | Pass: two cross terms and one square term occur exactly once. |
| `prime_power_gcd_modes` | Checked (3.12) and retained the packet's \(p^{\nu-1/2}\) modes. | Pass/no-go: no uniform coefficientwise square-root bound was used. |
| `fejer_prefactor_and_diagonal` | Derived (3.17). | Pass: \((D+U-1)/U\), the diagonal, and every Fejer weight remain. |
| `four_kloosterman_offdiagonal` | Displayed (3.18) and (3.22). | Open: this is the first unsupported estimate, so no positive conclusion is claimed. |
| `actual_stationary_symbol` | Derived (3.20)--(3.21), including support and Gaussian cancellation. | Pass as an interface; its required signed estimate remains open. |
| `entry_exit_and_error_ownership` | Worked only with the exact smooth-principal survivor and zero-extended its \(d\)-interval. | Pass: no raw transition, axis, entry/exit, or stationary error is reassigned. |
| `integer_and_perfect_power_resonance` | Exhibited (3.23) and a fourth-power example. | Pass/no-go: exact resonance is possible and must be isolated in any future estimate. |
| `complete_transform_and_uM_self_return` | Derived (3.9), (3.11), and (3.25). | Pass/no-go: \(u=jM\) returns full energy and cannot be removed. |
| `downstream_scope` | Compared only with \(X^\varepsilon J^2/T\) in the frozen \(C\)-range. | Pass: no assertion is made beyond the Round-86 interior survivor. |

## 6. Dependencies and exact artifacts used

Only the following statement-only artifacts were used:

1. `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/briefs/blind_four_kloosterman_rederivation.md` (task contract and exclusions).
2. `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/derivation_packet.md` (the complete mathematical input).

No prior-round report, sibling report, strategy file, proof-state file, source card, web source, or external theorem was read or used.  No numerical experiment was needed.

## 7. Recommended state effect

**Retain.**  Retain (2.2) as the unresolved exact survivor and retain the endpoint obligation.  The exact identities and quantitative obstruction above may be retained as candidate no-go evidence: the continuously twisted row bound supplies no \(B\)-power through multiplier \(L^1\), formal ambiguity Parseval is neutral, and the diagonal-scale one-step A-process stops at \(B^{-1/2}\) before the required \(B^{-5/9}\).  Do not promote a middle-shell or endpoint bound unless a separate seam review validates a signed estimate for (3.18), including Ramanujan terms, exact resonances, prime-power modes, and all \(u=jM\) self-returns.
