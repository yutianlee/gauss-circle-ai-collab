# Sign-adapted paired-interior cell-trace attack

- Campaign: m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate
- Round: 158
- Task: sign_adapted_cell_trace_attack
- Role: discovery
- Starting graph: 3acbfaf6fb95047babd19800dee4152fb60cb408197a8ceac93931a20c57491f
- Status: candidate evidence only

## 1. Result

**Terminal label: paired_interior_cell_trace_no_go.** The no-go is
route-scoped: it rules out closing the trace from endpoint root counts,
support cardinality, or one-variable profile BV alone. It is not a
lower bound and does not rule out a new signed theorem for the literal
coefficient.

The frozen \(D=1\) scalar target in this report is
\(O_\varepsilon(X^\varepsilon)\). The \(M^{-1/4}X^\varepsilon\)
bounds inherited for the zero and Nyquist pieces are stronger than the
required scalar target; they are not used to redefine it.

The exact prefix/suffix Abel calculation gives the trace printed in the
campaign, with a positive moving atom on both signed blocks. The two
outer Abel terms are different: the positive block leaves its right
endpoint, while the negative block leaves its left endpoint. Complete
half-period inversion, including all odd divisors of \(N\), gives the
physical full-frequency trace with no lost constant. The individual
\(v=0\) and \(v=H/2\) **trace pieces** (not merely their total rows) are
each

\[
 O_\varepsilon(M^{-1/4}X^\varepsilon).
\tag{158.R1}
\]

The endpoint \(s=j\) of the full-frequency trace is also target-safe.
The complete local root table is

\[
 \#\{j\bmod p^\nu:j(j-1)\equiv0\pmod {p^\nu}\}=2
\tag{158.R2}
\]

for every prime \(p\) and \(\nu\geq1\), while for
\(f_+(j)=j^2+j+1\) it is

\[
 \rho_+(p^\nu)=
 \begin{cases}
  0,&p=2,\\
  1,&p=3,\ \nu=1,\\
  0,&p=3,\ \nu\ge2,\\
  2,&p\ne2,3,\ p\equiv1\pmod3,\\
  0,&p\ne2,3,\ p\equiv2\pmod3.
 \end{cases}
\tag{158.R3}
\]

After deleting \(s=j\), the exact survivor is a boundary-frozen
selected sum

\[
 \mathcal S_{\rm str}(V)=
 \sum_{\ell\ge1}\chi _4(\ell)
 \left(\eta_+(\ell)W_+(\kappa(\ell))
       +\eta_-(\ell)W_-(\kappa(\ell))\right),
\tag{158.R4}
\]

where \(\kappa(\ell)\) is the unique nearest-cell coordinate, the two
selectors retain the exact strict prefix and suffix, and

\[
 \begin{aligned}
 W_+(k)&=F_{k-1}(k)
 =w_U\!\left(\frac{k^2-k+1}{N}\right)
   e\!\left(\sqrt{k^2-k+1}-k\right),\\
 W_-(k)&=F_{-k}(k)
 =w_U\!\left(\frac{k^2+k}{N}\right)
   e\!\left(\sqrt{k^2+k}-k\right),
 \end{aligned}
\tag{158.R5}
\]

with the inherited zero extension, component transitions, half-open
choices, and hard endpoints understood literally. In particular, the
profile is evaluated at the moving-cell boundary; it is **not**
evaluated at the selected integer quotient \(\ell\) in a strict term.

The normalized paired-interior trace therefore satisfies the exact
reduction with a stronger-than-required error

\[
 \boxed{
 \mathcal C_{\mathrm{int},U}(V)
 =\mathcal S_{\rm str}(V)
  +O_\varepsilon(M^{-1/4}X^\varepsilon).}
\tag{158.R6}
\]

The support of (158.R4) has size

\[
 L_{\rm str}(V)\ll_\varepsilon\min(M,V)X^\varepsilon,
\tag{158.R7}
\]

but the available absolute bound is only

\[
 |\mathcal S_{\rm str}(V)|
 \ll_\varepsilon M^{-3/4}\min(M,V)X^\varepsilon.
\tag{158.R8}
\]

There is an exact support-localization refinement. The trace vanishes
unless one of

\[
 \frac{k^2-k+1}{N},\qquad \frac{k^2+k}{N}
\tag{158.R9}
\]

with \(k\asymp V\) meets the literal support of \(w_U\). Since that
support is at scale \(M\), nonzero trace forces \(V\asymp\sqrt{NM}=K\)
up to the inherited support constants. Thus blocks disjoint from that
intersection form a genuine zero range for the trace only. On every
nonzero block, \(V\asymp K\gg M\) in the frozen range, so
\(\min(M,V)=M\); localization does not give the target. A genuine
square-root signed estimate would be more than target-safe, but the
actual requirement is only a raw \(M^{3/4}\) bound, rather than raw
square-root size \(M^{1/2}\). Endpoint roots and the literal
one-variable BV data prove neither threshold. This strict selected
estimate is the first missing theorem.

