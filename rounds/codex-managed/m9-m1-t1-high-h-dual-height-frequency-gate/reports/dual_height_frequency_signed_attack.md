# 1. Result: projective slow sector and literal-discrepancy barrier

- Campaign: m9-m1-t1-high-h-dual-height-frequency-gate
- Round: 189
- Task: dual_height_frequency_signed_attack
- Role: discovery
- Starting graph SHA-256:
  338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c
- Evidence status: candidate evidence only; no proof-state edit

Fix the exact Round-188 complement, with

\[
 Q=H_B=\lfloor(\log(2X))^B\rfloor,\qquad
 U=mq>4Q,\qquad q>Q,\qquad m|a|_q>Q,\qquad Qm<Y.
\tag{189.A1}
\]

For every retained unit \(a\bmod q\) and every literal \(v\), define

\[
 b_q(a,v)=[a\bar v]_q,\qquad
 j_q(a,v)=|a\bar v|_q
 =\min\{b_q(a,v),q-b_q(a,v)\}.
\tag{189.A2}
\]

Here \(\bar v\) is the inverse modulo \(q\). It exists because
\(q\mid U\mid u\) and \((u,v)=1\). The orientation sign replaces
\(b_q(a,v)\) by \(-b_q(a,v)\) and therefore does not change \(j_q\).

The coefficient-insensitive baseline sector

\[
 1\le j_q(a,v)\le \left\lfloor {U\over Y}\right\rfloor
 =\left\lfloor {mq\over Y}\right\rfloor
\tag{189.A3}
\]

is absolutely target-safe. More strongly, put \(P=Q\) and

\[
 T_P(m,q;Y)
 :=\min\!\left\{{q-1\over2},
       \left\lfloor {Pmq\over Y}\right\rfloor\right\}.
\tag{189.A4}
\]

Then the complete enlarged sector \(1\le j_q(a,v)\le T_P(m,q;Y)\)
has total absolute size

\[
 \boxed{|\mathscr S_{Y,Q;P}^{\sigma}|
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{189.A5}
\]

The proof is exact: at fixed \((\kappa,u,m,q,a)\) the projective slow
set occupies at most \(2T_P\) residue classes of \(v\bmod q\), hence
has \(O(uPm/Y)\) literal \(v\)-values. The \(O(Y)\) heights and
\(O(\kappa)\) affine sites contribute \(Y\kappa\), while the exact
Fourier-lift weight

\[
 c_{mq}(ma)=m^{-1}c_q(a)
\tag{189.A6}
\]

cancels the factor \(m\) from the projective count before any divisor
or outer-label triangle inequality. The remaining fixed-label cost is
\(O(P\kappa u\log(2q)X^\eta)\). The exact nested-label count is only
\(\sum_{mq\mid u}1=\tau_3(u)\), so \(P=Q\) is absorbed by a fresh
epsilon budget. No positive power of \(Y\) is absorbed.

The cap in (189.A4) is literal. If
\(\lfloor Pmq/Y\rfloor\ge(q-1)/2\), every possible dual frequency is
already paid. If \(\lfloor Pmq/Y\rfloor=0\), the sector is empty.
The baseline \(P=1\) required by the brief is a subset of (189.A5).
The same proof permits any specified fixed power of \(Q\), at the
corresponding fixed-polylogarithmic price; there is no largest fixed
polylogarithmic enlargement. The scale \(U/Y\) is the maximal
coefficient-insensitive scale before such epsilon-rebudgetable factors.

Define \(\mathscr F_{Y,Q;P}^{\sigma}\) by the exact complementary
condition

\[
 j_q(a,v)>T_P(m,q;Y).
\tag{189.A7}
\]

Then, before positivity,

\[
 \boxed{\mathscr C_{Y,Q}^{\sigma}
 =\mathscr S_{Y,Q;P}^{\sigma}
  +\mathscr F_{Y,Q;P}^{\sigma}.}
\tag{189.A8}
\]

The fast complement retains one outer real part over both
orientations and every literal label. Its complete target is not
proved. A dyadic geometric height sum would close it if the actual
zero-extended endpoint aggregate had the discrepancy stated in
(189.A28) below. The permitted dependencies give only the trivial
bound, larger by \(Y/(Pm)\) at the variation interface and by as much
as the full factor \(Y\) on primitive lifts. Literal squarefree,
coprimality, selector, profile, endpoint, anchor, and phase jumps
prevent replacing that missing relation by an assumed bounded-variation
law.

The centered exact-conductor identity also supplies a mandatory
falsifier: for an odd prime \(p\),
\(K_p^\circ(b)=E_p(b)\), and

\[
 \sum_{h=1}^{(p-1)/2}K_p^\circ(-2h)
 =-{p-1\over2}.
\tag{189.A9}
\]

Thus no uniform polylogarithmic height-prefix estimate follows merely
from exact-conductor centering. This is a kernel control, not literal
lower mass.

The proved candidate exit is
strict_dual_height_resonance_sector. The exact fast complement remains
an actual-coefficient discrepancy problem.

# 2. Exact statement and hypotheses

Fix real \(X\ge2\), a nonempty literal middle or lower residual hard-M1
shell \(L\ge2\), \(\sigma\in\{+1,-1\}\), fixed \(B>0\), and a
nonempty dyadic integer block \(Y<h\le2Y\) with \(Y>Q\). Put
\(R_0=\lceil L\rceil\), \(Q=H_B\), and retain exactly the accepted
Round-185 carrier and amplitudes (K185.27), (K185.30)--(K185.35).
Thus

\[
 \kappa,g,h,U,v>0,\quad \kappa,g,U\ {\rm odd},\quad
 (gU,v)=1,\quad(U,h)=1,\quad
 0<2\kappa gh<R_0.
\tag{189.A10}
\]

Write \(u=gU\), \(U=mq\), and

\[
 A_{\kappa,u,U,h,v,\omega}^{\sigma}
 :=\sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t),
 \qquad
 \mathfrak f=(\kappa,u/U,h,U,v).
\tag{189.A11}
\]

