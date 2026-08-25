# Blind statement-only report: incomplete-fibre additive twist

Campaign: `m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate`
Task: `blind_incomplete_fibre_additive_twist`
Role: blind rederiver
Graph hash supplied in the brief: `072e08848e9d368d65b89fbf03c36423a8e3662e7ae61c48052d4c352d1d71b0`

## 1. Result

There is a strict target-safe reduction, followed by a rigorous additive-twist obstruction.  Put

\[
 C(m):=\sum_{\substack{hr=m,\ r\ {\rm odd}\\r>4h}}\chi _4(r)
      =\sum_{\substack{hr=m,\ r\ {\rm odd}\\r>2\sqrt m}}\chi _4(r).
\tag{1.1}
\]

For fixed \(0<\rho<1/8\) and the fixed profile in the statement,

\[
 \mathfrak T_N=
 \sum_{m\geq1}m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 +O_{\rho,V_{\rm low}}(\log(2X)).
\tag{1.2}
\]

Thus the exact floor-dependent mask can be replaced by the cone \(r>4h\), but not by the complete divisor fibre, and (1.2) keeps an error which is already \(O_\varepsilon(X^\varepsilon)\).

The proposed use of \(\chi _4\)-periodicity as cancellation meets the opposite phenomenon.  Uniformly for every fixed \(c_0>0\), whenever \(y\) is sufficiently large and \(2\leq M\leq c_0y\), the exact coefficient in (B141.1) satisfies

\[
 \sum_{m\leq M}A_\rho(m)e(m/4)
   ={i\pi\over8}M+O_{\rho,c_0}(M^{3/4}),
\tag{1.3}
\]

and consequently

\[
 \sum_{m\leq M}m^{-3/4}A_\rho(m)e(m/4)
   ={i\pi\over2}M^{1/4}+O_{\rho,c_0}(\log(2M)).
\tag{1.4}
\]

If \(V_{\rm low}=1\) on \([0,c_V]\), taking \(M\leq c_VZ/2\asymp_V y\) places this resonance wholly inside the flat part of the actual support.  In particular, the incomplete coefficient has a full-sized additive Fourier mode at frequency \(1/4\); it does not have cancellation uniformly in the additive frequency.  This is the first rigorous obstruction.  It is directly relevant because the local slopes of \(m\mapsto\sqrt{Nm}\), modulo integer slopes, pass through \(1/4\).  A canonical transform at those slopes produces the reciprocal phase \(Nh/d\), and a second transform returns the original square-root phase.  Neither (1.3) nor the transform supplies a lower bound for the fixed-centre scalar, because the different nonlinear cells retain their phases.  Hence (B141.3) is not proved here.

## 2. Exact statement and hypotheses

Write

\[
 Z={N\over R^2}={N\over\sqrt X}.
\tag{2.1}
\]

If the positive support of \(V_{\rm low}\) is contained in \([0,C_V]\), then every term has \(m\leq C_VZ\).  Since \(y\leq\sqrt X<y+1\) and \(y^2\leq N\leq y^2+2y\),

\[
 y-1<Z\leq y+2.
\tag{2.2}
\]

Thus all estimates below only require \(m\ll_V y\) and \(h<\sqrt m/2\ll_V\sqrt y\).  Bounded \(X\) is absorbed into the implied constant, so the claims are stated for sufficiently large \(y\).

Let \(\delta_h=L_h+1\), so \(D_h=y-\delta_h\) and

\[
 0<\delta_h\leq {\rho y\over\sqrt h}+1.
\tag{2.3}
\]

For each relevant row define

\[
 E_N(m):=\sum_{\substack{hr=m,\ r\ {\rm odd}\\4h<r\leq r_h}}\chi _4(r).
\tag{2.4}
\]

Then the exact identity is

\[
 A_\rho(m)=C(m)-E_N(m).
\tag{2.5}
\]

All row floors remain present in \(E_N\); no rounded threshold was silently substituted.  The displayed row data give \(D_h>L_h\) for large \(y\) (indeed \(L_h\leq\rho y\) and \(\rho<1/8\)), so the relevant rows \(h\ll\sqrt y\) are nonempty.  Profile-zero terms are still killed by the same factor \(V_{\rm low}(m/Z)\).

Besides (1.2)--(1.4), the additive obstruction implies the exact variation obstruction

