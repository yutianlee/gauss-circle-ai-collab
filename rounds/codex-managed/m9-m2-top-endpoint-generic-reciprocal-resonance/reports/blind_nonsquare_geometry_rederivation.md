# 1. Result: lemma or no-go result.

There is a uniform metric-incidence saving which does not require replacing
the metric window by exact divisibility.  Put

\[
 u_{a,b}:=(\sqrt b-\sqrt a)^2,
 \qquad
 P=P(A,D,G):=\#\{(a,b)\in\mathscr P_L^{\rm ns}:
 a\asymp A, b-a\asymp D, G_{a,b}\asymp G\}.
\]

Then, for every allowed block and every \(R\geq1\),

\[
 \boxed{\quad
 \mathcal I_{\rm ns}(A,D,K,G;R)
 \ll_{\varepsilon,c} X^\varepsilon P\left(1+{K\over R}\right)
 \ll_{\varepsilon,c}X^\varepsilon AD\left(1+{K\over R}\right).
 \quad}                                                     \tag{R79.1}
\]

The elementary capacity is \(\mathcal I_{\rm ns}\ll_c PK\ll_c ADK\),
so (R79.1) saves

\[
 {K\over 1+K/R}={KR\over K+R}\asymp \min(K,R)               \tag{R79.2}
\]

up to \(X^\varepsilon\), whenever that quantity is unbounded.  The
saving is therefore real at intermediate and narrow windows, but is not
uniformly nontrivial at \(R=1\) or \(K\asymp1\).

There is also an exact nonsquare inverse statement.  Two distinct
primitive ordered nonsquare rays cannot both have an exact resonance at
the same \(X\).  Quantitatively, two distinct rays in one block cannot
both meet the metric window if

\[
 R>C_c A^5D^2K^7.                                           \tag{R79.3}
\]

If their products have the same squarefree kernel, the sharper threshold
is

\[
 R>C_c AD^2K^3.                                             \tag{R79.4}
\]

Above (R79.3), all incidences in the block lie on one ray and have one
common integer product \(\ell k\); consequently
\(\mathcal I_{\rm ns}\ll_\varepsilon X^\varepsilon\).  These thresholds
are uniform but generally far finer than the available range \(R\leq
N_{a,b}\ll G\), so this algebraic inverse statement does not by itself
close the intended range.

At the accepted coefficient scale, (R79.1) yields the positive bound

\[
 \boxed{\quad
 \mathcal A_{\rm ns}^{A,D,K,G}(R)
 \ll_\varepsilon X^\varepsilon
 J D^2\sqrt{AG}\left(K^{-1/2}+R K^{-3/2}\right).
 \quad}                                                     \tag{R79.5}
\]

This is only an exceptional-set/positive-diagnostic theorem.  A
phase-conjugated coefficient construction saturates the Abel factor at
scale \(\mathcal V_{a,b,k}R\).  Hence no signed primitive-ray estimate
follows from the incidence and variation data alone.  The rigorous
no-go is: the smallest remaining signed fiber correlation identified in
Section 4 needs information about the literal coefficients beyond
(79.3).

# 2. Exact statement and hypotheses.

All constants below may depend on the fixed dyadic comparison constants
in (79.9) and on the absolute window constant \(c\), but not on
\(X,L,A,D,K,G,R\).  The hypotheses are exactly those in the packet:
\(X>0\), \(J=\sqrt X\), \(1\leq L\leq H\leq J^{1/2}\), primitive odd
coprime \(a<b<4a\), \(ab\ne\square\), the open interval (79.2), and the
full metric error in (79.8).  No regularity of the opaque set
\(\mathcal G_{a,b}\) beyond the stated facts is assumed.

The conclusions are the following.

1. **Metric divisor-strip theorem.**  If \(P=P(A,D,G)\), then (R79.1)
   holds for every real \(X\), every \(R\geq1\), and empty, one-point, or
   longer \(k\)-intervals.  More precisely, for each fixed ray the number
   of \((k,\ell)\) is

   \[
    \ll_{\varepsilon,c}(AK^2)^\varepsilon
       \left(1+{K\over R}\right).                            \tag{R79.6}
   \]

2. **Exact-resonance isolation.**  If two incidences satisfy
   \(\Lambda_i=\ell_i k_i\) exactly at the same real \(X\), then their
   primitive rays are identical.  On that ray all exact incidences have
   the same integer \(M=\Lambda=\ell k\), so their number is at most
   \(\tau(M)\ll_\varepsilon X^\varepsilon\).

