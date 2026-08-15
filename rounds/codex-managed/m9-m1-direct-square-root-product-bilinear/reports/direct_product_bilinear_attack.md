# 1. Result

I do not prove the direct \(Q^{3/2}\) estimate and I find no
actual-symbol counterexample. I prove instead a precise route no-go:
two-dimensional Poisson summation of the actual direct bilinear is a
coefficient-preserving return to a fixed-centre near-product wavelet.
The Jacobian, character transform, Gaussian unit, one-sided cone, and
summed stationary remainder can all be kept. If \(J=X^{1/2}\) and
\(T=J/Q\), the returned sum has target \(J^{1/2}\), absolute capacity
\(T\), and hence the exact unsaved factor

\[
 \frac{T}{J^{1/2}}=\frac{J^{1/2}}{Q}.
\]

At \(Q=X^{1/5}\) this is \(X^{1/20}\). Thus the proposed direct
two-dimensional transform is an \(H/L\) self-return, not a new saving.
The same computation identifies the narrow remaining statement: a
signed, one-sided, fixed-centre character-divisor wavelet estimate.
Product squares, fourth powers, and exact rational stationary aliases
are all below the target and give no counterexample.

# 2. Exact statement and hypotheses

Write \(e(t)=e^{2\pi i t}\), \(J=X^{1/2}\), and \(T=J/Q\). Assume the
fixed-interior range \(1\ll Q\leq J^{1-\delta}\), with fixed
\(\delta>0\). Let
\(\beta\in C_c^\infty((0,\infty))\),
\(\Xi\in C_c^\infty((0,1))\), and retain the actual Round-68 symbol

\[
 C(y)=y^{3/4}\Xi(2\sqrt y).
\]

All supports are fixed and bounded away from their endpoints. Define

\[
 \mathcal T_Q=\sum_k\sum_{q\in\mathbb Z}\chi_4(q)
 \beta(k/Q)C(k/q)e(J\sqrt{kq}),
 \qquad
 K_\beta(z)=\int_0^\infty t^{1/2}\beta(t)e(zt)\,dt,
\]

where the smooth amplitude is extended by zero away from positive
\(k,q\). Put

\[
 \mathcal W_Q=
 \sum_{m\geq1}\ \sum_{\substack{r\geq1\\ r\ \mathrm{odd}}}
 \chi_4(r)\Xi(J/m)
 K_\beta\!\left(\frac{m}{J}\frac{X-mr}{T}\right).
\tag{2.1}
\]

Then the fixed-interior two-dimensional character-Poisson transform has
the asymptotic

\[
 \boxed{
 \mathcal T_Q=e(1/8)\frac{Q^{3/2}}{J^{1/2}}\mathcal W_Q
 +O_{\beta,\Xi,\delta,\varepsilon}
   ((QJ)^{-1/2}X^\varepsilon).}
\tag{2.2}
\]

Formula \((2.2)\) is not obtained by discarding all lower stationary terms.
More exactly, for every \(R\geq1\) the right side has a classical-symbol
expansion

\[
 e(1/8)\frac{Q^{3/2}}{J^{1/2}}
 \left(\mathcal W_Q+
 \sum_{1\leq \ell<R}(QJ)^{-\ell}\mathcal W_{Q,\ell}\right)
 +O_R((QJ)^{1/2-R}X^\varepsilon),
\tag{2.3}
\]

where every \(\mathcal W_{Q,\ell}\) has the same \(m,r\) support as
\((2.1)\), but with a kernel uniformly Schwartz in
\((m/J)(X-mr)/T\), and

\[
 |\mathcal W_{Q,\ell}|\ll_{\ell,A}TX^\varepsilon.
\tag{2.4}
\]

Taking \(R=1\) gives \((2.2)\). In particular the desired direct theorem is
equivalent, up to a negligible proved remainder, to

\[
 \boxed{\mathcal W_Q\ll_{\varepsilon,\beta,\Xi}J^{1/2}X^\varepsilon.}
\tag{WPB}
\]

The support in \((2.1)\) has \(m>J\), \(r<J\), and
\(mr=X+O(TX^\varepsilon)\); it is the transformed form of the original
fixed cone \(q>4k\), not a completed \(r_2/4\) convolution.

# 3. Proof or derivation

First, the Round-69 normalization is exact. If the wavelet coefficient
before absorbing the \(k\)-factor is
\(b_k=Q^{-1}\beta_0(k/Q)\), then \((69.3)\) gives

\[
 \sum_k b_k S_k
 =\mathfrak u\frac{\sqrt J}{Q}
 \sum_k k^{-1/2}\beta_0(k/Q)P_k+\text{accepted errors}
 =\mathfrak u\frac{\sqrt J}{Q^{3/2}}\mathcal T_Q
 +\text{accepted errors},
\]

