# Adjacent transport commutator attack

Campaign: m9-m2-adjacent-ray-transport-commutator
Task: adjacent_transport_commutator_attack
Role: discovery analyst
Starting graph SHA-256:
c93f14d6790341b792b54bbaa7ccb96c211741d666729f08addc80fb91d1b759

## 1. Result

**Phase-preserving transport and scaled-comb no-go lemma.** Let
\(b_q=a+2q\) and

\[
 \delta_q=\sqrt {b_q}-\sqrt a,\qquad
 \lambda_q=\left(\frac{\delta_q}{\delta_{q+1}}\right)^2.
\]

The continuous map

\[
 T_q(x,k)=(\lambda_qx,k/\lambda_q)
\tag{1.1}
\]

has determinant one and preserves both \(kx\) and the physical phase:

\[
 -J\sqrt g\,\delta_{q+1}\sqrt{\lambda_qx}
      +\frac{k}{\lambda_q}(\lambda_qx)
 =-J\sqrt g\,\delta_q\sqrt x+kx.
\tag{1.2}
\]

For the literal integer row, however, \(T_q\) does not preserve counting
measure. With the Fourier convention
\(\widehat H(\xi)=\int_{\mathbb R}H(y)e(-\xi y)\,dy\), the exact
one-dimensional comb commutator is

\[
 \boxed{
 \lambda_q\sum_{n\in\mathbb Z}H(\lambda_q n)
   -\sum_{n\in\mathbb Z}H(n)
 =\sum_{r\in\mathbb Z}
   \left\{\widehat H(r/\lambda_q)-\widehat H(r)\right\}.}
\tag{1.3}
\]

Thus the adjacent difference is exactly the sum of a phase-aligned
material/amplitude commutator, the scaled-comb term (1.3), and uniquely
owned arithmetic and support jumps. Section 3 gives the exact one-count
partition.

On a noncollapsed hard block,

\[
 a\asymp b_q\asymp A,\quad q\asymp D,\quad
 g\asymp G\asymp \frac{L}{A},\quad
 m\asymp L,\quad k\asymp K\asymp \frac{JD}{A},
\tag{1.4}
\]

one has \(1-\lambda_q\asymp D^{-1}\). Nevertheless the common stationary
part of (1.3) is not \(D^{-1}\) times a row. Its two exact centred carriers
differ by

\[
 \Delta\Theta_{q,g}(k)
 =\frac{Xg(\delta_{q+1}^2-\delta_q^2)}{4k}
 \asymp \frac{JL}{A}.
\tag{1.5}
\]

The unwrapped displacement in (1.5) is not perturbatively small, although
it can be integral or near integral. The full common band of
\(K\asymp JD/A\) modes remains, not only its \(J/A\)-wide symmetric
difference. Consequently continuous material transport can display a
formal \(D^{-1}\) factor while the literal lattice commutator retains the
same coefficient-blind capacity as the original fixed-\(q\) row.

The endpoint defects are also not fixed collars. The transported physical
support has lower and upper slabs of length \(\asymp L/D\), and the dual
stationary bands have endpoint slabs of length
\(\asymp J/A=K/D\). The Round-77 collars have fixed physical width,
whereas the transport slabs contain \(\asymp J/A\) stationary modes. The
available complete-integral majorant gives aggregate endpoint capacity

\[
 L^2\sqrt\kappa\,X^{O(\varepsilon)},\qquad
 \kappa=\frac{K}{L}=\frac{JD}{AL}\ge D,
\tag{1.6}
\]

so even these shorter slabs are not target-safe by absolute summation for
any \(D\to\infty\).

Hence the proposed transport proves neither the full
\(L^2X^\varepsilon\) target nor a strict polynomial hard subrange. It
gives an equal-capacity actual-symbol route obstruction. The first
surviving kernel is the signed common-band scaled-comb correlation

\[
 \sum_{a,q}(-1)^q
 \sum_{g\ {\rm common}}
 \sum_{k\in I_{q+1}\cap\lambda_q I_{q+1}}
 \left\{\widehat H_{a,q+1,g}(-k/\lambda_q)
              -\widehat H_{a,q+1,g}(-k)\right\},
\tag{1.7}
\]

