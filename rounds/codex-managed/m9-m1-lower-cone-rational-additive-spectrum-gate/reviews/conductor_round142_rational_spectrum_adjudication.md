# Round 142 conductor adjudication: the full rational spectrum is exact, but its reconstruction self-returns

Campaign: m9-m1-lower-cone-rational-additive-spectrum-gate

Starting graph SHA-256:
de02111a1831d30da33c9f4b2d4a549efa1942dcdc32b5d829e671f6ad5e0e76

## 1. Result and decision

Close Round 142 under
\(\mathsf{rational\_major\_arc\_self\_return\_no\_go}\).
Let

\[
C(m)=\sum_{\substack{hr=m,\ r\ {\rm odd}\\r>4h}}\chi _4(r),
\qquad e(t)=e^{2\pi it}.
\tag{142.J1}
\]

For every reduced rational \(a/q\), \(q\ge1\), and every real
\(M\ge2\), Round 142 proves the uniform theorem

\[
\boxed{
\sum_{m\le M}C(m)e(am/q)
=\mathbf1_{4\mid q}{i\pi\chi _4(a)\over2q}M
+O\!\left((\sqrt M+q)\log(2q)\right).}
\tag{142.J2}
\]

Thus \(1/4\) is not an isolated bad direction: every reduced
denominator divisible by four carries a linear mean.  Nevertheless,
the rational hierarchy does not prove the frozen nonlinear estimate and
does not yield a strict owner-complete reduction.  Every finite
projection leaves all omitted modes; the limiting coefficients have
divergent absolute and squared mass; their canonical denominator-Abel
sum reconstructs the complete coefficient \(r_2/4\), not the moving
cone; and the negative-character cone survives that completion
unchanged.  Local slope cells require a residual norm a factor \(R\)
stronger than (142.J2), while the stationary principal family
reassembles the reciprocal height--alias family.

The decision is based on proof seams, not a vote.  The statement-only
lane independently recovered the row constants, uniform error, local
cell scale, residual norm, and reconstruction obstruction.  Two
independent post-unmask audits checked the exact Gauss--Möbius--Abel
constants and the stationary signs.  A source cross-review initially
found an inapplicable Jutila hypothesis and an overstatement of the
two-step transform; the source report was repaired to retain only the
rigorous direct branch bound and principal-symbol self-return.  All
final review seams are green.

## 2. Exact rational-frequency theorem

Unfolding the strict cone gives

\[
S_C(M;a/q)=
\sum_{4h^2<M}\ \sum_{4h<r\le M/h}
\chi _4(r)e(ahr/q).
\tag{142.J3}
\]

Since

\[
\chi _4(r)={e(r/4)-e(-r/4)\over2i},
\tag{142.J4}
\]

the mean of the \(h\)-row is

\[
\mu_h(a/q)={1\over2i}
\left(
\mathbf1_{ah/q+1/4\in\mathbb Z}
-\mathbf1_{ah/q-1/4\in\mathbb Z}
\right).
\tag{142.J5}
\]

No row resonates unless \(4\mid q\).  If \(q=4Q\), the two classes
are \(h\equiv Q,3Q\pmod{4Q}\), with respective means
\((i/2)\chi _4(a)\) and \(-(i/2)\chi _4(a)\).  Summing the
nonconstant rows over complete \(h\)-periods uses the reciprocal
root-spacing bound

\[
\sum_{h\ ({\rm mod}\ q)}^{\!*}
\left\|{ah\over q}\mathbin{\pm}{1\over4}\right\|^{-1}
\ll q\log(2q).
\tag{142.J6}
\]

The exact lower boundary contributes the paired sum
\(\sum h\mu_h=O(\sqrt M)\), and the reciprocal rows give

\[
\sum_{h<\sqrt M/2}{\mu_h(a/q)\over h}
={i\pi\chi _4(a)\over2q}+O(M^{-1/2}).
\tag{142.J7}
\]

Equations (142.J3)--(142.J7), including the strict condition
\(4h^2<M\), the first odd integer \(4h+1\), and the upper floor,
prove (142.J2).  Its main term is relatively asymptotic when

\[
\left({q\over\sqrt M}+{q^2\over M}\right)\log(2q)=o(1);
\tag{142.J8}
\]

the simpler condition \(q\log(2q)=o(\sqrt M)\) is sufficient.
Abel summation gives

