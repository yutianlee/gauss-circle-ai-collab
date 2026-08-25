# Round 136 synthesis: exact character restoration, but no broad--narrow scalar gain

Campaign: `m9-m2-balanced-joint-cluster-defect-broad-narrow-gate`

Starting graph SHA-256:
`c43058006cec6849cd17a49e6a7a5298f5a3c124b34d2333b3279adcb54da1d1`

Resulting graph SHA-256:
`3c5003b1478d78b8469d4220ad305bb06ee0f869b9c4a741e7211642eeb52cc7`

## Frozen objective and decision

Round 136 asked whether the complete signed divisor-progressive balanced
bulk kernel could be split into transverse broad pieces and arithmetic
narrow rulings, with every piece totaling

\[
 |\mathcal K_B^{\mathrm{bulk}}|
 \ll_\varepsilon L^3X^\varepsilon,
 \qquad L\asymp X^{1/6}.
\]

Close the round under `broad_narrow_no_go`. The round proves new exact
character and ruling identities and rigorously reconciles three competing
geometric calculations, but it proves neither the \(L^3\) target nor a
strictly smaller owner-complete survivor.

## Exact character restoration

In the literal divisor progression

\[
 h+2s_d=d\ell_d,qquad \mu=\frac12-m,qquad
 \lambda=\frac\mu d,
\]

one has

\[
 \boxed{
 e\!\left(-\frac{\lambda h}{2}
 +s_d\left(\frac12-\lambda\right)\right)
 =-i(-1)^m\chi_4(d)\chi_4(h).}
\tag{136.S1}
\]

If \(2\lambda=a/b\) is reduced, every lift has

\[
 (d,\mu)=(bc,ac/2),\qquad a,b,c\ \mathrm{odd},
\]

and

\[
 (-1)^m\chi_4(d)=\chi_4(ab).
\tag{136.S2}
\]

Thus the full exponential-character carrier is

\[
 -i\chi_4(h)\chi_4(ab)
 e\!\left(R\sqrt{hk}-\frac{Xbk'}a\right),
\tag{136.S3}
\]

independent of the lift multiplier \(c\). The stationary point and both
far gates are also common. This corrects the residue-only picture:
equal-rational lifts are carrier-coherent, not character-canceling.

Their \(\gamma_{bc}\), divisor progression, \(J\)-condition, support, and
literal amplitude remain different. Equation (136.S3) does not merge the
lifts, prove their weighted sum positive, or give a lower bound.

## Reconciliation of the three determinants

With \(r=\sqrt{k/h}\) and \(z=\lambda/R\), the unfactored and gauged
normalized outer-gradient surfaces are

\[
 \Sigma_0=(r-z,r^{-1},-z^{-1}),\qquad
 \Sigma_1=(r,r^{-1},-z^{-1}).
\tag{136.S4}
\]

The blind report computes determinants of three points on
\(\Sigma_0\). The discovery report computes determinants of normals to a
gradient-image surface. The hostile report computes a one-body Hessian.
These are three different objects.

The raw and gauged surface normals are proportional to

\[
 (1,r^2,z^2),\qquad (1,r^2,0),
\]

respectively. Therefore the discovery three-normal broad class is empty
for its chosen gauged partition, but determinants of three gauged gradient
vectors can still be nonzero. The exact character gauge is a unit-modulus
coefficient modulation. It follows that raw surface-normal curvature is not
a representation-independent sufficient certificate for a
coefficient-uniform broad theorem.

This does not rule out a theorem formulated in the raw gauge and using the
specific arithmetic carrier. It identifies the missing seam: no report
proves an owner-preserving norm or scalar exponential-sum inequality that
turns any of the three determinants into the needed factor \(L^{-1}\) for
the one fixed-block scalar.

## Exact narrow ruling and capacity obstruction

Put

\[
 c=\frac{\lambda}{R}\sqrt{\frac hk},qquad
 Q=\frac{\mu^2h}{d^2k}=Xc^2,qquad A=\frac{k'}k.
\]

For fixed \(c\), both gradient descriptions satisfy
\(G_2+cG_3=0\). Hence every three-gradient determinant on this
fixed-\(Q\) ruling vanishes in either gauge. The gates are exactly

\[
 \rho=hk'\frac{c^2-1}{c^2},
 \qquad
 \Delta=hk\frac{A^2-c^2}{c^2}.
\tag{136.S5}
\]

They remove collars about \(c^2=1\) and \(c^2=A^2\), but do not remove
the ruling. For \(k'=k\), \(\Delta=-\rho\), so double-far
determinant-zero points occur beyond the common collar. This is an exact
geometric and gate control, not a proof that a literal physical packet is
nonzero.

At \(d=1\), aliaswise absolute values have \(L^5\) capacity and the
positive square shadow has \(L^4\) capacity, against the \(L^3\) target.
Fixed-slice same-parity reciprocal clusters of cardinality
\(\gg d^2L^2\) remain, but their claimed weighted masses are only upper or
adversarial capacities. No common \(v\)-run or actual-symbol lower mass is
proved. A phase-adapted bounded-amplitude array therefore refutes a theorem
uniform over all coefficients satisfying only the size bound, but it is not
the physical amplitude and supplies no lower bound.

The arithmetic identity

\[
 \sum_{d\mid n}\frac{\gamma_d}{d}
 =\sum_{r\mid n}\frac{\eta(r/G_0)}r
   \frac{\varphi(n/r)}{n/r}>0
\]

is retained only for a leading common-profile model under common
admissibility. It does not make the full \(J\)-dependent literal lift sum
positive.

## Smallest survivor and full-proof status

The smallest owner-complete unresolved object is still the full signed
kernel

\[
 \sum_{h,k,k'} b_B(h,k)
 \sum_{d\mid k'}\gamma_d
 \sum_{J,\mu}^{\mathrm{bulk}}
 \mathcal A_{d,J}(h,k,k';\mu)e(\Theta_{d,\mu}),
\]

with all distinct lifts, both gates, every profile, and the restored
character retained before any modulus. Its broad side would need a new
gauge-explicit scalar inequality; its narrow side would need a signed
estimate for the complete equal-lift and fixed-\(Q\) families jointly with
the outer variables. The displayed second-B calculation returns only the
square-root critical action and arithmetic lattice; it creates no new phase
direction and proves no full owner return.

The balanced oscillatory remainder, actual double-far energy, and balanced
quarter packet remain open. Hard TOP and every required UNBAL owner remain
open, so M9-M2 remains open. Both direct M9-M1 parents and the lower-GAR
alternative remain open. Endpoint uniformity, M9, the conditional quarter
bridge, and the Gauss-circle quarter target are therefore also open.

The strongest internally proved global exponent remains

\[
 \frac13.
\]

The separately audited external Li--Yang benchmark remains

\[
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots .
\]

Round 136 proves no global exponent improvement. The BAL broad--narrow
surface is parked until a genuinely new actual-symbol theorem appears; the
next round should rotate to a distinct open owner.
