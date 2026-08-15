# Blind finite reflected vector kernel

## 1. Result

At finite contour heights the radial functional equation gives the exact decomposition
\[
\boxed{\mathfrak I^{\,c}_{U,V,S}
=\mathfrak R^{\rm ar}_{U,V}
+\sum_{m\ge1}\sum_{hq=m}\mathcal K_{U,V,S,X}(h,q;m)
+\mathfrak B^{\rm rad}_{U,V,S}.}
\tag{1}
\]
Here \(\mathfrak I^{\,c}\) is the original finite \(u,v,s\) vertical integral, \(\mathfrak R^{\rm ar}\) is the crossed zeta residue, \(\mathcal K\) is a genuine vector kernel with dual radial index \(m\), and \(\mathfrak B^{\rm rad}\) consists of the two finite radial horizontal sides. No infinite-height identity or estimate is asserted.

## 2. Exact statement and hypotheses

Put \(D_j=2^{-j}\lfloor\sqrt X\rfloor\), \(H_j=\lfloor D_jX^{-1/4}\rfloor\), \(N_X=\lfloor16\sqrt X\rfloor\), and
\[
\mathcal A_j(u,v)=\widehat W_j(u)\widehat\phi(v)
\left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v,
\]
where \(\widehat W_0=\widehat W_+=1/u+\widehat W_{+,r}\), \(\widehat W_j=\widehat W\) for \(j\ge1\), and the top inversion is symmetric. Let
\[
g_v(x)=x^{-3/4-v/2}e(\sqrt{Xx})\mathbf1_{[1,N_X]}^*(x),\qquad
G_v(w)=\int_1^{N_X}x^{w-7/4-v/2}e(\sqrt{Xx})\,dx .
\]
The star means symmetric endpoint half-values upon inversion.

Use finite segments \(\Gamma_{a,U}:a-iU\to a+iU\), \(\Gamma_{b,V}\), and \(\Gamma_{c,S}\), with \(a,b>0\),
\[
c,c'>1+\frac{a+b}{2},\qquad \lambda=1-c',\qquad
S>\frac{U+V}{2}.
\tag{2}
\]
The last strict inequality keeps every moving pole \(w=1-(u+v)/2\) inside, not on, the radial rectangle. Define
\[
\mathfrak I^{\,c}_{U,V,S}
=\sum_{j=0}^J\frac1{(2\pi i)^3}
\int_{\Gamma_{a,U}}\int_{\Gamma_{b,V}}\int_{\Gamma_{c,S}}
\mathcal A_j(u,v)G_v(w)F_{u+v}(w)\,dw\,dv\,du .
\tag{3}
\]

## 3. Proof and exact kernel