## 2. Exact statement and hypotheses

Let \(X\) be large, \(N=\lfloor X\rfloor\), and retain the frozen range

\[
 1\ll M\le N^{1/2},\qquad
 M^{3/4}(\log(2X))^A<V\le K:=\sqrt{NM}.
\tag{158.R10}
\]

The exact integer signed blocks in \(V<|j|\le2V\) are

\[
 \begin{aligned}
 a_+&=\lfloor V\rfloor+1,&b_+&=\lfloor2V\rfloor,\\
 a_-&=-\lfloor2V\rfloor,&b_-&=-\lfloor V\rfloor-1,
 \end{aligned}
\tag{158.R11}
\]

so \(J_+=[a_+,b_+]\) and \(J_-=[a_-,b_-]\). Empty intervals, if any
among finitely many small parameters, contribute zero.

Put

\[
 q=4N,\qquad c=\frac qd,\qquad H=\frac c2,
 \qquad n=\frac Nd=\frac H2=\frac c4
\tag{158.R12}
\]

for every odd \(d\mid N\), and

\[
 \mathcal V_d^\circ=\{v\bmod H:v\ne0,n\}.
\tag{158.R13}
\]

The range (158.R13) contains both \(v\) and \(H-v\); no conjugacy or
pair cancellation is imposed. In particular, \(c=4\) gives \(H=2\)
and \(\mathcal V_d^\circ=\varnothing\), exactly as it should.

On the unique physical lift write

\[
 B_j(x)=\mathbf1_{x\ge\lambda_\sigma(j)}F_j(x),
 \qquad \lambda_+(j)=j+1,\quad\lambda_-(j)=-j,
\tag{158.R14}
\]

where \(F_j\) retains the actual complex residual phase, the real
zero-extended \(w_U\)-profile, every transition, the asymmetric cell,
the half-open conventions, and every physical and hard endpoint. The
only estimate used on a moving atom is

\[
 |F_j(\lambda_\sigma(j))|
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{158.R15}
\]

Set

\[
 A_j(v)=\widehat B_j(2dv),\qquad
 K_{d,v}(s)=K(-v^2,-s;c),
\tag{158.R16}
\]

and define the exact prefix and suffix

\[
 P^+_{d,v}(j)=\sum_{s=a_+}^{j}K_{d,v}(s),\qquad
 P^-_{d,v}(j)=\sum_{s=j}^{b_-}K_{d,v}(s).
\tag{158.R17}
\]

The object proved equivalent to (158.R4), up to (158.R1), is

\[
\begin{aligned}
 \mathcal C_{\mathrm{int},U}(V)
 ={}&-\frac{i(1+i)}{2Nq}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi _4(d)d\sqrt c\,\bigl(\mathcal C_{+,d}+\mathcal C_{-,d}\bigr),\\
 \mathcal C_{+,d}
 ={}&\sum_{j=a_+}^{b_+-1}F_j(j+1)
 \sum_{v\in\mathcal V_d^\circ}
 e_c(-2v(j+1))P^+_{d,v}(j),\\
 \mathcal C_{-,d}
 ={}&\sum_{j=a_-+1}^{b_-}F_j(-j)
 \sum_{v\in\mathcal V_d^\circ}
 e_c(2vj)P^-_{d,v}(j).
\end{aligned}
\tag{158.R18}
\]

No hypothesis of oddness, squarefreeness, or coprimality is placed on
\(N\) or \(N/d\). The external scalar \(B_{1,U}(1)\) is not included
in (158.R18) and remains a separate \(X^\varepsilon\)-sized assembly
seam.

## 3. Proof or derivation

### 3.1 Exact sign-adapted Abel identities and outer endpoints

On \(J_+\), direct subtraction of the two masks gives

\[
\begin{aligned}
 A_{j+1}(v)-A_j(v)
 ={}&-F_j(j+1)e_c(-2v(j+1))\\
 &+\sum_{x\ge j+2}
   \bigl(F_{j+1}(x)-F_j(x)\bigr)e_c(-2vx).
\end{aligned}
\tag{158.R19}
\]

Since \(K_{d,v}(j)=P^+_{d,v}(j)-P^+_{d,v}(j-1)\), with the prefix
before \(a_+\) equal to zero,

\[
\begin{aligned}
 \sum_{j=a_+}^{b_+}A_j(v)K_{d,v}(j)
 ={}&A_{b_+}(v)P^+_{d,v}(b_+)\\
 &+\sum_{j=a_+}^{b_+-1}
  F_j(j+1)e_c(-2v(j+1))P^+_{d,v}(j)\\
 &-\sum_{j=a_+}^{b_+-1}
  P^+_{d,v}(j)
  \sum_{x\ge j+2}
   \bigl(F_{j+1}(x)-F_j(x)\bigr)e_c(-2vx).
\end{aligned}
\tag{158.R20}
\]

