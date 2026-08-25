# Round 147 source seam review of the conductor candidate

## 1. Result and verdict

**Verdict: `revise`, with no rejection of the central scoped no-go.** Equations (147.C13)--(147.C23), (147.C25)--(147.C27), and (147.C30)--(147.C31) have the correct coefficient orientation, conductor, scalar, pole, and fixed-order kernel. Equation (147.C24) also has the correct convergence domain, but the proof printed after it is incomplete: the displayed

\[
 \mathscr K_p=1+a^2b+ab^2+O((|a|+|b|)^4)
\]

does not by itself prove absolute convergence throughout

\[
 \Re w>\frac{1+|\Re z|}{3},\qquad |\Re z|<\frac12,
\]

because the undifferentiated \(O((|a|+|b|)^4)\) bound permits pure fourth powers whose absolute convergence is not implied near \(|\Re z|=1/2\). This is the **first overstated derivation** in equation order. The conclusion is repaired by the exact mixed-monomial identity

\[
 \boxed{
 \mathscr K_p
 =\frac{1+a+b}{(1+a)(1+b)(1-ab)}
 =1+\frac{a^2b+ab^2+a^2b^2}
 {(1+a)(1+b)(1-ab)}.}
\tag{147.R1}
\]

Every numerator monomial in (147.R1) contains both \(a\) and \(b\). On a closed sub-half-plane of the claimed region, the denominators are uniformly separated from zero, and

\[
 |\mathscr K_p-1|
 \ll p^{-(3\Re w-|\Re z|)}+p^{-4\Re w},
\tag{147.R2}
\]

which is prime-summable exactly under (147.C24). Thus (147.C24) is true, but its current proof must be replaced or supplemented before promotion.

Two further source-seam clarifications are mandatory. First, (147.C28) is correct, but \(z=0\) is outside the strict Banerjee--Khurana strip; it must be presented as a direct \(z=0\) Mellin-functional-equation derivation, or accompanied by a locally uniform analytic-continuation argument. Second, the infinite \(k\)-version (147.C29) needs its ordering/convergence sentence made quantitative. For \(k>2M\), the primal sum is zero and the polar and dual scalars cancel, while

\[
 \sum_{k>2M}|h_z(k)|k^{\Re z-1}
 \ll_\varepsilon M^{-1/2+2\Re z+\varepsilon}
\tag{147.R3}
\]

for \(0<\Re z<1/4\). Equation (147.R3) makes the outer tail summable as an iterated series. Without this convention, (147.C29) should instead be written first with \(k\le2M\).

These are repairable proof-presentation seams. They do not change the conductor-four centre \(m=kN\), the growing-order caveat, the squarefree-\(H\) triangle loss, the reciprocal-zero warning, or the absence of any exponent improvement.

## 2. Exact audited statement and hypotheses

The source-level statement that survives audit is the following.

Let

\[
 A_z(n)=\sum_{de=n}\chi _4(e)(e/d)^z,
 \qquad B_z(n)=\mu^2(n)A_z(n),
\]

and take \(z=c+iv\) with \(0<c<1/4\). For each fixed \(z\) and \(F\in C_c^\infty(0,\infty)\),

\[
\begin{aligned}
 \sum_{n\ge1}A_z(n)F(n)
 ={}&L(1-2z,\chi _4)\int_0^\infty F(x)x^{-z}\,dx\\
 &+\pi4^z\sum_{m\ge1}A_{-z}(m)
 \int_0^\infty F(x)\mathscr B_{2z}(2\pi\sqrt{mx})\,dx,
\end{aligned}
\tag{147.R4}
\]

where

\[
 \mathscr B_\nu(y)=
 \left(\frac2\pi K_\nu(y)-Y_\nu(y)\right)
 \sin\frac{\pi\nu}{2}+J_\nu(y)\cos\frac{\pi\nu}{2}.
\tag{147.R5}
\]

The primary theorem itself assumes an analytic test on a finite interval, nonintegral endpoints, and \(0<\Re(2z)<1/2\). Formula (147.R4) for compact-smooth \(F\) is a fixed-\(z\) derivation from Mellin inversion and the completed functional equation, not a theorem quoted verbatim from that source. It has no growing-\(|v|\) estimate.

The coefficient identity is

\[
 \sum_{n\ge1}B_z(n)n^{-w}
 =H(w,z)\zeta(w+z)L(w-z,\chi _4),
 \qquad B_z=h_z*A_z,
\tag{147.R6}
\]

with the external cone-ratio scalar \(4^{-z}\) retained outside. At \(2\),

\[
 H_2=1-2^{-2w-2z},
\]

and the exact quadratic refactorization is

\[
 H(w,z)=\frac{\mathscr K(w,z)}
 {\zeta(2w+2z)\zeta(2w-2z)L(2w,\chi _4)}.
\tag{147.R7}
\]

Equation (147.R7) is initially an identity in the common absolute-convergence region. Its continuation below \(\Re w=1/2+|c|\) is meromorphic; no residue-free contour displacement follows from it.

## 3. Equation-by-equation hostile audit

