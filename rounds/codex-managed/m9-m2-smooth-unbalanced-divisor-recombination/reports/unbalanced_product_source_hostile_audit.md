# Round 107 unbalanced-product hostile/source audit

## 1. Result

**No-go lemma (literal truncated-divisor routes).**  Let \(X\) be large,
\(D=X^\delta\), \(L=X^\ell\), and

\[
 \frac14\leq\delta<\frac12,\qquad
 0\leq\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463,
\]

with the fixed-support boundary cells and their assigned owners treated
separately.  Put

\[
 K=\frac{XL}{D^2},\qquad M=LK=\frac{XL^2}{D^2},\qquad
 F=\sqrt{XM}=\frac{XL}{D},\qquad H_D=DX^{-1/4}.
\]

Assume the literal conductor split (K/L>16); the equality boundary is
owned by the balanced packet.

For the literal smooth positive M2 packet

\[
 \mathcal T_{L,K}
 =\sum_{h\asymp L}\sum_{k\asymp K}
   \chi_4(h)a_{L,K}(h,k)e(\sqrt{Xhk}),
\]

exact product regrouping and smooth Mellin separation are valid.  They do
not prove

\[
 \mathcal T_{L,K}\ll_\varepsilon M^{3/4}X^\varepsilon.
\]

Every audited completion/transform has one of the following outcomes.

1. Completing the moving coefficient to \(r_2/4\) is false before an
   additional physical one-count identity.  If one nevertheless passes to
   the complete radial coefficient at cutoff \(N=M\), Popov's exact
   remainder is
   \(\sqrt{X/M}\,X^{o(1)}=(D/L)X^{o(1)}\), exceeding the physical
   \(X^{1/4}\) target by the factor \(H_D/L>1\).  Extending to
   \(N\asymp X^{1/2}\) makes the error target-sized but returns to a radial
   sum equivalent to the Gauss-circle target.
2. On the radial Mellin saddle \(|\Im s|\asymp F\), the beta and zeta
   functional equations have root number \(+1\) and dual factor scales
   \(X/D\) and \(D\), respectively.  Their product is \(X\), not a shorter
   residual packet.  The reflected Mellin modes retain the character and
   the transformed owner kernel.
3. Resolving \(\chi_4\), applying the \(h\)-B-process, and then applying
   \(k\)-Poisson gives, at principal-symbol level and with the exact
   constant, a fixed-centre product-wavelet row supported on
   \(|dr-X|\lesssim D/L\).  Its absolute divisor-bound capacity is
   \((D/L)X^\varepsilon\); the required gain is again
   \[
     \frac{D/L}{X^{1/4}}=\frac{H_D}{L}.
   \]
   Thus this is an equal-capacity return, not an independent saving.

No Popov/Voronoi, double-large-sieve, cone-decoupling, Huxley, or current
exponent-pair theorem in the audited primary sources supplies the missing
signed estimate with the literal coefficient, profiles, owners, contours,
and endpoint errors.  This is a route-specific no-go result, not a lower
bound for the actual sum and not a disproof of the open three-quarter
estimate.

## 2. Exact statement and hypotheses

The actual normalized smooth symbol is

\[
 a_{L,K}(h,k)
 =q_L(h)\left(\frac{LK}{hk}\right)^{3/4}
 W\!\left(\sqrt{\frac{hX}{4kD^2}}\right),
\]

where \(q_L\) contains the literal Vaaler taper, height floor, and the
assigned \(h\)-profile.  The full packet also carries the physical profile,
both quarter shifts, both frequency signs when the real block is
reassembled, floors, stars, support crossings, and every prior owner.  A
rapidly decaying two-variable Mellin transform is legitimate only on a
fixed smooth component.  A sharp clipped row, star, or arithmetic owner is
not silently a smooth Mellin amplitude; it must be extracted or transported
as its exact finite kernel.

Product grouping is the exact identity

