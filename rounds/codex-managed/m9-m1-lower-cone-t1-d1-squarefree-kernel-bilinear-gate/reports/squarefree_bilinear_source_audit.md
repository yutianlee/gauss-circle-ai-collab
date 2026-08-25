# Round 153 primary-source audit: squarefree-kernel bilinear sums

- Campaign: m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate
- Research round: 153
- Role: primary-source auditor
- Graph SHA-256: 9ffef2e30c99d83d02d28141834b585d02dd77483fa7bfd8e572d45d6985fcc1
- Source search current through: 25 August 2026
- Allocation used: 100% analytical/algebraic and primary-source verification; 0% numerical
- Recommended terminal label: squarefree_kernel_bilinear_no_go

## 1. Result

**Exact recombination and audited-source no-go.**  Put

\[
 N=\lfloor X\rfloor,\qquad R=X^{1/4},\qquad
 1\ll M\leq R^2,\qquad M^{449}\ll R^{780},
\tag{153.S1}
\]

and \(H_M=\lceil M^{1/4}\rceil\).  Exact Möbius inversion followed by
\(r=as\) gives

\[
 P_U^*=Q_U^*+O_\varepsilon(X^\varepsilon),
\tag{153.S2}
\]

where the only non-absolutely-safe term is the one-variable wave

\[
 Q_U^*=
 \sum_{b\ {\rm odd}}
 \chi _4(b)b^{-3/4}A_U(b)e(\sqrt{Nb})\,
 \mathbf 1_{\mathcal R_*}(b;1).
\tag{153.S3}
\]

Thus the direct post-inversion coefficient is retained exactly:
\(\chi _4(a^2b)=\chi _4(b)\), and the survivor in (153.S3) still carries
\(\chi _4(b)\).  No source match in this report drops or replaces that
coefficient.

No audited primary theorem proves

\[
 |Q_U^*|\ll_\varepsilon X^\varepsilon
\tag{153.S4}
\]

below \(M^{449}\asymp R^{780}\), and hence none proves the same bound for
\(P_U^*\) or an owner-complete strict subrange of (153.S1).  The strongest
source-legal theorem for the surviving ordinary square-root wave remains
the Bourgain/Tao--Trudgian--Yang exponent-pair input already audited in
Round 152:

\[
 |Q_U^*|
 \ll_\varepsilon
 \left(\frac{R^{780}}{M^{449}}\right)^{1/1592}X^\varepsilon.
\tag{153.S5}
\]

It reaches the target exactly at \(M^{449}\gg R^{780}\) and is not
target-sized in the frozen open range.

The closest bilinear phase theorem, Robert--Sargos Theorem 1, can retain
\(\mu(a)\) on the \((a,s)\)-side and the exact \(\chi _4(b)\) on the
\(b\)-side, but it requires a coefficient separated between those sides.
The literal actual-profile/defect coefficient at \(a^2bs^2\) is not
separable.  Even in an ideal unmasked separable model, its first printed
term becomes

\[
 R^{1/2}M^{-1/8}(AS)^{-1/4}
 \gg R^{1/2}M^{-1/4}
 \gg R^{59/898}
\tag{153.S6}
\]

on (153.S1).  Hence that theorem cannot prove the target even before the
mask mismatch.

The exact recombination is stronger than this bilinear source test: all
\(1<r<H_M\) cancel, all \(r\geq H_M\) are target-safe absolutely, and
\(r=1\) is precisely (153.S3).  The first open step is therefore an
improvement for the literal one-variable
\(\chi _4(b)e(\sqrt{Nb})\) actual-profile wave below the Round-152
boundary.  The absence of such a theorem in the search is not a literature
impossibility theorem and is not a signed lower bound.

## 2. Exact statement and hypotheses

### 2.1 Literal object, inversion, and recombined statement

The accepted large-defect survivor is

\[
 P_U^*=\sum_{\substack{\ell=\tau s^2\ {\rm retained}\\
 |k(\ell)^2-N\ell|>M^{3/4}\\
 1\leq s<H_M}}
 \chi _4(\tau)(\tau s^2)^{-3/4}A_U(\tau s^2)
 e(s\sqrt{N\tau}),
\tag{153.S7}
\]

where \(\tau\) is odd squarefree, \(s\) is odd, \(k(\ell)\) is the
accepted unique nearest integer to \(\sqrt{N\ell}\), and \(A_U\) is the
literal zero-extended actual profile.  The inherited norm is

\[
 \|A_U\|_\infty+\operatorname {Var}A_U
 \ll_\varepsilon X^\varepsilon.
\tag{153.S8}
\]

The scalar \(B_{1,U}(1)\) remains outside the wave and has
\(O_\varepsilon(X^\varepsilon)\) size.  Exact squares, the small-defect
range, \(s\geq H_M\), bounded \(M\), and \(M^{449}\gg R^{780}\) remain
separate inherited owners.

