# Formal candidate: hard-M1 \(t=1\) \(P_2\) common-cell allocation commutator sector

- Campaign: `m9-m1-t1-p2-four-corner-allocation-commutator-gate`
- Round: 197
- Starting graph SHA-256:
  `b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae`
- Candidate status: conductor formalization; not accepted before independent
  seam review and a valid State Patch
- Numerical theorem evidence: none; the finite orbit search is diagnostic only

## 1. Statement

Fix real \(X\ge2\), one nonempty literal middle or lower residual
hard-M1 shell \(L\ge2\), \(\sigma\in\{+1,-1\}\), fixed \(B>0\), a
fixed selector constant \(K_{\mathrm{sel}}>0\), and a fixed accepted
Farey constant \(C_0\ge2\).  Put

\[
 y=\lfloor\sqrt X\rfloor,\qquad q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor,
\]

\[
 H_B=\lfloor(\log(2X))^B\rfloor,\qquad
 R_0=\lceil L\rceil,\qquad D_L=\lceil\sqrt L\rceil.
\tag{197.C1}
\]

For each squarefree \(N\), the Round-184 selector is fixed as follows.
Among unordered pairs of **distinct** odd prime divisors
\(p_N<q_N\) satisfying

\[
 \chi_4(p_Nq_N)=-1,\qquad
 |\log(q_N/p_N)|\le K_{\mathrm{sel}}L^{-1/2},
\tag{197.C1a}
\]

choose the lexicographically first ordered pair \((p_N,q_N)\) with
\(p_N<q_N\); if no such pair exists, select nothing.  This depends only on
\((N,L,K_{\mathrm{sel}})\), never on an allocation.  Define

\[
 \rho_N(v)=
 \begin{cases}
  1,&\text{no pair is selected},\\
  1-\mathbf1_{p_N\mid v}-\mathbf1_{q_N\mid v}
    +2\mathbf1_{p_Nq_N\mid v},&\text{a pair is selected}.
 \end{cases}
\tag{197.C1b}
\]

Retain the accepted total zero-extended endpoint coefficient

\[
 \lambda_{N,\sigma}(d)=
 \begin{cases}
 \mu^2(N)\rho_N(d)
 a_{L,X}^{\mathrm{lit},\sigma}(N/d,d),
 &N,d>0,\ \mu^2(N)=1,\ d\mid N,\ 2\nmid d,\\
 0,&\text{otherwise},
 \end{cases}
\tag{197.C2}
\]

where the literal symbol is itself zero outside its total accepted
domain.  It contains every original
shell, height, strict \(4m<d<16m\) cone, profile, floor, star, half
weight, hard sample, cell, crossing, endpoint, sign, squarefree,
allocation-coprimality, selector, conjugation, and zero-extension field.
On support,

\[
 |\lambda_{N,\sigma}(d)|\ll_\varepsilon X^\varepsilon.
\tag{197.C3}
\]

Open the complete even-shift correlation into

\[
 N=dm,\qquad N+r=d'm',\qquad d,d'\text{ odd},
 \qquad0<r<R_0,\quad2\mid r,
\tag{197.C4}
\]

with its character product and common scalar

