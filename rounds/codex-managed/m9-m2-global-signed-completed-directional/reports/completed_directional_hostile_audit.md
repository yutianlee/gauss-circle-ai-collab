# Round 110 hostile audit: global completed directional scalar

Campaign: `m9-m2-global-signed-completed-directional`

Task: `completed_directional_hostile_audit`

Role: hostile seam and source reviewer

Starting graph SHA-256: `33bf8e043cb8a1e0852b7f98941ee6186f798ed40124525de3d0373269019397`

## 1. Result

The real-part reduction is correct, but it is an exact return to the
original Round-75 off-diagonal problem, not a smaller global hard kernel.
Let \(\mathcal D_{75,L}\) be the separate Round-75 diagonal and let
\(\mathcal O_{75,L}\) be its real off-diagonal correlation, normalized
with one positive orientation and one outer \(2\Re\).  Exact summation of
the completed all-atom blocks, followed by the adjoint finite Poisson
inversion already certified in Rounds 77 and 80, gives at the level relevant
to the energy

\[
 \boxed{
 \mathcal O_{75,L}
  =2\Re \mathfrak C_L^{\mathrm{comp}}+\mathcal P_{77,L},
 \qquad
 |\mathcal P_{77,L}|\ll_\varepsilon L^2X^\varepsilon .}
\tag{110.H1}
\]

Here \(\mathcal P_{77,L}\) is the target-sized transform packet not placed
in the oriented completed atom space: the inherited primal endpoint and
collar samples, original Poisson zero/positive modes, and whichever
equality/nonstationary boundary terms remain outside the adopted finite
fixed-lattice cover.  Consequently

\[
 \boxed{
 \mathcal E_L^{\mathrm{top}}
 =\mathcal D_{75,L}+\mathcal P_{77,L}
  +2\Re\mathfrak C_L^{\mathrm{comp}},
 \qquad
 \mathcal D_{75,L}+|\mathcal P_{77,L}|
 \ll_\varepsilon L^2X^\varepsilon .}
\tag{110.H2}
\]

Thus the proposed one-sided estimate
\(\Re\mathfrak C_L^{\mathrm{comp}}\ll_\varepsilon
L^2X^\varepsilon\) is both sufficient and necessary, up to target-sized
terms, for the hard-top energy theorem.  It is nevertheless only a
re-expression of that theorem.  The completed complex sum remains a useful
finite transform representation, and its imaginary part need not return to
any real Round-75 quantity, but no strictly smaller scalar survivor remains
after *global* all-owner completion and inversion.

The conductor candidate does not itself write the literal recombined
kernel needed to verify (110.H1).  The accepted Round-109 all-atom
dictionary and the Round-80 adjoint return determine what any lawful formula
must do, but the candidate only defines
\(\mathfrak C_L^{\mathrm{comp}}=\sum_B\mathfrak Q_B^{\mathrm{comp}}\).
Accordingly the abstract implication and the actual-symbol self-return are
certified; the candidate's promised literal merged formula and every new
cancellation estimate are not.

There is no direct cancellation claim in the candidate to promote.  The
retained identity
\(\chi_4(ga)\chi_4(gb)=\chi_4(a)\chi_4(b)=(-1)^{(b-a)/2}\)
is exact, but it is the original Round-75 two-leg character.  It is constant
in \(a\) and in the odd lift \(g\) at fixed \(q=(b-a)/2\), and it cancels
identically after the fixed-\(a\) Gram lift.  Character retention therefore
identifies the only possible linear direction for a new proof; it supplies
no cancellation by itself.

## 2. Exact statement and hypotheses

Put \(J=X^{1/2}\), \(1\le L\le J^{1/2}\), and
\(T_\varepsilon=L^2X^\varepsilon\).  Use only primitive odd
\(a<b<4a\), one representative orientation, and one outer \(2\Re\).
All \(A,D,K,G\) lattices are finite and half-open; the reciprocal saddle
interval is open; genuine integer equalities retain their inherited stars
or half weights.  Physical completion means zero extension of the unchanged
collared coefficient, not deletion or point evaluation of a moving collar.

Assume the accepted identities

\[
 \mathcal E_L^{\mathrm{top}}
 =\mathcal E_{\mathrm{owned},L}
  +2\Re\sum_B\mathfrak Q_B^{\mathrm{res}},
 \qquad
 \mathfrak Q_B^{\mathrm{res}}
 =\mathfrak Q_B^{\mathrm{comp}}-
   \sum_\nu\mathfrak O_{B,\nu},
\tag{110.H3}
\]

