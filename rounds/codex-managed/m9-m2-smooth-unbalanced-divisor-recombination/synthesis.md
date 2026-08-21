# Round 107 synthesis: truncated-divisor fixed-centre return

Campaign: m9-m2-smooth-unbalanced-divisor-recombination

Starting graph SHA-256:
d20981c158e3525b89fd9f5e1352580fcd1349e7662e14c990bf9896b4da4e16

Resulting graph SHA-256 after the validated State Patch:
7347081c1a765acafc6a4d1e3a96171d7b971079c2af144f7a0eaa825309bb2a

## Frozen objective

The round asked whether the literal unbalanced smooth M2 packet

\[
 \mathcal T_{L,K}
 =\sum_{h\asymp L}\sum_{k\asymp K}
 \chi_4(h)a_{L,K}(h,k)e(\sqrt{Xhk}),
 \qquad K={XL\over D^2},
\]

could be regrouped into a complete (r_2/4) coefficient, transformed to a
strictly shorter packet, or bounded on a new residual corridor. The target
was \(\mathcal T_{L,K}\ll_\varepsilon(LK)^{3/4}X^\varepsilon\).

## Exact divisor and Mellin interface

Product regrouping is exact:

\[
 \mathcal T_{L,K}
 =\sum_nA_{L,K}(n)e(\sqrt{Xn}),\qquad
 A_{L,K}(n)=\sum_{hk=n}\chi_4(h)a_{L,K}(h,k).
\]

It preserves every lift and actual weight, and

\[
 \sum_n|A_{L,K}(n)|^2\ll_\varepsilon LKX^\varepsilon.
\]

For one separated Mellin mode,

\[
 \sum_{n\ge1}{1\over n^s}
 \sum_{hk=n}\chi_4(h)h^{it_1}k^{it_2}
 =L(s-it_1,\chi_4)\zeta(s-it_2).
\]

The literal coefficient is the full two-height inverse-Mellin
superposition. It is not the zero mode and does not equal (r_2(n)/4).
A prime (p\equiv3\pmod4) supplies an exact falsifier: a cell can contain
one complementary incidence while the complete coefficient is zero.

## Functional-equation capacity

With

\[
 M=LK={XL^2\over D^2},\qquad F=\sqrt{XM}={XL\over D},
\]

the radial Mellin height is (F). Both degree-one root numbers are (+1),
and the reflected factor lengths are

\[
 L^*\asymp {X\over D},\qquad K^*\asymp D,qquad
 L^*K^*\asymp X.
\]

The formal resonant width is

\[
 \Delta={X\over F}={D\over L}.
\]

Absolute dual summation therefore misses the target by

\[
 {\Delta\over X^{1/4}}
 ={D\over LX^{1/4}}={H_D\over L}.
\]

This becomes one only on the already owned terminal line. A complete
functional-equation theorem must additionally retain the zeta pole, both
Mellin tails, owner kernels, and endpoint errors; no root-number gain or
shorter packet appears.

## Exact smooth-component return

Resolving the character and applying the (h)-process gives

\[
 h_*={4Xk\over r^2},\qquad
 e(Xk/r),qquad
 2\sqrt2\,i,e(-1/8)\chi_4(r)(Xk)^{1/2}r^{-3/2}.
\]

For the literal smooth symbol, all scale factors cancel:

\[
 \mathcal T_{L,K}^{\mathrm{stat}}
 =i e(-1/8)X^{-1/4}(LK)^{3/4}
 \sum_{r\ \mathrm{odd}}\chi_4(r)W\!\left({X\over rD}\right)
 \sum_k{q_L(4Xk/r^2)\over k}e(Xk/r).
\]

The inherited physical prefactor leaves exactly (-i/(2\pi)) times the
dimensionless row. On a fixed flat smooth component, the aggregate
stationary remainder is (O(KF^{-1/2})), hence (O(L^{-1})) after physical
normalization. Sharp clipped, starred, hard, or arithmetic-owner boundaries
must remain as exact endpoint/Fresnel kernels.

Exact (k)-Poisson and regrouping by (s=dr) produce

\[
 \mathscr R_{D,L}(X)=
 \sum_s\sum_{\substack{r\mid s\\r\ \mathrm{odd}}}
 \chi_4(r)W\!\left({X\over rD}\right)
 \int_0^\infty {q_L(h)\over h}
 e\!\left({hr(X-s)\over4X}\right)dh.
\]

It is a prescribed-centre truncated-divisor wavelet supported rapidly on

\[
 |s-X|\lesssim {D\over L}.
\]

Divisor bounds give only \((D/L)X^\varepsilon\), while the physical
target is \(X^{1/4+\varepsilon}\). This reproduces exactly the deficit
\(H_D/L\).

## Exact correlation criterion

If (z_n=A_{L,K}(n)e(\sqrt{Xn})), zero-extended on an interval of length
(O(M)), sliding-window Cauchy shows that for (Q\asymp M^{1/2}),

\[
 \Re\sum_{q=1}^{Q-1}\left(1-{q\over Q}\right)
 \sum_nz_{n+q}\overline{z_n}
 \ll_\varepsilon MX^\varepsilon
\]

is sufficient for the three-quarter target. This exact outside-absolute
condition retains

\[
 h_1k_1-h_2k_2=q
\]

with both characters, both actual symbols, and the square-root phase. It is
a reduction, not a proved estimate.

## Source and completion gates

Popov applies to complete (r_2), not the moving truncated coefficient. At
cutoff (M), his exact error has size

\[
 \sqrt{X/M}\,X^{o(1)}={D\over L}X^{o(1)},
\]

and is target-safe only on the terminal line. Extending to (X^{1/2})
returns to the complete Hardy--Voronoi formulation of the Gauss target.
Audited Li--Yang/cone, TTY, double-large-sieve, Huxley, and withdrawn
Bourgain--Watt routes do not prove the literal fixed-centre correlation.

## Conductor decision

Promote narrowly:

- exact product regrouping and weighted energy;
- the separated (L\zeta) Mellin interface;
- failure of automatic (r_2/4) completion;
- the root-number, conductor, dual-length, and capacity ledger;
- the scoped flat-smooth (h)-process/(k)-Poisson normalization through
  (-i/(2\pi));
- the exact fixed-centre truncated-divisor survivor;
- the signed sliding-window correlation implication.

Retain open:

- the fixed-centre signed estimate and the original three-quarter target;
- endpoint/star/owner transform kernels outside the flat smooth scope;
- balanced smooth M2, the hard M2 cone, M9-M2, M9-M1, endpoint uniformity,
  M9, and the quarter target.

No global exponent changes. The repaired source-audited Li--Yang exponent

\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots
\]

remains the strongest certified global result in the project, and the
strongest internal uniform exponent remains (1/3).

## Next interface

The smallest coefficient-preserving survivor is

\[
 \mathscr R_{D,L}(X)\ll_\varepsilon X^{1/4+\varepsilon},
\]

with actual profiles and owners. Another functional equation, absolute
divisor estimate, or coefficient-blind cone argument returns the same
capacity. Any future attack must obtain the factor (H_D/L) from the true
signed truncated coefficient before absolute values, or leave this packet
for a genuinely different canonical core.
