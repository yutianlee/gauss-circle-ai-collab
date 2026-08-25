# Round 139 hostile audit: displacement completion, aliases, and self-return

## 1. Result

**Outcome: `displacement_quadratic_no_go`.**  The prescribed-centre
displacement formula and its rational quadratic core are exact, and the
core does give one nontrivial but strictly local certification.  If

\[
 L_h=c\min\left\{\frac y2,\left(\frac{y^2}{h}\right)^{1/3}\right\}
\tag{1.1}
\]

with fixed sufficiently small \(c>0\), then the part of the literal scalar
with \(0\leq v\leq L_h\) satisfies

\[
 \mathcal F_N^{\rm Tay}\ll_{\varepsilon,V_{\rm low}}R X^\varepsilon
\tag{1.2}
\]

uniformly in every real centre \(X\geq2\), including \(q=0\), \(q=2y\),
both parities of \(y\), and both scalar signs.  This is an exact weighted
quadratic-Gauss estimate: the correction is retained in the coefficient,
not discarded.  The modulus is \(2y\), the complete-sum loss is

\[
 |G|\leq \{2y\,(16h,2y)\}^{1/2}
 \ll \{y(h,y)\}^{1/2},
\tag{1.3}
\]

and the actual \(h^{-1}\) weight makes all gcd cases summable at the
target scale.

This certification cannot be extended to the full literal displacement
range by the proposed quadratic mechanism.  Already at \(q=0\), the exact
correction is

\[
 \mathcal E_{h,0,y}(v)=\frac{hv^3}{y(y-v)},
\tag{1.4}
\]

so the scale in (1.1) is the largest uniform origin-Taylor scale on which
that correction has bounded phase variation.  On the rest of the support
it is a new oscillatory phase, not a slowly varying coefficient.  Exact
quadratic completion then expresses the original sum as the correlation
of the quadratic Gauss transform with the discrete Fourier transform of
\(e(\mathcal E)\).  The transform is invertible.  An \(L^2\), coefficient-
blind, aliaswise, or blockwise modulus returns the \(y^{1+o(1)}\) scalar
capacity; retaining the correlation and inverting returns the original
reciprocal sum.  There is also no complete Salié sum: after parity is
resolved there is an additive quadratic Gauss factor, while the reciprocal
correction remains in a nonperiodic coefficient; in the \(d\)-variable its
denominator is the varying integer \(d\), not one fixed modulus.

The exact stationary alias calculation is the already accepted character-
Poisson family.  Its principal absolute ledger is

\[
 R^{3/2}\log(2X),
\tag{1.5}
\]

not \(R X^\varepsilon\), and taking moduli over its half-integer aliases is
therefore forbidden.  A second Legendre step returns \(Nh/d\).  No full
scalar estimate and no owner-complete estimate of the Round-138 residual
is obtained.

## 2. Exact statement and hypotheses

Let \(e(t)=e^{2\pi i t}\),

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor=y^2+q,\qquad 0\leq q\leq2y.
\tag{2.1}
\]

Use the fixed real smooth literal profile \(V_{\rm low}\), its certified
compact support, and its literal zero extension.  In particular, the
Round-121 support certificate gives a fixed \(\kappa>0\) such that a
nonzero term has

\[
 \frac hd<\frac{\kappa}{R},\qquad h\leq\frac{\kappa y}{R}\ll\sqrt y.
\tag{2.2}
\]

No plateau replacement is used in proving (1.2).  Constants below may
depend on the fixed profile and on \(c\), but not on \(X,y,N,q,h\).

The map

\[
 d\longleftrightarrow v=y-d
\tag{2.3}
\]

is a bijection from \(1\leq d\leq y\) to \(0\leq v<y\).  Put

\[
 \epsilon_y\equiv y-1\pmod2,\qquad \epsilon_y\in\{0,1\}.
\tag{2.4}
\]

The nonzero terms are precisely \(v=\epsilon_y+2n\): \(v\) is even for
odd \(y\), and odd for even \(y\).  For the positive sign the complete
phase is

\[
 \mathcal F_N=
 \sum_{h\geq1}\frac1h\sum_{0\leq v<y}\chi_4(y-v)
 V_{\rm low}\left(\frac{4R^2h^2}{(y-v)^2}\right)
 e\left(h\frac{q+v^2}{y-v}\right).
\]

\[
 \Psi_{h,q,y}(v)
 =h\frac{q+v^2}{y-v}+\frac{y-v-1}{4}.
\tag{2.5}
\]

