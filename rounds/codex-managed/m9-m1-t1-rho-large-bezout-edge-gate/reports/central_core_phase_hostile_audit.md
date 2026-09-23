# Round 192 hostile Farey-covector core and literal phase/carry audit

- Campaign: m9-m1-t1-rho-large-bezout-edge-gate
- Task: central_core_phase_hostile_audit
- Role: barrier/no-go
- Research round: 192
- Starting graph SHA-256:
  75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13
- Status: candidate evidence only; no shared-state edit
- Resource use: entirely analytical/algebraic; no numerical or external-theorem evidence

## 1. Result: exact sparse union, stronger deterministic coverage, and a scoped core no-go

The proposed Farey-covector union is an exact target-safe restriction of
the Round-191 rho-large remainder, provided it is defined to be empty
when \(T=0\). Fix

\[
 Q=H_B,\qquad U=mq>4Q,\qquad Qm<Y,\qquad
 T=\min\left\{\frac{U-1}{2},
       \left\lfloor\frac{QmU}{Y}\right\rfloor\right\},
\]

and, for a fixed \(C_0\geq2\), put

\[
 A=\min\{U-1,\lfloor Q^{C_0}\rfloor\},\qquad
 \mathcal F_A=\{(c,d):1\leq c\leq A,\ 0\leq d\leq c,\ (c,d)=1\}.
\]

For the canonical representative \(v_0=[v]_U\in\{1,\ldots,U-1\}\),
write

\[
 \rho v_0-\beta U=1,\qquad
 -\frac{U-1}{2}\leq\rho\leq\frac{U-1}{2},\qquad
 \ell_{c,d}=c\beta-d\rho.
\]

On \(T\geq1\), let

\[
 \mathcal E_A=\left\{v:\min_{(c,d)\in\mathcal F_A}
                      |\ell_{c,d}(v)|\leq T\right\};
\]

on \(T=0\), set \(\mathcal E_A=\varnothing\). Intersect this selector
with the exact Round-191 remainder, after its inverse-small, live-side
terminal, and isolated Fejer projections. At fixed
\((\kappa,u,m,q,a,J,\sigma)\), the resulting joint complex projection
satisfies, for every reserved \(\eta>0\),

\[
 \boxed{
 |\mathscr R_{\mathcal E_A,{\rm fix}}|
 \ll_{C_0,\eta} A^2Qm\kappa uX^{2\eta}
 \ll_{C_0,\eta}Q^{2C_0}Qm\kappa uX^{2\eta}.}
\tag{192.H1}
\]

The two orientations and all literal fields are completed before the
modulus in (192.H1). The exact \(m^{-1}c_q(a)\) lift cancels \(m\), and
the accepted coefficient, band, divisor, and shell ledger gives

\[
 \boxed{
 |\mathscr R_{\mathcal E_A,Y,Q}^{\sigma}|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon.}
\tag{192.H2}
\]

There is also a stronger deterministic coverage statement than the
small-\(U\) observation in the strategy. If \(r=|\rho|\), then for
every residue class there is a primitive \((c,d)\in\mathcal F_A\) with

\[
 \boxed{|c\beta-d\rho|
        \leq\left\lfloor\frac{r}{A+1}\right\rfloor.}
\tag{192.H3}
\]

Consequently, on \(T\geq1\), the exact complement of \(\mathcal E_A\)
can contain only

\[
 \boxed{r\geq(A+1)(T+1).}
\tag{192.H4}
\]

In particular the rho-large core is empty whenever

\[
 \boxed{
 T\geq
 \left\lfloor\frac{(U-1)/2}{A+1}\right\rfloor.}
\tag{192.H5}
\]

The proposed \(T\geq1,\ U\leq2Q^{C_0}\) coverage follows, including
all signs and endpoint fractions. Formula (192.H3) also shows that
the deterministic coverage is, in power terms, only a fixed
polylogarithmic enlargement of the already accepted inverse-small
count. Directly counting \(r\ll AT\) costs \(A\) target units and is
even cheaper than summing the \(O(A^2)\) covectors. It does not reach
the genuinely central range \(r\gg AT\).

