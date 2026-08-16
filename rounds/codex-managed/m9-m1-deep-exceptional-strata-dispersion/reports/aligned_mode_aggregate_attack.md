# Round 87 analytic report: aligned-mode aggregate attack

Campaign: `m9-m1-deep-exceptional-strata-dispersion`
Task: `aligned_mode_aggregate_attack`
Role: analytic discovery
Starting graph SHA-256:
`909b828c22ae9db75aabae375794d288259429d742c2b5f5fffcb0a97b84e167`

## 1. Result

The normalization audit changes the proposed conclusion.  The physical
row bounded by \(TQ^{-5/24}\) is the **normalized** row

\[
 \mathcal R_{b,x}(\theta)
 ={1\over M}\sum_n I_b(n)e_M(nx)e(n\theta),
 \tag{1.1}
\]

so an ordered-pair function is
\(e_M(K(\bar x-\bar y))\mathcal R_{b,x}\overline{\mathcal R_{b,y}}\),
with no additional \(M^{-2}\).  Consequently the initially suggested
\(U\asymp B\) estimate \(UT^4Q^{-5/6}/B\) is false by a factor \(M^4\).
The correct physical-row estimate for the full-prime-power exceptional
aggregate is

\[
 \boxed{\mathcal P_{\rm exc}(D,U)
 \ll_\varepsilon X^\varepsilon
 U B^3T^4Q^{-5/6}.}
 \tag{1.2}
\]

There is nevertheless a target-safe choice allowed by (87.7): take
\(U=\lfloor D\rfloor\asymp D\), not \(U\asymp B\).  Uniformly for every
deep dyadic interval,

\[
 \mathcal P_{\rm exc}(D,D)
 \ll_\varepsilon X^\varepsilon D B^3T^4Q^{-5/6}
 \ll X^\varepsilon {D\over B}J^{14/5}.
 \tag{1.3}
\]

Indeed,

\[
 B^4T^4Q^{-5/6}
 \le J^{3/5+31/15}=J^{8/3}
 =J^{14/5-2/15}.
 \tag{1.4}
\]

This proves, with power slack \(J^{-2/15}\), a signed symmetric Fejer
estimate for every CRT mixture in which at each **full prime-power
factor** the two physical ordered pairs are either both locally diagonal
or locally identical.  It includes the \(u=0\) diagonal and all
stride-\(M\) self-returns.  No cancellation in \(b\) is used.

The exact survivor is the cross-correlation between different
physical-pair groups, formula (2.13) below.  At some full prime-power
factor every such cross term fails both of the preceding alternatives.
It contains partial-depth lower-conductor returns, bad-prime pieces,
additional 2-adic coincidences, and genuinely aperiodic local traces.
No estimate for that survivor, (87.2), or the absolute-per-shift
quantity (87.7) is claimed.

For comparison, at \(D\asymp Q^2\), \(U\asymp B\), the corrected left
side supplied by (1.2) is

\[
 B^4T^4Q^{-5/6}=B^4J^{31/15},
 \tag{1.5}
\]

whereas (87.8) is only \(\asymp BJ^2\).  Their ratio is
\(B^3J^{1/15}\ge J^{13/30}\), because \(B\ge J^{11/90}\).  Thus there is
no target-safe \(U\le M\asymp B\) conclusion from the uniform row bound;
the large-\(U\) choice in (1.3) is essential.

## 2. Exact statement and hypotheses

Assume precisely the frozen scales, three class normalizations, support
ownership, and stationary interfaces in the Round-87 packet:

\[
 J=X^{1/2},\quad Q=J^{2/5},\quad T=J^{3/5},\quad
 B=C/T,\quad J^{11/90}<B\le J^{3/20},
 \tag{2.1}
\]

and

\[
 (g,M,K)\in\{(1,4b,k),(2,2b,2[k\bar4]_b),
 (4,b,[k\bar4]_b)\},\qquad gM=4b,\quad M\asymp B.
 \tag{2.2}
\]

