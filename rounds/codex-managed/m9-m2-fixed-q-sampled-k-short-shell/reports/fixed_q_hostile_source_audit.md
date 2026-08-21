# Round 104 hostile/source audit: uniform fixed-\(q\) rows and the exact \(D^2\) route ceiling

Campaign: m9-m2-fixed-q-sampled-k-short-shell

Task: fixed_q_hostile_source_audit

Role: hostile mathematical and primary-source auditor

Status: candidate evidence only; no shared proof state is edited.

## 1. Result

**The uniform fixed-\(q\) actual-row theorem survives, including the
collapsing-cone edge, but rowwise Cauchy leaves exactly a \(D^2\) route
ceiling.**  On every nonempty residual cell

\[
 a\asymp b=a+2q\asymp A,\qquad q\asymp D,\qquad
 k\asymp K\asymp {JD\over A},\qquad
 g\asymp G\asymp {L\over A},
\]

the complete centred physical integral, with every literal remaining
\(k\)-owner, satisfies

\[
 \sup_k|B_{a,q,g}(k)|
 +\operatorname {Var}_k B_{a,q,g}(k)
 \ll_\varepsilon X^\varepsilon V_D,\qquad
 V_D:=\sqrt{AL\over JD}.                              \tag{104.H1}
\]

The bound is uniform through both physical collars and remains uniform
when \(b/a\to4^{-}\) and the reciprocal interval collapses.  No proof
step divides by the interval length or by \(2-\sqrt{b/a}\).  If the two
physical collars overlap, their product still has the same fixed symbol
seminorms; if the integer reciprocal fibre becomes empty or a singleton,
the zero or pointwise part of (104.H1) applies.

Opening the complete punctured metric window produces

\[
 f_{\nu,g}(k)=\left(\nu-{g\over2}\right){\Lambda_q\over k},
 \qquad n:=|2\nu-g|\ge1,
\]

and

\[
 |f_{\nu,g}''(k)|\asymp {nA^2\over JD}.               \tag{104.H2}
\]

The density mode \(\nu=0\) is retained and has \(n=g\), not zero.  The
two metric Fourier half-moments cancel every \(D\)-power, giving

\[
 \boxed{|F_a(q)|\ll_\varepsilon X^\varepsilon {L^2\over A}}. \tag{104.H3}
\]

For \(q>1\), no prior owner creates a jagged external \(k\)-mask.
Primitivity, the square-ray owner, the safe-\(\rho\) owner and dyadic
packet ownership are constant on a fixed \((a,q)\) row.  The only
apparently \(k\)-dependent prior deletion is the exact metric centre,
where the punctured factor \(W_R(\Lambda_q/k)\) is already zero.  The
original Poisson-mode owner is the single open interval in \(k\), hence
zero extension has only two jumps.  Profiles, floors, stars, physical
collars, saddle transitions and finite odd-lift support remain in the
literal complete coefficient.

Consequently

\[
 E_D:=\sum_{a\asymp A}\sum_{q\asymp D}|F_a(q)|^2
 \ll_\varepsilon X^\varepsilon {DL^4\over A},         \tag{104.H4}
\]

and, for \(1\le H\le D\),

\[
 \mathcal G_H^{\rm act}
 \le H^2E_D
 \ll_\varepsilon X^\varepsilon {H^2DL^4\over A}.      \tag{104.H5}
\]

The frozen target equals

\[
 X^\varepsilon {H^2E_0\over\rho}
 =X^\varepsilon {H^2L^4\over AD},
\]

so (104.H5) is above it by exactly \(D^2\).  This proves the target for
fixed \(D\), and for every prescribed polylogarithmic range
\(D\le(\log X)^C\) after an epsilon split.  It proves no polynomial
\(D=X^\delta\) range.

This \(D^2\) statement is a **ceiling of the pointwise-row plus Cauchy
route**, not an actual obstruction or lower bound for the polynomial
shell.  Signed \(q\)-correlations can in principle cancel the Gram
diagonal, and no lower bound for the complete actual coefficient is
known.  No real actual-symbol counterexample to (104.H1) or (104.H3)
was found.  None of the primary theorems audited in Section 5 accepts
the literal moving coefficient and supplies the missing polynomial
\(q\)-correlation.

