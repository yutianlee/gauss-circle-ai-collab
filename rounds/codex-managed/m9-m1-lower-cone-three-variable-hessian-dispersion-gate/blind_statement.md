# Statement-only Round 146 problem

Let \(R=X^{1/4}\), \(N=\lfloor X\rfloor\), and let
\(\mathcal I_M=\mathbb N\cap[M,B_M)\), \(B_M\le2M\), be disjoint
half-open blocks with \(M\ll R^2\). Define

\[
C(m)=\sum_{\substack{hr=m\\r\ {\rm odd}\\r>4h}}\chi_4(r),\qquad
k_{s,t}=\left\lfloor t\sqrt{Ns}+\frac12\right\rfloor.
\]

You may take as the exact starting scalar

\[
\sum_M\sum_{1\le t<M^{1/4}}
\sum_{\substack{s\ {\rm squarefree}\\st^2\in\mathcal I_M\\
|k_{s,t}^2-Nst^2|>M^{3/4}}}
(st^2)^{-3/4}V_{\rm low}(R^2st^2/N)
C(st^2)e(t\sqrt{Ns}).
\]

The retained support satisfies \(s>M^{1/2}\). The desired bound is
\(O_{\varepsilon,V}(X^\varepsilon)\), uniformly for real \(X\).

One exact coefficient formula is

\[
C(st^2)=
\sum_{\substack{\gamma\mid t\\\gamma\ {\rm squarefree}\\
(\gamma,s)=1\\\gamma\ {\rm odd}}}\chi_4(\gamma)
\sum_{\substack{de=s\\e\ {\rm odd}}}\chi_4(e)
\sum_{\substack{ab=t/\gamma\\b\ {\rm odd}\\eb^2>4da^2}}1.
\]

Thus on \(de=s\) the phase is
\(f(t,d,e)=\sqrt N\,t\sqrt{de}\). Independently verify its complete
three-variable Hessian and decide whether a lawful multidimensional
estimate proves the target or makes a strict intermediate-\(t\) range
target-safe.

Retain the exact coefficient multiplicity, squarefree and coprimality
conditions, parity, character, strict cone, profile, terminal endpoints,
and nearest-square mask. Check every aspect ratio, especially
\(t=1\), bounded \(t\), \(D=1\), \(E=1\), and
\(T\) near \(M^{1/4}\). Also check exact radicals and the family
\(N=sL^2+1\), where surviving phases can rotate slowly. A nonzero
Hessian without a theorem whose coefficient and box hypotheses apply is
not a bound; an upper capacity is not a signed lower bound.

Return a seven-section report with a proof, strict owner-complete
reduction, or exact no-go. Do not consult claimant artifacts, strategy
files, the proof graph, or sibling reports.
