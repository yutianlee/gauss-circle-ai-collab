# Dual three-quarter attack

## 1. Result and verdict

For a genuinely smooth denominator block, the \(d\)-Poisson/\(B\)-process can
be completed with its leading constant and with a harmless uniform error.
For the positive \(h\)-block it gives

\[
 \boxed{
 \mathcal B^+_{L,W}
 =-\frac{e(1/8)}{2\pi}
 X^{1/4}(LK)^{-3/4}\,\mathcal T_{L,K}
 +O_W(1),
 \qquad K=\frac{XL}{D^2}. }
 \tag{1.1}
\]

Here \(\mathcal T_{L,K}\) is the exact character-weighted product-phase sum

\[
 \mathcal T_{L,K}
 =\sum_{h\asymp L}\sum_{k\asymp K}
 \chi_4(h)a_{L,K}(h,k)e(\sqrt{Xhk}),                 \tag{1.2}
\]

and \(a_{L,K}\) is the normalized symbol displayed in (4.2) below. Its
support is a fixed slanted subregion of the dyadic \(L\times K\) rectangle,
and it has bounded normalized derivatives to the order possessed by the
original cutoffs.

Consequently,

\[
 \mathcal T_{L,K}\ll_\varepsilon (LK)^{3/4}X^\varepsilon
 \tag{1.3}
\]

is not merely sufficient: for the separately controlled positive-frequency
smooth block it is, up to the \(O(1)\) transform error, **equivalent** to

\[
 \mathcal B^+_{L,W}\ll_\varepsilon X^{1/4+\varepsilon}. \tag{1.4}
\]

Thus the proposed dual estimate is an exact re-expression of the remaining
\(M2\) pointwise problem, not a weaker intermediate lemma.

The bound (1.3) does hold in regions already covered on the original side:
the accepted T2S terminal line, the isolated trivial/second-derivative
endpoint, and the conductor-audited exponent-pair wedge

\[
 178\ell+1638\delta\le 463,                           \tag{1.5}
\]

coming from the exponent pair
\((89/1282,997/1282)\). Outside those baseline regions, elementary
one-variable differencing gives no open new corridor. Product grouping
creates an irregular localized divisor coefficient; treating it as a smooth
coefficient is invalid. No exact primary-source theorem found in the
literature audit proves (1.3) for the actual symbol in the unresolved
corridor.

**Verdict:** promote the smooth transform and its exact normalization, but
retain (1.3) as unproved in the remaining corridor. The dual route has
identified a sharp equivalent formulation and an off-diagonal square-root
spacing interface; it has not reduced the difficulty.

No numerical experiment was used.

## 2. Exact hypotheses and original block

Write \(e(t)=e^{2\pi i t}\). Let

\[
 W\in C_c^\infty((a,b)),\qquad 0<a<b<\infty,
 \tag{2.1}
\]

and let \(\eta\) be a fixed smooth dyadic \(h\)-cutoff. Put

\[
 q_L(h)=\eta(h/L)\Phi(h/(H+1)).                       \tag{2.2}
\]

The exact positive-frequency Vaaler block considered here is

\[
 \mathcal B^+_{L,W}
 =-\frac1\pi\sum_{h\ge1}
 \frac{\chi_4(h)q_L(h)}h
 \sum_{d\in\mathbb Z}W(d/D)e\!\left(\frac{hX}{4d}\right).
 \tag{2.3}
\]

The support of \(W(d/D)\) is positive, so the apparent \(d=0\) term is
absent. The active project range is

\[
 X^{1/4}\le D\le X^{1/2},\qquad
 1\le L\le DX^{-1/4}.                                 \tag{2.4}
\]

Only the \(d\)-weight must be \(C_c^\infty\) for the transform below. The
\(h\)-weight may instead be normalized BV if (1.2) is interpreted with a BV
symbol. A sharp \(d\)-shell is not covered by the stated transform; its
boundary terms must be handled before an unsmoothed claim is made.

The character is kept exact:

\[
 \chi_4(h)=\frac{e(h/4)-e(3h/4)}{2i}.                 \tag{2.5}
\]

Thus (2.3) can equally be transformed shift by shift with the factor
\(e(\rho h/4)\), \(\rho=1,3\). Nothing below replaces this signed coefficient
by its absolute value.

