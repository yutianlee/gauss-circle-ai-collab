# Round223: isolated oscillatory Fourier transfer

- Task: blind_oscillatory_transfer; campaign: gc-full-goal-signed-source-review.
- Role: statement-only independent rederivation of the isolated analytic packet.
- Generated: 2026-09-28. Prior-agent history from rounds218--222 is disclosed; this is not history-free blindness.
- Access: only protocol.md and the isolated statement were read. No campaign, graph, strategy, source, application or sibling file was read. A current graph hash was therefore not consulted or verified.
- Allocation: 100 percent analytical; no web searches, source imports or experiments.

## 1. Result

The fixed-profile continuous assertion and the stated transfer identity are correct, including the Fourier signs. With the packet's hypotheses,

\[
 c\sqrt{\lambda}\le \|\widehat F_\lambda\|_{L^1(\mathbb R)}
                    \le C\sqrt{\lambda}
 \qquad(\lambda\ge1).
 \tag{1}
\]

The signed and absolute periodizations satisfy the different exact formulas

\[
 G_{\lambda,N}(\alpha)
   =\sum_{n\in\mathbb Z}F_\lambda(n/N)e(-n\alpha),
 \qquad
 \int_0^1 A_{\lambda,N}(\alpha)\,d\alpha
   =\|\widehat F_\lambda\|_1.
 \tag{2}
\]

The Fourier sum in (2) is finite. Thus

\[
 \sum_n c_nF_\lambda(n/N)
   =\int_0^1G_{\lambda,N}(\alpha)S(\alpha)\,d\alpha,
 \quad
 \left|\sum_n c_nF_\lambda(n/N)\right|
   \le\int_0^1 A_{\lambda,N}(\alpha)|S(\alpha)|\,d\alpha.
 \tag{3}
\]

The lower bound in (1) does not transfer automatically to the norm of the signed periodization, a sampled sum, or an optimal discrete functional norm. In the required one-sample control,

\[
 G_{\lambda,1}(\alpha)=W(1)e(\lambda)e(-\alpha),
 \qquad
 \|G_{\lambda,1}\|_{L^1(0,1)}=|W(1)|
 \quad\text{for every }\lambda\ge1.
 \tag{4}
\]

The cost \(\sqrt{\lambda}\) is sharp for the named continuous absolute-periodization mass. It is not a universal lower cost for every signed or discrete transfer. No arithmetic application is made.

## 2. Exact hypotheses and conventions

Let \(0<a<b\), let \(W\ne0\) be a fixed complex-valued function in \(C_c^\infty((a,b))\), and let \(\phi\) be fixed, real and smooth on a neighbourhood of \([a,b]\), with

\[
 |\phi''(x)|\ge c_0>0\qquad(a\le x\le b).
 \tag{5}
\]

Continuity implies that \(\phi''\) has one sign throughout this interval. We use

\[
 e(t)=\exp(2\pi it),\quad
 F_\lambda(x)=W(x)e(\lambda\phi(x)),\quad
 \widehat F_\lambda(u)=\int_{\mathbb R}F_\lambda(x)e(-ux)\,dx.
 \tag{6}
\]

The zero extension of \(F_\lambda\) is smooth because \(W\) vanishes near both endpoints. Fix \(\delta>0\) such that

\[
 \operatorname{supp}W\subset[a+\delta,b-\delta],
 \tag{7}
\]

