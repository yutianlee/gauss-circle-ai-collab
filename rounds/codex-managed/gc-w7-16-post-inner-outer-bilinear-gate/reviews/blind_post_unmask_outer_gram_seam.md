# Round 130 post-unmask seam audit: triangular Gram versus literal incidence Gram

## 1. Result

The conductor candidate is **correct after a scope qualification**, not as an unconditional identification of the two Grams.

The matrix

\[
G_{rs}=(1-W|\lambda_r-\lambda_s|)_+
\]

is an exact positive Gram for the complete random-cell triangular kernel. If the fully completed row operator is proved to be exactly \(T=G\), then

\[
\|Tb\|_2^2=b^*G^2b
\]

and the candidate's spectral inequality (130.C7) is exact. The literal post-inner resolved family, however, has incidence map \(H\), fixed input \(\mathbf 1\), and energy

\[
\|H\mathbf 1\|_2^2=\mathbf 1^*H^*H\mathbf 1.
\]

Here \(H^*H\) acts on increment/divisor/threshold labels, while \(G^2\) acts on outer-ray coefficient labels. They are not the same matrix and do not even act on the same space. The candidate's \(G^2\) language is therefore exact only for the completed random-cell operator after a proved connector identifying the completed literal row with \(Gb\). The candidate already gestures at this restriction in the last paragraph of section 3; that caveat must be moved into every claim calling \(G^2\) “the exact dual object.”

The determinant reindexing (130.C1)--(130.C3) is algebraically exact for a fixed primitive ray. Its \(O(1)\) multiplicity conclusion is rigorous on the top shell under the additional geometric hypothesis that the integer \(p\)-support is contained in \(O(1)\) intervals of span \(O(|a|)\). It is not a shell-uniform statement, and it does not count the remaining \(\rho,\eta\), owner, or character branches.

The rigorous no-gos are: no automatic independent-\(p\) saving from dimension counting; no inference of a positive square function from one scalar correlation; and no removal of \(\|G\|\) from (130.C7) without actual-vector information. Top-eigenvector alignment, product-window return, and unit-Hessian return are controls excluding support-only methods, not lower bounds or impossibility theorems for the literal coefficients.

## 2. Exact statements and seam hypotheses

Let

\[
H:\ell^2(\Xi)\longrightarrow \ell^2(\mathscr R),
\qquad F^{\rm res}=H\mathbf 1,
\]

be the literal incidence map of the frozen blind report, where \(\Xi\) consists of the admissible \((p,\rho,\eta)\) labels with all tapers, characters, thresholds, and ownership included in the entries. Its exact energy and scalar forms are

\[
E_{\rm res}=\mathbf 1^*H^*H\mathbf 1,
\qquad
\mathcal O=b^*H\mathbf 1
\tag{S1}
\]

up to the harmless convention conjugating \(b\).

Independently, let \(G:\ell^2(\mathscr R)\to\ell^2(\mathscr R)\) be the candidate's random-cell matrix. It is positive semidefinite: with

\[
\phi_r(t)=W^{1/2}\mathbf 1_{[\lambda_r-1/(2W),\,\lambda_r+1/(2W)]}(t),
\]

one has \(G_{rs}=\langle\phi_s,\phi_r\rangle\). Therefore, for the specifically defined complete operator \(T=G\),

\[
\|Gb\|_2^2=b^*G^*Gb=b^*G^2b,
\qquad
b^*G^2b\le \|G\|\,b^*Gb.
\tag{S2}
\]

The final inequality follows eigenvalue by eigenvalue from \(0\le\lambda^2\le\|G\|\lambda\).

To transfer (S2) to (S1), one needs an explicit vector-level connector

\[
H\mathbf 1=T b.
\tag{S3}
\]

Only when the reassembled literal operator satisfies \(T=G\), after all phase conventions have been absorbed, does its pulled-back ray Gram equal \(G^2\). More generally:

- if one resolved piece is \(T_\nu=P_\nu G\), then its energy is \(b^*G P_\nu^*P_\nu G b\), not \(b^*G^2b\);
- if phases give \(T=D_1GD_2\) with diagonal unitaries, then \(T^*T=D_2^*G^2D_2\), which is spectrally equivalent but not literally \(G^2\) before modulation;
- tapers, character multipliers, half-open owners, or incomplete rows produce the appropriate \(T^*T\), not automatically \(G^2\);
- summing positive energies of pieces gives \(\sum_\nu T_\nu^*T_\nu\), whereas squaring a reassembled signed row gives cross terms as well.

