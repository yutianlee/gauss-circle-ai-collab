# Conductor candidate: birth-block curvature followed by lift-character Abel

Campaign: gc-w7-16-joint-stieltjes-reciprocal-curvature-gate

Starting graph SHA-256:
476b1445ef73d86627fd87de8bd2dd76a5efa53564a5b195230f2ad33ba2bbe8

## 1. Result

The exact Stieltjes-character family admits a direct joint estimate at the
capacity required by the Round-127 connector:

\[
 \left|\sum_{v\in I}^{*}U_{i,\rho,\eta}(v)e(\phi(v))\right|
 \ll_\varepsilon
 {J_B^{1/2}\over L}
 \min\left(
 N_\rho,\,
 N_\rho\sqrt{\Lambda_\rho}+\Lambda_\rho^{-1/2}
 \right)Y^\varepsilon,
 \tag{129.C1}
\]

where

\[
 \phi(v)=-{ca'\over\kappa_i\rho v}
          +\vartheta_{i,\eta}\rho v,\qquad
 \Lambda_\rho=\lambda_B\rho^2,\qquad
 N_\rho\asymp Q_B/\rho.
\]

The proof does not establish the stronger norm-relative statement for
every \(V^2\) sequence.  Instead, it uses the actual threshold
representation proved in Round 128.  For one threshold, interchange the
\(v\)- and \(g\)-sums.  Consecutive \(g\)'s cut the \(v\)-window into
disjoint lift-birth blocks.  Apply the weighted second-derivative estimate
on each such block, sum their absolute values, and only then use the
bounded partial sums of \(\chi_4(g)\) by Abel summation in \(g\).

The apparent extra term \(J_B\Lambda_\rho^{-1/2}\) is absorbed because

\[
 {N_\rho\Lambda_\rho\over J_B-1}\asymp L\rho
 \tag{129.C2}
\]

whenever \(J_B-1\gg1\).  Thus the birth blocks are sparse enough relative
to the reciprocal curvature.  Exact Stieltjes superposition then costs
only the already accepted denominator-profile variation.

If every literal seam below survives independent review, (129.C1) gives
the complete \(Y^{73/96+\varepsilon}\) fixed-block bound.  It does not
reach the \(Y^{1/2+\varepsilon}\) determinant target and does not improve
the global one-third theorem.

## 2. Exact abstract statement

Let \(I\) be an interval of \(N\) consecutive integers, let
\(b'=\rho v\asymp B\) on \(I\), and let its physical \(b'\)-length be at
most \(Q\).  Suppose

\[
 |\phi''(v)|\asymp\Lambda
 \tag{129.C3}
\]

throughout \(I\).  Let \(P\), zero-extended to the integers, be supported
on \(g\asymp G\) and satisfy

\[
 \|P\|_\infty+\operatorname {Var}_gP\le C_P.
\]

Let \(w\), zero-extended to the integers, be supported on \(t\asymp D\)
and satisfy

\[
 \|w\|_\infty+\operatorname {Var}_tw\le C_w.
\]

Let \(\tau\) be supported on \(O(1)\) clipped subintervals of \(I\), with
zero-extended supremum plus variation at most \(C_\tau\).  Assume
\(|a|G\asymp L\), and define

\[
 U(v)={\tau(v)\over a}
 \sum_g{\chi_4(g)\over g}P(g)w(g\rho v).
 \tag{129.C4}
\]

Put

\[
 J=1+{DQ\over B^2},\qquad
 K=\min\left(N,N\sqrt\Lambda+\Lambda^{-1/2}\right).
\]

If either \(J=O(1)\), or

\[
 N\Lambda\gg J,
 \tag{129.C5}
\]

then

\[
 \boxed{
 \left|\sum_{v\in I}U(v)e(\phi(v))\right|
 \ll C_PC_wC_\tau\,{J^{1/2}K\over L}.}
 \tag{129.C6}
\]

For the literal critical parameters,
\(N=N_\rho\), \(\Lambda=\Lambda_\rho\), and (129.C5) holds with the
stronger identity (129.C2).

## 3. One-threshold proof

Zero-extend \(w\), put

\[
 c_t=w(t)-w(t+1),\qquad
 w(d)=\sum_{t\ge d}c_t,\qquad
 \sum_t|c_t|=\operatorname {Var}(w),
 \tag{129.C7}
\]

and first fix one \(t\asymp D\).  Define

\[
 U_t(v)={\tau(v)\over a}
 \sum_{g\le t/(\rho v)}{\chi_4(g)\over g}P(g).
\]

Finite Fubini gives

\[
 \sum_{v\in I}U_t(v)e(\phi(v))
 ={1\over a}\sum_g{\chi_4(g)P(g)\over g}Z_t(g),
 \tag{129.C8}
\]

where

\[
 Z_t(g)=
 \sum_{\substack{v\in I\\v\le t/(\rho g)}}\tau(v)e(\phi(v)).
 \tag{129.C9}
\]

Every \(Z_t(g)\) is a weighted partial interval sum.  The standard
weighted second-derivative estimate, including the trivial alternative,
therefore gives

\[
 \sup_g|Z_t(g)|\ll C_\tau K.
 \tag{129.C10}
\]

For consecutive \(g\), the difference \(Z_t(g+1)-Z_t(g)\) is the
weighted exponential sum over

\[
 I_{t,g}=
 I\cap\left({t\over\rho(g+1)},{t\over\rho g}\right].
 \tag{129.C11}
\]

The nonempty intervals (129.C11) are disjoint.  Their number \(R_t\) and
total length obey

\[
 R_t\ll J,\qquad
 \sum_g|I_{t,g}|\le N.
 \tag{129.C12}
\]

The zero-extended multiplier \(\tau\) has bounded variation.  Applying
the weighted second-derivative estimate separately on (129.C11) and
summing gives

\[
 \sum_g|Z_t(g+1)-Z_t(g)|
 \ll C_\tau
 \min\left(N,N\sqrt\Lambda+J\Lambda^{-1/2}\right).
 \tag{129.C13}
\]

If \(K=N\), the first branch in (129.C13) is at most \(K\), hence at most
\(J^{1/2}K\).  If
\(K=N\sqrt\Lambda+\Lambda^{-1/2}<N\), then

\[
 N\sqrt\Lambda\le K\le J^{1/2}K.
\]

For \(J=O(1)\), the last term in (129.C13) is also \(O(K)\).  For
\(J\gg1\), condition (129.C5) gives

\[
 {J\over\sqrt\Lambda}
 \le J^{1/2}N\sqrt\Lambda
 \le J^{1/2}K.
 \tag{129.C14}
\]

Thus in every case

\[
 \operatorname {Var}_g Z_t(g)
 \ll C_\tau J^{1/2}K.
 \tag{129.C15}
\]

Because \(P\) is sampled BV and \(g\asymp G\),

\[
 \sup_g\left|{P(g)Z_t(g)\over g}\right|
 +\operatorname {Var}_g\left({P(g)Z_t(g)\over g}\right)
 \ll {C_PC_\tau J^{1/2}K\over G}.
 \tag{129.C16}
\]

Every partial sum of \(\chi_4\) is bounded.  Abel summation in (129.C8),
performed before any modulus over \(g\), now yields

\[
 \left|\sum_{v\in I}U_t(v)e(\phi(v))\right|
 \ll {C_PC_\tau J^{1/2}K\over |a|G}
 \ll {C_PC_\tau J^{1/2}K\over L}.
 \tag{129.C17}
\]

This is the joint saving: curvature controls each birth block, and the
common lift character controls the variation of their cumulative sums.

## 4. Stieltjes superposition and literal parameters

By (129.C7),

\[
 U(v)=\sum_t c_tU_t(v).
\]

Triangle inequality over the threshold coefficients is lawful because
their total mass is exactly the zero-extended sampled variation of the
literal denominator profile.  Applying (129.C17) uniformly in
\(t\asymp D\) proves (129.C6).

For the literal phase,

\[
 \phi''(v)=-{2ca'\over\kappa_i\rho v^3},
\]

so on \(v\asymp B/\rho\),

\[
 |\phi''(v)|
 \asymp {YL\rho^2\over DB^2}
 =\lambda_B\rho^2=\Lambda_\rho.
 \tag{129.C18}
\]

Moreover,

\[
 {N_\rho\Lambda_\rho\over J_B-1}
 \asymp
 {{Q_B\over\rho}{YL\rho^2\over DB^2}
  \over {DQ_B\over B^2}}
 ={YL\rho\over D^2}
 =L\rho,
 \tag{129.C19}
\]

because \(D^2=Y\).  Thus (129.C5) holds with a power margin.  If
\(J_B-1=O(1)\), the bounded-block case already used above applies.

The M1 quarter-linear phase has zero second derivative and does not change
(129.C18).  The M2 reduced numerator character is fixed.  The Möbius
factor has modulus at most one, the proof is uniform for every
\(\rho\mid a'\), and the later divisor sum costs \(Y^\varepsilon\).

The literal triangular determinant weight, clipped sign sector, strict or
weak face, star, and half-open shell cut are all included in \(\tau\).
Their zero-extended supremum plus total variation is \(O(1)\) on the
same physical window.  A window meets only \(O(1)\) shell owners.

## 5. Generic \(V^2\) control and scope

For a general sequence \(u_1,\ldots,u_N\), set

\[
 \|u\|_H^2=|u_1|^2+\sum_{j<N}|u_{j+1}-u_j|^2+|u_N|^2.
\]

If \(z_j=e(\phi(j))\) and
\(T_k=\sum_{j>k}z_j\), \(0\le k\le N\), then the exact dual norm is

\[
 \left\|\sum_ju_jz_j\right\|_{H^*}
 =
 \min_{\alpha\in\mathbb C}
 \left(\sum_{k=0}^{N}|T_k-\alpha|^2\right)^{1/2}.
 \tag{129.C20}
\]

Interval bounds \(|T_j-T_k|\le K\) give only
\(O(N^{1/2}K)\) in (129.C20), and this loss is sharp for generic
amplitudes.  Therefore (129.C6) is not obtained from the displayed
\(V^2\) norm alone.  It is a direct theorem for (129.C4).  The accepted
connector should be revised from a generic norm-relative assertion to
this actual-family birth-block/character estimate.

## 6. Capacity consequence

At the critical block write \(B=Y^b\), \(1/3\le b\le1/2\).  Then

\[
 K_\rho\ \hbox{after the divisor sum has capacity}\ Y^{11/48+o(1)},
\qquad
 J_B=1+Y^{19/48-b}.
\]

The accepted outer ledger turns (129.C1) into

\[
 |\mathfrak O_{i,B}|
 \ll_\varepsilon
 Y^{35/48+\frac12\max(0,19/48-b)+\varepsilon}.
\]

The maximum is at \(b=1/3\), giving

\[
 |\mathfrak O_i|
 \ll_\varepsilon Y^{73/96+\varepsilon}.
 \tag{129.C21}
\]

This is a strict \(Y^{1/96}\) improvement over the complete
\(Y^{37/48+\varepsilon}\) envelope.  It remains far above the
\(Y^{1/2+\varepsilon}\) determinant target, and its persistence exponent
\(115/288\) is worse than \(1/3\).

## 7. First doubtful step and state recommendation

The analytic kernel is complete provided the blockwise weighted
second-derivative estimate in (129.C13) is uniform after every literal
clipping and star, and provided the accepted outer ledger really uses the
same \(Q_B\)-window and no additional cross-shell coefficient.  These are
the two seams requiring independent audit.

After those seams pass, promote the direct actual-family estimate
(129.C1) and the complete fixed-block consequence (129.C21).  Revise, but
do not falsely promote, the generic norm-relative formulation: (129.C20)
shows why generic \(V^2\) is insufficient.  Make no change to the
\(Y^{1/2}\) determinant target, either M9 component, endpoint uniformity,
M9, the global one-third theorem, or the quarter target.
