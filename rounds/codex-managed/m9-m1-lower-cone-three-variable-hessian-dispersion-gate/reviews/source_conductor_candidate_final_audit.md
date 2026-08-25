# Round 146 final source/power review of the conductor candidate

- Candidate reviewed: `candidates/conductor_round146_three_variable_unmasking_and_dispersion_no_go.md`
- Review role: final primary-source and power auditor
- Verdict: `revise_then_promote_scoped_no_go`

## 1. Result

The central source and power conclusion is correct: the favorable Cao--Zhai Theorem-6 placement is legal for the phase and scale but illegal for the literal coefficient, and even an ideal coefficient separation leaves the first source term

\[
 R^{3/8-5\tau/8},
\]

hence \(R^{1/16}\) at the formal \(\tau=1/2\) endpoint. All fourteen exponents in (146.C30) are correct. The Robert--Sargos and Sargos--Wu comparison powers are also correct, and the stationary-transform discussion is correctly limited to a phase-level self-return.

The candidate should nevertheless be revised before graph promotion. Four corrections are required:

1. complete the theorem cards with the exact hypotheses and mappings recorded below;
2. replace the current one-sentence treatment of Cao--Zhai Theorem 7 by its exact coefficient mismatch and the independent \(R^{7/8}\) well-defined term, while leaving only its printed final term source-inconclusive;
3. make (146.C25) an explicitly idealized capacity diagnostic unless a bounding-box lattice count is supplied;
4. repair the formal/non-source seams at (146.C1), (146.C7), and (146.C33): define \(\mathfrak T_N\) and \(k_m\), and do not call the isolated \(t=1\) estimate logically necessary for the full signed sum.

After those edits, the candidate is suitable only as a scoped theorem-interface and displayed-upper-bound no-go. It is not an impossibility theorem for the exact scalar.

## 2. Exact statements and hypotheses

### 2.1 Cao--Zhai Theorem 6

