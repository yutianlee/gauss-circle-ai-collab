# Round 147 statement-only blind rederivation: the squarefree (t=1) cone

Campaign: `m9-m1-lower-cone-t1-squarefree-voronoi-gate`  
Task: `blind_t1_squarefree_voronoi_rederivation`  
Role: statement-only blind rederiver  
Status: candidate evidence only

## 1. Result: exact reduction and no-go for absolute (H)-aggregation

Let (e(x)=e^{2\pi i x}), (R=X^{1/4}), and (N=\lfloor X\rfloor). The squarefree coefficient, including its even sector, is

\[
C(2^\nu n)=\sum_{\substack{e\mid n\\ e>2^{1+\nu/2}\sqrt n}}\chi _4(e),
\qquad \nu\in\{0,1\},\quad n\text{ odd and squarefree}.
\tag{1.1}
\]

Its unconed ratio-Mellin series has the exact factorization

\[
Z(w,z)=\zeta(w+z)L(w-z,\chi _4)H(w,z),
\tag{1.2}
\]

where

\[
H_2(w,z)=1-2^{-2w-2z}
\tag{1.3}
\]

and, for every odd prime (p), on writing

\[
x=p^{-w-z},\qquad y=\chi _4(p)p^{-w+z},
\]

one has

\[
H_p(w,z)=(1+x+y)(1-x)(1-y)
=1-x^2-y^2-xy+x^2y+xy^2.
\tag{1.4}
\]

The original Euler product is absolutely convergent for

\[
\Re(w+z)>1,\qquad \Re(w-z)>1,
\tag{1.5}
\]

while the residual product (H), and its coefficientwise absolute Dirichlet expansion, are absolutely convergent in the larger region

\[
\Re(w+z)>\tfrac12,\qquad \Re(w-z)>\tfrac12.
\tag{1.6}
\]

For fixed (z), write

\[
H(w,z)=\sum_{k\geq1}\frac{h_z(k)}{k^w}.
\]

Then (h_z) is multiplicative and is supported on integers whose nonzero prime exponents are (2) or (3), with exponent (3) excluded at (2). In particular it is supported on powerful integers. Its exact prime-power values are

\[
\begin{aligned}
h_z(p^2)&=-p^{-2z}-p^{2z}-\chi _4(p),&
h_z(p^3)&=\chi _4(p)p^{-z}+p^z &&(p\text{ odd}),\\
h_z(2^2)&=-2^{-2z},&h_z(2^j)&=0 &&(j\ne0,2),
\end{aligned}
\tag{1.7}
\]

and all other odd-prime powers vanish. Thus, on (Re z=0),

\[
|h_z(k)|\leq 3^{\omega(k)}\ll_\varepsilon k^\varepsilon,
\qquad
\sum_k |h_z(k)|k^{-\sigma}<\infty\quad(\sigma>\tfrac12),
\tag{1.8}
\]

uniformly in (Im z). This is not an unweighted physical (\ell^1) estimate.

A target-safe cone collar exists. On (d\asymp D) the pairs with

\[
|e-4d|\leq D^{1/2}
\tag{1.9}
\]

have total unweighted multiplicity (O(D^{3/2})=O(M^{3/4})) when (de\asymp M) and the cone boundary is met. They therefore cost (O(M^{3/4}X^\varepsilon)) in every clipped prefix, and (O(X^\varepsilon)) after multiplication by (s^{-3/4}). Removing this collar allows a smooth ratio cutoff with effective Mellin bandwidth

\[
|\Im z|\ll D^{1/2}X^\varepsilon.
\tag{1.10}
\]

In contrast, an exact hard Perron cutoff must distinguish (e=4d+1) and hence needs height (T\gg D).

The level-four generalized-divisor transform is lawful. Its exact completed functional equation is given in Section 3. At (z=0) it reduces to the particularly transparent identity

\[
\sum_{n\geq1}b_0(n)f(n)
=\frac{\pi}{4}\int_0^\infty f(x)\,dx
+\pi\sum_{m\geq1}b_0(m)\int_0^\infty f(x)J_0(2\pi\sqrt{mx})\,dx,
\tag{1.11}
\]

