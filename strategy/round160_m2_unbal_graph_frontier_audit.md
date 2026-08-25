# Round 160 M2-UNBAL graph-frontier audit

Date: 2026-08-25

Authoritative graph SHA-256:
`4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d`

This is a strategy report. It changes no proof status.

## 1. Result

The M2 strict-UNBAL flat packet is still open, but its old attack surfaces
are exhausted much more sharply than the short title of the open node
suggests. The exact remaining scalar is not an unspecified divisor sum or
a scalar Kloosterman sum. After the accepted zero-frequency deletion it is
the fully gcd-restored, centered, nonzero inverse-selector matrix

\[
 \mathscr R^\circ_{D,L}(X)=
 \sum_{\substack{g,n\ \mathrm{odd}\\gn\asymp R}}
 \chi _4(g)W\!\left(\frac{X}{gnD}\right)
 \sum_{1\le h<n}\widehat\gamma_{g,n}(h)
 S^{\chi _4}_{\infty0}(4N_0,h;2n),
\tag{160.1}
\]

with target

\[
 \boxed{\mathscr R^\circ_{D,L}(X)
 \ll_\varepsilon X^{1/4+\varepsilon}.}
\tag{160.2}
\]

The recommended genuinely non-redundant Round-160 candidate is an
**inverse-selector additive-reciprocity and projective-decomposition
gate**. It must insert additive reciprocity inside
\(\widehat\gamma_{g,n}(h)\), before a positive modulus norm, and decide
whether the resulting shorter-modulus \(j\)-family has an owner-saving
common-test, vector, or direct signed estimate. This attacks the first
unproved coefficient interface identified in Round 143. It does not repeat
the direct Bettin--Chandee/Wright map, rowwise Kuznetsov, the folded
majorant, or another full Fourier inversion.

The proposed campaign ID is
`m9-m2-unbalanced-inverse-selector-reciprocity-gate`. Its preferred exit
labels are:

- `inverse_selector_reciprocity_target`;
- `strict_reciprocity_matrix_range`;
- `inverse_selector_projective_capacity_no_go`.

If the last exit occurs, the strict flat UNBAL lane should be parked again
and the conductor should rotate to a different mandatory M2 owner rather
than reopen one of the mechanisms already closed below.

## 2. Exact statement and hypotheses

Write

\[
 X=N_0+\xi,\qquad N_0=\lfloor X\rfloor,\qquad 0\le\xi<1,
\]

\[
 D=X^\delta,\quad L=X^\ell,\quad
 R=\frac XD,\quad K=\frac{XL}{D^2},\quad
 \Delta=\frac RK=\frac DL,
\tag{160.3}
\]

under the accepted flat-smooth strict-UNBAL hypotheses

\[
 \frac14\le\delta<\frac12,\qquad
 0\le\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463.
\tag{160.4}
\]

For \(r=gn\), \(k=gj\), \((j,n)=1\), retain the literal support,
profiles, entries, exits, and real-centre factor in

\[
 b_{g,n}(j)=
 \frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n),
\tag{160.5}
\]

and define on \(\mathbb Z/n\mathbb Z\)

\[
 \gamma_{g,n}(m)=
 \begin{cases}
 b_{g,n}(\overline m_n),& (m,n)=1
 \text{ and }\overline m_n\text{ is in the literal support},\\
 0,&(m,n)>1,
 \end{cases}
\]

\[
 \widehat\gamma_{g,n}(h)=
 \frac1n\sum_{m\bmod n}\gamma_{g,n}(m)e(-hm/n).
\tag{160.6}
\]

The exact Round-143 identity is (160.1), with the \(h=0\) contribution
already \(O_\varepsilon(X^\varepsilon)\). Positive representatives
\(1\le h<n\) avoid importing an unaudited opposite-sign trace formula.
Equivalently, in ordinary Kloosterman notation (160.1) has the external
factor \(\chi _4(g)\chi _4(n)\) and \(S(N_0,h;n)\). Neither character may
be removed before the final scalar estimate.

The Round-160 mechanism starts from the exact reciprocity identity

\[
 e\!\left(-\frac{h\overline j_n}{n}\right)
 =e\!\left(\frac{h\overline n_j}{j}-\frac{h}{jn}\right),
 \qquad (j,n)=1.
\tag{160.7}
\]

Consequently

\[
 \widehat\gamma_{g,n}(h)
 =\frac1n
 \sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}
 \frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n)
 e\!\left(\frac{h\overline n_j}{j}-\frac{h}{jn}\right),
\tag{160.8}
\]

where \(\mathcal J_{g,n}\) is the literal moving \(j\)-support and
\(j\asymp K/g<n\asymp R/g\). The round must prove either (160.2), or an
owner-complete strict subrange, or a rigorous norm/capacity obstruction for
every lawful use of (160.8). A decomposition counts as progress only if it
keeps the full \(h\ne0\) matrix and has a complete projective, modulus
Sobolev, Bessel-bandwidth, level-\(4/8\), profile, and endpoint ledger.

The equivalent raw product-phase target remains

