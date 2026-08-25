# Primitive residue Fourier kernel on one determinant lift

Campaign: `gc-w7-16-top-shell-determinant-residue-zero-mode-gate`

Status: finite internal support-mask kernel; its use in the weighted physical
scalar requires a separate post-reassembly extension, interlacing, and envelope
estimate.

Write \(e(x)=e^{2\pi i x}\). Fix a primitive outer ray \((a,b)\), a
physical increment \(p\), and put \(m=a+p\). On this lift

\[
n=aq-bp,
\qquad q={n+bp\over a}.
\]

## M1

Let \(M\) be the odd part of \(|m|\). The stripped primitive M1
support-character mask is

\[
w_{1,m}(q)=\chi _4(b+q)\mathbf 1_{(M,b+q)=1},
\]

with minimal period \(4\operatorname{rad}(M)\) and valid completion modulus
\(4M\). For the normalized transform

\[
\widehat w_{1,m}(k)={1\over4M}\sum_{q\bmod4M}
w_{1,m}(q)e\!\left(-{kq\over4M}\right),
\]

one has

\[
\widehat w_{1,m}(k)=
{e(kb/(4M))\over4M}\,G_{4,M}(k)c_M(k),
\tag{K1}
\]

where \(c_M\) is the Ramanujan sum and

\[
G_{4,M}(k)=\sum_{u\bmod4}\chi _4(u)
e\!\left(-{k\overline M^{(4)}u\over4}\right).
\]

Here \(G_{4,M}(k)=0\) for even \(k\), while
\(|G_{4,M}(k)|=2\) for odd \(k\). Consequently

\[
|\widehat w_{1,m}(M)|=|\widehat w_{1,m}(3M)|
={\varphi(M)\over2M}.
\tag{K2}
\]

Proof: shift \(x=b+q\), then use the Chinese remainder theorem modulo
\(4M\). The mod-four factor is \(G_{4,M}(k)\). The other factor is
\(c_M(k\overline4^{(M)})=c_M(k)\), since multiplication by a unit
preserves a Ramanujan sum. Formula (K2) follows from
\(c_M(M)=c_M(3M)=\varphi(M)\).

The zero mode vanishes, but the two quarter modes are of natural density.
Under the determinant substitution they contribute, up to constants,

\[
e\!\left({n\over4a}\right),
\qquad e\!\left({3n\over4a}\right).
\]

If the progression is extended by zero to all integers \(n\), a valid
completion period is \(4|a|M\), not generally \(4|a|\); the minimal period
uses \(\operatorname{rad}(M)\).

## M2

For an active odd \(m\), the stripped primitive M2 support-character mask is

\[
w_{2,m}(q)=\epsilon_{\rm sgn}\chi _4(|m|)
\mathbf 1_{(|m|,b+q)=1}.
\]

It has minimal period \(\operatorname{rad}(|m|)\), admits the valid completion
modulus \(|m|\), and

\[
\widehat w_{2,m}(k)=
{\epsilon_{\rm sgn}\chi _4(|m|)\over|m|}
e\!\left({kb\over|m|}\right)c_{|m|}(k).
\tag{K3}
\]

In particular,

\[
\widehat w_{2,m}(0)=
\epsilon_{\rm sgn}\chi _4(|m|){\varphi(|m|)\over|m|},
\tag{K4}
\]

so the fixed-lift \(q\)-arithmetic zero coefficient is generically nonzero.
It is not the determinant point \(n=0\). A valid completion period after zero
extension to all \(n\) is \(|a||m|\).

## Completion cost and scope

The elementary bound

\[
\sum_{k\bmod R}|c_R(k)|\le R\tau(R)
\]

shows that the normalized Fourier \(\ell^1\) cost in (K1) and (K3) is
\(O(\tau(|m|))\). Thus the fixed-lift expansion costs no power of \(Y\),
but it gives no saving: (K2) and (K4) leave natural modes.

The physical top-shell scalar interlaces \(m=a+p\), its primitive modulus,
the lift owner, thresholds, reciprocal phase, and outer ray. Its weighted
Möbius atoms also retain \(\rho\)-dependent profiles, stars, and owners, so a
bare support identity does not factor the full coefficient. This kernel does
not assert a common modulus for that interlaced weight, a low-cost BV envelope,
a Salié sum, a signed scalar estimate, or a family lower bound.
