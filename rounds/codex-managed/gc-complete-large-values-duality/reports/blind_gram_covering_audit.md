# Round204: independent Gram and covering audit

## 1. Result

**Role:** statement-only independent derivation. **Task:** `blind_gram_covering_audit`. **Campaign:** `gc-complete-large-values-duality`. **Date:** 2026-09-23. The graph hash was not supplied in the isolated packet and was not accessed.

Put

\[
m=\#\{n\in\mathbb Z:N<n\leq2N\},\quad L=|J|,\quad
D=\frac{Am}{\sqrt N},\qquad
h_0(V)=\left(\frac{V^2}{2A^2}\right)^{1/\kappa}.
\]

For \(L>0\), let \(K(V)=\lceil L/h_0(V)\rceil\); in particular, \(K(V)=1\) when \(h_0(V)\geq L\). Write
\(\mu(V)=|\{R\in J:|S(R)|\geq V\}|\). There is an absolute constant \(C_0\) such that, whenever \(1\leq V^2\leq D\),

\[
\boxed{
\mu(V)\leq
\min\left\{
L,\quad
\frac{C_0A}{V^2}\left(1+\frac L{\sqrt N}\right),\quad
\frac{C_0A^2}{V^2}\log\left(2+\frac D{V^2}\right)
\left\lceil\frac L{h_0(V)}\right\rceil
\right\}.}
\tag{1}
\]

If \(V^2>D\), the level set is empty. If \(L=0\), its measure is zero. Constants in (1) do not depend on interval endpoints. Since \(m\leq2N\), a slightly weaker expression replaces \(D\) by \(2A\sqrt N\).

In particular, the covering part of (1) gives

\[
\mu(V)\ll_\kappa
\log\left(2+\frac D{V^2}\right)
\left\{\frac{A^2}{V^2}
+\frac{L A^{2+2/\kappa}}{V^{2+2/\kappa}}\right\}.
\tag{2}
\]

The first term in braces survives when the localization length exceeds the entire interval, including when it exceeds \(T\). Replacing the ceiling by \(L/h_0(V)\) is invalid.

An aligned coefficient family has supremum \(N^{1/4}\) and a peak of width comparable to \(N^{-1/2}\). Its twelfth moment is at least a constant times \(N^{5/2}\). Taking \(N=\lfloor T^{4\beta}\rfloor\), \(\beta=0.129\), gives the exponent \(10\beta=1.29>29/25=1.16\). Thus, wherever the packet's kernel hypothesis holds on these blocks, the generic data admit a coefficient family incompatible with the proposed \(29/25\) moment bound. This is a generic-coefficient obstruction, not a claim about fixed arithmetic coefficients.

## 2. Exact hypotheses and normalization

The hypotheses used are precisely the packet's: \(T\geq2\), \(1\leq N\leq T^{3/2}\), \(0<\kappa<1\), \(A\geq1\), and a real interval \(J\subset[cT,CT]\). Set \(e(x)=\exp(2\pi i x)\), and assume

\[
S(R)=\sum_{N<n\leq2N}a_ne(R\sqrt n),\qquad
q:=\sum|a_n|^2\leq A N^{-1/2}.
\]

For \(0<|u|\leq CT\), the assumed correlation estimate is

\[
|\mathcal K(u)|:=\left|\sum_{N<n\leq2N}e(u\sqrt n)\right|
\leq A\sqrt N\bigl(|u|^\kappa+|u|^{-1}\bigr).
\tag{3}
\]

The exact trivial bound is \(|\mathcal K(u)|\leq m\), including at \(u=0\). Every difference of two points of \(J\) lies in the stated range of (3). No integrality of \(N,T\), endpoints, or sample positions is assumed in the upper bound. The coefficients can be arbitrary complex numbers.

The sampling spacing is

\[
\boxed{\delta=\frac{A\sqrt N}{m}.}
\tag{4}
\]

It need not be less than the local interval length. That case is retained explicitly. The exact supremum estimate is

\[
|S(R)|^2\leq qm\leq D.
\tag{5}
\]

