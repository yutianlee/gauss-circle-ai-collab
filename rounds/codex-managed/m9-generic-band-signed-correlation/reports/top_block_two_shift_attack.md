# Round 4 report: top-block two-shift attack

## 1. Result and verdict

**Verdict: the top dyadic frequency block is pointwise controllable by an
elementary two-shift/divisor argument.**  No Bombieri--Iwaniec extension is
needed for the block (L\asymp H_D\asymp D X^{-1/4}).

More precisely, for the actual Vaaler coefficient, a bounded denominator
weight, and a normalized bounded-variation cutoff in (h\), the dyadic block

\[
 \mathcal B_L(D;X)=
 \sum_{L\le |h|<2L}\beta_{h,H}
 \sum_{D\le d<2D}w_D(d)e\!\left(\frac{hX}{4d}\right)
\]

satisfies

\[
 \boxed{
 |\mathcal B_L(D;X)|
 \ll_\varepsilon X^\varepsilon\left(1+\frac DL\right). }
\tag{1.1}
\]

Consequently,

\[
 L\asymp H_D\asymp D X^{-1/4}
 \quad\Longrightarrow\quad
 \mathcal B_L(D;X)\ll_\varepsilon X^{1/4+\varepsilon}
\tag{1.2}
\]

uniformly for (X^{1/4}\le D\le X^{1/2}).  The proof preserves the exact
(ho=1,3) decomposition, but it bounds the two shifts separately.  The
saving comes from geometric cancellation in (h), followed by the fact that
the near-integrality condition is represented by integers
(n=d(4m-\rho)) with divisor multiplicity.  It is not cancellation between
the two shifts.

This is a scoped top-block lemma, not a proof of `M9-M2`.  For a lower block
(L=H_D/Y), (1.1) loses the factor (Y); the intermediate and small
frequency blocks remain.  The printed Li--Yang theorem is structurally
compatible with each shift over some smaller-height parameter regions, but
it neither reaches the top height nor supplies the conjectural
(X^{1/4+\varepsilon}) exponent.

No numerical experiment was used.

## 2. Exact block and two-shift normalization

For positive (h), write

\[
 \beta_{h,H}=-\frac{\Phi(h/(H+1))\chi_4(h)}{\pi h},
\qquad
 \chi_4(h)=\frac{e(h/4)-e(3h/4)}{2i}.
\tag{2.1}
\]

Let (eta_L) be a fixed smooth or uniformly BV dyadic cutoff supported in
([L,2L]), truncated at (h\le H), and set

\[
 u_L(h)=\eta_L(h)\frac{\Phi(h/(H+1))}{h}.
\]

The positive-frequency block is a constant multiple of

\[
 \mathcal B_L^+
 =\sum_{\rho\in\{1,3\}}\sigma_\rho
 \sum_d w_D(d)
 \sum_h u_L(h)e\!\left(\frac h4\left(\frac Xd+\rho\right)\right),
 \qquad \sigma_1=1,\quad\sigma_3=-1.
\tag{2.2}
\]

The negative-frequency block has the same bound by applying the argument to
(-h); no reality assumption on (w_D) is needed.  Equivalently, if

\[
 S_\rho(L,D;X)=
 \sum_{h\asymp L}g_L(h/L)
 \sum_{d\asymp D}G_D(d/D)
 e\!\left(\frac h4\left(\frac Xd+\rho\right)\right),
\tag{2.3}
\]

where (g_L,G_D) have uniform BV norms, then the Vaaler block has size

\[
 \mathcal B_L\asymp L^{-1}(S_1-S_3)
\tag{2.4}
\]

up to fixed constants and partial summation.  Thus the project target for
this block is

\[
 |S_1-S_3|\ll_\varepsilon L X^{1/4+\varepsilon}.
\tag{2.5}
\]

## 3. Proven top-block lemma

### Lemma T2S

Let (X\ge X_0), (1\le L\le H\le D\le X^{1/2}), and suppose
(w_D) is supported on the integer shell ([D,2D)) with
(|w_D|_\infty\le C_w).  Suppose also that

