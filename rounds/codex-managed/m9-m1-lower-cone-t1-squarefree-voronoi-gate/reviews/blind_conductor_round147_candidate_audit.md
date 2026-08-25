# Round 147 independent arithmetic seam audit of the conductor candidate

Campaign: `m9-m1-lower-cone-t1-squarefree-voronoi-gate`  
Role: former statement-only blind rederiver, now independent candidate reviewer  
Candidate: `candidates/conductor_round147_t1_squarefree_voronoi_and_H_no_go.md`  
Allocation: 100% analytic; no numerical experiment

## 1. Result: revise, then arithmetic-green

**Exact verdict: REVISE; not green as written.** The coefficient algebra, parity ledger, divisor pairing, collar count, Euler factors, prime-power residual coefficients, convolution scaling, conductor-four centre, resonant width, and raw/physical amplitude are correct. The scoped methodological conclusion—Voronoi followed by modulus and absolute powerful-index aggregation does not reach the target—is also correct on the unitary ratio line.

Three corrections are required before the candidate can be promoted even as a reduction/no-go.

1. **Equations (147.C6) and (147.C40) silently use \(\Re z=0\).** They do not follow uniformly on the fixed strip stated around (147.C20). If (c=\Re z\), the same calculation contains an additional factor (k_0^{|c|}), where (k_0=M^{3/4}/R). The candidate must place the smoothed cone transform on (z\in i\mathbb R), or take \(|c|\ll1/\log X\), before asserting (147.C6).
2. **The local (d\asymp D) cone smoothing is not yet connected exactly to (147.C13)--(147.C15).** Mellin inversion of the (d/D) partition introduces an auxiliary order and a radial twist. The missing identity and its external constants are given in (2.8) below. Without it, the claimed (D)-dependent bandwidth and the global (B_z=h_z*A_z) transform are adjacent formulas, not one exact reduction.
3. **Equation (147.C29) mixes the full infinite (H(1-z,z)) representation with the later physical truncation (k\le2M).** Either retain the (k>2M) polar-plus-dual zero identities as an inseparable aggregate, or, preferably, apply Voronoi only to the finite physical convolution and replace (H(1-z,z)) by its truncated sum. Equation (147.C44) must then state (k\le2M).

There are also three required clarifications: state the original Euler product's absolute domain; display the hard-Perron (z=0) residue rather than merely mentioning it; and add the literal primal exact/near-radical controls (N=sL^2) and (N=sL^2+1).

The candidate does **not** make the logical error of declaring the separate (t=1) estimate necessary. Lines 100--102 explicitly call it sufficient but not necessary. For complete safety, “the first missing arithmetic statement” before (147.C44) should read “the first missing arithmetic statement for this separate-(t=1) Voronoi route.”

## 2. Exact statement and hypotheses after correction

Let (e(x)=e^{2\pi ix}), (X\ge2), (N=\lfloor X\rfloor), (R=X^{1/4}), (M\ll R^2), and (M\le U\le B_M\le2M). Let the radial profile be the inherited compact smooth (V_{\rm low}), and retain the half-open prefix exactly. For squarefree (s=2^\nu n), with (n) odd and \(\nu\in\{0,1\}), the coefficient is

\[
C(2^\nu n)=\sum_{\substack{e\mid n\\e>2^{1+\nu/2}\sqrt n}}\chi _4(e).
\tag{2.1}
\]

With (c_\nu=2^{1+\nu/2}) and

\[
\mathfrak B_\nu(n)=
\sum_{\substack{e\mid n\\c_\nu^{-1}\sqrt n<e<c_\nu\sqrt n}}\chi _4(e),
\]

one has

\[
\sum_{e\mid n}\chi _4(e)
=(1+\chi _4(n))C(2^\nu n)+\mathfrak B_\nu(n).
\tag{2.2}
\]

The ratio coefficient and complete coefficient are

\[
B_z(n)=\mu^2(n)A_z(n),\qquad
A_z(n)=\sum_{de=n}\chi _4(e)(e/d)^z
=n^{-z}\sigma_{2z,\chi _4}(n).
\tag{2.3}
\]

