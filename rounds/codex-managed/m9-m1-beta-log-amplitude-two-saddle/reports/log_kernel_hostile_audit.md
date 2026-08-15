# Round 30 hostile audit: logarithmic two-saddle kernel

## 1. Result

The abstract moving-logarithm stationary bound is true, sharp, and
uniform through a nondegenerate saddle, a moving logarithmic face, and an
integration endpoint.  In the beta normalization, where the saddle width
in \(\alpha\) is \(\sqrt{\lambda}\), a single logarithmic face costs at
most
\[
 O\!\left(M_\lambda\sqrt{\lambda}\log(2+\lambda)\right),
 \qquad
 \lambda=\frac{\pi q\sqrt{Xx}}{D_j},                 \tag{30.1}
\]
instead of the ordinary \(O(M_\lambda\sqrt{\lambda})\).  The same bound
holds for Hessian signs \(+\lambda^{-1}\) and
\(-\lambda^{-1}\), for a saddle at an endpoint, and when the face and
saddle coalesce.  The logarithm is unavoidable: exact coincidence with
a saddle has a leading term equal to one half of \(\log\lambda\) times
the ordinary Fresnel term, up to the normalization of the logarithm.

The finite-section delta and PV terms do combine into boundary values of
complex logarithms with the Plemelj sign accepted in Round 29.  The
remaining numerator-difference term is regular and piecewise BV provided
the complete numerator has uniform scaled \(C^2\) control.

This does **not** certify the complete beta kernel or its \(q^{-2}\)
power.  The abstract lemma preserves an algebraic prefactor already
proved for the complete singular coefficient; it does not create that
prefactor.  The accepted \(q^{-2}\) statement is a separated full-line
value estimate, while the present application needs uniform
scale-normalized variation of the finite-section numerator, including
the delta trace, moving endpoints, masks, and the recombined
\(\rho\)-seam.  That mapping is absent from the authorized evidence.
A bounded-value hypothesis alone is sharply insufficient.

There is an actual-profile improvement at the logarithmic height face.
With \(y=L-\nu\), the two singular denominators satisfy
\[
 \rho=\rho_0-i\alpha+iy/2=:A+iy/2,
\]
and the exact partial fraction is
\[
 \frac1{y(A+iy/2)}
 =\frac1A\frac1y-\frac{i}{2A}\frac1{A+iy/2}.         \tag{30.0}
\]
At a saddle-face collision \(L=\pm V\asymp\pm\lambda\),
\(A=\rho_0-i\alpha\asymp\lambda\), while the accepted fixed-\(b\)
profile gives \(f_b(L)=O_b(\lambda^{-3})\).  Hence the log coefficient
is \(O_b(\lambda^{-4})\).  Restoring the Round-27 stationary numerator
\((D_j/q)\lambda\) makes this boundary term
\(O_b((D_j/q)\lambda^{-3}\log(2+\lambda))\), two inverse powers better
than the generic local \(D_j/(q\lambda)\) capacity.  The logarithmic
face itself is therefore harmless.  The unresolved seam is the
variation of the regular second term in (30.0), including masks,
finite-part endpoints, and the \(\rho=0\) patch.

Thus the narrow abstract lemma is certifiable, but the proposed actual
profile conclusion remains open at the numerator-variation and
normalization seam.

## 2. Exact statement and hypotheses

Let \(\lambda\ge2\), \(\sigma\in\{+1,-1\}\), and let
\[
 \Psi_\lambda(\alpha)=\lambda\varphi(\alpha/\lambda)
\]
on an interval contained in \(\lambda[c,C]\) for the positive saddle,
or its reflected negative interval.  Assume that \(\varphi\in C^4\)
has one stationary point \(y_s\), that
\[
 \sigma\varphi''(y_s)>0,
\]
and that the exact Morse map and its inverse have uniformly bounded
first three derivatives.  Let the integration endpoints be arbitrary
points in the interval, so an endpoint may equal the saddle.

