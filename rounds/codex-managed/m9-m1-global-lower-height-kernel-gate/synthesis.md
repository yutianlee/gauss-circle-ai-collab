# Round 121 synthesis: exact lower-cone discrepancy reduction and pairing no-go

Campaign: `m9-m1-global-lower-height-kernel-gate`

Starting graph SHA-256:
`54f1c4ffd3a4ec9f166773ddb5f013a2fc7028b0a2586709f7379116a92da974`

Resulting graph SHA-256 after the validated State Patch:
`3e85caebbaf6c69d0019009bee3ce8f720f34f579bfb0cfa2035b92be0fb2c13`

## Frozen objective

The round asked whether summing the exact denominator profiles before any
norm and then pairing the period-four character produces a target-safe
joint height inequality for the complete lower-radial reciprocal
antecedent.  It also required the smallest exact survivor if the pairing
did not close.

The pairing does not close.  The round nevertheless proves a new global
reduction: the entire floor-perturbed lower profile is target-equivalent to
one flat sharp denominator cone and then to a prescribed-centre truncated
character-divisor discrepancy.

## New target-scale equivalence

Put \(R=X^{1/4}\), \(y=\lfloor\sqrt X\rfloor\),
\(D_j=2^{-j}y\), and \(H_j=\lfloor D_j/R\rfloor\).  Choose the fixed
lower cutoff sufficiently small relative to the certified fixed inactive
bottom support.  The exact positive reciprocal antecedent is

\[
 \mathcal B_{\rm low}^+
 =\sum_j\sum_{h\leq H_j}{\Phi(h/(H_j+1))\over h}
 \sum_d\chi_4(d)w_j(d)
 V_{\rm low}(4R^2h^2/d^2)e(hX/d).
\]

On the lower support, profile geometry forces \(h\leq H_j\),
\(h/(H_j+1)<1/2\), and exclusion of the inactive bottom.  Thus replacing
\(\Phi\) by one makes the active profiles telescope exactly to
\({\bf1}_{d\leq y}\).  The remaining \(\Phi-1\) error has a quadratic
height factor.  A uniform high-regularity two-variable Fourier separation,
together with the accepted frequency-first theorem, proves

\[
 \boxed{\mathcal B_{\rm low}^{\pm}
 =\mathcal B_{\rm flat}^{\pm}+O_{\varepsilon}(RX^\varepsilon),}
\]

where

\[
 \mathcal B_{\rm flat}^+
 =\sum_{d\leq y}\chi_4(d)\sum_{h\geq1}{1\over h}
 V_{\rm low}(4R^2h^2/d^2)e(hX/d).
\]

This covers the full lower cutoff, not only the earlier small-angle sector.
The transform normalization remains
\(\mathcal B_{\rm low}^+=(e(1/8)/i)R G_{\rm low}+O(\log^2X)\), so the
reciprocal target is \(RX^\varepsilon\).

Let \(N=\lfloor X\rfloor\), changing only the phase.  Absolute summation
gives

\[
 \mathcal B_{\rm flat}^+(X)
 =\mathcal B_{\rm flat}^{(N)}(X)+O(R).
\]

With the explicit sample-exact periodic interpolant

\[
 J_{R,y}(t)=\eta(yt){V_{\rm low}(4R^2t^2)\over t},
\]

define

\[
 A_y(m)=\sum_{\substack{d\leq y\\d\mid m}}\chi_4(d),
 \qquad c_y=\sum_{d\leq y}{\chi_4(d)\over d},
\]

for all integers \(m\), with \(d\mid0\), and

\[
 D_N(k)=\sum_{d\leq y}\chi_4(d)
 \left(\left\lfloor{N+k\over d}\right\rfloor
 -\left\lfloor{N\over d}\right\rfloor-{k\over d}\right)
 \quad(k\in\mathbb Z).
\]

Discrete Fourier completion and exact two-sided Abel summation give

\[
 \boxed{
 \mathcal B_{\rm flat}^{(N)}(X)
 =\sum_{k\in\mathbb Z}D_N(k)
 \{\widehat J_{R,y}(k)-\widehat J_{R,y}(k+1)\}.}
\]

This is a bidirectional equivalence at the target scale.  The raw
seminorms of \(J_{R,y}\) grow with \(y\); fixed-\(X\) Schwartz decay is
only an exact-convergence device, not a uniform estimate.

## Exact pairing and obstruction

After finite profile-first aggregation and zero extension, adjacent odd
denominators give

\[
 \mathcal B_{\rm low}^+=\mathcal E_{\rm amp}+\mathcal K_X,
 \qquad \mathcal E_{\rm amp}\ll\log^2X,
\]

with

\[
 \mathcal K_X=\sum_{d\equiv1(4)}\sum_h{b_X(h,d+2)\over h}e(hX/d)
 \left\{1-e\!\left(-{2hX\over d(d+2)}\right)\right\}.
\]

The flat amplitude seam is \(O(\log X)\).  Thus the phase kernel is
target-equivalent to the original lower antecedent.  The very narrow
integer-increment sector is target-safe, but the complementary
half-integer resonances are not small.

For fourth powers \(X=R^4\), disjoint resonance tubes with
\(d\asymp R^2\), \(R^{4/5}\leq h\leq cR\), and
\(2hX/(d(d+2))\) near a half-integer satisfy

\[
 \sum_T|\mathcal K_X[T]|\gg R^{3/2}.
\]

This exceeds the \(RX^\varepsilon\) budget and occurs at and above the
\(n=X^{2/5}\) interface.  It rules out termwise, pairwise, and
resonance-tubewise absolute closure.  Cancellation across heights and
resonance labels is still possible, so this is not a signed lower bound.

## Repairs and report reconciliation

All three independent audits accept the target-scale equivalence after two
repairs:

1. use a uniform smooth weighted Fourier/Wiener norm, not the false claim
   that two-dimensional \(C^1\) regularity gives absolute summability;
2. choose the cutoff relative to the certified fixed bottom-support
   constant, rather than invoking an uncited numerical edge.

They also verify the hard sample, floors, both signs, Fourier sign
\(N+k\), the convention \(d\mid0\), the all-integer floor formula, and
the Abel shift.  The exact discrepancy is a sharp global version of the
Round-64/65 unmatched-crossing return, not a new inequality.

## Decision and proof status

Round 121 promotes the full-profile flattening/integerization/discrepancy
equivalence and the scoped mod-four resonance-tube no-go.  It closes this
local pairing mechanism and replaces the lower GAR research target by one
precise global signed functional.

The lower-radial estimate and GAR remain open.  Even GAR would control the
total active M1 aggregate, not either direct blockwise M1 parent.  M9-M2
still needs its independent hard TOP, balanced, and unbalanced estimates;
endpoint uniformity and the final bridge remain separate.  The internal
pointwise exponent stays \(1/3\), and the audited external benchmark stays

\[
 {3292+25\sqrt{1717}\over13762}
 =0.3144831759740614\ldots .
\]

No quarter-scale Gauss-circle proof or exponent improvement is claimed.
