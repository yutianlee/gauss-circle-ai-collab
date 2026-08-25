# Round 138 discovery report: literal signed Farey scalar attack

Campaign: `m9-m1-lower-gar-signed-farey-scalar-gate`

Task: `literal_signed_farey_scalar_attack`

Role: discovery

Starting graph SHA-256: `56de446648dfb7a492fbb4b46c38d840fb14ac306df61bf61d466d26abfbe797`

Status: candidate evidence only; no graph or shared-state edit is licensed.

## 1. Result

**Exit label: `strict_signed_farey_reduction`.**

Put

\[
 R=X^{1/4},\qquad y=\lfloor\sqrt X\rfloor,\qquad
 N=\lfloor X\rfloor,
\]

and let \({\cal P}\) be the literal set of reduced samples

\[
 (a,b),\qquad 2\leq b\leq y,\quad b\ \text{odd},\quad
 1\leq a<b,\quad (a,b)=1,
\]

on which \(J_{R,y}(a/b)\ne0\).  Define

\[
 u_{a,b}:=L_\chi(y/b)\,
 {\eta(ya/b)V_{\rm low}(4R^2a^2/b^2)\over a},
 \quad
 \theta_{a,b}:={Na\over b},
 \quad
 \phi_{a,b}:={Na\over b}+{b-1\over4}.
\tag{138.1}
\]

At every nonzero literal sample \(ya/b\geq1\), so the displayed \(\eta\)
is actually one.  Since \(\chi _4(b)=e((b-1)/4)\), the exact scalar has
the two equivalent forms

\[
 {\cal F}_N
 =\sum_{(a,b)\in{\cal P}}\lambda_bJ_{R,y}(a/b)e(\theta_{a,b})
 =\sum_{(a,b)\in{\cal P}}u_{a,b}e(\phi_{a,b}).
\tag{138.2}
\]

Let \(\delta_*=y^{-2}\), and define the conjugation-closed signed
survivor

\[
 \begin{split}
 {\mathfrak S}_N:=
 \sum_{\substack{(a,b),(a',b')\in{\cal P}\; b\ne b'\\
  \|\theta_{a,b}-\theta_{a',b'}\|>\delta_*\\
  \|\phi_{a,b}-\phi_{a',b'}\|>\delta_*}}
 u_{a,b}\overline{u_{a',b'}}
 e(\phi_{a,b}-\phi_{a',b'}).
 \end{split}
\tag{138.3}
\]

Then, uniformly for every real \(X\geq2\),

\[
 \boxed{
 |{\cal F}_N|^2={\mathfrak S}_N+O_\varepsilon(yX^\varepsilon).}
\tag{138.4}
\]

This is a strict, owner-complete reduction.  Every pair left in
\({\mathfrak S}_N\) has different denominators and therefore nonzero
Farey determinant.  The deleted part contains the entire diagonal, all
same-denominator unequal-numerator pairs, every exact ordinary phase-one
collision, every exact alignment after absorbing the actual
\(\chi _4\)-carrier, and fixed-order microscopic neighbourhoods of both
types.  Thus \(|{\mathfrak S}_N|\ll_\varepsilon yX^\varepsilon\) would be
equivalent, after renaming \(\varepsilon\), to the required
\(|{\cal F}_N|\ll_\varepsilon RX^\varepsilon\).

The report does not prove that last survivor estimate.  The exact
determinant coordinates expose a coherent solution direction on which
neither the determinant phase nor the common-denominator character
oscillates.  Expanding the lift character and pairing adjacent odd
denominators returns the accepted lower height kernel.  At fourth-power
centres its literal half-integer stationary tubes have scalar absolute
capacity \(R^{3/2}\), versus target \(R\).  Character Poisson on a smooth
interior window gives the same modes with principal coefficient
\(N^{1/4}\chi_4(r)(hr)^{-3/4}\) and returns the lower Hardy--Legendre
radial sum.  Its exact squarefree-radical phase-one channel is target-safe,
but the nonsquare and near-radical modes retain the full \(R^{3/2}\)
principal capacity.  Hence these transforms diagnose the remaining
joint cancellation; they do not estimate it.

## 2. Exact statement and hypotheses

The hypotheses are exactly those in the Round-138 blind statement.  The
character is the primitive real character modulo four, \(e(t)=e^{2\pi it}\),

