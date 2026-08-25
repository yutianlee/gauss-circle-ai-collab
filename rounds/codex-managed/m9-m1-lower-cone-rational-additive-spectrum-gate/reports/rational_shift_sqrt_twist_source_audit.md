# Round 142 source audit: rationally shifted square-root branches

Task: rational_shift_sqrt_twist_source_audit
Status: candidate evidence only; no shared proof-state edit
Notation: \(e(t)=e^{2\pi i t}\), and \(\chi _4\) is the primitive odd character modulo \(4\).

## 1. Result

**Result: rational-major-arc self-return no-go.** Let

\[
C(m)=\sum_{\substack{hr=m\\ r\ {\rm odd}\\r>4h}}\chi _4(r).
\]

For every reduced \(a/q\) and every real \(T\ge 2\), the exact cone has the uniform rational mean

\[
\sum_{m\le T}C(m)e(am/q)
=\gamma(a,q)T+O\!\left((T^{1/2}+q)\log(2q)\right),
\qquad
\gamma(a,q)=
\begin{cases}
\displaystyle {i\pi\over 2q}\chi _4(a),&4\mid q,\\[4pt]
0,&4\nmid q.
\end{cases}                                                    \tag{1.1}
\]

The strict lower endpoint \(r>4h\), the upper endpoint \(r\le T/h\), and the odd-\(r\) convention are all included in (1.1). In particular, \(a/q=1/4\) gives \(i\pi T/8+O(T^{1/2})\), but every reduced denominator divisible by \(4\) has a main mode.

This is a genuinely growing-denominator theorem. The main term in (1.1) has size \(T/q\), and it dominates the proved error whenever

\[
q\log(2q)=o(T^{1/2}).                                             \tag{1.2}
\]

The exact cone on \(m\asymp M\), however, has a pointwise finite additive expansion with denominators \(q=4h\asymp 1,\ldots,\sqrt M\). A direct second-derivative estimate, uniform in the fractional linear shift, gives the rigorous coefficient-free branch bound

\[
\ll_W\min\!\left\{M^{1/4},RM^{-1/2}+R^{-1}\right\},
\qquad N\asymp R^4,                                               \tag{1.3}
\]

and the coefficient \(\ell ^1\)-mass is \(\asymp1\) per denominator. Branchwise modulus assembly over \(q\ll\sqrt M\), before the separate moving-boundary owner is restored, therefore has only the owner-sized ledger

\[
\ll_W\min\!\left\{M^{3/4},R+{\sqrt M\over R}\right\}.             \tag{1.4}
\]

This is \(O(R)\), not \(O(X^\epsilon)\), on the hard dyadic range. For the natural local-slope cutoff

\[
L_M\asymp {M^{3/4}\over R},\qquad Q_M=\lceil L_M\rceil,
\]

the extracted periodic branches still have capacity as large as \(R^{1/2+o(1)}\) at \(M\asymp R^2\).

At the stationary-principal level, aggregating the numerators and applying the matching saddle algebra a second time reproduces the same \(\chi _4(j)(hj)^{-3/4}e(\sqrt{Nhj})\) cone, with the phases \(e(-1/8)\) and \(e(+1/8)\) cancelling. This is principal-symbol self-return only: no branchwise first- or second-stage uniform remainder, hard endpoint, or Fresnel transition is proved here. The inherited Round-140 ledger applies after the reciprocal family is reassembled, not to each artificially separated rational branch. The primary-source divisor and twisted-Estermann formulae audited below either have a complete divisor coefficient, exclude the boundary parameter needed here, smooth the denominator sum in an \(m\)-dependent way, or combine the two complex directions. None supplies cancellation in the full \(q\)-sum at the fixed Round-142 centre.

Thus the first obstruction is **not** denominator uniformity in (1.1). At source-method level, no cited theorem proves a uniform \(C_c^\infty\) branchwise Poisson/stationary remainder, and this report makes no such claim. At mechanism level, the first gap is the missing convergent conic reconstruction and short-interval residual theorem needed on the local slope cells. The unregularized limiting coefficients have divergent absolute and square mass; the canonical denominator-Abel reconstruction is the complete radial coefficient \(\sigma_{\chi _4}=r_2/4\), not \(C\); and every finite cutoff retains all larger rational modes. The exact finite Fourier identity bypasses limiting reconstruction but meets the next obstructions: the moving cone boundary, owner-sized denominator accumulation, and principal-symbol self-return. This is a route obstruction, not a lower bound for the signed scalar and not evidence that the target estimate is false.

## 2. Exact statement and hypotheses

The source audit uses \(R=X^{1/4}\), \(N=\lfloor X\rfloor\asymp R^4\), and dyadic \(m\asymp M\ll N/R^2\asymp R^2\).

**Exact cone spectrum and exact finite expansion.** Formula (1.1) holds for a reduced fraction \(a/q\), \(q\ge1\), and \(T\ge2\). Abel summation gives the weighted consequence

\[
\sum_{m\le T}m^{-3/4}C(m)e(am/q)
=\mathbf1_{4\mid q}{2i\pi\chi _4(a)\over q}T^{1/4}
+O\!\left(q\log(2q)+1\right).                                   \tag{2.0}
\]