For that remaining core, Farey separation supplies no literal signed
estimate. It has exact phase and cumulative-carry identities, derived
below, but neither identity controls a magnitude. The first literal
relation needed by an iteration is invariance or signed correlation of
the complete endpoint/mask/phase coefficient under a covector-induced
height displacement. That relation fails at the level of exact
endpoint arguments and remains wholly unproved for the fixed literal
coefficient. A positive cover of a full central residue set needs on
the order of \(U/T\asymp Y/(Qm)\) target-sized slices, or else saturates
at the positive all-row bound; either way it restores the original
\(Y/(Qm)\) deficit. Bounded zero-extended arrays attain this capacity
even after any Farey selector is imposed. This is a method-class
no-go, not literal lower mass and not a disproof of the desired
rho-large estimate.

## 2. Exact statement and hypotheses

Retain exactly the accepted Round-189 and Round-191 hypotheses:

\[
 U=mq>4Q,\quad q>Q,\quad m|a|_q>Q,\quad Qm<Y,\quad
 j_q(a,v)>T_Q,\quad U\mid u,\quad g=u/U,
\tag{192.H6}
\]

with odd \(\kappa,g,U\), \((u,v)=1\), \((U,h)=1\),
\(0<2\kappa gh<R_0\), \(u\asymp v\asymp L/\kappa\), total literal
\(v\)-support length \(O(u)\), and \(L\ll X^{1/4}\). Retain the
power-of-two projective band \(J\leq j_q(a,v)<2J\). Work only on
\(|\rho_U(v)|>T\), after the exact live-side outer terminal projection
and isolated Fejer-difference projection have already been removed.

Every orientation, outer coprimality flip, canonical carry, affine
common site, affine birth and death, endpoint arithmetic mask,
endpoint coefficient, selector, profile, floor, star, half-weight,
hard sample, crossing, endpoint trace, endpoint zero extension, actual
square-root phase, and remaining zero extension stays in the same
complex aggregate before the final real part. No selector is replaced
by a smooth or free coefficient.

Let \(\mathscr R_{\rm fix}\) be this exact Round-191 fixed-packet
remainder. Multiplication of every \(v\)-indexed atom of
\(\mathscr R_{\rm fix}\) by \(\mathbf1_{\mathcal E_A}(v)\) defines
\(\mathscr R_{\mathcal E_A,{\rm fix}}\). Define the core by complex
subtraction,

\[
 \mathscr R_{{\rm core},{\rm fix}}
 =\mathscr R_{\rm fix}-\mathscr R_{\mathcal E_A,{\rm fix}}.
\tag{192.H7}
\]

This is one union selector, not a sum of overlapping row projections.
When \(T\geq1\), its row support satisfies

\[
 |c\beta-d\rho|>T
 \quad\text{for every }(c,d)\in\mathcal F_A,
\tag{192.H8}
\]

equivalently

\[
 \left|\frac{\beta}{\rho}-\frac dc\right|
 >\frac{T}{c|\rho|}.
\tag{192.H9}
\]

When \(T=0\), (192.H8) is not asserted: the sector was deliberately
defined empty, so the exact core is the entire Round-191 remainder.

The conclusions asserted in this report are exactly:

1. the factorization and residue count (192.H11)--(192.H14) below;
2. the target-safe union and outer estimate (192.H1)--(192.H2);
3. the deterministic coverage/core condition (192.H3)--(192.H5);
4. the literal-coordinate, height-phase, carry, and endpoint identities
   (192.H22)--(192.H31); and
5. the scoped impossibility of closing the core from Farey separation,
   boundedness, support, mechanical carry, displayed phase, or positive
   recombination alone.

No complete rho-large estimate is asserted outside (192.H5).

## 3. Proof and hostile derivation

### 3.1 Canonical signs and the literal transport quotient

The signed least inverse is nonzero. If \(\rho>0\), then

\[
 0\leq\beta<\rho;
\tag{192.H10a}
\]

if \(\rho=-r<0\), write \(\beta=-b\). Then

\[
 1\leq b\leq r,
\tag{192.H10b}
\]

with equality only at the edge \(r=b=1\). In both cases
\(\beta/\rho\in[0,1]\) and
\(\gcd(|\rho|,|\beta|)=1\). The two endpoints are real: \(\rho=1\)
gives \((|\rho|,|\beta|)=(1,0)\), while \(\rho=-1\) gives
\((|\rho|,|\beta|)=(1,1)\).

For an actual literal representative, write

\[
 v=v_0+nU,\qquad
 \rho v-\gamma U=1.
\]

Comparison with the canonical Bezout identity gives the exact and
essential distinction

\[
 \boxed{\gamma=\beta+n\rho.}
\tag{192.H10c}
\]

