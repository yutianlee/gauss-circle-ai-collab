---
campaign: m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate
round: 154
task_id: round154-blind-quadratic-root-wave-feasibility
role: statement-only blind rederiver
claim_status: blind
generated_at: 2026-08-25T10:30:44.3912035+08:00
graph_hash: not supplied in the statement-only packet and not inspected
context_files:
  - protocol.md
  - rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/blind_statement.md
---

## 1. Result

The nearest-root change of variables is exact and has a useful, but limited,
owner-complete consequence.  Put

\[
 H=\lfloor J\rfloor+1=\lfloor M^{3/4}\rfloor+1,
 \qquad \eta(k,j)=\sqrt{k^2-j}-k.
\]

Then the summands in (154.B1) are in bijection with the pairs \((k,j)\)
for which

\[
 -k\leq j\leq k-1,\qquad k^2-j=Nn,\qquad n>0\text{ odd},
 \qquad |j|\geq H,
\]

and the exact root phase is

\[
 e(\sqrt{Nn})=e(\eta(k,j)),\qquad
 \eta(k,j)=-\frac{j}{k+\sqrt{k^2-j}},\qquad
 j=-2k\eta-\eta^2.
\tag{154.R1}
\]

For every fixed constant \(C_0\), the shell

\[
 J<|j|\leq C_0J
\tag{154.R2}
\]

is target-safe by an unsigned capacity estimate alone.  In particular, the
first genuinely large-defect dyadic shell \(H\leq |j|<2H\) contributes
\(O_\varepsilon(X^\varepsilon)\), uniformly in the parity and factorization
of \(N\), in literal support endpoints, and in the two signs of \(j\).

I do **not** obtain (154.B3) for all \(|j|>J\).  I obtain instead the
following precise feasibility obstruction.  Fourier encoding of the quotient
character modulo \(4N\) is lawful, and incomplete quadratic Gauss sums can be
evaluated with all gcd losses retained.  But completing in \(k\) and then
using an absolute value or Cauchy in the Fourier variable either (a) returns
the raw root capacity, or (b) introduces a dense diagonal of size

\[
 K^{1/2}M^{-3/4}\asymp N^{1/4}M^{-1/2},
 \qquad K\asymp\sqrt{NM}.
\tag{154.R3}
\]

Under \(M^{449}\ll R^{780}\) this is at least a fixed power
\(R^{59/449}\), up to constants and \(X^\varepsilon\).  A simultaneous
\((k,j)\) completion does not remove it: after quotient Fourier expansion
the continuous phase is a function only of \(t=k^2-j\), and its Hessian is
singular on the relevant stationary set.  Thus independent quadratic savings
in the root and defect variables would be double-counting the same
oscillation.  The full target requires a new mask-preserving **signed outer
root-wave estimate**; Gauss evaluation, Poisson, root spacing, and the usual
Cauchy/dispersion placements do not supply it from the stated hypotheses.
This is a no-go result for that completion architecture, not a counterexample
to (154.B3).

## 2. Exact statement and hypotheses

Write \(e(z)=e^{2\pi iz}\).  Let the fixed dilation containing the support of
\(A\) be \([cM,CM]\), with fixed \(0<c<C\).  The argument uses only

\[
 \|A\|_\infty+\sum_n|A(n+1)-A(n)|\ll_\varepsilon X^\varepsilon,
\]

the stated \(O_\varepsilon(X^\varepsilon)\) number of literal support
components, \(1\ll M\leq R^2\), and \(N=\lfloor X\rfloor\asymp R^4\).
All endpoint inequalities below are inclusive or strict exactly as displayed;
no endpoint is smoothed away.

For a literal integer support component \([a,b]\), define

\[
 \mathcal D_{a,b}^{\pm}=
 \left\{(k,j):
 \begin{array}{l}
 k\geq1,\quad -k\leq j\leq k-1,\\
 k^2-Nb\leq j\leq k^2-Na,\\
 N\mid k^2-j,\quad (k^2-j)/N\text{ odd},\\
 j\geq H\quad(+)\quad\text{or}\quad j\leq-H\quad(-)
 \end{array}\right\}.
\tag{154.R4}
\]

