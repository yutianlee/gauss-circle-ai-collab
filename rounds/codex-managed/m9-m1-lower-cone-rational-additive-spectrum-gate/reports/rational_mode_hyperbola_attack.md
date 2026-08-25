# Round 142 discovery report: exact rational modes and denominator-subtraction self-return

Campaign: `m9-m1-lower-cone-rational-additive-spectrum-gate`
Task: `rational_mode_hyperbola_attack`
Role: discovery
Starting graph SHA-256: `de02111a1831d30da33c9f4b2d4a549efa1942dcdc32b5d829e671f6ad5e0e76`
Allocation: 100 percent analytic/algebraic; no numerical experiment and no source import.

## 1. Result: exact spectrum and a rational-major-arc self-return no-go

Write (e(t)=e^{2\pi i t}), let (chi=chi _4), and define

\[
 C(m)=\sum_{\substack{hr=m\\r\ {\rm odd}\\r>4h}}\chi(r).
\tag{142.1}
\]

For every reduced rational (a/q), (q\geq1), and every real
(M\geq1), the sharp-cone additive transform has the uniform formula

\[
 \boxed{
 \sum_{m\leq M}C(m)e(am/q)
 =\mathbf 1_{4\mid q}\,{i\pi\chi(a)\over2q}M
 +O\!\left((\sqrt M+q)\log(2q)\right).}
\tag{142.2}
\]

The implied constant is absolute and independent of (a,q,M).  Thus
the complete rational Bohr spectrum, in the convention

\[
 b(\beta)=\lim_{M\to\infty}{1\over M}
 \sum_{m\leq M}C(m)e(-\beta m),
\tag{142.3}
\]

is

\[
 \boxed{
 \operatorname {Spec}_{\mathbb Q}(C)
 =\{c/q\pmod1:(c,q)=1,\ 4\mid q\},\qquad
 b(c/q)=-{i\pi\chi(c)\over2q}.}
\tag{142.4}
\]

There are no other nonzero rational means.  In particular

\[
 S_C(M;1/4)={i\pi\over8}M+O(\sqrt M),\qquad
 S_C(M;-1/4)=-{i\pi\over8}M+O(\sqrt M),
\tag{142.5}
\]

so the Round-141 sign and constant are recovered, while (142.4) shows
that (1/4) is only the first member of an infinite spectrum.

Formula (142.2) is a fixed- and growing-denominator theorem.  For fixed
(q) it has error (O_q(\sqrt M)).  Uniformly for a varying
denominator satisfying

\[
 q\log(2q)=o(\sqrt M),
\tag{142.6}
\]

the displayed main term is an asymptotic whenever (4\mid q); if
(4\nmid q), (142.2) is the corresponding zero-main-term estimate.
The formula remains valid outside (142.6), but then its putative main
term need not dominate the stated error.

The exact denominator cutoff

\[
 B_Q(m):=-{i\pi\over2}
 \sum_{\substack{q\leq Q\\4\mid q}}{1\over q}
 \sum_{\substack{c\bmod q\\(c,q)=1}}
 \chi(c)e(cm/q),
 \qquad D_Q(m):=C(m)-B_Q(m),
\tag{142.7}
\]

does remove all the linear main modes with denominator at most (Q),
but it does not give an owner-complete target reduction.  Precisely,

\[
 \boxed{
 \sum_{m\leq M}D_Q(m)e(am/q)
 =\mathbf 1_{\{4\mid q,\ q>Q\}}
 {i\pi\chi(a)\over2q}M
 +O\!\left((\sqrt M+q)\log(2q)+qQ^2\right).}
\tag{142.8}
\]

Hence every finite cutoff retains the same linear mode at every larger
denominator.  More decisively, the full spectrum has no absolutely or
square-summable coefficient ordering, and the canonical
denominator-Abel reconstruction is not (C).  With (q=4d) and
(\eta>0), put

\[
 B_\eta(m):=-{i\pi\over8}
 \sum_{d\geq1}{1\over d^{1+\eta}}
 \sum_{\substack{c\bmod 4d\\(c,4d)=1}}
 \chi(c)e(cm/(4d)).
\tag{142.9}
\]