Thus the positive moving atom has a positive sign in the Abel formula,
and the exact outer term is the right endpoint
\(A_{b_+}(v)P^+_{d,v}(b_+)\).

On \(J_-\), the correct backward difference is

\[
\begin{aligned}
 A_j(v)-A_{j-1}(v)
 ={}&F_j(-j)e_c(2vj)\\
 &+\sum_{x\ge-j+1}
   \bigl(F_j(x)-F_{j-1}(x)\bigr)e_c(-2vx).
\end{aligned}
\tag{158.R21}
\]

Because \(K_{d,v}(j)=P^-_{d,v}(j)-P^-_{d,v}(j+1)\), with the suffix
after \(b_-\) equal to zero,

\[
\begin{aligned}
 \sum_{j=a_-}^{b_-}A_j(v)K_{d,v}(j)
 ={}&A_{a_-}(v)P^-_{d,v}(a_-)\\
 &+\sum_{j=a_-+1}^{b_-}
  F_j(-j)e_c(2vj)P^-_{d,v}(j)\\
 &+\sum_{j=a_-+1}^{b_-}
  P^-_{d,v}(j)
  \sum_{x\ge-j+1}
   \bigl(F_j(x)-F_{j-1}(x)\bigr)e_c(-2vx).
\end{aligned}
\tag{158.R22}
\]

The suffix atom again has a positive sign. Its exact outer term is the
left endpoint \(A_{a_-}(v)P^-_{d,v}(a_-)\). Equations (158.R20) and
(158.R22) also display the two profile-bulk remainders, including their
opposite Abel signs. Summing only their middle lines over all literal
interior frequencies and restoring the exterior factor gives
(158.R18). Neither outer term nor either bulk remainder is silently
included in the trace.

### 3.2 Full-frequency inversion and exact normalization

Opening the accepted theta multiplier and completing its quadratic
sum over the half-period gives, for every integer \(x,s\),

\[
\begin{aligned}
 \Phi_d(x,s)
 &:=
 \sum_{v\bmod H}e_c(-2vx)K(-v^2,-s;c)\\
 &=\frac{1-i}{2}\sqrt c
 \sum_{u\bmod c}^{*}\chi _4(u)e_c\bigl(u(x^2-s)\bigr).
\end{aligned}
\tag{158.R23}
\]

This remains valid for \(c=4\). Multiplication by the exterior factor
uses

\[
 -\frac{i(1+i)}{2Nq}\cdot\frac{1-i}{2}\cdot d c
 =-\frac{i}{2N},
 \qquad dc=q.
\tag{158.R24}
\]

The pairs \((d,u)\), with \(d\mid N\) odd and \(u\bmod q/d\) a unit,
partition the odd \(h\bmod q\) by \(h=du\) and \(d=(h,N)\). Moreover
\(\chi _4(d)\chi _4(u)=\chi _4(h)\) and
\(e_{q/d}(u t)=e_q(ht)\). Therefore

\[
\begin{aligned}
 &-\frac{i(1+i)}{2Nq}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi _4(d)d\sqrt c\,\Phi_d(x,s)\\
 &\hspace{24mm}=-\frac{i}{2N}
 \sum_{\substack{h\bmod q\\h\ {\rm odd}}}
 \chi _4(h)e_q\bigl(h(x^2-s)\bigr)\\
 &\hspace{24mm}=
 G_N(x^2-s),
 \qquad G_N(t)=\mathbf1_{N\mid t}\chi _4(t/N).
\end{aligned}
\tag{158.R25}
\]

Substitution of \(x=j+1\) and \(x=-j\), respectively, yields the
normalized full-frequency identity

\[
\begin{aligned}
 \mathcal C_+^{\rm full}
 &=\sum_{j=a_+}^{b_+-1}F_j(j+1)
   \sum_{s=a_+}^{j}G_N((j+1)^2-s),\\
 \mathcal C_-^{\rm full}
 &=\sum_{j=a_-+1}^{b_-}F_j(-j)
   \sum_{s=j}^{b_-}G_N(j^2-s).
\end{aligned}
\tag{158.R26}
\]

Let \(\mathcal Z_{\rm tr}\) and \(\mathcal F_{\rm tr}\) denote exactly
the normalized formulas (158.R18) with, respectively, \(v=0\) and
\(v=n=H/2\) in place of \(v\in\mathcal V_d^\circ\). Then the relation
between (158.R18) and (158.R26) is the identity

\[
 \mathcal C_{\rm int,U}(V)
 =\mathcal C_+^{\rm full}+\mathcal C_-^{\rm full}
  -\mathcal Z_{\rm tr}-\mathcal F_{\rm tr}.
\tag{158.R27}
\]

### 3.3 The removed frequencies are safe at trace level

In the accepted normalization, opening \(K\) gives, for any consecutive
integer interval \(I\) and any \(v\bmod H\),