With \(n(k,j)=(k^2-j)/N\), the exact reparametrized sum is

\[
 Q=\sum_{(k,j)\in\mathcal D^+\cup\mathcal D^-}
 \chi_4(n(k,j))n(k,j)^{-3/4}A(n(k,j))e(\eta(k,j)),
\tag{154.R5}
\]

where \(\mathcal D^\pm\) uses the actual support of the zero-extended profile,
so overlapping descriptions of support components do not duplicate a
summand.  The positive and negative branches are kept separate.  No lower
bound for either branch is asserted from an upper capacity.

The no-go conclusion is deliberately scoped: it rules out a proof which uses
only quotient Fourier expansion, separate incomplete Gauss/Poisson estimates,
root-spacing counts, and an absolute or Cauchy treatment of the remaining
outer sum.  It does not rule out a new correlation theorem which preserves
the \(\chi_4\) signs and both large-defect masks.  The external
\(O_\varepsilon(X^\varepsilon)\) coefficient is not inserted into \(Q\) and
is not used as a source of averaging.

## 3. Proof or derivation

**Exact cell, inverse map, and endpoints.**  If \(y=\sqrt{Nn}\), then
\(k=\lfloor y+1/2\rfloor\) is equivalent to

\[
 k-\tfrac12\leq y<k+\tfrac12.
\]

Since \(Nn\) is integral while the two squared endpoints have fractional
part \(1/4\), this is equivalent to

\[
 k^2-k+1\leq Nn\leq k^2+k,
\]

and hence exactly to \(-k\leq j=k^2-Nn\leq k-1\).  Conversely these integer
inequalities recover the nearest integer \(k\), so there is no half-integer
tie.  The map \(n\mapsto(k,j)\) and the inverse \((k,j)\mapsto(k^2-j)/N\)
are therefore a bijection on (154.R4).  In particular, the negative cell
contains \(j=-k\), whereas the positive cell stops at \(j=k-1\).  Thus
\(j\geq H\) requires \(k\geq H+1\), while \(j\leq-H\) requires only
\(k\geq H\).

For a component \([a,b]\), the fixed-\(k\) defect interval is exactly

\[
 [\max(-k,k^2-Nb),\ \min(k-1,k^2-Na)]\cap\mathbb Z.
\tag{154.R6}
\]

For fixed \(j\), its \(k\)-projection is the integer-square interval

\[
 Na+j\leq k^2\leq Nb+j
\tag{154.R7}
\]

intersected with \(k\geq\max(1,-j,j+1)\), with the irrelevant one of
\(-j,j+1\) omitted according to the sign.  Formulae (154.R6)--(154.R7)
retain a point at \(a\), \(b\), \(-k\), or \(k-1\) exactly when its displayed
weak inequality holds.

On the fixed dilation, all roots satisfy \(k\asymp K=\sqrt{NM}\).  More
precisely, a component has projected endpoints
\(\lfloor\sqrt{Na}+1/2\rfloor\) and
\(\lfloor\sqrt{Nb}+1/2\rfloor\).  Since \(M\leq R^2\) and \(N\asymp R^4\),
the largest relevant \(k\) is less than \(N/2\) for all sufficiently large
\(X\).  A single cell has integral \(Nn\)-width \(2k-1<N\), so at most one
\(n\) occurs for a fixed \(k\).  This proves injectivity of \(n\mapsto k\)
in the asymptotic range.  The pair map was bijective without this last size
observation.

Finally, \(\eta=\sqrt{k^2-j}-k\) lies strictly between \(-1/2\) and \(1/2\),
and (154.R1) follows by rationalizing.  Uniformly in the cell,

\[
 \eta(k,j)=-\frac{j}{2k}-\frac{j^2}{8k^3}
 +O\!\left(\frac{|j|^3}{k^5}\right).
\tag{154.R8}
\]

No approximation is needed in (154.R5); (154.R8) is only a scale check.

**Quotient parity and character, including every two-adic case.**  For an
integer \(t\), set

\[
 F_N(t)={\bf1}_{N\mid t}\,\chi_4(t/N),
\]

with \(\chi_4\) zero on even integers.  Then, without inverting \(N\),