Then the exact identity

\[
 \boxed{
 B_\eta(m)={\pi\over4L(1+\eta,\chi)}
 \sum_{\ell\mid m}\chi(m/\ell)\ell^{-\eta}}
\tag{142.10}
\]

gives

\[
 \lim_{\eta\downarrow0}B_\eta(m)
 =\sigma_\chi(m):=\sum_{\ell\mid m}\chi(m/\ell).
\tag{142.11}
\]

Thus the explicit full reconstruction self-returns to the complete
radial coefficient (\sigma_\chi=r_2/4), while the exact reconstruction
error is

\[
 C(m)-\sigma_\chi(m).
\tag{142.12}
\]

On (m=2^\nu n), (n) odd and (chi(n)=-1), one has
(\sigma_\chi(m)=0), so (142.12) equals (C(m)) exactly: the accepted
negative-character far sector is untouched.  On the complementary
sector the complete radial branch and the cone complement are both
owner-sized.  The extracted nonlinear square-root branch is also not
target-safe: the best elementary owner-complete ledger retains a
positive power of (R=X^{1/4}), and its stationary transform is the
accepted reciprocal self-return.

Accordingly the result label is

\[
 \boxed{\mathsf{rational\_major\_arc\_self\_return\_no\_go}.}
\tag{142.13}
\]

This is not a lower bound for the signed fixed-centre scalar.  It proves
that rational-mode extraction by itself supplies neither a target-safe
reconstruction nor a strict owner-complete survivor.

## 2. Exact statement and hypotheses

Assume throughout that (M\geq1) is real, (a\in\mathbb Z),
(q\in\mathbb N), and ((a,q)=1).  The upper endpoint (m\leq M) is
closed and the cone endpoint (r>4h) is strict.  Define

\[
 H_M:=\left\lfloor{\sqrt{1+16M}-1\over8}\right\rfloor,
\qquad
 K_h(M):=\left\lfloor{M/h-4h+1\over2}\right\rfloor
 \quad(1\leq h\leq H_M).
\tag{142.14}
\]

Thus (H_M) is the largest (h) for which the first admissible odd
integer (r=4h+1) satisfies (hr\leq M), and (K_h(M)) is exactly
the number of odd integers in

\[
 4h<r\leq M/h.
\tag{142.15}
\]

Put

\[
 z_h:=-e(2ah/q),\qquad
 G(K,z):=\sum_{n=0}^{K-1}z^n.
\tag{142.16}
\]

The finite transform before any asymptotic replacement is

\[
 \boxed{
 S_C(M;a/q)=\sum_{h=1}^{H_M}
 e\!\left({ah(4h+1)\over q}\right)G(K_h(M),z_h).}
\tag{142.17}
\]

There is a constant row if and only if

\[
 z_h=1
 \quad\Longleftrightarrow\quad
 q=4d\ \text{and}\ h=d\ell\ \text{with }\ell\text{ odd}.
\tag{142.18}
\]

For such a row (a) is odd and every summand has the exact value

\[
 e\!\left({ah(4h+1)\over q}\right)
 =e(a\ell/4)=i\chi(a)\chi(\ell).
\tag{142.19}
\]

Equations (142.14)--(142.19), including both cone endpoints and the
parity of (r), are part of the theorem, not an asymptotic convention.

For later use, partial summation in (142.2) gives the exact leading
weighted mode

\[
 \boxed{
 \sum_{m\leq M}m^{-3/4}C(m)e(am/q)
 =\mathbf1_{4\mid q}{2i\pi\chi(a)\over q}M^{1/4}
 +O\!\left(q\log(2q)\right).}
\tag{142.20}
\]

For (q=4), (142.20) is
(i\pi M^{1/4}/2+O(1)), the floor-free version of the Round-141
weighted quarter mode.  On a dyadic interval and with a fixed smooth
weight (w_M) satisfying
(|w_M^{(j)}|\ll_j M^{-3/4-j}), its main contribution is exactly

\[
 \mathbf1_{4\mid q}{i\pi\chi(a)\over2q}
 \sum_m w_M(m),
\tag{142.21}
\]

