# Round 109 statement-only blind owner-completion rederivation

## 1. Result: sharp abstract completion lemma and statement-level no-go

The supplied information does **not** imply the desired owner norm

\[
 \sum_{B,\nu}|O_{B,\nu}|\ll_\varepsilon L^2X^\varepsilon.
\]

The first unsupported implication is the passage from a signed aggregate, a row-energy estimate, or positivity of a full Gram form to the outside-absolute norm of the literal block-owner scalars.  This failure already has two-block finite countermodels satisfying (109.1), (109.2), exact one-count ownership, and disjoint owner atoms.

There is nevertheless a sharp abstract lemma.  Exact one-count ownership gives the algebraic completion.  The weakest norm needed merely to transfer an outer block \(\ell^1\) estimate is

\[
 D:=\sum_B\left|\sum_\nu O_{B,\nu}\right|\ll_\varepsilon L^2X^\varepsilon.
\]

The stronger quantity

\[
 C_{\rm own}:=\sum_{B,\nu}|O_{B,\nu}|
\]

is exactly the cost of inserting and subtracting every literal owner separately.  Thus (109.3) is sufficient for block transfer and is necessary for the specifically requested *ownerwise* outside-absolute completion, but it is not necessary for block transfer if different owners cancel inside a block.  From the permitted context one cannot identify a named literal owner as an actual obstruction: no literal owner formula or norm estimate is supplied.  The rigorous conclusion is an underdetermination/no-go for the proposed norm upgrade, not a counterexample to any actual M2 symbol.

## 2. Exact statement and hypotheses

Let \(\mathcal B\) and \(\mathcal O\) be finite, let \(S=\mathcal B\times\mathcal O\), and let \(\mathcal I\) be the finite set of literal scalar atoms removed from the hard expansion.  Assume:

1. **One-count ownership.**  There is a map \(\pi:\mathcal I\to S\); every atom occurs in exactly one fibre of \(\pi\), and no other copy of that atom is charged elsewhere.  If \(a_i\in\mathbb C\) is the complete oriented amplitude of atom \(i\), then
   \[
   O_{B,\nu}=\sum_{\pi(i)=(B,\nu)}a_i.
   \]
   The amplitude \(a_i\) includes all signs, smooth weights, and metric density.  No density is removed by the lemma.
2. **Exact scalar identity.**  With
   \[
   \Delta_B:=\sum_\nu O_{B,\nu},
   \qquad q^{\rm h}_B=q^{\rm f}_B-\Delta_B,
   \]
   the vectors \(q^{\rm h}\) and \(q^{\rm f}\) are the hard and fixed-lattice completed oriented scalar block sums.
3. **Uniformity.**  Any asserted majorant below is uniform in the stated ranges \(J=X^{1/2}\), \(1\leq L\leq J^{1/2}\), and in every dyadic/orientation parameter being summed.

For a target \(H>0\), define

\[
 A_{\rm sig}:=\left|\sum_{B,\nu}O_{B,\nu}\right|,
 \quad
 D:=\sum_B|\Delta_B|,
 \quad
 C_{\rm own}:=\sum_{B,\nu}|O_{B,\nu}|.
\]

Then the following completion lemma holds.

**(a) Norm hierarchy.**  One always has
\[
 A_{\rm sig}\leq D\leq C_{\rm own}.
\]
Neither reverse inequality holds with a dimension-free constant.

**(b) Minimal block-transfer criterion.**  The translation estimate
\[
 \|z-\Delta\|_{\ell^1(\mathcal B)}
 \leq \|z\|_{\ell^1(\mathcal B)}+H
 \quad\hbox{for every }z\in\mathbb C^{\mathcal B}
\]
holds if and only if \(D\leq H\).  Consequently,
\[
 \|q^{\rm h}\|_1\leq \|q^{\rm f}\|_1+D.
\]

