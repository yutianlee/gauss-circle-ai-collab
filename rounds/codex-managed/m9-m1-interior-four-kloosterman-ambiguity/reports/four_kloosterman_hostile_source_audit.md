# Hostile/source audit of the interior four-Kloosterman ambiguity

## 1. Result

**Mixed result: a new lower-interior deletion, followed by a sharp
source no-go.**  Put

\[
 D_1=\lfloor J^{87/140}\rfloor.
\]

The literal third-derivative estimate on each progression
\(n=r+M\ell\), combined with the exact periodic residue \(L^1\) bound,
proves

\[
 {1\over M^2}\sum_{b\asymp B}
 \sum_{D_0<|d|\le D_1}\sum_n
 A_{M,K,d}(n)I_b(n+d)\overline{I_b(n)}
 \ll_\varepsilon X^\varepsilon J^2/T.                             \tag{1.0}
\]

This holds uniformly for all three local classes, both signs,
reflected orientations, arbitrary composite and prime-power moduli,
nonzero modulus-multiple differences, and the centered Ramanujan term.
Since \(87/140-17/30=23/420>0\), it deletes a nonempty power-length
part of the interior.  The exact remaining smooth-principal survivor is

\[
 \mathfrak Y_{>D_1}={1\over M^2}\sum_{b\asymp B}
 \sum_{D_1<|d|<\Delta_b-E_*}\sum_n
 A_{M,K,d}(n)I_b(n+d)\overline{I_b(n)}.                            \tag{1.0a}
\]

Neither the continuously twisted physical-row identity followed by
multiplier triangle inequality nor a presently published complete
rational-trace, prime-power, or bilinear Kloosterman theorem proves

\[
 \mathfrak Y_{>D_1}\ll_\varepsilon X^\varepsilon J^2/T.
\]

The physical-row route keeps the valuable \(Q^{-5/12}\) energy factor,
but its literal triangle-inequality capacity is
\(X^\varepsilon C^3/(TQ^{5/12})\), with no power of \(B\).  At
\(C=J^{3/4}\) this exceeds the target by
\(J^{1/12}=B^{5/9}\).  A unit-plateau multiplier cannot repair this,
because its Fourier kernel has \(L^1\)-norm at least one.

The literal \(d\)-A-process has a target-safe diagonal, but its first
unsupported term is the signed, weighted four-Kloosterman correlation
with the actual \((b,d,u,n,m)\)-dependent stationary symbol.  More
strongly, the natural coefficientwise substitute for that term is
false.  If

\[
 \mathfrak T_M(u,v;h_1,h_2):=
 \sum_{a\bmod M}\mathcal C_{M,K}(a+u,h_1)
 \overline{\mathcal C_{M,K}(a,h_2)}e_M(-va),
\]

then exact completion gives a four-denominator rational phase.  On the
literal self-return slice \(v=0,h_1=h_2\), its reciprocal part cancels
identically.  For \(M=p^\nu\), \(p\) odd, \(\nu\ge2\),
\(h_1=h_2=p^{\nu-1}\), and
\(u=p^{\nu-1}\alpha\) with \(p\nmid\alpha\),

\[
 \boxed{\mathfrak T_{p^\nu}
   (p^{\nu-1}\alpha,0;p^{\nu-1},p^{\nu-1})
   =-p^{2\nu-1}.}
\]

Thus its magnitude is \(M^{2-1/\nu}\); for every fixed
\(\nu>2\) this contradicts a uniform
\(O_\varepsilon(M^{3/2+\varepsilon})\) complete-mode estimate for
sufficiently small \(\varepsilon\).  At \(u\equiv0\pmod M\), in
particular at the A-process shift \(u=M\), the value is the full
self-return \(M\varphi(M)=p^{2\nu}-p^{2\nu-1}\).  Hence restricting to
\(U\le M\) avoids the first exact period but does not avoid the large
prime-power near-return \(u=M/p\).

The obstruction is not confined to powerful moduli.  If
\(M=\ell R\), where \(\ell\) is any fixed odd prime and
\((\ell,R)=1\), then at

\[
 u=h_1=h_2=R=M/\ell,\qquad v=0,
\]

one has the second exact evaluation

\[
 \boxed{\mathfrak T_{\ell R}(R,0;R,R)
   =\ell R\,\varphi(R)\bigl(-1-e_\ell(R)\bigr).}                    \tag{1.1}
\]

For fixed odd \(\ell\), the last factor is bounded away from zero.
Taking \(R=q\) prime makes \(M=\ell q\) squarefree and gives size
\(\asymp_\ell M^2\), at the shift \(u=M/\ell<M\).  Thus squarefree CRT
does not remove the no-go: it replaces high p-adic valuation by a large
\((u,M)\) and an exact local self-return on the \(R\)-factor.

This calculation does **not** prove that the actual signed weighted
aggregate is large: its stationary symbol may cancel these modes after
joint summation.  It proves that such joint cancellation is an
indispensable new input.  The targeted primary-source audit current to
2026-08-16 found no theorem that supplies it for unrestricted
\(M\in\{b,2b,4b\}\), including arbitrary prime powers and the
\(2\)-part, while retaining the actual stationary symbol, all
Ramanujan terms, and the physical \(Q^{-5/12}\) factor.

