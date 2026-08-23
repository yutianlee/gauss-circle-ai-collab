# Conductor review: literal divisor-progressive aliases and aggregate errors

Campaign: m9-m2-balanced-nonzero-alias-defect-gate

Decision: pass after replacing the clean (d=1) model by the literal
divisor-progressive chart. This is a reduction, not the target estimate.

## 1. Gcd progression and character

For the exponential part of the double-far energy, write

\[
 h'=h+2s,\qquad k'=k+q.
\]

The parity identity is exact:

\[
 \chi_4(h)\chi_4(h+2s)=(-1)^s.
\]

Expand the second low-gcd mask as

\[
 \eta((h',k')/G_0)
 =\sum_{d\mid h',\ d\mid k'}\gamma_d.
\]

Only odd (d) occur. If (s_d\pmod d) is the unique residue satisfying
(h+2s_d\equiv0\pmod d), then

\[
 s=s_d+dt,\qquad h'=d(\ell_d+2t),\qquad
 \ell_d={h+2s_d\over d},
\]

and, because (d) is odd,

\[
 (-1)^s=(-1)^{s_d}(-1)^t.
\]

Thus the lawful one-variable transform is Poisson summation in (t), not
unrestricted Poisson summation in (s). For dual frequency (m\in\mathbb
Z), put

\[
 \mu={1\over2}-m,\qquad \lambda={\mu\over d}.
\tag{116.R1}
\]

The lift label ((d,\mu)) cannot be reduced to the rational number
(lambda): different lifts carry different (gamma_d) and progression
residue phases.

## 2. Finite Poisson legality and aggregate errors

For fixed ((h,k,k',d)), the literal support and the two affine far gates
split the accepted (t)-integers into (O_B(1)) consecutive runs. Surround
each run by half-integer endpoints and continue the fixed smooth symbol over
the two end half-cells. This leaves every integer coefficient unchanged and
gives a bounded-variation amplitude with the frozen rescaled derivative
bounds.

Finite Poisson summation on each run is exact with symmetric dual
summation. The half-integer endpoints make the leading boundary Fourier
tails alternating; after those tails are grouped before absolute values,
summation by parts gives (O_B(1+\log(2+dL^3))) for all nonstationary
modes on one progression component. Modes whose stationary point is within
one Fresnel width of an endpoint are kept as incomplete stationary
integrals. There are (O(dL)) such modes per endpoint and each has size
(O((dL)^{-1})). For an interior mode the stationary-phase remainder is
(O((dL^3)^{-1})); summing it over (O(dL^3)) modes again costs (O(1)).

Finally,

\[
 \sum_{d\mid k'}|\gamma_d|\ll_\varepsilon X^\varepsilon.
\]

There are (O(L^3)) outer triples ((h,k,k')). Therefore the complete
boundary, support-crossing, nonstationary, transition, and interior
stationary-error package is

\[
 O_\varepsilon(L^3X^\varepsilon).
\tag{116.R2}
\]

This estimate uses no aliaswise absolute value on the stationary bulk.

## 3. Stationary chart and exact phase

At an interior stationary point (x=h'),

\[
 \lambda=R\sqrt{k'/x},\qquad x={Xk'\over\lambda^2}.
\tag{116.R3}
\]

The active (lambda)-interval has length (asymp L^3) and spacing
(1/d), so it contains (asymp dL^3) lifted aliases. The second
derivative in (t) is (asymp d^2L^2), hence the stationary amplitude
is (asymp(dL)^{-1}). The square mass

\[
 (dL^3)(dL)^{-2}\asymp L/d
\]

matches the (L/d) points of the primal progression.

The phase, including the residue term, is

\[
 \Psi_d
 =R\sqrt{hk}-{Xk'\over2\lambda}-{\lambda h\over2}
 +s_d\left({1\over2}-\lambda\right).
\tag{116.R4}
\]

With (lambda_0=R\sqrt{k/h}) and (q=k'-k), direct expansion gives

\[
 \Psi_d
 =-{h(\lambda-\lambda_0)^2\over2\lambda}
  -{Xq\over2\lambda}
  +s_d\left({1\over2}-\lambda\right).
\tag{116.R5}
\]

The clean conductor formula without the last term is therefore only the
(d=1) bulk model.

## 4. Literal images of both gates

Put (lambda_r=Rk'/\sqrt{hk}). At (116.R3), the two determinant
coordinates are exactly

\[
 \rho=hk'-xk
 ={hk'\over\lambda^2}(\lambda^2-\lambda_0^2),
\tag{116.R6}
\]

\[
 \Delta=xk'-hk
 ={hk\over\lambda^2}(\lambda_r^2-\lambda^2).
\tag{116.R7}
\]

On critical support, each strict width-(L) corridor deletes only an
(O(L^2))-wide interval in (lambda), hence (O(dL^2)) of the
(asymp dL^3) aliases. The relation

\[
 \Delta+\rho=q(h+x)
\]

is exact, so the two projectors may not be replaced by independent
averages.

## 5. Exact reduction and first open step

Let (mathcal K_B) denote the fully signed finite-Poisson stationary
kernel of the discovery report: it retains (h,k,k',d,mu), both gates,
both literal symbols, (gamma_d), and the residue phase (116.R4), with
incomplete Fresnel factors at every transition. Then (116.R2) gives

\[
 \mathcal R_B^{\mathrm{osc}}
 =\mathcal K_B-M_B^{(0)}
  +O_\varepsilon(L^3X^\varepsilon).
\tag{116.R8}
\]

The phase-free term (M_B^{(0)}) is the accepted Round-115 owner and is
used exactly once. Consequently the first unproved estimate is the bulk
bound

\[
 |\mathcal K_B^{\mathrm{bulk}}|
 \ll_\varepsilon L^3X^\varepsilon.
\tag{116.R9}
\]

No report proves (116.R9).

## 6. Review decision and scope

Promote the exact divisor-progressive alias reduction and its target-safe
aggregate error package. Reject the divisor-independent half-integer grid,
merging equal rational aliases, and any stationary formula that drops the
residue, gates, or endpoint package.

Retain the oscillatory remainder, actual double-far energy, balanced
packet, hard TOP, unbalanced M2, both M1 parents, endpoint uniformity, M9,
and every global exponent claim as open.

Evidence:

- rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/reports/blind_half_shift_alias_rederivation.md
- rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/reports/literal_alias_local_energy_attack.md
- rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/reports/alias_large_sieve_hostile_audit.md
- rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/controls/conductor_round116_prechecks.md
