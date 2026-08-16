# Round 82 synthesis

## Objective and outcome

Round 82 asked whether the transition-flattened chirped Kloosterman
energy closes the first upper-conductor residual band. It does not.
The round nevertheless isolates a strictly smaller exact survivor.

For every local class and alias, the globally smooth row is first split
into admissible residue progressions modulo \(4b\). Bourgain's accepted
reciprocal estimate proves that the entire same-residue energy and every
fixed nonzero residue-offset layer are target-safe throughout the band,
indeed through \(C\le J^{47/60}\). The only remaining smooth-main object
is the coherent sum across all nonzero residue offsets.

## Exact survivor

With \(B=C/T\), write

\[
 S_b=\sum_{r\in\mathscr R_{\kappa,b}}u(r)R(r),
 \qquad |R(r)|\ll_\varepsilon X^\varepsilon TQ^{-5/24}.
\]

Then

\[
 \sum_{b\asymp B}|S_b|^2
 =\sum_{b,r}|R(r)|^2+
 \sum_b\sum_{r\ne s}u(r)\overline{u(s)}R(r)\overline{R(s)}.
\]

The first term and every fixed \(s-r\ne0\) layer are

\[
 \ll_\varepsilon X^\varepsilon C^2Q^{-5/12}.
\]

The residual correlation is

\[
 \mathfrak X_C^{(\kappa,k)}=
 \sum_b\sum_{r\ne s}u(r)\overline{u(s)}R(r)\overline{R(s)},
\]

and the target remains

\[
 \mathfrak X_C^{(\kappa,k)}
 \ll_\varepsilon X^\varepsilon J^2/T.
\]

Absolute offset summation gives only

\[
 X^\varepsilon C^3/(TQ^{5/12}),
\]

whose excess is \(J^{1/12}\) at \(C=J^{3/4}\). A gain
\(B^{-1/2}\) reaches \(J^{56/75}\); a gain \(B^{-5/9}\) closes the first
band. These gains remain conjectural.

## Transform and source conclusions

In the odd class, finite Fourier analysis turns the nonzero offsets into
a product-Kloosterman correlation. Its zero frequency is exactly the
already safe same-residue mode. Complete stationary Poisson returns
the nonzero frequencies to the original nonzero-offset correlation, so
it is an involution rather than a gain.

The ordinary Kloosterman large sieve loses exactly \(B\). The current
Pascadi and Blomer--Pascadi bilinear theorems do not accept the literal
varying-modulus product kernel with its joint actual symbol. Matched
Kuznetsov--Voronoi returns to short coefficient windows of length \(T\)
and retains the \(X^{1/20}\) deficit. Its center is conductor-dependent,
not universally \(X/4\).

## State decision

Promote the exact residue-offset reduction, but no conductor extension.
Reject coefficient-blind, fixed-column, and involutive-transform
shortcuts. Keep `M9-M1`, `M9-M2`, `M9`, endpoint uniformity, and the
Gauss-circle exponent open.

The next target is signed cancellation across the nonzero residue
offsets with the exact local units and reciprocal weights retained.