\[
 F_N(k^2-j)=
 {\bf1}_{k^2-j\equiv N\ (4N)}
 -{\bf1}_{k^2-j\equiv3N\ (4N)}.
\tag{154.R9}
\]

Thus (154.R9) simultaneously imposes divisibility by \(N\), oddness of the
quotient, and its character.  If \(N=2^aN_0\) with \(N_0\) odd, nonvanishing
is equivalently

\[
 N\mid k^2-j,\qquad v_2(k^2-j)=a,
\]

or, at the two-adic seam,
\(j\equiv k^2-2^a\pmod {2^{a+1}}\).  Moreover

\[
 \chi_4((k^2-j)/N)
 =\chi_4(N_0)\chi_4((k^2-j)/2^a),
\tag{154.R10}
\]

where the last odd residue is read modulo \(4\), equivalently modulo
\(2^{a+2}\) before division.  This covers \(a=0\), powers of two, and mixed
even \(N\); no primitive-character hypothesis has been inserted.

The exact modulo-\(4N\) Fourier formula is

\[
 F_N(t)=-\frac{i}{2N}
 \sum_{\substack{h\bmod 4N\\h\ \mathrm{odd}}}
 \chi_4(h)e\!\left(\frac{ht}{4N}\right).
\tag{154.R11}
\]

Indeed, the Fourier coefficient at \(h\) is

\[
 \sum_{r\bmod4}\chi_4(r)e(-hr/4)
 =\begin{cases}-2i\chi_4(h),&h\text{ odd},\\0,&h\text{ even}.
 \end{cases}
\]

Formula (154.R11) is valid even when \((h,N)>1\).

There is an important signed control when \(N\) is odd.  On an admitted fixed
\(j\) fiber,

\[
 \chi_4(n)=\chi_4(N)\chi_4(k^2-j)
 =\begin{cases}
 \chi_4(N)\chi_4(1-j),&j\text{ even }(k\text{ odd}),\\
 \chi_4(N)\chi_4(-j),&j\text{ odd }(k\text{ even}).
 \end{cases}
\tag{154.R12}
\]

The character is therefore constant in \(k\) on every fixed defect fiber
when \(N\) is odd.  Its possible saving lives in the **outer \(j\)-ordering**,
not inside an individual root sum.  Any argument that takes absolute values
over \(j\) has discarded the only stated feature distinguishing this case
from its unsigned analogue.

**Raw and weighted capacities, including imprimitive roots.**  Let
\(\rho_N(j)\) be the number of roots of \(x^2\equiv j\pmod N\).  For an odd
prime power \(p^\nu\), with \(b=v_p(j)<\nu\), the exact local count is zero
if \(b\) is odd and is \(2p^{b/2}\) if \(b\) is even and the resulting unit
is a quadratic residue modulo \(p^{\nu-b}\).  If \(p^\nu\mid j\), the count
is \(p^{\lfloor\nu/2\rfloor}\).  For \(2^\nu\), if
\(b=2c<\nu\), put \(m=\nu-2c\).  The count is respectively
\(2^c,2^{c+1},2^{c+2}\) for \(m=1,m=2,m\geq3\), subject respectively to
the unit conditions modulo \(2\), \(4\), and \(8\); it is zero otherwise.
For \(2^\nu\mid j\) the count is \(2^{\lfloor\nu/2\rfloor}\).  Chinese
remaindering therefore gives, for \(j\ne0\),

\[
 \rho_N(j)\ll 2^{\omega(N)+2}\sqrt{(j,N)}
 \ll_\varepsilon X^\varepsilon\sqrt{(j,N)}.
\tag{154.R13}
\]

The interval of relevant \(k\)'s has length less than \(N\), so each residue
root occurs at most once.  For either signed dyadic defect interval of length
\(O(D)\), \(D\geq1\), (154.R13) and

\[
 \sqrt{(j,N)}\leq\sum_{d\mid(j,N)}\sqrt d
\]

give

\[
 \mathcal C_D:=\#\{(k,j)\text{ admissible}:D\leq |j|<2D\}
 \ll_\varepsilon X^\varepsilon\min(M,D).
\tag{154.R14}
\]

