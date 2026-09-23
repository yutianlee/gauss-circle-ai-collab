# 1. Result: strict imprimitive-lift sector and completion barrier

- Campaign: m9-m1-t1-high-h-imprimitive-lift-gcd-gate
- Round: 188
- Task: imprimitive_lift_signed_attack
- Role: discovery
- Starting graph SHA-256:
  be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff
- Evidence status: candidate evidence only; no proof-state edit

Fix the exact Round-187 high packet and put

\[
 Q=H_B=\lfloor(\log(2X))^B\rfloor,\qquad Q<Y<h\leq 2Y.
\]

For each retained Fourier mode put

\[
 m=(k,U),\qquad q=\frac{U}{m},\qquad k=ma.
\tag{188.A1}
\]

Here \(m\) is the Round-188 Fourier lift, not either endpoint factor in
the pre-tangent coordinates.  The map is unique, \((a,q)=1\), and

\[
 U=mq,\qquad
 c_{mq}(ma)=\frac1m c_q(a),\qquad
 e\!\left(\frac{\epsilon_\omega ma\bar v h}{mq}\right)
 =e\!\left(\frac{\epsilon_\omega a\bar v h}{q}\right),
 \qquad |ma|_{mq}=m|a|_q.
\tag{188.A2}
\]

The complete subpacket

\[
 U>4Q,\qquad q>Q,\qquad |k|_U>Q,\qquad Q(k,U)=Qm\geq Y
\tag{188.A3}
\]

has total absolute size

\[
 O_{B,\varepsilon}(L^2X^\varepsilon).
\tag{188.A4}
\]

This is an imprimitive-lift gain, not signed cancellation.  On one
dyadic height block there are \(O(YL)\), rather than \(O(UL)\),
literal-capacity atoms at fixed \((\kappa,u,U)\).  Exact conductor
\(q\) has coefficient mass

\[
 \frac1m\sum_{a\in\mathbb U(q)}|c_q(a)|
 \ll\frac{\log(2q)}m.
\tag{188.A5}
\]

Thus \(Qm\geq Y\) changes \(Y/m\) to at most \(Q\).  The exact
nested-label count is

\[
 \sum_{mq\mid u}1=\sum_{U\mid u}\tau(U)=\tau_3(u),
\tag{188.A6}
\]

so the global price is
\(QL^2\log^{O(1)}(2LQ)X^\varepsilon\), target-safe after the same
fixed-polylogarithmic epsilon rebudgeting used in Round 187.

The exact remaining packet is

\[
 U=mq>4Q,\qquad q>Q,\qquad m|a|_q>Q,\qquad Qm<Y.
\tag{188.A7}
\]

It stays under one real part over both orientations and every literal
field.  Its positive capacity remains
\(O_\varepsilon(YL^2X^\varepsilon)\).  The complete one-sided target
is not proved.

The attempted signed mechanisms stop at a sharp identity.  If
\(S=S_{t,\omega}\) and \(w=w_{t,\omega}\), then the plus determinant
is \(h=Sv-Uw\), the minus determinant is \(h=Uw-vS\), and \(U=mq\)
gives in both orientations

\[
 e\!\left(\frac{\epsilon_\omega a\bar v h}{q}\right)
 =e\!\left(\frac{aS}{q}\right)
 =e\!\left(\frac{aS_{0,\omega}}q\right).
\tag{188.A8}
\]

The last equality uses \(S=S_{0,\omega}+Ut\).  The lifted phase is
constant along the literal affine \(t\)-ray.  Determinant transposition
therefore creates no new oscillation.  Height completion and additive
reciprocity require an unproved discrepancy or variation theorem for
the actual deleted endpoint amplitude, while squarefree-sieve opening
does not factor the Round-184 selector or endpoint profiles.  This is a
mechanism no-go from the permitted hypotheses, not a disproof of the
literal target.

The proved candidate exit is
strict_high_h_imprimitive_lift_sector.

# 2. Exact statement and hypotheses

Retain exactly the Round-185 carrier (K185.27),
(K185.30)--(K185.35), and the Round-187 high packet
(K187.6)--(K187.7).  Thus

