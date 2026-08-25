# Final source audit of the Round 144 conductor candidate

## 1. Result: GREEN after four exact repairs

The mathematical core of
conductor_round144_appell_completion_and_cell_reduction.md is
source-green:

* the level-four Appell normalization and all four \(i/4\)
  theta-times-\(R_{\rm Zw}\) corrections are exact;
* the completed torsion section is genuinely scalar of weight one and
  nebentypus \(\chi _4\) on \(\Gamma _0(4)\), and not scalar on the
  full modular group;
* the \(1/4\) term is the forced infinity-cusp/Appell zero term;
* no harmonic-Maass, coefficient-only Voronoi, cosine, or target-bound
  inference is made;
* the gcd-averaged displacement lemma and the
  \(M^{3/4}\) deletion are valid algebraic owner reductions; and
* the Appell/character-Poisson route is correctly described as an
  owner-complete return to the Round-140 reciprocal scalar.

The candidate is not clean enough to mark GREEN verbatim.  Four exact
repairs are required:

1. replace the two lone carriage-return corruptions in (144.C2) and
   (144.C24) by the literal TeX text \(r\ {\rm odd}\);
2. replace “only one ... is a new analytic reduction” in Section 1 by
   “only one ... is a new algebraic/arithmetic owner reduction”;
3. in (144.C9), restrict the interior stationary family to
   \(0<j<\sqrt N\), and state that \(j=\sqrt N\) belongs to the
   endpoint/Fresnel ledger;
4. in the multiplier proof after (144.C26), display the remaining
   constant exponential
   \(e[-c(d+3b)/4]=1\) before identifying
   \((-1)^{(a-1)/2}=\chi _4(d)\).

After these repairs the verdict is

\[
 \boxed{\mathrm{GREEN}.}
\tag{144.F1}
\]

The repairs do not change the result, capacity ledger, no-go label, or
recommended downstream scope.

## 2. Exact theorem and source-interface audit

### 2.1 Completed Appell source

The candidate's equations (144.C15)--(144.C16) agree exactly with
Bringmann--van Ittersum--Kaszian, equations (2.12)--(2.15), specialized
at

\[
 (\ell,z,w,\sigma)=(4,1/2,-3\tau,2\tau).
\tag{144.F2}
\]

The polar exclusion holds because
\(1/2\notin2\tau\mathbb Z+\mathbb Z\) on \(\mathbb H\).  Pairing the
positive and negative Appell indices gives

\[
 A_4(1/2,-3\tau;2\tau)=\frac12+2F(\tau),
\tag{144.F3}
\]

including the \(n=0\) value \(1/2\).  Halving gives the separate
constant \(1/4\) in (144.C6).

The correction

\[
 \mathcal R_a(\tau)=\frac{i}{4}(-1)^a
 \vartheta\!\left((2a-3)\tau+\frac32;8\tau\right)
 R_{\rm Zw}\!\left(\frac12+(3-2a)\tau;8\tau\right)
\tag{144.F4}
\]

has the correct coefficient, signs, arguments, modulus \(8\tau\), and
range \(0\leq a<4\).  The post-unmask source review proved by an exact
half-index bijection that

\[
 \sum_{a=0}^3\mathcal R_a(\tau)
 =\frac14\sum_{\substack{h,r\in\mathbb Z\\r\ {\rm odd}}}
 \chi _4(r)
 \left[
 E\!\left(\frac{(r-4h)\sqrt{\Im\tau}}2\right)
 -\operatorname {sgn}(r-4h)
 \right]e(hr\tau).
\tag{144.F5}
\]

Thus candidate equation (144.C24) is mathematically exact after its
text corruption is repaired.  There is no omitted holomorphic unary
term.

Semikhatov--Taormina--Tipunin Theorem 1.1 remains the accepted
Round-63 transformed-Appell interface with four Mordell terms.  The
candidate does not reuse that theorem's inapplicable double-cone
expansion, whose annulus hypothesis fails at modulus one.

