# Blind post-unmask verification of the Round 192 Farey-covector candidate

- Campaign: `m9-m1-t1-rho-large-bezout-edge-gate`
- Round: 192
- Role: blind post-unmask reviewer
- Independence basis: the finalized statement-only rederivation was completed
  before the formal candidate was exposed
- Starting graph SHA-256 supplied by the candidate:
  `75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13`
- Numerical theorem evidence: none

## 1. Result: REPAIR

**REPAIR, not fail.** The candidate's central arithmetic reduction agrees
with the independent statement-only derivation:

- the canonical \(\beta\)-coordinate and its distinction from the literal
  transport quotient \(\gamma\);
- the exact factorization (192.C18);
- the signed-divisor bound (192.C19);
- the Farey-family and literal-row counts (192.C21)--(192.C23);
- the single-indicator safe union and fixed-level no-double-count algebra;
- the circular-pigeonhole bound (192.C33), core lower bound (192.C13), and
  coverage criterion (192.C14), provided \(T\geq1\) is stated explicitly;
- the conclusion that a nonempty core is not controlled by Farey separation
  for arbitrary bounded arrays; and
- the quarantine of the complete rho-large remainder and every downstream
  owner and exponent.

The candidate also exposes full-context hypotheses that repair the one
bookkeeping connector unavailable in the blind packet: (192.C4) implies
\(U\leq u\ll L\ll X^{1/4}\), so the divisor arguments satisfy
\(|c+U\ell|<U^2\ll X^{1/2}\). Conditional on the newly exposed accepted
lift, terminal, Fejer, projective-band, and shell connectors, the passage
from (192.C26) to (192.C30) is arithmetically consistent and loses no
positive power of \(Y\).

The current candidate also states the exact fast projective predicate and
one nonempty power-of-two \(J\)-band in (192.C4a). This is a newly exposed
full-context connector. It only deletes rows in the fixed-band count, and
its later band assembly costs the logarithm already displayed in
(192.C29)--(192.C30); it creates no discrepancy with the blind lemma.

Five exact repairs are required before the formal candidate can pass.

1. **Attach \(T\geq1\) explicitly to every use of (192.C14).** At
   \(T=0\), \(P_A=0\) and the Farey union is empty by definition. The
   numerical inequality in (192.C14) can still hold, but it does not imply
   that the core is empty. The ell-zero observation also implies safe-union
   membership only for \(T\geq1\).
2. **Repair (192.C41).** The expression \(U/T\) is undefined when \(T=0\).
   For \(T\geq1\) and a nonempty rho-large sector, one may derive
   \(U/T\asymp Y/(Qm)\), but the claimed lower number of "target-sized
   covector pieces" additionally needs a defined central set, a proved
   cardinality for it, and a defined per-piece capacity. As written it is a
   diagnostic heuristic, not a formal consequence.
3. **Separate fixed-packet and outer levels in (192.C12).** The operator
   \(P_A\) is defined on \(\mathscr R_{\rm fix}\), whereas (192.C12) uses
   unqualified \(\mathscr R\) and \(\mathscr J_{\rm safe,191}\). State the
   exact fixed-level decomposition first and then apply the inherited linear
   outer operator. Equation (192.C27) supplies the correct fixed-level
   algebra.
4. **Add the missing anchor and affine-sign hypotheses for
   (192.C38)--(192.C40).** Congruence
   \(S_{0,\omega}(h)\equiv\epsilon_\omega\rho h\pmod U\) alone does not
   imply \(\theta_{+,c}\in\{-1,0\}\) or
   \(\theta_{-,c}\in\{0,1\}\): arbitrary height-dependent multiples of
   \(U\) can be added. The candidate must specify the exact canonical
   representative interval and the inherited rule producing
   \((-1)^{N_\omega}\). With those connectors, the displayed signs are
   algebraically correct.
5. **State the zero-extension hypothesis at (192.C37) and weaken the
   endpoint wording.** The long-step Abel identity is exact for a finite or
   summable array extended by zero and summed over all integer heights. Also,
   the two endpoint-translation formulas are not forced to agree; saying
   they are universally "unequal" is stronger than the algebra proves.

These repairs do not alter (192.C10), the exact core, the coverage
corollaries in their lawful \(T\geq1\) range, or the conclusion that
(192.C15)/(192.C42) remains open.

