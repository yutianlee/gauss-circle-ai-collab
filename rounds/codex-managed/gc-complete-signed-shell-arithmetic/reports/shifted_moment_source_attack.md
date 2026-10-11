# Round 206: shifted moments and actual representation coefficients

Campaign: `gc-complete-signed-shell-arithmetic`. Task:
`shifted_moment_source_attack`. Role: source/application analyst, selected
context, not blind. Date: 2026-09-26. Starting graph SHA-256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Candidate evidence only. Effort: 100 percent analytical/source inspection;
no numerical experiments. Exactly three substantive primary interfaces
were inspected. No source card or shared state was edited.

## 1. Result

**Scoped no gain.** A genuine actual-r2 shifted-pair theorem can be
transferred to the variable-width odd filter, with its arithmetic main
term, sharp-weight error and full shift aggregate priced. For some fixed
source exponent lambda>0, reduced if necessary to lambda<=1/2, the result is

\[
 \int w(x/X)|C_N(x)|^2dx
 \ll_\epsilon X^{1+\epsilon}H+
              X^{1-\lambda+\epsilon}H^2,
 \qquad H=2\sqrt X/\sqrt N.                         \tag{1}
\]

Here C_N is the exact centered additive filter defined below, including
its variable width. Its completely restored shell consequence is

\[
 \int_I|S_N(R)|^{12}dR
 \ll_\epsilon W_N^{10}T^\epsilon
       \bigl(TN^{-1/2}+T^{2-2\lambda}N^{-1}\bigr),       \tag{2}
\]

where
\(W_N\ll_\epsilon T^\epsilon
\min(N^{1/4},T^\beta,T^{1/2}N^{-1/2})\).
Summing every middle block costs only logarithms. This source route gives
the full exponent

\[
 E_{\rm pair}=\max(1+8\beta,\ 2-2\lambda+6\beta),       \tag{3}
\]

which is worse than the existing 10beta. No numerical value for the
source's unspecified lambda is assumed.

The two other interfaces fail before an applicable higher moment arises:
Hughes--Rudnick's actual-r2 sixth-moment smoothing range is disjoint from
the entire middle band; Tanigawa--Zhai's theorem concerns divisor
increments, fourth moments, and widths larger than every project width.
These are scoped application failures, not impossibility statements for
the actual signed moment.

The proposed uniform sixth-moment input is more than sufficient:
\(\int|C_N|^6\ll X^{1+\epsilon}H^3\), if proved, would yield the middle
twelfth moment \(O(T^{1+\epsilon})\) by the elementary block supremum.
None of the inspected sources supplies that input.

## 2. Exact hypotheses and primary interfaces

Use the fixed functions Psi, v, and L from the reviewed Round205
interface. Let X=T^2, let x range in a fixed compact positive multiple of
X, and put

\[
 K(u)=\int_0^\infty t^{-1}\Psi(\sqrt{N/T}\,t)v(t^2)
                   \sin(2\pi ut)\,dt,
 \qquad h(x)=2\sqrt x/\sqrt N,
\]
\[
 C_N(x)=\sum_{m\ge1}(r_2(m)-\pi)
                       K((x-m)/h(x)),
 \qquad T^{52/125}<N=2^j<T^{99/125}.                   \tag{4}
\]

All Schwartz seminorms of K are uniform in this range. Its Fourier
support lies in [-2,-1] union [1,2]; K is real and odd. Constants may
depend on the fixed functions, epsilon and fixed window. The test w is
smooth, compactly supported in a fixed positive interval, nonnegative
and at least one on [1/2,3], after enlargement if necessary. Thus its
moment dominates the requested real-radius interval. Widths obey
\(H\asymp h(x)\), with
\(X^{151/500}\ll H\ll X^{99/250}\).

