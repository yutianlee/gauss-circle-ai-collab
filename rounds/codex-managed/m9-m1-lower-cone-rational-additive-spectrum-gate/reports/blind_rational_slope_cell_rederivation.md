# 1. Result

**Rational-spectrum lemma and reconstruction no-go.**  Write (e(t)=e^{2\pi i t}).  For every reduced (a/q\in\mathbb Q/\mathbb Z), every (M\geq 1), and an absolute implied constant,

\[
 \boxed{
 S_C(M;a/q)
 =\mathbf 1_{4\mid q}\,{i\pi\chi _4(a)\over 2q},M
 +O\bigl((\sqrt M+q)\log(2q)\bigr).}
 \tag{1.1}
\]

Thus the quarter mode is only the first member of an infinite hierarchy: every reduced rational whose reduced denominator is divisible by (4) has a nonzero linear mean, and no other rational does.  For (q=4d), the two resonant row classes are

\[
 h\equiv d\pmod {4d},\qquad h\equiv3d\pmod {4d},
 \tag{1.2}
\]

with respective means ( (i/2)\chi _4(a)) and (-(i/2)\chi _4(a)).  In particular, (1.1) gives (i\pi M/8+O(\sqrt M)) at (a/q=1/4).  Formula (1.1) is uniform for all (q); it is a relative asymptotic on a growing range whenever

\[
 \left({q\over\sqrt M}+{q^2\over M}\right)\log(2q)=o(1),
 \tag{1.3}
\]

and, in particular, when (q\log(2q)=o(\sqrt M)).

The first exact obstruction occurs at reconstruction, before a rational-slope assembly can be declared owner-complete.  If one subtracts all modes of denominator at most (Q), the residual still has a nonzero linear mean at every omitted reduced (b/s) with (4\mid s).  Moreover, the natural denominator truncations have absolute coefficient mass (\asymp Q) and mean-square energy (\asymp\log Q); consequently they converge neither absolutely/uniformly nor in Besicovitch mean square.  There is therefore no finite projection with a rationally mean-zero complement, and the infinite spectrum itself supplies no reconstruction error.

The local derivative geometry can be made exact, but it does not repair this obstruction.  At scale (m\asymp M), the longest cell on which (\sqrt{Nm}) can be replaced by one additive slope using only a bounded Taylor remainder has length

\[
 H_M\asymp N^{-1/4}M^{3/4}\asymp {M^{3/4}\over R},
 \qquad
 \Delta_M\asymp H_M^{-1}\asymp {R\over M^{3/4}}.
 \tag{1.4}
\]

Covering all fractional slopes at this width needs denominators (q\lesssim H_M), and the raw overlap is (O(H_M)).  Even after subtracting a matching linear mean separately in each cell, (1.1) gives only short-interval control of size (\ll(\sqrt M+q)\log(2q)), whereas cellwise assembly would require

\[
 \sup_{|J|\leq H_M}
 \left|\sum_{m\in J}D(m)e(am/q)\right|
 \ll_\varepsilon X^\varepsilon N^{-1/4}M^{1/2}
 \asymp X^\varepsilon {\sqrt M\over R}.
 \tag{1.5}
\]

This is a factor (\asymp R) stronger than the error delivered by the rational-spectrum calculation.  The extracted periodic square-root branches are not target-safe from the available data either.  Hence this report proves neither (B142.4) nor its negation; it proves the requested first exact no-go for a finite/infinite rational-mode subtraction and identifies the strictly stronger residual estimate that any local-slope continuation would have to own.

# 2. Exact statement and hypotheses

Let

\[
 H(M)=\max\left(0,\left\lceil{\sqrt M\over2}\right\rceil-1\right),
 \qquad B_h(M)=\left\lfloor{M\over h}\right\rfloor,
 \qquad L_h(M)=B_h(M)-4h.
 \tag{2.1}
\]

Then (1\leq h\leq H(M)) is exactly the condition (4h^2<M), and the row in (B142.6) is exactly the integer interval

\[
 4h+1\leq r\leq B_h(M),
 \tag{2.2}
\]

