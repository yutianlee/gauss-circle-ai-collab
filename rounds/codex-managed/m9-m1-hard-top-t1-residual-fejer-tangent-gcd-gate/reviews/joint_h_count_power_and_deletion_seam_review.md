# Round 185 joint-\(h\) count, power, and deletion seam review

## 1. Result / verdict

**Verdict: REPAIR.**

The arithmetic identities, both opposing-orientation parametrizations,
the deductions from squarefreeness and coprimality, the fixed-parameter
counts, the double harmonic sum, the explicit
\(\gamma^{-1}\) and \(\delta^{-1}\) powers, and the capacity statements
(185.C38)--(185.C39) all rederive correctly.

The repair is at the claimed exact complement (185.C36), not at the
joint-\(h\) power count.  As written, an affine solution row has no
canonical base representative, and the sum over every \(t\in\mathbb Z\)
does not impose the defining opposing-orientation inequalities
\(s_t\geq1\) and \(w_t\geq1\).  The coefficient \(\lambda\) does not
encode those tangent-sign conditions.  Consequently the displayed
full-line formula can reinsert monotone sites and sites belonging to the
other cross orientation, and it can repeat a row under shifted choices
of \((S_0,w_0)\).  With a canonical representative for each affine
class, the inherited primitive-label conditions stated explicitly, and
the two positivity indicators inserted in each \(B_{\mathfrak f,\pm}\),
the complement and all reviewed counts are valid.

## 2. Exact statement and hypotheses

Fix \(X\geq2\), one nonempty literal middle or lower hard-M1 shell
\(L\geq2\), one \(\sigma\in\{\pm1\}\), and
\(R_0=\lceil L\rceil\).  At an even shift
\(r=2q\), \(0<r<R_0\), a nonzero opened incidence has

\[
 N=dm,\qquad N+r=d'm',
\]

