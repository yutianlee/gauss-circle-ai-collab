# Round 188 statement-only imprimitive Fourier-lift problem

This packet is self-contained. Do not use a proof graph, strategy file,
prior round, sibling report, source, or conductor analysis.

Put (e(z)=\exp(2\pi iz)). Fix real (X\ge2), (L\ge2),
(\sigma\in\{+1,-1\}), (B>0), and

\[
R_0=\lceil L\rceil,
\qquad Q=H_B=\lfloor(\log(2X))^B\rfloor.
\tag{B188.1}
\]

For every squarefree positive integer (N), an allocation-independent
rule selects at most one unordered pair of distinct odd prime divisors
(\{p_N,q_N\}) with (\chi_4(p_Nq_N)=-1). Define

\[
\rho_N(d)=
\begin{cases}
1,&\text{no pair is selected},\\
1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
+2\mathbf1_{p_Nq_N\mid d},&\text{a pair is selected}.
\end{cases}
\tag{B188.2}
\]

Let (A_{L,X}^{\sigma}(m,d)) be one fixed literal coefficient, not an
arbitrary array. It is zero off every original shell, height, strict
(4m<d<16m) cone, profile, floor, star, half-weight, hard sample,
crossing, endpoint, sign, squarefree, coprimality, and zero-extension
predicate. On support (m,d\asymp L) and

\[
|A_{L,X}^{\sigma}(m,d)|\ll_\varepsilon X^\varepsilon.
\tag{B188.3}
\]

No variation, density, equidistribution, Fourier norm, or translation
invariance of this literal coefficient may be invented. Put

\[
\lambda_{N,\sigma}(d)=
\begin{cases}
\mu^2(N)\rho_N(d)A_{L,X}^{\sigma}(N/d,d),
 &N,d>0,\ \mu^2(N)=1,\ d\mid N,\ 2\nmid d,\\
0,&\text{otherwise},
\end{cases}
\tag{B188.4}
\]

including zero extension outside positive integer arguments.

The primitive outer labels are

\[
\mathfrak f=(\kappa,g,h,U,v),\quad
\kappa,g,h,U,v>0,\quad \kappa,g,U\text{ odd},
\quad(gU,v)=1,\quad(U,h)=1,
\quad0<2\kappa gh<R_0.
\tag{B188.5}
\]

For (U>1), let (\bar v) be the inverse of (v\bmod U) and set

\[
\begin{array}{lll}
+:&S_{0,+}=[\bar vh]_U,&w_{0,+}=(S_{0,+}v-h)/U,\\[1mm]
-:&S_{0,-}=[-\bar vh]_U,&w_{0,-}=(h+vS_{0,-})/U.
\end{array}
\tag{B188.6}
\]

For (\omega\in\{+,-\}), put

\[
S_{t,\omega}=S_{0,\omega}+Ut,\qquad
s_{t,\omega}=gS_{t,\omega},\qquad
w_{t,\omega}=w_{0,\omega}+vt,
\tag{B188.7}
\]

\[
I_{\mathfrak f,\omega}
=\{t\in\mathbb Z:S_{t,\omega}>0,\ w_{t,\omega}>0\}.
\tag{B188.8}
\]

Positivity is imposed before each square-root evaluation. Put
(r=2\kappa gh). In the plus orientation define

\[
N_{\mathfrak f,t}^{+}
=\kappa gU(\kappa v+2w_{t,+}),\qquad
N_{\mathfrak f,t}^{+}+r
=(\kappa gU+2s_{t,+})\kappa v,
\tag{B188.9}
\]

\[
\begin{aligned}
B_{\mathfrak f,+}^{\sigma}(t)={}&
\left(1-\frac r{R_0}\right)
\lambda_{N_{\mathfrak f,t}^{+}+r,\sigma}
 (\kappa gU+2s_{t,+})
\overline{\lambda_{N_{\mathfrak f,t}^{+},\sigma}(\kappa gU)}\\
&\times e\!\left(
\frac{\sigma\sqrt X\,r}
{\sqrt{N_{\mathfrak f,t}^{+}+r}
+\sqrt{N_{\mathfrak f,t}^{+}}}\right).
\end{aligned}
\tag{B188.10}
\]

In the minus orientation define

\[
N_{\mathfrak f,t}^{-}
=(\kappa gU+2s_{t,-})\kappa v,\qquad
N_{\mathfrak f,t}^{-}+r
=\kappa gU(\kappa v+2w_{t,-}),
\tag{B188.11}
\]

