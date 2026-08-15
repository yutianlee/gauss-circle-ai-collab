## Result

**Exact normalization, corrected Farey capacity, and source-hypothesis
no-go.** The order-\(J\) Farey representative and the conductor-\(J\)
Heath--Brown representative agree, but the sharp nonaxial normalization is
smaller than the initially proposed \(T/c\) coefficient. For an odd modulus,
one compatible nonaxial stationary branch has

\[
 \alpha_{c,b}(\rho,\sigma;X)
 \asymp
 \frac{T}{c}
 \left(\frac{c}{J}\right)^{1/2}
 |\rho\sigma|^{-1/4}
 \times\{\text{a fixed smooth symbol}\}.                         \tag{1.1}
\]

Here \(b\asymp c/T\), the effective nonaxial dual variables
\(\rho,\sigma\) are \(O(1)\), and incompatible signs or larger dual
variables are nonstationary. Thus \(T/c\) is the outer Poisson/local
prefactor and a valid coarse upper envelope, but it is not the leading
beta-integrated coefficient when \(c=o(J)\). On \(c\asymp C\), the sharp
principal nonaxial absolute capacity is

\[
 \#c\;\#b\;\sup|\alpha|
 \asymp
 C\frac{C}{T}\frac{T}{\sqrt{CJ}}
 =\frac{C^{3/2}}{J^{1/2}},                                      \tag{1.2}
\]

not \(C\). Consequently these principal pieces are already at most the
target \(J^{1/2}\) for

\[
                         C\leq J^{2/3}.                          \tag{1.3}
\]

For \(C>J^{2/3}\), their raw required saving is

\[
 \frac{C^{3/2}}{J}
 =
 \frac{C^{3/2}}{T J^{1/2}}\,
 \frac{T}{J^{1/2}}.                                             \tag{1.4}
\]

The first factor in (1.4) recovers inflation caused by the order-\(J\)
representation; the second is the frozen original deficit
\(T/J^{1/2}=X^{1/20}\). At \(C=J\), (1.4) is \(J^{1/2}\), not merely
\(X^{1/20}\). Axial and sharp-cell boundary pieces do not inherit (1.1)
automatically and must be kept separate.

The stationary phase and odd-modulus reciprocity calculation proposed by
the conductor check is correct for the positive compatible branch. With
\(k=\rho\sigma>0\), it gives, up to a fixed Maslov factor and a smooth
amplitude,

\[
 e_{4b}(k\bar c)\,
 e\!\left(
   -\frac{\bigl(\sqrt b\,J+\sqrt{k}/(2\sqrt b)\bigr)^2}{c}
 \right).                                                       \tag{1.5}
\]

The current inverse-fraction large sieves do not accept the second factor
in (1.5) as a harmless weight: its normalized \(b\)- or \(c\)-derivative
has size \(X/T\). Completing the \(c\)-variable modulo \(4b\) does produce
complete sums \(S(n,k;4b)\) with \(n\asymp X/T^2=Q^2\), but the new
coefficient contains the square-root chirp \(e(-J\sqrt n)\). Expanding the
Kloosterman sum and applying the \(B\)-process to that chirp returns a dual
integer \(h\asymp C\), \(h\equiv c\pmod{4b}\), and exactly the phase in
(1.5). This is an involutive Fourier self-return, not a new saving.

No audited primary theorem proves

\[
             |\mathcal D_C|\ll J^{1/2}X^\varepsilon
             \qquad (T\leq C\leq J)                              \tag{1.6}
\]

for the full odd and even families with their actual weights and axes.
Pascadi's 2026 incomplete large sieve is the closest inverse-only result,
but its hypotheses exclude the high-conductor real phase, the
\(\chi_4(c)\) modulus weight, zero arguments, and the two even local
families as stated. DFI has the same coupled-weight obstruction and pays
the square of its derivative parameter. Standard Kuznetsov only becomes
formally available after the second completion and then discards the
special chirp whose elementary \(B\)-process is the self-return above.

