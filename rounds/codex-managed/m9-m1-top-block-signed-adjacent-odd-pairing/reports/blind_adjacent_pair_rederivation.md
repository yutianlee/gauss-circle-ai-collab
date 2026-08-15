# Blind rederivation: adjacent odd pairing on the high shell

## 1. Result

**Exact pairing lemma with an aggregate-capacity no-go.** For every
integer \(h\) with

\[
 {R\over4}<h\le {R\over2},
\]

the product window contains zero, one, or two odd denominators. If it
contains two, they are a unique adjacent pair \(q_h,q_h+2\). Hence

\[
\begin{aligned}
 P_J={}&
 \sum_{h\in\mathscr H_2}
 \chi_4(q_h)e(\sqrt{Xhq_h})
 \left\{\mathcal A_X(h,q_h)
 -\mathcal A_X(h,q_h+2)e(\Theta_h(q_h))\right\}\\
 &+\sum_{h\in\mathscr H_1}
 \chi_4(q_h)\mathcal A_X(h,q_h)e(\sqrt{Xhq_h}),              \tag{1}
\end{aligned}
\]

where \(\mathscr H_s\) is the set of rows containing exactly \(s\) odd
products and

\[
 \Theta_h(q)={2\sqrt{Xh}\over\sqrt{q+2}+\sqrt q}.             \tag{2}
\]

All values in (1) are the exact inherited full or starred values. The
cutoffs \(A,B\) create no new half-weights.

The matched row has the exact decomposition

\[
\begin{aligned}
 &\mathcal A_X(h,q)-\mathcal A_X(h,q+2)e(\Theta_h(q))\\
 &\qquad=
 \{\mathcal A_X(h,q)-\mathcal A_X(h,q+2)\}
 +\mathcal A_X(h,q+2)\{1-e(\Theta_h(q))\}.                   \tag{3}
\end{aligned}
\]

The adjacent-character identity alone has unweighted capacity \(R\), not
\(\sqrt R\). More precisely, if the fixed-row sampled-BV bound gives
\(\sup|\mathcal A_X|\ll_\varepsilon X^\varepsilon\), then the three
termwise-absolute ledgers

\[
\begin{aligned}
 E_{\rm amp}&=\sum_{h\in\mathscr H_2}
 |\mathcal A_X(h,q_h)-\mathcal A_X(h,q_h+2)|,\\
 E_{\rm ph}&=\sum_{h\in\mathscr H_2}
 |\mathcal A_X(h,q_h+2)|\,|1-e(\Theta_h(q_h))|,\\
 E_{\rm end}&=\sum_{h\in\mathscr H_1}
 |\mathcal A_X(h,q_h)|
\end{aligned}                                                \tag{4}
\]

satisfy only

\[
 E_{\rm amp}+E_{\rm ph}+E_{\rm end}
 \ll_\varepsilon X^\varepsilon R.                           \tag{5}
\]

The target requires the right side of (5) to be
\(O_\varepsilon(X^\varepsilon\sqrt R)\), or it requires cancellation
between the signed rows before these absolute values are taken. Neither
the row geometry, fixed-\(h\) sampled BV, nor
\(\chi_4(q+2)=-\chi_4(q)\) supplies that missing factor.

At \(X=K^4\), exact integral and half-integral values of
\(\Theta_h(q)\) are in fact impossible for positive integral \(h\) and
odd \(q\). Nonetheless there are admissible paired rows for which
\(\Theta_h(q)\) stays bounded away from the integers and approaches a
half-integer. Thus character sign reversal can give near-maximal
reinforcement rather than cancellation. A complete result would need a
new signed cross-\(h\) theorem for (1), together with a separate
\(O(\sqrt R)\) treatment of \(\mathscr H_1\).

## 2. Exact statement and hypotheses

Write

\[
 J=[A,B]\cap\mathbb Z,\qquad B-A+1\le R.
\]

For an integer \(h\) in the owned shell define

\[
 a_h=\left\lceil {A\over h}\right\rceil,\qquad
 b_h=\left\lfloor {B\over h}\right\rfloor,\qquad
 \mathcal Q_h=\{q\in[a_h,b_h]\cap\mathbb Z:q\ {\rm odd}\}.   \tag{6}
\]

The exact row cardinality is

\[
 \nu_h=|\mathcal Q_h|
 =\max\!\left(0,
 \left\lfloor{b_h+1\over2}\right\rfloor
 -\left\lfloor{a_h\over2}\right\rfloor\right).               \tag{7}
\]

Set

\[
 \mathscr H_s=\{h:R/4<h\le R/2,\ \nu_h=s\}
 \quad(s=0,1,2).
\]

