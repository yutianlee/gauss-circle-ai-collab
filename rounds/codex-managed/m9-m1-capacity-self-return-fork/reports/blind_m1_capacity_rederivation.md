# Round 90 blind M1 capacity rederivation

## 1. Result: statement-only no-go lemma and sharp verdict

**No-go lemma.**  From the frozen packet one can prove an exact scalar
squaring identity for the capacity ledger, but one cannot prove a literal
operator self-return and one cannot prove a strict non-return.  If

\[
 A_{82}:={C^3\over TQ^{5/12}},\qquad Y_{82}:={J^2\over T},
\]

and, suppressing the harmless flexible \(X^\varepsilon\) factor,

\[
 A_{\rm deep}(\Delta):=DB^3\Delta T^4Q^{-5/6},\qquad
 Y_{\rm deep}:={D\over B}J^{14/5},
\]

then the displayed normalizations imply

\[
 Y_{\rm deep}={D\over B}Y_{82}^2,
 \qquad
 A_{\rm deep}(\Delta)
 ={D\over B}{\Delta\over B^2}A_{82}^2,
 \qquad
 \Gamma_{\rm deep}(\Delta)
 ={\Delta\over B^2}\Gamma_{82}^2.                 \tag{R90.1}
\]

Consequently a full-degree deep graph has exactly the squared Round-82
gap at the level of powers and scalar majorants.  After the correct
square root,

\[
 \sqrt{\Gamma_{\rm deep}(\Delta)}
 =\Gamma_{82}\sqrt{\Delta/B^2};                    \tag{R90.2}
\]

for \(\Delta=B^2\) this equals \(\Gamma_{82}\).  This is not an
operator identity: the packet does not provide the complete-cell
partition, descent inversion, owner map, or norm-preserving transform
linking (90.6) back to (90.5).  The Round-89 \(q=8\) control moreover
leaves a full-degree survivor, so the supplied capacity majorant has no
strict power gain.

**Sharp verdict:** the packet proves scalar equal-capacity return after
square-root normalization, but it does **not** prove literal
self-return of the actual-symbol operator.  It also does **not** prove
a strict non-return.  The dichotomy is stopped at the named
**complete-cell/descent inverse-transform and one-count ownership
seam**.

## 2. Exact statement and hypotheses

Assume only the frozen packet's statements:

- \(J=X^{1/2}\), \(Q=J^{2/5}\), \(T=J^{3/5}\), \(B=C/T\),
  \(M\asymp B\), and \(B=J^{3/20}\) for the top-gap test;
- the row normalization \(M^{-1}\) and row bound
  \(TQ^{-5/24}\), hence the stated four-row factor \(Q^{-5/6}\);
- the capacity majorant (90.1), the deep target (90.2), and the
  Round-82 majorant and target in (90.8);
- the endpoint formulas (90.5)--(90.7), the asserted one-count
  \(u=0\) centering, the accepted deletion list, the strict-survivor
  support, and the asserted Round-89 \(q=8\) full-degree control.

Then:

- the three identities (R90.1) hold algebraically (with equality of
  powers and with the usual absorption of a changed
  \(X^\varepsilon\));
- at \(B=J^{3/20}\),

  \[
  \Gamma_{82}=J^{1/12},\qquad
  \Gamma_{\rm deep}(\Delta)
  =J^{1/6}{\Delta\over B^2};                         \tag{R90.3}
  \]

- hence \(\Gamma_{\rm deep}=o(J^{1/6})\) is equivalent, within the
  frozen capacity formula, to \(\Delta=o(B^2)\); a fixed strict power
  gain \(J^{-\eta}\) requires
  \(\Delta\ll B^2J^{-\eta}\), unless an additional operator-norm
  gain not present in (90.1) is proved;
- neither the exact reassembly identity nor such an additional norm
  gain follows from the packet.

No claim is made outside the transition-flattened smooth nonaxial M1
first band.

## 3. Proof and capacity derivation

First,

\[
 T^4Q^{-5/6}
 =J^{12/5}J^{-1/3}=J^{31/15}.
\]

Dividing (90.1) by (90.2) therefore gives

