# Round 165 blind Fejer short-shift rederivation

## 1. Result

The short-shift form has two exact and useful coordinate systems, but neither
the stated \(L^2\) bound nor a one-variable treatment of the square-root phase
proves the frozen target.

The exact direct completion is

\[
 \frac1R\sum_{s\in\mathbb Z}
 \left|\sum_{j=0}^{R-1}c_{s+j}e(J\sqrt{s+j})\right|^2
 =\sum_N|c_N|^2+2\Re\mathfrak C_{R,J,L}.                 \tag{1}
\]

Thus the desired upper bound is a local Fejer-energy upper bound, not a
consequence of positivity. Positivity gives the opposite one-sided
inequality. In fact, realness, zero extension, shell support, and
\(\sum|c_N|^2\ll L^2X^\varepsilon\) alone admit bounded real countermodels
with \(\Re\mathfrak C\gg L^3\).

After opening the divisor atoms, put

\[
 a=d'-d,\qquad b=m'-m.
\]

Then \(a\) is even, \(b\equiv r\pmod2\), and

\[
 db+am+ab=db+a m'=r,\qquad
 \chi_4(d)\chi_4(d')=(-1)^{a/2}.                         \tag{2}
\]

This is a multiplicity-one parameterization. The monotone sector
\(a,b\geq0\) has only \(O(L^2)\) atom tuples and is therefore owner-complete
at the target power under the bounded-atom normalization in the packet;
the sector \(a,b\leq0\) is empty for \(r>0\). Consequently every sector of
raw \(L^3\) capacity has \(ab<0\).

There is also an exact gcd parameterization. With

\[
 g=(d,d'),\quad d=gu,\quad d'=gv,\quad (u,v)=1,\quad
 r=gh,
\]

one has

\[
 vm'-um=h,\qquad
 m=m_0+vt,\quad m'=m'_0+ut,                              \tag{3}
\]

and hence

\[
 N_t=A+Kt,\quad N_t+r=A+r+Kt,\quad K=guv=\frac{dd'}g,
 \quad \chi_4(d)\chi_4(d')=\chi_4(uv).                  \tag{4}
\]

The character is constant along \(t\). A geometric \(t\)-row has
\(O(g)\) points, and all gcd rows together have raw capacity \(O(L^3)\).
The first exact missing theorem is therefore the actual, one-sided signed
bound for the opposing-displacement aggregate defined in (16) below. It
must save one complete factor \(L\), while retaining the sum over
displacements (or, equivalently, over \(u,v\)); no shiftwise or tuplewise
absolute-value proof can do this.

## 2. Exact statement and hypotheses

Fix shell constants \(0<\alpha<\beta<\infty\), independent of
\(L,H,J,X\), so that every nonzero coefficient has

\[
 \alpha L^2\leq N\leq\beta L^2.
\]

Write the literal opened coefficient in the form

\[
 c_N={\bf1}_{\mu^2(N)=1}
 \sum_{\substack{d\mid N,\ d\ {\rm odd}\\
                  \sqrt N\leq d\leq2\sqrt N}}
 \chi_4(d)W_N(d),                                       \tag{5}
\]

where \(W_N(d)\) includes the selector, both parity branches, the fixed
profiles, hard point values, and zero extension. The phrase "bounded
normalized sum" is used here in its literal atom sense:

\[
 |W_N(d)|\ll_\varepsilon X^\varepsilon.                 \tag{6}
\]

Because there are only finitely many profile and hard-point labels, they may
instead be kept as separate atoms; all counts below merely acquire a fixed
factor. If (6) is not what the packet's normalization means, then the
monotone-sector conclusion must be withheld until the exact normalization is
supplied. The Fejer identity, both parameterizations, and the route no-go do
not use (6).

The divisor window is equivalently

\[
 \frac d4\leq m\leq d,\qquad \frac{d'}4\leq m'\leq d'.  \tag{7}
\]

There are constants \(0<\kappa<\mathcal K\), depending only on
\(\alpha,\beta\), for which every valid opened tuple satisfies

\[
 \kappa L\leq d,d',m,m'\leq\mathcal K L.                \tag{8}
\]

For example, one can take
\(\kappa=\sqrt\alpha/2\) and
\(\mathcal K=2\sqrt\beta\).

Squarefree support is literal. Thus \(d,m\) are squarefree and coprime,
as are \(d',m'\). Since \(d,d'\) are odd, any factor \(2\) occurs once in
\(m\) or \(m'\), and is never removed by a change of variables.

The exact target powers are

\[
 R=\lceil L\rceil\asymp L,\qquad
 \#\{N:N\asymp L^2\}=O(L^2),\qquad
 \Re\mathfrak C\ll_\varepsilon L^2X^\varepsilon.       \tag{9}
\]

Here \(J=\sqrt X\), \(H\leq J^{1/2}\), and \(L\ll H\), so
\(J\geq H^2\) and \(J/L^2\) is in the large-oscillation range. The
quantity \(H\) does not otherwise occur in the exact correlation, its
multiplicity, or its endpoint conditions; no \(H\)-saving is available from
the statement alone.

## 3. Proof and derivation

### 3.1 Exact real-part completion

Set \(z_N=c_Ne(J\sqrt N)\), with \(z_N=0\) outside the literal coefficient
domain. Expanding the left side of (1), each difference
\(r=j-k\) occurs \(R-|r|\) times. The diagonal is
\(\sum_N|c_N|^2\), and the \(r\) and \(-r\) terms are conjugates. Moreover,

\[
 z_{N+r}\overline{z_N}
 =c_{N+r}c_N e\!\left(J(\sqrt{N+r}-\sqrt N)\right)
 =c_{N+r}c_N e\!\left(\frac{Jr}{\sqrt{N+r}+\sqrt N}\right).
\]

This proves (1), including all shell endpoints: zero extension permits
\(s\in\mathbb Z\), and every diagonal coefficient is counted exactly \(R\)
times before division by \(R\).

The elementary Cauchy bound on (1) is

\[
 \frac1R\sum_s\left|\sum_{j<R}z_{s+j}\right|^2
 \leq R\sum_N|c_N|^2
 \ll_\varepsilon L^3X^\varepsilon.                     \tag{10}
\]

Hence a full factor \(L\) is missing. Also (1) gives only

\[
 \Re\mathfrak C\geq-\frac12\sum_N|c_N|^2,
\]

so positivity points in the wrong direction for the frozen upper bound.

### 3.2 Additive tangent coordinates

Every opened tuple has a unique pair
\(a=d'-d,\ b=m'-m\), and conversely a valid
\((a,b,d,m)\) reconstructs \(d',m'\) uniquely. Since \(d,d'\) are odd,
\(a=2q\) for a unique \(q\in\mathbb Z\). Direct expansion gives

\[
 (d+a)(m+b)-dm=db+am+ab=db+a m'=r.                      \tag{11}
\]

Reduction modulo \(2\) gives \(b\equiv r\pmod2\). For odd \(d\), adding
\(2q\) preserves its residue modulo \(4\) when \(q\) is even and swaps the
two odd residue classes when \(q\) is odd. Therefore

\[
 \chi_4(d)\chi_4(d+2q)=(-1)^q,                           \tag{12}
\]

which proves the character assertion in (2). In particular, there is no
remaining \(d\)-character oscillation on a fixed displacement row. The
only visible character cancellation is the alternating sign in \(q=a/2\).

For \(ab\ne0\), let
\(\delta=(|a|,|b|)\). The equation to solve is

\[
 bd+am=r-ab.                                             \tag{13}
\]

It is soluble in unrestricted integers exactly when \(\delta\mid r\),
because \(\delta\mid ab\). Given one solution \((d_0,m_0)\), every solution
occurs once as

\[
 d=d_0+\frac a\delta t,\qquad
 m=m_0-\frac b\delta t,\qquad t\in\mathbb Z.             \tag{14}
\]

The positivity, shell, divisor-window, squarefree, selector, and parity
conditions simply retain their literal subset of these \(t\)'s. If
\(a/\delta\) is odd, \(d\) odd retains one residue class of \(t\pmod2\); if
\(a/\delta\) is even, it retains all or none. When \(a=0\), (13) is
\(bd=r\) and \(m\) is free subject to the literal domain. When \(b=0\), it
is \(am=r\) and \(d\) is free. The case \(a=b=0\) is impossible because
\(r>0\).

There is an exact sparse sector. From (11), if \(a,b\leq0\), not both
zero, then \(r=db+a m'<0\), so no tuple exists. If \(a,b\geq0\), then (8)
and \(r<R\leq L+1\) imply

\[
 \kappa L(a+b)\leq r<L+1,\qquad
 a+b\leq\frac{L+1}{\kappa L}=O_{\alpha}(1).              \tag{15}
\]

There are therefore only \(O_{\alpha}(1)\) possible monotone displacement
pairs. For each pair there are \(O(L)\) choices for \(d\) and \(O(L)\)
choices for \(m\), while \(d',m',r\) are then fixed. Thus the total atom
capacity is \(O(L^2)\). Under (6), the whole monotone sector is
\(O_\varepsilon(L^2X^\varepsilon)\), even for adversarial phases and signs.
This is a capacity bound for the already isolated sparse sector; no
\(\sum_r|\cdot|\) or tuplewise bound is inserted into the \(L^3\)-capacity
complement.

Define \(\mathcal U_q\) to be the set of all literal valid opened tuples
with \(a=2q\), \(ab<0\), and
\(r=d'm'-dm\in\{1,\ldots,R-1\}\), including all profile and parity atoms.
Put

\[
 B_q=\sum_{(d,m,d',m')\in\mathcal U_q}
 \left(1-\frac rR\right)
 W_{dm}(d)W_{d'm'}(d')
 e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right).               \tag{16}
\]

Then, with no multiplicity and no absolute values around shifts or tuples,

\[
 \mathfrak C_{\rm opp}=\sum_{0<|q|\ll L}(-1)^qB_q.       \tag{17}
\]

The exact remaining theorem is

\[
 \boxed{\ \Re\sum_{0<|q|\ll L}(-1)^qB_q
          \ll_\varepsilon L^2X^\varepsilon.\ }          \tag{18}
\]

Together with the monotone sector, (18) proves the frozen target.

### 3.3 Gcd-progression coordinates and phase powers

Let \(g=(d,d')\), \(d=gu\), \(d'=gv\). Then \(g,u,v\) are odd,
\((u,v)=1\), and the product-difference equation forces \(g\mid r\).
Writing \(r=gh\) gives \(vm'-um=h\). Choose the unique
\(m_0\in\{0,\ldots,v-1\}\) satisfying

\[
 um_0\equiv-h\pmod v,
\]

and put \(m'_0=(um_0+h)/v\). All solutions are exactly (3), and

\[
 A=gu m_0,\qquad K=guv,\qquad
 N_t=A+Kt,\qquad N_t+r=A+r+Kt.
\]

This proves (4) and gives a bijection: a tuple determines
\((g,h,u,v,t)\) uniquely, and a literal valid such quintuple reconstructs
one tuple. Because \(g\) is odd,

\[
 m'-m\equiv h\equiv r\pmod2.
\]

Squarefree support requires, in particular, \(g,u,v\) squarefree and
pairwise coprime, \(m,m'\) squarefree,
\((gu,m)=1\), and \((gv,m')=1\). These are restrictions on the literal
\(t\)-set; they are not replaced by density factors.

From (8), \(g\leq r<R\),

\[
 u,v\asymp\frac Lg,\qquad K=guv\asymp\frac{L^2}g,\qquad
 1\leq h<\frac Rg.                                      \tag{19}
\]

The geometric domain before squarefree and selector deletions is an
intersection of intervals in \(t\). Since \(m\) advances by
\(v\gg L/g\), while its allowed range has length \(O(L)\), it has

\[
 \#\mathcal T_{g,u,v,h}=O(g).                            \tag{20}
\]

For a fixed \(g\), the numbers of \(u,v,h\) are respectively
\(O(L/g),O(L/g),O(L/g)\). Thus the exact raw-capacity ledger is

\[
 \sum_{g\ll L}O\!\left(
     \frac Lg\frac Lg\frac Lg\,g\right)
 =O\!\left(L^3\sum_{g\geq1}\frac1{g^2}\right)
 =O(L^3).                                                \tag{21}
\]

Coprimality, squarefreeness, endpoints, and selectors can only delete
tuples from this count. Equation (21) displays the exact missing factor
\(L\).

The character becomes

\[
 \chi_4(gu)\chi_4(gv)=\chi_4(g)^2\chi_4(uv)=\chi_4(uv), \tag{22}
\]

so it is constant on every \(t\)-row. Put \(x=A+Kt\) and

\[
 \Phi(t)=J(\sqrt{x+r}-\sqrt x).
\]

The derivatives are exactly

\[
\begin{aligned}
 \Phi'(t)
 &=\frac{JK}{2}\big((x+r)^{-1/2}-x^{-1/2}\big),\\
 \Phi''(t)
 &=\frac{JK^2}{4}\big(x^{-3/2}-(x+r)^{-3/2}\big),\\
 \Phi'''(t)
 &=\frac{3JK^3}{8}\big((x+r)^{-5/2}-x^{-5/2}\big).
\end{aligned}                                           \tag{23}
\]

On the shell, with \(r=gh\) and (19), their sizes are

\[
 |\Phi'|\asymp\frac{Jh}{L},\qquad
 \Phi''\asymp\frac{Jh}{gL},\qquad
 |\Phi'''|\asymp\frac{Jh}{g^2L}.                        \tag{24}
\]

These are derivative sizes in the integer variable \(t\), not distances
to integers. On a nondegenerate row of length comparable to \(g\), the
derivative image has length comparable to \(Jh/L\). Since
\(g\leq L/h\) and \(J\geq H^2\gg L^2\), the curvature scale satisfies

\[
 \Phi''\gg \frac{Jh^2}{L^2},                             \tag{25}
\]

which is large, not a small-curvature regime.

A one-dimensional Poisson or van der Corput \(B\)-process followed by
absolute values cannot furnish the missing saving. On a full row it has
about \(Jh/L\) stationary integer frequencies. A single stationary term
has natural size

\[
 (\Phi'')^{-1/2}\asymp\left(\frac{gL}{Jh}\right)^{1/2}.
\]

Their absolute dual mass is therefore

\[
 \frac{Jh}{L}\left(\frac{gL}{Jh}\right)^{1/2}
 =\left(\frac{Jgh}{L}\right)^{1/2},                     \tag{26}
\]

whose ratio to the trivial row length \(g\) is

\[
 \left(\frac{Jh}{gL}\right)^{1/2}\gg1.                  \tag{27}
\]

Moreover, the squarefree and selector restrictions generally leave a
non-smooth subset of the \(t\)-interval. Thus a \(t\)-transform must first
preserve this arithmetic and must then retain cancellation among its many
dual modes. Treating the modes separately is a rigorous route no-go at the
power ledger (26)--(27).

## 4. First doubtful or unproved step

The first unproved mathematical statement is (18). Two plausible sources
of cancellation are visible, but neither is supplied by the packet:

1. In tangent coordinates, the entire character is the alternating sign
   \((-1)^q\). If \(B_q\) is extended by zero outside its literal range, a
   sufficient theorem, separately on \(q>0\) and \(q<0\), would be

   \[
    \sum_q|B_{q+1}-B_q|
    \ll_\varepsilon L^2X^\varepsilon.                   \tag{28}
   \]

   Alternating summation would then prove (18). But changing \(q\) changes
   the Diophantine progression, shell endpoints, squarefree rows, and the
   Boolean selectors. No bounded-variation or two-step invariance of these
   data is stated. The raw bound for the left side of (28) remains
   \(O(L^3X^\varepsilon)\).

2. In gcd coordinates, one could retain the two-variable sign
   \(\chi_4(uv)\) and seek a bilinear estimate before resolving \(t\).
   However, the \(t\)-row has no character oscillation, and its endpoints
   and deleted points depend jointly on \(u,v,g,h\). Cauchy followed by
   the row capacity (21), or a \(t\)-Poisson transform followed by absolute
   dual modes, does not save \(L\).

Therefore a proof needs an actual arithmetic theorem that couples the
squarefree/selector weights across adjacent displacement classes, or a
genuinely aggregate bilinear estimate in \(u,v\) that retains cancellation
among all dual modes. A bound for each \(r\), each tuple, each \(t\)-row,
or each dual frequency cannot meet the frozen exponent ledger.

There is also a definition seam: the target-power monotone sector uses the
uniform normalized-atom interpretation (6). The full coefficient formula
must be checked to confirm that no profile normalization introduces an
extra positive power of \(L\).

## 5. Required control test and outcome

An exact phase-aligned real-sequence control shows that (1) plus the stated
\(L^2\) norm cannot prove the target. Let \(\mathcal I\) be an integer
interval of length \(M\asymp L^2\) in the shell and, for
\(\alpha_0\in[0,1)\), set

\[
 c_N^{(\alpha_0)}=
 \begin{cases}
 \cos\big(2\pi(J\sqrt N-\alpha_0)\big),&N\in\mathcal I,\\
 0,&N\notin\mathcal I.
 \end{cases}                                             \tag{29}
\]

This sequence is real, bounded, zero-extended, shell-supported, and has
\(\sum|c_N^{(\alpha_0)}|^2\leq M\). For a window beginning at \(s\), let

\[
 n_s=|\mathcal I\cap[s,s+R-1]|,\qquad
 D_s(\alpha_0)=
 \sum_{N\in\mathcal I\cap[s,s+R-1]}
 \cos^2\big(2\pi(J\sqrt N-\alpha_0)\big).
\]

The projection in the direction \(e(\alpha_0)\) gives

\[
 \left|\sum_{N\in[s,s+R-1]}c_N^{(\alpha_0)}e(J\sqrt N)\right|^2
 \geq D_s(\alpha_0)^2.
\]

Averaging in \(\alpha_0\),

\[
 \mathbb E_{\alpha_0}D_s=\frac{n_s}{2},\qquad
 \mathbb E_{\alpha_0}D_s^2\geq\frac{n_s^2}{4}.
\]

If \(M\geq2R\), there are \(M-R+1\) full windows, and hence some
\(\alpha_0\) satisfies

\[
 \frac1R\sum_s
 \left|\sum_{j<R}c_{s+j}^{(\alpha_0)}e(J\sqrt{s+j})\right|^2
 \geq\frac{(M-R+1)R}{4}\geq\frac{MR}{8}.                \tag{30}
\]

For \(R\geq16\), (1), (29), and (30) give

\[
 \Re\mathfrak C_{R,J,L}\geq\frac{MR}{32}\asymp L^3.     \tag{31}
\]

Outcome: the norm-only/direct-completion route fails exactly by one factor
\(L\). This control is not asserted to be an actual divisor coefficient;
it proves precisely that the divisor character and selector algebra must be
used. The parity control passes in both coordinate systems:
\(b\equiv r\pmod2\) in (11) and
\(m'-m\equiv h\equiv r\pmod2\) in (3). The character controls also agree:
\(\chi_4(uv)=(-1)^{(d'-d)/2}\).

## 6. Dependencies and exact artifacts used

Only the following two artifacts were read, as required by statement-only
isolation:

1. protocol.md.
2. rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/blind_statement.md.

No proof graph, campaign manifest, strategy, conductor seed, earlier round,
kernel, sibling report, or external source was used. No numerical
experiment was used; the allocation is \(100\%\) algebraic/analytic and
\(0\%\) numerical.

## 7. Recommended state effect

**Retain and seam-review** the exact completion (1), tangent bijection
(11)--(14), gcd bijection (3)--(4), character identities (12) and (22),
the monotone-sector \(O(L^2)\) capacity result, and the derivative/capacity
ledger (19)--(27). The monotone-sector promotion should wait only for a
definitions review confirming the atom bound (6).

**Do not promote** the frozen target. Record (18) as the first exact missing
theorem. Reject as proof routes: norm-only Fejer completion, character
cancellation along an individual \(t\)-row, and one-dimensional Poisson
followed by absolute values of its dual modes. A next attack should test
the aggregate two-step displacement variation (28), or formulate a
bilinear \(\chi_4(uv)\) theorem that keeps the squarefree selectors and dual
modes coupled.
