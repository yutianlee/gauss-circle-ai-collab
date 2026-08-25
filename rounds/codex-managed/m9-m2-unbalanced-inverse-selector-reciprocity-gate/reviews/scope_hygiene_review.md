# Round 160 adversarial scope and artifact-hygiene review

Campaign: `m9-m2-unbalanced-inverse-selector-reciprocity-gate`

Task: `round160_scope_hygiene_review`

Role: independent post-unmask scope and artifact-hygiene reviewer

Starting graph SHA-256:
`4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d`

Generated at: `2026-08-25T18:55:53.6324476+08:00`

This is review evidence only and changes no proof status.

## 1. Result: revise before promotion; the narrow unweighted no-go is sound

The exact reciprocity, representative and parity conventions, literal
post-reciprocity scalar, complete-\(h\) reconstruction, and exactly-once
zero-row deletion are sound.  The finite unweighted kernel theorem is also
sound: for

\[
 F_j(a,h)=e(h\overline a_j/j),
 \qquad a\in U_j,\quad 1\le h\le j-1,
\]

one has

\[
 F_jF_j^*=jI_{\varphi(j)}-\mathbf 1\mathbf 1^*,
\]

with the singular spectrum and Schatten norms stated in
(160.CP3)--(160.CP4).  Restoring the positive column \(h=j\) gives the
blind report's normalized orthonormal-row matrix.  The long-\(h\) block
map has the exact norm (160.R11), and the fixed-strict-point power
comparisons are correct.

These facts support only the following route-scoped conclusion:

> Exact Hilbert rank-one scalarization of the unweighted inverse-residue
> kernel, followed termwise by a positive triangle inequality, is neither
> rank-free nor low-projective-cost.

The source report additionally claims that the named scalar realizations
do not offset this cost.  That part requires its distinct
source-hypothesis seam before it enters durable graph text.

They do not give a lower bound for the literal weighted coefficient
matrix or signed owner, and they do not exclude a coefficient-sensitive
vector theorem that keeps the Kloosterman array and both characters
inside the operator.  The candidate's buffered weighted-profile claim is
conditional on a lower-buffer hypothesis absent from the frozen packet.
It must be moved out of the unconditional result and controls before
promotion.

The campaign may close under its prescribed label
`inverse_selector_projective_capacity_no_go` only if the synthesis defines
that label by the boxed canonical-scalarization scope above.  The bare
label is too broad to stand alone: it must not be read as a no-go for every
projective realization, the fully weighted matrix, or a bespoke vector
method.

The current byte-level hygiene scan is green: the reviewed files contain
no invalid UTF-8, embedded carriage return, form feed, NUL, replacement
character, zero-width character, or trailing whitespace.  In particular,
the earlier damaged `\rm`, `\sqrt`, and `\frac` commands in the discovery
report are repaired.  Equation tags are unique within every artifact and
the display delimiters are balanced.  There is no equation-tag collision
in the conductor candidate.  The source report and post-blind review do,
however, use pervasive literal parenthetical notation such as `(j)` and
`(g=1)` instead of rendered inline math.  That is a presentation defect,
not a mathematical corruption; it should not be copied into the final
kernel or synthesis.

## 2. Exact statement and hypotheses

The promotable obstruction should be stated as follows.

Let \(j>1\), \(U_j=(\mathbb Z/j\mathbb Z)^\times\), and

\[
 F_j(a,h)=e(h\overline a_j/j),
 \qquad a\in U_j,\quad 1\le h\le j-1.
\tag{160.SH1}
\]

Then

\[
 F_jF_j^*=jI-\mathbf 1\mathbf 1^*,
\tag{160.SH2}
\]

so

\[
\begin{aligned}
 \|F_j\|_{S_1}
   &=(\varphi(j)-1)\sqrt j+\sqrt{j-\varphi(j)},\\
 \|F_j\|_{S_2}^2&=\varphi(j)(j-1).
\end{aligned}
\tag{160.SH3}
\]

Consequently every exact decomposition

