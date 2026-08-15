# Round 54 discovery report: exact Fejer correlation and its sharp capacity ledger

## 1. Result: reduction lemma and scoped no-go

Let

\[
 N_0=16\sqrt X,
 \qquad
 S_X=\sum_{n\leq N_0}^{*}A_X(n)n^{-3/4}e(\sqrt{Xn}).
\]

There is an exact coefficient-preserving Fejer identity, stated below, whose
off-diagonal terms are precisely the shifted correlations in the round
packet.  After an exact dyadic decomposition in the radial variable, a block
with \(n\asymp Y\) can meet the target after one differencing step if, for
some

\[
 Y^{1/2}\leq R\leq Y,
\]

its Fejer-weighted signed correlation satisfies

\[
 \left|\sum_{1\leq r<R}\left(1-\frac rR\right)
        \mathcal C_{Y,r}(X)\right|
 \ll_\varepsilon X^\varepsilon\frac RY.                 \tag{1.1}
\]

The genuinely weakest sufficient assertion is the corresponding bound for
the nonnegative diagonal-plus-correlation Fejer form; (1.1) is a convenient
slightly stronger signed theorem.  At the minimal useful value
\(R=Y^{1/2}\), (1.1) asks for \(Y^{-1/2+o(1)}\), whereas termwise absolute
values give \(1\).  For the largest block \(Y\asymp N_0\asymp X^{1/2}\), the
missing factor in the quadratic correlation is therefore

\[
 Y^{-1/2}=X^{-1/4+o(1)},
\]

whose square root is exactly the missing \(X^{-1/8}\) in the radial sum.

The sharp no-go is the following.  Taking absolute values of the shifted
correlations, using only divisor bounds, or treating \(A_X(n)\) as an
arbitrary divisor-bounded coefficient gives no improvement at any \(R\).
On a dyadic block it recovers exactly the absolute capacity \(Y^{1/4+o(1)}\);
on the unsplit global interval its best choice \(R=N_0\) again gives
\(N_0^{1/4+o(1)}=X^{1/8+o(1)}\).  This obstruction is sharp for the class of
arbitrary bounded coefficients.  It does **not** rule out (1.1) for the
actual angular coefficient; (1.1), with the full moving symbol below, is the
first unproved step.

No numerical experiment and no external theorem are used.

## 2. Exact statement and hypotheses

Put \(M=\lfloor N_0\rfloor\) and encode the radial top star by

\[
 \tau_X(n)=
 \begin{cases}
 1,&1\leq n<N_0,\\
 \tfrac12,&n=N_0\in\mathbb Z,\\
 0,&\text{otherwise}.
 \end{cases}
\]

Thus, after zero extension to all integers,

\[
 c_n=\tau_X(n)A_X(n)n^{-3/4}e(\sqrt{Xn}),
 \qquad S_X=\sum_{n\in\mathbb Z}c_n.                     \tag{2.1}
\]

For any consecutive integer interval \(I=[a,b]\subseteq[1,M]\), let
\(L=b-a+1\), \(c_{I,n}=\mathbf 1_I(n)c_n\), and \(1\leq R\leq L\).  Define

\[
 Q_I=\sum_n|c_{I,n}|^2                                      \tag{2.2}
\]

and, for \(1\leq r<R\),

\[
 \begin{split}
 \mathcal C_{I,r}(X)
   &=\sum_n c_{I,n+r}\overline{c_{I,n}}\\
   &=\sum_n\mathbf1_I(n+r)\mathbf1_I(n)
       \tau_X(n+r)\tau_X(n)
       A_X(n+r)\overline{A_X(n)}((n+r)n)^{-3/4}\\
   &\hspace{35mm}\times
       e\!\left(\sqrt X(\sqrt{n+r}-\sqrt n)\right).
                                                               \tag{2.3}
 \end{split}
\]

The exact Fejer form is

\[
 \mathfrak F_{I,R}
 =Q_I+2\operatorname {Re}\sum_{1\leq r<R}
       \left(1-\frac rR\right)\mathcal C_{I,r}(X).           \tag{2.4}
\]

Then

\[
 \boxed{
 \mathfrak F_{I,R}
 =\frac1R\sum_{k=a-R+1}^{b}
       \left|\sum_{s=0}^{R-1}c_{I,k+s}\right|^2\geq0,}
                                                               \tag{2.5}
\]