Fix one compatible smooth nonaxial principal component, sign, alias,
and reflected orientation.  Let \(\mathcal R_{b,x}\) be (1.1), so the
accepted estimate is

\[
 \sup_{x,\theta}|\mathcal R_{b,x}(\theta)|
 \ll_\varepsilon X^\varepsilon L,
 \qquad L:=TQ^{-5/24}.
 \tag{2.3}
\]

For an ordered pair \(P=(x,y)\) of distinct units modulo \(M\), define

\[
 F_{b,P}(\theta)
 =e_M\!\left(K(\bar x-\bar y)\right)
 \mathcal R_{b,x}(\theta)\overline{\mathcal R_{b,y}(\theta)}.
 \tag{2.4}
\]

Let \(\Pi_{b,D}\) be the Fourier projection onto one exact dyadic piece
of \(D_1<|d|<\Delta_b-E_*\), after extension by zero at the stationary
support endpoints.  Both reflected signs may instead be taken together.
In either convention it is a union of \(O(1)\) integer intervals and

\[
 \|\Pi_{b,D}f\|_\infty
 \ll \log(2+J)\|f\|_\infty.
 \tag{2.5}
\]

Factor \(M=\prod_{q\in\mathcal Q(M)}q\) into its exact full prime-power
factors \(q=p^{\nu_p}\).  Every global ordered pair \(P=(x,y)\) has the
unique nonempty active set

\[
 S(P)=\{q:x_q\ne y_q\pmod q\}.
 \tag{2.6}
\]

For \(\emptyset\ne S\subseteq\mathcal Q(M)\), put
\(m_S=\prod_{q\in S}q\) and \(r_S=M/m_S\).  An active label \(\alpha\)
specifies the distinct local ordered pair \((x_q,y_q)\) for every
\(q\in S\); an inactive label \(z\) specifies the common unit
\(x_q=y_q=z_q\) for every \(q\notin S\).  CRT gives a unique global pair
\(P(\alpha,z)\).  Set

\[
 H_{b,S,\alpha}(\theta)
 =\Pi_{b,D}\sum_zF_{b,P(\alpha,z)}(\theta).
 \tag{2.7}
\]

For \(D_U(\theta)=\sum_{j=0}^{U-1}e(j\theta)\), define the exceptional
aggregate

\[
 \mathcal P_{\rm exc}(D,U)
 =\sum_{b\asymp B}\int_{\mathbb T}|D_U(\theta)|^2
 \sum_{\emptyset\ne S\subseteq\mathcal Q(M)}
 \sum_\alpha |H_{b,S,\alpha}(\theta)|^2\,d\theta.
 \tag{2.8}
\]

If \(h_{b,S,\alpha}(d)\) denotes the \(d\)-th Fourier coefficient of
\(H_{b,S,\alpha}\), then (2.8) is exactly

\[
 \sum_{b,S,\alpha}\sum_{|u|<U}(U-|u|)
 \sum_d h_{b,S,\alpha}(d+u)
 \overline{h_{b,S,\alpha}(d)}.
 \tag{2.9}
\]

It is the one-count union of the two full-factor branches

\[
 h_1=h_2=0\pmod q,
 \qquad\text{or}\qquad
 v=0,\ h_1=h_2\pmod q,
 \tag{2.10}
\]

at every \(q\Vert M\).  Intersections are assigned to the first branch
when the common local ordered pair is diagonal.

The full projected row is

\[
 G_{b,D}=\Pi_{b,D}\sum_{x\ne y}^{*}F_{b,(x,y)}
 =\sum_{S,\alpha}H_{b,S,\alpha}.
 \tag{2.11}
\]

Thus its complete signed Fejer energy decomposes exactly as

\[
 \sum_b\int|D_U|^2|G_{b,D}|^2
 =\mathcal P_{\rm exc}(D,U)+\mathcal G_{\rm res}(D,U),
 \tag{2.12}
\]

