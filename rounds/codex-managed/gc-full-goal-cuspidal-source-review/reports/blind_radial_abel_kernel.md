# Round229: independent scalar radial Abel kernel

## 1. Result: lemma, scope, and isolation disclosure

Campaign: `gc-full-goal-cuspidal-source-review`. Task: `blind_radial_abel_kernel`. Role: statement-only independent analytic rederivation. Generated: 2026-09-28 23:53:51 UTC. Graph hash: deliberately unavailable under the isolation instruction; no graph was read.

**Isolation disclosure.** The only context files read were `protocol.md` and `rounds/codex-managed/gc-full-goal-cuspidal-source-review/briefs/blind_radial_abel_statement.md`. I did not inspect the agent brief, graph, manifest, strategy, history, arithmetic application, external sources, sibling reports, or conductor artifacts. I used no experiments, numerical computations, or computer algebra. The clock supplied the timestamp. The only file written is this assigned report; its final bytes are hashed separately after writing.

The proposed estimate is true:

\[
 M(U,L)\asymp_G\sqrt{U}\,e^{L/2}\qquad(U,L\ge2),
\]

with no relation between the two parameters. The front profile is nonzero, smooth, integrable, and has signed integral zero. Writing that profile as \(\Phi\), the stronger, uniform full-mass formula is

\[
\boxed{M(U,L)=2\pi\sqrt{U\sinh L}\,\|\Phi\|_1
 -2\cosh(L/2)H\bigl(i/(2U)\bigr)
 +O_G\bigl(U^{-1/2}\sqrt{\sinh L}\bigr).}
\tag{1}
\]

The exact signed integral is

\[
\boxed{J(U,L):=2\pi\int_0^\infty k(r)\sinh r\,dr
 =2\cosh(L/2)H\bigl(i/(2U)\bigr).}
\tag{2}
\]

Thus \(J\asymp e^{L/2}\), whereas \(M\asymp_G\sqrt U e^{L/2}\). The smaller signed answer cannot replace the absolute mass.

There is also a proved no-go statement concerning a different hypothesis: replacing the Fourier multiplier by any nonzero **even** function in \(C_c^\infty(\mathbb R)\) gives a radial Abel kernel that is **not** absolutely integrable against \(\sinh r\,dr\). Smooth compact spectral support does imply Schwartz decay of the time transform and \(e^{-r/2}\) times arbitrary inverse powers for the radial kernel; these do not imply radial absolute integrability.

## 2. Exact statements and hypotheses

Assume exactly the packet's hypotheses:

\[
0\le G\in C_c^\infty((-1,1)),\qquad G(-v)=G(v),\qquad \int G(v)\,dv=1,
\]

\[
H(t)=\int_{\mathbb R}G(v)e^{itv}\,dv,\quad
g(s)=U\{G(U(s-L))+G(U(s+L))\},\quad U,L\ge2,
\]

