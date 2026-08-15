# Round 57 conductor adjudication: local character pairing is not the missing square root

## 1. Decision

Promote the exact matched/unmatched adjacent-odd decomposition and a scoped
method obstruction.  Do not promote the high-shell estimate.  The three
reports independently agree that \(\chi_4(q+2)=-\chi_4(q)\) turns a
two-point row into a genuine difference, but neither the phase difference
nor the unmatched rows acquire a power saving.  The discovery report
additionally gives a strict actual-profile family with \(\gg R\) unmatched
mass after absolute values.

## 2. Exact finite decomposition

For \(J=[A,B]\cap\mathbb Z\), \(|J|\le R\), and
\(R/4<h\le R/2\), put

\[
 \mathcal Q_h(J)=\{q\ge1:q\ \text{odd},\ hq\in J\}.
\]

Because three odd denominators span product distance \(4h>R\), every row
has cardinality zero, one, or two.  A two-point row is uniquely
\(\{q_h,q_h+2\}\), and exists exactly when

\[
 A\le hq_h,\qquad h(q_h+2)\le B.
\tag{57.1}
\]

Writing \(\mathscr H_s=\{h:|\mathcal Q_h|=s\}\), the exact sum is

\[
\begin{aligned}
 P_J={}&\sum_{h\in\mathscr H_2}\chi_4(q_h)e(\sqrt{Xhq_h})
 \left\{\mathcal A_X(h,q_h)
 -\mathcal A_X(h,q_h+2)e(\Theta_h(q_h))\right\}\\
 &+\sum_{h\in\mathscr H_1}\chi_4(q_h)\mathcal A_X(h,q_h)
 e(\sqrt{Xhq_h}),
\end{aligned}
\tag{57.2}
\]

where

\[
 \Theta_h(q)={2\sqrt{Xh}\over\sqrt{q+2}+\sqrt q}\asymp hR
\tag{57.3}
\]

on \(hq\asymp R^2\), \(X\asymp R^4\).  Artificial window edges are
full owners; only inherited angular or radial equalities retain stars.

## 3. What the pairing actually saves

The paired bracket is

\[
 \{\mathcal A(h,q)-\mathcal A(h,q+2)\}
 +\mathcal A(h,q+2)\{1-e(\Theta_h(q))\}.
\tag{57.4}
\]

On smooth profile pieces the discovery report proves

\[
 |\mathcal A(h,q+2)-\mathcal A(h,q)|\ll h/R^2,
\]

so its total over the shell is \(O(1)\).  Hard-profile, equality-star,
or cutoff seams retain their explicit bounded jumps.  The top plateau can
make the amplitude difference exactly zero, but then the remaining factor
has size \(2|\sin(\pi\Theta_h(q))|\), which need not be small.  The blind
control supplies admissible fourth-power rows with \(\Theta\) bounded
away from the integers.  Thus character reversal is not itself phase
cancellation.

## 4. Sharp unmatched-row obstruction

For infinitely many \(X=K^4\), set \(R=K\) and use a length-\(K\)
window selected by averaging its starting point near \(K^2\).  For

\[
 3K/8\le h\le7K/16,
\]

the odd products have spacing \(2h\in[3K/4,7K/8]\).  An exact residue
count shows that a positive proportion of these rows contains one point,
not two.  The selected products satisfy

\[
 {2h\over\sqrt{hq}}\Subset(2/3,1),
\]

so they lie strictly on the actual top plateau, have
\(H_0=K>h\), Vaaler weight at least \(1/2\), and avoid every hard,
angular, product, and radial star.  Consequently

\[
 \sum_{h\in\mathscr H_1}|\mathcal A_X(h,q_h)|\gg R.
\tag{57.5}
\]

This proves that endpoint counting and every post-pair absolute-value
closure miss the \(\sqrt R\) target by \(\sqrt R\).  It is not a signed
lower bound: the surviving cross-\(h\) sum may still cancel.

## 5. Exact survivor and exponent ledger

The smooth amplitude-difference term is target-safe.  The remaining
high-shell problem is the signed combination in (57.2), equivalently the
matched phase brackets, explicit seam rows, and unmatched singleton rows
kept together across \(h\).  Triangle inequality gives \(R\); the required
unweighted bound is \(X^\varepsilon\sqrt R\).  After restoring
\((hq)^{-3/4}\asymp R^{-3/2}\), this is exactly the missing normalized
factor \(R^{-1/2}=X^{-1/8}\).

A point window gives a useful structural control: it contains no adjacent
pair and all divisor incidences have one common radial phase (equal to one
at \(X=K^4,n=K^2\)).  Its divisor-sized mass does not violate the target,
but it proves that a uniform argument cannot use adjacent pairing as its
only cancellation mechanism.

## 6. Controls and evidence

- Discovery and strict actual-profile unmatched witness:
  `reports/adjacent_odd_pairing_attack.md`.
- Clean statement-only rederivation, exact row formula, and fourth-power
  phase control: `reports/blind_adjacent_pair_rederivation.md`.
- Independent hostile endpoint and common-phase audit, corrected to the
  phase scale \(\Theta\asymp hR\):
  `reports/adjacent_pairing_hostile_audit.md`.
- Every report has the required seven sections and passed byte/TeX hygiene.
- Work was 100% analytical/algebraic and used no numerical experiment or
  external theorem.

## 7. State recommendation

Create one proved obstruction/reduction node containing (57.1)--(57.5).
Add it as evidence under the global angular-radial estimate.  Reject the
claims that all high rows pair, that character sign reversal makes the
paired phase small, or that unmatched rows are automatically
\(O(\sqrt R)\).  Retain the signed high-shell sum, the lower sector
\((\log X)^B<h\le R/4\), alpha transfer, M9-M1, M9, and the target open.

