# Complete payment of the polynomial-uniformity approximant

Round231 prelaunch candidate, conductor, 2026-10-11. Graph SHA256 a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b. Evidence only; nonauthor review required. This is a component estimate, not a new complete moment for actual B_T.

## 1. Result

The piecewise Type-I approximant in the polynomial-uniformity source can be summed across patches before estimation. Its complete upper-tail wave has supremum at most T^(13/125-13/52500+epsilon) and twelfth moment at most T^(29/25-1/2625+epsilon). Thus this explicit main fits within the preferred moment budget. The unknown remaining signed remainder is still essential.

## 2. Exact statement

Use the exact functions and conventions of briefs/complete_interface.md. Set X0=T^(52/125). Cover (X0,T^(3/2)] by consecutive shells of size comparable to their left scale N. Partial shells at either end are retained. Within each shell partition into intervals (x_j,x_(j+1)] of lengths comparable to H4=N^(9/10)T^(-1/5), with starts independent of R. Adjust equal patch lengths where possible. If an entire boundary fragment is shorter than H4, keep that fragment and use a nominal source interval of length comparable to H4 at its same left endpoint; the source's maximal prefix estimate then pays the fragment at the nominal length. This adds at most one charge per endpoint and leaves the approximant base unchanged. On a patch put Z_j=x_j^(1/20) and

    c_T(n)=4 sum_(Z_j<=d<Z_j²,d|n)chi4(d)(log n-log Z_j²)/log Z_j
          +4 sum_(d<Z_j,d|n)(chi4(d)+chi4(n/d)).

The displayed construction is for T>=T0, where T0 is a fixed sufficiently large constant for the source's strict length margins. Define c_T(n)=0 outside these shells, and define c_T(n)=0 everywhere for 2<=T<T0. This explicit bounded-parameter convention avoids any logarithm at a patch start1; all complete estimates on that compact T range follow by enlarging constants. Let S_T(R) be the real circle-phase wave with coefficients c_T(n)n^(-3/4)Psi(sqrt(n/T)). Its complex analogue obeys the same supremum estimate. There is no positivity hypothesis on c_T. It is a fixed, R-independent, divisor-bounded vector. The omitted actual tail n>T^(3/2) is O_A(T^-A) uniformly; alternatively the approximant could be extended with divisor bounds, with the same tail conclusion.

## 3. Derivation

The formula is the explicit approximant in Matomaki--Shao--Tao--Teravainen, Higher uniformity I, arXiv2204.03754v4, AppendixA.3. Only this formula is needed for the present component proof. The polynomial-correlation theorem controls a different owner, r2-c_T. Source: https://arxiv.org/html/2204.03754v4#A1.SS3 .

For each fixed d, the condition d<Z_j is monotone in patch index, while Z_j<=d<Z_j² holds on one interval of patch indices: d^10<x_j<=d^20, with endpoint conventions inherited exactly. Thus the support of each type of d-fibre is a single real interval in n, intersected with d|n. The logarithmic factor

    L_j(n)=20 log n/log x_j-2

is O(1). On open patches its total derivative integral over one shell is O(1/log N). At consecutive patch boundaries its jump has magnitude at most C(log x_(j+1)-log x_j)/log N, so the sum of jumps is also O(1/log N). The at most two support jumps for a given d cost O(1). Multiplication by the smooth amplitude contributes O_L(N^(-3/4)(1+N/T)^(-L)) to amplitude plus variation. There is consequently no factor equal to the number of patches.

The accepted Bourgain exponent-pair interface (k,l)=(13/84+epsilon,55/84+epsilon), including proper intervals and its existing source qualifications, applied to m~N/d and phase R sqrt(d m), gives

    |sum_m e(R sqrt(d m))|
       << T^epsilon [T^(13/84) N^(97/168) d^(-1/2)
                     + N^(1/2)/(T d)].

The harmless reciprocal-frequency term is recorded conservatively. The normalized phase is the exact square root; phase parameter R sqrt(N), length N/d. The required high-frequency regime holds uniformly for N<=T^(3/2), d>=1, large T. For chi4(m), separate the residue classes modulo4 and apply the same interval estimate after an affine change of variable; the square-root derivative pattern on a compact positive interval is unchanged. Equivalently treat each residue interval directly. The accepted proper-interval extension covers the fibre endpoints. Epsilon losses absorb logarithms and fixed affine constants.

Only d< (2N)^(1/10) occurs. Summing d^(-1/2) costs O(N^(1/20)), while sum1/d costs a logarithm. Abel summation using the proved variation bound therefore gives, for each shell,

    sup_R |S_N(R)|
      <<_L T^epsilon (1+N/T)^(-L)
                    [T^(13/84) N^(-103/840)+T^(-1)N^(-1/4)].

The first exponent is 97/168-3/4+1/20=-103/840. Since it is negative, summing shells from X0 upward gives

    sup_R |S_T(R)| << T^(gamma_s+epsilon),
    gamma_s=13/84-(103/840)(52/125)
           =13/125-13/52500=27235/262500.

Small bounded T can be absorbed into the constant. Schwartz decay and the divisor bound pay every tail and give absolute convergence. No sign of Psi is assumed in the estimate.

The coefficients satisfy |c_T(n)|<=C tau(n), because L_j is uniformly bounded. The accepted finite correlation/Gram proof therefore gives the same generic distribution for S_T,

    D_S(V)<<T^epsilon(V^-2+T V^(-136/13)), V>=1.

Here the vector is fixed as R varies; no actual-circle supremum is transferred to an arbitrary mask. Combining this distribution with the newly proved component supremum gives

    M12(S_T)<<T^epsilon[T+T^(10gamma_s)+T^(1+20gamma_s/13)]
            <<T^(29/25-1/2625+epsilon).

The final term is the largest. Epsilon parameters in the source, divisor bound, dyadic summation and distribution are chosen as sufficiently small fixed multiples of the requested output epsilon.

## 4. First missing step

The exact remaining wave has coefficients r2-c_T on n>X0, plus the full negligible far tail. The source supplies some uniform power saving for its polynomial correlations, but no quantified saving sufficient for the complete target is certified. Its twelfth moment is not proved at29/25 here. Adding the paid norm head, this remainder and S_T preserves every mixed term through the L12 triangle inequality; no piece can be discarded.

## 5. Controls

Patch cutoffs and logarithmic jumps were retained before any modulus. Independent review must specifically test their bounded variation, the character residue classes, phase-source applicability and the small positive exponent margin. Exact rational checks are archived in controls/finite_controls.json and may be extended with the final main exponents. A source length failure for quadratic patches is not used to reject quartic patches.

## 6. Dependencies

protocol.md; the two accepted complete kernels named in complete_interface.md; primary arXiv2204.03754v4 AppendixA.3 for the approximant formula (not its power-saving theorem for this proof); the conductor's independent fibre regrouping and exponent arithmetic. Statement-only candidate supplied independently to the nonauthor reviewer before this derivation was available to them.

## 7. Recommended state effect

Retain as reviewed component evidence if its seam review passes. No complete bound or pointwise improvement, no automatic analytic admission, and no graph promotion without a separate valid State Patch. The main's payment identifies the residual as the specific owner requiring a stronger signed estimate.
