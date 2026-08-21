## 1. Result

There are two separate conclusions.

First, the proposed maximal estimate has the stated Gram consequence by an exact one-count. If, for every permitted $a\asymp A$,

\[
\mathcal M_a(D)\ll_\varepsilon X^\varepsilon\frac{L^2}{A},
\]

then for $H\asymp D$,

\[
\mathcal G_H^{\rm act}
\ll_\varepsilon X^\varepsilon\frac{DL^4}{A}
\asymp X^\varepsilon\frac{H^2L^4}{AD}.
\]

The logical hierarchy is

\[
\text{total variation per row}
\Longrightarrow \text{bounded maximal partial sums per row}
\Longrightarrow \text{the direct Gram target}. \tag{1.1}
\]

Both arrows are one-way. In particular, the Gram target is an averaged square estimate and is strictly less information than a uniform maximal theorem.

Second, (105.B1) does not follow from the supplied fixed-row estimate and the verbal list of retained features. An arbitrary same-size coefficient can conjugate the outer sign: the coefficient shadow $F_a(q)=(-1)^qL^2/A$ has maximal alternating sum of order $DL^2/A$. This is a counterexample only to a coefficient-uniform analogue, not to the exact actual-symbol theorem. The packet supplies no formula with which to exclude that shadow for the actual symbol.

Total adjacent-$q$ variation would be sufficient, but it is genuinely stronger than necessary and is especially ill-suited to the zero-extended primitive mask. A primitive-mask shadow can have variation of order $DL^2/A$ while its alternating maximal sum is $O(L^2/A)$. The sharp unconditional survivor from the fixed-row input is therefore only the bounded-length estimate

\[
\sup_{\substack{I\subset[D,2D)\\ |I|\le R}}
\left|\sum_{q\in I}(-1)^qF_a(q)\right|
\ll_\varepsilon R X^\varepsilon\frac{L^2}{A}.
\]

It gives (105.B1) on bounded, or after reallocating epsilon on subpolynomial-length, $q$-ranges. It gives no nontrivial fixed positive-power subrange.

## 2. Exact statement and hypotheses

Let

\[
\mathcal Q=[D,2D)\cap\mathbb Z,
\qquad
\mathcal A=\{a:a\asymp A,\ a\text{ odd and permitted}\}.
\]

Interpret the $I$ in the definition of $\mathcal M_a(D)$ as a contiguous integer interval; this is the interpretation needed by the sliding-window Gram. Assume that $F_a(q)=0$ outside $\mathcal Q$, that $\#\mathcal A\ll A$, and that $H\asymp D\ge1$. No reality or conjugacy assumption on $F_a$ is made.

The conditional counting lemma is

\[
\mathcal G_H^{\rm act}
\le (D+H+O(1))\sum_{a\in\mathcal A}\mathcal M_a(D)^2. \tag{2.1}
\]

Consequently, (105.B1), used with epsilon replaced by $\varepsilon/2$, implies the target Gram bound.

For comparison, define the literal zero-extended total variation

\[
V_a(D)=\sum_{\substack{q,q+1\in\mathcal Q}}
|F_a(q+1)-F_a(q)|.
\]

For every interval $I\subset\mathcal Q$, consecutive pairing gives

\[
\left|\sum_{q\in I}(-1)^qF_a(q)\right|
\le \sup_{q\in\mathcal Q}|F_a(q)|+V_a(D). \tag{2.2}
\]

Thus the exact total-variation statement

\[
V_a(D)\ll_\varepsilon X^\varepsilon L^2/A \tag{2.3}
\]

would imply (105.B1). Neither (2.3) nor the weaker signed paired-difference estimate is a hypothesis of the packet. The only supplied analytic estimate is the pointwise fixed-row theorem.

Writing $B_\eta=X^\eta L^2/A$, the pointwise theorem alone gives the two sharp coefficientwise bounds

\[
\mathcal M_a(D)\ll D B_\eta \tag{2.4}
\]

and

\[
\mathcal G_H^{\rm act}
\ll A D H^2 B_\eta^2
=X^{2\eta}\frac{D H^2L^4}{A}. \tag{2.5}
\]

The direct target is $X^\varepsilon H^2L^4/(AD)$, so (2.5) misses it by exactly $D^2$. The maximal theorem removes a factor $D$ at amplitude level and hence this factor $D^2$ at energy level. It is sufficient, not necessary: an averaged actual correlation estimate could prove the Gram target without proving (105.B1).

## 3. Proof or derivation

**The Gram one-count.** For fixed $a,n$, put

\[
S_{a,n}=\sum_{0\le h<H}(-1)^hF_a(n+h).
\]

After setting $q=n+h$ and using zero extension,

\[
S_{a,n}=(-1)^n
\sum_{q\in [n,n+H)\cap\mathcal Q}(-1)^qF_a(q).
\]

