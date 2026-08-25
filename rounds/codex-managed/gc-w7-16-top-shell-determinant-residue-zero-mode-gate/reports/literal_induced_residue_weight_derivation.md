# Round 131 discovery report: literal induced residue weights

Campaign: `gc-w7-16-top-shell-determinant-residue-zero-mode-gate`

Task: `literal_induced_residue_weight_derivation`

Starting graph SHA-256:
`23e7bfacbf6abc5582769fbe8d427cbca2379e1d265b99df21d93a65ec504825`

## 1. Result: terminal degeneracy, with an exact repaired residue chart

The literal physical reassembly gives an exact determinant-residue
weight, but it does **not** give a single arithmetic factor periodic in
\(n\) modulo \(4|a|\) times a uniformly bounded-cost BV envelope.  (A
tautological finite-support envelope is of course BV, but its variation
is linear and returns the raw capacity.)  The failure is
already forced by physical primitivity.  For fixed \(p\), writing
\(a'=a+p\) and

\[
 b'_{r,p}(n)={b(a+p)+n\over a},
\]

the reassembled coefficient contains
\(\mathbf 1_{(a',b'_{r,p}(n))=1}\).  Under
\(n\mapsto n+4|a|\), \(b'\) changes by \(4\operatorname {sgn}(a)\),
so this primitive indicator is not invariant unless every odd prime
factor of \(a'\) divides \(4\).  Moving it into the envelope is not a BV
repair: when \(3\mid a'\), its variation on a \(q\)-interval of length
\(Q\) can be \(\gg Q\).

There is an exact weaker decomposition.  After the physical coefficient
has first been formed, re-expand its primitive indicator divisor by
divisor.  A divisor atom \(\rho\mid a'\) is periodic in \(n\) with modulus

\[
 M_{p,\rho}=|a|\operatorname {lcm}(4,\rho),                 \tag{131.1}
\]

not generally \(4|a|\).  Equivalently the unsplit primitive factor has
period \(|a|\operatorname {rad}(a')\), and its combination with the
quarter carrier has period
\(|a|\operatorname {lcm}(4,\operatorname {rad}(a'))\).
On each such divisor/lift/support chart, the nonoscillatory physical
amplitude has the accepted top-shell BV cost, with the boundary ledger
given below; the reciprocal phase must remain an oscillatory phase and
cannot be put into a bounded-cost BV envelope.

The genuine shifted modes are as follows.

* For M1, a fixed denominator-quarter branch \(\sigma=\pm1\) has
  Fourier support modulo \(4|a|\) only in
  \(k\equiv \sigma\operatorname {sgn}(a)\pmod 4\).  Thus the physical
  resonance is the quarter-shifted alias
  \(ca'/(b'(b'+1))+\sigma/4\), not the naive zero alias.
* For M2, on a fixed numerator-sign and \(q\pmod4\) sector with odd
  \(b\), the two numerator-character branches have determinant modes
  \(k\equiv-\tau\operatorname {sgn}(a')\bar b,|a|\pmod {4|a|}\),
  \(\tau=\pm1\), where \(b\bar b\equiv1\pmod4\).  The corresponding
  physical alias is \(c/(4b')-\tau\operatorname {sgn}(a')/4\).  When
  \(b\) is even, no such character of \(n\pmod {4|a|}\) exists; an
  extra two-adic \(p/q\) coordinate, hence a larger modulus, is
  indispensable.

These are linear additive-character completions.  The supplied algebra
contains neither a quadratic phase nor a modular inverse phase, so it
does not produce a growing-modulus quadratic Gauss sum or a Salié sum.
The only Gauss identity present is the fixed modulus-four Fourier identity
for \(\chi _4\), which supplies no power saving.

Same-denominator packets show that the shifted mode can be coherent on
each ray.  One top-shell resonant window has capacity

\[
 D{D/W\over L}K_D=Y^{30/48+o(1)},                          \tag{131.2}
\]

and there are \(O(1+WL/D)=Y^{5/48+o(1)}\) such windows; their total
length is of order \(L\), so their triangle capacity is the full
\(DK_D=Y^{35/48+o(1)}\).  No cancellation of the actual outer-ray sum is
contained in the supplied hypotheses.  Conversely, the aligned packets
do not prove a lower bound for the actual Vaaler family.  The terminal
label is therefore

\[
 \boxed{\texttt{degenerate}}.                              \tag{131.3}
\]

The first residual is the actual signed family sum of the complete
reassembled shifted-resonant ray blocks.  Neither a bank nor a physical
family-level obstruction follows before that scalar is estimated.

## 2. Exact statement and hypotheses

Fix the frozen top-shell data

\[
 W=Y^{7/16},\qquad D=Y^{1/2},\qquad L=Y^{1/6},\qquad
 B\asymp D,\qquad K_D=Y^{11/48+o(1)},                      \tag{131.4}
\]

one literal moving-symbol stratum, one orientation, and one M1 or M2
sign sector.  Write \(r=(a,b)\), \(A=|a|\), \(s_a=a/A\),
\(a'=a+p\), \(b'=b+q\), and

\[
 n=ab'-a'b=aq-bp.                                          \tag{131.5}
\]

For a physical pair \((a',b')\), form the Möbius sum before making the
determinant chart.  It is convenient to denote the exact reassembled
non-character part by

\[
\begin{aligned}
 \mathcal H_{i;r,p}(a',b')
 :={}&\sum_{\substack{\rho\mid a'\\ \rho\mid b'}}
       \mu(\rho)\,T_{i;r,p,\rho,D}^{\rm lit}(b'/\rho) \\
 &\quad\times\sum_t c_{i,t}
       \sum_{g\le t/b'}^{*}{\chi _4(g)\over g}P_{i,a'}(g).
                                                               \tag{131.6}
\end{aligned}
\]

Every frequency floor, threshold star, determinant taper, shell and cell
face, sign, and half-open owner remains in the superscript `lit`.  Formula
(131.6) is one physical coefficient: no modulus or absolute value is
inserted inside its \(\rho\)- or Stieltjes sum.  Its bare incidence factor
contains the exact identity

\[
 \sum_{\rho\mid(a',b')}\mu(\rho)
 =\mathbf 1_{(a',b')=1}.                                   \tag{131.7}
\]

For fixed \(r,n\), let \(\Lambda_{i,r}(n)\) be the set of literal
\(p\)-lifts for which

\[
 b'_{r,p}(n)={b(a+p)+n\over a}\in\mathbb Z                 \tag{131.8}
\]

and every physical sign, top-shell, determinant, cell, star, and owner
condition holds.  Then \(n\equiv-bp\pmod A\) and
\(\#\Lambda_{i,r}(n)=O(1)\), but the set is not replaced by a Cartesian
interval.

The exact induced weights are

\[
\boxed{
\begin{aligned}
 \mathcal W_{1,r}(n)
 ={}&\sum_{p\in\Lambda_{1,r}(n)}
 {\mathcal H_{1;r,p}(a+p,b'_{r,p}(n))\over\pi(a+p)}
 \sum_{\sigma=\pm1}\sigma e\!\left({\sigma b'_{r,p}(n)\over4}\right)
 e\!\left({cn\over b\,b'_{r,p}(n)}\right),\\[2mm]
 \mathcal W_{2,r}(n)
 ={}&\sum_{p\in\Lambda_{2,r}(n)}
 {-4\epsilon_{\rm sgn}\chi _4(|a+p|)\over\pi|a+p|}
 \mathcal H_{2;r,p}(a+p,b'_{r,p}(n))
 e\!\left({cn\over4b\,b'_{r,p}(n)}\right).
                                                               \tag{131.9}
\end{aligned}}
\]

Indeed

\[
 {ca\over\kappa_i b}-{c(a+p)\over\kappa_i b'}
 ={cn\over\kappa_i bb'},\qquad \kappa_1=1,\quad\kappa_2=4. \tag{131.10}
\]

Thus the physically reassembled scalar, before an outer or residue
triangle, is exactly

\[
 \mathfrak O_{i,D}^{+}=\sum_r^{\rm lit}A_i(r)
 \sum_{n>0}^{\rm lit}\mathcal W_{i,r}(n).                  \tag{131.11}
\]

The weakest useful periodic/BV statement is the following.  First form
(131.6).  Then, if Fourier analysis is desired, expand (131.7) and split
the bounded physical lift/support charts.  For fixed
\((r,p,\rho)\), the arithmetic factor is periodic with modulus (131.1),
while the zero-extended amplitude after removing the reciprocal phase
has variation bounded by its sampled-profile variation plus exactly the
faces listed in Section 3.  There is no legal assertion with one common
modulus \(4A\), and there is no legal assertion that absorbs either
primitivity or the reciprocal exponential into an \(O(Y^\varepsilon)\)-BV
envelope.

## 3. Proof and derivation

### 3.1 Physical reassembly precedes the residue chart

In the supplied pre-reassembly scalar, \(b'=\rho v\).  For fixed
\((a',b')\), only \(\rho\mid(a',b')\) occurs.  The M1 branch coefficients
are \(\mu(\rho)/(\pi a')\) and \(-\mu(\rho)/(\pi a')\), and their phases
are \(e(b'/4)\) and \(e(-b'/4)\).  The M2 coefficient is
\(-4\mu(\rho)\epsilon_{\rm sgn}\chi_4(|a'|)/(\pi|a'|)\).
Also \(g\le t/(\rho v)\) becomes \(g\le t/b'\).  Summing the common
physical \(\rho\)-atoms gives (131.6), including (131.7), and leaves the
two physical character factors

\[
 {e(b'/4)-e(-b'/4)\over\pi a'}\quad\text{(M1)},\qquad
 {-4\epsilon_{\rm sgn}\chi_4(|a'|)\over\pi|a'|}\quad\text{(M2)}.
                                                               \tag{131.12}
\]

Only now substitute (131.5) and (131.8).  Combining the two centre
phases by (131.10) proves (131.9)--(131.11).  This order also shows why a
Fourier expansion of an individual \(\rho\)-piece before reassembly would
not be a Fourier expansion of the physical scalar.

### 3.2 Why modulus \(4A\) fails, and the corrected modulus

For fixed \(p\), put \(q=(n+bp)/a\).  On its admissible progression,
\(n\mapsto n+4A\) sends \(q\mapsto q+4s_a\).  The M1 quarter carrier is
unchanged, but the primitive factor becomes

\[
 \mathbf1_{(a',b+q+4s_a)=1},
\]

which need not equal \(\mathbf1_{(a',b+q)=1}\).  For example, take an
admissible \(a'\) divisible by \(3\), choose an interior \(b+q\) divisible
by \(3\), and avoid the other prime factors of \(a'\).  The first pair is
nonprimitive while \(b+q+4s_a\) is not divisible by \(3\).  Both
determinants have the same residue modulo \(4A\).  Hence the literal
arithmetic weight is not \(4A\)-periodic.

Nor can this be hidden in a low-variation envelope.  On a physical
\(q\)-interval of length \(Q\), the sequence
\(\mathbf1_{3\nmid b+q}\) has two jumps in every three consecutive
positions.  After choosing \(a'\) with no additional obstruction on the
displayed positions,

\[
 \operatorname {Var}_{q}\mathbf1_{(a',b+q)=1}
 \ge 2\lfloor Q/3\rfloor-O(1).                              \tag{131.13}
\]

This is linear variation, not a boundary term.

After physical reassembly one may use the exact identity

\[
 \mathbf1_{(a',b')=1}
 =\sum_{\rho\mid a'}\mu(\rho)\mathbf1_{\rho\mid b'}.        \tag{131.14}
\]

For fixed \(p,\rho\), the last indicator has period \(A\rho\) in \(n\),
and the M1 quarter carrier has period \(4A\); their common period is
(131.1).  Summing (131.14) gives the unsplit period claimed in Section 1.
The divisor expansion costs at most the accepted \(Y^\varepsilon\)
divisor factor, but it produces a varying modulus depending on \(a'\)
and \(\rho\).  This is the exact repaired arithmetic separation.

There is a second, independent seam.  Choose the canonical solution
\(p_0(x)\pmod A\) of \(bp_0\equiv-x\pmod A\).  Physical lifts have the
form \(p=p_0(x)+kA\), with only \(O(1)\) active \(k\)'s at a fixed
\(x\).  Bounded multiplicity does not control how the active chart
changes as \(x\) varies, and M2's \(\chi_4(a+p)\) depends on that lift
modulo four.  Thus the bounded-to-one theorem alone supplies neither a
single periodic M2 factor nor a BV lift selector.

### 3.3 Complete variation and boundary ledger

The following ledger is for one fixed physical divisor/lift chart and is
then summed with the literal Stieltjes and divisor weights.  `BV cost'
means zero-extended discrete variation plus the supremum norm, before the
reciprocal oscillation is estimated.

| Factor or face | Exact treatment | Cost/outcome |
|---|---|---|
| \(1/(a+p)\) or \(1/|a+p|\) | Fixed on a \(p\)-chart | Variation \(0\), size \(\asymp L^{-1}\). |
| \(P_{i,a+p}(g)\) | Fixed in \(n\) once \(p,g\) are fixed | No \(n\)-variation; its accepted sampled variation is retained when charts are summed. |
| Stieltjes cutoff \(g b'\le t\), including equality star | One birth/death for each \((t,g)\) | Weighted variation \(\ll L^{-1}\sum_t|c_{i,t}|\sum_{g\asymp1}g^{-1}\ll L^{-1}\) on the top shell.  The equality value is charged once, not once to each adjacent plateau. |
| Denominator profile, top shell, and clipped cell support | Zero-extend each accepted BV profile and bounded union of intervals | Interior variation plus two endpoint suprema per interval; \(O(Y^\varepsilon/L)\) in the accepted top-shell normalization. |
| Determinant taper | Keep \((1-Wn/(\kappa_i bb'))_+\) intact | Since \(n/(bb')=a/b-a'/b'\), it is monotone on a fixed sign chart and has variation at most \(1\), plus its single support face. |
| Frequency floors and hard samples | Keep each literal plateau and star | Each plateau boundary is owned once.  The supplied top-shell BV/Stieltjes theorem prices their weighted total; no new free boundary is created by the residue chart. |
| M1 quarter carrier and M2 numerator character | Arithmetic, not BV | Put into the periodic factor only after the required divisor, sign, and two-adic sectors are fixed. |
| Physical primitivity | Arithmetic factor (131.14) | It has variation \(\gg Q\) if put in the envelope; its legal price is the varying modulus (131.1) and the divisor factor. |
| Reciprocal centre phase | Retain as the oscillatory phase | On a \(b'\)-interval of length \(Q\), its raw variation is \(O(1+c|a'|Q/(\kappa_iD^2))=O(1+LQ)\).  For the top local length \(Q_D=Y^{19/48+o(1)}\), this is \(Y^{27/48+o(1)}\), so it is not a bounded-cost envelope. |
| Lift selector \(p_0(x)+kA\) | Split into actual half-open support charts | The entry and exit of each fixed chart cost its endpoint supremum.  The supplied bounded-multiplicity statement gives no bound for the total cross-chart variation; an \(O(L)\) worst-case switching cost remains possible. |
| M2 sign crossing | Split \(a'>0\) and \(a'<0\), own \(a'=0\) once | For nonzero odd \(a'\), \(\epsilon_{\rm sgn}\chi_4(|a'|)=\chi_4(a')\).  Thus the crossing convention continues the actual character and creates no cancellation bonus. |
| Shell/cell equality, reciprocal-alias tie, and support face | Half-open owner, with the supplied star at equality | One copy only.  Fourier completion does not create a second owner. |
| \(n=0\) | Separate determinant diagonal | Excluded from the one-sided \(n>0\) residue scalar and retained by its accepted diagonal owner. |

Consequently the nonoscillatory amplitude is BV only after the primitive
and lift arithmetic has been split off and the reciprocal exponential
has been left outside.  The proposed single \(4A\)-periodic/BV
factorization fails exactly at those three entries; all ordinary
threshold and support faces are already affordable.

### 3.4 Shifted modes

For M1 and fixed \((r,p,\sigma)\), ignore only the separately displayed
primitive divisor factor and set

\[
 \Pi_{1,\sigma,p}(x)
 =\mathbf1_{x\equiv-bp\ (A)}
 e\!\left({\sigma\over4}
 \left[b+{x+bp\over a}\right]\right),\qquad x\pmod {4A}. \tag{131.15}
\]

Write an admissible residue as \(x=x_0+Au\), \(0\le u<4\).  Its finite
Fourier coefficient contains

\[
 \sum_{u=0}^{3}e\!\left({(\sigma s_a-k)u\over4}\right),    \tag{131.16}
\]

which is zero unless

\[
 k\equiv\sigma s_a\pmod4.                                  \tag{131.17}
\]

Thus \(\chi_4\)'s two denominator branches translate the unshifted class
to the two quarter classes.  Along the physical \(q\)-progression the
exact one-step phase difference is

\[
 \left[-{ca'\over b'+1}+{\sigma(b'+1)\over4}\right]
 -\left[-{ca'\over b'}+{\sigma b'\over4}\right]
 ={ca'\over b'(b'+1)}+{\sigma\over4}.                       \tag{131.18}
\]

Equation (131.18), including its integer aliases, is the shifted M1
resonance.  A zero-mode test would inspect the wrong class.

For M2, on one fixed sign sector put \(s'=\operatorname {sgn}(a')\).
For nonzero \(a'\),

\[
 \chi_4(|a'|)={1\over2i}\sum_{\tau=\pm1}
 \tau e\!\left({\tau s'a'\over4}\right).                  \tag{131.19}
\]

If \(b\) is odd and \(q\equiv q_0\pmod4\) is fixed, then
\(p\equiv\bar b(aq_0-n)\pmod4\).  Hence the \(\tau\)-branch in
(131.19) is a constant on the \(q_0\)-sector times

\[
 e\!\left(-{\tau s'\bar b,n\over4}\right)
 =e\!\left({k_{2,\tau}n\over4A}\right),\qquad
 k_{2,\tau}\equiv-\tau s'\bar b A\pmod {4A}.              \tag{131.20}
\]

At fixed \(b'\), the corresponding exact \(p\)-increment is

\[
 \Delta_p\left[-{c(a+p)\over4b'}+{\tau s'(a+p)\over4}\right]
 =-{c\over4b'}+{\tau s'\over4}.                            \tag{131.21}
\]

This gives the two shifted norms \(\|c/(4b')\mp1/4\|\).

The odd-\(b\) qualification is essential.  In an M2 ray \(A\) is odd.
If \(b\) is even, compare two allowed numerator positions differing by
\(2\): their M2 characters have opposite signs, while at fixed \(q\)
their determinants differ by \(-2b\).  A determinant character
\(e(kn/(4A))\) producing that sign change would require

\[
 bk\equiv-A\pmod {2A},                                      \tag{131.22}
\]

which has no solution because \(\gcd(b,2A)\) is even and \(A\) is odd.
Thus M2 is not, in general, a character of \(n\pmod {4A}\).  A larger
two-adic modulus and the missing \(p/q\)-parity coordinate are necessary.

### 3.5 Aligned packets, resonant mass, and Salié no-go

The same-denominator controls are literal.  For M1 take \(q=0\),
\(p=-t\), so \(b'=b\), \(n=bt>0\), and

\[
 e\!\left({cn\over b^2}\right)=e(ct/b).                    \tag{131.23}
\]

The denominator carrier in (131.12) is constant in \(t\), and the outer
and inner denominator characters align.  At \(c/b\in\mathbb Z\), or in
the corresponding width-\(1/T\) neighbourhood for \(t\le T\), the packet
is coherent.

For M2 take \(q=0\), \(p=-2j\), with \(a\) and \(a-2j\) in their literal
sign owners.  The sign convention gives

\[
 \chi_4(a)\epsilon_{\rm sgn}\chi_4(|a-2j|)
 =\chi_4(a)\chi_4(a-2j)=(-1)^j,                             \tag{131.24}
\]

including continuation across the sign split (with \(a'=0\) separately
owned).  The determinant phase is

\[
 e\!\left({c(2bj)\over4b^2}\right)=e(cj/(2b)).             \tag{131.25}
\]

Thus the product is coherent when \(c/b\) is an odd integer.  Equations
(131.23)--(131.25) refute character-forced per-ray vanishing.  They do not
discard the actual profiles and therefore do not assert a family lower
bound.

The determinant taper makes one same-denominator window have
\(T\asymp D/W\) numerator positions.  The accepted product-window ledger
has at most \(1+WL/D\) cells, so at the frozen scales

\[
 R_D={D\over W}=Y^{3/48},\qquad
 C_D={WL\over D}=Y^{5/48},\qquad C_DR_D=L.                  \tag{131.26}
\]

Since the fixed-\((r,a')\) inner scale is \(K_D/L\), the outer triangle
gives (131.2) for one window and

\[
 D C_D R_D{K_D\over L}=DK_D=Y^{35/48+o(1)}                 \tag{131.27}
\]

for the full resonant-window family.  A resonant mode is therefore not a
sparse error merely because it is one Fourier mode: a coherent Fourier
coefficient carries the full length of its window.

For comparison, square-root residue cancellation would give
\(DK_D/L^{1/2}=Y^{31/48+o(1)}\), an ideal one-term-per-ray result gives
\(DK_D/L=Y^{27/48+o(1)}\), and the target is
\(D=Y^{24/48}\).  The one-term floor only reaches the persistence
threshold; a strict global improvement still needs a cross-ray gain.

Finally, completing (131.15) gives only the four-term geometric sum
(131.16).  Completing (131.19) gives the fixed modulus-four transform of
\(\chi_4\).  Expanding primitivity adds linear congruence indicators.
There is no variable \(x\) for which the literal phase is
\(e((mx+\ell\bar x)/M)\), no unit condition making such \(\bar x\)
available modulo (131.1), and no quadratic \(x^2/M\) phase.  The centre
\(c\) is also a real centre, not a supplied integral residue parameter.
Therefore no exact Salié or growing quadratic-Gauss completion is
eligible.  The missing identity is an exact conversion of the real
reciprocal phase, the variable primitive modulus, and the physical
support into a fixed-modulus unit inverse phase with controlled
completion boundaries.  No such identity is present in the permitted
data.

## 4. First doubtful or unproved step

Let \(\mathcal R_{i,r,\nu}(c)\) denote the restriction of the exact
physical weight (131.9) to one literal cell \(\nu\) and to its shifted
alias (131.18) for M1 or (131.21) for M2, with the full reassembled
primitive factor, Stieltjes thresholds, reciprocal phase, taper, stars,
and owners retained.  The first exact residual is

\[
 \boxed{
 \mathfrak R_i^{\rm res}(c)
 =\sum_{r=(a,b)}^{\rm lit}A_i(r)
   \sum_{\nu}^{\rm lit}\mathcal R_{i,r,\nu}(c).}            \tag{131.28}
\]

The available facts give only

\[
 \sum_\nu|\mathcal R_{i,r,\nu}(c)|\ll K_DY^\varepsilon,
 \qquad |\mathfrak R_i^{\rm res}(c)|\ll DK_DY^\varepsilon. \tag{131.29}
\]

The first unavailable assertion is a signed actual-vector estimate for
(131.28), not a per-ray complete-sum bound and not a positive outer
energy.  Any local bank requires

\[
 |\mathfrak R_i^{\rm res}(c)|
 \ll DK_DY^{-\delta+\varepsilon}                            \tag{131.30}
\]

from the actual coefficients and the variable-modulus resonant blocks.
To cross the persistence threshold one needs total \(\delta>1/6\); the
ideal per-ray \(L^{-1}\) gain gives only equality \(\delta=1/6\).
Reaching the determinant target requires \(\delta=11/48\), namely a
further \(Y^{-3/48}=Y^{-1/16}\) gain after the one-term-per-ray floor.

No supplied identity gives (131.30).  The same-denominator calculations
show why it cannot come from character zero mean alone, while the data on
\(A_i(r)\) do not determine a coherent lower bound either.  This is the
precise reason for the `degenerate`, rather than `bank` or `obstruct`,
verdict.

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| exact top-shell M1/M2 dictionary | Green: (131.6), (131.9), and (131.12) retain the two M1 branches, the M2 numerator character and sign, \(\kappa_1=1\), \(\kappa_2=4\), all lift characters, thresholds, stars, taper, cells, and owners. |
| physical Möbius reassembly | Green: (131.6)--(131.7) are formed before (131.8); no \(\rho\)-piece is Fourier-expanded as though physical. |
| periodic/BV separation before Fourier | Red for a single modulus \(4|a|\), by (131.13).  Green for the repaired divisor/lift-chart statement with modulus (131.1) and the Section 3.3 ledger. |
| shifted resonant mode modulo \(4|a|\) | Green with scope: M1 has (131.17); odd-\(b\) M2 sectors have (131.20); even-\(b\) M2 has the exact no-go (131.22). |
| M1 same-denominator alignment | Green: (131.23) has constant denominator carrier and aligns at integral \(c/b\). |
| M2 positive-numerator alignment | Green: (131.24)--(131.25) align at odd-integral \(c/b\). |
| M2 sign-crossing packet | Green: \(\epsilon_{\rm sgn}\chi_4(|a'|)=\chi_4(a')\); the crossing owner creates no artificial cancellation. |
| resonant-window mass | Green: one window is \(Y^{30/48+o(1)}\), all \(C_D\) windows recover \(Y^{35/48+o(1)}\), by (131.26)--(131.27). |
| threshold equality, stars, support faces, and owners | Green: every face is charged once in Section 3.3; the diagonal, sign crossing, and half-open shell/cell boundaries remain separately owned. |
| scalar versus positive energy | Green: the survivor is the actual scalar (131.28); no operator norm, arbitrary direction, or positive Gram replaces it. |
| per-ray versus cross-ray capacity | Green: the ladder \(35/48\to31/48\to27/48\to24/48\) is explicit, and strict improvement below \(27/48\) is identified as cross-ray. |
| Salié/quadratic-Gauss eligibility | Green no-go: only linear/fixed-modulus-four transforms occur; the inverse phase, fixed unit modulus, and completion identity are absent. |
| no global or M9 promotion | Green: no complete exponent, endpoint, bridge, M9-M1, M9-M2, M9, or quarter claim is made. |

The work was 100% analytical/algebraic.  No computation and no external
theorem were used.

## 6. Dependencies and exact artifacts used

Only the permitted selected context was used:

1. `protocol.md`;
2. `state/proof_obligations.yml`, at graph scope
   `23e7bfacbf6abc5582769fbe8d427cbca2379e1d265b99df21d93a65ec504825`,
   especially the accepted reduced-Farey dictionary, top-shell
   bounded-lift theorem, local BV/Stieltjes theorem, shell support
   refinement, determinant-residue chart, outer-energy obstruction, and
   the open actual determinant correlation;
3. `state/active_campaign.yml` for Round 131;
4. `strategy/conductor_0823_full_proof_strategy.md`;
5. `rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/blind_statement.md`;
6. `rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/reviews/conductor_round130_post_inner_adjudication.md`;
7. `rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/synthesis.md`.

No Round 131 sibling report, historical derivation outside the permitted
packet, source theorem, or numerical experiment was used.

## 7. Recommended state effect

**Retain** `GC-W7-16-actual-reduced-determinant-correlation` as open and
**revise**, rather than promote, the proposed top-shell continuation:

* reject a single \(4|a|\)-periodic factorization with a uniformly
  bounded-cost BV envelope for the physically reassembled weight;
* retain the exact induced formulas (131.9) as candidate evidence;
* if this interface is ever cited, use the variable-modulus
  divisor/lift-chart decomposition (131.1), including the even-\(b\) M2
  parity residual;
* record that no genuine Salié or growing quadratic-Gauss sum has been
  identified;
* park the internal per-ray lane at the terminal `degenerate` verdict,
  with (131.28) as the first actual-family residual.

There is no graph, validation, synthesis, fixed-block exponent, global
exponent, M9 component, endpoint, bridge, or quarter promotion.
