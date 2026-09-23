# Hard-M1 \(t=1\) rho-large Farey-covector reduction

- Campaign: m9-m1-t1-rho-large-bezout-edge-gate
- Round: 192
- Starting graph SHA-256:
  75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13
- Formal candidate SHA-256:
  9562954b65ac8c0f465b535e39d1c30724339098ef5a0d520507cd0983996cd5
- Numerical theorem evidence: none

## Kernel statement

Retain the exact accepted Round-191 hard-M1 \(t=1\) rho-large remainder.
Thus

\[
 Q=H_B,\quad U=mq>4Q,\quad q>Q,\quad m|a|_q>Q,\quad Qm<Y,
\quad U\mid u,
\tag{192.K1}
\]

\[
 j_q(a,v)=|a\bar v_q|_q>
 \min\!\left\{\frac{q-1}{2},
      \left\lfloor\frac{Qmq}{Y}\right\rfloor\right\},
\quad
 J\le j_q(a,v)<2J,
\tag{192.K2}
\]

on one nonempty power-of-two fast band. The Round-191 inverse-small,
live-side terminal, and isolated Fejer projections have already been
removed. Both orientations and every literal field remain inside one
complex aggregate before the final real part.

For \(v_0=[v]_U\in\{1,\ldots,U-1\}\), define

\[
 \rho v_0-\beta U=1,\qquad
 -\frac{U-1}{2}\le\rho\le\frac{U-1}{2},
\tag{192.K3}
\]

\[
 T=\min\!\left\{\frac{U-1}{2},
      \left\lfloor\frac{QmU}{Y}\right\rfloor\right\}.
\tag{192.K4}
\]

Only \(|\rho|>T\) remains. Fix \(C_0\ge2\) independently of all asymptotic
variables, and set

\[
 A=\min\{U-1,\lfloor Q^{C_0}\rfloor\},
\quad
 \mathcal F_A=
 \{(c,d):1\le c\le A,\ 0\le d\le c,\ (c,d)=1\},
\tag{192.K5}
\]

\[
 \ell_{c,d}=c\beta-d\rho.
\tag{192.K6}
\]

For \(T\ge1\), define the single union

\[
 \mathcal E_A=
 \{v:\exists(c,d)\in\mathcal F_A,\,
       |\ell_{c,d}(v)|\le T\};
\tag{192.K7}
\]

for \(T=0\), define \(\mathcal E_A=\varnothing\). Let \(P_A\) multiply every
atom of the exact Round-191 fixed remainder by
\(\mathbf1_{\mathcal E_A}(v)\). Then

\[
 \boxed{
 |P_A\mathscr R_{\rm fix}|
 \ll_{B,C_0,\varepsilon}Qm\kappa uX^\varepsilon.}
\tag{192.K8}
\]

After the exact lift, coefficient mass, bands, divisor ledger, and shell sum,

\[
 \boxed{
 |\mathcal O_{Y,Q}^{\sigma}
  (\{P_A\mathscr R_{\rm fix}\})|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon.}
\tag{192.K9}
\]

The exact new decomposition is

\[
 \mathscr J_{\rm safe,192,fix}
 =\mathscr J_{\rm safe,191,fix}+P_A\mathscr R_{\rm fix},
\qquad
 \mathscr R_{\rm core,fix}=(I-P_A)\mathscr R_{\rm fix}.
\tag{192.K10}
\]

Linearity gives the identically typed outer decomposition. For \(T\ge1\),
every core row satisfies

\[
 |c\beta-d\rho|>T\quad((c,d)\in\mathcal F_A),
\qquad
 |\rho|\ge(A+1)(T+1).
\tag{192.K11}
\]

The core is guaranteed empty if

\[
 \boxed{
 T\ge1,\qquad
 \left\lfloor
 \frac{(U-1)/2}{A+1}
 \right\rfloor\le T,}
\tag{192.K12}
\]

equivalently \(U\le2(A+1)(T+1)-1\).

Outside (192.K12), the core estimate

\[
 \Re\mathscr R_{\rm core,Y,Q}^{\sigma}
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon
\tag{192.K13}
\]

remains open. Positive fixed-packet control has scale
\(Y\kappa uX^\varepsilon\), versus target
\(Qm\kappa uX^\varepsilon\), leaving \(Y/(Qm)\).

## 1. Canonical quotient and factorization

Equation (192.K3) implies

\[
 (\rho,\beta)=1,\qquad
 0\le\frac{\beta}{\rho}\le1.
\tag{192.K14}
\]

For the literal representative \(v=v_0+nU\), define
\(\rho v-\gamma U=1\). Then

\[
 \boxed{\gamma=\beta+n\rho.}
\tag{192.K15}
\]

Thus the Farey selector uses canonical \(\beta\), while literal transport
uses \(\gamma\).

For \(1\le c<U\),

\[
 \boxed{
 \rho(cv_0-dU)=c+U(c\beta-d\rho)
              =c+U\ell_{c,d}.}
\tag{192.K16}
\]

The right side is nonzero because it is congruent to
\(c\not\equiv0\pmod U\).

