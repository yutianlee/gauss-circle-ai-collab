# Round 197 common-cell power/operator post-repair verification

- Campaign: m9-m1-t1-p2-four-corner-allocation-commutator-gate
- Role: independent post-repair power/operator verification
- Starting graph SHA-256:
  b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae
- Final candidate SHA-256:
  285ea0975eb3d48691ffb27b5a83e251d33a68062eb4d14dd54972f6af6296c0
- Numerical theorem evidence: none

## 1. Result

**GREEN.**  On the final candidate hash above, the explicit repairs
(197.C8a)--(197.C8c), (197.C9a)--(197.C9k),
(197.C22)--(197.C24b), and (197.C28a) preserve and strengthen the earlier
power/operator PASS.

The repair now makes all three moving pieces exact:

1. the common-cell code first tests the complete arithmetic and literal
   live domain, then records a closed list of sharp branch, cell, and
   trace labels;
2. the core, cap, open, physical-source, and safe-projector operators are
   typed as linear functionals of a mask applied to the physical parent
   before Fourier, height, Farey, or packet operations; and
3. the actual lower coefficient difference is split by an exact
   three-term rule into smooth, normalized-BV, and selector
   commutators.

The complete raw count remains

\[
 D_L\sum_{\kappa\ll L}(1+L/\kappa)^2
 \ll D_LL^2X^\varepsilon.
\]

The smooth and BV ledgers are respectively

\[
 {D_L\over L}\,D_LL^2X^\varepsilon
 =D_L^2LX^\varepsilon\ll L^2X^\varepsilon,
\]

\[
 D_L^2\operatorname{Var}(\eta_L)\cdot
 LX^\varepsilon
 \ll D_L^2LX^\varepsilon\ll L^2X^\varepsilon.
\]

The selector commutator vanishes for all sufficiently large shells and
is paid absolutely on a \(K_{\rm sel}\)-dependent bounded set.  Hence

\[
 |\mathscr R_{\rm core,out}^\sigma(P_{\rm cc}W)|
 +|\mathscr R_{\rm open,out}^\sigma(P_{\rm cc}W)|
 \ll_{B,C_0,K_{\rm sel},\varepsilon}L^2X^\varepsilon
\]

with no hidden dependence on \(X,L,\sigma,\kappa,Y,\mathfrak m,q,a,J\),
an orientation, a Fourier copy, or a literal cell.

## 2. Exact statement and hypotheses

The verified mask is

\[
 P_{\rm cc}
 =P_2\mathbf1_{(m,\beta)=1}
       \mathbf1_{\chi_4(\alpha m)=-1}C_{\rm lit},
\]

where \(C_{\rm lit}\) means equality of the arithmetic/live sharp codes
at \((m,g\alpha)\) and \((\alpha,gm)\).  The selector width
\(K_{\rm sel}>0\), low-height exponent \(B>0\), and Farey constant
\(C_0\ge2\) are fixed independently of every asymptotic and packet
variable.

The accepted coefficient hypotheses are exactly the K184.11
moving-factor ledger, the uniformly \(C^1\) literal smooth cells, the
scale-normalized BV bound for \(\eta_L\), the selector truth table
\((1,0,0,1)\), and the total zero-extended K185 endpoint.  The accepted
operator hypotheses are the Round-193 transported physical-mask identity
and the Round-195 deletion-stable fixed-packet-to-outer ledger.  The
amendments introduce no new analytic hypothesis.

The theorem remains deliberately silent about nonemptiness, density,
nonvanishing, or positive mass of \(P_{\rm cc}\).

## 3. Verification

### 3.1 Arithmetic and literal dead/live code

Equation (197.C8a) tests positivity, \(uv=N\), oddness of the character
leg, squarefreeness, and allocation coprimality.  The separate
\(I_{\rm lit}\) test covers the named shell, frequency, height, strict
cone, profile support, hard sample, endpoint support, and zero-extension
predicates.

