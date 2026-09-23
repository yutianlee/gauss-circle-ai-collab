# Round 166 full-graph frontier strategy audit

- Campaign: `full-proof-round164-166-strategy-literature-review`
- Task: `full_graph_frontier_strategy_audit`
- Role: discovery / full-graph strategy
- Starting graph: `87d58660e7e11a23eb3d8759917e02376479ba38acaf727b0a2dc15d5920f5e0`
- Date of strategy and source check: 2026-08-26
- Status: candidate strategy evidence only; no proof-state mutation is licensed

## 1. Result

### 1.1 Strategy result

The authoritative graph has exactly two quarter-level routes:

1. the **standard blockwise route**, which requires the conjunction of both direct M1 parents, all three M2 parents, and endpoint-uniform blockwise assembly; and
2. the **GAR alternative**, which replaces both direct blockwise M1 parents by the complete global angular--radial theorem, but still requires all three M2 parents and does not prove `M9-M1` or `M9`.

No currently open local inequality closes either route by itself. In particular, neither residual Fejer theorem closes hard TOP, neither hard-TOP result transfers to BAL or UNBAL, GAR does not transfer to a blockwise M1 node, and endpoint uniformity is not an independent analytic substitute for any parent.

Among the lawful next inequalities, the highest-leverage *round-sized* frontier is still the minimal-scale residual Fejer aggregate

\[
 \boxed{
 \Re\mathfrak C_{R_0,2,{\rm opp},\,g<\gamma L}^{\rm rem}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon,
 \qquad R_0=\lceil L\rceil .}
 \tag{167.F}
\]

The reason to retain (167.F), rather than merely repeat Round 165, is that a genuinely new candidate source model is now identifiable: a **joint spectral treatment of the determinant equation**

\[
 d'm'-dm=r
\]

after the exact signed divisor opening but before any shiftwise modulus, rowwise completion, or positive majorization. Grimmelt--Merikoski, arXiv:2404.08502v2, Theorem 10.1, is a concrete primary-source model for such a multi-orbit determinant treatment. It is not an accepted dependency and is not assumed applicable. Its exact coefficient, smoothness, orbit-correlation, modulus, two-adic, main-term, and restored-power requirements must pass the promotion gate below.

The resulting ordered priority is:

1. (167.F), with one exact Grimmelt--Merikoski source-to-literal-interface/no-go gate; a bespoke determinant-kernel statement is allowed only if it is the literal formulation extracted inside that same gate;
2. the maximal-scale medium/long Fejer theorem (165.K26);
3. a direct complete residual scalar theorem;
4. a direct complete hard-TOP parent shortcut (distinct from estimating only the remaining nonresidual channels);
5. GAR;
6. the hard direct M1 parent;
7. the smooth direct M1 parent;
8. BAL;
9. UNBAL;
10. the separate \(W=Y^{7/16}\) sub-one-third determinant lane; and
11. endpoint uniformity, which is an assembly seam and is not presently selectable as a stand-alone inequality.

This ranking is not a claim that (167.F) is true or that Grimmelt--Merikoski proves it. It says that (167.F) is the smallest exact, mechanistically specified aggregate frontier whose determinant skeleton matches a concrete candidate source model without silently enlarging the owner.

### 1.2 Terminal label

The recommended Round-166 closing label is

\[
\boxed{\texttt{strategy\_frontier\_retained}.}
\]

No mathematical status and no certified exponent should change.

## 2. Exact statement and hypotheses

### 2.1 Frozen Round-167 inequality

Let \(J=\sqrt X\), retain the complete literal Round-164 residual coefficient

\[
 c_N^{\rm rem}
 =\sum_{\substack{d\mid N\\2\nmid d}}
   \chi_4(d)\lambda_N(d),
\]

with the neither/both residual selector (or the no-pair value one), the squarefree and coprime conditions, both parity branches, Vaaler taper, profiles, floors, stars, hard point value, support crossings, endpoint conventions, and zero extension. On its support,

