# Round 202 independent signed-convolution seam review

## 1. Result

- Campaign: `gc-strategy-signed-moment-majorant-review`; round: 202.
- Task/role: `signed_convolution_review`, independent analytical seam reviewer.
- Generated: 2026-09-23T12:53:27Z.
- Starting graph hash, supplied by the candidate: `682cb189a3ab0ef26f8d19701e2949547446d37505df01f7b7eaf1cfdd0f359c`.
- Exact reviewed candidate SHA256: `721062ebf220029faf13b12ee68b3aac1d5736f72d2b747694671bf91654b936`.
- Analytical work only; no numerical experiments or external sources.

**Result: retain the signed-convolution identity as a correct, complete reformulation; the low-head hypothesis can be discharged for the explicit choice U = T^(1/2047).** The Plancherel signs, all sixfold sign choices and their cross terms, polynomial-annihilating kernel moments, and finite-to-infinite passage check out with the conventions below. The implied disk-moment and persistence exponents have the stated arithmetic, conditional on the separate disk reduction and its error control.

**The identity is not an estimate.** In particular, this review does not prove candidate (C2), a sixfold approximation theorem, a power saving, or any open Gauss-circle obligation. Kernel moment cancellation supplies no bound for an arbitrary singular convolution measure.

## 2. Exact statement and hypotheses

Write e(x) = exp(2 pi i x), and use

\[
 \widehat f(\xi)=\int_{\mathbb R}f(R)e(-R\xi)\,dR,
 \qquad f(R)=\int_{\mathbb R}\widehat f(\xi)e(R\xi)\,d\xi.
\]

Let T >= 1, let Psi be a fixed real Schwartz function, and put

\[
 a_n(T)=r_2(n)n^{-3/4}\Psi(\sqrt{n/T}),\qquad
 H_{T,I}(R)=\sum_{n\in I}a_n(T)\cos(2\pi R\sqrt n-3\pi/4).
\]

Fix a real nonnegative chi in C_c^infinity((0,infinity)), equal to one on [1/sqrt(2),sqrt(3)], and put w = chi^2. The accepted exact-mass hypothesis granted in the task is the **absolute** bound

\[
 E_{12}(T):=2^{-12}\sum_{\varepsilon\in\{\pm1\}^{12}}
 \sum_{\substack{n_1,\ldots,n_{12}\ge1\\
       \sum_j\varepsilon_j\sqrt{n_j}=0}}
       \prod_{j=1}^{12}|a_{n_j}(T)|\le C_{\rm exact}.
 \tag{R1}
\]

The conductor explicitly confirmed that this accepted result is uniform under arbitrary, including unequal, cutoffs and includes nonpairing exact relations. Its supplied majorant applies to b_n <= C tau(n)n^(-3/4), with actual C = 4||Psi||_infinity. Thus every restriction of the summation in (R1) is also bounded. A bound only on one untruncated signed aggregate would not suffice here, but that is not the granted hypothesis.

For every real U >= 1, define

\[
 \mu_{T,>U}=\frac12\sum_{n>U}a_n(T)
 \{e(-3/8)\delta_{\sqrt n}+e(3/8)\delta_{-\sqrt n}\},
 \qquad \nu_{T,U}=\mu_{T,>U}^{*6},
 \qquad K_T(\xi)=T\widehat\chi(T\xi).
\]

Then the following hold:

1. The candidate identity (C1) is exact:
   \[
    \int w(R/T)|H_{T,>U}(R)|^{12}\,dR
       =\|K_T*\nu_{T,U}\|_2^2.
    \tag{R2}
   \]
2. Every integer j >= 0 satisfies
   \[
    \int \xi^jK_T(\xi)\,d\xi
       =T^{-j}(2\pi i)^{-j}\chi^{(j)}(0)=0.
    \tag{R3}
   \]
3. With the explicit choice U = T^(1/2047),
   \[
    \int w(R/T)|H_{T,\le U}(R)|^{12}\,dR\ll_{\chi,\Psi,C_{\rm exact}}T.
    \tag{R4}
   \]
4. For eta >= 0, the full physical moment bound
   \[
    \int w(R/T)|H_{T,\ge1}(R)|^{12}\,dR
       \ll_\epsilon T^{1+2\eta+\epsilon}
    \tag{R5}
   \]
   is equivalent, with arbitrary epsilon renamed, to candidate (C2)
   \[
    \|K_T*\nu_{T,U}\|_2\ll_\epsilon T^{1/2+\eta+\epsilon}.
    \tag{R6}
   \]

All constants are independent of T; the elementary separation proof below has very large but fixed constants.

## 3. Proof and derivation

### Absolute convergence and the legitimate Plancherel object

The elementary lattice bound sum_(n<=x) r_2(n) = O(x), for x >= 1, follows by placing the corresponding lattice points inside a square of side O(sqrt(x)). Partial summation or dyadic summation gives