with every actual profile, owner, collar, floor, star, entry/exit and
metric tag retained. Bounding (1.7), or its exact joint sum with the
endpoint slabs, is a new signed theorem equivalent in capacity to the
open hard direction; it is not supplied by the transport identity.

## 2. Exact statement and hypotheses

Put \(J=\sqrt X\), \(1\le L\le J^{1/2}\), and use one representative
orientation \(a<b_q<4a\), followed by one outer \(2\Re\). The literal
zero-extended row is

\[
\begin{aligned}
F_{L,a}(q)={}&1_{q\ge1}1_{(a,a+2q)=1}
 \sum_{\substack{g\ {\rm odd}\\ga,g(a+2q)\in\mathscr H_L}}
 \sum_{m=\lceil g(a+2q)/4\rceil}^{ga}
 a_{\rm end}(ga,m)\overline{a_{\rm end}(g(a+2q),m)}\\
&\hspace{25mm}\times
 e\!\left(-J\sqrt g\,\delta_q\sqrt m\right).
\end{aligned}
\tag{2.1}
\]

All inherited half-open cells, reciprocal intervals, equality atoms,
collars, floors, stars, prior-owner complements, entry/exit data, terminal
metric members and exact-centre conventions are part of the tagged
symbol; none is replaced by a scale-free coefficient. For odd \(a\),

\[
 (a,a+2q)=(a,q).
\tag{2.2}
\]

Write \(b=b_q\), \(\delta=\delta_q\),
\(\delta_+=\delta_{q+1}\), and

\[
 \rho_q=\frac{\delta_+-\delta}{\delta}
 =\frac{\sqrt b+\sqrt a}
 {q(\sqrt{b+2}+\sqrt b)}.
\tag{2.3}
\]

Then the exact dilation identities are

\[
 \lambda_q=(1+\rho_q)^{-2},\qquad
 \lambda_q^{-1}-1=2\rho_q+\rho_q^2,\qquad
 1-\lambda_q=\frac{2\rho_q+\rho_q^2}{(1+\rho_q)^2}.
\tag{2.4}
\]

Thus \(\rho_q\asymp D^{-1}\) and
\(1-\lambda_q\asymp D^{-1}\) on \(q\asymp D\), uniformly for
\(a\le b<4a\).

To state (1.3) without evaluating a discrete symbol informally at a
noninteger point, fix once and for all a tagged compact extension. Extend
every binary tag by its half-open unit-cell staircase, with a separate
midpoint equality atom, and interpolate each remaining finite scalar
sequence \(u(n)\) by

\[
 \mathcal Iu(y)=\sum_{n\in\mathbb Z}u(n)(1-|y-n|)_+.
\tag{2.5}
\]

For fixed \(a,q,g\), form the finite sum of these tagged extensions and
multiply its smooth core by
\(e(-J\sqrt g\,\delta_q\sqrt y)\). It agrees with (2.1) at every
integer and is compactly supported and piecewise \(C^1\), apart from
finitely many owned staircase jumps. Give every interpolation boundary
its symmetric value. Symmetric Poisson summation therefore applies
exactly, including the equality atoms. A different fixed extension moves
terms between the material and comb packets but leaves their sum exactly
unchanged. No estimate below is inferred from a favorable off-lattice
extension.

The continuous stationary endpoints for the \(q\)-row are

\[
 K_-(q)=\frac{J\delta_q}{2\sqrt a},\qquad
 K_+(q)=\frac{J\delta_q}{\sqrt{a+2q}},\qquad
 I_q=(K_-(q),K_+(q)).
\tag{2.6}
\]

The interval is open; integer equality modes retain their original
separate star or half-weight. Collapsing, empty and singleton fibres are
not excluded.

## 3. Proof or derivation

### 3.1 Parity high-pass and the literal transport

Finiteness and zero extension give, without endpoint error,

\[
 2\sum_q(-1)^qF_{L,a}(q)
 =\sum_q(-1)^q\{F_{L,a}(q)-F_{L,a}(q+1)\}.
\tag{3.1}
\]

This is a signed identity. It does not imply a total-variation bound.

