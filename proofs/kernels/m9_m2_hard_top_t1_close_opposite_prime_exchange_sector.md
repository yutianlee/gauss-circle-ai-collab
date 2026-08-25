# Kernel: hard-TOP \(t=1\) close opposite-prime exchange sector

## Lemma

Let \(J=\sqrt X\), \(y=\lfloor J\rfloor\),
\(q_X=X/y^2\), \(H=\lfloor yX^{-1/4}\rfloor\), and
\(1\ll L\ll H\leq J^{1/2}\).  Retain the exact half-open shells, cone,
profiles, floors, stars, endpoints, parity, and zero extension in

\[
 \mathcal S_{L,1}
 =\sum_{N\asymp L^2}\mu^2(N)
  \left(\frac{L^2}{N}\right)^{3/4}e(J\sqrt N)
  \sum_{\substack{d\mid N,\ d\ {\rm odd}\\
                  \sqrt N\leq d\leq2\sqrt N}}
  \chi_4(d)\eta_L(d)\Phi\!\left(\frac d{H+1}\right)
  W\!\left(\frac{\sqrt{q_X}\,d}{2\sqrt N}\right).
\tag{K163.1}
\]

Fix \(\kappa>0\).  For every supported squarefree \(N\), choose
canonically at most one pair of distinct odd prime divisors
\(\{p_{N,L,\kappa},q_{N,L,\kappa}\}\) satisfying

\[
 \chi_4(p_{N,L,\kappa}q_{N,L,\kappa})=-1,\qquad
 \left|\log\frac{q_{N,L,\kappa}}{p_{N,L,\kappa}}\right|
 \leq\kappa L^{-1/2}.
\tag{K163.2}
\]

The rule is fixed for the \((L,\kappa)\)-block, depends on \(N\), and
does not depend on a divisor allocation.  Let
\(\mathcal S_{L,1}^{\rm cp}\) be the complete subsum of (K163.1) on
which a pair was selected and exactly one selected prime divides \(d\).
Under the accepted fixed smooth \(\eta_L,W\) and bounded \(C^1\)
\(\Phi\) interfaces,

\[
 \boxed{\mathcal S_{L,1}^{\rm cp}\ll_\kappa L^{3/2}.}
\tag{K163.3}
\]

No density, nonemptiness, or estimate for the complementary incidences
is asserted.

For any \(p\equiv3\pmod4\) dividing \(N\), the corresponding one-prime
toggle has completely disjoint physical supports.  Averaging these
one-prime identities over all such \(p\), or averaging any normalized
family of sign-reversing full divisor-lattice involutions, returns the
original coefficient exactly.  Odd complementation maps the upper
window to \([\sqrt N/2,\sqrt N]\); when \(N=2M\), the physical
complement is even and the odd-part complement \(M/d\) maps it to
\([\sqrt N/4,\sqrt N/2]\).

## Proof

For a qualifying \(N\), abbreviate its selected primes by \(p,q\), and
let

\[
 \mathscr D_N^\oplus
 =\{d\mid N:d\ {\rm odd},\
 {\bf1}_{p\mid d}+{\bf1}_{q\mid d}=1\}.
\tag{K163.4}
\]

Put \(m=N/d\).  Exchange \(p\) and \(q\) between the two factors:

\[
 T_Nd=
 \begin{cases}
 dq/p,&p\mid d,\ q\mid m,\\
 dp/q,&q\mid d,\ p\mid m.
 \end{cases}
\tag{K163.5}
\]

Squarefreeness makes this an integral fixed-point-free involution of
\(\mathscr D_N^\oplus\).  It preserves \(N\), coprimality, oddness,
and the factor \(2\) in \(m\) on the even-\(N\) branch.  It also
preserves the canonical choice, normalization, shell, and phase.  Since
\(\chi_4(pq)=-1\),
\[
 \chi_4(T_Nd)=-\chi_4(d).
\tag{K163.6}
\]

