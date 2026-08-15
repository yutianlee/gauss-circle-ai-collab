# Blind one-sided transform for the top M1 block

- Campaign: `m9-combined-top-cones`
- Round: `9` (`combined_kernel_discovery`)
- Task: `blind_m1_top_transform`
- Role: statement-only deriver
- Graph SHA-256: `d155bdcc1ef62728419694f98c40a1cd4fe9664d6cc7e74528b282f8dc69fa2b`
- Isolation: no other Round-9 report or conductor combined-cone speculation was read.
- Status: candidate evidence only; no shared proof state was edited.

## 1. Result

Let

\[
y=\lfloor\sqrt X\rfloor,\qquad q=\frac{X}{y^2},\qquad
H_y=\lfloor yX^{-1/4}\rfloor,
\]

and let \(W\) be the accepted top profile, so \(W(1)=1\), \(W=1\) on
\([2/3,1]\), and \(W\) is flat and zero at and below \(1/2\).  For
\(1\le h\le H\le H_y\), define

\[
A_h=\sum_{d\le y}\chi_4(d)W(d/y)e(hX/d).
\]

The exact additive decomposition

\[
\chi_4(d)=\frac{e(d/4)-e(3d/4)}{2i}
\tag{1.1}
\]

and one-sided Poisson summation give, uniformly for sufficiently large
\(X\),

\[
\boxed{
\begin{aligned}
A_h={}&\frac1{2i}\left\{
\frac{e(hX/y+y/4)}{1-e(qh-1/4)}
-\frac{e(hX/y+3y/4)}{1-e(qh-3/4)}\right\}\\
&+\frac{e(1/8)(hX)^{1/4}}{i}
\sum_{\substack{4h<n\le16h\\ n\ \text{odd}}}
\frac{\chi_4(n)}{n^{3/4}}
W\!\left(\sqrt{\frac{4qh}{n}}\right)
e(\sqrt{Xhn})+R_h,
\end{aligned}}
\tag{1.2}
\]

where

\[
R_h\ll_W\log(2+h).
\tag{1.3}
\]

Thus the positive-frequency top M1 contribution

\[
\mathcal M^+_{1,\mathrm{end}}(H)
=-4\sum_{h=1}^{H}\alpha_{h,H}A_h,
\qquad
\alpha_{h,H}=-\frac{\Phi(h/(H+1))}{2\pi i h},
\tag{1.4}
\]

is

\[
\boxed{
\begin{aligned}
\mathcal M^+_{1,\mathrm{end}}(H)
={}&\mathcal E^+_{1,\mathrm{bdry}}(H)\\
&-\frac{2e(1/8)}{\pi}X^{1/4}
\sum_{h=1}^{H}\Phi(h/(H+1))h^{-3/4}
\sum_{\substack{4h<n\le16h\\n\ \text{odd}}}
\chi_4(n)n^{-3/4}
W\!\left(\sqrt{\frac{4qh}{n}}\right)e(\sqrt{Xhn})\\
&+O_W(\log^2(2H)),
\end{aligned}}
\tag{1.5}
\]

with the exact boundary

\[
\boxed{
\mathcal E^+_{1,\mathrm{bdry}}(H)
=-\frac1\pi\sum_{h=1}^{H}\frac{\Phi(h/(H+1))}{h}
\left\{
\frac{e(hX/y+y/4)}{1-e(qh-1/4)}
-\frac{e(hX/y+3y/4)}{1-e(qh-3/4)}
\right\}.}
\tag{1.6}
\]

In particular

\[
\mathcal E^+_{1,\mathrm{bdry}}(H)\ll\log(2H),
\qquad
\sum_{h\le H}\frac{\Phi(h/(H+1))}{h}|R_h|
\ll_W\log^2(2H).
\tag{1.7}
\]

Both are \(O_{W,\varepsilon}(X^\varepsilon)\).  Negative original
frequencies are the exact conjugates, and the actual two-sided top M1
block is