and the exact finite van-der-Corput inequality is

\[
 \boxed{
 \left|\sum_{n\in I}c_n\right|^2
 \leq\frac{L+R-1}{R}\,\mathfrak F_{I,R}.}                  \tag{2.6}
\]

For the full interval \(I=[1,M]\), (2.3) is exactly the packet's
\(\mathcal C_r(X)\).  If \(N_0\) is integral, its shifted upper term
\(n=N_0-r\) has the single radial factor \(1/2\).  The diagonal top term in
\(Q_I\) has factor \(1/4\).  These factors are separate from every angular
profile star.

For a dyadic interval \(I_Y\) of length \(L\asymp Y\) on which
\(n\asymp Y\), define \(\mathcal C_{Y,r}=\mathcal C_{I_Y,r}\).  The literal
weakest Fejer theorem sufficient for a target-sized block is

\[
 \boxed{
 \mathfrak F_{I_Y,R}\ll_\varepsilon X^\varepsilon\frac RY.}
                                                               \tag{FSC}
\]

Indeed, (2.6) then gives \(\sum_{n\in I_Y}c_n\ll_\varepsilon
X^\varepsilon\).  A conventional, easier-to-interface but stronger
sufficient theorem is (1.1), uniformly for one choice
\(Y^{1/2}\leq R\leq Y\), because the diagonal already obeys
\(Q_{I_Y}\ll_\varepsilon X^\varepsilon Y^{-1/2}\).
Indeed,

\[
 Y^{-1/2}\leq \frac RY
 \quad\Longrightarrow\quad
 \mathfrak F_{I_Y,R}
 \leq Q_{I_Y}
 +2\left|\sum_{r<R}\left(1-\frac rR\right)\mathcal C_{Y,r}\right|
 \ll_\varepsilon X^\varepsilon\frac RY.                    \tag{2.9}
\]

Thus (1.1) is genuinely sufficient with no negative off-diagonal main term
and no cancellation against the diagonal.  A negative correlation main term
would be needed only if one insisted on \(R<Y^{1/2}\).

For the global implication, partition \([1,M]\cap\mathbb Z\) exactly into
the consecutive shells

\[
 \left(M2^{-k-1},M2^{-k}\right]\cap\mathbb Z
\]

until only \(O(1)\) integers remain.  Every nontrivial shell has
length comparable to its radial scale \(Y\), the unique global top star
stays on the first shell, and the \(O(\log X)\) shell bounds are absorbed
by \(X^\varepsilon\).  Hence uniform FSC, or (1.1) with
\(R\geq Y^{1/2}\), really implies the global complex GAR bound and therefore
its required real part.

The exact shifted incidence is most compactly written by putting

\[
 \omega_{j,X}(h,q)=
 \mathbf1_{h\leq H_j}\Phi\!\left(\frac h{H_j+1}\right)
 \left[w_j\!\left(2\sqrt{\frac{Xh}{q}}\right)\right]^*,
 \qquad q\ \text{odd}.                                      \tag{2.7}
\]

Thus \(\Omega_X^*(hq,h)=\sum_j\omega_{j,X}(h,q)\).  With
\(m=h_1q_1\) and \(n=h_2q_2\), (2.3) becomes

\[
\boxed{
\begin{split}
 \mathcal C_{I,r}(X)
  ={}&\sum_{j_1,j_2}
 \sum_{\substack{h_1,h_2\geq1;\ q_1,q_2\geq1,\ q_1,q_2\ \mathrm{odd}\\
                   h_1q_1-h_2q_2=r}}
 \mathbf1_I(h_1q_1)\mathbf1_I(h_2q_2)
 \tau_X(h_1q_1)\tau_X(h_2q_2)\\
 &\quad\times
 \chi_4(q_1)\overline{\chi_4(q_2)}
 \omega_{j_1,X}(h_1,q_1)
 \overline{\omega_{j_2,X}(h_2,q_2)}\\
 &\quad\times (h_1q_1h_2q_2)^{-3/4}
 e\!\left(\sqrt X
       (\sqrt{h_1q_1}-\sqrt{h_2q_2})\right).
                                                               \tag{2.8}
\end{split}}
\]

All displayed angular quantities are real in the present problem, but the
conjugates in (2.3) and (2.8) record the Hermitian ownership correctly.
There is no (r_2)-replacement and no discarded angular floor or scale.

