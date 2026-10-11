# Signed cross-label cancellation: exact smooth main and unresolved arithmetic remainder

Prelaunch231, 11 October2026. Conductor candidate; reviewed evidence only, not a graph promotion. Graph provenance: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. Definitions and actual fixed functions are those of `briefs/complete_target.md` and accepted216. No absolute value is taken separately at a squarefree-label tuple in this argument.

## 1. Result

Pooling the arithmetic means of every squarefree harmonic recovers the exact area density. Its full real cosine transform vanishes on the physical window. This is a genuine exact signed cancellation of the smooth main term. It does not estimate the oscillating arithmetic remainder.

Writing that remainder as a complete frequency measure gives a precise sufficient input: a cumulative discrepancy of size `T^(4/25+epsilon)` at frequency resolution `1/T`, with the stated weighted tails, would give the complete twelfth target `T^(29/25+epsilon)`. No such arithmetic estimate has been proved here. Coarse squarefree mean laws cannot supply it by themselves.

## 2. Exact hypotheses and statements

For each integer `s>=1`, define the squarefree weighted mean

\[
A_s(x)=\sum_{d\le x,\ d\ {m squarefree}}r_2(ds^2).
\]

Let

\[
\kappa=\pi(1-2^{-2})
\prod_{p\equiv1(4)}(1-3p^{-2}+2p^{-3})
\prod_{p\equiv3(4)}(1-p^{-2}),
\quad
\kappa_s=\kappa\prod_{p^a\Vert s,\ p\equiv1(4)}
\left(1+\frac{2a(p+1)}{p+2}\right).
\]

For every fixed `1/2<sigma<1` and `eta>0`, uniformly in `s>=1,x>=1`,

\[
A_s(x)=\kappa_s x+O_{\sigma,\eta}(s^\eta x^\sigma),
\qquad \sum_{s\ge1}\frac{\kappa_s}{s^2}=\pi. \tag{1}
\]

Define the continuum of all classes, and the continuum of the large classes, respectively by

\[
\mathcal B_T(R)=\sum_{s\ge1}\kappa_s s^{-3/2}
\int_0^\infty x^{-3/4}\Psi(s\sqrt{x/T})
\cos(2\pi Rs\sqrt x-3\pi/4)\,dx,
\]
\[
\mathcal Z_{T,Q}(R)=\sum_{s\ge1}\kappa_s s^{-3/2}
\int_Q^\infty x^{-3/4}\Psi(s\sqrt{x/T})
\cos(2\pi Rs\sqrt x-3\pi/4)\,dx.
\]

These are absolutely convergent integrals and harmonic sums. They satisfy

\[
\boxed{\mathcal B_T(R)=0\quad(R>T^{-1/2}),}\tag{2}
\]
\[
\sup_{R\in[T/2,2T]}|\mathcal Z_{T,Q}(R)|
\ll T^{-1}Q^{-1/4}\ll T^{-11/10}. \tag{3}
\]

For the actual large-class sum `Z=Z_Q`, put `D=Z-mathcal Z`. Then

\[
M_{12}(D)-M_{12}(Z)
=O_\epsilon(T^{9\beta-11/10+\epsilon}), \tag{4}
\]

and, by accepted216,

\[
I_{12}(T)=M_{12}(D)+O_\epsilon(T^{8\beta-1/5+\epsilon}). \tag{5}
\]

Thus centering pays every complementary class and harmonic, but the twelfth moment of `D` is still the complete unresolved target.

## 3. Derivation

### Actual arithmetic means, including all primes

Set `g(s)=product_(p^a||s,p=1 mod4)(2a+1)`, so `r2(s^2)=4g(s)`. At a split prime write `u_p=2(a+1)/(2a+1)`, taking `a=0` if `p` does not divide `s`. The squarefree Dirichlet series has local factors `1+u_p p^(-z)` at split primes, `1+2^(-z)` at2, and1 at inert primes, with leading constant `4g(s)`.

Relative to the Dirichlet series of `r2`, the multiplicative convolution factor `h_s` has local polynomials

\[
1-X^2\quad(p=2\text{ or }p\equiv3\pmod4),
\qquad (1+u_pX)(1-X)^2\quad(p\equiv1\pmod4).
\]

Consequently `mu(d)^2 r2(ds^2)=g(s)(h_s*r2)(d)` coefficient by coefficient. For `p` not dividing `s`, the split polynomial is `1-3X^2+2X^3`; its nonconstant terms start at degree2. The finitely many modified split factors have bounded coefficients. The elementary divisor estimates therefore give

\[
g(s)\sum_{m\ge1}|h_s(m)|m^{-\sigma}\ll_{\sigma,\eta}s^\eta
\qquad(\sigma>1/2).
\]

