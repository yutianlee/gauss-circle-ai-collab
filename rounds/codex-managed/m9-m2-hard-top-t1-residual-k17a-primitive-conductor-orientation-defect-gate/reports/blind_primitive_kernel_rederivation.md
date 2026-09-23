# 1. Result

**Lemma (primitive projection, canonical trace/defect splitting, and arbitrary-bucket no-go).** For every odd positive integer (q),

\[
K_q(b)=\frac1q\sum_{d\mid q}d\,\mu(q/d)(-1)^{[b]_d}.
\tag{1.1}
\]

If (b\in U(q)), then

\[
K_q(b)+K_q(-b)=\frac{2\mu(q)}q.
\tag{1.2}
\]

Thus the sum is (2/q), (-2/q), or (0) according as (mu(q)=1), (mu(q)=-1), or (mu(q)=0). This includes (q=1), when the sum is (2). In (1.1), every divisor (d>1) cancels under (b\mapsto-b); the entire right side of (1.2) comes from the separately treated divisor (d=1).

Put

\[
\tau_q:=\frac{\mu(q)}q,
\qquad
H_q(b):=K_q(b)-\tau_q
=\frac1q\sum_{\substack{d\mid q\\d>1}}
d\,\mu(q/d)(-1)^{[b]_d}.
\tag{1.3}
\]

On (U(q)), (H_q(-b)=-H_q(b)), and the exact block has the canonical decomposition

\[
\boxed{
\mathcal C_{u_0,q}
=\underbrace{\frac{\mu(q)}{u_0}
  \sum_{b\in U(q)}(B^+_{q,b}+B^-_{q,b})}_{\mathcal T_{u_0,q}}
+\underbrace{\frac q{u_0}
  \sum_{b\in U(q)}H_q(b)(B^+_{q,b}-B^-_{q,b})}_{\mathcal D_{u_0,q}}.}
\tag{1.4}
\]

The first term has trace-scale absolute capacity (O(LX^\varepsilon)) after the stated harmless divisor-label sums. This dependence on the available atom mass is sharp.

No comparable conclusion for (mathcal D_{u_0,q}) follows from the stated finite kernel and atom-count hypotheses alone. More precisely, if

\[
\Lambda_q:=\max_{b\in U(q)}|H_q(b)|,
\tag{1.5}
\]

then the exact operator norm of the defect on arbitrary complex buckets with prescribed orientation masses (M^+) and (M^-) is

\[
\sup |\mathcal D_{u_0,q}|
=\frac q{u_0}\Lambda_q(M^++M^-).
\tag{1.6}
\]

For every odd prime (p), (Lambda_p=1). Hence admissible adversarial buckets can have zero trace and defect of order (pLX^\varepsilon) when (q=u_0=p). This is an arbitrary-bucket no-go only: it does not assert that the undisclosed literal coefficients realize those adversarial buckets.

# 2. Exact statement and hypotheses

Let (e(t)=e^{2\pi i t}), let ([x]_d\in\{0,\ldots,d-1\}) denote the least residue, and let (q) and (u_0) be odd positive integers with (q\mid u_0). Assume (B179.1)--(B179.3), and assume that the two bucket arrays are supported on (U(q)).

For each orientation, write the corresponding bucket as the sum of its atoms and define its absolute atom mass by

\[
M^\pm_{u_0,q}:=
\sum_{\text{atoms in the }\pm\text{ orientation}}|w|.
\tag{2.1}
\]

The hypotheses in the packet imply

\[
\sum_{b\in U(q)}|B^\pm_{q,b}|
\le M^\pm_{u_0,q}
\ll u_0L X^\varepsilon.
\tag{2.2}
\]

If the packet's atom-count bound is read as a bound for both orientations combined, replace (M^++M^-) below by that combined mass; all conclusions and sharp scalings are unchanged.

The claims are:

