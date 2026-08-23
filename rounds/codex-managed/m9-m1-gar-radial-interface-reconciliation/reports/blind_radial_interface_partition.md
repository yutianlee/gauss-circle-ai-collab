# 1. Result: exact owner partition and a no-go for automatic endpoint closure

**Result (blind radial-interface mismatch lemma).**  There is a fixed, exact,
one-count radial partition

\[
 \mathcal G_X=\mathcal G_X^{\rm low}
                 +\mathcal G_X^{\rm crit}
                 +\mathcal G_X^{\rm col},
\tag{120.R1}
\]

in which the middle term is covered by (120.B4), the first term is the
separate lower-radial parent, and the last term contains the complete sharp
upper collar, including the hard top.  If

\[
 \mathcal P_X^+=
 \sum_{hq\leq N_X}^{*}\chi _4(q)(hq)^{-3/4}
 H^{\rm prof}_{\infty,X}(h,q),
\tag{120.R2}
\]

is the accepted physical upper endpoint prefix, then coefficientwise
subtraction gives

\[
 \mathcal G_X^{\rm col}=\mathcal P_X^++\mathcal R_X^{\rm ri}.
\tag{120.R3}
\]

The exact formula for \(\mathcal R_X^{\rm ri}\) is given in Section 2.  Since
\(\mathcal P_X^+\ll_W1\), the sharp upper/interface parent is target-safe if
and only if \(\mathcal R_X^{\rm ri}\ll_\varepsilon X^\varepsilon\).

This is a strict identification of the already-owned physical-prefix
subpackage, but it does **not** close the radial-interface parent.  The stated
hypotheses give neither a coefficient identity nor an estimate connecting
the sharp radial-collar coefficient to
\(H^{\rm prof}_{\infty,X}(h,q)\).  The endpoint boundary package cannot fill
that gap: its lower prefix and recombined \(R_1\) residue are routed boundary
terms, not coefficients of the original radial collar, and its two diagonal
transition traces are explicitly excluded.  Thus the smallest exact
unmatched remainder definable from the permitted statement is
\(\mathcal R_X^{\rm ri}\), and its first unmatched coefficient is the
difference in (120.R10) below.

# 2. Exact statement and hypotheses

Assume (120.B1)--(120.B5) and the endpoint boundary and global radial
one-count statements in the blind packet, with \(X\) large,
\(Y=\sqrt X\), \(y=\lfloor\sqrt X\rfloor\), and
\(N_X=\lfloor16Y\rfloor\).  All factorization sums below use exactly the
domain in (120.B1), in particular \(q\) is odd.

Let \(\tau_X(n)\) denote the literal star multiplier in (120.B3):

\[
 \tau_X(n)=
 \begin{cases}
 1,&n<N_X,\\
 \tfrac12,&n=N_X,\\
 0,&n>N_X.
 \end{cases}
\tag{120.R4}
\]

Choose once and for all smooth functions \(L,U:[0,\infty)\to[0,1]\) with

\[
 \begin{aligned}
 &L(t)=1 &&(0\leq t\leq1),&\qquad L(t)=0&&(t\geq2),\\
 &U(t)=0 &&(0\leq t\leq14),&\qquad U(t)=1&&(t\geq15),
 \end{aligned}
\tag{120.R5}
\]

and put \(V=1-L-U\).  The transitions can be chosen monotone, so that
\(0\leq V\leq1\), and
\(V\in C_c^\infty((1/2,31/2))\); in particular its upper support endpoint is
strictly below \(16\).  This is a fixed partition, independent of \(X\).

For \(F\in\{L,V,U\}\), define the exact radial owner

\[
 \mathcal G_X[F]
 :=\sum_{n\leq N_X}\tau_X(n)F(n/Y)\mathcal C_X^*(n)n^{-3/4}
 e(\sqrt{Xn}).
\tag{120.R6}
\]

Thus
\(\mathcal G_X^{\rm low}=\mathcal G_X[L]\),
\(\mathcal G_X^{\rm crit}=\mathcal G_X[V]\), and
\(\mathcal G_X^{\rm col}=\mathcal G_X[U]\).
The literal divisor-pair form of the collar is

