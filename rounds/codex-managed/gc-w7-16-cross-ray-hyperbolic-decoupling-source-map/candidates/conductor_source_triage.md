# Round 132 conductor source triage

Campaign: `gc-w7-16-cross-ray-hyperbolic-decoupling-source-map`

Starting graph SHA-256:
`328a885e71415a8e3509466c46849129248594334dc17df8940bbcd3f12a0fe9`.

## Decision

Freeze the broad/transverse interface at the primary source

- Ciprian Demeter and Shukun Wu, *Restriction and decoupling estimates for
  the hyperbolic paraboloid in R^3*,
  [arXiv:2505.09037v2](https://arxiv.org/abs/2505.09037), especially
  Definition 1.2, Definitions 1.3 and 1.9, and Theorems 1.6 and 1.10.

The literal top-shell phase

\[
 \Phi_i(u,v)=-\frac{cu}{\kappa_i v}
\]

has nonvanishing negative Hessian determinant of unit order when
\(c\asymp Y\) and \(v\asymp D=Y^{1/2}\). This makes the hyperbolic
paraboloid the closest of the three proposed source geometries. The source
also explicitly identifies rational rulings as the obstruction and requires
separation in both coordinates, matching the precise control exposed in
Round 131.

## Why the other interfaces are not frozen

- The Li--Yang global circle theorem and its repaired final exponent are
  already accepted as an external dependency in the graph. Its
  Guth--Maldague first-spacing input is not itself a map from the actual
  Round-131 fixed-centre scalar to the standard Bombieri--Iwaniec sum. A
  second audit of the record exponent would duplicate Round 95 rather than
  test the new residual.
- A Bombieri--Iwaniec continuation first needs a derived resonance vector
  and both spacing problems for the physical outer-ray/alias family. That is
  a distinct normal-form campaign, retained as the next eligible import
  test if this round closes without a margin.
- Round 131 proved that the literal completion is fixed-modulus-four
  Gauss-times-Ramanujan and that no growing unit inverse phase or Salie
  normal form is currently available. A modulus-aspect Kloosterman or trace
  theorem therefore lacks its first algebraic hypothesis.

## Frozen risk

Demeter--Wu gives bilinear integral inequalities for transverse frequency
patches. The project needs a signed linear scalar at one prescribed centre,
and its accepted aligned packets occupy narrow rational rulings. Round 132
must therefore establish all of the following before any gain is credited:

1. a scale-correct normalization of the ratio phase to the source surface;
2. a legal broad--narrow partition with the narrow part retained;
3. a fixed-centre bridge from the source norm, including localization cost;
4. literal coefficient norms after physical reassembly; and
5. a final exponent strictly below \(27/48\).

Failure at the first unavailable item is a source-level no-go, not a request
for another internal transform.
