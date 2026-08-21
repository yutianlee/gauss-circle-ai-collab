# Conductor candidate: canonical M1 and M2 core statements

This candidate repairs the notation and bridge seams in the frozen
Round-92 packet.  It formalizes two open estimates; it proves neither
estimate and licenses no M9 or endpoint promotion.

## 1. Common scales and collision-free names

Put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5}.
\]

For M1, write \(C_{\mathrm{cond}}\) for the Farey/conductor scale,
\(B=C_{\mathrm{cond}}/T\), \(M_{\mathrm{loc}}\) for the class modulus,
and \(U\) for the dyadic deep-difference/Fejer length.  Thus

\[
 J^{13/18}<C_{\mathrm{cond}}\leq J^{3/4},\qquad
 J^{11/90}<B\leq J^{3/20},\qquad M_{\mathrm{loc}}\asymp B,
\]

and \(D_1<U\ll Q^2\), where
\[
 D_1=\lfloor J^{87/140}\rfloor,\qquad
 E_*=\lfloor Q^2J^{-1/20}\rfloor=\lfloor J^{3/4}\rfloor.
\]
The letter \(D_{\mathrm{ray}}\)
below is used only for the M2 primitive-ray separation scale.

For M2, \(L\) is the top-frequency scale,
\(A_{\mathrm{ray}}\asymp a\), \(D_{\mathrm{ray}}\asymp b-a\),
\(K_{\mathrm{rec}}\asymp k\), \(G_{\mathrm{lift}}\asymp
|\mathcal G_{a,b}|\), and \(R_{\mathrm{met}}\) is the punctured metric
window scale.  These names are not interchangeable with the M1
quantities.

## 2. Exact M1 physical and arithmetic dictionaries

For each of the three accepted local classes fix

\[
 (\kappa_{\mathrm{loc}},M_{\mathrm{loc}},K_{\mathrm{loc}})
 \in\{(1,4b,k),(2,2b,2[k\bar4]_b),
        (4,b,[k\bar4]_b)\},
\]

together with one accepted sign, alias, reflected orientation, and
transition-flattened smooth nonaxial principal component.  Put

\[
\begin{aligned}
 e_M(z)&=e(z/M),\\
 S(n,K;M)&=\sum_{x\bmod M}^{*}e_M(nx+K\bar x),\\
 c_M(d)&=\sum_{x\bmod M}^{*}e_M(dx),\\
 \mathcal R_{b,x}(\theta)
   &=M^{-1}\sum_{n\in\mathbb Z}I_b(n)e_M(nx)e(n\theta).
\end{aligned}
\]

Here \(I_b\) is the accepted actual Fourier symbol, including its
stationary support, one-pass entry and exit, class constants, hard
endpoints, stars, and zero extension.  It obeys

\[
 \|\mathcal R_{b,x}\|_\infty
 \ll_\varepsilon X^\varepsilon TQ^{-5/24}.
\]

For a physical ordered pair \(P=(x,y)\) of distinct units modulo \(M\),
define

\[
 F_{b,P}(\theta)
 =e_M(K(\bar x-\bar y))
   \mathcal R_{b,x}(\theta)\overline{\mathcal R_{b,y}(\theta)}.
\]

Let \(\{\Pi_{b,U}\}_U\) be the accepted finite dyadic signed partition
of

\[
 D_1<|d|<\Delta_b-E_*,
\]

including actual-support zero extension.  Set

\[
 f_{b,P,U}=\Pi_{b,U}F_{b,P},\qquad
 H_{b,U}=\sum_{P:x\ne y}f_{b,P,U}.
\]

Let

\[
 D_U(\theta)=\sum_{0\leq j<U}e(j\theta),\qquad
 |D_U(\theta)|^2
 =\sum_{|u|<U}(U-|u|)e(u\theta).
\]

Then

\[
 \mathcal E_U
 =\sum_{b\asymp B}\int_{\mathbb T}|D_U(\theta)|^2
 |H_{b,U}(\theta)|^2\,d\theta.
\]

After expanding two physical ordered pairs, use the unique coordinates

\[
 P=(x,x-A),\qquad P'=(x-V,x-V-B_2).
\]

The complete masked trace is

\[
\begin{aligned}
 \mathfrak T_M(u,A,B_2,V)
  =M\!\!\sum_{\substack{x\bmod M\\
  x,x-A,x-V,x-V-B_2\ {\rm units}}}
  e_M\!\left(u x+K\Phi_{A,B_2,V}(x)\right),\\
 \Phi_{A,B_2,V}(x)
  =\bar x-\overline{x-A}-\overline{x-V}
   +\overline{x-V-B_2}.
\end{aligned}
\]

The fourfold actual stationary symbol is