and

\[
 \mathcal E_{\mathrm{owned},L}\ll_\varepsilon T_\varepsilon,
 \qquad
 \sum_{B,\nu}|\mathfrak O_{B,\nu}|
 \ll_\varepsilon T_\varepsilon .
\tag{110.H4}
\]

The original owned energy is nonnegative; after owner transfer its signed
replacement need not be.  Define

\[
 \mathfrak C_L^{\mathrm{comp}}
 :=\sum_B\mathfrak Q_B^{\mathrm{comp}},
 \qquad
 \widetilde{\mathcal E}_{\mathrm{owned},L}
 :=\mathcal E_{\mathrm{owned},L}
    -2\Re\sum_{B,\nu}\mathfrak O_{B,\nu}.
\tag{110.H5}
\]

Then

\[
 \mathcal E_L^{\mathrm{top}}
 =\widetilde{\mathcal E}_{\mathrm{owned},L}
  +2\Re\mathfrak C_L^{\mathrm{comp}},
 \qquad
 |\widetilde{\mathcal E}_{\mathrm{owned},L}|
 \ll_\varepsilon T_\varepsilon .
\tag{110.H6}
\]

For the exact literal recombination, every base atom must have the same
nonmetric coefficient in each of its metric tags and must use

\[
 \sum_{\substack{1\le R<G_*\\R\ \mathrm{dyadic}}}
   W_R(t)+V_{G_*}(t)-1_{t\in\mathbb Z}
 =1_{t\notin\mathbb Z},
 \qquad t={\Lambda\over k},
\tag{110.H7}
\]

with the exact-centre contribution restored or owned exactly once when the
full carrier is recombined.  The zero Fourier coefficient of each smooth
member is the metric density; it is not the original Round-77 Poisson zero
mode.  Half-open \(A,D,K,G\) one-count, the terminal member, fixed
\(k\)-lattice, open physical reciprocal interval, finite lift support,
floors, stars, entry/exit transitions, empty/singleton fibres, and all
collars must remain unchanged until their exact partition sums are taken.

Under these hypotheses the sharp scalar equivalence is

\[
 \mathcal E_L^{\mathrm{top}}\ll_\varepsilon T_\varepsilon
 \quad\Longleftrightarrow\quad
 \bigl(\Re\mathfrak C_L^{\mathrm{comp}}\bigr)_+
       \ll_\varepsilon T_\varepsilon
 \quad\Longleftrightarrow\quad
 \Re\mathfrak C_L^{\mathrm{comp}}
       \ll_\varepsilon T_\varepsilon .
\tag{110.H8}
\]

This is a one-sided gauge, not a complex norm.  In the presence of
\(\mathcal E_L^{\mathrm{top}}\ge0\) and (110.H6), it also implies
\(|\Re\mathfrak C_L^{\mathrm{comp}}|\ll T_\varepsilon\).  It does not
imply \(|\mathfrak C_L^{\mathrm{comp}}|\),
\(\sum_B|\mathfrak Q_B^{\mathrm{comp}}|\), or any fixed-\(a\) Gram
estimate.

## 3. Proof or derivation

Substituting the second identity in (110.H3) into the first and using
finiteness gives (110.H6) without a limiting interchange.  If
\(\Re\mathfrak C_L^{\mathrm{comp}}\le C_1T_\varepsilon\), then

\[
 \mathcal E_L^{\mathrm{top}}
 \le |\widetilde{\mathcal E}_{\mathrm{owned},L}|
     +2C_1T_\varepsilon
 \ll_\varepsilon T_\varepsilon.
\]

Conversely, if the hard energy is target-sized, then

\[
 \Re\mathfrak C_L^{\mathrm{comp}}
 ={\mathcal E_L^{\mathrm{top}}
    -\widetilde{\mathcal E}_{\mathrm{owned},L}\over2}
 \ll_\varepsilon T_\varepsilon.
\]

Moreover energy positivity gives the unconditional lower bound

\[
 \Re\mathfrak C_L^{\mathrm{comp}}
 \ge -{1\over2}
       |\widetilde{\mathcal E}_{\mathrm{owned},L}|
 \ge -C_\varepsilon T_\varepsilon.
\tag{110.H9}
\]

This proves (110.H8) and shows why no estimate for the imaginary part is
needed.

