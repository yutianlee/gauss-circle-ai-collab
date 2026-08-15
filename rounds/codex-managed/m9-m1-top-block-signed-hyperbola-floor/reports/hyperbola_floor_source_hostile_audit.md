# Round 58 hostile/source audit: exact floor algebra, non-target Fourier closure

## 1. Result

The odd-character selector has an exact floor-compatible formula, and its
algebraic zero Fourier mode cancels exactly. This remains true with a
nonconstant summand only after retaining both Abel boundary terms and every
discrete-difference term.

This does not turn the actual high-shell sum into the Fourier transform of the
unweighted row count. On a two-point row the unweighted signed count is zero,
whereas the actual row is

\[
 \chi _4(q)\{W_h(q)-W_h(q+2)\},\qquad
 W_h(q)=\mathcal A_X(h,q)e(\sqrt{Xhq}),
\tag{58.H1}
\]

with all inherited stars included in \(W_h\). Its phase increment has size
\(\asymp hR\) and need not be small modulo one. Expanding only the floor count
therefore deletes an order-one part of an actual row.

A Vaaler expansion can be floor-compatible, but its positive Fejer residual
must remain. A crude uniform arithmetic estimate makes that residual
target-sized at truncation height \(M\ge R^{5/4}\); no smaller uniform height
follows from the pointwise Vaaler inequality alone. The nonzero modes retain a
floor-composed radial phase and the exact moving amplitude. Ordinary
frequency-spacing large sieve, Kloosterman-fraction, and rectangular
monomial-sum theorems do not give the required \(R^{1/2}\) bound.

This is a strict no-go for count-only, residual-free, or standard
modewise/black-box large-sieve implementations. It is not a signed
counterexample to \(P_J\ll X^\varepsilon\sqrt R\), and it does not exclude a
new theorem for the complete moving symbol.

## 2. Exact statement and hypotheses

Assume

\[
 Y=R^2\asymp\sqrt X,\qquad
 J=[A,B]\cap\mathbb Z\subset[cY,CY],\qquad B-A+1\le R,
\tag{58.H2}
\]

and \(R/4<h\le R/2\). Artificial endpoints \(A,B\) are full owners; only
equalities inherited from the angular or radial construction carry stars.
Put

\[
 a_h=\left\lceil {A\over h}\right\rceil,\qquad
 b_h=\left\lfloor {B\over h}\right\rfloor,\qquad
 C(m)=\sum_{1\le q\le m}\chi _4(q)\quad(m\ge0).
\tag{58.H3}
\]

Then

\[
 C(m)={1\over2}-{1\over2}\cos{\pi m\over2}
             +{1\over2}\sin{\pi m\over2},
\tag{58.H4}
\]

and the exact unweighted signed row selector is

\[
 \sigma_h=C\!\left(\left\lfloor {B\over h}\right\rfloor\right)
          -C\!\left(\left\lfloor {A-1\over h}\right\rfloor\right)
        =D(B/h)-D((A-1)/h),
\tag{58.H5}
\]

where

\[
 \begin{split}
 D(x)&=\left\lfloor{x+3\over4}\right\rfloor
       -\left\lfloor{x+1\over4}\right\rfloor\\
 &= {1\over2}-\psi_F\!\left({x+3\over4}\right)
                  +\psi_F\!\left({x+1\over4}\right).
 \end{split}
\tag{58.H6}
\]

Thus the \(1/2\) zero modes in the two endpoint copies of \(D\) cancel.
Equivalently,

\[
 \chi _4(q)={e(q/4)-e(3q/4)\over2i}
\tag{58.H7}
\]

has no character zero mode.

For the actual weighted row, write \(q=2r+1\), and put

\[
 r_0=\left\lfloor{a_h\over2}\right\rfloor,\qquad
 r_1=\left\lfloor{b_h-1\over2}\right\rfloor,\qquad
 G_h(r)=W_h(2r+1).
\tag{58.H8}
\]

Omit the row if \(r_0>r_1\). With

\[
 E(r)=\sum_{0\le j\le r}(-1)^j={1+(-1)^r\over2},
\tag{58.H9}
\]

finite Abel summation gives

\[
 \begin{split}
 \sum_{r=r_0}^{r_1}(-1)^rG_h(r)
  ={}&E(r_1)G_h(r_1)-E(r_0-1)G_h(r_0)\\
    &-\sum_{r=r_0}^{r_1-1}E(r)
      \{G_h(r+1)-G_h(r)\}.
 \end{split}
\tag{58.H10}
\]