of length (L_h(M)\geq0).  Extend (\chi _4) by zero on even integers.  For reduced (a/q), define the row mean

\[
 \mu_{a/q}(h)=
 \begin{cases}
  i/2,&ah\equiv q/4\pmod q,\\
  -i/2,&ah\equiv-q/4\pmod q,\\
  0,&\text{otherwise},
 \end{cases}
 \tag{2.3}
\]

where either of the first two cases is possible only when (4\mid q).  Equivalently, if (q=4d),

\[
 \mu_{a/q}(h)
 =\begin{cases}
 {i\over2}\chi _4(a)\chi _4(t),&h=dt, t\text{ odd},\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{2.4}
\]

The exact finite resonant-row contribution is

\[
 \mathcal M(M;a/q)
 ={i\over2}\chi _4(a)
 \sum_{\substack{t<\sqrt M/(2d)\\t\geq1}}
 \chi _4(t)
 \left(\left\lfloor{M\over dt}\right\rfloor-4dt\right)
 \quad(q=4d),
 \tag{2.5}
\]

and it is zero when (4\nmid q).  Uniformly in (M,q,a),

\[
 S_C(M;a/q)=\mathcal M(M;a/q)
 +O\bigl((H(M)+q)\log(2q)\bigr),
 \tag{2.6}
\]

and

\[
 \mathcal M(M;a/q)
 =\mathbf1_{4\mid q}{i\pi\chi _4(a)\over2q}M+O(\sqrt M).
 \tag{2.7}
\]

For reconstruction, put

\[
 A(a/q)=\mathbf1_{4\mid q}{i\pi\chi _4(a)\over2q},
 \tag{2.8}
\]

where \(a/q\) is reduced, and define the denominator-ordered finite projection

\[
 P_Q(m)=
 \sum_{\substack{4\mid q\leq Q}}
 \ \sum_{\substack{0<a<q\\(a,q)=1}}
 A(a/q)e(-am/q),
 \qquad D_Q(m)=C(m)-P_Q(m).
 \tag{2.9}
\]

The minus sign in (2.9) is forced by the plus-sign transform in (S_C).  For every fixed reduced (b/s),

\[
 \sum_{m\leq M}D_Q(m)e(bm/s)
 =\mathbf1_{4\mid s}\mathbf1_{s>Q}A(b/s)M
 +O\bigl((\sqrt M+s)\log(2s)+sQ^2\bigr).
 \tag{2.10}
\]

The (sQ^2) term is a completely explicit off-diagonal finite-projection bound; it is independent of (M).  In particular, for fixed (Q) and any fixed omitted (s), division by (M) and passage to infinity leaves the nonzero mean (A(b/s)).

For the local geometry, let

\[
 B_X=\left\lfloor {C_VN\over R^2}\right\rfloor,
 \qquad U_M=\min(2M,B_X+1),
 \qquad I_M=[M,U_M)\cap\mathbb Z,
 \tag{2.11}
\]

so the last integer in a nonempty block is (U_M-1).  Put (f(x)=\sqrt{Nx}) and

\[
 \Lambda_M={\sqrt N\over4M^{3/2}},
 \qquad H_M^{(0)}=\Lambda_M^{-1/2}=2N^{-1/4}M^{3/4}.
 \tag{2.12}
\]

When (H_M^{(0)}\geq4), take the half-open integer cells of length

\[
 H_M=\left\lfloor H_M^{(0)}/2\right\rfloor,
 \qquad \Delta_M=H_M^{-1};
 \tag{2.13}
\]

the final cell is truncated at (U_M).  When (H_M^{(0)}<4), use singleton cells.  For (s=n+a/q>\Delta_M), define the closed geometric slope arc before tie-breaking by

\[
 \mathfrak A_{s}(M)=
 [M,U_M)\cap
 \left[{N\over4(s+\Delta_M)^2},
       {N\over4(s-\Delta_M)^2}\right].
 \tag{2.14}
\]

At equality, assign a cell to the fraction with the smallest denominator, then the least numerator; block intervals remain left-closed and right-open.  This convention turns the overlapping arcs into an unambiguous partition when desired.

Finally, for a residual (D), define the exact local additive norm

