# Hostile lower-bound audit

- Campaign: `m9-weighted-mass-adjudication`
- Task: `hostile_lower_bound_audit`
- Role: `barrier_no_go`
- Access mode: `selected_context`
- Graph SHA-256: `3c06ffad9c2847b329c57a8954d0758e443ee55be2da01c00ce5731bad3d6b5f`
- Status: candidate evidence only; no graph promotion proposed

## 1. Result

The Round 9 count-versus-weighted dichotomy is false as stated on both sides.

First, A4-009's proposed actual-weight upper bound

$$
\Sigma_{\rm abs}\left(0<|N|\le \frac{D^4}{X}\right)
\ll_\epsilon \left(D+\frac{D^4}{X}\right)X^\epsilon
$$

is refuted by a compatible fixed-frequency window family. Under the H4 lower envelope for $\beta_{1,H}$ and the accepted H4-dependent exact-$N=0$ closure,

$$
\boxed{
\Sigma_{\rm abs}(0<|N|\le M)
\ge c\min(D^4,MD)-C_\epsilon D^2X^\epsilon .
}
\tag{W1-unit}
$$

In the global fat band $M=D^4/X$ this gives

$$
\boxed{
\Sigma_{\rm abs}\left(0<|N|\le \frac{D^4}{X}\right)
\ge c\frac{D^5}{X}-C_\epsilon D^2X^\epsilon .
}
\tag{1}
$$

Consequently, for every fixed $\delta>0$, all sufficiently large $X$, and

$$
X^{1/3+\delta}\le D\le X^{1/2},
$$

one has, after choosing $\epsilon<3\delta$,

$$
\Sigma_{\rm abs}\left(0<|N|\le \frac{D^4}{X}\right)
\gg \frac{D^5}{X}
\gg D^2X^\epsilon.
$$

Thus the full-support absolute fat-band target already fails beyond $D=X^{1/3+o(1)}$, not merely beyond $X^{3/8+o(1)}$. The familiar $X^{3/8}$ scale is recovered only by using a bulk frequency block $|h|\asymp H_D$ and paying the corresponding $H_D^{-4}$ beta factor; it is not the optimal obstruction once small frequencies are retained.

Second, A4-009's claimed weight-blind nonzero count $\asymp D H_D^3$ is not proved by its displayed family. With all four denominators equal to $d$,

$$
N=d^3(h_1-h_2+h_3-h_4).
$$

The relation used there, $h_1+h_3=h_2+h_4$, makes $N=0$ exactly. Since the frozen quantity excludes $N=0$, that family contributes nothing to the claimed nonzero fat-band count. No matching asymptotic for the raw nonzero count follows.

The older Round 8/A1/A2/A3 conclusion that W-1 obstructs the genuinely beta-weighted mass is therefore correct in scope, conditional on H4 and exact-resonance subtraction, but its $D^4X^{-3/4}$ bulk-frequency lower bound is nonoptimal. A4-009's count-only correction should be rejected.

These are no-go results for the absolute mass and for the comparison obtained after removing $\chi_4$ signs. They do not give a lower bound for the full true signed mass, because the positive fixed-frequency subtotal may be cancelled by tuples outside the family.

## 2. Exact statement and hypotheses

Let

$$
H=H_D\asymp DX^{-1/4},
\qquad X^{1/4}\le D\le X^{1/2},
$$

and let $\mathcal D_D=[D,2D)\cap\mathbb Z$. For an ordered tuple $({\bf h},{\bf d})$ set

$$
N({\bf h},{\bf d})
=h_1d_2d_3d_4-h_2d_1d_3d_4+h_3d_1d_2d_4-h_4d_1d_2d_3.
$$

Define the sharp-block frozen quantities

$$
\mathcal C(M)
=\#\left\{({\bf h},{\bf d}):d_i\in\mathcal D_D,
\ 1\le |h_i|\le H,\ 0<|N|\le M\right\},
$$

$$
\Sigma_{\rm abs}(M)
=\sum_{0<|N|\le M}\prod_{i=1}^4|\beta_{h_i,H}|,
$$

$$
\Sigma_\chi(M)
=\sum_{0<|N|\le M}\prod_{i=1}^4\beta_{h_i,H},
$$

