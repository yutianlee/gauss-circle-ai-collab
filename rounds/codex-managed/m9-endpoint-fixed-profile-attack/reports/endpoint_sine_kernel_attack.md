# Direct endpoint attack on the fixed-profile sine kernel

## 1. Result

**Verdict: no new signed endpoint range is proved.**  Fixed-profile smoothness
does not improve the product-annulus estimate after either residue separation
or absolute values.  For every fixed nonzero smooth profile, each one-sided
first annulus in either congruence class has average and occasional size
\(\gg D/L\) at \(D\asymp X^{1/2}\).  Thus a successful bound for the full
two-sided block must use signed cancellation within or between residue
classes, sides of the product centers, or annuli before taking absolute
values.  Mere residue separation supplies no saving.

The perfect-square model is also non-uniform.  At \(X=4N^2\), the reciprocal
phase near \(d=N\) is exactly quadratic modulo integers.  Changing \(X\) by
only \(\asymp N\) moves the same fixed-profile local window from a
character-alternating point to the first sine annulus.  The local contribution
changes from

\[
 O\!\left(N^{1/2}L^{-3/2}\right)
 \quad\hbox{to}\quad
 \asymp N^{1/2}L^{-1/2}.                                \tag{1.1}
\]

The latter is \(X^{1/4}L^{-1/2}\), so it does not disprove the desired
\(X^{1/4+\varepsilon}\) estimate.  It does prove that the exact square cannot
stand in for uniform real \(X\), and that a local stationary patch naturally
reaches the square-root scale.

The smallest surviving lemma is therefore a no-go statement for
classwise/absolute annulus methods, not a proof or refutation of the full
signed endpoint estimate.

## 2. Exact statements and hypotheses

Let \(W\in C_c^\infty((a,b))\) be real and nonzero.  Let
\(D\asymp Y^{1/2}\), let \(H\asymp Y^{1/4}\), and assume

\[
 1<L\le H/4.
\]

Let \(v_L\) be nonnegative, supported on \([L,2L]\), equal to one on a
fixed interior subinterval, and have uniform scale-normalized BV norm.  Put

\[
 a_{h,H,L}=\frac{v_L(h)\Phi(h/(H+1))}{2\pi h},
 \qquad
 K_{L,H}(t)=\sum_{\substack{h>0\\h\ \mathrm{odd}}}
 a_{h,H,L}\sin(\pi h t/2).                              \tag{2.1}
\]

For each real \(X\) and integer \(d\), choose a nearest odd integer
\(r_d(X)\) to \(X/d\), using any fixed rule at ties, and set

\[
 t_d(X)=\frac{X-d r_d(X)}d\in[-1,1].                    \tag{2.2}
\]

The full two-sided block from the brief is

\[
 B_L(X)=4\sum_{d\asymp D}W(d/D)\chi_4(r_d(X))
 K_{L,H}(t_d(X)).                                        \tag{2.3}
\]

### Lemma A: fixed-profile classwise annulus capacity

There are fixed constants \(0<c_1<c_2\) such that, for each
\(c\in\{1,3\}\), the one-sided class subtotal

\[
 \begin{aligned}
 P_c(X)=4\sum_{\substack{d\asymp D\\r_d(X)\equiv c\ (4)\\
                   c_1/L\le t_d(X)\le c_2/L}}
 W(d/D)\chi_4(c)K_{L,H}(t_d(X))                         \tag{2.4}
 \end{aligned}
\]

has the following property.  If \(J\Subset(a,b)\) is a fixed interval on
which \(W\) has one sign and is bounded away from zero, let \(P_{c,J}\) denote
(2.4) with the additional restriction \(d/D\in J\).  Then

\[
 \frac1Y\int_Y^{2Y}|P_{c,J}(X)|\,dX\gg_W\frac DL.       \tag{2.5}
\]

Consequently, for each class there is a real \(X\asymp Y\) for which that
fixed-profile subtotal is \(\gg_W D/L\).  The class \(c=3\) is the
\(\rho=1\) product class and \(c=1\) is the \(\rho=3\) product class.

This is not a lower bound for \(|B_L|\): the omitted terms may cancel (2.4).
It is a sharp obstruction to taking absolute values, treating either class as
nonoscillatory, or claiming that fixed-profile smoothness reduces the number
or mass of first-annulus encounters.  It does not exclude a genuinely signed
estimate for the full sum inside one class.

### Lemma B: exact square/near-square local transition

Let \(N\) be a positive integer, choose a point \(u_0\) in the upper half of
the support with \(W(u_0)\ne0\), and put \(D=N/u_0\).  For

\[
 X_\tau=4N^2+\tau N,\qquad d=N+m,                        \tag{2.6}
\]

one has the exact identity