Here the condition (e) odd is automatic because (\chi _4(e)=0) for even (e). Their series satisfy

\[
\sum_n\frac{A_z(n)}{n^w}=\zeta(w+z)L(w-z,\chi _4),
\qquad
B_z=h_z*A_z.
\tag{2.4}
\]

The original Euler product is absolutely convergent only in

\[
\Re(w+z)>1,\qquad \Re(w-z)>1,
\tag{2.5}
\]

whereas (H) is coefficientwise absolutely convergent in

\[
\Re(w+z)>\tfrac12,\qquad \Re(w-z)>\tfrac12.
\tag{2.6}
\]

For a hard cone, parity excludes equality and Perron gives

\[
1_{e>4d}
=\lim_{T\to\infty}\frac1{2\pi i}
\int_{c-iT}^{c+iT}4^{-z}(e/d)^z\frac{dz}{z},
\qquad c>0.
\tag{2.7}
\]

Any deformation toward the unitary line must retain the (z=0) residue. For the target-safe local smoothing, let (\psi_D(d)) be a smooth (d\asymp D) partition, with Mellin order (t), and let (\tau) be the Fourier order of the smoothed ratio cutoff. Then the exact normalization is

\[
d^{-it}(e/d)^{i\tau}
=(de)^{-it/2}(e/d)^{i(\tau+t/2)},
\qquad
z=i(\tau+t/2),
\tag{2.8}
\]

with external factor (D^{it}4^{-i\tau}) under the convention
\(\psi_D(d)=(2\pi)^{-1}\int\widehat\psi_D(t)D^{it}d^{-it}\,dt\). Equivalently, if one writes (4^{-z}), the compensating factor (4^{it/2}) must also appear. The radial test acquires (s^{-it/2}). The (t)-weight is rapidly decreasing and the cone order has \(|\tau|\ll D^{1/2}X^\varepsilon\), but both orders must be retained in the uniform kernel seam.

For a physical test (F) supported in (0<u<2M), the clean finite convolution identity is

\[
\sum_nB_z(n)F(n)
=\sum_{\substack{k\le2M\\h_z(k)\ne0}}h_z(k)
\sum_\ell A_z(\ell)F(k\ell).
\tag{2.9}
\]

Applying the candidate's fixed-order formula channel by channel gives

\[
\begin{aligned}
\sum_nB_z(n)F(n)
={}&L(1-2z,\chi _4)
\left(\sum_{k\le2M}h_z(k)k^{z-1}\right)
\int_0^\infty F(u)u^{-z}\,du\\
&+\pi4^z\sum_{k\le2M}\frac{h_z(k)}k
\sum_{m\ge1}A_{-z}(m)
\int_0^\infty F(u)
\mathscr B_{2z}(2\pi\sqrt{mu/k})\,du.
\end{aligned}
\tag{2.10}
\]

This finite form is the one compatible with the later termwise (k)-capacity calculation. The candidate's full-(H) form is also formally exact only if every (k>2M) polar-plus-dual zero identity is kept intact and the infinite rearrangement is justified; those terms may not then be discarded separately.

## 3. Proof and seam derivation

### 3.1 Coefficient, parity, and divisor pairing

If (s=2^\nu n) is squarefree and (e) is odd, then (e\mid n) and (d=2^\nu n/e). Thus

\[
e>4d\iff e^2>2^{\nu+2}n
\iff e>2^{1+\nu/2}\sqrt n,
\]

which verifies (147.C8). Equality would make the odd square (e^2) equal to the even integer (2^{\nu+2}n), so neither central boundary occurs.

Complementation (e\leftrightarrow n/e) maps the high tail to the low tail, and

\[
\chi _4(n/e)=\chi _4(n)\chi _4(e).
\]

Writing total (=H+L+\mathfrak B_\nu), one has (H=\chi _4(n)L), which proves (147.C9). If (\chi _4(n)=1), then (H=(\text{total}-\mathfrak B_\nu)/2). If \(\chi _4(n)=-1), the middle divisors pair antisymmetrically and their sum is zero, but (H=-L) remains. The candidate therefore correctly retains the negative-total-character tail.

