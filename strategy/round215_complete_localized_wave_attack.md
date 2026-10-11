# Round215 frozen strategy: complete localized lattice-wave moment

Date:2026-09-28. Campaign:gc-complete-localized-wave-moment.
Graph SHA256:4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
Previous goal turn:progress, verified by closed214 and its26-file archive.
Full target remains P(X)<<X^(1/4+epsilon). Next mandatory review217.

## 1. One frozen objective

Prove or rigorously delimit the complete weighted localized wave estimate
selected in214. A formal transform or unestimated new remainder is not
a positive estimate. Use T>=2 and every T^(166/325)<N<T^(242/325),
I=[T/sqrt(2),sqrt(3)T]. Put a=1/sqrt(2), d=sqrt(3)-a,
J=ceil(dT/sqrt(N)), R_j=aT+j sqrt(N), 0<=j<=J. These centers and
their central windows coverI. Finite changes in end windows cost constants.

Let v>=0 be a fixed nonzero smooth dyadic partition mask supported in[1,4].
Psi is the fixed real radial mollifier transform, Psi(0)=1. Define exactly

    F_N(x,R)=sum_(m in Z^2, m!=0) c_m e(x.m+R|m|),
    c_m=|m|^(-3/2)Psi(|m|/sqrt(T))v(|m|^2/N).

This is the actual lattice lift: F_N(0,R) is precisely the complex r2
block, with every norm multiplicity retained. Throughout this band
N/T tends to0 by a fixed power, so c_m>=0 for sufficiently largeT;
boundedT is paid by constants. Do not replace these coefficients by
arbitrary phases, or choose a different phase for each radius window.

Fix once real Schwartz functions phi:R^2->R and eta:R->R with small
compact Fourier support, phi(0)=eta(0)=1, both bounded below in modulus
on the required fixed central cubes. Such inverse-bump functions exist
after a fixed dilation. Use this product cutoff, a permitted specialization
of214's chi. Let W(y)=C_A(1+|y|^2)^(-A), with fixedA=100 and C_A>0
large enough for the fixed-bandwidth reproducing inequality. Set

    f_j(y,u)=phi(y/N)eta(u/N)
             F_N(y/sqrt(N),R_j+u/sqrt(N)),
    C(T,N)=sum_(j=0)^J integral_(R^3) W(y)|f_j(y,u)|^10 dydu.

Frozen target:

    C(T,N)<<_epsilon T^(83/65+epsilon).                    (C215)

Every window, real endpoint, lattice direction, integer norm, aligned or
narrow packet and full Schwartz tail belongs toC. Fixed spatial bandwidth
and du=sqrt(N)dR imply the complete physical tenth gate from(C215).
Its already costed reconstruction gives102/325 only. Quarter still needs
the corresponding full moment familyE(p)=1+o(p), or another complete route.

## 2. Three bounded orthogonal tasks

1. weighted_envelope_transfer: derive and quantitatively test a legal
   amplitude-dependent cone-envelope bound for this weighted tube mass.
   Inspect the primary Guth--Maldague amplitude-dependent theorem and its
   envelope definitions; no free replacement of Lebesgue measure byW.
   Preserve all threshold, packet, trace, localization, window and tail
   costs. Produce a concrete complete sufficient envelope inequality and
   the strongest justified cost, or a precise source/analytic obstruction.
   Do not repeat the already priced generic Theorem3 small-cap calculation.
2. actual_lattice_envelopes: analytically attack(C215) on the actual
   coefficients. Preserve the common modulation across radius windows,
   all directions including rational/aligned ones, and signed radial
   phases. Try an actual coefficient-sensitive envelope or arithmetic
   estimate, not an arbitrary-array norm or density heuristic. A useful
   negative result must delimit an explicitly stated complete certificate
   or prove a genuine actual obstruction. Any transformed remainder and
   its full power must be displayed. At most one promising source import.
3. blind_spatial_kernel: independently derive the isolated spatial-weight
   and radius-window kernel packet. It contains only explicit definitions
   and generic mass hypotheses, not prior conclusions or source arguments.
   No graph, manifest, strategy, other report or web. Test exact tenth
   expansion, both orders of taking modulus and their power implications,
   with certificate lower bounds kept distinct from the signed moment.

The conductor verifies actual coefficient mass, compares the analytic
and arithmetic interfaces, monitors drift and independently checks the
kernel/normalization seams. No216 task begins before215 closes.

## 3. Inherited barriers and controls

Closed214's legal generic small-cap/trace estimate is
M_p(H_N)<<T^epsilon[TN^(1-p/4)+TN^(p/4-1)]. It does not pay the tenth
gate; changing symbols or omitting trace/window costs is forbidden.
The source's amplitude-dependent estimate is not automatically weighted.
The radius Q_q input remains open and its positive certificate stops at
5/16 even if extended and proved. Earlier scalar/periodic centering and
positive Fourier certificates have scoped obstructions. Actual signed
cancellation, all full M1/M2/GAR parents and endpoints remain open.

Required controls: exactr2 lift; fixed actual modulation; spatial weight
and Fourier normalization; all real windows/Schwartz tails; narrow and
aligned directions; complete coefficient and cap norms; source hypotheses;
restored powers; actual versus arbitrary controls; certificate versus signed
lower bounds; full-quarter distinction. At least one important lemma is
independently derived statement-only. Required final-hash seams are analytic
weighted transfer, actual arithmetic/certificate scope and conductor kernel.

## 4. Budget and exit gates

At least95 percent analysis/algebra/source work; at most5 percent numerical
experimentation; plannedzero experiments. Three bounded seven-section
reports, one same-round seam cycle, and a bounded conductor synthesis.
The analytic task may audit one source interface, the arithmetic task at
most one new import; no broad literature review is due until217.

Exit only after three reports or explicit task termination, independent
seams, complete power comparison and validated State Patch. Promote only
mathematics that meets all graph requirements. A rigorous certificate
failure is useful evidence but never a lower bound on the Gauss error.