where

\[
b_z(n)=\sum_{ab=n}\chi _4(b)(b/a)^z,
\qquad b_0(n)=\frac{r_2(n)}4.
\tag{1.12}
\]

Thus the conductor is (4), the cusp transfer has phase

\[
e\!\left(\pm2\sqrt{mx/4}\right)=e(\pm\sqrt{mx}),
\tag{1.13}
\]

and the negative branch, against the retained individual phase (e(+\sqrt{Nx})), resonates at (m=N). After the exact (H)-convolution, the (k)-channel is tested at (x=s/k), the conductor remains (4), and its resonant band is

\[
m=kN+O\!\left(k\sqrt{N/M}\right).
\tag{1.14}
\]

The centre (m=kN) is exact, not an approximate radical relation.

The conclusion is a strict reduction and an exact methodological no-go:

> The factorization (1.2), the lawful level-four transform, stationary phase, absolute convergence of (H), and termwise modulus in either the dual variable or the powerful index do **not** prove the prefix target. Even for the bare (k=1) factor their best all-scale capacity has normalized loss
> \[
> \min\{M^{1/4},R/\sqrt M\},
> \tag{1.15}
> \]
> whose maximum on (1\leq M\leq R^2) is (R^{1/3}) at (M=R^{4/3}). With the full powerful convolution, optimizing trivial and transformed estimates channel by channel still gives, for (M\geq R^{4/3}), normalized loss
> \[
> R^{1/2}M^{-1/8},
> \tag{1.16}
> \]
> which is (R^{1/3}) at (M=R^{4/3}) and (R^{1/4}) at (M=R^2). For (M\leq R^{4/3}), the available loss is (M^{1/4}).

These are upper-capacity failures, not signed lower bounds for the original cone sum. The route survives only if one proves a new joint signed estimate over the actual (\chi _4)-coefficients, the powerful (h_z(k)), the moving bands (1.14), and the cone Mellin orders, uniformly for every clipped prefix. Section 4 states that missing owner exactly.

## 2. Exact statement and hypotheses

Assume (X\geq2), (N=\lfloor X\rfloor), (R=X^{1/4}), (M\ll R^2), and

\[
\mathcal I_M=\mathbb N\cap[M,B_M),\qquad B_M\leq2M.
\]

Let (V_{\rm low}) be a fixed, nonzero, compactly supported smooth radial profile, with constants allowed to depend on finitely many of its seminorms. Every assertion below is uniform in the half-open endpoint (M\leq U\leq B_M). The exact object is

\[
S(M,U)=\sum_{\substack{M\leq s<U\\ \mu^2(s)=1}}
V_{\rm low}(R^2s/N)C(s)e(+\sqrt{Ns}).
\tag{2.1}
\]

No cosine symmetrization, (N)-average, arbitrary-coefficient majorant, or (k)-dependent change of conductor is allowed.

For the ratio-Mellin coefficient define

\[
a_z(n)=\sum_{de=n}\mu^2(de)\,1_{2\nmid e}\,\chi _4(e)(e/d)^z.
\tag{2.2}
\]

Then

\[
\sum_{n\geq1}\frac{a_z(n)}{n^w}=Z(w,z),
\qquad
a_z=h_z*b_z,
\tag{2.3}
\]

with (h_z) and (b_z) as in (1.7) and (1.12). A local smooth partition (d\asymp D), followed by a target-safe smoothing of (1_{e>4d}) outside (1.9), gives ordinary Mellin/Fourier orders on (Re z=0) with (|\Im z|\ll D^{1/2}X^\varepsilon). If a smooth (d/D) partition introduces an auxiliary order (t), then

\[
d^{-it}(e/d)^{i\tau}=(de)^{-it/2}(e/d)^{i(\tau+t/2)},
\tag{2.4}
\]

