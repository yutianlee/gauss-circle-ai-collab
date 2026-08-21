## 1. Result: lemma or no-go result.

**Blind joint-operator lemma and atom-separation no-go.**  The displayed hard
energy has an exact realization as one matrix coefficient of a direct sum of
joint conductor blocks.  Inside each block all classes, signs, aliases,
reflections, and hard configurations are summed before an absolute value is
taken.  If \(\mathsf C_U\) denotes the resulting coefficient-blind Schur
capacity, the weakest sufficient estimate is the single, actual-symbol
directional inequality

\[
 \left|\widehat p_U^*\widehat{\mathcal K}_U\widehat q_U\right|
 \leq { (U/B)J^{14/5}\over \mathsf C_U}.
\]

At the top range, where the packet declares
\(\mathsf C_U\) to be larger than the target by \(J^{1/6}\), this is precisely
a \(J^{-1/6}\) Gram-level matrix-coefficient gain (up to the conventional
\(X^\varepsilon\) split).  The stronger coefficient-uniform condition
\(\|\widehat{\mathcal K}_U\|_{2\to2}\ll J^{-1/6}\) would also suffice.

There is, however, a rigorous equal-capacity obstruction to obtaining that
stronger condition by separating the configurations, bounding their trace
moments separately, or taking coefficientwise absolute values.  Every fixed
configuration contributes a separable character atom \(c\,a b^*\).  On a
rectangular or biregular full-degree cell its unique nonzero singular value is
exactly its Schur capacity, and its \(2r\)-th trace contribution remains the
\(2r\)-th power of that capacity for every \(r\).  The actual local
\(q=8\) fourfold phase supplies a nonoscillatory full-degree instance.  Thus
high trace can help only through cross-configuration terms in the *joint*
Gram expansion, or through small projections of the fixed \(I_b\)-vectors
onto coherent modes.  The statement-only packet does not contain enough
information to prove either property.  Consequently this report proves the
atom-separation/post-absolute-value no-go, not the boxed hard-energy target.

## 2. Exact statement and hypotheses.

Let \(\alpha=(b,u,d)\), with \(b\asymp B\), \(0<|u|<U\), and \(d\) in the
literal deep range.  Let \(\Sigma_\alpha\) be the configurations
\(\sigma\in\mathscr H_{b,U}\) compatible with \(\alpha\).  A configuration
fixes its literal class \((\kappa,M_\sigma,K_\sigma)\), shifts
\((A_\sigma,B_{2,\sigma},V_\sigma)\), sign, alias, reflection, support, and
entry/exit data.  Put

\[
 c_{\alpha\sigma}=
 \epsilon_\sigma M_\sigma^{-5}e_{M_\sigma}(dV_\sigma)
 \mathfrak T_{M_\sigma}
 (u,A_\sigma,B_{2,\sigma},V_\sigma),
\]

where \(\epsilon_\sigma\) is the literal enumerative sign (or \(1\) when that
sign is already encoded in the displayed summand).  If
\(D_{\alpha\sigma}\) is the exact deep incidence set in \((n,m)\), define

\[
 K_\alpha(n,m)=
 \sum_{\sigma\in\Sigma_\alpha}
 \mathbf1_{D_{\alpha\sigma}}(n,m)c_{\alpha\sigma}
 e_{M_\sigma}(nA_\sigma-mB_{2,\sigma}).                 \tag{2.1}
\]

Thus the sum over \(\sigma\), including all three local classes, is inside
the matrix entry.  Define

\[
 p_\alpha(n)=\sqrt{U-|u|}\,
 \overline{I_b(n+d+u)}I_b(n),\qquad
 q_\alpha(m)=\sqrt{U-|u|}\,
 \overline{I_b(m+d)}I_b(m).                            \tag{2.2}
\]

Let \(\mathcal K_U=\bigoplus_\alpha K_\alpha\),
\(p_U=\bigoplus_\alpha p_\alpha\), and
\(q_U=\bigoplus_\alpha q_\alpha\), using zero extension at every literal
support boundary.  For a concrete Schur normalization set

\[
 R_U=\sup_{\alpha,n}\sum_m|K_\alpha(n,m)|,\quad
 C_U=\sup_{\alpha,m}\sum_n|K_\alpha(n,m)|,\quad
 S_U=(R_UC_U)^{1/2},                                   \tag{2.3}
\]

