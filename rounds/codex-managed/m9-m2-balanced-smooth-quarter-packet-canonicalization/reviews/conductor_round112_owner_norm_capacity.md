# Conductor Round 112 owner, norm, and capacity review

## One-count owner equation

For one fixed residual smooth balanced physical block, give priority to:

1. the high-gcd part \(g\gg L^{1/2}\);
2. within the remaining physical sum, exact-square and
   \(R^{-1}\)-near-square terms;
3. the signed full small-gcd packet.

If \(\mathcal S_\lambda\) denotes the square/near-square subtotal after the
high-gcd owner has declined it, the exact accounting is
\[
\mathcal T_{\lambda,\mathrm{bal,res}}^+
=\frac1{2i}\sum_{\omega,G}G\mathcal Q_{\lambda,\omega,G}(R)
-\mathcal S_\lambda,
\qquad
|\mathcal S_\lambda|\ll_\varepsilon L^{1+\varepsilon}.
\tag{112.R7}
\]
Equivalently, one may leave \(\mathcal S_\lambda\) inside the packet and
use it only as diagnostic evidence. It must not be counted positively both
as a separate owner and as an additional packet term.

The smooth transform is
\[
\mathcal B_{\lambda}^+
=-\frac{e(1/8)}{2\pi}X^{1/4}M^{-3/4}
 \mathcal T_{\lambda}^+ +O_\lambda(1).
\tag{112.R8}
\]
The transform error, high-gcd term, and (112.R7) correction are already
target-safe. Hence
\[
\left|\sum_{\omega,G}G\mathcal Q_{\lambda,\omega,G}(R)\right|
\ll_\varepsilon L^{3/2}X^\varepsilon
\tag{112.R9}
\]
is exactly sufficient for this physical block. Logarithmically many
different \((D,L)\) blocks are estimated separately and assembled only
after (112.R9).

## Norm hierarchy

The direct required norm is (112.R9), with one absolute value outside the
entire internal \((\omega,G)\)-sum. Each of the following is stronger:
\[
\sum_{\omega,G}G|\mathcal Q_{\lambda,\omega,G}|
\ll_\varepsilon L^{3/2}X^\varepsilon,
\tag{112.R10}
\]
and the character-preserving Cauchy/Gram estimate
\[
\operatorname{Re}\mathfrak C_\chi(R;L)
\ll_\varepsilon L^2X^\varepsilon.
\tag{112.R11}
\]
There is no implication from (112.R9) back to (112.R10) or (112.R11).
For two shells with \(G_1Q_1=1\) and \(G_2Q_2=-1\), the direct sum vanishes
while the shellwise norm equals \(2\).

An unsigned quarter-resonance count and a product-fibre absolute bound are
also stronger and erase the signed \(1/4-3/4\) mechanism. Cauchy in the
wrong variable erases \(\chi_4\). Arbitrary coefficients are outside the
theorem: the phase-conjugating choice
\(a(h,k)=\chi_4(h)e(-R\sqrt{hk})\) has size \(\asymp L^2\).

## Complementary divisors and parity

For an odd product \(m=hk\),
\[
\chi_4(k)=\chi_4(m)\chi_4(h).
\]
Thus a symmetric complementary-divisor pair cancels only when
\(m\equiv3\pmod4\) and reinforces when \(m\equiv1\pmod4\). If \(m\) is
even, a contributing \(h\) is odd and its complement is even, so the
complementary character is zero. This is not a route to (112.R9).

## Capacity

The coefficient-blind bound for the balanced double sum is \(L^2\).
The accepted two-shift bound gives \(R^{1/2}L^{1/2}\). Against the target
\(L^{3/2}\), the exact current envelope loses
\[
\min\!\left(L^{1/2},\frac{R^{1/2}}L\right).
\tag{112.R12}
\]
The maximum occurs at \(L=R^{1/3}\), where the deficit is
\[
R^{1/6}=X^{1/12}.
\tag{112.R13}
\]
The packet reformulation changes neither exponent nor capacity. Its
smallest genuinely open object is the actual signed outside-absolute
quantity in (112.R9), for one fixed physical balanced block and its fixed
internal partition.

## Downstream scope

Proving (112.R9) uniformly would close only the balanced smooth parent of
the accepted M9-M2 assembly. The hard density-discrepancy parent and the
unbalanced smooth product-phase parent remain independent. Canonicalizing
(112.R9) proves no new \(L\)-range, no improvement of the global exponent,
and no implication for M9-M1.