so it only adds a radial unitary twist and replaces (z) by (i(\tau+t/2)). The (t)-transform is rapidly decreasing, but all such orders must remain uniform. A hard ratio Perron integral instead has its (1/z) pole and zero-frequency residue explicitly retained.

For each finite complex order (z), define

\[
D_z(w)=\zeta(w+z)L(w-z,\chi _4)=\sum_{n\geq1}\frac{b_z(n)}{n^w}.
\tag{2.5}
\]

The exact transform in Section 3 is applied to

\[
f_{k,M,U,t}(x)=1_{[M,U)}(kx)
V_{\rm low}(R^2kx/N)(kx)^{-it/2}e(+\sqrt{Nkx}),
\tag{2.6}
\]

under smooth approximation and passage to the bounded-variation limit. This preserves the actual half-open prefix. Equivalently one may remove a terminal interval of (O(M^{3/4})) integers, whose divisor-bounded coefficient mass is already (O(M^{3/4}X^\varepsilon)), and work with a compact smooth terminal profile. No endpoint may simply be discarded.

The result proved here is not the desired estimate (S(M,U)\ll M^{3/4}X^\varepsilon). It is:

1. an exact coefficient, Euler-product, cone-collar, functional-equation, and resonance derivation;
2. a proof that coefficientwise absolute aggregation cannot close the target at all scales;
3. an owner-complete isolation of the additional signed resonant estimate that would be sufficient.

## 3. Proof and derivation

### 3.1 Odd/even extraction and the character-sector ledger

If (mu^2(s)=1), write uniquely

\[
s=2^\nu n,\qquad \nu\in\{0,1\},\quad n\text{ odd and squarefree}.
\]

Because (e) is odd, (e\mid n) and (d=2^\nu n/e). Hence

\[
e>4d
\iff e^2>2^{\nu+2}n
\iff e>2^{1+\nu/2}\sqrt n,
\]

which proves (1.1). Equality cannot occur: (e=4d) is incompatible with (e) odd. In particular the strict cone is not silently changed at a boundary lattice point.

Put

\[
A_\nu=2^{1+\nu/2},\quad
\mathcal D_>=\{e\mid n:e>A_\nu\sqrt n\},\quad
\mathcal D_<=\{e\mid n:e<A_\nu^{-1}\sqrt n\},
\]

and let (\mathcal D_0) be the complementary middle divisors. Complementation (e\mapsto n/e) bijects (\mathcal D_>) with (\mathcal D_<), and

\[
\chi _4(n/e)=\chi _4(n)\chi _4(e).
\]

Consequently

\[
C(2^\nu n)=\chi _4(n)\sum_{e\in\mathcal D_<}\chi _4(e).
\tag{3.1}
\]

Let

\[
T(n)=\sum_{e\mid n}\chi _4(e)=\prod_{p\mid n}(1+\chi _4(p)),
\qquad
K_\nu(n)=\sum_{e\in\mathcal D_0}\chi _4(e).
\]

If (chi _4(n)=+1), the high and low sums agree, so

\[
C(2^\nu n)=\frac{T(n)-K_\nu(n)}2.
\tag{3.2}
\]

If (chi _4(n)=-1), the high and low sums are negatives. Complementation pairs the middle region antisymmetrically, so (K_\nu(n)=0), while

\[
C(2^\nu n)=-\sum_{e\in\mathcal D_<}\chi _4(e)
\tag{3.3}
\]

remains as a genuine tail. Thus the nonnegative complete sector (T(n)) in (3.2) and the antisymmetric negative-total-character tail (3.3) are both mandatory. In particular, the vanishing of (T(n)) when some (p\mid n) has (chi _4(p)=-1) does not imply the cone coefficient vanishes.

For an odd prime (p>4), (1.1) gives (C(p)=\chi _4(p)); for an odd prime (p>8), it gives (C(2p)=\chi _4(p)). These identities check both the negative-character tail and the changed even threshold. The finitely many smaller cases are retained directly.

### 3.2 Euler product, (p=2), and the powerful correction

Set

