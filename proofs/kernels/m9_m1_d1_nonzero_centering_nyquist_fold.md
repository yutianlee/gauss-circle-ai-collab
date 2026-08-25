# M9--M1 \(D=d=L=1\) nonzero centering and Nyquist-fold kernel

## Scope

Fix \(A>0\),

\[
 q=4N,\qquad K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\le K,
\]

and, for every odd \(d\mid N\), put

\[
 c=\frac qd,\qquad H=\frac c2,\qquad n=\frac Nd.
\]

The literal coefficient on one complete residue system is

\[
 B_j(x)=
 \mathbf 1_{x\ge1}\mathbf 1_{-x\le j\le x-1}
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right),
\tag{K157.1}
\]

with its inherited real off-congruence profile, exact complex phase,
all transitions, half-open endpoints, strict signed mask, and zero
extension.  Its physical support has \(O(KX^\varepsilon)\) integer
span and

\[
 \|w_U\|_\infty+\operatorname {Var}(w_U)
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{K157.2}
\]

This kernel concerns only the returned \(D=d=L=1\) outer-defect scalar.
The external \(B_{1,U}(1)\) factor is a separate assembly seam.

## 1. Exact nonzero centering

Let

\[
 G_N(t)=\mathbf 1_{N\mid t}\chi_4(t/N),\qquad
 A_j=\widehat B_j(0),\qquad
 \mathscr S_N(j)=\sum_{x\bmod q}G_N(x^2-j).
\]

The accepted complete half-period inverse-Gauss identity is

\[
\begin{aligned}
 &-\frac{i(1+i)}{2Nq}
 \sum_j\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c
 \sum_{v\bmod H}\widehat B_j(2dv)K(-v^2,-j;c)\\
 &\hspace{35mm}
 =\sum_j\sum_{x\bmod q}B_j(x)G_N(x^2-j).
\end{aligned}
\tag{K157.3}
\]

The accepted zero-row recombination is

\[
 \mathscr S_N(j)=
 -\frac{i(1+i)}{2N}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c\,K(0,-j;c).
\tag{K157.4}
\]

Subtracting the \(v=0\) term exactly once gives

\[
\boxed{
 \mathcal T_{\ne0,U}(V)=
 \sum_{V<|j|\le2V}\sum_{x\bmod q}
 \left(B_j(x)-\frac{A_j}{q}\right)G_N(x^2-j).}
\tag{K157.5}
\]

Equivalently,

\[
 \mathcal T_{\ne0,U}(V)=
 \sum_{V<|j|\le2V}\sum_{x\bmod q}
 B_j(x)\left(G_N(x^2-j)-\frac{\mathscr S_N(j)}q\right).
\tag{K157.6}
\]

Thus the centering constant is exactly \(q^{-1}=(4N)^{-1}\).
The constant tail is the closed zero row, its full-circle discrepancy
vanishes, and its sampled Fourier coefficient is zero at every
\(v\not\equiv0\pmod H\).

## 2. Complementary representatives and the single fold

Because the kernel depends on \(v^2\), every two-element orbit
\(\{v,H-v\}\), represented by \(1\le v<H/2\), contributes

\[
 \bigl(\widehat B_j(2dv)+\widehat B_j(-2dv)\bigr)
 K(-v^2,-j;c).
\tag{K157.7}
\]

The coefficient \(B_j\) is complex, so no conjugacy or doubled-real-part
identity is available.  Since \(H=2n\), the unique nonzero fixed point is

\[
 v=\frac H2=n,\qquad 2dv=2N=\frac q2.
\tag{K157.8}
\]

Its coefficient is the alternating mass

\[
 C_j=\widehat B_j(q/2)=\sum_{x\bmod q}(-1)^xB_j(x),
\tag{K157.9}
\]

and its literal normalized row is

\[
\mathcal F_U(V)=
-\frac{i(1+i)}{2Nq}
\sum_{V<|j|\le2V}
\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
\chi_4(d)d\sqrt c\,
C_jK(-n^2,-j;c).
\tag{K157.10}
\]

## 3. Target-safe Nyquist fold

For fixed \(j\), \(x\mapsto(x^2-j)/N\) is monotone on positive physical
support.  The zero-extended profile therefore retains the variation in
(K157.2).  The exact phase

\[
 f_j(x)=\sqrt{x^2-j}-x
\]

satisfies

\[
 |f_j'(x)|
 =\left|
 \frac{j}
 {\sqrt{x^2-j}\bigl(x+\sqrt{x^2-j}\bigr)}
 \right|
 \ll\frac V{K^2}.
\tag{K157.11}
\]

Across \(O(KX^\varepsilon)\) physical cells its variation is
\(O(X^\varepsilon)\), because \(V\le K\).  The nearest cell contributes
one spatial jump; every profile and support transition is already
charged by zero-extended variation.  Hence