after replacing \(\beta_0(t)\) by \(t^{-1/2}\beta_0(t)\). This proves
the factor \(\sqrt J/Q^{3/2}\), with no Cauchy step.

For the new transform, the exact Gauss-Poisson identity, in the Fourier
convention
\(\widehat F(\xi)=\int F(y)e(-\xi y)\,dy\), is

\[
 \sum_{q\in\mathbb Z}\chi_4(q)F(q)
 =\frac{i}{2}\sum_{\substack{r\in\mathbb Z\\r\ \mathrm{odd}}}
 \chi_4(r)\widehat F(r/4).
\tag{3.1}
\]

Indeed,
\(\sum_{a\bmod4}\chi_4(a)e(ar/4)=2i\chi_4(r)\).
Ordinary Poisson summation in \(k\), followed by \((3.1)\), gives the exact
integral identity

\[
 \mathcal T_Q=\frac{i}{2}\sum_m
 \sum_{r\ \mathrm{odd}}\chi_4(r)I_{m,r},
\]

\[
 I_{m,r}=\iint \beta(x/Q)C(x/y)
 e\!\left(J\sqrt{xy}-mx-\frac r4y\right)dx\,dy.
\tag{3.2}
\]

Use the homogeneous coordinates

\[
 x=\frac{Qu}{v},\qquad y=Qu,\qquad
 \left|\frac{\partial(x,y)}{\partial(u,v)}\right|
 =\frac{Q^2u}{v^2}.
\tag{3.3}
\]

Thus

\[
 I_{m,r}=Q^2\iint \frac{u}{v^2}\beta(u/v)C(1/v)
 e\{Qu\Psi_{m,r}(v)\}\,du\,dv,
\]

\[
 \Psi_{m,r}(v)=Jv^{-1/2}-mv^{-1}-\frac r4.
\tag{3.4}
\]

All stationary aliases are now visible. A stationary point in \(v\)
exists only for \(m>0\), and it is

\[
 v_0=\frac{4m^2}{X},\qquad
 \Psi''_{m,r}(v_0)=-\frac{J}{4v_0^{5/2}},\qquad
 \Psi_{m,r}(v_0)=\frac{X-mr}{4m}.
\tag{3.5}
\]

Equivalently, if the dual \(q\)-frequency is
\(\eta=r/4\in\mathbb Z\pm1/4\), the full homogeneous saddle is
\(4m\eta=X\). Its uncertainty is

\[
 |4m\eta-X|=|mr-X|\ll\frac{J}{Q}=T.
\tag{3.6}
\]

This is the claimed angular relation \(J=2\sqrt{m\eta}\), up to the
wavelet width.

One-dimensional stationary phase in \(v\), with the \(e(t)\)
normalization, contributes \(e(-1/8)\) and

\[
 2v_0^{5/4}(QuJ)^{-1/2}.
\]

Multiplying the Jacobian amplitude in \((3.3)\), and then setting
\(u=v_0t\), makes the leading part of \((3.2)\)

\[
 2e(-1/8)\frac{Q^{3/2}}{J^{1/2}}
 v_0^{3/4}C(1/v_0)
 K_\beta\!\left(\frac{Qm(X-mr)}{X}\right).
\tag{3.7}
\]

The actual symbol, rather than a generic moving symbol, is decisive in
the exact simplification

\[
 v_0^{3/4}C(1/v_0)
 =\Xi(2/\sqrt{v_0})=\Xi(J/m),
\]

and

\[
 \frac{Qm(X-mr)}{X}=\frac{m}{J}\frac{X-mr}{T}.
\]

Finally, \((i/2)\cdot2e(-1/8)=e(1/8)\), proving the leading term in
\((2.2)\).

Here is the required summed-remainder audit. Put
\(M=m/J\), \(R_0=r/J\), and \(\lambda=QJ\). On the fixed compact
angular support the phase in \((3.4)\), divided by \(J\), has a unique
nondegenerate \(v\)-critical point \(4M^2\), independent of \(u\) and
\(R_0\). The parameter-dependent Morse lemma therefore writes the local
phase exactly as its critical value minus a smooth square. Stationary
phase gives a full classical symbol in \(\lambda^{-1}\), whose
coefficients and all \(u,M\) derivatives are bounded. Since the
\(r\)-dependence occurs only through the factor

\[
 e\!\left(uQ\frac{X-mr}{4m}\right),
\]

the subsequent compact \(u\)-integral turns every coefficient and the
symbol remainder into a uniformly Schwartz function of
\((m/J)(X-mr)/T\). Away from the angular saddle, repeated integration
by parts has the same property. For every such Schwartz kernel \(H\),
the elementary divisor estimate gives

