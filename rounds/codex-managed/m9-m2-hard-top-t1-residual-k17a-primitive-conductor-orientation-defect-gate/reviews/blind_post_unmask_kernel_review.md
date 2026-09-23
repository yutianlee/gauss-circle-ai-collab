# Blind post-unmask kernel review

## Verdict

**GREEN.** The formalized kernel
\[
\text{proofs/kernels/m9\_m2\_hard\_top\_t1\_residual\_k17a\_primitive\_conductor\_parity\_self\_return.md}
\]
agrees with the independently saved blind derivation on the primitive projector, the isolated \(d=1\) contribution, the \(q/u_0\) normalization, the centered symmetric/antisymmetric split, and the \(q=1\) boundary. The additional unmasked all-conductor identity and self-return are exact. No repair is required on the audited seam.

The blind report was used only as an immutable comparison artifact and was not altered.

## Exact comparison and derivation audit

For \(r\mid q\), with \(d=q/r\), the formalized downsampling identity

\[
c_q(rk)=\frac1r c_d(k)
\]

is exact, including \(d=1\) and \(k=0\). Möbius inversion therefore gives

\[
K_q(b)
=\sum_{r\mid q}\frac{\mu(r)}rE_{q/r}(b)
=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b).
\]

This is identical to the blind formula. For \(b\in U(q)\), every \(d>1\) divisor has

\[
E_d(-b)=-E_d(b),
\]

whereas \(E_1(b)=E_1(-b)=1\). Hence

\[
K_q(b)+K_q(-b)=\frac{2\mu(q)}q,
\]

and the entire symmetric part comes from \(d=1\). The formalized kernel neither drops this term nor confuses it with the separate physical conductor \(q=1\).

With

\[
K_q^\circ(b)=K_q(b)-\frac{\mu(q)}q,
\]

one has \(K_q^\circ(-b)=-K_q^\circ(b)\), and the exact block is

\[
\mathcal C_{u_0,q}
=\frac q{u_0}\sum_bK_q^\circ(b)(B^+_{q,b}-B^-_{q,b})
+\frac{\mu(q)}{u_0}\sum_b(B^+_{q,b}+B^-_{q,b}).
\]

The normalization is correct: the accepted alias factor \(q/u_0\) occurs once, and multiplication by the centered trace coefficient \(\mu(q)/q\) leaves \(\mu(q)/u_0\). Equivalently, the asymmetric split has trace coefficient \(2\mu(q)/u_0\). Both forms are exact and differ only by moving the rank-one term \((\mu(q)/u_0)\sum_b(B^+_{q,b}-B^-_{q,b})\) between trace and defect. The centered formula is exactly the canonical symmetric split derived blindly.

## All-conductor identity

For odd \(u_0>1\) and \(\beta\in U(u_0)\), reduced modulo each \(q\mid u_0\),

\[
\begin{aligned}
\sum_{q\mid u_0}\frac q{u_0}K_q^\circ(\beta)
&=\frac1{u_0}\sum_{q\mid u_0}
  \sum_{\substack{d\mid q\\d>1}}\mu(q/d)dE_d(\beta)\\
&=\frac1{u_0}\sum_{\substack{d\mid u_0\\d>1}}
  dE_d(\beta)\sum_{r\mid u_0/d}\mu(r)\\
&=E_{u_0}(\beta).
\end{aligned}
\]

The last equality is valid because the inner Möbius sum vanishes unless \(d=u_0\). The hypothesis \(u_0>1\) is necessary for the centered version and is stated explicitly in (179.K10).

The buckets in (179.K4) are reductions of the same primitive atom residue \(\beta_z\), so this identity may be applied atom by atom. The minus contribution is correct because, for \(u_0>1\),

\[
E_{u_0}(-\beta_z)=-E_{u_0}(\beta_z).
\]

Thus the all-conductor centered defect equals \(\mathcal O_{u_0}\). Separately, the total unphased bucket sum is independent of \(q\), and

\[
\sum_{q\mid u_0}\mu(q)=0
\]

