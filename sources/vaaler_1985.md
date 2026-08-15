# Source Card: Vaaler 1985

## Bibliographic Data

Jeffrey D. Vaaler, “Some extremal functions in Fourier analysis,” *Bulletin of the American Mathematical Society (New Series)* **12** (1985), no. 2, 183–216.

- DOI: [10.1090/S0273-0979-1985-15349-2](https://doi.org/10.1090/S0273-0979-1985-15349-2)
- MR: 0776471 (86g:42005)
- Zbl: 0575.42003
- [AMS article record](https://www.ams.org/journals/bull/1985-12-02/S0273-0979-1985-15349-2/)
- [Official AMS PDF](https://www.ams.org/journals/bull/1985-12-02/S0273-0979-1985-15349-2/S0273-0979-1985-15349-2.pdf)
- [Accessible scan](https://scispace.com/pdf/some-extremal-functions-in-fourier-analysis-1fijhvmlkp.pdf)

## Local File / Integrity

- Local PDF: `sources/papers/vaaler_1985.pdf`
- SHA-256: `E606CCEF342E72D7E48B59A7DA7F8577F72FD351CE32989B23DD85E9E8CD4C1A`
- Rendered audit locations: Theorem 6 on article pp. 192–193; equations (6.5)–(6.6) on p. 206; equations (7.1)–(7.3) on p. 207; Theorem 18 on pp. 210–211.

## Exact Results Used

Vaaler writes `e(u)=exp(2 pi i u)`.  Theorem 6, equation (2.28), gives

\[
\widehat J(t)=
\begin{cases}
1,&t=0,\\
\pi t(1-|t|)\cot(\pi t)+|t|,&0<|t|<1,\\
0,&|t|\ge1.
\end{cases}
\]

The theorem further records that \(\widehat J\) is even, nonnegative, continuously differentiable, and strictly decreasing on \([0,1]\).

Equation (6.5) defines the normalized periodic Fejer kernel

\[
k_N(x)=\sum_{|n|\le N}\left(1-\frac{|n|}{N+1}\right)e(nx)
=\frac1{N+1}\left(\frac{\sin \pi(N+1)x}{\sin\pi x}\right)^2.
\]

Equation (6.6) uses the midpoint sawtooth

\[
\psi(x)=x-\lfloor x\rfloor-\frac12\quad(x\notin\mathbb Z),
\qquad \psi(x)=0\quad(x\in\mathbb Z).
\]

Equations (7.1)–(7.3) periodize the scaled entire functions \(I_{2N+2}\), \(J_{N+1}\), and \(K_{N+1}\) into trigonometric polynomials \(i_N,j_N,k_N\).  With Vaaler's scaling \(F_\delta(x)=\delta F(\delta x)\),

\[
\widehat J_{N+1}(n)=\widehat J\!\left(\frac{n}{N+1}\right).
\]

Theorem 18 defines

\[
p_N(x)=(\psi*j_N)(x)
=\sum_{\substack{|n|\le N\\n\ne0}}
\frac{-\widehat J_{N+1}(n)}{2\pi i n}e(nx)
\]

and equation (7.14) gives

\[
|p_N(x)-\psi(x)|\le \frac{k_N(x)}{2N+2}.
\]

Equations (7.13), (7.15), and (7.16) supply the sign, magnitude, and extremal-majorant properties; equation (7.17) supplies the periodized error identity.  They are not needed beyond confirming the normalization above.

## Project Notation Translation

Set \(H=N\), \(K_H=k_N\), and

\[
\Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\qquad 0<u<1.
\]

Then, for \(1\le |h|\le H\),

\[
\alpha_{h,H}=-\frac{\Phi(|h|/(H+1))}{2\pi i h}.
\]

The project's floor-compatible function is

\[
\psi_F(x)=x-\lfloor x\rfloor-\frac12,
\]

including \(\psi_F(n)=-1/2\) at integers.  Off the integers it equals Vaaler's \(\psi\), so (7.14) applies directly.  At an integer \(n\), the paired trigonometric polynomial has \(p_H(n)=0\), while

\[
\frac{K_H(n)}{2H+2}=\frac{H+1}{2H+2}=\frac12.
\]

Therefore the floor-compatible corollary holds for every real \(x\) and integer \(H\ge0\):

\[
\psi_F(x)=\sum_{1\le|h|\le H}\alpha_{h,H}e(hx)+R_H^F(x),
\qquad
|R_H^F(x)|\le\frac{K_H(x)}{2H+2}.
\]

The sign identity (7.13) does not transfer at integers and is not used there.

## M2 Coefficient Consequences

For

\[
C_h=e(h/4)-e(3h/4),
\]

one has \(C_h=2i\chi_4(h)\) for odd \(h\) and \(C_h=0\) for even \(h\).  Hence

\[
\beta_{h,H}=\alpha_{h,H}C_h
=-\frac{\Phi(|h|/(H+1))\chi_4(|h|)}{\pi|h|}
\mathbf 1_{2\nmid h}.
\]

Thus \(\beta_{h,H}\) is real and even.  Since Theorem 6 makes \(\Phi\) decreasing on \([0,1]\) and \(\Phi(1/2)=1/2\),

\[
|\beta_{1,H}|=\frac{\Phi(1/(H+1))}{\pi}\ge\frac1{2\pi}
\qquad(H\ge1).
\]

## Hypotheses / Endpoint Conventions

- The truncation height is an integer \(H\ge0\); the unit-frequency lower envelope requires \(H\ge1\).
- The source's midpoint convention and the project's floor-compatible convention differ only at integers; the endpoint corollary above must remain explicit.
- The Fejer kernel is normalized exactly as in (6.5), so \(K_H(0)=H+1\).
- The Fourier coefficient uses \(H+1\), not \(H\), in the argument of \(\Phi\).

## Rendered-Source Caution

The displayed uniqueness line immediately after (7.16) appears to print a coefficient \((2N+1)^{-1}k_N\).  That conflicts with (7.16) and \(\int k_N=1\); the consistent coefficient is \((2N+2)^{-1}\).  This apparent typographical issue is irrelevant to equation (7.14), which is the result imported by H4.  The suspect uniqueness line is not used.

## How Used In This Project

This source supplies the external theorem dependency for the finite floor-compatible Vaaler expansion, the Fejer residual, the exact \(\alpha_{h,H}\) normalization, the M2 odd-frequency beta algebra, and the uniform unit-frequency lower envelope.

## Not Sufficient For

It does not prove the reciprocal main-sum estimate `M9`, the exact-resonance mass bound, a near-collision estimate, or the Gauss-circle endpoint.  It also does not provide nondegeneracy of the project's dyadic weights.

## Audited By

- Round 2 source auditor: `rounds/codex-managed/m9-unit-frequency-w1-validation/reports/h4_weight_normalization_review.md`
- Conductor cross-check: `rounds/codex-managed/m9-unit-frequency-w1-validation/reviews/conductor_weight_transfer_analysis.md`

## Audit Status

`completed_primary_source_audit`

## Rounds Referencing This Source

- `rounds/web-research-test/round_027/judge/judge-027.md`
- `rounds/obligation-main/round_004/responses/A1-004.md`
- `rounds/codex-managed/m9-unit-frequency-w1-validation/reports/h4_weight_normalization_review.md`
