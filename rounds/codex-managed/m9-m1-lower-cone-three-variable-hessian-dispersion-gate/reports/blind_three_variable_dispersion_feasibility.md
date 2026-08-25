# Statement-only three-variable dispersion feasibility report

## 1. Result: exact Hessian, but a Hessian-only no-go

The literal phase

\[
f(t,d,e)=\sqrt N\,t\sqrt{de}
\]

does have a uniformly nondegenerate three-variable scaled Hessian: its determinant is exactly \(1/4\). The exact \(hr=st^2\) parametrization is also multiplicity one, and the opened coefficient is divisor-bounded. These facts do **not** yield a lawful estimate for the stated scalar.

The result of this blind rederivation is the following precise method no-go.

> **Three-variable Hessian-only no-go.** Under only the hypotheses in the statement, no argument can obtain a power saving merely from the nonzero scaled Hessian while either (i) treating the opened coefficient as an arbitrary divisor-bounded coefficient, or (ii) treating it and the nearest-square mask as a smooth separable amplitude. The first interpretation is refuted by the adversarial-coefficient control, and the second does not satisfy the amplitude hypotheses. Moreover, any three-variable theorem requiring all three side lengths to grow leaves the admissible \(t=1\) and bounded-\(t\) faces, whose available absolute price is \(X^\varepsilon M^{1/4}/T\), hence \(X^\varepsilon M^{1/4}\) at \(T=1\). The fixed-\(t\) \(d,e\) Hessian has determinant zero. Thus absolute disposal of the complement is not target-safe.

There are target-safe edge pieces: \(T\asymp M^{1/4}\) is safe by capacity alone, \(E=1\) is empty, and a fixed bounded-\(E\) face is forced by the cone to lie at \(T\asymp_E M^{1/4}\). These facts do not make the low-\(T\) complement safe. Consequently this report proves neither the desired \(O_{\varepsilon,V}(X^\varepsilon)\) estimate nor an owner-complete strict intermediate-\(t\) reduction. It does not assert that the exact signed scalar is large; the obstruction is to the proposed Hessian-only proof mechanism.

## 2. Exact statement and hypotheses

Put \(m=t^2de\), and define the literal mask and profile weight

\[
\mathfrak M_M(t,d,e)
=\mathbf 1_{\left|\lfloor f(t,d,e)+\tfrac12\rfloor^2-Nt^2de\right|>M^{3/4}},
\qquad
w_M(m)=m^{-3/4}V_{\rm low}(R^2m/N).
\]

For positive integers \(t,d,e\), define

\[
\begin{aligned}
\mathcal A(t,d,e)
={}&\mathbf 1_{de\ {\rm squarefree}}\mathbf 1_{e\ {\rm odd}}\chi_4(e)\\
&\times
\sum_{\substack{\gamma\mid t,\ \gamma\ {\rm squarefree\ and\ odd}\\
(\gamma,de)=1}}
\chi_4(\gamma)
\sum_{\substack{ab=t/\gamma,\ b\ {\rm odd}\\
eb^2>4da^2}}1 .
\end{aligned}
\]

Then the starting scalar is exactly

\[
\sum_M\sum_{t,d,e\geq1}
\mathbf 1_{t<M^{1/4}}
\mathbf 1_{de>M^{1/2}}
\mathbf 1_{M\leq t^2de<B_M}
\mathfrak M_M(t,d,e)w_M(t^2de)
\mathcal A(t,d,e)e(f(t,d,e)).                                      \tag{2.1}
\]

All inequalities in (2.1) are literal; in particular the block is half-open, the \(t\)-cutoff and cone are strict, and no collar at the nearest-square boundary has been removed.

The proved assertions are:

1. The coefficient formula above is multiplicity one and

   \[
   |\mathcal A(t,d,e)|\leq d_3(t)\ll_\varepsilon t^\varepsilon.
   \]

2. With \(L=\operatorname{diag}(t,d,e)\),

   \[
   f^{-1}L(\nabla^2f)L
   =\begin{pmatrix}
   0&1/2&1/2\\
   1/2&-1/4&1/4\\
   1/2&1/4&-1/4
   \end{pmatrix},
   \qquad \det=\frac14.                                           \tag{2.2}
   \]