where the strictly smaller survivor is

\[
 \boxed{
 \mathcal G_{\rm res}(D,U)
 =\sum_b\int|D_U|^2
 \sum_{(S,\alpha)\ne(S',\alpha')}
 H_{b,S,\alpha}\overline{H_{b,S',\alpha'}}.}
 \tag{2.13}
\]

The theorem is (1.2), and hence (1.3), for (2.8).  No bound is asserted
for (2.13).

## 3. Proof or derivation

**Normalization and the actual centered coefficient.**  Opening the
Kloosterman product gives

\[
 S(n+d,K;M)\overline{S(n,K;M)}
 =\sum_{x,y}^{*}e_M\!\left(n(x-y)+dx+K(\bar x-\bar y)\right).
 \tag{3.1}
\]

The terms \(x=y\) are exactly \(c_M(d)\).  Consequently

\[
 A_{M,K,d}(n)
 =\sum_{x\ne y}^{*}e_M\!\left(n(x-y)+dx+K(\bar x-\bar y)\right).
 \tag{3.2}
\]

Using the normalized row (1.1), a direct coefficient calculation gives

\[
 \widehat F_{b,(x,y)}(d)
 ={e_M(dx+K(\bar x-\bar y))\over M^2}
 \sum_n I_b(n+d)\overline{I_b(n)}e_M(n(x-y)),
 \tag{3.3}
\]

and therefore

\[
 Z_b(d)=\sum_{x\ne y}^{*}\widehat F_{b,(x,y)}(d).
 \tag{3.4}
\]

Equation (3.3) is the exact normalization check: the external \(M^{-2}\)
in \(Z_b\) is already supplied by the two normalized rows.  It must not
be inserted again in (2.4).  In a shifted correlation, the two copies of
(3.3) supply exactly \(M^{-4}\), as in (86.9).

The restriction \(x\ne y\) is algebraically the centered factor
\(S\overline S-c_M\).  Hence the product of two restrictions in (3.4)
contains the four-Kloosterman main, both Ramanujan cross terms, and the
Ramanujan square, with their actual signs and exactly once.  None is
dropped by the physical-pair notation.

