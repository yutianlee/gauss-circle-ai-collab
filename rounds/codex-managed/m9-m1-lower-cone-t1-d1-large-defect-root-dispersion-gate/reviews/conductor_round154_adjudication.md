# Round 154 conductor adjudication

- Campaign: `m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate`
- Round: 154
- Starting graph SHA-256: `6a36e4063b8f944bf5349c333e6cbf569694c8bdbeaa6314cad596631c125984`
- Terminal label: `strict_large_defect_root_range`
- Terminal reviews: mathematical GREEN; hostile scope/mask GREEN; primary-source GREEN

## 1. Result

Round 154 closes with a genuine but logarithmic strict defect owner, an
exact all-scale linearization, and a rigorously scoped completion
obstruction.  It does not prove the remaining direct wave and changes no
positive-power scale or global exponent.

Let

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 J=M^{3/4},\qquad K=\sqrt{NM},\qquad 1\ll M\le R^2,
\tag{154.A1}
$$

and let $Q_U$ be the literal direct large-defect scalar with the actual
zero-extended profile and external $B_{1,U}(1)$ left outside.  For

$$
 k=\left\lfloor\sqrt{Nn}+\frac12\right\rfloor,
 \qquad j=k^2-Nn,
\tag{154.A2}
$$

the exact cell is $-k\le j\le k-1$, and the map between retained odd $n$
and the corresponding $(k,j)$ is bijective.  On this selected scalar,

$$
 e\!\left(-\frac{j}{k+\sqrt{k^2-j}}\right)
 =e\!\left(-\frac{j}{2k}\right)
 +\text{a total }
 O_\varepsilon(N^{-1/2}M^{-1/4}X^\varepsilon)
 \text{ error}.
\tag{154.A3}
$$

For every fixed $A>0$, the complete collar

$$
 J<|j|\le J(\log(2X))^A
\tag{154.A4}
$$

has contribution $O_{\varepsilon,A}(X^\varepsilon)$.  Hence the first
open selected wave may be required to have
$|j|>J(\log(2X))^A$.  This is the only strict-range credit: it is not a
bound for $|j|\le JM^\delta$ for any fixed $\delta>0$, not a new range in
$M$, and not an exponent improvement.

The exact quotient-character Fourier selector is valid for every $N$.
Post-selection frequency Cauchy is equality; the lawful ambient rows are
distinct.  Exact finite completion of the latter produces the DFI
theta-multiplier Kloosterman sum and gives, for every dyadic block,

$$
 |Q_U(V)|\ll_\varepsilon
 \left(M^{-3/4}V+M^{-1/4}\right)X^\varepsilon.
\tag{154.A5}
$$

This independently certifies the collar but leaves the positive top-block
power $N^{1/2}M^{-1/4}$.  The principal full-cell stationary completion,
after lawful scalar restoration of the exact and small defects, reproduces
the already accepted reciprocal row.  Neither fact rules out a new signed,
mask-preserving outer-defect theorem.

## 2. Exact statement and owner scope

The literal scalar is

$$
 Q_U=\sum_{\substack{n>0,\ n\ \mathrm{odd}\\
 |k(n)^2-Nn|>J}}
 \chi _4(n)n^{-3/4}A_U(n)e(\sqrt{Nn}).
\tag{154.A6}
$$

It includes the large-square-factor terms, although Round 152 separately
owns their absolute contribution.  Exact squares and nonzero small defects
are absent from $Q_U$ and are restored only when passing to the full $P_U$
for the principal self-return.  Bounded $M$ and the already owned side
$M^{449}\gg R^{780}$ remain inherited owners rather than Round-154 credit.

The bijection gives

$$
 \begin{aligned}
 Q_U={}&\sum_{\substack{k\ge1,\ -k\le j\le k-1,\ |j|>J\\
 N\mid k^2-j,\ (k^2-j)/N\ \mathrm{odd}}}
 \chi _4\!\left(\frac{k^2-j}{N}\right)
 \left(\frac{k^2-j}{N}\right)^{-3/4}
 A_U\!\left(\frac{k^2-j}{N}\right)\\
 &\hspace{30mm}\times
 e\!\left(-\frac{j}{k+\sqrt{k^2-j}}\right).
 \end{aligned}