and the endpoint error is

\[
 O\!\left((M^{-1/4}+qM^{-3/4})\log(2q)\right).
\tag{142.22}
\]

For the Round-142 application, distinguish the rational denominator
(q) from the real-centre remainder (q_X):

\[
 R=X^{1/4},\qquad N=y^2+q_X,\qquad0\leq q_X\leq2y,
 \qquad M\leq C_VN/R^2\asymp R^2.
\tag{142.23}
\]

The coefficient theorem (142.2) is independent of (N) and hence of
both endpoint values (q_X=0,2y).  The phase ledger below uses only
(N\asymp R^4), uniformly over that full range.

Finally, the coefficient mass of the limiting spectrum is

\[
 \sum_{\substack{q\leq Q\\4\mid q}}
 \sum_{(c,q)=1}|b(c/q)|
 ={\pi\over2}\sum_{\substack{q\leq Q\\4\mid q}}{\varphi(q)\over q}
 \asymp Q,
\tag{142.24}
\]

whereas

\[
 \sum_{\substack{q\leq Q\\4\mid q}}
 \sum_{(c,q)=1}|b(c/q)|^2
 ={\pi^2\over4}\sum_{\substack{q\leq Q\\4\mid q}}
 {\varphi(q)\over q^2}\asymp\log(2Q).
\tag{142.25}
\]

Thus neither absolute nor (B^2)-type convergence is available for
the unregularized limiting coefficients.

## 3. Proof and derivation

### 3.1 Exact odd-row transform

Unfolding (m=hr) without changing either endpoint gives

\[
 S_C(M;a/q)=
 \sum_{h\geq1}
 \sum_{\substack{4h<r\leq M/h\\r\ {\rm odd}}}
 \chi(r)e(ahr/q).
\tag{142.26}
\]

The inner row is nonempty exactly for (h\leq H_M).  Its admissible
integers are

\[
 r=4h+1+2n,\qquad0\leq n<K_h(M).
\tag{142.27}
\]

Because (chi(4h+1+2n)=(-1)^n), the ratio of consecutive row terms is
(-e(2ah/q)=z_h), and the first term is the prefactor in (142.17).
This proves the exact finite identity.

The equation (z_h=1) says

\[
 {4ah\over q}\in2\mathbb Z+1.
\tag{142.28}
\]

Let (g=(q,4)).  Since ((a,q)=1), first (q/g\mid h), say
(h=(q/g)\ell).  Equation (142.28) becomes
(4a\ell/g\in2\mathbb Z+1).  This is impossible for (g=1,2), and
for (g=4) it is equivalent to (ell) odd.  This proves (142.18).
Putting (q=4d), (h=d\ell) in the first-row phase gives

\[
 {ah(4h+1)\over q}=ad\ell^2+{a\ell\over4},
\tag{142.29}
\]

which proves the sign (142.19).

### 3.2 The resonant main term

Let (L=\lfloor H_M/d\rfloor).  By (142.19), the total of the constant
rows is

\[
 i\chi(a)\sum_{\substack{\ell\leq L\\\ell\ {\rm odd}}}
 \chi(\ell)K_{d\ell}(M).
\tag{142.30}
\]

The exact endpoint formula (142.14) gives

\[
 K_{d\ell}(M)={M\over2d\ell}-2d\ell+O(1).
\tag{142.31}
\]

The two elementary character sums are

\[
 \sum_{\substack{\ell\leq L\\\ell\ {\rm odd}}}{\chi(\ell)\over\ell}
 ={\pi\over4}+O(L^{-1}),
 \qquad
 \sum_{\substack{\ell\leq L\\\ell\ {\rm odd}}}\chi(\ell)\ell=O(L).
\tag{142.32}
\]

If (d\leq H_M), (142.30)--(142.32) equal

\[
 {i\pi\chi(a)\over8d}M+O(\sqrt M).
\tag{142.33}
\]

