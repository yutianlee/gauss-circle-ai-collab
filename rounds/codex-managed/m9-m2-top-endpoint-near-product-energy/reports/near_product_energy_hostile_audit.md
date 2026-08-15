# Round 75 hostile/source audit: near-product reciprocal energy

## 1. Result

The candidate (75.7)--(75.16) is **not promotable as written**.  The
quarter-shift algebra, the odd dual index, the Gaussian units, the
one-sided sign of the active second Poisson frequency, and the scale
\(LJ\) are correct.  The two failures are more precise:

1. In (75.8), “evaluating the complete symbol at \(t_0\)” describes only
   the leading quadratic stationary-phase symbol.  The next term is
   generally nonzero and is only \(J^{-1}\) smaller.  Consequently the
   displayed remainder \(O_A(L^{3/2}X^{-A})\) in (75.7) does not follow
   from (75.8).  The additive \(B=\lceil\sqrt L\rceil\) collars do permit
   a uniform all-orders repair: either retain the exact normalized
   Gaussian integral in the moving kernel, or retain sufficiently many
   stationary coefficients.  A leading-symbol formula has a
   target-safe error, but not a super-polynomial error.
2. The \(LJ\) diagonal does not follow from the naive identity
   \(\sum_k|\widehat F(k)|^2=\int_{\mathbb R}|F|^2\).  The exact identity
   is Parseval for the periodization of \(F\).  The desired bound does
   follow, without a power loss, once one proves the moving-symbol
   envelope
   \[
     |\partial_l^rF_{\tau,j}(l)|
       \ll_{A,r}X^\varepsilon L^r
       (1+L|l-X/j|)^{-A}.                 \tag{1.1}
   \]
   That envelope is compatible with the repaired all-orders collar
   calculus, but it is asserted rather than proved in the packet.

There is also a sharp adjoint-return no-go.  The actual Fourier mass in
(75.13) is on the **negative** modes \(k=-m\), \(m\asymp L\).  A
quarter-shift B-process in the high \(j\)-leg gives
\[
 S_{-m}=e(-1/8)\Bigl(\frac JL\Bigr)^{1/2}R_m^\sharp
       +\text{target-safe all-orders error},                  \tag{1.2}
\]
where
\[
 R_m^\sharp=
 \sum_{\substack{m\le r\le4m\\r\ \mathrm{odd}}}
   \chi_4(r)a^\sharp(r,m)e(\sqrt{Xrm}),                       \tag{1.3}
\]
and \(a^\sharp\) is the adjoint actual collar/layer symbol.  With the
exact Gaussian symbol, \(a^\sharp=a\) modulo arbitrarily small
microlocal errors; with only the leading symbol,
\(a^\sharp=a+O_{\mathcal S}(J^{-1})\).  Hence the repaired form of
(75.16) is, at the only critical scale, precisely
\[
 \sum_{m\asymp L}|R_m^\sharp|^2\ll_\varepsilon L^2X^\varepsilon.
                                                               \tag{1.4}
\]
This is the transposed-row Cauchy energy of the original cone.  It is a
valid smaller survivor, not a new saving.  Its signed off-diagonal is
open, and none of the audited primary theorems supplies it.

## 2. Exact statement and hypotheses

Assume \(X\) is sufficiently large and put
\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad q_X=X/y^2,
 \qquad H=\lfloor yX^{-1/4}\rfloor.
\]
Let \(1\le L\le H\) be dyadic and
\(B=\lceil\sqrt L\rceil\).  The original amplitude is exactly (75.1),
with its actual dyadic cutoff, Vaaler factor, profile \(W\), ceiling,
and odd \(h\).  Remove the two lattice strips
\[
 0\le m-\lceil h/4\rceil\le2B,
 \qquad 0\le h-m\le2B.                                      \tag{2.1}
\]
They contain \(O(LB)=O(L^{3/2})\) bounded summands.  On the complement,
assume a one-count smooth partition \(\sum_\tau C_\tau=1\), of bounded
overlap, whose transition at additive distance \(D\) has angular
derivatives \(O_r((L/D)^r)\); here \(B\le D\ll L\), in dyadic layers.

Under these hypotheses the following corrected reduction is valid.