Thus \(\beta\) is a residue-class coordinate, while \(\gamma\) is the
actual transport quotient. They coincide only for \(n=0\).

### 3.2 Exact factorization, zero cases, and divisor multiplicity

For every \((c,d)\in\mathcal F_A\), multiplication of
\(\rho v_0-\beta U=1\) by \(c\) gives

\[
 \boxed{
 \rho(cv_0-dU)=c+U(c\beta-d\rho)=c+U\ell_{c,d}.}
\tag{192.H11}
\]

The signs are unchanged when \(\rho\) or \(\ell\) is negative. Since
\(1\leq c<U\), \(c+U\ell\neq0\) for every integer \(\ell\). This strict
inequality is indispensable: if \(c=U\), the value \(\ell=-1\) would
make the right side zero.

Fix \((c,d,\ell)\) and put \(N=c+U\ell\). Formula (192.H11) implies
\(\rho\mid N\). The map from a unit class \(v_0\bmod U\) to its signed
least inverse \(\rho\) is injective. Hence

\[
 \#\{v_0\bmod U:\ell_{c,d}(v_0)=\ell\}
 \leq 2\tau(|N|).
\tag{192.H12}
\]

This is the complete factor-pair multiplicity; not every signed divisor
of \(N\) is admissible, so it is only an upper bound. There is no
additional multiplicity from \(d\) or from choosing \(v_0\): a signed
\(\rho\) determines its inverse class uniquely.

The case \(\ell=0\) has \(N=c\neq0\) and is covered by (192.H12). If
\(\ell\leq-1\), then \(N<0\), because \(c<U\), and the absolute value in
(192.H12) handles it. Since \(T\leq(U-1)/2\), \(c\leq U-1\), and
\(U\leq u\ll X^{1/4}\), all relevant \(N\) have \(|N|<U^2\ll X^{1/2}\).
The elementary divisor bound therefore gives, for \(T\geq1\),

\[
 \begin{aligned}
 \#\{v_0\bmod U:|\ell_{c,d}(v_0)|\leq T\}
 &\leq 2\sum_{-T\leq\ell\leq T}\tau(|c+U\ell|)\\
 &\ll_\eta T X^\eta.
 \end{aligned}
\tag{192.H13}
\]

Here \(2T+1\leq3T\). This is exactly why \(T=0\) cannot be included:
the isolated \(\ell=0\) classes are not \(O(T)\). More substantively,
when \(QmU/Y<1\), a single residue class that is present in the literal
support has available positive capacity
\(O(Y\kappa u/U)\), already larger in scale than \(Qm\kappa u\). Thus
this density argument cannot certify even one such class as target-safe.

The family size is

\[
 |\mathcal F_A|=2+\sum_{2\leq c\leq A}\varphi(c)\ll A^2.
\tag{192.H14}
\]

For \(c>1\), neither \(d=0\) nor \(d=c\) is primitive. At \(c=1\),
both \((1,0)\) and \((1,1)\) occur. Thus the edge cases and the central
\((2,1)\) covector are counted with the stated conventions.

### 3.3 Literal row count, overlap, and the outer power ledger

The union bound in (192.H13)--(192.H14) gives at most
\(O_\eta(A^2TX^\eta)\) eligible residue classes modulo \(U\). The
literal support has total length \(O(u)\), \(U\mid u\), and every class
occurs \(O(u/U+1)=O(u/U)\) times. Projective bands and every literal
mask only delete rows. Therefore

\[
 \#\{v\text{ literal}:v\in\mathcal E_A\}
 \ll_\eta A^2\frac{uT}{U}X^\eta
 \leq A^2\frac{Qmu}{Y}X^\eta.
\tag{192.H15}
\]

If \(T=(U-1)/2\), the inherited rho-large row set is empty, so the
conclusion is vacuous. Otherwise (192.H15) uses the exact floor only
through \(T\leq QmU/Y\).

The definition (192.H7) counts an overlapping Farey union once. The
sum over covectors is used only after that exact projection, as an
upper bound. On rho-large rows, the Round-191 identity says that the
remainder is the original endpoint-exact Abel row packet minus the
already-defined terminal and Fejer projections. Restricting all three
objects by \(\mathbf1_{\mathcal E_A}(v)\) is lawful because this selector
depends only on the row. Abel inversion first returns the original row
packet exactly. Each row then has \(O(Y)\) heights, \(O(\kappa)\) live
sites per height, and pointwise literal weight \(O_\eta(X^\eta)\).
Equation (192.H15) proves the main term in (192.H1). The restricted
terminal and Fejer projections remain bounded by their Round-191
positive estimates because rows were only deleted. They are
\(O_\eta(\kappa uX^\eta)\) and are smaller than (192.H1). No terminal
or Fejer term is counted twice.

