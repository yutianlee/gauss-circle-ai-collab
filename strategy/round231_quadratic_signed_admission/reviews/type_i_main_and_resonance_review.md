# Round231 independent review: piecewise Type-I main and resonant patches

- Date: 2026-10-11.
- Role: independent nonauthor reviewer of the newly specified Type-I main and the conductor's resonant-patch control; this is separate from the frozen blind finite-field report.
- Packet: round231_quadratic_signed_admission.
- Starting graph identifier, supplied provenance only: a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
- No sibling report was read. No shared state or source artifact was edited.

## 1. Result and named seam verdicts

**PASS: complete piecewise Type-I main supremum.** The proposed bound is valid for the exact patch-dependent approximant in the review brief:

    sup_(T/2 <= R <= 2T) |S_sharp,T(R)|
      <<_epsilon T^(13/84+epsilon) X0^(-103/840)
      = T^(5447/52500+epsilon)
      = T^(13/125-13/52500+epsilon),

where X0=T^(52/125). An actual r2 tail beyond T^(3/2), if included in this explicitly owned main, contributes O_K(T^(-K)) for every fixed K.

**PASS: avoiding the patch-count loss.** For each divisor d, its support across the entire ordered shell is a single interval, and its varying logarithmic multiplier has bounded total variation across the entire shell. One first exchanges the divisor and n sums and then applies interval estimates plus summation by parts. There is no summation of one absolute exponential-sum estimate per patch.

**PASS: chi4(n/d), proper intervals, phase class, and endpoints.** The quotient character is handled by its two nonzero residue classes modulo 4. The resulting shifted square-root phases lie in the monomial derivative class of the accepted exponent-pair theorem. Arbitrarily short first/last interval portions are allowed.

**PASS: the proposed main moment.** Since the assembled coefficients are fixed independently of R and divisor bounded, the accepted coefficient-uniform large-value kernel applies and gives

    M_12(S_sharp,T) <<_epsilon T^(3044/2625+epsilon)
                              = T^(29/25-1/2625+epsilon).

This applies to the complex main and hence to its physical cosine projection.

**PASS, scoped: conductor resonant-patch control.** The displayed actual-r2 local lower bounds and their refutation of a uniform uncentered square-root estimate are correct. They give no lower bound for the complete wave or its complete moment.

**OPEN: residual and complete target.** Nothing here pays the difference r2-rsharp, converts a short-interval residual theorem into a complete residual ceiling, or improves the complete circle moment.

## 2. Exact hypotheses and objects

Use the mollifier and window from briefs/complete_interface.md. Thus Psi is fixed real even Schwartz with Psi(0)=1, and w is fixed bounded nonnegative and supported in [1/2,2]. Put

    X0=T^(52/125),       Z=T^(3/2),       T sufficiently large.

Take T large enough that every retained ambient shell has N>=3, so all logarithms in the approximant are nonzero and the source start parameter is in its stated domain. The asymptotic claims concern this range. A bounded lower-T extension would require specifying the approximant at any shell starting at 1; that convention is not supplied and is not needed here.

In each ambient dyadic shell (N,2N] meeting (X0,Z], choose an ordered partition into consecutive real intervals with starting points x_j and lengths comparable to H4=N^(9/10)T^(-1/5). Choose this partition independently of R. Cutting by X0 or Z can shorten endpoint pieces. Take a consistent half-open assignment of boundary integers.

For n belonging to the patch starting at x(n)=x_j, put r(n)=x(n)^(1/20) and

    rsharp_T(n)
       =4 sum_(r(n)<=d<r(n)^2, d|n)
             chi4(d) [log n-log r(n)^2]/log r(n)
        +4 sum_(d<r(n), d|n) [chi4(d)+chi4(n/d)].

This is exactly the formula in the brief and in the cited Appendix A.3, with the local start replacing its X.

Define

    S_sharp,T(R)
      = sum_(X0<n<=Z) rsharp_T(n) n^(-3/4)
                        Psi(sqrt(n/T)) e(R sqrt(n)).