\[
 \Omega_{b,d,u}(n,m)
 =I_b(n+d+u)\overline{I_b(n)}
  \overline{I_b(m+d)}I_b(m).
\]

All variables in the hard sum are now typed: \(b\) is the conductor
row, \(d\) is the deep dual difference, \(u\) is the Fejer shift,
\(n,m\) are Fourier indices, \(A,B_2,V\) are physical-edge
differences, and \(x\) is the completed unit base point.

## 3. Exact M1 owner order and open core

Let \(\mathscr U_{b,U}\) be the finite set of all tuples in the
expansion of \(\mathcal E_U\) with \(u\ne0\) and both deep multipliers
active.  Ownership is applied in this order:

1. \(\mathscr O_{87}\): the accepted full-prime-power same-group set;
2. \(\mathscr O_{88,c}\): on its complement, the accepted coarse
   coincidence shells \(1<R_*\leq\rho_*\);
3. \(\mathscr O_{88,g}\): on both complements, the accepted good-prime
   reciprocal-period graph with
   \(\mathfrak a\geq M^2/\rho_*^2\);
4. \(\mathscr O_{89}\): on all earlier complements, the accepted
   complete bad-prime cells and summable unions meeting the Round-89
   directed-degree threshold.

Here

\[
 \rho_*=\min\!\left(M,\lfloor J^{11/30}B^{-2}\rfloor\right).
\]

The hard set is the literal successive complement

\[
 \mathscr H_{b,U}
 =\mathscr U_{b,U}\setminus
  (\mathscr O_{87}\sqcup\mathscr O_{88,c}
 \sqcup\mathscr O_{88,g}\sqcup\mathscr O_{89}).
\]

Every owner set and its complement is closed under the accepted sign,
reflection, and conjugation involutions.  Consequently the paired hard
contribution is real; the absolute value below is nevertheless retained so
the estimate remains correctly typed before this symmetry is invoked.

Thus it contains, once only, \(R_*>\rho_*\),
\(\mathfrak a<M^2/\rho_*^2\), residual bad-prime cells, the full
nonunit union, affine/full-phase and projection-only periods, shallow
good-prime lifts, aperiodic factors, every class and sign, every
nonzero modulus multiple, the centered Ramanujan terms, and all four
actual weights.  Empty masks contribute zero.

Define

\[
\begin{aligned}
 \mathcal E_{\mathrm{hard}}(U)
  ={}&\sum_{b\asymp B}
 \sum_{\sigma\in\mathscr H_{b,U}}
 \sum_{0<|u|<U}(U-|u|)
 \sum_{d,n,m}^{\rm deep}
 {\Omega_{b,d,u}(n,m)\over M^5}\\
 &\times e_M(dV+nA-mB_2)
 \mathfrak T_M(u,A,B_2,V).
\end{aligned}
\]

The canonical first-band M1 theorem target is

\[
 \boxed{\;
 |\mathcal E_{\mathrm{hard}}(U)|
 \ll_\varepsilon X^\varepsilon{U\over B}J^{14/5}.
 \;}
\]

The exact one-count identities are

\[
 \mathcal E_U
 =\mathcal E_{u=0}
  +\mathcal E_{87}+\mathcal E_{88,c}
  +\mathcal E_{88,g}+\mathcal E_{89}
  +\mathcal E_{\mathrm{hard}},
\]

and

\[
 \mathfrak T_{82}
 =\mathfrak O_{82,\mathrm{same}}+\mathfrak X_{82},
 \qquad
 \mathfrak X_{82}
 =\mathfrak O_{83:86}
  +\sum_U\sum_{b\asymp B}H_{b,U}(0).
\]

The Gram identity has exactly one global \(u=0\) owner.  At linear level,
the Round-82 same-residue term lies outside \(\mathfrak X_{82}\) and is
owned only by \(\mathfrak O_{82,\mathrm{same}}\); the second identity owns
the literal \(d=0\), small-\(d\), outer-collar, entry/exit, wrong-sign,
stationary-error, and nonstationary terms once.
The proved finite Toeplitz estimate

\[
 \left|\sum_{b\asymp B}H_{b,U}(0)\right|^2
 \ll_\varepsilon X^\varepsilon{B\over U}\mathcal E_U
\]

therefore converts the boxed estimate, together with the already owned
pieces, to \(J^{7/5}=J^2/T\) at coefficient level.

The capacity identity is

\[
\begin{aligned}
 \mathsf C_{82}&=B^3T^2Q^{-5/12},&
 \mathsf T_{82}&=J^{7/5},\\
 \mathsf C_{\rm Gram}&=(U/B)\mathsf C_{82}^2,&
 \mathsf T_{\rm Gram}&=(U/B)\mathsf T_{82}^2.
\end{aligned}
\]