\[
 \mathcal T_{L,K}
 =\sum_{n\asymp M}A_{L,K}(n)e(\sqrt{Xn}),\qquad
 A_{L,K}(n)=\sum_{h\mid n}\chi_4(h)a_{L,K}(h,n/h).
\]

Its exact squared energy is

\[
\begin{aligned}
 \sum_n|A_{L,K}(n)|^2
  =\!\!\sum_{\substack{g,a,b,c\geq1\\ (a,b)=1}}
  &\chi_4(ga)\overline{\chi_4(gb)}\,
  a_{L,K}(ga,bc)\,
  \overline{a_{L,K}(gb,ac)},
\end{aligned}
\]

with the four displayed arguments constrained by their literal supports.
The parametrization is \(h_1=ga\), \(h_2=gb\),
\(k_1=bc\), \(k_2=ac\).  Divisor bounds give only

\[
 \sum_n|A_{L,K}(n)|^2\ll_\varepsilon MX^\varepsilon.
\]

Cauchy against the \(M\) radial phases therefore gives
\(|\mathcal T_{L,K}|\ll MX^\varepsilon\), not \(M^{3/4}\).
This energy is evidence about exact-product multiplicity, not a signed
estimate.

For a separated smooth Mellin mode, with the sign convention in the
campaign packet,

\[
 A_{\boldsymbol t}(n)
  =\sum_{hk=n}\chi_4(h)h^{it_1}k^{it_2},\qquad
 \sum_{n\geq1}\frac{A_{\boldsymbol t}(n)}{n^s}
  =L(s-it_1,\chi_4)\zeta(s-it_2).
\]

This is the complete convolution for that Mellin mode.  The literal
\(A_{L,K}\) is its inverse-Mellin superposition with the angular/slanted
cutoff still present; it is not the zero-mode coefficient.

Indeed,

\[
 \frac{r_2(n)}4=\sum_{h\mid n}\chi_4(h)
\]

uses every divisor.  A prime \(p\equiv3\pmod4\) already falsifies a
coefficient identity: a packet containing \((h,k)=(1,p)\) can have
\(A_{L,K}(p)=a_{L,K}(1,p)\neq0\), whereas \(r_2(p)/4=0\).
Squares and fourth powers likewise retain only those divisor incidences in
the slanted \(L\times K\) support, with the actual weights; complementary
divisors generally lie outside the unbalanced packet.  Summing only the
unbalanced residual labels cannot repair this: the missing incidences are
owned by terminal, TTY, hard, balanced, boundary, and previously removed
physical packets.  Round 97's physical one-count reduction treats those as
distinct owners, two of which remain analytically open.

## 3. Proof and hostile route audit

**Mellin heights, conductors, and root numbers.**  For a fixed smooth
component, normalized Mellin inversion gives

\[
 a(h,k)=\frac1{(2\pi)^2}\iint
 \widehat a(t_1,t_2)(h/L)^{it_1}(k/K)^{it_2}\,dt_1dt_2,
\]

with rapid decay in \(t_1,t_2\).  Mellin transforming the radial weight
\(w(n/M)e(\sqrt{Xn})\) introduces a further contour \(s=\sigma+iv\).
Stationary phase in logarithmic \(n\) localizes the non-negligible part to
\(|v|\asymp F=\sqrt{XM}\).  Since the smooth angular Mellin heights may be
truncated to \(X^{o(1)}\), both factor heights
\(|v-t_1|\) and \(|v-t_2|\) are \(\asymp F\).

The completed factors are

\[
\Lambda_4(z)=\left(\frac4\pi\right)^{(z+1)/2}
 \Gamma\!\left(\frac{z+1}{2}\right)L(z,\chi_4),
\qquad
\Lambda_\zeta(z)=\pi^{-z/2}\Gamma(z/2)\zeta(z).
\]

Because \(\chi_4\) is primitive odd of conductor \(4\) and
\(\tau(\chi_4)=2i\), its completed root number is
\(i^{-1}\tau(\chi_4)/2=+1\).  Thus

