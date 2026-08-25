# 1. Result

**Endpoint--rank--self-return no-go lemma.** The finite character-Poisson transform of the scalar in (140.B2) is exact only as a jointly summed Fourier identity with its hard-endpoint half-weight. It does not furnish a target-scale estimate by taking moduli of aliases: when a literal endpoint sample is nonzero and the row amplitude is smooth up to that endpoint, the individual dual integrals have a harmonic \(1/|k|\) boundary tail and are not absolutely summable. After that boundary tail is kept in its prescribed joint summation, the clean stationary leading family has phase

\[
G(h,r)=\sqrt{Nhr},
\]

whose two-variable Hessian has determinant identically zero and whose terms group exactly by the product \(n=hr\). Its unsigned upper capacity is \(R^{3/2+o(1)}\), whereas the scalar target is \(R X^\varepsilon\). The exact phase-one radical subfamily is \(O_\varepsilon(RX^\varepsilon)\), but no corresponding estimate follows for the near-radical product fibres. Finally, a second stationary/Poisson transform in \(r\) has Legendre phase \(Nh/d\) and therefore returns to the original reciprocal phase. Thus aliaswise modulus, a nondegenerate two-dimensional Hessian estimate, raywise modulus, and a second invertible transform are all rigorously excluded as the missing signed gain.

This is a no-go for those mechanisms, not a counterexample to (140.T). No owner-complete strict survivor of size \(O_\varepsilon(RX^\varepsilon)\) is obtained: a new arithmetic estimate for the truncated product-fibre coefficient, together with uniform bounds for every nonprincipal owner, is still required.

# 2. Exact statement and hypotheses

Put

\[
a_h=L_h+1=\left\lfloor {\rho y\over\sqrt h}\right\rfloor+1,
\qquad D_h=y-a_h,
\]

and retain only literal nonempty rows \(D_h\geq1\). For \(x>0\), set

\[
A_h(x)=V_{\rm low}\!\left({4R^2h^2\over x^2}\right)e(Nh/x),
\]

with the stated zero extension at the left. The exact finite Poisson formula below is understood in the Cesàro sense (equivalently, under the usual bounded-variation hypotheses, by the corresponding symmetric Fourier limit). This is the minimal regularity needed to interpret sharp finite-interval Poisson summation; the rank, product-fibre, and self-return conclusions are algebraic and do not require differentiability. The displayed large-alias asymptotic additionally assumes \(A_h\in C^2[0,D_h]\) after its zero extension. If the fixed profile is only piecewise smooth, every internal jump must be added as a separate boundary owner. Constants may depend on the fixed profile and on \(\rho\).

For each \(\tau\in\{+1,-1\}\), define

\[
I_{h,r}=\int_0^{D_h}A_h(x)e(rx/4)\,dx,
\qquad r=\tau-4k,\quad k\in\mathbb Z.
\]

Then the exact owner-complete identity is

\[
\mathcal S_N^+
=E_N+{1\over2i}\sum_{\tau=\pm1}\tau
 \sum_{\substack{h\ge1\\D_h\ge1}}{1\over h}
 \sum_{k\in\mathbb Z}^{(C)} I_{h,\tau-4k},
\tag{A}
\]

where

\[
E_N={1\over2}\sum_{\substack{h\ge1\\D_h\ge1}}{1\over h}
 \chi_4(D_h)V_{\rm low}\!\left({4R^2h^2\over D_h^2}\right)
 e(Nh/D_h).
\tag{B}
\]

The support implication in the frozen statement makes the effective height range \(h\ll R\). Hence, for a bounded fixed profile,

\[
|E_N|\ll \sum_{h\ll R}{1\over h}\ll\log(2R)
\ll_\varepsilon RX^\varepsilon.
\tag{C}
\]

Both residue branches occur in (A), every odd \(r\) occurs exactly once, and its branch sign is \(\tau=\chi_4(r)\). The negative scalar is the complex conjugate of (A), so every conclusion holds for both signs without a second argument.

# 3. Proof or derivation

For a fixed nonempty row, Poisson summation of the zero-extended function on \([0,D_h]\) gives the interior lattice samples with weight one and the sample at \(D_h\) with weight \(1/2\). Adding the missing half of that last sample and then using

