# Round 185 hostile M2-to-M1 tangent-gcd transfer and capacity audit

- Campaign: m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate
- Task: tangent_gcd_transfer_capacity_audit
- Role: barrier/no-go
- Starting graph SHA-256: f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0
- Evidence status: candidate evidence only; no proof-state edit
- Allocation: 100% analytical/algebraic, 0% numerical

## 1. Result: strict M1 counting sectors, then literal self-return

The accepted M2 theorem does not transfer as an M1 theorem. Its
coefficient, cone, sign field, and endpoints may not be substituted for
the M1 ones. After independently opening the exact M1 residual, however,
the coefficient-blind finite identities and counts do rederive
literally. They give this narrow result.

Put \(R_0=\lceil L\rceil\), and fix \(0<\gamma,\delta<1/2\). In the
even-shift Fejer correlation, split opened incidences in this order:

1. \(1\le r\le R_{\log}\), where

   \[
   R_{\log}
   =\min\{R_0-1,\lfloor(\log(2X))^{100}\rfloor\};
   \]

2. the remaining monotone tangent incidences;
3. opposing incidences with original character-leg gcd
   \(g_o=(d,d')\ge\gamma L\);
4. the remaining opposing incidences with inward cross gcd
   \(\kappa_*\ge\delta L\); and
5. the exact core

   \[
   \mathscr R_{\gamma,\delta}:\quad
   R_{\log}<r<R_0,\quad 2\mid r,\quad
   (d'-d)(m'-m)<0,\quad
   (d,d')<\gamma L,\quad \kappa_*<\delta L.
   \tag{185.A1}
   \]

The first four pieces are genuine target-safe M1 pieces. Before
absorption of divisor and logarithmic factors, their bounds are

\[
 L^2(\log(2X))^{100}X^\varepsilon,\qquad
 L^2X^\varepsilon,\qquad
 \gamma^{-1}L^2X^\varepsilon,\qquad
 \delta^{-1}L^2X^\varepsilon.
\tag{185.A2}
\]

Thus the high-original-gcd and high-inward-cross-gcd counts transfer
literally after M1-specific rederivation, with the real losses
\(\gamma^{-1}\) and \(\delta^{-1}\). They are opened-incidence sectors,
not unique product-row sectors. If
\(R_0-1\le(\log(2X))^{100}\), the first item contains every shift and
proves the residual correlation on that polylogarithmic shell range.
For general \(L\), (185.A1) remains.

Both cross-gcd orientations have exact multiplicity-one primitive
fibres, and their bare character is a fixed anchor times \((-1)^t\).
That does not contract a retained M1 fibre. The multiplier contains two
independently evaluated residual selectors, both squarefree and
coprimality deletions, sign-dependent profiles and hard values, endpoint
conjugation, and full zero extension. No fibre-variation theorem for
that multiplier is assumed.

The later primitive-alias and primitive-conductor algebra is likewise
coefficient-blind and rederives for M1. It proves a target-safe
polylogarithmic-conductor Fourier packet and a target-safe symmetric
trace. The complete centered high-conductor defect, however, is exactly
the original M1 orientation block minus the already-safe
low-conductor packet. Conductor centering is algebraic self-return.

Therefore bare alternation, rowwise Abel, shiftwise triangle, a positive
Gram norm, positive Poisson/B-process recombination, alias \(TT^*\), and
positive residue-bucket closure do not prove the frozen target. The
narrow terminal conclusion is

\[
\boxed{\texttt{hard\_m1\_t1\_residual\_tangent\_gcd\_capacity\_or\_self\_return\_no\_go}.}
\tag{185.A3}
\]

This no-go concerns only those mechanisms. It is not physical lower
mass and does not disprove a new literal, jointly signed theorem.

## 2. Exact statement and hypotheses

Fix real \(X\ge2\), one literal middle or lower hard-M1 residual shell
\(L\), and \(\sigma\in\{+1,-1\}\). Put \(J=\sqrt X\). For odd
\(d\mid N\), define

\[
\lambda_{N,\sigma}^{(1)}(d)
:=\mu^2(N)\rho_N(d)
a_{L,X}^{\mathrm{lit},\sigma}(N/d,d),
\qquad
c_{N,\sigma}^{\mathrm{rem}}
=\sum_{\substack{d\mid N\\d\ {\rm odd}}}
\chi_4(d)\lambda_{N,\sigma}^{(1)}(d).
\tag{185.A4}
\]

Here \(\rho_N=1\) when no pair is selected and, for a selected pair
\(\{p_N,q_N\}\),

\[
\rho_N(d)
=1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
+2\mathbf1_{p_Nq_N\mid d}.
\tag{185.A5}
\]

Its truth table is \(1,0,0,1\). Thus (185.A4) contains exactly all
no-pair allocations and the selected neither/both allocations. It is
extended by zero off every original shell, height, strict cone,
profile, floor, star, half-weight, hard-sample, crossing, endpoint, and
sign predicate.

On a nonzero atom, writing \(N=dm\),

\[
d,m\asymp L,\qquad d\ {\rm odd},\qquad
(d,m)=1,\qquad 4m<d<16m,\qquad
dm\asymp L^2,\qquad
|\lambda_{N,\sigma}^{(1)}(d)|\ll_\varepsilon X^\varepsilon.
\tag{185.A6}
\]

Both \(N\) and \(N+r\) are independently squarefree on a live opened
pair. A containing interval has \(M_L\asymp L^2\) integer sites, and
literal divisor counting gives

\[
D_{L,\sigma}
:=\sum_N|c_{N,\sigma}^{\mathrm{rem}}|^2
\ll_\varepsilon L^2X^\varepsilon.
\tag{185.A7}
\]

For every \(R\ge1\), let

\[
\mathfrak C_{R,\sigma}
=\sum_{1\le r<R}\left(1-\frac rR\right)
\sum_N c_{N+r,\sigma}^{\mathrm{rem}}
\overline{c_{N,\sigma}^{\mathrm{rem}}}
e\!\left(\sigma J(\sqrt{N+r}-\sqrt N)\right),
\tag{185.A8}
\]

where the inner sum is only over positive live pairs. The phase is
exactly

\[
\sigma J(\sqrt{N+r}-\sqrt N)
=\frac{\sigma\sqrt X\,r}{\sqrt{N+r}+\sqrt N}.
\tag{185.A9}
\]

There is one real part outside (185.A8). Let
\(\mathfrak C_{R,\sigma}^{(2)}\) be (185.A8) restricted to even \(r\).
The exact M1 incidence decomposition is

\[
\mathfrak C_{R_0,\sigma}^{(2)}
=\mathfrak C_{\rm small}
+\mathfrak C_{\rm mon}
+\mathfrak C_{g_o\ge\gamma L}
+\mathfrak C_{g_o<\gamma L,\,\kappa_*\ge\delta L}
+\mathfrak R_{\gamma,\delta,\sigma},
\tag{185.A10}
\]

and the first four terms satisfy (185.A2).

For fixed \(B>0\), put \(Q_B=(\log(2X))^B\). Exact primitive-anchor
Fourier decomposition further gives

\[
\mathfrak R_{\gamma,\delta,\sigma}
=\mathfrak P_{q\le Q_B,\sigma}
+\mathfrak T_{q>Q_B,\sigma}
+\mathfrak D^\circ_{q>Q_B,\sigma},
\tag{185.A11}
\]

where the first term is a Fourier packet, not a physical incidence
sector, the second is the symmetric primitive trace, and

\[
|\mathfrak P_{q\le Q_B,\sigma}|
+|\mathfrak T_{q>Q_B,\sigma}|
\ll_{B,\gamma,\delta,\varepsilon}L^2X^\varepsilon.
\tag{185.A12}
\]

The sole remaining relation at this interface is

\[
\boxed{
\Re\mathfrak D^\circ_{q>Q_B,\sigma}
\stackrel{?}{\ll}_{B,\gamma,\delta,\varepsilon}
L^2X^\varepsilon.}
\tag{185.A13}
\]

All \(\kappa,u,u_0,q,b\), both orientations, endpoint amplitudes, and
shifts remain under this one real part.

## 3. Proof or derivation

### 3.1 Fejer identity, parity connector, and terminal gaps

Put

\[
z_N=c_{N,\sigma}^{\mathrm{rem}}e(\sigma J\sqrt N)
\]

on the positive literal shell and zero elsewhere. Direct full-line
expansion gives

\[
\mathfrak E_{R,\sigma}
:=\frac1R\sum_{s\in\mathbb Z}
\left|\sum_{j=0}^{R-1}z_{s+j}\right|^2
=D_{L,\sigma}+2\Re\mathfrak C_{R,\sigma},
\tag{185.A14}
\]

because a pair at gap \(r\) occurs in exactly \(R-r\) windows. Exactly
\(M_L+R-1\) window starts can meet the containing interval, so

\[
\left|\sum_Nz_N\right|^2
\le\frac{M_L+R-1}{R}\mathfrak E_{R,\sigma}.
\tag{185.A15}
\]

The diagonal contribution has scale \(L^4/R\). It first reaches the
required \(L^3X^\varepsilon\) target-square scale at \(R\asymp L\).
Thus \(R_0=\lceil L\rceil\) is the minimal diagonal-safe scale up to
constants.

Split every window by the absolute parity of its sites. If \(R=2S\),
\(x_n=z_{2n}\), \(y_n=z_{2n+1}\), and

\[
\mathcal E_T(w)
=\frac1T\sum_k\left|\sum_{j=0}^{T-1}w_{k+j}\right|^2,
\]

then

\[
\mathfrak E_{2S,\sigma}^{(2)}
=\mathcal E_S(x)+\mathcal E_S(y).
\tag{185.A16}
\]

If \(R=2S+1\), then exactly

\[
\begin{aligned}
\mathfrak E_{2S+1,\sigma}^{(2)}
={}&\frac{S+1}{2S+1}
\{\mathcal E_{S+1}(x)+\mathcal E_{S+1}(y)\}\\
&+\frac S{2S+1}
\{\mathcal E_S(x)+\mathcal E_S(y)\}.
\end{aligned}
\tag{185.A17}
\]

The last even gap is \(R-2\), with weight \(2/R\), when \(R\) is even;
when \(R\) is odd it is \(R-1\), with exact weight \(1/R\). At \(R=1\)
both energies equal the diagonal. Pointwise
\(|A+B|^2\le2(|A|^2+|B|^2)\) gives for every \(R\)

\[
\mathfrak E_{R,\sigma}\le2\mathfrak E_{R,\sigma}^{(2)},
\qquad
\Re\mathfrak C_{R,\sigma}
\le\frac12D_{L,\sigma}+2\Re\mathfrak C_{R,\sigma}^{(2)}.
\tag{185.A18}
\]

This is a constant-cost connector, not cancellation. It works
separately for both signs and has no endpoint error.

The same all-\(R\) algebra rederives the M2 maximal-scale alternative
for M1: fixed-shift Cauchy can pay an initial range, and an unproved
even long-shift aggregate at \(R=M_L\) would suffice. That is a
different open target and is not pursued here.

### 3.2 The small/polylogarithmic shift packet is paid literally

For every fixed \(r\), literal Cauchy and (185.A7) give

\[
\sum_N|c_{N+r,\sigma}^{\mathrm{rem}}
c_{N,\sigma}^{\mathrm{rem}}|
\le D_{L,\sigma}
\ll_\varepsilon L^2X^\varepsilon.
\tag{185.A19}
\]

Equivalently, opening both divisor sums gives \(O(L^2)\) choices of
\(N\) and at most
\(\tau(N)\tau(N+r)X^\varepsilon\) weighted allocations. Summing
(185.A19) only for \(r\le R_{\log}\) costs a fixed logarithmic power,
absorbed after epsilon rebudgeting:

\[
|\mathfrak C_{\rm small}|
\ll_\varepsilon L^2X^\varepsilon.
\tag{185.A20}
\]

Thus no M2 small-shift theorem is imported and no omitted M1 packet is
silently deleted. Shiftwise triangle is not claimed affordable on the
remaining \(\asymp L\) shifts.

### 3.3 Multiplicity-one tangent opening and both parity branches

Open the two coefficients:

\[
N=dm,\qquad N+r=d'm',\qquad d,d'\ {\rm odd}.
\tag{185.A21}
\]

The ordered tuple \((d,m,d',m')\) occurs once. Put
\(a=d'-d\), \(b=m'-m\). Then

\[
r=db+am+ab=db+am',\qquad
a\equiv0\pmod2,\qquad b\equiv r\pmod2,
\tag{185.A22}
\]

and

\[
\chi_4(d')\chi_4(d)=(-1)^{a/2}.
\tag{185.A23}
\]

These are M1 identities with \(d=v\) the odd character leg and \(m=u\)
the cofactor; no M2 coefficient is substituted.

If \(a,b\ge0\), literal support gives
\(r=db+am'\gg L(a+b)\). Across \(r<R_0\), only \(O(1)\) pairs
\((a,b)\) occur and there are \(O(L^2)\) choices of \((d,m)\). Hence

\[
|\mathfrak C_{\rm mon}|
\ll_\varepsilon L^2X^\varepsilon.
\tag{185.A24}
\]

The sector \(a,b\le0\), apart from \((0,0)\), and either one-zero
negative sector are impossible for \(r>0\). Every unpriced tuple has
\(ab<0\), in exactly one of two orientations.

The M2 cofactor-gcd row also rederives. Let
\(s_c=(m,m')\), \(m=s_cu_c\), \(m'=s_cv_c\), and
\((u_c,v_c)=1\). Then \(r=s_ch\), \(v_cd'-u_cd=h\), and, after
selecting the odd solution class,

\[
d=D_0+2v_ck,\qquad d'=D_0'+2u_ck.
\tag{185.A25}
\]

The product step is \(2s_cu_cv_c=2mm'/s_c\), the row has
\(O(1+s_c)\) sites, and

\[
\chi_4(d(k))\chi_4(d'(k))
=\varepsilon_0(-1)^{(r\bmod2)k}.
\tag{185.A26}
\]

For even \(r\), \(m,m'\) have the same parity. In the odd-odd branch,
\(s_c,u_c,v_c\) are odd. In the squarefree even-even branch,
\(\nu_2(s_c)=1\), \(u_c,v_c\) are odd, \(4\mid r\), and \(h\) is even.
Thus (185.A26) is frozen on every even-shift cofactor row. The parity
connector has removed precisely the branch where this row character
alternates.

### 3.4 Original gcd and the restored \(\gamma^{-1}\) cost

Let

\[
g_o=(d,d'),\qquad d=g_ou,\qquad d'=g_ov,\qquad (u,v)=1.
\tag{185.A27}
\]

Then \(r=g_oh\) and

\[
vm'-um=h,\qquad
m=m_0+vt,\qquad m'=m'_0+ut.
\tag{185.A28}
\]

Using a canonical particular solution makes this multiplicity one.
The products have common step

\[
K_d=g_ouv=\frac{dd'}{g_o},
\tag{185.A29}
\]

the row has \(O(1+g_o)\) sites, and

\[
\chi_4(d')\chi_4(d)=\chi_4(uv)
\tag{185.A30}
\]

is fixed. For fixed \(g_o\), there are
\(O((L/g_o)^3)\) choices of \(u,v,h\); multiplying by row length gives
\(O(L^3/g_o^2)\) atoms. Therefore

\[
\sum_{g_o\ge G_0}O\!\left(\frac{L^3}{g_o^2}\right)
\ll\frac{L^3}{G_0},
\qquad
|\mathfrak C_{g_o\ge\gamma L}|
\ll_\varepsilon\gamma^{-1}L^2X^\varepsilon.
\tag{185.A31}
\]

Every M1 selector, parity branch, squarefree condition, profile,
endpoint, and zero-extension field only deletes or downweights atoms in
this count. It supplies no cancellation on the complement.

### 3.5 Inward cross gcd: orientations, parity, multiplicity, and count

On an even opposing tuple with \(d'>d\), \(m'<m\), put

\[
\kappa=(d,m'),\quad
d=\kappa u,\quad d'=\kappa u+2s,\quad
m'=\kappa v,\quad m=\kappa v+2w.
\tag{185.A32}
\]

Then \(\kappa,u\) are odd, \((u,v)=1\), \(s,w\ge1\), and

\[
r=2\kappa n,\qquad sv-wu=n>0.
\tag{185.A33}
\]

With \(s_0=[\bar v n]_u\) (and \(s_0=0\) for \(u=1\)) and
\(w_0=(s_0v-n)/u\), every solution is uniquely

\[
s_t=s_0+ut,\qquad w_t=w_0+vt.
\tag{185.A34}
\]

Both endpoint products advance by \(2\kappa uv\), and

\[
\chi_4(d')\chi_4(d)
=E_u(\bar v n)(-1)^t,\qquad
E_u(x)=(-1)^{[x]_u}.
\tag{185.A35}
\]

The other orientation, \(d'<d\), \(m'>m\), is uniquely

\[
d'=\kappa u,\quad d=\kappa u+2s,\quad
m=\kappa v,\quad m'=\kappa v+2w,\quad
uw-sv=n>0,
\tag{185.A36}
\]

with \(s_0=[-\bar v n]_u\), the same product step, and anchor
\(E_u(-\bar v n)(-1)^t\). The inverse maps recover all fibre labels
from the opened tuple, so there is no orientation multiplicity.

Both two-adic branches survive. If the endpoint products are odd, then
\(v\) is odd. If they are even and squarefree, then
\(v\equiv2\pmod4\), \(w,n\) are even,
\(w\mapsto w+v\) preserves that parity, and
\(s\mapsto s+u\) flips parity. Thus (185.A35) remains the exact
\((-1)^t\) law in the even-even branch.

Squarefreeness proves the fibre-stable original gcd. In the plus
orientation, upper-endpoint coprimality gives \((\kappa,s)=1\), and

\[
(d,d')=(\kappa u,\kappa u+2s)
=(u,s)=(u,sv-wu)=(u,n).
\tag{185.A37}
\]

The minus orientation is identical using the lower endpoint. Thus

\[
\boxed{
g_o=(d,d')=(u,n)
=\left(u,\frac r{2\kappa_*}\right)}
\tag{185.A38}
\]

is constant along the fibre and is distinct from \(\kappa_*\).

For fixed \(\kappa\), support gives
\(u,v\asymp L/\kappa\), \(n\ll L/\kappa\), and row length

\[
O\!\left(1+\frac{L^2}{\kappa uv}\right)=O(1+\kappa).
\tag{185.A39}
\]

Hence, for both orientations,

\[
C_\kappa
\ll_\varepsilon\frac{L^3}{\kappa^2}X^\varepsilon,
\qquad
\sum_{\kappa\ge K}C_\kappa
\ll_\varepsilon\frac{L^3}{K}X^\varepsilon.
\tag{185.A40}
\]

At \(K=\delta L\), this is
\(\delta^{-1}L^2X^\varepsilon\). The low-\(g_o\) restriction is only a
deletion and creates no hidden \(\gamma\)-gain. The
\(\delta^{-1}\) loss may not be dropped when \(\delta\) varies.

For the plus orientation, the exact M1 fibre amplitude is

\[
\begin{aligned}
\Lambda_\sigma^+(t)
={}&\left(1-\frac{2\kappa n}{R_0}\right)
\mathbf1_{R_{\log}<2\kappa n<R_0}
\mathbf1_{(u,n)<\gamma L}
\mathbf1_{\kappa<\delta L}
\mathbf1_{s_t,w_t\ge1}\\
&\times
\lambda_{N_t^++2\kappa n,\sigma}^{(1)}(\kappa u+2s_t)
\overline{\lambda_{N_t^+,\sigma}^{(1)}(\kappa u)},
\end{aligned}
\tag{185.A41}
\]

where

\[
N_t^+=\kappa u(\kappa v+2w_t),\qquad
\Psi_\sigma^+(t)
=\sigma J(\sqrt{N_t^++2\kappa n}-\sqrt{N_t^+}).
\tag{185.A42}
\]

The minus amplitude has the endpoint roles and conjugation reversed
exactly as in (185.A36). All other literal predicates are enforced by
the two \(\lambda^{(1)}\)'s and zero extension. The core is therefore the
real part of the sum of

\[
E_u(\bar v n)(-1)^t\Lambda_\sigma^+(t)e(\Psi_\sigma^+(t))
\quad\text{and}\quad
E_u(-\bar v n)(-1)^t\Lambda_\sigma^-(t)e(\Psi_\sigma^-(t))
\tag{185.A43}
\]

over all outer labels, with one real part after both orientations are
assembled.

### 3.6 Primitive aliases, conductors, and exact self-return

Put

\[
g_a=(u,n),\qquad u=g_au_0,\qquad n=g_an_0,\qquad (n_0,u_0)=1.
\tag{185.A44}
\]

Here \(g_a=g_o\) by (185.A38), and \(u_0\) is odd. The anchor reduces
exactly:

\[
E_u(\pm\bar v n)=E_{u_0}(\pm\bar v n_0).
\tag{185.A45}
\]

For

\[
c_m(k)=\frac{2}{m\{1+e(-k/m)\}},
\]

Fourier uniqueness gives the alias fold

\[
\sum_{j=0}^{g_a-1}c_u(\ell+ju_0)=c_{u_0}(\ell).
\tag{185.A46}
\]

The final additive conductor is

\[
q=\frac{u_0}{(\ell,u_0)},
\tag{185.A47}
\]

not \(u\) or \(u_0\). If \(\ell=(u_0/q)a\), \((a,q)=1\), then

\[
c_{u_0}(\ell)=\frac q{u_0}c_q(a),\qquad
\sum_{\operatorname{cond}(\ell)=q}|c_{u_0}(\ell)|
\ll\frac q{u_0}\log(2q).
\tag{185.A48}
\]

At fixed \((\kappa,u,u_0)\), there are \(O(u_0)\) admissible \(n_0\),
\(O(L/\kappa)\) values of \(v\), and \(O(1+\kappa)\) fibre sites.
Thus the M1 atom capacity is \(O(u_0LX^\varepsilon)\), and exact
conductor \(q\) has positive capacity

\[
O\!\left(Lq\log(2q)X^\varepsilon\right).
\tag{185.A49}
\]

Summing (185.A49) for \(q\le Q_B\), then over divisor labels and
\((\kappa,u)\), proves the first estimate in (185.A12). This proof uses
the M1 support and actual amplitudes, not the M2 coefficient.

For \(q\mid u_0\), define

\[
K_q(b)=\sum_{a\in U(q)}c_q(a)e(ab/q),\qquad
K_q^\circ(b)=K_q(b)-\frac{\mu(q)}q.
\tag{185.A50}
\]

Inclusion-exclusion and Fourier inversion give

\[
K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b),\qquad
K_q(b)+K_q(-b)=\frac{2\mu(q)}q
\quad(b\in U(q)).
\tag{185.A51}
\]

If \(B_{q,b,\sigma}^{\pm}\) are the exact M1 buckets formed from
(185.A41)--(185.A43), the exact-conductor block is

\[
\begin{aligned}
\mathcal C_{u_0,q,\sigma}
={}&\frac q{u_0}\sum_{b\in U(q)}K_q^\circ(b)
(B_{q,b,\sigma}^+-B_{q,b,\sigma}^-)\\
&+\frac{\mu(q)}{u_0}\sum_{b\in U(q)}
(B_{q,b,\sigma}^++B_{q,b,\sigma}^-).
\end{aligned}
\tag{185.A52}
\]

The second line is the trace in (185.A11). Its absolute cost is
\(O(LX^\varepsilon)\) for each supported \((\kappa,u)\). Divisor
summation and

\[
\sum_{\kappa<\delta L}\#\{u\asymp L/\kappa\}
\ll L\log(2L)
\]

prove the second estimate in (185.A12).

For every odd \(u_0>1\), atomwise Möbius inversion gives

\[
\sum_{q\mid u_0}\frac q{u_0}K_q^\circ(b)=E_{u_0}(b).
\tag{185.A53}
\]

The \(q=1\) centered kernel is zero, and its uncentered trace is
essential. Therefore, at fixed \(u_0\),

\[
\mathfrak D_{q>Q_B,\sigma}^\circ
=\mathcal O_{u_0,\sigma}
-\mathfrak D_{q\le Q_B,\sigma}^\circ,
\tag{185.A54}
\]

where \(\mathcal O_{u_0,\sigma}\) is the original literal
two-orientation block in (185.A43). The same identity holds for
uncentered blocks with the complete safe low-\(q\) packet subtracted.
This is exact self-return, not an estimate.

The evident orientation maps do not repair (185.A54). The reflection
\((s,w)\mapsto(u-s,v-w)\) is live on at most one fibre site and changes
both endpoints and every dependent literal field. The product-preserving
map

\[
(u,v,s,w,+)\mapsto(v,u,w,s,-)
\]

replaces each M1 character divisor by its complementary factor. A live
allocation has \(4m<d<16m\), so the swapped allocation violates the
strict cone; in the even branch its new character leg can also be even.
It maps to zero extension, not to a live opposite-orientation partner.

### 3.7 Capacity and positive-transform controls

The full \(R_0\)-scale off-diagonal has \(L^3X^\varepsilon\) positive
capacity against an \(L^2X^\varepsilon\) target. Indeed, taking a modulus
at every shift and applying Cauchy gives

\[
\sum_{r<R_0}
\left|\sum_Nc_{N+r,\sigma}^{\mathrm{rem}}
\overline{c_{N,\sigma}^{\mathrm{rem}}}e(\cdots)\right|
\ll R_0D_{L,\sigma}
\ll L^3X^\varepsilon.
\tag{185.A55}
\]

Through (185.A15), this returns only the scalar
\(L^2X^\varepsilon\) capacity. The safe counts do not change the
exponent of the low-\(g_o\), low-\(\kappa_*\) core: its positive count is
still dominated by \(\kappa=1\) and is \(O(L^3X^\varepsilon)\).

On a primitive fibre, \((-1)^t\) has bounded partial sums only before
multiplication by

\[
\Lambda_\sigma^\pm(t)e(\Psi_\sigma^\pm(t)).
\]

The selectors \(\rho_{N_t}\) and \(\rho_{N_t+r}\) change independently.
The squarefree/coprimality conditions can delete different parities, and
the M1 profile, strict cone, floors, stars, hard values, endpoints, and
zero extension create further jumps. No hypothesis bounds the
zero-extended variation of this product. Rowwise Abel therefore gives
only uncontrolled total variation.

Even without deletions, the effective phase

\[
\sigma J(\sqrt{x(t)+2\kappa n}-\sqrt{x(t)})+\frac t2
\tag{185.A56}
\]

has no proved uniform first-difference separation from the integers.
Changing \(\sigma\) reflects the derivative image but changes no
absolute capacity.

If smooth full fibres are completed and every stationary dual mode is
then absoluted, the rowwise B-process expression

\[
\sqrt F+\frac T{\sqrt F}
\]

has no uniform power saving over the row. Smooth-cell two-variable
Poisson followed by positive dual recombination returns the physical
\(L^3\) scale. These are controls only: a literal discontinuous M1
completion would still owe every boundary and transition term.

At exact conductor \(q\), (185.A49) shows that one optimistic reciprocal
square-root saving leaves
\(L\sqrt q\log(2q)\), above the local \(L\)-target for power-size \(q\).
Exact weighted alias \(TT^*\) is rank one and reconstructs the original
physical block squared; alias Cauchy and Parseval return positive
residue-bucket energy. Prime and prime-square artificial bucket arrays
attain the coefficient-uniform \(Lq\) shadow, but are not the literal
M1 selector/profile field and give no lower bound.

These calculations prove only the mechanism boundary (185.A3). A new
theorem retaining the one outer real part and jointly using the actual
selector, phase, gcd, alias, conductor, endpoint, and orientation labels
is not excluded.

## 4. First doubtful or unproved step

The first invalid transfer step is the assertion that

\[
\chi_4(d')\chi_4(d)=E_u(\pm\bar v n)(-1)^t
\]

gives a bounded or power-saving sum on a retained M1 fibre. The identity
is correct; the required variation statement for (185.A41) is absent.
M2's finite identity supplies no regularity for the independently
changing M1 residual selectors, squarefree and coprimality masks,
sign-dependent profiles, strict-cone endpoints, hard samples, or zero
extension. This is the first mismatch after the finite identities and
counts, and it occurs before rowwise Abel, Poisson, or a conductor
estimate can be licensed.

After the exact low-conductor and trace payments, the first precise open
estimate is (185.A13), namely

\[
\Re\sum_{\kappa,u,u_0}
\sum_{\substack{q\mid u_0\\q>Q_B}}
\frac q{u_0}\sum_{b\in U(q)}K_q^\circ(b)
\bigl(B_{q,b,\sigma}^+-B_{q,b,\sigma}^-\bigr)
\ll_\varepsilon L^2X^\varepsilon,
\tag{185.A57}
\]

with the ranges in (185.A1), every literal field, and one real part
outside the whole sum. By (185.A54), this is the original unresolved
literal core minus target-safe packets. A modulus per row or a positive
norm is not an equivalent substitute.

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| exact no-pair/neither-both residual | **PASS.** (185.A4)--(185.A5) retain exactly no-pair plus selected \(00/11\), with independent upper and lower selectors after opening. |
| literal coefficient and zero extension | **PASS for identities and counts.** No profile, floor, star, hard value, endpoint, or missing site is dropped. **BLOCKS fibre cancellation:** no joint variation law is available. |
| every shell, real \(X\), both signs, endpoints | **PASS.** The proof is shell-local, uses only \(J=\sqrt X\), and works separately for \(\sigma=\pm1\). Sign reversal reflects phases but changes no count. |
| one outer real part | **PASS.** It remains outside all shifts, gcds, conductors, buckets, orientations, and endpoint branches in (185.A13)/(185.A57). |
| \(L^3\) energy versus \(L^2\) target | **PASS.** (185.A55) restores the missing factor \(L\); no capacity is called a lower bound. |
| diagonal and minimal Fejer scale | **PASS.** \(D_{L,\sigma}\ll L^2X^\varepsilon\), and the diagonal scalar-square cost \(L^4/R\) first becomes safe at \(R\asymp L\). |
| endpoint-exact parity connector | **PASS.** (185.A16)--(185.A18) cover even and odd \(R\), including \(R=1\), without boundary error. |
| terminal even gap | **PASS.** Its weight is \(2/R\) for even \(R\) and \(1/R\) for odd \(R\). |
| small/polylog shift packet | **PASS.** It is paid independently by the M1 literal divisor-energy count, not inherited or deleted. |
| multiplicity-one double opening | **PASS.** Each opened pair gives one tangent tuple, and both cross-gcd inverse maps are unique. |
| tangent identity and \(\chi_4\) law | **PASS.** (185.A22)--(185.A23) are exact with \(d\) the M1 odd character leg. |
| monotone tangent and opposing complement | **PASS.** The monotone union has \(O(L^2)\) atoms; every remaining positive-shift tuple lies in exactly one opposing orientation. |
| cofactor-gcd parity branches | **PASS.** Odd-odd and squarefree even-even branches are retained; the character is frozen on all even shifts. |
| original-gcd normal form and row count | **PASS.** A row has \(O(1+g_o)\) sites; fixed-\(g_o\) mass is \(O(L^3/g_o^2)\). |
| high original gcd | **PASS with cost.** \(g_o\ge\gamma L\) costs \(\gamma^{-1}L^2X^\varepsilon\). |
| inward-cross-gcd parametrization | **PASS.** Both orientations, residues, product steps, positivity conditions, and even-even parity are explicit. |
| primitive anchor and gcd compatibility | **PASS.** The anchor is \(E_u(\pm\bar vn)(-1)^t\), and \(g_o=(u,n)\) is stable and distinct from \(\kappa_*\). |
| high inward cross gcd | **PASS with cost.** \(\kappa_*\ge\delta L\) costs \(\delta^{-1}L^2X^\varepsilon\); its complement is exact. |
| \(\gamma,\delta\) restoration | **PASS.** The safe ledger is \(O((1+\gamma^{-1}+\delta^{-1})L^2X^\varepsilon)\) before fixed-parameter absorption. |
| selector/squarefree/profile deletion | **PASS as a seam diagnosis.** Deletions are harmless for counts but destroy complete-fibre alternation; none is treated as a monotone deletion inside a signed sum. |
| primitive alias/conductor algebra | **PASS after M1 rederivation.** The low-\(q\) packet and symmetric trace are target-safe transformed pieces. |
| no positive norm or shift triangle | **PASS as a no-go.** Such a placement gives \(L^3\) energy and only \(L^2\) scalar capacity. |
| no rowwise Abel or positive dual recombination | **PASS as a no-go.** Missing literal fibre BV blocks Abel; positive dual sums retain the trivial power and separate endpoints. |
| primitive-conductor self-return | **PASS as an obstruction.** The centered high-\(q\) defect equals the original block minus the safe low packet. |
| M2-to-M1 transfer scope | **PASS only after rejecting theorem transfer.** Every finite identity and count was rederived with \(d=v\), \(m=u\), and \(\lambda^{(1)}_{N,\sigma}\). No M2 estimate is used as an M1 dependency. |
| arbitrary/dechirped coefficient quarantine | **PASS.** Artificial arrays diagnose coefficient-uniform capacity only and are never asserted to be literal or lower mass. |
| orientation self-return | **PASS.** Reflection changes endpoints; complementary-factor exchange leaves the strict M1 cone. |
| \(t\ge2\) and near-resonant quarantine | **PASS.** No \(t\ge2\) small-\(G\) or large-\(G\) near-resonant incidence is treated. |
| complete small-\(t\) owner quarantine | **PASS.** Even a proof of (185.A13) would complete only the t=1 residual after adjoining the Round-184 XOR sector. |
| downstream and exponent quarantine | **PASS.** No M1/M2 parent, endpoint seam, M9 theorem, bridge, quarter theorem, or exponent changes. |
| no in-round pivot | **PASS.** The maximal-scale alternative is recorded only as an algebraic audit. |

No numerical, symbolic, or web theorem evidence was used.

## 6. Dependencies and exact artifacts used

Only the assigned brief and its permitted context were used:

1. rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/briefs/tangent_gcd_transfer_capacity_audit.md;
2. protocol.md;
3. state/proof_obligations.yml;
4. state/active_campaign.yml;
5. strategy/round185_m1_hard_top_t1_residual_fejer_tangent_gcd_strategy.md;
6. proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md;
7. rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reports/m2_transfer_transport_capacity_audit.md;
8. proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md;
9. proofs/kernels/m9_m2_hard_top_t1_residual_k17a_cross_gcd_alternating_fibre_reduction.md;
10. proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_alias_conductor_reduction.md; and
11. proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_conductor_parity_self_return.md.

The accepted inputs used are the M1 residual coefficient and its
support/pointwise bounds, the full-line Fejer identity, divisor bounds,
and the finite M2 formulas used only as statements to be independently
checked. No unlisted artifact or theorem was imported.

## 7. Recommended state effect

**Promote only after independent seam review the M1-specific finite
reduction and strict counting sectors (185.A10); retain the complete
residual target as open; record the bare-alternation/positive-transform
and primitive-conductor self-return no-go; make no downstream or exponent
change from this report alone.**

Recommended Round 185 exit label:
**hard_m1_t1_residual_tangent_gcd_capacity_or_self_return_no_go**.

Concretely:

- retain the endpoint-exact parity connector, tangent identities,
  monotone count, original-gcd count, both inward-cross-gcd
  parametrizations, and the \(\gamma^{-1},\delta^{-1}\) strict-sector
  bounds as M1 candidate evidence;
- retain the independently proved M1 small/polylog shift packet, so the
  non-polylogarithmic restriction has an exact paid complement;
- retain the low-conductor packet and symmetric trace only as exact
  transformed subaggregates, not physical incidence sectors;
- reject any claim that the M2 residual theorem, bare \((-1)^t\),
  rowwise Abel, one reciprocal square root, positive Poisson/B-process,
  alias energy, conductor centering, or orientation exchange proves the
  M1 residual;
- leave (185.A13)/(185.A57) as the first exact open relation, with one
  outer real part and every literal field; and
- leave all \(t\ge2\), near-resonant, complete small-\(t\), M1/M2
  parent, endpoint, M9, bridge, quarter-target, and exponent owners
  unchanged.
