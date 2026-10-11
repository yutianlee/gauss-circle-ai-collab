# Round 231: isolated actual-residual obstruction

- Campaign/task: `round231_residual_saving` / `blind_residual_control`.
- Role/status: statement-only independent arithmetic derivation; candidate evidence, not accepted graph mathematics.
- Generated: 2026-10-11T14:53:37+08:00.
- Provenance graph identifier supplied by the brief: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b` (graph not read).
- Exact context: `protocol.md`; `strategy/round231_residual_saving/briefs/blind_residual_statement.md`; coordinator task message.
- Isolation: no graph, history, sibling reports, or web consulted. No numerical experiment was needed; the controls below are exact arithmetic identities.

## 1. Result: a no-go theorem

For the actual residual in the brief, a uniform estimate of the displayed form necessarily has

\[
\boxed{\kappa\leq \frac1{20}.}
\]

There are legal starts and lengths on which the constant-phase sum is asymptotic to
\(-34H x^{-1/20}\). There are the same starts and lengths on which the fixed linear phase \(P(n)=n/4\) gives a sum asymptotic to \(iH x^{-1/20}\).

The latter obstruction survives subtraction of **any scalar**, even a scalar chosen separately for each interval and allowed to be complex. In particular, subtracting the exact interval mean of the residual does not remove it.

These are restrictions only. They do not prove an upper bound for any positive \(\kappa\), including \(\kappa=1/20\).

## 2. Exact statement and hypotheses

Write \(\chi=\chi_4\), \(e(t)=\exp(2\pi i t)\), and

\[
\begin{split}
r_2(n)&=4\sum_{d\mid n}\chi(d),\qquad z=x^{1/20},\\
K_x(t)&=\frac{\log t-2\log z}{\log z},\\
r_x^\sharp(n)&=4K_x(n)\sum_{\substack{z\leq d<z^2\\d\mid n}}\chi(d)
 +4\sum_{\substack{d<z\\d\mid n}}[\chi(d)+\chi(n/d)],\\
v_x(n)&=r_2(n)-r_x^\sharp(n).
\end{split}
\]

All divisors in these formulas are positive. Use exactly the half-open interval \(x<n\leq x+H\) and exactly the indicated strict/non-strict divisor cutoffs.

For integers \(k\to\infty\), set

\[
z_k=4k+1,\qquad x_k=z_k^{20},\qquad
H_k=4\left\lfloor\frac{x_k^{24/25}}4\right\rfloor.
\]

These are real endpoints permitted by the problem, with the additional useful properties that \(x_k\) is an integer and \(H_k\) is a multiple of four. For sufficiently large \(k\),

\[
x_k^{1/3+1/25}=x_k^{28/75}\leq H_k\leq x_k^{24/25},
\qquad H_k\sim x_k^{24/25}.
\]

The precise conclusions are

\[
\frac{\sum_{x_k<n\leq x_k+H_k}v_{x_k}(n)}{H_k/x_k^{1/20}}
\longrightarrow -34,
\]

and, for every arbitrary scalar sequence \(c_k\in\mathbb C\),

\[
\frac{\sum_{x_k<n\leq x_k+H_k}(v_{x_k}(n)-c_k)e(n/4)}{H_k/x_k^{1/20}}
\longrightarrow i.
\]

Only the allowed divisor identity, bounded character partial sums, finite geometric sums, and
\(A(y)=\sum_{n\leq y}r_2(n)=\pi y+O(\sqrt y+1)\) are used. No lattice-counting theorem beyond the supplied estimate is required.

## 3. Proof and derivation

### 3.1 The relevant character tails, with exact cutoff conventions

Define

\[
B(u)=\sum_{1\leq d<u}\frac{\chi(d)}d,\qquad
T(u)=\frac\pi4-B(u).
\]

Bounded character partial sums establish convergence of the character series. More explicitly, grouping adjacent nonzero terms gives

\[
\sum_{d\geq1}\frac{\chi(d)}d
=\int_0^1\frac{dt}{1+t^2}=\frac\pi4.
\]

For every positive integer \(u\equiv1\pmod4\), the first term retained in the tail is the positive term \(1/u\). Hence

\[
T(u)=\sum_{j\geq0}\left(\frac1{u+4j}-\frac1{u+4j+2}\right)
=\int_0^1\frac{t^{u-1}}{1+t^2}\,dt.
\]

The integral follows by summing the nonnegative paired integrands; no interchange of an unconditionally divergent series is involved. Since

\[
0\leq\frac1{1+t^2}-\frac12\leq1-t\quad(0\leq t\leq1),
\]

we have the quantitative bounds

\[
\frac1{2u}\leq T(u)\leq\frac1{2u}+\frac1{u(u+1)}.
\tag{3.1}
\]

In particular, for our \(z\), both \(z\) and \(z^2\) are \(1\pmod4\), and

\[
T(z)=\frac1{2z}+O(z^{-2}),\qquad
T(z^2)=\frac1{2z^2}+O(z^{-4}).
\tag{3.2}
\]

The actual middle divisor block is exactly

\[
\sum_{z\leq d<z^2}\frac{\chi(d)}d=B(z^2)-B(z)=T(z)-T(z^2).
\tag{3.3}
\]

### 3.2 Constant-phase sum of the actual residual

Throughout this subsection let \(z=4k+1\), \(x=z^{20}\), and \(H=H_k\). Put

\[
J=\int_x^{x+H}K_x(t)\,dt.
\]

For each positive integer \(d\), the real-endpoint count is

\[
\#\{x<n\leq t:d\mid n\}=\lfloor t/d\rfloor-\lfloor x/d\rfloor
=\frac{t-x}{d}+O(1).
\]

Since \(K_x(x)=18\), \(K_x\) is increasing, and \(x+H\leq2x\), partial summation gives, uniformly in \(d\),

\[
\sum_{\substack{x<n\leq x+H\\d\mid n}}K_x(n)=\frac Jd+O(1).
\]

The error is bounded by a constant times the maximum and total variation of \(K_x\), both uniformly bounded here. The bounded partial sums of \(\chi\) also give

\[
\sum_{x/d<m\leq(x+H)/d}\chi(m)=O(1).
\]

Summing the three displayed parts of the actual \(r_x^\sharp\), without dropping the cofactor term, therefore yields

\[
\sum_{x<n\leq x+H}r_x^\sharp(n)
=4J[T(z)-T(z^2)]+4HB(z)+O(z^2+z).
\]

The supplied estimate for \(A\) yields

\[
\sum_{x<n\leq x+H}v_x(n)
=4HT(z)-4J[T(z)-T(z^2)]+O(\sqrt x+z^2).
\tag{3.4}
\]

The logarithmic weight is treated exactly up to a controlled integral:

\[
J=18H+R,\qquad
0\leq R=\frac1{\log z}\int_x^{x+H}\log(t/x)\,dt
\leq\frac{H^2}{x\log z}.
\]

Inserting this and (3.2) into (3.4) gives

\[
\sum_{x<n\leq x+H}v_x(n)
=-\frac{34H}{z}
 +O\left(\frac H{z^2}+\frac{H^2}{xz\log z}+\sqrt x+z^2\right).
\tag{3.5}
\]

Every error in (3.5) is \(o(H/z)\): its ratio to \(H/z\) is bounded respectively by constants times

\[
x^{-1/20},\quad x^{-1/25}/\log z,\quad x^{-41/100},\quad x^{-81/100}.
\]

This proves the asserted constant-phase limit.

### 3.3 An exact mod-four identity for the full coefficient

The divisor formula immediately implies

\[
r_2(2m)=r_2(m).
\tag{3.6}
\]

Indeed, only odd divisors contribute, and the odd divisors of \(2m\) and \(m\) coincide. If \(n\equiv3\pmod4\), all its divisors are odd and
\(\chi(n/d)=\chi(n)\chi(d)=-\chi(d)\). Replacing \(d\) by \(n/d\) in the divisor sum proves

\[
r_2(n)=0\quad(n\equiv3\pmod4).
\tag{3.7}
\]

Consequently the residue-class masses below \(y\) are exactly

\[
\begin{array}{c|c}
n\bmod4&\sum_{n\leq y,\ n\text{ in class}}r_2(n)\\ \hline
0&A(y/4)\\
1&A(y)-A(y/2)\\
2&A(y/2)-A(y/4)\\
3&0.
\end{array}
\]

Thus, for every real \(y\geq1\),

\[
F(y):=\sum_{n\leq y}r_2(n)i^n
=2A(y/4)-A(y/2)+i[A(y)-A(y/2)]
=\frac{i\pi y}{2}+O(\sqrt y+1).
\tag{3.8}
\]

In particular,

\[
\sum_{x<n\leq x+H}r_2(n)i^n=\frac{i\pi H}{2}+O(\sqrt x).
\tag{3.9}
\]

### 3.4 The actual truncated coefficient at the linear phase

Whenever \(\chi(d)\neq0\), \(d\) is odd, and all interval sums of \(i^{dm}\) are uniformly bounded by the finite geometric-series formula. Partial summation with the same bounded weight \(K_x\) shows

\[
4\sum_{z\leq d<z^2}\chi(d)
\sum_{x/d<m\leq(x+H)/d}K_x(dm)i^{dm}=O(z^2).
\tag{3.10}
\]

The unweighted small-divisor \(\chi(d)\) term is similarly \(O(z)\).

The cofactor term has a nonzero mean at this phase, which must be retained. For odd \(d\), the exact identity is

\[
\chi(m)i^{dm}=i\chi(d)\,1_{m\text{ odd}}.
\tag{3.11}
\]

For \(d\equiv0\pmod4\) the left side is \(\chi(m)\); for \(d\equiv2\pmod4\) it is \(-\chi(m)\). Its sums for even \(d\) are therefore bounded. For odd \(d\), counting the odd integers with the actual real endpoints gives

\[
\sum_{x/d<m\leq(x+H)/d}\chi(m)i^{dm}
=\frac{i\chi(d)H}{2d}+O(1).
\]

It follows that the complete cofactor term equals

\[
4\sum_{d<z}\sum_{x/d<m\leq(x+H)/d}\chi(m)i^{dm}
=2iHB(z)+O(z).
\tag{3.12}
\]

Combining (3.9)--(3.12) for the displayed actual residual yields

\[
\sum_{x<n\leq x+H}v_x(n)e(n/4)
=2iHT(z)+O(\sqrt x+z^2)
=\frac{iH}{z}+O\left(\frac H{z^2}+\sqrt x+z^2\right).
\tag{3.13}
\]

As before all errors are \(o(H/z)\).

### 3.5 Scalar subtraction and the exponent restriction

Our \(x\) is an integer and \(H\) is a multiple of four. Therefore the actual interval consists of \(H/4\) complete periods of \(i^n\), and

\[
\sum_{x<n\leq x+H}e(n/4)=0
\tag{3.14}
\]

exactly. For any scalar \(c\in\mathbb C\), (3.14) gives

\[
\sum_{x<n\leq x+H}(v_x(n)-c)e(n/4)
=\sum_{x<n\leq x+H}v_x(n)e(n/4).
\]

Equation (3.13) proves the scalar-subtraction assertion. For sufficiently large members of this sequence, either the raw residual or any scalar-centered residual has

\[
\left|\sum_{x<n\leq x+H}(v_x(n)-c)e(n/4)\right|
\geq\frac{H}{2z}=\frac12H x^{-1/20}.
\]

If a uniform bound \(CHx^{-\kappa}\) held with \(\kappa>1/20\), this would imply
\(x^{\kappa-1/20}\leq2C\) along an unbounded sequence, a contradiction. The fixed phases \(P=0\) and \(P(n)=n/4\) suffice; there is no phase depending on \(x\) or increasing degree.

## 4. First doubtful or unproved step

There is no unproved step in the restriction above, conditional only on the explicitly supplied estimate for \(A(y)\).

The first unsupported extension would be to infer that an upper bound with \(\kappa\leq1/20\) actually holds. The proof establishes a lower-bound obstruction along one legal sequence; it neither supplies uniform upper bounds for general phases nor excludes additional stronger obstructions. Similarly, removing a nonconstant periodic correction is outside the scalar-removal statement and is not assessed here.

## 5. Required controls and outcomes

All controls are exact analytical controls on the actual coefficients; no floating-point experiment is used.

1. **Actual cutoffs and endpoint control — PASS.** Since \(z=4k+1\), the tail \(T(z)\) includes the positive term \(1/z\); the divisor block is exactly \(T(z)-T(z^2)\). All interval counts use \(\lfloor(x+H)/d\rfloor-\lfloor x/d\rfloor\), retaining the open lower and closed upper endpoint. The selected integer starts are a legal subsequence of the required real starts.

2. **Exhaustive character/phase control — PASS.** For \(m\equiv0,1,2,3\pmod4\), the actual products \(\chi(m)i^{dm}\) are respectively:

   | \(d\bmod4\) | Four successive values | Period mean |
   |---|---|---|
   | 0 | \(0,1,0,-1\) | \(0\) |
   | 1 | \(0,i,0,i\) | \(i/2\) |
   | 2 | \(0,-1,0,1\) | \(0\) |
   | 3 | \(0,-i,0,-i\) | \(-i/2\) |

   This checks the sign and factor \(2iHB(z)\) in (3.12); treating the cofactor character as mean zero after multiplying by the phase would be false.

3. **Full-coefficient normalization control — PASS.** The exact identities (3.6)--(3.8) recover the Fourier density \(i\pi/2\) directly from the allowed divisor identity and \(A\). In particular, there is no unsupported assertion of equidistribution of represented integers among residue classes.

4. **Scalar-mean repair control — FAIL as a proposed repair.** Equation (3.14) annihilates every scalar exactly, while (3.13) retains the asymptotic \(iH/z\). Taking \(c=H^{-1}\sum v_x(n)\), the exact local arithmetic mean, does not change this result.

5. **Legal-window and error control — PASS.** The chosen length is asymptotic to the permitted upper endpoint \(x^{24/25}\), dominates the lower endpoint \(x^{28/75}\), and makes the supplied \(O(\sqrt x)\) discrepancy negligible compared with \(H/z\). No unprovided short-interval asymptotic is needed.

The proof uses the genuine \(\chi_4\) period and genuine divisor coefficients. It makes no unsigned or adversarial-coefficient cancellation claim, and has no asserted implication for physical circle moments.

## 6. Dependencies and exact artifacts used

1. `protocol.md`, SHA256 `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
2. `strategy/round231_residual_saving/briefs/blind_residual_statement.md`, SHA256 `8a9162e6f8f44fe97fa4213b3d2f8fe724d0b0417152b2f7d09cd6d26d4fb91f`.
3. Coordinator assignment message giving statement-only isolation, report path, and resource budget.
4. Mathematical inputs explicitly allowed by the brief: the divisor identity; bounded partial sums of \(\chi_4\); finite geometric sums; \(A(y)=\pi y+O(\sqrt y+1)\). The character-tail integral and mod-four identities were derived here.

No shared state, proof draft, validation matrix, synthesis, or legacy path was read or changed. The sole written artifact is this assigned report.

## 7. Recommended state effect

**Reject** any proposed uniform residual estimate with \(\kappa>1/20\) for the displayed actual coefficients and stated endpoint range. **Reject** the claim that subtracting only a scalar mean removes this obstruction: the fixed linear phase \(n/4\) survives every such subtraction on the same legal intervals.

**Retain** as an independently derived obstruction candidate pending the conductor's required seam review and graph validation. Make **no change** to claims of feasible positive saving, to estimates at or below \(1/20\), or to any downstream circle theorem. No next round is proposed by this task.
