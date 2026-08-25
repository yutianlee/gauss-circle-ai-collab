# M9--M1 \(D=d=L=1\) full-Abel common-profile recombination kernel

## Scope

Fix \(A>0\), set \(N=\lfloor X\rfloor\), and put

\[
 q=4N,\qquad K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\le K,\qquad M\le N^{1/2}.
\tag{K159.1}
\]

For every odd \(d\mid N\), let

\[
 c=\frac qd,\qquad H=\frac c2,\qquad n=\frac H2=\frac Nd.
\tag{K159.2}
\]

Retain the literal coefficient on its inherited unique nonwrapping
physical lift,

\[
 B_j(x)=
 \mathbf 1_{x\ge1}\mathbf 1_{-x\le j\le x-1}
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right),
\tag{K159.3}
\]

including the actual zero-extended profile components, transitions,
half-open choices, hard endpoints, and complex residual phase.  The
inherited profile satisfies

\[
 \operatorname {supp}(w_U)\subset[\alpha M,\beta M],\qquad
 \|w_U\|_\infty+\operatorname {Var}(w_U)
 \ll_\varepsilon M^{-3/4}X^\varepsilon
\tag{K159.4}
\]

for fixed positive \(\alpha,\beta\), componentwise with zero extension.
The external \(B_{1,U}(1)\) factor is a separate assembly seam.

## 1. The six finite Abel lines reconstruct the original row

Write

\[
 a=\lfloor V\rfloor+1,\qquad b=\lfloor2V\rfloor,
 \qquad J_+=[a,b]\cap\mathbb Z,
 \qquad J_-=[-b,-a]\cap\mathbb Z.
\tag{K159.5}
\]

If either signed block is empty, all sums over that block, including its
endpoint prefix or suffix sum, are defined to be zero.  Singleton blocks
are covered literally by the formulas below: the difference sums are then
empty and the outer term is the original row.

On the relevant signed block put

\[
 F_j(x)=w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right),
\]

with literal zero extension.  Thus

\[
 B_j(x)=\mathbf 1_{x\ge j+1}F_j(x)\quad(j\in J_+),
 \qquad
 B_j(x)=\mathbf 1_{x\ge-j}F_j(x)\quad(j\in J_-).
\tag{K159.6}
\]

For fixed \((d,v)\), abbreviate

\[
 A_j=\widehat B_j(2dv),\qquad K_j=K(-v^2,-j;c),
\]

and define

\[
 P^+(j)=\sum_{s=a}^{j}K_s,qquad
 P^-(j)=\sum_{s=j}^{-a}K_s.
\tag{K159.7}
\]

The positive coefficient difference is

\[
 B_j-B_{j+1}=T_j^++R_j^+,
\quad
 T_j^+(x)=\mathbf 1_{x=j+1}F_j(x),
\quad
 R_j^+(x)=\mathbf 1_{x\ge j+2}\bigl(F_j(x)-F_{j+1}(x)\bigr).
\tag{K159.8}
\]

Finite prefix summation therefore gives the exact three-line identity

\[
\begin{aligned}
 \sum_{j=a}^{b}A_jK_j
 ={}&A_bP^+(b)
 +\sum_{j=a}^{b-1}P^+(j)\widehat T_j^+(2dv)\\
 &+\sum_{j=a}^{b-1}P^+(j)\widehat R_j^+(2dv).
\end{aligned}
\tag{K159.9}
\]

The negative coefficient difference is

\[
 B_j-B_{j-1}=T_j^-+R_j^-,
\quad
 T_j^-(x)=\mathbf 1_{x=-j}F_j(x),
\quad
 R_j^-(x)=\mathbf 1_{x\ge-j+1}\bigl(F_j(x)-F_{j-1}(x)\bigr).
\tag{K159.10}
\]

Finite suffix summation gives

\[
\begin{aligned}
 \sum_{j=-b}^{-a}A_jK_j
 ={}&A_{-b}P^-(-b)
 +\sum_{j=-b+1}^{-a}P^-(j)\widehat T_j^-(2dv)\\
 &+\sum_{j=-b+1}^{-a}P^-(j)\widehat R_j^-(2dv).
\end{aligned}
\tag{K159.11}
\]

