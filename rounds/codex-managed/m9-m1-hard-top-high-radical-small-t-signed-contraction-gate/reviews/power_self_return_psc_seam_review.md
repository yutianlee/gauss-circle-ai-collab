# Round 183 power, self-return, and PSC seam review

- Campaign: `m9-m1-hard-top-high-radical-small-t-signed-contraction-gate`
- Round: `183`
- Role: independent hostile power reviewer
- Starting graph SHA-256:
  `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`
- Evidence status: review evidence only; no shared proof-state edit
- Verdict: **GREEN for the strict primitive-ray sector and the scoped
  truncated-Mobius self-return; no owner or PSC promotion**

## 1. Result and verdict

The power arithmetic and exact finite identities survive independent
rederivation.

1. The two-cutoff kernel is exactly
   \[
    K_{L,T}(b,u)=
    \sum_{\substack{a\mid u\\a^2b>L\\u/a<T}}\mu(a),
    \qquad T=\lceil\sqrt L\rceil .
   \]
   On (b>L, u<T), it is \(\mathbf 1_{u=1}\).  The complementary
   regions (b\le L) and (b>L, u\ge T) each have
   (O_\varepsilon(L^{3/2}X^\varepsilon)) mass.  Hence the frozen
   small-(t) scalar is the full literal product wave modulo a target-safe
   correction.
2. Splitting the original Mobius divisor at (a<T) and (a\ge T) does
   not improve this.  The (a\ge T) tail is absolutely
   \(O_\varepsilon(L^2/T)\), while the (a<T) kernel still equals
   \(\mathbf 1_{u=1}\) on (b>L, u<T).  Thus the small-(a) core is
   again the full product wave modulo target-safe corrections.
3. The fixed-row Fejer/van der Corput inequality, including its constants,
   diagonal, literal support intersection, phase, and restored (t)-sum,
   is correct.  It gives a sufficient (N_t^{3/4}) row theorem from one
   signed Fejer correlation-energy estimate.  That estimate is unproved
   already for (t=1), is stronger than the frozen aggregate owner, and
   is not a replacement owner.
4. The direct report's primitive-ray threshold is power-correct.  The
   general ray count is
   (O((1+L/G_0)^2)); (G_0=\lceil L^{1/4}\rceil) makes this
   (O(L^{3/2})).  Given the separately reviewed literal step-two BV
   bound, the nonresonant ray sum is therefore target-sized.  Its absolute
   incidence capacity is only bounded by (O(L^2/G_0)=O(L^{7/4})), so
   this is a genuine signed strict-sector theorem, not a proof of the
   complete (L^2)-capacity owner.

The first failed seams are exact: the (a=t=u=1) term in the truncated
Mobius core, the unproved signed Fejer brace at (t=1), and the direct
sector's explicit complement (G<G_0) or half-integer near resonance.
The full Round-183 target remains open.

One comparison must be read with scale precision.  The new fixed-row
deficit has the same **structural** (H/L) form as the old PSC deficit
when evaluated on the same hard-top shell.  The old Round-70
delta/Kloosterman packet used a different benchmark and recorded the
numerical loss (X^{1/20}); the present critical shell
(L\asymp X^{1/6}) records (X^{1/12}).  No old delta-method no-go is
being imported as a theorem about the new correlation.

## 2. Exact statement and hypotheses

Fix one literal middle or lower residual shell, one sign
\(\sigma\in\{+1,-1\}\), and real (X\ge2).  Put

\[
 F_\sigma(r)=C_{L,X}^{\sigma}(r)e(\sigma\sqrt{Xr}),
 \qquad T=\lceil\sqrt L\rceil .
\]

The coefficient is the exact zero-extended literal coefficient from the
campaign.  The accepted product support and divisor estimate give, after
epsilon relabelling,

