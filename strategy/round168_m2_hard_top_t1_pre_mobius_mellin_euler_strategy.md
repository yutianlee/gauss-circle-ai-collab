# Round 168 strategy: pre-Möbius Mellin--Euler product gate

## Conductor decision

Round 167 is closed on graph
b1af2cf47d81dd96aba8941e590f8b8ec2733476af6dda78a822041f46511c31.
The next frozen object is the complete selector-free \(t=1\) scalar, not
the Round-167 residual selector and not the maximal Fejer alternative.

Write its literal form as

\[
 \mathcal S_{L,1}
 =\sum_{\substack{d_1,d_2\geq1\\
                  d_1\ {\rm odd}\\
                  d_1d_2\ {\rm squarefree}}}
 \chi_4(d_1)\,
 \mathcal A_{L,X}(d_1,d_2)\,
 e\!\left(J\sqrt{d_1d_2}\right),
 \qquad J=\sqrt X ,
\tag{168.F1}
\]

where \(\mathcal A_{L,X}\) is the complete literal bounded amplitude from
the accepted \(t=1\) reduction: product shell, normalization, dyadic
profiles, cone, \(H+1\) profile, real centre, floors, stars, hard values,
endpoints, and zero extension.  Its support has \(d_1,d_2\asymp L\).
The target is

\[
 \boxed{\mathcal S_{L,1}\ll_\varepsilon L^{3/2}X^\varepsilon}
\tag{168.F2}
\]

uniformly for \(1\ll L\ll H\leq J^{1/2}\).

The accepted close opposite-prime XOR sector is already
\(O_\kappa(L^{3/2})\), and the literal full scalar is exactly that sector
plus the residual.  Thus (168.F2) would close the residual only after this
exact subtraction.  It would not close any other hard-TOP channel.

## Why this frontier is selected

The full scalar has only the missing half-power \(L^{1/2-o(1)}\) and removes
the allocation-dependent residual selector that blocked the determinant
source interface.  The maximal-scale alternative has positive capacity
\(L^4X^\varepsilon\) against an \(L^3X^\varepsilon\) target, introduces a
longer shift and phase interface, and its short-range connector already
uses the complete target allowance.  This ranking is a research decision,
not a proof.

Round 162 opened squarefreeness and coprimality term by term with Möbius
variables before Poisson.  That route produced the rank-one product collar,
positive capacity \(\sqrt{JL}\), exact character-transform self-return, a
moving incomplete divisor window, and hard-edge transitions.  Round 168
does not repeat that opening.  It retains the full signed arithmetic family
inside one two-variable Dirichlet series until after Mellin inversion and
any functional equation.

## Exact new algebraic interface

Initially for \(\Re s_1,\Re s_2>1\), set

\[
 D(s_1,s_2)=
 \sum_{\substack{d_1,d_2\geq1\\d_1\ {\rm odd}\\
                  d_1,d_2\ {\rm squarefree}\\(d_1,d_2)=1}}
 {\chi_4(d_1)\over d_1^{s_1}d_2^{s_2}} .
\tag{168.F3}
\]

The Euler factors must be derived, including \(p=2\), and checked against
the literal parity convention.  The candidate factorization to verify is

\[
 D(s_1,s_2)=L(s_1,\chi_4)\zeta(s_2)G(s_1,s_2),
\tag{168.F4}
\]

\[
 G_2=1-2^{-2s_2},\qquad
 G_p=(1+x_p+y_p)(1-x_p)(1-y_p)
\quad(p\ {\rm odd}),
\tag{168.F5}
\]

where \(x_p=\chi_4(p)p^{-s_1}\) and \(y_p=p^{-s_2}\).
In particular the first nonconstant terms of \(G_p\) are quadratic, so
absolute convergence is expected for
\(\min(\Re s_1,\Re s_2)>1/2\).  This statement itself is only algebra.

For a lawful exact interpolation or Mellin--Stieltjes realization of the
literal amplitude, derive

\[
 \mathcal S_{L,1}
 ={1\over(2\pi i)^2}
 \iint \widehat{\mathcal B}_{L,X}(s_1,s_2)
 D(s_1,s_2)\,ds_1\,ds_2
\tag{168.F6}
\]

on initial lines of absolute convergence.  Every hard and half-open
endpoint must be owned; an arbitrary smoothing that merely approximates
integer samples is not (168.F6).

## Ordered analytic gates

1. Prove the exact Euler product, its continuation region, and every pole
   or zero used in a contour move.
2. Construct an exact literal Mellin, Perron, or Stieltjes representation
   with the correct half-open and hard-value convention.
3. In radial/angular variables \(d_1=rw,d_2=r/w\), track the concentration
   \(t_1+t_2\asymp JL\) caused by \(e(Jr)\) and the angular
   \(t_1-t_2\) transform caused by the cone and profiles.
4. Shift contours or use functional equations without deleting the
   \(\zeta(s_2)\) pole.  Bound every residue separately.
5. Restore the complete \(t\)-integral.  Pointwise convexity,
   subconvexity, or a hybrid moment inserted under an absolute integral is
   acceptable only if its full length and weight yield (168.F2).
6. If an approximate functional equation or inverse Mellin step recreates
   the Round-162 Möbius--Poisson product collar, prove the exact
   correspondence and stop at that scoped self-return.
7. Preserve arbitrary real \(X\), all floors, profiles, stars, endpoints,
   parity, and zero extension, and record the first doubtful step.

## Promotion and stop rule

A target proof must establish (168.F2) for the complete literal scalar and
then use the accepted exact XOR subtraction to obtain the residual.  A
strict result must own a quantitatively defined complete sector and survive
all boundary and power checks.  A no-go must identify the first exact pole,
hard-boundary, transform-integrability, hybrid-moment, or self-return
obstruction and remain scoped to the tested Mellin--Euler mechanism.

Do not replace the signed series by absolute coefficients, open Möbius
variables termwise before the mechanism is assessed, assume rapid Mellin
decay across hard endpoints, discard the \(\zeta\) residue, or quote a
mean-value theorem without its exact range and weights.  There is no
in-round pivot to the residual determinant route, maximal Fejer scale,
another hard-TOP channel, BAL, UNBAL, M1, GAR, or exponent extraction.

Even (168.F2) leaves the other small-\(t\)/intermediate-\(D\) hard-TOP
channels and collars, hard TOP, BAL, UNBAL, M9--M2, both direct M1 parents,
GAR, endpoint uniformity, M9, both bridges, and the quarter theorem open.

## Allocation and terminal labels

The round is 100% analytical/algebraic and 0% numerical.  It closes under
exactly one label:

- hard_top_t1_full_scalar_target;
- strict_t1_mellin_euler_sector; or
- t1_mellin_euler_interface_no_go.

