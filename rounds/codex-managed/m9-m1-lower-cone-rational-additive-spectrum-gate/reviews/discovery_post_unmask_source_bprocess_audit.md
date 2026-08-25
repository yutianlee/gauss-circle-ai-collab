# Round 142 cross-review: rational-shift source and B-process audit

## 1. Result

**GREEN.** The repaired report resolves every earlier source and transform seam. The Jutila locations and hypotheses are now exact, the Banerjee–Khurana title is corrected, and the report explicitly states that Jutila's holomorphic-amplitude theorem does not apply to an arbitrary nonzero \(W\in C_c^\infty((1,2))\). It no longer asserts a branchwise Poisson asymptotic or uniform stationary remainder.

The rigorous coefficient-free input is now the separate second-derivative bound
\[
|\mathcal S_{a,q}(M)|
\ll_W\min\!\left\{M^{1/4},RM^{-1/2}+R^{-1}\right\},             \tag{1.1}
\]
uniform in the fractional linear shift. The reciprocal formulas are expressly confined to stationary-principal algebra. The finite \(\chi _4\) identity is stated directly, and the two-step discussion is downgraded to principal-symbol self-return with the first- and second-stage remainders, hard endpoint, and Fresnel transition left unresolved.

The exact rational spectrum, finite Fourier sign, fixed/growing-\(q\) range, stationary constants, and \(R,q\) capacity ledger remain correct. The report continues to distinguish all complete source coefficients from the incomplete moving cone and makes no promotion to the frozen cone scalar.

## 2. Exact statement and hypotheses

Let
\[
e(t)=e^{2\pi it},\qquad
C(m)=\sum_{\substack{hr=m\\r\ {\rm odd}\\r>4h}}\chi _4(r).
\]
For every reduced \(a/q\), \(q\ge1\), and real \(T\ge2\), the repaired report proves
\[
\sum_{m\le T}C(m)e(am/q)
=\gamma(a,q)T+O\!\left((\sqrt T+q)\log(2q)\right),              \tag{2.1}
\]
where
\[
\gamma(a,q)=
\begin{cases}
\dfrac{i\pi}{2q}\chi _4(a),&4\mid q,\\
0,&4\nmid q.
\end{cases}
\]
The main term dominates under the sufficient growing-denominator condition
\[
q\log(2q)=o(\sqrt T).                                           \tag{2.2}
\]
For every positive integer \(m\), with no reducedness requirement on the residues,
\[
C(m)=
\sum_{\substack{q\equiv0\pmod4\\q^2/4<m}}
\frac{2i}{q}\sum_{a\bmod q}\chi _4(a)e(-am/q).                  \tag{2.3}
\]

For \(N\asymp R^4\), \(m\asymp M\), \(W\in C_c^\infty((1,2))\), and \(0\le a<q\), define
\[
\mathcal S_{a,q}(M)
=\sum_{m\ge1}m^{-3/4}W(m/M)e\!\left(\sqrt{Nm}-\frac{am}{q}\right).
\]
The report proves only the rigorous estimate (1.1). It separately defines the stationary principal family
\[
\mathcal P^{\rm stat}_{a,q}(M)
=2e(-1/8)N^{-1/4}
\sum_{\substack{k\in\mathbb Z\\\lambda=k+a/q>0}}
W\!\left(\frac{N}{4M\lambda^2}\right)e\!\left(\frac{N}{4\lambda}\right), \tag{2.4}
\]
and names
\(\mathcal E^{\rm br}_{a,q}=\mathcal S_{a,q}-\mathcal P^{\rm stat}_{a,q}\)
without claiming any bound for it. All later reciprocal identities are explicitly identities or saddle calculations for \(\mathcal P^{\rm stat}\), not asymptotic formulas for \(\mathcal S\).

The corrected source hypotheses and locations are accurate:

- Jutila's Theorem 2.1 begins on printed page 50/PDF page 58 and uses conditions (i)–(v), including holomorphic continuations of both \(f\) and \(g\) to the complex \(\mu\)-tube. The negative-curvature remark is on printed page 59/PDF page 67. The report also records the extra \(U,J\), condition (vi), endpoint-strip factor, and condition (2.1.10) in Theorem 2.2. Theorem 1.1 is on printed page 22/PDF page 30.
- Kaneko's Theorem 3.1 uses a primitive character modulo \(q_0\) and \((h,\ell q_0)=1\); Lemma 3.2 has the strict condition \(\Re\xi>0\); Lemma 3.3 has fixed even entire \(G\), rapid vertical-strip decay, and \(G(0)=1\).
- Banerjee–Khurana's Theorems 4.3–4.4 are on page 11 of *Character Analogues of Cohen-Type Identities and Related Voronoi Summation Formulas* and require an odd primitive character, \(0<\Re\nu<1/2\), nonintegral endpoints, and an analytic test function on a contour neighborhood.

## 3. Proof and audit