\[
\chi_4(d)={1\over2i}\sum_{\tau=\pm1}\tau e(\tau d/4)
\]

proves (A)--(B). Empty rows contribute nothing. The stipulated support implication gives \(h\ll d/R\le y/R\le R\), proving (C).

The hard endpoint cannot be forgotten inside the dual sum. Under the \(C^2\) hypothesis just stated, two integrations by parts along either residue branch give

\[
I_{h,r}={2A_h(D_h)e(rD_h/4)\over \pi i r}+O_h(r^{-2})
\qquad (|r|\longrightarrow\infty).
\tag{D}
\]

Thus \(\sum_k|I_{h,\tau-4k}|=\infty\) whenever \(A_h(D_h)\ne0\). A literal internal profile jump produces an additional \(1/r\) boundary harmonic and must be retained as well. Formula (A) is nevertheless exact because the boundary harmonics are summed with the same Fourier convention as the half-endpoint term. Consequently an aliaswise absolute bound for all nonstationary modes is not an admissible owner estimate; one must first collect the boundary harmonics or smooth and compensate the cutoff exactly.

For \(r>0\),

\[
\phi'_{h,r}(x)=-{Nh\over x^2}+{r\over4},\qquad
\phi''_{h,r}(x)={2Nh\over x^3},
\]

so the unique stationary point is \(x_*=2\sqrt{Nh/r}\). It lies at or before the hard endpoint exactly when \(rD_h^2\ge4Nh\). Writing \(r=4h+s\), and using \(D_h=y-a_h\), this is

\[
s\ge T_h:={4h(2a_hy-a_h^2+q)\over(y-a_h)^2}.
\tag{E}
\]

To audit the floor and \(q\), write

\[
a_h={\rho y\over\sqrt h}+\theta_h,\quad0<\theta_h\le1,
\qquad \alpha_h={a_h\over y},\quad \delta={q\over y^2}\in[0,2/y].
\]

Then, exactly,

\[
T_h=4h{2\alpha_h-\alpha_h^2+\delta\over(1-\alpha_h)^2}.
\tag{F}
\]

For the effective range \(h\ll R\asymp\sqrt y\), uniformly in \(0\le q\le2y\), Taylor expansion on \(0\le\alpha_h\le1/4\) yields

\[
T_h={8\rho\sqrt h-4\rho^2\over(1-\rho/\sqrt h)^2}
     +O_\rho(h/y)\asymp_\rho\sqrt h.
\tag{G}
\]

The two extreme centres differ by the exact amount

\[
T_h(q=2y)-T_h(q=0)={8hy\over(y-a_h)^2}\ll h/y.
\tag{H}
\]

Equality in (E) is an endpoint stationary point and belongs to the incomplete-Fresnel owner, not to a clean full-Gaussian principal term.

At a clean interior stationary point,

\[
{4R^2h^2\over x_*^2}={R^2hr\over N},\qquad
\phi_{h,r}(x_*)=\sqrt{Nhr},\qquad
\phi''_{h,r}(x_*)={r^{3/2}\over4(Nh)^{1/2}}.
\]

The formal full-Gaussian contribution of \(I_{h,r}\) is therefore

\[
2e(1/8)(Nh)^{1/4}r^{-3/4}
V_{\rm low}(R^2hr/N)e(\sqrt{Nhr}).
\]

After the actual \(h^{-1}\) weight and branch coefficient are restored, the unavoidable clean principal model is

\[
\mathcal P=e(-1/8)N^{1/4}
 \sum_{\substack{h\ge1,\ r>0\ {\rm odd}\\rD_h^2>4Nh}}
 \chi_4(r)(hr)^{-3/4}V_{\rm low}(R^2hr/N)e(\sqrt{Nhr}),
\tag{I}
\]

with any chosen safety margin, entry/exit transition, profile crossing, and stationary remainder still owned separately. Equation (I) is a model extracted from (A), not an asserted replacement for it.

Grouping (I) by \(n=hr\) gives exactly

