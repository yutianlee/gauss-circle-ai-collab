# Centered nonzero root-discrepancy attack

## 1. Result

The exact physical centering identity is valid, with centering constant
exactly \(1/q=1/(4N)\). Put

\[
 q=4N,\qquad c=\frac qd,\qquad H=\frac c2,
 \qquad A_j=\widehat B_j(0),
\]

and

\[
 G_N(t)=\mathbf{1}_{N\mid t}\chi _4(t/N),\qquad
 \mathscr S_N(j)=\sum_{x\bmod q}G_N(x^2-j).
\]

Then, for each of the two signed blocks \(V<|j|\leq 2V\),

\[
\boxed{
\begin{aligned}
 \mathcal T_{\ne0,U}(V)
 &=-\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\leq2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi _4(d)d\sqrt c
 \sum_{\substack{v\bmod H\\v\ne0}}
 \widehat B_j(2dv)K(-v^2,-j;c) \\
 &=\sum_{V<|j|\leq2V}\sum_{x\bmod q}
 \left(B_j(x)-\frac{A_j}{q}\right)G_N(x^2-j) \\
 &=\sum_{V<|j|\leq2V}\sum_{x\bmod q}
 B_j(x)\left(G_N(x^2-j)-\frac{\mathscr S_N(j)}q\right).
\end{aligned}}
\tag{157.R1}
\]

Thus the global constant tail is neither deleted nor estimated by a
pointwise shortcut: it is exactly the already closed zero row. It is a
full-\(x\) direction annihilated by the centered discrepancy. At every
nonzero theta frequency it has zero Fourier coefficient, so centering
does not alter any \(v\ne0\) coefficient.

The literal two-variable variation does **not** follow from the accepted
one-variable BV statement. On the unique physical lift \(x=k>0\), the
nearest-cell mask is

\[
 -x\leq j\leq x-1,
 \qquad
 \lambda_+(j)=j+1,\quad \lambda_-(j)=-j,
\tag{157.R2}
\]

so a unit change in \(j\) moves one spatial endpoint by one integer. The
exact \(j\)-difference of every nonzero Fourier coefficient contains the
Fourier transform of that lost or gained point, of constant modulus at
all \(H-1\) nonzero sampled frequencies. Equivalently, the mixed
rectangular difference contains a diagonal atomic trace. The constant
tail has zero mixed \(x\)-difference and cannot cancel that trace. The
available profile facts give the trace only the capacity

\[
 \mathfrak C_{\mathrm{cell}}(V)\ll_\varepsilon
 V M^{-3/4}X^\varepsilon,
\tag{157.R3}
\]

not the \(M^{-3/4}X^\varepsilon\) mixed norm required by the proposed
rectangular reduction. A sharp moving-cell control model below shows
that the loss \(V\) cannot be removed from the accepted one-dimensional
BV hypotheses alone.

Even if one grants the ideal, unproved mixed norm
\(M^{-3/4}X^\varepsilon\), elementary two-parameter completion gives
only

\[
 \boxed{
 \sup_{I,J}|\mathscr D_N(I,J)|
 \ll \sqrt N\,\tau(N)(\log(2N))^2,}
\tag{157.R4}
\]

for consecutive residue and defect intervals. Restoring the literal
amplitude gives \(N^{1/2}M^{-3/4}X^\varepsilon\), which would be
target-sized only for \(M\geq N^{2/3-o(1)}\), outside the frozen
\(M\leq N^{1/2}\) range. Centering removes the exact spatial zero mode,
but the first nonzero completion modes and the low-\(v\)/complementary
wrapped branches remain.

There is an important corrected capacity. The exact nearest-cell
intervals partition the positive integers, so the selected \(M\)-block
has

\[
 L_U(V)\ll_\varepsilon \min(M,V)X^\varepsilon
\tag{157.R5}
\]

actual incidences, not merely \(O(VX^\varepsilon)\). Hence a *proved*
square-root signed incidence theorem would give

\[
 M^{-3/4}L_U(V)^{1/2}X^\varepsilon
 \leq M^{-1/4}X^\varepsilon
\tag{157.R6}
\]

for every \(V\), with no \(V\leq M^{3/2}\) restriction. No such signed
theorem is presently available; (157.R6) is a corrected capacity, not a
gain. Consequently this report proves no full target and no strict
owner-complete positive-power range. It establishes a route-scoped
mixed-variation and restored-power obstruction: the current data are
insufficient for the proposed centered-rectangle/fixed-\(v\) attacks,
without asserting impossibility of a theorem for the literal
coefficient.

