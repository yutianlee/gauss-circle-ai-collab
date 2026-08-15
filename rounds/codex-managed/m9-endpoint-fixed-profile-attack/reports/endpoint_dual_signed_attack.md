# Balanced dual signed endpoint attack

## 1. Result and verdict

Put

\[
 R=\sqrt X,\qquad D\asymp R,\qquad K\asymp L,\qquad
 1\le L\le R^{1/2}.
\]

For the actual smooth transformed symbol, write

\[
 \mathcal T_{L,L}(R)
 =\sum_{h\asymp L}\sum_{k\asymp L}
 \chi_4(h)a(h,k)e(R\sqrt{hk}).                       \tag{1.1}
\]

The target is

\[
 \mathcal T_{L,L}(R)\ll_\varepsilon L^{3/2}X^\varepsilon.
 \tag{1.2}
\]

The strongest bound justified by the accepted estimates and by the exact
primary theorems audited below is

\[
\boxed{
 |\mathcal T_{L,L}(R)|
 \ll_\varepsilon X^\varepsilon
 \min\!\left(L^2,R^{1/2}L^{1/2}\right).}
 \tag{1.3}
\]

The two terms meet at \(L=R^{1/3}=X^{1/6}\). Relative to the target, the
remaining loss is

\[
\boxed{
 \frac{\min(L^2,R^{1/2}L^{1/2})}{L^{3/2}}
 =\min\!\left(L^{1/2},\frac{R^{1/2}}L\right).}
 \tag{1.4}
\]

Thus (1.3) reaches (1.2) only at the already known ends: subpower/unit
frequency and \(L\asymp R^{1/2}=X^{1/4}\). Its largest power deficit occurs
at \(L=R^{1/3}\), where the ratio is

\[
 R^{1/6}=X^{1/12}.                                   \tag{1.5}
\]

There is, however, a rigorous reduction of the arithmetic obstruction:

- product multiplicity energy is only \(O(L^2\log L)\);
- all exact square products contribute \(O_\varepsilon(L^{1+\varepsilon})\);
- products within square-root distance \(R^{-1}\) of an integer contribute
  \(O_\varepsilon(L^{1+\varepsilon})\);
- every single squarefree product ray contributes
  \(O_\varepsilon((L/\sqrt q+1)L^\varepsilon)\);
- the part with \((h,k)\ge L^{1/2}\) is already
  \(O(L^{3/2})\) absolutely.

Hence squares, near-squares, one coherent squarefree ray, large gcd, and raw
product multiplicity are not the endpoint obstruction. The unresolved core
is the small-gcd aggregate of many nonsquare product rays.

The character can be retained exactly there. After writing
\(h=ga,\ k=gb,\ (a,b)=1\), it produces a difference of two quarter-integer
resonance packets for \(R\sqrt{ab}\); see (6.5). No audited theorem controls
that *signed* packet at the required strength. Complementary divisors also
do not close the problem: they cancel the odd \(m\equiv3\pmod4\) sector only
for a symmetric symbol, reinforce the \(m\equiv1\pmod4\) sector, and provide
no pairing at all for the even-product sector.

**Verdict:** no new endpoint \(L\)-range is closed. Retain (1.2) as open.
Promote only the scoped multiplicity/square/large-gcd reductions and retain
the signed quarter-resonance packet (6.7), or the alternating-shift
correlation (7.5), as the smallest surviving character-sensitive lemma.

No numerical experiment was used.

## 2. Exact hypotheses and normalization

The report treats a fixed balanced smooth block. More precisely, assume
\(a(h,k)=A(h/L,k/L)\), after a bounded number of dyadic subdivisions, where
\(A\) is supported in a fixed compact subset of
\((0,\infty)^2\) and has fixed normalized derivative bounds. The actual
symbol from the smooth \(d\)-Poisson transform has this form:

\[
 a(h,k)=q_L(h)
 \left(\frac{L^2}{hk}\right)^{3/4}
 W\!\left(c_D\sqrt{\frac hk}\right),                 \tag{2.1}
\]

where \(c_D\asymp1\), \(q_L\) is the Vaaler/dyadic amplitude, and
\(W\in C_c^\infty((0,\infty))\). Constants below may depend on these fixed
profiles. The factor \(\chi_4(h)\) is not absorbed into a generic
two-variable coefficient.