The primary source is X. Cao and W. Zhai, [*Multiple exponential sums with monomials*, Acta Arith. 92 (2000), 195--213, Theorem 6, pp. 211--212](https://matwbn.icm.edu.pl/ksiazki/aa/aa92/aa9231.pdf). It considers

\[
 S_I(M_0,M_1,M_2)=
 \sum_{m\sim M_0}\sum_{m_1\sim M_1}\sum_{m_2\sim M_2}
 a(m)b(m_1,m_2)e(A m^\alpha m_1^\beta m_2^\gamma)
\]

under all of

\[
\begin{gathered}
 M_0,M_1,M_2\geq1,\qquad A\neq0,\qquad
 |a(m)|\leq1,\quad |b(m_1,m_2)|\leq1,\\
 \alpha(\alpha-1)(\alpha-2)(\alpha-3)
 \gamma(\gamma-1)\neq0,\\
 F=|A|M_0^\alpha M_1^\beta M_2^\gamma\gg M_0.
\end{gathered}
\]

There is no restriction on \(\beta\). The candidate currently gives the exponent and \(F\)-conditions but should add \(A\neq0\), the three side-length conditions, and the coefficient bounds.

Up to \(d\leftrightarrow e\), the only legal phase placement is exactly

\[
 (m,m_1,m_2)=(d,t,e),\qquad
 (\alpha,\beta,\gamma)=\left(\frac12,1,\frac12\right),\qquad
 (M_0,M_1,M_2)=(D,T,E),\qquad A=\sqrt N.
\]

The linear \(t\)-exponent cannot occupy the \(\alpha\)- or \(\gamma\)-slot. Here

\[
 F=\sqrt N\,D^{1/2}TE^{1/2}=\sqrt{NM}.
\]

The candidate should explicitly verify \(F\gg D\): from \(D\ll M/T^2\), \(M\ll_VR^2\), and \(\sqrt N\asymp R^2\), one has \(\sqrt{NM}/D\gg_V1\). Thus phase, dimension, fixed center, individual complex direction, and scale pass; the single-tensor condition \(a(d)b(t,e)\) fails.

### 2.2 Cao--Zhai Theorem 7

The same primary source's Theorem 7 treats

\[
 \sum a(m_1)b(m_2)e(A m^\alpha m_1^\beta m_2^\gamma)
\]

with \(M_0,M_1,M_2\geq1\), \(A>0\), bounded \(a(m_1),b(m_2)\), and

\[
 \frac{\alpha\beta}{\alpha-1}\notin\{0,1,2,\ldots\}.
\]

The same placement gives \(\alpha\beta/(\alpha-1)=-1\), so its phase condition passes. Its amplitude has no coefficient in the distinguished \(d\)-variable and requires the remainder to split as \(a(t)b(e)\); the literal coefficient therefore fails even more strongly. Independently, its second well-defined displayed term is

\[
 (F^4T^7E^7)^{1/8},
\]

which becomes \(R^{7/8}\) after the top balanced \(R^{-3/2}\) normalization, independently of \(\tau\). The source's final printed term contains undefined \(N,H\); only that final term is source-inconclusive. The candidate's current statement that Theorem 7 is simply “not used” is too weak to support the claimed audit of all direct source routes.

### 2.3 Robert--Sargos Theorem 1

O. Robert and P. Sargos, [*Three-dimensional exponential sums with monomials*, J. reine angew. Math. 591 (2006), 1--20, Theorem 1](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf), assume positive integer \(H,N_0,M_0\), \(\mathcal X>1\), bounded coefficients \(a(h,n),b(m)\), and

\[
 \alpha(\alpha-1)\beta\gamma\neq0.
\]

The exact placement is

\[
 (h,n,m)=(t,e,d),\quad
 (\beta,\gamma,\alpha)=\left(1,\frac12,\frac12\right),\quad
 (H,N_0,M_0)=(T,E,D),\quad \mathcal X=F.
\]

It accepts only \(a(t,e)b(d)\), not the literal coefficient.

### 2.4 Sargos--Wu Theorem 9

P. Sargos and J. Wu, [*Multiple exponential sums with monomials and their applications in number theory*, Acta Math. Hungar. 87 (2000), 333--354, Theorem 9](https://doi.org/10.1023/A:1006777803163), require \(Z>0\), separated bounded coefficients \(a_m b_n\), and

\[
 \alpha\beta(\alpha-1)(\beta-1)(\alpha-2)(\beta-2)\neq0.
\]

After freezing \(t\), the exact mapping is

\[
 (m,n)=(d,e),\qquad
 (\alpha,\beta)=\left(\frac12,\frac12\right),\qquad
 (M_1,N_1)=(D,E),\qquad Z=F.
\]

The exponent condition passes, but the fixed-\(t\) coprimality and cone coefficient is not separated.

### 2.5 Sargos's multidimensional transform

P. Sargos, [*The multidimensional van der Corput transformation*, Functiones et Approximatio 52.1 (2015), 133--176, Section 5.1, Theorem 5.2 and Proposition 5.2](https://doi.org/10.7169/facm/2015.52.1.11), assumes fixed \(p>1\), \(k>p+5\), \(\mathcal T,M_i>1\), a connected bounded open \(\Omega\), \(f\in C^k(\Omega,\mathbb R)\), \(\chi\in C_c^k(\Omega,\mathbb C)\), uniform derivative bounds, support separated from \(\Omega^c\), \(|\det H_f|\geq\delta>0\), and injective \(f'\). Proposition 5.2 adds its geometric-boundary Fourier factor and norm. It does not accept an arithmetic coefficient.

For \(p=3\), normalized \(f(x,y,z)=x\sqrt{yz}\), and \((M_1,M_2,M_3)=(T,D,E)\), the smooth positive-box phase hypotheses pass; the length-one faces and literal amplitude do not.

## 3. Proof and power verification

The complete recomputation of (146.C30) is:

| term | exponent after \(R^{-3/2}\) | value at \(\tau=1/2\) |
|---:|---:|---:|
| 1 | \(3/8-5\tau/8\) | \(1/16\) |
| 2 | \(3/8-\tau\) | \(-1/8\) |
| 3 | \(11/29-43\tau/58\) | \(1/116\) |
| 4 | \(41/108-41\tau/54\) | \(0\) |
| 5 | \(37/98-37\tau/49\) | \(0\) |
| 6 | \(11/29-23\tau/29\) | \(-1/58\) |
| 7 | \(127/336-125\tau/168\) | \(1/168\) |
| 8 | \(115/304-115\tau/152\) | \(0\) |
| 9 | \(127/336-131\tau/168\) | \(-1/84\) |
| 10 | \(33/100-181\tau/200\) | \(-49/400\) |
| 11 | \(123/368-167\tau/184\) | \(-11/92\) |
| 12 | \(33/100-19\tau/20\) | \(-29/200\) |
| 13 | \(1/3-5\tau/6\) | \(-1/12\) |
| 14 | \(1/4-9\tau/8\) | \(-5/16\) |

Thus all fourteen entries in the candidate are correct. This recomputation holds the placement \((m,m_1,m_2)=(d,t,e)\) fixed across the entire fourteen-term bound; termwise swapping \(d,e\) is not legal. On an unbalanced box, choosing the larger of \(D,E\) as the distinguished side minimizes term 1 alone and must be done before evaluating the full fixed-placement ledger. In particular,

\[
 R^{-3/2}(F D^5T^7E^7)^{1/8}
 =R^{3/8-5\tau/8}.
\]

This term becomes \(O(1)\) only at \(\tau\geq3/5\), outside the small-\(t\) range. At \(\tau=1/2\), terms 1, 3, and 7 remain positive. Therefore the displayed Cao--Zhai bound itself is not target-sized anywhere in a new fixed-power \(\tau<1/2\) balanced corridor; at the endpoint it still carries \(R^{1/16}\), although that terminal layer is already safe by the separate trivial estimate.

For Robert--Sargos, its first displayed contribution under the mapping in Section 2.3 gives

\[
 R^{-3/2}(TED)
 \left(\frac{F}{TED^2}\right)^{1/4}
 =R^{1/2-\tau/2},
\]

hence \(R^{1/4}\) at \(\tau=1/2\).

For Sargos--Wu, summing fixed-\(t\) rows trivially, its sixth displayed contribution gives

\[
 R^{-3/2}T(F^2D^7E^6)^{1/10}
 =R^{2/5-3\tau/10},
\]

again \(R^{1/4}\) at \(\tau=1/2\). The candidate's two comparison powers are exact.

The algebra in (146.C23)--(146.C26) is also correct:

\[
 (t_*,d_*,e_*)=
 \left(\frac{2\sqrt{vw}}c,\frac uc\sqrt{\frac wv},
 \frac uc\sqrt{\frac vw}\right),\qquad
 g^*(u,v,w)=-\frac{2u\sqrt{vw}}c.
\]

This proves only monomial phase self-return, not amplitude self-return.

## 4. First doubtful or unproved step

The first source-applicability failure is exactly the coefficient tensor. The literal amplitude contains \(\mu^2(de)\), \((d,e)=1\), \(\gamma\mid t\), \((\gamma,de)=1\), \(ab=t/\gamma\), \(eb^2>4da^2\), \(\chi_4(\gamma e)\), the product staircase, profile, and clipped endpoints. None is covered by a single \(a(d)b(t,e)\), \(a(t,e)b(d)\), or \(a(d)b(e)\) source tensor, nor by Sargos's smooth amplitude. A bounded-norm superposition owning every boundary would be a new lemma.

The candidate correctly grants this missing separation before invoking the independent power obstruction. Its no-go language is calibrated correctly in Sections 1 and 5: a positive term in a published upper bound proves only that this displayed estimate does not deliver the target. It does not prove that the actual sum is large.

Two non-source qualifications are required:

1. In (146.C25), \(\asymp F^3/V_3\) is introduced as an ideal smooth-interior volume and then used to assert an “upper price.” Either downgrade the conclusion to an idealized capacity diagnostic, or add the elementary supported bounding-box count
   \[
   \#\{\text{aliases}\}\ll
   (1+F/T)(1+F/D)(1+F/E)
   \ll F^3/V_3
   \]
   in the regime where all three dual lengths exceed \(1\). In either version, state again that the source transform is inapplicable to the literal arithmetic amplitude.
2. The sentence before (146.C33), “Already the \(t=1\) face requires,” is logically too strong for the full signed scalar: cancellation between \(t=1\) and \(t\geq2\) is not excluded. Replace it by: “Any route that estimates \(t\)-layers separately must in particular prove the following prefix-uniform \(t=1\) estimate.” The displayed estimate is a valid standalone open slice and a necessary obligation only for such layerwise routes.

There are also two formal repairs: assign \(\mathfrak T_N\) explicitly to the sum in (146.C1), and define

\[
 k_m=\left\lfloor\sqrt{Nm}+\frac12\right\rfloor
\]

before using it in (146.C7), noting \(k_m=k_{s,t}\) when \(m=st^2\). The global assembly after the per-block (146.C8) should mention the absorbable \(O(\log X)\) block count. At the endpoint discussion, \(t^2de=B_M\) is the excluded upper boundary of the current half-open block, not an active product layer in that block.

## 5. Required controls and outcomes

| control | outcome |
|---|---|
| Primary links resolve to the primary paper, author manuscript, publisher DOI, or primary preprint | **Pass** |
| Cao--Zhai Theorem-6 legal variable placement | **Pass** |
| Cao--Zhai Theorem-6 exact hypothesis card | **Revise:** add \(A\neq0\), side lengths, and coefficient bounds |
| Cao--Zhai fourteen-term exponent ledger | **Pass:** all fourteen entries and endpoint values recomputed |
| Cao--Zhai term-1 conclusion | **Pass:** \(R^{3/8-5\tau/8}\), \(R^{1/16}\) at \(\tau=1/2\) |
| Cao--Zhai Theorem-7 screen | **Revise:** record the coefficient failure and the independent \(R^{7/8}\) second term; only the last printed term is inconclusive |
| Robert--Sargos mapping and power | **Pass**, with exact hypotheses to be added |
| Sargos--Wu mapping and power | **Pass**, with exact hypotheses to be added |
| Multidimensional \(B\)-process | **Pass as a phase-only diagnostic; revise alias-count wording** |
| Literal coefficient mismatch | **Pass** |
| Fixed center and individual \(e(+f)\) direction | **Pass** |
| No-go calibration | **Pass:** mechanism-level obstruction only |
| Exact unmasking seam | **Pass**, subject to the two symbol definitions and explicit dyadic assembly noted above |
| Short-face control | **Pass as an adverse slice; revise the necessity claim for (146.C33)** |

## 6. Dependencies and exact artifacts used

This review used only the conductor candidate and the already completed Round-146 primary-source audit:

- `candidates/conductor_round146_three_variable_unmasking_and_dispersion_no_go.md`;
- `reports/multidimensional_monomial_source_audit.md`.

The exact source cards were checked against the primary links listed in Section 2. No title or abstract was used in place of a theorem statement. The fourteen exponents and the Robert--Sargos/Sargos--Wu normalizations were recomputed algebraically.

## 7. Recommended state effect

**Revise, then promote only the scoped reductions.** The exact unmasking reduction may be promoted after the notation repairs. The three-variable result may be promoted only as:

- a literal coefficient-class mismatch;
- a displayed-upper-bound power obstruction for Cao--Zhai Theorems 6--7 and the stated Robert--Sargos/Sargos--Wu uses;
- a short-face and phase-level transform diagnostic.

Do not promote a lower bound, an impossibility theorem for all sign-sensitive methods, a standalone necessity of (146.C33), or any downstream target/exponent change.