## 2. Exact statement, hypotheses, and claim classification

The following claims follow from the blind statement and the independent
derivation, without using the newly exposed Round-191 structure:

1. Equations (192.C5)--(192.C9), including the piecewise definition
   \(P_A=0\) at \(T=0\).
2. Equations (192.C16)--(192.C19), with signed \(\rho\), signed \(\beta\),
   and \(c<U\) essential to the nonzero right side.
3. The fixed-covector count (192.C21), family size (192.C22), and literal
   multiplicity (192.C23), once the divisor factor is left explicit or the
   polynomial \(U\)-to-\(X\) connector is supplied.
4. The Farey approximation statements (192.C31)--(192.C33), hence
   (192.C13) and (192.C14) for \(T\geq1\).
5. The exact support-only core and the bounded-array no-go.

The following are newly exposed full-context hypotheses or connectors and
are not consequences of the blind packet alone:

- the shell, parity, height, profile, and polynomial-size assumptions
  (192.C1)--(192.C4), together with the exact fast predicate and fixed
  power-of-two band (192.C4a);
- the accepted Round-191 projection identity and its definitions in
  (192.C24)--(192.C27);
- the positivity of the inherited restricted terminal and Fejer envelopes;
- the lift, coefficient mass, band, divisor, and shell ledger
  (192.C28)--(192.C30);
- the precise outer assembly in (192.C11)--(192.C12);
- the anchor, affine parity, phase, and endpoint rules used in
  (192.C34)--(192.C40); and
- the durable dependency and graph-scope declarations in Section 7 of the
  candidate.

The review can test the algebra after these claims are stated, but it cannot
certify that they are accepted graph connectors from the permitted context.
They require their designated full-context seam or conductor check.

The candidate's intended narrow theorem should therefore read as follows.
For every fixed admissible packet, define the row multiplier

\[
 P_A(v)=1_{T\geq1}
 1_{\{\exists(c,d)\in\mathcal F_A:
              |c\beta-d\rho|\leq T\}}.
\]

Then the statement-only count, together with (192.C1)--(192.C4), proves

\[
 |P_A\mathscr R_{\rm fix}|
 \ll_{B,C_0,\varepsilon}Qm\kappa uX^\varepsilon.
\]

At the fixed level the exact decomposition must be written

\[
 \mathscr J_{\rm safe,192,fix}
 =\mathscr J_{\rm safe,191,fix}+P_A\mathscr R_{\rm fix},
 \qquad
 \mathscr R_{\rm core,fix}=(I-P_A)\mathscr R_{\rm fix}.
\]

Only afterward may the inherited linear operator
\(\mathcal O_{Y,Q}^{\sigma}\) be applied. For \(T\geq1\), the core is the
row set satisfying every strict covector inequality, and it obeys

\[
 |\rho|\geq(A+1)(T+1).
\]

For \(T=0\), it is the entire inherited rho-large remainder, with no
covector inequality added.

## 3. Proof and line-by-line derivation audit

### 3.1 Signs, canonical quotient, and factorization

The sign assertions in (192.C16) pass. From
\(\rho v_0-\beta U=1\),

\[
 \rho>0\Longrightarrow0\leq\beta<\rho,
 \qquad
 \rho<0\Longrightarrow\rho\leq\beta<0.
\]

Thus \(0\leq\beta/\rho\leq1\), including the positive edge
\((1,0)\) and negative edge \((-1,-1)\). A common divisor of \(\rho\) and
\(\beta\) divides one, so (192.C16) is exact.

For \(v=v_0+nU\), comparison of
\(\rho v-\gamma U=1\) with (192.C5) gives
\(\gamma=\beta+n\rho\), verifying (192.C17). Multiplying (192.C5) by
\(c\) and subtracting \(d\rho U\) verifies (192.C18). Since
\(1\leq c\leq A\leq U-1\), the right side is nonzero. If \(c=U\) were
allowed, \((d,\ell)=(v_0,-1)\) would give the exact zero-right-side
exception, so the strict cutoff is necessary.

### 3.2 Divisor bound, floors, and literal multiplicity

For fixed \((c,d,\ell)\), every admissible signed least inverse divides
\(c+U\ell\), and a chosen signed inverse determines at most one canonical
unit residue. Hence (192.C19) is correct with the factor
\(2\tau(|c+U\ell|)\).