Round 5 proved the smooth identity

\[
 \mathcal B^+_{L,W}
 =c_0R^{1/2}L^{-3/2}\mathcal T_{L,L}+O_W(1),
 \qquad |c_0|\asymp1,                                \tag{2.2}
\]

at \(D\asymp R\). Therefore the accepted T2S estimate

\[
 |\mathcal B^+_{L,W}|
 \ll_\varepsilon X^\varepsilon\left(1+\frac DL\right)
 \ll_\varepsilon X^\varepsilon\frac RL               \tag{2.3}
\]

implies

\[
 |\mathcal T_{L,L}|
 \ll_\varepsilon X^\varepsilon R^{1/2}L^{1/2}.
 \tag{2.4}
\]

Together with the trivial \(L^2\) estimate, this proves (1.3). The transform
error in (2.2) contributes \(O(R^{-1/2}L^{3/2})\) after inversion and is
smaller than every displayed bound.

## 3. Exact primary bilinear theorem and its deficit

The closest applicable primary theorem found is Proposition 5 of
E. Kowalski, O. Robert, and J. Wu,
[*Small gaps in coefficients of \(L\)-functions and \(B\)-free numbers in
small intervals*](https://arxiv.org/abs/math/0507001). It states, for
\(\alpha,\beta\notin\{0,1\}\), \(|\varphi_m|,|\psi_n|\le1\), and

\[
 S(M,N)=\sum_{m\sim M}\sum_{n\sim N}
 \varphi_m\psi_n
 e\!\left(\frac{\mathsf X m^\alpha n^\beta}
 {M^\alpha N^\beta}\right),
\]

that

\[
 S(M,N)\ll_\varepsilon
 \left[
 (\mathsf X M^6N^6)^{1/8}
 +M^{1/2}N+MN^{3/4}
 +\mathsf X^{-1/2}MN
 \right](MN)^\varepsilon.                            \tag{3.1}
\]

For (1.1), take

\[
 \alpha=\beta=\frac12,\qquad M\asymp N\asymp L,\qquad
 \mathsf X=R\sqrt{MN}\asymp RL.                      \tag{3.2}
\]

A fixed smooth two-variable symbol is admissible: extend \(A\) smoothly to
a fixed torus and use its absolutely summable Fourier series. Each Fourier
mode is a product coefficient \(\varphi_h\psi_k\), with
\(\chi_4(h)\) retained inside \(\varphi_h\). Summing (3.1) over the Fourier
modes gives

\[
 |\mathcal T_{L,L}|
 \ll_\varepsilon X^\varepsilon
 \left(
 R^{1/8}L^{13/8}
 +L^{3/2}+L^{7/4}
 +R^{-1/2}L^{3/2}
 \right).                                             \tag{3.3}
\]

Term by term, division by \(L^{3/2}\) gives

\[
 (RL)^{1/8},\qquad 1,\qquad L^{1/4},\qquad R^{-1/2}.
 \tag{3.4}
\]

Thus the theorem misses the target through both its first and third terms.
It is nontrivial against \(L^2\) only when \(L>R^{1/3}\). In that range its
first term dominates and the accepted T2S transfer (2.4) is smaller:

\[
 \frac{R^{1/2}L^{1/2}}{R^{1/8}L^{13/8}}
 =R^{3/8}L^{-9/8}\le1
 \quad(L\ge R^{1/3}).                                 \tag{3.5}
\]

For \(L\le R^{1/3}\), the trivial bound is no larger than the first term in
(3.3). Hence the exact primary bilinear theorem does not improve (1.3).

The spacing input behind (3.1) is Theorem 2 of O. Robert and P. Sargos,
[*Three-dimensional exponential sums with
monomials*](https://doi.org/10.1515/CRELLE.2006.012). For fixed
\(\alpha\ne0,1\), it proves

\[
 \#\left\{m_i\asymp M:
 |m_1^\alpha+m_2^\alpha-m_3^\alpha-m_4^\alpha|
 \le \Delta M^\alpha\right\}
 \ll_\varepsilon
 (M^2+\Delta M^4)M^\varepsilon.                      \tag{3.6}
\]

This is the optimal square-root spacing count needed by the
coefficient-blind double-large-sieve argument. It does not use
\(\chi_4\), and (3.3) records the remaining endpoint loss after its
application.

## 4. Product multiplicity, squares, and near-squares

Define the unsigned localized product multiplicity and the signed
coefficient

\[
 r_L(m)=\#\{(h,k):h\asymp L,\ k\asymp L,\ hk=m\},
 \tag{4.1}
\]

\[
 c_L(m)=\sum_{\substack{hk=m\\h,k\asymp L}}
 \chi_4(h)a(h,k).
 \tag{4.2}
\]

Then

\[
 \mathcal T_{L,L}=\sum_{m\asymp L^2}c_L(m)e(R\sqrt m),
 \qquad |c_L(m)|\ll r_L(m).                           \tag{4.3}
\]

### 4.1 Exact product-collision energy

One has

\[
\boxed{\sum_m r_L(m)^2\ll L^2\log(2L).}              \tag{4.4}
\]

Indeed, a solution \(h_1k_1=h_2k_2\) can be written uniquely as

\[
 h_1=ga,\qquad h_2=gb,\qquad
 k_1=bt,\qquad k_2=at,\qquad (a,b)=1.                \tag{4.5}
\]

The shell conditions force \(a\asymp b\), while for fixed \(a,b\) both
\(g\) and \(t\) have \(O(L/\max(a,b))\) choices. Group by the exact value
\(n=\max(a,b)\). There are \(O(n)\) coprime ordered pairs \((a,b)\) in that
group, and each contributes \(O(L^2/n^2)\). Therefore

\[
 \sum_m r_L(m)^2
 \ll \sum_{n\le CL} n\frac{L^2}{n^2}
 \ll L^2\log(2L),
\]

which proves (4.4). Consequently,

\[
 \sum_m|c_L(m)|^2\ll L^2\log(2L).                    \tag{4.6}
\]

This shows that product fibers have controlled energy, but Cauchy in
\(m\) still gives only \(O(L^2\sqrt{\log L})\), not \(L^{3/2}\).

### 4.2 Exact square products

The number of pairs for which \(hk\) is a square satisfies

\[
\boxed{
 \sum_{n}r_L(n^2)\ll L\log(2L)\ll_\varepsilon
 L^{1+\varepsilon}.}                                 \tag{4.7}
\]

To prove it, write uniquely

\[
 h=s u^2,\qquad k=s v^2,
 \tag{4.8}
\]

where \(s\) is squarefree. For fixed \(s\), there are
\(O(\sqrt{L/s}+1)\) choices for each of \(u,v\), hence
\(O(L/s+1)\) pairs. Summing over \(s\ll L\) proves (4.7). Therefore exact
square products are already below the target absolutely, even if
\(R\) is an integer and every square-product phase is \(1\).

More generally, every product has a unique squarefree-ray representation
\(m=qn^2\). On a fixed ray,

\[
\boxed{
 \sum_n r_L(qn^2)
 \ll_\varepsilon
 \left(\frac L{\sqrt q}+1\right)L^\varepsilon.}
 \tag{4.9}
\]

Indeed, there are \(O(L/\sqrt q+1)\) possible \(n\), and each product has
at most \(\tau(qn^2)\ll_\varepsilon L^\varepsilon\) localized divisors.
Thus complete phase coherence on any one squarefree ray is harmless. A
failure at \(L^{3/2}\) would have to aggregate many rays.

### 4.3 Products near squares

For \(0\le\eta\le1\),

\[
\boxed{
 \#\{(h,k):h,k\asymp L,\ 
 \operatorname{dist}(\sqrt{hk},\mathbb Z)\le\eta\}
 \ll_\varepsilon
 (L^2\eta+L)L^\varepsilon.}                          \tag{4.10}
\]

