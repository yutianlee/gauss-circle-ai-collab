# Verdict

**GREEN.**  The repaired durable kernel preserves every mathematical formula
(K187.1)--(K187.27), the current candidate's carrier and normalization, the
multiplicity and power ledgers, and every proved/open boundary.  The additions
are exact definitions of previously implicit notation, an explicit complete
`U=1` contribution, provenance/evidence metadata, and TeX hygiene.  They add no
new estimate and require no mathematical repair.

# Frozen and current hashes

| Artifact | SHA-256 |
|---|---|
| Previously GREEN durable kernel | `b9119e5d11e78d6ae45eca461f4acb2cdd9f6c49611612ee45e9f32f5dc27c74` |
| Current repaired durable kernel | `026b9709bba25251c4030bd8475a35710c8c1c25cd9d103e0172821bd694ce24` |
| Current formal candidate | `c2f01f57a41695d73d0d1f9716a03328147dbe79f0fcdeb7e8e3465b29779b89` |

# Exact delta classification

## Mathematical formulas (K187.1)--(K187.27)

Every numbered formula has the same variables, hypotheses, signs,
normalization, summation ranges, inequalities, and constants as in the frozen
kernel:

| Formula | Replay outcome |
|---|---|
| (K187.1) | Unchanged affine-parity amplitude `A`; same positive index set and literal `B`. |
| (K187.2) | Unchanged definitions of `E_U`, `c_U`, and `q_U`. |
| (K187.3) | Unchanged separate plus/minus `U=1` anchors `(0,-h)` and `(0,h)`. |
| (K187.4) | Unchanged complete exact-conductor set `q_U(k) <= Q`. |
| (K187.5) | Unchanged edge set: `q_U(k)>Q` and either `U<=4Q` or `0<|k|_U<=Q`. |
| (K187.6) | Unchanged high set: `U>4Q`, `q_U(k)>Q`, and `|k|_U>Q`. |
| (K187.7) | Unchanged sum over both orientations, the full primitive carrier, all modes, and literal amplitudes. |
| (K187.8) | Unchanged exact four-piece decomposition with one outer real part. |
| (K187.9) | Unchanged absolute target-safe bound for the `U=1`, low-conductor, and edge packets. |
| (K187.10) | Unchanged positive `O(Y L^2 X^epsilon)` complement bound. |
| (K187.11) | Unchanged, explicitly still-open, one-sided `O(L^2 X^epsilon)` complement relation. |
| (K187.12) | Unchanged odd-modulus geometric Fourier transform. |
| (K187.13) | Unchanged positive-phase inversion and mean `c_U(0)=1/U`. |
| (K187.14) | Unchanged half-angle coefficient, logarithmic l1 mass, and Parseval l2 mass one. |
| (K187.15) | Unchanged unique representation `k=(U/q)a`, `q|U`, with reduced `a`. |
| (K187.16) | Unchanged coefficient scaling `(q/U)c_q(a)` and inverse-residue phase reduction. |
| (K187.17) | Unchanged fixed-`(kappa,g,h,U)` literal atom-weight bound. |
| (K187.18) | Unchanged support bounds for `U` and `kappa g`. |
| (K187.19) | Unchanged dyadic height/product count. |
| (K187.20) | Unchanged exact-conductor coefficient mass. |
| (K187.21) | Unchanged nested-divisor low-conductor power ledger. |
| (K187.22) | Unchanged ordinary low-residue `Q/U` mass. |
| (K187.23) | Unchanged conductor kernel and centered kernel definitions. |
| (K187.24) | Unchanged exact-conductor inversion and unit Ramanujan pairing. |
| (K187.25) | Unchanged centered orientation-difference identity and `q=1` cancellation. |
| (K187.26) | Unchanged prime-conductor self-return. |
| (K187.27) | Unchanged retained high-mode l2 lower bound `8/pi^2`, including `q_U(k)>Q`. |

## Exact definitional additions

The following additions only make notation or an already-used component
self-contained:

1. `e(x)=exp(2 pi i x)`, the least-residue convention `[x]_U`, and
   `bar(v) v = 1 (mod U)` are now stated before use.
2. The complete `U=1` complex piece is now defined explicitly as
   
   \[
   \mathscr U_{1,Y}^{\sigma}
   =\sum_{\omega\in\{+,-\}}
    \sum_{\substack{\mathfrak f:\,Y<h\le2Y\\U=1}}
    A_{\mathfrak f,\omega}^{\sigma},
   \]
   
   with the inherited primitive carrier still imposed.  This is exactly
   candidate (187.K2), uses the unchanged anchors (K187.3), and neither adds
   nor removes any `U=1` atom.
3. `mathbb U(q)` is now explicitly the reduced residue group for `q>1`, with
   the existing special convention `mathbb U(1)={0}`.
4. `tau` and `mu` are identified as the divisor and Möbius functions before
   their uses.  Their formulas and estimates are unchanged.

## Non-mathematical and provenance additions

- The heading and inline mathematics received standard TeX delimiters and
  backslashes.
- Campaign, round, graph, source-candidate, reconciliation, evidence-status,
  and diagnostic-control metadata were added.
- The evidence section now states precisely that the blind report proves the
  direct small-modulus/ordinary-edge packet but not the stronger complete
  small exact-conductor grouping.  This is evidence attribution, not a change
  to the proved kernel.
- The two diagnostic artifacts are hash-bound and remain explicitly
  `diagnostic_only`; no numerical theorem evidence was added.

# Carrier, multiplicity, and boundary replay

The primitive domain remains

\[
 \kappa,g,h,U,v>0,\quad \kappa,g,U\text{ odd},\quad
 (gU,v)=1,\quad(U,h)=1,\quad0<2\kappa gh<R_0.
\]

Both orientations remain under one outer real part.  Every selector,
squarefree and allocation-coprimality deletion, profile, floor, star,
half-weight, hard sample, crossing, endpoint, conjugation, Fejer factor,
square-root phase, sign, and zero extension remains inside the unchanged
literal amplitude.

The multiplicity replay is unchanged: `u=gU`, `n=gh`, `h<<U`; at fixed
`(kappa,u,U)` there are `O(U)` heights, `O(L/kappa)` values of `v`, and
`O(kappa)` live sites, hence `O(UL)` atoms across both orientations.  Exact
conductor mass remains `O((q/U) log(2q))`, producing fixed-coordinate cost
`O(L q log(2q))` and the same target-safe nested-divisor bound.  Positive
recombination of the exact complement still loses the complete factor `Y`.

# First open step and state recommendation

The first open step remains exactly (K187.11):

\[
 \Re\mathscr R_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\]

Retain the **GREEN** normalization, carrier, multiplicity, power, and
candidate-consistency verdicts.  Accept the repaired durable kernel at hash
`026b9709bba25251c4030bd8475a35710c8c1c25cd9d103e0172821bd694ce24`
only as `proved_internal` evidence for the strict inverse-residue conductor
reduction.  Keep the complete high-height target, the original `t=1`
residual, every `t>=2` and near-resonant complement, all parents, bridges,
theorems, and exponent claims open.  No kernel, candidate, graph, synthesis,
validation-matrix, or proof-draft edit is made by this replay.
