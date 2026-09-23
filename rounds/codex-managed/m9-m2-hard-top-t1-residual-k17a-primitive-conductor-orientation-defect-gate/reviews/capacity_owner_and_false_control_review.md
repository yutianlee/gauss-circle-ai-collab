# Capacity, owner, and false-control review

## 1. Verdict

**GREEN.**  The centered primitive-conductor identity, symmetric trace,
all-conductor self-return, prime and prime-square false controls, and
restored-power ledger in
`m9_m2_hard_top_t1_residual_k17a_primitive_conductor_parity_self_return.md`
are correct.  The formalized candidate states the same result at the
proper owner level and quarantines both literal lower mass and every
downstream or exponent implication.

There is no repair issue in the finite algebra or the power bookkeeping.
The exact first unproved statement is (179.K19), the complete literal
centered-defect estimate.  The self-return shows that this estimate is
the unresolved original orientation block minus an already-safe low-(q)
term; it supplies no estimate for that block.

One scope wording must remain narrow when the candidate is converted into
a State Patch: “centered-conductor gain” may be rejected only as an
**automatic gain from centering or coefficient-uniform conductor
algebra**.  The result does not reject a future selector- and phase-aware
proof written in centered variables.

## 2. Exact claims and hypotheses audited

Retain the accepted literal K17a packet, with

\[
g=(u,n),\qquad u=gu_0,\qquad n=gn_0,\qquad(n_0,u_0)=1,
\]

(u,u_0) odd, ((u,v)=1), and all selectors, squarefree and
coprimality fields, parity branches, physical lifts, phases, hard
endpoints, endpoint conjugations, and zero extensions inside the literal
amplitudes.  For (q\mid u_0), every occupied
(b=\bar v n_0\pmod q) is a unit.

The review audits the following exact assertions.

1. With
   \[
   K_q^\circ(b)=K_q(b)-{\mu(q)\over q},
   \]
   one has (K_q^\circ(-b)=-K_q^\circ(b)) on (U(q)), and the
   exact-(q) block splits as
   \[
   \mathcal C_{u_0,q}
   ={q\over u_0}\sum_bK_q^\circ(b)(B^+_{q,b}-B^-_{q,b})
   +{\mu(q)\over u_0}\sum_b(B^+_{q,b}+B^-_{q,b}).
   \tag{179.R1}
   \]
2. For every odd (u_0>1) and (b\in U(u_0)), reduced modulo each
   (q\mid u_0),
   \[
   \sum_{q\mid u_0}{q\over u_0}K_q^\circ(b)=E_{u_0}(b).
   \tag{179.R2}
   \]
3. The complete high-(q) symmetric trace is
   (O_\varepsilon(LX^\varepsilon)) at fixed supported
   ((\kappa,u)).
4. The centered exact-(q) defect has coefficient-uniform capacity
   (O_\varepsilon(LqX^\varepsilon)), and prime and prime-square
   artificial buckets attain that scale while respecting the unit and
   bucket-count shadows.
5. One conductor square-root saving restores only
   (L\sqrt qX^\varepsilon), which is not uniform target scale over the
   power-size high-(q) range.
6. The result changes no owner or exponent beyond the proposed
   subordinate reduction/no-go record.

## 3. Independent derivation and power audit

### 3.1 Centered all-conductor identity

Removing the (d=1) term from the verified primitive projector gives

\[
K_q^\circ(b)
={1\over q}\sum_{\substack{d\mid q\\d>1}}
\mu(q/d)dE_d(b).
\tag{179.R3}
\]

Therefore, for (u_0>1),

\[
\begin{aligned}
\sum_{q\mid u_0}{q\over u_0}K_q^\circ(b)
&={1\over u_0}
  \sum_{\substack{d\mid u_0\\d>1}}dE_d(b)
  \sum_{r\mid u_0/d}\mu(r)\\
&=E_{u_0}(b),
\end{aligned}
\tag{179.R4}
\]

because the inner Möbius sum survives only at (d=u_0).  This proves
(179.R2) with no missing divisor, totient, or lift factor.

The (q=1) boundary is also correct:

\[
K_1(0)=1,\qquad K_1^\circ(0)=0.
\]

Thus (179.R2) is not asserted for (u_0=1); its high-conductor packet is
empty.  For (u_0>1), the (q=1) term is essential in the symmetric
trace because

\[
\sum_{q\mid u_0}\mu(q)=0.
\tag{179.R5}
\]

The unphased sum of each orientation's buckets is independent of (q),
so (179.R5) cancels the all-conductor centered trace exactly.  Applying
(179.R4) atom by atom gives

\[
\mathcal D^\circ_{>Q_B}
=\mathcal O_{u_0}-\mathcal D^\circ_{\le Q_B},
\qquad
\mathcal C_{>Q_B}
=\mathcal O_{u_0}-\mathcal C_{\le Q_B}.
\tag{179.R6}
\]

The accepted low-(q) block is locally target-safe: its positive ledger
at fixed ((\kappa,u)) is

