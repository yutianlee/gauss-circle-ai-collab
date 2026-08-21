# Round 108 hostile/source audit: metaplectic two-character energy

## 1. Result

**No-go result, with a logarithmic separation lemma.**  The proposed
Gaussian identity is correctly normalized, but only as an oscillatory
(tempered-distribution) identity.  Its nonzero-mode kernel has constant
modulus on the whole \(\tau\)-line and infinite total variation; the metric
density is a separate Dirac atom.  More strongly, if
\(c=X/(2gk)\), the sum of **all** metric-mode Fresnel operators is exactly

\[
 \mathcal M_{c,R}=\mathcal F^{-1}M_{W_R(cy^2)}\mathcal F.
\]

Thus the density term is the identity component and the complete
metaplectic mode sum is Fourier-conjugate to the original metric multiplier
\(W_R(\Lambda/k)\).  Each individual Fresnel operator is unitary and
invertible, while the complete windowed operator has exactly the same
\(L^2\)-capacity as the pre-existing window.  An exact second quadratic
transform likewise composes back to a chirp (with a caustic when its
Jacobian vanishes).  Gaussian linearization therefore supplies no part of
the required \(\rho^{-1/2}\) linear gain.

The feared algebraic separation-rank loss is not, by itself, a power loss.
On each fixed \((g,u)\) collar piece the accepted Round-77 physical amplitude
\(A_{ga,gb}(gu)\) is rank one in \((a,b)\); primitivity is exactly
Möbius-separable; and, for fixed \(k\), the reciprocal interval is the band

\[
 (1-k/J)^{-1}<\sqrt{b/a}<1+2k/J.
\]

On a finite block this band is a difference of two triangular masks and has
an exact separated Fourier expansion with coefficient \(\ell^1\)-cost
\(O(\log(2+N))\), where \(N\) is the number of ordered base points.  The
corresponding sharp Mellin kernel has a \(1/|\xi|\) tail, so a truncated
Mellin/triangular projection costs logarithmically, not by a positive power.
This does **not** produce smooth Mellin factors: the exact factors depend
jaggedly on ranks, \(k\), endpoints, and owners.

The character mechanism also disappears if it is postponed until the
positive Gram.  In the accepted notation \(F_a(q)\) is character-free and
\((-1)^q=\chi _4(a)\chi _4(a+2q)\).  After expansion of the Gram, the two
inserted character pairs cancel the Fejér sign identically, leaving no
residual character orthogonality.  A two-character theorem would therefore
have to act on each **linear** hard row before squaring.

Exact prior-owner reinsertion is automatically lawful only as a one-count
linear identity.  The accepted aggregate owned-energy bound does not supply
the blockwise projective/oscillatory norm needed to add the owners, apply a
source theorem to an enlarged fixed-\(K\) block, and subtract them after
absolute values or after the Gram.  Even granting such a new linear
completion lemma, none of the audited primary theta, Jacobi, half-integral
Kuznetsov, spectral-large-sieve, Poisson, or Voronoi formulas literally
accepts the complete moving symbol.  The first unsupported seam is the move
from the exact distributional Fresnel identity to an integrable direct
integral of genuine automorphic theta vectors; it fails both integrability
and automorphy hypotheses.  The requested \(\rho\)-gain remains wholly open.

## 2. Exact statement and hypotheses

Let \(e(z)=e^{2\pi i z}\), \(J=X^{1/2}\), \(b=a+2q\), \(h=ga\),
\(s=gb\), with \(a,b,g\) odd, \((a,q)=1\), and put

\[
 \Lambda_q={X(\sqrt b-\sqrt a)^2\over2},\qquad
 I_{a,q}=\left({J(\sqrt b-\sqrt a)\over2\sqrt a},
                    {J(\sqrt b-\sqrt a)\over\sqrt b}\right).
\]

The frozen character-free row and its target are

\[
 F_a(q)=\mathbf 1_{\rm residual}
 \sum_{\substack{g\ {\rm odd}\\k\in I_{a,q}}}
 \omega_{a,q,g,k}W_R(\Lambda_q/k)
 \int_{gb/4}^{ga}A^\circ_{ga,gb}(x)
 e\!\left(kx-J(\sqrt{gb}-\sqrt{ga})\sqrt x\right)dx,
\]

\[
 \mathcal G_H^{\rm act}
 =\sum_{a,n}\left|\sum_{0\le j<H}(-1)^jF_a(n+j)\right|^2
 \ll_\varepsilon X^\varepsilon {H^2E_0\over\rho},
 \quad E_0\asymp LJD^2,
 \quad \rho={AJD^3\over L^3}>1,
 \quad H\le D.
\]