For example, summing the right side before the minimum gives

\[
 \sum_{D\leq |j|<2D}\sqrt{(j,N)}
 \leq\sum_{\substack{d\mid N\\d\leq2D}}
 \sqrt d\,(O(D/d)+1)
 \ll_\varepsilon X^\varepsilon D.
\]

The zero defect is not estimated by the wasteful \(\sqrt N\) bound.  Writing
\(N=d s^2\) with \(d\) squarefree, \(Nn\) is a square exactly when
\(n=d u^2\), so its support capacity is \(O(\sqrt M+1)\).  Consequently

\[
 \#\{|j|\leq J\}\ll_\varepsilon X^\varepsilon(J+\sqrt M),
\quad
 \sum_{|j|\leq J}|n^{-3/4}A(n)|\ll_\varepsilon X^\varepsilon.
\tag{154.R15}
\]

This reproves only the scalar small-defect safety stated in the packet.

The total raw capacity is \(O(M)\) by injectivity.  On a dyadic block the
weighted capacities are

\[
 \sum |n^{-3/4}A(n)|
 \ll_\varepsilon X^\varepsilon M^{-3/4}\min(M,D),
\tag{154.R16}
\]

\[
 \sum |n^{-3/4}A(n)|^2
 \ll_\varepsilon X^\varepsilon M^{-3/2}\min(M,D),
\qquad
 \sum_{\mathrm{all}}|n^{-3/4}A(n)|^2
 \ll_\varepsilon X^\varepsilon M^{-1/2}.
\tag{154.R17}
\]

Taking \(D=H\asymp M^{3/4}\) in (154.R16) proves the owner-complete shell
(154.R2).  These are upper capacities only; they imply neither that a branch
is populated nor that a signed sum has comparable size.

**Phase and dyadic-defect test.**  In a block \(|j|\asymp D\leq K\),

\[
 \frac{\partial\eta}{\partial j}=-\frac1{2\sqrt{k^2-j}},
 \qquad
 \frac{\partial\eta}{\partial k}=\frac{k}{\sqrt{k^2-j}}-1.
\tag{154.R18}
\]

Thus the total root-phase variation across either a \(j\)-interval of length
\(D\) or a \(k\)-interval of length \(K\) is only \(O(D/K)\).  It is
\(o(1)\) near the cutoff and at most constant even at the cell edge.  There
is no analytic oscillation of power size inside a fixed root fiber.  The two
signs have opposite \(\eta\), so cancellation between them cannot be assumed.

Use the literal dyadic intervals \(H2^r\leq j<2H2^r\) and
\(-2H2^r<j\leq-H2^r\), truncated by (154.R6).  There are only
\(O(\log X)\) such intervals, but the logarithm can be absorbed only after a
uniform estimate for every block; it cannot repair a power loss that grows
with \(D\).

**Incomplete quadratic completion and exact Gauss losses.**  Let
\(\mathfrak q=4N\) and

\[
 G(h,b;\mathfrak q)=\sum_{x\bmod\mathfrak q}
 e((hx^2+bx)/\mathfrak q).
\]

For odd \(h\), put \(d=(h,\mathfrak q)\), which is odd.  Then
\(G=0\) unless \(d\mid b\).  If \(d\mid b\), reduction gives

\[
 G(h,b;\mathfrak q)=dG(h/d,b/d;\mathfrak q/d).
\]

The primitive sum on the right is zero unless \(b/d\) is even.  Writing
\(a=h/d\), \(Q_0=\mathfrak q/d\), and \(b/d=2r\), completing the square gives

\[
 G(a,2r;Q_0)=e(-\bar a r^2/Q_0)G(a,0;Q_0),
\]

and squaring the primitive Gauss sum gives

\[
 G(a,0;Q_0)=(1+i)\epsilon_a^{-1}
 \left(\frac{Q_0}{a}\right)\sqrt{Q_0},
 \qquad
 |G(h,b;\mathfrak q)|=\sqrt{2\mathfrak q d}.
\tag{154.R19}
\]

