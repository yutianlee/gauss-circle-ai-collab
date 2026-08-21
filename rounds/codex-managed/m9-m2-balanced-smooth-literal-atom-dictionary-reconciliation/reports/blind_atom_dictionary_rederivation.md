## 1. Result: a repaired identity exists, but the literal dictionary is not a complete lemma

The finite denominator and frequency telescopes, the balanced-ratio formula, the integer gcd partition, the \(1/4\)-minus-\(3/4\) character packet, and the coefficientwise one-count equation are algebraically correct. The stationary-phase leading constant is also the stated

\[
-\frac{e(1/8)}{2\pi}X^{1/4}M^{-3/4}.
\]

The statement nevertheless cannot be promoted as an exact finite smooth atom dictionary. There are four independent defects.

1. The first displayed \(d\)-sum contains \(d=0\), where \(e(hX/(4d))\) is undefined. The fact that \(W(0)=0\) does not define a product with an undefined phase.
2. \(A_{j,r}\) is introduced only on integer coefficient indices and is then evaluated at the real arguments \((G_\sigma tu,G_\sigma tv)\). If the displayed hard indicator in \(v_r\) is extended literally to real arguments, an admissible balanced block makes \(F_{\sigma,u,v}\) discontinuous. Thus the claimed uniform smooth seminorms are false under that literal extension, and the classical rapidly convergent Poisson packet is not justified.
3. The statement defines \(B_{2,j,r}=8\operatorname{Re}{\cal B}_{j,r}^{+}\), but supplies no antecedent two-sided physical formula from which the factor \(8\) can be derived. Pairing positive and negative frequencies gives a factor \(2\); an additional physical multiplicity \(4\) has to be stated separately.
4. The high-gcd subtotal and the exact transform-error atom are not defined. Consequently the displayed residual is the low-gcd packet minus square and near-square pieces, but it is not yet an exact formula for the full transformed packet minus every named prior owner.

A coefficient-preserving repair is available: either replace the \(d\)-sum by \(d\geq1\), or explicitly define the entire \(d=0\) summand (not merely its weight) to be \(0\); specify the two-sided conjugacy and physical multiplicity; extend \(v_r\) off the integers by the smooth function \(W(x/L)\) for residual labels \(r\geq1\); define \(F\) to be zero before evaluating its positive-real formula outside its support; and define literal high-gcd and normalized transform-error subtotals. The \(d=0\) convention and smooth extension completely close their two local seams without changing a single coefficient. Under those additions, all gcd and one-count identities below are exact. The correct state-level conclusion is therefore **revise**, not promote.

## 2. Exact statement and hypotheses

Assume all frozen definitions in the statement packet, with \(X\geq4096\), and let \(j,r\geq1\) be an existing active label: \(D=D_j\geq X^{1/4}\), \(0\leq r<J_H\), and \(1\leq K/L\leq16\). When the original notation \(\sum_{d\in\mathbb Z}\) is retained, additionally define its entire \(d=0\) summand to equal \(0\). This convention is equivalent to summing over \(d\geq1\), because \(W(d/D)=0\) for every \(d<0\). Then the following assertions hold.

**Finite profiles.** On positive integers,

\[
\sum_{0\leq j<J_y}w_j(d)+w_{\rm bot}(d)={\bf1}_{1\leq d\leq y},
\qquad
\sum_{0\leq r<J_H}v_r(h)+v_{{\rm bot},H}(h)={\bf1}_{1\leq h\leq H}.
\]

The second equality includes \(H=1,2\). Active labels have \(H\geq1\); there is no residual label \(r\geq1\) when \(H=1\) or \(H=2\).

**Balanced boundary.** Exactly, with no asymptotic replacement of the floor \(y=\lfloor\sqrt X\rfloor\),

\[
\frac KL=\frac X{D_j^2}=4^j\frac X{y^2}.
\]

For real \(X\geq4096\), \(j=1\) always satisfies the balanced inequality, \(j=2\) does so only when \(X=y^2\), and no \(j\geq3\) does so.

**Integer gcd partition.** Put

\[
p_{\rm low}(g):=\sum_{s<S}\psi_s(g)+\psi_{\rm bot}(g).
\]

For every \(g\in\mathbb N\),

