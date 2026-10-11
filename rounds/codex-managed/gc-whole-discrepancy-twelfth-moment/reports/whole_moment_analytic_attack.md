# Round 201: whole-moment analytic attack

Campaign: `gc-whole-discrepancy-twelfth-moment`  
Task: `whole_moment_analytic_attack`; role: discovery; status: candidate evidence only.  
Generated: 2026-09-23, Asia/Shanghai.  
Starting and locally verified raw graph SHA-256: `2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5`.  
No sibling report was read. No numerical experiment was performed. Only this assigned report was written.

## 1. Result: a complete reduction, with the signed offdiagonal still open

The fixed-window Poisson--Bessel reduction is valid for the **whole inclusive discrepancy**. With the definitions in Section 2, uniformly for real radii in the fixed window,

\[
 P(R^2)=\frac{\sqrt R}{\pi}H_T(R)
       +O_{\rho,c,C,\varepsilon}(T^{1/2+\varepsilon}).                 \tag{201.A1}
\]

The Bessel error inside this formula is only \(O(T^{-1/2})\); the larger displayed error is the fully accounted sharp-to-smooth annulus error. The coefficient sequence remains fixed as \(R\) varies.

The exact twelfth moment has all \(2^{12}\) signs:

\[
 \mathcal M_{12}(T)=\frac{T}{2^{12}}
 \sum_{\boldsymbol\sigma\in\{-1,1\}^{12}}
 e\!\left(-\frac38\sum_j\sigma_j\right)
 \sum_{\boldsymbol n\in\mathbb N^{12}}
 \left(\prod_j a_{n_j}(T)\right)
 \widehat w\!\left(-T\sum_j\sigma_j\sqrt{n_j}\right).              \tag{201.A2}
\]

All sums are absolutely convergent for fixed \(T\). The exact-resonance contribution \(\mathcal D_{12}(T)\) is \(O(T)\), including nonpairing relations. In fact \(0\le\mathcal D_{12}(T)\ll T\). Consequently the first unproved estimate is precisely the one-sided bound (201.A18) below for the complete signed nonzero-frequency aggregate. No such new bound is proved here.

As a normalization control, this argument proves

\[
 \int w(R/T)|H_T(R)|^2\,dR
 =\frac T2\widehat w(0)\sum_{n\ge1}a_n(T)^2+O_{\rho,w,B}(T^{-B})
 \ll_{\rho,w}T                                                     \tag{201.A3}
\]

for every fixed \(B>0\). It recovers \(\int_{Y/2}^{3Y}|P(x)|^2dx\ll_\varepsilon Y^{3/2+\varepsilon}\), with the same exponent as the accepted graph theorem.

The exit label supported by this report is `whole_discrepancy_moment_reduction_open_offdiagonal`. Neither a new pointwise exponent nor an M1/M2 estimate follows.

## 2. Exact statement and hypotheses

Write

\[
 N(R)=\#\{m\in\mathbb Z^2:|m|\le R\},\quad
 P(x)=N(\sqrt x)-\pi x,\quad r_2(n)=\#\{m:|m|^2=n\},\quad e(u)=e^{2\pi i u}.
\]

Take \(T=\sqrt Y\ge2\) and **one** \(\delta=T^{-1/2}\) for the entire window. Fix a real radial \(\rho\in C_c^\infty(\mathbb R^2)\), supported in the closed unit disk, with \(\rho\ge0\) and \(\int\rho=1\). Put

\[
 \rho_\delta(u)=\delta^{-2}\rho(u/\delta),\quad
 \widehat f(\xi)=\int f(u)e(-u\cdot\xi)\,du,\quad
 \Psi(s)=\widehat\rho(se_1).
\]

Thus \(\Psi\) is real and even, \(\Psi(0)=1\), \(|\Psi|\le1\), and \(|\Psi(s)|\le C_A(1+|s|)^{-A}\) for every fixed \(A\). Nonnegativity of \(\rho\) does **not** assert nonnegativity of \(\Psi\).

Fix a real nonnegative \(w\in C_c^\infty((0,\infty))\), equal to one on \([1/\sqrt2,\sqrt3]\), and choose fixed \(0<c<C<\infty\) containing its support. Define the one-dimensional transform by the same \(e(-u\xi)\) convention and set

