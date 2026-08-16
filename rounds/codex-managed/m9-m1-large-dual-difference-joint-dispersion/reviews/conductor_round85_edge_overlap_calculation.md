# Conductor Round 85 edge-overlap calculation

Campaign: `m9-m1-large-dual-difference-joint-dispersion`

Starting graph SHA-256:
`942453c8d45068875932507e8ca84ed87bcb2187ee141029a27eb0c0642bf60f`

Status: conductor candidate calculation pending the blind and hostile
gates.

## Candidate lemma

Let \(\mathscr N_b\) be the exact compact stationary support of the
phase-removed Round-84 principal profile for one class and orientation,
and put

\[
 \Delta_b=\sup\mathscr N_b-\inf\mathscr N_b\asymp Q^2.
\]

For

\[
 E_0=\lfloor J^{13/20}\rfloor,
\]

the main stationary contribution from the two edge families

\[
 \Delta_b-E_0\leq |d|\leq\Delta_b
\]

is \(O_\varepsilon(X^\varepsilon J^2/T)\), uniformly for
\(J^{13/18}<C\leq J^{3/4}\).  Differences with
\(|d|>\Delta_b\) have no main-main overlap.  The candidate conclusion
is useful only if the individual stationary errors and nonstationary
tails remain target-safe uniformly at these large shifts.

## Main-main calculation

For fixed \(d\), let

\[
 R_b(d)=\#\{n:n,n+d\in\mathscr N_b\}.
\]

On the edge family, \(R_b(d)\ll E_0\), and summing the overlap lengths
over either sign gives

\[
 \sum_{\Delta_b-E_0\leq |d|\leq\Delta_b}R_b(d)
 \ll E_0^2.
\]

Round 84 gives

\[
 \|\mathcal W_b\|_\infty\ll_\varepsilon X^\varepsilon H,
 \qquad H={C\sqrt T\over J},
\]

and exact Kloosterman residue Parseval gives

\[
 \sum_{r\bmod M}|A_{M,K,d}(r)|\leq2M^2.
\]

Partitioning an interval of \(R_b(d)\) integers into residue periods
therefore yields

\[
 {1\over M^2}\sum_n|A_{M,K,d}(n)|
 |\mathcal W_b(n+d)\mathcal W_b(n)|
 \ll_\varepsilon X^\varepsilon H^2
 \left(1+{R_b(d)\over M}\right).
\]

Since there are \(O(B)\) values of \(b\) and \(M\asymp B\), the whole
edge main is

\[
 \ll_\varepsilon X^\varepsilon H^2(BE_0+E_0^2).        \tag{85.C1}
\]

Write \(C=J^c\), \(13/18<c\leq3/4\).  Then

\[
 H^2=J^{2c-7/5}.
\]

For \(E_0=J^{13/20}\), the second term in (85.C1) is

\[
 J^{2c-7/5+13/10}=J^{2c-1/10}\leq J^{7/5},
\]

with equality only at \(c=3/4\).  The first term has exponent

\[
 (2c-7/5)+(c-3/5)+13/20=3c-27/20\leq9/10,
\]

and is smaller.  Moreover

\[
 \Delta_b-E_0\asymp Q^2=J^{4/5}>D_0=J^{17/30},
\]

so this deletes a genuinely new part of the exact Round-84 survivor.

## Error seam

The Round-84 conservative stationary remainder has normalized size
\(J^{-4/5+\varepsilon}\), versus normalized main size
\(J^{-1/10+\varepsilon}\).  If that pointwise all-support expansion is
used uniformly, absolute cross-error summation over \(O(E_0)\)
differences costs at most

\[
 X^\varepsilon B^2Q^2E_0J^{-9/10}
 \leq X^\varepsilon J^{17/20},
\]

at \(C=J^{3/4}\), and the error-error term is smaller.  The same
first-derivative tail hierarchy should own wrong-sign and exterior
indices.  Promotion requires the reports to verify that this uniform
pointwise interface, rather than only Round 84's small-shift sampled
product estimate, is an accepted dependency through both support
edges.

## Scope

This calculation gives no whole-offset \(B\)-saving and no conductor or
global-exponent improvement.  Even if certified, the middle range

\[
 D_0<|d|<\Delta_b-E_0
\]

remains the exact first-band smooth-principal obstruction.