There is no actual-symbol counterexample to (1.6). Nonaxial gcd factors
are \(X^{o(1)}\), and exact same-modulus off-diagonal resonances are
subdiagonal by a factor \(T\). The odd \(\rho=0\) axis and the
\(4\mid c,\sigma=0\) axis survive and remain separate open terms.

## Exact statement and hypotheses

Put

\[
 N=\lfloor X\rfloor,\qquad \vartheta=X-N,\qquad
 J=X^{1/2},\qquad Q=X^{1/5},\qquad T=J/Q=X^{3/10}.               \tag{2.1}
\]

Use \(e(z)=e^{2\pi iz}\), \(e_c(z)=e(z/c)\), and
\(\widehat f(\xi)=\int_{\mathbb R}f(t)e(-\xi t)\,dt\). Let
\(K=\widehat g\), where \(g\) is the fixed smooth compactly supported
function from the product-wavelet reduction and is supported away from
zero. Let \(\Omega(x/J,y/J)\) contain the complete fixed one-sided ratio
symbol and cutoffs. The wavelet is

\[
 \mathcal D_{J,T}(X)=
 \sum_{m,n\in\mathbb Z}\chi_4(n)\Omega(m/J,n/J)
 K\!\left(\frac{mn-X}{T}\right).                                \tag{2.2}
\]

The exact Heath--Brown identity at conductor \(J\) is

\[
 \delta(r)=\frac{c_J}{J^2}
 \sum_{c\geq1}\sum_{a\bmod c}^{*}
 e_c(ar)\,
 h\!\left(\frac cJ,\frac r{J^2}\right),
 \qquad c_J=1+O_A(J^{-A}).                                      \tag{2.3}
\]

For \(L_c=[c,4]\), define

\[
\begin{aligned}
 \mathcal I_{c,a}(\rho,\sigma)
  :=\sum_{\ell\in\mathbb Z}\iiint_{\mathbb R^3}
  &\Omega(x/J,y/J)K((t-\vartheta)/T)
  h\!\left(\frac cJ,\frac{xy-N-t}{J^2}\right)\\
  &\times e\!\left(
     -\frac{\rho x}{c}-\frac{\sigma y}{L_c}
     -\left(\ell+\frac ac\right)t
  \right)\,dt\,dx\,dy .                                         \tag{2.4}
\end{aligned}
\]

With

\[
 \mathfrak C_{c,a}(\rho,\sigma)
 =\sum_{u\bmod c}\sum_{v\bmod L_c}
   \chi_4(v)e_c(auv+\rho u)e_{L_c}(\sigma v),                    \tag{2.5}
\]

Poisson summation gives the exact identity

\[
 \mathcal D_{J,T}(X)
 =\frac{c_J}{J^2}
  \sum_{c\geq1}\frac1{cL_c}\sum_{a\bmod c}^{*}e_c(-aN)
  \sum_{\rho,\sigma\in\mathbb Z}
  \mathfrak C_{c,a}(\rho,\sigma)
  \mathcal I_{c,a}(\rho,\sigma).                                \tag{2.6}
\]

The complete local table is

\[
\mathfrak C_{c,a}(\rho,\sigma)=
\begin{cases}
 2ic\,\chi_4(c\sigma)e_c(\lambda_c\rho\sigma\bar a),
   &c\ {\rm odd},\ \sigma\ {\rm odd},\\
 0,&c\ {\rm odd},\ \sigma\ {\rm even},\\
 2c\,\chi_4(v_0)e_{2c}(\sigma v_0),
   &c\equiv2\pmod4,\ \rho,\sigma\ {\rm odd},\\
 0,&c\equiv2\pmod4,\ \rho\sigma\ {\rm even},\\
 -c\,\chi_4(a)\chi_4(\rho)e_c(-\bar a\rho\sigma),
   &4\mid c,\ \rho\ {\rm odd},\\
 0,&4\mid c,\ \rho\ {\rm even},
\end{cases}                                                     \tag{2.7}
\]

where

