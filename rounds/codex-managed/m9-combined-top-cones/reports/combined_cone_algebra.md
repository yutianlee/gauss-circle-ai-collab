# Combined M1/M2 top-cone algebra

- Campaign: `m9-combined-top-cones`
- Round: 9 (`combined_kernel_discovery`)
- Task: `combined_cone_algebra`
- Role: combined-kernel attacker
- Graph SHA-256: `d155bdcc1ef62728419694f98c40a1cd4fe9664d6cc7e74528b282f8dc69fa2b`
- Status: candidate evidence only; no shared state or synthesis was edited.

## 1. Result and verdict

Let

\[
y=\lfloor\sqrt X\rfloor,\qquad q=X/y^2,
\qquad H=H_y=\lfloor yX^{-1/4}\rfloor,
\]

and let the top denominator weight be

\[
w_{\rm end}(d)=W(d/y)\mathbf 1_{d\le y},
\]

with the accepted profile

\[
W(u)=0\quad(u\le 1/2),\qquad
W(u)=1\quad(2/3\le u\le 1),\qquad W(1)=1.
\]

There is an exact common-coordinate formula for the leading stationary
parts of the actual top M1 and M2 main sums.  In the common ordered pair
\((r,s)\), the character is always on the first variable and the phase is
always the same product phase:

\[
\boxed{\chi _4(r)e(\sqrt{Xrs}).}
\]

The two cones are

\[
\begin{array}{ll}
\text{transformed M1:}&r\text{ odd},\quad 1\le s\le H,
\quad 4s<r<16s,\\[2mm]
\text{transformed M2:}&r\text{ odd},\quad 1\le r\le H,
\quad \lceil r/4\rceil\le s\le r.
\end{array}                                                     \tag{1.1}
\]

Thus, for \(r\le H\), they partition the integer lattice at the affine
seam \(s=r/4\): M1 ends at \(s=\lfloor r/4\rfloor\) and M2 starts at
\(s=\lceil r/4\rceil\).  There is neither overlap nor a missing integer.

After the outer constants in the balanced H3 formula are restored, the
two stationary constants are identical:

\[
\boxed{-\frac{2e(1/8)}{\pi}X^{1/4}.}               \tag{1.2}
\]

They therefore reinforce; they do not cancel.  The exact combined
positive-frequency stationary term is

\[
-\frac{2e(1/8)}{\pi}X^{1/4}\mathcal K_H(X;q),       \tag{1.3}
\]

where

\[
\mathcal K_H(X;q)
=\sum_{\substack{r\ge1\ {\rm odd}\\s\ge1}}
\frac{\chi _4(r)}{(rs)^{3/4}}
\mathcal A_H(r,s;q)e(\sqrt{Xrs})                   \tag{1.4}
\]

and the two disjoint pieces of the actual symbol are

\[
\begin{aligned}
\mathcal A_H(r,s;q)
={}&\mathbf 1_{\substack{s\le H\\4s<r<16s}}
 \Phi\!\left(\frac{s}{H+1}\right)
 W\!\left(\sqrt{\frac{4qs}{r}}\right)\\
&+\mathbf 1_{\substack{r\le H\\\lceil r/4\rceil\le s\le r}}
 \Phi\!\left(\frac{r}{H+1}\right)
 W\!\left(\sqrt{\frac{qr}{4s}}\right).
                                                               \tag{1.5}
\end{aligned}
\]

The denominator profiles in (1.5) are reciprocal reflections and are
flatly compatible at the continuum seam.  The full symbols are not
compatible there: the M1 Vaaler factor is \(\Phi(s/(H+1))\), whereas the
M2 factor is \(\Phi(r/(H+1))\).  At \(s\sim r/4\) these become
\(\Phi(r/(4H))\) and \(\Phi(r/H)\), an order-one mismatch in general.
There is also an unmatched M1 wing \(H<r<16H\).  Hence the cones do not
assemble an exact smooth symmetric divisor coefficient, and there is no
coefficientwise cancellation or exact lattice involution across the
seam.

This is a rigorous no-go for the proposed *exact complementarity*
mechanism, not a no-go for every analytic estimate of the combined
kernel.  A remaining, strictly formulated candidate is

\[
\boxed{\mathcal K_{H,L}(X;q)\ll_\varepsilon X^\varepsilon}       \tag{1.6}
\]

Here \(\mathcal K_{H,L}\) denotes (1.4) with a fixed smooth dyadic
partition in \(r/L\) (equivalently in both variables, since (1.1) makes
\(r\asymp s\)).  Thus (1.6) is equivalent to the normalized
\(L^{3/2}X^\varepsilon\) product-phase bound.  No proof of (1.6) is given.

