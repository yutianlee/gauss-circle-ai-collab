# Round 175 strategy: whole-chain actual-symbol K26 gate

## Frozen objective

Work on authoritative graph
`e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211`
and on no other proof owner.  Put \(e(t)=e^{2\pi i t}\), let
\(J=\sqrt X\), \(1\ll L\ll H\le J^{1/2}\),
\(R_0=\lceil L\rceil\), and let \(M\asymp L^2\) be the exact length of
the containing interval on which the accepted residual coefficient is
zero-extended.  Retain

\[
 c_N^{\rm rem}
 =\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
   \chi_4(d)\lambda_N(d),\qquad
 z_N=c_N^{\rm rem}e(J\sqrt N),\qquad
 D_L=\sum_N|z_N|^2\ll_\varepsilon L^2X^\varepsilon.
 \tag{175.1}
\]

Here \(\lambda_N(d)\) is the complete literal residual incidence
coefficient: selector and no-pair values, squarefree and coprimality masks,
two-adic branch, Vaaler/profile factor, floors, stars, support crossings,
endpoint values, and zero-extension values are part of the coefficient.

Define the minimal terminal index \(K\) by

\[
 R_{j+1}=\min(2R_j,M)\quad(0\le j<K),\qquad R_K=M,
 \tag{175.2}
\]

so a strict final link is not rounded to a doubling.  With

\[
 F_R(\theta)=\sum_{|r|<R}\left(1-\frac{|r|}{R}\right)e(r\theta),
 \qquad B_{R,S}=F_S-F_R,
 \tag{175.3}
\]

use exactly the cardinal interpolation, Fourier convention, and transformed
functions \(U_{k,\ell}^{(\epsilon)}\) in equations (2.7)--(2.8) of
`rounds/codex-managed/full-proof-round171-173-strategy-literature-review/reports/full_graph_frontier_reconstruction.md`.
For \(R<S\le2R\), this fixes

\[
\begin{aligned}
 \mathcal N_{R,S}={1\over8}\Re\sum_{\epsilon=0}^1
 &\sum_{\substack{k,k'\in\mathbb Z\\k,k'\ \mathrm{odd}}}
  \sum_{\substack{\ell,\ell'\in\mathbb Z\\\ell,\ell'\ne0}}
  \chi_4(k)\chi_4(k')\\
 &\times\int_0^1B_{R,S}(\theta)
  U_{k,\ell}^{(\epsilon)}(\theta)
  \overline{U_{k',\ell'}^{(\epsilon)}(\theta)}\,d\theta.
\end{aligned}
\tag{175.4}
\]

The sole target is the deliberately one-sided inequality

\[
 \boxed{
 \sum_{j=0}^{K-1}\mathcal N_{R_j,R_{j+1}}
 \ll_\varepsilon L^3X^\varepsilon.}
 \tag{175.5}
\]

There is no absolute value outside the whole chain.  A whole-chain absolute
bound or linkwise bound is sufficient but stronger than required.

## Mechanism gate

The only eligible positive route must first prove and use a literal property
of the actual residual symbol that is absent from the admissible dechirped
and adversarial-sign controls.  The intended open resource is collective
signed correlation across the complete stopped chain before any modulus over
\(j,k,k',\ell,\ell'\), cardinal cells, arithmetic openings, parity peaks,
endpoints, transitions, or zero-extension pieces.

The accepted coefficient-insensitive capacity is
\(L^4X^\varepsilon\), against the target \(L^3X^\varepsilon\).  A valid
proof must exhibit exactly where the factor \(L\) is saved and must restore
all literal normalization and boundary costs after that saving.

## Mandatory controls

1. Keep both absolute-parity branches, the factors \(i/2\) and \(1/8\),
   and one outer real part.
2. Keep \(k,k'\) odd and \(\ell,\ell'\ne0\) until the full signed
   recombination.  Restore the ordinary-zero-containing sector only through
   the already proved collective estimate.
3. Retain every cardinal cell, selected/no-pair row, arithmetic mask,
   endpoint, transition, point value, support birth/death, and zero-extension
   jump.
4. Retain the strict terminal link and pay the short correction exactly
   once.
5. Distinguish the zero physical diagonal from a fixed dual diagonal.
6. Test the actual coefficient theorem against the nonliteral dechirped
   control, constant-character shadow, erased-selector shadow, and arbitrary
   sign control.  A theorem valid for all such controls has not used the
   required symbol structure.
7. Verify the complete restored power ledger before claiming a sector or
   owner implication.

## Forbidden restarts and stop rule

Stop at the first coefficient, normalization, parity, endpoint, transition,
terminal-link, ordinary-zero, fixed-dual-diagonal, rank-one-centre, or
restored-\(L^4\) failure.  Stop if an argument:

- takes a positive norm or modulus before the whole stopped chain;
- reduces to coefficient-uniform positivity, a dechirped estimate, a fixed
  dual diagonal, or rank-one stationary phase;
- repeats the Round-173 tangent first difference, its adjoint, or a second
  Abel transfer that merely returns the difference to the bandpass;
- repeats the accepted product-collar or fixed-product fibre routes;
- proves only a strict subaggregate, one link, one shift, one parity peak, or
  a smoothed endpoint; or
- restores the \(L^4X^\varepsilon\) envelope.

Do not pivot inside Round 175 to K17a, full \(t=1\), another hard-TOP
channel, BAL, UNBAL, M1, GAR, endpoint assembly, or a local-moment exponent
lane.

## Promotion and downstream scope

Promotion requires an exact proof of (175.5), independent seam review of the
literal formula and factor-\(L\) ledger, false-control survival, complete
endpoint and terminal-link restoration, and a mechanically valid State
Patch.  Strategy ranking, source resemblance, or a favorable nonliteral
model is not evidence.

Even success closes only K26 and, through the accepted maximal-scale
implication, the complete residual scalar.  It does not close full
\(t=1\), other hard-TOP channels, complete TOP, either BAL scope, UNBAL,
M9--M2, either direct M1 parent or GAR, endpoint uniformity, M9, a bridge,
the quarter theorem, or an exponent.

## Allocation and admissible terminal labels

Round 175, if launched, is 100% analytical/algebraic and 0% numerical.  It
must close under exactly one of:

- `hard_top_t1_residual_whole_chain_actual_symbol_target`;
- `strict_whole_chain_actual_symbol_sector`; or
- `whole_chain_actual_symbol_capacity_or_self_return_no_go`.
