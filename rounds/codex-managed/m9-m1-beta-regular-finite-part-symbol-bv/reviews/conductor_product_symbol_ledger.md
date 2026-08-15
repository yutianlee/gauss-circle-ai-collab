# Conductor product-symbol ledger for Round 31

Campaign: `m9-m1-beta-regular-finite-part-symbol-bv`  
Role: conductor seam analysis  
Allocation: 100% analytical/algebraic

## 1. Normalized saddle variable

Write \(\alpha=\pm\lambda y\) on a fixed enlarged saddle patch, where
\(\lambda=\pi q\sqrt{Xx}/D_j\).  A multiplicative factor \(M(\alpha)\)
is harmless for the Round-31 product rule if

\[
 \|M\|_\infty+\|\partial_yM\|_1\ll X^\varepsilon        \tag{31.P1}
\]

uniformly in all retained parameters.  Products of finitely many such
factors obey the same bound up to \(X^\varepsilon\).

## 2. Factors already benign on a separated patch

- Powers \(|\alpha|^c\) become \(\lambda^c|y|^c\); after the recorded
  leading monomial is factored out, their normalized symbols and first
  derivatives are bounded on \(|y|\asymp1\).
- Stirling remainders are classical order-zero symbols on
  \(|\alpha|\asymp\lambda\): one scaled derivative has the same size.
  This assertion is only for the separated large-height patch, not a
  transition plane.
- The phase itself is excluded from the amplitude and absorbed by the exact
  Morse coordinate.  Differentiating it as an amplitude would manufacture
  a false factor of \(\lambda\).
- The scale factors \((D_j/(2\sqrt X))^a(H_j+1)^b\), exact floors, and
  Vaaler height cutoff are independent of \(\alpha\) before endpoint
  ownership is changed.  They must be retained in the inherited monomial,
  but create no Morse derivative.
- For a smooth interior spatial profile, the transform
  \(\widehat W_j(a+i\mu)\), \(\mu=\alpha-\beta-\nu\), is rapidly decaying;
  one scaled derivative remains summable after the natural
  \(|\mu|\asymp\lambda\) rescaling.  The top \(1/u\) term is not included:
  it has already been distributionally split and is represented by the
  finite-section regular kernel.
- A fixed beta mask has bounded support and bounded derivatives.  In the
  beta-bounded branch it depends on beta rather than alpha, so it costs no
  Morse derivative; alpha-edge masks belong to the connector/double-bounded
  ownership ledger and cannot be silently inserted.

Combined with the separated finite-part calculation, these facts strongly
support the target scale away from transition and residue seams.

## 3. Omega recombination derivative

Let \(r=-\Im\rho\), so \(\partial_\alpha r\) is constant on a fixed
height slice.  Differentiating

\[
 \omega G+(1-\omega)R_1-\omega E_1                     \tag{31.P2}
\]

gives an omega-prime coefficient

\[
 (\partial_\alpha r)\omega'(r)(G-R_1-E_1)=0.          \tag{31.P3}
\]

Thus the cutoff derivative is exactly absent, provided all three summands
have the same finite section, beta mask, endpoint convention, and radial
domain before regular-part subtraction.  If the diagonal Plemelj piece is
removed termwise with different ownership, (31.P3) need not remain
visible.  The correct construction is therefore: form the recombined
numerator first, take the signed finite-section limit, subtract its single
combined diagonal/log term, and only then differentiate.

The ordinary derivatives of \(G,R_1,E_1\) in (31.P2) remain to be bounded.
Analyticity cancels the apparent pole in \(G\), while \((1-\omega)R_1\)
is separated from it.  The term \(-\omega E_1\) carries the ledgered
artificial residue; its regular remainder must be checked on the same
scale and cannot be inferred from (31.P3).

## 4. Candidate first obstruction

The likely first nonlocal seam is not a large derivative of a separated
factor, but uniformity under height exhaustion.  The finite-section BV
norm contains moving endpoint traces.  To pass \(U,V,S\to\infty\), one
needs their integrated norms to decay uniformly with the saddle location,
including the zones where \(V\asymp\lambda\).  Round 30 controls the
explicit face logarithm there, but the regular trace still contains all
connector and omega-recombined factors.  A proof must exhibit a summable
majorant; fixed-\(V\) BV alone is insufficient.

## 5. Provisional conclusion

On separated finite-height patches, all visible factors are compatible
with the target order-zero product calculus, and omega-prime terms cancel
exactly at the unsplit level.  The unresolved quantitative interfaces are:

1. the ordinary derivative of the complete analytic \(G/R_1/E_1\)
   package across \(\rho=0\) after combined diagonal subtraction;
2. moving endpoint traces uniformly in \(U,V,S\);
3. the \(b\downarrow0\) axial split; and
4. the final scale, height, and radial power sum.

No graph promotion follows from this ledger until the subagent derivations
or an independent conductor proof supplies those estimates.