\[
 F_\sigma(r)\ne0\Longrightarrow c_-L^2\le r\le c_+L^2,
 \qquad |F_\sigma(r)|\ll_\varepsilon X^\varepsilon,
 \tag{2.1}
\]

for fixed profile constants (c_-,c_+>0).  Every count below is an upper
count; it does not assert lower mass for the literal coefficient.  The
case (T=1) has an empty frozen small-(t) sum and is target-trivial, so
the identities involving (u=1) may be read under (T\ge2).

For a fixed nonempty row (1\le t<T), define on all integers

\[
 z_{t,\sigma}(s)=\mathbf1_{s>L}\mu^2(s)
 C_{L,X}^{\sigma}(st^2)e(\sigma t\sqrt{Xs}),
 \tag{2.2}
\]

zero outside the exact literal support.  Let (I_t=[A_t,B_t]\cap\mathbb Z)
be a consecutive interval containing that support and let
(N_t=B_t-A_t+1).  Then

\[
 N_t\ll 1+\frac{L^2}{t^2}\ll\frac{L^2}{t^2}
 \qquad(1\le t<T).
 \tag{2.3}
\]

The last absorption is valid because (t<T\ll\sqrt L+1), while the
bounded cases are harmless.

## 3. Independent derivation

### 3.1 The exact two-cutoff Mobius kernel

For the frozen scalar

\[
 \mathcal A_{L,\sigma}^{\rm st}
 =\sum_{\substack{s>L\\\mu^2(s)=1}}
   \sum_{1\le t<T}F_\sigma(st^2),
 \tag{3.1}
\]

insert \(\mu^2(s)=\sum_{a^2\mid s}\mu(a)\), write (s=a^2b), and only
then put (u=at).  Finiteness follows from zero extension.  This gives

\[
 \begin{aligned}
 \mathcal A_{L,\sigma}^{\rm st}
 &=\sum_{\substack{a,b,t\ge1\\a^2b>L\\t<T}}
   \mu(a)F_\sigma(b(at)^2)\\
 &=\sum_{b,u\ge1}K_{L,T}(b,u)F_\sigma(bu^2),
 \end{aligned}
 \tag{3.2}
\]

where

\[
 K_{L,T}(b,u)=
 \sum_{\substack{a\mid u\\a^2b>L\\u/a<T}}\mu(a).
 \tag{3.3}
\]

The inequalities are strict for different reasons: (a^2b=L) is outside
the high-radical owner, and (u/a<T) is exactly the integer condition
(t\le T-1).  Equivalently, admitted divisors satisfy

\[
 a>\max\!\left(\sqrt{L/b},\frac uT\right),\qquad a\mid u.
 \tag{3.4}
\]

If (b>L) and (u<T), every divisor (a\mid u) passes both tests.  Thus

\[
 K_{L,T}(b,u)=\sum_{a\mid u}\mu(a)=\mathbf1_{u=1}.
 \tag{3.5}
\]

In particular, for (T\ge2),

\[
 K_{L,T}(b,1)=\mathbf1_{b>L}.
 \tag{3.6}
\]

This (u=1) term is the full (a=t=1) product wave.  It is larger as an
individual expanded term than the squarefree (t=1) face; the other
Mobius representations cancel its nonsquarefree products when the exact
original sum is reconstructed.  It therefore cannot be discarded as a
target-safe remainder.

### 3.2 Exact partition and every correction power

Using (3.5), partition (3.2) disjointly as

\[
 \begin{aligned}
 \mathcal A_{L,\sigma}^{\rm st}
 ={}&\sum_{b>L}F_\sigma(b)\\
 &+\sum_{\substack{b\le L\\u\ge1}}
 K_{L,T}(b,u)F_\sigma(bu^2)\\
 &+\sum_{\substack{b>L\\u\ge T}}
 K_{L,T}(b,u)F_\sigma(bu^2).
 \end{aligned}
 \tag{3.7}
\]

