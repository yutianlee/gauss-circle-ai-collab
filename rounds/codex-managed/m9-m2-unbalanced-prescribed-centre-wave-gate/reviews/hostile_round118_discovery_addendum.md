# Hostile Round-118 discovery addendum

Scope: only the proposed promotions (118.3) and (118.7) in
literal_unbalanced_wave_attack.md were audited.

## Verdict table

| Candidate | Verdict | First issue | Maximal safe scope |
|---|---|---|---|
| Flat-row curvature/product-window bound (118.3) | **PASS with one parity clarification** | After resolving \(\chi _4\), the proof must either extend the character identity to all integers before splitting the two branches, or reparametrize \(r=2n+1\). A zero-extension of the smooth amplitude alone would have large variation. | Promote (118.3)--(118.6) for each frozen flat smooth component, with exact profiles and the accepted stationary remainder. No endpoint or downstream promotion follows. |
| Variable-step same-residue run lemma (118.7) | **REPAIR; do not promote verbatim as a uniform \(\delta\)-statement** | The implication \(\delta>1/3\Rightarrow X/D^3=o(1)\) is only uniform when \(\delta-1/3\) is fixed. It does not cover dyadic scales with \(D^3/X\) bounded while \(\delta=\delta(X)>1/3\). | Promote the actual-scale split (A.8) below. The original split is valid only for fixed \(\delta\), with constants and the starting \(X\) allowed to depend on \(\delta\). |

## Audit of (118.3)

For fixed \(r\), the literal \(k\)-weight has support \(O(K)\), supremum
and total variation \(O(K^{-1})\). Abel summation therefore gives
\[
 \left|\sum_k\frac{q_L(4Xk/r^2)}k e(Xk/r)\right|
 \ll \min\!\left(1,\frac1{K\|X/r\|}\right).
 \tag{A.1}
\]
If \(\|X/r\|<\eta\), the nearest integer \(d\asymp D\) gives an integer
product \(s=rd\) in an interval of length \(O(1+\eta R)\) about \(X\).
Each \(s\) has \(O_\varepsilon(X^\varepsilon)\) admissible divisor pairs.
The layer cake from \(K^{-1}\) to \(1/2\) consequently costs
\[
 \frac RK\log(2K)X^\varepsilon
 =\frac DL X^\varepsilon.
 \tag{A.2}
\]
Thus the first entry of (118.3) passes; it is also the direct absolute
capacity of the product form.

