# Round 143 statement-only packet

Campaign: `m9-m2-unbalanced-level-four-kuznetsov-matrix-gate`

This packet is the complete mathematical context for the blind task. Do
not consult strategy files, the proof graph, earlier campaign reports, or
the other Round-143 reports.

## 1. Parameters and literal scalar

Let

\[
 X=N_0+\xi,\qquad N_0=\lfloor X\rfloor,\qquad 0\le \xi<1,
\]

and put

\[
 D=X^\delta,\qquad L=X^\ell,\qquad R=\frac XD,
 \qquad K=\frac{XL}{D^2},\qquad
 \Delta=\frac DL=\frac RK,
\]

in the strict range

\[
 \frac14<\delta-\ell<\frac12,
 \qquad \frac14\le\delta<\frac12,
 \qquad \ell\ge0.
\]

On one fixed flat smooth cell consider

\[
 \mathscr R_{D,L}(X)=
 \sum_{\substack{r\asymp R\\r\ {\rm odd}}}
 \chi_4(r)W\!\left(\frac{X}{rD}\right)
 \sum_{k\asymp K}
 \frac{q_L(4Xk/r^2)}{k}e(Xk/r),
 \tag{143.B1}
\]

where \(e(z)=e^{2\pi iz}\), \(W\) and the normalized version of
\(q_L\) are smooth compactly supported profiles with uniformly bounded
logarithmic derivatives, and every summand outside its literal support is
zero. The desired bound is

\[
 |\mathscr R_{D,L}(X)|\ll_\varepsilon X^{1/4+\varepsilon}.
 \tag{143.B2}
\]

The currently available coefficient/curvature envelope is

\[
 X^\varepsilon\min\!\left(\Delta,
 \sqrt{\frac{XL}{D}}+\sqrt{\frac{X}{LD}}\right),
 \tag{143.B3}
\]

which is larger than \(X^{1/4}\) on the open strict range relevant here.

## 2. Exact gcd and inverse-first identities

Write \(r=gn\), \(k=gj\), with \(g,n\) odd and \((j,n)=1\). Then

\[
 \mathscr R_{D,L}(X)=
 \sum_{\substack{g,n\ {\rm odd}\\gn\asymp R}}
 \chi_4(g)\chi_4(n)W\!\left(\frac{X}{gnD}\right)
 \sum_{\substack{j\ge1\\(j,n)=1}}
 b_{g,n}(j)e(N_0j/n),
 \tag{143.B4}
\]

where

\[
 b_{g,n}(j)=
 \frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n),
 \qquad n\asymp R/g,\quad j\asymp K/g.
 \tag{143.B5}
\]

For a unit \(m\pmod n\), let \(\overline m_n\) be its inverse and set

\[
 \gamma_{g,n}(m)=b_{g,n}(\overline m_n),
 \qquad
 \widehat\gamma_{g,n}(h)=\frac1n
 \sum_{m\bmod n}\gamma_{g,n}(m)e(-hm/n),
 \tag{143.B6}
\]

with \(\gamma=0\) on nonunits or when the inverse leaves the support in
(143.B5). Fourier inversion gives the exact row identity

\[
 \sum_{m\bmod n}^{*}\gamma_{g,n}(m)e(N_0\overline m_n/n)
 =\sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n),
 \tag{143.B7}
\]

where

\[
 S(a,h;n)=\sum_{m\bmod n}^{*}
 e\!\left(\frac{a\overline m_n+hm}{n}\right).
 \tag{143.B8}
\]

The exact Parseval information is only

\[
 \sum_{h\bmod n}|\widehat\gamma_{g,n}(h)|^2
 \ll \frac1{RK}.
 \tag{143.B9}
\]

The dependence of \(\widehat\gamma_{g,n}(h)\) on both \(n\) and \(h\)
is literal and may not be replaced by an independent coefficient.

## 3. Frozen question

Decide whether the complete insertion of (143.B7) into (143.B4) can be
represented by fixed-level generalized Kloosterman sums and estimated by
a Kuznetsov trace formula or spectral large sieve while retaining
\(\chi_4(n)\) before every positive modulus norm.

You must derive the exact level, cusp pair, allowed modulus progression,
root-of-unity factors, Kloosterman normalization, test function, Bessel
transforms, and all holomorphic, Maass, Eisenstein, exceptional, and
continuous-spectrum terms. You must also price any separation or
vector-valued treatment of \(\widehat\gamma_{g,n}(h)\), restore every
\(g\)-stratum and the real-centre factor, and compute the full
\(D,L,R,K,\Delta\) power ledger.

The outcome must be exactly one of:

1. a proof of (143.B2);
2. a strictly smaller owner-complete spectral survivor with its complement
   bounded by (143.B2); or
3. a rigorous first obstruction at the level/cusp, coefficient-matrix,
   trace-formula, transform-return, or capacity seam.

Smooth-first Fourier completion is allowed as a hostile control, but a
Ramanujan/additive return of size \(\Delta X^\varepsilon\), or an exact
return to (143.B1), is not a saving. Numerical evidence cannot certify an
asymptotic estimate.

## 4. Scope

Only the flat smooth scalar (143.B1) is in scope. Sharp, clipped, starred,
hard, transition, balanced, top-endpoint, complete-M2, endpoint-uniform,
and global circle-problem owners are excluded.

Your report must contain the seven sections required by `protocol.md` and
must identify its first doubtful or unproved step even if the result is a
no-go theorem.
