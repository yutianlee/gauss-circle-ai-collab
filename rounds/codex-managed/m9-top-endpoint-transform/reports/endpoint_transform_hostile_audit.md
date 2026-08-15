# Hostile audit of the one-sided top-endpoint transform

- Campaign: m9-top-endpoint-transform
- Round: 8
- Task: endpoint_transform_hostile_audit
- Role: hostile falsifier
- Graph SHA-256 supplied in the brief: 7b5a7c93190fa88305d91bb1f2e64788921fe2f4cbbd02eddb8e60e654d64d58
- Isolation: no other Round-8 task report was read.
- Status: candidate evidence only; no shared state or synthesis was edited.

## 1. Result and verdict

The feared endpoint stationary transition does **not** occur. Put

\[
y=\lfloor\sqrt X\rfloor,\qquad
T=X-y^2,\qquad
H=\lfloor yX^{-1/4}\rfloor .
\]

For all sufficiently large \(X\), the exact minimum over the surviving
positive odd frequencies is

\[
\boxed{
\min_{\substack{1\le h\le H\\ h\ {\rm odd}}}
\operatorname {dist}\!\left(\frac{hX}{4y^2},\mathbb Z\right)
=\frac14-\frac{h_*T}{4y^2},}
\tag{1.1}
\]

where \(h_*\) is the largest integer \(h\le H\) with
\(h\equiv3\pmod4\). In particular,

\[
\operatorname {dist}\!\left(\frac{hX}{4y^2},\mathbb Z\right)
\ge \frac14-\frac1{2\sqrt y}-\frac1{4y^{3/2}}
=\frac14+O(y^{-1/2})
\tag{1.2}
\]

uniformly for \(y^2\le X<(y+1)^2\). The value is not identically \(1/4\):
the negative \(O(y^{-1/2})\) correction is real and is attained in order
of magnitude by the highest admissible \(3\pmod4\) frequency.

The closest stationary point is at distance \(\gg y/h\) from \(d=y\),
whereas its natural stationary width is \(\asymp\sqrt{y/h}\). Their ratio
is \(\gg\sqrt{y/h}\ge y^{1/4}\). Thus a half-Fresnel transition at the top
endpoint is uniformly excluded throughout the active height range.

There is nevertheless a material normalization trap. Poisson summation
for the included integer endpoint has an explicit extra half-weight. Its
Fourier integrals also have a conditionally convergent endpoint series.
Together their principal endpoint coefficient is

\[
\boxed{
E_h(X)=
\frac{e(hX/(4y))}{1-e(hX/(4y^2))}.}
\tag{1.3}
\]

The denominator is uniformly separated from zero by (1.2). With the
actual beta weights, the positive-frequency sum of (1.3) is
\(O(\log(2H))\), and this logarithm is sharp. The actual two-sided
real-even M2 endpoint contribution is instead \(O(1)\): the negative
frequency is the complex conjugate and the logarithmic part is purely
imaginary. On one dyadic frequency block \(h\asymp L\), even the
positive-frequency endpoint is \(O(1)\) absolutely.

Hence the endpoint term is target-sized, but a positive-frequency
one-sided formula may not hide it in a uniform \(O(1)\) error over the
full height. Exact Poisson renormalization and stationary separation
survive; the top M2 bound does not follow. The first genuinely unproved
step remains the signed estimate for the transformed stationary bulk, or
an equivalent direct estimate.

## 2. Exact minimum at the endpoint derivative

Put

\[
\eta=\frac{T}{4y^2},\qquad
0\le\eta<\frac{2y+1}{4y^2}.
\]

Then

\[
q_h:=\frac{hX}{4y^2}=\frac h4+h\eta.
\tag{2.1}
\]

Since \(H\le\sqrt y\), for sufficiently large \(y\),

\[
0\le h\eta<
\frac{\sqrt y(2y+1)}{4y^2}<\frac14
\tag{2.2}
\]

for every \(h\le H\). Therefore, for odd \(h\),

\[
\operatorname {dist}(q_h,\mathbb Z)=
\begin{cases}
\frac14+h\eta,&h\equiv1\pmod4,\\[2mm]
\frac14-h\eta,&h\equiv3\pmod4.
\end{cases}
\tag{2.3}
\]

The first line is minimized at \(h=1\), while the second is minimized at
the largest admissible \(3\pmod4\) integer. This proves (1.1), including
the tie at \(T=0\). Explicitly,