Indeed (M/(dL)+dL+L\ll\sqrt M), including the endpoint case
(H_M/2<d\leq H_M).  If (d>H_M), there is no constant row, but the
absolute size of the displayed prospective main term is
(M/d\ll\sqrt M); the same formula therefore remains valid.  Since
(q=4d), (142.33) is exactly the main term in (142.2).

### 3.3 Uniform sum of all nonconstant rows

Let

\[
 P={q\over(q,2)}.
\tag{142.34}
\]

The sequence (z_h) has period (P).  Across one period it is a
permutation either of all (P)-th roots of unity or of their half-step
translate.  In the case (4\mid q), the unique value (1) is precisely
the residue class already removed in (142.18).  For (z\neq1),

\[
 |G(K,z)|\leq {2\over|1-z|}.
\tag{142.35}
\]

The elementary root-spacing sum is

\[
 \sum_{\substack{1\leq j\leq P\\z_j\neq1}}
 {1\over|1-z_j|}\ll P\log(2P).
\tag{142.36}
\]

Splitting (1\leq h\leq H_M) into complete (P)-periods plus one
remainder and using (H_M\ll\sqrt M) gives

\[
 \sum_{\substack{h\leq H_M\\z_h\neq1}}|G(K_h,z_h)|
 \ll(H_M+P)\log(2P)
 \ll(\sqrt M+q)\log(2q).
\tag{142.37}
\]

Together with (142.33), this proves (142.2).  Notice that completing
each row separately by (O(q)) would give the weaker
(O(q\sqrt M)); (142.36) is the exact growing-(q) gain.

### 3.4 Exact finite-height spectrum

For (h\geq1), set

\[
 f_h(m)=\mathbf1_{h\mid m}\chi(m/h).
\tag{142.38}
\]

The exact discrete Fourier expansion is

\[
 f_h(m)={1\over2ih}\sum_{b=0}^{h-1}
 \left{
 e\!\left({(4b+1)m\over4h}\right)
 -e\!\left({(4b+3)m\over4h}\right)
 \right}.
\tag{142.39}
\]

Every reduced denominator in (142.39) is divisible by (4).  Fix a
reduced (c/q) with (q=4d).  It occurs in the (h)-th line exactly
when

\[
 h=dt,\qquad t\ {\rm odd}.
\tag{142.40}
\]

The corresponding numerator in denominator (4dt) is (ct), so the
sign of its coefficient is (chi(ct)=\chi(c)\chi(t)).  Consequently
the coefficient after retaining heights (h\leq H) is

\[
 b_H(c/q)=-{i\chi(c)\over2d}
 \sum_{\substack{t\leq H/d\\t\ {\rm odd}}}{\chi(t)\over t}.
\tag{142.41}
\]

Letting (H\to\infty) in this declared height order and using
(L(1,\chi)=\pi/4) yields (142.4).  This also independently checks the
sign convention between (142.2) and (142.4): the transform with
(+a/q) detects (b(-a/q)=i\pi\chi(a)/(2q)).

Equations (142.24)--(142.25) follow from
(|b(c/q)|=\pi/(2q)) and the elementary mean orders of
(\varphi(q)/q) and (\varphi(q)/q^2) on multiples of four.

### 3.5 Hard denominator cutoff and exact reconstruction formula

Let

\[
 \mathcal G_d(m):=
 \sum_{\substack{c\bmod4d\\(c,4d)=1}}
 \chi(c)e(cm/(4d)).
\tag{142.42}
\]

Möbius inversion of ((c,d)=1), with all even divisors killed by
(chi(c)), gives

\[
 \mathcal G_d(m)=2i
 \sum_{\substack{\ell\mid d,\ \ell\mid m\\d/\ell\ {\rm odd}}}
 \ell\,\mu(d/\ell)\chi(d/\ell)\chi(m/\ell).
\tag{142.43}
\]

The base complete sum used here is, with the convention that the right
side is zero unless (D\mid m),

\[
 \sum_{u\bmod4D}\chi(u)e(um/(4D))
 =2iD\chi(m/D).
\tag{142.44}
\]

Substituting (142.43) into (142.7) and writing (d=\ell k) proves the
finite, exact identity

