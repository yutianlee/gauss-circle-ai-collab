# Round 155 hostile terminal review: exact inversion, norm, endpoint, and promotion scope

- Campaign: `m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate`
- Role: independent hostile terminal reviewer
- Starting graph SHA-256: `84bbcb3413936c9b672c829cdba97b8d0bde69f7a6df677b61f24e9ec27e243a`
- Allocation: 100% analytic and algebraic review; 0% numerical experimentation

## 1. Result

The conductor candidate is mathematically valid as a narrowly scoped
`outer_defect_theta_dispersion_no_go`.  I found no factor, sign, gcd,
Parseval, zero-mode, endpoint, source-scope, or implication defect.

The promotable content is only the exact complete-half-period inverse-Gauss
identity (155.CA6)--(155.CA7), together with the exact sampled-Parseval
identity and route-scoped upper ledgers.  Complete dual resummation returns
the original quotient-selector stratum and therefore supplies no new square
root.  This is genuinely new relative to the starting graph: Round 154
froze the normalized theta completion and warned that complete resummation
could self-return, but did not prove the complete half-period inverse with
its sign, multiplier, and imprimitive partition.

The candidate does not prove the signed outer-defect target, a strict
positive-power defect range, a new \(M\)-range, an endpoint assembly, a
downstream owner, or either global exponent.  Its source conclusion is a
current direct-interface no-match, not an impossibility theorem.

## 2. Exact statement and hypotheses audited

I audited the candidate for arbitrary \(N=\lfloor X\rfloor\), including
even and nonsquarefree \(N\), every odd \(d\mid N\),

\[
 q=4N,\qquad c=q/d,\qquad H=c/2,
\]

and every dyadic outer block
\(M^{3/4}(\log(2X))^A<V\le \sqrt{NM}\).  Since \(d\) is odd,
\(c\equiv0\pmod4\), so the half-period and even-modulus Gauss formula are
legal in every stratum.

The coefficient in the inversion is the exact ambient, pre-linearization
\(B_j\), not the selected linearized coefficient.  Thus the pointwise-in-
\(j\) identity retains the zero extension, actual profile components and
transitions, strict mask, exact residual phase, asymmetric cell
\(-x\le j\le x-1\), both signs, and hard endpoints.  The accepted
linearization is used only for the selected scalar.  In particular, the
ordinary-K calculation in the blind report is correctly quarantined as a
surrogate control: lines 226--230 of the candidate expressly decline to use
it as the theta normalization.  The literal theta multiplier in
(155.CA5), not the blind ordinary kernel, is what enters (155.CA6).

The external \(B_{1,U}(1)\) factor remains an assembly seam.  Nothing in
the candidate assumes that the selected-row rank collapse holds for the
ambient rows, separates \(\widehat B_j(2dv)\), or replaces a fixed modulus
by a modulus average.

## 3. Proof and line-by-line seam audit

### Exact half-period, sign, multiplier, and gcd partition

For a unit \(a\pmod c\), set

\[
 I_c(a,x)=\sum_{v\bmod H}e_c(-\bar a v^2-2xv).
\]

Under \(v\mapsto v+H\), the change in the normalized exponent is

\[
 -\bar a v-\bar a c/4-x\in\mathbb Z,
\]

so \(H=c/2\) is the exact period and the complete sum modulo \(c\) is
twice this half sum.  Completing the square gives

\[
 -\bar a v^2-2xv\equiv-\bar a(v+ax)^2+ax^2\pmod c.
\]

With \(A\equiv-\bar a\pmod c\), the even Gauss formula, together with
\(\bar a\equiv a\pmod4\), gives

\[
 \epsilon_A^{-1}\Bigl(\frac cA\Bigr)
 =-i\epsilon_a\Bigl(\frac ca\Bigr),
\]

and hence exactly

\[
 I_c(a,x)=\frac{1-i}{2}\epsilon_a
 \Bigl(\frac ca\Bigr)\sqrt c\,e_c(ax^2).
\]

Multiplication by the theta multiplier already present in \(K\) squares
\(\epsilon_a(c/a)\) to \(\chi_4(a)\).  This proves (155.CA6) with the
displayed sign.  Restoring the ambient factor gives

\[
 -\frac{i(1+i)}{2Nq}d\sqrt c\,
 \frac{1-i}{2}\sqrt c
 =-\frac{i}{2N}\frac{dc}{q}
 =-\frac{i}{2N},
\]

so there is neither a missing two nor a residual square-root factor.

The imprimitive partition also is exact.  Every odd residue
\(h\pmod{4N}\) has the unique decomposition

\[
 d=(h,N),\qquad h=da,\qquad
 a\in(\mathbb Z/(4N/d)\mathbb Z)^*.
\]

