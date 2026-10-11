# Round210: statement-only independent frequency-bin transfer

Campaign: `gc-signed-near-frequency-cancellation`  
Task: `blind_bin_transfer`  
Role/status: independent blind rederivation, statement-only  
Generated: 2026-09-27 15:25:54 UTC  
Graph hash: deliberately unavailable under the statement-only isolation rule; no graph was read.

## 1. Result: transfer lemma and three no-go conclusions

The proposed transfer with the scaled derivative term is valid. For fixed scaled intervals and cutoff,

\[
\int_I|F(x)|^2\,dx\leq C\sum_j\int_{I^*}
\bigl(|B_j(x)|^2+X^2|B'_j(x)|^2\bigr)\,dx. \tag{1}
\]

The derivative-free replacement is false for arbitrary smooth amplitudes. Replacing the internally phased bins by their bin-zero coefficient sums is also false, even for constant amplitudes and even if derivatives of those zero sums are retained.

A moving prefix admits the valid bound

\[
\int_I\left|\sum_{\ell\leq f(x)}\sum_\mu
C_{\mu,\ell}(x)e(\mu x)\right|^2dx
\leq C d\sum_{Q\in\mathcal D}\sum_j\int_{I^*}
\bigl(|B_{j,Q}|^2+X^2|B'_{j,Q}|^2\bigr)dx, \tag{2}
\]

where \(d=1+\lceil\log_2 L\rceil\) and \(\mathcal D\) is the full canonical dyadic label tree after zero padding. This pays one outer logarithm and retains the complete dyadic energy. An additional logarithm arises if a separate common bound is available for the total energy at each dyadic level. No bound of that kind follows from the energy of the full unmasked sum.

The exact single-frequency energy and the supplied separation scale do not imply the required binned energy. The first missing mathematical input is a bound on the actual internally phased bin energy, including the derivative and, when necessary, every dyadic label block. The generic counterexamples below are not counterexamples to any unspecified arithmetic coefficient system.

## 2. Exact statements and hypotheses

Write \(I=XJ\), \(J=[a,b]\), and \(I^*=XJ^*\), where \(J^*\) is a fixed bounded interval containing \(J\) in its interior. Let \(\eta\in C_c^\infty(J^*)\) equal one on \(J\). There are finitely many distinct real frequencies. For

\[
\mathcal M_j=\{\mu:j/X\leq\mu<(j+1)/X\},\qquad
\delta_{\mu,j}=\mu-j/X,
\]

define

\[
B_j(x)=\sum_{\mu\in\mathcal M_j}C_\mu(x)e(\delta_{\mu,j}x).
\]

Then \(0\leq X\delta_{\mu,j}<1\) and
\(F(x)=\sum_j e(jx/X)B_j(x)\) exactly. Absolute continuity of the amplitudes suffices for these identities and the a.e. derivative formula. If the right side of (1) is infinite, the assertion is vacuous. Otherwise the cutoff bin functions are in \(H^1\), and the proof below applies. The constant in (1) depends on the fixed cutoff, not on \(X\), the number or positions of frequencies, or the amplitudes.

For (2), assume \(L\geq1\), each \(C_{\mu,\ell}\) is smooth on \(I^*\), and \(f:I\to\mathbb Z\) is measurable. Measurability is the minimal implicit repair needed to discuss the integral; no continuity or variation assumption is imposed on \(f\). Clip its values to \([0,L]\). Put \(m=\lceil\log_2L\rceil\), extend the labels to \(2^m\) by zero amplitudes, and set

\[
\mathcal D=\left\{
\{r2^k+1,\ldots,(r+1)2^k\}:0\leq k\leq m,
\ 0\leq r<2^{m-k}\right\}.
\]

For every fixed \(Q\in\mathcal D\), use its complete amplitudes throughout \(I^*\):

\[
C_{\mu,Q}=\sum_{\ell\in Q}C_{\mu,\ell},\quad
F_Q=\sum_\mu C_{\mu,Q}e(\mu x),\quad
B_{j,Q}=\sum_{\mu\in\mathcal M_j}C_{\mu,Q}e(\delta_{\mu,j}x).
\]

No selection indicator is included in \(C_{\mu,Q}\) or \(B_{j,Q}\).

For the physical comparison, a conductor clarification received after the frozen packet specifies that \(G=T^{473/65}N^{-1/2}\) is a threshold for the **squared** \(L^2\) integral, originally a tenth moment when \(F=Q_N^5\). This report uses that clarified convention. It makes no use of a supplied formula for \(Q_N\), because none was supplied.

## 3. Proof and derivation

### 3.1. A fixed-scale synthesis inequality

For a finite family of compactly supported \(H^1(\mathbb R)\) functions \(g_j\), define
\(S(t)=\sum_j e(jt)g_j(t)\). Use the Fourier transform
\(\widehat g(\xi)=\int g(t)e(-\xi t)dt\). Then

\[
\widehat S(\xi)=\sum_j\widehat g_j(\xi-j).
\]

Cauchy--Schwarz gives

\[
|\widehat S(\xi)|^2\leq
\left(\sum_{j\in\mathbb Z}\frac1{1+4\pi^2(\xi-j)^2}\right)
\sum_j\bigl(1+4\pi^2(\xi-j)^2\bigr)
|\widehat g_j(\xi-j)|^2.
\]

The first factor has an absolute upper bound \(C_0\). Indeed, choose a nearest integer \(j_0\) to \(\xi\). Its term is at most one, and the two tails are bounded by
\(2\sum_{n\geq1}(1+4\pi^2(n-1/2)^2)^{-1}<\infty\).
Integration, a change of variable in each summand, and the Fourier Plancherel identity give

\[
\|S\|_2^2\leq C_0\sum_j
\int_{\mathbb R}(1+4\pi^2u^2)|\widehat g_j(u)|^2du
=C_0\sum_j(\|g_j\|_2^2+\|g'_j\|_2^2). \tag{3}
\]

This proves the synthesis estimate without a frequency-count factor.

Now set \(g_j(t)=\eta(t)B_j(Xt)\), extended by zero outside \(J^*\). Then

\[
g'_j(t)=\eta'(t)B_j(Xt)+X\eta(t)B'_j(Xt).
\]

Consequently, with
\(C_\eta=\max\{\|\eta\|_\infty^2+2\|\eta'\|_\infty^2,
2\|\eta\|_\infty^2\}\),

\[
X(\|g_j\|_2^2+\|g'_j\|_2^2)
\leq C_\eta\int_{I^*}(|B_j|^2+X^2|B'_j|^2)dx.
\]

On \(I\), \(\eta(x/X)=1\). Therefore

\[
\int_I|F|^2dx\leq
X\left\|\sum_j e(jt)g_j(t)\right\|_2^2,
\]

and (3) proves (1) with \(C=C_0C_\eta\). This accounts for both the Jacobian \(dx=Xdt\) and the derivative factor \(X^2\).

### 3.2. The derivative and internal phases cannot simply be discarded

For the derivative-free claim, take \(M\) frequencies \(\mu_j=j/X\), \(1\leq j\leq M\), and smooth amplitudes
\(C_{\mu_j}(x)=e(-jx/X)\). Each bin contains one frequency, so

\[
B_j=e(-jx/X),\qquad F=M.
\]

Thus

\[
\int_I|F|^2dx=M^2|I|,\qquad
\sum_j\int_{I^*}|B_j|^2dx=M|I^*|.
\]

Their ratio tends to infinity with \(M\). All amplitudes are smooth.

For the bin-zero replacement, place two frequencies \(0\) and \(1/(2X)\) in bin zero and assign the constant amplitudes \(1\) and \(-1\). The bin-zero sum
\(A_0=\sum_{\mu\in\mathcal M_0}C_\mu\) and its derivative both vanish, whereas

\[
B_0(x)=1-e(x/(2X))
\]

is nonzero almost everywhere on every nondegenerate interval. Hence even
\(\int(|A_0|^2+X^2|A'_0|^2)\) cannot replace the true bin energy.

The derivative that must actually be controlled is

\[
B'_j=\sum_{\mu\in\mathcal M_j}e(\delta_{\mu,j}x)
\bigl(C'_\mu+2\pi i\delta_{\mu,j}C_\mu\bigr). \tag{4}
\]

Residual frequencies are \(O(X^{-1})\), but their phases over intervals of length \(X\) are of order one. Small residual frequencies alone do not preserve cancellation in \(A_j\). For comparison, if \(n_j=|\mathcal M_j|\), a legitimate but potentially expensive bound is

\[
|B_j|^2+X^2|B'_j|^2
\leq n_j\sum_{\mu\in\mathcal M_j}
\bigl((1+8\pi^2)|C_\mu|^2+2X^2|C'_\mu|^2\bigr). \tag{5}
\]

This follows directly from Cauchy--Schwarz and \(X|\delta_{\mu,j}|\leq1\). Its occupancy factor is not free cancellation.

### 3.3. Moving prefixes and the exact logarithmic accounting

Every prefix \(\{1,\ldots,r\}\), \(0\leq r\leq L\), is a disjoint union of canonical dyadic intervals obtained from the binary expansion of \(r\). Denote this collection by \(\mathcal P(r)\); it contains at most \(d=m+1\) intervals. At each \(x\), the moving prefix expression is exactly

\[
F_{\leq f}(x)=\sum_{Q\in\mathcal P(f(x))}F_Q(x).
\]

Finite-dimensional Cauchy--Schwarz, followed by discarding selection restrictions on a nonnegative sum, gives

\[
|F_{\leq f}(x)|^2
\leq d\sum_{Q\in\mathcal P(f(x))}|F_Q(x)|^2
\leq d\sum_{Q\in\mathcal D}|F_Q(x)|^2.
\]

Integrating over \(I\) and applying (1) separately to every complete, fixed \(Q\) proves (2). In particular, it does not differentiate \(f\), or a selection indicator, or an amplitude truncated to a set depending on \(x\).

Let

\[
E_Q=\sum_j\int_{I^*}(|B_{j,Q}|^2+X^2|B'_{j,Q}|^2)dx,\qquad
E_k=\sum_{Q\in\mathcal D:\,|Q|=2^k}E_Q.
\]

The unconditional bookkeeping is precisely
\(\int_I|F_{\leq f}|^2\leq Cd\sum_{k=0}^mE_k\).
There is **one explicit logarithm**. If a separate result gives \(E_k\leq E_*\) for each of the \(d\) levels, then

\[
\int_I|F_{\leq f}|^2\leq Cd^2E_*.
\]

Here the second logarithm counts levels. Membership of each label in \(d\) intervals is not by itself a proof of the required level bound: coherent cross terms inside each \(Q\) remain.

The failure of a full-unmasked-energy replacement is exact already at \(L=2\). Use the single frequency \(\mu=0\), with \(C_{0,1}=1\) and \(C_{0,2}=-1\). The full unmasked amplitude and energy are zero, but the two singleton dyadic energies are each \(|I^*|\). Thus

\[
E_{\{1,2\}}=0,\qquad \sum_{Q\in\mathcal D}E_Q=2|I^*|>0.
\]

The prefix \(f\equiv1\) is identically one. No multiple of the full unmasked energy controls this example, even with an arbitrary logarithmic factor.

A jumping prefix generally destroys absolute continuity. For example, \(L=1\), \(C_{0,1}=1\), and \(f(x)=\mathbf1_{[x_0,\infty)}(x)\) produce a step. Its distributional derivative has a point mass; its a.e. derivative zero does not make it an \(H^1\) amplitude. Smoothing a jump across width \(\varepsilon\) has derivative-squared integral of order \(\varepsilon^{-1}\), so ignoring the jump is not a valid limiting argument. The fixed-block method avoids this issue entirely.

### 3.4. What the exact energy and separation do, and do not, imply

Let \(E_0=XHQ^4\). With \(X=T^2\), \(H=T/\sqrt N\), and \(Q\asymp T\),

\[
E_0\asymp T^7N^{-1/2},\qquad
\frac G{E_0}\asymp T^{18/65}. \tag{6}
\]

A separation lower bound \(\Delta\gg Q^{-10}\) implies only the generic occupancy upper bound

\[
n_j\leq 1+O(Q^{10}/X)=O(T^8).
\]

It does not imply that actual arithmetic frequencies attain that occupancy. It does permit generic frequency sets whose occupancy and coherent loss are of that order.

Here is an explicit admissible family. It suffices to choose \(Q=T\), let \(\Delta=T^{-10}\), and put
\(K=\max(1,\sup_{t\in J^*}|t|)\). Choose a fixed \(0<c<1/(100K)\), let

\[
M=\lfloor c/(X\Delta)\rfloor\asymp T^8,\qquad
\mu_r=r\Delta\quad(0\leq r<M),\qquad
C_{\mu_r}(x)=A,
\]

where \(A>0\) is constant. All frequencies lie in bin zero and have minimum separation exactly \(\Delta\). For every \(x\in I^*\),
\(|\mu_rx|<cK<1/100\); hence

\[
\left|\sum_{r=0}^{M-1}e(\mu_rx)\right|\geq M/2.
\]

Normalize \(A^2=E_0/(M|I^*|)\). The exact-frequency diagonal energy is then exactly

\[
\sum_r\int_{I^*}|C_{\mu_r}|^2dx=E_0,
\]

but

\[
E_{\rm bin}\geq\int_{I^*}|B_0|^2dx\geq (M/4)E_0.
\]

Moreover, this is not merely an excess caused by the sufficient derivative norm:

\[
\int_I|F|^2dx\geq \frac{|I|}{4|I^*|}ME_0.
\]

In view of (6), the ratio of this lower bound to \(G\) grows at least as a constant times
\(T^{8-18/65}=T^{502/65}\). The factor \(N^{-1/2}\) cancels, so the example works throughout the stated \(N\)-range. The amplitudes are constant and have no moving prefix.

There is also an independent derivative obstruction if no amplitude-variation bound is assumed: with one frequency \(\mu=0\) and \(C_0(x)=Ae(K_1x/X)\), the exact diagonal energy is \(|A|^2|I^*|\), while the binned derivative energy is
\((1+4\pi^2K_1^2)|A|^2|I^*|\). This can be arbitrarily large at fixed exact energy. This latter example diagnoses the sufficiency norm; its oscillation does not itself increase \(|F|\).

Both examples are generic analytic constructions. Neither identifies an actual fifth-sum frequency family, a Vaaler coefficient, a character coefficient, or an arithmetic moving prefix. Such identification would require data absent from the packet. In particular, the supplied scale information does not furnish a signed cancellation mechanism that distinguishes the desired arithmetic expression from these coherent examples.

## 4. First doubtful or unproved step

There is no unproved step within (1) or (2), under the stated hypotheses. The first missing input for their proposed application is an estimate for the actual coefficient system of the form

\[
\sum_j\int_{I^*}(|B_j|^2+X^2|B'_j|^2)dx\ll G,
\]

or, with a prefix,

\[
d\sum_{Q\in\mathcal D}\sum_j\int_{I^*}
(|B_{j,Q}|^2+X^2|B'_{j,Q}|^2)dx\ll G.
\]

Bounds may allocate the logarithms elsewhere, but must explicitly pay them. The exact diagonal energy, the minimum separation, and the energy of the complete unmasked sum do not supply these estimates. Any argument that substitutes one of those quantities without a new lemma first fails at that substitution. No arithmetic derivative estimate or signed near-frequency cancellation estimate was furnished, proved, or disproved here.

## 5. Required control tests and outcomes

All controls are analytic; no numerical or symbolic experiments were performed.

1. **Cancellation of the inter-bin carriers:** \(C_{j/X}=e(-jx/X)\) makes \(F=M\). Outcome: rejects a uniform derivative-free transfer.
2. **Internal two-frequency cancellation:** coefficients \(1,-1\) at \(0,1/(2X)\) give a zero bin-zero sum but a nonzero true bin. Outcome: rejects dropping internal phases, even with derivatives of the zero sum.
3. **Dyadic cancellation:** labels \(1,-1\) at a single frequency give zero full energy and positive total dyadic energy. Outcome: rejects bounding all dyadic blocks by the complete unmasked energy.
4. **Coherent separated cluster:** \(M\asymp T^8\) frequencies separated by \(T^{-10}\) fit in a small part of one \(X^{-1}\)-bin. Outcome: exact diagonal energy \(E_0\) coexists with binned and direct energy \(\gg ME_0\), exceeding the proposed \(G\) threshold.
5. **Single-frequency variation:** \(Ae(K_1x/X)\) at frequency zero has fixed exact energy and unbounded scaled derivative energy. Outcome: amplitude regularity must be quantitatively controlled, not merely assumed smooth.

The transfer lemmas survive these controls because they retain the derivative, the actual internal phases, and all fixed dyadic-block energies. They do not assert cancellation for unsigned or adversarial inputs.

## 6. Dependencies and exact artifacts used

Only the following files were read:

- `protocol.md`.
- `rounds/codex-managed/gc-signed-near-frequency-cancellation/briefs/blind_bin_transfer_statement.md`.

An additional conductor message clarified only the convention that \(G\) denotes a squared \(L^2\) energy threshold. No claimant derivation or arithmetic data accompanied that clarification. Mathematical tools used are the Fourier Plancherel identity, the weak derivative Fourier identity, finite-dimensional Cauchy--Schwarz, and the binary decomposition of integer prefixes; the transfer argument itself is given above. No web sources were used. No state file, general generated brief, other report, historical proof, validation matrix, or synthesis was read or edited. The only written artifact is this task report.

## 7. Recommended state effect

**Retain** the scaled derivative transfer and the fixed-dyadic-block prefix reduction as proved analytic interface candidates, subject to the conductor's required seam validation and graph process. **Revise or reject** any formulation that removes derivatives, replaces internally phased bins by bin-zero sums without a separate cost, bounds the complete dyadic energy by full unmasked energy, or deduces the arithmetic binned estimate solely from exact energy and spacing.

**No promotion of the arithmetic target or its signed-cancellation obligation is justified by this report.** The generic controls establish the insufficiency of the listed inputs; they do not refute an arithmetic estimate whose defining coefficients were not supplied. No successor-round work is undertaken.
