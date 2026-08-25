# Round 155 conductor adjudication

- Campaign: m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate
- Round: 155
- Starting graph SHA-256: 84bbcb3413936c9b672c829cdba97b8d0bde69f7a6df677b61f24e9ec27e243a
- Terminal label: outer_defect_theta_dispersion_no_go
- Terminal reviews: inverse-Gauss mathematics GREEN; primary-source GREEN; hostile scope and promotion GREEN
- Allocation: 100% analytic, algebraic, and primary-source work; 0% numerical

## 1. Result

Round 155 proves an exact route obstruction but no signed outer-defect
estimate. Complete half-period resummation of the dual theta frequency is
the inverse of the Round-154 quadratic Gauss completion and returns the
literal quotient selector, with every imprimitive stratum and endpoint
retained. It supplies no second square-root gain.

Fix $A>0$ and put

$$
 J_A=M^{3/4}(\log(2X))^A,\qquad K=\sqrt{NM},\qquad
 J_A<V\le K.
\tag{155.A1}
$$

For $q=4N$, every odd $d\mid N$, $c=q/d$, and $H=c/2$, the exact
ambient coefficient satisfies

$$
 \boxed{
 \begin{aligned}
 &\sum_{v\bmod H}\widehat B_j(2dv)K(-v^2,-j;c)\\
 &\quad=\frac{1-i}{2}\sqrt c
 \sum_{x\bmod q}B_j(x)
 \sum_{a\bmod c}^{*}\chi_4(a)e_c(a(x^2-j)).
 \end{aligned}}
\tag{155.A2}
$$

After multiplication by the exact exterior factor and summation over
$d$, this is precisely

$$
 -\frac{i}{2N}
 \sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}
 \chi_4(h)e_{4N}(h(x^2-j)),
\tag{155.A3}
$$

the original odd-quotient selector. No full target, positive-power defect
range, new $M$-range, downstream theorem, or exponent follows.

## 2. Exact statement and owner scope

The selected object remains

$$
 \mathcal Q_U(V)=
 \sum_{\substack{k\ge1,\ -k\le j\le k-1\\
 V<|j|\le2V,\ N\mid k^2-j\\
 (k^2-j)/N\ \mathrm{odd}}}
 \chi_4\!\left(\frac{k^2-j}{N}\right)
 w_U\!\left(\frac{k^2-j}{N}\right)e\!\left(-\frac j{2k}\right).
\tag{155.A4}
$$

The accepted linearization is charged only on this selected graph. The
coefficient $B_j$ in (155.A2) is the exact pre-linearization ambient
coefficient: it retains the residual phase, literal zero extension,
actual support components and transitions, strict dyadic mask, asymmetric
cell, both signs, and every hard endpoint. The external $B_{1,U}(1)$
factor remains outside the scalar.

The ordinary-K calculation in the statement-only report is accepted only
as a blind surrogate and invertibility control. It is not imported as the
project's theta multiplier or normalization. No selected-row identity is
moved to the ambient array, and no nonseparable coefficient is replaced by
separated bounded weights.

## 3. Verified proof kernel and power ledger

For a unit $a\bmod c$, define

$$
 I_c(a,x)=\sum_{v\bmod H}e_c(-\bar a v^2-2xv).
\tag{155.A5}
$$

The summand has exact period $H$. Square completion and the all-parity
even Gauss formula give

$$
 I_c(a,x)=\frac{1-i}{2}
 \epsilon_a\left(\frac ca\right)\sqrt c\,e_c(ax^2).
\tag{155.A6}
$$

Since the theta multiplier squares to $\chi_4(a)$, (155.A2) follows.
The constant restoration is

$$
 -\frac{i(1+i)}{2Nq}d\sqrt c\,
 \frac{1-i}{2}\sqrt c
 =-\frac{i}{2N}\frac{dc}{q}=-\frac{i}{2N}.
\tag{155.A7}
$$

The decomposition $d=(h,N)$, $h=da$ partitions all odd residues even
when $d$ and $N/d$ are not coprime, proving (155.A3) for arbitrary
$N$.

For every later norm placement, sampled Parseval is exactly

$$
 \sum_{v\bmod H}|\widehat B_j(2dv)|^2
 =H\sum_{r\bmod H}|C_{j,d}(r)|^2,\qquad
 C_{j,d}(r)=\sum_{\substack{x\bmod q\\x\equiv r\pmod H}}B_j(x).
\tag{155.A8}
$$

Thus the collision period is $2N/d$, including every large-$d$ fold, and

$$
 \sum_{v\bmod H}|\widehat B_j(2dv)|^2
 \ll_\varepsilon
 \left(\frac{N^{3/2}}{dM}+\frac{N}{M^{1/2}}\right)X^\varepsilon.
\tag{155.A9}
$$

This is an upper capacity, not defect orthogonality. The mandatory zero
row satisfies

$$
 |\mathcal T_{0,U}(V)|\ll_\varepsilon
 \left(N^{-1/2}M^{-1/4}V+M^{-1/4}\right)X^\varepsilon,
\tag{155.A10}
$$

which is $M^{1/4}+M^{-1/4}$ at $V=K$. It is not a lower bound. The
nonzero termwise ledger remains $M^{-3/4}VX^\varepsilon$.