\[
 \sum_{m\asymp J}\sum_{r\asymp J}
 \left|H\!\left(\frac{m}{J}\frac{X-mr}{T}\right)\right|
 \ll_A TX^\varepsilon.
\tag{3.8}
\]

To see \((3.8)\), group by the integer product \(n=mr\), split
\(|n-X|/T\) into unit intervals, and use
\(d(n)\ll_\varepsilon n^\varepsilon\). The first omitted symbol term
therefore has total size

\[
 \frac{Q^{3/2}}{J^{1/2}}(QJ)^{-1}T X^\varepsilon
 =(QJ)^{-1/2}X^\varepsilon,
\]

and higher terms give \((2.3)\). Thus no unjustified claim that a single
stationary term has an \(O_A(Q^{-A})\) cellwise remainder is being made;
the full symbol and the product count are both necessary.

Taking absolute values in \((2.1)\) and using \((3.8)\) gives

\[
 |\mathcal W_Q|\ll TX^\varepsilon,\qquad
 |\mathcal T_Q|\ll (QJ)^{1/2}X^\varepsilon.
\tag{3.9}
\]

At \(Q=X^{1/5}\), \((3.9)\) is \(X^{7/20+\varepsilon}\), whereas the target
is \(X^{3/10+\varepsilon}\). The ratio is \(X^{1/20}\). This absolute
capacity is real for the actual class: choose admissible nonnegative
\(\beta,\Xi\) with \(K_\beta(0)\ne0\), and average \(X\) over a fixed
dyadic interval. Each of \(\asymp J^2\) admissible odd pairs \((m,r)\)
contributes an \(X\)-interval of length \(\asymp T\) on which
\(|K_\beta|\) is bounded below. Dividing the total incidence measure
\(\asymp J^2T\) by the \(X\)-interval length \(\asymp J^2\) shows that
for some \(X\) the unsigned actual-profile mass is \(\gg T\). Hence an
absolute-value proof cannot remove the missing factor.

Product grouping gives exactly

\[
 \mathcal T_Q=\sum_{n\asymp Q^2}A_Q(n)e(J\sqrt n),
 \qquad
 A_Q(n)=\sum_{kq=n}\chi_4(q)\beta(k/Q)C(k/q).
\tag{3.10}
\]

The divisor bound in \((3.10)\) gives only \(Q^{2+\varepsilon}\).
Mellin-inverting the two smooth factors yields, in absolute convergence,
a rapidly convergent superposition of Dirichlet series of the form

\[
 Q^w\zeta(s+w+z)L(s-z,\chi_4).
\tag{3.11}
\]

The \(w,z\) modes encode the moving \(k\)-cutoff and one-sided angular
projector. Completing \((3.11)\) therefore reflects or completes the
angular sector; it does not estimate the retained sector. At
\(w=z=0\) it is the complete \(r_2/4\) convolution and the accepted
Hardy return, not a bound for \((3.10)\). The direct Poisson computation
above is the physical-space manifestation of this same return.

Nor does ordinary two-dimensional differencing supply a hidden
curvature saving. For \(F(k,q)=J\sqrt{kq}\),

\[
 \det D^2F=0
\tag{3.12}
\]

identically: the two diagonal second derivatives have product
\(J^2/(16kq)\), exactly the square of the mixed derivative. The null
direction is forced by degree-one homogeneity and contains the product
fibres. Cauchy in \(k\) instead asks for
\(\sum_k|P_k|^2\ll Q^2X^\varepsilon\), precisely the unresolved
Round-68 lossless energy theorem. Thus product grouping,
two-dimensional differencing, direct Poisson, and the
\(\zeta L(\chi_4)\) convolution all encounter the same first signed
near-product estimate.

# 4. First doubtful or unproved step

The first unproved step is exactly \((\mathrm{WPB})\), with the character retained
outside every absolute value:

\[
 \sum_{m\ge1}\sum_{r\ \mathrm{odd}}\chi_4(r)\Xi(J/m)
 K_\beta\!\left(\frac{m}{J}\frac{X-mr}{T}\right)
 \ll J^{1/2}X^\varepsilon.
\]

The proved divisor envelope is \(TX^\varepsilon\), so the first exact
deficit is \(T/J^{1/2}=J^{1/2}/Q\), not a stationary-phase remainder or
a missing constant. Period-four cancellation would have to control a
fixed-centre signed union of the near-product incidences; pairing or
absolute values reconstructs the Round-64/65 product-wavelet
functional. I have neither proved this signed estimate nor produced a
signed lower bound that violates it.

# 5. Required control test and outcome

