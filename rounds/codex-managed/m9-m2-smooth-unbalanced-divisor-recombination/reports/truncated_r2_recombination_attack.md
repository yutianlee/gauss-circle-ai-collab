# Truncated \(r_2\) recombination attack

## 1. Result

**No-go with an exact survivor.**  For every literal smooth unbalanced
packet, the double Mellin transform and the two functional equations are
coefficient preserving and unitary on the critical line.  They do not
complete the packet to \(r_2/4\), shorten its capacity, or produce a new
residual corridor.  A direct audit of the same transform gives

\[
 \mathcal T_{L,K}
 =i e(-1/8)X^{-1/4}(LK)^{3/4}\mathscr R_{D,L}(X)
   +E_{L,K},                                           \tag{1.1}
\]

where \(K=XL/D^2\), \(F=XL/D\),
\(E_{L,K}\ll K F^{-1/2}\), and

\[
 \mathscr R_{D,L}(X)=
 \sum_{\substack{r\ge1\\r\ {\rm odd}}}\chi _4(r)
 W\!\left({X\over rD}\right)
 \sum_{k\ge1}{q_L(4Xk/r^2)\over k}e(Xk/r).          \tag{1.2}
\]

Consequently the inherited physical normalization is

\[
 \mathcal B^+_{L,W}=-{i\over2\pi}\mathscr R_{D,L}(X)+O_W(1). \tag{1.3}
\]

Exact Poisson summation in \(k\) turns (1.2) into the fixed-centre
truncated-divisor wavelet

\[
 \mathscr R_{D,L}(X)=
 \sum_{s\ge1}\ \sum_{\substack{r\mid s\\r\ {\rm odd}}}
 \chi _4(r)W\!\left({X\over rD}\right)
 \mathcal Q_L\!\left({r(X-s)\over4X}\right)+O_A(X^{-A}),    \tag{1.4}
\]

\[
 \mathcal Q_L(y)=\int_0^\infty {q_L(h)\over h}e(hy)\,dh .   \tag{1.5}
\]

It has physical width \(\Delta=D/L\).  Absolute divisor bounds give
\(\mathscr R_{D,L}\ll_\varepsilon\Delta X^\varepsilon\), whereas
(1.3) needs \(X^{1/4+\varepsilon}\).  The exact missing factor is

\[
 {\Delta\over X^{1/4}}={D\over LX^{1/4}}={H_D\over L}.       \tag{1.6}
\]

It is one only on the already-owned terminal line \(L\asymp H_D\) and is
a positive power throughout the strict residual region.  Thus (1.4), with
all its literal weights, is the smallest surviving signed correlation.

## 2. Exact statement and hypotheses

Let \(e(z)=e^{2\pi iz}\), \(X\ge2\),
\(X^{1/4}\le D\le X^{1/2}\), \(1\le L\le H_D\),
\(H_D=\lfloor DX^{-1/4}\rfloor\), and \(K=XL/D^2\).  Put

\[
 q_L(h)=\eta(h/L)\Phi(h/(H_D+1)),
\]

and retain the literal smooth physical profile \(W\), every sign, quarter
shift, floor, endpoint star, support crossing, and all prior-owner
restrictions.  On a smooth cell the normalized symbol is exactly

\[
 a_{L,K}(h,k)=q_L(h)\left({LK\over hk}\right)^{3/4}
 W\!\left(\sqrt{{hX\over4kD^2}}\right).              \tag{2.1}
\]

The theorem above applies to

\[
 \mathcal T_{L,K}=\sum_{h,k\ge1}\chi _4(h)a_{L,K}(h,k)
 e(\sqrt{Xhk}).                                      \tag{2.2}
\]

Smooth collars are flat at their support boundary.  Literal one-sided or
starred pieces are retained as separate finite collar terms; none is
replaced by a rectangular cutoff.  Negative physical frequency is the
conjugate calculation.  The unbalanced residual exponent range is

