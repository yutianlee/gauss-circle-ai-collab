# Round 160 conductor controls

- Campaign: `m9-m2-unbalanced-inverse-selector-reciprocity-gate`
- Round: 160
- Starting graph: `4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d`
- Resulting graph: `7e68cfd355ef48407712d3216382a1a54a28be9a27ac9e15c3fd1e59e081a447`
- Terminal label: `inverse_selector_projective_capacity_no_go`
- Allocation: 100% analytic, algebraic, and primary-source verification; 0% numerical experimentation

## 1. Mathematical control ledger

| Control | Outcome |
|---|---|
| exact_inverse_selector_reciprocity | GREEN. For every coprime (j,n), arbitrary inverse representatives, and either parity of (j), (e(-h\overline j_n/n)=e(h\overline n_j/j-h/(jn))). |
| even_odd_j_and_representatives | GREEN. Representative changes alter the exponent by an integer, and the proof never divides by two. |
| centered_h_nonzero_once | GREEN. The only deleted row is (h=0\pmod n); every (1\le h<n), including positive (h=mj), remains. |
| full_h_self_return | GREEN/no-gain. Complete (h\bmod n) orthogonality reconstructs the original reciprocal row exactly. |
| primitive_g1 | GREEN. The projective and long-block capacities already occur at (g=1), so no outer-(g) cancellation is credited. |
| chi4_before_positive_norm | GREEN. The literal scalar retains (chi_4(g)\chi_4(n)) before every positive modulus norm. |
| moving_j_support_and_zero_extension | GREEN. The accepted kernel keeps the literal moving support, exits, profiles, real centre, gcd strata, and endpoints. |
| n_mod_j_class_price | GREEN for the exact unweighted kernel. Its Gram matrix is (jI-\mathbf1\mathbf1^*). |
| projective_Sobolev_Bessel_norms | GREEN/scoped. Exact Hilbert rank-one scalarization plus termwise triangle pays the nuclear norm; high additive bandwidth is only a finite diagnostic until matched to a printed theorem. |
| long_h_complement | GREEN as an operator capacity. The exact compression norm is (\sqrt{\lceil(n-1)/j\rceil}\asymp\sqrt\Delta); this is not a signed lower bound. |
| level_four_eight_spectral_ledger | GREEN/no-match. Every compatible induced level and holomorphic, Maaß, exceptional, Eisenstein, newform, oldclass, and cusp contribution remains charged. |
| boundary_power_saving | GREEN pointwise in the strict region. Both the scalar projective price and long-block capacity exceed the entire missing power; no open-face-uniform margin is claimed. |
| source_theorem_literal_match | GREEN/no owner-saving scalar match through 25 August 2026. Every cited theorem is confined to its printed scalar hypotheses. |
| moving_literal_weighted_lower_bound | OPEN. The frozen hypotheses provide no nonzero lower buffer with complete unit-class coverage, and no unweighted-to-entrywise-Kloosterman lower-bound transfer is valid. |
| bespoke_vector_theorem | OPEN. The finite obstruction does not exclude a new theorem acting on the complete signed weighted matrix before positive norms. |
| flat_owner_and_downstream_scope | GREEN. No target, strict range, other owner, endpoint theorem, M9, bridge, or exponent is promoted. |

## 2. Exact accepted proof kernel

For (A\subseteq(\mathbb Z/j\mathbb Z)^\times), (M=|A|), and

\[
 F_{j,A}(u,h)=e(h\overline u_j/j),\qquad 1\le h\le j-1,
\]

the accepted kernel proves

\[
 F_{j,A}F_{j,A}^*=jI_M-\mathbf1\mathbf1^*.
\tag{160.CT1}
\]

Thus its singular values are (\sqrt j) with multiplicity (M-1) and
(\sqrt{j-M}) once. For all unit classes, exact Hilbert scalarization
followed termwise by triangle has nuclear-to-Hilbert--Schmidt inflation
(\sqrt{\varphi(j)}=j^{1/2-o(1)}). The normalized positive block
(1\le h\le j) has orthonormal rows.

The literal (1\le h<n) range also has the exact residue-compression norm