## 2. Divisor and literal multiplicities

Fix \((c,d,\ell)\) and put \(N=c+U\ell\ne0\). Every admissible \(\rho\) is
a signed divisor of \(N\), and a signed least inverse determines at most one
canonical unit class. Hence

\[
 \#\{v_0\bmod U:\ell_{c,d}(v_0)=\ell\}
 \le2\tau(|c+U\ell|).
\tag{192.K17}
\]

For \(|\ell|\le T\),

\[
 0<|c+U\ell|<U^2\ll X^{1/2},
\tag{192.K18}
\]

because \(T\le(U-1)/2\), \(c<U\), and the inherited shell connector gives
\(U\le u\ll L\ll X^{1/4}\). For \(T\ge1\),

\[
 \#\{v_0\bmod U:|\ell_{c,d}|\le T\}
 \ll_\eta TX^\eta.
\tag{192.K19}
\]

The family has

\[
 |\mathcal F_A|
 =2+\sum_{2\le c\le A}\varphi(c)
 \ll A^2\le Q^{2C_0}.
\tag{192.K20}
\]

The union indicator counts each row once; the covector sum is used only as
an upper bound. The literal support is a fixed finite interval union of total
length \(O(u)\). Since \(U\mid u\), every residue occurs
\(O(u/U+1)=O(u/U)\) times. Projective bands and literal masks only delete
rows. Therefore

\[
 \#\{v\ {\rm literal}:v\in\mathcal E_A\}
 \ll_\eta A^2\frac{uT}{U}X^\eta
 \ll_\eta A^2\frac{Qmu}{Y}X^\eta.
\tag{192.K21}
\]

The \(T=0\) sector is empty; no isolated zero-covector class is charged to a
sub-one-class density budget.

## 3. Fixed and outer estimates

At fixed parameters,

\[
 \mathscr R_{\rm fix}
 =\mathscr J_{\rm fix}
  -\mathscr J_{\rm inv,fix}
  -\mathscr J_{\rm terminal,fix}
  -\mathscr J_{\rm Fejer,fix}.
\tag{192.K22}
\]

Because \(P_A\) is supported on \(|\rho|>T\),
\(P_A\mathscr J_{\rm inv,fix}=0\). Restricting (192.K22), endpoint-exact
Abel inversion returns \(P_A\mathscr J_{\rm fix}\) to the original row sum
before positive counting. Every selected row has \(O(Y)\) heights,
\(O(\kappa)\) sites, and \(O_\eta(X^\eta)\) literal weight. Thus

\[
 |P_A\mathscr J_{\rm fix}|
 \ll_\eta A^2Qm\kappa uX^{2\eta}.
\tag{192.K23}
\]

Row deletion preserves the accepted positive terminal and Fejer bounds.
Their restricted contribution is \(O_\eta(\kappa uX^\eta)\).
Absorbing the fixed polylogarithm \(A^2\) into a fresh epsilon budget proves
(192.K8). Algebra gives

\[
 \mathscr J_{\rm safe,192,fix}
 =\mathscr J_{\rm inv,fix}
 +(I-P_A)\mathscr J_{\rm terminal,fix}
 +(I-P_A)\mathscr J_{\rm Fejer,fix}
 +P_A\mathscr J_{\rm fix},
\tag{192.K24}
\]

so old terminal and Fejer rows are replaced, not doubled.

The inherited identities

\[
 c_{mq}(ma)=m^{-1}c_q(a),\qquad
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q),\qquad
 \sum_{mq\mid u}1\le\tau_3(u)
\tag{192.K25}
\]

give

\[
 Q^{2C_0+1}X^{2\eta}
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u)
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon.
\tag{192.K26}
\]

The \(m^{-1}\) cancels \(m\) before the positive outer sum. No positive
power of \(Y\), \(U\), or \(L\) is hidden in the epsilon budget.

## 4. Circular-pigeonhole coverage

Put \(r=|\rho|\), \(b=|\beta|\). Then
\(0\le b\le r\), \((b,r)=1\), and

\[
 |c\beta-d\rho|=|cb-dr|.
\tag{192.K27}
\]

Place \(0,b,\ldots,Ab\pmod r\) on the circle of circumference \(r\). If
\(A\ge r\), two points coincide. If \(A<r\), the \(A+1\) distinct gaps sum
to \(r\), so one has integral length at most
\(\lfloor r/(A+1)\rfloor\). Its index difference gives
\(1\le c\le A\), \(0\le d\le c\), and

\[
 |cb-dr|\le\left\lfloor\frac r{A+1}\right\rfloor.
\tag{192.K28}
\]

Gcd reduction preserves the family constraints and only decreases the
determinant. Hence

\[
 \min_{(c,d)\in\mathcal F_A}|c\beta-d\rho|
 \le\left\lfloor\frac{|\rho|}{A+1}\right\rfloor.
\tag{192.K29}
\]

A \(T\ge1\) core row has integral minimum at least \(T+1\), proving
(192.K11)--(192.K12). If \(|\rho|\le A\), the primitive covector
\((|\rho|,|\beta|)\) has \(\ell=0\). These are coverage statements only.

