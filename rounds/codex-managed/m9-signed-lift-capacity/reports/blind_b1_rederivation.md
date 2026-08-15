# Blind rederivation of B1

## 1. Result

The proposed B1 envelope is correct for a fixed scale-normalized bounded-variation dyadic profile, and in fact under a weaker discrete cancellation hypothesis. Smoothness by itself is not enough: its norm must be uniform at dyadic scale. The exact result is as follows.

### Lemma (signed reduced-fraction lift)

Let \(D>0\), \(H=H_D\in\mathbb Z_{\ge 0}\), \(q\in\mathbb Z_{\ge1}\), and \(p\in\mathbb Z\), with \(p/q\) reduced when \(p\ne0\). Define

\[
A_\chi(p/q)=
\sum_{\substack{gq\in[D,2D)\\1\le |gp|\le H}}
\beta_{gp,H}\,w_D(gq),
\qquad
\beta_{h,H}=-\frac{\Phi(|h|/(H+1))\chi_4(|h|)}{\pi |h|}
\mathbf 1_{2\nmid h}.
\]

The \(p=0\) sum is empty. If \(p\ne0\) is even, then \(A_\chi(p/q)=0\). Suppose that \(p\) is odd. Put

\[
a=\left\lceil\frac Dq\right\rceil,
\qquad
b=\min\!\left\{
\left\lceil\frac{2D}{q}\right\rceil-1,
\left\lfloor\frac H{|p|}\right\rfloor
\right\},
\]

and let \(g_0<g_1<\cdots<g_m\) be the odd integers in \([a,b]\), when this set is nonempty. Assume the sampled twisted-discrepancy bound

\[
\max_{0\le r\le s\le m}
\left|\sum_{j=r}^{s}\chi_4(g_j)w_D(qg_j)\right|
\le C_w . \tag{TD}
\]

Then

\[
|A_\chi(p/q)|\le \frac{C_w}{\pi}\frac{q}{D|p|}. \tag{B1}
\]

It is enough to assume only the prefix version of (TD) for the actual interval; the subinterval form makes the hypothesis uniform under arbitrary support and truncation endpoints.

A convenient weight-only sufficient condition is

\[
M+V\le C_{\mathrm{BV}},\qquad
M=\max_{0\le j\le m}|w_D(qg_j)|,
\quad
V=\sum_{j=0}^{m-1}|w_D(qg_{j+1})-w_D(qg_j)|. \tag{DBV}
\]

Under (DBV), one can take \(C_w=C_{\mathrm{BV}}\). In particular, it suffices uniformly in \(D,q\) that

\[
\|w_D\|_{L^\infty([D,2D))}
+\operatorname{Var}_{[D,2D)}(w_D)\le C.
\]

Thus \(w_D(t)=W(t/D)\), with one fixed (possibly complex-valued) \(W\in BV([1,2])\), gives (B1), with the implied constant depending only on \(\|W\|_\infty+\operatorname{Var}(W)\). A fixed smooth profile is a special case. More generally, an absolutely continuous family is sufficient if