At the outer level,

\[
 c_{mq}(ma)=m^{-1}c_q(a),\qquad
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q),\qquad
 \sum_{mq\mid u}1\leq\tau_3(u).
\tag{192.H16}
\]

Thus the \(m\) in (192.H1) cancels before positive summation. Since
\(A^2\leq Q^{2C_0}\), the complete ledger is bounded by

\[
 Q^{2C_0+1}X^{2\eta}
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u)
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon,
\tag{192.H17}
\]

after choosing \(2\eta<\varepsilon\) with room for all fixed
logarithms. The exponent \(C_0\) must be fixed independently of
\(X,Y,U\); no positive power of \(Y\), \(U\), or \(L\) is absorbed.

### 3.4 Circular-pigeonhole coverage with exact floors

Put \(r=|\rho|\) and \(b=|\beta|\). Apart from the endpoint cases
\((r,b)=(1,0),(1,1)\), one has \(1\leq b<r\) and \((b,r)=1\).
Consider the \(A+1\) points

\[
 0,b,2b,\ldots,Ab\pmod r
\]

on the circle of circumference \(r\). If \(A\geq r\), two points
coincide and give zero error with \(1\leq c\leq r\leq A\). If
\(A<r\), the points are distinct. Their \(A+1\) circular gaps sum to
\(r\), so one gap is an integer at most
\(\lfloor r/(A+1)\rfloor\). Taking the difference of its two indices
gives \(1\leq c\leq A\) and an integer \(d\) such that

\[
 |cb-dr|\leq\left\lfloor\frac r{A+1}\right\rfloor.
\tag{192.H18}
\]

Because \(0\leq cb\leq cr\), the integer \(d\) can be taken in
\([0,c]\), including the two endpoint choices. If \(s=(c,d)>1\),
divide both by \(s\). The new error is \(|cb-dr|/s\), so gcd reduction
preserves the bound, decreases \(c\), and produces a member of
\(\mathcal F_A\). For \(\rho>0\), (192.H18) is exactly a bound for
\(|c\beta-d\rho|\); for \(\rho<0\), both \(\beta\) and \(\rho\) change
sign and the absolute value is unchanged. When \(A=1\), the two gaps
are \(b\) and \(r-b\), giving either \((1,0)\) or \((1,1)\). Thus no
\(A=1\), sign, endpoint, or gcd exception remains, and (192.H3) follows.

If a row lies in the \(T\geq1\) core, (192.H3) must exceed \(T\).
Since it is integral,

\[
 \left\lfloor\frac r{A+1}\right\rfloor\geq T+1,
 \qquad r\geq(A+1)(T+1),
\tag{192.H19}
\]

which proves (192.H4). Taking \(r\leq(U-1)/2\) proves (192.H5).
If \(U\leq2Q^{C_0}\), then \(r\leq A\); more explicitly the primitive
pair

\[
 (c,d)=(|\rho|,|\beta|)
\tag{192.H20}
\]

has \(\ell_{c,d}=0\). This includes \((1,0)\) and \((1,1)\), and proves
the advertised small-\(U\) corollary. It cannot be invoked when
\(T=0\), because \(\mathcal E_A\) is then empty by definition.

The same calculation exposes the limitation. Deterministic coverage
only reaches \(r\lesssim AT\), a fixed-polylogarithmic enlargement of
the inverse-small sector. Direct inversion-class counting gives

\[
 \#\{v:r\leq(A+1)(T+1)\}
 \ll A\frac{uT}{U}+\frac{Au}{U},
\tag{192.H21}
\]

and on \(T\geq1\) this is \(O(AuT/U)\), already target-safe with only
an \(A\) polylogarithmic cost. Farey coverage is nevertheless useful
for scattered large-\(r\) classes; it is not a new cancellation
mechanism for the central bulk.

### 3.5 What the covector does to phase, carry, and literal endpoints

The exact relations are stronger than a vague appeal to a mechanical
word, but they stop before an estimate. For a literal
\(v=v_0+nU\), set

\[
 d_v=cn+d,\qquad
 \Delta_{c,d}=cv-d_vU=cv_0-dU.
\tag{192.H22}
\]

