# Round220 review of exact rounding and the enlarged operator control

## 1. Result and scope

**Verdict: GREEN for the actual amplitude/mask binding, the stated phase-deletion cost, and the counterexample to the enlarged complex certificate, with the scope distinctions recorded below.**

The reviewed current artifact is the conductor's rounding/control report at SHA256
5d24c346a285958510dba55fc085d9a785c0099b3df2b03497cdc0bc325c790f.
Its actual transformed amplitude satisfies the smooth multiplier hypotheses. Its stationary support is an interval mask, with the inherited endpoint convention. Exact rounding preserves the phase and transfers an all-row operator bound at logarithmic cost.

The enlarged complex certificate is indeed false on the displayed class of separated radii. This does not refute the complete real sine energy at actual high points. The selected sine rows in the counterexample vanish identically, and no high-point property is established.

Two qualifications are material and consistent with the conductor's stated scope:

1. The displayed power-form certificate (C), with an unspecified constant, is not by itself a literal proof of the numerical \(1/256\) absorption term. The advertised logarithmic and small-constant strengthening is required.
2. The counterexample's particular single-denominator test vector is already separable in \(j,a\). Its force is not restricted to nonseparable test vectors. It tests a larger coefficient/anchor class than the prescribed complete real signed high-point sum.

**Reviewer provenance:** I authored the frozen isolated smooth-mask lemma. This is an independent audit of its binding to the newly supplied application and of the conductor's control calculation; it is not an independent review of my own abstract proof.

## 2. Exact objects and hypotheses reviewed

The closed219 report and review supply the actual rectangle parameters

\[
 T\geq2,\quad 1\leq D\leq N\leq T^{3/2},\quad
 K=N/D,\quad A=T\sqrt N/D,\quad
 b_0=D/(\sqrt T\,N^{1/4}),
 \tag{1}
\]

with the original dyadic conventions on \(N,D\), and positive integer cofactors \(k\in[K/2,2K)\). The actual radii lie in \([T/2,2T]\). The complete transformed real sum is

\[
 V(k)=\sum_{j,a}\sigma_j\chi_4(a)\,
       \omega_{j,a}(k)\sin(2\pi kR_j^2/a),\qquad
 E=\sum_kV(k)^2,
 \tag{2}
\]

where positive odd \(a\) range over one fixed enlargement \(a\asymp A\), and

\[
 \omega_{j,a}(k)=
 \sqrt{T/R_j}(K/k)
 \Psi\!\left(\frac{2R_jk}{a\sqrt T}\right)s_{j,a}(k).
 \tag{3}
\]

The function \(\Psi\) is the actual real smooth mollifier transform, with the fixed Schwartz seminorm bounds used in the closed219 transform. Its sign is retained. The signs \(\sigma_j\) are those of actual high rectangle values in the intended energy problem.

The reviewed sufficient real-energy target is

\[
 E\leq \frac{J^2v^2TK}{256}
       +C_\eta T^{\rho+\eta}JAK,\qquad
 \rho=\frac{208}{2625}.
 \tag{4}
\]

The closed219 normalization is consistent:
\(b_0^2AK=N\), and for its original
\(P_0=J^2v^2N^{3/2}/(64K)\),
\(P_0/b_0^2=J^2v^2TK/64\).
Its separately paid sharp-transform error remains an input here; the new phase-deletion error is not silently identified with that old error.

Round exactly by
\[
 R_j^2=M_j+\delta_j,\qquad M_j\in\mathbb Z,\qquad
 \delta_j\in[-1/2,1/2],
 \tag{5}
\]
with either nearest-integer choice permitted at a tie. The complex matrix used for the stronger certificate is
\[
 H((j,a),k)=e(M_jk/a).
 \tag{6}
\]
Its all-row bilinear operator norm is denoted by \(\Lambda\).

The conductor's illustrative power certificate is

\[
 \Lambda^2\leq C_\eta
 \left(T^{\rho+\eta}K+\frac{Jv^2TK}{A}\right).
 \tag{C}
\]

Its claimed counterexample concerns uniform validity on general admissible separated radii, not validity on a family already proved to be actual aligned high points.

## 3. Derivation and application audit

### Actual smooth factor

In the normalized column coordinate \(t=k/K\), (3) has the smooth factor

\[
 f_{j,a}(t)=\sqrt{T/R_j}\,t^{-1}\Psi(c_{j,a}t),
 \qquad c_{j,a}=\frac{2R_jK}{a\sqrt T}>0.
 \tag{7}
\]

