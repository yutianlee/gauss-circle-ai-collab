# Round 137 synthesis: product-fibre energy is controlled, but the fixed-centre scalar self-returns

Campaign: m9-m2-hard-top-product-fibre-divisor-scalar-gate

Starting graph SHA-256:
3c5003b1478d78b8469d4220ad305bb06ee0f869b9c4a741e7211642eeb52cc7

## Decision

Close under product_fibre_no_go. After the already proved square-entry
sector is removed, the exact hard-TOP scalar is

\[
 \mathcal T_L^{\rm ns}
 =L^{3/2}\sum_{\substack{n\asymp L^2\\n\ne\square}}
 n^{-3/4}C_L(n)e(J\sqrt n),
\]

\[
 C_L(n)=
 \sum_{\substack{h\mid n,\ h\ {\rm odd}\\
 \sqrt n\le h\le2\sqrt n}}
 \chi_4(h)\eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xh^2}{4n}}\right).
\tag{137.S1}
\]

This regrouping is termwise exact, including the ceiling, hard face,
profiles, floors, zero extension, real centre, and nonsquare condition.
It does not average a product fibre.

## Positive structural progress

The literal coefficient has the elementary upper energy envelope

\[
 \boxed{\sum_n|C_L(n)|^2\ll L^2\log(2L).}
\tag{137.S2}
\]

The proof parameterizes every equality \(h_1m_1=h_2m_2\) as

\[
 h_1=ga,\quad h_2=gb,\quad m_1=bt,\quad m_2=at,\quad(a,b)=1,
\]

and sums \(O(M)(L/M+1)^2\) over \(M=\max(a,b)\).
This is an upper bound, not a matching lower mass. Cauchy over the
\(O(L^2)\) product values still gives \(L^{2+o(1)}\), so the target
still lacks \(L^{1/2-o(1)}\).

There is also a sharp radical control. For every squarefree \(D>1\),

\[
 \boxed{
 \sum_{\substack{n\asymp L^2\\\operatorname{sf}(n)=D}}
 \left|L^{3/2}n^{-3/4}C_L(n)1_{n\ne\square}\right|
 \ll_\varepsilon
 \left(1+\frac L{\sqrt D}\right)L^\varepsilon.}
\tag{137.S3}
\]

For \(n=Dt^2\), exact phase one is
\((J\sqrt D)t\in\mathbb Z\). All exact nonsquare phase-one points at
one fixed centre lie in at most one squarefree channel, so their whole
absolute capacity is target-safe by (137.S3). This does not control
near resonances, and summing all radical channels returns
\(L^{2+o(1)}\).

Prime, prime-power, singleton-semiprime, and many-divisor tests show
that the truncated \(\chi_4\)-sum has no automatic fibrewise
cancellation.

## Curvature and exact self-return

For \(f(n)=J\sqrt n\), the coefficient-free derivative range contains
\(\asymp J/L\) integer modes, each of natural stationary size
\(L^{3/2}/\sqrt J\). Their formal absolute capacity is

\[
 \sqrt{JL}=L^{3/2}\frac HL,
\tag{137.S4}
\]

above target on every polynomial intermediate \(L\ll H\). This is
geometric capacity, not actual coefficient mass. The coefficient
\(C_L(n)\) is a discontinuous divisor-incidence sequence; neither
\(|C_L|\le\tau\) nor (137.S2) supplies the bounded variation or
additive partial sums needed for a one-dimensional derivative theorem.

Resolving \(h\mid n\) before Poisson makes the transform legal. The
residue/dual map is bijective, and the stationary calculation gives

\[
 x_{h,r}=\frac{Xh^2}{4r^2},\qquad
 \phi(x_{h,r})=\frac{Xh}{4r},
\]

\[
 W\!\left(\sqrt{\frac{q_Xh^2}{4x_{h,r}}}\right)=W(r/y),\qquad
 x_{h,r}^{-3/4}|\phi''(x_{h,r})|^{-1/2}=2J^{-1/2}.
\]

Hence the stationary principal family is

\[
 2e(-1/8)L^{3/2}J^{-1/2}
 \sum_{h\ {\rm odd}}
 \frac{\chi_4(h)\eta_L(h)\Phi(h/(H+1))}{h}
 \sum_{J/2\le r\le J}^{\star}
 W(r/y)e\!\left(\frac{Xh}{4r}\right).
\tag{137.S5}
\]

This is the original reciprocal hard-TOP principal family. The direct
\(m\)-B-process gives the same phase, profile, Hessian factor, and
range, and a second process returns the square-root phase. Endpoint
samples, zero and nonstationary modes, stationary remainders, crossings,
and square restoration keep their prior owners. Equation (137.S5) is
not by itself a full finite-sum identity.

Complementary-divisor switching is an exact involution with a transformed
literal profile. Completing to

\[
 C_L(n)=\frac{r_2(n)}4-R_L(n)
\]

introduces an uncontrolled complement. Importing the desired
Gauss-circle conclusion for the full radial term would be circular; an
independent localized radial theorem would be admissible new mathematics
but would still leave \(R_L\) open.

## Proof and exponent status

The smallest unresolved object remains the fixed-centre scalar (137.S1).
It needs a new actual-direction additive-twist theorem saving
\(L^{1/2-o(1)}\). Fibrewise modulus, positive energy, centre averaging,
smooth-amplitude curvature, divisor switching, full-\(r_2\) replacement,
and a repeated canonical transform are now parked at this interface.

Hard TOP remains open. BAL and all required UNBAL owners remain open, so
M9-M2 remains open. Both direct M9-M1 parents and the lower-GAR
alternative remain open. Endpoint uniformity, M9, the conditional
quarter bridge, and the Gauss-circle target remain open.

The strongest internally proved exponent remains

\[
 \frac13.
\]

The separately audited external Li--Yang benchmark remains

\[
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots .
\]

Round 137 proves no exponent improvement.

Resulting graph SHA-256:
56de446648dfb7a492fbb4b46c38d840fb14ac306df61bf61d466d26abfbe797
