# Round 88 hostile/source audit: cross-group period depth

## 1. Result

**Verdict: revise the proposed mechanism and retain the full target as open.**  Two strictly smaller statements are certifiable:

1. There is an exact, mask-aware prime-power Fourier filtration and an exact CRT factorization of the completed trace.  They route every prime power, including an empty unit domain, nonunit \(K\), and the full \(2\)-part, without making a cancellation claim.
2. A nonempty **congruence-aligned coarse-depth** part of the strict cross-group, \(u\ne0\) survivor is target-safe by physical-row counting.  If \(m\mid M\), \(R=M/m\), and two distinct full-\(M\) groups become the same Round-87-type group after reduction modulo \(m\), then their centered-Fejer package is
   \[
   \ll_\varepsilon X^\varepsilon D B^3R^2T^4Q^{-5/6}.
   \]
   Consequently it meets the frozen target whenever
   \[
      R\le R_{\rm crit}(B):=J^{11/30}B^{-2}.
   \]
   Since \(J^{11/90}<B\le J^{3/20}\), this threshold decreases from the scale \(B\) at the lower conductor boundary to \(J^{1/15}\) at the upper boundary.  Thus \(R\le J^{1/15}\) is a uniform sufficient condition over the frozen conductor range.
3. After that coarse deletion, a second nonempty part is target-safe by a good-prime depth/degree argument.  Put
   \[
      \rho_*(B)=J^{11/30}B^{-2}.
   \]
   At each \(p^\nu\Vert M\) with \(p\ge11\) and \(p\nmid K\), assign the unique maximal nontrivial period depth \(j_p\) of the **reciprocal masked weight** (not of the full affine phase), put \(a_p=\min(j_p,\nu-j_p)\), and set
   \[
      \mathfrak a=\prod_{\substack{p^\nu\Vert M\\p\ge11,\ p\nmid K\\j_p>0}}p^{a_p}.
   \]
   The remaining physical edges with
   \(\mathfrak a\ge M^2/\rho_*^2\) have a target-safe centered-Fejer package.  This statement leaves affine periods, nonunit-\(K\) primes, \(p\le7\), the \(2\)-part, and projected-frequency depth in the residual.

This does **not** prove
\(
\mathcal G_{\rm cross}(D)\ll_\varepsilon X^\varepsilon(D/B)J^{14/5}
\).
The proposed identification of all functional period depth with valuations of the quadratic numerator (88.11), or with pair congruence modulo \(M/R\), is false.  The four-unit mask creates accidental periods at \(p=3,5\); the \(2\)-part has an automatic first period whenever it is nonempty; a nonunit \(K\) lowers the phase conductor; and the additive frequency \(u\) can cancel a nonzero constant derivative on a small unit domain.  Divisor-lattice differences of the coarse groups therefore isolate only congruence-aligned depth, not all functional depth.

There is also an exact coefficientwise obstruction.  For \(q=3^\nu\), \(\nu\ge2\), and \(3\nmid K\), put
\[
 h_1=1,\qquad v=0,\qquad h_2=1+q/3,\qquad u=q/3.
\]
The two full-\(q\) active labels are distinct but the completed trace satisfies
\[
 |\mathfrak T_q(u,0;h_1,h_2)|=q^2/3.
\]
Thus a uniform square-root estimate for every cross-group completed coefficient is false, even for unit \(K\) and \(u\ne0\).  This example is, however, included in the certified coarse deletion with \(m=q/3\), \(R=3\).  It is not an actual-symbol lower bound and hence is not a no-go for the frozen aggregate itself.  No audited primary source supplies the missing joint estimate against the actual symbol \(\widehat\Omega(v,h_1,h_2)\).

## 2. Exact statement and hypotheses

Retain all frozen hypotheses of the derivation packet:
\[
 J=X^{1/2},\quad Q=J^{2/5},\quad T=J^{3/5},\quad B=C/T,
 \quad J^{13/18}<C\le J^{3/4},
\]
\(b\asymp B\), \(M\in\{4b,2b,b\}\asymp B\), the exact three values of \(K\), the signed deep projection \(\Pi_{b,D}\), and
\[
 \|\mathcal R_{b,x}\|_\infty\ll_\varepsilon
 X^\varepsilon L,\qquad L:=TQ^{-5/24}.
\]
The coefficient of \(F_{b,P}\) already contains \(M^{-2}\).  All statements below concern only the already-projected deep physical rows and make no claim for any support or error stratum excluded in the packet.

