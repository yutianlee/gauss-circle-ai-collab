# Signed-inverse normalization, transport, and power-ledger seam review

- Campaign: m9-m1-t1-fast-height-jump-coboundary-gate
- Round: 191
- Artifact reviewed:
  candidates/formalized_hard_m1_t1_fast_signed_inverse_transport_reduction.md
- Review role: exact normalization, transport, source-coverage, and power
  seam
- Numerical evidence: diagnostic only
- Verdict: **REPAIR**

## 1. Result

The candidate's central mathematics is sound at the stated strict-sector
level:

1. the signed-least-inverse transport (191.C17)--(191.C20) is exact in
   both orientations;
2. the carry parity in (191.C23)--(191.C24) has the correct sign;
3. the inverse-class count and literal-class multiplicity in
   (191.C26)--(191.C28) give the claimed
   \(Qm\kappa uX^\varepsilon\) fixed-packet scale;
4. the terminal and isolated Fejer pieces have the claimed
   \(O(\kappa uX^\varepsilon)\) scale; and
5. after the exact \(m^{-1}c_q(a)\) lift, the
   \(a,J,m,q,u,\kappa\) ledger closes at \(L^2X^\varepsilon\).

No target-safe term is mathematically forced to remain inseparable from
the open signed packet. The whole small-inverse row sector is an exact
row subset, while the terminal and Fejer pieces are exact linear
components of the backward difference. Each is bounded absolutely at
target scale before it is removed, so subtracting them leaves a lawful
single signed complement.

The candidate is nevertheless not ready for a green seam or graph
promotion. Three formal gaps must be repaired:

- the fixed-\((\kappa,u,m,q,a,J)\) packet and the global
  \(\mathscr F_{Y,Q}^{\sigma}\) aggregate are conflated in
  (191.C8)--(191.C12);
- (191.C25) does not display the product rule for the two conjugated
  endpoint coefficients, and its literal first-change list is not the
  complete Round-189 list; and
- the terminal and Fejer linear projections are described but not
  defined with their exact \(K,G,\mathcal C\), orientation, and band
  gates before the absolute estimates are taken.

These are repairable normalization and coverage defects, not a
counterexample to the strict signed-inverse reduction. The full fast
packet and the large-inverse remainder remain open.

## 2. Quantifiers, domain, and empty/saturated cases

The inherited conditions

\[
 U=mq>4Q,\quad q>Q,\quad m|a|_q>Q,\quad Qm<Y,
 \quad U\mid u,
\tag{R191.1}
\]

together with (191.C3)--(191.C4), match the Round-189 fast domain. In
particular \(Qm<Y\) implies \(Y>Q\), and odd \(U\) implies odd \(m,q\).
The signed least inverse is unique because \(U\) is odd.

The formal statement should nonetheless state, rather than leave
transitive, all of the following quantifiers:

\[
 m,q,\kappa,g,u,v,h>0,\qquad
 1\le a<q,\qquad(a,q)=1,\qquad L\ll X^{1/4}
\tag{R191.2}
\]

on nonzero inherited hard-top support. The unit condition on \(a\) is
used in the coefficient mass (191.C33) and is present in the Round-189
kernel, but is absent from (191.C1)--(191.C4). The support condition
\(L\ll X^{1/4}\) is needed when the fixed polylogarithmic \(Q\) and
divisor logarithms are absorbed in (191.C35).

There are two distinct saturation controls.

- If \(T_Q=(q-1)/2\), then (191.C4) is impossible because every unit
  slope has \(j_q(a,v)\le(q-1)/2\). The entire Round-189 fast packet is
  empty. This vacuous case should be stated explicitly before choosing a
  \(J\)-band.

- If \(T_\varrho=0\), (191.C7) is empty. If
  \(T_\varrho=(U-1)/2\), every unit inverse class is in (191.C7), so its
  complement inside the already fixed fast packet is empty. The
  candidate states both of these correctly.

For an exact global identity, the candidate must choose a disjoint
half-open dyadic partition of the nonempty fast values, for example
\(2^r\le j_q(a,v)<2^{r+1}\) with the final band truncated at
\((q-1)/2\). Saying only that dyadic bands cost a logarithm is enough
for an inequality, but not enough to make (191.C11) an exact identity.