For odd primes,

\[
C(p)=\chi _4(p)\quad(p>4),\qquad
C(2p)=\chi _4(p)\quad(p>8),
\]

and (C(1)=C(2)=0). These candidate controls are exact.

### 3.2 Strict cone, collar, and prefixes

On a boundary box (d\asymp D), (e\asymp4D), so (M=de\asymp D^2). The collar \(|e-4d|\le\sqrt D\) has at most

\[
O(D)\,O(\sqrt D+1)=O(D^{3/2})=O(M^{3/4})
\]

pairs. Squarefreeness, coprimality, parity, a character, and clipping at (U) can only decrease this absolute count. Multiplication by (s^{-3/4}\asymp D^{-3/2}) gives physical cost (O(1)). Outside the collar the relative gap is \(\gg D^{-1/2}), hence smooth Fourier bandwidth (D^{1/2}X^\varepsilon). The nearest strict point (e=4d+1) has logarithmic gap \(\asymp D^{-1}), so a hard Perron truncation needs height (\gg D). Equations (147.C11)--(147.C12) are correct; (2.8) is the missing interface to the Euler coefficient.

The candidate's terminal smoothing over (O(\sqrt M)) integers is target-safe because the literal coefficient is divisor-bounded and \(M^{1/2}\le M^{3/4}). This is uniform in every half-open prefix. It does not authorize scale-(M) derivative bounds for the moving transition, a caveat the candidate correctly retains.

### 3.3 Euler factors, residual coefficients, and support

At (2), the only squarefree choices are no (2), or (2\mid d). Thus the local numerator is (1+2^{-w-z}), and removal of the zeta factor gives

\[
H_2=(1+2^{-w-z})(1-2^{-w-z})=1-2^{-2w-2z}.
\]

At odd (p), put (a=p^{-w-z}) and (b=\chi _4(p)p^{-w+z}). The squarefree/coprime local numerator is (1+a+b), so

\[
H_p=(1+a+b)(1-a)(1-b)
=1-a^2-b^2-ab+a^2b+ab^2.
\]

Collecting equal powers of (p^{-w}) gives exactly

\[
\begin{aligned}
h_z(2^2)&=-2^{-2z},\\
h_z(p^2)&=-(p^{-2z}+p^{2z}+\chi _4(p)),\\
h_z(p^3)&=p^z+\chi _4(p)p^{-z}\qquad(p\text{ odd}),
\end{aligned}
\tag{3.1}
\]

with no other nontrivial prime-power coefficients. Hence every nonzero prime exponent in the support is (2) or (3), with exponent (3) absent at (2); the support is powerful. Equations (147.C16)--(147.C20) are arithmetically correct. The quadratic refactorization (147.C21)--(147.C24), including the compensating (p=2) factor, is also correct.

The missing domain sentence after (147.C14) is (2.5). Without it, (147.C18) can be misread as the absolute domain of the original (Z), rather than of its residual (H).

### 3.4 The fixed-strip power correction

Let (c=\Re z), \(|c|<1/2). From (147.C20) and powerful support one obtains

\[
\sum_{\substack{k\le K\\h_z(k)\ne0}}|h_z(k)|
\ll_\varepsilon K^{1/2+|c|+\varepsilon},
\qquad
\sum_{\substack{k>K\\h_z(k)\ne0}}\frac{|h_z(k)|}{k}
\ll_\varepsilon K^{-1/2+|c|+\varepsilon}.
\tag{3.2}
\]

Consequently, when (k_0=M^{3/4}/R\ge1), the calculation asserted in (147.C40) actually gives

\[
\sum_k|h_z(k)|\min(M/k,RM^{1/4})
\ll_\varepsilon
R^{1/2}M^{5/8}
\left(\frac{M^{3/4}}R\right)^{|c|+\varepsilon}.
\tag{3.3}
\]

Thus (147.C40) and the normalized statement (147.C6) are correct only on (c=0), or when \(|c|\ll1/\log X\) so that the extra factor is harmless. A fixed positive Perron line does not give the displayed (X^\varepsilon) price. This is an exact equation correction, not a source-uniformity issue.

