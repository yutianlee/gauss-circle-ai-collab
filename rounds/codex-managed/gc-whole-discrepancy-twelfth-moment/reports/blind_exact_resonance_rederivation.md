# Round 201: independent absolute exact-resonance rederivation

## 1. Result: lemma

- Campaign: `gc-whole-discrepancy-twelfth-moment`.
- Task: `blind_exact_resonance_rederivation`.
- Role/status: statement-only blind rederiver; candidate evidence only.
- Graph SHA-256 supplied for provenance, not inspected: `2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5`.
- Generated: `2026-09-23 12:18:48 UTC`.
- Allocation: analytical/algebraic only; no numerical experiments or external-source imports.

The proposed divisor-envelope bound is true for every fixed integer k >= 2. The broader squarefree-class l2 statement is also true, including odd k. The proof includes all exact resonances, not merely pairings, and extends to infinite sequences by monotone convergence. It is uniform under arbitrary, independently chosen restrictions on the indices in different positions.

For a finite cosine sum, the signed exact-frequency coefficient has the prescribed complex cosine phases and absolute value bounded by the proved mass. For real coefficients and even k, its *total* coefficient is nonnegative, although individual exact-resonance summands can be negative. No estimate of any nonzero frequency, finite-window moment, whole discrepancy, or pointwise exponent follows from this lemma alone.

## 2. Exact statement and hypotheses

Write every positive integer uniquely as n = d s^2, where d is positive squarefree, s is a positive integer, and d = 1 is allowed. For a complex sequence a, put

\[
 A_d=\sum_{s\ge1}|a_{ds^2}|,\qquad
 S=\sum_{d\ \mathrm{squarefree}}A_d^2.
\]

Let b_k be the number of set partitions of {1,...,k} whose blocks all have size at least two. Define the nonnegative, possibly initially extended-valued series

\[
 M_k(a)=\sum_{\epsilon\in\{-1,1\}^k}
 \sum_{\sum_j\epsilon_j\sqrt{n_j}=0}\prod_{j=1}^k|a_{n_j}|.
\]

**Lemma A.** If S is finite, then

\[
 M_k(a)\le 2^k b_k S^{k/2}.                         \tag{1}
\]

More generally, for k sequences a^(j) with corresponding class masses A_(j,d) and S_j = sum_d A_(j,d)^2, the mixed mass satisfies

\[
 \sum_\epsilon\sum_{\sum_j\epsilon_j\sqrt{n_j}=0}
 \prod_j|a^{(j)}_{n_j}|
 \le 2^k b_k\prod_j S_j^{1/2}.                    \tag{2}
\]

These statements apply to finite or infinite sequences. Restricting each n_j to any prescribed subset, including unequal finite intervals, preserves the estimate.

**Lemma B.** If |a_n| <= C tau(n) n^(-3/4), then

\[
 S\le C^2\zeta(3/2)^{10},\qquad
 M_k(a)\le 2^k b_k C^k\zeta(3/2)^{5k}.             \tag{3}
\]

The constants in (3) are explicit convenient upper bounds, not sharp constants. They are independent of support and cutoff.

**Finite moment statement.** Define e(x) = exp(2 pi i x) and

\[
 \widehat w(\xi)=\int_{\mathbb R}w(u)e(-u\xi)\,du.
\]

For a finitely supported sequence, T > 0, and w in C_c^infinity(R), set

\[
 H(R)=\sum_n a_n\cos(2\pi R\sqrt n-3\pi/4).
\]

The exact-frequency part of the expansion of integral w(R/T) H(R)^k dR is

\[
 D_k(T)=T\widehat w(0)E_k(a),\qquad
 E_k(a)=2^{-k}\sum_\epsilon\sum_{\Delta=0}
      e\!\left(-\frac38\sum_j\epsilon_j\right)\prod_j a_{n_j},
 \quad \Delta=\sum_j\epsilon_j\sqrt{n_j}.           \tag{4}
\]

Consequently

\[
 |D_k(T)|\le T|\widehat w(0)|b_k S^{k/2}
 \le T\|w\|_1 b_k C^k\zeta(3/2)^{5k}              \tag{5}
\]

under the respective hypotheses. For real a_n and even k, E_k(a) >= 0. If w is also nonnegative, D_k(T) >= 0. These are assertions about the summed exact contribution, not about each summand.

For complex coefficients, (4) concerns H^k; its coefficient need not be nonnegative. If the requested moment instead means |H|^(2m), use m coefficient factors a and m conjugate factors in (4). The same absolute bound applies, and the total exact coefficient is then nonnegative. Infinite-sequence versions of E_k are defined by their absolutely convergent exact-resonance series; existence or convergence of the full infinite H is not a hypothesis or conclusion of this report.

## 3. Proof or derivation

### Rational independence, with the squarefree class 1 included