\[
 \sum_{m<M}|A_\rho(m+1)-A_\rho(m)|\gg_{\rho,c_0}M
 \qquad( M\leq c_0y,\ M\to\infty).
\tag{2.6}
\]

Thus neither bounded variation nor a uniform power-saving hypothesis for additive partial sums can be assumed for this coefficient.  No external theorem, centre average, positivity statement, or downstream assertion is a hypothesis of these results.

## 3. Proof or derivation

First, an included pair obeys

\[
 r\geq r_h+2>{4Nh\over D_h^2}>4h,
\tag{3.1}
\]

because \(N\geq y^2\) and \(D_h\leq y-1\).  Since \(m=hr\), the inequality \(r>4h\) is equivalent to \(r>2\sqrt m\).  Odd integers occur in steps of two, so the terms in the cone which are absent from the exact mask are exactly those with \(4h<r\leq r_h\), proving (2.5).  Notice also that

\[
 m=hr>4h^2,\qquad h<\sqrt m/2.
\tag{3.2}
\]

For \(y\geq8\), (2.3) gives \(D_h\geq3y/4\).  With \(N=y^2+q\), \(0\leq q\leq2y\),

\[
\begin{aligned}
 {4Nh\over D_h^2}-4h
 &=4h{N-D_h^2\over D_h^2}\\
 &=4h{q+2y\delta_h-\delta_h^2\over D_h^2}\\
 &\ll h{1+\delta_h\over y}
 \ll_\rho \sqrt h+{h\over y}+1.
\end{aligned}
\tag{3.3}
\]

The least odd integer above a real number is less than that number plus two.  Hence, for \(h\ll_V\sqrt y\),

\[
 0<r_h-4h\ll_{\rho,V}\sqrt h+1.
\tag{3.4}
\]

Using \(r>4h\), boundedness of \(V_{\rm low}\), and then dropping its upper support only to majorize the correction,

\[
\begin{aligned}
 \sum_m m^{-3/4}|E_N(m)|\,|V_{\rm low}(m/Z)|
 &\leq \|V_{\rm low}\|_\infty
 \sum_{h\ll_V\sqrt y}h^{-3/4}
 \sum_{\substack{4h<r\leq r_h\\r\ {\rm odd}}}r^{-3/4}\\
 &\ll_{\rho,V}\sum_{h\ll_V\sqrt y}
 h^{-3/2}(\sqrt h+1)
 \ll_{\rho,V}\log(2y).
\end{aligned}
\tag{3.5}
\]

This proves (1.2), uniformly on every real-centre interval: \(N,y,L_h,D_h,r_h\) are constant there, while (3.5) is uniform in the continuously varying \(Z=N/\sqrt X\).

For the additive obstruction, first use the cone coefficient.  Put

\[
 S_C(M)=\sum_{m\leq M}C(m)e(m/4)
 =\sum_{4h^2<M}\ \sum_{\substack{4h<r\leq M/h\\r\ {\rm odd}}}
 \chi _4(r)e(hr/4).
\tag{3.6}
\]

If \(h\) is even, then \(e(hr/4)\) is constant as \(r\) runs through the odd integers, while the consecutive \(\chi _4(r)\)'s alternate; that row is \(O(1)\).  If \(h\) is odd, then for odd \(h,r\),

\[
 e(hr/4)=i\chi _4(hr)=i\chi _4(h)\chi _4(r),
\tag{3.7}
\]

so every summand in that row equals \(i\chi _4(h)\).  If \(H\asymp\sqrt M\) is the largest possible \(h\), the number of admissible odd \(r\)'s is

\[
 K_h={M\over2h}-2h+O(1).
\tag{3.8}
\]

Therefore

\[
 S_C(M)=i{M\over2}\sum_{\substack{h\leq H\\h\ {\rm odd}}}{\chi _4(h)\over h}
 -2i\sum_{\substack{h\leq H\\h\ {\rm odd}}}\chi _4(h)h+O(H).
\tag{3.9}
\]

Pairing \(4j+1\) with \(4j+3\) gives \(\sum_{h\leq H,\ h\ {\rm odd}}\chi _4(h)h=O(H)\).  Also

\[
 \sum_{\substack{h\leq H\\h\ {\rm odd}}}{\chi _4(h)\over h}
 =1-{1\over3}+{1\over5}-\cdots={\pi\over4}+O(H^{-1});
\tag{3.10}
\]

