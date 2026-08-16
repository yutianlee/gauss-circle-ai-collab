# Round 78 hostile audit: square-ray resonance mass

## 1. Result

The square/common-squarefree parametrisation, its sign, and its open
reciprocal-mode interval survive the audit. More importantly, the separate
signed square contribution is target-sized:

\[
 \boxed{\mathcal S_L^\square(X)\ll_\varepsilon
 L^2X^\varepsilon.}                                      \tag{H78.1}
\]

The lawful mechanism is cancellation in \(k\) after the exact outer phase
has been recombined with the complete Round-77 centred integral. It is not
raywise absolute Abel summation. For one actual odd lift \(g\), put

\[
 I_{s,u}=\left(\frac{Ju}{s},\frac{2Ju}{t}\right),\qquad
 t=s+2u,\qquad K=\frac{Ju}{s},\qquad
 B_g(k)=\mathfrak B^\circ_{s^2,t^2,k}(g).
\]

The pointwise estimate suggested in the route,

\[
 k|\partial_kB_g(k)|\ll \sqrt{gt^2/K},                    \tag{H78.2}
\]

is false at a fixed physical collar: while the saddle traverses the
collar, \(k|B_g'(k)|\) can be \(L\) times the size of \(B_g\). The sharp
repair is the discrete total-\(k\)-variation estimate

\[
 \boxed{
 \sup_{k\in I_{s,u}}|B_g(k)|+
 \sum_{\substack{k,k+1\in I_{s,u}\\k\in\mathbb Z}}
 |B_g(k+1)-B_g(k)|
 \ll_\varepsilon X^\varepsilon\sqrt{gt^2/K}.}             \tag{H78.3}
\]

The complete smooth collar is essential in (H78.3). Its transition lasts
\(\asymp K/L\) reciprocal modes, but it has only one normalized traverse,
so its total variation, unlike its pointwise logarithmic derivative, has
the scale in (H78.3). Exact quadratic stationary phase, with all lower
terms retained, proves this assertion uniformly at both collar crossings.

With

\[
 f_g(k)=-\frac{gXu^2}{k},\qquad
 |f_g''(k)|\asymp \frac{L}{K},                             \tag{H78.4}
\]

van der Corput and partial summation give

\[
 \sum_{k\in I_{s,u}\cap\mathbb Z}B_g(k)e(f_g(k))
 \ll_\varepsilon X^\varepsilon(gst+1)
 \ll_\varepsilon LX^\varepsilon.                         \tag{H78.5}
\]

Finally,

\[
 \sum_{\substack{s<t<2s\\s,t\ \mathrm{odd}\\ (s,t)=1}}
 N_{s^2,t^2}\ll L\log(2L),                               \tag{H78.6}
\]

so (H78.1) follows without requiring cancellation between distinct square
rays.

In contrast, the stronger absolute Abel majorant is false, by a polynomial
margin:

\[
 \boxed{\mathcal M_L^\square(X)\not\ll_\varepsilon
 L^2X^\varepsilon.}                                      \tag{H78.7}
\]

**Supplemental hostile gate (certified).** Under the standard
positive-interior fixed-support hypothesis, the stronger uniform capacity
statement is

\[
 \boxed{\sqrt J\,L^{3/2}\ll \mathcal M_L^\square(X)
 \ll_\varepsilon \sqrt J\,L^{3/2}X^\varepsilon.}          \tag{H78.7a}
\]

The lower bound comes from a positive-density terminal \(g=1\) box, not
from a resonance hypothesis. The upper bound follows from
\(\min(N,\cdots)\le N\), the exact \(k\)-window width, and
\(N\ll G\asymp L/t^2\). Thus the majorant's natural absolute capacity is
larger than \(L^2\) by \(\sqrt{J/L}\), up to \(X^\varepsilon\).

Even without the terminal-box lower bound, any fixed active
\((s,t)=(9,11)\) block contributes \(\gg\sqrt{LJ}\); for a fixed
admissible \(L=L_0\), this is \(\gg X^{1/4}\). Hence (78.12) fails before
exact or metric resonances amplify the summands. Metric near-resonances
can themselves have this same fixed-ray capacity, so a divisor-only audit
is also invalid.

The perfect-fourth-power family is exactly coherent in the odd-lift
direction, but its one exact mode has only target-safe absolute capacity.
It is a sharp no-cancellation control, not a lower bound for the full
energy and not a counterexample to (H78.1).

## 2. Exact statement and hypotheses

Let \(e(z)=e^{2\pi iz}\), \(J=\sqrt X\), and
\(1\le L\le H\le J^{1/2}\). Use the accepted normalized top symbol, the
fixed smooth dyadic and \(W\)-profiles, the accepted \(C^1\) extension of
\(\Phi\), the exact \(q_X\), the fixed smooth physical collars, and the
actual finite odd lift support. All constants may depend on finitely many
fixed profile and collar seminorms.

Let \(s,t\) be coprime odd integers with \(s<t<2s\), write \(t=s+2u\),
and let \(g\in\mathcal G_{s^2,t^2}\). Thus the original ordered pair is

\[
 (h,r)=(gs^2,gt^2),\qquad gs^2\asymp gt^2\asymp L.        \tag{H78.8}
\]

For the open interval \(I_{s,u}\) above, retain the complete centred
integral \(B_g(k)\), including both exact \(W\)-profiles, all lower
stationary terms, the smooth collars, floors, and finite support. No
leading stationary value is substituted for \(B_g(k)\).

The assertion (H78.3) is a sampled \(k\)-BV theorem on
\(I_{s,u}\cap\mathbb Z\). It does not assert the false pointwise bound
(H78.2). If the interval contains zero or one integer, the corresponding
empty variation has its evident meaning. Equality at either endpoint of
\(I_{s,u}\) is not included; those modes remain in the accepted Round-77
error.

For the fixed-ray absolute-majorant obstruction, choose a fixed admissible
dyadic block on which at least one lift of the primitive ray
\((s,t)=(9,11)\) lies in the interior of the actual support. Such a block
is fixed independently of \(X\); then \(N_{81,121}\ge1\) and
\(G_{9,11}\asymp L\), with the fixed factor \(11^{-2}\) suppressed.

For the two-sided capacity (H78.7a), use the standard fixed-support
consequence that there are constants \(0<A<B\) and
\(0<c<d<1/2\), independent of \(L,X\), for which the box

\[
 A\sqrt L<s<B\sqrt L,\qquad cs<u<ds,\qquad t=s+2u        \tag{H78.8a}
\]

lies in the positive interior of both dyadic/support factors at the
terminal lift \(g=1\). Shrinking these constants if necessary keeps
\(s^2,t^2\) away from every support endpoint. Hence every coprime pair in
this box has \(1\in\mathcal G_{s^2,t^2}\), \(N_{s^2,t^2}\ge1\), and
\(G_{s,t}\asymp1\). This positive-interior hypothesis, rather than mere
support nonemptiness at one isolated point, is what licenses the lower
half of (H78.7a).

## 3. Proof or derivation

### Square algebra, sign, and one-count

If \((a,b)=1\), prime valuations give

\[
 ab=\square\quad\Longleftrightarrow\quad
 a=s^2,\quad b=t^2.
\]

Oddness gives \(t-s=2u\), and
\((s,t)=1\Longleftrightarrow(s,u)=1\). Direct calculation gives

\[
 \delta=2u,\qquad
 \frac{b-a}{4}=u(s+u)\in\mathbb Z,\qquad
 \Lambda=2Xu^2,                                          \tag{H78.9}
\]

and the strict saddle inequalities are exactly

\[
 \frac{Ju}{s}<k<\frac{2Ju}{t}.                            \tag{H78.10}
\]

Moreover, \((b-a)/2=2u(s+u)\) is even, so the offset sign is \(+1\).
If \(g=2n+1\), the outer and lift phases recombine without a missing
half-density:

\[
 e(-Xu^2/k)e(-2nXu^2/k)=e(-gXu^2/k).                     \tag{H78.11}
\]

There is one term for each actual odd lift \(g\), and the factor \(2\Re\)
counts the opposite orientation exactly once.

In original variables, two entries have a common squarefree kernel if and
only if they are \(dp^2,dq^2\). Dividing \(p,q\) by their gcd gives the
unique primitive square ray above, while the discarded common square and
\(d\) are carried by \(g\). Hence there is no second family and no gcd
multiplicity.

### The corrected total-\(k\)-variation lemma

For a square ray, the accepted exact factorisation from Round 77 can be
written, after \(v=z^2\), as

\[
 B_g(k)=C_g\int_{\mathbb R}F_g(z)
 e\!\left(gk\left(z-\frac{Ju}{k}\right)^2\right)dz,
 \qquad C_g=L^3g^{-2}P_{s,t}(g),                          \tag{H78.12}
\]

where \(F_g\) contains the complete \(Q\)-factor and both physical
collars, extended smoothly by zero. It is independent of \(k\). On
\(z\asymp t\), the fixed-profile bounds and the two physical collars give

\[
 |F_g(z)|\ll t^{-5},\qquad
 \|F_g'\|_1\ll t^{-5},\qquad
 \|F_g^{(r)}\|_1\ll_r t^{-5}(gt)^{r-1}\quad(r\ge1).        \tag{H78.13}
\]

The last bound includes the collar derivatives: a collar has \(z\)-width
\(\asymp(gt)^{-1}\), so its \(r\)-th derivative has size \((gt)^r\), but
its \(L^1\) cost loses one such factor. Interior profile derivatives are
smaller.

Put \(\lambda=gk\) and \(z_0=Ju/k\). The exact quadratic stationary
expansion of (H78.12), applied to the smooth zero extension, is uniform as
\(z_0\) enters and leaves either collar:

\[
 \int F_g(z)e(\lambda(z-z_0)^2)dz
 =\sum_{0\le j<R}c_j\lambda^{-j-1/2}F_g^{(2j)}(z_0)
 +\mathcal R_R.                                          \tag{H78.14}
\]

Taylor's formula at \(z_0\), followed by two integrations by parts on each
remainder stage, proves (H78.14). Applying the same argument after one
\(z_0\)- or \(\lambda\)-derivative gives its parameter variation. By
(H78.13), the variation of the \(j\)-th coefficient as \(z_0\) traverses
the support is bounded by its derivative \(L^1\)-norm. Relative to the
leading term, every collar correction costs

\[
 \frac{(gt)^{2j}}{(gK)^j}
 =\left(\frac{gt^2}{K}\right)^j
 \asymp\left(\frac{L}{K}\right)^j.                        \tag{H78.15}
\]

An active square ray has \(t^2\ll L\), \(u\ge1\), and therefore

\[
 \frac{K}{L}=\frac{Ju}{sL}
 \gg\frac{J}{L^{3/2}}\ge J^{1/4}.                         \tag{H78.16}
\]

Thus (H78.14) and its differentiated remainder are summable with a fixed
\(R\). Variation of \(\lambda^{-j-1/2}\) over the constant-ratio
\(k\)-interval has the size of the factor itself, and \(z_0(k)\) is
monotone. Consequently,

\[
 \operatorname {BV}_{k\in I_{s,u}} B_g(k)
 \ll C_g t^{-5}(gK)^{-1/2}
 \asymp t\sqrt{g/K},                                      \tag{H78.17}
\]

because \(gt^2\asymp L\). This proves (H78.3), with any harmless fixed
logarithm absorbed by \(X^\varepsilon\).

This proof also exposes why (H78.2) is false. If
\(x_*(k)=g(Ju/k)^2\) crosses a collar edge \(x_e\), the leading term
contains

\[
 \sqrt{L/K}\,
 \rho\!\left(\frac{x_*(k)-x_e}{M}\right),\qquad
 \frac{dx_*}{dk}\asymp-\frac{L}{K}.                       \tag{H78.18}
\]

Where \(\rho'\ne0\), this has
\(k|B_g'(k)|\asymp L\sqrt{L/K}\). The crossing interval has length
\(\asymp K/L\), however, so its total variation is only
\(O(\sqrt{L/K})\). Deleting all these modes absolutely would cost
\(\asymp\sqrt{K/L}\) per lift and is not target-safe for small \(L\).

### Reciprocal-mode cancellation

For \(f_g(k)=-gXu^2/k\), strict saddle inclusion gives

\[
 |f_g''(k)|=\frac{2gXu^2}{k^3}
 =\frac{2x_*(k)}{k}\asymp\frac{L}{K}.                     \tag{H78.19}
\]

The second-derivative estimate, uniformly on every subinterval, is

\[
 \left|\sum_{k\in I'}e(f_g(k))\right|
 \ll |I'|\sqrt{L/K}+\sqrt{K/L}.                           \tag{H78.20}
\]

Partial summation with (H78.3) yields

\[
\begin{aligned}
 \left|\sum_{k\in I_{s,u}}B_g(k)e(f_g(k))\right|
 &\ll t\sqrt{g/K}
 \left(K\sqrt{\frac{gJ^2u^2}{K^3}}
       +\sqrt{\frac{K^3}{gJ^2u^2}}\right)\\
 &\ll gst+\frac ts\ll L+1,                               \tag{H78.21}
\end{aligned}
\]

where \(K=Ju/s\) and \(gst\le gt^2\asymp L\). If the open \(k\)-interval
is narrow or contains one point, the same formula, or the trivial bound,
is no larger. Small \(u\) only increases \(K/L\) relative to the safe
lower bound (H78.16).

For the lift count, \(t^2\ll L\) and
\(N_{s^2,t^2}\ll L/t^2\). Hence

\[
 \sum_{s,t}N_{s^2,t^2}
 \ll L\sum_{t\ll\sqrt L}\frac1{t^2}\#\{s:s<t\}
 \ll L\sum_{t\ll\sqrt L}\frac1t
 \ll L\log(2L),                                          \tag{H78.22}
\]

which with (H78.11) and (H78.21) proves (H78.1).

### Absolute Abel capacity and metric resonances

For \(N\ge1\), one always has

\[
 \min\!\left(N,\frac1{2\|\theta\|}\right)\ge1,            \tag{H78.23}
\]

including the convention at exact resonance. On the fixed primitive ray
\((s,t,u)=(9,11,1)\), the open \(k\)-interval has \(\asymp J\) integers.
Thus any fixed active lift block gives

\[
 \mathcal M_L^\square(X)
 \ge 2J\sqrt{G_{9,11}}
 \sum_{J/9<k<2J/11}k^{-3/2}
 \gg\sqrt{LJ}.                                            \tag{H78.24}
\]

Taking an admissible fixed \(L=L_0\) and any \(\varepsilon<1/4\)
contradicts (78.12). This lower bound uses no resonance at all.

### Supplemental hostile gate: full absolute capacity

The terminal \(g=1\) box (H78.8a) upgrades the fixed-ray obstruction to
the lower half of (H78.7a). First, it contains \(\gg L\) admissible
primitive pairs. Indeed \(s\) is odd, \(t=s+2u\) is then automatically
odd, and

\[
 (s,t)=1\quad\Longleftrightarrow\quad(s,u)=1.
\]

Möbius inversion in the planar box gives

\[
\begin{aligned}
 \#\{(s,u)\text{ in (H78.8a)}:s\ {\rm odd},(s,u)=1\}
 &=c_0L\sum_{\substack{q\ge1\\q\ {\rm odd}}}
   \frac{\mu(q)}{q^2}+O(\sqrt L\log(2L))\\
 &\gg L,                                                  \tag{H78.24a}
\end{aligned}
\]

where \(c_0>0\) is the area constant of the fixed box and the odd Euler
product is positive. Thus parity and coprimality do not remove a power of
\(L\).

For every pair in this box, \(s,u,t\asymp\sqrt L\), and the exact open
\(k\)-window has width

\[
\begin{aligned}
 \Delta K
 &=\frac{2Ju}{t}-\frac{Ju}{s}
 =\frac{Ju(s-2u)}{s(s+2u)}
 \asymp J,\\
 k&\asymp J.                                             \tag{H78.24b}
\end{aligned}
\]

It therefore contains \(\asymp J\) integers. Since \(G\asymp1\),
\(N\ge1\), and the Abel factor is at least one, one terminal primitive
pair contributes

\[
 J\cdot\frac{Ju\sqrt G}{J^{3/2}}
 \asymp\sqrt{JL}.                                         \tag{H78.24c}
\]

Combining (H78.24a)--(H78.24c) proves
\(\mathcal M_L^\square(X)\gg\sqrt J\,L^{3/2}\), uniformly in
the arithmetic nature of \(X\).

For the upper half, an active ray has \(t\ll\sqrt L\),
\(G\ll L/t^2\), and \(N\ll G\). Put \(K=Ju/s\). The exact window obeys
\(\Delta K\le K\), and

\[
 \sum_{k\in I_{s,u}\cap\mathbb Z}k^{-3/2}
 \ll (\Delta K+1)K^{-3/2}.                               \tag{H78.24d}
\]

Using \(\min(N,\cdots)\le N\), \(t=s+2u\asymp s\), and first the
\(\Delta K\)-part of (H78.24d), one obtains

\[
\begin{aligned}
 \mathcal M_{L,\mathrm{main}}^\square
 &\ll
 \sqrt J\,L^{3/2}
 \sum_{s\ll\sqrt L}\sum_{1\le u<s/2}
 \frac{\sqrt{us}}{(s+2u)^3}\\
 &\ll
 \sqrt J\,L^{3/2}\sum_{s\ll\sqrt L}\frac1s
 \ll \sqrt J\,L^{3/2}\log(2L).                           \tag{H78.24e}
\end{aligned}
\]

The \(+1\) in (H78.24d), which is essential for a narrow or singleton
integer window, contributes only

\[
\begin{aligned}
 \mathcal M_{L,\mathrm{short}}^\square
 &\ll
 \frac{L^{3/2}}{\sqrt J}
 \sum_{s\ll\sqrt L}\sum_{1\le u<s/2}
 \frac{s^{3/2}}{(s+2u)^3\sqrt u}\\
 &\ll \frac{L^{3/2}}{\sqrt J}\log(2L).                    \tag{H78.24f}
\end{aligned}
\]

Coprimality and oddness only decrease these upper sums. Since
\(\log(2L)\ll_\varepsilon X^\varepsilon\), (H78.24e)--(H78.24f) prove
the upper half of (H78.7a). The terminal \(g=1\) family supplies the
correct lower order, while the complete upper sum shows that neither
small \(u\), terminal \(G\asymp1\), nor narrow \(k\)-windows hide an
additional power.

Exact divisors do not repair the route. When \(2Xu^2\) is integral, exact
resonances are the divisors \(k\mid2Xu^2\) lying strictly in (H78.10), so
there are only \(X^\varepsilon\) per ray; endpoint-equality divisors are
not owned by this sum. For general real \(X\), however, metric resonances
occur at the actual width \(N^{-1}\). To see their capacity without an
equidistribution assumption, average \(X\) over a short fixed-proportion
interval \([Y,(1+\eta)Y]\) and restrict \(k\) to a fixed subinterval of
(H78.10) for every such \(X\). For each \(k\asymp\sqrt Y\),

\[
 \left\|\frac{2X}{k}\right\|\le\frac1{4N}                 \tag{H78.25}
\]

occupies a proportion \(\asymp N^{-1}\) of the \(X\)-interval, up to an
\(O(k/Y)\) endpoint error. Summing incidences shows that some real \(X\)
has \(\gg K/N\) such \(k\)'s. Each has Abel factor \(N\), so these metric
modes alone contribute

\[
 \gg \frac KN\,N\sqrt{L/K}\asymp\sqrt{LJ}                 \tag{H78.26}
\]

on the fixed ray. Counting exact divisors while omitting (H78.25) is
therefore decisively insufficient.

### Fourth powers and self-return

Let \(X=T^4\), with \(T\) odd and \(13\mid T\), and take
\((s,t,u)=(9,11,1)\), \(k_0=2T^2/13\). Then \(k_0\) is strictly inside
(H78.10),

\[
 \frac{2Xu^2}{k_0}=13T^2\in\mathbb Z,\qquad
 e(-gXu^2/k_0)=-1\quad(g\ \mathrm{odd}),                  \tag{H78.27}
\]

and the saddle is \(169/4\), with the two \(W\)-arguments \(9/13\) and
\(11/13\). Thus there is no invented in-lift cancellation. Nevertheless,
the one exact Abel term has capacity

\[
 N_{81,121}\frac{2J\sqrt G}{k_0^{3/2}}
 \ll\frac{L^{3/2}}{\sqrt J},                              \tag{H78.28}
\]

which is target-safe. Coherence supplies neither a lower bound for the
complete signed square contribution nor for the full energy.

Finally, multiplying the complete centred integral by its outer phase and
transforming the reciprocal variable back reconstructs the original
finite \(m\)-sum. That operation is the known rank-one self-return. The
proof above uses one second-derivative estimate in \(k\); it does not
count the inverse transform as a second saving.

## 4. First doubtful or unproved step

The first false step in the proposed closure is the pointwise
\(k\partial_k\) claim (H78.2). The formal identity

\[
 k\partial_k e\!\left(gk(z-Ju/k)^2\right)
 =\frac{z+Ju/k}{2}\,\partial_z
 e\!\left(gk(z-Ju/k)^2\right)                             \tag{H78.29}
\]

is exact, but after integration by parts the derivative can hit a fixed
physical collar. Equation (H78.18) then gives the missing factor \(L\).
Thus a proof that takes a pointwise \(k\)-derivative supremum, or removes
all \(O(K/L)\) transition modes absolutely, fails.

The corrected statement is total variation (H78.3), proved from the smooth
zero-extended complete integral and the exact quadratic expansion. It
must not be transferred to a sharp incomplete-Fresnel cutoff or to
arbitrary \(k\)-coefficients. After this repair, the first unproved step
is outside the square family: no argument here controls nonsquare or
near-square primitive rays, the full reciprocal resonance union, or the
full transposed energy.

For the supplemental absolute-capacity gate, the only indispensable
support seam is (H78.8a). If the fixed profiles did not contain a
positive-interior terminal \(g=1\) box, the lower conclusion would revert
to the fixed-ray no-go (H78.24). Under the stated fixed-support
hypothesis, the Möbius count and both parts of the upper sum are complete;
no exact- or metric-resonance assumption enters the two-sided capacity.

## 5. Required control test and outcome

| Required control | Outcome |
|---|---|
| External normalization and \(2\Re\) | **Pass.** The proof starts on the normalized Round-77 scale. Equation (H78.11) combines phases once, and \(2\Re\) only restores the opposite orientation. No physical top-transform or Gaussian factor is inserted again. |
| Square/common-kernel equivalence | **Pass.** Coprimality forces \(a=s^2,b=t^2\); the squarefree kernel and any common root are uniquely in the odd lift \(g\). |
| Primitive parity and sign | **Pass.** \(t=s+2u\), \((s,u)=1\), and \((b-a)/2=2u(s+u)\), so the ray sign is \(+1\). |
| Exact \(k\)-interval | **Pass.** The raw saddle gives the strict interval (H78.10). Equality modes remain in the accepted error and are not double-counted. |
| Complete actual symbol | **Pass.** The \(k\)-BV proof uses the smooth zero extension of the complete centred integral, exact \(q_X,W\), and all collar/stationary corrections; no leading-value replacement is made. |
| Smooth collar versus pointwise derivative | **Corrected.** Pointwise (H78.2) fails by a factor \(L\). Total \(k\)-variation (H78.3) survives because each smooth collar is traversed once. Absolute deletion of its \(O(K/L)\) modes is unsafe. |
| Small \(u\), narrow \(k\)-range, one-point lift | **Pass.** The lower bound (H78.16) is strongest at \(u=1\). A short or singleton \(k\)-interval is covered by (H78.20) or trivially. The proof works lift by lift and never assumes \(N\gg1\). |
| Stars, finite support, and \(\Phi\)-edge | **Pass.** Stars and raw endpoint equalities are owned by the Round-77 error. The actual finite \(g\)-support is counted by \(N\). The factor \(\Phi\) is constant in the \(k\)-analysis, so its terminal edge introduces no \(k\)-variation loss. |
| Exact versus metric resonance | **Pass with a no-go for divisor-only counting.** Exact modes obey divisor ownership when \(2Xu^2\) is integral, but the averaging argument (H78.25)--(H78.26) produces the full metric \(N^{-1}\) population for suitable real \(X\). The signed second-derivative estimate handles both uniformly. |
| Absolute majorant versus signed sum | **Decisive separation; supplemental gate certified.** The signed sum satisfies (H78.1). The terminal \(g=1\) box, coprime-pair count, exact \(k\)-width, and complete upper sum prove \(\mathcal M_L^\square\asymp_{X^\varepsilon}\sqrt J\,L^{3/2}\), equations (H78.24a)--(H78.24f). |
| Fourth-power coherence | **Pass as a hostile control.** Equation (H78.27) is strictly interior and has both \(W\)-weights equal to one. Its exact-mode mass (H78.28) is target-safe and is not a full-energy lower bound. |
| Coefficient adversary | **False analogue rejected.** A \(k\)-phase-conjugating multiplier preserves pointwise size but destroys (H78.3) and makes the absolute \(k\)-mass visible. The theorem depends on the actual complete centred coefficient. |
| Rank-one self-return | **Pass as a stopping control.** Reciprocal inversion returns the original finite block. Only the direct \(k\)-curvature estimate is used. |
| Near-square/nonsquare and downstream scope | **Pass.** The sparse count (H78.22) is special to exact square rays. No enlargement to near-square nonsquare rays, full energy, signed cone, \(M9\!-\!M2\), \(M9\), endpoint uniformity, or the exponent is claimed. |

No numerical computation and no external theorem were used.

## 6. Dependencies and exact artifacts used

Campaign: m9-m2-top-endpoint-square-resonance-mass. Task:
square_resonance_hostile_audit. Role: hostile seam reviewer. Starting graph
SHA-256: 5afbe1bb7b5c5d943be9438ba02bd9ede1ab6735344174b33b4a99c7de7f9123.

The mathematical derivation used exactly the selected campaign context:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/derivation_packet.md;
- rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/briefs/square_resonance_hostile_audit.md;
- rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reports/actual_symbol_hostile_audit.md;
- rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/reports/signed_offset_hostile_audit.md.

No sibling Round-78 report, source card, proof draft, validation matrix, web
source, or numerical artifact was used.

## 7. Recommended state effect

**Promote the corrected separate square-family theorem after the required
independent rederivation, and promote the sharp absolute-majorant capacity
as a route no-go.**

The promotable kernel is (H78.1), with the total-\(k\)-variation lemma
(H78.3), the reciprocal second-derivative bound (H78.19)--(H78.21), and
the sparse lift count (H78.22) recorded as its proof. The theorem is about
the complete actual square contribution and must retain the smooth
physical collars and exact \(k\)-phase.

Record the following no-go statements:

1. a pointwise bound \(k|B_g'(k)|\ll\sqrt{gt^2/K}\) through a physical
   collar;
2. absolute deletion of all \(O(K/L)\) collar-transition modes;
3. the target-sized absolute Abel assertion (78.12);
4. any exact-divisor-only treatment of the reciprocal resonance set; and
5. any coefficient-blind or repeated-transform proof of (H78.1).

The absolute route theorem should record the certified two-sided scale

\[
 \mathcal M_L^\square(X)
 \asymp_{X^\varepsilon}\sqrt J\,L^{3/2},
\]

under the positive-interior fixed-support hypothesis in (H78.8a). Its
lower proof is the terminal \(g=1\) primitive-pair box; its upper proof
must retain both the \(\Delta K\) and \(+1\) terms of (H78.24d). This
sharpens, and does not weaken, the rejection of (78.12).

Retain the fourth-power family as a permanent exact-coherence control, but
do not record it as a lower bound for the complete square sum or full
energy. Keep the generic resonance union, transposed energy, signed top
cone, \(M9\!-\!M2\), \(M9\), endpoint uniformity, and the Gauss-circle
exponent open.
