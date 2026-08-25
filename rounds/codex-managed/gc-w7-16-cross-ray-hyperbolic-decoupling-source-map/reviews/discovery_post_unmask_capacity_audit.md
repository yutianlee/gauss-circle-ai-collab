# Round 132 post-unmask review: normalization and capacity audit

Campaign: `gc-w7-16-cross-ray-hyperbolic-decoupling-source-map`

Role: discovery post-unmask reviewer

Starting graph SHA-256:
`328a885e71415a8e3509466c46849129248594334dc17df8940bbcd3f12a0fe9`

## 1. Result

The four records are mathematically compatible after distinguishing the
whole-shell chart from a determinant-band rescaling.  Their exact affine
charts are equivalent, and the two advertised physical radii refer to
different coordinates:

\[
 P_i={cL\over\kappa_iD}=Y^{32/48+o(1)}
 \tag{132.R1}
\]

is the evaluation scale in the bounded whole-shell hyperbolic coordinates,
while, on an \(\eta\)-difference band of width \(h\), the anisotropic
hyperbolic dilation gives the reciprocal-phase scale

\[
 R_h=P_i h.
 \tag{132.R2}
\]

At the widest determinant band
\(h\asymp h_*:=\kappa_iD/(WL)=Y^{-5/48+o(1)}\), this becomes

\[
 R_{h_*}={c\over W}=Y^{27/48+o(1)}.
 \tag{132.R3}
\]

Thus \(P_i\) and \(c/W\) are not competing normalizations.  The discovery
report's phrase “exact source scale” for \(c/W\) is too strong: (132.R3) is
the exact **rescaled physical evaluation scale**, but it becomes a source
radius only after an explicit Fourier thickening, Euclidean-neighborhood
check, spatial localization, and coefficient normalization.

The exact broad geometry is available only after this band rescaling and a
small-patch partition.  It requires separation in both

