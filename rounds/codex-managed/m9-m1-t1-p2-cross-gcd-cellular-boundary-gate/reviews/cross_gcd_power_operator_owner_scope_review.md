# Round 199 cross-gcd power/operator/owner/scope review

- Campaign: m9-m1-t1-p2-cross-gcd-cellular-boundary-gate
- Role: independent power/operator/owner-scope reviewer
- Starting/current graph SHA-256:
  63fa05e3a4d1493bc37bdd956453a4d3eefbb9dca6fadcbf8b7a68e32ade36b5
- Candidate SHA-256:
  261df263197c08f4816ed4e4c3a4845db445d00717847db243cca68e935ba23b
- Kernel SHA-256:
  ae0111a603cf07479098E47E0C67904CCEB10E363188671174DB5B85EE447A0C
- Numerical theorem evidence: none

## 1. Result

**REPAIR.** The packet and outer powers, the \(P_2/P_1\) owner
classification, the one-outer-norm rule, the capacity caveats, the
mechanism-only conclusion, and the graph/exponent quarantine are
substantively correct. In particular, neither artifact proves the
three-piece estimate, declares \(P_1\) safe, closes complete \(P_2\), or
changes a parent or exponent.

The pair is not yet suitable for durable acceptance for four precise
reasons.

1. The physical \(P_2\) and three-piece masks are correctly placed before
   spectral operations, but the accepted later cap/open projector is not
   distinguished sharply enough from a physical allocation-orbit mask.
   The \(B\)-\(E\)-\(C\) cycle changes the inward cross gcd in both primitive
   charts, so it is not a fixed-\(\kappa\), fixed-orientation open-packet
   orbit.
2. \(P_1\) is correctly identified as the unproved lower-far owner, but
   neither artifact gives its authoritative definition. That omission is
   material because the statement-only packet calls it “two-far,” whereas
   the accepted Round-193 partition defines
   \(P_1=\mathbf1_{\{|d-gm|>D_L\}}\), with no upper-far condition.
3. The durable kernel is a substantial compression, not a verified
   candidate transcription. A full no-index comparison changes 321 lines
   (113 insertions and 208 deletions). It drops frozen parity, shift,
   coefficient, complement, status, and state-effect data and thus broadens
   the displayed character-quotient statement beyond its live hypotheses.
4. Provenance and acceptance status are incomplete. The candidate has no
   exact dependency/provenance section, and the kernel neither cites the
   formal candidate nor says that graph acceptance is pending a valid State
   Patch. Its declarative “records” and “therefore ... closes” wording is
   stronger than the candidate's pending-review status.

These are formalization and operator-typing repairs. They do not overturn
the displayed coefficient-one self-return or require a new analytic
mechanism.

## 2. Exact audited statement and hypotheses

The admissible claim is the following narrow route boundary.

Fix the exact literal squarefree source with

\[
 N=dm,\qquad N+r=d'm',\qquad
 0<r<\lceil L\rceil,\qquad 2\mid r,
\]

