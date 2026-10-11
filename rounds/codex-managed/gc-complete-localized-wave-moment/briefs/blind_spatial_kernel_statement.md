# Round215 isolated spatial-kernel packet

Read only this packet and protocol.md. No web, graph, manifest, strategy,
general generated brief, other report or historical files. Write only
reports/blind_spatial_kernel.md in this campaign, with seven numbered
protocol sections, and stop. Graph hash supplied as metadata only:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.

Let T>=2, N=T^alpha, with fixed166/325<alpha<242/325 when testing
power limitations. Upper identities should allow the entire corresponding
open band, with realT,N. Let finite nonnegative coefficientsa_m, supported
on integer vectorssqrt(N)<=|m|<=2sqrt(N), satisfy

    sum_m a_m comparable to N^(1/4), 0<=a_m<=C N^(-3/4).

Do not infer a particular arithmetic origin or an actual circle theorem.
Define e(z)=exp(2pi iz), F(x,R)=sum_m a_m e(x.m+R|m|).
Fix real Schwartz phi:R^2->R and eta:R->R with compact small Fourier
support, phi(0)=eta(0)=1 and modulus bounded below on fixed central
cubes. Put W(y)=C(1+|y|^2)^(-100), C>0 fixed.
Let a=1/sqrt(2), d=sqrt(3)-a, J=ceil(dT/sqrt(N)),
R_j=aT+j sqrt(N), 0<=j<=J, and

    f_j(y,u)=phi(y/N)eta(u/N)F(y/sqrt(N),R_j+u/sqrt(N)),
    C(T,N)=sum_j integral W(y)|f_j(y,u)|^10 dydu.

Derive the exact tenth expansion into two five-tuples, retaining every
spatial and radial frequency difference, each center modulation, and
the true scales of the two Fourier transforms. Independently expressC
as a single integral inR with the sum of window weights. Include the
full Schwartz tails; do not cut a window at its central interval.

Then investigate these two explicit positive upper certificates:
(i) take the modulus of every expanded two-five-tuple kernel separately
for eachj before summing the windows;
(ii) first sum the actual center phases/window kernels exactly acrossj,
then take the modulus of each combined two-five-tuple kernel.
Give exact definitions and determine rigorous power lower bounds from
the supplied nonnegative mass and support hypotheses, if possible.
You may use elementary pigeonholing/Cauchy--Schwarz or analytic Fourier
identities, but not statistical independence. Check whether the spatial
Fourier factor has a uniformly positive lower bound on the relevant
bounded frequency-difference domain; prove or refute that assertion.
Compare any certificate bounds withT^(83/65+epsilon) throughout fixed
interior scales. A lower bound on an upper certificate is never a lower
bound onC, F or a physical discrepancy. Explicitly test that logical seam.

Finally derive the elementary fixed-spatial-bandwidth trace implication
from a bound onC to the tenth moment ofF(0,R) on
[T/sqrt(2),sqrt(3)T], paying du=sqrt(N)dR. State what remains unproved
about the actual signed moment. No numerical experiment is required.