\[
 \frac{hX_\tau}{4d}
 =h(N-m)+h z_\tau(m),
 \qquad
 z_\tau(m)=\frac{m^2}{N+m}+\frac{\tau N}{4(N+m)}.       \tag{2.7}
\]

Define the exact two-sided frequency kernel in the original cosine
coordinates by

\[
 G_{L,H}(z)=
 2\sum_{\substack{h>0\\h\ \mathrm{odd}}}
 \beta_{h,H}v_L(h)\cos(2\pi h z),
 \qquad
 \beta_{h,H}=-\frac{\Phi(h/(H+1))\chi_4(h)}{\pi h}.     \tag{2.8}
\]

For a sufficiently small fixed \(\eta>0\) and

\[
 |m|\le M:=\eta\sqrt{N/L},                              \tag{2.9}
\]

the exact square \(\tau=0\) satisfies

\[
 \sum_{|m|\le M}W((N+m)/D)G_{L,H}(z_0(m))
 \ll_W \frac{\sqrt N}{L^{3/2}}.                        \tag{2.10}
\]

On the other hand, one may fix a constant \(s>0\) and take
\(\tau=1+s/L\) so that

\[
 \left|
 \sum_{|m|\le M}W((N+m)/D)G_{L,H}(z_{1+s/L}(m))
 \right|\gg_W \sqrt{N/L}.                             \tag{2.11}
\]

The constants can be chosen uniformly for
\(1<L\le cH\asymp c\sqrt N\).  These are local-window statements.  They do
not estimate the complementary part of the fixed profile.

## 3. Proof and derivation

### 3.1 Proof of Lemma A

Choose, for example, \(c_1=1/8\) and \(c_2=1/6\).  When
\(c_1/L\le t\le c_2/L\), \(h\in[L,2L]\), and \(h\) is odd,

\[
 \frac{\pi}{16}\le\frac{\pi ht}{2}\le\frac{\pi}{6}.
\]

All sine factors in (2.1) are positive and bounded below on the interior
part of the frequency block.  Since \(2L\le H/2\), monotonicity and
\(\Phi(1/2)=1/2\) give

\[
                   K_{L,H}(t)\gg1                       \tag{3.1}
\]

throughout this interval.  This retains the actual \(\Phi/h\) amplitudes.

Fix \(d\).  As \(X\) varies, the nearest-odd cell associated with an odd
integer \(r\) is

\[
                d(r-1)\le X\le d(r+1),
\]

and \(t_d=(X-dr)/d\) moves linearly from \(-1\) to \(1\).  Within every
cell of the chosen congruence class, the favorable interval in (2.4) has
length

\[
                  \frac{(c_2-c_1)d}{L}.                 \tag{3.2}
\]

Cells in one fixed class modulo four recur every \(4d\).  Because
\(d\asymp D\asymp Y^{1/2}\), the interval \([Y,2Y]\) contains
\(\asymp Y/d\) such cells, with endpoint loss \(O(d/L)\).  Hence the measure
of favorable \(X\) for this one denominator is \(\gg Y/L\).

Since a nonzero continuous \(W\) has a fixed interval \(J\Subset(a,b)\) on
which it has constant sign and \(|W|\ge w_0>0\), there are \(\gg_W D\)
integers \(d\) with \(d/D\in J\).  On (2.4), every retained term has the
same sign.  Integrating term by term, applying (3.1)--(3.2), and then dividing
by \(Y\) proves (2.5).

The argument is insensitive to nearest-odd ties, which form a measure-zero
set in \(X\).  It also works on the negative side of a product center and for
both residue classes.  Therefore even a prescribed smooth profile has
\(D/L\) classwise first-annulus capacity.

### 3.2 Proof of Lemma B

Polynomial division gives

\[
 \frac{N^2}{N+m}=N-m+\frac{m^2}{N+m},
\]

which proves (2.7).  Pairing positive and negative frequencies gives (2.8)
without any positive-frequency shortcut.

At the exact square, \(z_0(m)=m^2/(N+m)\).  If \(|m|\le M\) and \(\eta\)
is sufficiently small, then

\[
                    |z_0(m)|\le \frac{1}{100L}.         \tag{3.3}
\]

The factor \(\chi_4(h)\) shifts the two geometric progressions by
\(\pm1/4\).  They remain a fixed distance from an integer in (3.3), so Abel
summation with the \(C^1\) Vaaler amplitude gives

\[
                    |G_{L,H}(z_0(m))|\ll L^{-1}.        \tag{3.4}
\]

There are \(O(M)\) integers in the window and \(W\) is bounded, proving
(2.10).

For odd \(h\),

\[
 \chi_4(h)\cos\bigl(2\pi h(1/4+u)\bigr)
 =-\sin(2\pi h u).                                      \tag{3.5}
\]

Consequently