Every residual selector, squarefree and allocation-coprimality
deletion, shell, cone, profile, floor, star, half-weight, hard sample,
crossing, endpoint, conjugation, Fejer factor, square-root phase,
orientation sign, positivity predicate, affine site, and zero
extension remains inside \(B\) and \(A\).

The exact Round-188 complex complement is

\[
\begin{aligned}
 \mathscr C_{Y,Q}^{\sigma}
 ={}&\sum_{\omega\in\{+,-\}}\sum_{\kappa,u}
 \sum_{\substack{mq\mid u\\mq>4Q\\q>Q\\Qm<Y}}
 {1\over m}
 \sum_{\substack{Y<h\le2Y\\(mq,h)=1\\
       0<2\kappa(u/(mq))h<R_0}}
 \sum_{\substack{v>0\\(u,v)=1}}\\
 &\quad\times
 \sum_{\substack{a\in(\mathbb Z/q\mathbb Z)^\times\\
                   m|a|_q>Q}}
 c_q(a)e\!\left({\epsilon_\omega a\bar v h\over q}\right)
 A_{\kappa,u,mq,h,v,\omega}^{\sigma},
\end{aligned}
\tag{189.A12}
\]

where \(\epsilon_+=1\), \(\epsilon_-=-1\), and all sums are literal
zero-extended sums. On live support,

\[
 u,v\asymp {L\over\kappa},\qquad
 \#\{t\ {\rm live\ on\ one\ oriented\ row}\}=O(\kappa),
\qquad
 |B(t)|\ll_\eta X^\eta.
\tag{189.A13}
\]

The coefficient normalization and mass are exactly

\[
 c_q(a)={2\over q\{1+e(-a/q)\}},\qquad
 {1\over m}\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}|c_q(a)|
 \ll {\,\log(2q)\over m}.
\tag{189.A14}
\]

For \(P\ge1\), define \(\mathscr S_{Y,Q;P}^{\sigma}\) by inserting
\(1\le j_q(a,v)\le T_P(m,q;Y)\) into (189.A12), and define
\(\mathscr F_{Y,Q;P}^{\sigma}\) by inserting
\(j_q(a,v)>T_P(m,q;Y)\). Equation (189.A8) is a disjoint exhaustive
complex identity. In particular,

\[
 \Re\mathscr C_{Y,Q}^{\sigma}
 =\Re\{\mathscr S_{Y,Q;P}^{\sigma}
       +\mathscr F_{Y,Q;P}^{\sigma}\}
\tag{189.A15}
\]

