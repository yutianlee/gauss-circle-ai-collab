# Round207 conductor: rational variance, masks and complete norm costs

Campaign: gc-signed-rational-filter-attack. Date:2026-09-27. Role: conductor
analytical derivation, candidate evidence pending independent review.
Starting graph SHA256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
100 percent analytical; no mathematical numerical experiments.

## 1. Result

The complete rational representation has a directly provable second moment
of variance order, including its moving index cutoff and the actual
variable-width multiplier. Neither feature forces a power loss in this
norm. The proof below retains frequency collisions before using separation.

An even fixed hyperbola cutoff removes the leading threshold-freezing
error. This is a harmless variant of the tested floor cutoff, with its
own exact identity and explicit comparison; it does not change the frozen
moment target. Neither this simplification nor the rational second moment
provides the required signed sixth moment. The complete signed estimate
of the discovery task and the separate actual-coefficient majorant
obstruction must be assessed with these precise costs.

## 2. Exact statements and hypotheses

Use the exact physical filter K of206, with K(u)=integral_1^2
t^-1 Psi(sqrt(N/T)t)v(t^2)sin(2pi t u)dt, X=T^2,
J=[X/2,3X], h(x)=2sqrt(x)/sqrt(N), H=T/sqrt(N), and the entire
middle range T^(52/125)<N<T^(99/125). K is real odd and uniformly
Schwartz, with Fourier support [-2,-1] union [1,2]. Its seminorms
and those of its Fourier transform are bounded uniformly in N,T.
For Fourier transforms use e(-u*xi), with e(z)=exp(2pi i z).

Let M=ceil(6X). Either use D=floor(sqrt(M)) or the explicitly stated
even variant D_e=2floor(floor(sqrt(M))/2). In both cases D~sqrt(X)
and L=floor(M/(D+1))~sqrt(X). All conclusions are for large X;
bounded X is absorbed into constants. Let eta be the localized cutoff
equal to1 on [1/3,4], supported in [1/4,6]. The actual centered filter
is Z(x)=sum_(m>=1)(r2(m)-pi)K((x-m)/h(x)).

The proposed direct bound is

\[
 \int_J |Z(x)|^2dx\ll_\epsilon X^{1+\epsilon}H. \tag{C1}
\]

This is independently known from original frequency spacing in206.
Here it is rederived entirely on the rational side to audit the actual
mask and coefficient costs. No new full moment bound is claimed.

## 3. Derivation and norm accounting

### Exact two-arm expansion and the even-cutoff variant

For every positive integer m<=M the fixed-cutoff identity is exact:

\[
 r_2(m)/4=\sum_{d\le D}\chi_4(d)1_{d\mid m}
 +\sum_{\ell\le L}1_{m>D\ell}1_{\ell\mid m}\chi_4(m/\ell).
 \tag{C2}
\]

This proof only partitions the divisors at D; it does not require
D=floor(sqrt(M)). The even variant therefore has the same identity
with its own L. The localization error, lattice mean and removal of
the positive half-line are rapidly small by the buffer around J and
uniform Schwartz decay, after summing O(sqrt(X)) atoms.

The isolated threshold analysis yields, with this orientation,

\[
 R_D(x)=-\chi_4(D)\sum_{\ell\le L}
 \eta(D\ell/X)1_{x>D\ell}K((x-D\ell)/h(x))+O_A(X^{-A}).
 \tag{C3}
\]

Here R_D is the sum of the differences between the original thresholds
and their frozen forms1_(x>Dell), without the external factor4 in(C2).
For completeness, an incorrect-side multiple m=j*ell other than
j=D is at distance at least ell from x whenever it can cross the
threshold. The relevant ell are comparable to sqrt(X), much larger
than H. If ell is smaller by a fixed factor, its threshold is remote
from J and every incorrect-side term is also remote. These bounds,
summed with sufficiently high Schwartz order, give the remainder in(C3).
The only possible nearby incorrect-side multiple is m=Dell, occurring
when x>Dell, with the displayed negative sign. Thresholds are spaced
by D, so the remaining bump train has supremum O(1) and sixth integral
O(sqrt(X)H). Its second integral has the same bound. At x=Dell the two
strict indicators agree for m=Dell; all other terms belong to the
rapidly small remainder. K(0)=0 as well. This proves all endpoint
conventions and extends the isolated proof to either D above.

For D=D_e, chi4(D)=0, and R_D=O_A(X^-A). Thus evenness removes the
entire leading threshold error, without deleting any nonzero character
term or altering a coefficient of r2. For the original floor cutoff the
already-safe error is retained. In either case it is smaller than(C1)
and than the sufficient sixth threshold.

Periodic Poisson summation now gives the complete rational expression
Z(x)=A(x)+B(x)+4R_D(x)+O_A(X^-A), where