\[
\sigma_+=\Re(w+z),\qquad \sigma_-=\Re(w-z).
\]

At (2), squarefreeness and the oddness of (e) allow either no factor (2), or a single factor (2) in (d). The local factor of (Z) is therefore

\[
1+2^{-w-z}.
\]

Since (L(s,\chi _4)) has no Euler factor at (2), removal of the local zeta factor gives

\[
(1+2^{-w-z})(1-2^{-w-z})=1-2^{-2w-2z},
\]

proving (1.3).

At an odd prime (p), the three squarefree, coprime possibilities are (p\nmid de), (p\mid d), and (p\mid e). Their local sum is (1+x+y). Removing the local factors of (\zeta(w+z)L(w-z,\chi _4)) multiplies by ((1-x)(1-y)), and direct expansion proves (1.4).

The sums of the linear local terms (x) and (y) give the absolute domain (1.5) for (Z). Every nonconstant monomial of (H_p-1) has exponent vector among

\[
(2,0),(0,2),(1,1),(2,1),(1,2)
\]

in ((x,y)). Therefore the coefficientwise absolute prime sum converges when (sigma_+>1/2) and (sigma_->1/2); these inequalities also imply (sigma_++\sigma_->1). This proves (1.6).

Collecting terms with the same radial power (p^{-w}) gives (1.7). It also proves the convolution (2.3), because

\[
\zeta(w+z)L(w-z,\chi _4)
=\sum_{n\geq1}\frac1{n^w}
\sum_{ab=n}\chi _4(b)(b/a)^z.
\]

On (Re z=0), all ratio powers have modulus one, which proves (1.8). More explicitly, a supported (k) has the unique form (k=a^2b^3), with (b) squarefree and with the prime sets in (a) and (b) disjoint. Hence

\[
\#\{k\leq K:h_z(k)\ne0\}\ll K^{1/2},
\tag{3.4}
\]

and partial summation gives

\[
\sum_{\substack{k>K\\h_z(k)\ne0}}\frac{|h_z(k)|}{k}
\ll_\varepsilon K^{-1/2+\varepsilon}.
\tag{3.5}
\]

At (z=0), for example,

\[
h_0(p^2)=-(2+\chi _4(p)),\qquad
h_0(p^3)=1+\chi _4(p),
\tag{3.6}
\]

so already the prime squares show that no unweighted (\ell^1) conclusion follows from (1.6).

### 3.3 Strict cone, collar cost, and Mellin bandwidth

On a local face (d\asymp D) meeting (e=4d), one has (e\asymp D) and (M=de\asymp D^2). For each of (O(D)) possible (d), the collar (1.9) contains (O(D^{1/2}+1)) possible odd (e). Coprimality, squarefreeness, a product prefix, and the character can only reduce its absolute multiplicity. Thus

\[
\#\{(d,e):d\asymp D,\ |e-4d|\leq D^{1/2},\ M\leq de<U\}
\ll D^{3/2}\ll M^{3/4}.
\tag{3.7}
\]

This proves the unweighted prefix cost in Section 1. Since (de\asymp D^2), multiplication by ((de)^{-3/4}) makes the physical cost (O(1)), up to harmless divisor partitions.

Outside the collar,

\[
|\log(e/4d)|\gg D^{-1/2}.
\]

A smooth transition on this logarithmic scale has (j)-th derivative (O_j(D^{j/2})), and repeated Fourier integration by parts gives effective support (|\Im z|\ll D^{1/2}X^\varepsilon), proving (1.10). By contrast, the nearest strict lattice point (e=4d+1) satisfies

\[
\log\frac{e}{4d}=\frac1{4d}+O(D^{-2}),
\]

so a truncated hard Perron kernel cannot distinguish it with a power-saving error unless (T\gg D). This establishes the sharp-versus-collar bandwidth distinction analytically.

Faces away from (e\asymp4d) have a constant cone decision after a sufficiently fine smooth ratio partition. The (D=1) face has (O(1)) cone bandwidth and remains in the exact sum; no argument here assumes that both divisor variables are long.