\[
 \Lambda_4(z)=\Lambda_4(1-z),\qquad
 \Lambda_\zeta(z)=\Lambda_\zeta(1-z).
\]

The two-factor root number is \(+1\), so there is no antisymmetric
root-number cancellation.  Reflection sends
\((t_1,t_2)\) to \((-t_1,-t_2)\), keeps the character on the same divisor
leg, and sends the smooth angular symbol to its reflected inverse-Mellin
kernel.  It does not replace that kernel by \(1\).

At height \(F\), factorwise duality sends the \(h\)-length and \(k\)-length
to

\[
 L^\ast\asymp \frac{F}{L}=\frac XD,\qquad
 K^\ast\asymp \frac{F}{K}=D,\qquad
 L^\ast K^\ast\asymp X.
\]

Applying only the zeta functional equation is the inverse
\(k\)-B-process and returns the original \(h\times d\) reciprocal block.
Applying only the beta functional equation gives the \(r\times k\) row
derived below.  Applying both puts the product variable at the dual centre
\(dr\asymp X\).  Apparent shortening of one factor is cancelled by its
gamma/Jacobian weight; no norm decrease follows from the identity.  A
common contour shift also crosses the pole of
\(\zeta(s-it_2)\) at \(s=1+it_2\).  Its face/residue contribution is not
zero mode by mode and can be cancelled only under an exact common physical
owner.  Root number \(+1\) does not remove it.

**The exact principal \(h\)-B/\(k\)-Poisson return.**  Resolve

\[
 \chi_4(h)=\frac{e(h/4)-e(-h/4)}{2i}
 =\sum_{\tau=\pm1}\frac{\tau}{2i}e(\tau h/4).
\]

For fixed \(k\), Poisson/B-process on the branch
\[
 f_\tau(h)=\sqrt{Xkh}+\frac{\tau h}{4}
\]
has dual integer \(m\).  Put
\[
 r=4m-\tau,\qquad p=m-\tau/4=r/4.
\]
The stationary data are

\[
 h_\ast=\frac{4Xk}{r^2},\qquad
 f_\tau(h_\ast)-mh_\ast=\frac{Xk}{r},\qquad
 |f_\tau''(h_\ast)|^{-1/2}
 =4\sqrt2\,(Xk)^{1/2}r^{-3/2}.
\]

The two congruence branches cover the odd \(r\)'s once, and
\(\tau=-\chi_4(r)\).  Including \(\tau/(2i)\), their combined principal
coefficient is therefore

\[
 2\sqrt2\,i\,e(-1/8)\chi_4(r)(Xk)^{1/2}r^{-3/2}.
\]

Substitution of the literal symbol at \(h_\ast\) gives exactly

\[
\boxed{
 \mathcal T_{\rm main}
 =i e(-1/8)X^{-1/4}(LK)^{3/4}
 \sum_{\substack{r\geq1\\r\ {\rm odd}}}
 \chi_4(r)W\!\left(\frac{X}{rD}\right)
 \sum_k\frac{q_L(4Xk/r^2)}{k}e\!\left(\frac{Xk}{r}\right).}
\]

Consequently the inherited physical normalization

\[
 -\frac{e(1/8)}{2\pi}X^{1/4}(LK)^{-3/4}
\]

cancels every scale and Gaussian factor and leaves precisely
\(-i/(2\pi)\) times the displayed \(r,k\) row.

Poisson summation in \(k\), followed by
\(h=4Xx/r^2\), is also exact at the integral level:

\[
 \sum_k\frac{q_L(4Xk/r^2)}{k}e(Xk/r)
 =\sum_{d\in\mathbb Z}
 \int_0^\infty\frac{q_L(h)}{h}
 e\!\left(h\left[\frac r4-\frac{dr^2}{4X}\right]\right)\,dh.
\]