- **Direct normalization:** pass; the factor is
  \(\sqrt J/Q^{3/2}\), derived before Cauchy.
- **Actual wavelet symbol:** pass; the factor
  \(v_0^{3/4}C(1/v_0)\) cancels exactly to \(\Xi(J/m)\). An arbitrary
  moving symbol was not substituted.
- **One-sided cone:** pass; \(q>4k\) becomes the fixed dual sector
  \(m>J>r\), up to the fixed support margins. It is never completed to
  \(r_2/4\).
- **Product grouping:** pass algebraically by \((3.10)\); the divisor
  envelope is \(Q^{2+\varepsilon}\) and supplies no target bound.
- **Perfect powers:** pass analytically. For any square class \(a\),
  the number of admissible pairs with \(kq=a\ell^2\asymp Q^2\) is
  \(O_\varepsilon(Q^{1+\varepsilon})\), since there are \(O(Q)\)
  possible products and \(d(n)\ll n^\varepsilon\). Product fourth
  powers contribute only \(O_\varepsilon(Q^{1/2+\varepsilon})\).
  Hence even complete phase coherence on these fibres is below
  \(Q^{3/2}\).
- **Stationary aliases and rational resonance:** pass. The complete
  dual set is \(m>0\), \(r>0\) odd, or equivalently
  \(\eta=r/4\in\mathbb Z\pm1/4\). Exact resonance is \(mr=X\) and has
  divisor-bounded multiplicity \(X^\varepsilon\) when it exists. The
  full near band \(|mr-X|\ll T\), not merely exact products, is the open
  signed object.
- **Remainder audit:** pass only after retaining the full stationary
  symbol. The lower terms sum as in \((2.3)\)--\((3.8)\); a bare leading-term
  assertion with a cellwise \(O_A(Q^{-A})\) remainder would be invalid.
- **Direct versus energy capacity:** pass. The direct target is weaker
  before Cauchy, but double Poisson turns it into \((\mathrm{WPB})\); Cauchy turns it
  into the stronger open \(Q^2\) energy theorem. Neither operation gives
  a saving.
- **Source applicability:** no external theorem is imported. The
  \(\zeta L(\chi_4)\) factorization is derived in its half-plane of
  absolute convergence and is used only as structural algebra.
- **Full-cone and downstream scope:** pass. All claims here are for the
  fixed smooth interior. Cone edges, sharp saddle transitions, negative
  branches, the remaining radial sectors, GAR, M9-M1, M9, and the
  Gauss-circle exponent remain open.

# 6. Dependencies and exact artifacts used

- `protocol.md`;
- `state/proof_obligations.yml`, especially the accepted nodes
  `M9-M1-reciprocal-product-wavelet-reduction`,
  `M9-M1-product-wavelet-affine-Abel-reduction`,
  `M9-M1-joint-reciprocal-energy-Bprocess-reduction`, and
  `M9-M1-square-root-product-energy-involution`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-direct-square-root-product-bilinear/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-joint-reciprocal-large-sieve/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-joint-reciprocal-large-sieve/synthesis.md`;
- `rounds/codex-managed/m9-m1-square-root-product-offdiagonal/actual_symbol_addendum.md`;
- `rounds/codex-managed/m9-m1-square-root-product-offdiagonal/reports/conductor_two_step_involution.md`;
- `rounds/codex-managed/m9-m1-square-root-product-offdiagonal/reviews/conductor_offdiagonal_adjudication.md`;
- `rounds/codex-managed/m9-m1-square-root-product-offdiagonal/synthesis.md`.

No Round-69 sibling report, external source, or numerical experiment was
used. The work is entirely analytical/algebraic.

# 7. Recommended state effect

Promote a narrowly scoped proved-internal reduction/no-go, suggested ID
`M9-M1-direct-product-wavelet-self-return`: on fixed smooth positive
ratio support, exact two-dimensional character-Poisson summation and a
summed full stationary-symbol expansion send the actual direct
square-root-product bilinear to \((2.1)\) with the factor
\(e(1/8)Q^{3/2}J^{-1/2}\); absolute closure gives only
\((QJ)^{1/2}X^\varepsilon\) and loses \(J^{1/2}/Q\).

Retain the direct \(Q^{3/2}\) theorem, \((\mathrm{WPB})\), GAR, M9-M1, M9, and the
exponent open. The next useful analytic target is \((\mathrm{WPB})\) itself, or its
exact period-four unmatched-crossing form, with the \(\chi_4(r)\) sign
kept before absolute values. Do not repeat two-dimensional Poisson,
complete the one-sided coefficient to \(r_2/4\), infer a bound from the
zero Hessian determinant, or promote this fixed-interior return to the
full cone.
