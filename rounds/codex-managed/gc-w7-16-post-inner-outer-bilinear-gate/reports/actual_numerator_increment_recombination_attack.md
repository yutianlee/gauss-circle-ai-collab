# Round 130 report: exact numerator--reciprocal recombination returns the original product wave at the top shell

Campaign: `gc-w7-16-post-inner-outer-bilinear-gate`
Task: `actual_numerator_increment_recombination_attack`
Role: discovery
Starting graph SHA-256:
`354f5ca462467d091a9a50c8dbc1173ffba56516963274f9fc232ea11890d20e`
Status: candidate evidence only; no shared proof state is changed.

## 1. Result

No complete target estimate and no strict fixed-power saving over the
accepted

\[
 D K_B=Y^{35/48+\varepsilon}
 \tag{130.1}
\]

are proved.  There are, however, three exact conclusions.

First, the literal post-inner numerator--reciprocal--threshold scalar can
be written before every outside modulus as

\[
\boxed{
\begin{aligned}
 \mathfrak O_{i,B}^{+}
 ={}&\sum_{r=(a,b)}^{\rm lit}
 A_i(a,b)e\!\left({ca\over\kappa_i b}\right)
 \sum_{p}^{\rm lit}\sum_{\rho\mid a+p}
 \sum_{\eta\in\mathcal E_i}\sum_v^{*}
 \zeta_{i,\rho,\eta}(a+p)\,
 T_{i;r,p,\rho,B}(v)                                      \\[1mm]
 &\quad\times\sum_t c_{i,t}
 \sum_{g\le t/(\rho v)}^{*}
 {\chi_4(g)\over g}P_{i,a+p}(g)
 e\!\left(-{c(a+p)\over\kappa_i\rho v}
           +\vartheta_{i,\eta}\rho v\right).
\end{aligned}}
\tag{130.2}
\]

Here $a'=a+p$, $b'=\rho v$, and every determinant, profile,
threshold, equality, support, sign, cell, and owner condition is in the
displayed factors, as specified precisely in Section 2.  No $p$-,
$v$-, threshold-, divisor-, or outer-ray triangle has been taken in
(130.2).

Second, literal reduced-numerator support improves the accepted shell
ledger.  If $b'\asymp B$, then

\[
 g\asymp {D\over B},\qquad |a'|\asymp {LB\over D},
 \qquad \#\{a'\}\ll 1+{LB\over D}\ll {LB\over D}.
\tag{130.3}
\]

Combining (130.3), the accepted outer facts

\[
 \#\{r\}\ll LD,\qquad
 \sum_r|A_i(r)|^2\ll {D\over L},
\tag{130.4}
\]

and the Round-129 branchwise theorem gives the rigorous shell refinement

\[
 \boxed{\;|\mathfrak O_{i,B}^{+}|
       \ll_\varepsilon B K_B Y^\varepsilon.\;}
\tag{130.5}
\]

At the critical scales, $K_B\asymp Y^{11/48+o(1)}$.  Thus a shell
$B=Y^b$, $16/48\le b\le24/48$, costs

\[
 Y^{b+11/48+\varepsilon}.
\tag{130.6}
\]

This is a genuine factor $B/D$ improvement over the deliberately crude
per-shell $D K_B$ ledger whenever $B<D$.  It localizes the complete
residual to $B\asymp D$, but it gives no complete fixed-power saving:
the logarithmic half-open shell sum is still dominated by

\[
 B\asymp D:\qquad B K_B\asymp D K_B=Y^{35/48}.
\tag{130.7}
\]

Third, on this remaining top shell, recombining $p$ with $v$ by each
of the available exact mechanisms self-returns at a capacity no smaller
than the accepted one.

* Undoing the Stieltjes and Mobius expansions and then the complete-lift
  grouping returns exactly the original ((h',d')) numerator/product
  wave.  The selected-context product-window theorem gives
  $Y^{37/48+\varepsilon}$, which is worse than (130.1) by $Y^{1/24}$.