\[
 a_n(T)=r_2(n)n^{-3/4}\Psi(\sqrt{n/T}),\qquad
 H_T(R)=\sum_{n\ge1}a_n(T)\cos(2\pi R\sqrt n-3\pi/4),
\]
\[
 \mathcal M_p(T)=\int_{\mathbb R}w(R/T)|H_T(R)|^p\,dR.
\]

All constants can depend on these fixed functions, their required finitely many seminorms, and the displayed fixed exponents. They do not depend on the real \(T,R\), integer cutoff, or particular resonance configuration. The elementary representation estimate used throughout is \(r_2(n)\le4d(n)\ll_\kappa n^\kappa\) for every fixed \(\kappa>0\).

The frozen improvement target is, for some fixed

\[
 0\le\eta<13\theta_{LY}-4,
 \qquad \theta_{LY}=\frac{3292+25\sqrt{1717}}{13762},
\]
\[
 \mathcal M_{12}(T)\ll_\varepsilon T^{1+2\eta+\varepsilon}.
                                                                    \tag{201.A4}
\]

It suffices for \(\int_{Y/2}^{3Y}|P(x)|^{12}dx\ll_\varepsilon Y^{4+\eta+\varepsilon}\). The value \(\eta=0\) is admissible in the target but is not proved. The threshold is about \(0.0882812876628\), as recorded in the frozen strategy.

## 3. Proof and derivation

### 3.1. Sharp count, inclusive jumps, and Poisson summation

Define

\[
 S_\delta(R)=\sum_{m\in\mathbb Z^2}(1_{B_R}*\rho_\delta)(m).
\]

The convolved indicator belongs to \([0,1]\), equals one for \(|m|\le R-\delta\), and equals zero for \(|m|>R+\delta\). Therefore, allowing both annular endpoints in an upper bound,

\[
 |N(R)-S_\delta(R)|
 \le\sum_{(R-\delta)^2\le n\le(R+\delta)^2}r_2(n)
 \ll_\kappa(R\delta+1)T^{2\kappa}
 \ll_\kappa T^{1/2+2\kappa}.                                      \tag{201.A5}
\]

This estimate remains valid when \(R^2\) is an integer. It pays the complete jump \(r_2(R^2)\), rather than imposing a half-weight boundary convention. There is no moving-radius differentiation or replacement of \(\delta\) by \(R^{-1/2}\).

For completeness, Poisson summation here follows directly by periodizing the function \(f=1_{B_R}*\rho_\delta\in C_c^\infty(\mathbb R^2)\). Its periodization is smooth on the two-dimensional torus, with Fourier coefficients \(\widehat f(k)\). Repeated integration by parts makes its Fourier series absolutely convergent. Evaluation at zero gives \(\sum_m f(m)=\sum_k\widehat f(k)\), without a nonsmooth-boundary summation convention.

Polar coordinates and the Bessel identities audited in Section 6 give, for \(s=|\xi|>0\),

\[
 \widehat{1_{B_R}}(\xi)
 =2\pi\int_0^R rJ_0(2\pi rs)\,dr
 =\frac R{s}J_1(2\pi Rs),
 \qquad \widehat{1_{B_R}}(0)=\pi R^2.
\]

The convolution preserves the integral exactly. Radiality of the transform then yields

\[
 S_\delta(R)-\pi R^2
 =R\sum_{n\ge1}\frac{r_2(n)}{\sqrt n}
       \Psi(\delta\sqrt n)J_1(2\pi R\sqrt n).                    \tag{201.A6}
\]

This identity is absolutely convergent for every fixed positive \(T,R\).

### 3.2. Bessel normalization and its entire summed remainder

For the fixed order one and positive \(z\), the large-argument formula is

\[
 J_1(z)=\sqrt{\frac2{\pi z}}\cos(z-3\pi/4)+O(z^{-3/2}).
\]

Since \(z=2\pi R\sqrt n\gg T\), insertion in (201.A6) gives exactly the leading coefficient \(\sqrt R/\pi\), and a remainder bounded by

\[
 C R^{-1/2}\sum_{n\ge1}r_2(n)n^{-5/4}|\Psi(\sqrt{n/T})|
 \le C R^{-1/2}\sum_{n\ge1}r_2(n)n^{-5/4}
 \ll R^{-1/2}.                                                     \tag{201.A7}
\]

