# Round 160 synthesis

- Campaign: `m9-m2-unbalanced-inverse-selector-reciprocity-gate`
- Starting graph: `4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d`
- Terminal label: `inverse_selector_projective_capacity_no_go`
- Graph mutation: applied
- Resulting graph: `7e68cfd355ef48407712d3216382a1a54a28be9a27ac9e15c3fd1e59e081a447`

## Outcome

Round 160 proves the exact additive-reciprocity presentation of the already
centered flat-smooth strict-UNBAL inverse-selector coefficient:

\[
 e(-h\overline j_n/n)
 =e(h\overline n_j/j-h/(jn)).
\tag{160.Y1}
\]

The proof covers arbitrary inverse representatives and even or odd (j).
It preserves the literal (1/(gnj)) normalization, both (chi_4)
directions, real centre, moving (j)-support, profiles, endpoints, and all
gcd strata. Complete (h\bmod n) summation reconstructs the original
reciprocal row exactly. Only the accepted target-safe (h=0\pmod n)
Ramanujan row is removed, once.

## Exact finite obstruction

For (A\subseteq U_j=(\mathbb Z/j\mathbb Z)^\times), (M=|A|), let

\[
 F_{j,A}(u,h)=e(h\overline u_j/j),
 \qquad u\in A,\quad 1\le h\le j-1.
\tag{160.Y2}
\]

Then

\[
 \boxed{F_{j,A}F_{j,A}^*=jI_M-\mathbf1\mathbf1^*.}
\tag{160.Y3}
\]

Hence

\[
 \|F_{j,A}\|_{S_1}=(M-1)\sqrt j+\sqrt{j-M},
 \qquad
 \|F_{j,A}\|_{S_2}^2=M(j-1).
\tag{160.Y4}
\]

For all unit classes, any exact Hilbert rank-one realization that feeds
scalar tests termwise and closes by triangle pays

\[
 \frac{\|F_j\|_{S_1}}{\|F_j\|_{S_2}}
 \asymp\sqrt{\varphi(j)}=j^{1/2-o(1)}.
\tag{160.Y5}
\]

The literal positive block (1\le h\le j), normalized by (j^{-1/2}),
has orthonormal rows. Thus the deleted (h=0\pmod n) row does not delete
the positive frequencies (h=j,2j,\ldots), which are zero only modulo
(j).

## Long frequencies and boundary power

Residue compression of the full physical range satisfies the sharp identity

\[
 \|P_{n,j}\|_{2\to2}
 =\sqrt{\left\lceil\frac{n-1}{j}\right\rceil}
 \asymp\sqrt\Delta.
\tag{160.Y6}
\]

The rows (h=mj<n) have inverse phase one and reciprocity correction
(1+O(1/j)). At the primitive stratum (g=1), (j\asymp K), the scalar
projective price is (K^{1/2-o(1)}). If (a=\delta-\ell), the missing
saving is

\[
 \mu(a)=
 \begin{cases}
 a-1/4,&1/4<a\le1/3,\\
 (1-2a)/4,&1/3\le a<1/2.
 \end{cases}
\tag{160.Y7}
\]

The exact comparisons are

\[
 \frac{1-\delta-a}{2}-\mu(a)
 =\begin{cases}
 (3-2\delta-6a)/4,&a\le1/3,\\
 (1-2\delta)/4,&a\ge1/3,
 \end{cases}
 \quad >0,
\tag{160.Y8}
\]

and (a/2-\mu(a)>0). Thus each omitted capacity exceeds the entire
missing factor at every fixed strict point. No margin uniform up to
(\delta=1/2) is claimed.

## Source and method frontier

The exact additive expansion into Kloosterman tests is a full-rank change
of basis and carries a fixed proportion of its joint mass at additive
frequencies of size (j). The audited Bettin--Chandee/Wright,
Blomer--Milićević, Deshouillers--Iwaniec, and Assing--Blomer--Li scalar
interfaces do not accept the complete moving (S(N_0,h;n))-weighted
matrix at an owner-saving norm. Mellin encoding has a large coefficient
cost and growing levels, while the sourced short Linnik band covers only
a proportion of the physical frequency row.

These are exact finite capacities and theorem-hypothesis mismatches. They
do not prove that the signed owner is large, do not provide a lower bound
for the literal weighted matrix, and do not exclude a bespoke vector-valued
theorem that retains the whole ((j,n,h)) interaction before positive norms.

## Proof status

The round closes one proposed continuation of the flat-smooth UNBAL route:
shorter-modulus reciprocity followed by canonical scalar common tests is not
a low-cost source of the missing power. The positive owner theorem remains
open. A future attack on this surface must prove a genuinely new signed
vector theorem for the literal matrix, including every long frequency,
moving boundary, gcd and two-adic stratum, and induced spectral level.

No strict M2 range is obtained. The three mandatory M2 parents remain the
hard-TOP density-discrepancy energy, balanced smooth quarter-packet estimate,
and unbalanced smooth three-quarter estimate. M1, endpoint uniformity, M9,
the conditional bridge, and the quarter theorem all remain open. The
internally proved exponent remains (1/3), and the separately audited
external Li--Yang exponent remains (0.3144831759740614\ldots).

## Reviews and requested state effect

The blind rederivation, post-blind seam, exact-kernel/power review,
source-level review, scope/hygiene review, conductor adjudication, and
terminal State Patch scope review support the narrow unweighted scalar-route
result. The validated State Patch creates one proved-internal obstruction,
updates four interfaces, rejects fifteen route-specific false inferences,
and records eleven explicit downstream no-change decisions. The resulting
graph is
`7e68cfd355ef48407712d3216382a1a54a28be9a27ac9e15c3fd1e59e081a447`.