## 2. Exact statement and hypotheses

Let \(X\geq2\), \(N=\lfloor X\rfloor\), \(R=X^{1/4}\), and retain the
frozen \(D=d=L=1\) outer-defect range

\[
 1\ll M\leq R^2\asymp N^{1/2},\qquad
 J_A=M^{3/4}(\log(2X))^A<V\leq K=\sqrt{NM}.
\tag{157.R7}
\]

The literal coefficient \(B_j(x)\) is the Round-154--156 ambient
pre-linearization coefficient: it retains the exact residual phase
\(e(\sqrt{x^2-j}-x)\), the zero-extended real profile, its actual
components and transitions, the strict \(j\)-mask, the asymmetric cell
\(-x\leq j\leq x-1\), both signs, and all physical and hard endpoints.
The external \(B_{1,U}(1)\) factor remains outside and costs only
\(X^\varepsilon\). The accepted scale ledger is

\[
 \|B_j\|_\infty+\operatorname {Var}_x B_j
 \ll_\varepsilon M^{-3/4}X^\varepsilon,
 \qquad \#\operatorname {supp}_xB_j\ll K,
\tag{157.R8}
\]

and, with \(A_j=\sum_{x\bmod q}B_j(x)\),

\[
 \sup_j|A_j|+\operatorname {Var}_jA_j
 \ll_\varepsilon K M^{-3/4}X^\varepsilon.
\tag{157.R9}
\]

The phase part of (157.R8) is literal rather than linearized: on support

\[
 \left|\partial_x(\sqrt{x^2-j}-x)\right|
 \ll \frac V{K^2},
 \qquad
 \left|\partial_j(\sqrt{x^2-j}-x)\right|
 \ll \frac1K,
\tag{157.R10}
\]

and \(V\leq K\). Profile and zero-extension jumps are charged to their
actual total variation.

For consecutive cyclic \(I\subset\mathbb Z/q\mathbb Z\) and a
consecutive interval \(J\) contained in one signed defect block, define

\[
 H_N(j,x)=G_N(x^2-j)-\frac{\mathscr S_N(j)}q,
 \qquad \sum_{x\bmod q}H_N(j,x)=0,
\tag{157.R11}
\]

and

\[
 \mathscr D_N(I,J)=\sum_{j\in J}\sum_{x\in I}H_N(j,x).
\tag{157.R12}
\]

For a coefficient array zero-extended past the two \(j\)-endpoints and
viewed cyclically in \(x\), set

\[
 \mathfrak V_\square(B)
 =\sum_{j\in\mathbb Z}\sum_{x\bmod q}
 |\Delta_j\Delta_xB_j(x)|.
\tag{157.R13}
\]

This is a genuine mixed rectangular norm. It is not the same as
\(\sum_j\|B_j\|_{BV_x}\),
\(\sum_x\|B_\bullet(x)\|_{BV_j}\), or the BV norm of the row sums
\(A_j\). Double discrete Abel summation gives

\[
 \left|\sum_{j,x}B_j(x)H_N(j,x)\right|
 \leq \mathfrak V_\square(B)
 \sup_{I,J}|\mathscr D_N(I,J)|,
\tag{157.R14}
\]

up to an absolute convention-dependent endpoint factor. Zero extension
in \(j\) includes the strict block endpoints. Since \(K<N<q\), the
physical support has a unique nonwrapping lift; cyclic intervals also
cover a possible residue cut.

The no-go statement proved here is method-specific and exact:

* the accepted one-variable profile facts do not imply
  \(\mathfrak V_\square(B)\ll M^{-3/4}X^\varepsilon\), because the
  literal moving cell has the diagonal trace (157.R3);
* ordinary centered quadratic completion proves only (157.R4), whose
  fully restored power is outside the target range even if the ideal
  mixed norm is granted; and
* fixed-\(v\) Abel, one-dimensional Fourier \(L^1\), physical-fold
  Parseval, and termwise completion have the capacities printed below
  and yield no positive-power enlargement beyond the accepted collar.

This does not assert that the signed matrix is large and does not rule
out a mask-preserving joint \(j\)-\(v\), diagonal-cell, or selected
incidence theorem.

## 3. Proof or derivation

**Exact nonzero projection and the \(1/q\) constant.** Complete
half-period resummation, with all the factors retained, gives

