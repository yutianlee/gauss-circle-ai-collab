# Round 159 conductor adjudication

- Campaign: `m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate`
- Round: 159
- Starting graph: `8a0f917fb8117e9dbaf287d9f773046ff201729d2d8d8c3df1a51bca7815574b`
- Terminal label: `paired_interior_abel_commutator_no_go`
- Allocation: 100% analytical, algebraic, and primary-source work; 0% numerical

## 1. Result

Round 159 closes under **`paired_interior_abel_commutator_no_go`**, in a
strictly route-scoped sense.  The round proves a useful structural
correction: the two Abel outer terms, the two moving terms, and the two
profile-difference terms are not six independent analytic obligations.
For every divisor and frequency they telescope back to the original
positive and negative rows.  Recombining them before estimation and then
performing complete frequency inversion restores exactly the common
quotient-profile nearest-square defect wave already accepted in Round 154.

Thus the full paired-interior (D=d=L=1) matrix has no residual Abel seam.
After the already safe whole zero and Nyquist rows are removed once, its
first open estimate is the same signed common-profile hard defect wave that
was open before the trace decomposition.  The isolated Round-158 moving
trace still has its two distinct boundary-frozen profiles and remains a
correct identity; it simply need not be estimated separately in a proof
that first recombines all six Abel lines.

No target estimate and no strict owner-complete range beyond the accepted
fixed-polylogarithmic collar is proved.  The internally proved global
exponent remains (1/3), and the audited external Li--Yang exponent remains
((3292+25\sqrt{1717})/13762).

## 2. Exact accepted statement and hypotheses

Fix (A>0), set (N=\lfloor X\rfloor), and put

\[
 q=4N,\qquad K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\le K,\qquad M\le N^{1/2}.
\tag{159.A1}
\]

For each odd (d\mid N), let (c=q/d), (H=c/2), and (n=H/2=N/d).
Retain the inherited complete nonwrapping physical lift and

\[
 B_j(x)=\mathbf1_{x\ge1}\mathbf1_{-x\le j\le x-1}
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right),
\tag{159.A2}
\]

including every zero-extended component, transition, half-open convention,
hard endpoint, and the complex phase.  Put

\[
 a=\lfloor V\rfloor+1,\qquad b=\lfloor2V\rfloor,
\tag{159.A3}
\]

and define empty reversed sums to be zero.  With

\[
 P^+(j)=\sum_{s=a}^{j}K(-v^2,-s;c),\qquad
 P^-(j)=\sum_{s=j}^{-a}K(-v^2,-s;c),
\tag{159.A4}
\]

finite Abel summation gives the exact identities

\[
\begin{aligned}
 \sum_{j=a}^{b}\widehat B_j(2dv)K(-v^2,-j;c)
 ={}&\widehat B_b(2dv)P^+(b)\\
 &+\sum_{j=a}^{b-1}P^+(j)\widehat T_j^+(2dv)
 +\sum_{j=a}^{b-1}P^+(j)\widehat R_j^+(2dv),\\
 \sum_{j=-b}^{-a}\widehat B_j(2dv)K(-v^2,-j;c)
 ={}&\widehat B_{-b}(2dv)P^-(-b)\\
 &+\sum_{j=-b+1}^{-a}P^-(j)\widehat T_j^-(2dv)
 +\sum_{j=-b+1}^{-a}P^-(j)\widehat R_j^-(2dv),
\end{aligned}
\tag{159.A5}
\]

where

\[
\begin{aligned}
 T_j^+(x)&=\mathbf1_{x=j+1}F_j(x),&
 R_j^+(x)&=\mathbf1_{x\ge j+2}(F_j(x)-F_{j+1}(x)),\\
 T_j^-(x)&=\mathbf1_{x=-j}F_j(x),&
 R_j^-(x)&=\mathbf1_{x\ge-j+1}(F_j(x)-F_{j-1}(x)).
\end{aligned}
\tag{159.A6}
\]

Both moving atoms have positive sign.  The outer endpoints are (b) and
(-b).  Singleton blocks reduce to their outer term, and zero extension
keeps all profile births, deaths, and transitions inside (159.A5).

The accepted half-period inverse identity, its exterior theta factor, and
(dc=q) leave exactly (-i\chi_4(d)/(2N)).  The map (h=du\pmod q), with
(d=(h,N)), partitions the odd residues and restores

\[
 G_N(t)=\mathbf1_{N\mid t}\chi_4(t/N).
\tag{159.A7}
\]

Consequently the complete six-line paired-interior package is

