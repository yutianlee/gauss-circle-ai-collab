# Round 187 statement-only high-height tangent-gcd problem

This packet is self-contained. Do not use a proof graph, strategy file,
prior round, sibling report, source, or conductor analysis.

Put \(e(z)=\exp(2\pi iz)\). Fix real \(X\ge2\), \(L\ge2\),
\(\sigma\in\{+1,-1\}\), and \(B>0\), and set

\[
 R_0=\lceil L\rceil,\qquad
 H_B=\lfloor(\log(2X))^B\rfloor .
\tag{B187.1}
\]

For every squarefree positive integer \(N\), an allocation-independent
rule selects at most one unordered pair of distinct odd prime divisors
\(\{p_N,q_N\}\) with \(\chi_4(p_Nq_N)=-1\). Define

\[
 \rho_N(d)=
 \begin{cases}
  1,&\text{no pair is selected},\\
  1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
   +2\mathbf1_{p_Nq_N\mid d},&\text{a pair is selected}.
 \end{cases}
\tag{B187.2}
\]

Let \(A_{L,X}^{\sigma}(m,d)\) be one fixed literal coefficient, not an
arbitrary array. It is zero off every original shell, height, strict
\(4m<d<16m\) cone, profile, floor, star, half-weight, hard-sample,
crossing, endpoint, sign, squarefree, coprimality, and zero-extension
predicate, and on support \(m,d\asymp L\). Only the pointwise envelope
\(|A_{L,X}^{\sigma}(m,d)|\ll\mathcal X\) is supplied, where
\(\mathcal X\) is an allowed subpolynomial loss. No variation, density,
equidistribution, Fourier norm, or translation-invariance hypothesis may
be invented.

Define

\[
 \lambda_{N,\sigma}(d)=
 \begin{cases}
  \mu^2(N)\rho_N(d)A_{L,X}^{\sigma}(N/d,d),
   &N,d>0,\ \mu^2(N)=1,\ d\mid N,\ 2\nmid d,\\
  0,&\text{otherwise},
 \end{cases}
\tag{B187.3}
\]

including zero extension outside positive integer arguments.

The primitive outer labels are

\[
 \mathfrak f=(\kappa,g,h,U,v),\quad
 \kappa,g,h,U,v>0,\quad \kappa,g,U\text{ odd},\quad
 (gU,v)=1,\quad(U,h)=1,\quad0<2\kappa gh<R_0.
\tag{B187.4}
\]

For \(U>1\), let \(\bar v\) denote the inverse of \(v\bmod U\) and set

\[
 \begin{array}{lll}
 +:&S_{0,+}=[\bar vh]_U,&w_{0,+}=(S_{0,+}v-h)/U,\\[1mm]
 -:&S_{0,-}=[-\bar vh]_U,&w_{0,-}=(h+vS_{0,-})/U.
 \end{array}
\tag{B187.5}
\]

For \(U=1\), use
\((S_{0,+},w_{0,+})=(0,-h)\) and
\((S_{0,-},w_{0,-})=(0,h)\). For
\(\omega\in\{+,-\}\), put

\[
 S_{t,\omega}=S_{0,\omega}+Ut,\qquad
 s_{t,\omega}=gS_{t,\omega},\qquad
 w_{t,\omega}=w_{0,\omega}+vt,
\tag{B187.6}
\]

\[
 I_{\mathfrak f,\omega}
 =\{t\in\mathbb Z:S_{t,\omega}>0,\ w_{t,\omega}>0\}.
\tag{B187.7}
\]

Positivity is imposed before every square-root evaluation. Put
\(r=2\kappa gh\). In the plus orientation define

\[
 N_{\mathfrak f,t}^{+}
 =\kappa gU(\kappa v+2w_{t,+}),\qquad
 N_{\mathfrak f,t}^{+}+r
 =(\kappa gU+2s_{t,+})\kappa v,
\tag{B187.8}
\]