**Exact masked local filtration.**  Let \(q=p^\nu\Vert M\), \(M_q=M/q\), and
\(
\lambda_q\equiv M_q^{-1}\pmod q
\).
For \(A=h_1\), \(B_2=h_2\), \(V=v\), define on \(\mathbb Z/q\mathbb Z\)
\[
 W_q(x)=\mathbf 1_{q}^{\rm unit}(x;A,B_2,V)
 e_q\!\left(\lambda_qK\Phi_{A,B_2,V}(x)\right),
\]
where the indicator requires \(x,x-A,x-V,x-V-B_2\) to be units.  For \(0\le r\le\nu\), set
\[
 E_rW_q(x)=p^{r-\nu}\!\sum_{t\bmod p^{\nu-r}}
 W_q(x+t p^r),\qquad
 L_0W_q=E_0W_q,\quad L_rW_q=E_rW_q-E_{r-1}W_q.
\]
Then \(W_q=\sum_{r=0}^{\nu}L_rW_q\); \(E_rW_q\) is \(p^r\)-periodic; the Fourier transform of \(L_0W_q\) is supported at frequency \(0\); and for \(r\ge1\) the Fourier transform of \(L_rW_q\) is supported in the exact-valuation shell
\[
 v_p(u)=\nu-r.
\]
This remains true when \(K\) is a nonunit and when the mask is empty.  It is an orthogonal algebraic decomposition, not a trace estimate and not a claim that \(E_rW_q\) remains a member of a standard rational-trace family.

With \(\widehat W_q(a)=\sum_{x\bmod q}W_q(x)e_q(ax)\), the exact CRT formula is
\[
 \mathfrak T_M(u,v;h_1,h_2)
   =M\prod_{q\Vert M}\widehat W_q(\lambda_qu).
\]
Multiplication by the unit \(\lambda_q\) does not change \(v_p(u)\).

**Limited large-prime period lemma.**  Suppose \(p\ge11\), \(\nu\ge2\), and \(p\nmid K\).  If the *reciprocal masked weight* \(W_q\) is invariant under translation by \(q/p\), then modulo \(p\)
\[
 A=B_2,\qquad AV=0.
\]
Hence either \(V=0,A=B_2\), or \(A=B_2=0\); in both cases the two local labels are the same after reduction modulo \(p\).  This statement is deliberately limited to \(W_q\).  It does not apply merely because the full summand \(e_q(ux)W_q(x)\) is periodic: the linear term can participate in an affine cancellation.