For fixed \(k\), put
\[
 w_k(r)=\frac1kW\!\left(\frac{X}{rD}\right)
 q_L\!\left(\frac{4Xk}{r^2}\right).
\]
On the strict flat cell, \(H_D+1\gg L\) (with the terminal crossing
owned separately), so
\[
 q_L'(h)\ll L^{-1}
\]
on the flat cell, including the Vaaler factor. Since
\((4Xk/r^2)'=O(L/R)\), the two composed profiles have total variation
\(O(1)\); hence
\[
 \|w_k\|_\infty+\operatorname {Var}(w_k)\ll K^{-1}.
 \tag{A.3}
\]
The floor in \(H_D\) is a fixed parameter and creates no \(r\)-jump.
This argument does not apply to a sharp, starred, hard, or clipped
endpoint kernel.

The parity step is safe but should be stated. The identity
\[
 \chi _4(r)=\frac{e(r/4)-e(-r/4)}{2i}
 \tag{A.4}
\]
holds on every integer, including the zero value on even integers.
One may therefore extend the character sum to all integers and bound
the two smooth branch sums separately. Equivalently, retain the odd
restriction and put \(r=2n+1\); the interval length is \(R/2\) and the
second derivative is multiplied by \(4\), producing the same order.
One should not zero-extend \(w_k\) itself and then claim (A.3).

For either lawful implementation,
\[
 f_\pm''(r)\asymp \frac{LD}{X},
\]
and the weighted second-derivative estimate gives, for each \(k\),
\[
 \sum_r\chi _4(r)w_k(r)e(Xk/r)
 \ll \frac1K
 \left(\sqrt{\frac{XL}{D}}+\sqrt{\frac{X}{LD}}\right).
 \tag{A.5}
\]
There are \(O(K)\) supported \(k\)'s and
\(K=X^{1+\ell-2\delta}\to\infty\), so the \(k\)-triangle cancels exactly
the displayed \(K^{-1}\). No Cauchy or extra divisor factor occurs.

Finally, with \(a=\delta-\ell\), the leading curvature exponent is
\((1-a)/2\), the other curvature term is no larger, and the product
capacity exponent is \(a\). Hence
\[
 \beta(a)=\min\!\left(a,\frac{1-a}{2}\right),\qquad
 \beta(a)<a\Longleftrightarrow a>\frac13,
 \tag{A.6}
\]
with saving \((3a-1)/2\). Because \(1/4<a<1/2\),
\(\beta(a)>1/4\). The exponent ledger in (118.3)--(118.6) passes
exactly. The same curvature bound works without the character, so it is
a literal-row bound but not evidence of character-specific cancellation.

## Audit and repair of (118.7)

Let
\[
 E=\sup_d\left|r_d-\frac Xd\right|\ll \frac cL.
 \tag{A.7}
\]
If all \(r_d\) lie in one residue class modulo \(4\), every finite
difference of \(r_d\) is in \(4\mathbb Z\). The second- and third-order
error differences are at most \(4E\) and \(8E\). Choosing the central
constant \(c\) so that these are strictly below half the lattice gap is
legitimate and uniform because \(L\geq1\).

For a fixed exponent \(\delta>1/3\), \(X/D^3\to0\), so the discovery
argument correctly forces \(\Delta^2r_d=0\). For fixed
\(1/4<\delta\leq1/3\), it correctly forces
\(\Delta^3r_d=0\). The latter smallness is in fact uniform in this
campaign: (118.9) and \(\ell<\delta-1/4\) imply
\(\delta>1015/3632\), and hence \(X/D^4\ll X^{-107/908}\).

The first implication is not uniform at the moving transition
\(\delta=1/3\). The safe statement is in terms of the actual scale.
There is a profile-dependent constant \(C_0\) such that, for all
sufficiently large \(X\),
\[
 U\ll
 1+
 \begin{cases}
  (D^3/(XL))^{1/2},&D^3\geq C_0X,\\[2mm]
  (D^4/(XL))^{1/3},&D^3<C_0X.
 \end{cases}
 \tag{A.8}
\]
Indeed, in the first case \(C_0\) makes
\(|\Delta^2(X/d)|+4E<2\), so the \(4\mathbb Z\) lattice gap forces
\(\Delta^2r_d=0\). In the second case the uniform bound
\(|\Delta^3(X/d)|+8E<2\) forces \(\Delta^3r_d=0\).

The length inference also passes once the separated points are made
explicit. If \(r_d\) is affine, take three points separated by
\(\asymp U\). Their second divided difference has error
\(O(E/U^2)\), while that of \(X/d\) is
\(\asymp X/D^3\), giving \(U^2\ll D^3/(XL)\). If \(r_d\) is quadratic,
take four points separated by \(\asymp U\). Their third divided
difference has error \(O(E/U^3)\), while that of \(X/d\) is
\(\asymp X/D^4\), giving \(U^3\ll D^4/(XL)\). Runs with fewer than the
required points are covered by the added \(1\).

There is no missed tie inside the selected residue class: after shrinking
\(c\), (A.7) is \(<2\), so at most one integer in that class can be
selected. A tie between the two odd residue classes belongs to the
uncontrolled complement and supplies neither cancellation nor a lower
bound.

Both branches of (A.8) are uniformly target-safe. In the second branch,
\(D^3<C_0X\) gives \(U\ll X^{1/9}L^{-1/3}\). In the first,
\(D<X^{1/2}\) gives \(U\ll X^{1/4}L^{-1/2}\); it is
\(o(X^{1/4})\) only when the exponent \(\delta<1/2\) is fixed away from
the hard boundary. Thus the uniform promotion should say
target-safe, not uniformly little-oh.

## Maximal safe promotion

Promote (118.3)--(118.6) for frozen flat smooth owners after inserting
the parity sentence above. Promote the run result only in the
actual-scale form (A.8), or retain the original (118.7) with an explicit
fixed-\(\delta\), nonuniform qualifier.

The run promotion is solely an upper bound for one consecutive
same-residue central-lobe selector. It does not require positivity of
\(W\), does not cover a union of runs, step-change complements,
noncentral shoulders, endpoint kernels, or the complete signed wave.
Neither promoted candidate proves a strict \(X^{1/4+\varepsilon}\)
subrange or changes any downstream obligation.
