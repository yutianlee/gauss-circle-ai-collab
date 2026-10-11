# Round 205 independent arithmetic-source application review

Campaign: `gc-full-frontier-moment-strategy-review`.
Reviewer: `internal_arithmetic_routes`, bounded post-report source seam.
Date: 2026-09-26. Analytical/source work only; no numerical experiments.

## 1. Result

**Scoped GREEN** for the application/no-import conclusions in
`controls/conductor_arithmetic_source_gate.md`, final SHA-256
`b642700d0f1f9348c31534a8c8c2681c416a6207f5dc303c5d280085b464e17f`.
This hash was independently checked after rereading the added origin
convention paragraph. The initially supplied hash
`96e3e0d8d8ec6fb923c134d15860863e8461b032ff1b438b45d14b4557194ac5`
is superseded for this review.

The two printed theorem interfaces match the candidate's uses. The
thin-box error has no supplied power rate; the random-model theorem's
exceptional set has no supplied target-sized twelfth moment. Neither
statement certifies the complete arithmetic middle-band objective.
No required mathematical correction remains. The clarifications below
fix the precise interpretation of repeated shifts, normalization and
exceptional-set compatibility.

This is an independent application review of the cited statements,
not a new proof of either external theorem, a full audit of their
proofs, or a source-card promotion. It also does not recertify the
separate radial-Poisson derivation underlying the middle-band strategy.

## 2. Exact hypotheses and primary statement checks

