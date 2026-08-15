# Conductor independent analysis: generic band and dual top block

## 1. Exact single-lift algebra

Let (H=H_D), and restrict the reduced-fraction lift decomposition to

\[
D\le q<2D,
\qquad (p,q)=1,
\qquad 1\le |p|\le H.
\]

The condition (gq\in[D,2D)) forces (g=1). Hence

\[
\boxed{A_\chi(p/q)=\beta_{p,H}w_D(q).}
\]

The audited coefficient admits two equivalent signed-(p) formulas:

\[
\beta_{p,H}
=-\frac{\Phi(|p|/(H+1))\chi_4(|p|)}{\pi|p|}
\mathbf1_{2\nmid p}
=-\frac{\Phi(|p|/(H+1))\chi_4(p)}{\pi p}.
\tag{1.1}
\]

The second identity is valid because both (p\mapsto p) and (p\mapsto\chi_4(p)) are odd. It makes the two important symmetries simultaneous:

\[
\beta_{-p,H}=\beta_{p,H},
\qquad
\beta_{p,H}=0\quad(2\mid p).
\]

For real (w_D), the generic-band sum is therefore

\[
S_{\rm gen}(t)
=2\sum_{\substack{1\le p\le H\\p\ {m odd}}}
\beta_{p,H}
\sum_{\substack{D\le q<2D\\(p,q)=1}}
w_D(q)\cos\!\left(\frac{\pi tp}{2q}\right).
\tag{1.2}
\]

No lift-index cancellation remains: B1 is sharp on this sector.

## 2. Exact pair convolution

Let

\[
\mathcal X_{\rm gen}
=\{p/q:(p,q)=1,\ D\le q<2D,\ 1\le|p|\le H,\ p\text{ odd}\}.
\]

Then

\[
R_{\rm gen}(r)
=\sum_{\substack{x+y=r\\x,y\in\mathcal X_{\rm gen}}}
A_\chi(x)A_\chi(y)
\]

is exactly

\[
R_{\rm gen}(r)
=\sum_{\substack{p_1/q_1+p_3/q_3=r\\
D\le q_1,q_3<2D\\
(p_i,q_i)=1\\
1\le|p_i|\le H,\ p_i\ {m odd}}}
\beta_{p_1,H}\beta_{p_3,H}w_D(q_1)w_D(q_3).
\tag{2.1}
\]

The critical global off-diagonal is the kernel-weighted correlation of (2.1) at

\[
0<|r-s|\le \kappa/X.
\]

Tuple by tuple this is

\[
0<|N|\le \frac{\kappa q_1q_2q_3q_4}{X},
\]

not the exact equality (N=0), and not exactly the constant threshold (D^4/X).

## 3. Why adjacent residue pairing is not a mechanism

The character identity

\[
\chi_4(p)=\frac{e(p/4)-e(3p/4)}{2i}
\tag{3.1}
\]

converts (1.2) into the difference of the two shifted reciprocal phases. This is useful globally, but it does not give a termwise (p\leftrightarrow p+2) cancellation. At a fixed denominator (q), the phase ratio between adjacent odd numerators is

\[
e\!\left(\frac{t(p+2)}{4q}\right)
e\!\left(-\frac{tp}{4q}\right)
=e\!\left(\frac{t}{2q}\right),
\tag{3.2}
\]

whose argument is unrestricted throughout the active range. Thus the opposite coefficient signs at residues (1) and (3\pmod4) may reinforce as well as cancel. Any proposed residue involution that ignores (3.2) fails the `proves-too-much` control.

Equivalently, summing the numerator variable first reconstructs a bounded square wave rather than a small quantity:

\[
\sum_{p\ne0}\beta_{p,H}e(tp/(4q))
\]

is the Vaaler main polynomial for

\[
\psi_F\!\left(\frac{t/q+1}{4}\right)
-\psi_F\!\left(\frac{t/q+3}{4}\right).
\]

The \(\chi_4\) oscillation is therefore already spent in producing the second balanced sawtooth leg. It cannot be counted again as an automatic power saving over \(q\).

## 3A. Direct pointwise high-frequency lemma

There is nevertheless a rigorous way to use the character before reconstructing the whole square wave. Let \(L\ge1\), and let \(I_L\subset[L,2L]\cap[1,H]\) be any integer interval. Define the positive-frequency block

\[
S_{2,L}^+(D;X)
=\sum_{h\in I_L}\beta_{h,H}
\sum_{D\le d<2D}w_D(d)e\!\left(\frac{hX}{4d}\right),
\]

where \(|w_D(d)|\le C_w\). Then

\[
\boxed{
|S_{2,L}^+(D;X)|
\ll_{C_w,\varepsilon}X^\varepsilon\left(1+\frac DL\right).}
\tag{3A.1}
\]

