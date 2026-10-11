# Round 203: independent displaced-filter and smoothing-scale audit

## 1. Result

**Result: exact identities and a scale no-go for obtaining a new norm bound from smoothing alone.** Put (p=\widehat\phi), (\lambda=hT), and (S=\|K_T*\nu\|_2). The smoothed and residual pieces have the exact physical-space multipliers

\[
\chi(x/T)p(hx)f(x),\qquad
\chi(x/T)(1-p(hx))f(x).
\]

For (\lambda\to0), the residual is (O(\lambda^2)S), while the smoothed piece retains (S(1+O(\lambda^2))). For (\lambda\to\infty), the smoothed piece is (O_N(\lambda^{-N})S), while the residual retains (S(1+O_N(\lambda^{-N}))). At (\lambda\asymp1), the exact multipliers must be retained: neither piece is automatically small, and zeros of (p) transfer all the corresponding energy to the residual. For every (h>0),

\[
\|K_T*g_h\|_2+\|K_T*e_h\|_2\ge S,
\qquad
\|K_T*g_h\|_2^2+\|K_T*e_h\|_2^2\ge \tfrac12S^2.
\]

Thus the cancellation of all moments of (K_T), together with the smoothness of (g_h), does not provide a new bound for the full filtered measure. It controls one multiplier and leaves the complementary multiplier to be estimated.

There is an essential quantifier distinction. For a **fixed** finite measure, or a family with uniformly bounded total variation, the requested (O(T^{0.58})) bound already follows from the elementary (O(T^{1/2})) estimate. A counterexample to that fixed-measure assertion would be incorrect. The generic obstruction concerns **(T)-dependent families without a sufficient total-variation bound**, as is relevant when the measure itself is constructed using (T). The family

\[
\nu_T=T^{1/10}\delta_0
\]

has (S=T^{3/5}\|\chi\|_2), disproving a uniform (O(T^{29/50})) conclusion based only on the stated structural properties. It is also a sixfold convolution, by taking (\mu_T=T^{1/60}\delta_0). This family is **not** the particular arithmetic measure in the packet, and gives no counterexample to an estimate for those particular coefficients.

Metadata: campaign `gc-complete-signed-convolution-attack`; round 203; task `blind_filter_scale_audit`; role statement-only independent rederivation; generated 2026-09-23 13:13:31 UTC. Graph hash was deliberately withheld under the isolation instruction and was not read. Analytical allocation: 100%; experiments: none.

## 2. Exact statement and hypotheses

Let (0<c<C), let (0\ne\chi\in C_c^\infty((c,C))) be real and nonnegative, and let

\[
\widehat u(\xi)=\int_{\mathbb R}u(x)e^{-2\pi ix\xi}\,dx,
\qquad
\check\nu(x)=\int_{\mathbb R}e^{2\pi ix\xi}\,d\nu(\xi).
\]

For (T,h>0), set (w_T(x)=\chi(x/T)), (K_T=\widehat w_T=T\widehat\chi(T\cdot)). Let (\nu) be a finite complex Borel measure, (f=\check\nu), and let (\phi\) be an even Schwartz function with integral one. No positivity or nonvanishing of (\widehat\phi) is assumed or needed. Define

\[
\phi_h(\xi)=h^{-1}\phi(\xi/h),\qquad
g_h=\phi_h*\nu,\qquad e_h=\nu-g_h(\xi)\,d\xi.
\]

