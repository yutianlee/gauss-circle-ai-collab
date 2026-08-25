# Blind final v2 review of the Round 148 conductor candidate

Campaign: m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate
Candidate: candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md
Role: hostile final seam reviewer

## 1. Result

**Verdict: GREEN.**  The local v2 repairs close the two remaining
AMBER seams.

First, (148.C14b)--(148.C14d) now distinguish the three different
error scales correctly:

- the displayed \(1\le r<6\) stationary symbols;
- the \(K=6\) stationary Taylor remainder, with transition factors
  \((M/\Lambda)^6\) and \((D/\Lambda)^6\);
- the sixfold nonstationary integration-by-parts terms, with the
  required conversion factor \(\Lambda^{1/2}\) relative to leading
  stationary capacity.

The scaled derivative bound, dyadic \(2^{-5v}\) tail, and finite
\(\mathcal P(d)\)-mass are now explicit.  Every term in (148.C14d)
is \(O(1)\), in fact a negative power of \(R\), after the factor
\(R\sqrt D\) is restored.  Thus the complete post-Poisson error is
\(O_{\varepsilon,V}(X^\varepsilon)\), and (148.C3) is a proved
target-equivalence rather than a leading-term shorthand.

Second, (148.C17a)--(148.C20a) construct a literal long-prefix
subfamily.  The choice \(\alpha^2\in\mathcal J_e\), \(b=1\),
and \(n=1\) proves membership in the \(d\)-dependent
\(\mathcal P(d)\); the common \(q/(\alpha^2Q)\)-interval supplies
\(\asymp\alpha^2Q\) frequencies per \(\alpha\); and the common
profile plateau plus squarefree-\(d\) density proves \(c_0D\).
It follows that the selected cells have mass
\(\asymp Q\sqrt E\).  Short collar-owned prefixes are expressly
excluded from this lower-mass assertion.

The \(N\)-dependent alignments and every pre-Cauchy signed regrouping
remain outside the obstruction.  The source no-go and all downstream
claims remain correctly scoped.  The candidate's bytes are clean.

## 2. Exact statement and hypotheses verified

Let

$$
 \Lambda=\sqrt{NM}=R^2\sqrt M,\qquad
 P_0=R\sqrt D\,X^\varepsilon.
\tag{V2.1}
$$

For \(1\le r<6\), the stationary-symbol capacity is

$$
 P_0\left[
 \Lambda^{-r}
M^{-1/2}(M/\Lambda)^r
{\bf1}_{M\asymp D^2}D^{-1/2}(D/\Lambda)^r
 \right].
\tag{V2.2}
$$

The \(K=6\) stationary remainder is bounded by the same expression
with \(r=6\).  The sixfold nonstationary pieces are bounded by

$$
 P_0\Lambda^{1/2}\left[
 \Lambda^{-6}
M^{-1/2}(\sqrt M/\Lambda)^6
{\bf1}_{M\asymp D^2}D^{-1/2}
  (\sqrt D/\Lambda)^6
 \right].
\tag{V2.3}
$$

These are exactly the three lines of (148.C14d).  Their summation uses

$$
 \sum_d\sum_{(\alpha,b)\in\mathcal P(d)}
 \frac1\ell\#\{q:q\asymp\ell Q,\ q\ {\rm odd}\}
 \ll_\varepsilon DQ\sqrt E\,X^\varepsilon,
\tag{V2.4}
$$

and the dyadic tail factor \(2^{-5v}\).

For the diagonal obstruction, the candidate now assumes a long
retained rectangle

$$
 \mathcal J_d\times\mathcal J_e,\qquad
 |\mathcal J_d|\asymp D,\quad|\mathcal J_e|\asymp E,
\tag{V2.5}
$$

on which every physical profile is bounded below.  It selects
\(b=1\), odd squarefree \(\alpha\) with
\(\alpha^2\in\mathcal J_e\), and a common compact range of
\(q/(\alpha^2Q)\) for which
\(e_0(d,\alpha^2,q)\in\mathcal J_e\) throughout
\(\mathcal J_d\).  Under precisely these hypotheses,

$$
 \sum_i|c_i|\asymp Q\sqrt E,\qquad
 \sum_{d\in\mathcal J_d}|a_{i,d}|^2\ge c_0D,
\tag{V2.6}
$$

and the cellwise positive-diagonal capacity is
\(Q\sqrt M=\sqrt N\,D=R(RD)\).

## 3. Proof and hostile verification

### 3.1 The \(q\)-partition and finite mass

In the two tails use \(y=\ell x/E\).  On the amplitude support,
the repaired derivative bound is

$$
 |\partial_y\phi|
 \gg\Lambda\left(1+\frac{|q|}{\ell Q}\right).
\tag{V2.7}
$$

Six integrations by parts give \(2^{-6v}\) on a dyadic tail
\(|q|\asymp2^v\ell Q\).  That tail contains
\(O(2^v\ell Q)\) frequencies, hence its summed factor is
\(2^{-5v}\), which is geometrically summable.