There are \(O(L)\) possible integers \(n\asymp L\). The condition
\(|\sqrt m-n|\le\eta\) puts the integer \(m\) in an interval containing
\(O(L\eta+1)\) integers, and each \(m\) has
\(O_\varepsilon(L^\varepsilon)\) localized factorizations. At the natural
coherence thickness \(\eta=R^{-1}\), the endpoint relation
\(R\ge L^2\) yields

\[
 \#\{\operatorname{dist}(\sqrt{hk},\mathbb Z)\le R^{-1}\}
 \ll_\varepsilon L^{1+\varepsilon}.                  \tag{4.11}
\]

Thus square and near-square products are not responsible for the
\(L^{1/2}\) saving missing from the full double sum.

## 5. Complementary divisors and the exact parity obstruction

Extend \(a\) by zero outside its balanced support and put

\[
 a_{\mathrm s}(h,k)=\frac{a(h,k)+a(k,h)}2,\qquad
 a_{\mathrm a}(h,k)=\frac{a(h,k)-a(k,h)}2.           \tag{5.1}
\]

For odd \(m\), complementary substitution \(h\leftrightarrow k=m/h\)
in (4.2) gives the exact identity

\[
 c_L(m)=\frac12
 \sum_{hk=m}\chi_4(h)
 \left(a(h,k)+\chi_4(m)a(k,h)\right).                \tag{5.2}
\]

