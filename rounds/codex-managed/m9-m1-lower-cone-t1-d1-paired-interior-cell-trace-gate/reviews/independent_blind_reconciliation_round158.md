# Independent reconciliation of the Round 158 blind cell-trace report

- Campaign: m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate
- Reviewed artifact: reports/blind_cell_trace_rederivation.md
- Review role: independent reconciliation against the accepted Round 157 kernel
- Status: review evidence only; no shared-state mutation

## 1. Result

**Verdict: retain with explicit revisions.** The blind report is a
substantively successful independent rederivation of the finite algebra.
Its positive-prefix and negative-suffix Abel identities, moving-atom
signs, outer-endpoint indexing, full-frequency physical trace,
strict-prefix/suffix ranges, endpoint prime-power tables, complementary
frequency bookkeeping, and \(c=4\) control agree with the accepted
kernel.

Four qualifications are required before any claim is imported.

1. The blind report's normalization doubt is resolved by the accepted
   identity (K157.3): its formula (2.2), unnormalised Fourier convention,
   and scalar
   \(\alpha=-i(1+i)/(2Nq)\) are correct.
2. Its formulas (3.15)--(3.21) are not an accepted proof for the
   special frequencies. They conditionally reinterpret the theta
   multiplier as a standard Kloosterman sum and, even if a comparable
   pointwise Weil bound is granted, retain an \(L^2\) capacity. The
   actual \(v=0\) and \(v=H/2\) Abel pieces are target-safe by opening
   the accepted kernel and summing its nonzero additive frequencies
   geometrically.
3. Its refusal to infer \(V\asymp K\) is correct from the intentionally
   sparse blind statement, which gives only support span. It is not
   correct after importing the literal kernel (K157.1): the two
   boundary weights force \(V\asymp K\) whenever the trace is nonzero.
4. The campaign's \(D=1\) scalar target is
   \(O_\varepsilon(X^\varepsilon)\), not
   \(O_\varepsilon(M^{-1/4}X^\varepsilon)\). The special rows and
   endpoint subrow satisfy the stronger bound, while the strict
   survivor needs only raw \(M^{3/4}\) cancellation.

The blind report therefore independently validates the
endpoint-root-only no-go. It does not prove the whole trace impossible,
and its exact outer Abel terms are bookkeeping outside the isolated
moving-cell trace.

## 2. Exact statement and hypotheses under review

Let

\[
 I=\{j\in\mathbb Z:V<j\le2V\}=[a,b]\cap\mathbb Z.
\tag{R158.BR1}
\]

Then the signed blocks are \(J_+=[a,b]\) and
\(J_-=[-b,-a]\). Retain the frozen \(D=1\) scale
\(M\le N^{1/2}\) and
\(M^{3/4}(\log(2X))^A<V\le K=\sqrt{NM}\). For every odd
\(d\mid N\), retain

\[
 q=4N,\qquad c=q/d,\qquad H=c/2,\qquad n=H/2=N/d
\tag{R158.BR2}
\]

and the unnormalised Fourier coefficient
\(\widehat B_j(2dv)\). The accepted Round 157 coefficient is

\[
 B_j(x)=
 \mathbf1_{x\ge1}\mathbf1_{-x\le j\le x-1}
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right).
\tag{R158.BR3}
\]

Thus the blind factorization
\(B_j(x)=\mathbf1_{x\ge\lambda_\sigma(j)}F_j(x)\) is exact on each
signed block, but the accepted kernel supplies more information than
the blind statement: it locates the profile at scale \(M\), rather
than specifying only an \(O(KX^\varepsilon)\) support span.

The isolated object is only the middle moving-atom contribution after
Abel summation. The two outer terms and the two profile-difference
remainders must be printed, but they are quarantined from the trace
target. The external factor \(B_{1,U}(1)\) is a different assembly
seam. The blind report's description of \(\alpha\) as the “external
scalar seam” should not be read as closing or replacing
\(B_{1,U}(1)\).

The correct scalar target for the normalized trace is

\[
 \mathcal C_{\mathrm{int},U}(V)
 \ll_\varepsilon X^\varepsilon.
\tag{R158.BR4}
\]

All stronger \(M^{-1/4}X^\varepsilon\) estimates below are safe errors,
not the definition of (R158.BR4).

## 3. Proof and line-by-line reconciliation

### 3.1 Abel signs, endpoints, and cell indexing

The blind positive identity (3.1) is exact:

\[
 \sum_{j=a}^{b}A_jT_j
 =A_bP_b+\sum_{j=a}^{b-1}(A_j-A_{j+1})P_j.
\tag{R158.BR5}
\]

Its pointwise difference

\[
 B_j-B_{j+1}
 =\mathbf1_{x\ge j+2}(F_j-F_{j+1})
  +\mathbf1_{[j+1,j+2)}F_j
\tag{R158.BR6}
\]

puts the moving atom at \(x=j+1\) with positive sign. The exact outer
term is the right endpoint \(A_bP_b\), whose physical cutoff is
\(x\ge b+1\).

The blind negative identity (3.4) is also exact:

\[
 \sum_{j=-b}^{-a}A_jT_j
 =A_{-b}S_{-b}
  +\sum_{j=-b+1}^{-a}(A_j-A_{j-1})S_j.
\tag{R158.BR7}
\]

The difference

\[
 B_j-B_{j-1}
 =\mathbf1_{x\ge-j+1}(F_j-F_{j-1})
  +\mathbf1_{[-j,-j+1)}F_j
\tag{R158.BR8}
\]

puts the moving atom at \(x=-j\), again with positive sign. The exact
outer term is the left signed-block endpoint \(A_{-b}S_{-b}\), whose
physical cutoff is \(x\ge b\). Consequently the outer and bulk formulas
in blind (3.7)--(3.8) are correct, but none is part of the isolated
cell trace.

The resulting cell ranges are also exact. Positive cells have
\(k=j+1\in[a+1,b]\), \(a\le s\le k-1\), with strict range
\(k\in[a+2,b]\), \(a\le s\le k-2\). Negative cells have
\(k=-j\in[a,b-1]\), \(-k\le s\le-a\), with strict range
\(k\in[a+1,b-1]\), \(-k+1\le s\le-a\). Thus blind
(1.1)--(1.2) and (3.9)--(3.12) have the correct endpoints.

### 3.2 Inverse normalization

The accepted identity (K157.3) is precisely the blind formula (2.2)
with \(G=B_j\). The scalar check is

\[
 -\frac{i(1+i)}{2Nq}
 =-\frac{2i(1+i)}{q^2},\qquad q=4N,
\tag{R158.BR9}
\]

and the all-\(d\) recombination gives

\[
 G_N(t)=\mathbf1_{N\mid t}\chi _4(t/N).
\tag{R158.BR10}
\]

Therefore the physical formulas (1.1)--(1.2) are correctly normalized;
no additional \(q^{-1}\) belongs in the unnormalised Fourier
coefficient. The “first doubtful normalization” in blind Section 4 was
an appropriate statement-only caveat, but it is GREEN after
reconciliation with the accepted kernel.

### 3.3 Special-frequency trace pieces

The exact subtraction in blind (3.13)--(3.14) is correct:
\(v=0\) has no spatial modulation, while \(v=n=c/4\) contributes
\(e_c(-2nx)=(-1)^x\). What is not accepted is the subsequent
standard-Kloosterman interpretation.

For the actual theta kernel, opening the \(u\)-sum gives, for
\(w=0\) or \(w=n\) and every consecutive interval \(J\),

\[
\begin{aligned}
 \sum_{s\in J}K(-w^2,-s;c)
 &=\sum_{u\bmod c}^{*}\beta_{c,w}(u)
   \sum_{s\in J}e_c(-us),\\
 |\beta_{c,w}(u)|&=1.
\end{aligned}
\tag{R158.BR11}
\]

Every \(u\) is a nonzero unit, so geometric summation gives

\[
 \sup_J\left|\sum_{s\in J}K(-w^2,-s;c)\right|
 \ll c\log(2c).
\tag{R158.BR12}
\]

With \(\eta=M^{-3/4}X^\varepsilon\), \(L\asymp V\), and all exterior
factors restored, either Abel-trace piece satisfies

\[
\begin{aligned}
 |\mathcal C^{(w)}|
 &\ll_\varepsilon
 \frac{\eta L}{Nq}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}d\,c^{3/2}X^\varepsilon\\
 &\ll_\varepsilon
 \eta\,\frac{V}{\sqrt N}X^\varepsilon
 \le M^{-1/4}X^\varepsilon.
\end{aligned}
\tag{R158.BR13}
\]

This directly proves the two special-frequency trace pieces, including
all odd divisors and \(c=4\). Blind (3.17)--(3.21) should remain only a
conditional capacity calculation: its \(L^2\)-term becomes
\(\eta V^2/N\asymp\eta M=M^{1/4}\) on the nonzero top block and does
not prove even the scalar target.

