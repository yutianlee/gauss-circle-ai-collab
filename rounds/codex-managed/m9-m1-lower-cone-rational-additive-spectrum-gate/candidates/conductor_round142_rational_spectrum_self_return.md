# Round 142 conductor candidate: rational spectrum and major-arc self-return

Campaign: `m9-m1-lower-cone-rational-additive-spectrum-gate`

Starting graph SHA-256:
`de02111a1831d30da33c9f4b2d4a549efa1942dcdc32b5d829e671f6ad5e0e76`

## 1. Result

Let (e(t)=e^{2\pi i t}) and

\[
C(m)=\sum_{\substack{hr=m,\ r\ {\rm odd}\\r>4h}}\chi _4(r).
\tag{142.C1}
\]

For every real (M\ge2) and every reduced rational (a/q), (q\ge1),

\[
\boxed{
 \sum_{m\le M}C(m)e(am/q)
 =\mathbf 1_{4\mid q}\,{i\pi\chi _4(a)\over2q}M
 +O\!\left((\sqrt M+q)\log(2q)\right).}
\tag{142.C2}
\]

Thus the quarter mode is one member of an infinite hierarchy indexed by
all reduced denominators divisible by (4).  Partial summation gives

\[
 \sum_{m\le M}m^{-3/4}C(m)e(am/q)
 =\mathbf 1_{4\mid q}\,{2i\pi\chi _4(a)\over q}M^{1/4}
 +O\!\left(q\log(2q)+1\right).
\tag{142.C3}
\]

The hierarchy does not prove the frozen nonlinear estimate and does not
give a strict owner-complete reduction.  The exact finite Fourier
reconstruction has a moving cone boundary of unsigned weighted capacity
\(\asymp M^{1/4}\), its rational coefficients are not absolutely or
square summable over growing denominators, and its smooth stationary
transform reassembles the already open reciprocal height--alias family.
Moreover, the prefix error in (142.C2) is longer than the natural local
slope cell on every active scale.  The round therefore closes, subject to
the assigned seam reviews, under
`rational_major_arc_self_return_no_go`.  The nonresonant cone scalar
remains open.

## 2. Exact rational-frequency theorem and proof

Unfolding (142.C1) gives the exact finite identity

\[
S_C(M;a/q)=
\sum_{4h^2<M}\ \sum_{4h<r\le M/h}
\chi _4(r)e(ahr/q),
\tag{142.C4}
\]

where extending the inner sum over all integers does not change it,
because \(\chi _4\) vanishes on the even integers.  The elementary
identity

\[
\chi _4(r)={e(r/4)-e(-r/4)\over2i}
\tag{142.C5}
\]

shows that the mean in the (h)-th row is

\[
\mu_h(a/q)={1\over2i}
\left(
 \mathbf1_{ah/q+1/4\in\mathbb Z}
 -\mathbf1_{ah/q-1/4\in\mathbb Z}
\right).
\tag{142.C6}
\]

For a rational \(\beta\), uniformly in real (A<B),

\[
\sum_{A<r\le B}e(\beta r)
=\mathbf1_{\beta\in\mathbb Z}(B-A)
+O\!\left(1+
 \mathbf1_{\beta\notin\mathbb Z}\|\beta\|^{-1}
\right).
\tag{142.C7}
\]

As (h) runs through a complete residue system modulo (q),
(ah/q\pm1/4) runs through a translate of the (q)-grid.  Ordering
the distances of this grid from the integers gives

\[
\sum_{\substack{1\le h<H\\ah/q\pm1/4\notin\mathbb Z}}
\left\|{ah\over q}\pm{1\over4}\right\|^{-1}
\ll (H+q)\log(2q).
\tag{142.C8}
\]

Taking (H=\sqrt M/2), with the strict endpoint (h<H), equations
(142.C4)--(142.C8) yield

\[
S_C(M;a/q)
=M\sum_{h<H}{\mu_h(a/q)\over h}
-4\sum_{h<H}h\mu_h(a/q)
+O((H+q)\log(2q)).
\tag{142.C9}
\]

The two integrality conditions in (142.C6) are

\[
4ah+q\equiv0\pmod{4q},\qquad
4ah-q\equiv0\pmod{4q}.
\tag{142.C10}
\]

They have no solution unless (4\mid q).  If (q=4Q), then (a) is
odd and, writing \(\bar a\) for its inverse modulo (q), the two
classes are