3. On a nonempty dyadic box \(t\asymp T,d\asymp D,e\asymp E\),

   \[
   T^2DE\asymp M,
   \qquad
   |S_{M,T,D,E}|_{\rm abs}
   \ll_{\varepsilon,V}X^\varepsilon\frac{M^{1/4}}{T}.             \tag{2.3}
   \]

4. A coefficient-blind estimate with a genuine phase saving is impossible for arbitrary bounded coefficients; a smooth-amplitude estimate is not applicable to the exact \(\mathcal A\mathfrak M_M\) without a new coefficient, cone, endpoint, and mask-boundary argument. A theorem requiring \(T,D,E\to\infty\) is not owner-complete because of the bounded-\(t\) face.

No unquoted exponential-sum theorem, averaging in \(N\), conjugate pairing, or replacement of the exact coefficient is assumed.

## 3. Proof and derivation

**Multiplicity-one coefficient reconstruction.** Start from one pair \(h,r\geq1\) with \(hr=st^2\), where \(s\) is squarefree. For a prime \(p\mid s\), the two valuations \(v_p(h),v_p(r)\) have opposite parity. Put \(p\) in \(d\) if \(v_p(h)\) is odd and in \(e\) if \(v_p(r)\) is odd. This gives \(de=s\). For \(p\nmid s\), the two valuations have the same parity; put \(p\) in \(\gamma\) exactly when both are odd. Thus \(\gamma\) is squarefree, \((\gamma,s)=1\), and \(\gamma\mid t\). The quotients

\[
a^2=\frac{h}{d\gamma},\qquad b^2=\frac{r}{e\gamma}
\]

are squares, and \(ab=t/\gamma\). Conversely, these data reconstruct

\[
h=d\gamma a^2,\qquad r=e\gamma b^2
\]

uniquely. Hence there is neither loss nor overcounting. The condition that \(r\) is odd is exactly that \(e,\gamma,b\) are odd. Then

\[
\chi_4(r)=\chi_4(e\gamma b^2)=\chi_4(e)\chi_4(\gamma),
\]

and \(r>4h\) is exactly \(eb^2>4da^2\). This proves (2.1), including squarefreeness, the induced coprimality \((d,e)=1\), the additional coprimality \((\gamma,de)=1\), parity, character, and strict cone. For fixed \(t,d,e\),

\[
|\mathcal A(t,d,e)|
\leq\sum_{\gamma\mid t}\tau(t/\gamma)
=d_3(t),                                                         \tag{3.1}
\]

with every omitted restriction only decreasing the right side.

**Complete Hessian.** The first and second derivatives are

\[
f_t=\frac ft,\quad f_d=\frac f{2d},\quad f_e=\frac f{2e},
\]

\[
f_{tt}=0,\quad f_{td}=\frac f{2td},\quad f_{te}=\frac f{2te},
\quad f_{dd}=-\frac f{4d^2},\quad f_{de}=\frac f{4de},
\quad f_{ee}=-\frac f{4e^2}.
\]

This gives (2.2). Expanding its determinant gives \(1/4\); its eigenvalues are
\(-1/2,1/\sqrt2,-1/\sqrt2\). In unscaled coordinates,

\[
\det\nabla^2f
=\frac{f^3}{4t^2d^2e^2}
=\frac{N^{3/2}t}{4\sqrt{de}}.                                    \tag{3.2}
\]

Thus the algebraic nondegeneracy is genuine and indefinite. It is nevertheless lost on a fixed-\(t\) face: the scaled \(d,e\) Hessian is

\[
\begin{pmatrix}-1/4&1/4\\1/4&-1/4\end{pmatrix},
\qquad \det=0.                                                    \tag{3.3}
\]

On a fixed-\(d\) face the remaining \(t,e\) matrix has determinant \(-1/4\), so a separate two-variable theorem could in principle apply when both of those sides grow; it is not a three-variable estimate and it still has to own the exact coefficient and mask.

**Dyadic capacity and aspect ratios.** A nonempty box meeting \(M\leq t^2de<B_M\leq2M\) has \(T^2DE\asymp M\). It contains at most \(O(TDE)=O(M/T)\) triples. Equations (3.1) and \(m\asymp M\) therefore give

\[
M^{-3/4}\frac MT\,X^\varepsilon
=X^\varepsilon\frac{M^{1/4}}T,
\]