If either test fails, (197.C8c) assigns the single code \(\dagger\).  A
live/dead mismatch therefore cannot enter \(P_{\rm cc}\).  If both codes
are \(\dagger\), both lower coefficients are zero by the named zero
extensions, so their difference contributes nothing.

On the live domain, the closed list (197.C8b)--(197.C8c) contains:

- shell, frequency, height, and strict-cone labels;
- profile support, plateau, and branch;
- the actual \(\Phi\)- and \(W_{\rm tr}\)-cell indices;
- floor, star, tie, half-weight, hard-sample, endpoint, and sign traces;
- crossing data, including the real-\(X\) ratio branch.

Thus equality of live codes gives the same numerical sharp multiplier
\(K_{\rm sharp}\) and the same branch formula at both lower inputs.  The
code correctly excludes evaluated smooth values, \(\eta_L\), and
\(\rho_N\): those changes are handled by (197.C22d).  Accidental
coefficient vanishing does not alter the code.

Actual cell indices, rather than reusable informal labels, ensure that
the two inputs lie in one literal \(C^1\) cell.  The code equality is
symmetric, so it does not disturb lower-orbit closure.

### 3.2 Physical, Farey, and outer operator typing

Equation (197.C9a) is the complete physical atom, containing the two
actual endpoint coefficients, character product, Fejer/radical scalar,
and physical zero extensions.  The mask is applied to this parent atom.

Equations (197.C9b)--(197.C9c) define the physical inward cross gcd in
both primitive orientations before any packet exists.  The notation now
separates this \(\kappa\) from both \(K_{\rm sel}\) and the spectral lift
gcd \(\mathfrak m\).

Equations (197.C9d)--(197.C9g) reproduce the accepted fixed packet,
centered inverse, \(T\), \(A\), Farey family, \(T=0\) convention, and
simultaneous strict \(T\ge1\) core inequalities.  The power-of-two
projective-band label \(J\le j_q(a,v)<2J\) is now typed explicitly.

Equations (197.C9h)--(197.C9k) define one linear outer restoration
\(\mathcal O_{195}^\sigma\), including the
\(\mathfrak m^{-1}\) lift weight and the accepted anchor, band, divisor,
shell, dyadic, orientation, and zero-extension data.  It takes no modulus
at a fixed height, orientation, anchor, or Fourier mode.  The cap and
open packet sets are disjoint and exhaustive, so for every physical
\(M\le P_2\),

\[
 \mathscr R_{\rm core,out}^\sigma(MW)
 =\mathscr R_{\rm cap,out}^\sigma(MW)
  +\mathscr R_{\rm open,out}^\sigma(MW)
\]

is an exact identity of the same linear operator.  Packet predicates are
not inserted into the lower orbit.

The final candidate also defines
\(\mathscr H_{\rm out}^\sigma(MW)\) and
\(\mathscr S_{\le192,\rm out}^\sigma(MW)\) and states the exact typed
identity

\[
 \mathscr R_{\rm core,out}^\sigma(MW)
 =\mathscr H_{\rm out}^\sigma(MW)
  -\mathscr S_{\le192,\rm out}^\sigma(MW).
\tag{197.C28a}
\]

Here the first term is the complete opposing physical source after the
accepted monotone and low-\(h\) exits, while the second recomputes every
Round-187--Round-192 safe projector on \(MW\) under the same outer
assembly.  This closes the last operator-typing seam in (197.C29)--(197.C31).
The transported mask commutator, births, deaths, carries, unequal
translations, both \(T\) branches, cells, crossings, anchors, phases,
and zero extensions remain in the core.  The one real part occurs only
after complete restoration.

### 3.3 Actual factorization and product rule

On a common live code the accepted K184.11 ledger is exactly

\[
 a^{\rm lit}_{L,X,\sigma}(u,v)
 =K_{\rm sharp}\eta_L(u)b^{\rm sm}_{L,X,\sigma}(u,v),
\]