\[
 -\frac{i(1+i)}{2Nq}
 \sum_j\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi _4(d)d\sqrt c
 \sum_{v\bmod H}\widehat B_j(2dv)K(-v^2,-j;c)
 =\sum_j\sum_{x\bmod q}B_j(x)G_N(x^2-j).
\tag{157.R15}
\]

The accepted Round-156 recombination is

\[
 \mathscr S_N(j)
 =-\frac{i(1+i)}{2N}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi _4(d)d\sqrt c\,K(0,-j;c).
\tag{157.R16}
\]

Consequently the \(v=0\) term in (157.R15) is exactly

\[
 -\frac{i(1+i)}{2Nq}
 \sum_j\sum_d\chi _4(d)d\sqrt c\,A_jK(0,-j;c)
 =\frac1q\sum_jA_j\mathscr S_N(j).
\tag{157.R17}
\]

Subtracting (157.R17) from (157.R15) proves (157.R1), including every
odd \(d\mid N\). The equality uses the exact gcd partition
\(d=(h,N)\), \(h=da\), so no imprimitive stratum is discarded. Also

\[
 \sum_{x\bmod q}\left(B_j(x)-\frac{A_j}q\right)=0.
\tag{157.R18}
\]

For \(v\not\equiv0\pmod H\),

\[
 \sum_{x\bmod q}\frac{A_j}q e_q(-2dv x)=0,
 \qquad
 2dv\equiv0\pmod q\iff v\equiv0\pmod H.
\tag{157.R19}
\]

Thus
\(\widehat{B_j-A_j/q}(2dv)=\widehat B_j(2dv)\) at every literal
nonzero mode. The constant tail has pointwise size at most
\(KM^{-3/4}/q\), spatial \(L^1\)-mass \(|A_j|\), and row variation
capacity (157.R9); it is nevertheless a full-circle direction for
which \(\mathscr D_N(\mathbb Z/q\mathbb Z,J)=0\). Equivalently,

\[
 \Delta_j\Delta_x(B_j-A_j/q)=\Delta_j\Delta_xB_j
\tag{157.R20}
\]

with cyclic \(x\)-difference. This is the exact constant-tail ledger.

**Literal mixed variation and the asymmetric cell.** For \(x>0\), the
two cell inequalities are exactly equivalent to
\(x\geq j+1\) on the positive block and \(x\geq-j\) on the negative
block. Remove only this lower-cell indicator from the literal formula
and call the remaining zero-extended coefficient \(F_j(x)\). This is
an exact factorization: every lower and upper physical-profile endpoint,
every internal profile component and transition, and every hard support
endpoint remains in \(F_j\). In particular, if an upper endpoint moves
with \(j\), its gained or lost point occurs in
\(F_{j+1}-F_j\) below and must be charged as an additional transition
trace; it is not treated as fixed. Thus, on the physical lift,

\[
 B_j(x)=\mathbf{1}_{x\geq\lambda_\sigma(j)}F_j(x),
 \quad
 \lambda_+(j)=j+1,\quad \lambda_-(j)=-j,
\tag{157.R21}
\]

For a positive block, \(\lambda_+(j+1)=\lambda_+(j)+1\), and for every
frequency \(r\bmod q\) the exact difference is

\[
\begin{aligned}
 \widehat B_{j+1}(r)-\widehat B_j(r)
 &=-F_j(\lambda_+(j))e_q(-r\lambda_+(j))\\
 &\quad+\sum_{x\geq\lambda_+(j)+1}
 \big(F_{j+1}(x)-F_j(x)\big)e_q(-rx).
\end{aligned}
\tag{157.R22}
\]

For a negative block, \(\lambda_-(j+1)=\lambda_-(j)-1\), and

\[
\begin{aligned}
 \widehat B_{j+1}(r)-\widehat B_j(r)
 &=F_{j+1}(\lambda_-(j)-1)e_q(-r(\lambda_-(j)-1))\\
 &\quad+\sum_{x\geq\lambda_-(j)}
 \big(F_{j+1}(x)-F_j(x)\big)e_q(-rx).
\end{aligned}
\tag{157.R23}
\]

The first line in each formula is the exact diagonal cell trace. At
\(r=2dv\), its phase is \(e_c(-2v\lambda_\sigma(j))\) and its modulus is
independent of \(v\). Define

