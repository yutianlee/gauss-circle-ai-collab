# Round 145 blind final audit of the conductor candidate

## Final verdict: RED

The arithmetic reduction itself is green: (145.C6), (145.C8), their multiplicities and distinct meanings, every (2)-adic case, the (M^{1/4}/T) tail, the ceiling split, strict (s>M^{1/2}), mask signs, exact-radical/Pell formulas, and the (N=sL^2+1) construction all recheck.  The capacity statements are also correctly phrased as upper-ledger limitations rather than lower bounds.

The candidate is nevertheless not promotion-ready because it imports a primary-source/power-mismatch package for which no Round-145 source report or theorem cards exist among the stated campaign evidence.  In particular, the claims culminating in (145.C22) cannot be independently hypothesis-audited from the candidate, the two reports, or the two cross-reviews, while the candidate says that a Round-145 source report contains the full cards and later lists “three Round-145 reports.”  The campaign contains only the two fibre reports.  This is an evidence and dependency gap under the protocol, so the required binary verdict is RED.  Exact repair: either remove the primary-source assertions, (145.C22), their proposed obstruction promotion, and the nonexistent third-report dependency, or produce the missing source report with exact citations, theorem statements, hypothesis matching, normalization, and power calculations and send it through independent review.

Two smaller exactness repairs should be made at the same time: express the terminal block with a literal half-open endpoint, and state the lower-profile plateau used by the exceptional family rather than leaving “active lower-profile range” implicit.

## 1. Squarefree-kernel formula (145.C6): GREEN

Let (A=v_p(h)) and (B=v_p(r)).  In the squarefree-kernel parametrization,

\[
v_p(\gamma)=1\quad\Longleftrightarrow\quad A\equiv B\equiv1\pmod2.
\]

After removing this common parity bit, (d={\rm sf}(h)/\gamma) and (e={\rm sf}(r)/\gamma) are squarefree and (gamma,d,e) are pairwise coprime.  Since the parity of (A+B) is the parity of exactly one of the residual bits, (de={\rm sf}(hr)=s).  The positive square roots

\[
a=\sqrt{h/(\gamma d)},\qquad b=\sqrt{r/(\gamma e)}
\]

are unique, and

\[
hr=\gamma^2de(ab)^2=s(\gamma ab)^2
\]

forces (t=\gamma ab).  Conversely, every tuple counted by (145.C6) reconstructs exactly one ordered pair

\[
h=\gamma da^2,qquad r=\gamma eb^2.
\]

Its squarefree kernels are exactly (gamma d) and (gamma e), so the recovered (gamma) is unique.  Allowing (gamma) to share primes with (a) or (b), and allowing (a,b) to share primes, is necessary and creates no multiplicity.  The only squarefree restriction is ((\gamma,s)=1), which follows from the parity construction and is also sufficient in the converse.

The coefficient conditions are exact:

\[
r\text{ odd}\iff \gamma,e,b\text{ odd},
\qquad
\chi _4(r)=\chi _4(\gamma)\chi _4(e),
\qquad
r>4h\iff eb^2>4da^2.
\]

Thus (145.C6) is a multiplicity-one parametrization of (C(st^2)).

## 2. Full-gcd formula (145.C8), distinction, and multiplicity: GREEN

For (G=(h,r)), the quotients (H=h/G) and (Q=r/G) are coprime and satisfy

\[
HQ=s(t/G)^2.
\]

They therefore have unique forms

\[
H=da^2,qquad Q=eb^2,qquad de=s,qquad (da,eb)=1.
\]

Comparison of products gives (Gab=t).  Conversely, a tuple in (145.C8) reconstructs

\[
h=Gda^2,qquad r=Geb^2,
\]

and ((da,eb)=1) makes its full gcd exactly (G).  This proves multiplicity one.  The conditions (Geb) odd, (eb^2>4da^2), and the weight (chi _4(Ge)) are precisely the original parity, cone, and character conditions.

The two parametrizations do not use the same common factor or, in general, the same (d,e,a,b).  Primewise,

\[
v_p(\gamma)=\mathbf1_{A\ {\rm odd}}\mathbf1_{B\ {\rm odd}},
\qquad
v_p({\rm sf}(G))\equiv\min(A,B)\pmod2.
\]