### 3.4 Exact level-four transform, polar term, and branches

For a compact smooth (f) supported away from zero, Mellin inversion starts from

\[
\sum_n b_z(n)f(n)=\frac1{2\pi i}\int_{(c)}D_z(w)\widetilde f(w)\,dw.
\]

Use the primitive odd character (\chi _4) of conductor (4), whose root number is (+1), and define

\[
\Lambda_z(w)=
\pi^{-(w+z)/2}\Gamma\!\left(\frac{w+z}{2}\right)
\left(\frac4\pi\right)^{(w-z+1)/2}
\Gamma\!\left(\frac{w-z+1}{2}\right)D_z(w).
\tag{3.8}
\]

The two scalar functional equations give exactly

\[
\Lambda_z(w)=\Lambda_{-z}(1-w).
\tag{3.9}
\]

Equivalently,

\[
D_z(w)=G_z(w)D_{-z}(1-w),
\tag{3.10}
\]

where

\[
G_z(w)=4^{1/2-w+z}\pi^{2w-1}
\frac{
\Gamma((1-w-z)/2)\Gamma((2-w+z)/2)}
{\Gamma((w+z)/2)\Gamma((1+w-z)/2)}.
\tag{3.11}
\]

Moving the contour across the sole Dirichlet-series pole (w=1-z) gives

\[
\sum_n b_z(n)f(n)
=L(1-2z,\chi _4)\widetilde f(1-z)
+\sum_m b_{-z}(m)\,\mathcal V_zf(m),
\tag{3.12}
\]

with the exact Mellin-Barnes kernel

\[
\mathcal V_zf(m)=\frac1{2\pi i}\int_{(c_*)}
4^{u-1/2+z}\pi^{1-2u}
\frac{\Gamma((u-z)/2)\Gamma((1+u+z)/2)}
{\Gamma((1-u+z)/2)\Gamma((2-u-z)/2)}
\widetilde f(1-u)m^{-u}\,du.
\tag{3.13}
\]

Formula (3.13), rather than a single selected asymptotic term, is the required complex-order transform: it fixes the conductor and cusp normalization and retains every Bessel branch. Uniform contour movement must avoid all displayed gamma poles and must be proved uniformly for every order furnished by (1.10) and (2.4).

At (z=0), the duplication formula reduces (3.8) to

\[
\Lambda_0(w)=4\pi^{-w}\Gamma(w)D_0(w).
\]

The inverse kernel in (3.13) is then exactly (\pi J_0(2\pi\sqrt y)), proving (1.11). Its two branches are visible from

\[
\pi J_0(2\pi\sqrt y)
=\frac{y^{-1/4}}2
\left[e(\sqrt y-\tfrac18)+e(-\sqrt y+\tfrac18)\right]
+O(y^{-3/4}).
\tag{3.14}
\]

Thus neither oscillatory direction may be omitted. The polar term in (3.12) is also explicit. After the (H)-convolution it carries the absolutely convergent factor

\[
\sum_k h_z(k)k^{z-1}=H(1-z,z)
\tag{3.15}
\]

on the unitary line. Moreover the phase derivative in its radial integral is dominated by (\sqrt N/\sqrt M), since the cone orders are at most (D^{1/2}X^\varepsilon\ll M^{1/4}X^\varepsilon) on a boundary face and (M\leq R^2). First-derivative integration, including the two terminal boundary terms of a clipped prefix, makes the polar contribution target-safe. It cannot cancel or replace the resonant dual owner below.

### 3.5 Exact resonance centre, width, and amplitude

Insert the exact convolution before transforming:

\[
\sum_n a_z(n)F(n)
=\sum_k h_z(k)\sum_\ell b_z(\ell)F(k\ell).
\tag{3.16}
\]

At (z=0), substitute (y=kx) into the dual integral in (1.11). It becomes

\[
\frac\pi k\int F(y)J_0\!\left(2\pi\sqrt{my/k}\right)\,dy.
\tag{3.17}
\]