## 2. Exact statement and hypotheses

Let \(e(t)=e^{2\pi it}\), \(J=\sqrt X\), and
\(1\le L\le J^{1/2}\).  Work on one residual hard-top cell with

\[
 b=a+2q,\qquad a,b\ {\rm odd},\qquad a<b<4a,\qquad
 a\asymp b\asymp A,\qquad q\asymp D.                 \tag{104.H6}
\]

Put

\[
 \delta_q=\sqrt b-\sqrt a={2q\over\sqrt a+\sqrt b},
 \qquad
 \Lambda_q={X\delta_q^2\over2},                       \tag{104.H7}
\]

and retain the literal open reciprocal interval

\[
 I_{a,q}=\left({J\delta_q\over2\sqrt a},
                    {J\delta_q\over\sqrt b}\right).   \tag{104.H8}
\]

Uniformly on (104.H6),

\[
 \delta_q\asymp {D\over\sqrt A},\qquad
 \Lambda_q\asymp {J^2D^2\over A},\qquad
 k\asymp K\asymp {JD\over A}.                         \tag{104.H9}
\]

A nonempty odd-lift fibre has \(g\asymp G=L/A\), so \(A\ll L\).
The primitive condition is \((a,b)=1\), equivalently \((a,q)=1\);
if it fails, the whole fixed row is zero.

The complete uncentred and centred integrals are

\[
 \mathfrak C^\circ_{a,q,k}(g)
 =g\int_{b/4}^{a}A^\circ_{ga,gb}(gu)
 e\!\left(g[ku-J\delta_q\sqrt u]\right)du,
\]

\[
 \mathfrak C^\circ_{a,q,k}(g)
 =e\!\left(-{g\Lambda_q\over2k}\right)
  \mathfrak B^\circ_{a,q,k}(g).                       \tag{104.H10}
\]

With \(t=\sqrt u\), the accepted exact homogeneous factorisation is

\[
 \mathfrak B^\circ_{a,q,k}(g)
 =L^3g^{-2}P_{a,b}(g)
  \int Q_{a,b,g}(t)e\!\left(gk(t-r_k)^2\right)dt,
 \qquad r_k={J\delta_q\over2k}.                       \tag{104.H11}
\]

Here \(P_{a,b}\) is the literal dyadic/Vaaler lift profile.
\(Q_{a,b,g}\) contains the exact \(q_X\), both physical \(W\)-profiles,
the real-affine collar product, the endpoint extension and all profile,
floor and star data.  The hypotheses used are the actual fixed profile
seminorms:

\[
 |P_{a,b}(g)|\ll1,\qquad
 \|Q_{a,b,g}\|_\infty+\operatorname {Var}Q_{a,b,g}
 \ll A^{-5/2},                                       \tag{104.H12}
\]

together with the corresponding fixed higher seminorms on smooth pieces,
flat collar endpoints and collar transition width

\[
 w_c\asymp {1\over g\sqrt A}.                         \tag{104.H13}
\]

These are substantially stronger than an arbitrary bounded coefficient
hypothesis.

