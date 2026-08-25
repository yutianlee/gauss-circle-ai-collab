# Round 162 post-unmask seam review: character-Poisson product collar

## 1. Result

**GREEN for the requested seams; no repair is required.**  The selected
candidate has the literal coefficient in the correct orientation, the
correct \(\chi _4\)-Poisson sign, the correct involution, the exact
squarefree/coprime opening and \((Q,R)\)-rescaling, the correct rank-one
stationary geometry, and the correct cone and product-collar powers.

In particular, with

\[
 Q=[a^2,c],\qquad R=[b^2,c],\qquad d_1=Qm,\qquad d_2=Rn,
\]

the one-variable character saddle is

\[
 m_s=\frac{4XQd_2}{s^2},\qquad
 d_1^*=\frac{4XQ^2d_2}{s^2},\qquad
 F_s(m_s)=\frac{XQd_2}{s},
\]

and its leading orientation is

\[
 e(1/8)\chi _4(Q)\chi _4(s).
\]

The exact two-variable resonant equation and collar are

\[
 s\ell=XQR,qquad
 |s\ell-XQR|\ll \frac{QRJ}{L},
\]

with cone

\[
 Q\ell\le Rs\le4Q\ell.
\]

One smooth dual slot has size
\(L^{3/2}/(QR\sqrt J)\), and the central collar has at most
\((QRJ/L+1)(XQR)^\varepsilon\) slots.  The \(QR\)-powers therefore cancel
under termwise positive control, leaving \(\sqrt{JL}\), exactly as the
candidate states.

The conductor's decision to leave the literal hard edges open is also
**GREEN**.  It is the logically conservative decision.  Zero extension
at a nonzero endpoint can produce only first-order Fourier decay; a
moving saddle meeting a hard edge is a transition term, not a rapidly
decaying interior error; and the files reviewed here do not certify the
literal profile variation and endpoint data needed for a complete edge
ledger.  The candidate explicitly keeps those families in the future
signed aggregate and does not use their omission as a saving.  This
preserves the smooth-interior route obstruction without promoting an
unproved hard-edge estimate.

This GREEN decision validates only the stated method obstruction.  It
does not prove the target estimate and does not turn the positive collar
capacity into physical mass or a lower bound.

## 2. Exact statement and hypotheses

The review concerns the selected candidate's following narrow claim.
For the literal scalar with

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=X/y^2,\qquad H=\lfloor yX^{-1/4}\rfloor,
\]

character-preserving Poisson followed by termwise positive dual control,
termwise positive control after the exact Mobius opening, a second bare
character transform, and standard positive differencing do not supply
the uniform gain required for

\[
 |\mathcal S_{L,1}|\ll_\varepsilon L^{3/2}X^\varepsilon,
 \qquad 1\ll L\ll H\asymp J^{1/2}.
\]

The exact algebra is reviewed without smoothness assumptions.  The
stationary principal coefficient and rapidly decaying collar tails are
reviewed for a compact smooth interior cell on the rescaled physical
support.  No claim is made that these principal formulas are all-orders
identities for the zero-extended hard amplitude.  The selected candidate
itself makes this distinction and leaves the literal hard families open.

The requested seam review covers:

1. the literal coefficient, parity, and orientation;
2. the additive \(\chi _4\) transform, its sign, leading Gaussian unit,
   and involution;
3. the exact Mobius projector and \((Q,R)\)-support rescaling;
4. one- and two-variable stationary equations;
5. the cone, radial degeneracy, collar width, factor count, and restored
   powers; and
6. the conductor's nonpromotion of a hard-edge estimate.

The named external-source comparisons in the candidate were not
re-audited from primary sources in this seam review.  GREEN therefore
does not add an independent source card for those comparisons.

## 3. Proof or derivation

