# Round 144 final conductor-candidate audit

## 1. Result

**Verdict: GREEN after five exact local repairs.**  No structural,
constant, owner, capacity, rational-spectrum, or downstream-scope
claim needs to be changed.

The candidate correctly states:

1. the signature-\((1,1)\), level-four lattice and signed odd-coset
   realization of \(C(m)\);
2. the normalization
   \[
   \mathcal H(\tau)=\frac12\widehat A_4(1/2,-3\tau;2\tau)
   =F(\tau)+\frac14+\sum_{a=0}^3\mathcal R_a(\tau);
   \]
3. the scalar law
   \[
   \mathcal H(\gamma\tau)
   =\chi_4(d)(c\tau+d)\mathcal H(\tau)
   \qquad(\gamma\in\Gamma_0(4));
   \]
4. the gcd-averaged nonzero-displacement count
   \(O_\varepsilon(JX^\varepsilon)\), the target-safe threshold
   \(J_M=M^{3/4}\), and the resulting strict arithmetic survivor;
5. the character-Poisson outer factor \(i/2\), saddle unit
   \(e(-1/8)\), and full constant \(e(1/8)N^{-1/4}\);
6. the aggregate, not termwise, return to the accepted Round-140
   reciprocal owner;
7. the \(M^{1/4}\), top \(R^{1/2}\), and reciprocal \(R\) capacity
   ledger; and
8. the Round-142 \(4\mid q\) hierarchy and denominator-Abel return to
   \(r_2/4\), not \(C\).

The five required repairs are:

- In (144.C2) and (144.C24), replace the embedded carriage-return
  corruption in \(r\ {\rm odd}\) by the literal LaTeX
  \(r\ {\rm odd}\).
- Restore the fixed Round-140/141 hypothesis \(0<\rho<1/8\) in the
  exact hypotheses.  Unless the candidate explicitly declares that
  dependence suppressed, write the equivalence errors in (144.C4) and
  (144.C30), and the reciprocal target constant in (144.C35), with
  subscript \((\varepsilon,\rho,V)\).
- After (144.C3), add the total-window statement
  \[
  \#\{m\in\mathcal I_M:|j_m|\leq J\}
  \ll_\varepsilon (J+\sqrt M)X^\varepsilon
  \quad(J\geq0),
  \tag{144.A1}
  \]
  noting that for \(J<1\) the nonzero set is empty and only \(j_m=0\)
  remains.
- In (144.C33), replace the coefficient-free strict sign \(>\) by
  \(\gg_V\):
  \[
  \left|\frac{k_m}{2m}-\frac{\sqrt N}{2\sqrt m}\right|
  \asymp\frac{|j_m|}{m\sqrt{Nm}}
  \gg_V\frac1{R^2M^{3/4}}.
  \tag{144.A2}
  \]
- At the first use of \(L_M\), define
  \(L_M\asymp M^{3/4}/R\), so that
  \(L_M^{-1}\asymp R/M^{3/4}\).

After these repairs the candidate is mathematically green.

## 2. Exact statement and hypotheses

Let \(X\geq2\), and fix the inherited \(0<\rho<1/8\),

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor\asymp R^4,\qquad
 \mathcal I_M=[M,2M)\cap[1,M_*],\qquad M_*\ll_VN^{1/2},
\tag{144.A3}
\]

with disjoint half-open dyadic blocks.  Put

\[
 k_m=\left\lfloor\sqrt{Nm}+\frac12\right\rfloor,\qquad
 j_m=k_m^2-Nm,
\tag{144.A4}
\]

\[
 C(m)=\sum_{\substack{hr=m\\r\ {\rm odd}\\r>4h}}\chi_4(r),
\qquad
 F(\tau)=\sum_{m\geq1}C(m)e(m\tau).
\tag{144.A5}
\]

The lattice in the candidate is

\[
 L_4=\mathbb Z(1,0)\oplus\mathbb Z(0,4),\qquad
 Q(h,r)=hr,\qquad
 \operatorname {Gram}(L_4)=
 \begin{pmatrix}0&4\\4&0\end{pmatrix}.
\tag{144.A6}
\]

Its dual is
\[
 L_4'=\left(\frac14\mathbb Z\right)\times\mathbb Z,
\tag{144.A7}
\]
its discriminant has order \(16\), and its level is exactly \(4\).
The signed combination of the cosets
\((0,1)+L_4\) and \((0,3)+L_4\) is respectively weighted \(+1\) and
\(-1\), hence is exactly \(\chi_4(r)\).