## 3. Proof and derivation

### 3.1 Exact differencing

Every (c_{I,n}) occurs exactly (R) times in the finite window sum, so

\[
 R\sum_{n\in I}c_n
 =\sum_{k=a-R+1}^{b}\sum_{s=0}^{R-1}c_{I,k+s}.               \tag{3.1}
\]

Cauchy--Schwarz in the (L+R-1) window starts gives

\[
 R^2\left|\sum_{n\in I}c_n\right|^2
 \leq(L+R-1)\sum_{k=a-R+1}^{b}
       \left|\sum_{s=0}^{R-1}c_{I,k+s}\right|^2.            \tag{3.2}
\]

Expanding the last square, the \(r=0\) pairs occur \(R\) times and the
ordered pairs at displacement \(r>0\) occur \(R-r\) times in each
orientation.  Hence the last sum is \(R\mathfrak F_{I,R}\), proving
(2.5)--(2.6).  Zero extension accounts for both interval boundaries, so
there is no omitted endpoint error.

Substituting the exact divisor formula for each \(A_X\), then writing
\(n+r=h_1q_1\), \(n=h_2q_2\), gives (2.8).  In particular the additive
condition is exactly

\[
 h_1q_1-h_2q_2=r,                                           \tag{3.3}
\]

not a congruence and not a same-product fiber.

### 3.2 Real-part scope

Let \(\zeta=e(1/8)\).  The route (2.6) uses

\[
 |\operatorname {Re}(\zeta S_I)|\leq |S_I|,                 \tag{3.4}
\]

so it deliberately proves the stronger complex estimate.  This loss is
not silent.  Applying Fejer directly to the real sequence
\(x_n=\operatorname {Re}(\zeta c_{I,n})\) does not retain only (2.3):

\[
 \sum_nx_{n+r}x_n
 =\frac12\operatorname {Re}\mathcal C_{I,r}
  +\frac12\operatorname {Re}\!\left\{\zeta^2\mathcal P_{I,r}\right\},
                                                               \tag{3.5}
\]

where

\[
 \mathcal P_{I,r}=\sum_n c_{I,n+r}c_{I,n}                   \tag{3.6}
\]

has the sum phase
\(e(\sqrt X(\sqrt{n+r}+\sqrt n))\) and an unconjugated coefficient
product.  Thus a genuinely phase-aware real-part argument must control
both kernels.  The Hermitian shifted-difference kernel alone lawfully
controls the target only through the stronger modulus bound (3.4).

### 3.3 The \(R,Y,N\) ledger

The accepted profiles are nonnegative and form a subpartition after the
height cutoff.  Also \(0\leq\Phi(u)\leq1\) for \(0<u<1\): for
\(u\leq1/2\), this follows from \(\tan(\pi u)\geq\pi u\), and the identity
\(\Phi(1-u)=1-\Phi(u)\) handles \(u\geq1/2\).  Consequently

\[
 |\Omega_X^*(n,h)|\leq1,
 \qquad |A_X(n)|\leq d(n)\ll_\varepsilon n^\varepsilon.     \tag{3.7}
\]

On \(I_Y\), (3.7) gives

\[
 Q_{I_Y}\ll_\varepsilon X^\varepsilon Y^{-1/2},
 \qquad
 |\mathcal C_{Y,r}(X)|
 \ll_\varepsilon X^\varepsilon Y^{-1/2}\quad(1\leq r\leq Y).
                                                               \tag{3.8}
\]

Write \(R=Y^\rho\).  The exact exponent ledger is

| item | bound from (2.6) and (3.8) | exponent in \(Y\) |
|---|---:|---:|
| diagonal contribution to block modulus | \(Y^{1/4}R^{-1/2}\) | \(1/4-\rho/2\) |
| absolute Fejer shift mass | \(RY^{-1/2+o(1)}\) | \(\rho-1/2\) |
| resulting absolute block bound | \(Y^{1/4+o(1)}\) | \(1/4\) |
| FSC/ASC shift scale | \(R/Y\) | \(\rho-1\) |
| required gain over absolute shift mass | \(Y^{-1/2}\) | \(-1/2\) |

The diagonal is target-sized exactly when \(R\geq Y^{1/2}\).  Once this
holds, (1.1) and (3.8) imply FSC.  A uniform per-shift estimate