The candidate's new connector (192.C4) closes the caveat recorded in the
blind report:

\[
 U\leq u\ll L\ll X^{1/4}.
\]

Together with \(T\leq(U-1)/2\) and \(c<U\), this gives

\[
 0<|c+U\ell|<U^2\ll X^{1/2}.
\]

For \(T\geq1\), summing the signed-divisor estimate over the
\(2T+1\leq3T\) ell values proves (192.C21). The exact family count is

\[
 |\mathcal F_A|=2+\sum_{2\leq c\leq A}\varphi(c)\ll A^2,
\]

and a fixed residue appears \(O(u/U+1)=O(u/U)\) times because \(U\mid u\).
Thus (192.C22)--(192.C23) pass. The projective and literal masks, including
the current fixed-band predicate (192.C4a), only delete rows.

At \(T=0\), none of these \(T\)-proportional bounds may be invoked. The
candidate correctly defines \(P_A=0\), but this convention must also govern
all later coverage prose.

### 3.3 Union projection, fixed-packet bound, and outer ledger

The single union indicator in (192.C9) counts each row once. The sum over
covectors occurs only in the positive upper bound, so overlaps cause no
algebraic double count. With the inherited per-row atom capacity,
(192.C23) proves (192.C26), and fixed powers of
\(A\leq Q^{C_0}\) are logarithmic because of (192.C1). Thus (192.C10)
passes.

Assuming the newly exposed accepted identity (192.C24), the algebra
(192.C25)--(192.C27) is correct:

\[
 \mathscr J_{\rm inv,fix}
 +(I-P_A)\mathscr J_{\rm terminal,fix}
 +(I-P_A)\mathscr J_{\rm Fejer,fix}
 +P_A\mathscr J_{\rm fix}
\]

replaces the terminal and Fejer pieces on selected Farey rows by the
complete selected original packet. It does not duplicate them. The claim
that restriction cannot increase their accepted positive bounds is a
full-context positivity connector, not something supplied by the blind
statement; it must be checked against the actual definitions.

Conditional on (192.C28)--(192.C29), the power ledger (192.C30) is
consistent. The \(m^{-1}\) factor cancels the fixed-packet \(m\) before
positive summation, \(A^2\) contributes only \(Q^{2C_0}\), and the
\(\kappa,u\) sum is of \(L^2\)-scale up to logarithms. No \(Y\)-power
remains because it was canceled earlier using
\(T\leq QmU/Y\). This verifies the algebra of (192.C11) while leaving the
accepted status of its connectors to the full-context review.

Equation (192.C12) is not yet formally exact because it changes notation
from \(\mathscr R_{\rm fix}\) to \(\mathscr R\) without defining the
assembly level. The fixed-level formula in Section 2 of this review, followed
by explicit linear application of \(\mathcal O_{Y,Q}^{\sigma}\), repairs
the one-outer-operation seam.

### 3.4 Coverage and the \(T=0\) exception

Put \(r=|\rho|\), \(b=|\beta|\). Then
\((r,b)=1\), \(0\leq b\leq r\), and
\(|c\beta-d\rho|=|cb-dr|\). The circular-gap proof in Section 5 of the
candidate matches the blind derivation and proves (192.C33).

If \(T\geq1\) and a row lies in the core, the integer minimum is at least
\(T+1\). Therefore

\[
 |\rho|\geq(A+1)(T+1),
\]

and the core is empty if

\[
 \left\lfloor\frac{(U-1)/2}{A+1}\right\rfloor\leq T.
\]

The claimed equivalent form

\[
 U\leq2(A+1)(T+1)-1
\]

is correct because \(U\) is odd and all quantities are integral.

This implication is false without the premise \(T\geq1\), because the
candidate deliberately defines \(\mathcal E_A=\varnothing\) at \(T=0\).
For example, even when \((U-1)/2\leq A\) makes the left side of (192.C14)
zero, the ell-zero covector is not selected. The formal statement should
therefore say "For \(T\geq1\), the core is guaranteed empty when
(192.C14)." The fact that \((|\rho|,|\beta|)\) is a primitive ell-zero
covector is always true, but its coverage consequence has the same
\(T\geq1\) premise.

