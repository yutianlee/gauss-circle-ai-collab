# Verdict

**GREEN.**  The durable kernel is substantively identical to the current
formal candidate on every mathematical interface reviewed.  It introduces no
new estimate, drops no literal field, changes no normalization or
multiplicity, and preserves every proved/open boundary.  No repair is
required.

# Frozen artifacts and hashes

The kernel was hashed before review and rechecked after review.

| Artifact | SHA-256 |
|---|---|
| `proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md` | `b9119e5d11e78d6ae45eca461f4acb2cdd9f6c49611612ee45e9f32f5dc27c74` |
| `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/candidates/formalized_hard_m1_t1_high_h_inverse_residue_conductor_reduction.md` | `c2f01f57a41695d73d0d1f9716a03328147dbe79f0fcdeb7e8e3465b29779b89` |

The candidate hash is the post-TeX-repair hash already verified in
`candidate_normalization_post_tex_repair_verification.md`.  The two inserted
backslashes in its conductor display are rendered correctly in kernel
(K187.15) and make no mathematical change.

# Exact candidate-to-kernel consistency checks

## Carrier, orientations, and literal scope

- Kernel lines 13--36 import exactly (K185.27) and
  (K185.30)--(K185.35), with
  
  \[
  \kappa,g,h,U,v>0,\quad \kappa,g,U\text{ odd},\quad
  (gU,v)=1,\quad(U,h)=1,\quad0<2\kappa gh<R_0,
  \]
  
  and the same affine sum
  \(A_{\mathfrak f,\omega}^{\sigma}=\sum_t(-1)^tB(t)\) as the
  candidate.
- Both orientations remain present through the sum over
  \(\omega\in\{+,-\}\), with one real part outside the complete aggregate.
- The kernel explicitly retains every residual selector, squarefree and
  allocation-coprimality deletion, profile, floor, star, half-weight, hard
  sample, crossing, endpoint, conjugation, Fejer factor, phase, sign, and zero
  extension inside the unchanged literal amplitude.  No support regularity is
  added.
- Kernel (K187.3) gives the exact separate \(U=1\) anchors
  \((0,-h)\) and \((0,h)\).  Since both have \(S_0=0\), their complete
  contribution has the same outer anchor sign (+1) as candidate (187.K2).
  The positive index sets and zero extension remain inherited from
  (K185.31)--(K185.35).

## Fourier normalization and conductor algebra

The following kernel/candidate correspondence is exact:

| Durable kernel | Current candidate | Check |
|---|---|---|
| (K187.2) | definitions before (187.K1) | Same (E_U), (c_U(k)=2/[U(1+e(-k/U))]), (q_U(k)=U/(k,U)), and orientation signs. |
| (K187.12) | (187.K9) | Same odd-(U) geometric sum (widehat E_U(k)=2/(1+e(-k/U))). |
| (K187.13) | (187.K10) | Same positive-phase inversion and mean (c_U(0)=1/U). |
| (K187.14) | (187.K11) | Same half-angle formula, logarithmic (ell^1) mass, and Parseval mass (1). |
| (K187.15)--(K187.16) | (187.K12) | Same unique (k=(U/q)a), (q\mid U), (a\in\mathbb U(q)), including ((q,a)=(1,0)), and the same coefficient and phase scaling. |
| (K187.23)--(K187.26) | (187.K20)--(187.K23) | Same unit-(b) conductor kernels, Ramanujan pairing, centered orientation difference, (q=1) cancellation, and prime self-return. |

In particular, the kernel preserves the previously verified hypotheses that
(a_{mathfrak f}=\bar vh) is a nonzero unit and that the centered identities
are used only for unit (b).

## Mode partition and exact decomposition

Kernel (K187.4)--(K187.6) is exactly candidate (187.K3)--(187.K5) written as
three mode sets:

\[
 q_U(k)\le Q;
\]

\[
 q_U(k)>Q,\quad U\le4Q\ \text{or}\ 0<|k|_U\le Q;
\]