For

\[
F(y)=1_{[M,U)}(y)V_{\rm low}(R^2y/N)e(+\sqrt{Ny}),
\]

the negative Bessel branch has phase

\[
\Phi_{k,m}(y)=\left(\sqrt N-\sqrt{m/k}\right)\sqrt y.
\tag{3.18}
\]

The conductor is still (4); (k) has only dilated the radial test. Hence (m=kN), not a modulus-dependent alternative, makes (3.18) identically zero. If (m=kN+j), then

\[
\sqrt N-\sqrt{m/k}
=-\frac{j}{2k\sqrt N}+O\!\left(\frac{j^2}{k^2N^{3/2}}\right),
\tag{3.19}
\]

and the phase varies by (O(1)) across a length-(M) profile precisely when

\[
|j|\ll k\sqrt{N/M}.
\]

This proves (1.14). Outside a fixed enlargement of this band, repeated first-derivative integration gives rapid decay for a smooth radial profile; approximation by bounded-variation profiles retains the endpoint terms for every (U).

At (m\asymp kN), (3.14) gives the per-term resonant capacity

\[
\frac1k\int_{y\asymp M}(Ny)^{-1/4}\,dy
\asymp \frac{M^{3/4}}{kN^{1/4}}
\asymp\frac{M^{3/4}}{kR}.
\tag{3.20}
\]

There are (O(k\sqrt{N/M})=O(kR^2/\sqrt M)) integral values of (m) in the band. Taking their moduli gives

\[
\frac{M^{3/4}}{kR}\cdot\frac{kR^2}{\sqrt M}
=R M^{1/4}
=M^{3/4}\frac R{\sqrt M},
\tag{3.21}
\]

independently of (k). The positive Bessel branch has phase coefficient (\sqrt N+\sqrt{m/k}) and is nonstationary. For a fixed (j), (3.19) also shows that the (m=kN+j) family rotates more and more slowly as (k) grows; for (j=0) it does not rotate at all. This is why neither off-resonance integration nor averaging a moving centre is available.

### 3.6 All-scale power and the powerful-index obstruction

For the bare factor, the direct divisor-bound estimate is (M^{1+\varepsilon}), which is the target (M^{3/4}) times (M^{1/4}). The transformed absolute estimate (3.21) is the target times (R/\sqrt M). Their minimum is (1.15). The increasing and decreasing powers meet when

\[
M^{1/4}=R M^{-1/2},
\]

namely (M=R^{4/3}), where the common loss is (R^{1/3}). At (M\asymp R^2), the bare transformed bound is only target-borderline. This proves the bare all-scale capacity assertion.

For the full convolution, the trivial (k)-channel costs (M/k), while (3.21) costs (RM^{1/4}). Therefore termwise modulus gives

\[
\sum_{\substack{k\leq M\\h_z(k)\ne0}}
|h_z(k)|\min\!\left(\frac Mk,RM^{1/4}\right).
\tag{3.22}
\]

When (M\geq R^{4/3}), split at

\[
K=\frac{M^{3/4}}R.
\]

Using (3.4) and (3.5), (3.22) is at best

\[
\ll_\varepsilon
RM^{1/4}K^{1/2+\varepsilon}
+M K^{-1/2+\varepsilon}
\ll_\varepsilon R^{1/2}M^{5/8}X^\varepsilon.
\tag{3.23}
\]

Division by (M^{3/4}) proves (1.16). If (M<R^{4/3}), the split point is below (1), so the direct estimate (M^{1+\varepsilon}), with loss (M^{1/4}), is the available one. In particular:

- at (M=R^{4/3}), even the bare factor loses (R^{1/3});
- on lower growing blocks, the direct loss (M^{1/4}) remains;
- at (M\asymp R^2), the bare factor is borderline but termwise powerful aggregation loses (R^{1/4});
- bounded (M), including the genuinely finite (D=1) edge, is harmless, but it does not repair the intermediate or top ranges.