Since \(|K_{L,T}(b,u)|\le\tau(u)\), (2.1) gives

\[
 \sum_{b\le L}\#\{u:F_\sigma(bu^2)\ne0\}
 \ll\sum_{b\le L}\left(1+\frac L{\sqrt b}\right)
 \ll L^{3/2},
 \tag{3.8}
\]

and

\[
 \sum_{u\ge T}\#\{b>L:F_\sigma(bu^2)\ne0\}
 \ll L^2\sum_{u\ge T}u^{-2}
 \ll\frac{L^2}{T}\ll L^{3/2}.
 \tag{3.9}
\]

Divisor factors are absorbed into (X^\varepsilon).  If

\[
 \mathcal P_{L,\sigma}=\sum_{r\ge1}F_\sigma(r),
\]

then

\[
 \sum_{b>L}F_\sigma(b)
 =\mathcal P_{L,\sigma}-\sum_{b\le L}F_\sigma(b),
 \qquad
 \sum_{b\le L}|F_\sigma(b)|\ll_\varepsilon LX^\varepsilon.
 \tag{3.10}
\]

Consequently

\[
 \boxed{
 \mathcal A_{L,\sigma}^{\rm st}
 =\mathcal P_{L,\sigma}
 +O_\varepsilon(L^{3/2}X^\varepsilon).}
 \tag{3.11}
\]

The transformed (u\ge T) term in (3.9) is paid once inside this
regrouping.  It is not an additional copy of the already accepted original
(t\ge T) sector.

### 3.3 The (a<T) truncation also self-returns

Split (3.2) before introducing (u):

\[
 \begin{aligned}
 \mathcal A_{<T}
 &=\sum_{\substack{a<T,\ b\ge1,\ 1\le t<T\\a^2b>L}}
 \mu(a)F_\sigma(b(at)^2),\\
 \mathcal A_{\ge T}
 &=\sum_{\substack{a\ge T,\ b\ge1,\ 1\le t<T\\a^2b>L}}
 \mu(a)F_\sigma(b(at)^2).
 \end{aligned}
 \tag{3.12}
\]

Support (2.1) leaves (O(L^2/(a^2t^2))) possible positive (b)'s.
Therefore

\[
 |\mathcal A_{\ge T}|
 \ll_\varepsilon X^\varepsilon L^2
 \sum_{a\ge T}a^{-2}\sum_{t\ge1}t^{-2}
 \ll_\varepsilon \frac{L^2}{T}X^\varepsilon
 \ll_\varepsilon L^{3/2}X^\varepsilon.
 \tag{3.13}
\]

After (u=at), the other kernel is

\[
 K_{L,T}^{<}(b,u)=
 \sum_{\substack{a\mid u\\a<T\\a^2b>L\\u/a<T}}\mu(a).
 \tag{3.14}
\]

For (b>L, u<T), every divisor (a\mid u) also satisfies (a<T), so

\[
 K_{L,T}^{<}(b,u)=\mathbf1_{u=1}.
 \tag{3.15}
\]

The same disjoint partition and the same counts (3.8)--(3.10) now yield

\[
 \boxed{
 \mathcal A_{<T}=\mathcal P_{L,\sigma}
 +O_\varepsilon(L^{3/2}X^\varepsilon),\qquad
 \mathcal A_{\ge T}\ll_\varepsilon L^{3/2}X^\varepsilon.}
 \tag{3.16}
\]

Thus a target-scale cutoff discards a safe tail but does not create a
smaller signed core.  The obstruction is exact and mechanism-scoped; it
does not refute the literal owner.

### 3.4 Exact fixed-row Fejer/van der Corput connector

Fix a nonempty row, abbreviate (z=z_{t,\sigma}), (I=I_t), and
(N=N_t).  For (1\le Q\le N), extend (z) by zero and set

\[
 B_m=\sum_{j=0}^{Q-1}z(m+j),
 \qquad A_t-Q+1\le m\le B_t.
\]

