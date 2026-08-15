# Round 40 synthesis: isolate the signed diagonal before absolute symbol bounds

Campaign: `m9-m1-beta-translation-divided-difference`  
Round type: beta translation divided difference  
Graph SHA-256 before patch: `d98e136765299e92cd0f959cc9666fe521435ef0c8c1a948fdd55be6065815c0`

## Conductor decision

Round 40 corrects the terminal-symbol interface a second time. The
fixed-physical-height translation identity is exact, but the complete
singular regularizer cannot satisfy the all-absolute mixed norm adopted in
Round 39. An actual diagonal term has a nonzero \(1/\nu\) Cauchy tail.
The finite contour operator is nevertheless target-safe because that term
has an exact signed logarithmic primitive.

The correct cell interface is therefore hybrid:

1. form the diagonal Cauchy section, with its moving faces and common
   face-log ownership, before taking absolute values or applying Morse
   localization;
2. impose the absolute mixed physical-height norm only on the
   off-diagonal divided difference and on smooth ordinary-\(\mu\) shares;
3. keep the two mixed-derivative terms recombined as endpoint divided
   differences.

This repairs the previously promoted separated \(R_1\) finite-section BV
and local \(q^{-2}\) conclusion, but it invalidates that node's claimed
pointwise domination by one integrable height weight. The complete actual
off-diagonal/connector/Morse estimate remains open.

## Exact translation identity

Put

\[
y=L-\nu,\qquad F(L,y)=H(L,L-y).
\]

At fixed physical \(\nu\),

\[
\partial_LH=F_L+F_y,
\qquad
(\partial_L+\partial_\nu)H(L,L)=F_L(L,0).
\]

Thus the coefficient isolated in Round 39 is

\[
\boxed{
\mathfrak E_H(L,L-y)
=\int_0^1F_{Ly}(L,ty)\,dt
+\int_0^1tF_{yy}(L,ty)\,dt.}                    \tag{40.1}
\]

There is no diagonal \(F_y(L,0)/y\) term. That term arose in an erroneous
conductor calculation which differentiated at fixed translation \(y\)
rather than fixed physical height \(\nu\); the calculation was retracted
and the campaign manifest repaired before closing the round.

Equation (40.1) is not a positive representation. For the actual
separated height profile, separately taking absolute values of its two
integrals loses four pointwise powers on a long translated segment. The
two terms must first be recombined into the original endpoint divided
difference.

## Diagonal Cauchy module

For the singular hard-top share, write

\[
\mathcal R_A[H]=K_C+K_\Delta,
\]

\[
K_C=-\frac{iH(L,L)}{2A(L)D(L,\nu)},
\qquad
K_\Delta=\frac{H(L,\nu)-H(L,L)}{(L-\nu)D(L,\nu)},             \tag{40.2}
\]

where

\[
A=-1-\frac b2-i(L+\beta),
\qquad D=A+\frac i2(L-\nu).
\]

For fixed \(L\),

\[
K_C(L,\nu)=\frac{H(L,L)}{A(L)\nu}+O_L(\nu^{-2}).             \tag{40.3}
\]

Hence \(\int|K_C|d\nu=\infty\) whenever the diagonal coefficient is
nonzero. This is already an exact counterexample inside the separated
actual \(R_1\) kernel, and its fixed-\(\nu\) derivative generically has the
same logarithmic absolute tail.

Let

\[
I_{U,V}(L)=[-V,V]\cap[L-U,L+U]=[p(L),q(L)].
\]

On the continuous left-half-plane logarithm,

\[
\boxed{
C_{U,V}[H](L):=\int_{p(L)}^{q(L)}K_C(L,\nu)\,d\nu
=\frac{H(L,L)}{A(L)}
\{\Log D(L,q(L))-\Log D(L,p(L))\}.}              \tag{40.4}
\]

The upper moving physical face has positive Leibniz sign and the lower
moving physical face negative sign. Affine switches agree and collapsed
sections vanish. On either actual separated saddle,

\[
\|C_{U,V}\|_\infty+operatorname {Var}C_{U,V}
\ll_b\lambda^{-4}\log(2+\lambda),                \tag{40.5}
\]

uniformly in the height cutoffs. The same bound is stable through full,
half-, entry-, and exit-Fresnel cells when the exact Morse operator is
applied after (40.4) is formed. In symmetric exhaustion,

\[
C_{T,T}[H](L)\longrightarrow i\pi\frac{H(L,L)}{A(L)}.         \tag{40.6}
\]

The explicit constant-numerator face log and (40.4) must retain one
common finite-section branch and ownership ledger.

## Separated kernel repair and remaining gap

For \(H(L,\nu)=f_b(\nu)\), the off-diagonal term \(K_\Delta\) is
absolutely integrable. Direct physical-center, top-diagonal, radial-ridge,
and far-tail estimates give its value, fixed-height derivative, and moving
trace norm at the required \(\lambda^{-2}\) scale. Combined with (40.5),
the separated finite-section amplitude has sup plus BV
\(O_b(\lambda^{-2})\); after the accepted stationary numerator it retains
the local \(D_j/(q\lambda)=D_j/(q^2\theta_j(x))\) coefficient. This is
the corrected content of the Round-31 separated-\(R_1\) lemma.

The discovery report claims the same absolute off-diagonal and exact
Morse bounds for the complete phase-removed terminal package. The
hostile audit identifies the unclosed seam: the displayed factorization
is exact only for a frozen singular share, while smooth profiles,
connector ownership, affine restrictions, and the normalized Morse
remainder need a complete one-count product formula. Moreover (40.1)
cannot be estimated by separate absolute mixed derivatives. The complete
hybrid terminal symbol is therefore retained open.

## State effect

- Promote the exact fixed-height identity (40.1).
- Promote the signed diagonal finite-section/logarithm module
  (40.4)--(40.6) in its actual separated scope.
- Correct, rather than discard, the separated \(R_1\) finite-section BV
  lemma: its conclusion and local \(q^{-2}\) scale survive under a hybrid
  proof, while its integrable pointwise weight assertion is false.
- Revise the axial-subtracted terminal-symbol obligation and the
  conditional cell-sum reduction to accept the hybrid signed-diagonal plus
  absolute-off-diagonal norm.
- Reject an all-absolute norm for \(\mathcal R_A\), pointwise Morse before
  the Cauchy section, termwise absolute use of (40.1), and extending a
  narrow factorization to every connector/smooth stratum without an exact
  formula.
- Retain bounded-alpha, double-bounded, the complete beta transition,
  M9-M1, M9-M2, M9, and the Gauss-circle target as open.

No computation or external theorem was used; the round allocation was
100% analytical/algebraic.