\[
h_*=4\left\lfloor\frac{H-3}{4}\right\rfloor+3.
\]

For completeness, if the small-\(X\) range has \(H<3\), the only
surviving odd frequency is \(h=1\), and the minimum is \(1/4+\eta\) as
long as (2.2) holds. The campaign is asymptotic, and \(H\ge3\) for all
sufficiently large \(X\).

Using \(h_*\le H\le\sqrt y\) and \(T<2y+1\) gives (1.2).

### Sharp control against the false constant \(1/4\)

Let \(m\equiv3\pmod4\), put \(y=m(m+1)\), and let
\(X\uparrow(y+1)^2\). Throughout this square interval,

\[
m<\frac{y}{\sqrt{y+1}}\le yX^{-1/4}\le\sqrt y<m+1,
\]

so \(H=m\) and \(h_*=m\). Consequently the infimum in this interval tends
to

\[
\frac14-\frac{m(2y+1)}{4y^2}
=\frac14-\frac1{2(m+1)}+O(m^{-3}).
\tag{2.4}
\]

Thus an asserted exact lower bound \(\ge1/4\) is false, although every
fixed lower bound \(1/4-o(1)\), and for example \(1/8\) for large \(y\),
is valid.

## 3. Stationary points cannot enter the endpoint width

For fixed \(h>0\), write \(A_h=hX/4\). In the Poisson integral with index
\(k=-m<0\), the phase is

\[
F_{h,m}(d)=\frac{A_h}{d}+md.
\]

Its critical point is

\[
d_m=\sqrt{\frac{A_h}{m}}=y\sqrt{\frac{q_h}{m}}.
\tag{3.1}
\]

It lies in the one-sided range \(d\le y\) exactly when \(m\ge q_h\).
Since \(q_h\notin\mathbb Z\), the closest such point corresponds to
\(m_0=\lceil q_h\rceil\). From (1.2),

\[
m_0-q_h\ge\operatorname {dist}(q_h,\mathbb Z)\gg1.
\tag{3.2}
\]

The exact endpoint gap is

\[
y-d_{m_0}
=\frac{y(m_0-q_h)}
{\sqrt{m_0}(\sqrt{m_0}+\sqrt{q_h})}
\gg\frac yh.
\tag{3.3}
\]

At the critical point,

\[
F''_{h,m_0}(d_{m_0})=\frac{2m_0}{d_{m_0}},
\]

so the natural quadratic width, up to an absolute \(2\pi\)
normalization, is

\[
\sigma_{h,m_0}\asymp\sqrt{\frac{d_{m_0}}{m_0}}
\asymp\sqrt{\frac yh}.
\tag{3.4}
\]

Equations (3.3)--(3.4) give

\[
\frac{y-d_{m_0}}{\sigma_{h,m_0}}
\gg\sqrt{\frac yh}\ge y^{1/4}.
\tag{3.5}
\]

For \(h=1\), the only positive stationary index is \(m=1\), and the point
is near \(y/2\), even farther from the endpoint. Thus neither the lowest
nor the highest surviving odd frequency creates an endpoint stationary
transition.

## 4. Correct one-sided Poisson normalization

Let \(W\) be the accepted top profile, so \(W(1)=1\), and set

\[
f_h(x)=W(x/y)e(A_h/x).
\]

The support stays away from \(x=0\). Define

\[
I_{h,k}=\int_0^y W(x/y)e(A_h/x-kx)\,dx.
\]

Poisson summation applied to the discontinuous extension
\(f_h(x){\bf1}_{x\le y}\) uses the midpoint value at the integer jump.
Since the project sum includes \(d=y\) with full weight, the exact
identity is

\[
\boxed{
\sum_{d\le y}W(d/y)e(A_h/d)
=\frac12e(A_h/y)+
\operatorname {PV}\sum_{k\in\mathbb Z}I_{h,k}.}
\tag{4.1}
\]

Thus the half-weight has a **plus** sign. Omitting it computes the sum
with half the endpoint value, not the project sum.

At the upper endpoint the phase derivative in \(I_{h,k}\) is
\(-q_h-k\). One integration by parts for large \(\lvert k\rvert\) gives

\[
I_{h,k}
=-\frac{e(A_h/y)}{2\pi i(k+q_h)}+O_{h,y}(k^{-2}).
\tag{4.2}
\]

