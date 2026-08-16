# 1. Result: lemma or no-go result.

The strongest uniform incidence statement available from the frozen
geometry is a **divisor-strip theorem**, and it is sharp at the random
density scale.  It has three consequences.

1.  On a dyadic block, the trivial incidence capacity is
    \(\ll A D K\), whereas the metric window gives
    \[
      \mathcal I_{\rm ns}(A,D,K,G;R)
      \ll_\varepsilon X^\varepsilon A D
          \min\!\left(K,1+{K\over R}\right).
      \tag{79.DS}
    \]
    In the actual range \(R\leq G\asymp L/A\),
    \(K\asymp JD/A\), and \(L\leq J^{1/2}\), one has
    \(K/R\gg JD/L\gg J^{1/2}\).  Thus (79.DS) saves exactly a
    factor \(R\):
    \[
      \mathcal I_{\rm ns}(A,D,K,G;R)
      \ll_\varepsilon X^\varepsilon {A D K\over R}.
      \tag{79.14}
    \]
    For a ray whose open \(k\)-interval has only one point, the sharper
    bound is of course one; (79.DS) is to be read with the actual
    \(k\)-count inside the minimum.

2.  Inserting the complete Round-77 coefficient scale gives
    \[
      \mathcal A_{\rm ns}(A,D,K,G;R)
      \ll_\varepsilon
      X^\varepsilon A\sqrt G\,\sqrt J\,D^{3/2}.
      \tag{79.15}
    \]
    This is independent of \(R\): the density saving \(R^{-1}\)
    exactly cancels the Abel weight \(R\).  Since \(G\asymp L/A\),
    (79.15) closes, by positive summation, only the subregion
    \[
       A J D^3\ \ll\ L^3.                              \tag{79.16}
    \]
    The smaller unresolved survivor is the strict metric set
    \(0<\|\Lambda/k\|\leq c/R\) in blocks with
    \(AJD^3\gg L^3\), together with the literal signed coefficient.

3.  Exact nonsquare resonances are much more rigid.  At a fixed real
    \(X\), at most one primitive nonsquare ray can have
    \(\Lambda\in\mathbb Z\).  Its exact reciprocal modes are divisors
    of \(\Lambda\), and its complete absolute contribution is
    \[
       O_\varepsilon(LX^\varepsilon).                  \tag{79.17}
    \]
    Hence exact nonsquare centers may be removed absolutely.  This does
    not remove the strict metric strip.

There is also a sharp no-go.  On every populated inner cone stable under
\(X\in[Y,2Y]\), averaging in \(X\) produces
\(\gg ADK/R\) **strictly metric** nonsquare incidences for some \(X\).
In a fixed-ratio block these incidences can occupy
\(\gg B^{1-\varepsilon}/R\) distinct nonsquare quadratic fields.
Thus the full metric resonant set is generically large and cannot all be
declared algebraically structured.  Any further inverse theorem must be
about excess over the \(1/R\) density baseline, and (79.15) shows that
even baseline incidence is too large in the surviving blocks unless a
signed primitive-ray/reciprocal-mode estimate is proved.

# 2. Exact statement and hypotheses.

Retain all hypotheses and notation of the Round-79 packet.  Thus
\(J=\sqrt X\), \(1\leq L\leq H\leq J^{1/2}\), the rays are primitive,
odd, coprime and satisfy \(a<b<4a\), the square family \(ab=\square\)
is excluded, and the open interval (79.2), the actual finite odd lift
set, stars, profiles, collars and complete integral coefficient are not
altered.

Put
\[
  m={a+b\over2},\qquad q={b-a\over2},\qquad
  s=\sqrt{m^2-q^2}=\sqrt{ab},
\]
and
\[
  u={q\over m+s}={m-s\over q}
    ={\sqrt b-\sqrt a\over\sqrt b+\sqrt a}.
  \tag{79.18}
\]
Then \(m,q\) are coprime and of opposite parity,
\(0<q<3m/5\), and \(0<u<1/3\).  Moreover
\[
 {\delta^2\over2}=m-s=qu,\qquad
 \Lambda=Xqu,                                      \tag{79.19}
\]
and the literal reciprocal interval becomes
\[
   {Ju\over1-u}<k<{2Ju\over1+u}.                   \tag{79.20}
\]
If \(v=k/(Ju)\), then
\[
   {1\over1-u}<v<{2\over1+u},\qquad
   {\Lambda\over k}={Jq\over v}.                  \tag{79.21}
\]
The square rays are exactly those for which \(s\in\mathbb Z\), or
equivalently \(u\in\mathbb Q\).

