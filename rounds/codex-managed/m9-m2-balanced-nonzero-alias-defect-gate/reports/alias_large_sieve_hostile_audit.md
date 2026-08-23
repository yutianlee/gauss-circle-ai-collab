## 1. Result: one-alias reciprocal spacing self-returns and the local energy is overstrong

**Scoped no-go lemma.** Fix one persistent \(j=1\) literal balanced block
with \(R=\sqrt X\asymp L^3\), \(h,k,h',k'\asymp L\), both low-gcd
weights, both slanted symbols, and both strict far gates retained. An
argument which expands the gcd mask into divisor progressions, applies one
B-process to \(h'=h+2s\), and then uses only reciprocal-\(q\) resonance
counting, aliaswise triangle inequality, a coefficient-blind large sieve,
or a second B-process cannot certify the missing factor \(L\).

The \(d=1\) bulk algebra in the conductor candidate is correct, but it is
not the literal transform. After the gcd expansion, the odd-\(d\)
progression has

\[
 \lambda=\frac{\mu}{d},\qquad
 \mu=\frac12-m\in\mathbb Z+\frac12,
\]

\(\asymp dL^3\) aliases and stationary amplitude
\(\asymp(dL)^{-1}\). If
\(h+2s_d=d\ell_d\), \(s=s_d+dt\), and \(k'=dv\), the exact dual phase is

\[
 R\sqrt{hk}+\frac{s_d}{2}
 -\frac{Xd^2v}{2\mu}-\frac{\ell_d\mu}{2}.
\tag{116.H1}
\]

A second B-process in \(\mu\), with dual integer \(r\), has stationary
point and phase

\[
 \mu=dR\sqrt{\frac{v}{\ell_d+2r}},\qquad
 -dR\sqrt{v(\ell_d+2r)}
 =-R\sqrt{(dv)d(\ell_d+2r)}.
\tag{116.H2}
\]

This is exactly the original progression phase. Its stationary amplitude
\(dL\) cancels the first amplitude \((dL)^{-1}\). The transforms are an
involution, not an inequality gain.

For \(d=1\), an optimal divisor-type near-hyperbola count gives
\(O_\varepsilon(L^2X^\varepsilon)\) per \((h,k)\), exactly the original
\(s,q\) capacity. The \(L^2\) outer rows therefore return
\(L^4X^\varepsilon\), not \(L^3X^\varepsilon\). Literal divisorwise
triangle inequality is worse, so the divisor family must remain signed.

The large-sieve spacing also fails. At \(d=1\) there are
\(N\asymp L^3\) frequencies but only \(Q\asymp L\) samples. At resolution
\(Q^{-1}\), some cluster contains \(\gg N/Q\asymp L^2\) aliases and there
are \(\gg N^2/Q\asymp L^5\) ordered near-collision pairs. Every
coefficient-uniform large-sieve constant is therefore \(\gg L^3\), the
full dual length.

Finally, the proposed row local energy is valid as a sufficient condition
but is stronger than the scalar target. With

\[
 S_B=\sum_{h',k'}\overline{a_B^<(h',k')}e(-R\sqrt{h'k'}),
\]

one has \(T_{h,k}=S_B-C_{h,k}\), where \(C_{h,k}\) contains only the two
width-\(L\) corridors and
\(|C_{h,k}|\ll_\varepsilon LX^\varepsilon\). Consequently

\[
 \sum_{h,k}|T_{h,k}|^2\ll_\varepsilon L^4X^\varepsilon
 \quad\Longrightarrow\quad
 |S_B|\ll_\varepsilon LX^\varepsilon.
\tag{116.H3}
\]

This is stronger than the required \(L^{3/2}X^\varepsilon\) linear
bound. The norm is a nearly repeated full-sum Gram, not an equivalent
reformulation. These are route no-go results, not lower bounds for the
actual signed block.

## 2. Exact statement and hypotheses

Let \(X\ge4096\) be real, \(R=\sqrt X\asymp L^3\), \(L\ge16\), and
\(1\le K/L\le16\). Fix one physical block \(B\), and put

\[
 a(h,k)=\chi_4(h)
 \eta\!\left(\frac{(h,k)}{\sqrt L/2}\right)A_B(h,k).
\]

All floors, tapers, stars, support crossings, and both literal symbols
remain. Write

\[
 \Delta=h'k'-hk,\qquad \rho=hk'-h'k,
\]

and let \({\rm df}\) mean \(|\Delta|>L\), \(|\rho|>L\). The audited object
is

\[
 \mathcal R_B^{\rm osc}
 =\sum_{\rm df}a(h,k)\overline{a(h',k')}
 \left\{e\!\left(R(\sqrt{hk}-\sqrt{h'k'})\right)-1\right\}.
\tag{116.H4}
\]

The accepted phase-free owner is used exactly once. For the oscillatory
term set \(h'=h+2s\), \(k'=k+q\), and expand the second gcd mask:

\[
 \eta\!\left(\frac{(h',k')}{G_0}\right)
 =\sum_{d\mid h',\,d\mid k'}\gamma_d,\qquad
 \gamma_d=\sum_{e\mid d}\mu(e)
 \eta\!\left(\frac{d/e}{G_0}\right),\qquad
 G_0=\frac{\sqrt L}{2}.
\tag{116.H5}
\]

Only odd \(d\) contribute. Choose \(s_d\pmod d\) with
\(h+2s_d=d\ell_d\), and write \(s=s_d+dt\). At fixed \(d\), write
\(k'=k+q=dv\), so the \(v\)-length is \(Q_d\asymp L/d\).

The no-go covers modewise absolute values, geometric \(v\)-sum bounds,
near-integral counting for \(Xd^2/(2\mu)\), spacing-only large sieves, and
a second B-process. It does not cover a new theorem retaining
\(d,h,k,v,\mu\), the residue phase, both gate images, and the actual
amplitude jointly signed.

## 3. Proof or derivation

### 3.1 Literal alias algebra and gate images

Since \(d\) is odd,

\[
 e((s_d+dt)/2)=e(s_d/2)e(t/2).
\]

Poisson in \(t\) at frequency \(m\) has phase

\[
 R\sqrt{hk}-R\sqrt{d(\ell_d+2t)k'}
 +\frac{s_d}{2}+\left(\frac12-m\right)t.
\]

Put \(\mu=1/2-m>0\), \(\lambda=\mu/d\), and
\(x=d(\ell_d+2t)\). The stationary equation is

\[
 \lambda=R\sqrt{\frac{k'}x},\qquad x=\frac{Xk'}{\lambda^2}.
\tag{116.H6}
\]

The change from \(t\) to \(s\) supplies \(1/d\), while

\[
 \frac{\partial^2}{\partial s^2}
 \{-R\sqrt{(h+2s)k'}\}
 =R\sqrt{k'}\,x^{-3/2}\asymp L^2.
\]

Hence one term has amplitude \(O((dL)^{-1})\), and the derivative range
contains \(\asymp dL^3\) aliases. Its stationary phase is

\[
 \Psi_d
 =R\sqrt{hk}-\frac{X(k+q)}{2\lambda}
 -\frac{\lambda h}{2}+s_d(1/2-\lambda)
\tag{116.H7}
\]

or, with \(\lambda_0=R\sqrt{k/h}\),

\[
 \Psi_d
 =-\frac{h(\lambda-\lambda_0)^2}{2\lambda}
 -\frac{Xq}{2\lambda}+s_d(1/2-\lambda).
\tag{116.H8}
\]

Thus the square completion is correct, but the literal residue term and
rational lattice were omitted. Substitution gives (116.H1).

The gate images are exactly

\[
 \rho=\frac{hk'}{\lambda^2}(\lambda^2-\lambda_0^2),\qquad
 \Delta=\frac{hk}{\lambda^2}(\lambda_r^2-\lambda^2),\qquad
 \lambda_r=\frac{Rk'}{\sqrt{hk}}.
\tag{116.H9}
\]

Their derivatives at the centres are \(\asymp L^{-1}\). Each width-\(L\)
corridor deletes \(O(dL^2)\) of \(dL^3\) aliases. Also

\[
 \lambda_r-\lambda_0=\frac{\lambda_0q}{k}\asymp qL^2.
\tag{116.H10}
\]

The neighbourhoods overlap only for \(q=O_B(1)\); that bounded-\(q\)
sector is already \(O(L^3)\) by primal absolute counting. The remaining
\(\asymp L\) shifts are not shortened.

### 3.2 Near-hyperbola resonance and self-return

For \(d=1\), put \(n=2\lambda\), so \(n\) is odd and \(n\asymp L^3\).
For \(L^{-1}\le\theta\le1/2\),

\[
 \#\left\{n:\left\|\frac Xn\right\|\le\theta\right\}
 \ll_\varepsilon(\theta L^3+1)X^\varepsilon.
\tag{116.H11}
\]

Indeed, \(|X-jn|\ll\theta L^3\) for some integer \(j\); the interval has
\(O(\theta L^3+1)\) integer products \(jn\), each with
\(O_\varepsilon(X^\varepsilon)\) divisors. At \(\theta=L^{-1}\), this is
the exact candidate resonance

\[
 |X-2j\lambda|\ll L^2
\]

and contains \(O_\varepsilon(L^2X^\varepsilon)\) aliases.

On the shell
\(\|X/(2\lambda)\|\asymp2^r/L\), there are
\(O_\varepsilon(2^rL^2X^\varepsilon)\) aliases, the \(q\)-sum is
\(O(L/2^r)\), and the stationary amplitude is \(L^{-1}\). Thus every
shell costs

\[
 (2^rL^2)L^{-1}\frac{L}{2^r}\ll L^2
\tag{116.H12}
\]

per \((h,k)\). This merely returns the primal \(s,q\) row capacity.

For literal \(d\), the progression frequency and resolution are

\[
 \beta_{d,\mu}=\frac{Xd^2}{2\mu},\qquad Q_d\asymp\frac Ld,
\tag{116.H13}
\]

and resonance is

\[
 \left\|\frac{Xd^2}{2\mu}\right\|\ll\frac dL
 \iff |Xd^2-2j\mu|\ll d^2L^2.
\tag{116.H14}
\]

There are \(O_\varepsilon(d^2L^2X^\varepsilon)\) such aliases, and the
same dyadic calculation, using amplitude \((dL)^{-1}\) and progression
sum \(O(L/(2^rd))\), costs \(O(L^2X^\varepsilon)\) for every fixed \(d\).
After reorganizing by \(d\), a divisorwise triangle can sum over
\(\asymp L\) progressions; it is not the divisor count for one fixed
\(q\). Signed divisor-alias cancellation remains mandatory.

### 3.3 Exact Cauchy/large-sieve diagonal and spacing

On a separated smooth cell, the fixed-\((h,k,d)\) quadratic form is

\[
 \sum_{v\in V_d}\left|\sum_{\mu\in\mathcal M_d}
 c_\mu e(-v\beta_{d,\mu})\right|^2
 =Q_d\sum_\mu|c_\mu|^2
 +\sum_{\mu\ne\mu'}c_\mu\overline{c_{\mu'}}
 D_{Q_d}(\beta_{d,\mu}-\beta_{d,\mu'}).
\tag{116.H15}
\]

Here

\[
 |\mathcal M_d|=N_d\asymp dL^3,\quad
 Q_d\asymp L/d,\quad |c_\mu|\asymp(dL)^{-1}.
\]

The diagonal is exactly of natural size

\[
 Q_d\sum_\mu|c_\mu|^2\asymp\frac{L^2}{d^2}.
\tag{116.H16}
\]

Summing the divisor incidence and \(L^2\) outer rows gives global diagonal

\[
 \mathfrak D_{\rm LS}\asymp L^4X^{O(\varepsilon)}
\tag{116.H17}
\]

on a nondegenerate core. Cauchy over the \(L^3\) outer
\((h,k,q)\)-choices gives, even with ideal diagonal control,

\[
 |\mathcal A_B|
 \ll(L^3\mathfrak D_{\rm LS})^{1/2}
 \asymp L^{7/2}X^{O(\varepsilon)}.
\tag{116.H18}
\]

Thus this Cauchy orientation already needs an actual subdiagonal
\(O(L^3)\) theorem.

Spacing is worse. Partition the circle into \(O(Q_d)\) arcs of length
\(Q_d^{-1}\). Pigeonhole gives

\[
 M_d\gg\frac{N_d}{Q_d}\asymp d^2L^2,\qquad
 \sum_I|\mathcal M_d\cap I|^2
 \ge\frac{N_d^2}{Q_d}\asymp d^3L^5.
\tag{116.H19}
\]

Coefficients supported on the largest cluster show that a
coefficient-uniform large-sieve constant is at least

\[
 Q_dM_d\gg dL^3\asymp N_d.
\tag{116.H20}
\]

The near-hyperbola count measures distance from \(0\pmod1\); the large
sieve measures every pairwise difference. The former does not control the
latter.

The smallest honest survivor is the **joint divisor-reciprocal cluster
defect norm**: group frequencies at scale \(Q_d^{-1}\), but retain
\(d,h,k,v,\mu\), (116.H8), both gates, and the actual amplitude signed
inside each cluster. No \(L^3\)-budget estimate for this norm is supplied.

Finally, applying a second B-process to (116.H1) gives

\[
 \frac{Xd^2v}{2\mu^2}-\frac{\ell_d}{2}-r=0,
\]

and hence (116.H2). Its amplitude is \(dL\), its dual range is
\(\asymp L/d\), and the original progression returns with unit net
amplitude. This is exact self-return.

### 3.4 Local-energy and boundary/owner costs

Let \(\mathcal X_B\) be a positive-area block core,
\(|\mathcal X_B|\asymp L^2\), and put
\(b_y=\overline{a(y)}e(-R\sqrt{h_yk_y})\), \(S_B=\sum_yb_y\).
For \(x=(h,k)\), let \(C_x\) contain the two corridor sums. The radial
corridor has

\[
 O\!\left(\sum_{|n-hk|\le L}\tau(n)\right)
 \ll_\varepsilon LX^\varepsilon
\]

pairs; the determinant corridor has \(O(L)\) pairs. Therefore

\[
 |C_x|\ll_\varepsilon LX^\varepsilon,\qquad
 \sum_{x\in\mathcal X_B}|C_x|^2
 \ll_\varepsilon L^4X^\varepsilon.
\tag{116.H21}
\]

Since \(T_x=S_B-C_x\), the proposed local-energy bound implies (116.H3).
Its Gram kernel is

\[
 K_B(y,z)=\#\{x:{\rm df}(x,y),{\rm df}(x,z)\}
 =|\mathcal X_B|+O_\varepsilon(LX^\varepsilon)
\]

for generic \(y,z\). The rows overlap almost completely, so the
off-diagonal replicates \(L^2|S_B|^2\). A phase-adapted bounded array with
\(b_y=1\) makes the norm \(\asymp L^6\). Thus the norm is not circular as
an implication, but it is a distinct stronger Gram and is false
coefficient-uniformly.

For fixed \((h,k,q)\), both far-gate complements contain \(O_B(1)\)
\(s\)-points because their slopes are \(\asymp L\). Restoring them costs
\(O_\varepsilon(L^3X^\varepsilon)\) once. After (116.H5), each progression
has \(O_B(1)\) support/gate pieces. A uniform aggregate B-process would
have \(O(\log X)\) endpoint and nonstationary-tail cost per piece, hence
total scalar allowance \(O_\varepsilon(L^3X^\varepsilon)\); the candidate
did not supply this lemma. A per-alias remainder multiplied by \(dL^3\)
would be unlawful.

The phase-free mode is used only once in
\(E_{B,{\rm df}}=M_B^{(0)}+\mathcal R_B^{\rm osc}\). It is not a Poisson
zero mode. No cross-block, hard TOP, UNBAL, M1, endpoint, or generic
\(j=2\) owner is imported.

## 4. First doubtful or unproved step

The first literal failure is treating the gcd mask as a smooth
\(s\)-amplitude while keeping \(\lambda=1/2-m\). The exact expansion
forces

\[
 \lambda=\frac{1/2-m}{d},
\]

amplitude \((dL)^{-1}\), \(dL^3\) aliases, residue phase
\(s_d(1/2-\lambda)\), and \(k+q\equiv0\pmod d\). Thus
(116.C1)--(116.C5) are only the \(d=1\) bulk model.

Even granting target-safe aggregate boundary control, the first analytic
gap is a factor-\(L\) cancellation in the jointly signed cluster-defect
norm. Near-hyperbola counting self-returns, a second B-process returns the
primal progression, and spacing-only large sieve sees \(L^2\)-sized
clusters. The local energy replaces this gap by the stronger
\(|S_B|\ll L\) problem.

## 5. Required control tests and outcomes

| Audit axis | Outcome | Exact reason |
|---|---:|---|
| Literal legality | **FAIL for candidate** | Gcd expansion changes the lattice, amplitude, residue phase, and \(q\)-progressions; aggregate boundary terms were not proved. |
| Alias geometry | **PASS after repair** | (116.H6)--(116.H10) give the exact phase and gate images. |
| Resonance count | **PASS as count / FAIL as saving** | The count is \(L^2\) at \(d=1\) and \(d^2L^2\) literally; dyadic summation self-returns. |
| Norm cost | **FAIL** | Global LS diagonal is \(L^4\), Cauchy gives \(L^{7/2}\), and forced clusters defeat a coefficient-uniform LS. |
| Source fit | **FAIL for transfer** | No exact primary-source theorem is supplied; previously audited Cowan/Chamizo hypotheses remain mismatched. |
| Owners | **PASS** | Corridors/boundaries cost at most \(L^3X^\varepsilon\) once; the phase-free owner is used once; one \(j=1\) block is fixed. |
| Downstream scope | **PASS** | This is a route no-go, not an actual-sum lower bound or a BAL/M9 claim. |

| Required control | Outcome |
|---|---|
| literal_half_shift_poisson_legality | **Fail for candidate; repaired chart derived.** |
| gcd_expansion_and_character_progressions | **Pass in audit.** |
| stationary_alias_range_and_amplitude | **Pass after revision:** \(dL^3\), \((dL)^{-1}\). |
| dual_phase_square_completion | **Pass after adding the residue phase.** |
| radial_and_determinant_gate_images | **Pass.** |
| reciprocal_q_frequency_resonance_count | **Pass as a self-return obstruction.** |
| signed_alias_norm_without_l1 | **Fail: cluster-defect norm remains open.** |
| large_sieve_spacing_and_diagonal_cost | **Pass as a no-go.** |
| boundary_and_nonstationary_errors | **Fail for candidate; target-safe only after an aggregate lemma.** |
| actual_symbol_vs_arbitrary_coefficients | **Pass as a distinction; no actual lower bound is claimed.** |
| fixed_block_and_owner_scope | **Pass.** |
| critical_j1_and_exact_square_j2_boundary | **Pass; \(j=2\) is untouched.** |
| external_theorem_hypothesis_fit | **Pass by rejection/non-use.** |
| linear_vs_energy_capacity | **Pass in audit; local-energy proposal is overstrong.** |
| downstream_scope | **Pass.** |

## 6. Dependencies and exact artifacts used

Authoritative proof-state hash:
6421d27cb531be922b11ec48b51002ba568f235d510d16ac28a7d84881d66dad.

The audit used, completely and only within their stated scope:

1. protocol.md;
2. state/proof_obligations.yml;
3. state/active_campaign.yml;
4. strategy/conductor_0821_full_proof_strategy.md;
5. rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/reports/literal_dispersion_attack.md;
6. rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/reports/actual_symbol_main_term_hostile.md;
7. rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/synthesis.md;
8. rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/derivation_packet.md;
9. rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/candidates/conductor_half_shift_alias_defect.md;
10. rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/briefs/alias_large_sieve_hostile_audit.md.

No numerical experiment and no external theorem were used. The finite
large-sieve identity, cluster lower bound, divisor-window count, and both
Legendre calculations were derived directly.

## 7. Recommended state effect

**Reject the conductor candidate as a completed proof mechanism; retain
the actual target open; promote only the scoped obstruction after conductor
seam review.**

1. Revise (116.C1)--(116.C3) as the smooth \(d=1\) bulk chart. The literal
   chart is (116.H6)--(116.H10), with rational aliases, residue phase,
   amplitude \((dL)^{-1}\), and \(dL^3\) modes.
2. Record the reciprocal one-alias self-return obstruction: optimal
   near-hyperbola counting only repairs the first B-process loss, and a
   second B-process exactly returns the original progression.
3. Record the reciprocal-cluster obstruction: \(L^3\) frequencies sampled
   \(L\) times force \(L^2\)-sized clusters and \(L^5\) near pairs.
4. Do not treat (116.D10)/(116.C6) as equivalent to the scalar target. It
   is a distinct stronger actual-symbol Gram implying \(|S_B|\ll L\).
5. Continue this route only with an exact \(O(L^3X^\varepsilon)\) theorem
   for the joint divisor-reciprocal cluster defect norm, retaining all
   congruences, gates, amplitudes, and boundary pieces before norms.
6. Make no status change to
   M9-M2-balanced-double-far-oscillatory-remainder,
   M9-M2-balanced-double-far-actual-energy, or
   M9-M2-smooth-balanced-quarter-packet-estimate, and no change to any
   TOP, UNBAL, M1, endpoint, M9, or exponent node.

This is a rigorous no-go for the named one-alias/reciprocal-spacing class,
not a lower bound for the actual signed sum and not a claim that BAL is
false.
