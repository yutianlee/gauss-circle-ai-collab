# Round 158 strategy: paired-interior moving-cell trace

## 1. Accepted starting point

Round 157 proves the exact centered nonzero interface and the unique
Nyquist fold. Fix \(A>0\) and put

\[
 q=4N,\qquad K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\le K.
\tag{158.S1}
\]

For every odd \(d\mid N\), put

\[
 c=\frac qd,\qquad H=\frac c2,\qquad n=\frac Nd,
\qquad
 \mathcal V_d^\circ=
 \{v\bmod H:v\ne0,\ v\ne H/2\}.
\tag{158.S2}
\]

The first open matrix is the paired interior part

\[
\begin{aligned}
 \mathcal T_{\mathrm{int},U}(V)
 =-\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c
 \sum_{v\in\mathcal V_d^\circ}
 \widehat B_j(2dv)K(-v^2,-j;c).
\end{aligned}
\tag{158.S3}
\]

The set \(\mathcal V_d^\circ\) contains both members of every
two-element orbit. Equivalently one may use
\(\widehat B_j(2dv)+\widehat B_j(-2dv)\) for
\(1\le v<H/2\). No conjugacy is available.

Write the literal coefficient on one physical lift as

\[
 B_j(x)=\mathbf 1_{x\ge\lambda_\sigma(j)}F_j(x),
 \qquad
 \lambda_+(j)=j+1,\qquad
 \lambda_-(j)=-j.
\tag{158.S4}
\]

Here \(F_j\) retains the actual zero-extended profile, exact residual
phase, all profile and support transitions, half-open conventions, and
hard endpoints. Round 157 shows that the moving boundary in (158.S4) is
the first explicit diagonal trace not controlled by one-variable BV.

## 2. Exact sign-adapted Abel trace

Let \(J_+=[a_+,b_+]\) and \(J_-=[a_-,b_-]\) denote the two consecutive
strict signed blocks. For

\[
 K_{d,v}(s)=K(-v^2,-s;c),
\tag{158.S5}
\]

define the sign-adapted kernel sums

\[
 P_{d,v}^+(j)=\sum_{s=a_+}^{j}K_{d,v}(s),
 \qquad
 P_{d,v}^-(j)=\sum_{s=j}^{b_-}K_{d,v}(s).
\tag{158.S6}
\]

The exact coefficient differences are

\[
\begin{aligned}
 \widehat B_{j+1}(2dv)-\widehat B_j(2dv)
 &=-F_j(j+1)e_c(-2v(j+1))\\
 &\quad+
 \sum_{x\ge j+2}\bigl(F_{j+1}(x)-F_j(x)\bigr)e_c(-2vx)
\end{aligned}
\tag{158.S7}
\]

on \(J_+\), and

\[
\begin{aligned}
 \widehat B_j(2dv)-\widehat B_{j-1}(2dv)
 &=F_j(-j)e_c(2vj)\\
 &\quad+
 \sum_{x\ge-j+1}\bigl(F_j(x)-F_{j-1}(x)\bigr)e_c(-2vx)
\end{aligned}
\tag{158.S8}
\]

on \(J_-\). The displayed first lines are the only moving-mask atoms.
Using prefix Abel on \(J_+\) and suffix Abel on \(J_-\), define

\[
\begin{aligned}
 \mathcal C_{+,d}
 &=\sum_{j=a_+}^{b_+-1}F_j(j+1)
 \sum_{v\in\mathcal V_d^\circ}
 e_c(-2v(j+1))P_{d,v}^+(j),\\
 \mathcal C_{-,d}
 &=\sum_{j=a_-+1}^{b_-}F_j(-j)
 \sum_{v\in\mathcal V_d^\circ}
 e_c(2vj)P_{d,v}^-(j).
\end{aligned}
\tag{158.S9}
\]

The normalized paired-interior cell trace is

\[
 \mathcal C_{\mathrm{int},U}(V)
 =-\frac{i(1+i)}{2Nq}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi_4(d)d\sqrt c
 \left(\mathcal C_{+,d}+\mathcal C_{-,d}\right).
\tag{158.S10}
\]

The first objective is to rederive (158.S7)--(158.S10) independently,
including every endpoint term and the sign of the suffix formula.

## 3. Full-frequency physical control and the endpoint trap

For a physical point \(x\) and row \(s\), exact half-period inversion
gives

\[
\begin{aligned}
 \Phi_d(x,s)
 &:=
 \sum_{v\bmod H}e_c(-2vx)K(-v^2,-s;c)\\
 &=\frac{1-i}{2}\sqrt c
 \sum_{u\bmod c}^{*}\chi_4(u)e_c(u(x^2-s)).
\end{aligned}
\tag{158.S11}
\]

After the exterior all-\(d\) recombination, the full-frequency versions
of (158.S9) are exactly

