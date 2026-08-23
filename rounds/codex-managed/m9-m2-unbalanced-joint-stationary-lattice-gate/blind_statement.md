# Blind statement: complete shifted stationary-lattice problem

This is a statement-only packet. Do not read the proof graph, strategy
files, prior nonblind rounds, or sibling reports.

Let \(X\geq2\) be real, let \(M\in\mathbb Z\) satisfy \(M\asymp X\),
and put

$$
 D=X^\delta,qquad L=X^\ell,qquad R=X/D,qquad K=XL/D^2,
$$

with

$$
 \frac14\leq\delta<\frac12,qquad
 0\leq\ell<\delta-\frac14,qquad
 178\ell+1638\delta>463.
$$

Fix smooth compact profiles \(W\) and \(q_L\), extended by zero, and
write

$$
 W_r=W(X/(rD)),qquad q_{r,k}=q_L(4Xk/r^2).
$$

All amplitudes and the denominator \(4X\) remain frozen at the original
real \(X\). For odd \(r\), define

$$
 c_k=sum_{r\ \mathrm{odd}}
 \chi_4(r)W_r\frac{q_{r,k}}{k}e(Mk/r).
$$

Choose one fixed zero-extension interval \(I\) of length \(J\asymp K\)
containing every sampled support. Put

$$
 H_0=\left\lceil X^{1/2}/D\right\rceil
$$

and consider the exact block square

$$
 \mathcal F_{M,H_0}
 =\frac{J+H_0-1}{H_0^2}
 \sum_n\left|\sum_{a=0}^{H_0-1}c_{n+a}\right|^2.
\tag{B.1}
$$

Its correlation expansion contains, for every \(|h|<H_0\),

$$
 \sum_k\sum_{r,s\ \mathrm{odd}}
 \chi_4(r)\chi_4(s)W_r\overline{W_s}
 \frac{q_{r,k+h}\overline{q_{s,k}}}{(k+h)k}
 e\!\left(Mk(1/r-1/s)+Mh/r\right),
\tag{B.2}
$$

with the exact Fejer multiplicity \(H_0-|h|\), the prefactor in (B.1),
and all support entries and exits retained.

For the unique nearest integer \(j\) to \(M(1/r-1/s)\), define

$$
 E=M(s-r)-jrs.
$$

You may take as hypotheses only the following already established
decomposition facts:

- the complete \(j=0\) part of (B.1) is
  \(O_\varepsilon(X^{1/2+\varepsilon})\);
- all nonzero exact aliases \(E=0\) together are
  \(O_\varepsilon(X^\varepsilon)\);
- the smooth tail \(|E|>X^{1+\rho}/L\) is rapidly small for fixed
  \(\rho>0\).

The open object is therefore the complete real ordered-pair aggregate

$$
 \mathfrak V_{M,H_0}=
 \sum_{\substack{r,s\ \mathrm{odd}\\
 j(r,s)\ne0,\ E(r,s)\ne0\\
 |E(r,s)|\leq X^{1+\rho}/L}}
 \chi_4(r)\chi_4(s)\Gamma_{M,H_0}(r,s),
\tag{B.3}
$$

where \(\Gamma\) means the exact kernel in (B.1)--(B.2), not an
unshifted or rectangular substitute. The target is

$$
 \boxed{\mathfrak V_{M,H_0}
 \ll_\varepsilon X^{1/2+\varepsilon}.}
\tag{B.4}
$$

Independently test a two-character Poisson/stationary treatment of the
\(r,s\) sums. Derive every dual sign, mode range, saddle, Gaussian unit,
principal amplitude, profile image, nonstationary term, endpoint saddle,
and aggregate error. Determine the exact stationary lattice, including:

1. the positive odd dual-mode coordinates and their character factors;
2. the complete dual phase and its derivatives;
3. the exact product defect governing equality of the two dual products;
4. the relationship between a dual \(k\)-frequency and the original
   reciprocal alias \(j\);
5. the dual diagonal, equal-mode shifted, unequal-mode, negative-shift,
   and all quarter-sign branches;
6. the distinction between a transform identity, a sufficient norm, and
   an inequality that actually proves (B.4).

Seek (B.4), a strict target-safe complete sector, a quantitative signed
saving, or a stronger inverse theorem. If none follows, prove the
smallest exact self-return or overstrong-norm obstruction. Do not infer a
signed lower bound from capacity, and do not replace the literal
characters by absolute, random, or adversarial coefficients.

Your report must contain the seven required sections: result; exact
statement and hypotheses; proof or derivation; first doubtful or unproved
step; control tests and outcomes; dependencies and exact artifacts used;
recommended state effect.