3. **Fine metric inverse theorem.**  For two metric incidences in the
   same block, define \(M_i=2\ell_i k_i\).  If the rays are distinct, then

   \[
    R\ll_c A^5D^2K^7.                                       \tag{R79.7}
   \]

   If the squarefree kernels of \(a_1b_1\) and \(a_2b_2\) coincide, then
   (R79.7) improves to \(R\ll_c AD^2K^3\).  Thus (R79.3)--(R79.4) have
   the stated inverse interpretation.

4. **Integral perfect-power control.**  If \(X\) is a positive integer
   (in particular an integral perfect square or fourth power), a
   nonsquare ray has no exact resonance.  Any metric incidence obeys

   \[
    R\ll_c XAK\asymp {A^3K^3\over D^2},                      \tag{R79.8}
   \]

   where the last comparison follows from the nonempty literal
   \(k\)-interval and \(a\asymp A,d\asymp D,k\asymp K\).
   This is again only an ultra-fine exclusion, not a claim that ordinary
   metric windows are empty.

5. **Coefficient ledger.**  With

   \[
    V:=X^\varepsilon{JD\sqrt G\over \sqrt A K^{3/2}},        \tag{R79.9}
   \]

   the capacities and the proved saving are

   \[
   \begin{array}{c|c}
   \text{quantity}&\text{blockwise upper bound}\ \\ \hline
   \text{incidence capacity}&PK\leq ADK\\
   \text{unwindowed Abel-}1\text{ capacity}&VPK\\
   \text{trivial window capacity}&VRPK\\
   \text{proved window bound}&VRP(1+K/R)=VP(R+K).
   \end{array}                                               \tag{R79.10}
   \]

   Inserting \(P\leq AD\) gives (R79.5), while the trivial window
   capacity is

   \[
    \ll_\varepsilon X^\varepsilon
       J D^2\sqrt{AG}\,R K^{-1/2}.                           \tag{R79.11}
   \]

   On blocks where \(D\ll A\) and hence \(K\asymp JD/A\), (R79.5)
   becomes

   \[
    \mathcal A_{\rm ns}^{A,D,K,G}(R)
    \ll_\varepsilon X^\varepsilon
    \left(\sqrt J\,A D^{3/2}\sqrt G
       +{R A^2\sqrt{DG}\over\sqrt J}\right),               \tag{R79.12}
   \]

   whereas (R79.11) becomes
   \(X^\varepsilon R\sqrt J\,A D^{3/2}\sqrt G\).  The ratio
   of the proved to trivial capacities is
   \(\ll X^\varepsilon(1/R+1/K)\), exactly matching (R79.2).
   Outside the stated \(D\ll A\) reduction, (R79.5) with the literal
   interval is the asserted ledger.

# 3. Proof or derivation.

Write \(d=b-a\) and \(u=u_{a,b}=\delta^2\).  On a block,

\[
 u={d^2\over(\sqrt a+\sqrt b)^2}\asymp {D^2\over A}.         \tag{R79.13}
\]

The open \(k\)-interval gives two strict inequalities which will be used
without rounding them:

\[
 {b k^2\over2}<\Lambda<2ak^2.                               \tag{R79.14}
\]

Indeed, squaring \(k<J\delta/\sqrt b\) gives
\(bk^2<J^2\delta^2=2\Lambda\), and squaring
\(k>J\delta/(2\sqrt a)\) gives \(2\Lambda<4ak^2\).
Consequently \(\Lambda\asymp AK^2\) on every nonempty block.

For completeness, the dyadic Abel majorant has the stated orientation.
If \(t=\|\theta\|\), the geometric partial sums are bounded by
\(\min(N,(2t)^{-1})\).  Dyadic \(R\)'s satisfying
\(R\leq \min(N,c/t)\) have total weight comparable to
\(\min(N,t^{-1})\); the leading \(1\) handles the remaining bounded
case.  Taking \(\theta=\Lambda/k\), nearest-integer distance gives

\[
 \left|{\Lambda\over k}-\ell\right|\leq {c\over R}
 \quad\Longleftrightarrow\quad
 |\Lambda-\ell k|\leq {ck\over R}.                          \tag{R79.15}
\]

Thus neither the factor \(1/2\) in \(\Lambda=Xu/2\) nor the orientation
\(\Lambda-\ell k\) is lost.

Now fix one ray and put \(m=\ell k\).  Since \(k\asymp K\), (R79.15)
places the positive integer \(m\) in an interval of length
\(O_c(K/R)\) centered at the real number \(\Lambda\).  There are
\(O_c(1+K/R)\) possible integers \(m\).  For each such \(m\), the
integer \(k\) is a divisor of \(m\), and \(\ell=m/k\) is fixed.  By
(R79.14), \(m\ll_c AK^2\), and the elementary divisor estimate gives