| Candidate equation | Verdict | Audit |
|---|---|---|
| C13 | **Pass.** | Since \(\mu^2(de)=\mu^2(n)\) for \(de=n\), and \(\chi _4(e)=0\) for even \(e\), \(B_z(n)=\mu^2(n)A_z(n)\) is the exact pre-cone squarefree/parity coefficient. |
| C14 | **Pass.** | \(A_z(n)=n^z\bar\sigma_{-2z,\chi _4}(n)\), so the Dirichlet series is \(\zeta(w+z)L(w-z,\chi _4)\). |
| C15 | **Pass.** | Primewise multiplication gives \(B_z=h_z*A_z\). The coefficient identity is finite at each integer and therefore survives outside the initial common half-plane. |
| C16 | **Pass.** | At \(2\), oddness of \(e\) leaves \(1+2^{-w-z}\); division by the local \(\zeta(w+z)\) factor gives \(1-2^{-2w-2z}\). |
| C17 | **Pass.** | Direct expansion of \((1+a+b)(1-a)(1-b)\) gives the displayed polynomial with the stated signs. |
| C18 | **Pass.** | The quadratic terms require \(\Re(w\pm z)>1/2\), and these inequalities also control \(ab\) and the cubic terms. This is absolute convergence of the \(H\) Euler product/Dirichlet series, not physical \(\ell^1\). |
| C19 | **Pass.** | The \(p^2\) and \(p^3\) coefficients, including \(p=2\), follow exactly from C16--C17; no higher local exponent occurs in \(H_p\). |
| C20 | **Pass.** | The local bounds imply \(|h_z(k)|\ll k^{|c|+\varepsilon}\), uniformly in \(v\), and the exponent-\(2/3\) support has powerful-number count \(O(K^{1/2+\varepsilon})\). |
| C21 | **Algebra pass; proof-use warning.** | The expansion is correct, but its generic \(O((|a|+|b|)^4)\) remainder is too coarse to prove C24 over the whole stated \(c\)-range. Use (147.R1). |
| C22 | **Pass.** | The extra \(p=2\) local factor from \(\zeta(2w-2z)^{-1}\) is canceled exactly by \((1-2^{-2w+2z})^{-1}\); \(L(2w,\chi _4)\) has no Euler factor at \(2\). |
| C23 | **Pass.** | Odd and even local factors match (147.R7). The equality is first absolute in \(\Re w>1/2+|c|\). |
| C24 | **Revise proof; conclusion passes.** | This is the first overstated step. The stated domain follows from (147.R1)--(147.R2), not from the printed undifferentiated fourth-order remainder. |
| C25 | **Pass only as a method limitation.** | Reciprocals of the three \(L\)-factors may have poles at their zeros unless \(\mathscr K\) cancels them. A contour must avoid or account for them. This is not proof that a pole occurs at any specified point and not an impossibility theorem for the coefficient sum. |
| C26 | **Pass.** | This is exactly the Theorem-4.3 \(J/Y/K\) combination for an odd primitive character. |
| C27 | **Pass at fixed \(z\), with provenance retained.** | Taking \(q=4\), \(\nu=2z\), \(f(x)=x^{z+1}F(x)\), and \(\tau(\chi _4)=2i\) gives \(-2\pi i\tau(\chi _4)4^{z-1}=\pi4^z\). The argument is \(2\pi\sqrt{mx}\), and the only Dirichlet-series pole is \(w=1-z\). The \(C_c^\infty\) version is derived, not source-stated. |
| C28 | **Formula passes; attribution must be tightened.** | At \(z=0\), \(A_0=r_2/4\), \(L(1,\chi _4)=\pi/4\), and \(\mathscr B_0=J_0\), so the constants are correct. Because the primary theorem's strip is strict, cite a direct \(z=0\) Mellin derivation or prove local uniform continuation before saying it “yields” C28. The claim of a separate independent derivation is not verifiable from this review's permitted dependencies. |
| C29 | **Pass after an ordering/convergence clarification.** | Applying C27 to \(F(k\cdot)\) gives the displayed \(k^{z-1}\) polar scaling and \(1/k\) dual scaling. The all-\(k\) display is legal as an iterated series after (147.R3); otherwise retain \(k\le2M\) and its finite polar sum. |
| C30 | **Pass.** | Both changes of variable \(u=kx\) are exact and introduce no omitted \(z\)-power in the dual integral. |
| C31 | **Pass as a formal near-resonance control, not as a theorem.** | On a cone-boundary box \(D\ll\sqrt M\), the smoothed bandwidth gives \(|z|^2\ll DX^\varepsilon\), hence the displayed ratio is \(O(N^{-1/2}X^\varepsilon)\) after renaming \(\varepsilon\). It proves neither uniform complex-order asymptotics nor the small/transition/off-resonant estimates. |

The fixed-order large-argument phase from C26 is

\[
 \left(\frac2{\pi y}\right)^{1/2}\cos(y-\pi/4),
\]

