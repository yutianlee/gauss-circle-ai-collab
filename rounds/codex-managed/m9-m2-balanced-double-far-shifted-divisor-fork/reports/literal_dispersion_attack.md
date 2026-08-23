## 1. Result: one-step literal dispersion has an exact equal-capacity seam

**Lemma/no-go (scoped to the first Fejer--Poisson dispersion).** Let \(B\) be one persistent \(j=1\) Round-113 block and let \(\mathcal E_{B,\mathrm{df}}\) be exactly the Round-114 double-far survivor. The smallest noninvertible outer-product dispersion is the Fejer window inequality applied to the literal product coefficient. Its zero mode is the positive full-product fibre energy

\[
E_0=\sum_n\left|\sum_{hk=n}a_B^<(h,k)\right|^2
   \ll_\varepsilon L^2X^\varepsilon,
\]

and not merely the atom diagonal \(h=h',k=k'\). If the Fejer length is \(H\) and the product support has diameter \(N_B\asymp LK\asymp L^2\), the noninvertible prefactor is \(P_H=(N_B+H-1)/H\). The accepted Round-114 estimates bound either complete corridor by \(O_\varepsilon(L^3X^\varepsilon)\) before dispersion; after dispersion they supply only the certified allowance

\[
\mathcal A_{\mathrm{corr}}(H)
\ll_\varepsilon P_HL^3X^\varepsilon
\ll_\varepsilon
\left(\frac{L^5}{H}+L^3\right)X^\varepsilon
\qquad (L\le H\le N_B).
\]

Thus those terms are certifiably target-safe from their accepted absolute owners only at the full **power** scale \(H=N_BL^{-o(1)}=L^{2-o(1)}\) (polylogarithmic losses are absorbed by \(X^\varepsilon\)). At that length the inequality still contains double-far shifts through the full power range and gives no fixed-power shortening. For \(2\le H\le L\), even the radial corridor has the available capacity

\[
P_H\,L^2(H+1)X^\varepsilon\ll L^4X^\varepsilon,
\]

so using its accepted absolute owner loses exactly the required factor \(L\). More generally, no \(H\le L^{2-\delta}\) with fixed \(\delta>0\) is certified target-safe by the Round-114 owners.

