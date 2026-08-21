## 1. Result: exact normalization and an equal-capacity no-go

The Gaussian constant in the frozen statement is exact.  If

\[
 K_\alpha(u):={e(\operatorname {sgn}(\alpha)/8)\over\sqrt{2|\alpha|}}
 e\!\left(-{u^2\over4\alpha}\right),\qquad \alpha\ne0,
\]

then, as an oscillatory distribution,

\[
 e(\alpha y^2)=\int_{\mathbb R}K_\alpha(t)e(ty)\,dt.
\]

For \(\alpha_{r,g,k}=rX/(2gk)\), the complete density-plus-discrepancy
coefficient is represented by the single oscillatory distribution

\[
 d\nu_{g,k,x}(\tau)
 :=\mu_R\delta_{J\sqrt x}(d\tau)
 +\sum_{r\ne0}\widehat W_R(r)
 K_{\alpha_{r,g,k}}(J\sqrt x-\tau)\,d\tau .
\]

It gives the exact two-character identity

\[
 e\!\left(-J(\sqrt s-\sqrt h)\sqrt x\right)
 W_R(\Lambda_q/k)
 =\int_{\mathbb R}^{\rm osc}
 e(\tau\sqrt h)e(-\tau\sqrt s)\,d\nu_{g,k,x}(\tau).
\]

The associated Gaussian operator is unitary, with inverse obtained by
replacing \(\alpha\) by \(-\alpha\).  Consequently Gaussian/metaplectic
linearization itself supplies no \(\rho^{-1/2}\) contraction.  It is an
invertible, equal-capacity reparametrization.  A gain can only come from
a new estimate exploiting cancellation in the one actual, fully coupled
symbol; it does not follow from phase separation or Plancherel.

The weakest sufficient transformed estimate is the estimate on that
actual coherent sum alone:

\[
 \tag{TC\(_{\rm act}\)}
 {AD\over H^2}\sum_{a,n}|\mathscr B^{\rm act}_{a,n;H}|^2
 \ll_\varepsilon X^\varepsilon L^4,
\]

where \(\mathscr B^{\rm act}_{a,n;H}\) is defined exactly in Section 2.
This is equivalent, not merely comparable, to the frozen target after
the exact transform.  No proof of \({\rm TC}_{\rm act}\) is furnished by
the Gaussian identity.  Thus the rigorous conclusion is a no-go for a
transform-alone gain, while an actual-symbol two-character estimate
remains logically possible and is precisely the missing lemma.

## 2. Exact statement and hypotheses

Assume the frozen residual block with \(J=X^{1/2}\), \(1\le H\le D\),
\(\rho=AJD^3/L^3>1\), positive \(g,k\), and the literal weight
\(\omega_{a,q,g,k}\).  All residual restrictions, ownership complements,
profiles, signs, orientations, lift support, collars, floors, stars,
entry/exit conditions, and zero extension remain inside this literal
weight and its displayed supports.  The Fourier expansion of \(W_R\)
is used as one complete coefficient and in its asserted oscillatory or
distributional sense; no absolute convergence is assumed.

Put \(q_j=n+j\), \(b_j=a+2q_j\), \(h_g=ga\), and
\(s_{g,j}=gb_j\).  With \(d\nu_{g,k,x}\) as in Section 1, define

\[
\begin{aligned}
 \mathscr B^{\rm act}_{a,n;H}
 := {}&\sum_{0\le j<H}(-1)^j\mathbf 1_{\rm residual}(a,q_j)
 \sum_{\substack{g\ \mathrm{odd}\\ k\in I_{a,q_j}}}
 \omega_{a,q_j,g,k}
 \int_{s_{g,j}/4}^{h_g} A^\circ_{h_g,s_{g,j}}(x)e(kx)\\
 &\hspace{35mm}\times
 \left\{\int_{\mathbb R}^{\rm osc}
 e(\tau\sqrt{h_g})e(-\tau\sqrt{s_{g,j}})
 \,d\nu_{g,k,x}(\tau)\right\}dx .
\end{aligned}
\]

Then

\[
 \mathscr B^{\rm act}_{a,n;H}
 =\sum_{0\le j<H}(-1)^jF_a(n+j)
\]

exactly.  Hence \({\rm TC}_{\rm act}\) is equivalent to