\[
 A(x)=4h(x)\sum_{d\le D}\frac{\chi_4(d)}d
       \sum_{k\in\mathbb Z}\widehat K(h(x)k/d)e(kx/d),
 \tag{C4}
\]
\[
 B(x)=-2ih(x)\sum_{\substack{\ell\le L\\D\ell<x}}\frac1\ell
       \sum_{k\in\mathbb Z}\chi_4(k)
       \widehat K(h(x)k/(4\ell))e(kx/(4\ell)).
 \tag{C5}
\]

The sign is fixed by sum_(r mod4)chi4(r)e(-kr/4)=-2i chi4(k).
Zero frequencies vanish; every nonzero harmonic is retained. Short
periods vanish when q<h(x)/2, including equality because the smooth
Fourier transform is zero at its support boundary. All harmonics lie
in a fixed enlarged envelope c/H<=|lambda|<=C/H on J.

### Exact collision grouping

For the first arm write k/d=a/q in lowest terms, q>0. A nonzero
character forces q odd and d=qj with j odd. After grouping, the
coefficient before the common multiplier h*Khat(h*lambda) is

\[
 c^A_{a/q}=\frac{4\chi_4(q)}q
       \sum_{j\le D/q}\frac{\chi_4(j)}j,\qquad q\ {\rm odd}.
 \tag{C6}
\]

For a fixed set I of quotient labels ell, write k/(4ell)=a/q
in lowest terms. Nonzero chi4(k) forces a odd, q divisible by4,
ell=qj/4 and k=aj with j odd. The grouped coefficient is

\[
 c^B_{a/q,I}=\frac{-8i\chi_4(a)}q
      \sum_{\substack{j\ge1\\qj/4\in I}}\frac{\chi_4(j)}j,
       \qquad4\mid q.
 \tag{C7}
\]

Thus the two arms have disjoint reduced-denominator classes; a
denominator2 mod4 is absent. This excludes exact cross-arm frequency
coincidence, not mixed near relations or cancellation in a sixth moment.
No duplicate rational frequencies remain within(C6) or(C7).

All reduced denominators are <=Q=max(D,4L)=O(sqrt(X)). Distinct
frequencies are separated by at least Q^-2>>X^-1. A frequency in
the fixed envelope has q>>H and O(q/H) possible numerators, including
both signs; counting noncoprime numerators only enlarges upper bounds.
For(C6) the alternating odd harmonic partial sum is uniformly bounded.
For(C7) an absolute logarithmic bound suffices for the variance audit.

### A separated-frequency norm bound with full collisions paid

If distinct real lambda have spacing >=c/X, expansion of the square
over any interval of length O(X) gives a kernel bounded by
min(CX,C/|lambda-mu|). Order the frequencies. Every absolute row sum
is O(X log(2+number of frequencies)), using the harmonic sum. Therefore

\[
 \int_J\left|\sum_\lambda b_\lambda e(x\lambda)\right|^2dx
 \ll X\log(2X)\sum_\lambda |b_\lambda|^2. \tag{C8}
\]

Only O(X) frequencies can occur here. The estimate is uniform in
translations of J and constant modulation of the whole sum. It is
an elementary Schur argument, not an uninspected external large sieve.

The actual varying multiplier costs no power. Write h(x)=H*s(x/X)
with s(y)=2sqrt(y), and choose a fixed compact extension in y and
z=H*lambda of
A_0(y,z)=s(y)Khat(s(y)z). On the envelope and y in J/X this is smooth
with uniform derivatives. Its two-variable Fourier transform has a
uniformly bounded L1 norm. Fourier inversion expresses the multiplier
as an absolutely integrable superposition of
e(u*x/X)e(v*H*lambda). The first is a common unit modulation; the
second translates the frequency polynomial by vH. Bound(C8) is
uniform under both operations. Minkowski therefore proves the same
bound for sum H*c_lambda*A_0(x/X,Hlambda)e(xlambda), with energy
H^2 sum|c_lambda|^2. This justifies the actual variable width rather
than freezing it or assuming arbitrary mixed coefficients factor.

For arm A, formulas(C6) and the envelope give
H^2 sum|c^A|^2 << H sum_(H<<q<=Q)1/q << H log(2X).
Together with(C8) this bounds integral|A|^2 by XH times logarithms.

### The actual moving prefix in arm B

For each x the retained ell form the prefix ell<x/D of [1,L].
Decompose every such prefix into its canonical disjoint dyadic
intervals. There is at most one selected interval at each scale.
Use Cauchy across the O(log X) scales. At a fixed scale the sets
of x selecting the different intervals I are disjoint, so after
integration their squared norms are bounded by sum_I integral_J|B_I|^2.

