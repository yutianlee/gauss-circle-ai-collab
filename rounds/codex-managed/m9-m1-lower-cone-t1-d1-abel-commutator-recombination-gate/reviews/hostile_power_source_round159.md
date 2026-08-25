# Round 159 hostile analytic, power, and source seam review

- Campaign: `m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate`
- Role: terminal hostile analytic/power/source reviewer
- Starting graph SHA-256: `8a0f917fb8117e9dbaf287d9f773046ff201729d2d8d8c3df1a51bca7815574b`
- Allocation: 100% analytic/algebraic; no computation

## 1. Result

### Verified route-scoped no-go, with one proof-text repair

Subject to the separately reviewed exact full-Abel/common-profile
recombination, the analytic and power conclusions of the Round 159 kernel
are correct.  In particular:

1. the exact residual band has four genuinely moving endpoint curves, with
   clipping at the centered-cell seam and with the strict $V$-edge and
   closed $2V$-edge retained;
2. the shifted Fourier zero mode is $h=-1$, and it is safely
   $O_\varepsilon(X^\varepsilon)$ in raw normalization because
   $\chi _4$ remains;
3. the complete Erdos--Turan/ordinary second-derivative ledger is

   \[
     \frac{M}{Q}+\sqrt{KQ}+\frac{M}{\sqrt K}+1,
     \qquad K=\sqrt{NM},
     \tag{159.HPS1}
   \]

   and its target feasibility requires $M\geq N^{2/3}$;
4. the literal Vaaler/Fejer incidence ledger is

   \[
     E_J\ll_\varepsilon
     \left(\frac KJ+\sqrt V+\sqrt M+1\right)X^\varepsilon,
     \tag{159.HPS2}
   \]

   so this displayed route requires
   $J\geq KM^{-3/4}$ and $V\leq M^{3/2}$;
5. the transformed-pair capacity at the literal height is exactly

   \[
     N^{195/796}M^{1295/3184+\varepsilon},
     \tag{159.HPS3}
   \]

   and reaches the raw target only if $M^{1093}\geq N^{780}$;
6. the older $M^{703}\geq N^{390}$ condition belongs only to the
   Round 158 favorable fixed-boundary model with an independently granted
   $M/J$ error.  It is not contradicted or replaced by (159.HPS2);
7. the stationary locations, reciprocal phases, dual length, absolute
   stationary amplitude, and exponent-pair $B$-self-return are correct.
   Only these convention-independent data are certified here; the literal
   global prefactor and eighth-root phase in the displayed Poisson formula
   remain quarantined from graph use; and
8. incomplete-quadratic completion has favorable raw capacity
   $N^{1/2}X^\varepsilon$, hence the same formal requirement
   $M\geq N^{2/3}$.

There is one repair to the printed proof of (159.HPS2).  Equation
(159.MA31) is stated only while the sampled point and endpoint lie in the
same half-cell; by itself it does not cover the periodic Fejer kernel seen
across the centered-cell seam.  The bound nevertheless survives, because
the exact shifted-root identities in Section 3.2 below count both the
same-half and wrap-around incidences at once.  The report should use that
argument in place of the restricted sentence around (159.MA31).

No target theorem and no strict owner-complete range is proved.  Every
failed power comparison above is an upper-bound capacity of its named
route, never a lower bound for the signed sum or a universal barrier.

## 2. Exact statement and hypotheses

Keep

\[
 q_0=4N,\qquad K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\leq K,\qquad M\leq N^{1/2},
 \tag{159.HPS4}
\]

and write

\[
 T_U(V)=\sum_{\ell\asymp M}\chi _4(\ell)\widetilde w_U(\ell)
 e(\sqrt{N\ell})
 \mathbf 1_{\{V<|r(\ell)|\leq2V\}},
 \quad
 r(\ell)=\kappa(\ell)^2-N\ell,
 \tag{159.HPS5}
\]

where