Every (z(s)) occurs in exactly (Q) blocks and there are (N+Q-1)
blocks.  Cauchy and exact expansion therefore give

\[
 Q^2\left|\sum_s z(s)\right|^2
 \le (N+Q-1)\sum_m|B_m|^2,
 \tag{3.17}
\]

\[
 \frac1Q\sum_m|B_m|^2
 =R_{t,\sigma}(0)+2\Re\sum_{1\le q<Q}
 \left(1-\frac qQ\right)R_{t,\sigma}(q),
 \tag{3.18}
\]

where

\[
 R_{t,\sigma}(q)=
 \sum_{s\in I_t\cap(I_t-q)}z_{t,\sigma}(s+q)
 \overline{z_{t,\sigma}(s)}.
 \tag{3.19}
\]

Substitution of (2.2) gives the exact coefficient and phase

\[
 \begin{aligned}
 R_{t,\sigma}(q)=\sum_s&\mathbf1_{s>L}\mathbf1_{s+q>L}
 \mu^2(s)\mu^2(s+q)\\
 &\times C_{L,X}^{\sigma}((s+q)t^2)
 \overline{C_{L,X}^{\sigma}(st^2)}\\
 &\times e\!\left(\sigma t\sqrt X
 (\sqrt{s+q}-\sqrt s)\right),
 \end{aligned}
 \tag{3.20}
\]

with the sum restricted by both zero-extended literal supports.  On
expanding both coefficients, each incidence satisfies

\[
 h_1n_1-h_0n_0=t^2q
 \tag{3.21}
\]

and carries both squarefree indicators, both characters, and the product
of the two literal symbols.  No endpoint completion or phase linearization
has occurred.

Take (Q=Q_t=\lceil\sqrt{N_t}\rceil).  Then (Q_t\le N_t) and

\[
 \frac{N_t+Q_t-1}{Q_t}\le2\sqrt{N_t}.
 \tag{3.22}
\]

The diagonal is exactly

\[
 R_{t,\sigma}(0)=\sum_s\mu^2(s)
 |C_{L,X}^{\sigma}(st^2)|^2
 \ll_\varepsilon N_tX^\varepsilon.
 \tag{3.23}
\]

Hence the still-unproved single signed estimate

\[
 R_{t,\sigma}(0)+2\Re\sum_{1\le q<Q_t}
 \left(1-\frac q{Q_t}\right)R_{t,\sigma}(q)
 \ll_\varepsilon N_tX^\varepsilon
 \tag{3.24}
\]

implies

\[
 |S_{t,\sigma}|\ll_\varepsilon N_t^{3/4}X^\varepsilon
 \ll_\varepsilon L^{3/2}t^{-3/2}X^\varepsilon.
 \tag{3.25}
\]

The brace in (3.24) is nonnegative because it equals
(Q_t^{-1}\sum_m|B_m|^2).  Importantly, (3.24) does not take separate
absolute values over (q); the blind report's modulus-summed version is a
valid but strictly stronger sufficient input.  Finally,

\[
 \sum_{1\le t<T}|S_{t,\sigma}|
 \ll_\varepsilon L^{3/2}X^\varepsilon
 \sum_{t\ge1}t^{-3/2}
 \ll_\varepsilon L^{3/2}X^\varepsilon.
 \tag{3.26}
\]

Thus the connector is exact, including (t=1), but the rowwise triangle
makes it strictly stronger than the one-absolute-value frozen owner.

### 3.5 Primitive-ray threshold and ray-count audit

For a literal incidence write (h=Gu,n=Gv), with
((u,v)=1), (v) odd, and (4u<v<16u).  The canonical squarefree
coordinates are

\[
 s=\operatorname{sf}(uv),\qquad
 t=G\sqrt{uv/s}.
 \tag{3.27}
\]