On a dyadic block \(a\asymp A\), \(b-a\asymp D\),
\(k\asymp K\), \(G_{a,b}\asymp G\), and \(R\leq N_{a,b}\), one has
\[
 u\asymp {D\over A},\quad {\delta^2\over2}\asymp {D^2\over A},
 \quad K\asymp {JD\over A},\quad
 {\Lambda\over k}\asymp JD.                       \tag{79.22}
\]
Let \(M_{a,b}(K)\) be the number of integers in the intersection of
(79.20) with \([K,2K)\).  Then the precise incidence statement is
\[
 \mathcal I_{\rm ns}(A,D,K,G;R)
 \ll_\varepsilon X^\varepsilon
 \sum_{(a,b)}
 \min\!\left(M_{a,b}(K),1+{K\over R}\right),       \tag{79.23}
\]
where the sum is over the residual rays in the block.  Since their
number is \(O(AD)\), (79.DS) follows.

For exact rigidity, write
\[
   ab=\mathfrak d r^2,qquad \mathfrak d>1
   \text{ squarefree},\qquad
   {\delta^2\over2}=m-r\sqrt{\mathfrak d}.          \tag{79.24}
\]
For distinct primitive nonsquare triples \((a_i,b_i,k_i)\),
\[
 {m_1-r_1\sqrt{\mathfrak d_1}\over k_1}
 \ne
 {m_2-r_2\sqrt{\mathfrak d_2}\over k_2}.           \tag{79.25}
\]
More strongly, the ratio of the two numerators in (79.25) is rational
only when the primitive rays are identical.  Consequently, if
\(X(m_i-r_i\sqrt{\mathfrak d_i})\in\mathbb Z\) for two rays, the rays
are identical.

Finally, the sharpness/no-go statement is as follows.  Let \(Y\) be
large and put \(J_0=\sqrt Y\).  Freeze an inner block with
\(u\leq u_+<3-2\sqrt2\), and take a collection \(\mathscr S\) of
actual nonsquare rays which remains populated, with \(N_{a,b}\geq R\),
throughout \(X\in[Y,2Y]\).  For each ray choose a fixed subinterval of
integers
\[
  \kappa_-J_0u<k<\kappa_+J_0u                       \tag{79.26}
\]
with
\[
 {\sqrt2\over1-u_+}<\kappa_-<\kappa_+
       <{2\over1+u_+}.
\]
It is contained in (79.20) for every \(X\in[Y,2Y]\).  If \(T\) is
the number of frozen triples \((a,b,k)\), and
\(\mu_R=\operatorname{meas}\{t\bmod1:\|t\|\leq c/R\}\asymp R^{-1}\),
then
\[
 \int_Y^{2Y}\!\#\left\{(a,b,k)\in\mathscr S:
       \left\|{X\delta_{a,b}^2\over2k}\right\|\leq {c\over R}
                  \right\}\,dX
 =\mu_RYT+O\!\left(T{J_0\over D}\right).           \tag{79.27}
