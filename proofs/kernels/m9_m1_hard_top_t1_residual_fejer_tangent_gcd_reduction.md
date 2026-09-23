# Hard-M1 \(t=1\) residual Fejer tangent-gcd reduction

- Campaign: m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate
- Starting graph SHA-256:
  f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0
- Exact source candidate:
  rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/candidates/formalized_hard_m1_t1_residual_tangent_gcd_reduction.md
  (SHA-256
  74099d8aa2ab72f73589f3902c36912ab3358d229122312791f9aff772bfdd65)
- Evidence status: durable proof-kernel candidate; pending final kernel and
  State Patch validation
- Numerical theorem evidence: none; one bounded exact-integer mechanism
  control is recorded below

## Statement

Fix real \(X\geq2\), one literal middle or lower hard-M1 residual shell
\(L\geq2\), \(\sigma\in\{+1,-1\}\), and a fixed \(B>0\).  For every
squarefree positive integer \(N\), let the Round-184 selector depend only
on \(N\) and its fixed external parameters, never on an allocation
\(N=dm\).  Its exact residual mask is

\[
 \rho_N(d)=
 \begin{cases}
  1,&\text{no pair is selected},\\
  1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
    +2\mathbf1_{p_Nq_N\mid d},&\text{a pair is selected}.
 \end{cases}
\tag{K185.1}
\]

Define the total zero-extended endpoint coefficient

\[
 \lambda_{N,\sigma}(d)=
 \begin{cases}
  \mu^2(N)\rho_N(d)
  a_{L,X}^{\mathrm{lit},\sigma}(N/d,d),
   &N,d>0,\ \mu^2(N)=1,\ d\mid N,\ 2\nmid d,\\
  0,&\text{otherwise},
 \end{cases}
\tag{K185.2}
\]

and

\[
 c_{N,\sigma}^{\rm rem}=\sum_d\chi_4(d)\lambda_{N,\sigma}(d),
 \qquad c_{N,\sigma}^{\rm rem}=0\quad(N\leq0).
\tag{K185.3}
\]

The literal symbol is zero off every original shell, height, strict
\(4m<d<16m\) cone, profile, floor, star, half-weight, hard-sample,
crossing, endpoint, sign, squarefree, and coprimality predicate.  Hence
(K185.3) is exactly the Round-184 no-pair plus selected-neither/both
residual.  On support,

\[
 d,m\asymp L,\qquad d\text{ odd},\qquad(d,m)=1,\qquad
 N=dm\asymp L^2,\qquad
 |\lambda_{N,\sigma}(d)|\ll_\varepsilon X^\varepsilon.
\tag{K185.4}
\]

Put

\[
 H_B=\left\lfloor(\log(2X))^B\right\rfloor,
 \qquad R_0=\lceil L\rceil.
\tag{K185.5}
\]

Open the even-shift Fejer correlation into ordered endpoint allocations

\[
 N=dm,\qquad N+r=d'm',\qquad d,d'\text{ odd},
 \qquad 0<r<R_0,\quad2\mid r.
\tag{K185.6}
\]

Let \(a=d'-d\), \(b=m'-m\).  The complete physical union consisting
of the monotone sector \(a,b\geq0\) and both opposing sectors
\(ab<0\) with the joint quotient \(h\leq H_B\), defined below, obeys