Let \(B_\lambda(\alpha)=b_\lambda(\alpha/\lambda)\), where on each of a
fixed finite number of pieces
\[
 \|b_\lambda\|_\infty+
 \|b_\lambda'\|_{L^1}+
 \|b_\lambda''\|_{L^1}\le M_\lambda.                 \tag{30.2}
\]
For \(0\le a\le1\) and a moving face \(\alpha_f\) lying in a fixed
\(O(\lambda)\) enlargement of the interval, define either boundary
branch of
\[
 {\cal L}_{a,f}(\alpha)=\Log(a+i(\alpha-\alpha_f)).
\]
Then
\[
 \left|\int_P^Q
 B_\lambda(\alpha){\cal L}_{a,f}(\alpha)
 e^{i\Psi_\lambda(\alpha)}\,d\alpha\right|
 \ll M_\lambda\sqrt{\lambda}\log(2+\lambda),         \tag{30.3}
\]
uniformly in \(a,\alpha_f,P,Q\).  Adding finitely many such logarithms,
steps, and piecewise-\(W^{2,1}\) regular terms preserves (30.3).

The statement is intentionally conditional on scaled variation, not
merely \(\|B_\lambda\|_\infty\).  Degenerate saddles, a number of faces
growing with \(\lambda\), and unbounded Morse distortion are excluded.

For the exact finite beta section put
\[
\ell(L)=\max(-U,L-V),\qquad
r(L)=\min(U,L+V),                                    \tag{30.4}
\]
and assume \(\ell(L)<r(L)\).  Write
\[
H_0(L)=H(L,L).
\]
The hypotheses needed to insert it into (30.3) are uniform scaled
piecewise \(C^2\) bounds for \(H\), its \(L,\nu\) derivatives, and every
other recombined beta factor on the saddle patches, plus summable
height-tail bounds.  These are requirements, not accepted conclusions.

## 3. Proof or derivation

### Abstract logarithmic stationary bound

Use the exact Morse coordinate \(z\), with \(z=0\) at the saddle, so
\[
 \Psi_\lambda(\alpha(z))
 =\Psi_\lambda(\alpha_s)+\sigma\lambda z^2/2,
 \qquad d\alpha=\lambda m(z)\,dz,                    \tag{30.5}
\]
where \(m\) and its derivatives are uniformly bounded.  If the moving
face is in the coordinate patch, let \(z_f\) be its image.  The mean
value formula gives
\[
 \alpha(z)-\alpha_f
 =\lambda(z-z_f)m_f(z,z_f),                          \tag{30.6}
\]
with \(m_f\) bounded above and below.  Hence the logarithm is the sum of
a harmless smooth term, a constant \(O(\log(2+\lambda))\), and
\(\Log(a/\lambda+i(z-z_f))\).

On \(|z|\le\lambda^{-1/2}\), absolute integration and local
integrability of the logarithm give
\[
 \int_{|z|\le\lambda^{-1/2}}
 \left|\Log(a/\lambda+i(z-z_f))\right|\,dz
 \ll\lambda^{-1/2}\log(2+\lambda).                   \tag{30.7}
\]
On a dyadic shell \(|z|\asymp R\ge\lambda^{-1/2}\),
the phase derivative has size \(\lambda R\).  If \(z_f\) lies in that
shell, remove an interval of radius \((\lambda R)^{-1}\) around it; its
absolute contribution is
\[
 O\!\left((\lambda R)^{-1}\log(2+\lambda R)\right).
\]
On the remaining pieces, one integration by parts costs
\((\lambda R)^{-1}\), while the total variation of the truncated
logarithm is \(O(\log(2+\lambda R^2))\).  Summing the geometric shells,
including endpoint-truncated shells, proves an
\(O(M_\lambda\lambda^{-1/2}\log(2+\lambda))\) bound in \(z\).
The Jacobian \(\lambda\) in (30.5) yields (30.3).
Changing \(\sigma\) only conjugates the quadratic oscillation, so both
saddle signs have the same bound.

The estimate is sharp.  With a cutoff equal to one near zero, take
\[
 \Psi_\lambda(\alpha)=\frac{\alpha^2}{2\lambda},
 \qquad
 {\cal L}(\alpha)=\log\frac{|\alpha|}{\lambda}.
\]
After \(\alpha=\sqrt{\lambda}\,t\),
\[
 {\cal L}(\sqrt{\lambda}t)
 =\log|t|-\tfrac12\log\lambda .
\]
The coefficient of \(\sqrt{\lambda}\log\lambda\) is a nonzero ordinary
Fresnel integral.  Restricting to one side of zero gives exactly its
half-Fresnel analogue.  Thus neither saddle-face nor
saddle-endpoint coalescence permits removal of the logarithm.

### Delta/PV recombination