## 3. Poisson summation and stationary phase

Fix \(h>0\), and set

\[
 A_h=\frac{hX}{4D}.
 \tag{3.1}
\]

Poisson summation gives the exact identity

\[
 \sum_dW(d/D)e\!\left(\frac{hX}{4d}\right)
 =D\sum_{r\in\mathbb Z}
 \int_{\mathbb R}W(u)e\!\left(\frac{A_h}{u}-rDu\right)du.
 \tag{3.2}
\]

### 3.1 Stationary frequencies and leading amplitude

For \(r\ge0\), the derivative of \(A_h/u-rDu\) has no zero on the positive
support. Write \(r=-k\) for the remaining frequencies. For \(k>0\), the
phase

\[
 F_{h,k}(u)=\frac{A_h}{u}+kDu
 \tag{3.3}
\]

has the unique critical point

\[
 u_0=\sqrt{\frac{A_h}{kD}}
     =\sqrt{\frac{hX}{4kD^2}},\qquad
 k\asymp \frac{hX}{D^2}.                              \tag{3.4}
\]

At this point,

\[
 F_{h,k}(u_0)=\sqrt{hXk},\qquad
 F''_{h,k}(u_0)=\frac{2A_h}{u_0^3}>0.                 \tag{3.5}
\]

The one-term stationary-phase formula, in the normalization \(e(t)\), is

\[
\begin{aligned}
 D\int W(u)e(F_{h,k}(u))du
 ={}&e(1/8)\frac{D W(u_0)}{\sqrt{F''_{h,k}(u_0)}}
       e(\sqrt{hXk})
       +O_W(DA_h^{-3/2})\\
 ={}&e(1/8)\frac{(hX)^{1/4}}{2k^{3/4}}
 W\!\left(\sqrt{\frac{hX}{4kD^2}}\right)e(\sqrt{hXk})
 +O_W(DA_h^{-3/2}).                                   \tag{3.6}
\end{aligned}
\]

This verifies both the phase and the factor \(1/2\). On the stationary
range, the leading size in (3.6) is equivalently

\[
 \asymp \frac{D^{3/2}}{(hX)^{1/2}}.                  \tag{3.7}
\]

### 3.2 Zero mode, nonstationary modes, and the total error

The zero mode has phase derivative \(\asymp A_h\) on the \(u\)-support, so
repeated integration by parts gives

\[
 D\int W(u)e(A_h/u)du=O_{J,W}(DA_h^{-J}).             \tag{3.8}
\]

For \(r>0\), the derivative has size \(\gg A_h+rD\), and summing the
corresponding integration-by-parts bounds is harmless. For \(r=-k<0\), a
uniform stationary-phase partition in the parameter \(kD/A_h\) gives
(3.6) whenever the critical point meets the support. Outside a fixed
enlargement of that parameter interval, integration by parts applies.

There are \(O(A_h/D)=O(hX/D^2)\) stationary frequencies. Hence the sum of
the displayed errors in (3.6) is

\[
 O_W\!\left(\frac{A_h}{D}\,DA_h^{-3/2}\right)
 =O_W(A_h^{-1/2}).                                    \tag{3.9}
\]

Because \(W\) is compactly supported and flat at the boundary of its
support, a critical point crossing that boundary introduces no half-Fresnel
or hard-endpoint term; the parameter-uniform stationary expansion continues
with \(W(u_0)=0\). Combining the stationary and nonstationary ranges gives
the conservative uniform transform

\[
\boxed{
 \sum_dW(d/D)e\!\left(\frac{hX}{4d}\right)
 =\frac{e(1/8)(hX)^{1/4}}2
 \sum_{k\ge1}\frac{W\!\left(\sqrt{hX/(4kD^2)}\right)}{k^{3/4}}
 e(\sqrt{hXk})+O_W(1). }
 \tag{3.10}
\]

The main sum in (3.10) is finite. In (2.4), \(A_h\gg X^{1/2}\), so the
large stationary parameter is uniform. Also \(hX/D^2\gg1\) in exponent
scale. At the transition \(D\asymp X^{1/2},h\asymp1\), the stationary sum
may contain only \(O(1)\), or even no, integer frequencies depending on the
support constants; (3.10) remains valid and its \(O(1)\) error is sufficient.

