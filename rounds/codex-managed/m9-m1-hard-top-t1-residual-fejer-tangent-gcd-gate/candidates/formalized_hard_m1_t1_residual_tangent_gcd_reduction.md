# Formalized Round 185 hard-M1 \(t=1\) residual tangent-gcd reduction

- Campaign: m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate
- Task: conductor_formalization
- Role: conductor-owned formal proof-kernel candidate
- Generated: 2026-08-28T01:29:56.2384012+08:00
- Starting graph SHA-256:
  f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0
- Evidence status: candidate evidence only; pending independent
  post-repair seam reviews, durable-kernel review, and State Patch
  validation
- Numerical theorem evidence: none; one bounded exact-integer
  falsification control is archived separately

## 1. Exact residual and endpoint-exact parity connector

Fix real \(X\geq2\), one literal middle or lower hard-M1 residual shell
\(L\geq2\), and \(\sigma\in\{+1,-1\}\).  For every squarefree positive
integer \(N\), the Round-184 selector depends only on \(N\) and its
fixed external parameters, never on an allocation \(N=dm\).  Its exact
residual mask is

\[
 \rho_N(d)=
 \begin{cases}
  1,&\text{no pair is selected},\\
  1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
    +2\mathbf1_{p_Nq_N\mid d},&\text{a pair is selected}.
 \end{cases}
\tag{185.C1}
\]

Thus the selected-pair truth table is \(1,0,0,1\).  Define

\[
 \lambda_{N,\sigma}(d)=
 \begin{cases}
  \mu^2(N)\rho_N(d)
  a_{L,X}^{\mathrm{lit},\sigma}(N/d,d),
   &N,d\in\mathbb Z_{>0},\ \mu^2(N)=1,\ d\mid N,\ 2\nmid d,\\
  0,&\text{otherwise},
 \end{cases}
\]

\[
 c_{N,\sigma}^{\rm rem}
 =\sum_d\chi_4(d)\lambda_{N,\sigma}(d),
 \qquad c_{N,\sigma}^{\rm rem}=0\quad(N\leq0).
\tag{185.C2}
\]

The literal symbol is extended by zero off every original shell,
height, strict \(4m<d<16m\) cone, profile, floor, star, half-weight,
hard-sample, crossing, endpoint, sign, squarefree, and coprimality
predicate.  Consequently (185.C2) is exactly the Round-184 no-pair plus
selected-neither/both residual.  On a nonzero atom \(N=dm\),

\[
 d,m\asymp L,\qquad d\text{ odd},\qquad (d,m)=1,\qquad
 dm\asymp L^2,\qquad
 |\lambda_{N,\sigma}(d)|\ll_\varepsilon X^\varepsilon.
\tag{185.C3}
\]

Put

\[
 z_N=c_{N,\sigma}^{\rm rem}e(\sigma\sqrt{XN}),\qquad
 D_{L,\sigma}=\sum_N|z_N|^2
 \ll_\varepsilon L^2X^\varepsilon,
\tag{185.C4}
\]

and extend \(z_N\) by zero on the full integer line.  For \(R\geq1\),
define

\[
 \mathfrak E_R=\frac1R\sum_{s\in\mathbb Z}
 \left|\sum_{j=0}^{R-1}z_{s+j}\right|^2,
\tag{185.C5}
\]

\[
 \mathfrak C_R^{(2)}
 =\sum_{1\leq q\leq\lfloor(R-1)/2\rfloor}
 \left(1-\frac{2q}{R}\right)
 \sum_Nz_{N+2q}\overline{z_N}.
\]

Splitting every window into its even and odd offsets and using
\(|A+B|^2\leq2|A|^2+2|B|^2\) gives the endpoint-exact inequality

\[
 \boxed{\mathfrak E_R\leq2D_{L,\sigma}
       +4\Re\mathfrak C_R^{(2)}.}
\tag{185.C6}
\]

For odd \(R\), the terminal even gap \(2q=R-1\) is present with Fejer
weight \(1/R\), hence coefficient \(4/R\) in (185.C6).  For even
\(R\), the terminal even gap \(R-2\) has weight \(2/R\), hence
coefficient \(8/R\).  There is no endpoint error.

