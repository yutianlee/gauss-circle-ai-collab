# Round 209 independent high-values seam review

## 1. Result and review verdict

**GREEN, within the report's stated scoped-failure conclusions.** The discrete
mean-wave estimate, alternative centered pointwise route, actual centered
absolute-majorant control, weighted Gram diagonal, both deficit formulas and
the complete high-value envelope are correct. The report does not prove the
complete tenth gate, a pointwise improvement or a new accepted arithmetic
bound.

Campaign: `gc-complete-signed-tenth-moment`. Round: 209.
Role: independent nonblind seam reviewer, following completion of the
separate `signed_fifth_convolution` discovery task. Generated:
2026-09-27T15:14:01Z. Starting graph SHA-256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Analytical effort: 100 percent; no mathematical numerical experiment.

Reviewed artifact:
`rounds/codex-managed/gc-complete-signed-tenth-moment/reports/actual_tenth_high_values.md`.
Its reviewed final SHA-256 is recorded in Section 7. This review is not
statement-only isolation and makes no such claim.

## 2. Exact claims, hypotheses and review boundary

The report uses the actual finite block

\[
 H_N(R)=\Re\left(e(-3/8)\sum_n r_2(n)f_N(n)e(R\sqrt n)\right),
 \quad f_N(t)=t^{-3/4}\Psi(\sqrt{t/T})v(t/N),
\]

on \(I=[T/\sqrt2,\sqrt3T]\), where \(v\) is fixed real smooth and nonzero,
supported in \([1,4]\), and \(\Psi(0)=1\). The complete band is

\[
 T^{166/325}<N<T^{242/325},\qquad
 b=83/650,\quad\gamma=10b=83/65,\quad
 U_N=T^\gamma N^{-1/2}.
\]

The required moment bound is \(M_{10}(H_N)\ll_\varepsilon U_NT^\varepsilon\).
The accepted inputs retained by the report are the variance distribution,
the two-term complete large-value bound with \(q=136/13\), and the actual
supremum \(T^{\omega+\varepsilon}\), where
\(\omega=\min(\alpha/4,\beta,(1-\alpha)/2)\) and \(N=T^\alpha\).

I checked the following finite claims and their scope:

1. The accepted **unweighted** exponent-pair specialization bounds the
   discrete mean wave, and only that wave, at the displayed power.
2. A target-sized centered tenth moment would imply the same pointwise
   milestone by reproduction, without being identified with the original
   tenth-moment gate or the unmodified shell.
3. The centered actual coefficient expansion has a large termwise absolute
   ten-frequency integral; this says nothing comparable from below about
   its signed moment.
4. Positive arithmetic weighted Cauchy has the stated exact diagonal and
   loses the location of the window if used only through energy and a
   difference kernel.
5. Both inherited moment terms, their deficiencies and all levels of the
   sufficient missing distribution bound remain accounted for.

The exact source theorem is used only as already accepted and specialized
in the supplied Round204 kernel. I did not extend it to arithmetic weights
or independently reaudit the external paper.

## 3. Independent derivations and seam checks

### Mean-wave exponent and source interface

The supplied kernel, Section 3 equation (L5), gives for an unweighted
proper interval of length comparable to \(N\)

\[
 \left|\sum e(R\sqrt n)\right|
 \ll_\varepsilon T^\varepsilon R^{13/84}N^{97/168}
\]

when \(R\ge C_0\sqrt N\), with the source's exact monomial phase and
proper-interval extension. In the present band,
\(R\asymp T\) and \(T/\sqrt N\ge T^{204/325}\), so the hypothesis holds
uniformly for sufficiently large \(T\). A bounded initial range is absorbed
into constants. Splitting \([N,4N]\) into two ordinary dyadic intervals
costs only a fixed constant.

After scaling \(t=Ns\), the mask has supremum and total variation
\(O(N^{-3/4})\): \(s\) lies in a fixed positive compact interval and
\(N/T\le1\) keeps all required derivatives of
\(\Psi(\sqrt{N/T}\sqrt s)\) uniformly bounded. Partial summation therefore
gives

