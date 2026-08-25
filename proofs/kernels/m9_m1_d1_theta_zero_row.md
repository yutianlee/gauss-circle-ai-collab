# Exact finite kernel for the D=1 theta zero row

Campaign: m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate

Status: accepted finite kernel after the validated Round-156 State Patch.

Put \(q=4N\) and

\[
 G_N(t)={\bf1}_{N\mid t}\chi_4(t/N),\qquad
 \mathscr S_N(j)=\sum_{x\bmod q}G_N(x^2-j).
\tag{K156.1}
\]

## Quotient projector and theta recombination

The exact finite projector is

\[
 G_N(t)=-\frac{i}{2N}
 \sum_{\substack{h\bmod q\\h\ {\rm odd}}}
 \chi_4(h)e_q(ht).
\tag{K156.2}
\]

For an odd \(h\), write

\[
 d=(h,N),\qquad h=da,\qquad c=q/d.
\]

Then \(d\mid N\) is odd and \(a\) is a unit modulo \(c\).  The \(x\)-sum
modulo \(q\) consists of \(d\) copies of the complete sum modulo \(c\),
and

\[
 \sum_{x\bmod c}e_c(ax^2)
 =(1+i)\epsilon_a^{-1}\left(\frac ca\right)\sqrt c.
\tag{K156.3}
\]

Since \(\chi_4(a)\epsilon_a^{-1}=\epsilon_a\), one obtains

\[
 \boxed{
 \mathscr S_N(j)=
 -\frac{i(1+i)}{2N}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)d\sqrt c\,K(0,-j;c),
 \qquad c=\frac{4N}{d}.}
\tag{K156.4}
\]

The physical root form is

\[
 \boxed{
 \mathscr S_N(j)=
 \rho_{4N}(j+N)-\rho_{4N}(j+3N),}
\qquad
 \rho_Q(t)=\#\{x\bmod Q:x^2\equiv t\pmod Q\}.
\tag{K156.5}
\]

Thus every odd divisor and two-adic root stratum is retained.

## Finite Fourier transform and interval bound

With

\[
 \widetilde{\mathscr S}_N(h)=
 \sum_{j\bmod q}\mathscr S_N(j)e_q(hj),
\tag{K156.6}
\]

the change of variables \(t=x^2-j\) gives

\[
 \widetilde{\mathscr S}_N(h)=
 \left(\sum_{r\bmod4}\chi_4(r)e_4(-hr)\right)
 \left(\sum_{x\bmod q}e_q(hx^2)\right).
\tag{K156.7}
\]

This vanishes for even \(h\).  If \(h\) is odd, then

\[
 \boxed{
 \left|\widetilde{\mathscr S}_N(h)\right|
 =2\sqrt{2q(h,N)}.}
\tag{K156.8}
\]

The magnitude of the primitive complete quadratic sum can also be checked
without a phase formula:

\[
 \left|\sum_{x\bmod c}e_c(ax^2)\right|^2
 =c\sum_{\substack{u\bmod c\\c\mid2u}}e_c(au^2)=2c.
\tag{K156.9}
\]

Fourier inversion and the finite geometric-series bound imply, for every
consecutive integer interval \(I\) with \(|I|\le q\),

\[
 \boxed{
 \left|\sum_{j\in I}\mathscr S_N(j)\right|
 \ll \sqrt N\,\tau(N)\log(2N).}
\tag{K156.10}
\]

Indeed the right side before divisor grouping is

\[
 \sqrt q\sum_{1\le h\le q/2}\frac{(h,N)^{1/2}}h.
\]

## Weighted zero-row consequence

Let \(A_j=\widehat B_j(0)\).  On either signed defect block, the literal
zero-extended profile, exact residual phase, asymmetric cell, strict mask,
and endpoints give

\[
 \sup_j|A_j|+\operatorname {Var}_j A_j
 \ll_\varepsilon K M^{-3/4}X^\varepsilon,
 \qquad K=\sqrt{NM}.
\tag{K156.11}
\]

The normalized zero row is, by (K156.4),

\[
 \mathcal Z_U(V)=
 \frac1{4N}\sum_{V<|j|\le2V}A_j\mathscr S_N(j).
\tag{K156.12}
\]

For \(V\le K<N<q\), discrete Abel summation on the two sign intervals,
(K156.10), and (K156.11) yield

\[
 \boxed{
 \mathcal Z_U(V)
 \ll_\varepsilon M^{-1/4}X^\varepsilon.}
\tag{K156.13}
\]

This kernel is specific to \(v=0\).  It does not estimate the incomplete
nonzero matrix containing
\(\widehat B_j(2dv)K(-v^2,-j;4N/d)\), and it makes no broader owner or
exponent claim.