For the self-return, Round 75 gives the exact finite decomposition

\[
 \mathcal E_L^{\mathrm{top}}
 =\mathcal D_{75,L}+\mathcal O_{75,L},
 \qquad \mathcal D_{75,L}\ll_\varepsilon T_\varepsilon,
\tag{110.H10}
\]

where \(\mathcal O_{75,L}\) is one positive offset correlation followed
by one outer \(2\Re\).  Round 77 applies finite Poisson summation to that
one-orientation correlation and leaves a componentwise target-sized
endpoint/collar/original-mode packet.  On every retained stationary atom,
Round 80 proves the exact carrier identity

\[
 \mathfrak C^\circ_{a,b,k}(g)
 =\int_{gb/4}^{ga}A^\circ_{ga,gb}(x)
   e\!\left(kx-J(\sqrt{gb}-\sqrt{ga})\sqrt x\right)dx.
\tag{110.H11}
\]

Under \(h=ga\), \(s=gb\), unique primitive-ray factorization gives

\[
 \chi_4(a)\chi_4(b)=\chi_4(h)\chi_4(s),
\]

and (110.H11), with the exact reciprocal interval, is the adjoint Poisson
kernel of the original Round-75 positive offset.  Round 109 then makes the
completion coefficientwise: `res` plus each first-priority owner is the
all-atom \(\mathfrak Q_B^{\mathrm{comp}}\).  Summing the half-open
\(A,D,K,G\) tags counts each physical atom once, summing (110.H7) restores
the full metric carrier with its centre convention, and the fixed-lattice
complement restores the nonstationary/equality negative modes assigned to
it.  The diagonal never enters this oriented atom space.  The surviving
primal endpoint/collar and original-mode terms are exactly the transform
packet \(\mathcal P_{77,L}\).  This proves (110.H1)--(110.H2).

This calculation is an actual-symbol no-go for gaining power merely by
global completion, Poisson inversion, Gaussian functional calculus, or
character refactorization: the result is the original correlation with the
same character and capacity.  It is not an arbitrary-coefficient
countermodel.

The direct character ledger is equally exact.  With \(b=a+2q\),

\[
 \chi_4(ga)\chi_4(gb)=(-1)^q.
\tag{110.H12}
\]

At fixed \(q\), (110.H12) is independent of \(a\) and every odd \(g\), so
there is no character orthogonality in either of those variables.  Across
\(q\), alternation remains available only before squaring and only if the
complete moving actual coefficient is controlled jointly with it.  In the
fixed-\(a\) shifted Gram, the Fejer shift sign times the two character pairs
is identically one.  Hence a Gram theorem cannot be inferred from the
linear character opportunity.

Finally, the norm upgrades are invalid.  The finite scalar choices
\(C=iM\), or \(Q_{B_1}=M\), \(Q_{B_2}=-M\), show respectively that a
small real part need not control modulus and that a small global scalar need
not control blockwise absolute mass.  A row \((M,-M)\) has zero linear sum
and positive energy \(2M^2\), so no positive Gram follows.  These three are
abstract norm controls only.  Likewise, replacing the actual coefficient
by an unsigned or phase-conjugating array can neutralize (110.H12), but that
array is not the Vaaler/collared actual symbol and is not a lower bound for
it.

## 4. First doubtful or unproved step

The first unsupported seam in the Round-110 candidate is its promised
literal kernel, not the real-part algebra.  The expression

\[
 \mathfrak C_L^{\mathrm{comp}}
 =\sum_B\mathfrak Q_B^{\mathrm{comp}}
\]

does not display the completed amplitude, its exact block weights, or the
map from the tagged union to one untagged atom space.  In particular it does
not itself prove that:

- the nonmetric coefficient is identical across all \(R\)-tags so that
  (110.H7) may be telescoped;
- the terminal \(V_{G_*}\) and the exact-centre point atom occur once;
- the metric density remains coupled to all discrepancy modes while the
  original Poisson zero mode stays in \(\mathcal P_{77,L}\);
- the half-open \(A,D,K,G\) partitions and fixed \(k\)-lattices cover the
  same finite negative-mode universe with no gap or repeated equality;
- the unchanged collars, physical entry/exit, floors, stars, lift endpoints,
  empty fibres, and singleton fibres are carried through the merger; and
- the diagonal and conjugate orientation are absent from the inner scalar.

