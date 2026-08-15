# Conductor adjudication: lower-radial phase diagram

Campaign: m9-m1-lower-radial-phase-diagram  
Round: 61  
Decision: promote the exact phase-diagram reduction; promote no new estimate.

## 1. Accepted result

Put \(N=X^\nu\), \(D=X^\delta\), and \(L=X^\ell\).  The stationary
identity
\[
 n=\frac{4Xh^2}{d^2}
\]
gives
\[
 \ell=\delta+\frac{\nu-1}{2},\qquad
 \frac{1-\nu}{2}\leq\delta\leq\frac12.
\]
The lower endpoint is a bounded-frequency layer and is interpreted with
the exact floors and support constants.

The accepted TTY region becomes
\[
 1816\delta+89\nu\leq552.
\]
It first meets the active interval at
\[
 (\nu,\delta,\ell)=
 \left(\frac{356}{819},\frac{463}{1638},0\right),
\]
but this is only the onset of partial scale coverage.  The terminal
theorem is exactly \(\nu=1/2\), while the V2 target point is exactly
\((\nu,\delta)=(0,1/2)\).  Therefore the accepted menu closes every
active denominator scale only for \(\nu=0\) and \(\nu=1/2\).
Every \(0<\nu<1/2\) retains the actual hard-top block
\[
 (\delta,\ell)=\left(\frac12,\frac{\nu}{2}\right).
\]

## 2. Exact residual and saving ledger

For \(0\leq\nu<1/2\), the residual set is
\[
 \mathcal U_{\rm rad}=
 \left\{(\delta,\nu):
 \frac{1-\nu}{2}\leq\delta\leq\frac12,\quad
 1816\delta+89\nu>552\right\}
 \setminus\left\{\left(\frac12,0\right)\right\}.
\]
The exact power above the \(X^{1/4}\) target for the best accepted
blockwise menu is
\[
 \sigma_*(\delta,\nu)=
 \min\left\{
 \frac{1-2\nu}{4},\
 \frac{1816\delta+89\nu-552}{2564},\
 \delta-\frac14,\
 \frac{\nu}{4}
 \right\}.
\]
At the hard top this reduces to
\[
 \sigma_{\rm top}(\nu)=
 \min\left\{\frac{\nu}{4},\frac{1-2\nu}{4}\right\},
\]
with crossover at \(\nu=1/3\).

## 3. Evidence reconciliation

The discovery, statement-only rederivation, and hostile/source audit
independently agree on the stationary map, active interval, TTY
substitution, exact contact rational, endpoint ownership, and all-scale
no-go.  The blind report was corrected during the round to retain the
global V2 deficit.  The final three reports agree on the four-term
best-menu ledger above.

No report proves cancellation on \(\mathcal U_{\rm rad}\).  In
particular, projection of the TTY-covered set onto the \(\nu\)-axis
cannot be substituted for coverage of every contributing denominator
scale.

## 4. Controls

- Stationary map and inequality directions: pass.
- Active support, floors, and bounded-height boundary: pass.
- Terminal, TTY, and V2 translations: pass.
- Union over denominator scales: pass.
- Mellin multiplier and transform-error stability: pass.
- Hard top, profiles, and stars: retained.
- Required saving: pass after inclusion of V2.
- Downstream implication: intentionally fails; no new bound is proved.

## 5. State decision

Create a proved-internal reduction node
M9-M1-lower-radial-phase-diagram.  Add it as evidence and a dependency
for the global angular radial estimate.  Record three rejected
inferences: treating \(356/819\) as a full threshold, optimizing over a
single denominator scale, and extending the terminal theorem below the
critical radial scale.

Keep the lower-radial estimate, full GAR, M9-M1, M9, and the Gauss-circle
target open.  The unconditional exponent is unchanged.

## 6. Resource and source audit

The round was entirely analytical.  No numerical experiment was used.
The TTY theorem stayed within its already audited source node, so no new
web source was required.

## 7. Next objective

For \(0<\nu<1/2\), exploit the subterminal ratio
\[
 \frac{h}{H_j}\asymp X^{(\nu-1/2)/2}\to0.
\]
The exact expansion \(\Phi(u)=1+O(u^2)\), combined with the spatial
partition of unity, may collapse the floor-perturbed angular symbol to
a one-sided character-divisor coefficient.  The next round must prove
the exact coefficient identity and its error before attempting
cancellation in the resulting radial sum.