\[
 {1\over4}\le\delta<{1\over2},\qquad
 0\le\ell<\delta-{1\over4},\qquad
 178\ell+1638\delta>463,
\]

with \(D=X^\delta,L=X^\ell\).  No statement is made for the hard profile,
balanced packet, or a packet removed by terminal, second-derivative, or
TTY ownership.

## 3. Proof and derivation

**Coefficient-preserving double Mellin formula.**  Write \(M=LK\) and
\(F=\sqrt{XM}=XL/D\).  For
\(A(u,v)=a_{L,K}(Lu,Kv)\), choose \(V\in C_c^\infty(0,\infty)\), nonzero
on the product projection of \(\operatorname{supp}A\), and write
\(A(u,v)=B(u,v)V(uv)\).  Then

\[
 B(u,v)={1\over(2\pi)^2}\int_{\mathbb R^2}
 \widehat B(t_1,t_2)u^{it_1}v^{it_2}\,dt_1dt_2,       \tag{3.1}
\]

where \(\widehat B\) has rapid decay uniformly in the normalized smooth
seminorms.  If

\[
 A_{\boldsymbol t}(n)=\sum_{hk=n}\chi _4(h)h^{it_1}k^{it_2},
\]

then, coefficient by coefficient,

\[
 \sum_{n\ge1}{A_{\boldsymbol t}(n)\over n^s}
 =L(s-it_1,\chi _4)\zeta(s-it_2).                    \tag{3.2}
\]

With \(G_F(y)=V(y)e(F\sqrt y)\) and
\(\widetilde G_F(s)=\int_0^\infty G_F(y)y^{s-1}dy\), (2.2) is the
\((t_1,t_2)\)-integral of

\[
 {1\over2\pi i}\int_{(c)}\widetilde G_F(s)M^s
 L(s-it_1,\chi _4)\zeta(s-it_2)\,ds,qquad c>1.      \tag{3.3}
\]

The independent angular heights \(t_1,t_2\) decay rapidly.  For those
heights the radial height \(\tau=\Im s\) is localized by stationary phase
to \(\tau=-\pi F\sqrt y\asymp-F\).  Thus the two local conductors are
\(4(1+|\tau-t_1|)\asymp F\) and
\(1+|\tau-t_2|)\asymp F\).

**Functional equations and roots.**  The exact factors are

\[
 X_4(z)=\left({4\over\pi}\right)^{1/2-z}
 {\Gamma(1-z/2)\over\Gamma((z+1)/2)},\qquad
 X_0(z)=\pi^{z-1/2}{\Gamma((1-z)/2)\over\Gamma(z/2)},
\]

\[
 L(z,\chi _4)=X_4(z)L(1-z,\chi _4),\qquad
 \zeta(z)=X_0(z)\zeta(1-z).                         \tag{3.4}
\]

Both root numbers are \(+1\).  Shifting (3.3) left and expanding the
dual series gives exactly

\[
 \sum_{r,d\ge1}{\chi _4(r)r^{-it_1}d^{-it_2}\over rd}
 \mathscr K_{\boldsymbol t,F}(Mrd)+\mathscr P_{\boldsymbol t}, \tag{3.5}
\]

\[
 \mathscr K_{\boldsymbol t,F}(Y)={1\over2\pi i}
 \int_{(-c_0)}\widetilde G_F(s)X_4(s-it_1)X_0(s-it_2)Y^s\,ds. \tag{3.6}
\]

The only crossed pole is that of \(\zeta(s-it_2)\); its residue contains
\(\widetilde G_F(1+it_2)\) and is rapidly small by nonstationary
integration, while the angular tails cover \(|t_2|\asymp F\).  Equations
(3.5)--(3.6) are otherwise exact.  Since
\(X_j(z)X_j(1-z)=1\) and \(|X_j(1/2+i\tau)|=1\), applying the transform
twice recovers (3.2) coefficient by coefficient and preserves Mellin
\(L^2\) capacity.  There is no hidden root-number saving.

