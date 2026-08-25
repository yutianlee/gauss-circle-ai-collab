# M9--M1 \(D=d=L=1\) paired-interior cell-trace kernel

## Scope

Fix \(A>0\),

\[
 q=4N,\qquad K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\le K,\qquad M\le N^{1/2}.
\]

For every odd \(d\mid N\), put

\[
 c=\frac qd,\qquad H=\frac c2,\qquad n=\frac Nd=\frac H2.
\tag{K158.1}
\]

Let \(J_+=[a_+,b_+]\) and \(J_-=[a_-,b_-]\) be the exact
positive and negative integer blocks in \(V<|j|\le2V\).  On the
unique physical lift write

\[
 B_j(x)=\mathbf 1_{x\ge\lambda_\sigma(j)}F_j(x),\qquad
 \lambda_+(j)=j+1,\qquad \lambda_-(j)=-j.
\tag{K158.2}
\]

Here \(F_j\) retains the literal zero-extended profile, complex
residual phase, asymmetric cell, component transitions, half-open
choices, and hard endpoints inherited from the Round 157 kernel.  In
particular,

\[
 |F_j(\lambda_\sigma(j))|
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{K158.3}
\]

This kernel concerns only the moving-mask Abel trace inside the paired
interior nonzero theta matrix.  It does not control the two Abel outer
terms, either profile-bulk remainder, the full paired matrix, or the
external \(B_{1,U}(1)\) scalar seam.

## 1. Sign-adapted Abel trace

Write

\[
 A_j(v)=\widehat B_j(2dv),\qquad
 K_{d,v}(s)=K(-v^2,-s;c),
\]

and define the positive prefix and negative suffix

\[
 P^+_{d,v}(j)=\sum_{s=a_+}^{j}K_{d,v}(s),\qquad
 P^-_{d,v}(j)=\sum_{s=j}^{b_-}K_{d,v}(s).
\tag{K158.4}
\]

Direct mask subtraction gives

\[
\begin{aligned}
 A_{j+1}(v)-A_j(v)
 ={}&-F_j(j+1)e_c(-2v(j+1))\\
 &+\sum_{x\ge j+2}(F_{j+1}(x)-F_j(x))e_c(-2vx)
\end{aligned}
\tag{K158.5}
\]

on \(J_+\), and

\[
\begin{aligned}
 A_j(v)-A_{j-1}(v)
 ={}&F_j(-j)e_c(2vj)\\
 &+\sum_{x\ge-j+1}(F_j(x)-F_{j-1}(x))e_c(-2vx)
\end{aligned}
\tag{K158.6}
\]

on \(J_-\).  Finite Abel summation therefore yields

\[
\begin{aligned}
 \sum_{j=a_+}^{b_+}A_j(v)K_{d,v}(j)
 ={}&A_{b_+}(v)P^+_{d,v}(b_+)\\
 &+\sum_{j=a_+}^{b_+-1}F_j(j+1)e_c(-2v(j+1))P^+_{d,v}(j)\\
 &-\sum_{j=a_+}^{b_+-1}P^+_{d,v}(j)
   \sum_{x\ge j+2}(F_{j+1}(x)-F_j(x))e_c(-2vx),
\end{aligned}
\tag{K158.7}
\]

and

\[
\begin{aligned}
 \sum_{j=a_-}^{b_-}A_j(v)K_{d,v}(j)
 ={}&A_{a_-}(v)P^-_{d,v}(a_-)\\
 &+\sum_{j=a_-+1}^{b_-}F_j(-j)e_c(2vj)P^-_{d,v}(j)\\
 &+\sum_{j=a_-+1}^{b_-}P^-_{d,v}(j)
   \sum_{x\ge-j+1}(F_j(x)-F_{j-1}(x))e_c(-2vx).
\end{aligned}
\tag{K158.8}
\]

Thus the moving atom has a positive sign on both blocks.  The exact
outer terms are the positive right endpoint and the negative left
endpoint.  The middle lines of (K158.7)--(K158.8), summed over

