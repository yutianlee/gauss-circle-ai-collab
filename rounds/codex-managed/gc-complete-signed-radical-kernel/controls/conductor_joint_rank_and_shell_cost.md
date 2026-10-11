# Round218 common-radius rank and actual shell-certificate cost

## 1. Result

Conductor analytical control, NONBLIND, 2026-09-28.
Campaign:gc-complete-signed-radical-kernel; starting graph
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
The common radius adds exactly two Hessian directions to the angular
rank. For p factors the rank is p+2 in dimension2p+1, leaving p-1
radial tangent directions. At p=12 this is rank14 and nullity11.
The full cosine signs do not make every resulting packet vanish.

The explicit positive certificate obtained by taking moduli of the
leading dual radial packets has, for fixed even p>=2 and one smooth
block N=T^a with fixed0<a<1, size

    T^(1+p/2) N^(-p/2)

up to upper epsilon factors. The upper envelope extends to the whole
range1<<N<=T^(3/2) with its Schwartz block factors. This is an actual dual-lattice certificate,
not a lower bound on the original signed moment. It quantifies why
the dimension increase alone gives no complete moment improvement.
All asymptotic stationary expansions invoked below require the separate
joint-radial seam review before being used as accepted evidence.

## 2. Exact setup and claim scope

Use p fixed, positive real scales L_j=sqrt(N_j), real R>0, dual
vectors k_j in R^2, and polar y_j=r_j omega_j with1<r_j<2.
The physical phase after scaling Gaussian lattice variables is

    Phi(R,r,theta)=sum_j L_j r_j
                        [sigma_j R-|k_j|cos(theta_j)],

where angles are relative to k_j and sigma_j is+1 or-1. The actual
Poisson frequency vectors lie in Z^2, but the local rank calculation
does not require that restriction. Smooth amplitude support is compact
inside the annuli and a positive R/T interval.

For the certificate claim use equal N and fix a nonzero nonnegative
smooth chi supported inside(1,2) in the radius variable. Choose the
norm block small enough, when necessary, that the actual mollifier is
positive. Equivalently the following claim may use a fixed smooth
radial block of the actual series, whose limiting profile is positive
on its support. At N=T^a with any fixed a<1, Psi(sqrt(N/T)r)
tends with all derivatives to1, uniformly on that support.
The lower-bound claim below is used only in this latter range,
including the critical N=T^(2/3); the upper envelope holds throughout
the stated full truncated range with Schwartz block factors.

## 3. Derivation

At a stationary point, each theta_j is0 or pi. Radial stationarity
forces |k_j|=R and cos(theta_j)=sigma_j. Radius stationarity is

    sum_j sigma_j L_j r_j=0.

All-positive or all-negative signs give no such point. Mixed signs
give a point only when this hyperplane meets the radial support;
for balanced signs and equal scales it meets its interior.

The angular Hessian is diagonal with nonzero entries
sigma_j L_j r_j R, hence rank p. Angular cross terms vanish at the
critical angles. On the R and p radial variables, the Hessian is

    [ 0   v^t ]
    [ v    0  ],       v_j=sigma_j L_j,

whose rank is2 and whose nonzero eigenvalues are+|v| and-|v|.
Thus the complete Hessian has rank p+2. Its tangent kernel consists
of radial changes dr with sum_j sigma_j L_j dr_j=0, dR=0 and all
dtheta=0. It has dimension p-1. No stationary direction has been
lost by using polar coordinates, whose Jacobian is nonsingular here.

The angular signature is sum sigma_j, while the R/radial pair has
signature0. Combining the angular phase with the original cosine
factor e(-3 sum sigma_j/8) gives e(-sum sigma_j/4).
For one factor this is the odd sine dual packet, not an everywhere
positive bump. Its leading profile, up to a fixed nonzero real
normalization, is

    T^(-1/2) S(sqrt(N)(R-|k|)),
    S(u)=integral chi(r) r^(-1) sin(2pi u r) dr,