\[
 \boxed{
 B_Q(m)={\pi\over4}\sum_{\ell\mid m}\chi(m/\ell)
 \sum_{\substack{k\leq Q/(4\ell)\\k\ {\rm odd}}}
 {\mu(k)\chi(k)\over k}.}
\tag{142.45}
\]

Thus the exact hard-cutoff reconstruction error is

\[
 \boxed{
 C(m)-B_Q(m)=C(m)-\sigma_\chi(m)
 +\sum_{\ell\mid m}\chi(m/\ell)
 \left[1-{\pi\over4}
 \sum_{\substack{k\leq Q/(4\ell)\\k\ {\rm odd}}}
 {\mu(k)\chi(k)\over k}\right].}
\tag{142.46}
\]

No convergence convention is hidden in (142.45)--(142.46).  If the
denominator order is regularized by (d^{-\eta}), (142.43) instead
gives

\[
 B_\eta(m)={\pi\over4}
 \sum_{\ell\mid m}\chi(m/\ell)\ell^{-\eta}
 \sum_{k\geq1}{\mu(k)\chi(k)\over k^{1+\eta}},
\tag{142.47}
\]

and the last series is (1/L(1+\eta,\chi)).  This proves
(142.10)--(142.12).  It also shows why an infinite rational-mode
subtraction cannot be asserted by formal rearrangement: the pointwise
Abel limit is the complete divisor coefficient and is not convergence
in a norm preserving the Bohr means.  In particular, the emerging
complete coefficient has additional rational means even though every
finite Fourier line (142.39) has denominator divisible by four.

To prove (142.8), note first that a mode in (B_Q) equals
(-a/q\pmod1) exactly when (4\mid q) and (q\leq Q); its coefficient
then cancels the main term in (142.2).  Every other frequency (c/s),
(s\leq Q), satisfies

\[
 \left\|{a\over q}+{c\over s}\right\|\geq {1\over qs}.
\tag{142.48}
\]

The finite geometric sum is therefore (O(qs)).  Multiplication by
(|b(c/s)|\ll1/s) and summation over all reduced (c) and
(s\leq Q) costs

\[
 O\!\left(q\sum_{s\leq Q}\varphi(s)\right)=O(qQ^2).
\tag{142.49}
\]

Equations (142.2), (142.48), and (142.49) prove (142.8), including both
the removed and surviving denominator ranges.

### 3.6 Local slopes, nonlinear branches, and the full (M,q,R) ledger

Let (F(t)=\sqrt{Nt}).  On (t\asymp M\leq C R^2), uniformly for
(0\leq q_X\leq2y),

\[
 |F''(t)|\asymp {R^2\over M^{3/2}},\qquad
 L_M:=|F''(M)|^{-1/2}\asymp {M^{3/4}\over R}.
\tag{142.50}
\]

On half-open physical intervals of length at most (cL_M), Taylor's
quadratic error is (O(c^2)), and the slope varies by (O(1/L_M)).
For (L_M\geq1), take the Farey order

\[
 Q_M:=\lceil L_M\rceil.
\tag{142.51}
\]

Every central slope modulo one has a reduced approximant (a/q),
(q\leq Q_M), with

\[
 |F'(t_0)-z-a/q|\leq {1\over qQ_M}\leq {1\over L_M}
\tag{142.52}
\]

for an integer (z).  A canonical disjoint assignment is obtained from
the Farey neighbors (a_-/q_-,a_+/q_+): use the half-open cell bounded
by the two mediants.  Its left and right widths from (a/q) are exactly

\[
 {1\over q(q+q_-)},\qquad {1\over q(q+q_+)}.
\tag{142.53}
\]

These cells have multiplicity one.  After thickening by the unavoidable
slope variation (O(1/L_M)) on a curvature interval, the broad rational
arcs have overlap (O(Q_M)=O(L_M)).  The slope winds through

\[
 \Delta_M=F'(M)-F'(2M)\asymp {R^2\over\sqrt M}
\tag{142.54}
\]

integer translates, so a fixed rational cell can recur
(O(1+\Delta_M)) times.  The number of physical curvature intervals is