## 5. Literal phase, carry, and endpoint identities

For \(v=v_0+nU\), set

\[
 d_v=cn+d,\qquad
 \Delta=cv-d_vU=cv_0-dU.
\tag{192.K30}
\]

Then

\[
 \rho\Delta=c+U\ell,\qquad
 \gamma\Delta=d_v+v\ell,
\tag{192.K31}
\]

and, for
\(z_{\omega,v}=e(\epsilon_\omega a\rho/q)\),

\[
 z_{\omega,v}^{\Delta}
 =e(\epsilon_\omega ac/q).
\tag{192.K32}
\]

For a finite or absolutely summable height sequence extended by zero to all
integer heights,

\[
 \frac1{1-z^\Delta}
 \sum_h\{W(h)-W(h-\Delta)\}z^h
 =\sum_hW(h)z^h
\tag{192.K33}
\]

when \(z^\Delta\ne1\). This is an exact self-return, not a saving.

Let \(S_{0,\omega}(h)\in[0,U)\) be the unique canonical anchor with
\(S_{0,\omega}(h)\equiv\epsilon_\omega\rho h\pmod U\). Put

\[
 N_\omega(h;\Delta)=
 \frac{S_{0,\omega}(h+\Delta)-S_{0,\omega}(h)
       -\epsilon_\omega\rho\Delta}{U}.
\tag{192.K34}
\]

Then

\[
 N_\omega(h;\Delta)
 =\theta_{\omega,c}(h)-\epsilon_\omega\ell,
\tag{192.K35}
\]

\[
 \theta_{\omega,c}(h)=
 \frac{S_{0,\omega}(h+\Delta)-S_{0,\omega}(h)
       -\epsilon_\omega c}{U},
\quad
 \theta_{+,c}\in\{-1,0\},\quad
 \theta_{-,c}\in\{0,1\}.
\tag{192.K36}
\]

The inherited affine parity is \((-1)^{N_\omega}\); the accumulated factor is

\[
 (-1)^{N_\omega(h;\Delta)}e(\epsilon_\omega ac/q).
\tag{192.K37}
\]

It has no lower separation from one supplied by the core.

With \(A_0=\kappa gU\), \(C_v=\kappa v\), the endpoint number/divisor
translations are

\[
\begin{array}{c|cc}
 &\Delta N_{i,+}&\Delta d_{i,+}\\ \hline
i=0&2A_0(d_v+v\ell)&0\\
i=1&2gC_v(c+U\ell)&2g(c+U\ell)
\end{array},
\tag{192.K38}
\]

\[
\begin{array}{c|cc}
 &\Delta N_{i,-}&\Delta d_{i,-}\\ \hline
i=0&-2gC_v(c+U\ell)&-2g(c+U\ell)\\
i=1&-2A_0(d_v+v\ell)&0
\end{array}.
\tag{192.K39}
\]

They need not coincide and contain the representative-dependent \(d_v\).
The full endpoint arithmetic masks, literal cells, square-root phases,
births, deaths, and coprimality fields are therefore not transport invariant.

## 6. Exact core and method boundary

For \(T\ge1\), the exact core is the simultaneous strict-covector set
(192.K11); for \(T=0\), it is the entire inherited rho-large remainder.
Every Round-191 literal field remains in one complex subtraction.

In an unsaturated prime-modulus residue-universe control with
\(1\le T<(U-1)/2\), suppose the inherited fast predicates leave
\(\asymp U\) central unit classes. A fixed covector meets only
\(O_\eta(TX^\eta)\) classes. Hence coefficient-blind coverage needs

\[
 M\gg_\eta\frac{U}{TX^\eta}
 \asymp\frac{Y}{Qm}X^{-\eta}.
\tag{192.K40}
\]

Positive recombination restores the original deficit. Literal masks may
delete these ambient rows, so (192.K40) is not literal lower mass.

For arbitrary bounded zero-extended height arrays, endpoint-exact Abel
summation has full support capacity after any static Farey selector.
This rules out support-only, bounded-array, positive-completion, and
separable-norm closures. It neither realizes the fixed literal coefficients
nor disproves (192.K13).

The first missing theorem is a jointly signed correlation estimate for the
actual unequal endpoint translations, masks, carries, square-root phases,
and affine births/deaths before any positive norm.

## 7. Dependencies and proof-state boundary

Direct dependencies:

- M9-M1-hard-top-t1-fast-signed-inverse-transport-reduction;
- Divisor-bound-elementary.

The exact lift, projective-band, terminal, Fejer, shell, and endpoint
connectors are inherited through the accepted Round-191 dependency chain.

This kernel proves only the strict Farey union, exact core, coverage
corollaries, and scoped method boundary. The complete rho-large remainder,
complete original \(t=1\), every original \(t\ge2\) range, the remaining
small-\(t\) owner, hard and smooth M1, GAR, all M2 parents, endpoint
uniformity, M9, both bridges, the quarter target, and every exponent remain
open, conditional, or unchanged.
