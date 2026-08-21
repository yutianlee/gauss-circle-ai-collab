# Blind pointwise-bridge rederivation (Round 94)

## 1. Result

All of the deterministic persistence statements are valid with the stated
one-sided orientations, including at an integer jump.  They imply the
one-separated sampling estimate and hence the asserted almost-all integer
exceptional-set estimate.  The buffer \([Y/2,3Y]\) is sufficient for every
favourable local interval when \(x\in[Y,2Y]\) and \(H\le Y/2\).

The proposed local bridge is also valid.  In fact there is a sharper exact
form.  If

\[
 Q(Y,H)\geq
 \sup_{\substack{I\subset[Y/2,3Y]\\ |I|=H}}
 \int_I |P(t)|^2\,dt,
\]

then, for \(M=|P(x)|\),

\[
 {M^2\over4}\min\!\left(H,{M\over2\pi}\right)\leq Q(Y,H).
 \tag{A}
\]

Consequently the advertised, but weaker, additive bridge

\[
 M\ll H+Y^{1/4+\delta/2}+\left({E(Y,H)\over H}\right)^{1/2}
 \tag{B}
\]

holds when \(Q=C_\delta HY^{1/2+\delta}+E\) with \(E\geq0\).  The exact
inverse of (A) also has a cubic branch, recorded below.  For
\(H=Y^{1/4+\sigma}\), the unmodified local scale
\(Q\ll HY^{1/2+o(1)}\) gives
\(M\ll Y^{1/4+\sigma/3+o(1)}\), not the strict quarter exponent when
\(\sigma>0\) is fixed.  It reaches the quarter exponent when
\(H=Y^{1/4+o(1)}\).  At a fixed longer window it would instead be enough to
prove the stronger total bound \(Q\ll Y^{3/4+o(1)}\).

Uniform unit-window \(L^2\) control is equivalent, with the usual
epsilon rescaling, to the real pointwise quarter-exponent problem.  The
accepted global mean square alone does not imply this local supremum.  Its
strongest prescribed-point consequence obtainable from persistence is
\(P(x)\ll_\varepsilon Y^{1/2+\varepsilon}\); this exponent is sharp in the
abstract class having the same monotonicity and inclusive integer-jump
structure.  The separately accepted \(1/3+\varepsilon\) fallback is stronger
but is not a consequence established here from the global moment alone.

## 2. Exact statements and hypotheses

Assume that for every sufficiently large \(T\) and every \(\delta>0\),

\[
 \int_T^{2T}|P(t)|^2\,dt\leq C_\delta T^{3/2+\delta},
 \qquad P(t)=A(t)-\pi t,
\]

where \(A(t)=N(\sqrt t)\) is nondecreasing and takes its post-jump value at
an integer jump.  Fix sufficiently large \(Y\), let \(x\in[Y,2Y]\), and
put \(M=|P(x)|\).  For the local assertions assume \(1\leq H\leq Y/2\);
the packet's range \(H\leq Y^{1/3}\) has this property after changing only
the harmless bounded range of \(Y\).

The exact persistence statements, for every \(u\geq0\) for which the
arguments are nonnegative, are

\[
 P(x)>0\quad\Longrightarrow\quad P(x+u)\geq P(x)-\pi u,
 \tag{P+}
\]

and

\[
 P(x)<0\quad\Longrightarrow\quad P(x-u)\leq P(x)+\pi u.
 \tag{P-}
\]

Thus, if \(P(x)=M>0\), then \(|P(x+u)|\geq M/2\) for
\(0\leq u\leq M/(2\pi)\); if \(P(x)=-M<0\), then
\(|P(x-u)|\geq M/2\) on the analogous left interval.  In particular,
\(M\geq2\pi H\) supplies a favourable adjacent interval of length \(H\).