If the support lies in an interval of \(M_L\asymp L^2\) integer sites,
then exact window summation and Cauchy give

\[
 \left|\sum_Nz_N\right|^2
 \leq\frac{M_L+R-1}{R}\,\mathfrak E_R.
\tag{185.C7}
\]

At \(R_0=\lceil L\rceil\), the diagonal and prefactor are target-safe.
It is therefore sufficient to bound the remaining one-outer-real-part
even-shift correlation by \(O_\varepsilon(L^2X^\varepsilon)\).  This
parity step is only a constant-cost connector.

## 2. Multiplicity-one tangent opening and monotone sector

Opening both residual coefficients at an even shift \(r=2q<R_0\)
gives every ordered tuple exactly once:

\[
 N=dm,\qquad N+r=d'm',\qquad d,d'\text{ odd}.
\tag{185.C8}
\]

Put \(a=d'-d=2\alpha\) and \(b=m'-m=2\beta\).  Then

\[
 r=db+am+ab=db+am'=am+bd',
\tag{185.C9}
\]

\[
 \frac r2=\alpha m+\beta d+2\alpha\beta
 =\alpha m'+\beta d=\alpha m+\beta d',
 \qquad
 \chi_4(d')\chi_4(d)=(-1)^\alpha.
\tag{185.C10}
\]

If \(a,b\geq0\), then \(r\gg L(a+b)\).  Since \(0<r<R_0\ll L\),
only \(O(1)\) displacement pairs occur, and the complete monotone
sector has

\[
 O(L^2)
\tag{185.C11}
\]

opened incidences.  The cases \(a,b\leq0\) and the one-zero cases with
a negative nonzero coordinate are empty for \(r>0\).  Hence the exact
complement of the monotone sector is the disjoint union

\[
 a>0>b\qquad\dot\cup\qquad a<0<b.
\tag{185.C12}
\]

All counts occur after the literal divisor opening.  No product-row
density or uniqueness assertion is used.

## 3. Original gcd, inward cross gcd, and joint quotient

For the original character-leg gcd \(g=(d,d')\), write

\[
 d=gu,\qquad d'=gv,\qquad (u,v)=1,\qquad
 vm'-um=\frac rg.
\tag{185.C13}
\]

At fixed \(g\), the number of incidences is \(O(L^3/g^2)\).
Consequently

\[
 \#\{g\geq G\}\ll\frac{L^3}{G}.
\tag{185.C14}
\]

On the plus cross orientation \(a=2s>0\), \(b=-2w<0\), put

\[
 \kappa=(d,m'),\qquad
 d=\kappa u,\quad d'=\kappa u+2s,\quad
 m'=\kappa v,\quad m=\kappa v+2w.
\tag{185.C15}
\]

Then \(\kappa,u\) are odd, \((u,v)=1\), and

\[
 r=2\kappa n,\qquad n=sv-wu>0.
\tag{185.C16}
\]

On the minus cross orientation \(a=-2s<0\), \(b=2w>0\), put

\[
 \kappa=(d',m),\qquad
 d'=\kappa u,\quad d=\kappa u+2s,\quad
 m=\kappa v,\quad m'=\kappa v+2w,
\tag{185.C17}
\]

so that

\[
 r=2\kappa n,\qquad n=uw-sv>0.
\tag{185.C18}
\]

Both parametrizations are multiplicity one.  The fixed-\(\kappa\)
count is \(O(L^3/\kappa^2)\), hence across both orientations

\[
 \#\{\kappa\geq K\}\ll\frac{L^3}{K}.
\tag{185.C19}
\]

There is a stronger joint normal form.  In the plus orientation,
squarefreeness and coprimality of the upper endpoint give
\((\kappa,s)=1\); in the minus orientation the lower endpoint gives
the same fact.  Therefore in both cases

\[
 g=(d,d')=(u,s)=(u,n).
\tag{185.C20}
\]

Write

\[
 u=gU,\qquad s=gS,\qquad n=gh.
\tag{185.C21}
\]

Then \(h\geq1\), and every live incidence satisfies

\[
 r=2\kappa gh,
\tag{185.C22}
\]

with the plus and minus primitive equations

\[
 Sv-wU=h,\qquad Uw-vS=h,
\tag{185.C23}
\]

respectively.  The invariant primitive outer labels satisfy

\[
 \kappa,g,h,U,v\in\mathbb Z_{>0},\quad
 \kappa,g,U\text{ odd},\quad
 (gU,v)=1,\quad (U,h)=1,\quad
 0<2\kappa gh<R_0.
\tag{185.C24}
\]

All remaining squarefree, coprimality, selector, profile, and endpoint
conditions are retained by the two zero-extended \(\lambda\)'s.
Along either primitive affine row the bare character is

\[
 \chi_4(d')\chi_4(d)=(-1)^s=(-1)^S.
\tag{185.C25}
\]

## 4. Target-safe bounded-\(h\) sector

For fixed \((\kappa,g,h)\), support permits

\[
 O\!\left(\frac{L}{\kappa g}\right)
 \quad\text{choices of }U,\qquad
 O\!\left(\frac{L}{\kappa}\right)
 \quad\text{choices of }v,
\tag{185.C26}
\]

and a primitive affine row has \(O(\kappa)\) geometric sites.
Therefore the incidence count is

\[
 O\!\left(\frac{L^2}{\kappa g}\right)
\tag{185.C27}
\]

for each \((\kappa,g,h)\), per orientation.  Since
\(r=2\kappa gh<R_0\) implies \(2\kappa gh<L\), for every \(H\geq1\)

\[
 \begin{aligned}
 \#\{ab<0:\ h\leq H\}
 &\ll L^2\sum_{h\leq H}
       \sum_{\kappa g<L/(2h)}\frac1{\kappa g}\\
 &\ll HL^2\log^2(2L).
 \end{aligned}
\tag{185.C28}
\]

Fix \(B>0\) and put

\[
 H_B=\left\lfloor(\log(2X))^B\right\rfloor.
\tag{185.C29}
\]

After rebudgeting the two endpoint coefficient bounds and fixed
logarithmic powers into \(X^\varepsilon\), the total absolute
contribution of the complete monotone sector and both opposing sectors
with \(h\leq H_B\) is

\[
 \boxed{
 \sum_{\substack{\text{opened even-shift incidences}\\
                  a,b\geq0\ \text{or}\ ab<0,\ h\leq H_B}}
 |\text{literal correlation summand}|
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{185.C30}
\]

This is a physical opened-incidence sector.  Every selector, deletion,
profile, sign, endpoint, conjugation, Fejer weight, and zero-extension
field only restricts or boundedly weights the count.  No cancellation
is used in (185.C30).

Equations (185.C14) and (185.C19) retain the explicit corollaries

\[
 g\geq\gamma L:\quad
 O_\varepsilon(\gamma^{-1}L^2X^\varepsilon),\qquad
 \kappa\geq\delta L:\quad
 O_\varepsilon(\delta^{-1}L^2X^\varepsilon).
\tag{185.C31}
\]

For \(H_B\geq(2\gamma)^{-1}\) and
\(H_B\geq(2\delta)^{-1}\), both fixed-proportion tails are already
contained in (185.C30), by (185.C22).

## 5. Canonical affine rows, exact complement, and first open relation

Let \([x]_U\) denote the least residue in
\(\{0,\ldots,U-1\}\).  For \(U>1\), let \(\bar v\) be the inverse of
\(v\bmod U\).  For \(U=1\), adopt the convention
\([x]_1=0\), without invoking an inverse.  For every outer label in
(185.C24), choose exactly one base representative per orientation:

\[
 \begin{array}{lll}
 \text{plus:}&
 S_{0,+}=[\bar v h]_U,&
 w_{0,+}=(S_{0,+}v-h)/U,\\[1mm]
 \text{minus:}&
 S_{0,-}=[-\bar v h]_U,&
 w_{0,-}=(h+vS_{0,-})/U.
 \end{array}
\tag{185.C32}
\]

For \(U=1\), these formulas mean
\((S_{0,+},w_{0,+})=(0,-h)\) and
\((S_{0,-},w_{0,-})=(0,h)\).  For
\(\omega\in\{+,-\}\), define

\[
 S_{t,\omega}=S_{0,\omega}+Ut,\qquad
 s_{t,\omega}=gS_{t,\omega},\qquad
 w_{t,\omega}=w_{0,\omega}+vt,
\]

\[
 I_{\mathfrak f,\omega}
 =\{t\in\mathbb Z:S_{t,\omega}>0,\ w_{t,\omega}>0\},
 \qquad
 \mathfrak f=(\kappa,g,h,U,v).
\tag{185.C33}
\]

The row amplitude is defined only for \(t\in I_{\mathfrak f,\omega}\);
this orientation restriction precedes every square-root evaluation.
For the plus orientation set

\[
 \begin{aligned}
 N_{\mathfrak f,t}^{+}
 &=\kappa gU(\kappa v+2w_{t,+}),\\
 N_{\mathfrak f,t}^{+}+r
 &=(\kappa gU+2s_{t,+})\kappa v,
 \end{aligned}
\]

\[
 \begin{aligned}
 B_{\mathfrak f,+}^{\sigma}(t)
 :={}&\left(1-\frac r{R_0}\right)
 \lambda_{N_{\mathfrak f,t}^{+}+r,\sigma}
        (\kappa gU+2s_{t,+})
 \overline{\lambda_{N_{\mathfrak f,t}^{+},\sigma}(\kappa gU)}\\
 &\times
 e\!\left(\frac{\sigma\sqrt X\,r}
 {\sqrt{N_{\mathfrak f,t}^{+}+r}
  +\sqrt{N_{\mathfrak f,t}^{+}}}\right),
 \qquad r=2\kappa gh.
 \end{aligned}
\tag{185.C34}
\]

For the minus orientation set

\[
 \begin{aligned}
 N_{\mathfrak f,t}^{-}
 &=(\kappa gU+2s_{t,-})\kappa v,\\
 N_{\mathfrak f,t}^{-}+r
 &=\kappa gU(\kappa v+2w_{t,-}),
 \end{aligned}
\]

\[
 \begin{aligned}
 B_{\mathfrak f,-}^{\sigma}(t)
 :={}&\left(1-\frac r{R_0}\right)
 \lambda_{N_{\mathfrak f,t}^{-}+r,\sigma}(\kappa gU)
 \overline{
 \lambda_{N_{\mathfrak f,t}^{-},\sigma}
        (\kappa gU+2s_{t,-})}\\
 &\times
 e\!\left(\frac{\sigma\sqrt X\,r}
 {\sqrt{N_{\mathfrak f,t}^{-}+r}
  +\sqrt{N_{\mathfrak f,t}^{-}}}\right),
 \qquad r=2\kappa gh.
 \end{aligned}
\tag{185.C35}
\]

The two \(\lambda\)'s implement every unshown literal predicate by zero
extension.  Because \(U\) is odd,

\[
 (-1)^{S_{t,\omega}}=(-1)^{S_{0,\omega}+t}.
\]

After removal of the target-safe sector (185.C30), the exact remaining
even-shift correlation is

\[
 \boxed{
 \Re\!\sum_{\omega\in\{+,-\}}
 \sum_{\substack{\mathfrak f\text{ satisfying }(185.C24)\\h>H_B}}
 (-1)^{S_{0,\omega}}
 \sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t).}
\tag{185.C36}
\]

There is one real part outside both orientations, all shifts, gcds,
selector states, rows, and endpoints.  Canonical representatives and
the oriented \(t\)-sets make (185.C36) multiplicity one.

A uniform bound

\[
 \Re\!\sum_{\omega\in\{+,-\}}
 \sum_{\substack{\mathfrak f\text{ satisfying }(185.C24)\\
                  Y<h\leq2Y}}
 (-1)^{S_{0,\omega}}
 \sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t)
 \ll_\varepsilon L^2X^\varepsilon
\tag{185.C37}
\]

for every dyadic \(Y>H_B\), with both orientations still coupled,
would close (185.C36) after epsilon rebudgeting.  Its positive capacity
is \(O(YL^2X^\varepsilon)\), so (185.C37) requires a genuinely global
factor \(Y\) across the primitive row labels.

The bare character law does not provide that factor.  Even an
unjustified \(O(1)\) estimate on every complete primitive row leaves

\[
 O\!\left(
 L^3\sum_{\kappa,g\geq1}\frac1{\kappa^3g^2}
 \right)=O(L^3)
\tag{185.C38}
\]

positive row capacity.  Thus rowwise Abel summation followed by positive
recombination is insufficient without a new global signed theorem.

## 6. Exact mechanism controls

For a selected product \(N=PK\), where
\(P=p_Nq_N\geq15\), the two surviving neither/both allocations in the
formal residual pairing have divisor-to-cofactor ratios differing by
\(P^2\geq225\).  They cannot both lie in \(4m<d<16m\), whose ratio
width is four.  The residual truth table is therefore not a
same-product self-return inside the hard cone.

The conductor reproduced a stronger exact no-pair arithmetic-deletion
control in the plus orientation.  The following \(s_\star,w_\star\)
name one local fibre site, not the canonical base representative:

\[
 \kappa=103,\qquad u=7,\qquad v=1,\qquad
 s_\star=99,\qquad w_\star=14.
\]

At the local site \((s,w)=(99,14)\),

\[
 (d,d',m',m)=(721,919,103,131),\qquad r=206.
\]

Both endpoint products are squarefree and allocation-coprime, both hard
ratios lie in \((4,16)\), and every odd prime divisor is
\(3\bmod4\).  Hence neither endpoint has an eligible
opposite-character pair and both residual masks equal one for every
canonical selector.  At its adjacent tangent site
\((s,w)=(106,15)\),

\[
 (d,d',m',m)=(721,933,103,133),\qquad r=206.
\]

Both ratios remain in \((4,16)\), but \((721,133)=7\), so the lower
product contains \(7^2\) and is deleted; the upper product remains
squarefree and coprime.  The character product changes from \(-1\) to
\(+1\), as the affine law predicts.  This is an exact arithmetic
mechanism control.  It does not assert nonvanishing of any opaque
literal profile or endpoint amplitude, prove a lower mass, or disprove
(185.C37).

In the canonical plus coordinates of (185.C32), \(g=h=1\),
\(U=7\), \(S_{0,+}=1\), and \(w_{0,+}=0\).  The two displayed local
sites are therefore the canonical indices \(t=14\) and \(t=15\).

For arbitrary bounded row weights,

\[
 \sup_{|B(t)|\leq1}
 \left|\sum_{t\in I}(-1)^tB(t)\right|=|I|,
\tag{185.C39}
\]

and a constant sequence on \(M\asymp L^2\) product sites has
even-shift Fejer capacity \(\asymp L^3\).  These are
coefficient-uniform mechanism controls only.  They are not lower bounds
or models for the fixed literal M1 coefficient.

## 7. Scope, dependencies, and terminal label

The candidate proves only the endpoint-exact finite reduction and the
strict physical opened-incidence sector (185.C30), with exact complement
(185.C36).  It does not prove the complete \(t=1\) residual or scalar
estimate.

The single selected campaign terminal label is

strict_hard_m1_t1_residual_tangent_gcd_sector.

Direct accepted proof dependencies are:

- M9-M1-hard-top-t1-comparable-factor-exchange-sector;
- M9-M1-top-endpoint-transform;
- M9-M1-frequency-phase-diagram-R10;
- M9-M2-dyadic-weight-nondegeneracy; and
- Divisor-bound-elementary.

The previously proved
M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector is routing
context for the remaining hard-M1 owner, not a proof dependency of the
bounded-\(h\) count.

Round evidence reconciled is:

- reports/literal_residual_fejer_tangent_gcd_attack.md;
- reports/tangent_gcd_transfer_capacity_audit.md;
- reports/blind_residual_fejer_tangent_rederivation.md;
- reviews/conductor_round185_report_reconciliation.md; and
- controls/conductor_round185_exact_fibre_deletion_control.md.

The M2 tangent, alias, and conductor kernels are method controls only,
not M1 theorem dependencies.  No external theorem is used.

Keep open every \(t\geq2\) small-\(G\) incidence, the large-\(G\)
near-resonant complement, the complete small-\(t\) owner, both M1
parents, GAR, every M2 parent, endpoint uniformity, M9, both bridges,
the Gauss-circle target, and every exponent claim.