1. (1.1)--(1.2) hold exactly, including the (d=1) and (q=1) cases.
2. (1.4) is the unique even/odd splitting obtained by taking the symmetric and antisymmetric parts of the two kernel coefficients (K_q(b)) and (K_q(-b)).
3. The trace obeys

   \[
   |\mathcal T_{u_0,q}|
   \le \frac{|\mu(q)|}{u_0}(M^+_{u_0,q}+M^-_{u_0,q}),
   \tag{2.3}
   \]

   and therefore

   \[
   \sum_{u_0\mid u}\sum_{q\mid u_0}|\mathcal T_{u_0,q}|
   \ll LX^\varepsilon
   \sum_{u_0\mid u}\sum_{q\mid u_0}|\mu(q)|.
   \tag{2.4}
   \]

   The remaining factor is exactly

   \[
   \sum_{u_0\mid u}\sum_{q\mid u_0}|\mu(q)|
   =\sum_{u_0\mid u}2^{\omega(u_0)}
   =\prod_{p^a\parallel u}(2a+1),
   \tag{2.5}
   \]

   so it is a divisor factor and is harmless by the packet's explicit convention. After the usual relabelling of epsilon, (2.4) is (O_\varepsilon(LX^\varepsilon)).
4. Under only (2.2), (1.6) is sharp. In particular, trace-scale control of the defect is not a universal algebraic consequence.

# 3. Proof or derivation

## Primitive-frequency divisor identity

For every divisor (h\mid q), write (q=hd). Since all these integers are odd, the denominators below are nonzero. Directly from (B179.1),

\[
c_q(hr)
=\frac{2}{hd\{1+e(-r/d)\}}
=\frac1h c_d(r).
\tag{3.1}
\]

Consequently the Fourier sum over frequencies divisible by (h) is

\[
\begin{aligned}
\sum_{\substack{a\bmod q\\h\mid a}}c_q(a)e(ab/q)
&=\sum_{r\bmod d}c_q(hr)e(rb/d)\\
&=\frac1h\sum_{r\bmod d}c_d(r)e(rb/d)\\
&=\frac1h E_d(b).
\end{aligned}
\tag{3.2}
\]

Möbius inversion gives, for residues (a\bmod q),

\[
\mathbf 1_{(a,q)=1}=\sum_{h\mid(a,q)}\mu(h).
\tag{3.3}
\]

This remains correct for (q=1). Insert (3.3) in (B179.2), apply (3.2), and then put (d=q/h):

\[
\begin{aligned}
K_q(b)
&=\sum_{h\mid q}\mu(h)
  \sum_{\substack{a\bmod q\\h\mid a}}c_q(a)e(ab/q)\\
&=\sum_{h\mid q}\frac{\mu(h)}h E_{q/h}(b)\\
&=\frac1q\sum_{d\mid q}d\,\mu(q/d)(-1)^{[b]_d}.
\end{aligned}
\tag{3.4}
\]

This proves (1.1).

## Sign reversal and the isolated (d=1) term

Fix (b\in U(q)). If (d\mid q) and (d>1), then (b) is also a unit modulo (d). Thus (r=[b]_d) lies in (\{1,\ldots,d-1\}), and

\[
[-b]_d=d-r.
\tag{3.5}
\]

Because (d) is odd,

\[
(-1)^{[b]_d}+(-1)^{[-b]_d}
=(-1)^r+(-1)^{d-r}=0.
\tag{3.6}
\]

For (d=1), both least residues are zero, so the corresponding bracket is (2), not (0). Hence (3.4) gives

\[
K_q(b)+K_q(-b)
=\frac1q\,1\,\mu(q)\{1+1\}
=\frac{2\mu(q)}q.
\tag{3.7}
\]

When (q=1), the sole divisor is simultaneously (d=1=q), and (3.7) still gives (2). Equation (1.3) and the oddness (H_q(-b)=-H_q(b)) now follow immediately.

## Canonical block decomposition

Set

\[
\Sigma_{q,b}=B^+_{q,b}+B^-_{q,b},
\qquad
\Delta_{q,b}=B^+_{q,b}-B^-_{q,b}.
\tag{3.8}
\]

By (1.3) and (3.7),

\[
K_q(b)=\tau_q+H_q(b),
\qquad
K_q(-b)=\tau_q-H_q(b).
\tag{3.9}
\]

