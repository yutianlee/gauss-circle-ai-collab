# Round 164 downstream graph and State-Patch scope review

## Result

**Verdict: graph-scope GREEN; two rejected-overclaim additions and final
evidence cleanup are required before application.** The materialized
Round-164 State Patch has the correct mutation envelope. It creates exactly
one proved node,

<code>M9-M2-hard-top-t1-residual-transport-fejer-energy-reduction</code>,

and updates exactly the two open hard-TOP parents:

- <code>M9-M2-top-endpoint-signed-cone</code>; and
- <code>M9-M2-top-endpoint-density-discrepancy-energy</code>.

For each parent the new child is added only as a dependency, while all
Round-164 evidence is added only as inconclusive evidence. The patch changes
neither parent's statement, open status, blockers, nor implication edge. It
does not create or promote a complete-residual node, a full-\(t=1\) node, a
hard-TOP theorem, or any downstream theorem.

The child type <code>reduction</code> is appropriate. Its strongest durable
affirmative output is the exact endpoint-safe Fejer reduction to one open
actual-coefficient short-shift theorem; the positive-transport no-go is a
route-scoped component of that reduction. The five listed dependencies are
sufficient and acyclic. Some are transitively redundant through the
Round-163 child, but the redundancy makes the coefficient-energy, profile,
and rank-one comparison provenance explicit and creates no false
implication.

The earlier source-provenance concern is resolved. The completed card
<code>sources/bennett_martin_obryant_rechnitzer_2018.md</code> records the
exact fixed-\(q=4\) theorem, thresholds, fixed-relative interval deduction,
and physical-scope exclusions, and the patch cites it as positive evidence.
Thus the internally derived reduction may retain the audited diagnostic
four-prime capacity while remaining <code>proved_internal</code>; the
external prime theorem is not being promoted as a new independent theorem.

Two narrow overclaims should nevertheless be rejected explicitly:

1. the unweighted sum \(\sum_N\operatorname{osc}C_N\) is not a necessary
   estimate for the fixed literal profile; the literal BV/triangle target is
   \(\sum_N\operatorname{osc}C_N\,V_N\), while the unweighted quantity is
   only the coefficient-uniform \(V_N\ll1\) envelope; and
2. taking absolute values in the additive relation \(d'm'-dm=r\) does not
   literally produce the multiplicative character-Poisson collar
   \(\lvert s\ell-XQR\rvert\ll QRJ/L\). The two are independent positive
   routes with the same missing-power warning.

The current graph file has SHA-256

<code>81690ebb72b0dedd99bdb6c6127f947df696a901a22af3f65ac8738209125306</code>,

equal to the frozen Round-164 starting hash, and the repository validator
reports <code>Patch OK</code>. No authoritative state has been edited by
this review.

## Exact statement and hypotheses

The proposed child has:

- id:
  <code>M9-M2-hard-top-t1-residual-transport-fejer-energy-reduction</code>;
- type: <code>reduction</code>;
- track: <code>M9_analytic</code>;
- status: <code>proved_internal</code>;
- implications: none;
- blockers: none; and
- next action: the one-sided actual residual Fejer off-diagonal, followed
  by the remaining few-point channels.

Its direct graph dependencies are exactly:

1. <code>M9-M2-hard-top-t1-close-opposite-prime-exchange-sector</code>;
2. <code>M9-M2-hard-top-truncated-divisor-energy-and-radical-control</code>;
3. <code>M9-M2-hard-top-t1-character-poisson-product-collar-obstruction</code>;
4. <code>M9-M2-top-endpoint-actual-symbol-variation</code>; and
5. <code>H4-Phi-regularity</code>.

All five are proved accepted nodes. The first supplies the exact canonical
selector and XOR owner. The second supplies accepted coefficient-energy
provenance, although the displayed diagonal also follows from the elementary
divisor bound. The third supplies the independent rank-one positive-route
comparison. The fourth and fifth supply the literal profile and bounded
\(C^1\) variation interfaces. The child does not depend on either open
parent that receives it.

The accepted mathematical content is limited to:

1. the exact Boolean residual, retaining \(00\) and \(11\) selected-prime
   incidences after subtracting XOR exactly once;
2. the selected/no-pair sign-mass dichotomy;
3. ordered Abel summation and the sharp zero-extended unequal-mass bound
   \[
   |b_N^{\rm rem}|
   \le \frac12\operatorname{osc}(C_N)
      \sum_{j=0}^{r}|a_{j+1}-a_j|;
   \tag{164.G1}
   \]
4. the coefficient-uniform four-prime positive-transport capacity, with
   the literal-profile and outer-phase quarantine;
