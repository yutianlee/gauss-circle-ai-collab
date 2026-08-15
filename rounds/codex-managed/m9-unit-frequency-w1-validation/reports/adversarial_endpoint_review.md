# Adversarial endpoint and seam review

- Campaign: `m9-unit-frequency-w1-validation`
- Research round: `2`
- Task: `adversarial_endpoint_review`
- Role: hostile seam reviewer
- Access mode: selected context
- Graph SHA-256: `3c06ffad9c2847b329c57a8954d0758e443ee55be2da01c00ce5731bad3d6b5f`
- Status: candidate evidence only; no shared proof state edited

## 1. Result and disposition

**Disposition: REVISE, not reject.** The elementary sharp-block unit-frequency
lower bound survives the hostile review. The proof of its combinatorial core is
valid, including the Cauchy window count, ordered-pair multiplicity, and clearing
of denominators. The surviving result is conditional on three hypotheses which
must be written into the statement:

1. `h=1` is in the Fourier support and has a uniform coefficient lower bound
   \(\lvert\beta_{1,H}\rvert\ge b_0>0\);
2. the **same weighted quantity** has total exact-resonance mass
   \(\Sigma_{\rm abs}(N=0)\le C_\epsilon D^2X^\epsilon\);
3. for a weighted dyadic block, the weight has a positive-density lower level
   set. Boundedness or smoothness alone is not enough.

With those hypotheses, the sharp-block formula

\[
 \Sigma_{\rm abs}(0<|N|\le M)
 \ge c\min(D^4,MD)-C_\epsilon D^2X^\epsilon
\]

is correct. At \(M=D^4/X\) it gives a power obstruction for
\(D\ge X^{1/3+\delta}\), after an explicit choice of epsilon. It gives no
power obstruction at the exact crossover \(D=X^{1/3}\). It applies to the raw
unit-frequency count, the absolute beta-weighted mass, and a genuinely
nonnegative character-removed mass. It does **not** give a lower bound for the
full true signed quantity.

The requested revision is therefore one of exact scope, not of the window
mechanism: replace every unqualified reference to an “actual smooth block” by
the lower-level-set hypothesis below, keep both H4-dependent inputs visible,
and say \(D>X^{1/3}\) by a fixed power rather than including the exact crossover.

## 2. Strongest surviving statement

### Lemma (conditional weighted unit-frequency window lower bound)

Let \(D\ge2\), \(H\in\mathbb N\) with \(H\ge1\), and

\[
 \mathcal D_D=[D,2D)\cap\mathbb Z.
\]

Let \(w_D:\mathcal D_D\to\mathbb C\). Assume that for constants
\(\kappa,\omega,b_0>0\), independent of \(D,H,X\), the set

\[
 A_D=\{d\in\mathcal D_D:|w_D(d)|\ge\omega\}
\]

satisfies

\[
 |A_D|\ge\kappa D,
 \qquad |\beta_{1,H}|\ge b_0.
 \tag{H1}
\]

For the usual cleared numerator

\[
 N=h_1d_2d_3d_4-h_2d_1d_3d_4
   +h_3d_1d_2d_4-h_4d_1d_2d_3,
\]

define the absolute weighted mass with the same \(w_D\) and beta coefficients
by

\[
 \Sigma^w_{\rm abs}(E)
 =\sum_{({\bf h},{\bf d}):E}
   \prod_{i=1}^4|w_D(d_i)\beta_{h_i,H}|.
\]

Assume, for every fixed \(\epsilon>0\), the exact-resonance estimate

\[
 \Sigma^w_{\rm abs}(N=0)\le C_{\epsilon,w}D^2X^\epsilon.
 \tag{H2}
\]

Then for every \(M>0\),

\[
 \boxed{
 \Sigma^w_{\rm abs}(0<|N|\le M)
 \ge c(\kappa,\omega,b_0)\min(D^4,MD)
      -C_{\epsilon,w}D^2X^\epsilon.}
 \tag{W1}
\]