Hence the Fourier-integral series is not absolutely convergent term by
term. It is the symmetric principal-value series

\[
\operatorname {PV}\sum_{k\in\mathbb Z}\frac1{k+q_h}
=\pi\cot(\pi q_h).
\tag{4.3}
\]

Equivalently, (4.1) has the exact renormalized form

\[
\sum_{d\le y}W(d/y)e(A_h/d)
=E_h(X)+
\sum_{k\in\mathbb Z}
\left(
 I_{h,k}+\frac{e(A_h/y)}{2\pi i(k+q_h)}
\right),
\tag{4.4}
\]

where the last series is absolutely convergent for fixed \(h,X\), with
the finitely many stationary indices retained inside it, and

\[
\begin{aligned}
E_h(X)
&=e(A_h/y)
\left(\frac12-\frac{\cot(\pi q_h)}{2i}\right)\\
&=\frac{e(hX/(4y))}{1-e(hX/(4y^2))}.
\end{aligned}
\tag{4.5}
\]

The apparent singularity in (4.5) is harmless precisely because of the
odd-frequency separation (1.2). Formula (4.4), rather than a separately
summed collection of \(1/k\) tails, is the safe normalization for a
one-sided stationary-phase expansion. Stationary phase may then be
applied to the finitely many \(k=-m\) terms with \(m>q_h\); (3.5) shows
that no endpoint Fresnel factor is needed.

## 5. Size after the actual beta weights

The accepted coefficients are

\[
\beta_{h,H}
=-\frac{\Phi(|h|/(H+1))\chi_4(h)}{\pi|h|}
\quad(h\ {\rm odd}),\qquad
\beta_{-h,H}=\beta_{h,H}\in\mathbb R.
\tag{5.1}
\]

By (1.2), \(|E_h(X)|\ll1\). Therefore

\[
\sum_{\substack{1\le h\le H\\h\ {\rm odd}}}
|\beta_{h,H}E_h(X)|\ll\log(2H),
\tag{5.2}
\]

and the same sum restricted to one dyadic block \(h\asymp L\) is
\(O(1)\).

The logarithm in the positive-frequency whole-height sum is sharp. Take
\(y=4n^2\) and \(X=y^2\). Then \(H=\sqrt y=2n\),
\(X/(4y)=y/4\in\mathbb Z\), and for odd \(h\),

\[
E_h(X)=\frac1{1-e(h/4)}
=\frac{1+i\chi_4(h)}2.
\]

Consequently,

\[
\begin{aligned}
\sum_{\substack{1\le h\le H\\h\ {\rm odd}}}
\beta_{h,H}E_h(X)
&=-\frac{i}{2\pi}
\sum_{\substack{1\le h\le H\\h\ {\rm odd}}}
\frac{\Phi(h/(H+1))}{h}+O(1)\\
&=-\frac{i}{4\pi}\log H+O(1).
\end{aligned}
\tag{5.3}
\]

Thus a positive-frequency endpoint remainder asserted to be \(O(1)\)
over the entire height is false. This is an exact-square countermodel
using the actual Vaaler amplitudes, not adversarial weights.

For the actual two-sided block, however,

\[
\mathcal E_{\rm full}
=2\operatorname {Re}
\sum_{\substack{1\le h\le H\\h\ {\rm odd}}}
\beta_{h,H}E_h(X).
\tag{5.4}
\]

Write

\[
b=\frac{X}{4y^2}=\frac14+\eta,\qquad
a=\frac{X}{4y}=yb.
\]

For \(h\le H\le\sqrt y\), (2.2) and (1.2) give uniformly

\[
\frac1{1-e(hb)}
=\frac1{1-e(h/4)}+O(h/y)
=\frac{1+i\chi_4(h)}2+O(h/y).
\tag{5.5}
\]

Inserting (5.5) into (5.4), the main summand is

\[
\frac{\Phi(h/(H+1))}{\pi h}
\left(
\sin(2\pi ha)-\chi_4(h)\cos(2\pi ha)
\right).
\tag{5.6}
\]

Both harmonic sums in (5.6) are uniformly bounded in \(a\) and \(H\).
Indeed the first is an odd subseries of the uniformly bounded sine
harmonic sum, while

\[
\chi_4(h)\cos(2\pi ha)
=\frac12\left(
\sin(2\pi h(a+1/4))+
\sin(2\pi h(1/4-a))
\right).
\]

