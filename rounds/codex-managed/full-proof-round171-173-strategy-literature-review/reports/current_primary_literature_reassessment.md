# Round 174 current-primary-literature reassessment

**Audit date:** 2026-08-27 (Asia/Shanghai).  The arXiv currency pass screens submissions returned through this date and checks the current retrieved versions of plausible matches; the mathematical scope is the frozen Round-174 scope.  Only official journal pages, author-hosted manuscripts, and arXiv records/manuscripts are used to certify theorem content.  Search-engine snippets and secondary summaries were used only to locate primary records, never to certify a claim.

## 1. Result

### 1.1 Dated source-audit lemma

As of 2026-08-27, the strongest source-audited **unrestricted pointwise** Gauss-circle upper exponent found in the designated primary record remains

\[
 \theta_*=
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots,
\]

in Li--Yang, arXiv:2308.14859v2, Theorem 1.2.  Here the area variable is

\[
 R(X)=\sum_{m^2+n^2\le X}1-\pi X,
\]

and the theorem asserts, for every \(\varepsilon>0\),

\[
 R(X)=O_\varepsilon(X^{\theta_*+\varepsilon}).
\]

This is a pointwise statement in the unrestricted real parameter \(X\), not an average, an almost-all statement, a smoothed count, or a restricted-arithmetic-subset result.  Its present bibliographic status is still **preprint**: the official arXiv record has only v1 (2023-08-28) and v2 (2023-09-14), and Xuerui Yang's author page still lists it as a preprint.  In this project it remains admissible only through the already repaired narrow import of Theorem 1.2 recorded in `sources/li_yang_2023.md`; the unrepaired general statements in that manuscript are not promoted.

No audited primary source proves any of the frozen project estimates `hard-TOP/t=1`, `K17a`, `K26`, the remaining `BAL` or `UNBAL` label owners, either direct `M1` parent, the complete `GAR` alternative, the hard endpoint/cardinal bridge, or the full theorem.  In particular, the August-2026 papers newly visible at this cutoff do not change that conclusion:

- Tang's short twisted second-moment reciprocity has one common height, two prime twist parameters, and a Gaussian weight;
- Ji's four-swap Gaussian-Hecke moment is a smooth average over a fixed CM family and explicitly leaves its twisted version conjectural;
- Liyang Yang's new Fourier toric reciprocity is a Hecke-character family identity with constant, residual, and continuous dual pieces;
- Milićević--Robinson--Shupe treat complete products of shifted normalized Kloosterman sums at one odd prime-power modulus;
- Mohammadi treats finite-field boxes and the kernel \(axy+b(xy)^{-1}\);
- Shi analyzes one smooth Bessel--Kuznetsov transform, not the arithmetic trace formula or a signed project aggregate;
- Cushman--Demeter--Wu count exact six-term additive coincidences on a convex curve;
- Gao--Li--Qi prove a pointwise subconvex bound for a fixed \(\mathrm{GL}_2\) representation twisted by one Archimedean Hecke character.

All first fail an exact project hypothesis before their saving exponent can be imported.

### 1.2 Interface conclusion

The closest results remain strategically informative but non-certifying:

1. fixed-modulus bilinear Kloosterman estimates do not supply the signed varying-modulus vector estimate required by `UNBAL`;
2. determinant and shifted-convolution theorems do not accept the project actual symbol, moving square-root phase, hard endpoints, or the full range of shifts required by `K17a/K26`;
3. exponent-pair and square-root-sum results apply to scalar or averaged coefficient families, not to the project selectors and outer signs;
4. reciprocity and hybrid-moment identities retain one shared height or average over a different arithmetic family, and they carry main, residual/degenerate, cuspidal, and continuous pieces not present in any proved project parameter map;
5. positive spectral/decoupling norms do not bypass the Round-171 `BAL` positive-capacity obstruction, the Round-172 `K26` positive-capacity obstruction, or the Round-173 tangent-chart self-return.

**Result:** a rigorous dated no-match result.  The current literature supplies no admissible promotion and no replacement exponent.  Recommended graph effect: **no change**.

## 2. Exact statement and hypotheses

### 2.1 Frozen project interfaces tested

The literature was tested against the following exact interfaces inherited from the selected Round-174 context.

