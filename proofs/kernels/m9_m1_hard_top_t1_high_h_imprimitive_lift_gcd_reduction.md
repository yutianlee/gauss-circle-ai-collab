# Hard-M1 \(t=1\) high-height imprimitive-lift gcd reduction

- Campaign: m9-m1-t1-high-h-imprimitive-lift-gcd-gate
- Round: 188
- Starting graph SHA-256:
  be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff
- Discovery report SHA-256:
  c77fe83e1c04042c221a1132121c50d8e745aaaca274d1284ec385e0bd3b8ca7
- Hostile report SHA-256:
  1f27281d91fd7290f548e3c1dfa696f2a6a9b82e184f8bc878747a29f1a3dce1
- Blind report SHA-256:
  a524bf81774ac9cdcdd0c423851320da6dc037b8feee5decba541952c996e3b6
- Formal candidate SHA-256:
  c6f0939ffe5153d38ded0205ec4ee0f211f1de711ea81068194082dd66122f65
- Evidence status: durable proof kernel after independent normalization,
  power, literal-scope, and blind-post-unmask review
- Numerical theorem evidence: none

## Accepted statement

Fix real \(X\ge2\), one nonempty literal middle or lower residual
hard-M1 shell \(L\ge2\), \(\sigma\in\{+1,-1\}\), and fixed \(B>0\).
The inherited nonzero hard-top support has

\[
 L\ll X^{1/4};
\tag{188.K1}
\]

this is a hash-bound accepted support connector, not an implicit
two-parameter assumption. Indeed the proved hard-top transform has

\[
 y=\lfloor\sqrt X\rfloor,\qquad
 H=\lfloor yX^{-1/4}\rfloor,\qquad 1\le h\le H,
\]

while the literal dyadic frequency shell has \(h\asymp L\) and is
zero-extended off that range. Hence
\(L\ll H+1\ll X^{1/4}\). The extraction and its accepted provenance are
recorded in
reviews/conductor_inherited_hard_m1_shell_support_connector.md.
Off that range the literal zero extension makes the aggregate empty.
Put

\[
 R_0=\lceil L\rceil,\qquad
 Q=H_B=\lfloor(\log(2X))^B\rfloor.
\tag{188.K2}
\]

Fix a nonempty dyadic integer-height block \(Y<h\le2Y\) with \(Y>Q\).
Use exactly the accepted Round-185 primitive carrier and amplitudes
(K185.27), (K185.30)--(K185.35), and the exact Round-187 high packet
(K187.6)--(K187.7). Thus every retained Fourier mode obeys

\[
 U>4Q,\qquad q_U(k)=\frac{U}{(k,U)}>Q,\qquad |k|_U>Q,
\tag{188.K3}
\]

and every selector, squarefree and allocation-coprimality deletion,
profile, floor, star, half-weight, hard sample, crossing, endpoint,
conjugation, Fejer factor, square-root phase, sign, positivity
predicate, orientation, and zero extension remains literal.

For every mode in (188.K3), put

\[
 m=(k,U),\qquad q=\frac Um,\qquad a=\frac km.
\tag{188.K4}
\]

Then the coordinates are unique,

\[
 U=mq,\qquad k=ma,\qquad 1\le a<q,\qquad(a,q)=1,
\tag{188.K5}
\]

and exactly

\[
 c_U(k)=\frac1m c_q(a),\qquad
 e\!\left(\frac{\epsilon_\omega k\bar vh}{U}\right)
 =e\!\left(\frac{\epsilon_\omega a\bar vh}{q}\right),
 \qquad |k|_U=m|a|_q.
\tag{188.K6}
\]

Define \(\mathscr I_{Y,Q}^{\sigma}\) by adding

\[
 Qm\ge Y
\tag{188.K7}
\]

