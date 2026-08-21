## 1. Result

**Result: exact algebraic lemma plus a rigorous statement-only no-go.**  For every
complex, zero-extended row \(F_a\), the proposed Gram has the exact Fejer
correlation expansion
\[
 {\cal G}^{\rm act}_H
 =H{\cal E}_{\rm act}
 +2\Re\sum_{d=1}^{H-1}(-1)^d(H-d){\cal C}(d),
 \qquad
 {\cal E}_{\rm act}:=\sum_{a,q}|F_a(q)|^2,\quad
 {\cal C}(d):=\sum_{a,q}F_a(q)\overline{F_a(q+d)}.
\]
Thus the diagonal coefficient mass is \(H\), the two-sided nonzero-shift
coefficient mass is \(H(H-1)\), and the full triangular-kernel mass is
\(H^2\).  Under the explicitly stated arithmetic hypotheses in Section 2,
each off-shift stationary cross-term has an exact zero/near/separated
partition determined by an integer determinant.

The target bound is not derivable from the statement packet.  The packet
gives neither a literal atomic formula for \(F_a(q)\), a relation between
\({\cal E}_{\rm act}\) and \(E_0\), nor the stationary kernel which turns
separation of the displayed determinant into decay.  Indeed, rescaling an
otherwise admissible abstract row by a scalar changes the Gram quadratically
while leaving the displayed \(E_0\) and \(\rho\) unchanged.  This is a no-go
for deduction from the packet, not a disproof for the fixed actual symbol.
The coefficient-uniform analogue is false by the explicit adversarial-phase
control in Section 5.

## 2. Exact statement and hypotheses

Let
\[
 S_a\subseteq
 \{q\in{\mathbb Z}:0<q<3a/2,\ (a,q)=1\}
\]
be the support left after all finite-lift, owner, interval, discrepancy, and
physical entry/exit restrictions, and extend \(F_a\) by zero on
\({\mathbb Z}\setminus S_a\).  No reality or support symmetry is assumed.
Let \(H\) be an integer with \(1\leq H\leq D_{\rm ray}\).  Define
\({\cal E}_{\rm act}\) and \({\cal C}(d)\) as in Section 1.

For the determinant ledger, make the additional literal hypothesis that a
stationary expansion of every cross-term is indexed by positive integers
\(g,k,g',k'\), with
\[
 v=a+2q,\qquad v_d=v+2d,\qquad
 \alpha=g'k,\qquad\beta=gk',
\]
and that its displayed comparison coordinate is
\[
 \Delta=\frac{g'}{k'v_d^{3/2}}-\frac{g}{kv^{3/2}}.
\]
For any \(\eta>0\), partition those stationary terms into
\[
 {\mathfrak I}_0=\{\Delta=0\},\qquad
 {\mathfrak I}_{\rm near}(\eta)=\{0<|\Delta|\leq\eta\},\qquad
 {\mathfrak I}_{\rm sep}(\eta)=\{|\Delta|>\eta\}.
\]
Writing the corresponding correlation sums as
\({\cal C}_0(d),{\cal C}_{\rm near}(d;\eta),{\cal C}_{\rm sep}(d;\eta)\)
is exact provided the stationary expansion really exhausts
\({\cal C}(d)\).  Define
\[
 {\cal O}_\star
 :=2\Re\sum_{d=1}^{H-1}(-1)^d(H-d){\cal C}_\star(d)
 \quad
 (\star=0,\ {\rm near},\ {\rm sep}).
\]
The exact target, with its implicit constant written as \(C_\varepsilon\),
is equivalent for a chosen \(H\) to the single signed inequality
\[
 {\cal O}_0+{\cal O}_{\rm near}+{\cal O}_{\rm sep}
 \leq
 C_\varepsilon X^\varepsilon\frac{H^2}{\rho}E_0
 -H{\cal E}_{\rm act}.                                      \tag{2.1}
\]
This is the weakest sufficient complete nonzero-shift inequality: it is
also necessary for that same constant.

## 3. Proof and derivation

