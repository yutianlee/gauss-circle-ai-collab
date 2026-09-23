# Literal primitive-conductor parity attack

## 1. Result: exact parity/trace lemma and orientation-defect no-go

The exact-conductor projector proposed in (179.S4), its unit-residue
sign law (179.S5), and the two-orientation decomposition (179.S7) are
correct with the (d=1) term and the factor (q/u_0) retained.  For the
complete high-conductor packet (q>Q_B), the resulting primitive trace is
target-safe after both divisor sums:

\[
 \mathcal T_{\kappa,u}
 :=\sum_{u_0\mid u}\sum_{\substack{q\mid u_0\\q>Q_B}}
 {2\mu(q)\over u_0}\sum_{b\in U(q)}B^-_{q,b}
 \ll_{B,\delta,\gamma,\varepsilon}L X^\varepsilon .
 \tag{179.L1}
\]

Consequently (177.K34) is equivalent, up to the proved error (179.L1),
to the same target bound for the complete literal orientation defect

\[
 \mathcal D_{\kappa,u}
 =\sum_{u_0\mid u}\sum_{\substack{q\mid u_0\\q>Q_B}}
 {q\over u_0}\sum_{b\in U(q)}K_q(b)
       \bigl(B^+_{q,b}-B^-_{q,b}\bigr).
 \tag{179.L2}
\]

No target bound for (179.L2) is proved.  The first exact obstruction is
that the product-preserving exchange of the two literal orientations is
not an involution of a fixed-((\kappa,u)) K34 block: it sends the outer
label (u) to the internal label (v).  It has no high-conductor fixed
point, since (u=v) and ((u,v)=1) force (u=v=1), hence (q=1).
Moreover, after allowing this label exchange, it replaces both selected
divisors by their complementary factors, which the literal selector
kills by zero extension (below the upper near-square divisor window in
the odd branch, and even in the even branch).

The primitive projector itself supplies no substitute contraction.  On
the admissible arbitrary-bucket false control (u_0=q=p), with (p) an
odd prime,

\[
 K_p(b)=(-1)^b-{1\over p},\qquad
 \sum_{b\in U(p)}|K_p(b)|=p-1.
 \tag{179.L3}
\]

Thus its \(\ell^\infty\)-to-scalar norm has full conductor size.  This
gives the authorized exit
`primitive_conductor_orientation_defect_capacity_or_self_return_no_go`.
It is a route-scoped no-go, not literal lower mass and not a disproof of
(177.K34).

## 2. Exact statement and hypotheses

Assume (177.K1)--(177.K3): (J=\sqrt X),
(1\ll L\ll H\le J^{1/2}), (R_0=\lceil L\rceil),
(R_{\log}=\min\{R_0-1,\lfloor(\log X)^{100}\rfloor\}), fixed
(0<\delta<1/2), (0<\gamma<1), and the complete literal low-cross-gcd
packet

\[
 R_{\log}<2\kappa n<R_0,\qquad \kappa<\delta L,
 \qquad (u,n)<\gamma L.
\]

Here (\kappa,u) are odd, (u\asymp L/\kappa), and the exact gcd fold is

\[
 g=(u,n),\qquad u=gu_0,\qquad n=gn_0,
 \qquad (n_0,u_0)=1.
 \tag{179.L4}
\]

For a fixed (u_0\mid u), put

\[
 A^\pm_{v,n_0,t}
 :=\Lambda^\pm_{\kappa,u,v,gn_0}(t)
 e\!\left(\Psi^\pm_{\kappa,u,v,gn_0}(t)+{t\over2}\right).
 \tag{179.L5}
\]

This notation does not erase any field: (A^\pm) is zero unless the
corresponding literal atom satisfies the squarefree and coprimality
conditions, the canonical selected/no-pair field, both parity branches,
the Fejer factor, determinant and original-gcd ranges, the two
opposing-displacement inequalities (s_t,w_t\ge1), profiles, floors,
stars, hard values, endpoint conjugations, and all other zero-extended
support conditions in (176.K18) and (176.K20).  Also ((v,u)=1).