For the constant-in-\(\mu\) part of the exact section,
\[
\begin{aligned}
K_{U,V}(L)
={}&\pi{\bf1}_{\ell(L)<0<r(L)}\\
&-i\,\operatorname{PV}\int_{\ell(L)}^{r(L)}
 \frac{d\mu}{\mu}.                                  \tag{30.8}
\end{aligned}
\]
Let
\[
 \Log_-(x)=\lim_{\epsilon\downarrow0}\Log(x-i\epsilon)
 =\log|x|-i\pi{\bf1}_{x<0}.
\]
Then exactly, away from irrelevant equality conventions,
\[
 \boxed{K_{U,V}(L)
 =-i\{\Log_-(r(L))-\Log_-(\ell(L))\}.}               \tag{30.9}
\]
This verifies both the delta sign and the PV sign.  At \(L=V\),
\(\ell(L)\) crosses zero; at \(L=-V\), \(r(L)\) crosses zero with the
opposite orientation.  A value assigned at the single equality point
does not determine the half-Fresnel coefficient; that coefficient comes
from the one-sided integration domain.

For a varying numerator,
\[
\begin{aligned}
C_{U,V}(L)
={}&H_0(L)K_{U,V}(L)-iR_{U,V}(L),\\
R_{U,V}(L)
={}&\int_{\ell(L)}^{r(L)}
\frac{H(L,L-\mu)-H_0(L)}{\mu}\,d\mu .                \tag{30.10}
\end{aligned}
\]
The quotient in \(R_{U,V}\) extends continuously through \(\mu=0\).
If \(H\) has the scaled \(C^2\) bounds required above, \(R_{U,V}\) is
piecewise BV; the max/min switches in (30.4) create only finitely many
ordinary corners.  The faces \(|L-\nu|=U\) are therefore not additional
top logarithms.  They are handled by the ordinary incomplete-Fresnel
endpoint estimate.  A face \(|\nu|=V\) can meet a saddle and an
\(\alpha\)-endpoint simultaneously, but (30.3) remains uniform.

### Normalization audit

Equation (30.3) adds no algebraic power of \(\lambda\) beyond the
ordinary stationary factor; it adds only \(\log(2+\lambda)\).  Therefore,
**if** the complete coefficient in (30.10), with its pre-stationary
normalization restored, satisfies the same scale-normalized symbol bound
that yields \(q^{-2}\) on separated patches, then
\[
 q^{-2}\longmapsto
 q^{-2}\log(2+q\theta_j(x)),\qquad
 \theta_j(x)=\frac{\pi\sqrt{Xx}}{D_j},               \tag{30.11}
\]
and the \(q\)-sum remains absolutely convergent.

The antecedent is not proved by the local accepted lemma.  In particular,
the delta sample \(H(L,L)\), the regular remainder in (30.10), and their
scaled \(L\)-variation must each be checked with the explicit
\(1/\rho\), height transform, beta factor, masks, radial profile, and
\(\omega G+(1-\omega)R_1-\omega E_1\) recombination present.  A
stationary theorem cannot supply a missing inverse \(q\)-power.

For the actual face coefficient, (30.0) sharpens this conclusion.  The
\(1/y\) coefficient is \(f_b(L)/A\), so at
\(|L|\asymp|\alpha|\asymp\lambda\),
\[
 \frac{f_b(L)}A=O_b(\lambda^{-4}).                   \tag{30.12}
\]
After restoring the stationary numerator, the face-log contribution is
\[
 O_b\!\left(\frac{D_j}{q}\lambda^{-3}
 \log(2+\lambda)\right).                             \tag{30.13}
\]
The sign of the first term in (30.0) is positive, so there is no hidden
minus that reverses the Plemelj ledger.  The second term is nonsingular
at \(y=0\), but its variation can grow when \(A+iy/2\) approaches zero.
That is precisely the artificial-\(\rho\) region where the complete
\(\omega\)-recombination is mandatory.  Away from it the term is a
regular finite-part symbol, but no authorized estimate controls all its
\(L\)-derivatives and moving endpoints uniformly.

There is a sharp adversarial control.  If only
\(\|B_\lambda\|_\infty\le1\) is assumed, choose
\[
 B_\lambda(\alpha)=e^{-i\Psi_\lambda(\alpha)}
\]
on a long subinterval.  The oscillation disappears and the integral has
length-size capacity, contradicting (30.3).  Its scaled variation is
large, exactly identifying why a separated value estimate cannot be
substituted for (30.2).

