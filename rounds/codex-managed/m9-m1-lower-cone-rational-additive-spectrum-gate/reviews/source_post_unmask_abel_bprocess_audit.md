# Round 142 source post-unmask audit: Abel reconstruction and B-process

Candidate reviewed: conductor_round142_rational_spectrum_self_return.md

## 1. Result

**GREEN.** All claims audited in the current candidate stand with their stated scope.

For \(\chi=\chi _4\), the Gauss/Möbius identity (142.C19d), the hard-cutoff formula (142.C19e), and the Abel formula (142.C19f) have the correct signs and constants:

\[
\mathcal G_d(m)
=2i\sum_{\ell\mid(d,m)}
\ell\,\mu(d/\ell)\chi(d/\ell)\chi(m/\ell),
\]

\[
P_Q(m)={\pi\over4}\sum_{\ell\mid m}\chi(m/\ell)
\sum_{\substack{k\le Q/(4\ell)\\k\ {\rm odd}}}
{\mu(k)\chi(k)\over k},
\]

and, for \(\eta>0\),

\[
P_\eta(m)
={\pi\over4L(1+\eta,\chi)}
\sum_{\ell\mid m}\chi(m/\ell)\ell^{-\eta}
\longrightarrow
\sigma_\chi(m)={r_2(m)\over4}.
\]

The candidate correctly distinguishes the finite hard cutoff from the denominator-Abel limit. The latter reconstructs the complete divisor coefficient, not the cone coefficient. If \(m=2^\nu n\), \(n\) is odd, and \(\chi(n)=-1\), then \(\sigma_\chi(m)=0\), so the residual \(C-\sigma_\chi\) equals \(C\) on that sector.

The stationary calculations (142.C24)–(142.C27) also pass. The condition \(k-\beta>0\), equivalently \(z=4hk-b>0\), is now explicit. Negative curvature contributes \(e(-1/8)\), the exact principal amplitude is \(2N^{-1/4}\), and multiplication by the finite Fourier coefficient gives

\[
{iN^{-1/4}e(-1/8)\over h}\chi(z).
\]

The dual branch length is \(K_M\asymp R^2/\sqrt M\), so its principal modulus capacity is \(K_M/R\asymp R/\sqrt M\). The \(2h\) branches at fixed height have total coefficient mass \(1\), and summing \(h\ll\sqrt M\) has raw capacity \(R^{1+o(1)}\). The candidate labels this only as capacity, not as a bound or lower bound for the signed scalar. A second stationary step has positive curvature, contributes \(e(+1/8)\), and returns the original square-root phase and character.

This GREEN verdict is confined to the exact coefficient algebra, Abel reconstruction, stationary principal family, power ledger, and the resulting no-go. It does not certify the open fixed-centre estimate or any downstream theorem.

## 2. Exact statement and hypotheses

Let

\[
\chi=\chi _4,\qquad
\tau(\chi)=\sum_{a\bmod4}\chi(a)e(a/4)=2i,\qquad
L(1,\chi)={\pi\over4}.
\]

For integers \(d,m\ge1\), define

\[
\mathcal G_d(m)=
\sum_{\substack{c\bmod4d\\(c,4d)=1}}
\chi(c)e(cm/(4d)).
\]

The hard projection uses

\[
A(a/q)=\mathbf1_{4\mid q}{i\pi\chi(a)\over2q},
\qquad
P_Q(m)=\sum_{\substack{q\le Q\\4\mid q}}
\sum_{a\bmod q}^{*}A(a/q)e(-am/q).
\]

It is a finite identity for every \(Q\ge1\); no convergence assertion is attached to it. The Abel object is separately defined, for fixed \(m\) and \(\eta>0\), by

\[
P_\eta(m)=-{i\pi\over8}
\sum_{d\ge1}{\mathcal G_d(m)\over d^{1+\eta}}.
\]

This series is absolutely convergent for every fixed \(m\) and \(\eta>0\) after (142.C19d) is inserted.

