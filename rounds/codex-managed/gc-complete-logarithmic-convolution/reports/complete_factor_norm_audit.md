# Round 225: complete factor, norm and range audit

## 1. Result

**complete_logarithmic_convolution_no_new_bound.** The complete logarithmic identity and both finite Vaughan branches are verified with literal cutoffs. The exact contraction
\[
 f*(\mu\psi)=\bar a_\psi,\qquad
 \bar a_1=\chi_4,\quad \bar a_{\chi_4}=1
\]
is used before norms; its truncated version leaves an actual complementary Möbius/divisor vector, not a freely cancellable error.

All terms, factor ranges, the singleton and the full Schwartz tail are accounted for below. Legal unweighted exponent-pair estimates give an independently proved complete complex ceiling \(T^{13/56+\varepsilon}\) through the fully contracted boundary choice of cutoffs. The inherited classical real envelope gives \(T^{1/6+\varepsilon}\); the strongest complete real bound remains
\[
 T^{\beta+\varepsilon},\qquad
 \beta=2(3292+25\sqrt{1717})/13762-\tfrac12.
\]
None improves.

The generic Type-II norm calculation has an interesting but insufficient local optimum. At \(N=T^{2/3}\), its formal best split gives \(T^{47/378+\varepsilon}\), which is below \(\beta\). It is not a complete gain: actual cutoffs must pay all short terms and all other factor lengths. Even granting the optimal split freely at every scale, its envelope combined with the classical high-scale estimate peaks at \(T^{81/614+\varepsilon}\), which is worse than \(\beta\). This is a scoped upper-certificate comparison, not an actual signed lower bound or an all-method no-go.

The first missing estimate is one bound for the entire actual real eight-term recombination in Section 4, stronger than the inherited complete exponent. No fragment replaces it. This report is an independent NONBLIND audit with disclosed prior history. No current sibling or blind packet was read, no experiment was run, and no new primary-source audit was needed.

## 2. Exact objects, cutoffs and finite identities

Let \(\chi=\chi_4\), \(f=1*\chi=r_2/4\), and let \(\Psi\) be the prescribed real even Schwartz transform of the fixed nonnegative radial mollifier. It may change sign. For every real \(T\ge2\) and \(R\in[cT,CT]\),
\[
 B_T(R)=4\sum_{n\ge1}f(n)n^{-3/4}\Psi(\sqrt{n/T})
             \cos(2\pi R\sqrt n-3\pi/4).
 \tag{1}
\]
Define
\[
 F(n)=\frac{n^{-3/4}\Psi(\sqrt{n/T})e(R\sqrt n)}{\log n}
 \quad(n\ge2),\qquad F(1)=0.
 \tag{2}
\]
The original \(n=1\) term, denoted \(B_1\), is retained separately and is \(O(1)\).

For \(\psi=1,\chi\), put
\[
 a_\psi=\psi,\quad g_\psi=\mu\psi,\quad
 b_\psi=\Lambda\psi,\quad c_\psi=\psi\log.
\]
All truncations are literal: \(g_{\le U}(d)=g(d){\bf1}_{d\le U}\), and similarly for real \(U,V\ge1\); complements use strict \(>\). Dirichlet convolution and complete multiplicativity, including \(\chi(2)=0\), give
\[
 g_\psi*a_\psi=\delta_1,\qquad
 c_\psi=a_\psi*b_\psi.
\]
Since logarithmic multiplication is a derivation for convolution,
\[
 f\log=f*\Lambda+f*(\chi\Lambda)=f*b,\qquad
 b(n)=(1+\chi(n))\Lambda(n).
 \tag{3}
\]
There is no division by \(\log1\). At every prime power,
\[
 b(2^k)=\log2,\quad
 b(p^k)=2\log p\ (p\equiv1\bmod4),\quad
 b(p^k)=
 \begin{cases}0& p\equiv3\bmod4,\ k\text{ odd},\\
 2\log p& p\equiv3\bmod4,\ k\text{ even}.
 \end{cases}
 \tag{4}
\]
Thus inert even powers and the prime two are not discarded.