Using (192.H10c) and (192.H11) gives the two literal-coordinate
factorizations

\[
 \boxed{
 \rho\Delta_{c,d}=c+U\ell_{c,d},\qquad
 \gamma\Delta_{c,d}=d_v+v\ell_{c,d}.}
\tag{192.H23}
\]

The second identity follows from
\(\gamma(cv-d_vU)=v(c\gamma-d_v\rho)+d_v\). It is the first place
where the canonical/literal distinction is fatal to a naive endpoint
argument: \(d_v=cn+d\) varies with the actual representative and need
not be small even when \(c,d,\ell\) are small.

Since \(\rho\equiv\bar v_q\pmod q\), the retained row phase is

\[
 z_{\omega,v}=e(\epsilon_\omega a\rho/q).
\]

The covector displacement satisfies the exact phase law

\[
 \boxed{
 z_{\omega,v}^{\Delta_{c,d}}
 =e(\epsilon_\omega ac/q).}
\tag{192.H24}
\]

The magnitude and sign of \(\ell\) disappear. The right side can equal
one when \(q\mid c\), and otherwise can be arbitrarily close to one;
the core condition gives no lower bound for it. Moreover, whenever it
is not one, the corresponding long-step Abel identity is merely

\[
 \frac1{1-z^{\Delta}}
 \sum_h\{W(h)-W(h-\Delta)\}z^h
 =\sum_hW(h)z^h.
\tag{192.H25}
\]

Thus a covector-step coboundary is an exact self-return unless a new
bound for the literal differences is proved. When \(z^\Delta=1\),
even this normalization is unavailable.

The cumulative carry is also exact. The canonical anchors satisfy
\(S_{0,\omega}(h)\equiv\epsilon_\omega\rho h\pmod U\). Define the
signed cumulative carry over \(\Delta=\Delta_{c,d}\) by

\[
 N_\omega(h;\Delta)=
 \frac{S_{0,\omega}(h+\Delta)-S_{0,\omega}(h)
       -\epsilon_\omega\rho\Delta}{U}.
\tag{192.H26}
\]

Using \(\rho\Delta=c+U\ell\),

\[
 N_\omega(h;\Delta)
 =\theta_{\omega,c}(h)-\epsilon_\omega\ell,
\tag{192.H27}
\]

where

\[
 \theta_{+,c}(h)\in\{-1,0\},\qquad
 \theta_{-,c}(h)\in\{0,1\}
\tag{192.H28}
\]

is the single endpoint wrap caused by adding \(+c\) or \(-c\) to the
canonical anchor. For positive \(\Delta\), (192.H26) is the sum of the
Round-191 adjacent carries; for negative \(\Delta\), it is the reversed
signed sum. Hence the product of the retained mode-and-affine factors
over the displacement is

\[
 \boxed{
 (-1)^{N_\omega(h;\Delta)}e(\epsilon_\omega ac/q).}
\tag{192.H29}
\]

The core lower bound on \(|\ell|\) says nothing about its parity, the
endpoint wrap, or the distance of (192.H29) from \(1\). It supplies no
carry cancellation.

Finally, let \(A_0=\kappa gU\) and \(C_v=\kappa v\). On a plus fibre,
forward transport by \(\Delta\) shifts \((S,w)\) by
\((\rho\Delta,\gamma\Delta)\). The two ordered endpoint arguments
therefore change by

\[
 \boxed{
 \Delta N_{0,+}=2A_0(d_v+v\ell),\qquad
 \Delta N_{1,+}=2gC_v(c+U\ell).}
\tag{192.H30}
\]

On a minus fibre, forward transport shifts by the negatives and the
endpoint order is reversed:

\[
 \boxed{
 \Delta N_{0,-}=-2gC_v(c+U\ell),\qquad
 \Delta N_{1,-}=-2A_0(d_v+v\ell).}
\tag{192.H31}
\]

These translations are unequal and nonzero even at \(\ell=0\). They
move squarefree, divisibility, allocation-coprimality, residual,
selector, profile, floor, star, half-weight, hard-sample, crossing,
trace, and endpoint-zero fields. They also change the square-root
phase through two nonlinear square-root increments with the same
\(\sigma\), not through opposite conjugate increments. Positivity can
fail along the transport, producing the inherited births and deaths.
The height mask \(\mathbf1_{(U,h)=1}\) is not invariant under
\(h\mapsto h+\Delta\), since \(\Delta\equiv cv_0\pmod U\). Farey
primitivity \((c,d)=1\) does not repair any of these facts.

