# Round 11 synthesis: exact near-product kernel and the cross-product seam

Campaign: `m9-m1-near-product-character-kernel`  
Round type: signed near-product kernel  
Graph SHA-256 before patch: `9ecc34dcf97f615b0f39fc8dfd3021ee5c31659e593088e09e88166b889199cb`

## Conductor decision

Promote the exact nearest-product regrouping and the exact two-sided odd
kernel. Promote the scoped no-go: neither single-fiber character
cancellation, coefficient-norm control, nor whole-shell freezing can provide
the missing power in a fixed interior part of the M1 residual corridor.
Retain the actual cross-product discrepancy estimate as open.

The exact kernel and freezing obstruction were independently derived in the
statement-only report and the hostile report. The prime-product norm
obstruction uses a primary fixed-modulus prime-counting theorem whose stated
hypotheses were checked against the official arXiv record.

## Exact regrouping

Let

\[
u_{L,H}(h)=v_L(h)\frac{\Phi(h/(H+1))}{h},
\qquad
\mathcal K^+_{L,H}(z)=\sum_{h>0}u_{L,H}(h)e(hz).
\]

Choose

\[
m_X(d)=\left\lfloor X/d+\frac12\right\rfloor,
\qquad n_X(d)=d,m_X(d).
\]

Then the actual positive M1 block, up to its displayed fixed factor, is
exactly

\[
\sum_n\sum_{\substack{d:n_X(d)=n}}
\chi_4(d)w_D(d)
\mathcal K^+_{L,H}\!\left(\frac{X-n}{d}\right).
\]

Equivalently, the inner conditions are

\[
d\mid n,qquad -d/2\le X-n<d/2,
\]

with the displayed half-integer tie convention. This finite regrouping
includes the hard top endpoint without a Poisson boundary term.

For real profiles, pairing the actual positive and negative Vaaler
frequencies gives the odd kernel

\[
\mathcal V_{L,H}(z)=\frac4\pi
\sum_{h>0}u_{L,H}(h)\sin(2\pi hz),
\]

and hence

\[
\mathcal M_{1,L}(D;X)=
\sum_n C_{D,L}(n;X),
\]

where

\[
C_{D,L}(n;X)=
\sum_{d:n_X(d)=n}
\chi_4(d)w_D(d)
\mathcal V_{L,H}\!\left(\frac{X-n}{d}\right).
\]

The exact-product fiber vanishes identically in the two-sided block because
\(\mathcal V_{L,H}(0)=0\). In a one-sided block it is only
\(O_\varepsilon(X^\varepsilon)\), as is the tie fiber.

## Required saving and exact open lemma

Write \(H\asymp DX^{-1/4}\). The natural critical window has length

\[
\Delta=D/L=X^{1/4}H/L.
\]

The target therefore requires a factor \(H/L\) beyond divisor multiplicity
whenever \(L<H\). The weakest exact remaining lemma is

\[
\boxed{
\left|\sum_n C_{D,L}(n;X)\right|
\ll_\varepsilon X^{1/4+\varepsilon}}
\]

uniformly on \(\mathcal U_1\). The absolute value must remain outside the
whole \((n,d)\)-sum.

An annular sufficient version retains the normalized actual symbol on
\(|X-n|\asymp R\) and asks for the same \(H/L\) saving over the trivial
\(O_\varepsilon(RX^\varepsilon)\) count.

## Why the simpler grouped routes fail

First, the kernel cannot be frozen to an \(n\)-only coefficient on a full
dyadic denominator shell. For \(d,d_0\asymp D\),

\[
\mathcal K((X-n)/d)-\mathcal K((X-n)/d_0)
\ll \frac{L|X-n||d-d_0|}{D^2}.
\]

At \(|X-n|\asymp D/L\) and \(|d-d_0|\asymp D\), this error is order one
per representation. Subdivision fine enough to make the absolute freezing
error target-sized needs at least \(H/L\) cells, consuming exactly the
saving sought.

Second, no uniform character cancellation exists inside one divisor fiber.
Prime powers and semiprimes can leave a single active divisor, while products
of primes \(1\pmod4\) make all divisor signs positive. More sharply, products
\(n=dp\) with both primes \(1\pmod4\), one prime in the actual spatial
profile and the other outside it, give for a suitable center \(X\)

\[
\sum_{|X-n|\asymp D/L}|C_{D,L}(n;X)|
\gg \frac{D/L}{(\log X)^2},
\]

and the squared \(\ell^2\) mass has the same lower scale. Thus post-grouping
triangle, coefficientwise, \(\ell^1\), \(\ell^2\), multiplicativity-only,
and complementary-divisor-only strategies fail by a power at every fixed
interior point below the terminal line.

This is not a lower bound for the total signed M1 block. The remaining
possible cancellation is between distinct nearby products \(n\).

## Positive control for the surviving mechanism

At \(X=y^2\), \(D=y\), consider \(d=y-s\) with even
\(0\le s\ll\sqrt{y/L}\). Then

\[
\frac{X}{d}=y+s+\frac{s^2}{y-s},
\qquad n=y^2-s^2,
\]

and \(\chi_4(y-s)\) alternates when \(s\) increases by two. Abel summation
reduces this actual-profile subtotal from its character-erased size
\(\asymp(D/L)^{1/2}\) to \(O(1)\). This exact control confirms that useful
M1 cancellation can occur across different products while being invisible
to any fiberwise norm estimate.

## Status and next kernel

No new point of \(\mathcal U_1\) is closed in Round 11. The mathematical
advance is sharper: the project now has the exact signed object and has
eliminated several false intermediate targets. The next round must attack
cross-product odd-kernel cancellation, preferably by pairing offsets
\(n=X-t\) and \(n=X+t\), or by an ordered-denominator Abel/large-sieve
estimate that fails for adversarial weights but uses the fixed actual
profile. M9-M1, M9-M2, M9, and the final target remain open.

No numerical experiment was used.