For \(h\in\mathscr H_1\), \(q_h\) denotes the sole member of
\(\mathcal Q_h\). For \(h\in\mathscr H_2\), it denotes the smaller member.
The exact stars in (57.2) are understood inside the displayed
\(\mathcal A_X(h,q)\) values in (1)--(4), exactly once. If a product equals
an inherited radial or angular equality location, its prescribed starred
value is used. If a product merely equals the artificial edge \(A\) or
\(B\), it has full cutoff ownership.

No global BV or Lipschitz control in \(h\) is assumed. The only amplitude
information stated in the packet is the fixed-\(h\), physical-window
sampled-BV theorem. It implies the rowwise estimates

\[
 \sup_{q\in\mathcal Q_h}|\mathcal A_X(h,q)|
 +\sum_{\substack{q,q+2\in\mathcal Q_h}}
 |\mathcal A_X(h,q+2)-\mathcal A_X(h,q)|
 \ll_\varepsilon X^\varepsilon,                             \tag{8}
\]

but because there is at most one difference in a high-shell row, (8)
does not provide a negative power of \(R\).

For later reference, the exact positive condition sufficient for the
target after applying (3) termwise is

\[
 E_{\rm amp}+E_{\rm ph}+E_{\rm end}
 \ll_\varepsilon X^\varepsilon\sqrt R.                       \tag{9}
\]

Condition (9) is stronger than necessary: the project needs the signed
sum (1), so cancellation among its rows may prove the target without
proving (9).

## 3. Proof and independent pairing ledger

### Two-point window geometry and endpoints

Three odd denominators in one row would be \(q,q+2,q+4\), whose extreme
products differ by \(4h>R\). But

\[
 B-A=|J|-1\le R-1.
\]

Therefore \(\nu_h\le2\). If \(\nu_h=2\), the two odd integers must be
consecutive in the odd lattice and hence are \(q_h,q_h+2\). This proves
the uniqueness asserted in (1). It also proves that every unmatched row
is an actual one-point window incidence, not half of an artificially
completed pair.

The criterion for a matched row is exactly

\[
 A\le hq_h,\qquad h(q_h+2)\le B,                             \tag{10}
\]

with \(q_h\) odd. A pair spans \(2h\in(R/2,R]\), so (10) depends on the
alignment of the two hyperbola samples with both window edges. Appending
a zero outside \(J\) is a possible algebraic notation, but that zero is an
artificial full cutoff value and acquires no star. Formula (7), rather
than an assumption that every row pairs, is the exact endpoint ledger.

There are at most

\[
 \#\{h:R/4<h\le R/2\}\le R/4+1                              \tag{11}
\]

rows and at most twice as many incidences. This gives the \(O(R)\) upper
capacity in (5). It is also the correct geometric scale: for a
full-cardinality window \(|J|=R\), every
\(h\le(R-1)/2\) has

\[
 {B-A\over h}\ge2,
\]

so its real \(q\)-interval contains at least one odd integer. Thus
\(\gg R\) high-shell rows may be occupied. Geometry alone cannot replace
the \(O(R)\) count by \(O(\sqrt R)\); it also does not force the unmatched
subset itself to be small.

### Pairing identity and phase increment

For a matched row, (57.4) gives

\[
\begin{aligned}
 &\chi_4(q)\mathcal A_X(h,q)e(\sqrt{Xhq})\\
 &\quad+\chi_4(q+2)\mathcal A_X(h,q+2)
 e(\sqrt{Xh(q+2)})\\
 &=\chi_4(q)e(\sqrt{Xhq})
 \left\{\mathcal A_X(h,q)
 -\mathcal A_X(h,q+2)e(\Theta_h(q))\right\},
\end{aligned}
\]

which proves (1). Rationalizing the square-root difference gives (2).
The universal phase-factor identity is

\[
 |1-e(\Theta)|=2|\sin(\pi\Theta)|
 \le \min(2,2\pi\|\Theta\|).                                \tag{12}
\]

Accordingly:

- if \(\Theta\in\mathbb Z\), the phase part of (3) vanishes;
- if \(\Theta\in\mathbb Z+\tfrac12\), it has the maximal multiplier \(2\);
- if \(\|\Theta\|\ge\delta\) and
  \(\|\Theta\|\le1/2\), its multiplier is at least
  \(2\sin(\pi\delta)\).

Thus sign reversal is useful only near an integer phase increment. It is
maximally adverse near a half-integer.

### Actual amplitude difference

Equation (3) retains the actual finite difference with every profile,
height floor, hard-top value, and equality star attached to its own
sample. On a top-profile plateau it may vanish exactly. At a profile,
effective-height, hard, or equality edge it may instead be of the same
order as the amplitude. The rowwise theorem (8) bounds both cases, but
does not distinguish them quantitatively because only one adjacent pair
is present.