\[
 \kappa,g,h,U,v>0,\quad \kappa,g,U\ {\rm odd},\quad
 (gU,v)=1,\quad (U,h)=1,\quad 0<2\kappa gh<R_0,
\tag{188.A9}
\]

where \(R_0=\lceil L\rceil\).  Put \(u=gU\), and write

\[
 A_{\kappa,u,U,h,v,\omega}^{\sigma}
 :=\sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t),
 \qquad \mathfrak f=(\kappa,u/U,h,U,v).
\tag{188.A10}
\]

The coefficient \(B\) is not regularized.  It retains the residual
selector, squarefree and allocation-coprimality deletions, shell,
strict cone, height, profile, floor, star, half-weight, hard sample,
crossing, both endpoints, conjugation, Fejer factor, square-root phase,
sign, positivity predicates, and zero extension.

With all exact restrictions in (188.A9)--(188.A10) understood, the
Round-187 complex complement is

\[
\begin{aligned}
 \mathscr R_{Y,Q}^{\sigma}
 ={}&\sum_{\omega\in\{+,-\}}\sum_{\kappa,u}
 \sum_{\substack{U\mid u\\U>4Q}}
 \sum_{\substack{Y<h\leq2Y\\(U,h)=1\\
       0<2\kappa(u/U)h<R_0}}
 \sum_{\substack{v>0\\(u,v)=1}}
 \sum_{\substack{1\leq k<U\\q_U(k)>Q\\|k|_U>Q}}\\
 &\hspace{12mm}
 c_U(k)e\!\left(\frac{\epsilon_\omega k\bar v h}{U}\right)
 A_{\kappa,u,U,h,v,\omega}^{\sigma}.
\end{aligned}
\tag{188.A11}
\]

All sums are literal zero-extended sums.  Thus support consequences
such as \(u,v\asymp L/\kappa\) do not replace original predicates.
The inverse modulo \(U\) reduces to the inverse modulo every
\(q\mid U\).

For \(q>1\), let

\[
 \mathbb U(q)=(\mathbb Z/q\mathbb Z)^\times,\qquad
 c_q(a)=\frac{2}{q\{1+e(-a/q)\}}.
\tag{188.A12}
\]

Reparameterizing (188.A11) by (188.A1) gives exactly

\[
\begin{aligned}
 \mathscr R_{Y,Q}^{\sigma}
 ={}&\sum_{\omega,\kappa,u}
 \sum_{\substack{mq\mid u\\mq>4Q\\q>Q}}
 \sum_{\substack{Y<h\leq2Y\\(mq,h)=1\\
       0<2\kappa(u/(mq))h<R_0}}
 \sum_{\substack{v>0\\(u,v)=1}}\frac1m\\
 &\hspace{12mm}\times
 \sum_{\substack{a\in\mathbb U(q)\\m|a|_q>Q}}
 c_q(a)e\!\left(\frac{\epsilon_\omega a\bar v h}{q}\right)
 A_{\kappa,u,mq,h,v,\omega}^{\sigma}.
\end{aligned}
\tag{188.A13}
\]

Define \(\mathscr R_{Y,Q}^{\rm lift,\sigma}\) by adding \(Qm\geq Y\)
to (188.A13), and define
\(\mathscr C_{Y,Q}^{\rm prim,\sigma}\) by adding \(Qm<Y\).  The split
is disjoint and exhaustive:

\[
 \mathscr R_{Y,Q}^{\sigma}
 =\mathscr R_{Y,Q}^{\rm lift,\sigma}
  +\mathscr C_{Y,Q}^{\rm prim,\sigma}.
\tag{188.A14}
\]

This is a complex identity before any triangle inequality.  Therefore

\[
 \Re\mathscr R_{Y,Q}^{\sigma}
 =\Re\{\mathscr R_{Y,Q}^{\rm lift,\sigma}
       +\mathscr C_{Y,Q}^{\rm prim,\sigma}\},
\tag{188.A15}
\]

with one real part outside all remaining labels.  The assertion proved
here is

