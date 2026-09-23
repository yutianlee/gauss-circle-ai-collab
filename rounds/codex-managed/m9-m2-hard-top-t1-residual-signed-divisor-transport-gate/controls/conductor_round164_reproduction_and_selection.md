# Round 164 conductor reproduction and kernel selection

- Campaign: `m9-m2-hard-top-t1-residual-signed-divisor-transport-gate`
- Starting graph:
  `81690ebb72b0dedd99bdb6c6127f947df696a901a22af3f65ac8738209125306`
- Resource use: 100% analytic/algebraic; 0% numerical
- Terminal decision: `hard_top_t1_residual_transport_no_go`

## Selected smallest kernel

The selected kernel is the exact residual Boolean and character-mass
algebra, the zero-extended Abel/BV dual identity, the selector-robust
coefficient-uniform positive-transport obstruction, and the endpoint-exact
length-\(L\) sliding Fejer reduction.  It is recorded in
`proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md`.

The kernel proves no residual estimate.  Its graph-changing content is a
rigorous route no-go together with the first exact affirmative theorem that
would bypass that no-go.

## Independent algebraic reproduction

For a selected pair, the residual indicator is

\[
 1-\mathbf1_{p\mid d}-\mathbf1_{q\mid d}
 +2\mathbf1_{p\mid d}\mathbf1_{q\mid d},
\]

so XOR and residual partition every odd divisor once.  Multiplicativity
gives zero selected residual sign mass.  With no pair, the sign mass is
\(\prod_{r\mid M_N}(1+\chi_4(r))\), which is zero if a \(3\pmod4\)
prime occurs and \(2^{\omega(M_N)}\) otherwise.  Thus ambient balance is
not universal and, even where it holds, does not locate the signs inside
the physical divisor window.

For ordered residual signs and amplitudes, direct coefficient collection
gives

\[
 b_N=C_ra_r+\sum_{j<r}C_j(a_j-a_{j+1})
 =-\sum_{j=0}^{r}C_j(a_{j+1}-a_j).
\]

Because the zero-extended increments sum to zero, subtracting
\((\max C+\min C)/2\) gives

\[
 |b_N|\leq\frac12\operatorname{osc}(C_N)V_N.
\]

This formula includes unequal mass without assigning a fictitious metric
cost to an arbitrary cemetery location.  The literal profile has
\(V_N\ll1\); no \(L^{-1/2}\) factor remains after the XOR sector has been
removed.  Its direct BV/triangle target is the weighted quantity
\(\sum_N\operatorname{osc}(C_N)V_N\).  The unweighted sum is only the
envelope for a theorem uniform over all profiles with bounded variation.

## Hostile capacity reproduction

Take four distinct odd primes of scale \(P\asymp\sqrt L\), two in each
odd residue class modulo four, in one sufficiently short fixed relative
interval.  The three physical two-prime partitions have signs
\(\{+,-,-\}\).  With no selector the unit-profile residual is \(-1\).  If
an opposite-character pair is selected, two partitions are XOR and the
remaining neither/both partition is negative, so the residual is still
(-1).

The fixed-\(q=4\) source card gives \(\gg P/\log P\) primes in each
required box.  Unique factorization yields
\(\gg L^2/(\log L)^4\) diagnostic products.  This rejects any
coefficient-uniform target theorem based only on sign mass, monotone
transport, bounded variation, finitely many hard faces, and positive
collar counting.  It is not a lower bound for the actual profile or the
oscillatory scalar.

## Fejer and power reproduction

For zero-extended \(z_N=c_N^{\rm rem}e(J\sqrt N)\), set

\[
 \mathfrak E_R=\frac1R\sum_s
 \left|\sum_{j=0}^{R-1}z_{s+j}\right|^2.
\]

Each pair at gap \(r<R\) occurs in \(R-r\) sliding windows, giving the
exact Fejer weights.  Every coefficient occurs in \(R\) windows, while
only \(M_L+R-1\) windows can be nonzero.  Hence

\[
 \left|\sum_Nz_N\right|^2
 \leq\frac{M_L+R-1}{R}\mathfrak E_R.
\]

With \(M_L\asymp L^2\), \(R\asymp L\), and
\(\sum_N|c_N^{\rm rem}|^2\ll_\varepsilon L^2X^\varepsilon\), the
diagonal contributes \(L^3X^\varepsilon\).  Thus the exact remaining
claim is the one-sided aggregate real-part bound

\[
 \Re\sum_{1\leq r<R}\left(1-\frac rR\right)
 \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(\frac{Jr}{\sqrt{N+r}+\sqrt N}\right)
 \leq C_\varepsilon L^2X^\varepsilon.
\]

Opening the coefficients gives \(d'm'-dm=r\) with \(1\leq r<L\), both
selectors, both parity branches, both literal profiles, and both
squarefree conditions.  Shiftwise absolute values are neither required
nor admissible as a free reduction: they leave a positive additive-shift
form and destroy the signed aggregate.  The accepted multiplicative
rank-one collar is a separate missing-power warning, not the same geometry.

## Source and literature controls

The Bennett--Martin--O'Bryant--Rechnitzer input is confined to fixed
relative-length intervals modulo four and is documented in
`sources/bennett_martin_obryant_rechnitzer_2018.md`.  It is not used for
the shrinking selector window.

The dated literature scan in
`controls/conductor_round164_updated_literature_scan.md` identified no
newer classical pointwise exponent or theorem whose audited hypotheses
imply the residual short-shift estimate.  This is a scoped search result,
not a theorem that no such result exists.

## Control matrix

| Control | Reproduced outcome |
|---|---|
| residual subtraction | Green: exact Boolean complement of XOR. |
| odd/even branch | Green: the character divisor stays odd and the factor \(2\) stays on the complementary leg. |
| sign mass | Green: exact selected/no-pair dichotomy. |
| Abel and hard endpoints | Green: zero-extended discrete identity; full-line regulated form has no extra terminal term. |
| unequal mass | Green: sharp BV dual form; no free cemetery. |
| literal variation | Green: fixed smooth profiles and finitely many hard faces give \(V_N\ll1\). |
| positive transport | Rejected as a coefficient-uniform target route; no physical lower bound. |
| source hypotheses | Green for fixed \(q=4\) and fixed relative boxes only. |
| outer phase | Green: retained in the sliding correlations. |
| Fejer endpoints | Green: exactly \(M_L+R-1\) possible windows and no endpoint error. |
| target power | Green reduction, open estimate: \(R\asymp L\) is the first diagonal-safe scale. |
| rank-one collar | Green route comparison only. |
| downstream scope | Green quarantine. |
| computation | Not used. |

## Selection decision

Promote one reduction node only after all three independent seam reviews
are green.  Attach it as inconclusive evidence to the two open hard-TOP
parents.  Keep the residual target and every downstream theorem open.  The
next research objective is the actual residual short-shift energy, not
another within-product matching.