Abel summation retains the bound after inserting the fixed-BV Vaaler
factor \(\Phi(h/(H+1))\). The total error from (5.5) is

\[
\ll\sum_{h\le H}\frac1h\frac h y
\ll H/y\ll y^{-1/2}.
\]

Therefore

\[
\boxed{\mathcal E_{\rm full}=O(1)}
\tag{5.7}
\]

uniformly over the complete square interval. The distinction is
essential: \(O(\log H)\) is sharp for the positive half, while \(O(1)\)
is correct for the actual real-even two-sided endpoint.

## 6. First false or doubtful step

The first false shortcut is to use the smooth full-line Poisson formula
on the top profile without (4.1). Already \(h=1\), \(X=y^2\) gives

\[
|E_1(X)|=|1-e(1/4)|^{-1}=2^{-1/2},
\]

so the missing endpoint is not \(o(1)\). The second false shortcut is to
claim the derivative threshold is exactly \(1/4\); (2.4) disproves that
constant. The third is to call the positive whole-height endpoint
\(O(1)\); (5.3) gives an actual-coefficient logarithmic counterexample.

After inserting the half-weight, summing the boundary series in symmetric
principal value, and keeping positive and negative frequencies distinct,
the first genuinely unproved analytic step is a uniform stationary-phase
remainder and signed estimate for the stationary bulk strong enough to
bound the full top M2 block. Endpoint separation alone gives no such
signed cone estimate. In particular, it does not improve the accepted
smooth dual three-quarter target; it only removes a potential Fresnel
seam.

## 7. Required controls and outcomes

1. **Exact minimum:** pass with correction. Formula (1.1) is exact; the
   simpler constant \(1/4\) fails on (2.4).
2. **Lowest frequency:** pass as a hostile control. At \(h=1,X=y^2\), the
   endpoint coefficient has constant size, so a boundary-free smooth
   transform fails.
3. **Highest frequency:** pass. The family \(y=m(m+1)\),
   \(h=m\equiv3\pmod4\), realizes the \(y^{-1/2}\) loss in the derivative
   separation.
4. **Natural stationary width:** pass. The endpoint gap exceeds the width
   by \(\gg y^{1/4}\), uniformly even at \(h\asymp H\).
5. **Poisson endpoint convention:** pass. The included endpoint contributes
   \(+\tfrac12f_h(y)\), and the \(1/(k+q_h)\) series must be interpreted in
   symmetric principal value.
6. **Actual beta weights:** pass only after splitting scopes. Positive
   frequencies give sharp \(O(\log H)\); one dyadic block gives \(O(1)\);
   the actual two-sided real-even block gives \(O(1)\).
7. **Proves-too-much:** pass after correction. The boundary analysis uses
   odd support, \(\chi_4\), real-even beta coefficients, and the exact top
   phase. It does not assert an arbitrary-coefficient or unsigned bound.
8. **Computation:** none used. All controls are exact analytical families.

## 8. Dependencies and exact artifacts used

- protocol.md
- state/proof_obligations.yml
- state/active_campaign.yml
- rounds/codex-managed/m9-top-endpoint-transform/briefs/endpoint_transform_hostile_audit.md
- rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md
- rounds/codex-managed/m9-endpoint-kernel-validation/reports/hostile_endpoint_scope_review.md
- rounds/codex-managed/m9-frequency-phase-diagram/reports/dual_three_quarter_attack.md

No external theorem, numerical artifact, other Round-8 report, proof draft,
validation matrix, or synthesis file was used.

## 9. Recommended state effect

1. **Retain M9-M2-top-endpoint-transform as open.** The endpoint
   stationary-threshold seam is benign, but no signed estimate for the
   transformed bulk has been proved.
2. **Promote or retain as exact infrastructure after seam review:** (1.1),
   the stationary-width exclusion (3.5), and the one-sided Poisson
   normalization (4.1)--(4.5).
3. **Record a scope correction:** the principal endpoint term is \(O(1)\)
   for the actual two-sided block, \(O(1)\) on each dyadic positive block,
   but only sharp \(O(\log H)\) for the positive whole-height sum.
4. **Reject** any top-transform statement that omits the half endpoint,
   sums the \(1/k\) boundary tails non-symmetrically, claims exact
   \(1/4\) threshold separation, or absorbs the positive whole-height
   endpoint into \(O(1)\).
5. **No change** to M9-endpoint-uniformity, M9-M2, M9, or the target.
