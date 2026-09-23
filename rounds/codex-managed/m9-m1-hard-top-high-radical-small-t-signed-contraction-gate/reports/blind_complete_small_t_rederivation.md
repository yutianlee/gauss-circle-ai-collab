# 1. Result.

The finite packet does not imply (B183.2).  More precisely, after granting the natural normalization \(\lVert a_{L,X}^{\sigma}\rVert _\infty\leq 1\) (which is not actually stated in the packet), the \(\ell^\infty\)-to-scalar norm allowed by the stated support is the exact site count

\[
 \mathcal K(L)=\sum_{1\leq t<T_L}\mathcal K_t(L),\qquad
 \mathcal K_t(L)=
 \sum_{\substack{s>L\\ \mu^2(s)=1}}d_L(st^2),
 \tag{1.1}
\]

where

\[
 d_L(r)=\#\left\{h\mid r:h\asymp L,\ r/h\ \mathrm{odd},\ 4h<r/h<16h\right\}.
 \tag{1.2}
\]

Thus \(\mathcal K_t(L)\ll L^2t^{-2}\mathcal X\), \(\mathcal K(L)\ll L^2\mathcal X\), and, for the ordinary nondegenerate dyadic meaning of \(h\asymp L\),

\[
 \mathcal K_1(L)\asymp L^2,
 \qquad \mathcal K(L)=L^{2+o(1)}.
 \tag{1.3}
\]

The complete \(t=1\) face therefore already has coefficient-insensitive capacity \(L^2\), a factor \(L^{1/2-o(1)}\) above the target.  A bounded complex-dechirped control attains (1.1), so no estimate of the strength (B183.2) can follow uniformly from support, boundedness, the displayed \(\chi _4\), and the displayed phase.  This is a mechanism no-go, not a lower bound for the fixed literal coefficient and not a refutation of (B183.2) for that coefficient.

The exact Möbius re-expansion is

\[
 S_{L,X}^{\sigma}
 =\sum_{b,u\geq1}\mathfrak m_L(b,u)
 C_{L,X}^{\sigma}(bu^2)e(\sigma u\sqrt{Xb}),
 \quad
 \mathfrak m_L(b,u)=
 \sum_{\substack{a\mid u\\a^2b>L\\u/a<T_L}}\mu(a).
 \tag{1.4}
\]

Both strict cutoffs in (1.4) are indispensable.  Cutting the Möbius divisor at \(a>A\) gives an absolutely target-safe tail only when \(A\gtrsim L^{1/2}\); the complementary core still contains the full \(a=1\) term and the squarefree \(t=1\) face.  Exact regrouping returns the original sum.  Hence the transform gives either a same-scale core or a literal self-return, not a smaller target core.

An exact fixed-row van der Corput connector is derived below.  It would prove

\[
 |S_t|\ll (L^2/t^2)^{3/4}\mathcal X
 =L^{3/2}t^{-3/2}\mathcal X
 \tag{1.5}
\]

from an averaged square-root shifted-correlation estimate for the exact literal coefficient.  Summing (1.5) proves (B183.2).  This connector is strictly stronger than (B183.2), because it controls every row before summing and does not permit cancellation between distinct \(t\)'s.  No hypothesis in the packet supplies its correlation estimate.

The narrowest exposed missing mechanism is therefore cancellation for the exact literal \(t=1\) row (or an explicit joint-\(t\) relation that cancels that row against the others).  At the shifted-correlation interface, the first missing relation is (3.25) below for \(t=1\).

# 2. Exact statement and hypotheses.

Let

\[
 \mathcal P_L=
 \{(h,n)\in\mathbb N^2:h\asymp L,\ n\ \mathrm{odd},\ 4h<n<16h\}.
 \tag{2.1}
\]

For \(r\geq1\), write \(r=s(r)t(r)^2\) uniquely with \(s(r)\) squarefree.  Define

\[
 \mathcal P_L^{<}=
 \{(h,n)\in\mathcal P_L:s(hn)>L,\ 1\leq t(hn)<T_L\},
 \tag{2.2}
\]

and let \(\mathcal P_{L,t}^{<}\) be its subset on which \(t(hn)=t\).  Then

\[
 \#\mathcal P_{L,t}^{<}=\mathcal K_t(L),\qquad
 \#\mathcal P_L^{<}=\mathcal K(L).
 \tag{2.3}
\]