\[
h\equiv-\bar aQ\pmod q,\qquad
h\equiv\bar aQ\pmod q.
\tag{142.C11}
\]

Since \(\bar a\equiv a\pmod4\), this is equivalently

\[
\mu_h(a/q)={i\chi _4(a)\over2}
\left(\mathbf1_{h\equiv Q\ (4Q)}
-\mathbf1_{h\equiv3Q\ (4Q)}\right).
\tag{142.C12}
\]

Pairing the two classes in each complete period gives

\[
\sum_{h<H}h\mu_h(a/q)\ll H,
\tag{142.C13}
\]

while the Gregory series, including a possible final unpaired term,
gives uniformly in (H>0)

\[
\begin{aligned}
\sum_{h<H}{\mu_h(a/q)\over h}
&={i\chi _4(a)\over2Q}
\left(\sum_{4n+1<H/Q}{1\over4n+1}
-\sum_{4n+3<H/Q}{1\over4n+3}\right)\\
&={i\pi\chi _4(a)\over2q}+O(H^{-1}).
\end{aligned}
\tag{142.C14}
\]

Equations (142.C9), (142.C13), and (142.C14) prove (142.C2), including
both strict cone endpoints.  When (4\nmid q), the main term is absent
and (142.C8) alone gives the asserted error.  Abel summation of (142.C2)
proves (142.C3).  For (q=4,a=1), these constants specialize to
(i\pi M/8) and (i\pi M^{1/4}/2), exactly the accepted Round-141
control; (a=3) reverses the sign.

## 3. Exact finite spectrum and reconstruction obstruction

For each fixed height define

\[
g_h(m)=\mathbf1_{h\mid m}\chi _4(m/h).
\tag{142.C15}
\]

Its exact discrete Fourier expansion modulo (4h) is

\[
\boxed{
g_h(m)=-{i\over2h}
\sum_{\substack{b\ ({\rm mod}\ 4h)\\b\ {\rm odd}}}
\chi _4(b)e\!\left({bm\over4h}\right).}
\tag{142.C16}
\]

Indeed, the inner sum vanishes unless (h\mid m); for (m=hr) it is
(h(e(r/4)-e(3r/4))=2ih\chi _4(r)).  Consequently

\[
C(m)=-{i\over2}
\sum_{4h^2<m}{1\over h}
\sum_{\substack{b\ ({\rm mod}\ 4h)\\b\ {\rm odd}}}
\chi _4(b)e\!\left({bm\over4h}\right).
\tag{142.C17}
\]

For the fixed truncation (P_H(m)=\sum_{h\le H}g_h(m)), the coefficient
of the reduced mode (e(am/q)) is zero unless (4\mid q), and otherwise
is exactly

\[
\widehat P_H(a/q)
=-{2i\chi _4(a)\over q}
\sum_{\substack{t\le4H/q\\t\ {\rm odd}}}{\chi _4(t)\over t}
=-{i\pi\chi _4(a)\over2q}+O(H^{-1}).
\tag{142.C18}
\]

The limiting coefficient in (142.C18) is the coefficient conjugate to
the correlation in (142.C2).  It also shows why a denominator cutoff is
not a harmless projection:

\[
\sum_{\substack{q\le Q\\4\mid q}}
\sum_{(a,q)=1}\left|{\pi\over2q}\right|\asymp Q,
\qquad
\sum_{\substack{q\le Q\\4\mid q}}
\sum_{(a,q)=1}\left|{\pi\over2q}\right|^2\asymp\log Q.
\tag{142.C19}
\]

Thus the limiting rational series has neither absolute nor bounded
square spectral mass as (Q\to\infty).  This is a norm obstruction, not
a pointwise lower bound.

There is also an exact finite-projection obstruction.  Put

\[
A(a/q)=\mathbf1_{4\mid q}{i\pi\chi _4(a)\over2q},\qquad
P_Q(m)=\sum_{\substack{4\mid q\le Q}}
\sum_{(a,q)=1}A(a/q)e(-am/q).
\tag{142.C19a}
\]

For every fixed omitted reduced (b/s), (4\mid s) and (s>Q),
distinct-rational spacing and (142.C2) give

\[
\sum_{m\le M}(C(m)-P_Q(m))e(bm/s)
=A(b/s)M+O((\sqrt M+s)\log(2s)+sQ^2).
\tag{142.C19b}
\]

