# Round 111 derivation packet

Campaign: m9-m2-adjacent-ray-transport-commutator

Starting graph SHA-256:
c93f14d6790341b792b54bbaa7ccb96c211741d666729f08addc80fb91d1b759

## Accepted starting point

Round 110 proves that the hard-top energy is target-sized if and only if,
up to target-sized terms,

\[
 \Re\mathfrak C_L^{\mathrm{off}}
 \ll_\varepsilon L^2X^\varepsilon,
\]

where, on one orientation,

\[
 \mathfrak C_L^{\mathrm{off}}
 =\sum_{a\ \mathrm{odd}}\sum_{q\in\mathbb Z}(-1)^qF_{L,a}(q)
 =\sum_{a,r}\bigl(F_{L,a}(2r)-F_{L,a}(2r+1)\bigr).
\tag{111.1}
\]

The literal row is

\[
 \begin{aligned}
 F_{L,a}(q)={}&1_{q\ge1}1_{(a,a+2q)=1}
 \sum_{\substack{g\ \mathrm{odd}\\ga,g(a+2q)\in\mathscr H_L}}
 \sum_{m=\lceil g(a+2q)/4\rceil}^{ga}
 a_{\mathrm{end}}(ga,m)\overline{a_{\mathrm{end}}(g(a+2q),m)}\\
 &\quad\times
 e\!\left(J(\sqrt{ga}-\sqrt{g(a+2q)})\sqrt m\right),
 \end{aligned}
\tag{111.2}
\]

zero-extended to every integer (q). All prior target-safe owners may be
removed only through their accepted scalar bounds; all remaining support
and coefficient data stay literal.

## Exact parity commutator

For the shift (Sf(q)=f(q+1)), finiteness and zero extension give

\[
 2\sum_q(-1)^qf(q)
 =\sum_q(-1)^q(I-S)f(q).
\tag{111.3}
\]

This is a high-pass identity, not a variation estimate. Taking absolute
values after (I-S) is a strictly stronger route and may fail.

## Proposed non-self-returning degree of freedom

Put (b_q=a+2q) and

\[
 \delta_q=\sqrt{b_q}-\sqrt a,
 \qquad
 \lambda_q=\left({\delta_q\over\delta_{q+1}}\right)^2.
\tag{111.4}
\]

For the continuous physical phase

\[
 \Phi_q(x)=-J\sqrt g\,\delta_q\sqrt x,
\]

one has the exact phase alignment

\[
 \Phi_{q+1}(\lambda_qx)=\Phi_q(x).
\tag{111.5}
\]

In the completed ((x,k)) representation the simultaneous scaling

\[
 (x,k)\longmapsto(\lambda_qx,k/\lambda_q)
\tag{111.6}
\]

also preserves (kx). The only possible gain must therefore come from the
commutator between this phase-preserving transport and the literal integer
lattices, finite supports, and actual amplitude. It may not be obtained by
another invertible Poisson, Gaussian, or stationary transform.

## Mandatory decomposition

Any positive proof must isolate and estimate, without overlap:

1. the smooth common-interior transported amplitude;
2. the integer (m)- or (k)-lattice mismatch under (111.6);
3. coprimality changes, using ((a,a+2q)=(a,q)) for odd (a);
4. lift births/deaths from (ga,g(a+2q)\in\mathscr H_L);
5. the moving ceiling and hard lower edge;
6. reciprocal-support, collar, entry/exit, floor, star, and equality jumps;
7. exact and near metric centres and the prior (q=1), polylogarithmic,
   square, Pell, fourth-power, and positive-safe owners.

The capacity target is (L^2X^\varepsilon). A strict subrange must state
its exact (A,D,G,K) inequalities and the saved power. An equal-capacity
result must identify the first defect that restores the original capacity.

## Frozen false routes

- total adjacent variation is sufficient but not necessary;
- centered material differentiation alone leaves the Round-105 reciprocal
  phase and is not new;
- a (q,k) Hessian followed by two B-processes returns the dual square;
- primitive Mobius expansion alone supplies no (D)-saving;
- arbitrary or phase-conjugating coefficients are controls, not lower
  bounds for the actual symbol;
- both orientations plus an outer (2\Re) double count.