\[
 \sum_{s\in I}K(-v^2,-s;c)
 =\sum_{u\bmod c}^{*}\alpha_{c,v}(u)
   \sum_{s\in I}e_c(-us),\qquad |\alpha_{c,v}(u)|=1.
\tag{158.R28}
\]

Every \(u\) is a nonzero unit modulo \(c\). The geometric-series bound
and harmonic summation over reduced residues give

\[
 \sup_I\left|\sum_{s\in I}K(-v^2,-s;c)\right|
 \ll c\log(2c).
\tag{158.R29}
\]

This proves (158.R29) separately for \(v=0\) and for \(v=n\); no
theorem for a complete zero or fold row has been transferred. The
extra trace phases have modulus one (at \(v=n\) they are the relevant
alternating signs). Using (158.R15) and the \(O(V)\) atoms on the two
blocks, either removed trace piece is at most

\[
\begin{aligned}
 &\frac{VM^{-3/4}X^\varepsilon}{Nq}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 d\sqrt c\,c\log(2c)\\
 &\quad\ll
 \frac{VM^{-3/4}X^\varepsilon}{Nq}
 q^{3/2}\sum_{d\mid N}d^{-1/2}\\
 &\quad\ll_\varepsilon
 VM^{-3/4}N^{-1/2}X^\varepsilon
 \le M^{-1/4}X^\varepsilon,
\end{aligned}
\tag{158.R30}
\]

because \(c=q/d\), \(q=4N\), and \(V\le\sqrt{NM}\). This proves
(158.R1), uniformly in every divisor stratum and at \(c=4\).

### 3.4 Complete endpoint root table

The endpoint \(s=j\) in (158.R26) contributes

\[
\begin{aligned}
 \mathcal E_{\rm full}
 ={}&\sum_{j=a_+}^{b_+-1}F_j(j+1)G_N(j^2+j+1)\\
 &+\sum_{j=a_-+1}^{b_-}F_j(-j)G_N(j^2-j).
\end{aligned}
\tag{158.R31}
\]

For \(f_-(j)=j(j-1)\), the two factors are coprime. Hence, for every
\(p^\nu\), all of \(p^\nu\) divides exactly one factor, and the only
roots are \(j\equiv0,1\pmod {p^\nu}\). This proves (158.R2), including
\(p=2\), and CRT gives exactly \(2^{\omega(N)}\) roots modulo \(N\)
(one root when \(N=1\)).

For \(f_+(j)=j^2+j+1\), there is no root modulo \(2\). Modulo \(3\),
\(j=1\) is the unique root, but every possible lift is \(j=1+3t\) and

\[
 (1+3t)^2+(1+3t)+1=3(1+3t+3t^2),
\tag{158.R32}
\]

which has exact \(3\)-adic valuation one. Thus no root exists modulo
\(9\) or any higher power. If \(p\ne2,3\), the discriminant is
\(-3\). A root is simple, so Hensel gives one lift at every higher
power for each root modulo \(p\). Quadratic reciprocity gives

\[
 \left(\frac{-3}{p}\right)=1
 \quad\Longleftrightarrow\quad p\equiv1\pmod3.
\tag{158.R33}
\]

This proves the complete table (158.R3). Equivalently,
\(\rho_+(N)=0\) if \(2\mid N\), if \(9\mid N\), or if an odd prime
\(p\equiv2\pmod3\) divides \(N\); in every other case

\[
 \rho_+(N)=2^{\omega(N)-\mathbf1_{3\mid N}}.
\tag{158.R34}
\]

The block lengths are \(<N\) in the frozen range (the finitely many
small \(N\) are harmless), so each root class occurs at most once in a
block. From (158.R15), (158.R31), and
\(2^{\omega(N)}\ll_\varepsilon N^\varepsilon\),

\[
 |\mathcal E_{\rm full}|
 \ll_\varepsilon M^{-3/4}X^\varepsilon
 \ll M^{-1/4}X^\varepsilon.
\tag{158.R35}
\]

### 3.5 Exact strict selected trace, support localization, and powers

Delete \(s=j\) from (158.R26). On the positive side put \(k=j+1\);
on the negative side put \(k=-j\). Since
\(G_N(k^2-s)=\mathbf1_{k^2-s=N\ell}\chi _4(\ell)\), the strict
physical trace is exactly

\[
\begin{aligned}
 \mathcal S_{\rm str}(V)
 ={}&\sum_{k=a_++1}^{b_+}W_+(k)
 \sum_{\substack{\ell\in\mathbb Z\\
          a_+\le k^2-N\ell\le k-2}}
 \chi _4(\ell)\\
 &+\sum_{k=-b_-}^{-a_--1}W_-(k)
 \sum_{\substack{\ell\in\mathbb Z\\
          -k+1\le k^2-N\ell\le b_-}}
 \chi _4(\ell),
\end{aligned}
\tag{158.R36}
\]

with \(W_\pm\) exactly as in (158.R5). The first line has
\(s<j=k-1\); the second has \(s>j=-k\). No endpoint, sign, profile
transition, or half-open choice has been replaced.