\[
 U>4Q,\quad q_U(k)>Q,\quad |k|_U>Q.
\]

The sets are pairwise disjoint and exhaustive.  Because (Q\ge1), the zero
mode has conductor (1) and occurs only in the first set.  Inserting these
sets into kernel (K187.7) is identical to the candidate's explicit
exact-conductor formula: (K187.15)--(K187.16) converts its (c_U(k)) form into
((q/U)c_q(a)e(\epsilon_\omega a\bar vh/q)).  Hence kernel (K187.8) is exactly
candidate (187.K1), with no rearrangement, omitted orientation, or duplicated
mode.

The high-mode energy statement is also unchanged.  For odd (U>4Q), the two
near-half modes have (q_U(k)=U>Q), (|k|_U>Q), and
(|c_U(k)|\ge2/\pi); kernel (K187.27) therefore matches candidate
(187.K24)--(187.K25), including the repaired conductor condition.

## Multiplicity, atom counts, and powers

Kernel (K187.17)--(K187.22) reproduces candidate (187.K13)--(187.K19):

- fixed ((\kappa,g,h,U)) costs
  \(O_\varepsilon(LX^\varepsilon)) after summing both orientations,
  (v), and live affine sites;
- (U\ll L/(\kappa g)), (kappa g\ll L/h), and the dyadic
  ((h,\kappa g))-count is (O(L\log(2L)));
- with (u=gU), (n=gh), one has (u,v\asymp L/\kappa),
  (n\ll L/\kappa), and (h\ll U);
- at fixed ((\kappa,u,U)), the (O(U)) heights,
  (O(L/\kappa)) values of (v), and (O(\kappa)) live sites give
  (O(UL)) atoms across both orientations;
- exact conductor (q) has mass
  (O((q/U)\log(2q))), hence fixed-coordinate cost
  (O_\varepsilon(Lq\log(2q)X^\varepsilon)); and
- the nested divisors (q\mid U\mid u) give the same
  (O_{B,\varepsilon}(L^2X^\varepsilon)) low-conductor packet.

The remaining edge packet uses exactly the same full small-(U) Fourier mass
and (Q/U) ordinary-edge mass.  The exact complement uses the full
logarithmic Fourier mass and has only

\[
 |\mathscr R_{Y,Q}^{\sigma}|
 \ll_\varepsilon YL^2X^\varepsilon.
\]

Thus kernel (K187.9)--(K187.10) matches candidate
(187.K6)--(187.K7), including the complete surviving factor (Y).  No
coefficient smoothness, equidistribution, or variation estimate is inferred.

# First open step and proved/open boundary

The first open step is exactly kernel (K187.11), equivalently candidate
(187.K8):

\[
 \boxed{\Re\mathscr R_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\]

The kernel correctly calls the following, and only the following, proved:

- the exact Fourier/conductor decomposition;
- the complete (U=1), (q\le Q), and edge-mode target-safe packet;
- the positive (O(YL^2X^\varepsilon)) capacity bound for the exact
  complement; and
- the centered-conductor and positive-energy self-return controls.

It does not call the one-sided complement estimate, the complete high-height
block, or the original (t=1) residual proved.  The adversarial coefficient
control is correctly quarantined as a mechanism test and is not asserted to be
literal lower mass or a disproof of the open relation.

# State scope and recommendation

Accept the durable kernel at hash
`b9119e5d11e78d6ae45eca461f4acb2cdd9f6c49611612ee45e9f32f5dc27c74`
as consistent evidence for
`M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction` with status
`proved_internal`, under the sole exit label
`strict_high_h_inverse_residue_fourier_sector`.

Retain open the exact original-(t=1) residual, every original (t\ge2)
small-(G) incidence, the large-(G) near-resonant complement, both complete
hard and smooth M1 parents, GAR, every M2 parent, endpoint uniformity, M9, both
bridges, the quarter target, and every exponent claim.  No kernel, candidate,
graph, synthesis, validation-matrix, or proof-draft edit is licensed by this
review.