the value is elementary from \(\int_0^1(1+t^2)^{-1}\,dt\), and the error is the alternating-series remainder.  Equations (3.9)--(3.10) yield

\[
 S_C(M)={i\pi\over8}M+O(M^{1/2}).
\tag{3.11}
\]

For \(M\leq c_0y\), (3.3) gives, without weights,

\[
 \#\{(h,r):hr\leq M,\ r\ {\rm odd},\ 4h<r\leq r_h\}
 \ll_{\rho,c_0}\sum_{h\ll\sqrt M}(\sqrt h+1+h/y)
 \ll_{\rho,c_0}M^{3/4}.
\tag{3.12}
\]

Combining (2.5), (3.11), and (3.12) proves (1.3).  Abel summation of (1.3) against \(m^{-3/4}\) gives (1.4): the main term is four times \((i\pi/8)M^{1/4}\), while the error contributes \(O(1)+O(\int_1^M t^{-1}dt)\).  Finally, partial summation against the bounded partial sums of \(e(m/4)=i^m\) gives

\[
 \left|\sum_{m\leq M}A_\rho(m)e(m/4)\right|
 \ll |A_\rho(M)|+|A_\rho(1)|+
 \sum_{m<M}|A_\rho(m+1)-A_\rho(m)|.
\tag{3.13}
\]

Since \(|A_\rho(M)|\leq d(M)\leq2\sqrt M\), (1.3) implies (2.6).

The phase geometry explains why this bad additive frequency cannot simply be excluded.  For \(\Phi(h,r)=\sqrt{Nhr}\),

\[
 \det \nabla^2\Phi=0;
\tag{3.14}
\]

indeed the product of the two diagonal Hessian entries equals the square of the mixed entry.  Thus the Hessian has rank one.  Moreover, on all integers

\[
 \chi _4(r)={e(r/4)-e(-r/4)\over2i}.
\tag{3.15}
\]

For the plus sign in (3.15), a Poisson frequency \(k\) has stationary phase

\[
 \sqrt{Nhr}+{r\over4}-kr,\qquad
 r_0={4Nh\over(4k-1)^2},\qquad
 \Phi_k(r_0)={Nh\over4k-1}.
\tag{3.16}
\]

For the minus sign, \(4k-1\) is replaced by \(4k+1\).  At either saddle \(d=4k\mp1\),

\[
 (hr_0)^{-3/4}|\Phi_k''(r_0)|^{-1/2}
 =2N^{-1/4}h^{-1},
\tag{3.17}
\]

which is independent of \(d\).  The canonical image is therefore a reciprocal phase \(e(Nh/d)\), with the mod-four character reappearing between the two residue classes.  A second stationary transform of \(Nh/d\) uses

\[
 {d\over dd}(Nh/d+jd)=0
 \quad\Longrightarrow\quad
 d_0=\sqrt{Nh/j},\qquad Nh/d_0+jd_0=2\sqrt{Nhj},
\tag{3.18}
\]

which is the original square-root phase with \(r=4j\), followed by the same mod-four splitting.  Equations (3.16)--(3.18) are the exact stationary equations and amplitude calculation; they are not asserted to be a completed Poisson formula with all endpoint errors.

## 4. First doubtful or unproved step

After (1.2), the remaining target is exactly the cone scalar

\[
 \sum_{h\geq1}\sum_{\substack{r>4h\\r\ {\rm odd}}}
 (hr)^{-3/4}V_{\rm low}(hr/Z)\chi _4(r)e(\sqrt{Nhr})
 \ll_\varepsilon X^\varepsilon.
\tag{4.1}
\]

The first unproved step is a fixed-centre, local estimate for (4.1) which treats the quarter-frequency survivor in (1.3), rather than assuming it cancels.  On a smooth dyadic block, a first canonical transform would require control of a dual expression of the shape

\[
 N^{-1/4}\sum_h{1\over h}
 \sum_{\substack{d\ {\rm odd}\\d\ {\rm in\ the\ exact\ dual\ endpoints}}}
 \chi _4(d)\,\mathcal W(h,d)e(Nh/d),
\tag{4.2}
\]

where the endpoints and \(\mathcal W\) must be derived from \(r>4h\), \(V_{\rm low}(hr/Z)\), and all endpoint saddles.  No estimate for (4.2), and no target-safe estimate for the nonstationary complement, follows from the statement.  Transforming (4.2) a second time merely gives (3.18), so doing so without a new arithmetic input is circular.