\[
 \sum_{n\le x}r_2(n)n^{-3/4}\ll x^{1/4}.
 \tag{R7}
\]

Schwartz decay of Psi, followed by dyadic summation above n = T, therefore gives

\[
 \sum_{n\ge1}|a_n(T)|\ll_\Psi T^{1/4}<\infty.
 \tag{R8}
\]

For example, on n in [2^k T,2^(k+1)T], the weighted r_2 sum is O((2^k T)^(1/4)), whereas Psi contributes O_M(2^(-kM/2)); any M > 1/2 makes the resulting series convergent. Consequently mu and nu have finite total variation, H is a uniformly convergent real-valued series, and all finite-degree expansions below are absolutely summable at fixed T.

With the stated Fourier convention, inverse transformation of mu gives exactly

\[
 \frac12\sum_{n>U}a_n(T)
   [e(R\sqrt n-3/8)+e(-R\sqrt n+3/8)]
      =H_{T,>U}(R).
\]

Its sixth power is the inverse Fourier transform of nu. The function to which Plancherel is applied is **chi(R/T) H_(T,>U)(R)^6**, which is compactly supported, bounded, and in L1 intersect L2. Direct Fubini gives its Fourier transform as K_T * nu, proving (R2). Neither H alone nor a nonzero atomic measure is being asserted to belong to L2.

For a fully explicit limiting argument, truncate the sums at n <= N. Then mu_N -> mu in total variation, and the convolution telescoping identity gives nu_N -> nu in total variation. Young's inequality in the measure form gives

\[
 \|K_T*(\nu_N-\nu)\|_2
       \le\|K_T\|_2\|\nu_N-\nu\|_{\rm TV}\longrightarrow0.
\]

Meanwhile H_N -> H uniformly, so the compactly supported physical integrals converge. Thus the infinite identity follows from the finite one without any unproved interchange or uniform-in-T limiting requirement.

### Sixfold phases and all cross strata

An atom of nu indexed by six signs sigma_j and six indices n_j has location and coefficient

\[
 A=\sum_{j=1}^6\sigma_j\sqrt{n_j},\qquad
 c_A=2^{-6}\prod_{j=1}^6a_{n_j}(T)
                e\!\left(-\frac38\sum_{j=1}^6\sigma_j\right),
\]

where the indexing is retained if different choices produce the same location. If k signs are positive, the phase is e(-3(2k-6)/8), for every k = 0,...,6. The convolution includes all seven groups and their binomial multiplicities.

For a second labelled atom B with coefficient c_B,

\[
 \int K_T(\xi-A)\overline{K_T(\xi-B)}\,d\xi
   =\int w(R/T)e(R(A-B))\,dR
   =T\widehat w(T(B-A)).
 \tag{R9}
\]

Hence the corresponding cross term is c_A conjugate(c_B) times the last expression. Writing the signs in the second group as minus their original signs converts A-B into a general twelve-root signed sum Delta and the coefficient phase into e(-3 sum(epsilon_j)/8). Equivalently the direct twelfth-power expansion has factor T hat(w)(-T Delta), in agreement with (R9).

Thus all 49 pairs of sixfold sign-count groups occur, and within them all 2^12 twelve-sign assignments occur. There is no restriction to six positive and six negative roots in the final twelve-root expansion. Repeated indices, exact collisions, nonpairing relations, and unbalanced sign counts have not been removed. Real coefficients give the useful symmetry nu(-A) = conjugate(nu(A)); w is generally not even, and replacing hat(w)(-T Delta) by hat(w)(T Delta) without the matching conjugation would be an error. The stated norm identity makes no such replacement.

### Kernel moments and their exact scope

Schwartz regularity allows differentiation under Fourier inversion and yields (R3). Because chi vanishes on a neighborhood of zero, all these derivatives are zero. Accordingly K_T * p = 0 for every polynomial p; the integral defining this convolution is absolutely convergent because K_T is Schwartz.

A precise smooth-function consequence is available when the needed derivative norm exists. Taylor's formula and the first m vanishing moments give, for m >= 1,

\[
 \|K_T*g\|_2
   \le \frac{T^{-m}}{m!}
      \left(\int |u|^m|\widehat\chi(u)|\,du\right)\|g^{(m)}\|_2,
 \tag{R10}
\]

initially for smooth g and then by the usual Sobolev approximation. The same bound holds with the supremum norm when the derivative is bounded and convolution is defined. This explains a possible smooth-bulk strategy but imposes an explicit derivative cost. The actual nu is an atomic measure, so (R10) cannot simply be applied to it. A decomposition nu = g + remainder would need both the displayed smooth cost and an adequate L2 bound on K_T * remainder.

### Independent radical-separation lemma