If a ray with (G\ge G_0) is nonempty, the literal shell (Gu\asymp L)
forces (u\ll L/G_0), and then (v\asymp u).  Therefore

\[
 \#\{(u,v):\hbox{a nonempty such ray}\}
 \ll\sum_{u\ll L/G_0}u
 \ll\left(1+\frac L{G_0}\right)^2.
 \tag{3.28}
\]

Oddness, coprimality, (s>L), (t<T), literal support, and
nonresonance can only decrease this count.  On a ray, consecutive odd
(G)'s have term ratio

\[
 -e(2\sigma\sqrt{Xuv}),
\]

so the geometric partial sums are bounded by the reciprocal of

\[
 \Delta_X(u,v)=\operatorname{dist}
 \left(2\sqrt{Xuv},\mathbb Z+\tfrac12\right).
\]

Given the direct report's separately reviewable literal
(BV_2\ll_\varepsilon X^\varepsilon), Abel summation gives
(O_\varepsilon(\delta^{-1}X^\varepsilon)) on every ray with
\(\Delta_X\ge\delta\).  Thus

\[
 |\mathcal A^{\rm ray,nr}(G_0,\delta)|
 \ll_\varepsilon \delta^{-1}X^\varepsilon
 \left(1+\frac L{G_0}\right)^2.
 \tag{3.29}
\]

With

\[
 G_0=\lceil L^{1/4}\rceil,\qquad
 \delta=(10\log(2X))^{-1},
\]

one has, uniformly including the ceiling,

\[
 \left(1+\frac L{G_0}\right)^2\ll L^{3/2},
 \qquad \delta^{-1}\ll_\varepsilon X^\varepsilon.
 \tag{3.30}
\]

The incidence envelope before ray cancellation is instead

\[
 \sum_{G\ge G_0}O\!\left(\frac{L^2}{G^2}\right)
 \ll\frac{L^2}{G_0}=O(L^{7/4}).
 \tag{3.31}
\]

So (L^{1/4}) is the first threshold at which the per-ray (O(1))
signed estimate and the two-dimensional primitive-ray count alone reach
(L^{3/2}).  The proof earns (G_0=L^{1/4}) relative to the absolute
capacity of this strict sector.  It does not earn the full (L^{1/2})
needed on the complete (G=1), (t=1) face.  The exact complement is

\[
 \{G<G_0\}\ \cup\
 \{G\ge G_0:\Delta_X(u,v)<(10\log(2X))^{-1}\},
 \tag{3.32}
\]

with every original support condition retained.

## 4. Full power ledger and old-PSC comparison

| Interface | Trivial or input scale | Required/output scale | Missing gain or conclusion |
|---|---:|---:|---|
| Complete small-(t) capacity | (L^2) | (L^{3/2}) | (L^{1/2}), already at (t=1) |
| Mobius correction (b\le L) | \(\sum_{b\le L}(1+L/\sqrt b)\) | (L^{3/2}) | target-safe |
| Mobius correction (b>L,u\ge T) | (L^2\sum_{u\ge T}u^{-2}) | (L^2/T\le L^{3/2}) | target-safe |
| Partial-Mobius tail (a\ge T) | (L^2\sum_{a\ge T}a^{-2}\sum_tt^{-2}) | (L^2/T\le L^{3/2}) | target-safe |
| Partial-Mobius core (a<T) | exact signed scalar | full product wave plus (O(L^{3/2})) | self-return |
| Fixed (t) row | (N_t\asymp L^2/t^2) ambient capacity | (N_t^{3/4}) | scalar saving (N_t^{1/4}\asymp L^{1/2}t^{-1/2}) |
| Fejer brace | (Q_tN_t) | (N_t) | squared-level saving (Q_t\asymp\sqrt{N_t}\asymp L/t) |
| Restored (t)-sum | (L^{3/2}\sum t^{-3/2}) | (L^{3/2}) | convergent |
| Primitive-ray sector, absolute | (L^2/G_0) | (L^{7/4}) at (G_0=L^{1/4}) | only an envelope |
| Primitive-ray sector, signed | \(\delta^{-1}(1+L/G_0)^2\) | (L^{3/2}X^\varepsilon) | strict sector proved, conditional on literal BV seam |