\[
 {DB^3\Delta J^{31/15}\over (D/B)J^{14/5}}
 =\Delta B^4J^{-11/15},
\]

which reproduces (90.3).  The Round-82 ratio is independently

\[
 {C^3/(TQ^{5/12})\over J^2/T}
 ={B^3T^3Q^{-5/12}\over J^2}
 =B^3J^{9/5-1/6-2}
 =B^3J^{-11/30}.                                    \tag{R90.4}
\]

Since \(Y_{82}^2=J^4/T^2=J^{14/5}\) and
\(A_{82}=B^3T^2Q^{-5/12}\), direct squaring gives (R90.1).  Thus
(90.9) is more than a coincidental equality of endpoint exponents: the
deep target is \((D/B)\) times the square of the Round-82 target, and
the deep scalar majorant is the same multiple of the squared Round-82
majorant, with the additional density factor \(\Delta/B^2\).  What is
not supplied is an equality of the underlying operators or norms.

At \(B=J^{3/20}\),

\[
 B^4J^{-11/15}=J^{3/5-11/15}=J^{-2/15},
\]

and \(B^2=J^{3/10}\).  Therefore

\[
 g(\delta):=\delta B^4J^{-11/15}
 =J^{1/6}{\delta\over B^2}.                          \tag{R90.5}
\]

This proves the top-gap criterion in Section 2.

For the requested roundwise ledger, let
\(\delta_r^-\), \(\delta_r^0\), and \(\delta_r^+\) denote the maximum
degrees of the before, removed, and surviving physical edge sets at
round \(r\), wherever that edge-set representation applies.  The only
ledger determined by the packet is the following.  An entry
\(g(\delta)\) is an exact consequence of (90.3), not a claim that the
three entries add.

| Stage | \(\Gamma_{\rm before}\) | \(\Gamma_{\rm removed}\) | \(\Gamma_{\rm survivor}\) | Information actually fixed by the packet |
|---|---:|---:|---:|---|
| R82 | precursor gap not separated | accepted same-residue/fixed-offset owners are target-safe, but no individual gap is supplied | \(\Gamma_{82}=B^3J^{-11/30}\) for the named coherent correlation | gives the post-owner coefficientwise/triangle majorant, not an additive split |
| R83 | \(g(\delta_{83}^-)\) | \(g(\delta_{83}^0)\) | \(g(\delta_{83}^+)\) | no R83 package, degrees, or transform ledger is supplied |
| R84 | \(g(\delta_{84}^-)\) | \(g(\delta_{84}^0)\) | \(g(\delta_{84}^+)\) | no R84 package, degrees, or transform ledger is supplied |
| R85 | \(g(\delta_{85}^-)\) | \(g(\delta_{85}^0)\) | \(g(\delta_{85}^+)\) | no R85 package, degrees, or transform ledger is supplied |
| R86 | \(g(\delta_{86}^-)\) | \(g(\delta_{86}^0)\) | \(g(\delta_{86}^+)\) | no R86 package, degrees, or transform ledger is supplied |
| R87 | \(g(\delta_{87}^-)\) | target-safe for the named full-prime-power same-group package; exact \(g\) absent | \(g(\delta_{87}^+)\) | survivor degree and one-count partition are absent |
| R88 | \(g(\delta_{88}^-)\) | target-safe for the named coarse shells and qualifying good-prime fibres; exact \(g\) absent | \(g(\delta_{88}^+)\) | survivor degree and one-count partition are absent |
| R89 | \(g(\delta_{89}^-)\) | target-safe for the named bad-prime cells/unions; exact \(g\) absent | \(g(\delta_{89}^+)\); the \(q=8\) control permits \(\delta_{89}^+\asymp B^2\), hence \(\Gamma\asymp J^{1/6}\) | the worst surviving capacity remains full-degree |

This table cannot be sharpened from qualitative target-safety.  Maximum
degree is not additive under a partition: for
\(\mathcal E=\mathcal F\sqcup\mathcal G\), all three of
\(\Delta(\mathcal E)\), \(\Delta(\mathcal F)\), and
\(\Delta(\mathcal G)\) can be of order \(B^2\).  Thus deleting any
number of target-safe named strata does not imply a degree saving for
the union that remains.  The stated \(q=8\) fibre realizes precisely
this obstruction at the level of the accepted capacity ledger.

