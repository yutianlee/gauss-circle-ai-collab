# Round 138 hostile audit: the signed lower-GAR Farey scalar

## 1. Result

**strict_signed_farey_reduction**

The target estimate is not proved. There is nevertheless an exact,
owner-complete reduction strictly smaller than the scalar square: the
whole same-denominator block and the whole cross-denominator exact
phase-collision block are target-safe with the actual coefficients. The
sole survivor is the signed cross-denominator, noncollision sum. None of
character pairing, determinant grouping, reciprocity, finite Fourier
completion, direct Poisson summation, or a B-process bounds this survivor
at the target scale. In particular, the square-root stationary family is
an interior principal family, not a replacement identity for the finite
Farey scalar.

## 2. Exact statement and hypotheses

Use exactly the literal data in (138.B1)--(138.B4):

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor,
\]

\[
 \lambda_b=\frac{\chi_4(b)}{b}L_\chi(y/b),\qquad
 |L_\chi(T)|\leq 1.
\]

Let

\[
 \mathscr I=\left\{(a,b):
 \begin{array}{l}
 2\leq b\leq y,\ b\ \mathrm{odd},\ 1\leq a<b,\ (a,b)=1,\\
 J_{R,y}(a/b)\neq0
 \end{array}\right\}.
\]

For \(i=(a,b)\in\mathscr I\), put

\[
 u_i=\lambda_bJ_{R,y}(a/b),\qquad
 \theta_i=\frac{Na}{b}\pmod 1.
\]

The literal support and coefficients give

\[
 |u_{a,b}|\ll \frac1a,\qquad a\ll\frac bR.
\tag{2.1}
\]

Define three disjoint ordered-pair owners:

\[
 \mathcal S_{\mathrm{row}}
 =\sum_b\left|
 \sum_{a:(a,b)\in\mathscr I}u_{a,b}e(\theta_{a,b})
 \right|^2,
\tag{2.2}
\]

\[
 \mathcal S_{\mathrm{col}}^\times
 =\sum_{\substack{i,j\in\mathscr I\\
                   b_i\neq b_j\\
                   \theta_i=\theta_j}}
 u_i\overline{u_j},
\tag{2.3}
\]

and

\[
 \mathcal S_{\mathrm{nr}}^\times
 =\sum_{\substack{i,j\in\mathscr I\\
                   b_i\neq b_j\\
                   \theta_i\neq\theta_j}}
 u_i\overline{u_j}\,e(\theta_i-\theta_j).
\tag{2.4}
\]

All phase equalities are modulo \(1\). Since every ordered pair and its
reverse are retained, (2.3) and (2.4) are real. The exact partition and
the proved owner bounds are

\[
 |\mathcal F_N|^2
 =\mathcal S_{\mathrm{row}}
  +\mathcal S_{\mathrm{col}}^\times
  +\mathcal S_{\mathrm{nr}}^\times,
\tag{2.5}
\]

\[
 0\leq\mathcal S_{\mathrm{row}}\ll y\log^2(2X),\qquad
 |\mathcal S_{\mathrm{col}}^\times|
 \ll_\varepsilon yX^\varepsilon.
\tag{2.6}
\]

In the last owner, reducedness implies

\[
 b_i\neq b_j,\qquad
 \Delta=a_ib_j-a_jb_i\neq0,\qquad
 b_ib_j\nmid N\Delta.
\tag{2.7}
\]

Since \(y\asymp R^2\), with the usual renaming of epsilon, the original
target is equivalent to

\[
 |\mathcal S_{\mathrm{nr}}^\times|
 \ll_\varepsilon yX^\varepsilon.
\tag{2.8}
\]

For proving the target, the one-sided upper bound
\(\mathcal S_{\mathrm{nr}}^\times\ll_\varepsilon yX^\varepsilon\)
already suffices. No such survivor estimate is established here.

## 3. Proof or derivation

**Flat cone, exact lift, and centre.** On every supported sample in
(138.B5), the certified lower support has \(1\leq h<d\leq y\), while
\(yh/d\geq1\). Hence the cutoff is literally one and

