# Round 80 blind strict-metric energy rederivation

## 1. Result

**Exact complete-coefficient centering cancellation and route-level no-go.**
For

\[
 \theta=\frac{\Lambda}{k},
 \qquad
 \mathfrak C^°_{a,b,k}(g)
 :=e(-g\theta/2)\mathfrak B^°_{a,b,k}(g),
\]

the actual coefficient formula (80.2) gives the exact identity

\[
 \mathfrak C^°_{a,b,k}(g)
 =g\int_{b/4}^{a}A^°_{ga,gb}(gu)
   e\!\left(g[-J\delta\sqrt u+ku]\right)\,du.        \tag{R80.1}
\]

Thus, when \(\theta=\ell+\eta\) and \(g\) is odd,

\[
 (-1)^{q+\ell}\mathfrak B^°(g)e(-g\eta/2)
 =(-1)^q\mathfrak C^°(g).                       \tag{R80.2}
\]

In particular, the nearest-integer sign \((-1)^\ell=(-1)^{p/k}\)
does not survive as an independent sign of the complete actual-symbol
summand.  It cancels exactly against the centered constant
\(X\delta^2/(4k)=\theta/2\) inside \(\mathfrak B^°\).  Product-fiber
quotient parity therefore cannot by itself close the strict-metric sum.

The same cancellation defeats the apparent half-integer Fourier gap.  An
integer window mode seems to have frequency \(r-g/2\), which is nonzero for
odd \(g\), but the moving complete coefficient satisfies
\(\mathfrak B^°(g)=e(g\theta/2)\mathfrak C^°(g)\); hence

\[
 \mathfrak B^°(g)e((r-g/2)\theta)
 =\mathfrak C^°(g)e(r\theta).                   \tag{R80.3}
\]

The integer zero mode \(r=0\), and therefore the ordinary density term,
is restored exactly.  Reindexing odd lifts without moving the complete
coefficient is unlawful; moving it gives (R80.3), support endpoints, and no
second frequency separation.

Quantitatively, put

\[
 \rho:=\frac{AJD^3}{L^3}.
\]

The accepted Abel and incidence estimates still give only

\[
 |\mathcal S^{\rm hard}_{A,D,K,G,R}|
 \ll_\varepsilon X^\varepsilon
 A\sqrt G\sqrt J D^{3/2}
 \asymp X^\varepsilon L^2\sqrt\rho .                 \tag{R80.4}
\]

This closes the target only on the boundary range \(\rho=O(1)\), already
belonging to the positive-safe transition up to fixed dyadic constants.  It
does not close any range in which \(\rho\) is unbounded.  The exact
centering cancellation is a rigorous no-go for a proof based on the literal
quotient sign or the odd-lift half-integer Fourier gap.  It is not a
counterexample to (80.14): cancellation could still come from
\((-1)^q\), the oscillatory integral (R80.1), or a new correlation of those
complete decentered symbols across distinct primitive rays.

## 2. Exact statement and hypotheses

Assume only the normalization, exclusions, identities, and estimates in the
derivation packet.  Fix a residual dyadic block

\[
 a\asymp A,\quad b-a\asymp D,\quad k\asymp K,\quad
 G_{a,b}\asymp G,
 \qquad
 K\asymp\frac{JD}{A},\quad G\asymp\frac LA,
\]

with \(AJD^3\gg L^3\), and a punctured strict-metric piece

\[
 0<c_1/R\leq |\eta|\leq c_2/R<1/2,
 \qquad R\leq N_{a,b}\ll G.
\]

Let \(\mathscr T_R\) be its residual tuples \(t=(a,b,k)\), with the fixed
smooth dyadic weights understood, and define \(\mathfrak C_t^°\) by
(R80.1).  Then:

1. The literal hard sum has the exact complete-symbol form
   \[
   \boxed{
   \mathcal S^{\rm hard}_{A,D,K,G,R}
   =\sum_{t\in\mathscr T_R}(-1)^{q_t}
      \sum_{g\in\mathcal G_t}\mathfrak C_t^°(g).}
                                                               \tag{R80.5}
   \]
   The metric condition still selects \(\mathscr T_R\), but neither
   \(\ell_t\), \(p_t/k_t\), nor \(\eta_t\) occurs as a separate phase in
   the summand after the complete coefficient is retained.

