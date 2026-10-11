# Round217 — statement-only even-moment family review

- Campaign: `gc-full-goal-distinct-source-review`; round: 217.
- Task/role: `blind_moment_family`, independent statement-only algebra reviewer.
- Generated: 2026-09-28T02:29:47+08:00.
- Supplied graph SHA256: `f7c8b74e9acaa3bf5234c3678f20e2aaf8dbb9ba6179f73d839fa2f0537a14d7` (metadata only; graph not read).
- Exact context read: `protocol.md`; `rounds/codex-managed/gc-full-goal-distinct-source-review/briefs/blind_moment_family_statement.md`.
- Isolation: no graph, manifest, strategy, generated general brief, other report, historical report, web page, or source was read. The conductor subsequently requested precise separation of the nonabsorbing certificate and absorption; that request supplied no external mathematical evidence.
- Resources: analytical/algebraic work only; zero computational experiments.

## 1. Result: complete identity, restricted certificate, and stronger conditional transfer

The distinct-index expansion is an exact set-partition identity. Its absolutely convergent infinite limit yields a one-sided signed-integral transfer without any positivity assumption on the distinct-index polynomial.

Writing

\[
M_r(F)=\int w(R/T)|F(R)|^r\,dR,\qquad
m(r)=\max\{1,\beta(r-2)\},
\]

with (M_0(F)=T\int w), the inherited distribution and ceiling imply (M_r(Z)\ll T^{m(r)+\varepsilon}) for each fixed nonnegative integer (r). Every nontrivial partition is dominated, at the exponent level of the **nonabsorbing insertion of these inherited moments**, by the partition consisting of one pair and (p-2) singletons. Its correction exponent is

\[
C_p(\alpha)=\max\{1,\beta(p-4)\}-\alpha/2.
\]

The complete head exponent is

\[
H_p(\alpha)=\max\{1,\alpha(p-2)/4,
                         1+\alpha(p-q)/4\}.
\]

Under the additional, unproved, one-sided grant (I_p\ll T^{1+\varepsilon}), the resulting restricted nonabsorbing certificate is

\[
M_p(B)\ll T^{\max(H_p(\alpha),C_p(\alpha))+\varepsilon}.
\tag{1}
\]

Put (c=1/(q-2)=13/110) and (p_c=4\beta/(\beta-c)). Optimizing (1) gives (E(p)=1) for even (4\le p\le10), and, for even (p\ge12),

\[
E(p)=
\begin{cases}
\displaystyle\frac{2+\beta(p-4)(p-q)}{p-q+2},&p\le p_c,\\[6pt]
\displaystyle\frac{\beta(p-4)(p-2)}p,&p\ge p_c.
\end{cases}
\tag{2}
\]

The two expressions agree at the transition. The restored exponent from this restricted certificate has its unique minimum over fixed even orders at (p=16):

\[
\min_{p\in2\mathbb Z,\ p\ge4}\Theta(p)
=\Theta(16)=\frac{227+216\beta}{833}.
\tag{3}
\]

As (p\) tends to infinity through fixed even orders, this restricted certificate instead tends to (1/4+\beta/2).

**This is not the best consequence of the packet plus the diagnostic grant.** All partition errors can be absorbed into half of (M_p(Z)), using only the same order (p). For every fixed (\eta>0),

\[
M_p(Z)\le 2I_p+O_{p,\eta,\alpha}
                 \bigl(TQ^{-p/4+p\eta}\bigr).
\tag{4}
\]

Taking (\eta<1/4), the same one-sided grant already gives (M_p(Z)\ll T^{1+\varepsilon}), with no lower-order grants. Consequently the stronger complete certificate is (M_p(B)\ll T^{H_p(\alpha)+\varepsilon}). At (\alpha=0), (Q=1), (H_p(0)=1), and a grant at that single pair ((p,0)) gives the full (p)-moment bound (T^{1+\varepsilon}). Grants at unbounded fixed even orders at that endpoint give restored exponents tending to (1/4). Thus an obstruction extracted from (2) cannot be promoted into a no-go theorem for recursive or absorbing uses of the hypotheses.

