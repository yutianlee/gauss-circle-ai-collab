# Round 118 prescribed-centre wave hostile/source audit

## 1. Result

**Verdict.** The full estimate
\[
 \mathscr R_{D,L}(X)\ll_\varepsilon X^{1/4+\varepsilon}
\]
is not proved, no strict target-safe subrange follows from the audited
one-variable methods, and no literal coherent counterexample survives the
required complement control. The prescribed-centre strategy therefore
remains open, but only at a smaller and more explicit signed interface.

Two rigorous scoped results are available.

**Flat-row curvature lemma.** For every accepted flat smooth component,
with its literal \(q_L\), \(W\), and \(\chi _4\), the reciprocal row obeys
\[
 |\mathscr R_{D,L}(X)|
 \ll_\varepsilon
 \left(\sqrt{\frac{XL}{D}}+\sqrt{\frac{X}{LD}}\right)X^\varepsilon.
 \tag{118.H1}
\]
Together with the absolute product-window capacity, this gives
\[
 |\mathscr R_{D,L}(X)|
 \ll_\varepsilon X^\varepsilon
 \min\!\left\{\frac DL,\sqrt{\frac{XL}{D}}
                 +\sqrt{\frac{X}{LD}}\right\}.
 \tag{118.H2}
\]
Writing \(q=\delta-\ell\), the leading exponent in (118.H2) is
\[
 \min\!\left\{q,\frac{1-q}{2}\right\}.
 \tag{118.H3}
\]
The strict residual hypotheses imply \(1/4<q<1/2\), so (118.H3) is
strictly larger than \(1/4\) everywhere. Thus the rowwise
second-derivative estimate followed by the \(k\)-triangle has **no**
target-safe strict subrange. It does give a quantified saving over
absolute capacity precisely when \(q>1/3\), of exponent
\[
 \frac{3q-1}{2}.
 \tag{118.H4}
\]
This is a bound for the actual row, but it is not a character-specific
gain: deleting \(\chi _4\) leaves the same curvature estimate.

**Fixed-step central-run no-go.** Let \(I\) be a consecutive interval of
integers \(d\asymp D\). Suppose odd integers \(r_d\) satisfy
\[
 r_{d+1}-r_d=4m\quad(d,d+1\in I),\qquad
 |X-r_dd|\leq C\frac DL .
 \tag{118.H5}
\]
Then
\[
 |I|\ll_C 1+\sqrt{\frac{D^3}{XL}}.
 \tag{118.H6}
\]
Consequently even a perfectly aligned run on which \(\chi _4(r_d)\) is
constant and the central wavelet has a common direction contributes at
most
\[
 X^\varepsilon\!\left(1+X^{(3\delta-1-\ell)/2}\right)
 =o(X^{1/4+\varepsilon})
 \tag{118.H7}
\]
in the strict region. This rules out the proposed fixed-multiple-of-four
run as a target-sized lower-bound mechanism. It does not bound a
disconnected selector or a selector whose multiple-of-four step changes;
those, together with the noncentral shoulders and the uncontrolled
complement, form the remaining signed survivor.

No audited primary theorem estimates that survivor with the literal
moving divisor cutoff, fixed real centre, profiles, and pointwise norm.

## 2. Exact statement and hypotheses

Let \(X\) be a large real number and
\[
 D=X^\delta,\qquad L=X^\ell,\qquad
 \frac14\leq\delta<\frac12,\qquad
 0\leq\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463.
 \tag{118.H8}
\]
Put
\[
 R=\frac XD,\qquad K=\frac{XL}{D^2},\qquad
 \Delta=\frac DL.
\]
The audit concerns one frozen flat smooth component for which \(W\) is
supported on \(r\asymp R\), \(q_L\) is real, nonnegative, supported on
\(h\asymp L\), and the normalized derivative or bounded-variation norms
of both profiles are \(X^{o(1)}\). The inherited Vaaler height taper is
part of \(q_L\), not discarded. With \(e(t)=e^{2\pi i t}\),
\[
 \mathcal Q_L(y)=\int_0^\infty \frac{q_L(h)}h e(hy)\,dh
 \tag{118.H9}
\]
and the accepted normalized wave is
\[
 \mathscr R_{D,L}(X)=
 \sum_s\sum_{\substack{r\mid s\\r\ {\rm odd}}}
 \chi _4(r)W\!\left(\frac{X}{rD}\right)
 \mathcal Q_L\!\left(\frac{r(X-s)}{4X}\right).
 \tag{118.H10}
\]
Its accepted reciprocal-row form is
\[
 \mathscr R_{D,L}(X)=
 \sum_{r\ {\rm odd}}\chi _4(r)W\!\left(\frac{X}{rD}\right)
 \sum_k\frac{q_L(4Xk/r^2)}k e\!\left(\frac{Xk}{r}\right),
 \tag{118.H11}
\]
modulo only the already accepted flat-smooth normalization and
target-safe aggregate stationary remainder. The support in (118.H11)
has \(r\asymp R\), \(k\asymp K\). The physical M2 component carries the
constant \(-i/(2\pi)\); it changes neither an absolute bound nor an
exponent, but it rotates any proposed positive real contribution.