has one real part outside both orientations and all remaining labels.
The proved assertion is (189.A5) for \(P=Q\). The exact remaining
one-sided relation is

\[
 \boxed{\Re\mathscr F_{Y,Q;Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{189.A16}
\]

No complete high-height relation, complete original-\(t=1\) residual,
small-\(t\) owner, parent, bridge, theorem, or exponent is asserted.

# 3. Proof and derivation

## 3.1 Projective bijection and exact two-sided count

Because \(q\mid u\) and \((u,v)=1\), the residue of \(v\) lies in
\((\mathbb Z/q\mathbb Z)^\times\). For fixed
\(a\in(\mathbb Z/q\mathbb Z)^\times\), the map

\[
 v\bmod q\longmapsto a\bar v\bmod q
\tag{189.A17}
\]

is a bijection of the units, with inverse class
\(v\equiv a b^{-1}\pmod q\). Thus no \(v\)-class is lost or
duplicated. The condition \(1\le|b|_q\le T\) uses at most \(2T\)
unit classes: one side has representatives \(1,\ldots,T\), the other
has \(q-T,\ldots,q-1\). If the sides overlap, this only lowers the
count.

The ambient literal \(v\)-support is contained in an interval of length
\(O(u)\), since \(v\asymp L/\kappa\) and
\(u\asymp L/\kappa\). Each residue class modulo \(q\) occurs at most

\[
 O(u/q+1)=O(u/q)
\tag{189.A18}
\]

times because \(q\mid u\) implies \(u/q\ge1\). Literal
coprimalities, selectors, endpoint restrictions, and zero extensions
only delete values. Therefore

\[
\begin{aligned}
 \#\{v\ {\rm literal}:(u,v)=1,\,
       1\le j_q(a,v)\le T_P\}
 &\ll {uT_P\over q}\\
 &\ll {uPm\over Y}.
\end{aligned}
\tag{189.A19}
\]

This includes arbitrary interval endpoints and both least-residue
sides. If \(T_P=0\), the left side is exactly zero. If
\(T_P=(q-1)/2\), it includes every possible unit class. The sign
\(\epsilon_\omega\) only interchanges the two sides, so (189.A19)
holds identically for both orientations.

## 3.2 Slow-sector atom and power ledger

Fix \((\kappa,u,m,q,a)\). There are \(O(Y)\) admissible heights in
the dyadic block, including a truncated terminal block,
\(O(uPm/Y)\) possible slow \(v\)'s by (189.A19), and
\(O(\kappa)\) live affine sites on each oriented row, including the
affine \(+1\). Hence

\[
 \sum_{\omega,h}
 \sum_{\substack{v:\,1\le j_q(a,v)\le T_P}}
 \sum_{t\in I_{\mathfrak f,\omega}}
 |B_{\mathfrak f,\omega}^{\sigma}(t)|
 \ll_\eta Pm\kappa uX^\eta.
\tag{189.A20}
\]

Weighting (189.A20) by the Fourier coefficients and summing \(a\)
uses exactly
\(m^{-1}\sum_a|c_q(a)|\ll m^{-1}\log(2q)\). It gives fixed
\((\kappa,u,m,q)\) cost

\[
 \ll_\eta P\kappa u\log(2q)X^\eta.
\tag{189.A21}
\]

The cancellation in (189.A21) is exact: the \(m\) from projective
multiplicity is removed by \(c_{mq}(ma)=m^{-1}c_q(a)\) before the
triangle inequality over \(m,q,u,\kappa\). No condition
\((m,q)=1\) is used.

There is no fourth divisor variable. Writing \(u=mqr\),

\[
 \sum_{mq\mid u}\log(2q)
 =\sum_{mqr=u}\log(2q)
 \le\tau_3(u)\log(2u).
\tag{189.A22}
\]

Since \(\kappa u\ll L\) on live support,

\[
\begin{aligned}
 |\mathscr S_{Y,Q;P}^{\sigma}|
 &\ll_\eta
 PLX^\eta
 \sum_{\kappa\ll L}
 \sum_{u\asymp L/\kappa}
 \tau_3(u)\log(2u)\\
 &\ll_\eta
 PL^2\log^{O(1)}(2L)X^\eta.
\end{aligned}
\tag{189.A23}
\]

The last line follows from
\(\sum_{n\le Z}\tau_3(n)\ll Z\log^2(2Z)\) and
\(\sum_{n\le Z}\tau_3(n)/n\ll\log^3(2Z)\), after swapping the
\(\kappa,u\) order. For \(P=Q\), the accepted support
\(L\ll X^{1/4}\) and fixed \(B\) absorb
\(Q\log^{O(1)}(2L)\) into a fresh part of \(X^\varepsilon\).
This proves (189.A5). The factor \(Y\) disappeared in
\(Y\cdot(uPm/Y)\cdot\kappa\cdot m^{-1}\) before positive
recombination; no power of \(Y\) was rebudgeted.

The same calculation with \(P=1\) proves the exact baseline
(189.A3). Conversely, a coefficient-insensitive threshold
\(T=R\,U/Y\) leaves the factor \(R\) in (189.A21). Thus \(U/Y\)
is the maximal scale with unit cost. Fixed powers of \(Q\) are lawful
enlargements only because their explicit \(R\) is
epsilon-rebudgetable, not because it vanishes.

## 3.3 Exact dyadic fast complement

For each fixed \((m,q,Y)\), the integer set
\(T_P<j\le(q-1)/2\) has the exact disjoint dyadic partition

\[
 \mathcal J_r=
 \{j:2^r(T_P+1)\le j<
       \min(2^{r+1}(T_P+1),(q+1)/2)\},
\tag{189.A24}
\]

with empty terminal sets omitted. Put \(J_r=2^r(T_P+1)\).
Then \(J_r\le j<2J_r\), and the union of the corresponding complex
subaggregates is exactly \(\mathscr F_{Y,Q;P}^{\sigma}\), still under
one outer real part.

For fixed \(a\), a \(J\)-block occupies \(O(J)\) projective
\(v\)-classes and hence

\[
 \#\{v\ {\rm literal}:J\le j_q(a,v)<2J\}
 \ll {uJ\over q}.
\tag{189.A25}
\]

If the amplitude were constant in height, the geometric estimate would
be

\[
 \left|\sum_{Y<h\le2Y}
 e\!\left({\epsilon_\omega a\bar v h\over q}\right)\right|
 \ll\min\{Y,q/j_q(a,v)\}\ll {q\over J}.
\tag{189.A26}
\]

Together (189.A25)--(189.A26) exactly balance \(J/q\) against
\(q/J\). The actual amplitude is not constant, so (189.A26) cannot be
inserted without a literal discrepancy theorem.

## 3.4 Exact Abel interface and quantitative deficit

For fixed \((\kappa,u,U,v,\omega)\), define the actual zero-extended
height sequence

\[
\begin{aligned}
 W_{\kappa,u,U,v,\omega}^{\sigma}(h)
 :={}&{\bf1}_{Y<h\le2Y}
 {\bf1}_{(U,h)=1}
 {\bf1}_{0<2\kappa(u/U)h<R_0}\\
 &\times A_{\kappa,u,U,h,v,\omega}^{\sigma}.
\end{aligned}
\tag{189.A27}
\]

All literal restrictions inside \(A\) remain present. Let
\(\mathsf V(W)\) be its total discrete variation on the integer line,
including the two zero-extension jumps. Summation by parts and the
geometric bound give, for \(J\le j_q(a,v)<2J\),

\[
 \left|\sum_h W(h)
 e\!\left({\epsilon_\omega a\bar v h\over q}\right)\right|
 \ll {q\over J}\,\mathsf V(W).
\tag{189.A28}
\]

The first sufficient actual-coefficient variation relation is

\[
 \boxed{
 \sum_{\substack{v\ {\rm literal},\ (u,v)=1\\
                  J\le j_q(a,v)<2J}}
 \mathsf V\!\left(
 W_{\kappa,u,mq,v,\omega}^{\sigma}\right)
 \ll_\eta {Pm\kappa uJ\over q}X^\eta.}
\tag{189.A29}
\]

Indeed (189.A28)--(189.A29) give a \(v,h\) discrepancy
\(O(Pm\kappa uX^\eta)\). Multiplication by \(1/m\), summation of
\(|c_q(a)|\), the \(O(\log(2q))\) dyadic blocks, and the exact
\(\tau_3(u)\) ledger then reproduce (189.A23), with one additional
fixed logarithm. Thus (189.A29), or a weaker genuinely joint signed
substitute with the same final ledger, would prove (189.A16).

No permitted dependency proves (189.A29). From (189.A13) one only has

\[
 |W(h)|\ll_\eta\kappa X^\eta,\qquad
 \mathsf V(W)\ll_\eta Y\kappa X^\eta,
\tag{189.A30}
\]

and hence

\[
 \sum_{v\ {\rm in\ a}\ J{\rm -block}}\mathsf V(W_v)
 \ll_\eta {Y\kappa uJ\over q}X^\eta.
\tag{189.A31}
\]

Relative to (189.A29), the missing factor is exactly
\(Y/(Pm)\). Because \(Pm<Y\) for \(P=Q\) on the Round-188 condition
\(Qm<Y\), this is a genuine loss. Primitive lifts \(m=1\) retain a
deficit \(Y/Q\), which is the full nonpolylogarithmic height factor up
to the already paid \(Q\).

Equivalently, before Abel summation define the actual discrepancy

\[
\begin{aligned}
 \mathcal D_{\kappa,u;m,q,a,\omega}^{\sigma}(J)
 :={}&
 \sum_{\substack{v\ {\rm literal},\ (u,v)=1\\
                  J\le j_q(a,v)<2J}}
 \left|\sum_h W_{\kappa,u,mq,v,\omega}^{\sigma}(h)
 e\!\left({\epsilon_\omega a\bar v h\over q}\right)\right|.
\end{aligned}
\tag{189.A32}
\]

A sufficient estimate is
\(\mathcal D(J)\ll_\eta Pm\kappa uX^\eta\). The available positive
bound is

\[
 \mathcal D(J)\ll_\eta {Y\kappa uJ\over q}X^\eta,
\tag{189.A33}
\]

whose excess over the sufficient scale is \(YJ/(Pmq)=YJ/(PU)\).
It is \(O(1)\) only when \(J\ll PU/Y\), namely at a nonempty paid
projective boundary; if that boundary lies below the integer lattice,
the first fast block already has a larger deficit. It can grow to a
full height factor. This is the exact first quantitative deficit, not
an assertion that the literal coefficient attains it.

## 3.5 Literal jumps block an assumed variation law

Changing \(h\) changes \(r=2\kappa(u/U)h\), the canonical anchors
modulo \(U\), both endpoint products, the Fejer factor, the
square-root phase, and every height-dependent profile and crossing.
The predicates \((U,h)=1\), squarefreeness, allocation coprimality,
the selected-prime residual mask, positivity, and zero extension can
jump. The accepted exact adjacent-site control already shows that
arithmetic support can disappear at one neighboring affine site while
the other endpoint survives. None of the permitted artifacts bounds
the number or signed size of the corresponding height jumps.

Consequently the displayed exponential may be periodic in \(h\bmod q\),
but \(W(h)\) is not proved periodic, translation-invariant, or of
variation \(O(Pm\kappa X^\eta)\). Möbius opening of squarefree or
coprimality predicates introduces divisor congruences but does not
factor the selector, profiles, endpoints, or phase. Positive
Cauchy, Parseval, large-sieve, Poisson, or alias energy returns
positive residue-bucket capacity and cannot replace (189.A29).

## 3.6 Centered exact-conductor and bad-slope controls

For a unit \(b\bmod q\), define

\[
 K_q(b)=\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}
 c_q(a)e(ab/q),\qquad
 K_q^\circ(b)=K_q(b)-{\mu(q)\over q}.
\tag{189.A34}
\]