If desired, define the separately paid actual infinite tail

    E_T(R)=sum_(n>Z)r2(n)n^(-3/4)Psi(sqrt(n/T))e(R sqrt(n)).

The conclusions hold for S_sharp,T and for S_sharp,T+E_T. No unspecified extension of rsharp beyond Z is needed. The physical main is Re(e(-3/8)S_sharp,T), so its absolute value is at most |S_sharp,T|.

The implicit constants may depend on epsilon, fixed partition-comparability constants, Schwartz seminorms, and w, but not on T, R, the number of patches, or the locations of their internal boundaries. In fact the main proof only needs x(n) to be nondecreasing within each shell and comparable to N; it does not use the particular size H4.

For the separate resonance seam, use exactly the conductor's hypotheses: fixed 2/5<sigma<2/3, N=T^sigma, and h=floor(c N^(5/6)T^(-1/3)) for sufficiently small fixed c>0.

## 3. Independent derivation and source audit

### 3.1. First assemble the entire shell

Within one shell let x(t) be its nondecreasing step function of patch starts. Thus x(t) is comparable to N, including endpoint restrictions. Write

    L(t)=20 log(t)/log(x(t))-2.

This is the logarithmic multiplier in rsharp. For every fixed positive integer d, its two possible supports are

    I_d^(mid) = {t: d^10 < x(t) <= d^20},
    I_d^(small) = {t: d^20 < x(t)}.

The strict and weak inequalities follow directly from r<=d<r^2 and d<r. Since x(t) is nondecreasing, each support, intersected with the shell and (X0,Z], is an interval, possibly empty and possibly with an open endpoint. It is not a union requiring one estimate per patch.

Moreover,

    sup |L| << 1,             Var_shell(L) << 1/log N,

for N large; a uniform O(1) bound suffices. To verify the variation claim, log t is increasing with total variation at most log 2, while 1/log x(t) is decreasing and has total variation O((log N)^(-2)). The product variation inequality gives

    Var(log t / log x(t))
       <= sup(log t) Var(1/log x(t))
          + sup(1/log x(t)) Var(log t)
       << 1/log N.

This includes all jumps at all patch boundaries. Restriction to either divisor support adds at most two jumps of bounded magnitude. The absence of a patch-count loss is therefore exact.

Let v_T(t)=t^(-3/4)Psi(sqrt(t/T)). Schwartz decay and differentiation show, on the shell, for every fixed A>=0,

    sup |v_T| + Var(v_T)
       <<_A N^(-3/4)(1+N/T)^(-A).

For example t times the derivative of Psi(sqrt(t/T)) equals
(sqrt(t/T)/2)Psi'(sqrt(t/T)); it has the same sort of Schwartz bound. Products with L obey the same inequality up to an absolute factor. These are bounded-variation weights for an interval sum in m after n=dm.

### 3.2. The accepted exponent-pair input applies to these phases

The primary exponent-pair source is Bourgain, arXiv:1408.5794v2, Section 5, Theorem 6 and the discussion of proper subintervals following it:
https://arxiv.org/html/1408.5794v2#S6

It states the pair (13/84+epsilon,55/84+epsilon); its discussion covers ambient length M up to the phase-size parameter and proper subintervals, at logarithmic cost. It requires the standard monomial derivative class, not arbitrary oscillatory functions. This review uses that full theorem, as already accepted in the listed kernel, rather than the narrower direct range preceding Theorem 6.

Here, for fixed d, the unsplit phase is

    f(m)=R sqrt(d m),       m comparable to M=N/d.

Its derivative is exactly (R sqrt(d)/2)m^(-1/2). The monomial parameter is s=1/2; every required derivative is an exact derivative of this model. The normalized phase is a constant multiple of sqrt(t) on a fixed positive compact interval. The source phase-size parameter is

    mathcalT comparable to R sqrt(N) comparable to T sqrt(N).

All relevant d satisfy d<<(2N)^(1/10), so M is large. Also

    M/mathcalT << sqrt(N)/(dT) <= T^(-1/4)/d

