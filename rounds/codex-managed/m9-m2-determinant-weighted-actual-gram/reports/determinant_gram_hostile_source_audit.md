# Round 102 hostile/source audit: the stationary determinant is only a carrier curvature

Campaign: m9-m2-determinant-weighted-actual-gram

Task: determinant_gram_hostile_source_audit

Role: hostile mathematical and primary-source auditor

Status: candidate evidence only; no shared proof state is edited.

## 1. Result

**Determinant-carrier no-go, exact normalization, and strict short-ray
survivor.**  No literal actual-symbol gain is certified.

For the zero-extended fixed-\(a\) row, put

\[
 E_{\rm act}:=\sum_{a,q}|F_a(q)|^2,\qquad
 C_h:=\sum_{a,q}F_a(q+h)\overline{F_a(q)}.
\]

The Gram in the frozen target has the exact expansion

\[
 \boxed{\mathcal G_H^{\rm act}
 =H E_{\rm act}
 +2\Re\sum_{1\le h<H}(H-h)(-1)^h C_h.}
 \tag{102.H1}
\]

Thus the diagonal is not an independently disposable error if
\(\rho>D_{\rm ray}\): it must be cancelled by the signed, complete
nonzero-shift correlations, or it must itself enjoy a new actual-symbol
energy saving.  Estimating the diagonal separately gives at most the
already known \(D_{\rm ray}^{-1/2}\) linear gain.

There is a sharper disjoint obstruction.  On a half-open \(q=1\),
\(D_{\rm ray}\asymp1\) block the row contains one point.  In the
unit-\(q\)-scale convention the only lawful averaging length is \(H=1\),
and hence

\[
 \mathcal G_1^{\rm act}=E_{\rm act},\qquad
 E_{\rm act}\stackrel{\rm target}{\ll_\varepsilon}
 X^\varepsilon E_0/\rho.
 \tag{102.H2}
\]

If the alternative \(b-a\) convention permits another bounded \(H\), all
nonzero \(C_h\) still vanish and
\(\mathcal G_H^{\rm act}=HE_{\rm act}\); this changes only a fixed
constant in (102.H2).  The near-square/Pell controls show that this
subrange can be primitive,
nonsquare, strictly metric, recurrent at fourth powers, and have
\(\rho\to\infty\).  Therefore a mechanism whose only new input is
separation of a nonzero-shift determinant cannot prove the full frozen
Gram.  This does not disprove (102.H2), because no lower bound for the
complete physical coefficient is known.  It isolates (102.H2) as the
first strict actual-symbol survivor.

For \(D_{\rm ray}>1\), writing

\[
 \lambda_a(q):={(\sqrt{a+2q}-\sqrt a)^2\over2},
 \qquad \theta_{a,q,k}:={X\lambda_a(q)\over k},
 \tag{102.H3}
\]

the exact carrier extracted from
\(\mathfrak C^\circ=e(-g\theta/2)\mathfrak B^\circ\) has cross-phase
curvature

\[
 \Phi''(q)=-{X\sqrt a\over2}\Delta,\qquad
 \Delta=
 {g'\over k'(a+2q+2h)^{3/2}}
 -{g\over k(a+2q)^{3/2}}.
 \tag{102.H4}
\]

This algebra is correct, including the factor \(X\sqrt a/2\), but
\(\Delta\) is only the curvature of the extracted saddle carrier.  It is
not a Hessian determinant for the complete moving Gram.  The multiplier
still contains two independently moving metric windows, exact centred
entry/exit integrals, primitive and prior-owner masks, \(k\)- and
\(g\)-support boundaries, profiles, floors, stars, collars, and both
orientations.  Round 77 gives variation in the odd lift \(g\), not
bounded variation in \(q\).  Consequently no second-derivative estimate
on (102.H4) applies to the literal row without a new \(q\)-variation or
direct complete-integral theorem.

Even the bare algebraic separation is too fine.  Away from
\(\Delta=0\), rationalization gives only

\[
 |\Delta|\gg (G K_{\rm rec}^3 A^{9/2})^{-1},
 \qquad
 |\Phi''|\gg (LJD_{\rm ray}^3)^{-1},
 \tag{102.H5}
\]

at the active scales \(G\asymp L/A\) and
\(K_{\rm rec}\asymp JD_{\rm ray}/A\).  Across a \(q\)-interval of length
\(D_{\rm ray}\), this lower bound gives
\(|\Phi''|D_{\rm ray}^2\gg (LJD_{\rm ray})^{-1}\), far below one.
Algebraicity alone therefore supplies no oscillatory saving.

The exact-zero locus is nonempty at the geometric level and is not the
same as a square-ray or exact-metric-centre owner.  More generally, the
natural unresolved nonzero-shift object is the signed complete
near-determinant package

\[
\begin{aligned}
 \mathscr R_H^{\rm near}(\tau_0):={}&H E_{\rm act}\\
 &+2\Re\sum_{1\le h<H}(H-h)(-1)^h
 \sum_{a,q}\sum_{\substack{(k,g),(k',g')\\
                         |\Delta|\le\tau_0}}
 Z_{a,q+h;k',g'}\,
 \overline{Z_{a,q;k,g}},
\end{aligned}
\tag{102.H6}
\]

