# Round 124 synthesis: unmasked stationary off-product reduction

Campaign: `m9-m2-unbalanced-joint-stationary-lattice-gate`

Starting graph SHA-256:
`2b60eca238542d4f321a19c90f20163c6dd4cd7c60da6f324910b6db10b638c6`

## Frozen objective

The round tested the complete Round-123 flat-smooth strict-UNBAL shifted
survivor

$$
 \mathcal V_{M,H_0}=
 \sum_{j\ne0,\ E\ne0,\ |E|\le X^{1+\rho}/L}
 \chi_4(r)\chi_4(s)\Gamma_{M,H_0}(r,s),
 \qquad H_0=\left\lceil\frac{X^{1/2}}D\right\rceil,
$$

at the target \(X^{1/2+\varepsilon}\).  Here
\(D=X^\delta\), \(L=X^\ell\), \(K=XL/D^2\asymp LH_0^2\), and
\(\ell<\delta-1/4\).

## Complete first stationary transform

For the full unmasked zero-extended row, character Poisson and uniform
scalar stationary phase give

$$
 \mathcal F_{M,H_0}[A]
 =\mathcal F_{M,H_0}[\widetilde A]+O(1),
$$

where

$$
 \widetilde A(k)=e(-1/8)M^{1/4}k^{-3/4}
 \sum_{p>0\atop p\ {
m odd}}\chi_4(p)p^{-3/4}
 W\!\left(\frac{X}{2D}\sqrt{\frac p{Mk}}\right)
 q_L((X/M)p)e(\sqrt{Mkp}).
$$

Both quarter classes, Gaussian units, moving profiles, support entries and
exits, negative and inactive modes, literal zero extension, and the exact
Fejer normalization are included.  Two independent reports reproduce the
aggregate \(O(1)\) error, and the hostile audit accepts this statement for
the unmasked flat-smooth square.

The transformed correlation has phase

$$
 \Theta_{p,q,h}(k)
 =\sqrt M\{\sqrt{p(k+h)}-\sqrt{qk}\}.
$$

Its complete product-equality principal sector is exactly
\(p=q,h=0\), and

$$
 \mathcal D_0\ll X^{1/2}.
$$

Writing \(\mathcal S_{\rm eq}^{\ne0}\) for \(p=q,h\ne0\) and
\(\mathcal S_{\rm neq}\) for \(p\ne q\), the Round-123 safe physical
package \(\mathcal Q_{\rm safe}\) gives the exact scalar reduction

$$
 \mathcal V_{M,H_0}
 =\mathcal S_{\rm eq}^{\ne0}+\mathcal S_{\rm neq}
 +(\mathcal D_0-\mathcal Q_{\rm safe})+O(1),
 \qquad
 \mathcal Q_{\rm safe}\ll_\varepsilon X^{1/2+\varepsilon}.
$$

Thus the complete dual off-product aggregate is target-equivalent to the
physical survivor modulo proved packages.  Any fixed-power violation
forces this aggregate, and hence at least one of its two complete sectors,
to carry the same power excess.  This is the round's strict reduction; it
does not bound either sector.

## Product defect, alias gradient, and exact saddle collar

The phase product defect

$$
 \mathcal N=p(k+h)-qk
$$

is not the gradient numerator.  The corrected identity is

$$
 \mathcal G=pk-q(k+h)=\mathcal N-(p+q)h,
$$

$$
 \partial_k\Theta
 =\frac{\sqrt M\,\mathcal G}
 {2\sqrt{k(k+h)}\{\sqrt{pk}+\sqrt{q(k+h)}\}}
 =M\left(\frac1{r_*}-\frac1{s_*}\right).
$$

For integer alias \(j\),

$$
 E_*(j)=M(s_*-r_*)-jr_*s_*
       =r_*s_*\{\partial_k\Theta-j\}.
$$

Every exact \(k\)-saddle therefore lies on \(E_*=0\), whether or not
\(\mathcal N=0\).  The live physical nonexact aliases form a coupled
discrete collar.  Their indicator cannot be inserted into two independent
rowwise Poisson formulae.  The accepted connector is the full-minus-safe
scalar identity above, not a termwise dual image of the projector.

## Joint principal-phase return

On fixed smooth \((k,h)\)-interiors, the Hessian is nondegenerate:

$$
 \det\nabla^2_{k,h}\Theta
 =-\frac{M\sqrt{pq}}{16(k+h)^{3/2}k^{3/2}}.
$$

For dual labels \((j,d)\), the simultaneous saddle satisfies

$$
 r_*=M/d,\quad s_*=M/(d-j),\quad
 k_*=\frac{Mq}{4(d-j)^2},\quad
 h_*=\frac M4\left(\frac p{d^2}-\frac q{(d-j)^2}\right),
$$

and

$$
 \Theta-jk-dh=jk+dh
 =\frac M4\left(\frac p d-\frac q{d-j}\right).
$$

The Legendre phase is the original reciprocal correlation phase at the
ideal selectors.  The Hessian amplitude cancels all \(k\)-powers and
leaves \(4C_H(H-|h_*|)/(pq)\).  Thus the proposed second stationary
operation returns to the primal phase at principal-symbol level.

This is not promoted as a complete \((k,h)\) transform.  The Fejer cusp,
shift faces, literal \(k\)-support boundaries, stationary transitions, and
nonstationary modules remain without a target-level aggregate ledger.

## Capacity and method disposition

The fixed-interior gradient-image ledger has unsigned capacity \(D^2\).
Retaining only the formal equal-mode part, or granting square-root credit
over the \(L^2\) character pairs, leaves \(D^2/L\).  Its ratio to the
target is

$$
 Q=\frac{D^2}{L\sqrt X}\to\infty.
$$

This is a diagnostic against triangle inequalities, coefficient-blind
energies, and random-sign credit.  It is not a positive lower bound;
\(p=q,h\ne0\) is a shifted autocorrelation rather than a termwise
modulus-square diagonal.  The round does not rule out every genuinely
joint signed norm.

Product equality, conjugate pairing, Hessian rank, and a second invertible
stationary transform are now parked as standalone mechanisms.  A lawful
continuation must prove

$$
 \mathcal S_{\rm eq}^{\ne0}+\mathcal S_{\rm neq}
 \ll_\varepsilon X^{1/2+\varepsilon},
$$

or give a stronger inverse theorem for one complete actual-sign sector.

## Decision and proof status

Promote the unmasked first stationary transform, the target-safe
product-equality diagonal, the off-product inverse reduction, and the
strict-interior principal-phase return as a scoped method obstruction.
Reject any transported near-alias projector, positive capacity lower
bound, or complete joint-transform claim.

The flat-smooth strict-UNBAL estimate remains open.  Every nonflat, sharp,
starred, clipped, hard, arithmetic-owner, and transition UNBAL packet is
still separate.  Hard TOP, BAL, complete M9-M2, both direct M1 parents,
the lower GAR alternative, endpoint uniformity, M9, and the Gauss-circle
quarter target remain open.

The internal global exponent remains \(1/3\).  The audited external
benchmark remains

$$
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots .
$$

Round 124 proves no global exponent improvement.

Resulting graph SHA-256:
`27bd4173fbdb16e5689595a02d42d82ffa8bb514b4610ea745ce2da6e2b8b152`.
