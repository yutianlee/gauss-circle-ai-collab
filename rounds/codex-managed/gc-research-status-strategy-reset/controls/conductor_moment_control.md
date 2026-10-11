# Round230 conductor control, frozen before receipt of blind report

Date: 2026-10-11. Conductor NONBLIND. Starting graph SHA256 a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b. Context: protocol, graph's accepted complete moment node, checkpoint229 and the isolated statement. No blind report read.

## 1. Result

The existing moment curve cannot improve the input pointwise exponent by elementary persistence. A complete twelfth-wave moment exponent below 13 beta - 1/2 would improve it; 29/25 is a concrete stronger target. A family of fixed orders is necessary for the stated moment route to quarter.

## 2. Hypotheses

N is nondecreasing, P(x)=N(x)-c x, c>0, |P(x)|=o(x), and moments are over [Y/2,3Y]. Constants may depend on the fixed p and epsilon. The wave-to-physical relation holds uniformly on R comparable to sqrt(Y), with error O(T^(1/2+epsilon)). The nonnegative moment window must cover those radii. No p(Y) is permitted.

## 3. Proof

Put M=|P(x0)| for Y<=x0<=2Y. If P(x0)>=0, monotonicity gives P(x0+s)>=M-cs for 0<=s<=M/(2c). If P(x0)<0, P(x0-s)<=-M+cs on that interval. Since M=o(Y), the respective interval lies in [Y/2,3Y] for large Y. Thus the p-moment is at least M^(p+1)/(2^(p+1)c), including values at jumps. A physical exponent a_p gives |P|<<Y^(a_p/(p+1)+epsilon), after choosing input epsilon for this fixed p.

For wave moment T^b, the factor sqrt(R)^p and Jacobian dx=2R dR give physical moment T^(b+1+p/2). The smoothing contribution is T^(2+p/2). Thus the restored exponent is

    theta_p = 1/4 + (max(b,1)+1/2)/(2(p+1)).

The max is essential for a hypothetical b<1; all tested b>=1. A sufficient fixed-order family has b_p=o(p), with p chosen depending on desired epsilon and then held fixed as Y tends to infinity. A uniform bound b_p<=5/4 yields 1/4+7/(8(p+1)). This does not prove the required family.

For b_p=max(1,(p-2)beta), beta=2theta-1/2 and theta<1/3, the second branch of the physical exponent is theta+(1-3theta)/(p+1)>theta. Hence the full maximum is strictly worse for each finite p and tends to theta as p increases. Choosing a fixed p for epsilon recovers the input theorem but improves no exponent.

For p=12, a sufficient strict improvement needs b_12<13beta-1/2=1.1765625753..., whereas the accepted bound has b_12=10beta=1.2896635195.... The candidate29/25 yields102/325=0.3138461538..., smaller than theta=0.3144831759..., but is not quarter. At the critical spectral shell N=T, an entire raw bound A^2N^(3/2)T^(2gamma) improves the real benchmark through the complex route only when gamma<beta. Relative to A^2T^2, this needs a raw saving delta>1/2-2beta=0.2420672961..., and quarter needs delta=1/2. A small arbitrary saving in an inferior norm certificate is insufficient.

## 4. First gap

No improved moment or cusp bound is proved by these implications. The exact actual arithmetic signed estimate remains missing. The declared power thresholds concern complete bounds, not one shell or a component.

## 5. Controls

Monotonicity covers both signs and integer jumps. Error maximum, Jacobian, fixed-p quantifiers and all-scale complex restoration are retained. Wolfram supplies exact symbolic identities and decimal diagnostics, independently reproduced by Fraction and Decimal in local_exponent_check.py. Neither computation proves an asymptotic theorem.

## 6. Dependencies

Only named starting contexts and the monotonicity argument above. Wolfram query/response archived in wolfram_symbolic_check.json; local results separately recorded. No source theorem imported by this control.

## 7. State effect

Retain as conductor evidence pending independent comparison/review. No graph or draft mutation, no accepted exponent change, no successor launched.