Changing \(a\) to \(-a\), using
\(c_q(a)+c_q(-a)=2/q\), and the unit Ramanujan sum gives

\[
 K_q(b)+K_q(-b)={2\mu(q)\over q},\qquad
 K_q^\circ(-b)=-K_q^\circ(b).
\tag{189.A35}
\]

The exact-conductor partition also gives, for odd \(U>1\) and unit
\(b\bmod U\),

\[
 E_U(b)=\sum_{q\mid U}{q\over U}K_q(b).
\tag{189.A36}
\]

For \(U=p\) prime, the \(q=1\) mean and \(\mu(p)=-1\) yield

\[
 K_p^\circ(b)=E_p(b)=(-1)^{[b]_p}.
\tag{189.A37}
\]

For \(1\le h\le(p-1)/2\),
\([-2h]_p=p-2h\) is odd. Therefore every term in the prefix is
\(-1\), proving (189.A9). Centering is an exact identity, not a
height estimate. Reinstating a complete conductor in the Round-188
packet also requires accounting for the inherited ordinary-frequency
deletion \(m|a|_q\le Q\). The complete centered kernel already has the
prime bad slope, so centering alone supplies no prefix estimate; no
claim is made here that the truncated high-frequency kernel equals the
complete kernel. No uniform polylogarithmic prefix claim is available.