The intended range \(1\le M\ll D^3\) lies on the linear branch, so (W1)
becomes \(cMD-C_{\epsilon,w}D^2X^\epsilon\), up to the fixed constant in the
meaning of \(\ll\). For the sharp block \(w_D\equiv1\), (H1) holds with fixed
\(\kappa,\omega\), and this is the candidate formula in the frozen question.

The positive-density lower-level-set condition is weaker than requiring a
whole interval on which \(|w_D|\) is bounded below. No contiguity, sign, or
smoothness of \(w_D\) is needed for the **absolute** mass proof. A fixed
nonzero smooth profile \(w_D(d)=W(d/D)\) normally supplies such a set, but that
fact must be verified for the project's actual profile.

## 3. Proof and seam audit

### 3.1 Window count and ordered-pair multiplicity: passes

Restrict to \(h_1=h_2=h_3=h_4=1\) and to denominators in \(A_D\). For an
ordered pair \((a,c)\in A_D^2\), set

\[
 s(a,c)=\frac1a+\frac1c.
\]

All pair sums lie in \((1/D,2/D]\), an interval of length at most \(D^{-1}\).
Take half-open windows of length

\[
 \eta=\frac{M}{16D^4}.
\]

The number \(K\) of windows meeting the pair-sum interval satisfies

\[
 K\le 2+\frac{D^{-1}}{\eta}
   =2+\frac{16D^3}{M}.
 \tag{3.1}
\]

If \(v_j\) counts ordered pairs in the \(j\)-th window, then

\[
 \sum_jv_j=|A_D|^2\ge\kappa^2D^2.
\]

Cauchy--Schwarz gives

\[
 \sum_jv_j^2
 \ge \frac{|A_D|^4}{K}
 \ge c_0\kappa^4\min(D^4,MD).
 \tag{3.2}
\]

There is no pair-multiplicity error here. An ordered pair of ordered pairs

\[
 ((d_1,d_3),(d_2,d_4))
\]

maps bijectively to the ordered denominator quadruple
\((d_1,d_2,d_3,d_4)\). The symmetries \((d_1,d_3)\leftrightarrow(d_3,d_1)\)
produce different ordered quadruples, as the fourth-moment sum itself does.
Repeated pair sums are exact collisions, not overcounting; they are handled by
the explicit subtraction in Section 3.3.

For reference, in the sharp block \(|\mathcal D_D|\ge D/2\) for \(D\ge2\).
Equations (3.1)--(3.2) then permit a completely absolute count constant, for
example a constant no smaller than \(1/288\) before the beta factor. The exact
numeric value is immaterial, but this verifies that the lower-bound constant is
uniform in \(D,M,X,H\).

### 3.2 Denominator clearing: passes

Two pair sums in the same half-open window differ by strictly less than
\(\eta\). With

\[
 Q=d_1d_2d_3d_4<16D^4,
\]

the unit-frequency numerator is exactly

\[
 N=Q\left(\frac1{d_1}-\frac1{d_2}
             +\frac1{d_3}-\frac1{d_4}\right).
\]

Consequently every quartet counted in (3.2) satisfies \(|N|<M\). The strict
inequalities from the half-open denominator block and windows remove the only
possible boundary ambiguity. No factor of \(D\), \(H\), \(X\), or a reduced
fraction lift is missing. Since \(1/d\) is already reduced, the construction
has lift multiplicity one.

### 3.3 Exact-\(N=0\) subtraction: conditionally passes and is essential

Every same-window tuple has absolute weight at least

\[
 (\omega b_0)^4.
\]

Thus (3.2) lower-bounds the same-window mass with \(|N|\le M\), including
exact resonances. Removing exact tuples by (H2) gives (W1).

This is logically sound because the exact upper bound and the near-collision
mass use the same coefficients and the same dyadic weight. An unweighted exact
bound cannot silently be substituted for a weighted one, or conversely.