\[
 \sup_h|u_L(h)|+
 \sum_h|u_L(h+1)-u_L(h)|\ll \frac1L.
\tag{3.1}
\]

Then each shifted block in (2.2), and hence their difference, satisfies

\[
 \left|
 \sum_d w_D(d)\sum_hu_L(h)
 e\!\left(\frac h4\left(\frac Xd+\rho\right)\right)
 \right|
 \ll_{\varepsilon,C_w}X^\varepsilon\left(1+\frac DL\right),
 \qquad \rho\in\{1,3\}.
\tag{3.2}
\]

The audited (C^1) regularity of (Phi), a fixed normalized BV cutoff, and
endpoint truncation at (H) imply (3.1), including when (L\asymp H).

### Proof

Abel summation and the geometric progression bound give, for every real
(	heta),

\[
 \left|\sum_hu_L(h)e(h\theta)\right|
 \ll
 \min\left(1,\frac1{L\|\theta\|}\right).
\tag{3.3}
\]

Fix (d\in[D,2D)) and (ho\in\{1,3\}).  Put

\[
 \theta_{d,\rho}=\frac14\left(\frac Xd+\rho\right),
\]

choose an integer (m=m(d,\rho)) nearest to (	heta_{d,\rho}), and define

\[
 n=d(4m-\rho)\in\mathbb Z.
\tag{3.4}
\]

Then

\[
 |X-n|=4d\|\theta_{d,\rho}\|,
 \qquad |X-n|\le2d<4D.
\tag{3.5}
\]

For a fixed (n), every participating (d) divides (n), and the congruence
(n/d\equiv-\rho\pmod4) only removes divisors.  Since
(n\asymp X) in the active range, the multiplicity is at most
(	au(n)\ll_\varepsilon X^\varepsilon).  Hence (3.3)--(3.5) imply

\[
\begin{aligned}
 \sum_{D\le d<2D}
 \min\left(1,\frac1{L\|\theta_{d,\rho}\|}\right)
 &\le
 \sum_{|n-X|<4D}\tau(n)
 \min\left(1,\frac{8D}{L|X-n|}\right)\\
 &\ll_\varepsilon
 X^\varepsilon\frac DL\log(2D)\\
 &\ll_\varepsilon X^\varepsilon\left(1+\frac DL\right).
\end{aligned}
\tag{3.6}
\]

If (X=n) for one integer, the corresponding summand is interpreted as
(1); it is already included in the last bound.  Multiplying by
(|w_D|_\infty) proves (3.2).  Applying it to both shifts and to both signs
of (h) proves (1.1). (square)

For the top dyadic block (L\asymp H_D\asymp D X^{-1/4}), (3.6) is exactly

\[
 \frac DL\asymp X^{1/4},
\]

which proves (1.2).  The argument is pointwise in the real parameter (X)
and uniform at all three requested (D)-scales.

## 4. Direct one-dimensional and transformed bound ledger

### 4.1 Summing (d) first: van der Corput loses (X^{1/8})

For fixed (h\asymp L), the phase (f(d)=hX/(4d)) has

\[
 |f''(d)|\asymp \frac{hX}{D^3}.
\]

The second-derivative estimate gives

\[
 \sum_{d\asymp D}w_D(d)e(hX/(4d))
 \ll
 \left(\frac{hX}{D}\right)^{1/2}
 +\left(\frac{D^3}{hX}\right)^{1/2},
\tag{4.1}
\]

for a smooth/BV denominator weight.  After the (1/h) Vaaler weight is
summed over (h\asymp L), this yields

\[
 \mathcal B_L
 \ll
 \left(\frac{LX}{D}\right)^{1/2}
 +\left(\frac{D^3}{LX}\right)^{1/2}.
\tag{4.2}
\]

At (L=D X^{-1/4}), the first term is (X^{3/8}), while the target is
(X^{1/4}).  The exact deficit of this direct route is therefore

\[
 \boxed{X^{1/8}.}
\]

The second term is (D X^{-3/8}\le X^{1/8}) and is harmless compared with
the first.

Conditionally, an exponent-pair estimate in the standard reciprocal-phase
normalization would give the main term