\[
 \frac1hV_{\mathrm{low}}(4R^2h^2/d^2)
 =\frac1dJ_{R,y}(h/d).
\tag{3.1}
\]

Thus the flat cone is exactly

\[
 \sum_{d\leq y}\frac{\chi_4(d)}d
 \sum_{1\leq h<d}J_{R,y}(h/d)e(Nh/d).
\tag{3.2}
\]

Write a nonzero fraction uniquely as \(h/d=a/b\), where
\((a,b)=1\), \(h=ag\), and \(d=bg\). Since
\(\chi_4(d)\neq0\) forces \(b\) and \(g\) odd, its complete lift
coefficient is

\[
 \sum_{g\leq y/b}\frac{\chi_4(bg)}{bg}
 =\frac{\chi_4(b)}b\sum_{g\leq y/b}\frac{\chi_4(g)}g
 =\lambda_b.
\tag{3.3}
\]

This proves the exact flat-cone-to-Farey identity without taking a norm
before aggregating the lifts. The only \(b=1\) class in the finite
completion is the zero residue. Its value is exactly zero because
\(J_{R,y}(0)=0\), so there is no centre correction. The opposite scalar
sign is the complex conjugate because the profiles and \(\chi_4\) are
real.

**Literal coefficient and equality diagonal.** For a rational sample,
\(ya/b\geq y/b\geq1\), so the lower cutoff is one. The upper profile
support only restricts \(a\ll b/R\). Moreover,

\[
 |\lambda_bJ_{R,y}(a/b)|
 \leq\frac1b\,O(b/a)\ll\frac1a,
\]

which proves (2.1). Squaring before any partial modulus gives exactly

\[
 |\mathcal F_N|^2
 =\sum_{i,j\in\mathscr I}u_i\overline{u_j}
 e\!\left(
 \frac{N(a_ib_j-a_jb_i)}{b_ib_j}
 \right).
\tag{3.4}
\]

For reduced fractions, \(a_ib_j-a_jb_i=0\) if and only if \(i=j\).
Consequently the equality diagonal satisfies

\[
 \sum_{i\in\mathscr I}|u_i|^2
 \ll\sum_{b\leq y}\sum_{a\ll b/R}\frac1{a^2}
 \ll y.
\tag{3.5}
\]

**The entire same-denominator block.** Keeping all unequal numerators
and their actual phases, its ordered-pair sum is exactly the
nonnegative row square (2.2). For each \(b\),

\[
 \sum_{a:(a,b)\in\mathscr I}|u_{a,b}|
 \ll\sum_{a\ll b/R}\frac1a
 \ll\log(2+b/R).
\]

Therefore

\[
 0\leq\mathcal S_{\mathrm{row}}
 \ll\sum_{b\leq y}\log^2(2+b/R)
 \ll y\log^2(2X).
\tag{3.6}
\]

This deletion is stronger than deleting only the equality diagonal and
loses no coefficient direction.

**Exact phase-collision fibres.** Fix a term \(a/b\), let
\(g=(N,b)\), \(q=b/g\), and write \(N=gn\). Then
\((n,q)=1\), \((a,q)=1\), and

\[
 \frac{Na}{b}=\frac{na}{q}\pmod1.
\tag{3.7}
\]

Conversely, fix a nonzero phase in its unique reduced form \(r/q\),
where \(q>1\). Every term in this fibre has

\[
 b=qg,\qquad g\mid N,\qquad qg\leq y,\qquad
 q,g\ \mathrm{odd},\qquad
 (q,N/g)=1,
\tag{3.8}
\]

and its numerator lies in the single residue class

\[
 a\equiv r\,(N/g)^{-1}\pmod q,
\tag{3.9}
\]

subject also to \((a,qg)=1\) and the literal profile support. Those
extra restrictions only delete terms. For each fixed \(g\),

\[
 \sum_{\substack{a\ll qg/R\\a\equiv c\;(\mathrm{mod}\ q)}}\frac1a
 \ll 1+\frac1q\log(2X)
 \ll\log(2X).
\tag{3.10}
\]