### 2.2 Direct indefinite-theta and harmonic-Maass scope

The candidate correctly confines direct indefinite-theta language to
the lattice and kernel description.  It does not invoke Zwegers's
Chapter 2 or Westerholt-Raum's cone theorem at the literal isotropic
characteristic, where the required nonintegral-pairing domain fails.
The pole-free Appell completion supplies the lawful regularization.

The sentence

\[
 \text{“real-analytic modular covariance, not }
 \Delta_1\mathcal H=0\text{”}
\tag{144.F6}
\]

is necessary and correct.  The explicit \(\bar\partial\)-image is a
mixed contraction of weight-\(1/2\) and weight-\(3/2\) unary Weil
vectors, not a source-certified scalar holomorphic shadow.  Therefore
the harmonic-Maass summation theorems audited in the source report do
not apply.  The candidate also correctly records that complete-divisor
Voronoi formulas have the wrong coefficient, boundary, or complex
direction.

### 2.3 Source-card promotion scope

The proposed source-audit node in Section 7 is legitimate only with
this wording:

> the cited Appell equations are the external source theorem; the
> scalar \(\Gamma _0(4)\) torsion specialization, error-function
> equality, and \(1/4\) constant are exact derived consequences.

They are not verbatim statements of the cited paper, and they imply no
coefficient estimate.  The existing Round-63 Appell source node must
be retained rather than duplicated.  The \(M^{3/4}\) displacement
lemma belongs in an internal arithmetic-reduction node, not in the
external source card.

## 3. Detailed derivation and owner checks

### 3.1 Scalar multiplier

For
\(\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)
\in\Gamma _0(4)\), the candidate correctly uses

\[
 \widetilde\gamma=
 \begin{pmatrix}a&2b\\c/2&d\end{pmatrix}\in\Gamma(2)
\tag{144.F7}
\]

and the integer shifts

\[
 m_1=\frac c4,\quad r_1=\frac{d-1}{2},\qquad
 m_2=-\frac{3(a-1)}2,\quad r_2=-3b.
\tag{144.F8}
\]

The source elliptic factor is

\[
 (-1)^{m_2}
 e\!\left(\frac{c(c+3a)}4\tau\right),
\tag{144.F9}
\]

and the modular factor is

\[
 (c\tau+d)e\!\left[
 -\frac c4\{(c+3a)\tau+d+3b\}
 \right].
\tag{144.F10}
\]

Their variable exponentials cancel.  The remaining exponential is

\[
 e[-c(d+3b)/4]=1
\tag{144.F11}
\]

because \(4\mid c\), and

\[
 (-1)^{m_2}=(-1)^{(a-1)/2}
 =\chi _4(a)=\chi _4(d).
\tag{144.F12}
\]

This proves (144.C8) with no eta or hidden Weil multiplier.  Repair 4
merely makes the already correct calculation fully visible.  Outside
\(\Gamma _0(4)\), \(c/4\) need not be integral, so the candidate's
full-group vector-valued qualification is correct.

### 3.2 Cusp and boundary wording

The \(1/4\) in (144.C6) is simultaneously the halved Appell zero term
and the regularized infinity-cusp constant.  The sum in (144.F5)
decays exponentially at infinity, so it does not change that constant.
The candidate does not claim that \(F\) itself has a modular constant,
nor does it discard \(1/4\) during transformation.

Its Round-142 wording is also exact: reduced rationals with denominator
divisible by \(4\) form the infinity cusp orbit of \(\Gamma _0(4)\),
but compatibility of the rational residues with this orbit is not a
convergent rational reconstruction.  Denominator-Abel reconstruction
still returns \(r_2/4\), not \(C\), and retains the negative-character
and moving-boundary owners.

### 3.3 Displacement reduction

For nonzero \(j\), the root estimate

\[
 \rho_N(j)\ll_\varepsilon
 N^\varepsilon\sqrt{(N,j)}
\tag{144.F13}
\]

