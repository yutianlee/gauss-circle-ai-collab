# Blind \(M=1\) endpoint boundary Cauchy algebra

## 1. Result

Freeze all contours. For each endpoint \(x\in\{N_X,1\}\), the terminal
vertical term, the two oriented radial sides, and the artificial-pole
residue collapse exactly to a right-chamber truncated Perron boundary term
minus that endpoint's arithmetic-pole contribution:
\[
\boxed{\mathfrak T_x+\mathfrak S_x+\mathfrak P_x
=\mathfrak C_x-\mathfrak A_x.}
\tag{1}
\]
Thus the artificial pole creates no new residue theorem. The collapsed
upper endpoint is a finite Perron version of a sharp twisted-divisor
partial sum; the lower endpoint is its \(x=1\) version. No target-sized
estimate follows.

## 2. Exact statement and hypotheses

Put \(N=N_X\), \(z=u+v\),
\[
\gamma_v=\frac34+\frac v2,\qquad
\delta=1-\frac z2-\gamma_v=\frac14-\frac u2-v,
\]
and assume first \(\delta\ne0\). Take the Round-19 rectangle with all
vertical segments upward,
\[
c-iS\to c+iS,\quad \lambda-iS\to\lambda+iS,\quad
c'-iS\to c'+iS,\qquad \lambda=1-c',
\]
and sides
\[
\lambda+iS\to c+iS,\qquad c-iS\to\lambda-iS.
\tag{2}
\]
Let \(\varepsilon_N=1,\varepsilon_1=-1\),
\(e_x=e(\sqrt{Xx})\), and
\[
E_x(w,v)=\varepsilon_xe_x\,\frac{x^{w-\gamma_v}}{w-\gamma_v}.
\tag{3}
\]
Then \(E_{N}+E_1\) is exactly the \(M=1\) endpoint term.

All outside expressions are integrated with
\[
\langle Y\rangle:=
\sum_{j=0}^J\frac1{(2\pi i)^2}
\int_{\Gamma_{a,U}}\int_{\Gamma_{b,V}}
\mathcal A_j(u,v)Y(u,v)\,dv\,du,
\tag{4}
\]
\[
\mathcal A_j=\widehat W_j(u)\widehat\phi(v)
\left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v,
\quad H_j=\lfloor D_jX^{-1/4}\rfloor ,
\]
where \(\widehat W_0=1/u+\widehat W_{+,r}\). Thus every scale, floor,
height profile, and hard-top convention remains present.

## 3. Exact finite derivation