\[
 \sup_x|B_j(x)|+\operatorname {Var}_x(B_j)
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{K157.12}
\]

Partial sums of \((-1)^x\) are bounded by one, so complex discrete Abel
summation yields

\[
 |C_j|\ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{K157.13}
\]

On either consecutive signed block put \(D_j=(-1)^jC_j\).  Its crude
variation is already sufficient:

\[
\begin{aligned}
 \sup_j|D_j|+\operatorname {Var}_j(D_j)
 &\le \sup_j|C_j|
 +\sum_j\bigl(|C_{j+1}|+|C_j|\bigr)\\
 &\ll_\varepsilon
 K M^{-3/4}X^\varepsilon.
\end{aligned}
\tag{K157.14}
\]

For every consecutive interval \(I\), opening the fold kernel gives

\[
\begin{aligned}
 \sum_{j\in I}(-1)^jK(-n^2,-j;c)
 &=
 \sum_{u\bmod c}^{*}
 \epsilon_u\left(\frac cu\right)e_c(-\bar u n^2)
 \sum_{j\in I}e_c((c/2-u)j).
\end{aligned}
\tag{K157.15}
\]

Here \(c/2\) is even and \(u\) is odd, so \(c/2-u\) is never zero
modulo \(c\).  In fact the shift permutes the unit residues.  Complete
periods vanish even when \(|I|>c\), and geometric summation gives

\[
 \sup_I\left|
 \sum_{j\in I}(-1)^jK(-n^2,-j;c)
 \right|
 \ll c\log(2c).
\tag{K157.16}
\]

Abel summation in \(j\), followed by restoration of every exterior
factor, now proves

\[
\begin{aligned}
 |\mathcal F_U(V)|
 &\ll_\varepsilon
 \frac{K M^{-3/4}}{Nq}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 d\,c^{3/2}X^\varepsilon\\
 &=
 \frac{K M^{-3/4}\sqrt q}{N}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}d^{-1/2}
 X^\varepsilon\\
 &\ll_\varepsilon M^{-1/4}X^\varepsilon.
\end{aligned}
\tag{K157.17}
\]

This proof is uniform in arbitrary \(N\), including \(c=4\), all
two-adic and repeated-prime strata, both signed blocks, and strict
endpoints.

## 4. Corrected selected-incidence capacity

On the selected graph, \(j=k^2-Nm\), and the asymmetric cell is

\[
 k^2-k+1\le Nm\le k^2+k.
\tag{K157.18}
\]

The upper endpoint for \(k\) is \(k^2+k\), and the lower endpoint for
\(k+1\) is \(k^2+k+1\).  These integer intervals partition the positive
integers.  Hence each positive \(m\) has exactly one \(k\), and then one
\(j\).  The physical profile supplies \(O(M)\) possible \(m\), while
the accepted all-parity root count supplies
\(O_\varepsilon(VX^\varepsilon)\) incidences.  Therefore

\[
 L_U(V)\ll_\varepsilon\min(M,V)X^\varepsilon.
\tag{K157.19}
\]

This is an unsigned support count.  Conditional on a genuine signed
square-root theorem, its coefficient-scale cost would be

\[
 M^{-3/4}L_U(V)^{1/2}X^\varepsilon
 \le M^{-1/4}X^\varepsilon
\tag{K157.20}
\]

for every allowed \(V\).  Thus the former capacity restriction
\(V\le M^{3/2}\) is obsolete at the literal selected level.  Equation
(K157.20) does not itself prove cancellation.

## 5. Remaining frontier

The centered identity and the fold estimate do not bound the paired
interior range

\[
 \sum_{v=1}^{H/2-1}
 \bigl(\widehat B_j(2dv)+\widehat B_j(-2dv)\bigr)
 K(-v^2,-j;c).
\tag{K157.21}
\]

The moving nearest-cell endpoint creates a diagonal atomic trace in the
mixed \(j\)-\(x\) difference.  The accepted one-variable BV data alone
permit mixed absolute capacity
\(VM^{-3/4}X^\varepsilon\), not
\(M^{-3/4}X^\varepsilon\).  Even granting the ideal mixed norm, ordinary
centered quadratic completion followed by absolute frequency summation
gives only

\[
 \sup_{I,J}|\mathscr D_N(I,J)|
 \ll \sqrt N\,\tau(N)(\log(2N))^2,
\tag{K157.22}
\]

and restores \(N^{1/2}M^{-3/4}X^\varepsilon\), outside the frozen
\(M\le N^{1/2}\) range.  These are route-scoped capacity statements,
not lower bounds or impossibility theorems.

The first open input is therefore a joint mask-preserving estimate for
the paired interior modes, or an exactly equivalent signed selected
incidence theorem retaining the literal profile, complex phase, both
signs, transitions, hard endpoints, all odd divisor strata, and the
external scalar seam.