A local interior estimate of size \(O(R^{-1})\), which would make
\(E_{\rm amp}\) target-safe, would require a normalized local derivative
bound for the exact profile formula plus a count of every exceptional
edge row. Neither such local modulus nor such a cross-\(h\) edge count is
stated in the permitted packet. It therefore cannot be inferred from
sampled BV. Even granting this ideal amplitude gain, \(E_{\rm ph}\) and
\(E_{\rm end}\) retain \(O(R)\) capacity.

### Cross-\(h\) aggregation

The exact matched-row base phase is

\[
 \Psi_h=\sqrt{Xh q_h},
\]

where \(q_h\) is selected by the floor and parity conditions (6)--(10).
As \(h\) changes, \(q_h\) is a discontinuous hyperbola-floor function.
The coefficient in braces in (1) also contains the actual \(h\)-dependent
height floors and profile edges. Fixed-\(h\) sampled BV gives no
regularity for either object across \(h\).

Consequently the target-capable interface is a signed theorem of the form

\[
\begin{aligned}
 \bigg|&
 \sum_{h\in\mathscr H_2}
 \chi_4(q_h)e(\Psi_h)
 \{\mathcal A_X(h,q_h)
 -\mathcal A_X(h,q_h+2)e(\Theta_h(q_h))\}\\
 &+\sum_{h\in\mathscr H_1}
 \chi_4(q_h)\mathcal A_X(h,q_h)e(\Psi_h)
 \bigg|
 \ll_\varepsilon X^\varepsilon\sqrt R.                      \tag{13}
\end{aligned}
\]

This is no stronger than the desired estimate on the owned shell, but it
makes clear that adjacent pairing has not proved it. A theorem only for
the matched sum is insufficient unless the unmatched sum is separately
\(O_\varepsilon(X^\varepsilon\sqrt R)\).

### Perfect-fourth-power resonance

Let \(X=K^4\) and \(R=K\). Then

\[
 \Theta_h(q)=K^2\{\sqrt{h(q+2)}-\sqrt{hq}\}.                 \tag{14}
\]

This number is never integral or half-integral. Indeed, if it were in
\(\tfrac12\mathbb Z\), then
\(r=\sqrt{h(q+2)}-\sqrt{hq}\) would be rational. Since

\[
 \sqrt{h(q+2)}+\sqrt{hq}={2h\over r},
\]

both square roots would be rational and hence integral. Thus both
\(hq\) and \(h(q+2)\) would be squares. Their quotient forces \(q\) and
\(q+2\) to have the same squarefree part \(d\), so

\[
 q=da^2,\qquad q+2=db^2,\qquad d(b^2-a^2)=2.
\]

Because \(q\) is odd, \(d\) is odd; hence \(d=1\), but two squares cannot
differ by \(2\). This is a contradiction. The mandatory exact
integer/half-integer cases are therefore empty at a perfect fourth power,
although arbitrarily close resonance is not excluded.

There are explicit admissible bounded-away alignments. Take

\[
 K=18t+9,\qquad h={K\over3},\qquad q=3K,
\]

and
\[
 J=[K^2,K^2+2K/3]\cap\mathbb Z.
\]

Then \(q\) is odd, \(K/4<h<K/2\), both products lie in \(J\),
\(|J|=2K/3+1\le K\), and all support inequalities in the packet are
strict. Taylor expansion gives

\[
\begin{aligned}
 \Theta_h(q)
 &=K^2\{\sqrt{K^2+2K/3}-K\}\\
 &={K^2\over3}-{K\over18}+{1\over54}+O(K^{-1})
 \equiv {14\over27}+O(K^{-1})\pmod1.                        \tag{15}
\end{aligned}
\]

Thus \(|1-e(\Theta_h(q))|\) approaches
\(|1-e(14/27)|\), which is close to its maximal value \(2\).
If this row lies on a nonzero amplitude plateau, the amplitude difference
in (3) is zero and the phase part reinforces almost maximally. The packet
does not state enough nonvanishing data to promote that conditional
observation to an actual-profile lower-bound family.

The base radial phase has its own perfect-fourth coherence. Writing
\(n=K^2+t\),

\[
 K^2\sqrt{K^2+t}
 =K^3+{K\over2}t-{t^2\over8K}+O(t^3/K^3).                  \tag{16}
\]

For even \(K\), the linear term is integral for every integer \(t\); for
odd \(K\), it is integral or half-integral according to parity. Therefore
no first-derivative gap across the \(h\)-rows may be assumed. A possible
quadratic square-root aggregate estimate would have to be proved with the
actual selected products \(hq_h\), amplitudes, and endpoint rows.

### Target exponent ledger

The unweighted ledgers are