\[
2\operatorname{Re}\mathcal M^+_{1,\mathrm{end}}(H).
\tag{1.8}
\]

The transform moves the character from the denominator to the dual
variable: the original \(h\) is unrestricted in parity, while the dual
variable \(n\) is odd and carries \(\chi_4(n)\).  No even \(n\) occurs.

## 2. Dyadic normalization and exact cone

For a smooth cutoff \(\eta_L\) supported on \(h\asymp L\), put

\[
a^{M1}_{L,H,q}(h,n)
=\eta_L(h)\Phi(h/(H+1))
\left(\frac{L^2}{hn}\right)^{3/4}
W\!\left(\sqrt{\frac{4qh}{n}}\right)
\tag{2.1}
\]

and

\[
\mathcal T^{M1}_L
=\sum_{h\asymp L}
\sum_{\substack{4h<n\le16h\\n\ \text{odd}}}
\chi_4(n)a^{M1}_{L,H,q}(h,n)e(\sqrt{Xhn}).
\tag{2.2}
\]

Then

\[
\boxed{
\mathcal M^+_{1,\mathrm{end},L}
=-\frac{2e(1/8)}{\pi}X^{1/4}L^{-3/2}\mathcal T^{M1}_L
+\mathcal E^+_{1,\mathrm{bdry},L}+O_W(\log(2L)),}
\tag{2.3}
\]

where \(\mathcal E^+_{1,\mathrm{bdry},L}=O(1)\).  On the cone interior,

\[
(h\partial_h)^i(n\partial_n)^j a^{M1}_{L,H,q}(h,n)
\ll_{i,j,W}1.
\tag{2.4}
\]

The upper support edge \(n=16qh\) is smooth and flat because \(W\) is
flat at \(1/2\).  The lower edge is hard because \(W(1)=1\); split by
\(n\bmod4\), it begins at

\[
n=4h+1\quad(n\equiv1\pmod4),\qquad
n=4h+3\quad(n\equiv3\pmod4).
\tag{2.5}
\]

Consequently the first unproved top-M1 estimate is

\[
\mathcal T^{M1}_L\ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{2.6}
\]

## 3. Exact interface with the accepted M2 cone

This comparison is an algebraic consequence of (1.5), not an assumed
cancellation mechanism.  Rename the M1 variables by

\[
r=n\quad(r\text{ odd}),\qquad m=h.
\]

The M1 cone becomes

\[
\mathcal C_1=\{(r,m):r\text{ odd},\ 1\le m\le H,
\ 4m<r\le16m\}.
\tag{3.1}
\]

The accepted positive-frequency M2 cone, in the same letters, is

\[
\mathcal C_2=\{(r,m):r\text{ odd},\ 1\le r\le H,
\ \lceil r/4\rceil\le m\le r\}.
\tag{3.2}
\]

Both have the phase \(e(\sqrt{Xrm})\), the character \(\chi_4(r)\), and
the base amplitude \((rm)^{-3/4}\).  Restoring the outer arithmetic factor
\(4\) in the draft's actual M2 definition, their leading constants also
agree exactly: each is

\[
-\frac{2e(1/8)}{\pi}X^{1/4}.
\tag{3.3}
\]

Indeed, on the M2 side

\[
4\alpha_{r,H}C_r
=-\frac{4\chi_4(r)\Phi(r/(H+1))}{\pi r},
\]

and multiplication by its stationary factor
\(e(1/8)(rX)^{1/4}/2\) gives (3.3).  Since odd \(r\) can never equal
\(4m\), the cones are disjoint and meet without a lattice gap at the seam:
for \(r\le H\), their union has

\[
\lceil r/16\rceil\le m\le r,
\tag{3.4}
\]

with M1 supplying \(m\le\lfloor r/4\rfloor\) and M2 supplying
\(m\ge\lceil r/4\rceil\).

For \(H<r\le16H\), only the M1 piece remains, with

\[
\lceil r/16\rceil\le m\le
\min\{H,\lfloor r/4\rfloor\}.
\]