\[
 |\mathcal C_{Y,r}(X)|\ll_\varepsilon X^\varepsilon Y^{-1}
                                                               \tag{3.9}
\]

would be sufficient, but is stronger than the required signed average.

For comparison, on the unsplit interval (3.7) and

\[
 \sum_{n\geq1}(n(n+r))^{-3/4}\ll r^{-1/2}                   \tag{3.10}
\]

give

\[
 Q_{[1,M]}\ll_\varepsilon X^\varepsilon,
 \quad |\mathcal C_r|\ll_\varepsilon X^\varepsilon r^{-1/2},
 \quad
 |S_X|\ll_\varepsilon X^\varepsilon N_0^{1/2}R^{-1/4}.
                                                               \tag{3.11}
\]

The best legal choice \(R\asymp N_0\) in (3.11) is only
\(N_0^{1/4+o(1)}=X^{1/8+o(1)}\).  Dyadic localization removes the
irrelevant low-\(n\) diagonal and lowers the useful differencing length to
\(R\asymp Y^{1/2}\), but it does not reduce the signed saving demanded by
(1.1).

### 3.4 Sharpness of the scoped no-go

The direct triangle inequality on \(I_Y\) is

\[
 \sum_{n\in I_Y}|A_X(n)|n^{-3/4}
 \ll_\varepsilon X^\varepsilon Y^{1/4}.                     \tag{3.12}
\]

Equations (2.6) and (3.8), after taking every
\(|\mathcal C_{Y,r}|\) separately, give the same bound for every
\(R\).  This is sharp for coefficient-blind methods: on \(I_Y\), replace
the actual coefficient by the bounded adversarial coefficient

\[
 \widetilde A(n)=e(-\sqrt{Xn}).                              \tag{3.13}
\]

Then \(|\widetilde A(n)|=1\), every transformed term is the
positive number \(n^{-3/4}\),
\(\widetilde{\mathcal C}_{Y,r}\asymp Y^{-1/2}\) for
\(1\leq r\leq R\leq Y/2\), and both (3.12) and the absolute Fejer ledger
are attained up to constants.  Therefore phase curvature plus only a
coefficient-size hypothesis cannot prove the desired saving.  Any advance
must use the actual product incidence, the two \(\chi_4\) factors, and the
coupled angular symbols in (2.8).

### 3.5 Radial derivative test: smooth positive control, actual-symbol obstruction

For fixed \(r\), the exact shifted radial phase is

\[
 \varphi_r(t)=\sqrt X(\sqrt{t+r}-\sqrt t)
 =\frac{\sqrt X\,r}{\sqrt{t+r}+\sqrt t},
\]

with

\[
 \varphi_r'(t)=\frac{\sqrt X}{2}
   \big((t+r)^{-1/2}-t^{-1/2}\big),\qquad
 \varphi_r''(t)=\frac{\sqrt X}{4}
   \big(t^{-3/2}-(t+r)^{-3/2}\big).                         \tag{3.14}
\]

Uniformly for \(t\asymp Y\) and \(1\leq r\leq Y\),

\[
 |\varphi_r'(t)|\asymp \sqrt X\,rY^{-3/2},\qquad
 \varphi_r''(t)\asymp \sqrt X\,rY^{-5/2}.                   \tag{3.15}
\]

This calculation gives a useful positive control but not an
actual-coefficient estimate.  If the coefficient multiplying the phase
were a smooth weight of size \(Y^{-3/2}\) and total variation
\(O(Y^{-3/2})\), the classical second-derivative lemma would give

\[
 |\mathcal C^{\rm sm}_{Y,r}|
 \ll
 X^{1/4}r^{1/2}Y^{-7/4}
 +X^{-1/4}r^{-1/2}Y^{-1/4}.                                \tag{3.16}
\]

Summing (3.16) for \(r<R\) yields

\[
 \sum_{r<R}|\mathcal C^{\rm sm}_{Y,r}|
 \ll
 X^{1/4}Y^{-7/4}R^{3/2}
 +X^{-1/4}Y^{-1/4}R^{1/2}.                                \tag{3.17}
\]

The first term in (3.17) is at most \(R/Y\) only when

\[
 R\ll R_{\rm res}:=\frac{Y^{3/2}}{\sqrt X},
\]

while the second is at most \(R/Y\) only when
\(R\gg R_{\rm res}\).  Thus the raw second-derivative ledger balances
precisely at