Equivalently, a one-dimensional derivative theorem applied in \(m\) would need either controlled variation of \(A_\rho(m)\) or additive partial sums uniform at the local linear frequencies.  Equation (2.6) rules out small variation, while (1.3) rules out even an \(o(M)\) uniform additive bound.  A tailored theorem could still isolate the quarter mode and exploit cancellation of the reciprocal phases, but that theorem and its hypotheses are precisely the missing step.

This obstruction is not a scalar lower bound.  The direction \(i\) in (1.3) is a coefficient Fourier direction; multiplying by the nonlinear residual phases in distinct cells can rotate and cancel it.  Consequently neither modulus, positive energy, nor a same-sign subfibre can decide (4.1).

## 5. Control tests and outcomes

1. **`exact_incomplete_fibre_mask_floors_profiles_and_real_centre` — pass.**  Equations (2.4)--(3.5) retain every \(L_h,D_h,r_h\) floor in \(E_N\), prove its weighted contribution is \(O(\log X)\), and are uniform as real \(X\) moves while \(N,y\) are fixed.  The same profile factor is retained, so profile-zero terms remain zero.

2. **`dyadic_m_range_weight_and_small_m_owner` — pass with an open main owner.**  The support is \(m\leq C_VZ\ll_Vy\); on \(M\leq m<2M\), the weight is \(\asymp M^{-3/4}\), and (3.2) gives \(h<\sqrt{2M}/2\).  The elementary bound \(|A_\rho(m)|\leq d(m)\ll_\varepsilon m^\varepsilon\) gives only \(M^{1/4+\varepsilon}\) on a dyadic block, which is not target-safe at the upper range.  Finitely many bounded \(m\) are target-safe, but all growing small and middle dyadic ranges remain owned by (4.1); they were not silently deleted.

3. **`chi4_parity_divisor_pairing_and_complete_fibre_comparison` — obstruction.**  Every included pair has \(r>4h\).  Its swapped pair has the wrong cone inequality, and if \(h\) is even it is not even a nonzero \(\chi _4\)-term.  The exact complete coefficient is
   \[
   \sum_{r\mid m}\chi _4(r)
   =C(m)+\sum_{\substack{hr=m,\ r\ {\rm odd}\\r\leq4h}}\chi _4(r),
   \]
   whose second term has not been proved target-safe.  Thus there is no half-fibre identity.  More strongly, (3.7)--(3.11) show that parity creates a main term at additive frequency \(1/4\), rather than cancellation.

