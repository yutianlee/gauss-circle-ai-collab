# Round 231: nonauthor harmonic-pooling seam review

Campaign: round231_harmonic_admission, admission selection only.  
Task: harmonic_pooling_seam_review.  
Role: nonauthor line/seam reviewer for the conductor's full harmonic proof; author of the separately frozen arithmetic input, disclosed below.  
Generated: 2026-10-11 03:04:03 UTC.  
Supplied graph provenance tag, not independently read: a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.  
Candidate reviewed: strategy/round231_harmonic_admission/conductor_harmonic_obstruction.md.  
Exact candidate SHA256: 83D83C24EF7030EC125C1755856222D5F09BF691F6F2EE8602C79AAD6BD1CCC7.

## 1. Result

**PASS for the stated harmonic-pooling obstruction, with no mathematical repair required.** Under the candidate's exact hypotheses,

\[
\mathcal C_{\rm harm}(T)
=\sum_{\substack{d_1,\ldots,d_{12}>Q\\
d_j\ {\rm squarefree,\ pairwise\ distinct}}}
\left|\int w(R/T)\prod_{j=1}^{12} f_{d_j}(R)\,dR\right|
\gg T^{5/2}.
\]

The complete infinite harmonic sums are pooled inside each integral before its absolute value. The proof actually makes each integral positive on a selected set of distinct label tuples of sufficient weighted mass, after paying the entire harmonic tail and all bounded nonproportional vectors.

The actual arithmetic majorant, rational saving, fixed-cutoff choice, weighted deletion argument, retained common multiples, phase normalization, and absolute convergence all pass. The lower bound refutes a per-label-tuple absolute-value upper bound with any exponent strictly below \(5/2\). It gives no lower bound for the signed sum across different label tuples or the complete moment.

**Scope qualification:** The candidate's references to accepted216/204 and their restoration exponents were not independently source-audited; those artifacts are outside this assignment's permitted context. This does not affect the standalone obstruction proof. There is no claim here to validate that external restoration bookkeeping.

## 2. Exact statement and hypotheses

Use the candidate's actual coefficients

\[
r_2(n)=4\sum_{k\mid n}\chi_4(k)
\]

and full waves

\[
f_d(R)=\sum_{s\ge1}r_2(ds^2)(ds^2)^{-3/4}
\Psi(s\sqrt{d/T})\cos(2\pi R s\sqrt d-3\pi/4).
\]

The fixed mollifier is nonnegative, real, radial, smooth, supported in the unit disk, and of mass one. Therefore its transform \(\Psi\) is real and even, Schwartz, satisfies \(\Psi(0)=1\), and has absolute value at most one. No positivity of \(\Psi\) away from the selected base-frequency shell is assumed. The fixed smooth window \(w\) is nonnegative, supported in \([1/2,2]\), and has integral \(W>0\). The Fourier convention is the candidate's \(e(-u\xi)\) convention. The cutoff is \(Q=\lfloor T^{2/5}\rfloor\), and \(T\) is real and tends to infinity.

The arithmetic input is the elementary summatory estimate for \(r_2\), the elementary divisor bound, and the fixed-shell squarefree mass independently derived in the reviewer's frozen report. The proof requires no unlisted distribution theorem or square-root independence theorem.

All of \(c_0,H,\delta,\Lambda\) are fixed before the final lower threshold on \(T\). Constants may depend on the fixed functions and these choices. The conclusion is for every sufficiently large real \(T\), not merely for a subsequence.

## 3. Proof or derivation of the review

**A. Shell input and weight normalization: PASS.** The reviewer's frozen arithmetic report proves, for every fixed \(0<u<v\), the candidate's lower bound

\[
\sum_{\substack{uT\le d\le vT\\ d\ {\rm squarefree}}}r_2(d)
\ge \frac{\pi(v-u)}{24}T-O_{u,v}(\sqrt T\log(2T)).
\]

It includes prime \(2\) with factor one, every odd prime through \(\sqrt{vT}\), and the real endpoints. Thus a fixed sufficiently small \(c_0>0\) with \(\Psi(\sqrt x)\ge1/2\) on \([c_0,2c_0]\) gives

\[
M=\sum_d b_d\asymp T^{1/4},\qquad
b_d=r_2(d)d^{-3/4}\Psi(\sqrt{d/T})>0,\qquad
b_*\ll_\eta T^{-3/4+\eta}.
\]

