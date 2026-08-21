# Round 97 statement packet: M2 outside-packet and endpoint assembly

This is a statement-only packet. It freezes a conditional assembly
question and does not assert that the canonical top theorem proves full
M9-M2.

## 1. Exact physical partition and target

Put \(y=\lfloor\sqrt X\rfloor\). The accepted denominator partition has

\[
 D_j=2^{-j}\sqrt X
\]

up to fixed constant rescalings, one hard top band with the physical
cutoff \(d\le y\), smooth interior bands, and a bottom remainder
\(d\ll X^{1/4}\). For an active band,

\[
 H_D=\lfloor DX^{-1/4}\rfloor,
\]

and the actual M2 Vaaler polynomial is decomposed into dyadic odd
frequency blocks \(1\le L\le H_D\), retaining both quarter shifts,
\(\chi_4(h)\), the exact \(1/h\) taper, profiles, floors, stars, and
both signs.

Write

\[
 D=X^\delta,\qquad L=X^\ell,\qquad
 \Omega=\left\{(\delta,\ell):
 \frac14\le\delta\le\frac12,\quad
 0\le\ell\le\delta-\frac14\right\}.
\]

The pointwise target for every literal block is
\(O_\varepsilon(X^{1/4+\varepsilon})\); logarithmically many blocks
must assemble with one-count ownership.

## 2. Accepted direct owners

The following are accepted:

1. the bottom denominator remainder is
   \(O(X^{1/4})\) before Fourier expansion;
2. every Vaaler Fejer residual, including hard top, exact products,
   integer jumps, and shifted legs, is
   \(O_\varepsilon(X^{1/4+\varepsilon})\) pointwise;
3. the two-shift theorem closes the terminal line
   \(\ell=\delta-1/4\);
4. the full second-derivative menu closes the point
   \((\delta,\ell)=(1/2,0)\);
5. the audited Tao--Trudgian--Yang pair and actual normalized-BV
   profiles close

\[
 178\ell+1638\delta\le463.
\]

Hence the exact residual phase-diagram set is

\[
 \mathcal U=
 \left\{(\delta,\ell)\in\Omega:
 0\le\ell<\delta-\frac14,\quad
 178\ell+1638\delta>463\right\}
 \setminus\{(1/2,0)\}.
\]

## 3. Smooth and hard endpoint transforms

For a smooth interior denominator band, exact Poisson and stationary
phase give

\[
 \mathcal B^+_{L,W}
 =-\frac{e(1/8)}{2\pi}X^{1/4}M^{-3/4}
 \mathcal T_{L,K}+O_W(1),
\]

where

\[
 K=\frac{XL}{D^2},\qquad M=LK,
\]

and

\[
 \mathcal T_{L,K}
 =\sum_{h\asymp L}\sum_{k\asymp K}
 \chi_4(h)a_{L,K}(h,k)e(\sqrt{Xhk}).
\]

The exact smooth target is

\[
 \mathcal T_{L,K}\ll_\varepsilon M^{3/4}X^\varepsilon.
\]

This is an equivalent formulation, not an accepted estimate. On
balanced top-scale smooth bands, the accepted gcd decomposition further
reduces the remaining small-gcd part to the outside-absolute signed
quarter packet

\[
 \left|\sum_GG\mathscr P_G\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

That packet estimate is also open.

The single hard top band has the one-sided transform

\[
 \mathcal T_{\rm end,L}
 =\sum_{\substack{h\asymp L\\h\ {\rm odd}}}
 \sum_{\lceil h/4\rceil\le m\le h}
 \chi_4(h)a_{\rm end}(h,m)e(\sqrt{Xhm}),
\]

with target \(L^{3/2}X^\varepsilon\). Its boundary and transform errors
are accepted and target-safe.

## 4. Canonical hard-top assumption

The open canonical theorem controls only the residual hard part of the
single hard top band:

\[
 \sum_{A,D_{\rm ray},K_{\rm rec},G,R}
 |\mathfrak Q_{A,D_{\rm ray},K_{\rm rec},G,R}|
 \ll_\varepsilon L^2X^\varepsilon.
\]

Together with the already owned hard-top diagonal, collars, Poisson
modes, square rays, exact nonsquare centres, positive-safe blocks, and
errors, it implies

\[
 \mathcal T_{\rm end,L}\ll_\varepsilon
 L^{3/2}X^\varepsilon.
\]

This assumption says nothing by itself about a smooth denominator band,
the unbalanced smooth dual target, or final assembly across all \(D,L\).

## 5. Frozen Round-97 question

Construct the exact one-count table for every physical denominator band
and every frequency block. Decide:

1. which cells are owned by the bottom, R5, terminal, second-derivative,
   or TTY inputs;
2. which residual cells are in the single hard top band and would close
   under the canonical assumption;
3. which residual cells are smooth balanced endpoint packets;
4. which residual cells are unbalanced smooth dual packets;
5. whether character-factor, near-collision, fourth-moment, or
   average-to-pointwise nodes are genuine additional dependencies or
   only alternative routes;
6. whether the resulting conditional assembly is uniform in real \(X\)
   through every dyadic endpoint.

The strongest possible positive output is a conditional theorem listing
the minimal additional outside-packet estimates which, together with the
canonical hard-top theorem, imply M9-M2. A rigorous proof that the
canonical theorem alone is insufficient is also a successful result.

## 6. Mandatory controls

Every proposed assembly must retain:

1. the exact active \((\delta,\ell)\) triangle and the residual
   \(\mathcal U\);
2. the distinction between the one hard top band and smooth bands with
   the same exponent-scale \(\delta=1/2+o(1)\);
3. the bottom remainder and R5 as separate owners;
4. both quarter shifts and the exact \(\chi_4(h)\) factor;
5. height floors, profiles, hard cutoff, stars, and both signs;
6. smooth Poisson support crossings and hard one-sided boundary terms;
7. one-count ownership under the dyadic \(D,L\) partitions;
8. real-\(X\) and \(y=\lfloor\sqrt X\rfloor\) uniformity;
9. the difference between a proved reduction and a proved estimate;
10. legacy fourth-moment and near-collision routes without circular
    dependencies;
11. downstream separation from M9-M1, M9, and the quarter target;
12. the unchanged global exponent ledger.

## 7. Scope

This is a reconciliation/formalization round, not a new speculative core
attack. Do not assume the open canonical Gram, the smooth
\(M^{3/4}\) product-phase bound, or the balanced quarter-packet bound.
Do not infer M9-M1. No global exponent may change unless an actual
previously open outside packet is proved and fully assembled.