\[
 \lambda_c=\frac{c^2-1}{4},\qquad
 v_0\equiv-\bar a\rho\pmod c.                                  \tag{2.8}
\]

For a dyadic \(V_C(c)\), \(T\leq C\leq J\), the endpoint variable is
\(a\equiv\epsilon b\pmod c\), \(\epsilon\in\{\pm1\}\), with
\(b\asymp c/T\). All claims involving stationary phase below are restricted
to a smooth interior Farey-cell piece, a fixed one-sided \((u,v)\)-patch,
and compatible nonzero \(\rho,\sigma\). Axes, critical points outside the
patch, and sharp cell endpoints are explicitly excluded from that
asymptotic and require separate bounds.

## Proof or derivation

Inserting (2.7) into (2.6) gives the three exact dyadic families

\[
\begin{aligned}
 \mathcal D_C^{\rm odd}
 &=\frac{ic_J}{2J^2}
 \sum_{\substack{c\ {\rm odd}}}\frac{V_C(c)}c
 \sum_{a\bmod c}^{*}\sum_{\rho\in\mathbb Z}
 \sum_{\substack{\sigma\in\mathbb Z\\\sigma\ {\rm odd}}}
 \chi_4(c\sigma)e_c(-aN+\lambda_c\rho\sigma\bar a)
 \mathcal I_{c,a}(\rho,\sigma),\\
 \mathcal D_C^{(2)}
 &=\frac{c_J}{J^2}
 \sum_{c\equiv2(4)}\frac{V_C(c)}c
 \sum_{a\bmod c}^{*}
 \sum_{\substack{\rho,\sigma\in\mathbb Z\\\rho,\sigma\ {\rm odd}}}
 e_c(-aN)\chi_4(v_0)e_{2c}(\sigma v_0)
 \mathcal I_{c,a}(\rho,\sigma),\\
 \mathcal D_C^{(4)}
 &=-\frac{c_J}{J^2}
 \sum_{4\mid c}\frac{V_C(c)}c
 \sum_{a\bmod c}^{*}
 \sum_{\substack{\rho,\sigma\in\mathbb Z\\\rho\ {\rm odd}}}
 \chi_4(a)\chi_4(\rho)e_c(-aN-\bar a\rho\sigma)
 \mathcal I_{c,a}(\rho,\sigma).
                                                                    \tag{3.1}
\end{aligned}
\]

After \(a\equiv\epsilon b\) and \(\rho\mapsto\epsilon\rho\), the odd
coefficient and phase are, exactly,

\[
 \alpha_{c,b}^{\rm odd,\epsilon}(\rho,\sigma;X)
 =\frac{ic_JV_C(c)}{2J^2c}\chi_4(c\sigma)
   \mathcal I_{c,\epsilon b}(\epsilon\rho,\sigma),               \tag{3.2}
\]

\[
 e_c(-\epsilon bN+\lambda_c\rho\sigma\bar b).                   \tag{3.3}
\]

This fixes the normalization before any stationary approximation.

**Farey cross-check.** The exact offset Poisson formula is

\[
 \sum_s K\!\left(\frac{s-\vartheta}{T}\right)e(-\alpha s)
 =T\sum_{\ell\in\mathbb Z}
 e(-\vartheta(\ell+\alpha))
 \widehat K(T(\ell+\alpha)).                                    \tag{3.4}
\]

In an order-\(J\) cell write
\(\alpha=\epsilon b/c+\beta\). Its width is

\[
 |\beta|\asymp\frac1{cJ},\qquad b\asymp\frac cT.                 \tag{3.5}
\]

The \(x,y\)-Poisson Jacobian \(1/(cL_c)\), the local factor of size
\(c\), and (3.4) give an outer factor \(\asymp T/c\) in all three
parity classes. For odd \(c\), set

\[
 \beta=\frac{\tau}{J^2},\quad x=Ju,\quad y=Jv,\quad
 U=\frac{X}{J^2}=1,\quad R=\frac{J\rho}{c},\quad
 S=\frac{J\sigma}{4c}.                                          \tag{3.6}
\]

