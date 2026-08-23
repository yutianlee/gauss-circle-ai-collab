# Round 118 square-sector seam review

## Decision

**PASS WITH REPAIR.**  The odd-`r` Poisson normalization, the interior stationary coefficient
scale, the phase-one count for the stated integer parameter, and the
\(\chi _4\)-weighted square-sector estimate are correct.  The estimate controls
the complete **interior leading stationary phase-one sector** under a uniform
smooth-profile hypothesis.  It does not, as written, control every exactly
coherent sector for arbitrary real \(X\), nor the stationary transition and
endpoint packages.

| Item | Verdict | Required qualification |
|---|---|---|
| Odd-`r` Poisson factor and phase | Pass | Smooth positive-support row; the other physical sign is its conjugate. |
| Stationary coefficient \(\sqrt F/M\) | Pass | Interior critical point, uniformly separated from profile endpoints. |
| Phase-one count \(O(\sqrt M X^\varepsilon)\) | Pass | For \(X=bA^2\in\mathbb Z\), \(b\) squarefree. |
| Actual \(\chi _4\)-weighted square sector \(O_G(\sqrt M)\) | Pass | Uniform compact scaled support and uniform \(C^1\) seminorms for the actual family \(G=G_X\). |
| Unsigned \(O_G(\sqrt M\log(2L))\) | Pass as an upper bound | Logarithmic sharpness needs a nonnegative profile with nonzero bulk integral. |
| “Complete exactly coherent sector” without restricting \(X\) | Fail | Replace by “complete phase-one sector for integer \(X\)” or classify the other common phases separately. |

## Odd-`r` Poisson and stationary normalization

With \(e(t)=e^{2\pi i t}\), writing \(r=2n+1\) and
\(\chi _4(2n+1)=(-1)^n\) gives exactly
\[
 \sum_{r\ {m odd}}\chi _4(r)f(r)
 =\frac12\sum_{\nu\in 2\mathbb Z+1}e(-\nu/4)
   \int_{\mathbb R}f(r)e(\nu r/4)\,dr .
\]
For positive \(r\), only \(\nu>0\) has a critical point in
\[
 \Phi(r)=\frac{Xk}{r}+\frac{\nu r}{4},\qquad
 r_0=2\sqrt{\frac{Xk}{\nu}},\qquad
 \Phi(r_0)=\sqrt{Xk\nu},\qquad
 \Phi''(r_0)=\frac{\nu}{2r_0}.
\]
Positive curvature contributes \(e(1/8)/\sqrt{\Phi''(r_0)}\).  Including the
outer factor \(1/2\), its magnitude is
\[
 \frac12\sqrt{\frac{2r_0}{\nu}}=\sqrt{\frac{r_0}{2\nu}}.
\]
For odd \(\nu\), the remaining root number is exactly
\[
 e(-\nu/4)e(1/8)=e(-1/8)\chi _4(\nu).
\]
Thus the coefficient displayed in the probe, including \(q_L(\nu)/k\) and
the literal smooth weight, has the right sign and normalization.  On
\(k\asymp K\), \(\nu\asymp L\), and \(r_0\asymp R=X/D\),
\[
 \frac1K\sqrt{\frac RL}
 =\frac{\sqrt F}{M},
 \qquad F=\frac{XL}{D},\quad M=KL,\quad K=\frac{XL}{D^2}.
\]

This is an interior leading-term identity.  It is not a bound for a critical
point entering or leaving the support, for a hard/star endpoint, or for the
stationary remainder.  Those terms require their separate transition and
endpoint owners.

## Phase-one count and parity

Let \(X=bA^2\in\mathbb Z\), with \(b\) squarefree.  Then
\[
 e(\sqrt{Xk\nu})=1
 \quad\Longleftrightarrow\quad
 bk\nu\text{ is a square}
 \quad\Longleftrightarrow\quad
 k\nu=bw^2.
\]
Since \(k\nu\asymp M\), there are
\(O(\sqrt{M/b})\) possible \(w\), and each has at most
\(\tau(bw^2)\ll X^\varepsilon\) admissible divisor pairs.  Hence the claimed
\(O(\sqrt M X^\varepsilon)\) count is valid.  The condition \(\nu\) odd causes
no loss in this upper bound, including when \(b\) is even.