Convolve the elementary area estimate `sum_(n<=y)r2(n)=pi y+O(sqrt(y)+1)`. Its errors and the residue tail are bounded by a constant times `s^eta x^sigma`, exactly as in the earlier squarefree mean proof. The residue is `pi g(s) sum_m h_s(m)/m`, which simplifies to the stated `kappa_s`. This proves the uniform assertion in(1), including real endpoints. It is a coarse mean law, not an oscillatory estimate.

The series of positive means converges absolutely. For a split prime, its normalized harmonic factor is

\[
K_p=\sum_{a\ge0}\left(1+\frac{2a(p+1)}{p+2}\right)p^{-2a}
=\frac1{1-p^{-2}}+\frac{2(p+1)p^{-2}}{(p+2)(1-p^{-2})^2}.
\]

Direct algebra gives `(1-p^(-1))^2(1+2p^(-1)) K_p=1`. For2 and inert primes the corresponding identity is `(1-p^(-2)) sum_(a>=0)p^(-2a)=1`. Multiplication gives the second part of(1). There is no averaging of random labels.

### Exact phase cancellation of the pooled continuum

Changing variables `y=s sqrt(x)` and using(1) gives

\[
\mathcal B_T(R)=2\pi\operatorname{Re}\left[
e(-3/8)\int_0^\infty y^{-1/2}\Psi(y/\sqrt T)e(Ry)\,dy\right]. \tag{6}
\]

Let `v(u)=integral rho(u,t)dt` be the smooth marginal, supported in `[-1,1]`. Then `Psi(y/sqrt(T))=integral v(u)e(-uy/sqrt(T))du`. Introduce an Abel factor `exp(-lambda y)`, `lambda>0`, in(6) before interchanging these integrals. For `R>T^(-1/2)` the quantity `b=R-u/sqrt(T)` is uniformly positive on the marginal's support, and

\[
\int_0^\infty y^{-1/2}e^{-\lambda y}e(by)\,dy
=\sqrt\pi(\lambda-2\pi i b)^{-1/2}
\longrightarrow\frac{e^{i\pi/4}}{\sqrt{2b}}.
\]

The limit may pass through the compact marginal integral, since `b` is bounded below. On the original side, `y^(-1/2)Psi(y/sqrt(T))` is integrable, so dominated convergence removes the Abel factor. The product `e(-3/8)e^(i pi/4)=-i` is purely imaginary. Its real part is zero, proving(2) exactly. The restriction to positive `R` matters.

### Complete large-class continuum and centering cost

After the same substitution, the `s`th integral defining `mathcal Z` starts at `y=s sqrt(Q)` and has amplitude `2 kappa_s s^(-2) y^(-1/2)Psi(y/sqrt(T))`. Integration by parts against `e(Ry)` costs

\[
\frac{\kappa_s s^{-2}}R
\left( |y_0^{-1/2}\Psi(y_0/\sqrt T)|
+\int_{y_0}^\infty\left|\frac d{dy}
[y^{-1/2}\Psi(y/\sqrt T)]\right|dy\right)
\ll\frac{\kappa_s s^{-5/2}}R Q^{-1/4}.
\]

The last inequality is uniform for every `y_0>0`: use bounded `Psi` for the derivative of `y^(-1/2)` and `integral_0^infinity |Psi'(u)|du<infinity` for the other term. Summing `kappa_s s^(-5/2)` proves(3), including the entire infinite tail. No sharp spectral cutoff is inserted.

Accepted204 and216 give `M12(Z)<<T^(10beta+epsilon)` and `M10(Z)<<T^(8beta+epsilon)`. Cauchy gives `M11(Z)<<T^(9beta+epsilon)`. Applying the elementary difference bound for twelfth powers with(3) proves(4); the term `T||mathcal Z||_infinity^12` is smaller. Since `9beta-11/10 < 8beta-1/5`, accepted216's complete repeated-class estimate proves(5). Its head cost `15/13` is below `29/25`. This retains all distinct classes, signs, mixed blocks, harmonics and real windows.

### Exact fine-scale signed interface

There is a finite complex frequency measure `tau_T` with conjugate symmetry whose Fourier transform is `D(R)`. Its atomic part is

\[
\frac12\sum_{d>Q\ {m sf},\ s\ge1}a_{ds^2}
\left[e(-3/8)\delta_{s\sqrt d}+e(3/8)\delta_{-s\sqrt d}\right],
\]

and its subtracted continuous part is the frequency measure of `mathcal Z`. Both variations are `O(T^(1/4))`, by the area bound, Schwartz decay and `sum_s kappa_s/s^2=pi`. Thus `mu_T=tau_T^{*12}` has variation `O(T^3)` and

\[
M_{12}(D)=T\int\widehat w(-Tx)\,d\mu_T(x).
\]

For any prescribed reference density `rho_T` whose signed contribution is negligible, let

\[
H_T(x)=(\mu_T-\rho_T\,dx)((-\infty,x]).
\]

The independently derived finite-measure identity is