The Jacobian satisfies \(d\beta\,dx\,dy=d\tau\,du\,dv\), and the full
continuous phase is

\[
             \Phi(\tau,u,v)=\tau(uv-U)-Ru-Sv.                   \tag{3.7}
\]

Its critical equations are

\[
 uv=U,\qquad \tau v=R,\qquad \tau u=S,\qquad
 \tau^2=\frac{RS}{U}.                                           \tag{3.8}
\]

Since the cell has \(|\tau|\asymp J/c\), (3.8) forces
\(\rho,\sigma=O(1)\) on fixed \(u,v\)-support. At a compatible critical
point,

\[
 \det\Phi''=2uv\tau=2U\tau,\qquad
 |\det\Phi''|^{-1/2}
 =U^{-1/4}\left(\frac cJ\right)^{1/2}
 |\rho\sigma|^{-1/4}.                                          \tag{3.9}
\]

The critical value is

\[
 \Phi_{\rm crit}
 =-2\sqrt{URS}
 =-\frac{J\sqrt{\rho\sigma}}{c}                                \tag{3.10}
\]

for the displayed positive branch. Equations (3.9)--(3.10) prove
(1.1). When \(c\asymp J\), there is no large stationary parameter, but
the uniform \(O(1)\) bound agrees with (3.9). For \(c=o(J)\),
three-variable stationary phase supplies the missing factor
\((c/J)^{1/2}\); integrating only the cell width and recording \(T/c\)
misses it. Summing the \(O(1)\) duals, \(C\) moduli, and \(C/T\)
numerators gives (1.2).

There is no three-variable critical point on either surviving axis.
Consequently smooth interior axial pieces are rapidly decreasing when
\(J/c\) is large. This observation does not by itself bound a sharp
Farey endpoint or the top range \(c\asymp J\); those terms retain the
Ramanujan/twisted arithmetic described below.

**Reciprocity and the \(B\)-process.** For odd \(c\) and
\((4b,c)=1\),

\[
 e_c(\lambda_c k\bar b)
 =e_c(-k\overline{4b})
 =e_{4b}(k\bar c)e\!\left(-\frac{k}{4bc}\right).                \tag{3.11}
\]

The rational centre and (3.10) contribute
\(e(-bX/c-J\sqrt{k}/c)\). Since \(J^2=X\), their product with
(3.11) is exactly (1.5). Other endpoint and sign branches are its
corresponding conjugate/sign variants.

Let

\[
 q=4b,\qquad
 A_b=\left(\sqrt b\,J+\frac{\sqrt{k}}{2\sqrt b}\right)^2.
\]

Poisson summation in \(c\) modulo \(q\) gives schematically, with all
smooth symbols retained,

\[
\begin{aligned}
 &\sum_{c}e_q(k\bar c)W(c/C)e(-A_b/c)\\
 &\qquad=
 \frac1q\sum_{n\in\mathbb Z}S(n,k;q)
 \int_{\mathbb R}W(x/C)e(-A_b/x-nx/q)\,dx.                      \tag{3.12}
\end{aligned}
\]

The compatible stationary frequencies satisfy

\[
 n\asymp\frac{qA_b}{C^2}
 \asymp\frac{X}{T^2}=Q^2,                                      \tag{3.13}
\]

and the integral phase at its critical point is

\[
 -2\sqrt{\frac{A_bn}{q}}
 =-J\sqrt n-\frac{\sqrt{kn}}{2b}.                              \tag{3.14}
\]

Thus Kuznetsov sees complete \(S(n,k;4b)\) only after (3.12), with
modulus \(b\asymp C/T\), index \(n\asymp Q^2\), and the special
coefficient (3.14). A general spectral large sieve may treat this
coefficient arbitrarily, but then it throws away its oscillation.
Pascadi's Theorem 1.5 treats a linear phase \(e(n\alpha)\), not this
square-root chirp; his Theorem 5.2 is an exceptional-spectrum inequality
under a frequency-concentration hypothesis, not a full cancellation
theorem for (3.12).

