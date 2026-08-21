# Completed directional kernel attack

## 1. Result

**Completed-kernel self-return lemma.**  Under the accepted Round-75,
Round-92, and Round-109 identities, the global completed scalar has a
literal finite common-atom formula, and the only norm needed for the hard
energy is

\[
 \Re \mathfrak C_L^{\rm comp}\ll_\varepsilon L^2X^\varepsilon.
\tag{1.1}
\]

This estimate is necessary and sufficient, up to target-sized terms, for
\(\mathcal E_L^{\rm top}\ll_\varepsilon L^2X^\varepsilon\).  Neither a
modulus estimate, blockwise absolute values, nor a fixed-\(a\) Gram is
needed for that implication.

Only the real-part assertion (1.3) is certified; no bound for the complex
difference is asserted.  There is, however, no new lower-capacity kernel after exact one-count
recombination.  Let

\[
 R_m=\sum_{\substack{h\in\mathscr H_L\\m\le h\le4m}}
 \chi _4(h)a_{\rm end}(h,m)e(J\sqrt{hm}),\qquad J=X^{1/2},
\tag{1.2}
\]

with the exact finite odd support and actual endpoint symbol.  If
\(\mathfrak C_L^{\rm off}\) denotes the one-orientation Round-75
off-diagonal correlation defined in (2.3) below, then

\[
 \boxed{\quad
 \Re\bigl(\mathfrak C_L^{\rm comp}-\mathfrak C_L^{\rm off}\bigr)
 =O_\varepsilon(L^2X^\varepsilon).
 \quad}
\tag{1.3}
\]

Thus the completed directional proposal is a strict physical self-return:
it removes the dyadic and metric scaffolding, but returns to the original
alternating off-diagonal row energy.  It does not by itself create a
power saving.  The smallest exact character-sensitive reformulation I
obtain is the adjacent-primitive-ray difference (3.12); its target bound
is still unproved because it retains every moving actual-symbol seam.

## 2. Exact statement and hypotheses

Fix real \(X\ge2\), put \(J=X^{1/2}\), and let
\(1\le L\le J^{1/2}\).  Write \(e(t)=e^{2\pi it}\).  The hypotheses are:

1. \(\mathscr H_L\) is the accepted exact finite half-open odd
   top-frequency support, and \(a_{\rm end}(h,m)\) is the accepted actual
   normalized endpoint coefficient.  In particular, its floors, stars,
   equality half weights, collars, physical entry and exit, and empty or
   singleton fibres are not replaced by smooth surrogates.
2. The accepted hard-energy and scalar-completion identities hold:

\[
 \mathcal E_L^{\rm top}
 =\mathcal E_{{\rm owned},L}
  +2\Re\sum_B\mathfrak Q_B^{\rm res},
\tag{2.1}
\]

\[
 \mathfrak Q_B^{\rm res}
 =\mathfrak Q_B^{\rm comp}-\sum_\nu\mathfrak O_{B,\nu},
 \qquad
 \sum_{B,\nu}|\mathfrak O_{B,\nu}|
 \ll_\varepsilon L^2X^\varepsilon,
\tag{2.2}
\]

   and the owned term is bounded in absolute value at the same scale.
   There is one representative orientation and one outer \(2\Re\).
3. Every \(A,D,K,G\) lattice is the inherited finite half-open one-count
   lattice.  The stationary reciprocal interval is the literal open
   interval, with zero extension outside it; genuine equality atoms keep
   their separately tagged inherited star or half weight.  The exact
   smooth metric telescope, including its terminal member and its centre
   atom, is used.

The exact physical diagonal and one-orientation off-diagonal scalar are

\[
 \mathcal D_L
 =\sum_{h\in\mathscr H_L}
   \sum_{\lceil h/4\rceil\le m\le h}|a_{\rm end}(h,m)|^2,
\tag{2.3a}
\]