Expanding the square and putting \(d=t-r\) gives
\[
 \begin{aligned}
 {\cal G}^{\rm act}_H
 &=\sum_{a,n}\sum_{0\leq r,t<H}
   (-1)^{r+t}F_a(n+r)\overline{F_a(n+t)}\\
 &=\sum_{d=-(H-1)}^{H-1}(-1)^d(H-|d|)
   \sum_{a,q}F_a(q)\overline{F_a(q+d)}.
 \end{aligned}
\]
Zero extension makes this identity exact at every support entry and exit.
Since \({\cal C}(-d)=\overline{{\cal C}(d)}\), pairing \(d\) and \(-d\)
proves Section 1 without assuming that \(F_a\) is real.  The coefficient
ledger follows from
\[
 H+2\sum_{d=1}^{H-1}(H-d)=H^2.
\]
Before coprimality and actual masks, a row contains at most
\[
 Q_a:=\left\lceil\frac{3a}{2}\right\rceil-1
\]
positive \(q\)'s, and shift \(d>0\) has at most
\((Q_a-d)_+\) candidate pairs.  The actual pair set is
\[
 \{q:q,q+d\in S_a,\ (a,q)=(a,q+d)=1\},
\]
so masks and entry/exit can only reduce this raw count; they need not reduce
the weighted mass.

