# M9--M2 hard-TOP \(t=1\) residual maximal-Fejer positive-transform obstruction

- Campaign: m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate
- Round: 172
- Role: conductor-selected proof kernel
- Starting graph SHA-256:
  c98f95b6b3500d0f48365af338e543f9a0f251b22062f3898df5f448d6b54853
- Terminal label: maximal_fejer_dyadic_character_poisson_no_go
- Allocation: 100% analytic/algebraic; 0% numerical experimentation

## 1. Exact scope and result

Let \(J=\sqrt X\), \(1\ll L\ll H\le J^{1/2}\),
\(R_0=\lceil L\rceil\), and \(M=M_L\asymp L^2\).  Retain the
complete literal residual coefficient

\[
 c_N^{\rm rem}
 =\sum_{\substack{d\mid N\\d\ {\rm odd}}}
   \chi_4(d)\lambda_N(d),
\tag{172.K1}
\]

including every selector, no-pair row, squarefree and coprimality mask,
complementary parity branch, profile, floor, star, crossing, endpoint
value, and zero-extension value.  On literal support
\(d,N/d\asymp L\) and \(|\lambda_N(d)|\ll X^\eta\) for arbitrarily
small \(\eta>0\); the number of divisor incidences is
\(O(L^2X^\eta)\).  Extend the coefficient by zero on an \(M\)-site
containing interval and put

\[
 z_N=c_N^{\rm rem}e(J\sqrt N),\qquad
 Z(\theta)=\sum_Nz_Ne(N\theta),\qquad
 D_L=\sum_N|z_N|^2\ll_\varepsilon L^2X^\varepsilon.
\tag{172.K2}
\]

The square root is evaluated only on positive literal support.  For

\[
 F_R(\theta)=\sum_{|r|<R}\left(1-\frac{|r|}{R}\right)e(r\theta),
 \qquad
 K_R^{(2)}(\theta)=\frac{F_R(\theta)+F_R(\theta+1/2)}2,
\]

define

\[
 \mathfrak E_R^{(2)}
 =\int_0^1|Z(\theta)|^2K_R^{(2)}(\theta)\,d\theta.
\tag{172.K3}
\]

The following facts are proved.

1. The even-parity Fejer identity, stopped integer-doubling telescope,
   one short correction, exact adjacent-scale tent, doubling-only Haar
   identity, and exact final non-doubling link all hold with full-line zero
   extension.  The first link is target-safe, but has no target-safe
   complement and is not an owner-complete sector.
2. A real cardinal interpolation gives an exact finite-support
   character--ordinary-Poisson transform at the common Fejer frequency.
   The character constant is \(i/2\), and the squared parity-averaged
   bandpass constant is \(1/8\).
3. All transformed terms containing an ordinary zero frequency are
   \(O_\varepsilon(L^3X^\varepsilon)\), but only after all signed odd
   character frequencies are recombined.  This is not a termwise
   \(k\)-estimate and is not the distinct Round-169 scalar zero mode.