The new fixed-row correlation is not the old
`M9-M1-shifted-divisor-correlation-PSC`.

- Old PSC fixes a half-lattice product center (c), pairs the disjoint
  nearest-product fibres at (c-u) and (c+u), and has one linear
  coefficient \(\chi_4(d)w_D(d)G_U(u,d)\) under one outside absolute
  value.
- The new correlation fixes (t), shifts the squarefree radical
  (s\mapsto s+q), and after coefficient expansion has the quadratic
  equation (h_1n_1-h_0n_0=t^2q), two characters, two literal symbols,
  two squarefree indicators, and the radical phase difference (3.20).
  Its midpoint ((2s+q)t^2/2) moves with (s,q,t), rather than being the
  fixed center of PSC.
- The new condition is sufficient for every row separately and then uses
  triangle in (t).  It is therefore stronger than the frozen Round-183
  scalar.  There is no proved implication in either direction between it
  and PSC, so it is neither an equivalent reformulation nor a necessary
  condition for the owner.

At the old PSC critical annulus, the trivial scale is (D/L), the target
is (X^{1/4}), and the missing factor is

\[
 \frac{D/L}{X^{1/4}}=\frac HL,
 \qquad H=DX^{-1/4}.
 \tag{4.1}
\]

At the hard top (D\asymp X^{1/2}), hence (H\asymp X^{1/4}).  On the
present critical shell (L\asymp X^{1/6}), (4.1) is
(X^{1/12}=L^{1/2}), matching the new (t=1) scalar deficit.  This is a
same-shell power comparison only.  Round 70 froze a different
fixed-interior benchmark and obtained (X^{1/20}).  Its
delta/Kloosterman analysis proves that standard completion does not close
that old moving-short-numerator interface; it does not prove failure of
(3.24), whose coefficient, center, shifts, and outer operation are
different.  The overlap is a warning about the broad shifted-product
mechanism, not a theorem transfer.

## 5. First doubtful or unproved step and controls

The Mobius derivations have no unproved analytic step beyond the accepted
support and divisor bounds.  Their first invalid prospective step would
be to call the (a<T) core smaller while it still contains
(K_{L,T}^{<}(b,1)=1) for every (b>L), or to delete (a=1) without an
estimate.

For the correlation route, the first unproved statement is (3.24), already
at (t=1).  Pointwise support gives only a brace of size (Q_tN_t), not
(N_t).  The old PSC and delta/Kloosterman artifacts do not supply the
missing signed relation.

For the direct strict sector, the first unproved part is the exact
complement (3.32), including all of (t=1).  This power review validates
the (G_0) threshold and ray count; promotion still depends on the
separate coefficient/BV and endpoint review.