\[
 \mathcal G_X^{\rm col}
 =\sum_{hq\leq N_X}\tau_X(hq)\chi_4(q)(hq)^{-3/4}
 U(hq/Y)e(\sqrt{Xhq})\Omega_X^*(hq,h),
\tag{120.R7}
\]

where \(\Omega_X^*\) is left exactly as in (120.B2).  Hence every
\(D_j=2^{-j}y\), \(H_j=\lfloor D_jX^{-1/4}\rfloor\), height cutoff,
\(\Phi\)-factor, internal \([w_j]^*\), hard \(j=0\) sample, support crossing,
and sign is retained once.

Group the accepted prefix coefficient by its physical product:

\[
 \mathcal H_X^{\rm prof}(n)
 :=\sum_{\substack{hq=n\\q\ \text{odd}}}
 \chi_4(q)H^{\rm prof}_{\infty,X}(h,q).
\tag{120.R8}
\]

The exact unmatched radial/interface remainder is

\[
 \boxed{
 \mathcal R_X^{\rm ri}
 =\sum_{n\leq N_X}\tau_X(n)n^{-3/4}
 \left[
 U(n/Y)e(\sqrt{Xn})\mathcal C_X^*(n)
 -\mathcal H_X^{\rm prof}(n)
 \right].}
\tag{120.R9}
\]

Equivalently its divisor-pair coefficient before the common factors
\(\tau_X(hq)\chi_4(q)(hq)^{-3/4}\) is

\[
 \boxed{
 \Delta_X(h,q)=
 U(hq/Y)e(\sqrt{Xhq})\Omega_X^*(hq,h)
 -H^{\rm prof}_{\infty,X}(h,q).}
\tag{120.R10}
\]

At the hard top, \(N_X/Y\geq15\) for \(Y\geq1\), so \(U(N_X/Y)=1\).  The
first explicitly visible unmatched grouped coefficient is therefore

\[
 e(\sqrt{XN_X})\mathcal C_X^*(N_X)
 -\mathcal H_X^{\rm prof}(N_X),
\tag{120.R11}
\]

and it occurs with the original half tie
\(\tfrac12N_X^{-3/4}\).  No equality or bound for (120.R11) is among the
stated hypotheses.

# 3. Proof or derivation

Because \(L+V+U=1\) pointwise, multiplying the literal summand of (120.B3)
by this identity proves (120.R1).  This operation does not alter
\(\mathcal C_X^*\), so all inner stars, floors, signs, and support conventions
remain untouched.  Reindexing the finite \(n\)-sum by \(n=hq\) gives
(120.R7), with \(\tau_X(hq)\) retaining the product half tie.

The function \(V\) is fixed and lies in
\(C_c^\infty((1/2,31/2))\), whose upper endpoint is less than \(16\).
Moreover \(V(N_X/Y)=0\), so the starred and unstarred versions of its sum
coincide.  Applying (120.B4) yields

\[
 \mathcal G_X^{\rm crit}\ll_{\varepsilon,V}X^\varepsilon.
\tag{120.R12}
\]

The lower term in (120.R1) is left as the separate open lower parent, exactly
as required by the global radial one-count statement.  Thus the only upper
radial owner after deletion of the fixed critical sector is (120.R7).

Now insert the algebraic zero
\(\mathcal P_X^+-\mathcal P_X^+\) into (120.R7).  Grouping by \(n=hq\)
gives (120.R3) and (120.R9)--(120.R10) without changing any coefficient.
By (120.B5), \(\mathcal P_X^+=O_W(1)\), hence

\[
 \mathcal G_X^{\rm col}\ll_\varepsilon X^\varepsilon
 \quad\Longleftrightarrow\quad
 \mathcal R_X^{\rm ri}\ll_\varepsilon X^\varepsilon.
\tag{120.R13}
\]

