# Round 138 hostile post-unmask audit: owners, capacity, and promotion scope

## 1. Result

The current clean conductor candidate is mathematically owner-complete
for exactly one advance:

\[
 |\mathcal F_N|^2
 =\mathcal R_{y^{-2}}+O_\varepsilon(yX^\varepsilon),
\tag{1.1}
\]

where \(\mathcal R_{y^{-2}}\) is the ordered, conjugation-closed sum over
different denominators for which both the ordinary carrier
\(\theta=Na/b\) and the character-adjusted physical carrier
\(\phi=Na/b+(b-1)/4\) are separated from their partners by more than
\(y^{-2}\). The deleted owners are exactly the complete
same-denominator row block and the cross-row union of the two microscopic
collision collars. Their total cost is
\(O_\varepsilon(yX^\varepsilon)\) with the literal coefficients.

No estimate of \(\mathcal R_{y^{-2}}\) is proved. Its coefficient-blind
absolute capacity remains \(y^{2+o(1)}\), against target
\(y^{1+o(1)}\). Determinant coordinates, character pairing, Poisson
summation, the squarefree-radical channel, and Legendre involution are
only controls on the open survivor. They are not additional deletions or
target estimates.

After the integerized-cone, parity, determinant-aspect, and stationary
scope repairs now present in the conductor candidate, no promoted seam
is missing an owner. The verdict is GREEN, with promotion restricted to
(1.1) and its elementary inputs.

## 2. Exact scalar, lift, small arc, and complete row owner

**Integerized cone and small arc.** The scalar in this round is
termwise equal to the integerized cone
\(\mathcal B_{\mathrm{flat}}^{(N)}(X)\), whose phase is \(e(hN/d)\).
It is not termwise equal to the original \(X\)-phase cone. The accepted
Round-121 seam separately gives

\[
 \mathcal B_{\mathrm{flat}}^+(X)
 =\mathcal B_{\mathrm{flat}}^{(N)}(X)+O(R).
\tag{2.1}
\]

The certified profile has a genuinely small positive arc. In the
Round-121 normalization,
\(V_{\mathrm{low}}(s)=0\) for \(s\geq2s_0\), with
\(s_0\leq1/100\). Hence every nonzero term satisfies

\[
 \frac hd
 <\frac{\sqrt{2s_0}}{2R}<1
\tag{2.2}
\]

for every \(X\geq2\), not merely asymptotically. Thus
\(1\leq h<d\leq y\), \(yh/d\geq1\), and

\[
 \frac1hV_{\mathrm{low}}(4R^2h^2/d^2)
 =\frac1dJ_{R,y}(h/d).
\tag{2.3}
\]

This explicit certificate closes the small-\(X\) caveat raised in the
blind report; an unspecified inequality \(h/d<C/R\) alone would not.

**Lift and centre.** Reduce \(h/d=a/b\) uniquely, with
\(h=ag\), \(d=bg\), and \((a,b)=1\). Only odd \(b,g\) survive, and
all lifts aggregate before any norm:

\[
 \sum_{g\leq y/b}\frac{\chi_4(bg)}{bg}
 =\frac{\chi_4(b)}b
  \sum_{g\leq y/b}\frac{\chi_4(g)}g
 =\lambda_b.
\tag{2.4}
\]

At every rational sample \(ya/b\geq1\), so \(\eta(ya/b)=1\). Therefore

\[
 \lambda_bJ_{R,y}(a/b)
 =\chi_4(b)c_{a,b},\qquad
 c_{a,b}
 =\frac{L_\chi(y/b)}a
  V_{\mathrm{low}}(4R^2a^2/b^2).
\tag{2.5}
\]

No factor of \(a,b,d\), or \(g\) is missing. The only \(b=1\)
completion class is the zero residue, which \(J_{R,y}(0)=0\) kills
exactly. The opposite scalar sign is the complex conjugate.

**Full row.** For odd \(b\),
\(\chi_4(b)=e((b-1)/4)\). With

\[
 \phi_{a,b}=\frac{Na}{b}+\frac{b-1}{4}\pmod1,
\]

one has