At \(B=J^{3/20}\), the linear gap is \(J^{1/12}\) and the Gram gap is
\(J^{1/6}\); Toeplitz square-roots the latter back to the former.

## 4. Exact M2 row-to-energy bridge

For the exact odd top-frequency support \(\mathscr H_L\), define

\[
\begin{aligned}
 \mathcal T_{\mathrm{end},L}
 &=\sum_{h\in\mathscr H_L}\chi_4(h)
   \sum_{\lceil h/4\rceil\leq m\leq h}
   a_{\mathrm{end}}(h,m)e(J\sqrt{hm}),\\
 R_m&=\sum_{\substack{h\in\mathscr H_L\\m\leq h\leq4m}}
   \chi_4(h)a_{\mathrm{end}}(h,m)e(J\sqrt{hm}),\\
 \mathcal E_L^\top&=\sum_m|R_m|^2.
\end{aligned}
\]

The exact finite regrouping and Cauchy inequality are

\[
 \mathcal T_{\mathrm{end},L}=\sum_mR_m,\qquad
 |\mathcal T_{\mathrm{end},L}|^2\leq
 \#\{m:R_m\ne0\}\mathcal E_L^\top
 \ll L\mathcal E_L^\top.
\]

The diagonal, fixed physical collars, original Poisson zero and
positive modes, equality modes, wrong-sign tails, entry/exit errors,
primitive square rays, exact nonsquare centers, and positive-safe
blocks are already owned with total \(O_\varepsilon(L^2X^\varepsilon)\).
The phrase “original Poisson zero mode” refers to the Round-77 Poisson
index.  It is not the metric-window Fourier index \(r=0\) below.

## 5. Exact M2 hard block and open core

For a primitive odd coprime ray \(a<b<4a\), put

\[
\begin{aligned}
 q&=(b-a)/2,\qquad
 u_{\mathrm{ang}}
 ={q\over (a+b)/2+\sqrt{ab}}
 ={\sqrt b-\sqrt a\over\sqrt b+\sqrt a},\\
 \Lambda&=Xq u_{\mathrm{ang}}
 ={X(\sqrt b-\sqrt a)^2\over2}.
\end{aligned}
\]

The literal reciprocal interval is

\[
 {Ju_{\mathrm{ang}}\over1-u_{\mathrm{ang}}}<k<
 {2Ju_{\mathrm{ang}}\over1+u_{\mathrm{ang}}},
\]

equivalently

\[
 {J(\sqrt b-\sqrt a)\over2\sqrt a}<k<
 {J(\sqrt b-\sqrt a)\over\sqrt b}.
\]

On one residual block,

\[
\begin{gathered}
 a\asymp A_{\mathrm{ray}},\qquad
 b-a\asymp D_{\mathrm{ray}},\qquad
 k\asymp K_{\mathrm{rec}},\qquad
 |\mathcal G_{a,b}|\asymp G_{\mathrm{lift}},\\
 K_{\mathrm{rec}}\asymp {JD_{\mathrm{ray}}\over A_{\mathrm{ray}}},
 \qquad
 G_{\mathrm{lift}}\asymp {L\over A_{\mathrm{ray}}},
 \qquad
 \rho={A_{\mathrm{ray}}JD_{\mathrm{ray}}^3\over L^3}\gg1.
\end{gathered}
\]

Primitive square rays, exact nonsquare centers, and \(\rho\ll1\)
blocks are excluded as prior owners.  Let \(W_R\) be the fixed smooth
punctured metric partition, supported on

\[
 0<c_1/R_{\mathrm{met}}\leq\|\Lambda/k\|
 \leq c_2/R_{\mathrm{met}}<1/2,
 \qquad 1\leq R_{\mathrm{met}}\leq N_{a,b}\ll G_{\mathrm{lift}},
\]

and write

\[
 W_R(t)=\mu_R+\sum_{r\ne0}\widehat W_R(r)e(rt),
 \qquad \mu_R\asymp R_{\mathrm{met}}^{-1}.
\]

For the actual odd lift set \(\mathcal G_{a,b}\), define

\[
 \mathfrak C^\circ_{a,b,k}(g)
 =\int_{gb/4}^{ga}A^\circ_{ga,gb}(x)
 e\!\left(kx-J(\sqrt{gb}-\sqrt{ga})\sqrt x\right)\,dx.
\]

This retains every Round-77 profile, floor, star, collar, finite-lift,
and transition convention.  Put

\[
\begin{aligned}
 \Omega_{h,s,g}&={X(\sqrt s-\sqrt h)^2\over2g}=\Lambda,\\
 \mathcal K_{R;h,s,g}(x)
 &=\sum_{k\ {\rm in\ the\ reciprocal\ interval}}
   \omega(k)W_R(\Omega_{h,s,g}/k)e(kx),\\
 \mathcal K_{r;h,s,g}(x)
 &=\sum_{k\ {\rm in\ the\ reciprocal\ interval}}
   \omega(k)e\!\left(kx+{r\Omega_{h,s,g}\over k}\right).
\end{aligned}
\]