For (2.1), the exact row endpoints are
\[
H_T=\left\lfloor\frac{\sqrt{1+16T}-1}{8}\right\rfloor,\qquad
K_h(T)=\left\lfloor\frac{T/h-4h+1}{2}\right\rfloor.
\]
The row begins at \(r=4h+1\), and the combined additive-character and \(\chi _4\) ratio is
\[
z_h=-e(2ah/q).
\]
The row is constant precisely when \(q=4d\) and \(h=d\ell\) with \(\ell\) odd. Its value is
\[
e(ah(4h+1)/q)=i\chi _4(a)\chi _4(\ell).
\]
Using
\[
K_{d\ell}(T)=\frac{T}{2d\ell}-2d\ell+O(1),\qquad
\sum_{\ell\le L}\frac{\chi _4(\ell)}{\ell}=\frac{\pi}{4}+O(L^{-1}),
\]
the constant rows contribute \(i\pi\chi _4(a)T/(2q)+O(\sqrt T)\). For the other rows, \(z_h\) has period \(P=q/(q,2)\), and the reciprocal chord sum over one root set or half-step translate is \(O(P\log(2P))\). Complete periods and one remainder give
\[
O((\sqrt T+q)\log(2q)).
\]
Comparison with \(T/q\) proves (2.2). The constants, signs, strict endpoint, and fixed/growing-\(q\) ledger pass unchanged.

For the finite Fourier coefficient,
\[
\sum_{b\bmod4h}\chi _4(b)e(bm/(4h))
=
\begin{cases}
2ih\,\chi _4(m/h),&h\mid m,\\
0,&h\nmid m.
\end{cases}
\]
Thus the coefficient is initially \(1/(2ih)=-2i/q\), \(q=4h\). Under \(a=-b\), oddness gives \(\chi _4(b)=-\chi _4(a)\), so the frequency reversal produces the positive coefficient \(2i/q\) in (2.3). The condition \(4h^2<m\) becomes exactly \(q^2/4<m\). This sign and endpoint seam passes.

The rigorous branch estimate is correctly separated from the transform algebra. On \(x\asymp M\),
\[
\left|\frac{d^2}{dx^2}\left(\sqrt{Nx}-\frac{ax}{q}\right)\right|
\asymp\frac{R^2}{M^{3/2}},
\]
independently of \(a/q\). The second-derivative estimate for the unweighted exponential sum is
\[
\ll_W RM^{1/4}+\frac{M^{3/4}}{R}.
\]
Partial summation against \(m^{-3/4}W(m/M)\), whose supremum and total variation are \(O_W(M^{-3/4})\), gives
\[
\ll_W RM^{-1/2}+R^{-1}.
\]
Taking the minimum with the trivial \(O_W(M^{1/4})\) estimate proves (1.1). No unproved Poisson remainder is used.

At \(q=4h\), the exact coefficient mass is one per denominator. Summing (1.1) over \(q\ll\sqrt M\), before restoring the separately owned moving-boundary wedge, yields
\[
\ll_W\min\!\left\{M^{3/4},R+\frac{\sqrt M}{R}\right\}.           \tag{3.1}
\]
This is \(O(R)\) on the relevant range and is explicitly only an absolute-capacity bound. For the principal family, the saddle
\[
x_\lambda=\frac{N}{4\lambda^2},\qquad
f_\lambda(x_\lambda)=\frac{N}{4\lambda},\qquad
x_\lambda^{-3/4}|f_\lambda''(x_\lambda)|^{-1/2}=2N^{-1/4}
\]
has negative curvature and factor \(e(-1/8)\). The dual length \(qR^2/\sqrt M\) after numerator aggregation cancels the displayed \(1/q\), leaving capacity \(R/\sqrt M\) per denominator. This agrees with, but is not substituted for, the rigorous bound (3.1).

The corrected second-saddle calculation uses the explicit identity
\[
\chi _4(r)=\frac{e(r/4)-e(3r/4)}{2i}.
\]
For \(\sigma\in\{1,3\}\), \(j=\sigma-4k>0\), the reciprocal phase has
\[
r_{h,j}=2\sqrt{\frac{Nh}{j}},\qquad
\Phi(r_{h,j})=\sqrt{Nhj},\qquad
|\Phi''(r_{h,j})|^{-1/2}=2(Nh)^{1/4}j^{-3/4}.
\]
Positive curvature contributes \(e(+1/8)\), cancelling the first \(e(-1/8)\). The two residue signs reproduce \(\chi _4(j)\), the amplitudes give \((hj)^{-3/4}\), and the formal saddle correspondence \(r<\sqrt N\) is exactly \(j>4h\). The report now calls this only principal-symbol self-return and explicitly withholds both remainders and the endpoint/Fresnel transition. That scope is rigorous.

The source coefficient audit also passes. Jutila's Theorem 1.1 has complete \(d(n)\) and a cosine; Kaneko has complete \(\sigma_\xi(n,\psi)\), two functional-equation directions, and strict \(\Re\xi>0\) in the Ramanujan lemma; Banerjee–Khurana has a complete generalized divisor coefficient and excludes \(\nu=0\). None is applied to the incomplete moving cone \(C(m)\).

## 4. First doubtful or unproved step