\[
 \mathcal V_d^\circ=\{v\bmod H:v\ne0,n\},
\tag{K158.9}
\]

and multiplied by the accepted exterior factor, define

\[
\begin{aligned}
 \mathcal C_{\mathrm{int},U}(V)
 ={}&-\frac{i(1+i)}{2Nq}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c\,(\mathcal C_{+,d}+\mathcal C_{-,d}),\\
 \mathcal C_{+,d}
 ={}&\sum_{j=a_+}^{b_+-1}F_j(j+1)
 \sum_{v\in\mathcal V_d^\circ}e_c(-2v(j+1))P^+_{d,v}(j),\\
 \mathcal C_{-,d}
 ={}&\sum_{j=a_-+1}^{b_-}F_j(-j)
 \sum_{v\in\mathcal V_d^\circ}e_c(2vj)P^-_{d,v}(j).
\end{aligned}
\tag{K158.10}
\]

When \(c=4\), the interior set (K158.9) is empty.

## 2. Full-frequency inversion and the removed trace rows

For every integer \(x,s\), complete half-period inversion gives

\[
 \sum_{v\bmod H}e_c(-2vx)K(-v^2,-s;c)
 =\frac{1-i}{2}\sqrt c
 \sum_{u\bmod c}^{*}\chi_4(u)e_c(u(x^2-s)).
\tag{K158.11}
\]

The normalization is fixed by

\[
 -\frac{i(1+i)}{2Nq}\frac{1-i}{2}dc=-\frac{i}{2N},
 \qquad dc=q.
\tag{K158.12}
\]

Writing \(h=du\) partitions the odd residues \(h\bmod4N\) according
to \(d=(h,N)\), and hence the all-divisor recombination is

\[
 -\frac{i(1+i)}{2Nq}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c
 \sum_{v\bmod H}e_c(-2vx)K(-v^2,-s;c)
 =G_N(x^2-s),
\tag{K158.13}
\]

where

\[
 G_N(t)=\mathbf 1_{N\mid t}\chi_4(t/N).
\]

Consequently the full-frequency moving trace is

\[
\begin{aligned}
 \mathcal C_+^{\mathrm{full}}
 &=\sum_{j=a_+}^{b_+-1}F_j(j+1)
   \sum_{s=a_+}^{j}G_N((j+1)^2-s),\\
 \mathcal C_-^{\mathrm{full}}
 &=\sum_{j=a_-+1}^{b_-}F_j(-j)
   \sum_{s=j}^{b_-}G_N(j^2-s).
\end{aligned}
\tag{K158.14}
\]

Let \(\mathcal Z_{\mathrm{tr}}\) and
\(\mathcal F_{\mathrm{tr}}\) be the normalized terms obtained from
(K158.10) by inserting only \(v=0\) and \(v=n=H/2\), respectively.
Then

\[
 \mathcal C_{\mathrm{int},U}(V)
 =\mathcal C_+^{\mathrm{full}}+\mathcal C_-^{\mathrm{full}}
  -\mathcal Z_{\mathrm{tr}}-\mathcal F_{\mathrm{tr}}.
\tag{K158.15}
\]

For every fixed \(v\bmod H\) and consecutive interval \(I\), opening
the theta kernel and summing its nonzero additive frequencies
geometrically proves

\[
 \sup_I\left|\sum_{s\in I}K(-v^2,-s;c)\right|
 \ll c\log(2c).
\tag{K158.16}
\]

Using (K158.3) on the \(O(V)\) trace atoms and restoring all odd
divisors gives, separately for \(v=0\) and \(v=n\),

\[
\begin{aligned}
 |\mathcal C^{(v)}|
 &\ll_\varepsilon
 \frac{VM^{-3/4}}{Nq}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}d\,c^{3/2}X^\varepsilon\\
 &\ll_\varepsilon VM^{-3/4}N^{-1/2}X^\varepsilon
 \le M^{-1/4}X^\varepsilon.
\end{aligned}
\tag{K158.17}
\]

This proves the two Abel-trace pieces directly; it does not transfer a
whole-row theorem to a trace term.

## 3. The endpoint subrow