\[
p_{\rm low}(g)=\eta(g/G_0),\qquad
\psi_{\rm hi}(g)=1-\eta(g/G_0),\qquad
p_{\rm low}(g)+\psi_{\rm hi}(g)=1.
\]

The high atom is zero for \(g\leq G_0\), is one for \(g\geq3G_0/2\), and owns its stated fractional weight in the transition \(G_0<g<3G_0/2\). At \(g=G_0\), if this is an integer, the low side owns the whole coefficient.

**Repaired smooth interpolation.** For the purpose of defining a real test function, set

\[
\widetilde v_r(x)=W(x/L)\quad(x>0)
\]

and form \(\widetilde A\) by replacing \(v_r\) by \(\widetilde v_r\). For \(r\geq1\), this changes no positive-integer coefficient. Define

\[
\widetilde F_{\sigma,u,v}(t)=
\begin{cases}
\vartheta_\sigma(t)\widetilde A(G_\sigma tu,G_\sigma tv),&t>0,\\
0,&t\leq0,
\end{cases}
\]

where the second branch is chosen before evaluating any power or square root. Then \(\widetilde F\) is real and \(C_c^\infty(\mathbb R)\), supported in \([1/2,3/2]\). For every integer \(m\geq0\),

\[
\sup_{t\in\mathbb R}\left|(t\partial_t)^m\widetilde F_{\sigma,u,v}(t)\right|
\leq C_m
\left(\frac{M}{G_\sigma^2uv}\right)^{3/4},
\]

with \(C_m\) independent of real \(X,j,r,\sigma,u,v\). This is a precise scale-normalized seminorm statement; the packet itself did not specify which seminorm was intended.

**Exact low packet and one count.** Define

\[
{\cal T}^{\rm full}:=\sum_{h,k\geq1}\chi_4(h)A_{j,r}(h,k)e(R\sqrt{hk}),
\]

and define \({\cal T}^{\rm low}\) and \({\cal T}^{\rm hi}\) by inserting \(p_{\rm low}((h,k))\) and \(\psi_{\rm hi}((h,k))\), respectively. With \(Q_\sigma\) constructed from the repaired test function,

\[
{\cal T}^{\rm low}=\frac1{2i}\sum_\sigma G_\sigma Q_\sigma(R),
\qquad
{\cal T}^{\rm full}={\cal T}^{\rm low}+{\cal T}^{\rm hi}.
\]

Let

\[
I_{\rm sq}(h,k)={\bf1}_{hk\text{ is a square}},
\]

\[
I_{\rm near}(h,k)={\bf1}_{hk\text{ is not a square}}
 {\bf1}_{\operatorname{dist}(\sqrt{hk},\mathbb Z)\leq R^{-1}},
\qquad
I_{\rm far}=1-I_{\rm sq}-I_{\rm near}.
\]

Define \({\cal S}^{\rm sq}\), \({\cal S}^{\rm near}\), and \({\cal T}^{\rm res}\) by inserting, respectively, \(p_{\rm low}I_{\rm sq}\), \(p_{\rm low}I_{\rm near}\), and \(p_{\rm low}I_{\rm far}\) into \({\cal T}^{\rm full}\). Then

\[
{\cal T}^{\rm res}
=\frac1{2i}\sum_\sigma G_\sigma Q_\sigma(R)
-{\cal S}^{\rm sq}-{\cal S}^{\rm near}
\]

and the stronger one-count identity is

\[
{\cal T}^{\rm full}
={\cal T}^{\rm hi}+{\cal S}^{\rm sq}
+{\cal S}^{\rm near}+{\cal T}^{\rm res}.
\]

**Exact transform-error repair.** Let

\[
C=\frac{e(1/8)}{2\pi}X^{1/4}M^{-3/4},
\qquad
E_{\rm tr}:={\cal B}_{j,r}^{+}+C{\cal T}^{\rm full},
\qquad
{\cal S}^{\rm tr}:=C^{-1}E_{\rm tr}.
\]

This is an exact definition, whether or not the claimed \(E_{\rm tr}=O(1)\) has been proved. It gives

\[
{\cal B}_{j,r}^{+}=-C\bigl({\cal T}^{\rm full}-{\cal S}^{\rm tr}\bigr).
\]

Thus a packet from which high gcd, low squares, low near-squares, and transform error have all been removed is