\[
 R\asymp R_{\rm res}.                                      \tag{3.18}
\]

Combining (3.18) with the diagonal requirement \(R\geq Y^{1/2}\)
forces \(Y\gg\sqrt X\).  Hence smooth radial curvature has exactly enough
capacity on the top radial blocks \(Y\asymp\sqrt X\), with
\(R\asymp Y^{1/2}\), but it supplies no uniform lower-block range by this
one-step estimate.

More importantly, (3.16) is not applicable after retaining the actual
coefficient.  The amplitude

\[
 B_{X,r}(n)=A_X(n+r)\overline{A_X(n)}
\]

changes whenever either integer acquires or loses a divisor and whenever
an angular floor or profile star changes.  No accepted bounded-variation
or partial-sum theorem exists for \(B_{X,r}\).  Its elementary variation
bound is only

\[
 \sum_{n\asymp Y}|B_{X,r}(n+1)-B_{X,r}(n)|
 \ll_\varepsilon X^\varepsilon Y.                          \tag{3.19}
\]

At the top scale, a first-derivative estimate for the phase alone gives
partial sums of size \(O(Y^{1/2}/r)\) before the radial normalization.
Abel summation using (3.19) therefore gives only
\(O_\varepsilon(X^\varepsilon/r)\) for the normalized correlation, and
the \(r\)-sum is \(O_\varepsilon(X^\varepsilon)\), missing (1.1) by the
same factor \(Y^{1/2}\).

This loss is not merely a technical choice of derivative lemma.  By
(3.15), integer derivative resonances occur on the scale
\[
 |\varphi_r'|\asymp r/R_{\rm res}.
\]
Applying a \(B\)-process through them introduces dual integer modes coupled
to \(B_{X,r}\).  Expanding \(B_{X,r}\) returns exactly (2.8), now with an
additional additive twist and with
\(h_1q_1-h_2q_2=r\).  Controlling those dual modes is an actual shifted
divisor-correlation theorem, not a phase-only estimate.  Thus radial
derivative cancellation proves a smooth-amplitude positive control but,
with the actual \(A_X\) retained, returns the same signed arithmetic
survivor rather than a nonempty proved range.

## 4. First doubtful or unproved step

The first unproved step is exactly the actual-coefficient averaged theorem
(1.1), or the weaker nonnegative form FSC, uniformly on every dyadic radial
block with \(Y^{1/2}\leq R\leq Y\).  Written without abbreviations, it is an
average over

\[
 h_1q_1-h_2q_2=r,\qquad 1\leq r<R,\qquad q_1,q_2\ \text{odd},
\]

with the sign \(\chi_4(q_1)\chi_4(q_2)\), the exact square-root difference
phase, two independent height floors, two dyadic scale sums, and every
profile star retained.  No permitted accepted result supplies the
(Y^{-1/2}) gain over its absolute capacity.

At \(R=Y^{1/2}\), proving FSC amounts to a mean-square local cancellation
statement at the diagonal scale.  At \(R\asymp Y\), it is a Cesaro
mean-square statement for long partial sums.  Merely enlarging (R) does
not reduce the required (Y^{1/2}) correlation saving.  A source theorem
for a fixed shifted divisor function is not applicable unless it also
handles the moving (X)-dependent symbols in (2.8), uniformly in
(r,R,Y,X).

Even a proof of (1.1) would establish the physical global angular radial
estimate through the accepted recombination, not automatically the
connector-completed alpha transition.  The latter still needs a common-
antecedent transfer theorem preserving Plemelj order, finite connectors,
and outside-height boundary terms.

## 5. Required control tests and outcomes