For \(k\ge1\), the integer intervals

\[
 I_k=[k^2-k+1,k^2+k]
\tag{158.R37}
\]

partition the positive integers, since the upper endpoint of \(I_k\)
is followed by the lower endpoint of \(I_{k+1}\). Let

\[
 \kappa(\ell)=
 \left\lfloor\sqrt{N\ell}+\frac12\right\rfloor
\tag{158.R38}
\]

be the unique \(k\) for which \(N\ell\in I_k\), and put

\[
 r(\ell)=\kappa(\ell)^2-N\ell
 \in[-\kappa(\ell),\kappa(\ell)-1].
\tag{158.R39}
\]

Then (158.R36) is (158.R4), with the literal selectors

\[
\begin{aligned}
 \eta_+(\ell)&=
 \mathbf1_{a_++1\le\kappa(\ell)\le b_+}
 \mathbf1_{a_+\le r(\ell)\le\kappa(\ell)-2},\\
 \eta_-(\ell)&=
 \mathbf1_{-b_-\le\kappa(\ell)\le-a_--1}
 \mathbf1_{-\kappa(\ell)+1\le r(\ell)\le b_-}.
\end{aligned}
\tag{158.R40}
\]

The endpoint cases excluded here are exactly
\(r=k-1\) on the positive side and \(r=-k\) on the negative side.
In a strict positive term,

\[
 \frac{k^2-k+1}{N}
 =\ell+\frac{r-k+1}{N}<\ell,
\tag{158.R41}
\]

whereas in a strict negative term

\[
 \frac{k^2+k}{N}
 =\ell+\frac{r+k}{N}>\ell.
\tag{158.R42}
\]

Thus the character is evaluated at the selected quotient \(\ell\), but
the positive and negative profiles are frozen just below and just above
that quotient, respectively. They are neither equal nor conjugate. The
two selectors in (158.R40) are disjoint because the first requires
\(r\ge a_+>0\), while the second requires \(r\le b_-<0\). Therefore
the union of the signed blocks supplies no termwise positive/negative
cancellation. Pairing \(\ell\) with \(\ell+2\) to reverse
\(\chi _4\) also gives no identity: \(\kappa\), \(r\), the strict
selector, the boundary profile argument, and the residual phase all
change, and no weight-preserving bijection is present in the frozen
algebra.

The \(w_U\)-support supplies \(O(MX^\varepsilon)\) possible quotients.
The strict \(k\)-ranges supply \(O(V)\) possible coordinates, and each
fixed \(k\) has at most one selected \(\ell\), since its \(s\)-interval
has length \(<N\). This proves (158.R7).

There is also an exact support test before using this cardinality. If

\[
\begin{aligned}
 &\left\{\frac{k^2-k+1}{N}:a_++1\le k\le b_+\right\}
 \cap\operatorname {supp}(w_U)=\varnothing,\\
 &\left\{\frac{k^2+k}{N}:-b_-\le k\le-a_--1\right\}
 \cap\operatorname {supp}(w_U)=\varnothing,
\end{aligned}
\tag{158.R43}
\]

then \(\mathcal S_{\rm str}(V)=0\), and in fact the whole moving-cell
trace is zero. On the inherited dyadic support
\(\operatorname {supp}(w_U)\asymp M\), a nonzero boundary weight has
\(k^2/N\asymp M\), while (158.R40) has \(k\asymp V\). Hence nonzero
trace forces

\[
 V\asymp K=\sqrt{NM}.
\tag{158.R44}
\]

This is a genuine trace-zero range whenever (158.R43) holds, but it
does not close the only nonzero range. Indeed,

\[
 \frac{K}{M}=\sqrt{\frac NM}\ge N^{1/4},
\tag{158.R45}
\]

so \(V\asymp K\) implies \(V\gg M\) and (158.R7) becomes only
\(L_{\rm str}\ll M X^\varepsilon\).

With

\[
 a:=M^{-3/4}X^\varepsilon,
\tag{158.R46}
\]

the complete power ledger is

| item | restored size |
|---|---:|
| one boundary-frozen atom | \(a\) |
| strict support | \(L_{\rm str}\ll\min(M,V)X^\varepsilon\), and \(L_{\rm str}\ll MX^\varepsilon\) on nonzero blocks |
| absolute strict trace | \(aL_{\rm str}\), hence at best \(aM=M^{1/4}X^\varepsilon\) |
| frozen scalar target | \(X^\varepsilon=aM^{3/4}\) |
| required raw saving on a full \(M\)-support | \(M\to M^{3/4}\), a factor \(M^{1/4}\) |
| hypothetical square-root trace | \(aL_{\rm str}^{1/2}\le aM^{1/2}=M^{-1/4}X^\varepsilon\), stronger than required |
| either removed \(v\)-row | \(aVN^{-1/2}X^\varepsilon\le aM^{1/2}X^\varepsilon\), stronger than required |
| full-frequency endpoint | \(aN^\varepsilon\), stronger than required |