| Contribution | Available absolute capacity | Required capacity |
|---|---:|---:|
| matched amplitude differences | \(X^\varepsilon R\) | \(X^\varepsilon\sqrt R\) |
| matched phase increments | \(X^\varepsilon R\) | \(X^\varepsilon\sqrt R\) |
| unmatched rows | \(X^\varepsilon R\) | \(X^\varepsilon\sqrt R\) |
| full signed shell | \(X^\varepsilon R\) by triangle inequality | \(X^\varepsilon\sqrt R\) |

Restoring \((hq)^{-3/4}\asymp R^{-3/2}\), the absolute result is only

\[
 X^\varepsilon R^{-1/2},
\]

whereas the normalized target is

\[
 X^\varepsilon R^{-1}=X^\varepsilon Y^{-1/2}.                \tag{17}
\]

The exact missing factor is \(\sqrt R\).

## 4. First doubtful or unproved step

The pairing identity, two-point geometry, endpoint decomposition, and
phase formulas are exact. The first estimate unavailable from the packet
is a local power-saving bound for the actual amplitude difference on each
matched row, including a proof that profile, effective-height, hard, and
equality edge rows have aggregate \(O(\sqrt R)\).

Even if that input is granted, the first decisive unproved step is the
signed cross-\(h\) estimate (13). The phase factor in (3) is not uniformly
small, as (15) demonstrates, and no hypothesis bounds
\(\#\mathscr H_1\) by \(O(\sqrt R)\). The packet gives neither global
amplitude regularity in \(h\) nor a theorem for the discontinuously
selected phases \(\Psi_h\). Adjacent pairing therefore does not close the
high shell.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| pairing_identity | **Pass.** Formula (1) follows exactly from the unique two-point rows and \(\chi_4(q+2)=-\chi_4(q)\). |
| two_point_window_geometry | **Pass.** Equations (6)--(11) prove \(\nu_h\le2\), state the exact alignment criterion, and retain zero-, one-, and two-point rows. |
| phase_increment | **Pass.** Equations (2), (12), and (14)--(15) distinguish near-integer cancellation from near-half-integer reinforcement. |
| amplitude_difference | **No automatic gain.** Formula (3) is exact; fixed-row sampled BV permits an order-one difference, and the missing local/exceptional-edge theorem is explicit. |
| unmatched_endpoints | **Open at target size.** Every unmatched incidence retains its full or inherited-starred value. Geometry permits \(O(R)\) rows and supplies no \(O(\sqrt R)\) bound. |
| cross_h_aggregation | **Open.** The exact required signed interface is (13); floor/parity selection and actual height/profile dependence prevent an unproved smooth-\(h\) argument. |
| perfect_fourth_power | **Pass.** Exact integral/half-integral \(\Theta\) values are impossible, the bounded-away family (15) is explicit, and the radial linear coherence (16) is recorded. |
| target_ledger | **No-go passed.** Triangle closure gives normalized \(R^{-1/2}\), losing \(\sqrt R\) against \(R^{-1}\). |
| lower_shell_scope | **Pass.** Only \(R/4<h\le R/2\) is owned. The sector \((\log X)^B<h\le R/4\) remains open. |
| downstream_scope | **Pass.** No alpha transfer, full shifted correlation, GAR, outside-height theorem, M9-M1, M9, or final target is inferred. |

## 6. Dependencies, exact artifacts, and isolation ledger

Dependencies used:

1. The high-shell object, exact amplitude convention, target, support
   conditions, and adjacent-character identity in the Round-57 packet.
2. The packet-stated fixed-\(h\) sampled-BV input, used only in its
   rowwise form (8).
3. Elementary odd-lattice geometry, exact square-root algebra, and Taylor
   expansion, all derived above.

Isolation ledger:

- Read
  rounds/codex-managed/m9-m1-top-block-signed-adjacent-odd-pairing/briefs/blind_adjacent_pair_rederivation.md.
- Read
  rounds/codex-managed/m9-m1-top-block-signed-adjacent-odd-pairing/derivation_packet.md.
- Did not read the proof graph, proof draft, prior reports or syntheses,
  validation matrices, or any other Round-57 artifact.
- Used no web source, external paper, numerical experiment, Python, or
  Mathematica.
- Wrote only this assigned report and made no shared proof-state edit.

## 7. Recommended state effect

**Retain the exact pairing decomposition; reject adjacent pairing alone as
a target-closing mechanism.** Promote after seam review formulas
(1)--(3), the exact row/endpoints ledger (6)--(11), the
perfect-fourth-power controls (14)--(16), and the \(\sqrt R\) capacity
gap. Retain as open the actual-amplitude local edge theorem, the unmatched
endpoint sum, and the signed cross-\(h\) interface (13). Do not promote an
actual-profile counterexample or any lower-shell or downstream conclusion.