In Matthiesen's current sole v1, Theorem 1.1 on pages 1--2 assumes
primitive irreducible binary quadratic forms, positive when definite,
a pairwise affinely independent affine system in d variables, and
a convex body in an ambient box of scale N with positive arguments
where required. The error is `o(N^d)`, and constants may depend on
the discriminants and affine-system coefficients. For discriminant
-4 the automorph factor printed in the theorem is 4. These are
representation counts, not representability indicators.
[Primary statement](https://arxiv.org/pdf/1205.4145),
[version record](https://arxiv.org/abs/1205.4145).

Lamzouri's sole arXiv v1, Theorem 6.2 on page 18, supplies one set
`A subset [Y,2Y]` with complement `O(Y(log Y)^(-10))`, simultaneously
for `|lambda|<=c_19(log_2 Y)^(3/4)(log_3 Y)^(-5/4)`. Its normalized
Laplace-transform error is `O(exp(-log_2 Y/log_3 Y))`. Theorem 1.6
on page 5 treats both signed tails only through
`V<=b_6(log_2 Y)^(1/4)(log_3 Y)^(2^(4/3)-17/12)` as printed.
Lemma 2.1(2) supplies finite random exponential moments.
[Theorems 1.6 and 6.2, primary text](https://arxiv.org/html/2410.03652v1),
[version record](https://arxiv.org/abs/2410.03652).

Here `log_j` denotes an iterated logarithm. The candidate only needs
the weaker, unambiguous fact that the tail range is an iterated-log
scale. No enlargement of that range is used. Both current arXiv
records were checked on 2026-09-26 and showed the versions just
specified, without withdrawal notices. The journal DOI was attempted
but its page did not load; no mathematical conclusion here depends on
fresh verification of journal metadata.

## 3. Independent derivation of the application costs

### Representation normalization and the anchored thin box

For positive n the proper automorphs of `x^2+y^2` are its four
rotations. Each orbit of a nonzero integer vector has size four.
Thus the primary count is exactly `r_2(n)/4`. A product of twelve
such counts differs from the desired representation product by the
fixed multiplier `4^12`; this changes no power or uniformity issue.

In one shell moment there are twelve integer arguments. The bijection

\[
(m_1,\ldots,m_{12})\longleftrightarrow
(x,h_2,\ldots,h_{12}),\quad x=m_1,\quad h_i=m_i-m_1
\]

has twelve variables, not thirteen. The continuous radius is integrated
into the weight; it is not another integer variable of the affine
system. The forms are `x` and `x+h_i`. Their linear coefficient
vectors are pairwise nonproportional when the shifts are independent
variables, so the ambient system passes the affine-independence test.

With `X=T^2`, `x asymp X`, and `|h_i|=O(h)`, an interior box has
volume comparable to `X h^11`. The middle-band range gives

\[
X^{151/500}<h<X^{99/250}.
\]

Applying the printed error at ambient scale X gives
`e(X)X^12`, with only `e(X)->0` known. Its ratio to the thin volume is

\[
e(X)(X/h)^{11}.
\]

The additional power of X lies between `1661/250` and `3839/500`.
No `o(1)` assertion without a rate absorbs that growing power.
In particular it does not establish even an error smaller than the
positive thin-box main term, much less the required signed moment
saving. Translating many short boxes to ambient scale h puts growing
translations into the affine constants; the theorem as stated gives
no uniform quantitative error for that procedure.

There is a useful distinction about repeated shifts. The ambient
12-variable theorem does include points where two values `h_i,h_j`
coincide; such points do not make the two ambient affine functions
identical. If those diagonal configurations are extracted into a
lower-dimensional subsystem, however, repeated functions may appear,
and the theorem cannot simply be reapplied to them. If instead all
shifts are fixed and only x varies, all linear parts are proportional,
outside its hypothesis. The candidate's instruction to retain those
configurations is therefore correct. No diagonal is declared negligible.

The odd shell kernel, the exact curvature `R-sqrt(m)`, the weights
`m^(-1/4)`, and every mixed term still need to be inserted and summed.
A positive unweighted asymptotic does not estimate their cancellation.

### Good-set exponential moments and the radius conversion

Let `F(x)=x^(-1/4)P(x)` in the source convention. Its allowed parameter
radius tends to infinity, so both fixed choices `lambda=1,-1` are
eventually permitted for the same A. Finiteness at these two values
also follows from the printed random exponential bounds at `+3,-3`,
using `e^(+/-u)<=1+e^(+/-3u)`. The comparison therefore gives

\[
\int_A(e^{F(x)}+e^{-F(x)})\,dx\ll Y.
\]

Since `|u|^12<=12!(e^u+e^(-u))`,

\[
\int_A|F(x)|^{12}\,dx\ll Y.
\tag{R1}
\]

This uses a positive pointwise inequality, not differentiation of the
comparison error. If the source omits the origin, project P equals
source P plus 1. The corresponding perturbation in F is
`O(Y^(-1/4))`; the fixed exponential bounds and (R1) persist. This
checks the final candidate's added paragraph.

Use the accepted kernel (L12) with the same fixed smoothing scale T:

\[
P(R^2)=\frac{\sqrt R}{\pi}H_T(R)+O_\eta(T^{1/2+\eta}),
\qquad R\asymp T.
\]

Hence `H_T(R)=pi F(R^2)+O_eta(T^eta)`. The origin adjustment in H
is `O(T^(-1/2))`, inside that error. For `A_R={R:R^2 in A}`,
the exact Jacobian `dx=2R dR` gives

\[
\int_{A_R}|F(R^2)|^{12}\,dR
\ll T^{-1}\int_A|F(x)|^{12}\,dx\ll T.
\]

The normalized reconstruction error contributes `O(T^(1+12eta))`;
choosing eta sufficiently small proves the stated
`O_epsilon(T^(1+epsilon))` good-set actual-series moment. The bad
radius set has measure

\[
|E_R|\ll T^{-1}Y(\log Y)^{-10}
\ll T(\log T)^{-10}.
\tag{R2}
\]

Any fixed enlarged radius window is covered by finitely many
comparable squared-radius intervals. Taking their good sets on
disjoint pieces retains (R1)--(R2). A fixed bounded window only
multiplies these upper bounds by its supremum. Thus no hidden factor
of T is lost in the conversion.

### Full exceptional-set price and the remaining range

The accepted supremum is `|H_T|<<T^(beta+eta)`. Its use on (R2)
gives exactly

\[
\int_{E_R}|H_T|^{12}\,dR
\ll_\epsilon T^{1+12\beta+\epsilon}(\log T)^{-10}.
\tag{R3}
\]

The exponent exceeds `29/25`; a logarithm does not repair this.
One may combine the measure cap with the accepted distribution:

\[
\int_{E_R}|H_T|^{12}
\le\int_0^{W}12V^{11}
\min\{|E_R|,D(V)\}\,dV,\qquad W\ll T^{\beta+\eta}.
\]

This retains the old high-level `T^(10beta+epsilon)` contribution.
To check the precise logical claim, an abstract peak of height
`W=T^beta` on measure `W^(-2)` satisfies the diagonal distribution
term at every lower level, has twelfth mass `W^10`, and fits entirely
inside the permitted exceptional-set measure. This is a compatibility
test for the supplied upper data, not an arithmetic lower bound or
a claim that the actual exceptional set contains such a peak. It
shows why its measure alone cannot remove the old power.

Finally, the printed Theorem 1.6 upper level is smaller than every
fixed positive power of Y, hence also smaller than `T^(13/125)`
when `Y=T^2`. The source treats actual circle signs, but not the
power-size levels responsible for the remaining moment deficit.
The candidate correctly preserves the entire exceptional contribution.

## 4. First unproved step and review boundary

For the correlation method the missing input is a quantitative,
coefficient-compatible signed thin-range estimate, uniform under the
required shifts and weights and with all repeated-index pieces
retained. For the random-model method it is a target-sized twelfth
moment on the entire bad set, or an equivalent complete estimate
that absorbs it.

No correction to the final candidate's application logic is required.
GREEN does not certify the external papers' complete proofs. It only
checks what their printed theorem statements would supply, and why
those statements cannot be credited as a proof of the present target.
The candidate explicitly proposes no external theorem promotion.

## 5. Controls and outcome

| Seam | Outcome |
|---|---|
| Final candidate identity | Hash checked; origin addition reread. |
| Primary theorem hypotheses | Exact count, dimension, affine independence, ambient error, common good set and parameter range checked. |
| `r_2/4` normalization | Four free rotations for positive representations; product constant `4^12`. |
| Repeated/fixed shifts | Ambient collisions retained; extracted diagonals and fixed-shift systems not silently imported. |
| Exponential-to-moment inference | Fixed parameters and positive inequality suffice; no error differentiation. |
| Origin convention | Constant-one difference is harmless at both normalizations. |
| Radius Jacobian and reconstruction | Factor `T^-1` and full `T^eta` error restored. |
| Exceptional-set price | Both direct supremum price and old distribution contribution retained. |
| Tail range | Printed iterated-log range gives no positive-power high-value control. |
| Full-proof scope | No middle-band estimate, new pointwise exponent, M1/M2 closure, or quarter theorem claimed. |

All controls are analytical/source checks. No numerical experiment or
unread theorem is used as evidence.

## 6. Exact dependencies and artifacts used

Only the permitted local files were read during this review:

1. `protocol.md`.
2. `rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_arithmetic_source_gate.md`, final reviewed hash above.
3. `rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_middle_band_strategy.md`, for scale and target context only.
4. `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`, especially (L1), (L2), and (L11)--(L14).

Primary sources independently inspected: Matthiesen arXiv1205.4145v1,
Theorem 1.1 pages 1--2 and its current record; Lamzouri
arXiv2410.03652v1, Theorems 1.6/6.2, Lemma 2.1(2), the circle
normalization and current record, via PDF text and HTML. URLs are in
Section 2. PDF screenshot requests returned no model-visible images;
the formula checks used the actual primary text, with HTML resolving
the Lamzouri exponents. The journal DOI attempt failed and secondary
search results were not mathematical evidence.

The conductor's follow-up pointed out only the origin convention and
reported its added paragraph/hash. No sibling review was read. The
completed discovery report and all shared state were left unchanged.

## 7. Recommended state effect

**GREEN, scoped to the final hash and this application/no-import seam.**
Archive the candidate as strategy evidence. Make no proof-graph,
source-card, proof-draft, exponent or parent-status change on this
review's authority. Retain the complete arithmetic objective and its
full exceptional/error obligations. This review stops here.
