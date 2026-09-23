# Round 187 final kernel formalization/provenance post-repair verification

## 1. Result / verdict

**GREEN.** The current durable kernel is frozen at SHA-256

a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2.

Every requested formalization and provenance repair is present, the
current diagnostic hashes match the files on disk, and no mathematical
content or promotion scope changed. The earlier hash
026b9709bba25251c4030bd8475a35710c8c1c25cd9d103e0172821bd694ce24
was an intermediate repaired kernel containing two mistyped diagnostic
hash strings; correcting only those strings produced the current hash.

## 2. Exact delta replay

A byte-level reverse replay was performed in memory.

1. Removing the provenance header, standard-symbol definitions, exact
   \(U=1\) formula, \(\mathbb U(q)\), \(\mu\), and \(\tau\)
   definitions, blind-attribution paragraph, and diagnostic-provenance
   block;
2. removing the added inline delimiters; and
3. reversing only the requested restored command slashes

reconstructs a 9,492-byte file with SHA-256

b9119e5d11e78d6ae45eca461f4acb2cdd9f6c49611612ee45e9f32f5dc27c74

exactly. Thus the full delta from the frozen pre-repair kernel is
precisely the requested formalization/provenance delta.

Separately, replacing the two current diagnostic hashes by the two
mistyped intermediate strings reconstructs SHA-256

026b9709bba25251c4030bd8475a35710c8c1c25cd9d103e0172821bd694ce24

exactly. Hence the final change from 026b...ce24 to a914...92f2 is
only the correction of those two provenance strings.

## 3. Formalization and reference checks

All requested checks pass:

- strict UTF-8 decoding: PASS;
- BOM: absent;
- NUL and other control characters: zero;
- line endings: LF, with a terminal line feed;
- inline TeX delimiters: 73 openings and 73 closings;
- display delimiters: 36 openings and 36 closings;
- aligned environments: two openings and two matching closings;
- tags: exactly one each of (K187.1)--(K187.27), with no gap or
  duplicate;
- internal K187 references: no undefined target;
- inherited references: (K185.27) and every tag
  (K185.30)--(K185.35) exist in the accepted parent kernel.

The previously missing \(\sigma\), \(\mathscr\), \(\mathbb\),
\(\sum\), and \(\mathcal\) command slashes are restored. All
mathematical prose spans identified by the prior review now use valid
inline delimiters.

The kernel now explicitly defines

\[
 e(x)=e^{2\pi i x},\qquad [x]_U,\qquad
 \bar vv\equiv1\pmod U,
\]

\(\mathbb U(q)=(\mathbb Z/q\mathbb Z)^\times\) for \(q>1\),
\(\mathbb U(1)=\{0\}\), the exact complete
\(\mathscr U_{1,Y}^{\sigma}\) sum, and the functions \(\mu\) and
\(\tau\). These definitions agree with the candidate and inherited
carrier.

## 4. Provenance, dependencies, and attribution

The new header correctly records:

- campaign and Round 187;
- starting graph hash
  d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a;
- current candidate hash
  c2f01f57a41695d73d0d1f9716a03328147dbe79f0fcdeb7e8e3465b29779b89;
- current reconciliation hash
  b3de83554db114db91b33a8e994f0daa3cd9d9c41550eceabd575fbca1250705;
- durable-candidate status pending State Patch validation; and
- numerical theorem evidence: none.

Every listed evidence path exists. The diagnostic paths and hashes now
match exactly:

| Artifact | SHA-256 |
|---|---|
| controls/conductor_round187_wolfram_inverse_residue_check.md | 032d8039636b0e4e2040caed7c0d2ade507d111a7f966b9b40f03676fadd1113 |
| controls/inverse_residue_exact_check.wls | e818367a710c4051f9259966133ca48b94810a55544b4b0ec3d3fbab15a06bcd |

The kernel explicitly says these finite checks are diagnostic only.
No asymptotic theorem claim depends on them.

Blind attribution is now exact: the blind report supports the direct
small-modulus and ordinary-edge packet but not the complete small
exact-conductor packet; the stronger packet is attributed to the
discovery and hostile derivations plus independent seam review.

The direct accepted dependencies remain exactly
M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction and
Divisor-bound-elementary. No external theorem, web result, or hidden
coefficient regularity is imported.

## 5. Mathematical and nonpromotion replay

The repair does not alter any tagged equation. Kernel
(K187.8)--(K187.11) still matches candidate (187.K1)--(187.K8);
(K187.12)--(K187.22) still matches candidate
(187.K9)--(187.K19); and (K187.23)--(K187.27) still matches
candidate (187.K20)--(187.K25).

The proved content remains only:

- the exact \(U=1\)/low-conductor/edge/high decomposition;
- the absolute target-safe packet (K187.9);
- the positive \(YL^2X^\varepsilon\) capacity bound (K187.10); and
- the centered-conductor and positive-energy self-return controls.

The first unproved relation remains exactly

\[
 \Re\mathscr R_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{K187.11}
\]

The one outer real part, both orientations, every literal endpoint
field, and the exact complement remain unchanged.

## 6. Frozen hashes

| Artifact | SHA-256 |
|---|---|
| Current durable kernel | a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2 |
| Pre-repair durable kernel | b9119e5d11e78d6ae45eca461f4acb2cdd9f6c49611612ee45e9f32f5dc27c74 |
| Intermediate repaired kernel | 026b9709bba25251c4030bd8475a35710c8c1c25cd9d103e0172821bd694ce24 |
| Parent tangent-gcd kernel | 4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160 |
| Current candidate | c2f01f57a41695d73d0d1f9716a03328147dbe79f0fcdeb7e8e3465b29779b89 |
| Reconciliation | b3de83554db114db91b33a8e994f0daa3cd9d9c41550eceabd575fbca1250705 |
| Discovery report | 4433de37846caa4c9ae0d51ba874221851a331e4a6af13043d4da0f0749ac298 |
| Hostile report | 5a09310baf8574bf1f2c841cd179a66d22aa5834cc50be555a11ad969569db1a |
| Blind report | abaf181178b56925bec5fa6b624ddd79be528f4e419e2bff7f22adf9593b9992 |
| Proof graph | d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a |
| Active campaign | aadf701b1725cdd0004bb29e1fc625754e391e5475130df3a08a2a2e18d761d3 |

## 7. Recommended state effect

Accept the current durable kernel at
a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2
as GREEN evidence for the proved-internal node
M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction, subject
to the conductor's mechanical State Patch and graph/lifecycle
validation.

Retain (K187.11), the complete high-height target, the complete
original-\(t=1\) residual, every original \(t\ge2\) and large-\(G\)
incidence, both M1 parents, GAR, all M2 parents, endpoint uniformity,
M9, both bridges, the quarter target, and every exponent claim open.
This review authorizes no direct graph, synthesis, candidate,
validation-matrix, proof-draft, or state edit.
