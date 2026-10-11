# Round210 independent nonblind review of the conductor transfer ledger

Campaign: `gc-signed-near-frequency-cancellation`  
Task: `independent_conductor_transfer_review`  
Role: independent NONBLIND seam reviewer; separate follow-up to the completed isolated task  
Generated: 2026-09-27 15:33:51 UTC  
Reviewed graph identifier, as reported by the source: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`  
No shared state was read or edited for this review. The original isolated report is unchanged.

## 1. Result and verdict

**GREEN for the revised C1--C9 within their stated scope.** C1--C2 are sufficient bin-energy transfers. C3 is an exact finite differencing identity followed by Cauchy. C4--C6 give a sufficient positive-part moment route, with a necessary diagonal payment only for that separated positive certificate. C7--C9 rule out the explicitly specified absolute Abel certificate. They do not lower-bound the actual signed correlations or moment and do not establish a necessary condition for the true arithmetic theorem.

Before issuing GREEN, I requested four repairs: the exact original label and strict-prefix convention, the smooth extension of complete fixed-label blocks, removal of an unnecessary global positivity assumption on the fixed mask, and a precise definition of the rejected positive certificate and its optimistic trivial cap. The conductor applied those repairs. This verdict binds the revised ledger SHA256 given in section 6, not the earlier version.

The new signed bin-energy and positive-part shift-moment bounds remain unproved. Neither the available exact-frequency energy nor any calculation in this ledger supplies them. No improved tenth moment, pointwise exponent, or full-quarter result follows unconditionally.

## 2. Exact statement, hypotheses and scope checked

The parameters are

\[
b=83/650,\quad \gamma=10b=83/65,\quad
N=T^\alpha,\quad 166/325<\alpha<242/325,
\]

with \(I=[T/\sqrt2,\sqrt3T]\), \(X=T^2\), \(J=[X/2,3X]\), physical tenth-energy target \(U=T^\gamma N^{-1/2}\), and rational squared-energy target \(G=T^6U\). These are energies, not square roots of energies.

For the centered route, write

\[
c_n=r_2(n)-\pi,\quad
f(t)=t^{-3/4}\Psi(\sqrt{t/T})v(t/N),\quad
u_n(R)=c_nf(n)e(R\sqrt n),\quad F(R)=\sum_nu_n(R).
\]

Here \(v\) is fixed, real, smooth, nonzero and supported in \([1,4]\). A closed interior interval on which it has a fixed nonzero sign exists. The source normalization \(\Psi(0)=1\), together with \(N/T\to0\) uniformly in this band, makes \(\Psi\) uniformly positive there for large \(T\). A sufficiently small fixed \(\delta>0\) gives a common interval of length comparable to \(N\) on which

\[
f(t+h)f(t)\gg N^{-3/2}\qquad(1\leq h\leq\delta N).
\]

No positivity of \(v\) away from this interval is needed. Smooth zero extension at the exterior support boundaries is understood. The shifts and differencing length are integers, \(2\leq L\leq\delta N\).

To avoid the source's harmless reuse of a letter in different subsections, this review writes \(D_{\rm cut}\) for the rational hyperbola cutoff and \(D_{\rm diag}=\sum_n|u_n|^2\) for the centered diagonal energy.

The rejected pointwise certificate is exactly the one that retains \((N/L)D_{\rm diag}\), adds absolute Abel remainder bounds with positive Fejer weights, assigns zero cost to the main-term contribution, and credits no negative main-term or remainder cancellation against the diagonal. The additional error-only trivial cap is explicitly an optimistic grant. It is not asserted to bound a remainder after a nonzero main term has been subtracted.

The inherited centering argument is used only for a sufficient pointwise route: the discrete mean is separately pointwise safe, and local reproduction can be applied to the centered wave. No equivalence between its centered moment and the unmodified rational tenth-moment gate is asserted or needed.

## 3. Independent derivation and seam checks

### C1: scaled derivative transfer — GREEN

Set \(t=x/X\), \(g_j(t)=\eta(t)B_j(Xt)\). Fourier transformation gives
\(\widehat{\sum_j e(jt)g_j}(\xi)=\sum_j\widehat g_j(\xi-j)\).
Cauchy with weights \(1+4\pi^2(\xi-j)^2\), and the uniformly bounded reciprocal-weight sum over \(j\in\mathbb Z\), gives

\[
\left\|\sum_j e(jt)g_j\right\|_2^2
\ll\sum_j(\|g_j\|_2^2+\|g'_j\|_2^2).
\]

The derivative is \(g'_j=\eta'B_j(Xt)+X\eta B'_j(Xt)\). Multiplication by the Jacobian \(X\) gives exactly the integrals of \(|B_j|^2+X^2|B'_j|^2\) in C1, with fixed cutoff constants. This agrees with the independently derived isolated transfer, without using a frequency-count factor. It is an upper bound only. Its derivative-free and unmodulated-bin variants fail under the source's explicit analytic controls.

### C2: the actual maximum-label prefix — GREEN after repair

The allowed rational coefficient formula contains

\[
s_*(L_0/b,x/(D_{\rm cut}b))
=\sum_{j\leq L_0/b,\ j<x/(D_{\rm cut}b)}\frac{\chi_4(j)}j.
\]

Put \(\ell=bj\). The two restrictions become \(\ell\leq L_0\) and \(D_{\rm cut}\ell<x\). Thus the complete B arm really can be written as

\[
\sum_{1\leq\ell\leq L_0}\mathbf1_{D_{\rm cut}\ell<x}B_\ell(x).
\]

The coefficient inside each fixed \(B_\ell\) is obtained by summing over divisors \(b\mid\ell\) and the original admissible numerators; its factor from the displayed coefficient is
\(2ih(x)\chi_4(a)\chi_4(\ell/b)/\ell\), times the unchanged Fourier multiplier. Negative frequencies retain the source's conjugate convention. No coefficient sign or multiplicity is discarded.

The exact integer cutoff is

\[
f_0(x)=\min\{L_0,\max\{0,\lceil x/D_{\rm cut}\rceil-1\}\}.
\]

At \(x=D_{\rm cut}\ell\), it is \(\ell-1\), so the strict endpoint is correct. At a noninteger ratio it is the usual floor. The A arm is always included and receives label zero.

With \(P_t=A+\sum_{1\leq\ell\leq t}B_\ell\) and \(P_{-1}=0\), the fifth-product expansion of \(P_t^5\) consists of all ordered five-tuples whose maximum label is at most \(t\). Consequently the complete sum whose maximum label belongs to \([a,b]\) is exactly

\[
F_{[a,b]}=P_b^5-P_{a-1}^5.
\]

This identity retains tuples mixing labels inside and outside \([a,b]\); it must not be replaced by \((\sum_{\ell\in[a,b]}B_\ell)^5\). It also treats the A-only product correctly when \(a=0\). Relabeling \(0,\ldots,L_0\) as \(1,\ldots,L_0+1\) puts this in the ordinary dyadic-prefix setting.

On \(J^*=[X/3,4X]\), the unchanged width \(h(x)=2\sqrt{x}/\sqrt N\) is smooth and comparable to \(H\). The compact Fourier support restricts the active numerators to a finite union. Denominators remain bounded by \(\max(D_{\rm cut},4L_0)\). Every complete fixed-label amplitude therefore extends smoothly by the same multiplier formula; so do its fixed products and collision groups. This extension claims nothing about the shell representation or its tail outside \(J\).

Each selected prefix has \(O(\log(2L_0))\) disjoint canonical intervals. Pointwise Cauchy pays that factor. Enlarging the selected interval sum to all fixed dyadic intervals and applying C1 to each proves C2. The full dyadic energy is retained. No derivative is taken through a selection indicator. There is one outer logarithm; a further logarithm would need a separately proved uniform estimate for each dyadic level.

### C3: exact Fejer identity and support count — GREEN

Put \(V_m=\sum_{j=0}^{L-1}u_{m+j}\). Expanding the finite sum gives

\[
\frac1L\sum_m|V_m|^2
=D_{\rm diag}+2\Re\sum_{h=1}^{L-1}(1-h/L)C_h
=D_{\rm diag}+S_L\geq0.
\]

There are \(O(N+L)\) nonzero starting indices \(m\), including real support endpoints after integer rounding. Also \(\sum_mV_m=LF\). Hence

\[
L^2|F|^2\leq O(N+L)\sum_m|V_m|^2
\ll NL(D_{\rm diag}+S_L),
\]

because \(L\leq\delta N\). This is C3. The sign convention for \(C_h\) is immaterial after \(2\Re\), and the given convention is consistent with the expansion.

### C4--C6: positive-part moment and shift length — GREEN

For \(D\geq0\), \(D+S\geq0\),

\[
(D+S)^5\leq(D+S_+)^5\leq16(D^5+S_+^5).
\]

The divisor envelope gives \(D_{\rm diag}\ll_\epsilon N^{-1/2+\epsilon}\). Since \(|I|\asymp T\), C3 therefore gives

\[
\int_I|F|^{10}\ll_\epsilon
T N^{5/2+\epsilon}L^{-5}+(N/L)^5\int_I(S_L)_+^5.
\]

Comparison of the diagonal term with \(U=T^{83/65}N^{-1/2}\) gives

\[
L^5\gtrsim T^{1-83/65}N^3,
\qquad L\gtrsim T^{-18/325}N^{3/5},
\]

with adjustable epsilon losses, precisely C5. The lower bound \(D_{\rm diag}\gg N^{-1/2}\), proved below, makes this necessary for paying that separated positive diagonal term. It is not necessary for the actual moment.

The exponent of \(T\) in the threshold length is
\(-18/325+3\alpha/5\), lying between \(408/1625\) and \(636/1625\) on the closed band. It is positive, while the exponent of its ratio to \(N\) is \(-18/325-2\alpha/5<0\). Thus the integer range \(2\leq L\leq\delta N\) can accommodate it for large \(T\).

For the other term, solving
\((N/L)^5\int(S_L)_+^5\ll U\) gives exactly

\[
\int_I(S_L)_+^5\ll_\epsilon
T^{83/65+\epsilon}L^5N^{-11/2}.
\]

This is C6, still an unproved sufficient arithmetic input. Negative values of \(S_L\) can cancel the diagonal in the original bracket; C4 deliberately does not use them.

### C7: actual atom floor and Abel variation — GREEN

The elementary lattice property \(r_2(n)\in4\mathbb Z_{\geq0}\) gives

\[
|c_n|\geq4-\pi,\qquad
|d_h(n)|=|c_{n+h}c_n|\geq(4-\pi)^2.
\]

On the common interior interval there are \(\asymp N\) integers and \(|f(n)|\gg N^{-3/4}\). This proves
\(D_{\rm diag}\gg N^{-1/2}\). It also gives the uniform coefficient absolute bound from below

\[
A_h:=\sum_n|c_{n+h}c_nf(n+h)f(n)|\gg N^{-1/2}
\qquad(1\leq h\leq\delta N).
\]

The divisor envelope gives the corresponding upper estimates with an arbitrarily small epsilon loss.

Let \(w_h(t)=f(t+h)f(t)\), \(\theta_h(t)=R(\sqrt{t+h}-\sqrt t)\), and \(g_h=w_he(\theta_h)\). Smooth-mask bounds give \(\|w_h\|_\infty\ll N^{-3/2}\) and \(\int|w'_h|\ll N^{-3/2}\). Uniformly on common support,

\[
\theta'_h(t)=
-\frac{Rh}{2\sqrt t\sqrt{t+h}(\sqrt t+\sqrt{t+h})}
\asymp -ThN^{-3/2}.
\]

Therefore

\[
\|g_h\|_\infty+\int|g'_h|
\ll N^{-3/2}+ThN^{-2},
\]

which is C7. The lower variation estimate is also valid: \(w_h\) is real, so

\[
|g'_h|^2=(w'_h)^2+4\pi^2(\theta'_hw_h)^2.
\]

On the common positive interval, \(|w_h|\gg N^{-3/2}\) over length \(\asymp N\). Thus \(\int|g'_h|\gg ThN^{-2}\). Cancellation between the amplitude derivative and phase derivative cannot remove this variation cost.

Write the unweighted cumulative sum as \(A_h^{\rm cum}(y)=M_h(y)+E_h(y)\), with continuous \(M_h\). At an interior integer \(n\), the jump of \(E_h\) is exactly \(d_h(n)\). The two one-sided values cannot both have modulus below half that jump. Consequently every uniform envelope obeys

\[
\mathcal E_h\geq (4-\pi)^2/2.
\]

This is an envelope lower bound. It does not bound a weighted oscillatory sum from below. Abel summation gives a remainder of the form boundary terms minus \(\int E_h(t)g'_h(t)dt\), hence the absolute upper bound \(\mathcal E_h(\|g_h\|_\infty+\int|g'_h|)\). Smooth exterior support makes the actual exterior terms zero; retaining a supremum term is harmless. Continuity of the main term suffices for the jump argument and for the usual integrated Abel split; no differentiability of that main term is used.

### C8--C9 and the optimistic trivial caps — GREEN

For the explicitly defined positive certificate, the diagonal cost is

\[
(N/L)D_{\rm diag}\gg N^{1/2}/L.
\]

Using the constant envelope floor and the variation lower bound, its absolute-remainder cost is at least a fixed multiple of

\[
\frac NL\sum_{h=1}^{L-1}(1-h/L)ThN^{-2}
\asymp TL/N.
\]

Here \(\sum_{h=1}^{L-1}(1-h/L)h=(L^2-1)/6\), so there is no small-integer exception. This proves the two certificate costs in C8.

Requiring both to be \(\ll T^{2b}\), at the power level, gives

\[
N^{1/2}T^{-2b}\lesssim L\lesssim NT^{2b-1},
\quad N\gtrsim T^{2-8b}=T^{318/325}.
\]

This is incompatible with the required upper scale \(T^{242/325}\). Also, the product of the two costs is \(TN^{-1/2}\), so their maximum is at least \(T^{1/2}N^{-1/4}\). Taking a square root gives the norm-certificate exponent at least \(1/4-\alpha/8\). Its minimum on the closed required band exceeds \(b\) by exactly

\[
\frac14-\frac18\frac{242}{325}-\frac{83}{650}
=\frac{19}{650}.
\]

This lower bound remains valid when an unconstrained formal minimizing length lies outside the legal integer range: restricting the range cannot reduce a minimum.

If the error-only absolute cap is optimistically granted, each capped cost is still bounded below by a fixed multiple of
\(\min(ThN^{-2},N^{-1/2})\), because both the Abel cost and the absolute coefficient bound have these respective floors. Summing shifts in a fixed interior portion of \([1,L]\), with the small cases checked directly, yields

\[
\frac NL\sum_{h<L}(1-h/L)
\min(ThN^{-2},N^{-1/2})
\asymp\min(TL/N,N^{1/2}).
\]

The transition is \(L\asymp N^{3/2}/T\). Below it, C8--C9 apply. Above it, the cost is \(\gg N^{1/2}=T^{\alpha/2}\), exceeding \(T^{2b}\) for every fixed interior \(\alpha>4b\). There is no claimed uniform positive gap as \(\alpha\downarrow4b\); the equality endpoint belongs to the already-safe complementary range. The fixed-interior obstruction suffices to reject this method as a proof on the whole required band. This remains a statement about the granted certificate, not a proof that the corresponding actual correlation is large.

## 4. First doubtful or unproved step

No unresolved step remains in C1--C9 as scoped in the revised ledger. The first missing arithmetic inputs are still:

- the full, internally modulated, fixed-dyadic-block derivative energy in C2, with its outer logarithm paid at the rational target \(G\); or
- the positive-part aggregate estimate C6, with a legal length satisfying the diagonal budget C5, or some different argument that preserves cancellation in \(D_{\rm diag}+S_L\).

The exact-frequency diagonal estimate does not imply the first. The actual atomic floor and the elementary Fejer identity do not imply the second. The rejected Abel transfer covers only a uniform unweighted cumulative remainder followed by absolute variation and the specified positive summation. It does not reject oscillatory Stieltjes estimates, estimates keeping correlated remainder signs, or use of a known negative main term to cancel a positive diagonal.

The inherited mean-wave and reconstruction statements are used within their already stated scopes, not re-proved here from external sources. Success at the fixed tenth gate would imply the stated milestone \(102/325\), not the full quarter theorem.

## 5. Required controls and outcomes

All checks were algebraic or analytic; no mathematical numerical experiment was performed.

1. **Strict prefix and A-only term:** At \(x=D_{\rm cut}\ell\), the repaired cutoff excludes \(\ell\). The A-only fifth product is retained through label zero. PASS.
2. **Mixed-label multiplicities:** \(P_b^5-P_{a-1}^5\) retains exactly the products selected by their maximum label, including mixed products and their ordered multiplicities. PASS.
3. **Fixed extension versus moving indicator:** Complete blocks extend smoothly by the original multiplier on \(J^*\); the indicators are removed before C1 is invoked. No outside-window shell error is imported. PASS.
4. **Cancellation controls for bin transfer:** Carrier-canceling amplitudes refute derivative-free transfer; opposite coefficients in one bin refute unmodulated bin sums; opposite label amplitudes refute replacement of total dyadic energy by full unmasked energy. The valid inequalities retain all three costs. PASS.
5. **Negative shift aggregate:** The exact identity allows \(S_L<0\). For instance, a generic two-entry sequence \((1,-1)\) has \(D=2\), \(S_L=-2+2/L\), and total sum zero. This is a bookkeeping control, not an arithmetic example. It confirms why no positive certificate cost can be interpreted as a lower bound for \(|F|\). PASS.
6. **Actual atomic inputs:** The diagonal and absolute-cap floors use \(r_2(n)\in4\mathbb Z_{\geq0}\), the fixed interior mask, and its common support under the allowed shifts. They are not generic-coefficient countermodels. PASS.
7. **Real endpoints, length constraints and caps:** The shift identity tolerates real \(N,T\); exterior masks vanish; C5 grows but is \(o(N)\); capped saturation at a transition below one is still covered because all legal lengths then lie in the saturated case. The strict open-band qualification is retained. PASS.
8. **Signed-scope and complete-cost check:** No actual signed lower bound, original-moment necessary condition, omitted bulk contribution, or full-quarter conclusion is inferred. PASS.

## 6. Dependencies, provenance and final source SHA256 bindings

This is a new nonblind review. It does not retroactively change the isolation status or content of `reports/blind_bin_transfer.md`.

The source files read are listed below. The conductor subsequently authorized equations (3)--(8) of the rational fifth-convolution report to verify the actual prefix. My retrieval search returned an overbroad excerpt including other sections of that file. That exposure is disclosed here; this review does not claim equation-restricted or statement-only isolation. The rational prefix audit above uses the defining coefficient formulas (3)--(8). No extra source file named inside an artifact was opened, no web source was used, and no new external theorem was imported.

Final SHA256 bindings, computed after the requested repairs:

| Source path | SHA256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `rounds/codex-managed/gc-signed-near-frequency-cancellation/controls/conductor_shift_and_bin_ledger.md` | `2a7bb78bcbca542e5fbecb4d056412e5e31a92467392564d4f8f396b939cf169` |
| `rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md` | `6aa17dd35e2d930cedadfb489adf8e042b6aed61ed5882ae8e2eb0cd36fbd552` |
| `rounds/codex-managed/gc-complete-signed-tenth-moment/reports/actual_tenth_high_values.md` | `8fb9d01885057aa2981da9a746890968212a73103b7a079fcbc65e640d598df9` |
| `rounds/codex-managed/gc-complete-signed-tenth-moment/reports/signed_fifth_convolution.md` | `3ad10212450a105eced8477cf5a162b1a9ac3613bf58bfcb0308a393e9e9bdda` |

The conductor's messages supplied the revised prefix/extension definitions, weakened mask hypothesis, and narrowed certificate/cap scope. Those changes were read back in the source before issuing GREEN. Source hashing is provenance checking, not a mathematical experiment.

## 7. Recommended state effect

**Retain** the hash-bound revised ledger as validated, scoped method evidence. C1--C2 and C3--C6 are sufficient interfaces with explicit costs; C7--C9 are an obstruction only to the specified positive absolute-Abel certificate, even under its optimistic cap allowance.

**No promotion** of either missing arithmetic input, the original tenth gate, any pointwise benchmark, M1/M2, or the full quarter target is justified. No shared graph, proof draft, validation matrix, synthesis, legacy artifact, or original isolated report was edited. Only this assigned review was written. This review is complete; no successor work is undertaken.