## 4. First doubtful or unproved step

The first failed audit is the first test in the prescribed order: CRT
partition followed by summation over complete local cells.  A literal
self-return would require an identity of the form

\[
 \mathcal O_{82}
 =\mathcal O_{\rm previously\ owned}
  +\sum_{\kappa\in\mathscr C}
    \sum_{\xi\in\mathscr F_\kappa}
    \mathcal I^{-1}_{\kappa,\xi}
       \mathcal O_{\kappa,\xi},                      \tag{R90.6}
\]

where \(\mathscr C\) is a disjoint complete-cell partition,
\(\mathscr F_\kappa\) is the complete supported descent-frequency set,
and the summands include reversal/transposition, both signs, all parity
classes and modulus multiples, the moving stationary weights, and the
centered \(u=0\) term exactly once.  The packet displays the endpoint
operators (90.5) and (90.6), but supplies none of the sets, coefficients,
inverse-transform constants, or owner incidences needed to state, much
less prove, (R90.6).

The four factors in \(\Omega\) do not themselves prove that (90.6) is
a norm square of (90.5).  In particular, the phase tensor
\(\mathfrak T_M\), the ranges of \(u,A,B_2,V\), the extra normalization
between \(M^{-5}\) and the formal square of \(M^{-2}\), and the
centered-diagonal subtraction have not been related by an isometry or
inverse-completion formula.  Hence (R90.1) is a scalar-majorant identity,
not a literal squared-operator normalization.

Because the right side of (R90.6) is not defined in the frozen packet,
even a literal residual
\(\mathcal O_{82}-\text{(reassembled deep operator)}\) cannot be written
from permitted data.  This is the first underdetermined seam.  The
second, conditional on closing it, is the absence of either
\(\Delta=o(B^2)\) or a separate cancellation norm for the actual
stationary symbol.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `capacity_ledger` | **Partial pass / not closed.** The scalar formulas (R90.1)--(R90.5) and the symbolic R82--R89 table are forced. Round-specific degrees and before/removed/survivor owner splits are absent. |
| `Q_power_normalization` | **Pass.** Four factors \(Q^{-5/24}\) give \(Q^{-5/6}\); equivalently each physical pair gives \(Q^{-5/12}\). The ordered-pair \(M^{-2}\) is already in the coefficient and was not counted again. |
| `complete_cell_reassembly` | **Not established.** No disjoint cell partition, exhaustive index set, or reassembly identity is stated. |
| `completed_descent_inverse_transform` | **Not established.** Supported frequencies and inverse constants are absent. |
| `global_diagonal_one_count` | **Asserted but not independently verified.** The packet names \(\mathcal K_D^\circ=|D_D|^2-D\); it does not give the incidence calculation showing that every reassembled \(u=0\) copy occurs once. |
| `prior_package_ownership` | **Not established.** Deletions are declared target-safe, but there is no round-indexed disjoint owner map and no proof that reassembly neither drops nor reinserts them. |
| `all_class_sign_modulus_multiple` | **Endpoint assertion only.** These components are declared present in (90.5), but their exhaustive return from (90.6) is not demonstrated. |
| `actual_stationary_symbol_support` | **Not established.** The moving weights and deep support are asserted, while \(\mathfrak T_M\), its support, and its inverse image are not specified. |
| `top_J_one_sixth_control` | **Pass.** Equations (R90.3) and (R90.5) give \(J^{1/6}\) for full degree, and the packet's \(q=8\) control says such a surviving fibre exists. |
| `literal_self_return_or_strict_nonreturn` | **Neither proved.** Scalar square-root capacity returns, literal operator return is unproved, and no \(J^{-\eta}\) survivor saving is present. |
| `downstream_scope` | **Pass.** No conclusion is extended beyond the frozen M1 first-band scope. |

