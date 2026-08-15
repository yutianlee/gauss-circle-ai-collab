# Blind two-step resonance decomposition

- Campaign: `m9-m1-ordered-denominator-resonance-cells`
- Round: 13
- Role: statement-only exact deriver
- Status: candidate evidence only; no shared proof state was edited

## 1. Result

The ordered odd-denominator decomposition is exact, but its best elementary
consequence is precisely the already known second-derivative/B-process bound.
It gives no new point of the residual corridor \(\mathcal U_1\).

For one positive-frequency shell, put

\[
 u_{L,H}(h)=v_L(h)\frac{\Phi(h/(H+1))}{h},
 \qquad
 \mathcal B^+_{1,L}(D;X)
 =\sum_{h\geq1}u_{L,H}(h)S_h,
\]

where

\[
 S_h=\sum_{d\ \mathrm{odd}}\chi_4(d)w_D(d)e(hX/d).
\]

Here \(v_L\) is the actual dyadic frequency profile, \(h\asymp L\),
\(1\leq L\leq H\), and \(H=\lfloor DX^{-1/4}\rfloor\).  For real
profiles, the exact two-sided M1 shell is

\[
 \mathcal M_{1,L}(D;X)=\frac4\pi\operatorname{Im}
 \mathcal B^+_{1,L}(D;X).
\tag{1.1}
\]

On odd \(d\), define

\[
 g_h(d)=\frac d4+\frac{hX}{d},
 \qquad
 \tau_h(d)=\frac{2hX}{d(d+2)}.
\]

Then

\[
 \chi_4(d)e(hX/d)=-i e(g_h(d))
\]

and the exact odd-lattice increment is

\[
 \boxed{g_h(d+2)-g_h(d)=\frac12-\tau_h(d).}
\tag{1.2}
\]

The character flip fails to cancel precisely near

\[
 \boxed{\tau_h(d)\in \tfrac12+\mathbb Z,}
\tag{1.3}
\]

because there the ratio of consecutive unweighted summands is close to
\(1\).  If

\[
 T_h=\frac{hX}{D^2},\qquad \lambda_h=\frac{hX}{D^3},
\]

then the number of resonance cells is \(O(1+T_h)\), their natural width is
\(O(1+\lambda_h^{-1/2})\), and their total elementary stationary
contribution is

\[
 \ll 1+\min\left(D,\sqrt{\frac{hX}{D}}\right).
\]

The nonresonant complement has the same bound.  Consequently

\[
 \boxed{
 \mathcal B^+_{1,L}(D;X)
 \ll 1+\min\left(D,\sqrt{\frac{LX}{D}}\right).}
\tag{1.4}
\]

Writing \(D=X^\delta\), \(L=X^\ell\), the exponent supplied by (1.4) is

\[
 E_{\rm ord}(\delta,\ell)=
 \begin{cases}
 \delta,&1+\ell-3\delta\geq0,\\[2mm]
 \dfrac{1+\ell-\delta}{2},&1+\ell-3\delta\leq0.
 \end{cases}
\tag{1.5}
\]

The condition \(E_{\rm ord}\leq1/4\) gives only the already removed lower
endpoint \(\delta=1/4\) on the trivial arm and the already accepted point
\((\delta,\ell)=(1/2,0)\) on the stationary arm.  Thus it adds nothing
beyond the accepted terminal/TTY/V2 menu.  The resonance centers are in
one-to-one correspondence with the odd dual frequencies of the accepted
M1 B-process cone, so an improvement requires signed cancellation between
stationary cells and is equivalent-hard to that cone estimate.

## 2. Exact statement and hypotheses

Let \(X\geq2\), \(y=\lfloor\sqrt X\rfloor\), and let \(D\) be active:

\[
 X^{1/4}\leq D\leq X^{1/2}.
\]

Let \(w=w_D\) be one of the accepted actual denominator profiles.  Thus it
is supported on a fixed-ratio interval \([c_0D,c_1D]\cap[1,y]\),

\[
 \|w\|_\infty+\sum_d|w(d+1)-w(d)|\ll1,
\tag{2.1}
\]

and only the top profile has a hard cutoff at \(d\leq y\).  Let \(a\leq b\)
be odd integers bounding the participating odd denominators, with every
odd denominator between them allowed and zeros of \(w\) retained.  In the
top block, \(b=d_{\rm top}\) is the largest odd integer at most \(y\).

Let \(v_L\) be the actual frequency-shell profile, supported on
\(h\asymp L\), with \(1\leq L\leq H\).  The only frequency facts needed
below are

