# Conductor candidate: K17a cross-gcd alternating-fibre reduction

## 1. Exact statement

Assume

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,\qquad 0<\gamma<1,
\tag{176.C1}
\]

and put

\[
 R_{\log}=\min\{R_0-1,\lfloor(\log X)^{100}\rfloor\}.
\tag{176.C2}
\]

Retain the complete literal residual atom

\[
 u_L(d,m)=\chi_4(d)\lambda_{dm}(d)e(J\sqrt{dm}),
\tag{176.C3}
\]

where \(\lambda\) includes the supported squarefree row, normalization,
the canonical neither/both or no-pair selector, both parity branches,
profiles, floors, stars, hard values, endpoints, and full-line zero
extension.  On nonzero atoms, \(d,m\asymp L\) and
\(|\lambda_{dm}(d)|\ll1\).

Consider the non-polylogarithmic K17a aggregate with one real part outside
all incidences,

\[
 R_{\log}<r<R_0,\qquad 2\mid r,\qquad
 (d'-d)(m'-m)<0,\qquad (d,d')<\gamma L.
\tag{176.C4}
\]

Define the orientation-dependent inward cross gcd on this disjoint union by

\[
 \kappa_*=
 \begin{cases}
  (d,m'),&d'>d,\ m'<m,\\
  (d',m),&d'<d,\ m'>m.
 \end{cases}
\tag{176.C4a}
\]

The following statements hold.

1. In the orientation \(d'=d+2s>d\), \(m=m'+2w>m'\), define

   \[
   \kappa=\kappa_*=(d,m'),\qquad d=\kappa u,\qquad m'=\kappa v,
   \qquad (u,v)=1.
   \tag{176.C5}
   \]

   Then \(\kappa,u\) are odd and there is a positive integer \(n\) with

   \[
   r=2\kappa n,\qquad sv-wu=n.
   \tag{176.C6}
   \]

   With \(\bar v v\equiv1\pmod u\), choose

   \[
   s_0=[\bar v n]_u,\qquad w_0={s_0v-n\over u}.
   \tag{176.C7}
   \]

   For \(u=1\), use the harmless convention \(s_0=0\) and interpret the
   residue and Fourier group modulo one.

   Every parity-compatible incidence in this orientation occurs exactly
   once as

   \[
   s=s_0+ut,\qquad w=w_0+vt,
   \tag{176.C8}
   \]

   with literal validity enforced by the zero-extended endpoint
   coefficients.  Both endpoint products advance by

   \[
   K_\kappa=2\kappa uv,
   \tag{176.C9}
   \]

   and the character is

   \[
   \chi_4(d')\chi_4(d)=E_u(\bar v n)(-1)^t,
   \qquad E_u(a)=(-1)^{[a]_u}.
   \tag{176.C10}
   \]

   The opposite orientation \(d=d'+2s>d'\), \(m'=m+2w>m\) has the
   same conclusions with \(\kappa=\kappa_*=(d',m)\), \(d'=\kappa u\),
   \(m=\kappa v\), \(uw-sv=n\), and anchor
   \(E_u(-\bar v n)\).  The two parametrizations are disjoint and retain
   both original parity branches.

   More explicitly, in the plus orientation set

   \[
   \begin{aligned}
    N_t^+&=\kappa u(\kappa v+2w_t),\\
    N_t^++2\kappa n&=\kappa v(\kappa u+2s_t),\\
    \Psi^+_{\kappa,u,v,n}(t)
      &=J(\sqrt{N_t^++2\kappa n}-\sqrt{N_t^+}),
   \end{aligned}
   \tag{176.C10a}
   \]

   and define

   \[
   \begin{aligned}
   \Lambda^+_{\kappa,u,v,n}(t)={}&
    \left(1-{2\kappa n\over R_0}\right)
    \mathbf1_{R_{\log}<2\kappa n<R_0}
    \mathbf1_{(u,n)<\gamma L}
    \mathbf1_{s_t\ge1,w_t\ge1}\\
   &\times
    \lambda_{N_t^++2\kappa n}(\kappa u+2s_t)
    \overline{\lambda_{N_t^+}(\kappa u)}.
   \end{aligned}
   \tag{176.C10b}
   \]

   In the minus orientation use the canonical solution of
   \(uw-sv=n\), namely
   \(s_0=[-\bar v n]_u\), \(w_0=(n+s_0v)/u\), and put

   \[
   \begin{aligned}
    N_t^-&=\kappa v(\kappa u+2s_t),\\
    N_t^-+2\kappa n&=\kappa u(\kappa v+2w_t),\\
    \Psi^-_{\kappa,u,v,n}(t)
      &=J(\sqrt{N_t^-+2\kappa n}-\sqrt{N_t^-}),
   \end{aligned}
   \tag{176.C10c}
   \]

   \[
   \begin{aligned}
   \Lambda^-_{\kappa,u,v,n}(t)={}&
    \left(1-{2\kappa n\over R_0}\right)
    \mathbf1_{R_{\log}<2\kappa n<R_0}
    \mathbf1_{(u,n)<\gamma L}
    \mathbf1_{s_t\ge1,w_t\ge1}\\
   &\times
    \lambda_{N_t^-+2\kappa n}(\kappa u)
    \overline{\lambda_{N_t^-}(\kappa u+2s_t)}.
   \end{aligned}
   \tag{176.C10d}
   \]

   Every unlisted endpoint condition is retained by the zero extension of
   \(\lambda\), but the displacement inequalities
   \(s_t,w_t\ge1\) are imposed explicitly.  With all outer labels
   positive, \(\kappa,u\) odd, and \((u,v)=1\), the exact aggregate is

   \[
   \boxed{
   \Re\mathfrak C^{\rm rem}_{\rm K17a,nonpolylog}
   =\Re\!\left\{
    \sum_{\kappa,u,v,n}\sum_{t\in\mathbb Z}
     E_u(\bar v n)(-1)^t\Lambda^+_{\kappa,u,v,n}(t)e(\Psi^+(t))
   +\sum_{\kappa,u,v,n}\sum_{t\in\mathbb Z}
     E_u(-\bar v n)(-1)^t\Lambda^-_{\kappa,u,v,n}(t)e(\Psi^-(t))
   \right\}.}
   \tag{176.C10e}
   \]

   Here \(\Psi^\pm(t)\) abbreviates the fully indexed phases above.
   Thus the Fejer weight, conjugations, determinant range, original-gcd
   cutoff, two orientations, and single outer real part are simultaneous
   in one identity.

2. On every nonzero literal atom, the original divisor gcd is constant on
   the cross-gcd fibre and equals

   \[
   \boxed{(d,d')=(u,n)=(u,r/(2\kappa_*)).}
   \tag{176.C11}
   \]

   Thus the original low-gcd cutoff is not a source of fibre variation and
   must not be confused with \(\kappa_*\).

3. For every odd modulus \(m\), the sawtooth has the exact discrete Fourier
   expansion

   \[
   \widehat E_m(k)=\sum_{a\bmod m}E_m(a)e(-ka/m)
   ={2\over1+e(-k/m)}
   ={e(k/(2m))\over\cos(\pi k/m)},
   \tag{176.C12}
   \]

   \[
   E_m(a)={1\over m}\sum_{k\bmod m}\widehat E_m(k)e(ka/m),
   \qquad
   {1\over m}\sum_{k\bmod m}|\widehat E_m(k)|\ll\log(2m).
   \tag{176.C13}
   \]

   If \(g=(u,n)\), \(u=gu_0\), and \(n=gn_0\), then the exact
   primitive form of the cross anchor is

   \[
   E_u(\pm\bar v n)=E_{u_0}(\pm\bar v n_0),
   \qquad u_0={u\over(u,n)}.
   \tag{176.C13a}
   \]

   For \(c_m(k)=\widehat E_m(k)/m\), Parseval and the near-half
   coefficient give \(\|c_m\|_2=1\) and
   \(\|c_m\|_\infty\asymp1\).

   This removes the canonical sawtooth at logarithmic algebra norm, but it
   creates incomplete inverse-residue phases
   \(e(\pm k\bar v n/u)\) in the fixed-\(u\), nonminimal expansion, or
   the corresponding primitive-modulus phases from (176.C13a).  The
   near-half mode has \(|\widehat E_m((m-1)/2)|\asymp m\), so it cannot
   be discarded.

4. For every fixed \(0<\delta<1/2\), independently of
   \(X,L,H,J\), the complete literal strict sector

   \[
   \boxed{
   \left|\mathfrak C^{\rm rem}_{R_{\log}<r<R_0,2,{\rm opp},
       (d,d')<\gamma L,\ \kappa_*\ge\delta L}\right|
   \ll_{\delta,\gamma,\varepsilon}L^2X^\varepsilon.}
   \tag{176.C14}
   \]

   This includes both orientations and every literal selector, endpoint,
   Fejer weight, and squarefree restriction.  For fixed
   \(\delta\ge1/2\), the sector is eventually empty apart from an
   immaterial ceiling edge, because \(r=2\kappa_*n<R_0\).  In the stated
   nonvacuous range its exact complement is \(\kappa_*<\delta L\).  If
   \(\delta\) shrinks with \(L\), the proved ledger costs
   \(\delta^{-1}\) and is not a target-scale theorem.

5. The identities above do not prove the full K17a target.  On a full
   fixed-relative fibre the physical length and phase parameter are

   \[
   T\asymp\kappa,\qquad F\asymp{2Jn\kappa\over L},\qquad
   {F\over T^2}\asymp{2Jn\over\kappa L}\gg1.
   \tag{176.C15}
   \]

   Rowwise Abel without selector variation control, rowwise second
   derivative or B-process, and rowwise Poisson followed by absolute dual
   summation return the trivial \(O(\kappa)\) row capacity.  A positive
   sum over rows therefore gives \(O(L^3X^\varepsilon)\); even one
   optimistic square-root saving in the inverse-residue variable leaves
   \(O(L^{5/2}X^\varepsilon)\).  Likewise, full two-variable Poisson
   followed by positive dual recombination returns the physical
   \(O(L^3X^\varepsilon)\) capacity.  This is a route-scoped

   \[
   \boxed{\texttt{k17a\_cross\_gcd\_alternating\_fibre\_capacity\_or\_self\_return\_no\_go}.}
   \tag{176.C16}
   \]

   It is not a lower bound for the literal aggregate and does not exclude
   a selector-aware signed joint inverse-residue or dual theorem.

## 2. Multiplicity, character, and the two gcds

For the first orientation,

\[
 d'm'-dm=(d+2s)m'-d(m'+2w)
 =2\kappa(sv-wu).
\tag{176.C17}
\]

Since \((u,v)=1\), the solutions to \(sv-wu=n\) are exactly
(176.C8); changing the base solution only translates \(t\).  Conversely,
the orientation, inward gcd, primitive pair, determinant, and \(t\)
reconstruct one ordered incidence.  This proves multiplicity one.  The
opposite orientation is identical after using
\(d'm'-dm=2\kappa(uw-sv)\).

Because both divisors are odd, \(\kappa\) and \(u\) are odd.  Hence

\[
 \chi_4(\kappa u+2s)\chi_4(\kappa u)=(-1)^s,
\tag{176.C18}
\]

and (176.C8) gives (176.C10).  Substitution in the two endpoint products
gives the common increment (176.C9).

For a nonzero plus-orientation atom, squarefreeness of
\((\kappa u+2s)\kappa v\) gives \((\kappa,s)=1\).  Therefore

\[
 (d,d')=(\kappa u,\kappa u+2s)
 =(\kappa u,s)=(u,s)=(u,sv-wu)=(u,n).
\tag{176.C19}
\]

The lower product in the opposite orientation gives the same coprimality,
and \(uw-sv=n\) gives the same final gcd.  This proves (176.C11).

The two-adic ledger is also fibre-stable.  In the odd-product branch,
\(v\) is odd.  In the even-even squarefree branch,
\(v=2v_1\) with \(v_1\) odd; both products are \(2\pmod4\), so
\(4\mid r\) and \(n\) is even.  Either primitive equation then forces
\(w\) even.  Since \(w_t=w_0+vt\), this parity remains fixed, while
\(s_t=s_0+ut\) changes parity at every step because \(u\) is odd.
After separating the factor two, every squarefree Möbius opening has odd
progression modulus and therefore preserves the half-frequency.

These coordinates agree exactly with the statement-only rederivation.
If that rederivation writes

\[
 g=(d,d'),\quad d_{\rm lo}=ga,\quad d_{\rm hi}=g(a+2k),
 \quad m_{\rm lo}=m_0,\quad m_{\rm hi}=m_0+2w,
\tag{176.C20}
\]

and \(K=km_0-aw\), then in the plus orientation

\[
 g=(u,n),\quad a={\kappa u\over g},\quad k={s\over g},
 \quad m_0=\kappa v,\quad K={\kappa n\over g},
 \quad (a,m_0)=\kappa.
\tag{176.C21}
\]

Consequently its translation step
\(2gam_0/(a,m_0)\) is exactly \(2\kappa uv\), and its character law
\((-1)^{k_0+t}\) is the same half-frequency in different coordinates.

## 3. Fourier anchor and strict-sector count

The geometric series with ratio \(-e(-k/m)\) proves

\[
 \widehat E_m(k)
 ={1-(-e(-k/m))^m\over1+e(-k/m)}
 ={2\over1+e(-k/m)},
\tag{176.C22}
\]

because \(m\) is odd.  Summing the reciprocal cosine around the unique
near-half pair proves (176.C13).  At \(k=(m-1)/2\), the denominator is
\(\sin(\pi/(2m))\), which proves the large-alias assertion.  For
(176.C13a), the congruence \(sv\equiv n\pmod u\) forces
\(s_0=gs_0'\), where
\(s_0'=[\bar v n_0]_{u_0}\).  Since \(g=(u,n)\) is odd on literal
support, \((-1)^{s_0}=(-1)^{s_0'}\), proving the primitive identity.

For the strict-sector count, fix \(\kappa\) and put \(Y=L/\kappa\).
The inward cross product is smaller than both opposing endpoint products,
so

\[
 \kappa^2uv\ll L^2,
 \qquad uv\ll Y^2,
 \qquad n\ll Y.
\tag{176.C23}
\]

Both endpoint products advance by \(D=2\kappa uv\).  A product shell of
length \(O(L^2)\) therefore contains at most
\(O(1+L^2/(\kappa uv))\) sites of a fixed primitive row.  Consequently

\[
\begin{aligned}
 C_\kappa
 &\ll X^\varepsilon
 \sum_{uv\ll Y^2}\sum_{n\ll Y}
 \left(1+{L^2\over\kappa uv}\right)\\
 &\ll X^\varepsilon\left{
 Y^3\log(2Y)+{L^2Y\over\kappa}\log^2(2Y)\right}
 \ll {L^3\over\kappa^2}X^\varepsilon.
\end{aligned}
\tag{176.C24}
\]

Here logarithms are absorbed after choosing the auxiliary divisor-bound
exponent below the final \(\varepsilon\).  This hyperbola count is valid
even without using the stronger accepted atomwise support
\(d,m,d',m'\asymp L\).  On that actual support it reduces to the simpler
row ledger \(u,v\asymp L/\kappa\) and \(O(1+\kappa)\) sites.

Summing (176.C24) over \(\kappa\ge K\) gives
\(O(L^3K^{-1}X^\varepsilon)\).  Putting \(K=\delta L\) proves
(176.C14).  The estimate counts both
orientations separately; all squarefree, low-gcd, selector, profile,
endpoint, Fejer, and non-polylogarithmic restrictions only delete atoms or
multiply by \(O(X^\varepsilon)\).  Taking an absolute value outside the
complete sum also controls its outer real part.

## 4. Exact route obstruction and controls

Write \(x(t)=N_0+2\kappa uv\,t\), \(r=2\kappa n\), and absorb the
half-frequency into

\[
 \Phi(t)=J(\sqrt{x(t)+r}-\sqrt{x(t)})+{t\over2}.
\tag{176.C25}
\]

On a fixed-relative interior fibre,

\[
 \Phi''(t)\asymp {2Jn\over\kappa L},\qquad
 |\Phi'''(t)|\asymp {2Jn\over\kappa^2L}.
\tag{176.C26}
\]

The derivative image has length \(\asymp2Jn/L\).  Poisson therefore has
\(O(1+2Jn/L)\) stationary half-lattice modes, and one saddle has size
\((\kappa L/(2Jn))^{1/2}\).  Their absolute recombination gives the usual

\[
 \sqrt F+{T\over\sqrt F},
\tag{176.C27}
\]

which is \(\gg T\) at the power scale in the frozen range; taking the
minimum with the trivial bound therefore gives no power saving over
\(T\).  The half-frequency shifts
the dual lattice but does not reduce its density.  No modulo-one separation
or literal selector variation theorem is available.

On these fixed-relative cells the positive power ledger is

\[
 \sum_{\kappa\ge K}(L/\kappa)^3\kappa
 \ll L^3/K,
\tag{176.C28}
\]

whereas a hypothetical \(O(X^\varepsilon)\) row bound would give
\(L^3/K^2\).  At \(K=L^{1/2}\) these are respectively \(L^{5/2}\)
and \(L^2\).  Classical row transforms justify only the first.

The positively recombined full two-variable transform self-returns on the
same fixed-relative cells.  For fixed \(\kappa,u,v\), write

\[
 \Theta(s,w)=J\{\sqrt{\kappa v(\kappa u+2s)}
 -\sqrt{\kappa u(\kappa v+2w)}\}+{s\over2}.
\tag{176.C28a}
\]

Its Hessian is diagonal and has determinant
\(|\det\operatorname{Hess}\Theta|\asymp J^2/L^2\).  Because
\((u,v)=1\), determinant and fibre coordinates form an integral
unimodular change of variables.  The strip
\(n\ll L/\kappa\), \(t\ll\kappa\) has physical area \(O(L)\).
Thus its gradient image has volume \(O(J^2/L)\), while one
nondegenerate stationary coefficient has scale \(L/J\).  Taking all dual
modes absolutely has \(O(J)\) capacity, so the better of the transformed
and physical certificates is only \(O(L)\).  Finally

\[
 \sum_{\kappa\ll L}(L/\kappa)^2L\ll L^3.
\tag{176.C28b}
\]

The term \(s/2\) merely translates one dual coordinate.  This calculation
audits only smooth fixed-relative cells followed by termwise positive dual
summation; it neither executes Poisson on the discontinuous literal symbol
nor excludes signed cancellation between dual modes.

The anchor itself does not force determinant alternation.  For odd \(u\),
take \(v=(u+1)/2\), \(s=2n\), and \(w=n\).  Then
\(sv-wu=n\), \(\bar v=2\pmod u\), and
\(E_u(\bar v n)=+1\) for \(0<n<u/2\).  A fixed interior subinterval has
the correct opposing near-square geometry.  This is an exact character
control, but no literal squarefree-selector density or phase alignment is
claimed; it is not physical lower mass.

Odd squarefree-Möbius progressions preserve \((-1)^t\), but positive
recombination over their short and singleton pieces restores the row
capacity.  Arbitrary support masks and dechirped arrays likewise refute
coefficient-uniform estimates only; they are quarantined from the literal
coefficient.  These controls establish exactly the scope in (176.C16).

## 5. First open step

After (176.C12), a sufficient new local theorem would, for both
orientations, prove uniformly in \(\kappa,u,v\) and \(k\pmod u\) that

\[
 \sum_{n\ll L/\kappa}\ \sum_{t\in\mathbb Z}
 \Lambda^\pm_{\kappa,u,v,n}(t)
 e\!\left(\Psi^\pm_{\kappa,u,v,n}(t)+{t\over2}
          \pm{k\bar v n\over u}\right)
 \ll_\varepsilon \kappa X^\varepsilon,
\tag{176.C29}
\]

with \(\Lambda^\pm\) exactly as in (176.C10b) and (176.C10d), so the
non-polylogarithmic determinant range, low-gcd condition, displacement
positivity, squarefree rows, selected/no-pair field, both endpoints, Fejer
factor, hard values, and zero extension all remain inside the sum.  Then
(176.C13)
and

\[
 \sum_{\kappa\ll L}\kappa\,
 \#\{(u,v):uv\ll(L/\kappa)^2\}
 \ll L^2(\log(2L))^2
\tag{176.C30}
\]

would prove the full K17a target after absorbing the resulting logarithmic costs
by choosing the auxiliary \(\varepsilon\) below the final one.  No accepted theorem supplies
(176.C29).  In particular, the canonical selector has no proved bounded
variation or Fourier norm in \(n,t\), or \(\bar v\), and the large alias
mode must be estimated rather than omitted.

## 6. Scope and state recommendation

Promote the exact two-orientation parametrization, fibre-stable original
gcd, canonical-anchor Fourier identities, strict fixed-proportion
cross-gcd sector, and the explicitly scoped positive-recombination no-go as
one internal reduction.  Retain the complete non-polylogarithmic K17a
target and every parent open.

Reject only claims that fibrewise alternation, automatic determinant
alternation, Abel without a selector theorem, or positively recombined
row/joint transforms already supply the missing factor \(L\).  Do not
reject a signed joint inverse-residue theorem, cancellation between the two
orientations, or another literal coefficient-sensitive method.

Nothing here proves the complete residual scalar, another hard-TOP
channel, hard TOP, BAL, UNBAL, M9--M2, M9--M1/GAR, endpoint uniformity,
M9, either bridge, the quarter theorem, or a better global exponent.