After factoring out the common actual leading constant (3.3), the exact
piecewise amplitude is

\[
\boxed{
\begin{aligned}
\mathcal A_{H,q}(r,m)
={}&\mathbf1_{\mathcal C_2}(r,m)
\Phi(r/(H+1))W\!\left(\sqrt{\frac{qr}{4m}}\right)\\
&+\mathbf1_{\mathcal C_1}(r,m)
\Phi(m/(H+1))W\!\left(\sqrt{\frac{4qm}{r}}\right).
\end{aligned}}
\tag{3.5}
\]

Hence the cones are geometrically complementary and their actual leading
constants and signs are compatible.  Their profiles are nevertheless
piecewise: the M1 side places \(\Phi\) on \(m\) and uses the reciprocal
\(W\)-argument, while the M2 side places \(\Phi\) on \(r\).  Formula (3.5)
licenses an exact combined signed kernel.  It does not license termwise
cancellation (the pieces are disjoint and have the same sign), nor
replacement by one smooth cone symbol without a new seam analysis.

## 4. Proof of the one-sided transform

### 4.1 Additive shifts and endpoint separation

Define, for \(\rho\in\{1,3\}\),

\[
S_{h,\rho}=\sum_{d\le y}W(d/y)e(hX/d+\rho d/4),
\qquad A_h=\frac{S_{h,1}-S_{h,3}}{2i}.
\tag{4.1}
\]

At \(t=y\), introduce

\[
B_{h,\rho}=hX/y+\rho y/4,
\qquad \lambda_{h,\rho}=qh-\rho/4.
\tag{4.2}
\]

Write \(\Delta=X-y^2\).  Since \(0\le\Delta<2y+1\) and
\(h\le H_y\le\sqrt y\),

\[
0\le h(q-1)=\frac{h\Delta}{y^2}<\frac3{\sqrt y}.
\tag{4.3}
\]

For large \(y\), (4.3) is below \(1/8\), and therefore

\[
\operatorname{dist}(\lambda_{h,1},\mathbb Z)
=\frac14-h(q-1)\ge\frac18,
\tag{4.4}
\]

while

\[
\operatorname{dist}(\lambda_{h,3},\mathbb Z)
=\frac14+h(q-1)\ge\frac14.
\tag{4.5}
\]

Thus both additive shifts are uniformly separated at the endpoint.  The
exact minimum over the two shifts is the quantity in (4.4), not \(1/4\).

### 4.2 Half-weight and principal-value boundary

Let

\[
F_{h,\rho}(t)=W(t/y)e(hX/t+\rho t/4).
\]

Finite Poisson summation with symmetric principal-value convergence gives

\[
\sum_{1\le d<y}F_{h,\rho}(d)+\frac12F_{h,\rho}(y)
=\operatorname{PV}\sum_{k\in\mathbb Z}
\int_0^yF_{h,\rho}(t)e(-kt)\,dt.
\tag{4.6}
\]

The project sum contains \(d=y\) with full weight.  The endpoint
derivative in the \(k\)-th integral is

\[
-qh+\rho/4-k=-(\lambda_{h,\rho}+k),
\]

so its modewise endpoint piece is

\[
-\frac{e(B_{h,\rho})}{2\pi i(\lambda_{h,\rho}+k)}.
\tag{4.7}
\]

Using

\[
\operatorname{PV}\sum_{k\in\mathbb Z}
\frac1{\lambda+k}=\pi\cot(\pi\lambda),
\]

the missing endpoint half plus (4.7) sum to

\[
e(B_{h,\rho})\left(\frac12+\frac i2\cot(\pi\lambda_{h,\rho})\right)
=\boxed{\frac{e(B_{h,\rho})}{1-e(\lambda_{h,\rho})}}.
\tag{4.8}
\]

Equations (4.4)--(4.5) bound (4.8) uniformly.  Keeping only the Poisson
midpoint would omit the real half in (4.8).

### 4.3 Stationary modes, phase, and constant

The \(k\)-th phase is