Split \(g_\psi*c_\psi\) at \(U\), then split its \(b_\psi\) factor at \(V\). The exact Vaughan identity is
\[
 b_\psi=b_{\psi,\le V}
 +g_{\psi,\le U}*c_\psi
 -g_{\psi,\le U}*a_\psi*b_{\psi,\le V}
 +g_{\psi,>U}*a_\psi*b_{\psi,>V}.
 \tag{5}
\]
Indeed \(g_{>U}*a=\delta_1-g_{\le U}*a\). Equality cases are already assigned by \(\le U,\le V\); there are no endpoint errors.

After convolution by \(f\), write the four terms as \(Q_{\psi,0},Q_{\psi,1},-Q_{\psi,2},Q_{\psi,3}\), respectively. Both branches occur, and the complete identity is
\[
 B_T(R)=B_1+4\Re\left\{e(-3/8)
 \sum_{\psi=1,\chi}\sum_{n\ge2}
 [Q_{\psi,0}(n)+Q_{\psi,1}(n)-Q_{\psi,2}(n)+Q_{\psi,3}(n)]
 F(n)\right\}.
 \tag{6}
\]
The common nonlinear phase is \(R\sqrt n\), or \(R\sqrt{\text{product}}\) after expansion.

## 3. Actual contraction, all norms and complete estimates

### 3.1 Exact complementary vectors before Cauchy

Define
\[
 \alpha_{\psi,\le U}=f*g_{\psi,\le U},\qquad
 \alpha_{\psi,>U}=f*g_{\psi,>U},\qquad
 \beta_{\psi,>V}=a_\psi*b_{\psi,>V}.
\]
The full arithmetic cancellations are
\[
 f*g_1=\chi,\qquad f*g_\chi=1,
\]
so
\[
 \alpha_{\psi,>U}=\bar a_\psi-\alpha_{\psi,\le U},\qquad
 \beta_{\psi,>V}(t)=\psi(t)
 \left(\log t-\sum_{\substack{k\mid t\\k\le V}}\Lambda(k)\right).
 \tag{7}
\]
In particular \(\alpha_{>U}(s)=0\) for \(s\le U\), while
\(\alpha_{\le U}(s)=\bar a_\psi(s)\) there; \(\beta_{>V}(t)=0\) for \(t\le V\).
No bound below assumes the complementary vector is unstructured before this identity is checked.

The long term is exactly
\[
 Q_{\psi,3}=\alpha_{\psi,>U}*\beta_{\psi,>V}.
 \tag{8}
\]
Also
\[
 Q_{\psi,1}-Q_{\psi,2}
 =\alpha_{\psi,\le U}*\beta_{\psi,>V}.
\]
Their sum is \(\bar a_\psi*a_\psi*b_{\psi,>V}=f*b_{\psi,>V}\).
Adding \(Q_{\psi,0}\) returns \(f*b_\psi\) exactly. This complete contraction checks signs and shows why deleting the long complementary vector is invalid. It is not a new estimate.

For a dyadic argument \(s\asymp S\), the actual sequence bounds used are
\[
 \begin{array}{c|c|c}
 \text{sequence}&\ell^1&\ell^2\\ \hline
 f& O(S^{1+\varepsilon})&O(S^{1/2+\varepsilon})\\
 \mu\psi\text{ with any literal cutoff}&O(S)&O(\sqrt S)\\
 \Lambda\psi,\ \psi\log\text{ with cutoffs}
       &O(S\log(2S))&O(\sqrt S\log(2S))\\
 \alpha_{\psi,\le U},\alpha_{\psi,>U}
       &O(S^{1+\varepsilon})&O(S^{1/2+\varepsilon})\\
 \beta_{\psi,>V}&O(S\log(2S))&O(\sqrt S\log(2S)).
 \end{array}
 \tag{9}
\]
They follow from \(|f|\le d_2\),
\(|\alpha_{\le U}|,|\alpha_{>U}|\le d_3\), and
\(|\beta_{>V}(t)|\le\log t\). Constants are independent of \(U,V\).
The bounds for \(f\) and \(\alpha\) are divisor bounds with epsilon/logarithmic losses; no fixed linear mean-square constant for \(f\) is assumed. There is no prime-density input.