Thus (192.H24), (192.H27), and (192.H30)--(192.H31) are the complete
lawful coupling presently available. None is an amplitude-correlation
estimate.

### 3.6 Quantitative full-cover and bounded-array barriers

There are arithmetic parameter packets in which the exact core is
large at residue-class level. As a clean control, take \(m=1\) and
\(q=U=p\) prime, choose a unit \(a\) with \(|a|_p>Q\), and take an
unsaturated \(T=\lfloor Qp/Y\rfloor\). In the signed inverse variable,
the rho-small set has at most \(2T\) classes and the projectively slow
set \(|a\rho|_p\leq T\) has at most \(2T\) classes. Hence at least

\[
 p-1-4T
\tag{192.H32}
\]

classes meet both inherited fast predicates. By (192.H13)--(192.H14),
at most \(O_\eta(A^2Tp^\eta)\) of them lie in \(\mathcal E_A\). Along
packets with \(p\gg A^2Tp^\eta\), a positive proportion remain in the
core. One of the \(O(\log p)\) projective bands then contains the
corresponding proportion up to a logarithm. This is a residue-universe
control only: literal masks may delete rows, so it is not physical lower
mass.

More generally, a family of \(M\) covectors certified only by
(192.H13) covers at most \(O_\eta(MTX^\eta)\) residue classes. Covering
an \(\asymp U\) central set therefore requires, up to divisor slack,

\[
 M\gtrsim\frac{U}{T}X^{-\eta}
 \asymp\frac{Y}{Qm}X^{-\eta}.
\tag{192.H33}
\]

Positive recombination of \(M\) fixed-covector estimates consequently
restores the same factor \(Y/(Qm)\). Taking all Farey fractions to an
order large enough for deterministic full coverage costs quadratically
many fractions and is worse; bounding their union directly caps only
at the all-row positive estimate \(Y\kappa uX^\eta\). No cover can turn
that positive mass into \(Qm\kappa uX^\varepsilon\) without a signed
property of the actual coefficient.

This obstruction is sharp for the coefficient-uniform class. For any
set \(\mathcal C\) of selected oriented rows, including the exact Farey
core, and finite height sets \(H_r\), endpoint-exact Abel summation gives

\[
 \sup_{|W_r(h)|\leq1}
 \left|
 \sum_{r\in\mathcal C}\frac1{1-z_r}
 \sum_h\Delta^-W_r(h)z_r^h
 \right|
 =\sum_{r\in\mathcal C}|H_r|.
\tag{192.H34}
\]

The extremizers \(W_r(h)=\overline z_r^{\,h}\mathbf1_{H_r}(h)\) are
lawful zero-extended arrays and make all rows reinforce under one
complex operation; prescribed square-root phases can be conjugated as
well. Farey separation neither changes (192.H34) nor creates a common
height coefficient. For \(m>1\), distinct inverse classes may also
alias modulo \(q\), so the core is not even a frequency-separated set
at the retained phase level. Equation (192.H34) rejects only proofs
uniform over bounded arrays, positive completions, separable norms, or
phase/carry data. It neither realizes the fixed literal endpoint
coefficient nor disproves its desired signed estimate.

## 4. First doubtful or unproved step

There is no doubtful step in the canonical sign analysis, the
factorization, \(c<U\) nonvanishing, divisor-pair count, \(\ell=0\) and
negative-\(\ell\) cases, \(T=0\) convention, literal multiplicity,
overlap-safe union, \(A^2\) family cost, outer ledger, circular
pigeonhole lemma, gcd reduction, exact floors, phase identity,
cumulative carry identity, or endpoint translations.

After removing the target-safe union, the first unproved relation is
the fixed-packet estimate

\[
 \boxed{
 |\mathscr R_{{\rm core},{\rm fix}}|
 \stackrel{?}{\ll}_{\varepsilon,C_0}
 Qm\kappa uX^\varepsilon.}
\tag{192.H35}
\]

The inherited final theorem needs only the corresponding one-sided
outer-real-part estimate, but (192.H35) would be a sufficient stronger
input. The first failed literal step in a covector iteration is an
identity or estimate of the form

\[
 B_{\omega,h+\Delta}^{\rm tr}
 \stackrel{?}{\approx} B_{\omega,h}
\tag{192.H36}
\]