\[
 \mathcal E_D(M,H,Q)=
 \max_{\substack{q\leq Q,(a,q)=1}}
 \max_{\substack{J=[u,v)\cap\mathbb Z\subset I_M\\v-u\leq H}}
 \left|\sum_{m\in J}D(m)e(am/q)\right|.
 \tag{2.15}
\]

No hypothesis asserting the bound (1.5) is contained in the statement-only packet; (2.15) records precisely the missing owner.

# 3. Proof or derivation

### 3.1 Exact rows, parity, and rational means

For every integer (r), including even (r),

\[
 \chi _4(r)=\sin(\pi r/2)
 ={e(r/4)-e(-r/4)\over2i}.
 \tag{3.1}
\]

Consequently the (h)-th row is

\[
 \sum_{r=4h+1}^{B_h(M)}\chi _4(r)e(ahr/q)
 ={1\over2i}\left(
 \sum_{r=4h+1}^{B_h(M)}e((ah/q+1/4)r)
 -\sum_{r=4h+1}^{B_h(M)}e((ah/q-1/4)r)
 \right).
 \tag{3.2}
\]

A finite geometric sum of length (L) equals (L) when its frequency is integral and otherwise has modulus at most

\[
 \min\left(L,{1\over2\|\theta\|}\right).
 \tag{3.3}
\]

Thus the first frequency in (3.2) has a mean precisely when
\(ah/q\equiv-1/4\pmod1\), and the second precisely when
\(ah/q\equiv1/4\pmod1\).  The signs in (3.2) give (-i/2) in the
former case and (+i/2) in the latter.  A rational with reduced
denominator (q/(q,h)) can equal \(\pm1/4\) only if \(4\mid q\).  If
(q=4d), coprimality forces (a) odd, and resonance is equivalent to
(h=dt) with (t) odd.  Then its sign is

\[
 {i\over2}\chi _4(at)={i\over2}\chi _4(a)\chi _4(t),
 \tag{3.4}
\]

which proves (2.3)--(2.5), including both row classes and their signs.

It remains to sum the nonmean pieces uniformly.  For either sign in (3.2), as (h) runs through a complete residue system modulo (q), the points

\[
 ah/q\pm1/4\pmod1
 \tag{3.5}
\]

are (q) distinct points separated by (1/q).  They lie on the (1/(4q))-grid.  After deleting a possible zero, ordering them by distance from the nearest integer and applying (3.3) gives

\[
 \sum_{h\bmod q}^{\!*}{1\over\|ah/q\pm1/4\|}
 \ll q\sum_{j\leq q}{1\over j}
 \ll q\log(2q).
 \tag{3.6}
\]

There are at most (H(M)/q) complete (h)-blocks and one incomplete block; positivity of the bound lets the incomplete block be bounded by a complete one.  Hence all incomplete-period errors from both the lower endpoint (4h+1) and the upper endpoint (B_h(M)) total

\[
 O((H(M)+q)\log(2q)),
 \tag{3.7}
\]

which proves (2.6).  Notice that (3.2) uses the exact lower endpoint, not a relaxed hyperbola, and that even (r) contribute exactly zero rather than an error.

### 3.2 Main constant and both cone endpoints

Suppose (q=4d) and put (Z=\sqrt M/(2d)).  In (2.5), replacing the upper floor by (M/(dt)) costs (O(Z)).  The upper endpoint then gives

\[
 {M\over d}\sum_{t<Z}{\chi _4(t)\over t}.
 \tag{3.8}
\]

The alternating Leibniz series and its elementary remainder give

\[
 \sum_{t<Z}{\chi _4(t)\over t}
 ={\pi\over4}+O(Z^{-1})
 \quad(Z\geq2).
 \tag{3.9}
\]

The exact lower cone endpoint contributes

\[
 -4d\sum_{t<Z}\chi _4(t)t=O(dZ)=O(\sqrt M),
 \tag{3.10}
\]

because pairing (4j+1) with (4j+3) shows
(\sum_{t<T}\chi _4(t)t=O(T)).  The tail error in (3.9) contributes

\[
 {M\over d}O(Z^{-1})=O(\sqrt M),
 \tag{3.11}
\]