The identities (7) retain actual Möbius and conductor-four signs. Using (9) loses their cancellation. Expanding short vectors later to expose a free variable is also a stated loss of cancellation, not a claim that the actual vector is arbitrary.

### 3.2 Singleton, dyadic weights and the entire tail

Choose a smooth dyadic partition of \(n\ge2\). On a shell \(n\asymp N\), the radial weight in (2), including the shell cutoff, has normalized sup and BV
\[
 \ll_A \frac{N^{-3/4}}{\log(2N)}
 (1+N/T)^{-A}.
 \tag{10}
\]
The same bound holds after fixing all but one positive product variable; a sharp product cutoff creates only the corresponding proper interval endpoint. Derivatives of the fixed Schwartz function give (10), including the transition \(N\asymp T\). Possible signs of \(\Psi\) are preserved until a stated modulus is taken.

Take \(Z=T^{3/2}\). Each of the eight absolute convolution coefficient majorants is at most a fixed divisor function times \(\log n\); for example the four-factor short term is bounded by \(d_4(n)\log n\), and the five-factor terms by \(d_5(n)\log n\). Thus (2) and arbitrary fixed Schwartz order \(L\) give, uniformly in all cutoffs,
\[
 \sum_{n>Z}\frac{d_5(n)\log n}{\log n}
 n^{-3/4}|\Psi(\sqrt{n/T})|
 \ll_{\eta,L}
 T^{L/2}Z^{1/4+\eta-L/2}
 =T^{3/8+3\eta/2-L/4}.
 \tag{11}
\]
Choose \(L\) sufficiently large for any required negative power. This pays each tail separately and licenses every rearrangement. No fixed-\(T\) Schwartz assertion is used as an unpriced uniform estimate.

Only \(O(\log T)\) shells remain. Cutoffs \(U_N,V_N\) may vary by shell because (5) holds coefficientwise for each choice before shell summation. Smooth overlaps sum back to one; this creates no transition residue. All finite partial shells, mixed factor sizes and singleton \(B_1\) remain.

### 3.3 Legal unweighted Type-I estimate

Use the already accepted global Bourgain exponent pair
\[
 (\kappa,\lambda)=(13/84,55/84),
\]
only on a genuinely unweighted interval after other factors have been fixed. This is not a new primary import.

