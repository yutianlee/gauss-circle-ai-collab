# Round 117 report: actual character and determinant-fibre attack

Campaign: `gc-w7-16-actual-determinant-fibre-gate`
Task: `actual_character_determinant_attack`
Role: discovery
Starting graph SHA-256:
`a27a89fd4e688cae719a28fec8f48dd74190bafb64d0345c590f1caadc2805d9`

## 1. Result

The target bound

\[
 \mathfrak O_i(D,L;c,Y^{7/16})
 \ll_\varepsilon Y^{1/2+\varepsilon}
\tag{117.1}
\]

is **not proved**, and no target-safe part of the hard exponent region is
closed.  A full-block literal numerator/product-window estimate, a sharper
top reduced-denominator estimate, and one scoped transform obstruction are
proved.

Before reduced-ray grouping, sum the numerator inside each random
frequency cell and then count the reciprocal resonances over the original
denominator.  For the complete fixed block this gives

\[
 \boxed{\;
 \mathcal C_i(c)
 \ll_\varepsilon
 \left({D^2\over L^2}+{WD\over L}\right)Y^\varepsilon ,
 \qquad
 |\mathfrak O_i|
 \ll_\varepsilon
 \left({D^2\over L^2}+{WD\over L}\right)Y^\varepsilon .
 \;}
\tag{117.1a}
\]

This retains every lift automatically because it is performed in the
original \((h,d)\) variables.  At minimax (117.1a) is

\[
 \mathcal C_i(c),\,|\mathfrak O_i|
 \ll_\varepsilon Y^{37/48+\varepsilon}.
\tag{117.1b}
\]

It saves \(Y^{1/8}\) from the coefficient-blind \(Y^{43/48}\), but
remains \(Y^{13/48}\) above the target.

