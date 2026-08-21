# Complete trace/spectral attack on the canonical hard M1 Gram

## 1. Result: lemma or no-go result.

**Lemma (actual-symbol two-row self-return; no independent \((d,u)\)-spectral gain).**  On the literal Round-92 hard complement, opening the completed trace and making the unimodular change of variables

\[
 r=n+d+u,\qquad s=m+d
\]

turns every fourfold stationary atom into a Gram atom

\[
 I_b(r)\overline{I_b(n)}\,
 \overline{I_b(s)}I_b(m)=Z_{b}(r,n)\overline{Z_b(s,m)}
\]

and turns the purportedly two-dimensional stationary phase into the difference of two one-row phases.  The nonzero Hessian determinant in \((d,u)\) is therefore the determinant of a tensor product after an integral change of lattice coordinates, not a new joint curvature.  Double Poisson/B-process is exactly the two one-row inverse transforms already present in the four normalized physical rows.  The outer factor \(M\) in \(\mathfrak T_M\) changes \(M^{-5}\) to \(M^{-4}\), exactly matching those four rows, so there is neither a spare factor of \(M\) nor a new factor \(J^{-1/5}\).

The Fejer factor becomes the difference kernel

\[
 W_U^\circ(r-n-s+m),\qquad
 W_U^\circ(v)=(U-|v|)\mathbf 1_{0<|v|<U},
\]

whose Fourier polynomial is \(|D_U|^2-U\).  Thus recompletion reconstructs the same centered Toeplitz Gram.  Prime-power period descent gives the already accepted exact self-return, and the arithmetic owner mask is not a smooth amplitude to which a uniform two-dimensional B-process can be applied.

Consequently the tempting estimate “nonzero two-dimensional Hessian saves \(J^{-1/5}\), hence beats the required \(J^{-1/6}\)” is a rigorous no-go: it double-counts the row transform already used in

\[
 \mathsf C_{\rm Gram}={U\over B}
 \bigl(B^3T^2Q^{-5/12}\bigr)^2.
\]

Likewise, an unrestricted high-trace/operator-norm argument cannot use conductor-row oscillation: the exact global operator is a direct sum in \(b\).  The actual fourfold phase is a diagonal Gram gauge and telescopes on paired trace cycles.  At the full-degree \(2\)-adic control \(q=8\), the complete local phase is itself a coboundary, so it supplies no random-phase spectral gap.  A successful estimate would have to be a directional estimate for the fixed actual vector, jointly with the literal hard mask (and, if desired, cancellation in the scalar sum over \(b\)); it cannot be a coefficient-uniform norm bound or a post-absolute-value trace estimate.

This report proves no part of the boxed hard estimate and no strict hard subrange.  It proves a scoped equal-capacity/self-return obstruction to the proposed Hessian, double-completion, and coefficient-uniform high-trace mechanisms.

## 2. Exact statement and hypotheses.

Put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},
 \qquad J^{11/90}<B\leq J^{3/20},\qquad M\asymp B,
\]

and let \(U\) be any accepted deep dyadic length.  Use the literal successive complement

\[
 \mathscr H_{b,U}=\mathscr U_{b,U}\setminus
 (\mathscr O_{87}\sqcup\mathscr O_{88,c}
 \sqcup\mathscr O_{88,g}\sqcup\mathscr O_{89}),
\]

with \(u=0\) removed once globally.  No owner set is enlarged.  All three classes, signs, aliases, reflected orientations, centered Ramanujan terms, the full \(2\)-part, nonunit \(K\), nonzero modulus multiples, prime powers, and the actual support/zero extension of \(I_b\) remain in the state space.

For a physical pair \(P=(x,x-A)\), define its exact frequency atom

\[
\begin{aligned}
 Z_{b,P}(r,n)
 ={}&M^{-2}\pi_{b,U}(r-n)
 I_b(r)\overline{I_b(n)}\\
 &\times e_M\!\left(rx+n(A-x)
 +K(\bar x-\overline{x-A})\right),
\end{aligned}
\]