so at conductor four the branches are \(e(\pm\sqrt{mx})\). After scaling by \(k\), the negative branch resonates against \(e(+\sqrt{Nu})\) at \(m=kN\). Thus the candidate's conductor, branch direction, centre, and width ledger are consistent with C26--C30.

## 4. First doubtful or unproved step

The first overstatement is the proof of (147.C24), not its conclusion. The printed \(O((|a|+|b|)^4)\) expansion is insufficient to control a putative pure \(b^4\) term when \(c>0\) is close to \(1/2\), since C24 alone would not force \(4(\Re w-c)>1\). Exact cancellation of all pure powers is essential and is exposed by (147.R1). This repair is algebraic and does not alter any later power.

The first genuinely open source hypothesis remains the one already stated after (147.C29): no audited theorem gives the needed Bessel expansion, all derivatives, and summable remainders uniformly for

\[
 |Im z|\lesssim D^{1/2}X^\varepsilon
\]

through every small-, transition-, and large-argument range and every moving prefix. The favorable quantity (147.C31) controls only the resonant large-argument formal parameter.

Granting that missing analytic theorem, the signed \(H\)-resonance correlation remains open. Neither (147.C18), (147.C24), nor disjoint dual windows supplies physical cancellation. The reciprocal-zero observation in (147.C25) is lawful only in its cautious form: it blocks an unowned contour argument but proves neither that \(\mathscr K\) fails to cancel a particular zero nor that the target estimate is impossible.

## 5. Control outcomes and required corrections

| Control | Outcome |
|---|---|
| Fixed-\(z\) compact-smooth extension | **Pass as a derivation, not as a quoted theorem.** Keep \(0<\Re z<1/4\), rapid Mellin decay, and fixed-parameter dependence explicit. |
| Scalar and conductor | **Pass.** The scalar is \(\pi4^z\); the kernel argument is \(2\pi\sqrt{mx}\), hence the unscaled centre is \(m=N\). |
| Pole ledger | **Pass.** There is one pole from \(\zeta(w+z)\) at \(w=1-z\); the primitive nonprincipal \(L(w-z,\chi _4)\) is entire. |
| \(p=2\) and odd Euler factors | **Pass.** C16--C19 and C22 have the correct local normalizations. |
| \(H\)-convolution scaling | **Pass after adding (147.R3) or retaining a finite \(k\)-sum.** No missing \(k^z\) occurs in the dual branch. |
| Every Bessel branch | **Pass at fixed order.** The \(J/Y\) combination contains both oscillatory signs; \(K\) is retained. Growing-order transition and derivative bounds stay open. |
| Quadratic refactorization | **Revise proof.** Insert (147.R1)--(147.R2); do not infer C24 from the coarse fourth-order remainder alone. |
| Reciprocal-zero inference | **Pass as scoped obstruction.** Continue to say “possible poles” and “unowned residues”; do not promote this to a pole-existence or impossibility claim. |
| \(z=0\) control | **Correction required.** Attribute C28 to a direct functional-equation derivation or prove the boundary continuation; the strict primary theorem does not state it. |
| Growing-order estimate | **Open.** No candidate equation through C31 closes it. |
| Downstream scope | **Pass.** No target, M1/M2 parent, M9, bridge, or exponent change follows. |

Required candidate corrections are therefore:

1. insert the exact local identity (147.R1) and use it to prove (147.C24);
2. state the legal derivation/provenance for the boundary formula (147.C28);
3. add the quantitative outer-tail convergence (147.R3) to (147.C29), or retain the finite physical \(k\)-sum before separating polar and dual pieces;
4. preserve the current fixed-order and reciprocal-zero caveats without strengthening either into a theorem.

## 6. Dependencies and artifacts used

Only the permitted seam-review dependencies were used:

- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/candidates/conductor_round147_t1_squarefree_voronoi_and_H_no_go.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/reports/complex_order_voronoi_source_audit.md`;
- `sources/banerjee_khurana_2023.md`.

The primary source card identifies Banerjee--Khurana equation (5.11) and Theorems 4.3--4.4, with analytic finite-interval testing, nonintegral endpoints, \(0<\Re\nu<1/2\), kernel argument \(4\pi\sqrt{nt/q}\), and fixed-parameter rather than growing-order scope. No additional theorem or numerical experiment was used.

## 7. Recommended state effect

**Recommended effect: `revise`; do not promote the conductor candidate as written.** After the three local corrections above, the fixed-\(z\) coefficient/Euler/Voronoi reduction and the scoped absolute-aggregation no-go are eligible for the ordinary remaining seam reviews. The repairs do not supply the missing growing-order theorem or signed \(H\)-correlation, do not prove the \(t=1\) target, and do not alter the internally proved \(1/3\) exponent.

Retain the label `squarefree_H_resonance_no_go` only as a method-specific obstruction: fixed-channel Voronoi plus modulus, unowned reciprocal-factor contour shifting, and literal squarefree expansion of the bare reciprocal phase fail to reach the target. It is not a signed lower bound and not an impossibility theorem for a future joint-correlation argument. Make no shared-state, proof-draft, downstream-owner, or exponent change from this review alone.