for the complete coefficient. Equations (192.H30)--(192.H31) show
that the two endpoint arguments undergo unequal translations involving
the representative-dependent \(d_v=cn+d\); arithmetic masks and
literal cells can flip and affine sites can be born or die. Thus
(192.H36) is not an exact relation, and no selected context proves a
signed substitute. The phase/carry factor (192.H29) does not control
this coefficient difference.

Without such a theorem, positive control remains

\[
 |\mathscr R_{{\rm core},{\rm fix}}|
 \ll_\eta Y\kappa uX^\eta,
\tag{192.H37}
\]

against the target \(Qm\kappa uX^\varepsilon\). The exact deficit is
\(Y/(Qm)>1\). The lower bound (192.H4) on \(|\rho|\) is not row
sparsity; it removes a small inverse interval and leaves the central
bulk. A future proof must use a jointly signed correlation of the
fixed literal endpoint, arithmetic, carry, and square-root-phase
fields before any positive norm.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| exact_round191_rho_large_remainder | PASS: (192.H6)--(192.H7) split only the exact \(|\rho|>T\) remainder. |
| round191_terminal_and_Fejer_already_removed | PASS: the new projection starts from \(\mathscr R_{\rm fix}\); restricted terminal/Fejer terms are used only to bound the exact restriction and are not re-added to the core. |
| canonical_v0_vs_literal_v_vs_transport_gamma | PASS: \(v=v_0+nU\) and \(\gamma=\beta+n\rho\) are explicit in (192.H10c); \(d_v=cn+d\) appears in the literal identities. |
| signed_least_inverse_and_beta_signs | PASS: (192.H10a)--(192.H10b) cover positive and negative \(\rho\), including ratios \(0\) and \(1\). |
| exact_unimodular_covector_factorization | PASS: canonical (192.H11) and literal (192.H23) are exact with both signs. |
| c_strictly_less_than_U_nonzero_rhs | PASS: \(A\leq U-1\); \(c+U\ell=0\) is impossible. |
| T_zero_sector_empty | PASS: \(\mathcal E_A=\varnothing\) at \(T=0\); no isolated zero class is charged to zero density. |
| ell_zero_and_floor_cases | PASS: \(\ell=0\) has nonzero factor \(c\); \(2T+1\leq3T\) only for \(T\geq1\); saturated \(T\) leaves no rho-large rows; (192.H3)--(192.H5) retain exact floors. |
| divisor_pair_multiplicity | PASS: a class injects into a signed divisor \(\rho\mid c+U\ell\), giving at most \(2\tau(|c+U\ell|)\), with no extra \(v_0\) multiplicity. |
| Farey_family_size_polylogarithmic | PASS conditionally on fixed \(C_0\): \(|\mathcal F_A|\ll A^2\leq Q^{2C_0}\), absorbed only through a fresh epsilon budget. |
| overlap and primitive endpoints | PASS: the exact union selector counts a row once; union bound is applied later; gcd reduction, \(A=1\), \((1,0)\), and \((1,1)\) are audited in Section 3.4. |
| one_outer_real_part_both_orientations | PASS: both orientations remain in one complex projection; the safe union is bounded only after its joint definition, and the core remains a complex subtraction. |
| no_literal_field_dropped | PASS: Section 2 freezes every Round-191 field; (192.H30)--(192.H31) show why none is invariant or discardable. |
| exact_badly_approximable_core | PASS as a description only: (192.H8)--(192.H9), strengthened by \(r\geq(A+1)(T+1)\); \(T=0\) is separately stated. |
| deterministic coverage | PASS: circular pigeonhole proves (192.H3), full coverage (192.H5), and the advertised \(U\leq2Q^{C_0}\) corollary. |
| no_false_Farey_full_cover_without_sector_cost | PASS: beyond (192.H5), the prime residue control and (192.H33) show that a coefficient-blind full cover needs the missing \(U/T\asymp Y/(Qm)\) capacity, up to divisor slack. |
| phase coupling | PASS as an audit, FAIL as a saving: \(z^\Delta=e(\epsilon ac/q)\) is exact but independent of \(|\ell|\); long-step Abel is the self-return (192.H25). |
| carry coupling | PASS as an audit, FAIL as a saving: cumulative carry is \(\theta-\epsilon\ell\), but the core controls neither parity, endpoint wrap, nor distance of (192.H29) from one. |
| endpoint displacement | PASS as an audit, FAIL as invariance: (192.H30)--(192.H31) retain unequal, representative-dependent translations and all resulting births, deaths, masks, and phases. |
| no_bounded_array_or_positive_completion_closure | PASS: (192.H34) has full capacity on the selected core; it is expressly quarantined from literal realizability. |
| Q_L_Y_X_power_and_epsilon_budget | PASS: (192.H17) has \(Q^{2C_0+1}\), the exact \(m^{-1}\) cancellation, \(\tau_3\), coefficient/band logarithms, \(L^2\), and no absorbed positive \(Y\)-power. |
| diagnostic_only_computation | PASS: no computation was used. |
| original_t1_only_downstream_scope | PASS: even a future proof of (192.H35) would close at most the exact original-\(t=1\) residual through accepted connectors. |
| exponent_quarantine | PASS: no internal, external, target, parent, bridge, or theorem exponent is changed. |

