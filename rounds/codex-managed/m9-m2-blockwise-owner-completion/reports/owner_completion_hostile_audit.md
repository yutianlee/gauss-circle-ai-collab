# Round 109 hostile audit: owner normalization and fixed-K completion

## 1. Result: conditional owner lemma and no-go for the candidate as written

The proposed full completion is **not certified as written**.  The first
failure is literal rather than asymptotic: neither
\(\mathfrak Q_B^{\rm comp}\) nor the atoms
\(\mathfrak O_{B,\nu}\) are defined, the punctured \(R\)-partition is not
given as an exact reconstruction formula, and the block index is said to
contain both orientations while (C109.1) also places one outer \(2\Re\)
around the block sum.  In the accepted Round-77/78 normalization one sums
only \(a<b\) and the single outer \(2\Re\) supplies the conjugate
orientation.  Summing two full orientation blocks under the same
\(2\Re\) doubles the off-diagonal energy unless each orientation has an
explicit half weight.  Thus (C109.1), and hence (C109.2), is not yet a
literal identity.

There is, however, no surviving *quantitative* owner obstruction once the
dictionary is repaired.  In particular, the apparent Round-78 obstruction
from putting absolute values outside the \(R\)-blocks can be removed for
the **existing smooth punctured metric windows**.  If

\[
 S_{g,R}^{\square}
 =\sum_{k\in I_{s,u}}B_g(k)e(-gXu^2/k)
       W_R(2Xu^2/k),
\]

then Fourier expansion of \(W_R\) changes the reciprocal phase to
\(-(g-2\nu)Xu^2/k\).  Since \(g\) is odd,
\(n=|g-2\nu|\geq1\).  Round 78 sampled-\(k\) BV together with the two
Fourier half-moments certified in Rounds 103--104 gives

\[
 |S_{g,R}^{\square}|\ll_\varepsilon (L+1)X^\varepsilon
\tag{109.H1}
\]

uniformly for \(1\leq R\leq N_{s^2,t^2}\ll G\).  Summing actual square
triples and dyadic tags is \(O_\varepsilon(L^2X^\varepsilon)\).
The puncture does not own exact centres.  They form a separate square
atom; for real \(X\) its blockwise absolute scalar sum is also
target-safe by divisor counting, as proved in Section 3.

The proposed follow-up reconstruction with finitely many smooth annuli and
the hard terminal interval
\(W_{\mathrm{deep},N}=1_{\{\|t\|\leq c/N\}}\) exposes one further
literal seam.  A finite sum of smooth annuli supported only above
\(c/N\) is continuous at that boundary and therefore cannot equal the
discontinuous complement \(1-W_{\mathrm{deep},N}\).  Half weights repair
the value at the tie, not the missing one-sided neighborhood.  The three
suggested terminal estimates are nevertheless valid **conditional on an
exact partition**.  The lawful exact repair is to define the terminal
multiplier as the remainder \(V_N=1-\sum_R W_R\), and then use
\(V_N-1_{t\in\mathbb Z}\) on the scalar punctured set.  This remainder
has the same target-sized square and short-row estimates as the proposed
hard interval.

The stronger smooth telescoping construction supplied in the follow-up
**does close this punctured seam**.  Take a fixed nonincreasing smooth
\(\eta\), equal to one on \([0,1/2]\) and zero on \([1,\infty)\), put
\(V_R(t)=\eta(R\|t\|)\), and
\(W_R=V_R-V_{2R}\).  For dyadic \(G_*\asymp G\),

\[
 1_{t\notin\mathbb Z}
 =\sum_{1\leq R<G_*}^{\rm dyadic}W_R(t)
   +V_{G_*}(t)-1_{t\in\mathbb Z}
\tag{109.H1a}
\]

pointwise.  The telescoping sum is \(V_1-V_{G_*}\), and
\(V_1\equiv1\) because \(\|t\|\leq1/2\).  All annuli and the terminal
\(V_{G_*}\) are smooth Fourier-scale multipliers with the same uniform
half-moments used in (109.H1).  Thus the hard-interval seam is a no-go for
that particular construction, not an obstruction to the smooth
telescoping replacement.

Consequently the strongest result of this audit is the following.

*Conditional blockwise owner lemma.*  Fix the positive orientation
\(a<b\), one outer \(2\Re\), half-open dyadic lattices, an exact
punctured-metric reconstruction with a separate exact-centre atom, a fixed
half-open \(\rho\)-boundary, a fixed prescribed polylogarithmic short-row
cutoff, and the owner priority in Section 2.  Let the physical completion
mean only zero extension of the **same complete collared coefficient**;
do not delete its moving collar factors.  Then every named Round-77,
Round-78, Round-79, Round-103, and Round-104 scalar owner satisfies

\[
 \sum_{B,\nu}|\mathfrak O_{B,\nu}|
 \ll_\varepsilon L^2X^\varepsilon .
\tag{109.H2}
\]

These additional hypotheses are not present in the conductor candidate, so
(109.H2) does not promote (C109.2)--(C109.3) as currently stated.

A weaker route is logically sound and should be distinguished from the
strong gate.  Once an exact orientation-normalized aggregate identity

\[
 S_{\rm res}=S_{\rm comp}-O_{\rm agg}
\tag{109.H3}
\]

