# Conductor candidate: exact Kloosterman-fraction source capacity

Round: 135

Status: reconciled conductor derivation. It remains candidate mathematics
until the Round-135 State Patch is validated and applied.

## 1. Literal scaled tensor and real-centre repair

Put

\[
 R=\frac XD,\qquad K=\frac{XL}{D^2},\qquad
 \Delta=\frac DL=\frac RK,\qquad F=\frac{XK}{R}=\frac{XL}{D}.
\tag{135.C1}
\]

Write (X=N_0+\xi), where \(N_0=\lfloor X\rfloor\) and
(0\leq\xi<1). On a fixed flat smooth cell, set (k=Ku), (r=Rv).
After the standard rescaling of (q_L), the complete normalized amplitude,
including (K/k), is

\[
 G_{\xi,\Delta}(u,v)
 =G(u,v)e\!\left(\frac{\xi}{\Delta}\frac uv\right).
\tag{135.C2}
\]

It is uniformly smooth on a fixed compact rectangle: every derivative of
the added factor is (O(\Delta^{-1})=O(1)). Buffered Fourier inversion in
\((\log u,\log v)\) gives an exact rank-one integral

\[
 G_{\xi,\Delta}(u,v)
 =\iint \widehat G_{\xi,\Delta}(t_1,t_2)
 u^{it_1}v^{it_2}\,dt_1dt_2,
 \qquad \iint|\widehat G_{\xi,\Delta}|\ll1.
\tag{135.C3}
\]

Thus (e(\xi k/r)) may be absorbed into the coefficients and every source
phase below may use the integer (N_0). Each direct fibre has

\[
 \|\alpha\|_2=1,\qquad
 \|\beta\|_2\asymp R^{1/2},\qquad
 \|\nu\|_2\asymp K^{-1/2},
\tag{135.C4}
\]

with (\chi_4(r)) retained in (\beta_r). The moving smooth profile and
the real centre are therefore not source obstructions on the frozen cell.

## 2. Exact direct source dictionaries

For Bettin--Chandee Theorem 1 and Wright Theorem 2.1 take

\[
 m=1,\qquad n=r,\qquad a=k,\qquad
 (A,M,N,R_0,\vartheta)=(K,1,R,1,N_0).
\tag{135.C5}
\]

The phase is exact after (135.C2), and coprimality is automatic. Bettin--
Chandee gives

\[
 |\mathscr R_{D,L}(X)|
 \ll_\varepsilon X^\varepsilon F^{1/2}
 \left(R^{11/10}K^{-3/20}+R\right).
\tag{135.C6}
\]

The two exponents are

\[
 E_{\mathrm{BC},1}=\frac{29}{20}+\frac{7\ell}{20}
 -\frac{13\delta}{10},\qquad
 E_{\mathrm{BC},2}=\frac32+\frac\ell2-\frac{3\delta}{2}.
\tag{135.C7}
\]

For (u=\delta-\ell), throughout the strict polytope,

\[
 E_{\mathrm{BC},1}-u>\frac3{10},\qquad
 E_{\mathrm{BC},2}-u>\frac14.
\tag{135.C8}
\]

Bettin--Chandee Remark 1 also repairs the fractional centre directly with
the phase perturbation (\xi a/n), but the coefficient absorption above is
stronger because it also applies to Wright. For Wright, (R_0=1) is the
only owner-complete fixed factor; (M=1) forces (R_0=O(1)). Its fifth
term dominates and yields

\[
 |\mathscr R_{D,L}(X)|
 \ll_\varepsilon X^\varepsilon R^{11/8}F^{1/4},
\qquad
 E_{\mathrm W}=\frac{13}{8}+\frac\ell4-\frac{13\delta}{8},
\tag{135.C9}
\]

with

\[
 E_{\mathrm W}-u
 =\frac{13}{8}+\frac{5\ell}{4}-\frac{21\delta}{8}
 >\frac5{16}.
\tag{135.C10}
\]

Both exact direct imports are therefore uniformly worse than the existing
absolute capacity (\Delta=X^u).

## 3. The nondegenerate inverse connector and sharp diagonal norm

On ((k,r)=1), set (a=j^2), (m=k), (j=m), and (n=r). Then

\[
 m^2\overline m\equiv m\pmod r,
\tag{135.C11}
\]

so the source phase with frequency (N_0), together with the separated
factor (e(\xi k/r)), equals the project phase for every real (X). The
correlated diagonal is separated exactly by

\[
 \mathbf1_{j=m}=\int_0^1e(t(j-m))\,dt,
 \quad
 \alpha_m(t)=m^{-1/2}e(-tm),
 \quad
 \nu_{j^2}(t)=j^{-1/2}e(tj).
\tag{135.C12}
\]

Both norms are (O(1)). This is sharp because the diagonal matrix
(m^{-1}\mathbf1_{j=m}) has nuclear norm
(\sum_{m\asymp K}m^{-1}\asymp1). Relative to the direct
(k^{-1})-vector norm (K^{-1/2}), the unavoidable inflation is
(K^{1/2}), not (K).

At ((A,M,N)=(K^2,K,R)), Bettin--Chandee gives

\[
 F^{1/2}\left(K^{21/20}R^{11/10}+K^{11/8}R\right).
\tag{135.C13}
\]

Its exponents are

\[
 E_{\mathrm{BC,sq},1}=\frac{53}{20}+\frac{31\ell}{20}
 -\frac{37\delta}{10},\qquad
 E_{\mathrm{BC,sq},2}=\frac{23}{8}+\frac{15\ell}{8}
 -\frac{17\delta}{4},
\tag{135.C14}
\]