Claims (118.H1)--(118.H7) apply only to this flat smooth owner. Sharp,
starred, clipped-top, hard, arithmetic-owner, and profile-crossing
endpoints are excluded unless their exact finite kernels are inserted.
The conjugate physical frequency satisfies the same absolute estimate.

For the run lemma, the fixed-step condition in (118.H5) is essential. It
is exactly the candidate mechanism in which the nearest admissible
\(r_d\) advances by one fixed multiple of four. Merely requiring
\(r_d\bmod 4\) to be constant does not force the step to be fixed and is
not covered by (118.H6).

## 3. Proof or derivation

**Literal normalization and capacity.** On the product side,
\(\mathcal Q_L(y)=O(1)\) for the normalized profiles, and rapid decay
restricts \(|s-X|\) to \(\Delta X^{o(1)}\). For each \(s\), the literal
inner sum has at most \(\tau(s)\) terms. Hence
\[
 |\mathscr R_{D,L}(X)|\ll_\varepsilon \Delta X^\varepsilon.
 \tag{118.H12}
\]
This count is made before any Cauchy inequality and contains every
divisor multiplicity. No hidden square-root normalization is available.
The exact product/row equivalence is the accepted \(k\)-Poisson identity;
it preserves \(q_L\), \(W\), \(\chi _4\), and the centre \(X\). Applying
the inverse transform again returns the same packet and capacity rather
than a positive or shorter coefficient.

**Proof of the curvature lemma.** For fixed \(k\asymp K\), set
\[
 w_k(r)=W\!\left(\frac{X}{rD}\right)
        q_L\!\left(\frac{4Xk}{r^2}\right).
\]
On its \(r\asymp R\) support, \(w_k\) has uniformly bounded total
variation up to \(X^\varepsilon\). Extend \(\chi _4\) by zero on even
integers and use the exact additive resolution
\[
 \chi _4(r)=\frac{e(r/4)-e(-r/4)}{2i}.
 \tag{118.H13}
\]
The two phases are
\[
 f_\pm(r)=\frac{Xk}{r}\pm\frac r4,\qquad
 |f_\pm''(r)|=\frac{2Xk}{r^3}
 \asymp\frac{LD}{X}=:\lambda .
 \tag{118.H14}
\]
The weighted second-derivative estimate, followed by partial summation
for \(w_k\), gives
\[
 \sum_r\chi _4(r)w_k(r)e(Xk/r)
 \ll_\varepsilon
 \left(R\sqrt{\lambda}+\lambda^{-1/2}\right)X^\varepsilon
 =
 \left(\sqrt{\frac{XL}{D}}+
       \sqrt{\frac{X}{LD}}\right)X^\varepsilon.
 \tag{118.H15}
\]
Since \(q_L(4Xk/r^2)\) restricts \(k\asymp K\) and
\(\sum_{k\asymp K}k^{-1}=O(1)\), taking the \(k\)-sum absolutely proves
(118.H1). For \(L\geq1\), its first term dominates. Combining it with
(118.H12) proves (118.H2).

Now \(q=\delta-\ell>1/4\) by
\(\ell<\delta-1/4\), while \(q<1/2\) by
\(\delta<1/2\) and \(\ell\geq0\). Therefore both \(q\) and
\((1-q)/2\) exceed \(1/4\). Comparing the two bounds gives
\((1-q)/2<q\) exactly when \(q>1/3\), and the difference from the
capacity exponent is (118.H4). This proves all exponent assertions. At,
for example, \((\delta,\ell)=(3/8,0)\), the capacity exponent is \(3/8\)
and (118.H1) gives \(5/16\), still not \(1/4\).