This equivalence is at the normalized level.  Only after it is proved may
the accepted external \(X^{1/4}\) factor be restored; no \(X^{1/4}\) is
available inside (120.R9).

It remains to check whether the accepted endpoint package makes
\(\Delta_X(h,q)\) vanish or bounds its sum.  It does not do so on the supplied
hypotheses.  A radial collar is the original coefficient in (120.R7), selected
by the physical variable \(hq/Y\) and still terminated sharply by
\(hq\leq N_X\).  In contrast, (120.R2) is an integration-by-parts endpoint
prefix after an accepted common physical limiting procedure.  Equality of
these objects would require an explicit transform identity, including all
cutoff derivatives, support-edge samples, artificial-pole cancellation, and
the two diagonal transition traces.  No such identity appears in the blind
statement; indeed the accepted boundary package expressly excludes the two
traces.

Nor can the lower boundary prefix or the recombined \(R_1\) residue be
declared part of \(\mathcal G_X^{\rm col}\).  Their target-safe assertion is
for their common routed aggregate.  They have no supplied coefficient map to
\(U(n/Y)\mathcal C_X^*(n)e(\sqrt{Xn})\), and the lower radial owner in
(120.R1) is independently open.  Adding those boundary terms to (120.R7)
would cease to be a one-count radial partition.  Therefore the only
coefficientwise subtraction justified by an explicit formula and a separate
bound is (120.R2), leaving exactly (120.R9).

Finally, fixed-smooth transfer cannot close the gap by exhaustion.  A finite
collection of admissible functions in (120.B4) has support below some fixed
\(C<16\), and hence misses an entire collar next to \(16\).  An
\(X\)-dependent family whose support approaches \(16\) is outside (120.B4);
using it would require a uniform estimate in cutoff seminorms and a summable
collar decomposition.  Neither is stated.  Consequently (120.R13) is the
strict reduction available here, not a proof of its right-hand side.

# 4. First doubtful or unproved step

The first unproved step needed for closure is the coefficientwise transform
comparison

\[
 U(hq/Y)e(\sqrt{Xhq})\Omega_X^*(hq,h)
 \stackrel{?}{=}
 H^{\rm prof}_{\infty,X}(h,q)
 +E_X^{\rm interface}(h,q),
\tag{120.R14}
\]

together with a normalized signed bound for the sum of
\(E_X^{\rm interface}\).  Such a comparison must explicitly account for the
radial cutoff derivative/interface, the flat support edge, both diagonal
transition traces, the hard \(j=0\) sample, all floors and stars, and the
common physical-limit routing of artificial poles.  The blind statement
contains neither (120.R14) nor any substitute estimate for (120.R10).

In particular, replacing the accepted physical limit in (120.R2) by a
finite Mellin-height truncation is not an admissible step.  No uniform
finite-height theorem, truncation error, or interchange of limit with the
\((h,q,j)\)-sum is supplied.  This is the first seam at which a purported
endpoint-prefix proof of the collar would become unsupported.

# 5. Required control tests and outcomes