\[
\sup_D\left(\|w_D\|_\infty+\int_D^{2D}|w_D'(t)|\,dt\right)<\infty.
\]

No differentiability is needed. At the discrete level, (TD) is weaker than bounded variation and is the actual cancellation property used by B1.

## 2. Proof

The conditions \(q\ge1\) and \(D>0\) force every contributing \(g\) to be positive. The half-open dyadic condition is exactly

\[
\left\lceil D/q\right\rceil\le g\le
\left\lceil2D/q\right\rceil-1,
\]

while the Fourier truncation is exactly \(g\le\lfloor H/|p|\rfloor\). This proves the endpoint description \([a,b]\) above. If it contains no odd integer, the sum is empty.

If \(p\) is even, every \(gp\) is even, so the parity indicator in \(\beta_{gp,H}\) kills every term. Now take \(p\) odd. The surviving \(g\)'s are precisely the odd members \(g_j=g_0+2j\) of \([a,b]\). Multiplicativity of \(\chi_4\) on positive odd integers gives

\[
\chi_4(g_j|p|)=\chi_4(g_j)\chi_4(|p|),
\]

and hence

\[
A_\chi(p/q)
=-\frac{\chi_4(|p|)}{\pi|p|}
\sum_{j=0}^{m}\chi_4(g_j)w_D(qg_j)K_j,
\qquad
K_j=\frac{\Phi(g_j|p|/(H+1))}{g_j}. \tag{1}
\]

Nonemptiness implies \(1\le g_j|p|\le H\), so

\[
0<\frac{g_j|p|}{H+1}\le\frac H{H+1}<1.
\]

The Vaaler source card records that \(\Phi\) is nonnegative, at most \(1\), and decreasing on \([0,1]\). Consequently \(K_j\ge0\) and \(K_j\) is nonincreasing. Also

\[
K_0\le \frac1{g_0}\le\frac qD. \tag{2}
\]

Set \(c_j=\chi_4(g_j)w_D(qg_j)\) and \(S_j=\sum_{i=0}^j c_i\). Abel summation gives

\[
\sum_{j=0}^{m}c_jK_j
=S_mK_m+\sum_{j=0}^{m-1}S_j(K_j-K_{j+1}). \tag{3}
\]

Under (TD), \(|S_j|\le C_w\). Since the differences in (3) are nonnegative and telescope,

\[
\left|\sum_{j=0}^{m}c_jK_j\right|
\le C_w\left(K_m+\sum_{j=0}^{m-1}(K_j-K_{j+1})\right)
=C_wK_0
\le C_w\frac qD. \tag{4}
\]

Combining (1) and (4) proves (B1).

It remains to verify the advertised BV corollary. Along the odd progression, \(\chi_4(g_j)=\chi_4(g_0)(-1)^j\), whose partial sums have modulus at most one. Applying discrete summation by parts to any block \(r\le j\le s\) yields

\[
\left|\sum_{j=r}^{s}\chi_4(g_j)w_D(qg_j)\right|
\le |w_D(qg_s)|+
\sum_{j=r}^{s-1}|w_D(qg_{j+1})-w_D(qg_j)|
\le M+V.
\]

Thus (DBV) implies (TD). Ordered samples cannot have more variation than the underlying BV function, and rescaling \(t\mapsto t/D\) preserves total variation. This completes the proof.

## 3. Weight-regularity audit

The phrase “fixed smooth or bounded-variation dyadic profile” is valid only with a uniform normalization. The following distinctions are necessary.

1. **Weakest hypothesis actually used.** Uniform boundedness of the twisted partial sums (TD) on the sampled odd \(q\)-lattice. This does not require a function on the continuum at all.
2. **Natural profile hypothesis.** Uniform discrete BV, or the stronger continuum bound \(\|w_D\|_\infty+\operatorname{Var}(w_D)=O(1)\). A fixed profile \(W(t/D)\) has exactly this property.
3. **Insufficient hypotheses.** Boundedness alone is insufficient. “Smooth” without scale-normalized derivative/variation bounds is also insufficient. In the active-range example in Section 5, \(q_0=\lceil2D/H_D\rceil\) and \(w_D(t)=\sin(\pi t/(2q_0))\) is smooth and bounded, but \(w_D(gq_0)=\chi_4(g)\) at every odd lift. Its variation on a dyadic interval is \(\asymp D/q_0\asymp H_D\), not \(O(1)\).
4. **Sharp weights.** The sharp dyadic profile is allowed. On the already restricted sample interval it has \(M=1,V=0\); if extended by zero outside \([D,2D)\), it still has only bounded endpoint variation.
5. **BV jump representatives.** Point values at jumps must be the actual values used in the sum. Any choice is harmless provided its contribution is included in the pointwise total variation; no almost-everywhere identification may silently change a sampled endpoint.

## 4. Endpoint and degeneracy audit

- **\(p=0\).** The condition \(1\le|gp|\) is impossible, so \(A_\chi(0)=0\). The displayed reciprocal bound is not asserted because it contains \(|p|^{-1}\).
- **Even \(p\).** The sum vanishes term by term, including every truncation boundary.
- **Empty odd lift interval.** If \(b<a\), or \([a,b]\) contains no odd integer, then \(A_\chi=0\). In particular, \(q\ge2D\) forces emptiness.
- **Lower dyadic endpoint.** A lift with \(gq=D\) is included, exactly as encoded by \(a=\lceil D/q\rceil\).
- **Upper dyadic endpoint.** A lift with \(gq=2D\) is excluded, exactly as encoded by \(\lceil2D/q\rceil-1\).
- **Truncation endpoint.** A lift with \(g|p|=H\) is included. Its argument is \(H/(H+1)<1\), not \(1\), so the quoted formula for \(\Phi\) remains in its valid interior range. If \(H<|p|\), the sum is empty. Truncation can only shorten the odd block and does not impair either partial-sum bound.
- **One-point interval.** Abel summation reduces to the single estimate \(|\beta_{gp,H}w_D(gq)|\le M/(\pi g|p|)\le Mq/(\pi D|p|)\).
- **Negative \(p\).** Only \(|p|\) enters the amplitude and \(\chi_4(|p|)\) is a harmless unit sign.
- **Reducedness and repeated denominators.** Coprimality is not used in this individual-lift estimate. Repetition of a denominator elsewhere has no effect on the pointwise lemma.
- **Dyadic scale endpoints.** Substitution of \(D=X^{1/4},X^{3/8},X^{1/2}\) in (2) gives respectively \(K_0\le qX^{-1/4},qX^{-3/8},qX^{-1/2}\). The proof is uniform at all three scales. Any dependence of \(H_D\) only changes the exact terminal integer \(b\), possibly making the sum empty; no argument crosses or averages past \(D=X^{1/2}\).

## 5. Required control tests

### `support-and-degeneracy`

- **Input:** the exact half-open interval, the inclusive \(H\)-truncation, both parities of \(p\), \(p=0\), an empty interval, a one-point interval, sharp/BV weights, and a truncation ending on either parity.
- **Expected invariant:** all surviving lifts form one finite odd arithmetic progression, and shortening either end preserves the bounded-prefix property.
- **Observed result:** the explicit integers \(a,b,g_0,\ldots,g_m\) above cover every case. Empty and even branches vanish; endpoint and one-point branches obey B1 directly or by the same Abel identity.
- **Implication:** no unrecorded lift, zero branch, or truncation-edge term remains.

### `coefficient-adversary`

- **Input (active scaling):** take an asymptotic sequence with \(H=H_D\to\infty\), \(H/D\to0\), put \(p=1\), and choose
  \[
  q_0=\left\lceil\frac{2D}{H}\right\rceil\asymp\frac{2D}{H}.
  \]
  For all sufficiently large members of the sequence, \(H\le D/2\). Every odd integer
  \[
  \frac{3H}{5}\le g<\frac{4H}{5}
  \]
  then satisfies \(D\le gq_0<2D\) and \(g\le H\): the lower bound follows from \(q_0\ge2D/H\), while
  \[
  gq_0<\frac{4H}{5}\left(\frac{2D}{H}+1\right)
  =\frac{8D}{5}+\frac{4H}{5}\le2D.
  \]
  Thus this is a genuine subblock of the active lift interval \(g\asymp H_D\), despite \(H_D\ll D\).
- **Expected failure:** either matching the weight to the character, or replacing the coefficients by adversarial equal phases, should remove the alternating partial-sum bound and leave a positive dyadic harmonic mass.
- **Observed result (weight adversary):** retain the genuine Vaaler coefficients and prescribe \(w_D(gq_0)=\chi_4(g)\) on the odd lift progression. One smooth bounded realization is
  \[
  w_D(t)=\sin\left(\frac{\pi t}{2q_0}\right).
  \]
  Let \(c_0=\Phi(4/5)>0\). The displayed subblock contains \(\gg H\) odd integers, and on it \(\Phi(g/(H+1))\ge c_0\). Hence
  \[
  |A_\chi(1/q_0)|
  \ge \frac{c_0}{\pi}
  \sum_{\substack{3H/5\le g<4H/5\\g\ \mathrm{odd}}}\frac1g
  \gg 1,
  \]
  whereas \(q_0/D\le2/H+1/D\ll1/H\). Therefore boundedness, and even unnormalized smoothness, does not imply B1 in the active range.
- **Observed result (coefficient adversary):** with \(w_D=1\), replace the genuine coefficients on the same active lift interval by \(+|\beta_{g,H}|\). The identical lower bound \(\gg1\) holds, while the proposed envelope is \(O(q_0/D)=O(1/H)\). Thus the arbitrary-phase coefficient analogue also fails within the active scaling; no example with \(H\gg D\) is needed.
- **Implication:** B1 is genuinely signed and profile-sensitive. It uses the exact \(\chi_4\) alternation together with uniform weight regularity; neither coefficient magnitudes, \(L^\infty\) control of the weight, nor \(\Phi\)-monotonicity alone suffices.

### `dyadic-endpoints`

- **Input:** \(D=X^{1/4},X^{3/8},X^{1/2}\), with arbitrary integer \(H_D\ge0\) and the exact rounded endpoints above.
- **Expected invariant:** the proof should use only \(g_0\ge D/q\) and monotone truncation, uniformly in the scale exponent.
- **Observed result:** (2)--(4) apply verbatim at all three values. The endpoint \(X^{1/2}\) introduces no extra term.
- **Implication:** the B1 lemma itself has no dyadic endpoint loss.

All controls are analytic; no numerical experiment was used.

## 6. First doubtful or unproved step

There is no unproved step in the lemma under (TD), (DBV), or the stated uniform continuum-BV hypotheses. The first invalid step in any broader formulation is the inference

\[
|w_D|\ll1\quad\Longrightarrow\quad
\sum\chi_4(g)w_D(qg)=O(1).
\]

The active-range construction \(q_0=\lceil2D/H_D\rceil\), \(w_D(gq_0)=\chi_4(g)\), and the coefficient-adversary calculation above refute that inference even when \(H_D\ll D\). Therefore “smooth” must mean a fixed rescaled profile or carry an explicit \(O(1)\) total-variation bound.

## 7. Dependencies and exact artifacts used

- `rounds/codex-managed/m9-signed-lift-capacity/briefs/blind_b1_rederivation.md`: frozen formula, task scope, and required controls.
- `problems/gauss_circle.md`: project-level problem context only.
- `sources/vaaler_1985.md`: exact \(\beta_{h,H}\) normalization, \(H+1\) argument, nonnegativity and monotonicity of \(\Phi\), and \(\Phi(1/2)=1/2\).
- `state/control_models.md`: definitions of the three required controls.

No excluded proof draft, proof graph, earlier B1 derivation, or campaign report was inspected. No computation or web source was used.

## 8. Recommended state effect

**Promote with an explicit hypothesis:** accept B1 for odd \(p\) under uniform twisted discrepancy (TD), and in particular for a fixed scale-normalized BV or smooth dyadic profile; accept termwise vanishing for even \(p\). **Reject** any formulation based only on boundedness, unnormalized smoothness, coefficient magnitudes, or adversarial coefficient phases. This report makes no inference about a global fat-band energy or pointwise \(S_2(D;X)\).
