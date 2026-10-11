# Round227: independent Mellin-phase report

Campaign: `gc-complete-joint-spectral-remainder`. Task/role: `blind_mellin_phase`, statement-only independent derivation. Generated: 2026-09-28T07:30:21+08:00. Graph hash: deliberately unavailable under the input-isolation contract; no graph was read. Status: candidate evidence only.

## 1. Result

The first potentially doubtful step is applying a stationary-phase expansion uniformly when its critical point approaches a moving support endpoint. No such expansion is assumed below. A change to logarithmic coordinates proves the required global upper bound directly, and an expansion is used only with a fixed positive interior margin.

Let

\[
D_d=(d+1/2,2),\qquad g_d(y)=-y f_d'(y).
\]

The phase has at most one critical point on this overlap. It exists exactly when

\[
\tau/L\in G_d^\circ
 :=\bigl(g_d(2),g_d(d+1/2)\bigr),
\]

and is then the unique point \(y_*=g_d^{-1}(\tau/L)\). In particular, its frequency is positive and its curvature is positive. This describes the phase on the entire overlap; a contribution can vanish if the amplitude vanishes at its critical point.

For every fixed \(b\geq0\), uniformly for \(0<d<3/2\) and \(L\geq1\),

\[
M_b(d,L):=\int_{\mathbb R}(1+|\tau|)^b|K_d(L,\tau)|\,d\tau
 \ll_b L^{b+1/2}.
\tag{1}
\]

The constant depends on finitely many of the stipulated amplitude derivative bounds. More strongly, for every integer \(M\geq0\), with \(h=3/2-d\),

\[
M_b(d,L)\ll_{b,M}h^M L^{b+1/2}.
\tag{2}
\]

For each fixed \(d\) and its fixed amplitude, there is the precise limit