\[
\phi_{h,\rho,k}(t)=\frac{hX}{t}+(\rho/4-k)t.
\]

Put

\[
n=\rho-4k.
\tag{4.9}
\]

A stationary point exists only for \(n>0\), and it is

\[
t_{h,n}=2\sqrt{\frac{hX}{n}},
\qquad
u_{h,n}=\frac{t_{h,n}}y=\sqrt{\frac{4qh}{n}}.
\tag{4.10}
\]

It lies strictly below \(y\) exactly when \(n>4qh\), and the support of
\(W\) requires \(n<16qh\).  At the stationary point,

\[
\phi_{h,\rho,k}(t_{h,n})=\sqrt{Xhn},
\qquad
\phi''_{h,\rho,k}(t_{h,n})
=\frac{n^{3/2}}{4(hX)^{1/2}}>0.
\tag{4.11}
\]

Therefore the one-term stationary contribution is

\[
\boxed{
2e(1/8)(hX)^{1/4}n^{-3/4}
W\!\left(\sqrt{\frac{4qh}{n}}\right)e(\sqrt{Xhn}).}
\tag{4.12}
\]

For \(y\) sufficiently large, (4.3) also gives

\[
16h(q-1)<1.
\tag{4.13}
\]

Consequently the moving inequalities \(4qh<n<16qh\) freeze exactly to

\[
4h<n\le16h.
\tag{4.14}
\]

For \(\rho=1\), (4.9) runs over \(n\equiv1\pmod4\); for \(\rho=3\), it
runs over \(n\equiv3\pmod4\).  Subtracting the two shifted transforms
therefore gives exactly \(\chi_4(n)\) on every odd \(n\), with every even
\(n\) absent.  Combining (4.8), (4.12), and (1.1) proves (1.2), including
its factor \(1/i\).

### 4.4 Uniform remainder and endpoint noncoalescence

Scale \(t=yu\).  The phase becomes

\[
y\left(\frac{qh}{u}+\frac n4u\right).
\]

Subtract (4.7) modewise.  On the nonstationary pieces, split dyadically by
the size of \(|\lambda_{h,\rho}+k|\) and integrate by parts twice.  On each
stationary piece use the Morse coordinate at (4.10), take (4.12) as the
main Gaussian term, and integrate once in each Gaussian tail.  The lower
support edge is flat.  The resulting mode sums are

\[
\ll_W1+\sum_{1\le j\le 1+16h}\frac1j+\frac hy
\ll_W\log(2+h).
\tag{4.15}
\]

This proves (1.3) for each shift.

For completeness, the closest stationary mode for the two shifts is

\[
n=4h+1\quad(\rho=1),\qquad n=4h+3\quad(\rho=3).
\]

Its derivative gap at \(u=1\) is respectively

\[
y\{1/4-h(q-1)\}\ge y/8,
\qquad
y\{3/4-h(q-1)\}\ge5y/8.
\tag{4.16}
\]

The ordinary endpoint distance is \(\asymp1/h\), whereas the stationary
width in \(u\) is \(\asymp(yh)^{-1/2}\).  Hence the closest point is

\[
\gg\sqrt{y/h}\ge y^{1/4}
\tag{4.17}
\]

stationary widths from \(u=1\).  There is no endpoint Fresnel transition
for either additive shift.

### 4.5 Insertion of the actual coefficients

From (1.1) and the audited Vaaler coefficient,

\[
-4\alpha_{h,H}\cdot\frac1{2i}
=-\frac{\Phi(h/(H+1))}{\pi h}.
\tag{4.18}
\]

Multiplying (4.8) and (4.12) by (4.18) proves the constants in
(1.5)--(1.6).  The bounds (1.7) follow from

\[
\sum_{h\le H}\frac1h\ll\log(2H),
\qquad
\sum_{h\le H}\frac{\log(2+h)}h\ll\log^2(2H).
\tag{4.19}
\]

