## 1. Result

The normalization in (72.6)--(72.8) is algebraically correct.  More precisely,
(72.8) implies (72.6) by Cauchy in the \(b\)-variable with
\(B\asymp C/T\), and multiplication by the outer coefficient in (72.5)
then gives \(J^{1/2}X^\varepsilon\).  The diagonal is of the asserted size
\(BC=C^2/T\leq J^2/T\) provided the intended stationary symbol has the
unstated \(L^2\)-normalization

\[
 \sum_{b\asymp B}\sum_{\substack{c\asymp C\\(c,4b)=1}}
 |a_{b,c,k}|^2\ll BCX^\varepsilon.                 \tag{R72.1}
\]

The packet does not contain enough quantitative information to prove
(72.8).  Literally, (R72.1) is the first missing symbol inequality.  If the
sentence following (72.4) and the asserted diagonal evaluation (72.9) are
taken as granting (R72.1), the first missing analytic inequality is a joint
short reciprocal-sum estimate for the off-diagonal after the exact
reciprocity rewrite below.  This is a strictly more specific survivor than
the already forbidden one-variable Poisson/B-process loop: its problematic
part consists of nonexact, near-resonant pairs in a simultaneous
\((b,c_1,c_2)\) sum with the moving actual symbol.

No counterexample to (72.8) follows from the diagonal, from \(b=O(1)\), or
from exact-square/fourth-power configurations.  Under the standard bounded
symbol normalization, exact arithmetic phase collisions in the integral
square cases have only divisor multiplicity and are diagonal-scale.  The
near-diagonal can, however, be resonant at the top conductor, and the packet
supplies no estimate that controls the remaining inverse phase there.  Thus
the outcome is underdetermination, not a disproof.  The even local classes,
the surviving axes, retained transition faces, and error tails cannot be
closed from the one odd nonaxial formula supplied here.

## 2. Exact statement and hypotheses

Let \(X>1\), \(J=X^{1/2}\), \(T=J^{3/5}=X^{3/10}\),
\(J^{2/3}<C\leq J\), and \(B=C/T\).  Fix the positive compatible odd
nonaxial branch \(k>0\), use only integers \(b\asymp B\) and
\(c\asymp C\) with \((c,4b)=1\), and define \(S_{b,k}(C)\) and
\(\mathcal E_{C,k}\) exactly as in (72.4) and (72.7).  Write
\(e(z)=\exp(2\pi i z)\), \(e_q(z)=e(z/q)\), and let
\(\overline{4b}^{(c)}\) denote the inverse of \(4b\pmod c\).

The unconditional statement derivable from the packet is

\[
 \mathcal E_{C,k}\ll J^2T^{-1}X^\varepsilon
 \quad\Longrightarrow\quad
 \left|\sum_{b\asymp B}S_{b,k}(C)\right|
 \ll J\sqrt C\,T^{-1}X^\varepsilon.               \tag{R72.2}
\]

The diagonal conclusion additionally requires (R72.1), unless the claim
"the diagonal has size \(BC\)" in (72.9) is itself treated as a frozen
input.  Any integration by parts, completion, or large-sieve proof further
requires quantitative seminorm/support bounds for the actual symbol, for
example a finite collection of normalized \((b,c)\) derivative or variation
bounds; no such bounds are stated in the packet.

For the exact perfect-power audit only, suppose additionally that
\(X=n^2\) and \(k=m^2\) with positive integers \(n,m\).  To turn divisor
counts into \(X^\varepsilon\), one also needs \(m\), hence
\(2bn+m\), to be at most a fixed power of \(X\), and one needs bounded
symbol values.  These quantitative hypotheses are not supplied; they are
made explicit here rather than silently attributed to the actual symbol.

No statement about the opposite orientation, either even local class,
either surviving axis, or a transition/error piece is included in this
proposition: their exact rows and symbol bounds are absent, and (72.2)--
(72.4) expressly forbid deriving them by a sign change.

## 3. Proof or derivation

There are \(O(B)\) values of \(b\asymp B\).  Hence Cauchy's inequality gives

\[
 \left|\sum_{b\asymp B}S_{b,k}(C)\right|^2
 \ll B\mathcal E_{C,k}.
\]