Hence

\[
 c_L(m)=
 \begin{cases}
 \displaystyle\sum_{hk=m}\chi_4(h)a_{\mathrm s}(h,k),
   &m\equiv1\pmod4,\\[2mm]
 \displaystyle\sum_{hk=m}\chi_4(h)a_{\mathrm a}(h,k),
   &m\equiv3\pmod4.
 \end{cases}                                         \tag{5.3}
\]

For a symmetric symbol, the \(m\equiv3\pmod4\) sector therefore vanishes,
but the \(m\equiv1\pmod4\) sector reinforces. The actual symbol (2.1) is
not symmetric in general: it contains both the one-sided Vaaler factor
\(q_L(h)\) and a ratio weight \(W(c_D\sqrt{h/k})\). Its antisymmetric part
is not power-small on a fixed balanced rectangle.

If \(m\) is even, every contributing \(h\) in (4.2) is odd and its
complement \(k=m/h\) is even. The complementary ordered term has
\(\chi_4(k)=0\), so there is no termwise character pairing at all. Thus
complementary-divisor cancellation cannot control the complete actual
symbol.

This also passes the proves-too-much test: replacing \(a\) by a symmetric
positive symbol does not create universal cancellation; it retains the
entire \(m\equiv1\pmod4\) sector, including all odd square products.

## 6. Gcd decomposition and exact quarter-resonance packets

Write

\[
 h=ga,\qquad k=gb,\qquad (a,b)=1.                    \tag{6.1}
\]

Dyadically localize \(g\asymp G\). Then
\(a,b\asymp A:=L/G\), and the number of terms in this gcd shell is

\[
 \ll G A^2=\frac{L^2}{G}.                            \tag{6.2}
\]

It follows immediately that

\[
\boxed{
 \sum_{\substack{h,k\asymp L\\(h,k)\ge L^{1/2}}}
 |\chi_4(h)a(h,k)|
 \ll L^{3/2}.}                                       \tag{6.3}
\]

Thus only \(G<L^{1/2}\) remains.

The character survives exactly in those shells. Since a contributing
\(h\) is odd, both \(g\) and \(a\) are odd and

\[
 \chi_4(h)=\chi_4(g)\chi_4(a).                       \tag{6.4}
\]

For fixed coprime \(a,b\), let \(F_{a,b,G}\) be the fixed smooth
scale-normalized \(g/G\)-profile induced by the actual symbol and gcd
cutoff. With \(\widehat F(\xi)=\int F(u)e(-u\xi)\,du\), Poisson summation
and

\[
 \chi_4(g)=\frac{e(g/4)-e(3g/4)}{2i}
\]

give the exact identity

\[
\begin{aligned}
 &\sum_g\chi_4(g)F_{a,b,G}(g/G)e(Rg\sqrt{ab})\\
 &\quad=\frac{G}{2i}\sum_{n\in\mathbb Z}
 \Big[
 \widehat F_{a,b,G}
   \big(G(n-R\sqrt{ab}-1/4)\big)
 -
 \widehat F_{a,b,G}
   \big(G(n-R\sqrt{ab}-3/4)\big)
 \Big].
                                                               \tag{6.5}
\end{aligned}
\]

In particular, for every \(B>0\),

\[
 \left|\sum_g\chi_4(g)F_{a,b,G}(g/G)e(Rg\sqrt{ab})\right|
 \ll_B G\sum_{\sigma=\pm1}
 \left(1+G\left\|R\sqrt{ab}-\frac{\sigma}{4}\right\|\right)^{-B}.
 \tag{6.6}
\]

Thus \(\chi_4(g)\) shifts the resonances from integers to the two
quarter-integer classes; it does not eliminate them.