\[
M_{12}(D)-\mathcal L_T(\rho_T\,dx)
=T\int\widehat w'(-u)[H_T(u/T)-c_T]du. \tag{7}
\]

It handles atoms and nonzero total mass; any constant baseline is legal. A sufficient, not necessary, arithmetic hypothesis is

\[
\inf_c\int |\widehat w'(-u)|\,|H_T(u/T)-c|du
\ll_\epsilon T^{4/25+\epsilon}. \tag{8}
\]

For example, a uniform cumulative error of that size implies(8). Alternatively, control on `|x|<=T^(-1+delta)` for fixed `delta>0`, together with `||mu_T-rho_T dx||_TV+|c_T|=O(T^3)`, pays the exterior by Schwartz decay. This condition concerns the variation of the discrepancy measure, not merely the signed mass of either measure. A fixed-width interval `|Tx|<=C` alone is insufficient. A reference `rho_T(x)=A_T ell_T^(-1)q(x/ell_T)` with fixed Schwartz `q`, `|A_T|=O(T^3)` and `ell_T` comparable to `sqrt(T)` has the required polynomial variation and contributes `O_A(T^(-A))` by direct Fourier scaling. One can also subtract a band-limited convolution exactly; the resulting discrepancy still needs a new bound.

This measure includes every mixed term in `(Z-mathcal Z)^12`; it is not the convolution of12 independently distributed labels. Equation(5) restores the full target from(8), if(8) can be proved for the actual arithmetic measure.

## 4. First unproved step

The missing step is(8), or a comparably strong bound for the signed transform in(7), for the actual arithmetic measure. The coarse mean laws in(1), exact continuum cancellation in(2), and spectral smoothing identities do not prove it. No improved complete upper bound follows from this candidate.

The exact mean cancellation is an arithmetic consistency identity followed by the geometric circle phase cancellation. It is not, by itself, a new estimate for arithmetic fluctuations. Treating the disappearance of the area term as the disappearance of those fluctuations would be circular.

## 5. Controls and quantitative cancellation already forced

The isolated transport report gives a nonnegative coherent modulation control with twelve factors. Its smooth continuum vanishes to arbitrary order on the physical window, and each factor has cumulative error only `T^(-5/4)`, yet its twelfth Fourier integral is of size `T^(5/2)`. It is an abstract information-content control, not a counterexample with the actual square-root locations or `r2` coefficients. It proves that multiplying coarse density laws is insufficient.

The previous reviewed full-harmonic certificate obstruction and the current accepted complete upper bound also show that substantial cancellation already occurs between actual label tuples. Put

\[
C_+=\sum_{\boldsymbol d}^{*}\max(J_{\boldsymbol d},0),\qquad
C_-=\sum_{\boldsymbol d}^{*}\max(-J_{\boldsymbol d},0).
\]

Absolute convergence gives `C_++C_-=C_harm` and `C_+-C_-=I12`. Since `C_harm>=cT^(5/2)` whereas `|I12|<<T^(10beta+epsilon)`, both `C_+` and `C_-` are at least a constant times `T^(5/2)` and

\[
\frac{|C_+-C_-|}{C_++C_-}
\ll_\epsilon T^{-1.2103364805\ldots+\epsilon}. \tag{9}
\]

This uses an already accepted upper bound and is not a new proof of that bound. Relative to the guaranteed `T^(5/2)` scale, the preferred target would imply a residual ratio `O(T^(-67/50+epsilon))`. That ratio is a necessary consequence, not a sufficient criterion without also controlling the absolute mass. A further saving `T^(10beta-29/25)=T^(0.12966351948...)` in the complete upper bound is still missing. Neither(9) nor the certificate lower bound gives a signed lower bound on the complete moment.

Wolfram checks of the local Euler identity and Abel phase were independently reproduced by exact local polynomial/rational/root-of-unity calculations. These bounded diagnostics certify no asymptotic estimate.

## 6. Dependencies and provenance

Protocol; exact complete-target brief; accepted204 and216 kernel files; previous reviewed full-harmonic admission and its elementary squarefree convolution formula; current `reports/blind_signed_transport.md` at SHA256 `47b6e84139f14a9e85e15200f51de0ae6a05eacb3b4443c71c51f394bea7186e`; conductor's own derivation of the harmonic residues and Abel cancellation. The conductor sent those two candidate formulas to the arithmetic discovery agent; that report must disclose this communication. The transport proof remained statement-only and received no derivation or arithmetic history. Source applicability is audited separately; no new external theorem is used above.

## 7. Recommended state effect

Retain as reviewed evidence after the nonauthor seam review. Do not launch analytic Round231 from these identities, do not promote the target, and do not alter the accepted graph or draft. Future admission requires a proved new arithmetic input for(7)/(8), or another complete signed estimate with a better restored exponent. Another change of notation for the same discrepancy is insufficient.