\[
 F_j=\sum_\nu u_\nu v_\nu^*
\tag{160.SH4}
\]

which is estimated termwise by a scalar theorem and a triangle inequality
satisfies

\[
 \sum_\nu\|u_\nu\|_2\|v_\nu\|_2
 \ge \|F_j\|_{S_1},
 \qquad
 \frac{\|F_j\|_{S_1}}{\|F_j\|_{S_2}}
 \gg_\varepsilon j^{1/2-\varepsilon}.
\tag{160.SH5}
\]

The last bound follows self-containedly from the accepted
`Divisor-bound-elementary`, since
\(j/\varphi(j)\le 2^{\omega(j)}\le d(j)\ll_\varepsilon j^\varepsilon\).

For the primitive \(g=1\) stratum, \(j\asymp K\), where

\[
 K=X^{1-\delta-a},\qquad a=\delta-\ell.
\]

At each fixed strict admissible pair \((\delta,\ell)\),
\(K^{1/2-o(1)}\) exceeds the missing power:

\[
 \frac{1-\delta-a}{2}-\left(a-\frac14\right)>0
 \quad(1/4<a\le1/3),
\]

\[
 \frac{1-\delta-a}{2}-\frac{1-2a}{4}
 =\frac{1-2\delta}{4}>0
 \quad(1/3\le a<1/2).
\tag{160.SH6}
\]

No uniform margin up to the open face \(\delta=1/2\) is part of the
statement.

Independently, for the block-sum map \(P_{n,j}\) of (160.R10),

\[
 \|P_{n,j}\|_{2\to2}
 =\sqrt{\left\lceil\frac{n-1}{j}\right\rceil}
 \asymp\sqrt\Delta.
\tag{160.SH7}
\]

The positive frequencies \(h=mj<n\) remain after centering and satisfy

\[
 e(h\overline n_j/j)=1,\qquad
 e(-h/(jn))=e(-m/n)=1+O(1/j).
\tag{160.SH8}
\]

Equations (160.SH7)--(160.SH8) are universal operator-capacity controls,
not signed lower bounds for the actual Kloosterman-weighted vector.

Any weighted robustness statement must add the explicit hypothesis that
some fixed \(j\asymp K\) has a literal odd-\(n\) interval containing a
representative of every required unit class and, after extracting unit
phases, a pre-Kloosterman amplitude \(A(n)=A_0(1+O(\eta))\) with
\(A_0\ne0\) and \(\eta=o(1)\).  The frozen graph does not prove the
existence of this interval, this \(j\), or this nonzero \(A_0\).

## 3. Proof, scope derivation, and artifact audit

For \(a,b\in U_j\), additive orthogonality gives

\[
 (F_jF_j^*)_{a,b}
 =\sum_{h=1}^{j-1}
 e(h(\overline a_j-\overline b_j)/j)
 =\begin{cases}j-1,&a=b,\\-1,&a\ne b.\end{cases}
\]

This proves (160.SH2).  Its eigenvalues are \(j\) on the orthogonal
complement of the all-ones vector and \(j-\varphi(j)\) on that vector,
which proves (160.SH3)--(160.SH5).  Adding the column \(h=j\) changes the
Gram matrix to \(jI\), agreeing exactly with the blind rederivation.

