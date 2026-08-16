# Round 77 derivation packet: complete odd-lift actual symbol

Campaign: `m9-m2-top-endpoint-actual-symbol-variation`  
Round: 77  
Starting graph SHA-256:
`e14373a05ee7d55258b53f07e18afa33682806add90bee49789208f464e46166`

## 1. Accepted antecedent

Put

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=X/y^2,\qquad H=\lfloor yX^{-1/4}\rfloor,
\]

and let \(1\le L\le H\le J^{1/2}\) be dyadic. The accepted normalized
top symbol is

\[
 a_L(h,m)=\eta_L(h)\Phi\!\left({h\over H+1}\right)
 \left({L^2\over hm}\right)^{3/4}
 W\!\left(\sqrt{{q_Xh\over4m}}\right),                 \tag{77.1}
\]

with the actual finite odd support. The external physical factor is not
part of \(a_L\) and must not be inserted in this round.

Round 75 proved the exact finite energy

\[
 R_m=\sum_{\substack{h\in\mathscr H_L\\m\le h\le4m}}
 \chi_4(h)a_L(h,m)e(J\sqrt{hm}),
 \qquad
 \mathcal E_L^\top=\sum_m|R_m|^2.                    \tag{77.2}
\]

Its diagonal is \(O(L^2X^\varepsilon)\). Its positive-offset part is

\[
\begin{aligned}
 \mathcal O_L={}&2\Re\sum_{r\ge1}(-1)^r
 \sum_{\substack{h,h+2r\in\mathscr H_L}}
 \sum_{m=\lceil(h+2r)/4\rceil}^{h}
 A_{h,h+2r}(m)
 e\!\left(-{2rJ\sqrt m\over\sqrt h+\sqrt{h+2r}}\right),
                                                        \tag{77.3}\\
 A_{h,s}(x)={}&a_L(h,x)\overline{a_L(s,x)}.
\end{aligned}
\]

The sign \(\chi_4(h)\chi_4(h+2r)=(-1)^r\) occurs before every absolute
value. The target energy estimate remains open.

## 2. Accepted Round-76 correction

Write uniquely

\[
 h=ga,\qquad s=h+2r=gb,\qquad (a,b)=1,
 \qquad a,b,g\text{ odd},\quad a<b<4a.                \tag{77.4}
\]

Set

\[
 \delta=\sqrt b-\sqrt a,\qquad
 \Lambda={X\delta^2\over2},\qquad
 \alpha={b-a\over4}-{X\delta^2\over4k}.              \tag{77.5}
\]

Round 76 proved

\[
 (-1)^r e\!\left(-{gX\delta^2\over4k}\right)=e(g\alpha),
 \qquad e(2\alpha)=e(-\Lambda/k).                     \tag{77.6}
\]

Thus the bulk lift progression has step two and resonance

\[
 \|\Lambda/k\|\lesssim G_{a,b}^{-1}.                 \tag{77.7}
\]

A fixed primal collar at both \(m\)-endpoints has total
\(O(L^2X^\varepsilon)\) capacity. If the sharp lower endpoint is not
removed, its \(g\bmod4\) dependence may require a step-four split. These
facts are accepted; the complete symbol below is not.

## 3. Candidate exact finite transform

For odd \(h<s\le4h\), put

\[
 C_{h,s}=J(\sqrt s-\sqrt h),\qquad
 A=\lceil s/4\rceil,\qquad B=h.                       \tag{77.8}
\]

The exact finite Poisson identity to audit is

\[
 \sum_{m=A}^{B}F(m)
 ={F(A)+F(B)\over2}
  +\sum_{\nu\in\mathbb Z}\int_A^B F(x)e(-\nu x)\,dx,
 \quad F(x)=A_{h,s}(x)e(-C_{h,s}\sqrt x).             \tag{77.9}
\]

For the negative mode \(\nu=-k\), \(k\ge1\), define

\[
 f_k(x)=-C_{h,s}\sqrt x+kx,\qquad
 x_k={C_{h,s}^2\over4k^2}.                            \tag{77.10}
\]

The interior leading data are

\[
 f_k(x_k)=-{C_{h,s}^2\over4k},\quad
 f_k''(x_k)={2k^3\over C_{h,s}^2},\quad
 {e(1/8)C_{h,s}\over\sqrt2\,k^{3/2}}.                \tag{77.11}
\]

Choose one fixed \(M\ge1\) and a fixed smooth \(\rho\) with
\(\rho(t)=0\) for \(t\le1\), \(\rho(t)=1\) for \(t\ge2\). Put

\[
 A_{h,s}^{\circ}(x)=A_{h,s}(x)
 \rho\!\left({x-s/4\over M}\right)
 \rho\!\left({h-x\over M}\right).                  \tag{77.12}
\]

For \(h=ga,s=gb\), define the *candidate complete centred integral*