which is (2.3). The logarithmically many choices of dyadic sides and blocks are absorbed into \(X^\varepsilon\). This is an upper capacity, not a lower bound for the signed scalar.

The cone sharpens the aspect ledger. Since \(ab=t/\gamma\),

\[
\frac ba\leq ab=\frac t\gamma\leq t.
\]

Consequently every surviving coefficient summand obeys

\[
et^2>4d.                                                          \tag{3.4}
\]

In dyadic notation this implies \(D\ll ET^2\), and together with \(DE\asymp M/T^2\) it gives

\[
D\ll M^{1/2},\qquad E\gg \frac{M^{1/2}}{T^2},                     \tag{3.5}
\]

up to harmless box constants. This necessary condition is not sufficient, because an admissible factorization \(ab=t/\gamma\) is still required.

The individual short faces are as follows.

- \(T\asymp M^{1/4}\): (2.3) is already \(O(X^\varepsilon)\) per box. No Hessian gain is needed.
- \(E=1\): (3.4) gives \(d<t^2/4\), hence \(m=dt^2<t^4/4<M/4\), contradicting \(m\geq M\). This face is empty.
- \(1\leq e\leq K\): from \(M\leq m<e^2t^4/4\),

  \[
  t>\frac{\sqrt2\,M^{1/4}}{\sqrt e},\qquad
  \frac{M^{1/4}}t<\sqrt{e/2}\leq\sqrt{K/2}.                       \tag{3.6}
  \]

  Thus each fixed bounded-\(E\) face is forced to the target-safe upper-\(t\) region. This does not cover growing but short \(E\).
- \(D=1\): there is no corresponding exclusion. In particular, at \(t=d=1\),

  \[
  \mathcal A(1,1,e)
  =\mathbf1_{e\ {\rm squarefree\ and\ odd}}\chi_4(e)\mathbf1_{e>4},
  \]

  before the profile and nearest-square mask. Hence the \(D=1\) face is structurally present. If \(T\) grows it is a two-variable \(t,e\) problem; if \(T=1\) it is one-dimensional.
- \(t=1\): necessarily \(\gamma=a=b=1\), so exactly

  \[
  \mathcal A(1,d,e)
  =\mathbf1_{de\ {\rm squarefree}}\mathbf1_{e\ {\rm odd}}
   \chi_4(e)\mathbf1_{e>4d}.                                     \tag{3.7}
  \]

  This is not an empty boundary. Its available box price is \(X^\varepsilon M^{1/4}\), and (3.3) shows that the three-variable curvature cannot be inherited after \(t\) is frozen. The same issue persists for any bounded number of \(t\)-slices.

The retained condition \(de>M^{1/2}\) is consistent with this ledger and in fact follows strictly from \(m\geq M\) and \(t<M^{1/4}\): \(de=m/t^2>M^{1/2}\).

**Literal mask, profile, and endpoints.** Write

\[
k=\lfloor f+1/2\rfloor,\qquad \rho=f-k\in[-1/2,1/2).
\]

Then

\[
k^2-f^2=-\rho(2f-\rho),
\qquad
\mathfrak M_M=\mathbf1_{|\rho|>M^{3/4}/(2f-\rho)}.                \tag{3.8}
\]

Since \(f\asymp\sqrt{NM}\), the excluded collar has fractional-phase thickness comparable to \(M^{1/4}/\sqrt N\). Formula (3.8) is a discontinuous arithmetic cutoff. It depends only on \(m=t^2de\), but that does not make it smooth in \(t,d,e\). The half-open block \(M\leq m<B_M\), the terminal endpoint \(B_M\), the strict \(t\)-cutoff, and the strict cone are additional sharp boundaries. Smoothing any of them changes lattice points, and the statement supplies no bound for the resulting internal collars. Although equality in \(eb^2=4da^2\) is impossible when \(e,b\) are odd, a positive-width smoothing collar around the cone can still contain lattice points and requires its own estimate.

**Why the determinant is not an estimate.** There are three independent obstructions.

First, a theorem uniform for arbitrary coefficients \(|u_{t,d,e}|\leq1\) cannot gain from this or any other phase: on any finite support \(\Omega\), the choice

\[
u_{t,d,e}=e(-f(t,d,e))
\]

