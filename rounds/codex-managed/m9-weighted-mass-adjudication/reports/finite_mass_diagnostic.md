# Finite Mass Diagnostic

- Campaign: `m9-weighted-mass-adjudication`
- Task: `finite_mass_diagnostic`
- Role: numerical falsifier
- Graph SHA-256: `3c06ffad9c2847b329c57a8954d0758e443ee55be2da01c00ce5731bad3d6b5f`
- Status: `diagnostic_only`
- Round: Research Round 1, bounded falsification

## 1. Result

### Finite no-conflation result

On the exact finite model specified below, the raw tuple count, reciprocal absolute mass, true beta-signed mass, and unsigned beta mass are materially different at the upper endpoint. For

\[
X=625,\qquad D=25=X^{1/2},\qquad H=5,
\]

with odd two-sided frequencies, sharp half-dyadic denominators (13\le d\le25), unit (d)-weights, and the natural nonzero band

\[
0<|N|\le \left\lfloor\frac{D^4}{X}\right\rfloor=625,
\]

the exact or high-precision values are

\[
\begin{array}{c|r}
\text{quantity}&\text{value}\\ \hline
\text{raw count}&401272\\
\sum |h_1h_2h_3h_4|^{-1}&99522824/1875=53078.8394666\ldots\\
\sum \beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}&208.0987633819331\ldots\\
\sum |\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}|&269.2955165467936\ldots
\end{array}
\]

Thus the reciprocal mass/raw-count ratio is (0.1322764595\ldots), the Phi suppression factor

\[
\frac{\pi^4\sum|\beta_{h_1}\cdots\beta_{h_4}|}
{\sum|h_1h_2h_3h_4|^{-1}}
=0.4942050683\ldots,
\]

and the fixed-character cancellation ratio is

\[
\frac{|\sum\beta_{h_1}\cdots\beta_{h_4}|}
{\sum|\beta_{h_1}\cdots\beta_{h_4}|}
=0.7727524247\ldots.
\]

This is a finite counterexample to silently identifying any two of the four normalizations. It does **not** refute or prove an exponent inequality connecting them after a valid coefficient-summation argument.

### Exact pairing correction

Let

\[
B_h(w)=\sum_d w_d e(hX/(4d))
\]

and let beta satisfy beta_{-h}=beta_h in the reals. For arbitrary shared complex d-weights,

\[
\sum_{1\le |h|\le H}\beta_hB_h(w)
=2\sum_{1\le h\le H}\beta_h\sum_d w_d\cos(2\pi hX/(4d)).
\]

The cosine pairing therefore remains valid for complex (w_d). The further shortcut

\[
2\sum_{h>0}\beta_h\operatorname{Re}B_h
\]

requires real (w_d), because only then is (B_{-h}=\overline{B_h}). At the endpoint control, raw minus cosine pairing was (1.17\times10^{-69}) at 70-digit precision for shared complex weights, while raw minus the invalid (operatorname{Re}B_h) shortcut was (0.37002645\ldots). Asymmetric positive/negative (h)-weights also broke symmetric cosine pairing by (0.45508403\ldots).

This falsifies the older diagnostic expectation that shared complex (d)-weights alone should break cosine pairing. The correct failure target is the real-part shortcut, or genuinely asymmetric (h)-weights.

## 2. Exact statement and hypotheses

For each parameter row, define

\[
\mathcal D_D=\{d\in\mathbb Z:\lfloor D/2\rfloor<d\le D\},
\qquad
\mathcal H_H=\{h\in\mathbb Z:1\le |h|\le H,\ 2\nmid h\}.
\]

The raw count is coefficient-compatible: it counts ordered tuples in ((\mathcal H_H\times\mathcal D_D)^4), not even frequencies where the true beta coefficient vanishes. Put

\[
N=h_1d_2d_3d_4-h_2d_1d_3d_4+h_3d_1d_2d_4-h_4d_1d_2d_3
\]

and

\[
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad
\beta_{h,H}=-\frac{\Phi(|h|/(H+1))\chi_4(h)}{\pi h}
\quad(2\nmid h).
\]

For either (N=0) or a stated cumulative nonzero band (0<|N|\le T), the four primary quantities are

\[
\begin{aligned}
C(T)&=\sum_{\mathbf h,\mathbf d}\mathbf1_{0<|N|\le T},\\
W(T)&=\sum_{\mathbf h,\mathbf d}\frac{\mathbf1_{0<|N|\le T}}{|h_1h_2h_3h_4|},\\
S_\beta(T)&=\sum_{\mathbf h,\mathbf d}\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}\mathbf1_{0<|N|\le T},\\
A_\beta(T)&=\sum_{\mathbf h,\mathbf d}|\beta_{h_1}\beta_{h_2}\beta_{h_3}\beta_{h_4}|\mathbf1_{0<|N|\le T}.
\end{aligned}
\]

The endpoint-compatible denominator support was chosen so (d\le D\le X^{1/2}). The height rule is the nearest integer to (D/X^{1/4}), with ties upward.