The rows of \(P_{n,j}\) have disjoint supports of sizes
\(\#\{1\le h<n:h\equiv s\pmod j\}\).  Hence
\(P_{n,j}P_{n,j}^*\) is diagonal with those sizes, proving
(160.SH7), including sharpness.  Substitution \(h=mj\) proves
(160.SH8).  The primitive power comparison is the algebra in
(160.D8)--(160.D9), equivalently (160.PR17).

None of these norm identities survives arbitrary entrywise weighting in
the form needed for the signed owner.  A zero or highly concentrated
literal profile may delete rows, while entrywise multiplication by
\(S(N_0,h;n)\) is not a unitary row or column scaling and can change rank
and nuclear norm.  Thus the conductor candidate's Section 3.3
perturbation is valid only after an explicit nonvanishing and relative
smoothness premise.  The asymptotic fact \(\Delta\to\infty\) proves that a
complete residue block fits inside a *given* buffer of width comparable
to \(R\); it does not prove that the literal moving joint support supplies
such a nonzero buffer.

The exact scalar and reconstruction are independently green in
(160.R1), (160.R7), and (160.R12), and in
(160.PR6), (160.PR12), and (160.PR13).  They should be copied into the
final kernel.  The current conductor candidate only alludes to
full-\(h\) self-return in its controls; that is an evidence seam because
the reconstruction is one of the frozen completion criteria.

The source-specific conclusions in the source audit are not reviewed by
the post-blind algebraic seam: that reviewer explicitly used no external
source.  Therefore the finite algebraic no-go can be promoted
independently, but any durable statement naming Bettin--Chandee, Wright,
Blomer--Milićević, Deshouillers--Iwaniec, or Assing--Blomer--Li must also
cite an independent source-hypothesis seam.  The phase-only Fourier
energy identities may be promoted as finite algebra; an automorphic
Sobolev or Bessel consequence remains diagnostic/source-dependent.

The artifact scan covered raw bytes, UTF-8 decoding, C0 and zero-width
characters, trailing whitespace, display delimiters, and all
`\tag{...}` values.  It found no current byte or tag defect.  The reports
do not all satisfy the protocol metadata contract, however:

- the blind and source reports omit campaign, task, role, starting graph
  hash, and generated time from their headers;
- the conductor candidate omits task/role and generated time;
- the post-blind review omits task, starting graph hash, and generated
  time; and
- the candidate's dependency section does not list the three Round-160
  reports or the post-blind seam even though the final promoted kernel
  relies on results independently established there.

These are provenance defects.  At minimum, the final kernel, synthesis,
controls, and State Patch must carry the complete metadata and cite all
evidence actually used.  If the reports themselves are retained as
protocol-conforming current artifacts, their missing header fields should
also be supplied.

## 4. First doubtful or unproved step

The first unsupported transfer is the unconditional reading of
(160.CP14): no accepted hypothesis proves a fixed \(j\), a complete
unit-class block inside the moving joint support, and a joint
\(Wq_L\)-amplitude bounded away from zero with relative smoothness.  Upper
support and derivative bounds do not imply this lower control.

Even after adding that hypothesis, the perturbation controls only a
smoothly row-weighted inverse-phase matrix before the Kloosterman
coefficient is inserted.  It does not lower-bound the literal
\(S(N_0,h;n)\)-weighted matrix or the final signed scalar.  The first open
positive step remains a coefficient-sensitive vector theorem for the
whole \(g,n,j,h\) array, with both characters, the full long-\(h\) range,
moving endpoints, and its literal spectral levels.

The first source-evidence gap is independent verification of the
Round-160 source audit's exact theorem hypotheses and growing-level
ledger.  Until that seam is green, those source-specific statements
should remain evidence rather than accepted graph text.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| reciprocity, representatives, even/odd \(j\) | **PASS.** The exact sign is independently reproduced. |
| literal scalar and both character directions | **PASS in the reports/review; MISSING from the conductor candidate's proof kernel.** Insert (160.PR6) or its equivalent. |
| full-\(h\) reconstruction and single zero deletion | **PASS in the reports/review; MISSING as a derivation in the candidate.** Insert (160.PR12)--(160.PR13). |
| unweighted spectrum and projective price | **PASS.** The two block conventions are compatible and equation tags do not collide. |
| long-\(h\) complement | **PASS with scope.** (160.SH7)--(160.SH8) are operator controls, not signed lower bounds. |
| primitive power comparison | **PASS pointwise only.** Replace any potentially uniform “throughout the polytope” wording by “at each fixed strict exponent pair.” |
| transfer to weighted matrix | **FAIL unconditionally / PASS conditionally.** State the lower-buffer hypothesis explicitly or delete the paragraph. |
| bespoke vector impossibility | **REJECT.** No such no-go is proved. |
| target or strict range | **NO CHANGE.** Neither is proved. |
| downstream/global exponent | **PASS scope.** No report licenses M2, M9, bridge, quarter-target, or exponent promotion. |
| source theorem promotion | **PENDING an independent source seam.** The post-blind review is algebraic only. |
| control characters and UTF-8 | **PASS on the current files.** No C0, zero-width, replacement, or invalid UTF-8 character remains. |
| equation tags and delimiters | **PASS.** Tags are unique per artifact; display delimiters are balanced. |
| rendered inline notation | **REVISE for publication quality.** Do not copy the source/review's bare `(j)`-style mathematical notation into final artifacts. |
| artifact provenance metadata | **REVISE.** Supply the omitted campaign/task/role/hash/time and exact evidence list described above. |

No numerical experiment was used.  This review is entirely algebraic,
logical, and artifact-level.

## 6. Dependencies and exact artifacts used

This review read and used:

- `AGENTS.md`;
- `protocol.md`;
- `state/proof_obligations.yml`, especially the five frozen Round-160
  targets and their accepted dependencies;
- `state/active_campaign.yml`;
- `strategy/round160_m2_unbalanced_inverse_selector_reciprocity_strategy.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/blind_statement.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/candidates/conductor_round160_reciprocity_seed.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reports/inverse_selector_reciprocity_attack.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reports/blind_reciprocity_matrix_rederivation.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reports/reciprocity_projective_source_audit.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/candidates/conductor_round160_reciprocity_projective_obstruction.md`; and
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/reviews/post_blind_reciprocity_projective_seam.md`.

No sibling review, synthesis, State Patch, proof draft, validation matrix,
or external webpage was read or edited.  The source-theorem assertions
were checked here only for their logical scope and evidence routing, not
re-audited against the primary papers.

## 7. Recommended state effect and exact repairs

**Revise, then promote only the narrow obstruction.**  Apply all of the
following before a graph patch:

1. In the candidate result, replace the unconditional-looking sentence
   after (160.CP4a) about the “same lower bound after the literal smooth
   row weights” by an explicitly conditional pre-Kloosterman statement
   with the lower-buffer hypothesis in Section 2 above, or delete it.
2. Retitle candidate Section 3.3 as conditional, insert the exact
   lower-buffer/complete-class hypothesis before choosing representatives,
   and change control 5 from “pass” to “conditional; not promoted.”
3. Replace “throughout the strict frozen polytope” by “at every fixed
   strict admissible exponent pair; no open-face-uniform margin.”
4. Add the exact quadruple scalar, both character directions, complete
   reconstruction, and the exactly-once zero-row formula to the final
   kernel.
5. Add the independently proved long-block norm and \(h=mj\) control, with
   an explicit sentence that neither lower-bounds the signed coefficient
   vector.
6. Derive \(\varphi(j)\gg_\varepsilon j^{1-\varepsilon}\) from
   `Divisor-bound-elementary` in one line, so the power comparison has no
   hidden dependency.
7. Keep Fourier high-frequency identities as finite algebra.  Do not
   promote a source-independent automorphic Sobolev/Bessel obstruction.
8. Add the discovery, blind, source, and post-blind artifacts to the
   candidate/final-kernel evidence list, and complete the missing metadata
   headers or at least make the final evidence chain protocol-complete.
9. If source-specific no-go language enters the durable graph statement,
   require and cite a distinct source-hypothesis seam.  Otherwise keep the
   graph node purely finite-algebraic and route-scoped.
10. Define the terminal label exactly as:
    `inverse_selector_projective_capacity_no_go` =
    “no low-cost exact Hilbert scalar common-test factorization plus
    termwise triangle for the unweighted inverse-residue kernel, together
    with failure of the explicitly audited scalar source realizations.”
    State in the same sentence that the fully weighted matrix and bespoke
    vector route remain open.

After these repairs, one new scoped obstruction node is supportable.
Retain `M9-M2-smooth-unbalanced-three-quarter-estimate`, every owner-
complete strict range, M9-M2, M9, endpoint uniformity, the conditional
bridge, `GC-target`, and the global exponent unchanged.