\[
 \mathcal F_N=\sum_{a,b}c_{a,b}e(\phi_{a,b}),\qquad
 |c_{a,b}|\ll\frac1a,\qquad a\ll\frac bR.
\tag{2.6}
\]

Consequently

\[
 \sum_{a,b}|c_{a,b}|\ll y\log(2X),\qquad
 \sum_{a,b}|c_{a,b}|^2\ll y.
\tag{2.7}
\]

Writing \(F_b=\sum_a c_{a,b}e(\phi_{a,b})\), the entire
same-denominator owner is the nonnegative row square

\[
 \sum_b|F_b|^2
 \leq\sum_{b\leq y}
 \left(\sum_{a\ll b/R}\frac1a\right)^2
 \ll y\log^2(2X).
\tag{2.8}
\]

It contains the \(O(y)\) equality diagonal and every
same-denominator unequal-numerator pair. The unequal-numerator subtotal
need not itself be positive; the candidate correctly promotes the whole
row square instead.

## 3. Ordinary and adjusted fibres, packing, and exact residual

Let

\[
 \theta_{a,b}=\frac{Na}{b}\pmod1,\qquad
 g=(N,b),\qquad q=b/g.
\]

Writing \(N=gn\), one has \((n,q)=1\) and
\(\theta_{a,b}=na/q\). Conversely, a fixed reduced phase \(u/q\)
has only

\[
 b=qg,\qquad g\mid N,\qquad q,g\ \mathrm{odd},\qquad
 (N/g,q)=1,
\tag{3.1}
\]

and one numerator class

\[
 a\equiv u(N/g)^{-1}\pmod q,
\tag{3.2}
\]

subject to the literal support and \((a,qg)=1\). The parity conditions
in (3.1) are necessary for the converse and are now explicit in the
candidate. For each \(g\),

\[
 \sum_{\substack{a\ll qg/R\\a\equiv a_0\;(\mathrm{mod}\ q)}}\frac1a
 \ll1+\frac1q\log(2X).
\tag{3.3}
\]

The case \(q=1\) is exactly the phase-zero fibre of odd divisor
denominators \(b\mid N\), with every supported primitive numerator.
There is no overlap: the reduced phase fixes \(q\), and a denominator
fixes \(g=(N,b)\). Thus

\[
 \max_zM_\theta(z)
 \ll\tau(N)\log(2X),\qquad
 \sum_zM_\theta(z)\ll y\log(2X).
\tag{3.4}
\]

A fixed physical fibre \(\phi=z\) is the union of at most two
restricted ordinary fibres: \(\theta=z\) for
\(b\equiv1\pmod4\), and \(\theta=z-1/2\) for
\(b\equiv3\pmod4\). Hence (3.4), up to an absolute factor, also holds
for \(M_\phi\).

Distinct reduced \(\theta\)-values have denominator at most \(y\), so
their circular spacing is at least \(y^{-2}\). Distinct
\(\phi\)-values have denominator at most \(2y\), so their spacing is at
least \((4y^2)^{-1}\). An arc of radius \(\delta\) contains
\(O(1+\delta y^2)\) values of either carrier. Therefore

\[
 \begin{aligned}
 \sum_{\|z-z'\|\leq\delta}M(z)M(z')
 &\leq
 \left(\sum_zM(z)\right)\max_zM(z)\,
 O(1+\delta y^2)\\
 &\ll y\tau(N)\log^2(2X)(1+\delta y^2).
 \end{aligned}
\tag{3.5}
\]

At \(\delta=y^{-2}\), this is
\(O_\varepsilon(yX^\varepsilon)\) for both carriers. This is an upper
control only; it is not a resonant lower bound.

The exact scalar square now has the disjoint owner partition:

- all \(b=b'\) pairs, owned by (2.8);
- among \(b\neq b'\), the union where
  \(\|\theta-\theta'\|\leq y^{-2}\) or
  \(\|\phi-\phi'\|\leq y^{-2}\), owned absolutely by (3.5);
- the complement, exactly \(\mathcal R_{y^{-2}}\).

Every condition is symmetric under reversing the ordered pair, so the
residual is real. Different reduced denominators imply nonzero Farey
determinant. The union bound prices collar overlaps without omitting or
double-charging an owner. Equations (2.8) and (3.5) prove (1.1).
Conversely, the target for \(\mathcal F_N\) and the target for the
residual imply one another after renaming \(\varepsilon\).

This partition is strictly stronger than the exact-collision-only
survivors in the blind and hostile primary reports. It does not reduce
the residual's coefficient-blind exponent: taking absolute values still
allows \(y^{2+o(1)}\).

## 4. Determinant aspect correction and fourth-power controls

**Determinant fibres.** For \(b=Gr\), \(b'=Gs\), with
\((r,s)=1\), all quantities \(G,r,s\) are odd and

\[
 \Delta=G\delta_0,\qquad
 \delta_0=as-a'r,\qquad
 \frac{N\Delta}{bb'}=\frac{N\delta_0}{Grs}.
\tag{4.1}
\]

Every solution is

\[
 a=a_0+r\ell,\qquad a'=a'_0+s\ell.
\tag{4.2}
\]

Both the determinant phase and
\(\chi_4(Gr)\chi_4(Gs)=\chi_4(rs)\) are constant in \(\ell\). The
identity

\[
 \frac1{aa'}=\frac1{\delta_0}
 \left(\frac{s}{a'}-\frac r a\right)
\tag{4.3}
\]

has no oscillatory partner. If \(a_{\min},a'_{\min}\) and \(A,A'\)
are the positive fibre endpoints, the safe estimate is

\[
 \sum_\ell\frac1{a_\ell a'_\ell}
 \ll\frac1{|\delta_0|}
 \left\{
 \frac r{a_{\min}}+\frac s{a'_{\min}}
 +\log\!\left(2+\frac A{a_{\min}}\right)
 +\log\!\left(2+\frac {A'}{a'_{\min}}\right)
 \right\}.
\tag{4.4}
\]

The aspect terms cannot be dropped. For odd \(S>1\), take
\(r=1\), \(s=S\), \(a=a'=1\), and \(\delta_0=S-1\). Choose odd
\(G\asymp R^{3/2}\), odd \(S\asymp R^{1/2}\), with \(GS\leq y\).
Both fractions lie in the literal small arc. The reciprocal kernel has
a one-point contribution \(1\), while
\(\log(2X)/|\delta_0|\to0\). This is an algebraic capacity
counterexample, not a lower bound for the physical Farey fibre.

The parity-invalid \(r=1,s=100\) working-draft line was superseded by
this variable odd-\(S\) family and has now been mechanically repaired in
the hostile primary report. The discovery report and current candidate
also use the corrected odd family. No promoted reduction depends on a
determinant-fibre estimate. Taking fibre moduli and then restoring all
denominator pairs returns \(y^{2+o(1)}\).

**Direct fourth-power packet.** Let \(X=N=M^4\), with \(M\) odd, so
\(R=M\) and \(y=M^2\). For

\[
 a=1,\qquad b_u=y-4u,\qquad1\leq u\leq cM,
\tag{4.5}
\]

one has \(b_u\equiv1\pmod4\), \(L_\chi(y/b_u)=1\), and, under the
accepted normalization \(V_{\mathrm{low}}=1\) near zero,

\[
 c_{1,b_u}=1,\qquad
 \frac N{b_u}
 =y+4u+\frac{16u^2}{y-4u}.
\tag{4.6}
\]

For fixed small \(c\), these fractional parts lie in one short sector
and are strictly increasing. Their consecutive gaps are
\(\gg y^{-1}\), far larger than \(y^{-2}\). Hence the packet's
unequal internal pairs survive both collars and have target-square
subtotal \(\asymp R^2\). This is a selected subtotal of the residual,
not a lower bound for \(\mathcal F_N\); exterior terms may cancel it.
Without quoting the accepted plateau normalization, the equality
\(c_{1,b_u}=1\) must be replaced by the literal profile value.

The discovery report's \(R^{3/2}\) half-integer tube total is a
different control: it is obtained after exact lift unaggregation,
adjacent-character pairing, stationary tube partitioning, and then
summing tube moduli. It is physical capacity under a forbidden partial
modulus, not a signed scalar lower bound or another safe deletion.

## 5. Hard-endpoint Poisson formula, normalization, and self-return

For fixed \(h\), put

\[
 a_h(x)=\frac1hV_{\mathrm{low}}(4R^2h^2/x^2).
\]

Since
\(\chi_4(d)=(e(d/4)-e(-d/4))/(2i)\), symmetric Poisson summation of
the inclusive hard interval gives the complete formula

\[
 \begin{aligned}
 \sum_{d\leq y}\chi_4(d)a_h(d)e(Nh/d)
 ={}&\frac12\chi_4(y)a_h(y)e(Nh/y)\\
 &+\frac1{2i}\sum_{\sigma=\pm1}\sigma
 \lim_{K\to\infty}\sum_{|k|\leq K}
 \int_0^y a_h(x)
 e\!\left(\frac{Nh}{x}+(\sigma/4-k)x\right)\,dx.
 \end{aligned}
\tag{5.1}
\]

The explicit half-endpoint term is required because Fourier inversion
assigns half weight at the jump. Its full \(h\)-sum is
\(O(\log(2X))\). Formula (5.1), including every integral, is exact;
the clean stationary family below is not.

For an interior stationary mode set \(r=\sigma-4k>0\). Then \(r\) is
odd, \(r\equiv\sigma\pmod4\), and \(\sigma=\chi_4(r)\). The phase
has

\[
 x_*=2\sqrt{Nh/r},\qquad
 \Phi(x_*)=\sqrt{Nhr},\qquad
 \Phi''(x_*)=\frac{r^{3/2}}{4(Nh)^{1/2}}.
\tag{5.2}
\]

The branch coefficient \(\chi_4(r)/(2i)\), Gaussian factor
\(e(1/8)\), reciprocal curvature
\(2(Nh)^{1/4}r^{-3/4}\), and \(1/h\) combine to

\[
 e(-1/8)N^{1/4}\chi_4(r)(hr)^{-3/4}
 V_{\mathrm{low}}(R^2hr/N)e(\sqrt{Nhr}),
\tag{5.3}
\]

where

\[
 e(-1/8)=-i\,e(1/8).
\tag{5.4}
\]

Thus both congruence branches, the profile argument, and the constant are
correct. A fixed smooth interior \(d/y\)-window has \(r\asymp h\) and
principal absolute capacity \(\asymp R^{3/2}\). Across all stationary
windows,

\[
 r\gg h,\qquad hr\ll N/R^2\asymp y,
\]

so the complete-principal absolute ledger is

\[
 N^{1/4}\sum_{h\ll R}h^{-3/4}
 \sum_{h\ll r\ll y/h}r^{-3/4}
 \ll R^{3/2}\log(2X).
\tag{5.5}
\]

This is a factor \(R^{1/2}\), up to logarithms, above the scalar target.

Write uniquely \(N=Ds^2\), where \(D=\operatorname{sf}(N)\). The
variable stationary phase is one exactly when

\[
 e(\sqrt{Nhr})=1
 \quad\Longleftrightarrow\quad
 hr=Dt^2.
\tag{5.6}
\]

There is only this one radical channel. With any correctly bounded
interior or incomplete-Fresnel transition weight, the profile and
divisor bounds give

\[
 N^{1/4}D^{-3/4}
 \sum_{t\ll R/\sqrt D}t^{-3/2}\tau(Dt^2)
 \ll_\varepsilon RD^{-3/4}X^\varepsilon.
\tag{5.7}
\]

This is a target-safe upper control inside the principal/transition
family. It is not a lower bound and controls neither near radicals nor
any nonprincipal owner. The common factor \(e(-1/8)\) is not part of the
variable phase-one test.

The owners outside (5.3) are the hard endpoint, its bounded
incomplete-Fresnel crossing, all nonstationary modes, lower-profile and
stationary entry/exit crossings, remainders, small heights, both
odd-lattice branches, the zero class, floors, simultaneous parameter
dependence, and the conjugate sign. If one starts in Farey coordinates,
the exact lift staircase and primitive-numerator reassembly also remain.

A second Legendre step sends \(2\sqrt{A\rho}-\rho x\) back to
\(A/x\), with \(A=Nh\). Periodic Fourier completion likewise returns
\(\sum_k\widehat J(k)A_y(N+k)\), the earlier flat discrepancy. Taking a
modulus between the two representations loses direction, while importing
the desired circle remainder is circular. These transforms are canonical
self-returns, not contractions.

## 6. Overclaim corrections, first open step, and scope

The post-unmask comparison requires the following exact corrections and
scope restrictions.

- The termwise Farey identity is with
  \(\mathcal B_{\mathrm{flat}}^{(N)}\); the original \(X\)-phase cone
  differs by the already priced \(O(R)\) seam.
- The certified small arc, not an unspecified asymptotic support
  constant, owns \(h<d\) uniformly.
- The phase-fibre converse retains \(q,g\) odd, including the
  \(q=1\) divisor fibre.
- The parity-invalid \(r=1,s=100\) working-draft line is superseded by
  the odd variable-\(S\) family in Section 4 and has now been
  mechanically repaired in the hostile primary report. The discovery
  report and candidate use the same corrected family.
- The full same-denominator owner is a row square; its
  unequal-numerator subtotal is not separately declared positive.
- The canonical residual deletes the union of both \(y^{-2}\) collars.
  No wider collar is promoted.
- The fourth-power packet is target-scale only. Its exact unit
  coefficients use the accepted plateau of \(V_{\mathrm{low}}\), and
  its subtotal is not a physical lower bound.
- Formula (5.1) is the full hard-endpoint identity; (5.3) is only an
  interior principal family. Every correction owner listed above remains.
- The radical estimate (5.7) is one-channel, principal-family, and
  upper-only. It proves nothing for near radicals or the full scalar.
- Determinant, Poisson, pairing, and Legendre capacity statements do not
  enter the proof of (1.1).

The first unproved statement is exactly

\[
 |\mathcal R_{y^{-2}}|
 \ll_\varepsilon yX^\varepsilon.
\tag{6.1}
\]

It requires the missing factor \(y\) of joint cancellation in the
scalar square. No positive auxiliary \(k\)-energy, arbitrary coefficient
array, rowwise modulus on the residual, centre average, or transform
involution supplies it.

This audit reread the current versions of:

- reports/literal_signed_farey_scalar_attack.md;
- reports/blind_reduced_fraction_scalar_feasibility.md;
- reports/farey_scalar_self_return_hostile_audit.md;
- candidates/conductor_round138_scalar_rows_and_resonance_fibres.md;
- reviews/discovery_post_unmask_transform_and_scope_audit.md;
- reviews/blind_post_unmask_scalar_fibre_audit.md.

The two sibling reviews also end green, but this verdict follows from
the owner calculation above, not from a vote. No numerical experiment,
symbolic computation, web result, arbitrary array, or centre average was
used. The promoted result concerns only the frozen lower-radial signed
scalar through the accepted connectors. It proves no direct blockwise
M1 estimate, M2 parent, endpoint-uniformity claim, M9 closure, quarter
theorem, or global exponent.

## 7. Recommended state effect and verdict

Promote only:

- the exact integerized flat-cone/Farey dictionary, including the lift
  coefficient and \(b=1\) centre;
- the complete same-denominator row estimate (2.8);
- the ordinary and physical fibre classification and the
  \(y^{-2}\) packing estimate (3.5);
- the exact strict residual identity (1.1).

Retain the residual estimate (6.1) as open. Retain determinant fibres,
the direct fourth-power packet, paired half-integer tubes, the
hard-endpoint Poisson formula, its normalized stationary principal
family, the radical bound, periodic completion, and Legendre involution
only as scoped controls. They prove no target bound.

Keep the lower-radial signed estimate, lower GAR, both direct blockwise
M1 parents, all M2 parents, endpoint uniformity, M9, the quarter theorem,
and both global exponents open. Do not edit shared state except through
the conductor's mechanically validated State Patch.

GREEN