## 2. Exact statements and hypotheses

All hypotheses are exactly those of the isolated packet: (q=136/13), (1/8<\beta<13/100), (\beta(q-2)>1), (T\ge2), fixed (0\le\alpha\le4\beta), (Q=\lfloor T^\alpha\rfloor), and the stated distribution, ceiling, absolute convergence, and power-sum bounds. The weight is fixed, nonnegative, smooth, and supported in ([1/2,2]). No arithmetic origin, independence, cancellation, or positivity of (E_p) is added.

The estimates concern each fixed even (p\ge4); constants can depend on (p), (\alpha), and each requested positive epsilon. The (I_p\ll T^{1+\varepsilon}) bound is always an explicitly additional hypothesis at the particular tested pair ((p,\alpha)). It is not proved by the supplied assumptions.

The finite identity is valid for arbitrary scalar functions on a finite set of indices; in the real setting it reads as a real identity. The limiting identity and the integral transfer follow from the packet's absolute convergence. If only the total integral is known to be real, taking real parts before the final inequality gives the same integral transfer.

The conclusions about arbitrarily small restored exponent losses require the supplied restoration formula to be valid in the intended application. The present packet supplies an abstract formula, not an arithmetic identification of its functions. No assertion concerning a particular arithmetic discrepancy follows here.

The word “best” in (1)–(3) refers specifically to bounding all non-singleton power sums in supremum, inserting the inherited lower-moment estimates individually, taking the maximum of their resulting powers, and optimizing the cutoff. It does not claim optimality among all deductions from the hypotheses. Formula (4) is a strictly stronger deduction after the grant is added.

## 3. Proof and derivation

### 3.1 Finite identity and infinite limit

For a finite index set (D_N=\{d:Q<d\le N\}), put

\[
S_{h,N}=\sum_{d\in D_N}f_d^h,qquad Z_N=S_{1,N}.
\]

For a set partition \(\pi\) of \(\{1,\ldots,p\}\), define

\[
\mu(\pi)=(-1)^{p-|\pi|}\prod_{C\in\pi}(|C|-1)!.
\]

Inclusion–exclusion on equalities of indices, equivalently inversion on the partition lattice, gives

\[
E_{p,N}=\sum_{\pi}\mu(\pi)\prod_{C\in\pi}S_{|C|,N}.
\tag{5}
\]

A direct coefficient proof, which fixes every normalization, is

\[
\sum_{p\ge0}\frac{E_{p,N}}{p!}t^p
=\prod_{d\in D_N}(1+t f_d)
=\exp\!\left(\sum_{h\ge1}\frac{(-1)^{h-1}}hS_{h,N}t^h\right)
\]

as a formal power-series identity. Extracting the coefficient gives the complete grouped formula

\[
E_{p,N}=p!\sum_{\substack{m_1,\ldots,m_p\ge0\\
                          \sum h m_h=p}}
\prod_{h=1}^p\frac{(-1)^{(h-1)m_h}S_{h,N}^{m_h}}
                         {m_h!h^{m_h}}.
\tag{6}
\]

There is one term (Z_N^p), corresponding to (m_1=p). Every other term has

\[
r=m_1,qquad n=p-r=\sum_{h\ge2}h m_h\ge2,qquad
k=\sum_{h\ge2}m_h\le\lfloor n/2\rfloor.
\tag{7}
\]

For each fixed (T), \(\sum A_d<\infty\) gives uniform absolute convergence of (Z_N), every (S_{h,N}), and the distinct-index multiple series, the latter dominated by \((\sum A_d)^p\). Its integral is dominated by a finite constant times the compact-window measure. Thus (5)–(6) pass to their infinite limits and can be integrated term by term. Write (S_h=\sum_{d>Q}f_d^h). Then (S_1=Z) and