\[
 \#\{(k,\ell)\text{ on this ray}\}
 \ll_{\varepsilon,c}(AK^2)^\varepsilon(1+K/R).               \tag{R79.16}
\]

If \(\ell=0\), (R79.14)--(R79.15) imply \(AKR\ll_c1\); all three
parameters are then bounded and this case is absorbed in (R79.16).
This proof counts the actual integers in an open interval, so it remains
valid when that interval is empty or contains one point.  Summing
(R79.16) over the \(P\) rays proves the first inequality in (R79.1).
The second follows merely by counting \(O(A)\) possible \(a\)'s and
\(O(D)\) possible \(d\)'s.

The harmless divisor loss may be written as \(X^\varepsilon\).  Indeed,
nonemptiness of \(\mathcal G_{a,b}\), together with
\(N_{a,b}\ll G_{a,b}\asymp L/b\), gives \(b\ll L\), hence
\(A\ll X^{1/4}\).  Also (79.2) gives \(k<J\), hence
\(K\ll X^{1/2}\).  Therefore \((AK^2)^\varepsilon\) is absorbed after
renaming \(\varepsilon\).

For the algebraic part, let \(q=q(a,b)>1\) be the squarefree kernel of
\(ab\), and let \(h=\sqrt{ab/q}\in\mathbb Z_{\geq1}\).  Then

\[
 u=a+b-2h\sqrt q                                             \tag{R79.17}
\]

is a quadratic algebraic integer.  The following injectivity is the key
nonsquare fact:

\[
 {u_{a_1,b_1}\over u_{a_2,b_2}}\in\mathbb Q
 \quad\Longrightarrow\quad (a_1,b_1)=(a_2,b_2).             \tag{R79.18}
\]

If the two squarefree kernels are different, (R79.18) follows from the
linear independence over \(\mathbb Q\) of
\(1,\sqrt{q_1},\sqrt{q_2}\).  If they are the same, comparison of the
rational and irrational coefficients gives

\[
 {a_1+b_1\over h_1}={a_2+b_2\over h_2}.
\]

But \((a+b)/h=\sqrt q\,(\sqrt{b/a}+\sqrt{a/b})\), and
\(x+x^{-1}\) is strictly increasing for \(x>1\).  Hence
\(b_1/a_1=b_2/a_2\); coprimality makes the two primitive ordered pairs
identical.  If two exact resonances coexist, then
\(u_1/u_2=(\ell_1k_1)/(\ell_2k_2)\in\mathbb Q\), proving exact
isolation.  On the resulting single ray, \(\ell k=\Lambda\) is fixed,
so the divisor bound applies.

For quantitative metric isolation, set

\[
 E_i=Xu_i-M_i,qquad M_i=2\ell_i k_i.
\]

The window gives \(|E_i|\ll_c K/R\), while (R79.13)--(R79.14) give
\(M_i\ll_c AK^2\).  Cross-multiplication eliminates the arbitrary real
number \(X\):

\[
 \eta:=M_2u_1-M_1u_2=E_1u_2-E_2u_1,
 \qquad
 |\eta|\ll_c {D^2K\over AR}.                                \tag{R79.19}
\]

For distinct rays, (R79.18) says \(\eta\ne0\).  It is an algebraic
integer in a field of degree at most four.  Every nonphysical conjugate
of \(u_i\) has size \(O(A)\), and hence every conjugate of \(\eta\) has
size \(O_c(A^2K^2)\).  Its nonzero rational-integer norm therefore gives

\[
 |\eta|\gg_c (A^2K^2)^{-3}=A^{-6}K^{-6}.                    \tag{R79.20}
\]

Combining (R79.19)--(R79.20) proves (R79.7).  If \(q_1=q_2\), the field
has degree two, so only one other conjugate occurs and
\(|\eta|\gg_c A^{-2}K^{-2}\), which proves (R79.4).  Once
\(R>C_cA^5D^2K^7\), only one ray is possible.  On that ray,
(R79.19) reduces to \(|M_1-M_2|\ll_c K/R<1\), so all incidences have
the same \(M_i\), and a final divisor bound gives
\(\mathcal I_{\rm ns}\ll_\varepsilon X^\varepsilon\).