Independently of any limiting spectrum, for every positive integer \(m\),

\[
\begin{aligned}
C(m)
&=\sum_{\substack{h\ge1\\4h^2<m}}
 {1\over 2ih}\sum_{b\bmod 4h}\chi _4(b)e\!\left({bm\over4h}\right)\\
&=\sum_{\substack{q\equiv0\ (4)\\q^2/4<m}}
 {2i\over q}\sum_{a\bmod q}\chi _4(a)e(-am/q).                    \tag{2.1}
\end{aligned}
\]

The first line includes all residues, with even residues killed by \(\chi _4\); the second is obtained by \(a=-b\). Fractions in (2.1) are not required to be reduced, and the cutoff \(q^2/4<m\) depends on \(m\). Hence (2.1) is an exact finite reconstruction, but it is not a fixed periodic projection obtained from the reduced means (1.1). On \(m\in[M,2M)\), denominators extend to \(q<2\sqrt{2M}\); only \(q<2\sqrt M\) lies wholly inside the strict cone throughout the block.

**Coefficient-free stationary principal family and rigorous branch bound.** Let \(W\in C_c^\infty((1,2))\), \(0\le a<q\), and

\[
\mathcal S_{a,q}(M)
=\sum_{m\ge1}m^{-3/4}W(m/M)e\!\left(\sqrt{Nm}-{am\over q}\right).
\]

For \(\lambda=k+a/q>0\), the saddle algebra defines the stationary principal family

\[
\mathcal P^{\rm stat}_{a,q}(M)
:=2e(-1/8)N^{-1/4}
\sum_{\substack{k\in\mathbb Z\\\lambda=k+a/q>0}}
W\!\left({N\over4M\lambda^2}\right)
e\!\left({N\over4\lambda}\right).                                \tag{2.2}
\]

Writing

\[
\mathcal S_{a,q}(M)=\mathcal P^{\rm stat}_{a,q}(M)
+\mathcal E^{\rm br}_{a,q}(W;N,M)
\]

only names the branchwise remainder owner; this report proves no uniform bound for \(\mathcal E^{\rm br}_{a,q}\). In particular, the cited Jutila theorem has a holomorphic-amplitude hypothesis and does not apply to an arbitrary nonzero \(C_c^\infty\) weight. A hard endpoint at \(m=q^2/4\), its Fresnel transition, nonstationary aliases, and stationary remainders remain outside (2.2). The inherited Round-140 ledger controls them only after the complete reciprocal family is reassembled.

The stationary lattice has length

\[
K_M\asymp \sqrt{N/M}\asymp {R^2\over\sqrt M}.                    \tag{2.3}
\]

Separately, the classical real-variable second-derivative estimate and partial summation give the rigorous uniform bound

\[
|\mathcal S_{a,q}(M)|
\ll_W\min\!\left\{M^{1/4},RM^{-1/2}+R^{-1}\right\}.              \tag{2.4}
\]

This estimate does not identify a transformed main term. The principal family (2.2) preserves the target direction algebraically: negative curvature gives \(e(-1/8)\) and reciprocal phase \(e(N/(4\lambda))\). The conjugate initial branch has positive curvature, \(e(+1/8)\), and the conjugate reciprocal phase; a cosine formula controls only their prescribed real combination.

**Primary-source theorem cards.**

