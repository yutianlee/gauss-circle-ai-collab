# Round 231: independent weighted squarefree shell mass

Campaign: round231_harmonic_admission (selection only).  
Task and role: blind_squarefree_mass; statement-only independent arithmetic rederiver.  
Generated: 2026-10-11 02:59:32 UTC.  
Supplied graph provenance tag (not independently read): `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

## 1. Result

The proposed statement holds for every fixed real shell (0<u<v). An elementary union bound pays every possible prime-square divisor and leaves an explicit positive proportion:

\[
\sum_{\substack{uT\le n\le vT\\n\text{ squarefree}}}r(n)
\ge \frac{\pi(v-u)}{24}T
-10E\sqrt{vT}\bigl(1+\log\sqrt{vT}\bigr),
\qquad vT\ge4,
\]

where the absolute constant (E) is specified below from the supplied lattice-count estimate. In particular, one can take

\[
c_{u,v}=\frac{\pi(v-u)}{48}>0
\]

for all sufficiently large real (T). No squarefree-density theorem, prime-number estimate, numerical simulation, or external source is used.

## 2. Exact statement and hypotheses

Let (\chi_4) be the real character modulo (4), and for positive integers define

\[
r(n)=4\sum_{d\mid n}\chi_4(d),\qquad
S(x)=\sum_{1\le n\le x}r(n)\quad(x\ge0).
\]

Use the supplied elementary fact that there exists an absolute (C\ge1) with

\[
|S(x)-\pi x|\le C(\sqrt{x}+1)\qquad(x\ge0).
\]

Fix such a (C), and put (E=\pi+2C). The claimed explicit error bound holds for every real (T>0) satisfying (vT\ge4). A sufficient threshold for the asserted linear lower bound is

\[
T\ge T_0(u,v):=
\max\left\{\frac4v,
\left(\frac{960E v^{3/4}}{\pi(v-u)}\right)^4\right\}.
\]

Squarefree means not divisible by (p^2) for any prime (p), and both interval endpoints are included. The dependence of (T_0) on (v-u) is permitted: the statement concerns each fixed shell, not a family whose width shrinks with (T).

## 3. Proof or derivation

**Coefficient domination, including possible zero factors.** Write (f(n)=r(n)/4). By unique factorization and complete multiplicativity of the character,

\[
f(n)=\prod_{p^e\Vert n}f(p^e),\qquad
f(p^e)=\sum_{j=0}^{e}\chi_4(p)^j
=\begin{cases}
1,&p=2,\\
e+1,&p\equiv1\pmod4,\\
1,&p\equiv3\pmod4,\ e\text{ even},\\
0,&p\equiv3\pmod4,\ e\text{ odd}.
\end{cases}
\]

All local factors are nonnegative. At (2), adding two to the valuation changes no local factor, so

\[
r(4m)=r(m)\qquad(m\ge1).
\]

For (p\equiv3\pmod4), adding two preserves parity, and therefore (r(p^2m)=r(m)). This equality includes the zero case. For (p\equiv1\pmod4), if (p^e\Vert m), then (e+3\le3(e+1)). Multiplication by the remaining nonnegative local factors proves

\[
0\le r(p^2m)\le3r(m)\qquad(p\text{ any odd prime},\ m\ge1).
\]

No division by (r(m)) is used, so vanishing representation counts cause no exception.

**Real endpoints with a uniform interval error.** For (0<a<b), set

\[
R(a,b)=\sum_{a\le m\le b}r(m),\qquad a_*:=\lceil a\rceil-1.
\]

Here (a_*\ge0), (0<a-a_*\le1), and the exact identity

\[
R(a,b)=S(b)-S(a_*)
\]

includes the lower endpoint even when it is an integer. Since (a_*\le b),

\[
\begin{aligned}
|R(a,b)-\pi(b-a)|
&\le\pi(a-a_*)+C(\sqrt b+1)+C(\sqrt{a_*}+1)\\
&\le\pi+2C(\sqrt b+1)\\
&\le E(\sqrt b+1).
\end{aligned}
\]

This also covers rescaled intervals below (1), including intervals containing no positive integer.

**An elementary strict saving in the square-divisibility union.** For integers (k\ge2),

\[
\frac1{(2k+1)^2}\le\frac1{4k(k+1)}
=\frac14\left(\frac1k-\frac1{k+1}\right).
\]

Consequently,

\[
\sum_{\substack{j\ge3\\j\text{ odd}}}\frac1{j^2}
\le \frac19+\frac14\sum_{k=2}^{\infty}
\left(\frac1k-\frac1{k+1}\right)
=\frac19+\frac18=\frac{17}{72}.
\]

In particular, without needing any distribution theorem for primes,

\[
\frac14+3\sum_{\substack{p\text{ odd}\\p\text{ prime}}}\frac1{p^2}
\le\frac14+3\cdot\frac{17}{72}
=\frac{23}{24}<1.
\]

The saving is the exact rational number (1/24); its strict positivity has no numerical-verification dependency.

**Payment of every prime and every error.** Put (N=\sqrt{vT}\ge2), (L=\pi(v-u)T), and let (B(T)) be the (r)-weighted mass of nonsquarefree positive integers in ([uT,vT]). Every such integer has a prime-square divisor with (p\le N). Nonnegativity and the coefficient estimates give the full finite union bound

\[
\begin{aligned}
B(T)
&\le R(uT/4,vT/4)
 +3\sum_{\substack{3\le p\le N\\p\text{ prime}}}
 R(uT/p^2,vT/p^2)\\
&\le L\left(\frac14+3\sum_{\substack{3\le p\le N\\p\text{ prime}}}\frac1{p^2}\right)
 +E(N/2+1)
 +3E\sum_{\substack{3\le p\le N\\p\text{ prime}}}(N/p+1)\\
&\le \frac{23}{24}L
 +E(N/2+1)+3EN(1+\log N)+3EN.
\end{aligned}
\]

For the last line, the number of listed odd primes is at most (N), and

\[
\sum_{\substack{3\le p\le N\\p\text{ prime}}}\frac1p
\le\sum_{j=1}^{\lfloor N\rfloor}\frac1j
\le1+\log N.
\]

Thus the (+1) error from each rescaled interval is paid over the entire prime range, while the square-root error is paid by a finite harmonic sum. There is no unestimated tail: primes above (N) cannot divide these integers to second order. Extending the reciprocal-square main term to all odd positive integers only increases its upper bound. Multiple prime-square divisibility is deliberately overcounted, which is valid because all weights are nonnegative.

Subtracting from the total interval mass (R(uT,vT)\ge L-E(N+1)) yields

\[
\begin{aligned}
\sum_{\substack{uT\le n\le vT\\n\text{ squarefree}}}r(n)
&\ge \frac{L}{24}
-E\left[\left(\frac{15}{2}+3\log N\right)N+2\right]\\
&\ge \frac{L}{24}-10EN(1+\log N).
\end{aligned}
\]

The last inequality holds for (N\ge2). This proves the explicit error estimate in Section 1. To obtain the stated sufficient threshold, use (1+\log N\le2\sqrt N) for (N\ge1); for example the difference (2\sqrt N-1-\log N) has nonnegative derivative and is positive at (1). Hence the error is at most (20E(vT)^{3/4}). The definition of (T_0) makes this at most (\pi(v-u)T/48), leaving the claimed lower bound with (c_{u,v}=\pi(v-u)/48).

## 4. First doubtful or unproved step

There is no remaining doubtful step in this isolated implication from the stated elementary inputs. The absolute constant (C) is not given a numerical value because the supplied lattice-count estimate states it only existentially; both the error constant and a sufficient threshold have been expressed explicitly in terms of (C). A numerical value for (C) is unnecessary for the required theorem.

This result has no asserted consequence for any unstated harmonic, signed, resonance, endpoint, or pointwise estimate.

## 5. Required control test and outcome

All controls were exact analytical checks; no asymptotic simulations or numerical experiments were performed.

1. **Actual prime (2): pass.** The factor is exactly (1), so its main-term cost is (1/4). Using the odd-prime factor (3) at (2) would destroy the displayed saving; the proof explicitly does not do that. For instance (r(4)=r(1)=4).
2. **Sharp split-prime domination: pass.** For (p=5,m=1), (r(25)=12=3r(1)). Thus the general odd-prime constant (3) is genuinely needed, and is derived rather than assumed.
3. **Inert-prime and zero-weight cases: pass.** The local formula gives (r(9)=r(1)=4), and (r(27)=r(3)=0). The proof works by multiplication of local inequalities and never divides by a zero weight.
4. **Every fixed narrow shell: pass.** The main term is proportional to (v-u>0); all error bounds are uniform for that fixed pair. The explicit threshold grows as the shell narrows, as allowed by the statement.
5. **Both real endpoints and small rescaled intervals: pass.** The exact identity with (a_*\) includes integers at either endpoint; for example (R(1,1.5)=S(1.5)-S(0)). The same identity applies when the rescaled interval contains no positive integer. In particular (p=N), when it is a prime integer, is included in the union.
6. **Whole union, overlap, and accumulated errors: pass.** All primes through (N), including those comparable to (N), are counted. The aggregate (+1) contribution is (O(N)), and the aggregate square-root contribution is (O(N\log N)). There is no truncation-and-tail exchange.
7. **Strict positivity: pass.** The explicit rational inequality (1-(1/4+3\cdot17/72)=1/24>0) establishes the saving without approximating any constant.

## 6. Dependencies and exact artifacts used

The only repository files read were:

- `protocol.md`;
- `strategy/round231_harmonic_admission/briefs/blind_squarefree_mass.md`;
- `strategy/round231_harmonic_admission/briefs/blind_squarefree_statement.md`.

The mathematical dependencies are the supplied definition of (r), the supplied summatory estimate, elementary properties of the character and prime factorization, telescoping series, the elementary harmonic-sum bound, and elementary real inequalities. The supplied representation-count identity is consistent with nonnegativity, which was also derived directly from the local factors. The supplied divisor bound is not needed.

No proof graph, history, sibling report, source search, or external theorem was consulted. No child task was launched because preserving the specified independent isolation was part of this task. Analytical/algebraic work accounted for all mathematical work; computation was limited to artifact writing and its final file hash. Only the assigned report was written.

## 7. Recommended state effect

**Promote the isolated arithmetic lemma after the conductor's required review.** The exact proposed input is proved, with a full prime-square union, real-endpoint control, and a quantitative positive constant for every fixed shell. This report is candidate evidence only; it neither changes the authoritative graph nor promotes any unstated downstream claim. No next-round recommendation or shared-state edit is made.