Indeed, an off-diagonal pair is separated by at least (1/(sq)), so
its geometric sum costs (O(sq)); multiplication by (1/q) and
summation over (O(Q^2)) reduced fractions gives (O(sQ^2)).  Thus no
finite denominator projection even leaves a complement with sublinear
means at all rational frequencies.

The arithmetic form of this projection identifies the full
reconstruction failure.  For (d\ge1), put

\[
\mathcal G_d(m)=
\sum_{\substack{c\ ({\rm mod}\ 4d)\\(c,4d)=1}}
\chi _4(c)e(cm/(4d)).
\tag{142.C19c}
\]

Möbius inversion of the unit condition and the primitive modulo-four
Gauss sum give

\[
\mathcal G_d(m)=2i
\sum_{\substack{\ell\mid(d,m)}}
\ell\,\mu(d/\ell)\chi _4(d/\ell)\chi _4(m/\ell),
\tag{142.C19d}
\]

where terms with even (d/\ell) vanish.  Therefore the projection in
(142.C19a) has the exact hard-cutoff form

\[
P_Q(m)={\pi\over4}\sum_{\ell\mid m}\chi _4(m/\ell)
\sum_{\substack{k\le Q/(4\ell)\\k\ {\rm odd}}}
{\mu(k)\chi _4(k)\over k}.
\tag{142.C19e}
\]

More canonically, damping denominator (4d) by (d^{-\eta}),
(\eta>0), gives the absolutely defined identity

\[
P_\eta(m)={\pi\over4L(1+\eta,\chi _4)}
\sum_{\ell\mid m}\chi _4(m/\ell)\ell^{-\eta}
\longrightarrow
\sigma_{\chi _4}(m)={r_2(m)\over4}.
\tag{142.C19f}
\]

Thus the natural denominator-Abel reconstruction of all limiting cone
modes is the complete radial coefficient, not (C).  Its residual is
(C-\sigma_{\chi _4}); when (m=2^\nu n) with
(\chi _4(n)=-1), the complete coefficient vanishes and this residual
is exactly (C(m)).  The accepted negative-character far owner is
therefore untouched.  This is an exact completion self-return, not a
convergence heuristic.

The moving cone boundary is the sharper owner obstruction.  On
(M\le m<2M), the fixed polynomial formed from (4h^2<M) leaves the
exact wedge

\[
W_M(m)=\sum_{\substack{h\mid m,\ r=m/h\ {\rm odd}\\
M\le4h^2<m}}\chi _4(r).
\tag{142.C20}
\]

Its unsigned incidence capacity satisfies

\[
\sum_{M\le m<2M}m^{-3/4}
\sum_{\substack{h\mid m,\ r=m/h\ {\rm odd}\\M\le4h^2<m}}1
\asymp M^{1/4}.
\tag{142.C21}
\]

For the lower bound, restrict \(h\) to a fixed subinterval of
\([\sqrt M/2,\sqrt{M/2})\); then \(4h<r<2M/h\) has
\(\asymp\sqrt M\) odd choices on each of \(\asymp\sqrt M\) rows.
The upper bound follows
from the same unfolded region.  At (M\asymp R^2), (142.C21) is
(R^{1/2}), so deleting the wedge by modulus is not target-safe.
Taking the height cutoff all the way to the moving boundary merely
restores the original joint cone.  Hence (142.C17) is an exact
reparameterization, not an owner-complete spectral reduction.

## 4. Local slopes, periodic branches, and canonical return

On \(m\asymp M\), let \(\Phi(m)=\sqrt{Nm}\).  Its curvature, natural
stationary-cell length, and derivative range are

\[
|\Phi''(m)|\asymp{R^2\over M^{3/2}},
\qquad
L_M:=|\Phi''(m)|^{-1/2}\asymp{M^{3/4}\over R},
\qquad
K_M\asymp{R^2\over\sqrt M}.
\tag{142.C22}
\]

The interval consequence of (142.C2) has error
(O((\sqrt M+q)\log(2q))), whereas

\[
{\sqrt M\over L_M}\asymp{R\over M^{1/4}}\ge R^{1/2}
\qquad(M\le C R^2).
\tag{142.C23}
\]