with \(d,d'\) odd, both endpoint products squarefree, the two original
factor pairs coprime, and \(d,d',m,m'\asymp L\).  Literal coefficients
are bounded by \(O_\varepsilon(X^\varepsilon)\); selectors, profiles,
endpoints, and all other physical conditions occur through the
zero-extended \(\lambda\)'s.

The statement audited here is the following.

1. For \(g=(d,d')\), fixed-\(g\) incidence count is
   \(O(L^3/g^2)\), hence the tail \(g\geq G\) is \(O(L^3/G)\).
2. In each opposing orientation, the inward cross gcd \(\kappa\), the
   joint gcd \(g\), and the quotient \(h\) give
   \(r=2\kappa gh\).  At fixed \((\kappa,g,h)\), the incidence count is
   \(O(L^2/(\kappa g))\).
3. Thus
   \[
   \#\{ab<0:h\leq H\}
   \ll HL^2\log^2(2L),
   \]
   and \(H=\lfloor(\log(2X))^B\rfloor\) is target-safe after the
   inherited literal-shell polylogarithmic rebudgeting.
4. The tails \(g\geq\gamma L\) and \(\kappa\geq\delta L\) cost exactly
   \(O_\varepsilon(\gamma^{-1}L^2X^\varepsilon)\) and
   \(O_\varepsilon(\delta^{-1}L^2X^\varepsilon)\), respectively.
5. One unjustified \(O(1)\) bound per primitive affine row would still
   have \(O(L^3)\) positive recombination capacity, and bare alternating
   signs alone give no contraction for arbitrary bounded row weights.

For an exact fibre partition, “primitive label” must mean at least
\(\kappa,g,h,U,v\in\mathbb Z_{>0}\), \(\kappa,g,U\) odd,
\((gU,v)=1\), \((U,h)=1\), \(2\kappa gh<R_0\), together with one
canonical solution class of the appropriate equation.  The conditions
\((gU,v)=1\) and \((U,h)=1\) are the explicit forms of the inherited
facts \((u,v)=1\) and \(g=(u,n)\); merely recording \((U,v)=1\) is not a
self-contained multiplicity-one label domain.

## 3. Proof or line audit

### Original gcd and its tail

Let \(g=(d,d')\), \(d=gu\), and \(d'=gv\).  Then \((u,v)=1\) and

\[
 vm'-um=\frac r g.
\]

In particular \(g\mid r\).  At fixed \(g\), there are
\(O((L/g)^2)\) choices for \((u,v)\), \(O(L/g)\) possible positive
values of \(r/g\), and, for each such triple, all solutions of the last
equation differ by

\[
 (m,m')\longmapsto(m+vt,m'+ut).
\]

Because \(u,v\asymp L/g\) while both \(m,m'\) lie in intervals of
length \(O(L)\), this row has \(O(1+g)=O(g)\) sites on nonempty support.
Therefore

\[
 O\!\left(\frac{L^2}{g^2}\right)
 O\!\left(\frac Lg\right)O(g)
 =O\!\left(\frac{L^3}{g^2}\right),
\]

and summing \(g^{-2}\) for \(g\geq G\) proves (185.C14).  Squarefree,
coprime, selector, and literal-profile restrictions can only decrease
this absolute count.

### Both inward-cross-gcd orientations

For \(a=2s>0\), \(b=-2w<0\), put
\(\kappa=(d,m')\).  Then

\[
 d=\kappa u,\quad m'=\kappa v,\quad
 d'=\kappa u+2s,\quad m=\kappa v+2w,
\]

where \((u,v)=1\), and direct subtraction gives

\[
 r=2\kappa(sv-wu)=2\kappa n,\qquad n>0.
\]

For \(a=-2s<0\), \(b=2w>0\), putting
\(\kappa=(d',m)\) instead gives

\[
 d'=\kappa u,\quad m=\kappa v,\quad
 d=\kappa u+2s,\quad m'=\kappa v+2w,
\]

and

\[
 r=2\kappa(uw-sv)=2\kappa n,\qquad n>0.
\]

The signs of \((a,b)\) make these orientations disjoint, and the gcd
definitions recover \(\kappa,u,v,s,w\) uniquely from an incidence.
At fixed \(\kappa\), there are \(O((L/\kappa)^2)\) choices of
\((u,v)\), \(O(L/\kappa)\) choices of \(n=r/(2\kappa)\), and
\(O(\kappa)\) sites on the solution line.  This is
\(O(L^3/\kappa^2)\), and summing \(\kappa^{-2}\) proves (185.C19).

### Squarefree joint gcd and primitive row

In the plus orientation the squarefree upper endpoint is
\((\kappa u+2s)\kappa v\); in the minus orientation the same
factorization is the squarefree lower endpoint.  If a prime divided
both \(\kappa\) and \(s\), it would divide both displayed factors.
Since \(\kappa\) is odd, this proves \((\kappa,s)=1\).  Hence in either
orientation

\[
 (d,d')=(\kappa u,\kappa u+2s)=(u,s).
\]

Also, using \((u,v)=1\),

\[
 (u,sv-wu)=(u,s),\qquad
 (u,uw-sv)=(u,s).
\]

Thus (185.C20) is exact:

\[
 g=(d,d')=(u,s)=(u,n).
\]

Writing \(u=gU\), \(s=gS\), and \(n=gh\) gives
\(r=2\kappa gh\) and the respective primitive equations

\[
 Sv-wU=h,\qquad Uw-vS=h.
\]

For fixed \((\kappa,g,h,U,v)\), each equation has one affine solution
class because \((U,v)=1\).  After selecting one representative, all
solutions have

\[
 S_t=S_0+Ut,\qquad w_t=w_0+vt.
\]

Since \(U\asymp L/(\kappa g)\), \(v\asymp L/\kappa\), and the physical
ranges of \(s=gS\) and \(w\) have length \(O(L)\), the intersection
with either opposing orientation has \(O(\kappa)\) sites.  Finally,
\(g,U\) are odd, so

\[
 \chi_4(d')\chi_4(d)=(-1)^s=(-1)^S=(-1)^{S_0+t}.
\]

This verifies (185.C20)--(185.C25), including the character anchor,
once the representative is fixed only once per affine class.

### Fixed \((\kappa,g,h)\), the harmonic sum, and restored powers

Support gives

\[
 \#U=O\!\left(\frac{L}{\kappa g}\right),
 \qquad
 \#v=O\!\left(\frac{L}{\kappa}\right),
 \qquad
 \#t=O(\kappa).
\]

Their product is exactly the asserted upper bound

\[
 O\!\left(\frac{L^2}{\kappa g}\right)
\]

per \((\kappa,g,h)\), for either orientation.  Since the integer
inequality \(r<R_0=\lceil L\rceil\) implies \(r<L\), one has
\(\kappa g<L/(2h)\).  Moreover

\[
 \sum_{\kappa g<T}\frac1{\kappa g}
 =\sum_{\kappa<T}\frac1\kappa
   \sum_{g<T/\kappa}\frac1g
 \ll\log^2(2T).
\]

Summation over \(h\leq H\) proves (185.C28), with the factor for two
orientations absorbed in the constant.  Taking
\(H=H_B=\lfloor(\log(2X))^B\rfloor\), multiplying by the two endpoint
coefficient bounds, and rebudgeting the fixed polylogarithms proves
(185.C30).  No cancellation is used.

The already verified tails give, on setting \(G=\gamma L\) and
\(K=\delta L\),

\[
 \frac{L^3}{\gamma L}=\gamma^{-1}L^2,
 \qquad
 \frac{L^3}{\delta L}=\delta^{-1}L^2.
\]

This checks the exact powers in (185.C31).  Also, from
\(2\kappa gh<L\), \(g\geq\gamma L\) implies
\(h<(2\gamma)^{-1}\), while \(\kappa\geq\delta L\) implies
\(h<(2\delta)^{-1}\).  Hence the stated containment in the bounded-
\(h\) sector is correct under the displayed condition on \(H_B\).

### Row capacity and arbitrary weights

For fixed \((\kappa,g)\), the number of complete primitive row labels
is at most

\[
 O\!\left(\frac{L}{\kappa g}\right)
 O\!\left(\frac{L}{\kappa}\right)
 O\!\left(\frac{L}{\kappa g}\right)
 =O\!\left(\frac{L^3}{\kappa^3g^2}\right),
\]

coming respectively from \(U,v,h\).  Therefore even granting an
unproved \(O(1)\) estimate for every row leaves

\[
 O\!\left(L^3\sum_{\kappa,g\geq1}
          \frac1{\kappa^3g^2}\right)=O(L^3),
\]

which verifies (185.C38).  For any finite integer interval \(I\), the
upper bound in (185.C39) is the triangle inequality, and equality is
obtained with \(B(t)=(-1)^t\) (up to a common unit phase).  Thus the
supremum is \(|I|\).  A constant sequence on \(M\asymp L^2\) sites has
\(\asymp M\) correlation at each of \(\asymp L\) even Fejer shifts, so
its even-shift capacity is \(\asymp L^3\).  These are mechanism-capacity
statements, not assertions about the fixed literal coefficient.

## 4. First doubtful or unproved step

The first nonvalid exactness claim in the reviewed seam is (185.C36).
For the plus equation \(Sv-wU=h>0\), the affine line

\[
 (S_t,w_t)=(S_0+Ut,w_0+vt)
\]

passes, as \(t\) increases, through a region with both entries negative
(the opposite orientation), possibly a region with \(S_t>0\) and
\(w_t\leq0\) (the monotone sector), and finally the intended region
with both entries positive.  The minus equation has the analogous
issue.  Squarefreeness, coprimality, hard cones, profiles, selectors,
and endpoint masks inside \(\lambda\) do not state the signs of the
tangent displacements.  Hence zero extension of \(\lambda\) cannot
justify replacing the orientation-specific interval by all of
\(\mathbb Z\).

The minimal exact repair is:

1. for each primitive \((\kappa,g,h,U,v)\) and each orientation, choose
   one canonical solution, for example the unique representative with
   \(0\leq S_0<U\), and do not range again over its translates;
2. state the full primitive outer domain, in particular
   \((gU,v)=1\), \((U,h)=1\), the oddness conditions, and
   \(0<2\kappa gh<R_0\);
3. replace each row weight by
   \[
   \widetilde B_{\mathfrak f,\pm}^{\sigma}(t)
   =\mathbf1_{s_t\geq1}\mathbf1_{w_t\geq1}
     B_{\mathfrak f,\pm}^{\sigma}(t),
   \qquad s_t=g(S_0+Ut),
   \]
   or equivalently restrict its \(t\)-sum to that orientation interval.

No further \(t\)-level domain indicator is needed: after these two sign
indicators and the primitive outer-domain restrictions are explicit,
the two \(\lambda\)'s correctly zero-extend all original product,
selector, squarefree/coprimality, profile, hard-sample, endpoint, sign,
and shell predicates.  The algebraic identities already enforce
\(N_t^\pm+r\) and the fixed positive even shift.

## 5. Controls and outcomes

The archived control was reproduced with exact integer arithmetic.
For \((\kappa,u,v,s_0,w_0)=(101,7,1,8,1)\):

- at \(t=0\),
  \((d,d',m',m)=(707,723,101,103)\), with
  \(N=72821=7\cdot101\cdot103\),
  \(N'=73023=3\cdot241\cdot101\), and \(r=202\);
- at \(t=1\),
  \((d,d',m',m)=(707,737,101,105)\), with
  \(N=74235=3\cdot5\cdot7^2\cdot101\),
  \(N'=74437=11\cdot67\cdot101\), and the same \(r=202\).

The four ratio checks are, exactly,

\[
 412<707<1648,\quad 404<723<1616,
\]

\[
 420<707<1680,\quad 404<737<1616.
\]

At \(t=0\) both products are squarefree and both original factor pairs
are coprime.  At \(t=1\), \((707,105)=7\), so the lower product is not
squarefree, while the upper product remains squarefree and coprime.
Furthermore

\[
 (707,723)=(707,737)=1,
 \qquad sv-wu=1
\]

at both sites, so \(g=h=1\).  The character product changes from
\(({-1})({-1})=+1\) to \((+1)({-1})=-1\).  This passes the archived
control's stated test: a tangent step need not preserve squarefree and
coprime hard support despite the bare character flip.

The conductor-supplied stronger control was also checked exactly.  For
\((\kappa,u,v,s_0,w_0)=(103,7,1,99,14)\):

- \(t=0\) gives \((721,919,103,131)\),
  \(N=94451=7\cdot103\cdot131\),
  \(N'=94657=919\cdot103\), and \(r=206\);
- \(t=1\) gives \((721,933,103,133)\),
  \(N=95893=7^2\cdot19\cdot103\),
  \(N'=96099=3\cdot311\cdot103\), and the same \(r=206\).

The ratio checks are

\[
 524<721<2096,\quad 412<919<1648,
\]

\[
 532<721<2128,\quad 412<933<1648.
\]

Both \(t=0\) products are squarefree/coprime; at \(t=1\),
\((721,133)=7\) deletes the lower product and the upper product remains
squarefree/coprime.  Again \(g=h=1\).  The character product changes
from \(-1\) to \(+1\).  The primes \(7,103,131,919\) are all
\(3\pmod4\), so neither live \(t=0\) endpoint has an eligible selected
pair and \(\rho=1\) independently of the canonical selector.

Replacing the archived example is not required for its narrowly stated
squarefree-support falsification rule.  The stronger example should
replace or supplement it if the candidate keeps language about the
residual selector or a “literal” adjacent-pair cancellation, because it
removes the archived example's selector-survival ambiguity.  Even the
stronger example does not verify nonvanishing of every literal profile
or endpoint amplitude, so its conclusion must remain a mechanism no-go:
it proves neither an asymptotic lower bound nor failure of the desired
fixed-coefficient estimate.

## 6. Exact artifacts used

- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/briefs/joint_h_count_power_and_deletion_seam_review.md`;
- `protocol.md`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/candidates/formalized_hard_m1_t1_residual_tangent_gcd_reduction.md`, verified candidate SHA-256 `791c6f3b6999991ac78198b55a106fa5e2b7767469702e853119d52b50e17385`;
- `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`;
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/controls/conductor_round185_exact_fibre_deletion_control.md`; and
- the conductor-supplied supplemental exact parameter packet
  \((103,7,1,99,14)\).

No sibling report, proof-state file, external source, or numerical
theorem evidence was used.  The two finite controls were recomputed only
with exact integer products, gcds, congruences, and square-divisor tests.

## 7. Recommended state effect

**Revise; no graph change yet.**  Retain (185.C13)--(185.C31) and
(185.C38)--(185.C39) as supported evidence.  Repair (185.C36) by fixing
one canonical base representative per affine class, spelling out the
primitive outer-label domain, and inserting
\(\mathbf1_{s_t\geq1}\mathbf1_{w_t\geq1}\) in both orientation row
weights.  The resulting orientation-restricted complement has the same
bounded-\(h\) and row-capacity counts.  Keep the deletion examples
quarantined as finite mechanism controls and do not promote a complete
residual estimate from them.