gives \(\sum_\Omega u_{t,d,e}e(f(t,d,e))=|\Omega|\). Hence divisor-boundedness alone cannot be the coefficient hypothesis. A valid proof must use the exact \(\chi_4(\gamma)\chi_4(e)\), squarefree/coprimality restrictions, factor multiplicity, and cone. Conversely, the exact \(\mathcal A\) is not a smooth separable amplitude: the divisibility and coprimality conditions jump, and the inner factor count jumps at the cone. The mask adds (3.8). Thus neither the arbitrary-coefficient nor the smooth-amplitude interpretation is lawful.

Second, even the bare smooth phase returns to the same phase class under a full three-variable stationary transform. If \(p,q,r>0\) are the dual variables, the stationary equations are

\[
p=\sqrt N\sqrt{de},\quad
q=\frac{\sqrt N\,t}{2}\sqrt{e/d},\quad
r=\frac{\sqrt N\,t}{2}\sqrt{d/e}.
\]

They invert to

\[
t=\frac{2\sqrt{qr}}{\sqrt N},\quad
d=\frac p{\sqrt N}\sqrt{r/q},\quad
e=\frac p{\sqrt N}\sqrt{q/r}.
\]

Euler's identity gives \(pt+qd+re=2f\), so the transformed stationary phase is exactly

\[
f-pt-qd-re=-\frac{2p\sqrt{qr}}{\sqrt N}.                          \tag{3.9}
\]

Thus a single \(B\)-type transform returns another linear-times-square-root-product phase. On a box, if \(F=\sqrt{NM}\), the dual side scales are \(F/T,F/D,F/E\), while the stationary amplitude scale is \(TDE/F^{3/2}\). Without a new estimate for the dual signed sum, (3.9) is a transform-return, not a closing bound. For the literal problem the Fourier transform of the sharp coefficient and mask is additionally uncontrolled.

Third, the nearest-square mask does not provide a uniform nonresonance hypothesis. Let \(s\) be squarefree and

\[
N=sL^2+1,\qquad
\alpha=\sqrt{Ns}=sL+\delta,\qquad
0<\delta=\frac{s}{\alpha+sL}<\frac1{2L}.
\]

For every \(1\leq t<L\), \(0<t\delta<1/2\), hence

\[
k_{s,t}=sLt,\qquad
k_{s,t}^2-Nst^2=-st^2=-m.                                        \tag{3.10}
\]

Whenever \(m\) lies in a retained block with \(M>1\), (3.10) passes the mask because \(m\geq M>M^{3/4}\), while

\[
e(t\sqrt{Ns})=e(t\delta)
\]

rotates arbitrarily slowly as \(L\) grows. Choosing \(L\) large also makes \(M\ll\sqrt N=R^2\) compatible with the block. Exact radicals \(N=sL^2\) are removed by the mask, but this \(+1\) family survives. It therefore refutes any uniform derivative-modulo-one, dual-separation, or Diophantine lower bound inferred merely from the mask. This calculation is for the required positive complex direction at the fixed center \(N\); no cosine pairing or center average is used.

Finally, suppose a hypothetical theorem treats only a strict interior range in which \(T,D,E\) all grow. The high-\(T\) and fixed bounded-\(E\) complements can be paid using (2.3) and (3.6). The bounded-\(T\) complement cannot: its available absolute price is \(X^\varepsilon M^{1/4}/T\), and at fixed \(t\) its remaining Hessian is singular by (3.3). The \(D=1,T=1\) subface (3.7) is present. Therefore the survivor complement is not target-safe without a distinct signed boundary theorem. This proves the stated no-go while making no unsigned lower-bound claim about the exact scalar.

## 4. First doubtful or unproved step

The first unavailable inference is

\[
\det\!\left(f^{-1}L(\nabla^2f)L\right)=\frac14
\quad\Longrightarrow\quad
\text{a power-saving lattice-sum estimate for (2.1)}.
\]

No theorem with hypotheses matching the literal amplitude has been supplied or derived. If its coefficient hypothesis is merely \(|a_{t,d,e}|\ll X^\varepsilon\), the adversarial control disproves it. If its hypothesis is a smooth amplitude on a rectangular box, then \(\mathcal A\), the squarefree/coprimality/parity conditions, the factor cone, the product block, and \(\mathfrak M_M\) do not satisfy it. Opening \(\gamma,a,b\) is an exact possible next operation, but it changes the summation dimension and leaves the cone, coprimality, profile, and mask boundaries to be estimated. No such estimate is proved here.

