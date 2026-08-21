# Blind primitive-ray q-dispersion rederivation

## 1. Result

**Result: exact reduction, followed by an equal-capacity no-go.** The
change of variables is a bijection from the primitive odd rays in the
stated cone to

\[
 \mathscr L=\{(m,q)\in\mathbb Z_{>0}^2:
 5q<3m,\ m+q\equiv1\pmod 2,\ (m,q)=1\}.
\]

On this lattice

\[
 a=m-q,\qquad b=m+q,\qquad
 \chi _4(a)\chi _4(b)=(-1)^q=(-1)^{m-1}.
\]

Thus the character is constant on every fixed-\(m\) fibre. The first
lattice-preserving fixed-\(m\) shift is \(q\mapsto q+2\), whose character
product is \(+1\). If the block is instead grouped into \(q\)-slices,
the first signed autocorrelation is

\[
 \Gamma _1=-\mathcal C_1,\qquad
 \mathcal C_1=\sum_qF_{q+1}\overline{F_q}.
\]

Its complete expansion is (3.6). Every pair in it has \(m'-m\) odd, so
this is not a same-\(m\) local \(q\)-difference.

There is also an exact phase factorization of the complete coefficient.
If \(r\) is a metric Fourier mode and \(g\) is an active odd lift, its
\(q\)-phase has coefficient

\[
 \alpha=r-\frac g2\in\mathbb Z+\frac12.
\]

The density mode \(r=0\) therefore belongs to the same nonzero
half-integral phase family as every discrepancy mode. At the
\(q\)-slice level, modulation by \(e(q/2)\) translates dual frequencies
by \(1/2\). On the exact fixed-\(m\) parity coset, however, the character
is a scalar and Poisson has a \(1/2\)-spaced dual lattice that includes
zero. Neither representation removes a frequency or reduces the
operator norm. Exact differencing gives the Gram form (3.9). With only
Cauchy/Plancherel control, it returns at the original positive capacity.
No \(\rho^{-1/2}\) gain and no genuinely hard growing-\(\rho\) subrange
follow from the packet. The first smaller survivor is the full
complete-coefficient shifted Gram form, including its density mode,
primitive mask, moving endpoints, lifts, and entry/exit samples.

## 2. Exact statement and hypotheses

Fix one residual block \((A,D,K,G,R)\) satisfying every hypothesis in
the statement packet. Put

\[
\begin{aligned}
 a(m,q)&=m-q, & b(m,q)&=m+q,\\
 v(m,q)&=\sqrt{m^2-q^2}, &
 u(m,q)&=\frac{q}{m+v(m,q)},\\
 \Lambda(m,q)&=Xq\,u(m,q)
              =X\bigl(m-v(m,q)\bigr).
\end{aligned}
\]

Let \(\mathscr D\subset\mathscr L\) be the exact block domain after
retaining the residual indicator, dyadic restrictions, and
\(m^2-q^2=ab\ne\square\). All previously owned sets are absent from
\(\mathscr D\). Define the literal integer interval

\[
 \mathcal I_{m,q}=
 \left\{k\in\mathbb Z:
 \frac{Ju(m,q)}{1-u(m,q)}<k<
 \frac{2Ju(m,q)}{1+u(m,q)}\right\};
\]

the weight \(\omega\) retains the \(K\)-localization. With

\[
 C_{m,q,k}(g)=\mathfrak C^\circ_{m-q,m+q,k}(g),
\]

put

\[
\begin{aligned}
 B_{m,q}={}&\mathbf 1_{\mathscr D}(m,q)
 \sum_{g\in\mathcal G_{m-q,m+q}}
 \sum_{k\in\mathcal I_{m,q}}
 \omega(k)W_R\!\left(\frac{\Lambda(m,q)}k\right)
 C_{m,q,k}(g),                                      \tag{2.1}\\
 F_q={}&\sum_mB_{m,q},
\end{aligned}
\]

and extend \(F_q\) by zero to every \(q\in\mathbb Z\). Then

\[
 \mathfrak Q_{A,D,K,G,R}=\sum_q(-1)^qF_q.            \tag{2.2}
\]

No smooth extension across the primitive mask, a moving \(k\)-endpoint,
a lift-set endpoint, a square-ray exclusion, or an exact-centre
exclusion is assumed. No estimate for a shifted correlation is among
the packet hypotheses. The conclusion below is therefore a no-go for
the proposed formal one-step mechanism under the stated hypotheses,
not a counterexample to the canonical theorem.

## 3. Proof or derivation

For odd \(a,b\), the numbers \(m=(a+b)/2\) and \(q=(b-a)/2\) are
integers of opposite parity. Conversely, \(m+q\) odd makes both
\(m-q\) and \(m+q\) odd. Moreover,

\[
 \gcd(m-q,m+q)=\gcd(m-q,2q)
 =\gcd(m-q,q)=\gcd(m,q),
\]

where the second equality uses that \(m-q\) is odd. Finally,
\(a<b<4a\) is equivalent to \(q>0\) and \(5q<3m\). This proves the
lattice assertion. For odd \(n\),
\(\chi _4(n)=(-1)^{(n-1)/2}\), whence

\[
 \chi _4(a)\chi _4(b)=(-1)^{m-1}=(-1)^q.
\]

For an odd lift \(g\), multiplication by \(\chi _4(g)^2=1\) changes
nothing.

Rationalizing \(u\) gives

\[
 u=\frac{\sqrt b-\sqrt a}{\sqrt b+\sqrt a},\qquad
 qu=m-\sqrt{ab},\qquad
 \Lambda=X(m-\sqrt{ab}),                              \tag{3.1}
\]

and the two moving endpoints become

\[
 \kappa_-(m,q)=\frac J2\left(\sqrt{\frac ba}-1\right),
 \qquad
 \kappa_+(m,q)=J\left(1-\sqrt{\frac ab}\right).        \tag{3.2}
\]

These endpoints are not replaced by fixed dyadic endpoints.

There is an exact completion of the phase in the actual symbol. Set
\(x=y^2\) and

\[
 y_0=\frac{J\sqrt g(\sqrt b-\sqrt a)}{2k}.
\]

Then

\[
 C_{m,q,k}(g)
 =e\!\left(-\frac{g\Lambda(m,q)}{2k}\right)
  \widetilde C_{m,q,k}(g),                             \tag{3.3}
\]

where, without altering the amplitude,

\[
 \widetilde C_{m,q,k}(g)=
 \int_{\sqrt{gb}/2}^{\sqrt{ga}}
 2yA^\circ_{ga,gb}(y^2)e\bigl(k(y-y_0)^2\bigr)\,dy.    \tag{3.4}
\]

The inequalities \(\kappa_-<k<\kappa_+\) are exactly
\(y_0<\sqrt{ga}\) and \(y_0>\sqrt{gb}/2\). Thus an integer crossing
either endpoint is a genuine saddle entry/exit sample.

Using \(\widehat W_R(0)=\mu_R\), (3.3) gives the joint exact expansion

\[
 W_R\!\left(\frac\Lambda k\right)C_{m,q,k}(g)
 =\sum_{r\in\mathbb Z}\widehat W_R(r)
 e\!\left(\left(r-\frac g2\right)\frac\Lambda k\right)
 \widetilde C_{m,q,k}(g).                              \tag{3.5}
\]

Because \(g\) is odd, \(r-g/2\) is a nonzero half-integer for every
\(r\), including \(r=0\). Formula (3.5) is an identity for the whole
coefficient; it does not license a separate density estimate.

For \(s\ge0\), define the unsigned \(q\)-slice correlation

\[
 \mathcal C_s=\sum_qF_{q+s}\overline{F_q}.
\]

Writing
\[
 a'=m'-(q+s),\qquad b'=m'+q+s,\qquad
 \Lambda'=\Lambda(m',q+s),
\]
its exact expansion is

