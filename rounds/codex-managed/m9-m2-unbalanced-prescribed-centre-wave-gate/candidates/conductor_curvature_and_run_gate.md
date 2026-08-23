# Conductor candidate: literal curvature bound and fixed-step run gate

Campaign: `m9-m2-unbalanced-prescribed-centre-wave-gate`

Status: candidate pending the Round-118 seam review.  This note proves no
pointwise quarter estimate.

## 1. A literal reciprocal-row estimate

Put

\[
 R={X\over D},\qquad K={XL\over D^2},\qquad
 a=\delta-\ell.
\]

In the reciprocal row, resolve

\[
 \chi _4(r)={e(r/4)-e(-r/4)\over 2i}
 \qquad (r\ {m odd}).
\]

For fixed \(k\asymp K\), either shifted phase

\[
 f_{k,\pm}(r)={Xk\over r}\pm {r\over4}
\]

has

\[
 |f_{k,\pm}''(r)|={2Xk\over r^3}\asymp {LD\over X}
 \qquad (r\asymp R).
\]

The sampled \(r\)-amplitude

\[
 W\!\left({X\over rD}\right)q_L\!\left({4Xk\over r^2}\right)
\]

has uniform normalized bounded variation on each fixed flat smooth collar.
Weighted second-derivative summation therefore gives

\[
 \sum_{r\asymp R\atop r\ {m odd}}
 \chi _4(r)W\!\left({X\over rD}\right)
 q_L\!\left({4Xk\over r^2}\right)e(Xk/r)
 \ll_\varepsilon
 \left(\sqrt{XL/D}+\sqrt{X/(LD)}\right)X^\varepsilon.
\]

Since \(\sum_{k\asymp K}k^{-1}\ll1\), taking the \(k\)-sum absolutely
costs no further power.  Thus, on the certified flat smooth scope,

\[
 \mathscr R_{D,L}(X)
 \ll_\varepsilon
 \left(\sqrt{XL/D}+\sqrt{X/(LD)}\right)X^\varepsilon
 \ll X^{(1-a)/2+\varepsilon}.
\tag{118.C1}
\]

Combining (118.C1) with the divisor bound \(X^{a+\varepsilon}\) gives

\[
 \mathscr R_{D,L}(X)
 \ll_\varepsilon X^{\beta(a)+\varepsilon},
 \qquad
 \beta(a)=\min\left(a,{1-a\over2}\right).
\tag{118.C2}
\]

This is a strict saving over absolute capacity exactly when \(a>1/3\),
of size \(X^{(3a-1)/2}\).  It is not target-safe anywhere in the strict
residual interval \(1/4<a<1/2\), because \(\beta(a)>1/4\).  Equality with
the target occurs only at the already owned boundary \(a=1/2\).  The
estimate is the reciprocal orientation of the previously accepted full
second-derivative menu, not a new closure of UNBAL.

## 2. Fixed-step coherent runs cannot falsify the target

Suppose consecutive integers \(d=d_0+u\), \(0\le u\le U\), are paired with

\[
 r_u=r_0-4mu,
\]

so that every \(r_u\) has the same \(\chi _4\)-sign.  Assume
\(d\asymp D\), \(r_u\asymp X/D\), the unbalanced separation
\(X/D^2\gg1\), and

\[
 |d r_u-X|\le C{D\over L}
\tag{118.C3}
\]

throughout the run.  Comparing two consecutive reciprocal centres gives

\[
 |4m|\asymp {X\over D^2}.
\]

The product \((d_0+u)(r_0-4mu)\) is quadratic with leading coefficient
\(-4m\).  Its oscillation on \(0\le u\le U\), even after the best possible
choice of the linear term, is \(\gg |m|U^2\).  Condition (118.C3) hence
forces

\[
 U\ll 1+\sqrt{{D/L\over X/D^2}}
   =1+\sqrt{{D^3\over XL}}.
\tag{118.C4}
\]

In exponent notation the power in (118.C4) is

\[
 {3\delta-1-\ell\over2}<{1\over4}
\]

because \(\delta<1/2\) and \(\ell\ge0\).  Thus even a completely aligned
fixed-step run satisfying the literal product window is individually
target-safe.  It is not a counterexample to (118.B8).

This conclusion is deliberately scoped.  Same-sign selectors whose
multiple-of-four increments change, separated coherent packets, and the
complete signed complement are not bounded by (118.C4).  Proving that a
large wave forces one fixed-step run would require a new inverse theorem.

## 3. Surviving interface

The product strip contains about \(D/L\) arithmetically sparse hits.  The
local fixed-step control rules out the proposed single-run falsifier, while
the curvature estimate saves only for \(a>1/3\) and still misses the target
by

\[
 X^{(1-2a)/4}.
\]

The smallest live problem is therefore cancellation between the separated
same-sign selector packets, with the literal complex wavelet and both
character classes retained.  A second scalar transform returns to the
physical packet, and an unsigned norm discards exactly this remaining
inter-packet cancellation.
