# Conductor candidate: target-safe artificial residue after alpha localization

Campaign: `m9-m1-beta-compact-selector-ownership`  
Role: conductor seam analysis for the replacement architecture  
Status: candidate for the next round, not accepted mathematics  
Allocation: 100% analytical/algebraic

## Exact radial coefficient

At the artificial pole \(\rho=0\), Round 38 retains

\[
 \operatorname{Res}_s R_{1,v}(1-s)=\pi i\sqrt X\,I_1(0),
 \qquad
 I_1(0)=\int_1^{N_X}x^{-1/2}e(\sqrt{Xx})\,dx.
\]

The substitution \(y=\sqrt x\) evaluates this coefficient exactly:

\[
 \boxed{
 \pi i\sqrt X\,I_1(0)
 =e(\sqrt{XN_X})-e(\sqrt X).}                     \tag{44.C4}
\]

Hence its absolute value is at most two.  The unrestricted \(O_X(1)\)
constant used for the Round-38 existence theorem is unnecessary on this
residue.

## Residue geometry

On \(\rho=0\), one has

\[
 s=\frac14-\frac v2,\qquad
 \beta_\rho=-\frac\mu2-\nu,\qquad
 \alpha_\rho=\frac\mu2.                            \tag{44.C5}
\]

The completed arithmetic factor is kept recombined as

\[
 \zeta\!\left(\frac34+\frac u2+v\right)
 L\!\left(\frac34-\frac u2,\chi_4\right),          \tag{44.C6}
\]

not expanded as a termwise \(h,q\) series.

For the central share, compact \(\alpha_\rho\) bounds \(\mu\), and
compact \(\beta_\rho\) then bounds \(\nu\).  Equation (44.C4), compact
gamma/arithmetic factors away from their poles, and the actual scale
weights therefore leave only a polylogarithmic scale/profile cost.

For the complementary share, compact beta support gives
\(\nu=-\mu/2+O(1)\).  The hard top contributes \(1/\mu\) away from its
already separated delta term, the height profile contributes
\(O_b((1+|\mu|)^{-3})\), and the accepted period-four partial-summation
bound gives

\[
 L(3/4-a/2-i\mu/2,\chi_4)\ll_a1+|\mu|.
\]

Thus the large-height residue density is integrable with
polylogarithmic constants.  Smooth spatial shares are stronger because
their Mellin profiles decay rapidly in \(\mu\).

## Required next-round checks

Before promotion, a fresh proof must verify the Plemelj subtraction near
\(\mu=0\), choose the actual \(a,b\) lines with a uniform gap from the
zeta pole, retain all contour constants and selectors, and show that the
dyadic scale sum is \(O(\log^C X)\).  It must also match this residue to
the accepted one-count axial/artificial ledger.  If these checks pass,
the whole artificial coefficient—not merely its central part—is
physically \(O_\varepsilon(X^{1/4+\varepsilon})\) after restoring the
external factor.

No numerical experiment or external theorem was used.