is written, a new direct theorem
\(|S_{\rm comp}|\ll_\varepsilon L^2X^\varepsilon\), together with the
accepted aggregate scalar owner bounds, is sufficient for the energy.
It does **not** require \(\sum_B|\mathfrak Q_B^{\rm comp}|\) or
\(\sum_{B,\nu}|\mathfrak O_{B,\nu}|\).  The Round-75 diagonal remains a
separate positive \(O(L^2)\) term.  This weaker conclusion is unavailable
until (109.H3) is literal, and no direct theorem for \(S_{\rm comp}\) is
proved here.

## 2. Exact statement and hypotheses

Use \(e(z)=e^{2\pi iz}\), \(J=X^{1/2}\),
\(1\leq L\leq J^{1/2}\), primitive odd \(a<b<4a\),

\[
 q={b-a\over2},\qquad
 \Lambda={X(\sqrt b-\sqrt a)^2\over2},\qquad
 {J(\sqrt b-\sqrt a)\over2\sqrt a}<k<
 {J(\sqrt b-\sqrt a)\over\sqrt b},
\tag{109.H4}
\]

and the complete Round-77 centred coefficient, including the actual
profiles, floors, stars, fixed smooth physical collars, finite odd-lift
support, and saddle entry/exit.  A fixed dyadic \(k\)-lattice is taken
half-open, for example \([K,2K)\cap\mathbb Z\).  Equality in either
endpoint of (109.H4) is not stationary residual mass; it is a Round-77
equality-mode atom.

The exact normalization required by the accepted transposed energy is one
of the following two, but not a mixture:

1. sum only the positive offset \(a<b\), and put one outer \(2\Re\);
2. sum both ordered orientations, put no outer \(2\Re\), and give each
   conjugate its literal coefficient.

This report uses the first convention.  If an orientation tag \(\sigma\)
is retained for bookkeeping, only one representative is summed; an
alternative two-tag convention must attach weight \(1/2\) to each tag
under the outer \(2\Re\).

For a genuine full owner partition, use the following one-count priority.
Writing \(P_j\) for the indicated predicate, define the \(j\)-th owner as
\(P_j\prod_{i<j}(1-P_i)\).  Thus overlap of verbal descriptions never
causes duplicate ownership.

| Priority | Literal owner predicate and normalization |
|---:|---|
| 0 | The Round-75 diagonal.  It is a positive energy term and is not an oriented \(\mathfrak O_{B,\nu}\). |
| 1 | Round-77 full lattice endpoint samples with their star half weights, removed primal collar samples, original Poisson zero and positive modes, negative equality/wrong-sign/nonstationary modes, and the pieces actually removed at saddle entry/exit.  Retained stationary collar transitions remain inside \(\mathfrak C^\circ\). |
| 2 | The retained stationary primitive square ray \(a=s^2,b=t^2\), including its separate exact-square-centre subatom and its smooth punctured \(R\)-subatoms. |
| 3 | Retained stationary primitive **nonsquare** exact centres \(\Lambda/k\in\mathbb Z\). |
| 4 | Retained stationary, nonsquare, nonexact positive-safe blocks on the chosen half-open side \(\rho_B\leq\rho_0\), where \(\rho_0\) is the fixed constant licensed by the Round-79 capacity proof.  Equality belongs here; the residual side is \(\rho_B>\rho_0\). |
| 5 | The remaining hard singleton row \(q=1\), with all priorities 1--4 still excluded, in the exact Round-103 block normalization. |
| 6 | The remaining hard rows \(2\leq q\leq (\log(2+X))^C\), for one fixed prescribed \(C\), in the exact Round-104 normalization.  Half-open dyadic \(q\)-shells are used. |
| 7 | The residual: none of priorities 1--6. |

The metric split must be written as an exact identity of the form

\[
 1_{\theta\notin\mathbb Z}
 =\sum_{R\in\mathcal R(g)}W_R(\theta),
 \qquad \theta={\Lambda\over k},qquad
 W_R(0)=0,qquad 1\leq R\leq N_{a,b}\ll G,
\tag{109.H5}
\]

with its periodic endpoint convention.  Formula (109.H5) is the required
punctured part; \(1_{\theta\in\mathbb Z}\) is owned before it.  The words
``punctured metric partition'' do not by themselves state (109.H5).

For the proposed terminal construction, put
\(E(t)=1_{\{t\in\mathbb Z\}}\) and
\(A_N(t)=\sum_{R\in\mathcal R_N}W_R(t)\), where the sum contains the
finite smooth annuli above \(c/N\).  The exact repair is

\[
 V_N(t):=1-A_N(t),\qquad
 1_{t\notin\mathbb Z}=A_N(t)+V_N(t)-E(t).
\tag{109.H5a}
\]

If one insists on the hard interval
\(W_{\mathrm{deep},N}=1_{\{\|t\|\leq c/N\}}\), the additional
transition correction

\[
 C_N(t)=1-A_N(t)-W_{\mathrm{deep},N}(t),\qquad
 V_N=W_{\mathrm{deep},N}+C_N
\tag{109.H5b}
\]

