# Conductor candidate: terminal-height completion of the GAR interface

Campaign: `m9-m1-gar-radial-interface-reconciliation`

Status: candidate pending statement-only and hostile review.

Put (R=X^{1/4}), (Y=\sqrt X), (s=n/Y), and retain the exact active
profiles (D_j=2^{-j}\lfloor\sqrt X\rfloor) and
(H_j=\lfloor D_j/R\rfloor). Choose a fixed small (s_0>0) with
(2s_0<16), and choose
(\vartheta\in C^\infty([0,\infty))) such that

\[
 \vartheta(u)=0\quad(u\leq\kappa/2),\qquad
 \vartheta(u)=1\quad(u\geq\kappa),\qquad
 \kappa={\sqrt{s_0}\over4}.
\]

Define the terminal-height angular coefficient by inserting
(\vartheta(h/H_j)) into every active (j,h) summand of
(\Omega_X^*(n,h)); call the resulting divisor coefficient
(\mathcal C_{T,X}^*(n)).  A scale with (H_j=0) is empty and is omitted
before this quotient is formed.

## Terminal-height radial bound

Before transformation, the corresponding positive reciprocal antecedent
is

\[
 \mathcal B_T^+=
 \sum_j\sum_{h\leq H_j}
 {\vartheta(h/H_j)\Phi(h/(H_j+1))\over h}
 \sum_d\chi_4(d)w_j(d)e(hX/d).
\tag{120.C1}
\]

The (h)-support in (120.C1) is a fixed-ratio terminal range. Decompose it
into (O_{s_0}(1)) fixed-BV dyadic shells. On every shell (L\asymp H_j),
the accepted frequency-first theorem gives

\[
 \mathcal B_{T,j}^+
 \ll_\varepsilon X^\varepsilon(1+D_j/H_j)
 \ll_\varepsilon X^{1/4+\varepsilon}.
\]

The logarithmic (j)-sum is absorbed in (X^\varepsilon). Applying the
accepted positive-frequency smooth and hard transforms with the same
height cutoff gives

\[
 \mathcal B_T^+
 ={e(1/8)\over i}R
 \sum_{n\leq N_X}^{*}
 \mathcal C_{T,X}^*(n)n^{-3/4}e(\sqrt{Xn})
 +O_\varepsilon(X^\varepsilon),
\tag{120.C2}
\]

where the hard cotangent boundary and aggregate transform errors are
polylogarithmic. Hence

\[
 \boxed{
 \sum_{n\leq N_X}^{*}
 \mathcal C_{T,X}^*(n)n^{-3/4}e(\sqrt{Xn})
 \ll_\varepsilon X^\varepsilon.}
\tag{120.C3}
\]

The same argument remains valid after multiplying the radial side by one
fixed smooth cutoff, using the accepted Mellin separation; the added
terminal-height factor preserves the (O((1+|t|)/H_j)) frequency BV norm.

## Exact support geometry

For a nonzero stationary profile atom put

\[
 t={2h\sqrt{X/n}\over D_j}={2hR\over D_j\sqrt s}.
\]

The certified profiles have \(1/2\leq t\leq C_W\) with the exact
uniform choice \(C_W=3/2\).  (A nonzero smooth-profile value has
\(t<3/2\), but no smaller uniform closed support constant is available.)
Therefore

\[
 {hR\over D_j}={t\sqrt s\over2}.
\tag{120.C4}
\]

Since (H_j\leq D_j/R), every atom with (s\geq s_0) satisfies

\[
 {h\over H_j}\geq{hR\over D_j}\geq{\sqrt{s_0}\over4}=\kappa.
\]

Consequently

\[
 \boxed{
 \mathcal C_{T,X}^*(n)=\mathcal C_X^*(n)
 \quad\text{whenever }n/Y\geq s_0.}
\tag{120.C5}
\]

Conversely, the accepted active-height lower bound
(H_j\geq D_j/(2R)), together with the support of (\vartheta), implies

\[
 {hR\over D_j}\geq{\kappa\over4}
\]

on every terminal-height atom. Equation (120.C4) then gives

\[
 n/Y\geq c_T:={\kappa^2\over4C_W^2}>0.
\tag{120.C6}
\]

Also (h\leq H_j\leq D_j/R) and (t\geq1/2) give (n/Y\leq16).
Thus the terminal-height coefficient is supported in one fixed compact
radial interval ([c_T,16]), with the literal endpoint star retained.

## Interface closure

Choose one fixed lower cutoff (V_{\rm low}\) with

\[
 V_{\rm low}(s)=1\quad(s\leq s_0),\qquad
 V_{\rm low}(s)=0\quad(s\geq2s_0).
\]

By (120.C5), coefficientwise on every integer (n),

\[
 (1-V_{\rm low}(n/Y))\mathcal C_X^*(n)
 =(1-V_{\rm low}(n/Y))\mathcal C_{T,X}^*(n).
\tag{120.C7}
\]

The right side is the full terminal-height sum (120.C3) minus its
\(V_{\rm low}\)-weighted part.  This second use of smooth transfer needs
one explicit support repair.  On the joint support of
\(\vartheta(h/H_j)w_j(d)\), the same floor inequalities give

\[
 {4R^2h^2\over d^2}\geq {\kappa^2\over9},
\]

because \(d\leq3D_j/2\).  Choose a fixed
\(\psi\in C_c^\infty((0,16))\) which is one on
\([\kappa^2/9,2s_0]\).  Then the reciprocal antecedent of the weighted
part is unchanged if \(V_{\rm low}(z)\) is replaced by the admissible
compact multiplier \(\psi(z)V_{\rm low}(z)\).  Mellin separation of that
multiplier, with the additional sampled factor \(\vartheta(h/H_j)\), has
frequency BV \(O((1+|t|)/H_j)\).  Thus the terminal-height version of the
accepted fixed-cutoff transfer bounds the weighted part by
\(O_\varepsilon(X^\varepsilon)\).
Therefore

\[
 \boxed{
 \sum_{n\leq N_X}^{*}
 (1-V_{\rm low}(n/Y))\mathcal C_X^*(n)n^{-3/4}
 e(\sqrt{Xn})
 \ll_\varepsilon X^\varepsilon.}
\tag{120.C8}
\]

Equation (120.C8) is exactly the whole nonlower radial complement.  For a
Round-98 lower--compact-critical--interface partition, subtracting the
already proved fixed compact critical sums from (120.C8) proves the old
sharp interface owner.  Equivalently one may use the exact two-piece
partition (V_{\rm low}+(1-V_{\rm low})=1).  It includes the complete
radial collar through (N_X); no limit (C\uparrow16), shrinking-cutoff
seminorm, or identification with an integration-by-parts prefix is used.
The physical endpoint prefix and aggregate endpoint/(R_1) modules belong
to an alternative transformed architecture.  They are not Poisson
transform errors and are inserted zero times on this route, so no boundary
owner is duplicated.

If every transform and one-count seam in (120.C1)--(120.C8) passes review,
this closes `M9-M1-global-radial-interface-estimate`. GAR would then have
one analytic parent left: the exact lower-radial signed aggregate. It would
not prove blockwise M9-M1 or change any exponent by itself.