The elementary \(B\)-process in \(n\) is an exact self-return at the
phase level. Expanding

\[
 S(n,k;q)=\sum_{r\bmod q}^{*}e_q(nr+k\bar r)
\]

and Poisson transforming \(n\), put \(h=r-q\ell\). Stationarity gives

\[
 h\asymp C,\qquad h\equiv r\pmod q,\qquad
 n=\frac{(A_b/b)q^2}{4h^2},                                    \tag{3.15}
\]

and the Legendre value is

\[
 -\frac{(A_b/b)q}{4h}=-\frac{A_b}{h}.                          \tag{3.16}
\]

Renaming \(h=c\) restores
\(e_q(k\bar c)e(-A_b/c)\). The stationary amplitudes are adjoint as
well. Hence a bare second \(B\)-process cannot supply the missing saving.

**Completion, axes, gcd, and resonance.** If \(w_c(b)\) denotes the
actual odd nonaxial weight after removing (3.3), finite Fourier inversion
gives

\[
 \sum_{b\bmod c}^{*}w_c(b)
 e_c(-\epsilon Nb+\lambda_c k\bar b)
 =\frac1c\sum_{h\bmod c}\widehat w_c(h)
 S(h-\epsilon N,\lambda_c k;c),                                \tag{3.17}
\]

\[
 \sum_{h\bmod c}|\widehat w_c(h)|^2
 =c\sum_{b\bmod c}|w_c(b)|^2.                                 \tag{3.18}
\]

The completion dual has length \(T\), but
\(h-\epsilon N\asymp X\); it is illegal to use \(T\) as the
spectral Fourier-index magnitude.

For nonaxial modes,

\[
 (c,\lambda_c\rho\sigma)=(c,\rho\sigma)
 \leq|\rho\sigma|=O(1),                                        \tag{3.19}
\]

up to rapidly decaying tails. The odd \(\rho=0\) axis instead gives

\[
 S(h-\epsilon N,0;c)=c_c(h-\epsilon N),\qquad
 |c_c(r)|\leq(c,r),                                             \tag{3.20}
\]

which can equal \(\varphi(c)\). The \(4\mid c,\sigma=0\) twisted axis
also survives. These zero-index terms are not covered by nonzero-index
Kuznetsov.

For fixed odd \(c\), equality of two nonaxial phases implies

\[
 c\mid(b_1-b_2)
 \bigl(4\epsilon N b_1b_2-\rho\sigma\bigr).                    \tag{3.21}
\]

The second factor is nonzero in the natural ranges. A divisor count,
summed over \(b_1,b_2\ll C/T\), gives

\[
 O_\varepsilon((C/T)^2X^\varepsilon)                           \tag{3.22}
\]

off-diagonal exact resonances, while the incidence diagonal has size
\(\asymp C^2/T\). Exact nonaxial resonances are therefore smaller by
\(T\), up to \(X^\varepsilon\). This does not prove cancellation of the
signed sum.

Finally, a window of width \(T<J\) contains \(O(1)\) squares and fourth
powers, each with divisor-bounded multiplicity. Perfect powers do not
give a lower bound at scale \(J^{1/2}\).

## First doubtful or unproved step

The first unproved step is a uniform decomposition of every exact Farey
cell into:

1. compatible nonaxial stationary pieces satisfying (1.1), including
   uniform transition bounds at \(c\asymp J\);
2. nonstationary interiors and sharp-cell boundary terms;
3. the odd Ramanujan axis and the \(4\mid c\) twisted axis; and
4. the two even-modulus analogues with their exact cusp/character data.

After that decomposition, only \(C>J^{2/3}\) needs nontrivial cancellation
for the principal nonaxial capacity. The required high-conductor estimate
is for the full phase-and-weight class

\[
 \sum_{c\asymp C}\sum_{b\asymp c/T}^{*}
 \sum_{\rho,\sigma}
 \alpha^\epsilon_{c,b}(\rho,\sigma;X)
 e_c(-\epsilon Nb+\lambda_c\rho\sigma\bar b),                  \tag{4.1}
\]