| Interface | Exact required statement or structure | Positive/unsigned capacity that must not be mistaken for a proof |
|---|---|---|
| full signed `t=1` moving product collar | \(I_\eta=E_0+\frac{i}{2}\sum^{\rm phys}_{Q,R}\frac{g(Q,R)}{QR}\sum_{k\ \mathrm{odd}}\chi_4(k)\sum_{\ell\ne0}\widetilde B(k/4Q,\ell/R)\), \(E_0\ll L^2/J\), with stationary collar \(k\ell=XQR\), \(Q\ell\le Rk\le4Q\ell\), and target \(\ll L^{3/2}X^\varepsilon\) | \(\sqrt{JL}=L^{3/2}(H/L+O(L^{-1}))\); a signed relative gain \(L/H\) is needed |
| `K17a` | \(\Re C_{{\rm rem},R_0,2,{\rm opp},g<\gamma L}\ll L^2X^\varepsilon\), \(R_0=\lceil L\rceil\) | \(L^3\) |
| `K26` | \(\Re\sum_{R_0\le r<M_L,\ 2\mid r}(1-r/M_L)\sum_N c^{\rm rem}_{N+r}\overline{c^{\rm rem}_N}e(J(\sqrt{N+r}-\sqrt N))\ll L^3X^\varepsilon\), \(M_L\asymp L^2\) | \(L^4\) |
| Round-172 exact common-frequency form | \(\mathcal N_{R,S}=\frac18\Re\sum_{\epsilon=0}^1\sum_{k,k'\,\rm odd}\sum_{\ell,\ell'\ne0}\chi_4(k)\chi_4(k')\int_0^1B_{R,S}(\theta)U_{k,\ell}^{\epsilon}(\theta)\overline{U_{k',\ell'}^{\epsilon}(\theta)}\,d\theta\) | the ordinary zero-frequency sector is safe only after recombination; physical zero diagonal does not delete the fixed dual diagonal |
| `BAL`, surviving \(j=1\) double-far family | \(h'=h+p,\ k'=k+q\), \(\Delta+\rho=q(2h+p)\), \(\Delta-\rho=p(2k+q)\), and for \(p=2s\) the literal sign \((-1)^s\) must survive | the retained \(P_{++}\) component and the mixed-Abel primitive ramp have \(L^4\) capacity against an \(L^3\) target |
| `UNBAL` | with \(X=N_0+\xi\), \(D=X^\delta\), \(L=X^\ell\), \(R=X/D\), \(K=XL/D^2\), \(\Delta=D/L\), \(a=\delta-\ell\), prove a signed vector estimate in \(1/4\le\delta<1/2\), \(0\le\ell<\delta-1/4\), \(178\ell+1638\delta>463\) | scalar projective inflation and blockwise norm losses exceed the required gain |
| direct route | both direct `M1` parents, all hard `M2` channels (`TOP`, `BAL`, `UNBAL`), endpoints, `M9`, bridge | proving one local theorem is not a full proof |
| alternative route | complete `GAR` may replace only blockwise `M1`; all `M2` and endpoint packages remain | `GAR` is not a blockwise `M1` estimate |

The `UNBAL` row that a source would have to control is, for odd \(g,n\), \(gn\asymp R\),

\[
 b_{g,n}(j)=\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n),
 \qquad
 \widehat\gamma_{g,n}(h)=\frac1n\sum_{\substack{j\in\mathcal J\\(j,n)=1}}
 b_{g,n}(j)e(-h\bar j_n/n),
\]

and the centered row contains

\[
 \frac{\chi_4(g)\chi_4(n)}{gnj}
 W\!\left(\frac{X}{gnD}\right)q_L\!\left(\frac{4Xj}{gn^2}\right)
 e\!\left(\frac{\xi j}{n}+\frac{h\bar n_j}{j}-\frac{h}{jn}\right)
 S_{\rm proj}(N_0,h;n),
\]

for \(1\le h<n\), where

\[
 S_{\rm proj}(N_0,h;n)=\sum_{x\bmod n}^{*}e\!\left(\frac{N_0\bar x+hx}{n}\right).
\]

The missing saving is

\[
 \mu(a)=
 \begin{cases}
 a-\frac14,&\frac14<a\le\frac13,\\[2mm]
 \frac{1-2a}{4},&\frac13\le a<\frac12.
 \end{cases}
\]

Any imported theorem must preserve the displayed characters, phases, stars, full \(h\)-range, non-coprime center cases, hard support, and the placement of every absolute value.

### 2.2 Unrestricted pointwise Gauss-circle exponent

#### Li--Yang

Primary record: Xiaochun Li and Xuerui Yang, *An improvement on Gauss's circle problem and Dirichlet's divisor problem*, [arXiv:2308.14859v2](https://arxiv.org/abs/2308.14859), manuscript [HTML](https://arxiv.org/html/2308.14859v2).  The official record lists submission 2023-08-28 and v2 on 2023-09-14.

Theorem 1.2 defines

\[
R(X)=\sum_{m^2+n^2\le X}1-\pi X,
\qquad
\Delta(X)=\sum_{n\le X}d(n)-X\log X-(2\gamma-1)X,
\]

and states, for every \(\varepsilon>0\),

\[
R(X),\Delta(X)=O_\varepsilon
\left(X^{\frac{3292+25\sqrt{1717}}{13762}+\varepsilon}\right).
\]

The quantifier is pointwise in unrestricted \(X\).  There is no smoothing or exceptional set in the theorem statement.  The project source card records five repairs and two range supplements needed for the narrow theorem import.  Therefore the certified project fact is the repaired final Theorem 1.2 only, not an unrestricted import of Proposition 3.1, Theorem 4.2, or their proof chain.

The author status page is [Xuerui Yang's publication list](https://sites.google.com/view/xuerui-yang), which continues to label the paper “Preprint.”

#### Huxley normalization control

Primary journal record: M. N. Huxley, *Exponential sums and lattice points III*, Proceedings of the London Mathematical Society 87 (2003), [official journal page](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/S0024611503014485).  The journal abstract gives exponent \(K=131/208\) in the **radius/curvature** variable.  For the circle area variable \(X=R^2\), this is \(X^{K/2}=X^{131/416}\).  Thus a source writing \(131/208\) directly in the area variable has changed normalization and is not evidence for an improvement.

#### Later records screened

- Peng Gao, *On the Gauss circle problem over smooth numbers*, [arXiv:2604.23918](https://arxiv.org/abs/2604.23918), concerns the restricted smooth-number weighted count \(\Psi_G(x,y)\), with an asymptotic only in specified \((x,y)\)-ranges.  It is not the unrestricted count.
- A. J. E. M. Janssen--Cloitre's Fibonacci-equivalence record, [arXiv:2607.20960](https://arxiv.org/abs/2607.20960), gives an equivalence with a fractional-part remainder; it does not supply a smaller pointwise upper exponent.
- K. Mahatab, [arXiv:2504.17032](https://arxiv.org/abs/2504.17032), proves omega/lower-bound phenomena, not a stronger upper bound.
- The official arXiv currency pass through 2026-08-27 found no later indexed unrestricted pointwise upper theorem.  This is a dated indexed/source-audited conclusion, not a claim about manuscripts absent from the searched primary indexes.

#### Withdrawn Bourgain--Watt dependency

J. Bourgain and N. Watt, *Mean square of zeta function, circle problem and divisor problem revisited*, [arXiv:1709.04340](https://arxiv.org/abs/1709.04340), is withdrawn in v2.  The withdrawal notice identifies gaps in Propositions 2, 3, and \(1'\), and says Theorems 1--3 lose theorem status.  Those withdrawn propositions and Theorems 1--3 cannot certify any project step.  Only algebraic identities that have been explicitly audited and independently rederived may remain in the repaired Li--Yang chain, including the retained Section-7 two-sign/two-range sawtooth algebra and separately rederived symbolic spacing material; no withdrawn theorem statement is imported as a black box.

### 2.3 Fixed-modulus Kloosterman, Kuznetsov, and large-sieve results

#### Blomer--Pascadi 2026

V. Blomer and A. Pascadi, *Bilinear forms with Kloosterman sums via quadratic characters*, [arXiv:2607.24311v1](https://arxiv.org/abs/2607.24311), submitted 2026-07-27.  Their unnormalized convention is

\[
S_{\rm src}(u,v;c)=\sum_{x\bmod c}^{*}e((ux+v\bar x)/c).
\]

Theorem 1.1: for \(c>0\), integer \(N\in[1,c]\), intervals \(I,J\) of lengths at most \(N\), arbitrary complex \(\alpha_m,\beta_n\), and \((a,c)=1\),

\[
\left|\sum_{\substack{m\in I,n\in J\\(m,n,c)=1}}
\alpha_m\beta_nS_{\rm src}(am,n;c)\right|
\ll \|\alpha\|_2\|\beta\|_2c^{1+o(1)}
\left(\frac{N^{1/8}}{c^{3/32}}+\frac{N^{5/16}}{c^{3/16}}+\frac{N^{2/3}}{c^{7/18}}\right).
\]

If \(I=J=[1,N]\), the printed theorem removes the joint gcd condition.  At \(N=c^{1/2}\), the first term gives the advertised \(c^{-1/32}\) saving.

Theorem 5.5 permits lengths \(M,N\le c\) and gives the same norm factor times \(c^{1+o(1)}\mathcal H(M,N,c)\), where

\[
\begin{aligned}
\mathcal H={}&
M^{1/8}\frac{((c+MN)(c+N^2))^{1/16}}{c^{1/4}}
\min(c/M,c^{1/2})^{1/16}\\
&+\left(\frac{N^2}{c^2}+\frac{N^{1/2}M(c+N^2)}{c^{5/2}}\right)^{1/16}
+\frac{M^{1/3}+N^{1/3}}{c^{1/5}}\\
&+\frac{M^{1/2}N^{1/6}+M^{1/6}N^{1/2}}{c^{7/18}}
+\frac{M^{1/15}+N^{1/15}}{c^{1/15}}.
\end{aligned}
\]

Theorem 5.7, for arbitrary intervals, arbitrary coefficients and \((m,c)=1\), gives

\[
\ll \|\alpha\|_2\|\beta\|_2c^{1+o(1)}
\left(\frac{(MN)^{1/2}}{c^{3/4}}+\frac{N^{1/2}}{c^{1/2}}+\frac{M^{1/2}}{c^{1/4}}\right).
\]

Theorem 1.6 is a **positive exceptional-spectrum** large sieve at fixed level/cusp:

\[
\sum_{\lambda_j<1/4}\mathcal X^{2\theta_j}
\left|\sum_{n\asymp N}\alpha_n\rho_{j,\mathfrak a}(n)\right|^2
\ll(qN)^{o(1)}(1+N/q)\|\alpha\|_2^2,
\]

where

\[
\mathcal X=1+q/N+
\min(q^{18/11}/N^{23/11},q^{16/13}/N^{18/13},q^{32/29}/N^{33/29})+q^2/N^3.
\]

It contains neither the regular Maaß, holomorphic, Eisenstein, nor diagonal/main pieces of a full Kuznetsov formula.

#### Pascadi 2025/2026

A. Pascadi, *Bilinear forms with Kloosterman sums and the exceptional spectrum*, [arXiv:2511.08445v2](https://arxiv.org/abs/2511.08445), current version 2026-06-21.

Theorem 1.1: for \(c,M,N>0\), \(M,N\ll c^{1/2+o(1)}\), initial intervals \(m\le M,n\le N\), arbitrary complex coefficients, \((a,c)=1\), and the joint gcd condition,

\[
\left|\sum\alpha_m\beta_nS(am,n;c)\right|
\ll \|\alpha\|_2\|\beta\|_2c^{1-1/700+o(1)}.
\]

If \(|\alpha_m|\le1\), the printed second branch requires only \((n,c)=1\) and gives

\[
\ll \sqrt M\,\|\beta\|_2c^{1-1/276+o(1)}.
\]

Theorem 1.2 assumes a factorization \(c=dd'e\), \(d'\mid d\), \((d,e)=1\), and writes \(f\) for the maximal integer with \(f^2\mid cd\); for square-root-length initial ranges it gives

\[
\ll\|\alpha\|_2\|\beta\|_2c^{1+o(1)}
\left(\frac{f}{\min(c,d^2)}\right)^{1/6}.
\]

Corollary 1.4 averages moduli but places the absolute value **inside** that average.  For \(q=dd'e\), fixed coefficient sequences, positive intervals of lengths at most \(C^{1/2+o(1)}\), and polynomially bounded support,

\[
\sum_{C<c\le2C,\ q\mid c}
\left|\sum_{(m,n,q)=1}\alpha_m\beta_nS(m,n;c)\right|
\ll \|\alpha\|_2\|\beta\|_2\frac{C^{2+o(1)}}q
\left(\frac{f}{\min(C,d^2)+\min(q,d^2C/q)}\right)^{1/6}.
\]

Thus it destroys any project sign between moduli.  Corollary 1.6 is again a positive square over the exceptional Maaß spectrum at the cusp infinity for factorizable level and \(N\le\sqrt q\), not a full trace formula.

The earlier published exceptional-spectrum paper is A. Pascadi, *Large sieve inequalities for exceptional Maaß forms and applications*, [arXiv:2404.04239v3](https://arxiv.org/abs/2404.04239), Forum of Mathematics, Pi 14 (2026), e8, [journal DOI](https://doi.org/10.1017/fmp.2026.10025).  Its scope is the exceptional positive spectrum (and special sparse Fourier sequences), not arbitrary signed project coefficients.

#### Milićević--Qin--Wu

Djordje Milićević, Xinhua Qin and Xiaosheng Wu, *Bilinear forms with Kloosterman sums and moments of twisted L-functions*, [arXiv:2511.07550v1](https://arxiv.org/abs/2511.07550), use

\[
\mathrm{Kl}_2(a;q)=q^{-1/2}\sum_x^*e_q(ax+\bar x).
\]

Theorem 1.1 assumes \(M\le Nq^{1/4}\), \(M^{7/5}N<q^{3/2}\), \(MN\le q^{5/4}\), and \((c,q)=1\), and proves

\[
\left|\sum_{m\le M,n\le N}\alpha_m\beta_n\mathrm{Kl}_2(cmn;q)\right|
\ll q^\varepsilon\|\alpha\|_2\|\beta\|_2(MN)^{1/2}
\left(M^{-1/2}q^{1/6}+M^{-3/25}N^{-3/10}q^{1/5}+(MN)^{-3/16}q^{11/64}\right).
\]

Restoring the unnormalized Kloosterman sum multiplies the right side by \(q^{1/2}\).  At \(M=1,N=q\), the leading restored size is \(q^{7/6+o(1)}\|\beta\|_2\), so it gives no full-row `UNBAL` saving.  Theorem 1.2 is a family-averaged twisted second moment for fixed automorphic data, not a literal two-height/cardinal project identity.

#### Wright

M. Wright, [arXiv:2604.25177v2](https://arxiv.org/abs/2604.25177), defines

\[
B(M,N,A;R)=\sum_{a,m,n\atop(m,nR)=1}
\alpha_m\beta_n\nu_a e(\vartheta a\bar m/(nR)).
\]

Theorem 2.1, for \(M\ll N^2\), \(R\ll M^{A_0}\) (the source also uses \(A\) for a length), gives

\[
\begin{aligned}
B\ll{}&M^\varepsilon\|\alpha\|_2\|\beta\|_2\|\nu\|_2(AMN)^{1/2}R^{1/4}
\left(1+\frac{|\vartheta|A}{MN}\right)^{1/4}\\
&\times\left(N^{-1/8}+R^{1/8}N^{1/8}M^{-1/4}
+\frac{M^{1/10}}{R^{3/20}A^{1/20}N^{3/20}}
+\frac{N^{3/20}}{A^{3/20}M^{1/5}}+\frac{N^{3/8}}{M^{1/2}}\right).
\end{aligned}
\]

Corollary 2.2 additionally assumes divisor-bounded \(\alpha,\beta\) and a Siegel--Walfisz property, and sums \(|E|\) over moduli.  It does not allow the joint project Kloosterman row with \(\widehat\gamma_{g,n}\), and its absolute value is again inside the modulus sum.

#### New August-2026 Kloosterman/Kuznetsov records

1. A. Mohammadi, *Bilinear Kloosterman sums over small boxes and uniformity of a random walk*, [arXiv:2608.01203v1](https://arxiv.org/abs/2608.01203).  Theorem 1: for boxes \(B_1,B_2\subset\mathbb F_q\), \(|B_1||B_2|\ge q^{1/2+\varepsilon}\), and arbitrary weights \(|\alpha|,|\beta|\le1\),
   \[
   \max_{a\in\mathbb F_q,b\in\mathbb F_q^*}
   \left|\sum_{x\in B_1,y\in B_2}\alpha(x)\beta(y)
   \psi(axy+b x^{-1}y^{-1})\right|
   \ll_\varepsilon p^{-\delta}|B_1||B_2|.
   \]
   The kernel, finite-field box geometry, fixed modulus, and size hypothesis do not match \(\sum_h\widehat\gamma(h)S_{\rm proj}(N_0,h;n)\); setting one box to a singleton loses the size hypothesis and still leaves the wrong reciprocal dependence.
2. D. Milićević, C. Robinson and C. Shupe, *Sums of products of Kloosterman sums to prime power moduli*, [arXiv:2608.21346v1](https://arxiv.org/abs/2608.21346).  For an odd prime \(p\), \(q=p^n\), fixed \(k\), and a shift tuple \(\mathbf a\), Theorem 1.1 proves
   \[
   S(\mathbf a;q)\ll_k p^{\,n-(n-\Delta^*(\mathbf a)-1)/\lceil k/2\rceil+1},
   \]
   where \(S\) is the complete sum over \(x\bmod q\) of a product of normalized \(\mathrm{Kl}_2(x+a_i;q)\), and \(\Delta^*\) is the theorem's precise power-sum alignment invariant.  It also exhibits aligned configurations with full size \(\asymp q\).  No project aggregate has been transformed into this one-modulus complete product; project moduli vary, coefficients and hard supports are nonconstant, and the required tangent/defect signs are absent from the theorem's input.
3. Y. Shi, *Asymptotic Analysis and Phase Transition of the Bessel--Kuznetsov Transform with an Oscillatory Phase*, [arXiv:2608.13232v1](https://arxiv.org/abs/2608.13232), author manuscript linked to [journal DOI](https://doi.org/10.1080/10652469.2026.2700610).  Theorem 1.1 treats only \(\phi(x)=W(x)e(\alpha x)\), \(W\in C_c^\infty[X,2X]\).  For \(0<\alpha\le1/(2\pi)\), \(\check\phi(t)\ll_Nt^{-N}\); for \(\alpha>1/(2\pi)\), it is negligible outside
   \[
   \tfrac12X\sqrt{4\pi^2\alpha^2-1}\le t\le X\sqrt{4\pi^2\alpha^2-1},
   \]
   and at an interior unique stationary point
   \[
   \check\phi(t)=-\frac{\pi W(x_0)}{2t}
   e^{\,i2t\operatorname{arsinh}(\sqrt{4\pi^2\alpha^2-1})}(1+O(t^{-1})).
   \]
   This is a transform asymptotic, not a Kuznetsov identity, large sieve, or bound for the arithmetic side.  No source theorem turns the project actual symbol and hard endpoints into this fixed smooth linear phase.
4. S. Bhattacharjee, [arXiv:2608.18253v1](https://arxiv.org/abs/2608.18253), gives alternate expressions and structural properties for long-Weyl \(\mathrm{GL}_n\) Kloosterman sums; it is not a bilinear or spectral estimate at the project interface.
5. R. Cass, M. P. Gu and E. Zelingher, [arXiv:2608.24836v1](https://arxiv.org/abs/2608.24836), concerns Kloosterman sheaves and Bessel functions for finite reductive groups, not the classical varying-modulus sums here.

### 2.4 Exact `UNBAL` restored-power test

For the favorable \(M=1,a=N_0\) orientation, set \(c=n\), \(I=\{1\}\), \(J=\{1,\dots,n\}\), \(N=n\), \(\alpha_1=1\), and \(\beta_h=\widehat\gamma_{g,n}(h)\) with \(\beta_n=0\).  This orientation requires \((N_0,n)=1\).  Inversion of the summation variable gives

\[
S_{\rm proj}(N_0,h;n)=S_{\rm src}(N_0,h;n)=S_{\rm src}(h,N_0;n).
\]

That coprimality restriction is not a universal obstruction to Blomer--Pascadi Theorem 1.1.  By Kloosterman symmetry,

\[
S_{\rm proj}(N_0,h;n)=S_{\rm src}(h,N_0;n).
\]

Apply Theorem 1.1 with \(c=N=n\), \(a=1\), and \(I=J=\{1,\ldots,n\}\).  Put

\[
\alpha_h=
\begin{cases}
\widehat\gamma_{g,n}(h),&1\le h<n,\\
0,&h=n,
\end{cases}
\qquad
\beta_m=\mathbf 1_{m=r(N_0)},
\]

where \(r(N_0)\in\{1,\ldots,n\}\) represents \(N_0\bmod n\), with \(r(0)=n\).  The multiplier \(a=1\) is a unit, both intervals are the full initial interval, and the printed initial-interval clause removes the joint gcd condition.  Thus this is a legal fixed-modulus application for every center \(N_0\), after symmetry, a delta coefficient, and zero padding.  It gives

\[
n^{23/18+o(1)}\|\widehat\gamma_{g,n}\|_2,
\]

which is non-saving, is taken under one absolute value at a fixed modulus, and is not the required signed varying-modulus vector theorem.

For the favorable coprime-center orientation, the remaining Blomer--Pascadi substitutions give:

- Theorem 5.5: \(\mathcal H(1,n,n)\) has terms \(n^{-1/32},1,n^{2/15},n^{1/9},1\), hence the bound is
  \[
  n^{17/15+o(1)}\|\widehat\gamma_{g,n}\|_2.
  \]
- Theorem 5.7: its bracket is \(n^{-1/4}+1+n^{-1/4}\asymp1\), giving
  \[
  n^{1+o(1)}\|\widehat\gamma_{g,n}\|_2,
  \]
  with zero power saving.
- Chopping the full row into \(n^{1/2}\) translated square-root blocks and applying Theorem 1.1 by triangle/Cauchy gives \(n^{39/32+o(1)}\), not a theorem for the recombined signed row and not a saving.

Pascadi's 2025 Theorem 1.1 cannot be applied to the full \(h<n\) row because it requires initial square-root ranges; translating blocks is not covered by its initial-range statement, and the \(1/276\) branch deletes non-coprime \(h\).  A hypothetical triangle/Cauchy recombination would be \(n^{5/4-1/700+o(1)}\), again larger than the required row scale and not a printed theorem.

Independently of those bounds, the scalar projective route inflates by

\[
K^{1/2-o(1)}=X^{(1-\delta-a)/2-o(1)},
\]

and a long-block norm loses \(X^{a/2}\).  Each exceeds \(X^{\mu(a)}\) somewhere, and together they exceed it throughout \(1/4<a<1/2\).  Hence no scalar or blockwise positive estimate proves the signed varying-vector owner.

### 2.5 Determinant and shifted-divisor correlations

#### Grimmelt--Merikoski 2024

L. Grimmelt and J. Merikoski, *Twisted correlations of the divisor function via discrete averages of \(\mathrm{SL}_2(\mathbb R)\) Poincaré series*, [arXiv:2404.08502v2](https://arxiv.org/abs/2404.08502).  Theorem 10.1 assumes

- \(\alpha\in\mathcal A(q_1,q_2,\chi,\xi)\), a precise left-automorphic/determinant-twisted class;
- \(A,C,D,\delta,\eta>0\), \(AD>\delta\), \(Z=\max(A^{\pm1},C^{\pm1},D^{\pm1},\delta^{-1})\);
- \(H,K\ge1\), \(HK\le(AD)^{1+\eta}\);
- \(f\in C^7_\delta(A/\sqrt{HK},C/\sqrt{HK},D/\sqrt{HK})\);
- dyadic \(\beta_h,\gamma_k\) and the explicit positive autocorrelation hypothesis (10.2), quantified by \(\mathcal K_+\).

It evaluates the signed determinant sum \(ad-bc=hk\) as an explicit principal-character main term plus

\[
O\!\left(Z^{O(\eta)}\delta^{-O(1)}(AD)^{1/2}
\|\beta\xi\|_2\mathcal K_+^{1/2}
(\mathcal R_0+\min(\mathcal R_1,\mathcal R_2))\right),
\]

with the exact \(\mathcal R_i\) of Theorem 10.1.  The project determinant map after the 2-adic split is

\[
(a,b,c,d)=(d',d,m,m'),\qquad ad-bc=d'm'-dm=r.
\]

This algebraic map is exact.  The first failed hypothesis is analytic/arithmetic: the project actual selector is not proved to lie in \(\mathcal A(q_1,q_2,\chi,\xi)\), and its moving square-root phase and hard endpoints are not one \(C^7_\delta\) bump.  Smoothing the variable-shift phase would require roughly \(\delta^{-1}\gtrsim1+Jr/L\), reaching \(J\) at \(r\asymp L\) and \(JL\) at \(r\asymp L^2\); the theorem records only \(\delta^{-O(1)}\), which cannot be silently absorbed.

The continuation, *Weighted averages of \(\mathrm{SL}_2(\mathbb R)\) automorphic kernel Part I: non-oscillatory functions*, [arXiv:2505.00489v2](https://arxiv.org/abs/2505.00489), still labels itself Part I and leaves two nonnegative automorphic-kernel discrepancy forms in its main result.  Its applications restore left invariance and smoothness.  No indexed oscillatory Part II matching the project phase was found by the cutoff.

#### Bettin--Chandee

S. Bettin and V. Chandee, *Trilinear forms with Kloosterman fractions*, author manuscript [arXiv:1502.00769](https://arxiv.org/pdf/1502.00769), Advances in Mathematics 328 (2018), [journal DOI](https://doi.org/10.1016/j.aim.2018.01.026).  Corollary 1 handles a fixed determinant with independent coefficient sequences and two smooth one-variable weights.  At four comparable lengths \(L\), its fixed-shift error is \(L^{39/20+\varepsilon}\).  Taking absolute values and summing \(L\) or \(L^2\) shifts exceeds the respective `K17a` and `K26` targets.  More fundamentally, the project selector and phase are nonseparable and are not inputs to the corollary.

#### Lau

Y. K. Lau, *Smoothed shifted convolutions of generalised divisor functions*, [arXiv:2509.07556v2](https://arxiv.org/abs/2509.07556).  Theorem 1.1: for \(k\ge4\), \(w\in C_c^\infty[1/2,1]\), and a fixed nonzero shift \(|h|\ll x^{25/28-\eta}\),

\[
\sum_nw(n/x)d_k(n)d(n+h)
=xP_{k,h,w}(\log x)
+O_{k,w,\varepsilon}\bigl(x^{1-7\eta/128+\varepsilon}+x^{127/128+\varepsilon}\bigr).
\]

Theorem 5.2 is a fixed-\((h,k)\) specialization of the Grimmelt--Merikoski determinant theorem, with a periodic automorphic selector verified inside that application.  Neither theorem accepts the project residual coefficient, moving actual selector, or hard endpoints.

#### Blomer--Jana--Nelson

V. Blomer, S. Jana and P. Nelson, *Local integral transforms and global spectral decomposition*, [arXiv:2404.10692v2](https://arxiv.org/abs/2404.10692), GAFA 35 (2025), 1051--1107, [official journal page](https://link.springer.com/article/10.1007/s00039-025-00714-0).  Theorem 3 fixes cuspidal \(\mathrm{PGL}_2\) representations \(\pi_1,\pi_2\), a finite set \(S\), assumes \(\pi_{2,v}\) principal series for \(v\in S\), fixes \(0\ne b\), and takes \(h\in C_c^\infty(F_S^\times\times F_S^\times)\).  It gives the exact identity

\[
\sum_{n_1-n_2=b}W_{\pi_1}^{(S)}(n_1)\overline{W_{\pi_2}^{(S)}(n_2)}h(n_1,n_2)
=\int_{\widehat{[G]}_{\rm gen,S}^{\rm u}}W_\pi^{(S)}(b)c_\pi^{(S)}h^\vee(\pi_S,b_S)\,d\pi.
\]

The spectrum is the full unitary generic spectrum, not a ready-made upper bound.  The coefficients are fixed Whittaker/Hecke data, the shift and smooth test are fixed, and no theorem identifies the project actual residual coefficients with them.  Even a hypothetical per-shift bound of the familiar \(L^{2+\theta}\) scale would sum to \(L^{2+\theta}\) for `K17a` and \(L^{3+2\theta}\) for `K26`, missing the targets.

### 2.6 Square-root sums, exponent pairs, and decoupling

#### Tao--Trudgian--Yang exponent pairs

T. Tao, T. Trudgian and A. Yang, *New exponent pairs, zero density estimates, and zero additive energy estimates*, [arXiv:2501.16779v1](https://arxiv.org/abs/2501.16779).  The arXiv index still has only v1 (2025-01-28); the rendered manuscript prints a later internal date, 2026-08-24, but that is not a separately indexed arXiv version.

Their exponent-pair definition is a **coefficient-one interval** estimate: for a model phase \(F\), \(T\ge N\ge1\), and \(I\subset[N,2N]\),

\[
\sum_{n\in I}e(TF(n/N))
\ll (T/N)^{k+o(1)}N^{\ell+o(1)}.
\]

Theorem 20 includes the exact pairs

\[
\left(\frac{89}{1282},\frac{997}{1282}\right),\quad
\left(\frac{652397}{9713986},\frac{7599781}{9713986}\right),\quad
\left(\frac{10769}{351096},\frac{609317}{702192}\right),\quad
\left(\frac{89}{3478},\frac{15327}{17390}\right).
\]

For the project reciprocal phase \(e(hX/4d)\), \(d\asymp D\), \(h\asymp L\), the first pair gives

\[
B_L(D;X)\ll
X^{[89(1+\ell)+819\delta]/1282+\varepsilon}.
\]

This reaches \(X^{1/4}\) precisely when

\[
178\ell+1638\delta\le463.
\]

The unresolved `UNBAL` region is the strict complement.  Moreover, the exponent-pair definition has no arbitrary project selector coefficients; partial summation for a bounded-variation weight must pay its variation.

For the scalar square-root wave

\[
P_U=\sum_{\ell\ \mathrm{odd}}\chi_4(\ell)\ell^{-3/4}A_U(\ell)e(\sqrt{N\ell}),
\]

the Bourgain--Demeter pair \((13/84,55/84)\) gives the source-card bound

\[
|P_U|\ll\left(\frac{R^{780}}{M^{449}}\right)^{1/1592}X^\varepsilon,
\]

so the scalar target holds when \(M^{449}\gg R^{780}\).  This is the scalar \(D=d=L=1\) regime, not the growing generic sector or `M9`.

#### Xiao averaged square-root sums

J. Xiao, *On the moments of exponential sums with square roots*, [arXiv:2606.28986v1](https://arxiv.org/abs/2606.28986).  With

\[
S(h,n)=\sum_{n/2\le a\le n}e(h\sqrt a),
\]

Theorem 1.1 proves \(M_2(H,n)\ll_{\varepsilon,\delta}Hn^{1+\varepsilon}\) for \(H\ge n^{1/2+\delta}\); Theorem 1.2 proves \(M_4(H,n)\ll_{\varepsilon,\delta}Hn^{2+\varepsilon}\) for fixed \(0<\delta<1/6\) and \(n^{1/2+\delta}\le H\le n^{2/3}\).  These are averages over \(h\), not a pointwise signed theorem with project coefficients, real center, and hard support.

#### Robert--Sargos and modular-square-root variants

O. Robert and P. Sargos, *Three-dimensional exponential sums with monomials*, author manuscript [PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf), [journal DOI](https://doi.org/10.1515/CRELLE.2006.012), supplies bounded-coefficient monomial-sum bounds and an unsigned four-square-root spacing count.  Hölder/Cauchy removes the project \(\chi_4\), selector, and outer defect signs before reaching the frozen owners.

Shparlinski--Xiao, [arXiv:2601.10113](https://arxiv.org/abs/2601.10113), concerns fixed-prime Salié/modular-square-root kernels and averaged moments.  It has no exact map to the real square-root determinant phase.

#### Current decoupling/additive-energy records

X. Yang, [arXiv:2511.00841v1](https://arxiv.org/abs/2511.00841), Theorem 1.5: if \(R^{1/2}\) is an integer, \(\omega\ge0\) on \(B_R=[0,R]^2\), \(\omega(B_R)\le R\), and

\[
G(x,t)=\sum_{n\le R^{1/2}}a_ne(nx/R^{1/2}+n^2t/R),
\]

then

\[
\int_{B_R}|G|^2\omega
\lesssim_\varepsilon R^\varepsilon
\sup_{R\times R^{1/2}\text{ tube }T}\omega(T)^{1/2}\,R\|a\|_2^2.
\]

Theorem 1.6 gives an \(L^4\) restriction estimate for a quadratic Weyl sum on a set formed by one \(N^{-1}\times N^{-2}\) box per horizontal strip.  These are positive spatial norms for a quadratic phase.  They do not encode the project square-root phase, actual symbols, cardinal endpoints, or signed defect aggregate.

A. Cushman, C. Demeter and S. Wu, *Near optimal three-fold additive energy bound for points on convex curves*, [arXiv:2608.12316v3](https://arxiv.org/abs/2608.12316), Theorem 1.1: for every finite \(X\subset\mathbb R\) and strictly convex \(\gamma\),

\[
J_3(\gamma(X))\le C_\varepsilon|X|^{3+\varepsilon},
\]

where \(J_3\) counts exact six-tuples satisfying equality of two sums of three points.  Corollary 1.3 specializes to exact lattice points on a circle.  The project requires approximate one-phase square-root correlations with coefficients, moving scales, and hard supports; it has no proved reduction to an exact two-coordinate six-term equality.  Thus the theorem is a useful structural comparison, not a `BAL`, `K26`, or square-root-sum estimate.

Li--Yang Proposition 3.1 contains an arbitrary-coefficient small-cap cone norm, but the project source card permits only the repaired narrow final circle theorem.  Missing range input in the general decoupling chain prevents importing Proposition 3.1 as an independent black box.

### 2.7 Reciprocity and hybrid moments

#### Liyang Yang, GL(3)-type reciprocity manuscript

L. Yang, [arXiv:2512.03305v1](https://arxiv.org/abs/2512.03305).  Its main reciprocity identity, for \(|\Re s_i|<1/2\), transforms a \(\mathrm{GL}_3\times\mathrm{GL}_2\) cuspidal-plus-Eisenstein spectrum under

\[
(s_1,s_2)\mapsto s^\vee=\left(\frac{s_2-s_1}{2},\frac{3s_1+s_2}{2}\right),
\]

and retains singular, dual, degenerate, dagger-degenerate, generic, continuous, and explicit residue terms.  No test datum in the source realizes the project's literal product

\[
L(\alpha+it_1,\chi_4)\zeta(\alpha+it_2)G
\]

with two independent heights and the cardinal coefficient \(g(Q,R)\).

#### New Liyang Yang Fourier toric reciprocity

L. Yang, *Fourier Spectral Reciprocity and Canonical Hecke L-Functions*, [arXiv:2608.23886v1](https://arxiv.org/abs/2608.23886), submitted 2026-08-24.  Theorem A, for a quadratic extension \(E/F\), induced section \(h(\cdot,s)\), and \(|\Re s|<1/2\), states

\[
\sum_{\chi\in\widehat C_E,\ \chi|_{\mathbb A_F^\times}=\bar\omega}
\frac{Z(\chi;h(\cdot,s))}{L(1,\eta)}
=J_{\rm Const}(h)+J_{\rm Res}(h)+J_{\rm Dual}(h),
\]

where \(J_{\rm Const}=h(I_2,s)+h^\Diamond(I_2,s)\),
\(J_{\rm Res}=[h(w,s)+h^\Diamond(w,s)]\prod_{v\mid\infty}\Gamma_{F_v}(1)\), and

\[
J_{\rm Dual}=\frac{1}{2\pi\operatorname{Res}_{\lambda=1}\zeta_F(\lambda)}
\sum_{\xi\in\widehat C_F}\int_{\mathbb R}\widetilde\Psi(W,\xi|\cdot|^{it})\,dt.
\]

Theorem B is a first-moment asymptotic over unitary canonical Hecke characters, with two explicit main terms and error

\[
\mathcal E_\mu(s,k)\ll
D_{E/F}^{7/16+2\delta+\varepsilon}
(1+k+|s|)^{15d/16+2\delta d+\varepsilon}
N_F(\mathfrak f)^{11/16+\delta+\varepsilon}L(1,\eta).
\]

The identity has one free spectral parameter and a specific Hecke-character family; it preserves constant, residual, and continuous dual pieces.  There is no two-independent-height/cardinal project test section.

#### Kwan

K. Kwan, *A Motohashi-type formula for the fourth moment of individual Dirichlet L-functions and applications*, [arXiv:2310.09419v3](https://arxiv.org/abs/2310.09419), current 2026-03-16; Journal of the Institute of Mathematics of Jussieu 25(4) (2026), 2265--2312.  The formula relates a shifted cubic \(\mathrm{GL}_2\) moment to a shifted fourth \(\mathrm{GL}_1\) moment with one **shared** height \(t\), a smooth \(\eta\in C_c^\infty[T,2T]\), main terms, and a continuous component.  The project has independent \(t_1,t_2\), a product collar, and a cardinal selector; no exact test-function map is provided.

#### Tang short twisted zeta moment

Z. S. Tang, *Reciprocity for the Short Twisted Second Moment of the Riemann Zeta Function*, [arXiv:2608.14852v1](https://arxiv.org/abs/2608.14852).  Theorem 1 assumes distinct odd primes \(p,q\), \(T>1\), \(H=T^\delta\), \(1/2<\delta<1\), and proves

\[
\begin{aligned}
&\int_{\mathbb R}(p/q)^{it}|\zeta(1/2+it)|^2e^{-(t-T)^2/H^2}\,dt\\
&=\frac{2\pi}{\sqrt{pq}}\bigl(G'_{T,H}(1)-G_{T,H}(1)\log(pq)+2\gamma G_{T,H}(1)\bigr)\\
&\quad+\sum_{\chi\bmod p}^{*}\frac{\sqrt p}{i^\alpha(p-1)}\chi(q)
\int_{\mathbb R}G_{T,H}(1/2+it)(\pi/q)^{it}
\frac{\Gamma((1+2\alpha-2it)/4)}{\Gamma((1+2\alpha+2it)/4)}
|L(1/2+it,\chi)|^2\,dt\\
&\quad+O\!\left(\frac{T}{H}(pqT)^\varepsilon
\left((p/q)^{1/2}+(q/p)^{1/2}\right)\right),
\end{aligned}
\]

with parity parameter \(\alpha\).  Dominance of the main term uses \(H^2/\max(p,q)>T^{1+\varepsilon}\).  This is a Gaussian-smoothed one-height identity with prime twists and a primitive-character average; it does not realize two independent project heights, \(\chi_4\) on one factor, or the cardinal product collar.

#### Ji shifted Gaussian-Hecke second moment

X. Ji, *Shifted second moment of Gaussian Hecke L-functions \(L(s,\lambda^k)\)*, [arXiv:2608.17199v4](https://arxiv.org/abs/2608.17199), current 2026-08-24.  For \(\Phi\in C_c^\infty[1,2]\), define

\[
\mathcal S(u,v,K,\Phi)=\sum_{k\ge1}\Phi(k/K)
\Lambda_k^*(1/2+u+v)\Lambda_k^*(1/2+u-v).
\]

Theorem 1.1 assumes \(|\Re u|+|\Re v|\ll1/\log K\), \(|u|,|v|<\log K\), and \(|u|,|v|,|u+v|,|u-v|\ge(\log K)^{-2}\).  It gives four explicit functional-equation-swap main terms (the \(\pm2u,\pm2v\) terms printed in (1.2)) plus

\[
O_{\Phi,\varepsilon}(K^{1/2+\varepsilon}).
\]

The proof separates zero frequency, moving Eisenstein residues, continuous spectrum, and Maaß/cuspidal contributions.  Crucially, the manuscript explicitly restricts the theorem to the **untwisted** moment and leaves a fixed-ideal twisted analogue as Conjecture 9.1 because the twist changes the congruence weights and the incomplete-Poincaré spectral expansion.  The project would require a substantially more structured twist and two-height/cardinal coefficient, so the source itself identifies the first missing hypothesis.

#### Other hybrid results

- A. Pascadi, [arXiv:2511.08445v2](https://arxiv.org/abs/2511.08445), Theorem 1.5 averages over primitive characters modulo \(q\) for fixed level-one holomorphic newforms, even weights in a fixed congruence class, with main term and error \(q^{1-1/674+o(1)}\).  It is a family average, not the project product.
- Milićević--Qin--Wu Theorem 1.2 is likewise a twisted-family second moment with fixed automorphic data and saving \(q^{-1/216}\), not a two-height actual-symbol theorem.
- Z. Gao, C. Li and Z. Qi, *Hybrid Weyl Subconvexity over Imaginary Quadratic Fields*, [arXiv:2608.05934v1](https://arxiv.org/abs/2608.05934), Theorem 1.1: for an imaginary quadratic field of class number one, fixed cuspidal \(\pi\), and \(\chi_{it,m}(n)=|n|^{it}(n/|n|)^m\),
  \[
  L(1/2,\pi\times\chi_{it,m})\ll_{\pi,\varepsilon,F}(1+|t|+|m|)^{2/3+\varepsilon}.
  \]
  This is a pointwise bound for one fixed automorphic datum and one Hecke character, not a moment identity or project collar estimate.

### 2.8 Quantifier, smoothing, and absolute-value ledger

| Source/result | Pointwise / averaged / almost-all / smoothed | Absolute-value and coefficient placement | First project mismatch |
|---|---|---|---|
| Li--Yang Thm. 1.2 | unrestricted pointwise in \(X\) | no exceptional set; final error magnitude | repaired proof dependency; exponent still \(>1/4\) |
| Huxley | pointwise, older published theorem | error magnitude | weaker exponent after area normalization |
| Gao smooth-number circle | restricted and smoothed/arithmetic subset | weighted smooth-number count | not unrestricted |
| Blomer--Pascadi Thms. 1.1/5.5/5.7 | fixed modulus, arbitrary coefficients | one absolute value around each bilinear form | all-center Thm. 1.1 is legal but non-saving at \(n^{23/18}\); the sharper \(M=1,a=N_0\) orientation needs a unit center; no varying-modulus signed vector |
| Pascadi Cor. 1.4 | modulus average | **absolute value inside** modulus sum | destroys outer signs |
| Pascadi/BP exceptional large sieves | spectral average, positive | sum of coefficient squares over \(\lambda_j<1/4\) | incomplete spectrum and positive norm |
| Wright Cor. 2.2 | modulus average | **absolute value inside** modulus sum | destroys outer signs and needs special coefficients |
| Xiao square-root moments | average over \(h\) | positive moments | not fixed signed family |
| X. Yang decoupling | spatial average | positive \(L^2/L^4\) norm | wrong phase and no actual symbol |
| Cushman--Demeter--Wu | exact combinatorial count | unsigned equality count | not approximate weighted project correlation |
| GM / Lau / BJN | fixed-shift or dyadically averaged, smooth | theorem-specific signed sum, but smooth and structurally restricted | selector/phase/endpoints fail |
| Tang | Gaussian-smoothed one-height integral and character average | \(|\zeta|^2\), \(|L|^2\) inside moment | one height, prime twist family |
| Ji | smooth \(k\)-family average | product of completed \(L\)-values; untwisted only | project twist/cardinal test absent |
| L. Yang Fourier reciprocity | Hecke-character family sum plus continuous dual integral | exact identity with const/residual/dual terms | no two-height/cardinal test section |
| TTY | coefficient-one interval estimate | absolute value only after summing the scalar phase | arbitrary selector costs not included |

No almost-all statement in this ledger is promoted to a fixed-center theorem.  In particular, a theorem true for almost all characters, shifts, moduli, centers, or frequencies does not settle the one project center and one hard selector unless an explicit exceptional-set removal is proved.

### 2.9 Spectral-piece ledger

A full Kuznetsov/spectral application would have to account for all of the following, with the correct cusps and scaling matrices:

1. diagonal/main term;
2. holomorphic spectrum;
3. regular Maaß spectrum;
4. exceptional Maaß spectrum;
5. Eisenstein/continuous spectrum;
6. residual or degenerate terms created by contour shifts or reciprocity.

Blomer--Pascadi and Pascadi's highlighted large sieves control only a positive exceptional part.  Blomer--Jana--Nelson integrate over the full unitary generic spectrum but give an identity, not the project coefficient bound.  Ji explicitly separates zero frequency, Eisenstein residues/continuous spectrum, and Maaß/cuspidal spectrum in a different family.  Kwan, Tang, and both Liyang Yang reciprocity formulas retain main, continuous, residual, or degenerate pieces.  No audited source permits those pieces to be dropped in a project application.

## 3. Proof or derivation

### 3.1 Audit method

For each primary theorem, I performed the same ordered interface test:

1. normalize the source's large variable and its Kloosterman convention;
2. copy the printed quantifiers, ranges, coefficient class, gcd/unit conditions, endpoint type, and location of every absolute value;
3. write the most favorable literal project parameter substitution available;
4. restore all normalization powers, block counts, and modulus/shift sums;
5. stop at the first failed hypothesis rather than borrowing the theorem's saving exponent;
6. check whether the source controls the complete spectral package rather than one positive component;
7. compare the surviving size with the exact project target and with the Round-171--173 positive-capacity obstructions.

No numerical experiment was used.  All comparisons are algebraic substitutions into printed estimates.

### 3.2 Exponent normalization derivation

Li--Yang use the area variable \(X\), so their exponent needs no halving.  Huxley uses a radius/curvature parameter \(R\); setting \(X=R^2\) gives

\[
R^{131/208}=X^{131/416}.
\]

This prevents the common but invalid comparison of \(131/208\) against area-variable exponents.  The later smooth-number and omega papers change either the counted set or the direction of the inequality, so neither enters the unrestricted pointwise upper-exponent ledger.

### 3.3 `UNBAL` derivation

The favorable \(M=1,a=N_0\) identification with the Blomer--Pascadi convention follows by the inversion \(x\mapsto\bar x\):

\[
\sum_x^*e((N_0\bar x+hx)/n)
=\sum_x^*e((N_0x+h\bar x)/n).
\]

The substitution \((c,M,N)=(n,1,n)\) gives the favorable-orientation Theorems 5.5/5.7 powers in Section 2.4 and is unavailable when \((N_0,n)>1\).  This does not block every fixed-modulus application: symmetry gives \(S_{\rm proj}(N_0,h;n)=S_{\rm src}(h,N_0;n)\), and Blomer--Pascadi Theorem 1.1 is legal for every center with \(c=N=n\), \(a=1\), full initial intervals, \(\alpha_h=\widehat\gamma_{g,n}(h)\) zero-padded at \(h=n\), and a delta coefficient at the representative of \(N_0\).  Its restored size is nevertheless \(n^{23/18+o(1)}\|\widehat\gamma_{g,n}\|_2\), so it is non-saving.  All these estimates take a fixed-modulus absolute value.  Passing to square-root blocks also changes the interval hypotheses, uses absolute values between blocks, and loses the outer \(\chi_4(g)\chi_4(n)\) cancellation.  Therefore the first missing object is not a slightly sharper exponent or a coprimality repair but a **signed varying-modulus vector theorem** for the exact \(\widehat\gamma_{g,n}\) family.

### 3.4 `K17a/K26` determinant derivation

The algebraic determinant map \((d',d,m,m')\mapsto d'm'-dm=r\) is valid.  To import Grimmelt--Merikoski one must next prove that the actual selector is left automorphic in their exact sense, verify their positive autocorrelation hypothesis, and represent the moving square-root phase and hard endpoints by one admissible \(C^7_\delta\) function with all \(\delta^{-O(1)}\) losses priced.  None is established.  Bettin--Chandee and Lau instead require fixed shifts and separable/smooth coefficient classes.  Absolute summation of fixed-shift errors spends at least one shift factor for `K17a` and two for `K26`, exceeding the targets before any Round-172/173 cancellation is addressed.

Thus determinant syntax alone is not a theorem map.

### 3.5 `BAL` derivation

Round 171 proves that axes and singular strips are target-safe but leaves the double-far \(j=1\) family with the exact oscillation \((-1)^s\).  The endpoint-swap identity leaves a positive \(P_{++}\) component of \(L^4\) size, and mixed Abel summation produces a primitive ramp of height \(\gg L\), again giving \(L^4\) capacity against \(L^3\).

Every audited fixed-modulus large sieve or decoupling theorem takes a norm/absolute value before the project nonlocal sign has been exploited.  Consequently it sees the retained \(L^4\) capacity.  None supplies a literal two-defect actual-symbol parameter map that preserves \((-1)^s\) through all geometric, gcd, and endpoint faces.  The August finite-field-box and prime-power-product results have different kernels and fixed complete domains, so they do not alter this first failure.

### 3.6 `K26` Round-172/173 derivation

Round 172 shows that the zero ordinary-frequency sector is target-safe only after exact recombination; deleting the physical zero diagonal does not delete the fixed dual diagonal.  A coefficient-uniform Fejér/spectral norm has sharp \(L^4\) capacity, and the smooth fixed opening at \(\varphi=0\) returns the rank-one product collar.  Round 173's tangent chart gives

\[
r_s=dv+2s(m+v),\qquad r_{s+1}-r_s=2m',\qquad
\chi_4(d+2s)\chi_4(d)=(-1)^s,
\]

but the actual-symbol remainder is

\[
2(T_{26}+B_{\rm short})-\sum{\rm commutator},
\]

so estimating the commutator returns to `K26`; positive variation is still \(L^4\).

No determinant theorem accepts this actual-symbol/tangent family, and no positive Kloosterman or spectral norm can improve the \(L^4\) capacity without using the literal outer sign.  Milićević--Robinson--Shupe's aligned prime-power examples reinforce that complete Kloosterman products may have a full-size aligned sector, but they are not a project lower bound and do not create the missing cancellation theorem.

### 3.7 Full `t=1`, hard `TOP`, `M1/GAR`, and endpoint derivation

Tang and Kwan have a single common height; Ji averages a different CM family; Liyang Yang's reciprocity identities use specific automorphic sections and retain constant/residual/continuous packages.  None realizes the exact two-independent-height product, the cardinal \(g(Q,R)\), or the moving stationary collar.  Shi's transform theorem handles one smooth linear phase but supplies neither the arithmetic trace formula nor a signed product-collar estimate.  Therefore the full signed relative \(L/H\) gain is absent.

No source theorem proves either direct `M1` parent or a complete `GAR` replacement with the project endpoint conventions.  Even a hypothetical complete `GAR` theorem would replace only blockwise `M1`, not any hard `M2` owner.  Likewise, none of the sources carries the half-open shells, stars, floors, zero extensions, cardinal interpolation, and real center \(X=N_0+\xi\) uniformly with all derivative/boundary terms.  These packages cannot be reconstructed by saying a theorem is “smoothly localizable.”

### 3.8 Conclusion of the derivation

Every apparent source match either fails a literal hypothesis before a numerical saving can be applied or, in the all-center Blomer--Pascadi Theorem-1.1 map, is legally applicable but restores to the non-saving size \(n^{23/18+o(1)}\|\widehat\gamma\|_2\) under a fixed-modulus absolute value.  The remaining project gaps are signed structural interfaces, not gaps that follow merely from using an older exponent.  Hence no source closes a graph node, no source invalidates the Round-171--173 no-go diagnostics, and the pointwise exponent remains the repaired Li--Yang value.

## 4. First doubtful or unproved step

The first global unproved step is:

> Construct a literal theorem-level parameter map from one of the audited analytic tools to the project's actual signed coefficient family, before taking absolute values or positive norms, while retaining hard endpoints, real center, all gcd/nonunit cases, and every spectral/residual term.

More specifically:

1. **Li--Yang:** outside the repaired narrow import, the first doubtful step is the unrepaired general decoupling/range chain.  It must not be used to certify new project lemmas.
2. **full `t=1`/hard `TOP`:** no source identifies a two-independent-height/cardinal automorphic test or proves the signed relative \(L/H\) gain on the moving collar.
3. **`BAL`:** no source gives a nonlocal actual-symbol theorem that preserves \((-1)^s\) before the \(P_{++}\) projection or mixed-Abel ramp is bounded.
4. **`K17a/K26`:** no source proves the project selector is in the determinant theorem's automorphic class or prices the moving square-root phase and hard endpoints; Round 173's commutator step self-returns to `K26`.
5. **`UNBAL`:** no source gives a varying-modulus vector estimate for the full \(h<n\) row with arbitrary \((N_0,n)\), the exact \(\widehat\gamma_{g,n}\), outer \(\chi_4\)-signs, and saving \(X^{\mu(a)}\).
6. **direct `M1`/complete `GAR`:** neither exact source statement exists; `GAR` would not discharge the hard `M2` and endpoint obligations anyway.
7. **spectral routes:** the first unjustified step would be discarding the diagonal, holomorphic, regular Maaß, Eisenstein, residual, or degenerate pieces because an exceptional-spectrum positive large sieve is available.

These are proof gaps, not stylistic reservations.

## 5. Required control test and outcome

| Control | Test performed | Outcome |
|---|---|---|
| `primary_source_exact_hypotheses` | checked official arXiv/journal/author manuscripts; recorded versions, theorem numbers, ranges, gcd/unit conditions, coefficient class, and smoothness | **PASS as an audit**; project applicability fails at a literal hypothesis or, for the legal all-center Blomer--Pascadi map, at the restored non-saving power and signed varying-modulus interface |
| `current_unrestricted_pointwise_exponent` | searched current official arXiv records and author/journal status through 2026-08-27; normalized radius versus area | **PASS:** repaired Li--Yang \(\theta_*\) remains the dated audited pointwise exponent |
| `average_vs_pointwise_quantifier` | classified every near match as pointwise, fixed-family, averaged, almost-all, or smoothed | **PASS:** no averaged/almost-all/smoothed theorem was upgraded to pointwise |
| `coefficient_sign_and_absolute_value_placement` | tracked outer characters, defect signs, coefficient norms, and whether \(|\cdot|\) lies inside a modulus/shift sum | **PASS:** Pascadi Cor. 1.4 and Wright Cor. 2.2 are explicitly excluded because the absolute value is inside the modulus average |
| `spectral_main_continuous_holomorphic_Maass_exceptional_terms` | compared the full spectral ledger with exceptional-only and reciprocity sources | **PASS:** no spectral piece is silently omitted |
| `hard_endpoint_cardinal_and_real_centre` | required half-open shells, floors/stars, zero extension, cardinal \(g(Q,R)\), and \(X=N_0+\xi\) to survive | **FAIL applicability:** no source carries this package |
| `Round171_BAL_scope` | tested whether a theorem preserves the literal double-far sign and bypasses \(P_{++}\)/ramp capacity | **FAIL applicability:** no source bypasses the Round-171 obstruction |
| `Round172_transform_scope` | required exact common-frequency recombination and fixed-dual-diagonal bookkeeping | **FAIL applicability:** positive norms remain \(L^4\); no exact transform supplied |
| `Round173_self_return_scope` | checked whether a source estimates the actual-symbol remainder rather than only the commutator | **FAIL applicability:** the tangent route self-returns to `K26` |
| `full_t1_vs_K17a_vs_K26` | treated the three estimates as distinct statements | **PASS:** no implication between them is asserted without proof |
| `M1_vs_GAR_scope` | checked route ownership | **PASS:** complete `GAR` is not misreported as all blockwise/direct `M1` or any `M2` estimate |
| `restored_power_accounting` | restored normalized Kloosterman factors, block counts, and fixed-shift sums | **PASS:** the explicit powers in Sections 2.4--2.6, including the legal all-center \(n^{23/18}\) bound, show no hidden saving |
| `new_2026_08_currency_refresh` | screened the August math.NT submissions returned by the official arXiv API, then checked the current cutoff-date versions of plausible matches in full primary records | **PASS:** new reciprocity, moment, Kloosterman, Bessel, and convex-energy papers do not match |
| `no_status_or_exponent_overpromotion` | separated theorem publication status, project repaired-import status, and graph status | **PASS:** no preprint is called published; no candidate report is called accepted mathematics; no exponent is replaced |

Overall control outcome: the source audit is complete enough to certify a **dated no-match**.  It does not certify any unresolved project theorem.

## 6. Dependencies and exact artifacts used

### 6.1 Exact local artifacts read

Only the following selected local context files were used:

1. `protocol.md`;
2. `state/active_campaign.yml`;
3. `strategy/round174_full_proof_strategy_current_literature_review.md`;
4. `rounds/codex-managed/full-proof-round167-169-strategy-literature-review/reports/current_primary_literature_reassessment.md`;
5. `rounds/codex-managed/m9-m2-balanced-critical-j1-two-defect-commutator-gate/synthesis.md`;
6. `rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/synthesis.md`;
7. `rounds/codex-managed/m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate/synthesis.md`;
8. `sources/li_yang_2023.md`;
9. `sources/huxley_2003.md`;
10. `sources/bourgain_watt.md`;
11. `sources/tao_trudgian_yang_2025.md`;
12. `sources/xiao_2026.md`.

The frozen project interfaces in this report come from those artifacts.  I did not edit or independently reinterpret the authoritative claim graph.

### 6.2 Primary-source citation ledger

| Topic | Primary citation and exact URL | Version/status audited |
|---|---|---|
| circle exponent | Li--Yang, [arXiv:2308.14859](https://arxiv.org/abs/2308.14859) | v2, preprint |
| older published circle bound | Huxley, [PLMS journal page](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/S0024611503014485) | published 2003 |
| withdrawn dependency | Bourgain--Watt, [arXiv:1709.04340](https://arxiv.org/abs/1709.04340) | v2 withdrawn |
| smooth-number variant | Gao, [arXiv:2604.23918](https://arxiv.org/abs/2604.23918) | v1/current at cutoff |
| Fibonacci equivalence | [arXiv:2607.20960](https://arxiv.org/abs/2607.20960) | v1/current |
| omega result | Mahatab, [arXiv:2504.17032](https://arxiv.org/abs/2504.17032) | current record |
| exponent pairs | Tao--Trudgian--Yang, [arXiv:2501.16779](https://arxiv.org/abs/2501.16779) | arXiv index v1; internal manuscript date noted separately |
| square-root moments | Xiao, [arXiv:2606.28986](https://arxiv.org/abs/2606.28986) | v1 |
| square-root spacing | Robert--Sargos, [author PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf), [DOI](https://doi.org/10.1515/CRELLE.2006.012) | author manuscript / published paper |
| modular square roots | Shparlinski--Xiao, [arXiv:2601.10113](https://arxiv.org/abs/2601.10113) | current record |
| decoupling | X. Yang, [arXiv:2511.00841](https://arxiv.org/abs/2511.00841) | v1 |
| convex energy | Cushman--Demeter--Wu, [arXiv:2608.12316](https://arxiv.org/abs/2608.12316) | v3, 2026-08-24 |
| bilinear Kloosterman | Blomer--Pascadi, [arXiv:2607.24311](https://arxiv.org/abs/2607.24311) | v1 |
| Kloosterman/exceptional spectrum | Pascadi, [arXiv:2511.08445](https://arxiv.org/abs/2511.08445) | v2, 2026-06-21 |
| published exceptional large sieve | Pascadi, [arXiv:2404.04239](https://arxiv.org/abs/2404.04239), [journal DOI](https://doi.org/10.1017/fmp.2026.10025) | v3 / published 2026 |
| product-kernel bilinear sum | Milićević--Qin--Wu, [arXiv:2511.07550](https://arxiv.org/abs/2511.07550) | v1 |
| trilinear Kloosterman fractions | Wright, [arXiv:2604.25177](https://arxiv.org/abs/2604.25177) | v2 |
| finite-field boxes | Mohammadi, [arXiv:2608.01203](https://arxiv.org/abs/2608.01203) | v1 |
| prime-power Kloosterman products | Milićević--Robinson--Shupe, [arXiv:2608.21346](https://arxiv.org/abs/2608.21346) | v1 |
| oscillatory Bessel transform | Shi, [arXiv:2608.13232](https://arxiv.org/abs/2608.13232), [journal DOI](https://doi.org/10.1080/10652469.2026.2700610) | arXiv v1 / author manuscript |
| long-Weyl Kloosterman structure | Bhattacharjee, [arXiv:2608.18253](https://arxiv.org/abs/2608.18253) | v1 |
| finite-group Kloosterman sheaves | Cass--Gu--Zelingher, [arXiv:2608.24836](https://arxiv.org/abs/2608.24836) | v1 |
| automorphic determinant | Grimmelt--Merikoski, [arXiv:2404.08502](https://arxiv.org/abs/2404.08502) | v2 |
| non-oscillatory kernel Part I | Grimmelt--Merikoski, [arXiv:2505.00489](https://arxiv.org/abs/2505.00489) | v2 |
| Kloosterman fractions | Bettin--Chandee, [arXiv PDF](https://arxiv.org/pdf/1502.00769), [journal DOI](https://doi.org/10.1016/j.aim.2018.01.026) | published 2018 |
| generalized shifted divisor | Lau, [arXiv:2509.07556](https://arxiv.org/abs/2509.07556) | v2 |
| spectral shifted convolution | Blomer--Jana--Nelson, [arXiv:2404.10692](https://arxiv.org/abs/2404.10692), [official GAFA page](https://link.springer.com/article/10.1007/s00039-025-00714-0) | v2 / published 2025 |
| Motohashi reciprocity | Kwan, [arXiv:2310.09419](https://arxiv.org/abs/2310.09419) | v3, 2026-03-16 / published 2026 |
| GL(3)-type reciprocity | L. Yang, [arXiv:2512.03305](https://arxiv.org/abs/2512.03305) | v1 |
| Fourier toric reciprocity | L. Yang, [arXiv:2608.23886](https://arxiv.org/abs/2608.23886) | v1, 2026-08-24 |
| short twisted zeta reciprocity | Tang, [arXiv:2608.14852](https://arxiv.org/abs/2608.14852) | v1 |
| Gaussian-Hecke shifted moment | Ji, [arXiv:2608.17199](https://arxiv.org/abs/2608.17199) | v4, 2026-08-24 |
| imaginary-quadratic hybrid subconvexity | Gao--Li--Qi, [arXiv:2608.05934](https://arxiv.org/abs/2608.05934) | v1 |

### 6.3 Search reproducibility and limits

The currency check used the official arXiv API and arXiv abstract/HTML pages, with targeted searches for Gauss circle, lattice-point error, Kloosterman/Kuznetsov/large sieve, shifted convolution/divisor, determinant, spectral reciprocity, hybrid moments, decoupling, and square-root/exponential sums.  The August-2026 `math.NT` submissions returned through 2026-08-27 were title/abstract screened; plausible matches and their current versions were then checked at theorem level.  Official journal pages and author-hosted PDFs were preferred for published or older sources.

This method can certify the dated indexed primary record and the named official/author sources.  It cannot certify that no unindexed private draft exists.  The conclusion is therefore intentionally phrased as a dated primary-source no-match, not an absolute statement about all mathematical manuscripts.

## 7. Recommended state effect

**Recommendation: no change.**

1. Retain the repaired Li--Yang pointwise exponent \(\theta_*\) exactly as the current external preprint dependency; do not promote it to a published theorem or import unrepaired general propositions.
2. Retain all frozen `hard-TOP/t=1`, `K17a`, `K26`, `BAL`, `UNBAL`, direct `M1`, complete `GAR`, endpoint, `M9`, and bridge owners as unresolved.
3. Retain the Round-171 `BAL` obstruction, Round-172 transform/positive-capacity obstruction, and Round-173 tangent self-return as valid scope controls; the current sources do not bypass them.
4. Record the August-2026 papers only as literature evidence and possible method leads.  They do not warrant a State Patch, proof-draft change, validation-matrix change, status promotion, or exponent replacement.
5. Do not infer a full proof from any combination of averaged, smoothed, exceptional-spectrum, fixed-modulus, fixed-shift, or one-height results without a new exact signed parameter map and full endpoint/spectral accounting.

Recommended report disposition under the seven-part contract: **retain as a rigorous no-go/source-audit result; no graph change**.