to the exact complex aggregate \(\mathscr R_{Y,Q}^{\sigma}\) of
(K187.7), and define \(\mathscr C_{Y,Q}^{\sigma}\) by adding \(Qm<Y\)
instead. Then, before any triangle inequality,

\[
 \boxed{\mathscr R_{Y,Q}^{\sigma}
 =\mathscr I_{Y,Q}^{\sigma}+\mathscr C_{Y,Q}^{\sigma}.}
\tag{188.K8}
\]

The complete strict imprimitive-lift packet is absolutely target-safe:

\[
 \boxed{|\mathscr I_{Y,Q}^{\sigma}|
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{188.K9}
\]

The exact complement has lift coordinates

\[
 \boxed{
 U=mq>4Q,\qquad q>Q,\qquad m|a|_q>Q,\qquad Qm<Y,}
\tag{188.K10}
\]

with all original carrier restrictions still imposed. It stays under
the same single outer real part over both orientations and every literal
label. The available positive estimate is only

\[
 |\mathscr C_{Y,Q}^{\sigma}|
 \ll_\varepsilon YL^2X^\varepsilon.
\tag{188.K11}
\]

Consequently the complete Round-187 high-height relation is reduced,
up to (188.K9), to the still-open one-sided estimate

\[
 \boxed{\Re\mathscr C_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{188.K12}
\]

No full high-height relation, complete original-\(t=1\) residual,
small-\(t\) owner, parent, bridge, theorem, or exponent is asserted.

## Proof of the strict packet

### Unique lift and exact coefficient mass

For \(1\le k<U\), (188.K4) gives a proper divisor \(m\mid U\).
Division by \(m\) yields (188.K5). Conversely, \(U=mq\) and
\(a\in(\mathbb Z/q\mathbb Z)^\times\) determine exactly one mode
\(k=ma\), so no mode is lost or duplicated. Direct substitution gives

\[
 c_{mq}(ma)
 =\frac{2}{mq\{1+e(-a/q)\}}=\frac1m c_q(a).
\tag{188.K13}
\]

Because \((v,U)=1\) and \(q\mid U\), the inverse of \(v\bmod U\)
reduces to the inverse of \(v\bmod q\), proving the phase identity in
(188.K6). Multiplication by \(m\) scales least residue distance, giving
\(|ma|_{mq}=m|a|_q\).

For odd \(q\),

\[
 |c_q(a)|=\frac1{q|\cos(\pi a/q)|}.
\]

Grouping residues by their odd distance from \(q/2\), and enlarging
from units to all residues, gives

\[
 \sum_{a\in(\mathbb Z/q\mathbb Z)^\times}|c_q(a)|
 \ll\log(2q).
\tag{188.K14}
\]

Thus exact conductor \(q\) at lift \(m\) has coefficient mass
\(O(m^{-1}\log(2q))\). The condition \(m|a|_q>Q\) only decreases this
positive mass.

### Dyadic atom count

Put \(u=gU\). Literal support gives

\[
 u,v\asymp\frac L\kappa,\qquad h\ll U.
\tag{188.K15}
\]

At fixed \((\kappa,u,U,h)\), \(g=u/U\) is fixed, there are
\(O(L/\kappa)\) possible \(v\)'s, and the accepted endpoint geometry
has \(O(1+\kappa)=O(\kappa)\) live affine sites per row. Both
orientations cost only an absolute factor. Therefore

\[
 \sum_{\substack{Y<h\le2Y\\v,\omega,t}}
 |B_{\mathfrak f,\omega}^{\sigma}(t)|
 \ll_\eta YLX^\eta
\tag{188.K16}
\]

at fixed \((\kappa,u,U)\). The terminal Fejer cutoff, coprimalities,
selectors, arithmetic masks, profiles, endpoints, phases, and zero
extensions only delete or downweight atoms. Equation (188.K16) is an
upper-capacity count, not a density or nonemptiness assertion.

### Divisor and power ledger

Multiplying (188.K16) by (188.K14), the exact
\((\kappa,u,m,q)\) cost is

\[
 \ll_\eta \frac{YL\log(2q)}mX^\eta.
\tag{188.K17}
\]

On (188.K7), \(Y/m\le Q\). Since \(U=mq\mid u\),

\[
 \sum_{U\mid u}\sum_{q\mid U}1
 =\sum_{mq\mid u}1
 =\tau_3(u),
\tag{188.K18}
\]

where \(\tau_3\) counts ordered factorizations into three positive
integers. Hence elementary triple-divisor summation gives

\[
\begin{aligned}
 |\mathscr I_{Y,Q}^{\sigma}|
 &\ll_\eta QLX^\eta
 \sum_{\kappa\ll L}
 \sum_{u\asymp L/\kappa}
 \tau_3(u)\log(2u)\\
 &\ll_\eta
 QL^2\log^{O(1)}(2LQ)X^\eta.
\end{aligned}
\tag{188.K19}
\]

Choose the endpoint allowance \(\eta<\varepsilon\). By (188.K1) and
fixed \(B\), \(Q\log^{O(1)}(2LQ)=X^{o(1)}\), so (188.K19) proves
(188.K9). No positive power of \(Y\) is absorbed: the factor \(Y\) is
removed only through \(1/m\le Q/Y\) before positive recombination.

Replacing (188.K7) by \(Qm<Y\) gives the exact complementary identity
(188.K8) and only the positive estimate (188.K11). Every condition in
(188.K3) and (188.K10) remains explicit.

## Determinant, completion, and primitive-lift controls

Let \(S=S_{t,\omega}\) and \(w=w_{t,\omega}\). The primitive equations
are

\[
 h=Sv-Uw\quad(\omega=+),\qquad
 h=Uw-vS\quad(\omega=-).
\tag{188.K20}
\]

Using \(\epsilon_+=1\), \(\epsilon_-=-1\), \(q\mid U\), and
\((v,q)=1\), both orientations satisfy

\[
 \epsilon_\omega\bar vh\equiv S\pmod q.
\]

Since \(S=S_{0,\omega}+Ut\), the lifted phase is exactly

\[
 e(\epsilon_\omega a\bar vh/q)
 =e(aS/q)=e(aS_{0,\omega}/q).
\tag{188.K21}
\]

It is constant along the affine \(t\)-ray and supplies no geometric
cancellation with \((-1)^t\). Determinant transposition therefore
returns to the same literal row unless a new endpoint relation is
proved.

For \(v>1\), let \(\bar q_v\) denote the inverse of \(q\bmod v\).
For \(v=1\), use the unique residue convention \(\bar q_1=0\).
Additive reciprocity is then exact:

\[
 e(\epsilon ah\bar v_q/q)
 =e(-\epsilon ah\bar q_v/v)e(\epsilon ah/(qv)),
\tag{188.K22}
\]

where the \(v=1\) identity is read as
\(e(\epsilon ah/q)=1\cdot e(\epsilon ah/q)\).
It does not make the actual amplitude periodic or bounded-variation
in \(h,v,q\), or \(a\). Height completion gives the full Fourier
transform of a zero-extended literal sequence; triangle, Cauchy,
Parseval, or a positive large-sieve placement returns positive
residue-bucket capacity. Möbius opening of squarefreeness or
coprimality does not factor the moving residual selector, endpoint
profiles, or square-root phase.

The complement (188.K10) contains every primitive lift \(m=1\), since
\(Y>Q\). For odd prime \(U=q>4Q\), the two modes

\[
 a=\frac{q\pm1}{2}
\]

remain in the complement and satisfy

\[
 |c_q(a)|=\frac1{q\sin(\pi/(2q))}\ge\frac2\pi.
\tag{188.K23}
\]

Their combined squared mass is at least \(8/\pi^2\). Thus the strict
lift payment does not remove the Round-187 primitive high-frequency
energy. Positive completion, Poisson, conductor, alias, orientation, or
height energy gives no automatic factor \(Y\).

An abstract bounded array can dephase the high kernel, \((-1)^t\), and
the square-root phase and attain the carrier capacity. This falsifies
coefficient-uniform completion based only on support and boundedness.
It is not the literal endpoint coefficient and proves neither physical
lower mass nor failure of (188.K12).

The first missing mathematical input is therefore a jointly signed
actual-coefficient discrepancy estimate for (188.K12), gaining the full
factor \(Y\) before any positive recombination. Equations
(188.K21)--(188.K22), exact completion, determinant transposition, and
sieve opening are algebraic identities, not that estimate.

## Exact scope and dependencies

The proved content is only:

1. the unique lift coordinates and exact normalization
   (188.K4)--(188.K6);
2. the exact complex split (188.K8);
3. the absolute target-safe strict sector (188.K9);
4. the exact primitive or moderately imprimitive complement
   (188.K10)--(188.K12); and
5. the determinant/completion/positive-energy mechanism controls.

Even a proof of (188.K12) would close only the exact original-\(t=1\)
residual through the accepted Round-184/185/187 connectors. Every
original \(t\ge2\) small-\(G\) incidence, the large-\(G\)
near-resonant complement, the complete hard and smooth M1 parents, GAR,
every M2 parent, endpoint uniformity, M9, both bridges, the quarter
target, and every exponent claim remain open.

Direct accepted dependencies are:

- M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction;
- Divisor-bound-elementary.

The inherited shell support used in (188.K1) is transitive through the
accepted Round-185/187 chain and is made explicit by the hash-bound
connector above; its authoritative source node is
M9-M1-top-endpoint-transform. No external theorem is used.

## Evidence and diagnostic

The candidate reconciles:

- reports/imprimitive_lift_signed_attack.md;
- reports/lift_power_completion_hostile_audit.md;
- reports/blind_lift_gcd_rederivation.md;
- reviews/conductor_round188_report_reconciliation.md;
- reviews/conductor_inherited_hard_m1_shell_support_connector.md.

The independent review chain is:

- reviews/lift_normalization_and_multiplicity_seam_review.md, SHA-256
  6c29cf14987029a3279c595ca38f051a29d5f7efbfb63ebe89e8b2e7ac56b899;
- reviews/lift_normalization_and_multiplicity_post_repair_verification.md,
  SHA-256
  097226ab0d8acf98f65502b3163f1d5c5a384289725aa06379d5e6a27be0401e;
- reviews/lift_power_literal_scope_completion_seam_review.md, SHA-256
  2ec3c9c0d96303400348fd3b2682e72dac4eeb955b0e558ab2f4dbad91548a01;
- reviews/blind_post_unmask_owner_scope_seam_review.md, SHA-256
  80c4359a5f5d1a37fa2de60262de25325cfa9f3e4b45c01ff1489eda0fadd2a1;
- reviews/blind_post_unmask_owner_scope_post_repair_verification.md,
  SHA-256
  79e0be1854c9e61f643081a42e300a766f1829826ecf97ac6ac7dd313e051c26.

The blind report's logarithmic caveat is resolved only by making the
already inherited support (188.K1) explicit. Its stronger complete
primitive-frequency identity is not needed for (188.K9) and is not
used as theorem evidence here.

The bounded control artifacts are:

- controls/lift_partition_exact_check.wls, SHA-256
  7bad1b482654e69325feaf844d359d1643a3245c8e990742ecfc83141e995b99;
- controls/conductor_round188_wolfram_lift_partition_check.md, SHA-256
  4d6173c31bfe63e158f5d07d90488808e65d6b81a58d5e428ed1e01ae69bcb42.

They check finite lift, phase, distance, partition, divisor, and
near-half identities only. They are diagnostic, not asymptotic theorem
evidence.