For every divisor (q\mid u_0), define

\[
 b(v,n_0)=\bar v n_0\pmod q,
\]

and the literal buckets

\[
 B^\pm_{q,b}
 :=\sum_{\substack{v,n_0,t\\
          \bar v n_0\equiv b\ (q)}}A^\pm_{v,n_0,t}.
 \tag{179.L6}
\]

Because (q\mid u_0\mid u), ((v,u)=1), and ((n_0,u_0)=1), every
occupied (b) lies in (U(q)).  All moduli (u,u_0,q) are odd.  For

\[
 c_q(a)={2\over q\{1+e(-a/q)\}},\qquad
 K_q(b)=\sum_{a\in U(q)}c_q(a)e(ab/q),
 \tag{179.L7}
\]

the exact-(q) block is

\[
 \mathcal C_{u_0,q}
 ={q\over u_0}\sum_{b\in U(q)}
 \{K_q(b)B^+_{q,b}+K_q(-b)B^-_{q,b}\}.
 \tag{179.L8}
\]

The conclusions are:

1. for every (b\in U(q)),

   \[
   K_q(b)={1\over q}\sum_{d\mid q}\mu(q/d)dE_d(b),
   \qquad E_d(b)=(-1)^{[b]_d},\quad E_1=1;
   \tag{179.L9}
   \]

2. (K_q(b)+K_q(-b)=2\mu(q)/q), with the entire right side coming
   from (d=1);
3. (179.L8) is exactly the sum of (179.L2) at ((u_0,q)) and the trace
   term in (179.L1);
4. the full high-(q) trace obeys (179.L1);
5. the natural same-product orientation exchange is neither local in
   (u) nor selector-preserving; and
6. the arbitrary-bucket operator already has the full (Lq) capacity
   in the prime control (179.L3).

The low packet (q\le Q_B=(\log(2X))^B) is excluded throughout.  The
(d=1) term in (179.L9) is an inclusion-exclusion term inside each
high exact-conductor projector; it is not a second occurrence of the
physical (q=1) alias.

## 3. Proof or derivation

### 3.1 Exact-conductor Mobius projector

Fourier inversion for the odd sawtooth gives

\[
 E_d(b)=\sum_{k\bmod d}c_d(k)e(kb/d).
 \tag{179.L10}
\]

Insert

\[
 \mathbf1_{(a,q)=1}=\sum_{r\mid(a,q)}\mu(r)
\]

into (179.L7), and write (d=q/r).  Then

\[
\begin{aligned}
 K_q(b)
 &=\sum_{r\mid q}\mu(r)
   \sum_{\substack{a\bmod q\\r\mid a}}c_q(a)e(ab/q)\\
 &=\sum_{d\mid q}\mu(q/d)
   \sum_{k\bmod d}c_q((q/d)k)e(kb/d).
\end{aligned}
\tag{179.L11}
\]

Directly from the definition of (c_m), including (d=1,k=0),

\[
 c_q((q/d)k)={d\over q}c_d(k).
 \tag{179.L12}
\]

Equations (179.L10)--(179.L12) prove (179.L9).  In particular the
(d=1) summand is exactly (\mu(q)/q), not zero.

If (b\in U(q)), then (b\in U(d)) for every (d\mid q).  For odd
(d>1), (1\le[b]_d\le d-1) and

\[
 [-b]_d=d-[b]_d,\qquad E_d(-b)=-E_d(b).
 \tag{179.L13}
\]

For (d=1), both signs give (E_1=1).  Adding (179.L9) at (b) and
(-b) therefore cancels every (d>1) term and gives

\[
 K_q(b)+K_q(-b)={2\mu(q)\over q}.
 \tag{179.L14}
\]

### 3.2 The (q/u_0) normalization and literal bucket identity