The companion Poisson checks do not remove this seam. The interior zero-frequency critical points are absent on the double-far support, but a bulk scalar model for the nonzero stationary family has potential \(L^4\) total absolute capacity. The factor \(\chi _4(h)\chi _4(h')\) shifts the relevant \(p/2\)-dual lattice by \(1/2\); it does not delete that stationary family. The fixed-\((p,q)\) phase is continuously nondegenerate when \(|\rho|>L\), but its two-dimensional Poisson aliases require a new modulo-one, actual-symbol cancellation theorem. Hence this report proves an exact first failed seam, not the desired bound and not an actual-symbol lower bound.

## 2. Exact statement and hypotheses

Assume \(X\ge4096\) is real, \(R=\sqrt X\asymp L^3\), \(1\le K/L\le16\), and \(B\) is one fixed persistent \(j=1\) physical block. Retain the literal real slanted symbol, all of its floors, tapers, profiles, stars and support crossings, and put

\[
a(h,k)=a_B^<(h,k)
=\chi _4(h)\eta\!\left(\frac{\gcd(h,k)}{\sqrt L/2}\right)A_B(h,k),
\qquad
c(n)=\sum_{hk=n}a(h,k),
\]

\[
b_n=c(n)e(R\sqrt n),
\qquad
\Gamma(r)=\sum_n b_n\overline{b_{n+r}}.
\tag{115.1}
\]

Zero-extend \(b_n\) to a consecutive interval \(I_B\) of length \(N_B\asymp LK\asymp L^2\). For \(r>0\), let \(\Gamma_{\le\rho}(r)\) be the same correlation as \(\Gamma(r)\), but after opening both divisor sums retain only \(|hk'-h'k|\le L\). The exact disjoint decomposition is

\[
\left|\sum_n b_n\right|^2
=E_0
+2\Re\sum_{1\le r\le L}\Gamma(r)
+2\Re\sum_{r>L}\Gamma_{\le\rho}(r)
+\mathcal E_{B,\mathrm{df}}.
\tag{115.2}
\]

The Round-114 bounds give

\[
E_0\ll_\varepsilon L^2X^\varepsilon,
\quad
\sum_{1\le r\le L}|\Gamma(r)|\ll_\varepsilon L^3X^\varepsilon,
\quad
\sum_{r>L}|\Gamma_{\le\rho}(r)|\ll_\varepsilon L^3X^\varepsilon.
\tag{115.3}
\]

In particular,

\[
\mathcal E_{B,\mathrm{df}}
=\left|\sum_n b_n\right|^2+O_\varepsilon(L^3X^\varepsilon),
\tag{115.4}
\]

with the sign of the owned terms understood through (115.2). No gate has been silently discarded: (115.2) restores the radial and determinant corridors exactly once and displays their cost.

For every integer \(1\le H\), translation averaging and one Cauchy inequality give the exact noninvertible estimate

\[
\left|\sum_n b_n\right|^2
\le P_H\,\mathfrak D_H,
\qquad
P_H=\frac{N_B+H-1}{H},
\tag{115.5}
\]

\[
\mathfrak D_H
=E_0+2\Re\sum_{1\le r<H}
\left(1-\frac rH\right)\Gamma(r)
=\frac1H\sum_m\left|\sum_{j=1}^{H}b_{m+j}\right|^2\ge0.
\tag{115.6}
\]

Equations (115.2)--(115.6), with the literal \(a(h,k)\), are the tested mechanism. A target proof through it would require

\[
\mathfrak D_H\ll_\varepsilon \frac{L^3}{P_H}X^\varepsilon
\asymp LHX^\varepsilon
\qquad (L\le H\le N_B),
\tag{115.7}
\]

whereas the accepted absolute corridor information is larger by \(N_B/H\) after multiplication by \(P_H\). This is a route-scoped implication audit; it does not assert that the literal signed quantity in (115.6) is large.

## 3. Proof and derivation

**Literal divisor and increment charts.** Substituting \(k=n/h\) and \(k'=(n+r)/h'\) gives

\[
\rho=hk'-h'k
=\frac{h^2(n+r)-h'^2n}{hh'},
\tag{115.8}
\]

so the determinant deletion remains an arithmetic condition inside the two divisor sums. With \(h'=h+p,\ k'=k+q\),

\[
r=hq+kp+pq,
\qquad \rho=hq-kp,
\qquad r+\rho=q(2h+p),
\qquad r-\rho=p(2k+q).
\tag{115.9}
\]

Only odd \(h,h'\) survive \(\chi _4\), hence \(p=2s\) and

\[
\chi _4(h)\chi _4(h+p)=(-1)^s=e(s/2).
\tag{115.10}
\]

Equations (115.8)--(115.10) preserve the gcd cutoffs and both copies of the slanted symbol; no product-fibre absolute value has been taken.

There is also a useful exact angular form. Put

\[
t=\log\frac h{\sqrt n},\qquad
t'=\log\frac {h'}{\sqrt{n+r}}.
\]

Then

\[
\rho=2\sqrt{n(n+r)}\sinh(t-t').
\tag{115.11}
\]

On balanced support \(\sqrt{n(n+r)}\asymp L^2\). Thus \(|\rho|>L\) imposes only angular divisor-ratio separation \(|t-t'|\gg L^{-1}\), while \(e(R(\sqrt n-\sqrt{n+r}))\) remains purely radial. The determinant gate therefore creates no phase oscillation within a fixed \((n,r)\)-fibre.

**Full energy and Fejer main term.** Expanding \(\Gamma(r)\) in (115.1) gives exactly the two literal divisor sums. Pairing \(r\) with \(-r\), assigning all \(|r|\le L\) pairs to the radial corridor, and then assigning \(|r|>L,\ |\rho|\le L\) to the determinant corridor proves (115.2). The three bounds in (115.3) are precisely the accepted equal-product and corridor estimates, so (115.4) follows.

For (115.5), each \(b_n\) occurs in exactly \(H\) translated windows. There are at most \(N_B+H-1\) nonzero windows, hence

\[
H^2\left|\sum_n b_n\right|^2
\le (N_B+H-1)\sum_m\left|\sum_{j=1}^{H}b_{m+j}\right|^2.
\]

Expansion of the last square proves (115.5)--(115.6). This Cauchy step is the first genuinely noninvertible operation.

The zero-shift/main contribution on the right of (115.5) is

\[
P_HE_0\ll_\varepsilon
\left(L^2+\frac{L^4}{H}\right)X^\varepsilon.
\tag{115.12}
\]

It is target-safe once \(H\gg L\). The corridors are more restrictive. If \(2\le H\le L\), the radial estimate with \(U=H\) gives the certified allowance

\[
P_H\sum_{r<H}|\Gamma(r)|
\ll_\varepsilon \frac{N_B}{H}L^2(H+1)X^\varepsilon
\ll_\varepsilon L^4X^\varepsilon.
\tag{115.13}
\]

If \(L\le H\le N_B\), either complete prior corridor has allowance

\[
P_H L^3X^\varepsilon
\ll_\varepsilon \frac{L^5}{H}X^\varepsilon+L^3X^\varepsilon.
\tag{115.14}
\]

At the level of powers, the right side becomes target-sized only at \(H=L^{2-o(1)}\); for every fixed \(\delta>0\), \(H\le L^{2-\delta}\) leaves the factor \(L^\delta\). Thus (115.6) still spans the full power range of \(\Gamma\) and retains the broad double-far correlation. If \(H>N_B\), all possible shifts occur and \(P_H\asymp1\); nothing is shortened. This proves the asserted fixed-power parameter no-go using only accepted estimates. It also explains why a corridor that was target-safe in (115.2) cannot simply be reused after a one-way Gram lift: its coefficient has changed from \(1\) to \(P_H(1-r/H)\).

There is an exact two-dimensional analogue on the atom array. For \(x_{h,k}=a(h,k)e(R\sqrt{hk})\), zero-extend to an integer box of side lengths \(N_h\asymp L\) and \(N_k\asymp K\). A \(P\)-by-\(Q\) translation window gives

\[
\left|\sum_{h,k}x_{h,k}\right|^2
\le \frac{(N_h+P-1)(N_k+Q-1)}{PQ}\,\mathfrak D_{P,Q},
\tag{115.15}
\]

Here

\[
\mathfrak D_{P,Q}
=\frac1{PQ}\sum_{u,v}
 \left|\sum_{i=1}^{P}\sum_{j=1}^{Q}x_{u+i,v+j}\right|^2
=\sum_{|p|<P}\sum_{|q|<Q}
 \left(1-\frac{|p|}{P}\right)
 \left(1-\frac{|q|}{Q}\right)
 \sum_{h,k}x_{h,k}\overline{x_{h+p,k+q}}\ge0.
\tag{115.15a}
\]

Thus \(\mathfrak D_{P,Q}\) is the exact triangularly weighted \((p,q)\)-correlation, whose zero shift is \(\sum_{h,k}|a(h,k)|^2\). The prefactor in (115.15) is \(\asymp L^2/(PQ)\) for \(P\le N_h,Q\le N_k\). Consequently, paying either complete \(O_\varepsilon(L^3X^\varepsilon)\) prior corridor inside this Gram lift is certified target-safe only at the full power area \(PQ=L^{2-o(1)}\); any fixed-power deficit in \(PQ\) reappears multiplicatively. This is the same owner-amplification seam, not an independent estimate.

**One-variable Poisson/B-process audit.** For the unshifted radial phase \(\phi(x)=R\sqrt x\) on \(x\asymp N_B\asymp L^2\),

\[
\phi'(x)=\frac{R}{2\sqrt x}=m,
\qquad
x_m=\frac{X}{4m^2},
\qquad
\phi(x_m)-mx_m=\frac{X}{4m},
\tag{115.16}
\]

and \(|\phi''(x)|\asymp R/N_B^{3/2}\asymp1\). There are \(\asymp L^2\) stationary integers \(m\asymp L^2\), each with stationary amplitude \(\asymp1\). The Poisson summand indexed by \(m=0\) still exists, but it has no interior critical point on this support; endpoint terms are separate. Thus the product-variable B-process is length- and amplitude-critical and returns the reciprocal phase \(X/(4m)\) on its stationary bulk. Moreover \(c(n)\) is an arithmetic divisor fibre, not a smooth scalar amplitude, so applying (115.16) literally would first require a new transform theorem for the actual \(c(n)\).

For a fixed positive shift \(r\), put

\[
\phi_r(x)=R(\sqrt x-\sqrt{x+r}).
\]

On a smooth bulk overlap interval of length \(\asymp L^2\), away from all literal support crossings, and for \(L<r<cL^2\) with a fixed sufficiently small \(c>0\),

\[
\phi_r'(x)\asymp r,
\qquad
|\phi_r''(x)|\asymp \frac r{L^2}.
\tag{115.17}
\]

the derivative range has length \(\asymp r\). The resulting smooth scalar model therefore has \(\asymp r\) nonzero stationary modes, each of stationary size \(L/\sqrt r\). Its potential absolute main-term budget is \(L\sqrt r\) for this shift, and

\[
\sum_{L<r<cL^2}L\sqrt r\asymp L^4.
\tag{115.18}
\]

The \(m=0\) Poisson summand again has no interior critical point, but its boundary terms have not been deleted. Equation (115.18) is only a bulk scalar-model capacity audit, not a lattice theorem, a bound, or a lower bound for the literal \(C_B(n,r)\); it shows that Poisson geometry itself does not supply the missing \(L\).

**Character and two-dimensional Poisson audit.** At fixed \(h,k,q\), Poisson in \(s=p/2\) sees the modulation \(e(s/2)\). Its stationary equation is, up to the harmless sign convention for the dual integer,

\[
R\sqrt{\frac{k+q}{h+2s}}\equiv \frac12\pmod{\mathbb Z}.
\tag{115.19}
\]

For a complete constant-amplitude model, the modulation would remove the ordinary zero coefficient. The literal amplitude is neither constant nor complete, so no actual-symbol Fourier coefficient is proved to vanish. In either case (115.19) shows that the modulation merely translates the stationary dual family by \(1/2\).

Finally set

\[
F_{p,q}(x,y)=\sqrt{(x+p)(y+q)}-\sqrt{xy}.
\]

Direct differentiation gives

\[
\det D^2F_{p,q}
=-\frac1{16}
\frac{\sqrt{xy}\sqrt{(x+p)(y+q)}(qx-py)^2}
{x^2(x+p)^2y^2(y+q)^2}.
\tag{115.20}
\]

Since \(qx-py=\rho\), \(x,y,x+p,y+q\asymp L\), and \(R\asymp L^3\),

\[
|\det D^2(RF_{p,q})|\asymp \rho^2.
\tag{115.21}
\]

Also \(\nabla F_{p,q}=0\) if and only if \(qx-py=0\). Hence determinant deletion removes the interior critical point of the zero-frequency two-dimensional Poisson integral and makes the continuous Hessian nondegenerate; it does not remove that Poisson summand or its sharp-gate boundary terms. On a generic smooth bulk cell \(|p|,|q|\asymp L,\ |\rho|\asymp L^2\), the continuous multiplicity-weighted gradient area \(\int|\det D^2(RF_{p,q})|\) has size \(\asymp L^6\), while a stationary integral has size \(\asymp L^{-2}\). If lattice aliases populated that image at unit density, absolute summation would have potential capacity \(L^4\), worse than the \(L^2\) primal \((h,k)\)-box. This is not an integer-alias count: injectivity, lattice discrepancy and boundary terms remain unproved. Cancellation across the actual dual aliases is a modulo-one arithmetic problem. The literal gcd factors, sharp double-far gates and slanted symbol remain in that dual amplitude, while (115.10) is constant in \(h,k\) at fixed \(p\). Continuous nondegeneracy alone therefore supplies no estimate.

## 4. First doubtful or unproved step

The first missing step is not a stationary-phase remainder. It is the signed actual-symbol estimate needed **before** the Fejer correlations or Poisson aliases are replaced by absolute values. Concretely, to obtain any fixed-power shortening one would need, for some fixed \(\delta>0\) and \(L\le H\le L^{2-\delta}\), the new local-energy theorem

\[
E_0+2\Re\sum_{1\le r<H}
\left(1-\frac rH\right)\Gamma(r)
\ll_\varepsilon LHX^\varepsilon,
\tag{115.22}
\]

with the two corridor projectors, \(\chi _4(h)\chi _4(h')\), both low-gcd factors, both slanted symbols and all support crossings retained jointly. At \(H=L\), (115.22) asks for \(O(L^2X^\varepsilon)\), while the accepted absolute radial corridor gives \(O(L^3X^\varepsilon)\): this is exactly the missing factor \(L\). Moving to Poisson replaces (115.22) by a cancellation theorem over the nonzero stationary family in (115.18)--(115.21); it does not remove the requirement.

No theorem proving (115.22), no target-sized dual-alias estimate, and no actual-symbol lower bound is established here. This is the first seam. Boundary stationary terms, smoothing/unsmoothing and transform remainders occur later and were therefore not estimated speculatively.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `literal_full_product_to_divisor_pair_identity` | **Pass.** Equations (115.1)--(115.2) open \(c(n)\overline{c(n+r)}\) into the exact two literal divisor sums; \(E_0\) is the full fibre square. |
| `determinant_gate_after_divisor_substitution` | **Pass.** Equation (115.8) retains the gate after \(k=n/h,\ k'=(n+r)/h'\). The determinant corridor is restored exactly once in (115.2), never silently deleted. |
| `increment_chart_and_parity_character` | **Pass.** Equations (115.9)--(115.10) give the exact chart and \((-1)^{p/2}\) character. |
| `gcd_cutoff_and_slanted_symbol_retention` | **Pass.** Both copies remain inside \(a(h,k)\overline{a(h',k')}\) throughout the exact Fejer mechanism. The Poisson discussion is explicitly only a capacity audit where no literal transform theorem is claimed. |
| `inner_vs_outer_cancellation` | **Pass.** No absolute value enters \(\Gamma(r)\), \(\mathfrak D_H\), or the outer signed sum. Absolute values are used only to display the cost of invoking an already accepted corridor owner. |
| `zero_frequency_and_main_term` | **Pass.** The Fejer zero mode is \(E_0\). The zero-frequency Poisson summands remain, but their bulk integrals have no interior critical point; no boundary term is silently deleted. The nonzero stationary bulk families are audited in (115.16)--(115.21). |
| `shift_range_and_conductor_uniformity` | **Pass.** The exact Fejer calculation is uniform for \(1\le K/L\le16\), \(N_B\asymp L^2\), \(R\asymp L^3\), every \(H\), and every active \(|r|\ll L^2\). The B-process diagnostic is restricted to its stated smooth bulk range \(L<r<cL^2\), away from support crossings. No fixed-shift asymptotic is substituted for the growing shift range. |
| `linear_vs_energy_capacity` | **Pass.** Linear target \(L^{3/2}\), energy target \(L^3\), Fejer corridor allowance \(L^4\) at \(H\asymp L\), and the missing linear factor \(L^{1/2}\) are kept distinct. |
| `actual_symbol_vs_phase_adapted_control` | **Pass.** The exact inequality uses the actual symbol, but no actual lower bound is asserted. The accepted phase-adapted control shows why coefficient-uniform improvement of the \(L^4\) budget is false. |
| `double_far_owner_and_corridor_scope` | **Pass.** Radial-first, determinant-second ownership in (115.2) is disjoint. The audit identifies the changed Fejer weights that prevent reusing those owners at unit cost. |
| `fixed_block_and_no_shellwise_l1` | **Pass.** Only one fixed \(B\) occurs. No distinct \(D,L\) block or gcd shell is combined, and no shellwise \(\ell^1\) estimate is imposed. |
| `critical_j1_and_exact_square_j2_boundary` | **Pass.** The argument is only for persistent \(j=1\). The isolated exact-square \(j=2\) boundary and all previous high-gcd, square, near-square and transform-error owners are untouched. |
| `external_theorem_hypothesis_fit` | **Pass by rejection.** [Chamizo](https://doi.org/10.1007/s00009-021-01959-3) treats the complete unweighted coefficient \(r(n)r(n+m)\), not the \(X\)-dependent truncated slanted divisor coefficient, nonlinear radial weight, determinant deletion or growing joint shift sum. [Cowan, Theorem 1.1](https://arxiv.org/html/2304.12572v1) assumes a prime level \(N\), even nontrivial characters \(\chi,\psi\pmod N\) with \(\chi\psi\) nontrivial, nonzero fixed \(u,v\), and all parameters except the cutoff fixed. The \(\chi _4\) self-correlation has conductor \(4\), \(\chi _4\) is odd, \(\chi _4^2\) is principal, the relevant complete specialization would have \(u=v=0\), and the present weight/gates are nonmultiplicative. Neither theorem imports. |
| `downstream_scope` | **Pass.** No balanced packet estimate, \(M9\)-\(M2\), \(M9\), endpoint bound or Gauss-circle exponent follows. |

## 6. Dependencies and exact artifacts used

The derivation used the following permitted artifacts completely:

1. `protocol.md`.
2. `state/proof_obligations.yml`.
3. `state/active_campaign.yml`.
4. `strategy/conductor_0821_full_proof_strategy.md`.
5. `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/briefs/literal_dispersion_attack.md`.
6. `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/derivation_packet.md`.
7. `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/candidates/conductor_shifted_divisor_fork.md`.
8. `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/synthesis.md`.
9. `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/reviews/conductor_round114_energy_and_corridors.md`.
10. `rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/reports/balanced_packet_actual_symbol_formalization.md`.

For the source-fit control only, the primary external sources were Fernando Chamizo, *The Additive Problem for the Number of Representations as a Sum of Two Squares*, Mediterranean Journal of Mathematics 19 (2022), article 44, DOI [10.1007/s00009-021-01959-3](https://doi.org/10.1007/s00009-021-01959-3), and Alex Cowan, *A twisted additive divisor problem*, [arXiv:2304.12572v1](https://arxiv.org/html/2304.12572v1). No external theorem was used in the proof. No numerical experiment or computational proof artifact was used.

## 7. Recommended state effect

**Promote only the scoped no-go; retain the broad actual-energy node as open.** Record that one-step product-variable Fejer dispersion, paid with the accepted Round-114 corridor norms, has no fixed-power target-safe shortening certified by those owners: \(H\le L^{2-\delta}\) amplifies the accepted corridor allowance by \(L^\delta\), while \(H=L^{2-o(1)}\) returns the full power shift range. Record also that the critical outer B-process, the \(p/2\) half-frequency shift, and fixed-\((p,q)\) Hessian nondegeneracy do not by themselves give a power saving; the smooth bulk scalar model exposes potential coefficient-blind \(L^4\) absolute capacity in their nonzero dual families.

Reject the shadows “character zero mode kills the shifted correlation,” “large real Hessian determinant implies discrete cancellation,” “outer B-process automatically shortens the balanced block,” and “Chamizo/Cowan applies after harmless smoothing.” Do **not** reject the literal actual-symbol estimate itself: a new theorem of the form (115.22), or an equivalent signed nonzero-dual cancellation estimate retaining the full symbol and both gates, could still prove it.
