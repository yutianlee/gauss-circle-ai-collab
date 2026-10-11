# A signed sixfold-convolution interface for the next analytic decision

Round202 conductor candidate, 2026-09-23. Starting graph hash:
682cb189a3ab0ef26f8d19701e2949547446d37505df01f7b7eaf1cfdd0f359c.
Context: closed Round201 full source and accepted exact kernel; current
Round202 majorant calculation. This is an exact reformulation, not an
analytic saving or a promoted theorem. It is considered for strategy
only after the current source and tail audits are reconciled.

## Exact physical measure and identity

Choose once a real chi in C_c^infinity((0,infinity)), nonnegative and
equal to one on [1/sqrt(2),sqrt(3)], and take w=chi^2. This is an
admissible fixed window. For any real cutoff U>=1 put

\[
 \mu_{T,>U}=\frac12\sum_{n>U}a_n(T)
   \{e(-3/8)\delta_{\sqrt n}+e(3/8)\delta_{-\sqrt n}\},
 \quad \nu_{T,U}=\mu_{T,>U}^{*6},
 \quad K_T(\xi)=T\widehat\chi(T\xi).
\]

All measures have finite total variation at fixed T because of the
actual Schwartz cutoff, and K_T is Schwartz. With the Fourier
convention of Round201, the inverse Fourier transform of mu is the
real cosine tail H_(T,>U). Plancherel therefore gives the exact identity

\[
 \int\chi(R/T)^2|H_{T,>U}(R)|^{12}dR
       =\|K_T*\nu_{T,U}\|_{L^2(\mathbb R)}^2.                \tag{C1}
\]

This retains all sixfold sign choices inside nu, all cross terms
after the L2 norm, and the complete tail n>U. No band has been
discarded, no independent squarefree phases substituted, and no
modulus has been inserted inside the convolution.

Since chi vanishes on a neighborhood of zero, for every j>=0
integral xi^j K_T(xi)dxi is a constant multiple of T^(-j)chi^(j)(0)=0.
Thus this filter annihilates polynomials in the frequency variable
when convolution is defined, and suppresses a smoothly varying bulk.
It is complex and oscillatory. Replacing K_T or nu by its total
variation discards exactly the cancellation at issue.

## Complete power target and limitations

If an independently proved low-head estimate gives
integral w|H_(T,<=U)|^12<<T^(1+epsilon), the full moment target is
equivalent at exponent level, by the two directions of the L12 triangle
inequality, to

\[
 \boxed{\|K_T*\nu_{T,U}\|_2
 \ll T^{1/2+\eta+\epsilon},\qquad
 0\le\eta<13\theta_{LY}-4.}                                  \tag{C2}
\]

This also controls all mixed head/tail terms by Holder; no individual
mixed stratum is silently removed. The permissible choice U=T^u and
its low-head proof must come from the reviewed cutoff task, not an
assumption. Restoring the disk amplitude and Jacobian gives
Y^(4+eta+epsilon), and persistence gives exponent (4+eta)/13.

C1 alone is not progress on C2. A prospective argument must produce
a coefficient-sensitive approximation or cancellation estimate for
the actual signed sixfold measure at frequency resolution 1/T, with
its full L2 cost. A smooth bulk subtraction is legitimate only with
an explicit remainder theorem; area counting of single r_2 weights
does not establish such a theorem for their sixfold convolution.
Continuous-frequency models with large zero-radius peaks and tiny
displaced moments are controls, not approximation theorems.

The interface keeps the object complete and exposes the oscillatory
filter that the physical majorant obstruction shows cannot be erased.
It offers a concrete place to test Fourier, additive-correlation, and
arithmetic pushforward methods, while making their first unproved
estimate explicit. No existing source found so far supplies C2.