**Interface A.** Hulse--Kuan--Lowry-Duda--Walker,
[*The Laplace Transform of the Second Moment in the Gauss Circle
Problem*, arXiv:1705.04771v3, Theorem 7.1, equations (7.1)--(7.3),
pp.26--27](https://arxiv.org/pdf/1705.04771v3).
For a positive integer k, its sharp formula is
\[
 \sum_{n\le Y}r_2(n)r_2(n+k)
 =c_kY+O_\lambda((Y+k)^{1-\lambda}+k)
 \quad\hbox{for some }\lambda>0,                     \tag{5}
\]
\[
 c_k={8(-1)^k\over k}\sum_{d\mid k}(-1)^d d.
\]
The smoother exponential-weight version has error
\(O_\epsilon(Y^{1/2+\epsilon}e^{k/Y}k^\Theta)\),
\(\Theta\le7/64\). The report uses (5), not an unproved transfer of
that stronger smoothed error to arbitrary weights. The remark proposing
lambda=1/8 is not a quantified theorem used here. Metadata identifies
v3 as 1 April 2020 and publication as *Algebra & Number Theory* 15 (2021),
1--27. Representation multiplicities match exactly.

**Interface B.** Hughes--Rudnick,
[*On the distribution of lattice points in thin annuli*,
arXiv:math/0304129v3, Proposition 5, p.8; Theorem 1, p.2]
(https://arxiv.org/pdf/math/0304129v3).
For their smoothed annulus, the m-th normalized moment has Gaussian
asymptotics when
\[
 M=O(T^{2(1-\delta)/(2^{m-1}-1)}),\quad
 L\longrightarrow\infty,\quad L/\sqrt M\longrightarrow0.
                                                               \tag{6}
\]
Here annulus thickness is 1/L, M controls boundary smoothing, and
delta>0 is fixed. Their sharp-annulus distribution theorem requires
\(L=T^{o(1)}\). It is a weak convergence statement; the passage to the
sharp count uses a mean-square approximation. The source really uses
r2, not the indicator of sums of two squares. Its current version is
16 September 2003.

**Interface C.** Tanigawa--Zhai,
[*On the fourth power moment of Delta(x) and E(x) in short intervals*,
arXiv:0805.1525, Theorem 1 and Corollary 1, pp.4--5]
(https://arxiv.org/pdf/0805.1525).
Its object is the fourth moment of the divisor discrepancy increment
Delta(x+U)-Delta(x), with \(Y^{3/7}\ll U\ll Y^{1/2}\), averaging
length J<=Y and \(J^8U^{21}\gg Y^{17}\). The corollary, with epsilon
margins, gives order \(JU^2\log^6(Y/U^2)\). The paper's separate zeta
mean-square error theorem concerns E, also not the circle coefficient.
No circle sixth-moment statement is imported.

Primary records and these theorem locations were checked on 2026-09-26.
The bounded selection is not an exhaustive literature claim.

## 3. Proof and complete application ledger

### Filter, curvature, centering, and tails

The identity \(L(z)=K(\sqrt N z)\) is exact. On the local shell write
\(u=(x-m)/h(x)\), \(x=R^2\). Then
\[
 \sqrt N(R-\sqrt m)=u+O(u^2/(T\sqrt N)),\qquad
 m^{-1/4}=x^{-1/4}
       +O(T^{-1/2}|u|/(T\sqrt N)).
\]
The uniform Schwartz bounds, the mean-value theorem and
\(r_2(m)\ll_\epsilon m^\epsilon\) show, after summing the local
shell of effective width h(x), that
\[
 S_N(R)=x^{-1/4}C_N(x)
       +O_\epsilon(T^{-1/2+\epsilon}N^{-1})
       +O_A(T^{-A}).                                  \tag{7}
\]
For this derivation one can first restrict |m-x|<=x/2. On its complement
both the curved and linear kernels have arguments of polynomial size
in T and N; increasing their fixed decay order makes the sum over all
m there arbitrarily small. This includes m far above X. In the local
part summing \((1+|u|)^{-A}\) costs O(1+h), with h>1, so the displayed
error is uniform even at lattice radii.

The mean subtraction in (7) is justified without a mean-density
heuristic. For h>2, Poisson summation and the Fourier support of K give
\(\sum_{m\in\mathbb Z}K((x-m)/h)=0\) exactly. Restoring the omitted
m<=0 has arbitrarily small size because x/h is a positive power of T.
Thus subtracting pi in (4) has the stated negligible cost. K(0)=0 also
holds at exact centers. No integer-endpoint deletion occurs.

### Actual local densities, including every divisor

Here is an elementary consequence of the explicit c_k in (5), derived
in this report:
\[
 \sum_{1\le k\le Z}c_k=\pi^2 Z+O(\log(2Z)).           \tag{8}
\]
Indeed put q=k/d in the divisor formula. The parity factor is negative
precisely when q is even and k/q is odd. Therefore
\[
 c_k=8\sum_{q\mid k}{1\over q}
       -16\sum_{\substack{q\mid k\\2\mid q, k/q\ {\rm odd}}}
                 {1\over q}.
\]
Sum over k<=Z. The first sum has main term 8 zeta(2) Z; the second
has main term
\(16(Z/2)\sum_{2\mid q}q^{-2}=2\zeta(2)Z\).
The floor and odd-count errors cost O(sum_(q<=Z) 1/q)=O(log(2Z));
extending the convergent main sums costs O(1). Since
6 zeta(2)=pi^2, (8) follows. Every even and odd divisor is present.

Set a_m=r2(m)-pi. Centering (5), using the accepted summatory circle
bound and then reducing lambda to at most 1/2, gives, uniformly for
t comparable to X and 1<=k<=C X,
\[
 \sum_{m\le t}a_m a_{m+k}
 =(c_k-\pi^2)t+O_\epsilon(X^{1-\lambda+\epsilon}+kX^\epsilon).
                                                               \tag{9}
\]
For example the shifted single sum is
\(\sum_{m\le t}r_2(m+k)=\pi t+O(X^{\theta+\epsilon}+1)\)
in this range, including its lower endpoint. As theta<1/2, it is
absorbed in (9). This use of the existing circle bound does not assume
the desired new exponent.

### Exact variable-width second moment

Open the square of (4) and define, for k>=1,
\[
 W_k(u)=\int w(x/X)K((x-u)/h(x))
                         K((x-u-k)/h(x))\,dx.
\]
After negligible remote tails, u is comparable to X. For every fixed A,
\[
 \|W_k\|_\infty+\int|W_k'(u)|du
 \ll_A H(1+k/H)^{-A}.                                \tag{10}
\]
This is a slowly varying weight, despite each individual kernel's
narrow support scale. To verify the derivative, substitute x=u+y.
Differentiation now hits w at cost 1/X and h(u+y) at relative cost
1/X. The factors y/h and (y-k)/h so produced are absorbed by Schwartz
decay. Integrating y costs H, and the u-range costs X in the derivative
integral. A fixed smooth cutoff restricting u to a comparable X-range
has the same bound and changes the result only by arbitrarily small
tails. This proves (10) for the actual h(x), without freezing it.

Partial summation of (9) against W_k gives an error at most
\[
 X^\epsilon H(1+k/H)^{-A}(X^{1-\lambda}+k).
\]
Summing all k>=1 costs
\(O_\epsilon(X^{1-\lambda+\epsilon}H^2+X^\epsilon H^3)\).
For k beyond a fixed multiple of X use Schwartz decay and the divisor
bound directly; choosing A large makes this negligible. Thus no
unestimated large-shift complement is created.

For the main term define the even Schwartz autocorrelation
\(A_K(z)=\int_{\mathbb R}K(t)K(t-z)dt\). Interchanging absolutely
convergent integrals gives the off-diagonal main contribution exactly,
up to the already paid tails, as
\[
 2\int w(x/X)h(x)
             \sum_{k\ge1}(c_k-\pi^2)A_K(k/h(x))\,dx.
\]
By (8) and partial summation its absolute value is
O(X H log(2X)). This uses the arithmetic average of c_k together with
cancellation in the signed autocorrelation. Bounding the shift sum by
sum_k c_k |A_K(k/h)|, or by analogous absolute pair weights, would
generally cost XH^2. Merely replacing c_k-pi^2 by c_k while retaining
the signed autocorrelation does not create that loss: since integral K=0
and h>2, Poisson summation gives sum_(k in Z) A_K(k/h)=0, so the
difference in the off-diagonal expression is only
-pi^2 A_K(0) integral w(x/X)h(x)dx=O(XH).
The k=0 diagonal, including repeated indices, is bounded by
O_epsilon(X^(1+epsilon)H) directly from a_m^2<<m^epsilon. Since
H^2<X throughout the band, H^3 is absorbed by XH. This proves (1).

### Restoring the supremum, Jacobian and all blocks

The coefficient sum gives \(|H_N|\ll N^{1/4+\epsilon}\), and the
reviewed physical-shell estimate gives
\(|H_N|\ll T^{1/2+\epsilon}N^{-1/2}\).
The third supremum \(|H_N|\ll T^{\beta+\epsilon}\) follows by a
legitimate smooth multiplier transfer: the even multiplier
v(xi^2/N) has a convolution kernel sqrt(N) q(sqrt(N)u) with uniformly
bounded L1 norm. Applying it to the complete H recovers H_N. On a
fixed enlarged positive radius interval use the accepted supremum of
H. Outside that interval the convolution kernel's rapid decay, together
with the global coefficient bound H<<T^(1/4+epsilon), gives an
arbitrarily small tail. Formula (7) and the reviewed shell reconstruction
transfer all three bounds to S_N with harmless errors. Thus W_N above
is justified blockwise; it is not inferred from a bound for a sum by
discarding its other terms.

Using dR=dx/(2sqrt(x)), (7), and (1),
\[
 \int_I|S_N|^2dR
 \ll_\epsilon T^\epsilon
          (TN^{-1/2}+T^{2-2\lambda}N^{-1}).             \tag{11}
\]
The twelfth moment of the uniform error in (7) is negligible. Multiplying
(11) by W_N^10 proves (2). Put N=T^nu and
\(\omega(\nu)=\min(\nu/4,\beta,(1-\nu)/2)\).
The two powers in (2) are
\[
 1-\nu/2+10\omega(\nu),\qquad
 2-2\lambda-\nu+10\omega(\nu).
\]
Both reach their maximum over the complete middle interval at nu=4beta,
which lies strictly between 52/125 and 99/125; also 4beta<1-2beta.
The maxima are exactly those in (3). Minkowski over O(log T) blocks
adds only a fixed logarithmic factor. The already estimated outer
portion, all reconstruction errors, and the infinite original tail
are unchanged. Taking the better of (3) and the accepted complete
bound retains precisely 10beta, since 1+8beta>10beta.

Even if an improved pair theorem removed the second term of (1)
entirely, this variance-plus-supremum application would still give
1+8beta. Thus the failure is not merely the unspecified sharp exponent.

### Sixth moments, fourth moments, and the two failed imports

For comparison suppose, as a new and unproved input, that for every
middle N one had \(\int w|C_N|^{2j}\ll X^{1+\epsilon}H^j\).
The restored shell moment would be
\[
 \int_I|S_N|^{2j}dR\ll T^{1+\epsilon}N^{-j/2}.         \tag{12}
\]
Using W_N^(12-2j) and maximizing over the entire band gives:

| Hypothetical centered input | Complete twelfth-moment exponent |
|---|---|
| Second moment XH | 1+8beta |
| Fourth moment XH^2 | 1+4beta |
| Sixth moment XH^3 | 1 |

For the sixth line it suffices to use W_N<=N^(1/4+epsilon), so the
powers N^(-3/2) and W_N^6 cancel. This is a conditional implication,
not proof of the sixth-moment input. Both lower-order lines exceed
the existing 10beta. They illustrate the precise loss from raising
the moment by the available supremum; no Gaussian inference is made.

In interface B the relevant radial thickness is rho comparable to
N^(-1/2), so L is comparable to sqrt(N). A sixth moment sets m=6 in
(6), requiring M<<T^(2(1-delta)/31), whereas resolving that annulus
requires M/N to tend to infinity. But N>T^(52/125), and
52/125>2/31. These requirements cannot hold for any middle scale.
The sharp theorem's subpolynomial L condition also fails throughout
the band. Even an admissible weak Gaussian limit would not itself
bound sixth moments of rare large values. Consequently no replacement
of the actual kernel by that sharp annulus is licensed.

In interface C identify its summation variable scale Y with X and
U with the proposed arithmetic width H. Even at the largest allowed
width, H<<X^(99/250), while 99/250<3/7. Thus the entire project range
is outside its theorem before addressing the different d(n) coefficients,
mean term, fourth-versus-sixth moment, smooth filter, or variable width.
The inequality r2<=4d does not compare centered signed moments: it
would restore the unwanted mean. No bound for (4) follows from this
source. The fourth line of (12) was explicitly hypothetical, not an
import from interface C.

## 4. First doubtful or unproved step

The first new arithmetic step needed for the proposed strong criterion
is a complete sixth moment of C_N of order XH^3 (or a weaker but
quantitatively sufficient replacement). Expanding that moment creates
six-factor shifted correlations, including all repeated shifts. Formula
(5) controls only pairs. Pairing the six factors and replacing their
joint average by products of pair averages is unproved and is not
implicit in spectral continuation of a two-factor Dirichlet series.

For the pair route, (1)--(3) are candidate deductions from the exact
source formula and the existing project bounds. Their transfer is
spelled out to permit an independent seam audit, not promoted as an
accepted theorem here. The stronger exponential-weight estimate in
interface A is not silently substituted for (5); doing so would need
an additional quantitative arbitrary-weight spectral argument.

Hughes--Rudnick fails its numerical range hypotheses; Tanigawa--Zhai
fails both range and object hypotheses. These first failures already
prevent their proposed applications, so none of their omitted-filter
or exceptional-value costs is assigned a fictional zero.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| complete_middle_range | All N between the two fixed dividing powers are included; maximization uses the interior scale N=T^(4beta). No smaller remainder replaces the target. |
| actual_r2_character | Interface A and (8) retain representation multiplicities and all parity factors. The divisor-only theorem is rejected as a transfer. |
| all_divisors_and_shifts | Formula (8) sums every divisor; (9)--(11) sum every shift. k=0 is kept separately. No six-factor diagonal is discarded. |
| curvature_and_mean_error | Formula (7) pays curvature and fourth-root amplitude variation. Poisson summation proves the lattice mean cancellation. |
| infinite_tails | Original and curved transform tails are covered by the reviewed interface; linear-filter, remote-index, large-shift and convolution tails are explicitly paid by fixed Schwartz decay. |
| real_endpoints | x and R remain real. Exact lattice radii satisfy K(0)=0. Sharp sums and their partial summations include endpoint errors. |
| signed_not_positive | c_k-pi^2 is kept before aggregation; positivity alone would cost XH^2. r2<=4d is not used on a centered signed moment. |
| full_moment_power_ledger | (2)--(3) include the Jacobian, actual block supremum, all middle blocks and outer errors. Best complete bound remains T^(10beta+epsilon). |
| source_hypotheses | Three exact primary interfaces checked. Lambda stays unspecified; the smoothed source error is not used for a different weight. |
| no_gaussian_inference | Neither second/fourth moments nor weak distribution convergence is asserted to imply a sixth moment. The table explicitly states hypothetical inputs. |
| full_proof_scope | No pointwise improvement, M1/M2 closure, or quarter theorem. Even the requested T^(29/25) milestone has not been proved. |

These are analytical controls. There were no numerical experiments,
random trials, source-card promotions, or votes on mathematical validity.

## 6. Exact dependencies and artifacts used

Local context, and no sibling report, was read:

- `protocol.md`.
- `state/proof_obligations.yml`: authoritative target and accepted
  `GC-complete-square-root-large-values-moment-bound`, with its repaired
  external pointwise dependency and unchanged open target.
- `state/active_campaign.yml`.
- `strategy/round206_complete_signed_shell_arithmetic_attack.md`.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/briefs/shifted_moment_source_attack.md`.
- `rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_middle_band_strategy.md`.
- `rounds/codex-managed/gc-full-frontier-moment-strategy-review/reviews/independent_middle_band_review.md`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.
- `rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_arithmetic_source_gate.md`.
- `strategy/gauss_circle_strategy_checkpoint_round205_2026-09-26.md`.

The three primary PDF links and theorem locations appear in Section 2.
Their public metadata pages are [HKLDW](https://arxiv.org/abs/1705.04771),
[Hughes--Rudnick](https://arxiv.org/abs/math/0304129), and
[Tanigawa--Zhai](https://arxiv.org/abs/0805.1525). Discovery results for
other papers were not treated as inspected substantive theorem interfaces
or as mathematical evidence. Earlier Matthiesen and Lamzouri limitations
were read only in the authorized predecessor artifact and not re-audited.

## 7. Recommended state effect

**No change.** Retain the existing complete exponent 10beta and the
open signed middle-band target. Archive (1)--(3) as a fully priced
pair-correlation application, and the two incompatible higher-moment
interfaces as scoped failures. The elementary local-density identity
(8) may be independently reviewed if useful, but it does not justify
a new target promotion. No source card, graph, proof draft, validation
matrix, synthesis, or successor design was changed. The task stops
after this report.
