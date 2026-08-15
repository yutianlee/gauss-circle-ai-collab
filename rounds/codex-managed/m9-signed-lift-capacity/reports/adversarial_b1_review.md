# Round 3 hostile review: B1 and its signed-energy capacity

## 1. Result

**B1 survives only after its weight hypothesis is made quantitative.**  The clean
statement is a restricted-lattice bounded-variation lemma.  It covers a sharp
dyadic interval, an endpoint-truncated interval, and a fixed smooth/BV profile
uniformly.  It is false for arbitrary bounded denominator weights.

**B1 alone has insufficient signed-energy capacity.**  It implies only

\[
 \|A_\chi\|_1\ll D\log(2H),\qquad
 \|A_\chi\|_2^2\ll D,
\]

and therefore, by Young's inequality, at best

\[
 \|A_\chi*A_\chi\|_2^2\ll D^3\log^2(2H).
\]

This is a factor (D), up to logarithms, above the desired (D^2X^\epsilon)
pair-energy scale.  More decisively, an even real adversarial coefficient array
satisfying the B1 envelope has smoothed fourth moment

\[
 \gg \frac{D^5}{X}.
\]

After the accepted exact-pair-sum diagonal bound, its off-diagonal term has the
same lower order for (D>X^{1/3+\delta}).  Thus no argument using only the B1
magnitude envelope can prove the signed fat-band target.  This is a capacity
no-go, not a counterexample to the actual Vaaler coefficients.

## 2. Strongest surviving B1 statement

Let (D>0), (H\ge0) be integers where appropriate, (q\ge1), and
(p\in\mathbb Z\setminus\{0\}), with (q>0).  Reducedness of (p/q) is needed
for the project's fraction grouping but not for the estimate.  Put (P=|p|) and

\[
 \mathcal G=\{g\ge1:D\le gq<2D,\ gP\le H,\ 2\nmid g\}.
\]

Order the elements of (mathcal G) as (g_1<\cdots<g_m), and define the
restricted-lattice BV norm

\[
 \mathcal B_{p,q}(w_D)
 :=2\sup_{g\in\mathcal G}|w_D(gq)|
   +\sum_{j<m}|w_D(g_{j+1}q)-w_D(g_jq)|,
\]

with value (0) if (mathcal G) is empty.  Assume
(mathcal B_{p,q}(w_D)\le B).  With the audited coefficient

\[
 \beta_{h,H}=-\frac{\Phi(|h|/(H+1))\chi_4(|h|)}{\pi|h|}
 \mathbf 1_{2\nmid h},
\]

one has

\[
 A_\chi(p/q)=0\quad(2\mid p),
\]

and, for odd (p),

\[
 \boxed{
 |A_\chi(p/q)|
 \le \frac{B}{\pi P}\min\!\left(1,\frac qD\right)
 \le \frac{Bq}{\pi DP}.}
 \tag{B1-BV}
\]

The implied constant is uniform in a short or one-point truncation interval.
Uniform discrete BV of (d\mapsto w_D(d)) is sufficient, since restriction to
the progression (q\mathbb Z) cannot increase total variation.  A fixed
profile (w_D(d)=W(d/D)), with

\[
 \|W\|_\infty+\operatorname{Var}_{[1,2]}W=O(1),
\]

also satisfies the hypothesis.  This includes fixed (C^1) profiles.  A sharp
interval, or a fixed profile multiplied by one endpoint truncation, has (B=O(1)).
The phrase "bounded smooth weight" is not sufficient unless these scaled norms
are uniform in (D).

### Proof

Even (p) makes every (gp) even, so every beta coefficient vanishes.  For odd
(p), only odd (g) contribute and complete multiplicativity gives

\[
 A_\chi(p/q)
 =-\frac{\chi_4(P)}{\pi P}
 \sum_{g\in\mathcal G}\chi_4(g),
 \frac{\Phi(gP/(H+1))}{g},w_D(gq).
 \tag{1}
\]

Along the ordered odd integers, (chi_4(g)) alternates, so every partial sum has
absolute value at most (1).  Vaaler's source card gives that (Phi) is
nonnegative and decreasing on ([0,1]).  Hence