If the free variable has ambient dyadic length \(M\) and the product has size \(N\le Z\), its phase is \(R\sqrt{vm}\), \(vM\asymp N\). The phase parameter is \(\mathcal T=R\sqrt N\), and
\(\mathcal T/M\gg T/\sqrt N\gg T^{1/4}\).
The source length convention is therefore satisfied for large \(T\).
The normalized square-root derivative pattern is uniform. For a conductor-four variable, split into its finitely many residue classes, retaining only the nonzero odd character classes when appropriate. With \(m=4r+a\), \(a\in\{0,1,2,3\}\), the phase is \(R\sqrt{v(4r+a)}=R\sqrt{4v}\sqrt{r+\alpha}\), \(\alpha=a/4\). On an ambient interval of length \(L\asymp M/4\), normalize \(r=Lt\); the phase parameter is \(\mathcal T'=R\sqrt{4vL}\asymp R\sqrt N\), and the normalized phase is \(\sqrt{t+\alpha/L}\). Its derivative of order \(j\) is \(\prod_{i=0}^{j-1}(1/2-i)(t+\alpha/L)^{1/2-j}\). On the fixed positive ambient interval these have the uniform, nonvanishing square-root derivative pattern, for every required order and every \(\alpha\in[0,1)\). This is the affine-translated model in the accepted standard derivative class. Also \(L\le\mathcal T'\) follows from \(\mathcal T'/L\gg T/\sqrt N\gg T^{1/4}\). Bounded ambient intervals are paid trivially. Product and ordering masks leave proper subintervals of this same ambient interval, not permission to replace its length by a shorter cell. Logarithms and (10) enter by Abel summation afterwards. For the remaining bounded range \(2\le T\le T_0(c,C)\), the fixed Schwartz/divisor absolute bound is uniform and is absorbed into the constant. No character is treated as an arbitrary weight in the exponent-pair theorem.

The resulting unweighted bound is
\[
 \sum_{m\in I}e(R\sqrt{vm})
 \ll_\varepsilon T^\varepsilon
 T^\kappa N^{\kappa/2}M^{\lambda-\kappa}
 =T^{\kappa+\varepsilon}N^{\kappa/2}\sqrt M.
 \tag{12}
\]
Neither Möbius, \(f\), nor an arbitrary prime weight is inserted inside this estimate.

Here is a full set of elementary Type-I prices. Write
\(u=\min(U,2N)\), \(v=\min(V,2N)\), and suppress the common
\(T^\varepsilon(1+N/T)^{-A}\). Each line may be capped by \(N^{1/4}\).
\[
 \begin{array}{c|c|c}
 \text{term}&\text{actual free factors used}&\text{normalized price}\\ \hline
 Q_{\psi,0}=f*b_{\psi,\le V}
  & f=1*\chi,\ k\le V&
 T^\kappa N^{\kappa/2}v^{1/4}\\
 Q_{\psi,1}=f*g_{\psi,\le U}*c_\psi
  & 1,\chi,\psi\log;\ d\le U&
 T^\kappa N^{\kappa/2+1/12}u^{1/6}\\
 Q_{\psi,2}=f*g_{\psi,\le U}*a_\psi*b_{\psi,\le V}
  &1,\chi,\psi;\ d\le U,\ k\le V&
 T^\kappa N^{\kappa/2+1/12}(uv)^{1/6}.
 \end{array}
 \tag{13}
\]
Empty short-prime terms are zero, not the displayed positive overestimate. To verify the powers, on a fixed short product \(a\), the longest of \(r\) free variables has \(M\gg(N/a)^{1/r}\). The number and divisor multiplicity of the remaining variables is at most \(N/(aM)\) up to logarithms. Equation (12), times \(N^{-3/4}\), gives
\[
 T^\kappa N^{\kappa/2+1/4-1/(2r)}
 a^{-1+1/(2r)}.
\]
Use \(r=2,a=k\) for the first line and \(r=3,a=d\) or \(dk\) for the other lines; summing the literal short coefficients with \(|\mu|\le1,\Lambda(k)\le\log k\) proves (13). A fixed ordering of the free variables handles ties once.

There is a useful complete boundary contraction. If \(U\ge2N\), then on this shell \(\alpha_{\le U}=\bar a_\psi\) and \(Q_{\psi,3}=0\). The first and third terms cancel exactly, leaving
\[
 \bar a_\psi*c_\psi.
 \tag{14}
\]
This has two free periodic variables, one logarithmic weight. Its price is
\(\min(N^{1/4},T^\kappa N^{\kappa/2})\), up to the factors already stated. Summing (14) over every shell and using the full Schwartz decay proves the independent complex bound
\[
 \left|\sum_{n\ge1}f(n)n^{-3/4}\Psi(\sqrt{n/T})e(R\sqrt n)\right|
 \ll_\varepsilon T^{3\kappa/2+\varepsilon}
 =T^{13/56+\varepsilon}.
 \tag{15}
\]
The singleton is \(O(1)\). This estimate is proved here from the accepted unweighted kernel; it is not inherited from a real-wave estimate. It is too weak to advance the complete real benchmark.

If \(V\ge2N\), the long-\(\Lambda\) vector vanishes on the shell and the other terms contract to \(f*b_\psi\). If \(UV\ge2N\), (8) is empty. These boundary cases are included rather than excluded from parameter optimization.

### 3.4 Complete Type-II norm bound and its factor range

On a nonempty shell of (8), let \(s\in(S,2S]\cap(U,\infty)\), \(t\in(K,2K]\cap(V,\infty)\), with \(SK\asymp N\). The first truncated dyadic shell is retained even when \(S\le U<2S\) or \(K\le V<2K\). Keep the exact \(\alpha_{\psi,>U}(s)\) and \(\beta_{\psi,>V}(t)\). Cauchy in \(s\), followed by expansion in \(t,t'\), places the arithmetic vector \(\alpha\) only in its actual norm (9). For \(t\ne t'\),
\[
 |R(\sqrt t-\sqrt{t'})|\asymp T|t-t'|/\sqrt K.
\]
Since \(N\le T^{3/2}\), this exceeds a fixed multiple of \(\sqrt S\) for large \(T\). The high-parameter unweighted square-root estimate therefore gives on every proper intersection interval
\[
 \left|\sum_s e(R\sqrt s(\sqrt t-\sqrt{t'}))\right|
 \ll_\varepsilon T^{\kappa+\varepsilon}
 |t-t'|^\kappa K^{-\kappa/2}S^{97/168}.
 \tag{16}
\]
All parameters are polynomial in \(T\), so source epsilon losses remain \(T^\varepsilon\). The kernel's ambient length is \(S\). The weight product from two copies of (10) is inserted by one-dimensional Abel summation on the intersection of their product intervals; no separability of a curved product mask is assumed.

Using \(|\alpha(s)|\ll S^\varepsilon\), \(|\beta(t)|\le\log(2K)\) and (9), the diagonal and off-diagonal sums give
\[
 |\mathcal T_{S,K}|
 \ll_\varepsilon T^\varepsilon(1+N/T)^{-A}
 \left\{(S/K)^{1/4}
       +T^{13/168}S^{13/336}K^{97/336}\right\}.
 \tag{17}
\]
For example the unnormalized off-diagonal square is at most
\(T^\kappa S^{265/168}K^{349/168}\) up to epsilon factors. Its square root and the \(N^{-3/4}\) normalization give (17). The swapped orientation is also valid, with the same norm audit, and either may be capped by \(N^{1/4}\). The elementary second-derivative alternative gives
\[
 (S/K)^{1/4}+T^{1/4}S^{-1/8}K^{3/8}.
 \tag{18}
\]
These bounds retain all legal factor rectangles and both branches. Cauchy and off-diagonal moduli have lost actual Möbius/character correlations; no arbitrary-vector example is asserted to be an arithmetic counterexample.

### 3.5 Complete optimization, including the apparently favorable local split

Write \(N=T^\nu\), \(K=T^k\), \(S=N/K\). The two exponents in (17) are
\[
 \gamma_1=\nu/4-k/2,\qquad
 \gamma_2=13/168+13\nu/336+k/4.
 \tag{19}
\]
Their formal optimum, when \(k\ge0\), is
\[
 k_*=(71\nu-26)/252,\qquad
 \gamma_*=(55\nu+26)/504.
 \tag{20}
\]
At \(\nu=2/3\), this gives \(k_*=16/189\) and
\(\gamma_*=47/378<1/8<\beta\).
This local numerical margin is real for the named bound, but not a complete result.

At this scale, the unswapped certificate beats \(T^\beta\) only if
\[
 1/3-2\beta<k<4\beta-26/63.
 \tag{21}
\]
Balanced factors lie outside that thin interval. If both cutoffs are below \(\sqrt N\), balanced Type-II rectangles remain. To force the short factor throughout (21), one cutoff must exceed \(\sqrt N\); for example requiring \(s>U\) to be long demands, to power accuracy,
\[
 V\gtrsim T^{1/3-2\beta},\qquad
 U\gtrsim T^{\,2/3-(4\beta-26/63)}.
\]
The swapped case interchanges the roles. This does not remove the short-prime or grouped short-Möbius terms in (5).

In particular, whenever \(V\ge2\), \(Q_{1,0}\) contains the actual prime-two component \(f(n/2)\log2\); its partner in the \(\chi\) branch at two is zero. At \(N=T^{2/3}\), the first Type-I certificate in (13), even for fixed \(k=2\), chooses the \(T^{1/6}\) trivial ceiling rather than the larger \(T^{13/63}\) exponent-pair price. Its incidencewise absolute mass is of order \(N^{1/4}/\log N\): \(\Psi(\sqrt{n/T})\to1\) uniformly there and the elementary lattice-area count gives \(\sum_{m\asymp N/2}f(m)\asymp N\). This is a control of that absolute closure, not a lower bound for the oscillatory prime-two component. If \(V<2\), the short term vanishes, but the long vector permits bounded \(t\), whose diagonal price is again \(N^{1/4}\). A cutoff emptying all such terms returns a contracted boundary expression such as (14). Nothing here proves those signed sectors are large; it records what the tested norm estimates still cost.

There is also a complete-scale failure even before these feasibility problems. Optimistically grant the formal split (20) at every scale and ignore all Type-I difficulties. Combine this hypothetical Type-II envelope with the inherited classical real block envelope
\[
 \min(N^{1/4},T^{1/2}N^{-1/2}).
 \tag{22}
\]
For \(\nu\ge26/71\), the increasing exponent \((55\nu+26)/504\) meets \((1-\nu)/2\) at
\[
 \nu=226/307,\qquad \gamma=81/614.
 \tag{23}
\]
Below \(26/71\), the trivial \(\nu/4\) envelope suffices; beyond the intersection the classical term decreases. Thus this optimistic complete menu still peaks at \(81/614\). It exceeds the complete benchmark, since
\[
 \beta<27/208<81/614.
\]
The second-derivative alternative (18) has best possible first off-diagonal exponent \(1/4-\nu/8\), already larger at (23), and does not lower this conclusion. The swapped (17) is included by allowing the shorter factor to play either role. Equations (20)--(23) are costs of named bounds under an optimistic split, not an actual inequality attaining that exponent for every Vaughan term.

For the actual complete wave, the verified separate-factor estimates bound every term, and (14)--(15) give a complete complex fallback. The inherited real envelope (22), summed over all scales with (10)--(11), gives \(T^{1/6+\varepsilon}\). The still stronger accepted real bound is \(T^{\beta+\varepsilon}\). No real-only bound is assigned to a complex wave or an arbitrary factor mask. Consequently the strongest complete conclusion of this audit is unchanged \(\beta\), not \(47/378\), \(81/614\), \(1/6\), or \(13/56\).

## 4. First doubtful or unproved step

Finite algebra, norms, interval estimates and full tail restoration above leave no unbounded term hidden as a local survivor. What is missing is a new inequality for the complete actual recombination:
\[
 \left|B_1+4\Re\left\{e(-3/8)
 \sum_{\psi=1,\chi}\sum_{n\ge2}
 [Q_{\psi,0}+Q_{\psi,1}-Q_{\psi,2}+Q_{\psi,3}](n)F(n)
 \right\}\right|
 \ll_\varepsilon T^{\gamma+\varepsilon}
 \tag{24}
\]
uniformly for all prescribed real radii, with some \(\gamma<\beta\), ultimately \(\gamma=0\). All literal cutoff transitions, prime powers and dyadic/tail terms occur in (24).

The required extra information must survive the actual \(\alpha_{>U}\) contraction, the \(\psi\)-branches and the nonlinear product phase. Pointwise bounds on a favorable factor rectangle, arithmetic vectors replaced by independent arbitrary arrays, or recombination back to \(f\log\) do not establish (24). No external theorem with missing coefficient or range hypotheses is substituted.

## 5. Required controls and physical outcome

| Control | Outcome |
|---|---|
| Actual complete wave | Fixed \(\Psi\), every real \(R\asymp T\), both cosine signs and all \(n\) retained. |
| Logarithmic identity | Finite derivation (3), prime-power check (4), and both Vaughan branches (5) verified. |
| Literal cutoffs | Real \(U,V\), inclusive short/strict long conventions, every boundary case and empty product range included. |
| Prime two/inert powers | Exactly as (4); no prime-only or squarefree replacement. |
| Singleton | Original \(n=1\) retained as \(B_1=O(1)\); \(F(1)=0\). |
| Actual arithmetic norms | Exact contractions precede the divisor norm estimates; no fixed linear mean-square class is assumed. |
| Type-I legality | Only a genuinely free periodic variable is reduced to finitely many unweighted intervals, with logs/BV afterwards. |
| Type-II legality | Exact complementary vectors, diagonal, all differences, ambient interval and curved-mask intersections retained. |
| Parameter optimization | Local \(47/378\) margin checked, complete cutoff feasibility restored, and optimistic all-scale \(81/614>\beta\) obstruction priced. |
| Infinite tail | Every decomposed coefficient is absolutely dominated in (11), with a fixed sufficient Schwartz order. |
| Real/complex scope | Complex \(13/56\) is independently derived; inherited \(\beta\) is used only for the real complete wave. |
| Actual versus generic | No actual signed lower bound is claimed; the prime-two absolute control and displayed ceilings have explicit certificate scope. |
| Source scope | Only the already accepted Bourgain interface is reused; no new audit or source grant. |
| Full goal | Sharp reconstruction and all independent owners remain unchanged absent (24). |

The accepted bridge is
\[
 P(R^2)=\frac{\sqrt R}{\pi}B_T(R)+O_\varepsilon(T^{1/2+\varepsilon}).
\]
A complete real exponent \(\gamma\ge0\) would yield discrepancy exponent \(1/4+\gamma/2\). The current \(\gamma=\beta\) restores exactly \(\theta_{\rm LY}\). The optimistic certificate exponent \(81/614\) would give \(97/307>\theta_{\rm LY}\), even if it were a complete theorem. Target \(\gamma=0\) would suffice for the full quarter theorem. No M1/M2/GAR, complete moment, endpoint or graph owner is independently discharged here.

## 6. Dependencies and provenance

Campaign gc-complete-logarithmic-convolution, round 225, role complete_factor_norm_audit. This agent has prior round history, including authorship of the 223 geometric report and 224 actual-profile report and attack review; it is not a history-free blind role. No current sibling report or blind statement was read. Only this assigned report is written.

| Artifact | SHA-256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/active_campaign.yml | 96ee2e0899a9b7e9d75aa276b7c098f0fbf1748850e94b5c6941733f856344fe |
| strategy/round225_complete_circle_logarithmic_convolution.md | 64be6a3fb32b2f33deea69cef87b846ec06732e002ffd2f5156f21f7ea8c878b |
| Current briefs/complete_factor_norm_audit.md | cd37ca8b79825294618700ea40562ad5ae52af88fcf7a4d2659731f409ac8082 |
| Current briefs/conductor_complete_circle_wave.md | 6adcf15bf5850f080aefd63c00d83d3482f6c244f5244c340b4206c47c46e0ef |
| strategy/gauss_circle_strategy_checkpoint_round223_2026-09-28.md | a0c75c5e2ef4ea45df4e388e3497d5be5133d6d49c7d7a2d71c166f11dd9dd33 |
| rounds/codex-managed/m9-m1-complete-gar-prime-amplification/synthesis.md | d5a94b25e876714c8e17602a497812afef3b42724a75dd4cc1501583d12fe98f |
| rounds/codex-managed/gc-complete-signed-convolution-attack/synthesis.md | 6ea983ef7066a7dc1a7833bbf4a99889e79c75eef9c42190421a4248c104aa5a |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| sources/bourgain_2017_exponent_pair.md | a2b13364b738457889546d0a52c027358d7eb450bebd4272a612d70f5e917361 |
| rounds/codex-managed/gc-full-goal-signed-source-review/synthesis.md | 3f97b688827680d7c733116ebc6bd0107b5ec1af4d2df5258fc0ce1cb0b5ae78 |

The accepted source is Jean Bourgain, *Decoupling, exponential sums and the Riemann zeta function*, global Theorem 6/Section 5, arXiv:1408.5794v2, as already audited in the permitted source card and accepted graph. This report performs no new primary audit. The graph's five Li--Yang application repairs remain unchanged.

The conductor independently highlighted the exact full Möbius contractions and the formal all-scale balance; both were rederived here. All other algebra and norm accounting is independently checked from the supplied actual interface. Zero mathematical experiments and no new literature search were used.

## 7. Recommended state effect

**No change to complete analytic bounds or exponents.** Retain the exact finite contractions, legal norm bounds and full parameter/tail ledger as candidate evidence pending review. Reject crediting the favorable \(N=T^{2/3}\) split as a complete gain, applying an unweighted exponent pair directly to actual arithmetic vectors, dropping a Vaughan branch or prime-power term, or inferring a complex bound from the inherited real supremum.

The complete missing inequality is (24). The bounded attempt supplies no validated \(\gamma<\beta\), and no counterexample to such an estimate. Stop this one decomposition audit without creating further local survivor tasks or beginning a successor.