The finite progression set has
\(\alpha\ll\sqrt E\) and \(b\mid d\).  For each fixed
\((d,\alpha,b)\), the middle \(q\)-range has
\(O(\ell Q)\) integers, so its factor \(1/\ell\) contributes
\(O(Q)\).  Summing the \(O(\sqrt E)\) possible \(\alpha\)'s,
the divisor-function number of \(b\)'s, and \(d\asymp D\) proves
(V2.4).  The same computation, with the geometric dyadic factor,
owns both tails.

### 3.2 Stationary symbols and the \(K=6\) remainder

In the bulk, \(H^{(2r)}(0)\ll_r1\).  On a radial transition it is
\(O_r(M^r)\), while that transition occupies an
\(O(M^{-1/2})\) fraction of the middle \(q\)-range.  On a cone
transition it is \(O_r(D^r)\), with fraction
\(O(D^{-1/2})\).  Division by \(\Lambda^r\) proves (V2.2).
Taylor's remainder at order \(12\) has the identical ledger with
\(r=6\); this is exactly the repaired second line of (148.C14d).

For a nonstationary integral, comparison with a leading Gaussian term
costs \(\Lambda^{1/2}\), because the latter contains the stationary
factor \(\Lambda^{-1/2}\).  Each integration by parts costs
\(1/\Lambda\) in the bulk, \(\sqrt M/\Lambda\) on a radial
transition, or \(\sqrt D/\Lambda\) on a cone transition.  Including
the transition fractions gives (V2.3).  The final bracket of
(148.C14d) therefore has the correct powers and owns the negative
frequencies, positive tails, endpoint buffer, and complementary
polynomial term.

### 3.3 Final power check

After multiplying by \(P_0\), the three \(r=1\) terms are

$$
 \frac1{R\sqrt E},\qquad \frac{\sqrt D}{R},\qquad \frac1R
\tag{V2.8}
$$

in the cone case for the last term.  They are \(O(1)\) because
\(D\le R\).  Each subsequent stationary term gains a factor at most

$$
 \Lambda^{-1},\qquad
 M/\Lambda=\sqrt M/R^2\le R^{-1},\qquad
 D/\Lambda\ll R^{-2},
\tag{V2.9}
$$

respectively.  The order-six stationary remainder is therefore
smaller than (V2.8).

For the nonstationary terms,
\(\sqrt M/\Lambda=R^{-2}\).  The bulk term is
\(P_0\Lambda^{-11/2}\).  The radial term is
$$
 P_0M^{-1/2}\Lambda^{1/2}R^{-12},
$$
and on \(M\asymp D^2\) the cone term is smaller still.  All are
negative powers of \(R\), uniformly for \(1\le M\le R^2\).
Consequently (148.C14d) really yields
\(\mathcal E_{\ge1}\ll_{\varepsilon,V}X^\varepsilon\).
Together with the separately counted collars, this proves (148.C3)
for all inherited prefixes; collar-short prefixes remain with their
primal owner.

### 3.4 Literal long-prefix diagonal family

For \(b=1\), \(\ell=\alpha^2\).  If
\(\alpha^2\in\mathcal J_e\), then for every
\(d\in\mathcal J_d\)

$$
 \mathscr A(d,[\alpha^2,1]\cdot1)
 =\mathscr A(d,\alpha^2)\ne0.
$$

Thus \((\alpha,1)\in\mathcal P(d)\) through the actual integer
progression point \(n=1\).  A fixed relative interval
\(\mathcal J_e\) contains \(\asymp\sqrt E\) odd squarefree
\(\alpha\)'s.

Writing \(q=t\alpha^2Q\) and using \(Q^2=4ND/E\) gives

$$
 e_0(d,\alpha^2,q)=\frac{d}{D}\frac{E}{t^2}.
\tag{V2.10}
$$

After narrowing \(\mathcal J_d,\mathcal J_e\) and the fixed
\(t\)-interval by constants, (V2.10) lies in
\(\mathcal J_e\) for all selected \(d,t\).  The interval contains
\(\asymp\alpha^2Q\) odd \(q\)'s.  Hence each \(\alpha\) contributes
\(\asymp Q\) to \(\sum|c_i|\), proving the first part of (V2.6).

On the same rectangle the profile and \(D/d\) are bounded below.
The squarefree integers have positive density in
\(\mathcal J_d\), so the squared \(d\)-mass is at least \(c_0D\),
uniformly in the selected cells.  This proves the second part of
(V2.6), and then (148.C21)--(148.C22) follow exactly.

This construction witnesses only a long retained interior prefix.
The candidate expressly makes no \(Q\sqrt E\) lower-mass claim for
a short prefix already assigned to the radial collar.

### 3.5 Scope and alignments

Equation (148.C22a) records the full additional alignment condition