4. **`phase_cell_definition_width_multiplicity_and_endpoints` — pass as a definition, no estimate smuggled in.**  For phase-value cells, define
   \[
   \vartheta_N(m)=\sqrt{Nm}-\lfloor\sqrt{Nm}+1/2\rfloor\in[-1/2,1/2)
   \]
   and, for an integer \(J\geq1\), use the half-open cells
   \[
   \mathcal C_{M,j}=\{M\leq m<2M:-\tfrac12+\tfrac jJ
      \leq\vartheta_N(m)<-\tfrac12+\tfrac{j+1}{J}\},
      \quad0\leq j<J.
   \]
   Their width is exactly \(1/J\), their multiplicity is
   \(\mu_{M,j}=\#\mathcal C_{M,j}\), and their weighted absolute capacity is at most
   \(M^{-3/4+\varepsilon}\mu_{M,j}\).  No nontrivial bound for \(\mu_{M,j}\) is supplied by the statement.

   The relevant quarter-slope cells are distinct from these value cells.  For
   \(F(x)=\sqrt{Nx}-x/4\), their centres are
   \[
   x_k={N\over4(k+1/4)^2}={4N\over(4k+1)^2},
   \qquad F'(x_k)=k.
   \]
   On \([M,2M)\), there are \(O(1+\sqrt{N/M})\) such centres.  With a sufficiently small absolute \(c>0\), take the explicit half-open cores
   \[
   [M,2M)\cap[x_k-\Delta_M,x_k+\Delta_M),\qquad
   \Delta_M=c\min(M^{3/2}N^{-1/2},M^{3/4}N^{-1/4}).
   \]
   The first scale is at most a fixed fraction of adjacent-centre spacing, so multiplicity is at most one; the second makes the quadratic Taylor variation \(O(1)\).  Endpoint truncation is explicit.  At \(M\asymp\sqrt N\), their total absolute weighted capacity is \(O_\varepsilon(N^\varepsilon)\), but this says nothing about the complement or lower dyadic ranges.

5. **`exact_radical_versus_near_radical_separation` — pass.**  Write uniquely \(N=Du^2\) with \(D\) squarefree.  Valuations show
   \[
   Nm\text{ is a square}\quad\Longleftrightarrow\quad m=Dt^2.
   \]
   Hence the exact-radical absolute contribution is
   \[
   \ll_\varepsilon\sum_t(Dt^2)^{-3/4+\varepsilon}\ll_\varepsilon X^\varepsilon.
   \]
   For a near radical, with \(n=\lfloor\sqrt{Nm}+1/2\rfloor\), one instead has a nonzero integer
   \[
   Nm-n^2=\vartheta_N(m)(\sqrt{Nm}+n),
   \]
   so counting it requires incomplete solutions of \(n^2\equiv-(Nm-n^2)\pmod N\) in exact short ranges.  The exact-radical argument supplies no such estimate.

6. **`nonresonant_complement_target_return` — obstruction.**  Removing the explicitly defined resonant cores does not prove that the complement is target-safe.  Summation by parts meets (1.3) and (2.6); canonical transformation meets (4.2), and a second transformation returns (3.18).  Thus the complement estimate is the original missing cancellation in another coordinate system.

7. **`fourth_power_rays_and_prime_square_fibres` — pass as hostile controls only.**  For every sufficiently large odd prime \(p\), the only possible included divisor pair for \(m=p^2\) is \((h,r)=(1,p^2)\), so
   \[
   A_\rho(p^2)=\chi _4(p^2)=1.
   \]
   If \(p\equiv1\pmod4\), every included term on the ray \(m=p^{4j}\) also has sign \(+1\).  When \(N\) is a square these phases equal one.  Nevertheless \(\sum_p p^{-3/2}\) and \(\sum_j(4j+1)p^{-3j}\) converge, so these controls refute automatic fibrewise cancellation but do not lower-bound the full scalar.

8. **`coefficient_variation_or_additive_partial_sum_hypothesis` — fail for the generic hypothesis.**  Equations (1.3) and (2.6) give respectively a linear additive partial sum at \(1/4\) and linear total variation.  Any usable imported one-dimensional theorem must explicitly allow and then estimate this resonant mode; its standard uniform-cancellation or low-variation hypothesis is false here.

9. **`canonical_transform_self_return_and_circularity` — pass as an obstruction.**  Equations (3.16)--(3.18) give the reciprocal phase, constant-in-\(d\) saddle amplitude, and exact phase return.  A transform alone is invertible bookkeeping, not a saving.

10. **`fixed_centre_signed_directionality` — pass.**  The obstruction (1.3) holds separately for each fixed \(N,y\) in the relevant range and has the signed direction \(i\).  No averaging over centres or absolute-value replacement was used.  The report also does not turn that direction into a scalar lower bound, because the nonlinear cell phases remain.

11. **`lower_GAR_and_downstream_scope` — pass.**  The statement-only packet supplies no independent lower_GAR implication, and none is asserted.  Even a proof of (B141.3) would concern only the frozen scalar.  This report proves only (1.2)--(1.4) and the associated no-go; it proves no residual deletion, M1/M2 statement, endpoint theorem, global quarter theorem, or exponent change.

## 6. Dependencies and exact artifacts used

The only mathematical context used was:

- `protocol.md`;
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/briefs/blind_incomplete_fibre_additive_twist.md` (assignment and isolation rules);
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/blind_statement.md` (the complete statement-only mathematical packet).

No excluded state, strategy file, Round-137--Round-141 nonblind artifact, sibling report, web source, numerical computation, or symbolic computation was inspected or used.  The only auxiliary facts used were proved above or were the elementary divisor bound, alternating-series estimate, and Abel summation.

## 7. Recommended state effect

**Retain** (1.2) as a candidate exact floor-to-cone reduction and retain (1.3)--(1.4) as the first rigorous obstruction, subject to independent seam review of the row convention and endpoint uniformity.  **Reject** any route which invokes \(\chi _4\)-periodicity, generic coefficient variation, or uniform additive partial-sum cancellation without first extracting the quarter-frequency survivor.  Leave the fixed-centre scalar target open: the required reciprocal-phase or nonlinear phase-cell cancellation has not been proved.  No shared proof state should be changed from this blind report alone.
