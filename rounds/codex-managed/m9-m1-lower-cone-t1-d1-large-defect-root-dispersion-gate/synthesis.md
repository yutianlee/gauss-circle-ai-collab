# Round 154 synthesis

- Campaign: `m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate`
- Starting graph: `6a36e4063b8f944bf5349c333e6cbf569694c8bdbeaa6314cad596631c125984`
- Terminal label: `strict_large_defect_root_range`
- Graph mutation: applied; resulting graph
  `84bbcb3413936c9b672c829cdba97b8d0bde69f7a6df677b61f24e9ec27e243a`

## Outcome

Round 154 proves a strict logarithmic enlargement of the owned defect
collar and an exact all-scale root-defect linearization.  It does not prove
the remaining direct wave or any positive-power range.

For

$$
 Q_U=\sum_{\substack{n>0,\ n\ \mathrm{odd}\\
 |k(n)^2-Nn|>M^{3/4}}}
 \chi _4(n)n^{-3/4}A_U(n)e(\sqrt{Nn}),
 \qquad
 k(n)=\left\lfloor\sqrt{Nn}+\frac12\right\rfloor,
\tag{154.Y1}
$$

put $j=k^2-Nn$.  The exact nearest cell is
$-k\le j\le k-1$, the converse holds, and the supported map has
multiplicity one.  Uniformly on the selected graph,

$$
 e\!\left(-\frac{j}{k+\sqrt{k^2-j}}\right)
 =e\!\left(-\frac{j}{2k}\right)
 +O\!\left(K^{-1}\right)
 \quad\text{per selected term},
\tag{154.Y2}
$$

and the complete weighted error is
$O_\varepsilon(N^{-1/2}M^{-1/4}X^\varepsilon)$.

For every fixed $A>0$, the complete collar

$$
 M^{3/4}<|j|\le M^{3/4}(\log(2X))^A
\tag{154.Y3}
$$

is $O_{\varepsilon,A}(X^\varepsilon)$.  Thus the first open direct wave
may be restricted beyond every fixed polylogarithmic collar and may use
the linearized phase.  This does not own $M^{3/4+\delta}$ for any fixed
$\delta>0$, does not change the boundary $M^{449}\asymp R^{780}$, and
does not improve an exponent.

## Completion status

The quotient-character selector modulo $4N$ is exact for arbitrary $N$.
After divisibility is already imposed, its odd Fourier rows have rank one
and normalized frequency Cauchy is equality.  Before selection, the ambient
rows remain distinct and admit lawful finite quadratic completion.

With $q=4N$, $d=(h,N)$, and $q'=q/d$, the full normalized completed family
is

$$
 -\frac{i(1+i)}{2Nq}
 \sum_j\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi _4(d)d\sqrt{q'}
 \sum_{v\bmod(q'/2)}
 \widehat B_j(2dv)K(-v^2,-j;q').
\tag{154.Y4}
$$

DFI Lemma 6.1 is an exact source match for the theta-multiplier
Kloosterman sum.  Restoring every gcd stratum, nonzero dual mode, zero
mode, sign, endpoint, profile, and outer defect gives

$$
 |Q_U(V)|\ll_\varepsilon
 \left(M^{-3/4}V+M^{-1/4}\right)X^\varepsilon.
\tag{154.Y5}
$$

This is target-sized on fixed or polylogarithmic first collars but loses
$N^{1/2}M^{-1/4}$ at the top defect scale.  The large right side is an
upper-bound term, not a signed lower bound.

If exact and small defects are restored at scalar level before completing
the full nearest-cell partition, the centered negative row has saddle

$$
 n_*=4N/a^2,\qquad e(\Psi_*)=e(N/a),
\tag{154.Y6}
$$

with exactly the accepted reciprocal-row symbol.  The remainder and
endpoint ownership is inherited from Round 152.  Thus the principal
full-cell transform self-returns rather than supplies a new gain.

## Current frontier

The first open theorem is a normalized signed outer-defect estimate for

$$
 \sum_{V<|j|\le2V}\sum_{d\mid N}\sum_v
 \widehat B_j(2dv)K(-v^2,-j;4N/d),
 \qquad
 M^{3/4}(\log(2X))^A\lesssim V\lesssim\sqrt{NM},
\tag{154.Y7}
$$

with the factor in (154.Y4), both signs, every gcd stratum, zero mode,
strict mask, actual profile, and literal cell endpoints.  Equivalently,
one may prove a selected signed cross-fibre estimate for $e(-j/(2k))$.
For odd $N$, the character is constant within each fixed-$j$ root fibre,
so the required sign must survive the outer $j$-ordering.

The $D>1$ recovery fibre, $L>1$ rows, growing-$M$ generic $t=1$ sector,
every original $t\ge2$ layer, the Round-138 cross owner, remaining M1 and
all M2 owners, endpoint uniformity, M9, and the conditional bridge remain
open.

The internally proved global exponent remains $1/3$.  The separately
audited external Li--Yang exponent remains

$$
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\tag{154.Y8}
$$

No global exponent changes in Round 154.

## State effect

The validated and applied State Patch creates one exact
root-defect/logarithmic collar reduction, one DFI source-audit node, and
one route-scoped root-dispersion obstruction; updates five frontier
interfaces; rejects twenty-one overbroad inferences; and records eight
principal downstream obligations unchanged. Three independent terminal
reviews are GREEN. The resulting graph is
`84bbcb3413936c9b672c829cdba97b8d0bde69f7a6df677b61f24e9ec27e243a`.
