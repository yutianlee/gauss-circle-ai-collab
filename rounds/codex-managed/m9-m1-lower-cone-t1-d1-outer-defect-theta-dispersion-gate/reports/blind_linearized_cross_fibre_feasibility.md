# 1. Result: literal reduction and surrogate no-go control

**Result.** Directly from the blind statement, one obtains an exact selected
reindexing, a selected-only residual-phase error, an elementary
incidence/capacity ledger, and an exact signed partial-sum seam. Those are the
literal conclusions of this report.

Separately, Sections 2.4 and 3.5 define an **ordinary-K blind surrogate**:
there \(K(A,B;q)\) is the ordinary Kloosterman kernel explicitly defined in
this report, with no additional theta multiplier. For that surrogate alone,
the standard unnormalised finite Fourier transform followed by the complete
half-period \(v\)-sum is an exact inverse quadratic-Gauss transform. It
restores the pre-transform coefficient row, coupled to a Salié-type kernel in
the original root variable. The surrogate \(v=0\) term is
\(\widehat B_j(0)c_q(j)\). None of these statements identifies that kernel or
zero mode with an unspecified project theta completion. Such identification
requires an external normalization and multiplier match before promotion.

For the actual selected points there is an exact reduction. The cell
\(-k\leq j\leq k-1\) assigns a unique \(k\) to every positive integer \(Nn\).
Writing

\[
 t_n=\sqrt{Nn},\qquad k_n=k(Nn),\qquad
 \delta_n=t_n-k_n,\qquad j_n=k_n^2-Nn,
\]

one has \(|\delta_n|<1/2\) and

\[
 j_n=-2k_n\delta_n-\delta_n^2,\qquad
 e\!\left(-\frac{j_n}{2k_n}\right)
 =e(t_n)e\!\left(\frac{\delta_n^2}{2k_n}\right).
\]

Replacing only the last residual factor by \(1\), on the already selected
graph and without changing any endpoint, costs

\[
 O_\varepsilon\!\left(
 M^{-3/4}X^\varepsilon\frac{M}{K}\right)
 =O_\varepsilon\!\left(
 X^\varepsilon N^{-1/2}M^{-1/4}\right).
\]

This does not justify linearising an ambient coefficient before selection.

The elementary modular-root capacity is

\[
 I(V):=\#\{n:n\text{ occurs in the selected block}\}
 \ll_\eta \min(M,VN^\eta).
\]

Absolute values therefore give only
\(M^{-3/4}I(V)X^\varepsilon\). A transform that loses selected sparsity and
asserts merely square-root cancellation among the \(O(VN^\eta)\) restored
defect incidences has capacity

\[
 X^\varepsilon M^{-3/4}V^{1/2}.
\]

This closes at most \(V\leq M^{3/2}X^{o(1)}\); at \(V=K\) it is
\(X^\varepsilon N^{1/4}M^{-1/2}\). This is an upper-bound capacity, not a
signed lower bound. Genuine square-root cancellation in the actual
\(I(V)\leq M\) selected points would be more than enough, but it does not
follow from the ordinary-K surrogate transform, Cauchy--Parseval, a raw
collision count, or an arbitrary-coefficient fixed-modulus large sieve.

Accordingly, neither the full target nor a strict owner-complete
positive-power subrange is proved here. The rigorous literal obstruction is
the missing signed selected cross-fibre estimate. The inverse-transform
calculation is only a mechanism control for the explicitly defined ordinary-K
surrogate, not a no-go theorem for an unmatched project theta completion.

# 2. Exact statement and hypotheses

Assume exactly the blind-statement hypotheses: \(X\) is large,
\(N=\lfloor X\rfloor\), \(1\ll M\leq X^{1/2}\),
\(K=\sqrt{NM}\),
\(M^{3/4}(\log(2X))^A<V\leq K\), and \(w_U\) is the literal
zero-extended bounded-variation profile supported on \(n\asymp M\), with

\[
 \|w_U\|_\infty+\operatorname {Var}(w_U)
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\]

All assertions are uniform in the support components of that literal
profile. No smoothness beyond bounded variation is assumed.

Define

\[
 C_k=[k^2-k+1,k^2+k]\cap\mathbb Z\qquad(k\geq1).
\]

The following five assertions form the precise no-go lemma.

