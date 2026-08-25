# Round 155 synthesis

- Campaign: m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate
- Starting graph: 84bbcb3413936c9b672c829cdba97b8d0bde69f7a6df677b61f24e9ec27e243a
- Terminal label: outer_defect_theta_dispersion_no_go
- Graph mutation: applied
- Resulting graph: f9866ea08923ae28f9631e503d2a5eb6be3cd85a09eb05505deec2903d1658b6

## Outcome

Round 155 proves the exact complete-dual obstruction at the first
post-collar D=1 outer-defect frontier. It does not prove the signed block,
a positive-power defect range, a new $M$-range, or an exponent.

For $q=4N$, every odd $d\mid N$, $c=q/d$, and $H=c/2$,

$$
 \sum_{v\bmod H}\widehat B_j(2dv)K(-v^2,-j;c)
 =\frac{1-i}{2}\sqrt c
 \sum_{x\bmod q}B_j(x)
 \sum_{a\bmod c}^{*}\chi_4(a)e_c(a(x^2-j)).
\tag{155.Y1}
$$

Restoring the exact exterior factor gives

$$
 -\frac{i(1+i)}{2Nq}d\sqrt c\,
 \frac{1-i}{2}\sqrt c
 =-\frac{i}{2N}\frac{dc}{q}=-\frac{i}{2N}.
\tag{155.Y2}
$$

The unique partition $d=(h,N)$, $h=da$ then reconstructs every odd
selector frequency. Complete $v$-resummation is therefore precisely the
inverse of the Round-154 quadratic Gauss completion. It supplies no new
square-root cancellation.

## Norm and zero-mode status

Sampled Parseval retains every fold modulo $H=2N/d$:

$$
 \sum_{v\bmod H}|\widehat B_j(2dv)|^2
 =H\sum_{r\bmod H}
 \left|\sum_{\substack{x\bmod q\\x\equiv r\pmod H}}B_j(x)\right|^2
 \ll_\varepsilon
 \left(\frac{N^{3/2}}{dM}+\frac{N}{M^{1/2}}\right)X^\varepsilon.
\tag{155.Y3}
$$

This is an upper norm capacity, not defect orthogonality. The mandatory
zero row has only

$$
 |\mathcal T_{0,U}(V)|\ll_\varepsilon
 \left(N^{-1/2}M^{-1/4}V+M^{-1/4}\right)X^\varepsilon,
\tag{155.Y4}
$$

while the nonzero termwise DFI ledger remains
$M^{-3/4}VX^\varepsilon$. At $V=\sqrt{NM}$ the zero-row upper capacity
contains $M^{1/4}$; this is not a lower bound.

Every proper dual cutoff becomes $\eta(u-ax)$ after square completion and
remains coupled in the unit and physical variables. A hypothetical
square-root selected-incidence estimate has size
$M^{-3/4}V^{1/2}X^\varepsilon$ and would be target-sized only for
$V\le M^{3/2}$, but no such estimate is proved.

The flat selected phase varies by only $O(V/\sqrt{NM})\le O(1)$. Its
exact expansion localizes only to

$$
 \left\|\frac ac+\frac1{2\sqrt{x^2-j}}\right\|_{\mathbb R/\mathbb Z}
 \ll\frac1V,
\tag{155.Y5}
$$

a circular arc of capacity $O(1+c/V)$ that wraps through zero. Both the
near-zero and near-$c$ branches remain. This is localization, not gain.

## Source and selected interfaces

DFI Lemma 6.1 remains an exact theorem for each individual
$K(-v^2,-j;4N/d)$, including $v=0$. The audited DFI/Sun spectral
formulas average moduli and retain their full spectral pieces; Lam is a
holomorphic varying-weight one-sequence sieve; the current fixed-modulus
bilinear theorems have ordinary or prime kernels and separated
coefficients. None directly matches the literal fixed-modulus
nonseparable family. This is a dated direct-interface no-match, not an
impossibility theorem.

The first source-unproved row is

$$
 \sum_{V<|j|\le2V}\widehat B_j(0)K(0,-j;4N/d).
\tag{155.Y6}
$$

If it is resolved, the next input is the incomplete nonzero matrix or the
selected partial-sum theorem

$$
 \sup_{I\subset\{n\asymp M\}}
 \left|\sum_{\substack{n\in I,\ n\ \mathrm{odd}\\
 V<|j_n|\le2V}}\chi_4(n)e(\sqrt{Nn})\right|
 \ll_\varepsilon M^{3/4}X^\varepsilon.
\tag{155.Y7}
$$

The ordinary-K calculation in the blind report is only a surrogate
invertibility control and is not used as the theta normalization.

## Downstream status

The proved defect owner remains only the fixed-polylogarithmic collar from
Round 154. The boundary $M^{449}\asymp R^{780}$ is unchanged. The D=1
zero and incomplete rows, $D>1$, $L>1$, generic $t=1$, every original
$t\ge2$ layer, the Round-138 cross owner, remaining M1 and all M2 owners,
endpoint uniformity, M9, and the bridge remain open.

The internally proved global exponent remains $1/3$. The separately
audited external Li--Yang exponent remains

$$
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\tag{155.Y8}
$$

No global exponent changes in Round 155.

## State effect

The validated State Patch creates one fixed-modulus spectral-source audit
and one complete-theta inverse-Gauss obstruction; updates five frontier
interfaces; rejects twenty overbroad inferences; and records eight
principal downstream obligations unchanged. Three independent terminal
reviews are GREEN. The resulting graph is
f9866ea08923ae28f9631e503d2a5eb6be3cd85a09eb05505deec2903d1658b6.