\[
 \widehat{\mathcal K}_U=S_U^{-1}\mathcal K_U,\qquad
 \widehat p_U=p_U/\|p_U\|_2,\qquad
 \widehat q_U=q_U/\|q_U\|_2,\qquad
 \mathsf C_U=S_U\|p_U\|_2\|q_U\|_2.                 \tag{2.4}
\]

The zero-capacity case is trivial.  Weighted or optimized Schur tests give
the same statements after diagonal rescaling.  The only capacity hypothesis
used below is the one declared in the packet: at the worst endpoint its
known coefficient-blind size is the desired size times \(J^{1/6}\), modulo
\(X^\varepsilon\).

For a product deep support
\(D_{\alpha\sigma}=N_{\alpha\sigma}\times
M_{\alpha\sigma}\), set

\[
 a_{\alpha\sigma}(n)=\mathbf1_{N_{\alpha\sigma}}(n)
 e_{M_\sigma}(nA_\sigma),\qquad
 b_{\alpha\sigma}(m)=\mathbf1_{M_{\alpha\sigma}}(m)
 e_{M_\sigma}(mB_{2,\sigma}).                         \tag{2.5}
\]

Then
\(K_\alpha=\sum_{\sigma}c_{\alpha\sigma}
a_{\alpha\sigma}b_{\alpha\sigma}^*\).  For a nonproduct incidence set,
(2.1) is authoritative; the no-go applies to each rectangular component and,
in particular, to any constant-modulus biregular component.  No assertion
that such a component survives the four owners globally is added as a
hypothesis.

## 3. Proof or derivation.

Taking the ordinary complex matrix product and substituting (2.1)--(2.2)
gives

\[
\begin{aligned}
 p_U^*\mathcal K_Uq_U
 &=\sum_{b,\sigma,u,d,n,m}^{\rm hard,deep}(U-|u|)
 I_b(n+d+u)\overline{I_b(n)}
 \overline{I_b(m+d)}I_b(m)\\
 &\quad\times M_\sigma^{-5}e_{M_\sigma}
 (dV_\sigma+nA_\sigma-mB_{2,\sigma})
 \mathfrak T_{M_\sigma}
 (u,A_\sigma,B_{2,\sigma},V_\sigma)\\
 &=\mathcal E_{\rm hard}(U).                          \tag{3.1}
\end{aligned}
\]

This proves the exact block-operator identity.  The restriction
\(\sigma\in\mathscr H_{b,U}\) applies the four disjoint owners once, and
\(0<|u|<U\) removes only the globally owned integer \(u=0\) coefficient.
No class or sign has been split off before (2.1).

Schur's test and (2.3) give
\(\|\widehat{\mathcal K}_U\|_{2\to2}\leq1\), while

\[
 |\mathcal E_{\rm hard}(U)|=
 \mathsf C_U
 \left|\widehat p_U^*\widehat{\mathcal K}_U
 \widehat q_U\right|.                                \tag{3.2}
\]

Hence the exact target-specific threshold is

\[
 \Delta_U={ (U/B)J^{14/5}\over\mathsf C_U}.           \tag{3.3}
\]

The inequality
\(|\widehat p_U^*\widehat{\mathcal K}_U\widehat q_U|
\ll_\varepsilon X^\varepsilon\Delta_U\) is both necessary and sufficient
for this one actual matrix coefficient, so it is weaker than every
coefficient-uniform spectral statement.  At the declared top-capacity gap,
\(\Delta_U=J^{-1/6}\) at the level of powers.  For any integer \(r\geq1\),
the sufficient high-trace condition is

\[
 \operatorname{Tr}\!\left[
 (\widehat{\mathcal K}_U^*\widehat{\mathcal K}_U)^r
 \right]\ll_\varepsilon X^\varepsilon\Delta_U^{2r}; \tag{3.4}
\]

at the top this asks for \(J^{-r/3}\).  Indeed the largest singular value
to the power \(2r\) is at most the trace in (3.4).

The exact joint moment that a positive proof would have to estimate can be
written without discarding the actual symbol.  On product supports, for
\(s_{r+1}=s_1\),

\[
\begin{aligned}
 \operatorname{Tr}[(K_\alpha^*K_\alpha)^r]
 =\sum_{s_1,t_1,\ldots,s_r,t_r\in\Sigma_\alpha}
 \prod_{j=1}^r
 &\overline{c_{\alpha s_j}}c_{\alpha t_j}
 \langle a_{\alpha s_j},a_{\alpha t_j}\rangle\\
 &\times\langle b_{\alpha t_j},b_{\alpha s_{j+1}}\rangle .       \tag{3.5}
\end{aligned}
\]