1. **Literal selected reduction.** The \(C_k\) partition the positive
   integers. Hence \(k_n\) above is unique, and

   \[
   \mathcal Q_U(V)=
   \sum_{\substack{n\geq1,\ n\ {\rm odd}\\V<|j_n|\leq2V}}
       \chi_4(n)w_U(n)e(t_n)
       e\!\left(\frac{\delta_n^2}{2k_n}\right).
   \tag{2.1}
   \]

   The strict lower and closed upper dyadic endpoints are retained. Positive
   defect is exactly \(\delta_n<0\), and negative defect is exactly
   \(\delta_n>0\).

2. **Selected-only linearisation.** When the selector in (2.1) is left
   literal, one has

   \[
   \mathcal Q_U(V)=
   \sum_{\substack{n\geq1,\ n\ {\rm odd}\\V<|j_n|\leq2V}}
     \chi_4(n)w_U(n)e(t_n)
   +O_\varepsilon(X^\varepsilon N^{-1/2}M^{-1/4}).
   \tag{2.2}
   \]

3. **Exact character selector.** For every integer \(s\), with \(q=4N\),

   \[
   {\bf1}_{N\mid s}\chi_4(s/N)
   =-\frac{i}{2N}
     \sum_{\substack{a\ ({\rm mod}\ q)\\a\ {\rm odd}}}
       \chi_4(a)e_q(as),
   \tag{2.3}
   \]

   where the left side is zero when the quotient is even. Thus parity and
   character form a joint \(k^2-j\) selector; they are not a character of
   \(j\) or \(k\) separately.

4. **Blind ordinary-K surrogate/invertibility control.** Put \(Q=q/2\),
   define

   \[
   e_q(z)=e(z/q),\qquad
   K(A,B;q)=\sum_{x\ ({\rm mod}\ q)}^*e_q(Ax+B\bar x),
   \qquad
   \widehat B(2v)=\sum_{r\ ({\rm mod}\ Q)}B(r)e_q(-2vr),
   \]

   and let \(B\) be any coefficient row on \(\mathbb Z/Q\mathbb Z\). This
   explicitly defined \(K\) is the ordinary Kloosterman kernel; no project
   theta multiplier is present. For this surrogate, and only for it,

   \[
   \begin{aligned}
   &\sum_{v\ ({\rm mod}\ Q)}
       \widehat B(2v)K(-v^2,-j;q)\\
   &\quad=\sqrt Q\sum_{r\ ({\rm mod}\ Q)}B(r)
       \sum_{x\ ({\rm mod}\ q)}^*
          \gamma_q(x)e_q((r^2-j)\bar x),
   \end{aligned}
   \tag{2.4}
   \]

   where

   \[
   \gamma_q(x)=Q^{-1/2}
      \sum_{v\ ({\rm mod}\ Q)}e_q(-xv^2),
   \qquad |\gamma_q(x)|=1
   \quad ((x,q)=1).
   \tag{2.5}
   \]

   Formula (2.4) is rowwise. If a surrogate coefficient is \(B_j\), it
   restores \(B_j(r)\), not a separated surrogate independent of \(j\). Its
   ordinary-K surrogate \(v=0\) summand is

   \[
   \widehat B_j(0)K(0,-j;q)=\widehat B_j(0)c_q(j).
   \tag{2.6}
   \]

5. **Power limitation of the ordinary-K norm-only surrogate.** A proposed
   conclusion based only on (2.4), Gauss/Weil magnitudes, Cauchy--Parseval,
   and an
   arbitrary-coefficient square-root estimate over all restored defect rows
   has, after the surrogate coefficient norm is restored, no better formal
   capacity than

   \[
   M^{-3/4}V^{1/2}X^{O(\eta)}.
   \tag{2.7}
   \]

   It cannot cover a fixed-power range with \(V>M^{3/2}\). Formula (2.7) is
   not a claim that the literal sum has this size; it is the first power
   obstruction for that norm-only route.

# 3. Proof or derivation

## 3.1 Exact cell partition and phase

For \(S=Nn\geq1\) and \(j=k^2-S\),

\[
 -k\leq j\leq k-1
 \quad\Longleftrightarrow\quad
 k^2-k+1\leq S\leq k^2+k.
\]

