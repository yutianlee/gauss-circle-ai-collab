# Literal alias/local-energy attack: divisor-progressive chart and involution barrier

## 1. Result: lemma or no-go result

**Result.**  The clean conductor chart is literal only in the unexpanded
`d=1` gcd sector.  After the mandatory expansion of the second gcd mask,
an odd divisor (d\mid k') forces the (s)-variable onto one progression
and changes the dual lattice to

\[
 \lambda={\mu\over d},\qquad \mu\in\mathbb Z+\tfrac12,
 \qquad \#\{\mu\}\asymp dL^3,
\]

with stationary amplitude (\asymp(dL)^{-1}).  It also contributes a
non-removable residue phase.  If (s_d\pmod d) is determined by
(h+2s_d\equiv0\pmod d), and

\[
 \ell_d={h+2s_d\over d},\qquad k'=dv,
\]

then the exact stationary phase is

\[
 R\sqrt{hk}+{s_d\over2}
 -{Xd^2v\over2\mu}-{\ell_d\mu\over2}.                 \tag{116.L1}
\]

Equivalently, with (q=k'-k),

\[
 -{h(\lambda-\lambda_0)^2\over2\lambda}
 -{Xq\over2\lambda}+s_d(\tfrac12-\lambda),
 \qquad \lambda_0=R\sqrt{k/h}.                        \tag{116.L2}
\]

Thus the literal reciprocal (v)-frequency is

\[
 \alpha_{d,\mu}={Xd^2\over2\mu},                      \tag{116.L3}
\]

not (X/(2\lambda)) on an unrestricted (q)-interval.  The latter is
the same phase before noticing that (q\equiv-k\pmod d).

Finite Poisson summation on each literal support/gate component gives a
fully signed stationary kernel (\mathcal K_B) below.  All nonstationary,
Poisson-endpoint, and natural stationary-transition terms have total cost
(O_\varepsilon(L^3X^\varepsilon)).  Consequently

\[
 |\mathcal R_B^{\rm osc}|
 \le |\mathcal K_B|+O_\varepsilon(L^3X^\varepsilon),   \tag{116.L4}
\]

and the reverse inequality holds with the same allowance.  This is a
literal reduction, not the desired estimate.

There is a rigorous scoped no-go.  A method which treats one alias at a
time, estimates the (v)-progression only through (116.L3), and then takes
absolute values over aliases and outer pairs has capacity (L^4X^\varepsilon),
even after the optimal elementary near-hyperbola count.  A coefficient-
uniform reciprocal-frequency large sieve has a diagonal constant at least
(dL^3), the number of aliases.  Applying a second B-process in (\mu)
is exactly invertible: its Legendre phase is

\[
 -dR\sqrt{v(\ell_d+2n)},                               \tag{116.L5}
\]

its amplitude is the reciprocal of the first stationary amplitude, and
the half-lattice factor ((-1)^n) restores the primal character.  Hence
this operation returns the original (h'=d(\ell_d+2n)), (k'=dv)
progression and supplies no saving.

The (L^3) target, a full positive-power saving, and the row local-energy
bound are **not proved**.  The smallest survivor is the complete signed
bulk kernel (\mathcal K_B^{\rm bulk}), with the (d,\mu,h,k,v) sums
still assembled.  It requires a noninvertible inequality using the joint
(\mu)-defect and residue phases; reciprocal (v)-frequency alone is
insufficient.

## 2. Exact statement and hypotheses

Let (X\ge4096) be real, (R=\sqrt X), and let (B) be one fixed
persistent (j=1) Round-113 smooth balanced physical block.  Thus
(L\asymp R^{1/3}), (1\le K/L\le16), and the constants implicit below
depend only on the fixed cutoffs.  Retain the literal real continuum symbol

\[
 A_B(x,z)=W(x/L)\Phi(x/(H+1))
 \left({M\over xz}\right)^{3/4}
 W\!\left(\sqrt{{xX\over4zD^2}}\right),               \tag{116.L6}
\]

extended by zero, with the already frozen floors, tapers, stars, support
crossings, and physical labels.  Put (G_0=\sqrt L/2) and

\[
 b_B(h,k)=\eta((h,k)/G_0)A_B(h,k),\qquad
 a_B^{<}(h,k)=\chi_4(h)b_B(h,k).                       \tag{116.L7}
\]

No physical block, gcd shell, residue sector, or shift family is combined
by an outside absolute value.

Define the exact Möbius coefficients

\[
 \gamma_d=\sum_{e\mid d}\mu(e)\eta\!\left({d/e\over G_0}\right),
 \qquad
 \eta((x,k')/G_0)=\sum_{d\mid x,\ d\mid k'}\gamma_d.  \tag{116.L8}
\]

For odd \(h\) and odd \(d\mid k'\), let
\(s_d=s_d(h)\in[0,d)\) be the
unique residue satisfying (h+2s_d\equiv0\pmod d), and set

\[
 \ell_d={h+2s_d\over d},\qquad
 x_d(t)=d(\ell_d+2t)=h+2s_d+2dt.                      \tag{116.L9}
\]

The accepted (t\)-values are those for which
((x_d(t),k')) lies in the literal support and

\[
 |x_d(t)k'-hk|>L,\qquad |hk'-x_d(t)k|>L.              \tag{116.L10}
\]

They form (O_B(1)) intervals of consecutive integers.  Surround each
such interval by half-integer endpoints and call the resulting real
interval (J).  This convention retains every strict equality boundary
and every support crossing without changing the integer set.

For (m\in\mathbb Z), put

\[
 \mu=\tfrac12-m,qquad \lambda={\mu\over d},
\]

and define

\[
 F_d(t)=R\sqrt{hk}-R\sqrt{x_d(t)k'}+{s_d+t\over2}.    \tag{116.L11}
\]

For those \(m\) for which \(F_d(t)-mt\) has a stationary point
\(t_*\in J\),
let

\[
 x_*={Xk'\over\lambda^2},                             \tag{116.L12}
\]

and define the **exact**, possibly complex transition amplitude

\[
 \mathcal A_{d,J}(h,k,k';\mu)
 =e(-\Theta_{d,\mu})
  \int_J A_B(x_d(t),k')e(F_d(t)-mt)\,dt,              \tag{116.L13}
\]

where

\[
 \begin{aligned}
 \Theta_{d,\mu}
 &=R\sqrt{hk}-{Xk'\over2\lambda}
   +{s_d\over2}-{\ell_d\mu\over2}\\
 &=-{h(\lambda-\lambda_0)^2\over2\lambda}
   -{Xq\over2\lambda}+s_d(\tfrac12-\lambda).
 \end{aligned}                                       \tag{116.L14}
\]

The two displayed forms are identical.  Define the literal signed alias
kernel

\[
 \boxed{
 \mathcal K_B=
 \sum_{\substack{h\ {\rm odd},\ k,k'}} b_B(h,k)
 \sum_{\substack{d\mid k'\\ d\ {\rm odd}}}\gamma_d
 \sum_{J}\ \sum_{\substack{\mu\in\mathbb Z+1/2,\ \mu>0\\t_*\in J}}
 \mathcal A_{d,J}(h,k,k';\mu)e(\Theta_{d,\mu}).}
                                                               \tag{116.L15}
\]

All support and both far gates occur in (J); no schematic gate has been
substituted into (116.L15).  Uniformly on the stationary range,

\[
 \mu\asymp dL^3,qquad
 \#\{\mu:t_*\in J\}\asymp dL^3,qquad
 |\mathcal A_{d,J}|\ll {1\over dL}.                  \tag{116.L16}
\]

On a smooth interior subinterval the usual leading term is

\[
 \mathcal A_{d,J}
 =e(1/8)A_B(x_*,k')
 {\sqrt{Xk'}\over d\lambda^{3/2}}
 +O_B((dL^3)^{-1}),                                   \tag{116.L17}
\]

while (116.L13), rather than (116.L17), is retained at every endpoint or
gate transition.

The exact conclusion is

\[
 \mathcal R_B^{\rm osc}
 =\mathcal K_B-M_B^{(0)}
  +O_\varepsilon(L^3X^\varepsilon),                  \tag{116.L18}
\]

where (M_B^{(0)}) occurs exactly once and is already
(O_\varepsilon(L^3X^\varepsilon)).  Therefore the remaining assertion is

\[
 \boxed{|\mathcal K_B^{\rm bulk}|
        \ll_\varepsilon L^3X^\varepsilon,}            \tag{116.L19}
\]

after removing only the target-safe Poisson/nonstationary/transition
pieces specified below.  Equation (116.L19) is the smallest exact survivor
and is unproved.

For comparison, the lawful but stronger row inequality is still

\[
 \mathfrak L_B:=\sum_{h,k}|T_{h,k}|^2
 \ll_\varepsilon L^4X^\varepsilon,                   \tag{116.L20}
\]

with (T_{h,k}) exactly as in (116.D9).  Since
(\sum|a_B^{<}|^2\ll L^2X^\varepsilon), (116.L20)
implies the desired scalar (L^3) energy bound by Cauchy.  No estimate for
the off-diagonal part of (116.L20) is obtained here.

## 3. Proof or derivation

**Parity and gcd legality.**  Nonzero terms have (h,h') odd.  Writing
(h'=h+2s),

\[
 \chi_4(h)\chi_4(h+2s)=(-1)^s.
\]

For fixed (k'), (116.L8) is ordinary Möbius inversion of the function
(g\mapsto\eta(g/G_0)).  Even (d) cannot divide odd (h').  For odd
(d), the congruence (d\mid h+2s) has the unique solution
(s=s_d+dt).  Since (d) is odd,

\[
 (-1)^{s_d+dt}=e(s_d/2+t/2).                          \tag{116.L21}
\]

This is the point at which the clean chart changes.  Poisson in (t), not
in all (s), has modes (m\in\mathbb Z); hence
(\mu=1/2-m\in\mathbb Z+1/2) and (\lambda=\mu/d).
The alternative expression (\lambda=1/2-m_0/d) is the same lattice after
the integer reindexing (m_0=m+(d-1)/2).  Omitting that reindexing is what
makes the conductor's (d=1) formula look divisor-independent.

Moreover

\[
 |\gamma_d|\le\tau(d),\qquad
 \sum_{d\mid k'}|\gamma_d|\le\tau_3(k')
 \ll_\varepsilon X^\varepsilon.                      \tag{116.L22}
\]

This estimate is used only for target-safe error terms and for the scoped
triangle no-go; it is not inserted into the surviving signed kernel.

**Sharp gates and finite Poisson.**  For fixed (h,k,k'), both gate
expressions in (116.L10) are affine in (x_d(t)).  Their strict
complements, intersected with the fixed slanted support of (116.L6), split
the (t)-line into (O_B(1)) components.  Choosing half-integer endpoints
around each accepted integer component preserves all equality conventions.
Finite Poisson summation on a bounded-variation interval gives

\[
 \sum_{t\in J\cap\mathbb Z}A_B(x_d(t),k')e(F_d(t))
 =\sum_{m\in\mathbb Z}
   \int_J A_B(x_d(u),k')e(F_d(u)-m u)\,du,             \tag{116.L23}
\]

with the symmetric endpoint convention.  Splitting modes according as
(F_d'(J)) contains (m), monotonicity of (F_d'), one first-derivative
integration near the derivative endpoints, and two integrations in the
tails give a collective nonstationary bound

\[
 O_B(1+\log(2+dL^3)).                                  \tag{116.L24}
\]

The total variation of the rescaled literal symbol is (O_B(1)) on each
component.  There are (O(L^3)) outer triples (h,k,k'); (116.L22)--
(116.L24) therefore cost (O_\varepsilon(L^3X^\varepsilon)) globally.
Natural endpoint-transition modes have derivative distance
(O(\sqrt{F_d''})=O(dL)); there are (O(dL)) per endpoint and each exact
integral is (O((dL)^{-1})).  They have the same target-safe total cost.
This proves the error assertion in (116.L18) without smoothing either far
gate.

**Stationary point, amplitude, and phase.**  Differentiating the integrand
phase in (116.L23) gives

\[
 {d\over dt}(F_d(t)-mt)
 =\mu-dR\sqrt{k'/x_d(t)}.
\]

Thus (\lambda=\mu/d=R\sqrt{k'/x_*}), which is (116.L12).  Also

\[
 (F_d-mt)''(t_*)
 =d^2R\sqrt{k'}x_*^{-3/2}
 ={d^2\lambda^3\over Xk'}\asymp d^2L^2.              \tag{116.L25}
\]

The second-derivative integral estimate proves (116.L16).  Stationary
phase with (e(z)=e^{2\pi iz}) gives the (e(1/8)) and Jacobian in
(116.L17).  The normalized cubic and amplitude variations are (O(L^{-2})),
which gives the stated interior remainder.  Direct substitution gives

\[
 F_d(t_*)-mt_*
 =R\sqrt{hk}+{s_d\over2}
  -{Xk'd\over2\mu}-{\ell_d\mu\over2},                \tag{116.L26}
\]

and (k'=dv) gives (116.L1).  Since
(s_d/2-\ell_d\mu/2=-\lambda h/2+s_d(1/2-\lambda)),
the conductor square completion remains exact after adding the residue
term, proving (116.L2).

**Exact gate images.**  At (x=x_*), set

\[
 \lambda_r={Rk'\over\sqrt{hk}}.
\]

Then, with no asymptotic replacement,

\[
 \rho=hk'-x_*k
 ={hk'\over\lambda^2}(\lambda^2-\lambda_0^2),         \tag{116.L27}
\]

\[
 \Delta=x_*k'-hk
 ={hk\over\lambda^2}(\lambda_r^2-\lambda^2).         \tag{116.L28}
\]

Thus the literal stationary gates are

\[
 |\lambda-\lambda_0|>
 {L\lambda^2\over hk'(\lambda+\lambda_0)},\qquad
 |\lambda-\lambda_r|>
 {L\lambda^2\over hk(\lambda+\lambda_r)},            \tag{116.L29}
\]

whenever the positive centres lie in the active chart.  On critical
support the two right sides are between fixed positive multiples of
(L^2).  Each gate therefore removes (O(dL^2)) points from a
(\asymp dL^3) alias interval, not the whole stationary family.  Equations
(116.L27)--(116.L29), rather than a schematic width assertion, are used in
(116.L15).

**Reciprocal frequency and near-hyperbola count.**  Because (d\mid k'),
write (k'=dv).  On every fixed smooth/gate component the (v)-length is
(N_d\asymp L/d), the normalized amplitude has (O_B(1)) total variation,
and its linear frequency is (116.L3).  Abel summation gives the charged
aliaswise estimate

\[
 \left|\sum_{v\in I}W_{d,\mu}(v)e(-\alpha_{d,\mu}v)\right|
 \ll_B \min\!\left({L\over d},
 {1\over\|Xd^2/(2\mu)\|}\right).                     \tag{116.L30}
\]

The resonant set in which the first entry is used satisfies

\[
 \left\|{Xd^2\over2\mu}\right\|\le {d\over L}
 \quad\Longrightarrow\quad
 |Xd^2-j(2\mu)|\ll d^2L^2                             \tag{116.L31}
\]

for an integer (j\asymp dL^3).  Since (u=2\mu) is odd and
(u\asymp dL^3), the products (ju) lie among (O(d^2L^2)) integers.
The elementary divisor bound consequently gives

\[
 \#\{\mu:\text{(116.L31)}\}
 \ll_\varepsilon d^2L^2X^\varepsilon.                \tag{116.L32}
\]

More generally, dyadically counting
(\|Xd^2/(2\mu)\|\le\delta) by the same product-window argument yields

\[
 \sum_{\mu\asymp dL^3}
 \min\!\left({L\over d},
 {1\over\|Xd^2/(2\mu)\|}\right)
 \ll_\varepsilon dL^3X^\varepsilon.                 \tag{116.L33}
\]

After multiplying by the first stationary amplitude ((dL)^{-1}),
(116.L33) costs (L^2X^\varepsilon) for each outer ((h,k)).  The
(L^2) outer pairs therefore give (L^4X^\varepsilon), not (L^3).
Even the resonant count alone has the same capacity:

\[
 (d^2L^2)\cdot(L/d)\cdot(dL)^{-1}=L^2.               \tag{116.L34}
\]

This explicitly charges the aliaswise absolute value.  It is a no-go
calculation, not an allowed final norm step.

**Large-sieve diagonal and exact inverse transform.**  After deleting the
two (O(dL^2)) gate neighbourhoods, a common interior (v)-slice still
sees (M_d\asymp dL^3) reciprocal frequencies.  Any coefficient-uniform
inequality

\[
 \sum_{\mu}\left|\sum_v c_v e(-\alpha_{d,\mu}v)\right|^2
 \le C_d\sum_v|c_v|^2                                 \tag{116.L35}
\]

has (C_d\ge M_d\): take (c_v) supported at one admissible (v).
Thus spacing cannot make the q/v large sieve cheaper than its alias
diagonal.  For (d=1), the transformed diagonal is already

\[
 L^2\ {\rm outer\ rows}\times
 L\ {\rm q\ values}\times
 L^3\ {\rm aliases}\times L^{-2}\ {\rm amplitude}^2
 \asymp L^4,                                           \tag{116.L36}
\]

exactly the full allowance in (116.L20).

There is also an algebraic involution, stronger than a capacity count.
Ignoring only the already retained endpoints, the (\mu)-phase in (116.L1)
is

\[
 g(\mu)=-{Xd^2v\over2\mu}-{\ell_d\mu\over2}.
\]

Poisson on (\mu\in\mathbb Z+1/2) introduces an integer (n), the factor
((-1)^n), and the stationary equation

\[
 g'(\mu)=n,qquad
 \mu=dR\sqrt{{v\over\ell_d+2n}}.                     \tag{116.L37}
\]

At this point

\[
 g(\mu)-n\mu=-dR\sqrt{v(\ell_d+2n)}.                 \tag{116.L38}
\]

Furthermore

\[
 |g''(\mu)|^{-1/2}={\mu^{3/2}\over d\sqrt{Xv}},
\]

which is the exact reciprocal of the first Jacobian
(d\sqrt{Xv}/\mu^{3/2}).  The two (e(\pm1/8)) factors cancel.  Since
(h'=d(\ell_d+2n)), (k'=dv), and
((-1)^{s_d}(-1)^n=(-1)^{s_d+dn}), the original phase, progression, and
character all return.  The sharp support and gates return through the same
finite endpoint pieces.  A second B-process is therefore an exact
capacity-preserving inversion, not the missing inequality.

**Signed norm.**  Cauchy before taking any shift or alias absolute value
gives (116.L20), with diagonal (O(L^4X^\varepsilon)).  Its off-diagonal
must therefore be controlled at diagonal scale.  The reciprocal-frequency
large sieve just audited has no spare factor, and (116.L37)--(116.L38)
shows that transforming it again returns the primal sum.  What remains is
precisely (116.L19): cancellation across the signed ((d,\mu,h,k,v))
family, including (s_d(1/2-\lambda)) and the quadratic
(\lambda-\lambda_0) defect, before any such absolute value.

## 4. First doubtful or unproved step

The first unproved step is exactly (116.L19), or the stronger off-diagonal
part of (116.L20).  All prior steps are identities, finite Poisson
decomposition, one-dimensional oscillatory-integral estimates, or
elementary divisor counting.

No available argument proves simultaneous cancellation in

\[
 (d,\mu,h,k,v)\longmapsto
 e\!\left(R\sqrt{hk}+{s_d\over2}
 -{Xd^2v\over2\mu}-{\ell_d\mu\over2}\right)          \tag{116.L39}
\]

with both gate images and the literal symbol retained.  Taking absolute
values over \(d\), \(\mu\), \(v\)-progressions, or outer pairs loses the
actual assembled character and stops at (L^4).  Applying Cauchy and a
coefficient-uniform large sieve pays an alias diagonal already at the full
local-energy allowance.  Applying the B-process again is the exact inverse.
Therefore a genuinely noninvertible actual-symbol inequality, not another
stationary transformation or a sharper count of (116.L31) alone, is still
required.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| `literal_half_shift_poisson_legality` | **Pass after repair.** Poisson is applied only after (116.L8)--(116.L10); the literal lattice is (\lambda=(1/2-m)/d). |
| `gcd_expansion_and_character_progressions` | **Pass.** Only odd (d) occur, (s=s_d+dt), and the residue phase (s_d(1/2-\lambda)) is retained. No divisorwise absolute value enters (\mathcal K_B). |
| `stationary_alias_range_and_amplitude` | **Pass.** There are (\asymp dL^3) aliases of spacing (1/d), with exact amplitude (116.L13) and size (O((dL)^{-1})). |
| `dual_phase_square_completion` | **Pass after repair.** The conductor square is correct only with the added residue term in (116.L2). |
| `radial_and_determinant_gate_images` | **Pass.** Equations (116.L27)--(116.L29) are exact; each deleted alias neighbourhood has width (\asymp L^2). |
| `reciprocal_q_frequency_resonance_count` | **Pass, but insufficient.** The progression frequency is (Xd^2/(2\mu)); (116.L32)--(116.L34) show that optimal divisor counting still leaves (L^4) capacity. |
| `signed_alias_norm_without_l1` | **Open survivor named.** The exact signed norm is (116.L19); no aliaswise (\ell^1) is hidden in it. |
| `large_sieve_spacing_and_diagonal_cost` | **Fail for the proposed saving.** The constant in (116.L35) is at least (dL^3), and the (d=1) transformed diagonal is already (L^4). |
| `boundary_and_nonstationary_errors` | **Pass.** Literal half-integer interval endpoints, gate crossings, nonstationary modes, and transition modes total (O_\varepsilon(L^3X^\varepsilon)). |
| `actual_symbol_vs_arbitrary_coefficients` | **Pass as a falsification.** The surviving kernel retains the actual residue and defect phases. Any aliaswise or coefficient-uniform norm erases them and would also apply to the known false phase-adapted (L^4) analogue. |
| `fixed_block_and_owner_scope` | **Pass.** Everything is for one fixed (B); (M_B^{(0)}) is subtracted exactly once. No shell or physical-block cancellation is imported. |
| `critical_j1_and_exact_square_j2_boundary` | **Pass.** The statement is only for persistent (j=1), (L\asymp X^{1/6}). The exact-square (j=2), (K/L=16) boundary is not claimed. |
| `external_theorem_hypothesis_fit` | **Pass by non-use.** No external theorem is invoked; finite Poisson, stationary phase, and the divisor-window count are derived here. |
| `linear_vs_energy_capacity` | **Pass.** The scalar energy allowance is (L^3); the optional row energy allowance is (L^4). Equation (116.L36) exhausts, rather than improves, the latter. |
| `downstream_scope` | **Pass.** No BAL parent, M2 parent, M1 statement, endpoint uniformity, M9, or Gauss-circle exponent is asserted. |

## 6. Dependencies and exact artifacts used

The derivation uses only the following permitted artifacts, read in full:

- `protocol.md`;
- `state/proof_obligations.yml`, especially the accepted Round-113 literal
  dictionary, Round-114 corridor reduction, and Round-115 phase-free mode;
- `state/active_campaign.yml`;
- `strategy/conductor_0821_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/synthesis.md`;
- `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/reviews/conductor_round115_identity_and_zero_mode.md`;
- `rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/candidates/conductor_half_shift_alias_defect.md`;
- the generated task brief
  `rounds/codex-managed/m9-m2-balanced-nonzero-alias-defect-gate/briefs/literal_alias_local_energy_attack.md`.

No sibling Round-116 report, excluded context, web source, or unstated
external estimate was used.  The only target-safe owner invoked is the
accepted fully assembled (M_B^{(0)}) bound; it is used once in
(116.L18).

## 7. Recommended state effect

**Recommendation: revise.**  Replace the candidate's divisor-independent
half-integer chart and near-hyperbola condition by the literal
divisor-progressive formulas (116.L1)--(116.L3), promote after seam review
the target-safe finite-Poisson error reduction, and record the exact
second-B-process involution plus the aliaswise reciprocal-frequency
(L^4)-capacity obstruction as scoped no-go results.

Retain `M9-M2-balanced-double-far-oscillatory-remainder`,
`M9-M2-balanced-double-far-actual-energy`, and
`M9-M2-smooth-balanced-quarter-packet-estimate` as open.  Do not promote
(116.L19) or (116.L20).  The mechanism should be parked unless a later
argument supplies a noninvertible signed inequality for the full kernel
(116.L15); another one-alias triangle, reciprocal-frequency large sieve,
or second B-process cannot furnish the missing factor (L).

