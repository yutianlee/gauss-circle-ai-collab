# Conductor candidate: character restoration and the gauge-sensitive broad--narrow obstruction

Round: 136

Starting graph SHA-256:
`c43058006cec6849cd17a49e6a7a5298f5a3c124b34d2333b3279adcb54da1d1`

Status: reconciled conductor candidate. It remains evidence rather than
accepted mathematics until all Round-136 reviews are green and the State
Patch is validated and applied.

## 1. Result

Round 136 closes under `broad_narrow_no_go`, not under a bound for the
literal balanced kernel. The exact new algebraic fact is

\[
 e\!\left(-\frac{\lambda h}{2}
       +s_d\left(\frac12-\lambda\right)\right)
 =-i(-1)^m\chi_4(d)\chi_4(h),
 \qquad \lambda=\frac{1/2-m}{d}.
\tag{136.C1}
\]

If \(2\lambda=a/b\) is reduced, with \(a,b\) odd, all literal lifts are

\[
 (d,\mu)=(bc,ac/2),\qquad c\ \mathrm{odd},
\tag{136.C2}
\]

and

\[
 (-1)^m\chi_4(d)=\chi_4(ab).
\tag{136.C3}
\]

Thus equal-rational-\(\lambda\) lifts have a common complete exponential
and character carrier. Their \(\gamma_{bc}\), progression intervals,
amplitudes, and labels remain distinct, so coherence neither merges them
nor proves that their physical sum is large.

The proposed broad--narrow proof has two independent exact failures. First,
the apparent outer-gradient geometry changes under the exact modulation
(136.C1): in particular, the raw gradient-image surface can have transverse
normals, whereas the gauged gradient-image surface is cylindrical. A
coefficient-modulation-invariant broad theorem cannot charge that raw
surface-normal determinant as a representation-independent certificate.
Second, neither that determinant nor the distinct determinant of three raw
gradient vectors has a proved inequality converting it into a gain for the
one fixed scalar kernel. Exact
fixed-\(Q\) rulings survive both gauges and both strict gates, while the
available positive square capacity remains \(L^4\), one factor \(L\) above
the \(L^3\) target.

This is a scoped obstruction to the audited geometric/positive-capacity
mechanism. It is not a lower bound, a disproof of BAL, or a universal no-go
for a future theorem using the literal signed amplitudes jointly.

## 2. Exact statement and hypotheses

Consider the complete interior bulk kernel