For every one-separated \(\mathcal X\subset[Y,2Y]\), meaning
\(|x-x'|\geq1\) for distinct points,

\[
 \sum_{x\in\mathcal X}|P(x)|^2
 \ll_\delta Y^{3/2+\delta}.
 \tag{S}
\]

It follows for every \(\eta>0\) that

\[
 \#\{n\in[Y,2Y]\cap\mathbb Z:|P(n)|>Y^{1/4+\eta}\}
 \ll_{\delta,\eta}Y^{1-2\eta+\delta}.
 \tag{E}
\]

For a local upper bound \(Q=Q(Y,H)\), (A) implies the following exact
piecewise inverse (absolute constants only):

\[
 M\leq
 \begin{cases}
  (8\pi Q)^{1/3},&Q<\pi^2H^3,\\[3pt]
  2(Q/H)^{1/2},&Q\geq\pi^2H^3.
 \end{cases}
 \tag{L}
\]

Equivalently for exponent bookkeeping,

\[
 M\ll Q^{1/3}+(Q/H)^{1/2}.
 \tag{L'}
\]

If \(H=Y^{\alpha+o(1)}\), \(E\ll Y^{\beta+o(1)}\), and
\(Q=C_\delta HY^{1/2+\delta}+E\), put

\[
 q=\max\{\alpha+1/2+\delta,\,\beta\}.
\]

The exact exponent delivered by persistence is

\[
 p=\max\left\{{q\over3},{q-\alpha\over2}\right\},
 \qquad M\ll Y^{p+o(1)}.
 \tag{X}
\]

For the unit-window equivalence, set

\[
 U(Y)=\sup_{\substack{I\subset[Y/2,3Y]\\|I|=1}}
       \int_I|P(t)|^2\,dt,
 \qquad
 S(Y)=\sup_{x\in[Y,2Y]}|P(x)|.
\]

Then

\[
 S(Y)\leq2\pi+2U(Y)^{1/2},
 \tag{U1}
\]

while, writing \(S^\sharp(Y)=\sup_{t\in[Y/2,3Y]}|P(t)|\),

\[
 U(Y)\leq S^\sharp(Y)^2.
 \tag{U2}
\]

Hence \(U(Y)\ll_\varepsilon Y^{1/2+\varepsilon}\) for all scales if and
only if \(P(X)\ll_\varepsilon X^{1/4+\varepsilon}\) for all large real
\(X\), after rescaling epsilon and dyadic constants.

## 3. Proof or derivation

**Persistence and jump convention.**  Monotonicity gives

\[
 P(x+u)-P(x)=A(x+u)-A(x)-\pi u\geq-\pi u,
\]

which proves (P+).  Similarly,

\[
 P(x-u)-P(x)=A(x-u)-A(x)+\pi u\leq\pi u,
\]

which proves (P-).  These comparisons use the literal values of \(A\) at
both endpoints, so they remain true when either endpoint is an integer
jump.  At an integer \(x\), \(A(x)\) includes the new lattice points.  A
positive post-jump value therefore persists to the right; a negative
post-jump value compared to the pre-jump values persists to the left.
No continuity or almost-everywhere reinterpretation is being used.

Taking \(u\leq M/(2\pi)\) gives the stated lower bound \(M/2\).  If
\(M\geq2\pi H\), use \([x,x+H]\) for the positive sign and \([x-H,x]\)
for the negative sign.  Since \(x\in[Y,2Y]\) and \(H\leq Y/2\), both
possible intervals lie in \([Y/2,3Y]\), including at \(x=Y\) and
\(x=2Y\).

**One-separated sampling.**  The global moment on three neighbouring
dyadic blocks gives

\[
 B_\delta(Y):=\int_{Y/2}^{4Y}|P(t)|^2\,dt
 \ll_\delta Y^{3/2+\delta}.
 \tag{C}
\]

For each \(x\in\mathcal X\) with \(|P(x)|\geq2\pi\), attach
\(J_x=[x,x+1]\) when \(P(x)>0\) and \(J_x=[x-1,x]\) when
\(P(x)<0\).  Persistence yields

\[
 |P(x)|^2\leq4\int_{J_x}|P(t)|^2\,dt.
\]

The points with \(|P(x)|<2\pi\) contribute at most
\(4\pi^2\#\mathcal X\ll Y\).  If \(t\in J_x\), then
\(x\in[t-1,t+1]\).  A closed interval of length two contains at most
three points of a one-separated set, so the family \(\{J_x\}\) has
overlap at most three (endpoint multiplicities are immaterial to the
integral).  All these intervals lie in \([Y-1,2Y+1]\subset[Y/2,4Y]\)
for large \(Y\).  Therefore

\[
 \sum_{x\in\mathcal X}|P(x)|^2
 \leq4\pi^2\#\mathcal X+12B_\delta(Y)
 \ll_\delta Y^{3/2+\delta},
\]

proving (S).  Apply (S) to the exceptional integers.  Each such term is
larger than \(Y^{1/2+2\eta}\), and division proves (E).  This step is a
count of exceptional integers only and says nothing about a prescribed
integer.

**Local bridge and additive error.**  Let

\[
 \ell=\min\left(H,{M\over2\pi}\right).
\]

On the sign-favourable adjacent segment of length \(\ell\), persistence
gives \(|P(t)|\geq M/2\).  This segment is contained in the corresponding
adjacent \(H\)-interval, so nonnegativity of \(|P|^2\) proves (A).
If \(M\leq2\pi H\), (A) reads \(M^3/(8\pi)\leq Q\).  If
\(M\geq2\pi H\), it reads \(M^2H/4\leq Q\).  If
\(Q<\pi^2H^3\), the latter case is impossible; if
\(Q\geq\pi^2H^3\), the square-root bound also dominates every
\(M<2\pi H\).  This proves (L) and (L').

The simpler dichotomy \(M<2\pi H\), or
\(M\leq2(Q/H)^{1/2}\), gives

\[
 M\leq2\pi H+2(Q/H)^{1/2}.
\]

For \(Q=C_\delta HY^{1/2+\delta}+E\), the inequality
\(\sqrt{a+b}\leq\sqrt a+\sqrt b\) proves (B).  Taking \(E=0\) and
using the local hypothesis with \(\delta=2\varepsilon\) gives the packet's
claimed

\[
 |P(x)|\ll_\varepsilon H+Y^{1/4+\varepsilon}.
\]

For the sharper ledger, the exponent of \(Q\) is \(q\); the two terms in
(L') have exponents \(q/3\) and \((q-\alpha)/2\), proving (X).  In
particular, with \(E=0\),

\[
 p=\max\left\{{\alpha\over3}+{1\over6}+{\delta\over3},
                    {1\over4}+{\delta\over2}\right\}.
\]

At \(\alpha=1/4+\sigma\) and \(\delta=o(1)\), this is
\(1/4+\sigma/3+o(1)\).  Thus a fixed positive \(\sigma\) cannot simply be
discarded.  More invariantly, to force a target amplitude \(A_0\) by this
method, the largest local-moment scale allowed by (A) is, up to absolute
constants,

\[
 Q\ll A_0^2\min(H,A_0).
 \tag{T}
\]

For \(A_0=Y^{1/4+o(1)}\), (T) is \(Q\ll HY^{1/2+o(1)}\) when
\(H\leq Y^{1/4+o(1)}\), and \(Q\ll Y^{3/4+o(1)}\) when
\(H\geq Y^{1/4+o(1)}\).  Therefore at
\(H=Y^{1/4+\sigma}\) with fixed \(\sigma>0\), a quarter-exponent
conclusion requires a total local bound of size \(Y^{3/4+o(1)}\), or
average size \(Y^{1/2-\sigma+o(1)}\), rather than the larger
\(HY^{1/2}\) scale.

**Unit-window equivalence.**  If \(M\geq2\pi\), the favourable unit
interval gives \(U(Y)\geq M^2/4\); if \(M<2\pi\), the constant term in
(U1) covers it.  This proves (U1), including values at isolated jumps.
(U2) is immediate by integrating the pointwise supremum over an interval
of length one.  Applying the forward pointwise estimate on the bounded
range of comparable scales \([Y/2,3Y]\), and choosing half the requested
epsilon before squaring, proves one direction at exponent level.  Taking
the square root in (U1), again with epsilon rescaled, proves the other.

**What the global moment alone gives.**  Use (C) and the favourable
segment of length

\[
 \ell_0=\min\left({M\over2\pi},{Y\over2}\right).
\]

It lies in \([Y/2,4Y]\), and hence

\[
 {M^2\ell_0\over4}\leq B_\delta(Y).
\]

If \(M\leq\pi Y\), this gives
\(M^3\ll Y^{3/2+\delta}\), hence
\(M\ll Y^{1/2+\delta/3}\).  If \(M>\pi Y\), it gives
\(M\ll Y^{1/4+\delta/2}\), contradicting \(M>\pi Y\) for all large
\(Y\).  Rescaling \(\delta\) proves the global-only prescribed-point
bound \(M\ll_\varepsilon Y^{1/2+\varepsilon}\).

This exponent cannot be improved from just the stated global bound,
monotonicity, and inclusive integer-jump structure.  Here is one explicit
abstract countermodel.  Put

\[
 B(t)=\lfloor\pi\lfloor t\rfloor\rfloor,
 \quad n_j=4^j,\quad K_j=2^j,\quad C_j=B(n_j)+K_j,
\]

and define the nondecreasing, integer-valued, right-continuous step
function

\[
 A_*(t)=\max\bigl(B(t),\max_{j:n_j\leq t} C_j\bigr),
 \qquad P_*(t)=A_*(t)-\pi t.
\]

All jumps of \(A_*\) occur at integers and their values are inclusive.
Outside a segment of length \(K_j/\pi+O(1)\) following \(n_j\),
\(P_*\) is bounded.  On that segment it is a descending spike of height
\(K_j+O(1)\).  The spikes are disjoint and geometrically separated, so
every dyadic block satisfies

\[
 \int_T^{2T}|P_*(t)|^2\,dt\ll T+T^{3/2}\ll T^{3/2},
\]

but \(|P_*(n_j)|\asymp n_j^{1/2}\).  A window of length
\(H=o(n_j^{1/2})\) immediately to the right of \(n_j\) even has moment
\(\asymp Hn_j\), much larger than \(Hn_j^{1/2}\).  This is not asserted
to be the Gauss counting function; it is a sharp logical obstruction
showing that the listed analytic premises do not entail a quarter bound
or a uniform local moment.  Additional arithmetic input would be needed.

## 4. First doubtful or unproved step

There is no unproved step in the persistence, bounded-overlap sampling,
integer exceptional-set, conditional local bridge, additive ledger, or
unit-window equivalence arguments.  The first genuinely unavailable step
is the passage from the global moment to a **supremum** over short-window
moments.

Indeed, if \(W(s)=\int_s^{s+H}|P(t)|^2\,dt\), Fubini and the global
moment give only

\[
 {1\over Y}\int_Y^{2Y-H}W(s)\,ds
 \ll_\delta HY^{1/2+\delta}.
\]

This is an average over window positions, not a uniform bound.  The spike
model in Section 3 satisfies the global estimate while violating the
desired local supremum by a power of \(Y\).  Consequently no
actual-coefficient short-window estimate, no prescribed-point quarter
bound, and no unassumed canonical-core estimate has been proved here.

## 5. Control tests and outcomes

- `positive_right_persistence` — **pass**.  It is the exact monotonicity
  identity (P+), with no loss beyond \(\pi u\).

- `negative_left_persistence` — **pass**.  It is the exact monotonicity
  identity (P-); reversing the direction or sign would be unjustified.

- `integer_jump_convention` — **pass**.  The inclusive post-jump value is
  used literally, and both inequalities remain valid at jump endpoints.

- `dyadic_boundary_windows` — **pass**.  Local sign-favourable intervals
  lie in \([Y/2,3Y]\); sampling intervals that cross \(Y\) or \(2Y\) are
  covered by the three blocks making up \([Y/2,4Y]\).

- `bounded_overlap_sampling` — **pass**.  Sign-oriented unit intervals
  have multiplicity at most three for a one-separated set.

- `integer_exceptional_count` — **pass**.  Threshold-squared division in
  (S) gives exactly \(Y^{1-2\eta+\delta}\).

- `local_bridge_exponent` — **pass with correction/sharpening**.  The
  advertised bridge is valid, but (A)--(L) are stronger.  A fixed
  \(H=Y^{1/4+\sigma}\) at the standard local scale yields exponent
  \(1/4+\sigma/3+o(1)\), not a strict quarter exponent.

- `additive_error_ledger` — **pass**.  The simple term is
  \((E/H)^{1/2}\); the exact inverse also contains the cubic regime and is
  summarized by (X).

- `unit_window_equivalence` — **pass**.  The exact inequalities are
  (U1)--(U2), with epsilon rescaled only when translating exponents.

- `canonical_core_nonimplication` — **pass as a no-go control**.  Global
  averaging does not imply a uniform local estimate or any unassumed
  coefficient/canonical-core cancellation; the explicit spike model
  witnesses the logical failure.

## 6. Dependencies and exact artifacts used

The derivation used only
`rounds/codex-managed/gc-prescribed-point-local-moment-bridge/briefs/blind_pointwise_bridge_rederivation.md`
and
`rounds/codex-managed/gc-prescribed-point-local-moment-bridge/derivation_packet.md`.
The only mathematical inputs taken from them were the definition of
\(P\), the inclusive convention, monotonicity of the counting function,
and the global dyadic mean square.  No graph, strategy file, prior or
sibling report, synthesis, source card, web source, or local-frequency
claim was opened or used.  No numerical experiment was needed.

## 7. Recommended state effect

Promote, subject to the conductor's seam check, the two persistence
inequalities, the bounded-overlap one-separated estimate, the integer
exceptional-set corollary, the exact conditional bridge (A)--(L), and the
unit-window equivalence.  Revise the additive-error statement to retain
both inverse branches and the exponent ledger (X).  Reject any inference
from the global moment to a uniform short-window moment or to a prescribed
quarter bound.  Retain the uniform local moment as an open obligation; at
\(H=Y^{1/4+\sigma}\) the quarter target requires the stronger total scale
\(Y^{3/4+o(1)}\), unless \(\sigma=o(1)\).  Make no change to shared proof
state on the basis of this candidate report alone.