The intersection is a contiguous interval in $\mathcal Q$, so

\[
|S_{a,n}|\le \mathcal M_a(D).
\]

It is nonzero only if $[n,n+H)$ meets $\mathcal Q$. There are at most $D+H+O(1)$ such integers $n$. Summing first in $n$ proves (2.1). Since $\#\mathcal A\ll A$, (105.B1) at exponent $\varepsilon/2$ gives

\[
\mathcal G_H^{\rm act}
\ll AD\left(X^{\varepsilon/2}\frac{L^2}{A}\right)^2
=X^\varepsilon\frac{DL^4}{A}.
\]

For $H\asymp D$, one has $D\asymp H^2/D$, which is exactly the advertised canonical scale. This derivation uses neither a real-part shortcut nor a density/discrepancy split.

**The weaker direct Gram formulation.** Cauchy--Schwarz in the $h$-sum, followed by the exact multiplicity with which each $q$ occurs in the sliding windows, gives

\[
\begin{aligned}
\mathcal G_H^{\rm act}
&\le H\sum_{a,n}\sum_{0\le h<H}|F_a(n+h)|^2\\
&=H^2\sum_{a,q}|F_a(q)|^2
\ll A D H^2 B_\eta^2,
\end{aligned}
\]

which is (2.5). Equivalently, expanding the square before summing over $n$ gives the exact correlation identity

\[
\mathcal G_H^{\rm act}
=\sum_{|r|<H}(H-|r|)(-1)^r
\sum_{a,q}F_a(q)\overline{F_a(q+r)}, \tag{3.2}
\]

with zero extension understood. Thus a proof of the weighted *aggregate* in (3.2) at the target scale would suffice. It need not control the supremum of every interval sum for every $a$. Conversely, the coherent coefficient shadow $F_a(q)=(-1)^qB$ makes interior windows have size $HB$ and saturates (2.5), so the $D^2$ gap is real for arbitrary coefficients.

The converse from the Gram target to (105.B1) also fails for coefficient arrays. Put all rows except one equal to zero, and on the exceptional row set $F_a(q)=(-1)^qB$ on a contiguous permitted block of length

\[
m\le c\min(D,\sqrt A).
\]

For $H\asymp D$ the exceptional row contributes $O(Dm^2B^2)$ to the Gram, which is at most $O(ADB^2)=O(DL^4/A)$, while its maximal alternating sum is $mB$. Whenever $m\to\infty$, the direct Gram scale is compatible with failure of a uniform one-row maximal bound. This is again a coefficientwise separation, not an actual-symbol construction.

**Pairing and total variation.** If $I=\{r,r+1,\ldots,s\}$, pair consecutive terms beginning at $r$. Apart from at most one endpoint,

\[
\sum_{q\in I}(-1)^qF_a(q)
=(-1)^r\sum_j\bigl(F_a(r+2j)-F_a(r+2j+1)\bigr).
\]

The triangle inequality proves (2.2). It also shows what is actually needed: cancellation in the *sum* of transported adjacent differences. Taking absolute values of every difference, as in total variation, discards that possible cancellation.

**Why primitive total variation is too strong.** Take an odd number $a=3p$ with $p>2D$, and consider the mask-respecting shadow

\[
F^{(0)}_a(q)=B\,\mathbf 1_{(a,q)=1},
\qquad B=L^2/A.
\]

On $\mathcal Q$, coprimality is then equivalent to $3\nmid q$. Every three steps the zero-extended sequence makes two jumps of size $B$, so

\[
V^{(0)}_a(D)\asymp DB.
\]

On the other hand, the signed sequence over a period of six is

\[
0,-B,+B,0,+B,-B,
\]

whose period sum is zero and whose interval sums are bounded by $2B$. Hence total variation can lose a factor $D$ even in a model where the desired maximal alternation holds.

More generally, for a frozen underlying coefficient $C$, exact Möbius inversion gives

\[
\sum_{q\in I}(-1)^q\mathbf 1_{(a,q)=1}C
=C\sum_{d\mid a}\mu(d)
  \sum_{r:\,dr\in I}(-1)^r, \tag{3.1}
\]

because every divisor $d\mid a$ is odd. Each inner alternating interval sum is at most one. This explains how primitivity can be retained arithmetically without paying its raw variation. For a moving actual coefficient, however, (3.1) would require an exact factorization beyond the primitive mask and uniform control along every progression $q=dr$; neither is stated.

**Sharpness of the pointwise input.** Let $\mathcal Q_a$ be the permitted $q$'s for a fixed $a$, and define the coefficientwise adversary

\[
F^{\rm adv}_a(q)=(-1)^qB\,\mathbf 1_{q\in\mathcal Q_a}.
\]