\[
 \boxed{
 \begin{aligned}
 \mathfrak C_L^{\rm off}
 ={}&\sum_{\substack{h,s\in\mathscr H_L\\h<s<4h}}
   \chi _4(h)\chi _4(s)
   \sum_{m=\lceil s/4\rceil}^{h}
   a_{\rm end}(h,m)\overline{a_{\rm end}(s,m)}\\
 &\hspace{38mm}\times
   e\!\left(J(\sqrt h-\sqrt s)\sqrt m\right).
 \end{aligned}}
\tag{2.3b}
\]

Equivalently, write \(s=h+2r_{\rm row}\).  Since \(h\) is odd,
\(\chi _4(h)\chi _4(h+2r_{\rm row})=(-1)^{r_{\rm row}}\), and the exact
Round-75 alternating formula is

\[
 \boxed{
 \begin{aligned}
 \mathfrak C_L^{\rm off}
 ={}&\sum_{\substack{h\in\mathscr H_L\\r_{\rm row}\ge1\\
               h+2r_{\rm row}\in\mathscr H_L\\
               h+2r_{\rm row}<4h}}
 (-1)^{r_{\rm row}}
 \sum_{m=\lceil(h+2r_{\rm row})/4\rceil}^{h}
 a_{\rm end}(h,m)\overline{a_{\rm end}(h+2r_{\rm row},m)}\\
 &\hspace{27mm}\times
 e\!\left(J(\sqrt h-\sqrt{h+2r_{\rm row}})\sqrt m\right).
 \end{aligned}}
\tag{2.3c}
\]

The subscript distinguishes the physical row shift from the metric
Fourier index \(r\) in (2.9).

The ceiling is literal, an empty interval contributes zero, and the
conjugate orientation \(s<h\) is not also summed.  Direct expansion gives

\[
 \mathcal E_L^{\rm top}=\mathcal D_L+2\Re\mathfrak C_L^{\rm off}.
\tag{2.4}
\]

Here is the literal completed kernel before physical self-return.  For a
primitive odd ray \((a,b)=1\), \(a<b<4a\), an odd lift \(g\) with
\(ga,gb\in\mathscr H_L\), put

\[
 \Lambda_{a,b}={X(\sqrt b-\sqrt a)^2\over2},\qquad
 I_{a,b}=\left(
 {J(\sqrt b-\sqrt a)\over2\sqrt a},
 {J(\sqrt b-\sqrt a)\over\sqrt b}
 \right).
\tag{2.5}
\]

On the common finite atom \(z=(B,a,b,g,k)\), let

\[
 \begin{aligned}
 \mathcal I_B(z)={}&
 \omega_B^{\rm act}(a,b,g,k)
 \int_{gb/4}^{ga}A^\circ_{B;ga,gb}(x)\\
 &\quad\times e\!\left(kx-J(\sqrt{gb}-\sqrt{ga})\sqrt x\right)\,dx .
 \end{aligned}
\tag{2.6}
\]

This is notation for the unchanged accepted collared coefficient, not an
arbitrary weight.  Its fixed half-open \(k\)-lattice is zero-extended off
the physical support \(k\in I_{a,b}\); the equality, endpoint, original
Poisson-zero, nonstationary, collar, floor, star, and entry/exit atoms
remain their distinct tagged atoms in the accepted one-count dictionary.
In particular, the original Poisson-zero tag is not the metric Fourier
index below.

For \(d(t)=\|t\|\), \(V_R(t)=\eta(Rd(t))\),
\(W_R=V_R-V_{2R}\), and the exact dyadic terminal \(G_*\asymp G\), set

\[
 \mathscr P_{G_*}(t)
 =\sum_{\substack{1\le R<G_*\\R=2^j}}W_R(t)
   +V_{G_*}(t)-1_{t\in\mathbb Z}
 =1_{t\notin\mathbb Z}.
\tag{2.7}
\]

Thus the completed all-atom multiplier is, exactly,

\[
 \mathscr P_{G_*}(t)+1_{t\in\mathbb Z}
 =\sum_{R<G_*}W_R(t)+V_{G_*}(t)=1.
\tag{2.8}
\]