First restrict a reduced-denominator shell to \(B\asymp D\).  Then
\(|a|,|a'|\asymp L\), and the lift ranges in both complete coefficients
contain \(O(1)\) integers.  Put

\[
 Q_*=\min\left(D,{D^2\over WL}\right),\qquad
 \lambda={YL\over D^3},\qquad
 V=\min\left(Q_*,Q_*\sqrt\lambda+\lambda^{-1/2}\right).
\tag{117.2}
\]

For both literal M1 and literal M2, including primitivity, all finite
lifts, the one-sided triangular weight, both frequency signs, the fixed
moving-symbol data, hard entry and exit points, and the real centre
\(c\asymp Y\), the top reduced-denominator shell satisfies

\[
 \boxed{\;
 |\mathfrak O_{i,B\asymp D}|
 \ll_\varepsilon D\,V\,Y^\varepsilon .
 \;}
\tag{117.3}
\]

This uses the actual reciprocal centre phase.  It is false for the
phase-conjugated coefficient shadow.  At the minimax point

\[
 D=Y^{1/2},\qquad L=Y^{1/6},\qquad W=Y^{7/16},
\]

one has

\[
 Q_*=Y^{19/48},\qquad
 \lambda=Y^{-1/3},\qquad
 V\ll Y^{11/48},
\]

and therefore

\[
 |\mathfrak O_{i,B\asymp D}|
 \ll_\varepsilon Y^{35/48+\varepsilon}.
\tag{117.4}
\]

The coefficient-blind capacity of this shell is \(DQ_*=Y^{43/48}\).
Thus (117.4) is a genuine \(Y^{1/6}\) saving, but it is still
\(Y^{11/48}\) above (117.1), and all lower reduced-denominator shells
remain open.

Second, the exact M2 numerator high-pass alone gives on the same top
shell

\[
 |\mathfrak O_{2,B\asymp D}|
 \ll_\varepsilon {D^2\over L}Y^\varepsilon .
\tag{117.5}
\]

At minimax this is \(Y^{5/6+\varepsilon}\), a \(D/W=Y^{1/16}\)
saving over the coefficient-blind capacity, but weaker than (117.4).
The corresponding M1 denominator high-pass is already incorporated as
a quarter shift in the proof of (117.3); it does not improve the
second-derivative magnitude.

The one-dimensional savings cannot lawfully be multiplied.  They are two
orientations of the same determinant phase.  At \(B\asymp\sqrt Y\),

\[
 \left|\det\nabla^2_{p,q}
 {c\over\kappa_i}\left({a\over b}-{a+p\over b+q}\right)\right|
 \asymp 1.
\tag{117.6}
\]

After the \(q\)-process, a further \(p\)-process has a full dual range
and restores the capacity that (117.3) saved.  Before reduced-ray
grouping, numerator Poisson turns the two character placements into
dual truncated product waves, but the clean
\(\sum_{d\mid s}\chi_4(d)=r_2(s)/4\) completion is only an unweighted
model.  With the literal truncations and endpoint atoms retained, the
transform is invertible.  Product-window counting gives the full-block
\(Y^{37/48}\) bound (117.1b), but no further cancellation.  The smallest
remaining object is the complete signed truncated divisor-product wave
(117.27) below, equivalently the original one-sided determinant
correlation after its safe diagonal is removed.

## 2. Exact statement and hypotheses

Let \(Y\) be large, let \(c_0Y\le c\le c_1Y\) be real, and let
\(W=Y^{7/16}\).  Fix one moving-symbol stratum and one literal M1 or M2
dyadic block

\[
 d\asymp D,\qquad |h|\asymp L,\qquad
 {1\over4}\le\delta\le{1\over2},\quad
 0\le\ell\le\delta-{1\over4},
\]

where \(D=Y^\delta\), \(L=Y^\ell\), and
\(3\delta-\ell>15/16\).  Reduce \(h/d=a/b\), aggregate every allowed
lift, and retain the exact coefficients

\[
 A_1(a,b)={2\chi_4(b)\over\pi ia}
 \sum_g{\chi_4(g)\over g}U_{1,a,b}(g),
\quad
 A_2(a,b)=-{4\chi_4(|a|)\over\pi|a|}
 \sum_g{\chi_4(g)\over g}U_{2,a,b}(g).
\tag{117.7}
\]

The coefficient functions in (117.7) contain the fixed Vaaler taper,
frequency and denominator profiles, floors, prefix, hard top, and
star.  No coefficient is replaced by an arbitrary bounded sequence.

For the proved saving, restrict both reduced denominators to a fixed
shell \(B\asymp D\).  Then

\[
 b,b'\asymp D,\qquad |a|,|a'|\asymp L,
\tag{117.8}
\]

and the original lift conditions \(gb\asymp D\), \(g|a|\asymp L\)
force \(g=O(1)\).  Expand these finitely many lifts before any norm.
For each fixed lift, the literal sampled profiles, zero-extended at
their support endpoints with their prescribed sampled values retained,
have \(O(1)\) total variation along \(a'\) or \(b'\).  This is a
consequence of the one-variable sampled-BV profiles in the original
\((h,d)\) coefficient, not an asserted BV estimate for a long
unexpanded lift transform.  This bounded-lift restriction is essential.

The off-diagonal is

\[
 \mathfrak O_i=2\Re
 \sum_{\substack{0<n=ab'-a'b<\kappa_i bb'/W\\
                 (a,b)=(a',b')=1}}
 A_i(a,b)\overline{A_i(a',b')}
 e\!\left({cn\over\kappa_i bb'}\right)
 \left(1-{Wn\over\kappa_i bb'}\right),
\tag{117.9}
\]

where \(\kappa_1=1\), \(\kappa_2=4\).  Formula (117.9) is interpreted
with each literal sign sector and support intersection; the displayed
gcd notation means \((|a|,b)=(|a'|,b')=1\).

The exact increment and character chart is

\[
 a'=a+p,\quad b'=b+q,\quad n=aq-bp,
\tag{117.10}
\]

\[
 {cn\over\kappa_i b(b+q)}
 ={ca\over\kappa_i b}-{c(a+p)\over\kappa_i(b+q)},
\tag{117.11}
\]

\[
 \begin{array}{ll}
 {\rm M1}:&q=2r,\quad
 \chi_4(b)\chi_4(b')=(-1)^r,\\[1mm]
 {\rm M2}:&p=2s,\quad
 \chi_4(|a|)\chi_4(|a'|)
   =\epsilon_{\rm sgn}(-1)^s .
 \end{array}
\tag{117.12}
\]

Here \(\epsilon_{\rm sgn}=1\) on the two same-sign sectors and is a
fixed minus sign on an opposite-sign sector.  This harmless fixed sign
must not be confused with deletion of that sector.

For fixed \((a,b,p)\), the one-sided determinant strip cuts the
\(b'\)-shell into \(O(1)\) intervals of total length

\[
 O(1+Q_*),\qquad
 Q_*=\min\left(D,{D^2\over WL}\right).
\tag{117.13}
\]

For fixed \((a,b,b')\), it cuts the \(a'\)-support into \(O(1)\)
intervals of total length

\[
 O(1+T),\qquad T=\min\left(L,{D\over W}\right).
\tag{117.14}
\]

The triangular factor has \(O(1)\) total variation on each such
interval.  These clipped widths cover same-sign and opposite-sign
sectors and all block-boundary intersections.

## 3. Proof or derivation

### Full-block numerator/product-window estimate

Work before reduced-ray grouping.  On one positive-frequency M1 cell
\(I\), the scalar is exactly

\[
 S_{1,I}(c)=C_1\sum_{d\asymp D}\chi_4(d)\omega_{1,D}(d)
 \sum_{h/d\in I}{F_1(h,d)\over h}e(ch/d),
\tag{117.14a}
\]

and M2 has the same form with \(h/(4d)\in I\), phase
\(e(ch/(4d))\), and numerator character \(\chi_4(h)\).  For fixed
\(d\), the intersection of one cell with the literal numerator support
is a union of \(O(1)\) integer intervals of total length

\[
 T_0\ll \min\left(L,{D\over W}\right)
\tag{117.14b}
\]

up to the harmless factor four for M2.  After extracting \(L^{-1}\),
the sampled numerator weight on each interval has bounded supremum plus
bounded total variation.  This includes the Vaaler taper, dyadic
profile, clipped hard top, and its prescribed endpoint sample.

Abel summation and the geometric progression formula therefore give

\[
 \left|\sum_{h/d\in I}{F_1(h,d)\over h}e(ch/d)\right|
 \ll {1\over L}
 \min\left(T_0,{1\over\|c/d\|}\right)
\tag{117.14c}
\]

for M1.  For M2, use
\(\chi_4(h)=(e(h/4)-e(-h/4))/(2i)\); the right side is the sum of the
two analogous terms

\[
 {1\over L}
 \min\left(T_0,{1\over\|c/(4d)\pm1/4\|}\right).
\tag{117.14d}
\]

Uniformly for real \(c\asymp Y\),

\[
 \sum_{d\asymp D}
 \min\left(T_0,{1\over\|c/d\|}\right)
 +
 \sum_{d\asymp D}
 \min\left(T_0,{1\over\|c/(4d)\pm1/4\|}\right)
 \ll_\varepsilon D\,Y^\varepsilon .
\tag{117.14e}
\]

To prove (117.14e), dyadically count the denominators for which the
relevant norm is \(<\eta\).  In M1, an integer \(r\) then satisfies
\(|c-rd|\ll\eta D\).  In M2 the same statement holds with
\(r\equiv\pm1\pmod4\).  The real interval of possible integer products
\(rd\) has \(O(1+\eta D)\) integers, and each integer has
\(O_\varepsilon(Y^\varepsilon)\) divisors.  Layer-cake summation from
\(\eta=T_0^{-1}\) to \(1/2\) proves (117.14e).  No integrality of
\(c\) is used.

Taking the denominator triangle only after (117.14c)--(117.14e) gives

\[
 |S_{i,I}(c)|\ll_\varepsilon {D\over L}Y^\varepsilon .
\tag{117.14f}
\]

The signed frequency band meets
\[
 J\ll 1+{WL\over D}
\]
cells, uniformly in the random shift.  Both signs cost only a constant.
Consequently

\[
 \mathcal C_i(c)
 \ll_\varepsilon J{D^2\over L^2}Y^\varepsilon
 \ll_\varepsilon
 \left({D^2\over L^2}+{WD\over L}\right)Y^\varepsilon .
\tag{117.14g}
\]

The exact identity
\(\mathcal C_i=\mathcal E_{i,=}+\mathfrak O_i\), with
\(\mathcal E_{i,=}\ll D/L\), also gives the absolute bound for
\(\mathfrak O_i\) in (117.1a).  This proof contains the complete
original lift multiplicity; no liftwise or reduced-ray absolute value
has occurred.

### Top-shell coefficient decomposition

On (117.8), write every complete lift sum in (117.7) as a sum over a
fixed finite set of \(g\)'s, extending each sampled profile by zero.
For fixed \(a'\), each resulting \(b'\)-weight has supremum and total
variation \(O(L^{-1})\); for fixed \(b'\), each resulting
\(a'\)-weight has the same bound.  A support entry or exit, a hard-top
sample, or a star contributes one of the finitely many jumps already
counted in this variation.

Primitivity is not suppressed.  In a \(b'\)-sum use

\[
 {\bf1}_{(a',b')=1}
 =\sum_{\rho\mid a',\,\rho\mid b'}\mu(\rho),
\tag{117.15}
\]

and write \(b'=\rho v\).  In an \(a'\)-sum use the same identity with
\(\rho\mid b'\) and write \(a'=\rho u\).  Only odd \(\rho\) occur in
the character-bearing M1 or M2 progression.  The number and reciprocal
sum of the divisors of a fixed integer cost \(Y^\varepsilon\).

### Reciprocal \(q\)-sum

Fix \(a,b,p\), so \(a'=a+p\) is fixed.  Apart from the constant
\(e(ca/(\kappa_i b))\), the phase is

\[
 f(b')=-{ca'\over\kappa_i b'}.
\tag{117.16}
\]

For M1, \(\chi_4(b')\) is split exactly as

\[
 \chi_4(b')={e(b'/4)-e(-b'/4)\over2i};
\tag{117.17}
\]

for M2 no \(b'\)-character is inserted.  After (117.15), the phase on
\(v\asymp D/\rho\) has

\[
 |f_\rho''(v)|
 \asymp {Y L\rho^2\over D^3}
 =\lambda\rho^2.
\tag{117.18}
\]

The linear quarter shifts in (117.17) do not change (117.18).

The elementary weighted second-derivative estimate says that, on an
interval of length \(N\), if
\(\Lambda\asymp|f''|\) and \(f''\) is monotone, then

\[
 \left|\sum_n w(n)e(f(n))\right|
 \ll(\|w\|_\infty+\operatorname{Var}w)
 \left(N\sqrt\Lambda+\Lambda^{-1/2}\right).
\tag{117.19}
\]

It follows by Weyl differencing with
\(H=\min(N,\lceil\Lambda^{-1/2}\rceil)\); Abel summation gives the
weighted form.  Apply (117.19) on the \(O(1)\) clipped intervals of
length \(Q_*/\rho\).  Equations (117.18)--(117.19) give

\[
 {1\over L}\left(
 Q_*\sqrt\lambda+{1\over\rho\sqrt\lambda}\right)
\tag{117.20}
\]

for one divisor progression.  Progressions shorter than one contain
at most one integer and are covered by the same final minimum with the
trivial estimate.  Summing \(\rho\mid a'\), and also retaining the
trivial \(Q_*/L\) bound, gives

\[
 \sum_{\substack{b'\ {\rm in\ the\ strip}\\(a',b')=1}}
 \overline{A_i(a',b')}
 e\!\left(-{ca'\over\kappa_i b'}\right)
 \left(1-{Wn\over\kappa_i bb'}\right)
 \ll_\varepsilon {V\over L}Y^\varepsilon .
\tag{117.21}
\]

There are \(O(LD)\) outer rays in the shell and \(O(L)\) possible
values of \(p\); the outer coefficient has size \(O(L^{-1})\).
Therefore (117.21) costs

\[
 (LD)\cdot L\cdot L^{-1}\cdot {V\over L}
 =DV,
\]

which proves (117.3).  Notice that every Cauchy or triangle factor is
visible here: the final triangle is over the \(O(LD)\) outer rays and
the \(O(L)\) numerator increments, after the literal oscillatory
\(b'\)-sum has been estimated.

At minimax,
\(\lambda=Y^{-1/3}\) and
\[
 Q_*\sqrt\lambda=Y^{11/48},\qquad
 \lambda^{-1/2}=Y^{8/48}.
\]
This proves (117.4).  If the inner coefficient is replaced by
\(L^{-1}e(ca'/(\kappa_i b'))\), then (117.16) is cancelled and the
inner sum has length \(Q_*\).  Thus (117.3) uses a literal feature
unavailable to the phase-conjugated adversary.

### Exact M2 \(p\)-high-pass and product-window count

Fix \(a,b,b'\) in M2 and sum over \(a'\).  On a fixed sign sector,
the product of the centre phase and the numerator character has
successive-\(s\) ratio

\[
 e\!\left({1\over2}-{c\over2b'}\right),
\qquad a'=a+2s.
\tag{117.22}
\]

After (117.15), write \(b'=\rho v\), \(a'=\rho u\).  The phase in
\(u\) is \(-cu/(4v)\), while \(\chi_4(u)\) supplies the shifts
\(\pm1/4\).  The interval length is at most \(T/\rho\).

For \(B_0,T_0\ge1\), \(T_0\le B_0\), the following uniform
product-window estimate is elementary:

\[
 \sum_{v\asymp B_0}
 \min\left(T_0,
 {1\over\|c/(4v)\pm1/4\|}\right)
 \ll_\varepsilon (B_0+T_0)Y^\varepsilon .
\tag{117.23}
\]

Indeed, if the norm is \(<\eta\), an odd integer \(r\) in one fixed
class modulo \(4\) satisfies

\[
 |c-rv|\ll\eta B_0.
\]

There are \(O(1+\eta B_0)\) integers in this product window and each
has \(O_\varepsilon(Y^\varepsilon)\) divisor pairs.  Dyadic
decomposition in \(\eta\) proves (117.23).

For \(\rho\le T\), apply (117.23) with
\((B_0,T_0)=(D/\rho,T/\rho)\); for \(\rho>T\), the \(u\)-interval
contains at most one point and the direct count is \(O(D/\rho)\).
Summing \(\rho\ll L\) costs only a logarithm.  Hence, for each outer
ray,

\[
 \sum_{b'}\left|
 \sum_{\substack{a'\ {\rm in\ the\ strip}\\(a',b')=1}}
 \overline{A_2(a',b')}
 e\!\left(-{ca'\over4b'}\right)\right|
 \ll_\varepsilon {D\over L}Y^\varepsilon .
\tag{117.24}
\]

The \(O(LD)\) outer rays have total absolute coefficient mass
\(O(D)\), proving (117.5).  This charges the gcd congruences, the
character sectors, every finite lift, all interval endpoints, and the
geometric-sum factor.  It also shows exactly why the high-pass alone is
insufficient.

### Why the two orientations do not multiply

For fixed \((a,b)\), the full increment phase has

\[
 \det\nabla^2_{p,q}\phi
 =-{c^2\over\kappa_i^2(b+q)^4}.
\tag{117.25}
\]

At \(b+q\asymp D\asymp\sqrt Y\), this is bounded above and below by
positive constants.  In the \(q\)-process, the M1 character shifts the
dual lattice by \(1/4\); M2 has the analogous shift in the \(p\)
coordinate.  The \(q\)-dual phase is a square-root phase.  Its
\(p\)-curvature has a full dual range of order \(D\), so a second
B-process repays the \(q\)-saving.  Equivalently, the two-dimensional
stationary map has unit-order Jacobian and preserves the increment-strip
area.  Taking absolute values after that second transform returns the
coefficient-blind capacity \(DQ_*\).  This is a scoped no-go for
sequential B-process/aliaswise-triangle arguments, not a lower bound for
the actual joint sum.

### Cellwise product return

For a positive M1 cell \(I=[x,x+W^{-1})\), symmetric Poisson summation
in the original numerator gives, with the exact sampled endpoint atoms
retained,

\[
 S_{1,I}(c)=C_1\sum_s\int_I
 {e((c-s)y)\over y}
 \sum_{d\mid s}\chi_4(d)F_1(dy,d)\,dy+\mathcal E_{1,I}.
\tag{117.26}
\]

For M2, using
\(\chi_4(h)=(e(h/4)-e(-h/4))/(2i)\), the modes are
\(r=4m\pm1\), and

\[
 S_{2,I}(c)=C_2\sum_s\int_I
 {e((c-s)y)\over y}
 \sum_{\substack{rd=s\\r\ {\rm odd}}}
 \chi_4(r)F_2(4dy,d)\,dy+\mathcal E_{2,I}.
\tag{117.27}
\]

Cell endpoints occur only for a measure-zero set of random shifts.
The terms \(\mathcal E_{i,I}\) are the exact fixed profile/hard-top/star
endpoint atoms required when a prescribed sampled value differs from
the symmetric Poisson value.  They are retained, not declared
target-safe.  On every smooth interior subpacket they vanish.

Without the \(d\)- and \(r\)-truncations and without the profiles, both
inner coefficients equal

\[
 \sum_{d\mid s}\chi_4(d)={r_2(s)\over4}.
\tag{117.28}
\]

In the literal block, however, (117.26) and (117.27) are different
truncated weighted orientations, and the omitted divisor orientations
have no supplied target-safe bound.  Thus (117.28) is not a legal
completion.

At minimax \(D>W\).  The band meets
\[
 J\asymp {WL\over D}=Y^{5/48}
\]
cells.  Taking every Poisson alias separately would allow \(O(D)\)
denominator-mode pairs, each at scale \(D/(LW)\), and would return the
old \(Y^{43/48}\) capacity.  That aliaswise triangle is unnecessary:
the finite numerator sum, equivalently the symmetrically resummed product
windows, obeys (117.14e).  Thus one cell costs \(D/L\), and the proved
transformed capacity is

\[
 J\left({D\over L}\right)^2
 ={WD\over L}
 =Y^{37/48}.
\tag{117.29}
\]

Poisson inversion, with the endpoint atoms included, returns the
original cell sum.  Thus Poisson alone is an exact self-return;
the noninvertible input in (117.29) is the product-window divisor count.
It proves (117.1a), but it still leaves the signed object

\[
 \int_0^1\sum_\nu\left|
 \sum_s\int_{I_{\nu,\vartheta}}
 {e((c-s)y)\over y}\,B_i(s;y)\,dy
 +\mathcal E_{i,\nu,\vartheta}
 \right|^2d\vartheta ,
\tag{117.30}
\]

where \(B_i\) is the complete literal truncated coefficient in
(117.26) or (117.27).  Subtracting the already-owned equal-ray
diagonal makes (117.30) exactly the one-sided determinant target.
No \(Y^{1/2}\) estimate for (117.30) is proved.

## 4. First doubtful or unproved step

After the proved top-shell saving (117.3), the first unproved step is a
joint signed inequality saving a further \(Y^{11/48}\) at minimax
without applying a second capacity-restoring transform.  It must keep
together:

* the \(O(L)\) numerator increments rather than taking their triangle
  after (117.21);
* the quarter-shifted reciprocal dual modes;
* both primitive congruence expansions and all lift signs;
* the one-sided triangular projector and its clipped endpoints; and
* the actual moving profiles.

The lower reduced-denominator shells have an earlier seam.  There the
lift range \(G=D/B\) is long.  Round 95 supplies cancellation and
sampled BV in \(g\), but not a \(B\)-uniform \(b'\)-variation theorem
for the fully aggregated lift transform.  Taking liftwise absolute
values loses \(G\), while endpoint entry and exit of \(g b'\) can have
total absolute variation of that size.  Thus (117.3) is not extended
to \(B<D\).

For the product-return route, the first unproved assertion is a
\(Y^{1/2+\varepsilon}\) bound for the augmented truncated wave
(117.30); (117.1a) stops at \(Y^{37/48+\varepsilon}\), leaving
\(Y^{13/48}\).  Replacing it by \(r_2(s)/4\), deleting endpoint atoms, or
estimating divisor orientations separately is not a proof.  The
Poisson identity itself is invertible and supplies no norm gain.

## 5. Control tests and outcomes

| Control | Test and charged factors | Outcome |
|---|---|---|
| Literal reduced ray and equal-lift diagonal | Use (117.7) only after summing every lift; keep the accepted \(\sum|A_i|^2\ll D/L\). | Pass.  The diagonal stays owned and is not re-counted in (117.3). |
| M1/M2 placement and factor four | Check (117.11)--(117.12), (117.17), and the M2 ratio (117.22). | Pass.  M1 shifts \(q\); M2 shifts \(p\); \(\kappa_2=4\) is retained. |
| Increment and orientation | Derive \(n=aq-bp\) and solve the two strict one-sided inequalities before clipping to support. | Pass.  They give (117.13)--(117.14), each a union of \(O(1)\) intervals. |
| Character high-pass progression | Use \(q=2r\) in M1 and \(p=2s\) in M2, including the fixed opposite-sign-sector sign. | Pass.  No parity sector is silently discarded. |
| Strip widths and boundary | Compare \(Q_*=\min(D,D^2/(WL))\), \(T=\min(L,D/W)\), and count profile/support endpoints in BV. | Pass on \(B\asymp D\).  Every entry/exit is charged once. |
| Centre phase | Apply (117.19) to \(-ca'/(\kappa b')\) with \(\lambda=YL/D^3\). | Pass.  At minimax it gives \(Y^{1/6}\) saving. |
| Gcd congruence and multiplicity | Expand (117.15); use divisor progressions and \(\tau,\sigma_{-1}\ll Y^\varepsilon\). | Pass.  No coprimality density heuristic is used. |
| Capacity after each norm | Full coefficient-blind: \(Y^{43/48}\).  Full numerator/product window: \(Y^{37/48}\).  Top-shell \(q\)-sum: \(DV=Y^{35/48}\).  M2 \(p\)-sum: \(D^2/L=Y^{40/48}\). | Pass.  None reaches \(Y^{24/48}\). |
| Poisson/B-process factors | \(q\)-progression length \(Q_*/\rho\), curvature \(\lambda\rho^2\), hence \(Q_*\sqrt\lambda+(\rho\sqrt\lambda)^{-1}\). | Pass.  The quarter shift changes aliases, not amplitude. |
| Actual versus phase-conjugated coefficients | Insert \(e(ca'/(\kappa b'))\) into a bounded shadow coefficient. | Required failure: it deletes (117.16), restores length \(Q_*\), and invalidates the saving. |
| Long lift seam | Let \(B<D\), so \(G=D/B\to\infty\), and take absolute endpoint variation of the \(g\)-sum. | Open.  It can lose \(G\); (117.3) is not claimed there. |
| Two-dimensional transform | Evaluate (117.25) at \(D=\sqrt Y\) and charge the full second dual range. | Scoped fail: sequential transform plus dual triangle returns \(DQ_*\). |
| Product completion | Compare (117.26)--(117.27) with (117.28), retaining truncations and endpoint atoms. | Clean \(r_2/4\) completion fails.  The augmented transform is exact; the noninvertible product-window count proves only \(Y^{37/48}\). |
| Real \(Y,c\) and endpoints | Use only \(c\asymp Y\); the product-window count uses integers \(rv\) in a real interval around \(c\). | Pass.  No integrality of \(Y\) or \(c\) is assumed. |
| Moving strata, bottom, R5, cross blocks | Keep (117.1a) on one complete fixed block and (117.3) on one shell; use no cancellation across owners or blocks. | Pass in scope.  Accepted bottom/R5 ownership is unchanged; cross-block assembly is not claimed. |
| Local mass and exponent | Compare \(Y^{37/48}\) and \(Y^{35/48}\) with \(Y^{1/2}\), then with the accepted \(W Y^{1/2}=Y^{15/16}\) local mass bridge. | No implication.  Both proved savings remain above the fixed-block target and prove no new pointwise exponent. |
| Downstream scope | Compare variables and norm with M9-M1/M9-M2 physical parents. | No implication to either M9 component, endpoint uniformity, M9, or the quarter theorem. |

All controls are analytic.  No numerical experiment and no external
theorem were used.

## 6. Dependencies and exact artifacts used

This report used the assigned brief and every permitted context file:

1. `protocol.md`, for graph authority, signed/unsigned separation,
   campaign discipline, and the seven-section contract;
2. `state/proof_obligations.yml`, for the exact status and scope of
   `GC-W7-16-actual-reduced-determinant-correlation`,
   `GC-nonsubcoherent-actual-cluster-local-moment`,
   `GC-one-sided-persistence-local-bridge`, M9-M1, and M9-M2;
3. `state/active_campaign.yml`, for the frozen question, hard region,
   capacities, controls, and graph hash;
4. `strategy/conductor_0821_full_proof_strategy.md`, for the graded-lane
   scope and the prohibition on another unpriced invertible mechanism;
5. `rounds/codex-managed/gc-prescribed-point-local-moment-bridge/reviews/conductor_round94_local_kernel.md`,
   for the exact triangular/random-cell kernel, literal frequencies,
   moving strata, and persistence scope;
6. `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/reports/actual_rational_cluster_attack.md`,
   for the complete lift formulas, sampled profiles, exact determinant
   reduction, all-block capacity, and phase-conjugated control;
7. `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/reviews/conductor_round95_cluster_adjudication.md`,
   for the accepted diagonal, hard region, owners, and downstream
   nonimplications;
8. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/derivation_packet.md`,
   for (117.D1)--(117.D15);
9. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/candidates/conductor_character_highpass_fibre.md`,
   for the proposed progression, curvature, and coefficient seams; and
10. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/candidates/conductor_cellwise_product_return.md`,
    received as a conductor diagnostic and audited in
    (117.26)--(117.30).

The only analytic tools added are the elementary second-derivative
estimate (117.19), Möbius inversion, divisor bounds, Abel summation,
and the product-window count proved above.  No web source, sibling
Round-117 report, or computation was used.

## 7. Recommended state effect

**Promote after independent seam review** the full-block
numerator/product-window estimate (117.1a).  Record its minimax
\(Y^{37/48+\varepsilon}\) capacity as a \(Y^{1/8}\) literal
centre-phase saving from the coefficient-blind \(Y^{43/48}\), not as a
target estimate.

**Promote after independent seam review** the bounded-lift top-shell
lemma (117.3), with its exact hypotheses \(B\asymp D\), frozen literal
stratum, finite lift expansion, and clipped widths.  Record its minimax
consequence (117.4) as a \(Y^{1/6}\) actual-centre-phase saving from
\(Y^{43/48}\) to \(Y^{35/48}\), not as a target estimate.

**Promote after seam review** the M2 progression product-window lemma
(117.23)--(117.5) as a weaker but exact character-high-pass diagnostic,
and the scoped no-go that this \(p\)-saving cannot be multiplied with a
second \(q\)-B-process by aliaswise absolute values at unit Hessian
determinant.

**Retain open** `GC-W7-16-actual-reduced-determinant-correlation`.
Its first complete survivor may be recorded as the augmented literal
truncated divisor-product norm (117.30).  The full-block deficit is
\(Y^{13/48}\), while the sharper top-shell phase-curvature deficit is
\(Y^{11/48}\) at minimax; the long-lift lower shells prevent extension
of that sharper shell estimate.

**Reject** the clean literal identification with \(r_2(s)/4\), deletion
of Poisson endpoint atoms, multiplication of the two one-dimensional
savings, and any coefficient-blind two-dimensional stationary transform
as a proof of the target.  These are capacity-returning operations once
their omitted data are restored.

**No change** is licensed for the complete local moment, the internal
pointwise exponent, M9-M1, M9-M2, endpoint uniformity, M9, or the Gauss
circle quarter target.