It obeys the supplied magnitude bound, but on any interval containing $N$ permitted points its alternating sum is $NB$. Thus the triangle-inequality estimate $RB$ for an interval of length $R$ is sharp among coefficients with the stated size and support. When $R=X^{o(1)}$, one may split the available epsilon between $R$ and the fixed-row theorem. If $R=X^\delta$ for a fixed $\delta>0$, this loss cannot be absorbed for every epsilon. This adversary is not asserted to be an actual row.

## 4. First doubtful or unproved step

The conditional Gram implication has no unproved analytic step, subject only to the explicit conventions that $I$ is an interval and the dyadic $a$-shell has $O(A)$ integers.

The first unsupported implication from the accepted fixed-row theorem to the desired conclusion is now quantitative: pointwise control gives (2.5), whereas the direct Gram target is smaller by $D^2$. Nothing stated supplies either that energy saving or the stronger factor-$D$ maximal saving.

For the proposed (105.B1) route, the first missing literal step occurs before any estimate: the packet gives no exact summand formula for $F_a(q)$, hence no adjacent-$q$ transport identity. A usable input would have to write the full coefficient as a sum over labelled reciprocal samples and then align the labels at $q$ and $q+1$ (or $q$ and $q+2$) while displaying, rather than suppressing,

- the changing integer $k$-interval and all entry/exit terms;
- the finite odd lifts and their boundaries;
- the primitive and prior-owner masks, preferably through an exact Möbius or residue decomposition;
- floors, stars, both orientations, physical collars, and cone-edge terms; and
- the punctured density together with every discrepancy mode.

Only after such an identity is available can one try to prove either total variation or the strictly weaker paired-transport correlation

\[
\sup_{u<v}
\left|\sum_j\bigl(F_a(u+2j)-F_a(u+2j+1)\bigr)\right|
\ll_\varepsilon X^\varepsilon\frac{L^2}{A}, \tag{4.1}
\]

with the obvious endpoint convention. Equation (4.1) is essentially the minimal adjacent-pair form exposed by the outer alternation; replacing its left side by the sum of absolute differences is an unsupported strengthening. The scale relations for $K,G,\rho$, including $\rho>1$, do not by themselves provide the missing identity or a finite-difference bound.

For the weaker direct route, one could instead target the complete signed shift aggregate (3.2). That would still require the full actual formula and all masks and modes, but it would not require total variation or bounded maximal partial sums. The packet provides no bound for any nonzero shift correlation and no improved diagonal energy, so this route is also open.

## 5. Required controls and outcomes

All controls below are analytical; no numerical experiment was used.