\[
 \sum_h|u_{L,H}(h)|\ll1,
 \qquad
 u_{L,H}(h)=v_L(h)\frac{\Phi(h/(H+1))}{h}.
\tag{2.2}
\]

For every participating \(h\), the following identity is exact:

\[
\begin{aligned}
 S_h={}&\frac12\chi_4(a)w(a)e(hX/a)
       +\frac12\chi_4(b)w(b)e(hX/b)\\
 &+\frac12\sum_{\substack{a\leq d\leq b-2\\d\ \mathrm{odd}}}
 \chi_4(d)e(hX/d)
 \left\{w(d)-w(d+2)e(-\tau_h(d))\right\}.
\end{aligned}
\tag{2.3}
\]

Splitting the braces gives the exact amplitude-mismatch and phase-increment
pieces

\[
 \mathfrak A_h=\frac12\sum_{d}
 \chi_4(d)e(hX/d)\{w(d)-w(d+2)\},
\tag{2.4}
\]

\[
 \mathfrak I_h=\frac12\sum_{d}
 \chi_4(d)e(hX/d)w(d+2)\{1-e(-\tau_h(d))\}.
\tag{2.5}
\]

The two endpoint terms in (2.3) are the exact boundary terms.  For the top
profile the upper one is the hard-top term

\[
 \boxed{
 \mathfrak H_h^{\rm top}
 =\frac12\chi_4(d_{\rm top})w(d_{\rm top})
 e(hX/d_{\rm top}).}
\tag{2.6}
\]

For the explicit accepted top profile, \(w(d_{\rm top})=1\) for large
\(X\).  Equations (2.1)--(2.2) imply

\[
 \sum_hu_{L,H}(h)\mathfrak A_h\ll1,
 \qquad
 \sum_hu_{L,H}(h)\mathfrak H_h^{\rm top}\ll1,
\tag{2.7}
\]

and the lower boundary is also \(O(1)\) after the frequency shell is
summed.

For \(0<\eta\leq1/4\) and \(j\geq0\), define the exact resonance cell

\[
 \boxed{
 \mathcal C_{h,j}(\eta)=
 \left\{d\in[a,b-2]:d\ \mathrm{odd},\;
 \left|\tau_h(d)-\left(j+\frac12\right)\right|<\eta
 \right\}.}
\tag{2.8}
\]

These are exactly the cells on which

\[
 \left\|g_h(d+2)-g_h(d)\right\|<\eta.
\]

At their centers the two-step ratio is \(1\); by contrast, if
\(\tau_h(d)\in\mathbb Z\), the ratio is \(-1\) and only amplitude mismatch
survives in the adjacent pair.

## 3. Proof and derivation

### 3.1 Character algebra, increment, and exact two-step formula

For odd \(d\), direct checking modulo \(4\) gives

\[
 \chi_4(d)=-i e(d/4).
\]

Also

\[
 \frac{hX}{d+2}-\frac{hX}{d}
 =-\frac{2hX}{d(d+2)},
\]

which proves (1.2).  Since \(\chi_4(d+2)=-\chi_4(d)\), two adjacent odd
terms satisfy

\[
\begin{aligned}
 &\chi_4(d)w(d)e(hX/d)
 +\chi_4(d+2)w(d+2)e(hX/(d+2))\\
 &\qquad=\chi_4(d)e(hX/d)
 \{w(d)-w(d+2)e(-\tau_h(d))\}.
\end{aligned}
\tag{3.1}
\]

Summing (3.1) for \(d=a,a+2,\ldots,b-2\) counts each interior term twice
and each endpoint once.  Adding one half of each endpoint proves (2.3),
and splitting its braces proves (2.4)--(2.5).  The step-two variation in
(2.4) is at most the ordinary discrete variation in (2.1), proving (2.7).

The increment itself is strictly increasing, with exact second difference

\[
 \boxed{
 \{g_h(d+4)-g_h(d+2)\}-\{g_h(d+2)-g_h(d)\}
 =\frac{8hX}{d(d+2)(d+4)}.}
\tag{3.2}
\]

Thus on \(d\asymp D\) the increment changes by \(\asymp\lambda_h\) per
odd step and traverses a range \(O(1+T_h)\).

### 3.2 Exact nonresonant two-step summation

The elementary estimate used here can be proved without importing an
exponential-sum theorem.  On an odd interval
\(J=\{p,p+2,\ldots,q\}\), write