5. the exact sliding Fejer identity and van der Corput inequality; and
6. the exact expansion \(d'm'-dm=r\), explicitly left as an open signed
   short-shift frontier.

For the Fejer step, let an integer interval \(I_L\) of cardinality
\(M_L\asymp L^2\) contain the complete literal shell, extend
\(c_N^{\rm rem}\) by zero, and set

\[
 z_N=c_N^{\rm rem}e(J\sqrt N),\qquad R=\lceil L\rceil,\qquad
 Y_s=\sum_{j=0}^{R-1}z_{s+j}.
\tag{164.G2}
\]

Then the exact energy asserted by the patch is

\[
\begin{aligned}
 \mathfrak E_R^{\rm rem}
 &:={1\over R}\sum_{s\in\mathbb Z}|Y_s|^2\\
 &=\sum_N|c_N^{\rm rem}|^2
 +2\Re\sum_{1\le r<R}\left(1-\frac rR\right)
   \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}\,
   e\!\left(J(\sqrt{N+r}-\sqrt N)\right).
\end{aligned}
\tag{164.G3}
\]

The open theorem is only the one-sided aggregate estimate

\[
\Re\sum_{1\le r<R}\left(1-\frac rR\right)
 \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}\,
 e\!\left(\frac{Jr}{\sqrt{N+r}+\sqrt N}\right)
\ll_\varepsilon L^2X^\varepsilon.
\tag{164.G4}
\]

No absolute value is allowed around a shift, selector branch, parity branch,
or divisor opening.

## Proof or derivation

The dependency direction is acyclic. The accepted Round-162 profile/collar
interfaces feed the Round-163 XOR sector; the accepted energy and profile
interfaces, together with that sector, feed the new reduction; and only
then does the new reduction feed the two open hard-TOP parents. There is no
reverse dependency and the child has no implication edge. Directly listing
the collar, actual-symbol, and \(\Phi\)-regularity nodes in addition to their
transitive occurrence through Round 163 is redundant but sound.

The repaired Fejer identity is represented faithfully in the candidate,
kernel, and State Patch. Expanding the sliding square gives

\[
\frac1R\sum_s\sum_{0\le j,k<R}z_{s+j}\overline{z_{s+k}}.
\]

Each diagonal term occurs in \(R\) windows. For a pair
\((N,N+r)\), \(1\le r<R\), exactly \(R-r\) window starts contain both
members. Combining the two orientations gives the factor \(2\Re\) and the
weight

\[
\frac{R-r}{R}=1-\frac rR,
\]

which proves (164.G3), including both zero-extended endpoints.

Moreover every \(z_N\) occurs in exactly \(R\) sliding windows, so

\[
 \sum_sY_s=R\sum_Nz_N.
\tag{164.G5}
\]

Only starts whose length-\(R\) window meets \(I_L\) can contribute. There
are at most \(M_L+R-1\) such starts. Cauchy's inequality therefore gives
the exact endpoint-safe bound

\[
\boxed{
\left|\sum_Nz_N\right|^2
\le \frac{M_L+R-1}{R}\,\mathfrak E_R^{\rm rem}.}
\tag{164.G6}
\]

There is no omitted endpoint term and no missing factor of \(R\). Since

\[
 \sum_N|c_N^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon,\qquad
 M_L\asymp L^2,\qquad R\asymp L,
\]

(164.G4) makes \(\mathfrak E_R^{\rm rem}\ll_\varepsilon
L^2X^\varepsilon\), and (164.G6) then gives the target square
\(L^3X^\varepsilon\). The choice \(R\asymp L\) is the first length that
closes this worst-case \(M_L\asymp L^2\) ledger; the patch states the lower
comparison on \(M_L\), so its minimality language is properly scoped.

Opening the two actual coefficients is multiplicity one:

\[
 N=dm,\qquad N+r=d'm',\qquad d'm'-dm=r,\qquad 1\le r<R.
\tag{164.G7}
\]

The patch retains supported squarefree rows, odd character-bearing
\(d,d'\), the even factors in \(m,m'\), both residual selectors, both
literal profiles, and the square-root phase. Thus (164.G7) is only an exact
cross-\(N\) reduction. It contributes no cancellation by itself.

The JSON mutation scan is equally narrow:

- <code>create</code> has one entry;
- <code>update</code> has exactly the two open hard-TOP parents;
- each update adds the child as a dependency and adds only inconclusive
  evidence, together with a scoped next action;
- <code>correct_rejected</code> is empty;
- <code>reject</code> contains twenty-one Round-164 overclaims; and
- <code>no_change</code> explicitly preserves twenty accepted/open
  objects from the antecedent interfaces through both global exponents.

