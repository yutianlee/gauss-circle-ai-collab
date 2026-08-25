# Blind final review of the Round 148 conductor candidate

Campaign: m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate
Candidate: candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md
Role: hostile final seam reviewer

## 1. Result

**Verdict: AMBER.**  Four of the five repairs requested in the first
seam review are now substantially correct:

1. The finite progression set \(\mathcal P(d)\) in (148.C2a) repairs
   the missing \(\alpha\)-cutoff and makes (148.C4) a finite scalar.
2. The convention in (148.C14a) makes the Gaussian expansion an exact
   identity by definition and explicitly assigns the complementary
   Taylor-polynomial subtraction and extended-domain tail to the
   remainder.
3. The diagonal claim is now restricted to unrecombined
   progression-cell Cauchy followed by a separately nonnegative
   \(d\)-diagonal.
4. The candidate explicitly leaves the \(N\)-dependent phase
   congruences, every pre-Cauchy regrouping, and signed cross-cell
   cancellation outside the no-go.

The remaining promotion blocker is (148.C14b).  Its displayed second
line does not follow from the stated \(K=6\) Taylor expansion and six
integrations by parts:

- on a radial transition the order-\(K\) stationary Taylor remainder
  has relative scale \((M/\Lambda)^K\), not
  \((\sqrt M/\Lambda)^K\);
- on a cone transition it has scale \((D/\Lambda)^K\), not
  \((\sqrt D/\Lambda)^K\);
- a sixfold nonstationary integration-by-parts bound, when measured
  relative to the leading stationary capacity, carries the missing
  factor \(\Lambda^{1/2}\).

Thus (148.C14b), as written, does not prove the claimed
\(O_{\varepsilon,V}(X^\varepsilon)\) aggregate.  The intended
conclusion is nevertheless repairable: the correctly weakened terms
are still far below \(X^\varepsilon\) throughout
\(M\le R^2\), \(D\le R\).

There is also a smaller diagonal-seam omission.  Because
\(\mathcal P(d)\) depends on \(d\), (148.C18)--(148.C20) must select
an explicit common long-prefix rectangle and an
\(\alpha\)-subfamily which belongs to \(\mathcal P(d)\) for every
\(d\) in the common plateau.  The asserted \(c_0D\) lower bound is
plausible and elementary on such a rectangle, but it is currently an
assertion rather than a derivation.  The no-go should be stated for
that long interior prefix; no \(Q\sqrt E\) lower mass is asserted for
an arbitrarily short terminal prefix.

The source and downstream wording is appropriately scoped.  The file
is valid UTF-8, has no forbidden control byte, no trailing whitespace,
and ends in a newline.

## 2. Exact statement and hypotheses

Let

$$
 P_0:=X^\varepsilon R\sqrt D,\qquad
 \Lambda:=\sqrt{NM}=R^2\sqrt M.
\tag{F148.1}
$$

For a middle-range saddle, the \(r\)-th stationary coefficient has
the following absolute capacities:

$$
 P_0\left[
 \Lambda^{-r}
M^{-1/2}(M/\Lambda)^r
{\bf1}_{M\asymp D^2}D^{-1/2}(D/\Lambda)^r
 \right].
\tag{F148.2}
$$

Consequently the \(r=1\) contribution and all \(2\le r<6\) symbols
are target-safe exactly as claimed in (148.C14).  For \(K=6\), a
standard exact stationary remainder has the same expression with
\(r=6\):

$$
 P_0\left[
 \Lambda^{-6}
M^{-1/2}(M/\Lambda)^6
{\bf1}_{M\asymp D^2}D^{-1/2}(D/\Lambda)^6
 \right].
\tag{F148.3}
$$

If six integrations by parts are used on the nonstationary pieces,
their capacity relative to \(P_0\) is bounded schematically by

$$
 P_0\Lambda^{1/2}\left[
 \Lambda^{-6}
M^{-1/2}(\sqrt M/\Lambda)^6
{\bf1}_{M\asymp D^2}D^{-1/2}
       (\sqrt D/\Lambda)^6
 \right],
\tag{F148.4}
$$

after summing the dyadic \(q\)-tails.  Alternatively, seven
integrations by parts make a version of the candidate's displayed
sixth-power majorant valid after harmless weakening.  Equations
(F148.2)--(F148.4), together with the finite progression mass, are
the required corrected form of (148.C14b).