Here is a self-contained field argument; independence is not assumed. Given finitely many distinct primes p_1,...,p_r, put K_j = Q(sqrt(p_1),...,sqrt(p_j)). We prove simultaneously:

1. [K_j:Q] = 2^j, with Q-basis the products of distinct radicals sqrt(p_i), including the empty product 1.
2. For a nonzero rational q, q is a square in K_j if and only if q = c^2 product_(i in I) p_i for some nonzero rational c and I contained in {1,...,j}.

Both assertions hold for j = 0. Suppose they hold for j - 1. The second assertion and unique prime factorization show that p_j cannot be a square in K_(j-1): its p_j-adic valuation is odd, whereas every proposed rational-square-times-prior-primes expression has even p_j-adic valuation. Thus adjoining sqrt(p_j) is a quadratic extension. This proves the degree and basis assertion at j.

If x in K_j satisfies x^2 = q in Q, write uniquely x = u + v sqrt(p_j) with u,v in K_(j-1). Comparison in this quadratic basis gives 2uv = 0. As a field has no zero divisors, either v = 0, so q = u^2, or u = 0, so q/p_j = v^2. Apply the induction hypothesis in each case. The converse follows by explicitly taking the product of the indicated radicals. This proves the second assertion and closes the induction.

Now take the finite set of primes dividing any finite collection of distinct positive squarefree integers d. Each sqrt(d) is a distinct member of the preceding basis. They are therefore linearly independent over Q. The d = 1 radical is the empty basis monomial, so it has not been omitted.

It follows, for every tuple and sign vector, that

\[
 \sum_j\epsilon_j\sqrt{n_j}=0
 \quad\Longleftrightarrow\quad
 \sum_{j:d_j=d}\epsilon_j s_j=0
 \quad\hbox{for every squarefree }d,\qquad n_j=d_js_j^2.       \tag{6}
\]

Each nonempty class in (6) has at least two positions, since s_j > 0. There is no conclusion that it has exactly two positions or that its members pair.

### Bounding all class partitions

First take finite supports. Partition the positions {1,...,k} by equality of their squarefree labels d_j. Equation (6) implies that the resulting partition has no singleton blocks. Each tuple has exactly one such partition.

Fix a sign vector and such a partition pi. For a block B, summing the product of coefficient magnitudes over its s variables subject to its signed integer equation is at most the unrestricted product of the class masses. Thus, in the mixed setting, the contribution is bounded by

\[
 \sum_{\substack{(d_B)_{B\in\pi}\text{ pairwise distinct}}}
       \prod_{B\in\pi}\prod_{j\in B} A_{j,d_B}
 \le \prod_{B\in\pi}\left(\sum_d\prod_{j\in B}A_{j,d}\right). \tag{7}
\]

The inequality drops only a distinctness restriction from nonnegative sums. For m = |B| >= 2, Holder's inequality and the l2-to-lm norm inequality give

\[
 \sum_d\prod_{j\in B}A_{j,d}
 \le\prod_{j\in B}\left(\sum_d A_{j,d}^{m}\right)^{1/m}
 \le\prod_{j\in B}S_j^{1/2}.                              \tag{8}
\]

For completeness, the last inequality follows from
sum_d x_d^m <= (sup_d x_d)^(m-2) sum_d x_d^2 <= (sum_d x_d^2)^(m/2)
for nonnegative x and m >= 2, with the m = 2 case an equality. Combining (7) and (8), then summing over the b_k partitions and 2^k sign vectors, proves (2). Taking all sequences equal proves (1).

This bound deliberately retains the full absolute mass. No coefficient sign, character cancellation, probabilistic independence, or pairing reduction is used.

### The divisor envelope implies the needed class norm

Let tau_r(n) count ordered r-tuples of positive integers with product n. Prime-power comparison gives

\[
 \tau(ds^2)\le\tau(d)\tau(s^2),\qquad
 \tau(s^2)\le\tau_3(s).
\]

The second assertion follows from 2e+1 <= (e+1)(e+2)/2 at every prime exponent e >= 0. Absolute positivity of the sums gives

\[
 \sum_{s\ge1}\tau_3(s)s^{-3/2}=\zeta(3/2)^3.
\]

Therefore

\[
 A_d\le C\tau(d)d^{-3/4}\zeta(3/2)^3.                       \tag{9}
\]

For squarefree d, tau(d)^2 = 4^(omega(d)) = tau_4(d), including d = 1. Consequently

\[
 \sum_{d\ \mathrm{squarefree}}\tau(d)^2d^{-3/2}
 \le\sum_{d\ge1}\tau_4(d)d^{-3/2}
 =\zeta(3/2)^4.
\]

Squaring (9) and summing proves S <= C^2 zeta(3/2)^10. Equation (3) follows from (1). These Dirichlet-series identities are just repeated multiplication of the convergent positive series sum_n n^(-3/2); no external number-theoretic theorem is imported.

