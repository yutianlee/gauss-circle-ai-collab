# Round 95 report: actual rational-cluster attack

Campaign: `gc-strict-sub-one-third-cluster-source-fork`  
Task: `actual_rational_cluster_attack`  
Role: analytic discovery  
Starting graph SHA-256: `e3233f94ee0630b28c21ba102a0ee0fc55016858af6fbd61e80ea0e264128104`

## 1. Result

The full fixed-window estimate (95.7) is **not proved**.  There is,
however, a strict exact reduction and a coefficient-blind no-go.

Fix one actual fixed-symbol dyadic block with

\[
 d\asymp D,\qquad |h|\asymp L,\qquad
 1\leq L\leq H_D\asymp DY^{-1/4},
 \qquad W=Y^{7/16},
\]

and put \(\kappa _1=1\), \(\kappa _2=4\).  After reducing
\(h/d=a/b\) and summing **all** lifts \((h,d)=(ga,gb)\), the literal
M1 and M2 ray coefficients satisfy

\[
 |A_i(a,b)|\ll L^{-1},\qquad
 \sum_{(a,b)=1}|A_i(a,b)|^2\ll {D\over L}.                 \tag{1.1}
\]

The proof uses the actual location of \(\chi _4\): it is
\(\chi _4(gb)=\chi _4(g)\chi _4(b)\) for M1 and
\(\chi _4(|ga|)=\chi _4(g)\chi _4(|a|)\) for M2.  Thus the lift
variable carries the bounded-partial-sum sequence \(\chi _4(g)\).
Consequently (1.1) includes, rather than discards, every cross term
between distinct lifts of the same reduced fraction.  The raw
\((h,d)=(h',d')\) diagonal and the complete equal-reduced-fraction
diagonal are both \(O(D/L)\), hence always at most \(Y^{1/2}\).

Writing

\[
 n=ab'-a'b,
\]

the cluster energy is exactly that diagonal plus the signed determinant
correlation