\[
 X^{\kappa(3/4-\delta)+\lambda\delta},
 \qquad D=X^\delta,quad L=D X^{-1/4}.
\tag{4.3}
\]

At the endpoint (delta=1/2), reaching (X^{1/4}) requires

\[
 \kappa+2\lambda\le1.
\tag{4.4}
\]

The classical (B)-process pair ((1/2,1/2)) gives (X^{3/8}), and (4.4)
is the conjectural boundary ((0,1/2)).  Thus a one-dimensional (d)-sum
exponent-pair argument does not explain the top-block endpoint; Lemma T2S
does so by reversing the summation order.

### 4.2 Poisson/stationary phase

For a smooth denominator weight, Poisson summation in (d) produces

\[
 D\int W(u)e\!\left(\frac{hX}{4Du}-kDu\right)du.
\]

For positive (h), stationary points occur for (k=-n<0), with

\[
 n\asymp \frac{hX}{D^2},qquad
 u_0=\left(\frac{hX}{4nD^2}\right)^{1/2},qquad
 \frac{hX}{4Du_0}+nDu_0=\sqrt{hXn}.
\]

The leading stationary-phase size is

\[
 \frac{D^{3/2}}{(hX)^{1/2}}
 e\!\left(\sqrt{hXn}+\frac18\right)
\]

times a smooth amplitude.  The two-shift factor (e(\rho h/4)) survives
unchanged.  Thus the top block is modeled by

\[
 \frac{D^{3/2}}{X^{1/2}L^{3/2}}
 \sum_{h\asymp L}e(\rho h/4)a_h
 \sum_{n\asymp hX/D^2}a_{h,n}e(\sqrt{hXn}).
\tag{4.5}
\]

At (L=D X^{-1/4}), the dual lengths satisfy

\[
 N\asymp X^{3/4}/D,qquad LN\asymp X^{1/2},
\]

and the prefactor in (4.5) is (X^{-1/8}).  Trivial estimation of the
(LN\) dual terms again gives (X^{3/8}).  A transformed proof would need

\[
 \left|\sum_{h\asymp L}\sum_{n\asymp hX/D^2}
 e(\rho h/4)a_{h,n}e(\sqrt{hXn})\right|
 \ll_\varepsilon X^{3/8+\varepsilon},
\tag{4.6}
\]

an (X^{1/8}) saving over the trivial (X^{1/2}).  Square-root cancellation
in (n) separately for each (h) would suffice and is exactly sharp at
(D=X^{1/2}).  No audited primary-source theorem in the repository supplies
(4.6) with these ranges and weights.  This transformed statement is not
needed for the top block because Lemma T2S is stronger and elementary.

## 5. Li--Yang/Bombieri--Iwaniec applicability