Substitution into (B179.3) yields (1.4). The coefficient \(\tau_q\) is exactly the symmetric part

\[
\frac{K_q(b)+K_q(-b)}2=\frac{\mu(q)}q,
\tag{3.10}
\]

and (H_q(b)) is exactly the antisymmetric part. Therefore (1.4) is the canonical, and hence smallest, decomposition into a (b)-independent symmetric trace and the remaining orientation defect.

There is a second useful exact form. Since (U(q)) is stable under sign reversal and (H_q) is odd,

\[
\mathcal D_{u_0,q}
=\frac q{2u_0}\sum_{b\in U(q)}H_q(b)
\{\Delta_{q,b}-\Delta_{q,-b}\}.
\tag{3.11}
\]

Thus only the sign-odd part of the orientation difference can contribute.

## Sharp trace capacity

The triangle inequality and (2.2) give (2.3). Summing it over \(q\mid u_0\) and (u_0\mid u) proves (2.4). For fixed (u_0), the squarefree divisors counted by (|\mu(q)|) give

\[
\sum_{q\mid u_0}|\mu(q)|=2^{\omega(u_0)}.
\tag{3.12}
\]

Multiplicativity over the possible exponents (0,\ldots,a) of each prime (p^a\parallel u) then proves (2.5): exponent zero contributes (1), and each of the (a) positive exponents contributes (2).

The bound (2.3) is the exact absolute capacity for arbitrary complex buckets with fixed masses: when (mu(q)\ne0), place all allowed bucket mass at any unit and give both orientations a common phase. Equality holds in (2.3). If (mu(q)=0), the trace is identically zero, which is again exact. Hence neither the factor (1/u_0) nor the linear dependence on atom mass can be improved from the abstract hypotheses.

## Exact defect capacity and no-go

From (1.4),

\[
|\mathcal D_{u_0,q}|
\le\frac q{u_0}\Lambda_q
\sum_{b\in U(q)}|B^+_{q,b}-B^-_{q,b}|
\le\frac q{u_0}\Lambda_q(M^++M^-).
\tag{3.13}
\]

Choose \(b_0\) attaining (Lambda_q). With independent arbitrary complex buckets, put all (+) mass at (b_0) with phase opposite to that of (H_q(b_0)), and put all (-) mass there with the opposite bucket sign. Every summand in the defect then has the same phase, and equality holds in (3.13). The construction can be realized by disjoint sets of atoms, all assigned to (b_0), with aligned phases and allowed individual magnitudes. This proves the exact operator norm (1.6).

For orientation on the possible size of (Lambda_q), (1.3) gives the elementary bound

\[
\Lambda_q
\le \frac1q\sum_{\substack{d\mid q\\d>1}}d|\mu(q/d)|
\le\prod_{p\mid q}\left(1+\frac1p\right).
\tag{3.14}
\]

Crucially, (Lambda_q) need not contain any conductor saving. If (q=p) is an odd prime, (1.1) says

\[
K_p(b)=(-1)^{[b]_p}-\frac1p,
\qquad
H_p(b)=(-1)^{[b]_p},
\qquad
\Lambda_p=1.
\tag{3.15}
\]

Take (u_0=q=p), fix (b_0\in U(p)), and choose

\[
B^+_{p,b_0}=A,
\qquad
B^-_{p,b_0}=-A,
\tag{3.16}
\]

with every other bucket zero. The two arrays can be built from disjoint aligned atom sets. Their trace is exactly zero, whereas

\[
|\mathcal D_{p,p}|=2|A|.
\tag{3.17}
\]

Taking (|A|\asymp pLX^\varepsilon) within the per-orientation atom capacity (or half that size under a combined capacity) gives defect size (asymp pLX^\varepsilon). Therefore an (O(LX^\varepsilon)) defect bound cannot follow universally from the finite kernel and mass constraints.

This adversarial model proves only insufficiency of the disclosed hypotheses. The literal coefficients may possess correlations, involutions, or cancellation rules that exclude (3.16); none was disclosed, so no theorem about their actual defect follows either positively or negatively.

## Sufficient additional orientation relations