An abstract bounded array can dephase the height exponential,
the affine parity, and the square-root phase and attain carrier
capacity. This forbids a coefficient-uniform theorem from support and
boundedness alone. Such an array need not be the literal endpoint
coefficient, so it is neither a literal lower bound nor a disproof of
(189.A16).

# 4. First doubtful or unproved step

There is no doubtful step in the projective bijection, floor/cap count,
exact \(1/m\) cancellation, \(\tau_3\) ledger, or the target-safe
sector (189.A5). The first unproved step is the actual-coefficient
height-discrepancy relation (189.A29), or a genuinely joint
one-outer-real-part substitute strong enough to imply (189.A16).

The exact remaining aggregate is (189.A12) with
\(j_q(a,v)>T_Q(m,q;Y)\), both orientations, all \(h,v,t,a,m,q,U\),
and every literal field still joint. Its available positive capacity
retains the factor \(Y/(Qm)\) at the variation interface; primitive
\(m=1\) modes retain \(Y/Q\). No accepted theorem controls the
literal total variation, prefix discrepancy, or joint \((h,v)\)
transform. The exact centered-kernel survivor (189.A9) rules out
substituting a uniform polylogarithmic conductor-prefix assertion.

# 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| exact_round188_Qm_lt_Y_complement | PASS. Equation (189.A12) retains \(U=mq>4Q\), \(q>Q\), \(m|a|_q>Q\), and \(Qm<Y\) exactly. |
| literal_K185_27_30_35_carrier | PASS. Equations (189.A10)--(189.A13) retain the invariant carrier, canonical anchors, positive affine rays, both endpoint products, and literal amplitude. |
| single_outer_real_part_and_both_orientations | PASS. Equations (189.A8), (189.A15), and (189.A16) split the complex aggregate before positivity and keep one real part outside both orientations. |
| dual_frequency_j_abs_a_v_inverse_mod_q | PASS. Equation (189.A2) uses the inverse modulo \(q\); the orientation sign preserves least distance. |
| projective_residue_bijection_and_two_sided_count | PASS. Equation (189.A17) is a unit-class bijection and (189.A19) counts both least-residue sides without duplication. |
| q_divides_U_divides_u_v_interval_multiplicity | PASS. Each class occurs \(O(u/q)\) times, including interval endpoints, because \(q\mid u\); the total is \(O(uPm/Y)\). |
| per_v_O_kappa_affine_sites | PASS. Equation (189.A20) includes \(O(\kappa)\), the affine \(+1\), both orientations, and terminal truncation. |
| exact_cU_m_inverse_cq_normalization | PASS. Equation (189.A6) supplies exactly \(1/m\), which cancels the projective \(m\) before divisor summation. |
| slow_j_le_floor_U_over_Y_sector_and_exact_complement | PASS. The \(P=1\) baseline is proved; the exact \(P=Q\) floor-and-cap enlargement is also proved, with exact complement (189.A7). |
| full_factor_Y_before_positive_recombination | PASS for the slow sector. Equation (189.A20) cancels \(Y\) before the outer triangle. OPEN for the fast complement, with exact deficit (189.A31)--(189.A33). |
| kappa_u_m_q_divisor_power_ledger | PASS. Equation (189.A22) is exactly the ordered triple \(u=mqr\); no fourth divisor variable or missing \(m\) remains. |
| centered_exact_conductor_identity | PASS. Equations (189.A34)--(189.A37) give exact centering, antisymmetry, conductor inversion, and the prime survivor. |
| prime_bad_slope_height_prefix_survivor | PASS. Equation (189.A9) is the exact prefix \(-(p-1)/2\); it is quarantined from literal lower-mass claims. |
| selector_squarefree_coprime_deletions | PASS. They only delete in the slow positive count and remain inside \(W\) in the complement; no regularity is inferred. |
| profile_endpoint_phase_zero_extension | PASS. Every field stays in \(A\) and \(W\), including both zero-extension jumps used in total variation. |
| no_invented_height_BV_or_periodicity | PASS. The report stops at (189.A29), records the trivial variation (189.A30), and assumes no translation law. |
| no_positive_large_sieve_Poisson_alias_energy | PASS. No positive transform is used as cancellation; centered and adversarial self-return controls are explicit. |
| false_unsigned_and_adversarial_controls | PASS. The abstract dephased array is only a mechanism falsifier and is not called a literal coefficient. |
| original_t1_only_downstream_scope | PASS. Even (189.A16) would close only the exact original-\(t=1\) residual through accepted connectors. |
| no_in_round_owner_pivot | PASS. The sole owner remains the exact Round-188 \(Qm<Y\) complement. |
| exponent_quarantine | PASS. No \(t\ge2\), near-resonant, M1/M2 parent, endpoint, M9, bridge, theorem, or exponent claim changes. |