\[
 \mathcal G_H^{\rm act}
 \ll_\varepsilon X^\varepsilon {H^2L^4\over AD}
 \asymp X^\varepsilon {H^2E_0\over\rho}.
\]

Equivalently, if the transformed linear capacity is normalized by

\[
 \mathcal C_H^{\rm act}:={\sqrt{AD}\over H}
 \|\mathscr B^{\rm act}_{\cdot,\cdot;H}\|_{\ell^2(a,n)},
\]

then the weakest sufficient inequality is

\[
 \mathcal C_H^{\rm act}\ll_\varepsilon X^{\varepsilon/2}L^2.
\]

Here the exponent \(\varepsilon/2\) may of course be renamed
\(\varepsilon\).  This formulation asks only for the actual coupled
coefficient.  It asks for neither a per-metric-mode estimate, an
unsigned estimate, nor a coefficient-uniform estimate.

The precise no-go statement is: for every \(\alpha\ne0\), convolution
by \(K_\alpha\) extends to a unitary map on \(L^2(\mathbb R)\), whose
inverse is convolution by \(K_{-\alpha}\).  Therefore no argument using
only this transform, changes of variables, and norm-preserving
orthogonality can reduce a linear capacity by \(\rho^{-1/2}<1\).  This
does not rule out \({\rm TC}_{\rm act}\); it rules out deriving it without
an additional cancellation theorem for the literal moving symbol.

## 3. Proof or derivation

Completing the square gives

\[
 -{t^2\over4\alpha}+ty
 =-{(t-2\alpha y)^2\over4\alpha}+\alpha y^2.
\]

The regularized Fresnel integral is

\[
 \int_{\mathbb R}^{\rm osc}e\!\left(-{u^2\over4\alpha}\right)du
 =\sqrt{2|\alpha|}\,e(-\operatorname {sgn}(\alpha)/8).
\]

Multiplication by
\(e(\operatorname {sgn}(\alpha)/8)/\sqrt{2|\alpha|}\) proves the stated
Gaussian formula, including its sign and its factor \(2\).

Since \(s=gb\) and \(h=ga\),

\[
 {r\Lambda_q\over k}
 ={rX(\sqrt b-\sqrt a)^2\over2k}
 ={rX\over2gk}(\sqrt s-\sqrt h)^2
 =\alpha_{r,g,k}(\sqrt s-\sqrt h)^2.
\]

Writing \(y=\sqrt s-\sqrt h\), multiplying the Gaussian formula by
\(e(-Jy\sqrt x)\), and substituting \(t=J\sqrt x-\tau\) yields

\[
\begin{aligned}
 e(-Jy\sqrt x)e(\alpha y^2)
 &=\int_{\mathbb R}^{\rm osc}
 K_\alpha(J\sqrt x-\tau)e(-\tau y)\,d\tau\\
 &=\int_{\mathbb R}^{\rm osc}
 K_\alpha(J\sqrt x-\tau)
 e(\tau\sqrt h)e(-\tau\sqrt s)\,d\tau.
\end{aligned}
\]

The normalization is especially transparent after \(\tau=J\sigma\).
For \(r\ne0\), using \(J^2=X\),

\[
 K_{\alpha_{r,g,k}}(J\sqrt x-J\sigma)J\,d\sigma
 =e(\operatorname {sgn}(r)/8)\sqrt{gk\over|r|}
 e\!\left(-{gk(\sqrt x-\sigma)^2\over2r}\right)d\sigma.
\]

Before this rescaling the prefactor is exactly

\[
 {1\over\sqrt{2|\alpha_{r,g,k}|}}
 =\sqrt{gk\over |r|X}.
\]

Thus there is no hidden power of \(J\).  With
\(g\asymp L/A\) and \(k\asymp JD/A\), the apparent prefactor is
\(A^{-1}\sqrt{LD/(|r|J)}\); its reciprocal oscillatory width supplies
the compensating factor.  The rescaled prefactor is
\(A^{-1}\sqrt{LJD/|r|}\).  Either coordinate gives the same operator
norm.

For the Fourier convention
\(\widehat f(\xi)=\int f(u)e(-u\xi)du\), the Gaussian identity gives

\[
 \widehat K_\alpha(\xi)=e(\alpha\xi^2).
\]

Consequently, for \(U_\alpha f=K_\alpha*f\),

\[
 \widehat{U_\alpha f}(\xi)=e(\alpha\xi^2)\widehat f(\xi),\qquad
 \|U_\alpha f\|_2=\|f\|_2,qquad
 U_{-\alpha}U_\alpha=I.
\]