| scale | (X) | (D) | (H) | exact (d)-support | natural (T=\lfloor D^4/X\rfloor) | tested (T) |
|---|---:|---:|---:|---|---:|---|
| lower | 625 | 5 | 1 | 3--5 | 1 | 1, 4 |
| crossover | 625 | 11 | 2 | 6--11 | 23 | 1, 23, 92 |
| endpoint | 625 | 25 | 5 | 13--25 | 625 | 1, 625, 2500 |

The computation also keeps (N=0) in a separate tensor; it is never merged into a nonzero band.

## 3. Derivation and exact-arithmetic method

Write (a_j=|h_j|), and let (C_{a_1,a_2,a_3,a_4}(T)) be the exact number of sign and denominator choices in the band with those four absolute frequencies. Then

\[
\begin{aligned}
C(T)&=\sum_{\mathbf a} C_{\mathbf a}(T),\\
W(T)&=\sum_{\mathbf a}\frac{C_{\mathbf a}(T)}{a_1a_2a_3a_4},\\
A_\beta(T)&=\frac1{\pi^4}\sum_{\mathbf a}
C_{\mathbf a}(T)\prod_{j=1}^4\frac{\Phi(a_j/(H+1))}{a_j},\\
S_\beta(T)&=\frac1{\pi^4}\sum_{\mathbf a}
C_{\mathbf a}(T)\prod_{j=1}^4\frac{\Phi(a_j/(H+1))\chi_4(a_j)}{a_j}.
\end{aligned}
\]

The four minus signs in beta cancel. These formulas show algebraically where raw counting, harmonic summation, Phi attenuation, and the fixed character sign enter as separate operations.

For exact enumeration set

\[
A=h_1d_2-h_2d_1,\qquad B=h_3d_4-h_4d_3.
\]

Then

\[
N=A,d_3d_4+B,d_1d_2.
\]

For every ordered denominator pair the script constructs the exact integer distribution of (A), retaining its absolute-frequency-pair multiplicities. For two denominator pairs it uses integer ceiling/floor bounds and binary search to find precisely those (B) for which (|N|\le T), rejects or separately records (N=0), and accumulates the outer product of the two multiplicity vectors. No floating-point comparison determines band membership.

If (L=\operatorname{lcm}\{a:a\in\mathcal H_H, a>0\}), then

\[
W(T)=L^{-4}\sum_{\mathbf a}C_{\mathbf a}(T)prod_{j=1}^4\frac{L}{a_j},
\]

so (W(T)) is also accumulated as an exact integer numerator and denominator. Independent literal Cartesian enumeration agreed exactly with every tensor at the lower and crossover scales. The endpoint literal enumeration was deliberately omitted under the bounded numerical mandate; it uses the same exact pair-join identity.

Phi and beta values were evaluated independently at 50 and 80 Decimal digits using Machin's formula for (pi) and Taylor sine/cosine after rational phase reduction. The largest relative 50-versus-80 digit discrepancy over all reported masses was below (6\times10^{-49}), well inside the (10^{-40}) pass threshold.

For a coefficient-sign pattern epsilon(a) in {+1,-1}, the same tensor gives

\[
S_\varepsilon(T)=\frac1{\pi^4}\sum_{\mathbf a}C_{\mathbf a}(T)
\prod_{j=1}^4\frac{\Phi(a_j/(H+1))\varepsilon(a_j)}{a_j}.
\]

The true pattern is epsilon(a)=chi_4(a). A deterministic random pattern was also tested. Brute force over all coefficient-level sign patterns confirmed the exact adversarial identity

\[
\max_\varepsilon |S_\varepsilon(T)|=A_\beta(T),
\]

because the all-positive pattern makes every summand nonnegative. Thus an unsigned estimate is literally the coefficient-sign adversarial envelope in this finite model, not evidence of fixed-(chi_4) cancellation.

## 4. Focused numerical observations

The natural-band rows were:

| scale | band | raw (C) | reciprocal (W) | signed (S_\beta) | unsigned (A_\beta) | (|S_\beta|/A_\beta) |
|---|---|---:|---:|---:|---:|---:|
| lower | (0<|N|\le1) | 0 | 0 | 0 | 0 | -- |
| crossover | (0<|N|\le23) | 264 | 264 | 0.7970016530 | 0.7970016530 | 1 |
| endpoint | (0<|N|\le625) | 401272 | 53078.8394667 | 208.0987634 | 269.2955165 | 0.7727524247 |

At the crossover row (H=2), odd support contains only (|h|=1). Therefore (C=W), and every fourfold coefficient product has the same character sign. The apparent agreement there is forced by support collapse and gives no evidence that the quantities remain comparable once (|h|=3,5) enter. The endpoint row exhibits both harmonic attenuation and character cancellation.

Band width also matters. At the endpoint, widening (T) from (625) to (2500) changed (A_\beta/D^2) from (0.4308728\ldots) to (1.5477727\ldots). The corresponding ratios to (D+D^4/X) were (0.4143008\ldots) and (1.4882430\ldots). This is a finite normalization warning, not a scale law or crossover fit.

The smallest endpoint nonzero band (0<|N|\le1) had raw count (144), reciprocal mass (4.48), signed beta mass (-0.0008850775\ldots), and unsigned beta mass (0.0012834974\ldots). In particular, a true beta-signed band mass need not be nonnegative.