The estimate (3.23) grants the transform its favorable stationary-phase size and grants uniform unitary-order constants. Thus a fixed-order or gamma-uniformity refinement alone cannot remove the displayed obstruction. Conversely, (3.23) is not a lower bound: cancellation among the actual values (h_z(k)b_{-z}(m)), among nearby (m), and across ratio orders could be decisive. That cancellation is exactly the missing owner.

## 4. First doubtful or unproved step

After the collar, local ratio partition, exact convolution, and exact transform, the first unproved step is the following signed resonant aggregation estimate.

Let (\Omega_D(\tau,t)) denote the actual Mellin weight produced by the target-safe cone cutoff and the smooth (d\asymp D) partition; it has rapidly decreasing (t)-tails and effective (|\tau|\ll D^{1/2}X^\varepsilon). Put

\[
z=i(\tau+t/2),
\]

and let (F_{M,U,t}) be the exact radial profile in (2.6), transferred to the (s)-variable. Define

\[
\mathcal J_{z;k,m}(M,U)
=\mathcal V_z\bigl[x\mapsto F_{M,U,t}(kx)\bigr](m)
\tag{4.1}
\]

by the full Mellin-Barnes kernel (3.13), not by one selected Bessel branch. The required new statement is

\[
\boxed{
\sup_{M\leq U\leq B_M}
\left|
\sum_D\iint \Omega_D(\tau,t)
\sum_{\substack{k\leq 2M\\h_z(k)\ne0}}h_z(k)
\sum_{\substack{m\geq1\\
|m-kN|\leq Ck\sqrt{N/M}\,X^\varepsilon}}
b_{-z}(m)\mathcal J_{z;k,m}(M,U)
\,d\tau\,dt
\right|
\ll_{\varepsilon,V}M^{3/4}X^\varepsilon .}
\tag{4.2}
\]

An equivalent version may include all (m) and the exact kernel; then the positive and off-resonant branches must be shown target-safe uniformly rather than deleted. The polar contribution is the explicit term in (3.12), aggregated as in (3.15), and must remain outside or inside (4.2) by declaration.

No estimate supplied by the Euler product proves (4.2). Absolute convergence of (H) places a weight (k^{-1/2-\delta}), whereas the resonant band length cancels the transform's (1/k) and leaves the unweighted channel capacity (3.21). Taking absolute values in (k), in (m), or in the Mellin orders reproduces (3.22)-(3.23).

The first doubtful step is therefore any assertion of (4.2) without a new arithmetic correlation theorem for the exact pair

\[
h_z(k)b_{-z}(kN+j),
\qquad |j|\ll k\sqrt{N/M},
\]

uniform in (N=\lfloor X\rfloor), (M,U,D,z), and the prescribed profile. Square-root cancellation for arbitrary coefficients, a cosine replacement, centre averaging, or assigning modulus (4k) is not such a theorem.

## 5. Required control tests and outcomes

All controls below were analytical; no numerical experiment was used.