Substitution of (72.8) and \(B=C/T\) gives

\[
 (B\mathcal E_{C,k})^{1/2}
 \ll \left(\frac CT\frac{J^2}{T}\right)^{1/2}X^\varepsilon
 =\frac{J\sqrt C}{T}X^\varepsilon,
\]

which is exactly (72.6).  Multiplying this by (72.5) gives

\[
 \frac{T}{\sqrt{CJ}}\frac{J\sqrt C}{T}=J^{1/2}.
\]

Thus every factor of \(B,C,J,T\) in the stated implication checks.  This
only verifies the packet's declaration of sufficiency relative to a
\(J^{1/2}X^\varepsilon\) post-coefficient budget; that terminal budget is
not otherwise stated in the isolated packet.  Cauchy does not give a
converse, so (72.8) is sufficient rather than necessary for (72.6).

On expanding the square, the diagonal is

\[
 D=\sum_{b\asymp B}\sum_{\substack{c\asymp C\\(c,4b)=1}}
 |a_{b,c,k}|^2.
\]

Under (R72.1),

\[
 D\ll BCX^\varepsilon=\frac{C^2}{T}X^\varepsilon
 \leq\frac{J^2}{T}X^\varepsilon.
\]

It is exactly target-scale at \(C=J\).  With only pointwise bounded weights,
the fully trivial estimate is instead

\[
 \mathcal E_{C,k}\ll BC^2X^\varepsilon
 =\frac{C^3}{T}X^\varepsilon,
\]

which reaches \(J^2/T\) precisely at \(C=J^{2/3}\).  This independently
explains why the strict upper range needs a new cancellation input.

The arithmetic and real phases admit the following exact reciprocity
normalization.  For \((c,4b)=1\),

\[
 \frac{\bar c}{4b}+\frac{\overline{4b}^{(c)}}c
 \equiv \frac1{4bc}\pmod 1.
\]

Since
\(A_b=bX+\sqrt{kX}+k/(4b)\), it follows that

\[
 e_{4b}(k\bar c)e(-A_b/c)
 =e_c\!\left(-k\overline{4b}^{(c)}\right)
  e\!\left(-\frac{bX+\sqrt{kX}}c\right).          \tag{R72.3}
\]

Consequently, with
\(\delta(c_1,c_2)=c_1^{-1}-c_2^{-1}\), the exact off-diagonal survivor is

\[
 \begin{split}
 O={}&\sum_{b\asymp B}
 \sum_{\substack{c_1,c_2\asymp C\\c_1\ne c_2\\(c_1c_2,4b)=1}}
 a_{b,c_1,k}\overline{a_{b,c_2,k}}
 e\!\left(-(bX+\sqrt{kX})\delta(c_1,c_2)\right)\\
 &\qquad\times
 e\!\left[-k\left(
 \frac{\overline{4b}^{(c_1)}}{c_1}
 -\frac{\overline{4b}^{(c_2)}}{c_2}
 \right)\right].                                  \tag{R72.4}
 \end{split}
\]

For \(c_2=c_1+h\),
\(\delta=h/(c_1c_2)\).  The linear real frequency in the \(b\)-variable is
\(Xh/(c_1c_2)\), so the natural derivative-resonance window is

\[
 \left\|\frac{Xh}{c_1c_2}\right\|\lesssim B^{-1}. \tag{R72.5}
\]

At \(C=J=\sqrt X\), this frequency is of order \(h\), and pairs with
\(c_1c_2\) close to \(X\) can lie in (R72.5).  The constant term
\(\sqrt{kX}\delta\) does not remove a \(b\)-resonance.  Nor may the final
inverse factor in (R72.4) be dropped: it can cancel, reinforce, or rearrange
the real oscillation.  The qualitative phrase "actual symbol" supplies no
bound for this joint short sum.  In the unrecriprocated real phase,

\[
 A_b'=X-\frac{k}{4b^2},
\]

so a smooth \(b\)-stationary point occurs at
\(b=\sqrt{k}/(2\sqrt X)\).  It is outside the present range if \(k\) is
fixed, but the packet gives no quantitative size relation between \(k\)
and \(X\), so uniform exclusion cannot be asserted from the word "finite."

In the integral square case \(X=n^2,\ k=m^2\), (R72.3) simplifies further.
Indeed