**(c) Literal-owner criterion.**  Every owner can be inserted and subtracted separately at total outside-absolute cost \(H\) if and only if \(C_{\rm own}\leq H\).  Equivalently, there are nonnegative numbers \(M_{B,\nu}\) such that
\[
 |O_{B,\nu}|\leq M_{B,\nu},
 \qquad \sum_{B,\nu}M_{B,\nu}\leq H.
\]
A practical familywise sufficient hypothesis is
\[
 \sum_B|O_{B,\nu}|\leq H_\nu
 \quad(\nu\in\mathcal O),
 \qquad \sum_\nu H_\nu\leq H.
\]

**(d) Absolutely summable separation is norm-preserving, not norm-creating.**  If
\[
 O_{B,\nu}=\sum_t\lambda_t O^{(t)}_{B,\nu}
\]
with absolute convergence, then
\[
 C_{\rm own}(O)
 \leq \sum_t|\lambda_t|C_{\rm own}(O^{(t)}).
\]
Thus bounded Fourier \(L^1\)-cost or absolutely summable weighted Möbius inversion safely preserves a previously proved owner \(\ell^1\) estimate.  Such separation alone does not turn a signed or energy estimate into (109.3).

**(e) Exact energy conversion requirement.**  If, for owner slots \(s\in S\),
\[
 O_s=\langle x_s,u_s\rangle_{\mathcal H_s},
 \qquad \sum_s\|x_s\|^2\leq A,
\]
then
\[
 C_{\rm own}\leq
 A^{1/2}\left(\sum_s\|u_s\|^2\right)^{1/2}.
\]
Hence a row-energy estimate is sufficient only after the row-summation mass \(\sum_s\|u_s\|^2\) is written and the displayed product is shown to be \(O(H)\).

**(f) Exact Gram conversion requirement.**  Suppose a positive form \(G\succeq0\) obeys \(c^*Gc\leq A\), while owner scalars are \(O_s=c^*G_sc\).  A sufficient hypothesis is the numerical-radius domination
\[
 |c^*G_sc|\leq w_s\,c^*Gc
 \quad\hbox{for all admissible }c,
 \qquad A\sum_s w_s\leq H.
\]
Positivity of \(G\) by itself, or an assertion that \(G_s\) is a sharp pair mask of \(G\), is not this hypothesis.  Commuting orthogonal coordinate compressions are one possible route to form domination; a pair-dependent owner need not have that form.

With \(H=C_\varepsilon L^2X^\varepsilon\), clauses (a)--(f) are the weakest exact abstract criteria and the standard sufficient conversions relevant to (109.3).

## 3. Proof and derivation

The one-count hypothesis partitions the atomic difference.  Summing the atoms first within each fibre and then over the fibres over block \(B\) gives
\[
 q^{\rm f}_B-q^{\rm h}_B
 =\sum_{i:\,\pi(i)\in\{B\}\times\mathcal O}a_i
 =\sum_\nu O_{B,\nu}=\Delta_B.
\]
This is the only algebra needed to place the completed scalar block sum on its fixed lattice.  It does not alter any coefficient or metric density.

Two applications of the triangle inequality give
\[
 \left|\sum_B\Delta_B\right|
 \leq\sum_B|\Delta_B|
 \leq\sum_{B,\nu}|O_{B,\nu}|,
\]
which proves the norm hierarchy.  If \(D\leq H\), then for every \(z\),
\[
 \|z-\Delta\|_1\leq\|z\|_1+\|\Delta\|_1
 \leq\|z\|_1+H.
\]
Conversely, taking \(z=0\) in that uniform translation inequality gives \(D=\|\Delta\|_1\leq H\).  This proves the necessary/sufficient block-transfer assertion.  The owner-majorant equivalence is also exact: the proposed \(M_{B,\nu}\) imply \(C_{\rm own}\leq H\), while if \(C_{\rm own}\leq H\) one may take \(M_{B,\nu}=|O_{B,\nu}|\).