with \(d,d'\) odd, the total zero-extended endpoint coefficients, and the
physical coefficient \(W\). Apply

\[
 P_2=\mathbf1_{\{|d-gm|\le D_L\}}
     \mathbf1_{\{|d'-gm'|>D_L\}},\qquad g=(d,d'),
\]

and

\[
 P_{\partial\mathrm{lit}}+P_{s\mathrm f}+P_{g\mathrm f}
\]

to the physical source before Fourier, height, anchor, Farey, packet, or
orientation decomposition. The accepted cap/open projector is a later
linear projector and is not an allocation-orbit mask. Its surviving region
is

\[
 \kappa<D_L,\qquad
 M:=\min(Y,D_L)>H_B\mathfrak m\kappa.
\]

The proposed complete-allocation cellular mechanism self-returns on the
mandatory aligned face: the same-\(g\) \(B\)-\(E\)-\(C\) triangle has actual
character holonomy \(+1\); endpoint product completion requires the
\(G_{00}\) corner \(V_A\), whose recomputed gcd is \(Aq\); and on large live
shells

\[
 |d-(d,d')m|_{V_A}=Aq|u-x|>D_L.
\]

Under the authoritative Round-193 partition this is exactly the unproved
lower-far mask

\[
 P_1:=\mathbf1_{\{|d-(d,d')m|>D_L\}}.
\]

There is no requirement that the upper defect also be far. Omitting
\(V_A\) leaves the structural coefficient-one endpoint term; including it
crosses the \(P_2/P_1\) owner boundary. This is only a no-go for the frozen
physical cellular identity. It is neither a lower bound nor a disproof of

\[
 \left|\mathscr R_{\mathrm{open,out}}^\sigma
 ((P_{\partial\mathrm{lit}}+P_{s\mathrm f}+P_{g\mathrm f})W)\right|
 \ll L^2X^\varepsilon
\]

by another coefficient-sensitive method.

## 3. Proof and seam audit

### 3.1 Physical masks, cap/open timing, and orientations

The candidate correctly imposes \(P_2\) at (199.K2) before all spectral
operations and repeats this order in Section 6. The kernel likewise says
that the three-piece physical mask precedes spectral decomposition. That
part passes.

The later open projector needs an explicit separate sentence. In the plus
primitive chart

\[
 \kappa=G_{01}=C,
\]

and in the minus chart

\[
 \kappa=G_{10}=B.
\]

For the candidate's vertices,

\[
\begin{array}{c|ccc}
 &V_B&V_E&V_C\\ \hline
 B&q&1&1\\
 C&1&1&q,
\end{array}
\]

so the plus inward gcd is \(1,1,q\), while the minus inward gcd is
\(q,1,1\). The cycle is genuinely \(P_2\)-preserving, but it is not
fixed-\(\kappa\) and cannot be paired inside a separate orientation norm.
This agrees with the accepted rejection
Round197-open-packet-condition-is-physical-orbit-mask: the packet condition
is applied only later through the linear cap/open projector.

The candidate merely lists packet and orientation restoration. The
kernel's Scope is more ambiguous: it says the mechanism is tested on the
open inequalities and on the exact mask “before spectral decomposition,”
which can attach the timing phrase to both. The repair must state that only
\(P_2\) and the three failure masks are coordinatewise physical masks; the
whole allocation cell is formed before the packet split; and no
fixed-\(\kappa\), one-orientation cancellation is claimed. Both \(T=0\)
and every simultaneous strict \(T\ge1\) branch then remain inside the later
full replay. Since the no-go is pre-Farey, it proves no branchwise bound.

### 3.2 \(P_2/P_1\) ownership

The owner conclusion itself passes. At the missing corner

\[
 V_A=(Aqu,x,Aqy,v),\qquad (Aqu,Aqy)=Aq,
\]

and the recomputed lower defect is \(Aq|u-x|\). From
\(A|x-qu|\le D_L\), \(q\ge3\), and the inherited live-shell lower bound
\(qu\gg L\), it exceeds \(D_L\) for all sufficiently large live shells.
Thus \(V_A\in P_1\). Bounded shells can be paid absolutely, but that does
not license the asymptotic \(P_1\) boundary.

The graph confirms that only the Round-193 partition is proved; no \(P_1\)
estimate is proved. The hard small-\(t\) owner
M9-M1-hard-top-high-radical-small-t-residual-estimate remains open. The
candidate and kernel consistently call \(P_1\) unproved and never put it
in \(E_{\rm safe}\). They must, however, insert the exact definition above
to remove the conflict with the blind packet's informal “two-far” wording.

The aligned use also needs one explicit support qualifier:
\(C_{\rm lit}=0\) at the paired \(V_E,V_C\) vertices. With \(p=-1\), those
two vertices then belong to \(P_{\partial\rm lit}\), while \(V_B\), with
\(B=q>1\), belongs to \(P_{g\rm f}\). Without the code-mismatch qualifier,
the same triangle can contain the already proved \(P_{\rm cc}\) sector and
is not by itself the stated three-piece target.

### 3.3 Outer norm and powers

The norm placement passes. The candidate displays one absolute value only
after \(\mathscr R_{\mathrm{open,out}}^\sigma\), and both artifacts
explicitly retain orientations, \(T\)-branches, phases, endpoint
translations, selectors, commutators, carries, births/deaths, cells,
crossings, Fourier copies, and zero extensions before the single outer real
part. No fixed-height, fixed-conductor, fixed-anchor, fixed-mode, component,
or orientation modulus is substituted.

The power ledger is also exact:

\[
 u\{\kappa+M\}X^\varepsilon
 \quad\hbox{versus}\quad
 H_B\mathfrak m\kappa uX^\varepsilon,
\]

and on the open region the unresolved part has ratio

\[
 \frac{M}{H_B\mathfrak m\kappa}>1.
\]

At outer scale the aligned unit face retains only the inherited positive
capacity

\[
 D_LL^2X^\varepsilon
\]

against \(L^2X^\varepsilon\). No factor \(D_L\), \(M\), \(Y\), \(\kappa\),
\(\mathfrak m\), or \(L\) is hidden in \(X^\varepsilon\). These formulas are
upper envelopes only; neither artifact converts them into nonemptiness,
nonvanishing, density, mass, or a literal lower bound.

One phrase should nevertheless be tightened. The candidate's result says
that the orbit has a “nonzero actual twisted augmentation.” What is proved
in (199.K15) is the nonzero actual-sign incidence augmentation of the
constant-endpoint control. The literal endpoints are not shown constant or
nonzero. Later caveats repair the intended meaning, but the result sentence
should use the qualified formulation so it cannot be read as literal
nonvanishing or an arbitrary-array theorem.

### 3.4 Sign branches and an internal candidate-only overstatement

For the displayed odd \(q\), same-\(A\) triangle the actual edge quotients
\(t,p,tp\), their product \(1\), and the constant-endpoint values in
(199.K15)/(K199.8) are consistent. The \(p=-1\) aligned obstruction is
therefore unaffected.

Candidate Section 5 additionally says, “If the swapped character is zero,
the mate is a literal live/dead boundary.” That is not a consequence of the
displayed triangle. Here \(r\) is even, \(d,d'\) are odd, and the triangle
has \(E=1\). Hence a live triangle has \(N,N+r\) odd and
\(p,t\in\{\pm1\}\); the zero-character class belongs to a different even
cross-state configuration. The kernel correctly omits this sentence.
Delete it from the candidate, or explicitly mark it as an unanalyzed
outside-triangle case which is unnecessary because the aligned face already
stops the mechanism.

### 3.5 No-go, graph, and exponent scope

The intended scope passes. The candidate expressly leaves the literal
three-piece estimate open to another method and excludes lower mass and
nonvanishing. Its final list correctly leaves complete \(P_2\), \(P_1\),
the rest of original \(t=1\), all original \(t\ge2\) incidences, the
large-\(G\) complement, complete hard and smooth M1, GAR, every M2 parent,
endpoint uniformity, M9, both bridges, and the quarter target open or
conditional.

The graph hash in the candidate equals the current authoritative file
hash. The relevant statuses are unchanged:

- M9-M1-hard-top-high-radical-small-t-residual-estimate: open;
- M9-M1-top-endpoint-signed-cone: open;
- M9-M1: open;
- M9: open;
- the Round-195 absolute-capacity node and Round-197 common-cell node:
  proved_internal only in their exact subordinate scopes.

The exponent sentence is accurate: the internal \(1/3\) theorem, the
accepted external \(0.3144831759740614\ldots\) theorem, and the target
\(1/4\) are unchanged.

The kernel must not itself sound graph-accepted. It currently opens with
“This kernel records” and concludes “Therefore the frozen mechanism
closes,” but it carries no pending-review/State-Patch status. Replace that
with a conditional state sentence: this is a candidate durable kernel;
subject to the remaining reviews and a mechanically valid State Patch, the
recommended terminal label is
p2_cross_gcd_cellular_boundary_self_return_no_go. The only admissible owner
effect is inconclusive/no-go evidence on the existing open small-\(t\)
owner and mechanism-scoped rejected-claim entries. No proved obligation,
dependency, blocker, target-safe sector, or exponent is added.

### 3.6 Candidate/kernel equivalence and provenance

The formulas common to both artifacts are consistent, but the kernel is
not an exact durable transcription. In particular, it omits from the
candidate:

1. \(0<r<\lceil L\rceil\), \(2\mid r\), and \(d,d'\) odd;
2. the total zero-extended endpoint hypothesis and the boxed outer target;
3. the exact three-piece definitions and the \(C_{\rm lit}=0\) aligned
   restriction;
4. the explicit false-control and downstream-scope ledger;
5. the starting graph, pending status, and exact proposed state effect.

The parity omission is not cosmetic. The kernel calls \(t,p,tp\) actual
character quotients. Those quotients require nonzero character factors on
the live odd sector. Without the frozen even-shift/odd-divisor hypotheses,
the compressed statement is broader than the derivation and a quotient can
be undefined. The safest repair is to formalize the repaired candidate body
verbatim in the durable kernel, changing only the title and
status/provenance wrapper.

All five sources currently listed by the kernel exist, but the lineage is
still incomplete. Add the formal candidate itself, its hash, the campaign,
round, starting graph hash, generation time, role/status, and exact
dependencies. Add an exact dependencies/provenance section to the candidate
as required by the protocol's artifact metadata rule. The kernel should
identify the candidate as its immediate formalization source rather than
jumping directly from reports and reconciliation.

## 4. First doubtful or unproved step

The first power/operator defect is the missing typed distinction between
the pre-spectral physical failure masks and the later linear cap/open
projector, together with the omitted plus/minus \(\kappa=C/B\) table.
Until repaired, “on the open packets” can be misread as saying that the
\(B\)-\(E\)-\(C\) triangle is a fixed-packet orbit, which it is not.

The first genuinely unproved analytic step remains exactly the theorem the
artifacts leave open: a coefficient-sensitive joint bound for

\[
 P_{\partial\mathrm{lit}}+P_{s\mathrm f}+P_{g\mathrm f}
\]

on the Round-195 open projector after the complete two-orientation,
two-\(T\)-branch outer replay. No estimate for \(P_1\), no cancellation of
the coefficient-one face, and no different signed mechanism is supplied.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Physical \(P_2\) timing | **PASS.** \(P_2\) is imposed before Fourier/height/Farey operations. |
| Three-piece mask timing | **PASS.** The complement remains a joint physical mask before positivity. |
| Cap/open timing | **REPAIR.** State explicitly that the accepted open projector is later and is not an allocation-orbit mask. |
| Plus/minus orientation ledger | **REPAIR.** Add \(\kappa=C\) in the plus chart and \(\kappa=B\) in the minus chart, and show the \(1,1,q/q,1,1\) migration. |
| Both \(T\)-branches | **PASS with clarification.** Both are retained; say that the pre-Farey no-go proves no branchwise estimate. |
| \(P_1\) owner | **PASS with definition repair.** \(V_A\) is lower-far and \(P_1\) is unproved; insert \(P_1=\mathbf1_{|d-gm|>D_L}\). |
| Aligned target membership | **REPAIR.** Insert \(C_{\rm lit}=0\) so \(V_E,V_C\in P_{\partial\rm lit}\) and \(V_B\in P_{g\rm f}\). |
| One outer norm | **PASS.** No separate orientation, branch, conductor, height, or component modulus is taken. |
| Packet power | **PASS.** The deficit \(M/(H_B\mathfrak m\kappa)>1\) is exact. |
| Global power | **PASS.** \(D_LL^2X^\varepsilon\) retains the missing \(D_L\). |
| Capacity versus mass | **PASS after wording repair.** Capacities are upper only; qualify “nonzero actual augmentation” as the constant-endpoint incidence control. |
| Zero-character clause | **REPAIR.** Delete it or move it outside the odd \(E=1\) triangle as unanalyzed and unnecessary. |
| No-go scope | **PASS.** The literal theorem remains open to another method. |
| Safe-owner audit | **PASS.** No unproved \(P_1\), \(P_{s\rm f}\), or \(P_{g\rm f}\) sector is treated as safe. |
| Graph and exponents | **PASS.** All named parents remain open and \(1/3\), \(0.314483\ldots\), and \(1/4\) are unchanged. |
| Candidate/kernel equivalence | **REPAIR.** Restore the omitted hypotheses, operator typing, controls, and state effect in the kernel. |
| Provenance/status | **REPAIR.** Add exact metadata, hashes, candidate lineage, and pending-State-Patch language. |
| Numerical evidence | **PASS.** None is used. |

## 6. Dependencies and exact artifacts used

1. protocol.md —
   f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a;
2. state/proof_obligations.yml —
   63fa05e3a4d1493bc37bdd956453a4d3eefbb9dca6fadcbf8b7a68e32ade36b5;
3. state/active_campaign.yml —
   d757f3f9adc3d331952bc39b3831cfd61b69cbf0028255ece6b299ca59a87a2c;
4. rounds/codex-managed/m9-m1-t1-p2-cross-gcd-cellular-boundary-gate/blind_statement.md —
   88d047a62d54ede7939de68b72dec6f51edbd64d9a541673f664b0b5cea3dd39;
5. rounds/codex-managed/m9-m1-t1-p2-cross-gcd-cellular-boundary-gate/candidates/formalized_hard_m1_t1_p2_cross_gcd_cellular_boundary_self_return.md —
   261df263197c08f4816ed4e4c3a4845db445d00717847db243cca68e935ba23b;
6. proofs/kernels/m9_m1_hard_top_t1_p2_cross_gcd_cellular_boundary_self_return.md —
   ae0111a603cf07479098e47e0c67904cceb10e363188671174db5b85ee447a0c;
7. rounds/codex-managed/m9-m1-t1-p2-cross-gcd-cellular-boundary-gate/reviews/conductor_round199_report_reconciliation.md —
   a8ddf14bff21d9cae94aea466d54d4187f5b1a9409ad20502ee3271611115ca6.

The reconciliation was used only to audit the candidate/kernel provenance
and the whole-swap versus partial-block distinction. No web source,
external theorem, or computation was used.

## 7. Recommended state effect and exact repairs

Do not apply a State Patch from the current artifacts. Make the following
repairs, then repeat candidate/kernel equivalence and power/operator review.

1. In both artifacts define \(P_1\) exactly as the Round-193 lower-far mask
   and state that no upper-far predicate is required. If the blind packet
   remains part of the final evidence bundle, correct its “two-far” label as
   well.
2. Separate the timing in a displayed operator paragraph: \(P_2\) and the
   three-piece complement are physical pre-spectral masks; the allocation
   cell is formed before packet/orientation splitting; the accepted
   cap/open projector is later and linear.
3. Add the plus/minus table \(\kappa=C/B\) and the \(q\)-migration through
   \(V_B,V_E,V_C\). Explicitly reject any fixed-\(\kappa\),
   one-orientation, or branchwise norm interpretation.
4. State \(p=-1\) and \(C_{\rm lit}=0\) on the mandatory aligned face so the
   two same-\(g\) vertices are in \(P_{\partial\rm lit}\) and the \(B=q\)
   vertex is in \(P_{g\rm f}\).
5. Replace “nonzero actual twisted augmentation” with “nonzero actual-sign
   incidence augmentation in the constant-endpoint control”; retain the
   explicit denial of literal nonvanishing or lower mass.
6. Delete the candidate's zero-character sentence, or explicitly mark it
   as an outside-triangle, unanalyzed case not used by the no-go.
7. Restore in the kernel the exact even-shift, odd-divisor, zero-extension,
   open-target, complement, false-control, downstream-scope, and
   state-effect hypotheses. Prefer a verbatim mathematical body shared with
   the repaired candidate.
8. Add complete artifact metadata and provenance. The kernel must cite the
   repaired candidate and hash as its immediate source and must say that it
   is pending review and a mechanically valid State Patch.
9. Replace the kernel's unconditional closing wording by the exact
   recommendation: after successful re-review, record only the
   mechanism-scoped terminal label/rejected claims and inconclusive
   evidence on the existing open hard-M1 small-\(t\) owner. Add no proved
   node, dependency, blocker, safe sector, parent implication, theorem, or
   exponent change.

REPAIR