Let \(A_N(d)\) be the literal profiled physical weight, extended by zero
to every odd divisor.  Reindexing the complete ambient XOR set gives

\[
 \sum_{d\in\mathscr D_N^\oplus}\chi_4(d)A_N(d)
 =\frac12\sum_{d\in\mathscr D_N^\oplus}\chi_4(d)
 \{A_N(d)-A_N(T_Nd)\}.
\tag{K163.7}
\]

Write \(\theta_N=\log(q/p)\), so
\(|\theta_N|\leq\kappa L^{-1/2}\).  The two orientations change
\((d,m)\) to
\((e^{\pm\theta_N}d,e^{\mp\theta_N}m)\).  On one common smooth cell,
the accepted profile seminorms give

\[
 |A_N(d)-A_N(T_Nd)|\ll_\kappa L^{-1/2}.
\tag{K163.8}
\]

Indeed, the ordinary derivative bound
\(\|\eta_L'\|_\infty\ll L^{-1}\) makes the dyadic profile change by
\(O(|\theta_N|)\), the
\(\Phi\)-profile by
\(O(|\theta_N|L/H)\), and the \(W\)-argument is multiplied by
\(e^{\pm\theta_N}\).  All other factors are invariant.  There are
\(O(L^2)\) possible ordered integer pairs in the support, so common
cells cost \(O_\kappa(L^{3/2})\).

The exchange multiplies \(d/m\) by \(e^{\pm2\theta_N}\).  A cone,
ratio-profile, dyadic, vertical-profile, or zero-extension face can be
crossed only in one of finitely many strips

\[
 |d-\lambda m|\ll_\kappa L^{1/2}+1,\qquad
 |d-\lambda L|\ll_\kappa L^{1/2}+1.
\tag{K163.9}
\]

Each has \(O_\kappa(L^{3/2}+L)\) lattice points.  Exact ceilings,
half-open ties, and star changes contribute only their \(O(L)\) face.
The product shell does not move, and every arithmetic restriction only
deletes pairs.  If one leg is supported, closeness keeps the other in a
fixed enlarged \(O(L)^2\) box; hence zero-extended partner legs create
no uncounted tail.  Boundedness of the normalized amplitude and
(K163.7)--(K163.9) prove (K163.3).

For the one-prime statement, write
\[
 b_{L,X}(N)=
 \sum_{\substack{d\mid N/p\\d\ {\rm odd}}}
 \chi_4(d)\{A_N(d)-A_N(pd)\}.
\tag{K163.10}
\]
If \(A_N(d)\ne0\), then \(pd>2\sqrt N\); if \(A_N(pd)\ne0\), then
\(d<\sqrt N\).  Thus the difference is all leakage.  Summing (K163.10)
over \(p\in\mathcal P_3(N)\), every active \(r\) appears with sign
\(\chi_4(r)\) whether \(p\nmid r\) or \(p\mid r\), since in the latter
case
\(-\chi_4(r/p)=\chi_4(r)\).  The sum is therefore
\(|\mathcal P_3(N)|b_{L,X}(N)\).  The same change-of-variables argument
proves exact self-return for any normalized family of sign-reversing
divisor-lattice involutions.

Finally, \(d\mapsto N/d\) sends
\([\sqrt N,2\sqrt N]\) to \([\sqrt N/2,\sqrt N]\).  For \(N=2M\),
\(N/d\) is even, while \(d\mapsto M/d\) sends the window to
\([\sqrt N/4,\sqrt N/2]\).  These are excluded lower-window rewrites,
not second physical legs.  This proves the lemma.

## Scope

The kernel closes only the exact canonical XOR incidence sector in
(K163.2)--(K163.4).  The neither-prime, both-prime, and no-qualifying-pair
incidences remain open, as do all other few-point channels, full hard
TOP, both smooth M2 packets, M9--M2, M9, endpoint uniformity, the
bridge, the quarter theorem, and both global exponents.