## 2. Exact statement and hypotheses

Put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad B=C/T,
 \qquad J^{13/18}<C\le J^{3/4},
\]

and, for each compatible local class,

\[
 (g,M,K)\in
 \{(1,4b,k),(2,2b,2[k\bar4]_b),(4,b,[k\bar4]_b)\},
 \qquad gM=4b,\qquad b\asymp B.
\]

There is no squarefree, prime, odd-modulus, or \((K,M)=1\) hypothesis.
For a fixed class, alias, stationary sign, and reflected orientation,
let \(I_b\) be the accepted stationary transform, supported on an
integer interval of length \(\Delta_b\asymp Q^2\), with

\[
 |I_b(n)|\ll_\varepsilon X^\varepsilon H_0,
 \qquad H_0={C\sqrt T\over J},
\]

and with principal phase
\(-\eta\lambda_b\sqrt{|n|}\),
\(\lambda_b=\sqrt X+\sqrt{\kappa k}/b\).  Define

\[
 A_{M,K,d}(n)=S(n+d,K;M)\overline{S(n,K;M)}-c_M(d),
\]

\[
 D_0=\lfloor J^{17/30}\rfloor,
 \qquad D_1=\lfloor J^{87/140}\rfloor,
 \qquad E_*=\lfloor Q^2J^{-1/20}\rfloor=\lfloor J^{3/4}\rfloor.
\]

The only object under audit is

\[
 \mathfrak Y_{\rm int}={1\over M^2}\sum_{b\asymp B}
 \sum_{D_0<|d|<\Delta_b-E_*}\sum_n
 A_{M,K,d}(n)I_b(n+d)\overline{I_b(n)}.                 \tag{2.1}
\]

Both signs of \(d\), reflected orientations, every nonzero
\(d\equiv0\pmod M\), and all local unit restrictions remain in (2.1).
Small differences, the outer support edge, entry/exit terms,
stationary remainders, and wrong-sign/nonstationary tails have already
been routed exactly once.  Raw Farey-transition errors and axes are not
part of (2.1).

The new direct estimate used below is the following precise interface.
For \(e=|d|\le D_1\), after reindexing a negative difference and/or a
reflected support, the principal phase on a progression is, up to an
irrelevant sign,

\[
 f_{b,e,r}(\ell)=\lambda_b
 \left(\sqrt{m+e}-\sqrt m\right),\qquad m=r+M\ell\asymp Q^2.        \tag{2.1a}
\]

The phase-removed product on that progression has sampled supremum
plus total variation

\[
 \ll_\varepsilon X^\varepsilon H_0^2,                              \tag{2.1b}
\]

uniformly in \(b,e,r\), and the progression length is
\(L\ll Q^2/M+1\).  Moreover

\[
 |f_{b,e,r}^{(3)}(\ell)|\asymp
 \rho_{b,e}:={JM^3e\over Q^7}.                                    \tag{2.1c}
\]

The weighted third-derivative estimate and
\(M^{-2}\sum_{r\bmod M}|A_{M,K,d}(r)|\le2\) then give, for each
\((b,d)\),

\[
 \left|M^{-2}\sum_n A_{M,K,d}(n)
 I_b(n+d)\overline{I_b(n)}\right|
 \ll_\varepsilon X^\varepsilon H_0^2
 \left(L\rho_{b,e}^{1/6}+L^{1/2}\rho_{b,e}^{-1/6}+1\right).        \tag{2.1d}
\]

For \(h\not\equiv0\pmod M\), use the exact finite Fourier coefficient

\[
 \mathcal C_{M,K}(a,h)=
 \sum_{\substack{y\bmod M\\(y(y+h),M)=1}}
 e_M\!\left(a(y+h)+K\big((y+h)^{-1}-y^{-1}\big)\right),             \tag{2.2}
\]

so that

\[
 A_{M,K,d}(n)=\sum_{h\ne0}\mathcal C_{M,K}(d,h)e_M(hn).             \tag{2.3}
\]

The hostile completion lemma proved here is the exact identity

\[
\boxed{
\begin{aligned}
 \mathfrak T_M(u,v;h_1,h_2)
 &=M\!\sum_{\substack{x\bmod M\\
 x,x-h_1,x-v,x-v-h_2\in(\mathbb Z/M\mathbb Z)^\times}}
 e_M\!\left(ux+K\Phi_{h_1,h_2,v}(x)\right),\\
 \Phi_{h_1,h_2,v}(x)
 &=x^{-1}-(x-h_1)^{-1}-(x-v)^{-1}+(x-v-h_2)^{-1}.
\end{aligned}}                                                     \tag{2.4}
\]

In particular,

\[
 \mathfrak T_M(u,0;h,h)
 =M\sum_{\substack{x\bmod M\\(x(x-h),M)=1}}e_M(ux).               \tag{2.5}
\]

The prime-power specialization in Section 1 follows from (2.5) and is
independent of \(K\).  It is therefore a literal obstruction even in
the locally good case \(p\nmid K\), not an artifact of bad primes of
the fixed parameter.

For a residual middle interval contained in
\(D_1<|d|<\Delta_b-E_*\), of length \(D\), put

