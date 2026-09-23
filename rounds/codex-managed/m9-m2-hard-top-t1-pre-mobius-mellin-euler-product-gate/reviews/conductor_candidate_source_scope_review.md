# Source/interface review of the Round-168 conductor candidate

## 1. Result

**Final verdict: PASS.**  The repaired candidate makes no unsupported affirmative
call to Topacogullari, Bourgain, Ramana--Ramare, or
Durkan--Karak--Mahatab.  It correctly uses all four source families only
as negative interface tests, explicitly removes the unproved
approximate-functional-equation-to-Round-162-collar equivalence, and
limits the \(\sqrt J\) conclusion to two named absolute placements.  The
cardinal-interpolation residue proof (168.C14)--(168.C20) is
source-independent and valid.

The three requested repairs are present: \(\eta\) is selected after the
target \(\varepsilon\) and \(L^{2\eta}\) is carried through both capacity
ledgers; the exact source report and theorem list are cited as negative
scope checks; and (168.C22) is attributed to the blind statement-only
report rather than to Ramana--Ramare.  No source/interface defect remains.

## 2. Exact statement and hypotheses checked

### 2.1 Primary-source placement

1. **Topacogullari.**  In [*The fourth moment of individual Dirichlet
   L-functions on the critical line*](https://doi.org/10.1007/s00209-020-02610-9):

   - Theorem 2.1 is a pointwise bound for the common-height product
     \(L(s,\chi_1)L(s,\chi_2)\), with primitive characters,
     \(0\leq\Re s\leq1\), and \(|s-1|>\varepsilon\).
   - Theorem 2.2 puts the absolute value inside a common-height first
     moment and assumes \(q_1,q_2\leq T\).
   - Theorems 1.5--1.6 concern
     \(|\zeta_K(1/2+it)|^2\) for a quadratic field.  Theorem 1.6 formally
     permits a fixed smooth compactly supported complex weight, but its
     constant depends on that weight and no parameter-uniform seminorm
     is stated.
   - Theorem 2.7 is a common-\(s\) AFE.  It assumes primitive
     \(\chi_i\pmod {q_i}\), \(1/2\leq\sigma\leq1\), \(q_i\leq t\),
     \(4\pi^2xy=q_1q_2t^2\), and returns coefficients
     \(\tau_{\chi_1,\chi_2}\).  For \((q_1,q_2)=(1,4)\), balanced length
     is \(t/\pi\asymp JL\), but only on the diagonal \(s_1=s_2\).

   The candidate invokes none of these as a signed two-height estimate.
   Its statement that the inspected common-height pointwise, absolute
   moment, and AFE results do not prove (168.C7) is exact.

2. **Bourgain.**  The authoritative published consequence in
   [JAMS 30 (2017), p. 206](https://doi.org/10.1090/jams/860) is
   \(|\zeta(1/2+it)|\ll_\varepsilon t^{13/84+\varepsilon}\); it is
   pointwise and concerns \(\zeta\) alone.  The candidate does not use
   it affirmatively.  Instead it grants the strictly stronger
   Lindelof-size product majorant as a hypothetical capacity test.  That
   is correctly labelled stronger than known and is not a source call.

3. **Ramana--Ramare.**  Theorem 2.1 of
   [*Variant of the truncated Perron formula and primes in polynomial
   sets*](https://ramare-olivier.github.io/Maths/Perron-IJNT.pdf) assumes
   a Dirichlet series with finite convergence abscissa,
   \(\kappa>\max(0,\sigma_c)\), \(x\geq1\), and
   \(\phi,\widehat\phi\in L^1\) with \(\phi(0)=1\).  Its exact identity
   contains a second integral of local partial-sum differences.
   Corollary 2.2 retains a signed local boundary sum after truncation.
   The candidate does not cite this theorem to justify the cardinal
   interpolant; (168.C14)--(168.C17) are a separate direct construction.
   Its final statement that an exact Perron formula *without* its local
   correction is insufficient is therefore correctly scoped.

4. **Durkan--Karak--Mahatab.**  Theorem 1.1 of
   [arXiv:2606.27516v3](https://arxiv.org/abs/2606.27516v3) assumes GRH
   for the Dedekind zeta function of the common Galois closure, fixed
   fields, positive exponents in a compact subset of
   \((0,\infty)^r\), and shifts \(|b_i|\leq T/2\).  Its integrand is a
   product of positive powers of absolute values of Dedekind zeta
   functions.  It contains neither a negative zeta power needed to
   isolate \(L(s_1,\chi_4)\) at unequal heights nor the signed nonlinear
   transform or \(G\).  The candidate calls it only a conditional
   positive shifted-moment theorem and derives nothing from it.  This is
   source-safe.

### 2.2 Exact candidate claims under review

The reviewed affirmative claims are: the Euler factorization
(168.C3)--(168.C4); the exact cardinal Mellin identity
(168.C14)--(168.C17); the sole \(s_2=1\) residue and bound
(168.C18)--(168.C20); the two explicitly granted absolute-capacity
calculations; and the trivial fixed-polylogarithmic sector.  None relies
on a primary theorem beyond standard analytic continuation and functional
equations already encoded in \(L(s,\chi_4)\) and \(\zeta(s)\).

## 3. Proof or derivation

### 3.1 Source-interface reconciliation

The signed object in (168.C21) has independent heights and a
parameter-dependent complex weight.  Topacogullari's relevant results
are common-height and absolute/positive, Bourgain is pointwise for
\(\zeta\) alone, Ramana--Ramare retains endpoint corrections, and
Durkan--Karak--Mahatab is GRH-conditional with positive absolute powers.
Thus the candidate's sentence that the audited sources do not supply
(168.C7) is justified.  It does not infer that no bespoke signed theorem
exists.

The candidate also says explicitly that no coefficient bridge from
factorwise functional equations or AFEs to the Round-162 collar has been
proved.  Its only collar comparison deliberately reopens the original
projector by the already accepted Mobius--Poisson route.  Hence no
AFE-to-collar equivalence is asserted or smuggled into the proof.

### 3.2 Source-independent residue proof

The residue argument passes all literal checks:

1. Because \(\operatorname{supp}\psi\subset(-1/3,1/3)\), the cardinal
   cells are disjoint and
   \(\mathcal B(n,m)=A_{L,X}(n,m)e(J\sqrt{nm})\) at every integer pair.
   Hard values, floors, stars, and zero values are encoded in the samples
   of \(A_{L,X}\), rather than inferred from an ordinary interpolation
   across a discontinuity.
2. The sum in (168.C14) is finite, smooth, compactly supported away from
   both axes, and hence has an entire Mellin transform with rapid decay
   on each fixed vertical strip.  This is sufficient for the contour
   rectangle for each \((L,J)\); no uniform derivative claim is needed
   for the identity.
3. In \(\Re s_i>1/2\), \(G\) is holomorphic, \(L(s_1,\chi_4)\) is
   entire, and only \(\zeta(s_2)\) contributes the pole at \(s_2=1\).
   The local calculation in (168.C18) is exact.
4. On the initial \(s_1\)-line \(>1\), the coefficient expansion is
   absolute, so one-variable Mellin inversion gives (168.C19) without a
   conditional interchange.
5. On a cell \(n,m\asymp L\),
   \(\partial_z(2\pi J\sqrt{nz})\asymp J\), with no stationary point.
   Since \(\psi\) is compactly supported, one integration by parts has
   no boundary term and gives \(O(J^{-1})\) uniformly.  The residue
   coefficient has modulus at most one.
6. There are \(O(L^2)\) cells, so
   \(R_\zeta\ll L^2/J\).  Because \(L\ll H\asymp J^{1/2}\),
   \[
     \frac{L^2/J}{L^{3/2}}
     =\frac{L^{1/2}}J\ll J^{-3/4},
   \]
   and the residue is target-safe without character cancellation.

The different discrete residue in (168.C22) is not used to prove
(168.C6), and the candidate correctly warns that the two interpolations
must not be conflated.

### 3.3 The \(\sqrt J\) ledger and repaired \(\eta\) quantifier

At \(\alpha=1/2+\eta\), the favorable smooth radial transform has
pointwise scale \(L^{2\eta}\sqrt{L/J}\) on a band
\(T\asymp JL\), and radial \(L^2\)-norm \(L^{1+2\eta}\).  The repaired
candidate carries these factors explicitly, so both named capacity
calculations give

\[
 L^{2\eta}\sqrt J\,L^{3/2}X^\delta
\]

before epsilon management.  It now chooses
\(0<\eta\leq\min(1/8,\varepsilon/4)\) for a requested final exponent
\(\varepsilon\), keeps a separate auxiliary \(\delta>0\), and uses
\(L\leq X^{1/4+o(1)}\), whence

\[
 L^{2\eta}\leq X^{\eta/2+o(1)}.
\]

Thus \(L^{2\eta}\leq X^{\varepsilon/8+o(1)}\), and choosing \(\delta\)
sufficiently smaller than \(\varepsilon\) places
\(L^{2\eta}X^\delta\) inside the final \(X^\varepsilon\).  The earlier
fixed-\(\eta\) defect is fully repaired.

Apart from this quantifier, the candidate scopes the conclusion exactly:
it tests triangle inequality with a granted pointwise product majorant
and Cauchy with a granted fixed-angular mean square; it asserts neither a
lower bound nor a no-go for other signed placements.

## 4. First doubtful or unproved step

No remaining defect appears in the three re-reviewed interfaces.  The
candidate correctly leaves (168.C7), the genuinely signed two-height
estimate for polynomial \(L\), as the first open theorem.  It does not
claim that the favorable smooth/BV norm belongs to the unit-cardinal
transform, does not promote an AFE-to-collar correspondence, and does not
derive (168.C22) from a primary source.

## 5. Control tests and outcomes

| Control | Outcome | Finding |
|---|---|---|
| No unsupported primary-source call | PASS | All primary results are used only to delimit what is unavailable. |
| Topacogullari hypotheses/placement | PASS | Common height, absolute/positive moments, fixed-weight dependence, and AFE coefficient class are respected. |
| Bourgain implication | PASS | The candidate grants Lindelof hypothetically and does not misstate the published pointwise theorem as a hybrid estimate. |
| Ramana--Ramare implication | PASS | Cardinal interpolation is independent; the local Perron correction is not discarded. |
| Durkan--Karak--Mahatab implication | PASS | GRH-conditional positive shifted moments are not used as signed or quotient bounds. |
| AFE-to-collar equivalence | PASS | Explicitly unproved and absent from the deduction. |
| Named \(\sqrt J\) placements | PASS | The repaired ledger carries \(L^{2\eta}\), chooses \(\eta\) after \(\varepsilon\), and confines the no-go to triangle/pointwise and Cauchy/fixed-angular mean-square placements. |
| Cardinal identity | PASS | Exact at all lattice samples; derivative costs are not claimed analytic smoothing. |
| Residue local factors | PASS | (168.C18) agrees prime by prime, including \(p=2\). |
| Residue oscillatory bound | PASS | Nonstationary unit-cell integration gives \(J^{-1}\); \(O(L^2)\) cells give a target-safe \(L^2/J\). |
| Fixed-polylogarithmic sector | PASS | \(L^2=L^{3/2}L^{1/2}\), and fixed polylogarithmic \(L^{1/2}\) is absorbed into \(X^\varepsilon\). |
| Downstream/source scope | PASS | No polynomial-\(L\) target, parent, bridge, quarter theorem, or exponent is promoted. |
| Source and imported-artifact attribution | PASS | The candidate names the exact source report/theorems and attributes (168.C22) to `reports/blind_mellin_euler_rederivation.md`. |

Research allocation: 100% analytical/algebraic, 0% numerical.

## 6. Dependencies and exact artifacts used

- `rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/candidates/conductor_round168_mellin_euler_polylog_and_signed_moment_reduction.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/reports/hybrid_zeta_l_source_hostile_audit.md`;
- the exact primary theorem statements and URLs recorded in that source
  report: Topacogullari Theorems 2.1, 2.2, 1.5--1.6, and 2.7; Bourgain's
  published p. 206 consequence; Ramana--Ramare Theorem 2.1 and
  Corollary 2.2; and Durkan--Karak--Mahatab Theorem 1.1.

No shared state, candidate, synthesis, or other report was edited.

## 7. Recommended state effect and final verdict

**Recommended state effect: promote the candidate's scoped claims, subject
to the ordinary graph/seam process.  Final source/interface verdict:
PASS.**  The eta/epsilon ledger, exact primary-source attribution, and
blind Stieltjes attribution are repaired.  The source-independent bound
\(R_\zeta\ll L^2/J\), fixed-polylogarithmic full-scalar and
\(\kappa\)-dependent residual sector, and named-placement
\(\sqrt J\) capacity statement are source-safe.  No further repair is
required by this review, and no polynomial-\(L\), downstream, or exponent
claim is licensed.
