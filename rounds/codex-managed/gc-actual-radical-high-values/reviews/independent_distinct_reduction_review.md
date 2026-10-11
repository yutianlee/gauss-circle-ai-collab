# Round216 independent NONBLIND seam: complete distinct-radical reduction

Campaign: `gc-actual-radical-high-values`.
Reviewer role: independent mathematical seam, explicitly NONBLIND.
Generated: 2026-09-28T02:07:35+08:00.
Candidate: `candidates/complete_distinct_radical_reduction.md`.
Reviewed candidate SHA256:
`d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee`.
Starting graph SHA256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
No experiments, source expansion, sibling-report access or shared-state edits.

## 1. Result

**GREEN** for the candidate's mathematical seam at the exact hash above.
No mathematical correction is required.

The actual head arithmetic, masked distribution extension, head moment,
all lower moments of the actual tail, collective partition identity,
complete repeated-class error, infinite limits, and four-way equivalence
are valid. In particular, the candidate proves

\[
 M_{12}(L_Q)\ll_\epsilon T^{15/13+\epsilon},\qquad
 \int w(R/T)|Z_Q^{12}-E_{12}|\,dR
       \ll_\epsilon T^{8\beta-1/5+\epsilon},
\]

and the stated equivalence with the signed distinct-class integral.
It does not prove any of the equivalent target estimates.
The small additive approximation is for \(M_{12}(Z_Q)\), **not**
for \(M_{12}(B_T)\). The candidate observes this distinction.

## 2. Exact statement and hypotheses checked

The reviewed definitions are the candidate's full mollified real cosine
series with actual \(r_2(n)\), real \(T\ge2\), the fixed radial
nonnegative unit-mass mollifier, and the fixed smooth nonnegative window
supported in \([1/2,2]\). They imply real even Schwartz \(\Psi\),
\(|\Psi|\le1\), and absolute summability for each fixed \(T\).

The cutoff is exactly \(Q=\lfloor T^{2/5}\rfloor\), including
\(Q\ge1\) for all permitted real \(T\). Each squarefree class
function contains all \(s\ge1\), its actual coefficients, and the
original real cosine phase. The ordered definition of \(E_{12}\)
agrees with the combinatorial identity and the factor \(2^{-12}\)
in the final Fourier expansion.

The accepted inputs used are the elementary divisor identity and bound,
the finite coefficient-vector argument inside the accepted round204
kernel, the qualified accepted physical Li--Yang supremum, and the
proved rational independence of distinct squarefree radicals from the
accepted exact-resonance kernel. The latter graph node was checked to
be `proved_internal`. No stronger external source assertion is needed.

The only numerical inequalities required of the accepted exponent are
\(1/8<\beta<13/100\). The candidate does not extrapolate a supremum
bound from the physical series to arbitrary coefficient masks.

## 3. Independent derivation of the reviewed seams

### Actual head arithmetic and the exponent \(15/13\)

For squarefree \(d\), the coefficient comparison
\(r_2(ds^2)\le r_2(d)\tau(s^2)\) is valid prime by prime.
If \(d\) contains a prime congruent to three modulo four, its
exponent in \(ds^2\) remains odd and both representation counts
vanish. Otherwise, at a prime congruent to one modulo four that
divides \(d\), the relevant factor is \(2e+2\le2(2e+1)\);
at a prime not dividing \(d\), it is \(2e+1\). The prime two
introduces no representation-count factor. The common leading factor
four is preserved, including \(d=1\).

Since \(\tau(s^2)\le\tau_3(s)\), summing over every \(s\)
gives the candidate's bound

\[
 A_d(T)\le\zeta(3/2)^3r_2(d)d^{-3/4}.
\]

The elementary estimate \(\sum_{n\le x}r_2(n)\ll x\) and partial
summation imply \(\sum_{d\le Q}A_d\ll Q^{1/4}\), with no
extra divisor logarithm. Restricting to squarefree indices only
decreases this positive sum. Thus \(\|L_Q\|_\infty\ll Q^{1/4}\).

The masked distribution has exponent \(q=136/13\). Layer cake
below amplitude one costs \(O(T)\), and above it the two terms
give, with \(W_L\ll Q^{1/4}\),

\[
 M_{12}(L_Q)\ll T^\epsilon
   \{T+W_L^{10}+T W_L^{12-q}\}
 \ll T^\epsilon\{T+Q^{5/2}+TQ^{5/13}\}.
\]

As \(Q\asymp T^{2/5}\), the powers are respectively
\(1,1,15/13\). This verifies (D1)/(D9) for the complete head,
rather than only its pointwise smallness.

### Masked distribution and every lower moment of the actual tail