\[
 z_d=e(g_h(d)),\qquad
 \rho_d=\frac{z_{d+2}}{z_d}
 =e(g_h(d+2)-g_h(d)).
\]

Whenever \(\rho_d\ne1\), put

\[
 c_d=\frac{A_d}{1-\rho_d}.
\]

Then the following summation identity is exact:

\[
\begin{aligned}
 \sum_{d\in J}A_dz_d
 ={}&c_pz_p
 +\sum_{\substack{p+2\leq d\leq q-2\\d\ \mathrm{odd}}}
 (c_d-c_{d-2})z_d
 +(A_q-c_{q-2})z_q.
\end{aligned}
\tag{3.3}
\]

Indeed, it is just

\[
 \sum_{d=p}^{q-2}c_d(z_d-z_{d+2})+A_qz_q.
\]

Suppose on \(J\) that the monotone increments stay in one strip

\[
 m+\eta\leq g_h(d+2)-g_h(d)\leq m+1-\eta.
\]

The exact identity

\[
 \frac1{1-e(t)}=\frac12+\frac i2\cot(\pi t)
\tag{3.4}
\]

shows that its supremum and its total variation on such a strip are both
\(O(\eta^{-1})\).  Applying (3.3) with \(A_d=w(d)\) therefore gives

\[
 \left|\sum_{d\in J}w(d)e(g_h(d))\right|
 \ll\eta^{-1}
 \left(\|w\|_{\infty,J}+\operatorname{Var}_J(w)\right).
\tag{3.5}
\]

This is the elementary nonresonant estimate.  It is exact two-step
summation by parts, not an appeal to an external first-derivative theorem.

### 3.3 Cell count, total lengths, and optimization

The resonance function is strictly decreasing and has exact decrement

\[
 \boxed{
 \tau_h(d)-\tau_h(d+2)
 =\frac{8hX}{d(d+2)(d+4)}\asymp\lambda_h.}
\tag{3.6}
\]

Hence only \(O(1+T_h)\) half-integer levels meet the denominator shell, and
each nonempty cell has

\[
 \#\mathcal C_{h,j}(\eta)\ll1+\frac{\eta}{\lambda_h}.
\]

Since \(T_h=\lambda_hD\) and \(T_h\gg1\) in the active range,

\[
 \boxed{
 \sum_j\#\mathcal C_{h,j}(\eta)
 \ll 1+T_h+\eta D.}
\tag{3.7}
\]

After removing the cells, split whenever the monotone increment crosses an
integer strip.  There are \(O(1+T_h)\) remaining components.  Summing
(3.5), using the global BV bound, gives

\[
 \boxed{
 |S_h({\rm nonresonant})|
 \ll\frac{1+T_h}{\eta}.}
\tag{3.8}
\]

Trivial estimation on the cells and (3.7)--(3.8) give

\[
 |S_h|\ll 1+T_h+\eta D+\frac{1+T_h}{\eta}.
\tag{3.9}
\]

If \(\lambda_h\leq1\), take \(\eta\asymp\sqrt{\lambda_h}\), truncated at
a fixed small constant.  Then \(T_h\leq D\), and (3.9) gives

\[
 |S_h|\ll1+\sqrt{DT_h}
 =1+\sqrt{\frac{hX}{D}}.
\tag{3.10}
\]

If \(\lambda_h>1\), the trivial estimate \(|S_h|\ll D\) is better.  Thus

\[
 \boxed{
 |S_h|\ll1+\min\left(D,\sqrt{\frac{hX}{D}}\right).}
\tag{3.11}
\]

The same calculation records the stationary capacity explicitly.  When
\(\lambda_h\leq1\), the natural cell width is

\[
 \lambda_h^{-1/2}\asymp
 \sqrt{\frac{D^3}{hX}},
\tag{3.12}
\]

there are \(O(T_h)\) cells, and their total length and total trivial
stationary contribution are

\[
 T_h\lambda_h^{-1/2}\asymp
 \sqrt{DT_h}=\sqrt{\frac{hX}{D}}.
\tag{3.13}
\]

The nonresonant total (3.8), at the same choice of \(\eta\), is of exactly
the same order.  When \(\lambda_h>1\), the cells have lattice width
\(O(1)\) and all elementary estimates saturate at \(D\).

Finally (2.2), (3.11), and \(h\asymp L\) prove (1.4).  The mismatch,
ordinary boundary, and hard-top pieces contribute only \(O(1)\) and do not
change it.

### 3.4 Exponent translation on \(\mathcal U_1\)