**(a) Literal coefficient and arithmetic opening.**  The selected
candidate reproduces the scalar with \(\chi _4(d_1)\), positive phase
\(e(J\sqrt{d_1d_2})\), normalization
\((L^2/(d_1d_2))^{3/4}\), cone
\(d_2\le d_1\le4d_2\), and ratio profile

\[
 W\!\left(\sqrt{\frac{q_Xd_1}{4d_2}}\right).
\]

There is no swap of the two legs and no conjugation of the phase.  Only
\(d_1\) is forced odd.  The exact projector follows from

\[
 \mu^2(n)=\sum_{a^2\mid n}\mu(a),
 \qquad
 1_{(d_1,d_2)=1}=\sum_{c\mid(d_1,d_2)}\mu(c),
\]

and is

\[
 \mu^2(d_1)\mu^2(d_2)1_{(d_1,d_2)=1}
 =\sum_{a^2\mid d_1}\mu(a)
  \sum_{b^2\mid d_2}\mu(b)
  \sum_{c\mid(d_1,d_2)}\mu(c).
\]

For a fixed triple, divisibility is exactly encoded by

\[
 Q=[a^2,c],\qquad R=[b^2,c],\qquad d_1=Qm,\quad d_2=Rn.
\]

Since \(a,c\mid d_1\) and \(d_1\) is odd, \(a,c,Q,m\) are odd.  There is
no such restriction on \(b,R,n\); hence the even \(d_2\) branch is
retained.  For the surviving first leg,

\[
 \chi _4(Qm)=\chi _4(Q)\chi _4(m).
\]

These identities verify (162.CA2)--(162.CA6).  They also verify the
candidate's warning that individual opened terms include intermediate
nonsquarefree configurations and must be recombined with all Mobius signs.

**(b) Character-Poisson sign.**  With

\[
 \widehat g(\xi)=\int_{\mathbb R}g(x)e(-\xi x)\,dx,
 \qquad
 \chi _4(m)=\frac{e(m/4)-e(-m/4)}{2i},
\]

Poisson gives

\[
 \sum_m\chi _4(m)g(m)
 =\frac1{2i}\sum_{\sigma=\pm1}\sigma
   \sum_k\widehat g\!\left(k-\frac\sigma4\right).
\]

Set \(s=4k-\sigma\).  If \(\sigma=1\), then
\(s\equiv3\pmod4\) and \(\chi _4(s)=-1\).  If \(\sigma=-1\), then
\(s\equiv1\pmod4\) and \(\chi _4(s)=1\).  Thus in both cases

\[
 \sigma=-\chi _4(s),\qquad
 \frac{\sigma}{2i}=\frac i2\chi _4(s),
\]

which proves the candidate's exact identity

\[
 \boxed{
 \sum_m\chi _4(m)g(m)
 =\frac i2\sum_{\substack{s\in\mathbb Z\\s\ {
m odd}}}
 \chi _4(s)\widehat g(s/4).}
\]

The sign is therefore GREEN.

**(c) One-variable saddle, normalization, and literal profile.**  For a
fixed opening and fixed physical \(d_2\), the phase is

\[
 F_s(m)=J\sqrt{Qd_2m}-\frac s4m.
\]

Only \(s>0\) has an interior saddle, and direct differentiation gives

\[
 m_s=\frac{4XQd_2}{s^2},\qquad
 d_1^*=Qm_s=\frac{4XQ^2d_2}{s^2},
\]

\[
 F_s(m_s)=\frac{XQd_2}{s},
 \qquad
 F_s''(m_s)=-\frac{s^3}{32XQd_2}.
\]

At this saddle,

\[
 \begin{aligned}
 &\left(\frac{L^2}{d_1^*d_2}\right)^{3/4}
 |F_s''(m_s)|^{-1/2}\\
 &\qquad=\frac{2L^{3/2}X^{-1/4}}{Qd_2}
 =\frac{2L^{3/2}J^{-1/2}}{Qd_2}.
 \end{aligned}
\]