## 6. Dependencies and exact artifacts used

Only the assigned brief and its exact selected context were used:

1. rounds/codex-managed/m9-m1-t1-rho-large-bezout-edge-gate/briefs/central_core_phase_hostile_audit.md
   — SHA-256
   ed5c41f87de2fbc3da3e1a6151710081d9e632da8fc4961b64ea18e60e8e64df.
2. protocol.md — SHA-256
   f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
3. state/proof_obligations.yml — SHA-256
   75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13.
4. state/active_campaign.yml — SHA-256
   4a1f3d9e8de532ac6977bc1350a999b155b53cb170e0e10f1874f098850d29b1.
5. state/failure_ledger.md — SHA-256
   1bb5488f73b9a272fd6e79706604272e071a560f521c2f1e4a7e348f30fc2456.
6. strategy/round192_m1_t1_rho_large_farey_covector_strategy.md
   — SHA-256
   2642ac2cebf718e156f8599791394fdb7270bad8b3ca58665b68476ddb87a4f7.
7. proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md
   — SHA-256
   7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2.
8. proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md
   — SHA-256
   31092b28826b9f36ecaedfb5efc5d7625f4caa4da2cf4c37bd48389c6ac6ee58.
9. rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/reports/joint_hv_phase_jump_hostile_audit.md
   — SHA-256
   902ea86fd79cef97ab2a4e3ad0f92457b49d13c97212a03be70078ada656b22e.
10. rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/reviews/final_kernel_power_literal_owner_scope_post_hygiene_verification.md
    — SHA-256
    8193106f54a970fb50713a6e9e5f8e792ac7c261f22afb3ae5086ca9e31aeb5e.
11. rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/reviews/conductor_round191_adjudication.md
    — SHA-256
    89a2c793e4ca1e693322e363834c19ebfcaf175718ed3e61cbe98d8ff2a32bda.

No sibling Round-192 artifact, unassigned kernel, web source, external
theorem, or numerical diagnostic was read or used.

## 7. Recommended state effect

**Revise the Round-192 candidate and retain every parent status.**

1. After independent normalization, literal-scope, power, and blind
   review, promote only the exact target-safe Farey-union restriction
   (192.H1)--(192.H2), its exact complex complement (192.H7), and the
   deterministic coverage/core lemma (192.H3)--(192.H5). Record that
   the coverage lemma is dominated in its contiguous \(r\lesssim AT\)
   range by a direct polylogarithmically enlarged inverse-class count.
2. Keep the exact central core (192.H8), (192.H19), and its target
   (192.H35) open. Its first missing input is a jointly signed theorem
   for the actual coefficient under the endpoint translations
   (192.H30)--(192.H31), not another positive cover.
3. Reject as closures: Farey separation by itself, iterative positive
   covector covering, long-step Abel, magnitude of the mechanical carry,
   parity of a large \(\ell\), phase-only nonresonance, assumed endpoint
   transport invariance, separate orientation norms, bounded-array
   estimates, positive completion, and alias/large-sieve energy without
   a common literal coefficient.
4. Retain the prime residue and bounded-array constructions only as
   mechanism controls. Assert no literal lower mass and no failure of
   the desired fixed-coefficient rho-large estimate.
5. Keep open every original \(t\geq2\) small-\(G\) incidence, the
   large-\(G\) near-resonant complement, the remaining small-\(t\)
   owner, hard and smooth M1, GAR, every M2 parent, endpoint uniformity,
   M9, both bridges, and the quarter theorem. Keep the internal
   \(1/3\), accepted external
   \(0.3144831759740614\ldots\), and target \(1/4\) exponents unchanged.

Recommended Round-192 label for this report:

    farey_sparse_union_and_exact_core_phase_carry_no_go