The main quantifier repair is to introduce two typed levels. First
define explicitly

\[
 \mathscr J_{\kappa,u,m,q,a,J}^{\sigma}
 =\sum_{\substack{\omega,v\ {\rm literal}\\
                   J\le j_q(a,v)<2J}}
 \frac1{1-z_{\omega,v}}
 \sum_h\Delta^-W_{v,\omega}(h)z_{\omega,v}^h,
\tag{R191.3}
\]

and define its safe and remainder components at this fixed level.
Second, define the global safe and remainder aggregates by inserting
the inherited outer factors, including \(m^{-1}c_q(a)\), and summing the
chosen disjoint \(J\)-partition. Only those global quantities may be
placed in the equality with the Round-189
\(\mathscr F_{Y,Q}^{\sigma}\). As written, (191.C8)--(191.C9) use fixed
packet quantities, while (191.C11)--(191.C12) use global notation
without defining the intervening lift and sum. This type mismatch is a
required repair.

## 3. Transport and C23--C25 source coverage

Let

\[
 \varrho v-\gamma U=1,\qquad
 \epsilon_+=1,\quad\epsilon_-=-1.
\tag{R191.4}
\]

For the plus determinant \(Sv-Uw=h\), subtracting
\((\varrho,\gamma)\) changes the determinant by \(-1\). For the minus
determinant \(Uw-vS=h\), adding the same pair also changes it by
\(-1\). Therefore (191.C17) is correct. Since the two canonical anchors
differ by a multiple of \(U\),

\[
 \nu_\omega(h)=
 \frac{S_{0,\omega}(h)-\epsilon_\omega\varrho
       -S_{0,\omega}(h-1)}U
\tag{R191.5}
\]

is integral; the signed-least range gives
\(\nu_\omega(h)\in\{-1,0,1\}\). Substitution in the defining formula
for \(w_{0,\omega}\) proves (191.C19)--(191.C20). Reindexing
\(t\mapsto t+\nu_\omega(h)\) multiplies the old affine parity by
\((-1)^{\nu_\omega(h)}\). The pre-Fourier parity ratio
\((-1)^\varrho\) is also correct in both orientations. No orientation
antisymmetry follows.

Equation (191.C23) is an exact partition: translation by the integer
\(\nu_\omega(h)\) is a bijection of \(\mathbb Z\), so the transported
common indices, current births, and previous deaths cover the two
positivity sets without overlap. Equation (191.C24) is also exact,
because

\[
 B_h-\chi B_-^{\rm tr}
 =(1-\chi)B_-^{\rm tr}+(B_h-B_-^{\rm tr})
\tag{R191.6}
\]

and the last difference is the displayed three-factor telescope.

The endpoint expansion is not yet formally complete. If

\[
 \Lambda_h=\lambda_{1,h}\overline{\lambda_{0,h}},
\tag{R191.7}
\]

the candidate must insert, with the actual orientation-dependent
endpoint arguments,

\[
\begin{aligned}
 \Lambda_h-\Lambda_-^{\rm tr}
 ={}&(\lambda_{1,h}-\lambda_{1,-}^{\rm tr})
       \overline{\lambda_{0,h}}\\
 &+\lambda_{1,-}^{\rm tr}
   (\overline{\lambda_{0,h}}
    -\overline{\lambda_{0,-}^{\rm tr}}).
\end{aligned}
\tag{R191.8}
\]

Only after (R191.8) is (191.C25) applied separately to endpoints
\(i=0,1\). This repair is needed to verify conjugation, endpoint order,
and exactly-once coverage; it may be made by writing the K185.33 and
K185.35 endpoint arguments explicitly or by an exact citation plus the
formula (R191.8).

The first-change list following (191.C25) must also be expanded. The
Round-189 literal class includes at least the original shell and height
predicates, the strict original endpoint-ratio cone, residual and any inherited
selector state, profile support/branch and numerical profile, floor,
star, half-weight, hard sample, real-\(X\) crossing, endpoint trace,
conjugation/order, and endpoint zero extension. Positivity is already
handled by (191.C23), outer \((U,h)=1\) by \(G\), squarefree and
allocation coprimality by \(M\), Fejer by \(F\), and phase by \(\Psi\).
The repaired list must say that its profile entry is a cell/branch
label, not a replacement of the actual numerical profile, and must
assign simultaneous changes by one declared first-change order. With
these additions, C23--C25 cover every named source exactly once. As
written, the omitted shell/height/strict-cone and generic-selector labels
make the claim of literal source coverage too strong.