No numerical or symbolic experiment was needed. All controls above are
analytical; there is no numerical theorem evidence.

# 6. Dependencies and exact artifacts used

Only the regenerated task brief and its permitted context were used:

| Artifact | SHA-256 |
|---|---|
| rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/briefs/dual_height_frequency_signed_attack.md | f76ca63975a7871b762038551adff729a716ba2c25efdc71489586e763523812 |
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | 338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c |
| state/active_campaign.yml | 966a17240b3a8c62900a54af6c4c5df1b86065025387c7eefcad9863fb342c70 |
| strategy/round189_m1_t1_high_h_dual_height_frequency_strategy.md | 9daac6924dda273bc49ffd674122d7960af30460720c76705cf07c7e9d7212ad |
| proofs/kernels/m9_m1_hard_top_t1_high_h_imprimitive_lift_gcd_reduction.md | ca313d2ed11884bdb3ff237c51380de7aadd713a5dc01b565935fbdb8fe9744a |
| proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md | a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2 |
| proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md | 4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160 |
| rounds/codex-managed/m9-m1-t1-high-h-imprimitive-lift-gcd-gate/reports/imprimitive_lift_signed_attack.md | c77fe83e1c04042c221a1132121c50d8e745aaaca274d1284ec385e0bd3b8ca7 |
| rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reports/literal_height_fourier_attack.md | 4433de37846caa4c9ae0d51ba874221851a331e4a6af13043d4da0f0749ac298 |