### 3.5 Conductor, centre, width, and amplitude

At (z=0), the candidate's normalization gives the exact kernel

\[
\pi J_0(2\pi\sqrt y)
=\frac{y^{-1/4}}2
\{e(\sqrt y-1/8)+e(-\sqrt y+1/8)\}
+O(y^{-3/4}).
\tag{3.4}
\]

This fixes conductor (4): the two phases are \(e(\pm2\sqrt{mx/4})=e(\pm\sqrt{mx})\). After scaling (u=kx), the negative branch against (e(+\sqrt{Nu})) has phase

\[
(\sqrt N-\sqrt{m/k})\sqrt u.
\]

Its exact centre is (m=kN), and, writing (m=kN+j), its variation across (u\asymp M) is (O(1)) for

\[
|j|\ll k\sqrt{N/M}.
\]

At the centre, one raw dual term, including the convolution factor (1/k), has size

\[
\frac1k\int_{u\asymp M}(Nu)^{-1/4}\,du
\asymp\frac{M^{3/4}}{kR}.
\tag{3.5}
\]

After multiplication by the physical weight (M^{-3/4}), this is (1/(kR)). The entire band has raw modulus capacity (RM^{1/4}), hence physical capacity (R/\sqrt M). Equations (147.C32)--(147.C37) and the result paragraph's one-term physical amplitude are correct.

### 3.6 Sufficiency is not necessity

The exact small-(t) scalar decomposes into a (t=1) summand plus the remaining (t\ge2) summands. A separate estimate for the first summand is sufficient in a proof that bounds layers separately. The converse implication is false: a bound for the joint (t)-sum need not bound its (t=1) summand because cross-layer cancellation is possible.

The candidate states this correctly at lines 100--102 and never uses (147.C3) as a logical consequence of the global target. “Mandatory” is used in the proper support sense: the face cannot be deleted from a termwise decomposition. The only potentially ambiguous sentence is line 582; adding “for this separate-(t=1) Voronoi route” before “first missing arithmetic statement” removes the ambiguity.

## 4. First doubtful or unproved step

The first defect in the written candidate is not arithmetic cancellation but the exact cone-to-transform interface: equations (2.7)--(2.10) and the unitary-line restriction must be inserted before the capacity no-go is mechanically valid.

After those corrections, the first genuinely unproved analytic step remains the candidate's uniform growing-imaginary-order, moving-prefix expansion of the complete (J/Y/K) kernel throughout its small, transition, and large argument regimes. Granting that theorem, the first arithmetic owner is the route-specific signed correlation

\[
\sum_{\substack{k\le2M\\k\ {\rm powerful}}}\frac{h_z(k)}k
\sum_{|j|\lesssim k\sqrt{N/M}}
A_{-z}(kN+j)\mathcal W_{k,z,U}(j)
\ll_\varepsilon X^\varepsilon,
\tag{4.1}
\]

after physical normalization and integration over the exact orders in (2.8). It must hold uniformly in (N,M,U,D,\tau,t), retain the positive physical direction, and use the actual (h_zA_{-z}) signs. Absolute convergence, disjoint bands, arbitrary-coefficient square-root cancellation, or a second termwise transform does not prove (4.1).

The adverse powers in (147.C6), (147.C40), and (147.C43) remain upper-bound limitations. They are not signed lower bounds for the literal cone scalar and do not disprove (4.1).

## 5. Control tests and outcomes