For \(r=0,1,2\),
\[
 c_{j,a}^{\,r}\Psi^{(r)}(c_{j,a}t)
 =t^{-r}(c_{j,a}t)^r\Psi^{(r)}(c_{j,a}t).
 \tag{8}
\]
The fixed Schwartz seminorms bound the right side uniformly on \(t\in[1/4,3]\); \(\sqrt{T/R_j}\) and the necessary powers of \(t^{-1}\) are also bounded. Applying the product rule to (7) therefore gives the required uniform \(C^2\) norm. This argument applies even when the argument of \(\Psi\) is large, and does not replace \(\Psi\) by a positive envelope in the exact identity.

The exact residual factor is
\[
 e(\delta_j k/a)=e((\delta_jK/a)t).
 \tag{9}
\]
The scale identity is
\[
 K/A=\sqrt N/T\leq T^{-1/4}.
 \tag{10}
\]
Because the actual denominator range is \(c_0A\leq a\leq C_0A\), the literal lower-bound parameter in the abstract lemma is \(c_0A\), not necessarily the nominal \(A\). This fixed enlargement changes only constants: \(K/(c_0A)\ll T^{-1/4}\), and the lemma's controlled large-ratio version also covers the bounded initial \(T\)-range. There is no power loss or missing parameter restriction here.

### Actual stationary interval and endpoint binding

For a fixed row \((j,a)\), write \(c=4R_j^2/a^2>0\). Then
\[
 d_a=ck,\qquad d_ak=ck^2.
 \tag{11}
\]
The divisor constraint \(D\leq d_a<2D\) and product constraints \(N\leq d_ak<2N\), \(d_ak\leq Z\), pull back to intervals in positive \(k\). Intersecting them with the original cofactor range is still one interval.

The stationary star belongs to this aggregate interval. When several constraints meet at one endpoint, its value is the inherited endpoint value, not an independently multiplied collection of half weights. Distinct saddle endpoints carry the inherited half contribution. The closed219 convention assigns an empty interval no main stationary mass, and already charges isolated literal original samples to the transform's endpoint error. These cases yield precisely the empty, singleton, or half-endpoint masks covered by the abstract lemma.

No derivative of a star or of an endpoint indicator is required. There is no regularity assumption across \(j\) or \(a\). Thus the actual amplitude and its complete support bind to the lemma without smoothing an arithmetic mask.

### Exact complex-to-real transfer and its cost

Let
\[
 Z_+(k)=\sum_{j,a}\sigma_j\chi_4(a)\omega_{j,a}(k)
                            e(R_j^2k/a).
 \tag{12}
\]
All displayed coefficients are real, so \(V(k)=\operatorname{Im}Z_+(k)\). Equivalently the two complex phase signs pair exactly as in the closed219 sine identity; neither is dropped from that identity. The negative rounded matrix is the conjugate of (6) and has the same all-row operator norm.

The smooth-mask lemma gives an operator cost \(C\log(2+K)\), where the fixed coefficient seminorms and fixed denominator enlargement are included in \(C\). The number of combined rows is \(O(JA)\), and the prescribed input vector \(u_{j,a}=\sigma_j\chi_4(a)\) has squared norm at most \(CJA\). Therefore

\[
 E\leq\sum_k|Z_+(k)|^2
 \leq C_*JA\log^2(2+K)\,\Lambda^2.
 \tag{13}
\]

This is the exact implication available from an all-row certificate. It does not estimate \(\Lambda\).

In particular, define \(\Xi=C_*\log^2(2+K)\). A literally sufficient normalized operator input for (4) would have the form

\[
 \Lambda^2\leq
 \frac{Jv^2TK}{256\,\Xi A}
 +\frac{C_\eta}{\Xi}T^{\rho+\eta}K.
 \tag{14}
\]

The logarithm in the second term can be absorbed by suitably allocating an arbitrarily small power loss. The quadratic absorption term needs its own displayed small-constant/logarithmic margin; an arbitrary constant in (C) does not supply that margin. The conductor explicitly describes (C) as an illustrative power bound and qualifies its sufficiency by a sufficiently strong version. With that qualification, there is no implication gap. Disproving even (C) disproves any stronger uniformly quantified version that would imply (14).

### Literal phase deletion has the stated separate cost

Uniformly on the actual rows,
\[
 |e(\delta_jk/a)-1|\ll K/A.
 \tag{15}
\]
The amplitude is uniformly bounded and there are \(O(A)\) denominators. Hence replacing the phase by its rounded phase causes at most \(CK\) error in one fixed-\((j,k)\) denominator sum. After the \(J\) actual signs are summed, the error in the vector \(V\) is at most \(CJK\) per cofactor. There are \(O(K)\) cofactors, so

