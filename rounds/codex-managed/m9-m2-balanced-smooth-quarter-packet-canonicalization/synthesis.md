# Round 112 synthesis: balanced smooth quarter-packet canonicalization

Campaign: m9-m2-balanced-smooth-quarter-packet-canonicalization  
Round type: non-core deliverable / canonicalization  
Starting graph SHA-256:
5c49f612b262b1191fe74642ddd8e5d6c70e04b34a59fb1473487d5b5132d747

Resulting graph SHA-256:
9d560539df2db7d69e72dd6e7e6af7247f00237ee795ac13b053b3f34eae8efa

## 1. Conductor decision

Promote only the scoped full-small-gcd normalization, owner-correction rule,
frequency conjugacy, blockwise norm scope, and capacity ledger. Revise the
candidate interface before calling it a standalone literal actual-symbol
theorem. Retain the signed balanced estimate and every downstream theorem
as open.

All three independent reports agree on the decisive point:

- the \(1/(2i)\) factor and \(1/4\)-minus-\(3/4\) packet are exact;
- the smooth Poisson packet represents the full small-gcd shell;
- exact-square and near-square owners require explicit signed subtraction;
- the outside-absolute \(\omega\)-sum may contain only internal
  subdivisions of one fixed physical \((D,L,+)\) block; and
- the frozen artifacts do not instantiate the finite owner-aware atom
  dictionary needed for the requested literal theorem.

This is a successful exit through the round's “first exact failed seam”
gate. It proves no analytic packet bound and changes no exponent.

## 2. Exact certified normalization

Fix one real smooth positive-frequency physical block
\[
B=(X,D,L,H_D,W_D,v_L,+),\qquad
H_D=\lfloor DX^{-1/4}\rfloor,
\]
put
\[
R=\sqrt X,\qquad K=\frac{XL}{D^2},\qquad 1\le K/L\le16,
\]
and let \(\Omega_B\) index only finitely many internal smooth
subdivisions of this block. On a fixed smooth gcd shell, write
\[
h=gu,\qquad k=gv,\qquad (u,v)=1.
\]
For a nonzero character term, \(g,u\) are odd and
\(\chi_4(gu)=\chi_4(g)\chi_4(u)\).

Assume the literal bridge
\[
\psi_G(g)A_{B,\omega}(gu,gv;X)
=F_{B,\omega,u,v,G}(g/G),
\tag{112.S1}
\]
where \(F\) is the real \(C_c^\infty\) extension of the complete physical
profile. With
\[
\widehat F(\xi)=\int_{\mathbb R}F(t)e(-t\xi)\,dt,
\qquad
\chi_4(g)=\frac{e(g/4)-e(3g/4)}{2i},
\]
Poisson gives
\[
\begin{aligned}
Q_{B,\omega,G}^{\mathrm{full}}(R)
=\sum_{\substack{(u,v)=1\\u\ \mathrm{odd}}}\chi_4(u)\sum_n\Big[
&\widehat F_{B,\omega,u,v,G}
 \!\left(G(n-R\sqrt{uv}-\tfrac14)\right)\\
-&\widehat F_{B,\omega,u,v,G}
 \!\left(G(n-R\sqrt{uv}-\tfrac34)\right)
\Big].
\end{aligned}
\tag{112.S2}
\]
If \(\mathcal G_B^\circ\) contains only shells wholly below
\(g=L^{1/2}\), then
\[
T_{B,\mathrm{small}}^{+,\mathrm{full}}
=\frac1{2i}\sum_{\omega\in\Omega_B}
  \sum_{G\in\mathcal G_B^\circ}GQ_{B,\omega,G}^{\mathrm{full}}(R)
+E_{B,\mathrm{gcd\text{-}bd}}.
\tag{112.S3}
\]
The boundary shell meeting \(L^{1/2}\) is explicit and belongs to the
target-safe large-gcd budget.

For real profiles,
\[
Q_{B,\omega,G}^{\mathrm{full}}(-R)
=-\overline{Q_{B,\omega,G}^{\mathrm{full}}(R)}.
\tag{112.S4}
\]
The minus sign cancels the minus from conjugating \(1/(2i)\), so the
physical negative-frequency child is the conjugate of the positive one.
Generic complex symbols do not satisfy this rule.

## 3. Owner correction and one-count scope

The displayed smooth packet cannot simultaneously be called the transform
of an arithmetic owner complement. Let \(T_{B,\mathsf{Sq},<}^+\) and
\(T_{B,\mathsf{Near},<}^+\) be the exact signed small-gcd restrictions to
\[
hk\ \text{square},
\qquad
hk\notin\square,\quad
\operatorname{dist}(\sqrt{hk},\mathbb Z)\le R^{-1},
\]
under one fixed priority convention. Then the lawful residual identity is
\[
\begin{aligned}
T_{B,\mathrm{res}}^+
=\frac1{2i}\sum_{\omega,G}GQ_{B,\omega,G}^{\mathrm{full}}(R)
+E_{B,\mathrm{gcd\text{-}bd}}
-T_{B,\mathsf{Sq},<}^+
-T_{B,\mathsf{Near},<}^+.
\end{aligned}
\tag{112.S5}
\]
The three correction terms are target-safe. Inserting their arithmetic
indicator into \(F\) would destroy the asserted uniformly smooth gcd
profile.