For \(D=X^\delta\), \(L=X^\ell\),

\[
 T_L=X^{1+\ell-2\delta},
 \qquad
 \lambda_L=X^{1+\ell-3\delta}.
\tag{3.14}
\]

In the stationary regime \(\lambda_L\leq1\):

\[
 \begin{array}{c|c}
 \text{quantity}&\text{power of }X\\ \hline
 \text{number of cells}&1+\ell-2\delta\\
 \text{natural width of one cell}&(3\delta-1-\ell)/2\\
 \text{total resonant length}&(1+\ell-\delta)/2\\
 \text{total stationary contribution}&(1+\ell-\delta)/2\\
 \text{nonresonant contribution}&(1+\ell-\delta)/2\\
 \text{mismatch/boundary/hard top}&0.
 \end{array}
\tag{3.15}
\]

In the large-curvature regime \(\lambda_L>1\), the elementary result is the
trivial exponent \(\delta\).  This proves (1.5).

On the stationary arm the target condition is

\[
 \frac{1+\ell-\delta}{2}\leq\frac14
 \quad\Longleftrightarrow\quad
 \delta\geq\ell+\frac12.
\]

Since \(\delta\leq1/2\) and \(\ell\geq0\), this forces
\((\delta,\ell)=(1/2,0)\).  On the trivial arm the target forces
\(\delta\leq1/4\), which gives only the lower active endpoint and no point
of \(\mathcal U_1\).  Therefore the ordered decomposition adds no region
to the accepted terminal line, TTY wedge

\[
 178\ell+1638\delta\leq463,
\]

and isolated V2 point \((1/2,0)\).

### 3.5 Exact identification with the M1 B-process cone

At exact resonance, write the half-integer as \(n/2\) with \(n\) odd.
Equation (2.8) has the exact continuous center

\[
 d^{\rm disc}_{h,n}
 =\sqrt{1+\frac{4hX}{n}}-1.
\tag{3.16}
\]

Now parameterize odd denominators by \(d=1+2r\).  The phase is
\(g_h(1+2r)\).  Its Fourier mode \(k\in\mathbb Z\) is stationary when

\[
 \frac{d}{dr}g_h(1+2r)=\frac12-\frac{2hX}{d^2}=k.
\]

Putting \(n=1-2k\) gives the odd dual frequency and the stationary point

\[
 d^{\rm stat}_{h,n}=\sqrt{\frac{4hX}{n}}.
\tag{3.17}
\]

The centers (3.16)--(3.17) differ by \(O(1)\), hence label the same natural
cell.  At (3.17), after subtracting the Fourier mode, the phase is

\[
 \sqrt{Xhn}+\frac{k}{2}.
\]

Combining the constant \(-i\) in
\(\chi_4(d)e(hX/d)=-ie(g_h(d))\) with \(k=(1-n)/2\) yields

\[
 e(-n/4)=-i\chi_4(n).
\tag{3.18}
\]

The quadratic stationary scale is
\(\lambda_h^{-1/2}\), equivalently

\[
 (hX)^{1/4}n^{-3/4}\asymp
 \sqrt{\frac{D^3}{hX}}
 \qquad(n\asymp T_h).
\tag{3.19}
\]

Thus the resonance-cell sum has exactly the actual dual character
\(\chi_4(n)\), product phase \(e(\sqrt{Xhn})\), dual length
\(n\asymp hX/D^2\), and stationary amplitude of the accepted M1
B-process transform.  On the hard top block \(D=y\), it becomes the
accepted odd cone

\[
 4h<n<16h,
 \qquad
 \chi_4(n)a_{M1}(h,n)e(\sqrt{Xhn}),
\]

up to the already controlled endpoint and transform terms.  Estimating the
cells absolutely gives (3.13), i.e. V2.  Any gain must retain (3.18) and
cancel different \((h,n)\) cells; that is the known signed M1 cone problem,
not a new easier mechanism.

## 4. First doubtful or unproved step

There is no doubtful step in the character identity, exact increment,
two-step formula, BV mismatch estimate, resonance count, nonresonant
summation identity, or exponent arithmetic.

The first unproved step is any cancellation between distinct stationary
cells after the absolute total (3.13).  On the top block this is exactly the
open estimate

\[
 \sum_{h\asymp L}
 \sum_{\substack{4h<n<16h\\n\ \mathrm{odd}}}
 \chi_4(n)a_{M1}(h,n)e(\sqrt{Xhn})
 \ll_\epsilon L^{3/2}X^\epsilon.
\]

