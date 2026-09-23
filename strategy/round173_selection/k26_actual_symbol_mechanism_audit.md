# Round 173 selection audit: actual-symbol mechanisms for K26

- Authoritative graph:
  70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f
- Role: bounded post-Round-172 selection audit
- Scope: the exact signed nonzero ordinary-frequency aggregate (172.K20)
  underlying the maximal residual Fejer theorem (165.K26)
- State effect: none

## 1. Result

**Recommendation: defer K26 in Round 173.**

**Literal-operator ruling:** the exact row projection (173.A6), the
disjoint-cardinal transform, and the stopped-chain sum are literal
operators, but none has a proved power-reducing action. There is no
accepted literal operator which preserves every selector, hole, parity
branch, endpoint cell, and transition while mapping (172.K20) to a
target-safe positive norm. The audited row projection self-returns through
large-toggle boundary leakage, and the scale operator self-returns through
(173.A16).

The concrete actual-symbol mechanism tested here is the strongest exact
one suggested by the accepted residual algebra:

1. project every zero-total-character fibre by subtracting a row constant;
2. use the selected/no-pair sign-mass dichotomy to isolate the only
   positive-mass no-pair rows;
3. retain squarefree and coprimality holes, both two-adic branches, and all
   cardinal endpoint cells; and
4. sum the entire parity--Fejer stopped chain before taking a positive norm.

Every identity in this proposal is valid, but the mechanism supplies no
factor \(L\). On a selected residual row, the sign-reversing partner is
obtained by multiplying the divisor by \(p_Nq_N\ge 15\), so the two literal
near-square supports are disjoint. On a balanced no-pair row, a
\(3\pmod 4\) prime toggle multiplies the divisor by at least \(3\), and the
supports are again disjoint. Thus fibre balance cancels only a constant
ambient profile; for the literal compact profile it returns the whole
coefficient as zero-extension and hard-face leakage. The remaining no-pair
rows with all odd primes \(1\pmod4\) have wholly positive character mass
and cannot be discarded as a power-sparse exception from any accepted
estimate.

Moreover, K26 contains only even shifts. On every accepted cofactor-gcd
row its character product is constant, in both the odd--odd and the
squarefree even--even branches. Squarefree and coprimality conditions are
unsigned deletion masks. The stopped-chain physical weights are all
nonnegative and telescope to the original K26 weight; they are not an
alternating or orthogonal scale decomposition. Disjoint cardinal cells
preserve, rather than cancel, the singleton, endpoint, transition, and
zero-extension contributions.

Consequently the proposed mechanism does not genuinely bypass the
Round-172 coefficient-uniform positive obstruction. Resuming K26 would
require a new quantitative signed shifted-convolution or selector-stable
spectral theorem for the complete literal two-product family. Merely
requiring that theorem restates (172.K20)/(165.K26) and is not a frozen new
mechanism.

This is a selection no-go for the audited fibre-projection, exceptional-row,
parity, cell, and stopped-chain route. It is not a disproof of K26.

## 2. Exact proposed interface and hypotheses

Retain the accepted literal residual coefficient

\[
 c_N^{\rm rem}=\omega_L(N)
 \sum_{d\mid M_N}\chi_4(d)\rho_N(d)A_N(d),
 \qquad N=2^{\nu_N}M_N,\quad \nu_N\in\{0,1\},
\tag{173.A1}
\]

where \(M_N\) is odd, \(N\) is squarefree on support, and every shell,
normalization, selector, profile, floor, star, crossing, endpoint value,
and zero-extension value is literal. If the canonical pair
\(p_N,q_N\) is selected, then

\[
 \rho_N(d)=1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
             +2\mathbf1_{p_N\mid d}\mathbf1_{q_N\mid d};
\tag{173.A2}
\]

if no pair is selected, \(\rho_N(d)=1\). Define the exact fibre mass

\[
 \Sigma_N=\sum_{d\mid M_N}\chi_4(d)\rho_N(d).
\tag{173.A3}
\]

The accepted dichotomy is

\[
 \Sigma_N=
 \begin{cases}
  0,&\text{a pair is selected},\\
  \prod_{p\mid M_N}(1+\chi_4(p)),&\text{no pair is selected}.
 \end{cases}
\tag{173.A4}
\]

Hence split the rows exactly into

\[
 \mathcal Z=\{N:\Sigma_N=0\},\qquad
 \mathcal P=\{N:\text{no pair is selected and every odd }p\mid N
                         \text{ has }p\equiv1\pmod4\}.
\tag{173.A5}
\]

