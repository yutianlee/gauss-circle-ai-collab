## 1. Result: lemma or no-go result.

**Separable-self-return no-go.**  The advertised full-rank Hessian in the two variables \((d,u)\) is real, but it is not new joint curvature.  After the integral unimodular change
\[
 r=n+d+u,\qquad s=m+d,
\]
it is exactly the direct sum of the two one-row curvatures belonging to \(I_b(r)\) and \(\overline{I_b(s)}\).  The same change turns the complete trace phase into the four original physical rows.  Consequently a two-dimensional Poisson/stationary-phase B-process applied before taking configurationwise absolute values is a self-return to the row representation whose sup-norm product already defines the Round-82 Schur capacity.  Guo's literal multidimensional B-process does give a scalar smooth-interior bound with a nominal \(J^{-1/5}\) saving, but there is no valid step that multiplies the already-normalized Schur capacity by that saving.  Applied after the hard-owner and moving-trace factors are installed, its amplitude hypotheses are not met.

This is also a **configuration-separated high-moment no-go**.  After expanding the complete trace at a fixed physical base \(x\), every fixed configuration is a rank-one \((n,m)\)-character atom.  Diagonal/backtracking words therefore survive in high traces at Schur scale.  The exact local configuration
\[
 q=8,\qquad A=B_2=V=2
\]
has constant inverse phase and a nonzero residual parity mode \(u=4\) of normalized magnitude \(1/2\).  Thus neither configurationwise absolute values nor a generic Deligne/high-Schatten argument can furnish the required gap.

There is a separate, conditional **uniform-norm barrier**.  If the literal remaining hard block has dimension \(N\asymp B^2\), normalized row mass \(\asymp1\), and \(\asymp N^2\) entries of magnitude \(\asymp N^{-1}\), then
\[
 \|K\|_{\mathrm{op}}\geq \frac{\|K\|_F}{\sqrt{N}}\asymp B^{-1}.
\]
At the top scale the target is \(J^{-1/6}=B^{-10/9}\), so even an ideal random/Hadamard-sized uniform norm is short by \(B^{-1/9}\).  The selected artifacts do **not** prove the comparable-entry premise for the complete hard symbol, so this is a required obstruction test, not a global lower bound.

None of these no-go statements rules out a genuinely directional estimate for the one actual vector after summing conductor cells and physical configurations *before* absolute values.  Such an estimate would have to prove small projection onto the coherent parity/pairing modes.  No audited primary theorem does this for the varying composite modulus, complete four-row trace, nonunit \(K\), full two-part, hard-owner masks, and the required \(J^{-1/6}\) gain.

## 2. Exact statement and hypotheses.

Work with
\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad B=C/T,
 \qquad J^{13/18}<C\leq J^{3/4},
\]
so \(B\leq J^{3/20}\).  The canonical hard estimate is
\[
 |\mathcal E_{\mathrm{hard}}(U)|\ll_\epsilon X^\epsilon\frac UB J^{14/5}.
\]
The Round-82 capacity is
\[
 \mathsf C_{82}=B^3T^2Q^{-5/12};
\]
after normalizing its Gram/Schur capacity to one, the missing top-scale operator gain is \(J^{-1/6}=B^{-10/9}\).

The audit retains literally the complete trace
\[
 \mathfrak T_M(u,A,B_2,V)
 =M\!\sum_{\substack{x\bmod M\\x,x-A,x-V,x-V-B_2\in(\mathbb Z/M\mathbb Z)^\times}}
 e_M\!\left(ux+K\Phi(x)\right),
\]
where
\[
 \Phi(x)=\bar x-\overline{x-A}-\overline{x-V}+\overline{x-V-B_2},
\]
and the actual fourfold symbol
\[
 \Omega_{b,d,u}(n,m)
 =I_b(n+d+u)\overline{I_b(n)}\,\overline{I_b(m+d)}I_b(m).
\]
The hard complement is the one remaining after the unique global \(u=0\) extraction and the Round-87--89 owner rules.  No class, sign, alias, reflection, modulus multiple, Ramanujan term, nonunit \(K\), or two-adic factor is silently removed.