If the actual value of \(q>0\) is known, the same argument improves (1) by replacing \(D\) with \(qm\), every \(A^2\) arising in the covering argument with \(qA\sqrt N\), and its localization length with
\((V^2/(2qA\sqrt N))^{1/\kappa}\). The spacing (4) remains unchanged. The Gaussian bound becomes \(C_0q(L+\sqrt N)/V^2\). If \(q=0\), every level set here is empty.

## 3. Proof and derivation

### Finite-vector duality, with the diagonal retained

Let \(R_1,\ldots,R_b\) be \(\delta\)-separated points in an interval of length at most \(h\), with \(|S(R_j)|\geq V\). Let \(M\) be the matrix with entries \(M_{j,n}=e(R_j\sqrt n)\). Its sample Gram matrix is

\[
G=MM^*,\qquad G_{ij}=\mathcal K(R_i-R_j),\qquad G_{ii}=m.
\]

Finite-dimensional duality and Cauchy--Schwarz give

\[
bV^2\leq\|Ma\|_2^2\leq q\|G\|_{2\to2}
\leq q\max_i\sum_j|G_{ij}|.
\tag{6}
\]

The final inequality follows directly from
\(2|z_i z_j|\leq|z_i|^2+|z_j|^2\) and symmetry, so no external large-sieve theorem is being imported.

Write \(B=A\sqrt N\). For \(0<|u|\leq h\), the two kernel bounds imply

\[
|\mathcal K(u)|\leq B h^\kappa+\min(m,B/|u|).
\tag{7}
\]

On either side of a fixed sample point, its \(j\)-th neighbor is at distance at least \(j\delta\). By (4), \(B/(j\delta)=m/j\). With \(H_r=\sum_{j=1}^rj^{-1}\) and \(H_0=0\), (6)--(7) yield

\[
\boxed{bV^2\leq D+A^2(b-1)h^\kappa+2D H_{b-1}.}
\tag{8}
\]

This inequality is valid also for \(b=1\), when it reads exactly \(V^2\leq D\). Neither the diagonal nor a sparse-sample case has been discarded.

If \(h\leq h_0(V)\), the middle term in (8) is at most \((b-1)V^2/2\). Consequently

\[
\frac{bV^2}{2}\leq D(1+2H_{b-1}).
\tag{9}
\]

For a nonempty level set put \(r=D/V^2\geq1\). For \(b\geq2\), use \(H_{b-1}\leq1+\log b\) to obtain
\(b\leq2r(3+2\log b)\). Elementary inversion gives

\[
b\ll r\log(2+r).
\tag{10}
\]

For example, \(b\leq64r\log(4r)\) follows by the monotonicity of \(x/(3+2\log x)\) for \(x\geq1\). The same bound includes \(b=1\).

### Separated cover, without a persistence assertion

Partition \(J\) into \(K=\lceil L/h_0(V)\rceil\) intervals of length at most \(h_0(V)\). For each piece \(I\), choose a maximal \(\delta\)-separated subset of
\(E_I=\{R\in I:|S(R)|\geq V\}\). A finite maximal subset exists: any separated set in \(I\) has at most \(1+|I|/\delta\) points. If it has \(b\) points, maximality covers \(E_I\) by the \(b\) intervals of radius \(\delta\) centered at those points. Therefore

\[
|E_I|\leq\min\{|I|,2\delta b\}
\ll\frac{\delta D}{V^2}\log\left(2+\frac D{V^2}\right)
=\frac{A^2}{V^2}\log\left(2+\frac D{V^2}\right).
\tag{11}
\]

Only the selected points must be large. There is no claim that the values persist throughout their covering intervals. If \(|I|<\delta\), a nonempty maximal sample set has one point and (8), (10), and (11) still apply. Assigning shared partition endpoints to either piece changes neither measure nor the proof. Open, closed, and half-open choices for \(J\) also cause no difficulty.

Summing (11) proves the covering term of (1). The inequality \(\lceil x\rceil\leq1+x\) gives (2), with the displayed powers of \(A\). In the regime \(h_0(V)\geq L\), the proof uses one interval. It never substitutes a fractional number of intervals.

For completeness, the same proof permits an optimization over the absorption parameter. For every \(0<h\leq L\) with
\(W^2:=V^2-A^2h^\kappa>0\), it gives

