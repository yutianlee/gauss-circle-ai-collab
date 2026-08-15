# Conductor axial subtraction calculation

Campaign: `m9-m1-beta-complete-physical-height-symbol`  
Role: conductor axial-seam analysis  
Allocation: 100% analytical/algebraic

## 1. Polar decomposition

On the line \(v=b+i\nu\), the accepted height Mellin transform has

\[
 f_b(\nu)=\frac1{b+i\nu}+r_b(\nu).                 \tag{32.A1}
\]

The pole term is not an error: its contour residue at \(v=0\) belongs to
the separate axial ledger. Define the axial-subtracted remainder by

\[
 f_b^\circ(\nu)=f_b(\nu)-\frac1{b+i\nu}.            \tag{32.A2}
\]

For a compact physical profile, Mellin integration by parts gives rapid
decay for \(f_b^\circ\) and its fixed number of derivatives, uniformly for
small positive \(b\), after the residue is removed. The exact uniform
constants for the actual one-sided top convention still require readback
from the profile definition.

## 2. Why fixed-nu differentiation is essential

The polar weight has

\[
 \left\|\frac1{b+i\nu}\right\|_{L^1(|\nu|\le1)}
 \asymp\log(1/b),
\]

but

\[
 \left\|\partial_\nu\frac1{b+i\nu}\right\|_{L^1(|\nu|\le1)}
 \asymp b^{-1}.                                     \tag{32.A3}
\]

Thus the Round-31 physical-height interface—ordinary \(L\) derivative at
fixed \(\nu\)—is compatible with polylogarithmic loss, whereas a mixed
derivative that absolutizes \(\partial_\nu f_b\) is not. Equation (32.A3)
is another reason to perform axial extraction before any complete-symbol
BV claim.

## 3. Conditional terminal symbol

Let \(K_{\rm term}^\circ\) be the side-collapsed, endpoint-free,
omega-recombined terminal kernel with \(f_b\) replaced by
\(f_b^\circ\), after one combined top diagonal/log subtraction. The exact
next bound is

\[
 |K_{\rm term}^\circ(L,\nu)|
 \ll X^\varepsilon\lambda^{-2}w^\circ(\nu),
 \qquad
 |\partial_LK_{\rm term}^\circ(L,\nu)|
 \ll X^\varepsilon\lambda^{-3}w^\circ(\nu),         \tag{32.A4}
\]

with \(\|w^\circ\|_1\ll(\log X)^C\). If (32.A4) holds, the Round-31
lemma yields the regular terminal BV estimate. The polar term itself must
be returned by the exact \(v=0\) residue identity, not estimated inside
(32.A4).

## 4. Remaining ownership question

The current packet states that the axial residue is separately retained,
but it does not yet give a mask-compatible identity proving that subtracting
\((b+i\nu)^{-1}\) from each omega and connector share yields exactly one
global \(v=0\) residue with no corner duplication. This finite-contour
identity is a prerequisite to promoting (32.A2) as the actual reduced
kernel definition.

Accordingly, the likely smallest Round-32 survivor is an axial-compatible
side-collapsed terminal identity, followed by (32.A4). Neither is proved by
the norm calculation alone.
