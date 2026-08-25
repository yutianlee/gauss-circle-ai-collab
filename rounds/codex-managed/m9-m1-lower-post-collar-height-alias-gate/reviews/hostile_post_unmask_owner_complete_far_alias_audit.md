# Round 140 post-unmask hostile audit: owner-complete far aliases

## 1. Result

**GREEN.** The patched conductor candidate survives hostile comparison
with all three primary reports and now satisfies every requested
owner-completeness and artifact-hygiene repair.

The sharp Poisson identity, its principal-value boundary obstruction,
the exact floor and \(q\) threshold, the two-collar smoothing support,
the derivative scales, the \(O(\sqrt h)\) transition count, the
\(r_{2,h}+2\) clean-bulk start, the stationary normalization, the exact
product coefficient, the rank-one obstruction, and the downstream
direction are all correct.

The three carriage-return corruptions are repaired, the empty-row
convention is explicit, the \(r_{2,h}\) wording is owner-safe, and the
new (140.C19a)--(140.C19f) ledger supplies the previously missing
rowwise smooth \(B\)-process proof.  In particular, the corrected
(140.C19e) now multiplies the transition-alias count by the per-alias
variation:

\[
 \sqrt h\,{w^2\over h\Delta_h}\ll {1\over h},
\tag{140.R0}
\]

The left side is \(h^{-1}\) because
\(w^2\asymp y/h\) and \(\Delta_h\asymp y/\sqrt h\).
The far arithmetic estimate (140.C6)/(140.C26) remains genuinely open.

## 2. Exact audited statement and hypotheses

Retain

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,\qquad0\le q\le2y,
\tag{140.R1}
\]

and fixed constants

\[
 0<\rho_1<\rho_2<1/8.
\tag{140.R2}
\]

For \(i=1,2\), let

\[
 L_{i,h}=\left\lfloor{\rho_i y\over\sqrt h}\right\rfloor,\qquad
 D_{i,h}=y-L_{i,h}-1.
\tag{140.R3}
\]

The profile hypotheses actually used are: \(V_{\rm low}\) is fixed,
real, smooth, compactly supported as a function of its argument, flat
at its support boundary, and equal to one near zero. Its zero extension
therefore makes
\[
 h^{-1}V_{\rm low}(4R^2h^2/x^2)
\]
smooth and identically zero near \(x=0\). A nonzero sample forces
\(h\ll x/R\), so every relevant height satisfies \(h\ll R\).
Empty rows are deleted before a \(D_{i,h}\)-denominator is formed.

For every nonempty row, define \(r_{2,h}\) as the least positive odd
integer satisfying

\[
 r_{2,h}\ge {4Nh\over D_{2,h}^2}.
\tag{140.R4}
\]

After the repairs in Sections 3--4, the exact promotable conclusion is

\[
 \mathcal S_{N,\rho_1}^{\pm}
 =\mathcal P_{\rho_2}^{\pm}
 +O_{\rho_1,\rho_2,V}(R\log^C(2X)),
\tag{140.R5}
\]

where

\[
 \mathcal P_{\rho_2}^{+}
 =e(-1/8)N^{1/4}
 \sum_{h\ge1}
 \sum_{\substack{r\ge r_{2,h}+2\\r\ {\rm odd}}}
 \chi_4(r)(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)e(\sqrt{Nhr}),
 \qquad
 \mathcal P_{\rho_2}^{-}=\overline{\mathcal P_{\rho_2}^{+}}.
\tag{140.R6}
\]

Thus the scalar target is equivalent to

\[
 |\mathcal P_{\rho_2}^{\pm}|
 \ll_\varepsilon RX^\varepsilon.
\tag{140.R7}
\]

Equation (140.R7) is not proved. No square identity is part of
(140.R5).

## 3. Equation-by-equation audit

**Sharp cutoff and principal value.** Equations (140.C8)--(140.C10)
are correct once empty rows are explicitly understood as zero. For

\[
 I_{h,r}^{\sharp}
 =\int_0^{D_{1,h}}A_h(x)e(Nh/x+rx/4)\,dx,
\]

integration by parts gives

\[
 I_{h,r}^{\sharp}
 ={A_h(D_{1,h})e(Nh/D_{1,h}+rD_{1,h}/4)
   \over2\pi i(r/4-Nh/D_{1,h}^2)}
 +O_h(r^{-2}).
\tag{140.R8}
\]

