# Round 231: blind odd-kernel mean, covariance, and discrepancy control

- Campaign: `gc-actual-upper-tail-a`.
- Task and role: `blind_odd_kernel_covariance`; statement-only blind rederiver.
- Generated: `2026-10-11T15:13:38Z`.
- Supplied graph SHA-256: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. The graph itself was not read.
- Status: candidate analytic evidence only; no arithmetic-center theorem and no parent-target conclusion.
- Allocation: entirely analytical/algebraic; no numerical experiments.

## 1. Result: exact analytic lemma and a scoped no-go result

The whole-line signed mean vanishes, but the whole-line positive second moment is

\[
 \boxed{\int_{\mathbb R}|S(t)|^2\,dt
 =L\sum_{i,j}a_i a_j C((v_i-v_j)/L)
 =L\int_{\mathbb R}|\widehat K(\eta)|^2
                  |\widehat\mu(\eta/L)|^2\,d\eta,}
\]

where \(\mu=\sum_j a_j\delta_{v_j}\) and
\(C(h)=\int K(u)K(u+h)\,du\). In particular,

\[
 C(h)=\|K\|_2^2-\tfrac12\|K(\cdot+h)-K\|_2^2
      =\|K\|_2^2-\tfrac12h^2\|K'\|_2^2+O_K(h^4).
\]

Thus covariance is positive and essentially undiminished at coincident or sufficiently near-coincident centers. Oddness and zero integral alone provide **no uniform power saving** in this positive second moment or in the length of a positive large-value set. They do provide exact signed-mean cancellation and a derivative saving against a slowly varying test, with coefficient, centering, and boundary costs given below.

Two additional rigorous interfaces isolate what extra cancellation would have to mean:

1. An exact representation by signed left-minus-right local coefficient discrepancies, followed by fully costed pointwise and \(L^p\) bounds.
2. An optimal Fourier-multiplier bound in terms of the \(L^2\) norm of the cumulative signed discrepancy, with the total-mass correction included when the coefficients are unbalanced.

These are general analytic controls. Their counterexamples do not imply failure of an estimate for any particular arithmetic family.

## 2. Exact statements and hypotheses

Let \(K\in\mathcal S(\mathbb R)\) be real, odd, and nonzero; \(L>0\); \(v_j,a_j\in\mathbb R\), with finitely many indices. Repeated centers are allowed. Define

\[
 S(t)=\sum_j a_jK((t-v_j)/L),\qquad
 \mu=\sum_j a_j\delta_{v_j},\qquad
 M=\sum_j a_j,\qquad A_1=\sum_j|a_j|.
\]

All displayed bounds using \(A_1\) remain valid if it is replaced by the total variation of the measure after coefficients at identical centers are combined. Write

\[
 \widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i t\xi}\,dt,
 \quad \widehat\mu(\xi)=\sum_j a_je^{-2\pi i\xi v_j},
 \quad m_1=\int uK(u)\,du,
 \quad M_r(K)=\int |u|^r|K(u)|\,du.
\]

**Signed means.** One has

\[
 \int S=0,\qquad \int tS(t)\,dt=L^2m_1 M,
 \qquad \widehat S(\xi)=L\widehat K(L\xi)\widehat\mu(\xi).
 \tag{2.1}
\]

The second identity is an ordinary signed first spatial moment, not an absolute moment. The first identity is the unweighted signed mean. More generally,

\[
 \int(t-c)^n S(t)\,dt
 =L\sum_j a_j\sum_{r=0}^n\binom nr(v_j-c)^{n-r}L^r
                       \int u^rK(u)\,du,
 \tag{2.2}
\]

and the terms with even \(r\) vanish. For a Schwartz test \(g\),

\[
 \int S(t)g(t)\,dt
 =L\int \widehat K(L\xi)\widehat\mu(\xi)\widehat g(-\xi)\,d\xi.
 \tag{2.3}
\]

**Slowly varying tests, with full costs.** Let \(g\in C^1(\mathbb R)\) have bounded derivative. It may grow linearly. Then

\[
 \int Sg
 =L\sum_j a_j\int K(u)\{g(v_j+Lu)-g(v_j)\}\,du,
 \quad
 |\int Sg|\le L^2M_1(K)A_1\|g'\|_\infty.
 \tag{2.4}
\]

Define the even Schwartz primitive