| Required control | Outcome |
|---|---|
| exact two-cutoff kernel | **PASS.** Both (a^2b>L) and (u/a<T) occur in (3.3). |
| ceiling and strict boundary | **PASS.** (T=\lceil\sqrt L\rceil), so (t=T) and (a^2b=L) are excluded. |
| (t=1) / (u=1) | **PASS as retained obstruction.** (a=t=u=1) remains in both full and (a<T) kernels. |
| exact partition | **PASS.** (3.7) is disjoint and exhaustive. |
| (b\le L) power | **PASS.** (3.8) is (O(L^{3/2})). |
| (b>L,u\ge T) power | **PASS.** (3.9) is (O(L^2/T)). |
| (a\ge T) tail | **PASS.** (3.13) is (O(L^2/T)). |
| large-(t) counted once | **PASS.** The transformed (u\ge T) correction is internal to the alternative regrouping. |
| (a<T) self-return | **PASS.** (3.15)--(3.16) retain the full product wave. |
| van der Corput constant | **PASS.** (3.17)--(3.18) have (N+Q-1), (Q^{-1}), and exact Fejer weights. |
| diagonal | **PASS.** (3.23) retains the literal coefficient squared. |
| shift range/support | **PASS.** (1\le q<Q_t), exact support intersection, no endpoint completion. |
| phase/product shift | **PASS.** Exact radical phase and (h_1n_1-h_0n_0=t^2q). |
| restored (t)-sum | **PASS conditionally.** (3.24) implies (3.26); (3.24) is open. |
| correlation not owner | **PASS.** Rowwise control plus (t)-triangle is strictly stronger. |
| old PSC overlap | **PASS with scale qualification.** Same structural (H/L) deficit at the same shell; no interface equivalence or theorem transfer. |
| primitive-ray (G_0) | **PASS.** (G_0=\lceil L^{1/4}\rceil) makes the ray count (O(L^{3/2})). |
| primitive-ray capacity | **PASS.** Absolute (O(L^{7/4})), signed (O(L^{3/2}X^\varepsilon)) on the declared sector. |
| downstream/exponent quarantine | **PASS.** No hard parent, smooth M1 parent, M2 owner, bridge, theorem, or exponent follows. |

No numerical or external-source theorem evidence was used.

## 6. Dependencies and exact artifacts used

The mathematical review used:

1. `protocol.md`;
2. `state/proof_obligations.yml`, especially the selected small-(t)
   owner, the radical Mobius obstruction, and
   `M9-M1-shifted-divisor-correlation-PSC`;
3. `state/active_campaign.yml`;
4. `strategy/round183_m1_hard_top_high_radical_small_t_signed_contraction_strategy.md`;
5. `proofs/kernels/m9_m1_hard_top_squarefree_radical_reduction_and_self_return.md`;
6. all three Round-183 reports;
7. the Round-12 cross-product-offset-pairing synthesis and its relevant
   exact PSC derivation;
8. the Round-68 square-root-product-offdiagonal synthesis and derivation
   packet;
9. the Round-70 near-product-delta-salie synthesis and derivation packet;
10. the Round-181 independent reduction/self-return and
    product/squarefree connector reviews, consulted only to verify the
    accepted support and endpoint conventions already inherited by the
    durable kernel; and
11. the assigned review brief.

The direct dependencies for the proved identities are the accepted
Round-181 literal product support, zero extension, coefficient divisor
bound, and unique squarefree coordinates.  The primitive-ray power check
also assumes the direct report's literal (BV_2) lemma, which belongs to a
separate review seam.

## 7. Recommended state effect

**Promote only at narrow scope, subject to the other GREEN seams.**

- The power seam supports the direct report's strict nonresonant
  primitive-ray sector with (G\ge\lceil L^{1/4}\rceil), together with
  its exact complement.  It does not support the complete small-(t)
  owner.
- Extend or refine only
  `M9-M1-hard-top-radical-mobius-mellin-joint-t-obstruction` by recording
  that the strict small-(t), (a<T) core self-returns to the full
  product wave modulo (O_\varepsilon(L^{3/2}X^\varepsilon)), while the
  (a\ge T) tail is target-safe.
- Retain the exact fixed-row Fejer connector only as inconclusive
  sufficient evidence.  Do not create it as a necessary owner, do not
  identify it with PSC, and do not promote (3.24).

Keep `M9-M1-hard-top-high-radical-small-t-residual-estimate`,
`M9-M1-top-endpoint-signed-cone`, the smooth direct-M1 parent, M9-M1,
every M2 parent, endpoint uniformity, M9, both bridges, and the Gauss-circle
target open.  The internal exponent remains (1/3), the accepted external
benchmark remains (0.3144831759740614\ldots), and the target remains
(1/4).