\[
 \mathcal K_B^{\mathrm{bulk}}
 =\sum_{h\ \mathrm{odd},k,k'}b_B(h,k)
  \sum_{\substack{d\mid k'\\d\ \mathrm{odd}}}\gamma_d
  \sum_J\sum_{\substack{\mu\in\mathbb Z+1/2,\ \mu>0\\t_*\in J}}^{\mathrm{bulk}}
  \mathcal A_{d,J}(h,k,k';\mu)e(\Theta_{d,\mu}),
\tag{136.C4}
\]

where

\[
 \begin{gathered}
 h+2s_d=d\ell_d,\qquad \mu=\frac12-m,\qquad
 \lambda=\frac\mu d,\qquad x_*=\frac{Xk'}{\lambda^2},\\
 \Theta_{d,\mu}=R\sqrt{hk}-\frac{Xk'}{2\lambda}
 -\frac{\lambda h}{2}+s_d\left(\frac12-\lambda\right),
 \qquad R=\sqrt X,\quad L\asymp X^{1/6}.
 \end{gathered}
\tag{136.C5}
\]

There are \(O(L^3)\) outer triples, \(\mu\asymp dL^3\), and
\(|\mathcal A_{d,J}|\ll(dL)^{-1}\). Every bulk atom retains both strict
gates

\[
 \rho=hk'-x_*k,\qquad \Delta=x_*k'-hk,
 \qquad |\rho|,|\Delta|>L.
\tag{136.C6}
\]

All divisor lifts, profiles, crossings, equality conventions, and the fixed
block remain literal. Boundary, transition, nonstationary, crossing, and
stationary-remainder terms stay with their already proved owners and are not
used again.

The accepted scoped proposition is only this:

> Equations (136.C1)--(136.C3) are exact. They make equal-rational lifts
> character-coherent and leave both gates invariant across those lifts. The
> raw and gauged gradient descriptions are exactly equivalent discrete
> descriptions but have different apparent broad geometry. The standard
> coefficient-uniform determinant, positive cap, spacing, and second-
> B-process mechanisms therefore do not prove
> \(|\mathcal K_B^{\mathrm{bulk}}|\ll L^3X^\varepsilon\). Exact fixed-
> \(Q\) narrow rulings survive both gates. The complete signed kernel remains
> the smallest owner-complete open object.

## 3. Proof and reconciliation

Because \(h+2s_d=d\ell_d\),

\[
 -\frac{\lambda h}{2}
 +s_d\left(\frac12-\lambda\right)
 =\frac{s_d}{2}-\frac{\mu\ell_d}{2}.
\tag{136.C7}
\]

Since \(\mu=1/2-m\) and \(\ell_d\) is odd,

\[
 e\!\left(\frac{s_d}{2}-\frac{\mu\ell_d}{2}\right)
 =-i(-1)^{s_d+m}\chi_4(\ell_d).
\]

The congruence \(d\ell_d=h+2s_d\pmod4\) gives
\((-1)^{s_d}\chi_4(\ell_d)=\chi_4(d)\chi_4(h)\), proving
(136.C1). For (136.C2), reduce \(2\mu/d=a/b\). Then
\(d=bc\), \(2\mu=ac\), and oddness forces \(c\) odd. Moreover

\[
 m=\frac{1-ac}{2},\qquad
 (-1)^m=\chi_4(ac),qquad
 (-1)^m\chi_4(bc)=\chi_4(ab),
\]

which proves (136.C3). Hence the full carrier on an equal-rational ruling is

\[
 -i\chi_4(h)\chi_4(ab)
 e\!\left(R\sqrt{hk}-\frac{Xbk'}a\right),
\tag{136.C8}
\]

independent of \(c\). Since \(x_*=Xk'/\lambda^2\), both gates are also
independent of \(c\). This proves coherence, not cancellation and not
coefficient identification.

To reconcile the geometric calculations, put

\[
 r=\sqrt{k/h},\qquad z=\lambda/R.
\]

Before (136.C1) is moved into the coefficients, the normalized outer
gradient is

\[
 \Sigma_0(r,z)=(r-z,r^{-1},-z^{-1}).
\tag{136.C9}
\]

After the exact gauge, the remaining smooth phase has normalized gradient

\[
 \Sigma_1(r,z)=(r,r^{-1},-z^{-1}).
\tag{136.C10}
\]

The normal surface for (136.C10) has normals proportional to
\((1,r^2,0)\), so a three-**surface-normal** broad part defined from this
gauged surface is empty. The raw surface (136.C9) has normals proportional
to \((1,r^2,z^2)\) and can have a nonzero three-normal determinant. The
determinant of three points \(\Sigma_i\) on either gradient surface is a
third object and can also be nonzero. None of these facts is a universal
geometric theorem about the literal scalar: (136.C9) and (136.C10) are
related by the exact discrete character modulation (136.C1). A
coefficient-uniform estimate must survive that modulation; a gauge-sensitive
estimate must explicitly exploit the restored carrier. No such scalar
estimate is proved here.

There is also a common narrow class in both descriptions. Set

\[
 c=\frac zr=\frac{\lambda}{R}\sqrt{\frac hk},
 \qquad Q=\frac{\mu^2h}{d^2k}=Xc^2.
\tag{136.C11}
\]

For fixed \(c\), both gradient families lie in a fixed plane because their
second and third coordinates satisfy \(G_2+cG_3=0\). Thus every
three-gradient determinant on this ruling is zero. If \(A=k'/k\), the
gates become exactly

\[
 \rho=hk'\frac{c^2-1}{c^2},\qquad
 \Delta=hk\frac{A^2-c^2}{c^2}.
\tag{136.C12}
\]

They exclude only collars about \(c^2=1\) and \(c^2=A^2\); they do not
remove fixed-\(c\) rulings. For \(k'=k\), \(\Delta=-\rho\), and strict
double-far points occur immediately beyond the common gate collar. This is
a routing and capacity obstruction, not a proof that the literal
amplitudes add positively on such a packet.

At scale \(L^{-1}\), the already audited alias ledger has \(L^5\)
triangle capacity and \(L^4\) positive square capacity at \(d=1\).
Same-denominator, same-parity reciprocal clusters of size
\(\gg d^2L^2\) remain after the two \(O(dL^2)\) gate collars. Their
character is constant, but their literal amplitudes need not have one sign.
Consequently positive cap or spacing control still misses the target by a
factor \(L\). A phase-adapted bounded-amplitude array can align transverse
terms, which rules out a coefficient-uniform scalar theorem based only on
the displayed size hypotheses. It is only an adversarial method control,
not a physical lower bound.

For the formal leading \(b=1\) common-profile subcase, the divisor algebra

\[
 \sum_{d\mid n}\frac{\gamma_d}{d}
 =\sum_{r\mid n}\frac{\eta(r/G_0)}r
   \frac{\varphi(n/r)}{n/r}>0
\tag{136.C13}
\]

is exact when the cutoff \(\eta\) is nonnegative. It shows that the signed
divisor expansion itself does not force cancellation. It is not promoted
as a positivity statement for the complete literal amplitude, whose
\(J\)-labels, profiles, and lift dependence remain distinct.

## 4. First doubtful or unproved step

On the broad side, the first unproved step is an owner-preserving
inequality that turns a gauge-sensitive joint determinant into an
\(L^{-1}\) gain for the single fixed-block scalar while retaining the exact
carrier (136.C1), the literal amplitude, and both gates. No spatial or
parameter norm with a proved return map to that scalar has been supplied.

On the narrow side, the first unproved step is a signed estimate for the
complete equal-lift and fixed-\(Q\) packets, schematically

\[
 \sum_{c\ \mathrm{odd}}\gamma_{bc}
 \sum_J\mathcal A_{bc,J}(h,k,k';ac/2),
\tag{136.C14}
\]

jointly with \(\chi_4(h)\), the outer variables, profiles, and both gates.
Divisor \(\ell^1\), same-denominator spacing, positive row energy, or a
second B-process proves no such estimate. The displayed second-B stationary
calculation returns the original square-root critical action and arithmetic
lattice, so it creates no new phase direction. A full return of profiles,
\(J\)-pieces, gates, transitions, and remainder owners would require a new
ledger and is not asserted here.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| literal bulk kernel and owner ledger | Green. Only the interior stationary bulk is reopened; every accepted error owner is used zero additional times. |
| divisor progression and distinct lifts | Green. Equations (136.C2), (136.C8), and (136.C14) retain all lift labels and amplitudes. |
| joint broad partition | Diagnostic only. A gauged surface-normal partition is entirely narrow; raw surface-normal and gradient-vector partitions can have broad triples. These are different geometric objects, and none supplies the missing scalar inequality. |
| gauge reconciliation | Green. The difference between (136.C9) and (136.C10) is exactly the character modulation (136.C1), not an approximation. |
| broad capacity to \(L^3\) | No-go. The positive shadow is \(L^4\), and phase-adapted bounded coefficients refute a coefficient-uniform scalar gain. |
| narrow ruling classification | Green at the exact fixed-\(Q\) and equal-rational-\(\lambda\) seams. No claim that these exhaust every possible useful arithmetic decomposition is made. |
| actual character and residue phase | Green after repair. The combined linear/residue carrier is (136.C1); residue alone is not the complete object. |
| coupled gates | Green. Equation (136.C12) shows that fixed-\(Q\) rulings and equal-rational lifts are not split by the gates. |
| coherent and opposite-character packets | Green as a method control. Coherent classes exist, but no literal positive lower bound or weight-preserving opposite-class involution is asserted. |
| scalar versus positive energy | Green. Positive square capacity is not substituted for the signed scalar target. |
| boundary and transition scope | Green. No collar, crossing, incomplete stationary term, or remainder is double-owned. |
| downstream scope | Green. BAL, M9-M2, M9-M1, endpoint uniformity, M9, and every global exponent remain unchanged. |

No numerical experiment or external theorem is used; the round is 100%
algebraic and analytic.

## 6. Dependencies and exact artifacts used

This candidate uses:

- `protocol.md`;
- `state/proof_obligations.yml` at the starting graph hash above;
- `state/active_campaign.yml`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/blind_statement.md`;
- all three Round-136 primary reports;
- the accepted Round-115 and Round-116 syntheses named in the campaign;
- the three Round-136 post-unmask seam reviews, once completed.

No web source, numerical computation, or sibling-derived statement was used
inside the statement-only rederivation before unmasking.

## 7. Provisional state effect

Promote (136.C1)--(136.C3) as an exact character-restoration lemma and
promote the reconciled, scoped broad--narrow obstruction. Reject claims
that equal-rational lifts cancel automatically, that they may be merged,
that the two gates remove the fixed-\(Q\) rulings, that either the raw or
gauged determinant alone yields a scalar saving, that positive \(L^4\)
capacity is the signed target, or that an adversarial coefficient control
is a lower bound for the physical kernel.

Retain the oscillatory remainder, actual double-far energy, balanced
quarter packet, full M9-M2, both M9-M1 parents, endpoint uniformity, M9,
the internal exponent \(1/3\), the external Li--Yang benchmark, and the
quarter target unchanged. Reopen BAL only for a genuinely new
gauge-sensitive, owner-preserving actual-symbol inequality; otherwise
rotate to a distinct open owner.