\[
\sum_{m\le M}m^{-3/4}C(m)e(am/q)
=\mathbf1_{4\mid q}{2i\pi\chi _4(a)\over q}M^{1/4}
+O\!\left(q\log(2q)+1\right).
\tag{142.J9}
\]

At \(q=4\), (142.J2)--(142.J9) recover the accepted Round-141
constants \(i\pi M/8\) and \(i\pi M^{1/4}/2\).

## 3. Finite spectrum and exact reconstruction obstruction

For

\[
g_h(m)=\mathbf1_{h\mid m}\chi _4(m/h),
\tag{142.J10}
\]

the exact finite Fourier identity is

\[
g_h(m)=-{i\over2h}
\sum_{\substack{b\ ({\rm mod}\ 4h)\\b\ {\rm odd}}}
\chi _4(b)e(bm/(4h)).
\tag{142.J11}
\]

Consequently \(C(m)=\sum_{4h^2<m}g_h(m)\).  If the height sum is
cut at \(h\le H\), the coefficient of a reduced positive frequency
\(a/q\) is zero unless \(4\mid q\), and otherwise equals

\[
-{2i\chi _4(a)\over q}
\sum_{\substack{t\le4H/q\\t\ {\rm odd}}}{\chi _4(t)\over t}
=-{i\pi\chi _4(a)\over2q}+O(H^{-1}).
\tag{142.J12}
\]

The limiting coefficient masses satisfy

\[
\sum_{\substack{q\le Q\\4\mid q}}
\sum_{(a,q)=1}{\pi\over2q}\asymp Q,
\qquad
\sum_{\substack{q\le Q\\4\mid q}}
\sum_{(a,q)=1}{\pi^2\over4q^2}\asymp\log Q.
\tag{142.J13}
\]

Hence denominator truncations are neither absolutely convergent nor
Cauchy in Besicovitch mean square.  This is a norm obstruction, not a
pointwise or signed lower bound.

The finite residual is also exact.  Put

\[
A(a/q)=\mathbf1_{4\mid q}{i\pi\chi _4(a)\over2q},
\qquad
P_Q(m)=\sum_{\substack{4\mid q\le Q}}
\sum_{(a,q)=1}A(a/q)e(-am/q).
\tag{142.J14}
\]

For a fixed omitted reduced \(b/s\), \(4\mid s\) and \(s>Q\),

\[
\sum_{m\le M}(C(m)-P_Q(m))e(bm/s)
=A(b/s)M+O\!\left((\sqrt M+s)\log(2s)+sQ^2\right).
\tag{142.J15}
\]

Thus no finite projection has a rationally mean-zero complement.

The canonical infinite grouping identifies the deeper self-return.  Set

\[
\mathcal G_d(m)=
\sum_{\substack{c\ ({\rm mod}\ 4d)\\(c,4d)=1}}
\chi _4(c)e(cm/(4d)).
\tag{142.J16}
\]

Möbius inversion and the primitive Gauss sum \(\tau(\chi _4)=2i\)
give

\[
\mathcal G_d(m)=2i
\sum_{\ell\mid(d,m)}
\ell\mu(d/\ell)\chi _4(d/\ell)\chi _4(m/\ell).
\tag{142.J17}
\]

Therefore the hard cutoff has the exact form

\[
P_Q(m)={\pi\over4}\sum_{\ell\mid m}\chi _4(m/\ell)
\sum_{\substack{k\le Q/(4\ell)\\k\ {\rm odd}}}
{\mu(k)\chi _4(k)\over k}.
\tag{142.J18}
\]

If complete numerator sets are summed first and denominators are
damped by \(d^{-\eta}\), \(\eta>0\), absolute convergence gives

\[
P_\eta(m)={\pi\over4L(1+\eta,\chi _4)}
\sum_{\ell\mid m}\chi _4(m/\ell)\ell^{-\eta}
\longrightarrow
\sigma_{\chi _4}(m)={r_2(m)\over4}.
\tag{142.J19}
\]

This reconstructs the complete radial coefficient, not \(C\).  If
\(m=2^\nu n\), \(n\) odd, and \(\chi _4(n)=-1\), then
\(\sigma_{\chi _4}(m)=0\); hence \(C-\sigma_{\chi _4}=C\) on that
sector.  The exact completion leaves the accepted negative-character
far owner untouched.

Finally, fixing \(4h^2<M\) on \(M\le m<2M\) leaves the moving wedge

