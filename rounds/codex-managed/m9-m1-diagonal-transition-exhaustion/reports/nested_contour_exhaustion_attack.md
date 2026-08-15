# Nested contour exhaustion attack

## 1. Result

Take
\[
 S_X(U,V)=(X+U+V+2)^4. \tag{E}
\]
This dominates \(U+V\), separates both radial horizontal sides from the
planes \(\Im w=\pm\Im(u+v)/2\), and removes radial stationary points.
Nevertheless it does **not** remove the exact horizontal sides. The sharp
radial cutoff gives a leading endpoint term of order \(S^{-1}\), while the
degree-two functional equation grows like \(S^{1-2\sigma}\) at the forced
left edge \(\lambda=1-c'<0\). Their product has capacity
\(S^{-2\lambda}\), which grows. Thus nested height alone cannot justify
side deletion; faster nesting makes the absolute obstruction worse.

The terminal vertical segment has a second independent obstruction. Its
single-transition traces remain
\[
 t=\pm(\Im u+\Im v)/2+O(1)
\]
for every large symmetric Perron height. One gamma ratio is bounded-order,
the other grows polynomially, and the outside \(1/u\) measure is not
absolutely integrable. No target-sized sector is closed.

## 2. Exact statement and hypotheses

Use the exact Round-19 finite identity. Write
\(u=a+i\tau\), \(v=b+i\nu\), \(z=u+v=\zeta+i\eta\), and
\(w=\sigma+it\), with \(|\tau|\le U\), \(|\nu|\le V\). Shift \(w\) from
\(\Re w=c\) to \(\lambda=1-c'\), where
\(c'>1+\zeta/2\). The upper radial side is
\[
 \mathfrak B^+_{U,V,S}=\sum_j\frac1{(2\pi i)^3}
 \int_{\Gamma_{a,U}}\int_{\Gamma_{b,V}}\int_\lambda^c
 \mathcal A_j(u,v)G_v(\sigma+iS)F_z(\sigma+iS)
 \,d\sigma\,dv\,du, \tag{H}
\]
and similarly below. The \(u,v\) lines are not moved, so their residues
and horizontal sides are not silently introduced. The top line stays the
symmetric segment \([-U,U]\).

## 3. Proof or derivation

Put \(y=\log x\). For
\[
 G_v(w)=\int_1^{N_X}x^{w-7/4-v/2}e(\sqrt{Xx})\,dx,
\]
the upper-side phase derivative is
\[
 \Psi_+'(y)=S-\nu/2+\pi\sqrt X\,e^{y/2},
\]
and the lower one is
\(\Psi_-'(y)=-S-\nu/2+\pi\sqrt X e^{y/2}\).
Choice (E) makes both \(\asymp S\). Integration by parts gives
\[
 G_v(\sigma\pm iS)=
 \left[\frac{e^{(\sigma-3/4-b/2)y}e^{i\Psi_\pm(y)}}
 {i\Psi_\pm'(y)}\right]_{0}^{\log N_X}
+O_{\sigma,b}\!\left(\frac{N_X^{O(1)}(1+X+V)}{S^2}\right). \tag{1}
\]
The endpoint star merely halves the boundary value. Repetition yields a
boundary asymptotic series beginning with \(S^{-1}\), not rapid decay.

Since \(S\gg U+V\), uniform Stirling applies to \(F_z(\sigma+iS)\).
At \(\sigma=\lambda\), the reflected series
\(F_{-z}(c'-iS)\) is absolutely convergent and
\[
 |F_z(\lambda+iS)|\ll S^{1-2\lambda}. \tag{2}
\]
The exponent is exact for the gamma quotient. Choosing \(c'\) sufficiently
large makes the tail of the dual Dirichlet series \(<1/2\), so its first
term also gives a uniform lower bound; because \(\lambda<0\), the
\(x=1\) endpoint dominates (1). Hence at \(\tau=\nu=0\)
\[
 |G_b(\lambda+iS)F_\zeta(\lambda+iS)|
 \asymp S^{-2\lambda}. \tag{3}
\]
Thus uniform pointwise decay of the side integrand is false. Cancellation
after the \(\sigma,u,v\) integrations is conceivable, but it would be a
new signed horizontal-side theorem, not contour exhaustion.

Now use terminal \(s=c'+it\) and diagonal variables
\[
 \alpha=t+\eta/2,\qquad \beta=t-\eta/2.
\]
The exact quotient factors into
\[
\frac{\Gamma((c'-\zeta/2+i\beta)/2)}
{\Gamma((1-c'+\zeta/2-i\beta)/2)}
\times
\frac{\Gamma((1+c'+\zeta/2+i\alpha)/2)}
{\Gamma((2-c'-\zeta/2-i\alpha)/2)}, \tag{4}
\]
times the elementary \(2,\pi\) powers. If \(|\beta|\le1\) and
\(|\alpha|\gg1\), its magnitude is
\[
 \asymp (1+|\alpha|)^{c'-1/2+\zeta/2}; \tag{5}
\]
the other trace has exponent \(c'-1/2-\zeta/2\). On \(\Re s=c'\),
\(G_v(1-s)\) and the dual \(m\)-series are absolutely convergent.
Along the top trace, \(|\eta|\asymp|\tau|\); multiplication by
\(\widehat W_+(a+i\tau)\asymp1/\tau\) leaves raw size
\[
 |\tau|^{c'-3/2+\zeta/2}, \tag{6}
\]
which is not integrable for the required \(c'>1+\zeta/2\).
Only a signed vector-valued Hilbert estimate could pass the symmetric
limit. Increasing \(S\) never changes (5)--(6), because the traces remain
inside \([-S,S]\).

Outside \(v\)-tails retain the rapid decay of \(\widehat\phi\), and smooth
interior \(u\)-profiles retain rapid Mellin decay. The obstruction is the
hard top \(1/u\) trace. Moving that line would add outside horizontal sides
whose vanishing is likewise not implied by (6); keeping it fixed preserves
the exact Perron convention.

## 4. First doubtful or unproved step

The first missing step is a signed estimate for (H) that cancels its two
radial endpoint expansions. Even after such a renormalization, the
diagonal vector-Hilbert traces (5)--(6) remain unproved.

## 5. Required control test and outcome

Under (E), \(S\pm\eta/2\asymp S\): transition separation on the radial
sides passes. Equation (3) disproves uniform pointwise side decay.
Setting \(t=\eta/2\) gives \(\beta=0\) at arbitrarily large \(\tau\),
showing that the terminal trace never enters the outer regime. No
numerical test was used.

## 6. Dependencies and exact artifacts used

Used only the authorized Round-20 packet: protocol, graph, active campaign,
Round-19 synthesis/reports, Round-15 formulas, and the assigned brief. No
external theorem or web source was used.

## 7. Recommended state effect

Promote (E), the sharp radial-endpoint exhaustion obstruction (1)--(3),
and the exact diagonal growth laws (5)--(6). Retain as the smallest
survivor the radial horizontal-side functional together with both
single-transition vector-Hilbert traces, the symmetric top measure, and
all listed residues. Do not promote side removal, a target sector, GAR,
M9-M1, or M9.