### 3.4 Endpoint arithmetic and strict survivor

The blind prime-power table is complete and correct. For
\(j(j-1)\), the roots modulo every \(p^\nu\), including \(2^\nu\), are
exactly \(0,1\), giving \(2^{\omega(N)}\) CRT classes. For
\(j^2+j+1\), there are no \(2\)-adic roots; modulo \(3\) there is the
single root \(1\), with no lift modulo \(9\); and for \(p\ne2,3\)
there are two simple roots at every \(p^\nu\) exactly when
\(p\equiv1\pmod3\). Its CRT count and solvability criterion are
therefore correct, with the usual \(N=1\) convention.

These tables govern only \(s=k-1\) and \(s=-k\). Blind
(3.9)--(3.10) correctly retain the strict terms and correctly
distinguish the selected quotient
\(\ell=(k^2-s)/N\) from the frozen coefficient
\(F_{k-1}(k)\) or \(F_{-k}(k)\). Its two simple strict controls validly
disprove an endpoint-only logical implication. They do not constitute
a literal asymptotic counterexample: freely supporting one arbitrary
boundary sample, the dyadic placement, and the accepted \(w_U\)-support
must not be imported from the sparse statement into (K157.1).

### 3.5 Support localization and scalar calibration

Blind control 5 is internally correct for the statement-only packet:
a support-span upper bound does not locate the support. The accepted
literal kernel adds exactly the missing location. At the two moving
boundaries it gives

\[
\begin{aligned}
 F_{k-1}(k)
 &=w_U\!\left(\frac{k^2-k+1}{N}\right)
   e\!\left(\sqrt{k^2-k+1}-k\right),\\
 F_{-k}(k)
 &=w_U\!\left(\frac{k^2+k}{N}\right)
   e\!\left(\sqrt{k^2+k}-k\right),
\end{aligned}
\tag{R158.BR14}
\]

with all inherited zero extensions and transitions. Since
\(\operatorname {supp}(w_U)\asymp M\) and a trace cell has
\(k\asymp V\), a nonzero cell forces

\[
 k^2/N\asymp M,\qquad V\asymp K=\sqrt{NM}.
\tag{R158.BR15}
\]

Blocks whose boundary arguments miss the literal support are genuine
zero ranges for the trace. On a nonzero block,
\(K/M=\sqrt{N/M}\gg1\), so the selected support bound becomes
\[
 L_{\rm str}\ll_\varepsilon M X^\varepsilon.
\tag{R158.BR16}
\]

After removing the atom scale \(\eta=M^{-3/4}X^\varepsilon\), the
correct missing estimate is raw \(M^{3/4}X^\varepsilon\):

\[
 \left|\mathcal S_{\rm str}(V)\right|
 \ll_\varepsilon X^\varepsilon.
\tag{R158.BR17}
\]

Absolute support gives only
\(\eta M=M^{1/4}X^\varepsilon\). Thus the required saving is a factor
\(M^{1/4}\); raw square-root cancellation would be sufficient but
stronger than necessary. The blind report's qualitative no-go remains
right, but its statement that no numerical target was supplied must be
replaced by this campaign calibration.

## 4. First doubtful, conditional, or unproved step

The blind report's first declared doubtful step, normalization (2.2),
is no longer doubtful: (K157.3) certifies it exactly.

The first non-promotable derivation in the blind report is (3.15).
The accepted \(K(-v^2,-s;c)\) is the theta/Salié-type multiplier with
the \(\epsilon_u(c/u)\) factor, not an object that may simply be
declared a “standard unnormalised Kloosterman sum.” A suitable
pointwise theta-Weil inequality may have a comparable gcd shape, but it
requires its own theorem and normalization audit. Even granting that
inequality does not promote (3.20): the \(L^2\) capacity misses the
correct scalar target on \(V\asymp K\). Formula (3.21) concerns outer
Abel terms, not the moving-cell trace, and is both conditional and
outside this target.

After replacing the special-row argument by (R158.BR11)--(R158.BR13),
the first genuine open mathematical input is the strict signed estimate
(R158.BR17), with the literal boundary arguments in (R158.BR14), the
positive and negative selectors, \(\chi _4(\ell)\), residual phases,
transitions, and hard endpoints. Endpoint roots and cardinality alone
do not prove it. The exact outer terms \(A_bP_b\) and
\(A_{-b}S_{-b}\), together with the profile-bulk differences, remain
separate adjacent-block/global-recombination seams; they are not
additional prerequisites for proving the isolated trace.