The upper bound for \(M\) follows from the full shell summatory estimate, without requiring a squarefree upper-density result. Zero base coefficients contribute no shell mass. For squarefree \(d\), their cause is an inert prime of odd valuation, and that valuation remains odd in \(ds^2\); their entire class wave is zero. The retained labels satisfy \(d>Q\) for all sufficiently large \(T\), because \(d\ge c_0T\).

**B. Actual local factors and summable envelope: PASS.** A split prime \(p\equiv1\pmod4\) contributes \(2e+1\) to the ratio \(r_2(ds^2)/r_2(d)\) if \(p\nmid d\), and \(e+1\) if \(p\mid d\), where \(e=v_p(s)\). The latter is at most \(2e+1\). Inert primes and prime \(2\) contribute exactly one for retained \(d\). Therefore

\[
0\le r_2(ds^2)/r_2(d)\le
g(s)=\prod_{p\equiv1\ (4)}(2v_p(s)+1).
\]

Dividing by the positive base mollifier value gives the real normalized coefficients \(q_d(1)=1\) and

\[
|q_d(s)|\le \ell_s=2g(s)s^{-3/2}.
\]

The local inequality \(2e+1\le(e+1)(e+2)/2\) holds because the difference is \(e(e-1)/2\). Hence \(g(s)\le\tau_3(s)\), and

\[
K=\sum_s\ell_s
\le 2\left(\sum_{m\ge1}m^{-3/2}\right)^3<\infty.
\]

This convergence uses the divisor envelope, not the weaker pointwise bound \(g(s)\le s^{3/4}\).

**C. Common-multiple series and rational margin: PASS.** Induction gives \(2e+1\le3^e\). Every split prime is at least \(5\), and \(3^4=81<125=5^3\), so \(g(h)\le h^{3/4}\). The absence of split primes in \(2,3,4\) gives \(g(2)=g(3)=g(4)=1\). Thus

\[
S=\sum_{h\ge2}g(h)^{12}h^{-18}
\le 2^{-18}+3^{-18}+4^{-18}
5^{-9}+\frac1{8\cdot5^8}.
\]

The tail inequality is the ordinary decreasing-function comparison for \(\sum_{h\ge5}h^{-9}\). An entirely rational verification of the required strict bound is

\[
2^{-18}<\frac4{10^6},\qquad
3^{-18}+4^{-18}<\frac1{10^8},\qquad
5^{-9}+\frac1{8\cdot5^8}
=\frac{13}{15625000}<\frac9{10^7}.
\]

For the middle inequality both denominators exceed \(2\cdot10^8\); for example \(3^{18}=387420489\), and \(4^{18}>3^{18}\). Consequently

\[
S<\frac{491}{10^8}<\frac1{200000}.
\]

It follows that \(2S<1/100000<2^{-13}\), whence

\[
2^{-12}-2S>2^{-13}.
\]

This proves the candidate's rational margin without relying on its reported software checks.

**D. Complete harmonic product-tail budget and order of choices: PASS.** The bounds

\[
|f_d|,\ |f_d^{\le H}|\le Kb_d,\qquad
|f_d-f_d^{\le H}|\le R_Hb_d
\]

hold uniformly in \(R,T,d\) on the selected shell. The exact twelve-factor telescoping identity therefore bounds the product difference by \(12K^{11}R_H\prod_j b_{d_j}\). Integrating against the nonnegative window gives the candidate's \(2^{-16}TW\prod b_d\) once the fixed \(H\) satisfies its stated condition.

This pays all products having at least one harmonic above \(H\), regardless of resonance, coefficient sign, or how many coordinates are in the tail. No estimate scales with the count of infinitely many discarded vectors. Since \(K<\infty\), such an \(H\) exists and is fixed before \(T\).

The Fourier choices are also valid: the support of \(w\) gives \(\operatorname{Re}\widehat w(\xi)\ge W/2\) whenever \(|\xi|\le1/12\), by \(\cos(2\pi u\xi)\ge1/2\) for \(|u|\le2\). Smooth decay supplies a fixed \(\Lambda\) with the candidate's far-frequency bound. Also \(|\widehat w|\le W\), by nonnegativity.

**E. Weighted binning, repeated-label removal, and rank-two deletion: PASS.** The weighted ordered sixfold root sums have total mass \(M^6\) and lie in an interval of length \(O(\sqrt T)\). Bins of width \(\delta/T\) number \(O(T^{3/2})\). Pairing two sixfold tuples in the same bin yields mass at least \(M^{12}/O(T^{3/2})\gg T^{3/2}\), with