\[
 4b\bigl(bn^2+mn+m^2\overline{4b}^{(c)}\bigr)
 \equiv(2bn+m)^2\pmod c,
\]

and hence the complete row phase is exactly

\[
 e_c\!\left(-\overline{4b}^{(c)}(2bn+m)^2\right). \tag{R72.6}
\]

Put \(N_b=2bn+m\).  The phase in (R72.6) is \(1\) only when
\(c\mid N_b^2\).  More generally, after reducing its rational argument,
its denominator is \(c/(c,N_b^2)\).  If two moduli \(c_1,c_2\) give the
same exact phase, their reduced denominators agree.  For a fixed reduced
denominator \(d\), every possible modulus has the form \(c=dg\) with
\(g\mid N_b^2\).  Thus every exact phase value has multiplicity at most
\(\tau(N_b^2)\), and the number of ordered exact-collision pairs for a
fixed \(b\) is \(O(C\tau(N_b^2))\).  Under polynomial size and bounded
weights this contributes \(O(BCX^\varepsilon)\), which is diagonal-scale
and therefore target-safe.  If \(N_b=r^2\), the numerator is the fourth
power \(r^4\); if \(X\) or \(k\) is itself a fourth power, the corresponding
root is a square.  Neither specialization changes the reduced-denominator
argument or its divisor multiplicity.  The fact that \(A_b\) is a real
square by definition is not, by itself, an arithmetic resonance.

Finally,

\[
 B=\frac CT>\frac{J^{2/3}}{J^{3/5}}=J^{1/15}=X^{1/30}.
\]

Therefore \(b\asymp B\) contains no \(b=O(1)\) regime asymptotically.  A
small-\(b\) issue can only enter through a transition or error tail not
described by (72.4), so it cannot contradict the displayed main row and
cannot be declared controlled for the full contribution.

## 4. First doubtful or unproved step

The first literal gap is (R72.1).  The packet names the factors inside
\(a_{b,c,k}\) and says they have fixed smoothness away from retained faces,
but it gives neither a formula nor a pointwise, \(L^2\), derivative,
variation, support-overlap, or transition bound.  Consequently even the
displayed evaluation of the diagonal cannot be rederived from the stated
symbol class alone.  Scaling and concentration are logically excluded only
by information that is intended but not present; it would be invalid to
invent that information.

If (72.9) is accepted as granting the needed normalization, the first
analytic gap is the following actual-symbol joint inequality:

\[
 \left|O\right|\ll_\varepsilon \frac{J^2}{T}X^\varepsilon, \tag{R72.7}
\]

with \(O\) exactly as in (R72.4), uniformly for
\(J^{2/3}<C\leq J\), including (R72.5), the moving Farey-neighbor and
Fresnel factors, and all permitted \(k\).  Equivalently, one may prove the
corresponding bound for the full energy after (R72.1).  A useful theorem
must retain simultaneously the real linear reciprocal twist and the
\(\overline{4b}^{(c)}\) twist; estimating either as arbitrary coefficients
or taking absolute values before their joint cancellation is precisely the
missing step.  No phase-specific spectral or reciprocal-square large-sieve
theorem, and no verification of such a theorem's hypotheses, is present.

This is underdetermination rather than a counterexample.  The packet fixes
one actual symbol in words, so an arbitrary adversarial coefficient choice
would not be a counterexample to that symbol.  Conversely, the words do not
give enough quantitative data to prove (R72.7) for it.

## 5. Required control test and outcome