\[
 G_{L,H}(1/4+u)
 =\frac2\pi\sum_{\substack{h>0\\h\ \mathrm{odd}}}
 \frac{v_L(h)\Phi(h/(H+1))}{h}\sin(2\pi h u).          \tag{3.6}
\]

Choose \(s\), then \(\eta\), so that for every \(|m|\le M\),

\[
 \frac{1}{32L}\le
 u_m:=z_{1+s/L}(m)-\frac14
 \le\frac{1}{16L}.                                     \tag{3.7}
\]

This is possible because the exact expression is

\[
 u_m=\frac{m^2}{N+m}
 +\frac{(s/L)N-m}{4(N+m)},                              \tag{3.8}
\]

the quadratic term is \(O(\eta^2/L)\), and the linear term
\(m/N=o(1/L)\) uniformly in the stated range.  On (3.7), every sine in
(3.6) is positive and bounded below on an interior portion of the frequency
block.  Hence

\[
                  G_{L,H}(z_{1+s/L}(m))\gg1.            \tag{3.9}
\]

Finally,

\[
 \frac{N+m}{D}=u_0\left(1+\frac mN\right)=u_0+o(1),
\]

so \(W((N+m)/D)\) has the fixed sign of \(W(u_0)\) and is bounded away from
zero.  Summing (3.9) over \(\asymp M\) integers proves (2.11).

The perturbation from \(4N^2\) is only
\(X_{1+s/L}-4N^2\asymp N\), a relative change \(O(N^{-1})\).  Thus the
perfect-square local pattern is not uniform even across very nearby real
parameters.

## 4. First doubtful or unproved step

The first unproved step is cancellation between the classwise subtotals
(2.4), their negative-side analogues, and the remaining annuli.  Lemma A
shows that none of these pieces is individually smaller than \(D/L\) for a
fixed smooth profile.  No exact involution pairs them with matching Vaaler
amplitude and denominator weight.

Likewise, (2.11) is only a local contribution.  The complement of
\(|d-N|\le M\) can cancel it, so it is not a lower bound for the full
\(B_L\).  Promoting either subtotal to a full-block obstruction would repeat
the rejected “positive subtotal lower-bounds a signed sum” error.

## 5. Required controls and outcomes

1. **Both frequency signs:** passed.  Lemma A starts from the accepted sine
   kernel; Lemma B uses the exact paired cosine kernel (2.8).
2. **Actual Vaaler amplitude:** passed.  Every lower and upper estimate keeps
   \(\Phi(h/(H+1))/h\), with \(L\le H/4\) used for a uniform lower envelope.
3. **Fixed profile:** passed.  The profile is a single prescribed smooth
   \(W(d/D)\).  No sparse or parameter-adapted denominator weight is used.
4. **Signed versus unsigned:** passed.  The fixed-profile \(D/L\) result is
   explicitly classwise or absolute.  It is not asserted for the full signed
   block.
5. **Uniform real \(X\):** passed as a no-go control.  Lemma A averages over
   a real interval and produces a real pointwise obstruction to classwise
   bounds.  Lemma B explicitly contrasts a square with nearby nonsquare real
   values and draws no uniform conclusion from the square.
6. **Endpoint support:** passed.  Choosing \(D=N/u_0\) places the quadratic
   point \(d=N\) inside the fixed profile and keeps \(D\asymp X^{1/2}\).
7. **Proves-too-much:** passed.  The argument does not claim cancellation from
   profile smoothness after modulus and does not convert a coherent subtotal
   into a lower bound for \(B_L\).
8. **Computation:** none used as evidence.

## 6. Dependencies and exact artifacts used

* `protocol.md`
* `state/proof_obligations.yml`
* `state/active_campaign.yml`
* `state/best_proof_draft.md`
* `state/control_models.md`
* `rounds/codex-managed/m9-endpoint-fixed-profile-attack/plan.json`
* `rounds/codex-managed/m9-endpoint-fixed-profile-attack/briefs/endpoint_sine_kernel_attack.md`
* `rounds/codex-managed/m9-frequency-phase-diagram/reports/hybrid_corridor_hostile.md`

No external theorem or numerical artifact is used.

## 7. Recommended state effect

* **Promote** Lemma A as a fixed-profile obstruction: residue-separated,
  one-sided, or absolute first-annulus estimates retain \(D/L\) capacity at
  the balanced endpoint.
* **Promote** the exact square/near-square identity (2.7) and its scoped local
  transition (2.10)--(2.11).
* **Reject** any inference that \(X=4N^2\) models uniform real \(X\), and any
  claim that residue separation or a classwise absolute majorant improves the
  lower endpoint corridor.
* **No change** to `M9-M2` or endpoint uniformity.  A successful direct proof
  must establish cancellation between the large fixed-profile subtotals, or
  use the equivalent signed dual product-phase estimate.