The following conclusions use only the finite packet.

1. **Exact capacity.**  For the class of all arrays \(\alpha(h,n)\) supported on \(\mathcal P_L\) with \(|\alpha(h,n)|\leq B\), the supremum of the modulus of the left side of (B183.2), with \(a_{L,X}^{\sigma}\) replaced by \(\alpha\), is exactly \(B\mathcal K(L)\).  On one fixed row it is exactly \(B\mathcal K_t(L)\).

2. **Capacity scale.**  If \(h\asymp L\) denotes a fixed nondegenerate dyadic window (so it contains a subinterval of length \(\gg L\) and is contained in one of length \(O(L)\)), then (1.3) holds.  Without an exact definition of the symbol \(\asymp\), (1.1)--(1.2), rather than a numerical constant, is the exact capacity determined by the packet.

3. **Möbius kernel.**  Formula (1.4) is an identity for the fixed literal coefficient, with no positivity and no discarded endpoint.  Equivalently, with

\[
 q_L(b,u)=\max\!\left(\sqrt{L/b},\frac{u}{T_L}\right),
 \tag{2.4}
\]

one has

\[
 \mathfrak m_L(b,u)=\sum_{\substack{a\mid u\\a>q_L(b,u)}}\mu(a)
 =\mathbf 1_{u=1}-\sum_{\substack{a\mid u\\a\leq q_L(b,u)}}\mu(a).
 \tag{2.5}
\]

The condition \(u/a<T_L\) may also be written exactly as \(u/a\leq T_L-1\), or \(u\leq a(T_L-1)\).

4. **Row connector.**  For each \(1\leq t<T_L\), let \(J_t\) be an integer interval of length \(N_t\) containing every \(s\) for which \(s>L\) and \(C(st^2)\ne0\), and extend the row by zero off its true support.  Literal support permits \(N_t\ll L^2/t^2\).  Put

\[
 A_t(s)=\mathbf 1_{s>L}\mu^2(s)C(st^2),\qquad
 z_t(s)=A_t(s)e(\sigma t\sqrt{Xs}),
 \tag{2.6}
\]

\[
 D_t=\sum_{s\in J_t}|A_t(s)|^2,
 \tag{2.7}
\]

and, for \(1\leq q<N_t\),

\[
 R_t(q)=
 \sum_{\substack{s,s+q\in J_t}}
 A_t(s+q)\overline{A_t(s)}
 e\!\left(\sigma t\sqrt X(\sqrt{s+q}-\sqrt s)\right).
 \tag{2.8}
\]

Let \(H_t=\max(1,\lfloor N_t^{1/2}\rfloor)\).  The sufficient shifted-correlation hypothesis is

\[
 D_t+2\sum_{q=1}^{H_t-1}
 \left(1-\frac q{H_t}\right)|R_t(q)|
 \ll N_t\mathcal X
 \quad(1\leq t<T_L).
 \tag{2.9}
\]

Under (2.9), (1.5) and hence (B183.2) follow.  An easy-to-state stronger sufficient version of (2.9) is

\[
 D_t\ll N_t\mathcal X,
 \qquad |R_t(q)|\ll N_t^{1/2}\mathcal X
 \quad(1\leq q<H_t).
 \tag{2.10}
\]

As usual, fixed powers of the allowed subpolynomial loss are absorbed back into \(\mathcal X\).

# 3. Proof or derivation.

**Flattening and capacity.**  Expanding (B183.1) inside (B183.2) and using \(hn=st^2\) gives the exact identity

\[
 \begin{aligned}
 S_{L,X}^{\sigma}
 &=\sum_{\substack{s>L,\ \mu^2(s)=1\\1\leq t<T_L}}
 \sum_{\substack{h\mid st^2,\ h\asymp L\\
 st^2/h\ {\rm odd},\ 4h<st^2/h<16h}}
 \chi_4(st^2/h)a(h,st^2/h)e(\sigma t\sqrt{Xs})\\
 &=\sum_{(h,n)\in\mathcal P_L^{<}}
 \chi_4(n)a(h,n)e(\sigma\sqrt{Xhn}).
 \end{aligned}
 \tag{3.1}
\]