For an exact-conductor alias

\[
 \ell=(u_0/q)a,\qquad (a,q)=1,
\]

the accepted gcd fold gives

\[
 c_{u_0}(\ell)={q\over u_0}c_q(a),
 \tag{179.L15}
\]

while the two conductor phases in (177.K15) are (e(ab/q)) and
(e(-ab/q)).  Keeping all other factors inside (179.L5), summing first
over (a\in U(q)), and only then bucketing by (b), gives (179.L8)
without an absolute value or a completion error.  Substituting

\[
 K_q(-b)={2\mu(q)\over q}-K_q(b)
\]

into (179.L8) gives the exact identity

\[
 \mathcal C_{u_0,q}
 ={q\over u_0}\sum_{b\in U(q)}K_q(b)
       (B^+_{q,b}-B^-_{q,b})
 +{2\mu(q)\over u_0}\sum_{b\in U(q)}B^-_{q,b}.
 \tag{179.L16}
\]

This rederives every factor in (179.S6)--(179.S7).  In particular, the
outer (q/u_0) cancels the (1/q) in the parity trace and leaves
(2\mu(q)/u_0), not (2\mu(q)/q) and not (2\mu(q)).

### 3.3 Target-safe summation of the primitive trace

At fixed ((\kappa,u,u_0)), the buckets for a given (q\mid u_0)
partition the same minus-orientation atoms, so

\[
 \sum_{b\in U(q)}B^-_{q,b}
 =\sum_{v,n_0,t}A^-_{v,n_0,t}.
 \tag{179.L17}
\]

The accepted literal count is (O(u_0L)), and
(|A^-_{v,n_0,t}|\ll1).  Hence, restricting from the outset to
(q>Q_B),

\[
\begin{aligned}
 |\mathcal T_{\kappa,u}|
 &\le \sum_{u_0\mid u}{2\over u_0}
       O(u_0L)\sum_{q\mid u_0}|\mu(q)|\\
 &\ll L\sum_{u_0\mid u}\tau(u_0)
 \le L\tau(u)^2
 \ll_\varepsilon L X^\varepsilon.
\end{aligned}
\tag{179.L18}
\]

Here (u\ll L\le X^{1/4}), and the last step is the standard divisor
bound.  Thus both divisor summations are safe.  No low-(q) alias is
reintroduced.

### 3.4 Physical lifts and the restored capacity

Put (h=u_0/q), so (u=ghq).  For one ordered unit residue pair
((v,n_0)\pmod q), the physical ranges contain respectively
(O(gh)) (v)-lifts and (O(h)) (n_0)-lifts, and the primitive fibre
contains (O(\kappa)) sites.  Its lift multiplicity is

\[
 O(\kappa gh^2)=O(Lh/q),
 \tag{179.L19}
\]

using (\kappa u\asymp L).  A fixed inverse-product residue
(b=\bar v n_0\pmod q) has (O(q)) ordered unit pairs, so

\[
 \#\{z:b(z)=b\}\ll Lh={Lu_0\over q}.
 \tag{179.L20}
\]

All literal selectors can only delete these atoms.  Since

\[
 |K_q(b)|\le\sum_{a\in U(q)}|c_q(a)|\ll\log(2q),
\]

triangle inequality in the defect gives the exact restored stop scale

\[
 |\mathcal D_{u_0,q}|
 \ll {q\over u_0}\,q\log(2q)\,{Lu_0\over q}
 \ll Lq\log(2q).
 \tag{179.L21}
\]

One conductor square-root saving in this ledger leaves
(L\sqrt q\log(2q)).  Positively summing exact conductors and then gcd
strata returns, up to divisor factors absorbed by (X^\varepsilon),

\[
 \sum_{q\mid u_0}Lq\ll Lu_0X^\varepsilon,
 \qquad
 \sum_{u_0\mid u}Lu_0\ll LuX^\varepsilon.
 \tag{179.L22}
\]