and write \(J=\phi'([a,b])\), an interval of positive length. All constants below may depend on these fixed profiles. No uniformity over moving profiles is assumed.

For the discrete statements, \(N\ge1\) is any real number, not necessarily an integer, and the complex coefficients \(c_n\) have arbitrary finite support on \(\mathbb Z\). Define

\[
 S(\alpha)=\sum_n c_ne(n\alpha),
 \tag{8}
\]

\[
 G_{\lambda,N}(\alpha)
    =N\sum_{m\in\mathbb Z}\widehat F_\lambda(N(\alpha+m)),
 \qquad
 A_{\lambda,N}(\alpha)
    =N\sum_{m\in\mathbb Z}|\widehat F_\lambda(N(\alpha+m))|.
 \tag{9}
\]

For each fixed \(\lambda,N\), these sums converge absolutely and uniformly on \([0,1]\), as proved below. In particular both periodizations are unambiguously defined.

## 3. Proof and derivation

### 3.1 Uniform curvature bound on the stationary band

For any \(u\in\mathbb R\), put \(g(x)=\lambda\phi(x)-ux\). Its derivative is monotone, and \(|g''|\ge\lambda c_0\). Let

\[
 D_W=\|W\|_\infty+\|W'\|_1.
 \tag{10}
\]

Here \(D_W>0\). For any \(t>0\), the set \(|g'|\le t\) is an interval of length at most \(2t/(\lambda c_0)\). The integral over that set is at most \(2t\|W\|_\infty/(\lambda c_0)\). The complement has at most two intervals. Integration by parts on each gives

\[
 \int W e(g)
 =\left[\frac{W e(g)}{2\pi i g'}\right]
 -\frac1{2\pi i}\int
      \left(\frac{W'}{g'}-\frac{Wg''}{(g')^2}\right)e(g).
 \tag{11}
\]

The boundary terms and the \(W'\) term are \(O(D_W/t)\). Since \(g'\) is monotone, the integral of \(|g''|/|g'|^2\) on the complementary intervals is \(O(1/t)\). Consequently

\[
 |\widehat F_\lambda(u)|
 \le C D_W\left(\frac{t}{\lambda c_0}+\frac1t\right).
 \tag{12}
\]

Choosing \(t=\sqrt{\lambda c_0}\) proves

\[
 \|\widehat F_\lambda\|_\infty
 \le B_W\lambda^{-1/2},
 \qquad B_W=C_0c_0^{-1/2}D_W,
 \tag{13}
\]

with an absolute constant \(C_0\), for instance a sufficiently large fixed constant such as \(20\). The estimate holds for all \(u\), including the whole stationary band \(u\in\lambda J\). The proof uses absolute values of \(W\) and \(W'\) only; positivity or constant argument of \(W\) is not required.

### 3.2 Nonstationary tails, including the ends of the band

If \(u\notin\lambda J\), monotonicity of \(\phi'\) and the support gap (7) give, on \(\operatorname{supp}W\),

\[
 |\lambda\phi'(x)-u|
 \ge \lambda c_0\delta+\operatorname{dist}(u,\lambda J).
 \tag{14}
\]

For \(j\ge2\), the derivatives of \(g\) satisfy \(g^{(j)}=\lambda\phi^{(j)}\). Repeated application of (11), now on the compact support with no boundary terms, therefore gives for every fixed integer \(q\ge1\)

\[
 |\widehat F_\lambda(u)|
 \le C_q\bigl(\lambda+\operatorname{dist}(u,\lambda J)\bigr)^{-q}
 \qquad(u\notin\lambda J).
 \tag{15}
\]

To see the uniformity in (15), every differentiation of \(1/g'\) introduces a derivative of \(g'\) of size \(O(\lambda)\), while every denominator is bounded below by a constant times \(\lambda+\operatorname{dist}(u,\lambda J)\). Hence the extra ratio \(\lambda/(\lambda+\operatorname{dist})\) is at most one. The finitely many differentiated amplitudes are controlled by derivatives of \(W\) through order \(q\) and of \(\phi\) through order \(q+1\). Their supports stay inside (7). This proves the asserted bound inductively without omitting a transition at an endpoint of \(\lambda J\).

For \(q>1\), integration over the two complementary half-lines yields

\[
 \int_{\mathbb R\setminus\lambda J}|\widehat F_\lambda(u)|\,du
 \le C_q'\lambda^{1-q}.
 \tag{16}
\]

The band has length \(\lambda|J|\). Equations (13) and (16), with \(q=2\), prove

\[
 \|\widehat F_\lambda\|_1
 \le |J|B_W\sqrt{\lambda}+C_2'\lambda^{-1}
 \le C\sqrt{\lambda}.
 \tag{17}
\]

One may take \(C=|J|B_W+C_2'\). Its profile dependence is explicit in the preceding bounds: \(c_0,\delta,a,b\), the indicated norms of \(W\), and finitely many derivatives of \(\phi\). The location of \(J\), or an added affine term in \(\phi\), does not affect its length or this argument. For fixed \(\lambda\), ordinary repeated Fourier integration by parts also shows that \(\widehat F_\lambda\) and all its derivatives decay faster than any power of \(|u|\).

### 3.3 Inversion, the \(L^2\) identity, and the lower bound

The integrability needed for inversion has already been established. For completeness, insert the Gaussian factor \(\exp(-\pi\varepsilon u^2)\), \(\varepsilon>0\). The elementary Gaussian Fourier formula and Fubini give

\[
 \int_{\mathbb R}\widehat F_\lambda(u)e(ux)
                      e^{-\pi\varepsilon u^2}\,du
 =\varepsilon^{-1/2}
      \int_{\mathbb R}F_\lambda(y)
                e^{-\pi(x-y)^2/\varepsilon}\,dy.
 \tag{18}
\]

The right side tends to \(F_\lambda(x)\), uniformly in \(x\), by the Gaussian approximate identity and uniform continuity. Dominated convergence on the left uses \(\widehat F_\lambda\in L^1\). Thus

\[
 F_\lambda(x)=\int_{\mathbb R}\widehat F_\lambda(u)e(ux)\,du
 \quad\text{for every real }x.
 \tag{19}
\]

Since \(F_\lambda\in L^1\) and \(\widehat F_\lambda\in L^1\cap L^\infty\), absolute Fubini applied to (19) gives

\[
 \int_{\mathbb R}|\widehat F_\lambda(u)|^2\,du
   =\int_{\mathbb R}|F_\lambda(x)|^2\,dx
   =\|W\|_2^2.
 \tag{20}
\]

In detail, the conjugate Fourier factor is
\(\overline{\widehat F_\lambda(u)}
 =\int\overline{F_\lambda(x)}e(ux)\,dx\);
the double integral is absolutely bounded by
\(\|\widehat F_\lambda\|_1\|F_\lambda\|_1\).

Combining (13) and (20),

\[
 \|W\|_2^2
 \le \|\widehat F_\lambda\|_\infty\|\widehat F_\lambda\|_1
 \le B_W\lambda^{-1/2}\|\widehat F_\lambda\|_1.
 \tag{21}
\]

This proves the lower bound in (1) for every \(\lambda\ge1\), with

\[
 c=\|W\|_2^2/B_W>0.
 \tag{22}
\]

It applies to complex or sign-changing \(W\) because \(|F_\lambda|=|W|\). In conjunction with (16), it also proves that the stationary band itself carries at least \(c\sqrt{\lambda}-O(\lambda^{-1})\) absolute mass. Thus the nonstationary tail cannot be responsible for the lower bound. No pointwise stationary-phase main term, or nonvanishing assertion about \(\widehat F_\lambda\) at every frequency, has been assumed.

### 3.4 Exact signed periodization and transfer signs

For fixed \(\lambda,N\), the Schwartz decay just proved implies uniform absolute convergence of both series in (9) on \([0,1]\). Derivatives of the signed series converge uniformly as well. Replacing \(\alpha\) by \(\alpha+1\) and reindexing \(m\) proves periodicity.

For every integer \(n\), absolute Fubini and \(u=N(\alpha+m)\) give

\[
 \begin{split}
 \int_0^1G_{\lambda,N}(\alpha)e(n\alpha)\,d\alpha
 &=\sum_m\int_{Nm}^{N(m+1)}
       \widehat F_\lambda(u)e(n(u/N-m))\,du\\
 &=\int_{\mathbb R}\widehat F_\lambda(u)e(nu/N)\,du\\
 &=F_\lambda(n/N).
 \end{split}
 \tag{23}
\]

The integer \(n\) makes \(e(-nm)=1\); no integrality of \(N\) is needed. The finite sum

\[
 P(\alpha)=\sum_{n\in\mathbb Z}F_\lambda(n/N)e(-n\alpha)
 \tag{24}
\]

has precisely these Fourier coefficients. It is finite because \(F_\lambda\) is compactly supported. The continuous periodic difference \(G-P\) has every Fourier coefficient zero, hence is zero: convolving it with the elementary Fejer approximate identity gives zero and converges uniformly to the difference. This proves the first identity in (2), with the negative sign in its Fourier series.

Integrating (24) against the positive-sign polynomial \(S(\alpha)\) selects equal indices. This proves (3). Equivalently, inserting (19) into the finite sampled sum and then periodizing gives the same result. There is no conjugation of \(c_n\), no reflection of its index, and no omitted factor of \(N\).

### 3.5 Absolute periodization and legal majorants

Tonelli and the same change of variables give the exact normalization

\[
 \begin{split}
 \int_0^1A_{\lambda,N}(\alpha)\,d\alpha
 &=\sum_m\int_{Nm}^{N(m+1)}
                    |\widehat F_\lambda(u)|\,du\\
 &=\|\widehat F_\lambda\|_1.
 \end{split}
 \tag{25}
\]

The equality is independent of \(N\). Also \(|G|\le A\) pointwise. Therefore

\[
 \left|\sum_n c_nF_\lambda(n/N)\right|
 \le\int_0^1|G||S|
 \le\int_0^1A|S|.
 \tag{26}
\]

If a nonnegative measurable \(B\) bounds \(|S|\) only on a measurable set \(E\), the legal consequence is

\[
 \left|\sum_n c_nF_\lambda(n/N)\right|
 \le \int_E AB+\int_{[0,1]\setminus E}A|S|.
 \tag{27}
\]

The second term cannot be dropped without a separate estimate. A majorant asserted almost everywhere is sufficient, since \(A\,d\alpha\) is absolutely continuous with respect to Lebesgue measure. A merely small exceptional set is not automatically negligible for this weighted integral.

Using a uniform bound \(|S|\le B_0\) in (26) produces the certificate
\(B_0\|\widehat F_\lambda\|_1\asymp B_0\sqrt{\lambda}\).
The two-sided size of its mass is a property of that absolute procedure; it does not force the sampled functional or a different signed transfer to have the same norm. Nor does it lower-bound \(\int A|S|\) for arbitrary \(S\).

### 3.6 The one-sample alias control and discrete norms

Take \(N=1\), \(\operatorname{supp}W\subset(1/2,3/2)\), \(W(1)\ne0\), and \(\phi(x)=\sqrt{x}\). This phase has nonzero curvature on a neighbourhood of the support. The sole integer at which \(F_\lambda\) can be nonzero is \(1\), with

\[
 F_\lambda(1)=W(1)e(\lambda).
 \tag{28}
\]

Equation (24) proves exactly (4). Hence, for arbitrary finite \(c_n\),

\[
 \sum_n c_nF_\lambda(n)=c_1W(1)e(\lambda).
 \tag{29}
\]

In particular, choosing \(S(\alpha)=e(\alpha)\) gives a sampled value of absolute size \(|W(1)|\), while the absolute certificate \(\int A|S|=\int A\) grows like \(\sqrt{\lambda}\). Choosing \(c_1=0\) gives zero. These examples separately rule out the proposed automatic lower transfer to the signed kernel norm and to sampled values.

There is also an exact optimal-norm statement. For every fixed \(N\) and \(1\le p\le\infty\), the functional on finitely supported coefficient sequences,

\[
 {\cal L}_{\lambda,N}(c)=\sum_n c_nF_\lambda(n/N),
 \tag{30}
\]

has operator norm for the coefficient \(\ell^p\) norm equal to

\[
 \|{\cal L}_{\lambda,N}\|_{\ell^p\to\mathbb C}
    =\left\|\{F_\lambda(n/N)\}_n\right\|_{\ell^{p'}}
    =\left\|\{W(n/N)\}_n\right\|_{\ell^{p'}},
 \quad \frac1p+\frac1{p'}=1.
 \tag{31}
\]

This follows from finite Holder duality, with equality by choosing the conjugate phases and the usual dual magnitudes; the endpoints \(p=1,\infty\) follow by a largest coordinate or aligned unit coefficients. It is independent of \(\lambda\). It does not claim equivalence with any other, unspecified norm on \(S\).

In the one-sample example, all norms in (31) equal \(|W(1)|\). The optimal functional norm when the denominator is \(\|S\|_\infty\) also equals \(|W(1)|\): the upper bound follows from \(|c_1|=|\int_0^1S(\alpha)e(-\alpha)\,d\alpha|\le\|S\|_\infty\), and \(S=e(\alpha)\) attains it. Thus the failure of the lower transfer persists even in the norm naturally used with the uniform majorant in Section 3.5.

### 3.7 Profile and regularity limitations

The upper constants use uniform curvature, support separation, and specified amplitude/phase derivative bounds. The lower constant additionally uses a nonvanishing \(L^2\) mass of \(W\). These conditions cannot be discarded when profiles move with a parameter or row.

For example, keeping a fixed nonzero \(W_0\) but choosing
\(W_j(x)=W_0(x)e(-\lambda_j\phi(x))\)
makes \(W_j(x)e(\lambda_j\phi(x))=W_0(x)\). Its Fourier \(L^1\) norm is fixed, not of order \(\sqrt{\lambda_j}\). The derivatives of \(W_j\) grow, so this does not contradict (1). Similarly, multiplying a fixed profile by a scalar tending to zero destroys a uniform positive lower constant.

If the curvature lower constant varies, the proof explicitly has
\(\|\widehat F_\lambda\|_\infty\ll D_W(\lambda c_0)^{-1/2}\).
For the family \(\phi_\kappa(x)=\kappa x^2/2\), the effective oscillatory parameter is \(\lambda\kappa\). Taking \(\kappa=1/\lambda\) leaves a fixed transform although \(\lambda\to\infty\). This shows why a uniform \(\sqrt{\lambda}\) lower bound with no curvature qualification is false. It does not prevent a different uniform theorem stated in terms of the effective parameter.

A sufficient family-level hypothesis for the preceding proof is a common compact support interval with a uniform support gap, uniform positive curvature lower bound and upper derivative bounds, uniform needed norms of \(W\), and a uniform positive lower bound for \(\|W\|_2\). Individual rowwise estimates alone do not justify interchanging a supremum over rows with an integral: \(\sup_j\int A_j\le\int\sup_j A_j\), with no reverse bound supplied here. The particular aggregate norm needed for a row-dependent transfer must be proved.

Hard cutoffs can destroy the absolute integrability itself. As an explicit control, let
\[
 F(x)=\mathbf1_{[1,2]}(x)e(\lambda x^2/2)
 \tag{32}
\]
for any fixed \(\lambda\). Two integrations by parts on \([1,2]\) give
\[
 \widehat F(u)
 =\frac{e(\lambda/2)e(-u)-e(2\lambda)e(-2u)}
        {2\pi i u}+O_\lambda(|u|^{-2}).
 \tag{33}
\]
The absolute value of the numerator is a nonzero periodic function of \(u\) with positive mean. Its \(1/|u|\) integral diverges, while the error is integrable. Thus \(\widehat F\notin L^1\). This example has nonzero phase curvature; its failure comes from the amplitude jumps.

For such a cutoff, inversion or periodization may require a specified symmetric, Abel or Cesaro convention, and inversion at a jump produces the average of the two one-sided limits. A literal endpoint value or star convention needs its own correction. Equations (19), (25) and (26) with a finite absolute mass must not be imported unchanged. Some less-than-smooth profiles do admit sufficient tail decay; that extension requires a proof of the relevant integrability and boundary conventions. The hard-cutoff example is not an impossibility result for every nonsmooth profile.

## 4. First doubtful or unproved step

There is no remaining unproved step in the fixed-profile assertions under (5)--(9). The automatic lower-transfer assertion is false and is corrected by (4), (29) and (31).

The first unsupported step in an extension would be one of: replacing \(A\) by \(G\) in the lower bound; dropping the exceptional-set term in (27); applying fixed-profile constants to a moving family without the required uniform bounds; or using absolute inversion/periodization for a nonsmooth cutoff without an integrable Fourier tail and exact endpoint convention. These are missing hypotheses or invalid inferences. No downstream conclusion is asserted, and no new task is initiated to supply such hypotheses.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| Curvature sign and stationary band | GREEN. The second derivative has one sign; the monotone-derivative split proves (13) on the entire band and beyond. |
| Nonstationary tail | GREEN. Support separation proves (14); all tails, including band-end transitions, are included in (15)--(16). |
| Complex/sign-changing profile | GREEN. The lower bound uses \(\|W\|_2^2>0\), not positivity or a common phase. |
| Inversion and integrability | GREEN. Absolute \(L^1\) and Gaussian regularization justify (19); Fubini proves (20). |
| Fourier sign and real \(N\) | GREEN. Equation (23) gives the negative-sign finite series for \(G\), paired with the positive-sign \(S\), for any real \(N\ge1\). |
| Signed versus absolute periodization | GREEN. Only \(A\) has exact mass \(\|\widehat F_\lambda\|_1\); \(\|G\|_1\le\int A\) has no corresponding automatic lower bound. |
| One-sample alias control | GREEN. The exact kernel is \(W(1)e(\lambda)e(-\alpha)\); its norm is constant for every \(\lambda\). |
| Optimal discrete norm | GREEN. The explicitly defined coefficient norms are given by (31); the one-sample supremum-polynomial norm is also constant. |
| Exceptional frequencies | GREEN. Equation (27) retains the entire complement. |
| Moving/nonsmooth profiles | QUALIFIED. Required uniform hypotheses are stated; explicit controls disprove unqualified extensions. |
| Isolation and scope | GREEN. Only the two permitted files were read; no arithmetic coefficient sequence or application was introduced. |

All controls are analytical. No numerical experiment was performed.

## 6. Dependencies and exact artifacts used

The derivation uses only the packet's assumptions, elementary integration by parts, Gaussian Fourier inversion, finite Fourier orthogonality, the Fejer approximate identity, Fubini/Tonelli and finite Holder duality. These elementary steps are supplied in the proof; no source theorem was imported.

| Exact artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| rounds/codex-managed/gc-full-goal-signed-source-review/briefs/blind_oscillatory_transfer_statement.md | 8f22f707e3ee85bb8438e11eff55613cba31a227a7b5a3b113bf35b12a087ea5 |

Prior-agent history is disclosed in the metadata, but no prior report was reread or used as evidence for these analytic claims. The intermediate message to the conductor reported the sign and one-sample finding; no sibling or application information entered the derivation. File reading and hashing are administrative checks, not experiments.

## 7. Recommended state effect

Retain the fixed-profile Fourier \(L^1\) lemma, exact signed transfer, absolute-periodization normalization and one-sample countercontrol as candidate analytic evidence for independent review. Reject only the automatic inference that the continuous absolute lower mass must also be a signed or discrete lower cost.

No graph promotion or arithmetic application is recommended by this isolated report. Moving profiles, nonsmooth endpoints and exceptional frequencies remain subject to their explicit hypotheses. No shared state was edited. The assigned task ends with this report and its final hash.