4. The first unproved transformed object is the complete signed
   \(\ell,\ell'\ne0\) aggregate.  The zero physical diagonal is not a zero
   dual diagonal; its cancellation occurs only after the full dual,
   endpoint-cell, frequency-endpoint, and zero-extension assembly
   recombines.
5. Any continuation which, before proving a literal actual-symbol saving,
   replaces that signed assembly by a coefficient-uniform positive norm
   over dual modes, cardinal cells, arithmetic openings, or common
   frequency has available maximal-link scale
   \(MD_L\ll_\varepsilon L^4X^\varepsilon\), not the target
   \(L^3X^\varepsilon\); the diagnostic family below is sharp at order
   \(L^4\).  Both centred Fejer peaks also return to the rank-one product
   collar.

This is a route-scoped obstruction.  It does not prove or disprove the
open maximal residual aggregate (165.K26).

## 2. Parity, chain, tent, Haar, and endpoint ledger

Put

\[
 C_r=\sum_Nz_{N+r}\overline{z_N},\qquad A_r=\Re C_r.
\]

The translation by \(1/2\) multiplies the \(r\)-th Fejer coefficient by
\((-1)^r\).  Therefore

\[
 \boxed{
 \mathfrak E_R^{(2)}
 =D_L+2\!\sum_{\substack{0<r<R\\2\mid r}}
 \left(1-\frac rR\right)A_r.}
\tag{172.K4}
\]

This retains both absolute site parities and removes only odd gaps.  For
the stopped chain \(R_{j+1}=\min(2R_j,M)\), with repetitions removed and
\(R_K=M\),

\[
 \boxed{
 T_{26}
 =\frac12\sum_{j<K}
 \left(\mathfrak E_{R_{j+1}}^{(2)}
       -\mathfrak E_{R_j}^{(2)}\right)-B_{\rm short},}
\tag{172.K5}
\]

where

\[
 B_{\rm short}
 =\sum_{\substack{0<r<R_0\\2\mid r}}
 r\left(\frac1{R_0}-\frac1M\right)A_r,
 \qquad
 |B_{\rm short}|\le R_0D_L
 \ll_\varepsilon L^3X^\varepsilon.
\tag{172.K6}
\]

The correction is paid once.  For every integer \(R<S\le2R\), direct
subtraction of the Fejer coefficients gives

\[
 b_{R,S}(r)=
 \begin{cases}
 r(S-R)/(RS),&0<r<R,\\
 1-r/S,&R\le r<S,\\
 0,&r\ge S,
 \end{cases}
 \qquad b_{R,S}(0)=0,
\tag{172.K7}
\]

and

\[
 \mathfrak E_S^{(2)}-\mathfrak E_R^{(2)}
 =2\!\sum_{\substack{r>0\\2\mid r}}b_{R,S}(r)A_r.
\tag{172.K8}
\]

At \(S=2R\), (172.K7) is the triangular tent

\[
 b_{R,2R}(r)=
 \begin{cases}
 r/(2R),&0<r<R,\\
 1-r/(2R),&R\le r<2R,\\
 0,&r\ge2R.
 \end{cases}
\tag{172.K9}
\]

For

\[
 Y_{s,R}^{(\epsilon)}
 =\sum_{\substack{0\le j<R\\s+j\equiv\epsilon\pmod2}}z_{s+j},
\]

full-line pair counting gives

\[
 \mathfrak E_R^{(2)}
 =\frac1R\sum_{s,\epsilon}|Y_{s,R}^{(\epsilon)}|^2.
\]

Thus, with

\[
 \mathfrak H_R^{(2)}
 =\frac1{2R}\sum_{s,\epsilon}
 |Y_{s,R}^{(\epsilon)}-Y_{s+R,R}^{(\epsilon)}|^2,
\]

the parallelogram identity yields

\[
 \boxed{
 \mathfrak E_{2R}^{(2)}
 =2\mathfrak E_R^{(2)}-\mathfrak H_R^{(2)}.}
\tag{172.K10}
\]

Absolute site parity is essential when \(R\) is odd.  Formula (172.K10)
is used only at exact doublings; a strict terminal \(R<S<2R\) uses
(172.K7).

Finally,

\[
 \sum_{r=1}^{S-1}b_{R,S}(r)=\frac{S-R}{2}.
\]

Consequently, for \(S=\min(2R_0,M)\),

\[
 |\mathfrak E_S^{(2)}-\mathfrak E_{R_0}^{(2)}|
 \le(S-R_0)D_L
 \ll_\varepsilon L^3X^\varepsilon.
\tag{172.K11}
\]

This includes a terminal first link.  It supplies no estimate for the
remaining links.

## 3. Exact common-frequency finite transform

For \(\epsilon\in\{0,1\}\), let

\[
 Z_\epsilon(\theta)
 =\sum_N(-1)^{\epsilon N}z_Ne(N\theta).
\]

Because \(d\) is odd in (172.K1),
\((-1)^{\epsilon N}=(-1)^{\epsilon m}\) when \(N=dm\); both
\(m\)-parity branches remain.  Choose a real-valued
\(\varphi\in C_c^\infty((-1/2,1/2))\) with \(\varphi(0)=1\), and define

\[
 \mathcal W_\epsilon(x,y)
 =\sum_{\substack{d,m\ge1\\d\ {\rm odd}}}
 (-1)^{\epsilon m}\lambda_{dm}(d)
 \varphi(x-d)\varphi(y-m),
\]

\[
 \mathcal B_{\epsilon,\theta}(x,y)
 =\mathcal W_\epsilon(x,y)e(J\sqrt{xy}+\theta xy).
\tag{172.K12}
\]

Every compact cell lies in \(x,y\asymp L>0\).  Since the bump support is
strictly shorter than one lattice cell,
\(\mathcal W_\epsilon(a,b)\) at an integer pair is exactly the literal
coefficient assigned to \((a,b)\), or zero.  The physical divisor
incidence \((d,m=N/d)\) has multiplicity one.  This statement is not
transferred to a later overlapping Möbius inclusion--exclusion opening.

With

\[
 \widetilde{\mathcal B}(\xi,\nu)
 =\iint_{\mathbb R^2}\mathcal B(x,y)e(-\xi x-\nu y)\,dx\,dy,
\]

ordinary Poisson and

\[
 \chi_4(n)=\frac{e(n/4)-e(-n/4)}{2i}
\]

give the exact character identity

\[
 \boxed{
 Z_\epsilon(\theta)
 =\frac i2
 \sum_{\substack{k\in\mathbb Z\\k\ {\rm odd}}}\chi_4(k)
 \sum_{\ell\in\mathbb Z}
 \widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell).}
\tag{172.K13}
\]

