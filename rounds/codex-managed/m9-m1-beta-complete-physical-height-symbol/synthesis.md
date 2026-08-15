# Round 32 synthesis: collapse boundary strata before defining the symbol

Campaign: `m9-m1-beta-complete-physical-height-symbol`  
Round type: common recombined physical-height kernel  
Graph SHA-256 before patch: `e53cc040c84e084cfa37f22c4a745080909deac6c510b61953eced488362f0b5`

## Conductor decision

Round 32 corrects the frozen target. A single pointwise
\(K_{\rm complete}(L,\nu)\) cannot include terminal verticals, radial
horizontal sides, and endpoint boundary functionals: they live on different
contour strata and have different normalizations.

The raw hard radial side begins with \(S^{-1}\), while the forced left-edge
degree-two factor has capacity \(S^{1-2\ell}\), \(\ell<0\). Its elementary
absolute capacity therefore grows like \(S^{-2\ell}\). It cannot satisfy a
uniform terminal \(\lambda^{-2}/\lambda^{-3}\) symbol bound.

The accepted remedy is architectural and exact:

1. subtract radial endpoints to arbitrary order and remove only the
   renormalized side under its nested-height theorem;
2. collapse the explicit endpoint and arithmetic boundary operator by the
   accepted finite Cauchy identity;
3. route the lower endpoint, physical upper endpoint, and recombined
   arithmetic residue to their already-proved modules;
4. define a side-collapsed, endpoint-image-free terminal beta kernel;
5. extract the full finite \(v=0\) vector residue, height connectors, and
   corner once;
6. impose the Round-31 weighted symbol bound only on the remaining
   axial-subtracted terminal kernel.

Under identical ownership,

\[
 \omega G+(1-\omega)R_1-\omega E_1=R_1,             \tag{32.1}
\]

so every rho Laurent/Taylor defect and every cutoff derivative cancels to
all orders. The missing seam is not rho regularity. It is the
mask-compatible endpoint/axial ownership identity, followed by the
axial-subtracted terminal weighted-symbol estimate.

Round 32 proves no complete beta estimate and uses no numerical experiment
or external theorem.

## Why the literal complete kernel is type-wrong

On a radial side \(w=\sigma\pm iS\), the hard endpoint expansion has

\[
 G_v(\sigma\pm iS)=O(S^{-1})+O(S^{-2}).             \tag{32.2}
\]

Against the left-edge functional-equation capacity, this gives

\[
 O(S^{-2\ell}),\qquad \ell=1-c'<0.                 \tag{32.3}
\]

Faster nesting worsens (32.3). The accepted arbitrary-order endpoint
subtraction writes \(G_v=E_{M,v}+R_{M,v}\); for \(M>-2\ell\), the
renormalized side from \(R_M\) vanishes under polynomial nesting. The
explicit endpoint functional \(E_M\) remains and is collapsed by the
finite Cauchy identity, not estimated as a terminal \((L,\nu)\) symbol.

The accepted \(M=1\) identity is

\[
 T_\xi+S_\xi+P_\xi=D_\xi-A_\xi.                   \tag{32.4}
\]

The artificial \(R_1\) residue cancels \(P_\xi\), and the arithmetic
shares recombine to the physical \(R_1\) residue. The graph already proves
the resulting lower endpoint, physical upper endpoint, and recombined
arithmetic residue are target-safe. Reinserting them into a local beta
symbol would double count them.

## Exact rho scope

Let all three radial pieces have the same beta mask, finite domain,
endpoint convention, diagonal subtraction, and residue ledger. Then (32.1)
holds as a meromorphic identity. For every compatible integer \(k\ge0\),

\[
 D^k\{\omega G+(1-\omega)R_1-\omega E_1\}=D^kR_1. \tag{32.5}
\]

Every coefficient of an omega derivative is a derivative of
\(G-E_1-R_1=0\). Consequently all artificial rho Laurent/Taylor
coefficients and cutoff derivatives cancel to all orders.

The blind report identifies what happens when ownership is not common. If

\[
 \mathcal E_{\rm own}=mathcal H_G-mathcal H_{E_1}
 -\mathcal H_{R_1},                                  \tag{32.6}
\]

then the first missing datum is its rho-constant coefficient
\(\mathcal E_{\rm own}(0;L,\nu)\), followed by its physical
\(L\)-derivative. The proper compatibility theorem must prove these defects
vanish after every mask, side, endpoint star, and connector is assigned.

## Axial vector seam

The height transform has the local polar form

\[
 f_b(\nu)=\frac1{b+i\nu}+f_b^\circ(\nu).            \tag{32.7}
\]

Its polar L1 norm is logarithmic, but its differentiated absolute norm is
\(\asymp b^{-1}\). This confirms that the physical-height derivative at
fixed \(\nu\) is the correct interface, yet local subtraction in (32.7)
is not the full contour operation.

When the finite \(v\)-line is moved, the exact residue is a vector
coefficient and must also be taken on the radial sides and arithmetic
pieces; the \(u=0\) share and joint corner are counted once, and finite
height horizontals remain. Therefore Round 32 does not promote an
axial-subtracted kernel definition until this connector-completed finite
identity is matched to the beta mask and endpoint collapse.

## Correct reduced target

After mask-compatible endpoint collapse and exact axial extraction, define
the side-collapsed terminal remainder \(K_{\rm term}^\circ(L,\nu)\). The
remaining analytic estimate is

\[
 |K_{\rm term}^\circ(L,\nu)|
 \ll X^\varepsilon\lambda^{-2}w(\nu),
 \qquad
 |\partial_LK_{\rm term}^\circ(L,\nu)|
 \ll X^\varepsilon\lambda^{-3}w(\nu),               \tag{32.8}
\]

with \(w\in L^1\) and polylogarithmic norm. The Round-31 finite-section
lemma would then give the regular terminal BV bound, and the accepted
stationary numerator would preserve local \(q^{-2}\).

Equation (32.8) is proved only on separated fixed-\(b\) \(R_1\) patches.
It remains open for the connector-completed, axial-subtracted reduced
terminal kernel and its height tails.

## Evidence assessment

- The blind report independently proves the separated kernel and identifies
  the rho-zero ownership defect as the first missing definition datum.
- The hostile audit proves the contour-stratum/type obstruction, raw side
  capacity, all-order rho cancellation, axial norm distinction, and the
  correct two-module architecture.
- The discovery report was conductor-materialized after a timebox and is
  not independent validation.
- The conductor independently audited the accepted endpoint Cauchy and
  boundary modules, reduced-kernel ownership, axial norm, and vector residue
  ledger.

The promoted facts below rest on accepted prior modules, hostile/blind
agreement, and conductor verification—not on the materialized report.

## State effect

- reject an all-inclusive pointwise terminal symbol containing radial sides
  and endpoint boundary operators;
- promote all-order rho/cutoff cancellation under identical ownership;
- promote the architectural reduction: radial side removal and endpoint/
  arithmetic modules precede the local terminal symbol;
- create a mask-compatible endpoint/axial compatibility obligation;
- create the axial-subtracted, side-collapsed terminal symbol bound (32.8)
  as the next open analytic lemma;
- retain the complete regular-symbol BV target, beta transition,
  double-bounded share, alpha branch, M9-M1, M9-M2, M9, and Gauss target as
  open.
