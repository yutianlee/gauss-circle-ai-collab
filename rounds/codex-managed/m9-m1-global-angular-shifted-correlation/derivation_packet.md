# Round 54 derivation packet: coefficient-preserving radial differencing

This packet freezes the first post-scale signed arithmetic object after the
Round-53 scale-capacity no-go.  It does not assert a shifted-correlation
estimate.

## 1. Exact global radial sum

Let

\[
 S_X=\sum_{n\le N}^{*} A_X(n)n^{-3/4}e(\sqrt{Xn}),
 \qquad N=16\sqrt X,
\]

where

\[
 A_X(n)=\sum_{\substack{h\mid n\\q=n/h\ {\rm odd}}}
 \chi_4(q)\Omega_X^*(n,h),
\]

\[
 \Omega_X^*(n,h)=\sum_j\mathbf1_{h\le H_j}
 \Phi\!\left(\frac h{H_j+1}\right)
 \left[w_j\!\left(2h\sqrt{X/n}\right)\right]^*.
\]

The global angular radial estimate asks

\[
 \operatorname{Re}\{e(1/8)S_X\}\ll_\varepsilon X^\varepsilon.
\]

The unique external \(X^{1/4}\), hard-top boundary, inactive bottom, and
transform errors are already separate and are not part of \(S_X\).

## 2. Frozen objective

For an integer Fejer/van-der-Corput parameter \(1\le R\le N\), derive an
exact finite differencing inequality that keeps the shift average outside
absolute values as long as possible.  Write the shifted coefficient

\[
 \mathcal C_r(X)=
 \sum_{n\le N-r}^{*}
 A_X(n+r)\overline{A_X(n)}
 ((n+r)n)^{-3/4}
 e\!\left(\sqrt X(\sqrt{n+r}-\sqrt n)\right)
\]

with every endpoint and star convention stated.  Expand the coefficient
product into its exact \((h_1,q_1,h_2,q_2,j_1,j_2)\) incidences, including
the additive constraint

\[
 h_1q_1-h_2q_2=r.
\]

Determine the weakest averaged signed shifted-correlation bound, with exact
\(R\)- and \(N\)-powers, that would imply the target.  Then either prove a
nonempty target-relevant range, or give a rigorous capacity/no-go theorem
for this one-step route.

## 3. Mandatory distinctions

- The project only needs the real part of \(e(1/8)S_X\); a proof may use a
  phase-aware polarization, but it may not silently replace this by a stronger
  complex bound without recording the loss.
- The star at \(n=N\), the shifted upper endpoint \(n=N-r\), and all angular
  profile stars are distinct.
- The coefficient \(A_X(n)\) depends on \(X\), on the divisor angle, floors,
  and the exact dyadic scale sum.  It is not \(r_2(n)/4\) and is not an
  arbitrary divisor-bounded sequence.
- Taking \(|\mathcal C_r|\) term by term, applying ordinary divisor bounds,
  or using generic square-root phase curvature may spend the entire desired
  saving.  Audit this explicitly.
- Any imported shifted-convolution, spectral, large-sieve, or exponent-pair
  theorem must match the additive shift, character placement, moving
  archimedean symbol, uniform \(r,R,X\) ranges, and endpoint conventions.
- Do not infer the alpha connector or outside-height estimate merely from a
  physical radial bound; state the exact transfer still required.

## 4. Completion rule

A successful result supplies:

1. the exact finite Fejer/van-der-Corput inequality with constants or
   harmless explicit absolute constants;
2. the exact shifted incidence kernel and owner table;
3. the precise averaged correlation theorem sufficient for the target;
4. a proof in a nonempty range, or a sharp obstruction showing what this
   differencing step cannot save;
5. an audited literature applicability decision if external methods are
   discussed.

No numerical experiment is needed.  The round is 100% analytical unless a
bounded exact check is used only to falsify an algebraic identity.