\[
 {|b-b'|\over D}\asymp1,
 \qquad
 {Wn\over\kappa_i bb'}\asymp1.
 \tag{132.R4}
\]

The same-denominator family remains an exact ruling and never satisfies the
bilinear transversality hypothesis.  On a rescaled broad pair, the first
unclosed interface is the owner-preserving factorization/projective norm of
the joint coefficient matrix; after a factorization, a generic fixed-point
kernel bridge exists but yields only the positive Demeter--Wu square
function and no negative power.

The capacity verdict in the discovery report is correct when read as an
**upper-capacity ledger**, not as actual resonant mass:

\[
 Y^{35/48}\quad\longrightarrow\quad Y^{27/48}
 \quad\longrightarrow\quad Y^{24/48}.
 \tag{132.R5}
\]

The main-source theorems do not close either the joint-coefficient/fixed-point
seam or the narrow ruling.  The scoped terminal label
`source_level_no_go` is therefore retained.

## 2. Exact reconciliation of charts and hypotheses

The conductor and discovery charts coincide:

\[
 \xi={b\over D},\qquad
 \eta=-{Da\over Lb},\qquad
 \zeta=-{a\over L},\qquad \zeta=\xi\eta.
 \tag{132.R6}
\]

The blind chart starts from \(z=u/v\), recentres
\((u,v,z)\) at \((u_0,v_0,z_0)\), and uses

\[
 \xi_B={v-v_0\over D},\quad
 \eta_B={z-z_0\over L/D},\quad
 \rho_B={u-u_0-v_0(z-z_0)-z_0(v-v_0)\over L},
 \quad \rho_B=\xi_B\eta_B.
 \tag{132.R7}
\]

Equations (132.R6) and (132.R7) differ only by sign, bounded translation,
coordinate permutation, and the standard affine shear that recentres
\(\mathbb H\).  The blind preliminary representation
\(q(u,v)=(u,v,u/v)\), evaluated at a vector of size \(c\), is likewise
consistent: after scaling the shell to bounded coordinates, the
contragredient evaluation vector has size \(P_i=cL/(\kappa_iD)\).
Physical Euclidean radius is coordinate-dependent until that bounded
normalization is fixed.

For a literal pair,

\[
 \eta_{r'}-\eta_r={Dn\over Lbb'}ll {D\over LW}=Y^{-5/48+o(1)}.
 \tag{132.R8}
\]

Accordingly, the blind claim that the whole determinant support is narrow
under a bounded-condition whole-shell normalization is correct.  The
conductor's dilation

\[
 (\xi,\eta,\xi\eta)
   =(\widetilde\xi,h\widetilde\eta,
     h\widetilde\xi\widetilde\eta)
 \tag{132.R9}
\]

does not contradict it: (132.R9) has condition number \(h^{-1}\) and is a
band-dependent zoom.  It changes the evaluation scale from \(P_i\) to
\(P_ih\).  On the widest band it gives exactly the discovery cell map and
(132.R3).

There are two distinct ruling/narrow statements, both valid:

1. the complete determinant relation is close to an
   \(\eta=\mathrm{constant}\) ruling because (132.R8) is small; and
2. the same-denominator control has \(\xi_{r'}=\xi_r\) exactly and lies on
   the other ruling family.

After an \(\eta\)-zoom, item 1 has a broad subpart only when the normalized
\(\eta\)-separation is constant-sized; item 2 remains narrow under every
such zoom.  Definition 1.2 also requires the separation for **every** point
in the two patches, so (132.R4) must be implemented with dyadic determinant
bands and sufficiently small separated subpatches, not with an undivided
ratio cell.

## 3. Seam and capacity derivation

The source card resolves the theorem direction exactly.  Theorems 1.6 and
1.10 start with two already-constructed independent functions.  Expanding
their product produces a rank-one pair coefficient; a sum of products
produces a projective tensor decomposition.  The physical Round-131 matrix

\[
 B_i(r,r')=A_i(r)H_{i;r,p}(n)C_{i;r,p}(n)
 \tag{132.R10}
\]

is joint in both rays through the lift selector, variable primitive moduli,
Möbius/Stieltjes profiles, thresholds, taper, stars, aliases, cells, signs,
and owners.  All reports agree that the tautological row or SVD
decomposition is not enough: its positive projective/nuclear cost is
uncontrolled by

\[
 \|A_i\|_1\ll D,qquad \|A_i\|_2^2\ll D/L.
 \tag{132.R11}
\]

This is the first missing hypothesis on a geometrically valid broad band.

The source card correctly says that no fixed-centre bridge is stated in the
paper.  The blind and discovery reports add the same project-level generic
bridge: because the Fourier support of an already-factorized product is
bounded, a reproducing kernel gives

\[
 |F_1(x_c)F_2(x_c)|
 \ll R^\varepsilon
 \mathcal D_R(F_1)\mathcal D_R(F_2),
 \quad
 \mathcal D_R(F)^2=\sum_\theta\|F_\theta\|_4^2.
 \tag{132.R12}
\]

Thus point evaluation is not logically impossible; what is absent is an
affordable arithmetic bound for the positive right side.  The discovery
cap-wave-packet realization, with \(L^4\)-size \(R^{1/2+o(1)}\) for an
amplitude-one packet, is a valid illustrative upper cost.  It is not a
universal lower bound on every possible embedding, and the discovery report
properly included that caveat.

For refined decoupling, the discovery wording that incidence is “maximal”
is an overclaim.  The exact conclusion is only that every packet contributing
at \(x_c\) meets the \(R^{1/2}\)-ball containing \(x_c\), so the theorem
charges the positive local counts \(M_j(Q_c)\).  Those counts are
uncontrolled by the packet, but they need not equal the total global packet
count or be polynomially maximal.

The accepted capacity calculation remains

\[
 C={WL\over D}=Y^{5/48+o(1)},qquad
 R_0={D\over W}=Y^{3/48},
 \tag{132.R13}
\]

\[
 D R_0{K_D\over L}=Y^{30/48+o(1)}quad\text{per aligned cell},
 \qquad
 C D R_0{K_D\over L}=DK_D=Y^{35/48+o(1)},
 \tag{132.R14}
\]

\[
 {DK_D\over L}=Y^{27/48+o(1)},qquad D=Y^{24/48}.
 \tag{132.R15}
\]

Equations (132.R14) are worst-case triangle capacities.  They neither prove
that all narrow cells are occupied coherently at the prescribed centre nor
give a family lower bound.  They do prove that the presently available
narrow estimate has no sub-\(27/48\) margin.  Consequently, granting the
broad contribution for free still does not prove a better complete bound.

## 4. First doubtful or overclaimed steps

The ordered audit is as follows.

1. **Naive whole-shell route.**  The first false step is
   “nonzero Hessian implies source transversality.”  Equation (132.R8)
   refutes it.  The blind report is correct at this scope.
2. **Band-rescaled broad route.**  Once (132.R9), Fourier support, and small
   separated patches are supplied, the first unproved step becomes the
   owner-preserving factorization/projective-norm bound for (132.R10).  The
   discovery report is correct at this later scope.
3. **Source radius wording.**  Calling \(R=c/W\) an “exact source scale” is
   too strong.  It is the exact reciprocal-phase radius after the widest-band
   dilation.  Transporting an Euclidean \(N_{1/R}\) neighborhood through
   the anisotropic map, or constructing a new one after the map, requires a
   separate thickening and normalization lemma.
4. **Smaller determinant bands.**  The discovery statement
   \(R_j=2^{-j}c/W\) down to \(R_j\asymp1\) is correct only for the
   reciprocal phase.  If the M1/M2 quarter carriers are encoded as physical
   coordinate shifts, the actual containing ball is at least
   \(\max(R_j,D,L)\).  Alternatively they may remain literal one-index
   coefficients, but that choice must be made before claiming a source
   radius.
5. **Refined incidence.**  “Maximal” should be replaced by “positive and
   uncontrolled local incidence,” as explained after (132.R12).
6. **Narrow handling in the source.**  It would be an overclaim to say the
   paper has no narrow mechanism.  The source card records linear Theorem
   2.4 and pointwise Proposition 4.11, which retain horizontal/vertical
   rectangle terms.  Those positive rectangle norms do not estimate the
   literal signed scalar, so they do not change the present no-go.
7. **Capacity language.**  “The narrow term retains \(35/48\)” is legitimate
   only as “the best available complete upper-capacity ledger is
   \(35/48\).”  It must not be read as an actual narrow lower bound.  The
   discovery and blind reports explicitly disclaim such a lower bound.

With these corrections, no contradiction remains among the reports.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| exact chart comparison | Pass: (132.R6) and (132.R7) are affinely equivalent exact charts, not Hessian approximations. |
| \(P_i\) versus \(c/W\) | Reconciled: whole-shell evaluation radius versus widest determinant-band reciprocal-phase radius.  Neither alone supplies Fourier thickness. |
| two-coordinate transversality | Pass only after band zoom and small-patch separation as in (132.R4); same denominator remains an exact ruling. |
| source rescaling hypotheses | Open at the project seam: anisotropic preservation of \(\mathbb H\) is exact, but Euclidean neighborhood thickness, caps, ball, Jacobian, and coefficient realization still require proof. |
| coefficient factorization | Red: the joint projective norm of (132.R10) is unavailable; row energy changes the signed interface. |
| fixed-point bridge | Generic kernel bridge passes for an already-factorized product, but has no negative power and leaves positive cap/packet norms uncontrolled. |
| refined incidence | Corrected to positive, uncontrolled local incidence; no automatic smallness or maximality. |
| ruling/narrow source treatment | Source retains narrow rectangles positively; no literal arithmetic narrow estimate follows. |
| \(35/48\), \(27/48\), \(24/48\) | Pass as upper-capacity, persistence, and determinant-target ledgers; the additional post-floor requirement is \(Y^{-3/48}=Y^{-1/16}\). |
| absolute-value direction | Pass: no positive square function, rectangle energy, row energy, or arbitrary coefficient norm is substituted for the actual scalar. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

This post-unmask review used only:

1. `reports/demeter_wu_exact_source_card.md`;
2. `reports/blind_pointwise_transversality_feasibility.md`;
3. `candidates/conductor_exact_hyperbolic_normalization.md`;
4. `reports/literal_ratio_phase_hyperbolic_map.md`; and
5. the campaign's already supplied Round-132 statement and protocol context.

No original report, shared graph, state file, plan, synthesis, validation
file, or sibling review was edited.

## 7. Recommended state effect

Retain the exact affine chart and record both scales with their scopes:
\(P_i=cL/(\kappa_iD)\) for the bounded whole-shell chart and
\(R_h=P_ih\), in particular \(R_{h_*}=c/W\), for a determinant-band zoom.
Describe the latter as a candidate source radius pending the full Fourier
thickening and coefficient map.

Retain `source_level_no_go` for direct use of Demeter--Wu Theorems 1.6 and
1.10 on the current literal scalar.  The geometrically transverse broad
subpart still lacks the owner-preserving projective coefficient bound and an
affordable positive-norm pointwise realization; the exact ruling/narrow part
still lacks an arithmetic estimate.  Keep the complete upper capacity at
\(Y^{35/48+\varepsilon}\), the persistence threshold at \(27/48\), and the
determinant target at \(24/48\).  Make no global exponent, M9 component,
endpoint, bridge, or quarter promotion.