\[
 \mathfrak C_\sigma(V)
 =\sum_{\substack{j\ \mathrm{in\ the\ signed\ block}}}
 |F_j(\lambda_\sigma(j))|,
\tag{157.R24}
\]

with the evident shifted value in (157.R23). Literal amplitude gives
only

\[
 \mathfrak C_\sigma(V)\ll_\varepsilon
 VM^{-3/4}X^\varepsilon.
\tag{157.R25}
\]

Before any new cancellation with the bulk term or with the theta
kernel, the sampled Fourier \(L^1\) capacity of this trace is

\[
 (H-1)\mathfrak C_\sigma(V).
\tag{157.R26}
\]

Equations (157.R22)--(157.R26), together with the two strict \(j\)
endpoint rows and the actual profile-transition differences, are the
literal mixed \(j\)-\(x\) ledger. Per-\(x\) BV or (157.R9) does not
bound its mixed absolute norm. Centering changes only \(r=0\) by
(157.R19) and therefore leaves (157.R22)--(157.R26) unchanged at every
mode occurring in the open matrix.

The sharp control model is useful because it distinguishes a genuine
mixed norm from one-dimensional BV. On a positive block
\(1\leq j\leq L\), take

\[
 B_j^{\mathrm{ctl}}(x)=a\,\mathbf{1}_{j+1\leq x\leq x_1},
 \qquad a=M^{-3/4},\quad L\leq x_1\asymp K<q.
\tag{157.R27}
\]

It has \(\|B_j^{\mathrm{ctl}}\|_\infty=a\),
\(\operatorname {Var}_xB_j^{\mathrm{ctl}}=2a\), and

\[
 \sup_j|A_j^{\mathrm{ctl}}|+\operatorname {Var}_jA_j^{\mathrm{ctl}}
 \ll Ka,
\tag{157.R28}
\]

exactly the accepted scale. Nevertheless

\[
 \mathfrak V_\square(B^{\mathrm{ctl}})
 =2a(L-1)+O(a),
\tag{157.R29}
\]

and, at every \(r\ne0\),

\[
 \widehat B_{j+1}^{\mathrm{ctl}}(r)-\widehat B_j^{\mathrm{ctl}}(r)
 =-a e_q(-r(j+1)).
\tag{157.R30}
\]

Subtracting \(A_j^{\mathrm{ctl}}/q\) changes neither (157.R29) nor
(157.R30) at a nonzero frequency. This model is not asserted to be the
literal coefficient; it proves rigorously that the currently accepted
one-dimensional controls cannot imply the required mixed norm. A
literal proof would have to exploit cancellation of the two lines in
(157.R22) or (157.R23), or prove a diagonal/mask-preserving discrepancy
theorem. Absolute layer cake cannot assume that cancellation.

**Centered physical completion.** The exact quotient projector is

\[
 G_N(t)=-\frac{i}{2N}
 \sum_{\substack{h\bmod q\\h\ \mathrm{odd}}}
 \chi _4(h)e_q(ht).
\tag{157.R31}
\]

For

\[
 E_I(h)=\sum_{x\in I}e_q(hx^2)
 -\frac{|I|}{q}\sum_{x\bmod q}e_q(hx^2),
\tag{157.R32}
\]

finite inversion gives

\[
 \mathscr D_N(I,J)
 =-\frac{i}{2N}
 \sum_{\substack{h\bmod q\\h\ \mathrm{odd}}}
 \chi _4(h)E_I(h)\sum_{j\in J}e_q(-hj).
\tag{157.R33}
\]

Let \(g=(h,q)=(h,N)\), the equality holding because \(h\) is odd. If

\[
 \mathcal G_q(h,r)=\sum_{x\bmod q}e_q(hx^2+rx),
\]

then \(\mathcal G_q(h,r)=0\) unless \(g\mid r\), and reduction to the
primitive even quadratic sum gives

\[
 |\mathcal G_q(h,r)|\leq \sqrt{2qg}.
\tag{157.R34}
\]

The \(r=0\) term is exactly removed in (157.R32). The Fourier
\(L^1\) norm of an interval and (157.R34) yield

\[
 |E_I(h)|\ll \sqrt{q(h,N)}\log(2q).
\tag{157.R35}
\]

Also, with \(|h|_q\) the least absolute representative,

\[
 \left|\sum_{j\in J}e_q(-hj)\right|
 \ll \min\left(V,\frac q{1+|h|_q}\right).
\tag{157.R36}
\]

