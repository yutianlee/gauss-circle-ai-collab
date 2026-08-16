# Round 82 conductor adjudication

Campaign: `m9-m1-transition-flattened-kloosterman-energy`

Round: 82

Starting graph SHA-256:
`01333baabd40e4b9fb94aa16495fefdc5ec54e86fb56c43cada928ff55a9b835`

## Decision

Promote only the strict residue-offset reduction. Do not promote a new
conductor interval and keep the target energy open.

The three independent reports agree on the exact normalization and on
the obstruction:

- the ordinary Kloosterman large sieve loses exactly \(B=C/T\) in
  energy;
- the complete same-residue mode and every fixed nonzero residue-offset
  layer are separately target-safe;
- only coherent cancellation among the nonzero offset layers remains;
- complete Poisson, the one-variable \(B\)-process, and the matched
  Kuznetsov--Voronoi chain are involutive and return to the same row;
- the audited current bilinear Kloosterman theorems do not supply the
  required varying-modulus product-energy saving.

No numerical experiment is used.

## Promoted reduction

For \(J^{13/18}<C\le J^{3/4}\), the exact transition-flattened smooth
main splits as

\[
 \sum_{b\asymp B}|S_b|^2
 =\mathfrak D_{\rm res}+\mathfrak X_C^{(\kappa,k)},
\]

where

\[
 \mathfrak D_{\rm res}
 \ll_\varepsilon X^\varepsilon C^2Q^{-5/12}
 \ll_\varepsilon X^\varepsilon J^2/T,
\]

and every fixed nonzero offset layer of
\(\mathfrak X_C^{(\kappa,k)}\) satisfies the same bound. These bounds
hold in fact through \(C\le J^{47/60}\). The first exact survivor is

\[
 \mathfrak X_C^{(\kappa,k)}=
 \sum_{b\asymp B}\sum_{r\ne s}
 u(r)\overline{u(s)}R(r)\overline{R(s)},          \tag{82.A1}
\]

with the actual odd or even local units and the actual reciprocal
symbols retained. Absolute accumulation over all offsets has capacity

\[
 X^\varepsilon{C^3\over TQ^{5/12}},               \tag{82.A2}
\]

so a signed \(B^{-\delta}\) offset gain is the next required input.

## Blind and hostile gates

The statement-only report independently rederived the odd Poisson
normalization, stationary scale, coefficient mass, exact factor-\(B\)
deficit, small-shift disposal, and large-shift covariance. It did not
infer the absent even spectral formulas.

The source-hostile report checked the current versions of Pascadi
arXiv:2511.08445 and Blomer--Pascadi arXiv:2607.24311, the ordinary
Deshouillers--Iwaniec large sieve, and switched-cusp Voronoi. Their
literal hypotheses do not map to the varying-modulus product kernel with
joint actual symbol. The report also corrected the spectral center to a
finite conductor-dependent family. No external theorem is promoted.

## Rejected shortcuts

Reject the following upgrades.

1. A coefficient-blind Kloosterman large sieve uses the common chirp.
2. A fixed-modulus bilinear Kloosterman theorem applies with one long
   variable and one singleton and yields the full factor \(B\).
3. Pascadi's modulus-average theorem has common divisor \(B\); the
   actual common divisor is only \(4\).
4. A complete Poisson, \(B\)-process, or matched trace/Voronoi transform
   counts as a second saving after it reconstructs the original row.
5. The level-four spectral family has one universal dual center \(X/4\).
6. Target-safe fixed offset layers may be summed absolutely with no
   factor \(B\).

## State decision

Create one proved internal residue-offset reduction and attach it to the
residual upper-conductor node and `M9-M1`. Record the source and
self-return failures as rejected routes. Keep `M9-M1`, `M9-M2`, `M9`,
and `GC-target` unchanged.

The next round should attack (82.A1) directly. A gain \(B^{-1/2}\)
would extend the fixed-interior range to \(C\le J^{56/75}\); a gain
\(B^{-5/9}\) closes the entire first residual band. Neither gain is
currently proved.