\[
\mu(V)\ll
\left\lceil\frac Lh\right\rceil
\frac{A^2}{W^2}\log\left(2+\frac D{W^2}\right).
\tag{12}
\]

One may take the infimum of this valid family together with the other bounds in (1). Choosing half of \(V^2\) for absorption gives the simpler explicit formula (1).

### Additional elementary \(L^2\) bound

Let \(R_c\) be the midpoint of \(J\), and put \(U=\max(L,\sqrt N)\). The Gaussian \(w(R)=\exp(-((R-R_c)/U)^2)\) is at least \(e^{-1/4}\) on \(J\). Its frequency Gram entries have absolute values

\[
\sqrt\pi U\exp\bigl(-\pi^2U^2(\sqrt n-\sqrt m)^2\bigr).
\]

For two indices in the block,
\(|\sqrt n-\sqrt m|\geq|n-m|/(2\sqrt{2N})\). Since \(U\geq\sqrt N\), each row sum is bounded by
\(\sqrt\pi U\sum_{k\in\mathbb Z}\exp(-\pi^2k^2/8)\ll U\).
The same finite-vector inequality as above proves

\[
\int_J|S(R)|^2\,dR\ll qU\ll A\left(1+\frac L{\sqrt N}\right).
\tag{13}
\]

Chebyshev's inequality yields the middle term of (1). The Gaussian Fourier integral used here follows by completing the square (equivalently by the elementary Gaussian transform); no arithmetic input or kernel estimate (3) is required for (13).

### Consequence for the twelfth moment

Suppose \(\|S\|_{L^\infty(J)}\leq M\), with \(M\geq1\), and let \(\ell=\log(2+D)\). Layer cake and (2) imply

\[
\int_J|S|^{12}\ll_\kappa
L+\ell\left[A^2M^{10}
+L A^{2+2/\kappa}\mathcal I_\kappa(M)\right],
\tag{14}
\]

where exactly

\[
\mathcal I_\kappa(M)=\int_1^M v^{9-2/\kappa}\,dv
=\begin{cases}
\dfrac{M^{10-2/\kappa}-1}{10-2/\kappa},&\kappa\ne1/5,\\[4pt]
\log M,&\kappa=1/5.
\end{cases}
\]

For \(\kappa<1/5\) this integral is bounded by a constant depending on \(\kappa\). If \(A=T^\varepsilon\), \(L\ll T\), \(N\leq T^{3/2}\), and \(M\ll T^\beta\), (14) has exponent at most

\[
\max\{1,\ 10\beta,\ 1+(10-2/\kappa)_+\beta\}
+O_\kappa(\varepsilon),
\tag{15}
\]

with a logarithm at \(\kappa=1/5\). Formula (14) records the full powers of \(A\) before any subpower convention. Crucially, the \(M^{10}\) term cannot be removed just because the localization length is long or a maximal sample set has few points.

## 4. First doubtful or unproved step

There is no unproved step in the finite-vector, covering, or Gaussian conclusions above, conditional on the packet's stated kernel estimate. The validity of that kernel estimate for a specific \((T,N,\kappa,A)\) is an input, not something proved by this report.

The first invalid step in a putative stronger generic argument would be replacing \(\lceil L/h_0\rceil\) by \(L/h_0\) when \(h_0>L\), or deleting the diagonal \(m\) in (6) when only one sample is present. Either loses the single-peak regime. Covering a level set by neighborhoods of selected points also does not authorize treating the entire neighborhoods as large-value sets; our proof only uses the valid direction of containment.

A claim about a fixed arithmetic coefficient family requires additional information that excludes or controls the aligned coefficients in Section 5. No such information appears in the isolated packet. It would be an unproved transfer to declare the arithmetic family's moment estimate false from this generic control alone.

## 5. Required controls and outcomes

**Aligned single peak, including its width.** Take an integer \(N\geq1\), so the block contains exactly \(N\) terms. Choose \(R_0\) in the interior of \(J\), and set

\[
a_n=N^{-3/4}e(-R_0\sqrt n),\qquad N<n\leq2N.
\tag{16}
\]

Then \(\sum|a_n|^2=N^{-1/2}\), and

\[
S(R_0)=N^{1/4},\qquad \sup_{R\in\mathbb R}|S(R)|=N^{1/4}.
\tag{17}
\]