Moreover \(K_\alpha\to\delta_0\) in the tempered-distribution sense as
\(\alpha\to0\), because its Fourier multiplier tends pointwise to
\(1\) and is uniformly bounded.  Translation therefore gives
\(K_\alpha(J\sqrt x-\tau)d\tau\to\delta_{J\sqrt x}\).  The metric
density term is exactly this identity operator/atom, with its own
coefficient \(\mu_R\); it is not to be discarded or separately
optimized.

Summing the density atom and every nonzero mode gives \(d\nu\).  Inserting
the preceding identity into the literal \(x,g,k,j\) sum gives
\(\mathscr B^{\rm act}_{a,n;H}=\sum_j(-1)^jF_a(n+j)\).  This proves the
two-character representation without altering its energy.

Finally,

\[
 {E_0\over\rho}\asymp
 {LJD^2\over AJD^3/L^3}={L^4\over AD}.
\]

In the frozen capacity normalization, suppressing harmless
\(X^\varepsilon\) factors,

\[
 \mathcal C_+=L^2\sqrt\rho,\qquad
 {\mathcal C_+^2\over AD}={L^4\rho\over AD}=LJD^2\asymp E_0,
\]

whereas the target requires

\[
 \mathcal C_{\rm req}=L^2,\qquad
 {\mathcal C_{\rm req}^2\over AD}={L^4\over AD}
 \asymp {E_0\over\rho}.
\]

Thus the required energy improvement is exactly \(\rho^{-1}\), and the
required linear-capacity improvement is exactly \(\rho^{-1/2}\).  Since
each Gaussian factor has operator norm one and exact inverse, the
transform returns \(\mathcal C_+\), not \(\mathcal C_{\rm req}\), unless
one proves new cancellation in the coherent actual-symbol sum.

The phase is separated but the coefficient is not: the moving interval
\(I_{a,q}\), the \(x\)-limits, \(A^\circ_{h,s}(x)\), \(\omega_{a,q,g,k}\),
and \(d\nu_{g,k,x}\) all couple \(h\) and \(s\).  Treating the two
characters as independent sequences would therefore be an additional
decoupling assertion, not a consequence of Gaussian linearization.

## 4. First doubtful or unproved step

The first unproved step is precisely \({\rm TC}_{\rm act}\), or any
claim that separated radical characters are orthogonal strongly enough
to replace \(L^2\sqrt\rho\) by \(L^2\).  Neither the Fresnel identity nor
Plancherel supplies this.  In particular, the moving owners and
amplitudes prevent the displayed expression from being a product of an
\(h\)-only coefficient and an \(s\)-only coefficient.  A valid next
lemma would have to identify an exact cancellation of the literal
\(\Phi/\chi_4\)-type symbol (as retained inside \(\omega\)), uniformly for
\(1\le H\le D\), while keeping density and all discrepancies coherent.

There is no doubtful algebraic step in the transform/no-go itself when
the asserted Fourier expansion is interpreted through finite symmetric
mode truncation and the standard oscillatory limit.  Passing from that
identity to a \(\rho^{-1/2}\) gain is the unsupported step.

## 5. Control tests and outcomes

- **`gaussian_constant_and_density_limit`.**  Exact input: the frozen
  \(e\)-normalization, arbitrary real \(\alpha\ne0\), and
  \(t=J\sqrt x-\tau\).  Expected invariant: the Fresnel constant must
  cancel exactly and the kernels must tend to the density atom.
  Outcome: the integral is
  \(\sqrt{2|\alpha|}e(-\operatorname {sgn}(\alpha)/8)\), so the frozen
  prefactor is exact; \(\widehat K_\alpha=e(\alpha\xi^2)\) and hence
  \(K_\alpha(J\sqrt x-\tau)d\tau\to\delta_{J\sqrt x}\).
  Implication: the density mode is the identity atom and there is no
  missing factor of \(2\), \(J\), or a conjugated sign.

- **`metric_density_discrepancy_jointness`.**  Exact input:
  \(W_R(t)=\mu_R+\sum_{r\ne0}\widehat W_R(r)e(rt)\).  Expected failure:
  estimating \(\mu_R\) and the nonzero modes as unrelated positive
  quantities discards their cross terms.  Outcome: they combine into
  the one distribution \(d\nu_{g,k,x}\), and the transformed row is
  exactly the original complete coefficient.  Implication:
  \({\rm TC}_{\rm act}\) must be stated for the coherent full mode sum;
  no separate density/discrepancy gain has been inferred.