For the diagonal claim, the exact additional hypotheses should be
displayed.  Choose a long retained interior rectangle

$$
 \mathcal J_d\times\mathcal J_e,\qquad
 |\mathcal J_d|\asymp D,\quad |\mathcal J_e|\asymp E,
\tag{F148.5}
$$

on which the physical profile has modulus bounded below.  Select odd
squarefree \(\alpha\) with
\(\alpha^2\in\mathcal J_e\), take \(b=1\), and restrict
\(q/(\alpha^2Q)\) to a fixed interval for which
\(e_0(d,\alpha^2,q)\in\mathcal J_e\) for all
\(d\in\mathcal J_d\).  Then
\((\alpha,1)\in\mathcal P(d)\) via \(n=1\),
there are \(\asymp\sqrt E\) such \(\alpha\), and

$$
 \sum_{d\in\mathcal J_d}|a_{i,d}|^2\gg D
\tag{F148.6}
$$

uniformly after restricting to squarefree \(d\).  Under these explicit
hypotheses, (148.C19)--(148.C22) follow.

## 3. Proof and hostile derivation

### 3.1 Exactness of \(\mathcal P(d)\)

After (148.C8), moving \(b\mid d\) outside and putting
\(\ell=[\alpha^2,b]\) gives the exact finite sum

$$
 \sum_{\substack{\alpha,b\\b\mid d}}
 \mu(\alpha)\mu(b)
 \sum_{\substack{n\ge1\\
       \mathscr A(d,\ell n)\ne0}}
 \chi_4(\ell n)\,(\cdots).
\tag{F148.7}
$$

If the inner progression is empty, its contribution to the original
discrete sum is exactly zero and may be omitted before Poisson.
Otherwise \(\ell n\le e_+\) implies
\(\alpha^2\le\ell\le e_+\).  Thus (148.C2a) is neither an
analytic truncation nor a favorable support assumption: it is the
literal finite index set inherited from (F148.7).  Conversely, every
original \((\alpha,b,e)\) term appears with
\((\alpha,b)\in\mathcal P(d)\) and \(e=\ell n\).
This closes the previous infinite-\(\alpha\) defect.

The dependence of \(\mathcal P(d)\) on \(d\) is harmless for the
transform identity, but it matters for the later common-cell diagonal
argument and motivates (F148.5)--(F148.6).

### 3.2 The (148.C14a) convention

For \(q>0\), define \(\mathcal R_K\) to be the exact difference
between \(I_{d,\ell,q}\) and the displayed \(K\)-term full-Gaussian
series.  With an even cutoff, the cutoff proof decomposes the difference
into the localized Taylor remainder, the complementary polynomial
subtraction, and the full-line/domain tail.  This is precisely the
correction missing from the discovery report.  Damped full Gaussian
moments give the same coefficients before the damping is removed.
For \(q\le0\), assigning the whole integral to
\(\mathcal R_K\) is also exact.  Therefore (148.C14a) passes as an
identity.

Exact definition alone does not bound \(\mathcal R_K\); that task is
the separate content claimed in (148.C14b).

### 3.3 Why (148.C14b) is not the displayed bound

On a radial transition,
$$
 H^{(2r)}(0)\ll_r M^r,
$$
because each \(u\)-derivative costs \(M^{1/2}\).  Hence the
\(r\)-th stationary term is
\(M^{-1/2}(M/\Lambda)^r\) after the transition-support fraction is
inserted.  The order-\(12\) Taylor remainder for \(K=6\) has the
same scale with \(r=6\), which is (F148.3).  The candidate instead
uses \(M^{-1/2}(\sqrt M/\Lambda)^6\), smaller by \(M^3\).
The identical calculation on a cone transition replaces \(M\) by
\(D\), so the displayed cone remainder is smaller than the natural
Taylor bound by \(D^3\).

For a nonstationary integral, the unintegrated oscillatory integral is
\(\asymp\Lambda^{1/2}\) times the leading stationary unit: stationary
phase itself supplies a factor \(\Lambda^{-1/2}\).  Six integrations
by parts in a dimensionless variable therefore give the relative
factor

$$
 \Lambda^{1/2}(S/\Lambda)^6,\qquad
 S\in\{1,\sqrt M,\sqrt D\},