because N<<T^(3/2). Thus the required length<=phase-size condition holds uniformly for sufficiently large T. Fixed enlargement constants are absorbed into the final constant; any bounded parameter range where the approximant is defined can be handled by increasing it.

Writing k=13/84 and l=55/84, the theorem on any proper interval J in this ambient shell yields

    |sum_(m in J) e(R sqrt(d m))|
       <<_epsilon T^epsilon mathcalT^k M^(l-k)
       <<_epsilon T^(13/84+epsilon)
                       N^(97/168) d^(-1/2).                 (1)

Every parameter is bounded by a fixed power of T, so source epsilon powers and the proper-interval logarithm are absorbed in the displayed T^epsilon. No weighted exponent-pair assertion is used.

For the quotient-character term, chi4(m)=1 on m=1 mod 4, -1 on m=3 mod 4, and zero on even m. Each of the two nonzero classes is parameterized as m=4ell+r, r in {1,3}. Its phase is

    f_r(ell)=R sqrt(d(4ell+r))
           =2R sqrt(d) sqrt(ell+r/4).

On ell comparable to N/(4d), every fixed derivative is the corresponding derivative of the exact shifted monomial. Relative to the unshifted monomial its derivative errors are O_j(1/M), uniformly for these two fixed shifts. They therefore meet the same finite-order monomial-approximation conditions for sufficiently large M. The length and phase-size parameters differ only by fixed constants. Thus (1) also holds for the chi4(m)-weighted sum, by adding the two class estimates. This step preserves the quotient character; it never identifies it with chi4(d).

### 3.3. Sum over divisors, not over patches

Summation by parts on the single support interval for each d now gives the following bound for each of the three types of divisor term:

    <<_epsilon T^(13/84+epsilon)
        N^(97/168-3/4) d^(-1/2)(1+N/T)^(-A).

The mid-range term has d<(2N)^(1/10). Consequently its full shell contribution is at most

    T^(13/84+epsilon) N^(-29/168)
          sum_(d<<(2N)^(1/10)) d^(-1/2)
       << T^(13/84+epsilon) N^(-103/840).                (2)

The two small-divisor terms have d<<(2N)^(1/20), and are bounded by

    T^(13/84+epsilon) N^(-29/168+1/40)
       = T^(13/84+epsilon) N^(-31/210),

which is stronger than (2). Factors 4, character signs, and the two residue classes are fixed constants.

No use of H4 entered (2). In particular, it has not been multiplied by N/H4. The two places where the full piecewise definition matters are its monotone supports and the globally bounded variation of L.

### 3.4. Dyadic recombination, endpoints, and complete tail

The exponent -103/840 is negative. Summing (2) over dyadic shells meeting (X0,Z] is a geometrically convergent sum bounded by a constant times

    T^(13/84+epsilon) X0^(-103/840).

A first shell with N<X0<=2N still has N comparable to X0. Its retained integers form an interval. The same applies to the last shell cut by Z. A divisor support cut by either endpoint is still an interval; the proper-interval bound (1) and the variation estimate cover even a singleton. No end interval is required to have length comparable to H4.

The exact exponent arithmetic is

    13/84 -(52/125)(103/840)
        = 5447/52500
        = 13/125-13/52500.                              (3)

For the actual remaining tail, r2(n)<=4d(n)<<_eta n^eta. With a fixed Schwartz decay order L sufficiently large,

    sup_R |E_T(R)|
       << T^(L/2) Z^(1/4+eta-L/2)
        = T^(3/8+3eta/2-L/4)
       <<_K T^(-K).

The bound is absolute, includes all tail terms, and is uniform in real R. This proves the stated supremum, with its explicitly assigned tail.

### 3.5. The complete main coefficient vector and its moment

On every patch, |L(n)|<<1. Therefore

    |rsharp_T(n)| << d(n) <<_eta n^eta.

The partition is independent of R, so the coefficients

    a_n=1_(X0<n<=Z) rsharp_T(n)n^(-3/4)Psi(sqrt(n/T))