\[
Z^p=E_p-\sum_{\mathbf m\ne(p,0,\ldots,0)}
a_{\mathbf m}Z^r\prod_{h\ge2}S_h^{m_h},
\quad
a_{\mathbf m}=p!\prod_h
\frac{(-1)^{(h-1)m_h}}{m_h!h^{m_h}}.
\tag{8}
\]

Signed powers (Z^r) remain in this identity. Absolute values are introduced only to bound a correction integral. Since (p) is even and (w\ge0), the direction of transfer is

\[
M_p(Z)\le I_p+
\sum_{\mathbf m\ne(p,0,\ldots,0)}|a_{\mathbf m}|
\left(\prod_{h\ge2}\|S_h\|_\infty^{m_h}\right)M_r(Z).
\tag{9}
\]

This uses (I_p), not (|I_p|). A one-sided upper bound for (I_p) suffices. The same identity also forces (I_p\ge-\text{error}); an arbitrarily negative (I_p) inconsistent with that inequality cannot occur.

### 3.2 Complete distribution-to-moment calculation

For a ceiling (U\ge\max(1,\|F\|_\infty)) and fixed real (r>0), layer cake gives, with harmless constants depending on (r),

\[
M_r(F)\ll T^\delta\left[T+
J_{r-2}(U)+T J_{r-q}(U)\right],
\quad
J_s(U)=\begin{cases}(U^s-1)/s,&s\ne0,\\\log U,&s=0.
\end{cases}
\tag{10}
\]

The (T) term is the entire level range (0<V<1); it cannot be omitted. Formula (10) retains both distribution terms and both borderline logarithms, at (r=2) and (r=q). For (r=0), the answer is exactly (T\int w).

The ceiling on (Z=B-L) is (\|Z\|_\infty\ll T^{\beta+\delta}), because (Q^{1/4}\le T^{\alpha/4}\le T^\beta). Above (q), comparison of the two growing terms gives

\[
\beta(r-2)-\{1+\beta(r-q)\}
=\beta(q-2)-1>0.
\]

At (q), the logarithmic term is also below (T^{\beta(q-2)+\varepsilon}). It follows, including all low levels, that

\[
M_r(Z)\ll T^{\max(1,\beta(r-2))+\varepsilon}.
\tag{11}
\]

For integer (r), this exponent is (1) for (0\le r\le9) and is (\beta(r-2)) for (r\ge10). In particular, (r=10<q) already has exponent (8\beta>1); crossing (q) does not restore the exponent (1).

Applying (10) to (L) with (U\ll Q^{1/4}) gives, for fixed even (p\ge4),

\[
M_p(L)\ll T^\varepsilon
\left[T+Q^{(p-2)/4}+TQ^{(p-q)_+/4}\right].
\tag{12}
\]

For a real order (p=q), the last contribution should be written (T\log(2Q)); (q) is not an even integer here. Formula (12) has exponent (H_p(\alpha)). The third term is essential for (p>q), even when the head ceiling is far below the full ceiling.

For all (\alpha\ge0),

\[
\tfrac12 T^\alpha\le Q\le T^\alpha.
\tag{13}
\]

Consequently every fixed positive or negative power of (Q) has the asserted (T)-power up to an order-dependent constant. At (\alpha=0), (Q=1) exactly; no large-(Q) approximation is used.

### 3.3 Every partition in the inherited, nonabsorbing certificate

The packet gives

\[
\prod_{h\ge2}\|S_h\|_\infty^{m_h}
\ll Q^{k-3n/4+\eta}
\tag{14}
\]

after splitting the requested loss among finitely many factors. For fixed (n), the largest possible exponent is attained at (k=\lfloor n/2\rfloor): pairs only if (n) is even, and one triple plus pairs if (n\ge3) is odd. Thus (9) and (11) give every partition's correction exponent, and their maximum is

\[
\max_{2\le n\le p}\left[
m(p-n)-\alpha\left(3n/4-\lfloor n/2\rfloor\right)\right].
\tag{15}
\]