## 2. Exact top main sums and positive-frequency conventions

The actual M1 top main sum from H3--H4 is

\[
\mathcal M_{1,\rm end}
=-4\sum_{1\le |h|\le H}\alpha_{h,H}
 \sum_{d\le y}\chi _4(d)W(d/y)e(hX/d),              \tag{2.1}
\]

and the actual M2 top main sum is

\[
\mathcal M_{2,\rm end}
=4\sum_{1\le |h|\le H}\alpha_{h,H}C_h
 \sum_{d\le y}W(d/y)e(hX/(4d)).                     \tag{2.2}
\]

For \(h>0\),

\[
\alpha_{h,H}=\frac{i}{2\pi h}\Phi\!\left(\frac h{H+1}\right),
\qquad
\alpha_{h,H}C_h=-\frac{\chi _4(h)}{\pi h}
\Phi\!\left(\frac h{H+1}\right)\mathbf 1_{h\ {\rm odd}}.
                                                               \tag{2.3}
\]

Write \(\mathcal M_{j,\rm end}=2\Re\mathcal M^+_{j,\rm end}\).
The positive pieces are therefore

\[
\mathcal M^+_{1,\rm end}
=-\frac{2i}{\pi}\sum_{h=1}^H
 \frac{\Phi(h/(H+1))}{h}
 \sum_{d\le y}\chi _4(d)W(d/y)e(hX/d),             \tag{2.4}
\]

and

\[
\mathcal M^+_{2,\rm end}
=-\frac4\pi\sum_{\substack{1\le h\le H\\h\ {\rm odd}}}
 \frac{\chi _4(h)\Phi(h/(H+1))}{h}
 \sum_{d\le y}W(d/y)e(hX/(4d)).                    \tag{2.5}
\]

The factor \(4\) in (2.5) is essential.  The accepted Round-8 transform
report writes the normalized \(S_2\) positive piece with coefficient
\(-1/\pi\); the actual H3 main sum is \(\mathcal M_2=4S_2\).

## 3. Independent one-sided transform of M1

The additive Fourier identity

\[
\chi _4(d)=\frac{e(d/4)-e(3d/4)}{2i}                \tag{3.1}
\]

puts the spatial character into two shifted denominator sums.  Define,
for \(\rho\in\{1,3\}\),

\[
S_{h,\rho}^{(1)}
=\sum_{d\le y}W(d/y)e(hX/d+\rho d/4).              \tag{3.2}
\]

Then (2.4) becomes

\[
\mathcal M^+_{1,\rm end}
=-\frac1\pi\sum_{h=1}^H\frac{\Phi(h/(H+1))}{h}
 \bigl(S_{h,1}^{(1)}-S_{h,3}^{(1)}\bigr).           \tag{3.3}
\]

### M1 transform lemma

Uniformly for \(1\le h\le H\) and \(\rho\in\{1,3\}\),

\[
\boxed{
\begin{aligned}
S_{h,\rho}^{(1)}
={}&B_{h,\rho}^{(1)}\\
&+2e(1/8)(hX)^{1/4}
\sum_{\substack{4h<n<16h\\n\equiv\rho\ (4)}}
 W\!\left(\sqrt{\frac{4qh}{n}}\right)n^{-3/4}
 e(\sqrt{Xhn})+R_{h,\rho}^{(1)},
\end{aligned}}                                                   \tag{3.4}
\]

where

\[
B_{h,\rho}^{(1)}
=\frac{e(hX/y+\rho y/4)}{1-e(qh-\rho/4)},
\qquad
R_{h,\rho}^{(1)}\ll_W\log(2+h).                    \tag{3.5}
\]

#### Proof

Finite one-sided Poisson summation, with full weight at \(d=y\), gives a
half-sample correction plus the principal-value sum of

\[
I_{h,\rho,k}
=\int_0^yW(t/y)e\!\left(\frac{hX}{t}
   +\left(\frac\rho4-k\right)t\right)dt .           \tag{3.6}
\]

At \(t=y\), the phase derivative is

\[
-qh+\rho/4-k=-(qh-\rho/4+k).
\]

Since

\[
\operatorname {dist}(qh-\rho/4,\mathbb Z)
\ge \frac14-(q-1)h\ge\frac18                     \tag{3.7}
\]

for all sufficiently large \(X\), the endpoint is uniformly
nonstationary.  Summing its modewise integration-by-parts term and adding
the missing endpoint half gives

\[
e(hX/y+\rho y/4)
\left(\frac12+\frac i2\cot\pi(qh-\rho/4)\right),
\]

which is (3.5).

Put