\[
 \boxed{
 \sum_{\substack{\text{opened even-shift incidences}\\
                  a,b\geq0\ \text{or}\ (ab<0,\ h\leq H_B)}}
 |\text{literal correlation summand}|
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{K185.7}
\]

This is a strict target-safe opened-incidence sector, not an estimate for
the complete residual.  Its exact complement is the canonical signed
aggregate (K185.36) below, containing both opposing orientations with
\(h>H_B\) under one outer real part.

## Endpoint-exact parity connector

Set

\[
 z_N=c_{N,\sigma}^{\rm rem}e(\sigma\sqrt{XN}),\qquad
 D_{L,\sigma}=\sum_N|z_N|^2
 \ll_\varepsilon L^2X^\varepsilon,
\tag{K185.8}
\]

and extend \(z_N\) by zero to the full integer line.  For \(R\geq1\),
write

\[
 \mathfrak E_R={1\over R}\sum_{s\in\mathbb Z}
 \left|\sum_{j=0}^{R-1}z_{s+j}\right|^2,
\tag{K185.9}
\]

\[
 \mathfrak C_R^{(2)}=
 \sum_{1\leq q\leq\lfloor(R-1)/2\rfloor}
 \left(1-{2q\over R}\right)
 \sum_Nz_{N+2q}\overline{z_N}.
\tag{K185.10}
\]

Splitting each window into even and odd offsets gives the exact inequality

\[
 \boxed{\mathfrak E_R\leq2D_{L,\sigma}
       +4\Re\mathfrak C_R^{(2)}.}
\tag{K185.11}
\]

For odd \(R\), the terminal even gap \(R-1\) has coefficient \(4/R\);
for even \(R\), the terminal gap \(R-2\) has coefficient \(8/R\).
There is no endpoint error.  If the support is contained in an interval
of \(M_L\asymp L^2\) integer sites, then

\[
 \left|\sum_Nz_N\right|^2
 \leq{M_L+R-1\over R}\,\mathfrak E_R.
\tag{K185.12}
\]

At \(R=R_0\), the diagonal and prefactor are target-safe.  It is
therefore sufficient to prove
\(\Re\mathfrak C_{R_0}^{(2)}\ll_\varepsilon L^2X^\varepsilon\).
The parity connector itself supplies no cancellation.

## Tangent identities and the monotone sector

The opening (K185.6) is multiplicity one.  Write
\(a=2\alpha\), \(b=2\beta\).  Direct expansion gives

\[
 r=db+am+ab=db+am'=am+bd',
\tag{K185.13}
\]

\[
 {r\over2}=\alpha m+\beta d+2\alpha\beta
 =\alpha m'+\beta d=\alpha m+\beta d',
 \qquad
 \chi_4(d')\chi_4(d)=(-1)^\alpha.
\tag{K185.14}
\]

When \(a,b\geq0\), support and \(r\ll L\) leave only \(O(1)\)
displacement pairs and therefore \(O(L^2)\) opened incidences.  Both
coordinates nonpositive, or one zero and the other negative, are
incompatible with \(r>0\).  The exact complement of the monotone sector
is consequently

\[
 a>0>b\qquad\dot\cup\qquad a<0<b.
\tag{K185.15}
\]

## Original gcd, inward cross gcd, and joint quotient

For \(g=(d,d')\), write

\[
 d=gu,\qquad d'=gv,\qquad(u,v)=1,
 \qquad vm'-um={r\over g}.
\tag{K185.16}
\]

There are \(O(L^3/g^2)\) incidences at fixed \(g\), so

\[
 \#\{g\geq G\}\ll {L^3\over G}.
\tag{K185.17}
\]

In the plus orientation \(a=2s>0\), \(b=-2w<0\), put

\[
 \kappa=(d,m'),\quad
 d=\kappa u,\quad d'=\kappa u+2s,\quad
 m'=\kappa v,\quad m=\kappa v+2w,
\tag{K185.18}
\]

so

\[
 r=2\kappa n,\qquad n=sv-wu>0.
\tag{K185.19}
\]

In the minus orientation \(a=-2s<0\), \(b=2w>0\), put

\[
 \kappa=(d',m),\quad
 d'=\kappa u,\quad d=\kappa u+2s,\quad
 m=\kappa v,\quad m'=\kappa v+2w,
\tag{K185.20}
\]

so

\[
 r=2\kappa n,\qquad n=uw-sv>0.
\tag{K185.21}
\]

Both parametrizations are multiplicity one.  At fixed \(\kappa\) there
are \(O(L^3/\kappa^2)\) incidences, hence

\[
 \#\{\kappa\geq K\}\ll {L^3\over K}.
\tag{K185.22}
\]

Squarefreeness and allocation coprimality at the appropriate endpoint
give \((\kappa,s)=1\).  In both orientations,

\[
 g=(d,d')=(u,s)=(u,n).
\tag{K185.23}
\]

Write

\[
 u=gU,\qquad s=gS,\qquad n=gh.
\tag{K185.24}
\]

Then

\[
 r=2\kappa gh,
\tag{K185.25}
\]

and the plus and minus primitive equations are respectively

\[
 Sv-wU=h,\qquad Uw-vS=h.
\tag{K185.26}
\]

The invariant primitive outer domain is

\[
 \kappa,g,h,U,v>0,\quad
 \kappa,g,U\text{ odd},\quad
 (gU,v)=1,\quad(U,h)=1,\quad
 0<2\kappa gh<R_0.
\tag{K185.27}
\]

For fixed \((\kappa,g,h)\), support permits
\(O(L/(\kappa g))\) choices of \(U\), \(O(L/\kappa)\) choices of
\(v\), and \(O(\kappa)\) geometric sites on each primitive affine row.
Thus the count is \(O(L^2/(\kappa g))\), per orientation, and

\[
 \#\{ab<0:\ h\leq H\}
 \ll HL^2\log^2(2L).
\tag{K185.28}
\]

Together with the monotone count and the two endpoint coefficient bounds,
(K185.28) proves (K185.7), after absorbing fixed logarithmic powers into
\(X^\varepsilon\).  The earlier tail estimates retain the explicit
corollaries

\[
 g\geq\gamma L:
 O_\varepsilon(\gamma^{-1}L^2X^\varepsilon),\qquad
 \kappa\geq\delta L:
 O_\varepsilon(\delta^{-1}L^2X^\varepsilon).
\tag{K185.29}
\]

When \(H_B\geq(2\gamma)^{-1}\) or
\(H_B\geq(2\delta)^{-1}\), the corresponding fixed-proportion tail is
already contained in (K185.7), by (K185.25).

## Canonical exact complement

Let \([x]_U\) be the least residue in \(\{0,\ldots,U-1\}\).  For
\(U>1\), let \(\bar v\) be the inverse of \(v\bmod U\).  Choose

\[
 \begin{array}{lll}
 \text{plus:}&S_{0,+}=[\bar vh]_U,&
 w_{0,+}=(S_{0,+}v-h)/U,\\[1mm]
 \text{minus:}&S_{0,-}=[-\bar vh]_U,&
 w_{0,-}=(h+vS_{0,-})/U.
 \end{array}
\tag{K185.30}
\]

For \(U=1\), take
\((S_{0,+},w_{0,+})=(0,-h)\) and
\((S_{0,-},w_{0,-})=(0,h)\).  For \(\omega\in\{+,-\}\), define

\[
 S_{t,\omega}=S_{0,\omega}+Ut,\qquad
 s_{t,\omega}=gS_{t,\omega},\qquad
 w_{t,\omega}=w_{0,\omega}+vt,
\]

\[
 I_{\mathfrak f,\omega}
 =\{t\in\mathbb Z:S_{t,\omega}>0,\ w_{t,\omega}>0\},
 \qquad \mathfrak f=(\kappa,g,h,U,v).
\tag{K185.31}
\]

The positivity restriction is imposed before every square-root
evaluation.  In the plus orientation put

\[
 N_{\mathfrak f,t}^{+}
 =\kappa gU(\kappa v+2w_{t,+}),\qquad
 N_{\mathfrak f,t}^{+}+r
 =(\kappa gU+2s_{t,+})\kappa v,
\tag{K185.32}
\]

\[
 \begin{aligned}
 B_{\mathfrak f,+}^{\sigma}(t)={}&
 \left(1-{r\over R_0}\right)
 \lambda_{N_{\mathfrak f,t}^{+}+r,\sigma}
        (\kappa gU+2s_{t,+})
 \overline{\lambda_{N_{\mathfrak f,t}^{+},\sigma}(\kappa gU)}\\
 &\times e\!\left({\sigma\sqrt X\,r\over
 \sqrt{N_{\mathfrak f,t}^{+}+r}
 +\sqrt{N_{\mathfrak f,t}^{+}}}\right),
 \qquad r=2\kappa gh.
 \end{aligned}
\tag{K185.33}
\]

In the minus orientation put

\[
 N_{\mathfrak f,t}^{-}
 =(\kappa gU+2s_{t,-})\kappa v,\qquad
 N_{\mathfrak f,t}^{-}+r
 =\kappa gU(\kappa v+2w_{t,-}),
\tag{K185.34}
\]

\[
 \begin{aligned}
 B_{\mathfrak f,-}^{\sigma}(t)={}&
 \left(1-{r\over R_0}\right)
 \lambda_{N_{\mathfrak f,t}^{-}+r,\sigma}(\kappa gU)
 \overline{\lambda_{N_{\mathfrak f,t}^{-},\sigma}
        (\kappa gU+2s_{t,-})}\\
 &\times e\!\left({\sigma\sqrt X\,r\over
 \sqrt{N_{\mathfrak f,t}^{-}+r}
 +\sqrt{N_{\mathfrak f,t}^{-}}}\right),
 \qquad r=2\kappa gh.
 \end{aligned}
\tag{K185.35}
\]

Since \(U\) is odd,
\((-1)^{S_{t,\omega}}=(-1)^{S_{0,\omega}+t}\).  Removing the
target-safe sector (K185.7), the exact remaining even-shift correlation
is

\[
 \boxed{
 \Re\!\sum_{\omega\in\{+,-\}}
 \sum_{\substack{\mathfrak f\text{ satisfying }(\mathrm{K185.27})\\
                   h>H_B}}
 (-1)^{S_{0,\omega}}
 \sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t).}
\tag{K185.36}
\]

Canonical anchors, oriented positive index sets, and zero extensions make
(K185.36) multiplicity one.  It has one real part outside both
orientations, every shift, gcd, selector state, row, and endpoint.

For every dyadic \(Y>H_B\), the still-open estimate

\[
 \Re\!\sum_{\omega\in\{+,-\}}
 \sum_{\substack{\mathfrak f\text{ satisfying }(\mathrm{K185.27})\\
                  Y<h\leq2Y}}
 (-1)^{S_{0,\omega}}
 \sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t)
 \ll_\varepsilon L^2X^\varepsilon
\tag{K185.37}
\]

would close (K185.36) after epsilon rebudgeting.  Its positive capacity is
\(O(YL^2X^\varepsilon)\), so a genuinely global factor \(Y\) is
missing.

## Capacity and deletion controls

The bare alternating law does not supply the missing global factor.
Even an unjustified \(O(1)\) bound on each complete primitive row leaves

\[
 O\!\left(L^3\sum_{\kappa,g\geq1}{1\over\kappa^3g^2}\right)
 =O(L^3)
\tag{K185.38}
\]

after positive recombination.  More generally,

\[
 \sup_{|B(t)|\leq1}
 \left|\sum_{t\in I}(-1)^tB(t)\right|=|I|.
\tag{K185.39}
\]

An exact plus-orientation arithmetic control uses
\((\kappa,u,v,s,w)=(103,7,1,99,14)\).  The first local site is

\[
 (d,d',m',m)=(721,919,103,131),\qquad r=206.
\]

Both endpoint products are squarefree and allocation-coprime, both hard
ratios lie in \((4,16)\), and every odd prime divisor is
\(3\bmod4\).  Hence neither endpoint has an eligible opposite-character
pair and both residual masks equal one.  At the adjacent site
\((s,w)=(106,15)\),

\[
 (d,d',m',m)=(721,933,103,133),\qquad r=206,
\]

but the lower endpoint is deleted because \((721,133)=7\) and \(7^2\)
divides its product; the upper endpoint remains squarefree and coprime.
The character product flips sign.  In canonical plus coordinates these
are indices \(t=14,15\).  This exact-integer control proves only that
bare adjacent character alternation need not preserve literal arithmetic
support.  It proves no profile nonvanishing, lower mass, asymptotic
estimate, or failure of (K185.37).

## Scope and dependencies

The proved content is the endpoint-exact finite reduction and the strict
physical sector (K185.7), with exact complement (K185.36).  The complete
\(t=1\) residual and scalar estimate remain open.  The sole Round-185
terminal label is

`strict_hard_m1_t1_residual_tangent_gcd_sector`.

Direct accepted dependencies are:

- M9-M1-hard-top-t1-comparable-factor-exchange-sector;
- M9-M1-top-endpoint-transform;
- M9-M1-frequency-phase-diagram-R10;
- M9-M2-dyadic-weight-nondegeneracy; and
- Divisor-bound-elementary.

The accepted small-\(t\) primitive-ray theorem is routing context, not a
proof dependency.  The M2 tangent, alias, and conductor kernels are method
controls only, not M1 theorem dependencies.  No external theorem is used.

Keep open every \(t\geq2\) small-\(G\) incidence, the large-\(G\)
near-resonant complement, the complete small-\(t\) owner, both M1
parents, GAR, every M2 parent, endpoint uniformity, M9, both bridges, the
Gauss-circle target, and every exponent claim.

## Reviewed evidence

- the exact source candidate and its conductor reconciliation;
- reports/literal_residual_fejer_tangent_gcd_attack.md;
- reports/tangent_gcd_transfer_capacity_audit.md;
- reports/blind_residual_fejer_tangent_rederivation.md;
- controls/conductor_round185_exact_fibre_deletion_control.md;
- reviews/residual_fejer_parity_tangent_multiplicity_post_repair_verification.md;
- reviews/joint_h_count_power_and_deletion_post_repair_verification.md; and
- reviews/blind_post_unmask_literal_owner_scope_post_repair_verification.md.