Thus completion modulo (q) cannot replace the physical ranges by one
primitive period: the (L\sqrt q), (Lq), (Lu_0), and (Lu) stop
tests all remain above the local (L)-target.

### 3.5 Arbitrary-bucket false control

Let (u_0=q=p>Q_B) be an odd prime.  The divisors (1,p) in
(179.L9) give, for (1\le b\le p-1),

\[
 K_p(b)=E_p(b)-{1\over p}=(-1)^b-{1\over p}.
 \tag{179.L23}
\]

There are equally many odd and even units, whence (179.L3).  With
(M=L/2), take the artificial arrays

\[
 B^+_{p,b}=M\,\operatorname{sgn}K_p(b),\qquad
 B^-_{p,b}=-M\,\operatorname{sgn}K_p(b).
 \tag{179.L24}
\]

They obey the physical bucket cap (O(Lu_0/q)=O(L)), and
(\sum_bB^+_{p,b}=\sum_bB^-_{p,b}=0), so the trace is zero.  Nevertheless

\[
 {p\over p}\sum_{b\in U(p)}K_p(b)(B^+_{p,b}-B^-_{p,b})
 =L(p-1).
 \tag{179.L25}
\]

This is a capacity-consistent falsification of any coefficient-only or
parity-only bucket theorem.  The arrays (179.L24) are not claimed to be
realizable by the selected squarefree endpoint atoms and therefore give
no literal lower bound.

### 3.6 Exact failure of the product-preserving orientation exchange

A plus atom has

\[
 d=\kappa u,\quad d'=\kappa u+2s,\quad
 m'=\kappa v,\quad m=\kappa v+2w,
 \qquad sv-wu=n.
 \tag{179.L26}
\]

Swapping the two factors at both endpoint products is

\[
 \tau:(u,v,s,w,+)\longmapsto(v,u,w,s,-).
 \tag{179.L27}
\]

Indeed, with (u'=v,v'=u,s'=w,w'=s),
(u'w'-s'v'=vs-wu=n), and the minus lower and upper products are

\[
 \kappa v'(\kappa u'+2s')
 =\kappa u(\kappa v+2w),
 \qquad
 \kappa u'(\kappa v'+2w')
 =\kappa v(\kappa u+2s).
 \tag{179.L28}
\]

Thus (\tau) preserves both endpoint products, their square-root phase,
and the determinant, but it changes the local K34 label from (u) to
(v).  If it stayed in the same fixed-(u) block, then (u=v); the
primitive condition ((u,v)=1) would force (u=v=1), and then every
(u_0,q) equals one, contrary to (q>Q_B).  In general it also changes
(u_0=u/(u,n)) to (v_0=v/(v,n)) and hence changes the conductor family.

Finally, (179.L27) replaces the selected divisors
(\kappa u,\kappa u+2s) by the complementary factors
(\kappa v+2w,\kappa v).  By the accepted literal selector support, the
complement lies below the allowed upper near-square divisor window in
the odd branch and is even in the even branch.  The corresponding
coefficient is therefore zero after the mandated zero extension.
Hence (\tau) proves neither (B^+_{q,b}=B^-_{q,b}) nor a contraction
of their difference; it is not a literal involution of (179.L2).

## 4. First doubtful or unproved step

The first unproved step is precisely a selector- and phase-aware estimate
for the complete defect (179.L2):

\[
 \left|\sum_{u_0\mid u}\sum_{\substack{q\mid u_0\\q>Q_B}}
 {q\over u_0}\sum_{b\in U(q)}K_q(b)
 (B^+_{q,b}-B^-_{q,b})\right|
 \stackrel{?}{\ll}_{B,\delta,\gamma,\varepsilon}LX^\varepsilon.
 \tag{179.L29}
\]