## 5. Control tests and outcomes

- **Abel endpoint indexing — GREEN.** Positive prefix, negative suffix,
  positive outer row \(b\), negative outer row \(-b\), and both moving
  atoms have the correct ranges and signs.
- **Outer-term scope — GREEN after qualification.** Blind
  (3.7)--(3.8) displays every outer and bulk term correctly. Its Result
  and Section 7 overstate their relevance if read as prerequisites for
  the moving-cell trace; they are quarantined.
- **Inverse normalization — GREEN.** Blind (2.2), (2.4), and (4.1)
  match (K157.3) and the unnormalised Fourier convention. The external
  \(B_{1,U}(1)\) seam remains separate.
- **Zero-frequency trace piece — GREEN only via replacement proof.**
  Exact subtraction is valid; the accepted proof is the interval
  estimate (R158.BR12), yielding (R158.BR13).
- **Nyquist trace piece — GREEN only via replacement proof.** The
  \((-1)^x\) factor and unique \(v=H/2\) indexing are correct; the same
  interval estimate proves the piece directly.
- **Weil capacities — CONDITIONAL/NO PROMOTION.** Blind
  (3.15)--(3.21) assumes the wrong named kernel interface and in any
  event supplies only upper capacities, including a forbidden
  \(M^{1/4}\) term at the scalar level.
- **Prime-power endpoint table — GREEN.** The \(2\)-adic,
  exceptional \(3\)-adic, simple odd-prime, Hensel, and CRT counts are
  all correct.
- **Strict survivor — GREEN as an identity and endpoint-route
  refutation.** Blind (3.9)--(3.10) has exact strict inequalities and
  keeps the quotient distinct from the boundary coefficient. Its
  arbitrary-profile controls are not literal lower bounds.
- **Support localization — GREEN as a blind caveat, REVISE on import.**
  The sparse statement does not imply \(V\asymp K\); the accepted
  literal profile does, by (R158.BR14)--(R158.BR15).
- **Target calibration — REVISE.** The target is
  \(O_\varepsilon(X^\varepsilon)\), requiring raw \(M^{3/4}\), while
  the special rows and endpoint row are stronger
  \(O_\varepsilon(M^{-1/4}X^\varepsilon)\)-scale errors.
- **Complementary modes and \(c=4\) — GREEN.** Both members of every
  ordinary orbit remain, the unique fold is removed once, and the
  \(c=4\) interior set is empty.
- **Downstream scope — GREEN after qualification.** No trace identity
  controls outer/profile-bulk terms, the full paired matrix, another
  \(D,L,t\) layer, M2, endpoint uniformity, M9, or the bridge.

No numerical experiment is needed for any reconciliation decision.

## 6. Dependencies and exact artifacts used

This review used exactly:

- protocol.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/blind_statement.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/reports/blind_cell_trace_rederivation.md; and
- proofs/kernels/m9_m1_d1_nonzero_centering_nyquist_fold.md.

The review did not inspect or review the discovery claimant's Round 158
report, any sibling source report, a candidate, synthesis, State Patch,
validation matrix, proof draft, or shared proof state. It used only the
accepted Round 157 kernel to resolve facts intentionally omitted from
the statement-only packet.

## 7. Recommended state effect

Recommend **retain/revise** the blind report as genuine independent
support for:

1. the exact prefix/suffix Abel algebra, including all outer endpoints
   and bulk terms;
2. the correctly normalized full-frequency physical cell trace;
3. the endpoint prime-power classification;
4. the exact strict selected survivor and the no-go for an
   endpoint-root-only proof; and
5. the complementary-mode and \(c=4\) controls.

Do not promote blind (3.15)--(3.21), the campaign-level
“no support localization” conclusion, the absence of a numerical
target, an arbitrary-profile lower-bound inference, or the claim that
outer Abel terms must be proved in order to close the isolated trace.
Replace the special-frequency estimates by (R158.BR13), import
\(V\asymp K\) only from the literal kernel, and calibrate the remaining
strict theorem to (R158.BR17).

The graph effect should be no direct mutation from this review. After
conductor adjudication, the exact blind algebra can corroborate the
trace reduction, while the strict signed selected estimate remains
open. Nothing here promotes the profile bulk, full paired matrix, a
broader owner, or a global exponent.
