# Round 149 terminal repair review of the conductor candidate

- Campaign: m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate
- Reviewed artifact: candidates/conductor_round149_gcd_lift_compression_and_energy_boundary.md
- Repair under review: paragraph (149.C30)--(149.C30a)
- Role: independent hostile repair reviewer
- Verdict: **GREEN**
- Status: review evidence only; no shared-state edit

## 1. Result

**GREEN.** The repair fully cures the prior RED.

The patched paragraph now:

1. introduces the total-variation hypothesis explicitly and only
   “for scale diagnosis”;
2. states that the weighted second-derivative lemma **would** give
   (149.C30a) under that additional hypothesis;
3. calls the dual derivative range and returned square-root phase
   formal;
4. expressly says that neither the coefficient norm nor boundedness
   of the profile proves the variation hypothesis;
5. expressly says that (149.C30a) is not used as an unconditional
   estimate; and
6. retains the \(D=1\) calculation only as a diagnostic, not a signed
   lower bound or a proof of the all-scale row.

No residual unconditional \(D=1\) second-derivative claim or
dual-transform claim remains elsewhere in the candidate. The first
unproved theorem remains (149.C31), exactly as intended.

## 2. Exact statement and hypotheses

The repaired statement is:

\[
\text{if}\quad
\operatorname{Var}_{q\equiv1(4)}
 \mathscr W_{d,U}(1/q)
+
\operatorname{Var}_{q\equiv3(4)}
 \mathscr W_{d,U}(1/q)
\ll_\varepsilon X^\varepsilon,
\tag{V2.1}
\]

then a weighted second-derivative lemma gives

\[
\sum_{q_0\asymp Q}
\chi_4(q_0)\mathscr W_{d,U}(1/q_0)e(Nd/q_0)
\ll_\varepsilon
(NM)^{1/4}+N^{1/4}M^{-3/4}
\tag{V2.2}
\]

at \(D=1\). In particular, (V2.2) is
\(O_\varepsilon(RX^\varepsilon)\) at \(M\asymp1\).

The candidate does **not** assert (V2.1) for the actual profile. It
instead states that boundedness and the coefficient norm do not prove
it. Therefore (V2.2) has the correct logical status: conditional
scale calculation only.

The associated statement that the derivative range has length
\(\asymp M\) and formally returns a square-root phase is within the
same conditional diagnostic paragraph. It is not cited as a proved
estimate for \(G_U(d)\), (149.C27), or (149.C31).

## 3. Proof and derivation

For \(D=1\), one has \(E\asymp M\) and

\[
Q\asymp \sqrt{N/M}.
\]

On either odd residue class modulo \(4\), \(\chi_4\) is constant.
Writing \(q=4n+c\), the phase

\[
f_c(n)=\frac{Nd}{4n+c}
\]

satisfies, for \(q\asymp Q\),

\[
|f_c''(n)|\asymp \frac{N}{Q^3}=:\Lambda.
\]

Under (V2.1), the weighted second-derivative bound is

\[
Q\Lambda^{1/2}+\Lambda^{-1/2}.
\]

Substitution of \(Q\asymp(N/M)^{1/2}\) gives

\[
Q\Lambda^{1/2}
\asymp (NM)^{1/4},
\qquad
\Lambda^{-1/2}
\asymp N^{1/4}M^{-3/4}.
\]

This verifies (149.C30a). Moreover,

\[
\Lambda Q
\asymp \frac{N}{Q^2}
\asymp M,
\]

which verifies the stated formal dual-index length.

The repaired prose matches this derivation exactly:

- “suppose additionally” makes the hypothesis conditional;
- “would then give” makes the theorem application conditional;
- “formal dual derivative range” prevents promotion of the
  transformed expression;
- “not used as an unconditional estimate” blocks any inference to
  the \(D=1\) target; and
- “diagnostic, not a signed lower bound” blocks an adverse-capacity
  misreading.

A search of the full patched candidate finds no second invocation of
a \(D=1\) second-derivative theorem. The dependency paragraph merely
states that the transform-self-return route does not fill the open
energy estimate; that negative conclusion does not require the
missing variation hypothesis.

The earlier algebraic seams remain unchanged by the repair:
(149.C2)--(149.C15), (149.C16)--(149.C19), and
(149.C20)--(149.C26) are the same exact compression, norms,
diagonal, and exact-alignment claims that passed the first review.

## 4. First doubtful or unproved step

There is no remaining doubtful step in the repaired
(149.C30)--(149.C30a) paragraph because it no longer claims that the
variation hypothesis is known.

The first genuinely unproved theorem is still stated openly as

\[
\begin{aligned}
\sum_{\eta=1,2}
\sum_{\substack{m\asymp D/\eta\\m\ {\rm odd\ squarefree}}}
\sum_{\substack{x_1\ne x_2\\\mathrm{nonexact}}}
A_{\eta m}(x_1)\overline{A_{\eta m}(x_2)}
e\!\left(m\frac{\eta N\delta}{HAB}\right)
\ll_\varepsilon R^2D X^\varepsilon.
\end{aligned}
\tag{V2.3}
\]

The candidate labels (V2.3)/(149.C31) missing and makes no inference
from (149.C30a) to it. Thus the proof boundary is now exact.

## 5. Control tests and outcomes

| Repair control | Outcome |
|---|---|
| total-variation hypothesis stated | **GREEN.** It is explicit and residue-class specific. |
| theorem invocation made conditional | **GREEN.** The text says “would then give.” |
| second-derivative powers | **GREEN.** They rederive as \((NM)^{1/4}+N^{1/4}M^{-3/4}\). |
| bottom scale \(M\asymp1\) | **GREEN.** \(O(RX^\varepsilon)\) is asserted only under the added hypothesis. |
| all-scale \(D=1\) row | **GREEN by scope.** It remains an entry test, not a proved row estimate. |
| dual range length | **GREEN.** \(\Lambda Q\asymp M\), labeled formal. |
| dual square-root phase | **GREEN by scope.** It is a formal diagnostic, not an audited transform estimate. |
| coefficient norm versus variation | **GREEN.** The candidate explicitly says the norm/boundedness does not imply variation. |
| use in joint energy | **GREEN.** (149.C30a) is expressly not used to prove (149.C31). |
| signed-lower-bound falsifier | **GREEN.** The paragraph says the diagnostic is not a signed lower bound. |
| residual claims elsewhere | **GREEN.** No second unconditional \(D=1\) or dual-transform assertion remains. |

Terminal repair outcome: **GREEN**.

## 6. Dependencies and exact artifacts used

This terminal review used:

1. protocol.md, already read under the campaign protocol;
2. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/blind_statement.md;
3. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/briefs/blind_compressed_energy_feasibility.md;
4. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/candidates/conductor_round149_gcd_lift_compression_and_energy_boundary.md, in its patched form; and
5. the precise defect recorded in the prior review
   reviews/blind_conductor_round149_math_review.md.

No graph, proof draft, sibling report, computation, or web source was
used.

## 7. Recommended state effect

**Accept the repair and supersede the prior RED with GREEN for this
seam.** The conditional \(D=1\) scale diagnostic may remain exactly
as patched. It should not be entered as an unconditional theorem
about the actual profile.

The separable exact compression, prefix-uniform norm, \(DQ\)
diagonal, and exact-alignment lemmas remain eligible for the
conductor’s normal promotion process. Keep the variable-row
near/generic energy (149.C31), the signed scalar target, and all
downstream obligations open. No shared-state edit is made by this
review.
