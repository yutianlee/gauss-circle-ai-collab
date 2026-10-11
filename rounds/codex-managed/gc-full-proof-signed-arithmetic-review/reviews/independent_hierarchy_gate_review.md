# Round208 independent hierarchy and bandlimited-gate review

Campaign: `gc-full-proof-signed-arithmetic-review`.
Task: `independent_hierarchy_gate_review`. Date: 2026-09-27.
Role: independent post-report seam reviewer, not statement-only in this task.
Starting graph: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
The original blind report's historical isolation is unchanged. This reviewer
does not review its own source report. No numerical experiment was run.

## 1. Result

**GREEN for the conditional mathematics and complete strategy gates in the
two artifacts at the final hashes in Section 6.** The blind hierarchy's
Jacobian, safe bands, Gaussian-order distinctions, and conditional error
qualification are correct. The actual Round206 error is much smaller than
the abstract harmless error allowed by that packet and closes the identified
transfer seam on the reviewed band.

The conductor's bandlimited reproduction bound and complete pointwise
reconstruction are valid. Equations B7--B10 correctly retain both terms of
the tenth-moment certificate. The exact worst missing tenth-moment power is
\(7\beta-101/130\), attained at \(\alpha=1-2\beta\). It is less than
\(13/100\), and its loss after taking a tenth root is smaller than the
corresponding sixth- and eighth-root certificate losses.

The comparison is between specified sufficient certificates. It is not a
claim that ten-factor arithmetic cancellation is intrinsically easier, or
that the new direct K10 gate and new direct K6 gate are logically equivalent.
The older Round206 p12-sufficient K6 estimate does imply the selected new
K10 gate on its smaller band, by the additional calculation below.

No mathematical correction is required. The final conductor version also
correctly names B8, rather than the nonselected B5 comparison, in its final
unproved-source sentence. No arithmetic moment bound or new pointwise
exponent has been proved.

## 2. Exact scope and hypotheses reviewed

Reviewed artifacts:

1. `reports/blind_moment_hierarchy.md` in this campaign.
2. `controls/conductor_bandlimited_strategy.md` in this campaign.

Use the actual smooth dyadic block, with its real cosine and fixed mollifier,

\[
 H_N(R)=\sum_n r_2(n)n^{-3/4}\Psi(\sqrt{n/T})v(n/N)
              \cos(2\pi R\sqrt n-3\pi/4),
\]

where \(v\) is supported in \([1,4]\). Put
\(X=T^2\), \(I=[T/\sqrt2,\sqrt3T]\), \(J=[X/2,3X]\),
\(N=T^\alpha\), \(q=136/13\),

\[
 \omega(\alpha)=\min(\alpha/4,\beta,(1-\alpha)/2),\qquad
 \beta=2\theta_{LY}-1/2,\qquad b=83/650.
\]

The actual source bridge on the reviewed Round206 range is

\[
 H_N(R)=R^{-1/2}Z_N(R^2)+E_N(R),\qquad
 |E_N(R)|\ll T^{-1/2+\varepsilon}N^{-1}+O_A(T^{-A}).
 \tag{R1}
\]

Here \(Z_N\) is the complete centered signed sum with width
\(h(x)=2\sqrt x/\sqrt N\). No replacement by a fixed width, a positive
majorant, or a truncated set of positive integers is made. The concrete
selected band

\[
 T^{166/325}<N<T^{242/325}                              \tag{R2}
\]

lies strictly inside the reviewed old band
\(T^{52/125}<N<T^{99/125}\). The general-b discussion is conditional on
having the same bridge and complement bounds on each required larger band;
the conductor says so explicitly.

The blind report has weaker abstract error hypotheses. It explicitly
requires a per-block complete p-moment error bound for its per-block
interpolation. An aggregate cancellation of uncontrolled errors would not
suffice. This distinction is preserved, rather than repairing the original
isolated packet silently with facts unavailable to its author.

## 3. Independent derivation of the reviewed seams

### Blind hierarchy and its error qualification

If the complete radius moment is \(T^{1+\delta_p+\varepsilon}\),
\(\delta_p\ge0\), multiplication by \(R^{p/2}\) and the Jacobian
\(dx=2R\,dR\) gives the sharp moment
\(X^{1+p/4+\delta_p/2+\varepsilon}\). Its reconstruction-error moment
has exponent \(1+p/4\), so is already included. Monotonicity of the
inclusive count gives a one-sided interval of length comparable to
\(|P(x_0)|\) on which \(|P|\) remains a fixed fraction of that value.
The margin between \([X,2X]\) and \(J\) contains this interval using
the initial sublinear bound. This proves the displayed pointwise exponent

\[
 \frac14+\frac{3+2\delta_p}{4(p+1)}.
\]