Thus the positive right outer endpoint, positive moving atom, positive
literal difference, negative left outer endpoint, negative moving atom,
and negative literal difference reconstruct the original \(j\)-row
separately for every \((d,v)\).  Both moving atoms have positive sign.
Zero extension keeps every component birth, death, and transition inside
the displayed differences.  No Abel piece is estimated in this assertion.

## 2. Complete inversion and one-time subtraction of the special rows

The accepted half-period inverse identity is

\[
 \sum_{v\bmod H}e_c(-2vx)K(-v^2,-s;c)
 =\frac{1-i}{2}\sqrt c
 \sum_{u\bmod c}^{*}\chi_4(u)e_c\bigl(u(x^2-s)\bigr).
\tag{K159.12}
\]

After multiplication by the exterior theta factor,

\[
 -\frac{i(1+i)}{2Nq}\chi_4(d)d\sqrt c
 \cdot\frac{1-i}{2}\sqrt c
 =-\frac{i}{2N}\chi_4(d),
\tag{K159.13}
\]

because \(dc=q\).  The change of variables \(h=du\pmod q\), with
\(d=(h,N)\), partitions the odd residues modulo \(4N\).  Hence the
complete \(d\)- and \(v\)-sum returns

\[
 G_N(t)=\mathbf 1_{N\mid t}\chi_4(t/N).
\tag{K159.14}
\]

Let \(\mathcal Z_U(V)\) and \(\mathcal F_U(V)\) be respectively the
whole \(v=0\) and whole \(v=H/2\) rows, with the original divisor sum
and normalization.  Recombining (K159.9)--(K159.11) before completing
frequency gives

\[
 \boxed{
 \mathcal T_{\mathrm{int},U}(V)
 =\mathcal S_U(V)-\mathcal Z_U(V)-\mathcal F_U(V),}
\tag{K159.15}
\]

where

\[
 \mathcal S_U(V)=
 \sum_{V<|j|\le2V}\sum_{x\in\mathcal L_U}B_j(x)G_N(x^2-j),
\tag{K159.16}
\]

and \(\mathcal L_U\) denotes the inherited complete set of physical
representatives modulo \(4N\).  This convention is essential because the
literal \(B_j\) is attached to that physical lift rather than being a
representative-invariant function before the lift is fixed.

Each special whole row is subtracted exactly once.  The special-frequency
pieces of the isolated Round-158 moving trace are not additional terms in
(K159.15).  When \(c=4\), the zero and Nyquist rows exhaust that fibre and
the paired-interior set is empty, consistently with (K159.15).

The accepted estimates

\[
 |\mathcal Z_U(V)|+|\mathcal F_U(V)|
 \ll_\varepsilon M^{-1/4}X^\varepsilon
\tag{K159.17}
\]

remain whole-row theorems; they are not transferred to any Abel subpiece.

## 3. The actual physical lift and the common-profile selected wave

If a term of (K159.16) is nonzero, write

\[
 x^2-j=N\ell.
\tag{K159.18}
\]

The literal cell becomes

\[
 x^2-x+1\le N\ell\le x^2+x.
\tag{K159.19}
\]

The integer intervals in (K159.19), as \(x\ge1\) varies, partition the
positive integers.  There is no half-integer tie.  Therefore