\[
W_M(m)=\sum_{\substack{h\mid m,\ r=m/h\ {\rm odd}\\
M\le4h^2<m}}\chi _4(r).
\tag{142.J20}
\]

Its unsigned \(m^{-3/4}\)-weighted incidence mass is
\(\asymp M^{1/4}\), hence \(\asymp R^{1/2}\) at the top block.
It cannot be deleted by modulus, while taking the cutoff to the moving
boundary simply restores the original joint cone.

## 4. Local slopes, periodic branches, and source scope

For \(\Phi(m)=\sqrt{Nm}\) on \(m\asymp M\),

\[
|\Phi''(m)|\asymp{R^2\over M^{3/2}},
\qquad
L_M\asymp{M^{3/4}\over R},
\qquad
K_M\asymp{R^2\over\sqrt M}.
\tag{142.J21}
\]

Farey fractions of order \(Q_M\asymp L_M\) cover slope arcs of
width \(L_M^{-1}\); the raw thickened overlap is \(O(L_M)\).
There are \(O(1+M/L_M)\) half-open physical cells.  If \(D\) is the
residual after a proposed mode subtraction, absolute cell assembly
requires

\[
\max_{\substack{q\le Q_M,\ (a,q)=1\\
J\subset[M,2M),\ |J|\le L_M}}
\left|\sum_{m\in J}D(m)e(am/q)\right|
\ll_\varepsilon X^\varepsilon{\sqrt M\over R}.
\tag{142.J22}
\]

The prefix theorem (142.J2) supplies only
\(O((\sqrt M+q)\log(2q))\), losing a factor \(R\) after the exact
cell count and weight.  For \(M\lesssim R^{4/3}\), \(L_M\lesssim1\)
and the cells are singletons.

