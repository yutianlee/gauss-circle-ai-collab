# Round 192 strategy: rho-large Farey-covector sparsity

## Frozen inherited packet

Work only inside the accepted Round-191 remainder. Put

\[
Q=H_B,\qquad U=mq>4Q,\qquad q>Q,\qquad Qm<Y,
\]

retain the exact Round-189 fast condition in the projective variable, and
retain

\[
|\varrho_U(v)|>T,\qquad
T=\min\!\left(\frac{U-1}{2},
\left\lfloor\frac{QmU}{Y}\right\rfloor\right).
\]

The outer terminal and isolated Fejer projections have already been removed.
The remaining packet is still one complex aggregate containing all literal
arithmetic, affine, endpoint, carry, cell, crossing, phase, orientation, and
zero-extension fields before the final real part.

## New arithmetic coordinates

For an actual literal row \(v\), let \(v_0=[v]_U\in\{1,\ldots,U-1\}\).
Define the signed least inverse \(\varrho=\varrho_U(v)\) and the canonical
residue quotient \(\beta=\beta_U(v)\) by

\[
\varrho v_0-\beta U=1,
\qquad |\varrho|\le\frac{U-1}{2}.
\tag{192.S1}
\]

This \(\beta\) is a residue-class coordinate. It is not the actual transport
quotient \(\gamma_U(v)=(\varrho v-1)/U\) when the literal representative
\(v\) is outside \((0,U)\).

For coprime integers \(1\le c<U\), \(0\le d\le c\), define the unimodular
covector

\[
\ell_{c,d}(v)=c\beta-d\varrho.
\tag{192.S2}
\]

Multiplying (192.S1) by \(c\) gives the exact factorization

\[
\boxed{\varrho(cv_0-dU)=c+U\ell_{c,d}(v).}
\tag{192.S3}
\]

Because \(c<U\), the right side never vanishes. For a fixed
\((c,d,\ell)\), every admissible residue class produces an integer factor
pair of \(|c+U\ell|\). Hence the number of residue classes is at most a
constant multiple of \(\tau(|c+U\ell|)\).

## Proposed strict sector

Fix a conductor exponent \(C_0\ge2\) once and for all and set

\[
A_Q(U)=\min\{U-1,\lfloor Q^{C_0}\rfloor\},
\]

\[
\mathcal F_A={(c,d):1\le c\le A_Q(U),\ 0\le d\le c,\ (c,d)=1\}.
\]

When \(T\ge1\), define the Farey-covector sector

\[
\mathcal E_A=\left\{v:\min_{(c,d)\in\mathcal F_A}
|\ell_{c,d}(v)|\le T\right\}.
\tag{192.S4}
\]

When \(T=0\), define \(\mathcal E_A=\varnothing\); this avoids the false
use of the isolated zero-covector classes when the target density is below
one residue class.

For each covector there are \(O(TX^\eta)\) eligible residue classes by
(192.S3) and the elementary divisor bound. Since
\(|\mathcal F_A|\ll A_Q^2\ll Q^{2C_0}\), the union has

\[
\#\{v\text{ literal}:v\in\mathcal E_A\}
\ll X^\eta Q^{2C_0}\frac{uT}{U}
\ll X^\eta Q^{2C_0}\frac{Qmu}{Y}.
\tag{192.S5}
\]

Here the inherited literal interval multiplicity
\(O(u/U+1)=O(u/U)\) uses \(U\mid u\); projective bands and literal masks
only delete rows.

Returning the endpoint-exact Abel packet to the original row sum, the
\(Y\) heights and \(O(\kappa)\) sites give

\[
|\mathscr R_{{\rm Farey},{\rm fix}}|
\ll X^{2\eta}Q^{2C_0}Qm\kappa u.
\tag{192.S6}
\]

With a fresh \(\eta<\varepsilon\), the fixed polylogarithmic factor is
absorbed only into the epsilon budget. The exact
\(m^{-1}c_q(a)\) lift then cancels \(m\), and the accepted coefficient,
band, and divisor ledger should give
\(O_{B,C_0,\varepsilon}(L^2X^\varepsilon)\).

## Exact proposed complement

The new core is the exact complex subtraction of (192.S4) from the
Round-191 remainder. It has \(T=0\), or else satisfies

\[
|c\beta-d\varrho|>T
\quad\text{for every }(c,d)\in\mathcal F_A.
\tag{192.S7}
\]

Thus \(\beta/\varrho\) is quantitatively separated from every Farey rational
of order at most \(A_Q\), at scale \(T/(c|\varrho|)\). This is only an exact
Diophantine description; no phase cancellation is inferred from it.

Two edge covectors are \((1,0)\) and \((1,1)\), giving \(\beta\) and
\(\beta-\varrho\); \((2,1)\) gives the central covector
\(2\beta-\varrho\). If \(|\varrho|\le A_Q\) and \(T\ge1\), the primitive
covector \((|\varrho|,|\beta|)\) has \(\ell=0\), so the Farey core is empty.
Consequently the complete fast remainder is closed on the strict subrange

\[
T\ge1,\qquad U\le 2Q^{C_0},
\tag{192.S8}
\]

after the accepted Round-191 pieces are restored.

## Required hostile questions

1. Does (192.S3) count actual residue classes without conflating \(v_0\),
   the literal representative \(v\), and the transport quotient \(\gamma\)?
2. Are the negative-\(\varrho\), endpoint covectors, \(T=0\), floor, and
   \(A_Q\ge U\) cases exact?
3. Does summing \(O(Q^{2C_0})\) sectors remain power-neutral through the
   lift and outer ledger?
4. Can (192.S7) feed a genuine phase/carry estimate, or do arbitrary bounded
   arrays and literal discontinuities still force a scoped no-go?
5. Does any attempted Farey covering of the entire core merely sum too many
   target-sized sectors and return the original \(Y/(Qm)\) deficit?

## Promotion boundary

The intended maximum promotion is one strict subordinate Farey-covector
reduction and exact core. Do not promote the whole rho-large remainder unless
the literal signed core is actually estimated. Even complete original
\(t=1\) success would leave every \(t\ge2\) small-\(G\) incidence, the
large-\(G\) near-resonant complement, smooth M1, all M2 parents, endpoint
uniformity, M9, both bridges, and the quarter theorem open.
