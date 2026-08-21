# Round 90 hostile/source audit: M1 capacity self-return

- Campaign: `m9-m1-capacity-self-return-fork`
- Task: `m1_self_return_hostile_source_audit`
- Role: `source_auditor`
- Graph SHA-256: `bd5eed1e732c8872b37c0ea51bc9cea65419fe3241c17a981df3c2a36cd2c0f1`
- Generated: `2026-08-17T08:17:26+08:00`
- Status: candidate evidence only; no shared proof state changed.

## 1. Result

**Capacity self-return is exact after the compulsory square root; there is no
additional \(J^{1/6}\) loss and no strict non-returning power gain.  A literal
operator involution is not proved and should not be claimed.**  Put

\[
 A_{82}:={J^2\over T}=J^{7/5},\qquad
 L:=TQ^{-5/24}.
\]

The Round-82 coefficientwise majorant is exactly

\[
 B^3L^2={C^3\over TQ^{5/12}},
 \qquad {B^3L^2\over A_{82}}
 =B^3J^{-11/30}=:\Gamma_{82}.                 \tag{1.1}
\]

For one deep dyadic \(d\)-shell of length \(\asymp D\), the accepted
unnormalized Fejer \(A\)-process at \(U=D\), followed by Cauchy over
\(b\asymp B\), has the exact scale

\[
 |\mathcal H_D|^2\ll_\varepsilon
 X^\varepsilon {B\over D}\,\mathcal E_D,       \tag{1.2}
\]

where \(\mathcal E_D\) is the complete four-row energy, including its once-owned
\(u=0\) diagonal.  For a physical edge graph of maximum in- and out-degree
\(\Delta\),

\[
 \mathcal E_D\ll_\varepsilon
 X^\varepsilon DB^3\Delta L^4.                  \tag{1.3}
\]

Consequently

\[
 { |\mathcal H_D|\over A_{82}}
 \ll_\varepsilon X^\varepsilon
 \bigl(\Delta B^4J^{-11/15}\bigr)^{1/2}.         \tag{1.4}
\]

At full degree \(\Delta\asymp M^2\asymp B^2\), (1.2)--(1.3) return
*exactly* to the Round-82 majorant:

\[
 \left({B\over D}\,DB^3B^2L^4\right)^{1/2}
 =B^3L^2.                                        \tag{1.5}
\]

Equivalently,

\[
 \Gamma_{\rm deep}=B^6J^{-11/15}=\Gamma_{82}^2,
 \qquad \sqrt{\Gamma_{\rm deep}}=\Gamma_{82}.   \tag{1.6}
\]

Thus at \(B=J^{3/20}\) the deep **energy** gap is \(J^{1/6}\), but the
corresponding gap for the original Round-82 operator is only its square root
\(J^{1/12}\), exactly the Round-82 gap.  Calling both gaps losses in the same
norm would double-count the \(A\)-process squaring.  Conversely, the Round-89
\(q=8\) fibre retains full directed degree, so the accepted R82--R89 filtration
does not reduce the worst energy exponent below \(J^{1/6}\).

The selected reports give the local ingredients which should reassemble the
**Fejer energy of the strict Round-86 hard residual**, not the linear Round-82
correlation itself, but they do not display the complete coefficient-level
cell/descent inverse identity.  Even after that documentary seam is closed, the
last passage is the one-sided inequality (1.2), and the R82--R86 target-safe
deletions are not invertible.  The defensible result is therefore an
equal-capacity barrier theorem, not an algebraic identity between (90.6) and
(90.5).  No audited current primary theorem supplies the missing joint estimate
on the varying-modulus actual symbol.

## 2. Exact statement and hypotheses

Assume exactly

\[
 J=X^{1/2},\quad Q=J^{2/5},\quad T=J^{3/5},\quad B=C/T,
 \quad J^{13/18}<C\le J^{3/4},\quad M\asymp B,     \tag{2.1}
\]

and fix a transition-flattened smooth nonaxial M1 principal component, one of
the three exact local classes, an alias, a sign, and a reflected orientation.
Let the normalized physical row be