\[
 Z_b(d)=M^{-2}\sum_n A_{M,K,d}(n)
 I_b(n+d)\overline{I_b(n)},                                        \tag{2.6}
\]

extended by zero off that interval.  For \(1\le U\le D\), a sufficient
literal off-diagonal input (with absolute values after the inner signed
correlation) is

\[
\begin{aligned}
 \mathcal E_1(D,U):={}&
 \sum_{b\asymp B}\sum_{1\le u<U}(U-u)
 \left|\sum_d Z_b(d+u)\overline{Z_b(d)}\right|,\\
 \mathcal E_1(D,U)\ll{}&X^\varepsilon
 {U^2\over B(D+U)}J^{14/5}.                                       \tag{2.7}
\end{aligned}
\]

An equally admissible new theorem could instead control the
outside-absolute signed Fejer aggregate at the corresponding scale.
In either formulation it must use, not discard, the full symbol

\[
 \Omega_{b,d,u}(n,m)=
 I_b(n+d+u)\overline{I_b(n)}
 \overline{I_b(m+d)}I_b(m),                                       \tag{2.8}
\]

whose principal phase is, on a fixed compatible sign branch,

\[
 -\eta\lambda_b\bigl(\sqrt{|n+d+u|}-\sqrt{|n|}
 -\sqrt{|m+d|}+\sqrt{|m|}\bigr).                                  \tag{2.9}
\]

It must also include the two Ramanujan cross terms and the
Ramanujan-square term created by expanding the two centered kernels in
(2.6).  No arbitrary-weight or coefficient-blind replacement is among
the hypotheses.

## 3. Proof or derivation

**Third-derivative deletion of \(D_0<|d|\le D_1\).**  Write
\(e=|d|\).  On the active positive-frequency support, both stationary
indices have size \(\asymp Q^2\).  Since

\[
 {D_1\over Q^2}\ll J^{-5/28},                                     \tag{3.0a}
\]

they stay in the same sign and in a fixed enlarged stationary band.
For \(d<0\), translating the summation index by \(e\) turns the phase
into the conjugate of the \(d>0\) phase; it merely translates the
periodic coefficient \(A_{M,K,-e}\), whose residue \(L^1\)-norm is
unchanged.  Replacing the stationary support by its reflection has the
same effect on the phase sign.  It is therefore enough to study
(2.1a).

Three differentiations, including the chain factor \(M^3\), give

\[
 f_{b,e,r}^{(3)}(\ell)
 ={3\lambda_bM^3\over8}
 \left((m+e)^{-5/2}-m^{-5/2}\right)
 =-{15\lambda_bM^3e\over16}\xi^{-7/2}                              \tag{3.0b}
\]

for some \(m<\xi<m+e\).  Here \(\lambda_b\asymp J\), and (3.0a)
gives \(m,\xi,m+e\asymp Q^2\) uniformly.  Thus (2.1c) holds with a
fixed sign and fixed comparability constants.  Across the full frozen
range,

\[
 J^{-13/15}\ll\rho_{b,e}\ll J^{-51/70}<1,                          \tag{3.0c}
\]

so the standard third-derivative estimate is uniform and nontrivial
on \(L\asymp Q^2/M\) points.

Let
\(P_b(n)=e(\eta\lambda_b\sqrt{|n|})I_b(n)\) on the active branch.
The accepted sampled bounded-variation hierarchy gives
\(\|P_b\|_\infty+\operatorname{Var}P_b
\ll_\varepsilon X^\varepsilon H_0\) on every relevant progression.
The elementary product-variation inequality therefore proves (2.1b),
uniformly under the translate by \(d\); extension by zero owns the
support endpoints.  Partial summation applied to

\[
 \sum_\ell P_b(r+M\ell+d)\overline{P_b(r+M\ell)}
 e\bigl(\mp f_{b,e,r}(\ell)\bigr)
\]

and the unweighted third-derivative bound yields the bracket in
(2.1d).  Finally split \(n=r+M\ell\).  Periodicity of \(A_d\) and the
exact all-modulus identity

\[
 {1\over M^2}\sum_{r\bmod M}|A_{M,K,d}(r)|\le2                    \tag{3.0d}
\]

spend the external \(M^{-2}\) exactly once and prove (2.1d), without
opening a Kloosterman sum or separating its Ramanujan subtraction.

Now \(M\asymp B\),
\(H_0^2=B^2J^{-1/5}\), \(Q=J^{2/5}\).  Summing (2.1d) over both signs,
\(b\asymp B\), and \(D_0<e\le D\) gives

\[
 \ll_\varepsilon X^\varepsilon\left(
 B^{5/2}J^{3/10}D^{7/6}
 +B^2J^{1/2}D^{5/6}
 +B^3J^{-1/5}D\right).                                            \tag{3.0e}
\]

At \(B\le J^{3/20}\) and \(D=D_1=J^{87/140}+O(1)\), the three
exponents of \(J\) are respectively

\[
 {7\over5},\qquad {369\over280},\qquad {61\over70}.               \tag{3.0f}
\]