\[
 J_M\asymp {M\over L_M}\asymp R M^{1/4}.
\tag{142.55}
\]

This gives the requested widths, endpoint convention, overlap, and
multiplicity.  For (M<R^{4/3}), one has (L_M<1), so there is no
nontrivial within-integer linearization cell at all.

The nonresonant condition in the frozen scalar is

\[
 |j_m|=|k_m^2-Nm|>\sqrt M,
\tag{142.56}
\]

which, through

\[
 \sqrt{Nm}-k_m=-{j_m\over k_m+\sqrt{Nm}},
\tag{142.57}
\]

controls a phase value.  Equations (142.50)--(142.54) concern the
derivative (F'(m)).  There is no implication from (142.56) to
separation from any rational derivative arc, and none is used here.

For (q\leq Q_M), (142.8) removes all rational main terms.  Since

\[
 Q_M\ll {M^{3/4}\over R}\leq M^{1/4}\qquad(M\leq R^2),
\tag{142.58}
\]

one has

\[
 qQ_M^2\leq Q_M^3\ll M^{3/4}.
\tag{142.59}
\]

Thus the residual reaches, up to logarithms, the necessary
(M^{3/4}) additive-partial-sum scale for the denominators actually
removed.  This is not an owner-complete scalar estimate: using it
separately on the (J_M) curvature intervals loses their full
multiplicity, and every (q>Q_M) mode remains as in (142.8).

It remains to price the extracted periodic branch itself.  For every
fixed rational (\beta), the smooth coefficient-free block obeys the
second-derivative and trivial bounds

\[
 \left|\sum_{m\asymp M}m^{-3/4}V(R^2m/N)
 e(\sqrt{Nm}+\beta m)\right|
 \ll
 \min\left\{M^{1/4},\ RM^{-1/2}+R^{-1}\right\}.
\tag{142.60}
\]

The accepted Round-141 congruence count shows that imposing
(|j_m|>\sqrt M) changes a coefficient-free branch by
(O_\varepsilon(X^\varepsilon)).  Summing (142.60) against the exact
spectral mass (142.24) therefore gives only

\[
 \boxed{
 |T_{B_Q,M}^{\rm nr}|
 \ll_\varepsilon Q\left(
 \min\{M^{1/4},RM^{-1/2}+R^{-1}\}+X^\varepsilon\right).}
\tag{142.61}
\]

With the scale-dependent cutoff (Q=Q_M), the right side is at best

\[
 O_\varepsilon(R^{1/2+\varepsilon})
\tag{142.62}
\]

uniformly over (M\leq R^2): for (M\geq R^{4/3}), the principal
product is (Q_M RM^{-1/2}\asymp M^{1/4}\leq R^{1/2}), while below
that transition the trivial bound is at most (R^{1/3}).  At the top
block,

\[
 M\asymp R^2,\qquad L_M\asymp Q_M\asymp R^{1/2},\qquad
 J_M\asymp R^{3/2},
\tag{142.63}
\]

and (142.61) is (R^{1/2+\varepsilon}), not (X^\varepsilon).
Restoring the Round-140 outer factor (N^{1/4}\asymp R) changes this
to (R^{3/2+\varepsilon}), against the required (R X^\varepsilon)
scale.  These are upper-capacity ledgers, not lower bounds.

Finally, Poisson or a (B)-process does not dispose of (142.60).  For a
dual integer (z), the shifted phase

\[
 \sqrt{Nm}+(\beta-z)m
\tag{142.64}
\]

has, when (z-\beta>0), the exact critical data

\[
 m_{z,\beta}={N\over4(z-\beta)^2},
 \qquad
 \sqrt{Nm_{z,\beta}}+(\beta-z)m_{z,\beta}
 ={N\over4(z-\beta)}.
\tag{142.65}
\]

This is the rationally shifted reciprocal family; a second transform
returns the original square-root branch.  At (\beta=-z_0/4), after a
harmless relabeling, (142.65) is exactly the Round-141 identity
(m=4N/z^2), critical value (N/z).  No noninvertible signed gain is
created.

## 4. First doubtful or unproved step

The first unproved step is not the rational coefficient algebra: that
algebra is closed by (142.2), (142.4), and (142.45).  The first open
analytic assertion required by a spectral subtraction is

\[
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>\sqrt M}}
 m^{-3/4}V_{\rm low}(R^2m/N)B_{Q_M}(m)e(\sqrt{Nm})
 \ll_\varepsilon X^\varepsilon,