\[
 L_\chi(T)=\sum_{g\leq T}{\chi_4(g)\over g},\qquad
 \lambda_b={\chi_4(b)\over b}L_\chi(y/b),
\tag{138.5}
\]

and the alternating-series estimate gives \(|L_\chi(T)|\leq1\).  The
fixed smooth literal profile is

\[
 J_{R,y}(t)=\eta(yt){V_{\rm low}(4R^2t^2)\over t}
\tag{138.6}
\]

on its small positive arc, is extended smoothly by zero and periodically,
and has \(J_{R,y}(0)=0\).  Fix constants \(C_V,M_V\) such that every
positive sample has \(a/b<C_V/R\) and \(|V_{\rm low}|\leq M_V\).  It
follows that

\[
 a\leq C_Vb/R,\qquad
 |\lambda_bJ_{R,y}(a/b)|=|u_{a,b}|\leq {M_V\over a}.
\tag{138.7}
\]

All implied constants below may depend on the fixed literal profiles but
not on \(X,N,y,a,b\).  The finitely many \(X\) below the fixed support
threshold are absorbed in those constants.  The negative scalar sign is
the complex conjugate and therefore has the identical square and all the
same estimates.

For reference, the complete power ledger is:

| Object | Literal capacity | Required level / proved deletion |
|---|---:|---:|
| denominator count | \(y\asymp R^2\) | retained exactly |
| numerator count in row \(b\) | \(O(b/R)\leq O(R)\) | retained exactly |
| total number of reduced samples | \(O(y^2/R)=O(R^3)\) | no counting gain claimed |
| row \(\ell^1\)-mass | \(O(\log(2+b/R))\) | used only in safe sectors |
| total scalar \(\ell^1\)-mass | \(O(y\log X)=O(R^2\log X)\) | absolute scalar capacity |
| exact-square diagonal | \(O(y)=O(R^2)\) | target-square-safe |
| complete same-denominator block | \(O(y\log^2X)\) | target-square-safe |
| one ordinary phase fibre | \(O(\tau(N)\log X)\) | subpolynomial |
| ordinary or adjusted \(\delta\)-near collisions | \(O(y\tau(N)\log^2(2X)(1+\delta y^2))\) | target-safe at \(\delta=y^{-2}\) |
| unrestricted cross-denominator absolute square | \(O(y^2\log^2X)=O(R^4\log^2X)\) | survivor still has this capacity |
| fourth-power stationary-tube scalar mass | \(\gg R^{3/2}\) after tube-wise modulus | target is \(R\) |
| corresponding cross-tube square capacity | \(\gg R^3\) | target is \(y\asymp R^2\) |

The last two lines concern actual physical coefficients on literal
interior support, not an arbitrary coefficient array.  They are capacity
statements after a forbidden partial modulus, not lower bounds for the
signed scalar.

## 3. Proof or derivation

**Exact scalar dictionary.**  In the flat cone write \(h/d=a/b\) in
lowest terms, so \(h=ag\), \(d=bg\), and \((a,b)=1\).  Complete
multiplicativity of \(\chi_4\) and the missing harmonic factor give

\[
 \sum_{g\leq y/b}{\chi_4(bg)\over ag}
 V_{\rm low}(4R^2a^2/b^2)e(aN/b)
 ={\chi_4(b)L_\chi(y/b)\over a}
 V_{\rm low}(4R^2a^2/b^2)e(aN/b).
\tag{138.8}
\]

Only odd lifts survive.  Conversely every \((a,b,g)\) on the right gives
the unique pair \((h,d)=(ag,bg)\), so there is neither a lost multiplicity
nor an extra \(1/d\).  At a nonzero sample \(ya/b\geq y/b\geq1\), hence
\(\eta=1\), and

\[
 \lambda_bJ_{R,y}(a/b)
 ={\chi_4(b)L_\chi(y/b)\over b}{b\over a}
 V_{\rm low}(4R^2a^2/b^2)
 ={\chi_4(b)L_\chi(y/b)\over a}V_{\rm low}(4R^2a^2/b^2).
\tag{138.9}
\]