\[
 \mathcal R_{b,x}(\theta)
 ={1\over M}\sum_n I_b(n)e_M(nx)e(n\theta),
 \qquad \|\mathcal R_{b,x}\|_\infty
 \ll_\varepsilon X^\varepsilon L.                \tag{2.2}
\]

Let \(\mathcal H_D\) denote the linear centered dual-difference residual on one
dyadic shell after the exact owners of same residue, literal \(d=0\),
\(0<|d|\le D_1\), and the outer collar have been removed, with

\[
 D_1<|d|<\Delta_b-J^{3/4}.                         \tag{2.3}
\]

Extend the shell coefficient by zero outside its actual \(b\)-dependent hard
support.  Let \(\mathcal E_D\) be its complete \(U=D\) Fejer energy before any
late local term is discarded.  Its completed coefficient is the literal

\[
 {1\over M^5}\sum_{n,m}
 \Omega_{b,d,u}(n,m)e_M(dV+nA-mB_2)
 \mathfrak T_M(u,A,B_2,V),                         \tag{2.4}
\]

\[
 \Omega_{b,d,u}(n,m)=
 I_b(n+d+u)\overline{I_b(n)}
 \overline{I_b(m+d)}I_b(m).                        \tag{2.5}
\]

The following distinctions are hypotheses of the statement, not optional
conventions.

- The \(M^{-1}\) in each row is already present.  An ordered pair contains
  \(M^{-2}\); completion has \(M^{-5}\) because four rows contribute \(M^{-4}\)
  and Fourier inversion contributes \(M^{-1}\), while the outer \(M\) remains
  inside \(\mathfrak T_M\).  No further \(M^{-2}\) is available.
- A pair has the physical gain \(Q^{-5/12}\); the four-row energy has
  \(Q^{-5/6}=(Q^{-5/12})^2\).  These are the same gain in two different norm
  levels.
- The literal integers \(d=0\) and \(u=0\) are distinct owners.  Nonzero
  multiples \(d=jM\) and \(u=jM\) remain.  Ramanujan centering is retained in
  the physical pair before the \(A\)-process.
- Round 87 owns same-group terms, Round 88 owns the certified coarse and
  good-prime packages, and Round 89 owns only its certified cells or unions.
  Their complements, including all bad-prime, nonunit, affine-only,
  projection-only, shallow and aperiodic factors, remain in the strict graph.
- All claims are per fixed component and are then summed over the finite class,
  sign, alias, and orientation families.  Dyadic-shell and finite-family losses
  are absorbed into \(X^\varepsilon\).

Under these hypotheses, (1.2)--(1.6) are an internal norm calculation.  They
do not estimate the strict actual-symbol energy and do not assert that a
phase-conjugating full-degree graph is realized as a signed lower bound.

## 3. Proof or derivation

**Fejer target and the square-root seam.**  For fixed \(b\), let
\(a_{b,d}\) be the zero-extended hard-shell coefficient and let its support
length be \(\ell_b\ll D\).  The elementary unnormalized Fejer inequality gives

\[
 \left|\sum_da_{b,d}\right|^2
 \le {\ell_b+D-1\over D^2}
 \sum_{|u|<D}(D-|u|)
 \sum_da_{b,d+u}\overline{a_{b,d}}.                \tag{3.1}
\]

The correlation on the right is the integral against
\(|D_D(\theta)|^2\).  Cauchy over \(b\asymp B\) changes (3.1) into (1.2).
This explains, rather than assumes, the late target:

\[
 {D\over B}A_{82}^2={D\over B}J^{14/5}.            \tag{3.2}
\]

The factor \(D\) in the four-row target is cancelled by the \(D^{-1}\) in
(3.1), and the factor \(B^{-1}\) is cancelled by Cauchy's \(B\).  Hence neither
is a gain.  Replacing \(|D_D|^2\) by
\(\mathcal K_D^\circ=|D_D|^2-D\) removes only \(u=0\); the positive diagonal
must be added once before using (3.1).  Its accepted bound is target-safe and
does not change the worst gap.