## 4. First doubtful or unproved step

The first unproved project-specific step is the map from the complete
recombined beta numerator to (30.2), uniformly in \(q,h,D_j,x,U,V,S\)
and \(b\).  Round 29 proves the signed Plemelj limit and local logarithmic
integrability; it does not prove scaled variation after differentiating
the finite-section endpoints, the exact profiles, the beta connectors,
or the \(\omega\)-package.

The logarithmic face coefficient itself is target-safe by
(30.12)--(30.13), and is two inverse \(\lambda\)-powers better than the
separated \(q^{-2}\) capacity.  The remaining normalization question is
the regular finite-part term from (30.0), the delta sample, and their
variation near mask and artificial-\(\rho\) seams.  Those pieces can be
larger than the face-log coefficient and cannot be inferred from it.

Finally, no uniform \(U,V,S\) exhaustion follows.  Constants in the BV
norms and the number/size of tail pieces must be bounded before
\(V\to\infty\), while the finite-vector constraint
\(S>(U+V)/2\) couples this limit to the still-open radial horizontal
sides.

## 5. Control tests and outcomes

1. **Signed versus unsigned.**  The sign in (30.9) correctly recombines
   the delta and PV pieces.  The abstract logarithmic bound itself is
   coefficient-blind and can hold after absolute treatment of the
   locally integrable log; it supplies no \(\chi_4\) saving.  Outcome:
   analytic lemma passes, arithmetic conclusion not implied.
2. **Support and degeneracy.**  For \(U,V>0\), zeros of \(\ell,r\) occur
   only at the two height faces.  The \(\mu=\pm U\) switches are regular
   corners.  Degenerate \(U=0\), \(V=0\), or a degenerate phase requires
   a separate direct statement.  Outcome: pass under the stated
   hypotheses.
3. **Residue and normalization.**  Formula (30.9) gives
   \(\pi\delta-i\,\mathrm{PV}\), and both Hessian signs retain the
   ordinary stationary magnitude.  The external
   \(-(4/\pi)X^{1/4}\operatorname{Re}\) factor is unchanged.  Outcome:
   signs pass; the actual face log is better than \(q^{-2}\) by
   (30.12)--(30.13), while the regular finite part remains unresolved.
4. **Endpoint uniformity.**  The dyadic proof covers a face at the
   saddle, a saddle at an endpoint, and simultaneous coincidence.  The
   \(\sqrt{\lambda}\log\lambda\) example proves sharpness.  Outcome:
   abstract bound passes.
5. **Order of limits.**  The physical top limit is already encoded in
   (30.8)--(30.10).  The singular estimate is finite-box uniform, but
   gives no height-tail or radial-side exhaustion.  Outcome: finite
   boxes pass, infinite heights open.
6. **Coefficient adversary.**  Phase-cancelling bounded amplitudes
   violate the claimed stationary size unless scaled variation such as
   (30.2) is assumed.  The current accepted evidence supplies only a
   separated value estimate.  Outcome: unconditional application
   falsified.

## 6. Dependencies and exact artifacts used

This audit used only protocol.md, state/proof_obligations.yml,
state/active_campaign.yml, the Round-28 stationary-patching synthesis,
the authorized Round-29 hostile report, and the Round-29 synthesis.  No
Round-30 claimant report, external theorem, web source, or numerical
experiment was used.

## 7. Recommended state effect

**Promote only the abstract analytic kernel:** the uniform
moving-logarithm two-sign stationary estimate (30.3), its sharp
\(\sqrt{\lambda}\log\lambda\) coalescence control, and the exact
delta/PV logarithm identity (30.9), under the explicit Morse and scaled
piecewise-variation hypotheses.

**Retain the actual beta claim as open:** do not promote
M9-M1-beta-log-amplitude-two-saddle-kernel or the beta transition until
the regular finite-part numerator satisfies (30.2), its delta and PV
coefficients are controlled through the \(\rho\)- and mask seams, and
the \(U,V,S\) tails and finite sides are exhausted.  The explicit
logarithmic face coefficient may be recorded as target-safe by
(30.12)--(30.13).

The smallest next proof obligation is an exact actual-profile symbol
lemma for \(H_0(L)\) and \(R_{U,V}(L)\), including their scaled variation
and \(q,h,D_j,x,b\) powers on both signed saddle patches.  Only after that
lemma is proved does (30.11) become a valid project conclusion.