For full formal clarity, the candidate should also display the
indicator identity that precedes C23: \(K\)-birth/death terms use the
complete live-side \(GA\); on common \(K\), \(G\)-birth/death terms use
the complete live-side \(A\); only common \(K=G=1\) enters C23. This
prevents a simultaneous \(K,G\) change from being charged twice.

## 4. Inverse-class multiplicity and strict-sector estimate

The inverse-class calculation is green. In signed representatives,

\[
 \#\{v\bmod U:0<|\varrho_U(v)|\le R\}
 =2\sum_{\substack{1\le r\le R\\(r,U)=1}}1
 \le2R,
 \qquad0\le R\le\frac{U-1}{2}.
\tag{R191.9}
\]

Because \(U\mid u\), a residue class in an interval of length \(O(u)\)
occurs

\[
 O(u/U+1)=O(u/U)
\tag{R191.10}
\]

times; \(u/U=g\ge1\) is essential in the last equality. Arbitrary
literal deletions only reduce this count. Hence

\[
 \#v_{\rm inv}\ll \frac{uT_\varrho}{U}
 \le\frac{Qmu}{Y}.
\tag{R191.11}
\]

The extra \(J\)-band and Round-189 fast predicates only delete values.
With \(O(Y)\) heights, \(O(\kappa)\) live sites per oriented row, and a
fresh endpoint \(X^\eta\) allowance, (R191.11) gives

\[
 |\mathscr J_{\rm inv}|
 \ll Qm\kappa uX^\eta.
\tag{R191.12}
\]

It is legitimate to avoid the \(q/J\) factor here: rowwise finite
support gives the exact inverse Abel identity (191.C15), after which the
whole selected row sum is bounded. The two orientations are both inside
the selected complex packet; the proof merely gives that packet a
stronger absolute estimate.

This strict sector uses no special endpoint regularity. Any prescribed
set of \(O(QmU/Y)\) inverse classes has the same proof. The signed
transport makes the cut natural and exposes the exact carry, but the
estimate itself is cardinality-only sector shaving. It supplies no
density assertion and no gain for the large-inverse complement.

## 5. Terminal/Fejer projections and one outer operation

The power estimates (191.C30) and (191.C32) are correct, subject to an
exact definition of the projected terms.

The \(K\)-support is the intersection of two integer intervals, so its
backward difference has at most one birth and one death. At a live side
the complete row has \(O(\kappa X^\eta)\) size. Thus

\[
 (q/J)(uJ/q)\kappa X^\eta
 \ll\kappa uX^\eta.
\tag{R191.13}
\]

On transported common sites with
\(K_h=K_{h-1}=G_h=G_{h-1}=1\),

\[
 F_h-F_{h-1}=-\frac{2\kappa g}{R_0}.
\tag{R191.14}
\]

Because a common live height has \(h-1>Y\) and
\(2\kappa g(h-1)<R_0\), one has
\(2\kappa gY/R_0<1\). Counting \(O(Y)\) heights and
\(O(\kappa)\) current live sites gives

\[
 (q/J)(uJ/q)Y\kappa\frac{2\kappa g}{R_0}X^\eta
 \ll\kappa uX^\eta.
\tag{R191.15}
\]

No phase, endpoint, or orientation cancellation is used in either
bound.

Separating these terms is lawful only as the following exact linear
operation. First remove all rows satisfying C7. On the remaining rows,
define the terminal projection from the two live-side terms in the exact
\(K\)-indicator identity. Define the Fejer projection only from the
\((F_h-F_{h-1})\Lambda_h\Psi_h\) summand of C24, with common
\(K,G\), transported-common \(t\), both orientations, the fixed fast
band, and the factor \(z^h/(1-z)\) still present. Form their signed sum
before applying the one exterior modulus used for the safe bound. The
remainder is the exact algebraic difference.

