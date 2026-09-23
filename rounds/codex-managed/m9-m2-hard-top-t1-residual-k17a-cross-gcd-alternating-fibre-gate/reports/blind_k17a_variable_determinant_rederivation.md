# Blind K17a variable-determinant rederivation

## 1. Result

There is an exact multiplicity-one determinant-fibre parametrization.  Put

\[
 g=(d,d'),\qquad d_{\rm lo}=ga,\qquad
 d_{\rm hi}=g(a+2k),\qquad
 m_{\rm lo}=n,\qquad m_{\rm hi}=n+2w .
\]

Then (g,a) are odd, \(k,w\geq1\), ((a,k)=1), and the two opposing
orientations are distinguished by the sign of

\[
 K=kn-aw.
\]

The shift and the character product are exactly

\[
 r=2g|K|,\qquad
 \chi _4(d')\chi _4(d)=(-1)^k.
\]

For fixed ((g,a,n,K)), let (h=(a,n)), (a_0=a/h), and
(n_0=n/h).  When \(h\mid K\), all solutions of (nk-aw=K) have the
unique form

\[
 k=k_0+a_0t,\qquad w=w_0+n_0t,\qquad t\in\mathbb Z,
\]

for a canonical pair ((k_0,w_0)).  Since (a_0) is odd, the exact
character law on this fibre is

\[
 (-1)^k=(-1)^{k_0}(-1)^t.
\]

Both endpoint products translate by the same step

\[
 T={2gan\over h}:\qquad P_t=P_0+Tt,\quad Q_t=Q_0+Tt,\quad
 Q_t-P_t=2gK.
\]

Thus the desired sum is exactly a joint sum, over all signed determinants
(K), of alternating common-translation fibres.  This is the strongest
forced oscillation visible from the statement-only packet.

It does **not**, by itself, prove (176.B1), nor an owner-complete literal
sector.  The narrow exact obstruction is twofold:

1. the retained two-endpoint multiplier has no stated variation or Fourier
   control along (t), so it can destroy the alternating gain at the level
   of every argument that uses it only through boundedness; and
2. keeping (K) joint does not create a second forced alternation, because
   the canonical base sign ((-1)^{k_0(K)}) can be constant on a long
   consecutive determinant interval.

This is a no-go for an **alternation-only or rowwise-transform proof**, not a
counterexample to the literal aggregate with its actual coefficients.

## 2. Exact statement and hypotheses

Assume exactly the statement-only packet: \(J=\sqrt X\),
\(1\ll L\ll H\leq J^{1/2}\), \(R_0=\lceil L\rceil\),
\(0<\gamma<1\), and

\[
 R_{\log}=\min\{R_0-1,\lfloor(\log X)^{100}\rfloor\}.
\]

At both endpoints use the stated zero-extended coefficient
\(\lambda_N(d)\), including the normalized half-open product shell,
squarefree row, row-dependent neither/both or no-pair selector, both parity
branches, smooth profiles, hard point values, and endpoint conventions.
No regularity beyond the stated boundedness is imposed on the arithmetic
selector.

For \(g,a,n\geq1\) with (g,a) odd, set (h=(a,n)).  For every nonzero
(K) satisfying

\[
 h\mid K,\qquad R_{\log}<2g|K|<R_0,\qquad g<\gamma L,
\]

write (a=ha_0), (n=hn_0), (K=hK_0).  Choose the unique
\(k_0\in\{0,1,\ldots,a_0-1\}\) such that

\[
 n_0k_0\equiv K_0\pmod {a_0},
\]

and put (w_0=(n_0k_0-K_0)/a_0).  Define

\[
 k_t=k_0+a_0t,\qquad w_t=w_0+n_0t,
\]
\[
 P_t=ga(n+2w_t),\qquad Q_t=g(a+2k_t)n,\qquad
 T={2gan\over h}.
\]

Only terms with \(k_t,w_t\geq1\) and ((a,k_t)=1) are admitted.  All other
original support conditions are retained by the following exact
zero-extended endpoint multiplier:

\[
 \Lambda^+_{g,a,n,K}(t)=
 \lambda_{Q_t}\!\left(g(a+2k_t)\right)
 \overline{\lambda_{P_t}(ga)}\qquad(K>0),
\]
\[
 \Lambda^-_{g,a,n,K}(t)=
 \lambda_{P_t}(ga)
 \overline{\lambda_{Q_t}\!\left(g(a+2k_t)\right)}\qquad(K<0).
\]

Here each expression is declared zero unless both endpoint data are valid
under every convention in the packet.  In particular, this declaration
retains the squarefree conditions, selectors, smooth factors, hard values,
both half-open endpoints, and zero extension rather than replacing any of
them by a majorant.

Let

\[
 M_t=\begin{cases}P_t,&K>0,\\ Q_t,&K<0,\end{cases}
 \qquad r_{g,K}=2g|K|,
\]

and let \(\Lambda^{\operatorname{sgn}K}\) mean the corresponding expression
above.  Then the complete left side of (176.B1), with the real part still
outside every incidence and determinant sum, is exactly

\[
 \boxed{
 \Re\!\sum_{\substack{g,a,n\geq1\; ;\;g,a\ {\rm odd}\\g<\gamma L}}
 \ \sum_{\substack{K\in\mathbb Z\setminus\{0\}\\(a,n)\mid K\\
 R_{\log}<2g|K|<R_0}}
 \left(1-{2g|K|\over R_0}\right)(-1)^{k_0}
 \sum_{t\in\mathbb Z}(-1)^t
 \Lambda^{\operatorname{sgn}K}_{g,a,n,K}(t)
 e\!\left(J\bigl(\sqrt{M_t+2g|K|}-\sqrt{M_t}\bigr)\right). }
 \tag{F}
\]

Formula (F) is an identity, not an estimate.  It keeps the two orientations,
all non-polylogarithmic determinants, the original divisor-gcd cutoff, the
Fejer factor, the square-root phase, every support value, and the outer real
part.

The exact conclusion derivable from the packet is the parametrization and
character law in (F), together with the alternation-only obstruction stated
in Section 1.  No assertion that (176.B1) is false is made.

## 3. Proof or derivation

Take a nonzero summand of (176.B1).  Both (d) and (d') are odd.  Since
(r=d'm'-dm) is even, \(m\equiv m'\pmod2\).  The cross condition says that
the larger of (d,d') is paired with the smaller of (m,m').  Consequently
there are unique positive integers

\[
 g=(d,d'),\quad a={\min(d,d')\over g},\quad
 k={|d'-d|\over2g},\quad n=\min(m,m'),\quad
 w={|m'-m|\over2}.
\]

The integers (g,a) are odd.  Moreover

\[
 1=\gcd\!\left({d\over g},{d'\over g}\right)
   =\gcd(a,a+2k)=\gcd(a,k),
\]

where the last equality uses that (a) is odd.  The two unordered endpoint
products are therefore

\[
 P=ga(n+2w),\qquad Q=g(a+2k)n,
\]

and direct subtraction gives

\[
 Q-P=2g(kn-aw)=2gK.
\]

If (K>0), then ((dm,d'm')=(P,Q)), so (d'>d) and (m'<m).  If
(K<0), then ((dm,d'm')=(Q,P)), so (d'<d) and (m'>m).  Hence both
opposing orientations are present and (r=2g|K|).  Also
((d,d')=g), so the original cutoff is precisely \(g<\gamma L\).

The character product is independent of the orientation.  Since (g,a)
are odd,

\[
 \begin{aligned}
 \chi_4(d')\chi_4(d)
 &=\chi_4(ga)\chi_4(g(a+2k))\\
 &=\chi_4(a)\chi_4(a+2k)=(-1)^k.
 \end{aligned}
\]

The last identity follows by checking \(2k\pmod4\): adding (2k) to an
odd integer preserves its \(\chi_4\)-value for even (k) and reverses it
for odd (k).

Now fix (g,a,n,K).  The equation (nk-aw=K) has a solution exactly when
(h=(a,n)) divides (K).  After division by (h), it is

\[
 n_0k-a_0w=K_0,\qquad (a_0,n_0)=1.
\]

The displayed congruence defining (k_0) gives one solution
((k_0,w_0)), and the standard subtraction of two solutions gives all and
only the solutions

\[
 k=k_0+a_0t,\qquad w=w_0+n_0t,\qquad t\in\mathbb Z.
\]

Because (a), hence (h) and (a_0), is odd,

\[
 (-1)^{k_t}=(-1)^{k_0+a_0t}=(-1)^{k_0}(-1)^t.
\]

Furthermore

\[
 \begin{aligned}
 P_t&=ga(n+2w_0)+2ga n_0t=P_0+{2gan\over h}t,\\
 Q_t&=g(a+2k_0)n+2ga_0nt=Q_0+{2gan\over h}t,
 \end{aligned}
\]

so the endpoints undergo a common translation and retain the fixed
difference (Q_t-P_t=2gK).

Conversely, every tuple in (F) with \(k_t,w_t\geq1\), ((a,k_t)=1), and
nonzero endpoint multipliers reconstructs exactly one original ordered pair:

\[
 (d,m;d',m')=
 \begin{cases}
 (ga,n+2w_t;\ g(a+2k_t),n),&K>0,\\
 (g(a+2k_t),n;\ ga,n+2w_t),&K<0.
 \end{cases}
\]

The canonical range for (k_0) makes (t) unique.  This proves both
surjectivity and injectivity, hence multiplicity one.  Substituting the
character identity, the correctly oriented endpoint coefficients, the
phase

\[
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right),
\]

and (r=2g|K|) gives (F).  Nothing has been smoothed, completed, or placed
inside an absolute value.

The obstruction also has an exact algebraic part.  Across determinants the
canonical residue is

\[
 k_0(K)\equiv n_0^{-1}K_0\pmod {a_0},\qquad 0\leq k_0<a_0.
\]

Its parity need not alternate with (K).  For example, take (h=1), an
odd prime (a), and (n=(a+1)/2).  For every
\(1\leq K\leq(a-1)/2\), the canonical solution is

\[
 k_0=2K,\qquad w_0=K,\qquad nk_0-aw_0=K.
\]

Thus ((a,k_0)=1) and ((-1)^{k_0}=+1) throughout this whole consecutive
positive-determinant interval.  The negative orientation has the mirror
example (n=(a-1)/2), \(K=-\kappa\), \(k_0=2\kappa\), \(w_0=\kappa\).
Therefore retaining all (K) before every modulus does not, on its own,
supply determinant-wise character cancellation.

Finally, on one fixed fibre write the complete post-character factor as

\[
 B(t)=\Lambda^{\operatorname{sgn}K}_{g,a,n,K}(t)
 e\!\left(J(\sqrt{M_t+2g|K|}-\sqrt{M_t})\right).
\]

Any estimate based only on \(|B(t)|\ll1\) would have to bound
\(\sum_t(-1)^tB(t)\) uniformly.  This is impossible: on an arbitrary-array
control set (B(t)=(-1)^t) on the admitted points, the sum equals their
cardinality.  Equivalently, one may absorb both the character and the
square-root phase into a bounded dechirped endpoint array.  This proves the
claimed no-go for a coefficient-blind alternating-fibre estimate.  It does
not assert that the packet's literal selector actually realizes that
control.

## 4. First doubtful or unproved step

There is no doubtful step in the bijection, the orientation rule, the
common-translation formula, or the character identity.  The first unproved
step is the genuinely analytic estimate obtained by placing the actual
retained multiplier into (F):

\[
 \Re\sum_{g,a,n}\sum_K
 \left(1-{2g|K|\over R_0}\right)(-1)^{k_0(K)}
 \sum_t(-1)^t B_{g,a,n,K}(t)
 \ \ll_{\gamma,\varepsilon}\ L^2X^\varepsilon,
 \tag{JF}
\]

with all conditions and zero extensions exactly as in (F), and without
taking absolute values fibrewise, determinant-wise, or modulus-wise.

To prove (JF) by this route one needs a new structural input about the
*actual two-endpoint selector-weighted coefficients*: for example, a joint
parity anti-correlation or a Fourier/variation estimate along the common
translations (P_t,Q_t), uniform after the squarefree conditions and both
selector branches are imposed.  None is supplied in the statement-only
packet.  Boundedness of \(\lambda\), smoothness of only some profiles, and
the exact \(\chi_4\) identity do not imply it.

The short-fibre seam is part of the same first open step.  A fibre with one
admissible (t) receives no saving from ((-1)^t); the packet gives no
owner-complete estimate showing that the total mass of such fibres is
\(O(L^2X^\varepsilon)\).  Since the stated coefficient-independent capacity
is \(L^3X^\varepsilon\), an (L)-saving cannot be inferred merely by
assigning an (O(1)) bound to each fibre.

## 5. Required control tests and outcomes

1. **Both orientations and parity branches — pass.**  (K>0) is exactly
   (d'>d,m'<m), and (K<0) is exactly (d'<d,m'>m).  Since (r) is even
   and (d,d') are odd, (m,m') have the same parity and their gap is
   (2w).  The parity of (n) is fixed on a fibre, so the two original
   parity branches remain disjoint.  Because (a_0) is odd in either
   branch, the law ((-1)^{k_t}=(-1)^{k_0+t}) is unchanged.

2. **Multiplicity and original gcd cutoff — pass.**  The forward map uses
   minima, the exact gcd, and positive half-gaps, so it is unique.  The
   canonical residue \(0\leq k_0<a_0\) makes (t) unique in the reverse
   map.  The condition ((a,k_t)=1) is retained, and then
   ((d,d')=g), not merely a divisor of (g).  Hence the cutoff is exactly
   \(g<\gamma L\).

3. **Constant-amplitude fibres — partial pass, insufficient.**  If the
   complete factor (B(t)) is constant on a consecutive (t)-interval,
   then the alternating sum has modulus at most (1).  Even with the exact
   coprimality filter one has

   \[
   \left|\sum_{t\in I\, :\, (a,k_t)=1}(-1)^t\right|\leq \tau(a),
   \]

   by Möbius inversion: every soluble congruence \(e\mid k_t\), \(e\mid a\),
   is a progression of odd step, on which parity alternates.  This verifies
   the character mechanism in its best model case.  It does not apply to
   the true square-root phase and opaque selector multiplier.

4. **Short fibres — fail for the proposed saving.**  On a singleton the
   character supplies no cancellation.  More generally, the endpoint shell
   and zero extension may leave an odd or bounded number of points.  There
   is no stated counting lemma making the aggregate of these fibres
   target-safe.

5. **Squarefree Möbius progressions — parity survives, absolute modulus
   summation fails.**  Along a fibre the varying cofactors are the linear
   forms

   \[
   n+2w_t=(n+2w_0)+2n_0t,\qquad
   a+2k_t=(a+2k_0)+2a_0t.
   \]

   Expanding a squarefree indicator by
   \(\mu^2(q)=\sum_{s^2\mid q}\mu(s)\) puts (t) into progressions of odd
   modulus for the odd factors (the even behavior is already fixed by the
   parity branch).  Parity still alternates on each such progression.  But
   summing the resulting square-divisor moduli absolutely costs the number
   of moduli—up to a square-root-scale cost for one varying cofactor and a
   product cost for two—and can restore the desired power.  Cancellation
   between Möbius moduli in the presence of both selectors is not supplied.

6. **Selected and no-pair rows / arithmetic-selector discontinuity —
   fail as a boundedness-only input.**  Both selector types remain inside
   \(\Lambda^\pm(t)\).  No complementarity, periodicity, or bounded variation
   across (t) is stated.  The diagnostic selector
   \(1_{t\equiv k_0\pmod2}\) keeps only one character sign and changes a
   length-(T_f) alternating fibre into a contribution of order (T_f).
   This does not claim that the literal selector equals this diagnostic
   array; it shows that a proof treating it as an arbitrary bounded support
   is invalid.

7. **Arbitrary-support and dechirped arrays — fail, exactly.**  On any
   chosen fibre, support on one parity removes the alternation.  More
   strongly, choosing the edge multiplier

   \[
   \Lambda(t)=(-1)^{k_0+t}
   e\!\left(-J(\sqrt{M_t+2g|K|}-\sqrt{M_t})\right)
   \]

   makes every complete summand positive after the extracted character and
   phase are restored.  This is a false control for coefficient-independent
   reasoning, not a lower bound for the literal aggregate.

8. **Rowwise summation by parts — restored-power failure.**  For a
   consecutive block (I), Abel summation gives only

   \[
   \left|\sum_{t\in I}(-1)^tB(t)\right|
   \ll \|B\|_\infty+\sum_{t,t+1\in I}|B(t+1)-B(t)|.
   \]

   The selector can make the variation comparable to (|I|).  Even for a
   constant coefficient, the genuine chirp has no stated small-variation
   bound.  With (M_t=M_0+Tt), (r=2g|K|), its continuous derivative is

   \[
   -{JTr\over
   2\sqrt{M_t}\sqrt{M_t+r}(\sqrt{M_t}+\sqrt{M_t+r})},
   \]

   and the hypotheses give no separation of this quantity from
   half-integer resonances.  Thus rowwise partial summation can return the
   full fibre length.

9. **Rowwise Poisson or van der Corput followed by absolute dual-mode
   summation — restored-power failure.**  Formally, for a smooth cutoff
   (W), Poisson rewrites

   \[
   \sum_t W(t)e(\Psi(t)+t/2)
   =\sum_{\ell\in\mathbb Z}\int W(x)
     e(\Psi(x)+(1/2-\ell)x)\,dx.
   \]

   Stationary modes satisfy \(\Psi'(x)+1/2=\ell\).  There is no hypothesis
   excluding such modes, and absolute summation over all modes meeting the
   derivative range discards the only possible cross-mode cancellation.
   The dechirped control above is decisive: its physical-space sum is the
   fibre length, so an exact transform followed by absolute values must
   restore that mass somewhere.  Van der Corput has the same obstruction
   once its row bounds are summed absolutely.

10. **Canonical parametrization jumps and joint determinants — fail for a
    second automatic alternation.**  The exact examples
    (n=(a+1)/2, K>0) and (n=(a-1)/2, K<0) from Section 3 have
    (k_0=2|K|) on a long consecutive determinant interval, hence constant
    base character sign.  The jump law is multiplication by
    \(n_0^{-1}\pmod{a_0}\), followed by canonical wraparound; it is not
    adjacency in (k).  Therefore summing all non-polylogarithmic (K)
    before any congruence split is necessary but not sufficient.

11. **Endpoints, hard values, and zero extension — pass as bookkeeping,
    adverse for cancellation.**  They are retained exactly in
    \(\Lambda^\pm\), with (t) summed over all integers and invalid points
    set to zero.  This prevents double counting at half-open boundaries.
    It also makes clear that endpoint truncations and hard isolated values
    may turn a long algebraic fibre into several short support pieces; no
    cancellation across the deleted points is legitimate.

## 6. Dependencies and exact artifacts used

This report used only:

- `protocol.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/blind_statement.md`; and
- the assigned brief only for the output path and seven-part report
  contract.

No proof graph, active campaign, strategy or barrier file, prior round,
source card, sibling report, conductor analysis, validation artifact, or
proposed state effect was read or used.  No external theorem or numerical
experiment is used.  The derivation is elementary integer algebra; the
controls are diagnostic and do not certify an asymptotic lower bound.

## 7. Recommended scoped state effect

**Retain** the multiplicity-one parametrization (F), the exact alternating
law ((-1)^{k_0+t}), the common-translation step (2gan/(a,n)), and the
canonical-jump examples as candidate evidence.

**Do not promote** (176.B1), and do not promote a strict literal sector from
this report.  **Reject** the narrower claim that exact \(\chi_4\) alternation,
even with all determinants kept joint before every modulus, yields the
required (L)-saving by rowwise Abel, Poisson, van der Corput, or
coefficient-independent fibre bounds.

The next admissible mathematical input would have to be an owner-complete,
selector-sensitive joint estimate for (JF), or a proved structural law for
the actual neither/both and no-pair selectors that rules out parity support,
dechirping, excessive variation, and a target-sized population of short
fibres.  Until such an input exists, the scoped state effect should be
**revise/retain the obstruction, with no target promotion**.