\[
\left|\sum_j\sigma_j\sqrt{d_j}\right|\le\delta/T,\qquad
\sigma=(1,1,1,1,1,1,-1,-1,-1,-1,-1,-1).
\]

For any specified equality \(d_i=d_j\), fix the common label and nine of the other ten labels. The remaining coordinate has coefficient \(1\) or \(-1\) in the near relation. Its root is confined to length \(O(1/T)\), and its norm to length \(O(T^{-1/2})<1\), so at most one integer norm completes it. Its mass is at most \(b_*\). The common label has weight \(b_d^2\), even if its two coefficients cancel. Thus the removed mass is at most

\[
\left(\sum_db_d^2\right)M^9b_*
\le M^{10}b_*^2\ll_\eta T^{1+2\eta}.
\]

For a bounded integer vector \(t\) not proportional to \(\sigma\), select a nonzero two-by-two minor of the two rows. Its determinant is a nonzero integer, hence has absolute value at least one. With the other ten norms fixed, the two near relations confine the remaining two roots to a parallelogram whose coordinate projections have length \(O_{H,\delta,\Lambda}(1/T)\). Each norm projection has length \(O(T^{-1/2})<1\). At most one ordered pair of integer norms can complete the tuple, and its weight is at most \(b_*^2\). Summing the other ten weights gives \(M^{10}b_*^2\).

There are only 66 equality pairs and at most \((2H)^{12}\) bounded vectors. These counts are fixed before \(T\). Taking any fixed \(\eta<1/4\) makes their entire deletion \(o(T^{3/2})\). This is a weighted count and does not confuse the number of completions with their potentially varying coefficients.

Finally, a bounded nonzero integer vector proportional to \(\sigma\) is exactly \(\pm h\sigma\), \(1\le h\le H\), because \(\sigma_1=1\). These vectors have rank one and are expressly retained.

**F. Phases, retained common multiples, and pooled positivity: PASS.** Set \(\Omega=\sum_j\sigma_j\sqrt{d_j}\). Expanding each cosine as two exponentials gives the factor \(2^{-12}\) and phase

\[
\exp\left(-\frac{3\pi i}{4}\sum_j\varepsilon_j\right).
\]

For either sign vector \(\varepsilon=\pm\sigma\), the sum of signs is zero, so the phase is one. The pair at harmonic one contributes exactly

\[
2^{-11}T\operatorname{Re}\widehat w(T\Omega)\prod_jb_{d_j}
\ge2^{-12}TW\prod_jb_{d_j}.
\]

Realness of \(w\) pairs its two Fourier values by complex conjugation; evenness of \(w\) is unnecessary.

The same balanced sign pattern occurs for \(\pm h\sigma\), because signs depend on the sign of the vector entries, not their magnitude. Their combined absolute contribution, summed over \(h\ge2\), is at most

\[
2^{-11}TW\prod_jb_{d_j}
\sum_{h\ge2}\prod_j|q_{d_j}(h)|
\le2STW\prod_jb_{d_j}.
\]

The factor \(2^{12}\) from the twelve normalized envelopes cancels the cosine normalization as in the candidate. This controls every possible sign change of the higher mollifier coefficients and needs no sign-coherence assumption.

For all retained nonproportional bounded vectors, \(|T\sum_jt_j\sqrt{d_j}|>\Lambda\). The sum of absolute normalized coefficients of the entire finite expansion is at most

\[
2^{-12}\sum_{\varepsilon\in\{\pm1\}^{12}}
\sum_{1\le s_j\le H}\prod_j|q_{d_j}(s_j)|
\le K^{12}.
\]

Thus their whole Fourier contribution costs at most \(2^{-16}TW\prod b_d\). Including the complete harmonic tail leaves a normalized lower bound greater than

\[
2^{-13}-2\cdot2^{-16}
=\frac6{65536}>\frac4{65536}=2^{-14}.
\]

Summation over the retained tuple weight \(\gg T^{3/2}\), followed by the factor \(T\), proves the claimed \(T^{5/2}\) obstruction.

**G. Absolute convergence and downstream interpretation: PASS within the stated scope.** With \(a_n(T)=r_2(n)n^{-3/4}\Psi(\sqrt{n/T})\), the area count gives \(\sum_{n\le T}|a_n|\ll T^{1/4}\). Dyadic blocks above \(T\), together with Schwartz decay, give the same bound for the tail. Thus

\[
\sum_n|a_n(T)|\ll T^{1/4}\qquad(T\ge1).
\]