\[
\lim_{L\to\infty}L^{-b-1/2}M_b(d,L)
 =\sqrt{2\pi}\int_{D_d}g_d(y)^b |a_d(y)|
                 \sqrt{-y g_d'(y)}\,dy.
\tag{3}
\]

Consequently the order is \(\Theta_{d,a_d,b}(L^{b+1/2})\) for every fixed nonzero amplitude. A positive uniform lower bound for an arbitrary allowed family is false. A sufficient uniform interior nonvanishing hypothesis is stated next.

## 2. Exact hypotheses

The assumptions used for (1)--(2) are exactly those in the packet: \(0<d<3/2\), \(L\geq1\), \(\tau\in\mathbb R\); the zero-extended amplitude is smooth, has support in \(D_d\), and for every integer \(j\geq0\),

\[
\sup_d\sup_y |\partial_y^j a_d(y)|\leq A_j<\infty.
\]

The amplitudes may be complex. They are indexed by \(d\), not by \(L\). No smoothness in \(d\) is required. Formula (3) fixes \(d\) and \(a_d\) before taking the limit.

A sufficient additional hypothesis for a matching lower bound uniform in a selected family of \(d\)'s is the existence of constants \(\alpha,\ell,\eta>0\) and intervals \(I_d\subset D_d\) such that

\[
|I_d|\geq\ell,\qquad
\operatorname{dist}(I_d,\partial D_d)\geq\eta,\qquad
|a_d(y)|\geq\alpha\quad(y\in I_d).
\tag{4}
\]

Under (4), \(M_b(d,L)\gg L^{b+1/2}\) for \(L\geq L_0\), with constants independent of the selected \(d\). These hypotheses necessarily exclude arbitrarily shrinking overlap.

All integrals over frequency are over the whole real line. There are no arithmetic hypotheses or arithmetic conclusions.

## 3. Proof and derivation

### Algebra and uniform curvature

Put \(u=y-d\). On the closure of \(D_d\), both \(y\) and \(u\) lie in \([1/2,2]\). Rationalization and an integral identity give

\[
f_d(y)=\frac1{\sqrt y+\sqrt u}
 =\frac12\int_0^1(y-\theta d)^{-1/2}\,d\theta,
\]

\[
f_d'(y)=-\frac1{2\sqrt y\sqrt u(\sqrt y+\sqrt u)},\qquad
g_d(y)=\frac{\sqrt y}{2\sqrt u(\sqrt y+\sqrt u)}
 =\frac y4\int_0^1(y-\theta d)^{-3/2}\,d\theta,
\]

\[
-g_d'(y)=\frac18\int_0^1
 (y+2\theta d)(y-\theta d)^{-5/2}\,d\theta
 \geq\frac1{8y^{3/2}}>0.
\tag{5}
\]

Every fixed derivative of these functions is uniformly bounded on the overlap, including as \(d\downarrow0\). In particular,

\[
c_0:=\frac1{4\sqrt2}\leq g_d(y)\leq
c_1:=\frac{\sqrt2}{3}.
\tag{6}
\]

For the upper bound, write \(s=\sqrt y\), \(t=\sqrt u\). Then
\(g=(2t)^{-1}s/(s+t)\), with \(t\geq1/\sqrt2\), \(s\leq\sqrt2\), and hence \(s/(s+t)\leq2/3\). The lower bound follows from the integral expression or from \(t\leq s\).

For \(r=\tau/L\), the normalized phase \(\phi_{d,r}=f_d+r\log y\) satisfies

\[
\phi_{d,r}'(y)=\frac{r-g_d(y)}y.
\]

The strict decrease of \(g_d\) proves the stationary-set claim. At its critical point,

\[
\phi_{d,r}''(y_*)=-\frac{g_d'(y_*)}{y_*}
 \geq\frac1{8y_*^{5/2}}\geq\frac1{32\sqrt2}.
\tag{7}
\]

For a bound that does not depend on the critical point remaining interior, use \(t=\log y\),

\[
F_d(t)=f_d(e^t),\quad B_d(t)=e^t a_d(e^t),\quad
K_d(L,\tau)=\int B_d(t)e^{i[LF_d(t)+\tau t]}\,dt.
\]

The integration interval is
\(T_d=(\log(d+1/2),\log2)\subset[\log(1/2),\log2]\).
On it,

\[
F_d'(t)=-g_d(e^t),\qquad
F_d''(t)=-e^t g_d'(e^t)\geq\frac1{8\sqrt2}.
\tag{8}
\]

Thus the full logarithmic phase has curvature at least \(L/(8\sqrt2)\), independently of \(\tau\). The zero-extended \(B_d\) has uniformly bounded derivatives of every fixed order.

### Uniform stationary and nonstationary bounds

Equation (8) gives

\[
|K_d(L,\tau)|\ll L^{-1/2}\quad\text{for every }\tau.
\tag{9}
\]

For completeness, split the interval where the absolute first derivative of the full phase is at most \(\sqrt L\) from its complement. Since this derivative increases at rate at least \(cL\), that central interval has length \(O(L^{-1/2})\). On either complementary interval the derivative is monotone, has constant sign and has magnitude at least \(\sqrt L\). Integration by parts there bounds the integral by
\(O(L^{-1/2})(\|B_d\|_\infty+\|B_d'\|_1)\). This proves (9), even if the central interval meets or misses an endpoint.

More precisely, if
\(\Delta=\operatorname{dist}(\tau,L\overline G_d)>0\), the same first-derivative argument gives

\[
|K_d(L,\tau)|\ll\min(L^{-1/2},\Delta^{-1}).
\tag{10}
\]

Outside the fixed positive frequency cone

\[
\mathcal C_L=[c_0L/2,2c_1L],
\]

one has \(|\tau-Lg_d(e^t)|\gg L+|\tau|\). Repeated integration by parts, using bounded higher derivatives of \(F_d\), gives for every integer \(N\geq0\)

\[
|K_d(L,\tau)|\ll_N(L+|\tau|)^{-N}
 \qquad(\tau\notin\mathcal C_L).
\tag{11}
\]

There are no boundary terms because of the smooth zero extension. Each integration-by-parts step supplies a factor \((L+|\tau|)^{-1}\). Differentiating the resulting coefficients preserves that factor: derivatives of the phase derivative are \(O_j(L)\), and \(L/(L+|\tau|)\leq1\).

Integrating (9) over \(\mathcal C_L\) gives \(O(L^{b+1/2})\). For an integer \(N>b+1\), (11) bounds the remaining weighted integral by

\[
\ll_{b,N}\int_{\mathbb R}(L+|\tau|)^{b-N}\,d\tau
 \ll_{b,N}L^{b+1-N}.
\]

This proves (1).

Write \(h=3/2-d\). Taylor's integral formula from either zero-extension endpoint gives, for all integers \(j,M\geq0\),

\[
\|a_d^{(j)}\|_\infty\leq A_{j+M}h^M/M!.
\tag{12}
\]

The corresponding bounds for every required derivative of \(B_d\) also gain \(h^M\). The preceding arguments are linear in the relevant amplitude seminorms. Repeating them with (12) proves (2).

### Interior leading phase and coefficient

Let \(r\) range in an interior interval for which \(y_*=g_d^{-1}(r)\) stays a positive distance from both endpoints. Define

\[
\Psi_d(r)=f_d(y_*)+r\log y_*.
\]

Then

\[
K_d(L,Lr)=
 a_d(y_*)\sqrt{\frac{2\pi y_*}{L[-g_d'(y_*)]}}
 \exp\{iL\Psi_d(r)+i\pi/4\}+O(L^{-3/2}).
\tag{13}
\]

The remainder is uniform under uniform positive interior margins and uniform derivative bounds. Here is a direct justification of that scope. In logarithmic coordinates set \(\psi(t)=F_d(t)+rt\). Around its critical point introduce

\[
v=\operatorname{sgn}(t-t_*)\sqrt{2[\psi(t)-\psi(t_*)]}.
\]

By (8), this is a smooth local coordinate with uniformly bounded required derivatives and \(dv/dt|_{t_*}=\sqrt{F_d''(t_*)}\). A cutoff in a fixed small neighborhood reduces the integral to a smooth compactly supported amplitude \(c(v)\) against \(e^{iLv^2/2}\). Subtract \(c(0)\chi(v)+c'(0)v\chi(v)\), for an even cutoff \(\chi=1\) near zero. The odd term integrates to zero. The constant term has integral \(e^{i\pi/4}\sqrt{2\pi/L}\) up to rapidly decreasing errors; this Gaussian identity follows by positive Gaussian regularization. The remainder is \(v^2R(v)\). One integration by parts writes its integral as \(-(iL)^{-1}\int(R+vR')e^{iLv^2/2}dv\), which is \(O(L^{-3/2})\) by the already proved curvature bound. The part outside the neighborhood is nonstationary and rapidly decreasing. Finally
\(c(0)=y_*a_d(y_*)/\sqrt{-y_*g_d'(y_*)}\), giving (13).

The dependence on frequency ratio is nontrivial:

\[
\Psi_d'(r)=\log y_*(r),\qquad
\Psi_d''(r)=\frac1{y_*(r)g_d'(y_*(r))}<0.
\tag{14}
\]

An explicit interior example is \(d=1/2\), with a smooth bump \(a\) supported in \((5/4,7/4)\), equal to one on \([7/5,8/5]\). For
\(r\in[g_{1/2}(8/5),g_{1/2}(7/5)]\), (13) has a positive coefficient bounded above and below by fixed multiples of \(L^{-1/2}\). It therefore provides the requested leading phase and size on a fixed nonvanishing example.

For fixed \(d\), apply (13) pointwise in \(r\) when the stationary point belongs to \(D_d\). If it does not, the integral is nonstationary on the compact amplitude support. The two endpoint ratios are irrelevant to integration. After \(\tau=Lr\),

\[
L^{-b-1/2}M_b(d,L)
 =\int_{\mathbb R}(|r|+L^{-1})^b\sqrt L\,|K_d(L,Lr)|\,dr.
\]

On the fixed cone \([c_0/2,2c_1]\), (9) supplies an integrable domination. Outside it, (11) makes the integral tend to zero. Dominated convergence and then the substitution \(r=g_d(y)\), reversing endpoints, yield

\[
\sqrt{2\pi}\int_{g_d(2)}^{g_d(d+1/2)}
 r^b|a_d(y_*)|\sqrt{\frac{y_*}{-g_d'(y_*)}}\,dr
 =\sqrt{2\pi}\int_{D_d}
 g_d(y)^b|a_d(y)|\sqrt{-y g_d'(y)}\,dy,
\]

which is (3). Its right side is positive exactly when the smooth amplitude is nonzero. Under (4), (13) is uniform on the corresponding intervals of ratios. Their lengths are at least \(\ell/(16\sqrt2)\) by (5), and the leading coefficient is bounded below uniformly. Integration there proves the stated uniform lower bound for sufficiently large \(L\).

### Transform mass versus signed values

With the sign convention used here, Fourier inversion is

\[
B_d(t)e^{iLF_d(t)}
 =\frac1{2\pi}\int_{\mathbb R}K_d(L,\tau)e^{-i\tau t}\,d\tau.
\tag{15}
\]

These integrals are absolutely convergent for each fixed \(L\) by smooth compact support and (11). The inverse transform has modulus \(|B_d(t)|\), whereas its absolute-mass upper certificate can grow like \(L^{1/2}\). Also \(K_d(L,0)=O_N(L^{-N})\) by (11). Neither the lower bound for absolute transform mass nor a triangle-inequality upper certificate is a lower bound for the original signed integral or for an inverse transform.

For the explicit \(d=1/2\) interior bump above, \(B_d(0)=a_d(1)=0\). Hence \(\int K_d(L,\tau)d\tau=0\) exactly by (15), even though \(\int|K_d(L,\tau)|d\tau\asymp L^{1/2}\).

## 4. First doubtful or unproved step

No unproved step remains in the scoped analytic statements (1)--(15). The initially doubtful extension of an interior stationary-phase expansion to a moving endpoint was avoided for the uniform upper bound. Equation (13) is asserted uniformly only under a positive interior margin; it is not an unrestricted moving-endpoint asymptotic.

A uniform positive lower bound without (4) or another quantitative nonvanishing condition would be the first invalid additional step. Zero amplitude disproves it immediately, and (2) rules it out through shrinking overlap even for many nonzero families. No conclusion concerning any other mathematical application is supplied or assumed.

## 5. Required controls and outcomes

All controls here are analytic; no experiments, symbolic software, numerical calculations, or web sources were used.

1. **Zero/empty amplitude.** If \(a_d\equiv0\), then \(K_d\equiv0\), both sides of (3) are zero, and no positive lower bound holds. If one extends the support condition to \(d\geq3/2\), the overlap is empty and the same conclusion follows. For the stipulated open range of \(d\), the geometric overlap itself is nonempty.

2. **Zero and negative frequencies.** There is no stationary point for \(\tau\leq0\); in particular \(K_d(L,0)=O_N(L^{-N})\) uniformly. This controls the sign in the stationary equation.

3. **The limit \(d\downarrow0\).** Uniformly with every fixed derivative on admissible compact sets,
   \[
   f_d(y)\to f_0(y)=\frac1{2\sqrt y},\quad
   g_d(y)\to g_0(y)=\frac1{4\sqrt y}.
   \]
   The limiting stationary point is \(y_*=(16r^2)^{-1}\), when it lies in \((1/2,2)\), and
   \[
   \Psi_0(r)=2r[1-\log(4r)],\qquad
   \Psi_0''(r)=-2/r<0.
   \]
   The leading coefficient in (13) tends to
   \(4\sqrt\pi\,a_0(y_*)y_*^{5/4}L^{-1/2}\) if an amplitude limit exists. No amplitude limit is assumed for (1)--(2). The integral representation proves the absence of a hidden \(d^{-1}\) loss.

4. **Support endpoints.** The curvature proof (8)--(9) covers a critical point arbitrarily close to either endpoint uniformly. At the exact endpoint ratios \(r=g_d(d+1/2)\) or \(r=g_d(2)\), one can in fact obtain \(O_N(L^{-N})\) uniformly from flatness. In logarithmic distance \(s\) to that endpoint, \(|\psi'|\geq cs\), all amplitude derivatives are \(O_M(s^M)\), and derivatives of \(1/\psi'\) of order \(j\) are \(O_j(s^{-j-1})\). After \(N\) integrations by parts the integrand is \(L^{-N}O(s^{M-2N})\). Choose \(M\geq2N+1\); boundary terms vanish and the remaining integral is uniformly bounded. This verifies the endpoint assertion without pretending that the endpoint is an interior stationary point.

5. **Shrinking overlap.** Equation (12) proves (2). A concrete nonzero allowed family is
   \[
   a_d(y)=e^{-1/h^2}\eta\bigl((y-d-1/2)/h\bigr),
   \qquad h=3/2-d,
   \]
   where \(\eta\in C_c^\infty((0,1))\) is a fixed nonzero bump. Every fixed derivative is uniformly bounded because \(h^{-j}e^{-1/h^2}\) is bounded. This family makes a \(d\)-uniform positive lower constant impossible.

6. **Fixed interior control.** The \(d=1/2\) bump in Section 3 has exactly one contributing stationary point throughout a ratio interval of positive length, positive curvature, the \(+\pi/4\) phase correction, size \(\asymp L^{-1/2}\), and weighted absolute mass \(\asymp L^{b+1/2}\). Its unweighted signed frequency integral is nevertheless exactly zero. These outcomes verify the required distinction between absolute mass and signed reconstruction.

## 6. Dependencies and exact artifacts used

Exactly two input files were read:

1. `protocol.md` — SHA256 `F26FB038496B5AE171B3352E7D02BA1A4B7DD808EF31BF8620E6D4930CEA9D5A`.
2. `rounds/codex-managed/gc-complete-joint-spectral-remainder/briefs/blind_mellin_phase_statement.md` — SHA256 `8F4F90D6CB580FC9485729690753D76C7BC64B7D79085E5E710E7FBD5F9AE49A`.

Input isolation: no graph, campaign manifest, strategy, other brief, external source, report, control, or review was read. The visible inherited context contains the user's repository instructions, general tool instructions, and the conductor's task assignment; it contains no earlier mathematical derivation of this phase task. This is a statement-only rederivation within that disclosed context, not a claim of erasing inherited instructions. The protocol's general target was visible because that file was expressly allowed, but no application to it was attempted.

File operations were limited to reading/hashing the two inputs and writing/hashing this assigned report. Hashing is provenance, not a mathematical experiment. There are no imported theorem dependencies: the needed oscillatory estimates and stationary-phase coefficient were derived above.

## 7. Recommended state effect

**Retain** this report as independently derived analytic evidence, subject to the conductor's required seam review. It supplies a uniform upper certificate, an exact fixed-amplitude absolute-mass asymptotic, a quantitatively scoped uniform lower bound, and endpoint/no-lower-bound controls. No graph promotion or application follows automatically. No authoritative state, proof draft, validation matrix, synthesis, or other task artifact was edited. The assigned task ends with the report's external SHA256; no successor work is begun.