The coefficient energy over these intervals must be controlled jointly,
not bounded separately by the full energy times their number. For fixed
a/q, the sets of j with qj/4 in the various disjoint I are disjoint.
Consequently

\[
 \sum_I\left|\sum_{qj/4\in I}\chi_4(j)/j\right|^2
 \le\left(\sum_{j\le4L/q}1/j\right)^2\ll\log^2(2X).
 \tag{C9}
\]

Counting the O(q/H) possible numerators and summing q now gives
sum_I H^2 sum_lambda|c^B_(lambda,I)|^2 <<H log^3(2X).
The multiplier argument applies simultaneously to the Hilbert direct
sum over I: Minkowski costs the same bounded Fourier L1 norm.
Apply(C8) to each fixed I and sum. The extra scale count and Cauchy
factor cost only further logarithms. Thus integral|B|^2 <<XH log^C X
for an absolute C. Add arm A, the threshold error and all tails to
obtain(C1) for the complete actual Z.

This is the exact point at which the row-interval mechanism succeeds:
the interval mask has logarithmic cost once the collision-grouped
coefficient energies are paid. It is not a claim of an unproved
bilinear sixth-moment operator estimate.

### Complete sixth and twelfth costs

The same grouped coefficients have pointwise absolute mass O(Q) up to
logarithms after the multiplier. Indeed O(q/H) numerators times H/q
cost O(1) per denominator. Hence the rational coefficient l1 bound
and(C1) give only

\[
 K_6=\int_J|Z|^6\ll_\epsilon X^{1+\epsilon}H Q^4
             \ll X^{3+\epsilon}H=T^{7+\epsilon}N^{-1/2}.
 \tag{C10}
\]

The separate signed second-derivative attempt instead gives the actual
original-coefficient supremum |Z|<<T^(1/2+epsilon)N^(1/4), so(C1)
would give K6<<T^(5+epsilon)N^(1/2). This is still worse than the
reviewed206 bound K6<<T^(5+epsilon)N^-29/110. Further retaining the
minimum of all known suprema reproduces the old variance interpolation,
not a new sixth theorem. These upper costs do not lower-bound K6.

The sufficient threshold remains T^(129/25-6omega+epsilon). None of
these complete rational norm calculations reaches it; even the better
reviewed206 sixth bound has the strictly positive missing profile g.
The accepted full p12 exponent10beta remains strongest. The other
analyst's actual-coefficient majorant must be read as a statement about
termwise absolute expansion, never as a lower bound for the signed sum.

## 4. First unproved step

A successful argument must use the actual signs in the complete six-factor
rational correlation, beyond(C8)--(C9) and the recovered second-derivative
supremum. Exact denominator separation is not independence of the two
arms and does not remove their mixed high-moment terms. A reciprocal
transform, a logarithmic interval-mask cost and a target-safe threshold
error do not establish that higher correlation inequality.

The signed second-derivative statement cited above is a separate task
candidate to be independently reviewed; the proof of(C1)--(C9) here
does not depend on that statement. The even-cutoff variant is also
subject to an independent post-report line review before closure.

## 5. Controls and outcome

Real endpoints, all zero/nonzero Fourier modes, both signs and both
hyperbola arms are retained. The mod4 factor is checked at k=1 as -2i.
The case even D eliminates only a coefficient already zero under chi4.
The floor D case retains its explicit bump train. Lower-half-line and
localization tails are paid before periodic extension. Collision grouping
precedes frequency separation, with correct odd and4-divisible denominator
classes. The prefix energy uses(C9), not an illegal multiplication by
the number of dyadic intervals. Uniform smoothness justifies variable
width at bounded product-integral cost. All norms include all middle N.

No mathematical numerical experiment, Gaussian inference, missing CRT
remainder or generic-coefficient counterexample for actual r2 is used.
No new external theorem is imported by this conductor derivation.

## 6. Dependencies and exact artifacts

protocol.md; state/proof_obligations.yml; active207 manifest;
strategy/round207_signed_rational_filter_attack.md; the reviewed206
actual divisor report, sixth power ledger and independent seams; the
reviewed205 middle-band interface; accepted204 large-values kernel.
The isolated207 report supplies the threshold statement, and its proof
is independently expanded in(C3). The two207 discovery reports are
used only for explicitly labeled comparison statements pending review.
All rational coefficient energies and multiplier/mask costs are derived
above, not attributed to an unnamed external theorem.

## 7. Recommended state effect

Retain as reviewed evidence if the independent seams pass. Do not promote
another graph fragment for recovered variance or an auxiliary cutoff
choice. If no full gain arrives, use an identity State Patch and preserve
the original proof draft and every accepted exponent. Close207 before
designing the mandatory broad strategy/current-literature review208.
