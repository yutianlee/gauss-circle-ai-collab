# Round 164 strategy: complete residual signed-divisor transport

## Conductor decision

Round 163 found the first literal target-safe incidence sector but did not
measure its density or its complement.  Round 164 should not repeat sector
mining.  It should freeze the complete residual

\[
 \mathcal S_{L,1}^{\mathrm{rem}}
 =\mathcal S_{L,1}-\mathcal S_{L,1}^{\mathrm{cp}}
\]

and decide whether all remaining within-product character cancellation
can be expressed and bounded through one exact one-dimensional transport
functional.

## Canonical transport formulation

For a fixed supported squarefree \(N\), let
\(\mathscr R_N\) be the residual odd divisors after the Round-163 XOR
sector is removed.  Split

\[
 \mathscr R_N^+=\{d\in\mathscr R_N:\chi_4(d)=1\},
 \qquad
 \mathscr R_N^-=\{d\in\mathscr R_N:\chi_4(d)=-1\}.
\]

Order each sign class by \(u=\log d\).  When the masses agree, the
monotone matching minimizes

\[
 \sum_i |\log(d_i^+/d_i^-)|.
\]

For unequal masses, the exact formula must retain the unmatched signed
mass.  Equivalently, with

\[
 F_N(u)=\sum_{\substack{d\in\mathscr R_N\\\log d\leq u}}\chi_4(d),
\]

discrete Stieltjes summation writes the residual coefficient as a boundary
term plus an integral of \(F_N\) against the derivative measure of the
literal zero-extended amplitude.  This formulation automatically exposes
hard jumps, profile variation, and sign imbalance.

The first quantitative gate is whether the sum over \(N\) of transport
cost, boundary crossings, and unmatched mass is
\(O_\varepsilon(L^{3/2}X^\varepsilon)\).  A proof closes the full
\(t=1\) face.  A lower-capacity result of order \(L^{2-o(1)}\) would be a
route no-go only: it would show that within-\(N\) positive transport
cannot work and that cancellation across \(N\) through
\(e(J\sqrt N)\) is mandatory.

## Mathematical interfaces

### Residual bookkeeping

The selector depends on \((N,L,\kappa)\) and may be absent.  The residual
contains:

- every product with no eligible selected pair;
- every incidence containing neither selected prime; and
- every incidence containing both selected primes.

The accepted XOR sector must be subtracted exactly once.  The even-\(N\)
branch and the odd character-bearing divisor remain unchanged.

### Profile and boundary measure

The amplitude contains the half-open product shell, the upper near-square
window, dyadic profile \(\eta_L\), \(\Phi(d/(H+1))\),
\(W(\sqrt{q_X}d/(2\sqrt N))\), cone restrictions, floors, stars,
endpoints, and zero extension.  The transport identity must use its full
variation measure rather than assuming global smoothness.

### Outer phase

Within each fixed \(N\), \(e(J\sqrt N)\) is constant and cannot help a
divisor matching.  If the aggregate transport norm exceeds target, the
phase must not be removed by a triangle inequality.  The discovery task
should then derive the smallest cross-\(N\) signed coefficient norm or
bilinear form that would use this oscillation.

### Capacity controls

Semiprime and multiprime families may falsify an optimistic transport
bound, but only after squarefreeness, residue classes, the upper window,
selector status, profile support, and weighted incidence multiplicity are
proved.  Raw counts are not physical lower bounds.  Any imported
prime-distribution theorem requires a primary-source card and an exact
hypothesis audit.

## Task decomposition

### 1. Complete residual transport attack

Derive the exact cumulative-discrepancy and monotone-coupling identities
for the literal residual.  Attempt the aggregate
\(L^{3/2}X^\varepsilon\) estimate.  If within-\(N\) transport fails,
retain the outer phase and isolate the exact cross-\(N\) theorem needed.

### 2. Statement-only rederivation

Starting from the frozen residual statement alone, reconstruct the
positive and negative divisor measures, unequal-mass correction, hard
boundary terms, and power ledger.  Prove a target result or identify the
first unavoidable missing estimate without importing the discovery
argument.

### 3. Hostile unmatched-mass audit

Test all claims that monotone matching is automatically cheap or nearly
balanced.  Build exact semiprime and multiprime controls, audit any
prime-distribution input, quantify the strongest legitimate capacity
statement, and prevent its promotion to a physical lower bound.

## Exit rule

Close under exactly one label:

- hard_top_t1_residual_target;
- strict_t1_residual_transport_sector; or
- hard_top_t1_residual_transport_no_go.

A successful strict sector must be owner-complete for a quantitatively
defined part of the residual.  Another arbitrary at-most-one matching is
not an admissible exit.  No conclusion transfers automatically to the
other few-point hard-TOP channels, BAL, UNBAL, M9--M2, M9--M1, endpoint
uniformity, M9, the bridge, the quarter target, or either exponent.