\[
\mathcal P=e(-1/8)N^{1/4}\sum_{n\ge1}n^{-3/4}
 V_{\rm low}(R^2n/N)e(\sqrt{Nn})\,\mathcal A_N(n),
\tag{J}
\]

where

\[
\mathcal A_N(n)=
 \sum_{\substack{hr=n,\ r\ {\rm odd}\\rD_h^2>4Nh}}\chi_4(r)
\]

(with the same clean-interior mask if a margin is imposed). The profile support gives \(n\ll N/R^2\ll R^2\), and \(|\mathcal A_N(n)|\le d(n)\). Hence the absolute estimate from (J) is only

\[
|\mathcal P|\ll_\varepsilon
R\sum_{n\ll R^2}n^{-3/4+\varepsilon}
\ll_\varepsilon R^{3/2}X^\varepsilon,
\tag{K}
\]

which misses (140.T) by \(R^{1/2}\). This capacity gap is real for the unsigned/adversarial analogue: if the fixed nonzero profile is bounded away from zero on any compact subinterval of its support, the \(h=1\), \(r\asymp R^2\) clean terms alone have total leading modulus \(\asymp R^{3/2}\); unit coefficients chosen to cancel their phases attain that size. Hence no estimate using only support, amplitude size, or the Hessian can give the target uniformly in bounded coefficients. The actual \(\chi_4(r)\) and its interaction with the radical phase and exact height cutoff must be used. Even \(\chi_4\) does not repair the estimate merely fibrewise: without the height cutoff the complete fibre coefficient is

\[
\sum_{\substack{r\mid n\\r\ {\rm odd}}}\chi_4(r)\ge0.
\tag{L}
\]

Indeed it is multiplicative; a prime \(p\equiv1\pmod4\) contributes \(v_p(n)+1\), while a prime \(p\equiv3\pmod4\) contributes \(1\) for even valuation and \(0\) for odd valuation. The exact height cutoff truncates this divisor sum and supplies no automatic cancellation theorem.

The exact radical channel is target-safe. Write \(N=\nu b^2\) with \(\nu\) squarefree. The condition \(Nn\) square is equivalent to \(n=\nu t^2\), and therefore

\[
N^{1/4}\sum_{\substack{n\ll R^2\\Nn=\square}}
n^{-3/4}d(n)
\ll_\varepsilon RX^\varepsilon.
\tag{M}
\]

This includes \(q=0\), and in particular an odd fourth power \(X=m^4\), for which \(N=m^4\), \(y=m^2\), and the radical products are precisely the squares. Formula (M) is uniform also at \(q=2y\). It gives no bound for the union of near-radical fibres.

Finally,

\[
\det \nabla^2G(h,r)=0,
\qquad \nabla^2G(h,r)(h,r)^{\mathsf T}=0.
\tag{N}
\]

On the rational ray \(h=v\ell,\ r=u\ell\), the phase is \(G=\ell\sqrt{Nuv}\); it is identically integral when \(Nuv\) is a square. Thus the missing \(R^{1/2}\) cannot be attributed to nondegenerate two-dimensional curvature. Nor can it come from repeating the transform: the stationary equation for the opposite Fourier kernel is

\[
{\partial G\over\partial r}={1\over2}\sqrt{Nh/r}={d\over4},
\qquad r_*={4Nh\over d^2},
\]

and its Legendre phase is

\[
G(h,r_*)-{r_*d\over4}={Nh\over d}.
\tag{O}
\]

The mod-four Fourier factor also returns, since

\[
\sum_{\tau=\pm1}\tau e(\tau d/4)=2i\chi_4(d).
\]

Thus a second complete transform is an exact self-return, not a signed estimate.

# 4. First doubtful or unproved step

The first false step in a proposed direct joint argument would be an invocation of a nondegenerate two-dimensional Hessian theorem for \(G(h,r)\): (N) violates its hypothesis identically. Before any principal-only argument, there is also an owner seam that has not been proved: one must turn (A), with its conditionally summed boundary harmonics, into (I) plus an \(O_\varepsilon(RX^\varepsilon)\) total of nonstationary modes, endpoint-entry incomplete-Fresnel terms, profile crossings, and stationary remainders.

Even granting that owner lemma, (140.T) would require the new signed product-fibre estimate