For example, (h=p^4,r=p^3) gives (gamma=1) in (145.C6), whereas (G=p^3) and ({\rm sf}(G)=p) in (145.C8); that (p) also occurs in the residual squarefree factor (d={\rm sf}(h/G)).  This validates the candidate's warning that (c={\rm sf}(G)) may overlap (d,e,a), or (b), while (gamma) is coprime to (s).  No extra coprimality with (G,c,ell) is legal.

## 3. Complete (2)-adic audit: GREEN

Because the original (r) is odd, the four cases are forced as follows.

1. If (s,t) are odd, all of (gamma,d,e,a,b) in (145.C6) are odd except that no further restriction is needed; in (145.C8), (G,e,b) are odd and (d,a) are consequently odd as well.
2. If (2\mid s) and (t) is odd, then (e) is odd and the unique factor (2) of (s) lies in (d); (a) remains odd.
3. If (s) is odd and (2^q\Vert t), (q>0), then (gamma,e,b) are odd and (2^q\Vert a).
4. If (2\mid s) and (2^q\Vert t), the factor (2) of (s) lies in (d), while the entire exponent (q) of (t) lies in (a).  Hence (v_2(h)=1+2q) and (r) is odd.

The full-gcd form gives the same ledger because (Geb) odd forces (G,e,b) odd.  The parity of (N) plays no role in the coefficient.  No (2)-adic fibre is lost or duplicated.

## 4. Tail, ceiling, terminal endpoint, and strict support: GREEN mathematically; endpoint notation repair required

For a literal half-open block

\[
\mathcal I_M=\mathbb N\cap[M,B_M),\qquad B_M\leq2M,
\]

the exact unmasked fixed-(t) count is

\[
\left\lceil\frac{B_M}{t^2}\right\rceil-
\left\lceil\frac{M}{t^2}\right\rceil
\leq \frac{M}{t^2}+1.
\]

Nonemptiness implies (t^2<B_M\leq2M), so the last quantity is at most (3M/t^2).  Consequently, for real (T\geq1),

\[
M^{-3/4}X^\varepsilon
\sum_{t\geq\lceil T\rceil}\frac{M}{t^2}
\ll X^\varepsilon\frac{M^{1/4}}{T}.
\]

This verifies (145.C10); profile, squarefreeness, phase, and mask are removed only after triangle inequality on the discharged complement.  Taking (T=M^{1/4}), summing the logarithmic number of blocks, and renaming epsilon is target-safe.

For integral (t), (145.C11) is exact, including when (M^{1/4}) is itself an integer.  The equality case then belongs to the large-(t) complement.  On the retained side,

\[
t^2<M^{1/2},\qquad st^2=m\geq M,
\]

and hence (s>M^{1/2}) strictly.

The candidate's opening notation

\[
\mathcal I_M=[M,2M)\cap[1,M_*]
\]

is not literally half-open at a truncated terminal endpoint.  It does not invalidate the majorant, because (145.C2) retains membership in the actual set and replacing the upper endpoint by (2M) only enlarges it, but an authoritative exact statement should replace it by (mathcal I_M=\mathbb N\cap[M,B_M)) with the inherited literal (B_M\leq2M).  If the intended terminal integer (M_*) is included, write (B_M=M_*+1); if it is excluded, write (B_M=M_*).  This removes the only endpoint ambiguity.

## 5. Mask signs, radical fibre, and Pell normalization: GREEN

With (x=t\sqrt{Ns}) and (delta=k-x),

\[
j=k^2-x^2=\delta(2x+\delta),
\qquad {\rm sgn}(j)={\rm sgn}(\delta).
\]

A half-integer tie is impossible because (4Nst^2) cannot be an odd square.  Thus (-1/2<\delta<1/2), the nearest-integer norm is exact,

\[
\|t\sqrt{Ns}\|=|\delta|=\frac{|j|}{k+t\sqrt{Ns}},
\]

and the strict mask retains both signs with no boundary cell silently moved.

Writing (N=Dw^2), (D) squarefree, gives (Ns) square exactly when (s=D); this fibre has (j=0) for every (t) and is absent from the strict survivor.  If (s\neq D), then

\[
g_s=(D,s),\qquad q_s=Ds/g_s^2>1
\]