On one dyadic \(h\)-block the corresponding bounds are \(O(1)\) and
\(O_W(\log(2L))\).  Finally, since \(W\) and \(\chi_4\) are real and
\(\alpha_{-h,H}=\overline{\alpha_{h,H}}\), the negative-frequency block
is the conjugate of the positive-frequency block.  This proves (1.8).

## 5. Required controls

### 5.1 Exact square \(X=y^2\): pass

Here \(q=1\).  The two endpoint denominators have exact distance \(1/4\)
from the integers.  The stationary cone is exactly

\[
4h<n<16h,\qquad n\text{ odd};
\]

writing the upper edge as \(n\le16h\) is equivalent because \(16h\) is
even.  Both residue classes occur with the signs prescribed by
\(\chi_4(n)\).

### 5.2 Unit frequency \(h=1\): pass

The exact-square stationary variables are

\[
n=5,7,9,11,13,15.
\]

Thus neither a large-\(h\) assumption nor an odd-\(h\) restriction has
entered the transform.  The \(n\equiv1\pmod4\) terms come from the
\(\rho=1\) shift, and the \(n\equiv3\pmod4\) terms come from the
\(\rho=3\) shift with the opposite additive-decomposition sign.

### 5.3 Terminal frequency \(h\asymp H_y\): pass

One still has \(h\le\sqrt y\).  Equations (4.4)--(4.5) and (4.13) remain
uniform, the cone does not move, and (4.17) gives at least \(y^{1/4}\)
stationary widths of endpoint separation.  The weighted error sums in
(1.7) remain \(O_{W,\varepsilon}(X^\varepsilon)\).

### 5.4 Both additive shifts: pass

The \(\rho=1\) shift has the smaller endpoint gap
\(1/4-h(q-1)\ge1/8\); the \(\rho=3\) shift has gap at least \(1/4\).
Their stationary residues are disjoint and exhaust the odd dual
variables.

### 5.5 Even/odd dual variables: pass

Every Poisson mode has \(n=\rho-4k\), hence \(n\) is odd.  Every positive
odd \(n\) in the stationary cone belongs to exactly one shift.  Even
\(n\) have zero coefficient, not merely cancellation after estimation.
The transformed character is exactly \(\chi_4(n)\).

### 5.6 Negative original frequencies: pass

For \(h<0\), the stationary Poisson sign reverses and the whole formula
is conjugated.  The two-sided block is exactly (1.8); no new cone or
error term appears.

## 6. First doubtful or unproved step

There is no unproved additive-character, endpoint half-weight,
principal-value boundary, stationary-frequency, cone, phase, leading
constant, endpoint-separation, or Vaaler-weighted error step in
(1.1)--(2.3).  The first unproved analytic step is (2.6), or a combined
estimate for the exact piecewise kernel (3.5).  In particular, geometric
cone complementarity does not prove cancellation: the constants agree,
but the disjoint pieces have the same sign and put \(\Phi\) on different
coordinates.

## 7. Dependencies and exact artifacts used

Only the brief-authorized context was used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-combined-top-cones/briefs/blind_m1_top_transform.md`;
- H1--H4 and the M1 definition in `state/best_proof_draft.md`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`;
- `rounds/codex-managed/m9-top-endpoint-transform/reports/one_sided_poisson_derivation.md`, used only for accepted endpoint conventions.

No other Round-9 report, synthesis, validation matrix, conductor note,
web source, or computational artifact was read.

## 8. Recommended state effect

1. **Promote after independent seam review:** add a scoped internal
   top-M1 endpoint-transform lemma consisting of (1.2), (1.5), the exact
   boundary (1.6), the cone \(4h<n\le16h\), and the weighted error bounds
   (1.7).
2. **Retain `M9-M1` as open:** the signed cone estimate (2.6) is not
   proved.
3. **Retain `M9` and endpoint uniformity as open:** this report controls
   the top-M1 transform only.
4. **Record the exact combined-kernel interface:** (3.5) is a valid
   piecewise kernel with common product phase and dual character.  It
   should not be replaced by a smooth amplitude or claimed to cancel at
   the seam.