The negative sign is its complex conjugate.  Define

\[
 Q_{h,q,y}(v)=\frac{hq}{y}+\frac{hv^2}{y}-\frac v4+\frac{y-1}{4},
 \qquad
 E_{h,q,y}(v)=h\frac{v(q+v^2)}{y(y-v)}.
\tag{2.6}
\]

Then \(\Psi=Q+E\) exactly.  Let \(\mathcal F_N^{\rm Tay}\) be the literal
sum restricted to allowed \(v\leq L_h\), with an integer endpoint chosen
by a floor, and let \(\mathcal F_N^{\rm tail}\) be its exact complement.
The certified statement is

\[
 \mathcal F_N=\mathcal F_N^{\rm Tay}+\mathcal F_N^{\rm tail},\qquad
 |\mathcal F_N^{\rm Tay}|\ll_\varepsilon R X^\varepsilon.
\tag{2.7}
\]

Thus the full scalar target is logically equivalent, after changing the
constant and renaming \(\varepsilon\), to the same target for
\(\mathcal F_N^{\rm tail}\).  Equation (2.7) is **not** a deletion from
the Round-138 square residual: a displacement cutoff splits the lift sum
inside a reduced Farey coefficient, and the small--tail cross owner is
not bounded by (2.7).

The no-go statement is deliberately scoped.  It rules out a proof that
uses only the exact core (2.6), evaluation or square-root bounds for its
complete quadratic Gauss sums, and coefficient-blind Fourier/BV/\(L^2\)
or aliaswise moduli.  It does not assert that no new signed theorem for
the exact correction spectrum or for the joint \((h,v)\)-sum can exist.

## 3. Proof or derivation

**Dictionary and exact Taylor algebra.**  Since

\[
 y^2\leq X<(y+1)^2
 \quad\Longrightarrow\quad
 y^2\leq N\leq y^2+2y,
\]

the range \(0\leq q\leq2y\) is exact.  Moreover, since

\[
 (y-v)(y+v)=y^2-v^2,
\]

one has in both directions

\[
 \frac{N}{y-v}=y+v+\frac{q+v^2}{y-v}.
\tag{3.1}
\]

The discarded contribution \(h(y+v)\) is an integer.  For odd
\(d=y-v\),

\[
 \chi_4(d)=e\left(\frac{d-1}{4}\right),
\tag{3.2}
\]

while even \(d\) vanish.  Equations (3.1)--(3.2) prove (2.5), with no
floor, sign, or parity loss.  Expanding only one reciprocal factor gives
the advertised exact core identity

\[
 \frac{q+v^2}{y-v}
 =\frac qy+\frac{v^2}{y}
  +\frac{v(q+v^2)}{y(y-v)}.
\tag{3.3}
\]

For comparison, the true second-order Taylor polynomial at \(v=0\) has
the exact remainder formula

\[
 \frac{q+v^2}{y-v}
 =\frac qy+\frac{qv}{y^2}+\frac{Nv^2}{y^3}
  +\frac{Nv^3}{y^3(y-v)}.
\tag{3.4}
\]

Thus moving the \(q\)-dependent linear drift into a quadratic Taylor core
does not remove the cubic scale.  It also loses the uniform modulus \(y\):
for example, if \(q=1\), \(y\) is an odd prime, and \(y\nmid h\), the
quadratic coefficient \(hN/y^3\) in (3.4) has denominator \(y^3\).
Consequently (3.4) supplies no exact modulus-\(y\), \(q\)-uniform Gauss
sum.

The correction is convex and increasing.  Direct differentiation gives

\[
 E'(v)=\frac{h\{qy+3yv^2-2v^3\}}{y(y-v)^2}\geq0,
\tag{3.5}
\]

and, with \(d=y-v\),

\[
 \Psi'(v)=h\left(\frac N{d^2}-1\right)-\frac14,
 \qquad
 \Psi''(v)=\frac{2hN}{d^3},
 \qquad
 E''(v)=2h\left(\frac N{d^3}-\frac1y\right)\geq0.
\tag{3.6}
\]

For \(v\leq y/2\), \(q\leq2y\), and \(L_h\) as in (1.1),

\[
 0\leq E(v)
 \leq \frac{2hv(2y+v^2)}{y^2}
 \leq \frac{4hv}{y}+\frac{2hv^3}{y^2}.
\tag{3.7}
\]

At \(v=L_h\), (2.2) makes the first term \(O(c)\), and the second is
\(O(c^3)\).  Hence \(E\) has bounded total phase variation on the Taylor
window, uniformly in \(q\).  Conversely, at \(q=0\),