\[
 \|\Delta V\|_2\ll JK^{3/2},\qquad
 \|\Delta V\|_2^2\ll J^2K^3.
 \tag{16}
\]

The ratio of this squared error norm to the real-energy absorption scale \(J^2v^2TK\) is \(O(K^2/(Tv^2))\), as stated in the control.

This is a bound for the energy of the error vector, not an assertion that
\(|E-E_{\rm rounded}|\leq CJ^2K^3\) without cross terms. A use in an energy upper bound must also invoke, for example,
\(\|V\|_2^2\leq2\|V_{\rm rounded}\|_2^2+2\|\Delta V\|_2^2\),
or the appropriate Young inequality with priced constants.

For one physical rectangle, summing the \(O(K)\) error over \(O(K)\) cofactors and restoring \(4N^{-3/4}b_0\) gives

\[
 O(N^{-3/4}b_0K^2)=O(K/\sqrt T).
 \tag{17}
\]

The control correctly treats (16)--(17) as upper costs, not lower bounds. At the scale example below, the nominal ratio in (16) has exponent \(73/250>0\), so the known necessary scale conditions do not force this crude upper cost to be negligible. The actual counterexample itself has \(\delta_j=0\), however, so its deletion error is exactly zero. The two observations must not be conflated.

### Enlarged complex-row control

Take
\[
 N\asymp T,\quad D\asymp T^{1/4},\quad
 A\asymp T^{5/4},\quad K\asymp T^{3/4},\quad
 v=T^{13/125},\quad J\asymp T^{1/2}.
 \tag{18}
\]
These choices respect the original dyadic scales; for instance a subsequence \(T=2^{4r}\) permits the exact powers for \(N,D\).

Choose an odd denominator \(a_0\asymp A\) inside the fixed allowed enlargement. The interval
\[
 \left[T^2/a_0,\ (6T/5)^2/a_0\right]
\]
has length \(11T^2/(25a_0)\asymp T^{3/4}\). It therefore contains more than the required \(J\asymp T^{1/2}\) distinct integers for all large \(T\). Choose such integers \(q_j\), and set
\[
 M_j=a_0q_j,\qquad R_j=\sqrt{M_j},\qquad\delta_j=0.
 \tag{19}
\]

Then \(T\leq R_j\leq6T/5\). Distinct selected integers give
\[
 |R_j-R_l|=\frac{a_0|q_j-q_l|}{R_j+R_l}
 \geq a_0/(3T)\asymp T^{1/4},
 \tag{20}
\]
which is much larger than \(N^{-1/2}\asymp T^{-1/2}\).

For every integer cofactor,
\[
 H((j,a_0),k)=e(q_jk)=1.
 \tag{21}
\]
The selected \(J\)-by-\(n\) submatrix is all ones. Unit constant vectors on its rows and columns give
\[
 \Lambda^2\geq Jn\asymp JK.
 \tag{22}
\]

Dividing (C) by \(JK\) would imply, up to fixed constants,
\[
 1\ll_\eta T^{\rho+\eta-1/2}
               +T^{26/125+1-5/4}
 =T^{\rho+\eta-1/2}+T^{-21/500}.
 \tag{23}
\]
For fixed \(\eta<1/2-\rho\), the right side tends to zero. Any fixed logarithmic loss is still dominated by these negative powers. This verifies the claimed failure of the uniformly quantified enlarged complex certificate.

### Why that control does not refute the actual target

For the same selected denominator,
\[
 \sin(2\pi kR_j^2/a_0)=\sin(2\pi kq_j)=0
 \tag{24}
\]
for every cofactor. Thus the selected rows of the exact real sine matrix vanish even before imposing any actual moving amplitude. In the complete sine Gram identity, this is precisely cancellation between the difference cosine \(1\) and the sum cosine \(1\). Retaining only one complex branch loses that cancellation.

The falsifying row vector is supported at \(a_0\), whereas the actual vector uses every denominator with its prescribed \(\sigma_j\chi_4(a)\). In fact the test vector is already of the form \(x_jy_a\), with \(y\) supported at \(a_0\); one should not describe this particular obstruction as requiring nonseparable row vectors. What matters is the enlarged coefficient freedom, complex branch, and enlarged anchor class.

The radii in (19) were not shown to satisfy \(|H(R_j)|>v\), to carry actual high-point signs, or to form a maximal high-point selection. Their separation is proved; their high-point status is not. Other denominator rows in the physical sine energy are neither bounded from below nor evaluated by this control.