If \(X\in\mathbb Z_{>0}\), then \(E=Xu-2\ell k\) is a nonzero
quadratic algebraic integer: it cannot vanish because \(u\) is
irrational.  Its conjugate is \(O_c(XA)\), using (R79.14), so its
nonzero integer norm gives \(|E|\gg_c (XA)^{-1}\).  Comparison with
\(|E|\ll_c K/R\) proves the first part of (R79.8).  Finally,
\(Xu=2\Lambda\asymp AK^2\) and (R79.13) give
\(X\asymp A^2K^2/D^2\), proving the displayed equivalent scale.

To obtain the coefficient ledger, use
\(\delta\asymp D/\sqrt A\) in (79.3).  Multiplication of (R79.1) by
\(VR\) gives

\[
 VRP(1+K/R)=VP(R+K),                                        \tag{R79.21}
\]

and substituting \(P\leq AD\) proves (R79.5).  The remaining formulas
in (R79.10)--(R79.12) are direct algebraic substitutions; in particular
no absolute sum beyond the positive diagnostic is being disguised.

Finally, the limitation is rigorous at the information level supplied
by the packet.  On an interval of \(N\) consecutive \(n\)'s, let
\(\theta=\Lambda/k\) and consider the coefficient analogue

\[
 \widetilde B_n=q_0e(n\theta).
\]

Its discrete variation norm (the norm used in the step-two Abel bound) is
\(\ll |q_0|(1+N\|\theta\|)\).  In a window
\(\|\theta\|\leq c/R\), choosing
\(|q_0|\asymp V/(1+N/R)\) makes that norm \(\ll V\), while

\[
 \left|\sum_n\widetilde B_ne(-n\theta)\right|
 =|q_0|N\asymp V\min(N,R).                                  \tag{R79.22}
\]

For \(R\leq N\) this is \(\asymp VR\), exactly the Abel-window scale.
Such analogues can be phase-aligned across incidences.  They are not a
replacement for the literal coefficient; rather, they prove that
variation plus incidence alone cannot certify cancellation for that
literal coefficient.

# 4. First doubtful or unproved step.

There is no unproved step in (R79.1), the exact-isolation lemma, the
fine-scale norm bounds, or the coefficient ledger.  The first unproved
step toward the signed top energy is a signed correlation within the
integer-product fibers exposed by the proof.

At the packet level, define the actual mode amplitude

\[
 Z_{a,b,k}:=
 \sum_{2n+1\in\mathcal G_{a,b}}
 \mathfrak B^\circ_{a,b,k}(2n+1)e(-n\Lambda/k),              \tag{R79.23}
\]

For each resonant \((a,b,k)\), choose one nearest admissible
nonnegative integer \(\ell\) (with a fixed tie rule), and let
\(\Omega_m(R)\) contain those actual modes for which \(\ell k=m\).
After the diagonal cardinality is controlled by (R79.1), the smallest
still-uncontrolled packet-expressible signed piece is