The exact weakest condition for vanishing defect is the weighted orthogonality

\[
\sum_{b\in U(q)}H_q(b)
\{B^+_{q,b}-B^-_{q,b}\}=0.
\tag{3.18}
\]

A stronger but transparent structural condition is evenness of the orientation difference:

\[
B^+_{q,b}-B^-_{q,b}
=B^+_{q,-b}-B^-_{q,-b}
\quad(b\in U(q)).
\tag{3.19}
\]

Equation (3.11) then makes the defect zero. Pointwise equality (B^+_{q,b}=B^-_{q,b}) is a still stronger sufficient condition.

Quantitatively, a trace-scale estimate follows, for example, from

\[
\sum_{b\in U(q)}
|\Delta_{q,b}-\Delta_{q,-b}|
\ll \frac{u_0}{q\Lambda_q}LX^\varepsilon
\tag{3.20}
\]

when (Lambda_q>0); (3.11) then gives (|\mathcal D_{u_0,q}|\ll LX^\varepsilon). Equivalently, one may prove the sharper cancellation statement

\[
\left|\sum_{b\in U(q)}H_q(b)\Delta_{q,b}\right|
\ll \frac{u_0}{q}LX^\varepsilon.
\tag{3.21}
\]

Either (3.19), (3.20), or (3.21) must come from the undisclosed literal coefficient structure, not from the primitive kernel alone.

# 4. First doubtful or unproved step

There is no doubtful step in the finite identities (1.1)--(1.4), the trace estimate, or the arbitrary-bucket operator norm. The first unproved application step would be any assertion that the literal orientation difference has zero or small sign-odd part, as in (3.19)--(3.21). The packet supplies atom counts and magnitudes but no relation of that kind. The absorption of (2.5) is also used only because the packet explicitly declares divisor factors harmless; no undisclosed range for (u) is inferred here.

# 5. Required controls and outcomes

1. **(d=1) control: pass.** For every (d>1), the two parity values cancel for unit (b). For (d=1), both are (1), producing exactly (2\mu(q)/q).
2. **(q=1) edge control: pass.** (K_1(0)=1), (H_1(0)=0), the sign sum is (2), and the defect vanishes.
3. **Prime-conductor control: pass.** Formula (3.15) gives (K_p(b)+K_p(-b)=-2/p) and (Lambda_p=1), exposing the absence of a universal conductor saving in the defect.
4. **Nonsquarefree control: pass.** If (mu(q)=0), then the trace is zero and (K_q(-b)=-K_q(b)); this agrees with (1.2)--(1.4).
5. **Symmetric-bucket control: pass.** If (B^+=B^-) pointwise, then (Delta=0), so only the trace remains.
6. **Even-difference control: pass.** If (3.19) holds, pair (b) with (-b) in (3.11); the defect cancels exactly. For odd (q>1), no unit is fixed by sign reversal.
7. **Adversarial-bucket control: pass as a no-go.** The prime example (3.16) has zero trace and a defect larger than trace scale by a factor of order (p), while respecting support, disjoint orientation, atom-count, and atom-magnitude hypotheses.

No numerical computation was used or needed.

# 6. Dependencies and exact artifacts used

Mathematical input was restricted to exactly:

- `protocol.md` (workflow and promotion rules only); and
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/blind_statement.md` (all mathematical definitions and hypotheses).

`AGENTS.md` was read only as the repository's administrative instruction file, as required by the assignment. No graph, campaign, strategy, proof draft, prior round, source, sibling report, review, control, synthesis, or conductor artifact was inspected. No external theorem or computation was used.

# 7. Recommended state effect

**Promote** the exact primitive divisor identity, sign-reversal law, canonical trace/defect decomposition, and trace-capacity estimate as a finite candidate lemma after the required independent review. **Reject** any universal claim that the disclosed finite kernel and atom capacities alone yield trace-scale control of the orientation defect. **Retain** the literal-coefficient defect obligation as open until a relation such as (3.19), (3.20), or (3.21) is proved from the actual bucket construction. The arbitrary-bucket no-go must not be misreported as a counterexample to that undisclosed literal problem.