2. For a period-one window \(W_R\), the exact Fourier decomposition is
   \[
   \begin{aligned}
   &W_R(\theta_t)(-1)^{q_t}
     \sum_g\mathfrak B_t^°(g)e(-g\theta_t/2)\\
   &\quad=(-1)^{q_t}\sum_g\mathfrak C_t^°(g)
      \left(\mu_R+
       \sum_{r\ne0}\widehat W_R(r)e(r\theta_t)\right).
   \end{aligned}                                           \tag{R80.6}
   \]
   Hence the density term is exactly
   \(\mu_R(-1)^{q_t}\sum_g\mathfrak C_t^°(g)\); it is not removed by
   oddness of \(g\).

3. Estimate (R80.4) follows from the accepted inputs.  Therefore any
   density-saturating block with \(\rho\) unbounded needs an additional
   saving of order \(\rho^{-1/2}\), jointly over density and discrepancy.

4. The step-two variation theorem (80.5) is a theorem for
   \(\mathfrak B^°\), not for \(\mathfrak C^°\).  Formally,
   \[
   \partial_g\mathfrak C^°(g)
   =e(-g\theta/2)
     \bigl(\partial_g\mathfrak B^°(g)
            -\pi i\theta\mathfrak B^°(g)\bigr),          \tag{R80.7}
   \]
   so (80.5) does not furnish a useful step-two variation bound for the
   decentered coefficient when \(|\theta|\) is large.  Such a bound may not
   be inserted after (R80.5).

5. A coefficient-uniform saving over (R80.4) is false.  To see this without
   making an actual-symbol claim, write
   \(M_t=J\delta_t\sqrt G/K^{3/2}\),
   \(\sigma_t=(-1)^{q_t+\ell_t}\), and, on any permitted full-size lift
   support with \(g\ll G\) and \(|\mathcal G_t|\geq cG\), take the proxy
   \[
   B_t^{\rm adv}(g)
   =\sigma_t M_t\frac RG e(g\eta_t/2).                \tag{R80.8}
   \]
   It satisfies
   \(|B_t^{\rm adv}|+g|\partial_gB_t^{\rm adv}|\ll M_t\), but
   \[
   \sigma_t\sum_{g\in\mathcal G_t}
      B_t^{\rm adv}(g)e(-g\eta_t/2)
   =M_t\frac RG|\mathcal G_t|\geq cM_tR.             \tag{R80.9}
   \]
   On odd lifts its decentered value is exactly
   \(e(-g\theta_t/2)B_t^{\rm adv}(g)=(-1)^{q_t}M_tR/G\).
   This proxy only falsifies an inference from (80.5); it is not asserted to
   arise from the actual amplitude \(A^°\).

## 3. Proof or derivation

Because \(g=2n+1\), the phases in (80.3) combine without approximation:

\[
 e\!\left(\frac q2-\frac{\Lambda}{2k}\right)e(-n\Lambda/k)
 =(-1)^q e(-g\Lambda/(2k))
 =(-1)^q e(-g\theta/2).                              \tag{R80.10}
\]

The constant term in the phase defining (80.2) is

\[
 \frac{X\delta^2}{4k}
 =\frac1{2k}\frac{X\delta^2}{2}
 =\frac{\Lambda}{2k}
 =\frac\theta2.
\]

Multiplying (80.2) by the final factor in (R80.10) cancels that constant
pointwise in every \((a,b,k,g,u)\), proving (R80.1).  This operation changes
neither integration endpoint, collar, profile, floor, star, nor saddle
transition.

Now write \(\theta=\ell+\eta\).  Since \(g\) is odd,

\[
 e(-g\ell/2)=(-1)^\ell.
\]

Therefore

\[
 (-1)^{q+\ell}\mathfrak B^°(g)e(-g\eta/2)
 =(-1)^q\mathfrak B^°(g)e(-g\theta/2)
 =(-1)^q\mathfrak C^°(g),
\]

which proves (R80.2) and (R80.5).  Equivalently, on the product fiber
\(p=\ell k\),

\[
 \mathfrak B^°(g)
 =e(g\theta/2)\mathfrak C^°(g)
 =(-1)^{p/k}e(g\eta/2)\mathfrak C^°(g),
\]

so the two quotient signs multiply to one:

\[
 (-1)^{q+p/k}\mathfrak B^°(g)e(-g\eta/2)
 =(-1)^q\mathfrak C^°(g).                       \tag{R80.11}
\]

The product-fiber constraint remains exact:

\[
 p=\ell k,\qquad k\mid p,
 \qquad |\Lambda-p|=k|\eta|\asymp K/R.
\]

It is only the proposed quotient-parity cancellation that disappears.
For completeness, if \(p=2^vm\), \(m\) odd, and \(k=2^wd\mid p\), then