Consequently the accepted implication chain remains

\[
\text{density-discrepancy energy}
\longrightarrow \text{signed cone}
\longrightarrow \text{physical one-count assembly},
\tag{164.G8}
\]

with both first nodes open and no new implication from the child.

## First doubtful or unproved step

The first genuinely unproved mathematical step is (164.G4). Neither the
sharp BV identity, the coefficient-uniform four-prime capacity, the
diagonal \(L^2\) energy, exact radical collisions, nor the accepted
rank-one collar proves this one-sided actual-coefficient real-part bound.
A phase-adapted arbitrary array satisfies the coarse support and diagonal
scales but can have length-\(L\) Fejer energy \(L^3\); the future theorem
must use the literal residual arithmetic.

The first State-Patch completeness gap is not a graph edge but rejected
wording. The actual literal triangle estimate is

\[
 \sum_N\operatorname{osc}(C_N)V_N
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{164.G9}
\]

The unweighted sum \(\sum_N\operatorname{osc}C_N\) is only the
coefficient-uniform envelope after using \(V_N\ll1\). The patch's child
statement avoids the false necessity claim, but its rejected-claim list
should record this distinction because the candidate remains positive
evidence.

The second gap is the geometry comparison. Taking moduli in (164.G4)
leaves a positive additive-shift form on \(d'm'-dm=r\); it does not
literally turn it into the multiplicative collar
\(\lvert s\ell-XQR\rvert\ll QRJ/L\). The State Patch correctly treats the
rank-one collar as an independent route comparison and does not put the
false identity in the child statement, but an explicit rejection would
fully quarantine the stronger wording in the candidate.

Two final evidence mechanics are outside the mathematical graph decision.
The kernel still contains two doubled inline escapes around \(\rho_N\),
and the State Patch forward-references the not-yet-materialized conductor
adjudication. These should be cleaned/materialized before the patch is
applied. Neither affects (164.G3)--(164.G7).

## Required control test and outcome

| Control | Outcome |
|---|---|
| Starting graph hash | **GREEN.** The file hash equals the frozen Round-164 hash \(81690e\ldots5306\). |
| Mechanical patch schema | **GREEN.** The repository validator returns <code>Patch OK</code>. |
| Proposed node type | **GREEN.** <code>reduction</code> matches the exact Fejer sufficiency result; the no-go remains route-scoped within it. |
| Child status and source | **GREEN.** Internal algebra plus a completed fixed-\(q=4\) source card supports <code>proved_internal</code>; no physical prime-box claim is made. |
| Dependencies | **GREEN.** All five are accepted and point into the child; redundancy is harmless and there is no cycle. |
| One-time residual subtraction | **GREEN.** The residual is \(1,0,0,1\) on \(00,10,01,11\), exactly complementary to XOR. |
| Unequal sign mass and Abel/BV | **GREEN.** The zero-extended midpoint inequality retains unmatched mass and all hard jumps. |
| Repaired sliding identity | **GREEN.** The \(1/R\), \(R-r\) pair count, \(2\Re\), and \(1-r/R\) weights are exact. |
| Endpoint constant | **GREEN.** At most \(M_L+R-1\) windows give precisely the coefficient in (164.G6). |
| Power ledger | **GREEN.** \(M_L\asymp L^2\), \(R\asymp L\), and diagonal \(L^2X^\varepsilon\) reduce the target to (164.G4). |
| Cross-\(N\) opening | **GREEN as a reduction only.** The exact relation is \(d'm'-dm=r\), with literal domains retained. |
| Parent attachments | **GREEN.** Dependency plus inconclusive evidence and next action only; no parent field carrying theorem strength changes. |
| Residual/full \(t=1\) | **OPEN.** No residual or full-\(t=1\) target node is created or promoted. |
| Downstream/global state | **GREEN.** Hard TOP, BAL, UNBAL, M9--M2, M9--M1, endpoint uniformity, M9, bridge, target, and both exponents remain unchanged. |
| Existing rejected claims | **GREEN.** <code>correct_rejected</code> is empty; no earlier route-scope record requires correction. |
| New rejected coverage | **REVISE narrowly.** The twenty-one entries cover all promotion and physical-mass overclaims; add the weighted/unweighted and additive/multiplicative distinctions above. |
| Evidence artifacts | **REVISE mechanically.** Clean the two doubled kernel escapes and materialize the cited adjudication before application. |
| Numerical experiment | **NOT USED.** This review is exact algebra and graph inspection only. |

The resulting downstream quarantine is:

| Layer | Required state effect |
|---|---|
| Complete residual and full \(t=1\) | Remain open; (164.G4) is next action only |
| The two hard-TOP parents | Remain open; dependency and inconclusive evidence only |
| Other few-point channels and near collars | Remain open |
| BAL and UNBAL smooth packets | Remain open and unchanged |
| Physical one-count assembly and M9--M2 | Assembly reduction unchanged; M9--M2 open |
| M9--M1 and endpoint uniformity | Open and unchanged |
| M9 | Open and unchanged |
| Conditional bridge and quarter target | Bridge conditional; target open |
| Internal exponent | Remains \(1/3\) |
| External benchmark | Remains \((3292+25\sqrt{1717})/13762\), under its accepted narrow source audit |

The existing twenty-one rejected entries already rule out, among other
things, complete-residual or full-\(t=1\) closure, ambient-to-physical mass
transfer, free cemetery mass, hard-face counting, BV closure, physical
four-prime lower mass, diagonal-only Fejer closure, exact-collision
closure, positive-collar closure, shiftwise-modulus necessity, smaller
\(R\), endpoint error, universal no-go, remaining-channel transfer,
smooth-packet transfer, M9/bridge/target promotion, and exponent change.
The two additions requested above complete the seam-review coverage rather
than changing the patch's mathematical result.

## Dependencies and exact artifacts used

This review used:

- <code>protocol.md</code>;
- <code>state/proof_obligations.yml</code>;
- <code>state/active_campaign.yml</code>;
- the Round-164 plan and barrier packet;
- <code>candidates/conductor_round164_residual_transport_fejer_reduction.md</code>
  and the earlier conductor seed in the same gate;
- all three Round-164 primary reports;
- <code>controls/conductor_round164_reproduction_and_selection.md</code>;
- <code>controls/conductor_round164_updated_literature_scan.md</code>;
- <code>proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md</code>;
- <code>sources/bennett_martin_obryant_rechnitzer_2018.md</code>;
- the Round-164 blind post-unmask, blind repair, and
  transport/profile/power/source reviews;
- <code>rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/state_patch.json</code>;
- the Round-163 State Patch and downstream graph-scope review for the
  established child-to-parent evidence convention; and
- <code>math_collab/validate_state_patch.py</code>.

The authoritative entries inspected include the five proposed child
dependencies, both hard-TOP parents, the physical one-count assembly, both
smooth packet parents, M9--M2, M9--M1, endpoint uniformity, M9, the
conditional bridge, the quarter target, the internal one-third theorem, and
the audited external Li--Yang benchmark.

No web lookup, numerical experiment, symbolic experiment, or authoritative
state mutation was performed. This review edited only its assigned file.

## Recommended state effect

**Revise the State Patch minimally, then apply its present one-child,
two-parent scope.**

Add these two rejected claims:

1. id:
   <code>Round164-unweighted-oscillation-is-necessary-for-literal-profile</code>;
   reason: the literal BV/triangle target is the weighted sum
   \(\sum_N\operatorname{osc}C_N V_N\); the unweighted sum is only the
   coefficient-uniform envelope under \(V_N\ll1\).
2. id:
   <code>Round164-additive-shift-modulus-is-the-rank-one-product-collar</code>;
   reason: taking moduli in the Fejer off-diagonal leaves the additive
   relation \(d'm'-dm=r\), whereas the accepted rank-one collar has the
   distinct multiplicative geometry
   \(\lvert s\ell-XQR\rvert\ll QRJ/L\); only their adverse positive power
   warning is comparable.

Then:

1. create only
   <code>M9-M2-hard-top-t1-residual-transport-fejer-energy-reduction</code>
   with the type, status, dependencies, empty implication/blocker lists,
   source card, and open next action already present;
2. update only
   <code>M9-M2-top-endpoint-signed-cone</code> and
   <code>M9-M2-top-endpoint-density-discrepancy-energy</code>, adding the
   child as a dependency and Round-164 artifacts as inconclusive evidence;
3. preserve both parent statements, statuses, blockers, and implication
   edges;
4. preserve every complete-residual, full-\(t=1\), remaining-channel,
   hard-TOP, smooth-packet, assembly, M9, bridge, target, and exponent
   status exactly as listed in <code>no_change</code>;
5. clean the two doubled \(\rho_N\) escapes in the kernel and ensure every
   positive-evidence path, including the conductor adjudication, exists
   before graph application; and
6. do not update the proof draft until the mechanically validated patch is
   applied after all required reviews are green.

The patch must not create a residual-target node, full-\(t=1\) theorem, or
short-shift theorem; remove any blocker; add an implication edge; or mutate
either global exponent. The next mathematical task remains precisely the
one-sided actual residual Fejer estimate (164.G4).