\[
n=\rho-4k.
\]

A stationary point exists precisely for \(n>0\), and it is

\[
t_{h,n}=\sqrt{\frac{4hX}{n}},\qquad
\phi(t_{h,n})=\sqrt{Xhn}.                           \tag{3.8}
\]

It lies in the nonzero part of the top profile exactly when

\[
4qh<n<16qh.                                         \tag{3.9}
\]

Here \((q-1)h<3/\sqrt y\).  For large \(y\), the lower perturbation in
(3.9) is less than one and the upper perturbation is also less than one.
Because \(n\) is odd, (3.9) is exactly

\[
4h<n<16h,qquad n\equiv\rho\pmod4.                 \tag{3.10}
\]

At the stationary point,

\[
\phi''(t_{h,n})=\frac{n^{3/2}}{4(hX)^{1/2}},
\]

so the one-term stationary contribution is

\[
2e(1/8)(hX)^{1/4}n^{-3/4}
W\!\left(\sqrt{\frac{4qh}{n}}\right)e(\sqrt{Xhn}). \tag{3.11}
\]

The Round-8 Morse-coordinate and twice-integrated nonstationary argument
applies with the shifted slopes \(n/4\).  The endpoint gap (3.7), the flat
lower support edge, and the \(O(h)\) stationary modes give

\[
1+\sum_{1\le j\le 1+16h}\frac1j+O(h/y)\ll\log(2+h),
\]

which proves the remainder in (3.5).  This proves (3.4). \(\square\)

Subtracting the two residues in (3.4) yields

\[
\begin{aligned}
\mathcal M^+_{1,\rm stat}
=-\frac{2e(1/8)}{\pi}X^{1/4}
\sum_{h=1}^H\sum_{\substack{4h<n<16h\\n\ {\rm odd}}}
\frac{\chi _4(n)\Phi(h/(H+1))}{(hn)^{3/4}}\\
\hspace{35mm}\times
W\!\left(\sqrt{\frac{4qh}{n}}\right)e(\sqrt{Xhn}).
                                                               \tag{3.12}
\end{aligned}
\]

Thus M1 has the same product phase as M2, and its spatial character has
transferred exactly to the dual variable \(n\).

Its boundary correction is

\[
\mathcal E^+_1
=-\frac1\pi\sum_{h=1}^H\frac{\Phi(h/(H+1))}{h}
\bigl(B_{h,1}^{(1)}-B_{h,3}^{(1)}\bigr),            \tag{3.13}
\]

with \(\mathcal E^+_1\ll\log(2H)\), and its summed transform error is
\(O_W(\log^2(2H))\).

## 4. M2 in the same normalization

Let

\[
S_h^{(2)}=\sum_{d\le y}W(d/y)e(hX/(4d)).
\]

The accepted one-sided transform is

\[
\begin{aligned}
S_h^{(2)}
={}&B_h^{(2)}
+\frac{e(1/8)(hX)^{1/4}}2
 \sum_{m=\lceil h/4\rceil}^{h}
 W\!\left(\sqrt{\frac{qh}{4m}}\right)m^{-3/4}
 e(\sqrt{Xhm})+R_h^{(2)},                           \tag{4.1}
\end{aligned}
\]

where

\[
B_h^{(2)}=\frac{e(hX/(4y))}{1-e(qh/4)},
\qquad R_h^{(2)}\ll_W\log(2+h).                    \tag{4.2}
\]

After inserting the actual H3 factor (2.5),

\[
\begin{aligned}
\mathcal M^+_{2,\rm stat}
=-\frac{2e(1/8)}{\pi}X^{1/4}
\sum_{\substack{1\le h\le H\\h\ {\rm odd}}}
\sum_{m=\lceil h/4\rceil}^{h}
\frac{\chi _4(h)\Phi(h/(H+1))}{(hm)^{3/4}}\\
\hspace{35mm}\times
W\!\left(\sqrt{\frac{qh}{4m}}\right)e(\sqrt{Xhm}).
                                                               \tag{4.3}
\end{aligned}
\]

The boundary is

\[
\mathcal E^+_2
=-\frac4\pi\sum_{\substack{1\le h\le H\\h\ {\rm odd}}}
\frac{\chi _4(h)\Phi(h/(H+1))}{h}B_h^{(2)},         \tag{4.4}
\]

and \(\mathcal E^+_2\ll\log(2H)\); the summed transform error is
\(O_W(\log^2(2H))\).

Comparing (3.12) and (4.3) proves the equality of phases and constants.
Relabel \((n,h)=(r,s)\) in (3.12) and \((h,m)=(r,s)\) in (4.3) to obtain
(1.3)--(1.5).

