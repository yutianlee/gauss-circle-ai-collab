# Full-goal strategy checkpoint after rounds223--225

## 1. Result and conductor decision

Mandatory review226, 2026-09-28. This checkpoint takes effect only after
validated round226 closure. The pinned September23 strategy remains in
force: count a complete bound or an improved fully restored exponent as
analytic progress. Rounds223--226 have supplied no such gain. All401 graph
nodes and the qualified Li--Yang benchmark remain unchanged.

The selected next objective is a COMPLETE signed Fejer sum of the actual
shifted r2 correlation remainders, specified below. The new reason to test
this interface is a current theorem directly about those correlations and
its Heegner-point spectral input. Its unweighted error does not already
prove the needed oscillatory estimate. This selection identifies the first
unproved inequality, not an established cancellation mechanism. Round227
must be designed after226 closes. Next broad current-primary review:229.

## 2. Exact full-goal scope and source conclusions

For fixed accepted radial mollifier rho, put Psi(s)=rho_hat(s e1), a real
even Schwartz function which may change sign. For every real T>=2 and
cT<=R<=CT, the entire real wave is
\[
B_T(R)=\sum_{n\ge1}r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
                 \cos(2\pi R\sqrt n-3\pi/4).
\]
Its target is T^epsilon. The inherited bound is for this COMPLETE REAL
wave only: beta=2theta_LY-1/2, where
theta_LY=(3292+25sqrt(1717))/13762. A complete exponent gamma restores
physical exponent 1/4+max(gamma,0)/2 through the accepted sharp bridge
P(R^2)=sqrt(R)B_T(R)/pi+O(T^(1/2+epsilon)). No per-block or complex beta
bound is inherited.

Exactly two theorem audits per source role were permitted. The reports
retain their primary versions, hypotheses, calculations and printed-text
limitations; none is imported into the accepted graph.