Finally the known necessary high-rectangle restrictions do not exclude the scales (18):
\[
 N\gg v^4,\qquad
 D\gg T^{-13/42-\eta}v^2N^{29/84}.
 \tag{25}
\]
At \(N\asymp T\), the second right-hand exponent without the small loss is
\[
 26/125+1/28=853/3500<1/4=875/3500.
 \tag{26}
\]
Equivalently, the associated scalar ceiling allows exponent \(3/28\), while
\(13/125<3/28\), with gap \(11/3500\).
These are only compatibility checks on necessary conditions. They do not establish the existence of any actual high point at these radii.

## 4. First unproved step and correction status

The first unproved arithmetic step remains the complete real signed energy estimate (4) for actual aligned high points, with the actual moving coefficients and all difference and sum aliases. The multiplier bound and exact rounding do not prove it.

No substantive correction to the reviewed current control is required for its expressly stated scope. The following interpretation must remain attached:

- use the fixed lower endpoint \(c_0A\) of the denominator enlargement when binding the abstract lemma;
- retain the logarithmic and numerical margin before claiming literal sufficiency for the \(1/256\) term;
- read the deletion quantity as an error-vector norm, with cross terms handled on use;
- retain the enlarged-class and real-sine distinctions in the counterexample.

The current control already makes the essential qualifications. The details above make their exact mathematical content explicit.

## 5. Controls and outcomes

- Actual coefficient normalization and real sign of \(\Psi\): GREEN.
- Uniform scaled \(C^2\) bounds, full \(a\asymp A\) enlargement, and bounded initial \(T\): GREEN.
- Aggregate interval support, coincident constraints, stars, empty and singleton sections, and \(K=1\): GREEN.
- Exact rounding for both complex signs and recovery of the real sine: GREEN.
- Operator-to-energy factor \(JA\log^2(2+K)\), with numerical absorption qualification: GREEN.
- Per-row deletion \(O(K)\), squared error norm \(O(J^2K^3)\), and physical restoration \(O(K/\sqrt T)\): GREEN as upper costs only.
- Availability of \(J\) integers, positive radii in range, and the required separation: GREEN.
- All-ones complex submatrix, \(\Lambda^2\gg JK\), and exponent \(-21/500\): GREEN.
- Exact zero of the same real sine rows, restricted denominator support of the test vector, and absence of any high-point claim: GREEN.
- Necessary scale compatibility and non-sufficiency of those restrictions: GREEN.

No new experiment, new source, numerical test, or additional theorem was introduced. This review does not independently certify the author's own isolated multiplier proof.

## 6. Exact artifacts and reviewer provenance

Newly read and independently hashed for this review:

1. protocol.md — SHA256 f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
2. rounds/codex-managed/gc-complete-anchored-divisor-energy/reports/joint_cofactor_dispersion.md — SHA256 cbb7e8de456bb37c871eafaf21ffb4ecedeb36e7aac50b1719275d13cb1fef81.
3. rounds/codex-managed/gc-complete-anchored-divisor-energy/reviews/independent_dispersion_review.md — SHA256 45f3b7c76a1297730ebc142ec0f98e2fd35635915a84fd278289cfee12e8b184.
4. rounds/codex-managed/gc-full-goal-arithmetic-source-review/controls/conductor_rounding_and_operator_control.md — SHA256 5d24c346a285958510dba55fc085d9a785c0099b3df2b03497cdc0bc325c790f, matching the dispatched claimant hash.

The abstract multiplier input is my own already frozen report:
rounds/codex-managed/gc-full-goal-arithmetic-source-review/reports/blind_smooth_mask.md,
SHA256 e27659b89c33da6c8216f5817351edfa1a3fd269ffaeb8d8c1e51e6ce180e33b.
That frozen hash was supplied by the conductor; its file was not reread or changed in this review. The report's isolated statement hash was
97c84fcd8befb47401c11076d4afa49c55d5708df31ec9c79dffce9ac3c24459.

Role: NONBLIND same-round application reviewer, 2026-09-28. Isolation ended before the present files were supplied. Prior round217--219 and current isolated-lemma history is retained and disclosed. This review independently checks the newly supplied application and finite control, but authorship of the abstract lemma prevents counting it as an independent review of that lemma.

No files beyond the four newly authorized artifacts were read for this review. In particular no current sibling, graph, manifest, external source, or strategy was opened. No shared state or original artifact was edited. Only this assigned review was written.

## 7. Recommended state effect

**Close this exact-hash application/control seam GREEN and retain it as bounded strategy evidence.**

The uniformly quantified enlarged complex certificate is refuted. The actual complete real signed energy, its high-point hypothesis, and the full target remain open. Exact smooth-phase and interval transference is useful infrastructure, with no complete-bound or exponent credit.

No graph mutation, synthesis, successor decision, or further task is undertaken. This review ends here.