\[
 b_g:=\frac{\Phi(gP/(H+1))}{g}
\]

is nonnegative and decreasing on (mathcal G).  Abel summation and the product
variation inequality give

\[
 \left|\sum_{g\in\mathcal G}\chi_4(g)b_gw_D(gq)\right|
 \le b_{g_1}\mathcal B_{p,q}(w_D).
\]

If (q\le D), then (g_1\ge D/q), while if (q>D), then (g_1\ge1).  Since
(0\le\Phi\le1),

\[
 b_{g_1}\le\frac1{g_1}
 \le\min\!\left(1,\frac qD\right).
\]

Substitution in (1) proves (B1-BV).  The exact cutoff (gP\le H) only shortens
the consecutive odd interval and creates no loss.  No derivative estimate for
(Phi) is needed beyond its audited monotonicity.  \(\square\)

## 3. Seam-by-seam hostile audit

### 3.1 Arbitrary bounded weights: reject

The B1 envelope is false under (|w_D|_\infty\le1) alone.  Take a large integer
(H\) divisible by (4), set

\[
 X=H^4,\qquad D=H^2=X^{1/2},\qquad q=4H,\qquad p=1,
\]

and prescribe, on the relevant multiples,

\[
 w_D(qg)=\chi_4(g)
 \quad\left(H/4\le g<H/2,\ 2\nmid g\right),
\]

with (w_D=0) elsewhere.  Then (gq\in[D,2D)), (g\le H), and

\[
 |A_\chi(1/q)|
 =\frac1\pi\sum_{\substack{H/4\le g<H/2\\2\nmid g}}
 \frac{\Phi(g/(H+1))}{g}
 \ge c>0,
\]

because (Phi(u)\ge\Phi(1/2)=1/2) for (u\le1/2).  The proposed right side is
(q/D=4/H\to0).  The weight has variation (asymp H), pinpointing the missing
hypothesis: it cancels the (chi_4(g)) oscillation.

### 3.2 Sharp, fixed smooth, and BV weights: accept with uniform norms

The proof of (B1-BV) covers all three.  For a sharp shell the sampled weight is
constant.  For (W(d/D)), its variation along (d=qg) is at most
(operatorname{Var}W).  A uniform discrete BV sequence is equally sufficient.
If the BV norm grows with (D), the bound carries that growth and the stated
(O(q/(DP))) conclusion need not hold.

### 3.3 Short truncations and support edges: accept

The exact nonempty condition is the existence of an odd (g) with

\[
 D\le gq<2D,\qquad gP\le H.
\]

It implies (q<2D), (P\le Hq/D), and (q\ge DP/H) when (H>0).  If
(q\ge2D), the sum is empty.  If (D\le q<2D), only (g=1) can occur; B1 is
then a trivial single-lift estimate and is sharp in order.  Empty, one-point,
parity-hole, and (gP=H) endpoint ranges are all covered by the same Abel
argument.  If (H=0) the sum is empty; if (H=1), only the generic single-lift
(p=\pm1) case can occur.

### 3.4 Parity and (p/q) edges: accept

- Even (p): (A_\chi=0) exactly.
- Odd (p): only odd (g) remain, and their (chi_4(g)) signs alternate.
- Negative (p): beta is even, so (A_\chi(-p/q)=A_\chi(p/q)).
- There is no extra (q)-parity condition.
- Reducedness introduces no analytic loss; it only removes candidate fractions.

### 3.5 Dyadic powers: B1 is uniform, but its useful range is structured

With (H\asymp DX^{-1/4}), the three requested scales are

| (D) | (H) | maximal lift gain near (q\asymp D/H) | generic (q\asymp D) |
|---|---:|---:|---:|
| (X^{1/3}) | (X^{1/12}) | (q/D\asymp X^{-1/12}) | no gain |
| (X^{3/8}) | (X^{1/8}) | (q/D\asymp X^{-1/8}) | no gain |
| (X^{1/2}) | (X^{1/4}) | (q/D\asymp X^{-1/4}) | no gain |