\]
Exact equalities may be deleted from the integrand without changing
(79.27), since they form a finite measure-zero set.  In a populated
block with \(\#\mathscr S\asymp AD\) and \(T\asymp ADK\), (79.27)
therefore supplies some \(X\) with \(\gg ADK/R\) strict metric
incidences.  The error-to-main ratio is
\(O(R/(J_0D))\), which is \(o(1)\) in the actual range.

# 3. Proof or derivation.

**Algebraic coordinates.**  Since \(a=m-q\) and \(b=m+q\), oddness of
\(a,b\) says that \(m,q\) have opposite parity.  Every common divisor
of \(a,b\) is odd, and
\[
 (a,b)=(m-q,m+q)=(m,q),
\]
so primitivity is exactly \((m,q)=1\).  The cone inequality
\(m+q<4(m-q)\) is \(5q<3m\).  Rationalizing (79.18) gives
\(qu=m-s\), hence (79.19).  Also
\[
 {\sqrt b\over\sqrt a}={1+u\over1-u}.
\]
Substitution in (79.2) gives (79.20), and (79.21) follows immediately.
The block comparisons (79.22) follow from \(m,s\asymp A\) and
\(q\asymp D\).

If \(u\) is rational, then \(s=q/u-m\) is rational; since \(s^2=ab\)
is integral, \(s\) is integral.  The converse is immediate.  Thus
\(u\in\mathbb Q\) is precisely the already removed square family.

**Trivial capacity and the divisor strip.**  There are \(O(AD)\)
possible \((a,b)\) in a block and at most \(O(K)\) possible \(k\)'s.
For a fixed triple, the interval
\(|\Lambda-\ell k|\leq ck/R\) contains only \(O_c(1)\) possible
integers \(\ell\).  Therefore
\[
   \mathcal I_{\rm triv}\ll ADK.                    \tag{79.28}
\]

For the saving, set \(p=\ell k\in\mathbb Z_{\geq1}\).  If
\(k\asymp K\), the full metric inequality implies
\[
       |\Lambda-p|\leq C{K\over R}.                 \tag{79.29}
\]
There are \(O(1+K/R)\) integers \(p\) in this strip.  For a fixed
\(p\), every admissible \((k,\ell)\) is a divisor factorization of
\(p\), so there are at most \(\tau(p)\ll_\varepsilon X^\varepsilon\)
of them.  Here \(p\ll X A\ll X^{5/4}\), so the elementary divisor
bound is uniform.  Intersecting this estimate with the actual open
\(k\)-interval proves (79.23).  Notice that (79.29), not exact
divisibility of \(\Lambda\), is the argument: the metric strip contains
\(O(K/R)\) different integers \(p\).

Because \(R\leq G\ll L/A\),
\[
 {K\over R}\asymp {JD\over AR}\gg {JD\over L}
       \geq {J\over L}\geq J^{1/2},                 \tag{79.30}
\]
which proves (79.14) whenever the interval has its normal capacity; the
minimum in (79.23) handles empty and one-point intervals.

**Complete coefficient ledger.**  The literal Round-77 estimate gives
on this block
\[
 \mathcal V_{a,b,k}\ll_\varepsilon
 X^\varepsilon{J(D/\sqrt A)\sqrt G\over K^{3/2}}
 \asymp_{X^\varepsilon}{A\sqrt G\over\sqrt{JD}}.    \tag{79.31}
\]
Before using (79.23), the positive coefficient capacity is
\[
 \mathcal C_{\rm triv}(R)
 \ll_\varepsilon X^\varepsilon
 {A\sqrt G\over\sqrt{JD}}\,R\,(ADK)
 \asymp X^\varepsilon A R\sqrt G\sqrt J D^{3/2}.   \tag{79.32}
\]
The divisor-strip saving replaces \(ADK\) by \(ADK/R\), proving
(79.15).  Since \(G\asymp L/A\), its right side is
\(X^\varepsilon\sqrt{ALJ}\,D^{3/2}\); comparison with \(L^2\)
is exactly (79.16).  Dyadic sums in \(A,D,G,R\) cost only powers of
\(\log X\), absorbed by \(X^\varepsilon\).

The standalone \(1\) in the Abel decomposition (79.6) has capacity
\(\mathcal V\,ADK\), exactly the right side of (79.15), so it introduces
no omitted term and obeys the same safe-region criterion (79.16).

This proves a lawful positive closure of (79.16).  It does not prove the
signed energy on the complementary blocks, because (79.31) has already
discarded the outer primitive-ray and reciprocal-mode phases.

**Exact nonsquare rigidity.**  Suppose first that the two frequencies
in (79.25) are equal.  Clearing denominators gives
\[
 k_2m_1-k_1m_2=k_2r_1\sqrt{\mathfrak d_1}
                  -k_1r_2\sqrt{\mathfrak d_2}.       \tag{79.33}
\]
If \(\mathfrak d_1\ne\mathfrak d_2\), linear independence of
\(1,\sqrt{\mathfrak d_1},\sqrt{\mathfrak d_2}\) over \(\mathbb Q\)
contradicts (79.33).  If the squarefree kernels agree, rational and
irrational parts give
\(k_2m_1=k_1m_2\) and \(k_2r_1=k_1r_2\).  Taking norms gives
\[
  k_2q_1=k_1q_2,
\]
because \(m_i^2-\mathfrak d r_i^2=q_i^2\).  The primitive integer
vectors \((m_i,q_i)\) are therefore positive rational multiples of
one another.  Primitivity forces the multiplier to be one, and then
\(a_1=a_2\), \(b_1=b_2\), and \(k_1=k_2\).  The same proof without
the \(k_i\)'s proves rational-ratio rigidity of the numerators.

If two primitive nonsquare rays were exactly resonant at the same
\(X\), then
\[
 X(m_i-r_i\sqrt{\mathfrak d_i})=p_i=\ell_i k_i\in\mathbb Z_{>0},
\]
so their numerator ratio would be \(p_1/p_2\in\mathbb Q\).  Hence the
rays coincide.  On that unique ray, exact modes satisfy \(k\mid p\),
and there are \(O_\varepsilon(X^\varepsilon)\) of them.  Applying
(79.4) with \(N_{a,b}\leq G\) and (79.31) gives
\[
 \sum_{\substack{k:\ \Lambda/k\in\mathbb Z}}
 \left|\sum_{g=2n+1\in\mathcal G_{a,b}}
   \mathfrak B^\circ_{a,b,k}(g)e(-n\Lambda/k)\right|
 \ll_\varepsilon X^\varepsilon
 {A G^{3/2}\over\sqrt{JD}}
 \ll_\varepsilon X^\varepsilon
 {L^{3/2}\over\sqrt{AJD}}
 \ll_\varepsilon LX^\varepsilon.                  \tag{79.34}
\]
This proves (79.17) without cancellation between modes.

**Why algebraic spacing does not resolve the metric strip.**  The same
norm argument does give a genuine but unusably fine root spacing.  For
distinct triples in an \((A,K)\)-block,
\[
 \left|{m_1-r_1\sqrt{\mathfrak d_1}\over k_1}
       -{m_2-r_2\sqrt{\mathfrak d_2}\over k_2}\right|
 \gg A^{-3}K^{-5};                                  \tag{79.35}
\]
if the squarefree kernels agree, the stronger lower bound is
\(\gg A^{-1}K^{-3}\).  Indeed, the cleared difference is a nonzero
algebraic integer of degree at most four, each other conjugate is
\(O(AK)\), and one then divides by \(k_1k_2\).

More directly, if two distinct rays in a common \((A,D,K,R)\)-block
are metric resonances with nearest integers \(\ell_i\), put
\(c_i=(m_i-r_i\sqrt{\mathfrak d_i})/k_i\).  Then
\[
 |\ell_2c_1-\ell_1c_2|\ll {D\over JR}.               \tag{79.36}
\]
The numerator after multiplying by \(k_1k_2\) is
\[
 F=(\ell_2k_2)(m_1-r_1\sqrt{\mathfrak d_1})
   -(\ell_1k_1)(m_2-r_2\sqrt{\mathfrak d_2}).
\]
Here \(\ell_i\asymp JD\), \(\ell_i k_i\asymp J^2D^2/A\), and every
nonidentity conjugate of \(F\) is \(O(J^2D^2)\).  Thus the norm gives
\[
 |\ell_2c_1-\ell_1c_2|
 \gg {A^2\over J^8D^8},                             \tag{79.37}
\]
or \(\gg A^2/(J^4D^4)\) in one quadratic field.  Comparing
(79.36)--(79.37) would separate the two resonances only for
\[
 R\gg {J^7D^9\over A^2},
 \quad\text{or, in one field,}\quad
 R\gg {J^3D^5\over A^2}.                            \tag{79.38}
\]
Both thresholds are far beyond
\(R\leq L/A\leq J^{1/2}/A\).  Hence exact injectivity is real, but its
algebraic norm spacing cannot see any allowed metric window.

**Random-density sharpness.**  For a frozen triple in (79.26), set
\[
 c_{a,b,k}={\delta^2\over2k}={qu\over k}\asymp {D\over J_0}.
\]
Periodicity gives the exact elementary estimate
\[
 \int_Y^{2Y}{\bf1}_{\{\|Xc_{a,b,k}\|\leq c/R\}}\,dX
 =\mu_RY+O(c_{a,b,k}^{-1})
 =\mu_RY+O(J_0/D).                                  \tag{79.39}
\]
Summing proves (79.27).  The condition
\(u_+<3-2\sqrt2\) is precisely what makes (79.26) possible, because
\[
 {\sqrt2\over1-u}< {2\over1+u}
 \quad\Longleftrightarrow\quad u<3-2\sqrt2.
\]

In a fixed-ratio block \(A\asymp D\asymp B\), elementary coprime-pair
counting supplies \(\asymp B^2\) primitive odd rays, while primitive
square rays contribute only \(O(B)\).  For a fixed nonsquare squarefree
kernel \(\mathfrak d\), writing
\(a=d_1x^2\), \(b=d_2y^2\), \(d_1d_2=\mathfrak d\), gives
\(O_\varepsilon(B^{1+\varepsilon})\) rays.  Since each field owns at
most \(O_\varepsilon(B^{1+\varepsilon}J_0)\) frozen triples, the
\(\gg B^2J_0/R\) incidences supplied by (79.27) occupy at least
\(\gg B^{1-\varepsilon}/R\) fields.  For example, with
\(L=J_0^{1/2}\), \(B=J_0^{1/3}\), and
\(R\leq G=J_0^{1/6}\), this tends to infinity uniformly even at the
largest window parameter.

At the coefficient scale (79.31), the random baseline contributes
\[
 \mathcal V\,R\,{ADK\over R}
 \asymp A\sqrt G\sqrt J D^{3/2},                    \tag{79.40}
\]
matching (79.15).  In the displayed example it is
\(J_0^{17/12}\), whereas \(L^2=J_0\).  Thus the factor-\(R\)
incidence theorem is sharp and still power-insufficient for positive
summation in the hard region.

# 4. First doubtful or unproved step.

The first unproved step is not the divisor-strip count, exact
injectivity, or their coefficient ledger; those are complete.  It is a
signed estimate for the baseline-sized strict metric population in
\(AJD^3\gg L^3\).

After removing (79.34) and the positively safe blocks (79.16), the
smallest remaining object is, blockwise and dyadically in \(R\),
\[
 \sum_{\substack{(a,b)\in\mathscr P_L^{\rm ns}\!,\ k\in\mathcal K_{a,b}\!
                  \\ AJD^3\gg L^3,
                  \ 0<\|\Lambda/k\|\leq c/R}}
 e\!\left({b-a\over4}-{X\delta^2\over4k}\right)
 \sum_{2n+1\in\mathcal G_{a,b}}
 \mathfrak B^\circ_{a,b,k}(2n+1)e(-n\Lambda/k).     \tag{79.41}
\]
The required bound must keep the outer sum outside absolute values and
must exploit the literal complete coefficient.  Equivalently, a future
\(TT^*\), large-sieve, or primitive-ray theorem has to control both the
\(\mu_R\)-density part and the centered discrepancy
\({\bf1}_{\{\|\Lambda/k\|\leq c/R\}}-\mu_R\); controlling only the
excess incidence cannot remove the baseline (79.40).

There are two explicit limitations to the no-go statement.  First, the
application of (79.27) with \(R>1\) to the literal symbol needs a
populated interior subblock with \(N_{a,b}\geq R\); the packet supplies
only the upper bound \(N_{a,b}\ll G\).  The averaging theorem itself is
unconditional for every frozen populated collection, and the standard
positive interior support used in Round 78 supplies the relevant model
control, but no new lower-support theorem is asserted here.  Second,
(79.40) is a coefficient-*scale* lower-capacity diagnostic; no uniform
lower bound for the actual complex variation \(\mathcal V_{a,b,k}\) is
claimed.  Neither limitation affects the rigorous upper closure
(79.16) or the incidence sharpness/no-inverse conclusion for (79.7)
alone.

# 5. Control tests and outcomes.

- **External normalization, parity and primitivity:** (79.18)--(79.21)
  retain the factor \(1/2\), the nearest-integer orientation, odd
  \(a,b\), even \(b-a=2q\), and \((a,b)=1\iff(m,q)=1\).  The literal
  open \(k\)-interval is used throughout.

- **Trivial capacity before saving:** (79.28) is \(ADK\).  The proven
  saving is exactly \(R\), with a minimum against the actual empty,
  singleton, or short \(k\)-interval.  No saving is claimed at a
  one-point interval merely because its dyadic scale \(K\) is large.

- **Exact versus metric:** exact resonance is \(\Lambda=p=\ell k\),
  hence \(k\mid p\), and is closed by (79.34).  A metric resonance only
  places the integer \(p=\ell k\) in the strip (79.29).  The
  \(O(K/R)\) distinct strip integers are indispensable.  The random
  baseline remains after all exact equalities are deleted.

- **Near-square nonsquares:** for \(q=1\) (that is, \(b=a+2\)),
  \(u\asymp A^{-1}\), \(K\asymp J/A\), and
  \(c_{a,b,k}\asymp J^{-1}\).  Formula (79.39) has endpoint error
  \(O(J)\), while its main term is \(J^2/R\); since
  \(R\leq J^{1/2}/A\), the relative error is negligible.  Thus
  near-square rays are not removed by root spacing.  Their positive
  capacity is covered by (79.15), and only those satisfying (79.16)
  close absolutely.

- **Large square factors and perfect powers in the rays:** (79.24)
  allows arbitrary \(r\), including \(a=d_1x^2\), \(b=d_2y^2\) with
  large \(x,y\), and distinguishes the squarefree kernel
  \(\mathfrak d\).  Exact injectivity remains valid; same-field norm
  spacing improves to the second threshold in (79.38), still far
  outside the allowed metric range.

- **Perfect-square and fourth-power \(X\):** if \(X=T^2\) or \(T^4\)
  with integer \(T\), then
  \(X(m-r\sqrt{\mathfrak d})\) is irrational for
  \(\mathfrak d>1\), so the exact nonsquare set is empty.  Metric
  resonances are not thereby empty and remain governed by (79.23).
  This is consistent with, but distinct from, the already removed
  coherent square-ray fourth-power control.

- **All metric windows:** (79.23) is uniform for every dyadic
  \(1\leq R\leq N_{a,b}\).  At \(R=1\), \(\mu_R\asymp1\) (and the
  window is universal if the harmless majorization constant is at least
  \(1/2\)); at \(R\asymp G\) and at intermediate \(R\), (79.27) gives
  the matching \(1/R\) density whenever the lift block is populated.

- **Endpoints, stars, saddle entry/exit and collars:** no endpoint or
  transition mode is deleted.  They stay in
  \(\mathfrak B^\circ\) and are used only through the complete
  Round-77 variation (79.31).  The previously accepted
  \(O(L^2\log(2+L))\) collar/endpoint ledger is unchanged.

- **Adversarial coefficients:** (79.15) is deliberately labelled a
  positive capacity.  Phase-conjugated outer coefficients can realize
  that capacity, so incidence plus the envelope cannot prove a theorem
  for arbitrary coefficients.  The future estimate (79.41) must use
  the actual profiles, floors, finite lift interval and both saddle
  transitions.

- **Rank-one self-return:** neither the divisor strip nor (79.18)
  creates a second curvature direction.  Poisson/B-process in the
  reciprocal variable returns the original \(m\)-phase and coefficient
  problem, so no additional saving is entered in the ledger.

- **Downstream scope:** the report closes exact nonsquare centers and
  the positively safe region (79.16) only.  It does not promote the
  full transposed energy, signed cone, \(M9\!-\!M2\), \(M9\), endpoint
  uniformity, or the Gauss-circle exponent.

# 6. Dependencies and artifacts used.

The derivation used only the permitted selected context:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/briefs/nonsquare_reciprocal_incidence_attack.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reviews/conductor_round77_adjudication.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/reviews/conductor_round78_adjudication.md`.

No sibling Round-79 report, external source, or numerical experiment was
used.  The elementary divisor bound is already an accepted internal
dependency.  All computation in this report is algebraic or analytic.

# 7. Recommended state effect.

**Promote, after seam review,** the following scoped internal facts:

1. the exact \((m,q,u)\) normal form (79.18)--(79.21);
2. the metric divisor-strip incidence theorem (79.23), including its
   exact factor-\(R\) coefficient ledger (79.15);
3. the exact nonsquare rational-ratio rigidity and the
   \(O_\varepsilon(LX^\varepsilon)\) closure (79.34);
4. the positive closure of blocks \(AJD^3\ll L^3\);
5. the random-density no-go: the \(ADK/R\) metric population is sharp,
   may be strictly nonexact and may span many squarefree kernels, so a
   classification of every metric incidence as algebraic is false.

**Retain as open** the signed hard survivor (79.41).  The next theorem
must be a complete-coefficient, outside-absolute signed correlation
estimate on \(AJD^3\gg L^3\), not another coefficient-blind incidence
count.  Make no status change to the full top energy or any downstream
global obligation.
