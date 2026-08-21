# Conductor review: Round 95 normalization and lift diagonal

Campaign: `gc-strict-sub-one-third-cluster-source-fork`

Starting graph SHA-256:
`e3233f94ee0630b28c21ba102a0ee0fc55016858af6fbd61e80ea0e264128104`

## Blind gate

The statement-only report used only its permitted derivation packet.  It
independently verifies

\[
 W=Y^{7/16},\qquad Q_{\rm target}=Y^{15/16+\varepsilon},
 \qquad \theta_{\rm target}=5/16,
\]

the \(Y^{5/48}\) minimax cell count, and the M1/M2 factor four. It
correctly refuses to estimate exact lifts without the literal
coefficients and isolates the signed near-frequency form after those
lifts are combined.

## Literal lift coefficients

The accepted H4 formulas close the blind report's first conditional seam.
On a signed height shell \(|h|\asymp L\), denominator shell \(d\asymp D\),
and a fixed moving-symbol stratum, write \(h=ga\), \(d=gb\),
\((a,b)=1\). Up to fixed constants,

\[
 B_1(a,b)=\frac{\chi_4(b)}a
 \sum_{g\asymp D/b}\frac{\chi_4(g)}gU_1(g),
 \qquad
 B_2(a,b)=\frac{\chi_4(a)}a
 \sum_{g\asymp D/b}\frac{\chi_4(g)}gU_2(g),
 \tag{R95.1}
\]

with the respective odd supports. Each \(U_i\) is a literal bounded-BV
height/profile/prefix symbol; a hard endpoint or star adds only a bounded
jump.

Since partial sums of \(\chi_4\) are bounded, BV partial summation gives

\[
 \left|\sum_{g\asymp G}\frac{\chi_4(g)}gU_i(g)\right|
 \ll_\varepsilon X^\varepsilon G^{-1}.
 \tag{R95.2}
\]

Here \(G\asymp D/b\asymp L/|a|\), so

\[
 |B_i(a,b)|\ll_\varepsilon X^\varepsilon L^{-1}.
 \tag{R95.3}
\]

There are \(O_\varepsilon(X^\varepsilon DL)\) reduced signed fractions
on the shell: for each \(b\), one has
\(|a|\asymp Lb/D\), and summing this interval length over
\(D/L\ll b\ll D\) gives \(O(DL)\). Consequently the complete
equal-frequency diagonal, including every lift cross term, satisfies

\[
 \boxed{\sum_{(a,b)=1}|B_i(a,b)|^2
 \ll_\varepsilon X^\varepsilon D/L.}
 \tag{R95.4}
\]

At the minimax point this is \(Y^{1/3+\varepsilon}\), below the
\(Y^{1/2+\varepsilon}\) target. Thus exact lifts are not the Round-95
blocker.

## First strict internal survivor

For \(\kappa_1=1\), \(\kappa_2=4\), put \(n=ab'-a'b\). The unequal part is

\[
 \mathcal O_i(c)=
 \sum_{n\ne0}B_i(a,b)\overline{B_i(a',b')}
 e\left(\frac{cn}{\kappa_i bb'}\right)
 \left(1-\frac{W|n|}{\kappa_i bb'}\right)_+,
 \tag{R95.5}
\]

where the displayed sum abbreviates the literal reduced supports and
\(n=ab'-a'b\). No character or arithmetic absolute value has been
removed.  The internal target is

\[
 |\mathcal O_i(c)|\ll_\varepsilon Y^{1/2+\varepsilon}.
 \tag{R95.6}
\]

Farey row degree alone gives
\((1+D^2/W)D/L=Y^{43/48+\varepsilon}\), missing by
\(Y^{19/48}\). This is a false-shadow capacity, not the best actual
arithmetic theorem.

## Best accepted full-discrepancy ceiling

The source-audited Popov local moment gives

\[
 Q(Y,W)\ll W\sqrt Y+Y(\log Y)^2.
 \tag{R95.7}
\]

At the frozen window, its divided cluster capacity is
\(Y^{1/2}+Y^{9/16}(\log Y)^2\). It misses the desired full local mass by
only \(Y^{1/16}\), but the additive \(Y\)-term returns exactly the
one-third exponent under persistence.  Therefore any strict internal
advance must save a fixed power in the actual off-diagonal/additive term;
the random-cell identity and diagonal accounting are already complete.

## Current decision

The normalization, moving-stratum implication, and lift diagonal pass.
No strict internal exponent is promoted before the analytic report estimates
(R95.5); an independent primary-source audit is a logically separate route to a
direct theorem.

Artifacts used:

- `state/best_proof_draft.md`;
- `rounds/codex-managed/gc-prescribed-point-local-moment-bridge/synthesis.md`;
- `rounds/codex-managed/gc-prescribed-point-local-moment-bridge/reviews/conductor_round94_local_kernel.md`;
- `rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/reports/moving_coefficient_moment_attack.md`;
- `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/reports/blind_fixed_cluster_rederivation.md`;
- `sources/popov_2024_local_moments.md` and its accepted graph node.