Thus \(G\) is the exact Gram of the random-cell feature functions, \(G^2=T^*T\) is the exact ray-space pullback for \(T=G\), and \(H^*H\) is the exact literal atom-space Gram. Calling any one of these “the Gram” without its domain and connector is ambiguous.

Two smaller qualifications are also needed. First, \(G\) **need not** be a projection; it can be a projection in degenerate separated configurations (for example \(G=I\)), so “positive but not a projection” should read “positive and not generally a projection.” Second, \(\|G\|\) is exactly the spectral capacity. Calling it “precisely a local ray-density capacity” additionally requires a comparison between the operator norm and a stated local weighted ray count; Schur's bound supplies one direction, but equivalence is a separate geometric estimate.

## 3. Proof and determinant-residue derivation

For fixed integers \(a,b\) and \(a'=a+p\), write \(b'=b+q\). Then

\[
n=ab'-a'b=a(b+q)-(a+p)b=aq-bp,
\]

so

\[
q={n+bp\over a},
\qquad
b'={b(a+p)+n\over a},
\qquad
n\equiv-bp\pmod a.
\tag{S4}
\]

This proves (130.C1)--(130.C3), including the displayed transformed phase, whenever \(a\ne0\). If \((a,b)=1\), multiplication by \(-b\) permutes the residue classes modulo \(|a|\), and each \(n\bmod |a|\) selects one residue class \(p\bmod |a|\). For fixed \(n\) and an integer \(p\)-support contained in an interval of length \(\ell\),

\[
\#\{p:n\equiv-bp\pmod a\}\le 1+{\ell\over |a|}.
\tag{S5}
\]

For a union of \(J=O(1)\) intervals, multiply the right side by \(J\). At the top reduced shell \(|a|\asymp L\) and \(\ell=O(L)\), (S5) is \(O(1)\); once \(p\) is fixed, \(q\) is uniquely fixed by (S4).

The assumptions in that conclusion are essential. If \(g=(a,b)>1\), solvability requires \(g\mid n\) and the effective modulus is \(|a|/g\), giving instead

\[
O\!\left(1+{g\ell\over |a|}\right)
\]

possible lifts in one interval. If \(|a|\ll L\) while the \(p\)-span remains \(O(L)\), the primitive bound becomes \(O(1+L/|a|)\), not \(O(1)\). Hence the candidate's multiplicity lemma is a primitive top-shell lemma and must not be propagated to other \(B\)-shells without their own \(|a|\), support-span, and ownership audit.

For fixed \(p\), a literal \(q\)-interval of length \(Q_*\) maps under (S4) to an arithmetic progression of the same cardinality, step \(|a|\), and real span \(\asymp |a|Q_*\). Interlacing the \(p\)-residues preserves the number of \((p,q)\) pairs up to the multiplicity in (S5). The stronger prose that these pairs form “one determinant sequence” of total area \(LQ_*\) additionally requires the \(p\)-dependent \(q\)-intervals to land in a common determinant interval with the asserted endpoint overlap. That follows from the literal determinant-strip geometry only after its half-open endpoints and tapers are written; it is not a consequence of the congruence alone.

Likewise, (S4) does not by itself dispose of auxiliary multiplicities. The labels \(\rho\mid a+p\), \(\eta\), shell owner, and orientation can give several atoms over the same \(n\). They must either be retained in the determinant sequence or bounded separately.