Formula (3.5), summed over \(\alpha\) and divided by \(S_U^{2r}\), is the
global trace moment.  It shows exactly where conductor-difference
oscillation would have to enter: in the two character Gram factors together
with the literal coefficients \(c_{\alpha\sigma}\).  Estimating the
\(s_j,t_j\) terms separately by absolute values destroys that possibility.

For the no-go, one atom \(A=cab^*\), with \(a,b\) unit-modulus character
vectors on sets of cardinalities \(N,L\), has

\[
 \|A\|_{2\to2}=|c|\sqrt{NL}
 =\sqrt{(|c|L)(|c|N)},                                \tag{3.6}
\]

which is exactly its Schur capacity.  Moreover

\[
 \operatorname{Tr}[(A^*A)^r]
 =(|c|\sqrt{NL})^{2r}.                                \tag{3.7}
\]

The same conclusion holds for a constant-modulus biregular cell after
removing its separable row and column phases: the constant vectors give the
singular value \(|c|\sqrt{d_Ld_R}\), equal to Schur.  If several atoms have
the same left and right characters and their adjusted scalars have one
phase, their sum is again rank one and (3.6)--(3.7) hold with the scalar sum.
Thus neither a higher moment nor a perfect-square/fourth-power pairing gives
a power saving on a coherent mode.  This proves the claimed
atom-separation and post-absolute-value obstruction.

For the literal \(8\)-part, a nonempty unit cell has
\(A,B_2,V\) even.  Every odd residue is its own inverse modulo \(8\), so

\[
 \Phi_{A,B_2,V}(x)\equiv
 x-(x-A)-(x-V)+(x-V-B_2)\equiv A-B_2\pmod 8.
\]

Consequently

\[
 \mathfrak T_8(u,A,B_2,V)
 =8e_8(K(A-B_2))c_8(u),                               \tag{3.8}
\]

where \(c_8(u)=4\) for \(8\mid u\), \(c_8(u)=-4\) for
\(u\equiv4\pmod8\), and \(c_8(u)=0\) otherwise.  Thus every surviving
band in (3.8) has magnitude \(32\) and only a common phase.  In particular,
nonzero integer multiples of \(8\) survive even though the integer
coefficient \(u=0\) is excluded.  This is an actual-fourfold-symbol,
full-degree local coherent mode, not an unsigned replacement.

## 4. First doubtful or unproved step.

The first unproved step toward the positive target is a power-saving bound
for the *joint* sum (3.5), or the weaker actual-vector projection in (3.2),
after the literal hard-owner complement is imposed.  The statement packet
does not specify the sets \(D_{\alpha\sigma}\), the configurations in
\(\mathscr H_{b,U}\), the normalization and support of \(I_b\), or the
congruence multiplicities needed to evaluate the cross-Gram factors.  It is
therefore impossible from the permitted files to determine whether the
\(q=8\) coherent factor extends to a globally reducing mode, whether other
classes cancel it entrywise, or whether the actual \(I_b\)-vectors have a
small projection onto it.  Claiming any of those facts would silently import
an excluded derivation.

This missing cross-configuration estimate is earlier than any downstream
summation issue.  The no-go in Section 3 is unconditional for a separated or
post-absolute-value proof, and conditional only when it is used to assert an
equal-capacity eigenspace of the full joint operator.  No such assertion is
made here.

## 5. Control tests and outcomes.

- **Canonical normalization and the required gain:** (3.1)--(3.4) give the
  exact identity, Schur-capacity-one normalization, target-specific weakest
  inequality, and the top \(J^{-1/6}\) Gram / \(J^{-r/3}\) trace threshold.
  Outcome: pass.

- **Prior owners, \(u=0\), and Ramanujan ownership:** only
  \(\sigma\in\mathscr H_{b,U}\) and \(0<|u|<U\) enter.  Formula (3.8)
  retains nonzero modulus multiples and the centered Ramanujan value rather
  than misclassifying them as the owned \(u=0\) term.  Outcome: pass.

- **Classes, signs, aliases, reflections, entry/exit, and the actual
  symbol:** all are retained in \(\Sigma_\alpha\) and summed inside (2.1);
  \(\mathfrak T_M\) remains literal in \(c_{\alpha\sigma}\), and the four
  actual \(I_b\) factors remain in (2.2).  Outcome: pass.