This does not require \((d,N/d)=1\): after division by the full gcd,
\((a,N/d)=1\), and oddness gives \((a,4)=1\).  Conversely every displayed
\((d,a)\) has \((da,N)=d\).  Since
\(\chi_4(da)=\chi_4(d)\chi_4(a)\) and
\(e_{4N}(da(x^2-j))=e_c(a(x^2-j))\), the \(d\)-sum in (155.CA7) is exactly

\[
 -\frac{i}{2N}\sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}
 \chi_4(h)e_{4N}(h(x^2-j)),
\]

which is the literal odd-quotient selector.  Thus the claimed complete-
\(v\) self-return is an identity, not an estimate or a second independent
Gauss saving.

### Sampled Parseval and norm powers

Because

\[
 \widehat B_j(2dv)
 =\sum_{r\bmod H}C_{j,d}(r)e_H(-vr),
\]

ordinary finite Parseval gives (155.CA11) with the factor \(H\), not \(q\).
The collision relation is exactly
\(x-y\equiv0\pmod H\), with \(H=2N/d\).  On total physical span \(O(K)\),
each fold has multiplicity
\(O(1+K/H)=O(1+dK/N)\).  Using
\(\sum_x|B_j(x)|^2\ll K M^{-3/2}X^\varepsilon\) yields

\[
 H(1+dK/N)K M^{-3/2}
 \ll
 \left(\frac{N^{3/2}}{dM}+\frac{N}{M^{1/2}}\right)X^\varepsilon,
\]

which is (155.CA12).  Large-\(d\) folds are therefore retained; no false
physical-diagonal-only identity or defect orthogonality is asserted.

### Zero mode and partial cutoff

For \(v=0\), DFI gives

\[
 |K(0,-j;c)|\le (j,c)^{1/2}c^{1/2}\tau(c).
\]

The restored prefactor satisfies
\(d\sqrt c\,c^{1/2}/(Nq)=1/N\), while
\(|\widehat B_j(0)|\ll KM^{-3/4}X^\varepsilon\).  The standard dyadic gcd
sum

\[
 \sum_{V<|j|\le2V}(j,c)^{1/2}
 \ll_\varepsilon(V+c^{1/2})c^\varepsilon
\]

and the divisor sum over \(d\) give exactly

\[
 |\mathcal T_{0,U}(V)|\ll_\varepsilon
 \left(N^{-1/2}M^{-1/4}V+M^{-1/4}\right)X^\varepsilon.
\]

At \(V=K\) its first term is \(M^{1/4}\).  The candidate repeatedly and
correctly labels this as an upper majorant, never as a signed lower bound
or evidence that the zero row is actually large.

For an arbitrary proper weight \(\eta\), the change \(u=v+ax\) gives
exactly (155.CA15), with the translated coefficient \(\eta(u-ax)\).
Thus a nonconstant cutoff is not translation-invariant and retains joint
\((a,x)\)-dependence.  The candidate promotes only this algebraic
nonseparability obstruction; it does not claim that no structured
incomplete transform can ever be estimated.

### Restored square-root capacity and hard endpoint

The all-parity root count supplies at most \(O(VX^\varepsilon)\) restored
defect incidences.  Granting, but not proving, their square-root
cancellation gives

\[
 M^{-3/4}V^{1/2}X^\varepsilon,
\]

which is target-sized only for \(V\le M^{3/2}\).  At the hard scale
\(V=K=\sqrt{NM}\), it equals \(N^{1/4}M^{-1/2}\), so the top is covered by
this hypothetical mechanism alone only at \(M\asymp N^{1/2}\), the upper
boundary of the frozen range.  Intersecting the top dyadic block with the
literal cell can only reduce its incidence count; it cannot invalidate this
upper-capacity ledger.  No positive-power range is inferred.

### Flat-\(j\) arc and wrapped branch

The selected phase varies by only \(O(V/K)\le O(1)\).  In the exact ambient
phase the \(j\)-derivative is

\[
 -\frac1{2\sqrt{x^2-j}}-\frac ac,
\]

so first-derivative or Poisson localization gives precisely the circular
condition (155.CA18), containing \(O(1+c/V)\) residue representatives.
For any nonempty fixed-\(x\) block, \(V<|j|\le x\), hence \(V<x\); the arc
radius \(c/V\) exceeds the centre distance \(c/(2x)\) from zero.  The arc
therefore wraps.  In positive representatives it has both the near-zero
piece and the negative-frequency piece near \(c-c/(2x)\).  The candidate
prints both and discards neither.  This is only localization capacity, not
square-root cancellation.

## 4. First doubtful or unproved step

The first source-unproved seam for a spectral route that separates
nonzero frequencies is the fixed-modulus zero row (155.CA20), uniformly in
all odd \(d\mid N\), both signs, the actual profile, and every endpoint.  If
that is controlled at target scale, the next missing input is a genuinely
signed bound for the incomplete nonzero matrix
\(\widehat B_j(2dv)K(-v^2,-j;4N/d)\), or the equivalent selected
cross-fibre bound (155.CA19), with the accepted exact/linearized seam
restored.