| Control | Exact input and expected invariant/failure | Observed outcome | Implication |
|---|---|---|---|
| `literal_global_radial_coefficient` | Insert (120.B1)--(120.B2) into (120.B3) without changing a coefficient. | (120.R7) retains \(\Omega_X^*(hq,h)\) literally. | Pass; the owner partition acts only by \(L,V,U\). |
| `external_X_one_quarter_normalization` | Test at the normalized level before restoring the external factor. | (120.R12)--(120.R13) target \(O_\varepsilon(X^\varepsilon)\); no internal \(X^{1/4}\) was used. | Pass. |
| `fixed_radial_partition_one_count` | Verify one fixed pointwise identity and one owner per original summand. | \(L+V+U=1\) proves (120.R1) exactly. | Pass; no additional flat or connector summand was inserted. |
| `compact_critical_transfer_scope` | Require fixed \(V\in C_c^\infty((c,C))\), \(C<16\), and forbid moving endpoint cutoffs. | The chosen \(V\) is supported in \([1,15]\); (120.B4) proves only (120.R12).  Finite fixed partitions still miss the top collar. | Pass as a scope audit; attempted endpoint exhaustion fails. |
| `upper_endpoint_prefix_coefficient` | Compare the literal collar coefficient with the physical-prefix coefficient. | Their exact difference is \(\Delta_X(h,q)\) in (120.R10); no vanishing statement is supplied. | The accepted part is exactly \(\mathcal P_X^+\); the mismatch remains open. |
| `endpoint_boundary_and_R1_routing` | Use the endpoint package only after its common physical routing and cancellation. | The lower prefix and recombined \(R_1\) have no stated map into the collar, while two diagonal traces are excluded. | They cannot be assigned as extra collar owners or used to erase (120.R10). |
| `radial_collar_vs_boundary_prefix` | Compare selection by \(U(hq/Y)\) under the sharp product top with an integration-by-parts boundary evaluation. | They are distinct formulas; equality would require the missing identity (120.R14). | Required distinction passes; automatic closure is rejected. |
| `floor_star_product_tie_hard_sample` | Preserve \(y,D_j,H_j\), both stars, the product tie, and \(j=0\). | They remain in \(\Omega_X^*\) and \(\tau_X(hq)\); (120.R11) displays the hard-top half tie. | Pass. |
| `physical_limit_vs_finite_height` | Permit only \(H^{\rm prof}_{\infty,X}\) in its accepted physical limit. | (120.R2), (120.R8), and (120.R10) use only that limit; no finite-height approximation is made. | Pass; finite Mellin truncation remains unavailable. |
| `lower_parent_disjointness` | Keep the lower radial owner independent of boundary-prefix terminology. | \(\mathcal G_X[L]\) is untouched, and no lower boundary term is charged to \(\mathcal G_X[U]\). | Pass. |
| `downstream_scope` | Determine only the normalized radial-interface implication for GAR. | Critical transfer plus (120.R13) reduces the upper owner; the lower parent and \(\mathcal R_X^{\rm ri}\) are still required. | No claim of GAR or full M1 closure follows. |

A further adversarial localization control diagnoses why the missing seam is
real.  At the level of the stated estimates, place a coefficient spike at an
integer \(n_X\) with \(n_X/Y\to16\), and set the prefix coefficient there to
zero.  Every fixed \(V\) allowed by (120.B4) eventually misses the spike and
(120.B5) still holds, while the sharp collar sees it.  This is not asserted to
be a counterexample to the fixed physical \(\Omega_X^*\); it is a rigorous
non-implication test showing that the two accepted estimates alone cannot
bound (120.R9).  The missing physical coefficient identity or signed collar
estimate is indispensable.

# 6. Dependencies and exact artifacts used

This statement-only derivation used exactly:

1. `AGENTS.md`;
2. `protocol.md`;
3. `problems/gauss_circle.md`;
4. `state/control_models.md`;
5. `rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/blind_statement.md`;
6. `rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/briefs/blind_radial_interface_partition.md`.

No proof graph, strategy file, derivation packet, Round-98 artifact,
Round-120 nonblind artifact, sibling report, shared proof draft, validation
matrix, web source, or computation was used.

# 7. Recommended state effect

**Retain** the radial-interface parent as open, while recording
(120.R1)--(120.R10) as candidate evidence for a strict exact reduction.  The
accepted physical upper prefix \(\mathcal P_X^+\) is already target-safe and
may be removed once, but the residual \(\mathcal R_X^{\rm ri}\) must not be
promoted without either (i) a full coefficientwise physical transform identity
plus bounds for every interface and diagonal trace, or (ii) a direct signed
\(O_\varepsilon(X^\varepsilon)\) estimate for (120.R9).  Reject any state
change that identifies the sharp radial collar with the boundary prefix,
uses arbitrary finite Mellin height, imports the lower endpoint aggregate
into the upper owner, or inserts an additional connector-completed summand.

---

## Follow-up addendum: hostile audit of (120.C1)--(120.C8)

### Addendum result and verdict