\[
\sum_{u_0\mid u}\sum_{\substack{q\mid u_0\\q\le Q_B}}
Lq\log(2q)
\ll LQ_B\log(2Q_B)\tau(u)^2
\ll_\varepsilon LX^\varepsilon.
\tag{179.R7}
\]

The low centered trace is also target-safe by the calculation below, so
(\mathcal D^\circ_{\le Q_B}) is safe.  Hence (179.R6) is an exact
self-return to the unresolved literal block, not a hidden proof of it.

### 3.2 Trace capacity and divisor labels

At fixed ((\kappa,u,u_0)), the combined literal atom mass of the two
orientations is (O_\varepsilon(u_0LX^\varepsilon)).  The symmetric
trace coefficient in (179.R1) is (|\mu(q)|/u_0), so

\[
\left|{\mu(q)\over u_0}\sum_b(B^+_{q,b}+B^-_{q,b})\right|
\ll |\mu(q)|LX^\varepsilon.
\tag{179.R8}
\]

The exact number of squarefree conductor labels across the two divisor
sums is

\[
\begin{aligned}
\sum_{u_0\mid u}\sum_{q\mid u_0}|\mu(q)|
&=\sum_{u_0\mid u}2^{\omega(u_0)}\\
&=\prod_{p^a\parallel u}(2a+1)
\le \tau(u)2^{\omega(u)}
\ll_\varepsilon X^\varepsilon.
\end{aligned}
\tag{179.R9}
\]

Restricting to (q>Q_B) only decreases this sum.  Equations
(179.R8)--(179.R9) prove the asserted (LX^\varepsilon) high-trace
bound.  For nonsquarefree (q), the trace vanishes exactly.  The
(d=1) projector term inside a high conductor is not the separate
(q=1) alias, so this calculation does not recount the accepted low
packet.

### 3.3 Physical lifts and exact-conductor capacity

Write

\[
h={u_0\over q},\qquad u=ghq\asymp {L\over\kappa}.
\]

A fixed ordered unit residue pair modulo (q) has (O(gh)) physical
(v)-lifts, (O(h)) (n_0)-lifts, and (O(\kappa)) fibre sites.  Its
multiplicity is

\[
O(\kappa gh^2)=O(Lh/q).
\tag{179.R10}
\]

A fixed inverse-product bucket has (O(q)) ordered residue pairs and
therefore (O(Lh)=O(Lu_0/q)) atoms.  Summing the unit buckets restores
the (O(u_0L)) stratum mass.

From (179.R3),

\[
|K_q^\circ(b)|
\le {1\over q}\sum_{\substack{d\mid q\\d>1}}
d|\mu(q/d)|
\le\prod_{p\mid q}\left(1+{1\over p}\right)
\ll_\varepsilon q^\varepsilon.
\tag{179.R11}
\]

Consequently the full positive defect capacity is

\[
{q\over u_0}\,q\,{Lu_0\over q}\,q^\varepsilon
\ll_\varepsilon LqX^\varepsilon.
\tag{179.R12}
\]

There is no erased (g,h,\kappa), or physical-period multiplicity in
(179.R12).  Positively summing conductors and gcd strata would restore
(Lu_0X^\varepsilon) and then (LuX^\varepsilon), not the local
(L)-target.

### 3.4 Prime and prime-square false controls

For (q=u_0=p), (p) an odd prime,

\[
K_p^\circ(b)=E_p(b),\qquad
\sum_{b\in U(p)}|K_p^\circ(b)|=p-1.
\tag{179.R13}
\]

Put (B^-_{p,b}=0) and
(B^+_{p,b}=M E_p(b)), with (M\asymp L).  This uses (O(L)) atoms
per bucket and (O(Lp)) in total, within (179.R10)--(179.R12).  Moreover
(\sum_{b\in U(p)}E_p(b)=0), so the symmetric trace vanishes, while

\[
\left|\sum_bK_p^\circ(b)B^+_{p,b}\right|
=M(p-1)\asymp Lp.
\tag{179.R14}
\]

For (q=u_0=p^2),

\[
K_{p^2}^\circ(b)=E_{p^2}(b)-{1\over p}E_p(b),
\qquad \mu(p^2)=0.
\tag{179.R15}
\]

Every unit value in (179.R15) has magnitude between (1-1/p) and
(1+1/p).  Hence

\[
(1-1/p)\varphi(p^2)
\le\sum_{b\in U(p^2)}|K_{p^2}^\circ(b)|
\le(1+1/p)\varphi(p^2),
\tag{179.R16}
\]

which is (\asymp p^2).  Filling each unit bucket with
(M\asymp L) atoms whose phase aligns with (K_{p^2}^\circ(b)) uses
(O(Lp^2)) total atoms and produces (\asymp Lp^2=Lq); its trace is
identically zero.  Both controls obey the unit support and literal
bucket-count **upper shadow**, but discard the actual selector and phase
field.  They reject only coefficient-uniform contraction and are not
literal K17a lower mass.

### 3.5 One-square-root and owner powers

Granting one square-root saving relative to (179.R12) gives