The determinant has the exact rationalization
\[
 \Delta
 =\frac{\alpha v^{3/2}-\beta v_d^{3/2}}
 {kk'(vv_d)^{3/2}}
 =\frac{{\mathfrak D}}
 {kk'(vv_d)^{3/2}
  \bigl(\alpha v^{3/2}+\beta v_d^{3/2}\bigr)},               \tag{3.1}
\]
where
\[
 {\mathfrak D}:=\alpha^2v^3-\beta^2v_d^3\in{\mathbb Z}.
\]
Consequently \(\Delta=0\) if and only if \({\mathfrak D}=0\), while for
\({\mathfrak D}\neq0\)
\[
 |\Delta|\geq
 \frac{1}
 {kk'(vv_d)^{3/2}
  \bigl(\alpha v^{3/2}+\beta v_d^{3/2}\bigr)}.               \tag{3.2}
\]
This is the only unconditional separation supplied by integrality.

The zero set can be classified exactly.  Let
\(v=cx^2\) and \(v_d=c'y^2\), where \(c,c'\) are squarefree.  Prime
valuations in \(\alpha^2v^3=\beta^2v_d^3\) show that \(v/v_d\) is a rational
square, hence \(c=c'\); after taking the positive square root, zero is
equivalent to
\[
 \alpha x^3=\beta y^3.
\]
Conversely these two conditions give zero.  More generally
\[
 {\mathfrak D}=cU^2-c'V^2,\qquad
 U=\alpha cx^3,\quad V=\beta c'y^3,                          \tag{3.3}
\]
and the shift condition is \(c'y^2-cx^2=2d\).  Thus small nonzero
determinants lie on constrained generalized-Pell equations; they cannot be
discarded as generic spacing.

Equation (2.1) follows by inserting the set-theoretic determinant partition
into the exact Gram identity.  A stronger but easier absolute-value package
would be
\[
 H{\cal E}_{\rm act}\leq \tfrac12 T,\qquad
 |{\cal O}_0|+|{\cal O}_{\rm near}|+|{\cal O}_{\rm sep}|
 \leq\tfrac12 T,\qquad
 T=C_\varepsilon X^\varepsilon H^2E_0/\rho.                 \tag{3.4}
\]
If \({\cal E}_{\rm act}\asymp_{X^\varepsilon}E_0\), the first inequality
uses capacity \(H\gtrsim_{X^\varepsilon}\rho\).  Since \(H\leq D_{\rm ray}\),
such a diagonal-separated proof requires, at the scale level,
\[
 \rho\lesssim_{X^\varepsilon}D_{\rm ray},
 \qquad\text{equivalently}\qquad
 AJD_{\rm ray}^2\lesssim_{X^\varepsilon}L^3.                \tag{3.5}
\]
Condition (3.5) is not necessary if one proves the sharper signed
cancellation (2.1), but it is the precise capacity obstruction to treating
the diagonal and the absolute off-shift ledger separately.

## 4. First doubtful or unproved step

The first missing literal datum is the atomic stationary formula
\[
 F_a(q)=\sum_{\iota\in{\cal I}_{a,q}}W_{a,q}(\iota)
\]
together with the exact ranges of \(g,k\), all lift multiplicities and
masks, and the cross-term kernel (including its dependence on \(\Delta\)).
The packet only says that a stationary comparison “contains” \(\Delta\).
It does not establish that every term of \({\cal C}(d)\) has such labels,
that the comparison equals rather than approximates the actual
correlation, or what residual is produced by moving intervals,
metric discrepancy, and physical entry/exit.  Therefore the formal
partition in Section 2 cannot yet be promoted as a partition of the actual
correlation.

Immediately after that datum, the first missing quantitative inputs are
\({\cal E}_{\rm act}\ll X^\varepsilon E_0\) and a weighted estimate strong
enough to imply (2.1), with the zero, constrained-Pell near set, separated
set, and support residual all included.  A raw count of determinant values
does not supply this estimate.  No canonical energy, named campaign
quantity, or exponent is inferred here.

## 5. Required controls and outcomes

- **\(D_{\rm ray}\asymp1\).**  Input: integer \(1\leq H\leq D_{\rm ray}\)
  with \(\rho>1\).  Expected invariant: no growing shift capacity.
  Observed: at \(D_{\rm ray}=1\), necessarily \(H=1\),
  \({\cal G}^{\rm act}_1={\cal E}_{\rm act}\), and there is no off-shift or
  determinant term at all.  The target then requires the independent bound
  \({\cal E}_{\rm act}\ll X^\varepsilon E_0/\rho\).  Implication: a
  determinant-cancellation proof cannot cover this case without a separate
  energy lemma.

- **Determinant zero.**  Input:
  \(a=7,q=1,d=8,v=9,v_d=25\), with
  \(g'=125,k'=1,g=27,k=1\).  Both primitive conditions hold,
  \(1,9<3a/2\), and
  \(125/25^{3/2}=27/9^{3/2}=1\).  Expected failure: a uniform nonzero gap
  without an exceptional ledger.  Observed: \(\Delta={\mathfrak D}=0\)
  exactly.  Implication: this arithmetic configuration must be retained
  whenever \(H\geq9\) and the unspecified lift and owner masks admit it;
  the packet does not say whether they do.

- **Near-square/Pell rays.**  Input: the squarefree decompositions in
  (3.3), together with \(c'y^2-cx^2=2d\).  Expected failure: “generic”
  determinant spacing may fail on Pell-type subfamilies.  Observed:
  \({\mathfrak D}=m\) is the constrained generalized-Pell equation
  \(cU^2-c'V^2=m\), and integrality gives only \(|m|\geq1\) off zero.
  Implication: a weighted count or cancellation theorem for these coupled
  constraints is required; (3.2) alone yields no scale saving.

- **Support entry/exit and degeneracy.**  Input: the actual zero-extended
  sets \(S_a\), compared with any stationary support
  \(\widetilde S_a\).  Expected invariant: the exact Gram identity keeps
  boundary terms, while a stationary replacement creates a residual.
  Observed: the residual at shift \(d\) is supported on the symmetric
  difference of the two pair sets and is bounded only tautologically by
  \[
   \sum_{\text{mismatched pairs}}|F_a(q)F_a(q+d)|
   \leq\frac12\sum_{\text{mismatched pairs}}
   \bigl(|F_a(q)|^2+|F_a(q+d)|^2\bigr).
  \]
  No bound on the number or energy of such mismatches is given; masks may
  create internal boundaries.  Implication: neither sharp endpoints nor
  \(uv=0\), repeated-denominator, or lift-boundary branches may be silently
  dropped.

- **Arbitrary-coefficient false analogue.**  Input: one primitive ray
  segment of length \(Q\geq H\), constant modulus \(w\), and adversarial
  phase \(F_a(q)=(-1)^q w\).  Such a segment is compatible with the displayed
  primitive-ray geometry, for example \(1\leq q\leq a-1\) with \(a\) prime.
  Expected failure: the outer \((-1)^r\) is cancelled by the chosen phase.
  Observed: every full window equals \((-1)^nHw\), so
  \[
   {\cal G}^{\rm adv}_H\geq(Q-H+1)H^2w^2,
   \qquad {\cal E}^{\rm adv}=Qw^2.
  \]
  For \(Q\gg H\) and normalization \({\cal E}^{\rm adv}=E_0\), this is of
  order \(H^2E_0\), not \(H^2E_0/\rho\).  Implication: no
  coefficient-uniform \(1/\rho\) gain follows from support, magnitudes, or
  determinant capacity alone; an actual-symbol cancellation property must
  be exhibited.

- **Raw versus weighted and signed variants.**  Input: the raw pair bound
  \((Q_a-d)_+\), versus the genuine products
  \(F_a(q)\overline{F_a(q+d)}\), and true, absolute, random, and adversarial
  phases.  Expected invariant: raw counts cannot be transferred to weighted
  mass, and the four sign models need not agree.  Observed: the Gram
  derivation is genuinely weighted and complex; the adversarial model above
  maximizes alignment, while the packet gives no literal true-symbol
  feature to test and no random-sign theorem.  Implication: raw and unsigned
  bounds do not establish (2.1).

- **Exact versus near resonance and real versus complex pairing.**  Input:
  \({\mathfrak D}=0\), \(0<|\Delta|\leq\eta\), and
  \(|\Delta|>\eta\), with arbitrary complex \(F_a\).  Expected invariant:
  exact and near ledgers remain separate, and conjugation is not replaced
  by a real-part shortcut inside a row entry.  Observed: the two-sided Gram
  pairs correlations only through
  \({\cal C}(-d)=\overline{{\cal C}(d)}\), which is valid for complex rows;
  the determinant zero classification does not control the near set.
  Implication: any later real or exact-resonance reduction needs additional
  symmetry or a near-determinant estimate.

- **Dyadic endpoints.**  Input:
  \(D_{\rm ray}=X^{1/4},X^{3/8},X^{1/2}\) and \(J=\sqrt X\).
  Expected invariant: the capacity condition is checked separately.
  Observed: (3.5) becomes respectively
  \(AX\lesssim L^3\), \(AX^{5/4}\lesssim L^3\), and
  \(AX^{3/2}\lesssim L^3\), up to \(X^\varepsilon\).  The packet gives no
  ranges for \(A,L\), so none can be certified and no endpoint may be
  crossed.  Implication: endpoint capacity remains open.

- **Named lower-bound families.**  Input available under the mandated
  isolation consists only of the names UNC, TS, and W-1 in the control
  document; their definitions, parity, coefficient envelopes, and scales
  are not in the allowed packet.  Expected failure: an absolute
  near-collision claim must survive them.  Observed: the literal test is not
  executable from the permitted files and is not recorded as passed.
  Implication: no absolute or unsigned near-determinant claim is eligible
  for promotion from this report.

## 6. Dependencies, isolation, and checks

This was a statement-only blind derivation.  The only artifacts read were:

- problems/gauss_circle.md;
- state/control_models.md;
- rounds/codex-managed/m9-m2-determinant-weighted-actual-gram/blind_statement.md;
- rounds/codex-managed/m9-m2-determinant-weighted-actual-gram/briefs/blind_determinant_gram_rederivation.md.

No proof-obligation state, proof draft, claimant or reviewer report, prior
Round-96--101 derivation, synthesis, validation matrix, web source, or
unlisted repository artifact was read.  No external computation is used as
evidence; every displayed control is exactly algebraically checkable.
Post-write checks found exactly seven numbered protocol headings, no
additional numbered heading, and no disallowed control byte.

## 7. Recommended state effect

**Recommended state effect: retain.**  Retain the Gram identity, triangular
capacity ledger, determinant rationalization, exact-zero classification,
and coefficient-adversary no-go as candidate evidence.  Do not promote the
actual-symbol target or any determinant saving.  The next admissible step is
to supply the literal atomic formula and prove the weighted signed inequality
(2.1), including determinant zero, constrained-Pell near terms, separated
terms, and support residual.  The arbitrary-coefficient analogue should be
rejected.

### Post-isolation seam audit (authorized follow-up)

This audit was appended after the blind report was closed.  It uses only
three claims supplied verbatim by the conductor in the follow-up message; no
new file or artifact was read.  The original blind provenance and conclusions
above are unchanged.

**Claim (i): conditionally correct, with essential fixed-row and box
hypotheses.**  To avoid collision with the shift notation, write
\(\delta\) for the squarefree integer called \(d\) in the supplied claim.
For
\[
 b=a+2q,\qquad b_s=b+2s,
\]
the argument in Section 3 gives, for positive integral variables,
\[
 \Delta=0
 \quad\Longleftrightarrow\quad
 b=\delta x^2,\quad b_s=\delta y^2,\quad
 \delta(y^2-x^2)=2s,\quad
 g'k\,x^3=gk'\,y^3.                                        \tag{7.1}
\]
This equivalence also requires that the two displayed reciprocal terms use
the same positive square-root branch.  For fixed \(a\) and fixed nonzero
\(s\), (7.1) gives
\[
 \delta(y-x)(y+x)=2s.
\]
Choosing \(\delta\mid 2|s|\), then the factor pair
\((|y-x|,y+x)\), gives at most
\(\sum_{\delta\mid2|s|}\tau(2|s|/\delta)
=\tau_3(2|s|)\ll_\varepsilon |s|^\varepsilon\) possibilities.
Parity, squarefreeness, positivity, \(q=(\delta x^2-a)/2\in\mathbb Z\),
the primitive conditions, and support masks only reduce this count.  The
fixed-\(a\) hypothesis is indispensable: with \(a\) also varying, this
factorization does not by itself give the asserted number of \(q\)'s.

For the lift count, let \(x=r x_0,y=r y_0\) with
\((x_0,y_0)=1\), and put \(A_1=g'k,B_1=gk'\).  The last equation in
(7.1) is equivalent to
\[
 A_1=t\,y_0^3,\qquad B_1=t\,x_0^3
\]
for a positive integer \(t\).  If
\[
 1\leq g,g'\ll G,\qquad 1\leq k,k'\ll K,\qquad N=GK,
\]
then \(A_1,B_1\ll N\), hence there are \(O(N)\) possible \(t\)'s, and each
of \(A_1,B_1\) has at most a divisor-function number of admissible
factorizations.  Provided all scales are \(X^{O(1)}\), the divisor bounds
are absorbed into \(X^\varepsilon\), proving
\[
 \#\{g,k,g',k'\text{ satisfying (7.1)}\}
 \ll_\varepsilon N X^\varepsilon
\]
per \(q\).  This normalization silently requires positive integral lifts,
common \(G,K\) boxes for primed and unprimed variables, and product upper
bounds \(g'k,gk'\ll GK\).  Oddness, dyadic lower bounds, finite support, and
owner masks only reduce the count.  The result is a raw multiplicity bound,
not a bound for the actual weighted mass.

**Claim (ii): the raw rational-window estimate is correct under the same
boxes, but its \(\eta\) is not a determinant threshold without rescaling.**
Set
\[
 \theta=(b_s/b)^{3/2},\qquad
 R=\frac{g'k}{gk'}=\frac{A_1}{B_1}.
\]
For every \(1\leq B_1\ll N\), the interval
\(|A_1/B_1-\theta|\leq\eta\) contains
\(O(\eta B_1+1)=O(\eta N+1)\) integers \(A_1\).  Summing over \(B_1\),
then inserting at most \(\tau(A_1)\tau(B_1)\) factorizations, gives
\[
 \#\{(g,k,g',k'):|R-\theta|\leq\eta\}
 \ll_\varepsilon X^\varepsilon(\eta N^2+N).                 \tag{7.2}
\]
This needs \(\eta\geq0\), positive nonzero denominators,
\(g,g'\ll G,\ k,k'\ll K\), and polynomial-in-\(X\) sizes for the divisor
bound.  It remains valid, but possibly very wasteful, when the interval
center lies outside the product boxes.

The exact normalization connecting (7.2) to the determinant is
\[
 \Delta
 =\frac{g}{k\,b_s^{3/2}}\left(R-\theta\right),\qquad
 |R-\theta|=|\Delta|\,\frac{k\,b_s^{3/2}}{g}.                \tag{7.3}
\]
Thus a fixed determinant band \(|\Delta|\leq\lambda\) gives a
\((g,k)\)-dependent rational window.  Only after dyadic localization
\(g\asymp G,\ k\asymp K,\ b_s\asymp A\) may one substitute
\(\eta\asymp\lambda(K/G)A^{3/2}\) in (7.2).  The comparison
\(b_s\asymp A\) itself needs \(b\asymp A\) and
\(|s|\ll A\).  None of these scale identifications was literal in the blind
packet.  Finally, (7.2) is again raw: applying it to
\({\cal C}_{\rm near}\) still requires the coefficient weights, lift
multiplicities, and support residual.

**Claim (iii): not auditable, hence unproved at this seam.**  The supplied
claim is
\[
 |\Psi'''|\asymp \frac{JL|s|}{D_{\rm ray}A^3}
 \quad(\Delta=0,\ s\ne0).                                  \tag{7.4}
\]
Neither \(\Psi\), its differentiation variable, nor the “stated dyadic
scales” occur in the allowed statement packet.  A change from a physical
variable to a unit or \(L\)-scaled variable changes a third derivative by
the cube of the rescaling, so even the power of \(L\) in (7.4) cannot be
checked without that normalization.  A two-sided estimate also needs the
literal phase formula, \(b,b_s\asymp A\) (normally requiring
\(0<|s|\lesssim D_{\rm ray}\ll A\)), the exact \(g/k\) dyadic relation that
produces \(D_{\rm ray}^{-1}\), the interval on which differentiation occurs,
and proof that no other phase term cancels the asserted main third
derivative.  The algebraic equality \(\Delta=0\) alone supplies none of
these.  Accordingly (7.4) must remain a claimant-side hypothesis until its
phase and scale normalization are provided; it cannot alter the retain/no
promotion recommendation of this blind report.