\tag{142.66}
\]

together with an owner-complete assembly of the residual
(D_{Q_M}) across all (J_M) slope cells.  Neither is proved.
The elementary branch bound stops at (142.62), and the canonical
stationary transform gives (142.65), not a saving.

Letting the denominator cutoff tend to infinity does not remove this
gap.  In the explicit convergent order (142.9), the extracted branch is
the complete radial coefficient (\sigma_\chi=r_2/4); its square-root
twist is an owner-sized complete radial circle sum.  Its residual
(C-\sigma_\chi) leaves the entire (chi(n)=-1) far sector unchanged.
Therefore there is no strict owner-complete survivor and no target-safe
reconstruction error.

The first doubtful inference to reject is:

\[
 \text{``all rational means are known''}
 \quad\Longrightarrow\quad
 \text{``the fixed-centre nonlinear scalar is controlled.''}
\tag{142.67}
\]

The failure is exact: coefficient mass is non-(\ell^1) and
non-(\ell^2), finite cutoffs retain the tail (142.8), the Abel-complete
cutoff self-returns (142.10), slope cells have the multiplicity
(142.55), and phase-value nonresonance does not separate derivative
arcs.  A new signed fixed-centre correlation theorem would be needed.

## 5. Required control tests and outcomes

1. **`exact_cone_hyperbola_endpoints_and_parity`: pass.**  Equations
   (142.14)--(142.17) use the exact first odd integer (4h+1), the
   inclusive upper endpoint (r\leq M/h), the strict lower endpoint,
   and the exact last nonempty height.

2. **`reduced_rational_frequency_and_q_mod_4_cases`: pass.**  Equation
   (142.28) proves that a row mean is impossible for (4\nmid q), and
   (142.18) gives the complete (4\mid q) condition.  Reduction of
   (a/q) is used at the divisibility step.

3. **`row_mean_residue_classes_sign_and_constant`: pass.**  The two
   odd residue classes are encoded by the alternating row ratio.  The
   exact row value is (i\chi(a)\chi(\ell)), giving
   (i\pi\chi(a)/(2q)).  The signs (a=1,3\pmod4) are opposite; at
   (q=4) they are (+i\pi/8) and (-i\pi/8).

4. **`fixed_q_versus_growing_q_error_uniformity`: pass.**  Fixed (q)
   gives (O_q(\sqrt M)); the exact uniform error is
   (O((\sqrt M+q)\log(2q))), and the dominance range is explicitly
   (142.6).  No fixed-(q) result is advertised as uniform beyond it.

5. **`rational_spectrum_convergence_and_reconstruction`: pass as a
   no-go.**  The finite cutoff is (142.7), its exact arithmetic form is
   (142.45), and its exact error is (142.46).  The declared
   denominator-Abel order is (142.9) and reconstructs
   (\sigma_\chi), not (C).  Equations (142.24)--(142.25) rule out
   silent absolute or square-summable rearrangement.

6. **`local_derivative_arc_width_overlap_and_multiplicity`: pass as a
   no-go.**  Curvature length, Farey order, exact mediant widths,
   half-open endpoint ownership, thickened overlap, winding
   multiplicity, and physical cell count are (142.50)--(142.55).  The
   top values are recorded in (142.63).

7. **`nonresonant_phase_value_versus_slope_distinction`: pass.**
   Equations (142.56)--(142.57) are phase-value statements; the
   derivative statements are (142.50)--(142.54).  No implication is
   asserted between them.

8. **`residual_additive_partial_sum_hypothesis`: fail at owner-complete
   level.**  Removed denominators satisfy the necessary
   (M^{3/4+o(1)}) scale by (142.58)--(142.59), but larger denominators
   retain their main modes by (142.8), and separate use on the
   (J_M) physical cells loses their multiplicity.  This is not a
   bound for the nonlinear residual.

