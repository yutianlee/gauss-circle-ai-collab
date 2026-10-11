# Conductor nonauthor review of the isolated quadratic rows

Round231 prelaunch, 2026-10-11. Reviewer: conductor. Claimant report SHA256 dcf93c50bbc93f8592038c0d1c15e0cddf9ccfe12613be042bfb864908faca6b. Starting graph a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.

## 1. Result

PASS for the exact finite identities, common-component obstruction and stated limitations. This is not an incomplete-sum or complete-moment estimate.

## 2. Exact statement reviewed

All odd primes, all a,b,c in the field including zero, both congruence classes, the stated exponential sign, raw centered transforms W, both common/residual decompositions, their Gram matrices and ranks. The report's natural split is nonorthogonal; its row-average split is orthogonal. Neither deletes a free term from the original expression.

## 3. Independent derivation and line audit

Writing chi=chi_p(-1), the elementary norm count gives L(n)=1-chi/p+chi 1_(n=0). Thus f(n)=chi(1_(n=0)-1/p). If G(a,b)=sum_n e_p(an²+bn), direct substitution yields W=chi/p-chi G/p². Independently summing the Gram in b forces equal n and produces

    sum_b W_(a,b) conjugate(W_(c,b))
       =1/p-2/p²+G(a-c,0)/p³.

This agrees with the report's normalized A=G/p expression, including a=c. The common row mean is chi(p-1)/p², not chi/p; retaining that distinction verifies the orthogonal energy fraction (p-1)/p. Orthogonality in a shows its residual column sum is also zero. Fourier diagonalization in the a variable counts n²=t and gives precisely the reported rank (p-1)/2 for the orthogonal residual.

The report proves the Gauss sign via the normalized Fourier matrix determinant. I checked the Vandermonde phase: sum_(j<k)(j+k)=p(p-1)²/2, so its exponential contribution is1 for odd p. The remaining phase i^(p(p-1)/2), the reflection eigenspace dimensions and the two trace possibilities select +sqrt(p) for p=1 mod4 and +i sqrt(p) for p=3 mod4. Completing the square has the negative b²/(4a) phase. The Hermitian Gram orientation agrees with conjugation under a-c -> c-a.

All-ones weights give sum_(a,b)W=chi(p-1), while the orthogonal residual sum is zero. This is an exact falsifier of silently deleting the common term, and does not imply anything about unknown physical downstream weights.

## 4. First unproved step

None found in the finite claim. A bridge from the decorrelated residual matrix to actual incomplete norm sums, with the deleted common owner restored, remains unproved and is explicitly outside the report.

## 5. Controls

Conductor independently reproduced 3354 transforms and 3354 Gram entries over ten odd primes3 through31 using direct integer residue enumeration and separate complex finite sums. Maximum absolute numerical error was below10^(-15), tolerance10^(-10). Row-mean energy fractions and zero cases also pass. See controls/reproduce_finite_controls.py and controls/finite_controls.json. These diagnostics do not certify the arbitrary-prime theorem; the algebra does.

## 6. Dependencies

protocol.md; briefs/blind_quadratic_statement.md; reports/blind_quadratic_rows.md; conductor independent finite calculations archived in controls/. The isolated claimant had no conductor derivation or research history. Review checked the final report only after the claimant had frozen it.

## 7. Recommended effect

Retain finite lemma and scoped raw-row no-go as reviewed admission evidence. No graph change, no complete estimate, and no general rejection of signed polynomial methods.