The residue centre \(b=1\) is \(J_{R,y}(0)=0\).  Equivalently, once
\(R\) exceeds the fixed support constant the positive support has
\(0<h<d\), so no positive integer ratio occurs; the bounded remaining
values of \(X\) are harmless.  Equations (138.8)--(138.9) prove the exact
equivalence of (138.B4) and (138.B5), including the primitive numerator,
odd lift, profile, floor, and centre conventions.  Absorbing
\(\chi_4(b)=e((b-1)/4)\) proves (138.2).

**Exact square, diagonal, and same denominator.**  Put

\[
 \Delta=ab'-a'b.
\tag{138.10}
\]

The two exact square dictionaries are

\[
 \begin{split}
 |{\cal F}_N|^2
 &=\sum_{{\cal P}\times{\cal P}}
 \lambda_b\overline{\lambda_{b'}}
 J(a/b)\overline{J(a'/b')}
 e\!\left({N\Delta\over bb'}\right)\\
 &=\sum_{{\cal P}\times{\cal P}}
 u_{a,b}\overline{u_{a',b'}}
 e\!\left({N\Delta\over bb'}+{b-b'\over4}\right).
 \end{split}
\tag{138.11}
\]

Equality \(\Delta=0\) means equality of two reduced positive fractions,
hence exactly \((a,b)=(a',b')\).  By (138.7),

\[
 {\cal E}_{\rm diag}
 =\sum_{(a,b)\in{\cal P}}|u_{a,b}|^2
 \ll\sum_{b\leq y}\sum_{a\geq1}{1\over a^2}
 \ll y.
\tag{138.12}
\]

For a fixed denominator let

\[
 H_b:=\sum_{\substack{a:(a,b)\in{\cal P}}}|u_{a,b}|
 \ll 1+\log(2+b/R)\ll\log(2X).
\tag{138.13}
\]

The entire same-denominator square block, before separating its diagonal,
is bounded by

\[
 \sum_{b\leq y}
 \left|\sum_{a:(a,b)\in{\cal P}}u_{a,b}e(\phi_{a,b})\right|^2
 \leq\sum_{b\leq y}H_b^2
 \ll y\log^2(2X).
\tag{138.14}
\]

Consequently the same-denominator unequal-numerator sector is also
\(O(y\log^2X)\).  This rowwise modulus is used only to delete a sector
already at target-square scale; it is not applied to the remaining
cross-denominator scalar.

**Ordinary and character-adjusted phase fibres.**  Reduce
\(\theta_{a,b}=Na/b\pmod1\).  If

\[
 g=(N,b),\qquad q=b/g,
\tag{138.15}
\]

then \((N/g,q)=1\) and

\[
 \theta_{a,b}={u\over q}\pmod1,
 \qquad u\equiv (N/g)a\pmod q,
 \qquad (u,q)=1
\tag{138.16}
\]

when \(q>1\); \(q=1\) is the zero phase.  Conversely a member of the
reduced fibre \(u/q\) has

\[
 b=qg,\qquad g\mid N,\qquad (N/g,q)=1,
\tag{138.17}
\]

and \(a\) lies in the single residue class
\(a\equiv (N/g)^{-1}u\pmod q\).  Primitive and profile restrictions only
delete entries from this progression.  Uniformly in its first positive
residue \(r\),

\[
 \sum_{\substack{a\leq C_Vqg/R\\a\equiv r\ (q)}}{1\over a}
 \ll 1+{1\over q}\log(2+C_Vg/R)\ll\log(2X).
\tag{138.18}
\]

There are at most \(\tau(N)\) possible \(g\)'s.  The same conclusion for
\(q=1\) follows by summing the harmonic rows over the divisors \(b\mid N\).
Thus, if \(M(z)\) denotes the \(\ell^1\)-mass in one exact ordinary phase
fibre,

\[
 \max_zM(z)\ll\tau(N)\log(2X),
 \qquad
 \sum_zM(z)\ll y\log(2X).
\tag{138.19}
\]

It follows immediately that all exact phase-one collisions, including
divisor denominators at fourth-power centres, have absolute mass

\[
 \sum_zM(z)^2\ll y\tau(N)\log^2(2X)\ll_\varepsilon yX^\varepsilon.
\tag{138.20}
\]

For the actual carrier \(\phi\), denominators \(b\equiv1\pmod4\) have no
shift and denominators \(b\equiv3\pmod4\) have shift \(1/2\).  Therefore
one exact \(\phi\)-fibre is the union of at most two restricted
\(\theta\)-fibres, separated by \(1/2\), and its mass is at most twice
the first bound in (138.19).  This proves the same estimate for every
exact full-carrier alignment.  In particular, absorbing \(\chi_4\) does
not expose a larger exact coherent family.

There is also a quantitative near-collision version.  Distinct reduced
\(\theta\)-values have denominators at most \(y\), hence circular spacing
at least \(y^{-2}\).  Distinct reduced \(\phi\)-values have denominators
at most \(2y\), hence spacing at least \((2y)^{-2}\).  Packing such values
in a circular arc and using (138.19) gives, for either carrier and every
\(0\leq\delta\leq1/2\),

\[
 \sum_{\|z-z'\|\leq\delta}M(z)M(z')
 \ll y\tau(N)\log^2(2X)(1+\delta y^2).
\tag{138.21}
\]

For \(\phi\) only the absolute constant changes (one may take the packing
factor \(1+8\delta y^2\)).  Taking \(\delta=\delta_*=y^{-2}\), combining
(138.12), (138.14), and (138.21), and deleting the union of the three safe
sets proves (138.4).  Numerator support endpoints cause no seam in this
argument: they merely shorten the progressions in (138.18).  The estimate
is uniform in the integer floors \(N,y\).

**Exact determinant-fibre attack.**  For a cross-denominator pair write

\[
 G=(b,b'),\qquad b=Gr,\qquad b'=Gs,\qquad (r,s)=1.
\tag{138.22}
\]

Then

\[
 \Delta=G\delta,\qquad \delta=as-a'r\ne0,
 \qquad {N\Delta\over bb'}={N\delta\over Grs}.
\tag{138.23}
\]

Given \((G,r,s,\delta)\), choose one solution \((a_0,a'_0)\) of
\(as-a'r=\delta\).  Every solution is

\[
 a=a_0+r\ell,\qquad a'=a'_0+s\ell.
\tag{138.24}
\]

The literal positive supports, primitive restrictions, and hard numerator
endpoints define an exact finite set \(I_{G,r,s,\delta}\) of such
\(\ell\)'s, and

\[
 |I_{G,r,s,\delta}|\ll1+G/R,
 \qquad |\delta|\ll Grs/R.
\tag{138.25}
\]

Since all denominators are odd,

\[
 \chi_4(Gr)\chi_4(Gs)=\chi_4(rs).
\tag{138.26}
\]

Thus both the determinant phase and the denominator character are
constant along the \(\ell\)-direction.  With the literal profile and
\(L_\chi\)-factors included in \(U_\ell\), the complete cross square is
exactly of the form

\[
 \sum_{\substack{G,r,s\ \text{odd}\\(r,s)=1,\ r\ne s\\Gr,Gs\leq y}}
 \chi_4(rs)
 \sum_{\delta\ne0}e\!\left({N\delta\over Grs}\right)
 \sum_{\ell\in I_{G,r,s,\delta}}^{*}
 {U_\ell\over(a_0+r\ell)(a'_0+s\ell)}.
\tag{138.27}
\]

The star in (138.27) is exactly
\((a_0+r\ell,Gr)=(a'_0+s\ell,Gs)=1\); it is not relaxed.  The strict
survivor additionally imposes the two inequalities in (138.3), which in
these coordinates are

\[
 \left\|{N\delta\over Grs}\right\|>y^{-2},\qquad
 \left\|{N\delta\over Grs}+{G(r-s)\over4}\right\|>y^{-2}.
\tag{138.28}
\]

There is a useful but insufficient scalar summation inside a determinant
fibre:

\[
 {1\over aa'}={1\over\delta}\left({s\over a'}-{r\over a}\right).
\tag{138.29}
\]

Taking full account of the literal bounded profile gives only the
aspect-sensitive estimate

\[
 \left|\sum_{\ell\in I_{G,r,s,\delta}}^{*}{U_\ell\over aa'}\right|
 \ll
 \min\!\left\{
  1+\log(2+G/R),
  {r+s+\log(2+G/R)\over|\delta|}
 \right\}.
\tag{138.30}
\]

Indeed, along a positive progression one has
\(r\sum 1/a\ll r+\log(2+G/R)\) and the analogous bound with \(s,a'\).
The factors \(r+s\) cannot be removed at the reciprocal-kernel level.
For any odd \(S>1\), take \(r=1,s=S,a=a'=1\), so
\(\delta=S-1\).  Choosing odd \(G\gg R\) with \(GS\leq y\), for
example \(G\asymp R^{3/2}\), \(S\asymp R^{1/2}\), places both pairs in
the literal small-arc chart.  The one-point reciprocal kernel is one,
whereas \(\log(2X)/(S-1)\to0\).  This refutes an aspect-free algebraic
bound without invoking a lower envelope for the actual profile; it is
not a lower bound for the physical fibre.  Thus (138.29) is not a
uniform \(1/|\delta|\) gain.  More safely, because
\(\delta\) merely partitions the pairs in one fixed denominator block,

\[
 \sum_{\delta\ne0}
 \left|\sum_{\ell\in I_{G,r,s,\delta}}^{*}{U_\ell\over aa'}\right|
 \leq H_{Gr}H_{Gs}\ll\log^2(2X).
\tag{138.30a}
\]

Summing (138.30a) over the unique triples \((G,r,s)\), equivalently over
all ordered denominator pairs, returns \(O(y^2\log^2X)\), exactly the
unrestricted square capacity.  The determinant chart is therefore an
exact dictionary, but neither (138.29) nor its correct aspect-sensitive
bound supplies a power contraction.  Primitive holes have no sign, the
phase is constant in \(\ell\), and the common factor \(G\) has disappeared
from \(\chi_4(Gr)\chi_4(Gs)\).

**Character pairing, fourth powers, and physical near resonance.**  Undoing
the lift aggregation in (138.8) is exact and returns

\[
 {\cal F}_N=\sum_{d\leq y}\chi_4(d)
 \sum_{h\geq1}{1\over h}V_{\rm low}(4R^2h^2/d^2)e(hN/d).
\tag{138.31}
\]

Pair \(d\equiv1\pmod4\) with \(d+2\equiv3\pmod4\).  Writing
\(W_h(d)=V_{\rm low}(4R^2h^2/d^2)\), one obtains exactly

\[
 {\cal F}_N={\cal E}_{\rm amp}+{\cal K}_N,
\tag{138.32}
\]

where boundary indicators are retained and

\[
 {\cal K}_N=
 \sum_h{1\over h}\sum_{d\equiv1(4)}
 W_h(d+2)e(hN/d)
 \left\{1-e\!\left(-{2hN\over d(d+2)}\right)\right\}.
\tag{138.33}
\]

The fixed-profile total variation and the one unmatched odd endpoint per
height give \({\cal E}_{\rm amp}\ll\log^2(2X)\) (in the flat smooth
interior the direct variation calculation gives \(O(\log X)\)).  This is
target-safe.  The factor in braces is small at integer increments but has
size two at half-integers.  For the unaggregated term put
\(\Phi_{h,d}=hN/d+(d-1)/4\).  It is exactly the corresponding
adjusted-carrier difference, because

\[
 \Phi_{h,d}-\Phi_{h,d+2}
 ={2hN\over d(d+2)}-{1\over2}\pmod1.
\tag{138.34}
\]

At fourth-power centres take an odd integer \(R\),
\(X=N=R^4\), and \(y=R^2\).  The literal interior used in the accepted
Round-121 tube lemma has \(d\asymp R^2\) and
\(R^{4/5}\leq h\leq cR\).  For each such \(h\), the decreasing function

\[
 \Psi_h(d)={2hR^4\over d(d+2)}
\tag{138.35}
\]

crosses \(\asymp h\) half-integers.  Around a crossing
\(\Psi_h(d_{h,m})=m+1/2\), take the \(d\equiv1\pmod4\) tube

\[
 |d-d_{h,m}|\leq c_0{R\over\sqrt h}.
\tag{138.36}
\]

The crossings are separated by \(\asymp R^2/h\), so these tubes are
disjoint.  Taylor expansion on the step-four lattice gives an integral
linear increment and \(O(1)\) quadratic variation on (138.36); choosing
\(c_0\) small keeps all terms in a fixed phase sector.  The profile stays
in its certified literal interior, and the factor in braces stays bounded
below.  Hence the actual tube contribution satisfies

\[
 |{\cal K}_N[h,m]|\gg {1\over h}{R\over\sqrt h}
 ={R\over h^{3/2}}.
\tag{138.37}
\]

Summing moduli over the \(\asymp h\) tubes for every retained \(h\) gives

\[
 \sum_{h,m}|{\cal K}_N[h,m]|
 \gg R\sum_{R^{4/5}\leq h\leq cR}h^{-1/2}
 \gg R^{3/2}.
\tag{138.38}
\]

The near-alignment width in (138.34) across one tube is
\(\asymp\sqrt h/R\), vastly larger than the safe Farey width \(y^{-2}=R^{-4}\).
Equation (138.38) is the actual physical reason that character pairing,
followed by tube-wise modulus, cannot reach \(R\).  It does not assert
that the signed sum of the tubes is large.  In the exact square their
cross-tube absolute capacity is \(R^3\), while the target is \(R^2\); the
missing cancellation must remain joint across heights and stationary
labels.

**Interior character Poisson and the radical control.**  To identify the
same stationary modes without losing correction owners, insert a fixed
smooth \(\psi(d/y)\) supported strictly inside the literal interval used
above and apply Poisson only to that exact interior piece.  With
\(\widehat f(\xi)=\int f(x)e(-x\xi)\,dx\), primitive character Poisson is

\[
 \sum_{d\in\mathbb Z}\chi_4(d)f(d)
 ={i\over2}\sum_{m\ \text{odd}}\chi_4(m)\widehat f(m/4).
\tag{138.39}
\]

For
\(f(x)=\psi(x/y)V_{\rm low}(4R^2h^2/x^2)e(hN/x)\), only
\(m=-r<0\) has an interior critical point, namely

\[
 x_0=2\sqrt{hN/r},\qquad
 {hN\over x_0}+{rx_0\over4}=\sqrt{Nhr}.
\tag{138.40}
\]

For critical points a fixed distance from the support boundary, direct
Taylor expansion gives

\[
 \int f(x)e(rx/4)\,dx
 =2(hN)^{1/4}r^{-3/4}A_{h,r}
 e(\sqrt{Nhr}+1/8)
 +O\!\left({1\over Rh^{3/2}}\right),
\tag{138.41}
\]

where

\[
 A_{h,r}=\psi(x_0/y)V_{\rm low}(R^2hr/N).
\tag{138.42}
\]

After the outside factor \(1/h\), the interior principal family is

\[
 -iN^{1/4}
 \sum_{\substack{h\geq1,\ r\ \text{odd}\\
                   (h,r)\ \text{in the stationary range}}}
 \chi_4(r)(hr)^{-3/4}A_{h,r}
 e(\sqrt{Nhr}+1/8).
\tag{138.43}
\]

Here \(h\) is any positive height, \(r\) is odd, and \(r\asymp h\).
For the well-inside modes the error in (138.41), after multiplication by
\(1/h\), summation over \(O(h)\) modes, and summation over \(h\), is
\(O(R^{-1})\), hence target-safe.  Modes whose critical points approach
the window boundary are not covered by this local expansion and are
retained below.  The principal absolute capacity is nevertheless

\[
 N^{1/4}\sum_{h\leq cR}h^{-3/4}
 \sum_{r\asymp h}r^{-3/4}
 \asymp R^{3/2}.
\tag{138.44}
\]

Grouping \(n=hr\) in (138.43) returns a literal angularly weighted
character-divisor coefficient multiplying
\(N^{1/4}n^{-3/4}e(\sqrt{Nn})\): this is the lower
Hardy--Legendre radial form, not a smaller object.

There is one useful exact control inside this principal family.  Write

\[
 N=Ds^2,\qquad D\ \hbox{squarefree}.
\tag{138.45}
\]

Then

\[
 e(\sqrt{Nn})=1\quad\Longleftrightarrow\quad Nn\ \hbox{is a square}
 \quad\Longleftrightarrow\quad n=Dk^2.
\tag{138.46}
\]

Using only \(|A_{h,r}|\ll1\) and the divisor bound, the complete exact
phase-one radical channel is

\[
 \begin{split}
 &N^{1/4}\sum_{Dk^2\ll R^2}(Dk^2)^{-3/4}
 \sum_{hr=Dk^2}1\\
 &\hspace{35mm}\ll_\varepsilon
 R D^{-3/4}X^\varepsilon\sum_{k\geq1}k^{-3/2}
 \ll_\varepsilon RX^\varepsilon.
 \end{split}
\tag{138.47}
\]

For \(D=1\) this is the square channel at fourth-power centres.  Thus the
stationary obstruction is not an exact-square main term; it lies in the
nonsquare and near-radical modes.

Equation (138.43) is deliberately not asserted as a full transform of
(138.31).  The exact owners still retained are the complement of the
inserted interior window, the hard \(d=y\) floor and endpoint, lower
profile/support crossings near \(d\asymp Rh\), critical points crossing
either window boundary, all remaining nonstationary Poisson integrals,
small heights, the simultaneous \((R,N,y)\) dependence, and the conjugate
sign.  Their coefficient-blind absolute capacity is not target-safe.
Keeping them rather than silently discarding them is precisely why
(138.43) is a self-return diagnostic and not a second reduction.  Near
radicals in (138.46) also remain open.

## 4. First doubtful or unproved step

The first unproved analytic statement is exactly

\[
 \boxed{|{\mathfrak S}_N|\ll_\varepsilon yX^\varepsilon}
\tag{138.48}
\]

for the literal signed survivor (138.3), uniformly for every real \(X\).
No earlier seam in (138.4) is conditional: the scalar dictionary,
diagonal, complete same-denominator sector, exact collision fibres, and
the \(y^{-2}\)-near collision deletion are elementary exact estimates.

In determinant coordinates, the first missing cancellation is joint in
\((G,r,s,\delta,\ell)\).  Summation in \(\ell\) alone cannot provide it:
the phase and \(\chi_4\)-factor are constant there, while (138.29) has
the unavoidable aspect cost \(r+s\) displayed in (138.30).  The safe
summation (138.30a) returns the full \(y^2\) capacity after all labels are
restored.  Taking moduli in \(\delta,G,r,s\), primitive
classes, support endpoints, or lift labels therefore loses the required
factor \(y\) in the square.

Character pairing is owner-complete only up to the exact target-safe
amplitude seam (138.32); its survivor (138.33) has the physical
near-stationary capacity (138.38).  Poisson plus stationary phase is
owner-complete only on the deliberately inserted smooth interior piece.
Its principal term (138.43) has capacity \(R^{3/2}\), and grouping
\(n=hr\) returns the radial problem.  The exact radical channel (138.47)
is safe, but no argument here controls the near-radical or nonsquare
principal modes together with all correction owners.  Claiming the
interior principal term as a full transform, treating its complement as
an error, or taking stationary-mode moduli would be the first invalid
step.

## 5. Required controls and outcomes

| Required control | Analytic test | Outcome |
|---|---|---|
| `literal_flat_cone_to_reduced_farey_scalar` | Reduced \((h,d)=(ag,bg)\) and checked (138.8)--(138.9), including the harmonic factor. | **Pass.** Exact bijection and coefficient. |
| `lift_character_and_b1_centre` | Summed every odd lift into \(L_\chi(y/b)\); even lifts vanish; checked \(J(0)=0\). | **Pass.** No missing multiplicity or centre. |
| `profile_floor_support_and_both_signs` | Used \(ya/b\geq1\), \(a\leq C_Vb/R\), literal \(N,y\), primitive endpoints, and conjugation for the other sign. | **Pass.** Uniform for real \(X\); bounded \(X\) is absorbed. |
| `exact_scalar_square_and_diagonal` | Derived both forms in (138.11) and used reducedness to identify \(\Delta=0\). | **Pass.** Diagonal is \(O(y)\). |
| `same_denominator_unequal_numerators` | Bounded the full row square before subtracting the diagonal. | **Pass.** \(O(y\log^2X)\). |
| `cross_denominator_determinant_arithmetic` | Derived (138.22)--(138.30), including primitive stars and literal support intervals. | **Strict reduction, target open.** The coherent \(\ell\)-direction and lost common-factor character prevent a fibrewise gain. |
| `exact_and_near_phase_one_families` | Classified ordinary and adjusted fibres, proved (138.20)--(138.21), and tested fourth powers and divisor denominators. | **Pass at exact and width \(y^{-2}\).** Wider half-integer tubes have actual \(R^{3/2}\) scalar capacity. |
| `character_pairing_and_stationary_dual_modes` | Derived the exact paired kernel, matched its half-integers to odd Poisson modes, and proved the squarefree-radical channel safe. | **Self-return.** Interior principal modes have \(R^{3/2}\) capacity; near radicals remain open. |
| `scalar_capacity_and_directionality` | Compared \(R^2\) scalar absolute capacity with target \(R\), and \(R^4\) square capacity with target \(R^2\). | **Pass as an audit.** No positive \(k\)-energy or arbitrary-array bound is substituted. |
| `transform_contraction_or_self_return` | Determinant reindexing gives (138.27); unaggregation gives (138.31); interior Poisson gives (138.43). | **No contraction after the strict safe deletions.** Pairing and Poisson return the lower radial kernel. |
| `real_centre_and_boundary_uniformity` | The strict reduction uses integer floors uniformly; the transform obstruction is tested on the required fourth-power subsequence; all unpriced Poisson boundaries are explicitly retained. | **Pass.** No fixed-centre average or hidden endpoint estimate. |
| `lower_GAR_and_downstream_scope` | Traced the possible payoff only through the lower-radial analytic owner. | **Pass.** No blockwise M1, M2, endpoint, M9, quarter, or exponent conclusion follows. |

An adversarial array can of course twist every coefficient by the inverse
carrier and realize essentially the full \(y^2\) square capacity.  That
observation is only a coefficient-uniform false control.  The substantive
obstruction used here is stronger and physical: (138.38) occurs for the
literal \(\chi_4\), harmonic height, multiplier, floors, and fourth-power
centre.  It rules out partial moduli across its stationary packets without
claiming that the actual signed scalar is large.

No numerical experiment, symbolic computation, centre average, or web
theorem was used.

## 6. Dependencies and exact artifacts used

Only the assigned context was used:

- `protocol.md` for proof-state authority, the seven-part contract, and
  the signed-versus-unsigned promotion rule.
- `state/proof_obligations.yml`, restricted to the three Round-138 target
  obligations and their direct dependencies, for the exact owner and
  downstream scope.
- `state/active_campaign.yml` for the frozen scalar, completion labels,
  controls, and zero-percent numerical allocation.
- `strategy/conductor_0823_full_proof_strategy.md` for the standing bans on
  separated positive energies, invertible-transform gains, and unpriced
  stationary modes.
- `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/synthesis.md`
  for the accepted flat-cone equivalence, target normalization, amplitude
  seam, and fourth-power half-integer tube obstruction.
- `rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/synthesis.md`
  for the exact wavelet scale, target-safe packages, and complementary
  self-return.
- `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reports/lower_gar_wavelet_feasibility.md`
  for the rejected separated square function and the earlier reduced-Farey
  dictionary.
- `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reviews/conductor_round127_frontier_selection_adjudication.md`
  for the Round-127 directionality and capacity adjudication.
- `rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/blind_statement.md`
  for the literal Round-138 statement, profiles, and exact target.
- `rounds/codex-managed/m9-m1-lower-gar-signed-farey-scalar-gate/briefs/literal_signed_farey_scalar_attack.md`
  for this task's role, output restriction, and required controls.

No unlisted historical artifact, sibling report, external source, or
computation was used.

## 7. Recommended state effect

**Recommend promotion, after independent seam review, of only the strict
reduction (138.4), its exact scalar/square dictionaries, the complete
same-denominator estimate (138.14), and the ordinary and adjusted carrier
collision bound (138.21).**  The determinant normal form (138.27),
coherent-fibre observation, radical bound (138.47), and explicit Poisson
owner ledger should be retained as scoped supporting evidence.

Keep `M9-M1-global-lower-radial-signed-estimate` open.  The remaining
survivor still needs the full factor \(y\) of cancellation in its exact
square.  Do not promote the interior principal Poisson family as a full
literal transform, and do not infer a target estimate from the safe exact
radical channel.  GAR, the two direct blockwise M1 parents, `M9-M1`, all
three M2 parents, `M9-M2`, endpoint uniformity, `M9`, the quarter theorem,
and both global exponents retain their present owners and statuses.