The negative and null vectors are

\[
 c_s=(1,-4),\qquad c_0=(0,-1),
\tag{144.A8}
\]

with
\[
 B(c_s,(h,r))=r-4h,\qquad B(c_0,(h,r))=-h.
\tag{144.A9}
\]

The strict cone is \(h>0,\ r>4h\).  The sloping wall has no odd point;
the isotropic wall is Abel/Appell regularized and supplies the separate
\(1/4\).

The Appell theorem is used only at positive integer level \(4\), for
\(\tau\in\mathbb H\), at the pole-free specialization
\((z,w,\sigma)=(1/2,-3\tau,2\tau)\).  Scalar covariance is asserted
only on \(\Gamma_0(4)\); outside that group the characteristic orbit is
vector-valued.  The coefficient transform is asserted only for
\(w\in C_c^\infty((0,\infty))\), after global mask restoration and
smooth dyadic localization.

## 3. Proof and derivation audit

### 3.1 Lattice, cosets, and completion normalization

The Gram matrix in (144.A6) has eigenvalues of opposite sign, so the
signature is \((1,1)\).  Equations (144.A7) and
\(Q(a/4,b)=ab/4\) show directly that the discriminant order is \(16\)
and the level is \(4\).  The two cosets select \(r\equiv1,3\pmod4\);
their signed difference is \(\chi_4(r)\).

The exact sign-kernel normalization underlying the candidate is

\[
 F(\tau)=\frac14
 \sum_{\substack{h\in\mathbb Z\setminus\{0\}\\r\ {\rm odd}}}
 \chi_4(r)
 \{\operatorname {sgn}(r-4h)+\operatorname {sgn}h\}
 e(hr\tau).
\tag{144.A10}
\]

The two opposite cones contribute equally because both the sign kernel
and \(\chi_4\) change sign under \((h,r)\mapsto(-h,-r)\).
Unfolding the positive cone gives

\[
 F(\tau)=\sum_{h\geq1}
 \frac{e((4h^2+h)\tau)}{1+e(2h\tau)}.
\tag{144.A11}
\]

Pairing the \(n\) and \(-n\) Appell summands and retaining the \(n=0\)
term proves

\[
 A_4(1/2,-3\tau;2\tau)=\frac12+2F(\tau).
\tag{144.A12}
\]

The candidate's four \(i/4\) theta--\(R_{\rm Zw}\) terms therefore
have the right outer normalization.  Their sum equals the single
absolutely convergent error-function correction (144.C24).  The
constant \(1/4\) is separate from those four terms.  No fifth
correction, residue, eta multiplier, or harmonic-Maass conclusion is
missing.

### 3.2 Scalar \(\Gamma_0(4)\) law

For
\(\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)
\in\Gamma_0(4)\),

\[
 \widetilde\gamma=
 \begin{pmatrix}a&2b\\c/2&d\end{pmatrix}\in\Gamma(2).
\tag{144.A13}
\]

The four candidate shifts

\[
 m_1=c/4,\quad r_1=(d-1)/2,\quad
 m_2=-3(a-1)/2,\quad r_2=-3b
\tag{144.A14}
\]

are integers because \(4\mid c\) and \(a,d\) are odd.  Substitution
in the completed Appell elliptic and modular laws cancels every
\(\tau\)-dependent exponential.  The remaining parity factor can be
written either

\[
 (-1)^{m_2}=(-1)^{(a-1)/2}
 =\chi_4(a)=\chi_4(d),
\tag{144.A15}
\]

since \(ad\equiv1\pmod4\).  This proves the candidate's weight-one
scalar law with no residual phase.  When \(4\nmid c\), \(c/4\) is not
an allowed elliptic shift, so the stated full-group limitation is
correct.

### 3.3 Displacement proof

For nonzero \(j\),

\[
 \rho_N(j)=\#\{k\bmod N:k^2\equiv j\pmod N\}
 \ll_\varepsilon N^\varepsilon\sqrt{(N,j)}
\tag{144.A16}
\]

holds uniformly for squareful \(N\).  Reversing the divisor sums gives,
for \(J\geq1\),

\[
\begin{aligned}
 \sum_{1\leq|j|\leq J}\sqrt{(N,j)}
 &\leq2\sum_{d\mid N}\sqrt d
       \left\lfloor\frac{\lfloor J\rfloor}{d}\right\rfloor\\
 &\leq2J\sum_{d\mid N}d^{-1/2}
 \ll_\varepsilon JN^\varepsilon.
\end{aligned}
\tag{144.A17}
\]

