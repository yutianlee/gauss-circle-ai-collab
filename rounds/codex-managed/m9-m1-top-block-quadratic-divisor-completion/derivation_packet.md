# Round 59 derivation packet: quadratic completion of the short divisor core

This packet freezes the exact high-shell survivor accepted in Round 58. It
asserts no B-process estimate.

## 1. Primal object and target

Let \(Y=R^2\asymp\sqrt X\), let
\(J=[A,B]\cap\mathbb Z\subset[cY,CY]\) have \(|J|\le R\), and retain

\[
 P_J=\sum_{n\in J}^{*}e(\sqrt{Xn})
 \sum_{\substack{h\mid n,\ R/4<h\le R/2\\n/h\ {m odd}}}
 \chi_4(n/h)\Omega_X^*(n,h).
\tag{59.1}
\]

Here \(\Omega_X^*\) is the exact actual angular symbol: all active dyadic
profiles, height floors, the one-sided hard top, angular equality stars,
and the independent radial star remain. The unweighted target is

\[
 |P_J|\ll_\varepsilon X^\varepsilon\sqrt R.
\tag{59.2}
\]

Round 58 already proved that the floor/Vaaler endpoint residual is target
safe. It must not be reintroduced as the missing loss.

## 2. Exact additive projector to verify

For integral \(h,n\), define

\[
 g_h(n)=\mathbf1_{h\mid n}\chi_4(n/h),
\]

where \(\chi_4\) vanishes on even integers. Finite Fourier inversion modulo
\(4h\) suggests the exact identity

\[
 \boxed{
 g_h(n)=-{i\over2h}\sum_{a\bmod4h}\chi_4(a)
 e\!\left({an\over4h}\right).}
\tag{59.3}
\]

The first task is to verify the constant and sign, including \(n/h\equiv
1,3\pmod4\). If correct, it gives the exact finite representation

\[
 P_J=-{i\over2}\sum_{R/4<h\le R/2}{1\over h}
 \sum_{a\bmod4h}\chi_4(a)
 \sum_{n\in J}^{*}\Omega_X^*(n,h)
 e\!\left(\sqrt{Xn}+{an\over4h}\right).
\tag{59.4}
\]

No smooth extension of the character is permitted; (59.3) must impose the
divisibility and character exactly.

## 3. Candidate radial B-process geometry

For a Poisson frequency \(k\in\mathbb Z\), stationarity in \(n\) is

\[
 {\sqrt X\over2\sqrt n}+{a\over4h}=k.
\]

Put

\[
 r=4hk-a.
\tag{59.5}
\]

Then the candidate stationary point and Legendre phase are

\[
 n_*(h,r)={4Xh^2\over r^2},\qquad
 \sqrt{Xn_*}+{a\over4h}n_*-kn_*={Xh\over r}.
\tag{59.6}
\]

As \(a\bmod4h\) and \(k\) vary, \(r\) should run once through the
relevant integers; since \(a\equiv-r\pmod{4h}\), one must audit
\(\chi_4(a)=\chi_4(-r)=-\chi_4(r)\). The stationary cone is

\[
 2h\sqrt{X/B}\le r\le2h\sqrt{X/A},
\tag{59.7}
\]

an interval of length \(\asymp R\) for each \(h\), centered at
\(r\asymp R^2\). Thus \(h\asymp R\), \(r\asymp R^2\), while only the
sheared offset below has size \(R\).

Since

\[
 {1\over\sqrt{|(\sqrt{Xn})''|}}
 ={2n^{3/4}\over X^{1/4}}\asymp\sqrt R,
\]

the outer factor \(1/h\) makes each dual stationary coefficient
\(\asymp R^{-1/2}\). Thus the raw two-dimensional dual sum must be
\(O_\varepsilon(X^\varepsilon R)\) to imply (59.2). Every endpoint,
nonstationary, transform-error, and star term must be accounted for.

## 4. Sheared reciprocal strip

Choose an integer \(K\asymp R\) such that \(4K\) is within \(2\) of the
central slope \(2\sqrt{X/N}\), where \(N\asymp R^2\) is the window
center, and write

\[
 r=4Kh+s.
\tag{59.8}
\]

Then \(|s|\ll R\) on the stationary strip and
\(\chi_4(r)=\chi_4(s)\). The exact reciprocal phase is

\[
 \Phi_K(h,s)={Xh\over4Kh+s}.
\tag{59.9}
\]

Here \(4Kh\asymp R^2\), so \(r\asymp R^2\) and \(|s|\ll R\). Its
Hessian has the exact determinant

\[
 \boxed{\det \nabla^2\Phi_K(h,s)
 =-{X^2\over(4Kh+s)^4}\asymp-1.}
\tag{59.10}
\]

This nonzero determinant is only geometry, not a lattice estimate: a
bilinear phase with integral mixed coefficient can be fully coherent.
The required raw model is

\[
 \sum_{h\asymp R}\sum_{s\asymp R}^{*}
 \chi_4(s)W_X(h,s)e(\Phi_K(h,s))
 \ll_\varepsilon X^\varepsilon R,
\tag{59.11}
\]

for the exact sheared support and transformed actual symbol. Prove (59.11),
or identify an exact resonance/return that prevents deriving it from the
available hypotheses.

## 5. Mandatory controls

- Check (59.3) at residues \(n/h\equiv0,1,2,3\pmod4\).
- A transform may not take absolute values over \(a,k,r,h\), or \(s\).
- The phase factor and stationary normalization, including the
  \(e(\pm1/8)\) convention, must be explicit.
- A nonzero Hessian determinant alone is insufficient; test integral and
  quarter-frequency mixed resonances with \(\chi_4(s)\) retained.
- At \(X=L^4\), expand near \(n=L^2\) and retain the integral/half-integral
  linear term and the critical quadratic term \(-t^2/(8L)\).
- Actual profile and hard-top seams, transform endpoints, and inherited
  stars remain separately owned.
- If the transform returns to the Hardy/GAR or original M1 kernel, prove the
  exact normalization and scope of that return; analogy is not enough.
- The lower sector \((\log X)^B<h\le R/4\), alpha connectors, height limits,
  M9-M1, and M9 are not owned.

No numerical experiment is required. The round is 100% analytical.