Define the actual signed packet

\[
\begin{aligned}
 \mathcal Q_G(R)=
 \sum_{\substack{a,b\asymp L/G\\(a,b)=1\\a\ {\rm odd}}}
 \chi_4(a)\sum_{n\in\mathbb Z}
 \Big[&
 \widehat F_{a,b,G}
   \big(G(n-R\sqrt{ab}-1/4)\big)\\
 -&
 \widehat F_{a,b,G}
   \big(G(n-R\sqrt{ab}-3/4)\big)
 \Big].
                                                               \tag{6.7}
\end{aligned}
\]

The gcd shell is exactly

\[
 \mathcal T_G=\frac{G}{2i}\mathcal Q_G(R).            \tag{6.8}
\]

After (6.3), the weakest direct signed lemma that closes the balanced
endpoint is therefore

\[
\boxed{
 \sum_{\substack{G<L^{1/2}\\G\ {\rm dyadic}}}
 G\,|\mathcal Q_G(R)|
 \ll_\varepsilon L^{3/2}X^\varepsilon,}
 \tag{6.9}
\]

or the still weaker version with the absolute value outside the sum over
\(G\), provided the chosen gcd partition is fixed. This lemma retains:

1. the numerator sign \(\chi_4(a)\);
2. cancellation between the \(1/4\) and \(3/4\) packets;
3. the actual profile-dependent Fourier kernels.

It is strictly less demanding than an unsigned count of quarter-resonant
pairs and than the character-erasing mean square from Round 5. Neither
Robert--Sargos (3.6) nor Kowalski--Robert--Wu (3.1) proves (6.9), because
their Cauchy/large-sieve input bounds absolute spacing multiplicities and
does not retain the signed packet difference.

Euclidean square-root spacing alone cannot replace (6.9). Although distinct
products \(m_1,m_2\asymp L^2\) satisfy

\[
 |\sqrt{m_1}-\sqrt{m_2}|\gg \frac{|m_1-m_2|}{L},      \tag{6.10}
\]

the endpoint is pointwise for every real \(R\). For any two distinct
products one may choose
\(R=N/|\sqrt{m_1}-\sqrt{m_2}|\), with \(N\) arbitrarily large, so their
phases coincide modulo \(1\). Uniform control requires a collective
arithmetic spacing theorem, not only the real-line minimum spacing.

## 7. The character-preserving Cauchy seam

If Cauchy is used, it should be applied in the \(k\)-variable:

\[
 |\mathcal T_{L,L}|^2
 \le L\sum_{k\asymp L}
 \left|\sum_{h\asymp L}
 \chi_4(h)a(h,k)e(R\sqrt{hk})\right|^2.              \tag{7.1}
\]

This preserves the character inside the squared sum. The diagonal
\(h_1=h_2\) contributes \(O(L^2)\), exactly the admissible mean-square
scale. For odd \(h\) and \(h+2r\),

\[
 \chi_4(h)\chi_4(h+2r)=(-1)^r.                       \tag{7.2}
\]

Consequently the off-diagonal is exactly the real part of

\[
 \mathfrak C_\chi(R;L)
 =
 2\sum_{r\ge1}(-1)^r
 \sum_{\substack{h,h+2r\asymp L\\h\ {\rm odd}}}
 \sum_{k\asymp L}
 a(h,k)\overline{a(h+2r,k)}
 e\!\left(R\sqrt{k}\,(\sqrt h-\sqrt{h+2r})\right).
 \tag{7.3}
\]

Thus the clean Cauchy-based signed successor is

\[
\boxed{
 \operatorname{Re}\mathfrak C_\chi(R;L)
 \ll_\varepsilon L^2X^\varepsilon.}                 \tag{7.4}
\]

It would imply (1.2) via (7.1). Unlike the Round-5 mean square obtained by
Cauchy in \(h\), (7.4) retains the exact alternating shift \((-1)^r\).
The absolute version

\[
 \sum_{r,h,k}|\cdots|\ll L^2X^\varepsilon            \tag{7.5}
\]

would discard the mechanism and is not proposed. No audited theorem
controls (7.3) with its alternating shift at the diagonal scale.

Statement (7.4) is stronger than the single linear target (1.2), because
it is still a Cauchy mean-square route. The direct packet lemma (6.9) is the
weaker and preferable next interface.

