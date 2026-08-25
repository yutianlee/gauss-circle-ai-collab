# Round 144 statement-only problem: automorphy of a one-sided divisor cone

Use \(e(t)=e^{2\pi i t}\), and let \(\chi _4\) be the primitive odd
character modulo \(4\).  For \(\tau\) in the upper half-plane define

\[
F(\tau)=
\sum_{\substack{h\ge1,\ r>4h\\r\ {\rm odd}}}
\chi _4(r)e(hr\tau)
=\sum_{m\ge1}C(m)e(m\tau),
\qquad
C(m)=
\sum_{\substack{hr=m,\ r\ {\rm odd}\\r>4h}}\chi _4(r).
\tag{144.B1}
\]

Independently determine the exact automorphic status of \(F\).  In
particular:

1. realize \(hr\) as an integral signature-\((1,1)\) quadratic form and
   write the strict cone \(h>0,\ r>4h\), the odd-\(r\) restriction, and
   \(\chi _4(r)\) as an exact lattice/coset/kernel expression;
2. decide whether \(F\) itself is modular, mixed mock modular,
   indefinite theta, false/partial theta, quantum modular, or only the
   holomorphic part of a completion;
3. if a completion exists, derive every nonholomorphic, isotropic-boundary,
   opposite-cone, unary, residue, or cusp term, together with its weight,
   level, multiplier, transformation law, and growth;
4. derive the strongest lawful summation formula for the coefficients
   \(C(m)\), keeping an individual complex direction rather than replacing
   it by an unaudited real or conjugate combination.

The analytic application is the fixed-centre scalar

\[
\mathfrak T_N=
\sum_M\sum_{\substack{m\in[M,2M)\cap[1,M_*]\\
|k_m^2-Nm|>\sqrt M}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm}),
\tag{144.B2}
\]

where

\[
R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
k_m=\left\lfloor\sqrt{Nm}+\frac12\right\rfloor,\qquad
M_*\asymp R^2,
\tag{144.B3}
\]

and \(V_{\rm low}\) is a fixed smooth compactly supported real profile.
The target is

\[
\mathfrak T_N\ll_{\varepsilon,V}X^\varepsilon
\tag{144.B4}
\]

uniformly for every real \(X\).

An automorphic name or formal transformation is not enough.  Price the
completion, the hard nonresonant mask, every dyadic endpoint, the
individual complex direction, and the complete \(R,M,N\) capacity.
Either prove (144.B4), reduce it to a strictly smaller owner-complete
signed survivor, or identify the first exact obstruction.

Return a seven-section report:

1. Result: lemma or no-go result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required control tests and outcomes.
6. Dependencies and exact artifacts used.
7. Recommended state effect.