The constant \(1/2\) part of \(E\) cancels identically in (58.H10), but the
alternating mode, both boundary values, and every actual difference remain.

Let \(V_M\) be Vaaler's degree-\(M\) approximation to \(\psi_F\), and let

\[
 \rho_M(t)={K_M(t)\over2(M+1)},\qquad
 K_M(t)={1\over M+1}
 \left({\sin\pi(M+1)t\over\sin\pi t}\right)^2.
\tag{58.H11}
\]

Then \(\lvert\psi_F(t)-V_M(t)\rvert\le\rho_M(t)\), with limiting value
\(\rho_M(n)=1/2\) at every integer. For \(N\asymp R^2\),
\(c_0\in\{1,3\}\), and \(R/4<h\le R/2\),

\[
 \sum_h \rho_M\!\left({N/h+c_0\over4}\right)
 \ll d(N)+{R^3\over(M+1)^2}.
\tag{58.H12}
\]

Consequently the four sawtooths in (58.H5)--(58.H6) have total residual

\[
 \ll_\varepsilon R^\varepsilon+{R^3\over(M+1)^2}
\tag{58.H13}
\]

before multiplication by the relevant bounded exact symbol. Thus
\(M\ge R^{5/4}\) is a crude sufficient height for an
\(O_\varepsilon(R^{1/2+\varepsilon})\) residual. Equation (58.H13) says
nothing about the nonzero Fourier modes.

## 3. Proof or derivation

The partial sums of \(\chi_4\) have values \(0,1,1,0\) on
\(m\equiv0,1,2,3\pmod4\), proving (58.H4). Since

\[
 \left\lceil {A\over h}\right\rceil-1
   =\left\lfloor {A-1\over h}\right\rfloor
\tag{58.H14}
\]

for integral \(A,h\), subtracting the two character partial sums proves
(58.H5). Counting the residue classes \(1\) and \(3\pmod4\) up to \(x\)
gives the first line of (58.H6); substituting
\(\lfloor t\rfloor=t-\psi_F(t)-1/2\) gives the second. The \(A-1\)
argument fully owns \(hq=A\), and the upper floor fully owns \(hq=B\).

For (58.H10), use \((-1)^r=E(r)-E(r-1)\). The constant part of \(E\)
contributes

\[
 {G_h(r_1)-G_h(r_0)\over2}
 -{1\over2}\sum_{r=r_0}^{r_1-1}
        \{G_h(r+1)-G_h(r)\}=0.
\tag{58.H15}
\]

This proves exact zero-mode cancellation, including singleton rows. Deleting
either Abel boundary creates a false zero-mode term. If a row has the two odd
points \(q,q+2\), (58.H10) is precisely (58.H1). Even on an amplitude
plateau its phase contains

\[
 1-e(\Theta_h(q)),\qquad
 \Theta_h(q)={2\sqrt{Xh}\over\sqrt{q+2}+\sqrt q}\asymp hR,
\tag{58.H16}
\]

whose fractional part is uncontrolled. Hence \(\sigma_h=0\) does not make
the actual row small.

For (58.H12), write

\[
 t={N/h+c_0\over4}={N+c_0h\over4h}.
\tag{58.H17}
\]

If \(t\in\mathbb Z\), then \(h\mid N\), so at most \(d(N)\) such \(h\)
occur and each contributes \(1/2\). Otherwise the numerator of the distance
to the nearest integer is nonzero, and

\[
 \lVert t\rVert\ge {1\over4h}\gg {1\over R}.
\tag{58.H18}
\]

The closed form (58.H11) and
\(\lvert\sin\pi t\rvert\gg\lVert t\rVert\) give

\[
 \rho_M(t)\ll{1\over(M+1)^2\lVert t\rVert^2}
             \ll {R^2\over(M+1)^2}.
\tag{58.H19}
\]

Summing over \(O(R)\) high-shell values proves (58.H12)--(58.H13). This
records the discontinuities rather than assigning them half ownership. The
Fejer residual itself has positive zero Fourier coefficient
\(1/(2(M+1))\); it is not erased by the algebraic character zero-mode
cancellation.

A nonzero endpoint harmonic is

\[
 e\!\left({mN\over4h}+{mc_0\over4}\right).
\tag{58.H20}
\]

When it multiplies an actual upper endpoint, let \(q_N(h)\) be the largest
admissible odd integer below \(N/h\), and put
\(r_N(h)=N-hq_N(h)\in[0,2h)\). The combined phase is