is valid for every prime-power factor of squareful \(N\).  Since the
relevant \(k_m\)-interval has length \(O(N^{3/4})<N\), each residue
root occurs at most once.  The gcd average

\[
 \sum_{1\leq |j|\leq J}\sqrt{(N,j)}
 \ll_\varepsilon JN^\varepsilon
\tag{144.F14}
\]

proves candidate equation (144.C3) for \(0<|j_m|\leq J\).  The
zero-displacement characterization \(N=Du^2\), \(m=Dt^2\), and its
target-safe weighted sum are correct and separate.

Consequently

\[
 M^{-3/4}\#\{m\in\mathcal I_M:
 0<|j_m|\leq M^{3/4}\}
 \ll_\varepsilon X^\varepsilon,
\tag{144.F15}
\]

and summing disjoint blocks proves (144.C4).  Calling this a genuine
arithmetic/algebraic support reduction is exact.  Calling it an
“analytic reduction” risks suggesting a transform estimate and is the
reason for repair 2.  The maximality statement is properly limited to
this root-count-plus-divisor-bound ledger and is not a lower bound
against signed cancellation.

### 3.4 Character-Poisson owner

The exact Round-63 coefficient identity is lawful for
\(w\in C_c^\infty((0,\infty))\) only after the hard cells are restored
globally and a smooth dyadic partition is inserted.  The phase

\[
 \phi_{h,j}(u)=\sqrt{Nu}-\frac{ju}{4h}
\]

has an interior saddle at

\[
 u_0=\frac{4Nh^2}{j^2}
\]

only when \(0<j<\sqrt N\), because the integration begins at
\(u=4h^2\).  At \(j=\sqrt N\), the saddle is the lower endpoint and
belongs to the separately retained endpoint/Fresnel owner; for
\(j>\sqrt N\), there is no interior saddle.  Candidate equation
(144.C9) must therefore read

\[
 e(1/8)N^{-1/4}
 \sum_{\substack{h\geq1\\0<j<\sqrt N}}
 \frac{\chi _4(j)}h
 V_{\rm low}\!\left(\frac{4R^2h^2}{j^2}\right)
 \psi_M\!\left(\frac{4Nh^2}{j^2}\right)e(Nh/j),
\tag{144.F16}
\]

with support crossings and endpoints assigned as already stated.
The amplitude \(2N^{-1/4}/h\) inside the braces, the outer \(i/2\),
and the resulting factor \(e(1/8)N^{-1/4}\) are otherwise exact.

After all half-boundary, subtraction, alias, collar, entry/exit,
profile, endpoint, and remainder owners are restored, (144.F16)
returns the accepted Round-140 reciprocal scalar.  The candidate
correctly forbids a correctionwise or branchwise identification.

## 4. First doubtful or unproved step

After the four repairs, no source or normalization seam remains in the
completed scalar law or cell reduction.  The first genuinely unproved
step is still

