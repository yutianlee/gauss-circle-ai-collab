# Round 121 statement-only packet: global lower-radial height kernel

This is the complete packet for the statement-only task.

Let

\[
 R=X^{1/4},\qquad Y=\sqrt X,\qquad y=\lfloor Y\rfloor,
 \qquad D_j=2^{-j}y,\qquad H_j=\lfloor D_j/R\rfloor.
\]

The exact active denominator profiles are denoted by \(w_j\). They
include the unique one-sided hard top profile and all nonempty smooth
profiles; the inactive bottom denominator range has already been bounded
before Fourier expansion. Put

\[
 a_j(h)={\bf1}_{h\leq H_j}
 \Phi\!\left({h\over H_j+1}\right),\qquad
 A_X(h,d)=\sum_j a_j(h)w_j(d).
\tag{121.B1}
\]

Fix the same real smooth lower cutoff as in the accepted radial
one-count partition: \(V_{\rm low}(s)=1\) near \(s=0\) and
\(V_{\rm low}(s)=0\) for \(s\geq2s_0\), where \(0<s_0<8\) is fixed.
The exact positive reciprocal antecedent of the remaining lower-radial
owner is

\[
 \mathcal B_{\rm low}^+
 =\sum_j\sum_{h\leq H_j}{\Phi(h/(H_j+1))\over h}
 \sum_{d\geq1}\chi_4(d)w_j(d)
 V_{\rm low}\!\left({4R^2h^2\over d^2}\right)e(hX/d).
\tag{121.B2}
\]

Equivalently, without applying an outside norm,

\[
 \mathcal B_{\rm low}^+
 =\sum_{h,d\geq1}{\chi_4(d)\over h}A_X(h,d)
 V_{\rm low}\!\left({4R^2h^2\over d^2}\right)e(hX/d).
\tag{121.B3}
\]

The accepted coefficient-preserving smooth and hard transforms reduce the
lower-radial theorem to

\[
 \boxed{\mathcal B_{\rm low}^+\ll_{\varepsilon,s_0}RX^\varepsilon.}
\tag{121.B4}
\]

The negative frequency is the conjugate after the exact real coefficient
is retained. The hard cotangent boundary, transform errors, inactive
bottom range, stationary stars, outer product half tie, and exact floors
must remain separately accounted for.

Because \(\chi_4(4m+1)=1\) and \(\chi_4(4m+3)=-1\), zero-extending the
full height sum gives the exact possible starting identity

\[
 \mathcal B_{\rm low}^+
 =\sum_{m\geq0}\{F_X(4m+1)-F_X(4m+3)\},
\tag{121.B5}
\]

where

\[
 F_X(d)=\sum_{h\geq1}{A_X(h,d)\over h}
 V_{\rm low}\!\left({4R^2h^2\over d^2}\right)e(hX/d).
\tag{121.B6}
\]

The task is to determine whether the exact profile-first kernel (121.B3)
or the denominator-paired kernel (121.B5) yields (121.B4) when the height
sum remains inside the pair, or to isolate the smallest exact survivor.
In particular:

1. rederive (121.B2)--(121.B6), including every support boundary;
2. separate amplitude variation from the phase increment
   \(2hX/(d(d+2))\) without taking a termwise absolute value in \(h\);
3. prove a target-safe amplitude seam if it is true;
4. test any resonant/nonresonant or height-first inequality at the full
   \(RX^\varepsilon\) budget;
5. explain exactly why the argument fails for the unsigned or
   adversarial-character analogue;
6. identify whether the surviving kernel is genuinely smaller than the
   earlier one-sided divisor, product-wavelet, or unmatched-crossing
   returns.

An exact estimate, strict target-safe subpackage, or rigorous no-go with
the smallest survivor is a successful outcome. Do not claim the global
angular-radial estimate, blockwise M9-M1, M9, or a new exponent unless all
of their independent parents are proved.