\[
 \frac{hv^3}{y^2}\leq E(v)\leq\frac{2hv^3}{y^2}
 \qquad(0\leq v\leq y/2).
\tag{3.8}
\]

The origin-Taylor correction is therefore uniformly \(O(1)\) only for
\(v\ll(y^2/h)^{1/3}\).  This is an exact fourth-power obstruction, not a
heuristic order symbol.

**Exact quadratic completion on the certified window.**  Write
\(v=\epsilon_y+2n\), set \(M=2y\), and zero-extend

\[
 w_h(n)={\bf1}_{0\leq v\leq L_h}
 V_{\rm low}\left(\frac{4R^2h^2}{(y-v)^2}\right)e(E_{h,q,y}(v))
\tag{3.9}
\]

to \(\mathbb Z/M\mathbb Z\).  The cutoff endpoints are part of this
definition.  Since the profile argument is monotone in \(v\), the total
variation of the profile factor is bounded by the fixed one-dimensional
variation of \(V_{\rm low}\).  Equations (3.5) and (3.7) give

\[
 \|w_h\|_\infty+\operatorname{Var}_{\mathbb Z/M\mathbb Z}(w_h)\ll1.
\tag{3.10}
\]

Apart from a unit constant, the core on this parity lattice is

\[
 e\left(\frac{8hn^2+(8h\epsilon_y-y)n}{2y}\right).
\tag{3.11}
\]

For

\[
 \widehat w_h(k)=\sum_{n\bmod M}w_h(n)e(-kn/M),
 \quad
 G_M(A,C)=\sum_{n\bmod M}e((An^2+Cn)/M),
\tag{3.12}
\]

finite Fourier inversion gives the exact identity

\[
 S_h^{\rm Tay}
 =\frac{e(C_h)}M\sum_{k\bmod M}\widehat w_h(k)
 G_M(8h,8h\epsilon_y-y+k),
\tag{3.13}
\]