The last series converges on choosing any fixed \(0<\kappa<1/4\). Combining (201.A5)--(201.A7) proves (201.A1), after renaming the arbitrarily small exponent. The large-argument constant is uniform over every \(n\ge1\) and \(R\in[cT,CT]\) once \(T\) is sufficiently large; the remaining bounded \(T\)-interval is absorbed by the constant.

### 3.3. Uniform tails and legitimate infinite moment expansion

For fixed \(\kappa>0\),

\[
 \sum_{n\ge1}|a_n(T)|\ll_{\rho,\kappa}T^{1/4+\kappa},\qquad
 \sum_{n\ge1}|a_n(T)|^2\ll_\kappa1\quad(\kappa<1/4).               \tag{201.A8}
\]

For every \(U\ge T\) and \(A>1/2+2\kappa\), a direct integral comparison gives

\[
 \sum_{n>U}|a_n(T)|
 \ll_{\rho,A,\kappa}
 T^{A/2}U^{1/4+\kappa-A/2}.                                       \tag{201.A9}
\]

In particular, fix any \(\alpha>0\) and put \(U=\lfloor T^{1+\alpha}\rfloor\), adjusting harmlessly to \(U\ge T\). By choosing \(A\) large enough, the tail in (201.A9) is \(O(T^{-K})\) for any prescribed fixed \(K\). Uniformly in all real \(R\), the same bound applies to \(H_T-H_{T,U}\). Since \(|H_T|+|H_{T,U}|\ll T^{1/4+\kappa}\),

\[
 |\mathcal M_{12}(T)-\mathcal M_{12,U}(T)|
 \ll T^{15/4+11\kappa-K}.                                        \tag{201.A10}
\]

Thus the moment truncation error can also be made \(O(T^{-B})\) for every prescribed \(B\). The analogous second-moment error is \(O(T^{5/4+\kappa-K})\). No claim is made that truncating sharply at \(n=T\) has a negligible tail.

For fixed \(T\), expanding a product of twelve infinite sums is justified by \((\sum|a_n|)^{12}<\infty\). Integration against the compactly supported weight is justified by the same absolute majorant. Using

\[
 \cos(2\pi R\sqrt n-3\pi/4)
 =\frac12\sum_{\sigma=\pm1}e(\sigma R\sqrt n-3\sigma/8)
\]

and then \(R=Tu\) proves (201.A2). This also handles every configuration with one or more large indices; there is no omitted tail stratum.

### 3.4. The fixed-window second moment

Expand the product of two cosines. The difference-frequency diagonal is

\[
 \frac T2\widehat w(0)\sum_n a_n(T)^2.                              \tag{201.A11}
\]

Here are full bounds on its complement. Fix \(0<\alpha<1\), for example \(\alpha=1/2\), and use the cutoff from Section 3.3. For distinct \(m,n\le U\),

\[
 T|\sqrt m-\sqrt n|
 =\frac{T|m-n|}{\sqrt m+\sqrt n}
 \ge\frac{T}{2\sqrt U}|m-n|=q_T|m-n|,
 \qquad q_T\gg T^{(1-\alpha)/2}.
\]

Repeated integration by parts in the transform of \(w\) gives

\[
 \sup_m\sum_{n\ne m}|\widehat w(T(\sqrt m-\sqrt n))|
 \ll_{w,A}q_T^{-A}\quad(A>1).
\]

The elementary Schur estimate, or \(2|a_ma_n|\le a_m^2+a_n^2\), bounds the difference offdiagonal by \(O(Tq_T^{-A}\sum a_n^2)\). This is \(O(T^{-B})\) after choosing \(A\) sufficiently large. The sum-frequency term has \(\sqrt m+\sqrt n\ge2\), and its absolute value is at most

\[
 C_{w,A}T^{1-A}(\sum_n|a_n(T)|)^2
 \ll T^{3/2+2\kappa-A}.
\]

It too is rapidly decreasing. Restoring the tails proves (201.A3). Dominated convergence also gives

\[
 \sum_n a_n(T)^2\longrightarrow
 \sum_{n\ge1}r_2(n)^2n^{-3/2}>0,
\]

so this is the correct nonzero normalization scale for \(H_T\). It is not a claim of an asymptotic constant for the sharp \(P\), whose smoothing error is larger.