| Control | Outcome | Reason |
|---|---|---|
| `t1_exact_extraction_and_prefix_target` | Pass | Equation (1.1) is exact for both parities, and (2.1) keeps every half-open (U). |
| `squarefree_coprime_even_odd_character_and_cone` | Pass | The three local prime states and the exceptional (2)-factor are derived explicitly; (e=4d) is impossible by parity. |
| `divisor_pairing_chi4_sector_ledger` | Pass | Equations (3.1)-(3.3) retain the complete (\chi_4(n)=+1) sector and the mandatory antisymmetric (\chi_4(n)=-1) tail. |
| `ratio_Mellin_Euler_product_p2_and_H` | Pass | Equations (1.2)-(1.8) give the exact (p=2) factor, odd factors, convergence regions, support, and coefficient sizes. |
| `target_safe_cone_collar_and_ratio_bandwidth` | Pass | The collar has prefix capacity (D^{3/2}=M^{3/4}); smooth and hard bandwidths are (D^{1/2}X^\varepsilon) and (\gg D), respectively. |
| `level_four_generalized_divisor_Voronoi_kernel` | Pass as an identity; fail as a target proof | Equations (3.8)-(3.14) fix conductor (4), root number, polar term, full kernel, and both (J_0) branches. |
| `uniform_complex_order_and_Bessel_asymptotics` | Retained, not assumed | The exact kernel (3.13) is valid order by order and (4.2) requires the full uniform range. The power obstruction is already present at (z=0), so fixed-order asymptotics do not close it. |
| `H_powerful_coefficients_tail_and_signed_aggregation` | Fail as currently justified | Powerful support gives weighted convergence only. Termwise optimized aggregation yields (3.23); the signed estimate (4.2) is unproved. |
| `dual_resonance_centre_width_amplitude_and_off_resonance` | Pass | Centre (kN), width (k\sqrt{N/M}), and per-term amplitude (M^{3/4}/(kR)) are derived in (3.18)-(3.21); the other branch is nonstationary. |
| `all_M_D_E_capacity_and_R4over3_barrier` | Pass as a no-go calculation | The bare loss peaks at (R^{1/3}); full termwise (H) aggregation also loses a positive power, including at the top block. |
| `clipped_prefix_profile_terminal_endpoint` | Pass in the reduction | The bounded-variation limit or a target-sized terminal collar retains boundary terms uniformly in (U); the survivor takes a supremum over (U). |
| `t1_D1_prime_even_and_slow_family_controls` | Pass | (D=1) is not removed; (C(p)=\chi_4(p)), (C(2p)=\chi_4(p)) in their exact strict ranges; (m=kN+j) is slowly rotating for fixed (j). |
| `individual_positive_direction_and_fixed_centre` | Pass | The external sign is always (+); only the negative Bessel branch resonates, and (N) is fixed rather than averaged. |
| exact radicals | Pass | Since (k,m,N) are integers, (m=kN) gives (\sqrt{m/k}=\sqrt N) identically, irrespective of whether (N) is a square. |
| primes and even squarefree inputs | Pass | The prime identities above show that neither negative character values nor the even threshold may be suppressed. |
| false unsigned/adversarial analogue | Pass as a warning | At (z=0), (b_0=r_2/4\geq0) and the negative (J_0) branch has a coherent resonant capacity. Only the exact (\chi_4) and signed (h_z) structure can remove it; absolute values erase the needed distinction. No lower bound for the original cone sum is asserted. |
| termwise dual moduli | Pass | The primitive conductor stays (4) in (3.17); the residual index moves the centre to (kN) but does not create modulus (4k). |
| `Round138_cross_and_downstream_scope` | Pass | This report claims only the displayed (t=1) face. It makes no claim about any independent cross owner, any (t\geq2) layer, M1/M2, endpoints downstream of this prefix, M9, a bridge, or the quarter exponent. |

## 6. Dependencies and exact artifacts used

This was a statement-only analytic derivation. The only artifacts read were:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/blind_statement.md`;
3. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/briefs/blind_t1_squarefree_voronoi_rederivation.md`.

No proof graph, proof draft, strategy file, nonblind Round 138-147 artifact, sibling report, web source, or numerical computation was consulted. The only standard identities used were written out in full: the scalar functional equations for (\zeta) and the primitive odd (L(s,\chi _4)), the gamma duplication formula, Mellin inversion, and the elementary (J_0) asymptotic.

## 7. Recommended state effect

**Retain/revise; do not promote the prefix target.** Promote only the exact algebraic and analytic reductions after independent seam checking: (1.1), (1.2)-(1.8), the collar and bandwidth calculation, the completed level-four transform (3.8)-(3.13), and the resonance ledger (1.14), (3.20).

Record an exact no-go against any argument that uses absolute convergence of (H), triangle inequality in the powerful index, or the bare transform/trivial minimum as though it met the target. The sole viable survivor identified here is the joint signed correlation estimate (4.2), with full complex-order, prefix, polar, and branch uniformity. Until that estimate or a different mechanism is proved, the (t=1) squarefree-cone prefix remains open.