Insert

\[
 \mu^2(\tau)=\sum_{a^2\mid\tau}\mu(a),\qquad \tau=a^2b.
\tag{153.S9}
\]

Since every variable is odd,

\[
 \chi _4(a^2b)=\chi _4(b),\qquad
 (a^2bs^2)^{-3/4}=a^{-3/2}b^{-3/4}s^{-3/2},
\qquad
 e(s\sqrt{Na^2b})=e(as\sqrt{Nb}).
\tag{153.S10}
\]

Thus, with every literal profile component, endpoint, transition,
nearest-integer convention, and strict defect mask retained,

\[
 P_U^*=\sum_{s,a,b\ {\rm odd}}
 \mu(a)\chi _4(b)(a^2bs^2)^{-3/4}
 A_U(a^2bs^2)e(as\sqrt{Nb})
 \mathbf 1_{\mathcal R_*}(a^2bs^2;s).
\tag{153.S11}
\]

Set \(r=as\).  The exact divisor coefficient is

\[
 c_{H_M}(r)=
 \sum_{\substack{s\mid r\\s<H_M}}\mu(r/s).
\tag{153.S12}
\]

The independently checked literal reindexing makes the remaining profile,
defect, and support factor a function of \(r^2b\); hence

\[
 P_U^*=
 \sum_{r,b\ {\rm odd}}c_{H_M}(r)\chi _4(b)(r^2b)^{-3/4}
 A_U(r^2b)e(r\sqrt{Nb})\mathbf 1_{\mathcal R_*}(r^2b).
\tag{153.S13}
\]

For \(r<H_M\), all divisors of \(r\) occur in (153.S12), so

\[
 c_{H_M}(r)=\sum_{d\mid r}\mu(d)=\mathbf 1_{r=1}.
\tag{153.S14}
\]

Equations (153.S13)--(153.S14) give the survivor (153.S3); Section 3.1
prices the \(r\geq H_M\) remainder.

### 2.2 The exact one-variable source boundary

