# Round 150 conductor adjudication

- Campaign: `m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate`
- Starting graph: `b6c5ee5b0d51d347876b389c05c78596c069b190af715d297bd937701ea893b6`
- Decision: promote a strict fixed-wrap range and a scoped large-wrap obstruction
- Terminal label: `strict_moving_coefficient_collar_range`

## 1. Decision

Round 150 proves a genuine strict range, not the complete collar.  The
accepted kernel consists of:

1. the exact low-projective-norm expansion of the arithmetic
   forced/excluded-prime masks in the two-row coefficient;
2. the prefix-uniform norm
   $$
   \sum_L\frac{|B_{d,U}(L)|}{\sqrt L}
   \ll_\varepsilon X^\varepsilon;
   $$
3. an absolute $O_\varepsilon(DQX^\varepsilon)$ bound for every fixed
   centered wrap class, and hence a target-sized packet of
   $O(1+R^2/Q)$ classes;
4. the full actual-profile transformed row when $M=O(1)$; and
5. the exact shifted-factor identity, positivity, fixed-nonzero-shift
   divisor recovery, and the no-go for separately summing those divisor
   bounds over all shifts.

The growing-$M$ large-wrap collar and the growing-$M$ generic
non-collar remain open.  No scalar, M1, M9, bridge, target, or exponent
claim follows.

## 2. Admitted proof kernel

Write $d=\eta m$, where $\eta\in\{1,2\}$ and $m=d_{\mathrm o}$ is
odd squarefree.  For $L_i=t_is_i^2$, expand $a_i\mid t_i$, put
$c_i=t_i/a_i$, and retain the exact $u_i,v_i$ sums and prefix values.
The two-row divisibility masks are exactly

$$
 {\bf1}_{F\mid m}{\bf1}_{(m,P)=1}
 ={\bf1}_{(F,P)=1}\sum_{z\mid P}\mu(z){\bf1}_{Fz\mid m},
$$

where

$$
 F=[a_1u_1,a_2u_2],\qquad
 P=\operatorname{rad}(c_1c_2s_1s_2v_1v_2).
$$

This is an exact projective expansion of the arithmetic incidence
atoms only.  The two literal prefixes and two sampled profiles remain
joint functions of the row and cells; no full-matrix rank claim is
admitted.  Harmonic $u_i$ sums, convergent $v_i^{-2}$ sums after the
$z$-divisor weights, and finite divisor sums give
$O_\varepsilon(X^\varepsilon)$ scalar coefficient norm at fixed
$(L_1,L_2)$.

The accepted closed coefficient bound
$|B_{d,U}(acs^2)|\ll X^\varepsilon/c$ yields

$$
 \sum_{L\ll E}\frac{|B_{d,U}(L)|}{\sqrt L}
 \ll X^\varepsilon
 \sum_{a\mid d_{\mathrm o}}a^{-1/2}
 \sum_{c\ge1}c^{-3/2}
 \sum_{s\le\sqrt E}s^{-1}
 \ll_\varepsilon X^\varepsilon.
$$

This uses only the literal finite support and $0\le\kappa\le1$.

For $q_i=hr_i$, $(r_1,r_2)=1$, put

$$
 \delta=L_1r_2-L_2r_1,\qquad
 \rho=N\delta-khr_1r_2,
$$

with $k$ centered.  Fix $(L_1,L_2,h,k,r_1)$ and set
$S=NL_1-khr_1$, $\alpha=hr_1/D$.  The collar is

$$
 |Sr_2-NL_2r_1|\le\alpha r_2.
$$

If a supported solution exists, then $r_i\asymp L_iQ/h$,
$S\asymp NL_1$, and $\alpha/S\ll Q/(DN)$.  The possible $r_2$ lie
in an interval of length

$$
 \ll\frac{L_2Q^2}{hDN}=\frac{4L_2}{hE}\ll1.
$$

The symmetric argument gives the raw count

$$
 \mathcal N_k(L_1,L_2;h)
 \ll\frac{Q\min(L_1,L_2)}h.
$$

After the literal $1/(L_1L_2)$ weights, the harmonic $h$ sum, and the
half-weight norm, every row costs $QX^\varepsilon$.  Thus every fixed
wrap costs $DQX^\varepsilon$, and any selected packet
$|\mathcal K|\ll1+R^2/Q$ costs

$$
 DQ\left(1+\frac{R^2}{Q}\right)X^\varepsilon
 \ll R^2DX^\varepsilon.
$$

The proof covers $k=0$, both signs of $k$, all $L_i\ll E$, exact common
gcd $h$, even squarefree rows, imprimitive denominators, and
denominators dividing $N$.  Restrictions are dropped only inside an
upper count.  It does not assert that the full collar contains only the
owned number of wraps.

## 3. Bounded-scale and shifted-factor seams

When $M\le M_0$, nonempty support forces $D,E,L=O_{M_0}(1)$ and
$Q\asymp R^2$.  The accepted Round-148 formula is

$$
 \mathscr W_{d,U}(L/q)
 =\mathscr A_{D,E,U}\!\left(d,\frac{4NdL^2}{q^2}\right).
$$

Writing $q=LQy$ makes the sampled $e$-coordinate
$e_0=(dE/D)y^{-2}$.  The explicit Round-148 finite factorization and
derivative ledger give bounded supremum plus total variation: bulk
logarithmic derivatives are $O_j(1)$, radial transitions are
$O_j(M^{j/2})$, cone transitions are $O_j(D^{j/2})$, and only finitely
many owned transitions occur.  A prefix shorter than its transition
collar already has the prior primal owner.