The quadratic direction is negative, so its Gaussian unit is
\(e(-1/8)\).  Multiplication by \(i/2\) from the character transform and
by the factor 2 above gives

\[
 i e(-1/8)=e(1/8).
\]

Together with the outer coefficient \(\chi _4(Q)\), the leading signed
unit is exactly

\[
 e(1/8)\chi _4(Q)\chi _4(s),
\]

not its conjugate or negative.

The cone substitution is also exact:

\[
 \frac{d_1^*}{d_2}=\frac{4XQ^2}{s^2},
\]

so \(1\le d_1^*/d_2\le4\) is equivalent to

\[
 JQ\le s\le2JQ.
\]

Finally,

\[
 \sqrt{\frac{q_Xd_1^*}{4d_2}}
 =\sqrt{\frac{X}{y^2}\frac{4XQ^2}{4s^2}}
 =\frac{XQ}{ys},
\]

because the stationary range has \(s>0\).  Thus (162.CA8)--(162.CA12),
including the exact floor-dependent \(W(XQ/(ys))\), are GREEN.

**(d) Involution.**  Define the continuous function

\[
 h(s)=\widehat g(s/4).
\]

Its Fourier transform is

\[
 \widehat h(\xi)
 =\int\widehat g(s/4)e(-\xi s)\,ds
 =4\int\widehat g(t)e(-4\xi t)\,dt
 =4g(-4\xi).
\]

Two character transforms therefore contribute

\[
 \left(\frac i2\right)^2
 \sum_{u\ {
m odd}}\chi _4(u)\,4g(-u)
 =-\sum_{u\ {
m odd}}\chi _4(u)g(-u).
\]

After \(v=-u\), the oddness
\(\chi _4(-v)=-\chi _4(v)\) supplies the second minus sign, returning

\[
 \sum_{v\ {
m odd}}\chi _4(v)g(v).
\]

Thus the reflection and scaling in (162.CA13) are correct.  A second bare
character transform is exactly involutive on the stated test-function
class and supplies no contraction.

**(e) Rank-one stationary equations and cone.**  The Hessian of
\(f(x,z)=J\sqrt{xz}\) is

\[
 \frac J4
 \begin{pmatrix}
 -z^{1/2}x^{-3/2}&(xz)^{-1/2}\\
 (xz)^{-1/2}&-x^{1/2}z^{-3/2}
 \end{pmatrix}.
\]

Its determinant is zero and its null vector is \((x,z)\), by direct
multiplication.  The linear dual terms do not alter this Hessian.

After ordinary Poisson in \(n\), the fixed-opening phase is

\[
 J\sqrt{QRmn}-\frac s4m-\ell n.
\]

In physical variables \(u=Qm=tw\), \(v=Rn=t/w\), it becomes

\[
 t\left(J-\frac{s}{4Q}w-\frac{\ell}{Rw}\right).
\]

The angular equations are

\[
 \frac{s}{4Q}=\frac J2\sqrt{\frac vu},
 \qquad
 \frac{\ell}{R}=\frac J2\sqrt{\frac uv},
\]

and multiplication gives

\[
 \boxed{s\ell=XQR.}
\]

At the angular saddle,

\[
 w_0^2=\frac{4Q\ell}{Rs}.
\]

Since the physical cone is \(1\le u/v=w^2\le4\), its exact dual form is

\[
 \boxed{Q\ell\le Rs\le4Q\ell.}
\]

All equations (162.CA14)--(162.CA18) are therefore GREEN.  In particular,
the candidate never divides by a nonexistent Hessian determinant.

**(f) Collar and restored \((Q,R)\)-powers.**  At \(w=w_0\), the radial
frequency is

\[
 \delta_{Q,R}(s,\ell)
 =J-\sqrt{\frac{s\ell}{QR}}.
\]

For \(s\ell\asymp XQR\), rationalization gives