The precise conclusions are as follows.

**(a) Exact Hessian statement.**  On any stationary branch on which a row has phase \(I_b(k)=a_b(k)e(\psi_b(k))\), put
\[
 \Psi(d,u)=\psi_b(n+d+u)-\psi_b(m+d)+\frac{dV+ux}{M}.
\]
Writing \(a=\psi_b''(n+d+u)\), \(b=\psi_b''(m+d)\),
\[
 D^2_{d,u}\Psi=
 \begin{pmatrix}a-b&a\\a&a\end{pmatrix},
 \qquad \det D^2_{d,u}\Psi=-ab.
\]
For the advertised leading row phase, \(k\asymp Q^2\) and
\[
 \psi_b''(k)\asymp JQ^{-3}=J^{-1/5},
\]
so the determinant is \(\asymp-J^{-2/5}\) and both singular values are \(\asymp J^{-1/5}\), provided the exact lower terms preserve this uniformly.  However, with
\[
 L=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad \det L=-1,
\]
one has exactly
\[
 D^2_{d,u}\Psi=L^T\operatorname{diag}(a,-b)L.
\]

**(b) Literal scalar B-process hypothesis.**  Guo, Proposition 2.4, considers
\[
 S(\mathcal T,\mathcal M;G,F)
 =\sum_{\mathbf m\in\mathbb Z^2}G(\mathbf m/\mathcal M)
 e(\mathcal T F(\mathbf m/\mathcal M)),
\]
with \(G\in C_c^\infty\), support a fixed positive distance inside a fixed bounded convex domain, uniformly bounded derivatives of \(G,F\) through the order stated there (order four when \(d=2\)), and \(|\det D^2F|\gg1\) throughout.  It gives
\[
 S\ll \mathcal T+\mathcal M^2\mathcal T^{-1}.
\]
For a smooth \(U\times U\) stationary interior with \(\lambda=J^{-1/5}\), \(\mathcal M=U\), and \(\mathcal T=\lambda U^2\), this is
\[
 S\ll J^{-1/5}U^2+J^{1/5}.
\]
For \(U\geq D_1=J^{87/140}\), the first term dominates and the isolated scalar sum has a nominal relative saving \(J^{-1/5}\).  This conclusion assumes a smooth compact interior amplitude, one fixed stationary/alias branch, bounded normalized derivatives of the *exact* phase, and no arithmetically moving trace or owner mask in the amplitude.

**(c) Fixed-configuration rank-one statement.**  Fix \(M,b,\sigma,u,d,A,B_2,V,x\).  The \((n,m)\)-coefficient after opening the trace is, up to a scalar independent of \((n,m)\),
\[
 \Bigl[I_b(n+d+u)\overline{I_b(n)}e_M(nA)\Bigr]
 \Bigl[\overline{I_b(m+d)}I_b(m)e_M(-mB_2)\Bigr].
\]
It is rank one.  Equivalently, after the \((r,s)\) change, one may attach the characters \(e_M(rx)\), \(e_M(n(A-x))\), \(e_M(s(V-x))\), and \(e_M(m(x-V-B_2))\) to the four physical rows; their product is the same expression up to the fixed \((d,u)\)-scalar.  Therefore a uniform improvement cannot be obtained by estimating each such configuration separately and then summing absolute values; high powers retain its diagonal/backtracking words.

**(d) Conditional Frobenius statement.**  Let \(K\) be an \(N\times N\) Schur-normalized hard block.  Suppose constants \(c_0,c_1>0\), independent of scale, exist such that at least \(c_0N^2\) entries satisfy \(|K_{ij}|\geq c_1/N\).  Then
\[
 \|K\|_{\mathrm{op}}\geq c_0^{1/2}c_1N^{-1/2}.
\]
If \(N\asymp B^2\), this is \(\gg B^{-1}\), incompatible with a uniform \(O(B^{-10/9})\) bound.  No positivity or phase alignment is assumed.  By contrast, this statement says nothing about \(Kv_{\rm actual}\) if the actual vector is nearly orthogonal to the large singular directions.