The notation (e_h=\nu-g_h) below identifies the (L^1) function (g_h) with its absolutely continuous measure. All three filtered measures belong to (L^2). Put (p=\widehat\phi=\check\phi), using evenness. Then (p\in\mathcal S), (p(0)=1), and (p'(0)=0).

The identities and inequalities below hold for every finite complex measure, with constants depending only on the displayed fixed test functions and indicated derivative order. They do not assert that a (T)-dependent measure has uniformly bounded variation.

For the sixfold statements, let (\mu) be any finite complex measure, set (M=\check\mu), and set (\nu=\mu^{*6}). Define

\[
\alpha_h=\phi_h*\mu,\qquad \beta_h=\mu-\alpha_h.
\]

As above, (\alpha_h) is identified with its density measure.

## 3. Proof and derivation

### 3.1. Exact filter, exact smooth/residual split, and the elementary bound

Since (\|f\|_\infty\le\|\nu\|_{\rm TV}), (w_Tf\in L^2). Fourier inversion, the measure convolution identity, and Plancherel give

\[
\check{(K_T*\nu)}=w_Tf,
\qquad
S=\|w_Tf\|_2\le T^{1/2}\|\chi\|_2\|\nu\|_{\rm TV}.
\tag{1}
\]

These identities can first be read in tempered distributions; their right sides belong to (L^2), so they are also (L^2) identities. Fubini applies to the smoothing because (\phi_h\in L^1) and (\nu) is finite. Thus

\[
\check g_h(x)=p(hx)f(x),\qquad
\check e_h(x)=(1-p(hx))f(x).
\tag{2}
\]

Writing (G=\|K_T*g_h\|_2), (E=\|K_T*e_h\|_2), and (y=x/T), the full exact formulas are

\[
\begin{aligned}
S^2&=T\int\chi(y)^2|f(Ty)|^2\,dy,\\
G^2&=T\int\chi(y)^2|p(\lambda y)|^2|f(Ty)|^2\,dy,\\
E^2&=T\int\chi(y)^2|1-p(\lambda y)|^2|f(Ty)|^2\,dy.
\end{aligned}
\tag{3}
\]

The split is an identity before taking absolute values. In particular, it is not generally orthogonal.

Let

\[
a(\lambda)=\sup_{y\in\operatorname{supp}\chi}|p(\lambda y)|,
\qquad
b(\lambda)=\sup_{y\in\operatorname{supp}\chi}|1-p(\lambda y)|.
\]

Then

\[
G\le aS,\quad E\le bS,\quad
G\ge(1-b)S,\quad E\ge(1-a)S,
\tag{4}
\]

where a negative lower bound is simply vacuous. The last two follow from the triangle inequality applied to the exact split. More strongly,

\[
|z|^2+|1-z|^2=\tfrac12+2|z-\tfrac12|^2
\]

and (3) prove (G^2+E^2\ge S^2/2), without any reality assumption on (p).

For a fixed (T,\nu), dominated convergence as (h\downarrow0) gives (G\to S), (E\to0). Therefore the exact optimization of the sum of the two norms is

\[
\inf_{h>0}(G+E)=S.
\tag{5}
\]

Choosing (h) can redistribute the full norm between pieces; it cannot by itself lower the total norm that a triangle-inequality argument must control.

### 3.2. The scale dichotomy

Evenness and Taylor's theorem at zero imply (p(u)=1+O(u^2)). Since (y\) ranges over a fixed compact set,

\[
b(\lambda)=O(\lambda^2),\qquad
E=O(\lambda^2)S,\qquad
G=S(1+O(\lambda^2))\quad(\lambda\to0).
\tag{6}
\]

Some choices of (\phi) give higher-order or flat behavior at zero; (6) is the uniformly available second-order conclusion. Any stronger flatness still makes the smoothed term retain the original norm.

Because (p) is Schwartz and (y\ge c>0) on the support,

\[
a(\lambda)=O_N(\lambda^{-N}),\qquad
G=O_N(\lambda^{-N})S,\qquad
E=S(1+O_N(\lambda^{-N}))\quad(\lambda\to\infty)
\tag{7}
\]

for every (N>0). For instance, (h=T^{-1+\delta}), with fixed (\delta>0), gives arbitrary power decay in the multiplier of the smoothed piece, but its residual has asymptotically the full norm (S).

At the borderline (hT\asymp1), (3) is the appropriate statement. There is no parameter-driven decay. If 

\[
\inf_{\chi(y)\ne0}|1-p(\lambda y)|\ge d>0,
\]

then (E\ge dS). A corresponding positive lower bound for (|p|) gives (G\ge dS). These are additional multiplier hypotheses, not consequences of smoothness. Regardless of zeros or exceptional values, (\max(G,E)\ge S/2).

A zero (p(\lambda y_0)=0), with (\chi(y_0)>0), prevents any uniform inversion of the smoothed multiplier near (y_0). Indeed choose nonzero (f\in C_c^\infty) supported in an arbitrarily small neighborhood of (Ty_0), and let (d\nu=\widehat f(\xi)\,d\xi). This is a finite measure. Continuity then makes (G/S) arbitrarily small and (E/S) arbitrarily close to one. This proves the obstruction even for an isolated zero. Conversely, where (p=1), the residual vanishes and the smoothed multiplier retains the full local energy. No division by (p) is legitimate without a nonvanishing lower bound on the relevant region.

In particular, a borderline zero is not merely hypothetical. Choose real even nonzero (b_0\in C_c^\infty((-1/2,1/2))), put (\psi=\check b_0), and set

\[
\phi=\frac{\psi^2}{\int\psi^2}.
\]

This is an even, nonnegative Schwartz approximate-identity profile, and (p=\widehat\phi) is supported in ([-1,1]). For the fixed constant (\lambda_0>1/c) and (h=\lambda_0/T), (p(\lambda_0 y)=0) on the filter support. Hence (G=0) and (E=S) exactly, even though (hT\asymp1).

### 3.3. All kernel moments vanish, but the derivative scale matters

For every integer (m\ge0),

\[
\int\xi^mK_T(\xi)\,d\xi
=T^{-m}(2\pi i)^{-m}\chi^{(m)}(0)=0,
\tag{8}
\]

since (\chi) is identically zero near zero. These cancellations are real and need no arithmetic input.

Taylor expansion of (g_h(\xi-\eta)), using the first (m) vanishing moments and the integral remainder, gives for (m\ge1)

\[
\|K_T*g_h\|_2
\le C_m T^{-m}\|g_h^{(m)}\|_2
\le C_{m,\phi}T^{-m}h^{-m-1/2}\|\nu\|_{\rm TV}.
\tag{9}
\]

Here (\|g_h^{(m)}\|_2\le h^{-m-1/2}\|\phi^{(m)}\|_2\|\nu\|_{\rm TV}) follows from Young's inequality for a finite measure. Thus the smoothness constants are not independent of (h) or of the measure. The exact multiplier calculation gives the cleaner uniform bound

\[
G\le C_N(1+hT)^{-N}T^{1/2}\|\nu\|_{\rm TV}.
\tag{10}
\]

Neither (9) nor (10) estimates the complementary residual. At the scales where they produce a strong smoothing gain, (7) identifies that residual with the original problem up to a relative error tending to zero.

### 3.4. A quantitative generic counterexample and the fixed-measure caveat

For (\nu_T=T^{1/10}\delta_0), (f_T=T^{1/10}), and hence

\[
S=T^{3/5}\|\chi\|_2.
\tag{11}
\]

All the hypotheses hold. The kernel has all moments zero and (g_h=T^{1/10}\phi_h) is Schwartz. Nevertheless, no selection (h=h(T)) can give both

\[
G=O(T^{29/50}),\qquad E=o(T^{29/50}),
\]

because their sum would contradict (11). The conclusion remains false if the second condition is weakened to (E=O(T^{29/50})).

The two extreme scale controls are explicit: (h=T^{-2}) gives (E=O(T^{-7/5})) but (G\sim T^{3/5}\|\chi\|_2); (h=T^{-1/2}) gives arbitrary polynomial suppression of (G), but (E\sim T^{3/5}\|\chi\|_2). They are deductions from (6)-(7), not experiments.

If instead (\nu) is fixed, (1) gives (S=O_\nu(T^{1/2})=o(T^{29/50})). Even the residual has this latter bound, since (E\le(1+\|p\|_\infty)S). More generally, the sufficient generic condition

\[
\|\nu_T\|_{\rm TV}=O(T^{2/25})
\]

already implies (S=O(T^{29/50})) by (1). Such a growth hypothesis was not supplied for the arithmetic convolution. The counterexample refutes the inference without a sufficient norm-growth or coefficient-specific hypothesis; it does not refute the true fixed-measure estimate.

### 3.5. Direct smoothing versus smoothing each factor: all six errors

Let (\nu=\mu^{*6}). Direct smoothing gives

\[
\check{(\phi_h*\nu)}=p(hx)M(x)^6,
\qquad
\check{(\nu-\phi_h*\nu)}=(1-p(hx))M(x)^6.
\tag{12}
\]

Smoothing each factor before convolution gives a different measure:

\[
\alpha_h^{*6}=\phi_h^{*6}*\nu,
\quad
\check{(\alpha_h^{*6})}=p(hx)^6M(x)^6,
\quad
\check{(\nu-\alpha_h^{*6})}=(1-p(hx)^6)M(x)^6.
\tag{13}
\]

The difference between the two smoothed measures has multiplier (p-p^6). No general replacement of (p^6) by (p) at the same scale is valid.

The complete convolution-binomial expansion is

\[
\nu=\alpha_h^{*6}+\sum_{j=1}^{6}R_j,
\qquad
R_j=\binom6j\alpha_h^{*(6-j)}*\beta_h^{*j}.
\tag{14}
\]

There are exactly six error terms. Their multipliers, after taking the inverse transform and removing the common (M^6), are

| (j) | Multiplier of (R_j) |
|---|---|
| 1 | (6p^5(1-p)) |
| 2 | (15p^4(1-p)^2) |
| 3 | (20p^3(1-p)^3) |
| 4 | (15p^2(1-p)^4) |
| 5 | (6p(1-p)^5) |
| 6 | ((1-p)^6) |

Here each (p) means (p(hx)). In particular,

\[
\begin{aligned}
\|K_T*R_j\|_2^2
&=\binom6j^2T\int\chi(y)^2
 |p(\lambda y)|^{2(6-j)}|1-p(\lambda y)|^{2j}
 |M(Ty)|^{12}\,dy,\\
\|K_T*R_j\|_2
&\le\binom6j a(\lambda)^{6-j}b(\lambda)^jS.
\end{aligned}
\tag{15}
\]

These bounds control every term without discarding a pure residual or replacing a signed sum by a purportedly small total. For the total residual, the stronger exact formula is

\[
\begin{aligned}
\left\|K_T*\sum_{j=1}^6R_j\right\|_2^2
&=T\int\chi(y)^2|1-p(\lambda y)^6|^2|M(Ty)|^{12}\,dy,\\
\left\|K_T*\sum_{j=1}^6R_j\right\|_2
&\le b(1+a+a^2+a^3+a^4+a^5)S.
\end{aligned}
\tag{16}
\]

At small (\lambda), (a=1+O(\lambda^2)), (b=O(\lambda^2)). Therefore the (j)-th error is (O_j(\lambda^{2j})S), the total residual is (O(\lambda^2)S), and the smoothed sixth power retains (S(1+O(\lambda^2))).

At large (\lambda), put (a=O_N(\lambda^{-N})\to0). The main sixth power is at most (a^6S), each of the first five errors is at most

\[
\binom6j a^{6-j}(1+a)^jS,
\]

and the sixth error satisfies

\[
\|K_T*R_6\|_2=S(1+O(a)),
\]

because ((1-p)^6=1+O(a)) uniformly on the filter support. The full residual in (16) is (S(1+O(a^6))). Thus dropping the pure six-error term would drop the original norm at these scales.

At the borderline, (15)-(16) remain valid without division. Where (p=0), the sixth error alone has multiplier one. Where (p=1), the main term alone has multiplier one. For general complex (p), cancellation among the six errors is possible; smallness of their sum would not by itself establish smallness of each. Finally,

\[
S\le\|K_T*\alpha_h^{*6}\|_2+\sum_{j=1}^{6}\|K_T*R_j\|_2,
\]

so at least one of these seven norms is at least (S/7), for every (h). Grouping the six errors together restores the two-piece lower bounds with (p) replaced by (p^6).

### 3.6. Exact arithmetic interface, without claiming an arithmetic counterexample

For the specific measure stated in the packet, its inverse transform is

\[
M_T(x)=\sum_{n>\lfloor T^{1/2047}\rfloor}
r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
\cos(2\pi x\sqrt n-3\pi/4).
\tag{17}
\]

The factor (1/2) and the conjugate phases give exactly this cosine normalization. For each fixed (T), the Schwartz decay of (\Psi), together with the elementary polynomial bound on the number of lattice points on a circle, makes the defining measure finite. Consequently all the preceding exact identities apply to (\nu_T=\mu_T^{*6}), and

\[
\|K_T*\nu_T\|_2^2
=\int\chi(x/T)^2|M_T(x)|^{12}\,dx.
\tag{18}
\]

Any claimed (O(T^{29/50})) bound is therefore a claim that this weighted twelfth-moment integral is (O(T^{29/25})). Direct smoothing inserts (|p(hx)|^2) in (18), with residual factor (|1-p(hx)|^2). Smoothing before convolution instead inserts (|p(hx)|^{12}), with full residual factor (|1-p(hx)^6|^2).

An arithmetic proof must establish the needed bound for these actual coefficients, including the complete residual. It may exploit structure absent from the atomic family. The identities here neither provide that additional arithmetic estimate nor rule out its existence.

## 4. First doubtful or unproved step

There is no unproved step in the Fourier identities, scale estimates, or generic counterexample above.

For the proposed smoothing route, the first unsupported step is the assertion that the residual is negligible at a scale (hT\to\infty) selected to make the smoothed term small. In that regime,

\[
\|K_T*e_h\|_2=(1+o(1))\|K_T*\nu\|_2,
\]

and the analogous statement holds for the complete pre-convolution residual. Proving negligibility at the desired target scale would already require the corresponding estimate for the original quantity. At (hT\to0), the unresolved estimate instead remains in the smoothed piece. At (hT\asymp1), it remains in the weighted integrals (3) or (16), unless an additional coefficient-specific argument is supplied.

A second possible unsupported step is treating the derivatives of (g_h) as bounded independently of (h) and (\nu_T); (9) exhibits their actual scaling. For pre-convolution smoothing, omitting the pure error (β_h^{*6}) is a concrete algebraic failure, not a small technical remainder.

## 5. Required controls and outcomes

All controls were analytical; no numerical or symbolic experiments were run.

1. **Moment normalization:** equation (8) verifies every moment of the specified (K_T) is zero with the stated Fourier convention. Outcome: pass; the no-go does not deny the kernel cancellation.
2. **Small-scale control:** (p(0)=1), (p'(0)=0) gives (6). Outcome: the residual is small but the main term retains the full norm.
3. **Large-scale control:** Schwartz decay away from the origin gives (7). Outcome: the smoothed term is small but the full residual retains the norm.
4. **Borderline/zero control:** the nonnegative Schwartz construction with compactly supported (p) gives (G=0,E=S) at a fixed (hT>1/c). The localized (C_c^\infty) inverse-transform construction also checks isolated zeros. Outcome: no uniform division by (p), and no omitted residual gain.
5. **Quantifier and scaling control:** the fixed-measure (O(T^{1/2})) bound is distinguished from the family (T^{1/10}\delta_0), whose norm is (T^{3/5}\|\chi\|_2). Outcome: the precise generic implication fails, while the fixed-measure assertion remains true.
6. **Full sixfold algebra:** equation (14) and the six multipliers sum to ((p+(1-p))^6=1); (15) controls every error term and (16) controls their exact sum. At (p=0), the sixth error is one. Outcome: the pre-convolution smoothing route has the same full-remainder obstruction.
7. **Arithmetic normalization and scope:** equation (17) independently checks both phases and the half-factor. Outcome: exact applicability of the filter identities, with no assertion that the generic atomic family has the given arithmetic coefficients.

## 6. Dependencies and exact artifacts used

Read only:

- `protocol.md`.
- `rounds/codex-managed/gc-complete-signed-convolution-attack/briefs/blind_filter_statement.md`.

No graph, active manifest, strategy, generated brief, historical report, claimant derivation, or sibling report was read. No external source was imported. The mathematical dependencies are elementary Fourier inversion and Plancherel for Schwartz functions/finite measures, Fubini, Young's inequality, Taylor's theorem, dominated convergence, and the convolution-binomial identity. No arithmetic cancellation theorem is used.

The report writes only the assigned artifact. It makes no authoritative graph or shared-state edit.

## 7. Recommended state effect

**Reject the inference that vanishing filter moments and smoothness alone yield a new uniform (T^{0.58}) bound with a negligible full remainder for the relevant (T)-dependent class.** Retain the exact multiplier identities and the scale dichotomy as a rigorous obstruction/control, subject to the conductor's required seam checks and State Patch procedure.

Do not record the literal fixed-finite-measure (O(T^{0.58})) statement as false: it follows trivially from (1). Do not record an arithmetic counterexample or promote the desired arithmetic bound. For the packet's particular coefficients, the complete weighted twelfth-moment/remainder estimate remains unproved by this method. Recommended target state: no promotion from this report.