Jean Bourgain,
[*Decoupling, exponential sums and the Riemann zeta function*](https://arxiv.org/html/1408.5794v2),
Theorem 6, proves that

\[
 \left(\frac{13}{84}+\varepsilon,
       \frac{55}{84}+\varepsilon\right)
\tag{153.S15}
\]

is an exponent pair.  Terence Tao, Tim Trudgian, and Andrew Yang,
[*New exponent pairs, zero density estimates, and zero additive energy
estimates: a systematic approach*](https://arxiv.org/html/2501.16779v1),
Definitions 11--12 formulate exponent-pair bounds uniformly on every
proper subinterval, Lemma 13 gives the \(B\)-process, Lemma 14 gives
Sargos's \(D\)-process, and Lemma 15 identifies the resulting global
exponent-pair condition.  Their exact transformations are

\[
 B(k,\lambda)=(\lambda-\tfrac12,k+\tfrac12)
\tag{153.S16}
\]

and

\[
 D(k,\lambda)=
 \left(
 \frac{5k+\lambda+2}{8(5k+3\lambda+2)},
 \frac{29k+21\lambda+10}{8(5k+3\lambda+2)}
 \right).
\tag{153.S17}
\]

Consequently

\[
 D\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{18}{199},\frac{593}{796}\right),
\qquad
 BD\left(\frac{13}{84},\frac{55}{84}\right)
 =\left(\frac{195}{796},\frac{235}{398}\right).
\tag{153.S18}
\]

For the ordinary phase \(e(\sqrt{N b})\), \(b\asymp M\), the phase
parameter is \(T\asymp\sqrt{NM}=R^2M^{1/2}\), and \(T/M\gg R\) throughout
\(M\leq R^2\).  The source hypotheses therefore hold on every proper
component.  Exact residue splitting keeps \(\chi _4(b)\), and Abel
summation inserts the literal zero-extended profile using (153.S8).
For a general exponent pair \((k,\lambda)\) this gives

\[
 |Q_U^*|\ll_\varepsilon
 R^{2k}M^{\lambda-k/2-3/4}X^\varepsilon
\tag{153.S19}
\]

after restoring the already target-safe pruned pieces.  Substitution of
(153.S18) is exactly (153.S5).  There is no character modulus average,
main term, exceptional spectrum, or omitted endpoint in this source
application.  Its first failed power condition below the boundary is
simply \(M^{449}\gg R^{780}\).

### 2.3 Robert--Sargos trilinear and spacing cards

O. Robert and P. Sargos,
[*Three-dimensional exponential sums with monomials*](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf),
Theorem 1, considers

\[
 S_0=\sum_{h\asymp H}\sum_{n\asymp K}\alpha(h,n)
 \sum_{m\asymp L}\beta(m)
 e\left(
 \frac{Yh^{\beta_0}n^{\gamma_0}m^{\alpha_0}}
 {H^{\beta_0}K^{\gamma_0}L^{\alpha_0}}
 \right).
\tag{153.S20}
\]

The exact hypotheses are: \(H,K,L\) positive integers, \(Y>1\),
\(|\alpha(h,n)|,|\beta(m)|\leq1\), fixed real exponents, and

\[
 \alpha_0(\alpha_0-1)\beta_0\gamma_0\neq0.
\tag{153.S21}
\]

It is pointwise, has hard dyadic ranges, no parameter average, and no
coupled mask.  The conclusion is

\[
 S_0\ll_\varepsilon(HKL)^{1+\varepsilon}
 \left\{
 \left(\frac{Y}{HKL^2}\right)^{1/4}
 +(HK)^{-1/4}+L^{-1/2}+Y^{-1/2}
 \right\}.
\tag{153.S22}
\]

Theorem 2, for fixed \(\alpha_0\neq0,1\), bounds the number of
\(m_i\in(M_0,2M_0]\) satisfying

\[
 |m_1^{\alpha_0}+m_2^{\alpha_0}
 -m_3^{\alpha_0}-m_4^{\alpha_0}|
 \leq\delta M_0^{\alpha_0}
\tag{153.S23}
\]

by

\[
 O_\varepsilon(M_0^{2+\varepsilon}
 +\delta M_0^{4+\varepsilon}).
\tag{153.S24}
\]

The \(M_0^2\) term is the diagonal scale.  Lemma 8 is the
Bombieri--Iwaniec double large sieve: its RHS is
\(Y^{1/2}\mathcal B_1^{1/2}\mathcal B_2^{1/2}\), where the two
\(\mathcal B_i\) count pairs spaced by at most \(Y^{-1}\).

Before recombination, the only legal assignment is

\[
 (H,K,L,Y;\beta_0,\gamma_0,\alpha_0)
 =(A,S,B,\mathcal T;1,1,1/2),
\qquad
 \mathcal T=AS\sqrt{NB}\asymp R^2M^{1/2}.
\tag{153.S25}
\]

The separated coefficients can contain \(\mu(a)\) and the exact
\(\chi _4(b)\).  The source mismatch is the coupled actual-profile/defect
factor at \(a^2bs^2\).  Placing \(a\) or \(s\) in the differenced
\(m\)-slot would give the forbidden exponent \(\alpha_0=1\).  After exact
recombination, the non-safe part has \(r=1\) and is one-variable, so the
trilinear theorem has no Möbius range left to exploit.

### 2.4 Other Möbius, character, and squarefree source cards

E. Kowalski, O. Robert, and J. Wu,
[*Small gaps in coefficients of L-functions and B-free numbers in short
intervals*](https://ems.press/content/serial-article-files/38194),
Proposition 5, treats separated bounded coefficients in

\[
 S(P,Q)=\sum_{m\asymp P}\sum_{n\asymp Q}
 \varphi_m\psi_n
 e\left(\frac{Y m^\alpha n^\beta}{P^\alpha Q^\beta}\right),
\tag{153.S26}
\]

under \(\alpha,\beta\in\mathbb R\setminus\{0,1\}\), and proves

\[
 S(P,Q)\ll_\varepsilon
 \{(YP^6Q^6)^{1/8}+P^{1/2}Q+PQ^{3/4}
 +Y^{-1/2}PQ\}(PQ)^\varepsilon.
\tag{153.S27}
\]

For fixed \(s\), the literal exponents are \(1\) in \(a\) and \(1/2\) in
\(b\); either ordering violates the printed exclusion of exponent one.
The source has no mask or exceptional case that repairs this.

K. Matomäki and J. Teräväinen,
[*On the Möbius function in all short intervals*](https://arxiv.org/html/1911.09076v2),
Theorem 1.5, proves, for fixed \(\theta>3/5\), uniformly in
\(\alpha\in\mathbb R\),

\[
 \sum_{x<n\leq x+H}\mu(n)e(\alpha n)
 =O\left(\frac{H}{(\log x)^{1/3-\varepsilon}}\right),
 \qquad H\geq x^\theta.
\tag{153.S28}
\]

It supplies only logarithmic cancellation, does not apply at \(a=1\),
has no \(b\)-average or product mask, and an absolute sum over \(b\)
discards rather than exploits \(\chi _4(b)\).

D. R. Heath-Brown,
[*A mean value estimate for real character sums*](https://matwbn.icm.edu.pl/ksiazki/aa/aa72/aa7234.pdf),
Theorem 1, states

\[
 \sum_{m\leq M_0}^{*}
 \left|\sum_{n\leq N_0}^{*}c_n
 \left(\frac{n}{m}\right)\right|^2
 \ll_\varepsilon(M_0N_0)^\varepsilon(M_0+N_0)
 \sum_{n\leq N_0}^{*}|c_n|^2,
\tag{153.S29}
\]

where both stars mean positive odd squarefree integers.  Its positive
diagonal is the \(M_0+N_0\) term.  It averages a varying Jacobi-symbol
family; (153.S11) instead has one fixed \(\chi _4(b)\), unrestricted \(b\)
after inversion, an Archimedean square-root phase, and no modulus average.

J.-C. Schlage-Puchta,
[*The exponential sum over squarefree integers*](https://arxiv.org/html/1105.1616v1),
Theorem 1, proves

\[
 \sum_{n\leq Y_0}\mu^2(n)e(\alpha n)
 \ll Y_0^{1+\varepsilon}Q^{-1}
\tag{153.S30}
\]

on the explicitly defined minor arcs, for \(Q\leq Y_0^{1/2}\).
Theorem 3 gives
\(O(Y_0^{1+\varepsilon}q^{-1}+Y_0^\varepsilon q)\) under
\(|q\alpha-a|\leq q^{-1}\).  The major arcs are exceptional.  The phase
is linear, and neither theorem supplies the ordinary square-root phase,
the growing parameter \(\sqrt N\), or the actual profile/mask.  A finite
additive decomposition can preserve \(\chi _4\), but it cannot repair
those phase and weight mismatches.

### 2.5 Nonlinear twists and current bilinear square roots

J. Kaczorowski and A. Perelli,
[*Twists and resonance of L-functions, I*](https://arxiv.org/html/1304.4734v1),
define the standard twist of a fixed degree-\(d\) extended-Selberg-class
function by

\[
 F(s,\alpha)=\sum_{n\geq1}a(n)n^{-s}e(-\alpha n^{1/d}).
\tag{153.S31}
\]

Theorems 1--5 concern analytic continuation, polar structure, and growth,
with constants allowed to depend on the fixed twist parameter.  A
degree-one standard twist is linear; a square-root standard twist requires
degree two.  Moreover

\[
 \sum_{n\geq1}\frac{\mu^2(n)\chi _4(n)}{n^s}
 =\frac{L(s,\chi _4)}{L(2s,\chi _4^2)}
\tag{153.S32}
\]

is not the coefficient series of the required fixed degree-two
\(L\)-function.  Analytic continuation supplies no uniform finite-sum
estimate at \(\alpha=\sqrt N\), scale \(M\), with the literal endpoints.

Their 2026 continuation,
[*Multiple standard twists of L-functions*](https://arxiv.org/html/2603.13885v1),
condition (1.3), imposes
\(\sum_{\nu=1}^{J}d_\nu\kappa_\nu=1\), and Theorem 1 is stated for
\(J\geq2\).  It concerns continuation of an infinite multiple Dirichlet
series, not a finite bilinear bound.  A one-function degree-one
specialization again forces exponent one.

The current title-nearest result is S. Baier,
[*On certain bilinear sums with modular square roots and
applications*](https://arxiv.org/html/2601.15448v4), revised 3 July 2026.
Theorem 2 treats

\[
 \sum_{|l|\leq L}\sum_{1\leq m\leq M_0}
 \alpha_l\beta_m e_r(l\sqrt{jm})e(lf(m)),
\tag{153.S33}
\]

under \((r,j)=1\), \(1\leq L,M_0\leq r\),
\(|f'|\leq F\leq L^{-1}\), and

\[
 1\leq H\leq\min\{(LF)^{-1},M_0\}.
\tag{153.S34}
\]

It proves

\[
 \ll\left(
 H^{-1/2}L^{1/2}M_0+H^{1/4}L^{1/4}M_0
 +H^{-1/4}L^{1/4}M_0^{3/4}r^{1/4}
 \right)
 \|\boldsymbol\alpha\|_2\|\boldsymbol\beta\|_\infty r^\varepsilon.
\tag{153.S35}
\]

The paper expressly states that \(\sqrt{jm}\) denotes modular square
roots, not the ordinary positive real square root.  There is no modulus,
modular-root fibre, or \(e_r\)-phase in (153.S3), so Theorem 2 has no
literal translation.  Its \(r^{1/4}\) term is also not an \(R,M\) saving.

## 3. Proof or derivation

### 3.1 Exact \(r=as\) collapse and the absolute remainder

Equations (153.S9)--(153.S13) are signed identities; no triangle
inequality has yet been used.  In particular, \(\mu(1)=1\) is retained,
and \(\chi _4(b)\) is the direct weight on every post-inversion term.
For \(r<H_M\), Möbius inversion is complete and (153.S14) proves exact
cancellation of every \(1<r<H_M\).

For \(r\geq H_M\), use

\[
 |c_{H_M}(r)|\leq\tau(r)\ll_\varepsilon r^\varepsilon.
\tag{153.S36}
\]

On a dyadic block \(r\asymp C\), \(b\asymp B\), the literal support gives

\[
 C^2B\asymp M,\qquad CB\asymp\frac{M}{C}.
\tag{153.S37}
\]

The actual weight is \(M^{-3/4}\), so (153.S8), (153.S36), and the raw
count give

\[
 \sum_{\substack{r\asymp C,\ b\asymp B\\r\geq H_M}}
 |c_{H_M}(r)|(r^2b)^{-3/4}|A_U(r^2b)|
 \ll_\varepsilon \frac{M^{1/4}}{C}X^\varepsilon.
\tag{153.S38}
\]

Summing dyadically over
\(H_M\leq C\ll M^{1/2}\) is geometric:

\[
 \sum_{C\geq H_M}^{\rm dyadic}\frac{M^{1/4}}{C}
 \ll\frac{M^{1/4}}{H_M}\ll1.
\tag{153.S39}
\]

The mask only deletes terms in this absolute estimate.  Therefore the
\(r\geq H_M\) part is \(O_\varepsilon(X^\varepsilon)\), proving
(153.S2).  This is an upper bound on an absolute remainder, not a lower
bound for the signed wave.

The \(r=1\) coefficient in (153.S14) is exactly one.  Substitution into
(153.S13) gives (153.S3), including the compulsory \(s=1\) seam, the
fixed character \(\chi _4(b)\), the actual zero extension, and the strict
large-defect mask.

### 3.2 Why the surviving one-variable wave remains below the source boundary

The accepted Round-152 pruning states

\[
 P_U=P_U^*+O_\varepsilon(X^\varepsilon).
\tag{153.S40}
\]

Combining (153.S2) and (153.S40) gives

\[
 Q_U^*=P_U+O_\varepsilon(X^\varepsilon).
\tag{153.S41}
\]

Thus the boundary-complete source estimate for the full actual-profile
one-variable wave applies to the survivor without pretending that the
hard defect indicator itself has small variation.  Equations
(153.S18)--(153.S19) give

\[
 |Q_U^*|
 \ll_\varepsilon
 R^{780/1592}M^{-449/1592}X^\varepsilon+X^\varepsilon.
\tag{153.S42}
\]

The first term is target-sized exactly when
\(M^{449}\gg R^{780}\).  In the open range it carries a positive power
loss.  The primary search found no theorem with all of the following
features simultaneously:

1. the ordinary positive square-root phase \(e(\sqrt{Nb})\);
2. the fixed coefficient \(\chi _4(b)\);
3. the growing parameter \(\sqrt N\) and length \(M\);
4. the literal actual profile, zero extension, endpoints, and inherited
   large-defect reduction; and
5. a power strictly stronger than (153.S42).

Accordingly, the answer to the conductor's explicit question is **no**:
none of the audited theorems estimates the surviving
\(\chi _4(b)e(\sqrt{Nb})\) actual-profile wave by
\(O_\varepsilon(X^\varepsilon)\) below
\(M^{449}\asymp R^{780}\).

### 3.3 Full bilinear power ledger and Robert--Sargos translation

Before recombination, on \(a\asymp A\), \(s\asymp S\),
\(b\asymp B\),

\[
 A^2BS^2\asymp M,\qquad
 ASB\asymp\frac{M}{AS},\qquad
 M^{-3/4}ASB\asymp\frac{M^{1/4}}{AS}.
\tag{153.S43}
\]

For fixed \(s\), the corresponding formulas are

\[
 A^2Bs^2\asymp M,\qquad
 AB\asymp\frac{M}{As^2},\qquad
 M^{-3/4}AB\asymp\frac{M^{1/4}}{As^2}.
\tag{153.S44}
\]

Hence absolute values are target-safe for \(AS\gg M^{1/4}\), or for
\(As^2\gg M^{1/4}\) at fixed \(s\).  These tails do not remove
\(A=S=1\).

Apply (153.S22), only as a formal power audit, to the more favourable
unmasked separated model (153.S25).  Since
\(ASB=M/(AS)\) and
\(\mathcal T=R^2M^{1/2}\), the four source terms, after the actual
\(M^{-3/4}\) weight, are

\[
 M^{-3/4}|S_0|
 \ll_\varepsilon X^\varepsilon
 \left\{
 R^{1/2}M^{-1/8}(AS)^{-1/4}
 +M^{1/4}(AS)^{-5/4}
 +M^{-1/4}
 +R^{-1}(AS)^{-1}
 \right\}.
\tag{153.S45}
\]

The first identity is

\[
 M^{-3/4}(ASB)
 \left(\frac{\mathcal T}{ASB^2}\right)^{1/4}
 =R^{1/2}M^{-1/8}(AS)^{-1/4}.
\tag{153.S46}
\]

Since \(B\gg1\) forces \(AS\ll M^{1/2}\),

\[
 R^{1/2}M^{-1/8}(AS)^{-1/4}
 \gg R^{1/2}M^{-1/4}.
\tag{153.S47}
\]

Using \(M^{449}\ll R^{780}\),

\[
 R^{1/2}M^{-1/4}
 \gg R^{1/2-195/449}=R^{59/898}.
\tag{153.S48}
\]

This is a lower bound for a term on the printed **upper-bound RHS**, so it
shows only that direct use of the theorem cannot yield the target.  It is
not a lower bound for \(S_0\), \(P_U^*\), or \(Q_U^*\).

### 3.4 Cauchy placement, diagonals, and surviving coefficients

For fixed \(s\), pull out the common dyadic weight and write

\[
 T_{A,B,s}=
 \sum_{a\asymp A}\sum_{b\asymp B}
 \mu(a)\chi _4(b)V_s(a,b)e(as\sqrt{Nb}),
\tag{153.S49}
\]

where \(V_s\) contains the normalized literal actual profile and mask.
Cauchy in \(a\) leaves correlations

\[
 \sum_{a\asymp A}\mu^2(a)
 \sum_{b_1,b_2\asymp B}
 \chi _4(b_1)\chi _4(b_2)
 V_s(a,b_1)\overline{V_s(a,b_2)}
 e\left(as\sqrt N(\sqrt{b_1}-\sqrt{b_2})\right).
\tag{153.S50}
\]

The \(b\)-character therefore survives exactly.  Its
\(b_1=b_2\) diagonal gives, after the actual weight,

\[
 M^{-3/4}A\sqrt B=\frac{M^{-1/4}}s,
\tag{153.S51}
\]

which is target-safe but does not control off-diagonal spacing.

Cauchy in \(b\) uses \(|\chi _4(b)|^2=1\) and leaves

\[
 \sum_{b\asymp B}\sum_{a_1,a_2\asymp A}
 \mu(a_1)\mu(a_2)
 V_s(a_1,b)\overline{V_s(a_2,b)}
 e\left(s\sqrt{Nb}(a_1-a_2)\right).
\tag{153.S52}
\]

Here the Möbius signs survive in the positive placement.  The
\(a_1=a_2\) diagonal costs

\[
 M^{-3/4}B\sqrt A
 =M^{1/4}A^{-3/2}s^{-2},
\tag{153.S53}
\]

which is \(M^{1/4}\) at \(A=s=1\).  Thus a Cauchy-first bilinear proof
must overcome an explicit diagonal at the same seam that exact
recombination isolates as (153.S3).

### 3.5 Exact and near frequency collisions

The frequencies after (153.S50) are

\[
 \theta_b=s\sqrt{Nb}\pmod1.
\tag{153.S54}
\]

Suppose \(b_1\neq b_2\) and

\[
 s\sqrt N(\sqrt{b_1}-\sqrt{b_2})=j\in\mathbb Z.
\tag{153.S55}
\]

Then
\(\sqrt{Nb_1}-\sqrt{Nb_2}=j/s\in\mathbb Q\), and

\[
 \sqrt{Nb_1}+\sqrt{Nb_2}
 =\frac{N(b_1-b_2)}{j/s}\in\mathbb Q.
\tag{153.S56}
\]

Both square roots are rational, hence integral:

\[
 Nb_1=\square,\qquad Nb_2=\square.
\tag{153.S57}
\]

Write \(N=2^\nu n_0\), \(n_0\) odd, and let \(d_N\) be the squarefree
kernel of \(N\).  If \(\nu\) is odd, \(d_N\) is even and (153.S57) has
no odd \(b_i\).  If \(\nu\) is even, then
\(b_i=d_Nr_i^2\) is the possible distinct collision ray.  But then

\[
 Na^2b_i s^2=(as)^2Nb_i=\square,
\tag{153.S58}
\]

so the nearest-integer defect is zero.  The strict large-defect mask
removes every distinct exact collision.  Only \(b_1=b_2\) remains inside
the literal survivor, for either parity of \(N\).

Near collisions remain.  Partition the unit circle into \(O(A)\) arcs of
length \(1/A\).  Occupancy Cauchy--Schwarz gives

\[
 \#\{(b_1,b_2):
 \|\theta_{b_1}-\theta_{b_2}\|\leq A^{-1}\}
 \gg \frac{B^2}{A},
\tag{153.S59}
\]

up to the harmless use of adjacent arcs.  The largest local multiplicity
is at least \(B/A\) when \(B>A\), and at \(A=1\) all frequencies lie in
one sampling cell.  This is positive capacity only.  It is not a signed
lower bound and does not permit deletion of
\(\chi _4(b_1)\chi _4(b_2)\).  Robert--Sargos Theorem 2 prices a
separable four-point spacing problem, but its resulting power is already
the insufficient bound (153.S45).

## 4. First doubtful or unproved step

There is no doubtful step in the exact divisor identity
(153.S12)--(153.S14) or in the absolute tail estimate
(153.S36)--(153.S39), given the frozen literal reindexing and inherited
profile support.  They prove the \(r=as\) collapse and leave (153.S3).

The first unproved analytic statement is (153.S4) in the range
(153.S1).  The first failed inequality for the strongest audited
one-variable source is

\[
 \left(\frac{R^{780}}{M^{449}}\right)^{1/1592}
 \ll X^\varepsilon,
\tag{153.S60}
\]

which holds only on the already owned side
\(M^{449}\gg R^{780}\).  A continuation must either improve the relevant
exponent-pair line or exploit the fixed \(\chi _4\), the large-defect
structure, or another arithmetic feature while retaining the literal
profile and all endpoints.

If one insists on working before exact recombination, the first source
hypothesis gap is the reduction of the coupled coefficient

\[
 \mu(a)\chi _4(b)
 A_U(a^2bs^2)\mathbf1_{\mathcal R_*}(a^2bs^2;s)
\tag{153.S61}
\]

to the separated class of Robert--Sargos Theorem 1.  Even if that gap
were filled, (153.S45)--(153.S48) show a further power loss.  Any useful
Cauchy/spacing substitute must retain the arithmetic factors in
(153.S50) or (153.S52), price both diagonals, and be uniform at
\(A=S=1\).

No inference of impossibility is made from the unsuccessful source
search.  The open object is a concrete one-variable estimate, not a claim
that future bilinear, spectral, or spacing methods cannot work.

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| literal_Pstar_survivor | **GREEN.** Equations (153.S7), (153.S11), and (153.S13) retain the exact large-defect survivor and do not reinsert exact squares, small defect, or the large-\(s\) tail. |
| owned_range_and_owner_exclusion | **GREEN.** The audit is confined to (153.S1). Bounded \(M\), \(M^{449}\gg R^{780}\), and all prior owners are excluded; no new strict range is claimed. |
| squarefree_kernel_uniqueness | **GREEN.** The incoming \(\ell=\tau s^2\) has its unique odd squarefree kernel, while (153.S9) is an exact signed expansion, not a competing canonical factorization. |
| exact_Mobius_inversion | **GREEN.** Every \(a\), including \(a=1\), its sign, weight, phase, and the exact direct coefficient \(\chi _4(b)\) occur in (153.S9)--(153.S13). The \(r=as\) recombination is (153.S12). |
| a1_short_divisor_seam | **GREEN/open obstruction.** Complete Möbius recombination leaves \(r=1\), exactly the one-variable wave (153.S3). It is not discarded or bounded by the old theorem below its boundary. |
| dyadic_A_B_s_power_ledger | **GREEN.** Fixed-\(s\), dyadic-\(S\), and recombined-\(r\) counts and weights are (153.S37)--(153.S44); the full Robert--Sargos translation is (153.S45). |
| actual_profile_mask_and_B11 | **GREEN.** The actual profile, zero extension, transitions, endpoints, nearest integer, and strict mask remain literal. \(B_{1,U}(1)\) stays outside and costs only \(X^\varepsilon\) after a wave bound. |
| Cauchy_coefficient_survival | **GREEN.** Cauchy in \(a\) retains \(\chi _4(b_1)\chi _4(b_2)\), (153.S50); Cauchy in \(b\) retains \(\mu(a_1)\mu(a_2)\), (153.S52). |
| diagonal_and_pigeonhole_capacity | **GREEN/open split.** The exact diagonals are (153.S51) and (153.S53); the forced near-pair capacity is (153.S59). None is called a signed lower bound. |
| exact_and_near_frequency_collisions | **GREEN/open split.** Distinct exact collisions are classified in (153.S55)--(153.S58) and removed by the literal mask for both parities of \(N\). Character-weighted near collisions remain open. |
| TypeI_TypeII_signed_bilinear_target | **NO NEW TARGET.** Exact recombination makes the \(r\geq H_M\) Type-I/II remainder absolutely safe and leaves (153.S3). No audited signed theorem bounds that survivor below (153.S60). |
| source_theorem_bilinear_match | **NO MATCH.** Robert--Sargos keeps \(\mu(a)\chi _4(b)\) but fails the coupled-mask hypothesis and the power test. Every other bilinear theorem has an earlier phase, exponent, character-family, average, or coefficient mismatch. |
| absolute_capacity_vs_signed_sum | **GREEN.** Equations (153.S38)--(153.S39), (153.S43)--(153.S44), and (153.S59) are explicitly absolute capacities or positive energies. No signed lower bound is asserted. |
| N_parity_endpoints_and_transitions | **GREEN.** Both \(2\)-adic parities of \(N\) are covered in (153.S57)--(153.S58). Strict inequalities, ceiling endpoint, hard dyadic endpoints, zero extension, and all profile transitions remain literal. |
| D_L_generic_tge2_cross_and_downstream_scope | **GREEN.** The result concerns only the actual \(D=d=L=1\), small-square-factor, large-defect scalar. It does not promote \(D>1\), \(L>1\), the generic sector, any original \(t\geq2\) layer, the Round-138 cross owner, M1/M2, endpoint assembly, M9, the bridge, target, or either global exponent. |

No numerical experiment or computational certification was used.

## 6. Dependencies and exact artifacts used

Repository artifacts inspected were the task brief and every item in its
permitted context:

1. protocol.md;
2. state/proof_obligations.yml;
3. state/active_campaign.yml;
4. strategy/round153_d1_squarefree_kernel_bilinear_strategy.md;
5. rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/barrier_packet.md;
6. rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reports/square_root_wave_source_audit.md;
7. rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reviews/source_conductor_round152_final.md;
8. sources/tao_trudgian_yang_2025.md;
9. sources/bourgain_2017_exponent_pair.md; and
10. rounds/codex-managed/m9-m1-lower-cone-t1-d1-squarefree-kernel-bilinear-gate/briefs/squarefree_bilinear_source_audit.md.

Primary sources checked directly were:

1. Jean Bourgain,
   [*Decoupling, exponential sums and the Riemann zeta function*](https://arxiv.org/html/1408.5794v2),
   Theorem 6;
2. Terence Tao, Tim Trudgian, and Andrew Yang,
   [*New exponent pairs, zero density estimates, and zero additive energy
   estimates: a systematic approach*](https://arxiv.org/html/2501.16779v1),
   Definitions 11--12, Lemmas 13--15, and Table 1;
3. O. Robert and P. Sargos,
   [*Three-dimensional exponential sums with monomials*](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf),
   Theorems 1--2 and Lemma 8;
4. E. Kowalski, O. Robert, and J. Wu,
   [*Small gaps in coefficients of L-functions and B-free numbers in short
   intervals*](https://ems.press/content/serial-article-files/38194),
   Proposition 5;
5. K. Matomäki and J. Teräväinen,
   [*On the Möbius function in all short intervals*](https://arxiv.org/html/1911.09076v2),
   Theorem 1.5;
6. D. R. Heath-Brown,
   [*A mean value estimate for real character sums*](https://matwbn.icm.edu.pl/ksiazki/aa/aa72/aa7234.pdf),
   Theorem 1;
7. J.-C. Schlage-Puchta,
   [*The exponential sum over squarefree integers*](https://arxiv.org/html/1105.1616v1),
   Theorems 1 and 3;
8. J. Kaczorowski and A. Perelli,
   [*Twists and resonance of L-functions, I*](https://arxiv.org/html/1304.4734v1),
   Theorems 1--5;
9. J. Kaczorowski and A. Perelli,
   [*Multiple standard twists of L-functions*](https://arxiv.org/html/2603.13885v1),
   Theorem 1 and condition (1.3); and
10. S. Baier,
    [*On certain bilinear sums with modular square roots and
    applications*](https://arxiv.org/html/2601.15448v4), Theorem 2.

The search also checked the 2026 follow-ups
[*On bilinear sums with modular square roots and applications
II*](https://arxiv.org/abs/2603.00768) and
[*A note on bilinear sums with modular square
roots*](https://arxiv.org/abs/2605.01635).  Their modular setting does
not change the literal mismatch in (153.S33)--(153.S35).  Every theorem
statement used above is from a primary source.  Every
\(R,M,A,B,s,r\) specialization, recombination, collision classification,
and power comparison is derived here or is an explicitly frozen incoming
identity.

No state file, source card, candidate, review, control, synthesis, or proof
draft was edited.

## 7. Recommended state effect

**Retain the exact recombination and source obstruction; make no graph
promotion from this report.**

1. Record the source-audit verdict squarefree_kernel_bilinear_no_go:
   exact \(r=as\) recombination reduces \(P_U^*\) to (153.S3) plus an
   absolute \(O_\varepsilon(X^\varepsilon)\) remainder.
2. Record explicitly that no audited theorem proves the surviving
   \(\chi _4(b)e(\sqrt{Nb})\) actual-profile wave below
   \(M^{449}\asymp R^{780}\).  The best licensed bound is (153.S42).
3. Record the first one-variable open step as an improvement of
   (153.S60).  If a pre-recombination bilinear route is retained for
   future work, its first source mismatch is the coupled coefficient
   (153.S61), and its first ideal-model power mismatch is
   \(R^{59/898}\) in (153.S48).
4. Do not infer an impossibility theorem or signed lower bound from the
   absence of a direct source match, a Cauchy diagonal, or pigeonhole
   capacity.
5. Do not change any \(D>1\), \(L>1\), generic, original \(t\geq2\),
   cross, M1/M2, endpoint, M9, bridge, target, or exponent obligation on
   the strength of this audit.
