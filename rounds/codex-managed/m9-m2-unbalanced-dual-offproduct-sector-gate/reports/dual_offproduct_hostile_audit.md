# Hostile audit: dual off-product sectors, curvature cells, and reciprocal packet

Campaign: `m9-m2-unbalanced-dual-offproduct-sector-gate`

Round: 125

Role: hostile seam reviewer
Starting graph SHA-256:
`27bd4173fbdb16e5689595a02d42d82ffa8bb514b4610ea745ce2da6e2b8b152`

Provenance note: references below to the candidate's rejected
integer-frequency defect mean the pre-review (4a) version supplied to
this audit. The live conductor candidate was subsequently revised to the
half-integer formulas proved here.

## 1. Result

No square-target estimate, strict complete-sector saving, or endpoint-complete
reciprocal transform is proved by the curvature-cell proposal.  The maximal
safe result is the following exact recombination together with a
strict-interior principal-symbol calculation.

Put

$$
 B_{p,n}:=\sum_{a=0}^{H-1}b_{p,n+a},\qquad
 B_n:=\sum_{p>0\atop p\ {\rm odd}}\chi _4(p)B_{p,n},
$$

with the literal zero extension, and define

$$
 \mathcal E_p:=C_H\sum_p\sum_n|B_{p,n}|^2,
 \qquad
 \mathcal G_{\rm act}:=C_H\sum_n|B_n|^2.
 \tag{125.H1}
$$

Then the exact Fejer algebra is

$$
 \mathcal E_p=\mathcal D_0+\mathcal S_{\rm eq}^{\ne0},
 \qquad
 \mathcal G_{\rm act}
 =\mathcal D_0+\mathcal S_{\rm eq}^{\ne0}+\mathcal S_{\rm neq},
 \tag{125.H2}
$$

and hence

$$
 \boxed{\mathcal S_{\rm off}=\mathcal G_{\rm act}-\mathcal D_0},
 \qquad
 \mathcal S_{\rm neq}=\mathcal G_{\rm act}-\mathcal E_p.
 \tag{125.H3}
$$

Thus the positive fixed-
$p$ row energy cancels **exactly** between the two proposed sectors.  Bounding
$\mathcal E_p$ is a strictly stronger sufficient route, not a reformulation
of the target.  Since $\mathcal G_{\rm act}\ge0$ and
$\mathcal D_0\ll X^{1/2}$,

$$
 \mathcal S_{\rm off}\ge-\mathcal D_0\ge-CX^{1/2},
 \tag{125.H4}
$$

and an absolute fixed-power violation is necessarily a positive violation
of the full actual-character block energy.  Up to the already-safe
$\mathcal D_0$, the desired estimate is exactly

$$
 \mathcal G_{\rm act}\ll_\varepsilon X^{1/2+\varepsilon}.
 \tag{125.H5}
$$

This is the maximal safe theorem and the exact object at which the lane can
be parked.  Splitting (125.H3) into equal and unequal modes can discard an
essential cancellation and supplies no smaller predetermined safe target.
The only unconditional sectorwise inverse statement is the elementary
disjunction

$$
 \mathcal S_{\rm off}>A
 \quad\Longrightarrow\quad
 \mathcal S_{\rm eq}^{\ne0}>A/2
 \ \hbox{or}
 \mathcal S_{\rm neq}>A/2.
 \tag{125.H5a}
$$

It localizes a realized violation to one of two complete sectors, but does
not select a sector in advance, estimate either one, or justify discarding
their cancellation.

On a fixed central smooth patch, the constants, reciprocal phase, moving
profile, and principal second-B-process return in (125.C5)--(125.C10) are
correct.  The diagonal stationary capacity is $KQ\asymp X^{1/2}$.
Recombining the $Q$ reciprocal crossings by bare Cauchy costs $Q$, while
working on the original $H$ terms costs $H$.  The correct coefficient-blind
diagnostic is therefore a loss $\min(H,Q)$ after choosing the better side,
not an unconditional necessary loss $Q$.  Both $H$ and $Q$ tend to
infinity, so this correction does not produce the target.