\[
 \mathcal T_{L,K}\ll_\varepsilon (LK)^{3/4}X^\varepsilon.
\tag{160.9}
\]

Round 107 proves the normalization equivalence between (160.9) and the
physical target (160.2) for the frozen flat smooth owner. This campaign
would not by itself cover sharp, clipped, starred, hard, arithmetic-owner,
or transition packets.

## 3. Proof or derivation of the strategy choice

The authoritative graph has exactly one open UNBAL analytic target,
`M9-M2-smooth-unbalanced-three-quarter-estimate`. Its next action says that
the survivor after the exact \(h=0\) deletion is the fully gcd-restored
centered nonzero inverse-selector matrix and that the audited scalar
trace-formula route is parked. The graph therefore rules out another round
whose only novelty is a theorem name applied to a fixed \(g\), fixed
\(h\), or positive row norm.

Equation (160.7) is exact: the classical congruence

\[
 j\overline j_n+n\overline n_j\equiv1\pmod{jn}
\]

gives
\(\overline j_n/n+\overline n_j/j\equiv1/(jn)\pmod1\), and hence
(160.7). Substitution into the defining Fourier transform gives (160.8)
without completing the \(j\)-interval, changing the centre, or deleting a
gcd stratum.

This changes the precise coefficient question. Round 143 could not supply
a common modulus test because the map \(j\mapsto\overline j_n\) and its
support moved roughly with \(n\). In (160.8), the nonsmooth arithmetic
dependence is instead periodic in \(n\bmod j\), with the strictly shorter
modulus \(j\asymp K/g\), while

\[
 e(-h/(jn)),\quad e(\xi j/n),\quad
 q_L(4Xj/(gn^2)),\quad W(X/(gnD))
\]

remain literal smooth factors on fixed dyadic cells. Thus the gate asks a
finite, falsifiable question: after splitting the necessary two-adic and
\(n\bmod j\) classes, does the exact family admit a common-test or direct
signed estimate whose total class/projective price is smaller than the
required saving, or does the class count restore the old capacity?

Let \(a=\delta-\ell\). The accepted flat envelope has exponent

\[
 \beta(a)=\min\left(a,\frac{1-a}{2}\right)>\frac14.
\]

Therefore every proposed decomposition must save, uniformly on its claimed
range,

\[
 X^{\beta(a)-1/4}=
 \begin{cases}
 X^{a-1/4},&1/4<a\le1/3,\\
 X^{(1-2a)/4},&1/3\le a<1/2.
 \end{cases}
\tag{160.10}
\]

At the contact point \(a=1/3\), the missing factor is \(X^{1/12}\).
This ledger prevents a merely formal shorter modulus from being called a
saving.

The candidate is non-redundant for one narrow reason: no prior UNBAL round
tested (160.7) inside the already-centered \(h\ne0\) level-four matrix and
priced the resulting \(n\bmod j\) decomposition before a norm. Round 135
tested direct, square-connector, completion, and physical-determinant maps
of the original scalar. Round 143 tested fixed-index scalar trace formulas,
row Parseval, interpolation, and full \(h\)-inversion. The present gate
starts after both reductions and attacks their common missing coefficient
interface.

A useful three-task design is:

1. a statement-only derivation of (160.8), all parity cases, moving support
   faces, and exact reconstruction;
2. a discovery attack on the direct signed \((j,n,h,g)\) scalar and on a
   low-projective-cost common-test decomposition, with the full power
   ledger (160.10);
3. a hostile audit that tests primitive \(g=1\), long \(h\), residue-class
   inflation, self-return, and every source hypothesis.

## 4. First doubtful or unproved step

The first unproved step is not additive reciprocity. It is the claim that
the periodic \(n\bmod j\) dependence in (160.8) can be used without paying
all \(\varphi(j)\) residue classes, all long \(h\)-frequencies, or an
equivalent projective/Sobolev norm that restores the accepted envelope.

In particular, the primitive stratum \(g=1\) must be estimated on its own
terms. Any claimed gain obtained only by cancellation in the outer
\(\chi _4(g)\)-sum is insufficient, because the previous positive norm
ledgers are dominated by small \(g\), including \(g=1\). Likewise, full
summation over \(h\) is not a solution: Fourier inversion gives the
original reciprocal row exactly. The round succeeds only if the centered
\(h\ne0\) restriction and the short modulus \(j\) interact before that
self-return.

If a fixed-level trace formula is used after (160.8), the next unproved
step is a source-legal common test or vector-valued theorem with all
odd-weight holomorphic, Maaß, exceptional, Eisenstein, level-eight
oldclass, and singular-cusp pieces. Existing scalar sources do not accept
the literal matrix automatically.

## 5. Required control tests and current outcomes

1. **Reciprocity sign and normalization.** Verify (160.7) for both signs
   and every coprime parity case. Outcome in this audit: pass by the CRT
   congruence above. Even \(j\) is allowed and must not be silently dropped.