* Summing the top-shell $p$-interval first and then putting the
  reciprocal variable in modulus gives

  \[
   \sum_{b'\asymp D}\min\!\left({D\over W},
          \|c/b'\|^{-1}\right)
   +\sum_{\pm}\sum_{b'\asymp D}
       \min\!\left({D\over W},
          \|c/(4b')\pm1/4\|^{-1}\right)
   \ll_\varepsilon D Y^\varepsilon,
  \tag{130.8}
  \]

  and hence the outer-triangle capacity $D^2/L=Y^{40/48}$.
* Keeping both variables and applying sequential two-dimensional
  transforms does not multiply the one-variable savings.  For
  $q=b'-b$, the exact ratio phase has unit-order Hessian determinant on
  $B\asymp D=\sqrt Y$; the M1 and M2 quarter characters merely translate
  one dual lattice coordinate.  Aliaswise modulus after the full
  transform returns $D Q_*=Y^{43/48}$.

The smallest rigorous conclusion is therefore a scoped no-go: after the
Round-129 $K_B/L$ theorem, neither exact inversion to the original
product wave, a $p$-first product-window estimate, nor a sequential
unit-Hessian transform followed by a positive norm yields a strict saving
over $D K_B$.  This is not a lower bound for the physical scalar.  The
first open object is the literal signed top-shell scalar (130.2); it needs
an actual correlation between numerator increments (and possibly outer
rays) and the thresholdwise reciprocal aliases before any positive norm.

## 2. Exact statement and hypotheses

Fix

\[
 W=Y^{7/16},\qquad D=Y^{1/2},\qquad L=Y^{1/6},
 \qquad {D\over L}\le B\le D,
\tag{130.9}
\]

one literal M1 or M2 block, one fixed moving-symbol stratum, one frequency
sign and M2 product-sign sector, one half-open inner reduced-denominator
shell, and a real centre $c\asymp Y$.  Let

\[
 \kappa_1=1,\qquad \kappa_2=4,
\tag{130.10}
\]

and retain the complete outer ray coefficients

\[
\begin{aligned}
 A_1(a,b)&=\chi_4(b){2\over\pi ia}
 \sum_{g\ge1}^{*}{\chi_4(g)\over g}
 P_{1,a}(g)\omega_{1,D}^{*}(gb;c),\\
 A_2(a,b)&=-{4\chi_4(|a|)\over\pi|a|}
 \sum_{g\ge1}^{*}{\chi_4(g)\over g}
 P_{2,a}(g)\omega_{2,D}^{*}(gb;c).
\end{aligned}
\tag{130.11}
\]

The notation $P_{i,a}$ contains the exact fixed Vaaler taper, frequency
profile, frequency floor, zero-extended support, and prescribed star.
The denominator sample has the exact discrete Stieltjes representation

\[
 c_{i,t}=\omega_{i,D}^{*}(t;c)-\omega_{i,D}^{*}(t+1;c),
 \qquad
 \omega_{i,D}^{*}(d;c)=\sum_{t\ge d}^{*}c_{i,t},
 \qquad \sum_t|c_{i,t}|\ll1.
\tag{130.12}
\]

Complex conjugation in the off-diagonal may conjugate the fixed profiles
and $c_{i,t}$; it does not change their support, sampled variation, or
Stieltjes mass.

For an outer primitive ray $r=(a,b)$, write

\[
 a'=a+p,\qquad b'=\rho v,\qquad \rho\mid a+p.
\tag{130.13}
\]

The exact determinant is

\[
 n=a\rho v-b(a+p).
\tag{130.14}
\]

Define

\[
\begin{aligned}
 T_{i;r,p,\rho,B}(v)
 ={}&{\bf1}^{\rm lit}_{\,0<a\rho v-b(a+p)<
                       \kappa_i b\rho v/W}
 \left(1-{W\{a\rho v-b(a+p)\}
              \over\kappa_i b\rho v}\right)\\
 &\times {\bf1}^{\rm owner}_{\rho v\asymp B}
 \;{\bf1}^{\rm lit}_{\rm cell,sign,original\ support,cross\ shell}(p,v).
\end{aligned}
\tag{130.15}
\]

The last factor is notation, not a discarded error: it retains the exact
fixed random-cell face, sign sector, original support intersections,
strict/weak conventions, and the unique half-open shell owner.  On each
of $O(1)$ clipped intervals in $v$, the zero-extended multiplier in
(130.15) has bounded supremum plus variation.  Numerator support exits and
frequency stars remain instead in $P_{i,a+p}(g)$.

The branch dictionary is

\[
 \mathcal E_1=\{+,-\},\qquad \mathcal E_2=\{0\},
\tag{130.16}
\]

\[
\begin{array}{c|c|c}
 (i,\eta)&\vartheta_{i,\eta}&\zeta_{i,\rho,\eta}(a+p)\\ \hline
 (1,+)& 1/4& \mu(\rho)/(\pi(a+p))\\
 (1,-)&-1/4&-\mu(\rho)/(\pi(a+p))\\
 (2,0)&0&-4\mu(\rho)\epsilon_{\rm sgn}
          \chi_4(|a+p|)/(\pi|a+p|).
\end{array}
\tag{130.17}
\]

These are the real-profile constants; under complex notation one
conjugates the fixed factors only.  In M1 the outer reduced character
$\chi_4(b)$ stays in $A_1$, the inner reduced character
$\chi_4(\rho v)$ is exactly the difference of the two carrier phases
$e(\pm\rho v/4)$, and the common lift character remains in the $g$-sum.
In M2 the outer $\chi_4(\lvert a\rvert)$ stays in $A_2$, while the inner
$\chi_4(\lvert a+p\rvert)$ stays in $\zeta_{2,\rho,0}$; the fixed
$\epsilon_{\rm sgn}$ records the product-sign sector.

With these definitions, (130.2) is the exact one-oriented scalar.  The
real off-diagonal is

\[
 \mathfrak O_i=2\Re\sum_B\mathfrak O_{i,B}^{+}.
\tag{130.18}
\]

No conjugate orientation is also placed inside (130.2).  The equal-ray
case $n=0$ is the separately owned diagonal
$\sum_r\lvert A_i(r)\rvert^2\ll D/L$ and is not counted in (130.2).

For the literal $p$-$v$ geometry, put

\[
 a+p=\rho u.
\tag{130.19}
\]

Then before a modulus the complete carrier is

\[
 \Phi_{i,\eta}(u,v)
 ={ca\over\kappa_i b}-{cu\over\kappa_i v}
  +\vartheta_{i,\eta}\rho v,
\tag{130.20}
\]

and the determinant gate is exactly

\[
 0<av-bu<{\kappa_i b v\over W},
\qquad
 {av\over b}-{\kappa_i v\over W}<u<{av\over b}.
\tag{130.21}
\]

Equivalently, the $p$-interval at fixed $v$ is

\[
 {a\rho v\over b}-a-{\kappa_i\rho v\over W}
 <p<
 {a\rho v\over b}-a,
 \qquad p\equiv-a\pmod\rho.
\tag{130.22}
\]

Equations (130.2), (130.12), and (130.20)--(130.22) are the requested
literal post-inner $p$-$v$-threshold formula.  The inner
strict/weak/star equality is the set $t=\rho vg$, not the determinant
diagonal $n=0$; the two owners are distinct.

## 3. Proof or derivation

### 3.1 Derivation of the exact joint scalar

Start from the accepted one-sided reduced determinant sum and factor its
centre phase:

\[
 e\!\left({c\{ab'-a'b\}\over\kappa_i bb'}\right)
 =e\!\left({ca\over\kappa_i b}\right)
  e\!\left(-{ca'\over\kappa_i b'}\right).
\tag{130.23}
\]

Set $a'=a+p$.  Insert primitivity only through the exact identity

\[
 {\bf1}_{(a',b')=1}
 =\sum_{\rho\mid a',\ \rho\mid b'}\mu(\rho),
 \qquad b'=\rho v.
\tag{130.24}
\]

Insert (130.12) into the complete inner lift coefficient.  In M1 split
the reduced denominator character before forming an amplitude:

\[
 \chi_4(\rho v)
 ={e(\rho v/4)-e(-\rho v/4)\over2i}.
\tag{130.25}
\]

In M2 leave $\chi_4(\lvert a+p\rvert)$ in its literal numerator coordinate.  The
common $\chi_4(g)$, the lift endpoint $g\le t/(\rho v)$, and the
frequency profile $P_{i,a+p}(g)$ remain together.  Finally put every
determinant and owner factor in (130.15).  These algebraic substitutions
give (130.2) with (130.17).  Substitution of (130.19) gives (130.20) and
division of (130.14) by $\rho b$ gives (130.21)--(130.22).

This derivation has not used a norm.  In particular, the Round-129 order
of operations remains available inside (130.2): freeze $t$, Abel-sum
the common lift character, partition $v$ by
$\lfloor t/(\rho v)\rfloor$, apply reciprocal curvature, and only then
sum the Stieltjes mass.  The present report changes only the placement of
the still-unsummed $p$-variable.

### 3.2 Exact threshold and character recombination

The joint formula exposes why the literal characters do not provide two
independent transverse high-passes.  At a threshold equality

\[
 t=\rho vg,
\tag{130.26}
\]

the phase in (130.2) is

\[
 {ca\over\kappa_i b}
 -{c(a+p)g\over\kappa_i t}
 +{\vartheta_{i,\eta}t\over g}.
\tag{130.27}
\]

For M1, summing the two exact branches in (130.17) turns the last factor
in (130.27) into $\chi_4(t/g)=\chi_4(b')$.  Multiplication by the common
lift character gives

\[
 \chi_4(g)\chi_4(b')=\chi_4(gb')=\chi_4(t),
\tag{130.28}
\]

with zero even samples reconstructed automatically.  For M2, including
the fixed product-sign sector factor,

\[
 \epsilon_{\rm sgn}\chi_4(g)\chi_4(|a+p|)
 =\epsilon_{\rm sgn}\chi_4(|g(a+p)|).
\tag{130.29}
\]

Thus on the literal divisor point the M1 sign is again the original
denominator character and the full M2 sector factor is again
\(\epsilon_{\rm sgn}\chi_4(|h'|)\).  The branch split changes where the
character is carried; it does not create an independent oscillation.

This is not confined to the equality atom.  For fixed
$(\rho,g,u,v)$, put

\[
 h'=g\rho u=g(a+p),\qquad d'=g\rho v.
\tag{130.30}
\]

The threshold inequality is $d'\le t$, with its prescribed star, so
(130.12) gives the exact identity

\[
 \sum_t c_{i,t}{\bf1}^{*}_{d'\le t}
 =\omega_{i,D}^{*}(d';c).
\tag{130.31}
\]

If one next sums (130.24), all nonprimitive representations cancel.
Every remaining original pair $(h',d')$ has the unique complete-lift
factorization

\[
 g=(|h'|,d'),\qquad a'=h'/g,\qquad b'=d'/g.
\tag{130.32}
\]

Equations (130.28)--(130.32) therefore undo the Stieltjes, Mobius, and
reduced-ray decompositions exactly.  The inner portion of (130.2) becomes
the original literal $(h',d')$ numerator wave, with the owner condition
$d'/(\lvert h'\rvert,d')\asymp B$, the phase $e(-ch'/(\kappa_i d'))$, and the
original M1 denominator character or the fixed M2 factor
\(\epsilon_{\rm sgn}\chi_4(|h'|)\).  Summing the half-open $B$-owners
returns the full original block exactly once.

Consequently exact $p$-threshold recombination is an inversion, not an
estimate.  Only after every half-open $B$-owner has been reassembled,
applying the accepted complete original-variable product-window theorem
yields

\[
 {D^2\over L^2}+{WD\over L}
 =Y^{32/48}+Y^{37/48}
 \ll Y^{37/48},
\tag{130.33}
\]

which is weaker than the already accepted $Y^{35/48}$ direct
threshold-curvature theorem.

The same return is visible at a single birth.  Along the progression
$a+p=\rho u$, let $s=g\rho$.  The $u$-interval in (130.21) has
length $O(t/(sW))$, and its carrier has slope
$-cs/(\kappa_i t)$.  The exact resonant windows are

\[
\begin{array}{ll}
 {\rm M1}:& |cs-mt|\ll sW,\\[1mm]
 {\rm M2}:& |cs-(4m\pm1)t|\ll sW,
\end{array}
\tag{130.34}
\]

up to harmless absolute constants.  In M2 the two signs are the exact
split of $\chi_4(\rho u)$; in M1 the two quarter branches remain in the
denominator coordinate.  Formula (130.34) is precisely a truncated
integer product window.  It is not a uniform nonresonance condition.

### 3.3 The sharp literal numerator count and the shell refinement

On the inner shell, a nonzero exact Stieltjes-recombined complete-lift
coefficient must satisfy

\[
 g\rho v\asymp D,\qquad g\,|a+p|\asymp L,\qquad \rho v\asymp B.
\tag{130.35}
\]

Hence $g\asymp D/B$ and (130.3) follows.  Since $B\ge D/L$, the
quantity $LB/D$ is at least a fixed positive constant, so the added
(1) is harmless.  Both signs and all fixed profile variants change only
the implied constant.

From (130.4), Cauchy gives the exact outer $\ell^1$ ceiling

\[
 \sum_r|A_i(r)|
 \le (LD)^{1/2}\left({D\over L}\right)^{1/2}
 \ll D.
\tag{130.36}
\]

For each fixed (r,a'), the promoted Round-129 theorem, followed only
then by the divisor and branch sum, is

\[
 \left|\sum_{\rho\mid a'}\sum_{\eta\in\mathcal E_i}
 S_{i,r,a',\rho,\eta}^{(B)}\right|
 \ll_\varepsilon {K_B\over L}Y^\varepsilon.
\tag{130.37}
\]

Here

\[
 Q_B={BD\over WL},\qquad
 \lambda_B={YL\over DB^2},\qquad
 K_B=\min\!\left(Q_B,
 Q_B\sqrt{\lambda_B}+\lambda_B^{-1/2}\right).
\tag{130.38}
\]

The equality atom, Mobius divisor cost, M1 branch pair, M2 fixed sign,
clipped intervals, and all endpoint stars are already in (130.37); they
must not be added again.  Applying the (a')- and outer-ray triangles
only after (130.37) gives

\[
 |\mathfrak O_{i,B}^{+}|
 \ll_\varepsilon
 D\left({LB\over D}\right){K_B\over L}Y^\varepsilon
 =B K_B Y^\varepsilon,
\tag{130.39}
\]

proving (130.5).

Write $B=Y^b$.  The critical arithmetic is

\[
 Q_B=Y^{b-5/48},\qquad
 \lambda_B=Y^{32/48-2b},\qquad
 Q_B\sqrt{\lambda_B}=Y^{11/48},\qquad
 \lambda_B^{-1/2}\le Y^{8/48}.
\tag{130.40}
\]

Thus $K_B\asymp Y^{11/48+o(1)}$, proving (130.6).  In particular,

\[
 B={D\over L}:\quad BK_B=Y^{27/48}=Y^{9/16},
 \qquad
 B=D:\quad BK_B=Y^{35/48}.
\tag{130.41}
\]

For any fixed $\sigma>0$, all shells
$B\le DY^{-\sigma}$ contribute
$O_\varepsilon(DK_BY^{-\sigma+\varepsilon})$.  The first exact
residual is therefore the bounded-lift top region $B>DY^{-\sigma}$,
and in particular the dyadic shell $B\asymp D$.  Since that shell is
present, the complete logarithmic sum remains (130.1).

The inner strict/weak/star equality residual alone is $O(L^{-1})$ for
fixed $(r,a')$.  The same refined ledger gives $O(BY^\varepsilon)$ on
one shell, hence at most $O(DY^\varepsilon)$ in total.  It is target-safe
and already included in (130.39).  The equal-ray diagonal remains the
separate $O(D/L)$ owner.

### 3.4 The first (p)-first product-window return on the top shell

Now restrict to $B\asymp D$.  Then the complete lift length is bounded,
so each lift may be expanded without a (G)-loss.  For fixed outer ray
and fixed $b'\asymp D$, (130.22) cuts $p$ into $O(1)$ intervals of
total length

\[
 T\ll 1+{D\over W}.
\tag{130.42}
\]

After zero extension, each finite-lift literal (p)-weight has supremum
plus sampled variation $O(L^{-1})$.  This includes the Vaaler profile,
the clipped numerator support, its exit sample, and its star.

For M1, Abel summation of the (p)-interval gives

\[
 {1\over L}\min\!\left(T,{1\over\|c/b'\|}\right).
\tag{130.43}
\]

For M2, keep $\chi_4(\lvert a+p\rvert)$ in the increment sum.  On each fixed sign
and parity sector its exact two-quarter decomposition gives

\[
 {1\over L}\sum_{\pm}
 \min\!\left(T,{1\over\|c/(4b')\pm1/4\|}\right).
\tag{130.44}
\]

The factor four and both quarter orientations are present.  Primitivity
may be retained by (130.24), or dropped for this upper bound; the divisor
sum costs $Y^\varepsilon$.

For completeness, the real-centre product-window count behind (130.8) is
elementary.  If one displayed norm is $<\eta$, an integer product
(mb') (in M2, with the appropriate odd residue class) lies in a real
interval of length $O(1+\eta D)$ about the corresponding multiple of
$c$.  Each integer has $O_\varepsilon(Y^\varepsilon)$ divisor pairs.
Dyadic layer-cake summation from $\eta=T^{-1}$ to $1/2$ gives (130.8),
uniformly for real $c\asymp Y$.

Therefore the (p)-first inner scalar for one outer ray is at best, by
this lawful product-window route,

\[
 O_\varepsilon\!\left({D\over L}Y^\varepsilon\right).
\tag{130.45}
\]

Putting the reciprocal variable or the outer rays in modulus and using
(130.36) gives

\[
 {D^2\over L}Y^\varepsilon=Y^{40/48+\varepsilon}.
\tag{130.46}
\]

For M1, the unused denominator quarter phase remains in the (b')-sum;
for M2, the numerator quarter phase has already been consumed in
(130.44).  Treating the remaining M1 phase by a second independent
one-variable estimate is exactly the sequential-transform issue below.
Thus (130.45) is a product-window return, not a strict improvement on the
Round-129 (v)-first bound.

### 3.5 Unit-Hessian sequential-transform return

Put $q=b'-b$.  Before the Mobius reparametrization, the exact joint
ratio phase is

\[
 f_i(p,q)={c\over\kappa_i}
 \left({a\over b}-{a+p\over b+q}\right).
\tag{130.47}
\]

Its Hessian determinant is

\[
 \det\nabla^2_{p,q}f_i
 =-{c^2\over\kappa_i^2(b+q)^4}.
\tag{130.48}
\]

Equivalently, in the literal ((p,v)) progression,

\[
 \det\nabla^2_{p,v}
 \left(-{c(a+p)\over\kappa_i\rho v}
       +\vartheta_{i,\eta}\rho v\right)
 =-{c^2\over\kappa_i^2\rho^2v^4}
 =-{c^2\rho^2\over\kappa_i^2b'^4}.
\tag{130.49}
\]

On the top $\rho=1$ progression with $b'\asymp D=\sqrt Y$, both
determinants have unit order.  The M1 character adds a quarter-linear
term in (q); after splitting the M2 numerator character, M2 adds a
quarter-linear term in (p).  Linear terms do not change (130.48) or
(130.49); they translate the stationary lattice only.

The exact Legendre phase of (130.47), up to the Fourier sign convention,
is

\[
 {ca\over\kappa_i b}+a r+b s+{c\over\kappa_i}{s\over r}.
\tag{130.50}
\]

The inverse stationary map returns (130.47).  At the critical top shell,
the primal $p$-by-$q$ region has $LQ_*$ lattice capacity, where

\[
 Q_*={D^2\over WL}=Y^{19/48}.
\tag{130.51}
\]

Unit Jacobian gives the same number of dual aliases; the stationary
amplitude is of constant order.  With coefficient scale $L^{-1}$, an
aliaswise triangle has size $Q_*$ for one outer ray.  The outer
$\ell^1$ ceiling (130.36) therefore returns

\[
 DQ_*=Y^{43/48}.
\tag{130.52}
\]

Applying the transform plateau by plateau and then taking absolute values
can only add threshold endpoints.  Recombining the thresholds before the
transform instead invokes the exact inversion (130.31)--(130.33).  Thus
the Stieltjes representation supplies no hidden noninvertible step in a
sequential (p)-(v) transform.  The accepted Round-129 saving comes
from stopping after the one-variable reciprocal-curvature theorem; a
second capacity-positive transform cannot be used to multiply it by the
numerator high-pass.

A coefficient-blind aligned control makes the scope precise.  On the same
top-shell determinant strip, the bounded shadow

\[
 \widetilde U(p,v)=L^{-1}
 e\!\left({c(a+p)\over\kappa_i v}
          -\vartheta_i v\right)
\tag{130.53}
\]

conjugates the carrier and fills the raw joint capacity.  It is not an
actual Vaaler/Stieltjes coefficient and gives no physical lower bound.
It shows that support, pointwise size, determinant geometry, and quarter
lattice placement alone cannot prove a contraction.  The missing
physical property would have to control correlation of the fixed
Stieltjes thresholds and complete lift characters with the moving
(p)-dependent reciprocal stationary aliases; no selected-context lemma
supplies that property.

## 4. First doubtful or unproved step

After (130.5), the first unproved scalar assertion is a strict saving on
the literal bounded-lift top shell:

\[
 \left|\mathfrak O_{i,B\asymp D}^{+}\right|
 \ll_\varepsilon D K_D Y^{-\delta+\varepsilon}
 \qquad\text{for some fixed }\delta>0.
\tag{130.54}
\]

The target would require $\delta=11/48$.  Equation (130.54) must keep the
$p$-sum, reciprocal aliases, exact M1 or M2 quarter orientation, and
possibly the outer-ray phase in one signed scalar.  A target-scale outer
energy is sufficient but stronger than (130.54); no positive Gram is
silently substituted here.

At a threshold birth, the first unresolved arithmetic object is the
signed truncated product window (130.34), with the physical Stieltjes
coefficient and complete lift character, not its divisor-count majorant.
On plateau interiors, the equivalent unresolved object is the top-shell
joint sum (130.2) with the exact phase (130.20).  The product-window
estimate (130.8) takes a modulus too early, while a second transform has
the unit-Hessian return (130.52).  Therefore the required new input is a
noninvertible actual-family correlation estimate.  It cannot be inferred
from:

* support and the $L^{-1}$ pointwise envelope;
* the common notation $\chi_4(g)$, because the character has already
  been consumed by the Round-129 Abel step;
* M1 and M2 quarter shifts separately, because (130.28)--(130.29)
  recombine them into the original single character;
* real Hessian nondegeneracy, because all integer aliases remain; or
* the outer $\ell^2$ norm alone, because a positive energy is stronger
  than the desired scalar and admits phase-aligned shadows.

No claim is made that the actual top-shell scalar saturates
$D K_D$.  The report proves only that the exact recombinations and
standard product-window/transform inequalities available in the selected
context do not improve it.

## 5. Control tests and outcomes

| Required control | Exact test | Outcome |
|---|---|---|
| `literal_post_inner_dictionary` | Expand the outer ray, set $a'=a+p$, apply Mobius with $b'=\rho v$, retain the Stieltjes threshold and complete lift, and split only the literal M1 reduced character. | **Pass.** Formula (130.2) contains both complete ray coefficients, every threshold, all centre phases, the determinant taper, and no outside modulus. |
| `outer_ray_and_increment_counts` | Use outer Cauchy (130.36) and the exact shell support $g\asymp D/B$, $\lvert a'\rvert\asymp LB/D$. | **Pass.** The shell cost improves from $DK_B$ to $BK_B$; the top shell $B\asymp D$ is the first residual and prevents a complete power saving. |
| `actual_character_placement` | Track $\chi_4(b)$, $\chi_4(\rho v)$, $\chi_4(\lvert a\rvert)$, $\chi_4(\lvert a+p\rvert)$, and $\chi_4(g)$ through (130.17), (130.25), and the threshold identity. | **Pass.** M1 returns $\chi_4(d')$, M2 returns $\chi_4(\lvert h'\rvert)$; no character is deleted or counted twice. |
| `M1_M2_increment_orientation` | In the original increments use $q=2r$ for M1 and $p=2s$ for M2; equivalently keep M1 quarter shifts in $v$ and M2 quarter shifts in $p$. | **Pass.** The two orientations are different coordinate placements of one determinant phase, not independent multiplicative savings. The factor $\kappa_2=4$ remains in every phase and window. |
| `product_window_resonance_return` | Sum $p$ first at $B\asymp D$, or evaluate a threshold birth. | **Pass as a no-go.** Equations (130.8), (130.34), and (130.45)--(130.46) return the original integer product windows and capacity $D^2/L$, not a saving over $DK_B$. Exact full recombination gives the separate $Y^{37/48}$ original-variable return. |
| `unit_Hessian_sequential_transform_return` | Differentiate the literal ratio phase and retain every translated integer alias. | **Pass as a scoped no-go.** The determinant is unit order on the top $\rho=1$ progression; the exact Legendre transform is involutive, and aliaswise modulus returns $DQ_*=Y^{43/48}$. |
| `Mobius_threshold_and_owner_ledger` | Keep $\rho\mid a+p$, sum divisors only after the branch theorem, use (130.31), and assign every $b'$ to one half-open $B$-shell. | **Pass.** Mobius costs only $Y^\varepsilon$, Stieltjes mass is counted once, and undoing both expansions is the exact original-wave identity rather than a new estimate. |
| `strict_weak_star_and_support_faces` | Distinguish determinant $n=0$, threshold equality $t=\rho vg$, outer $v$-stars, numerator support exits, and the hard denominator sample. | **Pass.** The determinant diagonal is separately $D/L$; threshold equality is already in the $K_B/L$ theorem and alone costs at most $B$ per shell; every other face is in $T$, $P$, or $c_t$. |
| `capacity_before_and_after` | Compare $BK_B$, $DK_B$, the original product return, the $p$-first return, the full transform return, and the target. | **Pass.** At top these are respectively $Y^{35/48}$, $Y^{35/48}$, $Y^{37/48}$, $Y^{40/48}$, $Y^{43/48}$, and $Y^{24/48}$. At the smallest shell $BK_B=Y^{27/48}=Y^{9/16}$, but the complete block is top-dominated. |
| coefficient-blind phase alignment | Conjugate the joint carrier on the same determinant strip as in (130.53). | **Required failure for the shadow.** It fills the positive capacity. The control is not a physical lower bound and identifies the missing input as actual threshold/alias correlation. |
| scalar versus positive energy | Compare (130.54) with any proposed outer $\ell^2$ energy. | **Pass.** Only the scalar is required. No target-scale positive Gram is inferred from outer $\ell^2$ data. |
| `no_exponent_or_M9_promotion` | Compare the complete $35/48$ exponent with the $9/16$ persistence threshold and with the scopes of M9-M1 and M9-M2. | **Pass.** $35/48>9/16$, so there is no global pointwise improvement. Nothing here proves either M9 component, endpoint uniformity, M9, the conditional quarter bridge, or the Gauss-circle target. |

Every control is analytical/algebraic.  No numerical experiment and no
external theorem were used.

## 6. Dependencies and exact artifacts used

The accepted graph facts used are the current statements and scopes of:

* `GC-W7-16-reduced-Farey-cluster-reduction`, for the complete ray
  dictionary, outer $L^{-1}$ and $D/L$ bounds, exact determinant, and
  equal-ray owner;
* `GC-W7-16-original-numerator-product-window-bound`, for the exact
  inversion return (130.33) and real-centre product-window count;
* `GC-W7-16-bounded-lift-top-shell-curvature-saving`, for the bounded-lift
  top-shell interface;
* `GC-W7-16-determinant-half-shift-transform-obstruction`, for the exact
  Hessian, Legendre phase, quarter-lattice placement, and sequential
  transform scope;
* `GC-W7-16-local-lift-BV-threshold-V2-lemma`, for the literal separable
  lift and owner dictionary;
* `GC-W7-16-direct-Stieltjes-birth-block-curvature-lemma`, for the exact
  branchwise $K_\rho/L$ theorem and equality residual;
* `GC-W7-16-complete-all-shell-curvature-saving`, for the accepted
  $DK_B=Y^{35/48}$ comparison; and
* `GC-W7-16-actual-reduced-determinant-correlation`, only for the still-open
  $Y^{1/2}$ scalar target and its downstream scope.

The exact permitted context artifacts read and used were:

1. `protocol.md`;
2. `state/proof_obligations.yml`;
3. `state/active_campaign.yml`;
4. `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/reports/actual_rational_cluster_attack.md`;
5. `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reports/actual_character_determinant_attack.md`;
6. `rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reports/graded_determinant_long_lift_feasibility.md`;
7. `rounds/codex-managed/gc-w7-16-joint-stieltjes-reciprocal-curvature-gate/reports/actual_stieltjes_reciprocal_sum_attack.md`;
8. `rounds/codex-managed/gc-w7-16-joint-stieltjes-reciprocal-curvature-gate/reviews/conductor_round129_direct_curvature_adjudication.md`; and
9. `rounds/codex-managed/gc-w7-16-joint-stieltjes-reciprocal-curvature-gate/synthesis.md`.

No Round-130 sibling report, unlisted strategy artifact, web source, or
computation was read or used.  The effort allocation was 100%
analytical/algebraic.

## 7. Recommended state effect

**Promote after independent seam review** the exact post-inner formula
(130.2), with the branch dictionary (130.17), the congruence-normalized
phase and determinant gate (130.20)--(130.22), and the threshold/original-
variable inversion (130.28)--(130.33).  These are algebraic identities,
not a new correlation estimate.

**Promote after count and owner review** the shellwise refinement

\[
 |\mathfrak O_{i,B}^{+}|\ll_\varepsilon BK_BY^\varepsilon,
\]

including the exact support count $\#a'\ll LB/D$.  Record its scope
carefully: it gives a factor $B/D$ on lower shells and localizes the
residual to $B\asymp D$, but it does not improve the complete
$Y^{35/48}$ exponent.

**Record as a scoped no-go** that the first lawful $p$-first
product-window modulus returns $D^2/L$, exact undoing of the auxiliary
decompositions returns the accepted $Y^{37/48}$ original product wave,
and a sequential two-dimensional transform with aliaswise modulus returns
$DQ_*$.  These conclusions exclude those mechanisms as strict
continuations of the Round-129 theorem; they are not lower bounds for the
actual scalar.

**Retain open** `GC-W7-16-actual-reduced-determinant-correlation`.  Its
smallest remaining interface is (130.54) on the literal bounded-lift top
shell, with all (p)-increments, threshold aliases, M1/M2 character
orientations, and outer phases retained before a positive norm.

**No change** is licensed for the complete fixed-block exponent, the
proved global one-third theorem, M9-M1, M9-M2, endpoint uniformity, M9,
the conditional quarter bridge, or the Gauss-circle target.