The extension in (D8) uses the finite proof inside the accepted kernel
correctly. An arbitrary zero-one mask depending on \(n,T\), but not
on \(R\), does not increase the block coefficient energy. Its
unweighted ambient correlation matrix is unchanged. The finite duality
and separated-set covering statement holds at every positive block
level, so the later threshold \(V/(C\log T)\) need not exceed one.
The singleton, partial last block, full diagonal, localization ceiling,
and the uniform Schwartz tail all remain present.

For \(Z_Q=B_T-L_Q\), its supremum follows specifically from the
accepted physical bound for \(B_T\) and the just-proved head bound:
\(T^{1/10}\) is smaller than \(T^\beta\). For \(2\le r\le10\),
the \(TV^{-q}\) part of layer cake is integrable above one because
\(r<q\). The \(V^{-2}\) part costs \(W_Z^{r-2}\), with only a
logarithm at \(r=2\). This proves (D10). The cases \(r=0,1\) cost
\(O(T)\) and \(O(T^{1+\epsilon})\), respectively, by the finite
window measure and Cauchy--Schwarz. Every lower moment used later is
therefore justified for the complete actual tail.

### Collective identity and all partition powers

For a finite family, expansion of (D11) assigns to an index tuple the
product, over its equality classes of size \(m\), of

\[
 \sum_{\pi\text{ partition of }[m]}
       \prod_{C\in\pi}(-1)^{|C|-1}(|C|-1)!.
\]

Interpreting each factor as the signed number of cycles gives the sum
of permutation signs. It is one for \(m=1\) and zero for \(m\ge2\),
by composing with a fixed transposition. Thus the identity keeps
precisely the ordered distinct-index tuples, with coefficient one.

After removing its all-singleton partition, every term has the form
\(Z^r\prod_i p_{h_i}\), with \(h_i\ge2\),
\(r+\sum_i h_i=12\), and \(0\le r\le10\). There is no
\(r=11\) term. For each fixed \(h\ge2\), the divisor envelope
gives

\[
 \sum_{d>Q}A_d^h\ll_\eta Q^{1-3h/4+\eta}.
\]

One may choose the input divisor exponent smaller than both the desired
output loss and a fixed fraction of \(3h/4-1\); consequently the
summed exponent is strictly below minus one for every desired
\(\eta>0\). The finitely many losses can be absorbed in the final
\(T^\epsilon\).

Bounding the power sums in supremum and using the complete \(r\)-th
moment of \(Z\) gives exactly (D13). Maximizing the number of
nonsingleton blocks gives the following full ledger:

| Singleton count \(r\) | Largest exponent among its partitions |
|---|---:|
| 0 | \(-1/5\) |
| 1 | \(-3/10\) |
| 2 | \(0\) |
| 3 | \(-1/10\) |
| 4 | \(1/5\) |
| 5 | \(1/10\) |
| 6 | \(2/5\) |
| 7 | \(3/10\) |
| 8 | \(3/5\) |
| 9 | \(1/2\) |
| 10 | \(8\beta-1/5\) |

For \(r\le9\), the relevant lower moment costs at most
\(T^{1+\epsilon}\), since \(7\beta<1\). The last exponent
exceeds \(4/5\) since \(\beta>1/8\), and is the maximum.
This proves the candidate's error \(8\beta-1/5\), including
every partition, and shows that it is less than \(21/25\).

The proof estimates a collective signed regrouping. It does not claim
that the sum of the absolute values of all individually expanded
repeated-label tuples has this small mass. This distinction is essential
and is handled correctly.

### Infinite limits, complete equivalence and Fourier normalization

For fixed \(T\), \(\sum_d A_d=\sum_n|a_n(T)|<\infty\).
Hence the class sums, power sums and twelvefold sums converge uniformly
in \(R\); the absolute twelvefold majorant is
\((\sum_d A_d)^{12}\). The finite identity therefore passes to the
infinite family and can be integrated against \(w(R/T)dR\).
The estimates are then applied to the infinite \(Z\) and power sums.
No uniform physical supremum for arbitrary finite subfamilies is needed.

The low part of the full physical moment costs
\(T+V_0^{10}+TV_0^{20/13}\), whose largest exponent is \(29/25\).
This proves the first equivalence. The two scalar power inequalities
between \(B=L+Z\) and \(Z=B-L\), together with the head exponent
\(15/13\), prove the next equivalence; the margin is exactly
\(29/25-15/13=2/325\). They are inequalities, not an assertion that
all mixed terms have the smaller additive error from (D2).

The absolute error integral gives
\(|M_{12}(Z)-I_{12}|\ll T^{8\beta-1/5+\epsilon}\), proving the
last equivalence. It also gives the stated lower bound on the possible
negative part of \(I_{12}\), so a one-sided upper estimate suffices.
The candidate's separate high-event check has the correct constant:
\(\|L\|_\infty/V_0\ll T^{-1/250}\), and eventually
\(|Z|>|B|/2>V_0/2\) on the original high event. The shifted
threshold is explicitly paid.