**Graph count and \(Q\)-power.**  There are \(O(B)\) moduli, \(O(M^2)\)
physical ordered-pair vertices per modulus, and at most \(\Delta\) directed
partners per vertex.  The centered Fejer kernel has \(L^1\)-mass \(O(D)\), and
four normalized rows cost \(L^4=T^4Q^{-5/6}\).  This gives (1.3).  Dividing by
(3.2) yields

\[
 {DB^3\Delta T^4Q^{-5/6}\over(D/B)J^{14/5}}
 =\Delta B^4J^{-11/15}.                            \tag{3.3}
\]

For \(\Delta=B^2\), (3.3) is the square of (1.1).  This also proves directly
that \(Q^{-5/24}\), \(Q^{-5/12}\), and \(Q^{-5/6}\) are row, pair, and
four-row powers, respectively; none may be credited twice.

**Coefficient-level \(M\)-normalization and the centered incidence.**  Write
the centered physical coefficient before differencing as

\[
 \mathcal A_{b,d}={1\over M^2}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.                        \tag{3.4}
\]

Before any completion, one \(A\)-process coefficient is therefore

\[
 \mathcal A_{b,d+u}\overline{\mathcal A_{b,d}}
 ={1\over M^4}\sum_{n,m}\Omega_{b,d,u}(n,m)
 \sum_{P,P'}e_M(\text{the complete physical phase}).\tag{3.5}
\]

If the inner base-point sum is denoted by $\tau_M$ and the completed-trace
convention is $\mathfrak T_M=M\tau_M$, then coefficientwise

\[
 {1\over M^5}\mathfrak T_M={1\over M^4}\tau_M.    \tag{3.6}
\]

Thus the \(M^{-5}\) in (90.6) is compatible with the square of the \(M^{-2}\)
in (3.4); it is not an additional \(M^{-1}\) gain.  This check is conditional
on summing the complete \(A,B_2,V\) label ranges with the same Fourier
convention and on \(\mathfrak T_M\) retaining its outer \(M\).  The selected
artifacts do not display one global line proving that every R89 cell and its
complement, after every local \(p^{2j}\) descent, reconstitute the exact inner
sum in (3.5) with multiplicity one.  Hence (3.6) certifies the only possible
normalization, but not the missing complete coefficient identity.

The exact uncentered Fejer energy is

\[
 \mathcal E_D=\sum_{b}\sum_{|u|<D}(D-|u|)
 \sum_d\mathcal A_{b,d+u}\overline{\mathcal A_{b,d}},\qquad
 \mathcal E_{D,0}=D\sum_{b,d}|\mathcal A_{b,d}|^2.\tag{3.7}
\]

The \(u=0\) term in (3.7) is the **whole** shift diagonal.  Since
\(\mathcal A_{b,d}\) already sums all physical groups and already contains
Ramanujan centering, \(\mathcal E_{D,0}\) includes same-group and cross-group
physical incidences and, on expansion, the four-Kloosterman term, both
Ramanujan cross terms, and \(|c_M(d)|^2\).  The subtraction
\(\mathcal K_D^\circ=|D_D|^2-D\) deletes this entire coefficient, not merely
the physical equality \(P=P'\).  Consequently an exact owner ledger must be

\[
 \mathcal E_D=\mathcal E_{D,0}^{\rm global}
 +\mathcal E_{D,u\ne0}^{\rm same}
 +\mathcal E_{D,u\ne0}^{\rm cross}.               \tag{3.8}
\]

The positive Round-87 full-\(|D_D|^2\) same-group square is the proved
dominating package, but it is not identical to the second term in (3.8): it
contains its own \(u=0\) coefficient.  That coefficient cannot simultaneously
be an exact owner if \(\mathcal E_{D,0}^{\rm global}\) is also owned.  A literal
ledger must either center the same-group incidence and bound the removed
same-group diagonal separately, or own the full same-group package and add
only the complementary cross-group part of the global diagonal.  The selected
artifacts state the domination convention but do not display this equality in
one coefficient formula.  This is a norm-bound versus incidence-ownership
distinction, not a new power loss.

**Exact ownership/reassembly diagram.**  The lawful reassembly has two norm
levels:

\[
 \mathfrak X_{82}
 =\mathfrak S_{82\text{--}86}+\sum_D\mathcal H_D,
 \qquad
 |\mathcal H_D|^2\ll {B\over D}\mathcal E_D,       \tag{3.9}
\]

\[
 \mathcal E_D=
 \mathcal E_{u=0}^{\rm global}+\mathcal E_{\rm same}^{u\ne0}
 +\mathcal E_{\rm coarse}+\mathcal E_{\rm good}
 +\mathcal E_{\rm cells}+\mathcal E_{\rm strict}.\tag{3.10}
\]

Here \(\mathfrak S_{82\text{--}86}\) is the sum of the already safe *linear*
owners.  Formula (3.10) is the required partition of the *squared Fejer
energy*, with every term after the global diagonal restricted to \(u\ne0\).
Adding the terms in (3.10) directly to \(\mathfrak S_{82\text{--}86}\) would mix norm
levels and is an ownership error.  Within (3.10), full CRT cells plus their
residual complement are exhaustive; empty masks are zero; completed descent
must reinsert every supported frequency with the exact \(p^{2j}\) trace factor;
reversal/transposition retains both directions; and inverse completion then
returns the physical Fejer autocorrelation *provided the missing
coefficient-level identity described after (3.6) is supplied*.  It does not
invert (3.1).

The capacity ledger is therefore:

| Round | Norm level | Gap before | Accepted removal | Worst survivor gap |
|---|---:|---:|---:|---:|
| R82 | coefficient | \(\Gamma_{82}\) | same residue and each already-owned fixed-offset layer are \(O(1)\) relative to \(A_{82}\) | \(\Gamma_{82}\) |
| R83 | coefficient | \(\Gamma_{82}\) | literal integer \(d=0\) is \(O(1)\); nonzero \(d\equiv0\pmod M\) stay | \(\Gamma_{82}\) |
| R84 | coefficient | \(\Gamma_{82}\) | \(0<|d|\le J^{17/30}\) is \(O(1)\) | \(\Gamma_{82}\) |
| R85 | coefficient / setup | \(\Gamma_{82}\) | support-edge and \(A\)-process diagonal bookkeeping give no whole-shell power; the raw transition is not re-owned | \(\Gamma_{82}\) |
| R86 | coefficient | \(\Gamma_{82}\) | \(J^{17/30}<|d|\le D_1\) and the smooth collar are \(O(1)\) | \(\Gamma_{82}\) |
| R87 | four-row energy | \(\Gamma_{82}^2\) | same-group package is \(O(J^{-2/15})\) relative to (3.2) | \(\Gamma_{82}^2\) |
| R88 | four-row energy | \(\Gamma_{82}^2\) | \(R_*\le\rho_*\) and \(\mathfrak a\ge M^2/\rho_*^2\) are \(O(1)\) | \(\Gamma_{82}^2\) |
| R89 | four-row energy | \(\Gamma_{82}^2\) | certified cells/unions are \(O(1)\); the full union is not | \(\Gamma_{82}^2\), witnessed at capacity level by the \(q=8\) full-degree fibre |

Thus R82--R89 remove genuine subaggregates but never lower the worst power.
The variables introduced by CRT, descent, completion, reversal, and local cell
classification are invertible coordinates or partitions when summed
completely.  The first noninvertible step is Fejer/Cauchy, but (1.5) shows that
it squares target and capacity in exactly the same proportion.  It creates no
strict non-returning signed degree of freedom.

**Claim-by-claim hostile and primary-source hypothesis map.**  The source
verdicts below are failures of literal hypotheses, not impossibility claims for
a future reformulation.

| Claim to be licensed | Exact hostile check | Closest current primary result and first mismatch | Verdict |
|---|---|---|---|
| A standard spectral large sieve closes the R82 carrier | The odd leading row has varying moduli \(4b\asymp B\), index length \(Q^2\gg B\), and after squaring a product kernel with a joint symbol | Deshouillers--Iwaniec, Theorem 2, has the coefficient-blind regular-spectrum cost; in the literal level-four map it gives \(BQ^2T=B A_{82}\) | no closure |
| Prime-field trace cancellation controls (2.4) | \(M\) is arbitrary composite, includes all prime powers and the full \(2\)-part, and \(\Omega\) is not a bounded-conductor trace function | Fouvry--Kowalski--Michel, Theorem 1.5 and Corollary 1.6, require a bounded-conductor bountiful sheaf over \(\mathbb F_p\) and normal-tuple/nonzero-twist hypotheses | not applicable |
| A high-prime-power product theorem controls every local factor | The prime and depth vary with \(b\); the four-pole mask, nonunit \(K\), \(p=2\), and affine cancellation all remain | Milićević--Zhang, Theorem 4, is a fixed odd-prime depth-aspect theorem for a bounded shift pattern and explicitly retains power-aligned exceptional shifts | routing analogy only |
| A mixed rational-sum theorem bounds the completed global operator | Constant and degenerate \(q=4,8,9\) branches can have large traces, and the open problem is the coupled \(b,d,u,n,m,A,B_2,V\) sum | Cochrane--Granville, Theorems 1.1, 3.1, 5.1 and 20.1, treat one mixed sum modulo one \(p^\nu\), with separate degenerate and \(2\)-adic branches | local input only; no graph or symbol estimate |
| Existing four-Kloosterman estimates include the survivor | The survivor has arbitrary full prime powers, a complete four-unit mask, varying \(M\), and moving \(\Omega\) | Zheng, Lemma 2.8, treats a special squarefree four-Kloosterman parallelogram; Lemma 2.10 allows only prime exponents at most two | not applicable |
| A general complete rational bound is uniformly square-root at bad powers | The \(q=8\) and \(q=9\) controls are lower-conductor/constant branches | Wu--Xi, Theorem A.1, is one complete rational sum and its high-prime-power factor records rather than removes the bad-power loss | no uniform coefficient bound |
| Current arbitrary-modulus bilinear Kloosterman theorems estimate (90.6) | Their operator is one \(S(am,n;c)\) with two separated sequences; (2.4) is a centered fourfold trace with coupled actual weights and varying \(M\) | Pascadi Theorems 1.1/7.1 and Corollary 7.9; Blomer--Pascadi Theorems 1.1/5.5; Milićević--Qin--Wu Theorem 1.1.  The literal compressed R82 map is a full residue interval and a singleton, and Pascadi's common varying-modulus divisor is only \(4\) | not applicable; no \(B\)-power |
| Trilinear inverse-fraction estimates accept the actual row | The phase and coefficient depend jointly on \(b,c,d,u,n,m\), and the direct sizes are strongly unbalanced | Bettin--Chandee Theorem 1 and Wright Theorem 2.1 require separated coefficient sequences (Wright's convolution consequences also require a Siegel--Walfisz input) | not applicable |
| General-residue inverse-sum results control the affine constrained weight | The variables satisfy linked shifts and unit masks, with exceptional residues and the joint product row | Bourgain--Garaev Theorems 3 and 5 concern separated rectangles or a pure unweighted incomplete inverse sum | not applicable |
| Local Fourier support gives a power saving | Exact support \(p^j\mid u\) is accompanied by \(p^{2j}\) completed descent and unchanged centered-Fejer mass | No external theorem is needed: exact finite Fourier inversion itself returns the physical norm | false as a saving |
| The complete R82--R89 chain is an operator involution | R82--R86 deletions are estimates, and (3.1) is one-sided | None of the cited sources changes this algebraic fact | only capacity self-return is proved |

## 4. First doubtful or unproved step

The first doubtful step is **not** the power arithmetic: (1.1), (1.3), (3.2),
and (1.5) settle it exactly.  There is no unmatched \(Q\)-, \(M\)-, \(B\)-,
\(D\)-, or square-root loss once the norm level is recorded.

The first unproved seam is coefficient-level reassembly, before any external
estimate is invoked.  The \(M\)-powers force (3.6), and the local reports prove
individual CRT, support, and \(p^{2j}\)-descent identities, but the selected
R82--R89 artifacts do not give one complete formula which:

- maps every ordered quadruple \((P,P')\) in (3.5) to exactly one
  \((A,B_2,V)\) cell with the correct phase and multiplicity;
- sums every descended frequency back through every prime-power factor,
  including the full \(2\)-part, nonunit and aperiodic complements; and
- implements the exact incidence ledger (3.8), rather than adding the
  full-\(|D_D|^2\) same-group majorant to an already-owned global \(u=0\)
  diagonal.

Until that identity is written, complete-cell/descent inverse-transform
self-return is plausible and normalization-compatible, but not certified.
After it is supplied, the next unproved upgrade would be either of the
following.

- To call the chain a literal operator self-return, one would have to invert
  Fejer/Cauchy and reinsert R82--R86 target-safe terms as identities.  This is
  impossible from the accepted statements: (3.1) is an inequality and the
  safe deletions are estimates.  Exact inverse completion returns only
  \(\mathcal E_D\), the autocorrelation energy of \(\mathcal H_D\).
- To claim a strict non-return, one would have to prove, for the complete
  strict graph and actual \(\Omega\), either
  \(\Delta=o(B^2)\) by a fixed power in both directions or a signed estimate
  \(o(DB^5L^4)\).  Round 89 supplies a retained full-degree \(q=8\) fibre, and
  no audited theorem estimates its joint symbol.  Fewer named strata, sparse
  \(u\)-support, or lower local conductor does not meet this requirement.

There is one further ownership caveat worth making explicit.  The exact local cell
sum is complete only after the nonperiodic and failed-threshold complement is
included.  Summing only the certified R89 cells is not inverse CRT.  Likewise,
the centered kernel alone is not the positive Fejer energy; the global \(u=0\)
diagonal must be restored once before (3.1).  Subject to these one-count rules,
zero extension handles every moving support boundary and every \(d+u\) crossing
without a power loss.

The smallest still-open analytic input is therefore a varying-modulus joint
actual-symbol estimate for \(\mathcal E_{\rm strict}\), with all prime powers,
both directed orientations, both signs, all classes, nonzero modulus multiples,
Ramanujan cross/square terms, and the four moving stationary factors retained.

## 5. Control tests and outcomes

Here “pass” means that the hostile control was executed; it does not mean that
the M1 estimate was proved.

| Required control | Outcome |
|---|---|
| `capacity_ledger` | **Pass.**  The table in Section 3 separates coefficient and four-row energy levels.  R82--R86 retain \(\Gamma_{82}\); R87--R89 retain \(\Gamma_{82}^2\). |
| `Q_power_normalization` | **Pass.**  Row, pair, and four-row powers are \(Q^{-5/24}\), \(Q^{-5/12}\), and \(Q^{-5/6}\).  The last is the square of the second, not a second saving. |
| `complete_cell_reassembly` | **Not fully certified.**  Certified cells, failed-threshold cells, nonunit, affine, projection-only and aperiodic cells are the required exhaustive partition, but the selected artifacts do not display one global coefficient identity proving multiplicity-one reassembly.  Certified cells alone fail this control. |
| `completed_descent_inverse_transform` | **Normalization passes; literal global inverse remains open.**  Every supported frequency must be reinserted and a depth-\(j\) completed trace descends by \(p^{2j}\).  Equation (3.6) matches squared \(M^{-2}\), but the all-factor/all-cell inverse formula is not displayed. |
| `global_diagonal_one_count` | **Pass at the incidence level.**  Same residue, literal \(d=0\), Ramanujan centering, and Fejer \(u=0\) are distinct.  \(\mathcal K_D^\circ\) removes the whole coefficient \(D\sum|\mathcal A_{b,d}|^2\), including cross-group physical incidences; \(u=jM\ne0\) remains. |
| `prior_package_ownership` | **Pass as the required ledger; documentary seam remains.**  Linear owners R82--R86 are not added to energy owners R87--R89.  If global \(u=0\) is owned, the exact same-group incidence must be centered and its removed diagonal separately controlled; the full positive same-group square is a domination package, not a second exact owner. |
| `all_class_sign_modulus_multiple` | **Pass.**  The finite family of \(M\in\{4b,2b,b\}\), both stationary signs, aliases and reflected orientations is retained.  Nonzero \(d\equiv0\pmod M\) and \(u\equiv0\pmod M\) are not renamed zero modes. |
| `actual_stationary_symbol_support` | **Pass.**  All four \(I_b\) factors in (2.5) remain.  Zero extension handles shell and moving-support boundaries; no raw transition, axis, wrong-sign, or collar owner is reopened. |
| `top_J_one_sixth_control` | **Pass with norm correction.**  At \(B=J^{3/20}\), \(\Gamma_{\rm deep}=J^{1/6}\) in energy and \(\sqrt{\Gamma_{\rm deep}}=J^{1/12}\) for the original operator.  The latter equals \(\Gamma_{82}\). |
| `literal_self_return_or_strict_nonreturn` | **Pass only at scalar-capacity level; literal gate open.**  Equation (1.5) rules out a strict power gain from the accepted filtration.  Complete coefficient reassembly is not displayed, and even after it is supplied Fejer/Cauchy and prior estimates prevent an operator equality. |
| `source_hypothesis_map` | **Pass.**  The claim-by-claim table in Section 3 checks modulus type, prime-power depth, kernel count, coefficient separation, variable lengths, varying \(b\), degeneracies, and actual-symbol dependence.  No audited source has the literal operator. |
| `downstream_scope` | **Pass.**  No claim is made for \(C>J^{3/4}\), raw transitions, axes, cone edges, other sectors, M9-M2, endpoint uniformity, R5-Full, full M9-M1, M9, or the Gauss-circle exponent. |

No numerical experiment was used.  The \(q=8\) item is inherited as an exact
symbolic hostile control, not used as an aggregate lower bound.

## 6. Dependencies and exact artifacts used

The graph file hash was independently checked as
`bd5eed1e732c8872b37c0ea51bc9cea65419fe3241c17a981df3c2a36cd2c0f1`.
The repository artifacts used were exactly:

- `protocol.md`;
- `state/proof_obligations.yml`, especially the accepted R82--R89 reductions
  and rejected normalization/self-return claims;
- `state/active_campaign.yml`;
- `strategy/conductor_0817_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m1-capacity-self-return-fork/derivation_packet.md`,
  including the authorized equations (90.8)--(90.9);
- the permitted Round-82, Round-83, Round-84, Round-86, Round-87, Round-88,
  and Round-89 synthesis files;
- the four permitted hostile/source reports from Rounds 82, 83, 88, and 89;
- the task brief
  `rounds/codex-managed/m9-m1-capacity-self-return-fork/briefs/m1_self_return_hostile_source_audit.md`.

No sibling Round-90 report was read.  No shared proof-state, synthesis,
validation, or draft file was edited.

The primary-source check was refreshed on 17 August 2026.  Exact sources used
for the hypothesis map were:

- Jean-Marc Deshouillers and Henryk Iwaniec,
  [*Kloosterman sums and Fourier coefficients of cusp forms*](https://doi.org/10.1007/BF01390728),
  Invent. Math. 70 (1982), Theorem 2;
- É. Fouvry, E. Kowalski and Ph. Michel,
  [*A study in sums of products*, arXiv:1405.2293v2](https://arxiv.org/abs/1405.2293),
  Theorem 1.5 and Corollaries 1.6--1.7;
- Djordje Milićević and Sichen Zhang,
  [*Distribution of Kloosterman paths to high prime power moduli*, arXiv:2005.08865v1](https://arxiv.org/abs/2005.08865),
  Theorem 4;
- Todd Cochrane and Andrew Granville,
  [*Mixed character sums modulo prime powers*, arXiv:2604.02614v1](https://arxiv.org/abs/2604.02614),
  Theorems 1.1, 3.1, 5.1 and 20.1;
- Zongkun Zheng,
  [*Primes in simultaneous arithmetic progressions*, arXiv:2512.22798v1](https://arxiv.org/abs/2512.22798),
  Lemmas 2.7, 2.8 and 2.10;
- Jie Wu and Ping Xi,
  [*Arithmetic exponent pairs for algebraic trace functions and applications*, arXiv:1603.07060v5](https://arxiv.org/abs/1603.07060),
  Theorem A.1;
- Alexandru Pascadi,
  [*Non-abelian amplification and bilinear forms with Kloosterman sums*, arXiv:2511.08445v2](https://arxiv.org/abs/2511.08445),
  Theorems 1.1 and 7.1 and Corollary 7.9;
- Valentin Blomer and Alexandru Pascadi,
  [*Bilinear forms with Kloosterman sums via quadratic characters*, arXiv:2607.24311v1](https://arxiv.org/abs/2607.24311),
  Theorems 1.1 and 5.5;
- Djordje Milićević, Xinhua Qin and Xiaosheng Wu,
  [*Bilinear forms with Kloosterman sums and moments of twisted L-functions*, arXiv:2511.07550v1](https://arxiv.org/abs/2511.07550),
  Theorem 1.1;
- Sandro Bettin and Vorrapan Chandee,
  [*Trilinear forms with Kloosterman fractions*, arXiv:1502.00769v1](https://arxiv.org/abs/1502.00769),
  Theorem 1 and Remark 1;
- Thomas Wright,
  [*Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions*, arXiv:2604.25177v2](https://arxiv.org/abs/2604.25177),
  Theorem 2.1 and its dispersion corollaries;
- J. Bourgain and M. Z. Garaev,
  [*Kloosterman sums in residue rings*, arXiv:1309.1124v1](https://arxiv.org/abs/1309.1124),
  Theorems 3 and 5.

The refreshed search found no later audited theorem whose statement
simultaneously accepts arbitrary varying composite \(M\), all full prime
powers including \(2\), the centered fourfold trace, the coupled moving symbol
(2.5), and the \(b,d,u,n,m\) aggregation.  This is a source-hypothesis result,
not a claim that no future reduction to a known theorem can exist.

## 7. Recommended state effect

**Promote a narrowly stated capacity-barrier lemma; retain every analytic M1
target open.**  The promotable statement is (1.2)--(1.6): with the exact
normalized rows, the \(U=D\) Fejer target is \((D/B)A_{82}^2\), a full-degree
deep graph has normalized energy gap \(\Gamma_{82}^2\), and the compulsory
square root returns the original Round-82 gap \(\Gamma_{82}\).  At the top
endpoint the same fact is \(J^{1/6}\) in energy versus \(J^{1/12}\) in the
linear operator.  There is no unmatched loss and no strict gain.

Record the canonical obstruction as the strict high-degree varying-modulus
actual-symbol Fejer energy \(\mathcal E_{\rm strict}\), together with the
one-count diagram (3.8)--(3.10).  Do **not** promote the stronger sentence that
(90.6) is algebraically identical to (90.5), and do not merge linear owners
with squared-energy owners.  Exact completion/inversion is a self-return only
inside \(\mathcal E_D\); Fejer/Cauchy remains one-sided.

Before any literal self-return promotion, require a single coefficient ledger
starting from (3.4), expanding (3.5), proving (3.6) with all label ranges,
reassembling every local descent and residual cell once, and ending at the
incidence decomposition (3.8).  The global \(u=0\) term must be the whole
\(D\sum|\mathcal A_{b,d}|^2\); a full-\(|D_D|^2\) same-group square is only a
domination package and may not be added as a second exact owner without an
explicit centered/diagonal decomposition.

Reject as routes to a strict non-return: duplicate \(M^{-2}\), duplicate
\(Q^{-5/12}\), sparse-frequency Fejer saving, \(p^j\) rather than \(p^{2j}\)
completed descent, omission of nonzero modulus multiples, re-ownership of
\(u=0\), incomplete local-cell reassembly, or another local period
classification with full survivor degree.

Retain open `M9-M1-bad-prime-cellwise-period-graph-bound` beyond its accepted
cellwise scope, `M9-M1-residual-upper-conductor-offdiagonal-reduction` beyond
its current reduction statement, and full `M9-M1`.  The next core attack must
prove cancellation in the complete joint actual symbol or a genuine fixed
power reduction of both directed degrees; none of the audited primary sources
currently supplies that theorem.
