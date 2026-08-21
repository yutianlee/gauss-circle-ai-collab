# Conductor Round 112 normalization and symbol review

## Fixed physical label

Fix one residual smooth physical block
\[
\lambda=(X,D,L,H_D,W_D,v_L,\mathrm{bal},+),
\qquad
H_D=\lfloor DX^{-1/4}\rfloor,
\]
after the terminal, full second-derivative, and TTY owners have declined it.
Put
\[
R=\sqrt X,\qquad K=\frac{XL}{D^2},\qquad M=LK,
\qquad 1\le K/L\le16.
\]
The symbol is not arbitrary. With
\[
q_{\lambda,L}(h)=v_L(h)\Phi\!\left(\frac{h}{H_D+1}\right),
\]
the accepted positive-frequency transform has
\[
a_\lambda(h,k)
=q_{\lambda,L}(h)
 \left(\frac{LK}{hk}\right)^{3/4}
 W_D\!\left(\sqrt{\frac{hX}{4kD^2}}\right).
\tag{112.R1}
\]
Equation (112.R1) is the accepted smooth-transform template once the
physical \(W_D\) and \(v_L\) have been fixed. It does not by itself
enumerate the literal finite atom dictionary, clipped/starred labels, or
support-crossing owner coefficients required by the Round-112 deliverable.
Any bounded smooth subdivision \(\omega\) multiplies (112.R1) by a
prescribed real cutoff \(c_{\lambda,\omega}(h/L,k/K)\), with
\(\sum_\omega c_{\lambda,\omega}=1\) on the block. The \(\omega\)-sum is
therefore internal to one fixed \((D,L)\) block. It must not combine
different physical blocks if the blockwise assembly is to be used.

## Fixed smooth gcd partition

Choose the accepted fixed smooth partition
\[
1=\vartheta_{\mathrm{hi}}(g)+\sum_G\vartheta(g/G)
\]
on the relevant gcd range, with the high part supported on
\(g\gg L^{1/2}\). The high part is absolutely \(O(L^{3/2})\). In a small
shell write
\[
h=gu,\qquad k=gv,\qquad (u,v)=1.
\]
Because a nonzero \(\chi_4(h)\) forces \(h\) odd, both \(g\) and \(u\)
are odd and
\[
\chi_4(gu)=\chi_4(g)\chi_4(u).
\]
For \(t\in\mathbb R\), define the literal real compactly supported profile
\[
F_{\lambda,\omega,u,v,G}(t)
=\vartheta(t)\,
 a_{\lambda,\omega}(Gtu,Gtv).
\tag{112.R2}
\]
Then \(F(g/G)=\vartheta(g/G)a_{\lambda,\omega}(gu,gv)\); all dependence
on \(X,D,L,H_D,W_D,v_L\), the actual Vaaler taper, and the bounded support
subdivision remains visible in (112.R2).

## Quarter-shift Poisson identity

Use
\[
\widehat F(\xi)=\int_{\mathbb R}F(t)e(-t\xi)\,dt,
\qquad
\chi_4(g)=\frac{e(g/4)-e(3g/4)}{2i}.
\]
Poisson summation gives
\[
\sum_gF(g/G)e(\alpha g)
=G\sum_{n\in\mathbb Z}\widehat F(G(n-\alpha)).
\]
Consequently
\[
\begin{aligned}
&\sum_g\chi_4(g)F(g/G)e(Rg\sqrt{uv})\\
&\quad=\frac{G}{2i}\sum_n\left[
\widehat F\!\left(G(n-R\sqrt{uv}-\tfrac14)\right)
-\widehat F\!\left(G(n-R\sqrt{uv}-\tfrac34)\right)
\right].
\end{aligned}
\tag{112.R3}
\]
Thus the exact order is \(1/4\) minus \(3/4\), with the factor \(G/(2i)\).
Any prose saying “\(3/4\) minus \(1/4\)” must be read only as an unordered
description, not as the signed formula.

Define
\[
\begin{aligned}
\mathcal Q_{\lambda,\omega,G}(R)
=\sum_{\substack{(u,v)=1\\u\ {\rm odd}}}\chi_4(u)\sum_n\left[
&\widehat F_{\lambda,\omega,u,v,G}
 \!\left(G(n-R\sqrt{uv}-\tfrac14)\right)\\
-&\widehat F_{\lambda,\omega,u,v,G}
 \!\left(G(n-R\sqrt{uv}-\tfrac34)\right)
\right].
\end{aligned}
\tag{112.R4}
\]
Before subtracting the target-safe square and near-square pieces,
\[
\mathcal T_{\lambda,\mathrm{small}}^+
=\frac1{2i}\sum_{\omega,G}G\mathcal Q_{\lambda,\omega,G}(R).
\tag{112.R5}
\]

## Both frequency signs

The profiles in (112.R1)--(112.R2) are real, and the physical
coefficients satisfy \(\beta_{-h}=\beta_h\). Hence
\[
\mathcal Q_{\lambda,\omega,G}^-
=-\overline{\mathcal Q_{\lambda,\omega,G}^+},
\qquad
\mathcal T_\lambda^-=\overline{\mathcal T_\lambda^+}.
\tag{112.R6}
\]
The minus sign in the packet identity cancels the minus from conjugating
\(1/(2i)\). Thus, if
\(S_\lambda=\sum_{\omega,G}G\mathcal Q_{\lambda,\omega,G}^+\), the
two-sided dual sum is \(\operatorname{Im}S_\lambda\), up to the already
separated physical normalization.
This is not true for a generic complex coefficient. The full physical
block is recovered by the prescribed real-part recombination together
with the conjugate stationary-phase constant. One positive-frequency
packet estimate is therefore sufficient, but a bound on the full real
part cannot be reversed to a bound for the positive packet.

## Exact scope qualification

Equation (112.R5) is exact for the full small-gcd sum. Exact squares and
\(R^{-1}\)-near-squares may be subtracted as prior target-safe owners, but
their subtraction then appears as an \(O_\varepsilon(L^{1+\varepsilon})\)
correction to (112.R5); the smooth Fourier packet itself still represents
the unmasked small-gcd sum. The hard denominator endpoint is absent:
smooth Poisson requires the full \(C_c^\infty\) denominator profile, while
the unique profile containing \(d=\lfloor\sqrt X\rfloor\) remains in the
hard child.

Therefore the normalization and typed profile bridge are certified, but a
standalone literal theorem still requires an explicit coefficientwise atom
list. The symbols \(W_D\), \(v_L\), and \(\omega\) cannot be treated as
their own definitions.