The endpoint \(s=j\) in (K158.14) is

\[
\begin{aligned}
 \mathcal E_{\mathrm{full}}
 ={}&\sum_{j=a_+}^{b_+-1}F_j(j+1)G_N(j^2+j+1)\\
 &+\sum_{j=a_-+1}^{b_-}F_j(-j)G_N(j(j-1)).
\end{aligned}
\tag{K158.18}
\]

For every prime power \(p^\nu\), the congruence
\(j(j-1)\equiv0\pmod {p^\nu}\) has exactly the two roots \(0,1\).
For \(j^2+j+1\), the complete local count is

\[
 \rho_+(p^\nu)=
 \begin{cases}
  0,&p=2,\\
  1,&p=3,\ \nu=1,\\
  0,&p=3,\ \nu\ge2,\\
  2,&p\ne2,3,\ p\equiv1\pmod3,\\
  0,&p\ne2,3,\ p\equiv2\pmod3.
 \end{cases}
\tag{K158.19}
\]

The exceptional root modulo \(3\) does not lift modulo \(9\), and
all roots at \(p\ne2,3\) are simple.  The Chinese remainder theorem
therefore gives \(O_\varepsilon(N^\varepsilon)\) endpoint classes.
Since each signed block has length less than \(N\),

\[
 |\mathcal E_{\mathrm{full}}|
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{K158.20}
\]

This estimate controls only the endpoint face; it says nothing about
the strict prefix or suffix.

## 4. Exact strict selected sum

Put