\[
 \boxed{|\mathscr R_{Y,Q}^{\rm lift,\sigma}|
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{188.A16}
\]

The still-open relation is

\[
 \boxed{\Re\mathscr C_{Y,Q}^{\rm prim,\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{188.A17}
\]

# 3. Proof or derivation

## 3.1 Lift coordinates and coefficient normalization

Take \(1\leq k<U\) and set \(m=(k,U)\).  Then \(q=U/m>1\),
\(a=k/m\) is a unit modulo \(q\), and \(k=ma\).  Conversely,
\(U=mq\) and \(a\in\mathbb U(q)\) determine one mode \(k=ma\pmod U\)
of exact conductor \(q\).  No condition \((m,q)=1\) is needed.

Directly,

\[
 c_{mq}(ma)
 =\frac{2}{mq\{1+e(-a/q)\}}=\frac1m c_q(a).
\tag{188.A18}
\]

The phase identity in (188.A2) follows immediately.  Multiplication by
\(m\) maps least distances modulo \(q\) to least distances modulo
\(mq\), proving \(|ma|_{mq}=m|a|_q\).  Thus every high-packet
condition in (188.A13) is exact; no mode is lost or duplicated.

For odd \(q\), put \(j=|2a-q|\).  Then

\[
 |c_q(a)|=\frac{1}{q\sin(\pi j/(2q))}\ll\frac1j.
\]

There are at most two residues for each \(j\), hence

\[
 \sum_{a\in\mathbb U(q)}|c_q(a)|\ll\log(2q).
\tag{188.A19}
\]

Restricting to \(m|a|_q>Q\) only decreases the mass.  This proves
(188.A5).

## 3.2 Dyadic atom count

Literal support gives

\[
 u,v\asymp\frac{L}{\kappa},\qquad
 h<\frac{R_0U}{2\kappa u}\ll U.
\tag{188.A20}
\]

Fix \((\kappa,u,U)\).  The interval \(Y<h\leq2Y\) contains \(O(Y)\)
integer heights, including a first or final truncated block.  For each
height there are \(O(L/\kappa)\) possible \(v\)'s.  The intersection
of one primitive affine row with all endpoint-size and hard-cone ranges
contains \(O(1+\kappa)=O(\kappa)\) live \(t\)-sites.  Both
orientations cost only an absolute factor.  The accepted endpoint bound
therefore gives

\[
\begin{aligned}
 &\sum_{\omega}
 \sum_{\substack{Y<h\leq2Y\\(U,h)=1\\
       0<2\kappa(u/U)h<R_0}}
 \sum_{\substack{v>0\\(u,v)=1}}
 \sum_{t\in I_{\mathfrak f,\omega}}
 |B_{\mathfrak f,\omega}^{\sigma}(t)|\\
 &\hspace{35mm}\ll_\varepsilon YLX^\varepsilon.
\end{aligned}
\tag{188.A21}
\]

More precisely, the count is \(O(\min(Y,U)L)\), and a nonempty block
forces \(Y\ll U\) by (188.A20).  Selectors, arithmetic masks, profiles,
endpoint restrictions, positivity predicates, and zero extensions only
delete or downweight atoms, so none creates a missing multiplicity.

## 3.3 Summing the strict lift sector

At fixed \((\kappa,u,U=mq)\), (188.A5) and (188.A21) give exact-\(q\)
absolute cost

\[
 \ll_\varepsilon\frac{YL\log(2q)}mX^\varepsilon.
\tag{188.A22}
\]

On \(Qm\geq Y\), this becomes

\[
 \ll_\varepsilon QL\log(2q)X^\varepsilon.
\tag{188.A23}
\]

For every positive integer \(u\),

\[
 \#\{(m,q):mq\mid u\}
 =\sum_{U\mid u}\tau(U)=\tau_3(u).
\tag{188.A24}
\]

The equality follows by writing the ordered triple \(u=mqr\).
Dropping the high-packet restrictions enlarges the majorant, so

\[
\begin{aligned}
 |\mathscr R_{Y,Q}^{\rm lift,\sigma}|
 &\ll_\varepsilon QLX^\varepsilon
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \tau_3(u)\log(2u)\\
 &\ll QL^2\log^{O(1)}(2LQ)X^\varepsilon.
\end{aligned}
\tag{188.A25}
\]

For completeness, the last estimate follows by swapping \(u\) and
\(\kappa\): fixed \(u\ll L\) permits \(O(L/u+1)\) values of
\(\kappa\), while writing \(u=abc\) gives

\[
 \sum_{u\leq Z}\tau_3(u)\ll Z\log^2(2Z),\qquad
 \sum_{u\leq Z}\frac{\tau_3(u)}u\ll\log^3(2Z).
\]

The extra \(\log(2u)\) changes only the fixed logarithmic power.  Since
\(Q\) is a fixed power of \(\log(2X)\), the accepted epsilon
rebudgeting turns (188.A25) into (188.A16).  No positive power of
\(Y\) is absorbed.

On \(Qm<Y\), the same calculation gives only

\[
 |\mathscr C_{Y,Q}^{\rm prim,\sigma}|
 \ll_\varepsilon YL^2\log^{O(1)}(2L)X^\varepsilon.
\tag{188.A26}
\]

The remaining positive deficit is the full factor \(Y\).

The threshold is sharp for this complete exact-conductor positive
ledger.  For every odd \(q>Q\), the units \(a=(q\pm1)/2\) satisfy

\[
 |c_q(a)|=\frac{1}{q\sin(\pi/(2q))}\geq\frac2\pi.
\tag{188.A27}
\]

They also obey \(m|a|_q=(U-m)/2>Q\) when \(U=mq>4Q\) and \(q>Q\).
Thus an unseparated exact-\(q\) block has coefficient mass at least a
constant times \(1/m\).  If \(Qm<Y\), the atom/mass ledger retains
local capacity of order \(YL/m>QL\).  Coefficient smallness alone
cannot extend the complete-conductor payment across this boundary.
This is capacity, not literal lower mass for the endpoint coefficient.

## 3.4 Determinant transposition is an exact self-return

For a plus-oriented site \(h=Sv-Uw\); for a minus-oriented site
\(h=Uw-vS\).  Since \(q\mid U\) and \((v,q)=1\),

\[
 \epsilon_+\bar v h\equiv S\pmod q,\qquad
 \epsilon_-\bar v h\equiv S\pmod q.
\tag{188.A28}
\]

This proves the first equality in (188.A8).  Moreover,
\(S=S_{0,\omega}+Ut\), so

\[
 e(aS/q)=e(aS_{0,\omega}/q)e(amt)
 =e(aS_{0,\omega}/q).
\tag{188.A29}
\]

The Fourier phase is constant on each affine ray.  It cannot combine
with the inherited \((-1)^t\) to make a geometric sum.  Summing all
primitive \(a\)'s reconstructs the exact-conductor kernel audited in
Round 187; it is not a determinant estimate.

## 3.5 Reciprocity, completion, and sieve opening

Because \((q,v)=1\), additive reciprocity gives exactly

\[
 e\!\left(\frac{\epsilon ah\bar v}{q}\right)
 =e\!\left(-\frac{\epsilon ah\bar q}{v}\right)
  e\!\left(\frac{\epsilon ah}{qv}\right),
\tag{188.A30}
\]

where \(\bar q\) is the inverse of \(q\pmod v\).  This changes the
displayed phase but supplies no estimate.  The literal amplitude changes
with \(v,h\), the canonical anchor, \(r=2\kappa(u/U)h\), both endpoint
products, the selector, profiles, and the square-root phase.

Although \(e(\epsilon a\bar v h/q)\) is periodic in \(h\pmod q\) for
fixed \(v\), the zero-extended amplitude is not known to be periodic or
of bounded variation.  Translation \(h\mapsto h+q\) need not preserve
\((U,h)=1\), changes the anchor modulo \(U=mq\), changes the Fejer
factor and both endpoints, and can cross
\(2\kappa(u/U)h<R_0\).  Abel summation would require an actual total
variation bound; none is available.

The formal identities

\[
 \mu^2(N)=\sum_{d^2\mid N}\mu(d),\qquad
 {\bf1}_{(r,s)=1}=\sum_{d\mid(r,s)}\mu(d)
\]

can open squarefree and coprimality masks, but do not factor the
residual selector \(\rho_N\), endpoint profile, crossing, or
zero-extension predicates.  The same discrepancy remains, with extra
divisor variables.  No literal reciprocity, completion, determinant,
or sieve gain follows from the permitted hypotheses.

## 3.6 Positive-norm and false-array controls

The complement still contains, for every odd \(U>4Q\), the primitive
modes

\[
 m=1,\qquad q=U,\qquad k=\frac{U\pm1}{2}.
\]

Indeed \(Qm=Q<Y\), and

\[
 |c_U(k)|=\frac{1}{U\sin(\pi/(2U))}\geq\frac2\pi.
\tag{188.A31}
\]

Thus the lift payment does not remove the constant Fourier
\(\ell^2\)-mass found in Round 187.  Positive Fourier, Poisson, alias,
height, conductor, or orientation energy returns a diagonal of capacity
\(O(YL^2X^\varepsilon)\).

On any finite retained carrier, an abstract bounded array can cancel
\((-1)^t\), the phase (188.A8), and the square-root phase, attaining
the positive atom capacity.  This refutes a coefficient-uniform
completion theorem based only on support and boundedness.  The array
need not be realizable by the actual Vaaler/\(\chi_4\) endpoint
coefficient, so this is neither literal lower mass nor a disproof of
(188.A17).

# 4. First doubtful or unproved step

For fixed admissible \((\kappa,u,m,q)\), define the actual-coefficient
conductor block

\[
\begin{aligned}
 \mathfrak D_{\kappa,u;m,q}^{\sigma}(Y)
 :={}&\sum_{\omega\in\{+,-\}}
 \sum_{\substack{Y<h\leq2Y\\(mq,h)=1\\
       0<2\kappa(u/(mq))h<R_0}}
 \sum_{\substack{v>0\\(u,v)=1}}
 \sum_{\substack{a\in\mathbb U(q)\\m|a|_q>Q}}\\
 &\hspace{12mm}\times
 c_q(a)e\!\left(\frac{\epsilon_\omega a\bar v h}{q}\right)
 A_{\kappa,u,mq,h,v,\omega}^{\sigma}.
\end{aligned}
\tag{188.A32}
\]

Every literal field and both orientations remain inside (188.A32).
The exact remaining aggregate is

\[
 \mathscr C_{Y,Q}^{\rm prim,\sigma}
 =\sum_{\kappa,u}
 \sum_{\substack{mq\mid u\\mq>4Q\\q>Q\\Qm<Y}}
 \frac1m\mathfrak D_{\kappa,u;m,q}^{\sigma}(Y).
\tag{188.A33}
\]

The proved information gives only

\[
 |\mathfrak D_{\kappa,u;m,q}^{\sigma}(Y)|
 \ll_\varepsilon YL\log(2q)X^\varepsilon.
\tag{188.A34}
\]

A sufficient actual-coefficient completion estimate would be

\[
 |\mathfrak D_{\kappa,u;m,q}^{\sigma}(Y)|
 \ll_\varepsilon L\log(2q)X^\varepsilon
\tag{188.A35}
\]

uniformly in the admissible labels.  Equations (188.A24) and
(188.A33) would then give an absolute \(O(L^2X^\varepsilon)\) bound
for the complement.  The exact target asks only the weaker joint
relation

\[
 \boxed{
 \Re\sum_{\kappa,u}
 \sum_{\substack{mq\mid u\\mq>4Q\\q>Q\\Qm<Y}}
 \frac1m\mathfrak D_{\kappa,u;m,q}^{\sigma}(Y)
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{188.A36}
\]

The first unproved step in every attempted reciprocity or completion
argument is the replacement of (188.A34) by a discrepancy with the
full factor \(Y\) removed, such as (188.A35), or a genuinely joint
substitute sufficient for (188.A36).  No periodicity, bounded
variation, translation law, orientation equality, or squarefree-sieve
estimate for the actual amplitude has been proved.  Equations
(188.A8), (188.A30), and the Möbius identities are algebraic
reparametrizations only.

# 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| exact_round187_high_packet | PASS.  The three starting conditions are retained in (188.A11)--(188.A13). |
| literal_K185_27_30_35_carrier | PASS.  The exact carrier, anchors, positive rays, endpoints, Fejer factor, and phase remain in (188.A9)--(188.A10). |
| single_outer_real_part_and_both_orientations | PASS.  The split is a complex identity; only the strict sector is absoluted.  The complement retains one outer real part in (188.A36). |
| unique_U_mq_k_ma_lift_coordinates | PASS.  Section 3.1 proves the bijection without assuming \((m,q)=1\). |
| exact_cU_m_inverse_cq_normalization | PASS.  Equation (188.A18) gives the exact \(1/m\), with exact phase and least-distance identities. |
| dyadic_fixed_kappa_u_U_atom_count | PASS.  Equation (188.A21) proves \(O(YL)\), including terminal truncation and the affine \(+1\). |
| triple_divisor_convolution_power | PASS.  Equation (188.A24) gives exactly \(\tau_3(u)\). |
| Qm_ge_Y_sector_and_exact_complement | PASS.  Equations (188.A14)--(188.A17) are disjoint, exhaustive, and retain every high-packet condition. |
| full_factor_Y_before_positive_recombination | PASS for the strict sector; OPEN for the target.  The factor is removed by \(1/m\leq Q/Y\) before positivity.  The complement retains (188.A26). |
| selector_squarefree_coprime_deletions | PASS.  They remain literal; they reduce counts but license no translation or sieve-completion law. |
| profile_endpoint_phase_zero_extension | PASS.  Every field stays inside \(B\) and \(A\); no smoothing or endpoint deletion is made. |
| no_invented_height_or_residue_variation | PASS.  Section 3.5 isolates the missing variation/discrepancy input instead of assuming it. |
| no_positive_large_sieve_Poisson_alias_energy | PASS.  No positive norm is used on the complement; (188.A31) records the surviving spectral mass. |
| false_unsigned_and_adversarial_controls | PASS.  A dephased bounded array attains capacity but is quarantined from literal lower-mass claims. |
| original_t1_only_downstream_scope | PASS.  Even (188.A36) would close only the exact original-\(t=1\) residual through prior connectors; all original \(t\geq2\) and large-\(G\) complements remain open. |
| exponent_quarantine | PASS.  No complete M1 parent, GAR, M9--M1, M2 owner, endpoint owner, M9, bridge, theorem, or exponent changes. |

No numerical experiment was needed.  The report is entirely analytical;
there is no numerical theorem evidence.

# 6. Dependencies and exact artifacts used

Only the task brief and its explicitly permitted context were used:

1. protocol.md;
2. state/proof_obligations.yml, restricted to the relevant M9,
   M9--M1, Round-185, and Round-187 nodes;
3. state/active_campaign.yml;
4. strategy/round188_m1_t1_high_h_imprimitive_lift_gcd_strategy.md;
5. proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md;
6. proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md;
7. rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reports/literal_height_fourier_attack.md;
8. rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reports/deletion_resonance_capacity_audit.md;
9. rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/synthesis.md; and
10. rounds/codex-managed/m9-m1-t1-high-h-imprimitive-lift-gcd-gate/briefs/imprimitive_lift_signed_attack.md.

No sibling Round-188 report, unlisted artifact, web theorem, or
external result was used.

# 7. Recommended state effect

After independent normalization, power, literal-scope, and blind
reviews, promote only the strict sector (188.A3)--(188.A16) as a proved
subordinate reduction, and replace the Round-187 complement by the exact
primitive/moderately-imprimitive packet (188.A7),
(188.A32)--(188.A36).

Retain the complete high-height relation, complete original-\(t=1\)
residual, and every downstream owner as open.  Record (188.A8) as an
exact determinant self-return and the first missing actual-coefficient
discrepancy (188.A36), with the full factor-\(Y\) deficit.  Reject any
claim that additive reciprocity alone, height periodicity of the
displayed exponential, determinant transposition, Möbius opening, raw
orientation pairing, or a positive transform norm proves the
complement.

Recommended Round-188 exit label:
strict_high_h_imprimitive_lift_sector.
