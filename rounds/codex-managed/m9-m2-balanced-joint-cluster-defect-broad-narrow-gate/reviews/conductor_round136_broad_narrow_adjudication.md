# Round 136 conductor adjudication: character gauge, determinants, and rational rulings

Campaign: `m9-m2-balanced-joint-cluster-defect-broad-narrow-gate`

Starting graph SHA-256:
`c43058006cec6849cd17a49e6a7a5298f5a3c124b34d2333b3279adcb54da1d1`

## 1. Result

Close Round 136 under `broad_narrow_no_go`.

The round proves the exact character-restoration identity

\[
 e\!\left(-\frac{\lambda h}{2}
 +s_d\left(\frac12-\lambda\right)\right)
 =-i(-1)^m\chi_4(d)\chi_4(h),
\tag{136.1}
\]

and its equal-rational-lift consequence. If \(2\lambda=a/b\) is reduced,
then every lift is \((d,\mu)=(bc,ac/2)\), with \(a,b,c\) odd, and

\[
 (-1)^m\chi_4(d)=\chi_4(ab).
\tag{136.2}
\]

The complete phase and character carrier, as well as \(x_*\), \(\rho\),
and \(\Delta\), is therefore independent of the lift multiplier \(c\).
The literal divisor weight, progression, \(J\)-condition, and amplitude
remain distinct. The lifts are coherent in their unit carrier but may not
be merged and need not add positively.

The apparent conflict between the three reports is resolved. The blind
determinant is a determinant of three unfactored gradient vectors; the
discovery determinant is a determinant of normals to a gauged gradient
surface; and the hostile determinant is a one-body Hessian. All three
algebraic calculations can be correct because they are different objects.
None comes with an owner-preserving inequality that yields the missing
factor \(L\) for the fixed scalar kernel. Exact fixed-\(Q\) rulings survive
both gauges and both strict gates.

Thus the standard coefficient-uniform broad/positive-cap route is parked.
This is not a lower bound for the literal kernel, not a disproof of BAL,
and not a no-go for a new gauge-sensitive theorem using the actual signed
amplitudes jointly.

## 2. Exact statement and hypotheses

The only target is the fixed-block interior kernel