\[
 (-1)^{p/k}=
 \begin{cases}
 +1,&w<v,\\
 -1,&w=v.
 \end{cases}                                         \tag{R80.12}
\]

Thus quotient parity was not a uniformly balanced divisor character even
before (R80.11); for odd \(p\) it is constant.  After (R80.11), it is absent
altogether.

To prove the Fourier identity, expand \(W_R\) by (80.17).  Before using the
complete coefficient, the mode multiplying the lift phase is
\(e((r-g/2)\theta)\), and \(r-g/2\ne0\) for integer \(r\) and odd \(g\).
But (80.2) factors exactly as
\(\mathfrak B^°(g)=e(g\theta/2)\mathfrak C^°(g)\).  This proves
(R80.3) mode by mode, including \(r=0\), and summing the modes proves
(R80.6).  Hence the half-integer observation applies only after freezing a
coefficient which in fact moves by the cancelling half-integer phase.

For the quantitative bound, use

\[
 \delta=\frac{b-a}{\sqrt b+\sqrt a}\asymp\frac D{\sqrt A}
\]

and \(K\asymp JD/A\) to obtain

\[
 M_t=\frac{J\delta_t\sqrt G}{K^{3/2}}
 \asymp\frac{A\sqrt G}{\sqrt J\sqrt D}.              \tag{R80.13}
\]

The accepted pointwise Abel estimate (80.15), which remains valid under the
exact rewriting (R80.2), is \(O_\varepsilon(X^\varepsilon M_tR)\).
The strict-metric incidence count (80.8) is
\(O_\varepsilon(X^\varepsilon ADK/R)\).  Their product is

\[
 ADK M_t
 \asymp A\sqrt G\sqrt J D^{3/2}.
\]

Since \(G\asymp L/A\), this equals

\[
 \sqrt{ALJD^3}
 =L^2\sqrt{AJD^3/L^3}=L^2\sqrt\rho,
\]

proving (R80.4).  The ordinary \(1/R\) density has exactly canceled the
Abel \(R\), and (R80.6) shows why discarding the density mode is not lawful.

Finally, (R80.8) obeys the proxy variation bound because \(R\leq G\),
\(|\eta_t|\asymp1/R\), and \(g\ll G\):

\[
 |B_t^{\rm adv}(g)|\leq M_t,
 \qquad
 g|\partial_gB_t^{\rm adv}(g)|
 \ll gM_t\frac RG|\eta_t|\ll M_t.
\]

The two displayed phases cancel exactly, proving (R80.9).  It follows that
step-two variation plus parity admits rank-one aligned rows at the full Abel
scale.  Reciprocal re-enumeration
\((k,\ell)\leftrightarrow(k,p=\ell k)\) is bijective and returns the same
rows, the same metric thickness, and, by (R80.11), no residual quotient
character.  It therefore supplies no independent saving.

## 4. First doubtful or unproved step

For the quotient-parity or half-integer-gap proposal, the first false step is
treating \(\mathfrak B^°(g)\) as a fixed coefficient while extracting
the phase \(e(-g\theta/2)\).  The complete coefficient contains the exact
opposite phase \(e(g\theta/2)\).  Once it is retained, (R80.11) removes
\((-1)^{p/k}\), and (R80.3) restores the Fourier zero mode.

For any alternative route after this correction, the first genuinely
unproved step is a correlation estimate for the decentered actual symbols
(R80.1).  On a density-saturating block with \(\rho\) unbounded, one needs
schematically

\[
 \left|\sum_{t\in\mathscr T_R}(-1)^{q_t}
       \sum_{g\in\mathcal G_t}\mathfrak C_t^°(g)\right|
 \ll_\varepsilon X^\varepsilon\rho^{-1/2}
       \sum_{t\in\mathscr T_R}M_tR,                  \tag{R80.14}
\]

