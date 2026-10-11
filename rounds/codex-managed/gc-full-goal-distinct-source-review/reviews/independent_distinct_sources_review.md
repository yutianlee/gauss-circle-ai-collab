## 1. Result and verdict

**GREEN** for the bounded source/applicability and mathematical claims in
`reports/distinct_correlation_sources.md`, frozen SHA256
`45ec295cc04a23d061f7278015327af9ff7e4884c902c05319fb3629ed64bc59`.

Campaign `gc-full-goal-distinct-source-review`, round217; reviewer
`full_frontier_sources`; generated2026-09-28. This is a nonblind
cross-source review, independent of the claimant's derivation but not
statement-only. Zero mathematical experiments. No original report,
shared state, synthesis or other current artifact was changed.

The two source stops are accurate. The formal sign-product argument
remains valid when squareclasses are multiplicatively dependent. The
finite-window, coefficient, full-tail and hypothetical positive-count
costs are correct. The no-bootstrap formula has the claimed strict sign.
The claimant proves no bound for the missing actual signed integral and
does not misclassify these certificate failures as such a bound.

## 2. Exact scope and hypotheses checked

The review concerns the actual fixed radial mollifier and positive-radius
window of216, real T>=2, coefficients
`a_n=r2(n)n^(-3/4)Psi(sqrt(n/T))`, all harmonics `n=ds^2`, and ordered
pairwise distinct squarefree d. The p=12 cutoff is exactly
`Q=floor(T^(2/5))`. The Fourier convention is `e(t)=exp(2pi it)` and
`w-hat(x)=integral w(u)e(-xu)du`.

The claimant's conclusion is a no-import/no-gain audit. Its elementary
spacing lemma applies to every fixed p>=2, positive integer n_j<=U
with distinct squarefree parts, and every sign vector. Its positive
spacing comparison is explicitly an additional hypothetical upper
bound, not an invoked theorem. Existing complete moment and pointwise
inputs retain their qualified Li--Yang dependency.

Current official records were checked directly: Xiao2606.28986 has only
v1,27June2026; Zhai0805.1270 has only v1,9May2008, with journal reference
Acta Arithmetica114(2004),35--54. Neither record is withdrawn. This review
checks source statements and their application hypotheses, not the full
external proof internals.

## 3. Independent verification and derivation