is mandatory.  A finite sum \(A_N\) of smooth annuli cannot equal the
discontinuous function \(1-W_{\mathrm{deep},N}\): if all annuli vanish
for \(\|t\|<c/N\), continuity forces their sum to tend to zero at the
boundary from above, whereas exact reconstruction requires it to be one
immediately above.  Fixed half weights determine the value at the tie but
do not repair that neighborhood.  Thus the hard interval alone does not
establish (109.H5); the remainder (109.H5a), or equivalently the correction
(109.H5b), does.

The preferred literal realization of (109.H5a) is the smooth telescoping
family from (109.H1a).  Choose \(G_*=2^m\asymp G\) on the dyadic lift
block and set

\[
 A_{G_*}=\sum_{j=0}^{m-1}(V_{2^j}-V_{2^{j+1}})
 =1-V_{G_*},\qquad V_{G_*}=1-A_{G_*}.
\tag{109.H5c}
\]

At \(t\in\mathbb Z\), every annulus vanishes and \(V_{G_*}(t)=1\), so
the separate atom \(E(t)\) cancels the terminal value exactly.  For
\(R\geq2\) and every fixed \(M\), smoothness and scaling give

\[
 |\widehat V_R(\nu)|+|\widehat W_R(\nu)|
 \ll_M R^{-1}(1+|\nu|/R)^{-M};
\tag{109.H5d}
\]

\(R=1\) is a fixed harmless profile.  In particular the mean is
\(\asymp R^{-1}\), the Fourier \(\ell^1\)-norm is \(O(1)\), and the
terminal \(V_{G_*}\) satisfies the same two half-moment estimates as an
annulus with \(R=G_*\).

For the existing smooth \(W_R\), the Round-103/104 proof records, uniformly
for odd \(g\asymp G\),

\[
 \sum_{\nu\in\mathbb Z}|\widehat W_R(\nu)|
       |2\nu-g|^{1/2}\ll_\varepsilon X^\varepsilon G^{1/2},
\qquad
 \sum_{\nu\in\mathbb Z}|\widehat W_R(\nu)|
       |2\nu-g|^{-1/2}\ll_\varepsilon X^\varepsilon G^{-1/2}.
\tag{109.H6}
\]

These are accepted properties of the complete smooth periodic factor,
including the nearest modes to \(g/2\) and the remote tail.  They are not
properties of a sharp metric annulus or an arbitrary pair mask.

Finally, ``physical completion'' has two inequivalent meanings.  Since the
complete collared coefficient is smoothly zero-extended, replacing its
displayed integral by an integral over \(\mathbb R\) is an exact change of
notation.  Removing the factors
\(\rho(g(u-b/4)/M)\rho(g(a-u)/M)\), or replacing them by one fixed
uncollared range, creates a new pair-dependent transition integral.  No
permitted accepted theorem estimates that new complement.  The conditional
lemma permits only the first meaning.

## 3. Proof and owner-by-owner derivation

### Round 77: absolute mode/collar owner and fixed-\(K\) zero extension

For each ordered physical pair, Round 77 proves the absolute estimate

\[
 \sum_{\nu\geq0}|I_\nu(h,s)|+
 \sum_{\substack{k\geq1\\k\notin(D(h),D(s/4))}}
 |I_{-k}(h,s)|\ll \log(2X),
\tag{109.H7}
\]

and the removed primal collars and two starred endpoint samples have total
absolute capacity \(O(L^2)\).  There are \(O(L^2)\) ordered pairs.  Hence
the complete Round-77 atom is \(O(L^2\log(2X))\) after absolute values.
Any disjoint dyadic subdivision, either orientation convention above, and
multiplication by the bounded smooth \(W_R\) can only preserve this bound
up to logarithmic/fixed factors.  This is genuinely stronger than a signed
aggregate theorem.

It also gives the exact fixed-\(K\) complement: within a half-open lattice
\([K,2K)\cap\mathbb Z\), add the negative modes outside the strict interval
(109.H4), including equality, and subtract precisely those terms using
(109.H7).  Original Poisson \(\nu=0\) is included in (109.H7).  The metric
Fourier density \(\widehat W_R(0)=\mu_R\) is not that mode and remains in
the completed coefficient.  Retained stationary modes crossing a smooth
collar remain exact centred integrals and are not subtracted a second time.

### Round 78: punctured \(R\)-resolved square owner

Let \(a=s^2,b=t^2,t=s+2u\), \((s,u)=1\), and
\(K=Ju/s\).  On any subinterval of the strict reciprocal interval, Round
78 gives

\[
 \sup_k|B_g(k)|+\operatorname {Var}_k B_g(k)
 \ll_\varepsilon X^\varepsilon t\sqrt{g/K}.
\tag{109.H8}
\]

After expanding the smooth metric factor, the \(\nu\)-th phase is
\(f_{\nu,g}(k)=-(g-2\nu)Xu^2/k\).  Put
\(n=|g-2\nu|\geq1\).  Weighted second-derivative summation and (109.H8)
give

\[
 \left|\sum_kB_g(k)e(f_{\nu,g}(k))\right|
 \ll_\varepsilon X^\varepsilon
 \left(st\sqrt{gn}+{t\over s}\sqrt{g/n}\right).
\tag{109.H9}
\]