\[
 \chi_4(d')\chi_4(d)\Phi_{r,\sigma}(N),\qquad
 \Phi_{r,\sigma}(N)=
 \left(1-{r\over R_0}\right)
 e\!\left({\sigma\sqrt X\,r\over\sqrt{N+r}+\sqrt N}\right).
\tag{197.C5}
\]

Put

\[
 g=(d,d'),\qquad d=g\alpha,\qquad d'=g\beta,
 \qquad(\alpha,\beta)=1,
\tag{197.C6}
\]

and impose the physical first-failure mask

\[
 P_2=\mathbf1_{|d-gm|\le D_L}
     \mathbf1_{|d'-gm'|>D_L}.
\tag{197.C7}
\]

Define the lower allocation-swap domain

\[
 P_0=P_2\mathbf1_{(m,\beta)=1}
          \mathbf1_{\chi_4(\alpha m)=-1}.
\tag{197.C8}
\]

For a lower allocation \(N=uv\), let \(I_{\rm ar}(u,v)\) be the
conjunction

\[
 u>0,\qquad v>0,\qquad uv=N,\qquad2\nmid v,
 \qquad\mu^2(N)=1,\qquad(u,v)=1.
\tag{197.C8a}
\]

Let \(I_{\rm lit}(u,v)\) be the conjunction that every named shell,
frequency, height, strict \(4u<v<16u\) cone, profile-support,
hard-sample, endpoint-support, and zero-extension predicate in
(K184.11)--(K184.15) and (K185.2)--(K185.4) is live.  Denote their exact
truth or branch labels by the following closed list:

\[
\begin{aligned}
 &\ell_{\rm shell},\ \ell_{\rm frequency},\ \ell_{\rm height},
 \ \ell_{\rm cone},\ \ell_{\rm profile},\ \ell_{\rm floor},
 \ \ell_{\rm star},\ \ell_{\rm tie},\ \ell_{1/2},\\
 &\ell_{\rm hard},\ \ell_{\rm cell},\ \ell_{\rm crossing},
 \ \ell_{\rm endpoint},\ \ell_{\rm sign}.
\end{aligned}
\tag{197.C8b}
\]

Here \(\ell_{\rm profile}\) records only support, plateau, and branch;
\(\ell_{\rm cell}\) records the literal \(\Phi\)- and
\(W_{\rm tr}\)-cells; \(\ell_{\rm crossing}\) includes the real-\(X\)
ratio branch; and floor, star, tie, half-weight, hard-sample, and
endpoint labels are their actual discrete trace labels.  None is an
evaluated coefficient or smooth-factor value.  Define the fixed sharp
code

\[
 \mathfrak c_{N,\sigma}(u,v)=
 \begin{cases}
  \dagger,&I_{\rm ar}(u,v)I_{\rm lit}(u,v)=0,\\[1mm]
  (\ell_{\rm shell},\ell_{\rm frequency},\ell_{\rm height},
   \ell_{\rm cone},\ell_{\rm profile},\ell_{\rm floor},
   \ell_{\rm star},\ell_{\rm tie},\ell_{1/2},\ell_{\rm hard},
   \ell_{\rm cell},\ell_{\rm crossing},\ell_{\rm endpoint},
   \ell_{\rm sign}),&I_{\rm ar}(u,v)I_{\rm lit}(u,v)=1.
 \end{cases}
\tag{197.C8c}
\]

The dead value \(\dagger\) is determined only by the named arithmetic,
support, and zero-extension predicates.  In particular the code excludes
the values of \(a^{\rm lit}\), \(\lambda\), \(\rho_N\), \(\eta_L\),
\(\Phi\), \(W_{\rm tr}\), and every smooth factor.  Accidental
vanishing of any of these quantities does not alter the code.  If the
common code below is live, every sharp multiplier and branch formula is
identical at the two inputs; if it is \(\dagger\), both lower symbols are
zero by named zero extension.  The selector and normalized BV profile
are audited separately.

Set

\[
 C_{\mathrm{lit}}=
 \mathbf1_{\{\mathfrak c_{N,\sigma}(m,g\alpha)
              =\mathfrak c_{N,\sigma}(\alpha,gm)\}},
 \qquad P_{\mathrm{cc}}=P_0C_{\mathrm{lit}}.
\tag{197.C9}
\]

The definition is symmetric under the lower swap and independent of
coefficient nonvanishing.  No nonemptiness, density, or positive-mass
assertion is part of the theorem.

The physical atom to which a mask is applied is, with all predicates in
(197.C2)--(197.C4) understood,

\[
 W(d,m,d',m')=
 \chi_4(d')\chi_4(d)\Phi_{r,\sigma}(N)
 \lambda_{N+r,\sigma}(d')\overline{\lambda_{N,\sigma}(d)}.
\tag{197.C9a}
\]

The physical inward cross gcd \(\kappa\) is fixed before any spectral
packet is formed.  In the plus orientation it is

\[
 \kappa=(d,m'),\quad d=\kappa u,\quad d'=\kappa u+2s,
 \quad m'=\kappa v,\quad m=\kappa v+2w,
\tag{197.C9b}
\]

and in the minus orientation it is

\[
 \kappa=(d',m),\quad d'=\kappa u,\quad d=\kappa u+2s,
 \quad m=\kappa v,\quad m'=\kappa v+2w.
\tag{197.C9c}
\]

Writing \(u=gU\), \(s=gS\), the corresponding primitive equations are
\(h=Sv-Uw>0\) and \(h=Uw-vS>0\), respectively, with
\(r=2\kappa gh\).  Thus this \(\kappa\) is not the selector constant
\(K_{\mathrm{sel}}\).

For the Round-192 spectral decomposition put \(Q=H_B\).  A fixed packet
has the accepted type

\[
 p=(\kappa,u,\mathfrak m,q,a,J,Y,\sigma),\qquad
 U=\mathfrak m q>4Q,\quad q>Q,\quad
 \mathfrak m|a|_q>Q,\quad Q\mathfrak m<Y,\quad U\mid u,
\tag{197.C9d}
\]

where \(Y\) is the dyadic height, \(\mathfrak m\) is the spectral lift
gcd, \(J\) is the accepted power-of-two projective-band label
\(J\le j_q(a,v)<2J\), and \(C_0\) is the fixed Farey-core constant; the
physical height block is \(Y<h\le2Y\).
For the accepted Farey projector let \(v_0=[v]_U\in\{1,\ldots,U-1\}\)
and choose the centered inverse data

\[
 \varrho v_0-\beta_{\rm F}U=1,\qquad
 -{U-1\over2}\le\varrho\le{U-1\over2},
\]

\[
 T=\min\left\{{U-1\over2},
 \left\lfloor{Q\mathfrak m U\over Y}\right\rfloor\right\},
 \qquad A=\min\{U-1,\lfloor Q^{C_0}\rfloor\},
\tag{197.C9e}
\]

and

\[
 \mathcal F_A=\{(c,d_0):1\le c\le A,\ 0\le d_0\le c,
 (c,d_0)=1\}.
\tag{197.C9f}
\]

At \(T=0\) the Farey-union projector is zero and the complete inherited
Round-191 \(\rho\)-large remainder is retained.  At \(T\ge1\), every
core row retains simultaneously

\[
 |c\beta_{\rm F}-d_0\varrho|>T\quad((c,d_0)\in\mathcal F_A),
 \qquad |\varrho|\ge(A+1)(T+1).
\tag{197.C9g}
\]

Let \(\mathscr R_{\mathrm{core,fix}}^{\sigma,p}(MW)\) be the exact
accepted Round-192 fixed-packet core linear functional evaluated on the
physical source \(MW\).  Let \(\mathcal O_{195}^\sigma\) denote the exact
linear fixed-packet-to-outer restoration of (195.C20)--(195.C20b): it
sums the \(\mathfrak m^{-1}\) lift weight, accepted anchor, band, divisor
and shell weights, dyadic partition, and both physical orientations with
their original zero extensions.  It takes no modulus at a fixed height,
orientation, anchor, or Fourier mode; the single outer real part is
taken only after this assembly.  For the fixed sign \(\sigma\), define

\[
 \mathscr R_{\mathrm{core,out}}^\sigma(MW)
 :=\mathcal O_{195}^\sigma
   \bigl(\{\mathscr R_{\mathrm{core,fix}}^{\sigma,p}(MW)
          :p\in\mathcal P_{\rm all}\}\bigr),
\tag{197.C9h}
\]

where \(M\) is evaluated on the physical parent atom before Fourier or
height operations.  Define \(\mathscr R_{\mathrm{cap,out}}^\sigma\) by
the same map restricted to

\[
 \mathcal P_{\rm cap}^{\rm all}
 =\{\kappa\ge D_L\}\ \dot\cup\
   \{\kappa<D_L:\min(Y,D_L)\le H_B\mathfrak m\kappa\},
\tag{197.C9i}
\]

and define \(\mathscr R_{\mathrm{open,out}}^\sigma\) by restriction to

\[
 \mathcal P_{\rm open}
 =\{\kappa<D_L:\min(Y,D_L)>H_B\mathfrak m\kappa\}.
\tag{197.C9j}
\]

Thus \(\mathcal P_{\rm all}=\mathcal P_{\rm cap}^{\rm all}
\dot\cup\mathcal P_{\rm open}\), and linearity gives, for every physical
mask \(M\le P_2\),

\[
 \mathscr R_{\mathrm{core,out}}^\sigma(MW)
 =\mathscr R_{\mathrm{cap,out}}^\sigma(MW)
  +\mathscr R_{\mathrm{open,out}}^\sigma(MW).
\tag{197.C9k}
\]

The \(T=0\) branch and every simultaneous strict \(T\ge1\) condition in
(197.C9g) are part of each fixed core in (197.C9h), rather than an extra
mask.  The estimates below are uniform in \(\sigma\); the two
values of \(\sigma\) are restored only in the final scalar and are not
separately normed.  With these definitions,

\[
 \boxed{
 |\mathscr R_{\mathrm{core,out}}^\sigma(P_{\mathrm{cc}}W)|
 \ll_{B,C_0,K_{\mathrm{sel}},\varepsilon}L^2X^\varepsilon.}
\tag{197.C10}
\]

Its exact Round-195 packet remainder is

\[
 \kappa<D_L,\qquad
 \min(Y,D_L)>H_B\mathfrak m\kappa.
\tag{197.C11}
\]

Then the intersection with the same physical mask is also target-safe:

\[
 \boxed{
 |\mathscr R_{\mathrm{open,out}}^\sigma(P_{\mathrm{cc}}W)|
 \ll_{B,C_0,K_{\mathrm{sel}},\varepsilon}L^2X^\varepsilon.}
\tag{197.C12}
\]

The packet condition is not inserted into the orbit.  Equation
(197.C12) follows only after the complete physical estimate and masked
core passage, by subtracting the accepted deletion-stable Round-195 safe
packet union.

The exact physical complement is

\[
\begin{aligned}
 P_{g\mathrm f}&=P_2\mathbf1_{(m,\beta)>1},\\
 P_{s\mathrm f}&=P_2\mathbf1_{(m,\beta)=1}
                    \mathbf1_{\chi_4(\alpha m)\ne-1},\\
 P_{\partial\mathrm{lit}}&=P_0(1-C_{\mathrm{lit}}),
\end{aligned}
\tag{197.C13}
\]

so

\[
 \boxed{
 P_2=P_{\mathrm{cc}}\ \dot\cup\ P_{\partial\mathrm{lit}}
       \ \dot\cup\ P_{s\mathrm f}\ \dot\cup\ P_{g\mathrm f}.}
\tag{197.C14}
\]

Only \(P_{\mathrm{cc}}\) is proved target-safe.

## 2. Exact allocation and character algebra

On \(P_0\), define

\[
 \tau_0(g\alpha,m,g\beta,m')=(gm,\alpha,g\beta,m').
\tag{197.C15}
\]

The recomputed gcd at the image is

\[
 (gm,g\beta)=g(m,\beta)=g.
\tag{197.C16}
\]

The reverse cross condition is \((\alpha,\beta)=1\), already true.
Both products, \(r\), the Fejer factor, radical phase, and defects are
unchanged.  Since \(\chi_4(\alpha m)=-1\), the orbit has two distinct
corners and the character reverses.  Summing each orbit once gives the
exact actual-coefficient identity

\[
 \chi_4(g\beta)\chi_4(g\alpha)\Phi_{r,\sigma}(N)
 \lambda_{N+r,\sigma}(g\beta)
 \overline{\{\lambda_{N,\sigma}(g\alpha)
             -\lambda_{N,\sigma}(gm)\}}.
\tag{197.C17}
\]

The formal four-corner construction is a valid subsidiary identity.  At
corners \((00),(10),(01),(11)\), the recomputed gcds are

\[
 g,\quad g(m,\beta),\quad g(\alpha,m'),\quad g(m,m').
\tag{197.C18}
\]

Under the three cross-coprimalities, the swaps commute.  Their relative
character multipliers are

\[
 (1,s_0,s_1,s_0s_1),\qquad
 s_0=\chi_4(\alpha m),\quad s_1=\chi_4(\beta m').
\tag{197.C19}
\]

On \(s_0=s_1=-1\) the actual table is the common sign
\(\chi_4(\alpha\beta)\) times \((+,-,-,+)\), \(4\mid r\), and

\[
\begin{aligned}
 &F(g\alpha,g\beta)-F(gm,g\beta)
  -F(g\alpha,gm')+F(gm,gm')\\
 &\quad=\{\lambda_{N+r,\sigma}(g\beta)
          -\lambda_{N+r,\sigma}(gm')\}
 \overline{\{\lambda_{N,\sigma}(g\alpha)
          -\lambda_{N,\sigma}(gm)\}}.
\end{aligned}
\tag{197.C20}
\]

But this full rectangle forces \(\kappa=1\): in the plus chart
\((\alpha,m')=(\kappa U,\kappa v)=\kappa\), and in the minus chart
\((m,\beta)=(\kappa v,\kappa U)=\kappa\).  It cannot estimate the open
packets \(2\le\kappa<D_L\), and the simultaneous swap alone has
multiplier \(s_0s_1=+1\) on the rectangular sector.

## 3. Common-cell coefficient and power ledger

The two lower symbol inputs are

\[
 (m,g\alpha),\qquad(\alpha,gm),
\tag{197.C21}
\]

and their displacement is \(O(D_L)\).  Equality of the sharp codes in
(197.C9) is invariant under exchanging these inputs.  On a common live
cell, let \(K_{\mathrm{sharp}}\) be the exact common product of the
allocation-independent shell/sign normalizer and the numerical sharp
mask and endpoint-trace multipliers indexed by (197.C8b)--(197.C8c).
Define

\[
 b_{L,X,\sigma}^{\mathrm{sm}}(u,v)
 :=\Phi\!\left({u\over H+1}\right)
 W_{\rm tr}\!\left(\sqrt{{4q_Xu\over v}}\right)
 \left({L^2\over uv}\right)^{3/4}.
\tag{197.C22}
\]

Here \(W_{\rm tr}\) is the transformed hard profile denoted by \(W\) in
(K184.11), distinguished from the physical atom (197.C9a).  The accepted
K184.11 ledger is then the exact identity

\[
 a_{L,X}^{\mathrm{lit},\sigma}(u,v)
 =K_{\mathrm{sharp}}\eta_L(u)
   b_{L,X,\sigma}^{\mathrm{sm}}(u,v)
\tag{197.C22a}
\]

at each of the two common-code live inputs.  There is no omitted moving
factor in (197.C22a): all discontinuous factors are in the enumerated
\(K_{\mathrm{sharp}}\), while the product-only power is the last factor
of (197.C22).  On the common enlarged cell, with fresh epsilon
rebudgeting,

\[
 |K_{\mathrm{sharp}}|+\|\eta_L\|_\infty
 +\operatorname{Var}(\eta_L)+\|b^{\mathrm{sm}}\|_\infty
 +L\|\nabla b^{\mathrm{sm}}\|_\infty
 \ll_\varepsilon X^\varepsilon.
\tag{197.C22b}
\]

Put

\[
 \rho_0=\rho_N(g\alpha),\quad \rho_1=\rho_N(gm),\quad
 \eta_0=\eta_L(m),\quad\eta_1=\eta_L(\alpha),
\]

\[
 b_0=b^{\mathrm{sm}}(m,g\alpha),\qquad
 b_1=b^{\mathrm{sm}}(\alpha,gm).
\tag{197.C22c}
\]

The actual lower coefficient difference, including the selector, is
therefore exactly

\[
\begin{aligned}
 \lambda_{N,\sigma}(g\alpha)-\lambda_{N,\sigma}(gm)
 =\mu^2(N)K_{\mathrm{sharp}}\{&
 \rho_0\eta_0(b_0-b_1)
 +\rho_0b_1(\eta_0-\eta_1)\\
 &+(\rho_0-\rho_1)\eta_1b_1\}.
\end{aligned}
\tag{197.C22d}
\]

Lower closeness gives \(|g\alpha-gm|\le D_L\), hence the displacement
of the two symbol inputs is \(O(D_L)\).  Thus

\[
 |b^{\mathrm{sm}}(m,g\alpha)
  -b^{\mathrm{sm}}(\alpha,gm)|
 \ll_\varepsilon {D_L\over L}X^\varepsilon.
\tag{197.C23}
\]

No pointwise derivative is assigned to \(\eta_L\).  Telescoping gives

\[
 \sum_{|a-b|\le D_L}|\eta_L(a)-\eta_L(b)|
 \ll D_L^2\operatorname{Var}(\eta_L)\ll_\varepsilon D_L^2X^\varepsilon.
\tag{197.C24}
\]

Indeed, after opening each difference into increments, one increment is
crossed by \(O(D_L^2)\) ordered close pairs.

On every live lower atom, \(m\ge cL\) for the accepted shell constant
\(c>0\).  The strict hard cone and lower closeness give, exactly as in
(193.C13),

\[
 1\le g\le {d\over m}+{D_L\over m}
 \le16+c^{-1}{D_L\over L}\le G_0,
\tag{197.C24a}
\]

because \(D_L\le2\sqrt L\).  Thus \(g\) ranges over one fixed finite
set, uniformly for every \(L\ge2\); this is also the \(O(1)\)
multiplicity used in (197.C24) and below.

The selector truth table from (197.C1b) is \((1,0,0,1)\).  Under
\(\tau_0\), every selected prime outside \(g\) is complemented and every
selected prime in \(g\) remains on the character leg.  The selector can
change only when exactly one selected prime divides \(g\).  Set

\[
 \delta_{G_0}=
 \min_{\substack{p\le G_0\ {\rm prime}\\q\ne p\ {\rm prime}}}
 |\log(q/p)|>0.
\tag{197.C24b}
\]

The primes in (197.C1a) are distinct.  If exactly one divides \(g\),
then one is at most \(G_0\), whereas (197.C1a) gives
\(|\log(q_N/p_N)|\le K_{\mathrm{sel}}L^{-1/2}\).  Hence the selector
commutator in (197.C22d) vanishes once
\(K_{\mathrm{sel}}L^{-1/2}<\delta_{G_0}\).  In the remaining bounded
set of shells, \(D_L=O_{K_{\mathrm{sel}},G_0}(1)\), and the raw
\(O(D_LL^2X^\varepsilon)\) physical count is already
\(O_{K_{\mathrm{sel}},\varepsilon}(L^2X^\varepsilon)\).

For fixed inward cross gcd \(\kappa\), the accepted physical count is

\[
 \mathcal C_\kappa
 \ll D_L(1+L/\kappa)^2.
\tag{197.C25}
\]

Therefore

\[
 \sum_{\kappa\ll L}\mathcal C_\kappa
 \ll D_L\{L+L\log(2L)+L^2\}
 \ll D_LL^2X^\varepsilon.
\tag{197.C26}
\]

Equivalently, there are \(O(LD_L)\) lower-close pairs and, for each,

\[
 \sum_{0<r<R_0}\tau(N+r)\ll_\varepsilon LX^\varepsilon
\tag{197.C27}
\]

upper completions.  The bounded upper coefficient and (197.C23) give

\[
 {D_L\over L}\,D_LL^2X^\varepsilon
 =D_L^2LX^\varepsilon\ll L^2X^\varepsilon.
\tag{197.C28}
\]

Equation (197.C24), multiplied by (197.C27), gives the same bound for
the normalized-BV summand in the exact three-term rule (197.C22d).  The
selector summand is zero for large shells by (197.C24b), and the bounded
shells were paid absolutely.  These three estimates exhaust the actual
coefficient difference; divisor losses and logarithmic sums are absorbed
only by fresh epsilon rebudgeting.  Since \(D_L^2\le4L\), no positive
power is hidden in \(X^\varepsilon\).

## 4. Physical source and masked-operator passage

The lower orbit is formed before the high-height, orientation, Fourier,
anchor, or Farey decompositions.  A swap may change the canonical
\(\kappa\), quotient \(h\), orientation, or dyadic block.  The complete
outer physical aggregate is retained.  Define
\(\mathscr H_{\mathrm{out}}^\sigma(MW)\) to be the exact sum of the
masked physical weights (197.C9a) over the complete opposing source after
the monotone and \(h\le H_B\) exits are removed, with both primitive
orientations, all dyadic blocks, zero extensions, and the accepted outer
assembly retained.  Define
\(\mathscr S_{\le192,\mathrm{out}}^\sigma(MW)\) to be the same outer
assembly of the Round-187--Round-192 safe projector outputs recomputed on
the physical source \(MW\).  These definitions give the exact linear
identity

\[
 \mathscr R_{\mathrm{core,out}}^\sigma(MW)
 =\mathscr H_{\mathrm{out}}^\sigma(MW)
  -\mathscr S_{\le192,\mathrm{out}}^\sigma(MW).
\tag{197.C28a}
\]

The accepted Round-185 absolute
theorem prices the full monotone sector and both opposing orientations
with \(h\le H_B\) by \(O(L^2X^\varepsilon)\).  Intersecting with
\(P_{\mathrm{cc}}\) only deletes atoms.  Removing these safe exits from
the ambient paired estimate proves

\[
 |\mathscr H_{\mathrm{out}}^\sigma(P_{\mathrm{cc}}W)|
 \ll_{B,K_{\mathrm{sel}},\varepsilon}L^2X^\varepsilon.
\tag{197.C29}
\]

The accepted Round-193 masked-operator identity and its Round-195 replay
permit every Round-187--Round-192 safe projector to be rerun after this
coordinatewise physical deletion.  At a transported site the exact
product rule is

\[
 M_hB_h-\chi M_-^{\mathrm{tr}}B_-^{\mathrm{tr}}
 =M_h(B_h-\chi B_-^{\mathrm{tr}})
  +\chi(M_h-M_-^{\mathrm{tr}})B_-^{\mathrm{tr}}.
\tag{197.C30}
\]

Thus the physical-mask commutator, affine births and deaths, unequal
endpoint translations, carries, phases, cells, crossings, zero
extensions, complete anchors, all inherited Fourier-sign copies, the
\(T=0\) branch,
and all simultaneous strict \(T\ge1\) Farey conditions remain in the
recomputed core.  The deletion-stable safe aggregate is

\[
 |\mathscr S_{\le192,\mathrm{out}}^\sigma
      (P_{\mathrm{cc}}W)|
 \ll_{B,C_0,K_{\mathrm{sel}},\varepsilon}L^2X^\varepsilon.
\tag{197.C31}
\]

Subtracting (197.C31) from (197.C29) through the exact linear core
identity proves (197.C10).

The accepted Round-195 safe packet union consists of every
\(\kappa\ge D_L\) packet and every \(\kappa<D_L\) packet with

\[
 \min(Y,D_L)\le H_B\mathfrak m\kappa.
\tag{197.C32}
\]

Its fixed-packet and outer proofs are positive and deletion-stable.
Rerunning them on \(P_{\mathrm{cc}}W\) gives

\[
 |\mathscr R_{\mathrm{cap,out}}^\sigma
       (P_{\mathrm{cc}}W)|
 \ll_{B,C_0,K_{\mathrm{sel}},\varepsilon}L^2X^\varepsilon.
\tag{197.C33}
\]

The exact packet split gives

\[
 \mathscr R_{\mathrm{open,out}}^\sigma(P_{\mathrm{cc}}W)
 =\mathscr R_{\mathrm{core,out}}^\sigma(P_{\mathrm{cc}}W)
  -\mathscr R_{\mathrm{cap,out}}^\sigma(P_{\mathrm{cc}}W),
\tag{197.C34}
\]

which proves (197.C12).  One outer real part is taken only after each
complete complex aggregate has been restored.

Applying the same linear operator to (197.C14) gives an exact open-core
decomposition.  The new remaining packet region is (197.C11) intersected
with

\[
 P_{\partial\mathrm{lit}}\ \dot\cup\ P_{s\mathrm f}
 \ \dot\cup\ P_{g\mathrm f}.
\tag{197.C35}
\]

## 5. Sharp-face boundary and false controls

The theorem does not extend from \(P_{\mathrm{cc}}\) to all of \(P_0\)
with the current interface.  The two lower ratios are

\[
 {g\alpha\over m},\qquad {gm\over\alpha}.
\tag{197.C36}
\]

For \(\alpha\ne m\),

\[
 \left({g\alpha\over m}-g\right)
 \left({gm\over\alpha}-g\right)
 =-{g^2(\alpha-m)^2\over\alpha m}<0.
\tag{197.C37}
\]

Hence a sharp ratio/profile face aligned with the line of ratio \(g\)
can be crossed by all \(O(LD_L)\) lower-close pairs.  Upper completion
then leaves \(D_LL^2X^\varepsilon\), not \(D_L^2LX^\varepsilon\).
The accepted artifacts contain no exhaustive face transversality theorem
uniform in real \(X\) and no continuity theorem across every aligned
branch.  This is the first literal-face self-return.  It is only an
upper-capacity obstruction and supplies no lower mass for the literal
operator.

The remaining false controls are quarantined as follows.

1. Erasing the character changes the lower difference into a sum.
2. The simultaneous swap has multiplier \(+1\) on the rectangular
   sector and cannot replace the lower edge.
3. A missing corner is evaluated at its literal zero; deleting a live
   corner or a changed-gcd corner is invalid.
4. Arbitrary bounded endpoint arrays need not satisfy the common-cell
   \(C^1\) or normalized-BV ledger.
5. A cornerwise phase conjugation destroys the common physical scalar;
   the physical swap itself does not conjugate that phase.
6. Deleting \(P_2\) removes the only close displacement.
7. Fixed-\(Y\), fixed-anchor, fixed-conductor, separate-orientation, or
   separate-frequency norms are not claimant operators.
8. Neither the diagnostic examples nor the capacities prove
   nonemptiness, density, nonvanishing, or lower mass.

## 6. Dependencies and scope

The following accepted interfaces are reopened directly and are logical
prerequisites of this candidate.

1. `M9-M1-hard-top-t1-comparable-factor-exchange-sector`, represented by
   `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`,
   supplies the exact selector (K184.4), literal moving-factor ledger
   (K184.11), common-cell smooth/BV rules (K184.12)--(K184.16), and all
   named sharp fields used in (197.C8b)--(197.C8c).
2. `M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction`, represented
   by
   `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`,
   supplies the total zero-extended endpoint (K185.1)--(K185.4),
   multiplicity-one even-shift source (K185.6), the two primitive charts
   (K185.18)--(K185.27), and the absolute monotone/low-\(h\) exit theorem
   (K185.7).
3. `M9-M1-hard-top-t1-rho-large-gcd-scaled-close-sector`, represented by
   `proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md`,
   supplies the uniform finite-\(g\) lemma (193.C13), the exact
   physical-mask evaluation and transported-mask product rule
   (193.C19b)--(193.C21), and no one-close \(P_2\) estimate.
4. `M9-M1-hard-top-t1-rho-large-P2-absolute-capacity-sectors`, represented
   by
   `proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md`,
   supplies the fixed-\(\kappa\) physical count
   (195.C14)--(195.C17), deletion-stable masked-operator passage
   (195.C18), packet estimate (195.C20), fixed-to-outer ledger
   (195.C20b), and exact safe/open split (195.C5a).

These are accepted theorem interfaces.  The Round-197 reports and reviews
below are claimant and seam evidence, not substitute prerequisites; the
finite computation is not theorem evidence.

The claimant/reconciliation evidence is exactly
`reports/literal_four_corner_allocation_commutator_attack.md`,
`reports/four_corner_orbit_power_hostile_audit.md`,
`reports/blind_four_corner_commutator_rederivation.md`, and
`reviews/conductor_round197_report_reconciliation.md`, relative to this
campaign directory.  The finite orbit diagnostic is explicitly
diagnostic-only and is not theorem evidence.

This candidate proves only \(P_{\mathrm{cc}}\) and its exact
intersection with the open \(P_2\) packets.  It proves neither the full
lower-swap sector \(P_0\), the full four-corner rectangle, complete
\(P_2\), \(P_1\), complete original \(t=1\), any other original-\(t\)
incidence, the hard small-\(t\) owner, either M1 parent, GAR, any M2
parent, endpoint uniformity, M9, either bridge, or the Gauss-circle
target.  The internal exponent \(1/3\), accepted external benchmark
\(0.3144831759740614\ldots\), and target \(1/4\) are unchanged.

## 7. Proposed state effect

After independent coefficient/algebra, power/operator, blind/scope,
formalization/provenance, and graph-replay reviews:

1. create one subordinate `proved_internal` node for (197.C1)--(197.C35);
2. add it only as strict-sector evidence to the still-open hard-M1
   small-\(t\) owner;
3. leave the accepted Round-184, Round-185, Round-193, and Round-195
   nodes unchanged; record the refined remainder (197.C35) only in the
   new node and the open owner's `next_action`, so no reverse dependency
   or Round-197/Round-195 cycle is created;
4. record (197.C18)--(197.C20), the forced \(\kappa=1\) restriction, and
   the sharp-face self-return (197.C36)--(197.C37); and
5. leave every parent, bridge, theorem, and exponent unchanged.

The round closes under the frozen terminal label
`p2_four_corner_orbit_boundary_self_return_no_go`, while retaining the
reviewed subordinate common-cell sector.