are one fixed coefficient vector for the entire physical R window. On each ambient dyadic block,

    sum |a_n|^2 <<_eta N^(-1/2+2eta)
                  <<_eta T^(3eta) N^(-1/2).

Sections 4 and 5 of the accepted kernel apply directly to this vector: their finite duality bound uses this energy and an unweighted square-root correlation kernel. It does not require a_n to equal the actual r2 coefficients, or to have an arithmetic sign pattern. Zero-extension covers both endpoint blocks. With the finitely many dyadic blocks recombined as in that kernel, one obtains

    D_sharp(V) <<_epsilon T^epsilon
                    (V^(-2)+T V^(-q)),       q=136/13, V>=1.       (4)

The bound is for the complex wave as well. A negligible E_T can be included by replacing V by a fixed fraction of V. This use does not transfer the actual full-wave supremum to an arbitrary mask: the independent supremum (3) has already been proved for this main.

Let delta=5447/52500 and W=C_epsilon T^(delta+epsilon). Layer cake with (4) gives

    M_12(S_sharp,T)
       <<_epsilon T^(1+epsilon)
          +T^epsilon W^10
          +T^(1+epsilon) W^(12-q).

Here 12-q=20/13. Also delta(q-2)=4609/5250<1, so the W^10 term is smaller than the final term in exponent. Finally,

    1+(20/13)delta
       =3044/2625
       =29/25-1/2625.

Taking the epsilon losses sufficiently small proves the candidate main moment. The same moment follows for its physical cosine projection. A negligible added tail contributes negligibly by the norm inequality on a window of measure O(T).

### 3.6. What Appendix A.3 supplies, and what was not used

The primary arithmetic source is Matomaki, Shao, Tao, and Teravainen, arXiv:2204.03754v4, Theorem 1.1(iii) and Appendix A.3 / Proposition A.3:
https://arxiv.org/html/2204.03754v4

Appendix A.3 gives exactly the displayed twisted Type-I approximant, with R2=X^(1/20). Proposition A.3 transfers the k=2 residual theorem to r2-r2sharp. That theorem requires X^(1/3+epsilon)<=H<=X^(1-epsilon), with fixed degree/dimension and stated complexity dependence. It is a statement about the residual, not a bound for the explicit main.

The present main proof uses the approximant's exact algebraic formula and the separate accepted exponent-pair input; it does not invoke a residual estimate or replace the square-root phase by a polynomial.

For orientation, throughout the specified shell range,

    N^(109/260) <= H4 <= N^(23/30)

up to fixed endpoint comparability constants. Thus full-sized patches leave a positive source length margin: 109/260-1/3=67/780. This observation alone proves no residual wave estimate. The phase approximation, error summation, endpoint extension if needed for that theorem, and complete residual ownership remain outside this review.

### 3.7. Independent check of the conductor's actual-r2 resonance proof

The lattice disk/unit-square comparison gives

    A(x)=sum_(n<=x)r2(n)=pi x+O(sqrt(x)+1).

Therefore the interior shell [13N/10,17N/10] contains actual r2 mass at least cN for large N. Since h=o(N), each integer n in that interior shell is counted in exactly 2h+1 sums

    S_m=sum_(|n-m|<=h)r2(n),

with integer m in [6N/5,9N/5]. The sum over all such centers is at least cNh, and there are O(N) centers. Hence some integer m satisfies S_m>=c1h.

The hypotheses give

    h comparable to T^(5sigma/6-1/3) -> infinity,
    h/N -> 0.

For this center, set k to the nearest integer to T/(8m^(3/2)). Since sigma<2/3, that quotient tends to infinity; thus k>=1 and

    R=8k m^(3/2),       |R-T|<=4m^(3/2)=o(T).

In particular R lies in [T/2,2T] for sufficiently large T.

For every integer |j|<=h, the degree-two Taylor polynomial is exactly

    R sqrt(m+j)=8k m^2+4kmj-kj^2+E_j.