| control | outcome |
|---|---|
| `exact_differencing` | Pass.  (2.5) is an equality; (2.6) has the exact factor \((L+R-1)/R\), all \(R-r\) multiplicities, and no hidden boundary error. |
| `real_part_scope` | Pass with recorded strengthening.  The Hermitian kernel controls \(\lvert S\rvert\); an exact real-only route also creates the sum-phase kernel (3.6). |
| `shifted_incidence` | Pass.  Expansion (2.8) keeps \(h_1q_1-h_2q_2=r\) exactly. |
| `coefficient_ownership` | Pass.  Each leg owns one character, one height floor, one Vaaler factor, one scale profile, and one angular star.  The radial phase and power are owned once after forming the two products. |
| `endpoint_stars` | Pass.  The radial top contributes \(\tau_X(n+r)\tau_X(n)\); its diagonal square is \(1/4\).  The two angular stars remain separate and may multiply.  Artificial dyadic endpoints are ordinary hard cutoffs, not stars. |
| `R_N_exponents` | Pass.  The global and localized ledgers (3.8)--(3.11) identify \(R_{\min}=Y^{1/2}\) and the exact missing \(Y^{-1/2}\) correlation factor. |
| `absolute_capacity` | Fails as a proof route, sharply.  Absolute correlations reproduce \(Y^{1/4+o(1)}\), and (3.13) saturates the coefficient-blind inequality. |
| `radial_phase_derivatives` | Scoped pass/no-go.  Smooth curvature balances at \(R=Y^{3/2}/\sqrt X\), meeting the diagonal only on top blocks; the actual divisor amplitude has no BV theorem and its elementary Abel cost loses \(Y^{1/2}\). |
| `alpha_transfer_scope` | Open and explicitly separated.  Physical Fejer differencing contains no alpha connectors, Plemelj limit, or outside-height trace. |
| `downstream_scope` | Pass.  No claim is made for the alpha branch, M9-M1, M9, or the Gauss-circle target. |

Owner ledger:

| object | exact owner |
|---|---|
| \(\tau_X\) and the half weight at \(N_0\) | global radial endpoint, outside \(A_X\) |
| \(\mathbf1_I\) | finite radial localization introduced for differencing |
| \(1-r/R\) and \(L+R-1\) | Fejer window algebra |
| \(\chi_4(q_i)\) | odd divisor leg \(i\) |
| \(H_{j_i},\Phi,w_{j_i}\), angular star | scale/divisor leg \(i\) |
| \(e(\sqrt X(\sqrt m-\sqrt n))\) | Hermitian radial phase pair |
| external \(X^{1/4}\), hard-top boundary, inactive bottom, transform errors | not in \(S_X\); remain in the accepted recombination ledger |
| alpha masks, Plemelj terms, connectors, outside-height boundaries | not present in this physical correlation and not transferred |

## 6. Dependencies and exact artifacts used

The derivation used only:

- `protocol.md`;
- `state/proof_obligations.yml`, for the authoritative statuses and the
  exact statements of the global angular and alpha obligations;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-global-angular-shifted-correlation/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-alpha-coupled-dyadic-difference/synthesis.md`,
  for scale coherence, star ownership, and the prohibition on a scale-only
  saving;
- `rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md`, for the
  exact \(A_X\), \(\Omega_X^*\), global normalization, and physical transfer
  scope;
- `rounds/codex-managed/m9-m1-ordered-denominator-resonance-cells/synthesis.md`,
  for the exact restricted-product geometry and the prohibition on
  product-fiber absolute values;
- `rounds/codex-managed/m9-m1-near-product-character-kernel/synthesis.md`,
  for the earlier coefficient-norm and cross-product obstructions.

No external literature theorem is invoked, so there is no source hypothesis
to import or certify in this report.  The work is 100% analytical.

## 7. Recommended state effect

**Promote** a scoped exact-reduction node containing (2.2)--(2.8), the
global and dyadic target ledgers, and the real-part warning (3.5).

**Promote** the scoped no-go that termwise absolute shifted correlations,
ordinary divisor bounds, generic square-root phase curvature with arbitrary
coefficients, and coefficient-blind Fejer differencing cannot improve the
\(X^{1/8+o(1)}\) normalized absolute capacity.  Its adversarial sharpness
statement must not be mislabeled as a lower bound for the actual
\(A_X(n)\).

**Retain open** the averaged actual-symbol shifted-correlation theorem
(1.1)/FSC.  The preferred next kernel is the minimal block
\(R\asymp Y^{1/2}\), where it asks for

\[
 \sum_{r<R}\left(1-\frac rR\right)
 \sum_{h_1q_1-h_2q_2=r}\big(\text{the exact signed weight in (2.8)}\big)
 \ll_\varepsilon X^\varepsilon Y^{-1/2}.
\]

Do not promote the physical GAR estimate, the connector-completed alpha
bound, M9-M1, M9, or the final theorem.  A later proof must either establish
this signed product-shift theorem with exact source hypotheses or find a
different coefficient-sensitive mechanism.
