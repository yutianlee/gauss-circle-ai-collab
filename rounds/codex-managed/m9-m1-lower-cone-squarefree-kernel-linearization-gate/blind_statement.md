# Round 145 statement-only problem

Let \(X\ge2\), \(R=X^{1/4}\), \(N=\lfloor X\rfloor\), and let
\(V_{\rm low}\) be a fixed smooth compactly supported lower profile.  On
disjoint half-open dyadic blocks \(\mathcal I_M\subset[1,O(R^2)]\), put

\[
C(m)=\sum_{\substack{hr=m\\r\ {\rm odd}\\r>4h}}\chi_4(r),\qquad
k_m=\left\lfloor\sqrt{Nm}+\frac12\right\rfloor,
\qquad j_m=k_m^2-Nm.
\]

The exact frozen scalar is

\[
T_N=
\sum_M\sum_{\substack{m\in\mathcal I_M\\|j_m|>M^{3/4}}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm}),
\]

and the desired bound is

\[
T_N\ll_{\varepsilon,V}X^\varepsilon
\]

uniformly for every real \(X\).

Independently write every \(m\) in its unique squarefree-kernel form
\(m=s t^2\).  Derive the exact resulting formula for \(C(s t^2)\),
including every parity, character, cone, common-factor, and multiplicity
condition.  Decide whether the phase \(e(t\sqrt{Ns})\) gives the target or
a strict owner-complete reduction.  Any removed complement must be proved
target-safe with the literal block endpoints, profile, mask, exact
radicals, and terminal truncation.

You must test \(t=1\), bounded \(t\), large square parts, even parameters,
the exact squarefree kernel of \(N\), and Pell or continued-fraction near
resonances.  Retain the individual positive complex direction and fixed
centre.  Do not use a cosine, random-sign model, average over centres,
complete-divisor replacement, or formal transform as a substitute.

Return a seven-section report containing an exact result or no-go,
hypotheses, proof, first unproved step, controls, dependencies, and proposed
state effect.  Write only the assigned report; do not edit shared state.