\[
\sum_{n\ll R^2}n^{-3/4}V_{\rm low}(R^2n/N)
\mathcal A_N(n)e(\sqrt{Nn})\ll_\varepsilon X^\varepsilon
\tag{P}
\]

uniformly in every floor, \(0\le q\le2y\), and the clean/transition partition. Neither Hessian curvature, exact radicals, the divisor bound, nor transform inversion proves (P). Near radicals and truncated product fibres are therefore the first genuine signed-cancellation gap after the exact owner seam.

# 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| exact_tail_cutoff_floor_empty_rows_and_both_signs | Pass. Empty rows are omitted literally, \(D_h=y-a_h\) is never smoothed, (E)--(H) retain the floor and all \(q\), and the negative sign is the conjugate of (A). |
| mod_four_character_poisson_branches | Pass. Both \(\tau=\pm1\) occur; together they parameterize every odd \(r\) once, with coefficient \(\chi_4(r)\). |
| hard_endpoint_half_weight_and_zero_extension | Pass as an ownership check. The half endpoint is (B); (D) proves that raw aliaswise modulus is invalid when a literal boundary sample is nonzero. |
| stationary_entry_offset_s_exact_floor_q_ledger | Pass. (E)--(H) are exact before the uniform \(\asymp_\rho\sqrt h\) conclusion. |
| profile_stationary_entry_exit_and_crossings | Not discarded. Equality in (E), stationary entry/exit, and every profile crossing remain transition owners outside the clean model (I). |
| nonstationary_transition_and_remainder_owner_ledger | Open, and this is stated rather than hidden. Formula (A) owns all \(r\le0\), positive pre-entry aliases, conditional boundary tails, transitions, and remainders; no \(O(RX^\varepsilon)\) aggregate is claimed. |
| joint_phase_Hessian_rank_and_rational_rays | Obstruction proved by (N) and the ray formula \(G(v\ell,u\ell)=\ell\sqrt{Nuv}\). |
| product_fibre_exact_and_near_radical_controls | Exact products are grouped in (J); complete character fibres can be nonnegative by (L); radicals satisfy (M); near radicals remain unproved. |
| height_weight_dyadic_capacity_and_target_return | The original triangle capacity is \(\ll y\log X\), and the clean stationary upper capacity is (K), \(R^{3/2+o(1)}\). All conclusions are returned to the scalar target \(R X^\varepsilon\), never to a square. |
| fourth_power_q_zero_and_q_max_controls | Pass for the cutoff ledger by (H) and for radicals by (M). Odd fourth powers give the maximally coherent \(q=0\) square case but still only \(O(RX^\varepsilon)\) exact-radical mass; \(q=2y\) changes entry by \(O(h/y)\). |
| transform_noninvertibility_and_self_return | Obstruction proved. The exact transform is Fourier-invertible, and its second stationary Legendre transform is exactly (O), the starting reciprocal phase. |
| round138_residual_directionality_and_downstream_scope | Pass. No tail-square identity, residual deletion, lower GAR, blockwise theorem, M9-M1/M9-M2 statement, endpoint-uniformity theorem, M9 conclusion, quarter theorem, or exponent improvement is inferred. |

No numerical experiment or web source was used; the allocation was entirely analytical.

# 6. Dependencies and exact artifacts used

The derivation used only the following artifacts:

- protocol.md;
- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/blind_statement.md;
- rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/briefs/blind_height_alias_joint_feasibility.md.

No proof-state file, proof draft, Round-138 or Round-139 derivation/review, sibling report, computation, or external source was inspected. Equations (A)--(P) were derived independently from the frozen scalar and transform coordinates.

# 7. Recommended state effect

**Retain the obstruction and revise the proposed mechanism; do not promote (140.T).** Record that a sharp finite character-Poisson transform must be kept in a joint Fourier summation because of its endpoint \(1/r\) tail; that the clean height-alias phase is rank one and product-fibred; that exact radicals are target-safe but near radicals are not controlled; and that a second transform self-returns. A later candidate can change the state only by proving both the owner-complete reduction of (A) to a target-safe remainder plus a signed survivor and a uniform arithmetic estimate of the form (P). This report recommends no downstream state change.