For the worst square case \(b=1\), uniqueness of the squarefree kernel gives
\[
 k=a u^2,\qquad \nu=a v^2,
\]
where \(a\) and \(v\) are odd and \(u\) is unrestricted.  Consequently
\(\chi _4(\nu)=\chi _4(a)\); there is no missing parity sign.

## Euler summation and the actual signed saving

Put \(U=(K/a)^{1/2}\), \(V=(L/a)^{1/2}\).  For a fixed compactly supported
scaled \(C^1\) weight away from the coordinate axes, two-dimensional Euler
summation gives, uniformly in the relevant \(a\),
\[
 \sum_{u,v\geq1}G(u/U,v/V)
 =c_GUV+O_G(U+V+1).
\]
The main term is \(c_G\sqrt M/a\).  Its signed coefficient is bounded because
\[
 \sum_{\substack{a\leq A\\a\ {m odd}}}
   \frac{\mu^2(a)\chi _4(a)}a=O(1).
\]
Indeed, insert \(\mu^2(a)=\sum_{d^2\mid a}\mu(d)\); the inner partial sums of
\(\sum_m\chi _4(m)/m\) are uniformly bounded, while
\(\sum_{d\ {m odd}}d^{-2}<\infty\).  There is therefore no omitted
logarithmic tail in the signed main term.

Since the scaled support forces \(a\ll L\), the Euler errors cost
\[
 \sqrt K\sum_{a\ll L}a^{-1/2}
 +\sqrt L\sum_{a\ll L}a^{-1/2}
 +\sum_{a\ll L}1
 \ll \sqrt M+L\ll\sqrt M,
\]
using the unbalanced ordering \(K\geq L\).  Thus
\[
 S_G=O_G(\sqrt M)
\]
is correct.  Removing \(\chi _4(a)\) replaces the bounded harmonic sum by
\(O(\log(2L))\), yielding the valid upper bound
\(O_G(\sqrt M\log(2L))\).  A claim that the logarithm is attained needs, for
example, \(G\geq0\) with nonzero bulk integral.

For the literal profile this proof must record uniformity, not merely write
\(O_G\): after scaling it is of the form
\[
 G_X(x,y)=q_L(Ly^2)
 W\!\left(\frac{y}{2x}\right)x^{-3/2}y^{-3/2}
\]
up to fixed normalization.  The conclusion is uniform if this family has
compact support separated from \(x y=0\) and uniformly bounded scaled
\(C^1\) seminorms.  The flat smooth cell has this property after an interior
cutoff; endpoint/transition pieces do not follow from this Euler argument.

Multiplying by the stationary scale gives
\[
 \frac{\sqrt F}{M}S_G
 \ll \sqrt{\frac FM}=\sqrt{\frac DL},
\]
so the signed square-sector contribution is target-safe throughout the stated
strict unbalanced range \(D/L<X^{1/2}\).

## Exact scope of coherence

The preceding parametrization exhausts the **phase-one** pairs for the stated
integer \(X\).  It does not exhaust equal nonzero phases when \(X\) is allowed
to be an arbitrary real parameter.  For example, if \(X=A^2/4\) with \(A\)
odd, then every odd square \(k\nu=t^2\) has
\(e(\sqrt{Xk\nu})=e(At/2)=-1\).  This is a large exactly coherent sector but
is absent from the phase-one parametrization.

Accordingly, the probe may promote the following scoped claim:

> For integer \(X=bA^2\), the complete interior leading stationary phase-one
> sector has \(O(\sqrt M X^\varepsilon)\) modes; when \(b=1\), its literal
> \(\chi _4\)-weighted leading sum is \(O_G(\sqrt M)\), hence contributes
> \(O_G(\sqrt{D/L})\).

It must not promote this as control of the complete coherent sector uniformly
in real \(X\), of the stationary endpoints/remainders, or of the nonsquare
complement.  Those are separate obligations.