There is also a fatal second-stage correction.  Because the fixed-row
energy sums over **odd** $p$, its coherent frequency lattice is
$\frac12\mathbb Z$, not $\mathbb Z$.  The pre-review (4a)
nearest-integer defect misses every odd half-integer alias and cannot support the claimed
far-range deletion.  Even after repairing that lattice, the moving hard
interval $I_{p,n}$ leaves at most one $p$ at fixed $(n,d,d')$; consequently
there is no length-$L$ smooth $p$-sum at that stage.  The advertised
nonzero near-defect window is only a principal model for the stronger
$\mathcal E_p$, not a complete survivor.

## 2. Exact statement and hypotheses

Let $e(x)=\exp(2\pi i x)$, let $X\to\infty$, and let $M\asymp X$ be an
integer while every physical amplitude is frozen at $X$.  Put

$$
 D=X^\delta,\qquad L=X^\ell,\qquad
 K=\frac{XL}{D^2},\qquad
 H=\left\lceil\frac{X^{1/2}}D\right\rceil,
$$

where

$$
 \frac14\le\delta<\frac12,\qquad
 0\le\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463.
 \tag{125.H6}
$$

Let

$$
 Q=\frac{D^2}{L\sqrt X},\qquad H_c=\frac KD.
$$

Then, with ceiling errors kept asymptotic rather than exact,

$$
 K\asymp LH^2,\qquad
 \frac H{H_c}=\frac{DH}{K}\sim Q\longrightarrow\infty,
 \qquad H\longrightarrow\infty,
 \tag{125.H7}
$$

and

$$
 C_H=\frac{J+H-1}{H^2}\asymp\frac K{H^2}\asymp L.
 \tag{125.H8}
$$

The two regimes

$$
 Q\le H\iff D\le K,
 \qquad
 Q>H\iff D>K
 \tag{125.H9}
$$

are both allowed by (125.H6).  In the second regime $H_c<1$; the
$Q$ derivative crossings are continuous dual stationary labels, not $Q$
nonempty subsets of an $H$-point primal block.

For positive odd $p$, use exactly

$$
 b_{p,k}=e(-1/8)M^{1/4}k^{-3/4}p^{-3/4}
 \mathcal A_{p,k}e(\sqrt{Mpk}),
 \tag{125.H10}
$$

with

$$
 \mathcal A_{p,k}
 =W\!\left(\frac X{2D}\sqrt{\frac p{Mk}}\right)
 q_L((X/M)p)
$$

on the flat-smooth row and with literal zero extension everywhere else.
The character is not part of $b_{p,k}$: it occurs as $\chi _4(p)$ in the
full row $B_n$.  All exact conclusions (125.H1)--(125.H5) hold with the
moving profiles and all block entries and exits.

The stationary conclusions below require a fixed central patch with
$p\asymp L$, $k\asymp K$, all smooth profiles active, and each saddle a
fixed stationary width away from the hard block faces.  They do not include
Fresnel faces, ties, nonstationary modes, zero-extension transitions, or an
aggregate remainder estimate.

Under these hypotheses the maximal additional safe assertion is:

**Principal reciprocal-return lemma.**  For
$f_p(x)=\sqrt{Mpx}$, the strict-interior B-process of one block has positive
stationary labels $d$ with

$$
 x_{p,d}=\frac{Mp}{4d^2},\qquad
 f_p(x_{p,d})-dx_{p,d}=\frac{Mp}{4d},
 \tag{125.H11}
$$

and principal term

$$
 B_{p,n}^{\rm prin}
 =-\frac{2i}{p}q_L((X/M)p)
 \sum_{d\in I_{p,n}}
 W\!\left(\frac{Xd}{DM}\right)e\!\left(\frac{Mp}{4d}\right),
 \tag{125.H12}
$$

where

$$
 I_{p,n}=\{d>0:n<x_{p,d}<n+H\},\qquad
 |I_{p,n}|=\Theta(Q)+O(1)
 \tag{125.H13}
$$

on the central patch.  A strict-interior B-process in $d$ returns the
phase, scalar coefficient, moving profile, and selector of (125.H10).
This is a principal involution statement, not a complete hard-block
transform or an estimate.

## 3. Proof and hostile derivation

### 3.1 Exact sector algebra and conjugacy

Expanding $B_{p,n}$ and putting $h=a-b$, $k=n+b$ gives

$$
 \sum_n|B_{p,n}|^2
 =\sum_{|h|<H}(H-|h|)
   \sum_k b_{p,k+h}\overline{b_{p,k}}.
$$

Summing in $p$ proves the first identity in (125.H2).  Expanding
$|B_n|^2$ before the $p,q$ sums proves the second.  This derivation uses
the zero extension, so the change of variables does not omit block entries
or exits.  It also proves (125.H3).

For equal modes,

$$
 \sum_k b_{p,k-h}\overline{b_{p,k}}
 =\overline{\sum_k b_{p,k+h}\overline{b_{p,k}}}.
$$

For unequal modes, the map

$$
 (p,q,h,k)\longmapsto(q,p,-h,k+h)
 \tag{125.H14}
$$

conjugates the summand and preserves the real character product.  Negative
shifts and ordered pairs therefore prove reality, not cancellation.  The
only fixed set of (125.H14) is $p=q,h=0$, which is precisely
$\mathcal D_0$ and is removed from $\mathcal S_{\rm off}$.

The exact identities also expose why sector splitting is dangerous:

$$
 \mathcal S_{\rm eq}^{\ne0}=\mathcal E_p-\mathcal D_0,
 \qquad
 \mathcal S_{\rm neq}=\mathcal G_{\rm act}-\mathcal E_p.
 \tag{125.H15}
$$

Thus all of $\mathcal E_p$ cancels in their sum.  In an adversarial
coefficient control, two identical $p$-rows carrying opposite values of
$\chi _4(p)$ give $\mathcal G_{\rm act}=0$ while $\mathcal E_p$ is large;
then the unequal sector cancels the equal sector exactly.  This is not a
counterexample for the literal symbol, but it falsifies every
coefficient-blind implication from the separate positive row to the full
actual-character target.

The accepted unequal-mode identities remain

$$
 \mathcal N=p(k+h)-qk,\qquad
 \mathcal G=pk-q(k+h)=\mathcal N-(p+q)h.
 \tag{125.H16}
$$

Neither progression counting nor the strict-interior one-saddle property
estimates the actual $\chi _4(p)\chi _4(q)$ aggregate.  Replacing
$\mathcal G$ by $\mathcal N$, taking an outside $p,q$ modulus, or erasing
the character is still forbidden.

### 3.2 Curvature scale, crossing multiplicity, and the regime correction

On a central patch,

$$
 f_p'(k)\asymp D,\qquad |f_p''(k)|\asymp D/K=H_c^{-1}.
$$

Across a block of length $H$, $f_p'$ sweeps $\Theta(Q)$ integers.  More
exactly,

$$
 |I_{p,n}|
 =\frac{\sqrt{Mp}}2
  \{n^{-1/2}-(n+H)^{-1/2}\}+O(1)
 =\Theta(Q)+O(1).
 \tag{125.H17}
$$

For the equal-mode correlation
$\theta_{p,h}(k)=f_p(k+h)-f_p(k)$,

$$
 |\theta'_{p,h}(k)|\asymp\frac{D|h|}{K}
 =\frac{|h|}{H_c},\qquad
 |\theta''_{p,h}(k)|\asymp\frac{D|h|}{K^2}.
 \tag{125.H18}
$$

Hence a fixed nonzero shift has
$O(1+|h|/H_c)$ integer-gradient crossings, reaching $\Theta(Q)$ at
$|h|\asymp H$.  This is a multiplicity ledger, not a saving.

The exact primal Cauchy inequality gives

$$
 \mathcal E_p
 \le C_H H\sum_{p,n,a}|b_{p,n+a}|^2
 =H\mathcal D_0.
 \tag{125.H19}
$$

On the reciprocal principal packet, the natural diagonal mass is

$$
 C_H\sum_n\sum_p\sum_{d\in I_{p,n}}\frac4{p^2}
 \ll C_H KQ\sum_{p\asymp L}p^{-2}
 \asymp KQ\asymp X^{1/2}.
 \tag{125.H20}
$$

Bare Cauchy across $I_{p,n}$ multiplies (125.H20) by $Q$ and gives the
capacity $KQ^2=D^2/L$.  It is sharp for co-phased reciprocal entries.
However, when $Q>H$, (125.H19) is the better blind estimate.  A B-process
has then created more continuous stationary labels than primal lattice
points; they are not independent cells.  The correct best blind ledger is

$$
 \boxed{\mathcal E_p\text{ capacity }
 \asymp X^{1/2}\min(H,Q)},
 \tag{125.H21}
$$

not uniformly $QX^{1/2}$.  Since $H,Q\to\infty$, (125.H21) still misses
the target by a fixed power.  What is rigorously obstructed is a proof
whose only recombination is one of the two sharp Cauchy inequalities;
no claim is made that a phase-aware cell method must lose $Q$.

For completeness, the reciprocal central capacities are

| Treatment | Reciprocal energy ledger | Better primal/dual blind ledger |
|---|---:|---:|
| Fixed-$p$ positive row, coherent internal modes | $KQ^2=QX^{1/2}$ | $X^{1/2}\min(H,Q)$ |
| Full row, square-root only in $p$ | $KQ^2=QX^{1/2}$ | $X^{1/2}\min(H,Q)$ |
| Full row, all $p,d$ coherent | $LKQ^2=LQX^{1/2}=D^2$ | $LX^{1/2}\min(H,Q)$ |
| Fixed-$p$ row with square-root in $d$ | $KQ=X^{1/2}$ | target capacity |
| Full row with square-root in $d$ but coherent $p$ | $LKQ=LX^{1/2}$ | still loses $L$ |
| Full row with genuine joint $p,d$ square-root cancellation | $KQ=X^{1/2}$ | target capacity |

Every line is an unsigned capacity diagnostic.  In particular,
(125.H20) is the diagonal of an expansion of a modulus square but is not a
lower bound for that square: its off-diagonal terms can be negative.  An
outside modulus or Cauchy destroys precisely the cancellation still
needed.

### 3.3 Constants, moving profile, and principal self-return

At $x=x_{p,d}$,

$$
 f_p''(x)=-\frac{2d^3}{Mp}.
$$

The old unit in $b_{p,k}$ and the negative-curvature Gaussian unit are
both $e(-1/8)$.  Their product with the Hessian amplitude is

$$
 e(-1/8)M^{1/4}x^{-3/4}p^{-3/4}
 \;e(-1/8)\left(\frac{2d^3}{Mp}\right)^{-1/2}
 =-\frac{2i}{p}.
 \tag{125.H22}
$$

Also

$$
 \frac X{2D}\sqrt{\frac p{Mx_{p,d}}}=\frac{Xd}{DM},
 \tag{125.H23}
$$

while $q_L((X/M)p)$ is unchanged.  This proves (125.H12) and validates
the placement of $\chi _4(p)$ only after the $p$-rows are recombined.

For $g(d)=Mp/(4d)$,

$$
 g'(d)=-\frac{Mp}{4d^2},\qquad
 g''(d)=\frac{Mp}{2d^3}\asymp\frac KD=\frac HQ.
 \tag{125.H24}
$$

The second Fourier phase $g(d)+kd$ has saddle
$d_k=\sqrt{Mp}/(2\sqrt k)$ and critical value $\sqrt{Mpk}$.  Its positive
Gaussian unit and amplitude give

$$
 -\frac{2i}{p}e(1/8)\{g''(d_k)\}^{-1/2}
 =e(-1/8)M^{1/4}k^{-3/4}p^{-3/4}.
 \tag{125.H25}
$$

The $W$-profile in (125.H23) returns to that in (125.H10), and
$x_{p,d_k}=k$ returns the block selector.  Thus the second principal
B-process self-returns, including the constant.  Since $g'$ sweeps
$\Theta(H)$ integers across the $Q$-term packet, the two B-processes swap
the $H$ and $Q$ descriptions.  Applying Cauchy on the two sides yields the
$H$ and $Q$ losses in (125.H21); inversion supplies no gain.

This calculation does **not** cover a saddle at a block face, the precise
half-open convention, modes just outside $I_{p,n}$, nonstationary tails,
or summed errors.  Accordingly (125.H12) is a complete list of central
principal crossings, but it is not a complete transform of the hard
block.

### 3.4 Correct second-stage alias and the moving-window obstruction

Expanding the principal fixed-$p$ row gives phase

$$
 e\!\left(p\,\frac{M(d'-d)}{4dd'}\right).
 \tag{125.H26}
$$

Write $\Delta=d'-d$.  Because $p$ ranges over odd integers, choose
$A\in\mathbb Z$ nearest to

$$
 \frac{M\Delta}{2dd'},
$$

with a specified half-open tie convention, and set

$$
 E_d^*=M\Delta-2Add'.
 \tag{125.H27}
$$

Then the correct identities are

$$
 e\!\left(\frac{Mp\Delta}{4dd'}\right)
 =(-1)^A e\!\left(\frac{pE_d^*}{4dd'}\right),
 \tag{125.H28}
$$

and

$$
 (M-2Ad)(M+2Ad')-M^2=2AE_d^*.
 \tag{125.H29}
$$

The candidate's former (4a) identities are valid for the even sub-lattice
$A=2a$, but they omit all odd $A$.  At an odd half-integer
alias the candidate calls the defect far although (125.H26) is the
constant sign $(-1)^A$ throughout the odd $p$-sum.  This falsifies the
claimed alias/far partition.

For the corrected principal model, $E_d^*=0$, $A=0$ gives $d=d'$.
Its diagonal capacity is

$$
 C_H(H+O(1))\sum_{p\asymp L}p^{-2}\sum_{d\asymp D}1
 \ll DH\asymp X^{1/2}.
 \tag{125.H30}
$$

For $A\ne0$, write $d=gu$, $d'=gv$, $(u,v)=1$.  Exactness gives

$$
 M(v-u)=2Aguv.
$$

Since $(uv,v-u)=1$, $uv\mid 2M$; after $u,v$ are fixed, $Ag$ divides a
fixed integer.  The elementary divisor bound therefore gives
$O_\varepsilon(X^\varepsilon)$ nonzero exact pairs $(d,d')$ in the
central dyadic range.  Using at most $H+O(1)$ common block positions and
$C_H\sum_{p\asymp L}p^{-2}\ll1$, their absolute principal contribution is

$$
 O_\varepsilon(HX^\varepsilon)\ll X^{1/2+\varepsilon}.
 \tag{125.H31}
$$

Thus the corrected exact defects are target-safe **inside the principal
fixed-row model**.

The analogous far claim does not pass.  At fixed $(n,d)$, the hard
condition $d\in I_{p,n}$ forces

$$
 \frac{4d^2n}{M}<p<\frac{4d^2(n+H)}M,
$$

an interval of length

$$
 \asymp\frac{D^2H}{X}\asymp\frac1H=o(1).
 \tag{125.H32}
$$

The intersection for $(d,d')$ is no longer.  Therefore one cannot hold
$(n,d,d')$ fixed and perform smooth summation by parts in a length-$L$
$p$-sum.  If $n$ is summed first, the replacement weight is the exact
moving overlap

$$
 \Lambda_H(p;d,d')
 :=\#\{n:n<x_{p,d},x_{p,d'}<n+H\},
 \tag{125.H33}
$$

not a fixed smooth $p$-profile.  Its continuous triangle has an $O(1)$
floor/face discrepancy.  There are nominally $D Q$ supported
$(d,d')$ pairs, so taking that discrepancy absolutely has capacity

$$
 DQ=X^{1/2}\frac QH=X^{1/2}\frac DK,
 \tag{125.H34}
$$

which exceeds the target in the allowed regime $Q>H$.  No signed ledger
for (125.H33), the profile cutoffs, or the block faces is supplied.
Consequently even the corrected nominal window

$$
 0<|E_d^*|\lesssim D^2/L
 \tag{125.H35}
$$

is not a proved first survivor.  It is only a model obtained after an
incomplete transform of the stronger $\mathcal E_p$.

## 4. First doubtful or unproved step

The first unproved step is the passage from the strict-interior stationary
calculation (125.C5)--(125.C7) to a purported complete hard-block packet in
(125.C8)--(125.C10).  For the literal sum $a=0,\ldots,H-1$, one must fix
the half-open Poisson convention and sum, at target scale, all of the
following:

1. saddles at $x=n$ and $x=n+H$ and their Fresnel/half-weight transitions;
2. nearest-gradient ties and modes immediately outside $I_{p,n}$;
3. nonstationary positive and inactive modes;
4. entries and exits caused by literal zero extension;
5. moving $W$ and $q_L$ support transitions;
6. the second $d$-process faces and its aggregate remainder; and
7. all errors after the actual $p$-character rows are recombined, without
   an outside $p$-norm.

No such theorem or error budget is present.  Calling (125.C10) the
"complete" packet is therefore unsafe; it is the complete set of
strict-interior principal crossings only.

The first outright false seam comes later: the pre-review `4a`
nearest-integer formula uses the wrong lattice. Equations
(125.H27)--(125.H29) are the
required half-integer repair.  After that repair, (125.H32) is the next
fatal analytic seam: the moving hard selector removes the alleged
length-$L$ $p$-sum.  Hence neither the far deletion nor the nonzero
near-defect localization is established.

## 5. Control tests and outcomes

No numerical experiment or external theorem was used.  Every control was
algebraic or an asymptotic capacity calculation.

| Required control or seam | Verdict | Hostile outcome |
|---|---:|---|
| `literal_Round124_dual_offproduct_survivor` | **PASS** | (125.H2)--(125.H3) reproduce the complete scalar with the safe diagonal separated. |
| `H_K_Q_normalization` | **PASS with correction** | $K\asymp LH^2$, $H/H_c\sim Q$, and $C_H\asymp L$.  The ceiling makes these asymptotic.  Both $Q\le H$ and $Q>H$ occur, so the best blind loss is $\min(H,Q)$. |
| `bpk_profile_and_character_placement` | **PASS, principal chart** | The coefficient is (125.H10); $\chi _4(p)$ is outside $b_{p,k}$ but inside the full block sum.  It disappears only in the stronger fixed-$p$ energy. |
| `Fejer_block_square_identity` | **PASS exactly** | Zero extension gives (125.H2) with all positive and negative shifts and exact multiplicity $H-|h|$. |
| `equal_mode_offzero_vs_positive_energy` | **PASS as a distinction; FAIL as an estimate** | $\mathcal S_{\rm eq}^{\ne0}=\mathcal E_p-\mathcal D_0$.  Positivity belongs to $\mathcal E_p$, not to the off-zero sector, and no target bound for $\mathcal E_p$ is proved. |
| `equal_mode_integer_crossings_and_curvature` | **PASS with regime repair** | (125.H17)--(125.H18) give $Q$ continuous crossings and $O(1+|h|/H_c)$ shift crossings.  When $Q>H$ they are not $Q$ independent primal cells. |
| `unequal_mode_product_gradient_defects` | **PASS only as inherited algebra** | (125.H16) retains the distinction $\mathcal G=\mathcal N-(p+q)h$.  It yields no unequal-sector estimate. |
| `unequal_mode_character_persistence` | **PASS** | The full reciprocal block retains $\chi _4(p)$, and the principal second B-process returns it.  The character gives no automatic cancellation. |
| `sector_intercancellation` | **FAIL for separate-sector routes** | Equation (125.H15) shows exact cancellation of the whole positive row energy between the two sectors.  Separate absolute estimates can be genuinely overstrong. |
| `negative_shift_conjugacy` | **PASS** | (125.H14) proves reality only; negative shifts are not a saving and must not be double counted. |
| `mode_shift_multiplicity` | **PASS centrally; FAIL globally** | $|I_{p,n}|=\Theta(Q)+O(1)$ and the saddle is unique for each $d$.  Faces, ties, profile transitions, and the $Q>H$ rank issue prevent a global independent-cell count. |
| `moving_profile_and_zero_extension` | **PASS in (125.H2); FAIL in the B-process claim** | The exact block identity retains them.  Formula (125.H12) evaluates the smooth profile correctly but omits hard entries, exits, and moving overlap (125.H33). |
| `stationary_endpoint_and_error_scope` | **FAIL** | No aggregate target bound exists for hard faces, Fresnel transitions, outside modes, zero-extension edges, or either B-process remainder. |
| `signed_vs_unsigned_and_adversarial_coefficients` | **FAIL for coefficient-blind bounds** | Co-phased bounded coefficients make Cauchy sharp; opposite-character identical rows make $\mathcal E_p$ large while $\mathcal G_{\rm act}=0$.  These controls do not assert failure for the literal symbol. |
| `capacity_before_and_claimed_gain` | **PASS only after correction** | The reciprocal diagonal is $KQ=X^{1/2}$ and is not a lower bound.  Reciprocal Cauchy costs $Q$, primal Cauchy costs $H$, and the best blind ledger costs $\min(H,Q)$.  No claimed gain remains. |
| Constants in (125.C5)--(125.C7) | **PASS, strict interior** | The saddle, curvature, critical value, coefficient $-2i/p$, and profile $W(Xd/(DM))q_L((X/M)p)$ are exact at principal level. |
| Hard-block completeness of (125.C8)--(125.C10) | **FAIL** | These formulas omit the endpoint and aggregate-error modules listed in Section 4.  “Complete” must be replaced by “central principal.” |
| Second $d$-B-process self-return | **PASS locally; FAIL as a complete claim** | (125.H24)--(125.H25) return the original phase, unit, amplitude, profile, and selector at strict-interior principal level.  No endpoint-complete involution is proved. |
| Pre-review candidate (4a) alias | **FAIL; fatal correction** | Odd $p$ requires the half-integer lattice (125.H27). The proposed integer lattice omits coherent odd aliases. |
| Corrected exact $d$-defects | **PASS only in the principal positive-row model** | The diagonal is $O(X^{1/2})$ and nonzero exact pairs contribute $O_\varepsilon(HX^\varepsilon)$ by (125.H30)--(125.H31). |
| Corrected far $d$-defects | **FAIL** | The fixed-$(n,d,d')$ $p$-window has length $O(1/H)$, while summing $n$ first creates the hard moving multiplier (125.H33), whose naive face error can cost $DQ$. |
| `owner_and_downstream_scope` | **PASS for this audit** | Every stationary assertion is confined to the flat-smooth strict-UNBAL principal interior.  No nonflat, hard, sharp, clipped, starred, arithmetic, transition, TOP, BAL, M9-M2, M9, quarter-theorem, endpoint, or exponent conclusion follows. |

## 6. Dependencies and exact artifacts used

This report used only the selected context in the task brief and the
additional untrusted candidate explicitly supplied by the conductor:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/conductor_0821_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-unbalanced-joint-stationary-lattice-gate/reports/joint_stationary_lattice_hostile_audit.md`;
- `rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-unbalanced-dual-offproduct-sector-gate/candidates/conductor_curvature_cell_reciprocal_packet.md`.

No Round-125 sibling report, web source, numerical experiment, or
unlisted historical artifact was used.  All constants, capacities, alias
lattices, and factor identities were rederived algebraically.

## 7. Recommended state effect

**Recommendation: revise the curvature-cell candidate; retain only scoped
principal evidence; make no proof-state promotion.**

Retain as candidate evidence:

- the exact block-energy identities (125.H1)--(125.H5);
- the central saddle, coefficient $-2i/p$, moving profile, and
  $|I_{p,n}|=\Theta(Q)+O(1)$;
- the target-sized reciprocal diagonal as an unsigned capacity;
- the strict-interior second-B-process self-return as a method
  obstruction;
- the corrected half-integer identities (125.H27)--(125.H29); and
- target safety of the corrected exact $d$-defects inside the principal
  fixed-row model.

Reject or revise:

- “complete packet” to “central principal packet” until every hard face
  and aggregate error is target-safe;
- the claim that a cellwise proof necessarily loses $Q$ to the precise
  statement that dual bare Cauchy loses $Q$, primal bare Cauchy loses $H$,
  and the better blind capacity loses $\min(H,Q)$;
- any use of the reciprocal diagonal as a lower bound;
- the pre-review (4a) nearest-integer defect, which misses the odd
  half-integer aliases;
- the fixed-$(n,d,d')$ length-$L$ far-defect summation;
- the proposed nonzero near-$d$ window as a complete survivor; and
- every separate positive-$p$-row obstruction to the actual full target.

The exact parked survivor is

$$
 \boxed{
 \mathcal G_{\rm act}
 =C_H\sum_n\left|
   \sum_{p>0\atop p\ {\rm odd}}\chi _4(p)
   \sum_{a=0}^{H-1}b_{p,n+a}
 \right|^2},
 \tag{125.H36}
$$

with the literal moving profiles, hard block, zero extension, entries and
exits, and actual character all retained before the modulus.  Equivalently
one may park at
$\mathcal S_{\rm off}=\mathcal G_{\rm act}-\mathcal D_0$.
No smaller endpoint-complete reciprocal or near-defect functional has
been derived.  Keep
`M9-M2-smooth-unbalanced-three-quarter-estimate` open and rotate away from
this UNBAL lane unless a genuinely joint actual-character inequality for
(125.H36), or an endpoint-complete stronger inverse theorem, is supplied.
No downstream obligation or exponent changes.
