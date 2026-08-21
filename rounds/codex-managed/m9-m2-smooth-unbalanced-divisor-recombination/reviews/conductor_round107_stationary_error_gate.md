# Conductor review: aggregate (h)-process error gate

## Smooth-component normalization

Fix one component on which every (h)-support boundary is supplied by a
flat (C_c^infty) cutoff, every normalized derivative of the amplitude is
bounded, and no sharp star, clipped height endpoint, or arithmetic owner
boundary crosses the saddle. For fixed (kasymp K), write (h=Lu). The
large phase parameter is

\[
 \mathcal F_k=\sqrt{XkL}\asymp {XL\over D}=F.
\]

The derivative range has length

\[
 R\asymp {F\over L}\asymp {X\over D}.
\]

## Uniform stationary expansion

After Poisson summation in (h), every interior stationary integral has
the form

\[
 L\int A_{k,m}(u)e(F\phi_{k,m}(u))\,du.
\]

The normalized critical point is nondegenerate, with all normalized phase
and amplitude seminorms bounded uniformly on the fixed component. Keeping
the leading stationary term leaves

\[
 O_A(LF^{-3/2})
\]

per stationary dual frequency. There are (O(F/L)) such frequencies, so
the aggregate remainder for one (k) is (O_A(F^{-1/2})). Repeated
integration by parts makes the nonstationary tails smaller than any fixed
power of (F). Summing (kasymp K) gives

\[
 E_{L,K}\ll_A K F^{-1/2}.
\]

Under the accepted physical normalization this becomes

\[
 X^{1/4}(LK)^{-3/4}K F^{-1/2}
 ={1\over L},
\]

and is therefore target-safe.

## Boundary qualification

The calculation certifies the complete leading-term expansion and aggregate
error only on the stated flat smooth component. A clipped terminal height,
one-sided stationary entry, star, physical hard edge, or arithmetic owner
mask is not covered by this uniform scalar expansion. Such a piece must be
kept as its exact endpoint/Fresnel integral or assigned to its existing
owner before the fixed-centre formula is used.

Thus the aggregate-error objection is closed for strict smooth residual
components, but not for the full collection of literal endpoint atoms. This
scope is sufficient to validate the returned carrier and its exact deficit;
it does not prove the signed fixed-centre estimate.