\[
\begin{aligned}
 \mathcal C_s={}&
 \sum_{\substack{q,m,m'\\
                  (m,q),(m',q+s)\in\mathscr D}}
 \sum_{\substack{g\in\mathcal G_{a,b}\\
                  g'\in\mathcal G_{a',b'}}}
 \sum_{\substack{k\in\mathcal I_{m,q}\\
                  k'\in\mathcal I_{m',q+s}}}
 \omega(k')\overline{\omega(k)}\\
 &\quad\times
 W_R\!\left(\frac{\Lambda'}{k'}\right)
 \overline{W_R\!\left(\frac\Lambda k\right)}
 C_{m',q+s,k'}(g')\overline{C_{m,q,k}(g)}.             \tag{3.6}
\end{aligned}
\]

If (3.5) is inserted, the metric factor in (3.6) is the single double
sum

\[
 \sum_{r',r\in\mathbb Z}
 \widehat W_R(r')\overline{\widehat W_R(r)}
 e\!\left(
 \left(r'-\frac{g'}2\right)\frac{\Lambda'}{k'}-
 \left(r-\frac g2\right)\frac\Lambda k\right),         \tag{3.7}
\]

including all \(r=0\), \(r'=0\), and cross terms. The signed
autocorrelation is

\[
 \Gamma_s=
 \sum_q(-1)^{q+s}F_{q+s}\overline{(-1)^qF_q}
 =(-1)^s\mathcal C_s.                                  \tag{3.8}
\]

In particular, \(\Gamma_1=-\mathcal C_1\). Lattice parity in (3.6)
forces \(m'-m\equiv s\pmod2\). Hence \(s=1\) contains no \(m'=m\)
pair. On a fixed-\(m\) fibre, only even \(s\) occur and the character
factor in (3.8) is \(+1\). The nearest lattice-preserving odd shifts
are \((m,q)\mapsto(m+1,q+1)\), which holds \(a\) fixed and sends
\(b\mapsto b+2\), and \((m,q)\mapsto(m-1,q+1)\), which holds \(b\)
fixed and sends \(a\mapsto a-2\). Either shift changes the primitive
mask, the other ray endpoint, both reciprocal endpoints, the lift set,
and the complete actual symbol.

Let the \(q\)-support be contained in an interval of \(N\) consecutive
integers. For \(1\le H\le N\), zero extension, shift averaging, and
Cauchy give the exact one-step van der Corput inequality

\[
\begin{aligned}
 H^2|\mathfrak Q_{A,D,K,G,R}|^2
 &\le (N+H-1)\mathcal V_H,\\
 \mathcal V_H
 &=H\mathcal C_0+
 2\Re\sum_{s=1}^{H-1}(H-s)(-1)^s\mathcal C_s\\
 &=\sum_n\left|
 \sum_{h=1}^H(-1)^{n+h}F_{n+h}\right|^2.              \tag{3.9}
\end{aligned}
\]

For \(H=2\), this is the literal first-difference identity

\[
\begin{aligned}
 2\mathfrak Q&=\sum_q(-1)^q(F_q-F_{q+1}),\\
 \mathcal V_2
 &=2\mathcal C_0-2\Re\mathcal C_1
 =\sum_q|F_q-F_{q+1}|^2.                               \tag{3.10}
\end{aligned}
\]

The only structure-free estimate is
\(\lvert\mathcal C_s\rvert\le\mathcal C_0\). Inserting it into (3.9)
gives
\(\lvert\mathfrak Q\rvert^2\ll(N+H)\mathcal C_0\), the same capacity
as direct \(q\)-Cauchy. The signs in (3.9) cannot be used after
replacing \(\mathcal C_s\) by absolute values.

Finally, (3.5) shows explicitly what a lawful Poisson step does. Exact
parity must be imposed first. For fixed \(m\), put
\(r_m\equiv1-m\pmod2\). If \(f_m\) denotes any lawfully completed
fixed-\(m\) coefficient and
\(\widehat f_m(\xi)=\int f_m(t)e(-\xi t)\,dt\), then

\[
\begin{aligned}
 \sum_{\substack{q\in\mathbb Z\\q\equiv r_m\ (2)}}
 (-1)^qf_m(q)
 &=(-1)^{m-1}\sum_{j\in\mathbb Z}f_m(r_m+2j)\\
 &=\frac{(-1)^{m-1}}2
 \sum_{\ell\in\mathbb Z}
 e(\ell r_m/2)\widehat f_m(\ell/2).
\end{aligned}
\]

Thus the character is a scalar on the exact fibre and the dual
frequency is \(\beta=\ell/2\in\frac12\mathbb Z\), including
\(\beta=0\). If one instead forms the \(q\)-slice \(F_q\) first, the
modulation \(e(q/2)\) translates integer dual frequencies to
\(\mathbb Z+1/2\); the price is that adjacent slices contain opposite
\(m\)-parities and have no supplied smooth extension. These are two
unitarily equivalent descriptions, not two sources of saving.

For a fixed phase in (3.5), put
\(\alpha=r-g/2\), \(c=\alpha X/k\), and

\[
 \psi(q)=c\bigl(m-\sqrt{m^2-q^2}\bigr).
\]

At dual frequency \(\beta\in\frac12\mathbb Z\), a stationary point
obeys

\[
 \frac{cq}{\sqrt{m^2-q^2}}=\beta,                      \tag{3.11}
\]

and, when \(c\beta>0\), the stationary phase is

\[
 \psi(q_*)-\beta q_*
 =m\left(c-\operatorname{sgn}(c)
 \sqrt{c^2+\beta^2}\right).                            \tag{3.12}
\]

Thus the half-integral primal label \(\alpha\) is accompanied by the
full half-spaced dual lattice \(\frac12\mathbb Z\); there is no deleted
frequency class. Poisson/Plancherel is a norm-preserving
re-expression, and a second Fourier transform is adjoint return. In
the correlation (3.7), with \(\alpha'=r'-g'/2\), the exact
\(q\)-curvature is

\[
 \Phi_s''(q)=X\left[
 \frac{\alpha'm'^2}
 {k'\{m'^2-(q+s)^2\}^{3/2}}-
 \frac{\alpha m^2}
 {k\{m^2-q^2\}^{3/2}}
 \right].                                              \tag{3.13}
\]

No hypothesis supplies a lower bound for (3.13), or a count for its
exact and near-zero determinant locus. Consequently Poisson merely
replaces the full shifted Gram form by its adjoint dual form at equal
capacity.

## 4. First doubtful or unproved step

Everything through (3.13) is algebraic. The first unproved inequality
needed by the proposed mechanism is: for some lawful
\(1\le H\le N\), with the complete correlations (3.6), prove

\[
 \boxed{\displaystyle
 \mathcal V_H\ll_\varepsilon
 \frac{H^2}{N+H-1}L^4X^{2\varepsilon}.}                \tag{U96}
\]

This would imply a target-sized bound for that block through (3.9). At
the same \(q\)-Cauchy normalization, obtaining the advertised
\(\rho^{-1/2}\) gain requires the relative form

\[
 \mathcal V_H\ll
 \frac{H^2N}{(N+H-1)\rho}\mathcal C_0.                 \tag{U96'}
\]

If off-diagonal correlations are only bounded in absolute value and
the diagonal term \(H\mathcal C_0\) remains, (U96') requires
\(H\gtrsim\rho\). Since \(N\ll D\), this standard one-step route cannot
reach blocks with \(\rho\gg D\). The displayed hypotheses prove neither
(U96) nor (U96') in the potentially accessible range
\(\rho\lesssim D\). At \(H=2\), the first local version is a bound for
the full difference energy in (3.10), equivalently a quantitatively
controlled real part of the exact \(\mathcal C_1\). Sampled variation
of individual actual symbols does not bound that object because its two
\(q\)-slices have different \(m\)-parity, primitive masks, moving
integer intervals, and lift sets. A Poisson proof of (U96) would in turn
require a quantitative separation/count for the near-zero locus of
(3.13); that is also unstated and unproved.

## 5. Required control test and outcome

**Control 1 — exact lattice.** Passed algebraically: the domain is
\(5q<3m\), \(m+q\) odd, and \((m,q)=1\). Fixed-\(m\) shifts are even;
odd \(q\)-slice shifts force \(m'-m\) odd. Coprimality is retained as
two separate exact indicators in (3.6), not replaced by density.

**Control 2 — moving interval and entry/exit.** Passed as an identity,
but it obstructs the estimate. Both members of (3.6) use their own
strict intervals with endpoints (3.2). Zero extension retains every
integer entering or leaving either interval. Formula (3.4) shows that
these are precisely saddle entry/exit samples. A diagonal lattice shift
changes them; no boundary sample is discarded or declared small.

**Control 3 — metric density mode.** Passed. Equations (3.5) and (3.7)
keep \(r=0\) and \(r'=0\), their cross terms, and all discrepancy modes
in one coefficient. The density mode has \(\alpha=-g/2\ne0\); deleting
it before the signed estimate would change the operator. Nothing in the
packet bounds the resulting joint Gram form.

**Control 4 — orientations, real part, and stars.** Passed. The primed
factor and every weight in the unprimed factor are conjugated in
(3.6)–(3.7). The conjugate orientation gives the adjoint correlation.
The accepted outer \(2\Re\) is applied only after the complete complex
sum; it supplies at most
\(\lvert2\Re z\rvert\le2\lvert z\rvert\), not extra cancellation. No
orientation or star is counted twice.

**Control 5 — prior owners.** Passed. The residual indicator in (2.1)
excludes square rays and exact nonsquare centres from both sides of
every correlation. If a shift lands in an excluded set, the shifted
coefficient is zero. The resulting unmatched residual term is a
difference boundary; it is not charged to the prior owner, which would
double count.

**Control 6 — near-square, Pell, and fixed/short \(q\).** The proposed
gain fails this control. On a fixed-\(q\) or one-slice family there is
no nonzero \(q\)-shift correlation, and \((-1)^q\) is a scalar. On a
fixed-\(m\) fibre it is again a scalar because admissible \(q\)'s differ
by two. A two-slice family can have arbitrary relative phase. The
displayed scale relations do not preclude \(D=O(1)\) together with
\(\rho=AJD^3/L^3\gg1\), so short-\(q\) blocks cannot be silently
removed. Near-square/Pell families are not exact square rays and remain
in (3.6); a \(q\)-shift does not preserve such a family or provide a
correlation estimate for it.

**Control 7 — fourth powers and metric resonances.** If \(ab\) itself
is a fourth power, it is a square and is already excluded. No broader
fourth-power phase exclusion is stated, so all other resonant or
near-resonant cases remain. Exact metric resonance
\(\lVert\Lambda/k\rVert=0\) is outside the punctured support of \(W_R\),
but a shift into that zero creates an unmatched boundary term. Near
resonance is allowed. Indeed, for \(\Lambda/k=n+\delta\), the density
component contains

\[
 (-1)^qe\!\left(-\frac g2(n+\delta)\right)
 =(-1)^{q+n}e(-g\delta/2)
\]

because \(g\) is odd. When \(n\equiv q\pmod2\), the visible character is
neutralized; the packet gives no exclusion or saving for this allowed
near-resonant model. Exact and near cancellation of the two curvatures
in (3.13) is likewise uncontrolled.

**Control 8 — false unsigned and arbitrary-coefficient analogues.**
Failed by any character-only proof. If \(F_q=(-1)^qc\) on an interval,
then the signed sum equals the positive sum \(Nc\), and the Gram form in
(3.9) has full capacity. Conversely, the unsigned analogue is saturated
by \(F_q=c\). Multiplication by \((-1)^q\) is unitary and exchanges
these examples. They need not be realizable actual symbols to prove the
precise point: no argument using only the sign, support, and
structure-free operator norms can yield the claimed gain. A valid proof
must use a new estimate specific to the complete actual coefficient,
namely (U96).

**Control 9 — block sum and target gain.** Failed. The trivial bound
for (3.9) returns the positive capacity
\(L^2X^\varepsilon\sqrt\rho\); it does not supply the required
\(\rho^{-1/2}\). A bounded-\(\rho\) collar would already be target-sized
by positive capacity and is not a newly closed hard range. No unbounded
hard subrange is closed, and therefore summing the blocks cannot prove
(96.11).

**Control 10 — new operator or self-return.** The outcome is adjoint
self-return. If \(P\) denotes formation of the \(q\)-slice \(F_q\),
then (3.9) is the quadratic form of
\(P^*M^*A_H^*A_HMP\), where \(M\) is unitary modulation by
\((-1)^q\) and \(A_H\) is shift averaging. Without (U96), its norm is
bounded only by the original \(P^*P\) Gram operator. Poisson merely
diagonalizes the shifts: it either translates \(q\)-slice frequencies
by \(1/2\), or, on an exact fixed-\(m\) fibre, returns the
\(\frac12\mathbb Z\) dual lattice displayed before (3.11). No new
determinant estimate has been proved.

## 6. Dependencies and exact artifacts used

The derivation uses only:

- rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/briefs/blind_primitive_ray_q_rederivation.md for the assignment and output contract;
- rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/derivation_packet.md, Sections 1–7, for every mathematical hypothesis and all prior-owner declarations.

No proof graph, strategy file, prior round, source card, web source,
sibling Round-96 artifact, conductor state, or numerical computation was
used.

## 7. Recommended state effect

**Recommended state effect: revise.** Promote the exact lattice,
character, endpoint factorization, complete autocorrelation
(3.6)–(3.9), and half-integral Poisson self-return as a rigorous no-go
diagnostic. Do not promote a \(\rho^{-1/2}\) estimate, a hard-subrange
closure, or (96.11). Any successor mechanism must add and prove a
complete-coefficient estimate of the form (U96), including fixed/short
\(q\), primitive-mask boundaries, moving entry/exit samples, and the
near-zero curvature locus (3.13). The canonical proof state should
otherwise remain unchanged.
