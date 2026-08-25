# Round 158 conductor seed: exact sign-adapted cell trace

- Campaign: m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate
- Round: 158
- Role: conductor algebraic seed; candidate evidence only
- Starting graph: 3acbfaf6fb95047babd19800dee4152fb60cb408197a8ceac93931a20c57491f

## 1. Result

The moving-mask atom in the paired interior matrix has an exact
sign-adapted Abel form. Full-frequency inversion converts it to a
boundary-frozen selected physical sum. The zero-frequency and Nyquist
trace pieces are separately target-safe, so a target theorem for the
full-frequency physical trace would imply the paired-interior trace
target.

The endpoint subrow \(s=j\) is also target-safe by elementary p-adic
root counting. This does not close the strict trace: the prefix
\(s<j\) and suffix \(s>j\) reduce to a one-point-per-quotient signed
selected sum of capacity
\(\min(M,V)M^{-3/4}X^\varepsilon\). A square-root theorem would be
sufficient, but is not proved in this seed.

## 2. Exact statement and hypotheses

Put

\[
 q=4N,\quad c=\frac qd,\quad H=\frac c2,\quad
 \mathcal V_d^\circ=\{v\bmod H:v\ne0,H/2\}.
\tag{158.C1}
\]

Let \(J_+=[a_+,b_+]\) and \(J_-=[a_-,b_-]\) be consecutive strict
blocks inside \(V<|j|\le2V\). Write

\[
 B_j(x)=\mathbf 1_{x\ge\lambda_\sigma(j)}F_j(x),
 \qquad
 \lambda_+(j)=j+1,\quad\lambda_-(j)=-j,
\tag{158.C2}
\]

where the actual profile, complex phase, transitions, zero extension,
and endpoints remain in \(F_j\).

## 3. Proof or derivation

### 3.1 Positive prefix and negative suffix

For \(A_j(v)=\widehat B_j(2dv)\), positive-block differencing gives

\[
\begin{aligned}
 A_{j+1}(v)-A_j(v)
 &=-F_j(j+1)e_c(-2v(j+1))\\
 &\quad+
 \sum_{x\ge j+2}(F_{j+1}(x)-F_j(x))e_c(-2vx).
\end{aligned}
\tag{158.C3}
\]

With

\[
 P_{d,v}^+(j)=\sum_{s=a_+}^{j}K(-v^2,-s;c),
\tag{158.C4}
\]

the identity

\[
 \sum_{j=a_+}^{b_+}A_j(v)K(-v^2,-j;c)
 =
 A_{b_+}(v)P_{d,v}^+(b_+)
 +\sum_{j=a_+}^{b_+-1}
 (A_j(v)-A_{j+1}(v))P_{d,v}^+(j)
\tag{158.C5}
\]

puts the positive trace at

\[
 \sum_{j=a_+}^{b_+-1}F_j(j+1)e_c(-2v(j+1))
 P_{d,v}^+(j).
\tag{158.C6}
\]

On the negative block,

\[
\begin{aligned}
 A_j(v)-A_{j-1}(v)
 &=F_j(-j)e_c(2vj)\\
 &\quad+
 \sum_{x\ge-j+1}(F_j(x)-F_{j-1}(x))e_c(-2vx).
\end{aligned}
\tag{158.C7}
\]

With the suffix

\[
 P_{d,v}^-(j)=\sum_{s=j}^{b_-}K(-v^2,-s;c),
\tag{158.C8}
\]

one has

\[
 \sum_{j=a_-}^{b_-}A_j(v)K(-v^2,-j;c)
 =
 A_{a_-}(v)P_{d,v}^-(a_-)
 +\sum_{j=a_-+1}^{b_-}
 (A_j(v)-A_{j-1}(v))P_{d,v}^-(j).
\tag{158.C9}
\]

Thus the negative trace has the positive sign printed in (158.C7).
Summing (158.C6) and its negative analogue over
\(v\in\mathcal V_d^\circ\), then restoring
\(-i(1+i)\chi_4(d)d\sqrt c/(2Nq)\), gives the frozen trace.

### 3.2 Full-frequency inversion

For every \(x,s\),

\[
\begin{aligned}
 \sum_{v\bmod H}e_c(-2vx)K(-v^2,-s;c)
 =
 \frac{1-i}{2}\sqrt c
 \sum_{u\bmod c}^{*}\chi_4(u)e_c(u(x^2-s)).
\end{aligned}
\tag{158.C10}
\]

The exterior all-\(d\) identity for a delta mass at \(x\) therefore
gives

\[
 -\frac{i(1+i)}{2Nq}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c\,
 \sum_{v\bmod H}e_c(-2vx)K(-v^2,-s;c)
 =G_N(x^2-s).
\tag{158.C11}
\]

Substituting \(x=j+1\) on the positive side and \(x=-j\) on the negative
side proves

\[
\begin{aligned}
 \mathcal C_+^{\mathrm{full}}
 &=\sum_{j=a_+}^{b_+-1}F_j(j+1)
 \sum_{s=a_+}^{j}G_N((j+1)^2-s),\\
 \mathcal C_-^{\mathrm{full}}
 &=\sum_{j=a_-+1}^{b_-}F_j(-j)
 \sum_{s=j}^{b_-}G_N(j^2-s).
\end{aligned}
\tag{158.C12}
\]