\[
 \kappa(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,
 \qquad r(\ell)=\kappa(\ell)^2-N\ell.
\tag{K158.21}
\]

The intervals

\[
 [k^2-k+1,k^2+k],\qquad k\ge1,
\tag{K158.22}
\]

partition the positive integers, so (K158.21) is the unique
nearest-cell coordinate.  The exact strict selectors are

\[
\begin{aligned}
 \eta_+(\ell)&=
 \mathbf 1_{a_++1\le\kappa(\ell)\le b_+}
 \mathbf 1_{a_+\le r(\ell)\le\kappa(\ell)-2},\\
 \eta_-(\ell)&=
 \mathbf 1_{-b_-\le\kappa(\ell)\le-a_--1}
 \mathbf 1_{-\kappa(\ell)+1\le r(\ell)\le b_-}.
\end{aligned}
\tag{K158.23}
\]

Their literal boundary-frozen weights are

\[
\begin{aligned}
 W_+(k)&=F_{k-1}(k)
 =w_U\!\left(\frac{k^2-k+1}{N}\right)
   e(\sqrt{k^2-k+1}-k),\\
 W_-(k)&=F_{-k}(k)
 =w_U\!\left(\frac{k^2+k}{N}\right)
   e(\sqrt{k^2+k}-k).
\end{aligned}
\tag{K158.24}
\]

The quotient carrying the character is \(\ell\), whereas the positive
and negative profile arguments lie strictly below and above \(\ell\),
respectively.  They cannot be replaced by \(w_U(\ell)\), identified
with one another, or paired by conjugacy.

Deleting (K158.18) from (K158.14) gives exactly

\[
 \mathcal S_{\mathrm{str}}(V)=
 \sum_{\ell\ge1}\chi_4(\ell)
 \left[\eta_+(\ell)W_+(\kappa(\ell))
       +\eta_-(\ell)W_-(\kappa(\ell))\right].
\tag{K158.25}
\]

Combining (K158.15), (K158.17), and (K158.20) proves the exact
reduction

\[
 \boxed{
 \mathcal C_{\mathrm{int},U}(V)
 =\mathcal S_{\mathrm{str}}(V)
  +O_\varepsilon(M^{-1/4}X^\varepsilon).}
\tag{K158.26}
\]

The selected support satisfies

\[
 L_{\mathrm{str}}(V)
 \ll_\varepsilon\min(M,V)X^\varepsilon.
\tag{K158.27}
\]

Moreover, a nonzero boundary weight forces

\[
 \frac{k^2+O(k)}N\asymp M,
\]

while \(k\asymp V\).  Thus the moving trace is zero unless

\[
 V\asymp K=\sqrt{NM}.
\tag{K158.28}
\]

On this only possibly nonzero range, \(V\gg M\) and the support bound
in (K158.27) can still be \(O(MX^\varepsilon)\).  With atom scale
\(a=M^{-3/4}X^\varepsilon\), absolute summation gives only
\(aM=M^{1/4}X^\varepsilon\).  The frozen scalar target is
\(O_\varepsilon(X^\varepsilon)\), so the missing raw estimate is

\[
 \left|\sum_{\ell\asymp M}\chi_4(\ell)
  \left[\eta_+(\ell)\widetilde W_+(\kappa(\ell))
       +\eta_-(\ell)\widetilde W_-(\kappa(\ell))\right]\right|
 \ll_\varepsilon M^{3/4}X^\varepsilon,
\tag{K158.29}
\]

where \(W_\pm=a\widetilde W_\pm\).  Raw square-root size
\(M^{1/2}\) would be sufficient but is stronger than required.

## 5. Strict-survivor and method boundary

Endpoint roots do not exhaust the strict trace.  For \(L=2^h\),
\(h\ge3\), set

\[
\begin{aligned}
 V&=L^2,& \ell=M&=L+1,\\
 k&=(L+1)(L+4),& s&=L(L+1),\\
 N&=(L+1)(L+4)^2-L.
\end{aligned}
\tag{K158.30}
\]

Then

\[
 N\ell=k^2-s,\qquad V<s<k-1\le2V,\qquad
 \chi_4(\ell)=1,
\tag{K158.31}
\]

but

\[
 k-1-s=4L+3\in(0,N).
\tag{K158.32}
\]

Thus this is a genuine positive strict arithmetic selected point in the
support-localized top range while its endpoint polynomial is
nonresonant; it carries a literal trace term whenever the inherited
component is nonzero at the displayed boundary argument.  This family
is a survivor control, not a lower bound for the full signed sum.

Ordinary Abel summation against the bounded partial sums of \(\chi_4\)
does not prove (K158.29), because the sharp residual mask can have
variation of the same order as its support.  Standard
Erdős--Turán plus the second-derivative estimate for
\(h\sqrt{N\ell}\) gives the raw capacity

\[
 D(M)\ll M^{1/3}K^{1/3}+\frac{M}{\sqrt K},
\tag{K158.33}
\]

which reaches \(M^{3/4}\) only if \(M\ge N^{2/3}\).  The classical
exponent pair \((1/6,2/3)\) gives

\[
 D(M)\ll M^{4/7}K^{1/7}X^\varepsilon
\tag{K158.34}
\]

with the same threshold.  More generally, at \(M=N^{1/2}\) an
exponent pair \((\kappa_0,\lambda_0)\) in this placement would have to
satisfy

\[
 \lambda_0+\frac34\kappa_0\le\frac34.
\tag{K158.35}
\]

The accepted incomplete-quadratic completion has raw capacity
\(\sqrt N X^\varepsilon\) and also needs \(M\ge N^{2/3}\).  These are
capacities of the named placements, not lower bounds and not a
universal impossibility theorem.

## 6. Remaining frontier

There is no unproved step in the Abel signs and endpoints,
full-frequency normalization, separate zero and Nyquist trace bounds,
endpoint root table, strict selected-coordinate identity, support-zero
range, or restored target calibration under the printed hypotheses.
The first open trace input is (K158.29) for the literal sharp mask,
two boundary-frozen profiles, residual phases, transitions, endpoints,
and \(\chi_4\)-sign.

The exact outer terms
\(A_{b_+}P^+_{d,v}(b_+)\) and
\(A_{a_-}P^-_{d,v}(a_-)\), together with both profile-bulk
remainders in (K158.7)--(K158.8), remain separate open seams.  No claim
in this kernel controls the complete paired interior matrix, another
\(D,d,L,t\) layer, any other M1 or M2 owner, endpoint uniformity, M9,
the conditional bridge, the quarter target, or either global exponent.
