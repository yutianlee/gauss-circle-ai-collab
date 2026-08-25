# Conductor candidate: Fejer majorant uncertainty and order gate

Campaign: `m9-m2-unbalanced-one-sided-majorant-gate`

This candidate is scoped to the abstract majorant interface. It is not an
upper bound for the literal actual-symbol family.

## 1. Exact multiplier form

For any finitely supported complex sequence \(A\), put

$$
D_H(\alpha)=\sum_{a=0}^{H-1}e(a\alpha),\qquad
F_H(\alpha)=|D_H(\alpha)|^2.
$$

Zero extension and Parseval give exactly

$$
\sum_n\left|\sum_{a=0}^{H-1}A(n+a)\right|^2
=\int_0^1F_H(\alpha)|\widehat A(\alpha)|^2\,d\alpha,
\tag{134.C1}
$$

where

$$
F_H(\alpha)=\sum_{|h|<H}(H-|h|)e(h\alpha),\quad
F_H(0)=H^2,\quad \widehat F_H(0)=H.
\tag{134.C2}
$$

Thus the exact multiplier is already nonnegative and band limited to
degree \(H-1\).

## 2. Universal quadratic-form domination is pointwise domination

Let \(T\) be a continuous real trigonometric polynomial. Then

$$
\int T|\widehat A|^2\geq\int F_H|\widehat A|^2
\quad\hbox{for every finitely supported }A
\tag{134.C3}
$$

if and only if \(T(\alpha)\geq F_H(\alpha)\) for every \(\alpha\).
The forward implication is tested with

$$
A_N(k)=N^{-1/2}e(-k\alpha_0)1_{0\leq k<N}.
$$

Then \(|\widehat A_N|^2=N^{-1}F_N(\alpha-\alpha_0)\) is an approximate
identity, so (134.C3) tends to
\(T(\alpha_0)-F_H(\alpha_0)\geq0\). The reverse implication is immediate.

Accordingly, a universal one-sided block-energy comparison cannot use a
weaker coefficientwise order. An actual-family-only comparison is
logically possible, but it is a new spectral theorem about the literal
\(\widehat A\), not a consequence of extremal-majorant algebra.

## 3. Bandwidth--mass uncertainty

Let

$$
T_\Delta(\alpha)=\sum_{|r|\leq\Delta}t_re(r\alpha)
$$

be real and satisfy \(T_\Delta\geq F_H\). Then \(T_\Delta\geq0\) and
\(T_\Delta(0)\geq H^2\). Fejer--Riesz factorization writes

$$
T_\Delta(\alpha)=\left|\sum_{j=0}^{\Delta}c_je(j\alpha)\right|^2.
$$

Therefore

$$
t_0=\int_0^1T_\Delta=\sum_{j=0}^{\Delta}|c_j|^2,
$$

and Cauchy at \(\alpha=0\) gives

$$
\boxed{(\Delta+1)t_0\geq H^2.}
\tag{134.C4}
$$

The weaker bound \((2\Delta+1)t_0\geq H^2\) follows without factorization
from \(|t_r|\leq t_0\). Also \(t_0\geq H\) by integrating
\(T_\Delta-F_H\geq0\). At \(\Delta=H-1\), the exact choice
\(T_{H-1}=F_H\) attains equality in both relevant bounds.

For the delta-sequence \(A(k)=z1_{k=k_0}\), (134.C1) has value
\(H|z|^2\), whereas the majorized quadratic form has value
\(t_0|z|^2\). Hence every universal degree-\(\Delta\) majorant has
coefficient-adversarial overhead

$$
\frac{t_0}{H}\geq\max\left\{1,\frac{H}{\Delta+1}\right\}.
\tag{134.C5}
$$

In particular, a fixed-power contraction
\(\Delta\leq HX^{-\eta}\) forces a fixed-power mass loss
\(t_0/H\gg X^\eta\). Reducing the number of Fourier modes by
\(H/(\Delta+1)\) cannot by itself save a power: the zeroth coefficient
pays at least the same factor.

If one chooses \(\Delta\asymp H/\Gamma\) to seek the missing
\(\Gamma=\min(H,Q)\), then (134.C5) leaves

$$
\Gamma_{\rm before}=\Gamma,\qquad
\Gamma_{\rm claimed}=1,\qquad
\Gamma_{\rm survivor}\geq\Gamma
\tag{134.C6}
$$

in every coefficient-blind bandwidth ledger. This is a method-capacity
obstruction, not a lower bound for the literal physical array.

## 4. Coefficientwise majorization does not order complex squares

The implication

$$
0\leq w_a\leq m_a
\quad\Longrightarrow\quad
\left|\sum_aw_ac_a\right|^2
\leq\left|\sum_am_ac_a\right|^2
\tag{134.C7}
$$

is false. For \(w=(1,1)\), \(m=(1,2)\), and \(c=(2,-1)\), the two
linear forms are \(1\) and \(0\). More generally, unless \(m\) is a
nonnegative scalar multiple of \(w\), choose \(c\) orthogonal to \(m\)
but not to \(w\). Thus a one-sided Beurling--Selberg majorant of a window
cannot be inserted inside the modulus in the block square.

Replacing (134.C7) by the triangle inequality is lawful, but it discards
the complex cross terms and introduces the corresponding window mass.
It is a separate positive norm and supplies no majorant-only contraction.

## 5. Character-placement control

The lawful multiplier comparison is applied after forming

$$
A(k)=\sum_{p\ {m odd}}\chi_4(p)b_{p,k}.
$$

Applying a positive majorant row by row is not equivalent. If two rows
\(r\equiv1\pmod4\) and \(s\equiv3\pmod4\) are identical, then the true
combined \(A\) and its block energy vanish, whereas the separate positive
row energy is twice the one-row energy. This is an exact algebraic control,
not a physical counterexample.

At the combined level, taking \(T=F_H\) preserves the character but is
exactly (134.C1). Taking smaller degree forces (134.C4); bounding the new
form still requires an actual-character spectral estimate not furnished
by the majorant.

## 6. Candidate conclusion

The pure one-sided-majorant mechanism has only three lawful outcomes:

1. degree at least \(H-1\) and the exact Fejer multiplier, hence no new
   contraction;
2. degree below \(H\), with the bandwidth saving paid by the zeroth
   coefficient as in (134.C4)--(134.C6); or
3. an actual-family-only spectral inequality that uses the literal
   \(\chi_4\)-weighted square-root phases beyond majorant algebra.

The first two give a scoped majorant no-go. The third is a genuinely new
analytic theorem and remains open here. No conclusion is drawn for the
literal endpoint estimate until the independent reports and owner seams
are adjudicated.