Here \(\epsilon_a=1\) for \(a\equiv1\pmod4\), \(\epsilon_a=i\) for
\(a\equiv3\pmod4\), and the symbol is the Jacobi/Kronecker symbol.  Hence an
incomplete interval sum with bounded-variation amplitude has the standard
bound

\[
 \sum_{k\in I}B(k)e(hk^2/\mathfrak q)
 \ll \|B\|_{BV}\min\bigl(|I|,\sqrt{Nd}\log(2N)\bigr).
\tag{154.R20}
\]

The factor \(d^{1/2}\) is mandatory for every odd-prime imprimitive case.

For fixed \(j\), a piecewise-constant interpolation of
\(n^{-3/4}A(n)\) composed with \((k^2-j)/N\), and multiplied by
\(e(\eta(k,j))\), has BV norm
\(O_\varepsilon(X^\varepsilon M^{-3/4})\); monotonicity and (154.R18)
control it, and every component endpoint contributes its literal boundary
term.  Therefore (154.R11) and (154.R20) are lawfully applicable.  Taking
absolute values in \(h\), however, gives only

\[
 |S_j|\ll_\varepsilon X^\varepsilon M^{-3/4}\sqrt N,
\tag{154.R21}
\]

because the mean of \(\sqrt{(h,N)}\) over odd \(h\bmod4N\) is
\(O_\varepsilon(X^\varepsilon)\).  At the largest permitted \(M\), the
right side of (154.R21) still contains \(R^{313/449}\), even before the
outer \(j\)-sum.

Cauchy in \(h\) exposes the complementary obstruction.  A smooth
interpolation is dense on a \(k\)-interval of length \(\asymp K\).  For the
permitted control case in which \(N\) is an odd prime and \(k<N/2\), odd-\(h\)
orthogonality is exactly diagonal: for distinct positive \(k,l<N/2\),
\(N\nmid(k-l)(k+l)\), and

\[
 \sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}
 e\!\left(\frac{h(k^2-l^2)}{4N}\right)=0.
\]

Thus, if \(T_h=\sum_kB(k)e(hk^2/(4N))\),

\[
 \sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}|T_h|^2
 =2N\sum_k|B(k)|^2.
\tag{154.R22}
\]

The Cauchy bound in (154.R11) is consequently
\(\bigl(\sum_k|B(k)|^2\bigr)^{1/2}\), which has scale (154.R3).  A sparse
extension, zero away from the actual roots, removes this dense diagonal but
has variation proportional to the raw root count and makes (154.R20) no
better than (154.R14).  The statement supplies no quotient-profile estimate
that gives both the low BV of the dense interpolation and the low diagonal
of the sparse interpolation.

**Poisson and the rank-one stationary obstruction.**  The exact identity

\[
 \chi_4(n)=\frac{e(n/4)-e(-n/4)}{2i}
\tag{154.R23}
\]

turns a maskless Poisson transformation in \(n\) into stationary frequencies
\(h/4\), with \(h\) odd.  A stationary point satisfies

\[
 n_h=\frac{4N}{h^2},\qquad h\asymp H_0:=\sqrt{N/M},
\]

and its transformed phase is \(e(N/h)\).  Since
\(|(\sqrt{Nx})''|\asymp\sqrt N/M^{3/2}\), each transformed term, after the
factor \(n^{-3/4}\), has size \(\asymp N^{-1/4}\).  The diagonal/trivial
dual size is therefore

\[
 N^{-1/4}H_0=N^{1/4}M^{-1/2},
\tag{154.R24}
\]

the same as (154.R3).  A second-derivative estimate for
\(\sum_{h\asymp H_0}e(N/h)\) gives after normalization
\(O(M^{1/4}+M^{-3/4})\), not the target.  A first-derivative estimate is not
uniform because \(-N/h^2\) may be arbitrarily close to an integer.  If
\(n_h\) is exactly a literal component endpoint, the corresponding one-sided
(half-stationary) term remains on the same \(N^{-1/4}\) scale; it may not be
discarded or assigned to a smoothed neighboring component.

The literal large-defect mask has no stated small variation as a function of
\(n\); it can have up to \(O(M)\) jumps.  Standard Poisson cannot simply
charge its variation to that of \(A\).  Expanding the congruence first does
not create an independent second oscillatory direction.  Indeed the dense
phase for a Fourier mode \(h\) is