and the upper-floor error is (O(Z)=O(\sqrt M)).  If (Z<2), the entire difference between the empty/short sum and the asserted linear term is still (O(\sqrt M)), since then (M/d<4\sqrt M).  Multiplying (3.8) by ((i/2)\chi _4(a)) gives

\[
 {i\over2}\chi _4(a){M\over d}{\pi\over4}
 ={i\pi\chi _4(a)\over8d}M
 ={i\pi\chi _4(a)\over2q}M.
 \tag{3.12}
\]

This proves (2.7) and (1.1).  Dividing its error by (M/q) gives exactly the relative-error expression in (1.3).

### 3.3 Finite projection and infinite reconstruction obstruction

Distinct reduced rationals are distinct frequencies modulo one.  Therefore, for fixed reduced (b/s), the transform of (2.9) has one diagonal term exactly when (s\leq Q) and (4\mid s).  Every off-diagonal pair satisfies

\[
 \|b/s-a/q\|\geq {1\over sq},
 \tag{3.13}
\]

so its geometric sum is (O(sq)).  After multiplication by
(|A(a/q)|=\pi/(2q)), each off-diagonal frequency costs (O(s)).  Since
(\sum_{q\leq Q}\varphi(q)=O(Q^2)), the total is (O(sQ^2)).  Subtracting this from (1.1) proves (2.10).  Choosing any fixed reduced (b/s) with (s>Q) and (4\mid s) proves that no finite (P_Q) leaves a complement with sublinear additive sums at every rational frequency.

There is also no denominator-ordered infinite projection with a controlled standard convergence mode.  Its absolute coefficient mass and finite-polynomial mean-square energy are

\[
 \sum_{\substack{4\mid q\leq Q}}
 \sum_{(a,q)=1}|A(a/q)|
 ={\pi\over2}\sum_{\substack{4\mid q\leq Q}}{\varphi(q)\over q}
 \asymp Q,
 \tag{3.14}
\]

\[
 \lim_{L\to\infty}{1\over L}\sum_{m\leq L}|P_Q(m)|^2
 =\sum_{\substack{4\mid q\leq Q}}
 \sum_{(a,q)=1}|A(a/q)|^2
 ={\pi^2\over4}\sum_{\substack{4\mid q\leq Q}}{\varphi(q)\over q^2}
 \asymp\log Q.
 \tag{3.15}
\]

The orders follow elementarily from
(\varphi(n)/n=\sum_{d\mid n}\mu(d)/d); restricting to (q=4d) with (d) odd already supplies matching lower bounds, while (\varphi(q)\leq q) supplies the upper bounds.  Orthogonality of a finite set of distinct rational frequencies proves the equality in (3.15).  In particular, the energy in (Q<q\leq2Q) stays bounded below, so (P_Q) is not Cauchy in mean square.  Equations (3.14)--(3.15) do not rule out every specially ordered pointwise summation, but they do prove that the rational means alone provide neither an absolute/uniform reconstruction nor a mean-square reconstruction, and hence provide no tail error usable in (B142.3).

### 3.4 Local derivative arcs, overlap, and the residual norm

On the exact continuous hull ([M,U_M)),

\[
 f'(x)={\sqrt N\over2\sqrt x},\qquad
 f''(x)=-{\sqrt N\over4x^{3/2}},
 \tag{3.16}
\]

and

\[
 {\sqrt N\over4(2M)^{3/2}}
 \leq |f''(x)|\leq\Lambda_M.
 \tag{3.17}
\]

