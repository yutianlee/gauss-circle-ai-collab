# Round207: independent threshold and even-cutoff review

Campaign: `gc-signed-rational-filter-attack`. Task: `independent_threshold_even_cutoff_review`. Role: independent post-report seam reviewer, not blind. Date: 2026-09-27. Starting graph SHA-256: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`. Effort: 100 percent analytical; no mathematical numerical experiment or source import. This review follows a completed, frozen discovery task and does not alter that task's mathematics.

## 1. Result

**GREEN for the mathematical claims within this review's scope.** The full blind report's periodic identities, Fourier endpoint cancellation, bounded-atom completion, support buffer, real-transition analysis and threshold bounds are correct. Its sharper decomposition isolates the only possibly nonnegligible boundary multiple, with the stated sign and coefficient.

Conductor (C2)--(C5) are correct for both the original cutoff and

\[
 D_e=2\left\lfloor\frac{\lfloor\sqrt{\lceil6X\rceil}\rfloor}{2}\right\rfloor,
 \qquad L_e=\left\lfloor\frac{\lceil6X\rceil}{D_e+1}\right\rfloor.
\]

The even cutoff keeps the exact divisor identity and every nonzero physical coefficient. It makes the entire threshold-freezing error rapidly small because its extracted coefficient is exactly \(\chi_4(D_e)=0\). The argument requires \(L_e\), rather than silently retaining the original \(L\).

One wording precision issue was reported to the conductor and corrected before this verdict: at \(x=D\ell\), the two strict indicators agree **for the extracted atom \(m=D\ell\)**; they do not agree for every \(m\). The final reviewed conductor file now says this explicitly and assigns the other terms to the proved rapidly small remainder. The surrounding derivation already handled them correctly. No analytic estimate or coefficient formula needed repair.

This review does **not** assess conductor (C6)--(C10), its rational variance proof, multiplier decomposition, moving-prefix coefficient energy, or complete norm costs. Those have a different reviewer. The review does check that the threshold errors are harmless under the previously reviewed sixth-to-twelfth reconstruction. It establishes no new signed sixth moment, pointwise exponent, M1/M2 result or quarter theorem.

## 2. Exact reviewed hypotheses and scope

The two principal reviewed files and their exact hashes are listed in Section 6. The isolated statement packet was read to restore the blind report's definition of its boundary sum. Its instruction to remain statement-only applied to the original blind analyst; this is the conductor-authorized post-report review and claims no such isolation.

The blind setting is \(J=[X/2,3X]\), \(M=\lceil6X\rceil\), originally \(D=\lfloor\sqrt M\rfloor\) and \(L=\lfloor M/(D+1)\rfloor\). The cutoff satisfies \(0\le\eta\le1\), is supported in \([1/4,6]\), and equals one on \([1/3,4]\). The real odd Schwartz function \(K\) has Fourier support in \([-2,-1]\cup[1,2]\), with all required uniform seminorms. Its actual variable width satisfies

\[
 aH\le h(x)\le bH,\qquad
 X^\delta\le H\le X^{1/2-\delta},\qquad0<\delta<1/4.
\]

The boundary object has **no external factor four**:

\[
 R_D(x)=\sum_{\ell\le L}\sum_{\substack{m\ge1\\\ell\mid m}}
 \eta(m/X)\chi_4(m/\ell)
 \{1_{m>D\ell}-1_{x>D\ell}\}K((x-m)/h(x)).                 \tag{R1}
\]

The physical expansion multiplies (R1) by four. The even-cutoff version replaces both \(D\) and \(L\) in this formula.

In the physical application \(X=T^2\), \(h(x)=2\sqrt{x}/\sqrt N\), \(H=T/\sqrt N\), and \(52/125<\alpha=\log_TN<99/125\). Hence

\[
 X^{151/500}<H<X^{99/250}.
\]

The whole range satisfies the blind assumptions, for example with the single choice \(\delta=1/10\). Thus no unproved fixed-width-to-variable-width passage is needed.

All claims are asymptotic for sufficiently large real \(X\), with constants depending only on the fixed data and chosen decay orders. Integer moduli and residue classes are used for the physical progression identities. The blind report correctly distinguishes a general real affine lattice from the potentially different set of integers satisfying an informal real congruence.

## 3. Independent derivation of the reviewed seams

### Fourier orientation and exact mod-four phase

For \(f(t)=K((x-t)/h)\), direct substitution gives

\[
 \widehat f(\xi)=h e(-x\xi)\widehat K(-h\xi),
 \qquad \widehat K(\xi)=\int K(u)e(-u\xi)du.
\]

Periodizing on \(b+q\mathbb Z\) and then replacing \(k\) by \(-k\) gives exactly

\[
 \sum_{m\equiv b\ (q)}K((x-m)/h)
 =\frac hq\sum_k\widehat K(hk/q)e(k(x-b)/q).               \tag{R2}
\]

Schwartz decay licenses periodization and Fourier inversion. The right side is finite under the spectral support condition. The zero mode vanishes. Because \(\widehat K\) is smooth and supported in the two closed bands, it and every derivative vanish at all four endpoints. Thus \(q\le h/2\), including equality, annihilates the progression exactly.

For the quotient character, split the full lattice into the two residue classes \(\ell\) and \(3\ell\) modulo \(4\ell\). Their factor is

\[
 e(-k/4)-e(-3k/4)=-2i\chi_4(k).
\]

It is zero for even \(k\), \(-2i\) at \(k=1\), and \(2i\) at \(k=3\). Consequently the blind report's single-atom coefficient \(-ih/(2\ell)\), and the conductor's physical coefficient \(-2ih/\ell\) after multiplication by four, are correct. All negative modes are retained. The quotient atom vanishes for \(\ell\le h/8\), with equality covered by the endpoint zero.

For the physical sine integral, \(F=-K\) as functions. Their two customary orientations satisfy

\[
 F((m-x)/h)=K((x-m)/h),\qquad \widehat F=-\widehat K.
\]

The \(F\)-oriented expansion with \(e(-kx/q)\) and the opposite printed Gauss sign agrees with (R2) after replacing \(k\) by \(-k\). In particular the conductor's (C4)--(C5) and the actual additive filter have the same orientation; no extra sign or factor is missing.

The blind report's cutoff controls also check directly. With \(\widehat K=i\psi\), where \(\psi\) is real odd and supported strictly inside the bands, a range \(q<h<2q\) leaves only \(k=\pm1\). The resulting unweighted expression is \(-2(h/q)\psi(h/q)\sin(2\pi(x-b)/q)\). For \(4\ell<h<8\ell\), the quotient expression is \((h/\ell)\psi(h/(4\ell))\cos(2\pi x/(4\ell))\). These verify both constants and signs, and show that the guaranteed initial vanishing intervals cannot generally be extended.

### Boundary extraction, real endpoints and arbitrary decay

Fix \(\ell\), put \(t_\ell=D\ell\), and write \(m=\ell r\), \(r\ge1\). If \(x\le t_\ell\), the indicator difference in (R1) is one exactly for \(r>D\). If \(x>t_\ell\), it is minus one exactly for \(1\le r\le D\). The only term that can approach the real center while being on the incorrect side is \(r=D\), present in the second case. Extracting it gives

\[
 R_D(x)=-\chi_4(D)\sum_{\ell\le L}
  \eta(D\ell/X)1_{x>D\ell}K((x-D\ell)/h(x))+E_D(x).        \tag{R3}
\]

Every remaining term has \(r=D+j\) when \(x\le t_\ell\), or \(r=D-j\) when \(x>t_\ell\), with \(j\ge1\). Thus

\[
 |x-m|=|x-t_\ell|+j\ell.                                 \tag{R4}
\]

For \(\ell<X/(4D)\), the threshold lies below \(X/4\), the real center is at least \(X/2\), and the contributing indices have \(m\le t_\ell\). The distance is at least \(X/4\); the total number of these terms is at most \(DL=O(X)\). For the other indices, \(\ell\gg\sqrt X\), so (R4) bounds the absolute tail for each \(\ell\) by a constant times
\(\sum_{j\ge1}(H/(j\sqrt X))^p\), for any fixed \(p>1\).

Summing gives the independent uniform bound

\[
 \sup_J|E_D|
 \ll_p X(H/X)^p+\sqrt X(H/\sqrt X)^p
 \ll_p X^{1-p(1/2+\delta)}+X^{1/2-p\delta}.                \tag{R5}
\]

Choosing a sufficiently large fixed \(p\) proves \(E_D=O_A(X^{-A})\) for every fixed \(A\). This reproduces the blind report's explicit exponent choices. It uses no cancellation, derivative of \(h\), restriction to interior centers, or spectral hypothesis.

At \(x=D\ell\), the extracted atom has indicator difference zero and \(K(0)=0\). Terms with \(r>D\) do still have indicator difference one; (R4)--(R5) handle them. Contributions from other extracted centers are separated by multiples of \(D\) and are rapidly small. Thus the stronger claim \(R_D(D\ell)=O_A(X^{-A})\) holds directly at the exact threshold.

The nearby-point control is also sound. For fixed \(u\), solving \(x-D\ell=u c\sqrt{x}/\sqrt N\) reduces to a quadratic in \(\sqrt{x}\) with exactly one positive root. If \(D\ell\in[X,2X]\), the root lies in \(J\) for large \(X\), with displacement \(O(H)\). The other centers remain at distance at least a fixed multiple of \(D\). For \(u>0\), (R3) becomes \(-\chi_4(D)K(u)+O_A(X^{-A})\); for \(u<0\), the local extracted term is absent and the whole expression is rapidly small. For a fixed permitted nonzero \(K\), this is a valid counterexample to deleting every odd-\(D\) boundary profile.

### Separated centers and the stated moment errors

The centers \(D\ell\) have spacing \(D\asymp\sqrt X\gg H\). If \(F_*(x)\) is the sum of absolute values of the extracted terms in (R3), the nearest earlier center contributes at most a uniform constant and successive centers contribute a summable square tail. Hence \(\sup_JF_*\ll1\). The bound \(h(x)\le bH\) gives

\[
 \int_JF_*(x)dx
 \le C\sum_{\ell\le L}\int_{\mathbb R}
            (1+|x-D\ell|/(bH))^{-2}dx
 \ll LH\ll\sqrt XH.
\]

Therefore \(\int_JF_*^p\ll\sqrt XH\) for every fixed \(p\ge1\), in particular for \(p=2,6\). Adding (R5) proves the blind report's supremum and sixth bounds, and the conductor's additional second bound. Partial profiles at either real endpoint and centers outside \(J\) are included by integrating a larger nonnegative envelope, not discarded.

The extension to arbitrary bounded atom weights has the stated limited scope. It replaces the extracted \(\chi_4(D)\) by that atom's boundary value and proves the same upper estimates. It does not imply the even-cutoff improvement for arbitrary weights and says nothing about a complete unsigned arithmetic sixth moment.

### Buffered completion and unbounded arithmetic tails

For \(x\in J\), the factor \(1_{m\ge1}\eta(m/X)-1\) can be nonzero only if \(|m-x|\ge X/6\). A unit-interval comparison proves, uniformly in real \(x\),

\[
 \sum_{|m-x|\ge X/6}|m-x|^{-p}\ll_p X^{1-p}\quad(p>1).
\]

One atom with lattice weights bounded by one therefore has completion cost \(O_p(H^pX^{1-p})\). Summing \(O(\sqrt X)\) atoms with bounded outer coefficients gives

\[
 O_p\bigl(X^{3/2}(H/X)^p\bigr)
 =O_p\bigl(X^{3/2-p(1/2+\delta)}\bigr),                   \tag{R6}
\]

which is rapidly small after choosing \(p\). No periodicity is needed for this tail argument. It therefore covers frozen prefix coefficients, both residue branches, and bounded indicator differences, as well as complete periodic atoms. It cannot cover arbitrary unbounded atom normalizations or dense noninteger lattices without further costs; the blind report states these qualifications explicitly.

The buffer counterexample outside \(J\) is valid: at \(m_0=X/4\), smooth support forces \(\eta(m_0/X)=0\); a progression of modulus \(100X\) isolates that atom. Evaluation at \(x-m_0=u_0h(x)\), with \(K(u_0)\ne0\), gives completion difference \(-K(u_0)\) plus rapid tails. Such a point is outside the prescribed buffer and contradicts no asserted estimate.

Before applying the finite divisor identity, localizing the original arithmetic sequence also has rapid cost. Even the crude polynomial bound \(r_2(m)\le4m\), immediate from the divisor formula, suffices with arbitrarily high Schwartz decay. On the low remote range it contributes at most \(O(X^2(H/X)^p)\); the infinite high tail satisfies the analogous convergent integral bound. Thus the bounded-atom completion lemma is not being incorrectly applied directly to an unbounded \(r_2\) atom. The centered lattice mean vanishes after completion by (R2) with modulus one once \(h>2\); the discarded cutoff and negative-lattice parts are already covered by (R6).

### The even-cutoff extension preserves every physical coefficient

For **any** positive integer \(D\), let \(L=\lfloor M/(D+1)\rfloor\). A divisor \(d\) of \(m\le M\) lies either in \(d\le D\) or in \(d\ge D+1\). In the latter case \(\ell=m/d\le L\), and conversely \(\ell\mid m\), \(m>D\ell\) is exactly the condition \(d=m/\ell>D\). This proves conductor (C2) without any square-root equality assumption.

The specified \(D_e\) differs from \(\lfloor\sqrt M\rfloor\) by at most one and remains comparable to \(\sqrt X\). Its own \(L_e\) is comparable to \(\sqrt X\), and \(D_eL_e\le M\). Thus the proof of (R5) applies with only fixed comparison constants changed. The original blind report's convenient individual numerical inequalities for \(D,L\) need not be copied verbatim to every bounded \(X\); the conductor asserts the extension only for sufficiently large \(X\), with bounded cases absorbed.

Since \(D_e\) is even, its extracted coefficient in (R3) is zero. The remaining terms are all covered by (R5), proving

\[
 R_{D_e}(x)=O_A(X^{-A})\quad\text{uniformly on }J.         \tag{R7}
\]

If the original \(D\) is odd, lowering it to \(D_e=D-1\) does **not** delete the nonzero divisor coefficient \(\chi_4(D)\). That divisor moves from the first arm into the complementary second arm, with precisely the same coefficient. The enlarged bound \(L_e\) retains all its possible complementary divisors. No statement about replacing the original cutoff by an even one is valid if this repartition is omitted.

For an additional exact comparison, write \(Q_D=A_D+B_D\) for the frozen, completed main term with cutoff \(D\). Both cutoffs represent the same original filter:

\[
 Z=Q_D+4R_D+O_A(X^{-A})
  =Q_{D_e}+4R_{D_e}+O_A(X^{-A}).
\]

Consequently

\[
 Q_{D_e}-Q_D=4(R_D-R_{D_e})+O_A(X^{-A}).                  \tag{R8}
\]

When \(D\) is odd, (R8) generally contains the old one-sided boundary profile. The two frozen main terms need not agree up to a rapid error. What remains exact is the complete physical filter, and what becomes rapid is the boundary error for the newly repartitioned even cutoff. The conductor's claims have this valid scope.

Finally, apply (R2) to the two correctly repartitioned, completed periodic arms. Multiplying the first arm by \(4\chi_4(d)\) gives (C4); multiplying the quotient atom by four and retaining \(D\ell<x\) gives (C5). This proves the whole reviewed interface, with both signs, all harmonics, the strict mask, factor four and all tails retained.

### Restored errors are safely below the moment threshold

Use the previously reviewed physical bridge and define \(W_0=T^{\omega(\alpha)}\), up to epsilon losses, where \(\omega\le\alpha/4\). The sixth-to-twelfth certificate has prefactor \(T^{-4}W_0^6\). For the original cutoff, the physical error \(4R_D\) therefore contributes at most

\[
 T^{-4+6\omega+\epsilon}\,TH
 =T^{-2-\alpha/2+6\omega+\epsilon}
 \le T^{-2+\alpha+\epsilon}
 \le T^{-151/125+\epsilon}.                              \tag{R9}
\]

This is negligible relative to \(T^{29/25}\) uniformly over every middle scale. Equivalently, the unnormalized error sixth integral \(TH=T^{2-\alpha/2}\) is below the sufficient \(T^{129/25-6\omega}\) threshold by at least the fixed power \(T^{296/125}\). Its second integral \(TH\) is below the variance scale \(XH\) by a factor \(T\). The even cutoff improves these already safe errors to arbitrary negative powers.

A rapid error \(O_A(X^{-A})\) has sixth integral \(O_A(X^{1-6A})\), and its reconstruction cost remains rapid after choosing \(A\) large enough. The external factor four is fixed. The inherited curvature error has sixth contribution \(O(T^{-2+\epsilon}N^{-6})\) before multiplication by \(W_0^6\le N^{3/2}\). All logarithmically many block errors are harmless under Minkowski after choosing the input epsilon losses. None of these estimates upgrades a variance theorem to a signed sixth theorem.

## 4. First doubtful or unproved step

No mathematical gap was found in the full blind report or in conductor (C2)--(C5) with the stated conventions. The final conductor version has the local boundary-atom qualification corrected explicitly. An incorrectly broad reading would be false, but the displayed decomposition never uses that reading.

The first unproved parent input remains the complete actual signed sixth estimate or another complete twelfth-moment argument. Fourier support cancellation, a rapid even-cutoff boundary error, and bounded completion costs do not supply it.

The following inferences would be invalid and are expressly excluded: retaining the old \(L\) after changing the cutoff without proving exact coverage; deleting the old odd divisor rather than moving it to the other arm; treating the two frozen main terms as equal up to rapid error; applying the completion lemma without its plateau buffer or bounded atom hypotheses; and transplanting the Gauss sign between the \(K\) and \(F\) orientations without reindexing.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| Integer progression and real affine lattice | GREEN with the blind report's explicit distinction. |
| Zero mode and Fourier support endpoints | GREEN; vanishing includes \(q=h/2\) and \(\ell=h/8\). |
| Mod-four phase and physical factor four | GREEN; exact \(-2i\chi_4(k)\) in the \(K\), positive-exponential convention. |
| \(K\) versus \(F\) orientation | GREEN; \(F=-K\) and harmonic reindexing give the same physical sum. |
| Single real jump and integer transition | GREEN; extracted term has the stated sign; nonboundary terms at the transition remain in the rapid remainder. |
| Small quotient labels and remote thresholds | GREEN; the split in (R5) handles both without assuming every \(\ell\) is large. |
| Bounded atoms and support buffer | GREEN; all atom costs and the explicit counterexample outside the buffer are valid. |
| Actual variable width | GREEN; upper envelopes use \(h(x)\le bH\), without freezing the width or differentiating it. |
| Even cutoff and its own \(L_e\) | GREEN; exact repartition retains all physical divisor coefficients. |
| Comparison with old frozen main term | GREEN with (R8); no false rapid equivalence is inferred. |
| Error restoration and full middle range | GREEN; (R9) and the raw sixth/second comparisons are uniform with fixed power margins. |
| Conductor (C6)--(C10) | NOT REVIEWED in this assignment; no verdict supplied by this report. |
| Full arithmetic moment and proof scope | OPEN; no source import, Gaussian inference, pointwise improvement or parent closure. |

All checks are analytical. Hashing and the separately authorized byte-format repair are provenance/format operations, not mathematical experiments.

## 6. Exact dependencies and hashes

| Artifact | SHA-256 |
|---|---|
| `rounds/codex-managed/gc-signed-rational-filter-attack/reports/blind_periodic_threshold.md` | `2da72ef8f23acd4c6142856268bd4ab64483dcfccf1619efe4d36821fa3882e3` |
| `rounds/codex-managed/gc-signed-rational-filter-attack/controls/conductor_rational_norm_ledger.md` | `be115ee27206a429c9480594969aa9e9fddd7963569e3f635e8c3ce9085029d4` |
| `rounds/codex-managed/gc-signed-rational-filter-attack/briefs/blind_periodic_threshold_statement.md` | `06bf2d7b272e08e1532dc9d044c1e00e108bfcb7444db7e1be7a4f23c30d187d` |
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `rounds/codex-managed/gc-complete-signed-shell-arithmetic/controls/conductor_sixth_moment_power_ledger.md` | `0a60519b209389501b62a82225e5ca9506cf01c0e739acab8d7836b05d275f5a` |
| `rounds/codex-managed/gc-complete-signed-shell-arithmetic/reviews/independent_bridge_power_review.md` | `f2d4aa391cb12099f2e107af251f7460fb20d7d7dd4bf843963eab565d0666c4` |

The latter two exact interfaces were read only to check the inherited reconstruction and the error powers. No new external theorem, source card, sibling discovery file, or authoritative state was read for this review. Earlier discovery context remains known, so this report is expressly post-report rather than blind; its mathematical checks above do not use that discovery report as evidence for itself.

During this review, the conductor separately authorized a byte-only repair in the reviewer's frozen discovery report: exactly six bare CR bytes were each replaced by the literal two bytes backslash and `r`. No other bytes were changed. Its resulting hash is `f34a4a56d076bf9aa369181feac45a60bf387a38976ac7470f74244785e3cf19`. This is disclosed as a specifically authorized format exception; that report is not a mathematical dependency of this review.

## 7. Recommended state effect

**Retain as scoped GREEN review evidence, without an authoritative-state change.** The conductor may use the exact threshold decomposition and its even-cutoff corollary as validated auxiliary evidence. No graph promotion follows merely from these compatible identities and target-safe errors.

Keep the full signed sixth and twelfth targets, all M1/M2 obligations and the quarter theorem open. Conductor (C6)--(C10) remain outside this review's verdict.

Only this assigned review was written, apart from the explicitly authorized byte-only discovery-format repair recorded in Section 6. No mathematical discovery content, state, proof draft, validation matrix, shared synthesis, source card or successor artifact was edited. This review stops here.