Using (201.A1), \(dx=2R\,dR\), and \(R\asymp T\),

\[
 \int_{Y/2}^{3Y}|P(x)|^2dx
 \ll T^2\mathcal M_2(T)+T^{3+\varepsilon}
 \ll T^{3+\varepsilon}=Y^{3/2+\varepsilon}.                        \tag{201.A12}
\]

### 3.5. Full exact resonances, including nonpairings

Put \(\Delta(\boldsymbol\sigma,\boldsymbol n)=\sum_j\sigma_j\sqrt{n_j}\). Let \(\mathcal D_{12}(T)\) be the restriction of (201.A2) to \(\Delta=0\). The following elementary absolute estimate is sufficient:

\[
 \sum_{\boldsymbol\sigma}\ 
 \sum_{\Delta(\boldsymbol\sigma,\boldsymbol n)=0}
 \prod_j r_2(n_j)n_j^{-3/4}<\infty.                               \tag{201.A13}
\]

To verify it, write uniquely \(n_j=d_js_j^2\), with \(d_j\) squarefree. Distinct squarefree radicals are linearly independent over \(\mathbb Q\). One direct algebraic justification is to collect the finitely many primes involved. Their squareclasses are independent by unique factorization. Inductively, the rational numbers which become squares in \(\mathbb Q(\sqrt{p_1},\ldots,\sqrt{p_r})\) have precisely the squareclasses generated by those primes: in the next quadratic extension, if \((a+b\sqrt p)^2\) is rational, uniqueness of the quadratic decomposition forces \(ab=0\), reducing to the preceding stage. This also proves each extension has degree two. The independent sign-change automorphisms consequently act on the products of prime radicals by distinct characters. Character orthogonality isolates each coefficient of a putative linear relation, proving independence, including the radical \(\sqrt1=1\).

Thus every represented squarefree class in a resonance satisfies \(\sum_{j:d_j=d}\sigma_js_j=0\), and contains at least two indices. Partition \(\{1,\ldots,12\}\) by these classes. Fix \(0<\kappa<1/4\), and put \(b=3/4-\kappa>1/2\). The contribution of a block of size \(k\ge2\), even after discarding its integer relation, is at most a constant times

\[
 \sum_{d\ge1}d^{-bk}
 \prod_{j=1}^k\sum_{s_j\ge1}s_j^{-2b}<\infty.                     \tag{201.A14}
\]

There are finitely many set partitions and sign patterns. Allowing different blocks to use the same \(d\) only enlarges the positive upper bound. This proves (201.A13), uniformly in all cutoffs and \(T\), and therefore \(|\mathcal D_{12}(T)|\ll T\). It also justifies every infinite-limit passage in the exact-resonance part independently of mollifier decay.

For the optional sign assertion, truncate at finite \(U\) and hold \(T\) fixed. The long-time mean of the nonnegative trigonometric polynomial \(H_{T,U}(R)^{12}\) is exactly its zero-frequency coefficient. It is nonnegative. Taking \(U\to\infty\) gives \(\mathcal D_{12}(T)\ge0\), since \(T\widehat w(0)>0\). This is an auxiliary constant-coefficient mean identity; it supplies no finite-window offdiagonal estimate.

Pairings do not enumerate (201.A13). For example,

\[
 \sqrt d+\sqrt d+\sqrt{16d}
 =\sqrt{4d}+\sqrt{4d}+\sqrt{4d}
\]

is a nonpairing relation, and for \(d=1\) every coefficient is physically present. Add three cancelling pairs to obtain twelve terms. The proof includes this and unequal sign counts automatically; there was no Gaussian-pairing assumption.

### 3.6. The displaced signed offdiagonal and physical near resonances

Define the actual nonzero-frequency aggregate by

\[
 \mathcal O_{12}(T)=\frac{T}{2^{12}}\operatorname{Re}
 \sum_{\boldsymbol\sigma\in\{-1,1\}^{12}}
 e\!\left(-\frac38\sum_j\sigma_j\right)
 \sum_{\substack{\boldsymbol n\in\mathbb N^{12}\\
                  \Delta(\boldsymbol\sigma,\boldsymbol n)\ne0}}
 \left(\prod_j a_{n_j}(T)\right)
 \widehat w(-T\Delta(\boldsymbol\sigma,\boldsymbol n)).            \tag{201.A15}
\]