\[
{\cal T}^{\rm target}
=\frac1{2i}\sum_\sigma G_\sigma Q_\sigma(R)
-{\cal S}^{\rm sq}-{\cal S}^{\rm near}-{\cal S}^{\rm tr}.
\]

An exact physical formula with the further factor \(8\) additionally requires the missing physical multiplicity and negative-frequency convention described below.

## 3. Proof or derivation

The cutoff \(\eta\) is \(C^\infty\), equals \(1\) on \((-\infty,1]\), and equals \(0\) on \([3/2,\infty)\). On its transition it is decreasing. Hence \(W(t)=\eta(t)-\eta(2t)\) is a real nonnegative \(C^\infty\) function supported in \([1/2,3/2]\). In particular,

\[
W(1)=1,\qquad W(g)=0\quad(g\in\mathbb N,\ g\geq2).
\]

For \(D_{j+1}=D_j/2\),

\[
W(d/D_j)=\eta(d/D_j)-\eta(d/D_{j+1}).
\]

Therefore

\[
\sum_{j=0}^{J_y-1}W(d/D_j)+\eta(d/D_{J_y})=\eta(d/y)=1
\]

for \(1\leq d\leq y\). The displayed hard indicators make both sides zero outside this integer interval. The \(j=0\) cutoff is genuinely needed because \(W(d/y)\) can extend above \(y\); for \(j\geq1\), \(d\leq3D_j/2\leq3y/4\), so the upper clip is redundant.

The identical calculation with \(L_{r+1}=L_r/2\) gives

\[
\sum_{r=0}^{J_H-1}W(h/L_r)+\eta(h/L_{J_H})=\eta(h/H)=1
\]

for \(1\leq h\leq H\). For \(H=1\), \(J_H=0\), so the sole bottom value is \(\eta(1)=1\). For \(H=2\), \(J_H=1\): at \(h=1\), \(W(1/2)+\eta(1)=0+1\), and at \(h=2\), \(W(1)+\eta(2)=1+0\). If \(D\geq X^{1/4}\), then \(H=\lfloor DX^{-1/4}\rfloor\geq1\). For \(H=1,2\), \(J_H\leq1\), so no index \(r\geq1\) exists. For any existing \(r\geq1\), \(L\leq H/2\), and the support of \(W(h/L)\) gives \(h\leq3H/4\); the upper frequency clip is then redundant on integer samples.

The balanced identity is direct:

\[
K/L=X/D_j^2=X/(2^{-2j}y^2)=4^jX/y^2.
\]

Because \(y^2\leq X<(y+1)^2\) and \(y\geq64\), the \(j=1\) value lies in

\[
4\leq4X/y^2<4(65/64)^2<16.
\]

For \(j=2\), it is at least \(16\), with equality exactly when \(X=y^2\); otherwise it is greater than \(16\). Every \(j\geq3\) is greater than \(16\).

The positive Vaaler normalization is exact because

\[
2i\alpha_{h,H}=-\frac{\Phi(h/(H+1))}{\pi h}.
\]

The stationary constant can be checked independently at the level of one Poisson integral. The negative Poisson index \(-k\), \(k\geq1\), has phase

\[
f(d)=\frac{hX}{4d}+kd,\qquad
d_0=\sqrt{\frac{hX}{4k}},\qquad
f(d_0)=\sqrt{hXk},\qquad
f''(d_0)=\frac{4k^{3/2}}{(hX)^{1/2}}.
\]

For the convention \(e(t)=e^{2\pi it}\), its leading stationary factor is

\[
e(1/8)\,f''(d_0)^{-1/2}
=e(1/8)\frac{(hX)^{1/4}}{2k^{3/4}}.
\]

Multiplication by the outer coefficient \(-\Phi/(\pi h)\) gives

\[
-\frac{e(1/8)}{2\pi}X^{1/4}
v_r(h)\Phi(h/(H+1))(hk)^{-3/4}
W\!\left(\sqrt{\frac{hX}{4kD^2}}\right),
\]

which is exactly \(-C A_{j,r}(h,k)\), since \(M^{-3/4}(M/(hk))^{3/4}=(hk)^{-3/4}\). This checks the sign, \(e(1/8)\), and \(1/(2\pi)\). It does not, by itself, prove a uniform total \(O(1)\) remainder.