The function (m) is nondecreasing. The penalty is (n\alpha/4) for even (n), and ((n+2)\alpha/4) for odd (n). Both are at least (\alpha/2). Hence every term in (15) is at most (m(p-2)-\alpha/2), and (n=2) attains it. This proves (C_p\) and accounts for all partitions, including those with no singletons.

Finally (M_p(B)\le2^{p-1}(M_p(L)+M_p(Z))). Combining this with (9), (12), and the grant gives (1). There is no additional loss from an unexamined partition or from low levels.

### 3.4 Cutoff optimization and comparison across fixed even orders

Set (a=\alpha/4\in[0,\beta]). For (p\ge12),

\[
H_p(4a)=\begin{cases}
1+a(p-q),&0\le a\le c,\\
a(p-2),&c\le a\le\beta,
\end{cases}
\qquad C_p(4a)=\beta(p-4)-2a.
\]

The head increases and the correction decreases. Their unique intersection is feasible and is

\[
a_*=
\begin{cases}
\displaystyle\frac{\beta(p-4)-1}{p-q+2},&p\le p_c,\\[6pt]
\displaystyle\frac{\beta(p-4)}p,&p\ge p_c.
\end{cases}
\tag{16}
\]

The first numerator is positive for (p\ge12). Feasibility in that branch follows, for example, from \(\beta(q-6)<1\); the second branch has (a_*<\beta). The branch condition is exactly \(\beta(p-4)\le cp\). This proves (2). For (p\le10), (C_p\le1) and (\alpha=0) gives (H_p=1), proving (E(p)=1).

Since (E(p)\ge1), the restored expression simplifies to

\[
\Theta(p)=\frac14+\frac{1+2E(p)}{4(p+1)}.
\tag{17}
\]

For sufficiently large (p), (E(p)=\beta(p-6+8/p)), which proves the limit (1/4+\beta/2).

For completeness, (3) can be checked algebraically without a numerical search. Here (44<p_c<220/3), so orders (14,16,18) all lie in the first branch. Put

\[
k=q-2,\quad C=14\beta-1>0,\quad
D=4[1-\beta(q-6)]>0.
\]

In that branch,

\[
4\Theta(p)=1+2\beta-\frac C{p+1}
                         +\frac D{(p-k)(p+1)}.
\]

The sign of its derivative is that of

\[
C-D\frac{2p+1-k}{(p-k)^2}.
\]

This changes from negative to positive once, between (p=14) and (p=18), throughout the specified beta interval. The second branch is increasing for (p\ge12): its derivative has the sign of \(C-16\beta(2p+1)/p^2>0\). The low branch (p\le10) is decreasing, and even its endpoint is worse than (p=12). Thus only (14,16,18) need comparison. Their exact values are

\[
\Theta(14)=\frac{301+230\beta}{1080},\quad
\Theta(16)=\frac{227+216\beta}{833},\quad
\Theta(18)=\frac{633+686\beta}{2356}.
\]

After positive denominators are cleared, the two differences from order (16) have numerators (5573-41690\beta>0) and (-7523+62542\beta>0), respectively. This proves the unique discrete minimum.

### 3.5 Absorption of all partitions: stronger than the restricted certificate

Fix the order (p) and choose (\eta>0). Invoke each power-sum hypothesis with loss (2\eta). For (2\le h\le p), since (Q\ge1),

\[
\|S_h\|_\infty\ll Q^{1-3h/4+2\eta}
\le Q^{-h/4+h\eta}.
\]

Put (R_Q=Q^{-1/4+\eta}>0). Each nontrivial partition correction in (8) is bounded pointwise by

\[
K_{\mathbf m}R_Q^n|Z|^{p-n},\qquad n\ge2.
\tag{18}
\]

There are finitely many such partitions at fixed (p), and their constants are fixed before absorption. For each term with (r=p-n>0), choose a Young parameter \(\delta_{\mathbf m}>0\) so that

