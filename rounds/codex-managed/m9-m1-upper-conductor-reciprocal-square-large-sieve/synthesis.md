# Round 72 synthesis: third-derivative conductor advance

## Outcome

Round 72 proves a new exact fixed-interior conductor interval.  Combining
the Round-71 three-variable Farey theorem with the new row estimate makes
every order-\(J\) block

\[
 T\leq C\leq J^{32/45}=X^{16/45}
\]

target-safe.  The earlier endpoint was \(J^{2/3}=X^{1/3}\).  The remaining
fixed-interior range is \(J^{32/45}<C\leq J\).

No statement about cone edges, the complete product wavelet,
\(M9\!-\!M1\), \(M9\!-\!M2\), \(M9\), or a global circle exponent is
proved.

## Exact mechanism

For fixed Farey numerator \(b\asymp C/T\), split \(c\) into admissible
residue classes modulo \(4b\).  In every odd or even local class the local
arithmetic unit is then constant, and the remaining phase is

\[
 e\!\left(\pm A_{\kappa,b}/c\right),
 \qquad
 A_{\kappa,b}
 =\left(\sqrt{bX}+\sqrt{\kappa k/b}\right)^2,
 \qquad \kappa\in\{1/4,1/2,1\}.
\]

The exact Farey determinant equations partition each residue progression
into \(O(Q/B)\) intervals on which both neighbor numerators are fixed.
There are \(O(B)\) progressions, hence \(O(Q)\) pieces in total.  Each
piece has at most \(O(C/Q)\) samples.  Its incomplete-Fresnel endpoint
arguments vary by \(O(\sqrt{C/J})\), and every other normalized stationary
factor has bounded variation.  Thus the actual symbol, including saddle
entry and exit, has piecewise sup plus variation
\(O_\varepsilon(X^\varepsilon)\).

On \(c=r+4b\ell\),

\[
 |f'''(\ell)|\asymp J^2/T^4=Q^{-1}.
\]

One differencing step followed by the second-derivative estimate gives the
weighted third-derivative bound

\[
 LQ^{-1/6}+L^{1/2}Q^{1/6}+1.
\]

Summing the first term by total length and the second by Cauchy across the
exact pieces yields

\[
 |S_{b,k}^{(\kappa)}(C)|
 \ll_\varepsilon X^\varepsilon
 \{CQ^{-1/6}+C^{1/2}Q^{2/3}+Q\}
 \ll_\varepsilon X^\varepsilon CQ^{-1/6}.
\]

Therefore

\[
 \mathcal E_{C,k}^{(\kappa)}
 \ll_\varepsilon X^\varepsilon
 \frac{C^3}{TQ^{1/3}}.
\]

The sufficient target \(J^2/T\) holds exactly through
\(C\leq J^{2/3}Q^{1/9}=J^{32/45}\).  Both axes are smaller there because
their accepted nonstationary integral gives \(C^2/J\).  Large dual tails,
stationary remainders, half-open endpoints, singleton pieces, gcds, and the
finite dual family are retained and target-safe.

## Controls and independence

The clean statement-only report verified the normalization and showed why
an arbitrary phase-only estimate would be invalid.  After the actual
candidate existed, a separate independent seam review derived the exact
neighbor count, transition variation, even phases, axis bound, and exponent
without using the source audit.  The hostile/source report independently
verified the derivative powers and piece count and found no square,
fourth-power, diagonal, or source-hypothesis counterexample to the scoped
lemma.

The proof uses the actual symbol and takes no absolute value before the
signed row cancellation.  It therefore does not prove the false unsigned
or arbitrary-coefficient analogue.  No numerical experiment was used.

## Remaining obstruction

The third-derivative saving is only \(Q^{1/6}\); above \(J^{32/45}\) it
does not reach the diagonal-scale energy target.  Odd reciprocity and smooth
completion lead to a genuine level-four \((\infty,1)\) Kloosterman family
with a phase-matched Bessel branch.  A lossless Kuznetsov closure would
still require a pointwise short automorphic coefficient estimate of size
\(X^{1/4+\varepsilon}\), together with a uniform phase-specific Bessel
transform, actual transition separation, Eisenstein control, both even
classes, and zero-index axes.  The coefficient scale is conjectural and no
audited source supplies the complete theorem.

Thus the next target is only the exact residual range

\[
 J^{32/45}<C\leq J,
\]

preferably by a method that combines the third-derivative saving with a
genuinely joint average or proves a stronger transition-compatible
derivative estimate.  The forbidden bare \(c\)-Poisson/matching
\(B\)-process loop remains an exact self-return.

## State decision

Promote the scoped third-derivative lemma and add it as a dependency of the
global angular-radial obligation.  Retain all downstream targets open and
record no global exponent improvement.

Accepted evidence:

- rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/reports/upper_reciprocal_energy_attack.md;
- rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/reports/blind_upper_conductor_clean.md;
- rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/reports/upper_third_derivative_seam_review.md;
- rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/reports/upper_reciprocal_source_hostile_audit.md;
- rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/reviews/conductor_round72_adjudication.md.