The upper endpoint of \(C_k\) is \(k^2+k\), and the lower endpoint of
\(C_{k+1}\) is \(k^2+k+1\). Also \(C_1=\{1,2\}\). Hence the cells are
disjoint and cover all positive integers. This proves uniqueness of \(k_n\)
and (2.1). Since \(n\asymp M\), one has \(k_n\asymp K\).

Set \(t_n=k_n+\delta_n\). The lower cell endpoint exceeds
\((k_n-1/2)^2\), and the upper endpoint is below
\((k_n+1/2)^2\). Thus \(-1/2<\delta_n<1/2\). Direct algebra gives

\[
 j_n=k_n^2-t_n^2=-2k_n\delta_n-\delta_n^2
\]

and

\[
 -\frac{j_n}{2k_n}
 =\delta_n+\frac{\delta_n^2}{2k_n}.
\]

Because \(k_n\) is integral, \(e(\delta_n)=e(t_n)\). In particular,

\[
\begin{array}{ll}
 j_n>0:& \delta_n<0,\quad
 V<-2k_n\delta_n-\delta_n^2\leq2V,\quad j_n\leq k_n-1,\\[2mm]
 j_n<0:& \delta_n>0,\quad
 V<2k_n\delta_n+\delta_n^2\leq2V,\quad |j_n|\leq k_n.
\end{array}
\tag{3.1}
\]

Thus both branches and the one-unit cell asymmetry remain literal.

Since

\[
 \left|e\!\left(\frac{\delta_n^2}{2k_n}\right)-1\right|
 \ll k_n^{-1}\ll K^{-1},
\]

the selected linearisation error is at most