For \(p>q\), integrating the two tail terms up to the envelope \(M\)
gives \(T+M^{p-2}+TM^{p-q}\). Therefore the exact universal power
cutoff certified by this tail bound is

\[
 a_p=\min\left(\frac{1+\delta_p}{p-2},
                    \frac{\delta_p}{p-q}\right).
\]

The low and high safe bands are \(\alpha\le4a_p\) and
\(\alpha\ge1-2a_p\), intersected with \([0,1]\), with all scales
safe when \(a_p\ge\beta\). Since \(\beta<1/6\), a nonempty middle
is exactly \((4a_p,1-2a_p)\) when \(a_p<\beta\); the report's
empty, overlap and endpoint conventions are correct. The extensions
at \(p=2,q\) require only the stated logarithmic epsilon loss.

For \(B_N(R)=R^{-1/2}Z_N(R^2)\), the exact change of variables is

\[
 \int_I|B_N|^{2k}dR
 =\frac12\int_J x^{-(k+1)/2}|Z_N(x)|^{2k}dx
 \asymp_k T^{-k-1}K_{2k}(N).                            \tag{R3}
\]

The blind report correctly avoids multiplying a merely harmless lower-order
error by an uncontrolled envelope power. Splitting the domain at
\(|E_N|=|H_N|/2\) gives instead

\[
 |H_N|^p\ll_{p,k}M_N^{p-2k}|B_N|^{2k}+|E_N|^p.
\]

This proves its sufficient K-threshold using a per-block p-error bound.
Its reverse shell certificate correctly retains an extra
\(O(T^{k+2+\varepsilon})\) under only an abstract harmless 2k-error.
The direct radius variance certificate has no such transfer loss.

For Gaussian \(K_{2k}\ll XH^k=T^{k+2}N^{-k/2}\), fixed-order
interpolation yields loss
\((p-2k)\omega-k\alpha/2\). Splitting at \(4\beta\) and
\(1-2\beta\), its maximum is zero for \(2k\le p\le4k\) and
\((p-4k)\beta\) for \(p>4k\). The plateau and descending-branch
crossings in the report's formula (21) solve this same inequality exactly.
Thus one fixed Gaussian order is insufficient for its all-moment conclusion.
The independent functional peak control satisfies the supplied tail and
variance inequalities and can preserve monotonicity; it is expressly not an
arithmetic or bandlimited counterexample. The hierarchy criterion is a
subsequence of unbounded fixed orders with \(\delta_p/p\to0\), not an
unstated uniform estimate with moment order growing with T.

The required p12, \(\delta=4/25\), k=3 specialization recovers
\(a=13/125\), the old complete middle band, radius power \(29/25\),
sharp power \(102/25\), pointwise \(102/325\), and sufficient shell
power \(129/25-6\omega\). These agree exactly with the predecessor
ledger.

### Actual Round206 errors close the abstract transfer seam

The Round205 complete radial identity and Round206 additive bridge each
have the error size in (R1); adding them preserves that size. The latter
bridge follows from the exact curved-to-linear argument ratio, its summable
Schwartz error, the discrete zero mean from Fourier support, and the full
low/high arithmetic tails. Its original report and independent source
review were inspected. In particular, no error-free oddness assertion is
being used.

For every fixed k the actual error gives

\[
 \int_I|E_N|^{2k}dR
 \ll T^{1-k+\varepsilon}N^{-2k}+O_A(T^{-A}).
\]

In both directions, (R3) therefore gives

\[
 \begin{split}
 M_{2k}(H_N)&\ll T^{-k-1}K_{2k}
                         +T^{1-k+\varepsilon}N^{-2k},\\
 K_{2k}&\ll T^{k+1}M_{2k}(H_N)
                         +T^{2+\varepsilon}N^{-2k},
 \end{split}                                              \tag{R4}
\]

with rapid errors included. These terms are much smaller than the concrete
sixth- and tenth-moment thresholds. The blind report's caution is correct,
and the conductor has supplied the stronger hypothesis needed for its
concrete use.

### Finite bandwidth, reproduction, and complete pointwise assembly

The support of the finite Fourier polynomial is exactly contained in
\([-2\sqrt N,2\sqrt N]\). Taking a fixed Schwartz eta with Fourier
transform equal to one on \([-2,2]\), the rescaled reproducing kernel
is \(\eta_N(u)=\sqrt N\eta(\sqrt N u)\). For \(p=2k\),

\[
 \|\eta_N\|_{p'}=N^{1/(2p)}\|\eta\|_{p'}.
\]

Every \(R_0\in[T,\sqrt2T]\) has distance at least cT from the
complement of I. The global coefficient bound \(N^{1/4+\varepsilon}\)
pays the off-I convolution by an arbitrarily small Schwartz tail.
Consequently