The logarithmic Fourier kernel is negligible unless

\[
 |dr-X|\lesssim \Delta,\qquad \Delta=\frac DL.
\]

Regrouping by the exact product \(s=dr\) gives the smallest returned
correlation

\[
\boxed{
 \mathscr R_{D,L}(X)=
 \sum_{\substack{s\in\mathbb Z\\|s-X|\lesssim\Delta}}
 \ \sum_{\substack{r\mid s\\r\ {\rm odd}}}
 \chi_4(r)W\!\left(\frac{X}{rD}\right)
 \int_0^\infty\frac{q_L(h)}h
 e\!\left(\frac{hr(X-s)}{4X}\right)\,dh,}
\]

with the actual profiles, cutoff tails, stars, and owner complements
retained rather than replaced by the schematic sharp window.  Divisor
bounds give

\[
 |\mathscr R_{D,L}(X)|\ll_\varepsilon \Delta X^\varepsilon,
\]

whereas the physical target is \(X^{1/4+\varepsilon}\).  Since
\(\Delta/X^{1/4}=H_D/L>1\) throughout the strict residual region, the
chain has exactly the pre-existing physical-height deficit.  It closes
only on the terminal line \(L=H_D\), which already has a prior owner.

The boxed principal formula is not by itself a full transform theorem.
The literal clipped top frequency can create one-sided endpoint/Fresnel
terms, and a per-\(k\) \(O(1)\) B-process error would sum to an unsafe
quantity.  A full equality must retain the exact Fourier integrals or prove
a target-safe aggregate stationary remainder.  Replacing
\(W(X/(rD))\) by \(W(d/D)\), or replacing the smooth Fourier kernel by a
sharp condition \(dr=X\), is also not exact.  These qualifications do not
create a saving; they prevent over-promotion of the self-return.

**Popov and Voronoi.**  Popov's Theorem 5 applies, for \(x,N\geq3\), to
the complete coefficient \(r_2(n)\), the complete interval \(n\leq N\),
and the real cosine combination:

\[
 P(x)=-\frac{x^{1/4}}{\pi}\sum_{n\leq N}
 \frac{r_2(n)}{n^{3/4}}
 \cos\!\left(2\pi\sqrt{nx}+\frac\pi4\right)
 +O\!\left(\sqrt{\frac xN}\,\overline r(x)
 +\overline r(N)\log N\right).
\]

At the literal packet length \(N=M\), the first error is
\[
 \sqrt{X/M}\,X^{o(1)}=\frac DL X^{o(1)}
 =X^{1/4}\frac{H_D}{L}X^{o(1)}.
\]
At \(N\asymp X^{1/2}\) it is target-sized, but the completed radial sum is
then equivalent, in both directions up to target-sized errors, to the
Gauss-circle target.  Popov has no theorem for \(A_{L,K}(n)\), for one
quarter-shift/positive complex frequency alone, or for a slanted
moving-divisor cutoff.  A general shifted Eisenstein/Voronoi identity
applied after Mellin separation would still reflect the complete
\(A_{\boldsymbol t}\) modes and then inverse-Mellin-reconstruct the angular
owner; it is a transformation, not the missing estimate.

**Current exponent pairs.**  Tao--Trudgian--Yang Theorem 20 certifies
\[
 (\kappa,\lambda)=\left(\frac{89}{1282},
 \frac{997}{1282}\right)
\]
for one-dimensional model phases.  It lawfully transfers through a
normalized BV weight, but not through an arbitrary irregular coefficient
\(A_{L,K}(n)\) after product grouping.  Applied rowwise in \(k\) before
grouping, it gives
\[
 |\mathcal T_{L,K}|
 \ll_\varepsilon L\,D^\kappa K^\lambda X^\varepsilon.
\]
Relative to \(M^{3/4}\), its exponent is
\[
 \frac{71}{2564}+\frac{178}{641}\ell+\frac{9}{641}\delta>0.
\]
Thus the current pair produces no new product-phase cell at all.  The
already accepted reciprocal-side wedge
\(178\ell+1638\delta\leq463\) is obtained in a different
one-dimensional normalization; the Round 107 residual is its strict
complement.  An unweighted derivative estimate for
\(\sum_n e(\sqrt{Xn})\) cannot be applied to the moving \(A_{L,K}(n)\).