\[
\begin{aligned}
 \mathfrak B_{a,b,k}^{\circ}(g)
 ={}&g\int_{b/4}^{a} A_{ga,gb}^{\circ}(gu)\\
 &\times e\!\left(g\left[-J\delta\sqrt u+ku
              +{X\delta^2\over4k}\right]\right)du. \tag{77.13}
\end{aligned}
\]

This is the full integral, not a leading stationary value. The candidate
saddle condition is

\[
 {J\delta\over2\sqrt a}<k<{J\delta\over\sqrt b}.     \tag{77.14}
\]

If \(\mathcal G_{a,b}\) is the actual odd lift interval and \(g=2n+1\),
the candidate bulk identity is

\[
\begin{aligned}
 \mathcal O_{L,\mathrm{stat}}^{\circ}
 =2\Re\sum_{\substack{a<b<4a\\a,b\ {\rm odd}\\(a,b)=1}}
 \sum_{k\text{ satisfying }(77.14)} e(\alpha)
 \sum_{2n+1\in\mathcal G_{a,b}}
 \mathfrak B_{a,b,k}^{\circ}(2n+1)e(-n\Lambda/k).    \tag{77.15}
\end{aligned}
\]

The statement to prove or refute includes the aggregate assertion

\[
 \mathcal O_L
 =\mathcal O_{L,\mathrm{stat}}^{\circ}
  +O_\varepsilon(L^2X^\varepsilon),                  \tag{77.16}
\]

after the already accepted diagonal is treated separately. The error in
(77.16) must include the full endpoint samples, removed fixed collars,
zero and positive Poisson modes, negative nonstationary modes, saddle
entry/exit, all lower stationary corrections, floors, and stars. It may
not be inferred from a frozen leading amplitude.

## 4. Candidate step-two variation

Let

\[
 N_{a,b}=\#\mathcal G_{a,b},\qquad G\asymp L/b,
\]

and define

\[
 \mathcal V_{a,b,k}=
 |\mathfrak B^{\circ}(g_{\max})|
 +\sum_{\substack{g,g+2\in\mathcal G_{a,b}}}
 |\mathfrak B^{\circ}(g+2)-\mathfrak B^{\circ}(g)|. \tag{77.17}
\]

The candidate scale is

\[
 \boxed{
 \mathcal V_{a,b,k}
 \ll_{M,\eta,\Phi,W,\varepsilon}
 X^\varepsilon {J\delta\sqrt G\over k^{3/2}}.}       \tag{77.18}
\]

The round may correct this scale if it proves the corrected replacement.
Once a variation theorem is accepted, discrete Abel gives

\[
 \left|\sum_{2n+1\in\mathcal G_{a,b}}
 \mathfrak B^{\circ}(2n+1)e(-n\Lambda/k)\right|
 \le \mathcal V_{a,b,k}
 \min\!\left(N_{a,b},{1\over2\|\Lambda/k\|}\right). \tag{77.19}
\]

Abel's identity itself is elementary. The work is to prove (77.16) and
(77.18) for the complete actual symbol, uniformly through moving support
and saddle transitions.

## 5. Required controls

Every report must test:

1. the external normalization and one-count physical factor;
2. both full endpoint samples in finite Poisson;
3. fixed collar capacity without a growing-width substitution;
4. the actual \(\eta_L,\Phi,W,q_X\), floors, stars, and finite support;
5. zero, positive, negative nonstationary, and transition modes;
6. uniform stationary correction/error summation;
7. \(g\)-derivatives through dyadic support and \(\Phi/W\) transitions;
8. saddle entry and exit through each continuous collar;
9. the sharp lower-ceiling \(g\bmod4\) seam;
10. \(X=T^4\), odd \(13\mid T\), \((a,b)=(81,121)\),
    \(k=2T^2/13\), where the lift phase is fully coherent and both profile
    arguments lie on the \(W=1\) plateau;
11. a nonresonant actual-profile family and a \(\Phi\)-edge family;
12. rank-one reciprocal self-return and the coefficient adversary;
13. separation from any resonance-union estimate, the full energy, M2,
    M9, and the exponent.

## 6. False analogues and forbidden shortcuts

The theorem is not uniform over arbitrary bounded coefficients. A proof
must identify the actual symbol property that controls variation. Do not:

- replace \(\mathfrak B^{\circ}\) by its first stationary term;
- take absolute values over primitive pairs or reciprocal modes;
- use the false step-one distance \(\|\alpha\|\);
- discard a sharp endpoint without a primal capacity bound;
- infer (77.16) from pointwise asymptotics without summing every mode;
- invoke a nondegenerate two-dimensional Hessian;
- count a second matched transform as a gain.

## 7. Exit rule

Promotion requires an exact statement, proof, dependency list, clean
statement-only rederivation, hostile seam pass, and green validation for
the controls above. A corrected identity or sharper variation scale is
eligible. A precise first false term or a proof that the proposed
variation is too strong is also a successful no-go.

This round does not estimate the reciprocal resonance union and cannot
promote the hard-top energy, M9-M2, M9, endpoint uniformity, or the global
exponent.
