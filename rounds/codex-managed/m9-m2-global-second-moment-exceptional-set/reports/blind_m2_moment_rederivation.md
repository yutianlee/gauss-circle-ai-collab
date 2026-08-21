## 1. Result.

The frozen estimate (93.2) is correct, with the exact two-sided coefficient and with a constant depending only on \(c_0,c_1\).  In fact, grouping by signed reduced fractions gives a finite set of distinct \(D^{-2}\)-separated frequencies and coefficient mass \(O_{c_0,c_1}(D)\).  A self-contained continuous separated-frequency inequality then proves

\[
 \int_I |S_{D,H,w}(t)|^2\,dt
 \ll_{c_0,c_1} (V+D^2)D.
\]

Consequently, the single-block bound (93.7) and the all-dyadic union bound (93.8) are valid for frozen data.  Without suppressed logarithms, the latter is \(O(Y^{1-2\eta})\) under the stated hypothesis \(\sum_D D\ll Y^{1/2}\); allowing project-level \(Y^\varepsilon\) losses gives (93.8).

The claimed \(h=1\) diagonal sharpness is valid only after adding the necessary lower-bound hypotheses.  For a full shell \(D<d\le 2D\), it follows if \(|\beta_{1,H}|\gg1\) and \(\sum_{D<d\le2D}|w_D(d)|^2\gg D\).  It is not an unconditional consequence of the packet's hypotheses, which allow both \(\Phi(1/(H+1))=0\) and \(w_D\equiv0\).

Nothing proved here transfers the estimate to coefficients or denominator support moving with \(t\).  Freezing separately on the intervals on which \(\lfloor Dt^{-1/4}\rfloor\) is constant gives a loss as large as \(Y^{1/4}\) at \(D\asymp Y^{1/2}\), even before any continuously moving top profile is treated.

## 2. Exact statement and hypotheses.

Let \(D\ge H\ge1\), let \(\mathscr D_D\subset[c_0D,c_1D]\cap\mathbb Z_{>0}\), let \(|w_D(d)|\le1\), and let \(I\subset\mathbb R\) be an interval of length \(V\ge0\).  Put \(e(x)=e^{2\pi i x}\), and for \(0<|h|\le H\) put exactly

\[
 \beta_{h,H}=-\frac{\Phi(|h|/(H+1))}{\pi|h|}
 \chi_4(|h|)\mathbf 1_{2\nmid h},
 \qquad 0\le\Phi\le1,
\]

with \(\beta_{h,H}=0\) otherwise.  Thus \(\beta_{-h,H}=\beta_{h,H}\), but the positive and negative frequencies remain distinct.  Then

\[
 \int_I\left|\sum_{0<|h|\le H}\beta_{h,H}
       \sum_{d\in\mathscr D_D}w_D(d)e\!\left(\frac{ht}{4d}\right)
       \right|^2dt
 \le C_{c_0,c_1}(V+D^2)D. \tag{R93.1}
\]

For \(I=[Y,2Y]\) and \(D\le Y^{1/2}\), this implies

\[
 |\mathcal B_{D,H,w}(Y;\eta)|
 \le \min\!\left\{Y,\,C_{c_0,c_1}D Y^{1/2-2\eta}\right\}. \tag{R93.2}
\]

If \(\mathcal J\) is any fixed family of frozen dyadic blocks, every \(D\in\mathcal J\) satisfies \(D\le Y^{1/2}\), and \(\sum_{D\in\mathcal J}D\le C_*Y^{1/2}\), then

\[
 \left|\bigcup_{D\in\mathcal J}\mathcal B_{D,H_D,w_D}(Y;\eta)\right|
 \le \min\!\left\{Y,\,C_{c_0,c_1,C_*}Y^{1-2\eta}\right\}. \tag{R93.3}
\]

If the individual moment estimates are recorded with a \(Y^\varepsilon\) loss, the right side is instead \(O(Y^{1-2\eta+\varepsilon})\).  At \(\eta=0\) and \(D\asymp Y^{1/2}\), (R93.2) is only \(O(Y)\), so it gives no measure saving.

The exact conditional sharpness statement is as follows.  Define the top primitive zone

\[
 E_D=\{b\in\mathscr D_D:b>c_1D/2\}.
\]

Then