Let n_1,...,n_12 be arbitrary positive integers <= U, and let

\[
 \Delta=\sum_{j=1}^{12}\varepsilon_j\sqrt{n_j}\ne0.
\]

Then

\[
 |\Delta|\ge(12\sqrt U)^{-2047}.
 \tag{R11}
\]

To prove this without assuming independent squareclasses, first form the **formal** polynomial

\[
 \mathcal P(Z;x_1,\ldots,x_{12})
   =\prod_{\sigma\in\{\pm1\}^{12}}
               \left(Z-\sum_{j=1}^{12}\sigma_jx_j\right).
\]

It has integer coefficients and is invariant under each individual formal substitution x_j -> -x_j, because that substitution permutes the 4096 labelled factors. Therefore every coefficient, as a polynomial in the x_j, contains only even powers of every x_j. Specializing x_j = sqrt(n_j) consequently gives a monic polynomial P(Z) in Z[Z], degree 4096. This argument takes place before specialization and remains valid for repeated indices, square indices, and arbitrary dependencies among their squareclasses.

Some signed sums may vanish. Let m be the multiplicity of the zero root and write P(Z) = Z^m Q(Z), with Q in Z[Z] and Q(0) != 0. Removing these exact zero factors is essential. There are q = 4096-m nonzero roots, counted with multiplicity, each of absolute value at most L = 12 sqrt(U). Both Delta and -Delta occur as two labelled nonzero factors. Therefore

\[
 1\le|Q(0)|
   =\prod_{\text{nonzero labelled roots }s}|s|
   \le |\Delta|^2L^{q-2}
   \le |\Delta|^2L^{4094}.
\]

This proves (R11). In particular, neither linear independence of radicals nor a maximal-degree multiquadratic field is assumed. Extra collisions or extra zero factors can only strengthen the product estimate.

### Independent head estimate

Set U = T^(1/2047). For every nonzero signed sum in the head expansion, (R11) implies

\[
 T|\Delta|\ge12^{-2047}T U^{-2047/2}
                  =12^{-2047}T^{1/2}.
 \tag{R12}
\]

Write S_U = sum_(n<=U) |a_n(T)|. Boundedness of Psi and (R7) give S_U = O(U^(1/4)), with no divisor-bound epsilon needed. Expand the finite real twelfth power and integrate. The absolute value of the exact-resonance contribution is at most

\[
 T\widehat w(0)E_{12}(T)\ll T.
\]

For the remaining terms, |hat(w)(x)| <= C_w (1+|x|)^(-2). By (R12), the total absolute off-diagonal contribution is at most

\[
 C_w T S_U^{12}(1+12^{-2047}T^{1/2})^{-2}
       \ll T U^3 T^{-1}
       =T^{3/2047}\le T.
\]

This proves (R4). The constants absorbed in this estimate are fixed, however large. The proof works for real U and requires no squarefree restriction. It also shows why the asserted low-head estimate is genuinely independent of any proposed high-tail cancellation mechanism.

### Complete moment target, mixed head/tail terms, and net exponent

Use the positive measure d rho_T(R) = w(R/T)dR. Since H_full = H_head + H_tail, the L12(rho_T) triangle inequality in both directions and (R4) give the equivalence of (R5) and (R6) for eta >= 0, after renaming arbitrary epsilon. The convolution norm is the square root of the twelfth moment, so its eta contributes 2 eta in the T-moment exponent; this factor is essential.

For each j = 0,...,12, Holder gives

\[
 \int w(R/T)|H_{\rm head}|^{12-j}|H_{\rm tail}|^j\,dR
 \le M_{\rm head}^{(12-j)/12}M_{\rm tail}^{j/12}.
 \tag{R13}
\]

If (R6) holds, this is O_epsilon(T^(1+j eta/6+epsilon)), hence at most the full target O_epsilon(T^(1+2 eta+epsilon)). The binomial expansion contains only finitely many such terms. Therefore no mixed head/tail stratum is missing.

For the exponent conversion only, put Y = T^2. The separate disk reduction must identify a main term of size R^(1/2) H(R), with its remainder adequately controlled. Its twelfth power supplies R^6 and the substitution X = R^2 supplies dX = 2R dR. On the fixed window R asymptotic to T, the resulting cost is O(T^7). Thus a physical moment T^(1+2 eta+epsilon) yields

\[
 T^7T^{1+2\eta+\epsilon}
      =Y^{4+\eta+\epsilon/2}.
\]

The fact that chi = 1 on [1/sqrt(2),sqrt(3)] supplies the whole interval X in [Y/2,3Y]. For the standard discrepancy P(X) = N(sqrt(X))-pi X, monotonicity of N gives one-sided persistence of a value of magnitude A over an interval of length comparable to A. Its twelfth-moment cost is then comparable to A^13. Consequently the conditional moment above gives pointwise exponent (4+eta)/13, with epsilon renamed. Improving a benchmark theta_LY requires exactly eta < 13 theta_LY - 4. This checks the algebra, without independently importing the disk reduction, its error estimates, or the value and provenance of that benchmark.