for \(u_0>1\); hence the all-conductor centered trace vanishes. Splitting the exact all-conductor equality into \(q\le Q_B\) and \(q>Q_B\) gives (179.K12) and (179.K13) with no missing normalization or extra absolute value. This is correctly described as self-return, not as an estimate.

The uncentered check is also exact:

\[
\sum_{q\mid u_0}\frac q{u_0}K_q(\beta)
=E_{u_0}(\beta)+\frac1{u_0}\sum_{q\mid u_0}\mu(q)
=E_{u_0}(\beta)
\]

for \(u_0>1\).

## Boundary and control outcomes

| Control | Outcome |
|---|---|
| Exact primitive projector | **PASS.** The Möbius indices, divisor coefficient \(d/q\), and Fourier sign agree with the blind derivation. |
| \(d=1\) term | **PASS.** It is \(\mu(q)/q\) in each \(K_q\) and is the sole source of \(2\mu(q)/q\) under sign reversal. |
| Unit support | **PASS.** The parity reversal is used only for reductions of \(\beta_z\in U(u_0)\), which remain units modulo every \(q\mid u_0\). |
| \(q/u_0\) normalization | **PASS.** The centered trace is \(\mu(q)/u_0\); the asymmetric trace is \(2\mu(q)/u_0\). |
| Centered split | **PASS.** It is the unique symmetric/antisymmetric split and matches the blind \(H_q=K_q-\mu(q)/q\). |
| \(q=1\) boundary | **PASS.** \(K_1(0)=1\) and \(K_1^\circ(0)=0\). Therefore (179.K10) is correctly restricted to \(u_0>1\). The \(u_0=1\) stratum is wholly low conductor, while the uncentered identity remains valid there. |
| Prime control | **PASS.** For odd prime \(p\), \(K_p=E_p-1/p\) and \(K_p^\circ=E_p\). |
| Prime-square control | **PASS.** \(K_{p^2}^\circ=E_{p^2}-p^{-1}E_p\), confirming that vanishing trace does not contract the centered kernel. |
| All-conductor centered identity | **PASS.** Möbius collapse leaves only \(d=u_0\). |
| Atomwise coarsening | **PASS.** Every \(B_{q,b}^\pm\) is defined from the same \(q\)-independent amplitudes and the reduction of the same \(\beta_z\). |
| All-conductor trace cancellation | **PASS.** The \(q=1\) trace is essential; omitting it would invalidate the cancellation. |
| High/low self-return | **PASS.** The split is an exact partition of all divisors \(q\mid u_0\), with no low-\(q\) double count. |
| Arbitrary buckets versus literal coefficients | **PASS.** The formalized file quarantines the \(Lq\) artificial capacity controls from literal lower mass, consistently with the blind no-go. |

No numerical evidence is needed for these exact finite identities.

## Exact first issue

There is **no issue in the audited formal kernel**. The first unresolved mathematical step is instead the explicitly open bound (179.K19) for the complete literal centered defect. The all-conductor identity does not advance that estimate: it reconstructs the original literal orientation block after subtraction of the already-safe low-conductor packet. Any claim that centering itself provides conductor cancellation would be the first invalid step, and the formalized kernel makes no such claim.

## Scope

This GREEN verdict covers only:

1. (179.K5)--(179.K8), including the primitive projector, \(d=1\) parity trace, normalization, and centered split;
2. the \(q=1\) and \(u_0=1\) boundary handling;
3. (179.K10)--(179.K13), including atomwise all-conductor reconstruction, trace cancellation, and high/low self-return; and
4. compatibility of those statements with the three Round 179 reports and the preserved blind derivation.

It does not independently re-audit every literal selector, endpoint, lift-count, or orientation-map claim in (179.K14)--(179.K18), and it does not prove (179.K19), (177.K34), complete K17a, a parent obligation, a bridge, a theorem, or an exponent improvement.

## Recommended effect and edit discipline

**GREEN for promotion through the required conductor process** of the audited finite kernel and self-return, with the stated scope. Retain the complete literal centered defect as open and retain the arbitrary-bucket controls only as coefficient-uniform no-go evidence.

Only this review file was written. No proof graph, proof draft, validation matrix, synthesis, candidate, formalized kernel, saved blind report, or other artifact was edited.