\[
 \kappa(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,
 \qquad r(\ell)=\kappa(\ell)^2-N\ell
\tag{K159.20}
\]

give the unique selected pair \(x=\kappa(\ell)\), \(j=r(\ell)\).

The lift indicator that is necessary under a stripped arbitrary-BV
statement is identically one in the actual project.  Indeed, (K159.4)
gives \(\kappa(\ell)\asymp K\), the supported root hull has length
\(O(K)<N\), and \(2\kappa(\ell)<N\) for sufficiently large \(X\).
The inherited complete lift is chosen to contain this unique positive
nonwrapping physical hull.  The finitely many bounded values before the
displayed eventual inequalities hold are covered by that defining lift
convention.  Thus

\[
 w_U(\ell)\ne0\quad\Longrightarrow\quad
 \kappa(\ell)\text{ lies in the chosen physical lift}.
\tag{K159.21}
\]

At the selected pair,

\[
 w_U\!\left(\frac{x^2-j}{N}\right)=w_U(\ell),\qquad
 e\!\left(\sqrt{x^2-j}-x\right)=e(\sqrt{N\ell}),
\tag{K159.22}
\]

because \(x=\kappa(\ell)\) is integral.  Consequently

\[
 \boxed{
 \mathcal S_U(V)=
 \sum_{\ell\ge1}\chi_4(\ell)w_U(\ell)e(\sqrt{N\ell})
 \mathbf 1_{V<|r(\ell)|\le2V}.}
\tag{K159.23}
\]

This is exactly the hard dyadic block of the accepted Round-154
common-profile root-defect wave, using the inherited identification
\(w_U(\ell)=\ell^{-3/4}A_U(\ell)\).  It is an exact reparametrization, not
a new analytic estimate.  It does not alter the Round-158 fact that the
isolated moving trace has two different boundary-frozen profiles.  The
outer and difference lines restore the quotient profile only after all six
lines are recombined.

## 4. Variable residual mask and target calibration

Put

\[
 \delta(\ell)=\sqrt{N\ell}-\kappa(\ell)\in(-1/2,1/2).
\]

Then

\[
 r(\ell)=-\delta(\ell)\bigl(2\kappa(\ell)+\delta(\ell)\bigr).
\tag{K159.24}
\]

For \(s\in\{V,2V\}\), the two moving positive endpoint sizes are

\[
 u_s^+(k)=k-\sqrt{k^2-s},\qquad
 u_s^-(k)=\sqrt{k^2+s}-k,
\tag{K159.25}
\]

where \(u_s^+\) is used when \(s\le k^2\); outside that eventual supported
range its endpoint is defined by saturation at the half-cell.  Precisely,
the two selected intervals are

\[
 \delta\in[-u_{2V}^+(k),-u_V^+(k))\cap(-1/2,0)
 \quad\hbox{or}\quad
 \delta\in(u_V^-(k),u_{2V}^-(k)]\cap(0,1/2).
\tag{K159.25a}
\]

Thus the defect mask is not a fixed fractional interval.  Clipping matters
when \(V\asymp K\).

Write \(w_U=M^{-3/4}\widetilde w_U\), so that

\[
 \|\widetilde w_U\|_\infty+
 \operatorname {Var}(\widetilde w_U)\ll_\varepsilon X^\varepsilon.
\tag{K159.25b}
\]

The desired, presently unproved normalized scalar target is

\[
 \mathcal S_U(V)\ll_\varepsilon X^\varepsilon,
\tag{K159.26}
\]

equivalently the desired, presently unproved raw signed estimate

\[
 \left|
 \sum_{\ell\asymp M}\chi_4(\ell)\widetilde w_U(\ell)
 e(\sqrt{N\ell})\mathbf 1_{V<|r(\ell)|\le2V}
 \right|
 \ll_\varepsilon M^{3/4}X^\varepsilon.
\tag{K159.27}
\]

The accepted support estimate

\[
 \#\{\ell:w_U(\ell)\ne0, V<|r(\ell)|\le2V\}
 \ll_\varepsilon\min(M,V)X^\varepsilon
\tag{K159.28}
\]

is unsigned.  It recovers the accepted fixed-polylogarithmic collar but
does not prove (K159.27) beyond that collar.

## 5. Audited Fourier and transform frontier

Let \(h\) denote a Fourier mode of the exact variable band.  Since
\(e(h\delta)=e(h\sqrt{N\ell})\), the built-in phase shifts it to
\(e((h+1)\sqrt{N\ell})\).  The exceptional shifted mode is \(h=-1\).
Its square-root phase disappears but \(\chi_4(\ell)\) remains.  The exact
moving-band Fourier coefficient is defined by periodically extending

\[
 g_{k,V}(u)=\mathbf 1_{V<|-u(2k+u)|\le2V},
 \qquad -\tfrac12<u<\tfrac12,
 \qquad
 c_h(k)=\int_{-1/2}^{1/2}g_{k,V}(u)e(-hu)\,du.
\tag{K159.28a}
\]

The coefficient \(c_{-1}(k)\) has uniformly bounded total
variation for \(k\asymp K\).  Since \(\kappa(\ell)\) is monotone, discrete
Abel summation against bounded partial sums of \(\chi_4\) gives the precise
raw bound

\[
 \left|\sum_\ell\chi_4(\ell)\widetilde w_U(\ell)
 c_{-1}(\kappa(\ell))\right|\ll_\varepsilon X^\varepsilon.
\tag{K159.29}
\]

The corresponding contribution to the normalized \(\mathcal S_U(V)\) is
\(O_\varepsilon(M^{-3/4}X^\varepsilon)\).  This closes one Fourier mode
only.

Two complementary route ledgers remain above target in the frozen cone.

1. Ordinary Vaaler/Erdos--Turan plus the second-derivative bound gives,
   at height \(Q\), the favorable raw capacity
   \[
    \left(\frac M Q+\sqrt{KQ}+\frac M{\sqrt K}+1\right)X^\varepsilon.
   \tag{K159.30}
   \]
   Its optimized leading term reaches \(M^{3/4}\) only when
   \(M\ge N^{2/3}\), outside \(M\le N^{1/2}\).

2. Retaining literal sampled boundary incidences and the accepted root
   count gives, for polynomial degree \(J\),
   \[
    E_J\ll_\varepsilon
    \left(\frac KJ+\sqrt V+\sqrt M+1\right)X^\varepsilon.
   \tag{K159.31}
   \]
   This unsigned error is target-safe only if
   \(J\ge KM^{-3/4}\) and \(V\le M^{3/2}\).  Even in that subrange, the
   favorable transformed exponent pair
   \((195/796,235/398)\) gives raw capacity
   \[
    N^{195/796}M^{1295/3184+\varepsilon},
   \tag{K159.32}
   \]
   which reaches the target only if \(M^{1093}\ge N^{780}\), again
   outside the frozen cone.  This is a method-specific capacity, not a
   universal barrier.  Replacing (K159.31) by the unproved favorable
   \(M/J\) boundary surrogate recovers the older threshold
   \(M^{703}\ge N^{390}\); it does not improve the conclusion.

For \(h+1=q_1\ne0\), splitting \(\chi_4\) and applying the
Poisson/van-der-Corput \(B\)-process gives stationary denominators

\[
 d=4m\mp1,qquad
 \ell_{q_1,d}=\frac{4q_1^2N}{d^2},\qquad
 \text{stationary phase }e\!\left(\frac{q_1^2N}{d}\right).
\tag{K159.33}
\]

The \(q_1=\pm1\) branches are exactly the accepted reciprocal carrier
from Round 154; general \(q_1\) gives the same interface with numerator
\(q_1^2N\).  The dual length and stationary amplitude reproduce the
corresponding \(B\)-transformed exponent-pair capacity.  They supply no
automatic gain.

Finally, the exact quotient projector followed by the audited incomplete
quadratic bound has favorable raw capacity \(N^{1/2}X^\varepsilon\),
which would require \(M\ge N^{2/3}\).  These statements are scoped
upper-bound ledgers.  They are neither lower bounds for (K159.27) nor
impossibility theorems for a future joint signed method.

## 6. Remaining frontier

The exact finite algebra has no remaining Abel seam: the two outer, two
moving, and two difference lines are one telescoping presentation of the
already open common-profile wave.  The first unproved statement is
(K159.27), uniformly on the open side

\[
 M^{449}\ll R^{780},\qquad R=X^{1/4},qquad N=\lfloor X\rfloor,
\]

and beyond the accepted fixed-polylogarithmic defect collar.  A future
proof must couple the conductor-four sign, common quotient profile,
square-root phase, and all literal moving hard boundaries, or use a new
representation that preserves the same information.

Nothing in this kernel transfers to \(D>1\), \(L>1\), generic \(t=1\),
original \(t\ge2\), the cross owner, another M1 or M2 component, endpoint
uniformity, M9, the bridge, the quarter theorem, or either global exponent.