**Lengths and Gaussian constant.**  Resolving

\[
 \chi _4(h)={e(h/4)-e(3h/4)\over2i}
\]

and Poisson summing \(h\), let \(\rho=1,3\), with signs
\(\sigma_1=1,\sigma_3=-1\), and put \(r=4m-\rho\).  The stationary point
and phase are

\[
 h_*= {4Xk\over r^2},\qquad
 \sqrt{Xkh_*}+(\rho/4-m)h_*={Xk\over r},qquad
 |f''(h_*)|^{-1/2}=4\sqrt2(Xk)^{1/2}r^{-3/2}.         \tag{3.7}
\]

Because \(-\sigma_\rho=\chi _4(r)\), the two quarter branches combine,
with no absolute value, to

\[
 2\sqrt2\,i e(-1/8)\chi _4(r)(Xk)^{1/2}r^{-3/2}.    \tag{3.8}
\]

Substitution of the literal symbol (2.1) gives the exact simplification

\[
 (Xk)^{1/2}r^{-3/2}a(h_*,k)
 ={(LK)^{3/4}X^{-1/4}\over2\sqrt2}
 {q_L(4Xk/r^2)\over k}W\!\left({X\over rD}\right),  \tag{3.9}
\]

which proves (1.1)--(1.2).  The stationary error summed over the
\(F/L\) dual frequencies and \(K\) values of \(k\) is
\(E_{L,K}\ll KF^{-1/2}\); after the physical prefactor it is
\(O(L^{-1})\).  The inherited \(e(1/8)\) therefore cancels the Gaussian
\(e(-1/8)\), leaving exactly \(-i/(2\pi)\) in (1.3).

The first dual factor has length
\(R\asymp F/L\asymp X/D\), with its exact factor-two support retained by
\(W(X/(rD))\); the second has length \(F/K\asymp D\).  Their product is
\(X\), not a shorter box.  Exact Poisson summation in \(k\), followed by
\(h=4Xk/r^2\), gives

\[
 \sum_k{q_L(4Xk/r^2)\over k}e(Xk/r)
 =\sum_{d\in\mathbb Z}\int_0^\infty {q_L(h)\over h}
 e\!\left({hr(X-dr)\over4X}\right)dh,               \tag{3.10}
\]

and hence (1.4).  Repeated integration by parts in (1.5) restricts it to
\(|rd-X|\ll_A(D/L)X^\varepsilon\).  Thus the transformed box is a thin
product wavelet of raw capacity \(D/L\); inverse Poisson and (3.4) return
the original packet exactly.

## 4. First doubtful or unproved step

There is no doubtful algebraic step in (3.1)--(3.10) under the stated
smooth-cell hypotheses.  The first unproved analytic assertion is exactly

\[
 \left|\sum_{s\ge1}\sum_{\substack{r\mid s\\r\ \mathrm{odd}}}
 \chi _4(r)W\!\left({X\over rD}\right)
 \mathcal Q_L\!\left({r(X-s)\over4X}\right)\right|
 \ll_\varepsilon X^{1/4+\varepsilon}.               \tag{4.1}
\]

Divisor bounds give only \((D/L)X^\varepsilon\).  Hence (4.1) requires a
genuine signed saving \(H_D/L\).  A Mellin functional equation, scalar
Plancherel, coefficient energy, or formal completion to \(r_2\) supplies
none of it.  For nonsmooth endpoint atoms, the first additional seam is
the corresponding one-sided Fresnel kernel; it must remain attached to
its star and cannot be inferred from the smooth formula.

## 5. Required controls and outcomes