For a proper cutoff $\eta$, exact completion instead produces

$$
 \sum_{v\bmod H}\eta(v)e_c(-\bar a v^2-2xv)
 =e_c(ax^2)\sum_{u\bmod H}\eta(u-ax)e_c(-\bar a u^2).
\tag{155.A11}
$$

The translated cutoff remains coupled in $a$ and $x$. This is a route
obstruction only; a future structured incomplete transform is not ruled
out.

A hypothetical square-root gain over the selected defect incidences has
size $M^{-3/4}V^{1/2}X^\varepsilon$, target-sized only for
$V\le M^{3/2}$. No report proves that cancellation. At $V=K$ its size
is $N^{1/4}M^{-1/2}$, so it closes the top only at the hard boundary
$M\asymp N^{1/2}$.

Finally, the flat selected phase varies by only $O(V/K)\le O(1)$.
Expanding the exact theta phase localizes at most to the circular arc

$$
 \left\|\frac ac+\frac1{2\sqrt{x^2-j}}\right\|_{\mathbb R/\mathbb Z}
 \ll\frac1V,
\tag{155.A12}
$$

of capacity $O(1+c/V)$. The arc wraps through zero and contains both a
near-zero piece and the negative-frequency piece near $c-c/(2x)$. This
is localization, not cancellation.

## 4. First doubtful or unproved step

The first source-unproved row in a route that separates nonzero
frequencies is

$$
 \sum_{V<|j|\le2V}\widehat B_j(0)K(0,-j;4N/d),
\tag{155.A13}
$$

uniformly for every odd $d\mid N$, both signs, the actual profile, and
all endpoints. If this zero row is resolved, the next missing input is a
signed estimate for the incomplete nonzero matrix with
$\widehat B_j(2dv)$, or equivalently the selected bounded-variation seam

$$
 \sup_{I\subset\{n\asymp M\}}
 \left|\sum_{\substack{n\in I,\ n\ \mathrm{odd}\\
 V<|j_n|\le2V}}\chi_4(n)e(\sqrt{Nn})\right|
 \ll_\varepsilon M^{3/4}X^\varepsilon.
\tag{155.A14}
$$

Neither is proved. A complete proof must also retain every $d$, zero
and complementary mode, principal or exceptional spectral term, large-
$d$ fold, both signs, endpoints, and the external coefficient seam, and
must supply a second gain above $V=M^{3/2}$ when $M<N^{1/2}$.

## 5. Terminal review gate and controls

Three independent terminal reviews are GREEN:

- the mathematics review independently proves the half-period identity,
  multiplier sign, $dc=q$ cancellation, arbitrary-$N$ gcd partition,
  sampled Parseval folds, zero-mode powers, and both branches of the
  circular arc;
- the source review verifies DFI Section 6 and Lemma 6.1 term by term,
  the DFI erratum scope, the exact DFI/Sun modulus-average and nonzero-
  frequency hypotheses, the Lam coefficient class, and the fixed-modulus
  ordinary or prime-kernel mismatches; and
- the hostile review verifies that the blind ordinary-K surrogate is not
  imported, every upper capacity remains an upper bound, the hypothetical
  threshold is not promoted, and all downstream and exponent claims are
  excluded.

The source search is cutoff-checked through 25 August 2026. The source
review's two precision qualifications have been incorporated: DFI's
weakened Theorem-2.5 option retains $g(0)=g'(0)=0$, and Sun's Theorem
3.3 is directly stated for weights $1/2$ and $3/2$. These strengthen
the no-match and change no power. The search is not claimed exhaustive.

## 6. Dependencies and exact artifacts

The accepted kernel depends on the Round-154 exact root-defect cell,
selected-only linearization, logarithmic collar, and fully normalized
theta completion. Its direct Round-155 evidence is:

- all three assigned reports;
- conductor_round155_complete_v_inverse_gauss.md;
- conductor_round155_theta_dispersion_adjudication.md;
- independent_inverse_gauss_math_review.md;
- independent_spectral_source_review.md; and
- hostile_conductor_round155_final.md.

No computation or numerical experiment certifies an asymptotic claim.
No subagent edited the proof graph, proof draft, validation matrix,
synthesis, or State Patch.

## 7. Recommended state effect

Apply a State Patch that:

1. creates a route-scoped complete-theta inverse-Gauss obstruction
   containing (155.A2)--(155.A12);
2. creates a joint spectral-source audit recording DFI as termwise only
   and the current fixed-modulus nonseparable family as a direct no-match;
3. updates the existing D=1 outer-defect frontier so (155.A13), followed
   by (155.A14), are the first missing signed inputs;
4. rejects deletion of the zero row, a second gain from complete
   resummation, physical-diagonal-only Parseval, separated surrogate
   coefficients, automatic flat-$j$ cancellation, and promotion of the
   hypothetical $V\le M^{3/2}$ capacity; and
5. leaves the $M^{449}\asymp R^{780}$ boundary, every other M1 and M2
   owner, endpoint uniformity, M9, the bridge, the quarter target, the
   internal exponent $1/3$, and the separately audited external
   Li--Yang exponent unchanged.