\tag{F148.8}
$$

not merely \((S/\Lambda)^6\).  In the two \(q\)-tails, one should use
the scaled coordinate \(y=\ell x/E\); then
$$
 |\partial_y\phi|\gg
 \Lambda\left(1+\frac{|q|}{\ell Q}\right)
\tag{F148.9}
$$
on the appropriate dyadic pieces.  This records the factors which are
hidden if the \(x\)-derivative lower bound and dimensionless amplitude
derivatives are written in the same sentence.

These corrections do not threaten target-safety.  The \(r=1\) terms
are

$$
 P_0\Lambda^{-1}=\frac1{R\sqrt E},\qquad
 P_0M^{-1/2}\frac M\Lambda=\frac{\sqrt D}{R},\qquad
 P_0D^{-1/2}\frac D\Lambda=\frac1R
\tag{F148.10}
$$

in the cone case \(M\asymp D^2\).  Every term in (F148.3) gains five
additional factors at most \(R^{-1}\), \(R^{-2}\), or
\(\Lambda^{-1}\).  For (F148.4),
\(\sqrt M/\Lambda=R^{-2}\), and the worst corrected contribution is
still a negative power of \(R\).  Thus a corrected summed lemma would
prove \(O_{\varepsilon,V}(X^\varepsilon)\), but (148.C14b) does not
yet constitute that lemma.

It must also display the finite-mass summation

$$
 \sum_d\sum_{(\alpha,b)\in\mathcal P(d)}
 \frac1\ell\#\{q\asymp\ell Q\}
 \ll DQ\sqrt E\,X^\varepsilon
\tag{F148.11}
$$

and the geometric decay from dyadic upper and negative \(q\)-tails.
Those facts make the corrected powers summable; they are only described,
not derived, in the candidate.

### 3.4 Common plateau and the diagonal scope

Given (F148.5), choosing \(\alpha^2\in\mathcal J_e\) ensures
literal membership in \(\mathcal P(d)\) for every selected \(d\).
The odd squarefree \(\alpha\)'s have positive density in the
corresponding interval of length \(\asymp\sqrt E\), while squarefree
\(d\)'s have positive density in \(\mathcal J_d\).  Restricting
\(q/(\alpha^2Q)\) to a common compact interval gives
\(\asymp\alpha^2Q\) frequencies per \(\alpha\).  It follows that

$$
 \sum_i|c_i|\asymp Q\sqrt E,\qquad
 \sum_{d\in\mathcal J_d}|a_{i,d}|^2\gg D.
\tag{F148.12}
$$

Weighted Cauchy and a separately positive \(d\)-diagonal then give
the valid capacity \(Q\sqrt M=\sqrt N\,D\).  This proves only the
early, unrecombined cellwise placement.  A long interior prefix is
enough to falsify that placement as a uniform proof menu; the same
lower mass is not claimed for every short terminal prefix.

The repaired candidate correctly observes that equality of reduced
fractions is not the full alignment condition.  The exact additional
condition

$$
 N(\ell_1q_2-\ell_2q_1)\equiv0\pmod{q_1q_2}
\tag{F148.13}
$$

and every regrouping based on it are explicitly left outside the
no-go.  This closes the previous scope objection.

### 3.5 Source and no-go language

The candidate says only that the specifically audited progression,
additive, fixed-modulus complete-sum, and Kloosterman-fraction theorems
do not prove the literal varying-denominator signed estimate.  It
retains the alternative rational approximants allowed by
Schlage--Puchta, does not call the absolute squarefree \(Q+D\)
analogue false, and does not turn a positive diagonal capacity into a
lower bound for the signed scalar.  The terminal label is therefore
properly method- and source-scoped.

The evidence paragraph should continue to point to the primary-source
audit for exact theorem numbers and hypotheses; no broader claim about
all possible literature or all possible joint dispersion methods is
licensed.

## 4. First doubtful or unproved step

The first unproved step is the aggregate error estimate (148.C14b).
The exact remainder convention is repaired, but the stated powers do
not majorize both the \(K=6\) stationary Taylor remainder and the
sixfold nonstationary integration-by-parts pieces.  Until (F148.3),
(F148.4), the scaled tail derivative bound (F148.9), and the finite
mass sum (F148.11) are supplied in one lemma, (148.C3) is not yet a
proved target-equivalence.