The phase \(0\) is the exceptional \(q=1\) fibre. It consists exactly
of odd denominators \(b=g\mid N\), with all supported primitive
numerators. Its mass for each \(g\) is also \(O(\log(2X))\). If

\[
 L_\vartheta=\sum_{i:\theta_i=\vartheta}|u_i|,
\]

then, uniformly including \(q=1\),

\[
 \max_\vartheta L_\vartheta
 \ll\tau(N)\log(2X)
 \ll_\varepsilon X^\varepsilon.
\tag{3.11}
\]

There is no overlap: the reduced phase fixes \(q\), and a denominator
fixes \(g=(N,b)\). Furthermore,

\[
 \sum_\vartheta L_\vartheta
 =\sum_{i\in\mathscr I}|u_i|
 \ll y\log(2X).
\tag{3.12}
\]

It follows that the absolute mass of all ordered collision pairs is

\[
 \sum_\vartheta L_\vartheta^2
 \leq
 \left(\max_\vartheta L_\vartheta\right)
 \sum_\vartheta L_\vartheta
 \ll_\varepsilon yX^\varepsilon.
\tag{3.13}
\]

Deleting from this owner the already-owned equal-denominator pairs
proves the second estimate in (2.6). The three cases in (2.2)--(2.4)
partition every ordered pair in (3.4), which proves (2.5) exactly.

## 4. First doubtful or unproved step

The first unproved step is any target-scale cancellation estimate for
\(\mathcal S_{\mathrm{nr}}^\times\). The following prospective routes
do not supply one.

**Character pairing.** Pairing \(b\) with \(b+2\) flips
\(\chi_4(b)\), but it also changes the exact staircase
\(L_\chi(y/b)\), the primitive numerator set, both profile samples, and
the phase. Even for a common numerator the phase increment is

\[
 \frac{2aN}{b(b+2)},
\]

which can be near a half-integer and turn formal subtraction into
reinforcement. Pairing \(b\) with \(b+4\) preserves the character and
contains the near-resonant packet in Section 5. No uniform
coefficientwise character contraction follows.

