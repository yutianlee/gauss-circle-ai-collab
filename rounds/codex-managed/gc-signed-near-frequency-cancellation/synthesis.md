# Round210 synthesis: signed bins and actual shifted correlations

Campaign: `gc-signed-near-frequency-cancellation`. Conductor: Codex.
Date: 2026-09-27. The frozen objective is the complete signed near-frequency
estimate, or another complete pointwise gain. It is not achieved.

## Decision and complete target

Retain reviewed method evidence and close with an identity State Patch.
No complete tenth-moment estimate or accepted pointwise exponent improves.
The full quarter theorem and the independent M1/M2 parents remain open.
The graph retains all 399 nodes; the graph and proof-draft bytes are unchanged.

With X=T^2, H=T/sqrt(N), and every dyadic
T^(166/325)<N<T^(242/325), the objective remains

    |O10(N)| << T^(473/65+epsilon) N^-1/2.

The complete exact rational energy is already bounded by
T^(7+epsilon)N^-1/2, including nonpairing relations. Thus the displayed
signed target is equivalent, after the reviewed errors, to the original
physical gate M10(H_N)<<T^(83/65+epsilon)N^-1/2. Even success at that gate
would yield only the milestone 102/325, not the full quarter theorem.

The two terms in the best inherited bound both remain:

    M10(H_N) << T^epsilon [T N^(-3/110) + T^(8 omega)],
    omega=min(alpha/4,beta,(1-alpha)/2), N=T^alpha,
    beta=(50 sqrt(1717)-297)/13762.

The bulk term alone misses the gate when alpha>99/169; suppressing only
the high-value diagonal term would not solve the problem. The current
accepted external exponent remains (3292+25 sqrt(1717))/13762.

## What the round established

### Complete phase-preserving bins: a valid transfer, but an inadequate input

The isolated derivation validates the H1 transfer for internally modulated
bins at spacing 1/X. A scaled derivative is essential. Constant coefficient
sums inside bins do not replace internal modulation. Canonical decomposition
of a moving prefix costs one outer logarithm and retains the entire sum of
fixed-interval energies. Derivatives must be taken on those smooth blocks,
not on the jumping selection indicator. The generic countercontrols test
these analytic assertions only; they are not arithmetic counterexamples.

For the actual rational expansion, label the first arm by zero and the
second arm by its original integer quotient ell. The strict cutoff is
D ell<x. Grouping a fifth product by its maximum label turns its five
thresholds into one prefix. A complete fixed-label interval [a,b] contributes
S_b^5-S_(a-1)^5, with all mixed terms and multiplicities preserved.

The rational analyst defines a normalized joint energy E_N in equations
(12)--(13) of `reports/signed_rational_bins.md`. Its measure is dy=dx/X.
It includes all label intervals, bins, width derivatives and internal phase
derivatives. The complete transfer is

    integral_J |Q_N(x)|^10 dx << X log(2L+2) E_N.

Smooth bins and periodized Parseval convert their input to physical averages
with factor 1/X. Frozen prefixes have exact integer-lattice coefficients:
nonzero integers have divisor size, while the zero integer has coefficient
4 sum_(d<=D) chi4(d)=O(1). This cancellation survives every prefix and width
derivative. The all-real physical envelope, together with the joint interval
second moment, yields

    E_N << H^9 T^epsilon,
    integral_J |Q_N|^10 << X H^9 T^epsilon
                         =T^(11+epsilon) N^(-9/2).

All physical convolution tails and all dyadic levels are paid. This improves
the crude rational-coefficient calculation by N^4, but merely recovers the
known variance-times-supremum price. It does not improve the inherited best
moment bound. Its excess over the target is T^(242/65)N^-4, whose exponent
lies strictly between 242/325 and 546/325 on the required band.

For this particular sufficient route, the unproved input is

    E_N << T^(343/65+epsilon) N^-1/2.

The signed target need not imply this stronger joint energy estimate.
The failed upper calculation is not a lower bound for E_N or the moment.

### Actual shifted correlations: two precisely scoped failures

For u_n=c_n f_N(n)e(R sqrt(n)), with c_n=r2(n) or r2(n)-pi, define
D_diag=sum|u_n|^2 and the signed Fejer shift aggregate

    S_L=2 Re sum_(1<=h<L)(1-h/L) sum_n u_(n+h) conjugate(u_n).

