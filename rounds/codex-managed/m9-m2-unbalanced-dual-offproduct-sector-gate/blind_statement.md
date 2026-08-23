# Blind statement: complete dual off-product sector gate

Round: 125

This file is statement-only input.  Do not consult any proof graph,
strategy memo, prior nonblind round, sibling report, or conductor
derivation.

Let \(e(x)=e^{2\pi i x}\), let \(M\asymp X\) be an integer, and put

$$
 D=X^\delta,\qquad L=X^\ell,\qquad K=XL/D^2,\qquad
 H=\left\lceil X^{1/2}/D\right\rceil,
$$

where

$$
 \frac14\le\delta<\frac12,\qquad
 0\le\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463.
$$

Thus \(K\asymp LH^2\), and

$$
 Q:=\frac{D^2}{L\sqrt X}\longrightarrow\infty.
$$

All amplitudes below are the literal fixed smooth profiles from one
flat-smooth strict-UNBAL packet.  They are uniformly smooth after scaling,
compactly supported on positive fixed interiors, and extended by zero
before every block shift.  Define

$$
 \mathcal A_{p,k}
 =W\!\left(\frac{X}{2D}\sqrt{\frac p{Mk}}\right)q_L((X/M)p),
$$

and, for positive odd \(p\),

$$
 b_{p,k}=e(-1/8)M^{1/4}k^{-3/4}p^{-3/4}
 \mathcal A_{p,k}e(\sqrt{Mpk}).
\tag{125.B1}
$$

Put

$$
 \widetilde A(k)=\sum_{p>0\atop p\text{ odd}}\chi_4(p)b_{p,k},
 \qquad
 C_H=\frac{J+H-1}{H^2},\quad J\asymp K.
\tag{125.B2}
$$

The accepted unmasked stationary transform says that the original exact
shifted square differs by \(O(1)\) from

$$
 \widetilde{\mathcal F}_{M,H}
 =C_H\sum_n\left|\sum_{a=0}^{H-1}\widetilde A(n+a)\right|^2.
\tag{125.B3}
$$

Expand (125.B3) into

$$
 \mathcal D_0=C_HH\sum_{p,k}|b_{p,k}|^2,
\tag{125.B4}
$$

$$
 \mathcal S_{\rm eq}^{\ne0}
 =C_H\sum_p\sum_{0<|h|<H}(H-|h|)
 \sum_k b_{p,k+h}\overline{b_{p,k}},
\tag{125.B5}
$$

and

$$
 \mathcal S_{\rm neq}
 =C_H\sum_{p\ne q}\chi_4(p)\chi_4(q)
 \sum_{|h|<H}(H-|h|)
 \sum_k b_{p,k+h}\overline{b_{q,k}}.
\tag{125.B6}
$$

The exact identities are

$$
 \widetilde{\mathcal F}_{M,H}
 =\mathcal D_0+\mathcal S_{\rm eq}^{\ne0}+\mathcal S_{\rm neq},
\tag{125.B7}
$$

and

$$
 \mathcal D_0+\mathcal S_{\rm eq}^{\ne0}
 =C_H\sum_p\sum_n
 \left|\sum_{a=0}^{H-1}b_{p,n+a}\right|^2\ge0.
\tag{125.B8}
$$

It is accepted that \(\mathcal D_0\ll X^{1/2}\), and that the original
physical survivor is target-equivalent, modulo already-safe terms, to

$$
 \mathcal S_{\rm off}
 :=\mathcal S_{\rm eq}^{\ne0}+\mathcal S_{\rm neq}.
\tag{125.B9}
$$

The required estimate is

$$
 \boxed{\mathcal S_{\rm off}\ll_\varepsilon X^{1/2+\varepsilon}.}
\tag{125.B10}
$$

The correlation phase is

$$
 \Theta_{p,q,h}(k)
 =\sqrt M\{\sqrt{p(k+h)}-\sqrt{qk}\}.
\tag{125.B11}
$$

For \(p=q,h\ne0\),

$$
 \partial_k\Theta_{p,p,h}
 =-\frac{\sqrt{Mp}\,h}
 {2\sqrt k\sqrt{k+h}(\sqrt k+\sqrt{k+h})}.
\tag{125.B12}
$$

The exact product defect and gradient numerator are distinct:

$$
 \mathcal N=p(k+h)-qk,\qquad
 \mathcal G=pk-q(k+h)=\mathcal N-(p+q)h.
\tag{125.B13}
$$

A later joint stationary transform returns the primal reciprocal phase;
its unsigned fixed-interior ledgers are nominally \(D^2\) and \(D^2/L\),
with \(D^2/L=Q\sqrt X\).  These are diagnostics, not lower bounds.

Independently derive and prove one of the following:

1. (125.B10);
2. a complete target-safe equal-mode-shifted or unequal-mode sector and a
   lawful estimate for the other;
3. a fixed-power inverse theorem strictly smaller than (125.B9); or
4. the smallest rigorous no-go showing why the proposed sectorwise
   inequalities are overstrong, while identifying the exact complete
   signed survivor.

Do not infer cancellation from conjugate pairing.  Do not replace the
actual \(\chi_4\), moving profiles, Fejer weight, or zero extension by a
rectangular coefficient model.  Do not call (125.B8) target-equivalent to
(125.B10) without proving both directions.  A second Poisson or stationary
inversion is not a saving.  An unsigned capacity is neither an upper nor a
lower bound for (125.B9).
