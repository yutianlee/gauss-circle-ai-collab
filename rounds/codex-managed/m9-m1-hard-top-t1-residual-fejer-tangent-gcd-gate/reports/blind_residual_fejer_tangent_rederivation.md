---
campaign: m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate
task: round185_blind_residual_rederivation
role: statement-only blind rederiver
pre-normalization-sha256: a51982e042e34cf36c5310f1f22c376edcbdd7db1b5ad02745ea673cd545547a
edit-scope: typographic normalization only
---

# 1. Result

The requested correlation estimate is not derivable from the stated data alone.  What can be proved, without any density, variation, or Fourier-norm assumption, is the following exact connector and capacity theorem.

* The sliding Fejer identity is exact, and Cauchy at the two support endpoints gives
  \[
  \left|\sum_Nz_N\right|^2\le {M_L+R-1\over R}\,\mathfrak E_R.
  \]
  Splitting each window into its even and odd offsets gives the endpoint-exact inequality
  \[
  \mathfrak E_R\le 2D_L+4\Re\!\sum_{1\le q\le \lfloor(R-1)/2\rfloor}
       \left(1-{2q\over R}\right)
       \sum_Nz_{N+2q}\overline {z_N}.                                      \tag{1.1}
  \]
  If $R=2h+1$, the term $q=h$, i.e. the terminal gap $2q=R-1$, occurs with weight $1/R$ inside the sum and coefficient $4/R$ in (1.1).  It cannot be dropped.