\[
 \boxed{
 \mathcal T_{\mathrm{int},U}(V)
 =\mathcal S_U(V)-\mathcal Z_U(V)-\mathcal F_U(V),}
\tag{159.A8}
\]

where the two special terms are the **whole** zero and Nyquist rows and

\[
 \mathcal S_U(V)=
 \sum_{V<|j|\le2V}\sum_{x\in\mathcal L_U}
 B_j(x)G_N(x^2-j).
\tag{159.A9}
\]

They are removed exactly once, and

\[
 |\mathcal Z_U(V)|+|\mathcal F_U(V)|
 \ll_\varepsilon M^{-1/4}X^\varepsilon.
\tag{159.A10}
\]

The physical cells

\[
 x^2-x+1\le N\ell\le x^2+x
\tag{159.A11}
\]

partition the positive integers.  Fixed-dilation support and the inherited
lift compatibility put the unique root hull inside one physical lift.  With

\[
 \kappa(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,
 \qquad r(\ell)=\kappa(\ell)^2-N\ell,
\tag{159.A12}
\]

equation (159.A9) becomes exactly

\[
 \boxed{
 \mathcal S_U(V)=
 \sum_{\ell\ge1}\chi_4(\ell)w_U(\ell)e(\sqrt{N\ell})
 \mathbf1_{V<|r(\ell)|\le2V}.}
\tag{159.A13}
\]

Using the inherited identity (w_U(\ell)=\ell^{-3/4}A_U(\ell)), this is
the accepted Round-154 hard dyadic common-profile block, not a new analytic
object.

## 3. Analytic and source adjudication

Write (w_U=M^{-3/4}\widetilde w_U), with

\[
 \|\widetilde w_U\|_\infty+
 \operatorname {Var}(\widetilde w_U)\ll_\varepsilon X^\varepsilon.
\tag{159.A14}
\]

The desired scalar estimate is (O_\varepsilon(X^\varepsilon)), equivalently

\[
 \left|\sum_{\ell\asymp M}\chi_4(\ell)\widetilde w_U(\ell)
 e(\sqrt{N\ell})\mathbf1_{V<|r(\ell)|\le2V}\right|
 \ll_\varepsilon M^{3/4}X^\varepsilon.
\tag{159.A15}
\]

This estimate is unproved.  The support bound
(O_\varepsilon(\min(M,V)X^\varepsilon)) is unsigned.

For (delta=\sqrt{N\ell}-\kappa(\ell)), one has exactly

\[
 r=-\delta(2\kappa+\delta).
\tag{159.A16}
\]

The two branches have four (\kappa)-dependent endpoints, the (V)-edge
strict and the (2V)-edge closed, with clipping at the open centered
half-cell.  Hence the mask is not a fixed fractional interval.

The shifted Fourier exceptional mode is (h=-1), not (h=0).  Its
square-root phase disappears but (chi_4) remains.  The exact coefficient
has bounded variation, so character Abel summation gives raw
(O_\varepsilon(X^\varepsilon)), hence normalized
(O_\varepsilon(M^{-3/4}X^\varepsilon)).  This closes only that one mode.

The two complete standard ledgers are:

\[
 \frac M Q+\sqrt{KQ}+\frac M{\sqrt K}+1
\tag{159.A17}
\]

for ordinary Erdős--Turán plus the second-derivative estimate, and

\[
 E_J\ll_\varepsilon
 \left(\frac KJ+\sqrt V+\sqrt M+1\right)X^\varepsilon
\tag{159.A18}
\]

for the literal Vaaler/Fejér endpoint kernels plus root incidence.  The
periodic-wrap seam in the initial source-report derivation is repaired by
the exact circle identities

\[
 \|\delta+p_s(\sqrt{N\ell})\|=\|\sqrt{N\ell+s}\|,
 \qquad
 \|\delta-n_s(\sqrt{N\ell})\|=\|\sqrt{N\ell-s}\|.
\tag{159.A19}
\]

The first ledger reaches the raw target only for (M\ge N^{2/3}).  The
second requires (J\ge KM^{-3/4}) and (V\le M^{3/2}) merely to make its
unsigned boundary error target-safe.  At that literal height, the favorable
transformed pair ((195/796,235/398)) gives raw capacity

\[
 N^{195/796}M^{1295/3184+\varepsilon},
\tag{159.A20}
\]

which reaches the target only if (M^{1093}\ge N^{780}).  The older
(M^{703}\ge N^{390}) threshold belongs to an explicitly easier fixed-
boundary model with an unproved (M/J) surrogate; neither threshold is a
universal barrier.

For a nonzero shifted mode (q_1=h+1), the Poisson or (B)-process
stationary data are

\[
 d=4m\mp1,\qquad \ell_{q_1,d}=\frac{4q_1^2N}{d^2},\qquad
 e\!\left(\frac{q_1^2N}{d}\right).
\tag{159.A21}
\]

The (q_1=\pm1) branch is the accepted reciprocal carrier, and general
(q_1) has the same interface; no automatic cancellation follows.  The
exact overall stationary constant is not promoted.  Favorable incomplete-
quadratic completion has raw capacity (N^{1/2}X^\varepsilon), conditional
on unavailable joint variation, and again requires (M\ge N^{2/3}).

Vaaler, Bourgain, Tao--Trudgian--Yang, Müller, and Montgomery--Vaughan do
not supply the missing literal joint signed theorem under their audited
hypotheses.  Huxley's repository card licenses no theorem import.  Every
failed comparison above is an upper-bound capacity of its named route, not
a lower bound or an impossibility theorem.

## 4. First doubtful or unproved step

After the printed precision repairs, there is no doubtful step in the
six-line reconstruction, all-(d)/all-(v) normalization, one-time special-
row subtraction, physical-lift selection, common-profile compression,
variable-mask geometry, target calibration, or shifted (h=-1) estimate.
The blind report's lift countermodel is valid for its stripped arbitrary-BV
packet, but it violates the actual fixed-dilation support/lift compatibility
and does not refute (159.A13).

The first unproved theorem is (159.A15), uniformly on the open side

\[
 M^{449}\ll R^{780},\qquad R=X^{1/4},
\tag{159.A22}
\]

beyond the accepted fixed-polylogarithmic defect collar.  For
(V>M^{3/2}), the named Fourier route first lacks signed hard-boundary
incidence control beyond the unsigned (\sqrt V) term.  For
(V\le M^{3/2}), it first lacks a joint estimate for all nonzero shifted
modes with their moving coefficients.  A future proof may use another
representation, but it must retain the same character, quotient profile,
phase, mask, endpoints, and normalization.

## 5. Required controls and outcomes

- six Abel lines, signs, endpoints, empty/singleton blocks: **GREEN**;
- zero extension and profile transitions: **GREEN**;
- all odd (d), all (v), inverse constant, complementary modes: **GREEN**;
- one-time whole zero/Nyquist subtraction and (c=4): **GREEN**;
- physical representatives, lift compatibility, and nearest-cell map: **GREEN**;
- common quotient profile versus isolated trace profiles: **GREEN and distinct**;
- exact variable band and strict/closed clipping: **GREEN**;
- scalar/raw target calibration: **GREEN as calibration, open as theorem**;
- shifted (h=-1) character mode: **GREEN and target-safe**;
- ordinary discrepancy and literal Fejér/root ledgers: **GREEN as route capacities**;
- transformed powers and old-threshold reconciliation: **GREEN**;
- reciprocal stationary carrier: **GREEN only in convention-independent form**;
- source match: **no target match through 25 August 2026**;
- external (B_{1,U}(1)) seam and downstream owners: **QUARANTINED**; and
- computation: none used.

## 6. Dependencies and exact artifacts used

Promoted evidence is the Round-159 finite kernel, the full discovery report,
the repaired common-profile method audit, the actual-project lift review,
the independent kernel line review, and the hostile power/source review.
The statement-only blind report is retained as independent evidence for the
finite Abel algebra and for the necessity of printing lift compatibility,
not as evidence against the actual-project compression.  Rounds 154--158
supply the accepted common-profile wave, complete inverse identity, whole
zero and Nyquist estimates, and isolated trace identity.  No numerical
experiment certifies any assertion.

## 7. Recommended state effect

Create one proved-internal route-scoped node for the full-Abel common-profile
recombination obstruction.  Correct the active workflow: a proof of the full
paired-interior row need not estimate the six Abel pieces separately, but no
individual outer or profile-difference term is thereby proved target-safe.
Update the existing D=1 collar, inversion, trace, source, large-wrap, and
global-lower records to point to (159.A15) as the exact first analytic seam.

Reject lift deletion from arbitrary BV alone, separate-piece necessity,
special-row double subtraction, fixed-mask substitution, untwisted shifted
mode, truncated-Fourier boundary deletion, incomplete discrepancy ledgers,
capacity-as-lower-bound readings, reciprocal-transform novelty, and any new
range or downstream exponent.  Leave every other owner, M9, the bridge, the
quarter target, and both global exponents unchanged.