\[
 |\delta_{Q,R}|
 =\frac{|s\ell-XQR|}
 {QR\left(J+\sqrt{s\ell/(QR)}\right)}
 \asymp\frac{|s\ell-XQR|}{QRJ}.
\]

A physical radial cell of length \(\asymp L\) is non-negligible in its
central Fourier window only when \(|\delta_{Q,R}|\ll L^{-1}\), hence

\[
 \boxed{|s\ell-XQR|\ll QRJ/L.}
\]

The same width follows sequentially: the first saddle leaves phase
\((XQR/s-\ell)n\), while \(n\) has length \(L/R\); therefore

\[
 \left|\frac{XQR}{s}-\ell\right|\ll\frac RL,
\]

and \(s\asymp JQ\) gives the displayed product collar.

Because \(s\ell\) is an integer, the number of possible products in the
window is \(O(QRJ/L+1)\).  Each has at most
\(O_\varepsilon((XQR)^\varepsilon)\) admissible factorizations.  Thus the
candidate's count (162.CA21) is correct.

After writing \(d_2=Rn\), the leading pointwise coefficient from part
(c) is proportional to

\[
 \frac{L^{3/2}}{\sqrt J\,QRn}.
\]

Since \(n\asymp L/R\), and the radial \(n\)-interval has length
\(L/R\), one central dual slot has size

\[
 \frac{L^{3/2}}{QR\sqrt J}.
\]

Multiplication by the collar count gives

\[
 \frac{QRJ}{L}\frac{L^{3/2}}{QR\sqrt J}
 =\sqrt{JL}.
\]

This verifies (162.CA19)--(162.CA23).  The cancellation of \(QR\) is
exact at the power-ledger level; there is no hidden absolutely summable
gain in the fixed-opening rescaling.

**(g) Audit of the hard-edge decision.**  The selected candidate does
not assert that every hard edge is target-safe.  This is correct for four
independent reasons.

1. A nonzero endpoint left by zero extension has a Fourier transform with
   a first boundary term of order \(|\xi|^{-1}\).  Its full dual absolute
   sum is not automatically summable, so smooth rapid-decay estimates
   cannot simply be assigned to it.
2. When the moving transverse saddle reaches a hard support boundary, it
   lies in a boundary stationary/Fresnel transition.  The interior
   principal formula alone neither deletes nor uniformly estimates that
   family.
3. The literal cone equalities may vanish after the complete physical
   squarefree/coprime projector, but an individual Mobius-opened term
   does not inherit that cancellation.  In addition, the shell and named
   profiles have their own entries, exits, floors, and endpoint values.
4. The reviewed materials do not provide a complete finite-piece
   regularity and endpoint ledger that would justify peeling every edge
   and summing the resulting opened families.

Leaving these terms in the open signed aggregate does not undermine the
selected no-go.  The candidate's favorable smooth-interior calculation
already shows that termwise positive collar control does not pay the
required power on intermediate blocks.  A future cancellation between
interior and boundary terms would itself be a new joint signed theorem,
which the candidate explicitly leaves open.  The schematic formula
(162.CA30) is correctly labeled as the smooth principal interface and
not as a replacement for the literal boundary owners.

## 4. First doubtful or unproved step

There is no doubtful algebraic step in the reviewed coefficient,
character, scaling, stationary, cone, collar, or involution seams.  The
first unproved affirmative step remains exactly the one identified by the
candidate: a target-strength estimate for the complete signed aggregate,
retaining

\[
 \mu(a)\mu(b)\mu(c)\chi _4(Q)\chi _4(s),
\]

the moving near-square divisor window, all literal profiles, the even
\(d_2\) branch, collar tails, floors, zero-extension terms, boundary
transitions, and arbitrary-real-centre uniformity before every positive
norm.

The hard-edge substep is genuinely open rather than silently discharged.
To turn it green for an affirmative proof one would need the exact
profile definitions and a uniform decomposition showing, for every entry
and exit, either a target-safe primal bound or a jointly signed transformed
bound.  Nothing in the selected candidate assumes this result.