Conjugate sign patterns make the original sum real: \(\boldsymbol\sigma\mapsto-\boldsymbol\sigma\) conjugates both the constant phase and the Fourier kernel. Exactly,

\[
 \mathcal M_{12}(T)=\mathcal D_{12}(T)+\mathcal O_{12}(T),
 \qquad 0\le\mathcal D_{12}(T)\ll T.                              \tag{201.A16}
\]

The displacement is substantive. If, as an illustrative allowed choice, \(w(u)=v(u-u_0)\) for a real even bump \(v\), then

\[
 \widehat w(-T\Delta)=e(u_0T\Delta)\widehat v(T\Delta).            \tag{201.A17}
\]

The phase \(e(u_0T\Delta)\) cannot be erased in a proof of the requested signed aggregate. For general real \(w\), its Fourier transform need not even be real. The coefficients \(a_n(T)\) also need not all be positive.

The second-moment separation argument cannot be extended to twelve factors merely by comparing individual roots. There are physically represented nonzero near resonances:

\[
 \Delta_m=\sqrt{m^2+1}+\sqrt{m^2+49}-2\sqrt{m^2+25}
 =-144m^{-3}+O(m^{-5})\ne0.
\]

All three indices are sums of two squares, namely \((m,1)\), \((m,7)\), and \((m,5)\). Strict concavity gives the nonzero sign without asymptotics. Choose a sufficiently small fixed \(u_*>0\) with \(\Psi(u_*)>0\), and set \(T=m^2/u_*^2\). All indices are \(\asymp T\), all their mollifier factors are positive for large \(m\), and \(T\Delta_m\to0\). Four cancelling pairs turn this into a twelve-root nonzero relation with six signs of each kind. Accordingly \(\widehat w(-T\Delta_m)\to\widehat w(0)>0\). This control proves the existence of nonzero terms in the effective near-resonant range. Its small individual weight does **not** establish a power-sized lower bound for \(\mathcal O_{12}\), or refute (201.A4).

### 3.7. Reconstruction and the pointwise bridge

For \(p=12\), (201.A1), \(w=1\) on the desired radius interval, and \(dx=2R\,dR\) give

\[
 \int_{Y/2}^{3Y}|P(x)|^{12}dx
 \ll T^7\mathcal M_{12}(T)+T^{8+\varepsilon}.
\]

The power \(T^7\) consists of \(R^6\) from the twelfth power of \(\sqrt R\) and \(R\) from the Jacobian. The entire smoothing error costs \(T^{8+\varepsilon}=Y^{4+\varepsilon}\), so is safe for every \(\eta\ge0\). Uniform moment bounds for \(P\) on fixed comparable intervals conversely bound \(\mathcal M_{12}\) at the same exponent after division by \(\sqrt R\); the fixed support of \(w\) requires only a bounded number of comparable windows. No asymptotic equality of the sharp and smoothed twelfth moments is asserted.

For clarity, the persistence implication uses inclusivity correctly. If \(X\in[Y,2Y]\), \(V=|P(X)|\), and \(h\ge0\), monotonicity gives

\[
 P(X+h)\ge P(X)-\pi h,\qquad P(X-h)\le P(X)+\pi h.
\]

Use the forward interval when \(P(X)>0\), and the backward interval otherwise, up to length \(V/(2\pi)\). On that interval \(|P|\ge V/2\). An accepted sublinear bound keeps the interval inside \([Y/2,3Y]\) for large \(Y\). Hence the moment dominates \(V^{13}/(2^{13}\pi)\), yielding \(P(X)\ll X^{(4+\eta)/13+\varepsilon}\) if the target moment were established. An ideal twelfth moment alone would give \(4/13\), not one quarter.

## 4. First doubtful or unproved step and the quantitative deficit

After the proved reduction, the missing statement is exactly

\[
 \boxed{\quad
 \mathcal O_{12}(T)\le C_{\rho,w,\eta,\varepsilon}
 T^{1+2\eta+\varepsilon}
 \quad\text{for every }T\ge2,\quad
 0\le\eta<13\theta_{LY}-4.\quad}                                  \tag{201.A18}
\]