For positive/negative recombination, write \(z_h=\sum_{d\geq1}W(d/D)e(hX/(4d))\). Then \(z_{-h}=\overline{z_h}\). If the negative coefficient is explicitly defined to equal the real positive coefficient

\[
c_h=-\frac{\chi_4(h)v_r(h)\Phi(h/(H+1))}{\pi h},
\]

then the two-sided pair is \(c_hz_h+c_hz_{-h}=2\operatorname{Re}(c_hz_h)\). This proves only the factor \(2\). The packet contains no formula asserting that the physical block is four times this two-sided sum, so \(8=4\cdot2\) is not derivable; as written, it is merely part of the definition of \(B_{2,j,r}\).

For the gcd telescope, \(G_{s+1}=G_s/2\), whence

\[
\sum_{s<S}\psi_s(g)=\eta(g/G_0)-\eta(g/G_S).
\]

The definition of \(S\) ensures \(G_S\leq1\). For an integer \(g\geq2\), both \(\eta(g/G_S)\) and \(W(g)\) vanish. For \(g=1\), \(\eta(1/G_S)=c_L\) and \(W(1)=1\). Adding \(c_LW(g)\) consequently gives \(p_{\rm low}(g)=\eta(g/G_0)\) for every positive integer. The claimed support and boundary ownership of \(\psi_{\rm hi}=1-p_{\rm low}\) follow from the plateau and support of \(\eta\).

Now write \(h=gu,k=gv\), where \(g=(h,k)\) and \((u,v)=1\). The term vanishes unless \(u\) is odd, and then

\[
\chi_4(gu)=\chi_4(g)\chi_4(u),\qquad
\chi_4(g)=\frac{e(g/4)-e(3g/4)}{2i}.
\]

For a low shell, \(\vartheta_\sigma(g/G_\sigma)A(gu,gv)=\widetilde F_{\sigma,u,v}(g/G_\sigma)\) at all positive integer samples. Poisson summation with

\[
\sum_{g\in\mathbb Z}F(g/G)e(ag)
=G\sum_{n\in\mathbb Z}\widehat F(G(n-a))
\]

and \(a=R\sqrt{uv}+1/4\) or \(a=R\sqrt{uv}+3/4\) gives exactly

\[
{\cal T}_\sigma=\frac{G_\sigma}{2i}Q_\sigma(R).
\]

Summing the low shells proves the packet identity. Uniqueness of \(g=(h,k)\), together with \(p_{\rm low}+\psi_{\rm hi}=1\), proves the gcd one count. The indicators \(I_{\rm sq},I_{\rm near},I_{\rm far}\) are pairwise disjoint and sum to one, so multiplying that equality by \(p_{\rm low}\) proves the square/near/residual one count. Large gcd has priority because all of \(\psi_{\rm hi}\) is assigned before the low indicators are applied.

For the repaired smooth interpolation, on the support of \(\vartheta_\sigma\) one has \(1/2\leq t\leq3/2\). The slanted stationary cutoff becomes

\[
W\!\left(\sqrt{\frac{uX}{4vD^2}}\right),
\]

which is independent of \(t\). The remaining nonconstant factors are

\[
\vartheta_\sigma(t)W(G_\sigma tu/L)
\Phi(G_\sigma tu/(H+1))t^{-3/2}
\left(\frac{M}{G_\sigma^2uv}\right)^{3/4}.
\]

Whenever the second \(W\)-factor is nonzero, \(G_\sigma tu\leq3L/2\leq3H/4\). Hence the argument of \(\Phi\) stays in a fixed compact subinterval of \([0,1)\), where \(\Phi\) has its smooth removable extension at zero. Repeated \(t\partial_t\) derivatives are therefore uniformly bounded after division by \((M/(G_\sigma^2uv))^{3/4}\). Flatness of \(W\) at its support endpoints gives a \(C_c^\infty\) zero extension.

The literal interpolation fails. Take

\[
X=810000,\quad R=y=900,\quad j=1,\quad D=450,\quad H=15,
\quad r=3,\quad L=15/8.
\]

Then \(K/L=X/D^2=4\), so this is balanced, and \(J_H=4\), so \(r=3\) exists. Moreover

\[
G_0=\sqrt{15/32}<1,\quad S=0,\quad
1/G_0=\sqrt{32/15}\in(1,3/2),
\]