2. **Exact reconstruction.** Sum all \(h\bmod n\) after (160.8). Outcome:
   it must return the original reciprocal row; this is a self-return
   control, not a gain. The already-safe \(h=0\) term is subtracted once.
3. **Primitive-gcd control.** Run the complete ledger at \(g=1\) before
   crediting any outer-character cancellation. Outcome: no accepted bound
   currently supplies the missing power there.
4. **Residue/projective price.** Count the exact \(n\bmod j\) classes and
   the total common-test Sobolev/Bessel norm. Pass requires a net saving at
   least (160.10); a shorter displayed modulus alone fails.
5. **Long-frequency control.** Treat every \(1\le h<n\), not only the
   Linnik range \(h\ll K/(Lg^2)\). The accepted source range covers at most
   \(O(1/(Dg))\) of the row and eventually no nonzero integer.
6. **Signed-versus-unsigned control.** The argument must use the literal
   \(\chi _4(g)\chi _4(n)\) directions before positive modulus norms and
   must not also prove the arbitrary-unit-phase analogue. Row Parseval,
   Schatten, complete Kloosterman second moment, and coefficientwise
   majorization fail this test.
7. **Endpoint and scope control.** Preserve the moving \(j\)-support,
   zero extension, real-centre factors, two-adic classes, and all fixed-flat
   support entries and exits. Passing the flat packet does not certify
   sharp, clipped, starred, transition, hard-TOP, or BAL owners.
8. **Boundary-power control.** Test (160.10) near \(a=1/4\), at
   \(a=1/3\), and near \(a=1/2\). The current accepted envelope remains
   strictly above the target at every strict point; no uniform extra margin
   may be inferred at the open faces.

## 6. Dependencies and exact artifacts used

Minimal accepted graph dependencies for the candidate are:

- `M9-M2-smooth-dual-three-quarter-equivalence`;
- `M9-M2-character-factor`;
- `M9-M2-dyadic-weight-nondegeneracy`;
- `M9-M2-unbalanced-truncated-divisor-fixed-centre-return`;
- `M9-M2-unbalanced-flat-wave-curvature-envelope`;
- `M9-M2-unbalanced-Kloosterman-dispersion-interface-obstruction`;
- `Level-four-Kuznetsov-matrix-source-audit`;
- `M9-M2-unbalanced-level-four-spectral-matrix-obstruction`.

The target node is
`M9-M2-smooth-unbalanced-three-quarter-estimate`; a successful flat-packet
result would still require extension to its literal nonflat owners before
it could imply `M9-M2-physical-one-count-assembly`.

Exact files read for this audit were:

- `protocol.md`;
- `state/proof_obligations.yml` at the hash printed above;
- `state/round_ledger.yml`;
- `strategy/conductor_0823_full_proof_strategy.md`;
- the syntheses of the Codex-managed UNBAL campaigns in Rounds 107, 118,
  123, 124, 125, 134, 135, and 143;
- `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/candidates/conductor_round143_level_four_matrix_obstruction.md`;
- the exact coefficient and source-capacity passages of
  `rounds/codex-managed/m9-m2-unbalanced-level-four-kuznetsov-matrix-gate/reports/kuznetsov_source_hypothesis_audit.md`;
- the literal dual coefficient definition in
  `rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/blind_statement.md`.

The already-failed route ledger is:

- product regrouping, Mellin functional equations, and \(h\)-process plus
  \(k\)-Poisson return to the width-\(D/L\) fixed-centre wave (Round 107);
- one-dimensional curvature, a single coherent central run, the exact
  centre, ties, and the integer phase-one square sector (Round 118);
- ordinary positive Cauchy Gram, two-adic thinning, exact aliases, and
  fixed-alias first-derivative summation (Round 123);
- double-character stationary transformation, product equality, Hessian
  rank, and the joint principal Legendre transform (Round 124);
- separate positive rows, coefficient-blind sector bounds, repeated
  B-processes, and the incorrectly integral alias lattice (Round 125);
- universal one-sided band-limited majorants, diagonal or lag-count
  closure, and principal-only character Poisson (Round 134);
- direct or square-connector Bettin--Chandee/Wright, smooth-first and
  inverse-first completion, and the fixed-determinant source map
  (Round 135);
- fixed-index scalar Kuznetsov, row Parseval/SVD, exact interpolation,
  complete Kloosterman second moment, short Linnik coverage, and full
  \(h\)-summation (Round 143).

## 7. Recommended state effect

No state mutation is justified by this audit. Retain
`M9-M2-smooth-unbalanced-three-quarter-estimate`, `M9-M2`,
`M9-endpoint-uniformity`, `M9`, `Conditional-bridge`, and `GC-target` as
open, with no exponent change.

For Round 160, freeze only the reciprocity/projective gate above. Promote
something later only if it supplies an exact proof of (160.2), a genuinely
owner-complete strict range, or a rigorous scoped obstruction showing that
the \(n\bmod j\) class/projective price restores the old capacity. Do not
promote additive reciprocity alone; it is an elementary exact identity.
If the gate closes under the no-go label, record it as a method obstruction
and rotate to a distinct mandatory M2 owner.
