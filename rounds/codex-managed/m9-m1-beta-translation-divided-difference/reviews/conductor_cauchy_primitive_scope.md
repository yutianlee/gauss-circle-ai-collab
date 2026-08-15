# Conductor check: the independent diagonal regularizer is a signed Cauchy primitive

Campaign: `m9-m1-beta-translation-divided-difference`  
Role: finite-section ownership seam  
Allocation: analytical/algebraic only

The correct translation divided difference has no diagonal \(1/y\)
term. A different term nevertheless prevents an unqualified absolute
physical-height norm for the complete singular regularizer. With

\[
y=L-\nu,\qquad D(L,\nu)=A(L)+\frac{i}{2}(L-\nu),
\]

its diagonal component is

\[
K_C(L,\nu)=-\frac{iH(L,L)}{2A(L)D(L,\nu)}.       \tag{40.C3}
\]

On a finite physical-height section \(p<\nu<q\), direct integration
gives the exact oriented primitive

\[
\int_p^q K_C(L,\nu)\,d\nu
=-\frac{H(L,L)}{A(L)}
 \left\{
 \Log D(L,p)-\Log D(L,q)
 \right\}.                                      \tag{40.C4}
\]

For symmetric exhaustion \([-V,V]\), the signed logarithmic ratio is
bounded as \(V\to\infty\), with the branch fixed by the accepted
Plemelj orientation. By contrast,

\[
\int_{-V}^{V}|K_C(L,\nu)|\,d\nu
\asymp
\frac{|H(L,L)|}{|A(L)|}\log V                 \tag{40.C5}
\]

whenever the diagonal coefficient is nonzero. Thus a uniform absolute
\(L^1_\nu\) norm of the complete regularizer is false even though the
signed finite-section operator may converge.

For the separated height profile at a saddle \(|L|\asymp\lambda\),
the accepted decay gives \(H(L,L)=O_b(\lambda^{-3})\) and
\(A(L)\asymp\lambda\), so the coefficient in (40.C4) is
\(O_b(\lambda^{-4})\). This is quantitatively below the desired
\(\lambda^{-2}\) main symbol scale, provided its \(L\)-variation,
moving endpoints, and complete actual ownership retain the same decay.
Those complete-profile assertions remain to be proved by the round.

The lawful interface is therefore hybrid:

1. keep (40.C3) under its exact signed log primitive;
2. apply absolute or mixed-BV estimates only to the genuinely
   subtracted remainder, including the correct two-integral translation
   difference;
3. retain moving-face and branch-orientation terms explicitly.

This is separate from the previously analyzed top-pole face logarithm
and does not alter the exact identity in the companion conductor note.
No numerical experiment or external theorem is used.