Using
\((h,N)^{1/2}\leq\sum_{d\mid(h,N)}d^{1/2}\), every \(d\) here is odd,
and

\[
 \sum_{1\leq a\leq q/(2d)}
 \min\left(V,\frac{q/d}{a}\right)
 \ll \frac qd\log(2V),
\tag{157.R37}
\]

we obtain

\[
\begin{aligned}
 |\mathscr D_N(I,J)|
 &\ll \frac{\sqrt q}{N}\log(2q)
 \sum_{\substack{h\bmod q\\h\ \mathrm{odd}}}
 (h,N)^{1/2}
 \min\left(V,\frac q{1+|h|_q}\right)\\
 &\ll \sqrt N\,\tau(N)\log(2N)\log(2V),
\end{aligned}
\tag{157.R38}
\]

Here the complete normalization is
\[
 \frac1{2N}\,\sqrt q\,q
 =\frac{q^{3/2}}{2N}=4\sqrt N
 \qquad(q=4N),
\]
and
\(\sum_{d\mid N,\ d\ \mathrm{odd}}d^{-1/2}\leq\tau(N)\).
Thus no \(q\), \(N\), or divisor factor is suppressed in (157.R38),
which proves (157.R4). The divisor decomposition in (157.R37) is the
physical form of the full odd-\(d\) ledger; no coprimality between \(d\)
and \(N/d\) is assumed. Formula (157.R35) also shows precisely what
centering does: it deletes the \(r=0\) complete Gauss term, but the
\(r=\pm1\) terms still have square-root-modulus magnitude. Therefore
ordinary completion does not prove the desired
\(M^{3/4}X^\varepsilon\) discrepancy.

**Selected incidence correction.** On the literal selected graph,
\(j=k^2-Nn\) and the asymmetric cell is equivalent to

\[
 k^2-k+1\leq Nn\leq k^2+k.
\tag{157.R39}
\]

The upper endpoint for \(k\) is \(k^2+k\), while the lower endpoint for
\(k+1\) is \(k^2+k+1\). Hence these intervals partition the positive
integers and every \(n\) has exactly one \(k\), and therefore one \(j\).
Since the literal \(n\)-profile lies in a dyadic \(M\)-block,

\[
 L_U(V)\ll M.
\tag{157.R40}
\]

The accepted summed root estimate independently gives
\(L_U(V)\ll_\varepsilon VX^\varepsilon\); together these prove
(157.R5), for the union of both signs as well. With amplitude
\(M^{-3/4}X^\varepsilon\), absolute incidence gives only

\[
 M^{-3/4}\min(M,V)X^\varepsilon+M^{-1/4}X^\varepsilon,
\tag{157.R41}
\]

where the final term is the closed zero row. This is target-sized only
on the already accepted fixed-polylogarithmic collar. Square-root
cancellation in the \(L_U(V)\) *signed literal terms* would prove
(157.R6), but a cardinality bound is not such a theorem.

**Theta-coordinate \(N,M,V,d\) capacities.** Write
\(a=M^{-3/4}\) and suppress harmless \(X^\varepsilon\) factors. The
spatial BV bound gives, for least nonzero \(v\bmod H\),

\[
 |\widehat B_j(2dv)|
 \ll a\min\left(K,\frac H{|v|_H}\right),
 \qquad
 \sum_{\substack{v\bmod H\\v\ne0}}
 |\widehat B_j(2dv)|\ll aH\log(2H).
\tag{157.R42}
\]

Pointwise theta-Weil followed by divisor grouping therefore has, for
one \(d\), the capacity

\[
 \frac{d\sqrt c}{Nq}\,V\sqrt c\,(aH)
 \ll \frac{aV}{d}X^\varepsilon,
\tag{157.R43}
\]

and summing all odd \(d\mid N\) restores

\[
 \mathcal T_{\ne0,U}(V)\ll aV X^\varepsilon
 =M^{-3/4}VX^\varepsilon.
\tag{157.R44}
\]

This is the accepted termwise/Fourier-\(L^1\) capacity and gives no
positive-power range beyond the collar.

For the fixed-\(v\) interval theorem, let

\[
 P_{c,v}(J)=\sum_{j\in J}K(-v^2,-j;c),
 \qquad |P_{c,v}(J)|\ll_\varepsilon\min(V\sqrt c,c)X^\varepsilon.
\tag{157.R45}
\]

Abel summation must use