The aggregate in (201.A15), including all actual coefficients, signs, and the displaced Fourier factor, is the object of this inequality. Because \(\mathcal M_{12}\ge0\) and \(\mathcal D_{12}\ll T\), its negative part is already \(O(T)\). For \(\eta\ge0\), (201.A18) is equivalent at the exponent level to the complete target (201.A4). Bounds for each sign pattern or each frequency difference after taking absolute values are unnecessary stronger demands.

There is no proof here that an absolute-value route is impossible. Its unproved higher-order spacing input must not be mistaken for an established estimate. In particular, (201.A13) controls only \(\Delta=0\), and cannot control \(0<|\Delta|\lesssim T^{-1}\). The physical family in Section 3.6 explains the first failure of the second-moment argument at higher order.

The complete bound presently obtained from the **accepted second moment plus the accepted Li--Yang pointwise theorem** is

\[
 \int_{Y/2}^{3Y}|P(x)|^{12}dx
 \le\|P\|_\infty^{10}\int_{Y/2}^{3Y}|P(x)|^2dx
 \ll_\varepsilon Y^{3/2+10\theta_{LY}+\varepsilon}
 =Y^{4+\eta_2+\varepsilon},\qquad
 \eta_2=10\theta_{LY}-\frac52.                                    \tag{201.A19}
\]

Equivalently, (201.A1) gives \(\|H_T\|_\infty\ll T^{2\theta_{LY}-1/2+\varepsilon}\), so (201.A3) yields

\[
 \mathcal M_{12}(T)\ll T^{20\theta_{LY}-4+\varepsilon}.
\]

This baseline has \(\eta_2\approx0.6448317597406\), leaving the exact positive deficit

\[
 \eta_2-(13\theta_{LY}-4)=\frac32-3\theta_{LY}
 \approx0.5565504720778
\]

in the \(Y\)-moment exponent, or \(3-6\theta_{LY}\approx1.1131009441556\) in the \(T\)-moment exponent. A strict improvement over Li--Yang requires saving **more** than this margin relative to (201.A19). This is the baseline from the sources used by this task, not a claim that no audited higher moment can improve the baseline. The separate primary-source task owns that comparison. No lower-moment extrapolation is used as a twelfth-moment theorem.

## 5. Required control tests and outcomes

These are exact analytic/algebraic checks, not numerical experiments.

| Control | Outcome |
|---|---|
| `whole_discrepancy_scope` | PASS. Start from the complete lattice count, including the origin and every nonzero Fourier lattice point; no M1/M2 sector is substituted. |
| `fixed_window_smoothing` | PASS. \(\delta=T^{-1/2}\) and \(a_n(T)\) are fixed throughout the radius integration. |
| `inclusive_jump_error` | PASS. (201.A5) includes both annular endpoints and the entire integer-radius jump. |
| `bessel_and_fourier_normalization` | PASS. Disk transform is \(RJ_1(2\pi R|k|)/|k|\); leading factor is \(\sqrt R/\pi\); the cosine phase is \(-3\pi/4\); the moment kernel is \(T\widehat w(-T\Delta)\). |
| `uniform_tail_control` | PASS. (201.A9)--(201.A10) control the infinite series, every opened moment tail, and the cutoff used in the second moment. The scale \(n=T\) is a transition, not an exact endpoint. |
| `all_sign_patterns` | PASS. All 4096 patterns occur with phase \(e(-3\sum\sigma_j/8)\); pairing conjugates preserves the real aggregate. |
| `nonpairing_exact_resonances` | PASS as a candidate derivation. (201.A13)--(201.A14) include every class; the \(1+1+4=2+2+2\) radical relation explicitly defeats pairing-only enumeration. Independent acceptance belongs to the conductor. |
| `displaced_offdiagonal_phase` | PASS for the identity; OPEN for the estimate. (201.A15), (201.A17), and the nonzero physical \(\Delta_m\) retain what a positive spacing majorant discards. |
| `second_moment_normalization` | PASS. (201.A3), then the Jacobian, recovers \(Y^{3/2+\varepsilon}\); no sharp moment constant is inferred. |
| `moment_to_pointwise_exponents` | PASS conditionally. \(T^7\times T^{1+2\eta}=Y^{4+\eta}\), followed by one-sided persistence, gives \((4+\eta)/13\). |
| `primary_source_hypotheses` | PASS for the standard Bessel inputs below. Poisson is proved in the exact smooth setting. The accepted Li--Yang node is inherited without broadening its theorem scope. |
| `no_parent_or_exponent_overclaim` | PASS. (201.A18) is explicitly open; GC-target, M1, M2, M9, and the pointwise benchmarks remain unchanged. |