\[
L\sqrt qX^\varepsilon.
\tag{179.R17}
\]

Polylogarithmic (q) can be absorbed into (X^\varepsilon), but the
uniform high packet also contains power-size \(q\mid u_0\), so
(179.R17) remains above (LX^\varepsilon).  A full (q)-saving, two
coupled square roots, or an equivalent literal signed average is still
required.

The calculation ends at the residual K17a primitive-conductor mechanism.
It does not close complete K17a, another hard-TOP channel, hard TOP,
BAL, UNBAL, M9--M2, M1 or GAR, endpoint assembly, M9, either bridge, the
quarter theorem, or any exponent owner.

## 4. Exact first issue or unproved step

There is **no repair issue** before (179.K19).  The first unproved step is

\[
\left|
\sum_{u_0\mid u}\sum_{\substack{q\mid u_0\\q>Q_B}}
{q\over u_0}\sum_{b\in U(q)}K_q^\circ(b)
(B^+_{q,b}-B^-_{q,b})
\right|
\stackrel{?}{\ll}_{B,\delta,\gamma,\varepsilon}LX^\varepsilon.
\tag{179.R18}
\]

By (179.R6), this is the original unresolved literal orientation block
minus a safe low-conductor term.  The finite parity algebra proves no
relation between the actual (B^+) and (B^-) buckets.  The prime and
prime-square controls preclude a proof valid for arbitrary bounded
buckets, while neither control says that the actual literal defect is
large.

Accordingly, the candidate may park automatic/coefficient-uniform
centering and one-square-root routes, but it must not reject a future
literal signed theorem formulated using (K_q^\circ).

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Centered divisor identity | **PASS.** Independent Möbius interchange gives (179.R4). |
| (d=1) and (q=1) | **PASS.** Centering removes exactly (\mu(q)/q); (K_1=1), (K_1^\circ=0), and (q=1) is essential only to all-conductor trace cancellation. |
| Unit reduction | **PASS.** The same (\beta_z\in U(u_0)) reduces to a unit in every (q\mid u_0). |
| Symmetric trace capacity | **PASS.** Equations (179.R8)--(179.R9) give (LX^\varepsilon) after both divisor sums. |
| Squarefree/nonsquarefree trace | **PASS.** The trace is supported on squarefree (q); it vanishes for (p^2), while the defect retains full capacity. |
| Low-(q) boundary | **PASS.** The high/low split is exact, and (179.R7) verifies the low centered packet is target-safe. |
| (q/u_0) and physical lifts | **PASS.** Equations (179.R10)--(179.R12) restore the exact (Lq), (Lu_0), and (Lu) stop scales. |
| Prime false control | **PASS.** It has zero centered trace and (\asymp Lp) defect with (O(L)) mass per bucket. |
| Prime-square false control | **PASS.** Its trace is zero and its kernel has \(\ell^1\)-mass (\asymp p^2), giving (\asymp Lp^2). |
| False-control quarantine | **PASS.** The arrays obey only unit/count shadows and are not asserted to realize literal selectors or phases. |
| One-square-root restoration | **PASS as a no-go boundary.** It leaves (L\sqrt qX^\varepsilon), nonuniform on power conductors. |
| Orientation defect | **OPEN, correctly stated.** Neither evident orientation map proves (179.R18). |
| Outer absolute value | **PASS.** The complete defect retains one absolute value after all (u_0,q,b) and orientation recombination. |
| Owner scope | **PASS.** Only a subordinate K17a reduction/no-go is proposed; no parent status changes. |
| Exponent quarantine | **PASS.** Internal (1/3), external (0.3144831759740614\ldots), and target (1/4) remain unchanged. |

No numerical or external theorem evidence is used.

## 6. Dependencies and exact artifacts used

The review uses:

1. `AGENTS.md`, `protocol.md`, `state/proof_obligations.yml`, and
   `state/active_campaign.yml` for governance and inherited owner scope;
2. `proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_conductor_parity_self_return.md`;
3. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/candidates/formalized_primitive_conductor_parity_self_return.md`;
4. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/reports/hostile_orientation_defect_capacity_audit.md`;
5. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/reports/blind_primitive_kernel_rederivation.md`; and
6. the inherited accepted cross-gcd and primitive-alias kernels for the
   literal atom and lift capacities.

The hostile and blind reports were used as independent evidence, but all
divisor and power calculations in Sections 3.1--3.5 were recomputed.
No external source or computation was used.

## 7. Recommended state effect

**GREEN for promotion after the remaining required seams.**  The
formalized candidate may create a subordinate proved-internal
projector/trace/self-return reduction and record the scoped
`primitive_conductor_orientation_defect_capacity_or_self_return_no_go`.

Any rejected claim should say that **centering alone**, parity alone,
coefficient-uniform bucket bounds, the two evident orientation maps, or
one conductor square root does not prove (177.K34).  Do not formulate a
rejection of all selector-aware arguments in centered variables.

Retain (177.K34), complete K17a, every parent and bridge, the quarter
theorem, and every exponent at inherited status.  This reviewer makes no
graph or shared-state edit.