The finite smooth interpolation makes the dual sums rapidly convergent;
there is no omitted character-zero mode or ordinary scaling constant.
For \(B_{R,S}=F_S-F_R\), put

\[
 U_{k,\ell}^{(\epsilon)}(\theta)
 =\widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell).
\]

Since

\[
 \mathfrak E_S^{(2)}-\mathfrak E_R^{(2)}
 =\frac12\sum_{\epsilon=0}^1
 \int_0^1B_{R,S}(\theta)|Z_\epsilon(\theta)|^2\,d\theta,
\]

(172.K13) gives

\[
 \boxed{\begin{aligned}
 \mathfrak E_S^{(2)}-\mathfrak E_R^{(2)}
 =\frac18\Re\sum_{\epsilon=0}^1
 &\sum_{\substack{k,k'\ {\rm odd}\\
                    \ell,\ell'\in\mathbb Z}}
 \chi_4(k)\chi_4(k')\\
 &\times\int_0^1B_{R,S}(\theta)
 U_{k,\ell}^{(\epsilon)}(\theta)
 \overline{U_{k',\ell'}^{(\epsilon)}(\theta)}\,d\theta .
 \end{aligned}}
\tag{172.K14}
\]

The factor \(1/8\) is the parity average \(1/2\) times
\(|i/2|^2=1/4\).  There is one outer real part and no intervening
modulus.

## 4. Physical diagonal, dual diagonal, and ordinary zero modes

Extend \(b_{R,S}\) from (172.K7) evenly to negative integers and retain
\(b_{R,S}(0)=0\).  The continuous product-difference bandpass kernel is

\[
 \mathscr B_{R,S}(t)
 =\int_0^1B_{R,S}(\theta)e(t\theta)\,d\theta
 =\sum_{h\in\mathbb Z}b_{R,S}(h)I(t+h),
\quad
 I(u)=\int_0^1e(u\theta)\,d\theta.
\tag{172.K15}
\]

For an integer \(n\), it equals \(b_{R,S}(n)\), so the physical diagonal
has coefficient \(b_{R,S}(0)=0\).  For noninteger \(t\),

\[
 \mathscr B_{R,S}(t)
 =\frac{(e(t)-1)(S-R)}{2\pi it}
 -\frac1{2\pi it}\int_0^1
 B'_{R,S}(\theta)e(t\theta)\,d\theta,
\tag{172.K16}
\]

because \(B_{R,S}(0)=B_{R,S}(1)=S-R\).  It is not a compact tent.
On the nominal dual diagonal
\((k,\ell)=(k',\ell')\), the two cardinal integrations still have
independent variables, so \(t=xy-x'y'\) is generally noninteger and
nonzero.  The physical diagonal is recovered only after the entire dual
diagonal, dual off-diagonal, cell, endpoint, transition, and
zero-extension assembly recombines.

Define the fully character-recombined ordinary zero component by

\[
 Z_{\epsilon,0}(\theta)
 =\frac i2\sum_{k\ {\rm odd}}\chi_4(k)
 U_{k,0}^{(\epsilon)}(\theta).
\]

Applying the exact character identity in reverse gives

\[
 Z_{\epsilon,0}(\theta)
 =\sum_d\chi_4(d)\int_{\mathbb R}
 \mathcal B_{\epsilon,\theta}(d,y)\,dy.
\tag{172.K17}
\]

On every supported cell,

\[
 \partial_y(J\sqrt{dy}+\theta dy)
 =\frac J2\sqrt{d/y}+\theta d\asymp J
 \qquad(0\le\theta\le1),
\]

and the derivative of this quantity is \(O(J/L)\).  One cellwise
integration by parts has no cell-boundary term and costs \(O(J^{-1})\).
There are \(O(L^2X^\eta)\) literal incidences, so

\[
 \sup_{\epsilon,\theta}|Z_{\epsilon,0}(\theta)|
 \ll_\eta \frac{L^2}{J}X^\eta.
\tag{172.K18}
\]

Writing \(Z_\epsilon=Z_{\epsilon,0}+Z_{\epsilon,*}\), the complete part
of (172.K14) with \(\ell=0\) or \(\ell'=0\) is the expansion of

\[
 |Z_{\epsilon,0}|^2+
 2\Re(Z_{\epsilon,0}\overline{Z_{\epsilon,*}}).
\]

Since \(|B_{R,S}|\le R+S\),
\(\|Z_\epsilon\|_2=D_L^{1/2}\), and
\(\|Z_{\epsilon,0}\|_2\le\sup|Z_{\epsilon,0}|\), this complete sector is

\[
 \ll (R+S)
 \left(D_L^{1/2}\frac{L^2}{J}
       +\frac{L^4}{J^2}\right)X^{O(\eta)}
 \ll_\varepsilon L^3X^\varepsilon,
\tag{172.K19}
\]

using \(R+S\ll L^2\), \(L^2\le J\), and \(\eta>0\) chosen sufficiently
small in terms of the requested \(\varepsilon\).  This proof is collective
in the odd \(k\)-modes;
it licenses no termwise zero-mode bound.

## 5. First open signed aggregate

After (172.K19), the remaining part of one link is exactly

\[
 \boxed{\begin{aligned}
 \mathcal N_{R,S}
 =\frac18\Re\sum_{\epsilon=0}^1
 &\sum_{\substack{k,k'\ {\rm odd}\\
                    \ell,\ell'\ne0}}
 \chi_4(k)\chi_4(k')\\
 &\times\int_0^1B_{R,S}(\theta)
 U_{k,\ell}^{(\epsilon)}(\theta)
 \overline{U_{k',\ell'}^{(\epsilon)}(\theta)}\,d\theta .
 \end{aligned}}
\tag{172.K20}
\]

No dual diagonal can be deleted, and no modulus over \(k,k'\),
\(\ell,\ell'\), cardinal cells, arithmetic openings, endpoints, or
frequency may be taken before a new actual-symbol saving is proved.

A uniform linkwise estimate
\(\mathcal N_{R,S}\ll_\varepsilon L^3X^\varepsilon\), with epsilon
rebudgeting over the \(O(\log L)\) links, would suffice for (165.K26).
It is stronger than logically necessary: the frozen target also permits
cancellation among the signed link contributions in (172.K5).  Neither
the linkwise theorem nor the complete stopped-chain signed estimate is
proved here.

## 6. Sharp positive capacity and collar return

Fejer positivity and \(\|Z\|_2^2=D_L\) give

\[
 0\le\mathfrak E_R^{(2)}\le RD_L,\qquad
 |\mathfrak E_S^{(2)}-\mathfrak E_R^{(2)}|
 \le(R+S)D_L.
\tag{172.K21}
\]

At a maximal link this is
\(\ll_\varepsilon L^4X^\varepsilon\).  This available scale is sharp at
order \(L^4\) for the coefficient-uniform interface.  Take \(M=4P\), put
\(z_N=1\) on the \(2P\) even sites of an \(M\)-site interval, and use the
link \(2P\to4P\).  Then
\(D_L=2P\), \(A_{2s}=2P-s\), and direct summation of (172.K9) gives

\[
 \boxed{
 \mathfrak E_{4P}^{(2)}-\mathfrak E_{2P}^{(2)}
 =P^2=\frac18MD_L.}
\tag{172.K22}
\]

A positive translation makes the support lawful for the square root, and
the diagnostic coefficient \(c_N=e(-J\sqrt N)\) dechirps the phase.
Taking, for example, a power-of-two scale subfamily with \(M=L^2\) makes
\(M/2\to M\) a stopped-chain link.  The admissible choice
\(X=L^8\), \(J=L^4\), \(H=L^2\) then shows that for any fixed
\(0<\varepsilon_0<1/8\),

\[
 \frac{L^4}{L^3X^{\varepsilon_0}}
 =L^{1-8\varepsilon_0}\longrightarrow\infty.
\tag{172.K23}
\]

Thus support, \(D_L\), Parseval, Haar positivity, or a
coefficient-uniform positive transformed norm cannot supply the missing
factor \(L\).  This diagnostic sequence is not the literal residual
coefficient and proves no physical lower bound.  Conversely, a one-site
sequence has every bandpass increment exactly zero, so a positive
transformed diagonal surviving in isolation is missing compensating dual
or boundary pieces.  Positive-character no-pair rows likewise rule out
an assumed termwise character saving.

After centring either Fejer peak and moving the exact second-peak factor
\((-1)^N=(-1)^m\) into the amplitude, the smooth product phase is

\[
 \Phi_\phi(u,v)=J\sqrt{uv}+\phi uv-\xi u-\eta v,
\]

with

\[
 \det\operatorname{Hess}\Phi_\phi
 =-\phi^2-\frac{J\phi}{2\sqrt{uv}}.
\tag{172.K24}
\]

It is rank one at \(\phi=0\) for both centred peaks.  The bandpass has
maximal-scale height on reciprocal-scale arcs around those centres, so
deleting the centre or claiming uniform nondegenerate stationary phase is
not licensed.  On a centred smooth-interior cell with one fixed lawful
arithmetic opening, positive simultaneous dualization returns to the
accepted product-collar geometry and restores, rather than saves, its
available power.  This statement is not an identity or estimate for the
full cardinal family, noncentral arcs, hard endpoints, or transition
pieces; all of those remain inside the open signed aggregate (172.K20).

Equations (172.K21)--(172.K24) prove a no-go only for a continuation that
uses coefficient-uniform positivity before an actual-symbol gain.  They
do not exclude a new positive theorem that first proves a special property
of the literal coefficient, or a genuinely signed treatment of
(172.K20).

## 7. Power and owner boundary

The exact ledger is

| object | proved bound or available capacity | target |
|---|---:|---:|
| one short correction | \(L^3X^\varepsilon\) | \(L^3X^\varepsilon\) |
| first stopped-chain link | \(L^3X^\varepsilon\) | \(L^3X^\varepsilon\) |
| fully recombined ordinary-zero-containing sector | \(L^3X^\varepsilon\) | \(L^3X^\varepsilon\) |
| signed nonzero ordinary-frequency aggregate | open | \(L^3X^\varepsilon\) |
| maximal coefficient-uniform positive closure | \(\ll L^4X^\varepsilon\), sharp at order \(L^4\) on the diagnostic family | \(L^3X^\varepsilon\) |

The first-link and ordinary-zero statements are auxiliary pieces of the
same reduction; neither has an owner-complete complement, so neither is a
standalone proof-graph owner.

The kernel licenses one proved-internal, residual-only obstruction node:

M9-M2-hard-top-t1-residual-maximal-fejer-dyadic-positive-transform-obstruction.

It has no implication edge.  The maximal aggregate (165.K26), the complete
residual \(t=1\) scalar, all other \(t=1\) and hard-TOP channels, full hard
TOP, BAL, UNBAL, M9--M2, direct M1, GAR, endpoint assembly, M9, both
bridges, and the quarter theorem remain open.  The internal exponent
remains \(1/3\), the accepted repaired external Li--Yang benchmark remains
\(0.3144831759740614\ldots\), and the target remains \(1/4\).

## 8. Dependencies and evidence

Accepted dependencies:

- M9-M2-hard-top-t1-residual-fejer-parity-gcd-scale-reduction; and
- M9-M2-hard-top-t1-character-poisson-product-collar-obstruction.

Round-172 evidence consists of the repaired literal discovery, statement-
only blind rederivation, repaired hostile audit, independent parity,
transform, and power/owner reviews, both post-repair verifications, the
formalized candidate, and the conductor controls and adjudication.  No
numerical experiment or external theorem is used.