**Verdict: retain, not promote.**  The terminal-height construction contains
a useful and apparently correct coefficientwise geometry: after one
support-constant correction and explicit restriction to active heights,
(120.C5) and (120.C7) survive the hostile audit.  In particular, (120.C7)
really can bypass the endpoint-prefix mismatch (120.R10); it does so by a new
terminal-height estimate, not by identifying a radial collar with an
integration-by-parts prefix.

The construction is nevertheless incomplete as written.  The implications
(120.C1) \(\Rightarrow\) (120.C2) and, more decisively, (120.C3)
\(\Rightarrow\) the \(V_{\rm low}\)-localized terminal estimate used in
(120.C8), require transform and error theorems not stated or derived in the
candidate.  The accepted fixed critical transfer (120.B4) applies to
\(\mathcal C_X^*\), not automatically to the newly truncated
\(\mathcal C_{T,X}^*\).  Until the terminal multiplier is carried through the
smooth transform, hard transform, both frequency signs, and every boundary
and aggregate error with a summable uniform estimate, (120.C8) is not proved.

### Support constants and floors

The assertion that the certified profile lies in
\([1/2,C_W]\) for some \(C_W<3/2\) fails if the certified support reaches
\(3/2\).  The valid choice is \(C_W=3/2\), with the endpoint convention
retained.  This changes (120.C6) to the safe fixed constant

\[
 c_T=\frac{\kappa^2}{4(3/2)^2}
     =\frac{\kappa^2}{9}
     =\frac{s_0}{144}>0.
\tag{120.A1}
\]

This correction does not destroy the compact lower support.

All floor inequalities must be conditioned on an actual atom.  Put
\(x_j=D_j/R\).  If a summand with \(1\leq h\leq H_j\) exists, then
\(H_j=\lfloor x_j\rfloor\geq1\), hence \(x_j\geq1\) and

\[
 \frac{x_j}{2}\leq \lfloor x_j\rfloor\leq x_j.
\tag{120.A2}
\]

Consequently

\[
 \frac h{H_j}\geq\frac{hR}{D_j},
\qquad
 \frac{D_j}{H_j}\leq2R.
\tag{120.A3}
\]

Thus the floor step in (120.C5) is valid.  If
\(\vartheta(h/H_j)\ne0\), then \(h/H_j>\kappa/2\), and (120.A2) gives

\[
 \frac{hR}{D_j}
 =\frac h{H_j}\frac{H_jR}{D_j}
 >\frac{\kappa}{4}.
\tag{120.A4}
\]

Together with \(t\leq3/2\), this proves the corrected lower support
(120.A1).  Likewise \(hR/D_j\leq1\) and \(t\geq1/2\) still imply
\(n/Y\leq16\).  Heights with \(H_j=0\) have no atoms and must be omitted
before writing \(h/H_j\); otherwise the definition of the terminal
multiplier contains a division by zero.  These are repairable presentation
issues, not a falsification of (120.C5)--(120.C6).

### Transform applicability and error ownership

The terminal dyadic-shell estimate before transformation is plausible on
active heights: the support of \(\vartheta\) places
\(\kappa H_j/2<h\leq H_j\), only \(O_{s_0}(1)\) fixed-ratio shells are needed,
and (120.A3) supplies the claimed \(1+D_j/H_j\ll R\).  It proves (120.C3)
only if the following missing transform seam is supplied.

One needs an exact two-sided identity

\[
 \mathcal B_{T}^{\pm}
 =c_\pm R
   \sum_{n\leq N_X}^{*}
   \mathcal C_{T,X}^{*,\pm}(n)n^{-3/4}
   e(\pm\sqrt{Xn})
   +\mathcal E_T^\pm
\tag{120.A5}
\]

with the terminal factor included and
\(\mathcal E_T^\pm\ll_\varepsilon X^\varepsilon\) after summing all active
\((j,h)\).  The candidate writes only the positive antecedent and then
identifies it with the full coefficient carrying the stipulated two-sign
data.  That identification needs either both versions of (120.A5) or an
explicit conjugacy argument with its real/symmetric hypotheses.

