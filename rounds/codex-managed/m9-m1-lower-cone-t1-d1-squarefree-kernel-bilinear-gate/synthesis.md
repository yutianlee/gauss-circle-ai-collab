# Round 153 synthesis

- Campaign: `m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate`
- Starting graph: `9ffef2e30c99d83d02d28141834b585d02dd77483fa7bfd8e572d45d6985fcc1`
- Terminal label: `squarefree_kernel_bilinear_no_go`
- Graph mutation: applied; resulting graph
  `6a36e4063b8f944bf5349c333e6cbf569694c8bdbeaa6314cad596631c125984`

## Outcome

Round 153 proves that complete squarefree Mobius inversion and exact
recombination do not expose independent bilinear owners for the Round-152
survivor. With $S=\lceil M^{1/4}\rceil$ and the literal large-defect weight
$F_U$, one has

$$
 P_U^*=\sum_{r\ {
m odd}}C_S(r)
 \sum_{b\ {
m odd}}F_U(r^2b),
 \qquad
 C_S(r)=\sum_{\substack{a\mid r\\r/a<S}}\mu(a).
\tag{153.Y1}
$$

For $r<S$, $C_S(r)={\bf1}_{r=1}$. The remaining $r\ge S$ boundary has
absolute size $O_\varepsilon(X^\varepsilon)$. Therefore

$$
 P_U^*=\sum_{b\ {
m odd}}F_U(b)+O_\varepsilon(X^\varepsilon)
      =P_U+O_\varepsilon(X^\varepsilon).
\tag{153.Y2}
$$

The first equality is the new exact recombination statement. The second is
consistent with the accepted Round-152 owner ledger; the boundary is exactly
the negative of its safe large-square-factor sector.

## Scoped no-go

Assigning independent ownership to dyadic $a$- or $s$-blocks destroys the
exact divisor cancellation for $1<r<S$. Taking a coefficient-blind positive
majorant after Cauchy likewise cannot certify the signed sum. This closes
only complete inversion followed by complete recombination, together with
the audited coefficient-blind Type-I/Type-II majorants.

A future coefficient-sensitive signed bilinear theorem remains possible.
Such a theorem would prove the direct wave as well. The isolated $s=1$
squarefree layer remains an open partial subproblem, not a discarded seam.

## Source status

The best licensed one-variable estimate remains

$$
 \left|\sum_{b\ {
m odd}}F_U(b)\right|
 \ll_\varepsilon
 \left(\frac{R^{780}}{M^{449}}\right)^{1/1592}X^\varepsilon
 +X^\varepsilon.
\tag{153.Y3}
$$

It is target-safe only on the already owned side
$M^{449}\gg R^{780}$. No audited bilinear, Mobius, squarefree-twist,
nonlinear-twist, or modular-root theorem closes the literal open side.
Robert--Sargos has both a coefficient-separation mismatch and an unfavourable
printed upper-bound power even in a separated model. These are source-route
no-matches, not literature impossibility or signed lower bounds.

## Current frontier

The first unproved estimate remains

$$
 \left|\sum_{b\ {
m odd}}F_U(b)\right|
 \ll_\varepsilon X^\varepsilon
 \qquad(M^{449}\ll R^{780}).
\tag{153.Y4}
$$

Round 153 supplies no new range. The $D>1$ recovery fibre, $L>1$ rows,
growing-$M$ generic $t=1$ sector, every original $t\ge2$ layer, the
Round-138 cross owner, remaining M1 owners, all M2 owners, endpoint
uniformity, M9, and the conditional bridge remain open.

The internal global exponent remains $1/3$. The separately audited external
Li--Yang exponent remains

$$
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\tag{153.Y5}
$$

No global exponent changes in Round 153.

## State effect

The applied State Patch creates one exact recombination obstruction, updates
four existing frontier interfaces, rejects eighteen audited overbroad
inferences, and records eight principal downstream obligations unchanged.
Post-application validation is recorded in the conductor controls.
