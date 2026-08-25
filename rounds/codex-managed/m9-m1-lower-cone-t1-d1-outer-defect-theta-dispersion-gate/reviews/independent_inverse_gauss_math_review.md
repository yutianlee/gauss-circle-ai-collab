# Round 155 independent inverse-Gauss mathematics review

- Campaign: m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate
- Role: independent mathematics seam reviewer
- Starting graph SHA-256: 84bbcb3413936c9b672c829cdba97b8d0bde69f7a6df677b61f24e9ec27e243a
- Allocation: 100% analytic/algebraic; 0% numerical

## 1. Result

The complete \(v\)-resummation lemma (155.CI4)--(155.CI9) is correct.  For every odd \(d\mid N\), with

\[
q=4N,\qquad c=q/d,\qquad H=c/2,
\]

the complete \(v\bmod H\) transform exactly inverts the Round-154 quadratic Gauss completion and returns the original \(d=(h,N)\) selector stratum.  There is no residual \(c^{-1/2}\), \(d^{-1/2}\), or \(N^{-1/2}\) gain.

The discovery report's sampled-Parseval identity, zero-mode powers, literal-mask scope, and route-only implications are also correct.  Its flat-\(j\) localization is correct when the centered variable \(a_*\) in (155.R44) is read as a signed lift on the circle \(\mathbb Z/c\mathbb Z\); that circular arc includes both its near-\(c\) portion and the portion wrapping through \(a=0\).  No frequency branch may be discarded.

## 2. Exact statement and hypotheses

Let \(N\) be arbitrary, \(d\mid N\) odd, \(q=4N\), \(c=q/d\), and \(H=c/2\).  Then \(c\equiv0\pmod4\), including for even or highly composite \(N\).  For an arbitrary finite coefficient \(B_j\) on \(\mathbb Z/q\mathbb Z\), define

\[
\widehat B_j(2dv)
=\sum_{x\bmod q}B_j(x)e_q(-2dvx)
=\sum_{x\bmod q}B_j(x)e_c(-2vx).
\]

For \(a\in(\mathbb Z/c\mathbb Z)^*\), use

\[
\kappa_c(a)=\epsilon_a\left(\frac ca\right),\qquad
K(-v^2,-j;c)
=\sum_{a\bmod c}^{*}\kappa_c(a)e_c(-\bar a v^2-aj).
\]

The exact identity to review is

\[
\sum_{v\bmod H}\widehat B_j(2dv)K(-v^2,-j;c)
=\frac{1-i}{2}\sqrt c
\sum_{x\bmod q}B_j(x)
\sum_{a\bmod c}^{*}\chi_4(a)e_c(a(x^2-j)).
\tag{155.IR1}
\]

It is pointwise in \(j\) and requires no smoothness or estimate.  Consequently the literal zero extension, actual profile, strict dyadic mask, both defect signs, asymmetric cell, transitions, hard endpoints, and exact residual phase remain inside \(B_j\).  The selected linearization is not moved to the off-congruence ambient array.

## 3. Independent proof and normalization audit

### Half-period and half-Gauss sign

For

\[
I_c(a,x)=\sum_{v\bmod H}e_c(-\bar a v^2-2xv),
\]

the change under \(v\mapsto v+H\) is

\[
-\bar a v-\bar a\,\frac c4-x\in\mathbb Z.
\]

Thus \(H=c/2\) is an exact period, and the complete sum modulo \(c\) is twice \(I_c(a,x)\).  Completing the square gives

\[
-\bar a v^2-2xv
\equiv-\bar a(v+ax)^2+ax^2\pmod c.
\]

With \(A\equiv-\bar a\pmod c\), the all-parity Gauss formula therefore yields

\[
I_c(a,x)
=\frac{1+i}{2}\epsilon_A^{-1}
\left(\frac cA\right)\sqrt c\,e_c(ax^2).
\tag{155.IR2}
\]

### Epsilon and Kronecker multiplier

Because \(\bar a\equiv a\pmod4\), \(A\equiv-a\pmod4\).  The real character \(u\mapsto(c/u)\) is nonzero on units and satisfies

\[
\left(\frac cA\right)
=\left(\frac c{-\bar a}\right)
=\left(\frac c{\bar a}\right)
=\left(\frac ca\right).
\]

For \(a\equiv1\pmod4\), the epsilon product is \(-i\); for \(a\equiv3\pmod4\), it is \(i\).  Hence exactly