Indeed \(|f''|\asymp nXu^2/K^3\), and the two terms in the standard
second-derivative bound become the two displayed terms after
\(K=Ju/s\).  The remote Fourier tail is included in (109.H6), so no
unproved restriction \(n\ll g\) is being used.  Summing (109.H9) with
\(|\widehat W_R(\nu)|\), then using (109.H6), \(g\asymp G\),
\(t/s\asymp1\), and \(gt^2\asymp L\), gives

\[
 |S_{g,R}^{\square}|
 \ll_\varepsilon X^\varepsilon
 \left(st\sqrt g\sqrt G+{t\over s}{\sqrt g\over\sqrt G}\right)
 \ll_\varepsilon X^\varepsilon(L+1).
\tag{109.H10}
\]

The accepted count of actual lifted square triples is
\(O(L\log(2L))\).  A strict square reciprocal interval has ratio less
than two, so it meets only \(O(1)\) ordinary dyadic \(K\)-blocks; all
other dyadic tags and the \(R\)-sum cost logarithms.  Triangle inequality
over rays and lifts therefore proves the punctured square contribution to
(109.H2).  This is a direct scalar theorem for the sharp mask
\(ab=\square\); no projective factorization of that mask is asserted.

### Exact square centres

At an exact square centre,

\[
 {2Xu^2\over k}=\ell\in\mathbb Z.
\tag{109.H11}
\]

If any such \(k\) exists, \(M=2Xu^2=k\ell\) is a positive integer;
otherwise the exact atom is empty.  Thus, for fixed \((s,u)\), all exact
\(k\)'s are divisors of \(M\), and their number is
\(O_\varepsilon(X^\varepsilon)\) since
\(M\ll XL\).  From (109.H8), one exact coefficient is

\[
 |B_g(k)|\ll_\varepsilon X^\varepsilon\sqrt{gt^2/K}
 \ll_\varepsilon X^\varepsilon {L^{3/4}\over J^{1/2}},
\tag{109.H12}
\]

where Round 78 gives \(K/L\gg J/L^{3/2}\).  Summing the
\(O(L\log(2L))\) actual lifted square triples yields

\[
 \sum_{\rm exact\ square\ atoms}|B_g(k)|
 \ll_\varepsilon X^\varepsilon {L^{7/4}\over J^{1/2}}
 \ll_\varepsilon L^2X^\varepsilon.
\tag{109.H13}
\]

This is already an outside-absolute estimate, is uniform for real \(X\),
and includes the perfect-fourth-power coherent control.  Reciprocal
endpoint equality is excluded by the strict interval and remains a
Round-77 atom.  The smooth punctured \(R\)-pieces and (109.H11) are
therefore disjoint and exhaustive only after (109.H5) is stated.

### Round 79: nonsquare exact centres and positive-safe blocks

The accepted nonsquare rigidity theorem gives at most one exactly
resonant primitive nonsquare ray at fixed \(X\), and its divisor modes
contribute \(O_\varepsilon(LX^\varepsilon)\) **absolutely**.  This is
stable under every dyadic split and is disjoint from (109.H11) by the
square-first priority.

For a positive-safe block the accepted positive capacity is

\[
 A\sqrt G\sqrt J\,D^{3/2}X^\varepsilon.
\tag{109.H14}
\]

Since \(G\asymp L/A\), the condition
\(AJD^3\leq \rho_0L^3\), with fixed \(\rho_0\), makes (109.H14)
\(O_{\rho_0}(L^2X^\varepsilon)\).  The proof is already positive and
\(R\)-resolved, so blockwise outside absolute values do not change its
normalization.  What is missing from the candidate is not an estimate but
the exact choice of \(\rho_0\) and the ownership of equality.  A verbal
\(\rho\ll1\)/\(\rho\gg1\) dichotomy is not a partition.

### Rounds 103--104: explicit energy-to-scalar bridges

Let the phase/orientation factor multiplying \(F_a(q)\) have modulus one.
On the singleton block, Round 103 gives

\[
 \sum_{a\asymp A}|F_a(1)|^2
 \ll_\varepsilon X^\varepsilon{L^4\over A}.
\]

Therefore the required oriented scalar owner obeys, on every active block,

\[
 \left|\sum_{a\asymp A}\epsilon_aF_a(1)\right|
 \leq A^{1/2}
 \left(\sum_{a\asymp A}|F_a(1)|^2\right)^{1/2}
 \ll_\varepsilon L^2X^\varepsilon.
\tag{109.H15}
\]

This is the missing normalization; the row-energy statement is not simply
renamed a scalar theorem.  Empty fibres contribute zero and singleton
reciprocal fibres are covered by the accepted supremum/zero-extension
argument.  Pell, near-square, and fourth-power \(q=1\) rows are included.

For a fixed dyadic \(q\)-shell, Round 104 gives

\[
 \sum_{a\asymp A,\ q\asymp D}|F_a(q)|^2
 \ll_\varepsilon X^\varepsilon {DL^4\over A}.
\]

Thus

\[
 \left|\sum_{a\asymp A,\ q\asymp D}
       \epsilon_{a,q}F_a(q)\right|
 \leq (AD)^{1/2}
 \left(\sum_{a,q}|F_a(q)|^2\right)^{1/2}
 \ll_\varepsilon DL^2X^\varepsilon.
\tag{109.H16}
\]