For an interior block it is the corresponding actual-symbol cone with
\(n\asymp hX/D^2\).  No elementary consequence of monotonicity or of the
two-step character flip proves this signed estimate.  In the original
variables the same missing cancellation is the ordered-denominator/PSC
interface.  Treating cells separately, or summing their stationary sizes,
reproduces V2 and cannot change \(\mathcal U_1\).

## 5. Required controls and outcomes

### Character-flip control: pass

If \(\tau_h(d)\in\mathbb Z\) and \(w(d)=w(d+2)\), (3.1) is zero.  If
\(\tau_h(d)\in\mathbb Z+1/2\), (3.1) is twice the common-amplitude term.
Thus (2.8), rather than the integer cells of \(\tau_h\), is the correct
noncancelling resonance definition.

### Amplitude and boundary control: pass

The exact mismatch has total size bounded by the fixed discrete BV norm.
The ordinary endpoints and the unique hard-top term have shell-summed size
\(O(1)\).  No continuum smoothness is used, so the top jump is not hidden.

### Exact-square endpoint control: pass

Take \(X=y^2\) and the actual top profile.  Let \(b\) be the largest odd
integer at most \(y\), and put \(a=b-2\).  Both lie in the plateau where
\(w=1\).  If \(y\) is odd, then

\[
 \tau_h(a)=\frac{2hy^2}{(y-2)y}
 =2h+\frac{4h}{y-2}.
\]

If \(y\) is even, then

\[
 \tau_h(a)=\frac{2hy^2}{(y-3)(y-1)}
 =2h+O(h/y).
\]

Uniformly for \(h\leq H_y\leq y^{1/2}\), the top adjacent pair therefore
has size

\[
 |1-e(-\tau_h(a))|\ll h/y\leq y^{-1/2}.
\]

Thus the hard top is in the character-cancelling, not the resonant,
configuration.  The first admissible stationary frequency inside the exact
square top is \(n=4h+1\), since \(4h\) is even.  Its point is

\[
 d_{h,4h+1}=y\sqrt{\frac{4h}{4h+1}},
\]

whose distance from \(y\) is \(\asymp y/h\).  The natural width is
\(\asymp\sqrt{y/h}\), so their ratio is
\(\asymp\sqrt{y/h}\geq y^{1/4}\).  Hence no stationary cell collides with
the hard endpoint.  Interior cells remain, so this control does not improve
(1.4).

### Exponent-menu control: pass

The ordered estimate closes only \((1/2,0)\) beyond the lower active
endpoint.  That point is already the accepted V2 point and is explicitly
removed from \(\mathcal U_1\).  No point beyond the terminal/TTY/V2 menu is
claimed.

### Unsigned/adversarial control: pass

The proof uses the exact sign flip \(\chi_4(d+2)=-\chi_4(d)\).  Replacing
the character by unsigned coefficients destroys (1.2), (3.1), and the
half-integer resonance law.  Even with the actual character, taking
absolute values over stationary cells loses \(\chi_4(n)\) and recovers only
V2.  No numerical experiment was used.

## 6. Dependencies and exact artifacts used

Only the brief-authorized packet was used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `state/best_proof_draft.md`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`;
- `rounds/codex-managed/m9-m1-ordered-denominator-resonance-cells/briefs/blind_two_step_resonance_decomposition.md`.

No Round-13 report, Round-12 report, external theorem, web source, or
numerical experiment was read or used.  The exact transform comparison uses
only the accepted M1 B-process statement recorded in the authorized proof
draft; the resonance and nonresonance estimates above were derived directly.

## 7. Recommended state effect

1. **Promote after independent seam review:** retain (2.3), (2.8),
   (3.3), (3.7), and (3.11) as an exact ordered-denominator reduction and
   an internal elementary bound.
2. **Promote as a scoped no-go:** absolute totaling of the two-step
   resonance cells is equivalent to the accepted M1 V2/B-process bound and
   adds no point of \(\mathcal U_1\).
3. **Retain open:** `M9-M1-shifted-divisor-correlation-PSC`,
   `M9-M1-cross-product-odd-kernel-discrepancy`, `M9-M1`, and `M9`.
4. **Revise the next-action wording only:** any continued ordered-
   denominator attack must prove cancellation across the signed stationary
   cells (equivalently the actual M1 product-phase cone or PSC), rather than
   merely count resonance cells or estimate them separately.
5. **No theorem-level change:** the Gauss-circle target remains open, and
   no new exponent or residual region is proved.