## 5. Exact relation to the balanced H3 top contribution

The full two-sided combined top *main* contribution is

\[
\boxed{
\begin{aligned}
\mathcal M_{1,\rm end}+\mathcal M_{2,\rm end}
={}&2\Re\left\{-\frac{2e(1/8)}\pi X^{1/4}
\mathcal K_H(X;q)+\mathcal E^+_1+\mathcal E^+_2\right\}\\
&+O_W(\log^2(2H)).
\end{aligned}}                                                   \tag{5.1}
\]

In particular, omitting the boundary terms does not give the actual H3
top main contribution.  The formula also cannot be identified with the
whole top sawtooth contribution until the two H4 residuals are restored.
With

\[
\begin{aligned}
\mathcal R_{1,\rm end}
&=-4\sum_{d\le y}\chi _4(d)W(d/y)R_H^F(X/d),\\
\mathcal R_{2,\rm end}
&=4\sum_{d\le y}W(d/y)
\left[R_H^F\!\left(\frac{X/d+1}{4}\right)
-R_H^F\!\left(\frac{X/d+3}{4}\right)\right],
\end{aligned}                                                     \tag{5.2}
\]

the actual balanced H3 top contribution is exactly the right side of
(5.1) plus \(\mathcal R_{1,\rm end}+\mathcal R_{2,\rm end}\).  The
accepted R5 product-count argument makes (5.2) target-sized, but it does
not estimate \(\mathcal K_H\).

## 6. Why exact cone complementarity fails

### 6.1 Constants reinforce

Both pieces carry (1.2).  There is no minus sign between the lower and
upper cone.  The additive decomposition of \(\chi _4(d)\) contributes a
factor \(1/(2i)\), while the imaginary M1 Vaaler coefficient contributes
the compensating factor \(-2i\); the result has the same sign as the
actual \(4\alpha_hC_h\) coefficient in M2.

### 6.2 The character does match, but on a different route

M1 transfers \(\chi _4(d)\) to \(\chi _4(r)\) by selecting the two dual
residue classes \(r\equiv1,3\pmod4\).  M2 already has \(\chi _4(r)\) on
its original frequency.  This is genuine common structure, but it is not
cancellation because the leading constants also match.

### 6.3 The Vaaler factors do not match

At the affine seam, write \(r=4a+\epsilon\),
\(\epsilon\in\{1,3\}\).  The last M1 lattice point is \((r,a)\), while
the first M2 point is \((r,a+1)\).  On both sides the denominator profile
lies in the plateau \(W=1\) for large \(r\).  The Vaaler factors are,
however,

\[
\Phi\!\left(\frac a{H+1}\right)
\quad\hbox{and}\quad
\Phi\!\left(\frac r{H+1}\right).                  \tag{6.1}
\]

If \(r/H\to1\), the first tends to \(\Phi(1/4)>0\), while the second
tends to \(\Phi(1)=0\).  Thus the seam mismatch is order one and cannot
be absorbed into a smooth-symbol derivative bound.

### 6.4 The denominator profiles alone reflect, but no lattice involution does

In the ratio \(t=r/s\), the two denominator profiles are

\[
W(\sqrt{4q/t})\quad(4<t<16),
\qquad
W(\sqrt{qt/4})\quad(1\le t\le4).                   \tag{6.2}
\]

They are exchanged by the continuum reflection \(t\mapsto16/t\), and
they glue flatly at \(t=4\).  A product-preserving realization of this
reflection would be

\[
(r,s)\longmapsto(4s,r/4).                           \tag{6.3}
\]

But every active \(r\) is odd, so \(r/4\notin\mathbb Z\), and \(4s\) is
even, hence killed by the M2 odd-frequency projector.  Therefore (6.3)
is not a lattice involution and cannot pair terms.

### 6.5 The truncations leave an unmatched wing

M2 has \(r\le H\).  M1 has \(s\le H\), which permits
\(H<r<16H\).  Even away from the affine seam, the combined support is not
a symmetric finite divisor region.  Grouping by \(N=rs\) produces an
irregular localized odd-divisor coefficient, not a symmetric divisor
sum to which complementary-divisor pairing applies.

Mellin separation of (6.2) can separate the smooth ratio profile, but it
does not repair (6.1), the parity failure in (6.3), or the unmatched
wing.  It therefore yields no exact simplification before an analytic
estimate.

## 7. Required controls

### 7.1 Arbitrary separated surrogate coefficients: pass (no identity)

Replace the M1 Vaaler factor in (1.5) by an arbitrary sequence \(u_s\)
and the M2 factor by an independent sequence \(v_r\).  The combined
symbol becomes