\[
 |M_N(R)|\ll_\varepsilon
 T^{13/84+\varepsilon}N^{97/168-3/4}
 =T^{13/84+\varepsilon}N^{-29/168}.
\]

The exponent decreases with \(\alpha\). At the lower boundary it equals

\[
 \frac{13}{84}-\frac{29}{168}\frac{166}{325}
 =\frac{303}{4550}<\frac{83}{650}=b.
\]

The strict gap is \(139/2275\); choosing the input epsilon smaller than
that gap makes the pointwise mean contribution harmless for the milestone.
No weighted exponent-pair statement is used here.

### Centering gives an alternative pointwise implication

The exact split \(H_N=M_N+C_N\) is valid. The centered block has Fourier
support in \([-2\sqrt N,2\sqrt N]\), and
\(|r_2(n)-\pi|\le r_2(n)+\pi\ll_\varepsilon n^\varepsilon\)
gives its global coefficient bound \(N^{1/4+\varepsilon}\).
The supplied reproduction proof therefore applies to \(C_N\), including
its off-window tail and the factor \(N^{1/20}\). If
\(\int_I|C_N|^{10}\ll U_NT^\varepsilon\), it yields

\[
 |C_N(R_0)|\ll N^{1/20}U_N^{1/10}T^\varepsilon
 =T^{b+\varepsilon},\qquad T\le R_0\le\sqrt2T.
\]

Adding the independently bounded mean wave suffices for the actual block
pointwise goal. The original outer blocks and tails can still be estimated
directly; they need not be replaced by centered blocks.

This implication does **not** prove a target-sized tenth moment for the
mean wave. For example, simply integrating the pointwise mean estimate
would cost \(T^{1+10(13/84-29\alpha/168)+\varepsilon}\), and no assertion
that this is at most \(U_NT^\varepsilon\) is made. The report also explicitly
declines to apply the unchanged shell bridge to \(C_N\). Thus its centered
alternative is not mislabeled as an equivalent reformulation of the
original complete tenth gate.

The exact summatory identity is
\(A(t)=P(t)-1+\pi\{t\}\), since the origin contributes one to the lattice
count. Smooth exterior boundary values vanish, so Stieltjes summation by
parts has no unpaid exterior endpoint term. Its absolute variation cost is

\[
 N^{\theta_{LY}}\left(N^{-3/4}+T N^{-1/4}\right)
 =N^{\theta_{LY}-3/4}(1+T\sqrt N),
\]

as stated. It is worse than the original coefficient bound on this band.
The missing cancellation is in the oscillatory integral, not in the known
summatory bound.

### Actual centered absolute-majorant control

For every positive integer \(n\), \(r_2(n)\in4\mathbb Z_{\ge0}\).
Consequently \(|r_2(n)-\pi|\ge4-\pi>0\), including the case \(r_2(n)=0\).
On a fixed interior subinterval where \(|v|\) is bounded below, the
continuity of \(\Psi\) at zero and \(N/T\to0\) give
\(\asymp N\) actual coefficients of absolute size at least
\(cN^{-3/4}\). Their absolute mass is at least \(cN^{1/4}\).

The positive five-root-sum measure thus has mass at least \(cN^{5/4}\)
and support length \(O(\sqrt N)\). Binning with width \(c_0/T\) uses at
most \(C T\sqrt N\) bins, so its squared bin masses sum to at least
\(cN^2/T\). For each same-bin pair, the exact oscillatory integral over
\(I\) has modulus at least \(cT\): either center the phase and bound its
real part or use the elementary sine formula. The permitted fixed
\(c_0\) can be chosen small enough for the whole interval.

The resulting \(\gg N^2\) lower bound is therefore valid for the
termwise absolute expansion. In the real cosine expansion, the selected
five-positive/five-negative sector has factor \(2^{-10}\), and the five
constant phase factors cancel their five conjugates. Possible signs of
the centered coefficients or of \(v\) cause no problem because this is
an absolute majorant. No such argument gives a lower bound for the signed
moment.

For the uncentered vector, summing \(r_2(n)\) on the chosen interior
subband gives a main term comparable to \(N\), with smaller accepted
discrepancy error; the same mass argument applies. The cost relative to
\(U_N\) is