\[
\epsilon_a\left(\frac ca\right)
\epsilon_A^{-1}\left(\frac cA\right)
=-i\chi_4(a).
\tag{155.IR3}
\]

Equivalently,

\[
I_c(a,x)=\frac{1-i}{2}\kappa_c(a)\sqrt c\,e_c(ax^2),
\]

and \(\kappa_c(a)^2=\chi_4(a)\).  Expanding \(\widehat B_j\) and \(K\), then inserting this identity, proves (155.IR1) with the asserted sign.

### Fourier, selector, and \(dc=q\) cancellation

The exact Round-154 \(d\)-stratum is

\[
-\frac{i(1+i)}{2Nq}\chi_4(d)d\sqrt c
\sum_{v\bmod H}\widehat B_j(2dv)K(-v^2,-j;c).
\]

Substitution of (155.IR1) gives the constant

\[
-\frac{i(1+i)}{2Nq}\,
d\sqrt c\,\frac{1-i}{2}\sqrt c
=-\frac{i}{2N}\frac{dc}{q}
=-\frac{i}{2N}.
\]

There is no missing factor of two: \(v\) runs over the unique range \(c/2=q/(2d)\), exactly parametrizing \(b=2dv\bmod q\).  Odd residues \(h\bmod q\) are partitioned uniquely by

\[
d=(h,N),\qquad h=da,\qquad
a\in(\mathbb Z/(4N/d)\mathbb Z)^*.
\]

This remains true when \(d\) and \(N/d\) are not coprime.  Moreover
\(\chi_4(h)=\chi_4(d)\chi_4(a)\) and
\(e_q(h(x^2-j))=e_c(a(x^2-j))\).  Summing all odd \(d\mid N\) therefore restores

\[
-\frac{i}{2N}
\sum_{\substack{h\bmod4N\\h\ {\rm odd}}}
\chi_4(h)e_{4N}(h(x^2-j))
={\bf1}_{N\mid x^2-j}
\chi_4\!\left(\frac{x^2-j}{N}\right).
\]

This proves exact inverse-Gauss self-return for arbitrary \(N\).

### Sampled Parseval and zero mode

Since

\[
\widehat B_j(2dv)
=\sum_{r\bmod H}C_{j,d}(r)e_H(-vr),\qquad
C_{j,d}(r)=\sum_{\substack{x\bmod q\\x\equiv r\pmod H}}B_j(x),
\]

Parseval gives exactly

\[
\sum_{v\bmod H}|\widehat B_j(2dv)|^2
=H\sum_{r\bmod H}|C_{j,d}(r)|^2.
\]

The folds are \(x-y\equiv0\pmod{2N/d}\), not merely the physical diagonal.  On an \(x\)-span \(O(K)\), their multiplicity is
\(O(1+dK/N)\), giving

\[
\sum_{v\bmod H}|\widehat B_j(2dv)|^2
\ll_\varepsilon
\left(\frac{N^{3/2}}{dM}+\frac{N}{M^{1/2}}\right)X^\varepsilon.
\]

For \(v=0\), DFI gives
\(|K(0,-j;c)|\le(j,c)^{1/2}c^{1/2}\tau(c)\).  The factor
\(d\sqrt c\,c^{1/2}/(Nq)\) is \(1/N\), and
\(|\widehat B_j(0)|\ll KM^{-3/4}X^\varepsilon\).  Summing
\((j,c)^{1/2}\) over the block and all \(d\) yields

\[
|\mathcal T_{0,U}(V)|
\ll_\varepsilon
\left(N^{-1/2}M^{-1/4}V+M^{-1/4}\right)X^\varepsilon.
\]

At \(V=K\), this is \(M^{1/4}+M^{-1/4}\), an upper bound rather than a signed lower bound.

## 4. First doubtful or unproved step

The exact inversion proves no estimate for a proper \(v\)-subfamily.  With a cutoff \(\eta\), completing the square translates it to
\(\eta(u-ax)\); the coefficient remains coupled in \(a\) and \(x\).  The first open step is therefore a genuinely signed estimate for this incomplete, nonseparable kernel, or an equivalent selected cross-fibre theorem, with \(v=0\), every fold, both signs, all \(d\), and every literal endpoint restored.

The flat-\(j\) calculation introduces no hidden gain.  From