If these conditions are supplied, the completed all-atom sum necessarily
satisfies the self-return (110.H1); it cannot simultaneously be advertised
as a strictly smaller residual hard kernel.  If a proposed merged formula
still contains a residual square, safe, short-row, or hard-\(\rho\) owner
mask, then it has not summed the Round-109 all-atom completion.  If it omits
the target packet, exact centre, terminal member, or a reciprocal equality,
then it is not equal to the Round-75 correlation after inversion.

The smallest presently lawful object is therefore the **tagged**, unmerged
finite scalar

\[
 \mathfrak C_{L,\mathrm{tag}}^{\mathrm{comp}}
 :=\sum_{B=(A,D,K,G,R)}\mathfrak Q_B^{\mathrm{comp}},
\tag{110.H13}
\]

together with (110.H6) and the energy-relevant self-return
\(2\Re\mathfrak C_{L,\mathrm{tag}}^{\mathrm{comp}}
=\mathcal O_{75,L}+O_\varepsilon(T_\varepsilon)\).  Its one-sided estimate
is wholly open.  No strict positive-power subrange, smaller outside-absolute
survivor, or direct two-character cancellation is proved.

There is also a durable graph normalization defect: the current statement
of `M9-M2-top-endpoint-density-discrepancy-energy` says both conjugate
orientations are summed *and* places one outer \(2\Re\).  That literal
wording contradicts the accepted Round-109 convention and would double the
off-diagonal.  It must be revised to one orientation plus \(2\Re\), or both
orientations with no outer \(2\Re\), before it can serve as a downstream
target.

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| `real_part_modulus_blockwise_and_Gram_norms` | **Pass.** The positive real part is the minimal gauge. Energy positivity supplies the missing lower real-part bound. \(C=iM\), two cancelling blocks, and a cancelling two-entry row separate modulus, blockwise absolute mass, and Gram energy. These are abstract controls, not actual-symbol obstructions. |
| `energy_positivity_and_owned_sign` | **Pass.** The transferred owned correction may be signed, so only its absolute target bound is used. Positivity is used solely for (110.H9). |
| `Round75_self_return_and_transform_packet` | **Pass at the energy-relevant real level.** Exact all-atom recombination and adjoint Poisson inversion give (110.H1). The Round-75 diagonal and target-sized Round-77 primal/transform packet stay outside the oriented scalar. No new global kernel with smaller capacity remains. |
| `one_orientation_one_outer_2Re` | **Pass for Round 110; fail in one stale graph statement.** The candidate uses \(a<b\) and one outer \(2\Re\). Summing the conjugate orientation again doubles the off-diagonal. |
| `finite_block_interchange_and_one_count` | **Pass for the tagged sum; not certified for the advertised merged formula.** Finiteness licenses reordering. Half-open scale ownership and the Round-109 priority give one count, but the Round-110 candidate does not display the merger map. |
| `literal_completed_kernel_dictionary` | **Fail as written.** The candidate contains no atom-level formula. The accepted dictionary determines a valid tagged object, and any fully recombined all-atom formula must self-return as in (110.H1). |
| `original_zero_mode_vs_metric_density` | **Pass in the inherited dictionary.** The metric density is \(\widehat W_R(0)\) or \(\widehat V_{G_*}(0)\) inside the coefficient. The original Poisson zero mode belongs to \(\mathcal P_{77,L}\). The candidate does not display this distinction literally. |
| `terminal_member_and_exact_centre` | **Pass in the inherited telescope; absent from the candidate formula.** \(\sum_R W_R+V_{G_*}-1_{\mathbb Z}=1_{\mathbb R\setminus\mathbb Z}\) is exact. Omitting the point atom or terminal changes the kernel. |
| `q1_square_Pell_fourth_power_and_near_centres` | **Pass as hostile guards.** Fixed-\(q\) character constancy, square/fourth-power coherence, Pell/near-square rows, and exact/near centres reject uniform parity or derivative-gap arguments. They are owned or target-safe controls and do not lower-bound the complete actual scalar. |
| `false_unsigned_and_phase_conjugating_coefficients` | **Pass with scope.** They refute coefficient-blind cancellation and norm upgrades only. They are not actual-symbol no-go results. The Poisson self-return and fixed-variable character constancy are the actual-symbol no-go statements. |
| `Fejer_Gram_nonimplication` | **Pass.** The fixed-\(a\) Gram cancels the two character pairs and contains owner cross terms. Scalar completion does not commute through it and supplies no cross energy. |
| `transform_self_return` | **Pass exactly.** The Round-80 carrier identity and adjoint Poisson inversion return the original transposed two-character off-diagonal. Round-108 Gaussian functional calculus is the same equal-capacity phenomenon. |
| `primary_source_hypothesis_map` | **No new theorem invoked.** The candidate makes no Poisson, large-sieve, theta, Kuznetsov, or bilinear estimate. The Round-108 primary-source non-applicability map remains controlling; none of those sources accepts the literal moving completed symbol. |
| `downstream_and_exponent_scope` | **Pass.** No completed scalar estimate, fixed-\(a\) Gram, hard cone, smooth packet, \(M9\! -\! M2\), \(M9\! -\! M1\), endpoint theorem, \(M9\), or exponent is proved. |

