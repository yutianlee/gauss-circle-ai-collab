# Hostile audit of signed adjacent-odd pairing on the high shell

- Campaign: m9-m1-top-block-signed-adjacent-odd-pairing
- Research round: 57 (signed_adjacent_odd_pairing)
- Task: adjacent_pairing_hostile_audit
- Role: seam_reviewer
- Graph SHA-256 supplied in the brief: a460b66b30b01db14bb52d3891875f7e1a97ba2f0c73b77557eef1d60b599c0a
- Status: candidate evidence only; no shared proof state was edited.

## 1. Result

**Adjacent-odd pairing does not prove the high-shell bound.** It is an
exact algebraic rewrite only on those fixed-\(h\) rows containing two odd
denominators. Because the two products are spaced by \(2h\in(R/2,R]\),
each row has at most two terms, but a length-\(R\) window can be aligned so
that every nonempty row has exactly one. Such rows have no adjacent partner,
and their inherited amplitude and phase survive unchanged.

More precisely, for a product window \(J=[A,B]\cap\mathbb Z\), set

\[
 Q_h=\{q\in2\mathbb Z+1:A\le hq\le B\}.
\tag{57.1}
\]

On \(R/4<h\le R/2\), \(Q_h\) contains zero, one, or two elements. If
\(Q_h=\{q,q+2\}\), its contribution is exactly

\[
 \chi_4(q)e(\sqrt{Xhq})
 \{\mathcal A_X(h,q)-
   \mathcal A_X(h,q+2)e(\Theta_h(q))\},
\tag{57.2}
\]

where

\[
 \Theta_h(q)=\frac{2\sqrt{Xh}}{\sqrt{q+2}+\sqrt q}.
\tag{57.3}
\]

If \(|Q_h|=1\), the row remains the original full or inherited-starred
term. There is no lawful cross-\(h\) pairing supplied by (57.2).

The sharp geometry obstruction is a point window \(J=\{N\}\), allowed by
\(|J|\le R\). Then every nonempty row is a singleton divisor incidence
\(hq=N\), so the adjacent-pair part is empty. The sum becomes

\[
 P_{\{N\}}=e(\sqrt{XN})
 \sum_{\substack{h\mid N,\ R/4<h\le R/2\\N/h\ {\rm odd}}}^{*}
 \chi_4(N/h)\mathcal A_X(h,N/h).
\tag{57.4}
\]

Thus the radial phase is common to every surviving \(h\); phase curvature
and adjacent-\(q\) sign reversal provide no cancellation at all. At
\(X=K^4\) and \(N=K^2\), the common phase is
\(e(K^3)=1\). This perfect-fourth-power control makes the failure of a
phase-only adjacent-pair argument exact.

This is a structural falsification of the proposed mechanism, not a lower
bound contradicting the desired theorem: divisor multiplicity makes a
point window at most \(X^{o(1)}\), already below the allowed
\(X^\varepsilon\sqrt R\). For long windows, the exact paired rows also
need not be small: the plateau may eliminate only the amplitude difference,
leaving \(\mathcal A(1-e(\Theta))\), which is order one whenever
\(\Theta\) stays away from integers; amplitude or height seams can instead
make the first difference order one. No aggregate theorem for those paired
differences or for the unmatched rows is present.

The lawful conclusion is therefore a narrow no-go: adjacent pairing alone
cannot close the target (57.6). No strict signed actual-profile lower bound of order
\(R\), and no target-sized \(O_\varepsilon(X^\varepsilon\sqrt R)\) bound,
is certified here.

## 2. Exact statement and hypotheses

Assume \(Y=R^2\asymp\sqrt X\),
\(J=[A,B]\cap\mathbb Z\subset[cY,CY]\), \(|J|\le R\), and
\(R/4<h\le R/2\). Retain the packet's exact amplitude

\[
 \mathcal A_X(h,q)=\Omega_X^*(hq,h)
 =\sum_j\mathbf1_{h\le H_j}
 \Phi\!\left(\frac h{H_j+1}\right)
 \left[w_j\!\left(2\sqrt{Xh/q}\right)\right]^*,
 \quad H_j=\lfloor D_jX^{-1/4}\rfloor,
\tag{57.5}
\]

including the hard top, every angular equality star, and the independent
radial star. The unweighted target is

\[
 |P_J|\ll_\varepsilon X^\varepsilon\sqrt R.
\tag{57.6}
\]

For each \(h\), define the exact ordered list
\(Q_h=\{q_1<\cdots<q_{r_h}\}\), where the \(q_i\) are odd and
\(hq_i\in J\). Since consecutive odd denominators differ by two,