### 3.3 The removed rows are safe at trace level

For \(v=0\), the accepted fixed-frequency interval theorem gives

\[
 \sup_I\left|\sum_{s\in I}K(0,-s;c)\right|
 \ll c\log(2c).
\tag{158.C13}
\]

For \(v=H/2=n\), opening the kernel gives the same unmodulated interval
capacity

\[
 \sup_I\left|\sum_{s\in I}K(-n^2,-s;c)\right|
 \ll c\log(2c).
\tag{158.C14}
\]

Since \(|F_j(\lambda_\sigma(j))|
\ll M^{-3/4}X^\varepsilon\), either trace piece costs, after all
exterior factors,

\[
\begin{aligned}
 \frac{VM^{-3/4}}{Nq}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 d\,c^{3/2}X^\varepsilon
 \ll
 \frac{VM^{-3/4}}{\sqrt N}X^\varepsilon
 \le M^{-1/4}X^\varepsilon.
\end{aligned}
\tag{158.C15}
\]

Thus full-frequency trace control may lawfully be reduced to paired
interior control without transferring the total-row theorems.

### 3.4 Endpoint p-adic subrow

At \(s=j\), the positive and negative congruences are

\[
 j^2+j+1\equiv0\pmod N,\qquad
 j(j-1)\equiv0\pmod N.
\tag{158.C16}
\]

For the second congruence, coprimality of consecutive integers assigns
every prime power \(p^\nu\Vert N\) wholly to \(j\) or to \(j-1\), giving
exactly \(2^{\omega(N)}\) classes modulo \(N\).

For the first congruence there is no root modulo \(2\). Modulo \(3\)
there is the single root \(j=1\), and

\[
 (1+3t)^2+(1+3t)+1
 =3(1+3t+3t^2),
\tag{158.C17}
\]

so there is no root modulo \(9\). For every odd \(p\ne3\), the
discriminant is \(-3\); every root is simple and has a unique lift to
each \(p^\nu\), with at most two classes. CRT gives
\(O_\varepsilon(N^\varepsilon)\) classes.

Because \(V<N\), each signed block contains
\(O_\varepsilon(N^\varepsilon)\) endpoint roots. The literal amplitude
therefore bounds the full endpoint subrow by

\[
 M^{-3/4}X^\varepsilon
 \ll M^{-1/4}X^\varepsilon.
\tag{158.C18}
\]

### 3.5 Strict selected trace

For the positive trace put \(k=j+1\); for the negative trace put
\(k=-j\). Every surviving physical term has

\[
 k^2-s=N\ell,\qquad
 -k\le s\le k-1,
\tag{158.C19}
\]

and therefore the nearest-cell partition gives one \(k\) for each
positive \(\ell\). The positive coefficient is \(F_{k-1}(k)\), the
negative coefficient is \(F_{-k}(k)\), and the arithmetic sign is
\(\chi_4(\ell)\). Hence the strict trace is an exact restriction of

\[
 \sum_{\ell\asymp M}
 \chi_4(\ell)
 \left[
 \mathbf 1_{\mathrm{pos}}F_{k_\ell-1}(k_\ell)
 +\mathbf 1_{\mathrm{neg}}F_{-k_\ell}(k_\ell)
 \right],
\tag{158.C20}
\]

with the literal block, strict-prefix or suffix, profile, transition,
and endpoint selectors restored. Its support is at most
\(\min(M,V)X^\varepsilon\). This is a cardinality bound, not a signed
estimate.

## 4. First doubtful or unproved step

The endpoint-polynomial route proves only (158.C18). The first unproved
object is the strict selected trace (158.C20), equivalently (158.C12)
with \(s=j\) deleted and the safe zero and fold trace pieces removed.

The seed has not proved square-root cancellation for (158.C20), nor
that the remaining bulk differences in (158.C3) and (158.C7) are
target-safe.

## 5. Required controls and outcomes

- Sign-adapted Abel formulas: derived, pending blind review.
- Full-frequency normalization: derived from the accepted delta-mass
  identity, pending independent review.
- Zero and fold trace pieces: target-safe capacity (158.C15), pending
  endpoint and power review.
- Endpoint polynomials and \(p=2,3\): target-safe (158.C16)--(158.C18),
  pending p-adic review.
- Strict prefix and suffix: retained; not replaced by endpoints.
- Selected support: \(\min(M,V)\) only; no cancellation inferred.
- Profile bulk and downstream owners: explicitly open.
- Numerical controls: none used.

## 6. Dependencies and exact artifacts used

- protocol.md
- state/proof_obligations.yml
- strategy/round158_d1_paired_interior_cell_trace_strategy.md
- proofs/kernels/m9_m1_d1_nonzero_centering_nyquist_fold.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reports/centered_nonzero_root_discrepancy_attack.md
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reviews/conductor_round157_adjudication.md

## 7. Recommended state effect

Do not patch state from this seed. Promote only after independent review
proves the sign-adapted trace, full-frequency normalization, safe
removed-row pieces, p-adic endpoint table, and exact selected rewrite.

Even then, distinguish:

1. a proved target for the whole strict trace;
2. a strict target-safe subrow such as the endpoint only; and
3. a rigorous no-go showing that endpoint roots do not control the
   strict selected trace.

No conclusion transfers to the profile bulk, the full paired interior
matrix, another owner, or a global exponent.