Exactly D_diag+S_L=(1/L)sum_m|sum_(0<=j<L)u_(m+j)|^2>=0. The resulting
complete sufficient tenth-moment route has

    M10(F_c) << T N^(5/2+epsilon)L^-5
                +(N/L)^5 integral_I (S_L)_+^5.

One may pay its separated diagonal with
L>=T^(-18/325)N^(3/5), a growing but o(N) length throughout the band.
The first unproved signed estimate is

    integral_I (S_L)_+^5
       << T^(83/65+epsilon)L^5 N^(-11/2).

This is sufficient only. A proof keeping cancellation between D_diag and
S_L could avoid the separated diagonal condition. For centered coefficients,
the safe discrete mean supplies an alternative sufficient pointwise route;
it does not identify that moment with the original shell moment.

First, transferring an unweighted cumulative correlation error through
absolute Abel variation fails quantitatively. Actual centered atoms obey
|(r2(n)-pi)(r2(n+h)-pi)|>=(4-pi)^2, forcing a constant uniform remainder
floor against any continuous main term. The oscillatory weight has variation
at least a constant times T h N^-2 on a common interior interval. A positive
certificate that retains the diagonal, grants a free main term, and sums
absolute remainder costs therefore retains both

    N^(1/2)/L and T L/N.

Their compatibility with the squared-wave target T^(2b), b=83/650, would
require N>=T^(318/325), outside the required band. Even optimistically
granting an error-only absolute cap gives the cost
N^(1/2)/L+min(TL/N,N^(1/2)), which still fails on every fixed interior
scale. That cap is an extra allowance, not a bound asserted for a remainder
after nonzero main-term subtraction. These are certificate lower bounds;
no actual oscillatory correlation is lower-bounded.

Second, expanding actual r2(n)r2(n+h) into divisor pairs and estimating each
CRT progression before an absolute outer sum fails on exact singletons.
For small even h and odd n0 in a fixed common interior subband, take
d=n0 and e=n0+h. Then [d,e]>=N^2/h>3N, so the full progression contains
exactly n0. Each inner sum has modulus comparable to N^-3/2; there are
comparable to N distinct such pairs. Their exact positive cost is at least
N^-1/2 per shift and restores N^(1/2) in the squared-wave certificate.
Its tenth-energy price is at least T N^(5/2), larger than the target by
T^(-18/65)N^3. The character product is (-1)^(h/2), but the phases still
vary across n0: retaining their outer cancellation is precisely what this
failed closure discards. The same obstruction applies to a centered
expansion only if its four pieces are estimated separately in absolute
value. It does not refute a combined centered or signed dispersion method.

## Review, controls and state discipline

Three bounded reports were completed. The original bin rederivation used
only its isolated statement and protocol; its later conductor-ledger review
is separately marked nonblind. Cross-reviews cover the rational input and
actual shifted correlations. The conductor reviewed the isolated derivation,
reproduced the transfer and exponent algebra, and reconciled the scopes.
Final reports and reviews are bound by hashes in the reconciliation and
closure validation. GREEN applies to their stated local claims and closure,
not to either open arithmetic estimate.

Review repaired or clarified the strict prefix endpoint, smooth extension
of fixed blocks, the sign-definite interior mask, the positive-certificate
definition, the optimistic cap, and the zero/padded-prefix lattice
coefficient convention. Both generic analytic controls and
actual arithmetic controls are explicitly scoped. No new external theorem
was imported; no mathematical numerical experiment was used. Mathematical
effort was analytical/algebraic throughout. Frozen inputs, earlier closed
archives, prior ledger entries and both legacy directories are preserved.

The identity patch creates, updates, corrects and rejects zero nodes. The
useful finite algebra is retained as reviewed evidence; promoting another
interface node would not close the missing arithmetic parent.

## Consequence for the next decision

Round211 is the mandatory broad strategy and current-primary-literature
review after the closed208--210 block. It is pending design, not an
automatically launched successor attack. It must reassess the full quarter
goal and all M1/M2 alternatives, compare methods by restored net power, and
identify a source-compatible complete contribution before selecting another
attack. The pinned September23 review's warning against repeated local
reformulations applies directly: exact bins, prefixes and differencing
identities supply no saving without an actual signed high-order estimate.

Do not optimize the already-safe exact diagonal, repeat the same absolute
Abel/CRT closures, or treat a small individual sector as a complete result.
The live problem remains complete signed cancellation, with the two
explicit sufficient residuals above available for a genuinely new method.