The subtraction cannot be omitted. At minimum, every identical pair of pairs
contributes an exact resonance, and further reciprocal pair-sum coincidences
also occur. Without (H2), Cauchy energy alone does not show that any positive
proportion of (3.2) has \(N\ne0\). In the lower ranges the stated error is
larger than the window main term, which is why (W1) is then true but gives no
obstruction.

### 3.4 Coefficients and support: passes only as an explicit hypothesis

Only \(h=1\) is used. Hence the proof requires \(H\ge1\) and the uniform
lower bound \(|\beta_{1,H}|\ge b_0\). The asymptotic relation
\(H_D\asymp DX^{-1/4}\) by itself does not exclude a floor or normalization
which makes \(H_D=0\) at the lower endpoint; support must be stated directly.

Under the provisional H4 formula, \(u=1/(H+1)\in(0,1/2]\), and the asserted
continuity and positivity of \(\Phi\) would give the lower envelope. This review
does not convert that provisional formula into a source-validated theorem.
`H4-source-audit` remains the first external blocker.

Coefficient phases and \(\chi_4\) signs do not affect the absolute argument,
because it uses only \(|\beta_1|^4\). If \(\beta_1=0\), the weighted conclusion
is false; thus the coefficient lower envelope is a genuine hypothesis, not a
cosmetic normalization.

### 3.5 Sharp-to-smooth transfer: requires revision

The sharp proof does not automatically transfer to every bounded or smooth
weight. The zero weight \(w_D\equiv0\) is already a smooth bounded
counterexample to an unqualified transfer, and weights supported on \(o(D)\)
denominators destroy the \(D^2\) pair population.

The weakest simple sufficient hypothesis used by the proof is exactly the
positive-density lower-level-set condition in (H1), together with the weighted
exact-resonance estimate (H2). A subinterval of \(\asymp D\) denominators with
\(|w_D|\gg1\) is sufficient but stronger than necessary. For a theorem claimed
uniformly over a class of bounded weights, the constants \(\kappa,\omega\) and
the exact-resonance constant must be uniform over that class. If a proposed
upper bound is asserted for every admissible weight and the sharp choice
\(w_D\equiv1\) is admissible, the sharp counterexample alone refutes it. It does
not by itself refute an estimate for a different fixed weight.

### 3.6 Comparison with the blind and claimant arguments: no conflict

The blind report's upper bound

\[
 \mathcal M_{\rm abs}(D,H;K)
 \ll D^3(\log(1+H))^3(1+K/D^2)
\]

is compatible with the unit-frequency lower bound. At
\(K=D^4/X\) and \(D\le X^{1/2}\), the packing factor is bounded and the upper
scale is \(D^3\log^3(1+H)\), whereas the unit lower main term is \(D^5/X\le
D^3\). At \(D=X^{1/2}\), the two polynomial scales meet at \(D^3=X^{3/2}\),
up to logarithms. The blind argument packs the fourth reduced fraction after
fixing three coordinates; the lower argument measures the collision energy of
\(D^2\) pair sums. These are different seams and neither invalidates the other.

The hostile and conductor reports use the same valid pair-sum interface audited
above. Their claims about the unit-frequency lower bound survive. Their smooth
weight discussion must be read as conditional on a lower envelope, not as a
consequence of smoothness alone. Their rejection of the older equal-denominator
nonzero family is also correct: with all denominators equal,
\(N=d^3(h_1-h_2+h_3-h_4)\), so the displayed additive relation forces
\(N=0\).

## 4. Endpoint, range, and epsilon audit

For the fat band \(M=D^4/X\), the active range \(D\ge X^{1/4}\) ensures
\(M\ge1\), while \(D\le X^{1/2}\) ensures \(M/D^3=D/X\le X^{-1/2}\). Thus
the fat band lies safely in the linear window regime. Its main term and its
ratio to the \(D^2\) exact-mass scale are