**(e) Scope.**  The unconditional no-go is against (i) treating the leading Hessian as an extra factor on top of Schur capacity, (ii) applying a scalar B-process directly to the hard moving symbol, or (iii) separating configurations before a high-trace/norm argument.  It is not an unconditional lower bound for \(\mathcal E_{\mathrm{hard}}\), and it does not reject a new conductor-averaged, actual-vector directional lemma.

## 3. Proof or derivation.

**Exact physical-row change of variables.**  Set
\[
 r=n+d+u,\qquad s=m+d.
\]
This is an integral bijection in \((d,u)\), with inverse
\[
 d=s-m,\qquad u=r-s+m-n.
\]
It gives
\[
 \Omega_{b,d,u}(n,m)=I_b(r)\overline{I_b(n)}\,\overline{I_b(s)}I_b(m).
\]
More importantly, the entire additive phase after the physical trace is opened satisfies the identity
\[
 ux+dV+nA-mB_2
 =rx+s(V-x)+n(A-x)+m(x-V-B_2).
\]
Thus \(r,n,s,m\) are exactly the four row frequencies based respectively at
\[
 x,\qquad x-A,\qquad x-V,\qquad x-V-B_2.
\]
The inverse phase \(K\Phi(x)\) is unchanged.  This calculation retains the actual fourfold symbol rather than replacing it by arbitrary coefficients.

The Fejér and dyadic factors also expose the self-return rather than disappearing.  The triangular factor becomes
\[
 U-|u|=U-|r-s+m-n|,
\]
and the \(d\)-localizer becomes \(\Pi_{b,U}(s-m)\).  These are precisely the Toeplitz/Fejér couplings of the original Gram lift.  Hence the coordinate change does not create two independent new averaging variables: it returns the two moving rows, coupled by the already-used Gram weights.

**Hessian diagonalization.**  Differentiating the displayed \(\Psi\) gives
\[
 \partial_{dd}\Psi=a-b,\qquad
 \partial_{du}\Psi=a,\qquad
 \partial_{uu}\Psi=a,
\]
and therefore \(\det D^2\Psi=-ab\).  Since \((r,s)^T=L(d,u)^T+\text{constant}\), the congruence
\[
 D^2_{d,u}\Psi=L^T\operatorname{diag}(\psi_b''(r),-\psi_b''(s))L
\]
is exact.  In particular, the negative determinant records one positive and one negative row curvature.  It does not certify curvature of a new joint conductor symbol.

For the leading square-root phase \(\psi_b(k)=-J\sqrt{k}+\text{lower terms}\),
\[
 \psi_b''(k)=\frac{J}{4k^{3/2}}+\text{lower second derivatives}
 \asymp JQ^{-3}=J^{-1/5}
\]
on \(k\asymp Q^2\).  If \(\psi_b^{(j)}(k)\ll JQ^{1-2j}\), then after scaling a \(U\)-box and dividing by \(\lambda U^2\), the normalized derivatives of order \(j\geq2\) are
\[
 \ll \lambda^{-1}U^{j-2}JQ^{1-2j}
 =\left(\frac{U}{Q^2}\right)^{j-2},
\]
which are bounded for \(U\leq Q^2\).  This verifies why Guo's proposition is a legitimate model for a single smooth stationary interior, conditional on uniform control of the exact lower phase, amplitude, and branch boundaries.

It does not verify the canonical hard sum.  The proof of Guo's proposition is Poisson summation followed by stationary phase.  Here its two stationary transforms are the Legendre transforms of the \(r\)- and \(s\)-row phases.  The exact identity above shows that those transforms reconstruct the two physical rows based at \(x\) and \(x-V\); together with the fixed \(n,m\) rows, this is the four-row product whose sup-norm contribution \(T^4Q^{-5/6}\) is already present in \(\mathsf C_{82}^2\).  Multiplying that capacity by another \(J^{-1/5}\) counts the same row-level stationary cancellation twice.

**Why the moving symbol is outside the literal B-process.**  The trace is not a slowly varying amplitude in \(u\).  It is the finite Fourier transform
\[
 \mathfrak T_M(u,A,B_2,V)=M\sum_x w_{M,A,B_2,V,K}(x)e_M(ux),
\]
where \(w\) includes four unit conditions and \(e_M(K\Phi(x))\).  Its variation is arithmetic at the modulus scale.  To make it compatible with a smooth scalar theorem one must either:

* open the \(x\)-sum and absorb each character into the phase, which is exactly the physical-row self-return above; or
* split \((d,u)\) into residue/alias classes and estimate the pieces, which introduces as many mode/classes as the periodic symbol carries and supplies no theorem for their coherent recombination.

In the latter tactic a split into \((d,u)\bmod M\) has up to \(M^2\) pieces.  On each piece the variable spacing is \(M\), the Hessian scales by \(M^2\), and the box side falls from \(U\) to \(U/M\); summing the scalar bounds separately can erase the nominal gain.  Even a square-root loss from only a modulus-sized family is unaffordable relative to the advertised slack: for a family of size \(B=J^{3/20}\), Cauchy costs \(B^{1/2}=J^{3/40}>J^{1/30}\).  A saving survives only if a new joint theorem recombines the physical modes before absolute value; no cited B-process supplies that theorem.

The sharp Fejér factor alone is not the decisive defect.  Its kink at \(u=0\) and its endpoints can be split into two smooth interiors plus one-dimensional boundary strips; in the isolated scalar model those strips are smaller than the bulk.  The literal hard-owner indicator is different: it is a jagged arithmetic function of the row shifts and owner cells, and no uniform compact-interior derivative bounds are available.  Likewise, when a row stationary point enters or exits its support, the one-branch phase/amplitude description changes to an endpoint/transition expansion.  The selected packet provides neither a transition estimate below target nor a proof that exact lower terms preserve
\[
 |\det D^2\Psi|\gg J^{-2/5}
\]
through every retained alias and boundary cell.  A mere \(J^{-1/30}\) margin cannot absorb an unspecified polynomial loss from any of these operations.

**Rank-one atoms and high-trace return.**  With \(u,d,x,A,B_2,V\) fixed, the formula in Section 2(c) factors into one function of \(n\) and one function of \(m\).  Thus each configuration matrix is \(f_c\otimes g_c^*\).  Powers of a sum of such atoms contain the words in which an atom is immediately paired with its adjoint, as well as longer backtracking pairings.  Estimating configurations separately makes those words nonnegative and exactly recovers the row/Schur mass.  This is the operator version of the normal/non-normal dichotomy in trace-function moment theorems: non-normal paired tuples carry a main term rather than square-root cancellation.

**Exact two-adic coherent mode.**  For \(q=8\) and \(A=B_2=V=2\), the allowed bases are precisely the odd residues and
\[
 \Phi(x)=\frac1x-\frac2{x-2}+\frac1{x-4}
 =\frac{8}{x(x-2)(x-4)}\equiv0\pmod8.
\]
This is independent of \(K\), including nonunit \(K\).  Hence
\[
 w_8(x)=1_{x\ \mathrm{odd}},\qquad
 \widehat w_8(0)=4,qquad \widehat w_8(4)=-4,
\]
with all other Fourier coefficients zero.  In the normalization of \(\mathfrak T\),
\[
 \mathfrak T_8(0,2,2,2)=32,qquad
 \mathfrak T_8(4,2,2,2)=-32.
\]
After the unique global \(u=0\) owner is removed, \(u=4\) remains a genuine nonzero local eigencharacter; divided by \(8^2\), its magnitude is \(1/2\).  On the odd physical subspace, \(e_8(4x)=-1\) is scalar.  This proves a coherent actual local mode, not merely an arbitrary-weight counterexample.  It is compatible with CRT tensoring by an odd cofactor.  It does not by itself prove a signed global lower bound, because the odd local factors, archimedean rows, conductor cells, and owner restrictions may still cancel.

