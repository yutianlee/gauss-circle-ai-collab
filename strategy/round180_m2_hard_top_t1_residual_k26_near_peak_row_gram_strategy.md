# Round 180 strategy: K26 near-peak signed divisor-row Gram gate

## Frozen objective

Work on authoritative graph
e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4
and on no other owner. Put \(J=\sqrt X\), \(1\ll L\ll H\le J^{1/2}\),
\(R_0=\lceil L\rceil\), and let \(M\asymp L^2\) be the exact containing
interval cardinality from the accepted residual K26 kernel. Retain

\[
c_N^{\rm rem}
=\sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)\lambda_N(d),
\qquad z_N=c_N^{\rm rem}e(J\sqrt N).
\tag{180.1}
\]

The literal real coefficient \(\lambda_N(d)\) retains the selected/no-pair
residual selector, squarefree and coprimality projectors, both two-adic
branches, near-square divisor support, every Vaaler/profile factor, floor,
star, hard value, endpoint, transition, support birth/death, and full-line
zero extension.

For \(\epsilon\in\{0,1\}\), define the complete physical divisor rows

\[
R_{\epsilon,d}(\theta)
=\sum_{m\ge1}(-1)^{\epsilon m}\lambda_{dm}(d)
 e(J\sqrt{dm}+dm\theta),
\qquad
Z_\epsilon(\theta)=\sum_{d\ {\rm odd}}\chi_4(d)R_{\epsilon,d}(\theta).
\tag{180.2}
\]

For every integer \(|\nu|\le\lceil\sqrt L\rceil\), let

\[
I_\nu=
\left[\frac{\nu-1/2}{M},\frac{\nu+1/2}{M}\right)\pmod1
\tag{180.3}
\]

and define, with one outer real part and no rowwise modulus,

\[
\mathcal O_{\epsilon,\nu}
=2\Re\sum_{\substack{d<d'\\d,d'\ {\rm odd}}}
 \chi_4(d)\chi_4(d')
 \int_{I_\nu}R_{\epsilon,d}(\theta)
 \overline{R_{\epsilon,d'}(\theta)}\,d\theta.
\tag{180.4}
\]

The sole analytic target is

\[
\boxed{
 \frac12\sum_{\epsilon=0}^1\mathcal O_{\epsilon,\nu}
 \ll_\varepsilon LX^\varepsilon
 \quad\hbox{uniformly for }|\nu|\le\lceil\sqrt L\rceil.}
\tag{180.G}
\]

## Exact reduction to K26

The cell kernel is

\[
\int_{I_\nu}e((dm-d'm')\theta)\,d\theta
=e\!\left(\frac{\nu(dm-d'm')}{M}\right)
 \frac{\sin(\pi(dm-d'm')/M)}{\pi(dm-d'm')},
\tag{180.5}
\]

with value \(1/M\) at \(dm=d'm'\). The literal incidence ledger is to be
reverified in-round in the form

\[
\Lambda_2:=\sum_{d\ {\rm odd}}\sum_m|\lambda_{dm}(d)|^2
\ll_\varepsilon L^2X^\varepsilon,
\tag{180.6}
\]

and every row has \(O(L)\) possible cofactors. Hence the complete row
diagonal in one cell is at most

\[
 \frac{L}{M}\Lambda_2\ll_\varepsilon LX^\varepsilon.
\tag{180.7}
\]

Also

\[
F_M(\theta)\ll
\min\!\left(M,\frac1{M\|\theta\|^2}\right).
\tag{180.8}
\]

Thus the arcs \(M\|\theta\|\ge\sqrt L\) cost
\(O_\varepsilon(L^3X^\varepsilon)\) by Parseval, while (180.G) and
(180.7) give the same bound on the near cells after weighting by
\(F_M\ll M/(1+\nu^2)\). The accepted collective ordinary-zero restoration
and once-only short correction then reduce the K26 endpoint theorem

\[
Q_M^*\ll_\varepsilon L^3X^\varepsilon
\tag{180.9}
\]

to (180.G). Every implication in this paragraph is an in-round verification
gate; none is accepted merely because it appears in the strategy.

## Mechanism and capacity gate

The new variable is the exact near-peak cell centre \(\nu\), not the
exhausted stopped-scale index. The open object is the joint
\(\chi_4(d)\chi_4(d')\)-weighted off-row Gram form, with the square-root
phase and complete literal symbol retained before positivity.

The coefficient-uniform local-cell capacity is
\(L^2X^\varepsilon\), one factor \(L\) above (180.G); after the Fejér peak
height \(M\asymp L^2\), this is the inherited \(L^4X^\varepsilon\)
endpoint capacity. A valid proof must identify an exact contraction absent
from both the complex dechirped control and the real cosine-dechirped
control. Reality, support, energy, chirp geometry, row length, or
\(\chi_4\) modulation separately cannot supply the gain.

## Mandatory controls

1. Retain both parity branches, exact \(M\), the complete sinc kernel, and
   the product diagonal \(dm=d'm'\).
2. Retain one real part outside the complete row-pair sum; no modulus or
   positive row norm may precede the claimed \(L\)-saving.
3. Retain selected/no-pair, squarefree, coprimality, two-adic, profile,
   hard, endpoint, transition, and zero-extension fields.
4. Reprove the incidence-energy, row-length, diagonal, far-arc, wraparound,
   ordinary-zero, and short-correction seams with exact powers.
5. Test complex dechirped, real cosine-dechirped, arbitrary-real-sign,
   constant-character, erased-selector, all-\(1\bmod4\) no-pair, one-row,
   one-site, exact-collision, and hard-boundary controls.
6. Distinguish the physical row diagonal from a fixed dual diagonal and
   restore every cell and frequency before an owner implication.

## Forbidden restarts and stop rule

Stop at the first normalization, incidence, cell-cover, wraparound,
diagonal, ordinary-zero, endpoint, or restored-power failure. Stop if an
argument:

- uses realness alone or survives the cosine-dechirped control;
- takes a positive row, cell, mode, shift, or divisor norm before the gain;
- deletes exact or near product collisions;
- assumes \(d\mapsto d+2\) regularity without transporting selectors and
  endpoints;
- repeats the Round-162 product-collar positive closure, Round-164
  fixed-shift triangle, Round-165 minimal-scale/K17a reduction, Round-173
  tangent commutator, or Round-175 scale telescope;
- proves only an average in \(\nu\), one parity, smooth interiors, selected
  rows, or a shortened endpoint; or
- restores a local \(L^2\) or endpoint \(L^4\) capacity.

No in-round pivot to K17a, another hard-TOP channel, BAL, UNBAL, M1, GAR,
assembly, a bridge, or an exponent is authorized.

## Promotion and downstream scope

Promotion of (180.G) requires an exact proof, independent verification of
the reduction to (180.9), a literal selector/endpoint seam, a capacity and
false-control seam, a statement-only rederivation, and a mechanically valid
State Patch. A strict sector is useful only if it is owner-complete on its
stated atoms and its exact complement is retained.

Even a complete proof closes only K26 and, after a separate connector
review, the displayed residual scalar. It does not close full \(t=1\),
other hard-TOP channels, complete hard TOP, either BAL scope, UNBAL,
M9--M2, either direct M1 route or GAR, endpoint uniformity, M9, a bridge,
the quarter theorem, or an exponent.

Round 180 is 100% analytical/algebraic and 0% numerical. It must close
under exactly one label:

- literal_near_peak_row_gram_anticoncentration_target;
- strict_literal_row_gram_sector; or
- row_gram_offdiagonal_capacity_or_self_return_no_go.