For one fixed prescribed range \(D\leq(\log(2+X))^C\), dyadic summation
absorbs this in \(L^2X^\varepsilon\).  It does not own a positive-power
shell.  Priority 5 removes \(q=1\) before priority 6, preventing duplicate
use of Rounds 103 and 104.  Both accepted row theorems retain the complete
smooth \(W_R\), collars, floors, stars, open reciprocal interval, and
zero extension.  They do not license reinsertion of a new jagged
\(k\)-mask.

### Follow-up audit: hard terminal multiplier and exact remainder

Put \(\delta_N=c_0/N<1/2\), and give the periodic interval multiplier
\(W_{\mathrm{deep},N}\) value one for \(\|t\|<\delta_N\), value
one-half at \(\|t\|=\delta_N\), and value zero outside.  Its Fourier
coefficients are

\[
 \widehat W_{\mathrm{deep},N}(0)=2\delta_N,
 \qquad
 \widehat W_{\mathrm{deep},N}(r)
 ={\sin(2\pi r\delta_N)\over\pi r}\quad(r\ne0).
\tag{109.H19}
\]

They are not in \(\ell^1\), and their positive half-moment diverges.
Therefore the smooth-window modewise argument (109.H6) does **not** apply
directly to the hard terminal interval.  Nevertheless the Round-108
functional calculus survives in its natural \(L^2\) meaning.  If
\(\kappa=X/(2gk)\), define

\[
 \mathcal M_{\mathrm{deep},N}
 =\mathcal F^{-1}M_{W_{\mathrm{deep},N}(\kappa y^2)}\mathcal F.
\tag{109.H20}
\]

Then \(\|\mathcal M_{\mathrm{deep},N}\|_{2\to2}\leq1\), uniformly in
\(N\).  If \(\sigma_M W_{\mathrm{deep},N}\) denotes the Fejér Fourier
mean, then

\[
 \sum_{r\in\mathbb Z}
 \left(1-{|r|\over M+1}\right)_+
 \widehat W_{\mathrm{deep},N}(r)T_{r\kappa}f
 \longrightarrow \mathcal M_{\mathrm{deep},N}f
 \quad\hbox{strongly in }L^2.
\tag{109.H21}
\]

Indeed the Fejér means are uniformly bounded, converge to the prescribed
half values at the two jumps, and converge to the interval value elsewhere;
dominated convergence on the Fourier side proves (109.H21).  This is not
operator-norm convergence and does not license absolute Fubini over
Fresnel modes.

The exact-centre set \(\{y:\kappa y^2\in\mathbb Z\}\) is countable and
hence null in the continuous \(L^2\) model.  Multiplication by its
indicator is therefore the zero \(L^2\) operator.  Exact-centre point
values cannot be recovered or subtracted by (109.H20); the atom \(E\)
must be handled in the discrete scalar sum before or after the functional
calculus.  With that separation, item (i) of the follow-up passes in
\(L^2\), but not as an absolutely convergent mode sum.

For square rays, let \(S_{B}^{\square,\mathrm{full}}\) be the exact
Round-78 square sum with metric multiplier one.  Let
\(S_{B,R}^{\square}\) be its smooth annular pieces and
\(S_B^{\square,\mathrm{exact}}\) its exact-centre atom.  The terminal
remainder in (109.H5a) has the exact scalar identity

\[
 S_B^{\square,\mathrm{term}}
 =S_B^{\square,\mathrm{full}}
  -\sum_R S_{B,R}^{\square}
  -S_B^{\square,\mathrm{exact}}.
\tag{109.H22}
\]

Round 78 bounds the full term without cancellation between distinct rays
or lifts, and its second-derivative estimate is uniform on every dyadic
\(K\)-subinterval.  Hence its outside-absolute block sum is
\(O_\varepsilon(L^2X^\varepsilon)\).  Equations (109.H10) and
(109.H13) give the same bound for the annuli and exact centres.  Triangle
inequality in (109.H22) proves item (ii) for \(V_N-E\).  It also proves it
for the proposed hard terminal only if the correction \(C_N\) in
(109.H5b) is included; omitting \(C_N\) is an algebraic gap, not a square
estimate.

For a fixed nonsquare row, replace the metric factor by the full multiplier
one.  Its Fourier expansion consists only of \(\nu=0\), so the carrier
frequency is \(n=g\), not zero.  The accepted Round-104 single-mode
calculation gives, for one lift,

\[
 \sqrt{ALg}+\sqrt{L/A}\,g^{-1/2}\ll L+1
 \qquad(g\asymp G\asymp L/A).
\tag{109.H23}
\]

Summing \(O(G)\) actual lifts yields

\[
 |F_a^{\mathrm{full}}(q)|
 \ll_\varepsilon X^\varepsilon {L^2\over A}.
\tag{109.H24}
\]

Thus the full \(q=1\) scalar block costs \(O(L^2X^\varepsilon)\), and a
prescribed \(q\asymp D\) shell costs
\(O(DL^2X^\varepsilon)\), hence is target-safe for fixed polylogarithmic
\(D\).  Subtracting the already controlled smooth annuli and the Round-79
absolute nonsquare exact-centre atom gives the same estimates for the
terminal remainder.  Square rows were removed at the earlier owner
priority.  Empty and singleton fibres cause no change.  This proves item
(iii) for \(V_N-E\) and, conditionally, for a hard terminal plus its
transition correction.