**Double large sieve and cone decoupling.**  Li--Yang Proposition 3.1 is
an \(L^q\) first-spacing estimate for
\[
 \sum_{k\sim K_0}\sum_{l\sim L_0}a_{kl}
 e(lx_1+klx_2+l\sqrt{k}\,x_3),
\]
under \(1\leq L_0<K_0\leq\eta^{-1}\leq K_0L_0\),
\(4\leq q\leq4.5\), and
\((L_0/K_0)^{(q-2)/(q-4)}\leq\eta\).  Its cone input is an
\(L^q(\mathbb R^3)\) decoupling theorem for Schwartz functions whose
Fourier transforms lie in a thin truncated-cone neighborhood, with cap
parameters \(\beta_1\in[1/2,1]\), \(\beta_2\in[0,1]\).  Neither is a
pointwise theorem at the single vector defining
\(e(\sqrt{Xhk})\).

Li--Yang's later double-large-sieve theorem applies to the separated
standard reciprocal sum
\[
 S=\sum_{H\leq h\leq2H}g(h/H)
 \sum_{M_0\leq m\leq2M_0}G(m/M_0)
 e\!\left(\frac{hT}{M_0}F(m/M_0)\right),
\]
with \(g,G\) of bounded variation, \(F\in C^3\), all first three
derivatives bounded above and below, the additional determinant condition
\(|F'F'''-3(F'')^2|\gg1\), and the detailed Case A/Case B and second-spacing
inequalities.  The product symbol is slanted rather than separated, while
the returned \(s=dr\) row is a prescribed-centre divisor correlation, not
their first/second-spacing ensemble.  Mapping the original reciprocal
block back to their standard sum only recovers their audited global
exponent \(0.314483\ldots\), not \(1/4\).  Their own introduction explains
that short-sum decomposition loses orthogonality and does not reach the
quarter exponent.  Moreover, the project source card accepts the repaired
final Li--Yang application, not Proposition 3.1 in unrestricted printed
generality.

The rank-one Hessian of \(\sqrt{Xhk}\) identifies a cone geometry:
\[
 \det \operatorname{Hess}_{h,k}\sqrt{Xhk}=0.
\]
This does not turn a cone \(L^q\) average into the required pointwise
signed estimate.  A coefficient-blind pointwise theorem would be false by
phase-conjugating coefficients.  The actual \(\chi_4\) and slanted symbol
may exclude that artificial example, but no cited cone or large-sieve
theorem exploits precisely those literal features.