The following assertions are certified under precisely these finite-block
hypotheses.

1. For every nonzero integer metric mode \(r\), let
   \(\alpha=rX/(2gk)\) and

   \[
   K_{\alpha,x}(\tau)
   ={e(\operatorname {sgn}\alpha/8)\over\sqrt{2|\alpha|}}
   e\!\left(-{(J\sqrt x-\tau)^2\over4\alpha}\right).
   \]

   Then, in \(\mathcal S'(\mathbb R_\tau)\),

   \[
   e\!\left(-J(\sqrt s-\sqrt h)\sqrt x\right)e(r\Lambda_q/k)
   =\int_{\mathbb R}K_{\alpha,x}(\tau)
      e(\tau\sqrt h)e(-\tau\sqrt s)\,d\tau.
   \]

   For \(r=0\), the measure is instead
   \(\delta_{J\sqrt x}\), giving
   \(e(J\sqrt x\sqrt h)e(-J\sqrt x\sqrt s)\).  The nonzero kernel is
   not a finite complex measure: \(|K_{\alpha,x}(\tau)|
   =(2|\alpha|)^{-1/2}\) for every \(\tau\).

2. With the convention
   \(\mathcal Ff(y)=\int_{\mathbb R}f(t)e(ty)\,dt\), put

   \[
   K_\alpha(t)={e(\operatorname {sgn}\alpha/8)\over\sqrt{2|\alpha|}}
       e(-t^2/(4\alpha)),\quad
   T_\alpha f=K_\alpha*f,
   \]

   and define \(K_0=\delta_0\), \(T_0=I\).  Then

   \[
   \mathcal F(T_\alpha f)(y)=e(\alpha y^2)\mathcal Ff(y).
   \]

   Consequently, for \(c=X/(2gk)\),

   \[
   \mathcal M_{c,R}:=\sum_{r\in\mathbb Z}\widehat W_R(r)T_{rc}
   =\mathcal F^{-1}M_{W_R(cy^2)}\mathcal F,
   \]

   where \(\widehat W_R(0)=\mu_R\).  The smoothness of \(W_R\) makes
   the operator series convergent, and

   \[
   \|\mathcal M_{c,R}f\|_2^2
   =\int_{\mathbb R}|W_R(cy^2)|^2|\mathcal Ff(y)|^2\,dy.
   \]

   At the actual \(y=\sqrt s-\sqrt h\), \(cy^2=\Lambda_q/k\).

3. For a second quadratic chirp \(e(\beta\tau^2)\) and
   \(\gamma=1-4\alpha\beta\ne0\), symmetric Fresnel regularization gives

   \[
   \int_{\mathbb R}K_{\alpha,x}(\tau)e(\beta\tau^2)\,d\tau
   =\epsilon(\alpha,\beta)|\gamma|^{-1/2}
      e\!\left({Xx\beta\over\gamma}\right),
   \qquad |\epsilon(\alpha,\beta)|=1.
   \]

   At \(\gamma=0\) the quadratic coefficient vanishes and the formula has
   a distributional caustic; there is no uniform \(|\gamma|^{-1/2}\)-free
   bound through it.

4. On each accepted smooth collar piece, at fixed \((g,u)\), the physical
   factor \(A_{ga,gb}(gu)\) is rank one in \((a,b)\).  Moreover

   \[
   \mathbf 1_{(a,q)=1}
   =\sum_{d\mid a,\ d\mid q}\mu(d)
   =\sum_{d\mid a,\ d\mid b}\mu(d),
   \]

   because every such \(d\) is odd and \(b-a=2q\).  This costs at most a
   divisor factor on a fixed base variable.

5. Put \(z=k/J\).  Membership in \(I_{a,q}\) forces \(0<z<1\) and is
   equivalent, with the original strict endpoints, to

   \[
   (1-z)^{-1}<\sqrt{b/a}<1+2z.
   \]

   If the finite \(a\)- and \(b\)-grids have at most \(N\) points, its
   indicator has an exact representation

   \[
   \mathbf1_{k\in I_{a,q}}
     =\sum_\ell c_\ell(k)f_\ell(a,k)g_\ell(b,k),
   \quad |f_\ell|,|g_\ell|\le1,
   \quad \sum_\ell|c_\ell(k)|\ll\log(2+N).
   \]

   This is an arbitrary-coefficient/projective separation statement, not a
   smooth-symbol statement uniform in Mellin derivatives.

6. If \(\{P_\nu\}\) are the literal disjoint owner projectors, then
   \(F=\sum_\nu P_\nu F\) and, under an invertible transform \(U\),
   \(UF=\sum_\nu(UP_\nu U^{-1})UF\).  This preserves linear one-count,
   rank, complements, and projector norms.  No energy decomposition follows
   unless the Gram/shift operator commutes with the projectors or the cross
   terms are separately controlled.

7. Each Gaussian/Fourier mode is unitary on its natural \(L^2\) space and
   invertible.  Hence it cannot, for \(\rho>1\), imply a uniform contraction
   by \(\rho^{-1/2}\) on a transform-invariant class.  The complete mode sum
   is not generally unitary because it includes the window, but the exact
   functional calculus above shows that it is merely the original window
   under Fourier conjugation.  Any further saving must be a new
   actual-symbol estimate, not a property of the transform.

## 3. Proof, derivation, and primary-source hypothesis map

**Gaussian constant, density, nonlocality, and self-return.**  Completing
the square gives

\[
 -{t^2\over4\alpha}+ty
 =-{(t-2\alpha y)^2\over4\alpha}+\alpha y^2,
\]

while symmetric Fresnel integration gives

\[
 \int_{\mathbb R}e(-u^2/(4\alpha))\,du
 =\sqrt{2|\alpha|}\,e(-\operatorname {sgn}\alpha/8).
\]

This proves the displayed constant.  Taking
\(y=\sqrt s-\sqrt h\) and changing variables
\(t=J\sqrt x-\tau\) yields the stated two-factor identity, since
\(\alpha y^2=r\Lambda_q/k\).  Against a Schwartz test function the kernels
converge distributionally to \(\delta_{J\sqrt x}\) as \(\alpha\to0\), but
their total variation is infinite for every \(\alpha\ne0\).  Thus this is
not a dominated-convergence construction of the density mode, and there is
no lawful modulus truncation \(\tau\asymp J\sqrt x\) (or
\(\tau\asymp J\sqrt L\)): the apparent center is a phase center, not support.

There is nevertheless a lawful way to sum the modes without total
variation.  The same Gaussian identity says exactly that
\(\mathcal F K_\alpha(y)=e(\alpha y^2)\).  Hence convolution by
\(K_{rc}\) is the Fourier multiplier \(e(rcy^2)\), and summing with
\(\widehat W_R(r)\) gives

\[
 \mathcal F\mathcal M_{c,R}f(y)
 =\sum_r\widehat W_R(r)e(rcy^2)\mathcal Ff(y)
 =W_R(cy^2)\mathcal Ff(y).
\]

The \(r=0\) density is precisely \(\mu_R I\).  At
\(y=\sqrt s-\sqrt h\), this recovers \(W_R(\Lambda_q/k)\) exactly.  Thus
keeping density and discrepancies jointly makes the metaplectic proposal an
exact functional-calculus return to the original metric window.  Taking
absolute values mode by mode loses the cancellations that make this a
bounded operator, whereas treating the modes jointly creates no new
spectral capacity to exploit.

Completing the square once more after multiplying by \(e(\beta\tau^2)\)
gives quadratic coefficient \(-\gamma/(4\alpha)\), the Jacobian
\(|\gamma|^{-1/2}\), and residual phase \(e(Xx\beta/\gamma)\).  This proves
the carrier-composition formula and exposes \(\gamma=0\) as a caustic.  It
also gives an explicit metaplectic return, rather than a gain.  This is
consistent with Marklof's construction: the Shale--Weil operators are
unitary and \(R(i,\pi/2)\) is the Fourier transform
([Marklof, §§3.9--3.10](https://annals.math.princeton.edu/wp-content/uploads/annals-v158-n2-p02.pdf)).

**Two characters and their Gram cancellation.**  Since \(g,a,b\) are odd,

\[
 \chi_4(h)\chi_4(s)=\chi_4(g)^2\chi_4(a)\chi_4(b)
 =\chi_4(a)\chi_4(a+2q)=(-1)^q.
\]

Thus the linear sign can indeed be written as the product
\(\chi_4(h)e(\tau\sqrt h)\,\chi_4(s)e(-\tau\sqrt s)\).  But the expanded
accepted linear row is \(Q_a=\sum_q(-1)^qF_a(q)\), with \(F_a(q)\)
itself character-free.  Its expanded Gram contains pairs with shifts \(q\)
and \(q+s_0\), and the full sign is

\[
 (-1)^{s_0}
 \chi_4(a)\chi_4(a+2q+2s_0)
 \chi_4(a)\chi_4(a+2q)=1.
\]

Therefore the factorization is useful, if at all, only before the absolute
square; it is not a source of character orthogonality on the positive Gram.

**Triangular band and Mellin cost.**  For either inequality
\(y_j<c x_i\), rank the two finite sets \(\{y_j\}\) and \(\{cx_i\}\) in
one ordered list, breaking ties according to the required strict inequality.
If \(r_i,s_j\in\{0,\ldots,M-1\}\) are the resulting ranks, choose a cyclic
modulus \(P>2M\) and let \(u(d)=1\) for \(1\le d\le M\), and \(u(d)=0\)
for \(-M\le d\le0\).  Fourier inversion on \(\mathbb Z/P\mathbb Z\) gives

\[
 u(s_j-r_i)=\sum_{\ell\bmod P}\widehat u(\ell)
 e_P(\ell s_j)e_P(-\ell r_i).
\]

The geometric-series formula gives
\(|\widehat u(\ell)|\ll
\min(1,\|\ell/P\|^{-1}/P)\), hence
\(\sum_\ell|\widehat u(\ell)|\ll\log P\).  The ratio band is the
difference of the two nested triangular masks, so it has the same
logarithmic order.  Restricting to \(b=a+2q\) cannot increase this explicit
cost.  In logarithmic ratio coordinates, the Fourier/Mellin transform of a
Heaviside step is a delta term plus a principal-value \(1/(i\xi)\) term;
its truncated absolute integral is logarithmic and its untruncated absolute
integral diverges.  Thus there is no hidden power loss in exact finite
separation, but there is also no integrable smooth Mellin kernel.  The
classical logarithmic scale of the main triangular projection is
corroborated by the primary paper of
[Kwapień--Pełczyński](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/34/1/97410/the-main-triangle-projection-in-matrix-spaces-and-its-applications);
the upper bound used here is proved directly by the finite Fourier expansion.

**Owner completion and the corrected one-variable ledger.**  At a single
linear hard block, reinserting disjoint owners and the Round-77 equality,
nonstationary, and collar pieces once is an exact algebraic completion.
Möbius separation and a smooth \(b-a\) Fourier separation cost only
\(X^\varepsilon\), and completing the \(k\)-sum to a fixed dyadic \(K\)
can remove the sharp ratio mask if every complementary mode is genuinely
one of those owners.  Likewise, after \(x=gu\), extending the physical
\(u\)-range through its flat collars removes the moving inequalities
\(b/4<u<a\) only if the collar, entry/exit, equality, and nonstationary
pieces are restored exactly once.  The permitted accepted statement,
however, is only the aggregate identity

\[
 \mathcal E_L^\top=\mathcal E_{{\rm owned},L}
 +2\Re\sum_B\mathfrak Q_B,
 \qquad \mathcal E_{{\rm owned},L}\ll_\varepsilon L^2X^\varepsilon.
\]

It does not state the blockwise estimate for
\(\sum_B|\mathfrak Q_{B,{\rm owner}}|\), nor a projective/oscillatory
\(\tau\)-norm stable under adding and subtracting these pieces.  Dyadic
completion can replicate an owner unless a new linear one-count dictionary
is proved.  Consequently the proposed completion is plausible algebra at
the linear level but is **not licensed as an estimate** by the accepted
owner bound.  After the Fejér/zero-extension operator \(T_H\), generally
\(T_HP_\nu\ne P_\nu T_H\), and
\(\|T_H\sum P_\nu F\|_2^2\) contains uncontrolled cross terms.  Exact
Fourier conjugation preserves the projectors, but makes sharp owners
nonlocal Dirichlet-type kernels; point evaluation at a noninteger saddle is
not canonical.  Inserting an owner \(P_\nu\) into the exact functional
calculus replaces it by the conjugate
\(\mathcal FP_\nu\mathcal F^{-1}\) on the multiplier side.  Unless it
commutes with \(M_{W_R(cy^2)}\) and with the Fejér operator, the identity
does not split into owner energies.  The strongest mode-sum identity
therefore reinforces, rather than removes, the owner seam.

For the base-variable phase at fixed lift, the correct parameter is
\(T_g=\tau\sqrt g\).  In the accepted normalization its Poisson saddle is
\(a_*=4T_g^2/r^2\), and \(a\asymp A\) gives dual length

\[
 R_g\asymp {T_g\over\sqrt A}\asymp J{L\over A}=JG,
\]

not \(J\sqrt{L/A}\).  Plancherel leaves the coefficient mass at scale
\(A\).  This saddle ledger is itself conditional on controlling a relevant
\(\tau\)-range: the exact Fresnel distribution has no such support.  Thus
ordinary Poisson returns an \(A\)-mass vector of actual dual length
\(R_g\asymp JG\), and a generic large-sieve diagonal term cannot provide a
\(\rho\)-power.

**Literal primary-source maps.**  Each failure below is a failed theorem
hypothesis, not an assertion that no future theorem can treat the object.

| Primary result | Literal hypotheses/input | Exact failure for the moving actual symbol |
|---|---|---|
| [Marklof, §§4.2 and 4.4](https://annals.math.princeton.edu/wp-content/uploads/annals-v158-n2-p02.pdf), Jacobi theta and Poisson transformation | A fixed \(f\in\mathcal S(\mathbb R^k)\); the theta sum is over \(m\in\mathbb Z^k\) with quadratic lattice phase \(e(\tfrac12\|m-y\|^2u+m\cdot x)\).  The Jacobi transformation is proved by Poisson summation on this Schwartz function. | \(\Theta_{\chi_4}[v](\tau)=\sum_{n\ {\rm odd}}\chi_4(n)v(n)e(\tau\sqrt n)\) has square-root frequencies and a moving, owner-dependent weight.  It is not a Jacobi-group function with quadratic \(m^2\)-phase.  Reindexing \(n=m^2\) would retain only perfect squares, not the actual row.  The sharp rank factors and constant-modulus Fresnel density are not a fixed Schwartz input. |
| [Ahlgren--Andersen, Theorem 4.1](https://arxiv.org/pdf/1510.05191), half-integral Kuznetsov | \(\phi:[0,\infty)\to\mathbb C\) is \(C^4\), \(\phi(0)=\phi'(0)=0\), and \(\phi^{(j)}(x)\ll x^{-2-\varepsilon}\) for \(0\le j\le4\); \(m>0,n<0\).  The geometric input is the complete multiplier Kloosterman sum \(\sum_{c>0}S(m,n,c,\chi)c^{-1}\phi(4\pi\sqrt{\widetilde m|\widetilde n|}/c)\), and the output uses Fourier coefficients \(\rho_j(m)\rho_j(n)\) of a fixed weight-\(1/2\) Maass spectrum. | The actual block has no complete Kloosterman residue sum, modulus inverse, or fixed Bessel test depending only on \(\sqrt{|mn|}/c\); its \(\chi_4\) is not the paper's multiplier system, and its two factors are not \(\rho_j(m),\rho_j(n)\).  The signs \(e(\pm\tau\sqrt n)\) do not create automorphic positive/negative Fourier indices. |
| [Blomer--Corbett, Proposition 13](https://arxiv.org/pdf/1912.07496), half-integral Kuznetsov | \(\kappa\in\{1/2,3/2\}\), \(m,n>0\); \(h\) is even, holomorphic in \(|\Im t|<2/3\), and \(h(t)\ll(1+|t|)^{-4}\) (with \(h(\pm i/4)=0\) for the displayed positive-index formula).  It relates fixed automorphic coefficients and Eisenstein coefficients to complete \(K_\kappa(m,n,c)\), \(4\mid c\), through a fixed Bessel transform. | The Fresnel \(\tau\)-weight has constant modulus, is neither decaying nor holomorphic as such a spectral test, and has a caustic under quadratic composition.  There are no \(b_j(m)b_j(n)\), Eisenstein coefficients, or complete \(K_\kappa\)-sum in the actual block.  The moving owners and ratio/projective factors cannot be absorbed into one fixed \(h\). |
| [Mocanu, Theorem 5](https://arxiv.org/pdf/1712.08174), Jacobi--Poincaré series | A fixed positive-definite even lattice \(L\), positive integral weight \(k>\operatorname{rk}(L)+2\), and fixed support pair \((D,r)\) with \(D<0\); the series is a coset average on the fixed Jacobi group and lies in the corresponding Jacobi cusp space, reproducing its Fourier coefficient. | The actual symbol has no fixed lattice index/discriminant, Jacobi modular law, elliptic law, or Jacobi-group coset average.  The variables \(g,k,x,r\), reciprocal band, owners, and Fejér shift move with \((a,b)\).  A notation \(\Theta_{\chi_4}\) does not establish Jacobi automorphy. |
| [Lam, Theorem 2.3](https://www.numdam.org/item/10.5802/jtnb.887.pdf), half-integral spectral large sieve | \(M\) is divisible by \(4\); \(k=1/2+\ell\), \(k-1/2\) even; \(K\le k\le K+G_{\rm sp}\), \(1\le G_{\rm sp}\le K^{1-\varepsilon}\); \(f\) ranges over an orthonormal holomorphic cusp-form basis and \(a_n\) is arbitrary on \([N,2N]\).  The theorem bounds \(\sum_{k,f}|\sum a_n\rho_f(n)|^2\) by \((MKN)^\varepsilon(MKG_{\rm sp}+N)\sum|a_n|^2\). | The actual row has no spectral average and no automorphic \(\rho_f(n)\).  Treating its values as arbitrary \(a_n\) still leaves the mandatory \(\rho_f(n)\) and gives only the diagonal-capacity right side.  On the corrected dual scale \(N=R_g\asymp JG\), with coefficient mass \(A\), the theorem would add capacity rather than the required \(\rho^{-1}\) energy factor. |
| [Blomer--Corbett, Lemma 10](https://arxiv.org/pdf/1912.07496), half-integral Voronoi | A fixed weight \(1/2\) or \(3/2\) Maass form on \(\Gamma_0(4)\) with Fourier coefficients \(b(n)\); \(4\mid c\), \((a,c)=1\); and a smooth compactly supported \(\phi\) away from zero.  It transforms \(\sum b(n)\sqrt{|n|}e(an/c)\phi(n)\) through specified Bessel kernels. | \(\chi_4(n)\) is not such a fixed form's coefficient \(b(n)\); no fixed rational additive twist/modulus is present; and the complete two-index owner/band symbol is not one smooth compactly supported \(\phi\).  The radical oscillation alone could be placed in a smooth \(\phi\) after localization, but that does not repair the coefficient or moving-symbol failures. |
| [Marklof, §4.4](https://annals.math.princeton.edu/wp-content/uploads/annals-v158-n2-p02.pdf), ordinary Poisson inside the theta law | Poisson is applied to a fixed Schwartz function, after which the result remains in the same Shale--Weil/Jacobi representation. | A distributional regularization or finite-rank treatment can justify a blockwise Poisson identity, but the complete sharp symbol is not the stated Schwartz input.  More decisively, summing all actual metric modes gives \(\mathcal F^{-1}M_{W_R(cy^2)}\mathcal F\) exactly, including the density identity component.  Inversion returns the original metric-windowed row with precisely the same \(L^2\)-capacity; this is not the missing estimate. |
| [Popov, Theorem 5](https://www.mathnet.ru/links/e3363d53e79dddf8f594b8a071b52fd2/rm10162_eng.pdf), truncated Gauss Voronoi formula | For \(x,N\ge3\), the complete radial coefficient is \(r_2(n)\), with cutoff \(n\le N\), and the theorem gives the explicit radial cosine sum plus a quantified truncation error. | It accepts the completed radial \(r_2(n)\)-sum, not the angular, primitive-ray, owner-weighted two-character symbol.  It provides a Hardy--Voronoi return identity and no estimate of the required internal Gram. |
| [Li--Yang, main repaired pointwise theorem](https://arxiv.org/pdf/2308.14859v2) | The imported conclusion is the global inclusive discrepancy bound \(P(X)\ll_\varepsilon X^{(3292+25\sqrt{1717})/13762+\varepsilon}\). | This theorem has no moving hard-block symbol as an input and proves neither the internal quarter-scale Gram nor a \(\rho\)-saving.  Its separably weighted double-exponential machinery, as scoped in the permitted source card, is not a literal substitute for the joint radical/owner packet. |

Thus the source audit proves precise non-applicability of these formulas; it
does not make a literature-wide claim about every possible future
vector-valued theorem.

## 4. First doubtful or unproved step

The first unproved step occurs immediately after the valid distributional
identity: the candidate replaces the full hard symbol by a “finite sum or an
integrable direct integral” of products of \(\Theta_{\chi_4}\).  Neither
alternative has been established.  The complete mode sum does have a lawful
\(L^2\)-operator interpretation, but that interpretation is exactly
\(\mathcal F^{-1}M_{W_R(cy^2)}\mathcal F\), so it returns the original
metric multiplier instead of producing a new theta object.

* The measure is not integrable: every nonzero
  \(K_{\alpha,x}(J\sqrt x-\tau)d\tau\) has infinite total variation and no
  compact effective support.  Symmetric Fresnel cancellation must be retained
  across the complete \(\tau\)-integral, together with the separate density
  atom.  Absolute Fubini, Minkowski in \(\tau\), or insertion into a decaying
  spectral test is unavailable.
* The displayed \(\Theta_{\chi_4}\) is not a genuine half-integral-weight or
  Jacobi theta function.  Its phase is \(\tau\sqrt n\), whereas genuine theta
  automorphy arises from a quadratic lattice phase in the lattice variable.
  Here \(\tau\) is a real Fourier variable, not an upper-half-plane modular
  parameter.  The Dirichlet character \(\chi_4\) does not supply the missing
  modular law.
* At the Gram level the character product is identically \(1\).  The new
  theorem must act on the signed linear row before squaring and remain stable
  under the Fejér shifts and zero extension.
* A linear full-\(K\), full-collar completion could remove several sharp
  masks, but the permitted accepted owner result controls their aggregate
  contribution in the original energy identity, not the blockwise
  projective/Fresnel norm required for add--transform--subtract.  That exact
  linear completion theorem is absent.

Accordingly the smallest still meaningful analytic target is a
character-sensitive, vector-valued inequality for the **complete linear hard
row**, before the Gram, with the density atom and every nonzero Fresnel mode
treated as one oscillatory distribution, and with either (i) the exact
logarithmic triangular mask and conjugated owners retained, or (ii) a newly
proved linear one-count completion lemma.  It must gain \(\rho^{-1/2}\) and
must be uniform through the \(\gamma=0\) caustic or isolate it with a proved
target-sized bound.  No audited source supplies that theorem.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `gaussian_constant_and_density_limit` | **PASS distributionally.**  Completion of squares gives exactly \(e(\operatorname{sgn}\alpha/8)/\sqrt{2|\alpha|}\), and the kernels tend to \(\delta_{J\sqrt x}\) on Schwartz tests.  **FAIL** for total-variation or dominated-convergence use. |
| `metric_density_discrepancy_jointness` | **PASS, exactly.**  The density is \(\mu_R I\), and the joint sum is \(\mathcal F^{-1}M_{W_R(cy^2)}\mathcal F\).  Deleting it changes the original metric multiplier. |
| `two_character_factorization` | **PASS only linearly.**  \(\chi_4(h)\chi_4(s)=(-1)^q\).  **FAIL as a positive-Gram mechanism:** the two character pairs and Fejér sign multiply to \(1\). |
| `actual_symbol_vs_arbitrary_coefficients` | **PASS guard.**  No arbitrary-coefficient replacement is used.  The exact band decomposition is only an algebraic multiplier statement; it does not turn the whole row into an arbitrary sequence theorem.  The fixed-\(q\) false analogue remains excluded. |
| `primitive_and_prior_owner_one_count` | **Primitive PASS:** exact Möbius separation costs \(X^\varepsilon\).  **Owners PASS only as a linear identity; UNSUPPORTED as a blockwise transformed estimate or Gram decomposition.** |
| `sharp_owner_conjugation_and_interpolation` | **PASS obstruction.**  Exact conjugation preserves owner algebra but makes sharp owners nonlocal.  Point evaluation at a noninteger saddle is noncanonical; the Fejér operator need not commute with owner projectors. |
| `q1_Pell_near_square_and_fourth_power` | **PASS hostile guard.**  These accepted controls forbid generic derivative-gap, parity, or Diophantine shortcuts.  Flat collars/prior owners mean they are not actual lower bounds and do not alter the no-go. |
| `transform_inversion_and_capacity` | **PASS exact equal-capacity return.**  \(T_\alpha\) is the unitary multiplier \(e(\alpha y^2)\), and \(\sum_r\widehat W_R(r)T_{rc}=\mathcal F^{-1}M_{W_R(cy^2)}\mathcal F\).  The quadratic composition formula returns a chirp with Jacobian \(|1-4\alpha\beta|^{-1/2}\) and a caustic.  No new \(\rho^{-1/2}\) contraction follows. |
| `rho_power_and_endpoint_ledger` | **Target not met.**  \(H^2E_0/\rho=H^2L^4/(AD)\), whereas the accepted fixed-\(q\) route has scale \(H^2DL^4/A\), a \(D^2\) deficit.  Positive linear capacity is \(L^2\sqrt\rho\), so the missing gain is exactly \(\rho^{-1/2}\).  The corrected base dual length is \(R_g\asymp JG\), with mass \(A\), not \(J\sqrt G\). |
| `primary_source_hypothesis_map` | **PASS audit; FAIL applicability.**  Every considered primary theorem has a literal failed automorphic-coefficient, Kloosterman/modulus, smoothing, spectral-decay, fixed-index, or moving-owner hypothesis. |
| `downstream_and_exponent_scope` | **PASS.**  No inference is made for the full hard cone, balanced/unbalanced packets, all-denominator endpoint, \(M9\!-\!M2\), \(M9\), or the \(1/4+\varepsilon\) target; the Li--Yang global exponent is not repurposed. |
| Nonlocal-\(\tau\) and caustic control | **PASS obstruction.**  There is no modulus support \(\tau\asymp J\sqrt L\), and any theorem requiring a compact/decaying spectral weight fails literally.  The \(\gamma=0\) singularity forbids a uniform naive second-chirp estimate. |
| Proposed fixed-\(K\) linear completion | **UNSUPPORTED from the permitted accepted bounds.**  Algebraic one-count is possible, but no blockwise add--transform--subtract norm is supplied.  Even if granted, the nonlocal Fresnel measure and automorphy failures remain. |

No numerical experiment was used; all outcomes are exact algebraic,
operator-theoretic, or source-hypothesis checks.

## 6. Dependencies and exact artifacts used

The local evidence was restricted to the brief's permitted context:

* `protocol.md`;
* `state/proof_obligations.yml` and `state/active_campaign.yml`;
* `rounds/codex-managed/m9-m2-metaplectic-two-character-energy/briefs/two_character_spectral_source_hostile_audit.md`;
* `rounds/codex-managed/m9-m2-metaplectic-two-character-energy/derivation_packet.md`;
* `rounds/codex-managed/m9-m2-metaplectic-two-character-energy/candidates/conductor_metaplectic_two_character_core.md`;
* `rounds/codex-managed/m9-canonical-core-formalization/candidates/conductor_canonical_core_statements.md`;
* `rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/synthesis.md` (Round 80 density/discrepancy return);
* `rounds/codex-managed/m9-m2-polynomial-q-maximal-alternation/synthesis.md` (Round 105 primitive mask and carrier-level return);
* `rounds/codex-managed/m9-m2-dual-square-actual-symbol-transfer/synthesis.md` (Round 106 complete-Fresnel capacity and owner conjugation);
* `sources/popov_2024_voronoi_gauss.md` and `sources/li_yang_2023.md`.

Primary external sources actually checked are
[Marklof](https://annals.math.princeton.edu/wp-content/uploads/annals-v158-n2-p02.pdf),
[Ahlgren--Andersen](https://arxiv.org/pdf/1510.05191),
[Blomer--Corbett](https://arxiv.org/pdf/1912.07496),
[Lam](https://www.numdam.org/item/10.5802/jtnb.887.pdf),
[Mocanu](https://arxiv.org/pdf/1712.08174),
[Kwapień--Pełczyński](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/34/1/97410/the-main-triangle-projection-in-matrix-spaces-and-its-applications),
[Popov](https://www.mathnet.ru/links/e3363d53e79dddf8f594b8a071b52fd2/rm10162_eng.pdf),
and [Li--Yang v2](https://arxiv.org/pdf/2308.14859v2).  Only the theorem
hypotheses and transformations stated in those primary works were used; no
secondary summary is treated as mathematical authority.

## 7. Recommended state effect

**Revise the candidate; retain the main obligation open; no downstream
status change.**  Promote, at most, a scoped internal no-go package containing
the correctly normalized distributional Gaussian identity and density atom,
the nonfinite-TV/nonlocal-\(\tau\) warning, the exact functional calculus
\(\sum_r\widehat W_R(r)T_{rc}=\mathcal F^{-1}M_{W_R(cy^2)}\mathcal F\)
with density \(\mu_RI\), the quadratic composition and caustic formula,
equal \(L^2\)-capacity and inversion, the rank-one physical
profile, Möbius separation, the exact \(O(\log N)\) triangular-band
decomposition, linear-only owner one-count, the corrected
\(R_g\asymp JG\) dual length with mass \(A\), the exact disappearance of
\(\chi_4\)-orthogonality in the Gram, and the primary-source
non-applicability map.

Reject the formal “theta pairing” as a proof object and reject any claim that
unitarity, a generic spectral large sieve, or owner reinsertion supplies the
missing \(\rho\)-power.  The strictly smaller survivor is the complete signed
linear hard row before squaring, with the full Fresnel distribution plus
density and nonlocal conjugated owners (or a separately proved fixed-\(K\)
linear completion lemma).  It still requires a new actual-symbol theorem
giving \(\rho^{-1/2}\) at linear level.