where

\[
 b^{\rm sm}(u,v)
 =\Phi\!\left({u\over H+1}\right)
  W_{\rm tr}\!\left(\sqrt{{4q_Xu\over v}}\right)
  \left({L^2\over uv}\right)^{3/4}.
\]

There is no omitted moving factor.  The last factor is actually invariant
between the two lower allocations because both products equal \(N\);
retaining it inside \(b^{\rm sm}\) is harmless.

On live support \(u,v\asymp L\).  The accepted cellwise derivative bounds
and the elementary derivatives of \(u/v\) and \((uv)^{-3/4}\) give

\[
 |K_{\rm sharp}|+\|\eta_L\|_\infty
 +\operatorname{Var}(\eta_L)+\|b^{\rm sm}\|_\infty
 +L\|\nabla b^{\rm sm}\|_\infty
 \ll_\varepsilon X^\varepsilon.
\]

The input displacement obeys

\[
 |m-\alpha|\le D_L/g\le D_L,\qquad
 |g\alpha-gm|\le D_L,
\]

and hence the smooth difference is
\(O_\varepsilon(D_L/L\,X^\varepsilon)\).

With the notation in (197.C22c), direct expansion gives

\[
\begin{aligned}
 &\rho_0\eta_0(b_0-b_1)
 +\rho_0b_1(\eta_0-\eta_1)
 +(\rho_0-\rho_1)\eta_1b_1\\
 &=\rho_0\eta_0b_0-\rho_1\eta_1b_1.
\end{aligned}
\]

Thus (197.C22d) is an exact identity for the actual lower coefficient,
not a generic-array replacement.  The first term supplies the
\(D_L/L\) gain.  For the second term, a fixed BV increment is crossed by
\(O(D_L^2)\) ordered pairs; the uniform finite \(g\le G_0\) multiplicity
and \(O(LX^\varepsilon)\) upper completions give
\(D_L^2LX^\varepsilon\).  Fresh epsilon allocation absorbs only finite
products and logarithms.

### 3.4 Selector and constant dependence

Under the lower swap, each selected prime outside \(g\) is complemented
between the two character legs, while each selected prime in \(g\)
remains on the character leg.  The truth table \((1,0,0,1)\) can change
only when exactly one selected prime divides \(g\).

The strict cone and lower closeness give the uniform finite bound
\(g\le G_0\).  Since the selected primes are distinct,

\[
 \delta_{G_0}
 =\min_{\substack{p\le G_0\ {\rm prime}\\q\ne p\ {\rm prime}}}
   |\log(q/p)|>0.
\]

If exactly one selected prime divides \(g\), the selection condition
forces

\[
 \delta_{G_0}\le|\log(q_N/p_N)|
 \le K_{\rm sel}L^{-1/2}.
\]

Therefore the selector commutator is zero once
\(K_{\rm sel}L^{-1/2}<\delta_{G_0}\).  The remaining shells satisfy an
upper bound depending only on \(K_{\rm sel}\) and the fixed structural
constant \(G_0\); there \(D_L=O_{K_{\rm sel}}(1)\), so the raw
\(D_LL^2X^\varepsilon\) count is already
\(O_{K_{\rm sel},\varepsilon}(L^2X^\varepsilon)\).

This accounts for every displayed constant.  \(B\) pays the
polylogarithmic low-height and outer losses; \(C_0\) is the fixed Farey
constant; \(K_{\rm sel}\) pays the bounded selector shells.  The shell
constants, fixed cell family, and profiles are structural data of the
accepted transform.  No asymptotic or packet dependence is suppressed.

## 4. First doubtful or unproved step

There is no doubtful step introduced by the final repairs inside the
stated \(P_{\rm cc}\) theorem.  The first unproved step remains a target
bound for

\[
 P_{\partial\rm lit}\ \dot\cup\ P_{s\rm f}\ \dot\cup\ P_{g\rm f}
\]