No numerical experiment was used.  The actual-symbol conclusions are exact
finite algebra, character algebra, or invertible-transform identities.

## 6. Dependencies and exact artifacts used

The assigned context was read and used:

- `protocol.md`;
- `state/proof_obligations.yml`, in particular the three Round-110 target
  nodes, the accepted Round-75/77/80/108/109 interfaces, and the current
  rejection ledger;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-global-signed-completed-directional/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-global-signed-completed-directional/candidates/conductor_global_signed_kernel.md`;
- `rounds/codex-managed/m9-m2-blockwise-owner-completion/reports/linear_owner_completion_attack.md`;
- `rounds/codex-managed/m9-m2-blockwise-owner-completion/reports/owner_completion_hostile_audit.md`;
- `rounds/codex-managed/m9-m2-blockwise-owner-completion/reviews/conductor_round109_adjudication.md`;
- `rounds/codex-managed/m9-canonical-core-formalization/synthesis.md`;
- `rounds/codex-managed/m9-m2-metaplectic-two-character-energy/reports/two_character_spectral_source_hostile_audit.md`.

For the conductor-requested Round-75 inversion seam, the following exact
accepted artifacts were additionally checked:

- `rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/reviews/conductor_round75_adjudication.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reviews/conductor_round77_adjudication.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/reviews/conductor_round80_actual_symbol_recoupling.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/reviews/conductor_round80_adjudication.md`;
- `rounds/codex-managed/m9-m2-blockwise-owner-completion/reviews/conductor_round109_owner_dictionary.md`;
- `rounds/codex-managed/m9-m2-blockwise-owner-completion/reviews/conductor_round109_metric_reconstruction.md`;
- `rounds/codex-managed/m9-m2-blockwise-owner-completion/synthesis.md`.

No Round-110 sibling report, external theorem, web source, or computational
artifact is used.  The primary sources audited in Round 108 are relied on
only for the recorded non-applicability guard, not for a new estimate.

## 7. Recommended state effect

**Promote narrowly** the exact algebraic connector (110.H6)--(110.H9), with
the minimal target written as
\((\Re\mathfrak C_L^{\mathrm{comp}})_+\ll_\varepsilon
L^2X^\varepsilon\).  Record that, under the accepted all-atom one-count,
its globally recombined real part satisfies the actual-symbol self-return
(110.H1).  This connector is a reformulation of the hard-top energy, not a
new estimate.

**Retain and revise** the literal completed-kernel candidate.  Before calling
it a single merged kernel, write the atom-level coefficient and verify every
partition sum listed in Section 4.  The smallest lawful survivor until then
is the tagged finite sum (110.H13).  Once the merger is written correctly,
state explicitly that exact inverse Poisson returns the original Round-75
off-diagonal up to \(\mathcal P_{77,L}\); do not advertise the completed
global scalar as a strictly smaller correlation.

**Retain open** the one-sided estimate itself.  Record as actual-symbol
no-go information that completion/inversion has equal capacity, that the
primitive character is constant in \(a,g\) at fixed \(q\), and that it
vanishes from the fixed-\(a\) Gram.  Keep unsigned and phase-conjugating
arrays only as abstract controls.

**Revise** the stale orientation wording in
`M9-M2-top-endpoint-density-discrepancy-energy`: use one representative
orientation with one outer \(2\Re\), or both orientations with no outer
\(2\Re\), never both.

Make no status change to the fixed-\(a\) actual Gram, canonical blockwise
outside-absolute theorem, hard signed cone, either smooth M2 packet,
\(M9\! -\! M2\), \(M9\! -\! M1\), endpoint uniformity, \(M9\), the
conditional bridge, or the Gauss-circle target.