The last phase equality is exact because \(t\sqrt s=\sqrt{st^2}=\sqrt{hn}\), with positive square roots.  Triangle inequality in (3.1) gives \(|S|\leq B\mathcal K(L)\) when \(|a|\leq B\).  Conversely, on \(\mathcal P_L^{<}\) choose the control array

\[
 \alpha(h,n)=B\chi_4(n)e(-\sigma\sqrt{Xhn}),
 \tag{3.2}
\]

and put it equal to zero elsewhere.  Since \(n\) is odd, \(\chi_4(n)^2=1\), and every site in (3.1) contributes \(B\).  This proves the exact operator norm.  Restricting (3.2) to \(\mathcal P_{L,t}^{<}\) proves the fixed-row assertion.

Literal support gives \(hn\asymp L^2\).  For fixed \(t\), the possible \(s=hn/t^2\) lie in an interval of length \(O(L^2/t^2)\), while (1.2) is at most \(\tau(st^2)\).  The divisor bound, absorbed into \(\mathcal X\), therefore gives

\[
 \mathcal K_t(L)\ll \frac{L^2}{t^2}\mathcal X,
 \qquad
 \mathcal K(L)\ll L^2\mathcal X.
 \tag{3.3}
\]

For \(t=1\),

\[
 \mathcal K_1(L)=
 \#\{(h,n)\in\mathcal P_L:hn>L,\ \mu^2(hn)=1\}.
 \tag{3.4}
\]

In any positive-area dyadic subregion of (2.1), squarefree and coprimality sieving gives a positive proportion of such pairs.  To see positivity directly, at every odd prime \(p\) the local density of \(v_p(h)+v_p(n)\leq1\) is

\[
 (1-p^{-1})^2+2(p^{-1}-p^{-2})(1-p^{-1})
 =1-3p^{-2}+2p^{-3},
 \tag{3.5}
\]

and at \(p=2\), after imposing \(n\) odd, it is \((1/2)(3/4)=3/8\).  Hence the product

\[
 \frac38\prod_{p\ \mathrm{odd}}(1-3p^{-2}+2p^{-3})
 \tag{3.6}
\]

is positive.  Truncating the square-divisor sieve and then sending the truncation to infinity proves \(\mathcal K_1(L)\gg L^2\); the reverse bound is immediate.  For any fixed integer \(t\), the subfamily \(h=t^2h'\), with \(h'n\) squarefree and coprime to \(t\), similarly has order \(L^2/t^2\).  The uniform upper envelope (3.3), and especially the \(t=1\) lower bound, are all that the no-go needs.

**Exact Möbius kernel.**  Starting before any absolute value,

\[
 \begin{aligned}
 S
 &=\sum_{\substack{s>L\\1\leq t<T_L}}
 \left(\sum_{a^2\mid s}\mu(a)\right)
 C(st^2)e(\sigma t\sqrt{Xs})\\
 &=\sum_{\substack{a,b,t\geq1\\a^2b>L\\t<T_L}}
 \mu(a)C\bigl(b(at)^2\bigr)e(\sigma at\sqrt{Xb}).
 \end{aligned}
 \tag{3.7}
\]

Put \(u=at\).  Then \(a\mid u\), and the two original strict inequalities become

\[
 a^2b>L,
 \qquad \frac ua<T_L.
 \tag{3.8}
\]

This gives (1.4).  Conditions (3.8) are equivalent to \(a>q_L(b,u)\), proving the first equality in (2.5).  The second follows from

\[
 \sum_{a\mid u}\mu(a)=\mathbf1_{u=1}.
 \tag{3.9}
\]

Dropping either member of (3.8) changes the kernel: the omitted divisors are not an endpoint-null set.  Notice also that the phase in (1.4) remains

\[
 e(\sigma u\sqrt{Xb})=e(\sigma\sqrt{Xbu^2});
 \tag{3.10}
\]

the new divisor variable creates no phase oscillation among representations of the same integer.

For a truncation parameter \(A\geq1\), let the part of (3.7) with \(a>A\) be \(M_{>A}\).  If \(|a_{L,X}^{\sigma}(h,n)|\leq B\), then \(|C(r)|\leq B\tau(r)\ll B\mathcal X\).  For fixed \(a,t\), support \(ba^2t^2\asymp L^2\) leaves \(O(1+L^2/(a^2t^2))\) possible \(b\)'s and forces \(at\ll L\).  The summed contribution of the `1` is \(O(L\log(2+L/A))\), which is \(O(L^2/A)\) for \(1\leq A\ll L\); for larger \(A\) the sum is empty.  Therefore