\[
 \|w_U\|_\infty\frac{\#\{n\asymp M\}}K
 \ll_\varepsilon
 M^{-3/4}X^\varepsilon\frac{M}{\sqrt{NM}}
 =X^\varepsilon N^{-1/2}M^{-1/4}.
\]

No selector boundary moved. This estimate says nothing about an ambient
coefficient evaluated away from the selected graph.

## 3.2 Bounded variation isolates the signed seam

For any finite sequence \(a_n\), summation by parts with literal zero
extension gives

\[
 \left|\sum_n w_U(n)a_n\right|
 \leq
 (\|w_U\|_\infty+\operatorname {Var}w_U)
 \sup_I\left|\sum_{n\in I}a_n\right|,
 \tag{3.2}
\]

up to an absolute endpoint constant, where \(I\) ranges over integer
intervals. The zero-extension jumps and all support-component transitions
are included in \(\operatorname {Var}w_U\). Applied to (2.2), the needed new
theorem is

\[
 \sup_{I\subset\{n\asymp M\}}
 \left|
 \sum_{\substack{n\in I,\ n\ {\rm odd}\\V<|j_n|\leq2V}}
     \chi_4(n)e(\sqrt{Nn})
 \right|
 \ll_\eta X^\eta M^{3/4}.
 \tag{3.3}
\]

This is the exact signed selected cross-fibre seam. It is not a consequence
of bounded variation.

## 3.3 Incidence and collision ledger

For \(0<|j|<N\), let

\[
 \rho_N(j)=\#\{x\ ({\rm mod}\ N):x^2\equiv j\pmod N\}.
\]

Prime-power analysis gives, for every \(\eta>0\),

\[
 \rho_N(j)\ll_\eta N^\eta (N,j)^{1/2}.
 \tag{3.4}
\]

Indeed, at \(p^a\Vert N\), if \(b=v_p(j)<a\), solutions require \(b\)
even. Extracting \(p^{b/2}\) leaves at most two unit roots for odd \(p\)
and at most four for \(p=2\), with at most \(p^{b/2}\) lifts. If
\(b\geq a\), there are \(p^{\lfloor a/2\rfloor}\) roots. Multiplication over
prime powers costs only \(N^\eta\).

The support has \(k\asymp K\), and \(K\ll N^{3/4}<N\). For large \(X\), each
residue class modulo \(N\) occurs at most once in the full relevant
\(k\)-interval. Also \(2V<N\). Hence

\[
\begin{aligned}
 I(V)
 &\leq \sum_{V<|j|\leq2V}\rho_N(j)\\
 &\ll_\eta N^\eta
     \sum_{V<|j|\leq2V}(N,j)^{1/2}
 \ll_\eta VN^{2\eta}.
\end{aligned}
\tag{3.5}
\]

For the last inequality, majorise \((N,j)^{1/2}\) by
\(\sum_{d\mid(N,j)}d^{1/2}\) and interchange the \(j,d\) sums. The endpoint
term is \(O(VN^\eta)\), since \(V\gg1\). The cell partition also gives
\(I(V)\ll M\). Relabelling \(2\eta\) proves the stated bound.

Thus

\[
 |\mathcal Q_U(V)|
 \ll_\varepsilon
 X^\varepsilon M^{-3/4}\min(M,VX^\varepsilon).
 \tag{3.6}
\]

Near the lower collar this gives only polylogarithmic extensions, which can
be absorbed into \(X^\varepsilon\); it gives no fixed positive-power range.

There is no literal sign pairing in (3.5). For fixed \(n\) there is one cell
and one defect sign. For fixed relevant \(k\), the interval
\([-2V,2V]\) has length \(4V<N\) for large \(X\), so there is at most one
congruent defect.
The map \(j\mapsto-j\) changes the root equation and need not preserve the
quotient character. For composite \(N\), a collision
\(k_1^2\equiv k_2^2\pmod N\) implies only
\(N\mid(k_1-k_2)(k_1+k_2)\); complementary divisors can create nontrivial
collisions. Neither a raw root count nor a collision count carries the sign
of the original sum.

## 3.4 Exact joint character selector

Write \(a=b+4\ell\), where \(b\in\{1,3\}\) and \(0\leq\ell<N\). If
\(N\nmid s\), the sum over \(\ell\) on the right of (2.3) is zero. If
\(s=Nn\), it equals \(N\), and

\[
 \sum_{b\in\{1,3\}}\chi_4(b)e_4(bn)
 =\begin{cases}
 2i\chi_4(n),&n\ {\rm odd},\\
 0,&n\ {\rm even}.
 \end{cases}
\]

Multiplication by \(-i/(2N)\) proves (2.3). The exact selector factor is
\(N^{-1}\), but its Fourier phase is \(e_q(a(k^2-j))\). Extracting a
character of \(j\) alone, or replacing the coefficient depending on
\((k^2-j)/N\) by a tensor product, is not an algebraic consequence of
(2.3).

## 3.5 Blind ordinary-K half-period surrogate

Everything in this subsection concerns only the ordinary Kloosterman kernel
defined in Section 2.4. The blind statement does not specify a theta
multiplier or a completed coefficient, so no identity in this subsection is
attributed to the literal project completion without an external
normalization match.

Expand both transforms on the left of (2.4). Interchanging finite sums gives

\[
 \sum_rB(r)\sum_x^*e_q(-j\bar x)
   \sum_{v\ ({\rm mod}\ Q)}e_q(-xv^2-2rv).
 \tag{3.7}
\]

Since \(x\) is a unit modulo \(q\), completing the square gives

\[
 \sum_{v\ ({\rm mod}\ Q)}e_q(-xv^2-2rv)
 =e_q(\bar x r^2)
   \sum_{v\ ({\rm mod}\ Q)}e_q(-xv^2).
 \tag{3.8}
\]

The last summand is periodic modulo \(Q=q/2\). The full quadratic Gauss sum
modulo \(q\equiv0\pmod4\) is twice this half sum. For odd \(x\) coprime to
\(q\), its magnitude is \(\sqrt{2q}\); hence the half sum has magnitude
\(\sqrt{q/2}=\sqrt Q\). Equations (3.7)--(3.8) prove (2.4)--(2.5).
They show that the \(v\)-sum has inverted the Fourier transform and restored
\(B(r)\), rather than supplied an independent square root. With \(B=B_j\),
every ambient row remains distinct.

For comparison only, suppose an external completion were independently shown
to have exactly a modulus \(q_d=q/d\), an odd divisor \(d\mid N\), Fourier
factor \(q^{-1}\), quadratic Gauss factor \(d\sqrt{q_d}\), the same ordinary-K
kernel, the same transform convention, and no extra \(v\)-dependent
multiplier. Under those additional hypotheses, its conditional
normalisation ledger would be

\[
 q^{-1}d\sqrt{q_d}\sqrt{q_d/2}
 =\frac1{\sqrt2},
 \tag{3.9}
\]

because \(dq_d=q\). If that external normalization also contained exactly a
\((1+i)\) multiplier, its magnitude would cancel \(\sqrt2\). This is
conditional bookkeeping for the ordinary-K surrogate. The blind statement
defines no completion gcd variable \(d\), so (3.9) proves no literal
\(d\)-statement and is not promotable without the stated external match.

Within the ordinary-K surrogate, its zero mode must be removed before a
nonzero-mode estimate. Since inversion permutes the units,

\[
 K(0,-j;q)=\sum_x^*e_q(-j\bar x)=c_q(j).
\]

For a surrogate row, the BV assumption gives no identity
\(\widehat B_j(0)=0\). Moreover,
\(\sum_{V<|j|\leq2V}|c_q(j)|\ll_\eta VX^\eta\), but this is only an
absolute \(V\)-capacity. It is not a statement about an unspecified
theta-multiplied project zero mode.

With the unnormalised transform, Parseval is the equality

\[
 \sum_{v\ ({\rm mod}\ Q)}|\widehat B_j(2v)|^2
 =Q\sum_{r\ ({\rm mod}\ Q)}|B_j(r)|^2.
 \tag{3.10}
\]

For two surrogate rows it gives their exact correlation

\[
 \sum_v\widehat B_{j_1}(2v)
       \overline{\widehat B_{j_2}(2v)}
 =Q\sum_rB_{j_1}(r)\overline{B_{j_2}(r)},
 \tag{3.11}
\]

not orthogonality of \(j_1\) and \(j_2\). Thus surrogate post-selection
Cauchy--Parseval preserves the coefficient norm. Even inside that surrogate,
moving (3.10) or (3.11) before an independently imposed selected restriction
changes the coefficient rows. No project-completion equivalence is asserted.

## 3.6 Literal \(N\)-\(M\)-\(V\) power and conditional \(d\)-bookkeeping

Directly from the blind statement, the profile contributes
\(M^{-3/4}X^\varepsilon\), and the defect capacity is
\(VX^{O(\eta)}\) by (3.5). Thus literal absolute estimation has power
\(M^{-3/4}V\). Even granting a square root of that \(V\)-incidence capacity
gives

\[
 M^{-3/4}V^{1/2}X^{O(\eta)}.
\]

This is nonpositive only for

\[
 V\leq M^{3/2}X^{o(1)}.
\]

At \(V=K=\sqrt{NM}\), it becomes

\[
 M^{-3/4}K^{1/2}=N^{1/4}M^{-1/2},
\]

which is \(O(1)\) uniformly only at the extreme
\(M\asymp N^{1/2}\), not throughout the blind-statement range. These are
right-side
powers. They do not prove a lower bound for \(|\mathcal Q_U(V)|\), and they
do not exclude a stronger coefficient-sensitive estimate retaining
\(I(V)\leq M\).

No variable \(d\) occurs in the blind statement. The cancellation of
hypothetical \(q,d,q_d\) factors in (3.9) belongs only to the matched
ordinary-K surrogate described in Section 3.5 and has no literal state
effect.

# 4. First doubtful or unproved step

The first unproved step is the literal signed partial-sum estimate (3.3),
with both defect branches and the hard selector retained. No cancellation
estimate for

\[
 \sum_{\substack{n\in I,\ n\ {\rm odd}\\V<|j_n|\leq2V}}
   \chi_4(n)e(\sqrt{Nn})
\]

has been proved from the stated hypotheses.

The ordinary-K half-period calculation cannot be cited as that estimate: it
is an invertible self-return for its explicitly defined surrogate, and no
theta-multiplier normalization match is available in the blind statement.
Surrogate Cauchy--Parseval produces (3.10)--(3.11), including its positive
diagonal and row collisions. A fixed-modulus arbitrary-coefficient large
sieve cannot be transferred to the literal block without a theorem whose
hypotheses cover the actual coupled coefficient. A modulus-average theorem is
a different interface because \(N\) is fixed. The positive diagonal,
collision capacity, and right side in (2.7) are not signed lower bounds, so
they do not refute the target. They mark the exact place where the norm-only
model stops.

# 5. Required control tests and outcomes

1. **literal_outer_defect_block — pass.** Equation (2.1) is an exact
   reindexing by the cells \(C_k\); no point is added or removed.

2. **selected_ambient_equivalence_and_linearization_scope — pass/no-go.**
   The residual-phase error (2.2) is proved only after literal selection.
   Extending it to an ambient coefficient is unjustified. The exact selector
   (2.3) is literal algebra. The inverse transform (2.4) applies only to the
   ordinary-K surrogate and requires an external theta-normalization match.

3. **positive_negative_defect_and_cell_endpoints — pass.** Formula (3.1)
   retains \(j>0\), \(j<0\), \(j\in[-k,k-1]\), and
   \(V<|j|\leq2V\). No \(j\leftrightarrow-j\) pairing is available.

4. **N_M_V_d_power_ledger — pass with scope qualification.** The literal
   profile power is \(M^{-3/4}\), and the square-root incidence capacity is
   \(V^{1/2}\). The result is \(M^{-3/4}V^{1/2}\), closing at most
   \(V\leq M^{3/2}\); at \(V=K\) it is \(N^{1/4}M^{-1/2}\). The blind
   statement defines no \(d\). Formula (3.9) is only conditional
   ordinary-K-surrogate bookkeeping and has no literal \(d\)-conclusion.

5. **actual_profile_transitions_and_B11 — scoped pass.** Zero extension,
   every support component, and all transition jumps are retained through
   (3.2). No decomposition of the actual coupled coefficient is made. The
   blind statement gives no definition or hypothesis for the external
   \(B_{1,U}(1)\) seam, so no claim about that separate seam is made.

6. **Cauchy_Parseval_diagonal_and_collision_scope — pass/no-go.**
   Equations (3.10)--(3.11) show exact norm preservation and row correlation
   for the ordinary-K surrogate. The literal root-collision discussion in
   Section 3.3 retains composite-modulus collisions. Diagonal and collision
   masses are only positive upper-bound terms, never a lower bound for the
   signed block.

7. **square_root_range_V_le_Mthreehalves — pass as a capacity test, not as a
   theorem.** The restored calculation is in §3.6. The square-root premise is
   unproved for the literal coefficient, so no positive-power subrange is
   claimed.

8. **absolute_capacity_vs_signed_sum — pass.** The incidence estimate (3.5),
   the ordinary-K-surrogate zero-mode capacity and Parseval diagonals, and
   (2.7) are explicitly upper capacities. None is used as a signed lower
   bound or attributed to an unmatched project theta multiplier.

9. **D_L_generic_tge2_cross_and_downstream_scope — pass.** The blind
   statement defines only the displayed literal block; it defines no
   completion variables \(D,d,L,t\). This report therefore makes no claim for
   any recovery fibre, additional row or layer, cross owner, M2 owner,
   endpoint assembly, M9, or the pointwise bridge.

All controls are analytic. No numerical experiment or numerical
certification was used.

# 6. Dependencies and exact artifacts used

- Campaign:
  m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate.
- Research round: 155.
- Task: blind_linearized_cross_fibre_feasibility.
- Role and access: blind rederiver, statement only.
- Graph SHA-256:
  84bbcb3413936c9b672c829cdba97b8d0bde69f7a6df677b61f24e9ec27e243a.
- Assigned generation time: 2026-08-25T03:46:45.073676+00:00.
- Status: candidate evidence only.
- protocol.md.
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/blind_statement.md.

No proof graph, proof draft, strategy file, Round-151--155 nonblind artifact,
sibling report, claimant derivation, web source, or computational artifact was
read or used. The cell partition, selected-only error, incidence bound, and
signed partial-sum seam were derived directly from the blind statement. The
finite selector is an auxiliary exact identity. The half-period transform is
an independently defined ordinary-K surrogate control, not a matched project
completion. This report is candidate evidence only and makes no shared-state
edit.

# 7. Recommended state effect

**Retain the direct literal obstruction; do not promote the target.** The
exact selected reindexing, selected-only residual-phase bound,
incidence/capacity ledger, and signed partial-sum seam are the independently
proved literal conclusions. Retain (2.4) only as an ordinary-K surrogate
invertibility control. It must not be used as a statement about the project
theta completion until an external review matches its kernel, multiplier,
coefficient, Fourier convention, zero mode, and normalization. The target and
every strict owner-complete positive-power subrange remain open until (3.3),
or an equally strong literal coefficient-sensitive signed estimate, is proved
with collisions, transitions, both branches, and endpoints intact.