- **Global moment expansion:** (3.5) keeps all cross-configuration cycles.
  It also shows that separate complete-trace bounds are insufficient.
  Outcome: pass as an exact reduction; the needed estimate is open.

- **Full-degree \(q=8\) and the full \(2\)-part:** (3.8) proves analytically
  that the local fourfold phase is constant and has magnitude \(32\) on the
  surviving bands.  A full-degree biregular cell therefore has normalized
  singular value one.  Outcome: the local-sparsity or atomwise spectral-gap
  mechanism fails.

- **Repeated primes, prime powers, and CRT:** in (3.5), equal prime-power
  characters give full-size Gram factors.  Two occurrences of the same
  \(p^a\) have common denominator \(p^{\max(a_1,a_2)}\), not independent
  coprime conductors; CRT only factors genuinely coprime parts.  The diagonal
  cycle \(s_j=t_j=s_{j+1}\) is therefore a self-return of full size.
  Outcome: no repeated-prime saving follows from high trace alone.

- **Nonunit \(K\) and modulus multiples:** no coprimality of \(K\) was used.
  In (3.8), \(K\) merely rotates the common phase; for \(8\mid u\), a
  nonzero modulus multiple has maximal local Ramanujan value.  If a
  prime-power factor divides \(K\), the phase can become still more
  degenerate, never less.  Outcome: these cases cannot be dropped and do not
  provide a uniform gap.

- **Perfect-square/fourth-power resonance and transform self-return:** the
  diagonal terms of (3.5) are the positive quantities in (3.7); at
  \(r=1,2\) they are exact square and fourth-power returns.  Increasing the
  trace moment or re-expressing the same character transform does not shrink
  a coherent singular value.  Outcome: the self-return control fails for an
  atomwise proof.

- **Arbitrary-coefficient false shadow:** choose the left and right singular
  vectors of a coherent atom or biregular cell.  The normalized matrix
  coefficient is one, contradicting any \(J^{-1/6}\) coefficient-uniform
  claim.  The fixed vectors (2.2) might avoid this mode, which is exactly why
  the directional inequality is the weakest sufficient statement.  Outcome:
  arbitrary-coefficient strengthening is false for the separated shadow.

- **Post-absolute-value shadow:** \(|cab^*|=|c|\mathbf1\mathbf1^*\) on a
  rectangle, and a constant-modulus biregular adjacency has its Schur
  singular vector after absolute values.  Outcome: coefficientwise absolute
  values close at equal capacity and cannot yield the missing power.

- **Downstream scope:** no blockwise M1 conclusion, GAR estimate, M2 claim,
  endpoint statement, M9 conclusion, or circle-problem exponent is inferred.
  Outcome: pass.

All controls above are exact algebraic controls; no numerical experiment was
used.

## 6. Dependencies and artifacts used.

The mathematical dependencies were only the statement-only artifacts
`problems/gauss_circle.md`, `state/control_models.md`, and
`rounds/codex-managed/m9-m1-joint-four-row-spectral-gap/blind_statement.md`.
The task contract came from
`rounds/codex-managed/m9-m1-joint-four-row-spectral-gap/briefs/blind_joint_gram_rederivation.md`.
`protocol.md` and the `blind_joint_gram_rederivation` entry of
`state/active_campaign.yml` were read only for workflow, scope, and the
declared capacity gap.  No proof graph, best proof draft, Round-87--90
derivation, claimant report, reviewer report, sibling report, web source, or
external theorem was used.

## 7. Recommended state effect.

**Retain** the exact joint block representation (2.1)--(3.1), the weakest
directional threshold (3.2)--(3.3), the literal global moment expansion
(3.5), and the analytic \(q=8\) identity (3.8).  **Reject** as a route to the
missing gain every argument that first separates configurations, estimates
complete traces one at a time, takes coefficientwise absolute values, or
relies on higher trace to defeat the resulting coherent self-return.

Make **no promotion** of the hard-energy target.  A future positive attempt
must prove cancellation among the cross-configuration terms of (3.5) with
the exact hard set, or prove that the fixed \(I_b\)-vectors have
\(J^{-1/6}\)-small projection onto every capacity-size coherent mode.  A
future negative attempt must verify, from non-blind data, that a coherent
family survives all four owners and is reducing for the full joint operator;
the present packet does not certify that last seam.
