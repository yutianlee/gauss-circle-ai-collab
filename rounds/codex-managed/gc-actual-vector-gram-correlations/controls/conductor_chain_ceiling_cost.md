# Round221 cost of closing anchored chains by endpoint ceilings

## 1. Result

A specific higher-chain closure cannot improve the accepted generic
large-value certificate. If it replaces the fixed-vector endpoints by
a scalar ceiling W and bounds the interior by the same Gram operator
norm, the effective level is v_eff=v(v/W)^(1/(k-1))<=v for k>=2.
Thus every resulting term is at least as large as the old certificate
at v. This is a limitation of that written inequality chain, not a
lower bound on actual high values and not a no-go for signed chains.

## 2. Exact statement and hypotheses

Let U be a finite J by n complex matrix, b a fixed vector, f=Ub,
G=UU*, B=||b||², and a_k=b*(U*U)^k b=f*G^(k-1)f. Suppose
|f_j|>=v>0 and |f_j|<=W for every row, B>0, ||G||<=L. For each
fixed integer k>=2, consider only the closure

    (J v²)^k <= B^(k-1) a_k <= B^(k-1) J W² L^(k-1).       (1)

For the conditional block application take
S(R)=sum_(N<n<=2N) b_n e(R sqrt(n)), sum|b_n|²<=A N^(-1/2),
with A a sufficiently small fixed power of T as in204. The vector may
be the actual r2/Psi vector with the exact large-class mask. For points
R_j in an interval of length h, separated by delta=N^(-1/2), use the
accepted204 unweighted correlation with kappa=13/55 and the full Gram
diagonal. W must be a PROVED ceiling for this same block on its window.
The full-wave Li--Yang ceiling is not automatically a dyadic-block ceiling.

## 3. Derivation

Finite spectral Holder gives a_1^k<=B^(k-1)a_k. The high values give
a_1>=Jv². Positivity gives a_k<=||G||^(k-1)||f||²<=L^(k-1)JW².
Taking the (k-1)st root of (1) and rearranging yields exactly

    J v_eff² <= B L,
    v_eff²=v^(2k/(k-1)) W^(-2/(k-1)).                       (2)

The accepted local row-sum calculation, with every diagonal retained,
gives for the dyadic square-root Gram

    L <= C A [N + sqrt(N)(J h^kappa+delta^(-1)log(2+J))].   (3)

The extra harmless A on the diagonal only enlarges the bound. Combine
B<=A N^(-1/2) with (2)--(3), absorb the J h^kappa term using
h a small fixed multiple of (v_eff²/A²)^(1/kappa), and cover the
complete interval by O(1+T/h) pieces, keeping the1. The resulting
certificate, after the same logarithmic and small-power allocation as204,
is

    D_S(v) <<_epsilon T^epsilon
                 [v_eff^(-2)+T v_eff^(-q)], q=136/13.     (4)

Here the endpoint regimes are explicit. If v_eff<1, the trivial O(T)
measure bound proves (4). If the formal h=c(v_eff²/A²)^(1/kappa)
is below delta=N^(-1/2), use O(T) again: before small-power allocation
the second term is T(A²/v_eff²)^(1+1/kappa), which dominates a fixed
multiple of T when h<delta<=1 (take c small and fixed). The harmless
powers of A are then allocated inside T^epsilon as in204. If h exceeds
the full radius window, use one interval; the first v_eff^(-2) term
is retained. In particular, T/h alone is never the cover count.

For an actual mask the coefficient energy is still admissible, so this
conditional calculation applies without treating the mask as smooth.
Because v<=W, v_eff<=v, and (4) is termwise no smaller than
T^epsilon[v^(-2)+Tv^(-q)], the direct204 certificate already available
for this vector. Formula (4) states an upper certificate, not the actual
measure's size. For k=2 its two terms are explicitly

    W² v^(-4) + T W^q v^(-2q),                            (5)

with ratios (W/v)² and (W/v)^q to the old two terms. For each fixed k
the same conclusion holds. Letting k increase only tends back to the
old level, and no unbounded-with-T assertion is needed or made.

The actual coefficient l1 norm is one legal block ceiling if no sharper
one is available. Choosing a smaller proved W>=v reduces the loss but
never beats the direct certificate. Combining with the better accepted
blockwise estimate and restoring all blocks therefore leaves the existing
complete full-wave bound available; this closure contributes no power
improvement. The final moment comparison uses the proved full-wave
ceiling only after complete reconstruction, as in204/216.

## 4. First unproved step

A gain would require information on f*G^(k-1)f that uses correlations
between the fixed-vector endpoints and the interior, rather than the
second inequality in (1). Merely writing the anchored expression,
bordering the Gram matrix, or applying its operator norm is insufficient.
This control leaves every genuinely signed actual-correlation attempt
open and supplies no estimate for the required complete I12.

## 5. Controls and outcomes

For the exact finite model U=sqrt(L) I_J and b=(W/sqrt(L))1, one has
G=L I_J, f=W1 and B=JW²/L. At v=W both inequalities in (1) are
equalities for every k; thus no intrinsic strict saving follows from the
finite interpolation alone. This real, nonnegative model is a control
for the algebraic enlarged class, not actual square-root coefficients.
If v>W there are no rows. If B=0 then f=0 and no positive high event
occurs. Singular matrices cause no difficulty since all powers are
nonnegative and finite; no inverse is used here. J=0 is trivial.
The localization ceiling, Gram diagonal and both distribution terms
are retained. Zero numerical experiments.

## 6. Dependencies and provenance

Conductor, round221, graph SHA256
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
protocol; accepted204 kernel Sections3--5; accepted216 masked-vector
binding; closed209 positive weighted-duality barrier; current isolated
briefs/blind_anchored_gram_statement.md. The chain identities and Holder
calculation above were independently derived by the conductor before
reading the isolated report. No current sibling report was used and no
external theorem was imported. The analytic/application seam is separate
from the isolated finite proof. Exact final-hash review is still required.

## 7. Recommended state effect

Retain as a scoped, quantitative closure control if reviewed. Do not
promote the full target or reject actual signed Gram chains. No graph
or exponent change is justified by this cost calculation. Require the
attack to estimate the fixed-vector endpoint/interior correlation before
the indicated ceiling step, or to close with no complete gain.