Equation (2.8) is the required centre convention: the punctured metric
telescope subtracts the exact centre once, and completed owner
reinsertion adds that centre once.  The terminal \(V_{G_*}\) is not
dropped.  Moreover

\[
 W_R(t)=\widehat W_R(0)+\sum_{r\ne0}\widehat W_R(r)e(rt),
 \qquad
 V_{G_*}(t)=\widehat V_{G_*}(0)
             +\sum_{r\ne0}\widehat V_{G_*}(r)e(rt),
\tag{2.9}
\]

so every metric density \(r=0\) and every discrepancy \(r\ne0\) is
present jointly.

Let \(\Pi_B(z)\) be the product of the inherited exact
\(A,D,K,G\) one-count indicators/weights, including the prescribed
boundary convention.  On an active atom,
\(\sum_B\Pi_B(z)=1\).  The unique literal finite global completed scalar
is therefore

\[
 \boxed{
 \begin{aligned}
 \mathfrak C_L^{\rm comp}
 ={}&\sum_{\substack{(a,b)=1\;{\rm odd}\\a<b<4a}}
 \chi _4(a)\chi _4(b)
 \sum_{\substack{g\;{\rm odd}\\ga,gb\in\mathscr H_L}}
 \sum_{k}^{\rm fixed,*}
 \sum_B\Pi_B(a,b,g,k)\,\mathcal I_B(B,a,b,g,k)\\
 &\quad\times\left\{
 \mathscr P_{G_*(B)}(\Lambda_{a,b}/k)
 +1_{\Lambda_{a,b}/k\in\mathbb Z}\right\},
 \end{aligned}}
\tag{2.10}
\]

with the accepted separately tagged interpretation at the original
Poisson-zero atom, where \(\Lambda/k\) is not formed.  Formula (2.10),
not a coefficient-blind bare sum, is the literal formula: if a profile
depends on its dyadic scale, it remains inside \(\mathcal I_B\).  Finite
one-count permits the block sums to be interchanged, but it does not
permit deleting a collar or replacing \(\sum_B\Pi_B\mathcal I_B\) by a
new scale-free symbol.

## 3. Proof or derivation

Put \(T=L^2X^\varepsilon\),
\(\mathfrak O_L=\sum_{B,\nu}\mathfrak O_{B,\nu}\), and

\[
 \widetilde{\mathcal E}_{{\rm owned},L}
 =\mathcal E_{{\rm owned},L}-2\Re\mathfrak O_L.
\tag{3.1}
\]

Substitution of (2.2) into (2.1) gives the exact identity

\[
 \mathcal E_L^{\rm top}
 =\widetilde{\mathcal E}_{{\rm owned},L}
  +2\Re\mathfrak C_L^{\rm comp}.
\tag{3.2}
\]

If
\(|\mathcal E_{{\rm owned},L}|\le C_0T\) and
\(\sum_{B,\nu}|\mathfrak O_{B,\nu}|\le C_1T\), then

\[
 |\widetilde{\mathcal E}_{{\rm owned},L}|
 \le(C_0+2C_1)T.
\tag{3.3}
\]

Consequently, \(\Re\mathfrak C_L^{\rm comp}\le C_2T\) implies

\[
 \mathcal E_L^{\rm top}\le(C_0+2C_1+2C_2)T.
\tag{3.4}
\]

Conversely, \(\mathcal E_L^{\rm top}\le C_3T\) implies

\[
 \Re\mathfrak C_L^{\rm comp}
 \le\tfrac12(C_3+C_0+2C_1)T.
\tag{3.5}
\]

Since \(\mathcal E_L^{\rm top}\ge0\), (3.2) also supplies the automatic
lower bound

\[
 \Re\mathfrak C_L^{\rm comp}
 \ge-\tfrac12(C_0+2C_1)T.
\tag{3.6}
\]

Thus the upper real part is the weakest scalar target.  A bound for
\(|\mathfrak C_L^{\rm comp}|\) is sufficient but stronger; so is
\(\sum_B|\mathfrak Q_B^{\rm comp}|\).