\[
 h(q_{i+1}-q_i)=2h>R/2.
\]

Because the diameter \(B-A\le |J|-1<R\) for a nonempty consecutive
integer interval with \(|J|\le R\), one has \(r_h\le2\). Both terms occur
if and only if there is an odd \(q\) satisfying

\[
 A\le hq,qquad h(q+2)\le B,
\tag{57.7}
\]

or equivalently \(q\in[A/h,B/h-2]\). Otherwise a nonempty row is
unmatched. This condition, not the mere inequality \(2h\le R\), owns the
window alignment.

The exact row decomposition is

\[
 P_J=\sum_{h:r_h=2}P_h^{\rm pair}
      +\sum_{h:r_h=1}P_h^{\rm sing},
\tag{57.8}
\]

where \(P_h^{\rm pair}\) is (57.2) and

\[
 P_h^{\rm sing}=chi_4(q_h)\mathcal A_X(h,q_h)
 e(\sqrt{Xhq_h}),
\tag{57.9}
\]

with the inherited star multiplying its actual value. Artificial
window boundaries in (57.7) have full cutoff ownership; they acquire no
half weight.

## 3. Proof or derivation

For a two-term row \(Q_h=\{q,q+2\}\), use
\(\chi_4(q+2)=-\chi_4(q)\) and factor the first phase. This gives
(57.2), with (57.3) obtained by rationalizing the square-root difference.
Splitting the bracket yields the exact identity

\[
 \mathcal A(h,q)-\mathcal A(h,q+2)e(\Theta)
 =\{\mathcal A(h,q)-\mathcal A(h,q+2)\}
  +\mathcal A(h,q+2)\{1-e(\Theta)\}.
\tag{57.10}
\]

Neither term is automatically small. The profile report gives a genuine
top plateau \(W(t)=1\) for \(2/3\le t\le1\). When both samples stay in
one plateau and the same height factors remain active, the first brace can
vanish, but then the second has magnitude

\[
 2|\mathcal A(h,q+2)|\,|\sin(\pi\Theta_h(q))|,
\tag{57.11}
\]

which has no smallness unless \(\Theta_h(q)\) is proved close to an
integer. At a profile edge, height cutoff, or star equality, the first
brace can instead have constant size. Sampled BV controls the sum of
absolute differences along a row, but here there is only one difference;
it supplies an \(O(1)\) bound, not a power saving.

The exact phase increment has natural magnitude

\[
 \Theta_h(q)\asymp hR
\quad(hq\asymp R^2, X\asymp R^4),
\tag{57.12}
\]

because \(\sqrt q\asymp R/\sqrt h\). Its large real magnitude gives no
information about its fractional part, so sign reversal of \(\chi_4\)
cannot itself place it near an integer. At
\(X=K^4\), if \(h=a^2\) and \(q=b^2\) with odd \(b\), then the two-point
increment is

\[
 K^2a\{\sqrt{b^2+2}-b\},
\]

which is generally neither integral nor small. Conversely, exact integral
phase differences occur for more widely separated square denominators;
Round 56 records that such global coherence need not fit in a length-
\(R\) window. Both controls reject a universal phase-gap conclusion.

For the alignment obstruction, let \(J=\{N\}\). Then (57.7) is impossible
because its two products differ by \(2h>0\), hence every nonempty \(Q_h\)
is a singleton and (57.8) reduces to (57.4). Since \(hq=N\), the phase
\(e(\sqrt{Xhq})=e(\sqrt{XN})\) is independent of \(h\). Taking
\(X=K^4,N=K^2\) makes it one. The amplitude formula, floors, top edge, and
all stars remain present term by term; nothing was completed or altered.

For a general window, every two-term row consumes span \(2h>R/2\).
Shifting either endpoint by fewer than \(2h\) can create or destroy the
pair and replace it by a full unmatched term. Hence no uniform statement
that “almost all rows pair” follows from length alone. Moreover, a pairing
choice made separately for each \(h\) leaves the outer phases
\(e(\sqrt{Xhq_h})\) at unrelated products. Bounding their signed sum is a
new cross-\(h\) exponential/divisor problem, not a consequence of (57.10).

The exponent ledger is therefore unchanged. There are \(O(R)\) possible
\(h\)'s in the shell. Termwise control of either the paired bracket or an
unmatched row by \(O(1)\) gives \(O(R)\), while (57.6) requires
\(O(\sqrt R)\). Adjacent pairing supplies no theorem recovering that
missing factor \(\sqrt R\).

## 4. First doubtful or unproved step

The first unproved step in any positive adjacent-pair proof is a uniform
aggregate estimate for the exact decomposition (57.8). It must jointly
bound:

1. the unmatched signed sum (57.9), whose size is not controlled by the
   count of matched rows;
2. the amplitude-difference terms in (57.10), including height and profile
   seams;
3. the phase-difference terms (57.11), without assuming
   \(\Theta_h(q)\) is near an integer;
4. the remaining cross-\(h\) phases after each row is locally rewritten.

No such theorem is contained in the packet or accepted context. A bound
for local sampled BV, a top plateau, or the identity
\(\chi_4(q+2)=-\chi_4(q)\) proves none of these four assertions.

The point-window control shows that a proof whose only cancellation step
is adjacent-\(q\) pairing cannot be uniform in all allowed \(J\). It does
not falsify the target estimate itself because (57.4) is divisor-bounded.

## 5. Control tests and outcomes

- **pairing_identity -- pass with an unmatched remainder.** Equations
  (57.2), (57.8), and (57.9) are exact. Dropping the singleton sum is not.

- **two_point_window_geometry -- fail for universal pairing.** A row pairs
  exactly under (57.7). The allowed point window has no pair at all, and
  endpoint alignment can change a two-term row into a singleton.

- **phase_increment -- no automatic saving.** Formula (57.3) is exact.
  The phase bracket is governed by
  \(2|\sin(\pi\Theta)|\), not by the character sign alone.

- **amplitude_difference -- bounded but not small.** The plateau may make
  it zero, while profile, height, hard-top, or equality seams can make it
  order one. Sampled BV yields only constant control for the sole pair.

- **unmatched_endpoints -- fail for omission.** An artificial cutoff has
  full ownership. Only an inherited angular or radial equality retains its
  original star. The unmatched sum can contain \(O(R)\) candidate rows.

- **cross_h_aggregation -- open.** On a point window every phase is common;
  on a general window the paired-row base phases vary with \(h\). Neither
  case is bounded at target size by the pairing identity.

- **perfect_fourth_power -- phase coherence survives.** For
  \(X=K^4,N=K^2\), (57.4) has common phase one. For actual adjacent pairs,
  fourth-power structure does not universally force \(\Theta\) near an
  integer. Thus neither coherence nor nonresonance closes the sum.

- **target_ledger -- fail/open.** Absolute row accounting gives \(O(R)\);
  the target is \(O_\varepsilon(X^\varepsilon\sqrt R)\). The missing
  \(\sqrt R\) must come from a new signed cross-\(h\)/product theorem.

- **lower_shell_scope -- untouched.** Round 57 owns only
  \(R/4<h\le R/2\). The sector \((\log X)^B<h\le R/4\) remains open.

- **downstream_scope -- no implication.** The result does not prove the
  high-shell estimate, the residual core, GAR, alpha transfer, M9-M1, M9,
  or a Gauss-circle exponent.

No numerical, symbolic, web, or unlisted-source experiment was used.

## 6. Dependencies and exact artifacts used

This report used only the brief and its permitted selected context:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-top-block-signed-adjacent-odd-pairing/derivation_packet.md;
- rounds/codex-managed/m9-m1-top-block-intermediate-h-resonance/synthesis.md;
- rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md;
- the Round-57 hostile-audit brief.

The imported facts were the exact high-shell object and amplitude, the
Round-56 singleton/resonance obstruction, the explicit profile partition
and top plateau, height rounding, normalized BV, and endpoint ownership.
The matched/unmatched decomposition, alignment obstruction, point-window
common-phase test, paired-bracket audit, and exponent ledger were derived
directly. No other Round-57 report, proof draft, legacy artifact, or
external theorem was read.

## 7. Recommended state effect

**Reject adjacent-odd pairing as a standalone proof of the high-shell
estimate.** Promote only the exact reduction (57.7)--(57.10) together with
the following method obstruction:

1. each fixed-\(h\) row has at most two terms, but a pair exists only under
   the exact alignment condition (57.7);
2. unmatched rows retain full/inherited-starred ownership and cannot be
   dropped or assigned artificial half weights;
3. on the top plateau, amplitude equality leaves the unsaved phase factor
   \(1-e(\Theta)\); at seams the amplitude difference itself can be order
   one;
4. point windows have no adjacent pairs and reduce to the original signed
   divisor sum with a common radial phase, exactly one at
   \(X=K^4,N=K^2\);
5. local pairing supplies no \(\sqrt R\) gain in the outer \(h\)-sum.

Do not promote a signed lower bound from the point-window control or from
plateau rows: neither is shown to have more than divisor-sized coherent
mass. Keep the high-shell bound, the lower shell, residual core, GAR,
alpha transfer, M9-M1, M9, and the Gauss-circle target open.