with harmless fixed smooth positive radial factors depending on the
chosen norm-block convention. The exact power r^(-1) comes from
r dr, the original r^(-3/2) weight and angular r^(-1/2).
The profile is odd, Schwartz and nonzero: S'(0)=2pi integral chi>0.
At the center it vanishes. With an even p, however,
integral S(u)^p du>0. Therefore a single common-radius packet's
full-sign pth integral has nonzero leading size T^(-p/2)N^(-1/2).
This rules out claiming an automatic cancellation of every stationary
manifold just from the cosine phases. It is not a lower bound for the
sum over different dual radii.

For a literal positive leading-packet certificate on a fixed interior
radius interval J of length comparable to T, put

    G_N(R)=T^(-1/2) sum_(k in Z^2, |k| in J')
                         |S(sqrt(N)(R-|k|))|,

where J' is a shorter concentric interval with a fixed T-sized margin.
Both J and J' lie in a region with w(R/T)=1. The elementary lattice
annulus count gives #k with |k| in J' comparable to T^2. Each of these
packets has integral over J at least c T^(-1/2)N^(-1/2), for large T,
by nonzero S and the margin. Hence

    integral_J G_N >= c T^(3/2)N^(-1/2),
    integral_J G_N^p >= c T^(1+p/2)N^(-p/2)

by Holder. These are actual Gaussian-integer multiplicities, including
every representation; replacing them by one vector per unit radial
interval would be incorrect. Smooth T-dependent mollifier profiles
for fixed a<1 have the same uniform positive integral and yield the
same lower estimate. The leading coefficient |k|^(-1/2) is comparable
to T^(-1/2) and changes only fixed constants.

For the matching upper certificate, group dual radii in intervals of
width N^(-1/2). Each corresponds to an interval of integer squared norms
of length O(T/sqrt(N)+1). The elementary divisor bound gives at most
C_epsilon T^epsilon(1+T/sqrt(N)) lattice vectors. Schwartz decay of S
sums the intervals, yielding

    G_N <= C_epsilon T^(-1/2+epsilon)(1+T/sqrt(N))
         <= C_epsilon T^(1/2+epsilon)N^(-1/2)

when N<=T^(3/2). Integrating its pth power restores the matching upper
power. This prices the positive leading certificate only; stationary
remainder and far-frequency terms in the full exact Poisson expansion
must be paid by the discovery report and its application review.

At p=12,N=T^(2/3), the positive certificate costs T^3, well above
T^(29/25). Keeping an independently signed second moment can improve
the familiar variance-times-envelope result to the old T^(7/3) global
bound, but it is still worse than the accepted complete moment power.
The additional stationary R/radial integration has not created a new
arithmetic estimate of the near dual shells.

## 4. First unproved step

The missing step is cancellation between the actual neighboring dual
radii in the complete signed moment, retaining the odd profile and all
products. Neither Hessian rank nor a large number of ambient variables
bounds that arithmetic sum. The lower bound on G_N says nothing about
the signed sum before moduli. A small scalar remainder or paid diagonal
does not estimate every mixed near-shell term.

## 5. Controls and outcomes

Rank agrees at p=1 when the common-R critical condition has no solution
on a positive annulus; the fixed-R angular rank remains1. Balanced p=2
already has a one-dimensional radial critical manifold. Mixed signs,
unequal L_j and nonproduct smooth amplitudes change feasibility or
constants, not the local rank at a nonvanishing interior point. The
odd scalar profile vanishes exactly at its center, yet its even power
has positive integral. The certificate retains actual integer annulus
mass and all angular representations. No smooth squarefree mask or
lower bound on a signed arithmetic quantity is asserted. Zero experiments.

## 6. Dependencies and provenance

Read protocol, graph/manifest/frozen218 strategy, closed217 checkpoint,
accepted204/216/217 kernels, and closed203/210/213 syntheses. The rank
and shell-mass algebra above were reproduced locally by the conductor;
discovery-agent intermediate messages independently identified the same
rank and warned about the odd sine profile. Their uncompleted reports
are not accepted evidence here. The elementary disk count and divisor
bound are accepted inputs. No new external theorem is imported.

## 7. Recommended state effect

Retain as a bounded diagnostic control after exact-hash seam review.
No new graph node is requested merely for stationary geometry or a
restatement of the old scalar envelope. Keep the full signed I12 and
quarter theorem open. Any next method must estimate the actual signed
near-shell aggregate rather than claim a gain from ambient dimension.