**Huxley and Bourgain--Watt.**  The local Huxley 2003 card has no theorem,
hypotheses, constants, or project translation; the official paper concerns
the full Bombieri--Iwaniec--Mozzochi discrepancy/second-spacing
architecture, not the displayed truncated-divisor row.  It cannot be
imported until an exact theorem map is completed.  Bourgain--Watt
arXiv:1709.04340 is withdrawn: the authors state that Propositions 2, 3,
and \(1'\) have a gap/fault and Theorems 1--3 lose theorem status.  It is
method history only.  No conclusion in this audit depends on it.

## 4. First doubtful or unproved step

The earliest proposed positive step, completion
\[
 A_{L,K}(n)=r_2(n)/4,
\]
is not merely unproved; it is false, as the prime and asymmetric-support
controls show.  The earliest lawful replacement would be an exact
physical one-count formula summing all complementary profiles and owners
before absolute values.  No such formula is supplied for the isolated
unbalanced residual packet, and adding the complements imports the open
balanced and hard M2 parents or the complete radial target.

After refusing that false completion, the first unproved analytic step is
the signed prescribed-centre estimate
\[
 \mathscr R_{D,L}(X)\ll_\varepsilon X^{1/4+\varepsilon}
\]
for the boxed literal \(s=dr\) correlation, equivalently the original
\(M^{3/4}\) product-phase estimate.  Absolute divisor bounds miss by
\(H_D/L\).  No audited source proves this correlation.

Separately, any claim that the \(h\)-B/\(k\)-Poisson chain is an exact
full-symbol theorem must first prove a uniform aggregate stationary
remainder and transport every clipped endpoint, star, profile crossing,
and prior owner.  The principal constant and scale cancellation are
proved above; target-safe full errors are not.  Likewise, a
functional-equation proof must display the radial contour, the two angular
height contours, the zeta pole, horizontal tails, and the transformed
owner kernel.  Merely writing the two functional equations is not that
proof.

## 5. Required controls and outcomes

1. **Raw versus weighted product mass — pass/no gain.**  The exact
   \(ga,gb,bc,ac\) energy parametrization reproduces all equal products.
   Divisor bounds give \(MX^\varepsilon\), and Cauchy gives only the
   trivial \(M\) scale.
2. **Primes, squares, and fourth powers — completion fails.**  A
   \(p\equiv3\pmod4\) one-incidence packet disagrees with
   \(r_2(p)/4=0\).  Squares and fourth powers expose the same missing
   divisor legs and unequal slanted weights.  Complementary-divisor
   cancellation is unavailable when \(K/L>16\).
3. **Signed, unsigned, random, and adversarial — route guard passes.**
   The two B-process branches recombine to the literal \(\chi_4(r)\);
   neither Cauchy nor absolute divisor bounds are advertised as signed
   control.  Artificial coefficients
   \(c(n)=e(-\sqrt{Xn})\) make a coefficient-blind product-phase theorem
   false.  This does not refute the actual coefficient; it proves that a
   successful theorem must use it.
4. **Quarter shifts and root numbers — no cancellation.**  Both
   \(\tau=\pm1\) branches are present once, their constants give
   \(+2\sqrt2\,i\,e(-1/8)\chi_4(r)\), and both completed degree-one
   factors have root number \(+1\).  The negative physical frequency is
   the conjugate needed for the real cosine sum, not a bound for the
   positive complex block.
5. **Unbalanced endpoint scales — deficit reproduced.**  At
   \(D=X^{1/3},L=1\), \(\Delta=D/L=X^{1/3}\) misses by \(X^{1/12}\).
   At \(D=X^{3/8}\), the miss is \(X^{1/8}/L\).  At \(D=X^{1/2}\), it is
   \(X^{1/4}/L\).  On \(L=H_D\), \(\Delta=X^{1/4}\), exactly the already
   owned terminal line.
6. **Transform inversion and capacity — principal identity passes,
   full-error promotion fails.**  The factors
   \(h_\ast=4Xk/r^2\), \(e(Xk/r)\), the physical constant \(-i/(2\pi)\),
   the \(k\)-Poisson kernel, and the window
   \(|dr-X|\lesssim D/L\) agree.  The dual factor lengths multiply to
   \(X\), and regrouping has capacity \(\Delta\); no extra transform
   power remains.  Hard endpoints and aggregate B-errors were not proved
   target-safe.
7. **Primary-source hypothesis map — no applicable quarter theorem.**
   Popov requires complete \(r_2\); Li--Yang requires its standard
   reciprocal/spacing architecture and reaches only the audited
   \(0.314483\ldots\) theorem; Guth--Maldague is an \(L^p\) cone theorem;
   Tao--Trudgian--Yang is one-dimensional and gives no product-phase
   cell; Bourgain--Watt is withdrawn; the Huxley card is incomplete.
8. **Downstream scope — pass.**  The audit makes no claim for the
   balanced smooth packet, hard top, full M9-M2, endpoint uniformity, M9,
   or a global exponent.

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

Authorized local artifacts:

- protocol.md
- state/proof_obligations.yml
- state/active_campaign.yml
- rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/derivation_packet.md
- rounds/codex-managed/m9-frequency-phase-diagram/reports/dual_three_quarter_attack.md
- rounds/codex-managed/m9-m2-outside-packet-endpoint-assembly/synthesis.md
- sources/popov_2024_voronoi_gauss.md
- sources/li_yang_2023.md
- sources/bourgain_watt.md
- sources/huxley_2003.md

Primary sources checked:

- D. A. Popov, [“Voronoi's formulae and the Gauss
  problem”](https://www.mathnet.ru/eng/rm10162), especially Theorem 5,
  (5.1)--(5.2).
- Xiaochun Li and Xuerui Yang, [“An improvement on Gauss's Circle
  Problem and Dirichlet's Divisor
  Problem”](https://arxiv.org/html/2308.14859v2), especially Proposition
  3.1, Theorem 3.2 as used there, and Section 4's standard-sum
  hypotheses.
- Larry Guth and Dominique Maldague, [“Amplitude dependent wave envelope
  estimates for the cone in
  \(\mathbb R^3\)”](https://arxiv.org/html/2206.01093), Theorem 3 and its
  Fourier-support/\(L^p\) hypotheses.
- Terence Tao, Tim Trudgian, and Andrew Yang, [“New exponent pairs, zero
  density estimates, and zero additive energy estimates: a systematic
  approach”](https://arxiv.org/html/2501.16779), Definitions 11--12 and
  Theorem 20.
- Jean Bourgain and Nigel Watt,
  [arXiv:1709.04340](https://arxiv.org/abs/1709.04340), specifically the
  authors' withdrawal notice.
- M. N. Huxley, [“Exponential sums and lattice points
  III”](https://doi.org/10.1112/S0024611503014485), bibliographic record
  and official scope only; no theorem was imported.

No sibling Round 107 report, candidate derivation, shared synthesis, proof
draft, or validation matrix was read or edited.

## 7. Recommended state effect

**Retain**
M9-M2-smooth-unbalanced-three-quarter-estimate **open**, and make no
status change to M9-M2-physical-one-count-assembly, M9-M2, M9, or
the quarter target.

After independent seam review, the conductor may promote only the
following narrowly scoped algebra:

- exact product regrouping and the separated-mode Dirichlet series
  \(L(s-it_1,\chi_4)\zeta(s-it_2)\);
- the root-number/conductor ledger
  \((L^\ast,K^\ast)\asymp(X/D,D)\), with dual product \(X\);
- the displayed principal \(h\)-B/\(k\)-Poisson normalization through
  \(-i/(2\pi)\) and the prescribed-centre survivor
  \(\mathscr R_{D,L}(X)\), explicitly labelled
  principal-symbol-only until aggregate endpoint and stationary errors
  are proved.

Record or retain the following rejected claims:

- the unbalanced physical one-count completes \(A_{L,K}\) to \(r_2/4\);
- Popov/Voronoi bounds the truncated cone or makes the completed radial
  sum easier;
- the two functional equations give a shorter packet or root-number
  cancellation;
- \(h\)-B followed by \(k\)-Poisson supplies an independent power saving;
- a coefficient-blind exponent-pair, double-large-sieve, or cone theorem
  proves the literal product-phase target;
- withdrawn Bourgain--Watt or unaudited Huxley statements are theorem
  dependencies.

The sharp next analytic interface is

\[
 \boxed{\mathscr R_{D,L}(X)\ll_\varepsilon X^{1/4+\varepsilon}}
\]

with every literal profile and owner retained.  Its known absolute
capacity is \((D/L)X^\varepsilon\), so the missing signed power is exactly
\(H_D/L\).  This is the smallest coefficient-preserving survivor found by
the audit.