After that, the first remaining issue for the no-go node is the
construction of a common literal cell set inside \(\mathcal P(d)\)
which proves the asserted \(c_0D\) diagonal uniformly.  The rectangle
construction in (F148.5)--(F148.12) is a precise repair and also
clarifies that the obstruction is witnessed on a long interior prefix.

No defect was found in (148.C14a), the reduced resonance coordinate,
the explicit exclusion of \(N\)-dependent alignments, or the
source/no-go scope.

## 5. Control tests and outcomes

1. **\(\mathcal P(d)\) exactness -- GREEN.**  It is exactly the finite
   set of nonempty discrete progressions inherited before Poisson.
2. **Character-Poisson and saddle constants -- GREEN.**  The prior
   recalculation remains unchanged.
3. **(148.C14a) exact remainder convention -- GREEN.**  The missing
   complementary polynomial and domain-tail terms are now explicitly
   assigned.
4. **Fixed lower symbols -- GREEN.**  Equation (148.C14) and the first
   line of (148.C14b) have the correct powers.
5. **\(K=6\) stationary remainder -- RED as displayed.**  Transition
   factors require \((M/\Lambda)^6\) and
   \((D/\Lambda)^6\).
6. **Sixfold nonstationary \(q\)-partition -- RED as displayed.**  Its
   capacity relative to the leading term retains
   \(\Lambda^{1/2}\), and the scaled tail derivative and dyadic
   summation are not shown.
7. **Final \(O(X^\varepsilon)\) conclusion -- AMBER.**  It is true
   under the corrected powers (F148.3)--(F148.4), but it is not proved
   by the displayed inequality.
8. **Common plateau and \(c_0\) -- AMBER.**  The stated hypothesis is
   sufficient; explicit selection inside the \(d\)-dependent
   \(\mathcal P(d)\) remains to be written.
9. **Cellwise diagonal scope -- GREEN.**  It is now limited to the
   correct early positive-ledger placement and is not a signed lower
   bound.
10. **\(N\)-dependent alignments -- GREEN.**  Equation (148.C22a)
    states them and leaves them outside the obstruction.
11. **Source and no-go wording -- GREEN.**  It is confined to audited
    sources and the specified method.
12. **Bytes -- GREEN.**  The candidate is valid UTF-8 without BOM,
    contains no forbidden control byte or trailing whitespace, and
    ends with LF.

No numerical experiment was used.

## 6. Dependencies and artifacts used

This review used:

- protocol.md;
- the active Round-148 campaign and its four target graph nodes;
- strategy/round148_squarefree_reciprocal_dispersion_strategy.md;
- the Round-148 barrier packet;
- reports/signed_squarefree_reciprocal_attack.md;
- reports/squarefree_progression_source_audit.md;
- reviews/transform_and_diagonal_seam_review.md;
- candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md.

No candidate, shared state, proof draft, validation matrix, or sibling
report was edited.  No web source or computation was used.

## 7. Recommended state effect and precise repairs

Do not yet promote the exact-transform reduction or the diagonal
obstruction.  Retain the signed target and every downstream node open.
Apply these localized repairs to the candidate:

1. Set \(K=6\) explicitly.  Add the stationary-remainder terms
   (F148.3), with \(M/\Lambda\) and \(D/\Lambda\), rather than
   assigning that remainder to the square-root derivative factors.
2. For six nonstationary integrations, insert the
   \(\Lambda^{1/2}\) factor in (F148.4), or use seven integrations and
   prove a weaker displayed sixth-power majorant.  Work in a scaled
   coordinate and include the dyadic \(q\)-tail sum.
3. Display (F148.11) and show how it combines with every middle and
   tail bound.  Then the corrected powers do prove
   \(O_{\varepsilon,V}(X^\varepsilon)\).
4. Construct the common long-prefix rectangle and the literal
   \(\alpha\)- and \(q\)-subfamilies in (F148.5)--(F148.12), so that
   \((\alpha,1)\in\mathcal P(d)\) and \(c_0\) are consequences rather
   than hypotheses.
5. Preserve the current exclusions of pre-Cauchy regrouping,
   \(N\)-dependent alignments, signed cross-cell cancellation,
   unaudited sources, and downstream owners.

The candidate is close to green, but its central target-equivalence
still rests on an incorrectly stated aggregate remainder bound.

AMBER