The decisive falsification test for a claimed strict non-return is
(R90.5): substituting the packet's full-degree \(q=8\) survivor returns
\(J^{1/6}\), not \(o(J^{1/6})\).  The decisive missing test for literal
self-return is evaluation of (R90.6) with all owners and supported
frequencies included.

## 6. Dependencies and exact artifacts used

The derivation used only:

- `rounds/codex-managed/m9-m1-capacity-self-return-fork/briefs/blind_m1_capacity_rederivation.md` as the task and isolation contract;
- `rounds/codex-managed/m9-m1-capacity-self-return-fork/derivation_packet.md`, including its authorized (90.8)--(90.9) addendum, as the sole mathematical input;
- starting graph digest
  `bd5eed1e732c8872b37c0ea51bc9cea65419fe3241c17a981df3c2a36cd2c0f1`.

No prior report, review, strategy file, source card, web source, shared
proof-state file, or numerical experiment was used.  All computations
above are direct exponent and normalization algebra.

## 7. Recommended state effect

**Original statement-only recommended state effect: no change to the
accepted claim graph.**
Retain (R90.1)--(R90.5) as candidate ledger evidence: they establish
that the deep full-degree gap is the scalar square of the Round-82 gap
and that its correctly normalized square root returns to
\(J^{1/12}\).  Do not promote either literal operator self-return or a
strict non-return.

To close the round, require a seam artifact giving the exact identity
(R90.6): complete cells, every descent frequency and inverse constant,
sign/transposition and class/multiple coverage, actual stationary
support, and a one-count owner incidence table.  If that identity
holds with comparable norms, promote the canonical core (90.5) as a
literal self-return barrier.  If it fails, the failure must be written
as a literal residual operator and accompanied by either
\(\Delta\ll B^2J^{-\eta}\) or an independent \(J^{-\eta}\) norm gain.
The present packet supplies neither closing datum.

### Supplemental post-isolation seam audit

This supplemental audit uses only the four exact claims subsequently
supplied by the conductor.  It supersedes the statement-only state
recommendation immediately above, while leaving the original blind
diagnosis intact as an account of what the derivation packet alone
proved.  Throughout, residue sums are over complete residue systems,
the integral on the circle is normalized Haar measure, and a
"partition" is understood to be both disjoint and exhaustive.

#### Fourier identification and ownership

Write

\[
 H_{b,D}(\theta)=\sum_d h_{b,D}(d)e(d\theta).
\]

The supplied coefficient identity gives

\[
 h_{b,D}(d)
 ={1\over M^2}\sum_n
 \left(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\right)
 I_b(n+d)\overline{I_b(n)}.                         \tag{R90.7}
\]

Thus summing the Fourier coefficients over \(b\) and \(d\) is exactly
the centered canonical operator (90.5), with no further scalar or
\(M\)-normalization to recover.  This identifies the Round-82 core as
the linear Fourier data of \(H_{b,D}\).

Next, the supplied assertion that

\[
 E_D=\sum_b\int_{\mathbb T}|D_D(\theta)|^2
                    |H_{b,D}(\theta)|^2\,d\theta    \tag{R90.8}
\]

has one global \(u=0\) owner and disjoint successive
R87/R88/R89/hard-edge partitions closes the previously missing owner
incidence at the energy level.  Expansion of \(|H_{b,D}|^2\) is the
four-row Gram expansion; disjoint exhaustiveness means that the removed
packages plus the hard survivor reassemble to (R90.8) once and only
once.  In particular, the centered diagonal is not separately
reinserted at every local cell.

#### Completed descent and inverse completion

For

\[
 \mathfrak T_q(u)=q\sum_{y\bmod q}w_q(y)e_q(uy),
\]

character orthogonality gives the exact inversion

\[
 \begin{aligned}
 q^{-2}\sum_{u\bmod q}\mathfrak T_q(u)e_q(-ux)
 &=q^{-1}\sum_{y\bmod q}w_q(y)
       \sum_{u\bmod q}e_q(u(y-x))\\
 &=w_q(x).                                           \tag{R90.9}
 \end{aligned}
\]