| Control | Verdict | Audit |
|---|---|---|
| odd/even (t=1) coefficient | Green | (147.C8) follows exactly from forcing (2^\nu\) into (d). |
| divisor-pairing sectors | Green | (147.C9) is exact; the (\chi _4(n)=-1) high tail remains. |
| strict cone and equality | Green | Both potential equalities are impossible by parity. |
| cone collar and prefix price | Green | (D^{3/2}=M^{3/4}) raw and (O(1)) physical, uniformly after clipping. |
| local cone-to-Euler Mellin normalization | Revise | Insert (2.8), including (D^{it}4^{-i\tau}), the radial twist, and all induced orders. |
| hard Perron zero mode | Revise | Insert (2.7) and explicitly retain the residue when moving to (\Re z=0). |
| (p=2) and odd Euler factors | Green | (147.C16)--(147.C17) are exact. |
| (h_z(p^2),h_z(p^3)), support | Green | (147.C19) is exact; supported exponents are (2,3), with no (2^3). |
| original versus residual convergence | Clarify | Add (2.5); (147.C18) is the residual-(H) domain. |
| convolution normalization | Revise presentation | Use finite (2.9)--(2.10), or keep the full (k>2M) zero aggregate inseparable. |
| fixed-strip (k)-power | Red | (147.C40) lacks (k_0^{|\Re z|}); it becomes green on the unitary line. |
| conductor-four centre | Green | The argument (2\pi\sqrt{mu/k}) gives (m=kN), never (kN/4). |
| resonant width and amplitude | Green | Width (k\sqrt{N/M}); raw one-term size (M^{3/4}/(kR)); physical size (1/(kR)). |
| (D=1) | Green but still open | It has bounded cone bandwidth and remains literal; no target estimate is inferred from bounded (D). |
| primes | Green | (C(p)=\chi _4(p)) for odd (p>4), proving nonvacuity only. |
| even squarefree inputs | Green | (C(2p)=\chi _4(p)) for odd (p>8); the threshold is (2^{3/2}\sqrt p). |
| dual exact radical | Green | (m=kN\in\mathbb N) and (\sqrt{m/k}=\sqrt N) identically for fixed (N=\lfloor X\rfloor). |
| primal exact/slow radical | Add explicit control | If (N=sL^2), then (e(\sqrt{Ns})=1). If (N=sL^2+1), then \(\sqrt{Ns}=sL+\rho\), (\rho=(\sqrt{L^2+1/s}+L)^{-1}), so the retained phase can rotate arbitrarily slowly. Neither identity is a lower bound. |
| individual positive direction | Green | Only the negative Bessel branch resonates against the retained (+) direction. |
| sufficient versus necessary (t=1) bound | Green | The candidate expressly denies necessity; add the route-specific wording at line 582. |
| downstream scope | Green | No (t\ge2), cross-owner, M1/M2, M9, bridge, target, or exponent claim follows. |

## 6. Dependencies and exact artifacts used

This review used only the following project artifacts:

1. `protocol.md` (already read completely for the blind assignment);
2. `state/active_campaign.yml`;
3. the four active target entries extracted from `state/proof_obligations.yml`;
4. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/candidates/conductor_round147_t1_squarefree_voronoi_and_H_no_go.md`;
5. the earlier statement-only problem, brief, and blind rederivation as provenance.

No sibling Round-147 report, strategy artifact, web source, or computation was used in this seam audit.

## 7. Recommended state effect and exact candidate edits

**Recommended state effect: revise the candidate; make no graph promotion yet.** The following edits are sufficient for the arithmetic seam.

1. After (147.C14), insert the original absolute domain (2.5), distinguishing it from (147.C18).
2. After (147.C12), insert hard Perron formula (2.7), the local partition identity (2.8), and the induced radial twist and external constants.
3. Replace (147.C29), for the physical test used later, by finite formula (2.10). If the full-(H) version is retained as an alternative identity, label the (k>2M) polar-plus-dual tail an inseparable zero aggregate and do not use it in (147.C40).
4. Before (147.C40), state (\Re z=0). Alternatively replace (147.C40) by (3.3), and state that (147.C6) follows only after choosing a unitary or (O(1/\log X)) line.
5. In (147.C44), insert (k\le2M), the auxiliary order/radial twist from (2.8), and the phrase “for this separate-(t=1) Voronoi route.”
6. Expand control 9 with the explicit (N=sL^2) and (N=sL^2+1) formulas above.

After these corrections, the exact arithmetic/conductor/collar portion is green, while the candidate must remain a scoped `squarefree_H_resonance_no_go`: the growing-order transform estimate and signed correlation (4.1) are open, and the separate (t=1) target is sufficient but not necessary for every possible future proof route.