## 8. Mellin separation and the \(r_2\)/Voronoi return

The balanced product coefficient is close enough to an \(r_2\)-coefficient
that a Voronoi check is mandatory, but the check does not close the target.

### 8.1 Mellin-separated coefficient

For a fixed smooth symbol, Mellin separation gives schematically

\[
 A(h/L,k/L)
 =\iint_{\mathbb R^2}
 \widetilde A(t_1,t_2)
 (h/L)^{it_1}(k/L)^{it_2}\,dt_1dt_2,                 \tag{8.1}
\]

with rapidly decaying \(\widetilde A\). On the product fiber \(hk=m\), one
mode has coefficient

\[
 m^{it_2}
 \sum_{h\mid m}\chi_4(h)h^{i(t_1-t_2)}.              \tag{8.2}
\]

Its Dirichlet series is

\[
\begin{aligned}
 &\sum_{m\ge1}m^{-s+it_2}
 \sum_{h\mid m}\chi_4(h)h^{i(t_1-t_2)}\\
 &\qquad=\zeta(s-it_2)L(s-it_1,\chi_4).              \tag{8.3}
\end{aligned}
\]

Thus each Mellin mode is a degree-two Eisenstein/generalized-divisor
coefficient. At \(t_1=t_2=0\), summing all divisor-ratio pieces recovers

\[
 \sum_{h\mid m}\chi_4(h)=\frac14r_2(m).              \tag{8.4}
\]

This confirms that a uniform endpoint theorem for these modes is
circle-problem strength; it does not make the coefficient smooth in \(m\).

### 8.2 What the Voronoi transform actually produces

Consider first the \(r_2\) mode. The standard self-dual circle Voronoi
kernel contains \(J_0(2\pi\sqrt{ny})\). Apply it to

\[
 f(y)=w(y/L^2)e(R\sqrt y),\qquad y\asymp L^2.        \tag{8.5}
\]

With \(u=\sqrt y\), the two Bessel phases are

\[
 e\!\left((R\pm\sqrt n)u\right).                     \tag{8.6}
\]

The plus phase is nonstationary. The minus phase is large only when

\[
 |\sqrt n-R|\ll L^{-1},
 \qquad\text{equivalently}\qquad
 |n-R^2|\ll \frac RL.                                \tag{8.7}
\]

The Bessel amplitude and \(dy=2u\,du\) give the uniform resonant-kernel
scale

\[
 \mathcal H_R(n)
 \ll_A
 R^{-1/2}L^{3/2}
 \left(1+L|\sqrt n-R|\right)^{-A}.                   \tag{8.8}
\]

The same scale holds for the imaginary-order kernels arising from (8.3);
the rapid Mellin decay absorbs their polynomial order-dependence. Fixed
conductor factors change only the center by a fixed constant.

Therefore Voronoi returns a dual **first product annulus** of length
\(R/L\) around \(n\asymp R^2=X\):

\[
 \mathcal T_{L,L}
 \quad\leadsto\quad
 R^{-1/2}L^{3/2}
 \sum_{|n-R^2|\ll R/L}
 b(n)\,
 \mathcal W\!\left(L(\sqrt n-R)\right),              \tag{8.9}
\]

where \(b(n)\) is the dual generalized-divisor coefficient and
\(\mathcal W\) is a fixed Schwartz profile. The polar integral is
nonstationary for the smooth block and is harmless.

Using only \(b(n)\ll_\varepsilon n^\varepsilon\), the annulus in (8.9)
gives

\[
 R^{-1/2}L^{3/2}\frac RL X^\varepsilon
 =R^{1/2}L^{1/2}X^\varepsilon,                       \tag{8.10}
\]

exactly the T2S-transferred term in (1.3). Thus Voronoi does not improve
the best ledger; it is an involutive return to the first product annulus.

To reach \(L^{3/2}\), the weighted dual annulus in (8.9) would have to be

\[
 \ll_\varepsilon R^{1/2}X^\varepsilon               \tag{8.11}
\]

instead of its trivial size \(R/L\). For the full \(r_2\) mode, the
constant-density contribution is matched by the polar integral in the exact
Voronoi formula (equivalently, the oscillatory smooth kernel has zero
contribution from that main density). Partial summation then leaves the
circle remainder. A bound

