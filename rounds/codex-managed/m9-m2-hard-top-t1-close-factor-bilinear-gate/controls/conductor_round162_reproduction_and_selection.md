# Round 162 conductor reproduction and candidate selection

## Selection

Selected candidate:

`candidates/conductor_round162_t1_character_poisson_collar_obstruction.md`.

All three reports independently support the exact projector opening,
character transfer, rank-one product geometry, rescaled collar, and
missing-power conclusion.  The source report additionally audits named
interfaces.  The discovery report's blanket target-safe hard-edge claim
is not selected because the blind report did not receive enough literal
profile data to certify it.  Literal boundary families remain in the
first open signed aggregate.

## Exact algebra reproduction

Use

\[
 \chi_4(n)=\frac{e(n/4)-e(-n/4)}{2i},\qquad
 \widehat g(\xi)=\int g(x)e(-\xi x)\,dx.
\]

For the sign (\sigma\in\{1,-1\}), Poisson gives frequency
(k-\sigma/4).  Set (s=4k-\sigma).  If (\sigma=1), then
(s\equiv3\pmod4); if (\sigma=-1), then
(s\equiv1\pmod4).  In both cases
(\sigma=-\chi_4(s)), and

\[
 \frac{1}{2i}\sigma=-\frac{\chi_4(s)}{2i}
 =\frac i2\chi_4(s).
\]

This reproduces the sign in the exact character-Poisson formula.

For (Q=[a^2,c]), (R=[b^2,c]), (d_1=Qm), and (d_2=Rn), the
(m)-phase is

\[
 F(m)=J\sqrt{Qd_2m}-sm/4.
\]

Solving (F'(m)=0) gives

\[
 m_s=4XQd_2/s^2,qquad d_1^*=4XQ^2d_2/s^2,qquad
 F(m_s)=XQd_2/s.
\]

Also

\[
 F''(m_s)=-\frac{s^3}{32XQd_2},
\]

and direct exponent collection gives

\[
 \left(\frac{L^2}{d_1^*d_2}\right)^{3/4}
 |F''(m_s)|^{-1/2}
 =\frac{2L^{3/2}X^{-1/4}}{Qd_2}
 =\frac{2L^{3/2}J^{-1/2}}{Qd_2}.
\]

The cone (1\le d_1^*/d_2\le4) is equivalent to
(JQ\le s\le2JQ), and

\[
 \sqrt{q_Xd_1^*/(4d_2)}=XQ/(ys).
\]

## Rank and collar reproduction

For (f(x,z)=J\sqrt{xz}), direct multiplication gives

\[
 f_{xx}f_{zz}-f_{xz}^2=0,
\]

and

\[
 \operatorname{Hess}f\,(x,z)^T=0.
\]

With (u=Qm=tw), (v=Rn=t/w), the dual phase is

\[
 t\Psi(w),\qquad
 \Psi(w)=J-\frac{s}{4Q}w-\frac{\ell}{Rw}.
\]

The angular saddle has

\[
 w_0^2=\frac{4Q\ell}{Rs},\qquad
 \Psi(w_0)=J-\sqrt{\frac{s\ell}{QR}}.
\]

Thus exact resonance is (s\ell=XQR).  Since the radial physical
length is (L), the central Fourier window is

\[
 \left|J-\sqrt{\frac{s\ell}{QR}}\right|\ll L^{-1}.
\]

On (s\ell\asymp XQR), rationalizing the square roots gives

\[
 |s\ell-XQR|\ll QRJ/L.
\]

There are at most

\[
 O_\varepsilon((QRJ/L+1)(XQR)^\varepsilon)
\]

factor pairs, by counting the possible integers (s\ell) and applying
the divisor bound.  The transverse scale is
(L^{3/2}/(QR\sqrt J)), so the (QR)-powers cancel:

\[
 \frac{QRJ}{L}\frac{L^{3/2}}{QR\sqrt J}
 =\sqrt{JL}.
\]

Since (H=\sqrt J+O(1)), this is
(L^{3/2}(H/L+O(L^{-1}))).

## Involution and differencing controls

For (h(s)=\widehat g(s/4)), substitution in its Fourier transform gives

\[
 \widehat h(\xi)=4g(-4\xi).
\]

The two character factors contribute ((i/2)^2=-1/4), the Fourier
scaling contributes (4), and oddness of (\chi_4) changes the reflected
sum by another (-1).  The product is (1).  Thus the exact transform
is involutive.

For odd (d), periodicity modulo four gives

\[
 \chi_4(d+2h)\chi_4(d)=(-1)^h.
\]

Hence the character is constant across each standard nonzero
autocorrelation and is lost after a positive norm.

## Scope checks

| Check | Outcome |
|---|---|
| Literal orientation and even (d_2) | GREEN.  No swap; only the first leg is forced odd. |
| Character retained before norms | GREEN.  The exact dual coefficient is (i\chi_4(s)/2). |
| Rank-one geometry | GREEN.  No Hessian determinant is divided out. |
| Collar width and positive capacity | GREEN for a compact smooth interior cell. |
| Literal hard edges | OPEN in the selected kernel; no blanket target-safe claim promoted. |
| Möbius aggregate | OPEN; fixed-opening (QR)-decay is repaid by collar width. |
| Physical lower bound | REJECTED; every large quantity is a route capacity. |
| Downstream transfer | REJECTED; all other few-point channels and parents remain open. |

No numerical experiment was used.  The failed optional symbolic check was
not used as evidence; every displayed identity above was reproduced
algebraically.