\[
 \Lambda_d=
 \sum_{\substack{v\bmod H\\v\ne0}}
 \left(\sup_j|\widehat B_j(2dv)|
 +\operatorname {Var}_j\widehat B_j(2dv)\right),
\tag{157.R46}
\]

not merely the first term in (157.R42). The diagonal term in
(157.R22)--(157.R23) has the raw capacity
\(H\mathfrak C_\sigma(V)\), so the frequency decay and the \(j\)-BV
cannot legally be separated. Even if one grants the favorable but
unproved replacement \(\Lambda_d\ll aH X^\varepsilon\), the exact
exterior factor gives

\[
\begin{aligned}
 \frac{d\sqrt c}{Nq}\Lambda_d\min(V\sqrt c,c)
 &\ll
 a\min\left(\frac Vd,\frac{\sqrt N}{d^{3/2}}\right)X^\varepsilon,\\
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}(\cdots)
 &\ll a\min(V,\sqrt N)X^\varepsilon.
\end{aligned}
\tag{157.R47}
\]

For \(V\leq\sqrt N\) this is again \(aV\); for \(V\geq\sqrt N\) it is
\(N^{1/2}M^{-3/4}\), target-sized only if \(M\geq N^{2/3-o(1)}\).
The literal cell variation can only make this absolute Abel placement
larger unless a new coupled theorem uses its phase.

Sampled Parseval retains every fold modulo \(H=2N/d\):

\[
 \sum_{v\bmod H}|\widehat B_j(2dv)|^2
 =H\sum_{r\bmod H}|C_{j,d}(r)|^2,
 \qquad
 C_{j,d}(r)=\sum_{\substack{x\bmod q\\x\equiv r\pmod H}}B_j(x),
\tag{157.R48}
\]

and hence

\[
 \sum_{v\bmod H}|\widehat B_j(2dv)|^2
 \ll_\varepsilon
 \left(\frac{N^{3/2}}{dM}+\frac N{M^{1/2}}\right)X^\varepsilon.
\tag{157.R49}
\]

The second term is exactly the large-\(d\) collision contribution
coming from multiplicity \(O(1+dK/N)\); it may not be dropped. The
pointwise theta-Weil estimate gives the safe energy bound

\[
 \sum_{v\bmod H}|K(-v^2,-j;c)|^2
 \ll_\varepsilon c^2(j,c)X^\varepsilon.
\tag{157.R50}
\]

On either signed interval,
\[
 \sum_{V<|j|\leq2V}(j,c)^{1/2}
 \ll_\varepsilon VX^\varepsilon.
\]
Indeed
\((j,c)^{1/2}\leq\sum_{r\mid(j,c)}r^{1/2}\); divisors
\(r\leq2V\) contribute
\(\sum_{r\mid c,r\leq2V}r^{1/2}(V/r+1)
\ll_\varepsilon V X^\varepsilon\).
Thus Cauchy in \(v\), followed only by this absolute gcd grouping in
\(j\) and by no unproved \(j\)-orthogonality, gives for one \(d\)

\[
 \frac{d\sqrt c}{Nq}\,Vc
 \left(\frac{N^{3/2}}{dM}+\frac N{M^{1/2}}\right)^{1/2}
 \ll V\left(
 \frac{N^{1/4}}{dM^{1/2}}+
 \frac1{d^{1/2}M^{1/4}}
 \right)X^\varepsilon.
\tag{157.R51}
\]

After all odd \(d\mid N\), Parseval has only the upper capacity

\[
 V\left(N^{1/4}M^{-1/2}+M^{-1/4}\right)X^\varepsilon,
\tag{157.R52}
\]

not a signed defect estimate. Equations (157.R43), (157.R47), and
(157.R51) restore respectively the selector/Fourier factor, the
\(d\sqrt c\) factor, \(c=4N/d\), \(H=c/2\), all divisor strata, and the
large-\(d\) folds.

Finally, complementary representatives are not a cancellation identity.
For each two-element orbit, represented by \(1\leq v<H/2\),

\[
 (H-v)^2\equiv v^2\pmod c,
 \qquad 2d(H-v)\equiv-2dv\pmod q,
\tag{157.R53}
\]

so their exact pair is

\[
 \big(\widehat B_j(2dv)+\widehat B_j(-2dv)\big)
 K(-v^2,-j;c).
\tag{157.R54}
\]

