# Conductor support-separation observation

Campaign: `m9-m1-beta-axial-side-exhaustion`  
Role: conductor independent analytic check  
Allocation: 100% analytical/algebraic

The fixed transition mask from Round 26 is even, equals one on
\([-B, B]\), and is supported on \([-2B,2B]\). On a reflected radial
horizontal side, \(s=\sigma+it\) has \(t=\pm S\). With
\(u=a+i\mu\), \(v=b+i\nu\), the beta coordinate is

\[
 \beta=t-\frac{\mu+\nu}{2}.
\]

Throughout the original outside box \(|\mu|\le U\), \(|\nu|\le V\),

\[
 |\beta|\ge S-\frac{U+V}{2}.                     \tag{35.S1}
\]

Consequently, if

\[
 S>\frac{U+V}{2}+2B,                              \tag{35.S2}
\]

then \(\psi(\beta)=\psi'(\beta)=\psi''(\beta)=0\)
pointwise on the full radial-side product. The same inequality only
improves after restricting \(u=0\) (so \(\mu=0\)), \(v=0\), or both.
It also holds on every finite horizontal face of the \(u,v\) rectangles,
because those faces still satisfy \(|\mu|\le U\), \(|\nu|\le V\).

If the Round-34 two-axis operation is applied **to the beta-masked radial
side while the radial height remains fixed**, every one of its sixteen
strata therefore vanishes identically under (35.S2): pure boundary and
axis terms carry \(\psi\), first connectors carry \(\psi'\), and the
mixed product area carries \(\psi''\). This would make the Round-35
commutator zero by support, without using arbitrary-order \(R_M\) decay.

This observation is deliberately not yet a proof-state claim. Three scope
questions require independent validation:

1. whether the beta mask in the actual radial-side stratum uses reflected
   \(t=\pm S\) with precisely the same sign convention;
2. whether either outside-axis transfer changes the radial height or only
   moves \(u,v\), as assumed above;
3. whether the global boundary-first order leaves a beta-masked radial
   side to which this support argument applies, rather than an unmasked
   side whose removal must first be taken globally.

If all three pass, the side-exhaustion commutator is stronger than expected:
it is eventually exactly zero for every fixed \(M\), and the arbitrary-M
power table is needed only for the unmasked/global side module, already
covered by the accepted Round-21 lemma. If the third fails, support
separation cannot be used to commute localization with side removal, and
the original sixteen-stratum decay audit remains necessary.