For fixed \(u,v\), define
\[
\begin{aligned}
T_x={}&\frac{\varepsilon_xe_x}{2\pi i}
\int_{\Gamma_{c',S}}
\frac{x^{1-s-\gamma_v}}{1-s-\gamma_v}
K_z(1-s)F_{-z}(s)\,ds\\
={}&\varepsilon_xe_x\sum_{h,q\ge1}\chi_4(q)
\left(\frac hq\right)^{z/2}
\frac1{2\pi i}\int_{\Gamma_{c',S}}
\frac{x^{1-s-\gamma_v}K_z(1-s)(hq)^{-s}}
{1-s-\gamma_v}\,ds ,
\end{aligned}
\tag{5}
\]
where the second line is absolutely convergent. Define the sides, with
the orientations (2),
\[
S_x=\frac{\varepsilon_xe_x}{2\pi i}
\left\{\int_{\lambda+iS}^{c+iS}
+\int_{c-iS}^{\lambda-iS}\right\}
\frac{x^{w-\gamma_v}F_z(w)}{w-\gamma_v}\,dw .
\tag{6}
\]
The artificial pole \(w=\gamma_v\) lies inside because
\(|\Im v|/2<S\), and its residue is
\[
P_x=\varepsilon_xe_xF_z(\gamma_v)
=\varepsilon_xe_x
\zeta\!\left(\frac34+\frac u2+v\right)
L\!\left(\frac34-\frac u2,\chi_4\right).
\tag{7}
\]
The genuine arithmetic pole \(w=1-z/2\) contributes
\[
A_x=\varepsilon_xe_x\,\frac{x^\delta}{\delta}
L(1-z,\chi_4).
\tag{8}
\]
Finally let
\[
C_x=\frac{\varepsilon_xe_x}{2\pi i}
\int_{\Gamma_{c,S}}\frac{x^{w-\gamma_v}F_z(w)}
{w-\gamma_v}\,dw .
\tag{9}
\]
Cauchy's theorem on the finite rectangle, followed on the left segment by
the functional equation and \(s=1-w\), gives
\[
C_x=A_x+P_x+T_x+S_x,
\]
which proves (1) after applying (4). No horizontal segment is deleted.
When \(\delta=0\), the arithmetic and artificial poles collide; (1)
continues only after their combined Laurent coefficient is taken, not by
adding two simple residues.

### Endpoint-by-endpoint form in original variables

On \(\Re w=c\),
\[
F_z(w)=\sum_{h,q\ge1}\chi_4(q)
\left(\frac qh\right)^{z/2}(hq)^{-w}.
\]
Consequently
\[
C_x=\varepsilon_xe_xx^{-\gamma_v}
\sum_{h,q\ge1}\chi_4(q)\left(\frac qh\right)^{z/2}
\mathscr P_{c,S,\gamma_v}\!\left(\frac{x}{hq}\right),
\quad
\mathscr P_{c,S,\gamma}(A)=\frac1{2\pi i}
\int_{\Gamma_{c,S}}\frac{A^w}{w-\gamma}\,dw .
\tag{10}
\]
Thus, separately,
\[
\boxed{T_N+S_N+P_N
=C_N-e(\sqrt{XN})\frac{N^\delta}{\delta}L(1-z,\chi_4),}
\tag{11}
\]
\[
\boxed{T_1+S_1+P_1
=C_1+e(\sqrt X)\frac1{\delta}L(1-z,\chi_4).}
\tag{12}
\]
The terminal character factor in (5) is reflected,
\(\chi_4(q)(h/q)^{z/2}\); the collapsed right-chamber factor in (10) is
the original \(\chi_4(q)(q/h)^{z/2}\). Hence (11) is an exact return to
the original coefficient sector, not a new scalar cancellation.

The actual Round-21 boundary operator omits the reassigned artificial
residue:
\[
\mathfrak T_x+\mathfrak S_x
=\mathfrak C_x-\mathfrak A_x-\mathfrak P_x.
\tag{13}
\]
The renormalized \(M=1\) remainder has artificial residue \(-P_x\);
these two cancel before the full split is interpreted.

## 4. First doubtful or unproved step

The first unproved step is any finite-\(S\) or limiting estimate for
\(\langle C_N-A_N\rangle\). Formally, only after a separately justified
symmetric Perron limit, (10) becomes
\[
\varepsilon_xe_x\sum_{hq\le x}^{*}
\chi_4(q)(q/h)^{z/2}(hq)^{-\gamma_v};
\]
no such limit is taken here.

## 5. Required control test and outcome

Sign control passes: the upper endpoint is positive, the lower negative,
while the lower radial side is oppositely oriented. Artificial-residue
control passes because \(P_x+(-P_x)=0\). Endpoint stars do not halve
(3), (7), or (8); they apply only to a symmetric inverse-Mellin equality
case. No numerical experiment was used.

## 6. Dependencies and exact artifacts used

Only the authorized protocol, proof graph, active campaign, Round-21
synthesis and its two reports, Round-19 finite-vector synthesis/report, and
the assigned Round-22 brief were read. No other Round-22 report was read.

## 7. Recommended state effect

Promote (1), (5)–(13) as the finite \(M=1\) endpoint Cauchy reduction.
Record a scoped return/no-go: correct artificial-pole recombination turns
the boundary into an original-sector finite Perron endpoint sum minus its
arithmetic main term; it supplies no automatic cancellation. Retain the
upper endpoint estimate, outside residues, transition traces, GAR, and
M9-M1 as open.

## Normalization addendum: physical M1 scale

Round 14 places the entire Round-15 double-Mellin/GAR expression inside
\[
\sum_j\mathcal M_1(D_j;X)
=-\frac4\pi X^{1/4}\operatorname {Re}\!\left\{
e(1/8)\,\mathcal I(X)\right\}+O_W(\log^2X).
\]
There is no compensating \(X^{-1/4}\) in the finite Cauchy reduction.
Therefore, for
\(\mathfrak B_x^{\rm coll}:=\langle T_x+S_x+P_x\rangle
=\langle C_x-A_x\rangle\), its exact physical contribution is
\[
\boxed{-\frac4\pi X^{1/4}\operatorname {Re}\!\left\{
e(1/8)\mathfrak B_x^{\rm coll}\right\}.}
\]
The \(O_W(\log^2X)\) transform error remains separate.

Since \(N=N_X\asymp X^{1/2}\), an elementary inner bound
\[
|\langle C_N\rangle|\ll N^{1/4}\log^2X
\]
would become
\[
\ll X^{1/4}N^{1/4}\log^2X
\asymp X^{3/8}\log^2X
\]
in the physical M1 aggregate. **Verdict: not target-sized.** The required
physical scale \(X^{1/4+\varepsilon}\) corresponds here to an inner
\(X^\varepsilon\) estimate; absolute endpoint summation loses
\(N^{1/4}\asymp X^{1/8}\).
