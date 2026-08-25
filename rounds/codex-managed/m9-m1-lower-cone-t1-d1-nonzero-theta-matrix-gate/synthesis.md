# Round 157 synthesis

- Campaign: m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate
- Starting graph: 3b48c540f7acc5b3e2886279f735072e6c66ee14704e77cd05c74fe24f7b39ea
- Terminal label: outer_defect_centered_discrepancy_no_go
- Graph mutation: applied
- Resulting graph: 3acbfaf6fb95047babd19800dee4152fb60cb408197a8ceac93931a20c57491f

## Outcome

Round 157 proves the exact centered physical form of the incomplete
nonzero theta projection:

\[
 \mathcal T_{\ne0,U}(V)=
 \sum_{V<|j|\le2V}\sum_{x\bmod4N}
 \left(B_j(x)-\frac{\widehat B_j(0)}{4N}\right)
 G_N(x^2-j).
\tag{157.Y1}
\]

The subtraction is exactly the single closed zero row.  Its constant
tail is global in \(x\), has zero sampled coefficient at every
nonzero mode, and is not discarded by a pointwise-smallness argument.

Writing \(c=4N/d\), \(H=c/2\), and \(n=N/d\), complementary nonzero
frequencies contribute

\[
 \left(\widehat B_j(2dv)+\widehat B_j(-2dv)\right)
 K(-v^2,-j;c),
 \qquad 1\le v<H/2.
\tag{157.Y2}
\]

The unique nonzero fixed point is \(v=H/2=n\).  Its full normalized row
is target-safe:

\[
 \boxed{
 \mathcal F_U(V)\ll_{\varepsilon,A}
 M^{-1/4}X^\varepsilon.}
\tag{157.Y3}
\]

This closes one nonzero theta row but not the paired interior matrix.

## Nyquist-fold proof

The literal zero-extended coefficient satisfies, for every fixed \(j\),

\[
 \sup_x|B_j(x)|+\operatorname {Var}_x(B_j)
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{157.Y4}
\]

Monotone profile sampling charges every component and transition.  The
exact residual phase has derivative \(O(V/K^2)\) on physical support,
whose span is \(O(KX^\varepsilon)\), and the asymmetric cell adds one
jump.  Hence complex Abel summation against \((-1)^x\) gives

\[
 C_j:=\widehat B_j(2N)
 =\widehat B_j(q/2)
 =\sum_x(-1)^xB_j(x)
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{157.Y5}
\]

After setting \(D_j=(-1)^jC_j\), crude variation costs at most
\(KM^{-3/4}X^\varepsilon\).  Opening the theta kernel produces the
nonzero additive frequency \(c/2-u\) for every unit \(u\bmod c\), so

\[
 \sup_I\left|
 \sum_{j\in I}(-1)^jK(-n^2,-j;c)
 \right|
 \ll c\log(2c).
\tag{157.Y6}
\]

Restoring \(d\sqrt c/(2Nq)\), summing every odd \(d\mid N\), and using
\(K=\sqrt{NM}\) proves (157.Y3).  This works for arbitrary \(N\),
including \(c=4\), both signed blocks, the complex phase, all
transitions, and strict endpoints.

The blind report's provisional support-sized Nyquist obstruction is
therefore superseded: its alternating diagnostic violates the inherited
spatial-BV hypothesis.  Its exact projector, complex orbit split, fold
normalization, and low-frequency warning remain valid.

## Corrected selected-incidence capacity

On the selected graph \(j=k^2-Nm\), the exact nearest cell is

\[
 k^2-k+1\le Nm\le k^2+k.
\tag{157.Y7}
\]

These integer intervals partition the positive integers as \(k\)
varies.  Each positive \(m\) determines one \(k\) and one \(j\).
Intersecting the \(O(M)\) physical support with the accepted
\(O_\varepsilon(VX^\varepsilon)\) root count gives

\[
 L_U(V)\ll_\varepsilon\min(M,V)X^\varepsilon.
\tag{157.Y8}
\]

A future genuine signed square-root theorem would therefore cost

\[
 M^{-3/4}L_U(V)^{1/2}X^\varepsilon
 \le M^{-1/4}X^\varepsilon
\tag{157.Y9}
\]

for every selected \(V\).  This corrects two stale Round 155 capacity
explanations.  It proves no signed incidence theorem and enlarges no
complete range.

## Qualified no-go results

The moving nearest-cell endpoint creates a diagonal atomic trace.
Consequently the accepted one-variable BV data do not imply the ideal
mixed rectangular norm; the control class has mixed absolute capacity
\(VM^{-3/4}X^\varepsilon\).

Elementary centered completion proves only

\[
 \sup_{I,J}|\mathscr D_N(I,J)|
 \ll \sqrt N\,\tau(N)(\log(2N))^2.
\tag{157.Y10}
\]

Even with the ideal mixed norm, this restores
\(N^{1/2}M^{-3/4}X^\varepsilon\), outside \(M\le N^{1/2}\).
The audited fixed-frequency, Fourier-\(L^1\), sampled-Parseval, and
generic operator/nuclear-norm placements retain their documented
positive powers.  These are method capacities, not lower bounds or
universal impossibility results.

The source audit finds no exact theorem through 25 August 2026 for the
fixed arbitrary even composite theta multiplier with the entrywise
coefficient \(\widehat B_j(2dv)\).  DFI gives the correct pointwise
kernel bound.  Current fixed-modulus bilinear theorems use other kernels
and separated weights; half-integral Kuznetsov formulas average moduli
and retain all spectral pieces.  This is a cutoff-dated interface
no-match.

## Remaining seam

The first open literal object is

\[
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c
 \sum_{1\le v<H/2}
 \left(\widehat B_j(2dv)+\widehat B_j(-2dv)\right)
 K(-v^2,-j;c).
\tag{157.Y11}
\]

It needs a joint mask-preserving signed theorem, or an exactly
equivalent selected signed incidence theorem, retaining the diagonal
cell trace, literal profile, complex phase, all odd divisors, signs,
transitions, endpoints, and the external scalar seam.

## Reviews and downstream status

The independent centered-mathematics, independent fold, hostile
profile/scope, independent source, and terminal State Patch scope
reviews are GREEN.  The patch review confirms the evidence polarity,
dependency directions, corrected all-\(V\) capacity, range quarantine,
and absence of a new graph cycle.

The fixed-polylogarithmic collar remains the last proved range for the
complete \(D=1\) wave.  Every \(D>1\), \(L>1\), generic \(t=1\),
original \(t\ge2\), cross, remaining M1, and M2 owner remains separate.
Endpoint uniformity, M9, and the unconditional bridge remain open.

The internally proved global exponent remains \(1/3\).  The separately
audited external Li--Yang exponent remains

\[
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\tag{157.Y12}
\]

No global exponent changes in Round 157.

## State effect

The validated State Patch creates one proved-internal centered/fold
node; updates eight obligations; corrects two stale rejected records;
rejects twenty-three new overbroad inferences; and records eight
principal downstream obligations unchanged.  The resulting graph is
3acbfaf6fb95047babd19800dee4152fb60cb408197a8ceac93931a20c57491f.