On the active range, \(0\leq k_m\ll_VN^{3/4}<N\).  For fixed \(j\),
\[
 m=(k_m^2-j)/N
\tag{144.A18}
\]
makes \(m\mapsto k_m\) injective and lets each residue root occur at
most once.  This proves (144.C3).

For \(j=0\), write \(N=Du^2\) with \(D\) squarefree.  Then
\[
 j_m=0\iff m=Dt^2,
\tag{144.A19}
\]
and the weighted \(t^{-3/2}\) series is globally summable.  On a
single block, the zero-root count is \(O(1+\sqrt M)\), uniformly for
squareful \(N\).  This proves the total count (144.A1), including
\(J<1\).

The half-open dyadic convention assigns each integer to exactly one
block, including the terminal truncation.  A nearest-integer tie is
impossible, since it would give \(4Nm=(2k+1)^2\).  Hence there is no
endpoint or rounding ambiguity.

Multiplication by \(M^{-3/4}|C(m)|\ll
M^{-3/4}X^\varepsilon\) gives

\[
 \ll_{\varepsilon,V}
 (M^{-3/4}J+M^{-1/4})X^\varepsilon.
\tag{144.A20}
\]

The maximal polynomial threshold certified by this absolute method is
\(J=M^{3/4}\).  Summing the disjoint blocks proves (144.C4).  Any
power \(J=M^\beta\) with \(\beta>3/4\) is not certified by this
ledger, but no signed impossibility or lower bound is implied.

### 3.4 Character-Poisson constants

The candidate's exact coefficient formula has the accepted
half-boundary \(1/2\), outer \(i/2\), and subtraction
\(-2w(4h^2)/(\pi i j)\).  Since

\[
 \sum_{j\ne0}\frac{\chi_4(j)}j=\frac\pi2,
\tag{144.A21}
\]

the subtraction contributes \(-\frac12w(4h^2)\) after multiplication
by \(i/2\), cancelling the displayed half-boundary only in the lawful
symmetric recombination.

For
\[
 \phi_{h,j}(u)=\sqrt{Nu}-\frac{ju}{4h},
\]
the positive-\(j\) stationary point satisfies

\[
 u_0=\frac{4Nh^2}{j^2},\qquad
 \phi(u_0)=\frac{Nh}{j},\qquad
 u_0^{-3/4}|\phi''(u_0)|^{-1/2}=2N^{-1/4}.
\tag{144.A22}
\]

Negative curvature gives \(e(-1/8)\).  Thus

\[
 \frac i2\cdot2N^{-1/4}e(-1/8)
 =e(1/8)N^{-1/4},
\tag{144.A23}
\]

exactly as in (144.C9).  There is no missing two, conjugation, or
cosine.

### 3.5 Owner, capacity, rational, and displacement-slope ledgers

The accepted aggregate identity

\[
 \mathcal S_{\rm recip}^+
 =e(-1/8)N^{1/4}\mathcal S_{\rm cone}^+
 +O_{\varepsilon,\rho,V}(RX^\varepsilon)
\tag{144.A24}
\]

inverts to the constant in (144.A23).  This validates the return only
after the half-boundary, subtraction, negative aliases, collar,
entry/exit, profiles, and remainders are reassembled.  The candidate
correctly refuses a termwise identification with the four Appell
corrections.

The strict cone retains block capacity \(M^{1/4+o(1)}\), hence
\(R^{1/2+o(1)}\) at \(M\asymp R^2\).  The normalized reciprocal
stationary family retains absolute capacity \(N^{1/4}=R\).  These are
upper capacities or method costs, not signed lower bounds.

Round 142 is unchanged: the \(4\mid q\) rational hierarchy is
compatible with the scalar cusp orbit, while denominator-Abel
grouping returns \(\sigma_{\chi_4}=r_2/4\), changes the coefficient
owner, and leaves the negative-character sector and moving wedge.

Finally, the slope computation is correct after repair (144.A2).
Because \(m\asymp M\), \(N\asymp R^4\), and
\(|j_m|>M^{3/4}\), the hidden comparison constants preclude the
literal coefficient-one sign \(>\) in (144.C33).  With
\(L_M\asymp M^{3/4}/R\), the separation-to-cell-width ratio is
\(R^{-3}\), and the calculation controls only the induced slope
\(k_m/(2m)\), not arbitrary Farey slopes.

## 4. First doubtful or unproved step