- **Raw versus weighted mass and coefficient energy:**
  \(\sum_{h,k}|a(h,k)|\ll M\), while the grouped coefficient satisfies
  \(\sum_{n\asymp M}|\sum_{h\mid n}\chi _4(h)a(h,n/h)|^2
  \ll_\varepsilon M^{1+\varepsilon}\).  Cauchy still gives the trivial
  \(M^{1+\varepsilon}\), not \(M^{3/4}\).  On the dual side the same
  capacity is \(\Delta=D/L\); critical-line gamma factors have modulus
  one.

- **No compatible \(r_2/4\) completion:** the full coefficient is
  \(\sum_{r\mid s}\chi _4(r)=r_2(s)/4\), whereas (1.4) retains only
  \(r\asymp X/D\), the exact \(W\)-profile, the \(r\)-dependent wavelet,
  height floor, taper, stars, and prior owners.  At \(X=s=p\), with a
  large prime \(p\equiv1\pmod4\), every active smooth
  \(D\in[p^{1/4},p^{1/2}]\) misses the divisors \(1,p\); its central
  truncated coefficient is zero, while \(r_2(p)/4=2\).  For a square the
  central divisor lies in the hard profile, and for a fourth power the
  extreme and central factor pairs lie on bottom/hard owners.  Thus exact
  products, primes, squares, and fourth powers all preserve the angular
  truncation.  Artificially adding the complement imports packets not
  proved target-safe and, by the authorized M1 recombination audit, the
  completed radial object is a Hardy--Voronoi return rather than a gain.

- **Signed, unsigned, random, and adversarial:** (3.8) retains the actual
  \(\chi _4\) sign.  Unsigned divisor mass gives only \(\Delta X^\varepsilon\).
  Random signs suggest cancellation but prove nothing; phase-conjugated
  adversarial coefficients saturate raw capacity.  Therefore no estimate
  here proves the false coefficient-uniform analogue.

- **Endpoints and owners:** in exponent notation the deficit is
  \(X^{\delta-\ell-1/4}\).  It equals one only at
  \(\ell=\delta-1/4\), already terminal-owned, and is positive at every
  strict residual point; for example \((\delta,\ell)=(1/3,0)\) misses by
  \(X^{1/12}\).  SD and TTY cells, the unique hard band, balanced packets,
  and all previous owner masks are unchanged.  Both frequency signs,
  both quarter shifts, real-\(X\) floors, support crossings, and stars are
  transported, not erased.

- **Transform inversion, conductors, and sources:** (3.4) and exact
  Poisson inversion pass; the transformed lengths are
  \((X/D,D)\) with product thickness \(D/L\).  No external theorem is
  invoked.  In particular Popov/Voronoi, double-large-sieve, cone, or
  exponent-pair results are not applied to the literal moving coefficient;
  baseline TTY coverage is merely retained.

## 6. Dependencies and exact artifacts used

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/derivation_packet.md`
- `rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/candidates/conductor_truncated_r2_fork.md`
- `rounds/codex-managed/m9-frequency-phase-diagram/reports/dual_three_quarter_attack.md`
- `rounds/codex-managed/m9-m2-outside-packet-endpoint-assembly/synthesis.md`
- `rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md`
- Conductor messages fixing the \(h\)-B/\(k\)-Poisson constant and scale
  ledger; all displayed constants were independently checked above.

No sibling Round-107 report, external source, or numerical artifact was
used.

## 7. Recommended state effect

**Promote** the exact coefficient-preserving Mellin/functional-equation
identity (3.1)--(3.6), the root-number and inversion ledger, and the
literal \(h\)-B/\(k\)-Poisson identity (1.1)--(1.5).  **Record** the scoped
no-go: the transform has equal scalar capacity, does not complete the
physical packet to \(r_2/4\), and creates no nonempty residual corridor.
**Retain** (4.1) as the smallest exact signed truncated-divisor survivor,
with missing power \(H_D/L\).  **Retain open** the unbalanced
three-quarter estimate, balanced and hard parents, M9-M2, M9, endpoint
uniformity, and the Gauss target.  No downstream exponent claim is
licensed.