Let \(\mathcal G_{a,q}\) be the exact finite odd-lift set;
\(\#\mathcal G_{a,q}\ll G\).  The literal row can be written, without
changing any coefficient, as

\[
\begin{aligned}
 F_a(q)=\mathbf1_{\rm row\ owners}(a,q)
 \sum_{k\in I_{a,q}\cap\mathbb Z}
 W_R(\Lambda_q/k)
 \sum_{g\in\mathcal G_{a,q}}
 &\Omega_{a,q,g}(k)
 e\!\left(-{g\Lambda_q\over2k}\right)\\
 &\times\mathfrak B^\circ_{a,q,k}(g).
\end{aligned}                                        \tag{104.H14}
\]

The factors in \(\Omega\) not already in \(Q_{a,b,g}\) are fixed smooth
dyadic cutoffs, fixed signs and finitely many conjugate orientations.
Their product has bounded variation on the fixed \(k\)-fibre.  Sharp
reciprocal support is handled by zero extension.

For each complete metric member,

\[
 W_R(t)=\sum_{\nu\in\mathbb Z}\widehat W_R(\nu)e(\nu t),
 \qquad
 |\widehat W_R(\nu)|\ll_N
 R^{-1}(1+|\nu|/R)^{-N},\qquad 1\le R\le G.           \tag{104.H15}
\]

The coefficient \(\widehat W_R(0)\) is included.  Equations
(104.H1), (104.H3), (104.H4) and (104.H5) hold under precisely these
hypotheses.  They are upper estimates only.

## 3. Proof or derivation

Rationalising \(\delta_q\) proves (104.H7)--(104.H9).  Completing the
square gives the exact identity

\[
 ku-J\delta_q\sqrt u
 =k(\sqrt u-r_k)^2-{\Lambda_q\over2k},                \tag{104.H16}
\]

so no stationary expansion is being counted as an additional gain.  At
the two continuous endpoints of (104.H8), \(r_k=\sqrt a\) and
\(r_k=\sqrt b/2\), respectively.  Hence the saddle traverses the physical
interval once and monotonically.

The stationary width in \(t\) is \(w=(gk)^{-1/2}\).  From
(104.H9), (104.H13), \(g\asymp L/A\), \(A\ll L\) and \(L^2\le J\),

\[
 {w_c^2\over w^2}={k\over gA}
 \asymp {JD\over AL}\gg1.                             \tag{104.H17}
\]

Thus every collar transition is at least one stationary width.  The
general-\(q\) factor \(D\) helps this inequality.

The cone-collapse seam needs a separate literal check.  Write
\(s=\sqrt{b/a}\in(1,2)\).  Then

\[
 I_{a,q}=\left({J(s-1)\over2},{J(s-1)\over s}\right),
 \qquad
 |I_{a,q}|={J(s-1)(2-s)\over2s},                      \tag{104.H18}
\]

while the physical \(t\)-length is

\[
 \sqrt a-{\sqrt b\over2}={\sqrt a(2-s)\over2}.        \tag{104.H19}
\]

Both lengths collapse as \(s\to2\), but every \(k\) still satisfies
\(k\asymp K\).  The proof below uses only \(\#(I_{a,q}\cap\mathbb Z)\ll K\);
it never uses the reverse inequality.  If the collars overlap, the
product of their two fixed transition functions still has
\(L^\infty\), variation and higher seminorms bounded at the scale in
(104.H12)--(104.H13).  Shortening the saddle path can only shorten the
variation integral.  Therefore no factor \((2-s)^{-1}\) appears.

To prove the complete-Fresnel bound, split (104.H11) at
\(|t-r_k|\le2w\) and into dyadic outer annuli.  Use the exact complete
Fresnel integral on the central part and integrate twice on each outer
annulus with

\[
 {1\over4\pi i gk(t-r_k)}{d\over dt}
 e\!\left(gk(t-r_k)^2\right).
\]

Flat collars remove boundary terms.  When the saddle crosses a collar,
(104.H17) pays every differentiated collar factor.  Along
\(k\mapsto(gk,r_k)\), the Gaussian scale changes only by a fixed factor,
and monotonicity of \(r_k\) charges the total variation of the actual
profile once.  The odd central derivative term is integrated against one
profile derivative, just as in the accepted complete-Fresnel
\(g\)-variation identity.  This proves, uniformly also in (104.H18),

\[
\begin{aligned}
 &\sup_{k\in I_{a,q}}
 \left|\int Q_{a,b,g}(t)e(gk(t-r_k)^2)dt\right|\\
 &\quad+
 \operatorname {Var}_{k\in I_{a,q}}
 \left(\int Q_{a,b,g}(t)e(gk(t-r_k)^2)dt\right)
 \ll A^{-5/2}(gK)^{-1/2}.                             \tag{104.H20}
\end{aligned}
\]

Sampling continuous variation and adding the two zero-extension jumps
preserves the bound.  Multiplying by the prefactor in (104.H11) gives

\[
\begin{aligned}
 L^3g^{-2}A^{-5/2}(gK)^{-1/2}
 &\asymp
 L^3\left({A\over L}\right)^2A^{-5/2}
 \left({LJD\over A^2}\right)^{-1/2}\\
 &=\sqrt{AL\over JD}=V_D.                             \tag{104.H21}
\end{aligned}
\]

Product variation with the literal bounded-variation multiplier
\(\Omega\) proves (104.H1).

Open (104.H15) in (104.H14).  For fixed \(g,\nu\),

\[
 f_{\nu,g}(k)=\left(\nu-{g\over2}\right){\Lambda_q\over k},
 \qquad n=|2\nu-g|.
\]

Every actual \(g\) is odd, so \(n\) is a positive odd integer.  Since
\(\Lambda_q\asymp J^2D^2/A\) and \(K\asymp JD/A\),

\[
 |f_{\nu,g}''(k)|={n\Lambda_q\over k^3}
 \asymp {nA^2\over JD}.                               \tag{104.H22}
\]

The elementary second-derivative estimate, using only
\(\#I_{a,q}\ll K\), yields uniformly on every subinterval

\[
 \max_{U\subset I_{a,q}}
 \left|\sum_{k\in U\cap\mathbb Z}e(f_{\nu,g}(k))\right|
 \ll \sqrt{nJD}+{\sqrt{JD}\over A\sqrt n}.            \tag{104.H23}
\]

Partial summation with (104.H1) gives

\[
 \sum_{k\in I_{a,q}\cap\mathbb Z}
 B_{a,q,g}(k)e(f_{\nu,g}(k))
 \ll_\varepsilon X^\varepsilon
 \left(\sqrt{ALn}+\sqrt{L/A}\,n^{-1/2}\right).         \tag{104.H24}
\]

All \(D\)-powers have cancelled.  From (104.H15), uniformly for odd
\(g\asymp G\),

\[
 \sum_\nu|\widehat W_R(\nu)|\,|2\nu-g|^{1/2}
 \ll\sqrt G,\qquad
 \sum_\nu|\widehat W_R(\nu)|\,|2\nu-g|^{-1/2}
 \ll G^{-1/2}.                                       \tag{104.H25}
\]

For \(R\ll G\), the main Fourier mass has
\(|2\nu-g|\asymp G\); for \(R\asymp G\), sum the positive odd distances
from \(g/2\).  Rapid decay handles both tails, and the same proof covers
\(G\asymp1\).  Equations (104.H24)--(104.H25) cost
\(O_\varepsilon(X^\varepsilon(L+1))\) per lift.  Since there are
\(O(G)=O(L/A)\) lifts, the final absolute lift sum proves (104.H3).

There are \(O(A)\) possible \(a\)'s and \(O(D)\) possible \(q\)'s, proving
(104.H4).  Finally, with exact zero extension,

\[
\begin{aligned}
 \mathcal G_H^{\rm act}
 &=\sum_{a,n}\left|\sum_{0\le h<H}(-1)^hF_a(n+h)\right|^2\\
 &\le H\sum_{a,n}\sum_{0\le h<H}|F_a(n+h)|^2
 =H^2\sum_{a,q}|F_a(q)|^2.                            \tag{104.H26}
\end{aligned}
\]

Also

\[
 {E_0\over\rho}
 ={LJD^2\over AJD^3/L^3}={L^4\over AD}.              \tag{104.H27}
\]

Comparison of (104.H26) with (104.H27) proves the exact \(D^2\) ratio.
It is independent of \(H\), so no choice of \(H\) improves this Cauchy
route.  A fixed power of \(\log X\) is absorbed by applying (104.H3)
with a smaller epsilon.  For \(D=X^\delta\), the same argument loses
\(X^{2\delta}\).

## 4. First doubtful or unproved step

The first hostile seam was owner exhaustion for \(q>1\).  The prior
owners can be checked one by one.

- The Round-75 diagonal is \(q=0\), disjoint from (104.H6).
- The original Poisson stationary-mode owner is exactly the one interval
  (104.H8).  Equality and nonstationary modes belong to the accepted
  endpoint/collar error, and zero extension makes only two jumps even
  when (104.H18) collapses.
- The Round-78 square-ray condition \(ab\) square is fixed once
  \((a,q)\) is fixed.  It removes the whole ray, not scattered \(k\)'s.
- Primitivity is \((a,q)=1\), again fixed on the row.
- The positive-safe condition \(AJD^3\ll L^3\), equivalently
  \(\rho\ll1\), is dyadic-block data and removes the whole cell.
- The Round-79 exact nonsquare-centre deletion can depend on \(k\), but
  at such a point \(\Lambda_q/k\in\mathbb Z\), and the strict punctured
  factor in (104.H14) is exactly zero.  Multiplying by this deletion
  changes no value and creates no variation jump.
- A fixed strict metric annulus is the smooth periodic function \(W_R\)
  itself.  It is opened completely in (104.H15), rather than left as a
  sharp mask in \(\Omega\).
- Real-affine collars, profile edges, floors, stars and saddle
  entry/exit are already in \(Q_{a,b,g}\).  The finite odd-lift set is
  independent of \(k\).  Fixed orientations are conjugates.

Thus no prior \(q>1\) owner introduces a hidden jagged \(k\)-multiplier,
and no doubtful step remains inside the scoped fixed-\(q\) row theorem.
Merely assuming \(|\Omega|\le1\) would not suffice; the preceding literal
placement is essential.

The first unproved step after (104.H3) is the complete signed
polynomial-shell \(q\)-correlation.  The exact Gram is

\[
 H\sum_{a,q}|F_a(q)|^2
 +2\Re\sum_{1\le s<H}(H-s)(-1)^s
 \sum_{a,q}F_a(q+s)\overline{F_a(q)}.                 \tag{104.H28}
\]

The row theorem controls neither the sign nor the cancellation in the
second line.  To remove the \(D^2\) route ceiling one needs this complete
mode-resolved signed correlation, or an average row theorem stronger
than (104.H4) by \(D^{-2}\).  Both moving reciprocal fibres, both lift
sets, primitive and prior owners, metric density and every discrepancy
mode, entry/exit and zero-extension crossings reappear.

This is not an actual polynomial-shell obstruction.  A genuine
obstruction would require a lower bound showing that (104.H28) exceeds
target for the literal coefficient.  No such lower bound is proved.
Pell and fourth-power recurrence, a coherent carrier, the actual
interior Gaussian and a large unsigned component capacity do not control
the complementary modes or the outer real part.  They therefore test the
method but do not refute the Gram.

## 5. Required controls, outcomes, and primary-source hypothesis map

| Required control | Hostile test and outcome |
|---|---|
| general-q reciprocal geometry | Rationalisation gives (104.H7)--(104.H9); the saddle maps the literal endpoints to \(a\) and \(b/4\). **Pass.** |
| collapsing \(b/a\to4\) edge | Equations (104.H18)--(104.H19) display both collapsing lengths.  No reverse length bound is used; overlapping collars retain uniform symbol seminorms. **Pass.** |
| \(K,G,V_D\) normalization | Equation (104.H21) gives exactly \(K\asymp JD/A\), \(G\asymp L/A\), and \(V_D=\sqrt{AL/(JD)}\). **Pass.** |
| complete centred integral | Equation (104.H16) is exact; all incomplete-Fresnel transitions remain in \(\mathfrak B^\circ\). **Pass.** |
| sampled-\(k\) BV through collars | The resolution ratio is \(JD/(AL)\), and (104.H20) is uniform through both transitions and their overlap. **Pass.** |
| odd metric frequency | Odd \(g\) makes \(|2\nu-g|\) a positive odd integer. **Pass.** |
| density and discrepancy | The full Fourier series, including \(\nu=0\), is summed before estimation. **Pass.** |
| reciprocal curvature | Exact differentiation gives \(n\Lambda_q/k^3\asymp nA^2/(JD)\). **Pass.** |
| Fourier half-moments | Both signs of the half-power are controlled in (104.H25), including \(G\asymp1\). **Pass.** |
| primitive and prior owners | The owner-by-owner audit in Section 4 leaves no jagged external \(k\)-mask. **Pass.** |
| profiles, floors, stars, orientations | All moving physical data are in (104.H11); fixed conjugate orientations preserve variation. **Pass.** |
| entry/exit and zero extension | The open interval is literal; zero extension gives two jumps, including at the collapsing edge. **Pass.** |
| empty and singleton fibres | Empty fibres vanish; singleton fibres use the pointwise half of (104.H20). **Pass.** |
| Pell, near-square and fourth powers | They can force metric recurrence or carrier coherence but do not change (104.H17), odd \(n\), or (104.H22). **Pass as controls; no actual lower obstruction.** |
| \(G\asymp1\) and small fibres | The discrete proof of (104.H25) covers \(G\asymp1\); small reciprocal fibres are handled above. **Pass.** |
| arbitrary-coefficient false shadow | A size-\(V_D\) sequence multiplied by the conjugate reciprocal phase makes the \(k\)-sum coherent, but violates (104.H1). **False analogue rejected.** |
| unsigned false shadow | On an actual interior plateau the leading complete-Fresnel magnitude is of order \(V_D\) on many \(k\)'s, so taking absolute values restores \(KV_D\) capacity. **No unsigned transfer.** |
| row energy \(D\)-count | \(O(AD)\) rows give exactly \(DL^4/A\). **Pass.** |
| Cauchy-to-Gram power | Each entry is counted \(H\) times after the first Cauchy factor \(H\), giving \(H^2E_D\); comparison with (104.H27) gives \(D^2\). **Pass.** |
| polylog absorption | For fixed \(C\), \(D\le(\log X)^C\) is absorbed after applying the row theorem with smaller epsilon. **Pass.** |
| polynomial-shell status | For \(D=X^\delta\), this route loses \(X^{2\delta}\); no actual lower bound is inferred. **Route ceiling only.** |
| downstream scope | No full fixed-\(a\) Gram, canonical M2 energy, M9-M2, M9 or exponent is inferred. **Pass.** |

The natural primary theorems were checked from their primary papers.
Their literal hypotheses do not match (104.H28).

| Primary source | Literal hypotheses audited | Verdict for a polynomial \(q\)-gain |
|---|---|---|
| H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, Theorem 1 ([primary paper](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)) | Finitely many real frequencies distinct modulo one, a positive minimum pairwise separation, and a compatible common coefficient family in the Hilbert bilinear form. | Reciprocal mode frequencies can collide or cluster below the active scale, while supports and actual coefficients move with \(q\).  The needed separation parameter is absent. |
| E. Bombieri and H. Iwaniec, *On the order of \(\zeta(1/2+it)\)*, Lemma 2.4 ([primary paper](https://www.numdam.org/article/ASNSP_1986_4_13_3_449_0.pdf)) | Two finite point sets in coordinate boxes, factorised coefficient families, a dot-product phase and explicitly retained close-pair quadratic forms for both sets. | Lifting (104.H28) leaves a nonfactorised moving physical coefficient.  The required close-pair energy is the open complete mode-resolved near-determinant problem, not a theorem hypothesis already verified. |
| O. Robert and P. Sargos, *Three-dimensional exponential sums with monomials*, Theorem 2 ([primary paper](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf)) | A fixed exponent \(\alpha\ne0,1\), four integers in one dyadic interval, and an unweighted positive four-monomial spacing count bounded by \(M^{2+\varepsilon}+\delta M^{4+\varepsilon}\). | It discards \(k,g\), metric modes, owners, signs and the physical integral.  A positive count neither cancels the diagonal nor proves the signed correlation. |
| X. Li and X. Yang, *An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem*, Proposition 3.1 and Theorem 4.2 ([primary version](https://arxiv.org/html/2308.14859v2)) | Proposition 3.1 treats a rectangular cone norm with bounded \(a_{kl}\), \(1\le L<K\le\eta^{-1}\le KL\), \(4\le q\le4.5\), and its displayed \(\eta\)-condition.  Theorem 4.2 treats a separably weighted \((h,m)\)-sum with phase \((hT/M)F(m/M)\), fixed \(C^3\) derivative/nondegeneracy bounds and explicit parameter cases. | The fixed-\(X\) row has a coupled reciprocal phase, two moving fibres, primitive owners, metric modes and entry/exit integrals.  No literal substitution preserves the theorem's form and hypotheses. |
| H. Weyl, *Über die Gleichverteilung von Zahlen mod. Eins*, Satz 9 ([primary scan](https://zenodo.org/records/2425535/files/article.pdf)) | Qualitative equidistribution for a polynomial with an irrational nonconstant coefficient against a fixed interval as averaging length grows. | This supports fixed-width recurrence controls only.  It gives no shrinking metric-window uniformity or fixed-\(X\) coefficient-weighted \(q\)-correlation. |

The fixed-\(q\) row proof imports none of these theorems: the
second-derivative estimate and complete-Fresnel calculation are internal.
The source verdict is therefore negative in the exact required sense:
no audited primary theorem produces a genuine polynomial \(D\)-gain for
the literal moving actual Gram.

## 6. Dependencies and exact artifacts used

The report used exactly the assigned Round-104 brief and selected
repository context:

- protocol.md;
- state/proof_obligations.yml, with the target nodes, their direct
  dependencies and recorded route obstructions checked explicitly;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m2-fixed-q-sampled-k-short-shell/derivation_packet.md;
- rounds/codex-managed/m9-m2-q1-actual-diagonal-energy/reports/q1_actual_symbol_hostile_source_audit.md;
- rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reports/actual_symbol_hostile_audit.md;
- rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/synthesis.md;
- rounds/codex-managed/m9-m2-determinant-weighted-actual-gram/reports/determinant_gram_hostile_source_audit.md;
- strategy/conductor_0817_full_proof_strategy.md;
- rounds/codex-managed/m9-m2-fixed-q-sampled-k-short-shell/briefs/fixed_q_hostile_source_audit.md.

The source audit opened the original Montgomery--Vaughan,
Bombieri--Iwaniec and Robert--Sargos papers, Li--Yang's primary arXiv
version and the primary Weyl scan linked in Section 5.  No external
theorem was imported.  No sibling Round-104 report, proof draft,
validation matrix, synthesis, legacy response or unlisted repository
artifact was used.  No numerical experiment was performed.  Apart from
this assigned report, no campaign artifact or shared state was edited.

## 7. Recommended state effect

**Recommended effect: promote the literal uniform fixed-\(q\) row theorem
and its fixed/polylogarithmic short-shell corollary after the conductor's
ordinary seam check; retain the polynomial fixed-\(a\) Gram as open.**

The promotable internal statement is (104.H1)--(104.H3), with the exact
profile and owner hypotheses of Section 2 and the collapsing-edge
qualification (104.H18)--(104.H20).  Its decisive inputs are the
homogeneous actual factorisation, collar ratio \(JD/(AL)\), odd nonzero
reciprocal mode and the two complete metric Fourier half-moments.  Record
that it is false for arbitrary phase-conjugated \(k\)-coefficients and
does not assert an unsigned theorem.

Record (104.H4)--(104.H5) as the exact consequence.  It proves the
frozen Gram target on fixed shells and every prescribed
polylogarithmic shell after epsilon absorption, but the
pointwise-row/Cauchy route has an exact \(D^2\) ceiling on polynomial
shells.  This ceiling is not an actual polynomial-shell obstruction:
no lower bound or failure of the literal Gram is proved.

Do not promote M9-M2-primitive-ray-fixed-a-actual-Gram on its full
range, M9-M2-top-endpoint-density-discrepancy-energy, M9-M2, M9,
endpoint uniformity or any Gauss-circle exponent.  No external
dependency and no actual-symbol obstruction should be added.  The next
strict survivor is the complete polynomial-shell signed \(q\)-correlation
(104.H28), with all moving modes and owners retained.