and, after removing the $\chi_4$ signs,

$$
\widetilde\beta_{h,H}
=-\frac{\Phi(|h|/(H+1))}{\pi|h|}\mathbf 1_{2\nmid h},
\qquad
\Sigma_{\rm uns}(M)=\sum_{0<|N|\le M}\prod_{i=1}^4\widetilde\beta_{h_i,H}.
$$

The result uses the following hypotheses, all already visible in the selected graph context.

1. H4 beta algebra and positivity: for odd $h$,
   $$
   |\beta_{h,H}|=\frac{\Phi(|h|/(H+1))}{\pi|h|},
   $$
   and there is a constant $b_0>0$ such that
   $$
   |\beta_{1,H}|\ge b_0\qquad(H\ge1).
   \tag{B1-lower}
   $$
   The last assertion follows from the provisional H4 formula because $u=1/(H+1)\in(0,1/2]$, $\Phi$ is continuous with $\Phi(0)=1$, and $\Phi(u)>0$ on this compact range. It remains source-card-dependent.

2. Exact-resonance closure:
   $$
   \Sigma_{\rm abs}(N=0)\le C_\epsilon D^2X^\epsilon.
   \tag{E0}
   $$
   This is the accepted `M9-M2-exact-N0-total-mass` statement and is itself derived under H4.

3. The sharp dyadic block contains $\asymp D$ integers. For an actual smooth dyadic weight, the same lower bound transfers only if $|w_D|$ has a fixed positive lower bound on a subinterval containing $\asymp D$ integers. The campaign's frozen tuple quantities omit $w_D$, so no such extra hypothesis is needed for the adjudication itself.

4. The band parameter obeys $1\le M\ll D^3$ for the linear form $MD$ in (W1-unit). The global fat band satisfies this automatically because
   $$
   \frac{D^4/X}{D^3}=\frac DX\le X^{-1/2}.
   $$

Under these hypotheses, (W1-unit) is `derived_under_assumptions`, not `proved_internal`.

## 3. Proof and scale derivation

### 3.1 Unit-frequency W-1 family

Restrict all four frequencies to

$$
h_1=h_2=h_3=h_4=1.
$$

Parity is automatic, $1\le h_i\le H$ in the range of interest, and no reduced-fraction lift is present: each $1/d$ is already reduced and corresponds to the single lift $g=1$. Hence there is no hidden lift multiplicity and no truncation-edge loss.

For an ordered pair $(d_1,d_3)\in\mathcal D_D^2$, put

$$
s(d_1,d_3)=\frac1{d_1}+\frac1{d_3}.
$$

All these pair sums lie in

$$
\left(\frac1D,\frac2D\right],
$$

an interval of length at most $D^{-1}$. This is the scale omitted in A4-009's reciprocal-AP heuristic.

Let

$$
\eta=\frac{M}{16D^4}
$$

and partition that pair-sum interval into half-open windows of length at most $\eta$. The number of windows is

$$
K\le 2+\frac{1/D}{\eta}
\le C\left(1+\frac{D^3}{M}\right).
\tag{2}
$$

Let $v_j$ be the number of ordered pairs $(d_1,d_3)$ whose sum lies in window $j$. Since

$$
\sum_jv_j=|\mathcal D_D|^2\asymp D^2,
$$

Cauchy--Schwarz gives

$$
\sum_jv_j^2
\ge \frac{(\sum_jv_j)^2}{K}
\gg \frac{D^4}{1+D^3/M}
\gg \min(D^4,MD).
\tag{3}
$$

Every term counted by $\sum_jv_j^2$ is an ordered quadruple $({\bf d})$ with

$$
\left|
\frac1{d_1}-\frac1{d_2}+\frac1{d_3}-\frac1{d_4}
\right|<\eta.
$$

Since $Q=d_1d_2d_3d_4<16D^4$ and

$$
N=Q\left(\frac1{d_1}-\frac1{d_2}+\frac1{d_3}-\frac1{d_4}\right),
$$

these quadruples satisfy $|N|<16D^4\eta=M$. This conversion contains the complete clearing-denominator factor; no extra $D$, $H$, lift, or $X$ factor remains.