For the one-count test, all sums in (2.10) are finite.  Hence they may
be interchanged without convergence qualifications.  The half-open
\(A,D,K,G\) rules count each physical atom exactly once.  For each
fixed \(G\), (2.7)--(2.8) sum all annular members, the terminal member,
and the centre atom with the exact signs.  Thus no factor equal to the
number of dyadic blocks is introduced.  The map

\[
 (a,b,g)\longmapsto(h,s)=(ga,gb)
\tag{3.7}
\]

is a bijection between primitive odd rays with odd lifts and ordered
odd pairs \(h<s\): its inverse is
\(g=(h,s)\), \(a=h/g\), \(b=s/g\).  It preserves
\(a<b<4a\), and

\[
 \chi _4(ga)\chi _4(gb)
 =\chi _4(g)^2\chi _4(a)\chi _4(b)
 =\chi _4(h)\chi _4(s).
\tag{3.8}
\]

The accepted one-sided Poisson one-count then recombines the complete
tagged \(k\)-atoms into the exact integer \(m\)-sum in (2.3b).  Original
Poisson-zero, endpoint, equality, collar, nonstationary, and transform
error packets are the already bounded physical owner packet; the
metric density in (2.9) is never identified with that original zero
mode.  An entirely assumption-free way to certify the physically
relevant conclusion is to compare the two accepted energy identities
(2.4) and (3.2).  Since the Round-75 diagonal is an accepted owner and
\(0\le\mathcal D_L\ll_\varepsilon T\), subtraction gives the exact
constant

\[
 \boxed{
 \Re(\mathfrak C_L^{\rm comp}-\mathfrak C_L^{\rm off})
 ={\mathcal D_L-
    \widetilde{\mathcal E}_{{\rm owned},L}\over2}.}
\tag{3.9}
\]

Equations (3.3) and (3.9) prove (1.3).  Notice that the available input
proves (3.9), not
\(|\mathfrak C_L^{\rm comp}-\mathfrak C_L^{\rm off}|\ll T\); an
uncontrolled imaginary correction is irrelevant to the energy but may
not be silently bounded.

Formula (2.3c) retains the original capacity exactly.  The map
\((h,s)\leftrightarrow(h,r_{\rm row})\) is a bijective reindexing, changes
no coefficient or support, and (2.4) says

\[
 2\Re\mathfrak C_L^{\rm off}=\mathcal E_L^{\rm top}-\mathcal D_L.
\tag{3.9a}
\]

Since \(\mathcal D_L\) is only target-sized, an upper bound for the
one-sided real part of (2.3c) is equivalent to the original hard-energy
bound.  The visible factor \((-1)^{r_{\rm row}}\) therefore records the
actual character but, without an actual-symbol cancellation estimate,
does not reduce positive capacity.

The surviving two-character form can also be written exactly on
primitive rays.  Put \(b=a+2q\), and zero-extend

\[
 \begin{aligned}
 F_{L,a}(q)={}&1_{q\ge1}\,1_{(a,a+2q)=1}\!
 \sum_{\substack{g\;{\rm odd}\\ga,g(a+2q)\in\mathscr H_L}}
 \sum_{m=\lceil g(a+2q)/4\rceil}^{ga}
 a_{\rm end}(ga,m)\\
 &\quad\times\overline{a_{\rm end}(g(a+2q),m)}
 e\!\left(J(\sqrt{ga}-\sqrt{g(a+2q)})\sqrt m\right).
 \end{aligned}
\tag{3.10}
\]

Then \(\chi _4(a)\chi _4(a+2q)=(-1)^q\), so

\[
 \mathfrak C_L^{\rm off}
 =\sum_{a\;{\rm odd}}\sum_{q\in\mathbb Z}(-1)^qF_{L,a}(q).
\tag{3.11}
\]

Pairing adjacent integers on the finite zero-extended sequence gives
the exact smaller signed presentation

