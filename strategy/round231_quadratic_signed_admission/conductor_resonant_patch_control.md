# Conductor control: actual resonant quadratic patches

Round231 prelaunch evidence, 2026-10-11. Conductor independent derivation. Graph SHA256 a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b. Not an accepted graph lemma or a complete moment lower bound.

## 1. Result

Keeping quadratic curvature removes the earlier singleton obstruction at N~T^(2/3). However, even the actual moving Taylor phases have large resonant patches. A uniform square-root bound for every such uncentered arithmetic patch is false. The possible useful input must retain a main term or control resonant patches and their dependence on R in an averaged or joint signed estimate.

## 2. Exact statement and hypotheses

Fix 2/5<sigma<2/3. For each sufficiently large real T, let N=T^sigma and h=floor(c N^(5/6)T^(-1/3)), with a sufficiently small absolute constant c>0. Then h tends to infinity. There exist an integer m in [6N/5,9N/5] and an integer k>=1 such that R=8k m^(3/2) belongs to [T/2,2T], and

    sum_(|n-m|<=h) r2(n) >= c1 h,
    Re sum_(|n-m|<=h) r2(n)e(R sqrt(n)) >= c2 h.

Moreover, for the fixed mollifier in complete_interface.md and sufficiently large T,

    |sum_(|n-m|<=h) r2(n)n^(-3/4)Psi(sqrt(n/T))
                      cos(2pi R sqrt(n)-3pi/4)| >= c3 h N^(-3/4).

The constants depend on sigma and the fixed mollifier. This shows that a uniform bound O(h^(1/2)N^epsilon), for every epsilon>0 and every actual moving patch, is false. It does not say that all patches are large at one R, that a fixed preassigned partition always contains this center, or that the complete B_T moment is large.

## 3. Proof

The elementary lattice disk estimate A(x)=sum_(n<=x)r2(n)=pi x+O(sqrt(x)+1) gives mass at least cN in the interior shell [13N/10,17N/10]. Sum S_m=sum_(|n-m|<=h)r2(n) over integers m in [6N/5,9N/5]. Since h=o(N), every integer in that interior shell appears in exactly 2h+1 of these sums for large T. Thus sum_m S_m >= cNh, while there are O(N) centers. Some integer m has S_m>=c1 h.

Choose k to be the nearest integer to T/(8m^(3/2)). Since sigma<2/3, that quotient tends to infinity. Consequently k>=1 and |8k m^(3/2)-T|<=4m^(3/2)=o(T), proving the radius claim.

For integer j with |j|<=h, Taylor's theorem gives

    R sqrt(m+j)=8k m^2+4kmj-kj^2+E_j,
    |E_j|<=C T N^(-5/2)h^3<=C c^3.

The first three displayed terms are integers. Choose c such that |2pi E_j|<=pi/12. Then Re e(R sqrt(m+j))>=cos(pi/12), proving the complex estimate using r2>=0. Also cos(-3pi/4+2pi E_j)<=-1/2, so all terms have the same real negative sign in the physical circle phase. Since N/T tends to zero, continuity and Psi(0)=1 imply Psi(sqrt(n/T))>=1/2 throughout the patch, and n^(-3/4) is comparable to N^(-3/4). This proves the real weighted claim.

Write h~N^eta, where eta=5/6-1/(3sigma)>0. For epsilon<eta/2, h/(h^(1/2)N^epsilon) tends to infinity. Hence the proposed uniform square-root bound fails. This is a proof using actual r2, with the radius allowed to vary over its required full real window.

## 4. First doubtful or unproved step

None in the scoped resonant-patch statement. A useful estimate for the total contribution of such patches to M12 is not derived. In particular, summing their moduli, ignoring overlap among exceptional radii, or projecting this lower bound onto the full wave is unjustified.

## 5. Required controls and outcome

Check integer linear and quadratic coefficients, the physical -3pi/4 sign, real-radius availability and h growth separately. The proof does so exactly. A finite diagnostic may use m=10^6, k=1, T=8*10^9 and h=10; arbitrary-precision evaluation of the Taylor residual must agree with the cubic bound and exhibit the same negative real phase. Finite testing is diagnostic only. The full complement is deliberately absent from the claimed lower bound; no complete-moment inference is made.

## 6. Dependencies and exact artifacts

protocol.md; strategy/round231_quadratic_signed_admission/briefs/complete_interface.md; elementary disk-area/unit-square count; Taylor theorem; nonnegativity of actual r2; Psi continuity at zero. No sibling derivation or numerical premise is used.

## 7. Recommended state effect

Retain as scoped admission control after nonauthor review; reject only the stated uniform local square-root input. No graph mutation, no rejection of joint signed polynomial analysis, and no analytic admission from this control alone.