The lower endpoint vanishes. On the \(h=1\) plateau row the numerator
is nonzero for large \(X\), so the absolute odd-\(r\) sum diverges.
The half-endpoint and the branchwise symmetric limit are therefore
essential. This confirms (140.C14) and falsifies a sharp
closest-alias-only reduction.

**Floor and centre ledger.** Put \(a_{1,h}=L_{1,h}+1\). Then

\[
 {4Nh\over D_{1,h}^2}-4h
 ={4h(2ya_{1,h}-a_{1,h}^2+q)\over(y-a_{1,h})^2}.
\tag{140.R9}
\]

This is exactly (140.C12). Because
\(\rho_1y/\sqrt h<a_{1,h}\le\rho_1y/\sqrt h+1\), it is
\(\asymp_{\rho_1}\sqrt h\) on active rows. Changing \(q=0\) to
\(q=2y\) adds exactly \(8hy/D_{1,h}^2=O_{\rho_1}(h/y)\).
Equality is a boundary stationary point, not a full Gaussian. No
floor, parity, or \(q\)-term is missing.

**Smoothing support.** With

\[
 \Delta_h=D_{1,h}-D_{2,h}+1=L_{2,h}-L_{1,h}+1
 \asymp_{\rho_1,\rho_2}{y\over\sqrt h}
\tag{140.R10}
\]

and

\[
 W_h(x)=\eta\!\left({D_{1,h}+1-x\over\Delta_h}\right),
\tag{140.R11}
\]

one has \(W_h(d)=1\) for every integer \(d\le D_{2,h}\) and
\(W_h(d)=0\) for every integer \(d\ge D_{1,h}+1\). Hence

\[
 {\bf1}_{d\le D_{1,h}}-W_h(d)
\]

is supported exactly on \(D_{2,h}<d\le D_{1,h}\), equivalently

\[
 L_{1,h}<v=y-d\le L_{2,h}.
\tag{140.R12}
\]

This verifies the off-by-one choices in (140.C15)--(140.C17).
The sampled smoothing factor has \(O(1)\) variation, so the Round-139
exact-curvature estimate applies to the complete signed difference and
gives (140.C18). This step occurs before Poisson and therefore
preserves scalar direction.

**Derivative norms.** Flatness of \(\eta\) and the fixed profile gives

\[
 \|W_h^{(j)}\|_\infty\ll_j\Delta_h^{-j},
\]

\[
 \|\widetilde A_h\|_\infty+\|\widetilde A_h'\|_1\ll h^{-1},
 \qquad
 \|\widetilde A_h''\|_1
 \ll {1\over h}\left({1\over Rh}+{1\over\Delta_h}\right).
\tag{140.R13}
\]

The profile second derivative contributes \((Rh)^{-1}/h\), the smooth
collar contributes \(\Delta_h^{-1}/h\), and the mixed term is bounded by
their sum. All physical endpoint values and derivatives vanish.
Equation (140.C19) is correct.

**Transition and clean start.** A saddle lies in the smoothing ramp
only if

\[
 {4Nh\over(D_{1,h}+1)^2}
 \le r\le {4Nh\over D_{2,h}^2}.
\tag{140.R14}
\]

The length of this interval is \(O_{\rho_1,\rho_2}(1+\sqrt h)\);
the floor and \(q\) change only its constant. On the ramp
\(\phi''(x)\gg h/y\), and the BV norm of the weighted amplitude is
\(O(1/h)\), so one exact integral costs

\[
 O\!\left({1\over h}\sqrt{y/h}\right)=O(Rh^{-3/2}).
\tag{140.R15}
\]

Summing all ramp aliases costs \(O(R\log(2X))\). The alias \(r_{2,h}\)
is either the equality alias or the first odd alias immediately beyond
the threshold and costs the same; discarding it is valid. For
\(r\ge r_{2,h}+2\), the gap from the threshold is at least two, while
the transition width is \(O(\sqrt{h/y})<1\). The saddle is therefore
many Gaussian widths inside \(W_h=1\). The bulk start in (140.C4) is
correct. Starting instead at \(r_{1,h}+2\) would be false because it
would cut through the whole smoothing ramp.

**Stationary normalization.** With \(m=hr\),
\(\lambda=\sqrt{Nm}\), and \(x=x_*u\), the integral is

