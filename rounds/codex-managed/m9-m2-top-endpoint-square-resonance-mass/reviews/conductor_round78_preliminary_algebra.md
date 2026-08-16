# Round 78 conductor preliminary algebra

Campaign: `m9-m2-top-endpoint-square-resonance-mass`  
Graph SHA-256:
`5afbe1bb7b5c5d943be9438ba02bd9ede1ab6735344174b33b4a99c7de7f9123`  
Status: conductor working note, not accepted mathematics.

## Exact square-ray phase

Put

\[
 a=s^2,\qquad b=t^2,\qquad t=s+2u,
 \qquad (s,u)=1,
\]

with odd \(s,t\) and \(1\leq u<s/2\).  For an odd lift \(g\), the
two phases outside and inside the complete Round-77 integral combine
exactly as

\[
 e(-Xu^2/k)e(-2nXu^2/k)=e(-gXu^2/k),
 \qquad g=2n+1.                                      \tag{C78.1}
\]

Write \(A=Ju\).  In the square-root radial coordinate \(\tau=\sqrt v\),
the complete centred phase is

\[
 \psi(k,\tau)=k(\tau-A/k)^2.
\]

It satisfies the exact identity

\[
 k\partial_k e(g\psi)
 =\frac{\tau+A/k}{2}\,\partial_\tau e(g\psi).       \tag{C78.2}
\]

Pointwise differentiation through a physical collar can be large, so
(C78.2) alone does not prove the required bound.  The correct candidate
interface is sampled total variation in \(k\).

## Candidate complete-integral \(k\)-variation lemma

For fixed \((s,u,g)\), let

\[
 K\asymp \frac{Ju}{s},\qquad g t^2\asymp L,
\]

and let \(I_{s,u}=(Ju/s,2Ju/t)\).  The Round-77 factorisation gives

\[
 \mathfrak B^\circ(g,k)
 =g^{-2}E(g)\int q_g(\tau)
 e\!\left(gk(\tau-A/k)^2\right)d\tau,               \tag{C78.3}
\]

where \(q_g\) is a fixed smooth compactly supported symbol for this
\(g\), independent of \(k\).  More explicitly,

\[
 E(g)=\eta_L(gs^2)\overline{\eta_L(gt^2)}
 \Phi\!\left(\frac{gs^2}{H+1}\right)
 \overline{\Phi\!\left(\frac{gt^2}{H+1}\right)},
 \qquad |E(g)|\ll1,                                  \tag{C78.3E}
\]

by the fixed normalized dyadic and Vaaler profiles.  This factor is
independent of \(k\).  Also,

\[
\begin{aligned}
 q_g(\tau)={}&2\tau P_{s^2,t^2}(\tau^2)
 \rho\!\left(\frac{g(\tau^2-t^2/4)}M\right)
 \rho\!\left(\frac{g(s^2-\tau^2)}M\right),\\
 P_{s^2,t^2}(v)={}&
 L^3(st)^{-3/2}v^{-3/2}
 W\!\left(\sqrt{\frac{q_Xs^2}{4v}}\right)
 \overline{W\!\left(\sqrt{\frac{q_Xt^2}{4v}}\right)} .
\end{aligned}                                         \tag{C78.3a}
\]

Its size is \(Q_0\asymp g^3s\), its interior variation is on scale
\(s\), and its two physical collars have width

\[
 w\asymp (gs)^{-1}.
\]

For every fixed \(m\geq1\), the literal profiles give

\[
 \|q_g'\|_1\ll Q_0,\qquad
 \|q_g^{(m)}\|_1\ll_m Q_0w^{1-m},\qquad
 \|q_g^{(m)}\|_\infty\ll_m Q_0w^{-m}.                \tag{C78.3b}
\]

The broad interior pieces are smaller than these collar-dominated
bounds.  These are the only complete-symbol seminorms needed below.

Since \(J\geq L^2\), \(u\geq1\), and \(s\ll\sqrt L\),