## 4. First doubtful or unproved step

There is no doubtful step in (R2), (R3), or (R4) under the stated hypotheses. The candidate's first substantive unproved step is (C2)/(R6), uniformly in T for the complete actual signed measure with U = T^(1/2047).

The statement that the kernel suppresses a smoothly varying bulk is rigorous only with quantified hypotheses such as (R10). The candidate correctly requires a remainder theorem before using such a subtraction. Neither one-factor area counting, the existence of all vanishing moments, nor a continuous-frequency model supplies that theorem for the actual sixfold measure. Replacing mu or nu by total variation, or K_T by its absolute value, destroys the cancellation represented by the identity and is not a route to its claimed power target.

The downstream disk result also remains conditional on the separately accepted reduction and remainder control. This review verifies the exponent conversion, not those separate analytic premises.

## 5. Required control tests and outcomes

These are exact analytical controls, not numerical evidence.

1. **One-frequency Fourier-sign control: PASS.** For a single retained index, inverse transformation of the two atoms gives a_n cos(2 pi R sqrt(n)-3 pi/4), with the candidate's phase signs. A cross pair A,B yields T hat(w)(T(B-A)), agreeing with the direct e(R(A-B)) integral.
2. **All sixfold sign/mixed-stratum control: PASS.** The k = 0,...,6 decomposition and all 49 cross-group pairs are present. Formula (R13) covers every head/tail mixture, including the endpoints j = 0 and 12.
3. **Dependent-radical and square-index control: PASS.** Formal sign invariance precedes specialization. For example, if all n_j = 1, many signed roots vanish and many others coincide, but dividing out the full zero multiplicity leaves Q(0) a nonzero integer. The proof never assigns independent automorphisms to dependent squareclasses.
4. **Exact-zero-factor control: PASS.** The product lower bound is applied to Q(0), not P(0). The latter can vanish and would give no separation estimate.
5. **Infinite-tail control: PASS.** The actual Schwartz cutoff gives total-variation convergence, and the convolution/Plancherel limit uses compact physical support. No finite band has replaced the full tail.
6. **Constant and polynomial bulk control: PASS, limited scope.** All polynomial convolutions vanish exactly. For nonpolynomial smooth bulk, the explicit derivative cost in (R10) remains; for a general atomic measure no small norm follows.
7. **Unsigned/adversarial shortcut control: PASS as a limitation check.** The identity itself is coefficient-agnostic and therefore also holds for many altered real coefficients. Its existence cannot distinguish the arithmetic case from an obstructed analogue. Any future claim of a saving must introduce and verify a coefficient-sensitive estimate absent from this review. The head lemma claims only a small cutoff moment using the granted exact mass and therefore does not purport to solve the full unsigned or adversarial high-tail problem.

## 6. Dependencies and exact artifacts used

Files read, and no others:

- `protocol.md`.
- `rounds/codex-managed/gc-strategy-signed-moment-majorant-review/candidates/conductor_signed_convolution_interface.md`, SHA256 `721062ebf220029faf13b12ee68b3aac1d5736f72d2b747694671bf91654b936`.

Task-granted mathematical inputs: the actual coefficient formula, fixed real bounded Schwartz Psi, and the accepted full absolute exact twelve-root mass (R1), including the conductor's explicit confirmation of cutoff uniformity and nonpairing coverage. These accepted premises were supplied by the conductor rather than independently audited from graph files, preserving the assigned context isolation.

Other ingredients proved or explicitly derived here: the O(x) elementary lattice bound and its weighted consequence; absolute convergence; all convolution signs and limiting passages; the formal integer polynomial and separation estimate; the resulting O(T) head moment. Standard Fourier inversion, Plancherel, Taylor's formula, Young's inequality, and Holder/triangle inequalities are used with their required hypotheses stated above. There are no external citations, source-dependent estimates, or numerical experiments. The disk reduction and benchmark provenance remain separate dependencies, not results of this review.

## 7. Recommended state effect

**Retain** (C1) and the signed-convolution formulation as an exact strategy interface. **Revise** the candidate's provisional low-head clause to the explicit proved choice U = T^(1/2047), with (R1) listed as a dependency and (R11)--(R12) as the separation argument. The conductor may consider promoting that narrow head lemma only after the required independent validation and mechanically valid State Patch.

**No change** to the status of (C2), any full signed high-tail estimate, or any Gauss-circle target obligation. This report does not close the round or design its successor. It edits no authoritative graph, proof draft, validation matrix, or synthesis. The identity is not an estimate.