If \(W\) is replaced by a sharp interval indicator, the assertion about
boundary crossing is false. Endpoint integrals then have to be included;
this report proves only the smooth transform requested in the brief.

## 4. Exact dual normalization and equivalence

Insert (3.10) into (2.3), and put

\[
 K=\frac{XL}{D^2},\qquad M=LK=\frac{XL^2}{D^2}.       \tag{4.1}
\]

Define the actual normalized symbol

\[
 a_{L,K}(h,k)=q_L(h)
 \left(\frac{LK}{hk}\right)^{3/4}
 W\!\left(\sqrt{\frac{hX}{4kD^2}}\right).            \tag{4.2}
\]

Then (1.2) and (1.1) follow. Indeed,

\[
 \frac1h\frac{(hX)^{1/4}}{2k^{3/4}}
 =\frac{X^{1/4}}2(hk)^{-3/4}
 =\frac{X^{1/4}}{2M^{3/4}}
   \left(\frac{M}{hk}\right)^{3/4}.                  \tag{4.3}
\]

The transform error contributes only

\[
 \ll_W\sum_{h\asymp L}\frac1h\ll_W1.               \tag{4.4}
\]

On the support of (4.2), \(h\asymp L\), \(k\asymp K\), and

\[
 (h\partial_h)^i(k\partial_k)^j a_{L,K}(h,k)\ll_{i,j}1
 \tag{4.5}
\]

to every order available from \(q_L\) and \(W\). The periodic factor
\(\chi_4(h)\) is deliberately kept outside this smooth symbol.

Rearranging (1.1) gives

\[
 \mathcal T_{L,K}
 =-2\pi e(-1/8)X^{-1/4}M^{3/4}\mathcal B^+_{L,W}
 +O_W(X^{-1/4}M^{3/4}).                               \tag{4.6}
\]

Equations (1.1) and (4.6) prove the claimed two-way implication between
(1.3) and (1.4). For a full real block obtained by joining positive and
negative frequencies, (1.3) is still sufficient. The reverse implication
must be applied to the positive block (or separately to its two shifts),
since a bound on a real part alone need not bound the corresponding complex
sum. This is the only signed/complex qualification to the equivalence.

## 5. What elementary estimates actually give

Let \(a(h,k)\) have the normalized variation of (4.2), and temporarily
retain or discard \(\chi_4(h)\) only as explicitly stated.

### 5.1 One-variable second derivative estimates

For fixed \(h\asymp L\),

\[
 \frac{d^2}{dk^2}\sqrt{Xhk}\asymp
 \frac{\sqrt{Xh}}{K^{3/2}}.
\]

Van der Corput and partial summation in \(k\), followed by absolute summation
in \(h\), give

\[
 \mathcal T_{L,K}\ll_\varepsilon X^\varepsilon
 \left(
 X^{1/4}L^{5/4}K^{1/4}
 +X^{-1/4}L^{3/4}K^{3/4}
 \right).                                             \tag{5.1}
\]

The first term divided by the target \(M^{3/4}\) is

\[
 X^{1/4}\sqrt{\frac LK}.                              \tag{5.2}
\]

It reaches (1.3) only if \(K/L\ge X^{1/2}\). But

\[
 \frac KL=\frac X{D^2},                               \tag{5.3}
\]

so within \(D\ge X^{1/4}\) this happens only on the collapsed boundary
\(D\asymp X^{1/4}\). Interchanging \(h\) and \(k\) is worse because
\(K\ge L\) throughout the active triangle. The second term in (5.1) is
already smaller than the target by \(X^{-1/4}\).

The trivial estimate is

\[
 |\mathcal T_{L,K}|\ll M,                             \tag{5.4}
\]

which reaches \(M^{3/4}\) only when \(M=X^{o(1)}\); in the power diagram this
adds only the isolated point \(D=X^{1/2},L=1\). Therefore (5.1) and (5.4)
produce no open subregion of the still-unresolved corridor.

### 5.2 Product grouping and the irregular coefficient

Grouping by \(m=hk\) is an exact identity:

\[
 \mathcal T_{L,K}
 =\sum_{m\asymp M}c_{L,K}(m)e(\sqrt{Xm}),             \tag{5.5}
\]

where

\[
 c_{L,K}(m)=
 \sum_{\substack{h\mid m\\h\asymp L,\ m/h\asymp K}}
 \chi_4(h)a_{L,K}(h,m/h).                             \tag{5.6}
\]

One has only the pointwise divisor bound

\[
 |c_{L,K}(m)|\ll \tau(m).                             \tag{5.7}
\]

For the coefficient-free phase \(f(m)=\sqrt{Xm}\), a second-derivative
estimate would give

\[
 \sum_{m\asymp M}e(\sqrt{Xm})
 \ll X^{1/4}M^{1/4}+X^{-1/4}M^{3/4}.                 \tag{5.8}
\]

At the terminal product length \(M=X^{1/2}\), the first term in (5.8) is
exactly \(M^{3/4}=X^{3/8}\). But (5.8) does not transfer to (5.5): van der
Corput's unweighted second-derivative theorem does not allow an irregular
coefficient of arbitrary variation, and partial summation would require a
new bound for every partial sum of (5.6). The estimate

\[
 \sum_{m\asymp M}|c_{L,K}(m)|^2\ll_\varepsilon
 M X^\varepsilon                                      \tag{5.9}
\]

from divisor bounds, even when available with the localized symbol, gives
only \(M X^\varepsilon\) by Cauchy--Schwarz, namely the trivial scale rather
than \(M^{3/4}\).

The coefficient has no automatic sign cancellation. In the idealized
balanced, odd-\(m\), symmetric-symbol case, pairing complementary divisors
\(h,k=m/h\) gives

\[
 \chi_4(h)+\chi_4(k)
 =\chi_4(h)(1+\chi_4(m)).                              \tag{5.10}
\]

Thus pairs cancel for \(m\equiv3\pmod4\), but reinforce for
\(m\equiv1\pmod4\). For even \(m\), for \(L\ne K\), or for the actual
slanted symbol (4.2), complementary pairing is not available in this form.
After summing all divisor scales, the familiar identity

\[
 r_2(m)=4\sum_{h\mid m}\chi_4(h)                      \tag{5.11}
\]

shows why (5.6) is a localized Hardy/Voronoi coefficient rather than a
smooth weight. A uniform theorem for (5.5) at \(M\le X^{1/2}\) would contain
localized endpoint-strength circle-problem kernels; product grouping has
not simplified the arithmetic.

### 5.3 The exact correlation left by Cauchy

Cauchy in \(h\) gives

\[
 |\mathcal T_{L,K}|^2
 \le L\sum_{h\asymp L}
 \left|\sum_{k\asymp K}a_{L,K}(h,k)e(\sqrt{Xhk})\right|^2.
 \tag{5.12}
\]

The character has disappeared because \(|\chi_4(h)|^2\) is the odd-integer
indicator. The diagonal \(k_1=k_2\) on the right contributes
\(O(L^2K)\) after the outer factor \(L\), hence size \(L\sqrt K\) after
taking square roots. Since \(K\ge L\), this is at most \(M^{3/4}\), and it
is exactly critical when \(D=X^{1/2}\), where \(K\asymp L\).

The off-diagonal phases are

\[
 \sqrt{Xh}(\sqrt{k_1}-\sqrt{k_2}).                    \tag{5.13}
\]

Thus a clean sufficient successor lemma is the diagonal-sized mean-square
bound

\[
\boxed{
 \sum_{h\asymp L}
 \left|\sum_{k\asymp K}a_{L,K}(h,k)e(\sqrt{Xhk})\right|^2
 \ll_\varepsilon L^{1/2}K^{3/2}X^\varepsilon,
 \qquad K\ge L. }
 \tag{5.14}
\]

It implies (1.3) by (5.12). At \(L=K\), the right side of (5.14) is
\(L^2\), exactly the diagonal size, so no endpoint slack remains. Expanding
(5.14) makes it a spacing/correlation estimate for the square-root
differences in (5.13). Elementary differencing does not prove it: the first
Cauchy step has already erased the periodic sign, while close and resonant
square-root differences require collective spacing information.