Let \(\eta=1/(12\sqrt2)\). For \(|x|\leq\eta N^{-1/2}\), every angle \(2\pi x\sqrt n\) has absolute value at most \(\pi/6\). Taking real parts in
\(S(R_0+x)=N^{-3/4}\sum e(x\sqrt n)\) gives

\[
|S(R_0+x)|\geq\frac{\sqrt3}{2}N^{1/4}.
\tag{18}
\]

If \([R_0-\eta N^{-1/2},R_0+\eta N^{-1/2}]\subset J\), then

\[
\boxed{\int_J|S(R)|^{12}\,dR
\geq2\eta\left(\frac{\sqrt3}{2}\right)^{12}N^{5/2}.}
\tag{19}
\]

More generally, choosing \(R_0\) at the midpoint of an arbitrary nondegenerate \(J\) gives a lower bound \(\gg N^3\min(L,N^{-1/2})\). Thus the control accounts for the actual width and does not infer a positive moment contribution from a single point alone.

For \(N=\lfloor T^{4\beta}\rfloor\), \(\beta=129/1000\), the allowed range \(N\leq T^{3/2}\) holds for large \(T\). Any macroscopic displaced interval contains the required peak neighborhood. The supremum is comparable to \(T^\beta\), the peak width is comparable to \(T^{-2\beta}\), and (19) is
\(\gg T^{10\beta}=T^{129/100}\). The gap above \(29/25\) is \(13/100\).

**Scope of the kernel compatibility.** Changing the coefficient phases as in (16) changes neither the kernel \(\mathcal K\) nor its parameters. Hence, on every block where the assumed estimate (3) is valid, (16) is an allowed coefficient family satisfying the exact norm condition. If (3) is supplied uniformly over the packet's range, the preceding \(N=\lfloor T^{4\beta}\rfloor\) sequence is an immediate counterfamily to a generic \(29/25\) conclusion. This report does not independently assert uniform validity of (3) for arbitrary \(\kappa\); that is explicitly the packet's hypothesis. It also does not identify (16) with the fixed \(r_2\) arithmetic family.

**Single-sample control.** At \(R_0\), inequality (8) with \(b=1\), \(A=1\), reads \(N^{1/2}\leq N^{1/2}\): equality. Deleting the diagonal would make this legitimate sample impossible. For any larger admissible \(A\), the same control remains valid with slack.

**Endpoint and spacing controls.** The separated-cover proof remains valid for \(h_0>L\), \(\delta>L\), one sample, empty sample sets, real endpoints, and a level set consisting only of isolated points. Isolated points have zero measure, while (8) still controls their values. No endpoint rounding or derivative-based interpolation is required.

**Outcome:** all controls pass for (1)--(14); the aligned control rejects the proposed stronger generic moment implication on blocks satisfying the assumed correlation bound. These are analytic controls, not numerical experiments.

## 6. Exact dependencies and artifacts used

Only these files were read:

1. `protocol.md`.
2. `rounds/codex-managed/gc-complete-large-values-duality/briefs/blind_gram_statement.md`.

The only mathematical inputs beyond the displayed packet assumptions are finite-dimensional Cauchy--Schwarz, the elementary row-sum bound proved around (6), the harmonic-sum estimate, a finite maximal separated cover, the elementary Gaussian transform, and layer cake. Their uses and normalizations are supplied in Section 3.

No graph, manifest, strategy, generated claimant brief, source card, prior report, sibling artifact, web source, or experiment was consulted. No shared proof-state file was changed. This report is the only output artifact of this task.

## 7. Recommended state effect

**Retain** the generic Gram/covering bound with its diagonal, spacing, norm cutoff, and full ceiling. **Reject** an inference that these generic norm/correlation data alone force the \(29/25\) twelfth-moment exponent for all coefficient families with supremum comparable to \(T^{0.129}\), when the kernel hypothesis applies to the indicated blocks. The single aligned peak is already sufficient to obstruct that inference.

**No promotion of an arithmetic target:** the isolated packet supplies no arithmetic property distinguishing fixed coefficients from the aligned family. Any accepted-state change remains the conductor's responsibility after the required reviews. This task stops at this report and proposes no successor round.