Additional sign check: \(e(-3\sum\sigma/8)\) may be negative or nonreal before conjugate pairing. Thus even exact resonances need not contribute positively term by term. The nonnegativity of the **total** diagonal follows from the separate long-time-mean argument, not from termwise positivity. A finite displaced interval is never replaced by independent random squarefree phases.

## 6. Dependencies, exact artifacts, and source hypotheses

Repository context read:

1. `protocol.md`.
2. `state/proof_obligations.yml`, raw hash shown above; relevant nodes checked as structured records: `GC-target` (open), `GC-global-real-second-moment-density-one-quarter` (proved_internal), `GC-external-Li-Yang-theta-star` (proved_external_dependency), and `Divisor-bound-elementary` (proved_internal).
3. `state/active_campaign.yml`, Round 201 active manifest.
4. `rounds/codex-managed/gc-whole-discrepancy-twelfth-moment/briefs/whole_moment_analytic_attack.md`.
5. `strategy/round201_whole_discrepancy_twelfth_moment_strategy.md`.
6. `strategy/gauss_circle_strategy_review_2026-09-23.md`.
7. `rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/synthesis.md`.

The strategy review's statement about a then-unlocated Round 200 is historical prose. This task follows the current Round-201 manifest and does not infer present graph status from that earlier observation. No unrelated future-dated literature claim in the review is imported into this proof.

Standard-function source cards, checked directly on 2026-09-23:

- **NIST DLMF, 10.9.1:** [Bessel's integral](https://dlmf.nist.gov/10.9.E1). It supplies the angular identity for \(J_0\), specialized here to real nonnegative argument. The imaginary angular part vanishes by symmetry. This proves the polar integral used for the disk transform; no oscillatory asymptotic is needed at this step.
- **NIST DLMF, 10.6.6:** [Bessel derivative identity](https://dlmf.nist.gov/10.6.E6). Specialize the cylinder function to \(J\), \(k=1\), and \(\nu=1\), obtaining \((zJ_1(z))'=zJ_0(z)\). With \(z=2\pi rs\) and the regular value at zero this evaluates the disk's radial integral. There is no varying-order limit.
- **NIST DLMF, 10.17.2--10.17.3 and 10.17(iii):** [fixed-order large-argument expansion and real-argument remainder](https://dlmf.nist.gov/10.17). The expansion holds for fixed order in a closed sector away from the negative real axis. Here \(\nu=1\), \(z>0\), and \(z\gg T\). For an explicit remainder route, keep one term in each real cosine/sine series: the stated conditions on both truncation indices hold at index one. The sine term is \(O(z^{-1})\) inside the prefactor, and the controlled remaining terms are smaller. This gives the uniform \(O(z^{-3/2})\) remainder used in (201.A7). No large-order asymptotic or bound near zero is imported.

Poisson summation is derived by smooth periodization in Section 3.1, with its complete hypotheses checked there. The squarefree independence argument, summability, Fourier-kernel expansion, second-moment separation, and persistence bridge are internal derivations. The exponent in (201.A19) uses only the exact accepted Li--Yang graph theorem for real inclusive \(X\), including its existing scope restrictions; it does not rely on the paper's unaccepted general propositions.

## 7. Recommended state effect

Recommend **retain** the frozen twelfth-moment improvement as open, with (201.A18) as its exact remaining analytic estimate. Recommend **candidate subordinate promotion after the required independent seams** for the fixed-window whole-source reduction, all-sign moment identity with uniform tails, and the exact-resonance \(O(T)\) kernel. The second-moment derivation is an independent normalization check and gives no stronger sharp exponent than the existing node.

Recommend **no change** to `GC-target`, `GC-external-Li-Yang-theta-star`, M9-M1, M9-M2, endpoint uniformity, M9, or either conditional bridge. The quantified deficit is a failure to close this route with the used inputs, not a refutation of the actual twelfth-moment target. No new round is designed here; this bounded task ends with this report.
