# Round 206 conductor: the precise sixth-moment saving still needed

Campaign: gc-complete-signed-shell-arithmetic. Date: 2026-09-26.
Role: conductor analytical derivation; candidate evidence, no graph promotion.
Starting graph SHA256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
Effort:100 percent analytical; no numerical experiments.

## 1. Result

The centered variance-scale sixth-moment input suggested at launch is
stronger than needed. The actual sufficient loss is calculated below,
without replacing the frozen complete twelfth target. A coefficient-energy
argument already supplies the ideal block second moment, so improving a
two-point source to variance scale alone cannot repair the sixth-moment gap.

Combining that block second moment with the accepted distribution gives
the actual middle-block sixth bound

\[
 \int_I |H_N(R)|^6dR\ll_\epsilon T^{1+\epsilon}N^{-29/110}. \tag{C1}
\]

This is better than the complete generic sixth bound for these blocks,
but still far from the sixth estimate sufficient for the p12 milestone.
Raising (C1) by the available supremum gives complete p12 exponent
1+(272/55)beta, worse than the already accepted10beta. No new complete
twelfth bound or pointwise exponent follows.

## 2. Exact objects and hypotheses

I=[T/sqrt(2),sqrt(3)T], T>=2, and N runs over all dyadic scales in
T^(52/125)<N<T^(99/125). Use exactly the fixed smooth physical block
H_N, shell S_N and actual mollifier of the reviewed205 interface. Write

\[
 N=T^\alpha,\quad
 \omega(\alpha)=\min\{\alpha/4,\beta,(1-\alpha)/2\},
 \quad q=136/13.
\]

The coefficient l2 energy is O_eta(N^(-1/2+eta)), and the complete
block distribution obeys T^epsilon(V^-2+T V^-q). These follow from
the accepted204 kernel with bounded smooth coefficients and fixed
support enlargement. Supremum powers have arbitrary small epsilon
losses throughout; constants and finite logarithms are absorbed only
after choosing the input losses appropriately.

For the exact additive filter Z_N(x) of the isolated206 packet, put
X=T^2 and h_N(x)=2sqrt(x)/sqrt(N), with H=T/sqrt(N) denoting its scale.
The independent bridge report supplies
S_N(R)=R^(-1/2)Z_N(R^2)+O(T^(-1/2+epsilon)N^-1)+O_A(T^-A).
That report and the205 radial identity are explicit dependencies for
transferring any conclusion about H_N to Z_N; they are not silently
accepted as new graph nodes.

## 3. Derivation and restored powers

### An elementary ideal block second moment

For a complex block F(R)=sum a_n e(R sqrt(n)) on a fixed enlargement
of [N,2N], distinct frequencies obey

\[
 |\sqrt n-\sqrt m|\gg |n-m|/\sqrt N.
\]

Open its square over I. The diagonal is O(T sum|a_n|^2); an
off-diagonal integral has modulus O(sqrt(N)/|n-m|). Using
2|a_n a_m|<=|a_n|^2+|a_m|^2 and the harmonic sum gives

\[
 \int_I |F|^2dR\ll(T+\sqrt N\log(2N))\sum|a_n|^2
                \ll_\epsilon TN^{-1/2}T^\epsilon.       \tag{C2}
\]

Here N<T^(99/125)<T^2. The same bound holds for its real part H_N
and for the two ambient intervals needed by v's [1,4] support. This
is a direct calculation for the actual coefficient vector, requiring
no shifted-r2 theorem. Consequently the additional variance/error term
in a legal pair-source transfer may be bypassed for this particular
block second moment; no sixth moment follows from doing so.

### Legitimate block supremum

The coefficient l1 bound gives N^(1/4+epsilon); the reviewed absolute
shell bound gives T^(1/2+epsilon)N^-1/2. To obtain T^beta blockwise,
apply the Fourier multiplier v(xi^2/N) to the complete real H_T(R).
Its kernel is sqrt(N)q_0(sqrt(N)u), for a fixed Schwartz q_0, of
bounded L1 norm. On a fixed larger positive R interval use the accepted
complete supremum T^(beta+epsilon). Outside that interval use the global
l1 bound H_T<<T^(1/4+epsilon) and the arbitrarily decaying convolution
tail. This proves

\[
 \sup_I|H_N|\ll_\epsilon T^{\omega(\alpha)+\epsilon}.    \tag{C3}
\]

The exact even multiplier treats both signs in the cosine and kills
the zero frequency. It is not an inference from a bound on the whole
sum to an arbitrary summand. The known negligible radial error transfers
(C2)--(C3) to S_N.

### Intersecting the two actual level-set bounds

By (C2), the block level set also obeys
D_N(V)<<T^(1+epsilon)N^-1/2 V^-2 for every V>0.
Split its sixth layer-cake integral at

\[
 V_0=N^{13/220},\qquad V_0^{q-2}=N^{1/2}.
\]

Below V_0 use this Chebyshev bound. Above V_0 use the accepted
distribution, up to W=max(1,C T^(omega+eta)). If W<V_0 the low bound
alone is no larger than the asserted result. Otherwise the three
terms after integration are

\[
 TN^{-1/2}V_0^4=TN^{-29/110},\qquad
 W^4,\qquad TV_0^{6-q}=TN^{-29/110}.                   \tag{C4}
\]