The actual signed target (1.3) is weaker than (5.14), because it may exploit
\(\chi_4\) before Cauchy. Therefore (5.14) is proposed only as the weakest
clean *Cauchy-based* sufficient lemma, not as an equivalent reformulation.
The genuinely weakest new statement remains (1.3), which is equivalent to
the original block target by Section 4.

## 6. Parameter and endpoint audit

Write \(D=X^\delta\), \(L=X^\ell\). Then

\[
 K=X^{1+\ell-2\delta},\qquad
 M=LK=X^{1+2\ell-2\delta},\qquad
 \frac KL=X^{1-2\delta}.                              \tag{6.1}
\]

On the active triangle, \(K\ge L\) and \(M\le X^{1/2}\). On the terminal
line \(\ell=\delta-1/4\), one has \(M=X^{1/2}\) and the dual target is always
\(X^{3/8+\varepsilon}\). T2S already proves it for the actual symbol through
(4.6).

The three requested endpoint scales are:

| \(D\) | \(L\)-range | \(K\) | \(M\) | elementary dual conclusion |
|---|---|---|---|---|
| \(X^{1/4}\) | \(L=1\) | \(X^{1/2}\) | \(X^{1/2}\) | (5.1) reaches \(M^{3/4}\) |
| \(X^{3/8}\) | \(1\le L\le X^{1/8}\) | \(X^{1/4}L\) | \(X^{1/4}L^2\) | (5.1) misses by \(X^{1/8}\); terminal point is covered by T2S |
| \(X^{1/2}\) | \(1\le L\le X^{1/4}\) | \(L\) | \(L^2\) | trivial only at \(L=1\); for \(1<L<X^{1/4}\) the target remains critical |

The newly certified exponent pair

\[
 (\kappa,\lambda)=\left(\frac{89}{1282},\frac{997}{1282}\right)
 \tag{6.2}
\]

applied to the original reciprocal phase covers

\[
 \kappa(1+\ell-2\delta)+\lambda\delta\le\frac14,
 \tag{6.3}
\]

which is exactly (1.5) after clearing denominators. By (4.6), this also
proves the actual dual target (1.3) in that wedge. This is baseline
coverage transferred through the transform, not a new product-phase
estimate. The elementary dual bounds above do not enlarge it inside the
remaining open corridor.

## 7. Primary-source literature audit

