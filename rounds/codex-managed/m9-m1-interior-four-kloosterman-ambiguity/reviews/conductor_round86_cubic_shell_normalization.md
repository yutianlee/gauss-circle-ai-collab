# Round 86 conductor cubic-shell normalization

Campaign: `m9-m1-interior-four-kloosterman-ambiguity`

Starting graph SHA-256:
`910950f389c49a17cc188c8e0ad9b18e4d83d4a7f580fa0baacca97d39195fe6`

## Exact shell and phase

Put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
 B=C/T,
\]

\[
 D_0=\lfloor J^{17/30}\rfloor,\qquad
 D_1=\lfloor J^{87/140}\rfloor.
\]

The increment is genuinely nonempty because

\[
 {87\over140}-{17\over30}={23\over420}>0.
\]

On a progression \(n=r+M\ell\), after translating negative
differences and reflecting the opposite endpoint orientation, the
principal phase is

\[
 f(\ell)=\pm\lambda_b\bigl(\sqrt{m+e}-\sqrt m\bigr),
 \qquad e=|d|,\quad m\asymp Q^2,
\]

with \(\lambda_b\asymp J\).  Since \(e\leq D_1\) and

\[
 {D_1\over Q^2}=J^{-5/28},
\]

both square roots remain in one fixed sign band.  Three
differentiations, including the chain factor \(M^3\), give

\[
 f'''(\ell)
 ={3\lambda_bM^3\over8}
 \bigl((m+e)^{-5/2}-m^{-5/2}\bigr)
 =-{15\lambda_bM^3e\over16}\xi^{-7/2}.
\]

Hence

\[
 |f'''(\ell)|\asymp \rho_e:={JM^3e\over Q^7}
\]

with fixed sign and fixed comparability constants.  The hostile audit
independently verifies that throughout the frozen \(B,e\) ranges

\[
 J^{-13/15}\ll\rho_e\ll J^{-51/70}<1.
\]

## Weighted progression bound

The accepted phase-removed stationary symbol has sampled
\(\sup+\operatorname{Var}\ll X^\varepsilon H\), where

\[
 H={C\sqrt T\over J}=BJ^{-1/10}.
\]

Translation, support intersection, zero extension, and the product
variation inequality therefore give

\[
 \sup|a_{b,d,r}|+\operatorname{Var}(a_{b,d,r})
 \ll X^\varepsilon H^2.
\]

For progression length \(L\ll Q^2/M+1\), the weighted
third-derivative estimate yields

\[
 \sum_\ell a_{b,d,r}(\ell)e(f(\ell))
 \ll X^\varepsilon H^2
 \left(L\rho_e^{1/6}+L^{1/2}\rho_e^{-1/6}+1\right).
\]

Using the exact all-modulus arithmetic normalization

\[
 {1\over M^2}\sum_{r\bmod M}|A_{M,K,d}(r)|\leq2
\]

retains the centered Ramanujan term, prime-power gcd modes, and
nonzero differences divisible by \(M\).  It gives, for each \(b,d\),

\[
 {1\over M^2}\left|\sum_n A_{M,K,d}(n)
 I_b(n+d)\overline{I_b(n)}\right|
 \ll X^\varepsilon H^2
 \left(J^{1/2}M^{-1/2}e^{1/6}
 +J^{7/10}M^{-1}e^{-1/6}+1\right).
\]

## Aggregate exponent check

Since \(M\asymp B\) in all three local classes and
\(H^2=B^2J^{-1/5}\), summing both signs, \(b\asymp B\), and
\(D_0<e\leq D\) gives

\[
 X^\varepsilon\left(
 B^{5/2}J^{3/10}D^{7/6}
 +B^2J^{1/2}D^{5/6}
 +B^3J^{-1/5}D\right).
\]

At the worst conductor \(B=J^{3/20}\) and
\(D=D_1=J^{87/140}\), the three exponents are

\[
 {5\over2}{3\over20}+{3\over10}
 +{7\over6}{87\over140}={7\over5},
\]

\[
 2{3\over20}+{1\over2}
 +{5\over6}{87\over140}={369\over280}<{7\over5},
\]

\[
 3{3\over20}-{1\over5}+{87\over140}
 ={61\over70}<{7\over5}.
\]

Thus the newly deleted shell is target-safe.  All powers increase with
\(B\), so the bound is uniform on
\(J^{13/18}<C\leq J^{3/4}\).

## Arithmetic and ownership seams

- Negative \(d\) is a translate/conjugate and preserves residue
  \(L^1\) mass.
- The ratios \(M/b\in\{1,2,4\}\) alter only absolute constants.
- Extension by zero owns the smooth-principal support endpoints.
- Small differences \(0<|d|\leq D_0\), the outer collar
  \(|d|\geq\Delta_b-E_*\), stationary errors, entry/exit, wrong signs,
  and exterior tails are not counted again.
- Raw Farey transitions and axes remain separately owned.
- Integer first derivatives and square/fourth-power specializations do
  not defeat the fixed-sign third-derivative estimate.
- The physical \(Q^{-5/12}\) energy factor remains available on the
  residual interval because this shell is subtracted by a direct
  target-safe estimate.

## Conductor decision

The exact first-band smooth-principal survivor is now

\[
 D_1<|d|<\Delta_b-E_*.
\]

The complete rational-trace transform is useful only as a structural
reduction.  Exact prime-power and squarefree divisor-aligned modes can
have size nearly \(M^2\), so no coefficientwise uniform square-root
bound may be promoted.  Closing the residual interval requires a
joint actual-symbol estimate before absolute values, including the
exceptional gcd strata and all Ramanujan terms.