For the B-process, take a fixed smooth weight \(W\) supported on a compact subinterval of \((0,\infty)\), \(N\asymp R^4\), \(x\asymp M\), and

\[
\Phi(x)=\sqrt{Nx},\qquad
\beta={b\over4h},\qquad b\ {\rm odd}.
\]

Poisson frequency \(k\) has a stationary point only when \(k-\beta>0\). Put \(z=4hk-b>0\). The candidate's formula is explicitly the stationary principal family. Hard endpoints, saddle-edge transitions, nonstationary aliases, and stationary remainders remain assigned to the accepted Round-140 owner-complete ledger; they are not silently included in a bare pointwise saddle formula.

The primary-source compatibility checks are:

| Source | Exact relevant hypotheses | Audit use |
|---|---|---|
| I. Kaneko, *Mixed Moments of the Riemann Zeta and Dirichlet \(L\)-Functions*, [Lemma 3.2](https://arxiv.org/pdf/2109.12495) | A character \(\psi\bmod q_0\), \(n\ge1\), and strictly \(\Re\xi>0\); the displayed Ramanujan expansion reconstructs the complete normalized \(\sigma_\xi(n,\psi)\). | With \(q_0=4\), \(\psi=\chi _4\), and \(\xi=\eta>0\), it independently gives the same \(P_\eta\) constant. It does not authorize setting \(\eta=0\) inside an unregularized cone expansion. |
| M. Jutila, *Lectures on a Method in the Theory of Exponential Sums*, [Theorem 2.1 and its negative-curvature remark](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr80.pdf) | The phase and amplitude satisfy the stated analytic scale conditions; positive curvature gives \(e(+1/8)\), while the following remark gives \(e(-1/8)\) for negative curvature. | Confirms the Gaussian units, critical value, and Hessian normalization in (142.C24)–(142.C26). Theorem 2.2 is consistent with retaining smoothing and endpoint terms. It supplies no cancellation among branches. |
| S. Banerjee and R. Khurana, *Voronoï summation formula for the generalized divisor function*, [Theorems 4.3–4.4](https://arxiv.org/pdf/2306.12399) | Odd primitive character, strict \(0<\Re\nu<1/2\), nonintegral endpoints, and the stated analytic test function; the coefficient is complete. | Not used to prove the candidate. Its strict exclusion of \(\nu=0\) and complete coefficient confirm that it cannot replace the elementary boundary calculation for \(C\). |

## 3. Proof or derivation

**Gauss and Möbius constants.** For \(D\ge1\),

\[
\sum_{u\bmod4D}\chi(u)e(um/(4D))
=2iD\,\mathbf1_{D\mid m}\chi(m/D).                              \tag{3.1}
\]

To see this, write \(u=a+4t\), \(a\bmod4\), \(t\bmod D\). The \(t\)-sum vanishes unless \(D\mid m\); when \(m=Dr\), it equals \(D\), and the remaining sum is the primitive Gauss sum

\[
\sum_{a\bmod4}\chi(a)e(ar/4)=\tau(\chi)\chi(r)=2i\chi(r).
\]

Since a unit modulo \(4d\) is odd, Möbius inversion of \((c,d)=1\) may be written

\[
\begin{aligned}
\mathcal G_d(m)
&=\sum_{\substack{k\mid d\\k\ {\rm odd}}}
\mu(k)\sum_{\substack{c\bmod4d\\k\mid c}}
\chi(c)e(cm/(4d))\\
&=2i\sum_{\substack{k\mid d\\d/k\mid m}}
{d\over k}\mu(k)\chi(k)\chi\!\left({m\over d/k}\right).
\end{aligned}
\]

Putting \(\ell=d/k\) gives exactly (142.C19d). Even \(d/\ell\) need not be excluded separately because \(\chi(d/\ell)=0\) there.

**Hard-cutoff normalization.** For \(q=4d\), change \(c=-a\) in the definition of \(P_Q\). Since \(\chi(-c)=-\chi(c)\),

\[
P_Q(m)=-{i\pi\over8}
\sum_{d\le Q/4}{\mathcal G_d(m)\over d}.                         \tag{3.2}
\]

Inserting (142.C19d) gives the constant

\[
\left(-{i\pi\over8}\right)(2i)={\pi\over4}.
\]

Writing \(d=\ell k\) then yields (142.C19e), including the cutoff \(k\le Q/(4\ell)\), the odd-\(k\) condition, and the factor \(1/k\). Thus the hard formula is finite and exact.

**Abel reconstruction.** Insert (142.C19d) into \(P_\eta\), write \(d=\ell k\), and use that \(\ell\mid m\):

\[
\begin{aligned}
P_\eta(m)
&={\pi\over4}
\sum_{\ell\mid m}\chi(m/\ell)\ell^{-\eta}
\sum_{k\ge1}{\mu(k)\chi(k)\over k^{1+\eta}}\\
&={\pi\over4L(1+\eta,\chi)}
\sum_{\ell\mid m}\chi(m/\ell)\ell^{-\eta}.
\end{aligned}                                                     \tag{3.3}
\]

For \(\eta>0\), absolute convergence follows because \(\ell\) ranges over the finite divisors of \(m\) and \(\sum k^{-1-\eta}<\infty\). Letting \(\eta\downarrow0\) in the finite divisor sum and using \(L(1,\chi)=\pi/4\) gives

\[
\lim_{\eta\downarrow0}P_\eta(m)
=\sum_{\ell\mid m}\chi(m/\ell)
=\sum_{d\mid m}\chi(d)
={r_2(m)\over4}.                                                  \tag{3.4}
\]

Kaneko's Lemma 3.2 gives the same check directly:

\[
{\sigma_\eta(m,\chi)\over m^\eta}
={L(1+\eta,\chi)\over\tau(\chi)}
\sum_{d\ge1}{\mathcal G_d(m)\over d^{1+\eta}},
\]

and \(L(1,\chi)/\tau(\chi)=\pi/(8i)=-i\pi/8\).

If \(m=2^\nu n\), \(n\) is odd, and \(\chi(n)=-1\), only odd divisors contribute to (3.4). Pairing \(d\mid n\) with \(n/d\) gives

\[
\chi(n/d)=\chi(n)\chi(d)^{-1}=-\chi(d),
\]

so the pairs cancel. There is no fixed point because \(n\) cannot be a square when \(\chi(n)=-1\). Hence \(\sigma_\chi(m)=0\), and the candidate's negative-character residual statement is exact.

**First stationary transform.** For

\[
f_k(x)=\sqrt{Nx}+(\beta-k)x,
\]

the stationary condition is

\[
f_k'(x)={\sqrt N\over2\sqrt x}+\beta-k=0,
\]

so \(k-\beta>0\) and

\[
x_k={N\over4(k-\beta)^2}
={4Nh^2\over z^2},\qquad
f_k(x_k)={N\over4(k-\beta)}={Nh\over z}.                         \tag{3.5}
\]

Since

\[
f_k''(x)=-{\sqrt N\over4x^{3/2}}<0,
\]

stationary phase contributes \(e(-1/8)\), and

\[
x_k^{-3/4}|f_k''(x_k)|^{-1/2}=2N^{-1/4}.                         \tag{3.6}
\]

The exact Fourier coefficient of the \(b\)-branch in (142.C16) is
\(-i\chi(b)/(2h)\). Since \(z\equiv-b\pmod{4h}\),
\(\chi(z)=-\chi(b)\). Multiplication by (3.6) therefore gives

\[
{-i\chi(b)\over2h}\,2N^{-1/4}e(-1/8)
={iN^{-1/4}e(-1/8)\over h}\chi(z),
\]

which is exactly the corrected coefficient and sign in (142.C26). The transformed weight is

\[
W(x_k/M)=W\!\left({4Nh^2\over Mz^2}\right).
\]

**Second stationary transform.** Summing \(b\bmod4h\) over the odd residues makes \(z\) range once over the positive odd integers. Decompose

\[
\chi(z)={e(z/4)-e(3z/4)\over2i}.
\]

For \(\sigma\in\{1,3\}\) and Poisson integer \(j_0\), put \(j=\sigma-4j_0>0\). The reciprocal phase

\[
{Nh\over z}+\left({\sigma\over4}-j_0\right)z
\]

has

\[
z_{h,j}=2\sqrt{Nh/j},\qquad
\Psi(z_{h,j})=\sqrt{Nhj},\qquad
|\Psi''(z_{h,j})|^{-1/2}=2(Nh)^{1/4}j^{-3/4}.                    \tag{3.7}
\]

Here \(\Psi''>0\), so the Gaussian unit is \(e(+1/8)\), cancelling the first \(e(-1/8)\). The weight becomes \(W(hj/M)\), the two residue classes give \(\chi(j)\), and the amplitude becomes

\[
{iN^{-1/4}\over h}\,{1\over2i}\,2(Nh)^{1/4}j^{-3/4}
=(hj)^{-3/4}.
\]

Thus the stationary principal family returns the original \(\chi(j)(hj)^{-3/4}e(\sqrt{Nhj})\) square-root branch. This is a self-return, not a saving.

The moving cone endpoint is consistent with the same return. The original condition \(x_k>4h^2\) becomes \(z<\sqrt N\) after the first saddle; at \(z_{h,j}=2\sqrt{Nh/j}\), this is exactly \(j>4h\). For a hard cutoff the saddle-edge/Fresnel terms must still be retained, as the candidate explicitly requires.

**The \(q/R\) ledger.** On \(x\asymp M\), the admissible \(k\)-interval has length

\[
K_M\asymp\sqrt{N/M}\asymp {R^2\over\sqrt M}.
\]

Each stationary principal term has size \(N^{-1/4}\asymp R^{-1}\), so one coefficient-free branch has capacity \(K_M/R\asymp R/\sqrt M\). At fixed \(h\), there are \(2h\) odd residues and each exact Fourier coefficient has modulus \(1/(2h)\); their total mass is \(1\). Finally \(h\ll\sqrt M\), giving total principal capacity

\[
\sqrt M\,{R\over\sqrt M}=R.
\]

This verifies (142.C27) and also verifies that the candidate has not manufactured a denominator saving.

## 4. First doubtful or unproved step

There is no surviving doubtful algebraic or source-normalization step in the audited range. The current positivity condition \(k-\beta>0\), exact factor \(N^{-1/4}\), and restriction \(z>0\) make (142.C24)–(142.C26) precise.

The first genuinely unproved step remains cancellation in the fixed-centre signed scalar after all denominators, moving cone endpoints, and the nonresonant mask are assembled. Neither reconstruction route closes it:

* The hard \(P_Q\) is finite and exact, but retains all omitted rational modes and has an owner-sized moving-boundary residual.
* The Abel limit is convergent for \(\eta>0\), but returns \(r_2/4\), while \(C-r_2/4\) leaves the negative-character sector unchanged.
* The B-process is valid for the smooth principal family, but the second transform returns the original square-root branch. Jutila's method supplies the transform, not cancellation in its branch or denominator sum.

The accepted Round-140 ledger is still required for hard endpoints, transition saddles, nonstationary aliases, and remainders. The candidate explicitly retains that qualification, so it does not promote a stationary principal identity into a complete sharp transform.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| primitive_mod_four_gauss_sign | **Pass.** The base Gauss sum is \(2iD\,\mathbf1_{D\mid m}\chi(m/D)\); this fixes the \(+2i\) in (142.C19d). |
| mobius_unit_condition_and_even_terms | **Pass.** Möbius inversion is over odd \(k\mid d\); equivalently, even \(d/\ell\) terms vanish through \(\chi(d/\ell)=0\). |
| hard_projection_frequency_sign | **Pass.** Replacing \(a\) by \(-c\) contributes \(\chi(-c)=-\chi(c)\), and \((-i\pi/8)(2i)=\pi/4\). |
| hard_cutoff_versus_abel_order | **Pass.** (142.C19e) is finite; (142.C19f) is a separately damped, absolutely convergent identity for \(\eta>0\). No hard-cutoff limit is silently asserted. |
| kaneko_ramanujan_normalization | **Pass.** \(\tau(\chi)=2i\) and \(L(1,\chi)/\tau(\chi)=-i\pi/8\), reproducing the candidate's Abel coefficient. |
| complete_divisor_and_negative_character_residual | **Pass.** \(\sigma_\chi=\sum_{d\mid m}\chi(d)=r_2(m)/4\), and it vanishes when the odd part has \(\chi=-1\). |
| first_saddle_domain_phase_and_gaussian | **Pass.** \(k-\beta>0\), \(z>0\), critical value \(Nh/z\), negative curvature, and \(e(-1/8)\) are all correct. |
| stationary_amplitude_and_fourier_sign | **Pass.** The amplitude is exactly \(2N^{-1/4}\); the branch coefficient and \(\chi(z)=-\chi(b)\) give \(+iN^{-1/4}e(-1/8)\chi(z)/h\). |
| second_transform_character_and_return | **Pass.** Positive curvature gives \(e(+1/8)\); the Gaussian units cancel and the original square-root phase, \(\chi_4\), weight, and \((hj)^{-3/4}\) amplitude return. |
| q_and_R_power_ledger | **Pass as capacity.** The dual length is \(R^2/\sqrt M\), one branch costs \(R/\sqrt M\), fixed-height coefficient mass is \(1\), and all heights cost \(R^{1+o(1)}\). |
| source_method_and_endpoint_scope | **Pass.** Kaneko applies only for \(\eta>0\) and to the complete coefficient; Jutila supports the smooth saddle signs and amplitudes; the candidate retains the Round-140 endpoint/remainder owner. |
| capacity_versus_signed_bound | **Pass.** The \(R^{1+o(1)}\) figure is expressly an absolute principal-family capacity, not a signed bound or lower bound. |
| downstream_scope | **Pass.** No complete lower-radial estimate, lower GAR, direct M1 parent, M9-M1, M2 parent, M9-M2, endpoint theorem, M9, bridge, quarter theorem, or exponent change is inferred. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

The local artifacts used were:

* protocol.md;
* state/proof_obligations.yml, specifically the accepted Round-140 far-alias and Round-141 incomplete-fibre/self-return owners;
* state/active_campaign.yml;
* rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/candidates/conductor_round142_rational_spectrum_self_return.md;
* rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/reviews/conductor_round140_height_alias_adjudication.md;
* rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reviews/conductor_round141_incomplete_fibre_adjudication.md.

The primary sources used were:

* Kaneko, Theorem 3.1 and Lemmas 3.2–3.3 ([primary preprint PDF](https://arxiv.org/pdf/2109.12495));
* Jutila, Theorems 2.1–2.2 and the negative-curvature remark ([primary PDF](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr80.pdf));
* Banerjee–Khurana, Theorems 4.3–4.4, checked only to exclude an inapplicable boundary import ([primary preprint PDF](https://arxiv.org/pdf/2306.12399)).

The discovery report was not used. The Gauss sum, Möbius inversion, Abel normalization, divisor cancellation, both stationary transforms, and the complete \(R/q\) ledger were rederived directly. No shared state or candidate file was edited by this review.

## 7. Recommended state effect

**GREEN for promotion of the audited obstruction only.** The conductor may retain (142.C19c)–(142.C19f) as exact coefficient identities and (142.C24)–(142.C27) as the correctly normalized smooth stationary-principal self-return and capacity ledger.

Retain the hard-cutoff/Abel distinction explicitly: a finite projection does not remove the denominator tail, while the canonical Abel reconstruction returns \(r_2/4\), not the moving cone. Retain the strict scope that the B-process statement is principal-family and owner-complete only after the inherited endpoint, transition, and remainder ledger is restored.

The fixed-centre nonresonant scalar remains open. No downstream theorem, owner transfer, signed lower bound, or exponent improvement follows from this GREEN review.