$$
 N(\ell_1q_2-\ell_2q_1)\equiv0\pmod{q_1q_2}.
$$

The candidate explicitly excludes those fibres, every pre-Cauchy
regrouping, and all signed cross-cell cancellation from the no-go.
It also says that (148.C22) is not the diagonal of every joint
dispersion form and is not a lower bound for the signed scalar.
The source conclusion is limited to the named audited theorem families.
No downstream owner is crossed.

## 4. First doubtful or unproved step

No doubtful step remains in the two proposed scoped nodes.  The exact
transform has a finite arithmetic index set, an exact Gaussian
remainder convention, a complete \(K=6\) stationary and
nonstationary power ledger, and owned collars.  The progression-cell
obstruction has a literal common subfamily and the correct method
quantifiers.

The first genuinely open step is exactly the one stated by the
candidate: a joint coefficient-sensitive estimate for (148.C4) which
uses signed cross-progression cancellation before any separately
positive diagonal, or an exact Euler recombination followed by a
signed theorem for the Round-147 \(H\)-correlation.  Neither scoped
promotion claims to solve it.

For editorial precision only, the condition
\(\alpha\le\sqrt E\) in (148.C18) should be read with the campaign's
dyadic constants, equivalently \(\alpha\ll\sqrt E\); the exact
condition is \(\alpha^2\in\mathcal J_e\).  This does not affect any
count or claim.

## 5. Control tests and outcomes

1. **\(K=6\) declaration -- GREEN.**  It is explicit before the
   \(q\)-partition.
2. **Scaled tail derivative -- GREEN.**  Equation (V2.7) has the
   correct dimensionless phase scale.
3. **Dyadic tail sum -- GREEN.**  Six integrations and
   \(2^v\)-many frequencies give \(2^{-5v}\).
4. **Finite progression mass -- GREEN.**  Equation (148.C14b) gives
   \(DQ\sqrt E X^\varepsilon\).
5. **Stationary Taylor remainder -- GREEN.**  The repaired powers are
   \((M/\Lambda)^6\) and \((D/\Lambda)^6\).
6. **Nonstationary conversion -- GREEN.**  The final bracket retains
   \(\Lambda^{1/2}\).
7. **Final error -- GREEN.**  Every term in (148.C14d) is
   \(O(X^\varepsilon)\) after the \(R\sqrt D\) factor.
8. **\(\mathcal P(d)\) membership -- GREEN.**  It follows literally
   from \(b=1,n=1,\alpha^2\in\mathcal J_e\).
9. **\(Q\sqrt E\) mass -- GREEN.**  There are
   \(\asymp\sqrt E\) selected \(\alpha\)'s and
   \(\asymp\alpha^2Q\) \(q\)'s per \(\alpha\).
10. **Common \(c_0D\) diagonal -- GREEN.**  The common rectangle,
    profile lower bound, and squarefree-\(d\) density prove it.
11. **Short prefixes -- GREEN.**  They are excluded from the diagonal
    lower-mass claim and retained by the primal collar owner.
12. **\(N\)-dependent alignments and scope -- GREEN.**  They remain
    explicitly outside the obstruction.
13. **Source and downstream scope -- GREEN.**  Only audited families
    and the stated \(t=1\) method are covered.
14. **Bytes -- GREEN.**  The candidate is valid UTF-8 without BOM,
    has no forbidden control byte or trailing whitespace, and ends
    with LF.

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

This review used:

- protocol.md;
- the active Round-148 campaign and its four target graph nodes;
- strategy/round148_squarefree_reciprocal_dispersion_strategy.md;
- the Round-148 barrier packet;
- reports/signed_squarefree_reciprocal_attack.md;
- reports/squarefree_progression_source_audit.md;
- reviews/transform_and_diagonal_seam_review.md;
- reviews/blind_conductor_round148_candidate_final.md;
- candidates/conductor_round148_squarefree_reciprocal_transform_and_dispersion_no_go.md.

No candidate, shared state, proof draft, validation matrix, or sibling
report was edited.  No web source or numerical computation was used.

## 7. Recommended state effect

The two candidate nodes are promotion-ready within their stated scope:

1. the exact \(t=1\) squarefree reciprocal-transform reduction
   (148.C3)--(148.C17), including finite progression support,
   character-Poisson normalization, collars, all lower symbols, and
   the complete post-Poisson remainder; and
2. the progression-separated reciprocal-dispersion obstruction
   (148.C17a)--(148.C26), limited to unrecombined cellwise Cauchy with
   a separately nonnegative \(d\)-diagonal and the named audited
   source families.

Retain the signed reciprocal target, every strict range, all
pre-Cauchy signed regroupings, the Round-147 \(H\)-correlation,
Round-138 cross owner, every \(t\ge2\) layer, lower GAR, M9--M1,
M9--M2, endpoint uniformity, M9, the bridge, quarter target, and global
exponent as open.

GREEN
