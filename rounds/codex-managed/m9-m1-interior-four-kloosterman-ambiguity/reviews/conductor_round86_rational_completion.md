# Round 86 conductor rational-completion check

## Exact four-correlation identity

Use the accepted convention

\[
 \mathcal C_{M,K}(a,h)=
 \sum_{\substack{y\bmod M\\(y(y+h),M)=1}}
 e_M\!\left(a(y+h)+K((y+h)^{-1}-y^{-1})\right).
\]

For arbitrary residues \(u,v,h_1,h_2\bmod M\), expand both sums in

\[
 \Sigma_M(u,v;h_1,h_2)
 =\sum_{a\bmod M}\mathcal C(a+u,h_1)
 \overline{\mathcal C(a,h_2)}e_M(-va).
\]

The \(a\)-sum forces

\[
 y+h_1=z+h_2+v.
\]

Writing \(x=y+h_1\), hence
\(y=x-h_1\), \(z+h_2=x-v\), and
\(z=x-v-h_2\), gives the exact one-variable formula

\[
 \boxed{
 \begin{aligned}
 \Sigma_M(u,v;h_1,h_2)
 =M\!\sum_{\substack{x\bmod M\\
 (x(x-h_1)(x-v)(x-v-h_2),M)=1}}
 e_M\!\bigg(&ux+K\big[x^{-1}-(x-h_1)^{-1}\\
 &-(x-v)^{-1}+(x-v-h_2)^{-1}\big]\bigg).
 \end{aligned}}
 \tag{86.C1}
\]

No squarefree or coprime-difference hypothesis was used. At
\(v=0\), \(h_1=h_2=h\), (86.C1) becomes

\[
 M\sum_{\substack{x\bmod M\\(x(x-h),M)=1}}e_M(ux),
\]

which is exactly the already accepted self-return identity after
\(x=y+h\). Thus (86.C1) does not erase the hostile modes.

## Odd-prime nondegeneracy check

Let \(p\nmid K\) be odd. The inner rational phase is

\[
 R(x)=ux+K\left({1\over x}-{1\over x-h_1}
 -{1\over x-v}+{1\over x-v-h_2}\right).
 \tag{86.C2}
\]

Its positive simple poles are the multiset \(\{0,v+h_2\}\), and its
negative simple poles are \(\{h_1,v\}\). Equality of these multisets has
exactly two orientations. Complete cancellation of the rational part
modulo \(p\) occurs precisely when either

\[
 h_1\equiv h_2\equiv0\pmod p,
 \quad\hbox{or}\quad
 v\equiv0\pmod p,\qquad h_1\equiv h_2\pmod p.
 \tag{86.C3}
\]

The first alternative is a locally zero Fourier-mode collision even
though \(h_i\not\equiv0\pmod M\) globally; the second is the ordinary
local self-return. The full phase is constant only when also
\(u\equiv0\pmod p\).

Outside (86.C3), at least one simple pole remains. A nonconstant rational
function with a simple pole cannot be of Artin--Schreier form
\(G^p-G+c\), whose pole orders are divisible by \(p\). The standard
Weil bound therefore gives

\[
 \sum_x^{*}e_p(R(x))\ll p^{1/2},
 \qquad
 \Sigma_p(u,v;h_1,h_2)\ll p^{3/2},
 \tag{86.C4}
\]

with an absolute constant after the finitely many pole collisions are
separated. In the exact self-return case the size can be \(\asymp p^2\).

Consequently, for odd squarefree \(M\) coprime to \(K\), CRT gives the
gcd-sensitive bound

\[
 |\Sigma_M(u,v;h_1,h_2)|
 \ll_\varepsilon M^{3/2+\varepsilon}
 (M,h_1,h_2)^{1/2}(M,v,h_1-h_2)^{1/2}.
 \tag{86.C5}
\]

This deliberately overcounts primes belonging to both exceptional
families, which is harmless for an upper bound.

Primes dividing the fixed \(K\), the 2-adic factor, and powers
\(p^\nu\) require separate local treatment. In particular, (86.C4)
does not imply a uniform arbitrary-composite bound: congruences
\(u\equiv v\equiv0\) and \(h_1\equiv h_2\) to high \(p\)-adic order are
exactly the modes already known to be large.

## Consequence and limitation

Equation (86.C1) is a strict algebraic compression of the four complete
sums to one rational trace sum. It identifies the generic prime-local
square-root regime and the exact exceptional geometry. It does not by
itself estimate the Round-86 object because the completion frequency
\(v\), A-process shift \(u\), two Fourier modes, modulus \(b\), and the
stationary symbol are coupled. Taking (86.C4) pointwise discards both the
required signed averaging and the inherited physical \(Q^{-5/12}\)
factor. Promotion beyond the algebraic identity therefore requires an
aggregate actual-weight estimate, including the prime-power exceptional
set.