Combining (158.R27), (158.R30), (158.R31), and (158.R36) proves the
reduction (158.R6).

### 3.6 Calibration against standard discrepancy and completion

Write \(W_\pm=a\widetilde W_\pm\). The raw signed estimate required by
the scalar target is

\[
 \left|\sum_{\ell\asymp M}\chi _4(\ell)
 \bigl(\eta_+(\ell)\widetilde W_+(\kappa(\ell))
      +\eta_-(\ell)\widetilde W_-(\kappa(\ell))\bigr)\right|
 \ll_\varepsilon M^{3/4}X^\varepsilon.
\tag{158.R46a}
\]

The selector is a sharp window in the nearest-integer error of
\(y_\ell=\sqrt{N\ell}\), because

\[
 r(\ell)=(\kappa(\ell)-y_\ell)
          (\kappa(\ell)+y_\ell).
\tag{158.R46b}
\]

Consider first the standard Erdős--Turán/second-derivative placement,
granting harmless normalized BV for the boundary weight and freezing
the slowly varying window endpoints. Splitting the period-four
character into residue classes leaves exponential sums with phase
\(h\sqrt{N\ell}\). On \(\ell\asymp M\),

\[
 \left|\frac{d^2}{d\ell^2}h\sqrt{N\ell}\right|
 \asymp \frac{hK}{M^2},
\]

so the second-derivative estimate gives

\[
 S_h\ll \sqrt{hK}+\frac{M}{\sqrt{hK}}.
\tag{158.R46c}
\]

Truncation at height \(H_0\) therefore has the capacity

\[
 D(M)\ll \frac{M}{H_0}+\sqrt{KH_0}+\frac{M}{\sqrt K}.
\tag{158.R46d}
\]

Optimizing the first two terms gives

\[
 D(M)\ll M^{1/3}K^{1/3}+\frac{M}{\sqrt K}.
\tag{158.R46e}
\]

For (158.R46e) to be at most \(M^{3/4}\), its first term requires

\[
 K\le M^{5/4}
 \quad\Longleftrightarrow\quad
 M\ge N^{2/3},
\tag{158.R46f}
\]

which is disjoint from the frozen \(M\le N^{1/2}\) range for large
\(N\).

The classical exponent-pair placement does not repair this. The pair
\((1/6,2/3)\) gives

\[
 S_h\ll h^{1/6}K^{1/6}M^{1/2}X^\varepsilon
\]

and hence, after optimizing Erdős--Turán,

\[
 D(M)\ll M^{4/7}K^{1/7}X^\varepsilon.
\tag{158.R46g}
\]

The condition \(D(M)\le M^{3/4}X^\varepsilon\) is again
\(K\le M^{5/4}\), hence again outside the frozen range. More generally,
an exponent pair \((\kappa_0,\lambda_0)\) inserted in this exact
discrepancy placement yields the model capacity

\[
 D(M)\ll
 K^{\kappa_0/(1+\kappa_0)}
 M^{\lambda_0/(1+\kappa_0)}X^\varepsilon.
\tag{158.R46h}
\]

At the least unfavorable frozen endpoint \(M=N^{1/2}\), where
\(K=M^{3/2}\), reaching raw \(M^{3/4}\) would require the sharp
interface inequality

\[
 \lambda_0+\frac34\kappa_0\le\frac34.
\tag{158.R46i}
\]

No exponent-pair theorem satisfying (158.R46i) and matching the literal
sharp selector and boundary-frozen coefficient is present in the
permitted dependencies. Equation (158.R46i) is a source/interface
requirement, not a claim that no such future theorem can exist.

Finally, even granting the ideal mixed coefficient norm, the accepted
centered incomplete-quadratic/rectangular completion has raw capacity
\(\sqrt N\,X^\varepsilon\). After restoring the atom scale it gives

\[
 a\sqrt N\,X^\varepsilon
 =M^{-3/4}N^{1/2}X^\varepsilon.
\tag{158.R46j}
\]

This is \(O(X^\varepsilon)\) only if \(M\ge N^{2/3}\), again outside
\(M\le N^{1/2}\). Thus recalibrating the target from
\(M^{-1/4}\) to \(1\) weakens the missing cancellation from raw
square-root size to raw \(M^{3/4}\), but the standard discrepancy,
classical exponent-pair, and accepted incomplete-quadratic placements
still retain a positive power throughout the frozen range.

## 4. First doubtful or unproved step

There is no doubtful step in the Abel signs and endpoints, the
full-frequency normalization, the separate zero/Nyquist trace bounds,
the local root tables, the support-zero test, or the selected-coordinate
identity under the printed hypotheses.

The first unproved assertion needed for the nonzero trace range is

\[
 \boxed{
 \left|\sum_{\ell\ge1}\chi _4(\ell)
 \left(\eta_+(\ell)W_+(\kappa(\ell))
      +\eta_-(\ell)W_-(\kappa(\ell))\right)\right|
 \ll_\varepsilon X^\varepsilon.}
\tag{158.R47}
\]