\[
\Psi_h(k,j)=\sqrt{k^2-j}+\frac{h(k^2-j)}{4N}
 =\phi_h(t),\qquad t=k^2-j.
\tag{154.R25}
\]

The rank-one statement applies only to these ambient Fourier-selector rows
in the dense \((k,j)\) expansion.  After the \(h\)-sum reimposes
\(F_N(k^2-j)\), the post-selection rows are the sparse root incidences in
(154.R4); no two-dimensional Hessian claim is being made about that selected
array.

Its Hessian in \((k,j)\) has determinant

\[
 \det D^2\Psi_h=2\phi_h'(t)\phi_h''(t),
\tag{154.R26}
\]

which vanishes at every relevant stationary point \(\phi_h'(t)=0\).  Along
the curve \(t=\text{constant}\) the phase is exactly constant, not merely to
quadratic order.  On the original integer cell, a fixed \(t=Nn\) has exactly
one nearest root \(k\), so changing variables back to \((n,k)\) collapses the
putative tangent sum.  A two-dimensional quadratic completion that claims a
Gauss gain in both \(k\) and \(j\) therefore counts the same one-dimensional
oscillation twice.

**Dispersion, root spacing, mask order, and powers.**  If Cauchy is placed in
a defect block, the positive diagonal in the usual absolute-correlation
majorant has scale

\[
 M^{-3/4}\{D\min(M,D)\}^{1/2}
 =\begin{cases}
 DM^{-3/4},&D\leq M,\\
 D^{1/2}M^{-1/4},&D\geq M.
 \end{cases}
\tag{154.R27}
\]

It is target-sized at \(D\asymp J\), confirming the owner-complete first
shell, but grows to \(M^{1/4}\) at \(D=M\) and to \(R\) at \(D=K\).  This
is a limitation of that positive majorant, not a claimed lower bound for the
signed sum.

For two roots with the same defect and odd quotients,

\[
 (k_1-k_2)(k_1+k_2)=N(n_1-n_2),\qquad 2N\mid(k_1-k_2)(k_1+k_2).
\tag{154.R28}
\]

Thus distinct roots are separated by
\(|k_1-k_2|\geq2N/(k_1+k_2)\gg N/K=H_0\).  If their characters agree, the
product in (154.R28) is divisible by \(4N\); if the characters are opposite,
its quotient by \(N\) is \(2\pmod4\).  For nearby defects,

\[
 (k_1-k_2)(k_1+k_2)=N(n_1-n_2)+(j_1-j_2),
\tag{154.R29}
\]

so the same \(H_0\)-spacing holds when \(|j_1-j_2|=O(K)=o(N)\), unless the
two incidences are identical.  This spacing permits \(K/H_0\asymp M\)
points, exactly the raw capacity, and hence gives no square-root cancellation.
Factor splitting and the prime-power counts above show why no coprimality
improvement is uniform.

The small mask must remain on both sides of a correlation.  If
\(S=S_{\mathrm{large}}+S_{\mathrm{small}}\), then expanding \(|S|^2\) contains the
mixed products; the scalar estimate (154.R15) before Cauchy is not a bound
for every shifted or Fourier-resolved mixed correlation.  Replacing
\({\bf1}_{|j_1|>J}{\bf1}_{|j_2|>J}\) by \(1\) inside dispersion is therefore
not justified.  Positive and negative masks, component endpoints, and the
outer \(j\)-sum must all remain until after the correlation estimate.

Finally, at the endpoint \(M=R^{780/449}\),

\[
 K=R^{1288/449},\qquad J=R^{585/449},\qquad
 H_0=R^{508/449},\qquad
 N^{1/4}M^{-1/2}=R^{59/449}.
\tag{154.R30}
\]

The order of \(J\) and \(H_0\) changes at \(M=R^{8/5}\); at the requested
upper endpoint \(J/H_0=R^{77/449}\).  Hence an argument which silently
assumes either \(J\leq H_0\) or \(J\geq H_0\) is not uniform over the stated
range.  Component counts, dyadic logarithms, and the one external
\(X^\varepsilon\) coefficient can be absorbed by changing \(\varepsilon\),
but none absorbs the powers in (154.R21), (154.R24), (154.R27), or
(154.R30).

## 4. First doubtful or unproved step

The first unproved step in the proposed quadratic-root-wave route would be
the assertion that the Gauss saving from the \(k\)-completion survives the
outer \(h\)- and \(j\)-sums.  Absolute summation gives (154.R21), Cauchy gives
the exact prime-modulus diagonal (154.R22), and the ambient Fourier-selector
stationary phase is rank-one by (154.R26).  None of these is an endpoint or
harmless logarithm; it is the central missing cancellation.

A sufficient new input would be a theorem, uniform in all factorizations and
literal endpoints, of the form

\[
 \sum_{D\leq|j|<2D}\ 
 \sum_{\substack{k^2\equiv j\pmod N\\(k^2-j)/N\ \mathrm{odd}}}
 \chi_4((k^2-j)/N)B(k,j)e(\eta(k,j))
 \ll_\varepsilon X^\varepsilon
\tag{154.R31}
\]

for every \(D\geq2H\), with both large-defect masks retained after any
dispersion and with \(B\) carrying the stated quotient BV profile.  Such a
result must exploit signed correlations **across** defect fibers; for odd
\(N\), (154.R12) proves there is no character cancellation within a fiber.
No derivation of (154.R31) follows from the statement-only hypotheses.  Thus
(154.B3) remains unproved, while (154.R2) is owner-complete.

## 5. Required control test and outcome

The analytic controls have the following outcomes.

1. **Exact/extremal cell:** squaring the half-open nearest-integer cell gives
   \([-k,k-1]\), including \(-k\) and excluding \(k\); pass.
2. **Parity/two-adic:** the two residue classes in (154.R9) remain distinct
   for odd, even, power-of-two, and mixed \(N\); pass.
3. **Imprimitive Gauss:** retaining \(d=(h,4N)\) gives the compatibility
   conditions and \(\sqrt d\) loss in (154.R19); a primitive
   \(O(\sqrt N)\) replacement fails this control.
4. **False unsigned control:** for odd \(N\), (154.R12) makes the sign constant
   on each fixed \(j\) fiber.  Absolute outer summation would prove the same
   estimate for an unsigned fiber coefficient; fail for the proposed
   sign-blind mechanism.
5. **Endpoint/mask control:** literal inequalities (154.R6)--(154.R7) and both
   factors of the large mask survive every displayed correlation; pass in the
   exact derivation, fail if the small mask is deleted after Cauchy.
6. **Diagonal/power:** the allowed odd-prime control makes (154.R22) exactly
   diagonal and leaves \(R^{59/449}\) at the requested endpoint; fail for
   Fourier-variable Cauchy.
7. **Outer-sum:** the first shell passes by (154.R16), but the bounds grow as
   in (154.R27) for later shells; fail for capacity-only summation.

## 6. Dependencies and exact artifacts used

Only the following artifacts were read:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/blind_statement.md`.

No proof graph, active strategy, candidate, prior round, sibling report,
proof draft, validation file, or web source was inspected.  The derivation
uses only elementary integer inequalities, CRT prime-power root counts,
finite Fourier inversion, quadratic Gauss evaluation (derived above),
Cauchy/orthogonality, and one-dimensional stationary-phase scale checks.
This report is the only file edited by this task.

## 7. Recommended state effect

**Revise.**  Promote, subject to conductor seam review, the exact cell and
root-defect formulas (154.R1), the parity/character encoding
(154.R9)--(154.R12), the imprimitive capacity bound (154.R14), and the strict
owner-complete shell (154.R2).  Retain (154.B3) as open.  Record the
rank-one/completion and Cauchy-diagonal obstruction, and reject any candidate
step that obtains independent Gauss savings in \(k\) and \(j\), drops
\((h,N)^{1/2}\), deletes the small mask inside a correlation, or takes
absolute values over the outer defects while claiming to use \(\chi_4\).
No effect is recommended for another coefficient, \(D>1\), \(L>1\), another
\(t\)-layer, M2, or a global theorem.