\[
\sum_{r>0}K_{\mathbf m}\delta_{\mathbf m}\le\tfrac12.
\]

Apply \(y^r\le\delta_{\mathbf m}y^p+C_{p,r,\delta_{\mathbf m}}\) to \(y=|Z|/R_Q\). Terms with (r=0) are already constant multiples of (R_Q^p). Summing (18) therefore gives

\[
\left|Z^p-E_p\right|
\le\tfrac12|Z|^p+C_{p,\eta,\alpha}R_Q^p.
\tag{19}
\]

In the real setting, (19) implies (E_p\ge\tfrac12|Z|^p-CR_Q^p); it does not imply (E_p\ge0). Integrating against nonnegative (w) proves (4). Absolute convergence and the supplied ceilings ensure that the moment being absorbed is finite before this argument starts, so there is no circular integrability assumption.

Under the grant, choose (0<\eta<1/4). Then (Q^{-p/4+p\eta}\le1) and (4) gives (M_p(Z)\ll T^{1+\varepsilon}). Only the order-(p) grant was used. If (I_p) is negative, its sign is retained throughout; the identity itself limits how negative it can be.

### 3.6 Genuine lower-moment induction and exact availability requirements

A different valid route is induction at a fixed cutoff exponent \(\alpha\) and for the same tail family \(Z_\alpha\). The distribution gives (M_2(Z_\alpha)\ll T^{1+\varepsilon}). Suppose all lower even moments up to (p-2) have this bound. Hölder interpolation against the finite weighted measure gives the same bound for every integer (0\le r\le p-2), including odd (r). The power-sum factors in (9) are bounded by constants after taking a sufficiently small fixed coefficient loss. The order-(p) grant then yields (M_p(Z_\alpha)\ll T^{1+\varepsilon}).

This pure induction requires grants at orders (4,6,\ldots,p) for that same fixed \(\alpha\) and tail family, or some other already established bounds for every lower moment needed in (9). Bounds for an unrelated tail at a different cutoff cannot silently be substituted. The absorption argument in §3.5 removes this lower-order availability requirement entirely.

For the full function (B\), either route leaves the head exponent (H_p(\alpha)\). The exact distinctions are:

1. **One tested pair.** A grant at one fixed ((p,\alpha)), together with that pair's packet assumptions, implies (M_p(B)\ll T^{H_p(\alpha)+\varepsilon}). Absorption needs no other grant.
2. **One fixed positive cutoff exponent.** If grants are available for unbounded fixed even orders at one fixed \(\alpha>0\), the resulting head-based restored exponents tend to (1/4+\alpha/8\), because (H_p(\alpha)/p\to\alpha/4\). The head cannot be discarded.
3. **Endpoint availability.** Grants at ((p,0)) for arbitrarily large fixed even (p), for the same (B\) whose moments are being restored, give (M_p(B)\ll T^{1+\varepsilon}) and restored exponent (1/4+3/[4(p+1)]\). This tends to (1/4\). One need not have grants at every lower order if absorption is used.
4. **Cutoffs approaching zero.** It also suffices to have grants for an unbounded sequence of fixed even orders (p_j\) and fixed cutoff exponents \(\alpha_j\to0\), with each decomposition and distribution estimate applying to the same (B\). Indeed,
   \[
   H_{p_j}(\alpha_j)\le1+\alpha_j(p_j-2)/4,
   \quad
   \Theta_{\rm abs}(p_j,\alpha_j)
   \le\tfrac14+\frac3{4(p_j+1)}+\frac{\alpha_j}{8}.
   \]
5. **Meaning of uniform availability.** To obtain a bound with any prescribed final positive loss, choose one sufficiently large order and, when needed, one sufficiently small cutoff exponent; then keep both fixed as (T\to\infty\). Constants may depend arbitrarily on that selected pair. Uniform constants in (p\), in \(\alpha\to0\), or for a choice (p=p(T)\) are not required. What is required is availability of the hypotheses at the selected pairs for the same target function. A finite set of tested grants, or grants only above a positive cutoff lower bound, does not supply that availability.