Equivalently, after dividing out the atom size
\(a=M^{-3/4}X^\varepsilon\), the required raw character-mask bound is
\(M^{3/4}X^\varepsilon\). Raw square-root cancellation
\(M^{1/2}X^\varepsilon\) would be sufficient but is stronger than
needed.

Endpoint roots cannot prove (158.R47). Indeed, in a positive strict
term with \(s=k^2-N\ell\le k-2\),

\[
 k^2-k+1=N\ell-(k-1-s),\qquad 1\le k-1-s<N,
\tag{158.R48}
\]

and in a negative strict term with \(s\ge-k+1\),

\[
 k^2+k=N\ell+(s+k),\qquad 1\le s+k<N.
\tag{158.R49}
\]

Thus strict terms are precisely disjoint from the two endpoint
congruences; their offsets are nonzero and vary with the selected row.

This is not only a formal possibility, even when \(V\) is required to
be dyadic. Let \(L=2^h\), \(h\ge3\), and set

\[
\begin{aligned}
 V&=L^2,& \ell&=M=L+1,\\
 k&=(L+1)(L+4),&
 s&=L(L+1),\\
 N&=(L+1)(L+4)^2-L.
\end{aligned}
\tag{158.R50}
\]

Then

\[
\begin{aligned}
 N\ell&=k^2-s,&
 V&<s<k-1\le2V,\\
 \chi _4(\ell)&=1,&
 k-1-s&=4L+3.
\end{aligned}
\tag{158.R51}
\]

Thus \(j=k-1\) and \(s\) lie in the same positive dyadic block and
\(s<j\), so this is a genuine positive strict selected point. Since
\(0<4L+3<N\), (158.R48) shows explicitly that its endpoint polynomial
is nonresonant. If the inherited component is nonzero at its displayed
boundary argument, it is a literal trace term. Moreover

\[
 \frac{k^2-k+1}{N}
 =\ell-\frac{4L+3}{N}\asymp M,\qquad
 K=\sqrt{NM}=\sqrt{k^2-s}\asymp k\asymp V.
\]

Thus the strict survivor occurs in exactly the support-localized top
range. This family is an arithmetic control, not a lower bound for the
full literal sum.

Nor does bounded partial summation of \(\chi _4\) close the gap. If

\[
 A_\ell=\eta_+(\ell)W_+(\kappa(\ell))
          +\eta_-(\ell)W_-(\kappa(\ell)),
\]

then \(\sup_T|\sum_{\ell\le T}\chi _4(\ell)|\le1\), but zero extension
of the exact sparse selector gives only

\[
 \sup_\ell|A_\ell|+\operatorname {Var}_\ell(A_\ell)
 \ll a(1+L_{\rm str})X^\varepsilon.
\tag{158.R52}
\]

Each entry and exit of the strict moving mask is a genuine transition;
continuous BV of \(w_U\) does not delete it. Abel summation with
(158.R52) reproduces (158.R8), namely \(aM=M^{1/4}\) on a full
nonzero support, still a factor \(M^{1/4}\) above the scalar target. An
argument using only amplitude and support would also apply to an
adversarial sign-aligned coefficient and therefore cannot be a signed
theorem. A new estimate must exploit the literal joint arithmetic of
\(r(\ell)\), \(\chi _4(\ell)\), the two boundary-frozen profiles, and
the residual phases. Section 3.6 shows that the standard discrepancy,
classical exponent-pair, and accepted incomplete-quadratic placements
do not reach even the weaker raw \(M^{3/4}\) threshold. No matching
estimate is contained in the permitted dependencies.

The Abel outer terms
\(A_{b_+}(v)P^+_{d,v}(b_+)\) and
\(A_{a_-}(v)P^-_{d,v}(a_-)\), and both profile-bulk lines in
(158.R20)/(158.R22), are quarantined outside (158.R47). This report
does not assert that they are target-safe; adjacent-block or global
recombination is a separate seam.

## 5. Control tests and outcomes

- literal_paired_interior_trace — **pass**. Equation (158.R18) retains
  every odd \(d\mid N\), both members of each complementary orbit, the
  exact exterior constant, and the \(c=4\) empty-interior case.
- positive_prefix_negative_suffix_signs — **pass**. The two moving
  atoms both enter positively; see (158.R20) and (158.R22).
- all_Abel_outer_endpoints — **pass/quarantined**. The positive right
  endpoint \(A_{b_+}P^+(b_+)\) and negative left endpoint
  \(A_{a_-}P^-(a_-)\), as well as both bulk remainders, are explicit.
  No target estimate for them is claimed.
- full_frequency_delta_inversion — **pass**. Equations
  (158.R23)--(158.R25) retain the half-period constant, \(dc=q\), the
  complete odd-divisor partition, and the exact \(G_N\) normalization.