\[
 P(x)=\int_{-\infty}^xK(u)\,du,
 \qquad \tau(r)=\int_r^\infty|K(u)|\,du\quad(r\ge0).
\]

There is a slightly sharper version

\[
 \int Sg=-L\int g'(t)\sum_j a_jP((t-v_j)/L)\,dt,
 \quad
 |\int Sg|\le L^2\|P\|_1A_1\|g'\|_\infty,
 \quad \|P\|_1\le M_1(K).
 \tag{2.5}
\]

For \(g(t)=G((t-c)/H)\), this bound is
\(L^2H^{-1}\|P\|_1A_1\|G'\|_\infty\). There is no omitted dependence on the coefficient mass.

If additionally \(g\in C^3\) with bounded first three derivatives, then

\[
 \int Sg=L^2m_1\sum_j a_jg'(v_j)+R,
 \qquad |R|\le \tfrac16L^4M_3(K)A_1\|g'''\|_\infty.
 \tag{2.6}
\]

Replacing all \(g'(v_j)\) by \(g'(c)\) has the explicit centering cost

\[
 \left|\int Sg-L^2m_1Mg'(c)\right|
 \le L^2|m_1|\|g''\|_\infty\sum_j|a_j||v_j-c|
       +\tfrac16L^4M_3(K)A_1\|g'''\|_\infty.
 \tag{2.7}
\]

These identities allow \(m_1=0\); no nonvanishing first moment is assumed.

**Finite-interval boundary and variance costs.** For \(I=[A,B]\), \(A<B\), and \(g\in C^1(I)\), set \(Q(t)=\sum_j a_jP((t-v_j)/L)\). Then

\[
 \int_A^B Sg=L[g(t)Q(t)]_A^B-L\int_A^B g'(t)Q(t)\,dt,
 \tag{2.8}
\]

so

\[
 |\int_A^B Sg|
 \le L\sum_j|a_j|\left\{|g(B)|\tau(|B-v_j|/L)
                         +|g(A)|\tau(|A-v_j|/L)\right\}
       +L^2\|P\|_1A_1\|g'\|_{L^\infty(I)}.
 \tag{2.9}
\]

This formula needs no extension of \(g\) to any center outside \(I\). The boundary contribution is generally of order \(LA_1\) when a center is at an endpoint. When every center is distance at least \(d\) from both endpoints, it is at most
\(LA_1(|g(A)|+|g(B)|)\tau(d/L)\), with Schwartz decay as \(d/L\to\infty\).

Writing \(E=\int_{\mathbb R}S^2\) and \(E_I=\int_I S^2\), the exact second-moment truncation and a useful tail estimate are

\[
 E_I=L\sum_{i,j}a_i a_j
 \int_{(A-v_i)/L}^{(B-v_i)/L}
 K(u)K(u+(v_i-v_j)/L)\,du,
 \tag{2.10}
\]

\[
 0\le E-E_I\le L\left(\sum_j|a_j|\sigma_j\right)^2,
 \qquad
 \sigma_j^2=\int_{\{u:v_j+Lu\notin I\}}|K(u)|^2\,du.
 \tag{2.11}
\]

There is no uniform probability measure on the whole real line. The term covariance below means the whole-line bilinear \(L^2\) kernel. For actual variance under the uniform probability measure on \(I\), the exact centering correction is

\[
 \operatorname{Var}_I(S)=\frac{E_I}{|I|}
       -\left(\frac1{|I|}\int_I S\right)^2.
 \tag{2.12}
\]

**Covariance and Fourier energy.** With \(C(h)=\int K(u)K(u+h)\,du\),

\[
 C(-h)=C(h),\quad C(0)=\|K\|_2^2>0,\quad
 C(h)=\int|\widehat K(\eta)|^2e^{2\pi i\eta h}\,d\eta,
 \tag{2.13}
\]

\[
 E=L\sum_{i,j}a_i a_j C((v_i-v_j)/L)
  =L^2\int|\widehat K(L\xi)|^2|\widehat\mu(\xi)|^2\,d\xi.
 \tag{2.14}
\]

In particular \(0\le E\le L\|K\|_2^2A_1^2\), with equality in the upper bound for a same-sign coincident cloud. Also

\[
 C(0)-C(h)=\tfrac12\|K(\cdot+h)-K\|_2^2,
 \quad
 \left|C(h)-C(0)+\tfrac12h^2\|K'\|_2^2\right|
 \le \frac{|h|^4}{24}\|K''\|_2^2.
 \tag{2.15}
\]

Oddness makes \(\widehat K\) purely imaginary and odd. It does not make
\(|\widehat K|^2\) signed. The zero at frequency zero satisfies

\[
 |\widehat K(\eta)|\le 2\pi|\eta|M_1(K).
 \tag{2.16}
\]

For any \(H>0\), the contribution to (2.14) from \(|\xi|\le H^{-1}\) is therefore at most

\[
 \frac{8\pi^2}{3}L^4M_1(K)^2A_1^2H^{-3}.
 \tag{2.17}
\]

The complementary frequency integral remains in full; discarding it would be an unproved step.

**Actual signed local-discrepancy interface.** For \(r>0\), define

\[
 D_t(r)=\sum_{0<|t-v_j|\le r}a_j\operatorname{sgn}(t-v_j).
 \tag{2.18}
\]

This is the actual signed mass immediately to the left minus that to the right of \(t\); a coefficient at \(t\) contributes zero. Let
\(c_K=\int_0^\infty|K'(u)|\,du\). Then

\[
 \boxed{S(t)=-\int_0^\infty K'(u)D_t(Lu)\,du.}
 \tag{2.19}
\]

Consequently, for \(1\le p\le\infty\),

\[
 \|S\|_p\le\int_0^\infty|K'(u)|\|D_{\cdot}(Lu)\|_p\,du,
 \tag{2.20}
\]

\[
 \boxed{E\le c_K\int_0^\infty|K'(u)|
                         \|D_{\cdot}(Lu)\|_2^2\,du.}
 \tag{2.21}
\]

For a bounded-radius pointwise version, every \(R>0\) gives

\[
 |S(t)|\le\left(\int_0^R|K'(u)|\,du\right)
                 \sup_{0<r\le LR}|D_t(r)|
             +A_1\int_R^\infty|K'(u)|\,du.
 \tag{2.22}
\]

The tail cost cannot silently be dropped. These bounds require estimates on the **signed** \(D_t\), not on the number of centers. For completeness its Fourier energy is exactly

\[
 \|D_{\cdot}(r)\|_2^2
 =\int_{\mathbb R}\frac{(1-\cos(2\pi r\xi))^2}{\pi^2\xi^2}
                         |\widehat\mu(\xi)|^2\,d\xi,
 \tag{2.23}
\]

where the multiplier is set to its limiting value zero at \(\xi=0\).

**Cumulative signed-discrepancy interface, including centering mass.** Let
\(F(x)=\mu(({-\infty},x])\). It is bounded, and

\[
 S(t)=\frac1L\int_{\mathbb R}K'((t-v)/L)F(v)\,dv.
 \tag{2.24}
\]

If \(M=0\), \(F\) is a compactly supported step function. Put

\[
 B_K=\sup_{\eta\in\mathbb R}2\pi|\eta\widehat K(\eta)|.
\]

Then

\[
 \boxed{\|S\|_2\le B_K\|F\|_2\le\|K'\|_1\|F\|_2,}
 \qquad
 \|S\|_2\le L^{-1/2}\|K'\|_2\|F\|_1.
 \tag{2.25}
\]

The constant \(B_K\) is the optimal uniform multiplier constant over finite real atomic measures of total mass zero, for each fixed \(L\). If \(M\ne0\), \(F\) need not belong to \(L^2\), so that assertion cannot be used directly. For any chosen real center \(c\), define

\[
 F_c(x)=F(x)-M\mathbf1_{[c,\infty)}(x).
\]

This is compactly supported, and the corrected identities and bounds are

\[
 S(t)=M K((t-c)/L)+\frac1L\int K'((t-v)/L)F_c(v)\,dv,
 \tag{2.26}
\]

\[
 \|S\|_2\le |M|\sqrt L\|K\|_2+B_K\|F_c\|_2,
 \quad
 \|S\|_2\le |M|\sqrt L\|K\|_2
                   +L^{-1/2}\|K'\|_2\|F_c\|_1.
 \tag{2.27}
\]

The term involving \(M\) is essential. Global coefficient balance alone also does not make \(F\) small.

## 3. Proof and derivation

**Means and slow tests.** Oddness gives \(\int K=0\). Substituting \(t=v_j+Lu\) gives (2.1), (2.2), and the physical-space Fourier transform; pairing against \(g\) gives (2.3). Subtracting the constant \(g(v_j)\) in each whole-line integral is exact. The mean-value theorem gives
\(|g(v_j+Lu)-g(v_j)|\le L|u|\|g'\|_\infty\), proving (2.4). Equivalently the integral is

\[
 L\sum_j a_j\int_0^\infty K(u)
             [g(v_j+Lu)-g(v_j-Lu)]\,du.
\]

Because \(\int K=0\), its primitive \(P\) decays rapidly at both ends; because \(K\) is odd, \(P\) is even. For all \(x\),
\(|P(x)|\le\tau(|x|)\), and Tonelli gives
\(\|P\|_1\le2\int_0^\infty u|K(u)|\,du=M_1(K)\).
Since \(S=LQ'\), integration by parts proves (2.5) and (2.8). The endpoint terms at infinity vanish even for a linearly growing \(g\). Bounding the finite endpoints by \(\tau\) and the integral of \(|Q|\) by \(LA_1\|P\|_1\) proves (2.9). Taylor expansion to order two at each \(v_j\), using \(\int K=\int u^2K=0\), proves (2.6). The mean-value bound on \(g'(v_j)-g'(c)\) proves (2.7). Formula (2.10) is direct substitution, (2.11) is the triangle inequality in \(L^2(I^c)\), and (2.12) is the exact variance expansion.

**Covariance.** Expanding the finite sum and substituting \(t=v_i+Lu\) proves the first formula in (2.14). Plancherel gives the second and (2.13). The triangle inequality gives the general upper bound \(L\|K\|_2^2A_1^2\). Expanding the square of a translation difference gives the first identity in (2.15). Differentiating the Schwartz covariance and integrating by parts gives

\[
 C'(0)=C'''(0)=0,\quad C''(0)=-\|K'\|_2^2,
 \quad C^{(4)}(h)=\int K''(u)K''(u+h)\,du.
\]

Cauchy-Schwarz bounds the last derivative by \(\|K''\|_2^2\), so Taylor's theorem proves the stated global fourth-order remainder bound. Finally

\[
 \widehat K(\eta)=\int K(u)(e^{-2\pi i\eta u}-1)\,du
\]

and \(|e^{ix}-1|\le|x|\) prove (2.16). Use \(|\widehat\mu|\le A_1\) and integrate \(\xi^2\) over \([-H^{-1},H^{-1}]\) to obtain (2.17).

**Local discrepancy.** For fixed \(t\), each term in \(D_t(r)\) jumps at \(r=|t-v_j|\), with jump \(a_j\operatorname{sgn}(t-v_j)\). Thus, as a Stieltjes integral,

\[
 S(t)=\int_0^\infty K(r/L)\,dD_t(r).
\]

Integration by parts has zero endpoint contributions: \(K(0)=0\), \(K(\infty)=0\), and \(D_t\) is bounded. This proves (2.19). Minkowski gives (2.20), weighted Cauchy-Schwarz gives (2.21), and \(|D_t(r)|\le A_1\) gives (2.22). All these integrals are finite: for finite \(p\),

\[
 \|D_{\cdot}(r)\|_p\le A_1(2r)^{1/p},
\]

and the Schwartz derivative makes the resulting \(u\)-integral finite. Endpoint values at atoms change no \(L^p\) integral. Finally \(D_{\cdot}(r)=h_r*\mu\), where
\(h_r(t)=\operatorname{sgn}(t)\mathbf1_{0<|t|\le r}\). Direct integration gives

\[
 \widehat h_r(\xi)=-i\frac{1-\cos(2\pi r\xi)}{\pi\xi};
\]

Plancherel proves (2.23).

**Cumulative discrepancy.** Integration by parts against \(dF=d\mu\) gives (2.24), since the Schwartz kernel times bounded \(F\) vanishes at both infinities. If \(M=0\), the derivative-kernel convolution has Fourier multiplier

\[
 (2\pi i\xi)L\widehat K(L\xi)
       =2\pi i\eta\widehat K(\eta),\qquad\eta=L\xi.
\]

Its \(L^2\) operator norm is \(B_K\). This also follows directly from Plancherel and pointwise multiplication. The bound \(B_K\le\|K'\|_1\) is the Fourier \(L^1\) bound for \(K'\). Young's inequality with derivative-kernel \(L^2\) norm \(L^{-1/2}\|K'\|_2\) proves the second estimate in (2.25).

For optimality, real compactly supported step functions are dense in real \(L^2\), and each is the cumulative distribution of a finite real atomic measure of mass zero. The convolution operator is bounded. The usual multiplier lower bound follows by choosing Fourier support in small neighborhoods of a point where its modulus approaches the supremum and its negative, with conjugate symmetry to keep the function real. Density then gives the same supremum on these step functions. This proves the stated optimality without asserting that an arithmetic family attains it.

Apply the mass-zero identity to \(\mu-M\delta_c\) to obtain (2.26). The triangle inequality and the two bounds just proved give (2.27).

## 4. First doubtful or unproved step

There is no unproved step in the analytic identities or their inequalities. Their application to an arithmetic family first requires an actual estimate for at least one of the following quantities, with the correct coefficient sizes and scales:

\[
 \int|\widehat K(\eta)|^2|\widehat\mu(\eta/L)|^2\,d\eta,
 \quad
 \int_0^\infty|K'(u)|\|D_{\cdot}(Lu)\|_2^2\,du,
 \quad \|F\|_2\text{ or }\|F_c\|_2,
\]

with the nonzero-mass term in (2.27) retained. No such arithmetic discrepancy or spectral-energy estimate was assumed, read, or proved here.

In particular, replacing a small signed mean \(\int Sg\) by a small positive moment \(\int |S|^2\), omitting an interval endpoint term, treating \(\widehat K(0)=0\) as suppression of the entire active frequency band, or assuming near-resonant cross terms have negative sign would each be a false step. A moment/large-value application additionally needs its own exact implication and uniformity checks; none is supplied by this isolated packet.

## 5. Required control tests and outcomes

**Control: `blind_independence` — PASS.** Read only `protocol.md`, the assigned brief, and the isolated statement. No graph, active manifest, historical report, actual-interface file, sibling output, or external source was read. Every result above was derived from the isolated hypotheses.

**Control: `odd_resonance_and_detuning` — PASS; generic power gain refuted.** At coincident centers \(v_j=v\), let \(A=\sum_j a_j\). Then

\[
 S(t)=AK((t-v)/L),\quad \int S=0,
 \quad \int|S|^p=L|A|^p\|K\|_p^p\quad(1\le p<\infty).
 \tag{5.1}
\]

For \(n\) coefficients all equal to one, the positive second moment is
\(Ln^2\|K\|_2^2\). Hence neither an extra inverse power of \(n\) nor a uniform small factor attributed solely to oddness is possible relative to the sharp generic upper bound.

This obstruction persists under small distinct detunings. Suppose \(a_j\ge0\), \(A=\sum a_j>0\), and \(|v_j-v_0|\le\delta L\). The translation inequality
\(\|K(\cdot-h)-K\|_2\le|h|\|K'\|_2\) gives

\[
 \|S\|_2\ge A\sqrt L\bigl(\|K\|_2-\delta\|K'\|_2\bigr)_+.
 \tag{5.2}
\]

Thus any fixed sufficiently small \(\delta\) retains a fixed positive proportion of \(LA^2\|K\|_2^2\), even with pairwise distinct centers. For two equal coefficients at separation \(Lh\), the energy is
\(2a^2L(C(0)+C(h))\), which tends to \(4a^2LC(0)\) as \(h\to0\). For opposite coefficients, it is instead

\[
 2a^2L(C(0)-C(h))
 =a^2L\|K(\cdot+h)-K\|_2^2
 \le a^2Lh^2\|K'\|_2^2.
 \tag{5.3}
\]

The latter saving comes from actual opposite coefficient signs together with near coincidence. It is not an implication of the parity of the kernel; the translation argument works for nonodd kernels as well. Opposite coefficients far apart have energy tending to \(2a^2LC(0)\), since \(C(h)\to0\); total mass zero by itself does not ensure a small local energy.

**Control: positive and absolute large-value capacity — PASS.** Since a nonzero continuous odd \(K\) takes positive values, there are a bounded interval \(J\) of positive length and \(\kappa>0\) such that \(K(u)\ge\kappa\) on \(J\). The coincident cloud with \(A>0\) satisfies

\[
 |\{t:S(t)\ge \kappa A\}|\ge L|J|,
 \qquad |\{t:|S(t)|\ge\kappa A\}|\ge L|J|.
 \tag{5.4}
\]

At the same time its signed whole-line mean is zero. For the detuned nonnegative cloud,
\(|S(v_0+Lu)-AK(u)|\le A\delta\|K'\|_\infty\).
If \(\delta\|K'\|_\infty\le\kappa/2\), its positive large-value set at threshold \(\kappa A/2\) still has measure at least \(L|J|\). These exact lower controls prevent a general capacity saving inferred solely from signed-mean cancellation. Chebyshev's valid consequence remains
\(|\{|S|\ge V\}|\le E/V^2\); obtaining smaller capacity requires more information.

**Control: explicit odd kernel and boundary — PASS.** For
\(K(u)=u e^{-u^2}\), direct Gaussian integration gives

\[
 P(u)=-\tfrac12e^{-u^2},\quad m_1=\frac{\sqrt\pi}{2},
 \quad C(h)=\frac{\sqrt\pi}{4\sqrt2}(1-h^2)e^{-h^2/2}.
 \tag{5.5}
\]

This covariance is strictly positive for \(|h|<1\), despite oddness; it can be negative at larger separation. The signed test \(g(t)=t/H\) on the whole line gives exactly \(L^2m_1A/H\), showing the derivative scale in (2.4) is nonvacuous. A single center at zero with coefficient one and the constant test on \([0,RL]\) gives

\[
 \int_0^{RL}K(t/L)\,dt=\frac L2(1-e^{-R^2}).
 \tag{5.6}
\]

The derivative of the test is zero, but the endpoint term is not. Removing it would give a false first-moment estimate. All checks are exact; no numerical approximation is involved.

**Control: signed-discrepancy cost — PASS.** For a single atom \(a\delta_v\),
\(D_t(r)=a\operatorname{sgn}(t-v)\mathbf1_{0<|t-v|\le r}\), so
\(\|D_{\cdot}(r)\|_2^2=2a^2r\). The right side of (2.21) is therefore of order \(La^2\), consistent with the exact energy. For a dipole \(a(\delta_x-\delta_y)\), the cumulative discrepancy has
\(\|F\|_1=|a||x-y|\) and \(\|F\|_2^2=a^2|x-y|\). The \(L^1\) version of (2.25) reproduces the valid bound
\(E\le a^2|x-y|^2L^{-1}\|K'\|_2^2\). For an unbalanced atom, \(F\notin L^2\), and (2.27) correctly retains its full energy scale.

**Control: `generic_capacity_not_arithmetic_lower_bound` — PASS.** The coincident and detuned clouds are controls inside the isolated arbitrary-center/arbitrary-real-coefficient class. They disprove only the purported universal implication from oddness or zero integral to a power gain. They neither establish a lower bound for any arithmetic coefficient family nor rule out arithmetic cancellation in (2.19), (2.23), or (2.14). No arithmetic no-go is claimed.

## 6. Dependencies and exact artifacts used

Only the following files were read:

1. `protocol.md`; SHA-256 `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
2. `rounds/codex-managed/gc-actual-upper-tail-a/briefs/blind_odd_kernel_covariance.md`; SHA-256 `aa17531333a9c63664052397e44f1d6983148cef684c527b4670e47efaa21afb`.
3. `rounds/codex-managed/gc-actual-upper-tail-a/briefs/blind_odd_kernel_statement.md`; SHA-256 `bb3e8746c7a3bb71161949f3dc6910ce2351e078afbf68327c5599c1083a9223`.

Mathematical tools: changes of variables in finite sums of Schwartz functions, ordinary and Stieltjes integration by parts, Taylor's theorem, Fourier inversion/Plancherel with the stated convention, and the triangle, Cauchy-Schwarz, Minkowski, and Young inequalities. There are no imported specialized theorems, numerical dependencies, or source-hypothesis assumptions.

Only the assigned report path was written. The report is to be frozen by a SHA-256 computed after this write and delivered to the conductor; a self-referential file hash is not embedded in the report. No state, proof draft, validation matrix, synthesis, sibling artifact, or legacy file was changed.

## 7. Recommended state effect

**Retain** this report as independent exact analytic control evidence. **Reject** any universal inference that oddness/zero integral alone supplies a power gain for the positive second moment or positive/absolute large-value capacity. **Retain** the signed-discrepancy and Fourier-energy formulas as possible quantitative interfaces, contingent on an actual signed arithmetic estimate.

**No change** to the parent upper-tail or moment target on this report alone. Any graph promotion belongs to the conductor after the prescribed seam review and state validation. This assigned task ends with the report and its freeze hash; it does not propose or begin another round.