**One-count CRT identity.**  Consider two physical ordered pairs
\(P=(x,y)\) and \(P'=(x',y')\).  At a full factor \(q\Vert M\), the first
branch in (2.10) says that \(P\) and \(P'\) are each internally diagonal;
the second says \(P=P'\) locally.  If both alternatives hold, assign the
factor to the first branch.  It follows that the complete choice of
local branches holds precisely when

\[
 S(P)=S(P')=S,\qquad \alpha(P)=\alpha(P')=\alpha.
 \tag{3.5}
\]

The inactive diagonal units \(z,z'\) remain independent.  Their exact
contribution is

\[
 \sum_{\alpha,z,z'}
 \Pi F_{P(\alpha,z)}\overline{\Pi F_{P(\alpha,z')}}
 =\sum_\alpha\left|\Pi\sum_zF_{P(\alpha,z)}\right|^2.
 \tag{3.6}
\]

This proves (2.8)--(2.13) and counts every intersection once.  It is CRT
algebra on actual unit pairs, so it is valid for arbitrary prime powers,
for the complete 2-part, and whether or not \(p\mid K\).  If two groups
differ, then at some full factor neither alternative in (2.10) holds;
this proves the asserted strict reduction in (2.13).

**The actual fourfold symbol.**  Expanding (3.3) in one shifted
correlation gives the exact weight

\[
 I_b(n+d+u)\overline{I_b(n)}
 \overline{I_b(m+d)}I_b(m)=\Omega_{b,d,u}(n,m),
 \tag{3.7}
\]

with phase

\[
 -\eta\lambda_b\bigl(\sqrt{|n+d+u|}-\sqrt{|n|}
 -\sqrt{|m+d|}+\sqrt{|m|}\bigr).
 \tag{3.8}
\]

Thus (3.6) is an identity before absolute values with the actual
stationary symbol, not a coefficientwise trace majorant.

**Prime-power check.**  For \(q=p^\nu\), put

\[
 \mathcal F_q(u;t)=
 \sum_{\substack{x\bmod q\\p\nmid x(x-t)}}e_q(ux).
 \tag{3.9}
\]

Exact residue-class summation gives, for every prime including \(2\),

\[
 \mathcal F_q(u;t)=
 \begin{cases}
 q1_{q\mid u}-{q\over p}1_{q/p\mid u},&p\mid t,\\
 q1_{q\mid u}-{q\over p}1_{q/p\mid u}(1+e_q(ut)),&p\nmid t.
 \end{cases}
 \tag{3.10}
\]

Therefore the two complete local branches satisfy

\[
 \mathfrak T_q(u,0;h,h)=q\mathcal F_q(u;h),\qquad
 \mathfrak T_q(u,v;0,0)=q\mathcal F_q(u;v),
 \tag{3.11}
\]

and \(|\mathfrak T_q|\le2q(u,q)\).  In particular, with the corrected
hypothesis \(\nu\ge2\), (3.10) gives

\[
 \mathfrak T_{p^\nu}(p^{\nu-1}\alpha,0;
 p^{\nu-1},p^{\nu-1})=-p^{2\nu-1}
 \quad(p\nmid\alpha),
 \tag{3.12}
\]

and CRT gives (87.14).  For \(p=2\) and odd \(t\), the local unit-pair
set in (3.9) is empty, exactly as (3.10) says.  Moreover

\[
 \sum_{1\le u<U}(U-u)(u,q)
 \le U^2\tau(q),
 \tag{3.13}
\]

which verifies the anticipated size-density compensation.  It does not
repair the missing global \(M^4\) in the false \(U\asymp B\) normalization.

**Sharp projection and the corrected aggregate bound.**  The Dirichlet
kernel for an integer interval has \(L^1(\mathbb T)\)-norm \(O(\log J)\).
There are only \(O(1)\) intervals in the exact signed deep projection,
so (2.5) follows and its square is absorbed into \(X^\varepsilon\).
From (2.3)--(2.4),

\[
 \|\Pi_{b,D}F_{b,P}\|_\infty
 \ll_\varepsilon X^\varepsilon L^2.
 \tag{3.14}
\]

For fixed \(S\), there are at most \(m_S^2\) active labels and at most
\(r_S\) inactive units.  Hence

\[
 \sum_\alpha|H_{b,S,\alpha}(\theta)|^2
 \ll_\varepsilon X^\varepsilon m_S^2r_S^2L^4
 =X^\varepsilon M^2T^4Q^{-5/6}.
 \tag{3.15}
\]

There are at most \(2^{\omega(M)}\ll_\varepsilon M^\varepsilon\) sets
\(S\), and

\[
 \int_{\mathbb T}|D_U(\theta)|^2d\theta=U.
 \tag{3.16}
\]

Thus one \(b\) contributes at most
\(X^\varepsilon UM^2T^4Q^{-5/6}\).  Summing \(O(B)\) conductors with
\(M\asymp B\) proves (1.2).

The \(u=0\) exceptional diagonal obeys the same bound (use Parseval and
(3.14), then multiply by \(U\)).  Therefore the symmetric signed
off-diagonal part, which is (2.8) minus this diagonal, is bounded by
twice the right side of (1.2).  This is the outside-absolute signed
interface explicitly permitted after (87.8); it is not a bound for the
absolute value of every individual shifted correlation.

Finally choose \(U=\lfloor D\rfloor\asymp D\).  Since \(D+U\asymp D\),
the right side required by (87.8) is

\[
 {U^2\over B(D+U)}J^{14/5}\asymp {D\over B}J^{14/5}.
 \tag{3.17}
\]

Dividing (1.2) by (3.17) gives

\[
 B^4T^4Q^{-5/6}J^{-14/5}
 \le J^{-2/15},
 \tag{3.18}
\]

which proves (1.3) uniformly throughout the frozen conductor range.
Here \(D\ge D_1\gg M\), so all shifts \(u=jM\) are present.  They form
the positive stride-\(M\) Fejer norm already contained in (2.8), and
(3.14)--(3.18) bound it without deleting it or asserting cancellation.

**Exact residual conductor stratification.**  Formula (2.13) is already
an exact residual.  It can be partitioned further without conjectural
pole algebra.  For a local summand \(w_q(x)\) in (87.10), including its
unit-domain indicator and reciprocal phase, its additive period group
is a unique subgroup

\[
 \operatorname{Per}(w_q)=p^{\nu-j_q}\mathbb Z/p^\nu\mathbb Z
 \quad(0\le j_q\le\nu).
 \tag{3.19}
\]

Fourier orthogonality on its period orbits says exactly that the local
transform vanishes unless \(p^{j_q}\mid u\); if this holds, it is
\(p^{j_q}\) times the Fourier transform of the descended function on
the quotient of size \(p^{\nu-j_q}\).  Thus \(0<j_q<\nu\) is an exact
lower-conductor self-return, while \(j_q=0\) is the aperiodic local
piece.  Bad primes, extra 2-adic periods, and accidental domain periods
are classified by the same definition.  All of them remain in (2.13),
and no estimate is attached to this partition.

## 4. First doubtful or unproved step

The first unproved step is a target-sized estimate for the exact
cross-group survivor (2.13).  At an odd good prime, a group mismatch
usually leaves an uncancelled reciprocal pole and suggests a
square-root trace, but this does not supply a theorem uniform over
prime powers, bad primes, the 2-part, or the coupled
\((b,d,u,n,m)\)-symbol (3.7).  Partial period depth in (3.19) returns a
smaller complete transform and sparse shifts, but no permitted theorem
sums those returned transforms.

There is unused endpoint variation

\[
 {D_1\over QB}=J^{1/14}=B^{10/21}
 \quad(C=J^{3/4}),
 \tag{4.1}
\]

but it is not a lawful \(b\)-saving.  The \(n\)- and \(m\)-derivatives in
(3.8) can cancel, while \(M,K\), the CRT groups, and the supports move
with \(b\).  No sampled-\(b\) bounded-variation or large-sieve theorem
for (2.13) is available.  The proof of (1.3) deliberately uses no such
cancellation.

The large-\(U\) conclusion is also sharply scoped.  It proves only the
positive same-group aggregate and its symmetric signed off-diagonal.
It does not turn the stride-\(M\) self-return into a saving for
(2.13), nor does it control the per-\(u\) absolute values in (87.7).

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| `external_normalization` | **Corrected pass.** Equations (1.1), (2.4), and (3.3) show where \(M^{-2}\) occurs.  The former \(UT^4Q^{-5/6}/B\) claim is rejected; the correct result is \(UB^3T^4Q^{-5/6}\).  For \(D\asymp Q^2,U\asymp B\) it misses (87.8) by at least \(J^{13/30}\); for \(U=D\) it wins by \(J^{-2/15}\). |
| `all_class_local_units` | **Pass.** All three triples (2.2), \(gM=4b\), and their exact unit groups are retained; no even class is inferred from an odd one. |
| `physical_row_energy_factor` | **Pass.** Each normalized row contributes \(Q^{-5/24}\); (3.14) has \(Q^{-5/12}\), and the four-row aggregate (3.15) has \(Q^{-5/6}\). |
| `deep_difference_ownership` | **Pass.** \(\Pi_{b,D}\) acts only on \(D_1<\lvert d\rvert<\Delta_b-E_*\); earlier shells and the outer collar are not reintroduced. |
| `negative_and_modulus_multiple_differences` | **Pass.** Both signed deep intervals and every integer difference, including nonzero multiples of \(M\), remain in the projection. |
| `ramanujan_cross_and_square_terms` | **Pass.** Equations (3.1)--(3.4) identify \(x\ne y\) with the exact centered coefficient, so its product contains the main, two cross terms, and square once. |
| `prime_power_and_2adic_strata` | **Scoped pass.** The one-count full-factor grouping and (3.10) are valid at every \(p^\nu\), including \(2^\nu\); (3.12) states \(\nu\ge2\). Partial-depth, bad-prime, and additional 2-adic periods remain in (2.13). |
| `squarefree_divisor_aligned_modes` | **Pass.** CRT grouping contains (87.14) exactly; no squarefree trace estimate is assumed. |
| `fejer_prefactor_and_diagonal` | **Pass.** Equations (2.9) and (3.16) retain \(U-\lvert u\rvert\), the unnormalized Fejer kernel, and \(u=0\).  The theorem uses the packet-allowed \(U=D\). |
| `actual_fourfold_stationary_symbol` | **Pass.** Equations (3.7)--(3.8) occur before an inequality.  Absolute values enter only after same-group exceptional terms have become squares. |
| `generic_trace_remainder` | **Pass as an exact reduction only.** It is (2.13), further partitioned exactly by (3.19); no trace or aggregate estimate is claimed. |
| `entry_exit_and_error_ownership` | **Pass.** Only the frozen smooth principal row is used.  Entry/exit, stationary errors, wrong signs, tails, transitions, and axes stay with their existing owners. |
| `integer_and_perfect_power_resonance` | **Pass.** The phase-free bound (3.14)--(3.18) is unaffected by integer derivatives or perfect-power specializations. |
| `complete_transform_self_return` | **Pass.** Since \(U=D\gg M\), stride-\(M\) returns are included in the positive norm; partial local returns are retained in (3.19), not declared generic. |
| `downstream_scope` | **Pass.** No claim is made for (2.13), (87.2), (87.7) with its per-shift absolute values, a \(b\)-gain, transitions, axes, cone edges, another sector, full `M9-M1`, `M9-M2`, `M9`, uniformity, `R5-Full`, or the Gauss-circle exponent. |

No external theorem or numerical experiment is used.

## 6. Dependencies and exact artifacts used

Only the selected context was used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/conductor_0816_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/synthesis.md`;
- `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reports/twisted_ambiguity_attack.md`;
- `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reviews/conductor_round86_cubic_shell_normalization.md`;
- `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reviews/conductor_round86_rational_completion.md`.

No sibling Round-87 report, web source, or external theorem was read or
used.  The new ingredients are elementary CRT, exact unit-pair
expansion, finite Fourier orthogonality, and the Fejer identity.

## 7. Recommended state effect

**Promote after independent normalization and seam review** only the
scoped statement (1.2)--(1.4): with \(U=D\gg M\), the complete
full-prime-power local-zero/paired same-group aggregate is target-safe
as an outside-absolute symmetric Fejer estimate against the actual
fourfold stationary symbol.  Its exact formula (2.8), corrected
normalized row (1.1), and explicit inclusion of stride-\(M\) returns
must be part of any promoted statement.

**Retain as the exact next survivor** the cross-group correlation
(2.13), with the exact period-depth partition (3.19).  It is strictly
smaller than the input because every globally full-factor mixture of
the local-zero/paired branches has been removed.  Partial lower
conductors, bad-prime and additional 2-adic periods, and aperiodic local
traces remain.

**Reject** the earlier \(U\asymp B\) estimate
\(UT^4Q^{-5/6}/B\), any conclusion based on that normalization, and any
claim that size-density alone closes the endpoint with \(U\le M\).
Also do not promote (87.2), the per-shift absolute estimate (87.7), a
heuristic \(b\)-saving from (4.1), or a bound for (2.13).