\tag{154.A7}
$$

Every support component, zero-extension jump, half-open endpoint, both
defect signs, quotient parity, and two-adic case is literal.  On support,
$k\asymp K$, the total $k$-span is $O(K)<N$, and $2k<N$ for sufficiently
large $X$ with the fixed support dilates.  No multiplicity or cancellation
is inferred from these facts.

## 3. Verified proof kernel

The tie exclusion, exact cell, and converse follow from

$$
 k^2-k+1\le Nn\le k^2+k.
\tag{154.A8}
$$

For $s=\sqrt{k^2-j}$, the exact residual identity is

$$
 -\frac{j}{k+s}=-\frac{j}{2k}
 -\frac{j^2}{2k(k+s)^2}.
\tag{154.A9}
$$

Since $|j|\le k$, the second term is $O(K^{-1})$.  The selected weighted
absolute capacity is $M^{1/4}X^\varepsilon$, proving (154.A3).  This error
is not priced over off-congruence ambient points.

For $j\ne0$, the all-prime-power root calculation gives

$$
 \rho_N(j)\le4\,2^{\omega(N)}\sqrt{(|j|,N)},\qquad
 \sum_{0<|j|\le H}\rho_N(j)\ll_\varepsilon HX^\varepsilon
 \quad(H<N).
\tag{154.A10}
$$

With $H=J(\log(2X))^A$ and the actual $M^{-3/4}$ weight, epsilon splitting
proves the collar (154.A4).

The selector is

$$
 {\bf1}_{N\mid t}\chi _4(t/N)
 =-\frac{i}{2N}
 \sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}
 \chi _4(h)e\!\left(\frac{ht}{4N}\right).
\tag{154.A11}
$$

On $t=Nn$ with $n$ odd, the unnormalized rows are $iQ_U$ or $-iQ_U$ and
normalized $h$-Cauchy is equality.  Before selection they retain the factor
$e_N(m(k^2-j))$ and are genuinely distinct.

For $q=4N$, $d=(h,N)$, $h=da$, and $q'=q/d$, finite Fourier completion in
$k$ gives zero unless the dual frequency is $b=2dv$.  The exact completed
expression is