Thus the exact rational prefix theorem is much too coarse on the cells
where a local rational slope is approximately constant.  A fixed-(q)
Bohr coefficient is not the required short-interval residual theorem.
Dirichlet approximation at width (L_M^{-1}) may be made with
(Q_M=\lceil L_M\rceil); Farey spacing then gives raw overlap
(O(1+Q_M^2/L_M)=O(L_M)).  A deterministic tie-break makes the cells
disjoint but does not improve an absolute branch sum.
More precisely, there are (O(1+M/L_M)) half-open cells.  If (D) is
the residual after a proposed local mode subtraction, Abel summation on
each cell and then absolute assembly require

\[
\max_{\substack{q\le Q_M,(a,q)=1\\J\subset[M,2M),\ |J|\le L_M}}
\left|\sum_{m\in J}D(m)e(am/q)\right|
\ll_\varepsilon X^\varepsilon{\sqrt M\over R},
\tag{142.C23a}
\]

whereas subtraction using (142.C2) supplies only an
(O((\sqrt M+q)\log(2q))) error.  After the exact cell count and
(M^{-3/4}) weight, this is a factor (R) short.  In the range
(M\lesssim R^{4/3}), (L_M\lesssim1) and the cells are singletons,
so a cellwise additive argument supplies no cancellation at all.

The accepted smooth (B)-process makes the structural return explicit.
For one branch (\beta=b/(4h)), the critical equation for
\(\Phi(x)+\beta x-kx\), with (k-\beta>0), is

\[
x_k={N\over4(k-\beta)^2}={4Nh^2\over(4hk-b)^2},
\qquad
\Phi(x_k)+\beta x_k-kx_k={Nh\over4hk-b}.
\tag{142.C24}
\]

Stationary phase cancels the weight exactly:

\[
x_k^{-3/4}|\Phi''(x_k)|^{-1/2}=2N^{-1/4}\asymp{2\over R}.
\tag{142.C25}
\]

Put (z=4hk-b).  Since (z\equiv-b\pmod{4h}),
\(\chi _4(z)=-\chi _4(b)\).  Multiplying the principal transform by
the exact Fourier coefficient in (142.C16) gives

\[
{iN^{-1/4} e(-1/8)\over h}
\sum_{\substack{z>0,\ z\equiv-b\ (4h)\\z\ {\rm odd}}}
\chi _4(z)
W\!\left({4Nh^2\over Mz^2}\right)e(Nh/z),
\tag{142.C26}
\]

at the level of the stationary principal family; its coefficient has
size (\asymp(hR)^{-1}).  Summing the odd
residues (b\pmod{4h}) removes the congruence and
reassembles the reciprocal height--alias family from which (142.C1)
was obtained.  The full reassembled smooth transform has the accepted
Round-140 endpoint and remainder ledger; an artificial branchwise split
would have to re-establish that ledger rather than inherit each error
separately.  A second stationary transform returns the square-root
phase.  Branchwise principal modulus has capacity

\[
{K_M\over R}\asymp{R\over\sqrt M}
\tag{142.C27}
\]

before its rational coefficient; summing all (2h) Fourier branches of
size (1/(2h)) and all (h\ll\sqrt M) gives (R^{1+o(1)}), not
(R^\epsilon).  This capacity statement is not a signed lower bound;
it records exactly where branchwise estimates lose the required gain.