Accordingly, all three proposed analytic checks pass after the scalar
exact-centre atom is separated.  The literal formula with smooth annuli
plus the hard interval **alone** does not pass; its first failure is the
continuity/boundary correction in (109.H5b).  Defining the terminal block
as the exact remainder \(V_N\) closes the punctured reconstruction without
requiring a hard-multiplier Fourier half-moment.

### Algebraic and global-signed consequences

For actual scalar atoms \(c(\omega)\) and disjoint projectors
\(P_1,\ldots,P_6\), the identity

\[
 \sum_\omega\Bigl(1-\sum_{j=1}^6
 P_j\prod_{i<j}(1-P_i)\Bigr)c(\omega)
 =\sum_\omega c(\omega)-
 \sum_{j=1}^6\sum_\omega
 P_j\prod_{i<j}(1-P_i)c(\omega)
\tag{109.H17}
\]

is exact.  This is the algebra needed by (C109.2), but it is useful only
after the common atom space, weights, orientation, metric reconstruction,
and collar convention are written.  Smooth difference localization has
bounded Fourier \(L^1\)-cost, and the actual
\(a^{-3/4}b^{-3/4}\) factors make the Möbius cost
\(\sum_d d^{-3/2}<\infty\).  These costs apply to smooth projective
factors; (109.H10)--(109.H16), not an invented separation, control the
sharp pair owners.

If only the global signed theorem is sought, sum (109.H17) before taking
absolute values.  From

\[
 \mathcal E_L^\top=\mathcal E_{{\rm owned},L}
 +2\Re S_{\rm res},\qquad
 S_{\rm res}=S_{\rm comp}-O_{\rm agg},
\]

one gets

\[
 \mathcal E_L^\top
 \ll L^2X^\varepsilon+2|S_{\rm comp}|+2|O_{\rm agg}|.
\tag{109.H18}
\]

The accepted signed/absolute owner theorems and (109.H15)--(109.H16)
give \(|O_{\rm agg}|\ll L^2X^\varepsilon\).  Therefore a direct bound for
\(|S_{\rm comp}|\) would close this energy without the strong
outside-absolute gate.  This does not prove
\(\sum_B|\mathfrak Q_B^{\rm res}|\), and it gives no right to commute
owner projections through a Fejér operator or a positive Gram.

## 4. First doubtful or unproved step

The first unsupported implication is the passage from the verbal owner
list to (C109.1)--(C109.2).

1. **Orientation is not normalized.**  The candidate includes
   orientation in \(B\), asks for every conjugate orientation, and also
   uses one outer \(2\Re\).  Round 78 explicitly states that \(2\Re\)
   already counts the opposite orientation exactly once.  Without a
   one-orientation rule or half weights, even the starting energy identity
   is ambiguous by a factor two.
2. **The common atom space and projectors are absent.**  There is no
   formula specifying which Round-77 transition remains in
   \(\mathfrak C^\circ\), which one is removed, how square/exact/safe/short
   overlaps are prioritized, or how zero extensions attach to a block.
3. **The proposed hard terminal does not complement smooth annuli.**  The
   analytic square repair proves the norm for every existing smooth
   \(W_R\), and (109.H13) proves the exact-square atom, but continuity
   rules out \(A_N=1-W_{\mathrm{deep},N}\) for a finite smooth annular
   sum.  The correction \(C_N\), or the exact remainder \(V_N\), is
   required.  In continuous \(L^2\) the exact-centre atom is null and must
   still be restored at the discrete scalar level.
4. **The \(\rho=1\) and short-shell boundaries are verbal.**  Symbols
   \(\ll1\), \(\gg1\), and ``polylogarithmic'' do not give complementary
   projectors.  They must be replaced by a fixed half-open threshold and a
   fixed exponent \(C\).
5. **Physical completion is ambiguous.**  Zero extension of the same
   collared amplitude is exact and Round-77 controls the reciprocal-mode
   complement.  Erasing the moving collars or point-evaluating them at a
   noninteger stationary sample is a different operation with no accepted
   owner bound.

Thus no literal owner is the first quantitative failure: after the
R-resolved square repair every named norm has a lawful target-sized route.
The failure precedes those estimates, at the unprovided definition and
normalization of the completion itself.  If the completion is interpreted
as removing the collar multipliers, that new collar complement is the
first analytic residual.

