# Round 141 conductor adjudication: the microscopic cells close, the fixed-centre cone does not

Campaign: m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate

Starting graph SHA-256:
072e08848e9d368d65b89fbf03c36423a8e3662e7ae61c48052d4c352d1d71b0

## 1. Result and decision

Close Round 141 under
\(\mathsf{incomplete\_fibre\_dispersion\_no\_go}\).  Put

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,\qquad0\le q\le2y,
\tag{141.J1}
\]

and fix \(0<\rho<1/8\).  The Round-140 coefficient is

\[
 A_\rho(m)=
 \sum_{\substack{h\mid m,\ r=m/h\ \mathrm{odd}\\
 r\ge r_h+2}}\chi_4(r),
\quad
 r_h=\min\left\{r\ge {4Nh\over D_h^2}:
 r\ \mathrm{positive\ odd}\right\},
\quad
 D_h=y-\left\lfloor{\rho y\over\sqrt h}\right\rfloor-1.
\tag{141.J2}
\]

Define the constant-cone coefficient

\[
 C(m)=\sum_{\substack{hr=m,\ r\ \mathrm{odd}\\r>4h}}\chi_4(r).
\tag{141.J3}
\]

Let \(\mathcal I_M=[M,2M)\cap[1,M_*]\) be the disjoint powers-of-two
blocks covering the profile support, where
\(M_*=C_VN/R^2\asymp R^2\), and put

\[
 k_m=\left\lfloor\sqrt{Nm}+{1\over2}\right\rfloor,
 \qquad j_m=k_m^2-Nm.
\tag{141.J4}
\]

The accepted reduction is

\[
 \boxed{
 \mathfrak T_N=
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>\sqrt M}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
O_{\varepsilon,\rho,V}(X^\varepsilon).}
\tag{141.J5}
\]

It removes every exact radical, every nonzero microscopic
nearest-square cell \(0<|j_m|\le\sqrt M\), and every floor-dependent
entry correction.  The survivor in (141.J5) retains the full
coefficient-blind \(R^{1/2+o(1)}\) excess before the Round-140 outer
factor and is not bounded here.

The decision is not a vote.  The statement-only lane independently
proved the floor-to-cone reduction and a quarter-frequency main term;
the discovery lane proved the microscopic congruence bound and exact
divisor involution; and the source lane proved the smooth ratio-Mellin
factorization and audited the available theorems.  Three post-unmask
reviews then checked mutually different seams.  The source paragraph
and the variation range were repaired exactly as those reviews
required, after which all assigned seams were green.

## 2. Exact cone and microscopic-cell proof

Write

\[
 \delta_h=\left\lfloor{\rho y\over\sqrt h}\right\rfloor+1,
 \qquad D_h=y-\delta_h.
\tag{141.J6}
\]

For odd \(r\), least-odd minimality gives

\[
 r\ge r_h+2
 \Longleftrightarrow
 r-2\ge {4Nh\over D_h^2}
 \Longleftrightarrow
 (r-2)D_h^2\ge4Nh.
\tag{141.J7}
\]

Since \(N\ge y^2>D_h^2\), an exact far pair satisfies \(r>4h\).
The cone-minus-exact correction is therefore

\[
 E_N(m)=
 \sum_{\substack{hr=m,\ r\ \mathrm{odd}\\4h<r\le r_h}}\chi_4(r),
 \qquad A_\rho(m)=C(m)-E_N(m).
\tag{141.J8}
\]

The floors and the full real-centre range remain in

\[
 {4Nh\over D_h^2}-4h
 =4h{q+2y\delta_h-\delta_h^2\over D_h^2}
 \ll_\rho 1+\sqrt h+{h\over y}.
\tag{141.J9}
\]

On the effective support, \(r>4h\) and \(hr\ll y\) imply
\(h\ll R\).  Hence