where \(C_h=hq/y+(y-1)/4+h\epsilon_y^2/y-\epsilon_y/4\).
No coprimality has been assumed.  Squaring a complete Gauss sum and
putting \(u=n-n'\) gives

\[
 |G_M(A,C)|^2
 \leq M\#\{u\bmod M:M\mid2Au\}
 =M(2A,M).
\tag{3.14}
\]

Thus every vanishing and nonvanishing gcd case is safely covered by

\[
 |G_M(8h,C)|\leq\{2y(16h,2y)\}^{1/2}
 \ll\{y(h,y)\}^{1/2}.
\tag{3.15}
\]

The possible extra vanishing when the linear coefficient is inadmissible
cannot be used uniformly, because \(k\) runs through all residue classes
and no distribution theorem for \(\widehat w_h(k)\) in the admissible
classes is available.

Discrete summation by parts and (3.10) give

\[
 \frac1M\sum_{k\bmod M}|\widehat w_h(k)|\ll\log(2y).
\tag{3.16}
\]

Indeed the zero frequency costs \(O(1)\), while for \(1\leq |k|\leq M/2\),

\[
 |\widehat w_h(k)|
 \leq \frac{\operatorname{Var}(w_h)}{|1-e(k/M)|}
 \ll\frac{M}{|k|}.
\]

Combining (3.13), (3.15), and (3.16),

\[
 |S_h^{\rm Tay}|\ll\{y(h,y)\}^{1/2}\log(2y).
\tag{3.17}
\]

Finally,

\[
 \begin{aligned}
 \sum_{h\ll\sqrt y}\frac{(h,y)^{1/2}}h
 &\leq \sum_{d\mid y}d^{1/2}
       \sum_{\substack{h\ll\sqrt y\\d\mid h}}\frac1h  \\
 &\ll \log(2y)\sum_{d\mid y}d^{-1/2}
 \ll_\varepsilon y^\varepsilon.
 \end{aligned}
\tag{3.18}
\]

Equations (3.17)--(3.18), together with \(\sqrt y\leq R\), prove (1.2).
This calculation retains the actual \(h^{-1}\) weight; a false uniform
per-\(h\) coprime Gauss bound is not being used.

**Why full completion is an invertible return.**  Formula (3.13) remains
an exact identity on the whole literal support if the Taylor cutoff is
removed, but (3.10) then fails.  On a \(q=0\) profile plateau extending
to \(d\asymp Rh\), (1.4) reaches order \(R^3\); its continuous BV cost is
of that order.  More invariantly, Parseval gives

\[
 \sum_k|\widehat w_h(k)|^2=M\sum_n|w_h(n)|^2,
 \qquad
 \sum_k|G_M(8h,B+k)|^2=M^2.
\tag{3.19}
\]

Consequently coefficient-blind Cauchy in (3.13) gives only

\[
 |S_h|\leq M^{1/2}\|w_h\|_2\asymp y
\tag{3.20}
\]

on a full active interval.  For \(H\leq h<2H\), the \(H\) values of \(h\)
and the factor \(h^{-1}\asymp H^{-1}\) leave capacity \(y\) for each
dyadic height block, against target \(R=\sqrt y+O(y^{-1/2})\).  Expanding
\(\widehat w_h\) in (3.13) and using orthogonality in \(k\) recovers the
original \(n\)-sum term by term.  Thus preserving its direction is exact
self-return; taking its modulus is the capacity loss.  Any useful
continuation would have to prove a new signed correlation estimate for
\(\widehat{e(E)}\) against the admissible Gauss phases.  That estimate is
not supplied by Gauss evaluation itself.

There is likewise no Salié completion hidden here.  In (3.13) the
complete object is an ordinary additive quadratic Gauss sum.  The factor
containing \(q\), \(y-v\), the literal profile, and the hard interval is
\(w_h\), with no fixed-modulus unit inverse.  In the original variable
\(d=y-v\), \(e(Nh/d)\) has the varying denominator \(d\); the conductor-
four character alone cannot turn these varying rational phases into a
complete Salié sum of one growing modulus.

**Stationary aliases, boundaries, and Poisson capacity.**  On the parity
lattice the exact phase derivative is

\[
 \frac{d}{dn}\Psi(\epsilon_y+2n)
 =2h\left(\frac N{d^2}-1\right)-\frac12.
\tag{3.21}
\]

The alias \(k\in\mathbb Z\) is stationary precisely when

\[
 d_*=2\sqrt{\frac{Nh}{r}},\qquad r=4h+2k+1>0,
\tag{3.22}
\]

so \(r\) runs over the positive odd integers.  For the quadratic core
alone the corresponding condition is

\[
 \frac{4hv}{y}-\frac12=k,
 \qquad
 v_k^{\rm core}=\frac{y(2k+1)}{8h}.
\tag{3.23}
\]

These are exactly the half-integer stationary aliases.  The correction
is what moves (3.23) to (3.22); it cannot be dropped on the terminal
range.

The complete character-Poisson identity for
\(a_h(x)=h^{-1}V_{\rm low}(4R^2h^2/x^2)\) is

\[
 \begin{aligned}
 \sum_{d\leq y}\chi_4(d)a_h(d)e(Nh/d)
 ={}&\frac12\chi_4(y)a_h(y)e(Nh/y)\\
 &+\frac1{2i}\sum_{\sigma=\pm1}\sigma
 \lim_{K\to\infty}\sum_{|j|\leq K}
 \int_0^y a_h(x)
 e\left(\frac{Nh}{x}+(\sigma/4-j)x\right)\,dx.
 \end{aligned}
\tag{3.24}
\]

The endpoint vanishes when \(y\) is even and otherwise must remain; its
full \(h\)-sum is \(O(\log(2X))\).  For an interior stationary mode
\(r=\sigma-4j>0\), (3.22) gives the accepted principal factor

\[
 e(-1/8)N^{1/4}\chi_4(r)(hr)^{-3/4}
 V_{\rm low}(R^2hr/N)e(\sqrt{Nhr}).
\tag{3.25}
\]

The support has \(r\gg h\), \(hr\ll y\), and hence

\[
 N^{1/4}\sum_{h\ll R}h^{-3/4}
 \sum_{h\ll r\ll y/h}r^{-3/4}
 \ll R^{3/2}\log(2X).
\tag{3.26}
\]

This is the same excess capacity exposed by half-integer tube moduli.
Formula (3.25) is not (3.24): the hard endpoint, incomplete-Fresnel
stationary entry and exit, nonstationary modes, profile crossings,
remainders, small heights, both branches, and the opposite sign remain
separate owners.  A second stationary/Legendre step sends the phase back
to \(Nh/d\), so it is another exact self-return unless a new signed
\((h,r)\)-estimate is proved.

**Round-138 directionality.**  If \(h=ag\), \(d=bg\), then a displacement
condition is

\[
 y-bg\leq L_{ag}.
\tag{3.27}
\]

It depends on the lift \(g\) and therefore splits the exact lift aggregate
\(L_\chi(y/b)\) inside \(c_{a,b}\).  Moreover, after writing
\(\mathcal F_N=\mathcal F_N^{\rm Tay}+\mathcal F_N^{\rm tail}\), the
cross term

\[
 2\Re\bigl(\mathcal F_N^{\rm Tay}
            \overline{\mathcal F_N^{\rm tail}}\bigr)
\tag{3.28}
\]

is not target-square bounded from (1.2), because no target bound for the
tail is known.  Filtering (3.28) by the two Round-138 carrier collars is
not a positive sub-square.  Thus (1.2) gives a scalar-level equivalence,
but it deletes no owner from the exact residual
\(\mathcal R_{y^{-2}}\).  Applying a modulus before lift aggregation or
before (3.28) loses precisely the direction that Round 138 preserves.

## 4. First doubtful or unproved step

The first unproved analytic step is not the displacement identity or the
Gauss sum.  It is an owner-complete signed estimate for the correction
spectrum on \(v>L_h\).  In the exact completion notation it would have to
control, uniformly in \(q\),

\[
 \sum_{h\ll R}\frac1{2yh}
 \sum_{k\bmod 2y}\widehat w_h(k)
 G_{2y}(8h,8h\epsilon_y-y+k)
 \ll_\varepsilon R X^\varepsilon,
\tag{4.1}
\]

with the full literal \(w_h\), or prove an equally strong joint estimate
after exact Poisson.  Taking absolute values in \(k\), in \(h\), in
stationary aliases, or in displacement blocks does not prove (4.1);
Parseval gives (3.20), while principal alias moduli give (3.26).  Keeping
all phases but applying inverse Fourier summation reconstructs the
original reciprocal scalar.

Even a proof of (4.1) for an isolated pre-lift component would still have
to be transported through (3.27)--(3.28) to the exact Round-138 residual.
No such transport estimate is available.  This is the first legal place
for a genuinely noninvertible theorem: it must use the actual joint
direction of the correction coefficients and Gauss/alias phases, be
uniform at \(q=0\) and \(q=2y\), retain all boundaries, and return the
complete \(R\)-power ledger.  Merely naming Weyl, Gauss, Salié, or Poisson
does not supply it.

## 5. Required controls and outcomes

- `exact_N_y2_q_and_displacement_bijection` — **pass**.  Equations
  (2.1), (2.3), and (3.1) are bidirectional; \(v=y\) and \(d=0\) never
  enter.

- `literal_profile_support_zero_extension_and_both_signs` — **pass for
  the certified window, red as a global gain**.  The support implication
  (2.2), profile variation, sharp \(v=0\) endpoint, artificial Taylor
  endpoint, literal zero extension, and conjugate sign are retained.

- `physical_mod_four_carrier_and_y_parity` — **pass**.  Even \(d\) vanish;
  \(v=\epsilon_y+2n\), and the carrier \(-v/4+(y-1)/4\) produces the
  linear coefficient \(8h\epsilon_y-y\) modulo \(2y\).  No parity of
  \(y\) is suppressed.

- `exact_quadratic_core_and_Taylor_correction` — **pass locally, no-go
  globally**.  Equations (3.3)--(3.8) retain both the prescribed core and
  the true second-order Taylor alternative.  At \(q=0\) the cubic scale
  in (1.1) is sharp for bounded correction variation; for generic
  \(q=1\), the true Taylor quadratic has natural denominator \(y^3\), not
  \(y\).

- `small_v_and_terminal_v_boundaries` — **pass as an owner audit**.  The
  small-\(v\) hard boundary is included in (3.9); the terminal active
  range is \(d\gg Rh\), not \(v=y\).  Profile exits, artificial partitions,
  and incomplete-Fresnel crossings cannot be discarded.

- `dyadic_h_v_capacity_ledger` — **red for completion of the full
  scalar**.  A dyadic \(h\asymp H\) block has absolute displacement
  capacity \(y\).  The Taylor piece is \(R X^{o(1)}\) by (3.17)--(3.18),
  but coefficient-blind full completion returns \(y\), and stationary
  alias moduli return \(R^{3/2}X^{o(1)}\).

- `quadratic_Gauss_Salie_completion_cost` — **pass for the exact cost,
  red for the claimed saving**.  The modulus is \(2y\), the gcd is
  \((16h,2y)\), and (3.13) includes every Fourier mode.  There is no
  growing-modulus Salié unit sum; the reciprocal correction remains in
  the coefficient.

- `stationary_alias_and_half_integer_tubes` — **pass as a no-go**.
  Equations (3.22)--(3.23) identify the exact aliases and their core
  half-integer approximations.  Aliaswise modulus is prohibited by
  (3.26) and by the accepted \(R^{3/2}\) paired-tube control.

- `q_zero_q_max_and_real_centre_uniformity` — **pass**.  For \(q=0\),
  (1.4) proves the cubic obstruction.  For \(q=2y\), (3.7) remains
  uniform and the \(v=0\) reciprocal phase contributes \(e(2h)=1\)
  whenever the parity carrier is nonzero.  Since
  \(y\leq R^2<y+1\), all profile and power estimates are uniform as real
  \(X\) moves inside a floor interval.

- Fourth-power control — **pass with restricted meaning**.  If
  \(X=N=M^4\) with odd \(M\), then \(R=M\), \(y=M^2\), \(q=0\), and the
  literal packet \(h=1\), \(v=4u\), \(1\leq u\leq cR\), has phase
  \(e(16u^2/(y-4u))\), character \(+1\), and target-scale coherent
  capacity \(\asymp R\) for small fixed \(c\).  It shows sharpness of the
  local target but is not a lower bound for the full scalar; exterior
  terms may cancel.  Even fourth powers are covered by the parity-lattice
  calculation, although this particular constant-character packet uses
  odd \(M\).

- `map_back_to_round138_exact_residual` — **red as an owner deletion**.
  Equations (3.27)--(3.28) show the split lift coefficient and uncontrolled
  cross owner.  The only valid conclusion is the scalar-level equivalence
  in (2.7); no part of \(\mathcal R_{y^{-2}}\) is estimated.

- `noninvertibility_directionality_and_self_return` — **red for the
  proposed mechanism**.  Exact DFT completion and the second Legendre
  step are invertible.  Moduli lose direction and return excess capacity;
  inversion returns the starting scalar.

- `lower_GAR_and_downstream_scope` — **pass as a scope restriction**.
  No lower-radial signed estimate, lower GAR, direct blockwise M1 parent,
  M9-M1, M2 parent, endpoint-uniformity owner, M9, quarter theorem, or
  exponent follows.

## 6. Dependencies and exact artifacts used

This audit used only the assigned brief and the permitted context:

- `rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/briefs/displacement_completion_hostile_audit.md`;
- `protocol.md`;
- `state/proof_obligations.yml`, in particular
  `M9-M1-global-lower-radial-signed-estimate`,
  `M9-M1-lower-radial-flat-discrepancy-equivalence`,
  `M9-M1-lower-mod-four-resonance-tubewise-no-go`,
  `M9-M1-lower-signed-farey-row-resonance-reduction`, and
  `M9-M1-lower-signed-farey-transform-radical-obstruction`;
- `state/active_campaign.yml`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/synthesis.md`;
- `rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/candidates/conductor_round138_scalar_rows_and_resonance_fibres.md`;
- `rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/reviews/hostile_post_unmask_owner_and_capacity_audit.md`;
- `rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/synthesis.md`;
- `rounds/codex-managed/m9-m1-lower-denominator-displacement-quadratic-gate/blind_statement.md`.

No Round-139 sibling report, numerical or symbolic experiment, web
result, arbitrary coefficient theorem, centre average, or desired circle
estimate was used.  The argument is entirely analytic.

## 7. Recommended state effect

Close Round 139's hostile seam under `displacement_quadratic_no_go`.
Retain (2.7), with proof (3.9)--(3.18), as a scoped exact certification
of the maximal uniform origin-Taylor/Gauss window.  Retain (3.13),
(3.19)--(3.20), the exact alias dictionary (3.21)--(3.23), and the
Round-138 Poisson ledger as obstruction controls.  Do not describe the
Taylor-window estimate as a deletion from the Round-138 residual and do
not promote a Salié, Weyl, or full quadratic-completion bound.

The first open target remains

\[
 |\mathcal R_{y^{-2}}|\ll_\varepsilon yX^\varepsilon,
\]

equivalently the full scalar bound
\(|\mathcal F_N|\ll_\varepsilon R X^\varepsilon\).  Keep the lower-radial
signed estimate, lower GAR, both direct M1 parents, M9-M1, all M2 parents,
endpoint uniformity, M9, the quarter theorem, and both global exponents
open.  No shared proof state should change except through a conductor-
validated State Patch.