\[
 \boxed{
 \mathfrak C_L^{\rm off}
 =\sum_{a\;{\rm odd}}\sum_{r\in\mathbb Z}
 \bigl(F_{L,a}(2r)-F_{L,a}(2r+1)\bigr).}
\tag{3.12}
\]

Therefore the actual-symbol adjacent-variation estimate

\[
 \sum_{a,r}|F_{L,a}(2r)-F_{L,a}(2r+1)|
 \ll_\varepsilon L^2X^\varepsilon
\tag{3.13}
\]

would suffice.  This is strictly weaker than taking absolute values of
the two adjacent rays separately, but it is not proved here and is not a
Gram lift.  Equations (3.9)--(3.12) show that it is a reformulation of
the original signed correlation, not an independently gained
positive-power subrange.

## 4. First doubtful or unproved step

The first unproved step is (1.1), equivalently a target bound for the
real part of (2.3b), or the stronger adjacent-difference estimate
(3.13).  Exact completion supplies no estimate for it.

In (3.12), shifting \(q\) by one changes \(b=a+2q\), the coprimality
mask, the exact lift set, the ceiling \(\lceil g(a+2q)/4\rceil\), the
open reciprocal interval, its equality atoms, the stationary phase,
the collars and entry/exit profiles, and the locations of exact and near
metric centres.  Hence there is no accepted bounded-variation estimate
for \(F_{L,a}(q+1)-F_{L,a}(q)\).  Replacing these moving data by a common
box, deleting birth/death atoms, or evaluating a collar at a formal
saddle would change the actual symbol.

The one-count collapse is therefore a rigorous no-go for treating the
global completed scalar as a new transform gain: after every legitimate
partition is summed, its real part is the original Round-75
off-diagonal energy up to a target-sized packet.  No strict
positive-power residual range is proved.  The already accepted
\(q=1\), prescribed-polylogarithmic \(q\), square-ray, exact-centre,
positive-safe, endpoint, collar, and nonstationary families remain
target-sized owners; near-centre residual atoms outside those owners
remain in (3.10).

## 5. Required control test and outcome

1. **Real part, modulus, blockwise absolute value, and Gram.**  The
   implication uses only the upper real part.  The finite scalar
   \(C=iM\) has \(\Re C=0\) and \(|C|=M\), while two blocks
   \(Q_1=M,Q_2=-M\) have \(|Q_1+Q_2|=0\) and
   \(\sum|Q_j|=2M\).  Thus neither stronger norm is necessary.  A
   positive Gram is phase-invariant: the vectors \((1,1)\) and
   \((1,-1)\) have the same squared norm but different pairing with the
   alternating vector.  The fixed-\(a\) Gram additionally cancels the
   primitive character identically, so it does not imply (1.1) without
   a new directional-to-energy bridge.  **Outcome: pass.**
2. **Energy positivity and owned sign.**  No positivity is assigned to
   \(\widetilde{\mathcal E}_{\rm owned}\); its absolute bound is used.
   Positivity of \(\mathcal E_L^{\rm top}\) gives only (3.6), not the
   needed upper bound.  **Outcome: pass.**
3. **Orientation and factor two.**  Formula (2.3b) uses only \(h<s\),
   equivalently \(a<b\), and (2.4) has exactly one outer \(2\Re\).
   Adding \(s<h\) inside the scalar would double count.  **Outcome:
   pass.**
4. **Finite interchange and one-count.**  All atom spaces are finite;
   half-open \(A,D,K,G\) labels are one-count, and the \(R\)-sum is the
   exact telescope (2.7), not an absolute dyadic sum.  A block-dependent
   coefficient remains under \(\sum_B\Pi_B\).  **Outcome: pass, with no
   logarithmic loss.**
5. **Zero modes, terminal member, and exact centre.**  The original
   Poisson-zero tag and metric Fourier density \(r=0\) are distinct.
   The terminal \(V_{G_*}\) remains.  The punctured identity subtracts
   \(1_{t\in\mathbb Z}\) once, and completed reinsertion adds it once as
   in (2.8).  **Outcome: pass.**