1. Terence Tao, Tim Trudgian, and Andrew Yang,
   [*New exponent pairs, zero density estimates, and zero additive energy
   estimates: a systematic approach*](https://arxiv.org/abs/2501.16779),
   supplies the primary exponent-pair source for (6.2). The exact
   reciprocal-phase normalization and weighted transfer were audited by the
   conductor; this report uses only the resulting wedge (1.5). The paper
   does not state (1.3).

2. Xiaochun Li and Xuerui Yang,
   [*An improvement on Gauss's Circle Problem and Dirichlet's Divisor
   Problem*](https://arxiv.org/abs/2308.14859), develops a
   Bombieri--Iwaniec first/second-spacing architecture. Its introduction
   explicitly identifies the loss from breaking the long sum into short
   sums as the reason that this architecture does not reach the \(1/4\)
   circle exponent. Its first-spacing norm involves the vector
   \((l,kl,l\sqrt k,l/\sqrt k)\), not the exact pointwise symbol (4.2), and
   no displayed theorem in the audited local source yields (1.3).

3. M. N. Huxley and G. Kolesnik,
   [*Exponential Sums and the Riemann Zeta Function III*](https://doi.org/10.1112/plms/s3-62.3.449),
   studies one-dimensional exponential sums by the discrete
   Hardy--Littlewood method and counts approximate equalities among sums of
   square roots. This is structurally relevant to (5.13), but it is not a
   theorem for the localized divisor coefficient (5.6).

4. O. Robert and P. Sargos,
   [*A Fourth Derivative Test for Exponential Sums*](https://doi.org/10.1023/A:1014363224308),
   proves a one-dimensional fourth-derivative estimate via triple
   exponential sums. It likewise does not permit the irregular coefficient
   in (5.5) and therefore cannot justify applying an unweighted derivative
   test to that sum.

5. Jean Bourgain and Nigel Watt,
   [*Mean square of zeta function, circle problem and divisor problem
   revisited*](https://arxiv.org/abs/1709.04340), is retained only as a
   structural Bombieri--Iwaniec reference. The project source card remains
   incomplete, so no theorem from it is imported.

No exact primary-source result located in this audit has the hypotheses and
conclusion of (1.3) or (5.14) throughout the unresolved \((\delta,\ell)\)
corridor.

## 8. Required controls

### Source applicability

Only the conductor-certified exponent pair (6.2) is used positively, and
only through its exact wedge. Li--Yang, Huxley--Kolesnik,
Robert--Sargos, and Bourgain--Watt are not imported as black boxes for the
product-phase target.

### Proves-too-much

The transform theorem is for the fixed Vaaler character and the actual
smooth symbol. Estimate (1.3) is not asserted for arbitrary bounded
coefficients. In particular, (5.8) is never applied to (5.5), and the
divisor bound (5.7) is not mistaken for bounded variation. The Cauchy
lemma (5.14) is explicitly labeled stronger than the signed target because
it discards \(\chi_4\).

### Signed versus unsigned

The exact \(\chi_4\) factor survives Poisson summation. Complementary-divisor
cancellation is shown to be partial by (5.10), and Cauchy is shown explicitly
to remove the sign in (5.12). No unsigned moment or absolute collision count
is used as pointwise signed control.

### Dyadic endpoints

The transform remains uniform when \(K\asymp1\). The three named \(D\)-scales
and both \(L=1\) and \(L=DX^{-1/4}\) are checked in Section 6. Smooth support
endpoints are covered; sharp interval endpoints are expressly excluded.

## 9. First doubtful or unproved step

Under (2.1), the Poisson and stationary-phase derivation through (4.6) has
no unproved asymptotic step. The first unproved analytic step is (1.3) in
the complement of the already covered regions, or, after sacrificing the
character by Cauchy, the diagonal-sized correlation estimate (5.14).

For the unsmoothed project sum, the first additional seam is a quantitative
smoothing/unsmoothing argument that controls the hard \(d\)-endpoints. It
is not supplied here and must not be inferred from (3.10).

## 10. Dependencies and exact artifacts used

- rounds/codex-managed/m9-frequency-phase-diagram/briefs/dual_three_quarter_attack.md
- rounds/codex-managed/m9-frequency-phase-diagram/plan.json
- rounds/codex-managed/m9-frequency-phase-diagram/reports/blind_phase_diagram.md
- rounds/codex-managed/m9-generic-band-signed-correlation/reports/top_block_two_shift_attack.md
- state/proof_obligations.yml
- state/best_proof_draft.md
- state/active_campaign.yml
- sources/li_yang_2023.md
- sources/bourgain_watt.md
- Primary local source:
  rounds/web-research-test/Li-Yang-arXiv-2308.14859v2.tex
- The five primary-source links listed in Section 7.
- Conductor message certifying the exponent pair (6.2), its normalized-BV
  applicability, and the wedge (1.5).

No computational artifact was used.

## 11. Recommended state effect

- **Promote** a scoped smooth \(d\)-Poisson/\(B\)-process lemma: (3.10), with
  the exact stationary phase, amplitude, zero/nonstationary control, and
  smooth-endpoint hypothesis.
- **Promote** the exact normalized identity (1.1) and record that the
  \((LK)^{3/4}\) target for the actual positive-frequency symbol is equivalent
  to the \(X^{1/4}\) smooth block target.
- **Record baseline coverage** of the dual target on the T2S terminal line,
  at the isolated unit-frequency endpoint, and in the certified wedge
  \(178\ell+1638\delta\le463\).
- **Retain unresolved** (1.3) in the remaining corridor. Do not advertise it
  as an independent reduction of \(M9\)-\(M2\).
- **Retain as a candidate interface** the stronger Cauchy-based mean-square
  lemma (5.14), with the warning that it erases the only explicit character
  sign and is exactly diagonal-critical at \(D=X^{1/2}\).
- **No promotion** of a product-grouped one-dimensional derivative estimate,
  any Bourgain--Watt/Li--Yang endpoint theorem, the full \(M9\)-\(M2\)
  obligation, or the global proof claim.