\[
\begin{aligned}
B_{\mathfrak f,-}^{\sigma}(t)={}&
\left(1-\frac r{R_0}\right)
\lambda_{N_{\mathfrak f,t}^{-}+r,\sigma}(\kappa gU)
\overline{\lambda_{N_{\mathfrak f,t}^{-},\sigma}
 (\kappa gU+2s_{t,-})}\\
&\times e\!\left(
\frac{\sigma\sqrt X\,r}
{\sqrt{N_{\mathfrak f,t}^{-}+r}
+\sqrt{N_{\mathfrak f,t}^{-}}}\right).
\end{aligned}
\tag{B188.12}
\]

For odd (U>1), define

\[
c_U(k)=\frac{2}{U\{1+e(-k/U)\}},\qquad
q_U(k)=\frac{U}{(k,U)},\qquad
|k|_U=\min(k,U-k).
\tag{B188.13}
\]

For every nonempty dyadic block (Y<h\le2Y) with (Y>Q), the exact
remaining high packet is

\[
\boxed{
\begin{aligned}
\mathscr R_{Y,Q}^{\sigma}:={}&
\sum_{\omega\in\{+,-\}}
\sum_{\substack{\mathfrak f\text{ satisfying }(\mathrm{B188.5})\\
Y<h\le2Y,\ U>4Q}}
\sum_{\substack{1\le k<U\\q_U(k)>Q,\ |k|_U>Q}}
c_U(k)e(\epsilon_\omega k\bar vh/U)\\
&\hspace{28mm}\times
\sum_{t\in I_{\mathfrak f,\omega}}
(-1)^tB_{\mathfrak f,\omega}^{\sigma}(t),
\qquad \epsilon_+=1,\ \epsilon_-=-1.
\end{aligned}}
\tag{B188.14}
\]

There is one real part outside every term in (B188.14). The target is

\[
\boxed{
\Re\mathscr R_{Y,Q}^{\sigma}
\ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{B188.15}
\]

The complete positive capacity is (O(YL^2X^\varepsilon)), so the
missing gain is the full factor (Y).

You may use only after verifying it: for every mode in (B188.14), put

\[
m=(k,U),\qquad U=mq,\qquad k=ma,\qquad(a,q)=1.
\tag{B188.16}
\]

Then

\[
c_U(k)=\frac1m c_q(a),\qquad
e(\epsilon_\omega k\bar vh/U)
=e(\epsilon_\omega a\bar vh/q),
\tag{B188.17}
\]

and

\[
\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}|c_q(a)|
\ll\log(2q).
\tag{B188.18}
\]

The literal support also gives, with (u=gU),

\[
u,v\asymp L/\kappa,\qquad h\ll U,
\tag{B188.19}
\]

and at fixed ((\kappa,u,U,h)), both orientations together contain
(O(L)) live ((v,t))-atoms. Therefore the dyadic block contains at
most (O(YL)) atoms at fixed ((\kappa,u,U)). Verify this multiplicity
from the endpoint parametrization rather than treating it as a density
or nonemptiness assertion.

Independently do all of the following.

1. Verify the carrier, endpoints, both orientations, parity signs,
   positivity, Fourier normalization, unique lift coordinates, phase,
   and multiplicity one.
2. Split (B188.14) exactly into

   \[
   Q(k,U)\ge Y
   \qquad\text{and}\qquad
   Q(k,U)<Y.
   \tag{B188.20}
   \]

3. Prove or refute that the complete first sector in (B188.20) has
   absolute size (O_{B,\varepsilon}(L^2X^\varepsilon)), restoring the
   (\kappa,u,U,m,q,Y,L,X) powers and every divisor multiplicity.
4. Keep the second sector jointly signed under one outer real part.
   Attempt (B188.15) by exact reciprocity, completion, determinant
   transposition, or a squarefree-sieve opening only if every required
   literal-coefficient hypothesis is proved.
5. Test terminal dyadic blocks, near-half modes, prime conductors,
   arithmetic deletions, endpoint changes, and adversarial bounded arrays.
   Positive energy or an arbitrary-weight theorem is not cancellation.
6. Give either a proof of (B188.15), the widest target-safe exact sector
   with its exact complement, or a rigorous no-go and the first additional
   actual-coefficient relation needed.

Success affects only the exact original-(t=1) residual after separate
accepted connectors. It proves no (t\ge2), near-resonant, parent,
endpoint, bridge, global theorem, or exponent. Computation is diagnostic
only.

Return exactly:

1. Result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required control test and outcome.
6. Dependencies and exact artifacts used.
7. Recommended state effect.