\[
 |H_N(R_0)|\ll N^{1/(4k)}M_{2k}(H_N)^{1/(2k)}+O_A(T^{-A}).
 \tag{R5}
\]

Combining (R4)--(R5) gives exactly B4. The explicit error is
\(T^{(1-k)/(2k)+\varepsilon}N^{-1+1/(4k)}\), harmless for k>=2.
Inserting
\(K_{2k}\ll T^{k+1+2kb+\varepsilon}N^{-1/2}\)
cancels the N powers and produces \(T^{b+\varepsilon}\).

Low blocks \(N\le T^{4b}\) sum geometrically using their coefficient
supremum; high blocks \(N\ge T^{1-2b}\) use the full radial bound.
The reviewed bound \(T^{1/2}N^{-1/2}+O(T^{-1/2})\), summed to
\(T^{3/2}\), and the remaining Schwartz tail also justify the stated
\(N\ge T\) contribution. The singleton is bounded. Middle summation
costs only logarithms, and equality at both dividing scales belongs to
the known complement. Sharp reconstruction gives
\(P(x)\ll x^{1/4+b/2+\varepsilon}\) for every real x. This is a
complete implication, not a conclusion from a moment window without margin.

### B7--B10 and the tenth-order selection

For \(2<p<q\), split layer cake at
\(V_0=N^{13/220}\), so \(V_0^{q-2}=N^{1/2}\).
The variance Chebyshev bound applies down to zero, where its integrand
\(V^{p-3}\) is integrable. It contributes

\[
 TN^{-1/2}V_0^{p-2}
      =TN^{-(q-p)/(2(q-2))}.
\]

The two high-tail terms contribute \(W^{p-2}\) and
\(TV_0^{p-q}\), with the latter equal to the same N power. If
\(W<V_0\), the low integral is smaller still. Thus B7 is valid
uniformly, without inserting an incorrect O(T) floor or deleting a
Gram-diagonal term. At p10 it becomes

\[
 M_{10}\ll T^{1+\varepsilon}N^{-3/110}
                      +T^{8\omega+\varepsilon}.
\]

Equation (R4) restores both shell terms
\(T^7N^{-3/110}+T^{6+8\omega}\). The target is
\(T^{473/65}N^{-1/2}\), equivalently
\(M_{10}\ll T^{83/65}N^{-1/2}\), up to epsilon losses.
Subtracting the target gives exactly

\[
 d_A=1-10b+(26/55)\alpha,\qquad
 d_B=8\omega-10b+\alpha/2.
\]

Their difference is \(8\omega-1+(3/110)\alpha\), increasing on
the first two omega branches and decreasing on the last. Its endpoint
values are \(634/17875\) and \(748/17875\), both positive. Hence
dB dominates throughout. It is zero only at the lower boundary of the
open target band, positive within it, and has slopes \(5/2,1/2,-7/2\).
The unique maximum is therefore at \(1-2\beta\), with value
\(7\beta-101/130\). The upper endpoint value is \(38/325\).
These checks retain both interior breakpoints.

The exact beta formula and \(\sqrt{1717}<83/2\) give
\(7\beta-101/130<13/100\); positivity follows already from
\(\beta>b\). The sixth deficit has supremum \(7326/17875\), as
obtained from \(1-6b+(13/55)\alpha\). The eighth first-term deficit
at the upper endpoint exceeds \(24/100\). Taking roots does not
reverse the comparison: the tenth norm deficit is less than 13/1000,
whereas the sixth is \((7326/17875)/6\) and the eighth exceeds
\((24/100)/8\). These are exact power comparisons, not experiments.

For clarity, comparison of different moment orders is not by itself a
logical implication between their new gates. The new K6 gate combined
with the available supremum would give an additional factor
\(T^{4(\omega-b)}\) in the new K10 gate, which cannot be dropped in
the middle. The reverse implication is likewise not supplied by this
comparison.

There is, however, a valid implication from the **old** p12-sufficient
K6 threshold to the selected new gate. It gives
\(M_6\ll T^{29/25-6\omega}\), hence
\(M_{10}\le W^4M_6\ll T^{29/25-2\omega}\).
The new allowed exponent exceeds this by

\[
 10b-29/25-\alpha/2+2\omega.
\]

This difference is \(38/325\) on the low omega branch, then decreases
with slopes -1/2 and -3/2 to zero at the already safe upper endpoint.
It is strictly positive throughout the new open band. Together with
the strictly smaller required band, this confirms the claimed weakening
relative to that particular old certificate. It does not establish any
missing arithmetic estimate.

