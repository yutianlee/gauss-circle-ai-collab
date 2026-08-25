## 1. Result

**Verdict: GREEN.**  The requested exactness repairs are present and mathematically correct.  Discovery (3.4) now defines cross-channel relations with (D_1\ne D_2), (D_3\ne D_4), and (k,\ell\ne0); candidate (161.J9) explicitly states (D_1\ne D_2) and (k\ne0).  Both passages separate trivial same-atom loops from nontrivial within-channel repetitions, and discovery (3.4a)/candidate (161.J9a) correctly close the rational-channel shared-endpoint case.

## 2. Exact statement and hypotheses

Let (J>0), let every (D) be positive and squarefree, and let all atom indices be positive integers.  The repaired classification is:

1. A cross-channel atom relation is
   \[
   J(t_1\sqrt{D_1}-t_2\sqrt{D_2})=k,\qquad D_1\ne D_2,\quad k\ne0.
   \]
2. If (D_1=D_2=D), then
   \[
   (t_1-t_2)J\sqrt D=k.
   \]
   The case (t_1=t_2) is the trivial loop and forces (k=0); if (t_1\ne t_2), the relation forces (J\sqrt D\in\mathbb Q).
3. A rational channel (J\sqrt{D_0}=r\in\mathbb Q) cannot coexist with a cross-channel relation sharing either endpoint or disjoint from it.

## 3. Proof and derivation

For a cross-channel relation, (k=0) would give

\[
 \sqrt{D_1/D_2}=t_2/t_1\in\mathbb Q,
\]

which is impossible for distinct squarefree (D_1,D_2).  Thus the nonzero condition added after discovery (3.4) and in candidate (161.J9) is forced, not merely conventional.

For (D_1=D_2=D), direct subtraction gives the repaired same-channel equation.  If (t_1=t_2), its left side is zero and hence (k=0).  If (t_1\ne t_2), then

\[
 J\sqrt D=\frac{k}{t_1-t_2}\in\mathbb Q,
\]

so a nontrivial repetition occurs only on the unique possible rational channel.  This verifies the loop/repetition split in the text following discovery (3.4) and in candidate (161.J9).

Finally, combine (J\sqrt{D_0}=r\in\mathbb Q\setminus\{0\}) with the cross-channel equation.  Eliminating (J) gives exactly discovery (3.4a) and candidate (161.J9a):

\[
 rt_1\sqrt{D_1}-rt_2\sqrt{D_2}-k\sqrt{D_0}=0.
\]

If (D_0) is distinct from both endpoints, this contradicts independence of three squarefree radicals.  If (D_0=D_1), the coefficient of (\sqrt{D_2}) is (-rt_2\ne0); if (D_0=D_2), the coefficient of (\sqrt{D_1}) is (rt_1\ne0).  Independence of the remaining two radicals gives a contradiction in both shared-index cases.  Thus the displayed elimination covers every endpoint configuration.

## 4. First doubtful or unproved step

There is no remaining doubtful step in the repaired collision classification.  The repair does not address, and does not claim to address, near-collision collars or the physical signed (t=1) estimate.  Those remain the first analytic open seams exactly as stated after candidate (161.J9a).

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| Cross-channel definition (D_1\ne D_2) | **Pass:** discovery text after (3.4); candidate (161.J9). |
| Nonzero collision integer (k\ne0) | **Pass:** explicitly stated and forced by distinct squarefree kernels. |
| Trivial loop (D_1=D_2, t_1=t_2) | **Pass:** isolated and correctly gives (k=0). |
| Nontrivial same-channel repetition | **Pass:** (t_1\ne t_2) forces the unique possible rational channel. |
| Rational/cross shared endpoint | **Pass:** discovery (3.4a) and candidate (161.J9a) retain a nonzero coefficient of the other radical. |
| Disjoint rational/cross case | **Pass:** the same equations give a forbidden three-radical relation. |
| Exact versus near scope | **Pass:** neither repaired passage infers a gap or collar estimate. |

## 6. Dependencies and exact artifacts used

Only the repaired local passages in these two artifacts were re-read:

1. `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reports/literal_radical_frequency_attack.md`, discovery (3.4)--(3.4a) and the immediately surrounding text.
2. `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/candidates/conductor_round161_radical_control_and_obstruction.md`, candidate (161.J9)--(161.J9a) and the immediately surrounding text.

No source-auditor report or other new artifact was read.  No computation or external result was used.

## 7. Recommended state effect

Supersede the prior local **REPAIR** verdict for this seam with **GREEN**.  The repaired exact atom-collision classification may be retained together with the already reviewed base-collision theorem.  This green verdict is limited to the loop/cross-channel split, the nonzero-integer conditions, and rational-channel shared-endpoint elimination; it does not promote a near-collision theorem, the physical hard-TOP target, or any downstream claim.