For every fixed \(T\), this justifies all harmonic products, integrations, and label regroupings by absolute convergence. The total absolute certificate is at most \(TW(\sum_n|a_n|)^{12}\ll T^4\), so its definition is finite.

The proof takes a subset of a nonnegative sum of moduli. It does not delete the complementary terms of a signed sum. Accordingly, the proposed estimate \(\mathcal C_{\rm harm}\ll_\varepsilon T^{29/25+\varepsilon}\) for every \(\varepsilon>0\) is contradicted by choosing any \(0<\varepsilon<5/2-29/25=67/50\). An estimate for \(|\sum J_{\boldsymbol d}|\), or a complete moment after restoration, is not contradicted by this argument.

## 4. First doubtful or unproved step

No doubtful or unproved step remains in the standalone lower-bound argument under the hypotheses above. No proof repair is required.

The first statement in the candidate whose source-level validation lies outside this review is the assertion in Section 3F about the accepted216 head and repeated-class restoration errors, and the sufficiency of the \(29/25+\varepsilon\) benchmark for the complete moment. This reviewer was explicitly prohibited from reading those sources, so those claims remain externally attributed context here. They are unnecessary to prove the obstruction or its direct exclusion of exponents below \(5/2\).

The target-sized signed estimate across different label tuples remains mathematically unproved, exactly as the candidate states.

## 5. Required control tests and outcomes

All controls were analytical; no numerical experiments or source searches were used.

- **Actual coefficient control: PASS.** Prime \(2\) and inert primes contribute one; the smallest split prime is \(5\). In particular \(g(2)=g(3)=g(4)=1\). Replacing this by the generic \(\tau(s^2)\) value at \(s=2\) would give a single series term \(3^{12}/2^{18}>2\), invalidating the tiny common-multiple bound. The required saving is genuinely tied to the actual coefficients.
- **Rational margin: PASS.** The explicit rational comparisons in Section 3C prove \(S<1/200000\) and the claimed positive residual analytically.
- **Infinite mixed tail: PASS.** The twelve-factor telescoping estimate pays every product containing at least one index above the fixed \(H\), before any asymptotic counting.
- **Degenerate repeated coordinates: PASS.** Even if a repeated label cancels from the near relation, an outside coordinate still has coefficient \(\pm1\) and permits the claimed completion bound.
- **Rank-one control: PASS.** Vectors \(\pm h\sigma\) are not assigned a false rank-two deletion estimate. All their possible cancellation is charged by the actual \(S\)-bound.
- **Weighted rank-two completion: PASS.** A nonzero integer minor gives one possible ordered norm pair for sufficiently large \(T\), with weight at most \(b_*^2\), not unit weight.
- **Non-even window and signed higher harmonics: PASS.** Conjugate Fourier pairing and the absolute common-multiple bound cover both cases.
- **Fixed constants and real endpoints: PASS.** All cutoffs precede the \(T\) limit; shell counts and norm-spacing estimates hold for all sufficiently large real \(T\).
- **Downstream cancellation control: PASS.** No inference is made from a subset of positive pooled integrals to a lower bound on the complete signed sum.

## 6. Dependencies and exact artifacts used

Only the following files were read for this review:

- protocol.md;
- strategy/round231_harmonic_admission/conductor_harmonic_obstruction.md;
- strategy/round231_harmonic_admission/reports/blind_squarefree_mass.md.

The candidate hash is recorded at the top of this report. The frozen arithmetic report has SHA256 12AAF0A9FBB03786ABD862B3CC2DA11CDF25415EAFA02851F6F3E7F3087C0267, verified unchanged for this review. That arithmetic report is the reviewer's own prior statement-only derivation; this is disclosed rather than presented as a second independent author of the arithmetic seam. The full harmonic argument is conductor-authored, and this reviewer did not author its derivation.

No graph, restoration kernel, sibling report, historical argument, external source, or software control artifact was read. No child task was launched. The rational comparisons and all seam checks were rederived analytically. Only the assigned review report was written; the arithmetic report and candidate were not edited.

The final SHA256 of this report is supplied in the completion message after freezing the file, rather than embedded as a self-referential file hash.

## 7. Recommended state effect

**Retain the candidate as a reviewed scoped obstruction.** The core harmonic-pooling theorem passes this nonauthor seam review, with no requested repair. Do not promote a signed upper bound, complete-moment claim, pointwise improvement, or quarter theorem. Do not treat this review as a source audit of the externally cited accepted216/204 restoration statements.

No authoritative state change, synthesis edit, or successor-round design is made by this reviewer.