Fixed positive \(\alpha\) really can leave a large head under every signed-integral grant. For a nonzero weight, let (A=Q^{1/4}\), take (Z=0\) and all (f_d=0\), and set (B=L=A\) on a measurable set of weighted measure a sufficiently small constant times \(A^{-2}+TA^{-q}\), with (B=L=1\) elsewhere in the weighted window. Such a set exists for all sufficiently large (T\). The distribution is valid: for (1\le V<A\), its left side is that fixed small measure and its right side is minimized as (V\uparrow A\); above (A\), it is zero. The ceilings hold, every (I_p=0\), and

\[
M_p(B)\asymp T+A^{p-2}+TA^{p-q}
\]

at fixed positive \(\alpha\), hence has exponent (H_p(\alpha)\). This is an abstract control showing that extra information about the head, or availability at smaller cutoffs, is material. It is not a lower bound for any arithmetic moment or for a separately defined restored quantity.

## 4. First doubtful or unproved step

There is no unproved algebraic step in the finite identity, its dominated limit, the layer-cake calculation, the restricted optimization, the absorption argument, or the fixed-cutoff induction stated above.

The first unproved input is exactly the diagnostic hypothesis (I_p\ll T^{1+\varepsilon}\). The supplied packet does not establish it at even one pair. A conclusion at arbitrarily small restored loss additionally needs grants at the order/cutoff pairs described in §3.6 and their application to the same target (B\). Availability at finitely many tested pairs cannot be extrapolated. Finally, use of the restoration formula in a particular problem is a separate application hypothesis.

A purported unconditional barrier based only on the optimized nonabsorbing expression (2) would have a false first step: it would identify one deliberately restricted bounding procedure with every consequence of the hypotheses. Formula (4) explicitly disproves that identification.

## 5. Required controls and outcomes

1. **Order (p=4\): PASS, exact algebra.**
   \[
   E_4=Z^4-6Z^2S_2+3S_2^2+8ZS_3-6S_4.
   \]
   The transfer errors are bounded by constants times
   \(Q^{-1/2}M_2+Q^{-1}M_0+Q^{-5/4}M_1+Q^{-2}M_0\), with separately allocated coefficient losses. The largest inherited exponent is (1-\alpha/2\). Here (H_4=1\) throughout the allowed interval, so (E(4)=1\) and \(\Theta(4)=2/5\).
2. **Order (p=12\): PASS, all partitions included by (6).** The one-pair coefficient is \(\binom{12}{2}=66\), and its exponent is (8\beta-\alpha/2\). Every other partition is dominated by (15). The complete head exponent is \(\max(1,5\alpha/2,1+5\alpha/13)\). The optimum is
   \[
   \alpha_* =\frac{26(8\beta-1)}{23},\quad
   E(12)=\frac{13+80\beta}{23},\quad
   \Theta(12)=\frac{87+40\beta}{299}.
   \]
   The (TV^{-q}\) part of the head distribution is the active head contribution at this optimum.