\[
 2\sqrt{N/m}\int
 V_{\rm low}(R^2m/(Nu^2))W_h(x_*u)
 e\!\left({\lambda\over2}(u+u^{-1})\right)\,du.
\tag{140.R16}
\]

The Gaussian term is exactly

\[
 2e(1/8)N^{1/4}(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)e(\sqrt{Nhr}).
\tag{140.R17}
\]

Multiplication by \(\chi_4(r)/(2i)\) yields \(e(-1/8)\chi_4(r)\).
The local Taylor error
\(O(N^{-1/4}(hr)^{-5/4})\) sums absolutely. The normalization and
constant in (140.C22)--(140.C23) are green.

**Product coefficient.** Since both the profile and phase in
(140.R6) depend on \(h,r\) only through \(m=hr\), finite regrouping gives

\[
 A_{\rho_2}(m)=
 \sum_{\substack{h\mid m,\ r=m/h\ {\rm odd}\\
                 r\ge r_{2,h}+2}}\chi_4(r).
\tag{140.R18}
\]

There is no missing height weight: it is already contained in
\((hr)^{-3/4}\). The complete unmasked fibre is
\(\sum_{r\mid m}\chi_4(r)=r_2(m)/4\), so the candidate's incomplete
coefficient and self-return statements are exact. The prime-power
same-sign control should be qualified by
\(p^{2a}\ll y\), sufficiently large \(X\), and literal profile support;
it is an internal fibre control, never a scalar lower bound.

## 4. First doubtful step and completed repairs

The formerly doubtful step was the passage from (140.C19) to the final
sentence after (140.C23).  The blind report correctly left this owner
seam open: two integrations by parts are necessary for the remote
negative and profile-exterior aliases, and the derivative-image
distance, phase derivatives, dyadic physical blocks, and height sum
must be uniform.

The patched candidate now closes that seam in
(140.C19a)--(140.C19f).  Its rowwise statement is the following.  If

\[
 \widetilde I_{h,r}
 =\int_0^\infty\widetilde A_h(x)e(Nh/x+rx/4)\,dx,
\]

then a dyadic partition \(x\asymp Z\), local Gaussian expansion at every
stationary alias, and integration by parts off the stationary
neighborhoods give

\[
 \begin{split}
 {1\over2i}\sum_{r\ {\rm odd}}\chi_4(r)\widetilde I_{h,r}
 ={}&e(-1/8)N^{1/4}
 \sum_{\substack{r>0\\r\ {\rm odd}}}
 \chi_4(r)(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)W_h(x_{h,r})e(\sqrt{Nhr})\\
 &+O_{\rho_1,\rho_2,V}\!\left({\log^2(2X)\over h}\right).
 \end{split}
\tag{140.R19}
\]

Here \(x_{h,r}=2\sqrt{Nh/r}\). On \(x\asymp Z\),

\[
 \phi''\asymp {Nh\over Z^3},\qquad
 w_Z=(\phi'')^{-1/2}\asymp\left({Z^3\over Nh}\right)^{1/2}.
\tag{140.R20}
\]

The cubic phase parameter is
\[
 {Nh\over Z^4}w_Z^3\ll\sqrt{Z/(Nh)},
\]
the profile variation is \(O(w_Z/Z)\), and the smooth collar variation
is \(O(w_Z/\Delta_h)\). Multiplication by the number
\(O(1+Nh/Z^2)\) of stationary aliases on a block leaves
\(O(1)\) local error. Off those neighborhoods, distance to the nearest
odd derivative alias gives a harmonic \(O(\log(2X))\) block sum; a
second integration makes the remote alias tails absolute because every
boundary derivative vanishes. There are \(O(\log(2X))\) physical
blocks.  This proves (140.R19); candidate equation (140.C19b) is the
same identity with the same normalization.

Summing its error over \(h\ll R\) gives

\[
 \sum_{h\ll R}{\log^2(2X)\over h}\ll\log^3(2X).
\tag{140.R21}
\]

The principal terms for which \(x_{h,r}\) lies in the smoothing ramp,
together with \(r_{2,h}\), have the already verified
\(O(R\log(2X))\) cost. The remaining principal terms are exactly
(140.R6). Thus (140.R19)--(140.R21) repair the complete
nonstationary, profile-crossing, transition, and stationary-remainder
ledger without relying on a conditionally convergent sharp series.