inside the Round-195 open packet region.  On a sharp ratio face aligned
with \(g\),

\[
 \left({g\alpha\over m}-g\right)
 \left({gm\over\alpha}-g\right)<0
\qquad(\alpha\ne m),
\]

so all \(O(LD_L)\) close lower pairs may cross.  After upper completion,
the available capacity is \(D_LL^2X^\varepsilon\), not
\(D_L^2LX^\varepsilon\).  No literal face-by-face transversality theorem
uniform in real \(X\) is present, and capacity supplies no literal lower
mass.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Arithmetic/live code | **PASS.** \(I_{\rm ar}\), \(I_{\rm lit}\), and \(\dagger\) prevent unrecorded arithmetic or support exits. |
| Sharp-list exhaustiveness | **PASS.** The closed labels cover every K184/K185 discontinuous field while leaving smooth, BV, and selector values to (197.C22d). |
| Dead/dead orbit | **PASS.** Both lower coefficients are zero, so it adds no unpriced term. |
| Product-rule expansion | **PASS.** The three terms telescope exactly to \(\rho_0\eta_0b_0-\rho_1\eta_1b_1\). |
| Smooth and BV powers | **PASS.** Each ends at \(D_L^2L\ll L^2\). |
| Selector | **PASS.** It vanishes on large shells and the bounded shells cost only a \(K_{\rm sel}\)-dependent constant. |
| Farey typing | **PASS.** Packet, band, \(T=0\), and all simultaneous \(T\ge1\) conditions match the accepted core. |
| Mask timing | **PASS.** Every mask is evaluated on the physical parent before spectral operations. |
| Outer restoration | **PASS.** Lift, anchor, band, divisor, shell, dyadic, orientation, and zero-extension data precede the single real part. |
| Source/safe/core identity | **PASS.** (197.C28a) now types exactly the subtraction used in (197.C29)--(197.C31). |
| Cap/open subtraction | **PASS.** It is an exact partition of the same recomputed masked core. |
| Constant dependence | **PASS.** \(B,C_0,K_{\rm sel},\varepsilon\) cover every nonstructural fixed parameter. |
| Whole-sector extension | **FAIL, correctly quarantined.** The aligned sharp-face complement retains \(D_LL^2\) capacity. |

## 6. Dependencies and exact artifacts used

The final amended candidate was read completely:

- rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/candidates/formalized_hard_m1_t1_p2_common_cell_allocation_commutator_sector.md,
  SHA-256
  285ea0975eb3d48691ffb27b5a83e251d33a68062eb4d14dd54972f6af6296c0.

The repaired coefficient statement was checked against:

- proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md,
  SHA-256
  3387615b5522deeb4c63021fbdf4a665afa2c405052f2ff0868bed40338e602f.

The unchanged accepted source/operator interfaces are:

- proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md,
  SHA-256
  4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160;
- proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md,
  SHA-256
  470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83;
- proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md,
  SHA-256
  4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009.

The prior seam result being replayed is:

- rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/reviews/common_cell_power_operator_scope_seam_review.md,
  SHA-256
  a5062e07f293985e57c5f243f24105cf37796da39521c3b9eb07b8ed6c1ca38f.

No web source, diagnostic computation, shared state, or sibling report
was used as theorem evidence.

## 7. Recommended state effect

**GREEN: retain the narrow promotion recommendation without expansion.**
After the other required reviews and a valid State Patch, the candidate
may support one subordinate proved_internal \(P_{\rm cc}\) node.
Record the refined complement only in that node and the open owner's
next action.  Do not mutate the accepted Round-184, Round-185,
Round-193, or Round-195 nodes, and do not change any parent, bridge,
theorem, endpoint-uniformity claim, or exponent.

The route-wide terminal label remains
p2_four_corner_orbit_boundary_self_return_no_go; GREEN applies only to
the fully typed common-cell subsector.