is squarefree and

\[
j=k^2-q_s(g_swt)^2.
\]

This is the exact generalized Pell equation with the second-coordinate divisibility retained.  The mask removes (|j|\leq M^{3/4}), not all near-resonant quadratic-irrational fibres.

## 6. Exceptional family (N=sL^2+1): GREEN mathematically; profile hypothesis should be explicit

Take (X=N=sL^2+1), (s>1) squarefree.  Then

\[
\sqrt{Ns}=sL+\rho,
\qquad
\rho=\frac1{\sqrt{L^2+1/s}+L}.
\]

If (t\rho<1/2), the nearest integer is (k=sLt), so

\[
\delta=-t\rho,qquad j=(sLt)^2-Nst^2=-st^2=-m,
\qquad e(t\sqrt{Ns})=e(t\rho).
\]

Now set (L=s).  The inherited lower profile has a flat active interval at the origin; choose fixed (c>0) with (V_{\rm low}(y)=1) on (0\leq y\leq c^2).  For (1\leq t\leq c s^{1/4}),

\[
\frac{R^2m}{N}=\frac{m}{\sqrt N}
=\frac{st^2}{\sqrt{s^3+1}}\leq c^2,
\]

so the literal profile is active.  Also (t\rho<1/2).  If (M\leq m<2M), then (M>m/2=st^2/2); for all sufficiently large (s), (t^2<s/2), hence (t^4<M) and (t<M^{1/4}).  Finally,

\[
|j|=m\geq M>M^{3/4}
\]

for (M>1).  Thus the family genuinely lies in the profiled small-(t), strict large-displacement survivor, while (t\rho\to0) uniformly.  Since

\[
\rho^{-1}=\sqrt{L^2+1/s}+L
\]

has integer part (2L), the next continued-fraction quotient is unbounded.  Taking (s=p>4) prime and (t=1) gives (C(p)=\chi _4(p)\neq0), proving nonvacuity but no aggregate lower bound.

The candidate states this conclusion but omits the plateau choice and the displayed profile calculation.  Insert the sentence “choose (c>0) with (V_{\rm low}=1) on ([0,c^2])” and the ratio above, or cite the exact inherited profile lemma.  Without that explicit inherited hypothesis, a generic smooth compactly supported function called (V_{\rm low}) need not be active near zero.

## 7. Capacity and scope: arithmetic statements GREEN; source package RED

The arithmetic capacity language is correct.  Equation (145.C20) is only a divisor-envelope upper bound.  The (t=1) layer has one (t)-sample per squarefree (s) in its block, so linear summation in (t) gives no saving there, but cancellation across (s), between layers, or between blocks remains possible.  The identity (C(p)=\chi _4(p)) proves only that the layer is not algebraically empty.  Neither it nor the exceptional family gives an absolute or signed lower bound.  Equation (145.C23) correctly identifies the first still-unproved signed estimate.  The candidate also correctly refuses every downstream M1, M2, endpoint, M9, bridge, quarter-bound, and exponent promotion.

The primary-source subsection is not reviewable from the declared evidence.  There are exactly two Round-145 reports in the campaign:

- `reports/squarefree_kernel_fibre_attack.md`;
- `reports/blind_squarefree_linearization_feasibility.md`.

Neither is the “Round-145 source report” claimed after (145.C22), and neither contains the promised theorem cards or enough of the cited theorems to audit their hypotheses or reproduce the powers (R^{2/5}), (R^{1/2}), or (R^{3/4}).  The only source-audit artifact present is a brief, not a completed report.  The candidate's final sentence listing “three Round-145 reports” is therefore false as an artifact dependency.  Under the protocol, the source-exclusion claims and (145.C22) cannot be promoted on this record.

Exact repair options are:

1. remove the primary-source audit, (145.C22), the source/power-mismatch portion of the proposed obstruction, and the nonexistent third-report dependency from this candidate; or
2. complete the missing source report with exact bibliographic citations, verbatim theorem normalizations within quotation limits, all hypotheses, the substitution leading to each stated (R)-power, and an independent source seam review.

After one of those repairs, plus the endpoint and profile clarifications above, the strict squarefree-kernel reduction itself is GREEN and may be reconsidered for promotion.  On the candidate as written, the final verdict remains RED.