so \(c_L=\eta(1/G_0)>0\). Choose the bottom atom and \(u=v=1\). Under the literal real extension

\[
v_r(t)=W(t/L){\bf1}_{1\leq t\leq15},
\]

the resulting \(F(t)\) is zero for \(t<1\) sufficiently close to \(1\), while at \(t=1\) every factor is positive:

\[
c_L>0,\quad W(1)=1,\quad W(1/L)=W(8/15)>0,
\quad \Phi(1/16)>0,\quad
W\!\left(\sqrt{X/(4D^2)}\right)=W(1)=1.
\]

Thus \(F(1)>0\) but its left limit is zero. This is an exact counterexample to the literal smooth-seminorm claim.

The natural repair \(v_r^{\rm sm}(x)=W(x/L_r)\) closes this seam completely for every \(r\geq1\). Indeed, on positive integer samples with \(1\leq h\leq H\) it is identical to \(v_r(h)\), while for every integer \(h>H\) one has \(h/L_r>H/L_r=2^r\geq2\), so \(W(h/L_r)=0\). There is no positive integer below \(1\). Thus the repaired interpolation preserves every coefficient, removes both hard endpoints, gives the uniform seminorm bound already proved, and legitimizes the classical Poisson formula. This is a local repair, not a continuing obstruction; it does not supply the separate factor \(4\), the high-gcd owner subtotal, or the transform-error atom.

## 4. First doubtful or unproved step

The first undefined datum in textual order is the \(d=0\) summand in

\[
\sum_{d\in\mathbb Z}W(d/D)e(hX/(4d)).
\]

It must be replaced by a sum over \(d\neq0\), or, using the support of \(W\), by \(d\geq1\). An equally valid repair is the explicit convention

\[
\left.W(d/D)e(hX/(4d))\right|_{d=0}:=0
\]

for the entire summand. Declaring only \(W(0)=0\) is not enough to assign a value to the phase. Once the entire-summand convention is made, the zero and all negative indices vanish, so this seam is fully closed and the value is exactly the \(d\geq1\) sum.

After that harmless repair, the first normalization that cannot be proved from the packet is the factor \(8\): the data prove a positive/negative pairing factor \(2\), but do not supply the separate physical factor \(4\). The first outright false smoothness claim occurs later at the real interpolation \(F_{\sigma,u,v}\), as shown by the balanced counterexample in Section 3.

Before any signed estimate, the following data still have to be supplied explicitly:

- the negative-frequency coefficient/conjugacy convention and the source of the physical multiplicity \(4\);
- the smooth positive-real extension of \(A_{j,r}\) and the exact definition of the intended scale-normalized seminorms;
- the high-gcd signed subtotal \({\cal T}^{\rm hi}\) and its owner tag;
- the exact transform remainder \(E_{\rm tr}\), its normalized correction \({\cal S}^{\rm tr}\), and its owner/sign;
- the equation specifying which whole residual block, if any, has already been removed by a prior whole-block owner.

The mere notation \(O(1)\) cannot serve as a coefficientwise atom or preserve a sign. Likewise, the sentence that prior owners are whole-block tags correctly forbids arithmetic masking, but it does not specify the actual whole-block ownership datum.

## 5. Control tests and outcomes

**`denominator_telescoping_and_hard_profile`.** Input: \(D_j=2^{-j}y\), all \(0\leq j<J_y\), and the bottom term. Invariant: the weights must sum to the hard profile on every integer. Observed: the telescope equals \(\eta(d/y)=1\) on \(1\leq d\leq y\), and all displayed terms have the common hard indicator outside. The top clip is necessary; lower shells do not cross \(y\). Outcome: pass exactly.

**`frequency_telescoping_top_bottom_and_clipping`.** Input: arbitrary integer \(H\geq1\), all \(0\leq r<J_H\), and the frequency bottom. Invariant: one count on \(1\leq h\leq H\), including both edges. Observed: the telescope equals \(\eta(h/H)=1\). The \(r=0\) clip is needed, while for \(r\geq1\) the upper clip is redundant on integer samples. Outcome: pass exactly; the hard clip must not be carried literally into the real interpolation.

**`height_floor_and_empty_block`.** Input: active \(D\geq X^{1/4}\) and \(H=\lfloor DX^{-1/4}\rfloor\). Invariant: no undefined logarithm or nonexistent residual index. Observed: \(H\geq1\); \(H=1\) has only its bottom atom, \(H=2\) has \(r=0\) and its bottom, and neither admits \(r\geq1\). Outcome: pass after declaring such residual blocks empty.