\[
 \mathcal E_{\rm fib}^{\rm off}(R)
 :=\sum_m
   \sum_{\substack{\omega\ne\omega'\\
                    \omega,\omega'\in\Omega_m(R)}}
       Z_\omega\,\overline{Z_{\omega'}}.                    \tag{R79.24}
\]

A later formula may attach additional literal outer signs or weights;
none are supplied in the packet, so they cannot be invented here.  A
signed \(TT^*\), large-sieve, or primitive-ray estimate must control at
least the appropriately weighted version of (R79.24), and also any
off-fiber terms its exact kernel retains.  The positive count
(R79.1) and the individual bound \(|Z_{a,b,k}|\leq VR\) do not do so,
as (R79.22) demonstrates.  This is the first missing input, not an
unproved root-spacing assertion.

# 5. Control tests and outcomes.

- **Dyadic Abel identity:** Passed.  Summing dyadic weights up to
  \(\min(N,c/\|\theta\|)\), with the leading \(1\), gives the required
  \(\min(N,(2\|\theta\|)^{-1})\) scale.  Consecutive odd arguments are
  indexed by consecutive \(n\), so no extra factor two enters the
  phase.

- **Nearest-integer orientation and metric width:** Passed.  The proof
  uses \(|\Lambda-\ell k|\leq ck/R\), not exact divisibility and not the
  reversed quotient.  It retains \(\Lambda=X(\sqrt b-\sqrt a)^2/2\).
  Nonintegral \(\Lambda\) is handled by the real interval for
  \(m=\ell k\).

- **Primitive-square excision:** Passed.  Every incidence sum is over
  \(\mathscr P_L^{\rm ns}\).  The removed square family is neither
  counted nor reproved.  Nonsquareness enters only in (R79.17)--(R79.20),
  where it is actually needed.

- **Near-square nonsquares:** Passed.  For odd \(a\), the pairs
  \((a,a+2)\) are primitive nonsquares, and (R79.13) records the small
  scale \(u\asymp D^2/A\) exactly.  No claim of uniform separation is
  inferred merely from \(ab\ne\square\).  The powers of \(D\) in
  (R79.3)--(R79.5) remain visible.

- **Large square factors:** Passed.  Formula (R79.17) allows arbitrary
  \(h=\sqrt{ab/q}\), including families such as
  \(a=s^2,b=3t^2\) with coprime odd \(s,t\), \(3\nmid s\), and
  \(s^2<3t^2<4s^2\), for which
  \(ab=3(st)^2\) has an arbitrarily large square factor.  The norm bound
  uses the conjugate size \(O(A)\), not a false lower bound in terms of
  the squarefree kernel.

- **Perfect squares and fourth powers of \(X\):** Passed.  Integral
  perfect squares and fourth powers admit no exact nonsquare resonance,
  but metric resonances are not discarded.  Their only elementary
  exclusion here is the explicit ultra-fine condition (R79.8).

- **Exact and nonexact resonances:** Passed.  Exact resonances are
  isolated to one ray.  Conversely, nonsquareness alone does not forbid
  an exact resonance for arbitrary real \(X\): for a fixed primitive
  nonsquare coordinate pair, choose sufficiently large integers
  \(k,\ell\) with
  \(bk/2<\ell<2ak\), and set \(X=2\ell k/u\).  Then
  \(J\delta=\sqrt{2\ell k}\), and the two displayed inequalities are
  exactly equivalent to the open interval (79.2).  This is a
  coordinate-level no-go to any individual root-separation argument
  based only on nonsquareness; it makes no unsupported assertion about
  membership in the opaque set \(\mathcal G_{a,b}\).

- **Empty and one-point \(k\)-intervals:** Passed.  The divisor-strip
  proof counts actual integer divisors satisfying the literal open
  interval and never replaces their count by its length.  Zero and one
  therefore require no exceptional argument.

- **\(R=1\), intermediate \(R\), and \(R\asymp G\):** Passed.  At
  \(R=1\), (R79.1) correctly gives no forced power saving.  At an
  intermediate window it saves \(\asymp\min(K,R)\), and at
  \(R\asymp G\) it saves \(\asymp\min(K,G)\), always up to
  \(X^\varepsilon\).  The algebraic one-ray conclusion is asserted only
  when the explicit much stronger thresholds hold.

- **Saddle transitions, endpoint stars, and fixed collars:** Passed as
  an incidence control, not as a signed estimate.  Nothing in the proof
  alters, truncates, freezes, or models
  \(\mathfrak B^\circ_{a,b,k}\); all of those features remain inside the
  accepted variation \(\mathcal V_{a,b,k}\).  Consequently they still
  have to be used in any proof of (R79.24).

- **Coefficient adversaries:** Passed.  Equation (R79.22) is an explicit
  phase-conjugated analogue with the same allowed variation scale and
  with Abel size \(\asymp VR\).  It proves that the positive incidence
  theorem is not a coefficient-blind signed theorem.  It is not claimed
  to be the literal profile.

- **Rank-one reciprocal self-return:** Passed.  The metric geometry
  already reduces exactly to the fibers \(m=\ell k\), with the reverse
  operation being divisor enumeration \(k\mid m\).  Reapplying a
  one-dimensional reciprocal transform merely reorganizes these same
  fibers.  No second saving is credited without an independent signed
  estimate for (R79.24).

# 6. Dependencies and artifacts used.

Only the following two permitted artifacts were used:

1. `rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/briefs/blind_nonsquare_geometry_rederivation.md`;
2. `rounds/codex-managed/m9-m2-top-endpoint-generic-reciprocal-resonance/derivation_packet.md`.

The derivation is entirely analytical.  No computation, web source,
repository state, strategy file, earlier report, sibling report, source
card, or shared proof-state file was read or used.

# 7. Recommended state effect.

**Promote after independent validation** the metric divisor-strip bound
(R79.1), its coefficient ledger (R79.5), and the exact/fine nonsquare
isolation statements (R79.3)--(R79.4) as narrowly scoped incidence
claims.  They provide a genuine \(\min(K,R)\) mode-count saving and an
ultra-fine one-ray inverse theorem.

Make **no change** to any signed cone, transposed-energy, \(M9\!-\!M2\),
\(M9\), endpoint-uniformity, or global-exponent claim.  The next state
effect should depend on a proof or a rigorous obstruction for the
literal signed fiber correlation (R79.24); replacing it by the positive
bound (R79.5) would be invalid.
