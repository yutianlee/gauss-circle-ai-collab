# Round 123 derivation packet: reciprocal-frequency Gram and alias products

Campaign: `m9-m2-unbalanced-reciprocal-gram-factorization-gate`

Starting graph SHA-256:
`d29ae6c0f398cc2df699b15ee2901b525290263b6cde5eecece49cdeee095bb1`

## 1. Accepted interface

Round 118 proved, for one fixed flat smooth strict UNBAL component,

\[
 |\mathscr R_{D,L}(X)|\ll_\varepsilon X^\varepsilon
 \min\left({D\over L},\sqrt{XL/D}+\sqrt{X/(LD)}\right).
\]

Writing \(a=\delta-\ell\), this has exponent
\(\min(a,(1-a)/2)>1/4\) at every strict residual point. The exact centre,
one consecutive same-character central run, and the integer phase-one
square sector are target-safe. A second coefficient-preserving transform
returns the same truncated product wave. The smallest accepted survivor is
the complete joint row (123.B3) before the \(k\)-triangle.

No sharp, starred, clipped, hard, arithmetic-owner, or transition kernel
is part of this flat-smooth campaign.

## 2. Candidate phase integerization

Put \(N=\lfloor X\rfloor\). Direct termwise replacement of
\(e(Xk/r)\) by \(e(Nk/r)\) in the reciprocal row can cost \(K\), so the
formal estimate \(|X-N|k/r\ll L/D\) cannot simply be multiplied by the
post-cancellation product capacity.

The candidate lawful route is the physical kernel. The coefficientwise
Poisson identity sends the phase-integerized row to

\[
 \sum_{r\ {\mathrm{odd}}}\chi_4(r)W(X/(rD))
 \sum_d\mathcal Q_L\!\left({r(N-rd)\over4X}\right).
\]

Since

\[
 \mathcal Q_L'(y)=2\pi i\int_0^\infty q_L(h)e(hy)\,dh,
 \qquad |\mathcal Q_L'(y)|\ll L,
\]

the central-window pointwise perturbation is \(O(L/D)\). There are only
\((D/L)X^\varepsilon\) divisor incidences in the union of the two
unit-shifted product windows, suggesting total cost \(O(X^\varepsilon)\).
This is a candidate until a uniform rapid-tail layer cake, tied integer
products, support edges, and \(K\asymp1\) are all charged.

## 3. Exact weighted Gram

With \(A_{r,k}\) and \(B_k\) as in the blind statement,
\(\sum_{k\asymp K}1/k=O(1)\) gives

\[
 |\mathscr R_N^\sharp|^2
 \ll \sum_{k\asymp K}{|B_k|^2\over k}=:\mathcal G_N.
\tag{123.D1}
\]

Expanding produces the literal signed Gram

\[
 \mathcal G_N=
 \sum_{r,s\ {\mathrm{odd}}}\chi_4(r)\chi_4(s)
 W(X/(rD))W(X/(sD))\mathcal K_{r,s}.
\tag{123.D2}
\]

It is real and nonnegative only after all ordered pairs are combined. Its
diagonal is of order \(R=X/D\) on a nondegenerate interior cell, whereas
the square target is \(X^{1/2+\varepsilon}\). Since \(D<X^{1/2}\), a
proof that takes absolute values before signed off-diagonal aggregation
meets a diagonal barrier. A useful result must prove cancellation between
the diagonal and the complete actual-sign off-diagonal, or avoid this
Cauchy norm through a strictly stronger joint inequality.

Smooth summation by parts predicts

\[
 |\mathcal K_{r,s}|\ll_A
 \left(1+K\left\|N\left({1\over r}-{1\over s}\right)\right\|\right)^{-A}.
\tag{123.D3}
\]

Every derivative and the overlap of the two sampled \(q_L\) profiles
must be audited; (123.D3) is not permission to replace the kernel by a
rectangular cutoff.

## 4. Alias-product algebra

Choose an integer alias \(j\) and put

\[
 E=N(s-r)-jrs.
\]

Then

\[
 N(1/r-1/s)=j+{E\over rs},
\qquad
 (N-jr)(N+js)-N^2=jE.
\tag{123.D4}
\]

The Gram window (123.D3) has

\[
 |E|\lesssim {rs\over K}X^\varepsilon
 \asymp {X\over L}X^\varepsilon,
\qquad |j|\ll D,
\tag{123.D5}
\]

up to fixed support constants. Thus exact aliases factor a divisor of
\(N^2\), while near aliases are lattice points in a short multiplicative
annulus around \(N^2\). Absolute counting has capacity about \(X/L\) and
is not sufficient by itself.

For \(N=2^tN_0\), \(N_0\) odd, the definition of \(E\) gives

\[
 {jrs+E\over2^{t+1}}=N_0{s-r\over2}\in\mathbb Z.
\]

Consequently the exact character product may be written

\[
 \chi_4(r)\chi_4(s)
 =(-1)^{(s-r)/2}
 =(-1)^{(jrs+E)/2^{t+1}}.
\tag{123.D6}
\]

For \(E=0\), necessarily \(2^{t+1}\mid j\), and

\[
 \chi_4(r)\chi_4(s)=(-1)^{j/2^{t+1}}.
\tag{123.D7}
\]

These are elementary candidate identities to be independently checked,
especially for the orientation of \(j\), negative aliases, and all
two-adic branches. The analytic question is whether (123.D6) supplies
defect cancellation after the literal factor congruences and amplitudes
are retained, or is only the original period-four character written in
new coordinates.

## 5. Promotion threshold

Promote only one of:

1. the full flat-smooth target with phase perturbation and all seams;
2. a nonempty strict exponent region reaching \(X^{1/4+\varepsilon}\);
3. a quantified actual-sign saving beyond the Round-118 envelope;
4. an inverse theorem isolating all packets capable of exceeding target;
5. a scoped Gram/factorization no-go with the exact smallest signed
   survivor.

The first doubtful analytic step is cancellation in the complete
near-product defect sum. Exact factorization, exact-collision divisor
counts, the sign lock by itself, or a positive Gram identity does not
prove that cancellation. No numerical experiment or external theorem is
planned.