| Control | Exact input | Expected failure or invariant | Observed outcome | Implication |
|---|---|---|---|---|
| `raw-vs-weighted` | The packet calls $F_a(q)$ the exact actual row but gives no coefficient expansion or lift multiplicities. | No raw tuple count may be promoted to a coefficient-weighted bound. | The Gram one-count acts directly on $F_a$ and makes no transfer. The maximal theorem cannot be weight-audited from the packet. | The conditional implication passes; (105.B1) remains unproved. |
| `signed-vs-unsigned` | The outer sign is exactly $(-1)^q$; any internal actual signs are hidden inside $F_a(q)$. | A signed proof must identify why absolute, random, and adversarial phases behave differently. | Same magnitudes can range from bounded alternating sums to the coherent adversary $F^{\rm adv}=(-1)^qB$, which gives size $DB$. Random signs supply no theorem, and the true internal sign cannot be inspected. | Any coefficient-uniform argument is false; an actual proof must expose the literal sign/phase law. |
| `known-lower-bound-families` | The permitted files name UNC, TS, and W-1 but do not define their tuples, parity, envelopes, or scale ranges. | Absolute or unsigned near-collision claims must be checked against them. | No absolute/unsigned near-collision claim is used in the Gram proof. A literal family test is not executable from the supplied definitions. | They neither refute nor certify this signed maximal theorem; the control remains unresolved for an actual-symbol proof. |
| `dyadic-endpoints` | $D=X^{1/4},X^{3/8},X^{1/2}$, conditional on the corresponding shell being nonempty. | Counting must remain uniform and no below-endpoint smoothing may be extrapolated. | The number of relevant $n$'s is $D+H+O(1)$ at every endpoint, so (2.1) is uniform. The pointwise loss is $D$ in maximal amplitude and $D^2$ against the direct Gram target at every endpoint. | The Gram implication passes all three; neither (105.B1) nor the direct target follows from the fixed-row theorem at any endpoint. |
| `real-vs-complex-pairing` | $F_a(q)$ may be genuinely complex and asymmetric. | No $\operatorname{Re}B_h$ shortcut without conjugacy. | The proof uses the exact complex modulus and a change of variables only. | The conditional implication is valid for real or complex rows with no symmetry assumption. |
| `exact-vs-near-resonance` | The packet says the complete punctured metric density and every discrepancy mode are retained, but supplies no exact/near decomposition. | Exact centers must not be used to control nonzero bands. | The Gram proof never splits modes. No estimate of either exact or near bands can be derived. | Modewise promotion is forbidden; a future transport identity must carry both simultaneously. |
| `coefficient-adversary` | Replace the actual row by $F^{\rm adv}_a(q)=(-1)^qB$ on permitted points. | A magnitude-only maximal theorem should fail by coherent phase conjugation. | The maximal sum is $NB$ on an interval with $N$ permitted points. | The stronger arbitrary-coefficient analogue is rejected; this is not an actual-symbol lower obstruction. |
| `support-and-degeneracy` | Half-open $q$-support and zero extension are explicit; moving reciprocal edges, $uv=0$, repeated denominators, reduced-fraction boundaries, collars, floors, and stars have no formula. | Zero extension must handle sliding-window endpoints, while moving boundary jumps must be paid in variation. | Zero extension completely settles the Gram support count. It gives no bound on boundary jumps or degeneracies in adjacent transport. | The counting seam passes; the transport seam is the first missing literal input. |
| Primitivity | $a$ is odd and $(a,q)=1$. | Raw total variation can see every primitive gap, while the alternating sum may use odd-divisor arithmetic. | The $a=3p$ shadow has $V\asymp DB$ but maximal alternation $O(B)$; (3.1) records the exact constant-coefficient Möbius cancellation. | Total variation is not necessary. A variable actual row needs progression-uniform transport after exact arithmetic decomposition. |
| Moving reciprocal fibres and finite lifts | Only $K\asymp JD/A$ and $G\asymp L/A$ are stated. | Samples must be aligned and integer entry/exit retained. | Cardinality scales alone do not define a bijection or control its boundary. | No adjacent-$q$ estimate follows. |
| Complete density and discrepancy | The packet explicitly requires the punctured density and every discrepancy mode. | Deleting the density or bounding modes separately may change cancellation. | No mode formula or summability norm is provided, so no mode may be discarded or estimated. | The proposed maximal theorem is undecided, not disproved. |
| Pell and fourth-power rows | These structured rows are required controls but are not defined in the permitted packet. | A claimed phase derivative or nonstationarity must survive them. | The fixed-row bound remains formally uniform, but it contains no adjacent-$q$ phase information. The actual rows cannot be evaluated. | No actual lower obstruction and no pass may be claimed; the exact transport formula must be tested on them. |

## 6. Dependencies and exact artifacts used

Campaign: `m9-m2-polynomial-q-maximal-alternation`. Task: `blind_maximal_q_rederivation`. Role: statement-only rederivation.

The mathematical derivation above uses only:

- `rounds/codex-managed/m9-m2-polynomial-q-maximal-alternation/blind_statement.md` for the complete stated interface, scales, fixed-row theorem, proposed maximal theorem, and Gram definition;
- `state/control_models.md` for the named controls and their reporting requirements; and
- `problems/gauss_circle.md` only for the repository's stated global problem and research scope.

The task brief `rounds/codex-managed/m9-m2-polynomial-q-maximal-alternation/briefs/blind_maximal_q_rederivation.md` was used only for procedure and report format. No web source, source theorem, symbolic computation, or numerical experiment was used.

Exposure disclosure: before the brief was parsed, `protocol.md`, `state/proof_obligations.yml`, and `state/active_campaign.yml` were mistakenly loaded together in one truncated read because of the repository-level pre-research instruction. The visible material included the Round-105 manifest and a tail of the proof graph, but no Round-105 derivation packet, candidate, sibling report, or prior-round derivation was opened. Those accidentally exposed files were quarantined from the mathematical derivation above. This report is therefore statement-derived but is not exposure-free blind evidence.

## 7. Recommended state effect

**Recommended effect: revise.** Retain the exact conditional maximal-to-Gram counting lemma (2.1) and the direct correlation identity (3.2), but do not promote (105.B1), the direct Gram target, a total-$q$-variation theorem, or any downstream M2 conclusion. Record the exact unsupported gap as $D$ in maximal amplitude and $D^2$ in direct Gram energy. Reject the coefficient-uniform analogue and reject total variation as a necessary formulation. The next proof unit should supply one exact full-symbol adjacent-$q$ transport or averaged-shift identity, including arithmetic masks, moving samples and entries/exits, and all metric modes. It may target the signed paired correlation (4.1), or the weaker aggregate (3.2), before attempting absolute variation. Until such an input exists, the only proved maximal statement is the bounded/subpolynomial interval estimate. Because of the disclosed exposure, this report should not by itself satisfy an exposure-free blind-validation gate.
