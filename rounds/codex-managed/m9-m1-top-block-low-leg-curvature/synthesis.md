# Round 55 synthesis: the critical low-angular margin is target-safe

## 1. Conductor decision

Round 55 closes positively.  On the critical top radial block, every
polylogarithmic low-\(h\) margin is target-safe.  The apparent low-\(q\)
margin is empty on the actual angular support.  The intermediate-\(h\),
large-\(q\) core remains open, so there is no new global exponent yet.

## 2. Fixed-leg theorem

Let \(Y\asymp\sqrt X\), \(R\asymp\sqrt Y\), and let \(J\) be any
consecutive product window of length at most \(R\), including an edge
window.  With every floor, profile, angular star, and radial star retained,

\[
 \left|\sum_{n\in J}^{*}A_{X;H,Q}(n)n^{-3/4}e(\sqrt{Xn})\right|
 \ll_\varepsilon X^\varepsilon {H+Q\over\sqrt Y}.
\tag{55.1}
\]

The overlap is counted once by
\(\{h\le H\}\dot\cup\{h>H,q\le Q\}\).  Exact window propagation gives

\[
 |S_{Y;H,Q}|\ll_\varepsilon X^\varepsilon(H+Q).
\tag{55.2}
\]

## 3. Why the estimate is uniform

For a fixed leg \(\ell=h\) or \(q\), the complementary interval has
length \(O(R/\ell+1)\), and the square-root phase has curvature
\(\asymp\ell^2/R\).  The second-derivative estimate costs \(O(\sqrt R)\)
for \(\ell\le\sqrt R\); above that crossover, the trivial interval
length costs the same.  Restoring \(n^{-3/4}\) gives \(Y^{-1/2}\) per
leg.

On a length-\(R\) product window, the monotone angular coordinate changes
by relative size \(O(R/Y)\), so it meets only \(O(1)\) dyadic profiles.
Normalized profile variation, the Vaaler \(C^1\) bound, one height-floor
jump, the hard top, equality stars, and the radial star give the required
actual sampled-BV norm.  Integer and half-integer derivative resonances at
fourth powers do not affect the curvature proof.

## 4. Actual support and residual core

Active support forces

\[
 q\ge4h,\qquad q\ge2\sqrt n,\qquad h\le\sqrt n/2.
\tag{55.3}
\]

Thus any polylogarithmic low-\(q\) margin vanishes.  After removing
\(h\le(\log(2X))^B\), the exact survivor is

\[
 (\log(2X))^B<h\le\sqrt n/2\asymp\sqrt Y,
 \qquad q=n/h\ge2\sqrt n\asymp\sqrt Y.
\tag{55.4}
\]

Fixed-leg bounds summed through this whole range recover a
\(Y^{1/4}\)-scale loss.  Cancellation between distinct \(h\)-legs or
product fibers is therefore still required.

## 5. Rejected shortcuts

- A uniform first-derivative gap is false at fourth-power resonances.
- Summing the \(O(\sqrt R)\) bound over all remaining legs is not
  target-sized.
- The physical low-margin theorem does not automatically pass through
  the alpha mask, Plemelj connectors, or outside-height limits.

## 6. State effect

Promote a scoped top-block low-leg margin lemma.  Retain the full signed
correlation, GAR, alpha transition, M9-M1, M9, and the final target open.
No new Gauss-circle exponent is proved.

## 7. Next strategy

Freeze the intermediate-\(h\), large-\(q\) core in a length-\(R\) top
window.  The next useful test is a discrete-curvature resonance average:
after the odd-\(q\) split, derive a Weyl/completion bound that averages the
large fixed-\(h\) quadratic resonances over \(h\), with the actual angular
symbol retained.  Either obtain the missing \(\sqrt R\) aggregate bound or
exhibit an actual-profile resonance family showing that this route also
has full \(Y^{1/4}\) capacity.