**`exact_Phi_and_positive_frequency_constant`.** Input: the displayed \(\alpha_{h,H}\), one stationary pair \((h,k)\), and the \(e(t)=e^{2\pi it}\) convention. Invariant: coefficient and phase constants must agree without an asymptotic rescaling. Observed: \(2i\alpha=-\Phi/(\pi h)\), \(f(d_0)=R\sqrt{hk}\), and the Hessian gives \(e(1/8)(hX)^{1/4}/(2k^{3/4})\). Outcome: the stated \(-e(1/8)X^{1/4}M^{-3/4}/(2\pi)\) leading constant passes; the total uniform \(O(1)\) remainder is not established by the packet.

**`positive_negative_frequency_recombination`.** Input: real \(d\)-weights and a symmetric negative coefficient. Invariant: \(z_{-h}=\overline{z_h}\) and paired coefficients must be conjugate-compatible. Observed: the pair is exactly \(2\operatorname{Re}{\cal B}^{+}\). No supplied datum yields the additional factor \(4\). Outcome: factor \(2\) passes conditionally; factor \(8\) is unproved except as a definition.

**`balanced_ratio_boundary_and_real_X`.** Input: real \(X\geq4096\), \(y=\lfloor\sqrt X\rfloor\), and \(D_j=2^{-j}y\). Invariant: floors may not be replaced by \(y=\sqrt X\). Observed: \(K/L=4^jX/y^2\); \(j=1\) always qualifies, \(j=2\) only at \(X=y^2\), and \(j\geq3\) never qualifies. Outcome: pass, with the isolated real-\(X\) boundary recorded.

**`smooth_gcd_one_count_and_boundary_owner`.** Input: every \(g\in\mathbb N\), including \(g=1\), powers-of-two values of \(G_0\), and \(S=0\). Invariant: all low weights plus high weight equal one, and the bottom must replace the final telescope value. Observed: low weight is exactly \(\eta(g/G_0)\); \(c_LW(g)\) supplies precisely the \(g=1\) value \(\eta(1/G_S)\); high owns \(1-\eta(g/G_0)\). Outcome: integer one count passes. The partition has \(S+2\) formal atoms including bottom and high, so it is finite for each block but not uniformly bounded in cardinality as \(L\to\infty\).

**`square_near_square_and_large_gcd_priority`.** Input: each pair \((h,k)\), first the high fractional weight, then low exact squares, then low nonsquares in the near band. Invariant: no pair or fractional coefficient is lost or counted twice. Observed:

\[
\psi_{\rm hi}((h,k))+p_{\rm low}((h,k))
\bigl(I_{\rm sq}+I_{\rm near}+I_{\rm far}\bigr)=1.
\]

Outcome: pass exactly when “near” explicitly excludes squares and square/near tests are performed only inside the low weight. A transition-gcd coefficient is deliberately split, not assigned wholesale to two owners.

**`false_arithmetic_mask_and_unsigned_models`.** Input: (i) a hypothetical prior whole-block tag inserted as a coefficient mask, and (ii) replacement of \(\chi_4(g)\) by absolute, random, or adversarial signs. Invariant: whole-block ownership cannot alter selected coefficients, and the quarter packet must expose its signed dependence. Observed: inserting a nonconstant owner mask changes the coefficient dictionary and is invalid. Also \(\chi_4(g)=(e(g/4)-e(3g/4))/(2i)\) is essential; at \(g=3\) it gives \(-1\), whereas the unsigned model gives \(+1\). The unsigned odd indicator instead has \(0\)- and \(1/2\)-frequency shifts, and arbitrary signs have no fixed two-shift representation. Outcome: the packet is genuinely signed and does not transfer to unsigned or adversarial models.

**`capacity_and_downstream_scope`.** Input: all active balanced labels and all nonzero atom gates. Invariant: the identity must have finite coefficient support at fixed parameters and must not imply the desired estimate. Observed: if \(F\neq0\), then

\[
\frac{L}{3G_\sigma}\leq u\leq\frac{3L}{G_\sigma},
\qquad
\frac{uK}{9L}\leq v\leq\frac{uK}{L},
\]