\[
 |M_{>A}|
 \ll B\mathcal X L^2
 \sum_{a>A}a^{-2}\sum_{t\geq1}t^{-2}
 \ll \frac{B L^2}{A}\mathcal X.
 \tag{3.11}
\]

Thus \(A\asymp L^{1/2}\) is the first absolute target-scale cut.  But the part \(a\leq A\) contains in full the \(a=1\) expression

\[
 \sum_{\substack{b>L\\u<T_L}}C(bu^2)e(\sigma u\sqrt{Xb}),
 \tag{3.12}
\]

whose ambient capacity is still \(L^{2+o(1)}\).  Nonsquarefree terms in (3.12) may cancel against \(a>1\) representations, but if \(r\) is squarefree then its only representation \(r=bu^2\) has \(u=1,b=r\).  Consequently the entire squarefree \(t=1\) face occurs only in the \(a=1\) core.  If instead all representations are regrouped exactly by \(r\), (3.9) reconstructs \(\mu^2(s)\) and returns (B183.2).  This proves the asserted truncation dichotomy.

**Fixed-row shifted-correlation connector.**  Let

\[
 S_t=\sum_{s\in J_t}z_t(s).
 \tag{3.13}
\]

For any integer \(1\leq H\leq N_t\), zero-extension and Cauchy--Schwarz give the exact van der Corput inequality

\[
 |S_t|^2\leq
 \frac{N_t+H-1}{H}
 \left\{
 D_t+2\sum_{q=1}^{H-1}
 \left(1-\frac qH\right)\Re R_t(q)
 \right\}.
 \tag{3.14}
\]

Indeed, write \(HS_t\) as the sum, over \(N_t+H-1\) translates, of the \(H\)-term moving sums; expanding their squared moduli gives \(HD_t+2\sum_{q=1}^{H-1}(H-q)\Re R_t(q)\).  Replacing real parts by moduli yields the sufficient form (2.9).

The correlation in (2.8) has the exact phase difference

\[
 \sigma t\sqrt X(\sqrt{s+q}-\sqrt s),
 \tag{3.15}
\]

with no linearization.  Its coefficient is exactly

\[
 \begin{aligned}
 &\mathbf1_{s>L}\mathbf1_{s+q>L}\mu^2(s)\mu^2(s+q)
 C((s+q)t^2)\overline{C(st^2)}\\
 &=\mathbf1_{s>L}\mathbf1_{s+q>L}\mu^2(s)\mu^2(s+q)
 \sum_{\substack{h_+\mid(s+q)t^2\\h_+\asymp L\\n_+=(s+q)t^2/h_+\ \mathrm{odd}\\4h_+<n_+<16h_+}}
 \sum_{\substack{h_-\mid st^2\\h_-\asymp L\\n_-=st^2/h_-\ \mathrm{odd}\\4h_-<n_-<16h_-}}
 \chi_4(n_+)\chi_4(n_-)
 a(h_+,n_+)\overline{a(h_-,n_-)}.
 \end{aligned}
 \tag{3.16}
\]

This displays the diagonal, both shifted divisor fibres, the character, and the fixed literal coefficient before positivity.

Take \(H=H_t\asymp N_t^{1/2}\).  Under (2.9), (3.14) gives

\[
 |S_t|^2\ll N_t^{1/2}\cdot N_t\mathcal X
 =N_t^{3/2}\mathcal X,
 \qquad
 |S_t|\ll N_t^{3/4}\mathcal X.
 \tag{3.17}
\]

Restoring the support powers \(N_t\ll L^2/t^2\) yields

\[
 H_t\ll L/t,
 \quad D_t+2\sum_{q<H_t}(1-q/H_t)|R_t(q)|\ll L^2t^{-2}\mathcal X,
 \tag{3.18}
\]

\[
 |S_t|^2\ll L^3t^{-3}\mathcal X,
 \qquad |S_t|\ll L^{3/2}t^{-3/2}\mathcal X.
 \tag{3.19}
\]

Finally,

\[
 \left|\sum_{t<T_L}S_t\right|
 \leq\sum_{t<T_L}|S_t|
 \ll L^{3/2}\mathcal X\sum_{t\geq1}t^{-3/2}
 \ll L^{3/2}\mathcal X.
 \tag{3.20}
\]