plus both exact even lines of (3.1), and it must save

\[
                  \max\!\left(1,\frac{C^{3/2}}J\right)          \tag{4.2}
\]

relative to (1.2). At \(C=J\), this is \(J^{1/2}\). A statement that
the transformed family only needs the original \(X^{1/20}\) saving omits
the representation-recovery factor in (1.4).

No audited theorem simultaneously permits:

1. the high-conductor real phase \(e(-bX/c)\), or equivalently the
   coupled Archimedean factor in (1.5);
2. the actual matrix weight from (2.4), rather than separated arbitrary
   coefficients;
3. the \(\chi_4(c)\) modulus weight and both even level-four cusp families;
4. zero arguments with their Ramanujan/gcd main terms removed;
5. either the incomplete \(b\)-sum or the completed
   \(n\asymp Q^2\) square-root chirp without losing its structure; and
6. the dyadic saving (4.2).

The algebra through (3.21) is exact. What remains unproved is the uniform
analytic cell decomposition at its seams and the high-conductor
cancellation theorem, not the stationary critical point or reciprocity
identity themselves.

## Required control test and outcome

| Control | Outcome |
|---|---|
| Completeness | **Fail as a direct source import.** The \(b\)-sum has length \(c/T<\sqrt c\). Completion gives (3.17), \(T\) Fourier modes, and moving first argument \(N-h\asymp X\). |
| Numerator length | **Pass.** \(b\asymp c/T\), from \(O(1)\) at \(C=T\) to \(Q\) at \(C=J\). |
| Farey/HB normalization | **Pass with correction.** The cell width is \(1/(cJ)\), the nonaxial dual count is \(O(1)\), but the three-variable Hessian gives \((c/J)^{1/2}|\rho\sigma|^{-1/4}\). The sharp coefficient is \(T/\sqrt{cJ}\), and capacity is \(C^{3/2}/\sqrt J\), not \(C\). |
| Modulus average | **Open.** The original moduli are \(c\asymp C\); after reciprocity/completion the Kuznetsov moduli are \(4b\asymp C/T\), with \(n\asymp Q^2\). |
| Moving arguments | **Obstruction.** \(b\)-completion gives \(N-h\asymp X\). \(c\)-completion gives the chirp \(e(-J\sqrt n-\sqrt{kn}/(2b))\), which a coefficient-blind large sieve discards. |
| Dual-frequency lengths | **Pass with distinction.** Natural nonaxial \(\rho,\sigma\) are \(O(1)\); \(b\)-completion has length \(T\); reciprocity plus \(c\)-completion has \(n\asymp Q^2\), not length \(T\). |
| Coefficient restrictions | **Fail.** DFI requires separated sequences and its weighted corollary pays \(\eta^2\); the coupled phase forces \(\eta\geq X/T\). Pascadi Corollary 5.14 requires uniformly smooth normalized \((d,c)\)-weights. |
| Gcd and conductor four | **Pass with surviving terms.** Nonaxial gcds are \(O(1)\), but axial gcds can be \(c\); the even families require exact level-four cusp and nebentypus data. |
| Axial terms | **Open.** There is no interior three-variable critical point, so lower-conductor smooth pieces are nonstationary; sharp-cell/top-conductor bounds and the Ramanujan/twisted axes remain to be proved. |
| Spectral level and cusp | **Fail for the full family.** Knightly--Li gives a general complete trace formula and twisted Weil factors, but not the incomplete large sieve or a single automatic cusp identification for all lines of (3.1). |
| Smoothing | **Fail for inverse-fraction source import.** A normalized \(b\)- or \(c\)-derivative of \(e(-bX/c)\) costs \(X/T\). |
| Dispersion diagonal | **Obstruction, not a counterexample.** Parseval (3.18) preserves the completion diagonal. |
| Reciprocity phase | **Pass.** Equations (3.11) and (1.5) are exact on the chosen branch; the real centre \(X\), not merely \(N\), is needed for the perfect square. |
| \(B\)-process | **Self-return.** Equations (3.12)--(3.16) return the original \(c\)-family. A second elementary transform supplies no independent cancellation. |
| Exact resonance | **Pass.** Nonaxial off-diagonal exact resonances satisfy (3.21) and are subdiagonal by \(T\); axial divisibility resonances remain separate. |
| Benchmark power | **Corrected.** Principal pieces are target-safe for \(C\leq J^{2/3}\); above that the raw saving is \(C^{3/2}/J\), reaching \(J^{1/2}\) at \(C=J\). |
| Perfect powers | **Pass.** Only \(O(1)\) square/fourth-power products occur in the \(T<J\) window, with \(X^\varepsilon\) divisor mass. |
| Downstream scope | **Pass.** No cone-edge, GAR, \(M9\)-\(M1\), \(M9\), or final-exponent claim is made. |

