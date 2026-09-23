# Round 172 review: power, false-control, owner, and durable-state boundary

Campaign: `m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate`  
Role: independent power/owner/state-effect reviewer  
Verdict: **GREEN for one smallest route-scoped obstruction node, with local
REPAIR to the report wording; RED for every parent, target, or exponent
promotion.**

## 1. Result

The durable conclusion is the scoped
`maximal_fejer_dyadic_character_poisson_no_go`, not (165.K26).

The promotion rulings are:

| Candidate effect | Ruling | Exact boundary |
|---|---|---|
| finite parity--Fejer dyadic reduction | **GREEN** | The stopped-chain identity, short correction, link weights, zero diagonal, doubling tent/Haar formula, and exact final non-doubling link are proved. |
| first-link strict sector | **GREEN as a bound; REPAIR as a state effect** | The first link is target-safe, but its complement is not. Fold it into the reduction/obstruction node; do not create an owner-complete strict-sector node. |
| ordinary-zero sector | **GREEN as an auxiliary transformed sector; REPAIR as a state effect** | It is target-safe only after all character frequencies are recombined in the chosen exact cardinal interpolation. It is not the Round-169 scalar zero mode and should not be a standalone owner node. |
| positive-transform obstruction | **GREEN** | Coefficient-uniform positivity before an actual-symbol saving has sharp top capacity \(L^4X^\varepsilon\), versus the required \(L^3X^\varepsilon\). This is the one durable node. |
| (165.K26), residual scalar, or any downstream owner | **RED** | The signed nonzero ordinary-frequency aggregate remains open. |

Thus a no-graph-change decision would discard a proved route obstruction,
but more than one new node would overstate the owner decomposition. The
smallest sound patch is one proved-internal obstruction node containing the
finite reduction, the two target-safe preliminary pieces, and the exact
scope of the \(L^4\) restoration.

## 2. Exact statement and hypotheses

Let

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,\qquad M\asymp L^2,
\]

and let the complete literal residual coefficient be extended by zero on
an \(M\)-site containing interval. Put

\[
 z_N=c_N^{\rm rem}e(J\sqrt N),\qquad
 D_L=\sum_N|z_N|^2\ll_\eta L^2X^\eta
\]

for every \(\eta>0\), and

\[
 \mathfrak E_R^{(2)}
 =D_L+2\!\sum_{\substack{0<r<R\\2\mid r}}
 \left(1-\frac rR\right)
 \Re\sum_Nz_{N+r}\overline{z_N}.
\]

For the stopped chain \(R_{j+1}=\min(2R_j,M)\), with repetitions removed,

\[
 T_{26}=\frac12\sum_j
 \left(\mathfrak E_{R_{j+1}}^{(2)}-
       \mathfrak E_{R_j}^{(2)}\right)-B_{\rm sh},
\]

\[
 B_{\rm sh}=\sum_{\substack{0<r<R_0\\2\mid r}}
 r\left(\frac1{R_0}-\frac1M\right)
 \Re\sum_Nz_{N+r}\overline{z_N},
 \qquad |B_{\rm sh}|\ll_\eta L^3X^\eta.
\]

For \(R<S\le2R\), the exact link weight is

\[
 b_{R,S}(r)=
 \begin{cases}
 r(S-R)/(RS),&0<r<R,\\
 1-r/S,&R\le r<S,\\
 0,&r\ge S,
 \end{cases}
 \qquad b_{R,S}(0)=0.
\]

At \(S=2R\) this is the triangular tent and has the exact
absolute-site-parity Haar representation. A strict \(R<S<2R\) terminal
link uses this displayed Fejer difference, not a rounded Haar formula.

Under the exact real-cardinal character--ordinary-Poisson transform, the
fully recombined ordinary-zero component satisfies

\[
 \sup_{\epsilon,\theta}|Z_{\epsilon,0}(\theta)|
 \ll_\eta \frac{L^2}{J}X^\eta,
\]