For an absolutely convergent separation, Minkowski's inequality gives
\[
 \sum_s\left|\sum_t\lambda_tO_s^{(t)}\right|
 \leq\sum_t|\lambda_t|\sum_s|O_s^{(t)}|.
\]
For the row-energy conversion, first use Cauchy--Schwarz in each \(\mathcal H_s\), then across \(s\):
\[
 \sum_s|\langle x_s,u_s\rangle|
 \leq\sum_s\|x_s\|\,\|u_s\|
 \leq
 \left(\sum_s\|x_s\|^2\right)^{1/2}
 \left(\sum_s\|u_s\|^2\right)^{1/2}.
\]
The Gram assertion follows immediately by summing its stated form dominations.  None of these arguments permits deletion of the displayed normalization factors.

Finally, the supplied aggregate data cannot force (109.3).  For any \(T>0\), take two blocks, one owner family, disjoint singleton atoms with
\[
 O_{1}=T,\qquad O_{2}=-T,
 \qquad q^{\rm f}_1=q^{\rm f}_2=0,
 \qquad q^{\rm h}=(-T,T).
\]
Then (109.1) holds block by block.  Taking \(E_{\rm owned,L}=0\) and \(E_L^{\rm top}=0\) gives (109.2), because \(\sum_Bq_B^{\rm h}=0\).  The signed owner aggregate is also zero, whereas \(C_{\rm own}=D=2T\).  Letting \(T/(L^2X^\varepsilon)\) be arbitrarily large proves the logical no-go.  This is an arbitrary-coefficient model only; it makes no assertion that the literal M2 amplitudes attain these values.

## 4. First doubtful or unproved step

The first unproved step is any claim of the form
\[
 E_{\rm owned,L}\ll L^2X^\varepsilon
 \quad\hbox{or}\quad
 \left|\sum_{B,\nu}O_{B,\nu}\right|\ll L^2X^\varepsilon
 \quad\Longrightarrow\quad
 \sum_{B,\nu}|O_{B,\nu}|\ll L^2X^\varepsilon.
\]
The left sides retain cancellation or positivity at a different normalization; the right side forbids cancellation after every block-owner slot has been formed.  The accepted one-count/disjointness assertion solves the algebraic bookkeeping issue but supplies no such norm conversion.

Likewise, a separately proved scalar estimate is relevant only if it already has the form \(\sum_B|O_{B,\nu}|\), and an energy estimate is relevant only after the explicit row mass or a Gram form-domination theorem is included.  The permitted material does not state which prior owner estimates have either form.  Therefore this report cannot rigorously name a Round-77, Round-78, Round-79, Round-103, or Round-104 family as the first literal obstruction.  The first identifiable obstruction is the norm-upgrade inference itself.

## 5. Control tests and outcomes

**`owner_one_count_and_disjointness`.**  Exact input: take algebraically independent atom amplitudes \(a,b\) with intended difference \(a+b\).  The correct fibres \(O_1=a\), \(O_2=b\) sum to \(a+b\).  A duplicated assignment \(O_1=a\), \(O_2=a+b\) sums to \(2a+b\), and at \((a,b)=(1,0)\) overcounts by one; omission is detected similarly.  Expected invariant: equality coefficient-by-coefficient for arbitrary atom amplitudes.  Observed outcome: exact one-count and disjointness are necessary for a structural identity; equality for one accidental numerical specialization would not certify them.  Implication: the blind statement explicitly grants this invariant, so the abstract lemma conditionally passes this control, but the literal historical owner incidence cannot be audited from the permitted files.

**`scalar_vs_energy_normalization`.**  Exact input: one block-owner scalar is the sum of \(N\) row entries, \(O=\langle x,\mathbf1_N\rangle\), with \(x_r=N^{-1/2}\).  Then \(\sum_r|x_r|^2=1\), but \(|O|=\sqrt N\).  Expected failure: a row-energy bound of one does not give a scalar bound of one.  Observed outcome: the missing factor is exactly \(\|\mathbf1_N\|_2=\sqrt N\), and equality holds in Cauchy--Schwarz.  Implication: every energy-based owner proof must display its row-summation mass (and any block count); an unnormalized energy statement cannot establish (109.3).