Finally, expanding each real cosine gives the coefficient
\(2^{-12}e(-3\sum_j\epsilon_j/8)\). The substitution \(R=Tu\)
gives \(T\widehat w(-T\Delta)\), with the candidate's sign.
Distinct squarefree classes make every \(\Delta\) nonzero by the
accepted algebraic independence statement, but give no usable
quantitative lower bound for \(|T\Delta|\). The window transform
continues to encode the physical displacement. Equation (D16) is
therefore the correct remaining signed, finite-window problem.

## 4. First doubtful or unproved step

There is no unproved step in the narrow reduction (D1)--(D4) found in
this review. Its first remaining unproved mathematical assertion is the
target-sized estimate for the signed integral (D16), namely
\(|I_{12}(T)|\ll_\epsilon T^{29/25+\epsilon}\), or its stated
one-sided alternative.

Nonzero radical differences may be very small; exact independence does
not justify discarding their finite-window contribution. The reduction
does not provide that estimate, a complete physical moment improvement,
or a pointwise exponent improvement. It would also be incorrect to
replace (D3) by an additive approximation to \(M_{12}(B_T)\) with
the same error; no such claim occurs in the candidate.

## 5. Controls and outcomes

* **Actual coefficients and class one — PASS.** The prime-factor
  comparison keeps representation multiplicity, vanishing classes,
  powers of two, \(d=1\), and all square factors. No model coefficients
  replace the arithmetic ones.
* **Integer cutoff and real endpoints — PASS.** For real \(T\ge2\),
  \(Q\ge1\) and \(Q\asymp T^{2/5}\); all estimates survive the
  floor, and the finite covering argument has real radius endpoints.
* **All signs and absolute anchor — PASS.** Class functions are real,
  their full cosine expansions use every sign, and the Fourier factor
  in (D16) retains the window displacement.
* **Exact versus near and nonpairing — PASS.** The collective identity
  includes all repeated classes, including nonpairing relations and
  nonzero repeated-class frequencies. Distinct-class independence is
  used only to exclude exact zero frequencies, not to assert a finite
  time cancellation estimate.
* **Masks, levels and tails — PASS.** The finite accepted mechanism
  permits zeroed coefficients and arbitrarily small positive block
  levels. Every block and the uniform infinite Schwartz tail remain.
  The actual tail supremum uses \(B-L\), not arbitrary-mask transfer.
* **Finite algebra — PASS.** With fewer than twelve indices the
  permutation identity gives zero; with \(m\) equal values it gives
  the falling factorial \((m)_{12}\). Every non-singleton partition
  appears in the exponent ledger above.
* **High-event and integrand costs — PASS.** The low complement is
  bounded completely, the threshold shift is explicit, and the power
  inequalities pay the mixed head-tail terms. The claimed conclusion
  is an equivalence of bounds, not an additive expansion for \(B\).
* **Source and independence scope — PASS.** Only accepted dependency
  interfaces are used. This is a NONBLIND review of the complete
  candidate, not the separately required statement-only rederivation.
* **Full-quarter scope — PASS.** The open order-twelve bound would
  give only \(102/325\). The one-pair term at higher fixed order
  retains a possible cost linear in the order through
  \(Q^{-1/2}T^{(p-4)\beta}\). No sufficient unbounded-order family
  is claimed.

## 6. Dependencies and exact artifacts used

New material read for this review was restricted to:

1. `rounds/codex-managed/gc-actual-radical-high-values/candidates/complete_distinct_radical_reduction.md`,
   at the exact candidate hash recorded above.
2. `proofs/kernels/gc_weighted_square_root_exact_resonance_mass.md`.
3. The accepted exact-resonance node in `state/proof_obligations.yml`.

The previously permitted protocol, graph, round216 context and accepted
round204 kernel were retained from the completed assigned task. Its own
report remains frozen and was not edited. No sibling discovery report,
blind report, conductor ledger or unlisted historical reference was read
for this review. No web source was opened or added during this review.

The review uses the accepted source dependencies as specified, plus
the explicit algebra, tail estimates and moment calculations written
above. All controls are analytical; no computation serves as proof.

## 7. Recommended state effect

**GREEN; eligible for narrow promotion after the other required seams
and the conductor's validated State Patch.** Accept only the complete
head moment, collective repeated-class error and bound equivalence,
with the remaining signed integral and full-goal limitations explicit.
No target estimate, new pointwise exponent, M1/M2/GAR parent or endpoint
should be promoted from this candidate.

This recommendation is bound to SHA256
`d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee`.
No shared proof-state mutation has been made. Stop this review here.