This proves the connector and also shows why it is stronger than the desired total-sum estimate.

**Joint-\(t\), orientation, character, and Mellin checks.**  There is one useful exact character factorization.  For a positive integer \(m\), write \(m_{\rm o}=m/2^{v_2(m)}\).  If \(h\mid st^2\) and \(n=st^2/h\) is odd, then \(v_2(h)=v_2(st^2)\), so

\[
 n=\frac{s_{\rm o}t_{\rm o}^2}{h_{\rm o}},
 \qquad
 \chi_4(n)=\chi_4(s_{\rm o})\chi_4(h_{\rm o}),
 \tag{3.21}
\]

because \(\chi_4(t_{\rm o}^2)=1\) and an odd \(\chi_4\)-value is its own inverse.  Hence, without taking absolute values,

\[
 C(st^2)=\chi_4(s_{\rm o})A_s(t),
 \quad
 A_s(t)=
 \sum_{\substack{h\mid st^2,\ h\asymp L\\st^2/h\ \mathrm{odd},\ 4h<st^2/h<16h}}
 \chi_4(h_{\rm o})a(h,st^2/h),
 \tag{3.22}
\]

and

\[
 S=\sum_{s>L}\mu^2(s)\chi_4(s_{\rm o})
 \sum_{t<T_L}A_s(t)e(\sigma t\sqrt{Xs}).
 \tag{3.23}
\]

This is a genuine joint-\(t\) identity retaining the coefficient.  It also shows that \(\chi_4\) itself supplies no oscillation in \(t\): all remaining \(t\)-dependence is in the literal \(A_s(t)\) and the linear phase.  The divisor orientation has no internal swap symmetry, since \(4h<n<16h\) is sent by \((h,n)\mapsto(n,h)\) to a disjoint ratio range.  In the Möbius coordinates, (3.10) likewise gives no oscillation among square-divisor representations.

A formal two-variable Mellin transform can package the same data, for example through the finite polynomial

\[
 \mathscr D(z,w)=
 \sum_{(h,n)\in\mathcal P_L^{<}}
 \chi_4(n)a(h,n)(hn)^{-z}(n/h)^{-w}.
 \tag{3.24}
\]

Mellin inversion of a specified product cutoff and ratio profile would express (3.1) as an integral of such polynomials.  But the packet gives neither the formula for that profile nor a functional equation, spectral identity, off-central bound, or relation between \(\mathscr D(z,w)\) and a dual polynomial.  Since the finite transform is invertible, it cannot by itself improve the capacity, and the dechirped control remains dechirped after repackaging.  Thus (3.21)--(3.24) are the only coefficient-preserving structural relations available from the packet; none proves a saving.

At the row-differencing interface, the first substantive relation still needed is, already for \(t=1\),

\[
 D_1+2\sum_{1\leq q<H_1}
 \left(1-\frac q{H_1}\right)|R_1(q)|
 \ll L^2\mathcal X,
 \qquad H_1\asymp L,
 \tag{3.25}
\]

with \(R_1(q)\) containing the literal coefficient (3.16).  Alternatively, a genuinely joint-\(t\) theorem would have to state an explicit signed relation showing how the capacity-size \(t=1\) row cancels against the remaining rows.  No such relation follows from (3.21)--(3.23).

# 4. First doubtful or unproved step.

The first unproved step toward (B183.2) is not a delicate estimate inside the derivation: it is the absence of any quantitative cancellation relation for the fixed literal coefficient.  In particular, (3.25) is not proved.  Neither support nor \(\chi_4\) bounds its off-diagonal correlations after the coefficient is retained.

The packet also omits the formula and even an explicit uniform magnitude bound for \(a_{L,X}^{\sigma}(h,n)\), and it does not define the exact dyadic predicate denoted by \(h\asymp L\).  Consequently one cannot audit the advertised taper, floors, stars, half weights, strict coefficient edges, real-parameter crossings, or endpoint point values, and one cannot assign an exact numerical leading constant to (1.1).  All exact identities above are independent of those omissions.  The capacity-scale no-go grants the favorable bound \(|a|\leq1\); it therefore does not rely on the missing magnitude hypothesis.