### 3.5 Newly exposed phase and carry identities

Equations (192.C34)--(192.C37) pass algebraically, subject to an explicit
zero-extension hypothesis in (192.C37). Indeed,

\[
 d_v=cn+d,
 \qquad
 \Delta=cv-d_vU=cv_0-dU,
\]

and (192.C17)--(192.C18) give both equations in (192.C35). Since \(U=mq\),

\[
 e(\epsilon_\omega a\rho\Delta/q)
 =e(\epsilon_\omega ac/q),
\]

which proves (192.C36). For a finite zero-extended array,
reindexing \(h-\Delta\) proves (192.C37); the identity is a self-return and
provides no saving.

Equations (192.C38)--(192.C40) need an exposed normalization. If, for
example, \(S_{0,+}(h)\) and \(S_{0,-}(h)\) are the unique representatives
of \(\rho h\) and \(-\rho h\) in one fixed interval of length \(U\), then
\(\rho\Delta=c+U\ell\) gives

\[
 N_+(h;\Delta)=\theta_{+,c}(h)-\ell,
 \qquad \theta_{+,c}(h)\in\{-1,0\},
\]

\[
 N_-(h;\Delta)=\theta_{-,c}(h)+\ell,
 \qquad \theta_{-,c}(h)\in\{0,1\}.
\]

Thus the signs in (192.C39) are correct under that canonical-anchor rule.
But congruence alone permits
\(S_{0,\omega}(h)\mapsto S_{0,\omega}(h)+k(h)U\), which changes
\(N_\omega\) by \(k(h+\Delta)-k(h)\) and destroys the asserted two-value
range. The candidate must also state or cite the inherited affine sign rule
that converts this carry into \((-1)^{N_\omega}\) in (192.C40).

The endpoint formulas in (192.C35) show that equality of translations is
not structurally enforced. They do not prove literal inequality for every
row and covector, especially in edge cases. Replace "they are unequal" by
"they are not forced to agree and depend on the representative, endpoint,
and orientation."

### 3.6 Core capacity and method boundary

The qualitative bounded-array no-go passes. A static arithmetic selector
does not correlate arbitrary bounded coefficients: on any finite permitted
atom set, phase-conjugate coefficients can align all terms. This is an
operator-class obstruction only and supplies no literal lower mass.

The quantitative first sentence surrounding (192.C41) does not yet pass as
a formal claim. When \(T\geq1\) and the rho-large sector is nonempty,
\(T<(U-1)/2\), so the floor term is the active minimum and

\[
 T\leq\frac{QmU}{Y}<T+1\leq2T.
\]

Only in this regime does
\(U/T\asymp Y/(Qm)\) follow. A lower bound on the number of covering pieces
also needs the size of the set being covered and a uniform upper capacity
for one defined piece. Neither "central residue set" nor "target-sized
covector piece" is defined. The sentence should either be made a precise
conditional counting lemma or demoted to diagnostic prose. It cannot be
used at \(T=0\).

The open claims (192.C15) and (192.C42) are correctly quarantined. No actual
literal coefficient feature is proved to cancel the core, so the candidate
does not prove the complete rho-large remainder or any downstream result.

## 4. First doubtful or unproved step

As the candidate is currently written, the first newly exposed unproved
formal step is the bounded carry assertion (192.C39): it does not follow
from the congruence in (192.C38) without the canonical representative rule.
The next formal defects are the fixed/global ambiguity in (192.C12) and the
undefined/scopeless quantitative claim (192.C41).

After the five repairs in Section 1 and independent verification of the
newly exposed accepted connectors, the first genuinely open mathematical
step returns to exactly the candidate's stated frontier:

\[
 |\mathscr R_{\rm core,fix}|
 \ll_{C_0,\varepsilon}Qm\kappa uX^\varepsilon,
\]

or its assembled version (192.C15). Farey separation alone cannot prove
this estimate.

## 5. Control tests and outcomes

1. **\(T=0\): REPAIR.** The empty projector is defined correctly, but
   (192.C14), the ell-zero coverage prose, and (192.C41) must explicitly
   exclude this regime.
2. **Signed inverse and \(\beta\) signs: PASS.** Equations
   (192.C16)--(192.C18) have the correct positive and negative edges.