\[
 \|P_{n,j}\|_{2\to2}
 =\sqrt{\left\lceil\frac{n-1}{j}\right\rceil}
 \asymp\sqrt\Delta.
\tag{160.CT2}
\]

At (g=1), (j\asymp K), these capacities are respectively
(K^{1/2-o(1)}) and (X^{a/2}), each larger than the missing boundary
factor at every fixed strict exponent pair. This certifies only the named
scalarization and audited scalar-route obstruction.

## 3. Exact scope boundary

The exact finite matrix is unweighted. The accepted profile facts supply
upper bounds, regularity, support, and zero extension, but no interval on
which the complete joint amplitude is uniformly bounded below while every
unit class occurs. Even a future buffer theorem would not show that
entrywise interaction with (S(N_0,h;n)) preserves a nuclear lower bound.
Therefore no literal weighted-matrix lower bound, signed-sum lower bound,
or vector-method impossibility is recorded.

The first open positive theorem is a signed vector estimate for the entire
((g,n,j,h)) matrix, retaining both characters, the Kloosterman coefficient,
all positive frequencies, moving support and endpoints, arbitrary gcd and
two-adic strata, and every induced spectral level, with the required
(X^{\mu(a)}) gain.

## 4. Independent reviews

- the statement-only blind rederivation independently verifies reciprocity, reconstruction, residue rank, and the long-frequency issue;
- the post-blind seam review accepts the exact unweighted result and rejects an unconditional weighted transfer;
- the exact-kernel and power review independently reproduces the spectrum, long-block norm, and both boundary comparisons;
- the source-level review accepts the scalar no-match after parity-by-level, long-complement, and (chi_4)-encoding repairs; and
- the scope/hygiene review's requested route, weight, source, totient, metadata, and evidence repairs are incorporated in the accepted kernel and adjudication.

The terminal State Patch scope review is GREEN. It found all dependencies
and evidence, no return path or cycle, and no target, range, owner, weighted-
matrix, vector-method, downstream, or exponent overpromotion. After a
scope-narrowing repair that printed the frozen
(178\ell+1638\delta>463) hypothesis, the reviewer reran the dry validator
and retained the GREEN verdict.

## 5. Pre-mutation validation

- starting graph SHA-256: PASS;
- exact algebra reproduced independently: PASS;
- primary-source seam: PASS after printed repairs;
- strict campaign/kernel hygiene scan: PASS before State Patch drafting;
- MathJax preview rendering: PASS on all 18 then-existing campaign and
  kernel Markdown files; and
- numerical evidence: none used.

The graph and State Patch dry validators, active-campaign validator, and
terminal State Patch scope review passed before mutation.

## 6. State mutation

The validated State Patch applied:

- 1 obligation creation;
- 4 obligation updates;
- 15 rejected inferences; and
- 11 no-change decisions.

The graph validator passed after mutation. The resulting SHA-256 is
`7e68cfd355ef48407712d3216382a1a54a28be9a27ac9e15c3fd1e59e081a447`.
The proof draft was refreshed only after this graph mutation.

## 7. Downstream decision

Close under `inverse_selector_projective_capacity_no_go`. Park this exact
flat-UNBAL scalar surface. Reopen it only with a genuinely new signed
literal-matrix vector theorem; otherwise rotate to a different mandatory
M2 owner. The global proof and every exponent remain unchanged.

Complete closure validation passed:

- completed-campaign and patched-graph validators: PASS;
- seven structured JSON/YAML files: 7/7 parse;
- Python compilation: PASS;
- unit tests: 6/6 PASS;
- whitespace diff check: PASS, with repository line-ending policy warnings
  only;
- final campaign and kernel scan: PASS on 19 Markdown files with 297
  per-file-unique equation tags, 368 balanced bracket-display pairs, zero
  double-dollar tokens, and no byte, line-ending, whitespace, delimiter, or
  tag issue;
- final MathJax preview rendering: PASS on all 19 campaign and kernel
  Markdown files; and
- expanded closure hygiene scan: PASS on 34 campaign, kernel, proof-draft,
  manifest, directive, and state files.

The strict scans require valid UTF-8, LF-only files, no BOM, forbidden C0
or DEL byte, replacement, zero-width or directional code point, missing
final newline, trailing whitespace, duplicate per-file equation tag, or
unbalanced display delimiter.