The first exactly meets the target and the other two are strictly
smaller.  This proves (1.0).  It is uniform in the bounded ratios
\(M/b\in\{1,2,4\}\), in every local \(K\), and in modulus-multiple
differences.  Exact integer phase values cause no exception to a
third-derivative bound.  The already routed stationary and entry/exit
errors are not reintroduced; hence the new exact survivor is (1.0a).
This direct deletion does not spend or replace the inherited physical
row estimate, so \(Q^{-5/12}\) remains available on (1.0a).

**The physical-row capacity.**  The exact continuously twisted identity
is

\[
 \mathcal G_b(\theta)={1\over M^2}\sum_{d,n}
 A_{M,K,d}(n)I_b(n+d)\overline{I_b(n)}e(d\theta),
\]

and the reciprocal row is uniformly
\(O_\varepsilon(X^\varepsilon TQ^{-5/24})\).  Pairing a difference
multiplier \(w\) with \(\mathcal G_b\) and applying triangle inequality
therefore gives

\[
 X^\varepsilon\|K_w\|_1{C^3\over TQ^{5/12}}.                       \tag{3.1}
\]

If \(w(d_*)=1\) anywhere on its retained plateau, Fourier inversion
gives \(1=|w(d_*)|\le\|K_w\|_1\).  Relative to the target, (3.1) costs

\[
 {C^3/(TQ^{5/12})\over J^2/T}
 ={C^3\over J^{13/6}}.                                             \tag{3.2}
\]

At \(C=J^{3/4}\), (3.2) is \(J^{1/12}=B^{5/9}\).  Thus the identity
preserves \(Q^{-5/12}\), but multiplier triangle alone produces no
conductor saving.  Even an additional \(B^{-1/2}\) would leave
\(J^{1/120}\) at the endpoint and reaches only
\(C\le J^{56/75}\).

**The compulsory A-process term.**  Fejer/van der Corput followed by
Cauchy over \(b\) contains its full prefactor, its diagonal, and the
weights \(U-u\).  The accepted diagonal is below the target.  For
\(u\ne0\), however,

\[
 \sum_dZ_b(d+u)\overline{Z_b(d)}
 =M^{-4}\sum_{d,n,m}A_{d+u}(n)\overline{A_d(m)}
 \Omega_{b,d,u}(n,m).                                               \tag{3.3}
\]

Opening \(A_{d+u}\overline{A_d}\) gives exactly one four-Kloosterman
main term, two Ramanujan cross terms, and one Ramanujan-square term.
Taking any of these terms absolutely before exploiting (2.8) changes
the problem.  With \(U\le M\asymp B\), diagonal-only differencing has
at most the formal \(B^{-1/2}\) gain recorded above.  Taking
\(U>M\) includes \(u=M\), where the arithmetic coefficient is an exact
self-return; (2.5) also shows large p-adic near-returns before that
point.

**Completion identity.**  Substitute (2.2) twice in
\(\mathfrak T_M\), with summation variables \(y,z\).  The coefficient
of \(a\) is

\[
 (y+h_1)-(z+h_2)-v.
\]

Orthogonality in \(a\) forces
\(z=y+h_1-h_2-v\) and contributes \(M\).  Setting \(x=y+h_1\)
turns the four unit conditions into

\[
 x,\quad x-h_1,\quad x-v,\quad x-v-h_2\quad\hbox{units modulo }M,
\]

and the remaining phase is exactly the phase in (2.4).  If
\(v=0,h_1=h_2=h\), the four reciprocal terms cancel in pairs, proving
(2.5).  In particular \(u\equiv0\pmod M\) gives

\[
 \mathfrak T_M(0,0;h,h)=MN_M(h),                                   \tag{3.4}
\]

the exact ambiguity self-return.

Now take \(M=p^\nu\), \(h=p^{\nu-1}\), and
\(u=p^{\nu-1}\alpha\), with \(p\) odd and \(p\nmid\alpha\).  Since
\(p\mid h\), \(x-h\) is a unit exactly when \(x\) is, and hence

\[
\begin{aligned}
 \mathfrak T_{p^\nu}(u,0;h,h)
 &=p^\nu\sum_{x\bmod p^\nu}^{*}e_p(\alpha x)\\
 &=p^\nu p^{\nu-1}\sum_{r\bmod p}^{*}e_p(\alpha r)
 =-p^{2\nu-1}.                                                      \tag{3.5}
\end{aligned}
\]

For \(u\equiv0\pmod {p^\nu}\), the same computation gives
\(p^\nu\varphi(p^\nu)\).  Equation (3.5) is an exact member of the
family and needs no numerical experiment.  It refutes a uniform
coefficientwise square-root bound, while leaving open the possibility
of cancellation against the actual transform of (2.8).

The squarefree/composite evaluation (1.1) is just as direct.  Put
\(M=\ell R\), \((\ell,R)=1\), and \(u=h=R\) in (2.5).  Modulo \(R\),
the two unit conditions coincide and there are \(\varphi(R)\) choices.
Moreover \(e_M(Rx)=e_\ell(x)\).  Modulo \(\ell\), the condition is
\(x\not\equiv0,R\), so

\[
 \sum_{\substack{x\bmod\ell\\x\ne0,R}}e_\ell(x)
 =-1-e_\ell(R).
\]