The literal \(B_j\) is complex because of its residual phase, and even
for a real coefficient (157.R54) is generally twice a real part, not
zero. The low mode \(v=1\) and its \(H-1\) partner therefore survive.
The self-complementary Nyquist mode \(v=H/2\) occurs only once and is not
included in (157.R54); it is isolated as a separate fold row.
The nonzero projection removes only \(v=0\); it merely centers, rather
than removes, the principal low-frequency/wrapped reciprocal arc.

## 4. First doubtful or unproved step

The first unproved literal step is a two-variable theorem, not another
one-variable profile estimate. In physical coordinates one must prove
either

\[
 \mathfrak V_\square(B)\ll_\varepsilon M^{-3/4}X^\varepsilon
\tag{157.R55}
\]

after an exact cancellation of the diagonal terms in
(157.R22)--(157.R23), together with

\[
 \sup_{I,J}|\mathscr D_N(I,J)|
 \ll_\varepsilon M^{3/4}X^\varepsilon,
\tag{157.R56}
\]

or replace both by a diagonal/mask-preserving estimate that never takes
the absolute mixed norm. Neither follows from (157.R8)--(157.R9), and
ordinary completion proves only (157.R4).

Equivalently, in selected coordinates the missing input is a signed
theorem of strength

\[
 \left|
 \sum_{\substack{n\ \mathrm{in\ the\ literal}\ M\text{-block}\\
 n\ \mathrm{odd},\ V<|j_n|\leq2V}}
 \chi _4(n)\,W_U(n,j_n)e(\sqrt{Nn})
 \right|
 \ll_\varepsilon M^{3/4}X^\varepsilon,
\tag{157.R57}
\]

with the actual profile \(W_U\), both signs, transitions, and endpoints.
The incidence count (157.R5) makes a square-root version of (157.R57)
more than sufficient in every \(V\)-range, but count alone supplies no
signed cancellation.

In theta coordinates the same first gap is a joint estimate for
(157.R22) or (157.R23) coupled to \(K(-v^2,-j;c)\). Applying the
fixed-\(v\) theorem only after replacing \(\Lambda_d\) by separated
supremum and variation norms either restores the diagonal \(H\)-loss or,
even under the idealized norm, stops at (157.R47). Complementary modes,
the \(v=1\) wrapped branch, large-\(d\) folds, and the hard endpoints must
remain inside any future theorem.

Thus the report does not claim that (157.R55), (157.R56), or
(157.R57) is false. It proves that the proposed rectangular completion
and separated fixed-\(v\) placements cannot certify them with the frozen
inputs and their complete restored-power ledgers.

## 5. Control tests and outcomes

- **Literal nonzero matrix and exterior factors — pass.** Equations
  (157.R15)--(157.R17) retain
  \(-i(1+i)/(2Nq)\), \(\chi _4(d)d\sqrt c\), \(c=4N/d\), and all
  \(v\bmod(c/2)\) except zero.
- **Exact zero projection — pass.** Round-156 recombination forces the
  factor \(1/q=1/(4N)\); (157.R17) rules out \(1/N\), \(1/(2N)\), or a
  second subtraction.
- **Global constant tail — pass.** Its full spatial \(L^1\) mass is
  recorded, its mixed cyclic difference is zero, its nonzero sampled
  Fourier coefficients vanish, and its full-circle discrepancy is zero.
  It is exactly the closed zero row, not a discarded error.
- **Mixed variation versus one-dimensional BV — obstruction.** The
  exact cell formulas (157.R22)--(157.R26) contain a diagonal point trace.
  The control array (157.R27) satisfies the accepted amplitude, spatial
  BV, row-sum BV, support, and centering scales but has mixed norm
  \(\asymp VM^{-3/4}\).
- **Actual selected incidence count — pass and correction.** The cell
  intervals (157.R39) partition positive integers, proving
  \(L_U(V)\ll\min(M,V)X^\varepsilon\). A genuine square-root signed
  theorem would be target-safe for all \(V\), not only
  \(V\leq M^{3/2}\). This remains a hypothetical capacity.
- **Centered rectangular completion — obstruction.** Exact nonzero
  completion gives (157.R4); after the most favorable mixed profile
  norm it restores \(N^{1/2}M^{-3/4}\), a positive power everywhere in
  the frozen \(M\leq N^{1/2}\) range.