For \(z=u+v\),
\[
F_z(w)=K_z(w)F_{-z}(1-w),
\]
\[
K_z(w)=2^{1-2w+z}\pi^{2w-1}
\frac{\Gamma((1-w-z/2)/2)\Gamma((2-w+z/2)/2)}
{\Gamma((w+z/2)/2)\Gamma((w-z/2+1)/2)}.
\tag{4}
\]
Shift the finite \(w\)-segment from \(c\) to \(\lambda\), retain both horizontal sides, and set \(s=1-w\) on the terminal line. Since \(\Re s=c'\), expand absolutely
\[
F_{-z}(s)=\sum_{m\ge1}a_{-z}(m)m^{-s}
=\sum_{m\ge1}\sum_{hq=m}\chi_4(q)
\left(\frac hq\right)^{z/2}m^{-s}.
\tag{5}
\]
Thus
\[
\boxed{\begin{aligned}
\mathcal K_{U,V,S,X}(h,q;m)
={}&\mathbf1_{hq=m}\frac{\chi_4(q)}{(2\pi i)^3}
\sum_{j=0}^J\int_{\Gamma_{a,U}}\int_{\Gamma_{b,V}}
\int_{\Gamma_{c',S}}\mathcal A_j(u,v)
\left(\frac hq\right)^{(u+v)/2}\\
&\qquad\qquad {}\times G_v(1-s)K_{u+v}(1-s)m^{-s}\,ds\,dv\,du ,
\end{aligned}}
\tag{6}
\]
where every gamma factor is explicit through
\[
K_z(1-s)=2^{2s+z-1}\pi^{1-2s}
\frac{\Gamma((s-z/2)/2)\Gamma((1+s+z/2)/2)}
{\Gamma((1-s+z/2)/2)\Gamma((2-s-z/2)/2)}.
\tag{7}
\]
In particular \(G_v(1-s)=\int_1^{N_X}x^{-s-3/4-v/2}e(\sqrt{Xx})\,dx\); it is not a scalar profile factor.

The ordinary pole crossed in \(w\) gives
\[
\mathfrak R^{\rm ar}_{U,V}
=\sum_j\frac1{(2\pi i)^2}\int_{\Gamma_{a,U}}\int_{\Gamma_{b,V}}
\mathcal A_j(u,v)G_v(1-z/2)L(1-z,\chi_4)\,dv\,du .
\tag{8}
\]
No separated gamma pole is added: in the intact completion such poles are paired with trivial zeros.

With \(Q_{j,u,v}(w)=\mathcal A_j(u,v)G_v(w)F_z(w)\), the radial sides in (1) are exactly
\[
\mathfrak B^{\rm rad}
=\sum_j\frac1{(2\pi i)^3}\int_{\Gamma_{a,U}}\int_{\Gamma_{b,V}}
\left\{\int_{\lambda+iS}^{c+iS}Q_{j,u,v}(w)\,dw
+\int_{c-iS}^{\lambda-iS}Q_{j,u,v}(w)\,dw\right\}dv\,du .
\tag{9}
\]

The \(v=0\) and top \(u=0\) residues are **not** crossed in (1), because both outside lines remain positive. If one moves them, their vector coefficients are, with \(\delta=\mathbf1_{hq=m}\chi_4(q)\),
\[
\begin{aligned}
R_v&=\frac{\delta}{(2\pi i)^2}\sum_j\int_u\int_s
\widehat W_j(u)(D_j/(2\sqrt X))^u(h/q)^{u/2}
G_0(1-s)K_u(1-s)m^{-s}\,ds\,du,\\
R_u&=\frac{\delta}{(2\pi i)^2}\int_v\int_s
\widehat\phi(v)(H_0+1)^v(h/q)^{v/2}
G_v(1-s)K_v(1-s)m^{-s}\,ds\,dv,\\
R_{uv}&=\frac{\delta}{2\pi i}\int_sG_0(1-s)K_0(1-s)m^{-s}\,ds .
\end{aligned}
\tag{10}
\]
The signs are fixed by the chosen shift direction; the corner is counted once. The same residue operation must also be applied to (8) and (9), rather than silently discarding their axial terms. At finite \(U,V\), each move additionally retains the two horizontal segments
\[
\int_{-\alpha+iT}^{\alpha+iT}M(\xi)d\xi+
\int_{\alpha-iT}^{-\alpha-iT}M(\xi)d\xi
\tag{11}
\]
for \((\xi,\alpha,T)=(u,a,U)\) or \((v,b,V)\), with \(M\) the unsimplified full integrand. The radial endpoint stars are already encoded by \(G_v\); an auxiliary Perron cutoff would instead contribute its explicit boundary half-residue outside \(\mathcal K\).

## 4. First doubtful or unproved step

There is no doubtful step in the finite rectangle algebra. The first unproved step is deleting (9)–(10), passing any of \(U,V,S\) to infinity, or estimating the resulting vector operator uniformly in the three heights.

## 5. Required controls and outcomes

- **Reflection:** (5) gives \((h/q)^{z/2}\), hence \(a_{-z}\), not \(a_z\). Pass.
- **Orientation:** the substitution \(s=1-w\) sends the upward \(\lambda\)-line to the upward \(c'\)-line, giving the plus sign in (1). Pass.
- **Residues:** only (8) is crossed in the frozen positive-\(u,v\) derivation; height, Perron, and endpoint terms are neither silently discarded nor double-counted. Pass.
- **Finite-height scope:** (9) is retained exactly. Pass. No numerical control was used.

## 6. Dependencies and exact artifacts used

Only the brief-authorized protocol, proof graph, active campaign, Round-15 synthesis and radial attack, Round-16 synthesis and blind identity, Round-18 synthesis, and Round-19 brief were used.

## 7. Recommended state effect

Promote (1), (6)–(9) as the finite definition of M9-M1-post-FE-vector-kernel. Retain its uniform estimate, horizontal-side removal, hard Perron limit, high-\(2\)-adic reflected tail, GAR, and M9-M1 as open.