where \(Z\) is the literal component of \(F\), with every mask and actual
coefficient retained, and

\[
 \tau_0:={c\over X\sqrt A\,D_{\rm ray}^2}.
 \tag{102.H7}
\]

At this threshold the carrier has at most order-one quadratic phase
change across the whole row.  Even if the complementary separated locus
were granted at target size, (102.H6) would still have to satisfy

\[
 \mathscr R_H^{\rm near}(\tau_0)
 \ll_\varepsilon X^\varepsilon {H^2E_0\over\rho}.
 \tag{102.H8}
\]

No selected input, and no literally matching primary theorem, proves
(102.H2) or (102.H8).  The full Gram, every hard subrange, the canonical
M2 density--discrepancy energy, and all downstream estimates remain open.

## 2. Exact statement and hypotheses

Let \(e(t)=e^{2\pi i t}\).  Work on one residual hard top block with

\[
 a\asymp A,\qquad q\asymp D_{\rm ray},\qquad
 b=a+2q\asymp A,\qquad
 k\asymp K_{\rm rec}\asymp {JD_{\rm ray}\over A},
 \qquad g\asymp G\asymp {L\over A},
 \tag{102.H9}
\]

and

\[
 E_0\asymp_{X^\varepsilon}LJD_{\rm ray}^2,\qquad
 \rho={AJD_{\rm ray}^3\over L^3}>1,\qquad
 1\le H\le D_{\rm ray}.
 \tag{102.H10}
\]

Here \(D_{\rm ray}\) may denote either the dyadic \(q\)-scale or the
\(b-a\)-scale; the two differ by the harmless fixed factor two.  All
claims below are invariant under that convention.

For each \(a,q\), let \(\mathscr T_{a,q}\) be the exact finite set of
internal labels, including at least \(k,g\), satisfying

\[
 {J(\sqrt{a+2q}-\sqrt a)\over2\sqrt a}
 <k<
 {J(\sqrt{a+2q}-\sqrt a)\over\sqrt{a+2q}},
 \tag{102.H11}
\]

the finite odd-lift support, the primitive mask, every accepted prior
owner, the residual block masks, and zero extension.  Define

\[
 Z_{a,q;k,g}
 :=\omega_{a,q,g,k}\,
 W_R(\theta_{a,q,k})\,
 \mathfrak C^\circ_{a,a+2q,k}(g),
 \qquad
 F_a(q)=\sum_{(k,g)\in\mathscr T_{a,q}}Z_{a,q;k,g}.
 \tag{102.H12}
\]

The notation \(\omega\) retains both orientations, profiles, floors,
stars, signs, collars, and every owner.  The coefficient
\(\mathfrak C^\circ\) is the complete physical entry/exit integral.  In
particular, (102.H12) does not replace any factor by a bounded arbitrary
coefficient.

The hostile result consists of the following literal assertions.

1. **Gram assertion.**  Equation (102.H1) is exact with zero extension.
   If

   \[
   M_0^2\asymp_{X^\varepsilon}GJD_{\rm ray},\qquad
   N\asymp AD_{\rm ray},
   \tag{102.H13}
   \]

   are the accepted envelope and ray count, then

   \[
   E_0=NM_0^2,\qquad
   P:=NM_0=L^2\sqrt\rho
   \tag{102.H14}
   \]

   up to \(X^\varepsilon\).  The frozen Gram target is exactly the
   squared-scale input that returns the linear block target \(L^2\).