\[
 \frac{w^{-2}}{gK}=\frac{gs^2}{K}\asymp\frac{L}{K}\ll1.  \tag{C78.4}
\]

The exact Gaussian Fourier formula, followed by expansion of its
multiplier, gives uniformly for any fixed \(N\)

\[
 \int q_g(\tau)e(gk(\tau-r)^2)d\tau
 =\frac{e(1/8)}{\sqrt{2gk}}
 \sum_{j<N}c_j(gk)^{-j}q_g^{(2j)}(r)+R_N(k,r),       \tag{C78.5}
\]

where \(r=A/k\).  The two smooth collars obey

\[
 \|q_g^{(2j+1)}\|_1\ll Q_0w^{-2j},
\]

and the same Fourier-moment bounds control the value and the
\(r\)-variation of \(R_N\).  Because \(r=A/k\) traverses the physical
interval monotonically only once, (C78.4)--(C78.5) predict

\[
 \boxed{
 \sup_{k\in I_{s,u}}|\mathfrak B^\circ(g,k)|
 +\operatorname{Var}_{k\in I_{s,u}}\mathfrak B^\circ(g,k)
 \ll \sqrt{\frac{gt^2}{K}}.
 }                                                     \tag{C78.6}
\]

This is a statement about the complete smooth-collar integral.  It is
not a pointwise estimate for \(k\partial_k\mathfrak B^\circ\), and it
would be false with an unresolved sharp endpoint in place of each fixed
collar.  The independent reports must certify the remainder and sampled
endpoint terms in (C78.5) before (C78.6) can be accepted.

## Reciprocal-mode summation

For the outer phase

\[
 f(k)=-\frac{gXu^2}{k},
\]

one has throughout \(I_{s,u}\)

\[
 |f''(k)|\asymp \lambda
 :=\frac{gs^3}{Ju},
 \qquad
 \sqrt\lambda\asymp\sqrt{\frac{gt^2}{K}}.           \tag{C78.7}
\]

Moreover \(\lambda\ll1\), and the interval length is

\[
 M\asymp \frac{Ju(2s-t)}{st}.
\]

Weighted van der Corput using (C78.6) would therefore give

\[
 \left|\sum_{k\in I_{s,u}\cap\mathbb Z}
 \mathfrak B^\circ(g,k)e(-gXu^2/k)\right|
 \ll M\lambda+1
 \ll gs(2s-t)+1
 \ll L+1.                                            \tag{C78.8}
\]

Empty intervals contribute zero and one-point intervals are covered by
the value term in (C78.6).

Finally, the number of admissible primitive square lifts satisfies

\[
 \sum_{s\ll\sqrt L}
 \sum_{1\leq u<s/2}\#\mathcal G_{s^2,(s+2u)^2}
 \ll L\sum_{s\ll\sqrt L}\frac1s
 \ll L\log(2+L).                                    \tag{C78.9}
\]

Thus (C78.6) would imply the exact signed square-family bound

\[
 |\mathcal S_L^\square(X)|
 \ll L^2\log(2+L)
 \ll_\varepsilon L^2X^\varepsilon.                 \tag{C78.10}
\]

The absolute Abel majorant remains false: the fixed \((s,t)=(9,11)\)
ray along fourth powers already has mass \(\gg X^{1/4}\) at fixed
populated \(L\).  Hence a proof of (C78.10) must retain the signed
reciprocal-mode phase.

## Preliminary verdict

The square-family target reduces to the complete-integral sampled
\(k\)-variation lemma (C78.6).  Its scale, reciprocal curvature, and
aggregate arithmetic are exact.  The promotion gate is a uniform proof
of (C78.6) through both smooth collar crossings with the literal
Round-77 symbol.  No generic nonsquare energy, full \(M9\!-\!M2\),
\(M9\), endpoint-uniformity, or exponent conclusion follows from this
working note.