3. **Fewer than (p\) indices: PASS.** The finite product \(\prod_{d\in D_N}(1+t f_d)\) has degree below (p\), so (E_{p,N}=0\) exactly. Formula (6) therefore cancels to zero. In particular, one nonzero summand gives (Z=f\), (S_h=f^h\), and the complete partition correction, not any isolated leading term, recovers (Z^p\).
4. **Coincident and vanishing functions: PASS.** For (N\) equal functions (f_d=g\), the formulas specialize to (S_h=Ng^h\) and (E_p=(N)_p g^p\), including the exact zero for (N<p\). Zero functions cause no exception. No distinctness of function values is assumed; only indices are distinct.
5. **No positivity: PASS.** With exactly (p\) indices, (p-1\) values equal to (a>0\) and one equal to (-a\), (E_p=-p!a^p<0\). At \(\alpha=0\), taking (a\le1/p\), (L=0\), and (B=Z\) satisfies the distribution trivially above level (1\) and fits the amplitude assumptions. The signed transfer and absorption remain valid.
6. **Endpoint \(\alpha=0\): PASS.** The floor is exactly (Q=1\). The head is bounded; the nonabsorbing correction is (m(p-2)\), which exceeds (1\) for (p\ge12\), but absorption gives the stronger bound (M_p(Z)\le2I_p+O(T)\). This explicitly separates a deficient inherited certificate from a valid consequence of the same granted hypotheses.
7. **Crossing (q\) and logarithms: PASS.** Formula (10) includes both (r=2\) and (r=q\) logarithms. Head orders (10<q<12\) lie on different sides of the second-moment-distribution threshold. For tail moments above (q\), the strict inequality \(\beta(q-2)>1\) makes the (V^{-2}\) contribution dominate the (TV^{-q}\) contribution. No borderline logarithm is silently replaced by a constant.
8. **Strict epsilon allocation: PASS.** For a desired final loss \(\varepsilon>0\) and a fixed order, select the ceiling/distribution loss \(\delta>0\) so small that the layer-cake loss \((1+p)\delta\), all boundedly many coefficient losses multiplied by \(\alpha\le4\beta\), and an allowance for logarithms sum to less than \(\varepsilon\). Each lower-moment invocation can use a smaller loss before multiplication; there is no forced fixed loss per order. In absorption, select \(0<\eta<1/4\) first, fix the finitely many constants, and only then assign Young parameters so their total absorbed coefficient is at most (1/2\). These are finite choices at fixed (p\).
9. **Fixed order versus (p(T)\): PASS with restriction.** The limits in order describe a family of estimates, each with the order fixed before (T\to\infty\). They make no estimate for (p\) growing with (T\). Factorials, partition counts, and implicit constants prohibit that unstated inference.
10. **No finite-time independence: PASS.** Every identity and inequality is deterministic and pointwise or integrated against the given weight. Coincident-function controls are included explicitly. No probabilistic independence or asymptotic independence is invoked.
11. **Restricted-certificate versus actual-moment lower bound: PASS.** The maximum and minimization in (1)–(3) describe the output of a specified estimate. They are not lower bounds for an actual moment. The fixed-positive-cutoff head construction in §3.6 is separately identified as an abstract example, not transferred to another function family.

All controls above are exact symbolic or analytic controls; no numerical experiment was conducted.

## 6. Dependencies and exact artifacts used

- `protocol.md`: output contract, statement-only isolation, and state-ownership requirements.
- `rounds/codex-managed/gc-full-goal-distinct-source-review/briefs/blind_moment_family_statement.md`: the entire mathematical assumption packet and requested controls.
- Elementary formal power-series coefficient extraction, absolute/uniform convergence under \(\sum A_d<\infty\), layer cake, Hölder, and Young inequalities, each used explicitly above. No imported source theorem is required.
- The conductor's follow-up requested precise treatment of the absorption distinction, endpoint availability, and order-dependent constants; it was not used as evidence for any formula.

No other artifact or source was consulted. The graph hash is copied metadata and was not independently read or validated by this isolated reviewer.

## 7. Recommended state effect

**Promote as proved abstract conditional lemmas**, subject to the conductor's required seam review and graph validation: the complete partition identity and infinite limit; the one-sided signed transfer; the inherited nonabsorbing certificate with its exact optimization; and the stronger same-order absorption lemma (4).

**Revise any proposed barrier** that treats the nonabsorbing order limit (1/4+\beta/2\) as ruling out all recursive or absorbing consequences. Such a claim is false under the packet plus the stated diagnostic grants: endpoint availability yields full (T^{1+\varepsilon}\) moments and restored exponents approaching (1/4\).

**Retain as unproved premises** the signed-integral grants themselves, their availability at the required order/cutoff pairs for the same target function, and any arithmetic or downstream restoration identification. No state, validation matrix, synthesis, proof draft, sibling artifact, or successor-round artifact was edited by this task.