\[
k(r)=-\frac1{\pi\sqrt2}\int_r^\infty
\frac{g'(s)}{\sqrt{\cosh s-\cosh r}}\,ds\quad(r\ge0).
\]

Let \(b=\max\{|v|:v\in\operatorname{supp}G\}\), so \(0<b<1\), and set \(S=\sinh L\). Then:

1. With the same positive-exponent Fourier convention as the packet,
   \[
   \widehat g(t)=2\cos(Lt)H(t/U).
   \tag{3}
   \]
   This also holds for complex \(t\).
2. The support of \(g\) lies in the union of \([L-b/U,L+b/U]\) and \([-L-b/U,-L+b/U]\). For \(r\ge0\), only the first bump enters \(k\). The kernel is smooth on the radial half-line, vanishes for \(r\ge L+b/U\), and is strictly negative for \(0\le r<L-b/U\). Its outer support endpoint is exactly \(L+b/U\); its interior tail reaches \(r=0\).
3. Define
   \[
   \Phi(a)=-\frac1{\pi\sqrt2}\int_0^\infty G'(a+w)w^{-1/2}\,dw.
   \tag{4}
   \]
   For every fixed compact real interval \(I\) and integer \(j\ge0\),
   \[
   \sup_{a\in I}\left|\partial_a^j
   \left\{\sqrt S\,U^{-3/2}k(L+a/U)-\Phi(a)\right\}\right|
   \le C_{G,I,j}/U
   \tag{5}
   \]
   uniformly in \(L\ge2\) and \(U\ge U_I\), where \(U_I\) depends only on \(I\). This threshold ensures that all displayed radii are nonnegative. Equivalently,
   \[
   k^{(j)}(L+a/U)=\frac{U^{j+3/2}}{\sqrt{\sinh L}}
   \{\Phi^{(j)}(a)+O_{G,I,j}(U^{-1})\}.
   \tag{6}
   \]
   No restriction on the relative growth of \(U\) and \(L\) occurs. On the particular compact interval \([-b,b]\), (5) holds for every \(U,L\ge2\).
4. The profile obeys
   \[
   \Phi(a)=0\ (a\ge b),\qquad
   \Phi(a)=-\frac1{2\pi\sqrt2}\int G(v)(v-a)^{-3/2}\,dv<0\ (a<-b),
   \tag{7}
   \]
   \[
   \int\Phi=0,\qquad0<\|\Phi\|_1<\infty.
   \tag{8}
   \]
   In particular the profile is not identically zero. No assertion that \(\Phi(0)\) is nonzero is needed or made.
5. The two-sided mass estimate and exact/uniform formulas (1)--(2) hold for all \(U,L\ge2\), with constants depending only on \(G\). In particular
   \[
   \frac{M(U,L)}{\sqrt{U\sinh L}}\longrightarrow2\pi\|\Phi\|_1
   \]
   uniformly for \(L\ge2\) as \(U\to\infty\).

All these are scalar assertions about the definitions. No automorphic or arithmetic identity is assumed or asserted.

## 3. Proof and derivation

### 3.1 Fourier transform, basic support, and the interior sign

Changing variables separately in the two bumps gives

\[
\int g(s)e^{its}\,ds=e^{itL}H(t/U)+e^{-itL}H(t/U),
\]

which proves (3), including its entire extension. The stated support containment is immediate. Because \(L-b/U>0\), the negative bump is absent from every defining integral for \(k(r)\), \(r\ge0\).

For \(r<L-b/U\), integration by parts has no singular endpoint and gives

\[
k(r)=-\frac1{2\pi\sqrt2}\int G(v)
 \frac{\sinh(L+v/U)}{[\cosh(L+v/U)-\cosh r]^{3/2}}\,dv.
\tag{9}
\]

This proves strict negativity throughout that interior, including zero. At zero it specializes to

\[
k(0)=-\frac1{4\pi}\int G(v)
\frac{\cosh((L+v/U)/2)}{\sinh^2((L+v/U)/2)}\,dv<0,
\tag{10}
\]

and in particular \(|k(0)|\asymp e^{-L/2}\) uniformly for \(U,L\ge2\). The kernel is therefore not supported only in a thin front annulus.

The smoothness assertion can be seen without differentiating a singular moving endpoint. Set \(x=\cosh r\) and \(f(x)=g(\operatorname{arcosh}x)\). Here \(f\) vanishes near \(x=1\) and is smooth with compact support. Then

\[
k(\operatorname{arcosh}x)=-\frac1{\pi\sqrt2}
\int_0^\infty f'(x+t)t^{-1/2}\,dt.
\tag{11}
\]

Every fixed derivative in \(x\) can be taken under this integral. Composition with \(\cosh r\) also gives a smooth even extension near zero. Vanishing beyond \(L+b/U\) follows directly from the support. The exact outer endpoint follows from the inverse Abel identity proved in Section 3.6: if \(k\) vanished on the entire tail above some smaller radius, that identity would force \(g\) to vanish there also, contrary to the definition of \(b\).

### 3.2 Front expansion and differentiated controls

Write \(r=L+a/U\), \(s=L+(a+w)/U\), and

\[
Q_{U,L}(a,w)=\int_0^1
\frac{\sinh(L+(a+\theta w)/U)}{\sinh L}\,d\theta.
\]

The difference of cosines is exactly

\[
\cosh(L+(a+w)/U)-\cosh(L+a/U)
=\frac{S}{U}\,wQ_{U,L}(a,w).
\]

Consequently

\[
\sqrt S\,U^{-3/2}k(L+a/U)
=-\frac1{\pi\sqrt2}\int_0^\infty
G'(a+w)w^{-1/2}Q_{U,L}(a,w)^{-1/2}\,dw.
\tag{12}
\]

For \(a\) in a fixed compact interval, the integrand is zero unless \(w\) lies in a fixed bounded interval. Use the exact formula

\[
\frac{\sinh(L+z/U)}{S}=\cosh(z/U)+\coth L\sinh(z/U).
\]

Since \(\coth L\le\coth2\), for sufficiently large \(U\) depending only on the compact interval,

\[
Q=1+O_I(U^{-1}),\qquad Q\ge c_I>0,\qquad
\partial_a^m Q=O_{I,m}(U^{-m})\quad(m\ge1).
\]

Thus \(Q^{-1/2}-1=O_I(U^{-1})\), and every fixed positive-order \(a\)-derivative of \(Q^{-1/2}\) is \(O_{I,m}(U^{-1})\). Differentiating (12) is legitimate because its endpoint is fixed, all derivatives of \(G\) are bounded, and \(w^{-1/2}\) is locally integrable. This proves (5), with

\[
\Phi^{(j)}(a)=-\frac1{\pi\sqrt2}\int_0^\infty
G^{(j+1)}(a+w)w^{-1/2}\,dw.
\tag{13}
\]

If \(a\in[-b,b]\), all nonzero integrands have \(a+\theta w\in[-b,b]\). Therefore the same estimates hold for every \(U\ge2\), uniformly in \(L\ge2\); no large-parameter threshold is necessary there. Equation (6) follows by the chain rule.

### 3.3 Nonvanishing, tails, and signed mass of the profile

Let

\[
F(a)=\int_0^\infty G(a+w)w^{-1/2}\,dw.
\]

Then \(\Phi=-(\pi\sqrt2)^{-1}F'\). For \(a<-b\), ordinary integration by parts proves (7). Since \(G\ge0\) and \(\int G=1\), the right side of (7) is strictly negative. This establishes nonvanishing for the given \(G\) without any genericity assumption.

For \(a\to-\infty\), expansion under the compactly supported integral gives

\[
F(a)=(-a)^{-1/2}\{1+O_G(a^{-2})\},
\]

\[
\Phi(a)=-\frac1{2\pi\sqrt2}(-a)^{-3/2}
\{1+O_G(a^{-2})\}.
\tag{14}
\]

The missing first-order moment uses evenness of \(G\). The profile vanishes to the right of \(b\), is smooth on finite intervals, and has the integrable left tail (14). Hence \(\Phi\in L^1\). Also \(F\) tends to zero at both ends, so

\[
\int_{\mathbb R}\Phi(a)\,da=0.
\]

Together with strict negativity on \(( -\infty,-b)\), this implies that \(\Phi\) is positive somewhere and

\[
\|\Phi\|_1=2\int_{-b}^{b}\Phi(a)_+\,da>0.
\tag{15}
\]

### 3.4 Entire interior and uniform two-sided absolute mass

Set \(R=L-2/U\), so \(R\ge1\). For \(0\le r\le R\), use (9) and Tonelli's theorem. The whole interior contribution is exactly

\[
\begin{aligned}
M_{\mathrm{int}}
&:=2\pi\int_0^R |k(r)|\sinh r\,dr\\
&=\sqrt2\int G(v)\sinh s
\left\{(\cosh s-\cosh R)^{-1/2}
 -(\cosh s-1)^{-1/2}\right\}\,dv,
\qquad s=L+v/U.
\end{aligned}
\tag{16}
\]

Indeed, the inner integral is

\[
\int_0^R\frac{\sinh r\,dr}{(\cosh s-\cosh r)^{3/2}}
=2\{(\cosh s-\cosh R)^{-1/2}-(\cosh s-1)^{-1/2}\}.
\]

For all relevant \(s\),

\[
\sinh s\asymp S,\qquad \sinh R\asymp S,\qquad
\cosh s-\cosh R\ge (s-R)\sinh R\ge cS/U.
\]

The constants are uniform for \(U,L\ge2\), since \(s-L\in[-1/2,1/2]\) and \(L-R\le1\). Equation (16), with its second term retained or discarded only in the bounding direction, yields

\[
M_{\mathrm{int}}\le C\sqrt{US}.
\tag{17}
\]

For the remaining interval \(R\le r\le L+b/U\),

\[
\cosh s-\cosh r\ge cS(s-r),
\]

and the original integral, \(|g'|\le U^2\|G'\|_\infty\), and its interval length at most \((b+2)/U\) give

\[
|k(r)|\le C_G U^{3/2}S^{-1/2}.
\]

The weighted size of this interval is at most \(CS/U\). This and (17) prove the global upper bound \(M\le C_G\sqrt{US}\).

For the lower bound use only

\[
r=L+a/U,\qquad -2\le a\le-1.
\]

Every such radius lies strictly below the support of the positive bump, so (9) applies without cancellation. For every \(v\in\operatorname{supp}G\),

\[
\sinh s\ge cS,\qquad
\cosh s-\cosh r\le(s-r)\sinh s\le CS/U.
\]

Therefore \(|k(r)|\ge cU^{3/2}S^{-1/2}\). Also \(\sinh r\ge cS\), and this interval has length \(1/U\). It follows that

\[
c\sqrt{US}\le M(U,L)\le C_G\sqrt{US}.
\tag{18}
\]

Since \(\sinh L\asymp e^L\) for \(L\ge2\), this proves the requested estimate uniformly, including \(U=2\), \(L=2\), unrestricted ratios \(U/L\), and the full interior down to zero.

### 3.5 Exact signed integral and sharper full absolute mass

The compact support and integrable square-root singularity justify the following absolute Fubini interchange even with \(|g'|\):

\[
\begin{aligned}
J
&=-\sqrt2\int_0^\infty g'(s)
 \left\{\int_0^s\frac{\sinh r\,dr}{\sqrt{\cosh s-\cosh r}}\right\}ds\\
&=-2\sqrt2\int_0^\infty g'(s)\sqrt{\cosh s-1}\,ds\\
&=-4\int_0^\infty g'(s)\sinh(s/2)\,ds\\
&=2\int_0^\infty g(s)\cosh(s/2)\,ds\\
&=2\cosh(L/2)\int G(v)\cosh(v/(2U))\,dv.
\end{aligned}
\tag{19}
\]

The odd term disappears by evenness. This proves (2) and also \(J=\widehat g(i/2)\) with precisely the Fourier convention in (3). If \(m_2=\int v^2G(v)\,dv\), then

\[
J=2\cosh(L/2)\left\{1+\frac{m_2}{8U^2}+O_G(U^{-4})\right\},
\tag{20}
\]

uniformly for \(L\ge2\). In particular \(J>0\) and \(J\asymp e^{L/2}\).

There is a convenient exact way to pay the full interior while obtaining the leading constant in the **absolute** mass. Let

\[
P_+=2\pi\int_0^\infty k(r)_+\sinh r\,dr.
\]

By (9), every positive part is confined to \(L-b/U\le r\le L+b/U\). On that interval (5) applies for all \(U,L\ge2\), and

\[
\frac{\sinh(L+a/U)}{S}=1+O(U^{-1}).
\]

Because \(x\mapsto x_+\) is 1-Lipschitz,

\[
P_+=2\pi\sqrt{US}\left\{\int_{-b}^b\Phi(a)_+\,da+O_G(U^{-1})\right\}.
\tag{21}
\]

The exact identity \(M=2P_+-J\), followed by (15), proves (1). This argument neither discards nor approximates away the deep negative interior: its total signed contribution is incorporated exactly through \(J\). In normalized form,

\[
\frac{M}{2\pi\sqrt{US}}
=\|\Phi\|_1-\frac{J}{2\pi\sqrt{US}}+O_G(U^{-1}),
\]

so the asserted uniform leading constant and a uniform \(O_G(U^{-1/2})\) relative error follow immediately. Formula (18) separately provides the two-sided estimate for the entire parameter range rather than attempting to infer a lower bound from an asymptotic with an uncontrolled small-\(U\) error.

### 3.6 Smooth compact spectral support: a proved obstruction

Here consider a different input. Let \(h\in C_c^\infty(\mathbb R)\) be even and nonzero, and put

\[
g_h(s)=\frac1{2\pi}\int h(t)e^{-its}\,dt.
\]

Repeated integration by parts proves that \(g_h\) and every derivative are Schwartz functions. Define \(k_h\) by the same radial Abel formula with \(g_h\) in place of \(g\). For \(r\ge1\) and \(u\ge0\),

\[
\cosh(r+u)-\cosh r
=\frac{e^r}{2}(e^u-1)(1-e^{-2r-u})
\ge c e^r(e^u-1).
\]

Since \(\int_0^\infty(e^u-1)^{-1/2}\,du<\infty\), this gives, for every \(N\),

\[
|k_h(r)|\le C_{h,N}e^{-r/2}(1+r)^{-N}.
\tag{22}
\]

The same estimate holds for each fixed derivative: after shifting \(s=r+u\), derivatives in \(r\) of the denominator factor are bounded by constants times that factor, and derivatives of \(g_h\) remain Schwartz. At zero, evenness gives \(g_h'(s)=O(s)\), so the defining integral converges there. More generally the argument (11), now with the even smooth function \(g_h\), shows smoothness at zero. Formula (22) implies unweighted absolute integrability in \(dr\) and radial square integrability in \(\sinh r\,dr\), but its bound alone does not imply radial absolute integrability.

In fact radial absolute integrability is impossible for every such nonzero \(h\). This can be proved directly rather than left as a warning about insufficient estimates.

First, for either compactly supported smooth even \(g\) or even Schwartz \(g_h\), the inverse Abel identity is

\[
g_h(s)=\sqrt2\int_s^\infty
\frac{k_h(r)\sinh r}{\sqrt{\cosh r-\cosh s}}\,dr\quad(s\ge0).
\tag{23}
\]

To prove it, write \(f(x)=g_h(\operatorname{arcosh}x)\), insert (11), and interchange the two integrals. Absolute interchange holds because \(\int_x^\infty|f'(y)|\,dy<\infty\), and the inner beta integral is exactly

\[
\int_x^y\frac{dz}{\sqrt{z-x}\sqrt{y-z}}=\pi.
\]

The resulting expression is \(-\int_x^\infty f'(y)\,dy=f(x)\), since \(f\) vanishes at infinity. This proves (23) with its stated constant.

Suppose for contradiction that \(\int_0^\infty|k_h(r)|\sinh r\,dr<\infty\). Fix \(0<\sigma<1/2\). The elementary bound

\[
B_\sigma(r):=\int_0^r\frac{e^{\sigma s}}{\sqrt{\cosh r-\cosh s}}\,ds\le C_\sigma
\tag{24}
\]

holds uniformly for \(r\ge0\). For \(r\le1\), use \(\cosh r-\cosh s\ge(r^2-s^2)/2\). For \(r\ge1\), use

\[
\cosh r-\cosh s=\frac{e^r}{2}(1-e^{-(r-s)})(1-e^{-r-s})
\ge c e^r(1-e^{-(r-s)}).
\]

With \(u=r-s\), the resulting upper bound for (24) is

\[
Ce^{(\sigma-1/2)r}\int_0^r e^{-\sigma u}(1-e^{-u})^{-1/2}\,du\le C_\sigma.
\]

Taking absolute values in (23), integrating with \(e^{\sigma s}\), and applying Tonelli now yields

\[
\int_0^\infty |g_h(s)|e^{\sigma s}\,ds
\le\sqrt2 C_\sigma\int_0^\infty|k_h(r)|\sinh r\,dr<\infty.
\]

By evenness, \(\int_{\mathbb R}|g_h(s)|e^{\sigma|s|}\,ds<\infty\). Therefore

\[
z\longmapsto\int_{\mathbb R}g_h(s)e^{izs}\,ds
\]

is holomorphic for \(|\operatorname{Im}z|<\sigma\); differentiability follows by domination on smaller strips. On the real axis it equals \(h\), by Fourier inversion. But \(h\) vanishes on a nonempty open interval outside its compact support. The identity theorem would force this holomorphic function, and hence \(h\), to vanish identically, a contradiction. Thus

\[
\boxed{\int_0^\infty |k_h(r)|\sinh r\,dr=\infty
\quad\text{for every nonzero even }h\in C_c^\infty(\mathbb R).}
\tag{25}
\]

For an explicit allowed input, take \(h(t)=\exp[-1/(1-t^2)]\) for \(|t|<1\) and zero otherwise; (25) proves its failure without an experiment. This even subclass already disproves any assertion of radial absolute integrability for an arbitrary smooth compactly supported spectral multiplier. It also rules out compact radial support or a uniform integrable exponential tail for such a nonzero input. No assertion about non-even inputs is needed.

In contrast, the packet's time profile has compact support before Abel inversion, which directly gives compact radial support and finite radial absolute mass. Its Fourier multiplier is entire and Schwartz on the real axis; it is not a nonzero compactly supported spectral function. Bare smoothness without compact support or quantitative decay supplies still fewer decay conclusions. These are different hypotheses, not interchangeable smoothing descriptions.

## 4. First doubtful or unproved step

There is no remaining unproved step in the scalar conclusions above. The differentiated front expansion is an asymptotic in \(U\), uniform in every \(L\ge2\); for an arbitrary compact interval of \(a\), the stated threshold ensures the radius remains in its defined domain. All estimates used for the global result and the sharper mass formula hold for every \(U,L\ge2\).

The report establishes no automorphic identification, arithmetic cancellation estimate, or downstream theorem. Any application requiring one of those would have its first unproved step at that additional identification or estimate. No graph or application was read, so no such implication is evaluated here.

## 5. Required control tests and outcomes

All controls are analytic; no experiment was run.

1. **Normalization and sign control: passed.** Two independent integrations by parts give the negative interior formula (9) and the exact positive signed reconstruction (19). The constants combine to \(J=\widehat g(i/2)\), using precisely the positive-exponent Fourier convention specified in the packet.
2. **Nonvanishing and front-cancellation control: passed.** The exact formula (7) makes the profile strictly negative for every \(a<-b\), while its primitive proves \(\int\Phi=0\). Therefore the local leading profile is nonzero but its signed leading term cancels, consistently with \(M\) having size \(\sqrt U e^{L/2}\) and \(J\) having size \(e^{L/2}\).
3. **Entire interior and endpoint control: passed.** Equation (16) integrates the whole interval from zero through \(L-2/U\), including the subtraction at \(\cosh0=1\). Equation (10) checks the finite nonzero value at zero. The interval \(a\in[-2,-1]\) proves a lower bound without a large-\(U\) assumption. All estimates remain uniform when either parameter equals 2 and when their ratio is unrestricted.
4. **Absolute versus signed mass control: passed.** The exact identity \(M=2P_+-J\) and the fact that positivity is confined to a fixed rescaled front interval produce (1). This uses all of the negative interior rather than replacing it by a local asymptotic.
5. **False spectral-smoothing analogue: rejected by proof.** Equations (23)--(25) prove that every nonzero even smooth compact spectral input fails radial absolute integrability. The explicit bump given after (25) is a concrete analytic control. Schwartz time decay and the bound (22) cannot be promoted to the false radial \(L^1\) conclusion.

## 6. Dependencies and exact artifacts used

Context dependencies, and no others:

- `protocol.md` — research/reporting contract, authority, and round discipline.
- `rounds/codex-managed/gc-full-goal-cuspidal-source-review/briefs/blind_radial_abel_statement.md` — the complete scalar hypotheses and assignment.

Mathematical tools used and proved or justified where applied: change of variables, differentiation under a dominated integral, elementary integration by parts, Tonelli/Fubini with the displayed integrability bounds, Fourier inversion for Schwartz functions, the beta integral \(\pi\), and the holomorphic identity theorem. No external theorem source, source card, graph claim, candidate proof, computation, historical file, or arithmetic input was used.

Output artifact: `rounds/codex-managed/gc-full-goal-cuspidal-source-review/reports/blind_radial_abel_kernel.md`. The final SHA256 is communicated separately so that the report need not contain a self-referential checksum.

## 7. Recommended state effect and stopping status

**Recommended state effect: retain for conductor validation.** The isolated scalar packet is proved with the explicit qualifications on domain and spectral hypotheses above. This report supplies independent evidence for the scalar kernel, the exact signed/absolute distinction, and the spectral-support obstruction. It makes no graph promotion by itself and recommends no downstream arithmetic conclusion.

The assigned analytic task is complete. No shared state, proof draft, validation matrix, synthesis, or other file was edited. Freeze this artifact at its separately reported SHA256; this task stops here without designing or starting another round.
