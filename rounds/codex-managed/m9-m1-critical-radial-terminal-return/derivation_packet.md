# Round 60 derivation packet: the full critical radial sector

This packet freezes a fixed-relative-width sector of the accepted global
angular recombination.  It asserts no estimate beyond the already proved
terminal M1 theorem and the accepted interior/top transforms.

## 1. Exact target

Put

\[
 R=X^{1/4},\qquad Y=R^2=\sqrt X.
\]

Let \(V\in C_c^\infty((c,C))\), where
\(0<c<C<16\) are fixed.  The profile support and the positive lower
radial cutoff force \(h\gg H_j\), while the pre-existing exact factor
\(\mathbf1_{h\le H_j}\) owns the upper terminal edge.  The terminal
theorem permits the resulting endpoint jump at \(h=H_j\); no strict upper
margin is required.  With the accepted Round-14 coefficient

\[
 \mathcal C_X^*(n)=
 \sum_{\substack{h\mid n\\q=n/h\ {m odd}}}
 \chi_4(q)\Omega_X^*(n,h),
\]

\[
 \Omega_X^*(n,h)=\sum_j\mathbf1_{h\le H_j}
 \Phi\!\left({h\over H_j+1}\right)
 \left[w_j\!\left(2h\sqrt{X/n}\right)\right]^*,
\]

define

\[
 \mathcal G_V(X)=
 \sum_{n\le16Y}V(n/Y)\mathcal C_X^*(n)n^{-3/4}
 e(\sqrt{Xn}).
\tag{60.1}
\]

The frozen target needed by GAR is

\[
 \boxed{\operatorname{Re}\{e(1/8)\mathcal G_V(X)\}
 \ll_{\varepsilon,V}X^\varepsilon.}
\tag{60.2}
\]

The modulus bound is stronger and must not be inferred from this one fixed
projection without a separate complex positive-frequency argument.

This is a smooth critical radial sector only.  A finite smooth partition
would cover \(n\asymp Y\), but no lower radial range is claimed.

## 2. Candidate physical antecedent

For \(D_j=2^{-j}\lfloor\sqrt X\rfloor\) and
\(H_j=\lfloor D_j/R\rfloor\), the stationary relation is

\[
 n={4Xh^2\over d^2}.
\tag{60.3}
\]

Therefore introduce

\[
 \mathcal B_{j,V}=
 \sum_{h\ge1}\eta_j(h)\mathbf1_{h\le H_j}
 {\Phi(h/(H_j+1))\over h}
 \sum_d\chi_4(d)w_j(d)
 V\!\left({4Xh^2\over d^2Y}\right)e(hX/d),
\tag{60.4}
\]

where \(\eta_j\) is a fixed-normalized-BV lower terminal cutoff equal to
one on every \(h\) that can occur when the \(d\)-profile, \(V\), and
\(h\le H_j\) are all nonzero.  The exact upper cutoff is
\(\mathbf1_{h\le H_j}\), whose endpoint jump is retained.  Prove that
such \(\eta_j\) exists uniformly; treat bounded \(H_j\) separately if
needed.  The intended support calculation is

\[
 V(4R^2h^2/d^2)w_j(d)\ne0
 \quad\Longrightarrow\quad h\asymp d/R\asymp D_j/R\asymp H_j.
\tag{60.5}
\]

## 3. Exact Mellin separation to verify

Use

\[
 \widehat V(t)=\int_0^\infty V(z)z^{-it}{dz\over z},\qquad
 V(z)={1\over2\pi}\int_{\mathbb R}\widehat V(t)z^{it}\,dt.
\tag{60.6}
\]

Then (60.4) should become

\[
 {1\over2\pi}\int_{\mathbb R}\widehat V(t)
 \left({4X\over Y}\right)^{it}
 \sum_h u_{j,t}(h)
 \sum_d\chi_4(d)w_j(d)d^{-2it}e(hX/d)\,dt,
\tag{60.7}
\]

with

\[
 u_{j,t}(h)=\eta_j(h)\mathbf1_{h\le H_j}
 {\Phi(h/(H_j+1))\over h}h^{2it}.
\tag{60.8}
\]

The terminal interface requires

\[
 \|u_{j,t}\|_\infty+\sum_h|\Delta u_{j,t}(h)|
 \ll {1+|t|\over H_j},
\tag{60.9}
\]

while \(|w_j(d)d^{-2it}|\ll1\).  If (60.9) holds, the accepted
frequency-first divisor theorem gives

\[
 \mathcal B_{j,V}\ll_{\varepsilon,V}X^\varepsilon
 (1+D_j/H_j)\ll X^\varepsilon R.
\tag{60.10}
\]

The \(t\)-integration is allowed only after proving the needed weighted
\(L^1\) moments of \(\widehat V\).  Summing the active \(j\)'s may cost
only \(X^\varepsilon\).

## 4. Transform identity and normalization

For each Mellin mode, the stationary denominator is

\[
 d_*=2\sqrt{hX/q},\qquad n=hq.
\]

The mode must satisfy the exact identity

\[
 \left({4X\over Y}\right)^{it}h^{2it}d_*^{-2it}
 =\left({hq\over Y}\right)^{it}=\left({n\over Y}\right)^{it}.
\tag{60.11}
\]

After Mellin inversion, frequency-shell recombination, and pairing both
frequency signs, the expected relation is

\[
 \sum_j\mathcal M_{1,j,V}(X)
 =-{4\over\pi}R\operatorname{Re}\{e(1/8)\mathcal G_V(X)\}
 +\mathcal E_V(X),
\tag{60.12}
\]

with \(\mathcal E_V(X)\ll_{\varepsilon,V}R X^\varepsilon\), preferably
polylogarithmic.  A modulus bound for the complex sector requires applying
the same argument to a fixed phase rotation or proving the complex
positive-frequency version; do not silently infer it from one real part.

## 5. Mandatory seams

1. The terminal cutoff \(\eta_j\) may be inserted only if it is exactly
   one on every stationary contribution to (60.1).
2. The denominator mode \(d^{-2it}\) is bounded, but the B-process error
   depends on its derivatives; integrate the resulting polynomial
   \(t\)-loss against the Schwartz Mellin transform.
3. Retain the one-sided top profile, its cotangent boundary, the hard
   value \(d=\lfloor\sqrt X\rfloor\), and all stationary half-weights.
4. Keep height floors \(H_j\), active bottom scales, profile seams, and
   the inactive bottom owner distinct.
5. The artificial radial cutoff \(V\) is smooth; do not import the failed
   length-\(R\) sharp-window strip or its endpoints.
6. State whether (60.2) is proved in modulus or only in the precise real
   part needed by GAR.
7. No claim is allowed for \(n=o(Y)\), the alpha transition, full GAR,
   M9-M1, M9, or the final exponent.

No numerical experiment is requested.  The round is entirely analytic.