All three polynomial terms are integers. The third derivative of R sqrt(t) is 3R/(8t^(5/2)), so Taylor's theorem gives

    |E_j| <= C T N^(-5/2)h^3 <= C c^3.

Choose c so that |2pi E_j|<=pi/12. Then Re e(R sqrt(m+j))>=cos(pi/12). Nonnegativity of r2 proves the claimed complex lower bound.

For the physical phase,

    -3pi/4+2pi E_j lies in [-5pi/6,-2pi/3],

whose cosine is at most -1/2. Since N/T->0 and Psi is real continuous with Psi(0)=1, Psi(sqrt(n/T))>=1/2 throughout the patch for large T. Also n^(-3/4) is comparable to N^(-3/4). Every weighted cosine summand has the same negative sign, giving the claimed absolute lower bound c3hN^(-3/4).

Lastly, write h comparable to N^eta with eta=5/6-1/(3sigma)>0. For any fixed epsilon<eta/2,

    h/[h^(1/2)N^epsilon] -> infinity.

This refutes precisely the stated uniform uncentered local square-root input. The proof permits the center and R to depend on T. It does not claim that the center belongs to a prescribed partition, that other patches are coherent, or that the complement cannot cancel this patch. The conductor's scoped exclusions are necessary and correct.

## 4. First doubtful or unproved step

There is no identified gap in the explicitly defined Type-I main supremum, its coefficient-uniform moment consequence, or the narrowly scoped resonance control.

A patchwise triangle inequality followed by multiplication by the number of patches would fail to prove the candidate main exponent. The valid proof instead uses the ordered-cutoff and whole-shell variation structure in Section 3.1 before estimating.

The first unproved downstream step is any assertion that the residual r2-rsharp has a comparably paid ceiling or moment. Theorem 1.1(iii)/Proposition A.3 does not by its statement supply the required completed square-root residual bound. This review neither estimates that residual nor asserts that the main moment improves the complete actual M12(B_T).

For the resonance control, the first unproved extension would be passing from a single patch's coherent lower bound to the full wave or an integrated lower bound without controlling the complement and the measure/overlap of resonant radii. None is claimed here.

## 5. Controls and outcomes

Analytical controls, all passed:

1. **Cutoff reversal and equality:** r<=d<r^2 is exactly d^10<x<=d^20; d<r is exactly d^20<x. Each is an interval condition in the ordered start x.
2. **Many tiny patches:** the total variation proof telescopes through monotone log x and is independent of the number of patches. It continues to work if some supports have only one integer.
3. **Quotient character:** chi4(n/d) becomes chi4(m), with residues 1 and 3 retained separately; no multiplicative-character substitution is made.
4. **Source phase:** the unsplit derivative is an exact s=1/2 monomial, and the mod-4 versions are fixed translates with relative derivative perturbations O_j(1/M). Ambient length is below the phase-size parameter.
5. **Energy and fixedness:** the piecewise vector is divisor bounded and independent of R; all cutoffs are zero-extended into the ambient dyadic blocks.
6. **Tail:** increasing a fixed Schwartz seminorm order makes the actual remaining infinite tail smaller than any prescribed T power.
7. **Resonance:** integer constant, linear and quadratic phases; growing h; real-radius availability; negative physical cosine sign; and actual nonnegative r2 mass all hold simultaneously.
8. **Scope adversary:** no estimate for one fixed piece is substituted for the complete wave, and no bound for the main is substituted for the residual.

One bounded computation checked rational exponent arithmetic and a high-precision Taylor control. It is diagnostic_only. Python standard-library Fraction calculations were exact; Decimal precision was 70 digits; the final cosine sign diagnostic used binary64 on the already small residual, not on the original large phase.

Command: the following source was passed to python - on standard input in PowerShell.