Finally, the character sentence in the candidate is qualitatively sound but not yet an exact character formula. The congruence fixes \(p\) modulo \(a\); a parity twist can require the chosen lift modulo \(2a\), and a quarter character of \(b'\) requires tracking the numerator in (S4) modulo \(4a\), together with branches when \(a\) is even. These remain residue/branch weights rather than a second free long variable, but their conductor and endpoint formula must be stated before using cancellation.

## 4. First doubtful or unproved step

The first seam gap is the promotion from the complete random-cell identity

\[
\mathcal C_i=b^*Gb
\]

to the assertion that completing the literal one-sided determinant rows produces the vector \(Gb\). Defining a model row to be \(Gb\) makes (130.C6) tautologically exact; proving that it is the reassembly of the actual threshold/plateau, character, shell, and orientation pieces is the missing connector (S3). Until that connector is written, the literal target remains \(\mathbf 1^*H^*H\mathbf 1\), and there is no justified equality or order comparison with \(b^*G^2b\).

The next unproved seam is the top-shell support assertion needed for (S5): the candidate needs the actual \(p\)-support to lie in \(O(1)\) intervals of span \(O(|a|)\), not merely to contain \(O(L)\) points. The formulas for the M1/M2 twists after choosing the bounded lift of \(p\) are also required if the residue classes are to be used analytically rather than only as a counting reindexing.

## 5. Controls and rigorous method no-gos

### Rigorous statements

1. **Primitive top-shell collapse.** Under the hypotheses of (S5), \(p\) is a bounded-multiplicity lift of \(n\), so it is not an independent Cartesian long variable. This forbids awarding an automatic second square-root factor from dimension counting. It does not forbid cancellation among the interlaced residue weights.

2. **Scalar versus energy.** One fixed scalar form tests a rank-one projector, while a square energy tests an identity/operator Gram. Therefore the scalar target cannot imply the positive energy without an additional connector or uniformity theorem.

3. **Spectral loss for the completed model.** Conditional on \(T=G\), (S2) is rigorous, and no argument using only positivity can remove \(\|G\|\). A diagonal centre-phase modulation preserves the spectrum. The actual coefficient vector can nevertheless avoid the large eigenspaces, which is exactly the still-open signed possibility.

### Controls only

4. **Top-eigenvector alignment.** Scaling a top eigenvector and undoing the centre phase saturates the ratio in (130.C7) while respecting coefficient upper bounds. This is a coefficient-adversary control. It need not have the literal coefficient profile, full support, or saturated \(\ell^2\) mass, and it is not a lower bound for the actual vector.

5. **Reverse-summation/product window.** The stated \(D^2/L\) return is a method control for the accepted product-window estimate. It becomes a theorem about the literal row only after verifying that its window, taper, characters, and endpoints meet that estimate's hypotheses.

6. **Unit-Hessian sequential return.** A complete unit-Hessian chirp is carried unitarily to another full chirp, so Hessian nondegeneracy alone cannot force contraction. This is rigorous for the canonical complete transform and a falsifying control for generic transform heuristics; it is not a literal-family lower bound unless the exact row is reduced to that normal form with all aliases and boundaries retained.

7. **Capacity conclusion.** These controls prove insufficiency of support, mass, centre phase, and unit-Hessian geometry as isolated inputs. They do not prove failure of an actual M1/M2 residue cancellation theorem.

## 6. Dependencies and audit boundary

- `rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/candidates/conductor_determinant_residue_outer_gram.md`
- `rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/reports/blind_outer_bilinear_dual_feasibility.md`

The audit compares only the candidate's displayed formulas with the frozen incidence-Gram formulation. No shared proof state, sibling report, strategy file, web source, or numerical experiment was used. The candidate's quoted “accepted” product-window and Hessian-return estimates were classified by logical role rather than independently re-proved from undisplayed history.

## 7. Recommended state effect

**Retain with qualification** the determinant algebra (130.C1)--(130.C3), the primitive top-shell bounded-multiplicity lemma, positivity of the triangular random-cell Gram, and the conditional identity \(\|Gb\|_2^2=b^*G^2b\).

**Revise** the candidate's headline and section 3 language to say:

> For the fully completed random-cell operator \(T=G\), the ray-space pullback Gram is \(T^*T=G^2\). For the literal resolved post-inner map \(H\), the exact energy Gram is \(H^*H\); identifying its fixed quadratic value with \(b^*G^2b\) requires a proved completion connector, including all cross-piece, diagonal, taper, character, and ownership terms.

**Scope** the determinant multiplicity to primitive top-shell rays with \(p\)-span \(O(|a|)\), and retain \(\rho,\eta\) and character branches explicitly. **Label** eigenvector alignment, product-window reversal, and unit-Hessian return as controls rather than literal lower bounds. The scalar signed route remains open. No shared-state edit or exponent/M9 promotion is recommended.