\[
 \sum_{a,b}|A_{a,b}|^2
 \ge 2|\beta_{1,H}|^2\sum_{b\in E_D}|w_D(b)|^2. \tag{R93.4}
\]

Hence coefficient mass is \(\gg D\) if \(|\beta_{1,H}|\gg1\) and the weight has \(\ell^2\)-mass \(\gg D\) on \(E_D\).  For the full shell \(D<d\le2D\), one has \(c_1=2\) and every shell point lies in \(E_D\), which is precisely the packet's \(h=1,d>D\) control.

## 3. Proof or derivation.

For every original pair \((h,d)\), set

\[
 k=(|h|,d),\qquad a=h/k,\qquad b=d/k.
\]

Then \(k\ge1\), \(a\ne0\), \(b>0\), and \((|a|,b)=1\).  Conversely, every representation of a signed reduced fraction \(a/b\) is uniquely \((h,d)=(ka,kb)\) with \(k\ge1\).  This proves that the exact equal-frequency multiplicity is

\[
 K_{a,b}=\{k\in\mathbb Z_{\ge1}:k|a|\le H,\ kb\in\mathscr D_D\},
\]

and hence

\[
 A_{a,b}
 =-\frac1{\pi|a|}
   \sum_{k\in K_{a,b}}
   \frac{\Phi(k|a|/(H+1))}{k}
   \chi_4(k|a|)\mathbf1_{2\nmid ka}\,w_D(kb). \tag{R93.5}
\]

Thus the \(\chi_4\) sign is retained term by term; no absolute value has been inserted into the exact coefficient.  Negative \(a\)'s are also retained, and evenness gives \(A_{-a,b}=A_{a,b}\).  The exact regrouping is

\[
 S_{D,H,w}(t)=\sum_{\substack{a\ne0,\ b>0\\ (|a|,b)=1}}
 A_{a,b}e\!\left(\frac{at}{4b}\right), \tag{R93.6}
\]

where only finitely many terms are nonzero.

Write \(R=c_1/c_0\).  If \(K_{a,b}\ne\varnothing\), every one of its elements lies between \(c_0D/b\) and \(c_1D/b\).  With \(m=\lceil c_0D/b\rceil\), this set is contained in the integers from \(m\) through \(\lfloor Rm\rfloor\).  Therefore, including all possible support endpoints,

\[
 \sum_{k\in K_{a,b}}\frac1k
 \le \sum_{m\le k\le Rm}\frac1k
 \le 1+\log R.
\]

It follows directly from (R93.5) that

\[
 |A_{a,b}|\le \frac{1+\log(c_1/c_0)}{\pi|a|}. \tag{R93.7}
\]

Nonempty support also forces \(b\le c_1D\) and \(1\le|a|\le H\).  Dropping coprimality and all further support restrictions therefore gives

\[
 \begin{aligned}
 \sum_{a,b}|A_{a,b}|^2
 &\le \frac{(1+\log(c_1/c_0))^2}{\pi^2}
       \sum_{1\le b\le c_1D}\sum_{1\le|a|\le H}\frac1{a^2}\\
 &\le C_{c_0,c_1}D. \tag{R93.8}
 \end{aligned}
\]

This proof does not discard a partial first or last \(k\)-block and is unchanged when \(k|a|=H\) or \(kb\) is an included endpoint of \(\mathscr D_D\).

The distinct frequencies in (R93.6) are separated.  Indeed, for unequal signed reduced fractions \(a/b\ne a'/b'\),