**Conditional uniform-norm barrier and its limitation.**  Under the comparable-entry hypothesis,
\[
 \|K\|_F^2=\sum_{i,j}|K_{ij}|^2
 \geq c_0N^2\left(\frac{c_1}{N}\right)^2=c_0c_1^2.
\]
Since \(\operatorname{rank}K\leq N\), the singular values give
\[
 \|K\|_{\mathrm{op}}\geq\frac{\|K\|_F}{\sqrt{\operatorname{rank}K}}
 \geq c_0^{1/2}c_1N^{-1/2}.
\]
Taking \(N\asymp B^2\) yields \(B^{-1}\), whereas the target is \(B^{-10/9}\).  Random phases cannot change this Frobenius calculation.  The exact \(q=8\) computation proves a full local parity degree and nonvanishing local coefficient, but it does not prove that a positive proportion of entries of the *complete* hard block remain comparable after the odd factors and all \(I_b\)-weights are included.  That missing plateau is why this argument is not promoted to an unconditional norm obstruction.  Conversely, even if the uniform operator norm is large, a fixed actual vector may avoid its large singular subspace; only an actual-vector projection calculation can decide that route.

**Literal primary-source audit.**

* Jingwei Guo, [“On lattice points in large convex bodies,” Proposition 2.4](https://www.impan.pl/shop/publication/transaction/download/product/81980), *Acta Arith.* 151 (2012), 83--100, DOI 10.4064/aa151-1-6, is a literal two-dimensional B-process source.  Its hypotheses and bound are those stated in Section 2(b).  It validates the nominal \(J^{-1/5}\) scalar smooth-interior calculation, but not a moving arithmetic symbol, a hard owner mask, or a second gain after the physical rows have already been transformed.
* Fouvry--Kowalski--Michel, [“A study in sums of products,” Theorem 1.5 and Corollaries 1.6--1.7](https://arxiv.org/html/1405.2293v2), treats bounded-conductor bountiful sheaves over a **prime** field and products under \(\mathrm{PGL}_2\) transformations.  A normal tuple or nonzero additive twist gives \(O(\sqrt p)\); a non-normal paired tuple has \(m p+O(\sqrt p)\), with \(m=1\) for distinct pairs.  Thus the source explicitly preserves the pairing modes seen in configuration-separated high traces.  It does not cover a varying composite/powerful modulus, the full two-part, nonunit \(K\), hard four-pole unit mask, or the outer archimedean symbol.
* Milićević--Zhang, [“Distribution of Kloosterman paths to high prime power moduli,” Theorem 4](https://arxiv.org/html/2005.08865v1), treats a fixed odd prime \(p\), modulus \(p^n\), a fixed unit \(b_0\), bounded shift multiplicity, and a domain invariant under a deep translation subgroup.  It gives a power saving unless two active shifts collide modulo a prescribed power of \(p\).  The collision alternative is an explicit coherent exception.  The theorem excludes \(p=2\), and the hard owners are not the required translation-invariant domain; the \(q=8\) mode lies precisely outside its scope.
* Milićević--Qin--Wu, [“Bilinear forms with Kloosterman sums and moments of twisted L-functions,” Theorem 1.1](https://arxiv.org/html/2511.07550v1), is uniform in an integer modulus \(q\), but its kernel is one normalized \(\mathrm{Kl}_2(cmn;q)\) with \((c,q)=1\), two separated coefficient sequences, and the explicit length conditions \(1\leq M\leq Nq^{1/4}\), \(M^{7/5}N<q^{3/2}\), and \(MN\leq q^{5/4}\).  The canonical kernel is instead a varying-modulus complete four-pole trace multiplied by four coupled rows and permits nonunit \(K\).  No literal substitution identifies it with the theorem's single bilinear kernel.
* Pascadi, [“Non-abelian amplification and bilinear forms with Kloosterman sums”](https://arxiv.org/abs/2511.08445v2), and Blomer--Pascadi, [“Bilinear forms with Kloosterman sums via quadratic characters”](https://arxiv.org/abs/2607.24311v1), obtain strong fixed-kernel bilinear savings for composite/all moduli; the latter advertises \(q^{-1/32}\) at square-root lengths.  Both still require a single Kloosterman kernel with two coefficient sequences.  Opening the canonical four-row trace, freezing all other rows, and using Cauchy returns the fixed-column/capacity loss already diagnosed in the selected source audit.  Their high-moment/nonabelian word expansions also retain diagonal word solutions; they do not provide an actual-vector theorem for the complete joint symbol.
* The Deshouillers--Iwaniec Kuznetsov/product-Kloosterman large sieve controls one Kloosterman kernel with a smooth modulus test and separated coefficients.  Here the coefficient itself depends on the varying modulus through \(M^{-5}\mathfrak T_M\), four unit conditions, four row shifts, and the owner mask.  Making those quantities into coefficients before Kuznetsov destroys the required separation; opening and applying Cauchy reproduces the regular large-sieve capacity.  No audited Kuznetsov theorem simultaneously diagonalizes the four rows and the moving modulus without that return.

Accordingly, the primary-source search found a theorem for the idealized scalar Hessian and several theorems for one arithmetic kernel, but no theorem satisfying the literal canonical hypotheses or yielding the required normalized \(J^{-1/6}\) gain.

## 4. First doubtful or unproved step.

The first invalid step in the proposed positive route is the inference
\[
 |\det D^2_{d,u}\Psi|\asymp J^{-2/5}
 \quad\Longrightarrow\quad
 \|\mathcal K_{\mathrm{hard}}\|\ll J^{-1/5}\times
 (\text{Schur capacity}).
\]
The determinant estimate concerns the two already-transformed row phases.  Before hard decomposition, the B-process reconstructs those rows; after hard decomposition, the amplitude contains a nonsmooth moving trace/owner symbol and fails the literal theorem.  There is no intermediate representation in which both the hypotheses hold and the \(J^{-1/5}\) is independent of the row saving already charged to capacity.

Even for the scalar model, the first unproved technical input is a uniform exact-phase packet: lower second derivatives must leave both eigenvalues \(\asymp J^{-1/5}\); derivatives through Guo's required order must be bounded after every alias normalization; and stationary entry/exit plus Fejér/owner boundaries must have total cost \(O(J^\epsilon)\) relative to the bulk.  The leading phase alone does not establish any of these.  Since the nominal surplus is only \(J^{-1/30}\), an uncontrolled residue, transition, or mode split cannot be absorbed.

For the uniform-norm obstruction, the first unproved step is different and must remain separate: no selected artifact proves a dense \(N\asymp B^2\) block on which the *complete* entries, including the odd trace factors and all four \(I_b\)-amplitudes after the hard owners, are bounded below by \(\asymp1/N\).  The \(q=8\) computation proves one nonzero coherent local factor, not that global comparable-entry plateau.

For a still-possible actual-vector route, the missing statement is a directional projection estimate after summing the conductor and physical configurations before absolute value.  It must show that the canonical actual vector has \(O(J^{-1/6+\epsilon})\) overlap with every surviving paired/parity mode, including the \(u=4\) two-adic mode.  No primary source audited here supplies such a statement.

## 5. Control tests and outcomes.

| Control | Outcome |
|---|---|
| Canonical normalization and target | **Pass.** The comparison is made after Schur normalization; the required top gain is \(J^{-1/6}=B^{-10/9}\), not merely a saving over a larger pre-normalized expression. |
| Prior owners counted once | **Pass.** The argument starts on the Round-87--89 hard complement and does not reassign same-group, good-prime, or bad-prime cells. |
| Unique global \(u=0\)/Ramanujan term | **Pass.** The coherent control uses the nonzero mode \(u=4\); it does not duplicate the removed \(u=0\) owner. Nonzero modulus multiples are not silently deleted. |
| All classes, signs, aliases, reflections | **Pass for the no-go algebra.** The \((d,u)\leftrightarrow(r,s)\) change is integral and exact and retains every row. The \(q=8\) example is a control obstruction, not an assertion that every class is coherent. |
| Actual fourfold symbol | **Pass.** All four \(I_b\)-factors occur explicitly in the row identity and the fixed-configuration atom. No arbitrary coefficient sequence replaces them in the no-go. |
| Full-rank Hessian arithmetic | **Pass.** The determinant is exactly \(-\psi_b''(r)\psi_b''(s)\), hence \(\asymp-J^{-2/5}\) under the advertised uniform row-curvature hypothesis. The same calculation proves exact separability. |
| Sharp Fejér mask | **Conditional pass only in the scalar model.** Its kink/endpoints can be partitioned with lower-dimensional boundary strips. This does not smooth the arithmetic hard-owner mask. |
| Stationary entry/exit and exact lower terms | **Fail/open.** No uniform transition estimate or exact derivative/determinant packet with a \(J^{-1/30}\) margin is supplied. |
| Residue/physical-mode splitting | **Fail as a free step.** Freezing the moving trace produces a modulus-sized or larger family; separate absolute estimates can erase the nominal gain. Opening modes gives the exact physical-row self-return. |
| Double Poisson/B-process | **No-go pass.** The unimodular row variables show that it reconstructs the two physical rows and the original Fejér Gram coupling, so no independent multiplicative \(J^{-1/5}\) remains. |
| Configuration-separated global trace moments | **Fail.** Each configuration is rank one and diagonal/backtracking words survive at Schur capacity; Fouvry--Kowalski--Michel's paired main terms confirm the same structural exception. |
| Exact two-adic mode | **Pass.** At \((q,A,B_2,V)=(8,2,2,2)\), \(\Phi\equiv0\), and the residual \(u=4\) normalized eigenvalue has magnitude \(1/2\), independently of \(K\). |
| Powerful moduli and nonunit \(K\) | **No uniform source.** Milićević--Zhang excludes \(p=2\), assumes a unit parameter, and has a shift-collision exception. The \(q=8\) control is independent of \(K\). Prior exact pullback/descent remains a self-return rather than a saving. |
| Perfect-square/fourth-power coherence | **Too sparse alone.** If \(J\) is integral and \(r\) is a square, the leading factor \(e(-J\sqrt r)\) is constant. A length-\(U\) window near \(Q^2\) contains only \(O(1+U/Q)\) squares, hence \(O((1+U/Q)^2)\) paired points; this does not refute the scalar two-dimensional bound or prove a global lower bound. |
| Comparable-entry/Frobenius premise | **Conditional only.** If it holds on a full \(N\asymp B^2\) block, \(\|K\|_{op}\gg B^{-1}\), short of \(B^{-10/9}\) by \(B^{-1/9}\). The literal complete-symbol lower plateau is unproved. |
| Actual vector versus uniform norm | **Distinguished.** The Frobenius and high-trace barriers concern uniform norm/configuration-separated methods. A conductor-averaged actual vector could in principle avoid the coherent singular directions; its required projection estimate is open. |
| Arbitrary-weight false shadow | **Rejected as proof.** Phase-conjugating arbitrary coefficients trivially saturates a scalar sum, but the report's unconditional obstruction instead uses the exact row change and exact \(q=8\) symbol. |
| Absolute-value false shadow | **Detected.** Taking absolute values across physical/conductor configurations removes the only cancellation not ruled out here and returns capacity. |
| Deligne/Katz trace source map | **Fail literally.** Prime field, bounded-conductor, normal-tuple hypotheses do not cover the moving composite four-row symbol; paired tuples have a main term. |
| Kuznetsov/product large sieve source map | **Fail literally.** One smooth Kloosterman kernel and separated coefficients do not match the varying four-row modulus-dependent coefficient; Cauchy/column freezing recreates capacity. |
| Recent bilinear/dispersion source map | **Fail literally.** The available theorems concern a single \(\mathrm{Kl}_2\) kernel and their own length/coprimality conditions, not the complete trace times joint actual symbol. |
| Downstream scope | **Pass.** No GAR, M9, or final asymptotic claim is changed by this report. |

## 6. Dependencies and artifacts used.

Only the campaign-selected repository context was used:

* `protocol.md`;
* `state/active_campaign.yml`;
* `state/proof_obligations.yml` (the selected campaign obligations);
* `rounds/codex-managed/m9-m1-joint-four-row-spectral-gap/derivation_packet.md`;
* `rounds/codex-managed/m9-canonical-core-formalization/candidates/conductor_canonical_core_statements.md`;
* `rounds/codex-managed/m9-m1-capacity-self-return-fork/synthesis.md`;
* `rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/reports/kloosterman_energy_source_hostile_audit.md`;
* `rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/reports/bad_prime_hostile_source_audit.md`;
* `strategy/conductor_0817_full_proof_strategy.md`;
* the task brief `rounds/codex-managed/m9-m1-joint-four-row-spectral-gap/briefs/joint_gram_source_hostile_audit.md`.

Primary literature checked against the literal hypotheses:

* Jingwei Guo, [*On lattice points in large convex bodies*](https://www.impan.pl/shop/publication/transaction/download/product/81980), Proposition 2.4, *Acta Arith.* 151 (2012), DOI 10.4064/aa151-1-6;
* Étienne Fouvry, Emmanuel Kowalski, and Philippe Michel, [*A study in sums of products*](https://arxiv.org/html/1405.2293v2), Theorem 1.5 and Corollaries 1.6--1.7, arXiv:1405.2293v2;
* Djordje Milićević and Shucheng Zhang, [*Distribution of Kloosterman paths to high prime power moduli*](https://arxiv.org/html/2005.08865v1), Theorem 4, arXiv:2005.08865v1;
* Djordje Milićević, Kam Hung Yau Qin, and Kui Liu Wu, [*Bilinear forms with Kloosterman sums and moments of twisted L-functions*](https://arxiv.org/html/2511.07550v1), Theorem 1.1, arXiv:2511.07550v1;
* Alexandru Pascadi, [*Non-abelian amplification and bilinear forms with Kloosterman sums*](https://arxiv.org/abs/2511.08445v2), arXiv:2511.08445v2;
* Valentin Blomer and Alexandru Pascadi, [*Bilinear forms with Kloosterman sums via quadratic characters*](https://arxiv.org/abs/2607.24311v1), arXiv:2607.24311v1;
* Jean-Marc Deshouillers and Henryk Iwaniec, *Kloosterman sums and Fourier coefficients of cusp forms*, *Invent. Math.* 70 (1982/83), 219--288, as already source-mapped in the selected hostile audit.

The exact Hessian diagonalization, physical-row phase identity, rank-one factorization, \(q=8\) Fourier calculation, and conditional Frobenius estimate were derived algebraically in this audit.  No numerical experiment was used as proof.

## 7. Recommended state effect.

**Retain the canonical hard estimate as open.**  Promote/retain as a no-go the exact separable-self-return lemma: the \((d,u)\) Hessian is congruent to the two one-row Hessians, and a two-dimensional B-process on the complete pre-owner sum reconstructs the physical rows already charged to Schur capacity.  Reject the proposed multiplication of that capacity by a further \(J^{-1/5}\), and reject a direct invocation of Guo after installing the moving trace and hard-owner masks.

**Retain the configuration-separated obstruction.**  Fixed physical configurations are rank-one \((n,m)\) atoms, so high traces taken after configuration separation retain diagonal/backtracking mass.  Retain the exact \(q=8\), \(u=4\) parity mode as a mandatory control for every proposed joint spectral theorem.  Do not promote it to a global lower bound.

**Record, but do not promote, the Frobenius barrier.**  A dense comparable-entry \(N\asymp B^2\) block would force \(\|K\|_{op}\gg B^{-1}\), which cannot reach \(B^{-10/9}\).  The required global comparable-entry plateau is presently unproved.  A useful next hostile task would be to prove or falsify that premise for the literal complete hard symbol.

**Reject the audited source imports as complete proofs.**  Guo covers only the scalar smooth interior; Deligne/Katz product theorems preserve paired main terms and are prime-field statements; Milićević--Zhang has odd-prime/unit/translation-invariance hypotheses and a collision alternative; Kuznetsov and the recent bilinear theorems concern a single separated Kloosterman kernel.  None maps to the full canonical symbol or the \(J^{-1/6}\) target.

The only spectral route not excluded is a new **actual-vector directional** estimate that sums physical and conductor configurations before absolute value and proves small projection onto every surviving paired, parity, modulus-multiple, and transition mode.  It must include a uniform exact-phase/entry-exit packet and pay all mode or residue decompositions within \(J^{1/30}\).  Until such a lemma exists, make no downstream state change.