There is no missing factor of \(q\).  If \(q=p^jq'\), the map
\(u'\bmod q'\mapsto p^ju'\bmod q\) is a bijection onto the descended
frequency lattice, and

\[
 q^{-2}\mathfrak T_q(p^ju')
 =(p^jq')^{-2}p^{2j}\mathfrak T_{q'}(u')
 =q'^{-2}\mathfrak T_{q'}(u').                      \tag{R90.10}
\]

Also \(e_q(-p^ju'x)=e_{q'}(-u'x)\).  Hence completed summation over
the full supported descended lattice is exactly the \(q'\)-inverse
sum.  Together with the complete-cell partition in (R90.8), this
returns the actual weight on every cell and closes the
complete-cell/descent inverse-transform seam.  The word "completed" is
essential: (R90.10) alone would not justify dropping any supported
off-lattice frequency.

#### Toeplitz control and the correct square root

The supplied Toeplitz inequality is valid, and in fact admits the
slightly sharper constant \(2/(D+1)\).  Put

\[
 A(\theta)=\sum_{j=1}^D a_je(j\theta),\qquad
 P_k=\sum_{j=1}^k a_j,\qquad S=P_D,
\]

and take \(D_D(\theta)=\sum_{r=1}^D e(r\theta)\); a translate of this
Dirichlet kernel gives the same calculation.  Parseval applied to
\(D_DA\) yields

\[
 \int_{\mathbb T}|D_D|^2|A|^2
 =\sum_{k=1}^D|P_k|^2
  +\sum_{k=1}^{D-1}|S-P_k|^2.                       \tag{R90.11}
\]

For each \(k<D\),
\(|P_k|^2+|S-P_k|^2\geq |S|^2/2\), while
\(|P_D|^2=|S|^2\).  Therefore

\[
 \int_{\mathbb T}|D_D|^2|A|^2
 \geq {D+1\over2}|S|^2,
\]

and hence

\[
 \left|\sum_{j=1}^D a_j\right|^2
 \leq {2\over D+1}\int|D_D|^2|A|^2
 \leq {2\over D}\int|D_D|^2|A|^2.                 \tag{R90.12}
\]

Apply (R90.12) for each \(b\), then Cauchy over the \(\asymp B\)
values of \(b\).  For the reassembled linear Round-82 quantity
\(L_{82}\), this gives, up to an absolute constant,

\[
 |L_{82}|^2\ \ll\ {B\over D}E_D.                   \tag{R90.13}
\]

The outer factor is exactly the one required by the ledger:

\[
 {B\over D}Y_{\rm deep}=Y_{82}^2,
 \qquad
 {B\over D}A_{\rm deep}(B^2)=A_{82}^2.             \tag{R90.14}
\]

Thus taking the square root of the full-degree Gram estimate returns
both the Round-82 target and its \(J^{1/12}\) normalized gap, up to an
absolute constant.  Equivalently, the deep \(J^{1/6}\) gap is exactly
the squared energy version of the Round-82 gap, not an additional
analytic loss.

#### Supplemental verdict and revised state effect

Under the supplied exact claims, **the seam closes at the Gram level**.
Equations (R90.7)--(R90.10) identify the canonical Fourier data, give
one-count exhaustive energy reassembly, and make completed local
descent lossless.  Equations (R90.12)--(R90.14) then certify a
square-root equal-capacity barrier.  The canonical barrier is the
centered all-class actual-unit correlation (90.5), equivalently the
Fourier coefficient family of \(H_{b,D}\), and its Gram lift is
\(E_D\).

This is **not** a linear involution.  The passage
\(H_{b,D}\mapsto |H_{b,D}|^2\), the Toeplitz estimate, and Cauchy over
\(b\) are quadratic or one-way inequalities and do not reconstruct the
phase of \(H_{b,D}\).  What returns exactly is the complete Gram energy
and, after square root with the \(B/D\) normalization, its analytic
capacity.

**Revised recommended state effect: promote the Gram-level,
square-root equal-capacity barrier, but do not promote a linear
operator involution.**  The Round-89 full-degree control remains the
sharp obstruction to claiming a strict non-return: without a new
degree or norm saving, its \(J^{1/6}\) energy gap square-roots back to
the original \(J^{1/12}\) Round-82 gap.
