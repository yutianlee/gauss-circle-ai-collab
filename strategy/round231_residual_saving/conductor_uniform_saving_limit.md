# Conductor quantitative limit for the unchanged approximant

Round231 residual-saving admission, 2026-10-11. Conductor independent derivation; graph a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b. This is a limit on an all-polynomial estimate for the specified residual, not on the physical circle moment.

## 1. Result

The obstruction is stronger than an unspecified constant. For the displayed approximant, a uniform bound H x^(-kappa) over all constant phases cannot hold with kappa>1/20. In the source's parametrization kappa=c_(2,d,1) epsilon0, if the same c works for every permitted epsilon0, it necessarily satisfies c<=3/20. Consequently optimizing or extracting this unchanged uniform constant cannot cross the complete-ceiling gate1/4-beta.

## 2. Exact statement

Use rsharp_x and v_x from briefs/residual_interface.md. Let z run through positive integers1 modulo4, x=z^20, and take H=x^(2/3). Then

    sum_(x<n<=x+H) v_x(n) = -34 H/z + O(H/z²+sqrt(x)+H²/x+z²).

All error terms are o(H/z). Real endpoints are literal. Thus a bound with exponent kappa>1/20 fails on this sequence. The choice H=x^(2/3) lies within the source window for every fixed0<epsilon0<=1/3 (with equality at epsilon0=1/3). If one prefers strict endpoint margins, use epsilon0<1/3 and pass to its supremum in the resulting constant restriction.

## 3. Proof

Write A(z)=sum_(d>=z)chi4(d)/d. For z=1 mod4,

    A(z)=sum_(j>=0)(-1)^j/(z+2j)
        =integral_0^1 t^(z-1)/(1+t²) dt
        =1/(2z)+O(1/z²).

The integral follows first with finite geometric sums and then dominated convergence (or an Abel limit). In fact0<=A(z)-1/(2z)<=1/[z(z+1)], because0<=1/(1+t²)-1/2<=1-t on[0,1]. Also sum_(d<z)chi4(d)/d=pi/4-A(z), and the middle range sum is A(z)-A(z²). The latter endpoint also has z²=1 mod4.

Throughout the interval, the logarithmic multiplier is

    (log n-2log z)/log z =18+O(H/(x log z)).

The first small-divisor term sums to4H[pi/4-A(z)]+O(z), using the exact count H/d+O(1). The quotient-character small-divisor term sums to O(z), since chi4 partial sums are bounded. The constant18 part of the middle divisor sum is72H[A(z)-A(z²)]+O(z²). Its variable part is O(H²/x+z²): bound the multiplier perturbation by O(H/(x log z)), sum the absolute divisor incidences by O(H log z+z²), and use H<=x.

The actual coefficient sum is pi H+O(sqrt(x)+1), by subtracting two disk counts. Therefore

    sum v_x =4H[-17A(z)+18A(z²)]
              +O(sqrt(x)+H²/x+z²)
            =-34H/z+O(H/z²+sqrt(x)+H²/x+z²).

For H=x^(2/3), the leading exponent is37/60, while the error exponents are at most17/30,1/2,1/3,1/10. This proves the nonzero asymptotic. If the source estimate held with fixed c epsilon0>1/20, it would contradict that asymptotic. Since the theorem's c is independent of epsilon0, letting epsilon0 increase to1/3 yields c<=3/20. This is an upper restriction on any valid uniform exponent, not a lower bound for the saving actually available from the source proof.

## 4. First unproved step

None in the displayed uniform-saving obstruction. The phases of actual quartic Taylor approximations to R sqrt(n) need not include this zero-phase example. No physical lower bound or impossibility of a phase-specific improvement follows. Subtracting further arithmetic means changes the residual and requires separately paying those corrections.

## 5. Controls

The endpoints d<z and z<=d<z² matter: z=1 mod4 ensures the omitted first term has positive character, fixing the sign -34. The quotient-character term is not assigned a false nonzero average. Source epsilon and output epsilon are distinguished; no numerical source constant is invented. The independent statement-only report gives a stronger scalar-centering control using a fixed linear phase; its proof is separately reviewed.

## 6. Dependencies

protocol.md; briefs/residual_interface.md; exact source formula arXiv2204.03754v4 AppendixA.3 and Theorem1.1(iii) for the parameter-independence claim; elementary disk count and chi4 partial sums. This calculation was derived before reading the isolated analyst's report; the analyst independently communicated the same leading asymptotic on a different legal interval length.

## 7. Recommended effect

Retain after nonauthor review as a quantitative obstruction for the unchanged universal residual theorem. Shift effort to actual physical phases or stronger signed moment arguments. No graph mutation or complete-bound claim.
