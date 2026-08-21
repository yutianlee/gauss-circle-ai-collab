# Round 101 synthesis: the full two-adic local operator is unitary

Campaign: m9-m1-full-two-adic-orbit-convolution.

Starting graph SHA-256:
f4a21236d49d03ff141f637eef932fe95868612e8bb885c97c7f1d042b3c0133.

Resulting graph SHA-256:
fbe0e9b9e4db078128f75d97b790dd78a6adc8216c7b0b14c4fad928925637ca.

## Conductor decision

Promote the exact full-\(2^\nu\) actual-row orbit convolution, its guaranteed
twisted-period routing, and its qualified owner map. Reject low-rank and
period-sparsity saving claims. Retain the complete fixed-vector scalar and
every analytic parent as open.

## Exact normal form

For \(M=2^\nu N\), \(N\) odd, a nonempty local mask is the complete odd
orbit \(x=1+2j\), \(j\bmod L\), \(L=2^{\nu-1}\). The literal four-row
coefficient is

\[
 \mathcal C_{2^\nu}(F,G)
 ={1\over L^2}\sum_{k,l\bmod L}e_L(lv)
 \widehat w_{l-k}\widehat F_k\overline{\widehat G_l}.
\]

The normalized matrix \(L^{-1}\widehat w_{l-k}e_L(lv)\) is unitary and
has rank \(L\).

## Full two-power information

The reciprocal phase has guaranteed period

\[
 P_\nu=1\ (\nu\le3),\qquad P_4=2,qquad
 P_\nu=L/8\ (\nu\ge5).
\]

Thus

\[
 w_{j+P_\nu}=e_L(u_2P_\nu)w_j,qquad
 \widehat w_r=0\quad\text{unless}\quad
 r\equiv u_2\pmod{L/P_\nu}.
\]

This is an affine block routing, not a power saving. It also proves why the
Round-100 mod-\(8\) calculation is only the \(\nu=3\) specialization.

## Owners and survivor

The integer \(u=0\) is removed once. Full aligned and reversal terms are
tested using their odd and two-adic return orders; long-return higher
two-part terms can remain hard. Lower period is an owner only when an
accepted Round-89 degree condition applies.

After the successive Round-87--89 owners, the exact residual is one scalar
\(\mathscr S_{2\text{-adic}}(U)\) containing the odd completed trace, all
four actual rows, all class and conductor sums, nonunit \(K\), nonzero
modulus multiples, transitions, stars, aliases, reflections, and zero
extension before absolute value.

## Proof and exponent status

The local operator has norm one, so no \(J^{-1/6}\) gain follows from its
Fourier sparsity. The fixed actual-vector scalar, canonical Gram, GAR,
blockwise M9-M1, M9-M2, endpoint uniformity, M9, and the quarter theorem
remain open.

The strongest certified external exponent remains

\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots,
\]

and the strongest internal uniform theorem remains \(1/3\).