\[
 N\asymp L^2,\qquad d,N/d\asymp L,
 \qquad |\lambda_N(d)|\ll1,
\]

and the accepted diagonal estimate is

\[
 D_L:=\sum_N|c_N^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\]

Put \(z_N=c_N^{\rm rem}e(J\sqrt N)\), let
\(R_0=\lceil L\rceil\), and define

\[
 \mathfrak C_{R_0}
 =\sum_{1\le r<R_0}\left(1-\frac r{R_0}\right)
   \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
   e\!\left(J(\sqrt{N+r}-\sqrt N)\right).
\]

The subscript \(2,{\rm opp},g<\gamma L\) means simultaneously:

- \(r\) is even;
- after the literal divisor opening,
  \((d'-d)(m'-m)<0\), where \(N=dm\) and \(N+r=d'm'\);
- \(g=(d,d')<\gamma L\), for one fixed \(0<\gamma<1\); and
- all other literal weights and one outer real part are unchanged.

The sole Round-167 analytic target is (167.F). It may be dyadically decomposed internally in \(r\), determinant size, gcd, two-adic valuation, or smooth support, but every piece must be recombined before the final real part and the total must be (167.F). No dyadic or source-model estimate is itself the promotion target.

### 2.2 Exact implication and scope

The already proved Round-165 identities give

\[
 \mathfrak E_{R_0}\le 2\mathfrak E_{R_0}^{(2)},
 \qquad
 |\mathcal S_{L,1}^{\rm rem}|^2
 \le {M_L+R_0-1\over R_0}\mathfrak E_{R_0},
 \qquad M_L\asymp L^2.
\]

The monotone tangent sector costs \(O(L^2)\), and the fixed-fraction high-divisor-gcd sector costs \(O_\gamma(L^2X^\varepsilon)\). Therefore (167.F), together with the accepted diagonal, implies only

\[
 |\mathcal S_{L,1}^{\rm rem}|
 \ll_{\gamma,\varepsilon}L^{3/2}X^\varepsilon.
\]

It does not by itself prove the full \(t=1\) assembly, any other few-point channel, a near-collision collar, either hard-TOP parent, BAL, UNBAL, `M9-M2`, either M1 route, endpoint uniformity, `M9`, or a global exponent.

### 2.3 Promotion gate

Promotion of (167.F) requires all of the following.

1. **Literal determinant dictionary.** Opening both residual coefficients must give an exact multiplicity-preserving equality with the matrix family of determinant \(r=d'm'-dm\). Every multiplicity must be one or be carried by an explicit restoring weight, and every selector, squarefree mask, profile, star, endpoint, and parity label must be owned exactly once.
2. **Signed absolute-value placement.** The proof must estimate the single aggregate real part. No modulus may be inserted around an individual shift, gcd row, determinant orbit, Möbius opening, or spectral component unless its full cost is proved target-safe.
3. **Frozen source-to-interface match.** The literal weight must be represented in the class \(\mathcal A(q_1,q_2,\chi,\xi)\) of Grimmelt--Merikoski Theorem 10.1, or the audit must extract the exact literal determinant-kernel statement whose failure is being tested. Its \(C^7_\delta\) support must include the square-root phase at an admissible seminorm cost, the determinant factorization \(r=hk\) and \(\gcd(h,kq)=1\) must cover every even shift, and the orbit correlation \(\mathcal K_+\), main term, \(\mathcal R_0,\mathcal R_1,\mathcal R_2\), boundary, and completion costs must sum to \(O(L^2X^\varepsilon)\). At the first failed source class or fixed positive restored-power gate, the round stops rather than pivoting to a second mechanism.
4. **False controls.** The claimed mechanism must fail on the phase-aligned arbitrary-coefficient control at the unfiltered or filter-erased Fejer level, where the energy is \(\asymp L^3\). This is not a literal counterexample to the post-opening \({\rm opp},g<\gamma L\) sector unless an explicit incidence-level lift is constructed. The proof must explain which actual residual selector or \(\chi_4\) structure supplies the saving.
5. **Uniformity.** The estimate must be uniform in the real centre, the hard support crossings, the two-adic strata, the fixed \(\gamma\), and all physical labels inherited by the hard-top block.
6. **Validation.** A statement-only independent rederivation, a source-hypothesis review if applicable, a power/endpoint seam review, and graph-scope review must all be green before a State Patch can promote anything.

### 2.4 Stop rule

Stop Round 167 with a scoped no-go, and do not pass automatically to (165.K26), if any first unavoidable step does one of the following:

- the residual selector cannot be placed in an automorphic/periodic coefficient class without a projective or orbit-correlation cost of a fixed positive power;
- the square-root phase forces a \(C^7_\delta\), cell-count, or boundary cost that consumes the \(L\)-saving between the \(L^3\) positive capacity and the \(L^2\) target;
- the even-shift/two-adic decomposition fails the determinant-factor and gcd hypotheses on a non-target-safe stratum;
- the theorem yields only a shiftwise absolute, positive energy, or separated spectral norm;
- the main term or any \(\mathcal K_+\), \(\mathcal R_j\), Möbius, modulus, endpoint, or completion term exceeds \(L^2X^\varepsilon\); or
- the argument would also prove the known false arbitrary-coefficient analogue.

The no-go must identify the first failed hypothesis and its exact power. It must not be inflated into a no-go for all spectral or determinant methods.

## 3. Proof or derivation

### 3.1 Complete quarter-proof dependency trees

The standard tree is

```text
GC-target
`-- Conditional-bridge  [derived under assumptions]
    |-- H1-H3            [proved internal]
    |-- H4 + source audit[proved external dependency]
    |-- R5-Full          [proved internal]
    `-- M9               [open; uniform active blocks]
        |-- M9-M1        [open]
        |   `-- physical one-count assembly [proved conditional assembly]
        |       |-- M1 top-endpoint signed cone                    [open]
        |       `-- M1 direct smooth residual blockwise estimate   [open]
        |-- M9-M2        [open]
        |   `-- physical one-count assembly [proved conditional assembly]
        |       |-- TOP: density-discrepancy energy / signed cone   [open]
        |       |-- BAL: smooth balanced quarter packet             [open]
        |       `-- UNBAL: smooth unbalanced three-quarter estimate [open]
        `-- endpoint uniformity over every real-X active label      [open seam]
```

The hard-TOP residual Fejer work lies strictly below the TOP leaf:

```text
TOP density-discrepancy energy
`-- complete hard-TOP channel assembly
    |-- accepted square, exact-centre, long-channel, XOR, and other strict owners
    |-- t=1 residual
    |   |-- (165.K17a) minimal even short-shift aggregate [open]
    |   `-- (165.K26) maximal even medium/long aggregate  [open alternative]
    `-- remaining L << D << L^2, t << sqrt(L) few-point channels
        and their near-collision collars [open]
```

Thus (165.K17a) and (165.K26) are an OR only inside the residual child. They are not an OR with TOP, BAL, or UNBAL.

The alternative tree is

```text
GC-target
`-- GC-global-M1-alternative-bridge [derived under assumptions]
    |-- H1-H3, H4, R5-Full                         [accepted]
    |-- exact GAR-to-total-active-M1 equivalence   [proved internal]
    |   `-- GAR                                     [open]
    |       `-- global radial one-count assembly   [proved conditional assembly]
    |           |-- compact/nonlower/interface pieces [proved]
    |           `-- global lower-radial signed estimate [open]
    `-- M9-M2                                      [open]
        |-- TOP                                    [open]
        |-- BAL                                    [open]
        `-- UNBAL                                  [open]
```

GAR replaces the *conjunction* of the two direct M1 parents only in this global bridge. It does not prove `M9-M1`, blockwise endpoint uniformity for M1, or `M9`.

The separate exponent lane is not a third quarter tree:

```text
W=Y^(7/16) actual determinant correlation
`-- local persistence connector
    `-- possible pointwise exponent below 1/3
```

It bypasses neither the standard nor GAR quarter obligations and cannot be advertised as progress on `M9`.

### 3.2 Exact frontier, power, leverage, obstruction, and exponent matrix

In the table, “capacity” is an accepted upper-capacity or hostile-control scale, never a lower bound for the literal scalar.

| Rank | Candidate and exact target | Present positive capacity / missing saving | First genuinely new mechanism and accepted obstructions it must bypass | Downstream leverage | Lawful exponent effect |
|---:|---|---|---|---|---|
| 1 | **Minimal residual Fejer (165.K17a)/(167.F):** \(\Re\mathfrak C_{R_0,2,{\rm opp},g<\gamma L}^{\rm rem}\ll L^2X^\varepsilon\), \(R_0\asymp L\). | The direct opened-incidence positive ledger has capacity \(L^3\); an aggregate factor \(L\) is missing. Phase-aligned arrays separately diagnose any proof step that erases the incidence filters. The diagonal, monotone sector, and \(g\ge\gamma L\) sector are already target-safe. | Joint determinant-orbit spectral cancellation for \(d'm'-dm=r\), retaining one real part and the actual residual coefficient. It must bypass frozen character on even cofactor rows, absent modulo-one separation, adverse positive second derivative, adverse absolute dual modes, shiftwise-modulus positivity, XOR-scalar/non-energy separation, and hostile aligned arrays. | Closes only the complete residual scalar; the other hard-TOP channels remain. It is the smallest exact mechanistically specified aggregate frontier and now has a concrete candidate source model. | None alone. Quarter only after full TOP, BAL, UNBAL, a complete M1 route, endpoint assembly, and a bridge. |
| 2 | **Maximal residual Fejer (165.K26):** the even \(R_0\le r<M_L\) aggregate is \(O(L^3X^\varepsilon)\), with \(M_L\asymp L^2\). | Fixed-shift Cauchy gives \(L^4\) over the medium/long range; a factor \(L\) is missing. The \(r<R_0\) range is already paid inside the \(L^3\) budget. | Joint long-determinant spectral/large-sieve cancellation across \((r,N)\). It must retain the Fejer weight and endpoints; parity alone and positive row completion give no saving. | Same residual owner as rank 1. It is broader and has fewer strict-sector reductions, hence is the fallback rather than the first gate. | None alone. |
| 3 | **Direct residual scalar:** \(|\mathcal S_{L,1}^{\rm rem}|\ll L^{3/2}X^\varepsilon\). | Coefficient energy plus support Cauchy gives \(L^2X^\varepsilon\); a factor \(L^{1/2}\) is missing. | A coefficient-sensitive nonlinear square-root exponential-sum theorem acting before Fejer. It must bypass the Abel/BV \(L^2\) transport capacity, character-Poisson involution, product-collar repayment, common-test one-column alignment, uncontrolled divisor complement, and hard boundary transitions. No exact new source interface is presently as clean as the determinant correlation. | Same residual owner; formally a smaller power deficit but a less developed analytic interface. | None alone. |
| 4 | **Direct complete hard-TOP parent shortcut:** \(\Re C_{(L,{\rm tag})}^{\rm comp}\ll L^2X^\varepsilon\), with owner normalizations \(E_L^{\rm top}\ll L^2X^\varepsilon\) and \(T_{\rm end,L}\ll L^{3/2}X^\varepsilon\). | Coefficient-blind hard-cone energy is \(L^3\), or scalar capacity \(L^2\), leaving respectively \(L\) or \(L^{1/2}\). Fixed \(t\ge\tau\sqrt L\) channels are closed, but the residual, \(L\ll D\ll L^2,\ t\ll\sqrt L\) channels, and near collars remain. | One actual-vector cross-channel trace/spectral theorem that owns the residual plus every few-point channel. It must bypass product-fibre self-return, radical one-column alignment, exact-collision/near-collision confusion, positive outer energies, and the named common-test and four-root no-matches. | If the entire parent were proved, TOP would close, leaving BAL and UNBAL for `M9-M2`. Proving only the remaining nonresidual channels is a narrower, different frontier and would leave (167.F)/(165.K26) open. | None alone. |
| 5 | **GAR:** \(\Re\{e(1/8)\sum_{n\le16\sqrt X}C_X^*(n)n^{-3/4}e(\sqrt{Xn})\}\ll X^\varepsilon\). | All nonlower/interface owners are proved. With \(R=X^{1/4}\) and \(y=\lfloor\sqrt X\rfloor=R^2+O(1)\), the Round-122 localized lower wavelet has absolute capacity \(R^2\) against an \(RX^\varepsilon\) target; the separated centered-square route has \(y^3\) capacity against \(y^2X^\varepsilon\). | A joint signed lower-radial theorem across the medium-index, low-two-adic wavelet, not the stronger separated \(k\)-norm. It must bypass full-circle/complement self-return, uncentered drift, positive Farey energy, rational-spectrum/Appell/Voronoi/reciprocal self-returns, and the fixed-polylog collar boundary. | Proves the total active M1 contribution through the alternative bridge and bypasses both direct M1 parents. Still leaves all of M2. This is high global leverage but a much larger and more historically obstructed theorem than (167.F). | GAR alone leaves the internal exponent at \(1/3\); GAR plus all M2 gives \(1/4\) through the alternative bridge. |
| 6 | **Direct hard M1 parent:** normalized cone \(\ll L^{3/2}X^\varepsilon\), equivalently physical block \(\ll X^{1/4+\varepsilon}\). | Normalized capacity \(L^2\), or physical \(X^{1/4}L^{1/2}\); missing \(L^{1/2}=X^{1/12}\) at \(L=X^{1/6}\). | A sign-sensitive actual-symbol product-phase cone theorem. It must bypass phase-aligned bounded arrays, the direct-menu one-third contact, the worse critical TTY row, transform self-return, and false hard/smooth profile telescoping. | Closes only one of the two direct M1 parents. | None alone; both direct parents plus all M2 and endpoint are needed for the standard quarter route. |
| 7 | **Direct smooth M1 parent:** every literal \(B_1(D,L;X)\ll X^{1/4+\varepsilon}\). | The first smooth critical profile has accepted menu capacity \(X^{1/3+o(1)}\); missing \(X^{1/12}=L^{1/2}\). | A uniform actual-symbol theorem over all smooth \(\mathcal U_1\) labels, retaining profile and height boundaries. Equal hard/smooth deficits, the nonnegative profile telescope, and GAR cannot supply blockwise cancellation. | Closes only the other direct M1 parent. | None alone. |
| 8 | **BAL:** \(|\sum_GG\mathscr P_G|\ll L^{3/2}X^\varepsilon\) for every literal \(1\le K/L\le16\) block. | The present envelope loses at most \(X^{1/12}=L^{1/2}\) at the critical label. In the corresponding double-far squared-energy ledger, the positive capacity is \(L^4\) against an \(L^3\) signed-energy target; this is not an algebraic equivalence with every scalar formulation. | A gauge-sensitive, actual-symbol broad--narrow or multi-orbit theorem for the full \((h,k,k',d,\mu,J)\) kernel. It must survive the exact character gauge, fixed-\(Q\) rational rulings, inequivalent determinant notions, empty gauged broad class, and positive-cap/one-alias self-return. | Closes BAL only; TOP and UNBAL remain. | None alone. |
| 9 | **UNBAL:** \(\mathcal T_{L,K}\ll (LK)^{3/4}X^\varepsilon\), \(K/L>16\). | At \(a=\delta-\ell\), the exact missing factor is \(X^{\mu(a)}\), where \(\mu(a)=a-1/4\) for \(1/4<a\le1/3\) and \(\mu(a)=(1-2a)/4\) for \(1/3\le a<1/2\). The scalar projective cost \(K^{1/2-o(1)}\) and long-row cost \(X^{a/2}\) each exceed this missing factor. | A new signed vector theorem for the complete \((g,n,j,h)\) inverse-residue matrix, before positive norms, with all long frequencies and growing levels. It must bypass full-rank reciprocity, complete-frequency self-return, folded-majorant mass repayment, high bandwidth, and the named scalar Kloosterman/spectral no-matches. | Closes UNBAL only; TOP and BAL remain. | None alone. |
| 10 | **Lawful sub-\(1/3\) lane:** at \(W=Y^{7/16}\), prove the complete actual determinant correlation \(\ll Y^{\beta+\varepsilon}\). The frozen determinant-correlation target is \(\beta=1/2\). | Best complete bound is \(\beta=35/48\). Strict improvement over the internal \(1/3\) requires \(\beta<9/16\), hence more than \(Y^{1/6}\) saving from the present bound; reaching \(1/2\) requires \(Y^{11/48}\). | A joint signed cross-ray determinant-adapted DLS/decoupling theorem before positive norms. It must bypass per-ray persistence at \(9/16\), positive outer energy, independent-numerator fiction, sequential-transform self-return, insufficient Demeter--Wu transversality, and the direct/factor-first Li--Yang two-wave capacity. | Produces an intermediate theorem only; it closes no M9 parent. Its theorem is much larger than the residual Fejer gate. | For complete block exponent \(\beta\), \(\Theta(\beta)=\max\{(7/16+\beta)/3,\beta/2\}\). Thus \(\beta<9/16\) gives \(<1/3\), and \(\beta=1/2\) gives \(5/16\), slightly better than the external Li--Yang benchmark but not \(1/4\). |
| 11 | **Endpoint uniformity:** all chosen parent estimates hold for every real \(X\) and \(X^{1/4}\le D\le X^{1/2}\), with floors, stars, short blocks, and boundary labels. | No independent positive capacity: its blockers are precisely the five analytic parents on the standard route. | An endpoint audit and finite completion after the parents close. It cannot manufacture a missing analytic saving. | Necessary for standard `M9`; the GAR route bypasses blockwise M1 but not M2's own endpoint-complete statements. | None independently. |

The matrix proves the ranking. GAR and the full hard-TOP parent have greater eventual graph leverage, but their open statements contain many independent unresolved owners. The direct residual has the smallest raw scalar deficit, but every tested direct mechanism returns or loses the needed sign. The candidate source matches the determinant skeleton already isolated in (165.K17a); that is enough to retain one final source-to-interface/no-go gate, not to infer applicability or cancellation.

### 3.3 Grimmelt--Merikoski mechanism: exact preliminary map, not applicability

The primary source is Lasse Grimmelt and Jori Merikoski, *Twisted correlations of the divisor function via discrete averages of \(\operatorname{SL}_2(\mathbb R)\) Poincaré series*, arXiv:2404.08502v2, Theorem 10.1. It averages matrices of determinant \(hk\), twisted by
\(\alpha\in\mathcal A(q_1,q_2,\chi,\xi)\), with:

- \(\beta_h\) on \(|h|\in[H,2H]\) and \(\gamma_k\) on \(|k|\in[K,2K]\);
- \(HK\le(AD)^{1+\eta}\);
- a scaled \(C^7_\delta\) test function;
- the coprimality condition \(\gcd(h,kq)=1\);
- an explicit multi-orbit correlation hypothesis (10.2) measured by \(\mathcal K_+\); and
- a main term plus an error proportional to
  \[
  Z^{O(\eta)}\delta^{-O(1)}(AD)^{1/2}
  \|\beta\xi\|_2\mathcal K_+^{1/2}
  \bigl(\mathcal R_0+\min(\mathcal R_1,\mathcal R_2)\bigr).
  \]

The literal determinant map is

\[
 \begin{pmatrix}a&b\\c&d\end{pmatrix}
 =\begin{pmatrix}d'&d\\m&m'\end{pmatrix},
 \qquad ad-bc=d'm'-dm=r.
\]

This source is strategically relevant for three precise reasons: it keeps the determinant equation intact, it treats interactions among several automorphic orbits rather than scalarizing into independent Kloosterman tests, and its final theorem estimates a signed aggregate before a termwise triangle inequality.

Literal applicability is nevertheless open. The first source seams are:

1. the canonical residual selector depends on the factorization of \(N\) and is not yet shown to lie in \(\mathcal A(q_1,q_2,\chi,\xi)\);
2. squarefree/coprime and residual conditions may require Möbius and congruence openings with growing \(q_1,q_2\), and no target-safe \(\mathcal K_+\) ledger exists;
3. the compulsory even shifts require a two-adic factorization \(r=hk\) compatible with \(\gcd(h,kq)=1\) and the matrix gcd conditions on every stratum;
4. the oscillatory factor
   \(e(J(\sqrt{N+r}-\sqrt N))\) must enter the \(C^7_\delta\) weight, whose scaled derivatives can be large; the unspecified \(\delta^{-O(1)}\) cost cannot be ignored;
5. the opposing-displacement and low-gcd cuts, hard support, stars, and zero-extension boundaries require a literal smooth/boundary partition and recombination;
6. the source main term and all \(\mathcal R_j\) terms must be shown target-safe after the Fejer, two-adic, gcd, and Möbius sums; and
7. the source theorem cannot be used after taking absolute values of individual shifts or orbits, because that would return the accepted \(L^3\) capacity.

Therefore Theorem 10.1 currently supplies a candidate source model and an exact audit checklist, not a proof or graph dependency. The dedicated Round-166 source audit remains authoritative for any final source conclusion.

## 4. First doubtful or unproved step

The first mathematical gap is the following exact source/interface lemma:

> After a finite target-safe partition of the literal residual determinant family, represent each piece by a Grimmelt--Merikoski admissible automorphic coefficient and \(C^7_\delta\) weight, or by a bespoke determinant-Poincaré kernel with the same one-real-part placement, such that the total main term and spectral error are \(O_{\gamma,\varepsilon}(L^2X^\varepsilon)\).

No such representation or estimate is proved. In particular, it is doubtful at present that the nonlocal neither/both selector is automorphic at acceptable orbit-correlation norm, or that the square-root phase can be placed into the source's smooth test class without a fatal \(\delta^{-O(1)}\) cost. These are the first issues to test; a general discussion of spectral cancellation before resolving them would be premature.

Even if this source/interface lemma succeeds, the actual spectral inequality still has to save a full factor \(L\) over the coefficient-blind \(L^3\) capacity. Thus a successful dictionary is necessary but not sufficient.

## 5. Required control tests and outcomes

### 5.1 Round-166 controls

| Required control | Outcome |
|---|---|
| `authoritative_dependency_tree` | **GREEN.** Both complete trees and every open mandatory leaf are displayed in Section 3.1. |
| `standard_vs_GAR_logical_or` | **GREEN.** GAR replaces total active M1 only in the alternative bridge and is not a blockwise M1 theorem. |
| `minimal_vs_maximal_Fejer_scale` | **GREEN.** Targets \(L^2\) and \(L^3\), capacities \(L^3\) and \(L^4\), and their residual-only scope are separate. |
| `residual_vs_full_hard_TOP_scope` | **GREEN.** A residual theorem leaves the other few-point channels, near collars, and the parent energy. |
| `BAL_UNBAL_independence` | **GREEN.** They remain distinct mandatory smooth parents with different exact kernels. |
| `direct_M1_vs_GAR_scope` | **GREEN.** The two direct parents are conjunctive; GAR is a global alternative and implies neither. |
| `power_margin_and_global_exponent_connector` | **GREEN.** Every target deficit is recorded, and the only explicitly quantified open internal sub-one-third connector compared in this ranking is \(\Theta(\beta)\). |
| `rejected_mechanism_bypass` | **GREEN as a strategy requirement, OPEN analytically.** The selected joint determinant mechanism is outside rowwise/positive transforms, but literal source applicability is unproved. |
| `single_Round167_objective` | **GREEN.** Only (167.F) is selected. (165.K26) is not an automatic second task. |
| `no_status_or_exponent_overpromotion` | **GREEN.** No node or exponent changes. |

### 5.2 Mandatory Round-167 false controls

1. **Aligned-array control.** At the unfiltered or filter-erased Fejer level, replace the actual residual coefficient by a phase-aligned array with the same support and \(\ell^2\) scale. Any argument that still returns \(O(L^2)\) is using false coefficient-uniform information and must be rejected. This is not a literal counterexample to the post-opening \({\rm opp},g<\gamma L\) aggregate unless the control is lifted to explicit incidences.
2. **Shiftwise-modulus control.** Insert absolute values around each \(r\)-correlation. The resulting positive additive-shift form has \(L^3\) capacity; no target claim may survive without an additional proved saving.
3. **Even-row character control.** On cofactor-gcd rows and even shifts, the character is frozen. Any claimed alternating-row gain is false.
4. **Modulo-one control.** Large real derivatives in the accepted ledger do not imply distance from integers or half-integers.
5. **High-gcd ownership control.** The \(g\ge\gamma L\) bound concerns opened divisor incidences, not a unique product-row partition; it may be removed only once.
6. **Source-class control.** Test the exact residual selector, not merely \(\chi_4(d')\chi_4(d)\), against the definition of \(\mathcal A(q_1,q_2,\chi,\xi)\).
7. **Source-power control.** Restore \(\delta^{-O(1)}\), \(\mathcal K_+\), \(\mathcal R_j\), modulus, Möbius, cell, endpoint, and main-term costs before comparing with \(L^2\).
8. **Downstream control.** Even a proof of (167.F) may update only the residual child after its seams are validated; no parent or exponent is automatic.

No numerical experiment is relevant to these controls. This report used 100% analytical, algebraic, graph, and source-hypothesis reasoning.

## 6. Dependencies and exact artifacts used

The derivation uses only the assigned graph and context packet, plus the parent-supplied primary-source candidate:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `state/best_proof_draft.md`;
- `strategy/round166_full_proof_strategy_current_literature_review.md`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-unbalanced-inverse-selector-reciprocity-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/synthesis.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md`;
- the generated brief
  `rounds/codex-managed/full-proof-round164-166-strategy-literature-review/briefs/full_graph_frontier_strategy_audit.md`; and
- Grimmelt--Merikoski, arXiv:2404.08502v2, Theorem 10.1 and the source definition of \(\mathcal A(q_1,q_2,\chi,\xi)\) immediately preceding it: <https://arxiv.org/abs/2404.08502>.

The Round-166 sibling reports were not used. The dedicated source auditor must independently confirm the version, theorem numbering, hypotheses, parameter map, and any later publication status before the source can affect the graph.

## 7. Recommended state effect

**Recommended state effect: retain / no graph change.**

- Close Round 166 under `strategy_frontier_retained`.
- Keep every current status unchanged.
- Keep the internal exponent \(1/3\), the separately audited external Li--Yang exponent
  \[
  \frac{3292+25\sqrt{1717}}{13762}
  =0.3144831759740614\ldots,
  \]
  and the target \(1/4\) distinct.
- Freeze exactly (167.F) for Round 167.
- Permit Grimmelt--Merikoski Theorem 10.1 only as a candidate mechanism subject to the exact promotion gate in Section 2.3.
- If the first literal source hypothesis or restored power fails, record the scoped no-go required by Section 2.4 and return to strategy selection; do not silently advance to (165.K26), direct residual, GAR, or another parent.

This report neither proves (167.F) nor recommends promoting any source, parent, bridge, or exponent.