- zero_trace_piece — **pass**. The actual prefix/suffix trace piece is
  bounded in (158.R28)--(158.R30), independently of the total zero row.
- Nyquist_trace_piece — **pass**. The same calculation applies
  separately at \(v=H/2=N/d\), including its alternating trace phases.
- endpoint_polynomial_p_adic_roots — **pass**. The exact tables at
  every prime power, including \(p=2,3\), are (158.R2)--(158.R3), with
  CRT formula (158.R34).
- strict_prefix_suffix_survivor — **obstruction retained**. The exact
  survivor is (158.R36)/(158.R4), not the endpoint row; the analytic
  family (158.R50) confirms a nonendpoint arithmetic survivor in the
  top physical range.
- selected_coordinate_boundary_weight — **pass**. Equations
  (158.R5), (158.R41), and (158.R42) distinguish the selected quotient
  from both literal off-integer boundary profile arguments.
- positive_negative_profiles_and_endpoints — **pass**. The two
  profiles, phases, strict ranges, and endpoint residues are not
  identified with one another; all inherited transitions remain in
  \(F_j\). The selectors are disjoint, so their union is not a
  cancellation identity.
- support_localization — **pass/no target**. Equation (158.R43) gives a
  genuine trace-zero condition. Every nonzero component has
  \(V\asymp K\gg M\), so its cardinality capacity is \(M\), not a
  target estimate.
- N_M_V_d_c_power_ledger — **pass**. The all-\(d\) removed-row
  calculation is (158.R30), and every physical selected power is listed
  after (158.R46), with the scalar target correctly set to
  \(O(X^\varepsilon)\).
- upper_capacity_vs_signed_sum — **pass/no gain**. Equation (158.R7)
  is support only; (158.R52) shows why ordinary
  \(\chi _4\)-Abel summation remains absolute. Neither raw
  \(M^{3/4}\) cancellation nor the stronger square-root theorem is
  inferred.
- standard_discrepancy_exponent_pair_completion — **no gain**. The
  second-derivative and classical exponent-pair capacities
  (158.R46e)/(158.R46g), and the accepted incomplete-quadratic capacity
  (158.R46j), become scalar-target sized only at
  \(M\ge N^{2/3}\), outside the frozen range. A different exponent pair
  would have to meet the explicit interface (158.R46i) and the literal
  coefficient hypotheses.
- profile_bulk_and_downstream_scope — **pass**. Equations (158.R20)
  and (158.R22) leave both profile-bulk differences and both outer
  endpoints outside this trace result. Nothing is transferred to the
  full paired matrix, \(D>1\), \(L>1\), generic \(t=1\), \(t\ge2\),
  cross, another M1 or M2 owner, endpoint uniformity, M9, the bridge,
  the quarter target, or either global exponent.

No numerical, symbolic, or web experiment was used.

## 6. Dependencies and exact artifacts used

This report used only the task brief and the selected Round-158
context:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- strategy/round158_d1_paired_interior_cell_trace_strategy.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/barrier_packet.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/candidates/conductor_round158_cell_trace_seed.md;
- proofs/kernels/m9_m1_d1_nonzero_centering_nyquist_fold.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reports/centered_nonzero_root_discrepancy_attack.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-nonzero-theta-matrix-gate/reviews/conductor_round157_adjudication.md; and
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/briefs/sign_adapted_cell_trace_attack.md.

The inversion uses the accepted complete half-period inverse-Gauss
normalization and exact odd-divisor recombination already frozen in the
Round-157 kernel. No sibling Round-158 report, shared state, proof
draft, validation matrix, synthesis, review, control artifact, or State
Patch was read or edited.

## 7. Recommended state effect

Recommend **retain** the paired-interior trace target as open and close
this task under paired_interior_cell_trace_no_go. After independent
sign, endpoint, and power review, the conductor may promote only the
following narrow facts:

1. the exact sign-adapted Abel decomposition, including both outer
   endpoints and both bulk remainders;
2. the full-frequency trace identity and the separate target-safe
   \(v=0\) and \(v=H/2\) trace bounds;
3. the complete endpoint root table, the target-safe full-frequency
   endpoint row, and the exact support-zero condition; and
4. the exact equivalence (158.R6) between the open paired-interior trace
   and the strict boundary-frozen selected sum modulo a
   stronger-than-required \(M^{-1/4}X^\varepsilon\) error.

Retain (158.R47) as the first open signed input. Reject any inference
that endpoint root multiplicity controls strict prefixes or suffixes,
that \(\min(M,V)\) is cancellation, that support localization controls
the nonzero top block, that positive and negative selectors or
\(\ell,\ell+2\) terms pair automatically, that ordinary
\(\chi _4\)-Abel summation removes the sparse-mask variation, that the
standard discrepancy or incomplete-quadratic capacities reach the raw
\(M^{3/4}\) threshold in the frozen range, that the
unproved Abel outer terms are safe, or that a trace result controls the
profile bulk or any downstream owner. No direct shared state change is
made by this report.
