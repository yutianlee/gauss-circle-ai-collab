# Round 120 blind statement: GAR radial-interface reconciliation

This statement is self-contained. Treat every displayed coefficient and
scope restriction literally. A proved endpoint boundary module is not
automatically a bound for a sharp radial collar.

Let

\[
 Y=\sqrt X,\qquad y=\lfloor\sqrt X\rfloor,
 \qquad N_X=\lfloor16Y\rfloor,
\]

and let the exact global angular coefficient be

\[
 \mathcal C_X^*(n)=
 \sum_{\substack{hq=n\\q\ {
m odd}}}
 \chi_4(q)\Omega_X^*(n,h),
\tag{120.B1}
\]

where

\[
 \Omega_X^*(n,h)=
 \sum_j\mathbf1_{h\leq H_j}
 \Phi(h/(H_j+1))
 \left[w_j\!\left(2h\sqrt{X/n}\right)\right]^*,
 \quad
 H_j=\lfloor D_jX^{-1/4}\rfloor,
 \quad D_j=2^{-j}y.
\tag{120.B2}
\]

The normalized global radial sum is

\[
 \mathcal G_X=
 \sum_{n\leq N_X}^{*}
 \mathcal C_X^*(n)n^{-3/4}e(\sqrt{Xn}).
\tag{120.B3}
\]

After multiplication by the accepted external factor (X^{1/4}), an
(O_\varepsilon(X^\varepsilon)) bound for (120.B3) is the total active
M1 quarter target.

The following statements are already accepted.

1. **Fixed smooth critical transfer.** For every fixed
   (V\in C_c^\infty((c,C))), with (0<c<C<16),

   \[
   \sum_{n\leq N_X}V(n/Y)\mathcal C_X^*(n)n^{-3/4}
   e(\sqrt{Xn})\ll_{\varepsilon,V}X^\varepsilon.
   \tag{120.B4}
   \]

   This excludes the sharp endpoint (n=N_X), sharp moving cutoffs, and
   (n/Y\to0).

2. **Physical upper endpoint prefix.** In the accepted symmetric physical
   profile limit,

   \[
   \sum_{hq\leq N_X}^{*}
   \chi_4(q)(hq)^{-3/4}
   H^{\rm prof}_{\infty,X}(h,q)\ll_W1,
   \tag{120.B5}
   \]

   with all scales, height floors, the hard-top star, and the product half
   tie retained. This is the upper endpoint prefix produced by the radial
   endpoint module. It is not a uniform finite-top-Mellin-truncation
   theorem.

3. **Endpoint boundary package.** The lower endpoint prefix, (120.B5),
   and the recombined (R_1) arithmetic residue are target-safe after
   their common physical limit and artificial-pole cancellation. This
   package excludes the two diagonal transition traces and does not by
   itself identify a sharp radial collar in (120.B3).

4. **Global radial one-count.** Choose one fixed smooth partition of
   (120.B3) into a lower cutoff, finitely many compact critical functions,
   and a sharp upper/interface remainder. The compact functions are owned
   by (120.B4). The lower piece is a separate open parent. If the lower
   parent and the sharp upper/interface remainder are both
   (O_\varepsilon(X^\varepsilon)), then GAR follows.

The open radial-interface parent asks for the normalized
(O_\varepsilon(X^\varepsilon)) bound on the sharp upper endpoint and
every finite-support, cutoff, and top-interface piece excluded by
(120.B4) and by the chosen lower cutoff, with the endpoint star, hard
sample, floors, signs, and transform boundary terms retained once.

Required outcome: construct one exact physical partition and determine
coefficientwise which part of this open parent is already owned by
(120.B5) and the endpoint boundary package. Either prove the complete
radial-interface parent, prove a strict target-safe subpackage, or isolate
the smallest exact remainder. Distinguish the original radial collar from
an integration-by-parts boundary prefix, and distinguish the accepted
physical limit from an arbitrary finite Mellin truncation. Do not insert
the connector-completed alpha architecture as an additional summand.