For a cell of length (H_M) and a rational slope (s=n+a/q) satisfying
(|f'(x_0)-s|\leq\Delta_M) at its left endpoint, Taylor's theorem gives

\[
 \sup_{x\text{ in cell}}
 |f(x)-f(x_0)-s(x-x_0)|
 \leq H_M\Delta_M+\tfrac12\Lambda_MH_M^2=O(1).
 \tag{3.18}
\]

This proves the scales in (1.4).  Monotonicity of (f') gives the exact inverse image (2.14).  A stationary point of the shifted branch
(f(x)-(n+a/q)x) is

\[
 x_{n,a/q}={N\over4(n+a/q)^2},
 \tag{3.19}
\]

and it lies in the half-open block exactly when

\[
 f'(U_M)<n+a/q\leq f'(M).
 \tag{3.20}
\]

Thus the right block endpoint is excluded and the left endpoint is included.

Let (\mathcal F_Q) be the reduced Farey fractions of denominator at most (Q), on the circle.  Two distinct members are separated by at least (Q^{-2}).  Hence arcs of radius (\Delta<1/2) have overlap multiplicity at most

\[
 2+2\Delta Q^2;
 \tag{3.21}
\]

for (\Delta\geq1/2), the trivial bound is (O(Q^2)).  Dirichlet approximation gives a member of (\mathcal F_Q) within (1/Q) of every fractional slope.  Thus (Q_M=\lceil\Delta_M^{-1}\rceil\asymp H_M) covers all slope cells, but (3.21) is then (O(H_M)).  A lexicographic tie-break makes the assignment disjoint, but cannot improve the sum of absolute cell estimates.

On a cell assigned to (a/q), Abel summation applied to
(D(m)e(am/q)) and the bounded-variation factor
(e(f(m)-am/q)), using (3.18), gives

\[
 \left|\sum_{m\in J}m^{-3/4}V_{\rm low}(R^2m/N)D(m)e(f(m))\right|
 \ll M^{-3/4}\mathcal E_D(M,H_M,Q_M).
 \tag{3.22}
\]

There are (O(1+M/H_M)) half-open cells.  In the nonsingleton range their total is therefore

\[
 \ll N^{1/4}M^{-1/2}\mathcal E_D(M,H_M,Q_M)
 \asymp R M^{-1/2}\mathcal E_D(M,H_M,Q_M).
 \tag{3.23}
\]

This proves the requirement (1.5), up to the harmless number of dyadic blocks.  By contrast, subtracting the matching mean at one rational frequency in (1.1) gives on an arbitrary interval (J\subset I_M) only

\[
 \left|\sum_{m\in J}
 \bigl(C(m)-A(a/q)e(-am/q)\bigr)e(am/q)\right|
 \ll(\sqrt M+q)\log(2q).
 \tag{3.24}
\]

For the needed denominators \(q\lesssim H_M\), the uniformity condition
(1.3) is in fact adequate: over \(M\leq C_VN/R^2\),

\[
 {H_M\log(2H_M)\over\sqrt M}
 \ll N^{-1/4}M^{1/4}\log R
 \ll R^{-1/2}\log R.
 \tag{3.25}
\]

The obstruction is not failure of the row asymptotic in this denominator range.  It is that its (\sqrt M)-sized endpoint error inserted into (3.23) costs (\asymp R), while (1.5) needs (\sqrt M/R).  In the singleton range (M\lesssim N^{1/3}\asymp R^{4/3}), a cellwise argument has no additive cancellation at all.  Any successful continuation must therefore add cross-cell cancellation or prove the genuinely stronger local norm (1.5); neither follows from the rational spectrum.

### 3.5 Periodic branches, the nonresonant mask, and canonical self-return

For one extracted frequency, first omit the nonresonant mask and write

\[
 B_M(a/q)=\sum_{m\in I_M}m^{-3/4}V_{\rm low}(R^2m/N)
 e(\sqrt{Nm}-am/q).
 \tag{3.26}
\]

The second derivative is unchanged by the rational shift.  The second-derivative estimate with
(\lambda\asymp\sqrt N M^{-3/2}), together with partial summation of the fixed smooth weight, gives

\[
 |B_M(a/q)|
 \ll \min\left(M^{1/4},
 N^{1/4}M^{-1/2}+N^{-1/4}\right).
 \tag{3.27}
\]

After multiplication by (|A(a/q)|=\pi/(2q)), the exact (q)-power ledger is

\[
 \begin{array}{c|c}
 \text{object}&\text{bound supplied by (3.27)}\\ \hline
 \text{one }(a,q)\text{ on one }M
 &q^{-1}\min(M^{1/4},RM^{-1/2}+R^{-1})\\
 \text{all }a\pmod q\text{ on one }M
 &(\varphi(q)/q)\min(M^{1/4},RM^{-1/2}+R^{-1})\\
 \text{all dyadic }M\leq C_VN/R^2\text{ at fixed }q
 &O(R^{1/3})\\
 \text{all }q\leq Q\text{ and all dyadic }M
 &O(QR^{1/3}).
 \end{array}
 \tag{3.28}
\]

The crossover is (M\asymp N^{1/3}\asymp R^{4/3}).  These are upper bounds, not lower bounds, but even the unrestricted branch is not certified target-safe by this argument.

For the actual branch with the indicator
(\mathbf1_{|j_m|>\sqrt M}), the second-derivative lemma cannot simply be applied: the indicator is not a smooth interval weight.  Without a separate estimate for its jumps, the rigorous direct ledger is only

\[
 \begin{array}{c|c}
 \text{one }(a,q)\text{ on one }M&q^{-1}M^{1/4}\\
 \text{fixed }q\text{ over all }M&O(R^{1/2})\\
 q\leq Q\text{ over all }M&O(QR^{1/2}).
 \end{array}
 \tag{3.29}
\]

Replacing the masked branch by (3.26) would require pricing the removed cells for the periodic coefficient itself; target-safety of those cells for the original coefficient (C) does not imply that new assertion.

The nonresonant condition does not remove the rational arcs in (2.14).  The exact identity

\[
 |k_m-\sqrt{Nm}|={|j_m|\over k_m+\sqrt{Nm}}
 \tag{3.30}
\]

shows that it is a condition on the value (f(m)).  If a reduced positive rational (u/q) were exactly equal to (f'(m)), then
(Nq^2=4mu^2), hence (q^2\mid4m), (\sqrt{Nm}=2mu/q\in\mathbb Z), and (j_m=0).  Thus nonresonance excludes exact rational equality, but the only general quantitative separation obtained from integrality is

\[
 \left|f'(m)-{u\over q}\right|
 ={ |Nq^2-4mu^2|\over
 4mq^2(f'(m)+u/q)}
 \geq {1\over4mq^2(f'(m)+u/q)}.
 \tag{3.31}
\]

When (u/q\asymp f'(m)) and (m\asymp M), this is merely
\(\gg(q^2\sqrt{NM})^{-1}\), far smaller than the arc width
(\Delta_M\asymp N^{1/4}M^{-3/4}).  Hence (|j_m|>\sqrt M) supplies no usable rational-slope separation.

Finally, applying the canonical Poisson stationary transform to the unrestricted phase gives, for (s=n+a/q>0),

\[
 x_s={N\over4s^2},\qquad
 f(x_s)-sx_s={N\over4s},\qquad
 x_s^{-3/4}|f''(x_s)|^{-1/2}=2N^{-1/4}.
 \tag{3.32}
\]

Thus the dual sum has phase (e(N/(4(n+a/q)))), amplitude of order (N^{-1/4}), and (\asymp\sqrt N/\sqrt M) stationary indices on a full dyadic block.  It is a reciprocal-cone self-return, not an estimate.  No Poisson/Voronoi/Mellin label changes that accounting.

# 4. First doubtful or unproved step

The rational row calculation through (1.1) is complete.  The first unavailable step is the assertion that these Fourier--Bohr means can be subtracted with an owner-complete reconstruction error.  It fails for every finite projection by (2.10), while the natural infinite truncations fail the absolute and mean-square Cauchy tests (3.14)--(3.15).  A specially regularized conditional reconstruction is not ruled out, but no such summation law or tail estimate is present and none follows from the means.

Even granting a scale-dependent formal subtraction, the next unproved step is the residual local estimate (1.5).  The proven rational error gives only (3.24), a factor (R) too large after the exact number and weight of slope cells are inserted.  Separately, every periodic branch would need a masked estimate of size (X^\varepsilon); (3.28) and (3.29) show the powers actually available from the self-contained derivative and trivial arguments.  Therefore there is no owner-complete strict reduction of (B142.3) in the statement-only data.

# 5. Control tests and outcomes

1. **`exact_cone_hyperbola_endpoints_and_parity` — pass.**  Equations (2.1)--(2.2) retain (4h^2<M), lower endpoint (4h+1), upper endpoint (\lfloor M/h\rfloor), and exact odd parity through (3.1).  The lower (-4h), upper floor, and incomplete-period errors are separately priced in (3.7), (3.10), and (3.11).
2. **`reduced_rational_frequency_and_q_mod_4_cases` — pass.**  For reduced (a/q), the mean is zero for (q\equiv1,2,3\pmod4) and nonzero exactly for (q\equiv0\pmod4).
3. **`row_mean_residue_classes_sign_and_constant` — pass.**  For (q=4d), (h\equiv d,3d\pmod q) have means ((i/2)\chi _4(a)) and (-(i/2)\chi _4(a)); the resulting scalar constant is (i\pi\chi _4(a)/(2q)).
4. **`fixed_q_versus_growing_q_error_uniformity` — pass.**  The all-(q) error is ((\sqrt M+q)\log(2q)); (1.3) states exactly when it is a relative asymptotic.  No fixed-(q) statement is silently used beyond that range.
5. **`rational_spectrum_convergence_and_reconstruction` — obstruction.**  Finite residuals retain every omitted mode by (2.10).  Absolute mass is (\asymp Q), energy is (\asymp\log Q), and no usable infinite reconstruction error follows.
6. **`local_derivative_arc_width_overlap_and_multiplicity` — pass, with capacity failure.**  Exact half-open block endpoints, cell length, width, inverse-image arcs, stationary endpoint convention, coverage denominator, and overlap (O(1+\Delta Q^2)) appear in (2.11)--(2.14) and (3.19)--(3.21).  At covering height (Q\asymp H_M), raw overlap is (O(H_M)).
7. **`nonresonant_phase_value_versus_slope_distinction` — pass.**  Equations (3.30)--(3.31) show exactly what phase-value information implies and why its rational-slope separation is microscopic relative to (\Delta_M).
8. **`periodic_branch_all_dyadic_R_and_q_power_ledger` — target safety not obtained.**  The unrestricted ledger is (q^{-1}) per mode, (O(R^{1/3})) per denominator, and (O(QR^{1/3})) through height (Q).  With the actual mask, the direct ledger is (O(R^{1/2})) per denominator and (O(QR^{1/2})) through height (Q).
9. **`residual_additive_partial_sum_hypothesis` — missing owner identified.**  Equation (1.5), formulated precisely by (2.15), is what the cellwise method needs; (3.24) is a factor (R) too weak.
10. **`raw_capacity_versus_fixed_centre_signed_scalar` — pass.**  The mass and energy in (3.14)--(3.15) are used only as reconstruction obstructions.  They are neither an upper nor a lower bound for the signed, masked, fixed-(N) scalar; triangle estimates (3.28)--(3.29) are explicitly only upper ledgers.
11. **`canonical_transform_self_return_and_downstream_scope` — pass.**  Equation (3.32) records the reciprocal-cone return and claims no gain.  The conclusion concerns only the proposed treatment of (B142.3); it proves no square identity, lower GAR, M1, M2, endpoint theorem, M9, global quarter theorem, or exponent improvement.

# 6. Dependencies and exact artifacts used

This was a 100% analytic, statement-only derivation.  No numerical experiment, web search, source import, strategy file, proof-state file, nonblind artifact, or sibling report was used.  The exact artifacts read were:

- `protocol.md`;
- `rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/briefs/blind_rational_slope_cell_rederivation.md`;
- `rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/blind_statement.md`.

The only supplied mathematical fact used as a consistency control was (B142.5); the general formula (1.1) was derived independently and specializes to it.

# 7. Recommended state effect

**No change to the target obligation.**  Retain (1.1), (2.5), and the exact row-mean table as candidate lemmas for independent seam review.  Reject a finite periodic projection or the unregularized denominator-ordered infinite projection as an owner-complete proof mechanism.  Do not promote (B142.4) or any downstream statement.  A future route must separately own either a convergent reconstruction with a quantitative tail plus masked periodic-branch bounds, or a non-cellwise cancellation principle strong enough to replace the residual requirement (1.5).