\[
\left\|\frac ac+\frac1{2\sqrt{x^2-j}}\right\|_{\mathbb R/\mathbb Z}
\ll \frac1V,
\]

and \(|j|\le x\asymp K\), the replacement of the second term by \(1/(2x)\) costs \(O(K^{-2})\), below \(1/V\).  On the circle this is one arc centered at
\(a/c\equiv-1/(2x)\pmod1\), of total capacity \(O(1+c/V)\).  In standard positive representatives it has two visible pieces:

\[
0<\frac ac\lesssim\frac1V-\frac1{2x},
\qquad\text{and}\qquad
\left|\frac{a_*}{c}-\frac1{2x}\right|\lesssim\frac1V,
\quad a=c-a_*.
\]

The first is the wrap through \(a=0\); the second is the centered negative-frequency piece.  Equation (155.R44) is valid with \(a_*\) taken as a signed lift.  Reading it only with \(0<a_*<c\) would omit the wrapped piece, so that convention must be retained in any later state text.  Either representation gives only the stated arc capacity and leaves the mask and endpoints in \(B_j\).

The hypothetical square-root incidence size
\(M^{-3/4}V^{1/2}\) is target-sized only for \(V\le M^{3/2}\).  No such cancellation is proved, and no second mechanism above that range is supplied.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| \(c/2\) period | GREEN.  The shift changes the phase by an integer and the complete Gauss sum is exactly twice the half sum. |
| Half-Gauss phase and sign | GREEN.  \(A=-\bar a\) and the linear term \(-2x\) give \(e_c(ax^2)\) and the factor \((1-i)/2\). |
| Epsilon/Kronecker identity | GREEN.  Both unit classes modulo four give (155.IR3); no primitive or odd-\(N\) assumption is inserted. |
| Fourier and selector factors | GREEN.  The \(1/q\), \(-i/(2N)\), \(d\sqrt c\), and \(\sqrt c/2\) factors restore exactly to the quotient selector. |
| \(dc=q\) and gcd strata | GREEN.  Every odd \(d=(h,N)\), including noncoprime factorizations and all two-adic content in \(c\), is present. |
| Literal mask and linearization scope | GREEN.  The inverse calculation is pointwise in \(j\) and arbitrary in exact \(B_j\); the selected linearization is never charged on ambient points. |
| Sampled Parseval folds | GREEN.  The period is \(H=2N/d\), and the large-\(d\) folds are retained in the exact norm. |
| Zero mode | GREEN/scoped obstruction.  Its complete \(N\)-\(M\)-\(V\)-\(d\) power is the displayed upper bound; it is neither omitted nor called a lower bound. |
| Flat-\(j\) reciprocal arc | GREEN with signed-lift convention.  The circular arc wraps through zero; both positive-representative pieces are retained and have total \(O(1+c/V)\) capacity. |
| Complete versus truncated transform | GREEN/no gain.  Complete resummation self-returns; every proper cutoff remains nonseparable. |
| Downstream implication | GREEN.  No positive-power owner, \(M\)-range, \(D>1\), \(L>1\), generic \(t=1\), original \(t\ge2\), cross, M2, endpoint assembly, M9, bridge, target, or exponent conclusion follows. |

## 6. Dependencies and exact artifacts used

This review read only:

1. protocol.md;
2. state/active_campaign.yml;
3. rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/candidates/conductor_round155_complete_v_inverse_gauss.md;
4. rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reports/outer_defect_spectral_dispersion_attack.md; and
5. rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_root_dispersion_adjudication.md, specifically its exact normalized expression (154.CA22a).

No web source, sibling Round-155 report, proof graph, strategy, barrier packet, computation, or numerical experiment was used.

## 7. Recommended state effect and verdict

Promote, subject to the remaining terminal gates, only:

- the exact inverse-Gauss identity (155.CI4)--(155.CI9);
- complete \(v\)-resummation as a route-scoped self-return, not an estimate;
- sampled Parseval with its \(2N/d\) folds; and
- the zero-mode formula as an upper power ledger.

Retain every incomplete-\(v\), nonseparable signed outer-\(j\), selected cross-fibre, spectral, and positive-power-range problem as open.  If the flat-\(j\) arc is transcribed later, state explicitly that \(a_*\) is a signed lift, or print both wrapped pieces; do not silently delete the near-zero portion.  Make no downstream theorem or exponent change.

First exact defect: none.

GREEN