Then

\[
 \mathcal K_R=\mu_R\mathcal K_0+
 \sum_{r\ne0}\widehat W_R(r)\mathcal K_r,
\]

and the retained \(r=0\) term is the metric density mode.  It is not
one of the earlier Round-77 Poisson-mode owners.

The exact hard contribution on a block is

\[
\begin{aligned}
 \mathfrak Q_{A,D,K,G,R}
 ={}&\sum_{\substack{a,b\ {\rm residual}\\ab\ne\square}}
 \sum_{g\in\mathcal G_{a,b}}
 \chi_4(ga)\chi_4(gb)\\
 &\times\int_{gb/4}^{ga}A^\circ_{ga,gb}(x)
 e\!\left(-J(\sqrt{gb}-\sqrt{ga})\sqrt x\right)
 \mathcal K_{R;ga,gb,g}(x)\,dx.
\end{aligned}
\]

The accepted one-count reduction has the form

\[
 \mathcal E_L^\top
 =\mathcal E_{\mathrm{owned},L}
  +2\Re\sum_{A,D,K,G,R}\mathfrak Q_{A,D,K,G,R},
\qquad
 \mathcal E_{\mathrm{owned},L}
 \ll_\varepsilon L^2X^\varepsilon,
\]

with the \(O(L^2\log(2+L))\) transformation error absorbed into the
owned term.  Hence the canonical hard-top M2 theorem target is

\[
 \boxed{\;
 \sum_{A,D,K,G,R}|\mathfrak Q_{A,D,K,G,R}|
 \ll_\varepsilon L^2X^\varepsilon.
 \;}
\]

It implies \(\mathcal E_L^\top\ll L^2X^\varepsilon\), and therefore
\(\mathcal T_{\mathrm{end},L}\ll L^{3/2}X^\varepsilon\).
The positive capacity on a hard block is
\(L^2X^\varepsilon\sqrt\rho\); the missing signed gain is exactly
\(\rho^{-1/2}\).

The density term \(\mu_R\mathcal K_0\) and all \(r\ne0\) discrepancy
terms are one coefficient and must be estimated jointly.  The complete
carrier cancels quotient parity and restores integer metric
frequencies, including \(r=0\).  Applying Poisson to the density term
returns the original transposed two-character row.

## 6. False shadows and source guardrails

The two open targets are not replaced by any of the following:

1. arbitrary bounded coefficients in place of either actual symbol;
2. absolute values before the joint signed interaction;
3. the M1 linear row identified with its Gram lift;
4. M1 local period depth, Fourier support, or graph sparsity without a
   joint actual-symbol estimate;
5. deletion of modulus multiples, Ramanujan terms, bad primes, or the
   full \(2\)-part;
6. M2 quotient parity, a half-frequency gap, discrepancy alone, or a
   second reciprocal Poisson step;
7. classification of the ordinary \(1/R\) density as exceptional;
8. an unquantified global moment in place of pointwise endpoint control.

Li--Yang treats a separably weighted double exponential sum
\(\sum_hg(h/H)\sum_mG(m/M)e((hT/M)F(m/M))\), with a nondegenerate
\(C^3\) one-variable phase and explicit Case A/B parameter
inequalities.  It does not literally accept the M1 fourfold
varying-modulus trace or the M2 joint radical moving symbol.

Xiao treats unweighted sums \(\sum_{n/2\leq a\leq n}e(h\sqrt a)\)
through height-averaged second and fourth moments.  Its discrepancy
consequence uses an additional pointwise input.  It does not literally
accept either fixed-\(X\) actual-symbol kernel above.

## 7. Downstream scope and proposed graph effect

The M1 boxed estimate closes only the first-band smooth nonaxial
principal core.  Upper conductors, axes, raw transitions, cone edges,
other radial sectors, alpha/top interfaces, and target-scale endpoint
uniformity remain separate.

The M2 boxed estimate closes only the residual hard top cone.  All
other M2 ranges and final target-scale endpoint owners remain separate.

The lawful graph effect is to create two exact open obligations, one
for each boxed estimate, and point their parent M9-M1 and M9-M2 nodes
to the remaining outside-owner assemblies.  The stale instruction to
extract an unconditional exponent or close R5 must be removed:
Round 91 already proved the \(1/3+\varepsilon\) theorem and R5-Full.
No status changes for M9-M1, M9-M2, M9, endpoint uniformity, the
conditional bridge, or the \(1/4+\varepsilon\) target.