6. **Floors, stars, collars, entry/exit, and zero extension.**  They are
   retained in \(a_{\rm end}\), \(A_B^\circ\), and
   \(\omega_B^{\rm act}\); (2.3b) keeps
   \(m=\lceil s/4\rceil\), and empty/singleton fibres are literal.
   **Outcome: pass.**
7. **\(q=1\), square, Pell, fourth-power, exact/near centres.**  The
   one-count owner priority is not altered.  Primitive square rays
   (including fourth-power subfamilies), their Pell-type centre
   phenomena, exact nonsquare centres, and \(q=1\) remain assigned once
   to the accepted target-sized packet.  Nonowned near centres remain
   in the hard sequence and are not declared negligible.  **Outcome:
   pass.**
8. **False unsigned and phase-conjugating models.**  Removing
   \(\chi _4(h)\chi _4(s)\) turns (3.11) into an unsigned correlation.
   In the bounded control model
   \(a^\#(h,m)=\chi _4(h)e(-J\sqrt{hm})\) on the same support, every row
   summand is nonnegative and coherent, so the off-diagonal correlation
   has full positive capacity.  This does not model the Vaaler symbol;
   it proves that character notation alone cannot establish (1.1).
   Any proof must use a property of the actual coefficient that excludes
   this phase-conjugating behaviour.  **Outcome: proposed automatic
   character cancellation fails, as required.**
9. **Transform self-return and downstream scope.**  Equation (3.9) is
   the explicit self-return.  No Gaussian functional calculus, second
   Poisson step, scalar Plancherel, or coefficient-blind spacing estimate
   is invoked.  Nothing here estimates either smooth M2 packet or any M1
   packet.  **Outcome: pass.**

## 6. Dependencies and exact artifacts used

The derivation uses only the following assigned artifacts:

- `protocol.md`;
- `state/proof_obligations.yml`, at the nodes
  `M9-M2-blockwise-linear-owner-completion`,
  `M9-M2-primitive-ray-fixed-a-actual-Gram`, and
  `M9-M2-top-endpoint-density-discrepancy-energy`;
- `state/active_campaign.yml` for Round 110;
- `rounds/codex-managed/m9-m2-global-signed-completed-directional/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-global-signed-completed-directional/candidates/conductor_global_signed_kernel.md`;
- `rounds/codex-managed/m9-m2-blockwise-owner-completion/synthesis.md`;
- `rounds/codex-managed/m9-m2-blockwise-owner-completion/reviews/conductor_round109_adjudication.md`;
- `rounds/codex-managed/m9-canonical-core-formalization/candidates/conductor_canonical_core_statements.md`;
- `rounds/codex-managed/m9-canonical-core-formalization/synthesis.md`;
- `rounds/codex-managed/m9-m2-metaplectic-two-character-energy/synthesis.md`.

No external theorem, web source, sibling Round-110 report, or numerical
experiment is used.  The proof is finite algebra plus the already accepted
one-count, owner, and physical row identities.

## 7. Recommended state effect

**Retain the analytic obligations open; revise the interpretation of the
candidate.**  The conductor may promote, after seam review, the narrow
formal statement (3.2)--(3.6) that the one-sided real-part estimate is the
necessary-and-sufficient scalar hard-energy target, and record (3.9) as a
self-return obstruction: global \(A,D,K,G,R\) completion recovers the
original Round-75 alternating off-diagonal correlation in real part, up to
the target-sized owned packet.

Do not promote an estimate for \(\mathfrak C_L^{\rm comp}\), (3.13), the
fixed-\(a\) Gram, the hard cone, either smooth M2 packet, \(M9\!-!M2\),
\(M9\!-!M1\), endpoint uniformity, \(M9\), or the quarter exponent.  The
smallest live direct object remains the actual signed off-diagonal
correlation (2.3b), equivalently its exact adjacent-ray presentation
(3.12).