$$
 -\frac{i(1+i)}{2Nq}
 \sum_j\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi _4(d)d\sqrt{q'}
 \sum_{v\bmod(q'/2)}
 \widehat B_j(2dv)K(-v^2,-j;q').
\tag{154.A12}
$$

DFI Lemma 6.1 applies because $q'\equiv0\pmod4$:

$$
 |K(m,n;c)|\le(m,n,c)^{1/2}c^{1/2}\tau(c).
\tag{154.A13}
$$

The $d\sqrt{q'}$ Gauss factor is mandatory.  Together with the DFI
$\sqrt{q'}$ it gives $dq'=q$ and cancels only the finite-Fourier factor
$1/q$, leaving the selector normalization.  The BV harmonic sum over
nonzero $v$ contributes $M^{-3/4}$ per $j$; the zero mode contributes
$M^{-3/4}V+M^{-1/4}$ over a block.  This proves (154.A5) with every
$d,v,j$, sign, endpoint, and outer cost restored.

Finally, full nearest cells partition every positive integer $t$ once.
After the accepted scalar restoration $Q_U=P_U+O_\varepsilon(X^\varepsilon)$,
the negative centered selector row $h=4N-a$ has

$$
 n_*=\frac{4N}{a^2},\qquad
 e(\Psi_*)=e(N/a),\qquad
 \text{symbol }e(1/8)N^{-1/4}\chi _4(a)A_U(4N/a^2).
\tag{154.A14}
$$

The nonstationary pieces, lower symbols, buffers, transitions, tails, and
endpoints are supplied by the accepted Round-152 ledger, not by a new
claim that a standalone van der Corput error is negligible.  Thus the
principal completion is the accepted reciprocal self-return.

## 4. First doubtful or unproved step

The first open theorem is a signed outer-defect estimate for

$$
 \sum_{V<|j|\le2V}\sum_{d\mid N}\sum_v
 \widehat B_j(2dv)K(-v^2,-j;4N/d),
 \qquad J(\log(2X))^A\lesssim V\lesssim K,
\tag{154.A15}
$$

with the normalization in (154.A12), every gcd stratum, the zero mode,
both signs, the literal cell and profile endpoints, and the strict mask.
The coefficient $\widehat B_j(2dv)$ is nonseparable in $j$ and $v$.
Equivalently, after (154.A3), one needs a signed cross-fibre theorem for
$e(-j/(2k))$.

For odd $N$, the quotient character is constant on each fixed-$j$ root
fibre.  Therefore taking absolute values over the outer defects discards
the available sign.  Existing fixed-polynomial, modulus-average,
prime-modulus, square-modulus, sparse-root, and separated-coefficient
theorems do not directly match (154.A15).  This is a checked source
boundary, not a proof that such a theorem cannot exist.

## 5. Terminal review gate and controls

Three independent terminal reviews are GREEN:

- the mathematical review independently reproduces every exact formula,
  power, and endpoint, and requires the full $d\sqrt{q'}$ normalization;
- the hostile review verifies selected versus ambient rows, scalar mask
  order, even/composite/prime controls, both cell endpoints, the direct-wave
  inclusion of large-square-factor terms, and all downstream exclusions;
- the primary-source review verifies DFI Section 6 and Lemma 6.1, its
  official erratum's non-impact, the exact theta multiplier and zero-mode
  ledger, Müllner's auxiliary incomplete-Gauss statement, and the
  Round-152 dependency of the self-return remainder.

The source search is current through 25 August 2026 in the bounded sense
recorded by the review; its bibliography is not claimed exhaustive.  No
numerical experiment was used.  Raw counts, theorem right sides, positive
Cauchy diagonals, and absolute capacities are never treated as signed lower
bounds.

## 6. Dependencies and exact artifacts

The accepted kernel depends on the Round-152 exact/small-defect owner,
strict $M$-range, profile and reciprocal boundary ledger, and on the
Round-153 direct-wave recombination.  Its direct evidence is:

- all three Round-154 reports;
- `conductor_round154_exact_root_defect_reparametrization.md`;
- `conductor_round154_root_dispersion_adjudication.md`;
- `math_conductor_round154_final.md`;
- `hostile_conductor_round154_final.md`;
- `source_conductor_round154_final.md`; and
- the DFI and Müllner primary-source theorem cards in the source audit.

No sibling wording that excludes large-square-factor terms from the direct
$Q_U$ is accepted; that wording was corrected before closure.  No graph,
proof draft, validation matrix, or synthesis was edited by a subagent.

## 7. Recommended state effect

Apply a State Patch that:

1. creates an exact root-defect/logarithmic-collar reduction containing
   (154.A2)--(154.A4), (154.A7), and (154.A10);
2. creates a source-audit node for the exact DFI theta-Kloosterman match and
   its fixed-block bound;
3. creates a route-scoped root-dispersion obstruction containing
   post-selection Cauchy equality, the normalized ambient completion,
   (154.A5), the principal reciprocal self-return, and the open normalized
   signed outer-$j$ theorem;
4. updates the existing D=1 and global lower-radial frontier nodes so the
   first direct-wave survivor has
   $|j|>J(\log(2X))^A$ and may use the linearized phase;
5. rejects every overbroad inference identified in the terminal controls;
   and
6. leaves M9--M1, M9--M2, endpoint uniformity, M9, the bridge, the quarter
   target, the internal exponent $1/3$, and the separately audited external
   Li--Yang exponent unchanged.