The candidate currently specifies these gates only in prose. It must
write them into the definitions of
\(\mathscr J_{\rm terminal}\),
\(\mathscr J_{\rm Fejer}\), and
\(\mathscr J^{\rm safe}\). Once that repair is made, no target-safe term
has been improperly detached from a cancellation on which its proof
depends: (R191.13)--(R191.15) are independent absolute bounds. The
large-inverse remainder must continue to keep its coprimality flips,
births/deaths, carry, both endpoint changes, literal events, and phase
under one outer real part. It may not be separately absolutized.

## 6. Lift, outer \(L^2\) ledger, and diagnostics

The lift and coefficient normalization are green:

\[
 c_{mq}(ma)=m^{-1}c_q(a),\qquad
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q).
\tag{R191.16}
\]

Multiplying the fixed safe bound \(Qm\kappa uX^\eta\) by the lift
removes \(m\) exactly before any positive outer sum:

\[
 m^{-1}|c_q(a)|Qm\kappa u
 =Q\kappa u|c_q(a)|.
\tag{R191.17}
\]

The disjoint \(J\)-bands cost one logarithm. Writing \(u=mqr\),

\[
 \sum_{mq\mid u}1=\tau_3(u),
\tag{R191.18}
\]

so the outer sum is

\[
 QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u)
 \ll QL^2\log^{O(1)}(2L)X^\eta.
\tag{R191.19}
\]

Using the inherited nonzero support \(L\ll X^{1/4}\), fixed \(B\), and
a fresh \(\eta<\varepsilon\), (R191.19) is
\(O_{B,\varepsilon}(L^2X^\varepsilon)\). No positive power of \(Y\)
is hidden. Candidate (191.C35) is correct after the support and fresh
epsilon are stated explicitly.

The first Wolfram note,
controls/conductor_round191_wolfram_height_jump_check.md, passes
470,029 exact ordinary-anchor/Abel checks and 2,720 bounded-array
capacity cases, with zero failures and maximum numerical error
\(3.21\times10^{-14}\). Its anchor convention uses the ordinary least
inverse, so by itself it does not check the signed representative.

The second note,
controls/conductor_round191_signed_inverse_transport_check.md, directly
passes 420,672 exact signed-inverse transport/parity checks and 1,325
exact inverse-class counts, with zero failures. It checks both
orientations, the carry range, and the parity ratio. These controls
support the finite algebra only. They do not prove the literal interval
multiplicity, asymptotic bound, lift, outer ledger, density, or any
cancellation in the remainder; those are supplied, or left open, by the
analytic argument above.

Exact artifacts used in this review were:

1. protocol.md;
2. proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md;
3. rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/candidates/formalized_hard_m1_t1_fast_signed_inverse_transport_reduction.md;
4. rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/controls/conductor_round191_wolfram_height_jump_check.md; and
5. rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/controls/conductor_round191_signed_inverse_transport_check.md.

No external theorem or numerical asymptotic evidence was used.

## 7. Required repairs and recommended state effect

Verdict: **REPAIR**, followed by a focused replay of this seam.

The candidate must make all of the following changes before promotion:

1. add the missing unit/positivity quantifiers, the inherited
   \(L\ll X^{1/4}\) support, and the empty saturated-fast case;
2. define the fixed packet (R191.3), choose a disjoint dyadic
   \(J\)-partition, then separately define the lifted global safe and
   remainder aggregates before asserting the global equality C11;
3. insert the two-endpoint conjugated product rule (R191.8), with the
   actual orientation-dependent endpoint order;
4. expand the first-change labels to every Round-189 literal field and
   distinguish profile cell labels from their actual numerical values;
5. write the complete \(K,G\) indicator identity and the exact gated
   definitions of the terminal and Fejer projections before bounding
   them; and
6. state the fresh-\(\eta\) rebudget and inherited shell support used in
   C35, and cite both diagnostics only as finite controls.

After those repairs, the signed-inverse transport, strict row sector,
terminal/Fejer projections, exact complement, and outer power ledger are
eligible for a green re-review as one subordinate reduction. Until
then, do not create or promote a proved_internal node from
(191.C5)--(191.C11). Keep the complete fast packet, complete original
\(t=1\) residual, every original \(t\ge2\) and large-\(G\) complement,
both M1 parents, every M2 parent, endpoint uniformity, M9, both bridges,
the quarter theorem, and every exponent unchanged.