\[
 \left|\frac a{4b}-\frac{a'}{4b'}\right|
 =\frac{|ab'-a'b|}{4bb'}
 \ge \frac1{4c_1^2D^2}. \tag{R93.9}
\]

This includes pairs of opposite sign because zero numerators are absent.

For completeness, here is a proof of the continuous separated-frequency inequality used next.  Let \(\Lambda\) be any finite \(\delta\)-separated subset of \(\mathbb R\), let \(F(t)=\sum_{\lambda\in\Lambda}c_\lambda e(\lambda t)\), and let \(I\) have centre \(T\) and length \(V\).  Set \(L=\max(V,\delta^{-1})\) and

\[
 W(t)=2\left(1-\frac{|t-T|}{L}\right)_+.
\]

Since \(W\ge1\) on \(I\),

\[
 \int_I|F(t)|^2dt\le\int_{\mathbb R}W(t)|F(t)|^2dt.
\]

With the convention \(e(x)=e^{2\pi ix}\), direct integration of the triangular function gives

\[
 \left|\int_{\mathbb R}W(t)e(\xi t)dt\right|
 =2L\left|\frac{\sin(\pi L\xi)}{\pi L\xi}\right|^2. \tag{R93.10}
\]

Order the frequencies.  For any fixed frequency, its \(n\)-th neighbour on either side is at distance at least \(n\delta\).  Since \(L\delta\ge1\), the row sum of the absolute values of the kernel in (R93.10) is at most

\[
 2L+2\sum_{n\ge1}\frac{2L}{\pi^2L^2n^2\delta^2}
 \le 2L+\frac{2L}{3}=\frac{8L}{3}. \tag{R93.11}
\]

The kernel of absolute values is symmetric.  Applying \(2|uv|\le|u|^2+|v|^2\) to the expanded quadratic form and then (R93.11) proves

\[
 \int_I|F(t)|^2dt
 \le \frac83\max(V,\delta^{-1})\sum_{\lambda\in\Lambda}|c_\lambda|^2
 \le \frac83(V+\delta^{-1})\sum_{\lambda\in\Lambda}|c_\lambda|^2. \tag{R93.12}
\]

Apply (R93.12) to (R93.6), use \(\delta^{-1}\le4c_1^2D^2\) from (R93.9), and then use (R93.8).  This proves (R93.1), hence (93.2).  If \(I=[Y,2Y]\) and \(D^2\le Y\), it gives \(\int_Y^{2Y}|S|^2dt\ll YD\), which is (93.3).

Chebyshev's inequality at threshold \(Y^{1/4+\eta}\) now gives

\[
 |\mathcal B_{D,H,w}(Y;\eta)|
 \le Y^{-1/2-2\eta}\int_Y^{2Y}|S(t)|^2dt
 \ll D Y^{1/2-2\eta},
\]

proving (R93.2).  Summing this bound over the fixed dyadic family and using \(\sum_D D\ll Y^{1/2}\) proves (R93.3).  The cardinality \(O(\log Y)\) creates no additional loss once the stronger sum-of-scales hypothesis is used.

To prove (R93.4), take \(b\in E_D\).  The \(k=1\) term belongs to \(K_{1,b}\), while every \(k\ge2\) has \(kb>c_1D\) and hence cannot belong to \(\mathscr D_D\).  Thus

\[
 A_{1,b}=\beta_{1,H}w_D(b),\qquad
 A_{-1,b}=\beta_{-1,H}w_D(b)=\beta_{1,H}w_D(b).
\]

Summing these two signed-frequency contributions over \(E_D\) proves (R93.4).  The diagonal part of the interval integral is \(V\sum_{a,b}|A_{a,b}|^2\), so it is \(\gg VD\) under the stated lower hypotheses.  Moreover, for any fixed finite frequency set, division of the exact expanded integral by \(V\) and passage to \(V\to\infty\) kills every off-diagonal term.  Thus the \(VD\) term in the uniform upper bound cannot in general be removed.  This does not supply an unconditional lower bound: exactly

\[
 \beta_{1,H}=-\frac{\Phi(1/(H+1))}{\pi},
\]

and the permitted assumption \(0\le\Phi\le1\) supplies no positive lower bound.

Finally, suppose only \(H(t)=\lfloor Dt^{-1/4}\rfloor\) moves and all other data freeze whenever \(H\) does.  On \([Y,2Y]\), the number \(N\) of nonempty constancy intervals satisfies

\[
 N\le 2+D\bigl(Y^{-1/4}-(2Y)^{-1/4}\bigr)
 \ll 1+DY^{-1/4}. \tag{R93.13}
\]

Applying (R93.1) on every such interval \(I_j\), of length \(V_j\), and summing yields only

\[
 \sum_j (V_j+D^2)D
 =YD+ND^3
 \ll YD+D^3+D^4Y^{-1/4}. \tag{R93.14}
\]

At \(D\asymp Y^{1/2}\), this is \(O(Y^{7/4})\), whereas the frozen target is \(O(Y^{3/2})\): the first floor-by-floor unsmoothing loses \(Y^{1/4}\).  If the top denominator support or profile varies even while \(H\) is fixed, this partition does not freeze the block at all.

## 4. First doubtful or unproved step.

There is no doubtful step in the frozen upper bound: the grouping, mass estimate, spacing, and continuous inequality are all proved above.  The first unproved step in any transfer is the replacement of the fixed vector \((A_{a,b})\) in (R93.6) by a \(t\)-dependent vector.  Formula (R93.12) is not a variable-amplitude inequality, and (R93.14) shows the first exact loss incurred by the elementary floor-interval workaround.  The packet gives no formula or bounded-variation/basis estimate for a moving top profile, so a same-power moving theorem cannot be concluded.

The other unavailable step is an unconditional sharpness lower bound.  The hypotheses do not imply \(|\beta_{1,H}|\gg1\), do not require any nonzero weight, and do not require \(\ell^2\)-mass in the no-multiplicity top zone.  For example, \(\Phi\equiv0\) is permitted and makes every coefficient vanish even if the weight has large \(\ell^2\)-mass.  Thus only the conditional sharpness statement (R93.4) is justified from the packet.

## 5. Control tests and outcomes.

- **Exact reduced-fraction grouping, including negative frequencies:** passed.  The signed numerator \(a=h/(|h|,d)\), positive denominator \(b=d/(|h|,d)\), and positive multiplier \(k=(|h|,d)\) give a bijection.  Positive and negative \(a\) are distinct terms.
- **Equal-frequency multiplicity and support endpoints:** passed.  The exact multiplier set is \(K_{a,b}\).  The harmonic bound contains the first and last admissible integers, and an endpoint is present precisely when it belongs to the stated set.  For the sharpness test, the strict inequality \(b>c_1D/2\) is necessary because equality may allow \(k=2\).
- **Coefficient \(\ell^2\)-mass:** passed for the upper bound, uniformly in \(H\), the arbitrary subset \(\mathscr D_D\), and all endpoint configurations; (R93.8) is \(O(D)\).  A lower bound is conditional as in (R93.4).
- **Continuous separated-frequency inequality:** passed by the triangular-majorant proof (R93.10)--(R93.12), with no external citation.
- **Exact \(\chi_4\) coefficient:** passed.  It remains explicitly inside the multiplier sum (R93.5).  In particular, even \(ka\) terms vanish and odd signs are not replaced by their absolute values in the regrouping.
- **Single-block and all-dyadic exceptional measures:** passed.  The exact consequences are (R93.2) and (R93.3); a suppressed \(Y^\varepsilon\) propagates to the union bound.  At \(\eta=0,D\asymp Y^{1/2}\), the test correctly gives no density saving.
- **\(h=1\) diagonal sharpness:** conditionally passed and unconditionally refuted.  The no-multiplicity top zone gives (R93.4), but the packet lacks the lower hypotheses needed to turn it into \(\gg D\).
- **Frozen versus moving and pointwise scope:** the frozen result passes.  The moving transfer is not established, and the naive freeze loses \(Y^{1/4}\) at the top scale.  An \(L^2\) bound permits exceptional points and supplies neither a supremum bound nor simultaneous endpoint uniformity.  Therefore it does not imply pointwise M9--M2, M9, or a one-quarter theorem.  The packet does not state the Round-92 canonical hard cores, so no identification with either hard core is justified; the proved deliverable is only the frozen global moment.

## 6. Dependencies and exact artifacts used.

Only the following two permitted artifacts were read or used:

- `rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/briefs/blind_m2_moment_rederivation.md`;
- `rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/derivation_packet.md`.

No proof graph, strategy file, prior or sibling report, source card, conductor candidate, computation, or web source was consulted.  The separated-frequency inequality and every control above were derived in this report.

## 7. Recommended state effect.

**Promote** (93.2), (93.3), (93.7), and the frozen all-dyadic consequence, together with the exact grouping and coefficient-mass lemma.  **Revise** the \(h=1\) sharpness claim to include \(|\beta_{1,H}|\gg1\) and nontrivial \(\ell^2\)-mass on a no-multiplicity top sub-shell.  **Retain** the moving-height/top-profile transfer as an open seam, recording the floor-by-floor bound \(YD+O(D^3+D^4Y^{-1/4})\) and its \(Y^{1/4}\) top-scale loss.  Make **no change** to any pointwise or Round-92 hard-core obligation.