On each allowed residue class modulo $4L$, the phase $NdL/q$ has
one-sign second derivative $\asymp R^{-2}$ over $O(R^2)$ terms.
Van der Corput's second-derivative bound, followed by Abel summation,
gives $O_\varepsilon(RX^\varepsilon)$ per $L$.  The accepted weighted
$\ell^1$ norm therefore proves

$$
 |G_U(d)|\ll_\varepsilon RX^\varepsilon,
 \qquad
 \sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \ll_\varepsilon R^2DX^\varepsilon.
$$

This is a theorem for the actual bounded-$M$ profile.  It is not a
theorem for an arbitrary bounded smooth profile and does not extend to
growing $M$, where the same curvature placement has first term
$RM^{1/4}$.

For the remaining collar, the exact identities are

$$
 (NL_1-khr_1)(NL_2+khr_2)=N^2L_1L_2+kh\rho,
$$

$$
 r_2(NL_1-khr_1)=NL_2r_1+\rho,\qquad
 r_1(NL_2+khr_2)=NL_1r_2-\rho.
$$

Both factors are positive on the collar.  For fixed
$(L_1,L_2,h,k,\rho)$ with $k\ne0$, divisor factorization gives
$O_\varepsilon(X^\varepsilon)$ candidates.  Separately summing all
legal shifts instead gives raw capacity

$$
 \frac{NL_1L_2Q}{D}X^\varepsilon,
$$

which is worse than the trivial $L_1L_2Q^2$ pair capacity by
$N/(DQ)\ge R$.  This rejects the separate absolute per-shift
placement, not the actual signed sum.

## 4. Blind and source reconciliation

The statement-only blind countermodel is accepted with narrow scope.
It constructs a bounded smooth profile whose derivatives and variation
grow with the sample size and which interpolates both $\chi_4$ and the
reciprocal phase.  It proves that pointwise bounded smoothness alone
cannot imply the full collar theorem.  It does not refute the fixed-wrap
absolute count, and it is excluded from the bounded-$M$ actual-profile
edge by the quantitative Round-148 variation ledger.

The primary-source audit is also accepted with narrow scope.  The
Bombieri--Iwaniec double large sieve stops at nonseparable row-cell
coefficients and local cluster forms.  Duke--Friedlander--Iwaniec's
quadratic divisor theorem has smooth product weights, divisor
coefficients, a fixed shift, and an adverse direct specialization at
the present $N^2L_1L_2$ scale.  Bettin--Chandee requires independent
sequences or four separated fixed-determinant weights.  Reuss treats a
pure two-squarefree fixed shift.  None directly estimates the literal
large-wrap sum.  This is a source-applicability result, not an
exhaustive literature impossibility theorem.

The weighted second-derivative source card supplies exactly the
unweighted interval bound; discrete Abel summation proves its
bounded-variation form.  The independent mathematics review supplies
the missing factor-by-factor link from the accepted Round-148 profile
to bounded variation at $M=O(1)$.

## 5. First unproved step

Choose the symmetric owned packet
$\mathcal K=\{k:|k|\le K_0\}$ with
$2K_0+1\ll1+R^2/Q$.  The first remaining collar is the growing-$M$
signed sum with unique centered $k\notin\mathcal K$ and
$0<|\rho|\le hr_1r_2/D$, retaining

$$
 \chi_4(L_1L_2r_1r_2)
 B_{d,U}(L_1)\overline{B_{d,U}(L_2)}
 \mathscr W_{d,U}(L_1/q_1)
 \overline{\mathscr W_{d,U}(L_2/q_2)}
 e\!\left(\frac{d\rho}{hr_1r_2}\right).
$$

The full wrap range has size $N/Q$, a factor $R^2$ larger than the
owned packet.  At $D=1,L_1=L_2=1$, no row average exists and this is
the actual character reciprocal endpoint.  A joint signed wrap
average or a further exact recombination is required.  The growing-$M$
generic non-collar remains a separate open sector.

## 6. Review gate and controls

The terminal review gate is:

- `blind_fixed_wrap_lemma_review.md`: GREEN for the all-$L$ fixed-wrap
  packet, with the full-collar cardinality caveat;
- `independent_conductor_round150_math_review.md`: GREEN for the
  incidence/norm/fixed-wrap kernel and bounded-$M$ actual-profile edge;
- `source_conductor_round150_final.md`: source and scope verdict; and
- the original statement-only countermodel is retained as an
  under-specified-profile control, not an adverse review of the accepted
  actual-profile theorem.

All campaign controls pass for the promoted strict ranges.  The full
shift summation, growing-$M$ $D=1,L=1$ endpoint, and full collar remain
explicitly open.  Raw counts, absolute weighted masses, and signed sums
are never identified.  Exact $\rho=0$ retains its Round-149 owner.

## 7. State effect

Create one reduction recording the exact two-row incidence, half-weight
norm, fixed-wrap packet, and bounded-$M$ row.  Create one obstruction
recording the growing-$M$ large-wrap source and per-shift placement
boundary.  Update the Round-149 compression/energy frontier and the
global lower-radial owner.  Reject only the false inferences identified
in the State Patch.

Leave unchanged M9--M1, M9--M2, endpoint uniformity, M9, the
conditional bridge, the internally proved exponent $1/3$, the audited
external exponent $0.3144831759740614\ldots$, and the quarter target.
