# Round 171 discovery report: literal two-defect commutator attack

- Campaign: `m9-m2-balanced-critical-j1-two-defect-commutator-gate`
- Task: `literal_two_defect_commutator_attack`
- Role: discovery
- Starting graph: `4c98bb13558c06159c5ad23128c6f6ff52970db296863858832309a24a4720ac`
- Allocation used: 100% analytic/algebraic, 0% numerical
- Terminal label recommended: `balanced_two_defect_commutator_no_go`

## 1. Result

**Result type: exact coordinate and axial lemma, followed by a scoped
translation-commutator/summation-by-parts no-go.**

For the complete literal persistent critical (j=1) block, the passage

\[
 (h,k,h',k')\longleftrightarrow (h,k,p,q),
 \qquad p=h'-h,\qquad q=k'-k,
\]

is a multiplicity-one bijection after the original positive support and the
two strict far gates are imposed.  On character support (p=2s), and

\[
 \chi _4(h)\chi _4(h+2s)=(-1)^s.
\]

The sectors (p=0) and (q=0) are not empty in the double-far region, but
each has absolute literal mass (O_\varepsilon(L^3X^\varepsilon)).  They
are therefore target-safe without division.

Put

\[
 U:=\Delta+\rho=q(h+h'),\qquad
 V:=\Delta-\rho=p(k+k'),
\]

and let (D_s=T_s-1), (D_q=T_q-1), where (T_s) sends (p) to (p+2)
and (T_q) sends (q) to (q+1).  The two canonical defect
commutators are exactly

\[
 [D_q,M_U]=(h+h')T_q,
 \qquad
 [D_s,M_V]=2(k+k')T_s.
\tag{1.1}
\]

Consequently their normalized forms are merely the two commuting shifts:

\[
 {1\over h+h'}[D_q,M_U]=T_q,
 \qquad
 {1\over 2(k+k')}[D_s,M_V]=T_s,
 \qquad [T_s,T_q]=0.
\tag{1.2}
\]

Thus the defect factorizations do **not** produce a nonzero normalized
two-direction commutator.  The apparent side-length denominators in
(1.1) give no (L^{-1}): after summation by parts they cancel against
(U/(h+h')=q) and (V/(2(k+k'))=s).

The unnormalized parity-compatible diagonal commutator is nonzero, but
equals \(8(y-x)T_sT_q^2\), with \(x=h+h'\), \(y=k+k'\).  The exact or
constant-width \(y=x\) strip is target-safe by one linear relation.
Off that strip, division by \(y-x\) cancels the same commutator multiplier
and recovers only the alternating diagonal difference, still at \(L^4\)
capacity.  In the actual-real endpoint-swap decomposition,
\(\tau_h\tau_k\mathscr W=\mathscr W\), so the cross projections vanish
exactly; the unique uncaptured parity complement is the \((++)\) piece,
whose positive capacity remains \(L^4X^\varepsilon\).

There is an exact universal two-direction summation-by-parts identity.  If
(F_{h,k}(s,q)) is the complete zero-extended literal summand after removing
the character product, then, for any fixed (q_0),

\[
 \mathcal R_B^{\rm osc}
 ={1\over2}\sum_{h,k,s,q}(-1)^s(q-q_0)
 D_sD_qF_{h,k}(s,q).
\tag{1.3}
\]

However the factor (q-q_0) is unavoidable: the discrete adjoint equation
for summation by parts against the constant (q)-weight forces every
primitive to vary by one per lattice step.  On a (q)-run of length
\(\asymp L\), its supremum is at least a constant times (L).  In the
literal four-corner expansion, this multiplier amplifies the already
target-saturating gate/support boundary allowance from (L^3) to (L^4),
and the bulk retains an undifferenced literal coefficient times a full-size
mixed exponential difference.  The one-direction character identity has
only (L^4) positive capacity; (1.3) has (L^5) coefficient-blind capacity.
No factor (L) is saved before a positive norm.

This is the first rigorous failed gate for this placement.  It rejects the
canonical local translation/defect commutator and coefficient-independent
two-step Abel mechanism.  It is **not** a lower bound for the physical
scalar, a disproof of the target, or a no-go for a future genuinely signed
actual-symbol theorem.

## 2. Exact statement and hypotheses

### 2.1 Literal block and zero extension

Let (X\ge4096) be real, (R=\sqrt X), (y=\lfloor R\rfloor), and let
(B=(X,j=1,r,+)) be one persistent critical balanced residual block.  Thus

\[
 D=2^{-1}y,\qquad H=\lfloor DX^{-1/4}\rfloor,\qquad
 L=2^{-r}H\asymp X^{1/6},\qquad
 K={XL\over D^2},\qquad M=LK,
\]

with (K/L=4X/y^2\asymp1).  Every floor, clipped endpoint, half-open
profile convention, star, crossing, and fixed physical-block label is the
one in the accepted literal dictionary.  On the positive quadrant the
continuum core is

\[
 A_B(x,z)=W(x/L)\Phi(x/(H+1))
 \left({M\over xz}\right)^{3/4}
 W\!\left(\sqrt{{xX\over4zD^2}}\right),
\tag{2.1}
\]

with the actual clipped profiles of (B), and it is extended by zero off
the literal support.  In the notation of the target put

\[
 G_0={\sqrt L\over2},\qquad
 b_B(h,k)=\eta\!\left({(h,k)\over G_0}\right)A_B(h,k),
 \qquad a_B^<(h,k)=\chi _4(h)b_B(h,k).
\tag{2.2}
\]

No gcd expansion, shift shell, divisor class, quarter-shift packet, lift,
alias, or endpoint is put outside the fixed-block sum.  Formula (2.2) is
the coefficientwise recombination of both quarter shifts furnished by the
accepted dictionary.  The bounds and supports of the literal profiles give

\[
 |b_B(h,k)|\ll1,\qquad
 \#\{(h,k):b_B(h,k)\ne0\}\ll L K\ll L^2,
\tag{2.3}
\]

with harmless (X^\varepsilon) factors when divisor expansions are used.

### 2.2 Exact coordinate domain

Let

\[
 \mathcal S_B=\{(h,k)\in\mathbb Z_{>0}^2:b_B(h,k)\ne0\}.
\]

The original ordered domain is

\[
 \Omega_B=\left\{
 (h,k,h',k')\in\mathcal S_B^2:
 h,h'\ {\rm odd},\quad
 |h'k'-hk|>L,\quad |hk'-h'k|>L
 \right\}.
\tag{2.4}
\]

Its exact increment chart is

\[
 \begin{aligned}
 \mathcal D_B=\{(h,k,p,q)\in\mathbb Z^4:\;&(h,k)\in\mathcal S_B,
 \ (h+p,k+q)\in\mathcal S_B,\ h,h+p\ {\rm odd},\\
 &|hq+kp+pq|>L,\quad |hq-kp|>L\}.
 \end{aligned}
\tag{2.5}
\]

Negative (p,q) are retained; positivity is exactly the condition
((h+p,k+q)\in\mathcal S_B).  Strict inequalities, rather than rounded or
smoothed gates, are used.  The map and inverse are

\[
 (h,k,h',k')\mapsto(h,k,h'-h,k'-k),
 \qquad
 (h,k,p,q)\mapsto(h,k,h+p,k+q).
\tag{2.6}
\]

They are mutually inverse, so every ordered pair has multiplicity one.
The swap of the ordered atoms is the involution

\[
 (h,k,p,q)\mapsto(h+p,k+q,-p,-q).
\tag{2.7}
\]

There is no fixed point in the double-far domain.  In particular no factor
two, primitive-ray multiplicity, gcd multiplicity, or unordered-pair
normalization is introduced by (2.6).

### 2.3 Scoped no-go theorem

For fixed (h,k), set (p=2s), (h_s=h+2s), (k_q=k+q), and define

\[
 \begin{aligned}
 \Delta_{s,q}&=h_sk_q-hk=hq+2ks+2sq,\\
 \rho_{s,q}&=hk_q-h_sk=hq-2ks,\\
 \theta_{s,q}&=R(\sqrt{hk}-\sqrt{h_sk_q}),\\
 \mathfrak g_{s,q}&=
 1_{|\Delta_{s,q}|>L}1_{|\rho_{s,q}|>L},\\
 C_{h,k}(s,q)&=b_B(h,k)\overline{b_B(h_s,k_q)},\\
 F_{h,k}(s,q)&=\mathfrak g_{s,q}C_{h,k}(s,q)
 [e(\theta_{s,q})-1],
 \end{aligned}
\tag{2.8}
\]

where all functions are zero when either atom leaves its literal support.
Then

\[
 \mathcal R_B^{\rm osc}
 =\sum_{\substack{h\ {\rm odd},\,k>0\\s,q\in\mathbb Z}}
 (-1)^sF_{h,k}(s,q).
\tag{2.9}
\]

The theorem proved below is:

> The chart (2.5) is exact and the two axial sectors of (2.9) are
> target-safe.  Nevertheless the coordinate translations and the two
> multiplication operators supplied by the factorizations admit no
> nonzero normalized commutator: they reduce to commuting shifts.  Any
> coefficient-independent second summation by parts in the uncharactered
> (q)-direction requires a primitive of size \(\gg L\) on a full balanced
> fibre.  Hence this commutator/SBP placement cannot lower the positive
> (L^4X^\varepsilon) capacity to (L^3X^\varepsilon) before positive
> norms, even after all one-step boundaries are written exactly.

The conclusion is restricted to this operator placement.  A future theorem
that estimates the complete signed (q)-aggregate using the actual gcd,
slanted, alias, and character structure is outside the no-go.

## 3. Proof or derivation

### 3.1 Coordinate algebra, character, and multiplicity

Substitution of (h'=h+p), (k'=k+q) gives coefficientwise

\[
 \Delta=hq+kp+pq,\qquad \rho=hq-kp,
\]

and therefore

\[
 \boxed{\Delta+\rho=q(2h+p)=q(h+h'),\qquad
 \Delta-\rho=p(2k+q)=p(k+k').}
\tag{3.1}
\]

The inverse (2.6) proves the multiplicity ledger independently of (3.1);
the factorizations are not being used as an inverse map.  Since nonzero
(\chi _4) forces (h,h') odd, (p=2s).  The elementary relation
(\chi _4(n+2)=-\chi _4(n)) for odd (n) yields

\[
 \chi _4(h)\chi _4(h+2s)=(-1)^s.
\tag{3.2}
\]

This sign is constant in (h,k,q) on every fixed-(p) fibre.  It supplies
no inner-(h) cancellation there.

### 3.2 Axial sectors

If (p=0), then

\[
 \Delta=\rho=hq,
\]

so both strict far gates reduce to (|hq|>L); this sector is generally
nonempty.  There are (O(L)) choices for (h) and (O(K^2)) ordered
choices for (k,k'), and the bracket has modulus at most (2).  Thus

\[
 \sum_{\substack{\Omega_B\\p=0}}
 |a_B^<(h,k)a_B^<(h',k')|
 |e(\theta)-1|
 \ll LK^2X^\varepsilon\ll L^3X^\varepsilon.
\tag{3.3}
\]

If (q=0), then

\[
 \Delta=kp,\qquad \rho=-kp,
\]

and the same argument gives

\[
 \sum_{\substack{\Omega_B\\q=0}}
 |a_B^<(h,k)a_B^<(h',k')|
 |e(\theta)-1|
 \ll KL^2X^\varepsilon\ll L^3X^\varepsilon.
\tag{3.4}
\]

Their intersection has \(\Delta=\rho=0\) and is absent.  Equations
(3.3)--(3.4) prove, rather than delete, both axial sectors.  They also show
why division by (p) or (q) is neither needed nor lawful on the full
domain.

### 3.3 The exact defect commutators collapse to shifts

On zero-extended arrays in ((s,q)), let

\[
 T_sf(s,q)=f(s+1,q),\quad T_qf(s,q)=f(s,q+1),
 \quad D_s=T_s-1,\quad D_q=T_q-1.
\tag{3.5}
\]

Write

\[
 A=h+h'=2h+2s,\qquad B=k+k'=2k+q,\qquad
 U=qA,\qquad V=2sB.
\tag{3.6}
\]

Both (A) and (B) are strictly positive throughout the literal domain.
Direct calculation gives

\[
 D_sU=2q,\qquad D_qU=A,\qquad
 D_sV=2B,\qquad D_qV=2s.
\tag{3.7}
\]

For a multiplication operator (M_w),

\[
 [D_x,M_w]f=(D_xw)T_xf.
\tag{3.8}
\]

Equations (3.7)--(3.8) prove (1.1), and hence

\[
 \mathcal N_q:={1\over A}[D_q,M_U]=T_q,\qquad
 \mathcal N_s:={1\over2B}[D_s,M_V]=T_s.
\tag{3.9}
\]

The two cross choices give

\[
 [D_s,M_U]=2qT_s,\qquad [D_q,M_V]=2sT_q.
\]

After the axial sectors are removed, normalizing by \(2q\) or \(2s\)
again gives \(T_s\) or \(T_q\).  On the axes those normalizations are
undefined, which is exactly why (3.3)--(3.4), rather than division, are
required.  Thus none of the four defect/direction pairings produces a new
operator after normalization.

Thus

\[
 [\mathcal N_s,\mathcal N_q]=0
\tag{3.10}
\]

coefficientwise, including on every gate, gcd, profile, alias, and ruling
class after zero extension.  There is no remainder in (3.10) that could
equal the target summand.

Leaving the operators unnormalized does not help.  If

\[
 \mathcal C_s=[D_s,M_V]=2BT_s,\qquad
 \mathcal C_q=[D_q,M_U]=AT_q,
\]

then

\[
 [\mathcal C_s,\mathcal C_q]
 =2(2B-A)T_sT_q.
\tag{3.11}
\]

This has a coefficient of size (O(L)), not (L^{-1}).  If the affine slice
(2B=A) meets a chosen support, it also has a zero there.  On any subdomain
where (2B-A) is bounded away from zero, division merely turns (3.11) into
the tautological shift (T_sT_q): the size-(L) commutator coefficient
exactly repays the apparent size-(L) denominator.  Normalizing the two
individual defect directions by the always-positive side sums returns
exactly the zero commutator (3.10).

There is a second, parity-compatible **diagonal-shift audit**.  Put

\[
 x:=A=h+h',\qquad y:=B=k+k',\qquad
 \widehat T_q:=T_q^2,\qquad \widehat D_q:=\widehat T_q-1.
\]

Thus both \(T_s\) and \(\widehat T_q\) move their increment variable by
two.  Since

\[
 D_sV=2y,\qquad \widehat D_qU=2x,
\]

the corresponding unnormalized multiplier commutators are

\[
 \mathfrak P:=[D_s,M_V]=2yT_s,\qquad
 \mathfrak Q:=[\widehat D_q,M_U]=2x\widehat T_q.
\tag{3.11a}
\]

Now \(T_sx=x+2\), while \(\widehat T_qy=y+2\), and the two shifts commute.
Therefore

\[
\begin{aligned}
 [\mathfrak P,\mathfrak Q]
 &=4\{y(x+2)-x(y+2)\}T_s\widehat T_q\\
 &=8(y-x)T_s\widehat T_q.
\end{aligned}
\tag{3.11b}
\]

This explicitly resolves the fact that an **unnormalized** multiplier
commutator need not vanish even though the normalized shifts commute.  It
still gives no saving.  Off the locus \(y=x\), division by its
\(O(L)\) multiplier yields exactly

\[
 {[\mathfrak P,\mathfrak Q]\over8(y-x)}
 =T_s\widehat T_q.
\tag{3.11c}
\]

Subtracting the identity recovers only the alternating diagonal
difference

\[
 D_{\rm diag}:=T_s\widehat T_q-1,\qquad
 \sum_{s,q}(-1)^sD_{\rm diag}F(s,q)
 =-2\sum_{s,q}(-1)^sF(s,q).
\tag{3.11d}
\]

Thus the apparent \(1/L\) from \(1/(y-x)\) is exactly repaid by the
multiplier in (3.11b); after recombination (3.11d) has the original
\(L^4\) positive capacity and a full-size phase difference.  On the
singular locus \(y=x\), the raw commutator in (3.11b) is zero and division
is illegal.  If that locus is absent from a particular clipped support,
(3.11c) remains merely a shift identity; if it is present, it is an
additional exact boundary/ruling that must be retained.  It is nevertheless
target-safe as a slice: for a fixed integer \(t=y-x\), choosing
\((h,h',k)\) determines

\[
 k'=h+h'+t-k,
\]

so the literal support contains \(O(L^3)\) quadruples on \(y-x=t\).
Consequently every fixed-width strip \(|y-x|\le C\) has absolute mass
\(O_C(L^3X^\varepsilon)\).  On its complement one may dyadically divide
by \(|y-x|\), but (3.11b) supplies the same factor \(|y-x|\) in the
commutator numerator.  The factors cancel coefficientwise before any
estimate, leaving (3.11c)--(3.11d), not an \(L^{-1}\) gain.  Hence neither
the singular strip nor its complement closes the target.

Finally, using either identity in (3.9) under a sum exposes the cancellation
of the apparent side-length denominator.  For example

\[
 {U\over A}=q,\qquad {V\over2B}=s.
\tag{3.12}
\]

Thus discrete integration by parts produces coordinate multipliers of
length (L), not a gain (L^{-1}).

#### Actual-real endpoint-swap parity audit

There is one further exact symmetry seam.  On zero-extended ordered
quadruples define the endpoint swaps

\[
\begin{aligned}
 \tau_h(h,k,h',k')&=(h',k,h,k'),\\
 \tau_k(h,k,h',k')&=(h,k',h',k).
\end{aligned}
\tag{3.12a}
\]

They commute and their product swaps the two complete atoms.  Let
\(\mathscr F\) be the complete complex literal summand, including both
strict gates, and let

\[
 \mathscr W:={1\over2}
   \{\mathscr F+\tau_h\tau_k\mathscr F\}.
\tag{3.12b}
\]

All literal coefficients are real in the accepted block dictionary.
Under the full atom swap, \(\Delta,\rho\) change sign and the phase and
coefficient product are conjugated.  The gate is invariant.  Hence
\(\mathscr W=\Re\mathscr F\),

\[
 \tau_h\tau_k\mathscr W=\mathscr W,
 \qquad
 \mathcal R_B^{\rm osc}=\sum\mathscr W.
\tag{3.12c}
\]

For \(\epsilon,\eta\in\{+1,-1\}\), form the exact parity projections

\[
 \mathscr W_{\epsilon\eta}
 ={1\over4}(1+\epsilon\tau_h)(1+\eta\tau_k)\mathscr W.
\tag{3.12d}
\]

Equation (3.12c) gives

\[
 \mathscr W_{+-}=\mathscr W_{-+}=0,\qquad
 \mathscr W=\mathscr W_{++}+\mathscr W_{--}.
\tag{3.12e}
\]

Thus the endpoint symmetry improves the complement ledger: there are not
three generic parity complements.  The double antisymmetrization

\[
 (1-\tau_h)(1-\tau_k)\mathscr W=4\mathscr W_{--}
\]

can capture only the \((--)\) piece, while the sole surviving complement is

\[
 \boxed{\mathscr W_{++}
 ={1\over4}(1+\tau_h)(1+\tau_k)\mathscr W.}
\tag{3.12f}
\]

This \((++)\) component is symmetric, not automatically zero or positive.
After the paid axes and constant-width \(y-x\) slice are removed, its
coefficient-blind capacity is still \(L^4X^\varepsilon\).  The exact-real
symmetry supplies no bound for it, and fixed-\(Q\) ruling families remain
eligible inside it.  Therefore an endpoint-swap commutator identity also
fails at the complement gate: the obstruction is specifically the
surviving \((++)\) component, not three unexamined parity sectors.

### 3.4 Exact one- and two-direction summation by parts

For every finitely supported sequence (G(s)),

\[
 \sum_s(-1)^sD_sG(s)=-2\sum_s(-1)^sG(s).
\tag{3.13}
\]

Applying this to (2.9) gives the exact bounded-primitive character identity

\[
 \mathcal R_B^{\rm osc}
 =-{1\over2}\sum_{h,k,s,q}(-1)^sD_sF_{h,k}(s,q).
\tag{3.14}
\]

There is no analogous bounded primitive for the constant (q)-weight.
For every finitely supported (G(q)) and every constant (q_0),

\[
 \sum_qG(q)=-\sum_q(q-q_0)D_qG(q).
\tag{3.15}
\]

Combining (3.14)--(3.15), and using (D_sD_q=D_qD_s), proves the exact
two-direction identity (1.3).

The multiplier in (3.15) is forced.  More generally, suppose

\[
 \sum_{q\in I}G(q)=\sum_{q\in I}w(q)D_qG(q)+\text{endpoint terms}
\tag{3.16}
\]

holds for all (G) supported in the interior of an integer interval (I).
Testing one-point sequences gives the adjoint equation

\[
 w(q-1)-w(q)=1.
\tag{3.17}
\]

Hence (w) is affine of slope (-1) in the interior.  If
(|I|\asymp L), then

\[
 \inf_c\max_{q\in I}|w(q)+c|\ge { |I|-1\over2}\gg L.
\tag{3.18}
\]

Balanced literal (k')-supports have (q)-length (\asymp K\asymp L)
on interior fibres; each far gate deletes only bounded-width intervals in
(q), since its slope is (h) or (h'=h+2s\asymp L).  The fixed-(Q)
rulings are not removed by these gates.  Thus (3.18) cannot be avoided by
recentring (q_0).  Splitting into shorter intervals simply moves the same
variation into new endpoint terms.

### 3.5 Exact gate and support-boundary expansion

To display every correction, write

\[
 J_{s,q}=1_{A_B(h+2s,k+q)\ne0},\quad
 H^\Delta_{s,q}=1_{|\Delta_{s,q}|>L},\quad
 H^\rho_{s,q}=1_{|\rho_{s,q}|>L},\quad
 I=JH^\Delta H^\rho,
\tag{3.19}
\]

and

\[
 Y_{s,q}=C_{h,k}(s,q)[e(\theta_{s,q})-1].
\]

At the four corners let (I_{ij}=I(s+i,q+j)), (Y_{ij}=Y(s+i,q+j)).
The exact four-corner product rule is

\[
\begin{aligned}
 D_sD_q(IY)=\;&I_{11}D_sD_qY
 +(I_{11}-I_{01})D_qY
 +(I_{11}-I_{10})D_sY\\
 &+(I_{11}-I_{10}-I_{01}+I_{00})Y_{00}.
\end{aligned}
\tag{3.20}
\]

The first term is the common interior.  The next two are the two oriented
edge corrections, and the last is the corner correction.  There is no
suppressed boundary convention in (3.20).

Each oriented indicator difference has the exact three-source expansion

\[
\begin{aligned}
 I_+-I_0={}&(J_+-J_0)H^\Delta_+H^\rho_+\\
 &+J_0(H^\Delta_+-H^\Delta_0)H^\rho_+\\
 &+J_0H^\Delta_0(H^\rho_+-H^\rho_0).
\end{aligned}
\tag{3.21}
\]

Applying (3.21) on each edge of the corner difference in (3.20) expands
all support, radial-gate, and determinant-gate corrections exactly once.
The relevant increments are

\[
\begin{array}{c|cc|c}
\text{edge}&\Delta_+-\Delta_0&\rho_+-\rho_0&\text{primed atom}\\
\hline
s\to s+1&2(k+q)&-2k&(h',k')\to(h'+2,k')\\
q\to q+1&h+2s&h&(h',k')\to(h',k'+1)\\
s\to s+1\text{ at }q+1&2(k+q+1)&-2k&(h',k'+1)\to(h'+2,k'+1)\\
q\to q+1\text{ at }s+1&h+2s+2&h&(h'+2,k')\to(h'+2,k'+1)\\
\end{array}
\tag{3.22}
\]

A sharp-gate difference in (3.21) forces one endpoint of its edge into
(|\Delta|\le L) or (|\rho|\le L).  After a unit reindexing, the accepted
corridor estimates therefore bound all unweighted gate-edge and gate-corner
masses by (O_\varepsilon(L^3X^\varepsilon)).  Here \(J\) records only the
geometric/profile zero extension; the low-gcd weight remains inside \(C\)
and is not incorrectly treated as interval support.  The literal profile
support has (O(1)) interval endpoints on each coordinate line, so its
one-step zero-extension edges have (O(L^3)) atoms.  Floors, clips, stars,
crossings, and equality conventions stay at their original corner and do
not increase this count.  Thus the geometric/gate boundary created by the
one-direction identity (3.14) is target-safe; arithmetic gcd changes remain
in the bulk coefficient terms.

The second identity (1.3), however, multiplies every term in (3.20) by
(|q-q_0|).  The exact owner ledger then becomes

\[
 O_\varepsilon(L^3X^\varepsilon)\times O(L)
 =O_\varepsilon(L^4X^\varepsilon),
\tag{3.23}
\]

unless a new signed boundary theorem is proved before taking a modulus.
The same issue occurs if the already paid (p=0) sector is removed before
differencing: the new (s=-1,0) edge carries a (q)-multiplier and has
coefficient-blind (L^4) capacity.  Keeping the axes inside (1.3) is exact,
but supplies no division or saving.  This is the first target-safe-complement
failure of the nonzero two-direction SBP fallback.

### 3.6 Bulk phase and literal-coefficient ledger

Even if all boundary terms in (3.23) were supplied by a new theorem, the
common interior does not have a coefficientwise (L^{-1}).  Put

\[
 Z_{s,q}=e(\theta_{s,q})-1.
\]

The exact product rule is

\[
\begin{aligned}
 D_sD_q(CZ)=\;&C_{11}D_sD_qZ
 +(C_{11}-C_{01})D_qZ\\
 &+(C_{11}-C_{10})D_sZ
 +(D_sD_qC)Z_{00}.
\end{aligned}
\tag{3.24}
\]

The first term retains the complete undifferenced coefficient at one
corner, including both gcd weights and both slanted symbols.  Moreover

\[
 D_sD_qZ=e(\theta_{11})-e(\theta_{10})
 -e(\theta_{01})+e(\theta_{00});
\tag{3.25}
\]

the constant (-1) cancels whenever a difference lands on \(Z\).  It remains
inside the last term \((D_sD_qC)Z_{00}\), where both differences land on
the coefficient, and inside the indicator boundary terms (3.20).  Thus the
proved phase-free subtraction is not being silently reused as a deletion of
these corrections.

Writing (h'=h+2s), (k'=k+q), the exact phase increments are

\[
\begin{aligned}
 \theta_{10}-\theta_{00}
 &=-R\{\sqrt{(h'+2)k'}-\sqrt{h'k'}\},\\
 \theta_{01}-\theta_{00}
 &=-R\{\sqrt{h'(k'+1)}-\sqrt{h'k'}\},\\
 D_sD_q\theta
 &=-R\{\sqrt{(h'+2)(k'+1)}-\sqrt{(h'+2)k'}\\
 &\hspace{32mm}-\sqrt{h'(k'+1)}+\sqrt{h'k'}\}.
\end{aligned}
\tag{3.26}
\]

On the balanced support the first two real phase increments have scale
(R\asymp L^3), while the mixed real increment has scale (R/L\asymp L^2).
These large real derivatives imply no smallness modulo one.  Consistently
with the accepted hostile control, the bracket and (3.25) can have order-one
size; there is no uniform (O(L^{-1})) coefficientwise bound.

The coefficient differences in the other three terms do not repair this.
The smooth profile part has ordinary scaled variation, but the literal
second gcd factor

\[
 \eta\!\left({(h+2s,k+q)\over G_0}\right)
\]

is arithmetic under the unit shifts, and its discrete difference is not
uniformly (O(L^{-1})).  Opening it into divisors changes the divisor and
progression sets at the four corners and is precisely the already parked
aliaswise/divisorwise route.

The restored power ledger is therefore

\[
\begin{array}{c|c|c}
\text{object}&\text{certified positive capacity}&\text{target}\\
\hline
\text{original complete double-far pairs}&L^4X^\varepsilon&L^3X^\varepsilon\\
p=0\text{ and }q=0\text{ axes}&L^3X^\varepsilon&L^3X^\varepsilon\\
\text{fixed-width }|y-x|\text{ strip}&L^3X^\varepsilon&L^3X^\varepsilon\\
\text{actual-real }(++)\text{ complement}&L^4X^\varepsilon&L^3X^\varepsilon\\
\text{one-step gate/support boundaries}&L^3X^\varepsilon&L^3X^\varepsilon\\
\text{one-direction character difference bulk}&L^4X^\varepsilon&L^3X^\varepsilon\\
\text{two-direction boundary after forced primitive}&L^4X^\varepsilon&L^3X^\varepsilon\\
\text{two-direction bulk after triangle}&L^5X^\varepsilon&L^3X^\varepsilon\\
\end{array}
\tag{3.27}
\]

The last line is not asserted as physical mass or a lower bound.  It is the
operator's exact coefficient-blind capacity: (O(L^4)) four-tuples, an
(O(L)) forced primitive, and an (O(1)) four-corner phase difference.
Thus neither (3.14) nor (1.3) licenses a positive norm after saving the
required factor (L).

### 3.7 Literal restoration and fixed-(Q) ledger

The derivation was performed before opening any literal structure.  Its
restoration ledger is:

| Literal datum | Exact location in the derivation | Outcome |
|---|---|---|
| both characters | (3.2), leaving exactly ((-1)^s) | constant on fixed (p); only one bounded primitive |
| both low-gcd weights | the two factors in (C_{h,k}(s,q)) | retained at every corner of (3.24); their arithmetic differences give no smooth gain |
| both slanted symbols and Vaaler taper | (A_B(h,k)\overline{A_B(h+2s,k+q)}) | retained with the actual clipped profiles |
| floors, stars, crossings, and endpoints | fixed labels in (A_B), zero extension (J), and the four corners of (3.20) | never rounded, smoothed, or identified across corners |
| strict far gates | (H^\Delta,H^\rho) and (3.21)--(3.22) | every edge and corner correction exposed |
| axial sectors | (3.3)--(3.4) | retained and paid absolutely |
| phase-free subtraction | (Z=e(\theta)-1) | the constant cancels only where a difference lands on \(Z\); coefficient and boundary terms remain |
| actual-real endpoint swaps | \(\tau_h\tau_k\mathscr W=\mathscr W\), (3.12a)--(3.12f) | cross parities vanish; the \((++)\) complement is retained |
| aliases and lifts | not opened before the identity | opening them gives different divisor/progression sets at the four corners; no aliaswise modulus is taken |
| fixed-(Q) rulings | subsets of the unchanged literal/alias bulk | neither (3.9) nor the subtraction removes them |
| arbitrary real centre | (R=\sqrt X) in every phase in (3.26) | never replaced by (y=\lfloor\sqrt X\rfloor) |
| block owner and outer modulus | one fixed (B), one joint scalar | no shellwise, shiftwise, divisorwise, residuewise, or aliaswise triangle is used to claim the target |

If the accepted second-gcd alias chart is opened after (3.24), every
(d\mid h',k'), half-integer (\mu), (J)-condition, lift multiplier,
(\gamma_d), and restored carrier remains corner-dependent.  The Round-136
equal-rational lifts remain carrier-coherent and the fixed-(Q) relations
remain allowed by both far gates.  The coordinate translations do not
create a weight-preserving bijection among these corner-dependent lift sets.
Hence the proposed identity neither exploits nor deletes the known rulings.

## 4. First doubtful or unproved step

The coordinate inverse, multiplicity ledger, character formula, and axial
estimates are proved.  The first failed mechanism gate is the requested
**nontrivial exact two-defect commutator with a pre-norm factor-(L) gain**.

The side-sum-normalized defect commutators are exactly (T_s) and (T_q),
so their commutator is zero.  Their unnormalized commutator has a large
coefficient and, wherever it can be divided, reduces to a tautological
shift.  The parity-compatible diagonal version has the exact multiplier
\(8(y-x)\): its singular fixed-width strip is paid at \(L^3\), while on
the complement division cancels that multiplier and returns the original
alternating diagonal difference.  Exact-real endpoint symmetry kills the
two cross parity projections but leaves the \((++)\) complement at
\(L^4\) capacity.  The only universal nonzero two-direction SBP fallback
is (1.3), whose second primitive is necessarily
of size (L).  Its exact sharp-gate/support complement has only an (L^4)
ledger after restoration, and its interior contains the full undifferenced
phase term (3.25).  Therefore the required (L^{-1}) is absent before any
positive norm.

What remains unproved is the original signed estimate.  It is logically
possible that the complete actual gcd/slanted/alias sum has a new joint
(q)-cancellation theorem.  Such a theorem would be new analytic input,
not a consequence of (3.1), (1.1), or discrete integration by parts.  No
claim is made that the (L^4) or (L^5) capacities are lower bounds for
the physical remainder.

By the Round-171 stop rule, the task stops here.  It does not pivot to a
different BAL label, fixed-defect counting, broad--narrow, another
B-process, K26, TOP, UNBAL, M1, GAR, or endpoint assembly.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `literal_critical_j1_scope` | **Pass.** Only persistent (j=1), (L\asymp X^{1/6}), one fixed literal block is used. |
| `coordinate_bijection_and_multiplicity` | **Pass.** Equations (2.5)--(2.7) give the exact inverse and ordered multiplicity one. |
| `Delta_rho_factorizations` | **Pass.** Equation (3.1) is coefficientwise; it is not mislabelled as an estimate. |
| `two_discrete_difference_identity` | **No-go.** The normalized defect commutator is identically zero.  The exact nonzero SBP fallback (1.3) has a forced length-(L) primitive. |
| unnormalized diagonal commutator | **Pass as an exact no-go seam.** It is \(8(y-x)T_sT_q^2\).  The fixed-width singular strip is \(O(L^3X^\varepsilon)\); complement division cancels the multiplier and recovers only the alternating diagonal difference. |
| actual-real endpoint-swap parity | **Pass.** \(\tau_h\tau_k\mathscr W=\mathscr W\); the \(+-\) and \(-+\) projections vanish.  The surviving \((++)\) complement retains \(L^4\) capacity. |
| `fixed_p_character_constancy` | **Pass.** Equation (3.2) is constant on every fixed-(p) fibre; no inner-(h) saving is claimed. |
| `p0_q0_axial_sectors` | **Pass.** Both sectors can be double-far and are paid by (3.3)--(3.4). |
| `sharp_far_gate_and_support_boundaries` | **Exact expansion pass; target-safe-complement fail for the two-step route.** Equations (3.20)--(3.23) expose every edge and corner; the forced (q)-primitive amplifies their ledger to (L^4). |
| `phase_free_subtraction_scope` | **Pass.** Only (e(\theta)-1) is used.  The (-1) survives indicator/coefficient boundary differences. |
| `fixed_Q_rulings` | **Pass as hostile control.** They remain in the bulk; neither strict gate nor the commutator deletes them. |
| `gcd_slanted_symbol_and_alias_restoration` | **Pass as an exact ledger; no gain.** Every literal factor stays at all four corners, and distinct lift sets are not merged. |
| `endpoint_and_real_centre_restoration` | **Pass.** Zero extension, floors, stars, crossings, strict inequalities, and (R=\sqrt X) are retained. |
| `positive_capacity_factor_L` | **Fail for this route.** The one-direction bulk remains at (L^4); the two-direction positive ledger is no better and can be (L^5). |
| `target_safe_complement` | **Fail for this route.** The endpoint-swap \((++)\) complement already retains \(L^4\) capacity, and the second Abel primitive turns the supplied (L^3) boundary owner into an (L^4) ledger. |
| `no_positive_norm_before_saving` | **Pass as a stop control.** No positive norm is used to assert the target; the task stops when the pre-norm saving is absent. |
| `owner_quantifier_quarantine` | **Pass.** No noncritical (j=1), exact-square (j=2), or other balanced label is touched. |
| `no_in_round_pivot` | **Pass.** No alternative owner is attacked. |
| `no_status_or_exponent_overpromotion` | **Pass.** No BAL parent, M9--M2, M9, bridge, quarter theorem, or exponent is claimed. |
| constant-character false control | **Pass.** Replacing ((-1)^s) by (1) destroys the bounded-primitive identity (3.13); the defect commutator alone still gives zero. |
| erased-structure false control | **Pass.** The coordinate/SBP identities remain universal, but the estimate fails at capacity, so no false coefficient-uniform theorem is produced. |
| phase-adapted-coefficient false control | **Pass.** The undifferenced order-one phase term and (L^4/L^5) ledgers leave the adversarial capacity intact. |

No numerical computation, symbolic experiment, or external theorem was
used.

## 6. Dependencies and exact artifacts used

This report read and used exactly the permitted packet:

1. `protocol.md`;
2. `state/proof_obligations.yml`, including the literal dictionary,
   corridor, phase-free, oscillatory-remainder, alias, ruling, remaining-label,
   BAL-parent, M9--M2, M9, and target entries at the stated graph;
3. `state/active_campaign.yml`;
4. `strategy/round171_m2_balanced_critical_j1_two_defect_commutator_strategy.md`;
5. `rounds/codex-managed/m9-m2-balanced-critical-j1-two-defect-commutator-gate/barrier_packet.md`;
6. `rounds/codex-managed/full-proof-round167-169-strategy-literature-review/synthesis.md`;
7. `rounds/codex-managed/full-proof-round167-169-strategy-literature-review/reports/full_graph_frontier_reconstruction.md`;
8. `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/synthesis.md`;
9. `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/reviews/conductor_round114_energy_and_corridors.md`;
10. `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/synthesis.md`;
11. `rounds/codex-managed/m9-m2-balanced-double-far-shifted-divisor-fork/reviews/conductor_round115_identity_and_zero_mode.md`;
12. `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/synthesis.md`;
13. `rounds/codex-managed/m9-m2-balanced-joint-cluster-defect-broad-narrow-gate/reviews/conductor_round136_broad_narrow_adjudication.md`; and
14. the complete task brief
   `rounds/codex-managed/m9-m2-balanced-critical-j1-two-defect-commutator-gate/briefs/literal_two_defect_commutator_attack.md`.

The accepted inputs used quantitatively are the literal balanced atom
dictionary, (K\asymp L), the (L^4) positive capacity, the two (L^3)
corridor bounds, the (L^3) phase-free theorem, and the exact character and
fixed-(Q) ruling identities.  No sibling Round-171 report, unpermitted
artifact, web source, computation, or unaccepted theorem enters the proof.

## 7. Recommended state effect

**Recommended effect: retain the target open and record a scoped
`balanced_two_defect_commutator_no_go`; no proof-state promotion.**

The conductor may retain (2.5)--(2.7), (3.3)--(3.4), the operator
identities (1.1)--(1.3), the diagonal audit (3.11a)--(3.11d), and the
endpoint-swap audit (3.12a)--(3.12f) as candidate evidence.  The axial estimate is a
target-safe strict sub-sector, but it does not reduce the positive capacity
of the nonaxial bulk.  The exact no-go should be scoped to:

1. the canonical parity-preserving (p)-translation and unit
   (q)-translation;
2. commutators with multiplication by
   (\Delta+\rho) and (\Delta-\rho), normalized by the positive side
   sums;
3. the parity-compatible unnormalized diagonal commutator, including the
   \(y=x\) strip and complement;
4. endpoint-swap double antisymmetrization, whose exact-real complement is
   \((++)\); and
5. coefficient-independent local two-step Abel summation before a positive
   norm.

Do not interpret it as a lower bound, a disproof of
`M9-M2-balanced-double-far-oscillatory-remainder`, or a no-go for every
possible actual-symbol identity.  That obligation and the equivalent
critical actual energy remain open.  The separate remaining-label owner,
full BAL, hard TOP, UNBAL, M9--M2, both direct M1 parents or GAR, endpoint
assembly, M9, both bridges, and the Gauss-circle quarter target all remain
open.  The internal exponent and every external benchmark remain unchanged.