and their margins over (u) exceed (3/10) and (1/4). Wright gives

\[
 F^{1/4}KR^{11/8}
 =X^{21/8+5\ell/4-29\delta/8},
\tag{135.C15}
\]

whose exponent exceeds (u) by more than (5/16). The inverse identity is
genuine, but its independent-coefficient realization is not target-capable.

## 4. The two inequivalent completion orders

First restore all gcd strata by (r=gn), (k=gj), ((j,n)=1). Then
(n\asymp R/g), (j\asymp K/g), and (n/j\asymp\Delta).

If the original smooth (j)-weight is Fourier-expanded first, its
normalized coefficients satisfy

\[
 |\widehat b_{g,n}(h)|
 \ll_B\frac1R\left(1+\frac{\|h\|_n}{\Delta}\right)^{-B}.
\tag{135.C16}
\]

Inversion only permutes reduced residues, so the complete inverse-only sum
is the Ramanujan sum (\mathfrak c_n(N_0+h)), not a two-frequency
Kloosterman sum. The estimate

\[
 |\mathfrak c_n(q)|\le(n,q),\qquad
 \sum_{n\asymp T}\frac{(n,q)}n\ll_\varepsilon X^\varepsilon
\tag{135.C17}
\]

and the (O(\Delta)) effective frequencies give, after the harmonic
(g)-sum,

\[
 |\mathscr R_{D,L}(X)|\ll_\varepsilon\Delta X^\varepsilon.
\tag{135.C18}
\]

This is the exact existing capacity, hence no strict reduction.

If the inverse selector (g_r(m)=w_r(\overline m)) is formed first and
then Fourier-expanded in the rough variable (m), one instead obtains

\[
 \sum_{h\bmod r}\widehat g_r(h)S(N_0,h;r),\qquad
 \sum_h|\widehat g_r(h)|^2\ll\frac1{rK}.
\tag{135.C19}
\]

The exact complete-frequency identity
(\sum_h|S(N_0,h;r)|^2=r\varphi(r)) gives the positive row cost
(\sqrt\Delta), and the modulus triangle gives

\[
 R\sqrt\Delta\,X^\varepsilon
 =X^{1-(\delta+\ell)/2+\varepsilon}.
\tag{135.C20}
\]

Its exponent exceeds (u) by more than (1/4). The coefficients in
(135.C19) depend jointly on modulus and frequency, so neither audited
trilinear theorem accepts them. The two completion orders must not be
conflated.

## 5. Physical residue and fixed determinant

Writing (s=N_0+t) gives the exact congruence

\[
 r\mid s\quad\Longleftrightarrow\quad t\equiv-N_0\pmod r,
 \qquad |t-\xi|\ll\Delta X^\varepsilon.
\tag{135.C21}
\]

This is a fixed integral residue, but it is not uniformly coprime to (r),
the short (t)-variable is not an independent convolution, and the kernel
depends jointly on ((r,t)). Wright's dispersion corollary also subtracts a
principal term and places absolute values inside the modulus sum, whereas
the project needs one outer absolute value after the (\chi_4(r))-signed
sum. There is no literal dispersion-corollary dictionary.

There is an exact Bettin--Chandee Corollary 1 map. For fixed
(\tau=N_0-dr\ne0), take

\[
 (m_1,n_2,m_2,n_1)=(d,r,1,N_0),\qquad
 m_1n_2-m_2n_1=-\tau.
\tag{135.C22}
\]

With scales ((M_1,M_2,N_1,N_2)=(D,1,X,R)), norms (1,R^{1/2}), and
aspect ratio (O(1)), the error per determinant is

\[
 X^{3/5+\varepsilon}R^{17/20}
 =X^{29/20-17\delta/20+\varepsilon},
\tag{135.C23}
\]

whose exponent is greater than (41/40). The main term is
(O(X^\varepsilon)) per determinant by
(\sum_{r\asymp R}(N_0,r)/r\ll X^\varepsilon). Summing the
(O(\Delta X^\varepsilon)) effective determinants therefore returns
(\Delta X^\varepsilon) in the main terms and multiplies the already huge
errors by (\Delta). The zero determinant is one divisor-bounded level.

## 6. First unproved step and validation status

The three post-unmask reviews independently verify the source statements,
real-centre repair, direct and square exponents, the two completion orders,
and the determinant ledger. The first unproved positive step is a new
estimate for the literal coupled signed family

\[
 \sum_{k\asymp K}\frac1k\sum_{r\asymp R}
 \chi_4(r)G(k/K,r/R)e(Xk/r),
\tag{135.C24}
\]

or its exact prescribed-centre divisor form, which preserves the character
before every positive modulus norm and beats the accepted envelope

\[
 X^\varepsilon\min\!\left(\Delta,
 \sqrt{XL/D}+\sqrt{X/(LD)}\right).
\tag{135.C25}
\]

Neither primary source supplies that coefficient-matrix or pointwise signed
fixed-centre theorem. This is a scoped source-method obstruction, not a
lower bound for the literal wave and not a universal no-go.

## 7. Provisional state effect

Promote the exact source card and the scoped interface obstruction after
State Patch validation. Record smooth-first completion only as the
equal-capacity Ramanujan return, and inverse-first completion as the rough
Kloosterman matrix with positive cost (R\sqrt\Delta). Reject blanket
claims that the moving profile or real centre prevents a source map, that an
ordinary fraction cannot be encoded by an inverse phase, or that the source
no-go rules out a future tailored theorem.

Keep the flat-wave quarter estimate, complete UNBAL, M9-M2, M9-M1, endpoint
uniformity, M9, the internal one-third exponent, and the quarter target
unchanged.