| Primary source | Consequence of the specified application |
|---|---|
| [Hulse--Kuan--Lowry-Duda--Walker1705.04771v3, Theorem7.1](https://arxiv.org/html/1705.04771v3) | The Laplace correlation error includes X^(1/2+epsilon) exp(h/X) h^Theta, with Theta<=7/64. The prose does not license removing h^Theta. A fixed Laplace test is not our rapidly oscillating weight, and complex substitution is unproved. |
| [Assing--Humphries2607.13518v1, Theorems1.2--1.3](https://arxiv.org/html/2607.13518v1) | Direct actual-r2 correlation and fixed-level, fixed-Heegner-point fourth-moment input. The first correlation regime gives N^(2/3) when h<=N^(64/69), using vartheta=7/64; other regimes remain. Absolute Abel transfer costs 1+Th/sqrt(N), so it yields no complete wave gain. The printed mean-square exponent N^(4/2) and proof self-reference are recorded literally; no conjectured typographical correction is used. |
| [Gan--He--Li--Wu2502.05973v2, Theorem1.3](https://arxiv.org/html/2502.05973v2) | A legal three-dimensional torus lift gives the actual two-dimensional coefficients. Rephased data, spatial trace, temporal evaluation and all scales cost complex T^(9/20+epsilon), weaker than the original triangle bound. The theorem does not permit a direct dimension-two substitution. |
| [Edwin--Lin2412.05485v1, Theorem1.1](https://arxiv.org/html/2412.05485v1) | Square-lattice growth parameter P=2 gives radius2/3, physical1/3 and complete real-wave1/6. It is applicable but weaker than the benchmark. |

The bounded status check preserves all five accepted Li--Yang application
repairs. Bourgain--Watt1709.04340, Dong--Robles--Zeindler2601.00292 and
Kim2509.24152 remain withdrawn in their inspected primary records.
Numerical evidence2609.04725 is not an asymptotic theorem. This review is
not an exhaustive assertion that no other relevant paper exists.

## 3. Complete next inequality and its exact sufficiency

Choose a fixed smooth phi on the positive axis, equal to one on x<=1 and
zero on x>=2, with bounded derivatives, and put w(x)=phi(x)-phi(2x).
Use dyadic integers N=2,4,... and define the zero-extended real weights
\[
g_N(t)=(t/N)^{-3/4}\Psi(\sqrt{t/T})w(t/N),\qquad
A_J(N)=(1+N/T)^{-J}.
\]
The support lies in N/2<t<2N. For each fixed derivative order and J,
the scaled derivatives are O(A_J), using a larger fixed Schwartz order
when needed. Put
\[
z_n=r_2(n)g_N(n)e(R\sqrt n),\quad
C_h=\sum_n z_{n+h}\overline{z_n},\quad
\rho_h=\frac8h\sum_{d\mid h}(-1)^{h+d}d,
\]
\[
I_h=\int_0^\infty g_N(t+h)g_N(t)
           e(R(\sqrt{t+h}-\sqrt t))\,dt,
\qquad {cal R}_h=C_h-\rho_h I_h.
\]
All n are positive integers; every overlap, including an empty one, is
literal. These are the actual r2 coefficients and the source's exact
density, not cusp-form substitutes or arbitrary coefficient vectors.

Set H=2N. The selected sufficient target, for any fixed J large enough,
is the ONE-SIDED complete signed estimate
\[
\boxed{\quad
2\Re\sum_{h=1}^{H-1}(1-h/H){\cal R}_h
\ll_{\epsilon,J} A_J(N)^2 N^{3/2}T^\epsilon .\quad}       \tag{F}
\]
Require it uniformly for all dyadic 2<=N<=P, all specified real R, and
P=2^ceil(log2(T^(3/2))). Thus T^(3/2)<=P<2T^(3/2), apart from harmless
equality at dyadic endpoints. The fixed cutoffs and mollifier are part
of the statement. There is no omitted shift regime, exceptional spectrum,
mean term or high-frequency shell. A proof can use a stronger two-sided
estimate, but individual absolute values are not assumed in (F).

Here is a direct sufficiency check. The ambient interval of integers has
L=3N/2-1 entries. Zero extension and Cauchy--Schwarz on the H translates
give the exact Fejer inequality
\[
|\sum_nz_n|^2\le\frac{L+H-1}{H}
 \left(\sum_n|z_n|^2+
       2\Re\sum_{h=1}^{H-1}(1-h/H)C_h\right).            \tag{G}
\]
Indeed summing H translates gives H times the original sum; the support
of the translated sum has at most L+H-1 integers. Expanding its square
has H copies of the diagonal and H-h copies of each correlation.
The multiplier in (G) is less than two and the bracket is nonnegative.

The diagonal is O(A_J^2 N^(1+eta)). On a nonempty overlap the derivative
of R(sqrt(t+h)-sqrt(t)) has magnitude comparable to Rh/N^(3/2).
The scaled phase has no stationary point; its higher derivative ratios
are uniformly bounded for the full overlap range. Smooth zero extension
therefore gives
\[
|I_h|\ll_J A_J^2\frac{N^{3/2}}{Th},\qquad
\rho_h\ll_\eta h^\eta.                                \tag{H}
\]
One integration by parts proves (H), including endpoint derivatives;
the weights vanish smoothly at the support boundaries. Empty overlaps
give zero. The normalized shell is N^(-3/4)sum z_n. Substituting (F)--(H)
into (G) pays its squared modulus by
\[
\ll A_J^2\{N^{-1/2+\eta}
       +T^{-1}N^\eta\log(2N)+T^\epsilon\}
\ll A_J^2T^{\epsilon'}.
\]
Use eta sufficiently small because N<=2T^(3/2), and rename epsilon.

The partition is exact: for every integer n>=2,
sum_{N=2,4,...,P} w(n/N)=phi(n/P), and its infinite limit is one.
The omitted original weight is 1-phi(n/P), supported on n>P. At fixed
sufficient Schwartz order its total absolute contribution is O(T^-A)
for any requested fixed A. The singleton n=1 is O(1). There are O(log T)
retained blocks, including all overlap endpoints. Thus (F) implies the
complete COMPLEX wave is O(T^epsilon), hence the required real wave and
the physical quarter theorem. This is a sufficient stronger complex
route; it is not granted by the inherited real benchmark.

## 4. First unproved step and method selection

No audited source proves (F). In the first Assing--Humphries regime an
absolute Abel application to one normalized correlation yields
N^(-5/6+epsilon)(1+Th/sqrt(N)). Summing its absolute errors through a
Fejer length H leaves squared-wave terms N^(1/6) and TH N^(-1/3), before
capping by the original coefficient bound. Already at N=T^(2/3), h=1,
the phase variation is order N. Fixed-h or fixed-test estimates cannot
silently absorb it. The other source regimes do not remove this problem.

The selected attempt must retain the joint signed oscillatory spectral
remainder through the h sum and its test transform. It must derive the
actual Heegner/spectral kernel and pay continuous and discrete spectra,
spectral ranges, transform norms, all shifts and reconstruction before
claiming improvement. The new fourth-moment source is a reason to inspect
that kernel, not permission to discard its costs. Repeating elementary
divisor completion from221 or the same absolute Abel bound is not a new
analytic step. If the bounded attempt stops at (F), report that fact.

The alternative theta report derives an exact damped Poisson expression
with delta=T^-1, actual mollifier average, real phase, continuous
subtraction and every dual shell retained. Damping removal costs
T^(-1/4+epsilon). Its separately absolute dual integral costs
T^(1/2+epsilon); coefficient triangle T^(1/4+epsilon) is already better.
This is an equivalent full signed interface, not an estimate or an
actual lower bound. Retain it as an alternative, not the selected next
objective: it currently lacks a more specific new quantitative input.

## 5. Controls and every complete frontier

The isolated complex-subordination derivation and separate application
review price legal straight rays at sqrt(omega/sigma), when
omega>=2sigma and sigma sqrt(N) is bounded. The one-coefficient test
separates this absolute-integral certificate from the actual value.
For actual shells sigma=N^-1/2, the loss is T^(1/2)N^(1/4).
Finite shell damping can be removed at bounded cost; global exponential
undamping of an infinite Schwartz series is not justified. Nothing here
rules out a different signed theta estimate or other contours.

| Complete owner | Preserved missing estimate |
|---|---|
| M1 HARD | Actual chi4 cone at L^(3/2) with all signs, profiles, floors and stars; full small-t/large-G remainder, t=1 and t>=2, not merely P2. |
| M1 SMOOTH | Every physical smooth residual at X^(1/4+epsilon); first critical profile still has X^(1/12) certificate deficit. HARD does not discharge it. |
| M2 TOP | Entire literal endpoint cone or accepted full real outer-energy complement, with every tag, collar, terminal member and exact centre. |
| M2 BAL | Full sum over G of G P_G at L^(3/2), both quarter shifts and actual symbols, including noncritical and boundary companions. |
| M2 UNBAL | Full actual chi4(h)a(h,k)e(sqrt(Xhk)) sum at (LK)^(3/4), K=XL/D^2, K/L>16, including transform and endpoint companions. |
| Total-M1 GAR | Entire real angular-divisor wave for C_X^*, not r2. Nonlower120 is paid; lower ownership through159 retains every D>1,L>1, generic t=1, t>=2 and the separate cross owner. Parent122 shorthand does not erase them. GAR still needs M2 and endpoints. |
| Whole-wave and moments | Complete real supremum, or an adequate unbounded sequence of FIXED even moments. The fixed distinct-class twelfth target29/25 yields only102/325, not quarter. |

Accepted204 retains both distribution terms V^-2 and TV^(-136/13),
and moments M_p<<T^(1+epsilon)+T^((p-2)beta+epsilon). Accepted216's
class/head bridge makes Q_p=floor(T^(1/p)), I_p<<T^(5/4+epsilon) at an
unbounded sequence of fixed even orders sufficient for quarter. No p(T)
uniformity is asserted. No such moment improvement follows here.

Closed224's angular prime commutator and closed225's all-scale factor
menu81/614>beta remain scoped evidence. The favorable local47/378 is not
a complete gain. Closed225's complex13/56 ceiling may cap weaker complex
certificates but does not improve the complete real benchmark. All upper
certificate limitations are distinguished from arithmetic lower bounds.

## 6. Dependencies and provenance

Conductor, NONBLIND, round226. Uses protocol, graph/manifest, pinned Sep23
review, checkpoint223, closed224--225 syntheses, accepted204/216 kernels,
the frozen complete interface packet, the two current source reports,
isolated subordination report and conductor application. Primary status
is recorded separately in controls/conductor_current_primary_status.md.
Current campaign root: rounds/codex-managed/gc-full-goal-spectral-source-review.
Final report and checkpoint hashes are bound by nonauthor reviews and the
closure reconciliation. At least95 percent analytical work; zero experiments.

## 7. State effect and stopping rule

Identity State Patch, pending required green reviews and mechanical
validation. No graph/draft promotion or complete exponent improvement.
Retain the source audits and limited controls; select (F) for the next
bounded analytic design. Close the current round before beginning that
design. Full quarter and every alternative complete owner remain open.
An inability to prove (F) is not an external blocker or a disproof of the
actual target. Do not replace it with an indefinite list of smaller
unestimated complements. Review the broad strategy and current primary
literature again at229.