Each such tuple has absolute beta weight $|\beta_{1,H}|^4\ge b_0^4$. Equation (3) therefore gives same-window absolute mass

$$
\Sigma_{\rm abs}(|N|\le M;h_i=1)
\gg \min(D^4,MD).
$$

This includes exact resonances. Subtracting the exact contribution using (E0) yields

$$
\Sigma_{\rm abs}(0<|N|\le M)
\ge c\min(D^4,MD)-C_\epsilon D^2X^\epsilon,
$$

which is (W1-unit).

The same calculation gives a raw-count lower bound. Indeed, on this family every tuple has weight between two fixed positive constants, so (E0) bounds the number of exact tuples in the family by $O_\epsilon(D^2X^\epsilon)$. Hence

$$
\mathcal C(M)
\ge c\min(D^4,MD)-C_\epsilon D^2X^\epsilon.
\tag{4}
$$

This is a family-specific comparison, not a transfer principle from arbitrary raw counts to weighted masses.

### 3.2 Fat-band specialization and endpoint scales

Set

$$
M=M_{\rm fat}=\frac{D^4}{X}.
$$

Because $D/X\ll1$, the linear branch of (W1-unit) applies, giving (1). Its ratio to the proposed budget is

$$
\frac{D^5/X}{D^2}=\frac{D^3}{X}.
$$

Thus a power violation begins at $D>X^{1/3+\delta}$.

At the three frozen scales:

| Scale | $H_D$ | $M_{\rm fat}$ | Unit W-1 main term $D^5/X$ | Comparison with $D^2$ |
|---|---:|---:|---:|---:|
| $D=X^{1/4}$ | $\asymp1$ | $1$ | $X^{1/4}$ | Exact subtraction dominates; no obstruction obtained |
| $D=X^{3/8}$ | $X^{1/8}$ | $X^{1/2}$ | $X^{7/8}$ | Exceeds $D^2=X^{3/4}$ by $X^{1/8}$ |
| $D=X^{1/2}$ | $X^{1/4}$ | $X$ | $X^{3/2}$ | Exceeds $D^2=X$ by $X^{1/2}$ |

Therefore $X^{3/8}$ is not the crossover of the genuine full-support beta-weighted mass.

### 3.3 Where the old $X^{3/8}$ factor comes from

For completeness, take a frequency block

$$
P\le h\le2P,
\qquad 1\le P\le\kappa H,
$$

with $h$ odd, $(h,d)=1$, and fixed $\kappa<1/2$ so that the beta lower envelope is uniform away from the truncation edge. There are $\asymp PD$ one-body fractions $h/d$, each has weight $\asymp P^{-1}$, and their values lie in an interval of length $O(P/D)$. Repeating the window argument gives

$$
\Sigma_{\rm abs}(M)
\ge c\min\left(D^4,\frac{MD}{P}\right)-C_\epsilon D^2X^\epsilon,
\tag{5}
$$

while the corresponding raw same-window count before exact subtraction is

$$
\gg \min(P^4D^4,MDP^3).
\tag{6}
$$

The factor $P^{-4}$ from the four beta coefficients has therefore been paid explicitly. There is still no lift multiplicity: this construction uses coprime pairs with $g=1$.

At the fat band, (5) becomes $D^5/(PX)$. Choosing $P\asymp H=DX^{-1/4}$ gives

$$
\frac{D^5}{HX}=D^4X^{-3/4},
$$

which is exactly the older W-1 lower-bound scale and crosses $D^2$ at $D=X^{3/8}$. Choosing $P=1$ gives the stronger $D^5/X$ scale and the $X^{1/3}$ crossover. Thus $X^{3/8}$ is a bulk-frequency artifact, not a raw-versus-weighted boundary.

### 3.4 Why A4-009's two formulas fail

A4-009's raw count uses equal denominators. If $d_1=d_2=d_3=d_4=d$, then

$$
N=d^3(h_1-h_2+h_3-h_4).
$$

Its additive relation forces the parenthesis to vanish. Hence every counted tuple is an exact resonance. Moreover, for the fat band,

$$
0<|N|\le \frac{D^4}{X}
\quad\Longrightarrow\quad
0<|h_1-h_2+h_3-h_4|\ll\frac DX<1,
$$