2. **Carrier-curvature assertion.**  On an elementary nonzero-shift
   product with \(b'=b+2h\), fixed internal labels \(k,g,k',g'\), and
   exact factorization

   \[
   \mathfrak C^\circ_{a,b,k}(g)
   =e(-g\theta_{a,q,k}/2)\mathfrak B^\circ_{a,b,k}(g),
   \tag{102.H15}
   \]

   the extracted carrier has (102.H4).  No assertion is made that the
   remaining product of \(\mathfrak B^\circ\), windows, or masks is a
   slowly varying \(q\)-amplitude.

3. **Exact-zero assertion.**  For positive integral \(b,b',g,g',k,k'\),
   \(\Delta=0\) if and only if there are a squarefree \(d\) and positive
   integers \(u,v\) such that

   \[
   b=du^2,\qquad b'=dv^2,\qquad
   g'ku^3=gk'v^3.
   \tag{102.H16}
   \]

   The primitive and square-ray owners do not, as algebraic statements,
   imply the negation of (102.H16).

4. **Nonzero-spacing assertion.**  If \(\Delta\ne0\), then the exact
   integer rationalization in Section 3 gives (102.H5).  This is only a
   lower bound; it does not count how often \(\Delta\) is near zero and
   does not weight incidences by (102.H12).

5. **Short-ray assertion.**  If a half-open \(D_{\rm ray}\asymp1\) block
   contains only \(q=1\), then every nonzero \(C_h\) vanishes.  With the
   unit-\(q\)-scale convention \(H=1\) and the target is exactly
   (102.H2); any other fixed-factor convention changes only a bounded
   factor.  A proof must use the actual coefficient or an already
   accepted owner, because determinant separation is vacuous.

6. **Scope assertion.**  The result is a no-go for the proposed
   determinant-only mechanism, algebraic spacing alone, a separately
   estimated diagonal, and coefficient-uniform analogues.  It is not a
   lower bound for \(\mathcal G_H^{\rm act}\) and not a counterexample to
   the actual Gram theorem.

## 3. Proof or derivation

Expanding the square and putting \(h=s-r\) gives

\[
\begin{aligned}
\mathcal G_H^{\rm act}
 &=\sum_{a,n}\sum_{0\le r,s<H}
   (-1)^{r+s}F_a(n+r)\overline{F_a(n+s)}\\
 &=H\sum_{a,q}|F_a(q)|^2
   +2\Re\sum_{1\le h<H}(H-h)(-1)^h
     \sum_{a,q}F_a(q+h)\overline{F_a(q)}.
\end{aligned}
\]

Every endpoint, owner crossing, and empty fiber is included because
\(F_a\) is zero-extended.  This proves (102.H1); it does not make any
shifted support rectangular.

To check the target normalization, put \(z_{a,q}=(-1)^qF_a(q)\).  For a
row supported on \(O(D_{\rm ray})\) integers,

\[
 H\sum_q z_{a,q}
 =\sum_n\sum_{0\le r<H}z_{a,n+r}.
\]

Cauchy over the \(O(D_{\rm ray}+H)\) nonempty windows and then over
\(O(A)\) values of \(a\) gives

\[
 \left|\sum_{a,q}(-1)^qF_a(q)\right|^2
 \ll {A(D_{\rm ray}+H)\over H^2}\,
       \mathcal G_H^{\rm act}.
 \tag{102.H17}
\]

Substituting the frozen target and \(H\le D_{\rm ray}\) yields

\[
 {AD_{\rm ray}\over H^2}
 \cdot {H^2E_0\over\rho}
 \asymp
 {AD_{\rm ray}\,LJD_{\rm ray}^2
  \over AJD_{\rm ray}^3/L^3}
 =L^4.
 \tag{102.H18}
\]

Thus every displayed \(H,E_0,\rho\) power in the target is necessary for
the intended \(L^2\) linear conclusion.

On the other hand, if the diagonal in (102.H1) is estimated separately,
its envelope is \(HE_0\).  Fitting that term alone inside the target
requires

\[
 HE_0\ll {H^2E_0\over\rho},\qquad\hbox{hence}\qquad
 H\gg\rho.
 \tag{102.H19}
\]

Since \(H\le D_{\rm ray}\), this route has capacity only when
\(\rho\ll D_{\rm ray}\).  Taking the maximal \(H\asymp D_{\rm ray}\) in
(102.H17) shows the squared gain \(D_{\rm ray}^{-1}\), hence the linear
gain \(D_{\rm ray}^{-1/2}\).  Signed nonzero correlations can cancel the
diagonal inside the exact square, but proving that cancellation is a new
actual-symbol theorem, not a benefit supplied by determinant separation.

For \(D_{\rm ray}\asymp1\), the half-open \(q\)-block has one point, so
all nonzero-shift correlations vanish.  Taking the lawful \(H=1\),
equations (102.H1) and (102.H19) reduce to (102.H2); a convention allowing
another bounded \(H\) yields the same required \(\rho^{-1}\) energy gain
up to a fixed factor.  The
primitive near-square family

\[
 (a,b)=(m-1,m+1),\qquad q=1,\qquad m\ {\rm even},
 \tag{102.H20}
\]

is nonsquare, and the Pell subfamily \(m^2-3n^2=1\) includes
\((a,b)=(25,27)\).  With \(A\asymp L\), \(D_{\rm ray}\asymp1\), one has

\[
 \rho\asymp {J\over L^2}\longrightarrow\infty.
 \tag{102.H21}
\]

The selected Round-80 control takes \(X=T^4\), \(J=T^2\),
\(k=T^2/32\) and obtains

\[
 \theta=32(26-15\sqrt3)T^2.
 \tag{102.H22}
\]

For each fixed strict metric annulus, Weyl's theorem gives infinitely
many recurrent \(T\).  This proves that short rays are not removed by a
generic metric or fourth-power premise.  It supplies no lower bound for
\(\mathfrak C^\circ\), which is why (102.H2), rather than a contradiction
to it, is the correct survivor.

It remains to verify the determinant.  Directly from (102.H3),

\[
 \lambda_a(q)=a+q-\sqrt{a(a+2q)},\qquad
 \lambda_a'(q)=1-\sqrt{a\over a+2q},
\]

\[
 \lambda_a''(q)={\sqrt a\over(a+2q)^{3/2}},\qquad
 \lambda_a'''(q)=-{3\sqrt a\over(a+2q)^{5/2}}.
 \tag{102.H23}
\]

For the cross carrier

\[
 \Phi(q)=
 -{g'X\lambda_a(q+h)\over2k'}
 +{gX\lambda_a(q)\over2k},
 \tag{102.H24}
\]

equation (102.H23) gives (102.H4), up to the immaterial reversal of both
signs caused by conjugating the orientation.  A bound stated only in
terms of \(|\Delta|\) misses the actual curvature multiplier
\(X\sqrt a/2\).

The exact-zero classification follows by squaring the equality

\[
 g'k\,b^{3/2}=gk'\,{b'}^{3/2}.
 \tag{102.H25}
\]

It forces \(b'/b\) to be a rational square, hence \(b=du^2\) and
\(b'=dv^2\) for one squarefree \(d\).  Cancelling \(d^{3/2}\) gives the
last equality in (102.H16), and the converse is immediate.

The locus is not formal only.  For example, take

\[
 a=367,\quad b=529=23^2,\quad b'=625=25^2,\quad
 q=81,\quad h=48,\quad g=23,\quad g'=27,
 \tag{102.H26}
\]

and, for a positive integer \(T\),

\[
 k=359375T=23\cdot25^3T,\qquad
 k'=328509T=27\cdot23^3T,\qquad
 J=2152500T.
 \tag{102.H27}
\]

Then \((a,b)=(a,b')=1\), neither \(ab\) nor \(ab'\) is a square, and

\[
 {g\over kb^{3/2}}
 ={g'\over k'{b'}^{3/2}}
 ={1\over T\,23^3 25^3}.
 \tag{102.H28}
\]

Both reciprocal intervals are strict.  Dividing (102.H11) by \(T\), the
four relevant bounds are

\[
 215885.23\ldots<359375<359631.83\ldots,
\]

\[
 328244.81\ldots<328509<503061.28\ldots.
 \tag{102.H29}
\]

The inequalities can equivalently be verified exactly by squaring
positive expressions involving \(\sqrt{367}\).  For large \(T\), the top
frequency ceiling \(H_{\rm top}\le\sqrt J\) can contain the fixed lift
labels.  Taking \(T=2152500s^2\) makes \(X=J^2\) a fourth power.  This is
an exact determinant-incidence control only: the remaining prior-owner
masks, dyadic profiles, strict metric window, and the value of the
physical integral must still be checked before claiming nonzero actual
mass.

If (102.H25) fails, rationalization gives

\[
\begin{aligned}
 |\Delta|
 &={|g'k\,b^{3/2}-gk'\,{b'}^{3/2}|
    \over kk'(bb')^{3/2}}\\
 &={|(g'k)^2b^3-(gk')^2{b'}^3|
    \over
    kk'(bb')^{3/2}
    \{g'k\,b^{3/2}+gk'\,{b'}^{3/2}\}}\\
 &\ge
 {1\over
    kk'(bb')^{3/2}
    \{g'k\,b^{3/2}+gk'\,{b'}^{3/2}\}}.
\end{aligned}
\tag{102.H30}
\]

At (102.H9) this is
\((G K_{\rm rec}^3A^{9/2})^{-1}\).  Multiplication by
\(X\sqrt A\), followed by
\(K_{\rm rec}\asymp JD_{\rm ray}/A\) and \(G\asymp L/A\), gives

\[
 X\sqrt A\,|\Delta|
 \gg {J^2\sqrt A\over
          (L/A)(JD_{\rm ray}/A)^3A^{9/2}}
 ={1\over LJD_{\rm ray}^3}.
 \tag{102.H31}
\]

This proves (102.H5).  The natural quadratic-oscillation threshold is
\(X\sqrt A|\Delta|D_{\rm ray}^2\asymp1\), namely (102.H7), so (102.H31)
is much too weak.

At an exact zero with \(h>0\), fixed labels do give a simple crossing:
if
\[
 t={g\over kb^{3/2}}
   ={g'\over k'{b'}^{3/2}},
\]
then
\[
 {d\Delta\over dq}
 =3t\left({1\over b}-{1\over b'}\right)>0.
 \tag{102.H32}
\]

Thus the zero is not an identically flat phase for fixed labels.  But a
third-derivative estimate near (102.H32), including its scale for
\(h=1\), would be another theorem and still requires control of the
complete moving multiplier.  Merely naming exact zeros does not estimate
their signed coefficient mass.

Finally, the multiplier is not a lawful slow amplitude.  The endpoints
of (102.H11) move by

\[
 {d\over dq}{J(\sqrt{a+2q}-\sqrt a)\over2\sqrt a}
 ={J\over2\sqrt{a(a+2q)}}\asymp {J\over A},
\]

\[
 {d\over dq}{J(\sqrt{a+2q}-\sqrt a)\over\sqrt{a+2q}}
 ={J\sqrt a\over(a+2q)^{3/2}}\asymp {J\over A}.
 \tag{102.H33}
\]

A shift \(h\) can therefore gain or lose
\(O(1+Jh/A)\) reciprocal modes.  Lift endpoints move on scale
\(O(1+Lh/A^2)\).  Also

\[
 {d\theta_{a,q,k}\over dq}
 ={X\over k}\left(1-\sqrt{a\over a+2q}\right)
 \asymp J
 \tag{102.H34}
\]

on the active \(k\)-scale.  Hence the strict metric factor is not slowly
varying in \(q\).  Primitive and owner masks jump, and the centred saddle
can enter or leave a physical collar.  Round 77 controls those transitions
for the exact integral and its \(g\)-variation, but proves no \(q\)-BV
bound.  Zero extension makes (102.H1) exact; it does not remove any term
in (102.H33)--(102.H34).

Expanding each \(C_h\) using (102.H12), splitting at (102.H7), and keeping
the diagonal intact yields (102.H6).  Therefore (102.H2) on the disjoint
short block and (102.H8) on longer blocks are the smallest literal
actual-symbol survivors left by an ideal separated-determinant estimate.

## 4. First doubtful or unproved step

The first doubtful step in any positive determinant argument is the
passage from the exact factorization (102.H15) to a scalar
second-derivative estimate in \(q\).  The phase derivative (102.H4) is
exact, but the proposed amplitude is

\[
\begin{aligned}
 &\mathbf1_{\mathscr T_{a,q+h}}(k',g')\,
  \mathbf1_{\mathscr T_{a,q}}(k,g)\,
  W_R(\theta_{a,q+h,k'})
  W_R(\theta_{a,q,k})\\
 &\qquad\times
 \mathfrak B^\circ_{a,a+2q+2h,k'}(g')\,
 \overline{\mathfrak B^\circ_{a,a+2q,k}(g)}
\end{aligned}
\tag{102.H35}
\]

together with profiles, floors, stars, signs, both orientations, and
entry/exit ownership.  No selected lemma bounds its \(q\)-variation at a
scale that permits partial summation.  Replacing it by a common bounded
coefficient, a same-\(k\) or same-\(g\) product, a rectangular overlap,
or a stationary leading term would change the theorem.

Before that analytic seam can even matter on every block, one must prove
the determinant-free short-ray estimate

\[
 \boxed{\sum_{\substack{a\\q=1}}|F_a(1)|^2
 \ll_\varepsilon X^\varepsilon {E_{0,\rm short}\over\rho}.}
 \tag{102.H36}
\]

This is the strictest disjoint survivor because no shifted correlation
exists there.  It must come from the complete actual symbol or a new
lawful owner.  The Pell/fourth-power control forbids declaring the block
empty merely from primitivity, nonsquareness, or metric recurrence.

For \(D_{\rm ray}>1\), a positive route would additionally need both:

\[
 \mathscr S_H^{\rm sep}(\tau_0)
 \ll_\varepsilon X^\varepsilon {H^2E_0\over\rho}
 \quad\hbox{with the literal multiplier (102.H35),}
 \tag{102.H37}
\]

and the signed near package (102.H8).  An incidence count for
\(|\Delta|\le\tau_0\) is not enough: density and discrepancy are coupled,
and the target is coefficient-weighted and signed.  Conversely, taking
absolute values in (102.H8) prevents the negative correlation needed to
cancel the diagonal when \(\rho>D_{\rm ray}\).

No primary result in the selected source maps supplies (102.H36),
(102.H37), or (102.H8).  The first missing mathematical input is therefore
an actual-symbol short-ray energy theorem, followed on longer rows by a
joint \(q,k,g\), near-determinant signed correlation theorem with owner and
entry/exit uniformity.

## 5. Required control tests, outcomes, and primary-source hypothesis map

| Required control | Exact test | Outcome |
|---|---|---|
| literal_fixed_a_row | Expanded the zero-extended fixed-\(a\) row in (102.H1), with shifts \(q\mapsto q+h\). | Pass; the sign is exactly \((-1)^h\). |
| complete_actual_symbol | Defined \(Z\) by (102.H12), retaining \(W_R\mathfrak C^\circ\) and every multiplier. | Pass for the no-go; no actual gain is inferred. |
| primitive_and_prior_owner_masks | Kept the product of the two masks in (102.H35). | Pass; an owner at either endpoint deletes that term, and no translation invariance is assumed. |
| moving_k_and_g_intervals | Differentiated the literal open \(k\)-endpoints in (102.H33) and retained independent \(k,k',g,g'\). | Pass; same-\(k\), same-\(g\), or rectangular replacement is unlawful. |
| metric_density_discrepancy_jointness | Kept the product of the two complete \(W_R\)'s in (102.H35). | Pass; neither the density mode nor mixed density--discrepancy products are dropped. |
| exact_Gram_and_diagonal | Proved (102.H1), (102.H17), and (102.H19). | Pass; separate diagonal capacity is only \(D_{\rm ray}^{-1/2}\) linearly. |
| determinant_separated_locus | Derived the exact carrier curvature (102.H4) and the natural threshold (102.H7). | Algebra passes; a literal separated estimate fails at the unproved \(q\)-variation seam (102.H35). |
| near_determinant_incidence | Proved the exact-zero classification (102.H16), the exact control (102.H26)--(102.H29), the nonzero lower bound (102.H30), and the simple crossing (102.H32). | Pass as algebra; neither incidence nor actual coefficient mass is bounded at target scale. |
| D_ray_one_and_q_one | Set \(H=1\) on the one-point block. | Determinant mechanism is vacuous; the strict survivor is (102.H36). |
| Pell_and_near_square | Used \((25,27)\) in the \(q=1\) Pell family. | Pass; the block is primitive, nonsquare, constant-sign, and can have \(\rho\to\infty\). |
| fourth_power_recurrence | Used (102.H22); also noted the exact-zero family can be placed at fourth powers by the indicated scaling. | Pass qualitatively at fixed metric width; no shrinking-window rate or coefficient lower bound. |
| entry_exit_and_zero_extension | Retained \(\mathfrak C^\circ\), physical collars, and zero extension, and audited support motion. | Pass for exact bookkeeping; zero extension does not make the multiplier smooth. |
| arbitrary_coefficient_false_shadow | On a one-point row, or on longer rows with \(F_a(q)=(-1)^q c_a\), the signed window is coherent. | Any coefficient-uniform \(\rho^{-1}\) Gram theorem is false; this is not a counterexample to the genuine symbol. |
| unsigned_false_shadow | Removing the \((-1)^h\) character and taking constant rows gives the same \(H^2\) coherent capacity. | No unsigned theorem can be imported as the required signed gain. |
| transform_self_return | Fourier transform of (102.H1) is the exact squared half-frequency window multiplier; Round 80's reciprocal adjoint returns to the same complete row. | Plancherel or another reciprocal completion gives equality of capacity, not a new \(\rho\)-power. |
| rho_power_ledger | Verified \(P=L^2\sqrt\rho\), \(E_0=LJD_{\rm ray}^2\), (102.H18), and the diagonal condition \(H\ge\rho\). | Pass; the required linear gain is exactly \(\rho^{-1/2}\). |
| primary_source_hypothesis_map | Mapped only the primary results below; no theorem was imported into the no-go. | No literal source proves (102.H36), (102.H37), or (102.H8). |
| downstream_and_exponent_scope | Compared only with the residual hard-top fixed-\(a\) Gram. | No implication to other M2 packets, M9-M2, M9, endpoint uniformity, or an exponent. |

The relevant primary-source map is negative except for the qualitative
Weyl recurrence control:

| Primary source | Literal hypotheses audited | Verdict for the Round-102 row |
|---|---|---|
| H. Weyl, *Über die Gleichverteilung von Zahlen mod. Eins*, Satz 9 ([primary scan](https://zenodo.org/records/2425535/files/article.pdf)) | A real polynomial with an irrational nonconstant coefficient; the test interval is fixed as the averaging length grows. | Applies to (102.H22) only as fixed-width qualitative recurrence.  It gives no uniform shrinking metric window, fixed-\(X\) Gram, or coefficient-weighted cancellation. |
| E. Bombieri and H. Iwaniec, *On the order of \(\zeta(1/2+it)\)*, Lemma 2.4 ([primary paper](https://www.numdam.org/article/ASNSP_1986_4_13_3_449_0.pdf)) | Two finite point sets, factorized coefficients, a dot-product phase, coordinate boxes, and two explicitly paid close-pair energies. | Any lift exports the problem to the near-\(\Delta\) energy and requires factorization of the joint window, moving supports, owners, and physical integral.  The theorem does not estimate (102.H8). |
| H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, Theorem 1 ([primary paper](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)) | Distinct frequencies modulo one with an explicit minimum separation and one common coefficient sequence. | Exact and arbitrarily near determinant collisions defeat a uniform separation parameter, while (102.H35) is row-dependent.  No hypothesis-preserving substitution gives the target. |
| O. Robert and P. Sargos, *Three-dimensional exponential sums with monomials*, Theorem 2 ([primary paper](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf)) | An unweighted positive count of four monomials in one dyadic interval, with a diagonal term and a volume term. | It can only majorize a coefficient-blind radical collision count after discarding \(k,g\), owners, metric modes, and the actual integral.  It neither cancels the diagonal nor proves (102.H8). |
| X. Li and X. Yang, *An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem*, Proposition 3.1 and Theorem 4.2 ([primary version](https://arxiv.org/html/2308.14859v2)) | A specific rectangular cone extension, or a separably weighted double sum with fixed \(C^3\) phase and all displayed derivative and parameter inequalities. | The source can handle a cone null direction in its own setting, but no literal map retains two moving fibers, the fixed-\(X\) metric product, owners, collars, and (102.H35).  Structural analogy is not applicability. |

No new web theorem was needed or imported.  These are the primary results
already hypothesis-mapped in the selected Round-80 and Round-96 evidence;
the present report uses them only to reject an unsupported transfer.

## 6. Dependencies and exact artifacts used

The report used exactly the selected Round-102 context and its assigned
brief:

- protocol.md;
- state/proof_obligations.yml, restricted to the four Round-102 target
  obligations and the recorded Round-96 no-go;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m2-determinant-weighted-actual-gram/derivation_packet.md;
- rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/reports/primitive_ray_q_hostile_source_audit.md;
- rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/reviews/conductor_round96_capacity_and_controls.md;
- rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reports/actual_symbol_hostile_audit.md;
- rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/reports/strict_metric_energy_hostile_source_audit.md;
- strategy/conductor_0817_full_proof_strategy.md;
- rounds/codex-managed/m9-m2-determinant-weighted-actual-gram/briefs/determinant_gram_hostile_source_audit.md.

The exact-zero example was located diagnostically and then verified
algebraically in (102.H26)--(102.H29); no numerical experiment is used as
proof.  No sibling Round-102 report, synthesis, proof draft, validation
matrix, legacy report, or unlisted repository artifact was read.  No
external theorem beyond the already selected primary-source maps was
imported.  No shared state was edited.

## 7. Recommended state effect

**Recommended effect: retain the target as open, promote no estimate,
record the determinant-carrier no-go, and revise the first survivor.**

The graph may retain the exact identities (102.H1), (102.H4), the
\(\rho\)-ledger (102.H14)--(102.H19), and the determinant algebra
(102.H16), (102.H30), and (102.H32) as candidate evidence after conductor
review.  It should reject any claim that:

- a nonzero-shift determinant mechanism covers \(D_{\rm ray}\asymp1\);
- algebraic nonvanishing of \(\Delta\) gives useful active-scale
  separation;
- the Round-77 \(g\)-variation theorem supplies the missing \(q\)-BV
  hypothesis;
- separately bounding the diagonal and taking absolute values in the
  other shifts gives \(\rho^{-1/2}\) when \(\rho>D_{\rm ray}\);
- an unsigned, arbitrary-coefficient, discrepancy-only, Plancherel, or
  adjoint-reciprocal estimate transfers to the complete actual Gram.

The first strict disjoint survivor is the literal short-ray diagonal
(102.H36).  On \(D_{\rm ray}>1\), the next survivor is the signed complete
near-determinant package (102.H8), together with a genuinely literal
separated estimate (102.H37).  Both must retain the density mode and every
discrepancy mode jointly, two moving \(k,g\) fibers, primitive and
prior-owner masks, profiles, floors, stars, collars, zero extension,
physical entry/exit, both orientations, and the outer real part.  A
positive proof must explain why the phase-aligned arbitrary-coefficient
and unsigned shadows fail while the actual symbol gains.

Accordingly,
M9-M2-primitive-ray-fixed-a-actual-Gram,
M9-M2-top-endpoint-density-discrepancy-energy,
M9-M2-top-endpoint-signed-cone, M9-M2, M9, endpoint uniformity, and every
Gauss-circle exponent implication remain open.  There is no certified
hard subrange, no new \(\rho\)-power, and no external source dependency to
promote.

### Authorized conductor seam audit: raw density-mode incidence and graph effect

The sharper raw incidence lemma is correct under its stated common-box
hypotheses.  Fix \(a,q,h\), put \(b_h=b+2h\asymp A\), and write

\[
 \alpha:=\left({b_h\over b}\right)^{3/2}\asymp1,\qquad
 \mathcal N:=GK.
\]

For \(g,g'\asymp G\) and \(k,k'\asymp K\), set
\(u=g'k\) and \(v=gk'\).  Then \(u,v\asymp\mathcal N\), and the number of
representations of either product in its prescribed dyadic rectangle is
at most the divisor function.  Therefore

\[
\begin{aligned}
 &\#\left\{(g,g',k,k'):
 \left|{g'k\over gk'}-\alpha\right|\le\eta\right\}\\
 &\quad\ll_\varepsilon X^\varepsilon
 \sum_{v\asymp\mathcal N}
 \#\{u\in\mathbb Z:|u-\alpha v|\ll\eta\mathcal N\}\\
 &\quad\ll_\varepsilon
 X^\varepsilon\{\eta\mathcal N^2+\mathcal N\}.
\end{aligned}
\tag{102.H38}
\]

All parity, primitive, owner, and moving-support restrictions can only
decrease this raw count after the boxes have been fixed.  The divisor
bound is uniform because all active integers are of polynomial size in
\(X\).

For the density-mode carrier determinant

\[
 \Delta_0:={g'\over k'b_h^{3/2}}
           -{g\over kb^{3/2}},
\]

one has the exact identity

\[
 \Delta_0={g\over kb^{3/2}}
 \left\{
 {1\over\alpha}{g'k\over gk'}-1
 \right\}.
\tag{102.H39}
\]

Consequently \(|\Delta_0|\le\lambda\) implies

\[
 \left|{g'k\over gk'}-\alpha\right|
 \ll \lambda\,{K\over G}A^{3/2},
\tag{102.H40}
\]

and the proposed conversion
\(\eta\asymp\lambda(K/G)A^{3/2}\) has the correct powers.  At the natural
quadratic threshold \(\lambda=\tau_0\) from (102.H7),

\[
 \eta_0\asymp {A\over JLD_{\rm ray}},\qquad
 \mathcal N=GK\asymp {LJD_{\rm ray}\over A^2},
\tag{102.H41}
\]

so (102.H38) becomes

\[
 \#\{|\Delta_0|\le\tau_0\}
 \ll_\varepsilon X^\varepsilon
 \left\{{LJD_{\rm ray}\over A^3}
       +{LJD_{\rm ray}\over A^2}\right\}
 \ll_\varepsilon X^\varepsilon\mathcal N
\tag{102.H42}
\]

for each fixed \(a,q,h\).  This is a genuine raw pair-incidence saving
from \(\mathcal N^2\) to \(\mathcal N\).

The proposed exact-zero counts are also correct.  If \(h\ne0\) is fixed
and \(\Delta_0=0\), the rationality of \(g'k/(gk')\) forces
\[
 b=du^2,\qquad b_h=dv^2,\qquad
 2h=d(v-u)(v+u)
\tag{102.H43}
\]
with \(d\) squarefree.  Choosing \(d\mid2h\) and a factorization of
\(2h/d\) determines \(u,v\), subject only to parity and positivity.
Hence, for fixed \(a,h\), the number of possible base \(q\)'s is
\[
 \ll\sum_{d\mid2h}\tau(2h/d)
 =\tau_3(2h)\ll_\varepsilon h^\varepsilon.
\tag{102.H44}
\]
For each such \(q\), exact equality is
\(u^3g'k=v^3gk'\).  Grouping again by the two products, of size
\(\asymp\mathcal N\), gives
\[
 \#\{(g,g',k,k'):\Delta_0=0\}
 \ll_\varepsilon X^\varepsilon\mathcal N.
\tag{102.H45}
\]
These bounds include no actual coefficient and do not assert that an
exact-zero tuple survives every owner or has nonzero physical integral.

Neither (102.H42) nor (102.H45) controls the complete mode-resolved actual
near tube.  There are three independent failures of implication.

First, after
\[
 W_R(\theta)\mathfrak C^\circ(g)
 =\sum_{\nu\in\mathbb Z}\widehat W_R(\nu)
   e((\nu-g/2)\theta)\mathfrak B^\circ(g),
\]
the curvature for modes \(\nu,\nu'\) contains
\[
 \Delta_{\nu,\nu'}=
 {g'-2\nu'\over k'b_h^{3/2}}
 -{g-2\nu\over kb^{3/2}},
\tag{102.H46}
\]
not \(\Delta_0\).  The effective numerators can be zero, negative, or
outside a common \(G\)-box.  Thus (102.H38) treats only the
density--density carrier.  If the Fourier modes are not opened, the same
failure reappears as the uncontrolled \(q\)-variation of the complete
metric factor in (102.H35).

Second, the raw edge count supplies neither a weighted operator norm nor
the negative actual correlation needed to cancel \(HE_{\rm act}\).
Even in an ideal equal-size, coefficient-blind model, reducing
\(\mathcal N^2\) pairs to \(\mathcal N\) yields at most a
\(\mathcal N^{-1/2}\) linear capacity gain.  Matching
\(\rho^{-1/2}\) would at least require
\[
 \rho\ll\mathcal N,\qquad
 {\rho\over\mathcal N}
 ={A^3D_{\rm ray}^2\over L^4}\ll1,
\tag{102.H47}
\]
which is not a frozen hypothesis and fails on lawful blocks, for example
when \(L\asymp A\) and \(D_{\rm ray}\gg A^{1/2}\).  The actual
normalization is still harder: (102.H38) contains no bound for the
mode-dependent \(\mathfrak B^\circ\), no maximum-degree estimate, and no
conversion of component mass to \(E_0\).

Third, (102.H44)--(102.H45) concern exact zero only.  The target tube has
positive width \(\tau_0\), includes all density--discrepancy and
discrepancy--discrepancy modes, and retains support crossings,
entry/exit, both orientations, and owner products.  Sparsity of exact
zeros cannot bound that weighted signed tube.

The proposed graph effect is therefore sound with narrow wording:

- Create an **open** node, suggested identifier
  M9-M2-primitive-ray-q1-actual-diagonal-energy, whose exact statement is
  (102.H36) on every residual singleton \(q=1\) block with the complete
  actual row.  It owns only that disjoint short-ray subrange and does not
  imply the longer-row Gram.
- Create one **proved route-obstruction** node, suggested identifier
  M9-M2-determinant-carrier-short-ray-route-obstruction.  Its statement
  should combine (102.H1), the carrier-only identity (102.H4), the
  determinant-free singleton-row fact, the diagonal capacity condition
  (102.H19), and the scoped raw incidence facts (102.H38)--(102.H45).
  It must say explicitly that these facts do not estimate the complete
  mode-resolved actual near tube and do not refute the Gram.

The raw incidence lemmas may be recorded as proved internal evidence
inside that obstruction (or as a narrowly typed auxiliary lemma), but
they do not license a proved actual-symbol node, a target-safe subrange,
or any implication to the canonical density--discrepancy energy.  The
existing fixed-\(a\) actual-Gram node remains open, with (102.H36) and the
complete version of (102.H8) as distinct required inputs.