Complete resummation cannot provide this missing bound because it is the
proved inverse identity.  Sampled Parseval preserves the folded norm, and
bare \(j\)-localization only finds the wrapped reciprocal arc.  None of
these positive right sides is a lower bound or an impossibility theorem.

First exact defect in the conductor candidate: **none**.

## 5. Hostile controls and outcomes

| Audit seam | Outcome |
|---|---|
| Blind ordinary-K surrogate | GREEN.  It is explicitly confined to the blind report and is not imported as the project theta multiplier or normalization. |
| Half-period factor and sign | GREEN.  The period is \(c/2\), the half-Gauss factor is \((1-i)\sqrt c/2\), and all constants restore to \(-i/(2N)\). |
| Gcd and two-adic strata | GREEN.  Every odd \(d=(h,N)\) occurs uniquely, including noncoprime factorizations; \(c\equiv0\pmod4\) retains all two-adic content. |
| New-route status | GREEN/scoped.  The exact complete-\(v\) inverse was not proved in the starting graph and obstructs only complete resummation, not future incomplete signed mechanisms. |
| Sampled Parseval | GREEN.  The fold period is \(2N/d\), the multiplicity and both norm powers are correct, and the result is only an upper capacity. |
| Zero mode | GREEN/scoped obstruction.  Its displayed \(N\)-\(M\)-\(V\) bound is correct and is never converted into a lower bound. |
| Partial cutoff | GREEN.  The exact translate \(\eta(u-ax)\) preserves the joint coefficient; structured incomplete estimates remain open. |
| Square-root threshold and top endpoint | GREEN.  \(V\le M^{3/2}\) and the top value \(N^{1/4}M^{-1/2}\) are exact hypothetical capacities, not a promoted range. |
| Flat-\(j\) endpoint geometry | GREEN.  The circular arc wraps through zero, and both positive-representative branches are retained. |
| Source scope | GREEN.  DFI is used termwise; all joint results are reported only as hypothesis no-matches.  The cutoff-checked search is not called exhaustive or impossible. |
| Downstream scope | GREEN.  No \(D>1\), \(L>1\), generic \(t=1\), original \(t\ge2\), Round-138 cross, other M1, M2, endpoint assembly, M9, bridge, quarter-target, or global-exponent conclusion is made. |
| Seven-section contract | GREEN.  The three assigned reports have exactly seven substantive sections, and the conductor candidate itself has seven numbered sections covering result/scope, exact derivation, first open step, controls/source scope, and recommended state effect. |

No computation, finite numerical experiment, or empirical certification was
used.

## 6. Dependencies and exact artifacts used

This review used the required packet:

1. `protocol.md`;
2. the relevant current graph nodes in `state/proof_obligations.yml` and
   the complete `state/active_campaign.yml` manifest;
3. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/plan.json`;
4. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/barrier_packet.md`;
5. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/blind_statement.md`;
6. all three assigned reports:
   `reports/outer_defect_spectral_dispersion_attack.md`,
   `reports/blind_linearized_cross_fibre_feasibility.md`, and
   `reports/theta_bilinear_spectral_source_audit.md`;
7. `candidates/conductor_round155_theta_dispersion_adjudication.md`; and
8. `reviews/independent_inverse_gauss_math_review.md`.

For the narrow newness and format comparisons, I also checked the relevant
normalized-completion lines of
`rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_root_dispersion_adjudication.md`,
the Round-155 seed
`candidates/conductor_round155_outer_defect_seed.md`, and the section
structure of
`rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/reviews/hostile_conductor_round154_final.md`.

The graph nodes used for scope were
`M9-M1-lower-cone-t1-d1-root-defect-logarithmic-collar-reduction`,
`M9-M1-d1-theta-kloosterman-source-audit`,
`M9-M1-lower-cone-t1-d1-root-dispersion-obstruction`,
`M9-M1-lower-cone-t1-squarefree-large-wrap-collar-obstruction`, and
`M9-M1-global-lower-radial-signed-estimate`.  No web search, source
extension, or computation was used.

## 7. Recommended state effect and terminal verdict

Promote, subject to the other required terminal gates, only:

- (155.CA6)--(155.CA7) as the exact mask-preserving complete-half-period
  inverse-Gauss self-return;
- (155.CA11)--(155.CA12) as sampled Parseval with all \(2N/d\) folds;
- (155.CA13)--(155.CA15) and the circular reciprocal arc as upper-ledger or
  route-scoped obstructions, never lower bounds or impossibility claims.

Retain the zero-row estimate, the incomplete coupled theta matrix, and the
selected cross-fibre theorem as open analytical seams.  Retain every
positive-power range and all downstream obligations as open.  Make no
scale-boundary, endpoint, \(M\)-range, target, bridge, M9, or exponent
change.

Required correction before promotion: **none**.

GREEN