The statement that \(\mathcal K_1(L)\asymp L^2\) uses the standard nondegenerate dyadic interpretation explicitly stated in Section 2.  If the literal cutoff were allowed to be sparse or identically zero, only the exact formula (1.1) would remain, which further confirms that the fixed formula is essential for a proof about the literal family.

# 5. Required control test and outcome.

1. **Unsigned capacity control — fails at target scale.**  Replacing every summand in (3.1) by its modulus gives exactly \(\sum_{\mathcal P_L^{<}}|a(h,n)|\).  For unit site weights its capacity is \(\mathcal K(L)=L^{2+o(1)}\), and its \(t=1\) capacity is \(\asymp L^2\).  Thus positivity cannot be introduced before a fixed-coefficient cancellation relation.

2. **Complex-dechirped control — refutes the arbitrary-sequence analogue.**  The bounded array (3.2) makes every selected site positive, for either sign \(\sigma\) and every \(X>0\).  It yields \(S=B\mathcal K(L)\), or \(B\mathcal K_t(L)\) when restricted to one row.  Outcome: support and boundedness alone do not imply (B183.2).  This is not asserted to be the literal coefficient and supplies no literal lower mass.

3. **Character-erased control — \(\chi_4\) alone is insufficient.**  Taking \(\alpha(h,n)=\chi_4(n)\beta(h,n)\) removes the displayed character exactly because \(n\) is odd.  Relation (3.21) also shows that the rowwise \(t\)-square contributes no new \(\chi_4\)-oscillation.  Outcome: any character saving must use a proved incompatibility between the literal \(a\) and this absorption; none is stated.

4. **One-site control — passes normalization but gives no mass claim.**  A single admissible site contributes exactly one bounded term after dechirping.  It checks the phase identity and strict support predicates, but is far below the target and cannot support a lower bound for the literal family.

5. **One-fibre control — multiplicity is only subpolynomial.**  On one fixed \(r=st^2\), all admissible divisor orientations can be aligned, producing exactly \(d_L(r)\leq\tau(r)\ll\mathcal X\).  Outcome: no single fibre violates the target; the obstruction is the \(\asymp L^2\) collection of possible sites, especially the \(t=1\) face.

6. **Square-centre control — exact squares are outside this sector.**  If \(r=m^2\), its canonical squarefree part is \(s(r)=1\leq L\), so it belongs to the already-paid complementary sector, not (B183.2).  A square-centred adversarial example therefore cannot be cited as literal lower mass here.  Square multiples \(r=st^2\) with squarefree \(s>L\) are already represented exactly, and the complete \(t=1\) face remains the valid capacity control.

7. **Endpoint controls — all strict endpoints are preserved, and phase-only uniformity fails.**  The values \(n=4h\) and \(n=16h\) are excluded; \(s=L\) is excluded; \(t=T_L\) is excluded; and the integer range is exactly \(1\leq t\leq T_L-1\), so \(t=1\) is included.  In the Möbius kernel this is the exact inequality \(u/a\leq T_L-1\).  Moreover, on \(r\asymp L^2\) the total variation of \(\sqrt{Xr}\) is \(O(L\sqrt X)\).  For \(X\ll L^{-2}\), the displayed phase is nearly constant across the whole support.  Outcome: a theorem uniform for all \(X>0\) cannot rely only on phase oscillation; it needs literal coefficient cancellation at the small-\(X\) endpoint.  Since the coefficient itself depends on \(X\), this observation is again diagnostic, not a lower bound for it.

No numerical computation was used; all controls are exact algebraic or counting controls.

# 6. Dependencies and exact artifacts used.

Only the following two permitted artifacts were read or used:

1. `protocol.md`.
2. `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/blind_statement.md`.

No proof graph, campaign state, strategy, prior round, durable kernel, source, sibling report, review, control artifact, candidate, synthesis, conductor analysis, or repository summary was read.

# 7. Recommended state effect.

**Retain.**  Retain (B183.2) as open and retain this report as a narrow mechanism no-go: support, boundedness, the visible character, exact Möbius inversion, divisor orientation, and formal Mellin repackaging do not close the target.  Do not promote a literal lower bound or reject the fixed theorem on the basis of the adversarial controls.  The next admissible proof input must expose the exact coefficient formula and prove either the literal shifted-correlation relation (3.25), extended over all rows as (2.9), or a comparably explicit joint-\(t\) signed relation that controls cancellation of the full \(t=1\) face against its complement.