9. **`periodic_branch_all_dyadic_R_and_q_power_ledger`: fail at the
   target.**  The exact coefficient mass, per-branch van der Corput
   bound, microscopic deletion cost, scale-dependent cutoff, top
   block, and restored outer factor are (142.24),
   (142.60)--(142.63).  The surviving normalized excess is
   (R^{1/2+o(1)}).

10. **`raw_capacity_versus_fixed_centre_signed_scalar`: pass.**  The
    quantities (Q), (J_M), and (R^{1/2}) are used only to show
    that modulus assembly does not prove the target.  They are not
    claimed as lower bounds for the complex scalar; nonlinear branches
    may still cancel.

11. **`canonical_transform_self_return_and_downstream_scope`: pass.**
    Equations (142.64)--(142.65) give the exact reciprocal self-return.
    Equations (142.10)--(142.12) give the coefficient-completion
    self-return.  Neither proves a square, a lower GAR parent, a direct
    M1 parent, M9-M1, any M2 parent, endpoint uniformity, M9, the
    bridge, the quarter theorem, or a new exponent.

12. **Small/top scales and centre endpoints: pass.**  If (H_M=0),
    (142.17) is empty and (142.2) remains valid.  The top scale is
    (142.63).  The coefficient theorem is independent of (q_X), and
    all curvature estimates are uniform at (q_X=0) and (q_X=2y).

## 6. Dependencies and exact artifacts used

The derivation uses only the following permitted artifacts:

- `protocol.md`;
- `state/proof_obligations.yml`, graph SHA-256
  `de02111a1831d30da33c9f4b2d4a549efa1942dcdc32b5d829e671f6ad5e0e76`;
- `state/active_campaign.yml` for Round 142;
- `strategy/conductor_0823_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/candidates/conductor_round141_cone_nonresonant_reduction.md`;
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reviews/conductor_round141_incomplete_fibre_adjudication.md`;
- `rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/synthesis.md`.

Accepted Round-141 facts used are the exact cone coefficient, the
dyadic support (M\ll R^2), the singleton nearest-square cells, the
congruence price for (|j_m|\leq\sqrt M), the unsquared scalar
direction, the negative-character complete-fibre obstruction, and the
canonical reciprocal transform.  The rational row theorem, growing-
denominator error, complete spectrum, Möbius/Gauss reconstruction, and
slope-capacity ledger are derived here from first principles.

No web theorem, primary source, numerical computation, symbolic
experiment, centre average, positive energy, arbitrary-array model, or
desired circle estimate is used.  All work is analytic.  This report is
candidate evidence only and makes no shared-state mutation.

## 7. Recommended state effect

**Recommendation: retain the Round-141 open scalar and record this
report as a proved rational-spectrum obstruction; close the task under
`rational_major_arc_self_return_no_go`.**

The conductor may promote, after independent seam review, the narrow
facts (142.2), (142.4), (142.17)--(142.19), (142.41), (142.45), and
(142.10): the exact rational additive spectrum consists of every
reduced denominator divisible by four, with coefficient
(-i\pi\chi(c)/(2q)); the uniform error is
((\sqrt M+q)\log(2q)); and the declared full denominator-Abel
reconstruction is the complete radial divisor coefficient.

Record the obstruction that a finite cutoff retains all larger modes,
has non-summable total spectral mass, and leaves an unproved periodic
square-root branch; the full cutoff self-returns to
(\sigma_\chi=r_2/4), while (C-\sigma_\chi) leaves the
(chi(n)=-1) far sector unchanged.  Rational phase-value
nonresonance does not remove rational derivative arcs, and the local
cell multiplicity is not paid.

Make no promotion of the fixed-centre nonresonant cone bound, the
complete lower-radial signed estimate, lower GAR, either direct M1
parent, M9-M1, any M2 parent, M9-M2, endpoint uniformity, M9, the
conditional bridge, the quarter target, or either recorded exponent.
The exact Round-141 scalar remains open and still requires a genuinely
new signed fixed-centre correlation mechanism.
