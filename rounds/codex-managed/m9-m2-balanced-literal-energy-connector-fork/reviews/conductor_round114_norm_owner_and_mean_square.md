# Conductor Round-114 review: mean-square connector, norms, and owners

Campaign: `m9-m2-balanced-literal-energy-connector-fork`

## Mean-square connector decision

The hostile report identifies a correction to the conductor candidate.
The old proposed mean-square node concerns the **full** smooth symbol, not
the gcd-masked low packet.  For

\[
\mathfrak M_h^{\rm full}(B)
=\sum_{\substack{h\asymp L\\h\ {\rm odd}}}
\left|\sum_{k\asymp K}A_B(h,k)e(R\sqrt{hk})\right|^2,
\]

Cauchy gives

\[
|\mathcal T_B|^2
\le L\mathfrak M_h^{\rm full}(B).
\]

Consequently

\[
\mathfrak M_h^{\rm full}(B)
\ll_\varepsilon L^{1/2}K^{3/2}X^\varepsilon
\tag{114.R10}
\]

implies

\[
|\mathcal T_B|\ll_\varepsilon(LK)^{3/4}X^\varepsilon.
\]

For `1<=K/L<=16` this is `O(L^(3/2)X^epsilon)`.  Subtracting the already
proved high-gcd owner gives the same bound for `T_B^low`, and the exact
identity `Z_B=2iT_B^low` proves the balanced packet target.  Thus the
fixed-block implication from (114.R10) to BAL is proved.

The estimate (114.R10) itself is not proved.  It is diagonal-critical: its
row diagonal is `asymp LK`, the full permitted scale.  It also loses
`chi_4(h)`, which is constant on the outer row and disappears under the
modulus.  A coefficient-uniform strengthening is false by phase
conjugation.

The character-preserving alternative is

\[
\mathfrak M_k^{\rm full}(B)
=\sum_{k\asymp K}
\left|\sum_{h\asymp L}\chi_4(h)A_B(h,k)e(R\sqrt{hk})\right|^2
\ll_\varepsilon L^{3/2}K^{1/2}X^\varepsilon.
\tag{114.R11}
\]

It also suffices after Cauchy in `k`; at `K asymp L`, both mean-square
budgets are `L^2X^epsilon`.  Neither mean square is equivalent to the
direct scalar target, and failure of one would not refute the packet.

## Graph-scope correction

The existing proposed node `M9-M2-dual-square-root-spacing-mean-square`
currently points directly to all of `M9-M2`.  That implication is invalid:
the hard TOP parent is independent.  Round 114 certifies only the literal
fixed-balanced-block connector.  A later owner audit may also connect the
same full-symbol mean square to UNBAL, but that edge is not promoted here.

Accordingly, remove the direct `M9-M2` implication and point the proposed
mean square only to the balanced smooth parent for now.  Keep its status
`proposed`.

## Owner and norm audit

- The smooth gcd telescope is summed exactly before the direct modulus;
  no shellwise `l1` estimate is used.
- The direct packet energy, the full-symbol mean square, the gcd-masked
  Gram, and the character-preserving Gram are four distinct objects.
- High gcd is used once, after the full-symbol mean-square implication.
- Square and near-square terms remain target-safe linear owners.  They are
  not inserted as masks into the smooth symbol or used to cancel the
  double-far survivor.
- The proof is per one physical `(D,L)` block; no cross-block cancellation
  occurs.
- The corridor counts are uniform for fixed `1<=K/L<=16`.  The persistent
  analytic target is `j=1`; the `j=2` exact-square boundary remains a
  separate control and is not declared estimated.
- The `L^(3/2)` linear budget and `L^3` energy budget are kept separate.

## False-shadow decision

On a dense comparable low-gcd odd rectangle, arbitrary bounded phases may
conjugate `e(R sqrt(hk))`, making either mean-square Gram of order `L^3`
and the direct double-far energy of order `L^4`.  This rejects all
coefficient-uniform versions.  It does not lower-bound the actual Vaaler
symbol, whose theorem remains open.

## Round closing decision

Promote the exact energy/corridor reduction and the conditional full-symbol
mean-square connector.  Create the double-far actual energy as the next
open child.  Retain the balanced estimate and every downstream endpoint
claim open.  A Round-115 continuation is justified only for a theorem
acting on the signed inner correlation in (114.R8), not for generic cone
transversality or another capacity-preserving change of variables.