* On every even-shift allocation incidence, with $a=d'-d=2\alpha$ and $b=m'-m=2\beta$,
  \[
  {r\over2}=\alpha m+\beta d+2\alpha\beta
  =\alpha m'+\beta d=\alpha m+\beta d',
  \qquad
  \chi _4(d')\chi _4(d)=(-1)^\alpha .                                      \tag{1.2}
  \]
  The exact complement of $a,b\ge0$ is the disjoint union $a>0>b$ and $a<0<b$.

* The complete monotone sector has $O(L^2)$ allocation incidences.  For the original gcd $g=(d,d')$, the sector $g\ge G$ has
  \[
  O(L^3/G)                                                               \tag{1.3}
  \]
  incidences; hence $g\ge\gamma L$ costs $O(\gamma^{-1}L^2)$.  In either cross orientation, if $\kappa$ is the inward cross gcd specified below, the union of the two sectors $\kappa\ge K$ has $O(L^3/K)$ incidences; hence $\kappa\ge\delta L$ costs $O(\delta^{-1}L^2)$.  All dependence on fixed $\gamma,\delta$ is explicit.

* There is a stronger joint gcd normal form on the cross sector.  Writing $g=(d,d')$, one has $g\mid n$, where $n=r/(2\kappa)$.  With $h=n/g$, every active cross incidence satisfies
  \[
  r=2\kappa gh.                                                          \tag{1.4}
  \]
  For each fixed positive integer $H$, the complete cross sector $h\le H$ has
  \[
  O\!\left(HL^2\log ^2(2L)\right)                                      \tag{1.5}
  \]
  incidences and is therefore target-safe under the allowed subpolynomial-loss convention.  If $H\ge\max\{\lceil(2\gamma)^{-1}\rceil,\lceil(2\delta)^{-1}\rceil\}$, this sector contains the two fixed-proportion gcd sectors and also includes many incidences with both gcds smaller than a fixed proportion of $L$.

For fixed $\gamma,\delta>0$ and fixed $H\ge1$, let the safe set be the union of the monotone sector, $g\ge\gamma L$, the appropriate inward cross-gcd sector $\kappa\ge\delta L$, and the cross sector $h\le H$.  Taking one modulus only after aggregating this whole capacity-safe union gives
\[
 \left|\mathfrak C^{\rm even}_{R,\mathrm{safe}}\right|
 \ll \left(1+\gamma^{-1}+\delta^{-1}+H\log ^2(2L)\right)L^2\mathcal X^2,
                                                                            \tag{1.6}
\]
where, as usual for the stated allowed subpolynomial loss, a fixed power of $\mathcal X$ and logarithms may be renamed $\mathcal X$.  The exact unresolved complement is
\[
\begin{split}
 \mathcal U^+_{\gamma,\delta,H}
 &=\{a>0>b:\ g<\gamma L,\ \kappa_+=(d,m')<\delta L,\ h_+>H\},\\
 \mathcal U^-_{\gamma,\delta,H}
 &=\{a<0<b:\ g<\gamma L,\ \kappa_-=(d',m)<\delta L,\ h_->H\},             \tag{1.7}
\end{split}
\]
with every literal predicate from the statement retained.  No row-density assertion is made.

The bare character alternates under the primitive tangent step on both cross orientations, but the full literal weight does not have a stated self-return law.  Moreover, even a hypothetical $O(1)$ bound obtained separately on every primitive row leaves $O(L^3)$ row capacity in the corner $\kappa=g=1$.  Thus rowwise alternation is not the missing global cancellation.  A uniform signed dyadic estimate across the remaining row labels (in particular across $h$) is the first additional literal relation needed.  Consequently neither (B185.8) nor (B185.9) is proved here.

# 2. Exact statement and hypotheses

Fix $L\ge2$, $X\ge2$, $\sigma\in\{+1,-1\}$, and $R\ge2$.  All assertions below apply to the one literal coefficient in the packet.  Choose fixed constants $0<c_*<C_*<\infty$, supplied by the notation $m,d\asymp L$, such that a nonzero pair of coefficient factors forces
\[
 c_*L\le m,d,m',d'\le C_*L.                                                \tag{2.1}
\]
No constant below depends on $L,X,\sigma$, on a selector, or on a tangent row.  Constants may depend on $c_*,C_*$ and on the fixed literal shell definitions.

Let
\[
 K_r=\sum_Nz_{N+r}\overline {z_N},\qquad
 \mathfrak C_R^{\rm even}
 =\sum_{1\le q\le\lfloor(R-1)/2\rfloor}
 \left(1-{2q\over R}\right)K_{2q}.                                       \tag{2.2}
\]
Then (1.1) holds for every finitely supported complex sequence $z$.  If $z$ is zero-extended outside a containing interval of exactly $M_L$ sites, then
\[
 \left|\sum_Nz_N\right|^2\le {M_L+R-1\over R}\mathfrak E_R.               \tag{2.3}
\]
Hence, at $R=R_0=\lceil L\rceil$, the accepted diagonal bound together with
\[
 \Re\mathfrak C_{R_0}^{\rm even}\ll L^2\mathcal X                         \tag{2.4}
\]
would imply (B185.9).  This is an alternative sufficient signed target; parity splitting itself supplies no cancellation.

For an even shift $r=2q<R_0$, let $\Omega_r$ be the set of quadruples $(d,m,d',m')$ giving nonzero terms when both coefficients are opened, so that
\[
 dm=N,\qquad d'm'=N+r,\qquad d,d'\text{ odd}.                               \tag{2.5}
\]
Every squarefree, coprimality, ratio, shell, height, profile, floor, star, half-weight, hard-sample, crossing, endpoint, and zero-extension condition is part of membership in $\Omega_r$, or equivalently is a zero-one deletion factor.  The two residual selectors are also zero-one weights.  The literal values of the two $A$'s and the phase are weights, not density assumptions.

For $1\le G,K\le L/2$, the following global incidence bounds hold:
\[
\begin{array}{ll}
 \#\{\Omega_{2q}:a,b\ge0\}&\ll L^2,\\[2mm]
 \#\{\Omega_{2q}:(d,d')\ge G\}&\ll L^3/G,\\[2mm]
 \#\{\Omega_{2q}:ab<0,\ \kappa_{\rm in}\ge K\}&\ll L^3/K,\\[2mm]
 \#\{\Omega_{2q}:ab<0,\ h\le H\}&\ll HL^2\log^2(2L).
\end{array}                                                               \tag{2.6}
\]
The counts range over all $q$ in (2.2), both cross orientations where relevant, and all allocation variables.  Thus they are capacity estimates on entire sectors, not moduli taken shift by shift, row by row, gcd by gcd, orientation by orientation, or selector status by selector status.

The exact cross parameters are as follows.

* If $a>0>b$, put $a=2s$, $b=-2w$,
  \[
  \kappa_+=(d,m'),\qquad d=\kappa u,\quad m'=\kappa v,
  \quad d'=\kappa u+2s,\quad m=\kappa v+2w.                                \tag{2.7}
  \]
  Then $(u,v)=1$, $u$ and $\kappa$ are odd, and
  \[
  r=2\kappa(sv-wu),\qquad n=sv-wu>0.                                      \tag{2.8}
  \]

* If $a<0<b$, put $a=-2s$, $b=2w$,
  \[
  \kappa_-=(d',m),\qquad d'=\kappa u,\quad m=\kappa v,
  \quad d=\kappa u+2s,\quad m'=\kappa v+2w.                               \tag{2.9}
  \]
  Then
  \[
  r=2\kappa(wu-sv),\qquad n=wu-sv>0.                                      \tag{2.10}
  \]

In either case, with $g=(d,d')$, active coprimality gives $g\mid n$.  Defining $h=n/g$ gives (1.4).  The full literal cross contribution has the exact form
\[
 \Re\sum_{\mathfrak f}\epsilon_{\mathfrak f}
       \sum_{t\in\mathbb Z}(-1)^t B_{\mathfrak f}^{\sigma}(t),            \tag{2.11}
\]
where there is one real part outside the aggregate, $\mathfrak f$ ranges over both orientations and all primitive row labels, $\epsilon_{\mathfrak f}\in\{\pm1\}$, and $B_{\mathfrak f}^{\sigma}(t)$ contains every selector, arithmetic deletion, literal coefficient, endpoint, zero-extension, Fejer weight, and the phase with the original $\sigma$.  No bound for (2.11) beyond capacity is assumed.

# 3. Proof or derivation

## Sliding identity, endpoints, and even gaps

Write
\[
 W_s=\sum_{j=0}^{R-1}z_{s+j}.
\]
On expanding and putting $r=k-j$, every ordered pair of offsets at positive gap $r$ occurs $R-r$ times.  Therefore
\[
 {1\over R}\sum_s|W_s|^2
 =\sum_N|z_N|^2+2\Re\sum_{1\le r<R}
       \left(1-{r\over R}\right)\sum_Nz_{N+r}\overline {z_N},              \tag{3.1}
\]
which is (B185.6)--(B185.7), since
\[
 z_{N+r}\overline {z_N}
 =c_{N+r,\sigma}^{\rm rem}\overline {c_{N,\sigma}^{\rm rem}}
 e\!\left({\sigma\sqrt X\,r\over\sqrt{N+r}+\sqrt N}\right).             \tag{3.2}
\]
The sign $\sigma$ has not been normalized away.

If the containing support interval is $[A,A+M_L-1]$, then $W_s$ can be nonzero only for
\[
 A-R+1\le s\le A+M_L-1,
\]
an interval of exactly $M_L+R-1$ starting positions.  Also
\[
 \sum_sW_s=R\sum_Nz_N.
\]
Cauchy on precisely these starting positions proves (2.3); no endpoint term is suppressed.

Next put
\[
 W_s^{(0)}=\sum_{\substack{0\le j<R\\j\ {\rm even}}}z_{s+j},\qquad
 W_s^{(1)}=\sum_{\substack{0\le j<R\\j\ {\rm odd}}}z_{s+j}.
\]
Let $h_0=\lceil R/2\rceil$, $h_1=\lfloor R/2\rfloor$.  The elementary inequality

\[
 |W_s^{(0)}+W_s^{(1)}|^2\le2|W_s^{(0)}|^2+2|W_s^{(1)}|^2
\]
and exact expansion of the two nonnegative energies give
\[
 \sum_s|W_s^{(\nu)}|^2
 =h_\nu D_L+2\Re\sum_{q=1}^{h_\nu-1}(h_\nu-q)K_{2q}.
\]
For $1\le q\le\lfloor(R-1)/2\rfloor$,
\[
 (h_0-q)_++(h_1-q)_+=R-2q.                                                 \tag{3.3}
\]
Substitution proves (1.1).  When $R=2h+1$, (3.3) at $q=h$ reads $1+0=1$, proving the asserted terminal contribution.

At $R_0=\lceil L\rceil$, one has $R_0-1<L$ and $M_L\asymp L^2$, so (2.3) costs $O(L)$.  Thus $\mathfrak E_{R_0}\ll L^2\mathcal X$ implies (B185.9), after harmlessly renaming a square root of a subpolynomial loss.  The full target (B185.8) implies the same energy bound directly through (3.1); (2.4) is the separate even-gap route furnished by (1.1).

## Exact residual-pair algebra and its shell obstruction

For a selected pair $P=p_Nq_N$, the truth table in (B185.1) says exactly
\[
 \rho_N(d)=1\quad\Longleftrightarrow\quad
 \{p_N,q_N\}\subset d\ \hbox{ or }\ \{p_N,q_N\}\subset N/d.               \tag{3.4}
\]
Thus $0\le\rho_N(d)\le1$.  Put $K=N/P$.  Since $N$ is squarefree, every surviving odd divisor is uniquely either $e$ or $Pe$, with $e\mid K$ odd.  Because $\chi _4(P)=-1$, the selected-pair coefficient has the exact paired form
\[
 c_{N,\sigma}^{\rm rem}
 =\mu^2(N)\sum_{\substack{e\mid K\\e\ {\rm odd}}}\chi _4(e)
 \left[
 A_{L,X}^{\sigma}(PK/e,e)-A_{L,X}^{\sigma}(K/e,Pe)
 \right].                                                                 \tag{3.5}
\]
Zero extension of $A$ makes (3.5) exact even when only one displayed allocation is literal.

Equation (3.5) is a difference, but it is not an available same-$N$ cancellation in the hard ratio shell.  The two divisor-to-cofactor ratios are
\[
 \theta_0={e\over PK/e}={e^2\over PK},\qquad
 \theta_1={Pe\over K/e}={Pe^2\over K}=P^2\theta_0.                         \tag{3.6}
\]
Here $P\ge3\cdot5=15$.  Two numbers both lying in $(4,16)$ have ratio $<4$, whereas $\theta_1/\theta_0=P^2\ge225$.  Hence at most one member of every bracket in (3.5) can obey $4m<d<16m$.  The residual truth table therefore supplies a signed deletion/relabeling, not a self-returning pair inside the hard shell.  All further literal predicates can only delete more terms.

## Multiplicity-one opening, parity, product, character, and phase

Opening both coefficients in $K_r$ gives exactly
\[
\begin{split}
K_r={}&\sum_{d,m,d',m'}
 \mathbf 1_{d'm'-dm=r}\,
 \mu^2(dm)\mu^2(d'm')\,
 \chi _4(d')\chi _4(d)\\
&\quad\times\rho_{d'm'}(d')\rho_{dm}(d)
 A_{L,X}^{\sigma}(m',d')\overline {A_{L,X}^{\sigma}(m,d)}
 e\!\left({\sigma\sqrt X\,r\over\sqrt{d'm'}+\sqrt{dm}}\right),           \tag{3.7}
\end{split}
\]
where the sum may be unrestricted because all literal zero conditions remain in the factors.  The map
\[
 (N,d,d')\longleftrightarrow(d,N/d,d',(N+r)/d')
\]
is a bijection on the opened terms.  Thus there is no allocation multiplicity hidden in (3.7), and the canonical selector attached to $N$ is not reselected when an allocation is opened.

Let $a=d'-d$, $b=m'-m$.  Since $d,d'$ are odd, $a$ is even.  If $r$ is even, reduction of $d'm'-dm$ modulo $2$ shows $b\equiv r\equiv0\pmod2$.  Put $a=2\alpha$, $b=2\beta$, with signed integers $\alpha,\beta$.  Direct expansion in all useful orientations gives
\[
\begin{split}
r&=(d+a)(m+b)-dm=am+bd+ab\\
 &=am'+bd=am+bd',                                                     \tag{3.8}\\
q={r\over2}&=\alpha m+\beta d+2\alpha\beta
 =\alpha m'+\beta d=\alpha m+\beta d'.                              \tag{3.9}
\end{split}
\]
For every odd $x$, $\chi _4(x+2j)=\chi _4(x)(-1)^j$.  Hence
\[
 \chi _4(d')\chi _4(d)=(-1)^\alpha.                                       \tag{3.10}
\]
These identities hold for both signs of $a,b$; the phase in (3.7) retains the prescribed $\sigma$.

## Complete monotone sector and its exact opposing sector

Suppose $\alpha,\beta\ge0$.  They are not both zero because $r>0$.  From (3.9), (2.1), and $q<(R_0/2)\le L/2+1/2$,
\[
 c_*L(\alpha+\beta)\le q,
\]
so $\alpha+\beta=O_{c_*}(1)$.  For each of the finitely many pairs $(\alpha,\beta)$, the choices of $d,m$ number $O(L^2)$, and then $d',m',r$ are determined.  Every literal condition is a deletion or a bounded weight, so the complete monotone sector has $O(L^2)$ incidences and weighted absolute capacity $O(L^2\mathcal X^2)$.

If $a,b\le0$, then $d'\le d$ and $m'\le m$, so $d'm'\le dm$, contrary to $r>0$.  Consequently the complement of $a,b\ge0$ in the complete active even-shift incidence set is exactly
\[
 \{a>0>b\}\ \dot\cup\ \{a<0<b\}.                                      \tag{3.11}
\]
In particular, the axes $a=0<b$ and $b=0<a$ belong to the monotone sector, while a negative coordinate cannot be opposed by a zero coordinate.  No density of (3.11) is inferred.

## Original-gcd normal form, row multiplicity, and count

Put
\[
 g=(d,d'),\qquad d=gu,\qquad d'=gv,\qquad (u,v)=1.                         \tag{3.12}
\]
All of $g,u,v$ are odd.  Equation (3.8) becomes the primitive linear equation
\[
 v m'-u m=k,\qquad k={r\over g}.                                           \tag{3.13}
\]
Thus $g\mid r$.  Since $r$ is even and $g$ odd, $k$ is a positive even integer.  Conversely, if $(m_0,m'_0)$ is one solution of $vm'-um=k$, every solution is uniquely
\[
 m=m_0+vt,\qquad m'=m'_0+ut,\qquad t\in\mathbb Z.                          \tag{3.14}
\]
The parity $m\equiv m'\pmod2$ follows automatically from (3.13), because $u,v$ are odd and $k$ is even.  The character is constant on this row and satisfies
\[
 \chi _4(d')\chi _4(d)=\chi _4(uv)
 =(-1)^{(v-u)/2}.                                                          \tag{3.15}
\]
This covers $v>u$, $v<u$, and the axis case $u=v=1$.

For an endpoint-exact geometric row formula, set
\[
 J(D)=\{M\in\mathbb Z:c_*L\le M\le C_*L,\ 4M<D<16M\}.                    \tag{3.16}
\]
It is an integer interval (possibly empty), with endpoints
\[
 j_-(D)=\max\{\lceil c_*L\rceil,\lfloor D/16\rfloor+1\},\qquad
 j_+(D)=\min\{\lfloor C_*L\rfloor,\lceil D/4\rceil-1\}.                 \tag{3.17}
\]
Before the opaque literal deletions, the admissible row is
\[
 I_{g,u,v,k}^{\rm geom}
 =\{t:m_0+vt\in J(gu),\ m'_0+ut\in J(gv)\}.                               \tag{3.18}
\]
If $L_0$ is the maximum of the two corresponding ceiling lower bounds in $t$, and $U_0$ the minimum of the two floor upper bounds, its exact multiplicity is
\[
 |I_{g,u,v,k}^{\rm geom}|=[U_0-L_0+1]_+.                                  \tag{3.19}
\]
In particular,
\[
 |I_{g,u,v,k}^{\rm geom}|\ll 1+{L\over\max(u,v)}\ll 1+g.                 \tag{3.20}
\]
The active row is an arbitrary subset of (3.18) after all remaining predicates and selectors are inserted.

For fixed $g$, (2.1) gives $u,v\asymp L/g$, hence $O(L/g)$ choices for each.  Also $k<L/g$, and (3.20) gives $O(g)$ row points.  Therefore the total capacity at this exact gcd is
\[
 O\!\left((L/g)^2(L/g)g\right)=O(L^3/g^2).                                \tag{3.21}
\]
Summing (3.21) for $g\ge G$ proves
\[
 \#\{g\ge G\}\ll L^3\sum_{g\ge G}g^{-2}\ll {L^3\over G}.              \tag{3.22}
\]
There are in fact no rows with $g\ge L/2$, because the positive even integer $k$ and $gk=r<L$ force $2g<L$.  Taking $G=\gamma L$ gives $O(\gamma^{-1}L^2)$; the factor $\gamma^{-1}$ is not hidden and $\gamma$ has not been allowed to shrink with $L$.

## Both inward cross-gcd normal forms, their characters, and their counts

In the plus orientation $a=2s>0$, $b=-2w<0$.  Put
\[
 \kappa=(d,m'),\qquad d=\kappa u,\qquad m'=\kappa v,
\]
so $(u,v)=1$, $\kappa,u$ are odd, and
\[
 d'=\kappa u+2s,\qquad m=\kappa v+2w.                                     \tag{3.23}
\]
Substitution gives exactly
\[
 d'm'-dm=2\kappa(sv-wu).                                                   \tag{3.24}
\]
Thus $n=sv-wu=r/(2\kappa)>0$.  For any particular solution $(s_0,w_0)$, primitivity of $(u,v)$ gives all solutions once:
\[
 s=s_0+ut,\qquad w=w_0+vt.                                                 \tag{3.25}
\]
The character law is
\[
 \chi _4(d')\chi _4(d)=(-1)^s=(-1)^{s_0+t},                               \tag{3.26}
\]
because $u$ is odd.

In the minus orientation $a=-2s<0$, $b=2w>0$, put
\[
 \kappa=(d',m),\qquad d'=\kappa u,\quad m=\kappa v,
\quad d=\kappa u+2s,\quad m'=\kappa v+2w.                                 \tag{3.27}
\]
Then
\[
 d'm'-dm=2\kappa(wu-sv),\qquad n=wu-sv={r\over2\kappa}>0,                 \tag{3.28}
\]
and again all solutions are (3.25).  Here $a/2=-s$, so the same exact law holds:
\[
 \chi _4(d')\chi _4(d)=(-1)^{-s}=(-1)^s=(-1)^{s_0+t}.                     \tag{3.29}
\]
Both orientations have therefore been retained, and neither has been separately real-parted or separately estimated as a purported cancellation.

The geometric $t$-set in (3.25) is the intersection of the inequalities $s,w\ge1$, the four size inequalities, and the two hard-ratio inequalities after (3.23) or (3.27).  It is a consecutive integer interval.  Since $u,v\asymp L/\kappa$, its length is
\[
 O\!\left(1+{L\over\max(u,v)}\right)=O(1+\kappa).                        \tag{3.30}
\]
All other literal conditions may punch arbitrary holes in that interval.

For a fixed exact $\kappa$, there are $O(L/\kappa)$ choices of each of $u,v$, $O(L/\kappa)$ positive choices for $n$, and $O(\kappa)$ geometric row points.  Across the two orientations this is
\[
 O(L^3/\kappa^2).                                                          \tag{3.31}
\]
Consequently
\[
 \#\{ab<0,\ \kappa_{\rm in}\ge K\}
 \ll L^3\sum_{\kappa\ge K}\kappa^{-2}\ll {L^3\over K}.                 \tag{3.32}
\]
Putting $K=\delta L$ proves $O(\delta^{-1}L^2)$, with the full $\delta^{-1}$ dependence displayed.  Again $2\kappa\le r<L$, so the sector is empty for $\delta\ge1/2$.

## Joint primitive form and the enlarged bounded-h sector

The original gcd and inward cross gcd are not independent.  Consider the plus orientation.  From the active coprimality condition $(d',m')=1$ and $\kappa\mid m'$, equation $d'=\kappa u+2s$ gives
\[
 (\kappa,s)=1.                                                            \tag{3.33}
\]
Since $\kappa$ is odd,
\[
 g=(d,d')=(\kappa u,\kappa u+2s)=(\kappa u,s)=(u,s).                       \tag{3.34}
\]
Write
\[
 u=gU,\qquad s=gS,\qquad (U,S)=1.                                        \tag{3.35}
\]
As $(u,v)=1$, also $(U,v)=1$.  Equation (3.24) becomes
\[
 n=g(Sv-wU),\qquad h={n\over g}=Sv-wU>0.                                  \tag{3.36}
\]
Thus $g\mid n$ and $r=2\kappa gh$.  The full plus parametrization is
\[
 d=\kappa gU,\quad d'=g(\kappa U+2S),\quad
 m'=\kappa v,\quad m=\kappa v+2w,
\quad Sv-wU=h.                                                            \tag{3.37}
\]
In the minus orientation, the active condition $(d,m)=1$ gives the same (3.33)--(3.35), and
\[
 d'=\kappa gU,\quad d=g(\kappa U+2S),\quad
 m=\kappa v,\quad m'=\kappa v+2w,
\quad Uw-vS=h>0.                                                          \tag{3.38}
\]
Since $g$ is odd, the character in both cases is
\[
 (-1)^s=(-1)^S.                                                           \tag{3.39}
\]
The primitive solutions are $S=S_0+Ut, w=w_0+vt$; $U$ is odd, so (3.39) is $(-1)^{S_0+t}$.

For fixed $\kappa,g,h$, the size restrictions permit $O(L/(\kappa g))$ choices of $U$, $O(L/\kappa)$ choices of $v$, and $O(\kappa)$ values of $t$.  Hence the incidence capacity is
\[
 O\!\left({L^2\over\kappa g}\right)                                    \tag{3.40}
\]
for each $\kappa,g,h$.  Because $2\kappa gh<L$, summing (3.40) for $h\le H$ gives
\[
\begin{split}
 \#\{ab<0,h\le H\}
 &\ll L^2\sum_{h\le H}\sum_{\kappa g<L/(2h)}{1\over\kappa g}\\
 &\ll HL^2\log^2(2L),                                                    \tag{3.41}
\end{split}
\]
using the elementary double harmonic bound
\(
 \sum_{\kappa g\le Y}(\kappa g)^{-1}\ll\log^2(2Y)
\).
This proves (1.5).  It also shows directly that $g\ge\gamma L$ forces $h<1/(2\gamma)$, and $\kappa\ge\delta L$ forces $h<1/(2\delta)$, although the direct counts (3.22) and (3.32) give the cleaner $\gamma^{-1}$ and $\delta^{-1}$ losses without an extra displayed logarithm.

Combining (3.11), (3.22), (3.32), and (3.41) proves the safe union bound (1.6) and the exact set complement (1.7).  The character, phase, selectors, and literal coefficients have not been discarded in obtaining the set identity; only the final capacity estimate of the whole safe union uses their absolute bounds.

## Exact fibre weight and failure of literal self-return

For the plus row in (3.25), define
\[
\begin{split}
 N_t&=\kappa u(\kappa v+2w_t),\\
 N_t+r&=(\kappa u+2s_t)\kappa v,
\end{split}
\qquad N_{t+1}-N_t=2\kappa uv.                                             \tag{3.42}
\]
Apart from the sign $(-1)^{s_0+t}$, its complete literal weight is
\[
\begin{split}
B_{\mathfrak f,+}^{\sigma}(t)={}&
 \left(1-{r\over R}\right)
 \mu^2(N_t)\mu^2(N_t+r)
 \rho_{N_t}(\kappa u)\rho_{N_t+r}(\kappa u+2s_t)\\
&\times A_{L,X}^{\sigma}(\kappa v,\kappa u+2s_t)
 \overline {A_{L,X}^{\sigma}(\kappa v+2w_t,\kappa u)}\\
&\times e\!\left({\sigma\sqrt X\,r\over\sqrt{N_t+r}+\sqrt{N_t}}\right),
                                                                            \tag{3.43}
\end{split}
\]
with all unshown literal predicates implemented by zero extension.  For the minus row,
\[
\begin{split}
 N_t&=(\kappa u+2s_t)\kappa v,\\
 N_t+r&=\kappa u(\kappa v+2w_t),
\end{split}
\qquad N_{t+1}-N_t=2\kappa uv,                                             \tag{3.44}
\]
and
\[
\begin{split}
B_{\mathfrak f,-}^{\sigma}(t)={}&
 \left(1-{r\over R}\right)
 \mu^2(N_t)\mu^2(N_t+r)
 \rho_{N_t}(\kappa u+2s_t)\rho_{N_t+r}(\kappa u)\\
&\times A_{L,X}^{\sigma}(\kappa v+2w_t,\kappa u)
 \overline {A_{L,X}^{\sigma}(\kappa v,\kappa u+2s_t)}\\
&\times e\!\left({\sigma\sqrt X\,r\over\sqrt{N_t+r}+\sqrt{N_t}}\right).
                                                                            \tag{3.45}
\end{split}
\]
Equations (3.43)--(3.45) retain both orientations and $\sigma$, and yield (2.11).

The geometric tangent map $t\mapsto t+1$ preserves $r$ and flips the character.  It does not preserve any of the following stated factors:

* $N_t$ and $N_t+r$ change by $2\kappa uv$, so their canonical selected pairs may change with no assumed relation;
* $\rho_{N_t}$ and $\rho_{N_t+r}$ may therefore delete either member of an adjacent pair;
* squarefreeness and the two allocation coprimalities may hold at one $t$ and fail at $t+1$;
* the two literal $A$-values, profiles, floors, hard samples, crossings, endpoints, and zero extensions have no stated translation law in $t$;
* the phase in (3.43) or (3.45) also varies with $t$.

Thus (3.26), (3.29), or (3.39) is only a bare character law.  For arbitrary bounded row weights,
\[
 \sup_{|B(t)|\le1}\left|\sum_{t\in I}(-1)^tB(t)\right|=|I|,                \tag{3.46}
\]
by choosing $B(t)=(-1)^t$; deleting one parity gives the same obstruction up to a factor two.  This is a coefficient-uniform no-go, not an assertion that the literal physical coefficient has large mass.

There is a second capacity obstruction.  Even granting an unjustified $O(1)$ estimate for each complete primitive $t$-row, the number of rows for fixed $\kappa,g,h$ is $O(L^2/(\kappa^2g))$.  Summing over $h<L/(2\kappa g)$ leaves the positive row-capacity bound
\[
 O\!\left(L^3\sum_{\kappa,g}{1\over\kappa^3g^2}\right)=O(L^3),            \tag{3.47}
\]
with the primitive corner $\kappa=g=1$ already allowing $O(L^3)$ row labels.  Therefore rowwise Abel summation or rowwise character pairing, followed by positive recombination, cannot by itself supply the required factor $L$.

# 4. First doubtful or unproved step

No step in the connector, algebra, parametrizations, exact complement, or capacity bounds above is left doubtful.  The first unproved step needed for the target is a genuinely global signed estimate on the exact unresolved set (1.7).

More explicitly, zero-extend (3.43) and (3.45) in $t$, and use the joint primitive labels $\mathfrak f=(\pm,\kappa,g,U,v,h,\text{residue class})$.  For every dyadic $Y\ge H$, the missing literal relation can be isolated as
\[
 \boxed{
 \Re\!\sum_{\substack{\mathfrak f:\ Y<h\le2Y\\
                  g<\gamma L,\ \kappa<\delta L}}
 (-1)^{S_{0,\mathfrak f}}
 \sum_{t\in\mathbb Z}(-1)^tB_{\mathfrak f}^{\sigma}(t)
 \ll L^2\mathcal X
 }                                                                         \tag{4.1}
\]
uniformly in $Y,L,X,\sigma$, with one real part outside the aggregate and with both orientations included.  Summing (4.1) over $O(\log L)$ dyadic $Y$'s would close the even-shift target (2.4).  Relative to the capacity $O(YL^2\mathcal X)$ of such a block, (4.1) demands a factor $Y$ of global cancellation.

Equivalently, a proof could derive a global weighted self-return/even-odd balance for the actual $B_{\mathfrak f}^{\sigma}$, but it must couple row labels as well as adjacent $t$'s.  Neither (B185.3), (B185.5), the residual truth table, nor the bare character identity implies (4.1).  In particular, (3.6) rules out the most immediate same-$N$ residual-pair self-return inside the hard shell, and (3.47) rules out stopping after a positive sum of rowwise estimates.  This is the first open relation; assuming it would merely rename the remaining problem.

# 5. Required control test and outcome

1. **Odd-$R$ endpoint control: passed.**  At $R=3$, $h_0=2,h_1=1$, and (1.1) is
   \[
   \mathfrak E_3\le2D_L+{4\over3}\Re K_2.
   \]
   The $r=2=R-1$ term is present.  At $R=5$, the $r=4$ term is present with coefficient $4/5$.  These are the terminal terms that would disappear under the erroneous cutoff $q<h_1$.

2. **Both-orientation algebra control: passed.**  Direct substitution in (2.7) gives $r=2\kappa(sv-wu)$, while substitution in (2.9) gives $r=2\kappa(wu-sv)$.  Replacing $(s,w)$ by $(s+u,w+v)$ leaves both determinants unchanged.  Since $u$ is odd, it flips $(-1)^s$ in both orientations.

3. **Arithmetic-deletion control: alternation does not survive.**  Take the plus parameters
   \[
   \kappa=101,\quad u=7,\quad v=1,\quad s_0=8,\quad w_0=1.
   \]
   At $t=0$,
   \[
   (d,d',m',m)=(707,723,101,103),\qquad d'm'-dm=202.
   \]
   Here $707=7\cdot101$, $723=3\cdot241$, and both products are squarefree with the required allocation coprimalities; both ratios lie in $(4,16)$.  At $t=1$,
   \[
   (d,d',m',m)=(707,737,101,105),\qquad d'm'-dm=202,
   \]
   and both ratios still lie in $(4,16)$, but $(707,105)=7$, so the lower product is not squarefree and the literal term is deleted.  The bare characters are $+1=(-1)^8$ and $-1=(-1)^{15}$, exactly as predicted, but the adjacent literal weights do not form a cancelling pair.  Opaque predicates could only create further failures of return.

4. **Residual pair-move control: failed as a cancellation mechanism.**  Formula (3.6) shows that moving a selected pair $P=pq$ from one side of an allocation to the other multiplies $d/m$ by $P^2\ge225$.  Therefore the two opposite-character allocations in (3.5) cannot both lie in $4m<d<16m$.  This is an exact shell obstruction, not a numerical heuristic.

5. **Coefficient-uniform control: failed, with no physical lower-mass claim.**  On one abstract complete row, choosing $B(t)=(-1)^t$ turns the bare alternating sum into $|I|$.  At the sequence level, taking $z_N=1$ on $M\asymp L^2$ consecutive sites gives $D=M$ but
   \[
   \sum_{q}\left(1-{2q\over R}\right)K_{2q}\asymp MR\asymp L^3
   \]
   for $R\asymp L$.  These controls prove that boundedness, support, and the diagonal estimate do not yield the correlation estimate uniformly over coefficients.  They do not assert that this artificial sequence or row is realized by the fixed literal $A_{L,X}^{\sigma}$.

No computer algebra, numerical experiment, web source, or external theorem was used; all controls are exact finite algebra.

# 6. Dependencies and exact artifacts used

Only the following two artifacts were read or used:

* `protocol.md`;
* `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/blind_statement.md`.

No proof graph, active campaign, strategy file, prior round, kernel, source, sibling report, or conductor analysis was accessed.  The derivation depends only on the definitions and hypotheses (B185.1)--(B185.7), the accepted diagonal estimate (B185.5), elementary divisor/allocation bijections, elementary linear Diophantine parametrization, and finite counting.

# 7. Recommended state effect

**Retain the target as open; no promotion of (B185.8) or (B185.9).**  The exact Fejer/parity connector, multiplicity-one identities, residual shell obstruction, monotone $O(L^2)$ count, original-gcd and inward-cross-gcd capacity bounds with explicit $\gamma^{-1},\delta^{-1}$, joint identity $r=2\kappa gh$, bounded-$h$ capacity lemma, and exact complement (1.7) are suitable for seam review and possible promotion as auxiliary lemmas.  The next proof obligation should be the global literal dyadic relation (4.1), or a comparably strong signed mechanism coupling the unresolved row labels.  A rowwise Abel estimate, a positive recombination, or the bare alternating character alone should be rejected as insufficient.
