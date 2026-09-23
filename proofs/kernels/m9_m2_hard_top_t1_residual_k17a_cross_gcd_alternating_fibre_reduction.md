# Kernel: residual K17a cross-gcd alternating-fibre reduction

## Statement

Assume

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,\qquad 0<\gamma<1,
\tag{176.K1}
\]

and

\[
 R_{\log}=\min\{R_0-1,\lfloor(\log X)^{100}\rfloor\}.
\tag{176.K2}
\]

Retain the complete literal residual endpoint atom

\[
 u_L(d,m)=\chi_4(d)\lambda_{dm}(d)e(J\sqrt{dm}),
\tag{176.K3}
\]

where \(\lambda\) contains the supported squarefree row, normalization,
canonical neither/both or no-pair selector, both parity branches, profiles,
floors, stars, hard values, endpoints, and zero extension.  On nonzero
atoms, \(dm\asymp L^2\), \(d,m\asymp L\), and
\(|\lambda_{dm}(d)|\ll1\).

Consider the complete non-polylogarithmic K17a aggregate with one real
part outside all incidences:

\[
 R_{\log}<r<R_0,\qquad 2\mid r,\qquad
 (d'-d)(m'-m)<0,\qquad (d,d')<\gamma L.
\tag{176.K4}
\]

Define its orientation-dependent inward cross gcd by

\[
 \kappa_*=
 \begin{cases}
  (d,m'),&d'>d,\ m'<m,\\
  (d',m),&d'<d,\ m'>m.
 \end{cases}
\tag{176.K5}
\]

Then the following conclusions hold.

1. The two opposing orientations have exact, disjoint, multiplicity-one
   parametrizations.  In the plus orientation,

   \[
   d=\kappa u,\quad d'=\kappa u+2s,\quad
   m'=\kappa v,\quad m=\kappa v+2w,
   \quad \kappa=\kappa_*,
   \tag{176.K6}
   \]

   where \(\kappa,u\) are odd, \((u,v)=1\), and

   \[
   r=2\kappa n,\qquad sv-wu=n>0.
   \tag{176.K7}
   \]

   With \(s_0=[\bar v n]_u\),
   \(w_0=(s_0v-n)/u\), all solutions are

   \[
   s_t=s_0+ut,\qquad w_t=w_0+vt.
   \tag{176.K8}
   \]

   For \(u=1\), take \(s_0=0\).  Both endpoint products advance by
   \(2\kappa uv\), and

   \[
   \chi_4(d')\chi_4(d)=E_u(\bar v n)(-1)^t,
   \qquad E_u(a)=(-1)^{[a]_u}.
   \tag{176.K9}
   \]

   In the minus orientation,

   \[
   d'=\kappa u,\quad d=\kappa u+2s,\quad
   m=\kappa v,\quad m'=\kappa v+2w,
   \tag{176.K10}
   \]

   with \(uw-sv=n>0\), canonical
   \(s_0=[-\bar v n]_u\), \(w_0=(n+s_0v)/u\), the same solution step,
   common product increment, and character anchor
   \(E_u(-\bar v n)(-1)^t\).

2. On every nonzero literal atom, squarefreeness gives the fibre-stable
   original divisor gcd

   \[
   \boxed{(d,d')=(u,n)=(u,r/(2\kappa_*)).}
   \tag{176.K11}
   \]

   Thus the original low-gcd cutoff is not the cross gcd and does not vary
   along a fixed cross-gcd fibre.

3. For every odd modulus \(m\),

   \[
   \widehat E_m(k)=\sum_{a\bmod m}E_m(a)e(-ka/m)
   ={2\over1+e(-k/m)}
   ={e(k/(2m))\over\cos(\pi k/m)},
   \tag{176.K12}
   \]

   \[
   E_m(a)={1\over m}\sum_{k\bmod m}\widehat E_m(k)e(ka/m),
   \qquad
   {1\over m}\sum_{k\bmod m}|\widehat E_m(k)|\ll\log(2m).
   \tag{176.K13}
   \]

   If \(g=(u,n)\), \(u=gu_0\), and \(n=gn_0\), then the primitive
   cross-anchor identity is

   \[
   E_u(\pm\bar v n)=E_{u_0}(\pm\bar v n_0),
   \qquad u_0={u\over(u,n)}.
   \tag{176.K14}
   \]

   For \(c_m(k)=\widehat E_m(k)/m\), one has
   \(\|c_m\|_2=1\), \(\|c_m\|_\infty\asymp1\), and
   \(\|c_m\|_1\ll\log(2m)\).  Thus the canonical sawtooth has only
   logarithmic algebra cost but no power contraction.

4. For every fixed \(0<\delta<1/2\), independently of
   \(X,L,H,J\), the complete literal strict sector satisfies

   \[
   \boxed{
   \left|\mathfrak C^{\rm rem}_{R_{\log}<r<R_0,2,{\rm opp},
       (d,d')<\gamma L,\ \kappa_*\ge\delta L}\right|
   \ll_{\delta,\gamma,\varepsilon}L^2X^\varepsilon.}
   \tag{176.K15}
   \]

   Its exact complement is \(\kappa_*<\delta L\).  If \(\delta\)
   shrinks with \(L\), the proved bound costs \(\delta^{-1}\) and is
   not target-scale.

5. The half-frequency does not by itself prove the remaining K17a
   aggregate.  On full fixed-relative fibres, rowwise Abel without a
   selector theorem, rowwise derivative or B-process estimates, and
   rowwise Poisson followed by absolute dual-mode summation return the
   trivial row power.  Smooth-cell two-variable Poisson followed by
   positive dual recombination returns the physical \(L^3X^\varepsilon\)
   capacity.  Positive Möbius-progression recombination and one optimistic
   inverse-residue square-root saving also remain above target.  This is
   the route-scoped terminal conclusion

   \[
   \boxed{\texttt{k17a\_cross\_gcd\_alternating\_fibre\_capacity\_or\_self\_return\_no\_go}.}
   \tag{176.K16}
   \]

   It is not physical lower mass and does not exclude a selector-aware
   signed joint inverse-residue, signed dual, or two-orientation theorem.

## Exact two-orientation identity

For the plus orientation define

\[
\begin{aligned}
 N_t^+&=\kappa u(\kappa v+2w_t),\\
 N_t^++2\kappa n&=\kappa v(\kappa u+2s_t),\\
 \Psi^+(t)&=J(\sqrt{N_t^++2\kappa n}-\sqrt{N_t^+}),
\end{aligned}
\tag{176.K17}
\]

\[
\begin{aligned}
 \Lambda^+(t)={}&
 \left(1-{2\kappa n\over R_0}\right)
 \mathbf1_{R_{\log}<2\kappa n<R_0}
 \mathbf1_{(u,n)<\gamma L}
 \mathbf1_{s_t\ge1,w_t\ge1}\\
 &\times
 \lambda_{N_t^++2\kappa n}(\kappa u+2s_t)
 \overline{\lambda_{N_t^+}(\kappa u)}.
\end{aligned}
\tag{176.K18}
\]

For the minus orientation define

\[
\begin{aligned}
 N_t^-&=\kappa v(\kappa u+2s_t),\\
 N_t^-+2\kappa n&=\kappa u(\kappa v+2w_t),\\
 \Psi^-(t)&=J(\sqrt{N_t^-+2\kappa n}-\sqrt{N_t^-}),
\end{aligned}
\tag{176.K19}
\]

\[
\begin{aligned}
 \Lambda^-(t)={}&
 \left(1-{2\kappa n\over R_0}\right)
 \mathbf1_{R_{\log}<2\kappa n<R_0}
 \mathbf1_{(u,n)<\gamma L}
 \mathbf1_{s_t\ge1,w_t\ge1}\\
 &\times
 \lambda_{N_t^-+2\kappa n}(\kappa u)
 \overline{\lambda_{N_t^-}(\kappa u+2s_t)}.
\end{aligned}
\tag{176.K20}
\]

All other literal restrictions are enforced by zero extension.  With all
outer labels positive, \(\kappa,u\) odd, and \((u,v)=1\), the exact
identity is

\[
\boxed{
\begin{aligned}
 \Re\mathfrak C^{\rm rem}_{\rm K17a,nonpolylog}
 =\Re\Bigg\{&
 \sum_{\kappa,u,v,n}\sum_{t\in\mathbb Z}
 E_u(\bar v n)(-1)^t\Lambda^+(t)e(\Psi^+(t))\\
 &+\sum_{\kappa,u,v,n}\sum_{t\in\mathbb Z}
 E_u(-\bar v n)(-1)^t\Lambda^-(t)e(\Psi^-(t))
 \Bigg\}.
\end{aligned}}
\tag{176.K21}
\]

The inequalities \(s_t,w_t\ge1\) explicitly enforce opposing
displacement.  Equation (176.K21) retains the Fejer factor, determinant
range, low original-gcd cutoff, endpoint conjugations, both orientations,
all literal fields, and one outer real part.

## Proof of the algebra and parity seams

In the plus orientation,

\[
 d'm'-dm=(d+2s)m'-d(m'+2w)=2\kappa(sv-wu).
\tag{176.K22}
\]

The primitive equation gives (176.K8), and its canonical residue makes
the map bijective.  The minus orientation follows from
\(d'm'-dm=2\kappa(uw-sv)\).  Since \(\kappa u\) is odd,

\[
 \chi_4(\kappa u+2s)\chi_4(\kappa u)=(-1)^s,
\tag{176.K23}
\]

which proves the character laws.  Direct substitution gives the common
product step.

In the plus orientation, squarefreeness of
\((\kappa u+2s)\kappa v\) gives \((\kappa,s)=1\).  Hence

\[
 (d,d')=(\kappa u,\kappa u+2s)
 =(\kappa u,s)=(u,s)=(u,sv-wu)=(u,n).
\tag{176.K24}
\]

The lower squarefree endpoint gives the same result in the minus
orientation.  This proves (176.K11).

The two-adic branches are retained.  In the odd-product branch, \(v\) is
odd.  In the even-even squarefree branch, \(v=2v_1\) with \(v_1\) odd,
both products are \(2\pmod4\), and therefore \(n\) and \(w\) are even.
The step \(w\mapsto w+v\) preserves that parity, whereas
\(s\mapsto s+u\) flips parity.  After removing the fixed factor two,
every squarefree Möbius progression has odd modulus and preserves
\((-1)^t\).

The Fourier formula follows from the geometric series with ratio
\(-e(-k/m)\); its numerator is two because \(m\) is odd.  The normalized
\(\ell^1\) bound is the reciprocal-cosine harmonic sum around \(m/2\),
and the \(\ell^2\) identity is Parseval.  For (176.K14), the congruence
\(sv\equiv\pm n\pmod u\) forces its canonical residue to be
\(g[\pm\bar v n_0]_{u_0}\).  The integer \(g=(u,n)\) is odd, so the
parities agree.

The statement-only original-gcd coordinates are compatible with the cross
coordinates.  If

\[
 g=(d,d'),\quad d_{\rm lo}=ga,\quad d_{\rm hi}=g(a+2k),
 \quad m_{\rm lo}=m_0,\quad m_{\rm hi}=m_0+2w,
\tag{176.K25}
\]

and \(K=km_0-aw\), then in the plus orientation

\[
 g=(u,n),\quad a={\kappa u\over g},\quad k={s\over g},
 \quad m_0=\kappa v,\quad K={\kappa n\over g},
 \quad (a,m_0)=\kappa.
\tag{176.K26}
\]

Thus the common step \(2gam_0/(a,m_0)\) equals \(2\kappa uv\), and the
two character laws are identical.

## Strict-sector count

Fix \(\kappa\) and put \(Y=L/\kappa\).  The inward cross product is
smaller than both opposing endpoint products, and the shift is below
\(R_0\), so

\[
 uv\ll Y^2,\qquad n\ll Y.
\tag{176.K27}
\]

A primitive row advances by \(2\kappa uv\), so it has at most
\(O(1+L^2/(\kappa uv))\) sites in the product shell.  Therefore

\[
\begin{aligned}
 C_\kappa
 &\ll X^\varepsilon\sum_{uv\ll Y^2}\sum_{n\ll Y}
 \left(1+{L^2\over\kappa uv}\right)\\
 &\ll X^\varepsilon\left{
 Y^3\log(2Y)+{L^2Y\over\kappa}\log^2(2Y)\right}
 \ll {L^3\over\kappa^2}X^\varepsilon.
\end{aligned}
\tag{176.K28}
\]

Both orientations change only the constant.  All literal restrictions
delete atoms or downweight them.  Hence

\[
 \sum_{\kappa\ge K}C_\kappa
 \ll {L^3\over K}X^\varepsilon,
\tag{176.K29}
\]

which proves (176.K15) at \(K=\delta L\).

## Positive-transform self-return

On a full fixed-relative fibre, write

\[
 x(t)=N_0+2\kappa uv\,t,\qquad r=2\kappa n,
 \qquad \Phi(t)=J(\sqrt{x(t)+r}-\sqrt{x(t)})+{t\over2}.
\tag{176.K30}
\]

Then

\[
 T\asymp\kappa,\qquad
 F\asymp{2Jn\kappa\over L},\qquad
 \Phi''\asymp{2Jn\over\kappa L},\qquad
 |\Phi'''|\asymp{2Jn\over\kappa^2L}.
\tag{176.K31}
\]

The derivative image has \(O(1+2Jn/L)\) half-lattice modes, and one
saddle has size \((\kappa L/(2Jn))^{1/2}\).  Absolute recombination gives

\[
 \sqrt F+{T\over\sqrt F},
\tag{176.K32}
\]

which has no power saving over \(T\).  Thus the positive row tail is
\(L^3/K\), whereas a hypothetical \(O(X^\varepsilon)\) complete-row
bound would give \(L^3/K^2\).  At \(K=L^{1/2}\), these are
\(L^{5/2}\) and \(L^2\).

For the two-variable smooth-cell transform, put

\[
 \Theta(s,w)=J\{\sqrt{\kappa v(\kappa u+2s)}
 -\sqrt{\kappa u(\kappa v+2w)}\}+{s\over2}.
\tag{176.K33}
\]

Its Hessian is diagonal with determinant of size \(J^2/L^2\).  The
primitive vector \((v,-u)\) extends to a unimodular basis; the determinant
and fibre strip has physical area \(O(L)\).  The gradient image therefore
has volume \(O(J^2/L)\), while one stationary coefficient has scale
\(L/J\).  Positive dual recombination has \(O(J)\) capacity, so the
physical \(O(L)\) certificate wins.  Summing over anchors returns

\[
 \sum_{\kappa\ll L}(L/\kappa)^2L\ll L^3.
\tag{176.K34}
\]

The half-frequency only translates one dual coordinate.  Equations
(176.K30)--(176.K34) concern named positive-recombination mechanisms on
smooth fixed-relative cells.  They do not execute a literal discontinuous
Poisson theorem and are not lower bounds.

The canonical anchor also has constant-sign controls, for example
\(v=(u+1)/2\), \(s=2n\), \(w=n\), but (176.K12)--(176.K14) remove that
sawtooth at logarithmic algebra cost.  Such controls refute only naive
determinant pairing.  Arbitrary-support, dechirped, selector-erased, and
positive Möbius controls likewise remain nonliteral diagnostics.

## First open step and scope

Using the fixed-\(u\) Fourier expansion, a sufficient new theorem would,
for both orientations and uniformly in \(\kappa,u,v\) and \(k\pmod u\),
prove

\[
 \sum_{n\ll L/\kappa}\sum_{t\in\mathbb Z}
 \Lambda^\pm_{\kappa,u,v,n}(t)
 e\!\left(\Psi^\pm_{\kappa,u,v,n}(t)+{t\over2}
          \pm{k\bar v n\over u}\right)
 \ll_\varepsilon \kappa X^\varepsilon.
\tag{176.K35}
\]

All literal fields and the displacement indicators are those in
(176.K18) and (176.K20).  Since

\[
 \sum_{\kappa\ll L}\kappa
 \#\{(u,v):uv\ll(L/\kappa)^2\}
 \ll L^2(\log(2L))^2,
\tag{176.K36}
\]

(176.K13) and (176.K35) would prove the full K17a target after absorbing
logarithms.  No accepted theorem proves (176.K35); in particular, the
literal selected/no-pair field has no proved variation or Fourier norm in
the required joint labels, and the large near-half alias must be retained.

Accordingly, the fixed-proportion cross-gcd sector is closed, but the
complement, the full K17a target, the complete residual scalar, every other
hard-TOP channel, hard TOP, BAL, UNBAL, M9--M2, M9--M1/GAR, endpoint
uniformity, M9, both bridges, the quarter theorem, and every stronger
exponent remain open.
