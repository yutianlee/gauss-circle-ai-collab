# Round218 conductor review of the isolated radial lemma

## 1. Result

GREEN for the stated abstract integral, uniform mismatch factors and
sharp normal rank. Claimant:reports/blind_joint_radial.md, SHA256
339971305a6dd5af4460d8827cb920c75350531294021b50df8c9249be062a47.
Conductor NONBLIND line review, 2026-09-28; campaign
gc-complete-signed-radical-kernel; starting graph
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
This does not prove the actual signed arithmetic moment.

## 2. Exact hypotheses checked

Fixed m and signs; a complex smooth, possibly nonproduct amplitude
compactly supported in the product of open annuli1<|y_j|<2; lambda_j>=2;
arbitrary xi_j, rho_j=|xi_j|; e(t)=exp(2pi it). Constants use finitely
many uniformly bounded amplitude derivatives. No uniformity in growing
m or in unbounded amplitude seminorms is asserted. The claimed global
factor per variable is (lambda_j+rho_j)^(-1/2)
(1+|lambda_j-rho_j|)^(-A).

## 3. Independent verification

The critical equation sigma_j lambda_j y_j/|y_j|=xi_j forces
rho_j=lambda_j and leaves exactly the radial ray variable r_j free.
The Cartesian Hessian block is sigma_j lambda_j/r_j times the
orthogonal projection onto the angular tangent, giving normal rank1
and one radial zero. Thus total rank m and critical dimension m follow
without an ambient-dimension assumption.

Near either angular branch, z=2sin((theta-theta_tau)/2) gives the
exact quadratic phase tau rho r z^2/2. The Fresnel Fourier identity
has factor e(tau/8)(rho r)^(-1/2) under the stated Fourier convention.
After including the polar Jacobian, the leading coefficient is
e(tau/8)r^(1/2)a(tau r omega); this checks the sign and normalization.
The Fourier remainder's radial derivatives introduce at most2k powers
of the Fourier variable for k derivatives. Two additional integrations
by parts in that variable make the weighted Fourier integral integrable.
The safe3k+2 amplitude derivative count therefore suffices for the
exact branch symbol, not merely for a leading asymptotic remainder.

Radial integration by parts then yields every prescribed mismatch
power. The opposite angular branch costs lambda+rho, and the angular
complement has at least q+1 direct nonstationary gains with q=ceil(A).
In the local comparable range this is stronger than the desired
lambda^(-1/2)(1+|lambda-rho|)^(-A). In the far range the full gradient
has size at least(lambda+rho)/3, including xi=0. Its adjoint integration
by parts gives arbitrary inverse powers and hence the stated product
factor. No angular direction is selected at xi=0.

The one-variable estimates retain passive-variable derivatives; iteration
therefore handles joint amplitudes with the stated generous total count
m(3ceil(A)+12). At resonance the only zero radial branch is tau=sigma.
Every other angular branch or symbol error gains at least one inverse
lambda_j. This verifies the unequal-parameter leading expression and
error with factor sum lambda_j^(-1). A fixed nonnegative bump on the
critical manifold has a positive leading coefficient, so decay
lambda^(-m/2) is sharp even for a parameter-independent amplitude.

## 4. First doubtful or unproved step

No gap is found in the abstract claims at the reviewed hash. Applying
the result to a nonsmooth arithmetic squarefree mask would be an
additional unjustified step. Summing actual dual frequencies, integrating
the common radius and estimating the signed arithmetic aggregate require
separate controls. The abstract lemma alone supplies none of those gains.

## 5. Controls and outcomes

GREEN for m=1, mixed signs, both angular branches, compact radial
boundaries, small/large/far/zero mismatches, joint amplitudes, unequal
parameters, exact e-convention, finite derivative counts and fixed-m
sharpness. If the amplitude vanishes on the critical set, only the upper
remainder claim remains; no lower bound is inferred. Zero experiments.
The original reviewer retained disclosed prior217 context, but received
only the new statement and protocol for this lemma; no current claimant
derivation was supplied. This is statement-only for the new lemma,
not a claim of a fresh history-free agent.

## 6. Dependencies and provenance

Read the frozen report and its isolated packet, protocol, frozen218
strategy and current graph. The derivation above independently checks
the elementary polar, Fourier and integration-by-parts seams. No external
theorem or web statement is used. The report remains byte-for-byte frozen.
The mathematical application belongs to the two actual discovery reports
and their later reviews, not to this abstract control.

## 7. Recommended state effect

Retain as reviewed analytical evidence. No graph node is needed merely
for this stationary-phase calculation. Use its correct normal rank and
uniform mismatch estimate in the complete cost audit; keep the signed
moment and quarter theorem open unless an actual arithmetic saving is
proved separately.