\[
 MD=\frac{D^5}{X},
 \qquad
 \frac{D^5/X}{D^2}=\frac{D^3}{X}.
\]

| \(D\) | \(M=D^4/X\) | window main term \(D^5/X\) | ratio to \(D^2\) | verdict |
|---|---:|---:|---:|---|
| \(X^{1/4}\) | \(1\) | \(X^{1/4}\) | \(X^{-1/4}\) | exact subtraction dominates; no obstruction |
| \(X^{1/3}\) | \(X^{1/3}\) | \(X^{2/3}\) | \(1\) | exact crossover only; no power obstruction |
| \(X^{3/8}\) | \(X^{1/2}\) | \(X^{7/8}\) | \(X^{1/8}\) | power obstruction if the exact-bound epsilon is \(<1/8\) |
| \(X^{1/2}\) | \(X\) | \(X^{3/2}\) | \(X^{1/2}\) | power obstruction if the exact-bound epsilon is \(<1/2\) |

The epsilon quantifiers are as follows. Fix \(\delta>0\) with a nonempty range
\(X^{1/3+\delta}\le D\le X^{1/2}\), and choose
\(0<\epsilon_0<3\delta\). Applying (H2) with \(\epsilon_0\),

\[
 \frac{D^5/X}{D^2X^{\epsilon_0}}
 =\frac{D^3}{X^{1+\epsilon_0}}
 \ge X^{3\delta-\epsilon_0}\longrightarrow\infty.
\]

Hence for sufficiently large \(X\), (W1) yields
\(\Sigma_{\rm abs}\ge(c/2)D^5/X\), uniformly over that \(D\)-range. A
purported upper bound \(\Sigma_{\rm abs}\ll_\epsilon D^2X^\epsilon\) for every
\(\epsilon>0\) is then contradicted by choosing any target epsilon
\(<3\delta\). At \(D=X^{1/3}\) there is no positive exponent margin, and the
\(X^\epsilon\) exact-subtraction term prevents this conclusion.

## 5. Scope across the four quantities

### Weight-blind raw nonzero tuple count

For the sharp block, (3.2) is already a raw same-window count. The exact raw
count within the unit family is at most

\[
 b_0^{-4}\Sigma_{\rm abs}(N=0),
\]

so (H2) also gives the analogous raw nonzero lower bound. This comparison is
valid only because every selected tuple has the fixed coefficient
\(|\beta_1|^4\ge b_0^4\); it is not a general raw-to-weighted transfer.

### Absolute beta-weighted mass

This is the direct content of (W1). Coefficient signs, random phases, and
adversarial phases of the same magnitude do not change it.

### Character-removed unsigned mass

If “unsigned” means the nonnegative mass formed from coefficient magnitudes,
the same proof applies verbatim. If it instead means merely deleting
\(\chi_4\) algebraically, then positivity of the remaining \(\Phi\) factors and
of any non-absolute dyadic factors must be stated; otherwise a positive
unit-frequency subtotal need not lower-bound the full sum. Under the intended
Vaaler positivity and a genuinely nonnegative definition, the unit family is
identical to the absolute family.

### Full true signed quantity

The argument gives no lower bound. The \(h_i=1\) subtotal has positive
coefficient product, but the complementary frequencies can cancel it. The
inequality “full signed sum is at least a positive subtotal” is unavailable.
Random-sign and adversarial-sign controls make the same logical failure
immediate. No conclusion follows for `M9-M2-character-factor`, the signed
fat-band constant, pointwise M2, M9, or the Gauss-circle target.

## 6. Counterexample attempts and required controls

