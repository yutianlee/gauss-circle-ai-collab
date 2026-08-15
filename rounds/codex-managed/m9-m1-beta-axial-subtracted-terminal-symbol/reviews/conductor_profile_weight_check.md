# Conductor audit: an L-independent height weight must absorb translated profiles

Campaign: `m9-m1-beta-axial-subtracted-terminal-symbol`  
Role: conductor weighted-symbol seam review  
Allocation: 100% analytical/algebraic

The accepted profile satisfies

\[
|f_b^{(r)}(\nu)|\ll_{b,r}(1+|\nu|)^{-3-r}.
\tag{39.C5}
\]

In (39.C1), however, one term contains \(f_b(L)\), while the proposed
right side is \(\lambda^{-2}w_b(\nu)\) with a single weight independent of
the saddle location \(L\).  A pointwise proof must not silently use
\(w_b(\nu)=(1+|\nu|)^{-3}\) for every term: at \(\nu\) near \(L\), the
diagonal quotient is controlled by translated derivatives
\(f_b'(L+t(\nu-L))\), whereas at \(\nu\) near zero the large-
\(|L|\) value \(f_b(L)\) is small.

A legal fixed weight can be assembled by region, for example from a finite
sum of the unshifted profile weight and rational Cauchy tails, but the
proof must verify it uniformly in \(L\) and after the fixed-\(\nu\)
derivative.  The weaker and naturally sufficient interface for the
Round-31 finite-section lemma is

\[
\sup_L\int|K(L,\nu)|\,d\nu\ll_b\lambda^{-2},\qquad
\int_{L\text{-cell}}\int|\partial_LK(L,\nu)|\,d\nu\,dL
\ll_b\lambda^{-2},
\tag{39.C6}
\]

together with the two translated moving-face traces.  A single pointwise
product majorant is stronger than (39.C6) and should be promoted only if
it is actually proved.  If it fails at a translated diagonal, Round 39
should revise the obligation to the mixed norm (39.C6), not mistake the
failure for a no-go against the downstream BV result.

No computation or external theorem is used.