### Unequal ranges, infinite limits, and exact-series tails

Replacing a^(j)_n by a^(j)_n times the indicator of any position-specific set only decreases its class masses. This proves all asserted range uniformity, even when the ranges have no common scale.

For infinite sequences, truncate every sequence to n <= N. The nonnegative masses increase to the full mixed mass, while every truncated S_j is at most S_j. Monotone convergence proves (1) and (2) for infinite sequences. The limiting statements are therefore unconditional under their displayed norm hypotheses.

There is also a useful explicit continuity statement. Define

\[
 A_d^{>N}=\sum_{s:ds^2>N}|a_{ds^2}|,\qquad
 S_{>N}=\sum_d(A_d^{>N})^2.
\]

Every A_d is finite if S is finite. Hence A_d^(>N) tends to zero pointwise in d and is bounded by A_d; dominated convergence for the series yields S_(>N) -> 0. A union bound on which position exceeds N, followed by (2), gives

\[
 \sum_\epsilon\sum_{\substack{\Delta=0\text{ and}\max_jn_j>N}}
      \prod_j|a_{n_j}|
 \le k\,2^k b_k\,S_{>N}^{1/2}S^{(k-1)/2}\longrightarrow0.   \tag{10}
\]

With a fixed divisor-envelope constant C, the right side can use the tail class masses of b_n = C tau(n)n^(-3/4). By the proved result those masses have finite square sum. This makes exact-resonance tail convergence uniform over the entire coefficient family with that envelope. No quantitative decay rate or nonzero-frequency tail estimate is asserted.

### Cosine phases, Fourier normalization, and positivity

The elementary identity

\[
 \cos(2\pi R\sqrt n-3\pi/4)
 =\tfrac12\sum_{\epsilon=\pm1}e(\epsilon R\sqrt n)e(-3\epsilon/8)
\]

gives, for finite sums,

\[
 \int w(R/T)H(R)^k\,dR
 =T2^{-k}\sum_\epsilon\sum_{n_1,\ldots,n_k}
   \left(\prod_j a_{n_j}\right)
   e\!\left(-\tfrac38\sum_j\epsilon_j\right)
   \widehat w(-T\Delta).                                  \tag{11}
\]

The change of variable R = Tu fixes both the factor T and the minus sign in the Fourier argument. Keeping precisely Delta = 0 gives (4); absolute values and (1) give (5).

To prove the qualified positivity assertion without a finite-interval independence assumption, take the finitely many squarefree classes present and introduce one torus coordinate x_d in R/Z for each. Put

\[
 F(x)=\sum_d\sum_s a_{ds^2}\cos(2\pi s x_d-3\pi/4).
\]

Expansion and coordinatewise Fourier orthogonality show

\[
 \int_{(\mathbb R/\mathbb Z)^D}F(x)^k\,dx=E_k(a),           \tag{12}
\]

because its constant-term conditions are exactly the class equations (6). If all a_n are real and k is even, F(x)^k is nonnegative, proving E_k(a) >= 0. This is an algebraic torus integral, not a claim that R on a fixed interval has a uniform torus distribution. For complex a and |H|^(2m), apply the same argument to |F|^(2m). For complex a and H^k, positivity is false: a single nonzero coefficient a_1 = exp(i pi/k) gives a_1^k = -1 times the positive even cosine constant coefficient.

By (10), the signed exact series converges absolutely and its finite-support coefficients converge. Thus the total-coefficient positivity for real a and even k also survives the infinite limit. This conclusion does not construct an infinite torus function or the infinite cosine sum.

## 4. First doubtful or unproved step

There is no unproved step identified inside Lemmas A and B or the finite expansion (11). Their extension to the infinite *exact-resonance series* is justified by positivity and the proved tail bound.

The first genuinely unproved extension would be to estimate the nonzero-frequency part

\[
 T2^{-k}\sum_\epsilon\sum_{\Delta\ne0}
   \left(\prod_j a_{n_j}\right)
   e\!\left(-\tfrac38\sum_j\epsilon_j\right)
   \widehat w(-T\Delta).                                  \tag{13}
\]

Neither radical independence nor the class l2 norm controls small nonzero Delta. No bound on (13), no interchange involving an unproved infinite H expansion, and no twelfth-moment theorem is supplied. Likewise, this report does not derive a smoothed Bessel expansion of the discrepancy or bound its error terms. The supplied graph was deliberately not inspected, so downstream claims cannot be declared discharged here.

## 5. Control tests and outcomes

All controls below are exact analytical checks, not numerical evidence.