or a joint density-discrepancy theorem of equivalent strength.  The packet
contains no variation or orthogonality theorem for
\(\mathfrak C^°_{a,b,k}\) as \((a,b,k)\) varies, and (R80.7) prevents
one from transferring the accepted lift variation mechanically.  The
complete oscillatory integral must therefore be analyzed anew; neither
fiber parity nor Fourier reindexing proves (R80.14).

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `external_normalization` | Passed.  Used \(J=\sqrt X\), \(K\asymp JD/A\), and \(G\asymp L/A\).  The aggregate's outer \(2\Re\) and accepted error occur once, outside the block analysis. |
| `round78_round79_exclusions` | Passed.  Primitive square rays, exact nonsquare centers, positive-safe blocks, and the accepted endpoint/collar error are never used as hard examples or counted again. |
| `primitive_parity` | Passed.  The only surviving explicit sign after (R80.2) is \((-1)^q\).  In the hostile near-square range \(D=2\), \(q=1\) is constant. |
| `combined_odd_lift_phase` | Passed by (R80.10), before any nearest-integer reduction. |
| `nearest_integer_sign` | Passed and neutralized lawfully: the literal \((-1)^{q+\ell}\) is first retained and then canceled by the exact centered constant of the complete coefficient in (R80.2). |
| `strict_metric_one_count` | Passed.  Unique nearest \(\ell\), the fixed tie convention, \(p=\ell k\), and \(|\Lambda-p|\asymp K/R\) are retained.  The metric window remains in the tuple set after phase cancellation. |
| `density_and_discrepancy` | Passed as an obstruction.  Formula (R80.6) retains both \(\mu_R\asymp1/R\) and all centered modes; the apparent half-integer gap does not remove the density term. |
| `complete_actual_coefficient` | Passed centrally.  Identity (R80.1) uses the full coefficient and exposes the exact phase that invalidates a frozen-coefficient Fourier or quotient-parity argument. |
| `lift_support_and_step_two_variation` | Passed.  Variation is used only for \(\mathfrak B^°\), never transferred to \(\mathfrak C^°\) through (R80.7).  Any mode reindexing must still translate the finite odd support and retain both endpoints. |
| `fiber_product_parity` | Passed.  The exact sign \((-1)^{q+p/k}\) is retained on the fiber, then its quotient factor cancels exactly as in (R80.11).  Formula (R80.12) also shows it is not intrinsically balanced. |
| `safe_block_boundary` | Passed.  The positive capacity is exactly \(L^2\sqrt\rho\); only \(\rho=O(1)\) is target-sized without new cancellation. |
| `near_square_and_Pell` | Passed.  For \(s^2-3t^2=-2\), \((a,b)=(s^2,3t^2)\) is primitive odd, has \(b=a+2\), \(q=1\), and \(ab=3(st)^2\) nonsquare.  Under \((s,t)\mapsto(2s+3t,s+2t)\), \(\delta=2/(s+\sqrt3t)\) is multiplied by \(2-\sqrt3\).  No generic parity or metric randomness is assumed there. |
| `perfect_power_metric_recurrence` | Passed.  The derivation is uniform for every nonzero strict distance and makes no inference from the absence of rational exact nonsquare centers; square and fourth-power metric recurrences remain in the residual incidence problem. |
| `endpoints_stars_and_collars` | Passed.  (R80.1) removes only a constant phase.  The same integration endpoints, floors, stars, profiles, physical collars, finite lift support, and saddle transitions remain owned exactly once. |
| `coefficient_adversary` | Passed.  (R80.8) is explicitly a proxy showing that (80.5) cannot imply signed cancellation; it is not represented as an actual choice of \(A^°\) or a counterexample to (80.14). |
| `rank_one_self_return` | Passed.  Product-fiber re-enumeration is bijective, and the proxy becomes constant positive rows after the exact decentering, so a norm-only \(TT^*\) argument has a rank-one aligned obstruction. |
| `downstream_scope` | Passed.  No claim is made for the full residual target, \(M9\!\! -\! M2\), \(M9\), endpoint uniformity, or the global exponent. |

## 6. Dependencies and exact artifacts used

Only the following two permitted artifacts were read or used:

1. `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/briefs/blind_strict_metric_energy_rederivation.md`.
2. `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/derivation_packet.md`.

No shared state, strategy file, prior-round report, sibling report, source
card, web source, or computation was used.  The result is a packet-local
algebraic derivation.

## 7. Recommended state effect

**Retain** (R80.1)--(R80.6) as an exact actual-symbol no-go for the proposed
quotient-parity and half-integer Fourier-gap mechanisms.  Reject any closure
which freezes \(\mathfrak B^°\) while extracting
\(e(-g\Lambda/(2k))\), or which discards the restored \(r=0\) density term.
Do not reject (80.14) and do not record an actual-symbol counterexample: a
new analysis of the decentered integral (R80.1), possibly exploiting
\((-1)^q\) jointly with its cross-ray dependence, could still close the
sum.  The residual obligation should remain open and, if revised, should
demand an estimate of the strength (R80.14).  No downstream promotion is
warranted.