3. **Floors and saturation: PASS after the \(T\geq1\) qualifier.** The
   equivalent form of (192.C14) is exact. If
   \(T=(U-1)/2\), the rho-large sector is already empty.
4. **Divisor bound: PASS.** Equations (192.C19)--(192.C23) retain the signed
   factor, ell zero, \(c<U\), and literal residue multiplicity. The new
   (192.C4) connector justifies the \(X^\eta\) absorption.
5. **Farey-family cost: PASS.** \(A^2\leq Q^{2C_0}\) is a fixed
   polylogarithmic cost because of (192.C1).
6. **Fast predicate and \(J\)-band: FULL-CONTEXT CONNECTOR, count PASS.**
   Equation (192.C4a) is not present in the blind packet, but it is a row
   deletion at fixed band and is compatible with (192.C23); its band sum is
   part of the asserted logarithmic outer ledger.
7. **Union projection and overlaps: PASS at fixed level; REPAIR (192.C12).**
   The indicator and (192.C27) are exact, but fixed and assembled notation
   must be separated.
8. **Terminal/Fejer restriction: FULL-CONTEXT CONNECTOR.** The algebra is
   valid if their accepted envelopes are positive under row deletion; that
   property is not present in the blind packet.
9. **Outer ledger: FULL-CONTEXT CONNECTOR, algebra PASS.** Equations
   (192.C28)--(192.C30) close (192.C11) if the stated accepted identities and
   index ranges are verified externally to this blind review.
10. **Coverage: PASS for \(T\geq1\).** Equations (192.C31)--(192.C33) prove
   (192.C13)--(192.C14) in precisely that regime.
11. **Long-step phase: PASS.** Equations (192.C34)--(192.C37) are exact for
    finite zero-extended arrays; resonance gives self-return failure, not
    saving.
12. **Carry parity: REPAIR/CONNECTOR.** The signs in (192.C39) are
    conditionally correct, but canonical anchor ranges and the inherited
    affine sign convention are missing.
13. **Endpoint translations: REPAIR WORDING.** They are not forced equal;
    universal inequality is not proved.
14. **Quantitative cover count (192.C41): REPAIR.** Add \(T\geq1\),
    nonempty-sector, set-size, and piece-capacity hypotheses, or remove it as
    a numbered formal claim.
15. **Bounded-array closure: PASS as a no-go.** It is correctly separated
    from literal lower mass and does not disprove (192.C15).
16. **Original-\(t=1\) and downstream scope: PASS.** The candidate explicitly
    leaves the full rho-large packet, complete original \(t=1\), every
    \(t\geq2\) range, parents, bridges, theorem, and exponents unchanged.

No computation or external source was used.

## 6. Dependencies and exact artifacts used

This post-unmask review used only the authorized four artifacts:

- `protocol.md`, SHA-256
  `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`;
- `rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/reports/blind_unimodular_covector_rederivation.md`,
  SHA-256
  `186081c5acb3896598b36f9edc18e683df1b5f5162261a46dfb4da6ffc00a461`;
- `rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/blind_statement.md`,
  SHA-256
  `8650eb7142a4e8d498b3b3f9a8c6cbdf451486c554822dfb5a3e301ad005505c`;
- `rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/candidates/formalized_hard_m1_t1_rho_large_farey_covector_reduction.md`,
  SHA-256
  `4914693c73b6a3e1c3f761aa752a076c6ddbcb1b716b326645419260749cb4b6`.

No sibling report, strategy artifact, graph file, reconciliation, earlier
round, source, control, kernel, synthesis, or state file was inspected.
Claims labeled full-context connectors above are therefore explicitly not
certified by this review.

## 7. Recommended state effect

**Revise the candidate; make no state change yet.** Preserve the narrow
Farey safe-union lemma, fixed-level exact core, divisor and literal-row
counts, \(T\geq1\) coverage corollaries, and bounded-array no-go. Repair the
five formal seams in Section 1 and route the newly exposed Round-191 and
outer-ledger connectors to their full-context owners.

After those repairs pass, a subordinate reduction may be considered for
promotion. Keep (192.C15)/(192.C42), the complete rho-large remainder,
complete original \(t=1\), every \(t\geq2\) range, all M1 and M2 parents,
endpoint uniformity, M9, both bridges, the quarter target, and every exponent
open, conditional, or unchanged.
