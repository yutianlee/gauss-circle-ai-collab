# Round 214 isolated radius-optimization packet

Read only this packet and protocol.md. No graph, manifest, strategy,
general generated brief, prior reports, siblings or web. Write only
reports/blind_radius_optimization.md in this campaign, then stop.
Use seven numbered protocol sections. Supplied graph metadata only:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.

Let T>=2, 1<=N<=T. A family of complex block sums F_(T,N)(R), R~T,
has elementary caps, at epsilon-loss level,

    |F| <= min(N^(1/4), (T/N)^(1/2)).

For integer lengths 2<=L<=K<=cN (fixed small c>0), suppose finite
differencing gives

    |F|^4 << T^epsilon [N/L^2+N/K+A4].

Put U=N^(3/2)/T, D=LK/U. The repeated shifts and products hk<=U,
together with any smooth-model contribution, have complete normalized
cost at most T^epsilon[N/K+N/D], allowing harmless logarithms. The
residual product shells q=2^j, q<hk/U<=2q have fractions

    delta_j <= C min(1,q log(2L)/D), sum_j delta_j<=1,

and q<=D for each nonempty shell. For every shell the paid radius
transfer is

    sup_R shell_RMS <= C sqrt(q) Q_j+C_B N T^epsilon q^-B,

for arbitrary fixed B>1, where Q_j is a normalized L2 radius norm on
a larger interval with fixed positive margins. Assume as a hypothetical
arithmetic input, uniformly for the lengths to which it is applied,

    Q_j <= C_epsilon T^epsilon [sqrt(N)+N q^(-3/2)].

The region D<=1 can be treated by the original elementary caps; no
residual shell then exists. Bounded N can be paid separately. Logs and
ceilings must be retained or rigorously absorbed. No arithmetic proof
of this hypothetical input is supplied.

Derive the complete certificate for |F|^4 and optimize its uniform
power in T over all allowed L,K and all 1<=N<=T, combining the caps.
Determine whether free length optimization beats a target-power choice
L~sqrt(N)T^-2b, K~NT^-4b on the band T^(4b)<N<T^(1-2b).
If a limiting exponent is inherent in this certificate, prove that
statement at an exact scale; an upper certificate is not an actual
lower bound for F.

As an additional formal comparison, replace only sqrt(N) in the
hypothetical radius input by sqrt(N)q^-sigma, 0<=sigma<=1. For the
displayed target-power lengths and fixed 0<b<1/6, derive the precise
power condition for |F|<=T^(b+epsilon), using the full shell fractions
when their power is decreasing. State the limit needed for b tending
to zero, without asserting feasibility of the stronger arithmetic input.
Do not silently give this input a wider validity range in lengths than
its hypothesis. Explicitly distinguish algebraic optimization, actual
arithmetic truth and consequences for a physical discrepancy that would
be T^(1/2) times a sum of logarithmically many such blocks, with squared
radius X=T^2 and target-safe complementary errors.
