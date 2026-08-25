# Blind statement: one-sided band-limited majorant gate for the full-character block energy

Round: 134

This file is statement-only input. Do not consult any proof graph, strategy
memo, prior nonblind round, sibling report, or conductor derivation.

Let \(e(x)=e^{2\pi i x}\), let \(M\asymp X\) be an integer, and put

$$
D=X^\delta,\qquad L=X^\ell,\qquad K=XL/D^2,\qquad
H=\left\lceil X^{1/2}/D\right\rceil,
$$

where

$$
\frac14\leq\delta<\frac12,\qquad
0\leq\ell<\delta-\frac14,\qquad
178\ell+1638\delta>463.
$$

Thus \(K\asymp LH^2\), and

$$
Q:=\frac{D^2}{L\sqrt X}\longrightarrow\infty.
$$

All profiles below are the literal fixed smooth profiles from one
flat-smooth strict-UNBAL packet. They are uniformly smooth after scaling,
compactly supported on positive fixed interiors, and extended by zero
before every shift. For positive odd \(p\), define

$$
\mathcal A_{p,k}
=W\!\left(\frac{X}{2D}\sqrt{\frac p{Mk}}\right)q_L((X/M)p),
$$

$$
b_{p,k}=e(-1/8)M^{1/4}k^{-3/4}p^{-3/4}
\mathcal A_{p,k}e(\sqrt{Mpk}).
\tag{134.B1}
$$

Put

$$
A(k)=\sum_{p>0\atop p\ {m odd}}\chi_4(p)b_{p,k},\qquad
B_{p,n}=\sum_{a=0}^{H-1}b_{p,n+a},
$$

$$
C_H=\frac{J+H-1}{H^2},\qquad J\asymp K,
$$

and

$$
\mathcal E_\chi
=C_H\sum_n\left|\sum_{p>0\atop p\ {m odd}}
\chi_4(p)B_{p,n}\right|^2
=C_H\sum_n\left|\sum_{a=0}^{H-1}A(n+a)\right|^2.
\tag{134.B2}
$$

It is accepted that the physical flat-smooth strict-UNBAL survivor is,
modulo already target-safe terms, equivalent to the upper estimate

$$
\boxed{\mathcal E_\chi\ll_\varepsilon X^{1/2+\varepsilon}.}
\tag{134.B3}
$$

It is also accepted that

$$
\mathcal D_0=C_HH\sum_{p,k}|b_{p,k}|^2\ll X^{1/2},
\tag{134.B4}
$$

whereas the best available complete separate positive-row estimate has
capacity

$$
\mathcal E_{\rm eq}
=C_H\sum_{p,n}|B_{p,n}|^2
\ll_\varepsilon X^{1/2+\varepsilon}\min\{H,Q\}.
\tag{134.B5}
$$

For a finitely supported sequence \(A\), set

$$
\widehat A(\alpha)=\sum_k A(k)e(k\alpha),\qquad
D_H(\alpha)=\sum_{a=0}^{H-1}e(a\alpha),\qquad
F_H(\alpha)=|D_H(\alpha)|^2.
$$

Exact Parseval gives

$$
\mathcal E_\chi
=C_H\int_0^1F_H(\alpha)|\widehat A(\alpha)|^2\,d\alpha.
\tag{134.B6}
$$

Here

$$
F_H(\alpha)=\sum_{|h|<H}(H-|h|)e(h\alpha),\qquad
F_H(0)=H^2,\qquad \int_0^1F_H=H.
\tag{134.B7}
$$

Thus the exact block multiplier is already a nonnegative trigonometric
polynomial of degree \(H-1\).

The proposed noninvertible move is a lawful one-sided band-limited
majorant. One possible formulation is a real trigonometric polynomial

$$
T_\Delta(\alpha)=\sum_{|r|\leq\Delta}t_re(r\alpha),
\qquad T_\Delta(\alpha)\geq F_H(\alpha)\quad(\alpha\in\mathbb R/\mathbb Z),
\tag{134.B8}
$$

which implies the positive-semidefinite comparison

$$
\mathcal E_\chi\leq
C_H\int_0^1T_\Delta(\alpha)|\widehat A(\alpha)|^2\,d\alpha.
\tag{134.B9}
$$

Other Beurling--Selberg or Vaaler placements are allowed only after their
exact order relation is proved. In particular, distinguish:

1. pointwise domination of a scalar cutoff;
2. coefficientwise domination of a window;
3. pointwise domination of a Fourier multiplier;
4. positive-semidefinite domination of the resulting quadratic form; and
5. an inequality proved only for the literal actual-symbol family (134.B1).

Independently prove one of the following:

1. the target (134.B3) by a complete one-sided majorant argument;
2. a strict fixed-power reduction to a smaller endpoint-complete
   actual-character survivor;
3. a quantitative theorem giving the smallest possible zeroth coefficient
   and bandwidth of (134.B8), together with its exact capacity consequence;
   or
4. the smallest rigorous no-go identifying the first invalid order,
   cross-term, bandwidth, character, endpoint, or Poisson inference.

For any claimed bandwidth gain, state
\(\Gamma_{\rm before}=\min(H,Q)\),
\(\Gamma_{\rm claimed}=1\), and the exact surviving factor. Test a one-row
coherent sequence, two identical rows in opposite \(\chi_4\)-classes, true
\(\chi_4\), \(|\chi_4|\), random signs, and phase-adapted complex
coefficients. A coefficient adversary can falsify a universal majorant
inference but is not a counterexample to the literal array (134.B1).

Do not take a modulus before the actual \(\chi_4\)-weighted \(p\)-sum. Do
not infer domination of a complex block square from coefficientwise
majorization alone. Do not count (134.B7) rewritten as itself, or an
invertible Poisson/stationary transform, as a saving. Preserve the moving
profiles, zero extension, entries, exits, and all signs. Scope every result
to the flat-smooth strict-UNBAL owner; no hard, sharp, clipped, starred,
arithmetic-owner, nonflat, transition, downstream M9, or exponent claim is
licensed here.