CRT proves (1.1).  Because an odd-order root of unity cannot equal
\(-1\), this factor is nonzero; for fixed \(\ell\) its magnitude has a
positive lower bound.  In the especially transparent case \(\ell=3\),
the magnitude is exactly one.  Consequently the large aligned modes
are not a power-sparse collection of prime-power moduli.

**Prime-local rational-phase check and squarefree gcd loss.**  Let
\(p\) be odd with \(p\nmid K\).  Over \(\mathbb F_p\), the finite poles
of the reciprocal part of (2.4), with signed multiplicity, are

\[
 \{0,v+h_2\}_{+}\quad\hbox{and}\quad\{h_1,v\}_{-}.                  \tag{3.6}
\]

If \(h_1,h_2\ne0\pmod p\), these multisets agree, and hence all
rational poles cancel, exactly when
\(v=0,h_1=h_2\).  If local Fourier modes are allowed to vanish, there
is one further cancellation branch:
\(h_1=h_2=0\), with arbitrary \(v\).  This extra branch matters after
CRT, because a globally nonzero \(h_i\bmod M\) can vanish at some
prime factors.  Outside these branches at least one simple pole
remains.  A rational function of the form \(G^p-G+c\) cannot have a
simple pole, so the phase is not Artin--Schreier degenerate; the Weil
bound gives \(O(\sqrt p)\) for the inner sum in (2.4), hence
\(O(p^{3/2})\) after restoring its outer factor \(p\).  When the poles
cancel, the phase is \(ux\): it is constant only if \(u=0\pmod p\).
For \(u\ne0\) the punctured linear sum is \(O(1)\); for \(u=0\) it has
size \(p+O(1)\) and gives the local diagonal loss.

For a squarefree modulus coprime to \(2K\), CRT therefore yields, up to
\(M^\varepsilon\), the schematic sharp hypothesis map

\[
 |\mathfrak T_M(u,v;h_1,h_2)|
 \ll_\varepsilon M^{3/2+\varepsilon}\mathfrak r^{1/2},             \tag{3.7}
\]

where \(\mathfrak r\) is the product of primes \(p\mid M\) for which

\[
 p\mid u,\qquad
 \bigl[p\mid v,\ p\mid(h_1-h_2)\bigr]
 \quad\hbox{or}\quad
 \bigl[p\mid h_1,\ p\mid h_2\bigr].                               \tag{3.8}
\]

Primes dividing \(2K\) require a separate bounded-prime local ledger.
The factor \(\mathfrak r^{1/2}\) is not an \(M^\varepsilon\) nuisance:
global self-return has \(\mathfrak r=M\), and (1.1) has
\(\mathfrak r\) containing the full \(R\)-factor.  Therefore even an
optimal generic prime-field theorem leaves a genuine divisor-aligned
aggregate to estimate against (2.8).

**Literal primary-source map.**  Normalizations are essential here.
The Kloosterman sums in (2.1) are unnormalized.  In sources using a
bounded normalized trace function, four such unnormalized factors
restore a factor \(p^2\).  In Zheng's convention the finite Fourier
transform includes \(q^{-1/2}\), so a displayed bound for
\(\widehat Y\) must be multiplied by \(q^{1/2}\) to recover the raw
complete sum.