The Round-141 condition \(|k_m^2-Nm|>\sqrt M\) concerns the value
\(\Phi(m)\), while (142.C24) concerns its derivative.  If (q=4Q) and
the stationary point (Nq^2/[4(qk-a)^2]) happens to be an integer, then
coprimality forces (q^2\mid4m), hence (q\mid m), and
\(\sqrt{Nm}=2m(k-a/q)\) is an integer; that exceptional integer is an
already removed exact radical.  For a nonresonant integer (m), exact
equality (\Phi'(m)=u/q) is impossible.  The integrality identity
\[
 \left|\Phi'(m)-{u\over q}\right|
 ={\left|Nq^2-4mu^2\right|\over
 4mq^2\bigl(\Phi'(m)+u/q\bigr)}
 \ge {1\over4mq^2\bigl(\Phi'(m)+u/q\bigr)}
\tag{142.C24a}
\]
gives only (\gg(q^2\sqrt{NM})^{-1}) near the relevant slope, far
smaller than (L_M^{-1}).  Thus phase-value nonresonance supplies no
major-arc exclusion at the scale used here.

At the level of the whole cone scalar, the Round-141 absolute estimate
allows the removed phase-value cells to be restored before (142.C16).
After the Fourier polynomial is split into individual modes, however,
that estimate cannot be assigned mode by mode: it controls the original
coefficient (C), not each periodic projection and the wedge
separately.  This is another owner seam, not permission to put the
discontinuous mask into a smooth branch estimate for free.

## 5. First doubtful or unproved step

The first open estimate remains

\[
\boxed{
\sum_M\sum_{\substack{m\in\mathcal I_M\\|k_m^2-Nm|>\sqrt M}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
\ll_\varepsilon X^\varepsilon.}
\tag{142.C28}
\]

To turn (142.C2) into a strict major-arc reduction one would first need
the short-interval theorem (142.C23a), uniformly over
the required growing denominators, whose residual is stable under the
moving cone boundary.  One would then have to prove every periodic
branch target-safe after (142.C24), sum its full (q)-dependence, and
bound (142.C20) or an equivalent reconstruction residual.  None of
(142.C2), (142.C16), the accepted nonresonant mask, or the canonical
transform supplies those estimates.  The exact transform instead
returns the prior reciprocal owner in (142.C26).

In particular, a coefficient main term at (a/q), the divergent norm
capacities in (142.C19), or the branch capacity in (142.C27) is neither
a bound nor a lower bound for (142.C28).  Nonlinear phases from distinct
cells, numerators, denominators, and conjugate directions may cancel.

## 6. Required controls, dependencies, and outcomes

The (q\not\equiv0\pmod4) case has zero row mean; the (q=4Q) case has
exactly the two classes (Q,3Q\pmod{4Q}), with sign
(i\chi _4(a)/2).  The controls (q=4,a=1) and (a=3) recover opposite
quarter-mode constants.  Equations (142.C4), (142.C9), and (142.C20)
retain the strict lower and upper cone endpoints.  The estimate is
uniform in growing (q), but it is asymptotic only where its displayed
main term dominates its displayed error; no fixed-(q) statement is
silently used as a denominator sum.

The exact finite reconstruction, limiting spectrum, wedge incidence,
slope-cell length, derivative range, stationary amplitude, (R)-power,
and canonical return are explicit in (142.C16)--(142.C27).  The
nonresonant condition is kept separate from derivative distance.  All
capacity statements are labelled unsigned or branchwise and are not
used as scalar lower bounds.

Dependencies are `protocol.md`, the active graph and campaign, the
accepted Round-141 candidate/adjudication/synthesis, and the accepted
Round-140 smooth height--alias transform inherited through Round 141.
The three assigned Round-142 reports and post-candidate seam reviews
will be incorporated before closure.  No numerical experiment, centre
average, positive energy, arbitrary-array surrogate, or desired circle
estimate is used; the allocation is 100 percent analytical/source
verification.

The conclusion changes only the mechanism ledger for (142.C28).  It
does not prove a square identity, the lower GAR, either direct M1 parent,
M9-M1, any M2 parent, M9-M2, endpoint uniformity, M9, the conditional
bridge, or the Gauss-circle target.  The internally proved exponent
remains (1/3), and the separately audited external Li--Yang exponent
remains

\[
{3292+25\sqrt{1717}\over13762}
=0.3144831759740614\ldots.
\tag{142.C29}
\]

## 7. Recommended state effect

Create one proved obstruction recording (142.C2), (142.C6),
(142.C12), (142.C16)--(142.C21), and (142.C22)--(142.C27): the cone has
the full (4\mid q) rational hierarchy with exact constants and a
growing-(q) error; exact finite Fourier reconstruction leaves an
owner-sized moving-boundary wedge; the limiting spectrum has divergent
branch norms; its denominator-Abel reconstruction is the complete
(r_2/4) owner and leaves the negative-character cone unchanged; local
slope cells are shorter than the available rational partial-sum error;
and the branchwise stationary transform reassembles the reciprocal
height--alias owner.

Update the Round-141 cone reduction, the Round-141 incomplete-fibre
obstruction, and the global lower-radial signed owner to retain
(142.C28) as the first open scalar while parking unqualified rational
mode subtraction and derivative-major-arc reconstruction.

Reject claims that (1/4) is the only main mode; that fixed-(q)
asymptotics provide short-interval or denominator-uniform residual
control; that a finite rational projection reconstructs the moving cone
at target cost; that phase-value nonresonance is slope separation; that
individual periodic branches or their denominator sum are target-safe
without the displayed ledger; or that raw spectral capacity is a signed
lower bound.  Make no downstream theorem or exponent change.