After the local repairs above, there is no doubtful step in the
lattice/coset normalization, completion, scalar multiplier,
displacement reduction, character-Poisson constant, aggregate owner
return, capacity ledger, or Round-142 compatibility.

The first unproved estimate remains exactly (144.C34):

\[
 \sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>M^{3/4}}}
 m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
 \ll_{\varepsilon,V}X^\varepsilon.
\tag{144.A25}
\]

After global restoration and the accepted aggregate equivalence, this
is equivalent to the still-open signed reciprocal estimate
\[
 \mathcal S_{\rm recip}^+\ll_{\varepsilon,\rho,V}RX^\varepsilon
\tag{144.A26}
\]
with every Round-140 owner retained.  Real-analytic modularity,
capacity comparisons, and the larger cell deletion do not prove
either estimate.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| lattice, dual, discriminant, and level | **GREEN.** The hyperbolic lattice has signature \((1,1)\), discriminant order \(16\), and exact level \(4\). |
| signed odd cosets and cone walls | **GREEN.** The \(1/3\bmod4\) cosets have signs \(+/-\); the sloping wall is empty and the null wall supplies the separate Abel/Appell constant. |
| completed Appell normalization | **GREEN.** The bilateral zero term, outer \(1/2\), and four \(i/4\) corrections are exact. |
| scalar \(\Gamma_0(4)\) multiplier | **GREEN.** The shifts are integral, exponentials cancel, and the remaining factor is \(\chi_4(d)\). |
| squareful displacement and \(J<1\) | **GREEN after adding (144.A1).** Nonzero gcd averaging, exact radicals, and the empty nonzero window for \(J<1\) are all controlled. |
| dyadic and nearest-integer endpoints | **GREEN.** Half-open blocks are disjoint and no half-integer tie exists. |
| maximal absolute window | **GREEN.** \(J_M=M^{3/4}\) is the maximal polynomial scale certified by this method, not a signed barrier. |
| character-Poisson constants | **GREEN.** The half-boundary, subtraction, \(i/2\), \(e(-1/8)\), and \(e(1/8)N^{-1/4}\) all match. |
| owner reassembly | **GREEN.** The Round-140 return is aggregate and no Appell-correction or rational-branch termwise claim is made. |
| capacities | **GREEN/no-go.** \(M^{1/4}\), top \(R^{1/2}\), and reciprocal \(R\) are correctly scoped as capacities. |
| Round-142 compatibility | **GREEN/no-go.** The level-four hierarchy is compatible, while Abel returns \(r_2/4\), not \(C\). |
| displacement-slope statement | **GREEN after (144.A2) and the \(L_M\) definition.** The ratio \(R^{-3}\) and arbitrary-slope prohibition are correct. |
| downstream scope | **GREEN.** No lower-GAR, M1/M2, M9, endpoint, bridge, quarter, Li--Yang, internal-\(1/3\), or Gauss-circle exponent is promoted. |

No numerical result is needed or accepted in this audit.

## 6. Dependencies and exact artifacts used

This audit used:

- rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/candidates/conductor_round144_appell_completion_and_cell_reduction.md;
- rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reports/blind_cone_automorphy_feasibility.md;
- rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reports/indefinite_theta_lattice_completion_attack.md;
- rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reviews/discovery_post_unmask_blind_cell_and_completion_audit.md;
- rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reviews/blind_post_unmask_appell_return_and_cell_audit.md;
- rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reviews/source_post_unmask_completion_and_summation_audit.md; and
- the accepted Round-63, Round-140, Round-141, and Round-142 artifacts
  cited by the candidate and seam reviews.

No new external theorem is invoked.  The Appell source hypotheses and
normalizations were already audited in the named source report; this
review checks only their exact specialization and the internal seams.
No state, graph, campaign, synthesis, validation, plan, or proof draft
was edited.

## 7. Recommended state effect

Apply only the five local candidate repairs listed in Section 1.
After those repairs, accept the conductor candidate as **GREEN**.

Retain its proposed state effect:

- promote the scalar completed-Appell specialization without
  duplicating the accepted Round-63 identity;
- strengthen the Round-141 cell reduction from \(\sqrt M\) to
  \(M^{3/4}\) and revise the old summed \(J^{3/2}\) exhaustion;
- record the Appell/character-Poisson reciprocal self-return as an
  aggregate owner obstruction; and
- leave (144.C34)--(144.C35) and every downstream target open.

The repairs do not authorize any downstream exponent or theorem
change.  In particular, the internal \(1/3\), audited Li--Yang,
quarter, and Gauss-circle exponents remain untouched.