\[
 \begin{aligned}
 B_{\mathfrak f,+}^{\sigma}(t)={}&
 \left(1-{r\over R_0}\right)
 \lambda_{N_{\mathfrak f,t}^{+}+r,\sigma}
        (\kappa gU+2s_{t,+})
 \overline{\lambda_{N_{\mathfrak f,t}^{+},\sigma}(\kappa gU)}\\
 &\times e\!\left({\sigma\sqrt X\,r\over
 \sqrt{N_{\mathfrak f,t}^{+}+r}+\sqrt{N_{\mathfrak f,t}^{+}}}\right).
 \end{aligned}
\tag{B187.9}
\]

In the minus orientation define

\[
 N_{\mathfrak f,t}^{-}
 =(\kappa gU+2s_{t,-})\kappa v,\qquad
 N_{\mathfrak f,t}^{-}+r
 =\kappa gU(\kappa v+2w_{t,-}),
\tag{B187.10}
\]

\[
 \begin{aligned}
 B_{\mathfrak f,-}^{\sigma}(t)={}&
 \left(1-{r\over R_0}\right)
 \lambda_{N_{\mathfrak f,t}^{-}+r,\sigma}(\kappa gU)
 \overline{\lambda_{N_{\mathfrak f,t}^{-},\sigma}
        (\kappa gU+2s_{t,-})}\\
 &\times e\!\left({\sigma\sqrt X\,r\over
 \sqrt{N_{\mathfrak f,t}^{-}+r}+\sqrt{N_{\mathfrak f,t}^{-}}}\right).
 \end{aligned}
\tag{B187.11}
\]

For every nonempty dyadic block \(Y<h\le2Y\) with \(Y>H_B\), the
target is the one-sided inequality

\[
 \boxed{
 \Re\!\sum_{\omega\in\{+,-\}}
 \sum_{\substack{\mathfrak f\text{ satisfying }(\mathrm{B187.4})\\
                  Y<h\le2Y}}
 (-1)^{S_{0,\omega}}
 \sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t)
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{B187.12}
\]

There is one real part outside both orientations, all primitive rows, and
all affine indices. No lower bound for a negative block is requested.
The complete positive capacity is \(O(YL^2\mathcal X)\), so the required
gain is the full factor \(Y\).

You may use and must verify the finite identity, for odd \(U>1\),

\[
 E_U(a):=(-1)^{[a]_U},\qquad
 \widehat E_U(k)={2\over1+e(-k/U)},\qquad
 E_U(a)={1\over U}\sum_{k\bmod U}\widehat E_U(k)e(ka/U),
\tag{B187.13}
\]

and the anchors
\((-1)^{S_{0,+}}=E_U(\bar vh)\),
\((-1)^{S_{0,-}}=E_U(-\bar vh)\). The \(U=1\) convention remains
separate. Splitting a zero mode, a low-frequency packet, or an
orientation trace is useful only if it is bounded at target size and the
exact signed complement remains. Centering, positive Fourier
recombination, or a positive alias energy is not cancellation.

Independently do all of the following.

1. Verify the primitive parametrization, anchors, both orientations,
   positivity sets, endpoint products, phase, parity sign, and
   multiplicity-one scope.
2. Reproduce the \(O(YL^2\mathcal X)\) positive capacity and the exact
   missing factor \(Y\), including the terminal truncated block.
3. Derive (B187.13), treat \(U=1\), and price the Fourier zero mode and
   every proposed low/nonresonant packet with all outer labels restored.
4. Keep every nonzero mode jointly signed over \(h,v,t\), both
   orientations, and every literal field until a proved inequality is
   available. Do not take modewise, rowwise, orientationwise, selector,
   or endpoint moduli and then claim the factor \(Y\).
5. Test the exact arithmetic deletions and zero extensions. An
   adversarial bounded-array example can refute a coefficient-uniform
   mechanism but is not physical lower mass. A valid proof must identify
   which actual coefficient property defeats that false analogue.
6. Give either a proof of (B187.12), the widest rigorously target-safe
   exact signed sector with its exact complement, or the narrowest exact
   deletion/resonance/capacity/self-return no-go and the first additional
   literal relation needed.

Success affects only the exact original-\(t=1\) residual after separate
accepted connectors. It does not prove any \(t\ge2\) or near-resonant
component, parent estimate, endpoint theorem, bridge, global theorem, or
exponent. Computation, if any, is diagnostic only.

Return exactly:

1. Result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required control test and outcome.
6. Dependencies and exact artifacts used.
7. Recommended state effect.