\[
 \sum_{n\le x}r_2(n)-\pi x\ll_\varepsilon x^{\theta+\varepsilon}
\]

would give at best \(R^{2\theta+\varepsilon}\) for the annular sum. The
requirement (8.11) is exactly \(\theta\le1/4\). Existing exponents
\(\theta>1/4\) therefore return a power loss, while assuming
\(\theta=1/4\) is circular for this project. The Mellin-shifted modes
require the analogous uniform generalized-divisor remainder.

Hence a GL(2)/Eisenstein or \(r_2\) Voronoi transform is a useful
normalization check, not a proof of (1.2). It returns precisely the
first-annulus problem that produced (2.4).

### 8.3 Arithmetic special phase \(R\in\mathbb Z\)

Let \(R=N\) be an integer. In the original sum, every exact square product
has phase

\[
 e(N\sqrt{hk})=1.
\]

Nevertheless its total absolute contribution is
\(O_\varepsilon(L^{1+\varepsilon})\) by (4.7). On every nonsquare
squarefree ray \(m=qn^2\), the phase is \(e(Nn\sqrt q)\); it is not
identically \(1\). A single completely coherent ray is still bounded by
(4.9), below the target.

On the Voronoi side, the annulus (8.7) is centered at the exact square
\(n=N^2\). The central term contributes only

\[
 R^{-1/2}L^{3/2}b(N^2)
 \ll_\varepsilon R^{-1/2}L^{3/2}X^\varepsilon,
 \tag{8.12}
\]

which is harmless. Since neighboring squares differ from \(N^2\) by
\(\asymp R\), while the annulus has width \(R/L\), it contains only
\(O(1)\) square centers for \(L\ge1\). Its remaining \(R/L\)-scale
nonsquare content is unchanged.

Thus the perfect-square model \(X=N^2\) creates one exact central resonance
and coherent square-product fibers, both already below \(L^{3/2}\). It
neither obstructs nor proves the uniform real-\(X\) estimate.

## 9. Literature applicability audit

### Kowalski--Robert--Wu