The Round-141 deletion condition concerns the phase value, not its
derivative.  For a nonresonant integer \(m\), exact equality
\(\Phi'(m)=u/q\) is impossible, but integrality gives only

\[
\left|\Phi'(m)-{u\over q}\right|
={|Nq^2-4mu^2|\over4mq^2(\Phi'(m)+u/q)}
\ge {1\over4mq^2(\Phi'(m)+u/q)}
\gg {1\over q^2\sqrt{NM}}.
\tag{142.J23}
\]

This is far smaller than \(L_M^{-1}\), so phase-value nonresonance
does not exclude the derivative arcs.

For a coefficient-free smooth periodic branch, the rigorous
second-derivative estimate is

\[
\left|\sum_m m^{-3/4}W(m/M)
e(\sqrt{Nm}-am/q)\right|
\ll_W\min\{M^{1/4},RM^{-1/2}+R^{-1}\}.
\tag{142.J24}
\]

Summing the exact coefficient mass over all fixed-height denominators
gives only the owner-sized bound
\(\min\{M^{3/4},R+\sqrt M/R\}\).  At the local cutoff it still has
top-block capacity \(R^{1/2+o(1)}\).

The stationary algebra is diagnostic only.  For
\(\beta=b/(4h)\), \(k-\beta>0\), and \(z=4hk-b>0\),

\[
x_k={4Nh^2\over z^2},
\qquad
\Phi(x_k)+\beta x_k-kx_k={Nh\over z},
\qquad
x_k^{-3/4}|\Phi''(x_k)|^{-1/2}=2N^{-1/4}.
\tag{142.J25}
\]

Multiplication by the exact branch coefficient gives the stationary
principal family with coefficient
\(iN^{-1/4}e(-1/8)\chi _4(z)/h\).  Summing residues removes the
congruence, and the matching second saddle reproduces the original
square-root phase, character, amplitude, and formal strict condition
\(j>4h\).  This is principal-symbol self-return only.  No branchwise
first- or second-stage remainder, hard endpoint, or Fresnel transition
is proved; the accepted Round-140 ledger applies only after complete
reassembly.

The repaired source audit is correspondingly negative and precise.
Jutila's holomorphic-amplitude theorem does not cover an arbitrary
nonzero \(C_c^\infty\) weight; his divisor formula has complete
\(d(n)\) and a cosine.  Kaneko's Ramanujan expansion assumes
\(\Re\xi>0\) and reconstructs a complete \(\sigma_\xi\).  The
Banerjee--Khurana theorems require \(0<\Re\nu<1/2\), analytic tests,
and a complete generalized-divisor coefficient.  No audited theorem
provides the conic local residual (142.J22) or a bound for the required
individual complex direction.

## 5. First open step and directionality

The first open scalar is unchanged:

\[
\boxed{
\sum_M\sum_{\substack{m\in\mathcal I_M\\
|k_m^2-Nm|>\sqrt M}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
\ll_\varepsilon X^\varepsilon.}
\tag{142.J26}
\]

A rational-slope continuation would have to prove (142.J22) uniformly
for growing denominators, keep the moving boundary stable, and prove
every extracted masked periodic branch target-safe.  Neither the exact
means, the finite DFT, the Abel completion, nor the principal-symbol
transform supplies those estimates.

The quantities in (142.J13), (142.J20), and the branch-capacity ledger
are norms or unsigned capacities.  They are not upper or lower bounds
for (142.J26).  Distinct cells, numerators, denominators, conjugate
directions, and the original coefficient may still cancel.  Round 142
therefore proves a mechanism obstruction, not failure of the desired
estimate.

The Round-141 equivalence remains unsquared.  No collar--tail cross
term, lift-dependent square identity, or positive residual deletion is
obtained.  The complete lower-radial estimate, lower GAR, both direct
M1 parents, M9-M1, all M2 parents, M9-M2, endpoint uniformity, M9, the
conditional bridge, and the quarter theorem remain open.

## 6. Reviews, controls, dependencies, and exponent status

The final post-unmask reviews are green:

1. `blind_post_unmask_rational_reconstruction_audit.md` independently
   checked the row constants, fixed-height DFT, finite residual,
   spectral norms, Gauss--Möbius--Abel reconstruction, moving wedge,
   local cell powers, repaired phase/slope distinction, and principal
   stationary sign.
2. `source_post_unmask_abel_bprocess_audit.md` independently rederived
   the primitive Gauss sum, hard and Abel constants, negative-character
   residual, both saddle symbols, positivity condition, strict-cone
   correspondence, and full \(R/q\) capacity.
3. `discovery_post_unmask_source_bprocess_audit.md` checked the primary
   sources and initially returned RED.  After repair it is GREEN: source
   locations and hypotheses are exact, the direct branch bound is
   separated from transform algebra, and the two-step claim is limited
   to principal-symbol self-return.

All twelve frozen controls have determinate outcomes.  Exact cone
endpoints, parity, \(q\bmod4\), signs, constants, growing-
\(q\) error, reconstruction order, local slope geometry,
phase-value/derivative separation, direct branch powers, source
hypotheses, capacity direction, and canonical principal self-return are
green.  The residual local theorem and frozen scalar are deliberately
open and cause the terminal no-go label.

Dependencies are `protocol.md`, the graph and active campaign, the
accepted Round-140 height--alias artifacts, the accepted Round-141 cone
reduction, the three Round-142 reports, the conductor candidate, and
the three final-green cross-reviews.  No numerical or symbolic
experiment, centre average, positive energy, arbitrary-array
surrogate, or desired circle estimate was used; allocation was 100
percent analytical and source-based.

The strongest internally proved exponent remains \(1/3\).  The
separately audited external Li--Yang exponent remains

\[
{3292+25\sqrt{1717}\over13762}
=0.3144831759740614\ldots.
\tag{142.J27}
\]

## 7. Recommended State Patch

Create one proved obstruction recording (142.J2), (142.J11)--
(142.J20), and (142.J21)--(142.J25): the cone has the complete
\(4\mid q\) rational hierarchy with a sharp growing-denominator error;
finite projections leave omitted modes; the limiting spectrum is not
absolutely or mean-square summable; denominator-Abel completion returns
\(r_2/4\) and leaves the negative-character cone unchanged; the moving
boundary has owner-sized unsigned capacity; local cells require the
unproved norm (142.J22); and stationary principal symbols self-return.

Update the Round-141 cone reduction, incomplete-fibre obstruction,
Round-140 height--alias obstruction, and global lower-radial owner with
this evidence.  Leave (142.J26) as the first open scalar and park
unqualified rational-mode subtraction and derivative-major-arc
reconstruction.

Reject claims that \(1/4\) is the only rational mode; that a fixed-
\(q\) asymptotic is a local residual theorem; that finite or
unregularized rational projections reconstruct the cone; that the Abel
limit is \(C\); that complete radial extraction removes the negative-
character sector; that phase-value nonresonance is derivative
separation; that branchwise errors are inherited; or that any displayed
capacity is a signed lower bound.  Make no downstream theorem or
exponent change.