Neither parity nor the literal same-product exchange supplies a relation
between the two buckets in a fixed (u)-block.  Any continuation must
therefore prove a new signed correlation among the actual squarefree,
selected/no-pair, endpoint-weighted and incompletely lifted atoms, or a
new signed average across the retained (u_0,q,b) labels, before taking
positive norms.  The arbitrary control and (179.L19)--(179.L25) show why
an argument valid for all bounded buckets, one reciprocal square root,
or a lift-erasing completion cannot establish (179.L29).

This report does not claim that no different literal mechanism exists.
It proves no nontrivial defect sector and does not disprove (177.K34).

## 5. Required control test and outcome

| Control | Outcome |
|---|---|
| Odd modulus and unit residue | PASS.  (q\mid u_0\mid u) is odd, and ((v,u)=(n_0,u_0)=1) gives (b\in U(q)). |
| Exact-conductor Mobius projection | PASS in (179.L11)--(179.L12). |
| (d=1) trace term | PASS.  It is (\mu(q)/q) in each (K_q) and gives (2\mu(q)/u_0) after orientation pairing and (q/u_0) normalization. |
| (q/u_0) normalization | PASS in (179.L15)--(179.L16). |
| (q\mid u_0), (u_0\mid u) summation | PASS for the trace in (179.L18); positive defect summation returns (Lu_0) and (Lu) in (179.L22). |
| Literal two-orientation buckets | PASS.  They are defined separately in (179.L5)--(179.L6) before any absolute value. |
| Low-(q) no double count | PASS.  Every displayed aggregate is restricted to the disjoint exact packet (q>Q_B).  The projector's (d=1) summand is not a low-(q) alias. |
| Endpoint, parity, selector, lift, and zero extension | PASS.  They remain inside (A^\pm); the lift count is restored in (179.L19)--(179.L20), and selector failure of the exchange is explicit. |
| Outer absolute value | PASS.  Equations (179.L8), (179.L16), and (179.L2) are exact complex recombinations before the final absolute value. |
| Arbitrary-bucket false control | PASS in (179.L23)--(179.L25), explicitly quarantined from literal lower mass. |
| (L\sqrt q,Lq,Lu_0,Lu) stop tests | STOP.  They are restored in (179.L21)--(179.L22), not mistaken for (L). |
| No aliaswise pivot | PASS.  No use is made of (177.K35). |
| Downstream and exponent quarantine | PASS.  No claim is made about complete K17a, another hard-TOP channel, hard TOP, BAL, UNBAL, M9--M2, M1/GAR, assembly, a bridge, the quarter theorem, or any exponent. |

No numerical theorem evidence was used.

## 6. Dependencies and exact artifacts used

The mathematical derivation uses exactly the selected context:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `strategy/round179_m2_hard_top_t1_residual_k17a_primitive_conductor_orientation_defect_strategy.md`;
5. `proofs/kernels/m9_m2_hard_top_t1_residual_k17a_cross_gcd_alternating_fibre_reduction.md`;
6. `proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_alias_conductor_reduction.md`;
7. `rounds/codex-managed/full-proof-round175-177-strategy-literature-review/reviews/conductor_round178_adjudication.md`; and
8. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/synthesis.md`.

The task scope and write restriction come from `AGENTS.md` and
`rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/briefs/literal_primitive_conductor_parity_attack.md`.
No external theorem or source is invoked.

## 7. Recommended state effect

**Promote after seam review** the exact finite projector, parity identity,
two-orientation decomposition, and target-safe high-(q) trace
(179.L9)--(179.L18) as a subordinate proved-internal reduction.

**Retain** (177.K34), complete K17a, and all downstream owners as open.
Record the exact fixed-(u)/selector nonclosure (179.L26)--(179.L28) and
the prime projector norm self-return (179.L23)--(179.L25) under the
route-scoped label
`primitive_conductor_orientation_defect_capacity_or_self_return_no_go`.
Do not promote a strict defect sector, an aliaswise estimate, a bridge, a
quarter theorem, or an exponent change.