| Control | Outcome and scope |
| --- | --- |
| `whole_discrepancy_scope` | PASS as a scope guard: the result concerns precisely the exact-frequency subseries. It makes no whole-discrepancy moment claim. |
| `fixed_window_smoothing` | PASS for the finite Fourier identity (11), valid for any stated w and T. No distributional independence on the fixed radius interval is assumed. Derivation of a smoothing formula for the discrepancy is outside this task. |
| `inclusive_jump_error` | NOT AUDITED: no lattice jump approximation is used or asserted. This report cannot discharge that separate control. |
| `bessel_and_fourier_normalization` | Fourier part PASS: factors 2^(-k), T, phase e(-3 sum(epsilon)/8), and argument -T Delta are derived explicitly. Bessel normalization is NOT AUDITED and is not needed for this lemma. |
| `uniform_tail_control` | PASS for exact resonances: (10) gives convergence, uniform under a common divisor envelope. It does not control the offdiagonal tail or the full cosine series. |
| `all_sign_patterns` | PASS: all 2^k signs occur in (1), (2), and (11). All-equal signs have no resonance because n_j > 0. No zero-frequency sign pattern has been silently removed. |
| `nonpairing_exact_resonances` | PASS: sqrt(1) + sqrt(4) - sqrt(9) = 0 and sqrt(1) + sqrt(16) - sqrt(4) - sqrt(9) = 0 are included through a single block of size three or four. They disprove a pairing-only characterization. |
| `displaced_offdiagonal_phase` | PASS as a scope guard: (13) retains the precise complex phase and Fourier factor. No positivity or cancellation claim about that sum is inferred. |
| `second_moment_normalization` | PASS: at k = 2 the only possibilities have opposite signs and equal n, so M_2(a) = 2 sum_n |a_n|^2. For H^2, E_2 = (1/2) sum_n a_n^2; for real a, or the absolute-square moment with complex a, this is the expected (1/2) sum_n |a_n|^2. |
| `moment_to_pointwise_exponents` | NOT INVOKED: obtaining O(T) for the exact part alone establishes no eta and no pointwise exponent. In particular eta = 0 cannot be entered into the supplied bridge using this result alone. |
| `primary_source_hypotheses` | PASS without an external source: the radical independence and divisor summability proofs are self-contained; only elementary field algebra, Holder, Fourier orthogonality, and monotone/dominated convergence are used. |
| `no_parent_or_exponent_overclaim` | PASS: no parent obligation, M1/M2 interface, offdiagonal estimate, finite-window moment, or target exponent is claimed. |

Additional controls:

- **Class 1:** explicitly the empty prime-radical monomial in the independence proof; all displayed nonpairing examples lie in this class and are admissible.
- **Unequal ranges:** the mixed inequality (2) permits separate arbitrary supports in every position. No dyadic comparability is needed.
- **Negative exact summand at k = 12:** take eight positively signed copies of n = 1 and four negatively signed copies of n = 4. Then Delta = 8 - 8 = 0, sum(epsilon) = 4, and the phase is e(-12/8) = -1. For positive a_1,a_4 the displayed ordered summand is negative. Thus total positivity cannot be justified by termwise positivity, even for positive coefficients.
- **No special arithmetic cancellation:** the absolute lemma is also valid for arbitrary signs and for unsigned coefficients under the same envelope. This is consistent because only exact resonances are bounded; it does not assert the stronger unsigned/adversarial finite-window estimates prohibited by the protocol.

## 6. Dependencies and exact artifacts used

Read exactly:

1. `protocol.md`.
2. `rounds/codex-managed/gc-whole-discrepancy-twelfth-moment/briefs/blind_resonance_statement.md`.
3. `rounds/codex-managed/gc-whole-discrepancy-twelfth-moment/briefs/blind_exact_resonance_rederivation.md`.

No authoritative graph, active manifest, strategy review, other report, historical derivation, or outside source was read. The graph hash in Section 1 is only the supplied provenance value. No computation is used as mathematical evidence, and no shared state has been edited.

Mathematical dependencies are unique prime factorization, basic quadratic-extension algebra, the elementary divisor inequalities proved above, Holder's inequality, Fourier orthogonality for finite trigonometric polynomials, and monotone/dominated convergence for nonnegative series. In an application to the supplied coefficients a_n(T), a uniform bound of the displayed divisor-envelope form remains the application's hypothesis; full discrepancy expansions and their errors are separate dependencies.

## 7. Recommended state effect

**Promote**, subject to the conductor's required independent seam review and graph-validation procedure, only the isolated exact-resonance lemma (1), its divisor-envelope corollary (3), and the carefully qualified exact-frequency consequence (4)-(5). The broader squarefree-class l2 formulation is proved and can be retained as the clean reusable interface.

**No change** to any whole-discrepancy twelfth-moment, signed nonzero-frequency, pointwise-exponent, or parent obligation. The sign-sensitive offdiagonal sum (13), including its near-zero frequencies and uniform tails, remains completely outside the proved claim. Stop after this report; no next round is proposed.