**Determinant fibres and aspect-ratio loss.** Put
\(b=g_0r\), \(b'=g_0s\), with \((r,s)=1\). Then

\[
 \Delta=g_0\delta,\qquad \delta=as-a'r,
\]

and the solutions on one fibre have
\(a=a_0+rt\), \(a'=a'_0+st\). Its exponential phase is constant,
so there is no oscillation along the fibre. The identity

\[
 \frac1{aa'}=\frac{s/a'-r/a}{\delta}
\tag{4.1}
\]

does not permit the factors \(r,s\) to be discarded. For a finite
positive solution interval \(T\), let \(a_{\min},a'_{\min}\) be its
least occurring coordinates and \(A,A'\) its upper coordinates. The
safe bound is

\[
 \sum_{t\in T}\frac1{a_ta'_t}
 \ll\frac1{|\delta|}
 \left\{
 \frac r{a_{\min}}+\frac s{a'_{\min}}
 +\log\!\left(2+\frac A{a_{\min}}\right)
 +\log\!\left(2+\frac {A'}{a'_{\min}}\right)
 \right\}.
\tag{4.2}
\]

Indeed, take absolute values in (4.1) and sum the two arithmetic
progressions. Their integral parts cancel the step sizes, but their
first terms do not. For any odd \(S>1\), take

\[
 r=1,\qquad s=S,\qquad a=a'=1,\qquad\delta=S-1.
\]

Choose odd \(g_0\asymp R^{3/2}\), odd
\(S\asymp R^{1/2}\), with \(g_0S\leq y\). Both fractions lie in the
literal small-arc chart. The reciprocal kernel has the one-point
contribution \(1/(aa')=1\), whereas
\(\log(2X)/|\delta|\to0\). Thus a uniform
\(O(\log X/|\delta|)\) estimate without the aspect/end-point terms is
false. This is an algebraic reciprocal-kernel control, not a lower bound
for the physical Farey fibre. Grouping only by \(\Delta\) also fails
because the phase retains \(bb'\). The reduction in Sections 2--3 does
not use a determinant-fibre estimate.

**Reciprocity and finite Fourier completion.** Reciprocity requires
unit and gcd splits; Möbius inversion then owns primitive and divisor
corrections. It is an invertible phase rewrite and leaves exact and near
collisions present. Periodic Fourier expansion gives the exact
Ramanujan-sum formula

\[
 \widehat J_{R,y}(k)=\int_0^1J_{R,y}(t)e(-kt)\,dt,\qquad
 A_y(m)=\sum_{\substack{d\leq y\\d\mid m}}\chi_4(d),
\]

\[
 \sum_{a\bmod b}^{*}J_{R,y}(a/b)e(Na/b)
 =\sum_{k\in\mathbb Z}\widehat J_{R,y}(k)c_b(N+k).
\tag{4.3}
\]

Additive completion and the lift sum give

\[
 A_y(m)-c_y
 =\sum_{\substack{2\leq b\leq y\\b\ \mathrm{odd}}}
 \lambda_bc_b(m),
\tag{4.4}
\]

where \(c_y=\sum_{d\leq y}\chi_4(d)/d\). Since
\(\sum_k\widehat J(k)=J(0)=0\), (4.3)--(4.4) return exactly

\[
 \mathcal F_N
 =\sum_k\widehat J_{R,y}(k)A_y(N+k).
\tag{4.5}
\]

This is the earlier completion/flat-cone representation, not a
contraction. Taking norms before reassembling (4.5) loses the lift and
cross-frequency directions. Using the desired short-interval circle
estimate to bound (4.5) is circular.

**Exact \(d\)-Poisson formula versus the stationary principal family.**
For fixed \(h\), set

\[
 a_h(x)=\frac1hV_{\mathrm{low}}(4R^2h^2/x^2).
\]

Using
\(\chi_4(d)=(e(d/4)-e(-d/4))/(2i)\), Poisson summation of the
literal hard interval, with symmetric summation in the dual integer,
gives the complete formula

\[
 \begin{split}
 \sum_{d\leq y}\chi_4(d)a_h(d)e(Nh/d)
 ={}&\frac12\chi_4(y)a_h(y)e(Nh/y)\\
 &+\frac1{2i}\sum_{\sigma=\pm1}\sigma
 \lim_{K\to\infty}\sum_{|k|\leq K}
 \int_0^y a_h(x)
 e\!\left(\frac{Nh}{x}+(\sigma/4-k)x\right)\,dx.
 \end{split}
\tag{4.6}
\]

The explicit half-endpoint term repairs the Fourier value at the jump;
omitting it is not an exact identity. Its absolute \(h\)-sum is
\(O(\log(2X))\), and the \(h\)-sum in (4.6) is finite on the literal
profile support. Formula (4.6), not its stationary leading term, is the
complete Poisson representation.

For an interior stationary mode put \(r=\sigma-4k>0\). Then \(r\) is
odd, \(r\equiv\sigma\pmod4\), and
\(\sigma=\chi_4(r)\). Its phase

\[
 \phi_{h,r}(x)=\frac{Nh}{x}+\frac{rx}{4}
\]

has

\[
 x_*=2\sqrt{Nh/r},\qquad
 \phi(x_*)=\sqrt{Nhr},\qquad
 \phi''(x_*)=\frac{r^{3/2}}{4(Nh)^{1/2}}.
\tag{4.7}
\]

Combining the branch factor \(\chi_4(r)/(2i)\), Gaussian factor
\(e(1/8)\), reciprocal square root
\(2(Nh)^{1/4}r^{-3/4}\), and \(1/h\), the correctly normalized
interior principal family is

\[
 e(-1/8)N^{1/4}
 \sum_{h\geq1}
 \sum_{\substack{r\geq1,\ r\ \mathrm{odd}\\
                  x_*=2\sqrt{Nh/r}\ \mathrm{interior}}}
 \chi_4(r)(hr)^{-3/4}
 V_{\mathrm{low}}(R^2hr/N)e(\sqrt{Nhr}).
\tag{4.8}
\]

Here

\[
 e(-1/8)=-i\,e(1/8),
\]

so this constant is the same as the convention which leaves the factor
\(-i\) outside the Gaussian phase. Formula (4.8) fixes the constant,
both congruence branches, and the profile argument, but it is only the
interior principal family. The hard endpoint imposes \(x_*\leq y\),
equivalently \(r\geq4Nh/y^2\). A stationary point crossing that
endpoint must carry a bounded incomplete-Fresnel transition
\(\omega_y(h,r)\), not a sharp unproved replacement. The explicit
endpoint in (4.6), every \(r\leq0\) nonstationary mode,
profile-boundary crossings, stationary entry and exit, and stationary
remainders retain separate ownership. No audited uniform error ledger
identifies the finite scalar with (4.8).

On the possible stationary support,

\[
 r\gg h,\qquad hr\ll N/R^2\asymp y.
\]

Consequently its absolute capacity is

\[
 N^{1/4}\sum_{h\ll R}h^{-3/4}
 \sum_{h\ll r\ll y/h}r^{-3/4}
 \ll X^{3/8}\log(2X),
\tag{4.9}
\]

which loses \(X^{1/8}\) against the scalar target. A second stationary
transform Legendre-dualizes \(\sqrt{Nhr}\) back to \(Nh/d\), with the
reciprocal Jacobian and the original radial profile. Direct
B-processing in \(b\) likewise sends \(Na/b\) to a phase
\(2\sqrt{Nak}\), with \(k\asymp a\) near \(b\asymp y\), and a second
process returns. Taking moduli between the two processes loses exactly
the directions needed for cancellation.

Any transform ledger must additionally preserve the two odd-lattice
branches, the \(d=y\) endpoint, the exact staircase
\(L_\chi(y/b)\), primitive-numerator Möbius corrections, both ends of
the literal \(J_{R,y}\) support, the zero class, the floors \(N,y\),
and both conjugate scalar signs. None is an optional error term.

## 5. Required controls and outcomes

| Control | Exact outcome | Consequence |
|---|---|---|
| Flat cone, lift coefficient, and \(b=1\) | Equations (3.1)--(3.3) retain every odd lift; \(J(0)\) exactly kills the zero class. | Passed, with no missing correction owner. |
| Equality diagonal | Equation (3.5) is \(O(y)\). | Target-square safe. |
| Entire \(b=b'\) sector | It is the row square (2.2), bounded by \(O(y\log^2(2X))\). | Target-square safe with actual coefficients. |
| Exact collision fibres | Equations (3.7)--(3.13), including \(q=1\), coprimality, literal support, and uniqueness, give maximum fibre \(\ell^1\)-mass \(O_\varepsilon(X^\varepsilon)\). | The complete cross-row collision owner is \(O_\varepsilon(yX^\varepsilon)\). This is only an upper control. |
| Divisors of \(N\) | They are exactly the \(q=1\) phase-zero fibre and have divisor-log mass. | They do not force a lower bound. |
| Determinant fibre | The correct estimate is (4.2), with unavoidable aspect/end-point terms. | No \(1/|\delta|\) contraction follows from the displayed partial fraction alone. |
| Character pairing | Exact staircase, primitive, profile, and phase data do not pair uniformly. | No signed saving is certified. |
| Finite Fourier/reciprocity | After all corrections they return (4.5). | Canonical self-return; a separated norm loses direction. |
| \(d\)-Poisson/stationary phase | Equation (4.6) is complete; (4.8) is only the normalized interior principal family and has capacity (4.9). | No target bound; endpoint, nonstationary, crossing, and remainder owners remain. |

Two further adversarial controls locate residual capacity without
claiming a physical lower bound.

**Literal fourth-power near resonance.** Let \(X=N=M^4\) with \(M\)
odd, so \(R=M\) and \(y=M^2\). For a sufficiently small fixed \(c>0\)
and \(1\leq u\leq cM\), take

\[
 a=1,\qquad b_u=y-4u.
\]

For all sufficiently large \(M\), these are supported primitive
fractions, \(y/b_u<2\), and

\[
 L_\chi(y/b_u)=1,\qquad
 \chi_4(b_u)=\chi_4(y)=1,\qquad
 V_{\mathrm{low}}(4R^2/b_u^2)=1.
\]

Hence the actual coefficient is exactly

\[
 \lambda_{b_u}J_{R,y}(1/b_u)=1,
\]

while

\[
 \frac N{b_u}
 =y+4u+\frac{16u^2}{y-4u}.
\tag{5.1}
\]

Choosing \(c\) small puts all fractional parts in one fixed short
sector. They are strictly increasing and therefore distinct. The packet
contains \(\asymp R\) actual terms, and its internal unequal-pair
subtotal lies wholly in \(\mathcal S_{\mathrm{nr}}^\times\) at scale
\(\asymp R^2\). This proves only that the survivor has literal
target-scale near-resonant capacity. Terms outside the packet may cancel
it, so it is not a lower bound for \(\mathcal F_N\).

**Squarefree channel in the principal family.** Write uniquely

\[
 N=Ds^2,\qquad D=\operatorname{sf}(N)\ \mathrm{squarefree}.
\]

The stationary phase in (4.8) is exactly one only when \(Nhr\) is a
square, equivalently

\[
 hr=Dt^2.
\tag{5.2}
\]

Thus there is only the unique squarefree channel \(D\). If the hard
endpoint is uniformized correctly, its incomplete-Fresnel multiplier
satisfies \(|\omega_y(h,r)|\ll1\). For fixed \(t\), the number of
factorizations in (5.2), even before requiring \(r\) odd and imposing
the cone, is at most \(\tau(Dt^2)\). Since the literal profile forces
\(Dt^2\ll N/R^2\asymp y\), the absolute principal mass of this channel
is at most

\[
 N^{1/4}D^{-3/4}
 \sum_{t\ll R/\sqrt D}t^{-3/2}\tau(Dt^2)
 \ll_\varepsilon RD^{-3/4}X^\varepsilon.
\tag{5.3}
\]

The literal bounded transition and divisor multiplicities therefore do
not break this upper control. An unbounded endpoint factor would signal
a nonuniform, invalid stationary formula. Equation (5.3) neither gives
a lower bound nor controls the nonstationary, endpoint, crossing, and
remainder owners outside the principal family.

Finally, completing (4.5) to a radial \(r_2\)-sum and then using a
target-size circle remainder assumes the estimate under construction.
Keeping the complementary divisor range instead reconstructs the
original flat cone. That route is circular or a self-return, depending
on where the modulus is taken.

## 6. Dependencies and exact artifacts used

This audit is wholly analytic and uses exactly the following supplied
artifacts:

- protocol.md;
- state/proof_obligations.yml, restricted in use to the active target
  and its direct dependencies;
- state/active_campaign.yml;
- strategy/conductor_0823_full_proof_strategy.md;
- rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/synthesis.md;
- rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/candidates/conductor_profile_flattening_and_integer_phase.md;
- rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/synthesis.md;
- rounds/codex-managed/full-proof-frontier-inequality-selection-gate/candidates/conductor_lower_discrepancy_farey_energy_connector.md;
- rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reports/lower_gar_wavelet_feasibility.md;
- rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/blind_statement.md;
- rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/briefs/farey_scalar_self_return_hostile_audit.md.

No numerical experiment, web source, separated auxiliary square
function, or unlisted theorem is used.

## 7. Recommended state effect

Promote only the exact owner decomposition (2.5), the full-row estimate
(3.6), and the cross-row collision-fibre estimate (3.13) as a strict
candidate reduction. Retain the scalar target as unresolved, with
\(\mathcal S_{\mathrm{nr}}^\times\) as the sole signed survivor. Reject
any promotion of the clean square-root stationary family as a full
identity, any determinant-fibre estimate that omits the aspect/end-point
terms in (4.2), and any use of (5.1) or (5.3) as a physical lower bound.
This report proves neither the lower-GAR target nor any blockwise parent,
M2 estimate, or final circle theorem. No graph or shared-state file was
edited.