- **`actual_symbol_vs_arbitrary_coefficients`.**  Exact input: the
  literal \(\omega\), moving supports, signed alternating row, and
  actual amplitudes.  Expected failure: an unsigned or arbitrary
  bounded-coefficient analogue is not a valid positive premise.
  Outcome: \({\rm TC}_{\rm act}\) quantifies only the one actual symbol;
  no coefficient-adversary estimate is used.  The unitary no-go is an
  operator statement about what the transform alone can do, not a claim
  that the actual symbol cannot cancel.  Implication: a future gain must
  exhibit where the literal signs and profiles enter.

- **`transform_inversion_and_capacity`.**  Exact input: convolution by
  \(K_\alpha\), including its full oscillatory range and normalization.
  Expected invariant: an exact metaplectic change of coordinates should
  preserve \(L^2\) capacity and admit inversion.  Outcome:
  \(U_\alpha^*=U_{-\alpha}=U_\alpha^{-1}\) and
  \(\|U_\alpha\|_{2\to2}=1\).  The apparent factor
  \(\sqrt{gk/(|r|X)}\) is exactly balanced by scale/Jacobian.  Implication:
  transform plus Plancherel returns equal capacity; a strict
  \(\rho^{-1/2}\) gain requires a separate restriction/correlation
  estimate.

- **`rho_power_and_endpoint_ledger`.**  Exact input:
  \(J=X^{1/2}\), \(E_0\asymp LJD^2\),
  \(\rho=AJD^3/L^3\), and the three required values of \(D\).  Expected
  invariant: the linear and energy savings must remain respectively
  \(\rho^{-1/2}\) and \(\rho^{-1}\), with no endpoint-created Gaussian
  saving.  The exact ledger is

  \[
  \begin{array}{c|c|c|c|c}
  D&\rho&E_0&E_0/\rho&\sqrt{E_0/\rho}\\ \hline
  X^{1/4}&AX^{5/4}/L^3&LX&L^4/(AX^{1/4})&L^2/(\sqrt A X^{1/8})\\
  X^{3/8}&AX^{13/8}/L^3&LX^{5/4}&L^4/(AX^{3/8})&L^2/(\sqrt A X^{3/16})\\
  X^{1/2}&AX^2/L^3&LX^{3/2}&L^4/(AX^{1/2})&L^2/(\sqrt A X^{1/4})
  \end{array}
  \]

  up to the asserted comparability in \(E_0\).  At \(H=D\), the target
  energy is \(H^2E_0/\rho\asymp L^4D/A\).  Outcome: all three endpoints
  demand the same relative \(\rho^{-1}\) energy improvement, including
  \(D=X^{1/2}\).  Implication: Gaussian separation creates no legal
  endpoint shortcut.

No numerical experiment was used; all five controls were algebraic.

## 6. Dependencies and exact artifacts used

Only the following statement-only artifacts were read and used:

1. `problems/gauss_circle.md`.
2. `state/control_models.md`.
3. `rounds/codex-managed/m9-m2-metaplectic-two-character-energy/blind_statement.md`.
4. `rounds/codex-managed/m9-m2-metaplectic-two-character-energy/briefs/blind_two_character_energy_rederivation.md`.

No proof graph, proof draft, strategy file, derivation packet, candidate,
earlier report, sibling report, web source, or shared-state artifact was
consulted.  The derivation depends only on the standard regularized
Fresnel integral, Plancherel, and the formulas asserted in those four
artifacts.

## 7. Recommended state effect

**Revise.**  Retain the exact Gaussian constant, density atom, coherent
distribution \(d\nu\), and two-character identity.  Promote, subject to
the conductor's seam checks, the unitary equal-capacity no-go: exact
Gaussian/metaplectic separation alone cannot supply the missing
\(\rho^{-1/2}\) linear gain.  Reject any inference of the target from
phase separation or the visible Gaussian prefactor alone.  Keep the
main energy target open, with \({\rm TC}_{\rm act}\) recorded as the
weakest sufficient additional lemma and with arbitrary-coefficient,
unsigned, or separately estimated density/discrepancy substitutes
explicitly inadmissible.