**Proof of the fixed-step run no-go.** Put \(F(d)=X/d\). The product
residual in (118.H5), with \(d\asymp D\), implies
\[
 |F(d)-r_d|\ll_C \frac1L.
 \tag{118.H16}
\]
The fixed-step condition makes \(d\mapsto r_d\) affine. On the dyadic
interval,
\[
 F''(d)=\frac{2X}{d^3}\asymp\frac{X}{D^3}.
 \tag{118.H17}
\]
Compare the two endpoints and a midpoint of any subinterval of length
\(T\). Strict convexity gives a second affine difference
\(\gg T^2X/D^3\), whereas the affine approximant contributes zero and
the three errors in (118.H16) contribute \(O_C(1/L)\). Thus
\[
 \frac{T^2X}{D^3}\ll_C\frac1L,
\]
with an added \(O(1)\) for integer endpoints, proving (118.H6).
Moreover \(W\) and \(\mathcal Q_L\) are \(O(X^\varepsilon)\), so the
whole selected run is bounded by its length. Since
\[
 \frac{3\delta-1-\ell}{2}<\frac14
\]
for \(\delta<1/2\), (118.H7) follows. This conclusion holds for either
constant character sign. Independently, selecting only this run could
never prove a lower bound for (118.H10) without controlling every
remaining active pair.

**Exact centre, ties, and arithmetic strata.** If \(X\notin\mathbb Z\),
there is no exact term \(s=X\). If \(X\in\mathbb Z\), that term is
\[
 \mathcal Q_L(0)
 \sum_{\substack{r\mid X\\r\ {\rm odd}}}
 \chi _4(r)W\!\left(\frac{X}{rD}\right)
 \ll_\varepsilon X^\varepsilon,
 \tag{118.H18}
\]
so it is target-negligible.

An exact tie between the two nearest odd integers to \(X/d\) requires
\(X/d\) to be an even integer. It is therefore divisor-sparse when it
exists. Its two residuals have size \(\asymp d\asymp D\), so for
\(L\to\infty\) they lie outside the central \(D/L\) window. When \(L\)
is bounded, the exact relation
\(\mathcal Q_L(-y)=\overline{\mathcal Q_L(y)}\) holds because \(q_L\)
is real, and the two odd integers have opposite \(\chi _4\)-signs.
The \(r\)-dependent argument and \(W\)-weight prevent an automatic exact
cancellation or a positive pair, but the exact-tie set remains
divisor-bounded.

For a sufficiently small fixed \(c_0>0\),
\[
 \left|\frac{r(X-s)}{4X}\right|\leq \frac{c_0}{L}
 \quad\Longrightarrow\quad
 \Re\mathcal Q_L\!\left(\frac{r(X-s)}{4X}\right)>0
 \tag{118.H19}
\]
on a nonzero profile core: this follows directly by keeping
\(\cos(2\pi h y)\) positive on \(h\asymp L\). This is only a
near-centre common real direction. The two character residues, the
imaginary part, the physical factor \(-i/(2\pi)\), and the entire
complement remain. Hence (118.H19) is not positivity of the full wave.

For \(s=p,p^2,p^4\asymp X\) with \(p\) prime, the possible divisors are
too sparse. In the strict region,
\[
 R=X^{1-\delta},\qquad \frac12<1-\delta<\frac34,
\]
where the upper endpoint \(3/4\) cannot occur because the strict
\(\ell\)-condition forces \(\delta>1/4\). Thus none of
\(\{1,p\}\), \(\{1,p,p^2\}\), or
\(\{1,p,p^2,p^3,p^4\}\) lies on the required \(R\)-scale for all large
\(X\), apart from excluded endpoint/profile coincidences. Arbitrary
squares, fourth powers, and highly composite \(s\) may have an active
divisor, but their contribution for one \(s\) is still
\(O_\varepsilon(X^\varepsilon)\). Across the whole window this recovers
only (118.H12), with no sign conclusion. In particular these tests do
not complete the truncated coefficient to \(r_2(s)/4\).

**Actual symbol, both signs, and source fit.** The additive resolution
(118.H13) shows that the literal character has been retained. However,
the linear quarter shifts do not change \(f''\), so (118.H1) would also
hold for the same reciprocal phase with an unsigned bounded profile.
Conversely, a phase-conjugated artificial coefficient can destroy the
oscillation, but it is not the literal coefficient and cannot falsify
(118.H10). The negative physical frequency is the conjugate packet and
obeys the same bound; it is not an independent cancellation theorem.

No audited source passes the coefficient-and-norm test:

- Popov's Theorem 5 is a truncated Voronoi formula for the **complete**
  coefficient \(r_2(n)\), the complete initial range \(n\leq N\), and
  the real cosine combination. At the packet cutoff its stated error is
  \((D/L)X^{o(1)}\); at \(N\asymp X^{1/2}\) it returns to the full Gauss
  target. It has no estimate for (118.H10). See the
  [official Math-Net record](https://www.mathnet.ru/eng/rm10162).
- Ivić--Zhai study \(\Delta(x+U)-\Delta(x)\) for the complete divisor
  problem, not the moving, profile-truncated \(\chi _4\)-divisor
  orientation or its fixed-centre complex wave. The first coefficient
  hypothesis already fails. See
  [arXiv:1209.0872](https://arxiv.org/abs/1209.0872).
- Matomäki--Shao--Tao--Teräväinen prove, for \(d_2\) in all intervals of
  length at least \(X^{1/3+\varepsilon}\), uniformity of
  \(d_2-d_2^\sharp\) against bounded-complexity nilsequences, with a
  bound of interval length times logarithmic saving. Here the
  coefficient is neither \(d_2-d_2^\sharp\) nor complete, \(\Delta\)
  may be below \(X^{1/3}\), and even in the overlap an
  \(\Delta\log^{-A}X\) estimate does not supply the required power.
  See [arXiv:2204.03754](https://arxiv.org/abs/2204.03754).
- Kiral--Zhou give Voronoi identities for coefficients of fixed
  \(L\)-functions and additive twists. The centre- and profile-dependent
  truncated divisor coefficient in (118.H10) is not such a fixed
  coefficient, and a transform identity is not a pointwise estimate.
  See [arXiv:1508.01985](https://arxiv.org/abs/1508.01985).
- The exact Tao--Trudgian--Yang exponent-pair theorem audited in Round
  107 is one-dimensional. Its lawful rowwise application does not prove
  a cell in the strict residual region, and it does not accept the
  irregular product-grouped coefficient.

The Round-117 prescribed-centre wave supports only the algebraic warning
that transform inversion can return the same kind of product fibre. Its
scales, norms, and proved savings differ; no Round-117 exponent has been
used in (118.H1)--(118.H7).

## 4. First doubtful or unproved step

After the exact row/product equivalence and the elementary bound
(118.H2), the first unproved analytic step is a genuinely joint estimate
\[
 \sum_{k\asymp K}\frac1k
 \sum_{r\asymp R}\chi _4(r)
 W\!\left(\frac{X}{rD}\right)
 q_L\!\left(\frac{4Xk}{r^2}\right)
 e\!\left(\frac{Xk}{r}\right)
 \ll_\varepsilon X^{1/4+\varepsilon}.
 \tag{118.H20}
\]
It must use the coupled \(k,r\) profile or the literal sparse
product-selector structure before taking the \(k\)-triangle. A theorem
for arbitrary coefficients is impossible, while a theorem for complete
\(d_2\) or \(r_2/4\) has the wrong coefficient.

Equivalently, one needs a decomposition of the active \(s=rd\) selector
that controls both character residues, every noncentral shoulder, every
step-change run, and the complement in one norm. The remaining power
over the target after (118.H2) is
\[
 X^{\,\min\{q,(1-q)/2\}-1/4}.
 \tag{118.H21}
\]
No inverse theorem for the residual non-affine selector, and no primary
source theorem with the literal hypotheses, has been supplied.

Separately, extending any flat-smooth conclusion to sharp, starred,
hard, clipped, or arithmetic-owner packets remains unproved until their
exact kernels and aggregate boundary errors are transported. That seam
is outside (118.H20), not silently absorbed by it.

## 5. Control tests and outcomes

Here PASS means that the audit control was carried out without changing
the literal object; it does not mean the quarter target was proved.

| Control | Outcome | Verdict |
|---|---|---|
| Literal wave and physical normalization | The accepted row and product forms retain \(q_L,W,\chi _4\), the real centre, and the physical factor \(-i/(2\pi)\). The factor is harmless for upper bounds but blocks naive real positivity. | PASS |
| Product/row equivalence and transform self-return | Exact accepted \(k\)-Poisson preserves the coefficient and returns a \(\Delta=D/L\) window. A second inversion supplies no contraction. | PASS / no gain |
| Exact centre and exact tie | The exact centre and exact nearest-odd ties are divisor-bounded; growing \(L\) also pushes ties outside the central window. Neither is a countermodel. | PASS |
| Near-centre kernel sign | A sufficiently small core has positive real part, but not a positive full complex wave after character signs, physical rotation, and complement. | PASS for local sign; FAIL as lower bound |
| Prime, prime-square, prime-fourth-power, divisor-rich strata | Prime-power tests have no divisor on the strict \(R\)-scale; general divisor-rich values reproduce only \(\Delta X^\varepsilon\). No \(r_2/4\) completion follows. | PASS |
| Coherent run selector | A consecutive fixed-step multiple-of-four run has length (118.H6) and is target-negligible even before cancellation. | PASS: named mechanism rejected |
| Complement cancellation | No proposed coherent subset controls the remaining active pairs. Therefore no subset produces a rigorous lower bound or literal counterexample. | FAIL |
| Character residue and both physical signs | Both quarter shifts give the exact \(\chi _4\); the conjugate frequency is bounded identically. Curvature gain is not character-specific. | PASS / limited |
| Capacity before and after norms | Product divisor count gives \(\Delta X^\varepsilon\); rowwise van der Corput plus the exact \(k^{-1}\)-mass gives (118.H1), with no hidden Cauchy loss. | PASS |
| Actual symbol versus unsigned/adversarial models | The actual row is bounded, but neither an unsigned model nor a phase-conjugated artificial coefficient proves or refutes the literal wave. | PASS |
| Strict residual exponent region | \(1/4<\delta-\ell<1/2\); (118.H2) never reaches \(1/4\), and improves capacity only for \(\delta-\ell>1/3\). | PASS; target FAIL |
| Profile support and endpoint kernels | The proof is uniform for frozen flat smooth profiles. Sharp/starred/hard/clipped/arithmetic-owner kernels were not supplied and are not covered. | FAIL for endpoint extension |
| External theorem hypotheses | Popov, short-interval divisor uniformity, general Voronoi, and one-dimensional exponent-pair results all fail at the coefficient, range, pointwise norm, or power-saving hypothesis. | FAIL: no matching theorem |
| Round-117 transfer | Only exact algebraic self-return is transferred; no exponent or norm estimate is imported. | PASS |
| Downstream scope | Nothing here closes all UNBAL, TOP, BAL, M9-M2, M9, or the Gauss-circle quarter target. | PASS |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

The audit read the frozen brief and only its authorized context:

- protocol.md
- state/proof_obligations.yml
- state/active_campaign.yml
- strategy/conductor_0821_full_proof_strategy.md
- rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/synthesis.md
- rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/reports/unbalanced_product_source_hostile_audit.md
- rounds/codex-managed/m9-m2-smooth-unbalanced-divisor-recombination/reviews/conductor_round107_recombination_and_capacity.md
- rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/reviews/conductor_round117_involution_product_and_source.md
- rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/derivation_packet.md
- rounds/codex-managed/m9-m2-unbalanced-prescribed-centre-wave-gate/candidates/conductor_wave_probe.md
- sources/popov_2024_voronoi_gauss.md

The proof-obligation graph hash was checked against the brief:
\[
 \texttt{d4e626708a04680cc97b043835466948204c6e123a1dc9fd569b50377349feeb}.
\]
The relevant graph nodes leave the smooth unbalanced three-quarter
estimate and all downstream parents open.

Primary-source theorem-fit checks used the official Popov source linked
above and the primary records for Ivić--Zhai, Matomäki--Shao--Tao--
Teräväinen, and Kiral--Zhou linked in Section 3. The already authorized
Round-107 source audit supplies the exact Tao--Trudgian--Yang theorem
map. No sibling Round-118 report, shared synthesis, proof draft, or
validation matrix was read or edited.

## 7. Recommended state effect

**Retain open:** M9-M2-smooth-unbalanced-three-quarter-estimate,
M9-M2, M9, and the quarter target. Do not infer any endpoint or global
exponent improvement.

**Candidate for promotion after independent seam review:**

1. the flat-smooth curvature estimate (118.H1)--(118.H4), explicitly
   labelled as a rowwise, non-character-specific saving that improves
   absolute capacity only on \(\delta-\ell>1/3\) and never reaches the
   target in the strict region; and
2. the fixed-step central-run no-go (118.H5)--(118.H7), explicitly
   limited to consecutive runs with one fixed multiple-of-four step.

**Reject as proof routes in their present form:** exact-centre
obstruction, exact-tie obstruction, prime-power or divisor-rich
positivity, completion to \(r_2/4\), a positive-core subset without its
complement, a second transform as a norm contraction, automatic
Round-117 exponent transfer, and every audited external theorem import.

**Smallest surviving interface:** prove (118.H20), or an equivalent
whole-selector estimate, by a genuinely joint argument that gains the
power (118.H21) while retaining the actual character, profiles, fixed
real centre, both sides of the kernel, and the complement. Even a proof
of that flat-smooth interface would not by itself close sharp, hard,
balanced, top, or arithmetic-owner packets.