Finally, Gaussian scale inserted in B1 leaves the deficit
\(1-2kb-\alpha(k-1)/2\). Its worst required alpha approaches 4b,
so the sufficient condition is \(b\ge1/(4k-2)\). For k3 this yields
3/10 only on the entire enlarged band \((2/5,4/5)\). Gaussian sixth
on the old band alone certifies b=13/125 and exponent151/500 instead.
The conductor correctly retains this complement distinction and requires
unbounded fixed k, with verified corresponding bands, for its full-quarter
hierarchy.

## 4. First doubtful or unproved step

No gap was found in the stated conditional implications. The selected
unproved statement is the actual complete K10 inequality B8 on every
dyadic scale in (R2), with real T, the actual centered kernel, moving width,
both arithmetic arms and all tails. Neither B7 nor the finite-bandwidth
argument proves this improvement.

General b and all-order extensions require the bridge and complements on
their corresponding enlarged bands. The existing Round206 bridge was not
silently certified outside its reviewed interval. A fixed-order success
would not prove the quarter theorem or any independent M1/M2 parent.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Original isolated hierarchy | GREEN under its explicit per-block error interpretation; the original historical isolation is preserved. |
| Exact206 error transfer | GREEN on the reviewed band, with both directions of (R4) and all factors retained. |
| Bandwidth and global convolution tail | GREEN; exact finite Fourier support, positive window margin, global coefficient norm, and no integer sampling. |
| B7 low/high split | GREEN for 2<p<q; the lower integral reaches zero lawfully and both upper terms remain. |
| B8--B10 | GREEN; exact shell power, both deficit terms, endpoint values, slopes and interior maximum verified. |
| Norm comparison | GREEN as comparison of the stated certificates; no implication between different new moment gates or arithmetic ease is inferred. |
| Full complements/endpoints | GREEN for the concrete gate; conditional for general-b range extensions. |
| Signed/absolute distinction | GREEN; actual signed sum precedes the norm; no positive-majorant lower bound is treated as a signed lower bound. |
| Fixed-order/full-quarter scope | GREEN; fixed order leaves a gap through the specified implication; unbounded fixed orders and their complements remain required for the stated hierarchy. |

The bandwidth saturation test correctly keeps the factor
\(N^{1/(4k)}\): an aligned Fourier polynomial can realize peaks of
width \(N^{-1/2}\). It is not an actual-r2 counterexample. The blind
constant-shell normalization gives \(TN^{-k/2}\) exactly as required.
All mathematical checks were analytical.

## 6. Exact artifacts and final hashes

| Reviewed artifact | Final SHA-256 |
|---|---|
| `rounds/codex-managed/gc-full-proof-signed-arithmetic-review/reports/blind_moment_hierarchy.md` | `e44f561ff7fec0796822fe82f856c008b1722810ae0d1f030db6da4457424acb` |
| `rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md` | `6aa17dd35e2d930cedadfb489adf8e042b6aed61ed5882ae8e2eb0cd36fbd552` |

The conductor's final B5-to-B8 reference correction and added paragraph
stating the old206-to-B8 implication, while distinguishing the two new
direct gates, were reread. Both final hashes were rechecked after these
changes; the added paragraph agrees with the derivation in Section 3.

Additional authorized source-transfer context actually inspected:

* `protocol.md` and the retained current campaign/context from the preceding
  source assignment;
* the original `briefs/blind_moment_hierarchy_statement.md`, read only in
  this explicitly post-report cross-review, hash
  `236470d52ee584e039e40430415581d32c499c140d79a675773945dfe694b0ac`;
* Round205 `controls/conductor_middle_band_strategy.md`, hash
  `f297dadc44d0113097d6549650228992b6e969740b75e25451eab3a514cebffb`;
* Round206 `controls/conductor_sixth_moment_power_ledger.md`, hash
  `0a60519b209389501b62a82225e5ca9506cf01c0e739acab8d7836b05d275f5a`;
* Round206 `reports/blind_odd_shell_bridge.md`, its initial bridge,
  hypotheses and derivation sections, hash
  `f7c7e3362acc69e71ca8c38b2ec37a1d5b5a08f87682f9c056f2bc4c6770d511`;
* Round206 `reviews/independent_bridge_power_review.md`.

No new external theorem was imported, and no other Round208 report was
reviewed. The review does not certify the mathematical content of the
reviewer's own previously written source report.

## 7. Recommended state effect

**GREEN as independent strategy and conditional-transfer evidence; no
accepted mathematical state change.** The conductor may use B8 and the
correctly scoped order comparison to select its complete arithmetic
objective after closure. Neither reviewed artifact proves B8, a new
pointwise exponent, the full moment hierarchy, the quarter theorem, or an
M1/M2 parent.

Only this assigned review was written. No source report, shared state,
proof draft, synthesis, or successor artifact was changed by this reviewer.