No numerical experiment was used. Computation could diagnose a local
formula but could not certify the missing asymptotic estimate.

## Dependencies and exact artifacts/sources used

The repository artifacts used were exactly:

* protocol.md;
* state/proof_obligations.yml;
* state/active_campaign.yml;
* the assigned Round-71 brief and derivation_packet.md;
* rounds/codex-managed/m9-m1-near-product-delta-salie/synthesis.md;
* rounds/codex-managed/m9-m1-near-product-delta-salie/reviews/conductor_delta_salie_adjudication.md;
* rounds/codex-managed/m9-m1-near-product-delta-salie/reports/delta_kuznetsov_source_hostile_audit.md.

No sibling Round-71 report was read in producing this independent report.

The primary-source audit was:

* **Exact delta method.** Heath--Brown,
  [*A New Form of the Circle Method, and its Application to Quadratic
  Forms*, J. reine angew. Math. 481 (1996), 149--206](https://ora.ox.ac.uk/objects/uuid%3Abbd3c62f-f010-44b5-8be5-87e903fb0084),
  Theorem 1 and Lemmas 4--5. These give (2.3), the support and derivative
  properties of \(h\), but do not keep an added wavelet numerator complete.

* **Current spectral and incomplete large sieve.** Pascadi,
  [*Large sieve inequalities for exceptional Maass forms and the greatest
  prime factor of \(n^2+1\)*, Forum Math. Pi 14 (2026), e8](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/DC9B30CB4824955671C7B018C473863A/S2050508626100250a.pdf/large-sieve-inequalities-for-exceptional-maass-forms-and-the-greatest-prime-factor-of-dollarn21dollar.pdf),
  Theorems 1.2, 1.5, and 5.2, Assumption 5.4, and Corollaries 5.11 and
  5.14. Corollary 5.14 averages \(r,s,n,c,d\) in
  \(e(\pm n\overline{rd}/(sc))\), requires \((rd,sc)=1\), an admissible
  spectral coefficient sequence, and uniformly smooth normalized
  \((d,c)\)-weights. It corrects the \(D^2NR\) diagonal term in DI
  Theorem 12. It does not include \(e(-bX/c)\), \(n=0\),
  \(\chi_4(c)\), or the even local data. Theorem 1.5 handles
  \(e(n\alpha)\), not (3.14); Theorem 5.2 controls exceptional forms under
  its frequency-measure hypotheses and does not replace the full regular
  spectral analysis.

* **Classical spectral large sieve.** Deshouillers--Iwaniec,
  [*Kloosterman sums and Fourier coefficients of cusp forms*, Invent.
  Math. 70 (1982), 219--288](https://doi.org/10.1007/BF01390728),
  Theorems 5, 7, 11, and 12, using the exact normalization and correction
  recorded by Pascadi. These concern complete generalized Kloosterman
  sums and spectral coefficient sequences at specified levels/cusps. They
  do not justify changing the completed index magnitude \(X\) to its
  displacement span \(T\).

* **Bilinear Kloosterman fractions.** Duke--Friedlander--Iwaniec,
  [*Bilinear forms with Kloosterman fractions*, Invent. Math. 128 (1997),
  23--43](https://www.math.ucla.edu/~wdduke/preprints/bilinear.pdf),
  Theorems 1--2, the weighted Corollary, and Lemma 8. Theorems 1--2 use
  separated coefficients. The Corollary assumes
  \(F^{(j,k)}(m,n)\ll\eta^{j+k}m^{-j}n^{-k}\) and pays \(\eta^2\).
  Here \(\eta\geq X/T\). Lemma 8 allows one incomplete linear-plus-inverse
  phase, but completion/Weil is non-improving for \(c/T<\sqrt c\).
  Dong--Robles--Zeindler,
  [*Bilinear forms with Kloosterman fractions and applications*
  (2026)](https://arxiv.org/abs/2601.00292), improves inverse-only
  separated bounds, not the coupled real phase (1.5).

* **Incomplete inverses at one prime.** Browning--Haynes,
  [*Incomplete Kloosterman sums and multiplicative inverses in short
  intervals*](https://arxiv.org/abs/1204.6374), Theorem 2. It is a mean
  square over disjoint intervals for one fixed prime and one fixed nonzero
  inverse phase. The varying composite modulus, coupled real phase, axes,
  and level-four data here do not match.

* **Kuznetsov completeness.** Kuznetsov,
  [*Petersson's conjecture for cusp forms of weight zero and Linnik's
  conjecture. Sums of Kloosterman sums*](https://www.mathnet.ru/eng/sm2598),
  and Young,
  [*The fourth moment of Dirichlet \(L\)-functions*](https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n1-p01-p.pdf),
  Theorem 2.6. Their geometric side uses complete
  \(S(m,\pm n;c)\), fixed nonzero indices, and prescribed smooth Bessel
  weights. It applies only after a completion such as (3.12), not to the
  original incomplete numerator or to axial zero indices.

* **Level, cusp, twisted gcd, and conductor.** Knightly--Li,
  [*Kuznetsov's trace formula and the Hecke eigenvalues of Maass
  forms*](https://arxiv.org/abs/1202.0189), Theorems 7.14, 8.1, and 9.2.
  These give complete generalized twisted sums at specified level,
  nebentypus, and cusps. Theorem 9.2 retains gcd and character-conductor
  factors. They supply neither the needed incomplete large sieve nor an
  automatic common cusp model for all three parity lines in (3.1).

Every source was checked at the averaged variables, completeness, index
size and motion, coefficient dependence, gcd, level/cusp, nebentypus,
smoothing, axes, and required dyadic power.

## Recommended state effect

**Retain the \(J^{1/2}X^\varepsilon\) fixed-interior wavelet estimate as
open.** Retain the accepted Round-70 short-numerator reduction. Subject
to an independent seam check, promote as evidence:

* the exact HB normalization (2.4)--(3.3);
* the order-\(J\) Farey stationary ledger (3.5)--(3.10), including the
  corrected coefficient \(T/\sqrt{cJ}\), capacity
  \(C^{3/2}/\sqrt J\), and target-safe principal range
  \(C\leq J^{2/3}\);
* the exact reciprocity phase (1.5);
* the completion/\(B\)-process self-return (3.12)--(3.16);
* the completion diagonal (3.17)--(3.18), axial/gcd ledger
  (3.19)--(3.20), and resonance congruence (3.21).

Do not promote the sharp-cell or axial bounds: the stationary calculation
does not prove them. Do not import Pascadi, DFI, or Kuznetsov across the
failed coefficient, cusp, or zero-index seams.

The smallest next result is a uniform Farey-cell decomposition that proves
the sharp boundary and axial estimates, followed by a high-conductor
\(C>J^{2/3}\) estimate for (4.1) with the actual delta weight and all
level-four data. Any such estimate must recover the representation factor
in (1.4) before claiming the frozen \(X^{1/20}\) gain. No cone-edge, GAR,
\(M9\)-\(M1\), \(M9\), or final-exponent promotion is licensed.