where \(\pi_{b,U}\) is the actual signed dyadic multiplier, including zero extension.  Put \(k(r,n)=r-n\).  The analogous definition for \(P'=(x-V,x-V-B_2)\) uses its own physical endpoints.  Flatten the remaining finite labels (class, sign, alias, orientation, stationary branch, physical pair, and frequency pair) into \(\alpha\).  Then the hard contribution has the exact directional block form

\[
 \mathcal E_{\rm hard}(U)
 =\sum_b\sum_{\alpha,\beta\,\text{over }b}
 Z_\alpha\overline{Z_\beta}\,
 W_U^\circ(k_\alpha-k_\beta)
 \mathbf 1_{\mathscr H_{b,U}}(\alpha,\beta),                 \tag{2.1}
\]

with the accepted incidence multiplicities.  Formula (2.1) is a definition by the unique physical coordinates and is not a replacement by arbitrary coefficients.  In particular the actual \(I_b\) occurs four times in every matrix coefficient.  Conjugation closure makes the resulting quadratic form real.

On a smooth stationary interior patch only, write the chosen actual branch as

\[
 I_b(t)=a_b(t)e(\psi_b(t)),\qquad
 \psi_b(t)=\epsilon_\psi\lambda_b\sqrt t,
\]

with the actual amplitude \(a_b\), support, and class constants unchanged.  Assume the audited stationary range in which

\[
 |\psi_b''(t)|={|\lambda_b|\over4t^{3/2}}\asymp J^{-1/5}.
\]

No smoothness is assumed across entry/exit or across \(\mathbf 1_{\mathscr H_{b,U}}\); there the exact zero extension and arithmetic mask are retained.

The current and target Gram scales are

\[
\begin{aligned}
 \mathsf C_{\rm Gram}
 &= {U\over B}B^6T^4Q^{-5/6},\\
 \mathsf T_{\rm Gram}
 &= {U\over B}J^{14/5},\\
 {\mathsf T_{\rm Gram}\over\mathsf C_{\rm Gram}}
 &=J^{11/15}B^{-6}.                                      \tag{2.2}
\end{aligned}
\]

At \(B=J^{3/20}\), (2.2) is \(J^{-1/6}=B^{-10/9}\).  The no-go statement is that the \((d,u)\) Hessian, its factorized double B-process, conductor-block high traces, local period descent, and coefficient-uniform spectral cancellation do not produce this ratio.  It does **not** assert that the fixed actual vector has a large Rayleigh quotient; that stronger lower bound is not determined by the selected packet.

## 3. Proof or derivation.

**Exact opening and the missing \(M\)-factor audit.**  Open the completed trace in one literal hard atom:

\[
 \mathfrak T_M(u,A,B_2,V)
 =M\sum_x^{\rm four\ units}
 e_M\!\left(ux+K\Phi_{A,B_2,V}(x)\right).
\]

The prefactor \(M\) turns \(M^{-5}\mathfrak T_M\) into \(M^{-4}\) times the base-point sum.  Set

\[
 r=n+d+u,\qquad s=m+d;qquad
 d=s-m,\quad u=r-n-s+m.                                  \tag{3.1}
\]

This is a bijection of \(\mathbb Z^4\) with determinant of absolute value \(1\).  The modular linear phase becomes

\[
\begin{aligned}
 dV+nA-mB_2+ux
 ={}&rx+n(A-x)+s(V-x)\\
 &+m(x-V-B_2).                                           \tag{3.2}
\end{aligned}
\]

Together with

\[
 K\Phi=K(\bar x-\overline{x-A})
 -K(\overline{x-V}-\overline{x-V-B_2}),
\]

(3.2) factors the whole actual symbol and arithmetic phase as

\[
 Z_{b,(x,x-A)}(r,n)
 \overline{Z_{b,(x-V,x-V-B_2)}(s,m)}.                    \tag{3.3}
\]

There are four factors \(M^{-1}\) in the four normalized rows, hence exactly \(M^{-4}\).  Thus (3.3) has precisely the normalization obtained by opening \(\mathfrak T_M\); no factor \(M^{\pm1}\) remains available for a saving.

For clarity, temporarily suppress only the hard incidence indicator, not the actual weights.  Since

\[
 W_U^\circ(v)=\int_{\mathbb T}
 (|D_U(\theta)|^2-U)e(-v\theta)\,d\theta,
\]

the \(r,n,s,m\) sum in (3.3) factors under this integral into

\[
 \mathcal R_{b,x}(-\theta)
 \overline{\mathcal R_{b,x-A}(-\theta)}
 \overline{\mathcal R_{b,x-V}(-\theta)}
 \mathcal R_{b,x-V-B_2}(-\theta),                        \tag{3.4}
\]

with the two accepted deep multipliers inserted.  Formula (3.4) is the original centered four-row Fejer Gram.  Restoring the literal hard indicator merely restricts its physical-pair incidences and arithmetic fibres; it does not create another transform.

**Hessian audit.**  For fixed \(n,m\), the nonconstant stationary phase in \((d,u)\), up to sign and linear modular terms, is

\[
 \phi(d,u)=\psi_b(n+d+u)-\psi_b(m+d)=\psi_b(r)-\psi_b(s).
\]

With

\[
 L={\partial(r,s)\over\partial(d,u)}
 =\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad \det L=-1,
\]

one has the exact congruence

\[
 \nabla^2_{d,u}\phi
 =L^{\!T}
 \begin{pmatrix}\psi_b''(r)&0\\0&-\psi_b''(s)\end{pmatrix}L. \tag{3.5}
\]

Consequently

\[
 \det\nabla^2_{d,u}\phi
 =-\psi_b''(r)\psi_b''(s)
 =-{\lambda_b^2\over16r^{3/2}s^{3/2}}\asymp-J^{-2/5},   \tag{3.6}
\]

and both eigenvalues have magnitude \(\asymp J^{-1/5}\) on the stated interior patch.  Equations (3.5)--(3.6) verify the proposed Hessian calculation but also identify its meaning: \(L\in GL_2(\mathbb Z)\), so the dual lattice is carried bijectively to the product dual lattice by \(L^{-T}\).  A double B-process is exactly a B-process in \(r\) and one in \(s\).  The Fejer strip is

\[
 0<|r-s+m-n|<U
\]

with weight \(U-|r-s+m-n|\); Fourier inversion gives (3.4).  Applying a two-dimensional stationary-phase factor \(J^{-1/5}\) on top of the already normalized rows therefore counts the same two row oscillations twice.

Entry and exit do not repair the argument.  On each interior patch (3.5) is exact.  Across a support boundary the zero-extended amplitude is not a uniform smooth B-process amplitude; one may use exact incomplete sums or return to (3.4), but one may not claim the interior determinant uniformly.  The same problem is stronger for \(\mathbf1_{\mathscr H}\), which has divisor, congruence, period-depth, and projection conditions in \(u\).

**Global block and trace moments.**  Equation (2.1) gives

\[
 \mathbb K_U=\bigoplus_{b\asymp B}\mathbb K_{b,U}.        \tag{3.7}
\]

Therefore

\[
 \|\mathbb K_U\|=\max_b\|\mathbb K_{b,U}\|,
 \qquad
 \operatorname {Tr}(\mathbb K_U\mathbb K_U^*)^\ell
 =\sum_b\operatorname {Tr}(\mathbb K_{b,U}
 \mathbb K_{b,U}^*)^\ell.                               \tag{3.8}
\]

There are no mixed-\(b\) closed walks in (3.8).  Hence conductor-row oscillation is unavailable to an ordinary norm or trace moment of the exact operator.  It can only be used in the fixed scalar sum \(\sum_b\langle Z_b,\mathbb K_{b,U}Z_b\rangle\), before replacing that sum by a norm.

The phase of the actual symbol also gives no generic high-trace cancellation.  In (3.3) it is a diagonal gauge: an edge \(\alpha\to\beta\) contains \(Z_\alpha\overline{Z_\beta}\).  On every reflected two-cycle,

\[
 (Z_\alpha\overline{Z_\beta})
 (Z_\beta\overline{Z_\alpha})
 =|Z_\alpha Z_\beta|^2.                                 \tag{3.9}
\]

More generally, its phase telescopes on a closed walk.  The following moment diagonals are therefore compulsory.

- The literal \(u=0\) edge is absent and owned once globally, but a two-step walk with shifts \(u,-u\), both nonzero, survives and gives (3.9).  It is not the \(u=0\) owner.
- Sign, alias, orientation, and reflection closure guarantees the reverse edge needed for these paired cycles.
- Under CRT, a paired global cycle closes at each prime power.  Repeated visits to the same prime-power residue are correlated collisions, not independent generic trace functions.
- If a local weight descends from \(p^\nu\) to \(p^{\nu-j}\), the accepted identity

  \[
  q^{-2}\sum_{u\bmod q}\mathfrak T_q(u)e_q(-ux)
  =(q/p^j)^{-2}\sum_{u'\bmod q/p^j}
  \mathfrak T_{q/p^j}^{\downarrow}(u')e_{q/p^j}(-u'x)
  \]

  shows that the \(p^{2j}\) trace factor cancels the quotient-square normalization.  Restricting Fejer shifts to \(p^j\mid u\) rescales their count and weight but yields the same total normalized mass.  Every repetition of this step in a high moment is another exact self-return.
- Perfect-square and fourth-power indices are contained with weights \(|I_b(t)|\).  Paired trace cycles cancel the radical phases by multiset equality, whether or not an index is a perfect power; perfect powers can create additional coherence but cannot be deleted or credited with cancellation.  No count of them is used here.

A non-backtracking trace does not evade (3.9): it estimates a different polynomial in \(\mathbb K\).  Removing the paired cycles from the original quadratic form would require a new disjoint owner and an exact subtraction identity.  No such owner is present.

**The exact \(q=8\) control.**  For \(M=8\), every unit is its own inverse.  If the four physical points are units, then \(A,B_2,V\) are even and the unit mask is all four odd residues.  Directly,

\[
 \Phi_{A,B_2,V}(x)\equiv A-B_2\pmod 8
\]

and

\[
 \mathfrak T_8(u,A,B_2,V)
 =8e_8(K(A-B_2))c_8(u),                                  \tag{3.10}
\]

where

\[
 c_8(u)=
 \begin{cases}
 4,&8\mid u,\\
 -4,&u\equiv4\pmod8,\\
 0,&4\nmid u.
 \end{cases}
\]

Thus every nonzero surviving multiple of \(4\) has trace magnitude \(32=M^2/2\), and

\[
 e_8(K(A-B_2))=e_8(KA)\overline{e_8(KB_2)}               \tag{3.11}
\]

is a coboundary.  It remains a coboundary for nonunit \(K\), becoming still more coherent when \(K\) has large \(2\)-adic valuation.  Along a local closed walk, (3.11) telescopes.  Hence the accepted full-degree \(q=8\) residual cannot contribute a local random-phase saving; after diagonal conjugation its local transfer is nonnegative.  The formula also retains nonzero modulus multiples \(8\mid u\), so the global \(u=0\) deletion does not remove this control.

**Quantitative norm barrier and its exact scope.**  At one modulus there are

\[
 N_b=\varphi(M)(\varphi(M)-1)=B^{2+o(1)}
\]

ordered physical-pair states.  A coefficient-uniform matrix normalized to absolute row capacity \(1\), with at most \(N_b\) entries in a row which attains that capacity, obeys

\[
 \|K\|_{2\to2}\geq\|\text{that row}\|_2
 \geq N_b^{-1/2}=B^{-1+o(1)}.                            \tag{3.12}
\]

At the top conductor the requested gain is

\[
 J^{-1/6}=B^{-10/9},
\]

which is smaller than (3.12) by \(B^{-1/9+o(1)}\).  Even ideal square-root cancellation among \(B^2\) full-degree physical states is therefore insufficient for a **coefficient-uniform** spectral norm.  The centered Fejer direction supplies no extra random dimension: on an interval of \(U\) consecutive differences, the off-diagonal Toeplitz matrix

\[
 (U-|d-d'|)\mathbf1_{0<|d-d'|<U}
\]

has constant-vector Rayleigh quotient \(\asymp U^2\), comparable with its Schur norm.  Nor does the direct sum (3.7) supply a square root of the number of conductor rows.  The only remaining possible source of the extra \(B^{-1/9}\) in such a strategy is a theorem about the fixed actual-vector projection, an arithmetic sparsity of its mass that is proved rather than assumed, or signed scalar cancellation across \(b\).

Equation (3.12) is deliberately an audit of the arbitrary-coefficient shadow.  It is not promoted to a lower bound for the literal actual vector, since the selected context gives no lower mass estimate for its projection on the capacity-attaining row.

## 4. First doubtful or unproved step.

The first genuinely unproved step in every positive spectral version is the directional estimate

\[
 \left|\sum_b\langle Z_b,
 \mathbb K^{\rm hard}_{b,U}Z_b\rangle\right|
 \ll_\varepsilon X^\varepsilon
 J^{11/15}B^{-6}\,\mathsf C_{\rm Gram},                  \tag{4.1}
\]

for the fixed actual atoms \(Z_b\), with the literal successive-complement mask.  Neither a bound for \(\|\mathbb K^{\rm hard}_{b,U}\|\) nor the Hessian determinant proves (4.1).

There are two precise missing inputs.  First, the mask left by Rounds 87--89 is arithmetic in the physical labels and in the Fejer shift; it is not supplied as a bounded-variation or uniformly smooth amplitude on \((d,u)\).  Splitting it into period fibres invokes the exact prime-power self-return above, while Fourier-expanding a general residual mask may have capacity-sized \(\ell^1\) mass.  Second, the selected packet supplies an upper row bound but no quantitative theorem forcing the actual \(|I_b|\)-mass to avoid the Perron/coherent subspaces of the residual transfer matrices.  Full directed degree alone is not a lower bound for that actual projection.

Accordingly, this report does not assert a global equal-capacity lower bound for \(\mathcal E_{\rm hard}\), does not prove (4.1), and does not identify a new hard owner.  Its proved conclusion is only that the proposed \((d,u)\) curvature and coefficient-uniform trace mechanisms cannot serve as the missing input.

## 5. Control tests and outcomes.

| Required control | Outcome |
|---|---|
| Canonical operator normalization | Passed.  Opening \(\mathfrak T_M\) gives \(M^{-4}\), exactly four normalized rows.  The capacity/target ratio is \(J^{11/15}B^{-6}\), equal to \(J^{-1/6}=B^{-10/9}\) at the top. |
| Prior-owner one-count | Passed.  The operator uses the literal successive complement \(\mathscr H\); no R87, R88, or R89 term is reintroduced or reassigned. |
| \(u=0\) and Ramanujan ownership | Passed.  \(W_U^\circ\) has zero \(u=0\) coefficient.  Nonzero paired shifts and modulus multiples remain.  Centered Ramanujan coordinates remain inside the actual physical-row vector and are not declared diagonal. |
| All classes, signs, aliases, reflections | Passed algebraically.  Equations (3.1)--(3.5) are class-independent; the corresponding class constants stay in \(I_b\) and \(K\).  Conjugation closure is used only to identify reverse trace edges. |
| Actual fourfold symbol | Passed.  It is retained exactly as \(I_b(r)\bar I_b(n)\bar I_b(s)I_b(m)=Z_\alpha\bar Z_\beta\); no arbitrary replacement is used in the no-go lemma. |
| Global trace-moment expansion | Passed as an obstruction audit.  Conductor blocks do not mix, actual phases telescope on closed walks, and nonzero \(u,-u\) backtracks survive.  A non-backtracking trace would require a new subtraction identity. |
| Required \(J^{-1/6}\) gain | Failed for the proposed mechanism.  The apparent \(J^{-1/5}\) Hessian gain is the existing pair of row transforms.  A coefficient-uniform square-root norm on \(B^2\) states reaches only \(B^{-1}\), short of \(B^{-10/9}\) by \(B^{-1/9}\). |
| \(q=8\) full-degree control | Passed.  Equations (3.10)--(3.11) give magnitude \(M^2/2\) on \(4\mid u\) and an exactly gauge-removable phase.  No local spectral cancellation is available. |
| Prime powers and full \(2\)-part | Passed.  Repeated-prime paired cycles are compulsory; exact descent cancels the quotient-square normalization.  The full \(2\)-adic obstruction is retained rather than modeled by an odd squarefree theorem. |
| Nonunit \(K\) and modulus multiples | Passed.  Formula (3.10) holds for every \(K\); nonunit \(K\) does not break the coboundary.  Nonzero \(8\mid u\) terms remain after the sole \(u=0\) deletion. |
| Perfect-square/fourth-power resonance | Passed as a no-deletion audit.  Their actual \(I_b\)-weights remain.  Paired trace phases cancel exactly, and perfect powers may add coherence; no unproved density saving is assigned to them. |
| Arbitrary-coefficient false shadow | Passed as a falsifier, not as evidence for the target.  The Frobenius/row bound (3.12) shows why a coefficient-uniform norm theorem cannot reach the requested exponent.  No conclusion about the fixed actual projection is inferred from it. |
| Absolute-value false shadow | Failed, as required.  Absolute values before the \(b\), shift, or four-row sums leave the Schur capacity and erase the only possible directional cancellation. |
| Transform self-return | Passed.  The integral lattice change has determinant \(1\), Fejer inversion gives the original Gram, and opening/recompletion has no residual \(M\)-factor. |
| Downstream and exponent scope | Passed.  No claim is made for the full first band, upper conductors, axes, transitions, other radial sectors, GAR, M9-M1, M9-M2, endpoint uniformity, M9, or the quarter exponent. |

No numerical experiment was used; the \(q=8\) test is an exact four-residue calculation.

## 6. Dependencies and exact artifacts used.

The derivation used only the following selected artifacts.

- `protocol.md`: proof-state, one-count, false-shadow, and downstream rules.
- `state/proof_obligations.yml`: the exact open canonical-hard obligation, the proved square-root self-return barrier, the parent M9-M1/GAR scope, and the Rounds 83--90 rejected shadows.
- `state/active_campaign.yml`: Round-99 target, normalization, exit gates, and mandatory controls.
- `rounds/codex-managed/m9-m1-joint-four-row-spectral-gap/derivation_packet.md`: frozen hard target, global flattening, actual-symbol requirements, and hostile controls.
- `rounds/codex-managed/m9-canonical-core-formalization/candidates/conductor_canonical_core_statements.md`: exact physical rows, complete trace, fourfold symbol, owner order, capacity identity, and downstream scope.
- `rounds/codex-managed/m9-m1-capacity-self-return-fork/synthesis.md`: accepted Fejer/Toeplitz and prime-power inverse-transform self-return.
- `rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/synthesis.md`: same-group owner and exact cross-group survivor.
- `rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/synthesis.md`: complete-mask period routing, good-prime deletion, and strict residual.
- `rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/synthesis.md`: cellwise graph theorem, full-degree \(q=8\) control, nonunit/\(2\)-adic survivor, and termination of local period peeling.

No external theorem, source analogy, unselected historical derivation, or computation is used.  The stationary Hessian scale is needed only to audit the tempting \(J^{-1/5}\); the exact separation and self-return identities do not depend on that scale.

## 7. Recommended state effect.

**Promote after seam review** a scoped reduction/no-go node with the following content: on the literal canonical hard Gram, the \((d,u)\) stationary Hessian is integrally equivalent to two separable one-row Hessians; exact double completion reconstructs the centered four-row Gram with no extra \(M\)-factor; ordinary high traces are direct sums in conductor and retain paired, CRT, repeated-prime, and \(q=8\) coherent cycles.  Therefore neither the determinant \(\asymp J^{-2/5}\), a second completion, nor a coefficient-uniform operator norm supplies the missing \(J^{-1/6}\).

Add the rejected claims “Round99-two-dimensional-Hessian-gives-an-extra-\(J^{-1/5}\)” and “Round99-global-high-trace-automatically-uses-conductor-row-cancellation.”  Retain `M9-M1-canonical-hard-actual-symbol-Gram-estimate`, M9-M1, GAR, M9-M2, endpoint uniformity, M9, and the target exponent open.

The next lawful spectral attempt, if pursued, must formulate and prove the fixed-vector estimate (4.1), including the exact post-owner arithmetic mask and an actual-symbol projection or scalar conductor-dispersion input.  It must not resume local period peeling, remove paired trace cycles without a new owner, or multiply the existing row gain by the separable Hessian gain.