## 5. First doubtful or unproved step

There is no doubtful step in the integer band classification or the displayed finite identities. The first unproved step would be any extrapolation from (X=625) to a uniform statement in (X,D,H), especially an assertion of an (X^{3/8}) transition or a bound by (D+D^4/X). This run was intentionally too small and too narrow to support exponent fitting.

Two further transfer gaps remain explicit:

1. The beta normalization is conditional on the repository's not-yet-source-validated H4/Vaaler formula.
2. The mass enumeration uses sharp unit (d)-weights on one half-dyadic support. It does not test every smooth (w_D), complex fourth-moment weight, lower-bound family, or lift multiplicity model.

## 6. Controls, rules, and outcomes

| control | pass/fail rule | outcome |
|---|---|---|
| raw-vs-weighted | endpoint natural-band reciprocal mass must be strictly below the odd-supported raw count | PASS: ratio (0.1322764595\ldots) |
| signed-vs-unsigned | triangle inequalities must hold in every band; endpoint true signed mass must differ from unsigned; include random and adversarial coefficient signs | PASS: true ratio (0.7727524\ldots), deterministic-random ratio (0.7802335\ldots), adversarial ratio (1) |
| dyadic-endpoints | run (D=X^{1/4}), rounded (D=X^{3/8}), and (D=X^{1/2}), each with its natural band | PASS |
| real-vs-complex-pairing | raw equals cosine pairing for shared real or complex (d)-weights; Re shortcut only for real weights; asymmetric (h)-weights must break symmetric pairing | PASS: complex cosine error (1.17\times10^{-69}), Re mismatch (0.3700\ldots), asymmetric mismatch (0.4551\ldots) |
| exact-vs-near | store (N=0) and (0<|N|) in disjoint exact-integer tensors | PASS |
| exact enumeration | independent literal enumeration must match the optimized pair join at the two small scales | PASS, exact tensor equality |
| precision | 50- and 80-digit beta masses agree to relative error below (10^{-40}) | PASS |

The deterministic random endpoint pattern on absolute frequencies (1,3,5) was ((-1,+1,+1)), distinct from the true ((+1,-1,+1)), unsigned, and their global negatives.

Passing these controls validates only the implementation and the finite algebraic distinctions. It does not validate an asymptotic theorem.

## 7. Dependencies and artifacts

Selected mathematical context used:

- `state/best_proof_draft.md`
- `state/proof_obligations.yml`
- `state/control_models.md`
- `rounds/obligation-main/round_003/artifacts/m9_regression/run.py`
- `rounds/obligation-main/round_003/artifacts/m9_regression/table_small.csv`
- `rounds/obligation-main/round_003/artifacts/m9_regression/precision.log`
- `rounds/obligation-main/round_003/artifacts/m9_regression/report.md`

Workflow inputs used were `protocol.md`, `state/active_campaign.yml`, and the task brief. No web sources or other Round 9 materials were used.

Task-local generated artifacts:

- `controls/finite_mass_diagnostic/run.py` — executable diagnostic
- `controls/finite_mass_diagnostic/command.txt` — exact working-directory command
- `controls/finite_mass_diagnostic/parameters.csv` — parameter table
- `controls/finite_mass_diagnostic/results.json` — full machine-readable tensors, masses, controls, and metadata
- `controls/finite_mass_diagnostic/results.csv` — compact machine-readable result table
- `controls/finite_mass_diagnostic/precision.log` — runtime and exact/precision record
- `reports/finite_mass_diagnostic.md` — this report

Run from repository root with:

```powershell
py rounds/codex-managed/m9-weighted-mass-adjudication/controls/finite_mass_diagnostic/run.py
```

The reproduced run completed all controls with exit code 0.

## 8. Limitations

- One bounded instance (X=625) was used; there was no size sweep, regression, or exponent fit.
- Raw count means odd-supported raw count. An all-frequency count would be a different normalization.
- Unit sharp (d)-weights were used for the tuple masses.
- Only (N=0), (|N|\le1), the natural band (|N|\le\lfloor D^4/X\rfloor), and four times the natural band were considered.
- Random-sign output depends on the recorded deterministic seed and is only a falsification control.
- Computation can expose a conflation or formula error but cannot prove M9, M9-M2, a uniform mass bound, or the Gauss circle target.

## 9. Recommended state effect

**No promotion; retain as `diagnostic_only`.**

The coordinator should use this report only to enforce the following seams in later analytical work:

1. write the harmonic coefficient summation before transferring any raw-count scale to a beta-weighted mass;
2. keep unsigned/adversarial mass separate from fixed-(chi_4) signed mass;
3. correct complex-weight pairing tests so that shared complex (d)-weights preserve cosine pairing while invalidating only the (operatorname{Re}B_h) shortcut;
4. treat the crossover row's single-magnitude support as degenerate rather than confirmatory;
5. keep endpoint and band-width normalizations explicit.

No change to M9, M9-M2, the near-collision estimate, endpoint uniformity, or the final target is recommended.