\[
 (5/2)\alpha-\gamma=(5/2)(\alpha-4b)>0,
\]

with supremum \(38/65\) at the upper boundary. This lower bound includes
exact and nonexact relations, exactly as the report states. The displayed
perfect-square nonpairing control is also valid: both lists of positive
square roots sum to \(5m+5\), their multisets differ, and the corresponding
square arguments have positive \(r_2\).

### Weighted Gram diagonal and the location lost after Cauchy

In the positive measure \(\mu_n=r_2(n)\), aligning the sampled values and
applying weighted Cauchy gives exactly the report's inequality (17).
The Gram kernel is \(K_\mu(R_j-R_k)\), with the full ambient interval
\([N,4N]\); zero mask values are not an excuse to replace its diagonal.
The summatory formula yields
\(K_\mu(0)=3\pi N+o(N)\asymp N\), with endpoint conventions affecting
only smaller terms. Smooth bounded weights and a positive lower subband
give \(E_\mu\asymp N^{-1/2}\).

Thus the diagonal times energy is \(\asymp N^{1/2}\).
If a difference-kernel argument merely controls the off-diagonal and then
retains this term, it gives \(J V^2\ll N^{1/2}\) up to its other losses.
At separation \(\delta=N^{-1/2}\), maximal-set covering costs
\(\delta J\ll V^{-2}\). Even when the formal localization interval is
longer than \(I\), one whole interval remains. This checks the claimed
method cost; it is not an assertion that negative off-diagonal terms can
never cancel the diagonal for the actual vector.

The input summary after Cauchy retains only \(E_\mu\) and point
differences. It is invariant under simultaneous translation of the
evaluation points. The vector \(|f_N(n)|e(-R_*\sqrt n)\) indeed has
the same energy and produces an aligned peak \(\asymp N^{1/4}\) at
\(R_*\), throughout a sufficiently small fixed multiple of
\(N^{-1/2}\). This is a valid control of the information discarded by
the method. The report correctly refuses to call it an actual arithmetic
counterexample. No weighted analogue of the unweighted kernel theorem
is silently imported.

### Both deficits and the complete level envelope

The variance/bulk crossing is \(V_0=N^{13/220}\). Integrating variance
below it gives
\(T N^{-1/2}V_0^8=T N^{-3/110}\). Integrating the bulk bound above it
gives \(T V_0^{10-q}=T N^{-3/110}\); integrating the other term gives
\(W^8\). Here the entire required band has \(V_0>1\) for large \(T\),
and \(V_0<W\). Hence the report correctly preserves

\[
 M_{10}\ll T^\varepsilon
       (T N^{-3/110}+T^{8\omega}).
\]

Subtracting the target exponent gives
\(d_A=1-\gamma+26\alpha/55\) and
\(d_B=8\omega-\gamma+\alpha/2\).
The zero of \(d_A\) is exactly \(99/169\). Also
\(d_B-d_A=8\omega-1+3\alpha/110\), which is positive across the
whole band by checking the three linear branches and their endpoints.
The slopes of \(d_B\) are \(5/2,1/2,-7/2\), so its maximum is at
\(\alpha=1-2\beta\), with value \(7\beta-101/130\).

For \(V_c=T^{9/260}\), the low-level variance contribution is
\(T N^{-1/2}V_c^8=U_N\). The proposed envelope
\(D_N(V)\ll_\varepsilon U_NT^\varepsilon V^{-10}\) above \(V_c\)
integrates to \(O(U_NT^\varepsilon\log T)\), which can be absorbed
by choosing all input epsilon losses smaller than the requested output
epsilon. A fully literal ceiling is
\(W_\eta=C_\eta T^{\omega+\eta}\), with \(\eta>0\) fixed sufficiently
small and the constant from the actual supremum bound. Above this ceiling
the level set is empty, and \(\log(W_\eta/V_c)=O_\eta(\log T)\).
This supplies the precise interpretation of the report's
\(T^{\omega+o(1)}\) notation; it introduces no new hypothesis.

Comparing each known high-level term with the envelope gives exactly