For \(N\in\mathcal Z\), any row constant \(\alpha_N\) gives the exact
projection

\[
 b_N^{\rm rem}
 =\sum_{d\mid M_N}\chi_4(d)\rho_N(d)
     \{A_N(d)-\alpha_N\}.
\tag{173.A6}
\]

The proposed mechanism was to use (173.A6) for the \(\mathcal Z\) rows,
bound the \(\mathcal P\) rows by a strictly smaller positive energy, and
then retain all four \(\mathcal Z/\mathcal P\) cross-correlations inside the
one outer real part. A purely positive treatment of the exceptional part
would need, at minimum,

\[
 D_{\mathcal P}:=\sum_{N\in\mathcal P}|c_N^{\rm rem}|^2
 \ll_\varepsilon L X^\varepsilon,
\tag{173.A7}
\]

because the maximal Fejer capacity is \(M D_{\mathcal P}\) and
\(M\asymp L^2\). The accepted estimate is only
\(D_{\mathcal P}\le D_L\ll_\varepsilon L^2X^\varepsilon\).

For the scale component, let \(w_R(r)=(1-r/R)_+\) and
\(b_j(r)=w_{R_{j+1}}(r)-w_{R_j}(r)\), where
\(R_{j+1}=\min(2R_j,M)\). The proposed full-chain estimate would keep

\[
 \sum_j\mathcal N_{R_j,R_{j+1}}
\tag{173.A8}
\]

signed until every character frequency, ordinary nonzero frequency,
cardinal cell, endpoint, transition, and zero-extension piece has been
recombined. No linkwise modulus is part of the proposal.

## 3. Derivation and evidence for the no-go

### 3.1 Selected rows: zero mass is entirely nonlocal leakage

If \(p_N,q_N\) are selected, write \(M_N=p_Nq_NR_N\). The residual
divisors are \(a\) and \(p_Nq_Na\), \(a\mid R_N\), with opposite signs.
Thus exactly

\[
 b_N^{\rm rem}
 =\sum_{a\mid R_N}\chi_4(a)
   \{A_N(a)-A_N(p_Nq_Na)\}.
\tag{173.A9}
\]

The literal physical divisor support is
\(\sqrt N\le d\le2\sqrt N\). Since \(p_Nq_N\ge15\), the two terms in
each brace of (173.A9) cannot be simultaneously supported. The constant
projection (173.A6) therefore does not produce a small close difference;
it transports every active value through a hard exit into the zero
extension. Its cost is unit-size profile leakage, not
\(O(L^{-1/2})\) close-prime variation. The close exchange with ratio
\(q_N/p_N=1+O(L^{-1/2})\) belonged to the already removed XOR sector and
is absent from the residual neither/both sector.

### 3.2 Balanced no-pair rows: a one-prime toggle has the same defect

If no pair is selected but \(p\equiv3\pmod4\) divides \(M_N\), then
\(\Sigma_N=0\), and exact reindexing gives a one-prime form

\[
 b_N^{\rm rem}
 =\sum_{d\mid M_N/p}\chi_4(d)
   \{A_N(d)-A_N(pd)\}.
\tag{173.A10}
\]

Again \(p\ge3\). If \(A_N(d)\ne0\), then \(pd>2\sqrt N\); if
\(A_N(pd)\ne0\), then \(d<\sqrt N\). Hence (173.A10) is also all
leakage. Averaging several such toggles returns the original coefficient
and gives no additional cancellation.

### 3.3 Positive no-pair rows are not a target-safe exceptional class

For \(N\in\mathcal P\), every \(\chi_4(d)=1\), and

\[
 \Sigma_N=2^{\omega(M_N)}.
\tag{173.A11}
\]

There is no fibre projection. The accepted coefficient sources provide no
power-saving count or energy estimate such as (173.A7). Existing fixed-box
unit-profile controls have \(L^{2-o(1)}\) coefficient-uniform capacity, so
the all-\(1\pmod4\) class is not structurally reduced from \(L^2\) to
\(L\) by a row classification. Those controls are not a literal lower
bound, but they rigorously rule out deriving (173.A7) from sign mass,
squarefreeness, bounded variation, or support geometry alone.

The decomposition (173.A5) also does not license positive estimates of
the four \(\mathcal Z/\mathcal P\) correlation blocks. Cauchy on those
blocks returns the \(M D_L\asymp L^4\) capacity. Any useful cancellation
would have to remain joint across the row classes, so isolating
\(\mathcal P\) has not simplified the open signed object.