**Corrected moving-symbol lemma.**  There are exact normalized kernels
\(\mathcal K^{\mathrm{ex}}_{\tau,l}\), obtained by retaining the full
Gaussian integral after \(m=xt^2\), for which
\[
 \mathcal T_{L,\mathrm{int}}
 =e(1/8)L^{3/2}J^{-1/2}\mathcal D_L^{\mathrm{ex}}
   +O_A(L^{3/2}X^{-A}),                                      \tag{2.2}
\]
after all nonstationary aliases are included and then truncated.  The
same assertion holds with a finite kernel containing the first \(N\)
stationary coefficients, with error
\[
 O_{N,\varepsilon}(L^{3/2}J^{1/2-N}X^\varepsilon).            \tag{2.3}
\]
In particular \(N\ge2A+2\) gives (2.2).  If only the value at \(t_0\)
is retained, the rigorously available remainder is of the order
\(L^{3/2}J^{-1/2}X^\varepsilon\), which is target-safe but is not the
remainder claimed in (75.7).

For the repaired kernel define \(F_{\tau,j}\), \(\widehat F_{\tau,j}\),
and \(b_{\tau,j,k}\) exactly as in (75.10)--(75.13).  If (1.1) and the
analogous finite-overlap bounds in \(\tau\) are established, then
\[
 b_{\tau,j,k}\ll_{A}X^\varepsilon(1+|k|/L)^{-A},\qquad
 \sum_{\tau,j,k}|b_{\tau,j,k}|^2
       \ll_\varepsilon LJX^\varepsilon.                       \tag{2.4}
\]
The \(j=j'\) part of the energy is therefore \(O(LJX^\varepsilon)\).
No assertion here bounds the signed \(j\ne j'\) part.

Finally, let
\[
 R_m=
 \sum_{\substack{r\asymp L,\ r\ \mathrm{odd}\\
                   \lceil r/4\rceil\le m\le r}}
 \chi_4(r)a(r,m)e(\sqrt{Xrm}).                                \tag{2.5}
\]
Then the direct, exact transposed-row reduction is
\[
 |\mathcal T_L|^2
   \ll L\sum_{m\asymp L}|R_m|^2.                             \tag{2.6}
\]
Thus \(\sum_m|R_m|^2\ll L^2X^\varepsilon\) is sufficient for the cone
target.  Equations (1.2)--(1.4) show that the corrected reciprocal
energy returns to this same sufficient problem, up to the extracted
boundary and target-safe stationary corrections.

## 3. Proof or derivation

**Ceiling, \(q_X\), and collars.**  Since
\(q_X-1=O(J^{-1})\) and \(h\le H\ll J^{1/2}\),
\((q_X-1)h/4<1/4\) for large \(X\).  For odd \(h\), whose fractional
part modulo four is \(1/4\) or \(3/4\), this gives
\[
 \lceil q_Xh/4\rceil=\lceil h/4\rceil.                        \tag{3.1}
\]
Thus the stated ceiling is compatible with the actual stationary point,
and at that point
\[
 W\!\left(\frac{\sqrt{q_X}}{2t_0}\right)=W(l/y)              \tag{3.2}
\]
exactly.  The upper row maps to \(l=J/2\); flatness of \(W\) at
\(1/2\), together with the extracted upper strip, prevents an omitted
half-Fresnel functional.  An additive collar has
\(d_-(x,t)=x(t^2-1/4)\) or \(d_+(x,t)=x(1-t^2)\).  On its narrowest
transition,
\[
 \partial_t^r C(d_\pm/B)\ll_r(L/B)^r\ll_rL^{r/2}.             \tag{3.3}
\]
The dyadic layers have smaller derivative costs, and their one-count
sum is geometric apart from an absorbable logarithm.  This is why the
collar may depend on both \(x\) and \(t\), but cannot be replaced by a
fixed angular cutoff.

**Quarter shift and the first Gaussian.**  Expand
\[
 \chi_4(h)=\sum_{\rho=\pm1}\frac{\rho}{2i}e(\rho h/4).
\]
After two-dimensional Poisson, put \(m=xt^2\).  For dual integers
\(u,l\),
\[
 \phi=x\{Jt+\rho/4-u-lt^2\},\quad
 t_0=\frac J{2l},\quad j=4u-\rho,                             \tag{3.4}
\]
and
\[
 \phi=x\frac{X-jl}{4l}-xl(t-t_0)^2.                          \tag{3.5}
\]
Here \(j\) is odd, \(j\equiv-\rho\pmod4\), hence
\(\rho=-\chi_4(j)\).  With the convention \(e(z)=e^{2\pi iz}\),
\[
 \int_{\mathbb R}e(-xlv^2)\,dv
 =\frac{e(-1/8)}{\sqrt{2xl}}.                                \tag{3.6}
\]
The Jacobian is \(dm=2xt\,dt\).  Combining it with
\(L^{3/2}x^{-3/2}t^{-3/2}\), (3.6), and \(t_0=J/(2l)\) gives
\(2L^{3/2}J^{-1/2}dx/x\).  Finally
\[
 \frac{\rho}{2i}\,2e(-1/8)=e(1/8)\chi_4(j),                 \tag{3.7}
\]
which proves the sign and constant in (2.2).  The external physical
factor remains the already accepted
\(-2\pi^{-1}e(1/8)X^{1/4}L^{-3/2}\), counted once; the negative original
frequency is its conjugate.

**Why the leading kernel is not all-orders.**  If \(g_{x,l}(t)\) is the
complete collar/layer amplitude, quadratic stationary phase gives
\[
 \int g_{x,l}(t)e(-xl(t-t_0)^2)dt
 =\frac{e(-1/8)}{\sqrt{2xl}}
   \sum_{\nu<N}c_\nu(xl)^{-\nu}g_{x,l}^{(2\nu)}(t_0)
   +R_N.                                                      \tag{3.8}
\]
By (3.3),
\((xl)^{-\nu}g^{(2\nu)}(t_0)\ll J^{-\nu}\).  The
\(\nu=1\) term is generally nonzero.  Therefore evaluation at \(t_0\)
alone cannot have an \(O_A(X^{-A})\) remainder.  On the other hand,
the distance from a discarded stationary point to the collar is at
least \(B/L\), so the phase derivative is \(\gg J\sqrt L\); integration
by parts has the same effective gain \(J^{-1}\).  There are
\(O(JX^\varepsilon)\) effective near-product aliases after radial
decay.  Summing (3.8) therefore gives (2.3).  This proves both the
failure of the stated leading-only error and the all-orders repair.

**Poisson measure and the true Parseval identity.**  With
\(\widehat F(k)=\int F(\lambda)e(-k\lambda)d\lambda\), ordinary Poisson
summation gives exactly
\[
 \mathcal D_L=L^{-1}\sum_kS_k,qquad
 S_k=\sum_{\tau,j}\chi_4(j)b_{\tau,j,k}e(-kX/j).              \tag{3.9}
\]
There is no missing factor two or odd-lattice density in this
uncharactered \(l\)-leg.  Put \(F_j=\sum_\tau F_{\tau,j}\).  Since
\(b_{j,k}e(-kX/j)=L\widehat F_j(k)\),
\[
 \sum_k|S_k|^2
 =L^2\int_0^1\left|
      \sum_{n\in\mathbb Z}\sum_j\chi_4(j)F_j(x+n)
    \right|^2dx.                                              \tag{3.10}
\]
This is periodized Parseval.  From (1.1),
\[
 \int_0^1\left|\sum_nF_j(x+n)\right|^2dx\ll L^{-1}X^\varepsilon,
                                                                    \tag{3.11}
\]
including \(L=1\).  Summing over \(j\), and using finite layer overlap
or Cauchy with \(O(\log L)\) absorbed by \(X^\varepsilon\), proves the
\(LJ\) diagonal.  Repeated integration by parts in \(l\) proves the
\(k\)-tail in (2.4).  It does not bound the off-diagonal in (3.10).

**Active sign and adjoint B-process.**  The radial variable is
\(z=x/L>0\).  In the Fourier transform in \(l\), the phase is
\[
 \frac{LzX}{4l}-kl.
\]
It has a stationary point only when \(k=-m<0\); the actual symbol then
forces \(m\asymp L\).  The modes \(k\ge0\), and negative modes away
from \(-L\), are nonstationary (bounded \(L\) being separately safe).
For \(k=-m\), expand \(\chi_4(j)\) and Poisson-sum the \(j\)-leg.  The
phase is
\[
 \frac{mX}{x}+\frac{\rho x}{4}-nx,qquad
 r=\rho-4n>0,qquad x_*=2\sqrt{mX/r}.                          \tag{3.12}
\]
Thus \(r\) is odd, \(r\equiv\rho\pmod4\), and
\(\chi_4(r)=\rho\).  At the saddle,
\[
 \phi(x_*)=\sqrt{Xmr},\qquad
 \phi''(x_*)>0,qquad
 |\phi''(x_*)|^{-1/2}=2(mX)^{1/4}r^{-3/4}.                    \tag{3.13}
\]
The positive Gaussian contributes \(e(1/8)\), and
\[
 \frac{\rho}{2i}\,2e(1/8)=e(-1/8)\chi_4(r).                 \tag{3.14}
\]
Moreover, the preceding \(l\)- and radial stationary calculations give
\[
 b_{j,-m}=\frac Lm A_0\!\left(\frac{4Xm}{j^2},
                              \frac{j}{2J}\right)
             +\text{all-orders corrections},                 \tag{3.15}
\]
where \(A_0\) is exactly the normalized collar/layer/profile symbol.
Substitution of (3.15) into (3.13) proves (1.2):
\[
 (mX)^{1/4}r^{-3/4}\frac Lm
 =\Bigl(\frac JL\Bigr)^{1/2}
    L^{3/2}(rm)^{-3/4}.                                       \tag{3.16}
\]
Finally, \(J<x_*<2J\) is equivalent to
\[
 m<r<4m,                                                       \tag{3.17}
\]
which is precisely the transposed original cone
\(\lceil r/4\rceil\le m\le r\).  The character, profile
\(W(\sqrt{q_Xr/(4m)})\), Vaaler factor, and both collar images return
with it.  The factors \(e(1/8)\) from (2.2) and \(e(-1/8)\) from
(1.2) cancel.  Hence the high-leg B-process is an adjoint return, and
(75.16) is (1.4), not a fresh large-sieve gain.

**Off-diagonal and capacity.**  Expanding the energy leaves
\[
 \sum_{j\ne j'}\chi_4(j)\chi_4(j')
 \sum_{\tau,\tau',k}b_{\tau,j,k}\overline{b_{\tau',j',k}}
 e\!\left(kX(1/j'-1/j)\right),                                \tag{3.18}
\]
which is unproved.  The bounds (2.4) alone cannot imply it: for one
allowed \(k_0\), artificial coefficients
\(b_{j,k_0}=\chi_4(j)e(k_0X/j)\) make \(|S_{k_0}|\asymp J\) while still
obeying the coefficient-size budget.  Exact primal square resonances
have \(O_\varepsilon(L^{1+\varepsilon})\) capacity, exact products
\(jl=X\) are divisor-bounded when they exist, and for \(X=R^4\) the
anti-diagonal window has \(O(\sqrt{J/L})\) points.  These controls are
target-safe, but they do not estimate (3.18).

**Primary-source applicability.**  The following checks use the primary
statements, not a methodological analogy.

- [Kowalski--Robert--Wu, Proposition 5](https://ems.press/content/serial-article-files/38194)
  treats separable bounded coefficient sequences in the monomial bilinear form
  \(e(\mathcal X m^\alpha n^\beta/(M^\alpha N^\beta))\), for fixed
  \(\alpha,\beta\notin\{0,1\}\).  After lawful Mellin separation of the
  actual interior ratio symbol, \(M=N=L\),
  \(\alpha=\beta=1/2\), and \(\mathcal X=JL\) give
  \[
   J^{1/8}L^{13/8}+L^{3/2}+L^{7/4}+J^{-1/2}L^{3/2}.           \tag{3.19}
  \]
  This is the exact applicable import already identified in Round 74;
  it never reaches \(L^{3/2}\), and where it improves on \(L^2\) it is
  dominated by the inherited two-shift envelope.
- [Robert--Sargos, Theorem 2](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf)
  counts quadruples satisfying
  \(|m_1^\alpha+m_2^\alpha-m_3^\alpha-m_4^\alpha|le
  \delta M^\alpha\) and proves
  \(O_\varepsilon(M^{2+\varepsilon}+\delta M^{4+\varepsilon})\).
  It is the root-spacing input behind (3.19); it has no prescribed
  centre \(X\), mod-four sign, or moving \((j,k)\)-symbol, so it does not
  prove (3.18) or (1.4).
- The separated-point large sieve in
  [Bombieri, *On the large sieve*](https://doi.org/10.1112/S0025579300005313)
  gives a constant of the form \(K+\delta^{-1}\).  There are \(\asymp J\)
  points \(X/j\pmod1\), so even the pigeonhole upper bound on their
  minimum spacing is \(\delta\ll J^{-1}\); the resulting coefficient-blind
  scale is at least \(J^2\), not \(LJ\) for \(L\le J^{1/2}\).  The theorem
  also discards the character/symbol correlation.
- [Huxley--Watt](https://doi.org/10.1112/plms/s3-57.1.1) gives, under its
  smooth derivative hypotheses, a row bound
  \(J^{1/2}(mJ)^{9/56}\log(mJ)\) for the reciprocal phase after splitting
  the fixed mod-four classes and applying partial summation.  Summing
  squares gives at best
  \(LJ(LJ)^{9/28}X^\varepsilon\), with a positive conductor loss.
- [Ivi\'c](https://www.numdam.org/item/10.5802/jtnb.669.pdf) estimates an
  integral over the centre,
  \(\int_X^{2X}(\Delta_k(x+h)-\Delta_k(x))^2dx\), for the full divisor
  coefficients.  It is neither pointwise at the prescribed \(X\) nor a
  theorem for the truncated mod-four moving symbol.
- [Bettin--Chandee](https://arxiv.org/abs/1502.00769) treats trilinear
  Kloosterman fractions \(e(a\overline m/n)\), with modular inverses and
  the associated coprimality/sequence norms.  The phase here is the
  ordinary real reciprocal \(e(-kX/j)\).  There is no lawful parameter
  substitution turning one into the other.
- [Deshouillers--Iwaniec](https://doi.org/10.1007/BF01390728) applies a
  Kuznetsov/spectral large sieve to complete Kloosterman sums averaged in
  their modulus and spectral data.  The fixed-centre band (3.18) contains
  no complete Kloosterman family or such average.  Completion or a
  phase-matched spectral transform is an additional transformation and,
  with the actual symbol, returns to the same short row problem rather
  than proving it.

Thus the source audit is negative for the target.  It does not claim
that no future actual-symbol theorem is possible; it says that none of
the named primary statements has the required hypotheses and conclusion.

## 4. First doubtful or unproved step

In the packet's order, the first doubtful step is the jump from the
leading evaluation at \(t_0\) in (75.8) to the super-polynomial identity
(75.7).  Equation (3.8) exhibits the omitted \(J^{-1}\) correction.
This seam is repairable and target-safe, but it must be repaired before
the moving wavelet can be called exact.

After that repair, the first genuinely power-saving unproved step is
the signed off-diagonal (3.18), equivalently the transposed-row estimate
\[
 \sum_{m\asymp L}\left|
  \sum_{\substack{m\le r\le4m\\r\ \mathrm{odd}}}
   \chi_4(r)a(r,m)e(\sqrt{Xrm})
 \right|^2
 \stackrel{?}{\ll}_\varepsilon L^2X^\varepsilon.             \tag{4.1}
\]
The diagonal in (4.1) is exactly of order \(L^2\).  No audited argument
controls its signed off-diagonal.  A second high-character B-process
proves no gain: equations (3.12)--(3.17) show that it is the adjoint map
back to (4.1).

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| External normalization | **Pass.** The accepted physical factor is counted once; the negative original frequency is the conjugate. The internal \(e(1/8)\) is independently forced by (3.7). |
| Hard and flat boundary collars | **Pass only after extraction.** Both strips have \(O(LB)=O(L^{3/2})\) capacity. The additive collars give the derivative scale (3.3); a fixed angular substitute is invalid. Flatness at \(W(1/2)\) removes an upper half-Fresnel term. |
| Actual \(q_X\) and layer ownership | **Pass.** Equation (3.1) keeps the exact ceiling and (3.2) gives \(W(l/y)\). A bounded-overlap, one-count dyadic partition has only geometric derivative cost and an absorbable \(\log L\). |
| Quarter shift and Gaussian constant | **Pass.** \(j=4u-\rho\) is odd, \(\rho=-\chi_4(j)\), the Jacobian is \(2xt\), and the first Gaussian gives \(e(1/8)\chi_4(j)\). |
| Moving \(l\)-symbol | **Fail as stated / repairable.** Evaluation at \(t_0\) omits algebraic corrections. The exact normalized Gaussian kernel or an \(N\)-term symbol package repairs it uniformly. |
| Alias and layer errors | **Pass for the repaired symbol.** The narrowest collar gives an effective \(J^{-1}\) integration-by-parts gain; \(N\) terms give (2.3). The packet does not contain this proof. |
| Poisson measure | **Pass.** With the stated Fourier convention, (3.9) has exactly the factor \(1/L\); the uncharactered leg has no half-density. |
| Parseval diagonal | **Pass conditionally, with a correction.** Periodized Parseval, not continuous Parseval, is exact. Under (1.1) it gives \(LJX^\varepsilon\), including all layer cross-terms. |
| Signed off-diagonal | **Fail/open.** Equation (3.18), equivalently (4.1), is not bounded. |
| Character self-return | **Pass as an obstruction.** The active modes are \(k=-m\asymp-L\); the second Gaussian is \(e(-1/8)\), the dual odd variable satisfies \(m\le r\le4m\), and the actual character/profile/collars return. |
| Perfect powers and exact products | **Pass as capacity only.** Primal exact-square fibres are \(O_\varepsilon(L^{1+\varepsilon})\), exact \(jl=X\) fibres are divisor-bounded, and the fourth-power anti-diagonal has \(O(\sqrt{J/L})\) points. None proves cancellation. |
| Adversarial weights | **Pass as rejection.** A phase-conjugating artificial \(b\) obeys the size budget but makes one \(S_k\) of size \(J\); (2.4) alone cannot imply (75.16). |
| Source applicability | **Fail for the target.** KRW gives only (3.19); root spacing, separated-point large sieve, reciprocal exponent pairs, centre-averaged divisor means, Kloosterman fractions, and Kuznetsov each miss an exact hypothesis or retain a positive power loss. |
| Downstream scope | **Pass.** The corrected reduction and (4.1) do not prove the cone, full M2, M9, or the global exponent. |

No numerical computation was used.  The controls are algebraic or
source-based and satisfy the campaign's analytical allocation.

## 6. Dependencies and exact artifacts used

The local repository artifacts used, and only the selected-context
artifacts used, were:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/briefs/near_product_energy_hostile_audit.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-affine-cone/synthesis.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-affine-cone/reports/m2_cone_source_hostile_audit.md`;
- `rounds/codex-managed/m9-top-endpoint-transform/synthesis.md`.

No sibling Round-75 report, proof draft, validation matrix, source card,
or shared Round-75 synthesis was read.  The primary external artifacts
were the seven papers linked in Section 3: Kowalski--Robert--Wu
Proposition 5; Robert--Sargos Theorem 2; Bombieri's large sieve;
Huxley--Watt's smooth exponential-sum theorem; Ivi\'c's centre-averaged divisor
mean square; Bettin--Chandee's Kloosterman-fraction theorem; and the
Deshouillers--Iwaniec Kloosterman/spectral framework.

The only accepted mathematical input is the exact one-sided endpoint
transform and its external boundary/error normalization.  The
all-orders moving-symbol construction, (1.1), (1.2), and the signed
off-diagonal remain candidate evidence until independently checked and
patched by the conductor.

## 7. Recommended state effect

**Revise, do not promote, the Round-75 near-product reduction.**  Replace
the leading-only \(\mathcal K_{\tau,l}\) in (75.8) by an exact normalized
Gaussian kernel or a stated \(N\)-term moving symbol, replace the naive
Parseval justification by periodized Parseval plus (1.1), and record that
the active second-Poisson sign is \(k=-m\asymp-L\).

The narrow graph-worthy result is the following no-go/reduction:

> The repaired reciprocal energy is the adjoint image of the exact
> transposed-row Cauchy energy (4.1).  Its high-character B-process
> restores the odd character, the cone \(m\le r\le4m\), the positive
> phase \(e(\sqrt{Xrm})\), and the actual profile/collars, with Gaussian
> unit \(e(-1/8)\).  It therefore supplies no independent saving.

The direct transposed-row implication (2.6) may be retained as an exact
sufficient reduction, and the all-orders collar/periodized-Parseval
repair may be retained as candidate evidence.  Keep
`M9-M2-top-endpoint-signed-cone`,
`M9-M2-sign-preserving-poisson-voronoi-route`, `M9-M2`, `M9`, and the
global exponent open.  Add no external-dependency promotion: the only
applicable primary bound, (3.19), is dominated, and no completed source
card was produced in this task.