\[
 V\le U_N^{1/8}=T^{83/520}N^{-1/16},\qquad
 V\ge(T/U_N)^{13/6}=T^{-3/5}N^{13/12}.
\]

The second threshold exceeds \(V_c\) exactly when
\(\alpha>99/169\). It can exceed the ceiling, so its unproved level
range cannot be discarded. These checks confirm that removing the
diagonal term alone does not settle the target.

Finally, the shell conversion is \(T^{-6}\) in the physical tenth
moment and \(T^6\) in the opposite direction. Integrating the tenth
power of the bridge error gives \(T^{-4+\varepsilon}N^{-10}\) and
\(T^{2+\varepsilon}N^{-10}\), respectively. The reproduction factor,
outer ranges, equality endpoints and sharp reconstruction are the
unchanged fully paid supplied bridge. They imply only the conditional
milestone \(102/325\).

## 4. First doubtful or unproved step

No error was found in the reviewed finite claims or their stated cost
comparisons. The first unproved mathematical input remains the report's
inequality (9), or a sufficient integrated replacement, for the actual
complete displaced-window high values. Its centered alternative needs
the corresponding centered moment or distribution estimate; the mean-wave
bound does not provide it.

The weighted-duality discussion is GREEN only with its stated method scope:
it concerns an argument that reduces the vector to energy and handles a
difference Gram kernel. It is not a universal impossibility theorem for
coefficient-sensitive arithmetic duality or for signed off-diagonal
cancellation. The report itself makes this distinction.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Actual coefficients | GREEN: centering uses the exact multiple-of-four property, and weighted duality uses the actual positive measure. |
| Accepted source interface | GREEN: the exponent-pair estimate is used only on unweighted partial sums in its high-parameter regime, followed by legitimate smooth partial summation. |
| Centered route versus original gate | GREEN: pointwise reproduction for the centered block is separate from the original moment and shell equivalence. |
| Complete scales and levels | GREEN: both inherited terms, the low-level integral, bulk threshold, upper ceiling and all required scales are retained. |
| Signed versus absolute | GREEN: every lower obstruction is explicitly a positive majorant or information-loss control, not an actual signed-moment lower bound. |
| Exact nonpairing relations | GREEN: the finite example is valid; exact and near terms remain included in the absolute binning result. |
| Real endpoints and costs | GREEN: actual window margins, masks, factor \(N^{1/20}\), diagonal, localization ceiling, shell powers and sharp reconstruction are paid. |
| Epsilon integration | GREEN: independently adjustable input losses and one logarithm give the stated output epsilon. |
| Full quarter and independence scope | GREEN: no full tenth gate, new pointwise exponent, M1/M2 closure or quarter claim; this is an independent nonblind seam review. |

No numerical experiment or new external source was used.

## 6. Dependencies and exact artifacts read

- `rounds/codex-managed/gc-complete-signed-tenth-moment/reports/actual_tenth_high_values.md`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`,
  especially the exact source specialization, equations (L5)--(L7),
  coefficient scope and generic aligned control.
- `rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md`,
  already read during the completed discovery assignment, for the supplied
  reproduction/bridge, complete complementary ranges and both moment terms.
- The previously read `protocol.md`, Round209 manifest and strategy packet
  determine ownership, frozen scope and required seams. The relevant
  authoritative graph scope and exact repaired \(\beta\) were also read
  during the completed discovery assignment.

Only the newly assigned review file was written in this seam task. The
claimant report, the completed rational-convolution report and all shared
state were left unchanged. This review does not claim statement-only
isolation or an independent external source-card audit.

## 7. Recommended state effect and final reviewed hash

**GREEN: accept this seam review for the scoped high-values failure report.**
Retain the complete tenth-moment gate, both deficits and the precise
high-level residual as open. No accepted graph or proof-draft promotion
of a complete arithmetic bound is warranted by this report.

Final reviewed artifact:
`rounds/codex-managed/gc-complete-signed-tenth-moment/reports/actual_tenth_high_values.md`.

Final reviewed SHA-256:
`8fb9d01885057aa2981da9a746890968212a73103b7a079fcbc65e640d598df9`.

No successor work or shared-state edit is authorized by this review.
