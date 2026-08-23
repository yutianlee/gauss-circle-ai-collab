# Round 130 synthesis: lower-shell support sharpens, top-shell correlation remains open

Campaign: `gc-w7-16-post-inner-outer-bilinear-gate`

Starting graph SHA-256:
`354f5ca462467d091a9a50c8dbc1173ffba56516963274f9fc232ea11890d20e`

## Frozen question

Round 130 tested whether the exact post-inner numerator increments and
outer rays yield a signed contraction beyond the complete
$Y^{35/48+\varepsilon}$ fixed-block bound, or whether positive duality,
product windows, and the unit-Hessian transform return the same capacity.

## Exact outcome

There is a rigorous shellwise improvement.  On a half-open reduced
denominator shell $b'\asymp B$, the exact Stieltjes-recombined complete
lift has

\[
 g\asymp D/B,
 \qquad |a'|\asymp LB/D,
 \qquad \#\{a'\}\ll LB/D.
\]

The Round-129 inner estimate $K_B/L$, together with
$\sum_r|A_i(r)|\ll D$, gives

\[
 \boxed{|\mathfrak O_{i,B}^{+}|\ll_\varepsilon
 BK_BY^\varepsilon.}
\]

Thus every lower shell gains the factor $B/D$ over the earlier uniform
ledger.  The complete residual is now localized to $B\asymp D$, where

\[
 BK_B=DK_D=Y^{35/48+o(1)}.
\]

No complete fixed-power saving follows because the top shell remains.

The exact outer-energy calculation also closes a normalization seam.  In
literal atom coordinates the resolved energy is
$\mathbf1^*H^*H\mathbf1$; after physical reassembly it is
$b^*K_{B,+}^*K_{B,+}b$.  The full triangular random-cell operator instead
has $\lVert Gb\rVert_2^2=b^*G^2b$.  There is no proved connector from the
resolved row to $G^2$.  A support- and norm-matched aligned control reaches
$LDK_B^2$ energy and $DK_B$ scalar capacity.  Hence marginal support and
norm facts cannot prove either contraction; this is not a lower bound for
the actual coefficients.

On the primitive top shell, for one fixed outer ray,

\[
 n=aq-bp,
 \qquad n\equiv-bp\pmod {|a|},
 \qquad b'={b(a+p)+n\over a}.
\]

If the physical $p$-support has span $O(|a|)$, fixed $n$ has only $O(1)$
admissible $p$-lifts.  The numerator increment is therefore an induced
determinant residue, not a second independent long variable.  This rules
out automatic independent-$p$ square-root credit but leaves a literal
residue-correlation theorem open.

Exact Stieltjes, Möbius, and complete-lift recombination returns the
original product wave.  M1 restores $\chi_4(d')$; M2 retains the fixed
$\epsilon_{\rm sgn}\chi_4(|h'|)$ sector factor.  After all $B$-owners
are reassembled, the accepted original-variable theorem gives only
$Y^{37/48+\varepsilon}$.  On the isolated top shell, a $p$-first
product-window modulus gives the still weaker $D^2/L=Y^{40/48}$, and a
two-variable transform followed by aliaswise modulus gives
$DQ_*=Y^{43/48}$.  These are scoped method no-gos, not physical lower
bounds.

## Proof status

The complete critical fixed block remains

\[
 |\mathfrak O_i|\ll_\varepsilon Y^{35/48+\varepsilon},
\]

which is $Y^{11/48}$ above the determinant target $Y^{1/2}$.  The first
open graded object is now only the actual signed $B\asymp D$ scalar: prove
any fixed-power saving while retaining outer coefficients, determinant
residue lifts, thresholds, reciprocal aliases, characters, and owners
before a positive norm.  A full $Y^{11/48}$ saving would close this
determinant target.

The local shell refinement does not lower the complete correlation
exponent below $9/16$.  Therefore the internally proved global exponent
stays $1/3$, and the audited external benchmark is unchanged.
M9-M1, M9-M2, endpoint uniformity, M9, the conditional bridge, and the
quarter target all remain open.

No computation or external theorem was used.  The round was 100%
analytical/algebraic.

Resulting graph SHA-256:
`23e7bfacbf6abc5582769fbe8d427cbca2379e1d265b99df21d93a65ec504825`.