\[
 \boxed{
 \begin{aligned}
 \mathfrak O_i(D,L;c,W)=2\Re
 \sum_{\substack{(a,b),(a',b')\in\mathscr R_i\\
             0<n=ab'-a'b<\kappa_i bb'/W}}
 &\Xi_i(a,b)\Xi_i(a',b')
 U_i(a,b)\overline{U_i(a',b')}\\[-2mm]
 &\times e\!\left({cn\over\kappa_i bb'}\right)
 \left(1-{Wn\over\kappa_i bb'}\right),
 \end{aligned}}                                                   \tag{1.2}
\]

where \(A_i=\Xi_iU_i\),

\[
 \Xi _1(a,b)=\chi _4(b),\qquad
 \Xi _2(a,b)=\chi _4(|a|),                                    \tag{1.3}
\]

and \(U_i\) retains the exact Vaaler taper, denominator profile,
frequency profile, height, prefix, hard top, and star.  Formula (1.2)
also retains the centre phase, both orientations through \(2\Re\), and
the literal factor four in M2.  Signed numerators are allowed in
\(\mathscr R_i\), so both frequency signs are present.

The smallest sufficient new assertion is the one-sided signed bound

\[
 \mathfrak O_i(D,L;c,Y^{7/16})
 \ll_\varepsilon Y^{1/2+\varepsilon}                          \tag{1.4}
\]

for the blocks not already closed below.  An absolute value on the
left of (1.4) would be stronger than necessary.  Every reduction before
(1.4) is proved in Section 3.

If signs and the centre phase are discarded only after (1.1), Farey
spacing gives

\[
 \mathcal C_i(D,L;c)
 \ll {D\over L}
   \left(1+\min\left(DL,{D^2\over W}\right)\right)
 \ll {D\over L}+\min\left(D^2,{D^3\over WL}\right).          \tag{1.5}
\]

At the minimax block

\[
 (D,L,W)=(Y^{1/2},Y^{1/6},Y^{7/16}),
\]

the exact ledgers are

\[
 \#\mathscr R_i\asymp Y^{2/3},\qquad
 \#\hbox{ cells}\asymp Y^{5/48},\qquad
 {D^2\over W}=Y^{9/16},\qquad
 \mathcal E_{i,=}:=\sum|A_i|^2\ll Y^{1/3},                  \tag{1.6}
\]

and (1.5) is

\[
 \mathcal C_i\ll Y^{43/48+\varepsilon}.                    \tag{1.7}
\]

Thus random cells and coefficient-blind Farey spacing save
\(Y^{5/48}\) from the coherent \(D^2=Y\) capacity, but the remaining
actual signed correlation must still save

\[
 Y^{43/48}/Y^{1/2}=Y^{19/48}.                                \tag{1.8}
\]

This is a quantitatively smaller survivor, but it is not an estimate of
that survivor.  A phase-conjugating coefficient model attains the order
in (1.7), so no argument using only support, \(|A_i|\ll L^{-1}\), and
rational spacing can close (1.4).

There is also a distinct, much sharper aggregate ceiling.  Popov's
accepted local second moment gives for the **full discrepancy**

\[
 Q(Y,W)\ll W\sqrt Y+Y(\log Y)^2,
\]

so at this window

\[
 {Q(Y,W)\over W}\ll Y^{1/2}+Y^{9/16}(\log Y)^2.             \tag{1.9}
\]

The additive \(Y\)-term is only \(Y^{1/16}\) above the desired total
local mass \(Y^{15/16}\).  No power saving over that additive term is
obtained here.  Importantly, (1.9) does not bound the positive
triangular energy of each fixed M1/M2 block: the sinc-square inequality
runs from the triangular form to the local integral, not conversely,
and Popov's theorem may use cancellation between blocks and owners.

## 2. Exact statement and hypotheses

Let \(c\asymp Y\), \(W=Y^{7/16}\), and work on one of the fixed-symbol
strata supplied by the accepted Round-94 moving-symbol reduction.  Let
\(v_L\) be one actual dyadic frequency profile and let
\(\omega_{i,D}\) be the literal denominator profile on that stratum.
It can be an interior smooth profile or the sampled-BV hard-top profile,
with the specified endpoint star.  Its sup norm and sampled variation
are \(O(1)\).  The height \(H\) and all prefix/floor data are fixed on
the stratum.

With

\[
 \alpha_{h,H}=-{\Phi(|h|/(H+1))\over 2\pi i h},
 \qquad
 C_h=e(h/4)-e(3h/4),                                        \tag{2.1}
\]

define the literal block coefficients

\[
 \begin{aligned}
 q_1(h,d)&=-4\alpha_{h,H}\chi _4(d)
              \omega_{1,D}(d)v_L(|h|),\\
 q_2(h,d)&= 4\alpha_{h,H}C_h
              \omega_{2,D}(d)v_L(|h|).
 \end{aligned}                                               \tag{2.2}
\]

Thus the two polynomials are

\[
 S_i(t)=\sum_{h,d}q_i(h,d)e\!\left({ht\over\kappa_i d}\right),
 \qquad \kappa_1=1,\quad\kappa_2=4.                         \tag{2.3}
\]

There is no relabelling of M1 as an M2 frequency.  The outer factors
\(-4\) and \(4\), and the factor \(4\) in the M2 phase, all remain in
(2.2)--(2.3).

Reduce every \(h/d\) uniquely as \(a/b\), where
\(a\in\mathbb Z\setminus\{0\}\), \(b>0\), and
\((|a|,b)=1\), and define the complete ray coefficient

\[
 A_i(a,b)=\sum_{g\geq1}q_i(ga,gb).                           \tag{2.4}
\]

The sum is over exactly the lifts allowed by all literal supports; it
is not replaced by a lift count.  Let \(\mathscr R_i\) be the finite set
on which (2.4) is nonzero.  The fixed-block triangular energy is

\[
 \mathcal C_i(c)=
 \int_0^1\sum_\nu
 \left|\sum_{a/b:\ a/(\kappa_i b)\in C_{\nu,\vartheta}}
 A_i(a,b)e\!\left({ca\over\kappa_i b}\right)\right|^2
 d\vartheta.                                                 \tag{2.5}
\]

The claimed reduction is:

* \(\mathcal C_i=\mathcal E_{i,=}+\mathfrak O_i\), with
  \(\mathcal E_{i,=}\ll D/L\) and \(\mathfrak O_i\) exactly (1.2);
* coefficient-blind estimates prove the target whenever, in exponent
  notation \(D=Y^\delta\), \(L=Y^\ell\),

  \[
   {1\over4}\leq\delta\leq{1\over2},\qquad
   0\leq\ell\leq\delta-{1\over4},\qquad
   3\delta-\ell\leq {15\over16};                            \tag{2.6}
  \]

* the exact remaining block region is therefore

  \[
  \mathscr H_{95}=\left\{(\delta,\ell):
    {1\over4}\leq\delta\leq{1\over2},\quad
    0\leq\ell\leq\delta-{1\over4},\quad
    3\delta-\ell>{15\over16}\right\},                     \tag{2.7}
  \]

  and (1.4), uniformly there, suffices for the blockwise target.

All constants may depend on the fixed dyadic profiles.  All logarithmic
losses from dyadic blocks and fixed-symbol strata are allowed inside
\(Y^\varepsilon\).  No arbitrary moving coefficient, smoothed-away top,
deleted star, one-sided frequency convention, or unsigned arithmetic
majorant is among the hypotheses.

## 3. Proof or derivation

**The exact \(5/16\) implication.**  The desired local mass is

\[
 Q(Y,W)\ll W Y^{1/2+\varepsilon}
 =Y^{15/16+\varepsilon}.                                    \tag{3.1}
\]

The accepted persistence bridge gives

\[
 |P(X)|\ll Q^{1/3}+(Q/W)^{1/2}
 \ll Y^{5/16+\varepsilon}+Y^{1/4+\varepsilon},              \tag{3.2}
\]

so the delivered exponent is exactly \(5/16\).  It is not \(1/4\).

**M1/M2 algebra and the lift sum.**  From (2.1),

\[
 C_h=
 \begin{cases}2i\chi _4(h),&h\text{ odd},\\0,&h\text{ even},\end{cases}
 \qquad
 \alpha_{h,H}C_h
 =-{\Phi(|h|/(H+1))\chi _4(|h|)\over\pi|h|}.                \tag{3.3}
\]

The second coefficient is real and even.  For a reduced signed ray
\((a,b)\), put

\[
 F_{i,a,b}(g)=
 \Phi(g|a|/(H+1))v_L(g|a|)\omega_{i,D}(gb),                 \tag{3.4}
\]

with every literal support indicator and star included in this sampled
function.  Multiplicativity of \(\chi _4\), including its zero on even
integers, gives the exact formulas

\[
 \begin{aligned}
 A_1(a,b)
 &= {2\chi _4(b)\over\pi i a}
    \sum_{g\geq1}{\chi _4(g)\over g}F_{1,a,b}(g),\\
 A_2(a,b)
 &= -{4\chi _4(|a|)\over\pi |a|}
    \sum_{g\geq1}{\chi _4(g)\over g}F_{2,a,b}(g).
 \end{aligned}                                               \tag{3.5}
\]

In particular M1 rays with even \(b\) vanish, and M2 rays with even
\(a\) vanish.  Both signs of \(a\) remain in (3.5).

If the support in (3.4) is nonempty, its lift variable satisfies

\[
 g\asymp G,\qquad G\asymp {L\over|a|}\asymp {D\over b}.     \tag{3.6}
\]

The fixed smooth profiles have bounded sampled variation.  The hard top
\(W(x){\bf1}_{x\leq1}\) is BV, and a prescribed star is one additional
bounded jump.  Hence

\[
 \sup_g|F_{i,a,b}(g)|+\operatorname{Var}_gF_{i,a,b}(g)\ll1,
 \qquad
 \operatorname{Var}_g\!\left({F_{i,a,b}(g)\over g}\right)
 +\sup_g{ |F_{i,a,b}(g)|\over g}\ll G^{-1}.                 \tag{3.7}
\]

Since every partial sum of \(\chi _4(g)\) is bounded, Abel summation in
(3.5) yields

\[
 \sum_g{\chi _4(g)\over g}F_{i,a,b}(g)\ll G^{-1},
 \qquad |A_i(a,b)|\ll {1\over |a|G}\ll {1\over L}.         \tag{3.8}
\]

There are \(O(DL)\) possible signed primitive pairs, since necessarily
\(|a|\ll L\), \(b\ll D\).  Therefore

\[
 \sum_{\mathscr R_i}|A_i(a,b)|^2\ll {DL\over L^2}={D\over L}.
                                                                    \tag{3.9}
\]

Before ray aggregation, (2.2) also gives directly

\[
 \sum_{h,d}|q_i(h,d)|^2\ll DL\,L^{-2}={D\over L}.           \tag{3.10}
\]

Thus (3.9), not (3.10), is the required exact multiplicity audit: it
shows that all equal-frequency lift cross terms remain safe because of
the actual character in the lift variable.  On a nondegenerate interior
part of the minimax block, (3.10) is also \(\gg D/L\), so the diagonal
scale \(Y^{1/3}\) in (1.6) is genuine.

**Exact triangular expansion and determinant survivor.**  The random-cell
identity applied after (2.4) is

\[
 \begin{aligned}
 \mathcal C_i(c)=
 \sum_{(a,b),(a',b')\in\mathscr R_i}
 &A_i(a,b)\overline{A_i(a',b')}
 e\!\left({c(ab'-a'b)\over\kappa_i bb'}\right)\\
 &\times
 \left(1-{W|ab'-a'b|\over\kappa_i bb'}\right)_+ .          \tag{3.11}
 \end{aligned}
\]

Because both fractions are reduced with positive denominator,
\(ab'-a'b=0\) if and only if \((a,b)=(a',b')\).  Its contribution is
exactly (3.9).  Pairing the terms with positive and negative determinant
gives (1.2).  No absolute value has been inserted in the arithmetic sum.

**Coefficient-blind Farey ledger.**  Distinct reduced fractions with
denominators at most \(O(D)\) have spacing \(\gg D^{-2}\).  Hence each
ray has at most

\[
 O\!\left(1+{\kappa_iD^2\over W}\right)                    \tag{3.12}
\]

neighbours seen by the triangular kernel, and of course at most
\(O(DL)\) neighbours.  Schur's test applied to the absolute-value
adjacency matrix, followed by (3.9), proves (1.5).  In exponent notation
its possibly large term is

\[
 \min\left(Y^{2\delta},
           Y^{3\delta-\ell-7/16}\right).                    \tag{3.13}
\]

The diagonal exponent \(\delta-\ell\) is always at most \(1/2\).  If
\(\delta>1/4\), the first exponent in (3.13) is larger than \(1/2\), so
the coefficient-blind target closes exactly when
\(3\delta-\ell-7/16\leq1/2\), which is (2.6).  This proves the full
all-block classification (2.6)--(2.7), not only the minimax calculation.

At the minimax point the frequency band has width \(\asymp L/D\) and
therefore meets \(\asymp WL/D=Y^{5/48}\) random cells.  The ray count is
\(\asymp DL=Y^{2/3}\), so the mean coefficient-blind occupancy is
\(D^2/W=Y^{9/16}\).  Multiplying this degree by the exact ray energy
\(D/L=Y^{1/3}\) gives \(Y^{43/48}\), proving (1.6)--(1.8).

**The false arbitrary-coefficient shadow is sharp.**  In the minimax
rectangle choose \(\gg DL\) primitive one-lift rays
\(a\asymp L,b\asymp D\), with \(b\) odd for the M1 parity support or
\(a\) odd for the M2 parity support.  The elementary Mobius count of
coprime pairs in a dyadic rectangle gives this positive-density subset.
Set

\[
 \widetilde A(a,b)=L^{-1}e\!\left(-{ca\over\kappa_i b}\right).
                                                                    \tag{3.14}
\]

This respects the support, parity, and the envelope
\(|\widetilde A|\leq L^{-1}\), but not the actual Vaaler/character
phase.  After multiplication by the centre phase, every selected term
in every cell is \(+L^{-1}\).  For each shift there are
\(O(1+WL/D)\) occupied cells.  Cauchy--Schwarz on the cell occupancies
therefore gives

\[
 \widetilde{\mathcal C}_i
 \gg { (DL)^2\over L^2(1+WL/D)}
 \asymp {D^3\over WL}=Y^{43/48}.                             \tag{3.15}
\]

Thus the operation “aggregate rays, forget the literal coefficients,
then use spacing” self-returns at exactly (1.7).  The random-cell identity
is not cancellation.

**Frequency signs.**  If \(a\) and \(a'\) have opposite signs, then on
one dyadic block

\[
 \left|{a\over\kappa_i b}-{a'\over\kappa_i b'}\right|
 \gg {L\over\kappa_iD}.                                     \tag{3.16}
\]

Hence cross-sign cells are absent whenever \(WL/(\kappa_iD)\gg1\); in
particular they are absent at the minimax block, where this ratio is
\(Y^{5/48}/\kappa_i\).  In the remaining low-frequency blocks they are
not dropped: cellwise \(2|z_+z_-|\leq|z_+|^2+|z_-|^2\) charges the
cross-sign ledger to the two same-sign energies with no power loss.

**Cross-scale, moving-symbol, bottom, and R5 ledgers.**  There are only
polylogarithmically many denominator/frequency blocks.  For their exact
union, cellwise Cauchy gives

\[
 \left|\sum_B z_B\right|^2\leq \#\{B\}\sum_B|z_B|^2.       \tag{3.17}
\]

Thus cross-scale and M1--M2 cross terms, including coincident frequencies,
are bounded rather than silently deleted; the loss is a power of
\(\log Y\).

On a length-\(W\) window,

\[
 \sqrt{t+W}-\sqrt t<1,
 \qquad
 D\,| (t+W)^{-1/4}-t^{-1/4}|\ll DY^{-5/4}W<1,               \tag{3.18}
\]

uniformly for \(D\leq Y^{1/2}\).  Each moving prefix and height therefore
has \(O(1)\) changes, and all scales give \(O(\log Y)\) fixed-symbol
strata.  A stratum shorter than \(W\) can be enclosed in a length-\(W\)
interval for its fixed polynomial before applying the positive kernel.
The hard top and stars are already present in (3.4)--(3.7).  The bottom
and the accepted R5 sum are pointwise \(O_\varepsilon(Y^{1/4+\varepsilon})\),
so their length-\(W\) square mass is
\(O_\varepsilon(WY^{1/2+\varepsilon})\).  Cauchy absorbs their cross
terms with the main sums.  Hence (1.4) on every block in (2.7) really is
sufficient for (3.1).

## 4. First doubtful or unproved step

The first unproved step is precisely (1.4): cancellation in the literal
\(n\neq0\) determinant sum (1.2), uniformly for every block in
\(\mathscr H_{95}\).  At the minimax point it must gain \(Y^{19/48}\)
over the sharp coefficient-blind rational-cell capacity.  The summands
that have survived still contain

* the M1 sign \(\chi _4(b)\chi _4(b')\), or the M2 sign
  \(\chi _4(|a|)\chi _4(|a'|)\);
* the alternating lift transforms inside both \(U_i\)'s;
* the reciprocal centre phase \(e(cn/(\kappa_i bb'))\);
* the moving Vaaler taper and literal BV/profile endpoints; and
* the triangular cutoff with its variable hard top
  \(n<\kappa_i bb'/W\).

No selected-context theorem estimates this joint object.  Taking absolute
values in \(n\), in the rational neighbours, or in the cell sums gives
back (1.5).  The direct pointwise one-third block menu controls one value
of the original polynomial, not the family of frequency-restricted cell
sums in (2.5).  The Round-93 global moment averages in \(t\) before this
fixed-centre positive form and permits the prescribed centre to be
exceptional.

At the level of the full discrepancy, the first known quantitative seam
is instead Popov's additive \(Y(\log Y)^2\) in the local square mass.  At
\(W=Y^{7/16}\) it is a \(Y^{1/16}\) excess over (3.1).  The selected
context does not identify that upper-bound term with a literal subset of
(1.2), so it would be an overclaim to call it an exact determinant
off-diagonal.  No power over it emerges from the present reduction.

## 5. Required control tests and outcomes

| Control | Exact test | Outcome |
|---|---|---|
| \(5/16\) and local \(15/16\) | Substitute \(W=Y^{7/16}\), \(Q=WY^{1/2}\) into both persistence branches. | Pass: \(Q=Y^{15/16}\), branches \(Y^{5/16}\) and \(Y^{1/4}\). |
| M1/M2 algebra and factor four | Use (2.1)--(2.3) before reduction. | Pass: M1 frequency is \(h/d\); M2 frequency is \(h/(4d)\), its determinant cutoff is \(4bb'/W\), and both outer factors four remain. |
| Raw diagonal | Sum \(|q_i(h,d)|^2\) over \(DL\) terms of size \(L^{-1}\). | Pass: \(O(D/L)\), and \(\asymp D/L\) on a nondegenerate minimax interior. |
| Exact reduced-fraction multiplicity | Sum every lift in (2.4), then use the actual \(\chi _4(g)\) in (3.5). | Pass: Abel gives \(|A_i|\ll L^{-1}\), so the complete equal-ray contribution is \(O(D/L)\). No lift cross term is omitted. |
| Near unequal rays | Expand the triangular form and set \(n=ab'-a'b\). | Open only at (1.2). Coefficient-blind degree is \(1+D^2/W\); at minimax the capacity is \(Y^{43/48}\). |
| Both frequency signs | Test the minimum distance of opposite-sign dyadic bands, and retain the low-band cross term. | Pass: it vanishes at minimax; elsewhere it is charged by \(2|z_+z_-|\leq|z_+|^2+|z_-|^2\). |
| Minimax cell count | Compute \(WL/D\). | Pass: \(Y^{7/16+1/6-1/2}=Y^{5/48}\). |
| All dyadic blocks | Apply the refined Schur bound (1.5). | Pass as a classification: (2.6) is safe; only (2.7) survives. No claim is made that the survivor is bounded. |
| Cross-scale and M1--M2 assembly | Apply cellwise Cauchy before deleting any cross term. | Pass: only polylogarithmic loss; literal M1/M2 frequency systems stay separate. |
| Moving height and denominator floors | Check both variations in (3.18). | Pass: \(O(1)\) changes per scale and \(O(\log Y)\) fixed-symbol strata. |
| Prefix, hard top, and stars | Put the jump and specified endpoint value inside the sampled-BV function in (3.4). | Pass: their total variation is \(O(1)\), including in the lift Abel bound. |
| Bottom and R5 ownership | Square the accepted pointwise \(Y^{1/4+\varepsilon}\) bounds on a length-\(W\) interval. | Pass: each is within \(WY^{1/2+\varepsilon}\), with cross terms handled by Cauchy. |
| Arbitrary-coefficient false shadow | Conjugate the centre phase as in (3.14) on \(\gg DL\) primitive rays. | Fail for the shadow, as required: it attains \(Y^{43/48}\). Actual character/phase correlation is indispensable. |
| Random-cell identity as an estimate | Compare the exact identity (3.11) with (3.15). | No implication: the identity is a positive re-expression and supplies no arithmetic saving. |
| Popov ceiling | Divide \(W\sqrt Y+Y\log^2Y\) by \(W\). | Pass as a guardrail: \(Y^{1/2}+Y^{9/16}\log^2Y\), but it does not upper-bound each block's triangular form. |
| Pointwise/menu implication | Compare one central block value with all restricted cell sums. | No implication in either required direction. The accepted one-third pointwise envelope does not prove (1.4), and (1.4) would deliver only the \(5/16\) discrepancy exponent. |
| Canonical core, M9, and quarter target | Compare variables, norm, and conclusion with the two Round-92 cores and M9. | No implication is asserted. The pre-transform \(W=Y^{7/16}\) determinant correlation is neither canonical core; even its proof would not prove M9-M1, M9-M2, M9, endpoint uniformity, or \(GC\)-target. |

Every control above is analytic.  No numerical experiment was used.

## 6. Dependencies and exact artifacts used

The result uses only the brief and selected-context artifacts assigned to
this task:

* `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/briefs/actual_rational_cluster_attack.md`
  for the literal target, mandatory ledgers, and output scope;
* `protocol.md` for proof-state ownership, signed/unsigned separation, and
  the seven-section report contract;
* `state/proof_obligations.yml` for the exact statuses and statements of
  R5-Full, M9-M1, M9-M2, the M2 character factor and beta algebra, the
  moving global moment, the persistence bridge, the triangular kernel,
  the non-subcoherent cluster obligation, the one-third theorem, the two
  canonical cores, the Popov guardrail, and the rejected false
  implications;
* `state/best_proof_draft.md` for H1--H4, the literal M1/M2 coefficients,
  the actual dyadic profiles, hard top, direct one-third menu, bottom/R5
  owners, and the accepted Round-91--94 scope;
* `state/active_campaign.yml` for the frozen window, target, controls, and
  graph hash;
* `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/derivation_packet.md`
  for (95.1)--(95.9);
* `rounds/codex-managed/gc-prescribed-point-local-moment-bridge/synthesis.md`
  for the accepted local bridge, cluster scope, and Popov ceiling;
* `rounds/codex-managed/gc-prescribed-point-local-moment-bridge/candidates/conductor_exact_cluster_kernel.md`
  for the exact sinc-square/random-cell formula and moving-stratum
  interface;
* `rounds/codex-managed/gc-prescribed-point-local-moment-bridge/reviews/conductor_round94_local_kernel.md`
  for the corrected literal frequencies and subcoherence boundary;
* `rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/reports/moving_coefficient_moment_attack.md`
  for exact ray grouping, height differences, moving prefix/BV transfer,
  hard-top/star treatment, and its pointwise/canonical nonimplications;
* `rounds/codex-managed/gc-unconditional-exponent-extraction/candidates/conductor_one_third_assembly.md`
  for the literal all-block menu and bottom/R5 assembly.

No sibling Round-95 report, unlisted strategy artifact, web source, or
computation was read or used.

## 7. Recommended state effect

**Promote, after conductor seam review,** the exact actual-lift lemma
(3.5)--(3.9), the determinant decomposition (3.11)--(1.2), the
coefficient-blind all-block classification (2.6)--(2.7), and the minimax
capacity no-go (1.6)--(1.8).  These form a graph-ready reduction with
literal M1/M2 coefficients and all owners retained.

**Create or retain open** the narrow survivor
`GC-W7/16-actual-reduced-determinant-correlation`: prove the one-sided
bound (1.4) for both \(i=1,2\), uniformly on the hard region
\(\mathscr H_{95}\), with \(U_i\), \(\Xi_i\), centre phase, triangular
top, both signs, floors, profiles, hard top, stars, and logarithmic
assembly exactly as in (1.2).  At the minimax block its required signed
gain is \(Y^{-19/48}\) relative to coefficient-blind capacity.

**Reject** “random cells plus Farey spacing” and every arbitrary-bounded-
coefficient variant as proofs of the target; (3.14)--(3.15) make the
failure sharp.  Also reject any claim that Popov's additive \(Y\) term is
already an exact identified subset of (1.2).

**No change** is licensed for
`GC-nonsubcoherent-actual-cluster-local-moment`, `M9-M1`, `M9-M2`, `M9`,
either Round-92 canonical core, endpoint uniformity, or `GC-target`.
The certified uniform exponent remains \(1/3\); this report proves no
strict sub-one-third theorem.