| Control / attempted break | Exact input | Outcome | Implication |
|---|---|---|---|
| Window-count constants | Half-open windows of width \(M/(16D^4)\) over pair sums in an interval of length \(D^{-1}\) | Passes: \(K\le2+16D^3/M\) | Gives the claimed \(\min(D^4,MD)\) energy |
| Pair multiplicity | Ordered pairs \((d_1,d_3)\), \((d_2,d_4)\) | Passes: mapping to ordered quadruples is bijective | No missing or duplicated multiplicity factor |
| Denominator boundary | \(d_i\in[D,2D)\), same half-open window | Passes: \(Q<16D^4\) and the phase difference is \(<M/(16D^4)\) | Gives \(|N|<M\) with room at the endpoint |
| Exact versus near | Include identical pair-pairs and other equal pair sums | Would fail without (H2); passes conditionally after global exact-mass subtraction | (H2) is indispensable and must match the weight |
| Coefficient adversary | Set \(\beta_1=0\), or take \(H=0\) | Falsifies the weighted conclusion | \(H\ge1\) and \(|\beta_1|\ge b_0\) are indispensable |
| Smooth-weight adversary | \(w_D\equiv0\), or support on \(o(D)\) denominators | Falsifies an unqualified smooth/bounded-weight transfer | Require a uniform positive-density lower level set |
| Raw versus weighted | Restrict all four frequencies to \(1\) | Passes only for this fixed-frequency family | No general raw-to-weighted exponent transfer is licensed |
| Signed versus unsigned | Keep the positive \(h=1\) subtotal but allow complementary true beta signs | Fails as a signed lower-bound argument | The true signed quantity remains excluded |
| Dyadic endpoints | \(D=X^{1/4},X^{1/3},X^{3/8},X^{1/2}\) | Outcomes are the table in Section 4 | Only \(D>X^{1/3}\) by a fixed power gives the claimed obstruction |
| Support and degeneracy | \(h=1\), repeated denominators, dyadic edges, reduced-fraction lifts | Passes: no lift or \(uv=0\) branch arises; repeated-denominator exact cases are subtracted | No hidden degeneracy remains in the unit family |

No numerical experiment was used. All controls above are analytical.

## 7. First doubtful or unproved step

The window/Cauchy/denominator-clearing derivation has no doubtful step. The
first unverified input is the H4/Vaaler normalization needed to certify a
uniform \(|\beta_{1,H}|\) lower envelope and \(h=1\) support. The next
conditional input is `M9-M2-exact-N0-total-mass`, which is currently
`derived_under_assumptions` and H4-dependent. For transfer to the actual M2
weight, the first project-specific step is verification of a uniform
positive-density lower level set and availability of (H2) for that exact
weight.

## 8. Dependencies and exact artifacts used

Workflow instructions read:

- `protocol.md`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-unit-frequency-w1-validation/briefs/adversarial_endpoint_review.md`.

Selected mathematical context read, and no other campaign derivation used:

- `state/proof_obligations.yml`;
- `state/control_models.md`;
- `state/validation_matrix.yml`;
- `rounds/codex-managed/m9-weighted-mass-adjudication/reports/blind_weighted_upper_bound.md`;
- `rounds/codex-managed/m9-weighted-mass-adjudication/reports/hostile_lower_bound_audit.md`;
- `rounds/codex-managed/m9-weighted-mass-adjudication/reports/conductor_independent_analysis.md`;
- `rounds/codex-managed/m9-weighted-mass-adjudication/synthesis.md`.

No literature theorem or numerical computation was used in this seam review.

## 9. Recommended state effect

**Revise.** Retain the unit-frequency W-1 mechanism and its sharp-block
conditional lower bound as candidate evidence. State the positive-density
weight hypothesis, \(H\ge1\), the beta-1 lower envelope, and the matching
weighted exact-resonance closure explicitly. Record the power obstruction only
for \(D\ge X^{1/3+\delta}\) with epsilon chosen below \(3\delta\), not at the
exact \(X^{1/3}\) crossover. Keep the result restricted to raw/absolute and
genuinely nonnegative character-removed quantities. Make no signed, pointwise,
M9-M2, M9, or final-theorem promotion.

