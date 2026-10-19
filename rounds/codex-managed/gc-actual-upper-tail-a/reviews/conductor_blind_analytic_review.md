# Round231 nonauthor review of the isolated odd-kernel result

Campaign `gc-actual-upper-tail-a`; round231; conductor as nonauthor analytic reviewer; generated2026-10-11 UTC. Graph hash `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. Claimant report SHA256 `b4333428aee065f580ee3adae0a4b6a6ef952c9be115eb8638fa926f130de810`.

## 1. Result

PASS at the report's explicitly generic analytic scope. The exact covariance, boundary and discrepancy formulas are correct. They refute a universal gain from kernel oddness, and supply valid conditional norm interfaces. They do not refute target A for the actual arithmetic family.

## 2. Exact statement and hypotheses

The reviewed statement is the finite real atomic measure convolved with one real odd nonzero Schwartz kernel at scale L>0, with arbitrary repeated real centers. Finite intervals and slowly varying tests obey the precise differentiability hypotheses in the claimant. No arithmetic or independence assumption is present. The initial report was frozen before its author received any actual-interface or conductor-report context for a separate review task.

## 3. Independent derivation and seam checks

For S=K_L*mu with K_L(t)=K(t/L), the Fourier transform is L Khat(L xi) muhat(xi). Squaring and changing variable eta=L xi gives L integral |Khat(eta)|^2 |muhat(eta/L)|^2 d eta. This verifies both forms of the energy, including the single factor L in the pairwise covariance sum. The covariance satisfies2(C(0)-C(h))=||K(.-h)-K||_2^2. Its second derivative at zero is -||K'||_2^2; the fourth derivative is a translate pairing of K'', bounded by ||K''||_2^2. The claimed h^4/24 Taylor remainder and positivity near zero follow.

The primitive P has derivative K, is even and Schwartz because K is odd and has zero integral. Consequently S=L Q' for Q=sum a_jP((t-v_j)/L). This proves both finite-boundary terms in(2.8); the endpoint estimate uses |P(x)|<=tau(|x|). A constant test with a center at an endpoint gives a nonzero boundary term, exactly as the Gaussian control states. The whole-line small-frequency bound integrates xi^2 over[-1/H,1/H], verifying8pi^2/3 and H^-3. It has no implication for the omitted frequency range.

For the left-minus-right signed local count D_t(r), each atom contributes its sign times a jump at |t-v|. Integration by parts in r gives S(t)=-integral_0^infinity K'(u)D_t(Lu)du, with no boundary term since K(0)=K(infinity)=0. Its Fourier multiplier is -i(1-cos(2pi r xi))/(pi xi), confirming the squared multiplier and its zero limit at xi=0. Minkowski and weighted Cauchy-Schwarz give the stated inequalities without a missing L.

For the cumulative measure F, integration by parts gives S=(L^-1 K'(./L))*F. The convolution multiplier is2pi i eta Khat(eta), eta=L xi, so its norm is independent of L. The L1-to-L2 convolution norm is L^-1/2||K'||_2. A nonzero mass makes F fail to decay at one end; subtracting M delta_c supplies precisely the retained M K((t-c)/L). The density argument for the optimal multiplier constant is valid for finite signed atomic measures with zero total mass. That optimality is over this generic class, not any arithmetic subclass.

## 4. First doubtful or unproved step

No repair is needed for the isolated statements. An actual application would need estimates for the signed measure with its varying amplitudes, all scales and exceptional-set restriction. In particular, multiplying by the indicator of {|F_actual|>T^gamma} loses the slow-test premise. The whole-line energy identity does not pay this new weighted integral. No such arithmetic estimate is supplied by the report.

## 5. Required controls and outcome

Analytically rechecked: same-sign coincident cloud, near-coincident cloud using the translation inequality, opposite near-pair, far opposite pair, one atom at an interval endpoint, and nonzero cumulative mass. All agree with the formulas. The Gaussian covariance C(h)=sqrt(pi)/(4sqrt(2)) (1-h^2)exp(-h^2/2) follows by centering the quadratic exponential and confirms positive near covariance. No numerical test or asymptotic extrapolation is used in this review.

## 6. Dependencies and exact artifacts

Reviewed `reports/blind_odd_kernel_covariance.md` at the hash above, its isolated statement and `protocol.md`. The conductor also knows the frozen actual interface from its own role; it was not supplied to the blind author before the initial freeze. General calculus, Fourier Plancherel and elementary inequalities suffice; no external theorem application is newly claimed.

## 7. Recommended state effect

Retain as independently rederived and nonauthor-reviewed control evidence. No parent promotion, actual arithmetic lower bound, pointwise improvement or graph change follows. Any use of the report must preserve its generic scope and the exceptional-set caveat.