The positive quantity \(\sqrt{JL}\) remains a method capacity only.
Neither the candidate nor this review supplies a matching lower bound or
shows that the physical coefficients are nonzero on enough collar slots.

## 5. Control tests and outcomes

| Seam control | Outcome |
|---|---|
| Literal coefficient and orientation | **GREEN.** \(\chi _4\) remains on the first leg; the phase, normalization, cone, ratio profile, floors, and even second leg have the displayed orientation. |
| Exact Mobius projector | **GREEN.** The three sums in (162.CA4) and the lcm scalings \(Q=[a^2,c]\), \(R=[b^2,c]\) are exact, including shared primes. |
| Parity under \((Q,R)\)-scaling | **GREEN.** \(a,c,Q,m\) are odd; \(b,R,n\) need not be odd, so the even \(d_2\) branch is retained. |
| \(\chi _4\)-Poisson coefficient | **GREEN.** The exact coefficient is \(i\chi _4(s)/2\), not \(-i\chi _4(s)/2\). |
| Stationary Gaussian orientation | **GREEN.** Negative curvature contributes \(e(-1/8)\), and together with \(i/2\) and the normalization factor 2 yields \(e(1/8)\). |
| Bare character involution | **GREEN.** Fourier scaling gives 4, \((i/2)^2=-1/4\), and odd reflection supplies the compensating minus sign. |
| One-variable saddle and literal \(W\)-profile | **GREEN.** \(m_s=4XQd_2/s^2\), phase \(XQd_2/s\), cone \(JQ\le s\le2JQ\), and profile \(W(XQ/(ys))\) are exact. |
| Rank-one product geometry | **GREEN.** The Hessian determinant is zero with radial null vector; no two-variable determinant estimate is used. |
| Two-variable product and cone | **GREEN.** \(s\ell=XQR\) and \(Q\ell\le Rs\le4Q\ell\) follow directly from the angular equations. |
| Dual product collar | **GREEN.** The radial and sequential derivations both give width \(QRJ/L\). |
| Collar count and coefficient power | **GREEN.** The count is \(O_\varepsilon((QRJ/L+1)(XQR)^\varepsilon)\), one slot is \(L^{3/2}/(QR\sqrt J)\), and the product is \(\sqrt{JL}\). |
| Literal hard edges | **GREEN AS OPEN.** The candidate correctly rejects a blanket target-safe claim and retains endpoints and saddle-edge transitions in the future signed aggregate. |
| Physical-mass distinction | **GREEN.** \(\sqrt{JL}\) and \(\min\{L^2,\sqrt{JL}\}\) are labeled route capacities, not upper/lower bounds for the complete physical Mobius sum. |
| Downstream scope | **GREEN.** The candidate does not close other few-point channels or any parent obligation. |

No numerical experiment was used in this review.

## 6. Dependencies and exact artifacts used

This post-unmask review used exactly:

1. `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/candidates/conductor_round162_t1_character_poisson_collar_obstruction.md`;
2. `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/reports/blind_t1_close_factor_rederivation.md`;
3. `rounds/codex-managed/m9-m2-hard-top-t1-close-factor-bilinear-gate/controls/conductor_round162_reproduction_and_selection.md`.

No state file, sibling report, external source, web page, code, or
numerical output was used.  The source-theorem comparisons in the selected
candidate are therefore outside this review's independent GREEN scope.

## 7. Recommended state effect

**GREEN: retain the selected candidate without repair for the reviewed
seams.**  It may support the proposed method-obstruction node, subject to
the conductor's remaining graph and source requirements.  Do not promote
(162.CA1), do not record the positive collar capacity as physical mass,
and do not mark the literal hard-edge families closed.  Their inclusion
in the first future joint signed aggregate is the correct state boundary.