The primary source is Xiaochun Li and Xuerui Yang,
[*An improvement on Gauss's Circle Problem and Dirichlet's Divisor
Problem*](https://arxiv.org/abs/2308.14859), arXiv:2308.14859v2.  The exact
local source audited was
`rounds/web-research-test/Li-Yang-arXiv-2308.14859v2.tex`, especially their
Section 4 definition of (S), Cases A/B, and main theorem.  Bourgain--Watt
([arXiv:1709.04340](https://arxiv.org/abs/1709.04340)) is used only as a
structural reference; its project source card is incomplete, so no theorem
is imported from it.

### Exact map

Li--Yang study

\[
 S=\sum_{\mathsf H\le h\le2\mathsf H}g(h/\mathsf H)
 \sum_{\mathsf M\le m\le2\mathsf M}G(m/\mathsf M)
 e\!\left(\frac{h\mathsf T}{\mathsf M}
 F(m/\mathsf M)\right).
\]

For each M2 shift the exact map is

\[
 \boxed{
 \mathsf H=L,quad \mathsf M=D,quad \mathsf T=X/4,quad
 F_\rho(u)=u^{-1}+\rho D/X. }
\tag{5.1}
\]

Indeed, the phase becomes (h(X/d+\rho)/4).  The derivative hypotheses hold:

\[
 F'=-u^{-2},\quad F''=2u^{-3},\quad F'''=-6u^{-4},
 \quad F'F'''-3(F'')^2=-6u^{-6}.
\]

The Vaaler coefficient is (L^{-1}) times a uniform BV function of (h/L),
so the desired project quantity is precisely (S/\mathsf H).  Li--Yang's
theorem applies to each shift separately; it does not exploit interference
between (ho=1) and (ho=3).

### Height feasibility

At the project top,

\[
 L_{\rm top}=D X^{-1/4}.
\]

Li--Yang Case A has the upper-height condition

\[
 L\le D X^{-49/164}.
\tag{5.2}
\]

Thus the top misses Case A by the exact factor

\[
 \boxed{X^{49/164-1/4}=X^{2/41}.}
\tag{5.3}
\]

Their Case B upper-height condition becomes

\[
 L\le \min\left(D^{35/69}X^{-2/23}, D^{3/2}X^{-1/2}\right).
\tag{5.4}
\]

Writing (D=X^\delta), the definition-level height comparison is:

| (D) | top exponent (delta-1/4) | Case A upper exponent | Case B upper exponent | Case B top gap |
|---|---:|---:|---:|---:|
| (X^{1/3}) | (1/12) | (17/492) | (0) | (1/12) |
| (X^{3/8}) | (1/8) | (25/328) | (1/16) | (1/16) |
| (X^{1/2}) | (1/4) | (33/164) | (1/6) | (1/12) |

The Case A gap is always (2/41).  More generally, the two Case B gaps are

\[
 \frac{34}{69}\delta-\frac{15}{92},qquad
 \frac14-\frac\delta2,
\]

and the larger one is forced because of the minimum in (5.4).

These are only upper-height checks.  The printed main theorem additionally
requires (4\le q\le4.5), the auxiliary (N)-condition, and, in the Case B
reduction,

\[
 D^{-27/23}X^{53/92}<L<D^{-9}X^4(\log X)^{171/140}.
\]

The v2 TeX also contains an apparent sign inconsistency in the first Case A
threshold: the definition prints (M<T^{-7/16}), while the final-argument
restatement prints (M<T^{7/16}).  Until the rendered source card reconciles
this, the safe statement is only that (5.2)--(5.4) are necessary height
conditions, not a complete theorem-import certificate.

### Output-exponent deficit

Even where the parameter conditions hold, Li--Yang's printed estimate is a
record-exponent theorem, not an (X^{1/4}) theorem.  Their final circle
exponent is

\[
 \theta^*=0.3144831759741\ldots,
\]

so the exact project-level exponent deficit is

\[
 \boxed{\theta^*-\frac14=0.0644831759741\ldots.}
\tag{5.5}
\]

For a transparent blockwise check, insert (q=9/2) into their displayed
bound for (S/H).  If that formula were extrapolated to the project top
(H/M=X^{-1/4}), its main exponent would be

\[
 \frac{2839}{9000}=0.315444\ldots,
\]

with deficit (589/9000=0.065444\ldots); its final bracket is (O(1)).
At the Case A ceiling (H/M=X^{-49/164}), the same displayed expression is
approximately (X^{0.31484}), still far above (X^{1/4}).

Therefore the smaller-(L) ranges are only **theorem-height-admissible** (and
only after all auxiliary conditions are checked).  They are not covered at
the project's conjectural exponent.  Conversely, the top block is outside
the printed Li--Yang height range but is covered directly by Lemma T2S.

## 6. Weakest sufficient lemma and remaining gap

The weakest top-block statement needed by the project is

\[
 \boxed{
 \mathcal B_L(D;X)\ll_\varepsilon X^{1/4+\varepsilon}
 \quad\text{for}\quad
 L\asymp D X^{-1/4},\quad X^{1/4}\le D\le X^{1/2}. }
\tag{6.1}
\]

Lemma T2S proves (6.1) under the exact Vaaler BV hypothesis and bounded
dyadic denominator weights.  Thus no new Bombieri--Iwaniec theorem is needed
for this interface.

What remains after removing the top block is a lower-frequency theorem.  A
minimal pointwise successor would be

\[
 \mathcal B_L(D;X)\ll_\varepsilon X^{1/4+\varepsilon}
 \quad (1\le L\ll D X^{-1/4}),
\tag{6.2}
\]

or a hybrid partition proving (6.2) only on the gap between an independently
verified lower-block theorem and (L\asymp H_D).  The elementary estimate
(1.1) becomes (X^{1/4}(H_D/L)), so it does not solve (6.2).  Neither the
published Li--Yang exponent nor an ordinary one-dimensional (d)-sum
estimate closes this remaining gap.

If one insists on the Poisson route, (4.6) is the weakest sufficient new
dual lemma for the top block, but it is now strategically unnecessary.

## 7. Controls

### `signed-vs-unsigned`

The actual character is preserved exactly through
(chi_4(h)=(e(h/4)-e(3h/4))/(2i)).  The proof then bounds the two shifts
separately.  In fact, the same divisor argument also bounds the top block
with (|\beta_h|), using the unshifted frequency (X/(4d)).  This does not
conflict with the accepted unsigned fat-band obstruction: (1.1) is a
pointwise bound for one (h)-block, not an absolute fourth-moment or
near-collision-mass bound.

### `coefficient-adversary` / `proves-too-much`

Arbitrary signs (sigma_h) destroy (3.1): the discrete variation of
(sigma_h/h) can be order one rather than (1/L), so Abel summation no
longer gives (3.3).  Thus the proof does not establish the same result for
adversarial coefficients.  Its structural input is the fixed Vaaler
amplitude together with the exact periodic shift.

### `dyadic-endpoints`

At (D=X^{1/3},X^{3/8},X^{1/2}), the top height is respectively
(X^{1/12},X^{1/8},X^{1/4}), but in all cases

\[
 D/L\asymp X^{1/4}.
\]

Hence Lemma T2S has no endpoint power loss.  The condition (H_D\ge1) is
explicit; endpoint-truncated (h)-blocks are covered by the BV variation
term in (3.1).

### `source-applicability`

The exact Li--Yang variable and phase map is verified, as are the derivative
hypotheses.  The top block fails their displayed height hypotheses, their
output exponent exceeds (1/4), and their auxiliary conditions have not
been silently omitted.  No Bourgain--Watt or Huxley theorem is imported from
an incomplete source card.

## 8. First doubtful or unproved step

The proof of Lemma T2S has no unproved analytic step beyond the already
accepted (C^1) regularity of (Phi) and the elementary divisor bound.  The
first unproved project step is the lower/intermediate-frequency estimate
(6.2), not the top block.

The Poisson formula (4.5) is only a leading stationary-phase model: a proof
through that route would still need zero-mode, nonstationary-tail,
support-edge, and uniform error estimates.  Likewise, the Li--Yang
comparison remains a method audit until the source-card threshold typo and
all auxiliary inequalities are reconciled.

## 9. Dependencies and artifacts used

- `state/proof_obligations.yml`
- `state/best_proof_draft.md`
- `sources/li_yang_2023.md`
- `rounds/codex-managed/m9-signed-lift-capacity/reviews/conductor_literature_method_audit.md`
- primary local source:
  `rounds/web-research-test/Li-Yang-arXiv-2308.14859v2.tex`
- Xiaochun Li and Xuerui Yang,
  [arXiv:2308.14859v2](https://arxiv.org/abs/2308.14859)
- Jean Bourgain and Nigel Watt,
  [arXiv:1709.04340](https://arxiv.org/abs/1709.04340), structural comparison only

No numerical or experimental artifact was used.

## 10. Recommended state effect

- Add a scoped **top-frequency two-shift lemma** with status
  `proved_internal`: under bounded denominator weights and the actual
  normalized-BV Vaaler amplitude, (1.1) holds, hence the block
  (L\asymp H_D) is (O_\varepsilon(X^{1/4+\varepsilon})) pointwise.
- Update `M9-M2-reciprocal-SPD-route` to remove the top block from its
  blocker statement and target the remaining lower/intermediate blocks.
- Keep `Li-Yang-source-audit` open.  Record the exact phase map, Case A gap
  (2/41), Case B endpoint gaps, output deficit (5.5), and the apparent
  threshold-sign inconsistency.
- No promotion of `M9-M2`, `M9`, the signed fat-band constant, or any
  global-to-pointwise bridge.