All literal repairs are also complete: (140.C4), the odd sum after
(140.C14), and (140.C25) contain clean TeX; empty rows are removed
before \(D_{i,h}\) or \(r_{2,h}\) is used; the prime-power fibre is
restricted to sufficiently large fourth-power centres and a fixed
nonzero profile range; and \(r=4h+s\) is correctly called an invertible
linear change.  The corrected multiplication in (140.C19e) is exactly
(140.R0).

The first genuinely unproved estimate is now exactly (140.C26),
equivalently (140.R7).

## 5. Controls and outcomes

| Seam | Outcome |
|---|---|
| Sharp half-endpoint and principal value | GREEN. (140.R8) proves the \(1/r\) boundary tail; the sharp series cannot be separated absolutely. |
| Exact floor and \(q\) threshold | GREEN. (140.R9) retains every floor, equality, parity, \(q=0\), and \(q=2y\) case. |
| Two-collar smoothing support | GREEN. The off-by-one choice in \(\Delta_h\) gives exactly (140.R12), with no new physical sample. |
| Cutoff/profile derivative norms | GREEN. Equation (140.R13) has the correct \(h^{-1}\), \((Rh)^{-1}\), and \(\Delta_h^{-1}\) factors. |
| Transition count and cost | GREEN. The full ramp has \(O(1+\sqrt h)\) aliases and costs \(O(R\log X)\). |
| \(r_{2,h}+2\) clean bulk | GREEN. The first clean alias is separately safe; the next odd alias is beyond the incomplete-Fresnel width. |
| Local stationary normalization | GREEN. Equations (140.R16)--(140.R17) reproduce the Gaussian constant, profile argument, and height power. |
| Nonlocal stationary and smooth nonstationary owners | GREEN. Candidate equations (140.C19a)--(140.C19f) reproduce (140.R19)--(140.R21), including the corrected transition multiplication and twice-integrated remote tails. |
| Exact product coefficient | GREEN. Equation (140.R18) includes the exact far mask and no spurious height weight. |
| Hessian and rational rays | GREEN. The determinant stays zero under \(r=4h+s\); the fourth-power ray is character-correct and only target-scale. |
| Exact and near radicals | GREEN scope. Exact radicals are target-safe; no near-radical estimate is claimed. |
| Directionality and downstream scope | GREEN. The only support change is a signed target-safe band before Poisson; no tail square, residual deletion, GAR, M1, M2, M9, quarter, or exponent result follows. |
| Artifact hygiene | GREEN. The patched candidate has zero forbidden control or carriage-return bytes, seven numbered sections, 38 matched display delimiters, no trailing whitespace, no conflict markers, and a clean diff check. |

## 6. Dependencies and artifacts audited

This review used only:

- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/candidates/conductor_round140_smoothed_far_alias_reduction.md;
- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/reports/exact_tail_poisson_alias_connector.md;
- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/reports/blind_height_alias_joint_feasibility.md;
- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/reports/tail_alias_hostile_directionality_audit.md.

The discovery report supplies the detailed smooth rowwise
\(B\)-process calculation; the blind report independently certifies the
sharp principal-value, rank-one, product-fibre, radical, and self-return
obstructions while deliberately leaving the owner lemma open; the
hostile primary report supplies the floor-based two-collar version and
the clean \(r_{2,h}+2\) interface. This review recomputed the seams
above rather than accepting any report by vote or deference.

No numerical experiment, web source, state file, sibling post-unmask
review, desired circle estimate, or unlisted theorem was used.

## 7. Recommended state effect

Mark this post-unmask hostile review **GREEN**.  The reduction
(140.C1)--(140.C6) may be considered for promotion subject to the other
independent seam reviews and mechanical State Patch validation.
The sharp principal-value obstruction, rank-one Hessian, exact
incomplete product coefficient, \(R^{3/2+o(1)}\) coefficient-blind
capacity, exact-radical upper bound, and second-transform self-return
may then be recorded with their stated scope.

Retain the far-family estimate (140.C26), the literal tail target, the
complete lower-radial signed estimate, lower GAR, both direct M1
parents, M9-M1, all M2 parents, endpoint uniformity, M9, the conditional
bridge, and the quarter theorem as open. Retain both recorded global
exponents unchanged.