The logical distinction between aggregate and blockwise norms remains
real.  For two abstract blocks, take
\(\mathfrak O_{B_1}=Z\), \(\mathfrak O_{B_2}=-Z\).  Then the aggregate
owner is zero while
\(\sum_B|\mathfrak O_B|=2|Z|\), arbitrarily large.  This finite model does
not obstruct the actual symbol; it proves only that (C109.3) cannot be
deduced from the accepted aggregate identity without the owner-specific
arguments above.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `owner_one_count_and_disjointness` | **Fail as written; conditional pass with the priority table.**  Square precedes nonsquare exact centres; exact precedes safe; safe precedes short rows; \(q=1\) precedes the remaining prescribed polylog shell.  Round-77 removed pieces come first, while retained stationary collar transitions stay in the coefficient. |
| `scalar_vs_energy_normalization` | **Pass only through explicit bridges.**  Equations (109.H15)--(109.H16) supply the exact Cauchy factors.  In general, \(N\) entries of size \(N^{-1/2}\) have energy one but scalar sum \(N^{1/2}\), so row energy cannot merely be renamed a scalar owner. |
| `blockwise_absolute_vs_signed_aggregate` | **Pass for the conditional ledger, fail as an inference from the aggregate theorem.**  Round 77 is absolute; Round 78 is upgraded by (109.H10) and (109.H13); Round 79 is absolute/positive; short rows use blockwise Cauchy.  The two-block countermodel in Section 4 proves the general nonimplication. |
| Terminal metric reconstruction | **Hard proposal fails literally; exact remainder passes.**  A finite smooth annular sum cannot complement a hard interval at \(c/N\).  With \(V_N=1-\sum_R W_R\), squares pass by (109.H22), short rows by (109.H23)--(109.H24), and exact centres remain separate.  The hard multiplier itself is lawful only as a strongly convergent bounded \(L^2\) functional calculus, not an absolutely summable Fresnel-mode expansion. |
| `fixed_K_completion_and_open_endpoints` | **Conditional pass.**  Use a half-open dyadic integer lattice and the same collared coefficient.  Strict reciprocal equality modes are Round-77 atoms.  No endpoint is sampled at a noninteger saddle. |
| `physical_collar_and_entry_exit` | **Pass for zero extension; fail for collar deletion.**  Removed primal collar samples are absolute Round-77 owners.  Stationary traversal of the retained smooth collar is part of \(\mathfrak C^\circ\).  Replacing that collar by an uncollared fixed range is unsupported. |
| `original_zero_mode_vs_metric_density` | **Pass.**  The original Poisson zero/positive modes belong to Round 77.  The metric \(\nu=0\) term is \(\mu_R\) inside \(W_R\); in the square repair it gives \(n=g\), and it is never subtracted as an original zero mode. |
| `sharp_pair_owner_projective_norm` | **Pass without false factorization.**  Smooth \(b-a\) and Möbius factors have the accepted summable costs.  Square, exact-centre, safe, and short-row masks are controlled by their direct scalar theorems, not assigned a fictitious projective norm. |
| `square_fourth_power_and_Pell` | **Pass.**  Perfect-fourth-power square coherence is included in the exact atom (109.H13).  On punctured \(R\)-pieces odd \(g\) forbids \(g-2\nu=0\).  Nonsquare Pell/near-square \(q=1\) rows are included in Round 103 and receive no derivative-gap shortcut. |
| `q1_polylog_and_empty_singleton` | **Pass with scope.**  Equation (109.H15) owns \(q=1\); (109.H16) owns only a fixed prescribed polylogarithmic range with \(q=1\) removed.  Empty fibres are zero and singleton fibres use the accepted supremum/zero extension.  No positive-power shell is claimed. |
| `exact_centre_and_rho_boundary` | **Exact centres pass; \(\rho\)-dictionary fails as written.**  Square exact centres satisfy (109.H13); nonsquare exact centres have the accepted \(O(LX^\varepsilon)\) absolute bound.  Equality at a fixed \(\rho_0\) must be assigned to the safe owner; \(\rho\ll1\)/\(\rho\gg1\) is not literal. |
| `orientation_floor_star_halfweight` | **Fail as written; repaired convention stated.**  Use \(a<b\) and one outer \(2\Re\).  Both physical endpoint half samples, ceiling strata, floors, and stars are Round-77 atoms once only.  Two full orientation tags under the same \(2\Re\) are forbidden. |
| `Fejer_commutator_and_Gram_nonimplication` | **Pass as a stopping control.**  The owner proof is scalar before a second Gram.  For a noncommuting projection \(P\) and Fejér/shift operator \(T\), \(TP\ne PT\) and cross terms remain.  No owner energy decomposition or transformed projective estimate follows from (109.H17). |
| `downstream_and_exponent_scope` | **Pass.**  No estimate is proved for the completed directional vector, the character-neutral cross-\(q\) Gram, either smooth M2 packet, M9-M2, M9-M1, endpoint uniformity, M9, or the Gauss-circle exponent. |

The fixed-\(R\) square calculation uses the accepted smooth Fourier
moments, not numerical experimentation.  No external theorem is imported.

## 6. Dependencies and exact artifacts used

Campaign: `m9-m2-blockwise-owner-completion`.  Task:
`owner_completion_hostile_audit`.  Role: hostile seam reviewer.  Starting
graph SHA-256:
`f861f43d46bec112682a73e4c6062cbebf82f83fdcf0639e6fe122c6a123ad0d`.