**`blockwise_absolute_vs_signed_aggregate`.**  Exact input: use the two-block model from Section 3 with \(O_1=T\), \(O_2=-T\).  Expected failure: cancellation makes the signed aggregate and the accepted scalar identity small while the outside-absolute cost is large.  Observed outcome:
\[
 \left|O_1+O_2\right|=0,
 \qquad E_{\rm owned,L}=E_L^{\rm top}=0,
 \qquad \sum_B|O_B|=2T.
\]
Thus even an individual owner family can have a perfect signed aggregate estimate and an arbitrarily bad blockwise absolute norm.  A second exact input, one block with two owners \(O_{1,1}=T\), \(O_{1,2}=-T\), has \(D=0\) but \(C_{\rm own}=2T\).  Implication: \(D\) is the sharp block-transfer norm, while (109.3) is the sharper ownerwise certificate and cannot be recovered from cancellation between owners.

**`Fejer_commutator_and_Gram_nonimplication`.**  Exact input: for \(T>1\), put \(\delta=T^{-2}\) and use the two-point positive Gram matrix, sharp coordinate projection, and pair mask
\[
 F_\delta=
 \begin{pmatrix}1&1-\delta\\1-\delta&1\end{pmatrix},
 \qquad
 P=\begin{pmatrix}1&0\\0&0\end{pmatrix},
 \qquad
 M=\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad x=T\binom{1}{-1}.
\]
The eigenvalues of \(F_\delta\) are \(\delta\) and \(2-\delta\), so it is positive definite.  Expected failure: positivity of the full Fejer-type Gram and smoothness of its entries do not control a noncommuting sharp compression or a pair-dependent Schur mask.  Observed outcome:
\[
 x^*F_\delta x=2,
 \qquad
 [P,F_\delta]=
 \begin{pmatrix}0&1-\delta\\-(1-\delta)&0\end{pmatrix}\ne0,
 \qquad
 (Px)^*F_\delta(Px)=T^2,
\]
and
\[
 x^*(F_\delta\circ M)x=-2(1-\delta)T^2.
\]
The masked matrix is indefinite.  Implication: neither a full positive Gram bound nor an unjustified commutation step controls a sharp pair owner; one needs literal numerical-radius/form domination or a direct scalar outside-absolute estimate.  This is a finite arbitrary-coefficient control, not a claim that \(F_\delta\) is the literal M2 Fejer matrix or that the actual coefficients realize \(x\).

All four controls are analytical finite models; no numerical experiment is used as proof.

## 6. Dependencies and exact artifacts used

This report used only:

- `rounds/codex-managed/m9-m2-blockwise-owner-completion/briefs/blind_owner_completion_rederivation.md` (task contract and frozen question);
- `rounds/codex-managed/m9-m2-blockwise-owner-completion/blind_statement.md` (the statement-only algebra and desired gate);
- `problems/gauss_circle.md` (problem scope); and
- `state/control_models.md` (control semantics and reporting requirements).

No proof graph, proof draft, strategy file, derivation packet, conductor candidate, sibling report, prior claimant derivation, web source, or computational artifact was used.

## 7. Recommended state effect

**Retain** the blockwise owner-completion gate as unresolved and do not promote the fixed-\(K\) ownerwise completion from the supplied aggregate or energy information.  Reject the aggregate-to-blockwise, unnormalized energy-to-scalar, and positivity-to-masked-owner implications as proof steps.

Closure requires, for every literal owner family, (i) an audited one-count incidence statement and (ii) either a direct estimate \(\sum_B|O_{B,\nu}|\leq H_\nu\) with \(\sum_\nu H_\nu\ll L^2X^\varepsilon\), or an energy/Gram estimate accompanied by the exact normalization or form-domination argument in Section 2.  Until those literal data are supplied, no named owner should be promoted or rejected on the basis of this isolated report.