| Primary result | Exact hypotheses and coefficient class | Smoothing, denominator range, and complex direction | Applicability |
|---|---|---|---|
| M. Jutila, *Lectures on a Method in the Theory of Exponential Sums*, [Theorem 2.1, printed p. 50/PDF p. 58](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr80.pdf), and the [negative-curvature remark, printed p. 59/PDF p. 67](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr80.pdf) | Conditions (i)–(v) require \(f\) real on the interval and both \(f\) and \(g\) holomorphic in the stated complex tube with scale \(\mu\), together with \(|g|\ll G\), \(|f'|\ll F/\mu\), positive curvature \(f''\gg F/\mu^2\), and the scale regularity. The later remark replaces \(+1/8\) by \(-1/8\) and \(f''\) by \(|f''|\) for negative curvature. | Theorem 2.2 takes \(U>0\), a fixed nonnegative integer \(J\), and \(JU<(b-a)/2\); adds (vi), \(F(x)\gg1\); and assumes (2.1.10), \(U\gg\delta(x_0)\mu(x_0)F(x_0)^{-1/2}\), where \(\delta\) detects the two \(JU\)-endpoint strips. Its factor \(\xi_J(x_0)\) and error terms depend on whether the saddle lies in an endpoint strip. No \(q\)-saving is asserted. | Confirms the local saddle normalization under its holomorphic-amplitude hypotheses. It does **not** cover arbitrary nonzero \(W\in C_c^\infty((1,2))\) and does not prove a uniform remainder for (2.2). |
| Jutila, [Theorem 1.1, printed p. 22/PDF p. 30, equations (1.5.2)–(1.5.4)](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr80.pdf) | For reduced \(h/k\), \(x\ge1\), \(k\le x\), and \(1\le N_d\ll x\), the complete sharp divisor sum (with its primed endpoint) has, after its main term, a truncation proportional to \(\sum_{n\le N_d}d(n)e_k(-n\bar h)n^{-3/4}\cos(4\pi\sqrt{nx}/k-\pi/4)\), with error \(O(kx^{1/2+\epsilon}N_d^{-1/2})\). | Sharp endpoint; complete \(d(n)\); explicit positive power of \(k\); cosine rather than one independently bounded complex direction. | Wrong coefficient and direction for \(C(m)\); it is not a full-\(q\) estimate for (2.1). |
| I. Kaneko, *Mixed Moments of the Riemann Zeta and Dirichlet \(L\)-Functions*, [Theorem 3.1](https://arxiv.org/pdf/2109.12495) | \(\psi\) is primitive modulo \(q_0\), \(h,\ell,q_0\ge1\), and \((h,\ell q_0)=1\). Initially in its absolute-convergence half-plane, \(D_\psi(s,\xi;h/\ell q_0)=\sum_{n\ge1}\sigma_\xi(n,\psi)e_{\ell q_0}(hn)n^{-s}\), with \(\sigma_\xi(n,\psi)=\sum_{d\mid n}\psi(d)d^\xi\), continues meromorphically and satisfies the displayed functional equation. | Exact Dirichlet-series identity for every \(\ell\), with conductor factor \((\ell q_0)^{\xi-2s+1}\), gamma factors, and both dual twists \(\pm\bar h/(\ell q_0)\). It is not a denominator-uniform estimate. | At \(\psi=\chi _4\), denominators are \(4\ell\), but the coefficient is the complete \(\sigma_\xi\), not the cone \(C\), and both directions occur. |
| Kaneko, [Lemma 3.2, equation (3.4)](https://arxiv.org/pdf/2109.12495) | For a character \(\psi\bmod q_0\), \(n\ge1\), and strictly \(\Re\xi>0\), \(\sigma_\xi(n,\psi)n^{-\xi}\) equals \(\frac{L(1+\xi,\psi)}{\tau(\psi)}\sum_{\ell\ge1}\ell^{-1-\xi}\sum_{h\bmod\ell q_0}^{*}\psi(h)e_{\ell q_0}(hn)\). | Infinite reduced Ramanujan expansion over every \(\ell\); no cutoff; absolute damping \(\ell^{-1-\Re\xi}\); one displayed additive direction. | For \(\psi=\chi _4\), the formal value at \(\xi=0\) is \(L(1,\chi _4)/\tau(\chi _4)=\pi/(8i)\), giving the same signed \(1/q\) coefficients as (1.1) after reversing frequency. But \(\xi=0\) is excluded, and the left coefficient is complete. |
| Kaneko, [Lemma 3.3](https://arxiv.org/pdf/2109.12495) | \(G\) is fixed, even, entire, rapidly decreasing in vertical strips, and \(G(0)=1\); the identity is valid for \(\xi\in\mathbb C\) with its stated weights \(f_{\pm\xi}\). | Exact two-piece, \(n\)-dependent smoothed expansion over \(\ell\) and reduced residues modulo \(\ell q_0\). Both \(\pm\xi\) pieces are retained. | Reaches \(\xi=0\) only through an \(n\)-dependent two-branch smoothing of complete \(\sigma_0\); it is not a finite periodic projection of \(C\) with a controlled residual. |
| D. Banerjee and K. Khurana, *Character Analogues of Cohen-Type Identities and Related Voronoi Summation Formulas*, [Theorems 4.3–4.4, p. 11](https://arxiv.org/pdf/2306.12399) | Odd primitive \(\chi\bmod q_0\), strict \(0<\Re\nu<1/2\), nonintegral \(0<\alpha<\beta\), and a test function analytic inside a closed contour strictly containing \([\alpha,\beta]\); the coefficient is the complete generalized divisor function \(\sigma_{-\nu,\chi}\). | Bessel/Voronoï identity with its explicit endpoint convention; \(q_0\) is the character conductor, not a proved growing-denominator saving. | The needed boundary \(\nu=0\) is outside the theorem, the coefficient is complete, and the analytic test/endpoints do not match the exact cone without additional work. |

The Round-141 cards for Robert–Sargos, Sargos–Wu, Tao–Trudgian–Yang, Popov/Li–Yang, and Kaczorowski–Perelli remain inherited no-go evidence: respectively they retain positive powers of \(R\), require separated coefficients, work only rowwise, control a complete real cosine combination, or lack the required growing-parameter uniformity. No claim below upgrades those source results.

## 3. Proof or derivation

**The rational mean, including endpoints and the sharp growing-\(q\) error.** Define

\[
H_T=\left\lfloor{\sqrt{1+16T}-1\over8}\right\rfloor,\qquad
K_h(T)=\left\lfloor{T/h-4h+1\over2}\right\rfloor.
\]

The first admissible odd integer in the \(h\)-row is \(4h+1\), so unfolding without changing either endpoint gives the exact finite identity

\[
\sum_{m\le T}C(m)e(am/q)
=\sum_{h=1}^{H_T}
e\!\left({ah(4h+1)\over q}\right)
G(K_h(T),z_h),                                                    \tag{3.1}
\]

where

\[
z_h=-e(2ah/q),\qquad G(K,z)=\sum_{n=0}^{K-1}z^n.                 \tag{3.2}
\]

A row is constant exactly when

\[
z_h=1
\quad\Longleftrightarrow\quad
q=4d,\quad h=d\ell,\quad \ell\ {\rm odd}.                        \tag{3.3}
\]

Indeed, \(z_h=1\) is equivalent to \(4ah/q\) being an odd integer. Since \((a,q)=1\), this is impossible unless \(4\mid q\), and for \(q=4d\) it is equivalent to \(h=d\ell\) with \(\ell\) odd. On such a row every summand equals

\[
e\!\left({ah(4h+1)\over q}\right)
=e(a\ell/4)=i\chi _4(a)\chi _4(\ell).
\]

Writing \(L=\lfloor H_T/d\rfloor\), the constant rows contribute

\[
\begin{aligned}
i\chi _4(a)\sum_{\substack{\ell\le L\\\ell\ {\rm odd}}}
\chi _4(\ell)K_{d\ell}(T)
&={i\chi _4(a)T\over2d}
\sum_{\ell\le L}{\chi _4(\ell)\over\ell}+O(T^{1/2})\\
&={i\pi\chi _4(a)\over2q}T+O(T^{1/2}).                           \tag{3.4}
\end{aligned}
\]

Here \(K_{d\ell}(T)=T/(2d\ell)-2d\ell+O(1)\),
\(\sum_{\ell\le L}\chi _4(\ell)/\ell=\pi/4+O(L^{-1})\), and
\(\sum_{\ell\le L}\chi _4(\ell)\ell=O(L)\). If \(d>H_T\), there is no constant row, but the prospective main term is \(O(T/d)=O(T^{1/2})\), so the same formula remains valid.

It remains to sum all nonconstant rows without bounding each row by \(O(q)\). Put \(P=q/(q,2)\). The sequence \(z_h\) has period \(P\), and in one period it is a permutation of the \(P\)-th roots of unity or their half-step translate. Excluding \(z=1\),

\[
|G(K,z)|\le {2\over|1-z|},\qquad
\sum_{\substack{z\ {\rm in\ one\ period}\\z\ne1}}
{1\over|1-z|}\ll P\log(2P).
\]

Splitting \(1\le h\le H_T\) into complete \(P\)-periods and one remainder yields

\[
\sum_{\substack{h\le H_T\\z_h\ne1}}|G(K_h(T),z_h)|
\ll (H_T+P)\log(2P)
\ll (T^{1/2}+q)\log(2q).                                        \tag{3.5}
\]

Equations (3.4)–(3.5) prove the sharp form (1.1). For fixed \(q\) the error is \(O_q(T^{1/2})\); for varying \(q\), the main term is asymptotic in the dominance range (1.2). When \(4\nmid q\), every row is nonconstant and (3.5) is the asserted zero-main-term estimate. The former \(O(qT^{1/2})\) estimate is only the weaker result obtained by completing each row separately.

**Exact pointwise Fourier identity and convergence ledger.** Put

\[
F_h(m)=\mathbf 1_{h\mid m}\chi _4(m/h).
\]

Breaking a complete residue sum modulo \(4h\) first modulo \(4\) and then modulo \(h\) gives

\[
\sum_{b\bmod4h}\chi _4(b)e(bm/(4h))
=
\begin{cases}
2ih\,\chi _4(m/h),&h\mid m,\\
0,&h\nmid m.
\end{cases}                                                       \tag{3.6}
\]

Thus \(F_h(m)=(2ih)^{-1}\sum_b\chi _4(b)e(bm/(4h))\), proving (2.1) after imposing \(4h^2<m\). At fixed \(q=4h\), exactly \(q/2\) residues have nonzero character and each coefficient in the second line of (2.1) has modulus \(2/q\). Hence the exact \(\ell^1\)-mass is \(1\) per denominator and \(\asymp Q\) through \(q\le Q\).

The reduced mean coefficients have the same obstruction:

\[
\sum_{\substack{a\bmod q\\(a,q)=1}}|\gamma(a,q)|
={\pi\phi(q)\over2q}\asymp1
\quad\text{on average},\qquad
\sum_{\substack{q\le Q\\4\mid q}}\sum_{a\bmod q}^{*}|\gamma(a,q)|^2
\asymp\log Q.                                                     \tag{3.7}
\]

Consequently the formal series made only from the means is neither absolutely summable nor square summable in the naive denominator ordering. This is not merely a missing convergence argument. For \(\eta>0\), the canonical denominator-Abel ordering is

\[
B_\eta(m)=-{i\pi\over8}
\sum_{d\ge1}{1\over d^{1+\eta}}
\sum_{\substack{c\bmod4d\\(c,4d)=1}}
\chi _4(c)e(cm/(4d)).
\]

Möbius inversion of the unit condition and the primitive modulo-four Gauss sum give the exact identity

\[
B_\eta(m)
={\pi\over4L(1+\eta,\chi _4)}
\sum_{\ell\mid m}\chi _4(m/\ell)\ell^{-\eta}
\longrightarrow
\sigma_{\chi _4}(m)={r_2(m)\over4}                               \tag{3.7a}
\]

as \(\eta\downarrow0\). Thus the natural convergent reconstruction of all limiting rational modes is the complete radial coefficient, not the conic coefficient \(C\). Its residual is \(C-\sigma_{\chi _4}\); on \(m=2^\nu n\) with \(n\) odd and \(\chi _4(n)=-1\), one has \(\sigma_{\chi _4}(m)=0\), so this residual equals \(C(m)\).

A finite denominator projection is equally nonterminal. Define

\[
B_Q(m)=-{i\pi\over2}
\sum_{\substack{s\le Q\\4\mid s}}{1\over s}
\sum_{c\bmod s}^{*}\chi _4(c)e(cm/s),\qquad D_Q=C-B_Q.
\]

Distinct-rational spacing and the sharp theorem (1.1) give, for reduced \(a/q\),

\[
\sum_{m\le T}D_Q(m)e(am/q)
=\mathbf1_{\{4\mid q,\ q>Q\}}\gamma(a,q)T
+O\!\left((T^{1/2}+q)\log(2q)+qQ^2\right).                       \tag{3.7b}
\]

Every finite cutoff therefore retains the same linear main modes at all larger denominators. Kaneko's Lemma 3.2 supplies convergence only after the strict factor \(\ell^{-\Re\xi}\) and reconstructs the complete \(\sigma_\xi\), consistently with (3.7a). Formula (2.1) is pointwise finite, but its \(m\)-dependent cutoff and nonreduced residues are precisely the conic structure lost by replacing it with a fixed periodic projection.

**Stationary principal algebra and the rigorous \(R/q\) capacity.** For \(\lambda=k+a/q>0\), the principal saddle in (2.2) is

\[
x_\lambda={N\over4\lambda^2},\qquad
\sqrt{Nx_\lambda}-\lambda x_\lambda={N\over4\lambda},\qquad
x_\lambda^{-3/4}|f''(x_\lambda)|^{-1/2}=2N^{-1/4}.                \tag{3.8}
\]

This proves the phase, direction, and amplitude of the principal symbol, not a uniform asymptotic for \(\mathcal S_{a,q}\). The dual length is (2.3), so the absolute principal-family capacity is \(N^{-1/4}K_M\asymp R/\sqrt M\). Separately, on \(x\asymp M\),

\[
\left|{d^2\over dx^2}\left(\sqrt{Nx}-{ax\over q}\right)\right|
\asymp {R^2\over M^{3/2}}.
\]

The second-derivative estimate gives an unweighted bound
\(O_W(RM^{1/4}+M^{3/4}/R)\); partial summation against \(m^{-3/4}W(m/M)\), together with the trivial estimate, proves (2.4). This is the rigorous branch bound used in (1.3)–(1.4).

For the exact finite expansion, take \(q=4h\) and stay away from the moving endpoint \(m=q^2/4\). Summing only the principal families (2.2) over the nonzero residues with the coefficient from (2.1), and writing \(r=qk+a\), gives the algebraic identity

\[
{2i\over q}\sum_{a\bmod q}\chi _4(a)\mathcal P^{\rm stat}_{a,q}(M)
= {4i\,e(-1/8)N^{-1/4}\over q}
\sum_{r>0}\chi _4(r)
W\!\left({Nq^2\over4Mr^2}\right)
e\!\left({Nq\over4r}\right).                                    \tag{3.9}
\]

The \(r\)-sum has length

\[
L_{q,M}\asymp {q\sqrt N\over\sqrt M}
\asymp {qR^2\over\sqrt M}.                                      \tag{3.10}
\]

The prefactor is \(N^{-1/4}/q\asymp1/(Rq)\), so (3.10) gives principal capacity \(R/\sqrt M\) at each \(q\): the explicit \(q^{-1}\) is cancelled by dual length. There are \(\asymp\sqrt M\) possible denominators. This is a principal-symbol capacity ledger only. Formula (1.4) instead follows rigorously by applying (2.4) branchwise to a smooth fixed-height truncation; the moving-boundary wedge remains a separate owner.

If instead one inserts the reduced mean coefficients, the fixed-\(q\) principal aggregate is

\[
\sum_{a\bmod q}^{*}\gamma(a,q)\mathcal P^{\rm stat}_{a,q}(M)
= {i\pi e(-1/8)N^{-1/4}\over q}
\sum_{\substack{r>0\\(r,q)=1}}\chi _4(r)
W\!\left({Nq^2\over4Mr^2}\right)
e\!\left({Nq\over4r}\right).                                    \tag{3.11}
\]

The coprimality is the only structural change in the principal algebra; the \(q\)-power ledger is identical. Thus neither exact nor reduced principal aggregation displays a \(q^{-1}\) saving after dual length is counted. No claim about the aggregated branchwise errors is made.

The hard nonresonant mask is also not made harmless by treating branches separately. A coefficient-free branch pays \(O(X^\epsilon)\) for the accepted near-radical count, but this cost accumulates with the rational coefficient mass; moreover, the accepted bound for the original \(C\)-weighted scalar cannot be assigned separately to every periodic projection and the moving-boundary wedge. More fundamentally, with

\[
\vartheta(m)={\sqrt N\over2\sqrt m},\qquad
\vartheta'(m)=-{\sqrt N\over4m^{3/2}},                            \tag{3.12}
\]

a derivative arc of radius \(\Delta\) around an integer lift \(k+a/q\) has \(m\)-width

\[
\asymp {\Delta M^{3/2}\over\sqrt N}.                             \tag{3.13}
\]

The natural curvature-cell length and Farey order are

\[
L_M=|\vartheta'(M)|^{-1/2}\asymp {M^{3/4}\over R},
\qquad Q_M=\lceil L_M\rceil.                                    \tag{3.13a}
\]

For \(L_M\ge1\), a reduced approximant \(a/q\), \(q\le Q_M\), can be assigned its half-open Farey cell between the two neighboring mediants. If the neighbors are \(a_\pm/q_\pm\), the exact left and right widths are

\[
{1\over q(q+q_-)},\qquad {1\over q(q+q_+)}.
\]

The unthickened cells have multiplicity one. Thickening by the unavoidable slope variation \(O(1/L_M)\) on a curvature interval gives overlap \(O(Q_M)=O(L_M)\). The slope crosses \(\asymp K_M=R^2/\sqrt M\) integer translates, and the number of physical curvature intervals is

\[
J_M\asymp {M\over L_M}\asymp RM^{1/4}.                           \tag{3.13b}
\]

When \(M<R^{4/3}\), \(L_M<1\) and there is no nontrivial within-integer linearization cell. The condition \(|j_m|>\sqrt M\) controls the phase value \(\sqrt{Nm}\) relative to its nearest integer; it gives no implication excluding any derivative arc above.

Most importantly, (1.1) is a prefix theorem, not the local residual theorem required after subtracting \(B_{Q_M}\). Absolute assembly over the \(J_M\) cells would require a bound of the shape

\[
\max_{\substack{q\le Q_M,\ (a,q)=1\\
J\subset[M,2M),\ |J|\le L_M}}
\left|\sum_{m\in J}D_{Q_M}(m)e(am/q)\right|
\ll_\epsilon X^\epsilon{\sqrt M\over R},                         \tag{3.13c}
\]

stable under the moving cone boundary. The available prefix error \((\sqrt M+q)\log(2q)\) does not imply (3.13c). None of the audited source identities supplies this conic short-interval residual theorem.

**Second stationary principal-symbol algebra.** Put \(q=4h\) in the principal expression (3.9). It becomes

\[
{i\,e(-1/8)N^{-1/4}\over h}
\sum_{r>0}\chi _4(r)
W\!\left({4Nh^2\over Mr^2}\right)e(Nh/r).                        \tag{3.14}
\]

Use the character Fourier identity

\[
\chi _4(r)={e(r/4)-e(3r/4)\over2i}.
\]

In the \(\sigma\in\{1,3\}\) component, Poisson frequency \(k\) has phase

\[
{Nh\over r}+\left({\sigma\over4}-k\right)r,
\qquad j=\sigma-4k>0.
\]

Its saddle and Hessian are

\[
r_{h,j}=2\sqrt{Nh/j},\qquad
\Phi(r_{h,j})=\sqrt{Nhj},\qquad
|\Phi''(r_{h,j})|^{-1/2}=2(Nh)^{1/4}j^{-3/4}.                    \tag{3.15}
\]

Positive curvature contributes \(e(+1/8)\), cancelling the \(e(-1/8)\) in (3.14), and

\[
W\!\left({4Nh^2\over Mr_{h,j}^2}\right)=W(hj/M).
\]

The two residue classes have signs \(+\) for \(j\equiv1\pmod4\) and \(-\) for \(j\equiv3\pmod4\). Multiplying the principal amplitudes in (3.14)–(3.15) therefore produces

\[
\sum_{\substack{j>0\\j\ {\rm odd}}}
\chi _4(j)(hj)^{-3/4}W(hj/M)e(\sqrt{Nhj}).                       \tag{3.16}
\]

The saddle map sends the strict inequality \(m>4h^2\) formally to \(r<\sqrt N\), and at the second saddle this is \(j>4h\). Thus the phase, character, amplitude, Gaussian units, and formal strict-cone correspondence of the stationary principal symbol reproduce the original \(h\)-row. This is not a two-step asymptotic theorem: the second-stage remainder and hard endpoint/Fresnel transition are not derived here, and the inherited Round-140 ledger applies only to the fully reassembled reciprocal family. Likewise, Möbius removal of \((r,q)=1\) in (3.11) is only a principal-family reorganization unless its own errors and endpoints are reassembled. The calculation diagnoses principal-symbol self-return and no visible power saving; it does not reduce the target to a strictly smaller proved owner.

## 4. First doubtful or unproved step

The first unproved step is **not** the growing-\(q\) coefficient theorem: (1.1) is uniform, with dominance range (1.2). At source-method level, the first unavailable assertion would be a uniform formula

\[
\mathcal S_{a,q}(M)
=\mathcal P^{\rm stat}_{a,q}(M)+O_W(1)
\]

for arbitrary nonzero \(W\in C_c^\infty((1,2))\), followed by a second uniform transform with its moving endpoint/Fresnel transition. Jutila's Theorem 2.1 does not prove the first assertion because its amplitude is holomorphic in a complex tube, and no matched real-variable proof of either branchwise remainder is supplied here. Accordingly, (2.2), (3.9), (3.11), and (3.14)–(3.16) are explicitly restricted to stationary principal-symbol algebra. The rigorous estimate retained for separated branches is only (2.4).

After that qualification, the first substantive mechanism gap is a convergent reconstruction that preserves the moving cone and supplies the local residual estimate (3.13c). A proposed statement would have to specify

\[
C(m)=
\sum_{\substack{q\le Q\\4\mid q}}
\sum_{a\bmod q}^{*}\gamma(a,q)e(-am/q)+E_Q(m),                   \tag{4.1}
\]

where \(Q\), the summation convention, the moving boundary, and the short-interval bounds for \(E_Q\) are all explicit. Formula (1.1) gives the Bohr coefficients but does not prove (4.1). The divergence ledger (3.7), the exact finite-cutoff tail (3.7b), and the Abel identity (3.7a) show why: finite cutoffs retain every larger mode, while the canonical convergent ordering reconstructs \(\sigma_{\chi _4}=r_2/4\), not \(C\). Kaneko's strict hypothesis \(\Re\xi>0\) and complete coefficient are the matching source-level obstruction, not a weakness in the sharp \(q\)-uniform row theorem.

If limiting reconstruction is bypassed with the exact identity (2.1), the next unproved step is signed cancellation after summing all \(q\ll\sqrt M\), their moving endpoints, and the Round-142 nonresonant mask. The rigorous branchwise modulus ledger (1.4) is owner-sized; even the scale-dependent local cutoff \(Q_M\) leaves \(R^{1/2+o(1)}\) at the top block; and the principal-symbol calculation (3.14)–(3.16) merely reproduces the original phase and coefficient. No audited primary theorem estimates this individual fixed-centre complex direction with the incomplete cone coefficient.

It would be invalid to declare a contradiction or a lower bound from the \(O(R)\) capacity, to identify phase-value nonresonance with derivative separation, to discard the \(q^2/4<m\) endpoint, to treat principal-symbol self-return as an exact two-step theorem, or to infer an individual complex-branch estimate from a Voronoï cosine. The sharp rational-mean computation, exact finite Fourier algebra, and local saddle signs/amplitudes are not doubtful; the missing branchwise remainders and endpoint transitions are.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| exact_cone_hyperbola_endpoints_and_parity | **Pass.** Equation (3.1) starts at the exact first odd integer \(4h+1\), uses the closed upper endpoint through \(K_h(T)\), and stops at the exact last nonempty height \(H_T\). |
| reduced_rational_frequency_and_q_mod_4_cases | **Pass.** Reduced modes have a main term exactly when \(4\mid q\). The exact finite identity separately retains nonreduced residues and the moving cutoff \(q^2/4<m\). |
| row_mean_residue_classes_sign_and_constant | **Pass.** Constant rows are exactly \(q=4d,\ h=d\ell\) with \(\ell\) odd; their value is \(i\chi _4(a)\chi _4(\ell)\). Summation gives \(i\pi\chi _4(a)/(2q)\), with opposite signs for \(a\equiv1,3\pmod4\). |
| fixed_q_versus_growing_q_error_uniformity | **Pass.** Complete \(h\)-periods and reciprocal root spacing give the uniform error \(O((\sqrt M+q)\log(2q))\). The dominance range is \(q\log(2q)=o(\sqrt M)\); the weaker \(O(q\sqrt M)\) rowwise estimate is not used. |
| rational_spectrum_convergence_and_reconstruction | **Pass as an exact no-go.** Mean coefficients have \(\ell^1\)-mass \(\asymp Q\) and squared mass \(\asymp\log Q\); (3.7b) retains every omitted denominator; and the canonical Abel order (3.7a) reconstructs \(r_2/4\), not \(C\). Kaneko's convergent expansion has \(\Re\xi>0\) and the matching complete coefficient. |
| local_derivative_arc_width_overlap_and_multiplicity | **Pass as a no-go.** Equations (3.12)–(3.13b) give the curvature length, Farey order, exact mediant widths, half-open ownership, thickened overlap, integer winding, and physical cell count. The missing input is the conic short-interval residual estimate (3.13c). |
| nonresonant_phase_value_versus_slope_distinction | **Pass as a prohibition.** The condition on \(j_m\) is not used to remove stationary derivative arcs. Branchwise filter removal would in any case accumulate over the full denominator mass. |
| periodic_branch_all_dyadic_R_and_q_power_ledger | **Fail at target scale.** The rigorous direct bound is \(\min\{M^{1/4},RM^{-1/2}+R^{-1}\}\); the fixed-\(q\) coefficient mass is \(1\); branchwise assembly over \(q\ll\sqrt M\) gives (1.4), before the separate moving-boundary owner. The natural cutoff \(Q_M\asymp M^{3/4}/R\) still leaves \(R^{1/2+o(1)}\) at \(M\asymp R^2\). |
| source_theorem_coefficient_q_range_and_direction | **Pass as a corrected audit, no applicable cone theorem.** Jutila's Theorem 2.1 and negative-curvature remark are at printed pp. 50 and 59 (PDF pp. 58 and 67); its holomorphic amplitude does not cover arbitrary nonzero \(C_c^\infty\) \(W\), and Theorem 2.2 has additional \(U,J\), condition (vi), and (2.1.10) scope. His divisor formula is complete and cosine-valued; Kaneko is complete and excludes \(\xi=0\) in Lemma 3.2; Banerjee–Khurana exclude \(\nu=0\) and require analytic testing. |
| raw_capacity_versus_fixed_centre_signed_scalar | **Pass.** Equations (1.3)–(1.4) are explicitly only absolute capacities. No lower bound and no failure of the signed target are asserted. |
| canonical_transform_self_return_and_downstream_scope | **Pass only as principal-symbol algebra.** The second saddle reproduces the phase, character, amplitude, Gaussian unit, and formal \(j>4h\) correspondence. No second uniform remainder or hard endpoint/Fresnel transition is proved branchwise; only the reassembled Round-140 owner ledger is inherited. No lower GAR, direct M1, M9-M1, M2, endpoint, M9, quarter, or exponent promotion is claimed. |

No numerical experiment was performed. The allocation was 100% analytical, algebraic, and primary-source verification.

## 6. Dependencies and exact artifacts used

The permitted local artifacts used were:

* protocol.md;
* state/proof_obligations.yml;
* state/active_campaign.yml;
* strategy/conductor_0823_full_proof_strategy.md;
* rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reports/sqrt_divisor_twist_source_audit.md;
* rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reviews/blind_post_unmask_source_mellin_audit.md;
* rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reviews/conductor_round141_incomplete_fibre_adjudication.md;
* rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/synthesis.md;
* rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/reports/rational_mode_hyperbola_attack.md;
* rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/candidates/conductor_round142_rational_spectrum_self_return.md;
* rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/reviews/discovery_post_unmask_source_bprocess_audit.md;
* the Round-142 task brief for this report.

The primary sources checked directly were:

* M. Jutila, *Lectures on a Method in the Theory of Exponential Sums*, Theorems 1.1, 2.1, 2.2 and the negative-curvature remark ([primary PDF](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr80.pdf));
* I. Kaneko, *Mixed Moments of the Riemann Zeta and Dirichlet \(L\)-Functions*, Theorem 3.1 and Lemmas 3.2–3.3 ([primary preprint PDF](https://arxiv.org/pdf/2109.12495));
* D. Banerjee and K. Khurana, *Character Analogues of Cohen-Type Identities and Related Voronoi Summation Formulas*, Theorems 4.3–4.4 ([primary preprint PDF](https://arxiv.org/pdf/2306.12399)).

The exact row-mean, finite Fourier, finite-cutoff, and Abel calculations were derived analytically. The stationary points, critical phases, Hessian amplitudes, Gaussian units, and principal-symbol self-return were also derived algebraically, but no branchwise two-step remainder theorem is asserted. The branch bound (2.4) is the separate rigorous second-derivative estimate. No computation was used. No graph, proof draft, shared state, validation file, plan, synthesis, review, or control artifact was edited.

## 7. Recommended state effect

**Promote as candidate auxiliary evidence, subject to conductor seam review:** the exact rational-mean lemma (1.1), including its \(O((\sqrt T+q)\log(2q))\) error and \(q\log(2q)=o(\sqrt T)\) dominance range; the exact finite rational identity (2.1); the finite-cutoff and Abel reconstruction identities (3.7a)–(3.7b); the rigorous direct branch bound (2.4); and the stationary-principal algebra (3.8)–(3.16), limited to its signs, critical points, amplitudes, \(R/q\) capacity, and formal strict-cone correspondence.

**Retain unresolved:** a hypothesis-matched uniform \(C_c^\infty\) first transform with branchwise remainder; the second-stage remainder and hard endpoint/Fresnel transition; the fixed-centre nonresonant estimate \(T_{\rm nr}\ll X^\epsilon\); the conic short-interval residual theorem (3.13c); and any cancellation theorem for the fully reassembled signed aggregate.

**Reject as Round-142 closure mechanisms:** treating Jutila's holomorphic-amplitude theorem as a uniform theorem for arbitrary nonzero \(C_c^\infty\) \(W\); treating (3.14)–(3.16) as an exact two-step transform; extracting all required modes from fixed-\(q\) means; truncating the formal \(\xi=0\) Ramanujan spectrum without a reconstruction theorem; summing rational branches by absolute values; deleting endpoint or nonresonant masks branchwise without paying their denominator mass; or importing a complete divisor/Voronoï cosine bound into the incomplete individual complex direction.

No downstream proof-state promotion follows from this source audit alone.