and all bandpass terms with \(\ell=0\) or \(\ell'=0\), recombined over all
odd character frequencies first, are
\(O_\varepsilon(L^3X^\varepsilon)\). The remaining theorem required for
each unclosed link is the complete one-real-part, signed
\(\ell,\ell'\ne0\) aggregate before every positive norm.

## 3. Proof and power derivation

Expanding the two Fejer peaks retains exactly even physical gaps. Ordinary
telescoping gives the displayed identity for \(T_{26}\), while direct
subtraction of the two Fejer weights gives \(b_{R,S}\). Cauchy and zero
extension give \(|C_r|\le D_L\), hence

\[
 |B_{\rm sh}|\ll R_0D_L\ll_\eta L^3X^\eta.
\]

More sharply, summing all positive link weights gives

\[
 \sum_{r=1}^{S-1}b_{R,S}(r)=\frac{S-R}{2}.
\]

Therefore

\[
 \left|\frac{\mathfrak E_S^{(2)}-
                   \mathfrak E_R^{(2)}}2\right|
 \le\frac{S-R}{2}D_L,
 \qquad
 |\mathfrak E_S^{(2)}-\mathfrak E_R^{(2)}|
 \le(S-R)D_L.
\]

For the first link, \(S-R=R_0\asymp L\), so it is
\(O_\eta(L^3X^\eta)\). This proves a literal-coefficient first-link bound,
but no target-safe estimate for the remaining links follows. At a maximal
link, \(S-R\asymp M\asymp L^2\), the same positive estimate is
\(L^4X^\eta\). The still more automatic Fejer-positive estimate
\(|\Delta_{R,S}|\le(R+S)D_L\) has the same top power.

This \(L^4\) endpoint is sharp for the coefficient-uniform interface. Take
\(M=4P\), put \(z_N=1\) on the \(2P\) even sites in \([0,M-1]\), and use
the link \(2P\to4P\). Then \(D_L=2P\) and the exact tent sum is
\(\gg P^2\asymp MD_L\). Equivalently the diagnostic coefficients dechirp
the square-root phase. Choosing the admissible scale family
\(X=L^8\), \(J=L^4\), \(H=L^2\), and \(M\asymp L^2\), one has

\[
 \frac{L^4}{L^3X^{\varepsilon_0}}
 =L^{1-8\varepsilon_0}\longrightarrow\infty
 \quad(0<\varepsilon_0<1/8).
\]

Thus the adversary genuinely falsifies a bound asserted for every
\(\varepsilon>0\) from support, \(D_L\), Parseval, Haar positivity, or a
coefficient-uniform positive transformed norm alone. It is not the actual
residual coefficient and proves no physical lower bound.

For the ordinary-zero sector, cellwise integration by parts costs
\(J^{-1}\) because
\(\partial_y(J\sqrt{dy}+\theta dy)\asymp J\) uniformly on the positive
cells. There are \(O_\eta(L^2X^\eta)\) incidences. Consequently the
zero-containing bandpass terms are bounded by

\[
 (R+S)\left(D_L^{1/2}\frac{L^2}{J}
                 +\frac{L^4}{J^2}\right)X^{O(\eta)}
 \ll L^3X^{O(\eta)},
\]

using \(R+S\ll L^2\), \(D_L^{1/2}\ll_\eta LX^\eta\), and
\(L^2\le J\). For a requested \(\varepsilon\), take every input loss with
\(\eta\le\varepsilon/4\); this supplies the required uniform
\(X^\varepsilon\) statement. Likewise, any future sum over
\(O(\log L)\) proved links would require an epsilon shrink before absorbing
the logarithm; the present round does not prove those links.

The exact transform review repairs the hostile ordering: the cardinal
common-frequency transform and the collectively recombined ordinary-zero
sector are closed. The first open seam is the fully signed nonzero
ordinary-frequency aggregate. Taking a modulus over modes, cells,
openings, or frequency before estimating that aggregate restores the sharp
coefficient-uniform \(L^4\) capacity.

## 4. First doubtful or unproved step

The first unproved affirmative statement is, uniformly for every remaining
stopped-dyadic link, the complete signed \(\ell,\ell'\ne0\) common-frequency
bilinear aggregate of (172.D23)/(R172.10) bounded by
\(L^3X^\varepsilon\), with one outer real part and every literal selector,
parity branch, arithmetic hole, endpoint cell, and transition term
retained.

Neither the first-link estimate nor the ordinary-zero estimate has a
target-safe complement. The Round-169 untwisted complete-scalar zero mode
is a different object and is not an owner or proof of this residual
frequency-family estimate. No report proves or disproves the remaining
actual-symbol aggregate.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| \(L^4\) versus \(L^3\) | **GREEN**: top positive capacity is \(MD_L\asymp L^4X^\eta\); the target is \(L^3X^\varepsilon\). |
| epsilon uniformity | **GREEN after explicit rebudgeting**: choose input \(\eta\) below the requested \(\varepsilon\); one fixed \(\varepsilon_0<1/8\) makes the adversarial falsification asymptotic. |
| first-link power | **GREEN**: width \(R_0\asymp L\) times \(D_L\) is target-safe. |
| first-link owner | **REPAIR**: no target-safe complement, hence no standalone strict-sector promotion. |
| ordinary-zero power | **GREEN collectively**: sum all character modes before the \(\ell=0\) estimate. |
| ordinary-zero owner | **REPAIR**: cardinal-representation auxiliary sector only; not the Round-169 scalar zero mode and not a standalone owner. |
| actual versus adversarial | **GREEN**: the dechirped arrays refute only coefficient-uniform positive routes and are not literal residual lower bounds. |
| physical versus dual diagonal | **GREEN**: zero physical diagonal emerges only after full dual/cell/endpoint recombination. |
| positive-transform scope | **GREEN**: obstruction applies before an actual-symbol saving; it does not forbid a new literal-coefficient positive theorem. |
| residual-only implication | **GREEN**: every new statement is confined to (165.K26) and the complete residual \(t=1\) scalar. |
| parent and exponent scope | **GREEN/no change**: no hard-TOP parent, M9--M2, M9, bridge, theorem, or exponent closes. |

The discovery sharpness example should use the in-range \(M=4P\) control,
and the hostile report should move its first missing gate from the transform
identity to the signed nonzero-mode estimate. These are local report
repairs, not mathematical red flags for the scoped node.

## 6. Dependencies and exact artifacts used

Only the assigned artifacts were used:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/barrier_packet.md`;
5. the three Round-172 reports in this campaign;
6. `rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/reviews/literal_common_frequency_transform_review.md`;
7. `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/synthesis.md`; and
8. `rounds/codex-managed/full-proof-round167-169-strategy-literature-review/synthesis.md`.

No web source, external theorem, or numerical experiment was used.

## 7. Recommended state effect

Create exactly one smallest node:

- **ID:** `M9-M2-hard-top-t1-residual-maximal-fejer-dyadic-positive-transform-obstruction`
- **type/status:** `obstruction` / `proved_internal`
- **dependencies:**
  `M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction` and
  `M9-M2-hard-top-t1-character-poisson-product-collar-obstruction`
- **implies/blockers:** none
- **owner:** `Codex conductor`
- **statement:** The exact stopped parity--Fejer chain reduces (165.K26)
  to adjacent links plus one target-safe short correction; the first link
  and the fully recombined ordinary-zero transformed sector are
  \(O_\varepsilon(L^3X^\varepsilon)\). The remaining signed nonzero-mode
  aggregate is open. Any continuation that, before proving a literal
  actual-symbol saving, replaces it by a coefficient-uniform positive norm
  over dual modes, cardinal cells, openings, or common frequency restores
  sharp capacity \(MD_L\asymp L^4X^\varepsilon\). The sharp dechirped
  controls are adversarial only and do not disprove (165.K26). The
  obstruction is residual-only and implies no parent or exponent result.

Do not create separate first-link or zero-mode owner nodes. Retain
(165.K26), the complete residual scalar, the other \(t=1\) channels, hard
TOP, BAL, UNBAL, M9--M2, M9, both bridges, and the quarter target in their
current statuses. The internally proved exponent remains \(1/3\), the
accepted external Li--Yang benchmark remains
\(0.3144831759740614\ldots\), and the target remains \(1/4\).