~~~python
from fractions import Fraction as F
from decimal import Decimal, getcontext
import math
kappa=F(13,84)
shell=kappa/2+F(1,2)-F(3,4)+F(1,20)
delta=kappa+F(52,125)*shell
moment=1+(12-F(136,13))*delta
print('shell exponent =', shell)
print('supremum exponent =', delta, '=', F(13,125)-F(13,52500))
print('moment exponent =', moment, '=', F(29,25)-F(1,2625))
print('secondary W^10 exponent =', 10*delta, '<', moment)
print('minimum H4 log_N exponent =', F(9,10)-F(25,52))
getcontext().prec=70
m=10**6
R=Decimal(8)*Decimal(m)**Decimal('1.5')
errs=[]
for j in range(-10,11):
    E=R*Decimal(m+j).sqrt()-Decimal(8*m*m+4*m*j-j*j)
    errs.append(E)
assert max(abs(v) for v in errs)<Decimal(1)/24
assert max(math.cos(-3*math.pi/4+2*math.pi*float(v)) for v in errs)<-0.5
print('resonance diagnostic m=1000000,k=1,h=10: PASS')
print('max_abs_Taylor_residual =',max(abs(v) for v in errs))
~~~

Observed output:

~~~text
shell exponent = -103/840
supremum exponent = 5447/52500 = 5447/52500
moment exponent = 3044/2625 = 3044/2625
secondary W^10 exponent = 5447/5250 < 3044/2625
minimum H4 log_N exponent = 109/260
resonance diagnostic m=1000000,k=1,h=10: PASS
max_abs_Taylor_residual = 0.000500003125021875164063789072973720093515326231440340538
~~~

No numerical claim substitutes for any asymptotic proof. The resonance diagnostic tests phase arithmetic at one parameter choice; it does not test the mass-pigeonhole claim, which was proved analytically. More than 80 percent of this assignment was analytical/source-hypothesis reasoning; computation was limited to this one bounded check.

## 6. Exact dependencies and artifacts

Local contexts actually read:

- protocol.md, already read for the preceding isolated task and retained as protocol context.
- strategy/round231_quadratic_signed_admission/briefs/type_i_main_review.md.
- strategy/round231_quadratic_signed_admission/briefs/complete_interface.md.
- proofs/kernels/gc_complete_square_root_large_values_moment_bound.md.
- strategy/round231_quadratic_signed_admission/conductor_resonant_patch_control.md.

An initial read at strategy/round231_quadratic_signed_admission/complete_interface.md returned file-not-found; the correctly named briefs/complete_interface.md was then read. No content was obtained from the nonexistent path.

Primary sources inspected:

- Bourgain, arXiv:1408.5794v2, Section 5, Theorem 6 and proper-interval/phase-class discussion after (5.1), https://arxiv.org/html/1408.5794v2#S6. This is the primary source identified by the accepted kernel and required by the assigned exponent-pair seam.
- Matomaki, Shao, Tao, and Teravainen, arXiv:2204.03754v4, Theorem 1.1(iii), Appendix A.3 and Proposition A.3, https://arxiv.org/html/2204.03754v4.

Other mathematical inputs: elementary divisor bounds, finite summation by parts for bounded-variation weights, geometric dyadic summation, layer cake, the elementary lattice disk/unit-square estimate, Taylor's theorem, and continuity of the fixed mollifier transform.

The Type-I derivation was independent of the conductor and sibling reports. The resonance claim was reviewed directly as the explicitly assigned nonauthor seam. The graph, validation matrix, historical rounds, and sibling reports were not read.

Sole newly written artifact:

    strategy/round231_quadratic_signed_admission/reviews/type_i_main_and_resonance_review.md

## 7. Scoped state recommendation

Retain or promote, subject to the conductor's required graph validation and remaining admission gates, the exact complete Type-I main supremum and its main-only moment consequence. The proof genuinely avoids the patch-count loss by using divisor-wise whole-shell intervals and bounded variation.

Retain the conductor's resonance control as a rigorous scoped obstruction to the stated uncentered local square-root input. Do not promote it as a complete-wave or complete-moment lower bound.

No shared state is changed by this report. The residual remains unpaid here; this review supplies no complete-moment improvement and no authorization to infer one. No successor round or additional assignment is proposed.