Using Chebyshev even below V=1 is legal and its V^3 integral converges
at0; no incorrect O(T) baseline is inserted there. The high-distribution
threshold is >=1. In the entire middle range W^4 is dominated by
TN^-29/110 after small epsilon losses: omega<=beta<1/6 gives4omega<2/3,
whereas1-(29/110)alpha>1-(29/110)(99/125)>3/4.
This proves (C1). All comparison constants are independent of the dyadic
scale and real T, including boundary-adjacent scales.

Multiplying by W^6 and summing all middle blocks by Minkowski gives

\[
 M_{12}(\text{middle})\ll T^{E+\epsilon},\qquad
 E=\max_{52/125\le\alpha\le99/125}
       \{1-(29/110)\alpha+6\omega(\alpha)\}
  =1+(272/55)\beta.                                  \tag{C5}
\]

The piecewise function increases up to alpha=4beta and decreases
afterwards;4beta<1-2beta and both lie inside the closed displayed range.
Since beta<1/6<55/278, E-10beta=1-(278/55)beta>0.
The accepted complete p12 bound remains stronger. Thus a locally improved
sixth estimate is not by itself a better complete p12 estimate.

### Weakest sixth input certified by these supremum bounds

The exact Jacobian and amplitude give

\[
 \int_I|S_N|^6dR\ll T^{-4}\int_{X/2}^{3X}|Z_N(x)|^6dx
                    +\text{negligible error}.          \tag{C6}
\]

Consequently a sufficient uniform input is

\[
 \boxed{\int_{X/2}^{3X}|Z_N|^6dx
  \ll_\epsilon T^{129/25+\epsilon-6\omega(\alpha)}.}   \tag{C7}
\]

This is the exact threshold of this particular supremum-times-sixth
certificate, not a necessary fact about the actual p12 moment. Relative
to the variance-scale sixth size XH^3=T^5N^-3/2, (C7) permits a factor
T^(ell(alpha)+epsilon), where

\[
 \ell(\alpha)=4/25+(3/2)\alpha-6\omega(\alpha).        \tag{C8}
\]

In particular ell>=4/25 throughout, using omega<=alpha/4. A uniform
variance-scale bound with a T^(4/25) loss therefore still suffices.
The stronger variance-scale input itself gives middle M12<<T^(1+epsilon)
by the elementary coefficient supremum; the outer part remains bounded
at the requested29/25 scale unless separately improved. It is incorrect
to call failure of variance scale a refutation of the weaker target(C7).

The proved block sixth estimate (C1) corresponds to a loss N^(68/55)
relative to its variance scale. The net sixth-moment saving still needed
for this route is, at N=T^alpha,

\[
 g(\alpha)=6\omega(\alpha)-4/25-(29/110)\alpha.         \tag{C9}
\]

It is positive everywhere in the complete middle interval. On the first
piece it is increasing and at52/125 equals2436/6875>0. On the second
piece it decreases, and on the final piece it decreases further; at
99/125 it equals3509/13750>0. Its maximum occurs at4beta and is
(272/55)beta-4/25. No middle scale is dismissed on the basis of (C1).

## 4. First unproved step

The actual signed sixth moment must beat (C1) by the complete profile
(C9), or a direct twelfth-moment argument must bypass this sufficient
certificate. A pair theorem or Gaussian analogy is not the required
six-factor arithmetic information. All distinct- and repeated-shift
correlations and the signed local densities must be retained.

Neither the strong variance input nor the weaker sufficient(C7) is proved
here. The full target, the accepted10beta p12 bound and pointwise theta
remain unchanged. A generic norm calculation does not refute actual r2.

## 5. Controls and outcome

The second moment retains the full diagonal, every off-diagonal frequency
and all coefficients. Layer cake uses the correct threshold and is
integrable at0. Fixed real interval enlargement licenses the multiplier
supremum. The p6 conversion loses exactly T^4 before any p12 estimate.
The complete dyadic maximum is at the interior4beta, not an omitted
endpoint. The strong and weak sufficient inputs are explicitly separated.
All original and transformed tails remain those of the complete interface.

These are analytical derivations, pending independent line review. No
numerical experiment or new external theorem is used. No sign cancellation
in an actual six-factor arithmetic remainder is asserted.

## 6. Exact dependencies and artifacts

protocol.md; current state/proof_obligations.yml and active206 manifest;
strategy/round206_complete_signed_shell_arithmetic_attack.md;
proofs/kernels/gc_complete_square_root_large_values_moment_bound.md;
the reviewed205 middle-band candidate and its independent review;
reports/blind_odd_shell_bridge.md for the centered-filter transfer;
reports/shifted_moment_source_attack.md for comparison with its priced
pair route. The proofs of(C1)--(C5) above are direct conductor calculations,
not imported source conclusions. The multiplier bound is rederived here.

## 7. Recommended state effect

Retain as a complete power ledger, not an additional proof-graph fragment.
If no actual signed arithmetic improvement arrives, close206 with an
identity State Patch. Archive the exact remaining saving profile and
the actual absolute-placement obstruction from the arithmetic task;
do not replace the whole target with a stronger Gaussian conjecture or
an unestimated selected subrange.