### 3.4 Squarefree and coprimality holes carry no automatic sign

The conditions \(\mu^2(N)=1\) and \((d,N/d)=1\) delete incidences; they do
not alternate them. Opening them with Mobius sums creates signed auxiliary
variables, but a positive sum over those openings is prohibited by the
Round-172 obstruction, while exact recombination returns the same literal
coefficient. A gain from those signs would therefore require a new uniform
shifted-convolution theorem, including the canonical selector
\(\rho_N(d)\); it is not an algebraic consequence of the holes.

### 3.5 Both parity branches freeze the character on the relevant rows

Open a correlation at even shift \(r\) as \(N=dm\),
\(N+r=d'm'\), with \(d,d'\) odd. Then

\[
 a=d'-d\equiv0\pmod2,\qquad
 b=m'-m\equiv0\pmod2,\qquad
 \chi_4(d')\chi_4(d)=(-1)^{a/2}.
\tag{173.A12}
\]

In cofactor-gcd coordinates \(s=(m,m')\), \(m=su\), \(m'=sv\),
\((u,v)=1\), all solutions have

\[
 d=D_0+2vk,\qquad d'=D'_0+2uk,
\tag{173.A13}
\]

and the exact character law is

\[
 \chi_4(d(k))\chi_4(d'(k))
 =\sigma_0(-1)^{(r\bmod2)k}=\sigma_0.
\tag{173.A14}
\]

This covers the odd--odd branch. On the squarefree even--even branch,
\(\nu_2(s)=1\), \(u,v\) are odd, \(4\mid r\), and (173.A14) remains
constant. Thus the tempting tangent alternation in (173.A12) supplies no
oscillation along the actual one-dimensional Diophantine rows. Across
different rows it is precisely the character sum already retained in the
Round-172 transform; no new orthogonality follows.

### 3.6 Endpoint cells preserve the obstruction

The real-cardinal interpolation has disjoint cells of width less than one
and reproduces every literal lattice value with multiplicity one. The
large toggles in (173.A9)--(173.A10) connect separated cells and cross the
literal support boundary. Smoothing those exits would change the
coefficient. Keeping them exact leaves hard boundary, point-value,
transition, and zero-extension cells inside the signed nonzero-frequency
aggregate (172.K20). A single active cell is allowed, so no cellwise
zero-mean or dual-diagonal deletion is valid. The ordinary-zero-containing
sector is already target-safe only after full character recombination; it
does not control these nonzero cells.

### 3.7 The stopped chain has no alternating scale cancellation

For every fixed \(r>0\), \(w_R(r)\) is nondecreasing in \(R\). Hence

\[
 b_j(r)=w_{R_{j+1}}(r)-w_{R_j}(r)\ge0
\tag{173.A15}
\]

and exactly

\[
 \sum_j b_j(r)=w_M(r)-w_{R_0}(r).
\tag{173.A16}
\]

After the one short correction is removed, (173.A16) is just the positive
K26 weight on \(r\ge R_0\). Thus summing links first is lawful and weaker
than a linkwise estimate, but it introduces neither an alternating scale
sign nor orthogonal projections. At a doubling,
\(\mathfrak E_{2R}^{(2)}-\mathfrak E_R^{(2)}
=\mathfrak E_R^{(2)}-\mathfrak H_R^{(2)}\); this is useful only after a
new actual-symbol lower bound for the Haar detail. No such lower bound
follows from (173.A3)--(173.A14).

The in-range \(M=4P\) dechirped one-parity control makes one maximal link
equal to \(MD_L/8\). It is nonliteral, so it is not a lower bound for
K26, but it rigorously falsifies any scale-only square-function or
martingale inference from (173.A15)--(173.A16).

## 4. First doubtful or unproved step

After the exact failures above, the first potentially useful statement is
a genuinely joint estimate for

\[
\begin{aligned}
 \Re\sum_{\substack{R_0\le r<M\\2\mid r}}
 \left(1-\frac rM\right)
 \sum_{\substack{d,m,d',m'\\d'm'-dm=r}}
 &\mu^2(dm)\mu^2(d'm')
 \omega_L(d'm')\overline{\omega_L(dm)}
 \chi_4(d)\chi_4(d')
 \rho_{dm}(d)\rho_{d'm'}(d')\\
 &\times A_{d'm'}(d')\overline{A_{dm}(d)}
 e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right),
\end{aligned}
\tag{173.A17}
\]

with every normalization, branch, cell, endpoint, and zero-extension
value restored and one outer real part. A two-variable Poisson, spectral,
or dispersion theorem could in principle estimate (173.A17), but the
accepted state contains no theorem whose hypotheses include the
allocation-independent canonical selector on both products and whose
restored power is \(L^3X^\varepsilon\).

Calling (173.A17) a signed actual-symbol theorem does not define a new
mechanism: it is the physical form of K26, while (172.K20) is its exact
nonzero-frequency transform. A future K26 campaign should be selected
only after supplying an additional falsifiable kernel, for example an
exact selector-stable transform with a displayed factor-\(L\) estimate
before every positive opening. The first doubtful step in any such
proposal is selector stability: \(\rho_N(d)\) changes discontinuously with
the prime factors of \(N\), and neither fibre balance nor Mobius opening
controls those changes.

## 5. False controls and outcomes

| Proposed shortcut or control | Outcome |
|---|---|
| Selected-row total character mass is zero | **Fails quantitatively.** The exact partner is \(d\mapsto p_Nq_Nd\), and the two physical supports are disjoint. |
| Balanced no-pair row cancels by a \(3\pmod4\) prime | **Fails quantitatively.** The toggle \(d\mapsto pd\) is all zero-extension leakage. |
| All-\(1\pmod4\) no-pair rows form a power-small exception | **Not available and not structurally implied.** The accepted energy is still \(L^2X^\varepsilon\), not the \(LX^\varepsilon\) needed for positive closure. |
| Squarefree/coprimality holes give cancellation | **False algebraically.** They are deletion masks; useful Mobius cancellation would be a new signed theorem. |
| Tangent character alternation saves the even-shift rows | **False on the actual rows.** Equation (173.A14) freezes the character in both parity branches. |
| The even--even branch supplies an extra two-adic sign | **False.** It forces \(4\mid r\) and leaves the same constant character law. |
| Endpoint or transition cells may be smoothed into the row projection | **False.** They are where the large-toggle leakage lives and must remain literal. |
| A fixed dual diagonal vanishes because the physical diagonal does | **False by Round 172.** Independent cardinal variables cancel only after the full dual/cell assembly. |
| Summing the stopped chain creates scale orthogonality | **False.** The physical link weights are nonnegative and satisfy (173.A16). |
| Coefficient-uniform positivity after the projection is harmless | **False.** The first such norm has sharp available capacity \(MD_L\asymp L^4\). |
| A one-site or one-cell coefficient forces a positive diagonal term | **False.** Its exact Fejer increments vanish; compensating dual and boundary terms are mandatory. |

No numerical experiment and no external theorem is used in this audit.

## 6. Dependencies and exact artifacts used

- protocol.md;
- state/proof_obligations.yml at the authoritative post-Round-172 hash;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/synthesis.md;
- rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/reviews/conductor_round172_adjudication.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md;
- proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md;
- proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md; and
- proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md.

The residual coefficient facts used are exactly the one-time XOR
subtraction, selected/no-pair sign-mass law, large-toggle leakage,
squarefree odd-divisor convention, both parity branches, literal profile
and zero-extension support, and even-shift cofactor-row character law. No
sibling Round-173 report, web source, or computation is used.

## 7. Recommendation: defer

Do not select K26 merely as “prove the signed nonzero-frequency aggregate”
in Round 173. Round 172 has already made that object exact, and the
accepted residual algebra supplies no additional actual-symbol gain that
survives selected and no-pair rows, squarefree/coprimality holes, both
parity branches, hard cells, endpoints, and full stopped-chain
recombination.

Defer K26 until one of the following exists:

1. a selector-stable signed transform of (173.A17) with an explicit
   factor \(L\) before all positive mode/cell/opening sums;
2. a proved coefficient-sensitive positive property stronger than
   \(D_L\ll L^2X^\varepsilon\), with all-\(1\pmod4\) no-pair rows included;
   or
3. a source-audited shifted-convolution or spectral theorem whose exact
   hypotheses accept (173.A17) and whose restored endpoint power is
   \(L^3X^\varepsilon\).

Until then, another frontier with a genuinely new finite mechanism should
be preferred for Round 173. K26, the complete residual \(t=1\) scalar,
hard TOP, M9--M2, M9, the bridge, the quarter theorem, and both exponent
ledgers remain unchanged.