- **Fixed-\(v\), Fourier-\(L^1\), and completion capacities — pass/no
  gain.** The full per-\(d\) and summed ledgers are (157.R43),
  (157.R47), and (157.R44). Fixed-\(v\) Abel cannot replace the literal
  \(j\)-variation by frequency decay.
- **Parseval and folds — pass/no gain.** Equations (157.R48)--(157.R52)
  retain the collision period \(2N/d\) and the large-\(d\) term
  \(N/M^{1/2}\). No physical-diagonal or defect-orthogonality claim is
  made.
- **Nonzero and complementary modes — pass.** Equations
  (157.R53)--(157.R54) keep every two-element orbit and show that pairing
  is not automatic cancellation. The self-complementary mode \(v=H/2\)
  is explicitly excluded from the pair formula and retained as a
  separate fold row.
- **Principal low-frequency/wrapped arc — retained.** Centering deletes
  only exact \(v=0\) (or \(r=0\) in (157.R32)); \(v=1,H-1\) and
  \(r=\pm1\) survive with square-root completion capacity.
- **Both signs, cells, transitions, and endpoints — pass.** The two
  different cell motions are printed in (157.R22) and (157.R23), profile
  transitions stay in the bulk differences, and zero extension in
  (157.R13) charges both strict \(j\)-endpoints. The two signed blocks
  are never paired without a theorem.
- **Arbitrary \(N\), all odd \(d\), and powers — pass.** The gcd grouping
  in (157.R37), sampled Parseval, and the divisor sums require no
  squarefree, odd-\(N\), or coprime-\(d\) hypothesis. All divisor sums
  cost only \(X^\varepsilon\).
- **External and downstream scope — pass.** The external
  \(B_{1,U}(1)\) seam is retained as an \(X^\varepsilon\) factor. No
  statement is transferred to \(D>1\), \(L>1\), generic \(t=1\),
  \(t\geq2\), cross, another M1 or M2 owner, endpoint uniformity, M9, the
  bridge, the quarter target, or either global exponent.

All work in this report is analytic/algebraic. No numerical experiment
or numerical certification was used.

## 6. Dependencies and artifacts used

This report used exactly the selected Round-157 context:

- protocol.md;
- state/proof_obligations.yml, in particular the five active target
  obligations and the Round-155--156 rejected-claim controls;
- state/active_campaign.yml;
- strategy/round157_d1_nonzero_theta_matrix_strategy.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/barrier_packet.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/candidates/conductor_round157_centered_seed.md;
- proofs/kernels/m9_m1_d1_theta_zero_row.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reviews/conductor_round156_adjudication.md; and
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reviews/conductor_round155_adjudication.md.

The exact identity depends on the accepted Round-155 complete
half-period inverse-Gauss formula and the accepted Round-156 zero-row
recombination. The profile scale, phase, cell, transition, mask, sign,
and endpoint hypotheses are precisely those frozen by the campaign. No
shared proof state, synthesis, review, validation matrix, or proof draft
was edited.

## 7. Recommended state effect

Recommended terminal label:
outer_defect_centered_discrepancy_no_go.

After independent review, promote only the route-scoped exact centering
identity (157.R1), the constant-tail/mixed-cell ledger
(157.R19)--(157.R30), the elementary centered completion bound
(157.R38), and the corrected incidence count (157.R5). Record that:

- the \(1/(4N)\) projection is exact and the zero row is removed once;
- ordinary rectangular Abel requires a genuine mixed norm and cannot
  infer it from the accepted one-dimensional BV data because of the
  moving cell;
- even an ideal mixed norm followed by ordinary completion restores the
  forbidden \(N^{1/2}M^{-3/4}\) power;
- fixed-\(v\), Fourier-\(L^1\), Parseval, and separated completion remain
  upper capacities with the powers (157.R43), (157.R47), and
  (157.R51);
- the earlier \(V\leq M^{3/2}\) square-root-incidence capacity should be
  corrected at the selected level: since there are at most
  \(O(\min(M,V)X^\varepsilon)\) literal incidences, a genuine square-root
  theorem would close every \(V\), but no such theorem is proved; and
- centering removes exact DC only and does not remove the low nonzero or
  complementary wrapped branches.

Do not promote the nonzero target, a positive-power defect range, a
signed square-root incidence estimate, or any downstream theorem. The
fixed-polylogarithmic collar remains the last proved complete
\(D=d=L=1\) range, and the incomplete nonzero theta matrix or an exactly
equivalent mask-preserving selected theorem remains open.