Thus B1 is a genuine small-(q), many-lift estimate.  It gives no cancellation
on (q\in[D,2D)), where (g=1) and the accepted W-1 obstruction lives.

### 3.6 Unsigned and adversarial coefficient controls: required failure occurs

Replace (eta_g) by (|\beta_g|) and use the sharp weight in the construction
of Section 3.1.  Then the lift sum is again (gg1), whereas (q/D=4/H).  Thus
B1 does **not** prove the unsigned analogue: the (chi_4(g)) alternation is its
essential input.

Conversely, on the generic band (q\asymp D) there is only (g=1); signed and
unsigned envelopes coincide in size.  Hence B1 cannot bypass the character-blind
W-1 obstruction there.

## 4. What B1 alone implies for energy

Ignoring reducedness and parity only enlarges the sums.  The support condition
gives (q<2D) and (P\le Hq/D).  From B1,

\[
\begin{aligned}
 \sum_{p/q}|A_\chi(p/q)|
 &\ll \frac1D\sum_{q<2D}q
        \sum_{1\le P\le Hq/D}\frac1P
 \ll D\log(2H),\\
 \sum_{p/q}|A_\chi(p/q)|^2
 &\ll \frac1{D^2}\sum_{q<2D}q^2
        \sum_{P\ge1}\frac1{P^2}
 \ll D.
\end{aligned}
\]

Both orders are saturated, up to logarithms, by generic single-lift fractions.
For the pair function (R=A_\chi*A_\chi), Young gives

\[
 \sum_s|R(s)|^2
 \le \|A_\chi\|_1^2\|A_\chi\|_2^2
 \ll D^3\log^2(2H).
 \tag{2}
\]

The desired energy is (D^2X^\epsilon).  B1 therefore leaves an entire factor
(D) to be won by a correlation statement not present in the pointwise
envelope.

### Envelope-saturating signed adversary

The failure is not just an inefficient application of Young.  Let (V\ge0) be
the fixed global-moment weight, with (V=1) on ([1,2]), and define

\[
 F_A(t)=\sum_x A(x)e(tx/4).
\]

Average over (t_0\in[5X/4,7X/4]).  Since the period of
(|\cos(\pi t/(2q))|) is (2qll X), there is a (t_0) for which

\[
 \sum_{D\le q<2D}\left|\cos\frac{\pi t_0}{2q}\right|\gg D.
\]

Choose an even real coefficient array

\[
 A(1/q)=A(-1/q)
 =a\,\operatorname{sgn}\!\left(\cos\frac{\pi t_0}{2q}\right)
 \quad(D\le q<2D),
\]

and (A=0) elsewhere, where (a>0) is a sufficiently small fixed constant.
This array obeys parity, evenness, support, and the B1 magnitude envelope because
(q/D\asymp1).  At (t=t_0),

\[
 |F_A(t_0)|
 =2a\sum_{D\le q<2D}\left|\cos\frac{\pi t_0}{2q}\right|
 \gg aD.
\]

Moreover,

\[
 |F_A'(t)|\le a\pi\sum_{D\le q<2D}\frac1q\ll a,
\]

so this lower bound persists on an interval of length (gg D), contained in
the plateau of (V(t/X)).  Consequently

\[
 \boxed{
 \frac1X\int V(t/X)|F_A(t)|^4\,dt
 \gg a^4\frac{D^5}{X}.}
 \tag{3}
\]

The accepted exact pair-sum arithmetic bounds the diagonal for this magnitude
class by (O_\epsilon(D^2X^\epsilon)).  Thus the off-diagonal term in the exact
smoothed identity is

\[
 \gg \frac{D^5}{X}-O_\epsilon(D^2X^\epsilon).
\]

For (D\ge X^{1/3+\delta}), choose (epsilon<3\delta); this is power-larger than
(D^2X^\epsilon).  At the requested scales, the ratio of (3) to (D^2) is

| (D) | (D^3/X) | verdict |
|---|---:|---|
| (X^{1/3}) | (1) | target-scale only; no power contradiction |
| (X^{3/8}) | (X^{1/8}) | B1-only implication fails by a power |
| (X^{1/2}) | (X^{1/2}) | B1-only implication fails by a power |

