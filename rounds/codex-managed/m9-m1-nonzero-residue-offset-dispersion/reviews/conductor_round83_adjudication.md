# Round 83 conductor adjudication

Campaign: `m9-m1-nonzero-residue-offset-dispersion`

Round: 83

Starting graph SHA-256:
`abbec651f0dc76e3e15408ce7fce76700aee01652d88db261d84f83815bdb112`

## Decision

Promote the exact all-class inverse-unit normalization and the
target-safe removal of the literal dual difference (d=0).  Do not
promote a (B)-power saving or a new conductor interval.

The round replaces the raw coherent nonzero residue-offset energy by the
strictly smaller centred correlation

\[
 \mathfrak Y_C^{(\kappa,k)}
 ={1\over M^2}\sum_{b\asymp B}\sum_{d\ne0}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)},                              \tag{83.A1}
\]

with (M\in\{4b,2b,b\}), the exact class-dependent inverse unit, and
the full actual Fourier weights.  No stationary truncation or arbitrary
coefficient replacement occurs in (83.A1).

## Promoted facts

1. After (c=g_\kappa x), all three local classes have an ordinary
   inverse unit (e_{M_\kappa}(K_\kappa\bar x)).  The two even formulas
   are derived separately from (bs_0+\rho=tc).
2. Finite orthogonality identifies (a=0) with the same-residue mode
   already removed in Round 82.
3. The literal integer slice (d=0) inside the remaining (a\ne0)
   energy is target-safe.  A theorem-free bound is
   (O_\varepsilon(X^\varepsilon B^2C)); the standard complete-sum bound
   sharpens it to (O_\varepsilon(X^\varepsilon BC)).
4. Complete offset Fourier transformation and inversion are exact
   self-returns in all three local classes.

## Blind and hostile gates

The statement-only report independently verifies the residue-offset
one-count, odd inverse phase, rational completion, prime-power gcd
degeneracies, and the factor-(B) target ledger.  It correctly proves
that a pointwise square-root bound uniform in the offset is false at
prime powers, while leaving a gcd-sensitive aggregate possible.

The hostile/source report verifies the exact rank-one all-offset
self-return and audits the current trace-function, Kloosterman-product,
incomplete-inverse, and varying-modulus dispersion theorems.  None accepts
the literal composite modulus family and joint actual row.  It also
isolates the odd wrap offset (a=q/2) as constant but target-safe.

The conductor independently checks the two even units, Poisson
normalization, sampled Parseval identity, derivative scale, and target
ledger in `conductor_round83_dual_normalization.md`.

## Rejected shortcuts

Reject the following upgrades.

1. A uniform pointwise square-root bound for every rational complete sum
   and composite offset.
2. A coefficient-blind trace estimate implies cancellation for the
   actual row.
3. A square-root average over the (O(B)) offsets closes the full band;
   it reaches only (C\le J^{56/75}).
4. Complete offset Fourier transformation supplies a (B)-saving after
   its inverse reconstructs the original row.
5. The residue-diagonal (a=0), the literal dual difference (d=0), and
   nonzero multiples (d\equiv0\pmod M) are the same object.
6. Odd local-unit algebra may be copied to the two even classes without
   their exact rescaling.

## State decision

Create one proved-internal dual-difference reduction and attach it to the
upper-conductor residual node and `M9-M1`.  Keep the centred (d\ne0)
correlation, every (B^{-\delta}) gain, all conductor extensions,
`M9-M1`, `M9-M2`, `M9`, and `GC-target` open.

The next round should analyze (83.A1) before absolute values, using the
stationary shape of (I_b(n+d)\overline{I_b(n)}), and must preserve the
existing (Q^{-5/12}) row saving.