which is impossible. The proposed $DH_D^3$ family is therefore wholly outside the frozen nonzero quantity.

The claimed weighted upper bound $D+D^4/X$ drops the pair-sum multiplicity. For the $D$ unit reciprocals, there are $\asymp D^2$ ordered pairs, not $D$ objects. They occupy only $K\asymp X/D$ windows of width $1/X$ in the fat-band normalization, so their collision energy is at least

$$
\frac{D^4}{X/D}=\frac{D^5}{X},
$$

not $D^4/X$. The missing factor is exactly the extra $D$ coming from pair-sum multiplicity.

## 4. UNC, TS, and W-1 scope ledger

The three known controls have different ranges. They should not be merged into a single slogan.

| Family | Exact construction and band | Raw count / absolute beta mass | True signed scope | Correct obstruction scope |
|---|---|---|---|---|
| UNC | $h_i=1$, $d=(a,a+j,b,b+k)$; $N=j,b(b+k)+k,a(a+j)>0$; for $D^2\ll M\ll D^3$, take $j,k\ll M/D^2$ | $\gg M^2/D^2$ for both raw and absolute/chi-removed mass; no lifts; $\beta_1^4\asymp1$ | The family subtotal is positive, but the full signed band may cancel against other tuples | Refutes the old graded envelope when $M\gg X$, possible only once $D^3\gg X$; it does not enter the fat band for $D<X^{1/2}$ because $M_{\rm fat}<D^2$ |
| TS | $h_i=1$, $d=(a,a+j,b+j,b)$; $N=j(b-a)(a+b+j)>0$ | In the fat band, nonempty for $D^3\gtrsim X$ and gives $\gg D^4/X$ (up to a divisor-log if all $j,\ell$ are used); raw and weighted scales coincide | Positive subtotal only; no lower bound for the full signed mass | Compatible with $D^2$ throughout $D\le X^{1/2}$ and reaches that scale only at the endpoint; it is not a refutation |
| W-1($P$) | Fractions $h/d$ with $h\asymp P$, window width $M/(16D^4)$; same-window pair sums | Raw $\gg MDP^3$ and absolute $\gg MD/P$ in the fine band, before exact subtraction; $P^{-4}$ beta factor explicit; $g=1$ | Absolute/chi-removed obstruction only. Character signs vary for $P>1$; even at $P=1$, a positive subtotal can be cancelled by the complement | $P\asymp H$ gives $D^4X^{-3/4}$ and the old $3/8$ threshold. $P=1$ gives $D^5/X$ and the stronger $1/3$ threshold |

UNC and TS are explicit nonzero families. W-1 is a Cauchy window family and becomes a nonzero lower bound only after exact-$N=0$ mass is subtracted. That subtraction is essential and was omitted in A2-009's `proved_internal` wording.

## 5. Required control tests and outcomes

### `raw-vs-weighted`

Input: the frequency block $h\asymp P$, the same denominator block, and the same $N$-band.

Outcome: raw same-window multiplicity is $\gg MDP^3$, whereas four beta magnitudes contribute $P^{-4}$ and produce weighted mass $\gg MD/P$. No exponent transfers without this summation. For $P=1$, the coefficient is bounded below and the two quantities have the same scale; this special compatible family refutes the proposed weighted upper bound.

### `signed-vs-unsigned`

Input: true $\beta_h$, absolute values, and coefficients with $\chi_4$ removed.

Outcome: because $\Phi\ge0$ on the active support and there are four coefficients,

$$
\prod_{i=1}^4\widetilde\beta_{h_i,H}
=\prod_{i=1}^4|\beta_{h_i,H}|.
$$

Thus the chi-removed fourfold mass is exactly the absolute mass, and all absolute lower bounds transfer to it. They do not transfer to $\Sigma_\chi$: the fixed-$h=1$ subfamily is positive, but no sign-preserving lemma prevents cancellation by its complement. The signed obligation remains open.

### `known-lower-bound-families`

Input: UNC, TS, bulk W-1, and the unit-frequency W-1 specialization.