\[
 \mathcal K_B^{\mathrm{bulk}}
 =\sum_{h\ \mathrm{odd},k,k'}b_B(h,k)
  \sum_{\substack{d\mid k'\\d\ \mathrm{odd}}}\gamma_d
  \sum_J\sum_{\substack{\mu\in\mathbb Z+1/2,\ \mu>0\\t_*\in J}}^{\mathrm{bulk}}
  \mathcal A_{d,J}(h,k,k';\mu)e(\Theta_{d,\mu}),
\tag{136.3}
\]

where

\[
 \begin{gathered}
 h+2s_d=d\ell_d,\qquad \mu=\frac12-m,qquad
 \lambda=\frac\mu d,qquad x_*=\frac{Xk'}{\lambda^2},\\
 \Theta_{d,\mu}=R\sqrt{hk}-\frac{Xk'}{2\lambda}
 -\frac{\lambda h}{2}+s_d\left(\frac12-\lambda\right),
 \qquad R=\sqrt X,\quad L\asymp X^{1/6}.
 \end{gathered}
\tag{136.4}
\]

There are \(O(L^3)\) outer triples, \(\mu\asymp dL^3\), and
\(|\mathcal A_{d,J}|\ll(dL)^{-1}\). Every atom retains

\[
 \rho=hk'-x_*k,qquad \Delta=x_*k'-hk,qquad
 |\rho|,|\Delta|>L.
\tag{136.5}
\]

The fixed block, both low-gcd weights, slanted profiles, all distinct
lifts, exact equality conventions, and real-centre phases remain literal.
Already controlled boundary, transition, crossing, nonstationary,
stationary-remainder, and phase-free owners are excluded and used zero
additional times.

The accepted proposition is scoped to the following method statement:

> The exact carrier identity and the exact gradient/ruling formulas do not,
> with the supplied hypotheses, imply
> \(|\mathcal K_B^{\mathrm{bulk}}|\ll L^3X^\varepsilon\). A
> coefficient-modulation-invariant broad theorem cannot use the raw
> surface-normal curvature as a representation-independent certificate,
> and no raw gradient-vector or one-body-Hessian determinant has a proved
> scalar norm interface. Equal-rational and fixed-\(Q\) narrow classes have
> no automatic character cancellation. The complete signed kernel remains
> open.

## 3. Proof and reconciliation

From \(h+2s_d=d\ell_d\),

\[
 -\frac{\lambda h}{2}
 +s_d\left(\frac12-\lambda\right)
 =\frac{s_d}{2}-\frac{\mu\ell_d}{2}.
\]

Using \(\mu=1/2-m\), odd \(\ell_d\), and
\(d\ell_d=h+2s_d\pmod4\) gives (136.1). Reducing
\(2\mu/d=a/b\) gives \((d,2\mu)=(bc,ac)\), and

\[
 (-1)^m=\chi_4(ac),qquad
 (-1)^m\chi_4(bc)=\chi_4(ab),
\]

which proves (136.2). Hence the owner-complete equal-rational packet has
carrier

\[
 -i\chi_4(h)\chi_4(ab)
 e\!\left(R\sqrt{hk}-\frac{Xbk'}a\right)
\tag{136.6}
\]

times the still-literal lift sum

\[
 \sum_{\substack{c\ \mathrm{odd}\\bc\mid k'}}\gamma_{bc}
 \sum_{J:t_*(bc)\in J}^{\mathrm{bulk}}
 \mathcal A_{bc,J}(h,k,k';ac/2).
\tag{136.7}
\]

Because \(x_*=Xk'/\lambda^2\), both gates are common across the lifts in
(136.7). Their support and amplitudes need not be common.

For the geometry, put \(r=\sqrt{k/h}\), \(z=\lambda/R\). The raw and
gauged normalized gradient surfaces are respectively

\[
 \Sigma_0=(r-z,r^{-1},-z^{-1}),qquad
 \Sigma_1=(r,r^{-1},-z^{-1}).
\tag{136.8}
\]

The blind identity computes \(\det(\Sigma_{0,1},\Sigma_{0,2},
\Sigma_{0,3})\), which can be nonzero. The normals to the two surfaces are
proportional to \((1,r^2,z^2)\) and \((1,r^2,0)\), respectively. Thus the
discovery three-normal determinant is identically zero in the gauged
representative, while a raw three-normal determinant can be nonzero. The
hostile unit Hessian is instead a local transform Jacobian. No one of these
determinants implies either of the others, and no report proves the
inequality connecting one of them to the fixed scalar.

The exact gauge (136.1) is a unit modulation of coefficients. It preserves
all coefficient magnitudes, indices, owners, and gates. Consequently a
coefficient-uniform square-function theorem cannot treat raw normal
curvature as an intrinsic sufficient condition. A theorem may choose the
raw gauge and exploit the specific restored character, but it must prove a
new actual-symbol inequality; none is present.

There is also a gauge-robust narrow class. Put

\[
 c=\frac{\lambda}{R}\sqrt{\frac hk},qquad
 Q=\frac{\mu^2h}{d^2k}=Xc^2,qquad A=\frac{k'}k.
\tag{136.9}
\]

For fixed \(c\), the second and third coordinates of both gradient
families obey \(G_2+cG_3=0\), so every three-gradient determinant on the
ruling vanishes. Direct substitution gives

\[
 \rho=hk'\frac{c^2-1}{c^2},qquad
 \Delta=hk\frac{A^2-c^2}{c^2}.
\tag{136.10}
\]

The gates remove collars but not the ruling; for \(k'=k\),
\(\Delta=-\rho\). This is an exact gate/routing control, not a
nonvanishing theorem for a physical packet.

Finally, the audited capacities are \(L^5\) for aliaswise \(\ell^1\) and
\(L^4\) for the positive square shadow at \(d=1\), against target
\(L^3\). Same-parity reciprocal clusters of cardinality
\(\gg d^2L^2\) exist on a fixed admissible slice, but their weighted
\(dL\) and unit square masses are only upper/adversarial capacities. No
common \(v\)-run, actual lower mass, or physical lower bound is promoted.
The exact identity \(\sum_{d\mid n}\gamma_d/d>0\) is retained only as a
leading common-profile control, not as positivity of (136.7).

## 4. First doubtful or unproved step

The first broad-side gap is an owner-preserving scalar theorem that turns
a gauge-explicit joint geometric separation into a factor \(L^{-1}\) while
retaining the actual coefficient class and returning to the one fixed
block. A determinant lower bound alone is not such a theorem.

The first independent narrow-side gap is a signed estimate for (136.7)
and the fixed-\(Q\) or same-denominator classes, jointly with
\(b_B(h,k)\), \(\chi_4(h)\), both gates, and every profile. The residue
phase alone is the wrong carrier, while the complete carrier is coherent
across equal-rational lifts.

A phase-adapted bounded-amplitude array validly falsifies any theorem
uniform over arbitrary arrays satisfying only the displayed magnitude
bound. It need not be the literal stationary amplitude and is not a lower
bound. The displayed second-B calculation returns the square-root critical
action and arithmetic lattice only; it proves neither a new saving nor a
full profile/owner return without a separate ledger.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| literal kernel and owner ledger | Green. Every bulk label is retained and no accepted error owner is reopened. |
| divisor progression and distinct lifts | Green. Equations (136.6)--(136.7) keep every lift distinct. |
| character and residue phase | Green after repair. The full combined carrier is (136.1), not the residue-only multiplier. |
| equal-rational lifts | Green as coherence. The carrier and gates are common; amplitudes and progression owners remain distinct. |
| joint broad partition | Diagnostic. The gauged surface-normal partition is entirely narrow, whereas raw normal and gradient-vector partitions may have broad triples. |
| determinant reconciliation | Green. Gradient vectors, surface normals, and one-body Hessians are not conflated. |
| broad capacity to \(L^3\) | No-go. There is no scalar norm interface, and positive capacity remains \(L^4\). |
| fixed-\(Q\) ruling | Green. Equations (136.9)--(136.10) survive the gauge and both gates. |
| same-denominator cluster | Green only as fixed-slice cardinality and adversarial capacity; no common-run or actual-mass theorem is asserted. |
| opposite-character and phase-adapted packets | Green as controls. No weight-preserving involution or physical lower bound is inferred. |
| second B-process | Canonical phase self-return only. No complete owner return is charged. |
| scalar versus positive energy | Green. The positive shadow is not substituted for the signed scalar. |
| boundary and transition scope | Green. No equality, collar, crossing, transition, or remainder is double-owned. |
| full downstream scope | Green. No BAL parent, M9-M2, endpoint, M9, quarter, or exponent claim is closed. |

No computation or external theorem was used. Round 136 is 100% algebraic
and analytic.

## 6. Dependencies and exact artifacts used

The adjudication uses:

- `protocol.md`;
- `state/proof_obligations.yml` at the starting hash above;
- `state/active_campaign.yml`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- the Round-136 blind statement and all three task briefs;
- all three Round-136 primary reports;
- all three post-unmask Round-136 reviews; and
- `candidates/conductor_round136_character_gauge_ruling_obstruction.md`.

No web source, numerical experiment, or unaccepted external theorem enters
the adjudication.

## 7. Recommended state effect

Create one exact character-restoration/coherence node and one scoped
broad--narrow obstruction node. Add Round-136 evidence and the new
obstruction dependency to the open oscillatory remainder, actual energy,
and balanced packet nodes.

Reject automatic lift cancellation, merging equal-rational lifts, removal
of fixed-\(Q\) rulings by the gates, a scalar gain from any determinant
without its operator theorem, intrinsic empty-broad language, positivity of
the full literal amplitude from \(\sum\gamma_d/d>0\), full second-B owner
return without a ledger, any physical-lower-bound reading of adversarial
capacities, and any exponent improvement.

Keep M9-M1, M9-M2, endpoint uniformity, M9, the conditional bridge, the
internal \(1/3\) theorem, the repaired external Li--Yang benchmark, and the
quarter target unchanged. Reopen BAL only for a genuinely new
gauge-sensitive, noninvertible actual-symbol theorem; otherwise rotate to a
different open owner.