This adversary is intentionally not claimed to be the actual fixed-profile
Vaaler array.  It proves the precise logical point: an estimate depending only
on (|A(p/q)|\ll q/(D|p|)), parity, support, and evenness cannot prove the signed
fat-band estimate.  A successful proof must use an additional correlation law
for the actual signs/weights on the generic band.

## 5. First doubtful or unproved step

There is no doubtful step in (B1-BV) once the uniform restricted-lattice BV norm
is assumed and Vaaler's audited monotonicity of (Phi) is imported.  The first
unproved project step is instead the transfer to the **actual** dyadic weights:
the draft says only "bounded smooth dyadic partition" and does not specify a
uniform scaled BV norm, top-block truncation rule, or fixed profile.

For the energy route, the first missing step is much larger: one needs a theorem
showing cancellation among generic single-lift fractions (q\asymp D) in the
kernel-weighted pair sum.  B1 contains no such information.  Neither a
pointwise lift envelope nor the global fourth moment, even if bounded, closes
the separate average-to-pointwise obligation.

## 6. Controls and outcomes

No numerical experiment was used.

| Control | Exact input | Expected invariant/failure | Outcome | Implication |
|---|---|---|---|---|
| signed-vs-unsigned | sharp weight, (p=1,q=4H,D=H^2) | signed lift cancels; unsigned lift does not | pass | (chi_4(g)) is essential to B1 |
| coefficient-adversary | even real envelope-saturating (A(\pm1/q)) | B1 alone must not control signed energy | pass via (3) | B1 has insufficient energy capacity |
| support-and-degeneracy | empty, one-lift, parity-hole, (gP=H), endpoint-truncated intervals | uniform estimate or exact zero | pass analytically | no hidden short-range loss |
| proves-too-much | arbitrary bounded (w_D(qg)=\chi_4(g)) | an overbroad B1 statement should fail | pass: explicit counterexample | require uniform lattice BV |
| dyadic endpoints | (D=X^{1/3},X^{3/8},X^{1/2}) | expose power crossover | pass | no B1-only power obstruction exactly at (1/3); failure above it |

## 7. Dependencies and exact artifacts used

- `sources/vaaler_1985.md`: exact beta normalization; positivity, monotonicity,
  and endpoint values of (Phi).
- `state/proof_obligations.yml`: authoritative statuses and the B1, signed
  fat-band, exact-pair-sum, character, and pointwise obligations.
- `state/control_models.md`: signed/unsigned, coefficient-adversary,
  support/degeneracy, and proves-too-much controls.
- `state/best_proof_draft.md`: exact (S_2), B1, global-moment, and endpoint
  normalizations.
- `rounds/obligation-main/round_008/responses/A4-008.md`: claimant B1 proof and
  proposed (c_\chi) identity.
- `rounds/obligation-main/round_008/reviews/A1.md`: prior seam warnings and
  generic-band scope.
- `rounds/codex-managed/m9-unit-frequency-w1-validation/synthesis.md`: accepted
  absolute W-1 obstruction and (X^{1/3}) crossover.

## 8. Recommended state effect

1. **Revise/retain B1.**  Replace "suitable smooth or bounded-variation weights"
   by (B1-BV), or by the sufficient fixed-profile hypothesis
   (w_D(d)=W(d/D)) with a uniform (|W|_\infty+\operatorname{Var}W) bound.
   Keep the claim conditional until the actual block profiles and endpoint rule
   are checked.  Record the arbitrary-bounded-weight counterexample.
2. **Reject `B1 implies signed fat-band energy`.**  Record the capacity no-go:
   B1 alone permits (D^5/X) fourth-moment energy and gives only the norm bound
   (2).  Do not promote `M9-M2-signed-fat-band-constant` from B1.
3. **No change** to `M9-M2`, `M9`, the pointwise bridge, or the theorem target.
   The next signed lemma must act on the generic (q\asymp D) band and state an
   actual sign-correlation mechanism that fails for the adversarial array above.