There is no doubtful step inside the claims the repaired report asks to retain. The first unavailable source-method assertion would be a uniform branchwise identity
\[
\mathcal S_{a,q}(M)=\mathcal P^{\rm stat}_{a,q}(M)+O_W(1)
\]
for arbitrary nonzero \(W\in C_c^\infty((1,2))\), followed by a second transform uniform through the moving endpoint and Fresnel transition. The report now explicitly states that Jutila does not prove this and makes no such assertion. It retains only the rigorous direct estimate (1.1) for separated branches.

The first substantive mechanism gap is consequently the stated conic reconstruction and local-residual problem: a summation convention preserving the moving cone, a short-interval estimate for the residual after rational-mode subtraction, and signed cancellation after reassembling all denominators, endpoints, and the nonresonant mask. The report correctly leaves these unresolved and treats principal-symbol self-return only as a route diagnosis.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| primary_source_locations_and_title | **GREEN.** Jutila's printed/PDF locations, Jutila Theorem 1.1, Banerjee–Khurana page 11, and the Banerjee–Khurana title are corrected. |
| primary_source_hypotheses | **GREEN.** Jutila conditions (i)–(vi), Theorem 2.2's \(U,J\) and endpoint condition, Kaneko's strict boundary, and Banerjee–Khurana's character, parameter, endpoint, and analyticity assumptions are accurately recorded. |
| jutila_Ccinfinity_applicability | **GREEN.** The report expressly says the holomorphic-amplitude theorem does not cover arbitrary nonzero compactly supported smooth \(W\) and claims no branchwise remainder from it. |
| exact_rational_transform_and_dominance | **GREEN.** The endpoint ledger, coefficient \(i\pi\chi _4(a)/(2q)\), error \(O((\sqrt T+q)\log(2q))\), and sufficient range \(q\log(2q)=o(\sqrt T)\) are correct. |
| finite_chi4_fourier_sign | **GREEN.** The complete sum is \(2ih\chi _4(m/h)\), and frequency reversal gives \(+2i/q\). |
| rigorous_branch_bound_separation | **GREEN.** The second-derivative and partial-summation proof of (1.1) is valid and is kept separate from the named principal family and its unbounded remainder owner. |
| stationary_phase_constants_and_R_q_ledger | **GREEN.** The critical point, reciprocal phase, amplitude \(2N^{-1/4}\), Gaussian unit, dual length, coefficient mass, and owner-sized accumulation are correct. |
| corrected_chi4_reference | **GREEN.** The report states the required character Fourier identity directly and no longer points to the unrelated geometric-sum formula. |
| two_step_return_endpoints_and_remainders | **GREEN.** Only the principal phase, character, amplitude, Gaussian units, and formal \(j>4h\) correspondence are claimed; both uniform remainders and the hard endpoint/Fresnel transition remain explicit owners. |
| complete_versus_incomplete_scope | **GREEN.** Every source theorem remains attached to its complete coefficient and prescribed direction. |
| frozen_cone_scalar_scope | **GREEN.** No cited theorem, capacity bound, or principal-symbol calculation is promoted to the frozen scalar or target estimate. |

No numerical experiment was performed. This re-audit was entirely analytic and source-based.

## 6. Dependencies and exact artifacts used

The re-audit used:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/reports/rational_shift_sqrt_twist_source_audit.md;
- the preceding version of rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/reviews/discovery_post_unmask_source_bprocess_audit.md;
- the Round-142 re-audit assignment and the campaign context already named in the report.

The primary sources checked directly were:

- M. Jutila, *Lectures on a Method in the Theory of Exponential Sums*, Theorems 1.1, 2.1, 2.2 and the negative-curvature remark, https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr80.pdf;
- I. Kaneko, *Mixed Moments of the Riemann Zeta and Dirichlet \(L\)-Functions*, Theorem 3.1 and Lemmas 3.2–3.3, https://arxiv.org/pdf/2109.12495;
- D. Banerjee and K. Khurana, *Character Analogues of Cohen-Type Identities and Related Voronoi Summation Formulas*, Theorems 4.3–4.4, https://arxiv.org/pdf/2306.12399;
- sources/papers/banerjee_khurana_2023.pdf and its local text extraction.

Only this existing review artifact was patched. No audited report, graph, proof draft, shared state, validation, plan, synthesis, or control artifact was edited.

## 7. Recommended state effect

**GREEN: promote with the repaired report's explicit scope.** Candidate auxiliary evidence may include the exact rational-mean lemma and its growing-\(q\) range, the exact finite rational identity, the finite-cutoff and Abel reconstruction identities, the rigorous direct branch bound, and the stationary-principal signs, critical points, amplitudes, \(R,q\) capacity, and formal strict-cone correspondence.

Retain unresolved every branchwise Poisson/stationary remainder for arbitrary \(C_c^\infty\) weights, the second-stage remainder, the hard endpoint/Fresnel transition, the convergent reconstruction preserving the moving cone, the local short-interval residual theorem, full signed denominator cancellation, and the fixed-centre nonresonant cone estimate.

No source theorem or principal-symbol calculation is promoted to the frozen cone scalar, and no downstream proof-state closure follows from this GREEN source audit alone.