**Good-prime depth-to-degree lemma.**  Suppose \(p^\nu\Vert M\), \(p\ge11\), \(p\nmid K\), \(1\le j\le\nu-1\), and the reciprocal masked weight \(W_q\) has period \(p^{\nu-j}\).  Put
\[
 a=\min(j,\nu-j).
\]
Then
\[
 p^a\mid(B_2-A),\qquad p^a\mid AV,\qquad
 p^a\mid AV(V+B_2).                                      \tag{3}
\]
For each nonzero mask, define \(j_p\) to be its unique maximal such depth, with \(j_p=0\) if it has no nontrivial period, and put
\[
 \mathfrak a=\prod_{\substack{p^\nu\Vert M\\p\ge11,\ p\nmid K\\j_p>0}}
 p^{\min(j_p,\nu-j_p)}.
\]
For a fixed oriented physical pair \(P\), the number of partner pairs \(P'\) with a prescribed good-prime depth vector is at most
\[
 \Delta_{\rm deg}:=\frac{M^2}{\mathfrak a};
\]
the same bound holds for in-degree and out-degree.  After first deleting the certified coarse-congruence edges, restrict to the remaining edges and retain their maximal depth labels.  With
\(\rho_*=J^{11/30}B^{-2}\), the union of remaining exact good-depth edge classes satisfying
\[
 \mathfrak a\ge \frac{M^2}{\rho_*^2}                     \tag{4}
\]
obeys the frozen target.  Empty masks are zero and receive no depth label.  No assertion is made here for a period of the full affine summand, a nonunit \(K\), \(p\le7\), \(p=2\), or a Fourier projection that is periodic although \(W_q\) itself is not.

**Small-prime and \(2\)-adic exceptions.**  The following are exact.

- For every \(\nu\ge2\), \(q=3^\nu\), and any unit \(K\), the choice
  \((A,B_2,V)=(1,2,1)\) has unit domain \(x\equiv2\pmod3\), and \(W_q\) has period \(q/3\), although the numerator
  \(N=x^2+2x\) has a \(3\)-adic unit coefficient.
- For every \(\nu\ge2\), \(q=5^\nu\), and any unit \(K\), the choice
  \((A,B_2,V)=(1,2,2)\) has unit domain \(x\equiv3\pmod5\), and \(W_q\) has period \(q/5\), although the three displayed numerator coefficients are \(1,4,-8\), all \(5\)-adic units.
- For \(q=5^\nu\), \((A,B_2,V)=(1,1,2)\), the domain is \(x\equiv4\pmod5\) and \(\Phi'(x)\equiv1\pmod5\) there.  Thus the *full* summand has period \(q/5\) whenever \(u\equiv-K\pmod5\), even though this need not be a period of \(W_q\).
- For \(q=2^\nu\), the unit domain is nonempty exactly when \(A,B_2,V\) are all even, in which case it is precisely the odd residue classes.  If \(\nu\ge2\), \(W_q\) then always has period \(q/2\).  If one of \(A,B_2,V\) is odd, the local trace is zero.  No deeper \(2\)-adic classification is asserted beyond the exact filtration above.

An empty domain is the zero function.  Its vacuous possession of every period must be routed as a zero trace, not counted as large periodic mass.

**Certified coarse-depth subaggregate.**  Fix any divisor \(m\mid M\), and write \(R=M/m\).  Factor \(m\) into its full prime-power factors.  For a physical ordered pair \(P=(x,y)\), reduce it modulo \(m\) and form the same active-set/active-label datum used in Round 87; unlike the full-\(M\) datum, the coarse active set is allowed to be empty.  Denote this coarse group by \(c_m(P)\), and denote the original full-\(M\) group by \(\gamma_M(P)\).

For a coarse group \(c\) and a full group \(\gamma\), put
\[
 H^{(m)}_{b,c,\gamma}
 =\Pi_{b,D}\!\sum_{\substack{P:\ c_m(P)=c\\
                         \gamma_M(P)=\gamma}}F_{b,P}.
\]
Let
\[
 K_D^\circ(\theta)=|D_D(\theta)|^2-D.
\]
Its zero Fourier coefficient vanishes, its nonzero Fourier coefficients are (D-|u|) for (0<|u|<D), and
\(
\|K_D^\circ\|_{L^1(\mathbb T)}\le2D
\).
Define the exact aligned strict-cross package
\[
 \mathcal G^{(m)}_{\rm align}(D)
 =\sum_{b\asymp B}\int_{\mathbb T}K_D^\circ(\theta)
   \sum_c\sum_{\gamma\ne\gamma'}
     H^{(m)}_{b,c,\gamma}(\theta)
     \overline{H^{(m)}_{b,c,\gamma'}(\theta)}\,d\theta.
\]
This is exactly the part of the original strict full-group cross term for which the two physical pairs lie in one coarse group modulo \(m\), with \(u=0\) removed coefficientwise.  Uniformly in all three exact classes, arbitrary \(K\), and without assuming \((m,R)=1\),
\[
 \boxed{
 |\mathcal G^{(m)}_{\rm align}(D)|
 \ll_\varepsilon X^\varepsilon D B^3R^2T^4Q^{-5/6}.}
\]
Nested divisor-lattice differences may isolate exact *coarse-congruence* shells at a divisor-count cost.  They may not be identified with the functional (L_rW_q)-shells.

## 3. Proof or derivation

**Normalization and completion.**  Each physical factor is
\[
 F_{b,P}=e_M(K(\bar x-\bar y))
          \mathcal R_{b,x}\overline{\mathcal R_{b,y}},
 \qquad \|F_{b,P}\|_\infty\ll_\varepsilon X^\varepsilon L^2.
\]
There are two normalized rows here, so the physical Fourier coefficient already has (M^{-2}).  In the centered complete expansion the normalization is
\[
 M^{-5}\!\sum_{v\bmod M}\sum_{h_1,h_2\ne0}
 \mathfrak T_M(u,v;h_1,h_2)\widehat\Omega(v,h_1,h_2):
\]
\(M^{-4}\) comes from the four normalized rows and \(M^{-1}\) from Fourier inversion, while \(\mathfrak T_M\) retains its outer \(M\).  There is no further \(M^{-2}\).  The coarse proof below stays in physical variables and therefore preserves the same normalization automatically.

**Masked filtration and CRT.**  The operators \(E_r\) are conditional averages over the subgroup \(p^r\mathbb Z/p^\nu\mathbb Z\).  Hence
\(
E_rE_s=E_{\min(r,s)}
\), the differences \(L_r\) are mutually orthogonal projections, and they telescope to \(E_\nu=1\).  Translation invariance by \(p^r\) forces
\(
e_q(up^r)=1
\), equivalently \(p^{\nu-r}\mid u\).  Subtracting \(E_{r-1}\) removes the frequencies divisible by \(p^{\nu-r+1}\), proving the exact valuation assertion.  This argument uses the entire masked function and so has no good-prime, nonunit-\(K\), or nonempty-domain proviso.

CRT gives
\(
e_M(z)=\prod_{q\Vert M}e_q(\lambda_qz)
\)
and the four unit conditions factor over \(q\Vert M\).  The \(x\)-sum therefore factors, giving the displayed product formula.  Tensor orthogonality now says only that a global frequency must lie in the compatible local valuation supports.  It supplies no saving in the size of a surviving factor or in the later \(v,h_1,h_2,b\) sums.

**Why numerator-only depth fails.**  Put \(h=q/p=p^{\nu-1}\).  For every unit \(z\pmod q\),
\[
 (z+h)^{-1}\equiv z^{-1}-hz^{-2}\pmod q,
\]
because \(h^2\equiv0\pmod q\).  Thus on a mask stable under the translation,
\[
 \Phi(x+h)-\Phi(x)\equiv h\Phi'(x)\pmod q.       \tag{1}
\]
For \((A,B_2,V)=(1,2,1)\) modulo \(3\), the four poles reduce to \(0,1,1,0\); the sole allowed class is \(x=2\), and direct substitution gives \(\Phi'(2)=0\).  For \((1,2,2)\) modulo \(5\), the poles are \(0,1,2,4\); the sole allowed class is \(x=3\), and \(\Phi'(3)=0\).  Equation (1) proves the claimed periods, while (88.11) gives the stated unit numerator coefficients.  For \((1,1,2)\) modulo \(5\), the sole allowed class is \(4\) and \(\Phi'(4)=1\); applying (1) to \(ux+K\Phi(x)\) gives the affine cancellation condition \(u+K\equiv0\pmod5\).

If \(p^\kappa\mid K\), the exponential phase is already evaluated at a modulus lowered by \(p^\kappa\), subject to the residual mask conductor.  This is another depth mechanism not read off from \(N\).  The exact projections route it without guessing its smallest period.

For \(p=2\), simultaneous unit conditions force \(x\) odd and each of \(A,V,V+B_2\) even, equivalently \(A,B_2,V\) all even.  On odd \(x\), every inverse square is \(1\pmod2\), so
\[
 \Phi'(x)=-x^{-2}+(x-A)^{-2}+(x-V)^{-2}-(x-V-B_2)^{-2}
 \equiv0\pmod2.
\]
Equation (1), now with \(h=q/2\), proves the automatic \(q/2\)-period.  If one of the shifts is odd, no \(x\pmod2\) satisfies the four unit conditions.

For the limited \(p\ge11\) lemma, period \(q/p\) and \(p\nmid K\) imply \(\Phi'(x)=0\pmod p\) on every allowed residue.  There are at least \(p-4>5\) such residues.  With
\[
 D_0=x(x-A)(x-V)(x-V-B_2),\qquad \Phi=N/D_0,
\]
the numerator of \(\Phi'\) is \(N'D_0-ND_0'\), of degree at most \(5\).  It therefore vanishes identically over \(\mathbb F_p\).  Since all numerator and denominator degrees are \(<p\), a rational function with zero derivative is constant; since \(\deg N<\deg D_0\), it is zero.  Thus \(N=0\).  Its three coefficients give
\(
B_2=A
\) and \(AV=0\).  Pole collisions only decrease the number of forbidden residues, so they do not damage the root count.  The proof does not extend to the full affine phase, and the small-prime examples show that the threshold cannot simply be discarded.

For the deeper good-prime statement, let \(a=\min(j,\nu-j)\) and
\(s=\nu-a=\max(j,\nu-j)\).  Translation by \(p^s\) is a multiple of the assumed period \(p^{\nu-j}\), while \(2s\ge\nu\).  Inverse Taylor expansion at that translation has no surviving quadratic term modulo \(p^\nu\), so invariance and \(p\nmid K\) give
\[
 \Phi'(x)\equiv0\pmod {p^a}
\]
for every allowed \(x\).  Choose six allowed integer representatives in distinct residue classes modulo \(p\); at least \(p-4\ge7\) are available.  The degree-at-most-five polynomial
\[
 R_0=N'D_0-ND_0'
\]
vanishes modulo \(p^a\) at those six points.  Their Vandermonde determinant is a \(p\)-adic unit, so every coefficient of \(R_0\) is divisible by \(p^a\).

Modulo \(p\), \((N/D_0)'=0\).  Since all degrees are \(<p\), \(N/D_0\) is constant in \(\mathbb F_p(x)\), and its value at infinity is zero; hence \(p\mid N\).  Write \(N=pN_1\), divide \(R_0\) by \(p\), and repeat.  Induction gives \(p^a\mid N\) coefficientwise.  Formula (88.11), with \(2\) a \(p\)-unit, gives (3).

**Large cross-group return.**  Let \(q=3^\nu\), \(L=q/3\), and use the parameters in Section 1.  The mask is \(x\equiv2\pmod3\), so it contains \(q/3\) points.  Writing \(z=x-1\), one has \(L^2\equiv0\pmod q\) and
\[
 \Phi(x)=(z-L)^{-1}-z^{-1}\equiv Lz^{-2}\pmod q.
\]
Hence
\[
 e_q\big(ux+K\Phi(x)\big)
 =e_q\big(L(x+Kz^{-2})\big)=e_3(2+K)
\]
on the whole mask.  The inner complete sum has magnitude \(q/3\); the outer factor \(q\) in \(\mathfrak T_q\) gives \(q^2/3\).  The labels \(1\) and \(1+L\) differ modulo \(q\), but agree modulo \(L\), so this exact obstruction lies in the coarse package \(m=L,R=3\).  Since \(M\asymp B\ll D_1\le D\), its nonzero shift also carries a full-size Fejer weight; it cannot be removed by choosing \(U<D\).

**Coarse physical-row count.**  For a coarse active set (S), let (m_S) be the product of its active prime-power factors and (r_S=m/m_S).  There are at most (m_S^2) coarse active labels.  Once a label is fixed, there are at most (r_S) inactive diagonal residue choices modulo (m), and each reduced ordered pair has at most (R^2) lifts modulo (M).  Thus a coarse group contains at most (r_SR^2) physical pairs.  The sharp deep projection costs only the logarithm in (88.4), and therefore
\[
 \sum_{c:\,S(c)=S}\left|\Pi_{b,D}\sum_{P:c_m(P)=c}F_{b,P}\right|^2
 \ll_\varepsilon X^\varepsilon
 m_S^2(r_SR^2)^2L^4
 =X^\varepsilon M^2R^2L^4.                     \tag{2}
\]
Intersecting a coarse group with the full groups \(\gamma\) does not enlarge this bound: if its fiber sizes are \(n_{c,\gamma}\), then
\(
\sum_\gamma n_{c,\gamma}^2\le(\sum_\gamma n_{c,\gamma})^2
\).
The number \(2^{\omega(m)}\) of active sets is absorbed into \(X^\varepsilon\).  This counting uses only the reduction map; it does not require \((m,R)=1\), and unit constraints only reduce the fibers.  The coarse empty active set must be retained because an off-diagonal pair modulo \(M\) can become diagonal modulo \(m\).

For each (c),
\[
 \sum_{\gamma\ne\gamma'}H_{c,\gamma}\overline{H_{c,\gamma'}}
 =\left|\sum_\gamma H_{c,\gamma}\right|^2-
   \sum_\gamma|H_{c,\gamma}|^2.
\]
Taking absolute values costs the two positive quantities controlled by (2).  The kernel \(K_D^\circ\), rather than a second use of the global A-process diagonal, removes \(u=0\) exactly and has \(L^1\)-norm at most \(2D\).  Summing (2) over \(b\asymp B\), using \(M\asymp B\) and \(L^4=T^4Q^{-5/6}\), proves
\[
 |\mathcal G^{(m)}_{\rm align}(D)|
 \ll_\varepsilon X^\varepsilon DB^3R^2T^4Q^{-5/6}.
\]
The ratio of this bound to the frozen target is
\[
 \frac{B^3R^2T^4Q^{-5/6}}{B^{-1}J^{14/5}}
 =R^2B^4J^{-11/15},
\]
because (T^4=J^{12/5}) and (Q^{-5/6}=J^{-1/3}).  This proves the sharp stated threshold.

**Good-depth directed-edge count.**  In (88.10), \(A\) and \(B_2\) are the oriented differences of the two physical pairs.  For a fixed first pair, (3) gives
\(B_2\equiv A\pmod{\mathfrak a}\).  Before unit and off-diagonal restrictions, choose one coordinate of the partner in \(M\) ways and the other in at most \(M/\mathfrak a\) ways.  Thus both directed in-degree and out-degree are at most \(M^2/\mathfrak a\).  Removing the already-owned coarse edges can only decrease these degrees.

For the remaining exact-depth graph, Schur's directed-edge bound gives pointwise
\[
 \left|\sum_{(P,P')\in E}(\Pi F_P)\overline{(\Pi F_{P'})}\right|
 \le \frac{M^2}{\mathfrak a}\sum_P|\Pi F_P|^2
 \ll_\varepsilon X^\varepsilon
 \frac{M^4}{\mathfrak a}L^4.
\]
The centered kernel contributes \(O(D)\), and summation over \(b\asymp B\) gives
\[
 \ll_\varepsilon X^\varepsilon
 DB^3\frac{M^2}{\mathfrak a}T^4Q^{-5/6}.             \tag{5}
\]
There are at most a divisor-function number of exact depth vectors, absorbed into \(X^\varepsilon\).  The ratio of (5) to the frozen target is
\((M^2/\mathfrak a)B^4J^{-11/15}\).  Since
\(\rho_*^2=J^{11/15}B^{-4}\), condition (4) makes this ratio \(O(1)\).  Maximal reciprocal-weight period depth gives a unique edge label; processing the coarse deletion first and then restricting the graph prevents double ownership.

**Why completion does not finish the residual.**  At (v=0), the actual completed symbol has the form
\[
 \widehat\Omega(0,h_1,h_2)
 =\sum_d F_{d+u}(h_1)\overline{F_d(h_2)}.
\]
Only \(h_1=h_2\) is a same-frequency shifted correlation.  For the strict cross terms \(h_1\ne h_2\), no orthogonality identity is available.  Applying a pointwise trace bound before exploiting this symbol discards the only remaining possible source of cancellation, while applying completion and inversion without a new operator estimate returns to the original physical sum.  The \(q^2/3\) example shows concretely that completion can expose a lower-conductor return rather than create a gain.

## 4. First doubtful or unproved step

The first genuinely unproved step after the certified coarse deletion and the large-\(\mathfrak a\) good-depth graph deletion is a joint, actual-weight estimate for the residual pieces:
\[
 M^{-5}\sum_{v,h_1,h_2}
 \mathfrak T_M(u,v;h_1,h_2)\widehat\Omega(v,h_1,h_2),
\]
summed with the true Fejer weights, both signs of \(u\), all \(b\asymp B\), and the exact deep support.  Neither the prime-power projections nor CRT orthogonality bounds this operator.  In particular:

- \(E_rW_q\) is an exact projected function but need not be a rational phase to which a quoted one-variable theorem applies.
- Local Fourier supports select valuations of \(u\); after that selection their norms can still be maximal, and compatible large factors tensor together.
- Coarse Möbius inversion sees only pair congruence.  The good-depth graph sees only an actual period of the reciprocal masked weight at \(p\ge11\), \(p\nmid K\).  The residual still contains \(p=3,5,7\), affine \(u+K\Phi'\) cancellation, nonunit-\(K\) conductor loss, the \(2\)-part, small-\(\mathfrak a\) good depth, and aperiodic or projection-only depth.
- Taking absolute values in \(v,h_1,h_2\) before the actual symbol is used loses the cross-frequency structure and gives no route to the required \(Q^{-5/12}\) row gain.

Accordingly, any assertion that “all exact-depth shells follow by divisor-lattice Möbius inversion” is unproved and false if “depth” means functional period depth.  The literal defensible version is only “all nested coarse-congruence shells can be differenced at divisor-count cost.”

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Normalized rows / duplicate (M^{-2}) | **Pass.**  (F_{b,P}) contains the two row normalizations already.  The completed expression is (M^{-5}\mathfrak T_M\widehat\Omega), with the outer (M) retained inside \(\mathfrak T_M\).  No additional (M^{-2}) was used. |
| (Q^{-5/12}) | **Pass for the certified part.**  Two rows give (L^2); squaring the group sum gives (L^4=T^4Q^{-5/6}).  No source theorem was credited with manufacturing this factor. |
| Fejer (U=D) and (u=0) | **Pass.**  (K_D^\circ=|D_D|^2-D) has exactly the nonzero Fejer coefficients and \(\|K_D^\circ\|_1\le2D\).  The global (u=0) diagonal is not re-owned. |
| Round-87 same-group ownership | **Pass.**  The new package uses \(\gamma\ne\gamma'\) throughout.  Its positive squares are only a domination device for a signed strict-cross expression, not a reassignment of the accepted same-group package. |
| Exact prime-power depth | **Pass only algebraically.**  The (E_r,L_r) filtration includes the unit mask and gives exact frequency supports.  **Fail** for any numerator-only or congruence-only analytic classification. |
| Bad primes / nonunit (K) | **Routed, not estimated.**  Nonunit (K) lowers phase conductor and the mask can set the remaining conductor.  Empty masks are zero.  These cases remain exact in the filtration and in the coarse physical count. |
| Full (2)-part | **First layer proved; deeper estimate open.**  Nonempty iff (A,B_2,V) are even; then the domain is odd (x) and the reciprocal weight has period (q/2).  Otherwise the trace is zero.  The exact filtration covers all deeper layers without claiming cancellation. |
| Pole collisions / root count | **Pass for (p\ge11).**  Collisions leave at least (p-4>5) allowed residues.  The derivative numerator has degree at most five.  Small primes are explicitly exceptional. |
| Good-prime depth / Vandermonde / graph degree | **Pass at restricted scope.**  For an actual reciprocal-mask period, \(p^a\mid N\) follows by six-point Vandermonde and induction over \(p^a\).  The congruence \(B_2\equiv A\pmod{\mathfrak a}\) gives both in- and out-degree at most \(M^2/\mathfrak a\).  Maximal depth labels are unique; coarse edges are removed first.  Affine periods and bad primes are excluded. |
| Tensor orthogonality | **No analytic gain certified.**  CRT and local Fourier support are exact, but only select compatible valuations. |
| Actual symbol before absolute values | **Pass in the coarse proof; open in the residual.**  Physical-row counting keeps the actual rows intact.  No coefficientwise trace bound is promoted as a substitute for \(\widehat\Omega\). |
| Negative and modulus-multiple differences | **Pass.**  (K_D^\circ) retains every (0<|u|<D), including negative (u) and (u=jM).  Since (D\gg M), modulus multiples cannot be declared absent. |
| Ramanujan centering | **Pass.**  In the physical off-diagonal expansion the omitted (x=y) sum is exactly (c_M(d)).  Squaring already contains the four-Kloosterman term, the two cross terms, and \(|c_M(d)|^2\) once.  Nothing is appended or dropped. |
| Perfect powers / integer phases | **Pass only for the certified count.**  That proof assumes no nonresonance and remains valid for perfect-power moduli and constant phases.  Generic source bounds requiring nondegeneracy cannot absorb these cases. |
| Support and prior errors | **Pass.**  The proof acts after the exact signed deep projection.  Zero extension forces both shifted coefficients into the deep band.  The literal zero, short offsets, collar, entry/exit, stationary errors, wrong signs, transitions, axes, and tails remain with their prior owners. |
| Complete-transform self-return | **Fail as a proposed saving.**  Completion followed only by orthogonality/inversion returns to the physical norm.  A new estimate on the actual symbol is necessary. |
| Target arithmetic | **Pass for the stated subaggregates.**  The coarse ratio is \(R^2B^4J^{-11/15}\), yielding \(R\le J^{11/30}B^{-2}\), uniformly \(R\le J^{1/15}\).  The good-depth ratio is \((M^2/\mathfrak a)B^4J^{-11/15}\), yielding \(\mathfrak a\ge M^2/\rho_*^2\). |

The only computation used was a bounded small-prime search to locate candidate exceptions.  Every example and every promoted statement above was then proved symbolically; the computation is not certification.

## 6. Dependencies, exact artifacts, and primary sources used

**Repository artifacts read completely.**  No sibling Round-88 report was read.

- `protocol.md`.
- `state/proof_obligations.yml` (graph hash in the brief: `e2346245d09d22ba66e17037ad57e85cf56808d9ca70526657f78d94e52809be`).
- `state/active_campaign.yml`.
- `rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/derivation_packet.md`.
- `rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/synthesis.md`.
- `rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reports/exceptional_trace_hostile_source_audit.md`.
- `rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reviews/conductor_round87_crt_fejer.md`.
- `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reports/four_kloosterman_hostile_source_audit.md`.

**Current primary-literature audit (searched through 2026-08-17).**

| Primary source and exact result | Hypotheses actually supplied | Hypothesis map to Round 88 |
|---|---|---|
| T. Cochrane and A. Granville, [*Mixed character sums modulo prime powers*, arXiv:2604.02614v1](https://arxiv.org/html/2604.02614v1), Theorems 1.1, 3.1, 5.1 and 20.1 | One rational mixed character sum modulo (p^m).  Theorem 1.1 assumes their nondegeneracy; Theorem 3.1 explicitly lowers a degenerate sum to modulus (p^{m-\ell}), with the constant-on-domain case allowing no nontrivial estimate.  Theorem 5.1 splits odd-(p) sums into residue disks, kills noncritical disks, and bounds critical disks according to multiplicity; Theorem 20.1 is the separate (2)-adic version. | This is the closest literal source for mask-aware critical disks and conductor loss.  It confirms that degenerate/constant branches must be routed rather than assigned generic square-root cancellation.  It is pointwise at one prime power.  It does not provide the CRT-weighted (v,h_1,h_2,b) operator estimate, the actual \(\widehat\Omega\), or the frozen (Q)-gain.  A principal-character encoding of the four-unit domain must keep all four factors; reducing only the exponential numerator changes the domain. |
| É. Fouvry, E. Kowalski and P. Michel, [*A study in sums of products*, arXiv:1405.2293v2](https://arxiv.org/html/1405.2293v2), Theorem 1.5 and Corollaries 1.6–1.7 | A bounded-conductor bountiful sheaf over the prime field; square-root cancellation is conditional on normal/(r)-normal tuples or a nonzero additive twist, with special-involution and monodromy qualifications. | Applies to good prime-field trace functions after all geometric hypotheses are verified.  It does not cover (p^\nu) for \(\nu>1\), composite (M), the (2)-part, nonunit (K), varying bad primes, or the actual physical symbol.  It cannot be imported merely because four Kloosterman-like factors appear. |
| D. Milićević and S. Zhang, [*Distribution of Kloosterman paths to high prime power moduli*, arXiv:2005.08865v1](https://arxiv.org/html/2005.08865v1), Theorem 4 | A fixed high prime-power setting, a translation-invariant (p)-adic domain, and a phase that is a bounded linear combination of chosen square-root branches.  It gives power cancellation or a deep congruence collision between shifts. | Methodologically validates a collision/aperiodic dichotomy and shows why deep shift coincidences must be separated.  The phase family and domain are not (88.10), and the theorem does not treat arbitrary composite (M), the full (2)-part, varying (b), or \(\widehat\Omega\).  It cannot bound the residual here without a new reduction theorem. |
| X. Zheng, [*Primes in simultaneous arithmetic progressions*, arXiv:2512.22798v1](https://arxiv.org/html/2512.22798v1), Lemmas 2.7, 2.8 and 2.10 | Lemma 2.7 is a prime-modulus product estimate with the paired zero-twist exception.  Lemma 2.8 treats a special four-Kloosterman parallelogram for squarefree (q), with explicit gcd losses.  Lemma 2.10 treats a general rational phase only when every prime exponent in (q) is at most two. | These are exact warnings against suppressing paired and gcd branches.  The full prime powers of Round 88, arbitrary four-unit mask, variable (K), and actual \(\widehat\Omega\) fall outside the hypotheses. |
| J. Wu and P. Xi, [*Arithmetic exponent pairs for algebraic trace functions and applications*, arXiv:1603.07060v5](https://arxiv.org/html/1603.07060v5), Theorem A.1 | A single complete rational exponential sum modulo (c), with explicit numerator, derivative, and denominator gcd factors.  Prime powers (p^\beta\Vert c) with \(\beta\ge3\) enter through the factor \(\Xi(c)^{1/2}\), originating from a trivial estimate for that high-power part. | This theorem is not a uniform square-root estimate at full prime-power depth.  It is useful only after the exact degeneracy factors are controlled, and supplies neither the fourfold actual-symbol correlation nor a (b)-average. |
| V. Blomer and A. Pascadi, [*Bilinear forms with Kloosterman sums via quadratic characters*, arXiv:2607.24311v1](https://arxiv.org/html/2607.24311v1), Theorem 1.1 | One fixed modulus (c), two arbitrary coefficient sequences on intervals of length at most (N\le c), and the single kernel (S(am,n;c)), with the displayed coprimality condition except for initial intervals.  The (c^{-1/32}) saving is in the critical (N=\sqrt c) range. | This is a strong current all-modulus bilinear theorem, but its operator is not the centered fourfold trace (88.10), its two free coefficient sequences are not the coupled \(d,n,m,v,h_1,h_2\) symbol, and it does not average the varying (M\in\{4b,2b,b\}).  No literal specialization was found. |

A targeted search also inspected recent arbitrary-modulus Kloosterman bilinear work, including A. Pascadi, [arXiv:2511.08445v2](https://arxiv.org/html/2511.08445v2), and D. Milićević, X. Qin and X. Wu, [arXiv:2511.07550v1](https://arxiv.org/html/2511.07550v1).  Their objects are fixed-modulus bilinear forms with a single Kloosterman kernel and separated coefficient sequences.  No current primary theorem located in this search simultaneously supplies arbitrary full prime powers (including (2)), the four-unit rational phase, all degeneracies, the varying-(b) sum, and the actual Round-88 symbol.  This is a hypothesis audit, not a claim that no future reformulation is possible.

## 7. Recommended state effect

**Revise** the Round-88 period-depth route; do not promote the full target (88.9).

- **Promote, at the smallest literal scope,** the exact masked projections (E_r,L_r), their local Fourier supports, and the CRT factorization as algebraic routing identities only.
- **Promote** the congruence-aligned coarse-depth estimate
  \[
  |\mathcal G^{(m)}_{\rm align}(D)|
  \ll_\varepsilon X^\varepsilon DB^3R^2T^4Q^{-5/6}
  \]
  for \(m\mid M\), \(R=M/m\), including coarse empty-active labels and without a coprimality condition.  Record the target-safe range \(R\le J^{11/30}B^{-2}\), hence uniformly \(R\le J^{1/15}\).
- **Promote, after applying that coarse deletion first,** the good-prime directed-edge estimate (5) for the unique maximal reciprocal-mask period-depth vector.  Its target-safe scope is exactly
  \[
     \mathfrak a\ge M^2/\rho_*^2,\qquad
     \rho_*=J^{11/30}B^{-2}.
  \]
  Do not extend it to affine/full-phase periods, nonunit \(K\), \(p\le7\), \(p=2\), or projection-only depth.
- **Promote as hostile controls** the exact (q=3^\nu) trace of size (q^2/3), the (p=3,5) mask-created periods, the affine-period example, and the automatic nonempty (2)-adic (q/2)-period.  These reject coefficientwise square-root and numerator-only depth claims.
- **Reject** the statement that divisor-lattice Möbius inversion captures every functional period-depth shell.  Retain it only for nested coarse-congruence shells.
- **Retain open** the residual strict cross-group, (u\ne0) actual-symbol estimate, including accidental small-prime periods, nonunit-(K) branches, deeper (2)-adic layers, affine frequency cancellation, small-\(\mathfrak a\) good depth, projection-only depth, and genuinely aperiodic traces.
- Make **no change** to the accepted Round-87 same-group package, the once-owned global (u=0) diagonal, or any separately owned support/error stratum.  No shared proof-state file was edited by this audit.