Outcome: UNC is a large-$M$ weighted obstruction; TS is a compatible fat-band floor but not a violation; W-1 is genuinely beta-weighted once its $P^{-4}$ factor and exact subtraction are included. The unit-frequency specialization strengthens the accepted W-1 threshold from $3/8$ to $1/3$.

### `exact-vs-near-resonance`

Input: A4-009's equal-denominator family and the W-1 windows.

Outcome: the equal-denominator family is exactly $N=0$ and cannot support a nonzero-band conclusion. W-1 counts $|N|\le M$ first and uses (E0) to remove $N=0$ explicitly. UNC and TS have displayed strictly positive $N$ identities.

All outcomes above are analytical. No finite diagnostic is used as proof evidence.

## 6. First doubtful or unproved step

The combinatorial window argument, interval length, Cauchy energy, denominator clearing, and equal-denominator refutation are elementary and complete.

The first source-dependent step is (B1-lower), the uniform lower bound for $|\beta_{1,H}|$. It depends on the exact H4/Vaaler coefficient formula, positivity and endpoint behavior of $\Phi$, and therefore remains blocked by `H4-source-audit`.

The second conditional input is (E0), the accepted exact-$N=0$ absolute mass closure. It is needed to turn a same-window $|N|\le M$ lower bound into a strictly nonzero-band lower bound. Its graph status is `derived_under_assumptions`, not `proved_internal`.

For an actual smooth fourth-moment weight, a further hypothesis is required: $|w_D|$ must be bounded below on $\asymp D$ denominators. The frozen campaign quantities do not include $w_D$, so this is a downstream transfer condition rather than a gap in (W1-unit).

No literature theorem is used. The no-go proof is elementary once H4 and (E0) are assumed, so the campaign's separate method-literature review does not affect this adjudication.

## 7. Dependencies and exact artifacts used

Mathematical dependencies:

- `H4` and `M9-M2-beta-algebra` for the exact beta magnitude, odd support, and $\beta_1$ lower envelope;
- `H4-Phi-regularity` for the provisional positivity/continuity justification;
- `M9-M2-exact-N0-total-mass` for exact-resonance subtraction;
- `M9-M2-fourth-moment-expansion` for the cleared numerator $N$.

Selected artifacts used:

- `state/best_proof_draft.md`;
- `state/proof_obligations.yml`;
- `state/control_models.md`;
- `rounds/obligation-main/round_008/responses/A4-008.md`;
- `rounds/obligation-main/round_009/responses/A1-009.md`;
- `rounds/obligation-main/round_009/responses/A2-009.md`;
- `rounds/obligation-main/round_009/responses/A3-009.md`;
- `rounds/obligation-main/round_009/responses/A4-009.md`.

Workflow artifacts read as required:

- `protocol.md`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-weighted-mass-adjudication/briefs/hostile_lower_bound_audit.md`.

No shared proof state, synthesis, validation matrix, manifest, or proof draft was edited.

## 8. Recommended state effect

Recommendation: **revise**, with no direct state mutation by this task.

1. Reject A4-009 Claim A and Lemma A4-9.1. The asserted upper bound $D+D^4/X$ is contradicted by (1).
2. Reject A4-009 Claim B/A4-9.2 as a nonzero-band count statement. Its exhibited $DH_D^3$ family lies entirely at $N=0$.
3. Retain `M9-near-collision-absolute-lower-bounds` as `derived_under_assumptions`, not `proved_internal`, and strengthen its candidate statement: the unit-frequency W-1 family obstructs the absolute and chi-removed fat-band target for $D\ge X^{1/3+\delta}$, conditional on H4 and exact-$N=0$ closure.
4. Retain the old $D^4X^{-3/4}$ W-1 formula only as the $P\asymp H_D$ bulk-frequency specialization, not as the strongest weighted result and not as a weight-blind-only statement.
5. Keep UNC, TS, and W-1 separate with the scope ledger above. In particular, TS does not refute the fat-band budget, while UNC concerns large $M$.
6. Make no change to the signed target: none of these lower bounds controls the full true signed mass. `M9-M2-character-factor`, `M9-M2-signed-fat-band-constant`, `M9-M2`, `M9`, and the Gauss-circle target remain open.

This report should be routed to independent normalization, counting, coefficient-summation, and endpoint seam review before the coordinator considers any State Patch.