| Control | Test performed | Outcome from the isolated packet |
|---|---|---|
| Normalization | Substitute \(B=C/T\) into Cauchy and multiply by \(T/\sqrt{CJ}\). | Pass: (72.8) gives (72.6), then \(J^{1/2}X^\varepsilon\).  The isolated packet does not separately state the terminal \(J^{1/2}\) budget. |
| Diagonal | Expand \(\mathcal E\) at \(c_1=c_2\). | \(D\leq BCX^\varepsilon\leq J^2/T\) conditional on (R72.1); (R72.1) is not stated quantitatively. |
| Trivial boundary | Use \(\lvert S_b\rvert\leq CX^\varepsilon\). | Gives \(C^3/T\), exactly reaching the target at \(C=J^{2/3}\) and not closing the strict upper range. |
| Near diagonal | Put \(c_2=c_1+h\) and inspect the \(b\)-frequency. | Unresolved: the window (R72.5) survives, especially near \(C=J\), and the inverse phase cannot be discarded. |
| Exact resonances | In the integral-square case reduce (R72.6) to lowest terms. | No forced contradiction: exact phase collisions have divisor multiplicity and are \(BCX^\varepsilon\)-scale under the explicitly stated boundedness conditions. |
| Squares and fourth powers | Test \(X=n^2,\ k=m^2\), \(N_b=r^2\), and fourth-power roots. | No new large family: all are covered by divisors of \(N_b^2\) (or \(r^4\)); quantitative uniformity still needs a size bound for \(k\). |
| Smooth derivative resonance | Solve \(A_b'=0\). | The point is \(\sqrt{k}/(2\sqrt X)\); excluded for fixed \(k\), not uniformly excluded without a \(k\)-size hypothesis. |
| \(b=O(1)\) and \(b\asymp B\) | Compute the smallest \(B\) in (72.1). | The displayed dyadic row has \(B>X^{1/30}\), so no small-\(b\) main regime.  Unspecified tails remain unaudited. |
| Farey-neighbor and transition faces | Look for support widths, overlap counts, and variation/seminorm bounds. | Not supplied; neither (R72.1) nor partial summation across the faces can be checked. |
| Odd gcd factors | Check the hypothesis used in reciprocity. | Controlled only for the displayed row by \((c,4b)=1\); (R72.3) is exact there. |
| Two even local classes and their gcd factors | Look for their exact phases, units, and coprimality conditions. | Not supplied, and the packet forbids sign-change inference; unresolved. |
| Both surviving axes | Look for an axial row and outer coefficient. | Not supplied; unresolved.  Setting \(k=0\) in the nonaxial row would be an unauthorized substitution. |
| Finite \(k\)-sum | Check cardinality, \(k\)-size, and uniform symbol constants. | Only qualitative finiteness is stated.  An \(O(1)\) cardinality and uniform (R72.7) would suffice, but are not documented. |
| Transition/error tails | Look for exact ranges and estimates. | Not supplied; unresolved. |
| Candidate theorem seams | Check real twist, inverse twist, level four, moving symbol, zero indices, and required power. | No theorem is cited, so none of these hypotheses can be audited. |
| Scope and global gap | Compare the conclusion with the frozen scope. | Even a proof of (72.8) would close only this fixed-smooth-interior upper-conductor representation.  It would not cover cone edges, the missing even/axial antecedents, the original wavelet's global \(X^{1/20}\) gap, \(M9\!-\!M1\), \(M9\), or the Gauss-circle exponent. |

## 6. Dependencies and exact artifacts/sources used

Isolation ledger: exactly two artifacts were read:

1. `rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/briefs/blind_upper_conductor_rederivation.md`.
2. `rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/derivation_packet.md`.

No state file, proof graph, active campaign file, prior or sibling report,
legacy report, proof draft, validation matrix, source card, repository file
outside those two artifacts, web page, or web literature was read.  No
external theorem was relied on for the target estimate.  The only general
facts used were Cauchy's inequality, elementary modular reciprocity, and the
standard divisor bound for the explicitly conditional perfect-power
control.  The only file created or edited is
`rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/reports/blind_upper_conductor_clean.md`.

## 7. Recommended state effect

Retain the upper-conductor obligation; do not promote (72.8), (72.6), any
even or axial estimate, or any global \(M9\!-\!M1\) claim.  The Cauchy
normalization, exact reciprocity identity (R72.3), exclusion of \(b=O(1)\)
from the displayed upper-range row, and conditional divisor-multiplicity
control of integral square/fourth-power exact collisions may be retained as
checked algebraic evidence.  Before another proof attempt, revise the input
packet to supply (i) explicit normalized symbol and transition seminorms,
(ii) uniform \(k\)-cardinality and size data, and (iii) either a proved
joint inequality of the form (R72.7) or a phase-specific theorem with every
listed seam verified.  Exact rows and bounds for both even classes and both
axes are separately required before any target-safe full-scope conclusion.