\[
\begin{aligned}
 \sum_m m^{-3/4}|E_N(m)|
 |V_{\rm low}(R^2m/N)|
 &\ll_{\rho,V}
 \sum_{h\ll R}h^{-3/2}
 \left(1+\sqrt h+{h\over y}\right)\\
 &\ll_{\rho,V}\log(2X).
\end{aligned}
\tag{141.J10}
\]

This is an exact target-safe floor-to-cone replacement.

There are no ties in (141.J4), since
\(\sqrt{Nm}=k+1/2\) would make \(4Nm\) an odd square.  The real cell
with nearest integer \(k\) is

\[
 \mathcal C_k=
 \left[{(k-1/2)^2\over N},{(k+1/2)^2\over N}\right),
 \qquad |\mathcal C_k|={2k\over N}.
\tag{141.J11}
\]

On \(m\le M_*\), \(k\ll_VN/R\), so
\(|\mathcal C_k|\ll_VR^{-1}<1\).  Each such cell contains at most one
integer \(m\); the phase relabeling creates no within-cell sum.
Moreover

\[
 e(\sqrt{Nm})=
 e\!\left(-{j_m\over k_m+\sqrt{Nm}}\right).
\tag{141.J12}
\]

For nonzero \(j\), let
\(\rho_N(j)=\#\{k\bmod N:k^2\equiv j\pmod N\}\).  Prime-power lifting
and the Chinese remainder theorem give

\[
 \rho_N(j)\le4^{\omega(N)+1}\sqrt{(N,j)}
 \ll_\varepsilon N^\varepsilon|j|^{1/2}.
\tag{141.J13}
\]

The effective range has \(k_m<N\).  For fixed \(j\), the identity
\(m=(k_m^2-j)/N\) injects the relevant \(m\)'s into the residue roots
counted by (141.J13).  Therefore

\[
 \#\{m\in\mathcal I_M:0<|j_m|\le\sqrt M\}
 \ll_\varepsilon
 N^\varepsilon\sum_{1\le j\le\sqrt M}j^{1/2}
 \ll_\varepsilon N^\varepsilon M^{3/4}.
\tag{141.J14}
\]

Multiplication by \(m^{-3/4}|A_\rho(m)|\), with
\(|A_\rho(m)|\le\tau(m)\), makes each block target-safe.  If \(j_m=0\),
write \(N=Du^2\), \(D\) squarefree.  Then \(m=Dt^2\), and

\[
 \sum_{j_m=0}m^{-3/4}|V_{\rm low}A_\rho(m)|
 \ll_\varepsilon
 D^{-3/4}X^\varepsilon\sum_{t\ge1}t^{-3/2}
 \ll_\varepsilon X^\varepsilon.
\tag{141.J15}
\]

Equations (141.J10), (141.J14), and (141.J15) prove (141.J5).  The
same root-count argument gives
\(M^{-3/4}J^{3/2}X^\varepsilon\) for \(|j|\le J\), so it reaches target
scale at \(J=\sqrt M\) and gives no wider target-safe conclusion.

## 3. Divisor pairing and the quarter-frequency obstruction

Write \(m=2^\nu n\) with \(n\) odd.  For \(dr=n\), define

\[
 F_\nu(d,r)=\mathbf1_{\{r\ge r_{2^\nu d}+2\}},
 \qquad
 A_\nu(n)=\sum_{dr=n}\chi_4(r)F_\nu(d,r).
\tag{141.J16}
\]

Equation (141.J7) implies
\(F_\nu(d,r)=1\Rightarrow r>4\,2^\nu d\), so

\[
 F_\nu(d,r)F_\nu(r,d)=0.
\tag{141.J17}
\]

Put

\[
 B_\nu(n)=\sum_{dr=n}\chi_4(r)
 \{1-F_\nu(d,r)-F_\nu(r,d)\},
 \qquad
 \sigma_{\chi_4}(n)=\sum_{r\mid n}\chi_4(r).
\tag{141.J18}
\]

Swapping \(d,r\) makes the second far sector
\(\chi_4(n)A_\nu(n)\).  Thus

\[
 \boxed{
 \sigma_{\chi_4}(n)
 =(1+\chi_4(n))A_\nu(n)+B_\nu(n),}
\tag{141.J19}
\]

and exactly

\[
 \boxed{
 A_\nu(n)=
 {1\over2}\sigma_{\chi_4}(n)-{1\over2}B_\nu(n)
 +\mathbf1_{\{\chi_4(n)=-1\}}A_\nu(n).}
\tag{141.J20}
\]

For \(\chi_4(n)=-1\), the complete coefficient and central band both
vanish under the involution, leaving a tautology.  For
\(\chi_4(n)=1\), the complete term is

\[
 \sigma_{\chi_4}(n)={r_2(2^\nu n)\over4},
\tag{141.J21}
\]

but the exact central band remains.  Complete radial mass, raw central
incidences, and raw negative-character far incidences all retain
top-scale \(R^{1/2+o(1)}\) weighted \(\ell^1\) capacity.  This is not a
lower bound for a grouped coefficient or the signed fixed-centre
scalar.

The coefficient also has an exact additive obstruction.  Unfolding the
cone gives

\[
 S_C(M):=\sum_{m\le M}C(m)e(m/4)
 =\sum_{4h^2<M}
 \sum_{\substack{4h<r\le M/h\\r\ \mathrm{odd}}}
 \chi_4(r)e(hr/4).
\tag{141.J22}
\]

Even \(h\)-rows total \(O(\sqrt M)\).  For odd \(h,r\),

\[
 e(hr/4)=i\chi_4(h)\chi_4(r),
\tag{141.J23}
\]

so an odd row has constant summand \(i\chi_4(h)\) and
\(M/(2h)-2h+O(1)\) terms.  Since

\[
 \sum_{\substack{h\le H\\h\ \mathrm{odd}}}{\chi_4(h)\over h}
 ={\pi\over4}+O(H^{-1}),
 \qquad
 \sum_{\substack{h\le H\\h\ \mathrm{odd}}}\chi_4(h)h=O(H),
\tag{141.J24}
\]

one gets

\[
 S_C(M)={i\pi\over8}M+O(M^{1/2}).
\tag{141.J25}
\]

For \(M\le c_0y\), the number of correction pairs in (141.J8) is
\(O_{\rho,c_0}(M^{3/4})\).  Consequently

\[
 \sum_{m\le M}A_\rho(m)e(m/4)
 ={i\pi\over8}M+O_{\rho,c_0}(M^{3/4}),
\tag{141.J26}
\]

and Abel summation gives

\[
 \sum_{m\le M}m^{-3/4}A_\rho(m)e(m/4)
 ={i\pi\over2}M^{1/4}
 +O_{\rho,c_0}(\log(2M)).
\tag{141.J27}
\]

For some \(M_0=M_0(\rho,c_0)\), bounded partial sums of \(e(m/4)\)
then imply

\[
 \sum_{m<M}|A_\rho(m+1)-A_\rho(m)|
 \gg_{\rho,c_0}M
 \qquad(M_0\le M\le c_0y).
\tag{141.J28}
\]

Choosing \(c_0\) inside the fixed \(V_{\rm low}=1\) plateau makes this
a literal supported coefficient obstruction.  It disproves uniform
additive cancellation and low variation, but nonlinear cell phases may
still rotate and cancel it; (141.J26) is not a lower bound for
(141.J5).

## 4. Smooth Mellin factorization and repaired source audit

On \(h\asymp H\), smoothing the cone across relative ratio width
\(H^{-1/2}\) changes \(O(\sqrt H)\) odd \(r\)'s per height and costs
\(O(1)\) per dyadic block.  Let

\[
 u=hr,\qquad v={r\over4h},
\tag{141.J29}
\]

and absorb the smooth ratio cutoff, dyadic weights, profile, radial
weight, and square-root phase into a compactly supported
\(\Psi(u,v)\).  Double Mellin inversion on an initial
absolute-convergence contour gives, after \(t\mapsto-t\), the exact
arithmetic factor

\[
 \boxed{4^{-t}\zeta(s+t)L(s-t,\chi_4).}
\tag{141.J30}
\]

This identity does not itself estimate the contour.  The sharp Perron
kernel needs height \(T\gg H\), because the nearest odd ratio has
\(|\log(r/(4h))|\asymp H^{-1}\).  Only the target-safe smoothing
licenses rapid ratio-Mellin decay beyond
\(|\Im t|\lesssim H^{1/2}X^\varepsilon\).

The independent source review corrected two initial attributions.
At \(H\asymp K\asymp R\):

- Robert--Sargos gives \(R^{1/2+\varepsilon}\) only in the
  smoothed/separated specialization; inserting the exact joint mask
  directly gives \(R^{3/4+\varepsilon}\).
- The genuine Sargos--Wu Theorem 9 admits the monomial
  \((\alpha,\beta)=(1/2,1/2)\) with separated coefficients and gives
  \(R^{2/5+\varepsilon}\).  The adjacent general-domain lemma permits
  a joint staircase domain but excludes
  \(\alpha+\beta-1=0\).
- The Tao--Trudgian--Yang pair
  \((89/1282,997/1282)\) applies rowwise and gives
  \[
  R^{2\kappa+\lambda-1/2+\varepsilon}
  =R^{267/641+\varepsilon}.
  \tag{141.J31}
  \]
- Popov's complete radial cosine combination, coupled with the
  separately repaired Li--Yang exponent, gives only
  \[
  R^{4\theta_*-1+\varepsilon}
  =R^{(50\sqrt{1717}-297)/6881+\varepsilon}
  \tag{141.J32}
  \]
  after removing the outer \(N^{1/4}\asymp R\).  It neither treats the
  incomplete coefficient nor bounds an individual complex branch.

Banerjee--Khurana has a complete generalized-divisor coefficient and
a strict \(0<\Re\nu<1/2\) hypothesis; Kaczorowski--Perelli fixes the
standard-twist parameter while the present centre grows with the
length; and the audited subconvex and moment results do not estimate
the required fixed-centre oscillatory linear functional with opposite
shifts.  On the balanced block, even an ideal uniform shifted mean
square, used through Mellin Plancherel and Cauchy--Schwarz, gives only
\(R^{1+\varepsilon}\).  No audited theorem reaches
\(R^\varepsilon\).

## 5. First open step and directionality

The first open estimate is exactly

\[
 \boxed{
 \sum_M\sum_{\substack{m\in\mathcal I_M\\
 |k_m^2-Nm|>\sqrt M}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 \ll_\varepsilon X^\varepsilon.}
\tag{141.J33}
\]

A sufficient dyadic partial-sum statement is

\[
 \sup_{M\le U\le2M}
 \left|
 \sum_{\substack{M\le m<U\\|k_m^2-Nm|>\sqrt M}}
 A_\rho(m)e(\sqrt{Nm})
 \right|
 \ll_\varepsilon M^{3/4}X^\varepsilon.
\tag{141.J34}
\]

Neither the congruence count, the exact divisor involution, the
quarter-frequency main term, nor an audited source theorem proves
(141.J34).  The phase cells are singletons; the elementary root count
uses all its target-safe power at \(|j|=\sqrt M\); the involution is
blind on \(\chi_4(n)=-1\) and otherwise returns an owner-sized complete
plus central split; and the coefficient has linear quarter-frequency
partial sums and variation.

For

\[
 \Phi_z(m)=\sqrt{Nm}-{mz\over4},
\tag{141.J35}
\]

the critical point and value are

\[
 m_z={4N\over z^2},\qquad \Phi_z(m_z)={N\over z}.
\tag{141.J36}
\]

Resolving divisor incidence before transforming returns the reciprocal
family; a second transform returns the square-root phase.  Completing
the fibre returns (141.J20)--(141.J21).  None is a noninvertible signed
gain.

Equation (141.J5) is an unsquared scalar equivalence.  Restoring the
Round-140 factor \(N^{1/4}\asymp R\), every discarded family costs
\(O(RX^\varepsilon)\), while (141.J33) is exactly the remaining target.
No collar--tail cross term, lift-dependent square identity, or positive
Round-138 residual is controlled.

## 6. Seam reviews, controls, dependencies, and scope

The post-unmask reviews are all final green:

1. discovery_post_unmask_cone_quarter_mode_audit.md independently
   rederived the least-odd dictionary, correction sign and price,
   constants \(i\pi/8\) and \(i\pi/2\), large-\(M\) variation range,
   plateau relevance, and non-lower-bound direction.
2. source_post_unmask_phase_pairing_audit.md independently rederived
   the tie convention, singleton cells, prime-power root count,
   \(k<N\) injection, all dyadic weights, exact radicals, \(2\)-adic
   pairing, central and negative-character controls, and raw-capacity
   wording.
3. blind_post_unmask_source_mellin_audit.md independently checked the
   Mellin signs and bandwidth, source hypotheses, every quoted
   \(R\)-power, and radial-cosine direction.  Its red findings were
   repaired before its final green verdict.

Every campaign control now has a determinate outcome.  Exact mask,
floors, parity, profiles, dyadic support, real centre, \(q=0\), and
\(q=2y\) are green.  Phase-cell definitions, endpoints, widths,
multiplicities, exact radicals, and microscopic weights are green.
Divisor pairing, complete-fibre comparison, fourth-power and
prime-power hostile controls, coefficient variation, source
hypotheses, canonical self-return, fixed-centre direction, and
downstream scope are green as proved reductions or obstructions.  The
nonresonant complement control is deliberately open and is the reason
for the terminal no-go label; it is not silently marked target-safe.

Exact dependencies are protocol.md, the active graph and campaign,
the Round-140 accepted candidate/adjudication/synthesis, the Round-137
hard-TOP synthesis, the three Round-141 reports, the conductor
candidate, and the three final-green post-unmask reviews.  Primary
source citations and theorem cards are retained in
reports/sqrt_divisor_twist_source_audit.md.  No numerical or symbolic
experiment, centre average, positive energy, arbitrary array, or
desired circle estimate is used.  The allocation is 100 percent
analytical/source verification.

The complete lower-radial signed estimate, lower GAR, both direct M1
parents, M9-M1, every M2 parent, M9-M2, endpoint uniformity, M9, the
conditional bridge, and the quarter theorem remain open.  The strongest
internally proved exponent remains \(1/3\).  The separately audited
external exponent remains

\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots.
\tag{141.J37}
\]

## 7. Recommended State Patch

Create one proved reduction recording (141.J5): the Round-140 exact far
scalar is target-equivalent to the floor-free cone scalar after removal
of exact and microscopic nearest-square cells, with all removed
families target-safe.

Create one proved obstruction recording (141.J11)--(141.J13),
(141.J19)--(141.J21), (141.J25)--(141.J32), and
(141.J35)--(141.J36): nearest-square cells are singleton; the
elementary root count stops at the microscopic width; pairing
self-returns or is blind; the exact coefficient has a full
quarter-frequency mode and linear variation; the smooth cone has an
exact shifted-\(L\) Mellin representation but every audited source
retains a positive power, a wrong coefficient/direction, or an
inapplicable hypothesis; and the canonical transform self-returns.

Update the Round-140 far-alias reduction and the global lower signed
owner with (141.J5), leaving (141.J33) as their next action.  Update the
Round-140 rank-one/product-fibre obstruction with the new exact
pairing, phase-cell, additive-mode, source, and transform controls.

Reject uniform additive cancellation, low variation, cell
multiplicity, wider near-radical extrapolation, target-safe central or
negative-character deletion, direct complete-fibre replacement,
unqualified source imports, sharp Perron truncation, capacity-to-lower-
bound inference, and downstream promotion.  Leave M9-M1, M9-M2,
endpoint uniformity, M9, the bridge, the quarter target, and both
recorded exponents unchanged.

The applied patch produces graph SHA-256
de02111a1831d30da33c9f4b2d4a549efa1942dcdc32b5d829e671f6ad5e0e76.