**Xiao source.** The primary [v1 text, definitions(1.1)--(1.2) and
Theorem1.2](https://arxiv.org/html/2606.28986v1#S1.SS1) agrees with the
claimant: the integer h fourth moment of the unweighted sum over
`n/2<=a<=n` is bounded by `H n^(2+epsilon)` only for
`n^(1/2+delta)<=H<=n^(2/3)`, with `0<delta<1/6`. Section3.8 labels its
all-order ideal estimate Conjecture3.15. The physical test n~T,H~T
violates the upper range by a fixed power. Replacing h by h+t introduces
coefficient phases `e(t sqrt(a))`; the theorem stated here is not a
weighted or continuous-radius sampling theorem. Thus the claimed first
failure is valid without deciding any extension of Xiao's method.

**Zhai source.** The [primary v1 PDF](https://arxiv.org/pdf/0805.1270v1),
printed pages2 and6, gives P(x)=sum_(n<=x)r(n)-pi x, and Theorem3
requires an optimal absolute A0-moment with A0>9. Its conclusion is for
integer `3<=k<A0`, with constant
`(-1)^k B_k(r)/[(1+k/4)2^(k-1)pi^k]` and the claimant's delta1.
The definitions of K0,b,sigma match, including the equality endpoint in
the second sigma branch. For k=12, A0>12 is indispensable. Adding the
origin changes P by1, so the elementary power inequality preserves the
absolute-moment hypothesis. The source has not provided the missing
higher optimal absolute moment through its own conclusion.

**Fourier normalization.** Expanding each cosine as half of its two
complex exponentials gives the factor2^(-p), the phase
`e(-3 sum eps_j/8)`, and after R=Tu the kernel
`T w-hat(-T Delta)`. Reality follows by replacing every eps_j by its
negative and using real w and a_n. It does not give positivity. The
positive-radius displacement of w is retained in that Fourier transform.

**Algebraic spacing without a Galois-independence assumption.** Work first
in the polynomial ring Z[x_1,...,x_p] and form

    F(x)=product_(eta in{+-1}^p)(eta_1 x_1+...+eta_p x_p).

Changing the sign of any x_j permutes the factors. Hence every monomial
in F has even exponent in each variable, and
`F in Z[x_1^2,...,x_p^2]`. Evaluation at x_j=sqrt(n_j) is an integer.
Distinct squarefree radicals are linearly independent over Q; multiplying
their coefficients by positive s_j changes neither that fact nor the
nonvanishing of any formal signed factor. The resulting integer is
nonzero and has modulus at least1.

Fix Delta equal to one factor. Its opposite is another factor, including
when the actual field has fewer than2^p automorphisms. With
`B=p sqrt(U)`, the remaining2^p-2 factors have modulus at most B. Thus

    1 <= |Delta|^2 B^(2^p-2),
    |Delta| >= B^(-(2^(p-1)-1)).

This argument uses a formal invariant polynomial, not a claim that all
formal sign changes are field automorphisms. For example squareclasses
2,3,6 are multiplicatively dependent, but their three radicals remain
linearly independent, so the same proof applies. The p=2 bound is
`1/(2sqrt(U))`, in agreement with rationalizing two unequal roots.

**Window and coefficient costs.** Since w is smooth and compactly
supported, direct integration and one integration by parts respectively
give `T||w||_1` and `||w'||_1/(2pi|Delta|)`. The coefficient sum is
`sum_(n<=U)|a_n|<<U^(1/4+epsilon)`. Applying the former or latter bound
uniformly to the same finite expansion proves

    |I_p,U| << U^(p/4+epsilon) min(T,U^A_p),
    A_p=(2^(p-1)-1)/2.

At p=12, A_p=2047/2 and p/4+A_p=2053/2. Its second branch reaches the
desired T^(29/25) only at `U<=T^(58/51325)` at power level. The first
branch requires `U<=T^(4/75)`. Both are below the nonempty retained
range U>Q~T^(2/5). Repeating integration by parts supplies
`T U^(p/4+epsilon)(U^A_p/T)^m`; its favorable power regime again requires
`U=T^eta` with eta<1/A_p. Constants depending on the fixed order m are
not uniform gains when U grows faster. This verifies the claimant's
certificate limitation, without lower-bounding the actual signed sum.

**Infinite harmonics and unequal blocks.** Let
`A(T)=sum_n|a_n(T)|<<T^(1/4+epsilon)` and
`A_tail(T)=sum_(n>T^(3/2))|a_n(T)|<<_B T^(-B)` for arbitrary fixed B.
Every omitted ordered p-tuple contains at least one tail coordinate.
Its absolute product sum is at most `p A_tail A^(p-1)`, even after
imposing distinct squarefree parts. Integration multiplies by O(T).
Choose B greater than any required fixed exponent plus (p-1)/4; all
omitted harmonics are then negligible. Nothing grants this tail estimate
at the much smaller cutoff required by the algebraic certificate. No
equal-block assumption appears in the union bound.

**Hypothetical positive count.** At a dyadic block N the p-fold absolute
coefficient costs `N^(-3p/4+epsilon)`. If the posited count were
`N^epsilon[N^(p/2)+h N^(p-1/2)]`, applying it at h=1/T and successive
dyadic shells with rapidly decreasing Fourier weight gives

    T N^(-3p/4)[N^(p/2)+T^(-1)N^(p-1/2)]N^epsilon
      <<T^epsilon[T N^(-p/4)+N^(p/4-1/2)].

The same calculation works with all finitely many sign patterns. At
p=12,N~T the second price is T^(5/2). It remains a term in this
hypothesized upper-certificate calculation after distinctness is imposed
unless a stronger count or signed argument is supplied. The report
correctly asserts neither that count nor a matching lower bound.

**No-bootstrap algebra.** Put `theta=1/4+beta/2` and
`q_star=2+1/beta`. The existing radius moment has
`E(p)=max(1,(p-2)beta)`. Restoring amplitude, Jacobian and sharp smoothing
gives the stated Theta(p). Above q_star, direct subtraction yields

    (p+1)(Theta(p)-theta)=1/4-3beta/2 > 0.

Below q_star, Theta(p)=1/4+3/[4(p+1)] decreases in p and is still larger
than theta at the endpoint by the same identity. The accepted beta is
between1/8 and13/100, hence beta<1/6 and q_star is strictly between9
and10. The source hypothesis is therefore available from the inherited
family only below ten. The prospective p=12 milestone yields sharp
exponent102/25=4+2/25, not the optimal exponent4. Neither that nonoptimal
moment nor Zhai's lower-order output supplies an optimal A0>12 input.

## 4. First open step and limits of this verdict

The first unresolved estimate remains the full one-sided signed I12 at
T^(29/25+epsilon), with its displaced window and thin near-zero scale.
The source range and higher-moment-premise failures are explicit and
unchanged by the elementary algebra. A new complete arithmetic estimate
is required before either a fixed milestone or any recursion can start.

GREEN is limited to the two exact source statements, the failed transfers,
the algebraic certificate, tails, hypothetical upper-cost comparison and
no-bootstrap computation. It does not accept Xiao's or Zhai's proof
internals as a newly audited external dependency, certify every metadata
screen in the claimant's bibliography, or promote any conjectural count.
No assertion about the isolated task's optimized general-order bound is
reviewed here.

## 5. Controls and outcomes

| Control | Review result |
|---|---|
| Actual coefficients and Fourier convention | GREEN: r2 multiplicities and fixed Psi remain; phase2pi and factor2^(-p) correct. |
| Multiplicatively dependent squareclasses | GREEN: formal polynomial invariance avoids an invalid field-degree argument. |
| Harmonic sizes and infinite tails | GREEN: n=ds^2 is the bounded variable; the full tail costs p A_tail A^(p-1) times T. |
| Finite window versus torus | GREEN: integration-by-parts rate explicitly depends on growing U. |
| Positive versus signed statement | GREEN: hypothetical count and upper certificates are never signed lower bounds. |
| Source ranges and normalization | GREEN: Xiao fourth order has its upper range; Zhai k<A0 and the optimal absolute-moment premise remain. |
| No-bootstrap restoration | GREEN: exact positive difference and smoothing floor checked. |
| Real endpoints and all complements | GREEN: no integer sampling replacement or harmonic deletion is granted. |
| Full-quarter and parent scope | GREEN: fixed12 is a milestone; M1/M2/GAR and the complete higher-order family remain open. |
| Independent-review status | NONBLIND: claimant text read; no statement-only status claimed. |

All these checks are algebraic or primary-source inspections. There was no
numerical experimentation and no inference from a finite computation to
an asymptotic statement.

## 6. Exact artifacts and sources used

Reviewed claimant:
`rounds/codex-managed/gc-full-goal-distinct-source-review/reports/distinct_correlation_sources.md`.
Its bytes were rehashed before review closure and match
`45ec295cc04a23d061f7278015327af9ff7e4884c902c05319fb3629ed64bc59`.

Original permitted context was retained from the earlier assigned task:
protocol, the frozen graph/manifest, round217 strategy,23September strategy,
214 checkpoint,216 synthesis, the complete moment and distinct kernels,
216 anchored-divisor report,208 arithmetic-frontier report and214 harmonic
source report. No additional current artifact was read.

Fresh primary inspections:

* [Xiao official current record](https://arxiv.org/abs/2606.28986) and
  [v1 text](https://arxiv.org/html/2606.28986v1), definitions(1.1)--(1.2),
  Theorem1.2 and Section3.8.
* [Zhai official current record](https://arxiv.org/abs/0805.1270) and
  [v1 PDF](https://arxiv.org/pdf/0805.1270v1), printed page2 definitions
  and printed page6 Theorem3; the journal reference is also on the
  official record.

The report's additional source screens were not turned into theorem
dependencies and were not independently broadened in this bounded review.

## 7. Recommended state effect

**GREEN; retain as validated strategy/source evidence, with no graph
promotion.** No repair to the frozen claimant is required for the seams
assigned here. Preserve every stated no-import and no-gain limitation.
The unproved signed integral, all full-frontier parents and the full
quarter objective retain their existing status.

Final claimant hash reviewed:
`45ec295cc04a23d061f7278015327af9ff7e4884c902c05319fb3629ed64bc59`.
This review stops here; the conductor owns closure and any State Patch.