\[
 \kappa(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,
 \qquad
 \|\widetilde w_U\|_\infty+
 \operatorname {Var}(\widetilde w_U)\ll_\varepsilon X^\varepsilon.
 \tag{159.HPS6}
\]

The required raw estimate is

\[
 |T_U(V)|\ll_\varepsilon M^{3/4}X^\varepsilon;
 \tag{159.HPS7}
\]

restoring $w_U=M^{-3/4}\widetilde w_U$ turns this into the scalar
$O_\varepsilon(X^\varepsilon)$ target.

Put $y=\sqrt{N\ell}$, $k=\kappa(\ell)$, and
$\delta=y-k\in[-1/2,1/2)$.  A half-integer tie is impossible because
$y^2=N\ell$ is an integer.  Exactly,

\[
 r=-\delta(2k+\delta).
 \tag{159.HPS8}
\]

For $s>0$, define

\[
 a_s(k)=k-\sqrt{k^2-s},\qquad
 b_s(k)=\sqrt{k^2+s}-k.
 \tag{159.HPS9}
\]

For sufficiently large $K$, all radicals needed for
$s\in\{V,2V\}$ are real.  The literal band in the centered cell is

\[
 \begin{aligned}
 \mathcal B_{k,V}={}&
 \{-u:a_V(k)<u\leq a_{2V}(k),\ 0<u\leq\tfrac12\}\\
 &\cup
 \{u:b_V(k)<u\leq b_{2V}(k),\ 0\leq u<\tfrac12\}.
 \end{aligned}
 \tag{159.HPS10}
\]

The first component is the positive-defect branch and the second the
negative-defect branch.  If a lower endpoint reaches $1/2$, that
component is empty.  If only an upper endpoint reaches $1/2$, it is
clipped there with the displayed centered-cell convention.  The lower
dyadic edge remains strict and the upper dyadic edge remains closed.
Because there is no half-integer tie, the formal inclusion choice at the
cell seam does not change a sampled term, but it must remain visible in a
finite polynomial identity.

All conclusions below concern the actual BV profile (159.HPS6), or an
explicitly identified smoother/favorable model.  No arbitrary bounded
coefficient theorem is asserted.

## 3. Proof and derivation

### 3.1 Fourier coefficients and the safe shifted mode

Let $\gamma_h(k;V)$ be the Fourier coefficient of the two-component
indicator (159.HPS10).  With $\alpha=V/K$, direct differentiation of
(159.HPS9), followed by clipping, gives

\[
 |\gamma_0|+\operatorname {Var}\gamma_0\ll\alpha,
 \qquad
 |\gamma_h|\ll\min(\alpha,|h|^{-1}),
 \qquad
 \operatorname {Var}\gamma_h\ll\alpha\quad(h\ne0).
 \tag{159.HPS11}
\]

Indeed, each endpoint derivative is $O(s/k^2)$, while the physical
$k$-hull has length $O(K)$.  Clipping is monotone and introduces only
the finitely many displayed transitions.

Since $e(h\delta)=e(h\sqrt{N\ell})$, the built-in phase shifts $h$
to $h+1$.  At $h=-1$ the square-root phase disappears, but the term is

\[
 \sum_{\ell\asymp M}\chi _4(\ell)\widetilde w_U(\ell)
 b_{-1,J}(\kappa(\ell);V).
 \tag{159.HPS12}
\]

The Vaaler coefficient correction at this fixed mode has the same bounded
variation type as (159.HPS11).  Thus the product in (159.HPS12) has
supremum plus total variation $O_\varepsilon(X^\varepsilon)$.
Partial sums of $\chi _4$ are bounded, including its zero values on even
integers, so discrete Abel summation proves

\[
 \text{raw shifted }h=-1\text{ mode}\ll_\varepsilon X^\varepsilon.
 \tag{159.HPS13}
\]

Boundary half-weights and exact hard-boundary atoms remain in the separate
Vaaler remainder; they are not silently assigned to (159.HPS13).

### 3.2 The two literal boundary treatments

It is useful to use an equivalent pointwise interval representation
parameterized by $y$ rather than by $k$:

\[
 p_s(y)=\sqrt{y^2+s}-y,\qquad
 n_s(y)=y-\sqrt{y^2-s}.
 \tag{159.HPS14}
\]

At the sampled value $t=\delta$, this interval indicator is exactly the
same hard defect mask as (159.HPS10), although its auxiliary endpoints as
functions of a free $t$ are different.  Vaaler's fixed-interval theorem
may be applied separately at each $y$, and the endpoint phases are then
governed exactly by $\sqrt{N\ell+s}$ and
$\sqrt{N\ell-s}$.

For the ordinary Erdos--Turan treatment, the second derivatives satisfy

\[
 \left(h\sqrt{N\ell\pm s}\right)''
 \asymp \frac{hK}{M^2}
 \quad(1\leq h\leq Q),
 \tag{159.HPS15}
\]

uniformly for $s\in\{V,2V\}$, since $s/K^2=O(K^{-1})$.  The
second-derivative estimate and Abel transfer give

\[
 \frac{M}{Q}+
 \sum_{1\leq h\leq Q}\frac1h
 \left(\sqrt{hK}+\frac{M}{\sqrt{hK}}\right)
 \ll
 \frac{M}{Q}+\sqrt{KQ}+\frac{M}{\sqrt K}.
 \tag{159.HPS16}
\]

The nonexceptional Fourier modes have the same aggregate capacity, so
(159.HPS16), not $M/Q$ alone, is the discovery report's complete
ledger.  When the optimizer
$Q\asymp M^{2/3}K^{-1/3}$ is at least one, its first two terms are
$\asymp M^{1/3}K^{1/3}$.  Comparing with $M^{3/4}$ gives

\[
 K\leq M^{5/4}
 \quad\Longleftrightarrow\quad
 M\geq N^{2/3}.
 \tag{159.HPS17}
\]

If the optimizer is below one, $Q=1$ leaves an $O(M)$ capacity and
does not help.  Thus the ordinary route has no target range in
$M\leq N^{1/2}$.

For the sharper arithmetic incidence treatment, let

\[
 \mathfrak F_J(t)=\frac1{(J+1)^2}
 \left(\frac{\sin\pi(J+1)t}{\sin\pi t}\right)^2
 \ll\min\left(1,\frac1{J^2\|t\|^2}\right).
 \tag{159.HPS18}
\]

The wrap-safe identities missing from the local wording of (159.MA31)
are

\[
 \begin{aligned}
 \|\delta+p_s(y)\|&=\|\sqrt{N\ell+s}\|,\\
 \|\delta-n_s(y)\|&=\|\sqrt{N\ell-s}\|.
 \end{aligned}
 \tag{159.HPS19}
\]

They hold on the circle and hence include an endpoint near $-1/2$
viewed from a sample near $+1/2$, and conversely.  Choose the nearest
integer $m$ to the square root on the right.  With
$t=m^2-N\ell\in\mathbb Z$,

\[
 |t\mp s|\asymp K\,\|\sqrt{N\ell\pm s}\|.
 \tag{159.HPS20}
\]

The $m$-hull has length $O(K)<N$.  The accepted fixed-root estimate
therefore gives $O_\varepsilon(\sqrt{(N,t)}X^\varepsilon)$ samples for
fixed nonzero $t$.  For an integer interval $I$ of length $D$ near
$|t|\asymp V$, a divisor split gives

\[
 \sum_{t\in I}\sqrt{(N,t)}
 \ll_\varepsilon(D+\sqrt V+1)X^\varepsilon.
 \tag{159.HPS21}
\]

If a shell reaches $t=0$, the exact-square fibre contributes the
additional $O_\varepsilon(\sqrt M X^\varepsilon)$.  Dyadic shells of
width $2^mK/J$, weighted by $2^{-2m}$, yield (159.HPS2).  A genuinely
clipped cell-seam endpoint is handled with the nearest odd integer to
$2\sqrt{N\ell}$; its nonzero defect modulo $4N$ costs
$O_\varepsilon((K/J+1)X^\varepsilon)$.  Thus no wrap, equality atom, or
clipped endpoint is omitted.

For the right side of (159.HPS2) itself to be at most the raw target, one
must take, up to ceilings and $X^\varepsilon$,

\[
 J\geq J_{\mathrm{lit}}:=KM^{-3/4}=N^{1/2}M^{-1/4},
 \qquad V\leq M^{3/2}.
 \tag{159.HPS22}
\]

These are feasibility conditions for this unsigned error bound only.

### 3.3 Transformed-pair powers and the older favorable model

For a nonzero shifted frequency $q=h+1$, an exponent pair
$(\kappa_0,\lambda_0)$ gives the unweighted interval bound

\[
 |q|^{\kappa_0}N^{\kappa_0/2}
 M^{\lambda_0-\kappa_0/2+\varepsilon}.
 \tag{159.HPS23}
\]

The source condition $M\leq |q|K$ holds.  A BV weight is inserted only
afterward.  In the favorable endpoint-in-phase placement the $1/|h|$
coefficient is retained, so absolute mode summation costs $J^{\kappa_0}$.
The sharper coefficient bound $\min(V/K,1/|h|)$ does not improve the
power: at the literal height,

\[
 \frac{V}{K}J_{\mathrm{lit}}=VM^{-3/4}>(\log(2X))^A,
 \tag{159.HPS24}
\]

and the high-frequency tail already has size $J^{\kappa_0}$, up to
$X^\varepsilon$.

For

\[
 (\kappa_0,\lambda_0)=
 \left(\frac{195}{796},\frac{235}{398}\right),
 \tag{159.HPS25}
\]

the fixed-mode factor is
$N^{195/1592}M^{745/1592}$.  Multiplication by
$J_{\mathrm{lit}}^{195/796}$ gives (159.HPS3).  Since
$M^{3/4}=M^{2388/3184}$, the comparison is exactly

\[
 N^{780}M^{1295}\leq M^{2388}
 \quad\Longleftrightarrow\quad
 M^{1093}\geq N^{780}.
 \tag{159.HPS26}
\]

There is no conflict with Round 158.  The three ledgers are:

| Boundary treatment | Complete requirement or cost | Resulting condition |
|---|---:|---:|
| favorable fixed-boundary model | grant $M/J$, take $J=M^{1/4}$ | $M^{703}\geq N^{390}$ |
| literal root incidence | (159.HPS2), take $J=KM^{-3/4}$ | $M^{1093}\geq N^{780}$ |
| ordinary moving-boundary discrepancy | all of (159.HPS16), optimize $Q$ | $M\geq N^{2/3}$ |

In the first row the raw transformed-pair term is

\[
 N^{195/1592}M^{1685/3184+\varepsilon},
 \tag{159.HPS27}
\]

whose comparison with the target is precisely
$M^{703}\geq N^{390}$.  The $M/Q$ term in (159.HPS16) may not be
detached from $\sqrt{KQ}+M/\sqrt K$ and substituted for that favorable
grant.  The two Round 159 bounds are alternative complete controls of the
literal sampled boundary, whereas the Round 158 row is an explicitly
easier fixed-boundary benchmark.

### 3.4 Stationary carrier and convention-independent self-return

Splitting the character gives phases

\[
 F_{\sigma,q}(x)=q\sqrt{Nx}+\frac{\sigma x}{4},
 \qquad \sigma\in\{1,-1\}.
 \tag{159.HPS28}
\]

For Poisson frequency $m$, put $d=4m-\sigma$.  A stationary point
exists precisely when $qd>0$, and direct differentiation gives

\[
 x_{q,d}=\frac{4q^2N}{d^2},\qquad
 F_{\sigma,q}(x_{q,d})-mx_{q,d}=\frac{q^2N}{d},
 \tag{159.HPS29}
\]

and

\[
 |F''_{\sigma,q}(x_{q,d})|^{-1/2}
 =\frac{4\sqrt2\,|q|N^{1/2}}{|d|^{3/2}}.
 \tag{159.HPS30}
\]

For $\sigma=1$, $d\equiv3\pmod4$; for $\sigma=-1$,
$d\equiv1\pmod4$, so $\sigma=-\chi_4(d)$.  The dual support is

\[
 |d|\asymp |q|\sqrt{N/M}.
 \tag{159.HPS31}
\]

These locations, congruences, phases, support length, and absolute
amplitude are convention-independent.  The exact overall constant and
eighth-root stationary factor depend on the chosen Poisson and Fourier
normalizations and are not promoted by this seam.

Applying $(\kappa,\lambda)$ on the dual interval gives

\[
 |q|^{\lambda-1/2}N^{\lambda/2-1/4}
 M^{3/4+\kappa-\lambda/2+\varepsilon},
 \tag{159.HPS32}
\]

which is identically the direct square-root estimate for

\[
 B(\kappa,\lambda)=
 \left(\lambda-\frac12,\kappa+\frac12\right).
 \tag{159.HPS33}
\]

Thus $B(18/199,593/796)=(195/796,235/398)$.  For $q=1$, the two
branches are the already accepted reciprocal phases
$e(N/(4m-1))$ and $e(N/(4m+1))$; for $q=-1$, (159.HPS29) gives
the sign-reversed carrier after reindexing the negative denominators.
General $q$ changes the numerator to $q^2N$ but supplies no automatic
cancellation.

### 3.5 Incomplete quadratic and source interfaces

The exact quotient projector has normalization $1/(2N)$.  After the
residual interval is summed geometrically, an odd projector frequency
$a\bmod4N$ contributes a denominator

\[
 |1-e_{4N}(a)|^{-1}\ll
 \frac{N}{\min(a,4N-a)}.
 \tag{159.HPS34}
\]

Müllner's incomplete quadratic estimate contributes
$\sqrt{N(a,N)}X^\varepsilon$ on the physical interval.  Therefore,
even after granting the joint BV needed to move every literal coefficient
through the two Abel steps,

\[
 |T_U(V)|\ll_\varepsilon
 \frac1N\sum_{\substack{a\bmod4N\\a\ \mathrm{odd}}}
 \frac{N\sqrt{N(a,N)}}{\min(a,4N-a)}X^\varepsilon
 \ll_\varepsilon N^{1/2}X^\varepsilon.
 \tag{159.HPS35}
\]

The last harmonic gcd sum is $O_\varepsilon(X^\varepsilon)$.  Comparing
with (159.HPS7) again gives $M\geq N^{2/3}$.  Without the joint BV
grant, the literal route stops earlier; (159.HPS35) is still only a
favorable upper capacity.

The source conclusions are also correctly scoped.  Bourgain's audited
global pair controls one standard smooth phase and accepts the actual BV
weight only through subsequent Abel summation.  The transformed pair is
licensed by the permitted Round 158 Tao--Trudgian--Yang audit, again only
mode by mode.  Vaaler's fixed-interval theorem supplies the pointwise
Fejer error but not a sampled $M/J$ bound.  Montgomery--Vaughan gives a
continuous-parameter mean square for separated real frequencies, not the
needed pointwise fixed-$N$ multimode estimate; exact and near collisions
also remain to be grouped and separated.  The Huxley 2003 repository card
contains no audited theorem or hypotheses, so it licenses no import.

## 4. First doubtful or unproved step

The first doubtful line in the supplied source-audit derivation is the
same-half-cell restriction attached to (159.MA31): a periodic Fejer kernel
also sees the opposite representation of the centered-cell seam.  This
review repairs that local proof seam by (159.HPS19)--(159.HPS21), without
changing the claimed power (159.HPS2).

After that repair, the first unresolved mathematical seam is the raw
signed estimate (159.HPS7).  More precisely:

- for $V>M^{3/2}$, the first missing input is signed control of the
  literal hard-boundary/Fejer incidences beyond the unsigned
  $\sqrt V$ capacity;
- for $V\leq M^{3/2}$, after $J\geq J_{\mathrm{lit}}$, the first missing
  input is a genuinely joint estimate for all nonzero shifted modes with
  their moving coefficients.  Pointwise exponent pairs give
  (159.HPS3), the $B$-process self-returns, and incomplete completion
  gives (159.HPS35).

No audited source supplies either input.  Failure of these named routes
does not show that $T_U(V)$ is large.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `variable_residual_band` | **PASS.** Equations (159.HPS8)--(159.HPS10) retain both defect signs, exact quadratic endpoints, empty-component cases, clipping, and strict/closed dyadic sides. |
| `chi4_shifted_zero_mode` | **PASS / TARGET-SAFE.** The exceptional mode is $h=-1$; (159.HPS12)--(159.HPS13) retain $\chi_4$ and prove raw $O(X^\varepsilon)$. |
| `ordinary_ET_second_derivative_capacity` | **PASS.** The complete ledger is (159.HPS16), including its oscillatory discrepancy terms; its feasibility threshold is $M\geq N^{2/3}$. |
| `literal_Vaaler_root_incidence` | **PASS AFTER PROOF-TEXT REPAIR.** The claimed bound (159.HPS2) is valid by the wrap-safe shifted-root identities (159.HPS19), not solely by the same-half formulation of (159.MA31). |
| `literal_J_V_conditions` | **PASS AS ROUTE CONDITIONS.** Equation (159.HPS22) is exactly what makes the displayed unsigned error target-safe. |
| `transformed_pair_power` | **PASS.** Equations (159.HPS23)--(159.HPS26) reproduce $N^{195/796}M^{1295/3184}$ and $M^{1093}\geq N^{780}$. |
| `round158_threshold_reconciliation` | **PASS.** The table in Section 3.3 separates the full ET ledger, literal root ledger, and favorable fixed-boundary $M/J$ model; only the last yields $M^{703}\geq N^{390}$. |
| `stationary_location_phase_self_return` | **PASS IN CONVENTION-INDEPENDENT FORM.** Equations (159.HPS29)--(159.HPS33) verify the carrier and $B$-self-return.  The literal prefactor and eighth-root phase are not promoted here. |
| `incomplete_quadratic_capacity` | **PASS / FAVORABLE MODEL.** Equation (159.HPS35) has raw capacity $N^{1/2}$, conditional on joint BV, and requires $M\geq N^{2/3}$. |
| `source_theorem_common_profile_match` | **NO TARGET MATCH.** Bourgain/TTY are pointwise one-mode tools; Vaaler does not estimate sampled excess; Montgomery--Vaughan has the wrong averaging interface; Huxley is unaudited. |
| `upper_capacity_vs_signed_bound` | **PASS.** Every failed comparison is explicitly route-scoped and is neither a lower bound nor an impossibility theorem. |
| `external_scalar_and_downstream_scope` | **PASS / QUARANTINED.** The $M^{-3/4}$ atom is restored, and the external $B_{1,U}(1)$ seam and every downstream owner remain separate. |

## 6. Dependencies and exact artifacts used

Repository evidence used:

1. `protocol.md`;
2. `state/proof_obligations.yml`, restricted to the active Round 154--159
   obligations and their accepted scope;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/barrier_packet.md`;
5. `proofs/kernels/m9_m1_d1_full_abel_common_profile_recombination.md`;
6. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/reports/full_abel_commutator_attack.md`;
7. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/reports/common_profile_mask_method_audit.md`;
8. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/reports/cell_trace_source_audit.md` and its permitted independent source review
   `rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/reviews/independent_source_round158.md`;
9. `sources/vaaler_1985.md`;
10. `sources/bourgain_2017_exponent_pair.md`;
11. `sources/tao_trudgian_yang_2025.md`;
12. `sources/montgomery_vaughan_1974.md`; and
13. `sources/huxley_2003.md`.

The exact common-profile algebra was treated as the separately reviewed
input requested by this analytic seam.  No web theorem, numerical test, or
symbolic computation was used.

## 7. Recommended state effect

Recommend **revise, with no target or strict-range promotion**.

Revise the proof of the literal Fejer ledger so that the restricted
same-half relation around (159.MA31) is replaced by the circle-exact
shifted-root identities (159.HPS19).  Retain, as candidate evidence, the
target-safe $h=-1$ lemma, the repaired literal incidence ledger, the
checked power arithmetic, and only the convention-independent reciprocal
$B$-process self-return.

Do not promote (159.HPS1), (159.HPS3), or (159.HPS35) as estimates for the
signed target: they are failed capacities of named upper-bound routes.  Do
not reinterpret $M^{1093}\geq N^{780}$, $M\geq N^{2/3}$, or
$M^{703}\geq N^{390}$ as lower bounds, universal barriers, or new
owners.

All three thresholds lie outside $M\leq N^{1/2}$, hence a fortiori give
no new range on the strict open side $M^{449}\ll R^{780}$, with
$R=X^{1/4}$ and $N=\lfloor X\rfloor$.  The accepted
fixed-polylogarithmic defect collar is not enlarged.  Nothing transfers to
$D>1$, $L>1$, another $d,t$ layer, the cross owner, another M1 or M2
component, endpoint uniformity, M9, the bridge, the quarter target, or a
global exponent.  The terminal route label remains
`paired_interior_abel_commutator_no_go` in this strictly method-scoped
sense.
