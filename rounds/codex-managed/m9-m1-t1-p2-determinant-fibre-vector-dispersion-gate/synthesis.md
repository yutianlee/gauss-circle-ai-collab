# Round 195 synthesis

## Outcome

Round 195 proves two exact target-safe sectors of the physical
lower-close/upper-far mask

\[
 P_2=\mathbf1_{\{|d-gm|\le D_L\}}
     \mathbf1_{\{|d'-gm'|>D_L\}},
 \qquad D_L=\lceil\sqrt L\rceil.
\]

First, the entire physical sector \(\kappa\ge D_L\) is safe.  Second, on
\(\kappa<D_L\), every fixed packet satisfying

\[
 \min(Y,D_L)\le H_B\mathfrak m\kappa
\]

is safe.  The union has outer contribution
\(O_{B,C_0,\varepsilon}(L^2X^\varepsilon)\).

## Decisive bounds

The large-\(\kappa\) physical count is

\[
 \sum_{\kappa\ge D_L}D_L(1+L/\kappa)^2
 \ll L^2+LD_L\log(2L)\ll L^2.
\]

For the small-\(\kappa\) complement, fixed-height and all-height counts
combine to give

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D}W)|
 \ll u\{\kappa+\min(Y,D_L)\}X^\varepsilon.
\]

The fixed-to-outer lift weight cancels the spectral
\(\mathfrak m\)-factor, and the accepted anchor, band, divisor, and shell
ledger restores \(L^2X^\varepsilon\).

## Exact remaining seam

The complete \(P_2\) estimate is not proved.  Its exact remaining packet
region is

\[
 \boxed{\kappa<D_L,\qquad
 \min(Y,D_L)>H_B\mathfrak m\kappa.}
\]

Within one primitive row, the far variable has only \(O(1)\) live samples.
The minus anchor factor is constant; the plus fixed-mode factor is
carry-dependent.  Correct same-site event recombination returns the
original masked jump, and coefficient-blind Gram bounds self-return to
positive capacity.  The next admissible theorem must estimate the actual
cross-row \(++,+-,-+,--\) Gram on the boxed region.

The blind squareful quadratic family is not live and supplies no lower
mass.  Live squarefreeness reduces fixed congruence fibres to
\(U^\varepsilon\) candidates, but that algebraic fact does not control the
anchor denominator or endpoint/radical correlations.

## Proof-state consequence

The durable kernel is
proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md
at SHA-256
4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009.

The State Patch may create only one subordinate proved-internal node and
update only the still-open hard-M1 high-radical small-\(t\) owner.  It does
not prove complete \(P_2\), \(P_1\), complete original \(t=1\), the hard-M1
owner, M9-M1, M9-M2, M9, either bridge, or the quarter theorem.

The strongest internal exponent remains \(1/3\).  The strongest accepted
global benchmark remains the external Li--Yang value
\(0.3144831759740614\ldots\).  No global exponent improves.

Round 195 closes under
strict_p2_absolute_capacity_sectors.
