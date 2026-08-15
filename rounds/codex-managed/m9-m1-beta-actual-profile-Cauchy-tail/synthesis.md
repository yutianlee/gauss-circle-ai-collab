# Round 38 synthesis: the actual endpoint-free beta Cauchy tail converges

Campaign: `m9-m1-beta-actual-profile-cauchy-tail`  
Round type: actual beta-slab Cauchy tail  
Graph SHA-256 before patch: `da69e58e4abbfdf5bc16207c4f3b7411e29661cc8d43c07769c4c2adf28ff0bf`

## Conductor decision

Round 38 proves the complete positive-\(b\) signed Cauchy tail left open in
Round 37.  The fixed endpoint-free vector therefore has a unique symmetric
outside-height/profile limit.  This closes the limit interfaces in the
connector ledger and mask--endpoint--axial compatibility architecture.  It
does **not** prove the quantitative terminal-symbol estimate or an
\(X^\varepsilon\) bound.

Choose the lawful terminal line

\[
 c'=\frac54,\qquad b=\frac1{\log(2X)},\qquad
 0\le a<a_0,\qquad a+b<\frac12,\qquad \frac a2+b<\frac14,
 \tag{38.1}
\]

and, before taking an absolute value, put

\[
 t=\frac{\mu+\nu}{2}+\beta,\qquad
 \alpha=\mu+\nu+\beta,\qquad
 \eta=\frac\mu2+\nu+\beta .
 \tag{38.2}
\]

The Jacobian is one.  With \(A=s-(u+v)/2\) and
\(B=s+(u+v)/2\),

\[
 A=\left(\frac54-\frac{a+b}{2}\right)+i\beta,
 \qquad
 B=\left(\frac54+\frac{a+b}{2}\right)+i\alpha .
 \tag{38.3}
\]

Thus the first gamma factor stays on a compact beta slab and the second has
power

\[
 \kappa=\Re B-\frac12=\frac34+\frac{a+b}{2}<1.
 \tag{38.4}
\]

The exact coefficient phase and real powers are

\[
 \left(\frac hq\right)^{(u+v)/2}(hq)^{-s}
 =h^{-5/4+(a+b)/2}q^{-5/4-(a+b)/2}
   q^{-i(\mu+\nu)}(hq)^{-i\beta}.
 \tag{38.5}
\]

Both coefficient series, including one logarithmic derivative, converge
absolutely.  The post-endpoint radial coordinate is

\[
 \rho=-1-\frac b2-i\eta,
 \tag{38.6}
\]

and direct absolute integration of the \(I_1\) weight gives

\[
 |R_{1,v}(1-s)|+|\partial_\mu R_{1,v}(1-s)|
 \ll_X\frac1{1+|\eta|}.
 \tag{38.7}
\]

After summing the actual \(h,q,j\) factors and retaining bounded beta
shifts, the terminal numerator satisfies

\[
 |H(\mu,\nu)|\ll_{X,b}|\widehat\phi(b+i\nu)|
 \frac{(1+|\mu+\nu|)^\kappa}{1+|\mu/2+\nu|}.
 \tag{38.8}
\]

The physical top is kept as the signed distribution

\[
 \frac1{2\pi}\frac1{0^++i\mu}
 =\frac12\delta_0(\mu)-\frac{i}{2\pi}\operatorname{PV}\frac1\mu.
 \tag{38.9}
\]

Only after the symmetric PV subtraction may absolute values be taken.  The
key elementary convolution is

\[
 \int_{|\mu|>1}
 \frac{(1+|\mu+\nu|)^\kappa}
 {|\mu|(1+|\mu/2+\nu|)}\,d\mu
 \ll (1+|\nu|)^{\kappa-1}\log(2+|\nu|),
 \tag{38.10}
\]

uniformly in the \(\mu\)-cutoff.  Its far range converges exactly because
\(\kappa<1\).  Since
\(|\widehat\phi(b+i\nu)|\ll_b(1+|\nu|)^{-3}\), the terminal density has
the integrable majorant

\[
 |\mathcal F_T(\nu)|
 \ll_{X,b}(1+|\nu|)^{\kappa-4}\log(2+|\nu|).
 \tag{38.11}
\]

## Artificial-pole correction

The discovery report's terminal right-chamber series must **not** be
continued termwise onto \(\rho=0\).  That residue lies outside its absolute
Dirichlet chamber.  The hostile audit supplies the lawful treatment:

\[
 K_{u+v}(1-s)F_{-(u+v)}(s)
 =\zeta(1-A)L(1-B,\chi_4).
 \tag{38.12}
\]

Compact beta support then forces \(\mu=-2\nu+O(1)\).  The top factor is
\(O(|\nu|^{-1})\), the height profile is \(O_b(|\nu|^{-3})\), and bounded
partial sums of \(\chi_4\) give
\(L(\sigma+i\tau,\chi_4)\ll_\sigma1+|\tau|\).  Hence the oriented
artificial residue contributes

\[
 \mathcal F_\rho^{\rm ef}(\nu)=O_{X,b}((1+|\nu|)^{-3}).
 \tag{38.13}
\]

Its top delta, the \(v=0\) axial shares, and the joint corner have bounded
\(\nu\)-support.  Collisions retain the accepted one-count convention.

Equations (38.11)--(38.13) are uniform in \(U\).  They prove the joint
\((U,V)\) Cauchy property.  For

\[
 S=(2+X+U+V+2B_0)^2,
 \tag{38.14}
\]

compact beta support deletes the radial sides and makes the \(S\)-stage
eventually constant.  Therefore the complete endpoint-free physical
remainder exists and is independent of the prescribed cofinal exhaustion.

## Independent validation and scope

The statement-only blind report independently obtained the unit Jacobian,
the same \(c'=5/4\) threshold \(\kappa<1\), the exact real coefficient
powers, the direct \(R_1/\rho\) bound, and a coarser but still integrable
uniform tail.  The hostile report independently recomputed the terminal
majorant and found the artificial-residue chamber correction above.  The
conductor rederived the convolution estimate and power ledger in
`reviews/conductor_cauchy_majorant_check.md`.

The constants in (38.7), (38.11), the finite scale sum, and (38.13) have
not been reduced to \(O(X^\varepsilon)\).  The theorem is at fixed positive
\(b\); it does not move \(b\) through zero, where the separately extracted
\(v=0\) vector residue lives.  It uses no local stationary \(q^{-2}\)
estimate.  Consequently it proves existence and ownership, not the local
\(\lambda^{-2}/\lambda^{-3}\) symbol bounds, the complete beta transition,
M9-M1, M9, or the Gauss-circle target.

## State effect

- Promote the actual positive-\(b\) Cauchy-tail theorem.
- Promote the unique physical endpoint-free beta axial remainder limit.
- Close the limiting connector-ledger and mask--endpoint--axial
  compatibility interfaces, whose only remaining condition was that limit.
- Retain the axial-subtracted terminal-symbol bound open.  It is now the
  next quantitative interface.
- Reject pre-Plemelj absolute integration, termwise coefficient expansion
  on the artificial-residue line, transfer of local \(q^{-2}\) to the
  global tail, a simultaneous \(b\downarrow0\) limit, and any inference of
  an \(X^\varepsilon\) bound from the fixed-\(X\) Cauchy theorem.

Round 39 should define the limiting axial-subtracted terminal symbol from
this now-licensed vector and audit the full \(X\)-dependence of its value and
physical-height derivative before attempting the downstream BV lemma.