\[
\begin{aligned}
 \mathcal C_+^{\mathrm{full}}
 &=\sum_{j=a_+}^{b_+-1}F_j(j+1)
 \sum_{s=a_+}^{j}G_N((j+1)^2-s),\\
 \mathcal C_-^{\mathrm{full}}
 &=\sum_{j=a_-+1}^{b_-}F_j(-j)
 \sum_{s=j}^{b_-}G_N(j^2-s).
\end{aligned}
\tag{158.S12}
\]

The interior trace is not automatically equal to (158.S12): the
\(v=0\) and \(v=H/2\) Abel-trace pieces must be subtracted and bounded
separately. The already proved total zero and fold rows cannot be
silently transferred to their individual Abel pieces.

The diagonal endpoints \(s=j\) in (158.S12) are

\[
 G_N(j^2+j+1),\qquad G_N(j^2-j).
\tag{158.S13}
\]

Their congruences have \(N^\varepsilon\)-scale root multiplicity:
\(j(j-1)\equiv0\pmod N\) has exactly \(2^{\omega(N)}\) residue classes,
while \(j^2+j+1\equiv0\pmod N\) has at most two classes per odd prime
away from the exceptional \(3\)-adic case, no \(2\)-adic class, and no
lift beyond modulus \(3\) at \(3\). This p-adic statement must be
proved, not assumed.

Crucially, (158.S13) is only the endpoint of each prefix or suffix.
The strict trace also contains \(s<j\) on the positive side and
\(s>j\) on the negative side. Since \(V<N\), each fixed \(j\) has at
most one selected \(s\), but the total support can still be
\(\min(M,V)X^\varepsilon\). Endpoint root counts alone therefore do not
close (158.S10).

## 4. Selected-coordinate form

In the positive trace set \(k=j+1\). A selected pair obeys

\[
 k^2-s=N\ell,\qquad a_+\le s\le k-1,
\tag{158.S14}
\]

and contributes the boundary-frozen coefficient \(F_{k-1}(k)\) with
\(\chi_4(\ell)\). In the negative trace set \(k=-j\). Then

\[
 k^2-s=N\ell,\qquad -k\le s\le b_-,
\tag{158.S15}
\]

and the coefficient is \(F_{-k}(k)\).

The nearest-cell intervals partition the positive integers, so there
is at most one selected \(k\) per positive \(\ell\). This recovers the
capacity

\[
 L_{\mathrm{trace}}(V)
 \ll_\varepsilon\min(M,V)X^\varepsilon.
\tag{158.S16}
\]

Equation (158.S16) is unsigned. A square-root signed theorem for the
literal boundary-frozen weights would be target-safe for every \(V\),
but this must be proved with the actual \(\chi_4(\ell)\), residual
phase, profiles, transitions, both signs, and endpoints.

## 5. Mechanisms and controls

The round tests:

1. exact sign-adapted Abel decomposition and endpoint bookkeeping;
2. exact full-frequency physical inversion of the trace;
3. separate target bounds for the zero-frequency and Nyquist trace
   pieces, rather than transfer from their total rows;
4. complete p-adic root counts for the two endpoint polynomials;
5. an exact selected-coordinate rewrite of the strict trace;
6. signed cancellation in the boundary-frozen selected sum;
7. primary fixed-modulus or incomplete-quadratic sources against that
   exact coefficient; and
8. the remaining profile-bulk difference after the trace is removed.

The following are forbidden gains:

- treating (158.S13) as the whole trace;
- using endpoint root multiplicity to bound strict prefixes or suffixes;
- calling (158.S16) cancellation;
- subtracting the closed zero or fold row without bounding its trace
  piece;
- reopening complete \(v\)-resummation, ordinary centered completion,
  separated fixed-\(v\) estimates, or physical-diagonal-only Parseval;
- dropping either complementary mode, a large-\(d\) fold, a profile
  transition, a strict endpoint, or the external scalar seam; and
- transferring a trace result to the profile bulk, full paired matrix,
  another owner, M9, or a global exponent.

## 6. Round tasks and exit rule

Use three orthogonal tasks:

1. derive and attack the exact sign-adapted trace (158.S7)--(158.S16);
2. blindly rederive the trace from the statement-only paired matrix and
   test whether the endpoint-polynomial route closes more than the
   diagonal subrow; and
3. audit primary incomplete quadratic, polynomial-character,
   fixed-modulus root, and trace-relevant spectral theorems against the
   exact boundary-frozen selected sum.

Close under exactly one label:

- paired_interior_cell_trace_target;
- strict_paired_interior_cell_trace_range; or
- paired_interior_cell_trace_no_go.

No next round begins before adjudication and graph validation.

## 7. Downstream scope

Round 158 treats only the moving-mask trace inside the paired interior
\(D=d=L=1\) outer-defect row. Even a full trace theorem leaves the
profile-bulk coefficient differences to be proved. Every \(D>1\),
\(L>1\), generic \(t=1\), original \(t\ge2\), cross, remaining M1, and
M2 owner remains separate. Endpoint uniformity, M9, the bridge, the
quarter theorem, the internal exponent \(1/3\), and the audited
external Li--Yang exponent remain unchanged unless separately proved.