Only the assigned selected context was used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-blockwise-owner-completion/briefs/owner_completion_hostile_audit.md`;
- `rounds/codex-managed/m9-m2-blockwise-owner-completion/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-blockwise-owner-completion/candidates/conductor_blockwise_owner_completion.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reports/actual_symbol_hostile_audit.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/reports/square_resonance_hostile_audit.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/reports/nonsquare_resonance_hostile_source_audit.md`;
- `rounds/codex-managed/m9-m2-q1-actual-diagonal-energy/reviews/conductor_round103_owners_controls_and_sources.md`;
- `rounds/codex-managed/m9-m2-fixed-q-sampled-k-short-shell/reviews/conductor_round104_actual_symbol_and_owner_seam.md`;
- `rounds/codex-managed/m9-m2-metaplectic-two-character-energy/reports/two_character_spectral_source_hostile_audit.md`.

No Round-109 sibling report, shared proof draft, validation matrix, synthesis,
source card, web source, or numerical artifact was read.

## 7. Recommended state effect

**Revise and retain; do not promote the full completion identity yet.**

Record the following as candidate evidence after an independent seam check:

1. the smooth punctured-\(R\) square-owner lemma
   (109.H8)--(109.H10), based on the already accepted Round-103/104 Fourier
   half-moments;
2. the separate real-\(X\) exact-square-centre absolute bound
   (109.H11)--(109.H13);
3. the explicit scalar Cauchy bridges (109.H15)--(109.H16); and
4. the conditional owner priority and strong norm (109.H2); and
5. the terminal-complement estimates (109.H19)--(109.H24), with the
   distinction between strong \(L^2\) functional calculus and discrete
   exact-centre ownership.

Before any blockwise completion node is promoted, replace the conductor
candidate by a literal formula that fixes: one orientation plus one outer
\(2\Re\) (or the equivalent half-weight convention); the common scalar
atom space; half-open \(A,D,K,G,R\) ownership; the exact punctured identity
(109.H5) and separate exact atom; the terminal remainder
\(V_N=1-\sum_R W_R\) (or the explicit correction \(C_N\) if a hard
interval is retained); the safe \(\rho\)-threshold including
equality; the fixed short-row exponent \(C\); and the rule that physical
completion is zero extension of the unchanged collared coefficient.  A
claim that removes the collar multipliers requires a new owner estimate.

The smallest presently lawful survivor is the positive-orientation linear
completion at fixed half-open \(K\) using the unchanged zero-extended
collared coefficient and only the Round-77 nonstationary/equality
complement.  The sharp pair masks remain until the literal priority and
metric reconstruction are installed.

The conductor may also formulate a distinct, weaker global-signed
obligation: prove \(|S_{\rm comp}|\ll L^2X^\varepsilon\) after writing the
exact aggregate identity (109.H3).  That theorem would be sufficient for
the scalar energy with the Round-75 diagonal separate and would not need
the strong blockwise outside-absolute gate.  It must not be advertised as a
blockwise directional-vector theorem, a Fejér-commuting owner theorem, or a
positive-Gram decomposition.

Keep the completed directional estimate, fixed-a actual Gram, balanced and
unbalanced smooth M2 packet estimates, M9-M2, M9-M1, endpoint uniformity,
M9, and the exponent open.

### Short seam verdict on (109.M1)--(109.M5)

- **(109.M1), exact dyadic telescoping: YES.**  For dyadic
  \(G_*=2^m\), \(\sum_{j<m}(V_{2^j}-V_{2^{j+1}})+V_{G_*}=V_1=1\)
  pointwise.  Since every annulus vanishes and \(V_{G_*}=1\) at an exact
  centre, subtracting \(1_{t\in\mathbb Z}\) gives the literal punctured
  identity once, with no half-weight ambiguity.
- **(109.M2), smooth Fourier normalization and half-moments: YES.**
  Both \(W_R\) and the terminal \(V_{G_*}\) satisfy
  \(|\widehat V_R(\nu)|+|\widehat W_R(\nu)|
  \ll_MR^{-1}(1+|\nu|/R)^{-M}\).  Their means are \(\asymp R^{-1}\),
  and for odd \(g\asymp G\), \(R\leq G_*\asymp G\), the accepted
  positive and negative half-moments are respectively
  \(O(G^{1/2})\) and \(O(G^{-1/2})\).
- **(109.M3), Round-108 bounded functional calculus: YES, with the exact
  atom scalar.**  Smooth Fourier \(\ell^1\) convergence makes every
  annular and terminal operator lawful in operator norm.  The exact-centre
  indicator is null in continuous \(L^2\) and must be subtracted in the
  discrete scalar identity; it is not an \(L^2\) owner projector.
- **(109.M4), terminal square owner: YES.**  The terminal
  \(V_{G_*}\) obeys the same \(|2\nu-g|^{\pm1/2}\) moment proof as the
  smooth annuli, giving \(O_\varepsilon((L+1)X^\varepsilon)\) per lift.
  Equivalently it is the full Round-78 square sum minus the annuli; the
  exact-square atom (109.H13) is separately outside-absolute target-safe.
- **(109.M5), terminal \(q=1\) and prescribed polylog rows: YES.**
  Directly, the full multiplier one has only \(\nu=0\), hence
  \(n=g\ne0\), and gives (109.H23)--(109.H24); subtracting annuli and the
  Round-79 nonsquare exact atom is target-safe.  The same conclusion follows
  directly from the terminal \(V_{G_*}\) half-moments.  No positive-power
  \(q\)-shell is obtained.

**Verdict:** the smooth telescoping version closes the literal punctured
metric reconstruction.  The earlier no-go applies only to a hard terminal
interval paired with finitely many smooth annuli and no transition
correction.  Orientation under the outer \(2\Re\), the common owner atom
dictionary, the \(\rho\)-boundary, and any deletion of the physical collar
remain independent unresolved completion seams.