\[
u_sW(\sqrt{4qs/r})\mathbf1_{4s<r<16s}
+v_rW(\sqrt{qr/(4s)})\mathbf1_{r/4\le s\le r}.
\]

Taking \(v\equiv0\) and \(u\) supported at one \(s\), or conversely,
shows that no coefficientwise cancellation, divisor involution, or
combined-to-separate norm inequality can follow from cone geometry
alone.  Conversely, choosing one nonzero surrogate term in each cone and
adjusting their complex coefficients makes the combined sum zero while
both pieces are nonzero.  Hence a combined bound need not imply a
separate M1 or M2 bound.

### 7.2 Exact-square \(X\): pass and reinforces

If \(X=y^2\), then \(q=1\), all boundary denominators are separated by
exactly \(1/4\), and every square product \(rs\) has phase one.  For
\(H\ge45\), the M1 pair

\[
(r,s)=(45,5)
\]

and the M2 pair

\[
(r,s)=(25,9)
\]

both have \(rs=225\), \(\chi _4(r)=1\), and denominator profile value
\(W(2/3)=W(5/6)=1\).  Their leading contributions have the same sign.
Thus even exact-square phases do not create the proposed cancellation.

### 7.3 Odd/even products: pass

The common character variable \(r\) is odd in both cones, but \(s\) is
unrestricted.  Therefore \(rs\) is odd exactly when \(s\) is odd, and
both odd and even products occur.  There is no second parity projector
that removes the even-product subcone.

### 7.4 Diagonal affine edge: pass with a jump

For odd \(r\), \(r/4\notin\mathbb Z\).  M1 contains
\(s=\lfloor r/4\rfloor\) and M2 contains
\(s=\lceil r/4\rceil\).  The lattice is exactly partitioned, and both
denominator profiles approach the plateau value one.  Equation (6.1)
shows that the full amplitude jumps by order one for \(r\asymp H\).

### 7.5 Both original frequency signs: pass

For positive original frequency the stationary Poisson modes have the
sign used in (3.4) and (4.1).  For negative original frequency every
term is the complex conjugate, because \(W\), \(\chi _4\), \(\Phi\), and
the H3 weights are real.  Thus the actual formula is exactly the
\(2\Re\) formula (5.1).  The negative-frequency half neither reverses
the relative M1/M2 sign nor removes either boundary.

### 7.6 Combined versus separate bounds: pass

The separated-surrogate example proves the logical point.  For the
actual coefficients, (5.1) controls only
\(\mathcal M_{1,\rm end}+\mathcal M_{2,\rm end}\).  It gives no estimate
for either summand without an additional projection or stability lemma.
Accordingly, even a proof of (1.6) would not by itself prove the graph's
separate obligations `M9-M1` and `M9-M2`; it would support a new combined
top-block route only.

## 8. First doubtful or unproved step

The first unproved step is the analytic estimate (1.6), or any estimate
of equivalent strength for the exact combined symbol (1.5).  The common
phase and character do not supply an algebraic cancellation, and taking
absolute values or applying Cauchy before exploiting the odd-divisor
coefficient loses the only remaining signed structure.

This report does not prove the top M1 block, the top M2 block, their
combined target bound, endpoint uniformity, M9-M1, M9-M2, or M9.

## 9. Dependencies and exact artifacts used

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `state/best_proof_draft.md`, specifically H1--H4 and the exact M1/M2
  main-sum definitions
- `rounds/codex-managed/m9-combined-top-cones/briefs/combined_cone_algebra.md`
- `rounds/codex-managed/m9-top-endpoint-transform/reports/one_sided_poisson_derivation.md`

No blind Round-9 report, web source, legacy response, or computational
artifact was read or used.  No numerical experiment was performed.

## 10. Recommended state effect

1. **Retain for independent seam review a scoped M1 endpoint-transform
   candidate:** equations (3.4)--(3.13), including the explicit
   principal-value boundary, transferred dual character, exact cone,
   leading constant, and summed error.
2. **Retain as a candidate combined kernel:** equations (1.4)--(1.6) and
   the exact balanced-main identity (5.1).
3. **Record a no-go for exact cone complementarity:** the constants
   reinforce, the Vaaler factors use different variables, the continuum
   reflection is not a parity-compatible lattice involution, and M1 has
   an unmatched \(r>H\) wing.
4. **Do not promote any estimate:** (1.6) is open, and a combined bound
   would not imply the separate graph obligations.
5. **Retain `M9-M1`, `M9-M2-top-endpoint-signed-cone`,
   `M9-endpoint-uniformity`, `M9-M2`, and `M9` as open.**
