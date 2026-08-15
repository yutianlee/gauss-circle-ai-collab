# Round 43 explicit amplitude packet

This is the frozen statement for isolated validation. It is not an
accepted proof and does not authorize reading another Round-43 artifact.

Fix

\[
b=\frac1{\log(2X)},\qquad
r=\frac54-\frac{a+b}{2},\qquad
p=\frac54+\frac{a+b}{2},
\]

on the accepted contour (a+b<1/2), (a/2+b<1/4). Let

\[
D_j=2^{-j}\lfloor\sqrt X\rfloor,\qquad
H_j=\lfloor D_jX^{-1/4}\rfloor,
\]

and let (0\le j\le J_X) be exactly the active scales (H_j\ge1).
Then (J_X+1\ll\log(2X)).

## Frozen finite family

After the accepted global endpoint, side, arithmetic, artificial, axial,
connector-axis, collision, corner, and height-limit routing, the beta-owned
compact terminal remainder is assumed to have the following explicit
finite form. There is an index set \(\mathfrak T\), of cardinality bounded
independently of (X), partitioned into singular and smooth types. For
each \(\tau\in\mathfrak T\):

1. (M_\tau(L,\beta)) is supported in
   \(|L|+|\beta|\le C_0\), independent of (x,j,h,q), apart from a
   monomial of fixed degree in the logarithms of (h,q,D_j,H_j+1,x).
   For (k\le1),
   \[
   |\partial_L^kM_\tau(L,\beta)|
   \le C_\tau\log^{C_\tau}(2Xhq).
   \]
   It includes the exact unit phase
   \(e^{i\{(L+\beta)\log(4/\pi)-\beta\log\pi\}}\), exact compact gamma
   ratios, the hierarchical beta/central-alpha masks, and any fixed
   connector derivative assigned to this terminal stratum.
2. The modulated height profile is
   \[
   p_{j,x}(\nu)=
   e^{i\gamma_{j,x}\nu}\widehat\phi(b+i\nu),\qquad
   \gamma_{j,x}=\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x}.
   \]
   Uniformly in active (j) and (1\le x\le N_X\),
   \[
   \|p\|_1+\|p'\|_\infty+\|(1+|\nu|)p(\nu)\|_1
   +\sup_\nu(1+|\nu|)^3|p(\nu)|\ll\log^C(2X).
   \]
3. A singular type occurs only for the (j=0) hard (1/u) top. A
   smooth type has a normalized profile (W_\tau(L-\nu)), where the
   required derivatives have a uniform fixed Schwartz seminorm
   (\ll\log^C(2X)). This includes the regular top remainder and the
   interior dyadic profiles.

Put

\[
A=-1-\frac b2-i(L+\beta),\qquad
D=-1-\frac b2-i\left(\frac{L+\nu}{2}+\beta\right),
\]

and

\[
g_{\tau,j,h,q,x}(L,\beta)=M_\tau(L,\beta)
e^{iL\log(D_j/(2q\sqrt{Xx}))}e^{-i\beta\log(hqx)}.
\]

The singular functional is exactly

\[
\mathsf P_\tau=
\frac{g_\tau(L,\beta)p_{j,x}(L)}A
-\frac{ig_\tau(L,\beta)}{2\pi}
\int_{\mathbb R}\frac{p_{j,x}(\nu)-p_{j,x}(L)}
{(L-\nu)D}\,d\nu,
\]

and a smooth functional is

\[
\mathsf S_\tau=
\frac{g_\tau(L,\beta)}{2\pi}
\int_{\mathbb R}\frac{p_{j,x}(\nu)W_\tau(L-\nu)}D\,d\nu.
\]

Define

\[
\begin{aligned}
\mathcal A_{\rm db}(x)={}&-\pi i
\sum_{j=0}^{J_X}\sum_{h,q\ge1}\chi_4(q)h^{-r}q^{-p}
\left(\frac{D_j}{2\sqrt X}\right)^a(H_j+1)^b\\
&\times\sum_{\tau\in\mathfrak T}
\int_{\mathbb R^2}\frac{dL\,d\beta}{(2\pi)^2}
\begin{cases}
\mathbf1_{j=0}\mathsf P_\tau,&\tau\text{ singular},\\
\mathsf S_\tau,&\tau\text{ smooth}.
\end{cases}
\end{aligned}
\]

The routing assertion to be audited separately is that the actual compact
remainder is exactly this family: no endpoint, side, arithmetic,
artificial-pole, axial, connector-axis, collision, or corner module is
inserted again. The same-mask identity (G-E_1-R_1=0) has already removed
all common cutoff derivatives. Internal alpha-partition derivatives cancel
between the central and large-alpha complements before this family is
frozen.

## Frozen theorem

Prove or refute

\[
\boxed{
\sup_{1\le x\le N_X}
\{|\mathcal A_{\rm db}(x)|+x|\mathcal A'_{\rm db}(x)|\}
\ll\log^C(2X).}
\]

If true, the already accepted Round-42 radial-BV reduction gives

\[
\sqrt X\int_1^{N_X}x^{-3/2-b/2}e(\sqrt{Xx})
\mathcal A_{\rm db}(x)\,dx\ll\log^C(2X),
\]

with full radial endpoint coefficients. Restoring the external factor
gives (O_\varepsilon(X^{1/4+\varepsilon})\).

An isolated analytic proof may use only the displayed family and
seminorms. A separate line audit must verify that the actual routed
operator maps to this family and that all modules are counted once.