so only finitely many coprime \((u,v)\) occur. With the repaired \(C_c^\infty\) interpolation, the \(n\)-sum is rapidly convergent. The shell count is \(O(1+\log^+L)\), not an absolute constant. No estimate for \(Q_\sigma\), no owner bound, and no transform-error proof follows. Outcome: identity capacity passes after repair; downstream analytic scope remains entirely open.

The repository-wide controls give the same diagnosis:

- **`raw-vs-weighted`:** the derivation retains the literal \(A_{j,r}\) weight and makes no raw-count-to-weighted-mass inference; no exponent claim is tested.
- **`signed-vs-unsigned`:** true signs give the quarter packet; absolute, random, and adversarial signs fail the fixed \(1/4,3/4\) representation.
- **`known-lower-bound-families`:** no absolute near-collision estimate is asserted, so UNC, TS, and W-1 are not invoked; the statement packet contains no family data with which to make a further comparison.
- **`dyadic-endpoints`:** the algebraic identities use exact \(D\) and remain valid whenever the label exists at \(D=X^{1/4},X^{3/8},X^{1/2}\); no averaging step crosses an endpoint.
- **`real-vs-complex-pairing`:** real symmetric weights support \(2\operatorname{Re}\); genuinely complex or asymmetric weights do not, absent extra conjugacy hypotheses. This is exactly why the factor \(8\) is not certified.
- **`exact-vs-near-resonance`:** exact squares and nonsquare near values are disjoint by definition; no exact-resonance energy is used to bound the near band.
- **`coefficient-adversary`:** the gcd Poisson identity uses the fixed \(\chi_4\) structure at the displayed character identity. The \(\Phi\) factor is retained literally, but no cancellation estimate from it is claimed.
- **`support-and-degeneracy`:** \(u,v,g,h,k\geq1\) excludes \(uv=0\); unique gcd reduction handles repeated denominators; top and bottom clips telescope. The real-interpolation discontinuity falsifies the literal extension, and the coefficient-preserving repair \(v_r^{\rm sm}=W(\cdot/L_r)\) closes it for every residual \(r\geq1\). The explicit entire-summand value \(0\) similarly closes the \(d=0\) degeneracy.

All outcomes above are analytical. No numerical experiment was used as proof or evidence.

## 6. Dependencies and exact artifacts used

Only the following artifacts were read or used:

- `rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/briefs/blind_atom_dictionary_rederivation.md`;
- `rounds/codex-managed/m9-m2-balanced-smooth-literal-atom-dictionary-reconciliation/blind_statement.md`;
- `problems/gauss_circle.md`;
- `state/control_models.md`.

No proof graph, strategy file, derivation packet, candidate, earlier balanced-packet derivation, sibling report, web source, or external theorem was consulted. The stationary calculation used only the displayed phase and the Fourier convention in the statement packet. No shared proof-state or sibling artifact was edited.

## 7. Recommended state effect

**Recommendation: revise.** Retain as proved candidate evidence the two finite telescopes, the exact real-\(X\) balanced boundary, the formula \(p_{\rm low}(g)=\eta(g/G_0)\), the signed \(1/4\)-minus-\(3/4\) Poisson identity under a smooth interpolation, the stationary leading constant, and the coefficientwise high/square/near/residual one-count equation.

Reject the literal claims of a fully defined physical normalization and uniform smooth atom family. Before reconsideration, the authoritative statement should:

1. remove \(d=0\) from the reciprocal phase sum or explicitly define the entire \(d=0\) summand to be \(0\);
2. state the negative-frequency coefficient and the independent physical factor \(4\);
3. replace the real hard-clipped \(v_r\) interpolation by \(\widetilde v_r(x)=W(x/L)\) for \(r\geq1\), define \(F=0\) outside the positive formula, and name the seminorm;
4. define \({\cal T}^{\rm hi}\), \(E_{\rm tr}\), \({\cal S}^{\rm tr}\), and the exact prior-owner equation;
5. clarify whether “finite” means finite per block (\(S+2=O(1+\log^+L)\), which is true) or uniformly bounded cardinality (which is false for this construction).

After those repairs, the exact residual to send to a later signed estimate is \({\cal T}^{\rm target}\) from Section 2, not the current formula lacking the transform-error correction. No desired packet estimate is asserted here.