| Primary source and theorem | Literal hypothesis/result | Verdict for (2.1)--(2.9) |
|---|---|---|
| Fouvry--Kowalski--Michel, [*A study in sums of products*, Corollaries 1.6--1.7, arXiv:1405.2293v2](https://arxiv.org/html/1405.2293) | A bounded-conductor bountiful trace sheaf over the prime field \(\mathbb F_p\); square-root cancellation for a normal tuple or a nonzero additive twist.  Corollary 1.7 gives a main term of order \(p\) for paired non-normal tuples. | It agrees with the generic prime-local check (3.6), but only after a normality check.  It has no prime powers, composite residue rings, or \(2\)-part.  The constant self-return slice is precisely paired/non-normal, local zero modes create the second CRT cancellation branch, and the real weight (2.8) is not a bounded-conductor finite-field trace function. |
| Zheng, [*Primes in simultaneous arithmetic progressions*, Lemma 2.7, arXiv:2512.22798v1](https://arxiv.org/html/2512.22798) | For prime \(p\), a complete additive twist of a product of shifted unnormalized Kloosterman sums is \(\ll\delta_p p^{k/2}\), with \(\delta_p=p\) when the twist is zero and every shift has even multiplicity, and \(p^{1/2}\) otherwise. | The theorem itself records the exact type of diagonal exception met here.  It is prime-only and complete/unweighted; it gives no aggregate theorem for (3.3). |
| Zheng, same paper, Lemma 2.8 | For **squarefree** \(q\), the normalized Fourier transform of the special parallelogram \(Y(t)=S(t,\xi)S(t+\ell_1,\xi)S(t+\ell_2,\xi)S(t+\ell_1+\ell_2,\xi)\) is \(\ll q^{2+\varepsilon}(\ell_1,v,q)^{1/2}(\ell_2,v,q)^{1/2}(\xi,\ell_1,\ell_2,q)^{3/2}\). | The four arguments in (3.3) are not this parallelogram for general \(u\); even matching slices inherit the displayed exceptional gcd factors.  Equations (1.1) and (3.7)--(3.8) show why those factors cannot be suppressed even for squarefree moduli.  Unrestricted higher powers, the \(2\)-part, and (2.8) are absent.  The normalized \(q^{2+\varepsilon}\) is a raw \(q^{5/2+\varepsilon}\) generic bound before gcd losses, not a missing normalization gain. |
| Zheng, same paper, Lemma 2.10 (a specialization of Wu--Xi, [Theorem A.1, arXiv:1603.07060v5](https://arxiv.org/abs/1603.07060)) | A complete bounded-degree rational phase modulo \(q\), but only when every prime exponent in \(q\) is at most two.  The estimate is \(q^{1/2}\) times coefficient and derivative gcd factors, including \((\lambda',q_2)\) at squared primes. | This is the closest theorem to the inner sum in (2.4).  It does not cover \(p^\nu\parallel M\) for \(\nu\ge3\).  On \(v=0,h_1=h_2\), the reciprocal phase cancels; when \(u\) has high p-adic valuation the derivative gcd factor loses the asserted saving (for \(p^2,u=p\alpha\), it already permits the trivial inner bound).  It is a complete one-variable estimate, not the required sum over its exceptional strata with (2.8). |
| Zheng, same paper, Lemma 2.15 | An \(A^2B\) inequality after a chosen factorization \(q=q_0q_1q_2\); its decisive input is a Fourier bound for a complete fourfold parallelogram \(Z\) on the \(q_0\)-factor. | No such uniformly useful factorization is frozen for arbitrary \(M\), and the required \(\widehat Z\) bound is exactly where aligned/gcd modes occur.  The lemma does not supply the actual \(b,d,u,n,m\) aggregate or preserve \(Q^{-5/12}\) by itself. |
| Milićević--Zhang, [*Distribution of Kloosterman paths to high prime power moduli*, Theorem 4, arXiv:2005.08865v1](https://arxiv.org/html/2005.08865) | High powers \(p^n\) of one fixed odd prime, on specified p-adic domains.  Its complete phase sum either has a power saving or two active shifts collide modulo \(p^{\lfloor\delta_2n\rfloor}\). | The self-return and (3.5) are in the collision alternative, for which the theorem deliberately asserts no saving.  It supplies no varying arbitrary-composite theorem, no \(2\)-adic component, and no estimate with the actual archimedean symbol (2.8). |
| Kerr--Shparlinski--Wu--Xi, [*Bounds on bilinear forms with Kloosterman sums*, Lemma 4.1, arXiv:2204.05038v5](https://arxiv.org/html/2204.05038) | For arbitrary \(q\), a gcd-sensitive bound for \(q^{-1}\sum_t\mathscr K_q(x,t)\mathscr K_q(y,t)e_q(-zt)\), where both kernels have the same varying second argument \(t\) and fixed \(x,y\). | The present pair has shifted varying arguments, and (3.3) has four kernels.  There is no literal parameter substitution.  Completing again gives (2.4), including its self-return, rather than a theorem for (2.8). |
| Pascadi, [*Non-abelian amplification and bilinear forms with Kloosterman sums*, arXiv:2511.08445v2](https://arxiv.org/abs/2511.08445); Blomer--Pascadi, [*Bilinear forms with Kloosterman sums via quadratic characters*, arXiv:2607.24311v1](https://arxiv.org/abs/2607.24311); Milićević--Qin--Wu, [*Bilinear forms with Kloosterman sums and moments of twisted L-functions*, arXiv:2511.07550v1](https://arxiv.org/abs/2511.07550) | Bilinear estimates for a single Kloosterman kernel with separated coefficient sequences and source-specific length/factorization hypotheses. | Cauchy cannot turn the remaining Kloosterman factors and (2.8) into independent harmless coefficients: they depend on the same variables.  The fixed-column specialization also loses the populated second variable.  None is a four-Kloosterman aggregate theorem or a carrier of the physical row saving. |

The rational-phase result is therefore **not** a usable aggregate bound
for the literal family with its actual stationary symbol.  At most it
controls generic complete local pieces after one separately (i) limits
prime exponents to at most two, (ii) counts every coefficient/derivative
gcd stratum, (iii) handles the exact paired strata such as (3.5), and
(iv) proves that completion and recombination with (2.8) meet (2.7).
Those four steps are the missing argument, not consequences of the
cited theorem.  This is not cured by a sparsity assertion: for fixed
\(\ell\), (1.1) ranges over a full dyadic family \(R\asymp B/\ell\),
and its mode \(h=u=R\) becomes a bounded-modulus twist on the remaining
\(\ell\)-factor.  Nothing in the accepted support/BV hypotheses forces
the corresponding \(v=0\) transform of (2.8) to vanish.  Proving its
cancellation is an actual-symbol problem; summing the gcd losses
absolutely is not a substitute and does not recover \(Q^{-5/12}\).
The targeted search found no current primary theorem that performs
this aggregate calculation.

**Perfect-power hostile control.**  The stationary phase also has exact
arithmetic resonances.  On an admissible subsequence with
\(J\in\mathbb Z\) and \(\sqrt{\kappa k}\in\mathbb Z\), square pairs
\(n=r^2,n+d=s^2\) with \(b\mid(s-r)\) make the phase difference
integral.  More explicitly, with \(a\asymp J^{1/5}\),

\[
 n=a^4,\qquad n+d=(a+b)^4,
 \qquad d\asymp J^{3/5}B,
\]

lies in the middle range because
\(J^{11/90}<B\le J^{3/20}\), and swapping the two values gives negative
\(d\).  Hence a blanket nonresonance argument is false.  The complete
literal perfect-power lattice was already bounded absolutely below the
target in the permitted Round-85 audit, so this is a seam to isolate,
not evidence that (2.1) itself is large.

## 4. First doubtful or unproved step

After the proved deletion (1.0), the first unproved step is precisely a
bound of the strength (2.7), or its outside-absolute signed analogue,
for (3.3) restricted to
\(D_1<|d|<\Delta_b-E_*\), **before** replacing
\(\Omega_{b,d,u}(n,m)\) by absolute values or separated arbitrary
coefficients.  Equivalently, after completion in \(d\bmod M\), it is a
joint estimate over \(b,u,v,h_1,h_2\) of (2.4) weighted by the exact
finite transform induced by (2.8), with all gcd strata and the
Ramanujan cross/square pieces restored.

The earliest illegitimate step in a source-based proof would be one of
the following:

1. asserting \(|\mathfrak T_M|\ll M^{3/2+\varepsilon}\) uniformly;
   (3.5) refutes it on prime powers and (1.1) refutes it even on
   squarefree moduli;
2. invoking a prime-field or squarefree theorem for arbitrary
   \(M=b,2b,4b\), or invoking the rational-phase lemma when a prime cube
   divides \(M\);
3. declaring the paired \(v=0,h_1=h_2\) modes negligible without
   evaluating their actual stationary coefficient;
4. deleting the Fejer prefactor, diagonal, \(U-u\) weights, or the
   \(u=M\) shifts when \(U>M\);
5. opening the centered product but dropping either Ramanujan cross
   term or the Ramanujan square;
6. applying a single-kernel bilinear theorem after treating the other
   kernels and (2.8) as independent coefficients;
7. using generic stationary nonresonance without isolating the exact
   square/fourth-power loci.

No theorem-hypothesis check presently bridges this first step.  In
particular, (3.5) says the needed result must be an aggregate theorem
with an explicit exceptional-mode ledger; it cannot be a
coefficientwise trace estimate in disguise.

## 5. Required control test and outcome

| Required control | Outcome |
|---|---|
| `external_normalization` | **Pass.**  The new deletion uses (3.0d), so the external \(M^{-2}\) is spent exactly once before the third-derivative estimate.  It is also retained in (2.1), (2.6), and as \(M^{-4}\) in (3.3).  Source Fourier normalizations and normalized trace functions are converted explicitly. |
| `all_class_local_units` | **Pass algebraically; open analytically.**  Identity (2.4) retains the four unit conditions and is valid for all three \((g,M,K)\) classes without assuming \(K\) or \(M\) prime.  The audited prime/squarefree/odd-prime theorems do not uniformly cover the \(2\)-part, higher powers, or bad fixed-\(K\) primes. |
| `physical_row_energy_factor` | **Preserved.**  The direct estimate (3.0e) deletes its slice without spending or replacing the row bound, leaving \(Q^{-5/12}\) on (1.0a).  Under multiplier triangle it is exactly \(Q^{-5/12}\) in (3.1), but the remaining endpoint deficit is \(B^{5/9}\); none of the mapped arithmetic theorems carries it. |
| `middle_difference_ownership` | **Pass with a new exact split.**  The disjoint band \(D_0<|d|\le D_1\) is target-safe by (3.0e); the only survivor is \(D_1<|d|<\Delta_b-E_*\).  No small-shift or support-edge contribution is reintroduced. |
| `negative_and_modulus_multiple_differences` | **Pass.**  Reindexing proves the same third-derivative bound for negative \(d\), and (3.0d) is uniform when \(M\mid d\).  Both kinds also remain in the residual source audit. |
| `ramanujan_cross_and_square_terms` | **Pass.**  The direct deletion estimates the centered \(A_d\) as a whole via (3.0d), so its Ramanujan term is included exactly once.  On the residual A-process, expanding (3.3) still yields the four-Kloosterman main, two cross terms, and the square term exactly once. |
| `prime_power_gcd_modes` | **Uniform square root fails, even squarefree.**  Equation (3.5) gives \(M^{2-1/\nu}\) at \(u=M/p\); \(u\equiv0\pmod M\) gives \(M\varphi(M)\).  Equation (1.1) gives \(\asymp M^2\) for squarefree \(M=\ell q\) at \(u=M/\ell\).  Any positive estimate must stratify and aggregate these gcd-aligned modes. |
| `fejer_prefactor_and_diagonal` | **Pass on the residual.**  The diagonal and \(B(D+U)/U^2\)-type Fejer/Cauchy prefactor are compulsory.  The diagonal is target-safe, but \(U\le M\) gives at most \(B^{-1/2}\) and can already contain the divisor-aligned shifts \(u=M/\ell\); \(U>M\) crosses exact periods. |
| `four_kloosterman_offdiagonal` | **Open only on (1.0a).**  Equation (3.3) is the first unsupported term for \(D_1<|d|<\Delta_b-E_*\).  No cited theorem specializes to the full signed correlation at the required scale. |
| `actual_stationary_symbol` | **Certified for the new slice; open in fourfold form on the residual.**  Sampled product BV and the exact square-root phase give (3.0b)--(3.0e).  The residual fourfold symbol is (2.8), with phase (2.9), moving supports, and endpoints; arbitrary separated coefficients are not a replacement. |
| `entry_exit_and_error_ownership` | **Pass by scope.**  Extension by zero makes the principal product BV at its support endpoints.  Already routed entry/exit, stationary-error, wrong-sign, and exterior terms are not reclaimed.  Raw Farey-transition errors and axes remain separately owned. |
| `integer_and_perfect_power_resonance` | **Pass for the deletion; blanket nonresonance remains false.**  The third-derivative test is uniform even when the phase is integral at isolated points.  Exact square and fourth-power resonances occur for both signs outside/inside the broader survivor, and the permitted Round-85 calculation bounds their literal lattice below target. |
| `complete_transform_and_uM_self_return` | **Fails as a saving.**  Formula (2.4) is exact; (2.5) gives the \(u=M\) self-return, the prime-power near-return (3.5), and the squarefree CRT near-return (1.1), both already at \(u<M\).  Completion merely moves the obstruction to a rational phase. |
| `source_hypothesis_map` | **Pass as a negative audit.**  Prime-field trace results, squarefree fourfold transforms, exponent-at-most-two rational sums, fixed-odd-prime depth results, arbitrary-\(q\) two-kernel transforms, and single-kernel bilinear bounds were checked literally.  None proves (2.7) with (2.8). |
| `downstream_scope` | **Pass.**  No claim is made for \(C>J^{3/4}\), raw transitions, axes, cone edges, other radial sectors, full `M9-M1`, `M9-M2`, `M9`, endpoint uniformity, `R5-Full`, or the Gauss-circle exponent. |

No numerical experiment was used.  The hostile controls are exact
finite orthogonality, an exact Ramanujan-sum evaluation, scale algebra,
and literal primary-theorem hypothesis checks.

## 6. Dependencies and exact artifacts used

The report used only the assigned selected context and current primary
sources.  The repository artifacts were:

- `protocol.md`;
- `state/proof_obligations.yml`, in particular the current
  `M9-M1-centred-dual-difference-small-shift-bound`,
  `M9-M1-centred-dual-difference-support-edge-bound`,
  `M9-M1-residual-upper-conductor-offdiagonal-reduction`, and `M9-M1`
  entries and the Round-85 rejection ledger;
- `state/active_campaign.yml` at Round 86;
- `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/synthesis.md`;
- `rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/reports/large_difference_source_hostile_audit.md`;
- `rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/reports/kloosterman_energy_source_hostile_audit.md`;
- `rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/reports/offset_trace_source_hostile_audit.md`;
- the assigned brief
  `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/briefs/four_kloosterman_hostile_source_audit.md`, graph SHA-256
  `910950f389c49a17cc188c8e0ad9b18e4d83d4a7f580fa0baacca97d39195fe6`.

The primary literature links and theorem numbers are recorded in the
source map in Section 3.  All sibling Round-86 reports were excluded and
were not read.

## 7. Recommended state effect

**Promote the scoped lower-interior deletion (1.0), and retain the
remaining interior obligation open.**  The new graph-level statement
may set

\[
 D_1=\lfloor J^{87/140}\rfloor
\]

and replace the exact survivor \(D_0<|d|<\Delta_b-E_*\) by
\(D_1<|d|<\Delta_b-E_*\).  Its proof is the all-class periodic
\(L^1\) normalization plus the uniform weighted third-derivative bound
(3.0b)--(3.0f); it includes both signs, modulus multiples, prime-power
modes, the centered Ramanujan term, support endpoints, and reflected
orientations.  It neither uses nor degrades the physical
\(Q^{-5/12}\) row estimate on the survivor.

Do not promote a bound for \(\mathfrak Y_{>D_1}\), a new conductor
range, or any downstream claim from the continuously twisted identity
or from existing four-trace/p-adic literature.

Record (2.4)--(2.5), the exact prime-power value (3.5), and the
squarefree/composite CRT value (1.1) as a hostile no-go against uniform
complete-mode square-root estimates.  In particular, record that
\(U\le M\) avoids only the exact period, not p-adic or divisor-aligned
near-return modes, while \(U>M\) necessarily contains the exact
\(u=M\) self-return.

The smallest admissible next input is a proof of (2.7), restricted to
the new residual range, or a strictly stronger outside-absolute signed
version, with the actual stationary symbol (2.8), all three local
classes, the full prime-power/gcd exceptional ledger, both Ramanujan
cross terms and the square term, and the inherited \(Q^{-5/12}\)
factor.  A valid alternative is to isolate the self-return and
near-return strata exactly and prove them target-safe, then prove a
quantitatively sufficient generic remainder bound.  Existing
rational-trace and p-adic theorems do not perform this aggregate
decomposition.