The same estimate holds for the two-sided block because the negative-frequency contribution has the identical absolute bound. This is a direct pointwise estimate at the fixed value \(X\), not a moment estimate.

### Proof

For a fixed \(d\), put

\[
\theta_d=\frac{X}{4d},
\qquad
\rho_d=\left\|2\theta_d+\frac12\right\|
=\left\|\frac{X/d+1}{2}\right\|.
\]

Writing odd \(h=2j+1\), the ratio between consecutive terms of

\[
\chi_4(h)e(h\theta_d)
\]

is

\[
-e(2\theta_d)=e\!\left(2\theta_d+\frac12\right).
\]

Therefore every partial sum over an interval of odd \(h\)'s is

\[
\ll \min(L,\rho_d^{-1}),
\tag{3A.2}
\]

with the convention that the right side is \(L\) at exact resonance.

On \(I_L\), the non-character amplitude

\[
a_h=\frac{\Phi(h/(H+1))}{h}
\]

satisfies

\[
\sup_{I_L}|a_h|+\operatorname{Var}_{I_L}(a_h)\ll L^{-1}.
\tag{3A.3}
\]

Indeed, \(0\le\Phi\le1\), \(\|\Phi'\|_\infty<\infty\), and the variation contributions from \(h^{-1}\) and \(\Phi(h/(H+1))\) are respectively \(O(L^{-1})\) and \(O((|I_L|/H)L^{-1})=O(L^{-1})\). Endpoint truncation only shortens the interval. Abel summation with (3A.2) gives

\[
\left|
\sum_{h\in I_L}\beta_{h,H}e(h\theta_d)
\right|
\ll \min\!\left(1,\frac1{L\rho_d}\right).
\tag{3A.4}
\]

It remains to sum (3A.4) over \(d\). Choose an integer \(m_d\) nearest to \((X/d+1)/2\), and set

\[
\ell_d=2m_d-1,
\qquad
n_d=d\ell_d.
\]

Then \(\ell_d\) is odd and

\[
|X-n_d|=2d\rho_d.
\tag{3A.5}
\]

For \(0<R\le1/2\), (3A.5) and \(d\asymp D\) show

\[
\#\{d\in[D,2D):\rho_d\le R\}
\le
\sum_{\substack{n\in\mathbb Z\\|n-X|\ll DR}}\tau(|n|)
\ll_\varepsilon (1+DR)X^\varepsilon.
\tag{3A.6}
\]

For the active range \(X\ge1\), all relevant \(n\) are positive after harmless treatment of bounded \(X,D\). Ties in the nearest-integer choice contribute at most a fixed multiplicity and do not change (3A.6).

The bin \(\rho_d\le L^{-1}\) contributes

\[
\ll_\varepsilon(1+D/L)X^\varepsilon.
\]

For \(2^j/L<\rho_d\le2^{j+1}/L\), the weight in (3A.4) is \(O(2^{-j})\), while (3A.6) counts at most

\[
O_\varepsilon\!\left(1+\frac{D2^j}{L}\right)X^\varepsilon
\]

denominators. Summing \(0\le j\ll\log(2L)\) gives

\[
\sum_{D\le d<2D}
\min\!\left(1,\frac1{L\rho_d}\right)
\ll_\varepsilon
X^\varepsilon\left(1+\frac DL\right),
\]

after absorbing the logarithm into \(X^\varepsilon\). This proves (3A.1).

### Consequence and limit

For the top Vaaler block

\[
L\asymp H_D\asymp DX^{-1/4},
\]

(3A.1) gives

\[
\boxed{S_{2,L}(D;X)\ll_\varepsilon X^{1/4+\varepsilon}}
\]

uniformly for every active \(D\), including \(D=X^{1/2}\). Thus the literal largest frequency block is not the remaining endpoint obstruction.

For smaller \(L\), the bound degrades to \(D/L\). It does not by itself close all frequency blocks. Combined with the previously audited Li--Yang Case A ceiling

\[
L\le D X^{-49/164}
=H_DX^{-2/41},
\]

it exposes an intermediate height corridor

\[
D X^{-49/164}<L\ll D X^{-1/4}
\]

that needs either a quantitative extension of the direct estimate, an applicable Case B region, or a new hybrid argument. The conductor has assigned an independent audit of (3A.1); it must not be promoted before that seam review returns.

## 4. Formal B-process map and the critical product scale

This subsection is a method calculation, not yet a proved project lemma: a full use requires a smooth Poisson formula with boundary, zero-frequency, and nonstationary errors.

On a positive frequency block (p\asymp L), Poisson summation in (q\asymp D) produces dual frequencies (k>0) from the stationary phase

\[
f(q)=\frac{tp}{4q}+kq.
\]

The stationary point and its phase are

\[
q_0=\sqrt{\frac{tp}{4k}},
\qquad
f(q_0)=\sqrt{tpk}.
\tag{4.1}
\]

Participation of (q_0\asymp D) forces

\[
k\asymp K:=\frac{XL}{D^2}.
\tag{4.2}
\]

The stationary-phase amplitude has scale

\[
|f''(q_0)|^{-1/2}\asymp \frac{D^{3/2}}{\sqrt{XL}}.
\]

Since (|\beta_p|\asymp L^{-1}) on the block, the formal top-block main term has the shape

\[
\frac{D^{3/2}}{X^{1/2}L^{3/2}}
\sum_{p\asymp L\atop p\ {m odd}}\chi_4(p)
\sum_{k\asymp K}a_{p,k}
e\!\left(\sqrt{Xpk}+\frac18\right),
\tag{4.3}
\]

where (a_{p,k}) is a smooth bounded symbol.

For the largest Vaaler block

\[
L\asymp H_D\asymp DX^{-1/4},
\]

(4.2) gives

\[
K\asymp X^{3/4}/D,
\qquad
\boxed{LK\asymp X^{1/2}.}
\tag{4.4}
\]

Thus every active denominator scale sends its top frequency block to the same critical product scale (pk\asymp X^{1/2}). At (D=X^{1/2}), the dual block is balanced:

\[
L\asymp K\asymp X^{1/4}.
\]

The trivial bound for the double sum in (4.3) gives (S_L\ll X^{3/8+o(1)}). Reaching (X^{1/4+\varepsilon}) requires a factor (X^{1/8-o(1)}) of cancellation in the unit-weight ((p,k)) sum, uniformly through the balanced endpoint.

## 5. Product grouping uses, but does not magically exploit, the character

Grouping (4.3) by (m=pk) produces a square-root phase

\[
e(\sqrt{Xm})
\]

and a restricted divisor coefficient of the form

\[
a_L(m)=\sum_{p\mid m\atop p\asymp L}\chi_4(p)\,b(p,m/p).
\tag{5.1}
\]

This is the local Hardy/Voronoi shape. The phase now depends only on the product, so the two-dimensional phase has an exact degeneracy along divisor fibers.

There is an elementary warning at the balanced point. If (L=K), (m) is odd, and the symbol is symmetric under (p\leftrightarrow k=m/p), then pairing complementary divisors gives

\[
\chi_4(p)+\chi_4(k)
=\chi_4(p)(1+\chi_4(m)).
\tag{5.2}
\]

The pair cancels for (m\equiv3\pmod4), but reinforces for (m\equiv1\pmod4). Hence complementary-divisor symmetry converts part of the character into arithmetic support; it does not yield uniform signed cancellation. This is consistent with the classical appearance of nonnegative two-square representation coefficients after the full self-dual transformation.

The tempting application of a one-dimensional second-derivative estimate to (e(\sqrt{Xm})) is invalid with the irregular coefficient (5.1) unless one first proves suitable partial-sum or bilinear control for that coefficient. Treating (a_L(m)) as an arbitrary (X^\varepsilon)-bounded weight would prove too much.

## 6. Smallest credible next lemma

The generic-band problem should not be phrased as “use the alternating signs of (\chi_4(p)).” A credible transformed target is a bilinear square-root phase estimate at (4.4): for the actual smooth symbol produced by Poisson,

\[
\boxed{
\sum_{p\asymp L\atop p\ {m odd}}\chi_4(p)
\sum_{k\asymp K}a_{p,k}e(\sqrt{Xpk})
\ll_\varepsilon X^{3/8+\varepsilon},
\qquad LK\asymp X^{1/2},
}
\tag{6.1}

uniformly for

\[
DX^{-1/4}\asymp L\le X^{1/4},
\qquad
K\asymp X^{1/2}/L.
\]

At the top block, (6.1) has exactly the scale needed after the prefactor in (4.3). Its proof must exploit either the actual divisor-fiber structure, the two-shift difference before Poisson, or a first-spacing theorem; a generic coefficient bound is not enough.

Before promoting (6.1), the project must derive (4.3) with all errors and check whether the symbol is symmetric, separable, and uniformly BV. The global-to-pointwise gap is avoided only if this is applied directly to (S_2(D;X)), not via a fourth moment.

## 7. Preliminary strategy decision

The exact generic-band algebra rules out a local residue-pairing shortcut. The B-process calculation identifies a more concrete top-block kernel and explains the Li--Yang height failure: the missing block is precisely the critical product regime (LK\asymp X^{1/2}), balanced at the endpoint. Round 4 should therefore decide between:

1. a direct two-shift/first-spacing estimate before product grouping;
2. a rigorously derived version of (6.1);
3. a no-go result showing that the transformed lemma is equivalent in strength to the original endpoint circle problem.

No pointwise M2 or Gauss-circle conclusion is claimed here.