It is also not enough to say that the hard cotangent boundary and aggregate
errors remain polylogarithmic.  Multiplication by
\(\vartheta(h/H_j)\) creates an \(h\)-interface near
\(\kappa H_j\).  A valid proof must show, term by term, whether the smooth
and hard transform errors are bounded absolutely under that multiplier or
whether their old estimate used cancellation across the deleted heights.
Any artificial-pole, hard-sample, diagonal-transition, or \(R_1\) term must
be assigned exactly once.  The accepted full-height physical endpoint
package cannot simply be relabeled as the error of the terminal-height
transform; a linear decomposition or a fresh error bound is required.

### Does (120.C7) bypass the earlier remainder?

Yes, algebraically.  For \(s=n/Y\geq s_0\), \(t\geq1/2\) gives

\[
 \frac{hR}{D_j}=\frac{t\sqrt s}{2}
 \geq\frac{\sqrt{s_0}}4=\kappa,
\]

and (120.A3) yields \(h/H_j\geq\kappa\), so every nonzero atom has
\(\vartheta(h/H_j)=1\).  For \(s\leq s_0\),
\(1-V_{\rm low}(s)=0\), and throughout the transition
\(s_0<s<2s_0\) the same coefficient equality holds.  Therefore

\[
 (1-V_{\rm low}(n/Y))\mathcal C_X^*(n)
 =(1-V_{\rm low}(n/Y))\mathcal C_{T,X}^*(n)
\tag{120.A6}
\]

is exact, including the hard top, floors, and internal profile stars.

But (120.A6) is an identity, not an estimate.  From (120.C3) one still has
to bound

\[
 S_T[V_{\rm low}]
 :=\sum_{n\leq N_X}^{*}
 V_{\rm low}(n/Y)\mathcal C_{T,X}^*(n)n^{-3/4}
 e(\sqrt{Xn}).
\tag{120.A7}
\]

(120.B4) cannot be applied to (120.A7), because its coefficient is
\(\mathcal C_{T,X}^*\), not \(\mathcal C_X^*\).  Also
\(V_{\rm low}\) itself is not compactly supported away from zero.  The
corrected support result permits one to choose a fixed
\(\widetilde V\in C_c^\infty((c_T/2,C))\), with
\(2s_0<C<16\), such that
\(\widetilde V=V_{\rm low}\) on the support of
\(V_{\rm low}\mathcal C_{T,X}^*\).  Closure therefore reduces to the
following precise new lemma:

\[
 \sum_{n\leq N_X}^{*}
 \widetilde V(n/Y)\mathcal C_{T,X}^*(n)n^{-3/4}
 e(\sqrt{Xn})
 \ll_{\varepsilon,\widetilde V,s_0}X^\varepsilon.
\tag{120.A8}
\]

The sentence about Mellin separation sketches a possible proof of
(120.A8), but does not establish it.  It must provide a Mellin-uniform
version of (120.A5), including a sufficiently integrable dependence on the
Mellin variable, the \(O((1+|t|)/H_j)\) frequency-BV calculation for all
other amplitude factors, the hard \(j=0\) case, and the full transformed
error sum.  If (120.A5) and (120.A8) are proved, then (120.C8) follows and
does genuinely close the sharp nonlower radial owner.  In that event the
earlier mismatch (120.R9) is bounded as a consequence (after subtracting
the already-safe physical prefix); it is never asserted to vanish.

### Addendum state recommendation and provenance

Retain the terminal-height construction as a promising candidate and revise
its constants and hypotheses as above.  Do not promote (120.C8) until
(120.A5) and (120.A8), with exact error ownership and both signs, receive a
complete proof.  No counterexample was found to the corrected support
geometry or to (120.C7); the present obstruction is an unproved analytic
seam, not a geometric no-go theorem.

This addendum used only the prior permitted statement and brief together
with
rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/candidates/conductor_terminal_height_interface_completion.md.
The original seven sections retain their statement-only provenance; no
state, synthesis, sibling report, or other Round-120 artifact was read or
edited.