Proposition 5 of
[arXiv:math/0507001](https://arxiv.org/abs/math/0507001) matches:

- phase \(e(Rh^{1/2}k^{1/2})\) through (3.2);
- balanced lengths \(M\asymp N\asymp L\);
- arbitrary bounded separated coefficients;
- the endpoint \(\mathsf X\asymp RL>0\).

The fixed smooth actual symbol is transferred by an absolutely summable
Fourier separation. The exact resulting bound is (3.3), and every term is
compared with the target in (3.4). It does not prove (1.2).

### Robert--Sargos

Theorem 2 of
[*Three-dimensional exponential sums with
monomials*](https://doi.org/10.1515/CRELLE.2006.012)
matches the square-root exponent \(\alpha=1/2\) and gives (3.6). It is an
unsigned four-variable spacing count. Its use in the primary bilinear
theorem is already reflected in (3.3); importing it separately does not
recover \(\chi_4\) after Cauchy.

### Tao--Trudgian--Yang

The source card for Terence Tao, Tim Trudgian, and Andrew Yang,
[*New exponent pairs, zero density estimates, and zero additive energy
estimates*](https://arxiv.org/abs/2501.16779), certifies a
one-dimensional reciprocal-phase exponent pair. At \(\delta=1/2\), its
project wedge would require

\[
 178\ell+819\le463,
\]

which is impossible. Applying an exponent pair separately to one variable
of (1.1) and summing the other absolutely also misses \(L^{3/2}\). It
supplies no balanced signed bilinear theorem.

### Li--Yang

Xiaochun Li and Xuerui Yang,
[*An improvement on Gauss's Circle Problem and Dirichlet's Divisor
Problem*](https://arxiv.org/abs/2308.14859), treats a
Bombieri--Iwaniec first/second-spacing architecture. Its first-spacing norm
uses a vector involving \((l,kl,l\sqrt k,l/\sqrt k)\), not the pointwise
sum (1.1), and its source card remains incomplete. Its published method is
at an exponent strictly above \(1/4\). No theorem from it is imported.

No exact primary theorem located in this audit proves (6.9), (7.4), or the
target (1.2) for the actual balanced symbol.

## 10. Required controls

### Signed versus unsigned

The character is retained in (5.2), in the gcd factorization (6.4), in the
packet difference (6.5), and as the alternating correlation shift (7.2).
The only coefficient-blind bounds are explicitly labeled as such. An
unsigned multiplicity or spacing count is never promoted to the signed
target.

### Diagonal, products, and squares

The exact product collision energy is (4.4). Exact square products,
individual squarefree rays, and \(R^{-1}\)-near-square products are bounded
in (4.7), (4.9), and (4.11), all below \(L^{3/2}\). The Cauchy diagonal is
\(O(L^2)\), exactly the required mean-square scale.

### Proves-too-much

The target is not asserted for arbitrary two-variable coefficients:
\(a(h,k)=\chi_4(h)e(-R\sqrt{hk})\) would make the sum \(L^2\).
Kowalski--Robert--Wu is applied only after using the fixed smooth symbol's
separable Fourier expansion. The proposed packet lemma retains all actual
profile kernels.

### Balanced endpoint

Every exponent uses \(R=\sqrt X\), \(K\asymp L\), and
\(1\le L\le R^{1/2}\). The unit and terminal blocks are recognized as
already solved. Section 8.3 checks \(R\in\mathbb Z\) separately and does
not substitute it for the uniform real parameter.

### Source applicability

The exact hypotheses and all four terms of the applicable bilinear theorem
are recorded in Section 3. The Robert--Sargos spacing theorem is used only
as an unsigned input. No theorem is imported from an incomplete source
card.

## 11. First doubtful or unproved step

All statements through the reduction (6.8), including the bound ledger,
product-energy estimate, square and near-square estimates, complementary
divisor algebra, large-gcd bound, and quarter-packet identity, are proved.

The first unproved step is the collective signed estimate (6.9) for the
small-gcd nonsquare rays. If Cauchy is chosen instead, the first unproved
step is (7.4). Existing square-root spacing theorems control unsigned
near-equalities and do not retain either the two packet signs in (6.7) or
the alternating shift in (7.3). Applying Voronoi merely replaces this by
the dual first-annulus estimate (8.11), which at the \(r_2\) mode requires
the same \(1/4\)-strength circle remainder.

## 12. Dependencies and exact artifacts used

- rounds/codex-managed/m9-endpoint-fixed-profile-attack/briefs/endpoint_dual_signed_attack.md
- rounds/codex-managed/m9-endpoint-fixed-profile-attack/plan.json
- rounds/codex-managed/m9-frequency-phase-diagram/reports/dual_three_quarter_attack.md
- rounds/codex-managed/m9-frequency-phase-diagram/synthesis.md
- sources/li_yang_2023.md
- sources/tao_trudgian_yang_2025.md
- state/proof_obligations.yml
- state/active_campaign.yml
- state/best_proof_draft.md
- E. Kowalski, O. Robert, J. Wu,
  [arXiv:math/0507001](https://arxiv.org/abs/math/0507001), Proposition 5.
- O. Robert, P. Sargos,
  [DOI 10.1515/CRELLE.2006.012](https://doi.org/10.1515/CRELLE.2006.012),
  Theorem 2.

No computational artifact was used.

## 13. Recommended state effect

- **Retain** the balanced target (1.2) as open.
- **Record** the best proved endpoint dual profile (1.3) and exact deficit
  (1.4)--(1.5).
- **Promote as scoped reductions** the localized product energy (4.4),
  square/near-square controls (4.7)--(4.11), complementary-divisor identity
  (5.2)--(5.3), and the large-gcd bound (6.3).
- **Retain as the preferred next lemma** the actual signed quarter-resonance
  packet estimate (6.9), restricted to \(G<L^{1/2}\).
- **Retain as a stronger backup** the character-preserving alternating-shift
  correlation (7.4); do not replace it by an absolute off-diagonal bound.
- **Record no endpoint theorem import** from Tao--Trudgian--Yang or
  Li--Yang, and record that the exact Kowalski--Robert--Wu bound is
  dominated by the accepted trivial/T2S envelope.
- **Record the Voronoi no-gain identity:** Mellin separation gives the
  Eisenstein products (8.3), whose Voronoi transform returns an annulus of
  length \(R/L\) at \(n\asymp R^2\); trivial estimation is exactly (2.4),
  and the \(r_2\) remainder reaches the target only at exponent \(1/4\).
- **No promotion** of \(M9\)-\(M2\), endpoint uniformity, or the global
  Gauss-circle target.
