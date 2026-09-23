# Round 175 statement-only packet: whole-chain residual scale correlation

- Round: 175
- Campaign: m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate
- Access: statement only
- Graph hash supplied only as provenance:
  e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211
- Evidence status: candidate only

## Exact literal coefficient

Let

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor,\qquad
 1\ll L\ll H\le J^{1/2}.
\tag{175.B1}
\]

Let \(\mathcal I_L^{\rm lit}\) be a fixed half-open shell of squarefree
integers \(N\asymp L^2\), with every endpoint, floor, star, and point-value
convention part of the data. Write \(N=2^{\nu_N}M_N\), with
\(\nu_N\in\{0,1\}\) and \(M_N\) odd.

For each \(N\), a deterministic rule either selects no pair or selects
distinct odd primes \(p_N,q_N\mid M_N\) satisfying

\[
 \chi_4(p_Nq_N)=-1,\qquad
 |\log(q_N/p_N)|\le\kappa L^{-1/2}.
\tag{175.B2}
\]

If no pair is selected, set \(\rho_N(d)=1\). Otherwise put

\[
 \rho_N(d)=1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
 +2\mathbf1_{p_N\mid d}\mathbf1_{q_N\mid d}.
\tag{175.B3}
\]

For odd \(d\mid M_N\), define

\[
\begin{aligned}
 A_N(d)
 &=\mathbf1_{\{\sqrt N\le d\le2\sqrt N\}}^{\rm lit}
   \eta_L(d)\Phi\!\left(\frac d{H+1}\right)
   W\!\left(\frac{\sqrt{q_X}\,d}{2\sqrt N}\right),\\
 \omega_L(N)
 &=\mathbf1_{\mathcal I_L^{\rm lit}}(N)\mu^2(N)
   \left(\frac{L^2}{N}\right)^{3/4},\\
 \lambda_N(d)&=\omega_L(N)\rho_N(d)A_N(d).
\end{aligned}
\tag{175.B4}
\]

All three functions are zero outside their literal domains. The smooth
pieces have bounded fixed-rescaling \(C^1\) norms and
\(\eta_L'(d)\ll L^{-1}\); no hard face is smoothed. Put

\[
 c_N^{\rm rem}
 =\sum_{\substack{d\mid N\\d\ {\rm odd}}}\chi_4(d)\lambda_N(d),
 \qquad
 z_N=c_N^{\rm rem}e(J\sqrt N),
 \qquad
 D_L=\sum_N|z_N|^2\ll_\varepsilon L^2X^\varepsilon.
\tag{175.B5}
\]

A consecutive interval of exact cardinality \(M\asymp L^2\) contains the
literal \(N\)-shell, and \(z_N\) is zero-extended on the full integer line.

## Stopped Fejer chain

Let \(R_0=\lceil L\rceil\) and define the minimal terminal index \(K\) by

\[
 R_{j+1}=\min(2R_j,M)\quad(0\le j<K),\qquad R_K=M.
\tag{175.B6}
\]

Thus the actual terminal link is retained: it is strict when
\(R_{K-1}<M<2R_{K-1}\) and is the exact final doubling when
\(M=2R_{K-1}\). Define

\[
 F_R(\theta)=\sum_{|r|<R}\left(1-\frac{|r|}{R}\right)e(r\theta),
 \qquad B_{R,S}=F_S-F_R.
\tag{175.B7}
\]

Choose a real \(\varphi\in C_c^\infty((-1/2,1/2))\), \(\varphi(0)=1\).
For \(\epsilon\in\{0,1\}\), put

\[
\begin{aligned}
 \mathcal W_\epsilon(x,y)
 &=\sum_{\substack{d,m\ge1\\d\ {\rm odd}}}
 (-1)^{\epsilon m}\lambda_{dm}(d)
 \varphi(x-d)\varphi(y-m),\\
 \mathcal B_{\epsilon,\theta}(x,y)
 &=\mathcal W_\epsilon(x,y)e(J\sqrt{xy}+\theta xy),\\
 \widetilde{\mathcal B}_{\epsilon,\theta}(\xi,\nu)
 &=\iint_{\mathbb R^2}\mathcal B_{\epsilon,\theta}(x,y)
 e(-\xi x-\nu y)\,dx\,dy,\\
 U_{k,\ell}^{(\epsilon)}(\theta)
 &=\widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell).
\end{aligned}
\tag{175.B8}
\]

For integers \(R<S\le2R\), define

\[
\begin{aligned}
 \mathcal N_{R,S}={1\over8}\Re\sum_{\epsilon=0}^1
 &\sum_{\substack{k,k'\in\mathbb Z\\k,k'\ {\rm odd}}}
 \sum_{\substack{\ell,\ell'\in\mathbb Z\\\ell,\ell'\ne0}}
 \chi_4(k)\chi_4(k')\\
 &\times\int_0^1B_{R,S}(\theta)
 U_{k,\ell}^{(\epsilon)}(\theta)
 \overline{U_{k',\ell'}^{(\epsilon)}(\theta)}\,d\theta .
\end{aligned}
\tag{175.B9}
\]

The constants \(i/2\) before squaring and \(1/8\) after parity averaging,
both absolute-parity branches, and the one outer real part are exact.

## Frozen target

Prove the deliberately one-sided estimate

\[
 \boxed{
 \sum_{j=0}^{K-1}\mathcal N_{R_j,R_{j+1}}
 \ll_\varepsilon L^3X^\varepsilon.}
\tag{175.B10}
\]

There is no absolute value around the whole chain. Linkwise absolute control
or an absolute bound for the full sum is sufficient but stronger.

The entire sector with \(\ell=0\) or \(\ell'=0\) is already target-safe
only after collective signed recombination over all odd character
frequencies. A separate short-shift correction is target-safe and is paid
exactly once. These pieces may be restored only in those complete forms.

## Required derivation and controls

Independently determine whether the whole scale sum in (175.B10) has a
non-tautological cancellation supplied by the actual
\(\omega_L\rho_NA_N\) symbol. Permitted ideas include an exact scale
martingale or Haar identity, a scale summation by parts, a selector or
squarefree correlation, a divisor involution, or a new joint transform, but
every claimed saving must precede any modulus over scale, frequency, cell,
opening, or endpoint.

A valid factor-\(L\) mechanism must fail for at least the following broader
controls:

1. arbitrary coefficients with the same support and energy;
2. phase-dechirped one-parity coefficients;
3. the constant-character shadow;
4. the erased-selector shadow \(\rho_N\equiv1\);
5. a one-site physical array; and
6. any model that leaves an isolated fixed dual diagonal.

The coefficient-insensitive positive capacity is \(L^4X^\varepsilon\).
This is a method-capacity statement, not a lower bound for the literal
coefficient. Both centred product-phase peaks may be rank one.

Retain every cardinal cell, arithmetic opening, endpoint, transition, hard
point value, support birth/death, zero-extension jump, parity branch,
ordinary frequency, and the strict final link. If the first proposed
mechanism returns to the original whole-chain aggregate or restores
\(L^4X^\varepsilon\), state the exact no-go and the surviving unexcluded
mechanisms.

Even a proof of (175.B10) closes only this K26 residual route and the
complete residual scalar. It has no direct implication to full \(t=1\),
complete hard TOP, BAL, UNBAL, M9--M2, M9, a bridge, the quarter theorem, or
an exponent.