\[
 \sum_M\sum_{\substack{m\in\mathcal I_M\\
 |j_m|>M^{3/4}}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 \ll_{\varepsilon,V}X^\varepsilon.
\tag{144.F17}
\]

Neither real-analytic modularity nor the four corrections supplies
this estimate.  Exact coefficient extraction has one completed
pairing minus four correction pairings, and no audited primary theorem
accepts all five owners with the literal square-root test.  The
independent character-Poisson identity gives an equality, but its
owner-complete stationary transform self-returns.

The wider phase-value gap in (144.C4) does not imply derivative
separation: candidate equation (144.C33) is correctly smaller than the
natural derivative-cell width by \(R^{-3}\) and refers only to the
special nearest-square slope.  Thus it cannot be used to delete
arbitrary Farey arcs or improve the reciprocal capacity.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| external_Appell_equations | **GREEN.** The definition, pole condition, completion, elliptic law, and modular law match equations (2.12)--(2.15) of the cited source. |
| four_correction_normalization | **GREEN after text repair.** Equations (144.C7) and (144.C24) are exactly equivalent; both lone carriage returns must be replaced. |
| Gamma0_4_multiplier | **GREEN after explicit seam repair.** The result is correct; add (144.F11) so the constant exponential is not silently omitted. |
| harmonicity_and_summation_disclaimers | **GREEN.** The candidate proves no harmonicity and imports no mismatched harmonic-Maass or complete-divisor estimate. |
| cusp_and_boundary_owner | **GREEN.** The \(1/4\) term is mandatory and Round-142 cusp compatibility is not promoted as reconstruction. |
| displacement_count_and_exact_radicals | **GREEN.** Nonzero gcd averaging and the \(j=0\) squareful channel are exact and separately owned. |
| M_three_quarters_scope | **GREEN after wording repair.** It is an algebraic/arithmetic reduction, not an analytic estimate or lower barrier. |
| stationary_range_and_endpoint | **REPAIR.** Add \(0<j<\sqrt N\) to (144.C9) and retain \(j=\sqrt N\) in the endpoint/Fresnel ledger. |
| individual_complex_direction | **GREEN.** The outer \(i/2\), \(e(1/8)\), and positive direction are exact; no cosine inference occurs. |
| owner_capacity_and_downstream_scope | **GREEN.** The \(M^{1/4}\), top \(R^{1/2}\), and reciprocal \(R\) values are capacities, not signed bounds, and all downstream claims remain open. |
| source_card_promotion | **GREEN with qualification.** Record the scalar law as a derived specialization of the cited equations, not as a verbatim theorem or a new Round-63 Appell identity. |

No numerical evidence was used in this audit.

## 6. Dependencies and exact artifacts used

This audit read in full:

* rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/candidates/conductor_round144_appell_completion_and_cell_reduction.md;
* rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reviews/source_post_unmask_completion_and_summation_audit.md.

The latter carries the exact primary-source audit of:

* Bringmann--van Ittersum--Kaszian, equations (2.12)--(2.15),
  https://arxiv.org/abs/2401.02820;
* Semikhatov--Taormina--Tipunin, definition (1.1), Theorem 1.1, and
  the separate domain of double-cone equation (2.2),
  https://arxiv.org/abs/math/0311314;
* Zwegers, Lemma 1.8 and the failed direct-isotropic domain
  conditions, https://arxiv.org/abs/0807.4834;
* the audited harmonic-Maass and complete-divisor summation sources
  listed in the Round-144 source report.

No graph, campaign, synthesis, validation, plan, proof draft,
candidate, or shared-state file was edited.

## 7. Exact repairs and recommended state effect

Apply these repairs to the conductor candidate before promotion:

1. In (144.C2) and (144.C24), replace each corrupted sequence
   consisting of \(r\ \{\), a lone carriage return, and
   \(m\ {\rm odd}\}\) by \(r\ {\rm odd}\).
2. In the opening paragraph, replace “only one of which is a new
   analytic reduction” by “only one of which is a new
   algebraic/arithmetic owner reduction.”
3. Replace the summation indices \(h,j>0\) in (144.C9) by
   \(h\geq1,\ 0<j<\sqrt N\), and append:
   “The equality \(j=\sqrt N\) is assigned to the endpoint/Fresnel
   ledger; \(j>\sqrt N\) has no interior saddle.”
4. After (144.C26), insert:

   \[
    e[-c(d+3b)/4]=1\qquad(4\mid c),
   \]

   before the character identification.
5. In the source-card action, qualify the new node as a derived scalar
   specialization of the cited completed-Appell equations and retain
   the Round-63 source card without duplication.

With those changes, promote the scalar-completion structural node, the
internal \(M^{3/4}\) cell-reduction node, and the scoped
completion/self-return obstruction exactly as proposed.  Retain
\(\mathsf{indefinite\_theta\_completion\_no\_go}\), leave
(144.C34)--(144.C35) open, and make no downstream theorem or exponent
promotion.
