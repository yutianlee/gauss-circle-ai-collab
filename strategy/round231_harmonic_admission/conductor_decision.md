# Full harmonic pooling: Round231 admission decision

11 October 2026. User-requested follow-up to the previous admission screen. **Do not launch analytic Round231 on this mechanism.** Full harmonic pooling followed by one absolute value for each squarefree-label tuple still has an unavoidable \(T^{5/2}\) certificate. This is a new proof for the requested pooling order, not an inference from the earlier fixed-norm result.

## Exact outcome

Let \(f_d\) contain every harmonic of the actual squarefree class \(d\), with the original mollifier and real cosine phase. For \(Q=\lfloor T^{2/5}\rfloor\), write

\[
J_{\boldsymbol d}(T)=\int w(R/T)\prod_{j=1}^{12}f_{d_j}(R)\,dR,
\quad I_{12}(T)=\sum_{\boldsymbol d}^{*}J_{\boldsymbol d}(T),
\]

where the star means ordered, pairwise distinct squarefree labels \(d_j>Q\). Pooling every harmonic and sign before taking a modulus gives

\[
\mathcal C_{\rm harm}(T)=\sum_{\boldsymbol d}^{*}|J_{\boldsymbol d}(T)|.
\]

The reviewed conclusion, for every sufficiently large real \(T\), is

\[
\boxed{\mathcal C_{\rm harm}(T)\gg T^{5/2}.}
\]

Consequently this certificate cannot satisfy \(T^{29/25+\varepsilon}\), nor any exponent below \(5/2\). It does **not** disprove a target-sized bound on the signed \(I_{12}\), and does not lower-bound the complete moment.

## Why the harmonics do not remove the obstruction

The direct proof constructs many actual squarefree-label tuples whose fundamental six-versus-six frequency is within \(O(1/T)\). Unlike the earlier proof, it then controls each complete class integral, including every higher harmonic.

The arithmetic coefficient ratio is bounded by

\[
\frac{r_2(dh^2)}{r_2(d)}\le g(h),
\qquad g(h)=\prod_{p\equiv1\pmod4}(2v_p(h)+1),
\]

and the higher common multiples obey the exact bound

\[
\sum_{h\ge2}g(h)^{12}h^{-18}<\frac1{200000}.
\]

After the mollifier normalization and cosine factors are restored, these common multiples cannot cancel the positive fundamental contribution. This calculation allows every higher mollifier coefficient to have either sign. Nonproportional bounded harmonic relations remove only a smaller weighted set of tuples. The entire infinite mixed harmonic tail is paid before taking any modulus. Thus a positive contribution of size \(T^{5/2}\) survives even inside the fully pooled class integrals.

A separate statement-only proof reaches the same result by a different argument. It treats full sixfold class products as vectors in a weighted function space. A frequency approximation of dimension \(O(T^{3/2})\) retains positive energy; a weighted Gram inequality gives absolute correlation mass \(\gg T^{5/2}\). All repeated-label contributions cost only \(O(T^{9/4})\). This proof includes the infinite harmonics directly and does not assume that any particular fundamental resonance survives.

The needed actual squarefree mass is also independently proved. An elementary prime-square union costs at most \(23/24\) of the weighted shell main term, with \(O(\sqrt T\log T)\) error. Thus no unverified squarefree-density or fine-scale equidistribution claim is used.

## Complete target and strategy consequence

Accepted216 still pays the head at exponent \(15/13\) and repeated-class error at \(8\beta-1/5\). The preferred complete target remains

\[
M_{12}(B_T)\ll T^{29/25+\varepsilon},
\]

equivalently a bound of that size for the fully signed \(I_{12}\). The accepted complete exponent is still \(10\beta=1.28966351948\ldots\). The additional saving needed is still \(10\beta-29/25=0.12966351948\ldots\); no new upper bound has been obtained.

The next admissible mechanism must retain cancellation **between different squarefree-label tuples**, or obtain an equivalent complete signed estimate through another representation. Full harmonic pooling alone, followed by absolute values at those tuples, is now excluded by a direct proof. This is a restriction on the proposed method, not an impossibility result for the Gauss circle problem. Round231 remains pending design with no analytic tasks.

## Evidence and state

- [Conductor's minimal full proof](conductor_harmonic_obstruction.md), independently reviewed at its frozen hash in [the seam review](reviews/harmonic_pooling_seam_review.md).
- [Independent discovery proof](reports/harmonic_pooling_discovery.md), [statement-only Gram proof](reports/blind_harmonic_pooling.md), and [isolated squarefree-mass proof](reports/blind_squarefree_mass.md).
- [Conductor report and restoration review](reviews/conductor_report_review.md). Exact Wolfram inequalities were reproduced locally with integer/fraction arithmetic; all asymptotic conclusions are analytical.

These are reviewed admission results, not newly promoted graph nodes. The graph's401 nodes, proof draft, validation matrix, closed Round230 manifest, round ledger, previous admission packet and historical campaigns remain unchanged. No State Patch is proposed or applied. Admission/navigation metadata records the result and the narrower requirement for a future mechanism. The full proof and the complete twelfth-moment target remain open.