Even after a hypothetical lawful interior decomposition, the first global boundary obstruction is bounded \(t\), particularly (3.7): it loses the \(t\)-direction, has singular \(d,e\) Hessian, and is not target-safe by absolute capacity. A separate signed lemma for this face is mandatory.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| exact_t_d_e_coefficient_and_multiplicity | **Pass.** The prime-valuation construction gives a bijection \(h=d\gamma a^2,r=e\gamma b^2\), so every factor pair occurs exactly once. |
| squarefree_coprimality_parity_character_and_cone | **Pass.** \(de\) is squarefree, hence \(d,e\) are squarefree and coprime; \((\gamma,de)=1\); \(e,\gamma,b\) are odd; the sign is exactly \(\chi_4(e)\chi_4(\gamma)\); the cone is \(eb^2>4da^2\). |
| literal_profile_mask_and_block_endpoints | **Obstruction recorded.** Equation (3.8), \(V_{\rm low}(R^2m/N)\), \(M\leq m<B_M\), the strict \(t\)-cutoff, and the strict cone are all retained. No unowned smoothing is made. |
| three_variable_scaled_Hessian_determinant | **Pass.** Matrix (2.2), determinant \(1/4\), eigenvalues, and unscaled determinant (3.2) are verified. |
| aspect_ratio_and_short_face_ledger | **Pass with obstruction.** Relations (3.5), the empty \(E=1\) face, bounded-\(E\) upper-\(t\) forcing, the present \(D=1\) face, and the singular fixed-\(t\) face are all priced. |
| M_T_D_E_capacity_and_dyadic_assembly | **Pass.** The coefficient-blind weighted price is (2.3); logarithmic assembly is absorbable into \(X^\varepsilon\). |
| t_equals_one_and_bounded_t_boundary | **Fails the target-safety gate.** Formula (3.7) is exact, the available price is \(X^\varepsilon M^{1/4}\), and the remaining two-variable Hessian is singular. |
| exceptional_slow_frequency_family | **Fails any uniform nonresonance hypothesis.** Equations (3.10) give surviving phases \(e(t\delta)\) with \(0<\delta<1/(2L)\). |
| individual_complex_direction_and_fixed_centre | **Pass.** Every calculation uses \(e(+f)\) at the fixed \(N=\lfloor X\rfloor\); no conjugate, cosine, mean square, or center average substitutes for it. |
| strict_survivor_complement_target_safety | **Fail.** High \(T\) and fixed bounded \(E\) are safe, but bounded \(T\) and \(D=1,T=1\) are not controlled at target scale by the available bounds. |
| Round138_cross_owner_and_downstream_scope | **Pass.** This report makes no claim about the independent cross owner, the full lower problem, any configuration-side owner, endpoint uniformity, the bridge, or a global exponent. |

The adversarial-coefficient test is diagnostic of theorem scope, not evidence that the exact \(\chi_4\)-weighted scalar has large magnitude. Likewise, (2.3) is only an upper capacity.

## 6. Dependencies and exact artifacts used

Mathematical dependencies used:

- the definitions and exact scalar in rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/blind_statement.md;
- the report and evidence rules in protocol.md;
- the task restrictions and required controls in rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/briefs/blind_three_variable_dispersion_feasibility.md.

No proof graph, strategy file, Round-138--146 nonblind artifact, sibling report, external source, numerical experiment, or symbolic-computation output was consulted. All calculations above are direct algebraic derivations from the statement.

## 7. Recommended state effect

**Reject** the nonzero three-variable Hessian as a standalone proof or owner-complete strict-intermediate-\(t\) reduction. **Retain** as candidate evidence the multiplicity-one coefficient identity, divisor bound, exact Hessian and Legendre return, capacity formula, cone aspect constraints, empty \(E=1\) face, bounded-\(E\) upper-\(t\) forcing, exact \(t=1\) coefficient, and the \(N=sL^2+1\) slow-frequency obstruction. The target estimate should receive **no promotion** from this report.