For one common \(a,g\), let \(H_q\) be the cardinally extended literal
summand in (2.1), including its phase. Since
\(\delta_{q+1}\sqrt{\lambda_q}=\delta_q\),

\[
 H_{q+1}(\lambda_qx)
 =U_{q+1}(\lambda_qx)
  e(-J\sqrt g\,\delta_q\sqrt x),
\tag{3.2}
\]

so the phases in \(H_q(x)\) and \(H_{q+1}(\lambda_qx)\) agree exactly.
Insert and subtract the Jacobian-normalized transported sum:

\[
\begin{aligned}
 \sum_nH_q(n)-\sum_nH_{q+1}(n)
={}&\sum_n\{H_q(n)-\lambda_qH_{q+1}(\lambda_qn)\}\\
 &+\left\{\lambda_q\sum_nH_{q+1}(\lambda_qn)
              -\sum_nH_{q+1}(n)\right\}.
\end{aligned}
\tag{3.3}
\]

The first line is the phase-aligned material/amplitude commutator. For
\(f(x)=\lambda_qH_{q+1}(\lambda_qx)\),
\(\widehat f(r)=\widehat H_{q+1}(r/\lambda_q)\); Poisson summation proves
(1.3) exactly. The factor \(\lambda_q\) in (3.3) is the one-dimensional
Jacobian. In the formal continuous \((x,k)\)-plane, (1.1) has Jacobian
\(\lambda_q\lambda_q^{-1}=1\). The actual mixed measure
\(dx\otimes\#_{\mathbb Z}(k)\) is not invariant, which is precisely the
comb term in (1.3).

### 3.2 Exact common-interior and jump-atom partition

On the inherited tagged atom space, let
\(M_{j,q}(z)\in\{0,1\}\) be the literal binary masks, in the following
fixed priority order:

\[
\begin{array}{c|l}
j&\text{mask owned at the first failure}\\ \hline
1&q\ge1\text{ and zero-extension endpoint},\\
2&(a,q)=1\text{ (coprimality)},\\
3&g\text{ odd and }ga,gb_q\in\mathscr H_L\text{ (lift)},\\
4&m\ge\lceil gb_q/4\rceil,\ m\le ga\text{ (hard support/ceiling)},\\
5&k\in I_q\text{ with the exact open/equality convention},\\
6&\text{physical and reciprocal collar support},\\
7&\text{entry/exit, owner, half-open cell and floor support},\\
8&\text{terminal, puncture, exact/near metric-centre support}.
\end{array}
\tag{3.4}
\]

Expand a nonbinary star, equality, collar or metric weight into its finite
tagged atoms first; equivalently use the ordinary product telescoping
identity on those scalar factors. Put

\[
 P_q=\prod_jM_{j,q},\qquad
 P_+^T=\prod_jM_{j,q+1}\circ T_q,
\tag{3.5}
\]

and let \(U_q,U_+^T\) be the remaining actual smooth coefficients, with
the one-dimensional factor \(\lambda_q\) included in \(U_+^T\).
Pointwise,

\[
\begin{aligned}
P_qU_q-P_+^TU_+^T
={}&P_qP_+^T(U_q-U_+^T)\\
&+\sum_jP_q
 \left(\prod_{i<j}M_{i,q+1}\circ T_q\right)
 (1-M_{j,q+1}\circ T_q)U_q\\
&-\sum_jP_+^T
 \left(\prod_{i<j}M_{i,q}\right)
 (1-M_{j,q})U_+^T.
\end{aligned}
\tag{3.6}
\]

Indeed, (3.6) is
\(PQ(U-V)+P(1-Q)U-Q(1-P)V\), followed by
\(1-\prod_jM_j=\sum_j(1-M_j)\prod_{i<j}M_i\).
It is therefore exact, and every birth or death is assigned once to its
first failed mask. On the common binary support, write the remaining
coefficient as an ordered product of the smooth profile, collar, endpoint
profile, floor/equality weight, star and metric-centre weight and use

\[
 \prod_{j=0}^Nu_j-\prod_{j=0}^Nv_j
 =\sum_{j=0}^N(u_j-v_j)
   \prod_{i<j}v_i\prod_{i>j}u_i.
\tag{3.7}
\]

Equations (3.6)--(3.7) give, without overlap, the requested
common-interior smooth, coprimality, lift, ceiling, reciprocal-support,
collar, endpoint/floor, star/equality and metric-centre commutators. The
integer-lattice commutator is (1.3). Summing them reconstructs the literal
adjacent difference in (3.1); no atom is deleted or duplicated.

Two concrete jump sizes are useful. Since \(gb\) is odd,

\[
 \left\lceil\frac{g(b+2)}4\right\rceil
 -\left\lceil\frac{gb}4\right\rceil
 =\frac{g-\chi_4(gb)}2.
\tag{3.8}
\]

This is the literal untransported hard-edge jump. Under phase-preserving
transport, the continuous neighbor interval becomes

\[
 \left[\frac{g(b+2)}{4\lambda_q},\frac{ga}{\lambda_q}\right].
\tag{3.9}
\]

When its intersection with \([gb/4,ga]\) is nonempty, the lower and upper
unmatched widths are

\[
 \Delta x_-=\frac g4\left(\frac{b+2}{\lambda_q}-b\right),\qquad
 \Delta x_+=ga(\lambda_q^{-1}-1),
\tag{3.10}
\]

both \(\asymp L/D\). If the intersection is empty, the entire atom is a
support jump and there is no common-interior gain.

### 3.3 Dual endpoint slabs and the full common-band defect

The stationary endpoints in (2.6) are increasing, with exact increments

\[
 K_-(q+1)-K_-(q)
 =\frac{J}{\sqrt a(\sqrt{b+2}+\sqrt b)},
\tag{3.11}
\]

\[
 K_+(q+1)-K_+(q)
 =\frac{2J\sqrt a}
 {\sqrt b\sqrt{b+2}(\sqrt b+\sqrt{b+2})}.
\tag{3.12}
\]

They are both \(\asymp J/A\). Likewise the symmetric difference between
\(I_{q+1}\) and \(\lambda_qI_{q+1}\) has endpoint widths
\((1-\lambda_q)K_\pm(q+1)\asymp J/A=K/D\). These are the dual images of
the \(L/D\) physical slabs in (3.10).

Crucially, (1.3) also contains every integer in the common band. For a
negative Fourier mode \(r=-k\), \(k>0\), put
\(c_+=J\sqrt g\,\delta_{q+1}\). The exact square completion is

\[
 -c_+\sqrt y+ky
 =k\left(\sqrt y-\frac{c_+}{2k}\right)^2-\frac{c_+^2}{4k}.
\tag{3.13}
\]

At the scaled frequency \(k/\lambda_q\), the exterior carrier is
\(-c_+^2\lambda_q/(4k)\). Hence their exact phase displacement is

\[
 \frac{c_+^2(1-\lambda_q)}{4k}
 =\frac{Xg(\delta_{q+1}^2-\delta_q^2)}{4k}.
\tag{3.14}
\]

Now \(\delta_{q+1}^2-\delta_q^2\asymp D/A\); inserting (1.4) into
(3.14) gives (1.5). Thus Taylor expansion of the scaled comb costs
\((1-\lambda_q)c_+^2/k\asymp JL/A\), not \(D^{-1}\). Pairing \(k\)
with the nearest integer to \(k/\lambda_q\) has the same defect: an
\(O(1)\) frequency rounding error is multiplied by \(y\asymp L\). The
invertible continuous map therefore becomes a full common-band arithmetic
commutator on the integer comb.

### 3.4 Capacity ledger

The exact target for one \(L\)-block is \(L^2X^\varepsilon\). There are
\(O(AD)\) base/offset pairs in (1.4). The proved fixed-\(q\) row scale is
\(L^2/A\); a coefficient-blind sum over \(D\) offsets therefore has
capacity \(DL^2\).

The phase-aligned smooth material symbol displays only the factors
\(1-\lambda_q\asymp D^{-1}\) and the smaller relative change
\(b\mapsto b+2\). Even granting the optimally differentiated fixed-row
bound \(L^2/(AD)\) per \((a,q)\), this part would sum to \(L^2\). It is
not the obstruction.

The full common-band comb term has no such multiplier because of (3.14).
Its coefficient-blind capacity remains \(L^2/A\) per \((a,q)\), hence
\(DL^2\) in aggregate. Proving cancellation in its actual signed vector
is exactly a new polynomial-\(q\) theorem.

For comparison, the Round-77 complete collared coefficient satisfies

\[
 |\mathfrak B^\circ(g,k)|+g|\partial_g\mathfrak B^\circ(g,k)|
 \ll \frac{J\delta\sqrt G}{k^{3/2}}
 \asymp \sqrt{\frac{AL}{JD}}.
\tag{3.15}
\]

Absolute summation over the \(\Delta K\asymp J/A\) endpoint modes, all
\(G\asymp L/A\) lifts, and \(AD\) base/offset pairs gives

\[
 AD\,\frac JA\,\frac LA\,\sqrt{\frac{AL}{JD}}
 =L^2\sqrt{\frac{JD}{AL}}=L^2\sqrt\kappa.
\tag{3.16}
\]

Since \(A\le L\) and \(L^2\le J\),
\(\kappa=JD/(AL)\ge D\). Thus the endpoint slabs alone have an available
absolute deficit at least \(D^{1/2}\). Fixed physical collars do not cover
them. Cancellation between slabs and common bulk is possible, so (3.16)
is a route barrier, not an actual lower bound.

For every strict polynomial shell \(D=X^\eta\), \(\eta>0\), the common
comb ledger has deficit \(X^\eta\), and the endpoint ledger has deficit at
least \(X^{\eta/2}\). No choice of the literal \(A,L\) satisfying
\(A\le L\le J^{1/2}\) removes both. Bounded or prescribed
polylogarithmic \(D\) can be absorbed into \(X^\varepsilon\), but that
range was already owned before this round and is not a strict polynomial
subrange.

## 4. First doubtful or unproved step

The first unproved estimate is the one-sided signed bound for the literal
common-band scaled-comb packet (1.7), with its actual coefficient and all
tags. The continuous transport, its Jacobian, the parity high-pass and the
jump partition do not estimate it. Replacing (1.7) by the symmetric
difference of the two stationary bands discards the full common-band
terms and is false as an identity. Taylor expanding them loses the large
factor \(JL/A\) in (3.14).

The physical and dual endpoint slabs are a second open seam. Estimating
them separately by absolute values is stronger than the required global
real-part bound; (3.16) shows that the available absolute estimate is not
target-safe. A future proof may exploit joint cancellation between the
bulk comb, support jumps and endpoint slabs, but that is the original
actual signed problem in a new representation, not a gain proved here.

The no-go result is therefore scoped: phase preservation and smooth
material variation alone cannot yield a \(D\)-saving on the literal
integer symbol. It is not a lower bound for the actual Vaaler row and does
not rule out a new arithmetic estimate for (1.7).

## 5. Required control test and outcome

1. **\(q=1\).** Here \(1-\lambda_q\) need not be small and the common
   interval in (3.9) can be empty. The exact zero-extension and first-ray
   atom in (3.6) retain it; the accepted \(q=1\) owner is not reopened.
   **Outcome: pass; no transport gain is claimed.**

2. **Prescribed polylogarithmic rows.** If
   \(D\le(\log X)^C\), the coefficient-blind deficits in Section 3 can be
   absorbed into \(X^\varepsilon\), consistently with the proved
   fixed-\(q\) short-shell result. This gives no fixed positive-power
   range. **Outcome: pass.**

3. **Square, Pell, fourth-power and exact/near centres.** The carrier
   increment (3.14) can be integral or near integral on the previously
   recorded square, Pell and fourth-power configurations. Hence its large
   real size does not give a uniform distance from an integer. Accepted
   exact-centre and square owners are assigned once by (3.4); residual
   near centres remain in (1.7). **Outcome: a derivative-gap shortcut
   fails.**

4. **Hard lower edge.** Formula (3.8) retains the literal ceiling and
   \(W(1)=1\). Formula (3.10) shows that phase-preserving transport creates
   an \(L/D\) entry slab in addition to the \(O(g)\) adjacent ceiling
   jump. It is not swallowed by a fixed collar. **Outcome: pass; the slab
   is open at the capacity (3.16).**

5. **Empty and singleton fibres.** The open interval and equality atoms
   remain separate. If either the physical or reciprocal common
   intersection is empty, (3.6) assigns the whole term to a birth/death
   packet; if it has one integer, (1.3) is still exact. No division by the
   fibre length occurs. **Outcome: pass.**

6. **Coprimality and lifts.** Identity (2.2) is exact. Mobius expansion
   shows that the primitive mask alone has bounded alternating interval
   sums, but its raw adjacent variation can be \(\asymp D\); multiplying
   it by (1.7) is precisely the unproved seam. Lift births and deaths from
   \(gb_q\in\mathscr H_L\) are owned before the ceiling packet by (3.4).
   **Outcome: pass; no primitive or lift saving is inferred.**

7. **False unsigned and phase-conjugating coefficients.** On any finite
   common band, a bounded phase-conjugating model can make
   \(\widehat H(-k/\lambda_q)\) and \(-\widehat H(-k)\) coherent, so the
   comb difference has the full band capacity. Removing \((-1)^q\), or
   taking absolute values before summing \(q\), is therefore false as a
   coefficient-blind route. This model is not a lower bound for the
   Vaaler symbol; it shows exactly why a proof must use a new property of
   the actual coefficient. **Outcome: required false analogue fails.**

8. **Exact target and norm separation.** The material ledger is at best
   \(L^2\), the common-comb ledger is \(DL^2\), and the endpoint absolute
   ledger is \(L^2\sqrt\kappa\) with \(\kappa\ge D\). The high-pass remains
   signed throughout; no total variation, modulus, fixed-\(a\) Gram or
   blockwise absolute norm is substituted for the required global real
   part. **Outcome: no polynomial subrange closes.**

9. **Orientation and downstream scope.** Only \(a<b\) is present and the
   hard energy retains one outer \(2\Re\). The analysis uses no second
   Poisson/Gaussian/B-process as a claimed gain. It says nothing about
   either smooth M2 packet or any M1 packet. **Outcome: pass.**

## 6. Dependencies and exact artifacts used

The derivation uses only the following supplied artifacts and the accepted
nodes they record:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m2-adjacent-ray-transport-commutator/derivation_packet.md;
- rounds/codex-managed/m9-m2-adjacent-ray-transport-commutator/candidates/conductor_adjacent_transport_commutator.md;
- rounds/codex-managed/m9-m2-global-signed-completed-directional/synthesis.md;
- rounds/codex-managed/m9-m2-global-signed-completed-directional/reviews/conductor_round110_recombination_and_orientation.md;
- rounds/codex-managed/m9-m2-polynomial-q-maximal-alternation/synthesis.md;
- rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reviews/conductor_round77_adjudication.md.

The exact parity row and physical real-part target depend on
M9-M2-global-completed-realpart-self-return. The complete coefficient
bound (3.15) depends on M9-M2-top-endpoint-actual-symbol-variation. The
\(q=1\) and polylogarithmic controls are used only in their already
accepted scopes. No external theorem or numerical experiment is used.

## 7. Recommended state effect

**Retain** M9-M2-top-endpoint-density-discrepancy-energy and
M9-M2-top-endpoint-signed-cone as open. **Promote only if independently
reviewed** the scoped exact connector/obstruction consisting of
(1.1)--(1.5), the one-count decomposition (3.6)--(3.7), the slab sizes
(3.10)--(3.12), and the conclusion that phase-preserving continuous
transport does not furnish a coefficient-blind \(D^{-1}\) bound for the
literal integer row. **Reject** claims that only the \(J/A\) endpoint band
survives, that fixed Round-77 collars own the \(L/D\) transport slabs, or
that a large real carrier increment supplies a uniform modular gap.

The smallest lawful next object is the actual signed common-band
scaled-comb correlation (1.7), possibly kept jointly with its support
slabs so that no necessary cancellation is destroyed. There is no state
change for the fixed-\(a\) Gram, either smooth M2 packet, M9-M2, M9-M1,
endpoint uniformity, M9 or the global exponent.