The direct accepted mathematical dependencies are the Round-188
imprimitive-lift reduction, the Round-187 exact Fourier normalization
and centered-conductor identities, the Round-185 literal
multiplicity-one carrier, and elementary divisor bounds. No external
theorem, unlisted report, sibling Round-189 artifact, or hidden
coefficient regularity is used.

# 7. Recommended state effect

After independent normalization, power, literal-variation,
centered-kernel, and blind-post-unmask reviews, promote only the strict
dual-height projective sector. The required baseline
\(j_q(a,v)\le\lfloor U/Y\rfloor\) is proved, and the exact
fixed-polylogarithmic enlargement

\[
 j_q(a,v)\le
 \min\!\left\{{q-1\over2},
       \left\lfloor {Q\,U\over Y}\right\rfloor\right\}
\]

is also target-safe with every floor, cap, multiplicity, lift weight,
and divisor power explicit. Use the Round-189 exit label
strict_dual_height_resonance_sector.

Replace the Round-188 open complement only by the exact fast aggregate
\(\mathscr F_{Y,Q;Q}^{\sigma}\) and retain its one-sided estimate as
open. Record (189.A29) as the first sufficient actual-coefficient
variation relation, with deficit \(Y/(Qm)\), and record the prime
bad-slope prefix only as a falsifier of uniform centered-kernel height
bounds.

Make no status change to the complete high-height relation, complete
original-\(t=1\) residual, any original \(t\ge2\) or large-\(G\)
near-resonant component, the small-\(t\) owner, either M1 parent, GAR,
any M2 parent, endpoint uniformity, M9, either bridge, the Gauss-circle
target, or any exponent.