The index \(\omega\) in (112.S2)--(112.S5) may only recombine bounded
internal subdivisions of this one block \(B\). Distinct \(D\)- and
\(L\)-blocks are estimated separately and are summed only after their
magnitudes have been bounded. The accepted physical assembly licenses no
cancellation across those blocks.

The direct open estimate is therefore
\[
\boxed{
\left|\sum_{\omega\in\Omega_B}
 \sum_{G\in\mathcal G_B^\circ}
 GQ_{B,\omega,G}^{\mathrm{full}}(R)\right|
\ll_\varepsilon L^{3/2}X^\varepsilon
}
\tag{112.S6}
\]
for every fixed literal balanced smooth block \(B\). Shellwise
\(\sum_{\omega,G}G|Q_{B,\omega,G}|\), product-fibre absolute values, and
character-preserving Cauchy/Gram estimates are stronger sufficient norms,
not equivalent formulations.

## 4. First unresolved seam

The frozen Round-112 artifacts name but do not define the complete finite
dictionary
\[
\mathscr A_{D,L}(X)
=\{\Omega_B,\ W_{B,\omega},\ v_{B,\omega},\
\text{floor/star/crossing tags},\
A_{B,\omega},\ E_{B,\omega,\mathrm{tr}}\}.
\tag{112.S7}
\]
They provide the accepted template
\[
A_{B,\omega}(h,k)
=q_{B,\omega}(h)
 \left(\frac{LK}{hk}\right)^{3/4}
 W_{B,\omega}\!\left(\sqrt{\frac{hX}{4kD^2}}\right),
\qquad
q_{B,\omega}(h)
=\Phi\!\left(\frac{h}{H_D+1}\right)v_{B,\omega}(h),
\tag{112.S8}
\]
but the literal profile list, clipped/starred coefficients, support
crossings, and exact finite subdivision identity are not instantiated
coefficientwise. Symbols such as “the actual profile” and
\(F_{B,\omega,u,v,G}\) cannot serve as their own definitions.

Accordingly, (112.S1) is the first unresolved formal antecedent. Once
(112.S7) is supplied and checked, (112.S6) is the first genuinely analytic
gap.

## 5. Capacity and source audit

The current balanced envelope is
\[
|\mathcal T_{L,L}(R)|
\ll_\varepsilon X^\varepsilon
\min(L^2,R^{1/2}L^{1/2}).
\]
Relative to \(L^{3/2}\), its loss is
\[
\min\!\left(L^{1/2},\frac{R^{1/2}}L\right),
\]
whose maximum is
\[
R^{1/6}=X^{1/12}
\]
at \(L=R^{1/3}=X^{1/6}\). Canonicalization changes neither capacity nor
the global exponent.

The hostile audit checked the literal primary hypotheses of
Kowalski--Robert--Wu Proposition 5 and Robert--Sargos Theorem 2.
Kowalski--Robert--Wu applies only after smooth coefficient separation and
is dominated by the accepted envelope here. Robert--Sargos is an unsigned
square-root spacing count and erases both \(\chi_4(u)\) and the signed
quarter-packet difference. Vaaler supplies the finite coefficient
normalization only, and the Tao--Trudgian--Yang theorem is one-variable and
out of the balanced packet's literal scope. No source proves (112.S6).

Complementary divisors also do not close it: a symmetric symbol cancels
only odd products \(m\equiv3\pmod4\), reinforces
\(m\equiv1\pmod4\), and gives no character-bearing swapped term for even
products.

## 6. Controls and nonimplications

- Reversing the \(1/4\) and \(3/4\) terms changes the sign.
- The packet relation is \(Q(-R)=-\overline{Q(R)}\), not
  \(Q(-R)=\overline{Q(R)}\).
- A sharp gcd cutoff introduces an unowned Fourier tail.
- An arithmetic square/near-square mask is not a smooth \(g/G\)-profile.
- Shellwise \(\ell^1\), product-fibre absolute values, and Gram bounds do
  not follow from the direct outside-absolute target.
- The hard profile containing \(d=\lfloor\sqrt X\rfloor\) is outside the
  smooth packet even when its scale exponent tends to \(1/2\).
- Phase-conjugating arbitrary coefficients disprove coefficient-uniform
  versions but are not lower bounds for the actual packet.
- No M9-M1 statement is involved.

## 7. State effect and next deliverable

Create one proved guardrail node for the normalization, explicit
owner-correction rule, blockwise \(\omega\)-scope, conjugacy, and norm
hierarchy. Update the proved abstract small-gcd reduction and the open
balanced estimate with these guardrails. Retain the analytic estimate,
hard child, unbalanced child, M9-M2, endpoint uniformity, M9, and GC target
as open.

The next non-core deliverable should instantiate (112.S7) directly from the
accepted dyadic-profile certificate, exact Vaaler coefficient, and smooth
stationary-transform formula. It must not attempt the signed estimate until
the coefficientwise dictionary and one-count equality validate.