\[
 \Phi_{N,m}(h)=\sqrt{X\{N-r_N(h)\}}+{mN\over4h}+{mc_0\over4},
\tag{58.H21}
\]

with an analogous lower-endpoint formula. The amplitude is still
\(\mathcal A_X(h,q_N(h))\), including height floors, profiles, the one-sided
hard top, and inherited stars. The remainder \(r_N(h)\) jumps on the
hyperbola-floor scale, so (58.H21) is not the smooth phase \(mN/(4h)\).

There is no uniform frequency-separation rescue. Take \(X=K^4\),
\(N=K^2\), \(R=K\), and \(K=165u\) with \(u\) odd. The two actual odd
divisor incidences

\[
 (h_1,q_1)=(55u,495u),\qquad
 (h_2,q_2)=(75u,363u)
\tag{58.H22}
\]

both lie in \(R/4<h\le R/2\), and

\[
 {N\over4h_1}-{N\over4h_2}={q_1-q_2\over4}=33u\in\mathbb Z.
\tag{58.H23}
\]

Thus reciprocal endpoint frequencies collide modulo one on the actual odd
lattice, while \(e(\sqrt{XN})=e(K^3)=1\). A separated-frequency large sieve
cannot be invoked without grouping collisions and proving a new
multiplicity/correlation estimate. Even if a remaining sector had spacing
\(\delta\asymp R^{-1}\), the standard estimate

\[
 \sum_{m\le M}\left|\sum_{h\asymp R}a_he(mx_h)\right|^2
 \ll (M+\delta^{-1})\sum_h|a_h|^2
\tag{58.H24}
\]

followed by Cauchy against coefficients \(O(1/m)\) has capacity \(R\), not
\(\sqrt R\), for \(M\lesssim R\), and worse for the crude
\(M\ge R^{5/4}\) truncation. This is a method-capacity statement, not a
lower bound for \(P_J\).

The primary-source audit yields no black-box closure:

- [Vaaler, Some extremal functions in Fourier analysis, Bull. AMS 12
  (1985), 183--216](https://www.ams.org/journals/bull/1985-12-02/S0273-0979-1985-15349-2/)
  supplies the finite approximation and positive Fejer residual in
  (58.H11). It supplies no estimate for the sampled \(h\)-sum, and its
  residual must be kept at integer discontinuities.
- [Robert--Sargos, Three-dimensional exponential sums with monomials,
  J. reine angew. Math. 591 (2006), 1--20](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf),
  Theorem 1, treats rectangular dyadic boxes and one fixed product-monomial
  phase with fixed nondegenerate exponents. Absorbing the strip and actual
  symbol into their arbitrary joint coefficient and taking their third
  length \(M_0=1\) leaves an upper-bound term
  \((HN)^{1+\varepsilon}\asymp R^{2+\varepsilon}\). Compressing to the
  sparse strip instead gives (58.H21), outside the monomial hypothesis.
  Adding the Fourier index creates a sum of phases, not one product monomial.
- [Duke--Friedlander--Iwaniec, Bilinear forms with Kloosterman fractions,
  Invent. Math. 128 (1997), 23--43](https://www.math.ucla.edu/~wdduke/preprints/bilinear.pdf),
  Theorems 1--3 and the smooth-weight corollary concern
  \(e(a\overline m/n)\) on coprime dyadic rectangles; their weighted version
  requires derivative bounds through order two. Equation (58.H20) is an
  ordinary real reciprocal, not a modular inverse, and (58.H21) with the
  exact profile/floor/star symbol is not a smooth factorizable weight.

## 4. First doubtful or unproved step

The first invalid step is replacing the actual row by the unweighted floor
selector \(\sigma_h\) times one representative value of \(W_h\). It fails on
every two-point row: \(\sigma_h=0\), while (58.H1) need not be small. Exact
Abel summation repairs the identity only by restoring the boundary and
discrete-difference terms whose size is the Round-57 obstruction.

After that repair, the first unproved analytic step is a signed estimate for
the complete family (58.H21), with moving endpoint, actual amplitude, and
Fejer residual. No first-derivative gap, separated reciprocal frequencies,
modewise square-root cancellation, or theorem uniform in this moving symbol
has been proved. Any assertion of an \(O(R/M)\) truncation error additionally
needs an averaged Fejer-kernel spacing lemma; it does not follow from
Vaaler's pointwise inequality.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| **exact_floor_selector** | **Pass, narrowly.** Equations (58.H5)--(58.H6) are exact and use \(A-1\), so both artificial window edges are fully owned. They describe the unweighted signed count, not the actual weighted row. |
| **zero_mode** | **Pass with warning.** The character/Abel zero mode cancels by (58.H15). The positive Fejer-residual zero coefficient does not disappear. |
| **fourier_truncation** | **No target closure.** The residual is (58.H13); \(M\ge R^{5/4}\) is a crude sufficient height. No source controls the nonzero modes at target scale. |
| **character_projector** | **Pass.** Equation (58.H7), or the odd-index alternation in (58.H9), is exact. Splitting residues and taking absolute values is not licensed. |
| **cross_h_phase** | **Fail for the proposed smooth model.** The actual phase is (58.H21), containing discontinuous \(r_N(h)\); (58.H23) gives an exact frequency collision. |
| **actual_amplitude** | **Retained, unresolved.** It is evaluated at the floor-selected odd endpoint and includes every height floor, profile, hard-top jump, and local star. No audited theorem accepts it. |
| **endpoint_and_stars** | **Pass.** \(A,B\) are full owners; \(\psi_F(n)=-1/2\) and residual value \(1/2\) implement the floor jump. Only inherited angular/radial equalities remain starred. |
| **perfect_fourth_power** | **Hostile pass.** At \(X=K^4,N=K^2\), the point radial phase is \(1\); (58.H22)--(58.H23) falsify universal spacing or phase-gap premises on actual odd incidences. The Round-57 star-free plateau family retains \(\gg R\) unmatched absolute mass. |
| **target_ledger** | **Fail.** Trivial actual mass is \(R\), target is \(\sqrt R\). The floor identity saves no power; crude residual control creates many modes; standard large sieve has \(R\)-capacity; the audited monomial theorem gives a full-box bound and the Kloosterman theorem is inapplicable. |
| **downstream_scope** | **Pass.** Nothing here treats \((\log X)^B<h\le R/4\), alpha connectors, height limits, GAR, M9-M1, M9, or the final exponent. |

For the point-window control, (58.H5) gives exactly

\[
 P_{\{N\}}=e(\sqrt{XN})
 \sum_{\substack{h\mid N,\ R/4<h\le R/2\\N/h\equiv1\pmod 2}}^{*}
 \chi_4(N/h)\mathcal A_X(h,N/h).
\tag{58.H25}
\]

There is no artificial half weight. At \(X=K^4,N=K^2\), its common phase is
\(1\). Its divisor-size support makes it a consistency control, not a large
signed counterexample.

## 6. Dependencies and exact artifacts used

The audit used exactly the permitted repository context:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-top-block-signed-hyperbola-floor/derivation_packet.md;
- rounds/codex-managed/m9-m1-top-block-signed-adjacent-odd-pairing/synthesis.md;
- rounds/codex-managed/m9-m1-top-block-intermediate-h-resonance/synthesis.md.

The three primary sources linked in Section 3 were consulted only for the
stated theorem shapes and hypothesis audit. No other Round-58 report or
candidate was read. No numerical experiment was used; the allocation was
100% analytical/algebraic.

## 7. Recommended state effect

**Revise.** Promote, at most, the narrow exact floor identity
(58.H5)--(58.H6), exact Abel zero-mode cancellation (58.H10)--(58.H15), the
explicit residual ledger (58.H12)--(58.H13), and the scoped no-go for
count-only, residual-free, standard separated-frequency, or presently cited
black-box source arguments. Reject any claim that the unweighted floor count
is the actual row, that the Fejer residual cancels with the character zero
mode, or that an existing monomial/Kloosterman theorem proves the high shell.

Retain the signed high-shell estimate and every downstream obligation open. A
viable successor theorem must estimate the full signed moving symbol
(58.H21) before absolute values, explicitly allowing floor discontinuities,
frequency collisions, actual profiles, and inherited stars.

### Conductor-requested seam addendum: certification of the stronger Fejer-residual sum

This addendum audits only Section 3.3, equations (3.7)--(3.10a), of the
Round-58 discovery report. It supersedes the assessment in Sections 1, 2, 4,
and 5 above that an \(O(R/T)\) residual estimate was still unproved. The
earlier bound (58.H12)--(58.H13) remains correct but is strictly cruder in the
relevant range.

The strengthened kernel lemma is valid with the following hypotheses made
explicit. Let \(N,c,d\in\mathbb Z\), let \(d\) be fixed and nonzero (in the
application \(d\in\{2,4\}\)), let \(N\asymp R^2\), and let
\(\mathcal I_H\) be any integer interval contained in \([H,2H]\), with
\(H\ll R\) and \(N\gg H\). For \(T\ge1\), set

\[
 t_h={N+ch\over dh}.
\tag{58.S1}
\]

If

\[
 \kappa_T(t)\ll\min\left(1,{1\over T^2\lVert t\rVert^2}\right),
\tag{58.S2}
\]

with its exact limiting value at integers, then

\[
 \boxed{\displaystyle
 \sum_{h\in\mathcal I_H}\kappa_T(t_h)
 \ll_\varepsilon X^\varepsilon\left({H\over T}+1\right).}
\tag{58.S3}
\]

In particular, \(H\asymp R\) gives the claimed
\(X^\varepsilon(R/T+1)\) bound.

Indeed, if \(0<\delta\le1/2\) and
\(\lVert t_h\rVert\le\delta\), choose a nearest integer \(k\) and define

\[
 s=N-(dk-c)h.
\tag{58.S4}
\]

The integrality of \(N,c,d,h,k\) is essential here: \(s\in\mathbb Z\),
\(\lvert s\rvert\le |d|h\delta\ll\delta H\), and
\(h\mid N-s\). Since \(N-s\asymp N>0\), the divisor bound, uniformly for
each possible \(s\), gives

\[
 \#\{h\in\mathcal I_H:\lVert t_h\rVert\le\delta\}
 \ll_\varepsilon X^\varepsilon(\delta H+1).
\tag{58.S5}
\]

Exact integers correspond to \(s=0\). They satisfy \(h\mid N\), so their
number is \(O_\varepsilon(X^\varepsilon)\); the \(+1\) in (58.S5) owns
them without changing their residual value or assigning an artificial star.

For \(T\ge2\), the range \(\lVert t_h\rVert\le1/T\) contributes
\(O_\varepsilon(X^\varepsilon(H/T+1))\). On

\[
 {2^j\over T}<\lVert t_h\rVert\le {2^{j+1}\over T},
\tag{58.S6}
\]

up to distance \(1/2\), (58.S2) is \(O(2^{-2j})\), while (58.S5) counts
\(O_\varepsilon(X^\varepsilon(2^jH/T+1))\) points. Summing the geometric
series proves (58.S3). For \(1\le T<2\), the trivial \(O(H)\) bound is
already (58.S3). The same proof works separately on every dyadic
\(h\)-shell; summing \(O(\log X)\) such shells only changes the
\(X^\varepsilon\) factor.

This strictly improves the earlier

\[
 X^\varepsilon\left(1+{R^3\over T^2}\right)
\tag{58.S7}
\]

ledger whenever the power terms are relevant and \(T<R^2\). Most
importantly, a target-sized residual now needs only
\(T\ge R^{1/2}\), whereas (58.S7) required \(T\ge R^{5/4}\). At
\(T=R^{5/4}\), (58.S3) is already \(O_\varepsilon(X^\varepsilon)\).
For very large \(T\), both estimates are governed by the unavoidable
exact-integer \(+1\) term, so “strict” refers to the nonconstant power
ledger rather than to every numerical \(T\).

Pointwise bounded actual-symbol multiplication preserves (58.S3). Precisely,
if \(\lvert B_h\rvert\le C X^\eta\), then positivity gives

\[
 \sum_{h\in\mathcal I_H}|B_h|\kappa_T(t_h)
 \ll_{\varepsilon,C}
 X^{\varepsilon+\eta}\left({H\over T}+1\right).
\tag{58.S8}
\]

Thus a bounded finite collection of the actual remainder multipliers,
including hard-profile values and inherited star factors in \([0,1]\), is
harmless; no smoothness or BV assertion is needed for this multiplication.
Equation (3.10a) is therefore certified provided the multipliers appearing
in its exact remainder are pointwise uniformly bounded and there are only
\(O(1)\) residual summands per \(h\), as asserted in the audited section.
This seam does not independently verify any multiplier derivative formula
outside the permitted excerpt.

The improvement removes the truncation residual as the obstruction at
\(T\asymp\sqrt R\). It does not estimate the nonzero Fourier modes, repair a
count-only replacement of the weighted row, or prove the signed high-shell
bound. The source/mode-capacity verdict of the main report remains unchanged
with that narrower qualification.
