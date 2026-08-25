# Round 142 synthesis: exact rational spectrum, no owner-complete major-arc reduction

Campaign: m9-m1-lower-cone-rational-additive-spectrum-gate

Starting graph SHA-256:
de02111a1831d30da33c9f4b2d4a549efa1942dcdc32b5d829e671f6ad5e0e76

## Decision

Close under
\(\mathsf{rational\_major\_arc\_self\_return\_no\_go}\).
For

\[
C(m)=\sum_{\substack{hr=m,\ r\ {\rm odd}\\r>4h}}\chi_4(r),
\]

every reduced \(a/q\) satisfies the uniform theorem

\[
\boxed{
\sum_{m\le M}C(m)e(am/q)
=\mathbf1_{4\mid q}{i\pi\chi_4(a)\over2q}M
+O((\sqrt M+q)\log(2q)).}
\tag{142.S1}
\]

The target fixed-centre nonresonant cone estimate is not proved.

## Positive progress

The quarter mode is now understood as one member of the complete
rational hierarchy: a nonzero mean occurs exactly when the reduced
denominator is divisible by four.  The two resonant height classes,
their signs, both strict cone endpoints, and the growing-denominator
error are exact.  Partial summation gives

\[
\sum_{m\le M}m^{-3/4}C(m)e(am/q)
=\mathbf1_{4\mid q}{2i\pi\chi_4(a)\over q}M^{1/4}
+O(q\log(2q)+1).
\tag{142.S2}
\]

For each height,

\[
\mathbf1_{h\mid m}\chi_4(m/h)
=-{i\over2h}\sum_{\substack{b\ ({\rm mod}\ 4h)\\b\ {\rm odd}}}
\chi_4(b)e(bm/(4h)),
\tag{142.S3}
\]

so the cone has an exact finite, moving rational expansion.

## Exact reconstruction obstructions

A finite projection through denominator \(Q\) leaves the same linear
mean at every omitted denominator.  The limiting coefficient masses are

\[
\sum_{q\le Q}\sum_a|A(a/q)|\asymp Q,
\qquad
\sum_{q\le Q}\sum_a|A(a/q)|^2\asymp\log Q,
\tag{142.S4}
\]

so the natural cutoffs are neither absolutely nor mean-square Cauchy.
The exact twisted Gauss sum and Möbius inversion show that the hard
cutoff is

\[
P_Q(m)={\pi\over4}\sum_{\ell\mid m}\chi_4(m/\ell)
\sum_{\substack{k\le Q/(4\ell)\\k\ {\rm odd}}}
{\mu(k)\chi_4(k)\over k}.
\tag{142.S5}
\]

With complete numerator sets grouped before denominator-Abel damping,

\[
P_\eta(m)={\pi\over4L(1+\eta,\chi_4)}
\sum_{\ell\mid m}\chi_4(m/\ell)\ell^{-\eta}
\longrightarrow {r_2(m)\over4}.
\tag{142.S6}
\]

Thus the canonical completion reconstructs the complete radial
coefficient, not \(C\).  On odd-part character \(-1\), the complete
coefficient is zero, so the cone residual remains exactly \(C\).

Freezing the height cutoff over \([M,2M)\) also leaves a moving wedge
with unsigned weighted incidence \(\asymp M^{1/4}\), hence
\(R^{1/2}\) at the top scale.  This is capacity only, not a signed
lower bound.

## Local slope and transform status

The curvature length and derivative range are

\[
L_M\asymp{M^{3/4}\over R},
\qquad K_M\asymp{R^2\over\sqrt M}.
\tag{142.S7}
\]

Farey arcs of order \(L_M\) cover the slopes with raw overlap
\(O(L_M)\).  Absolute cell assembly requires the residual norm

\[
\max_{q\le L_M,\ |J|\le L_M}
\left|\sum_{m\in J}D(m)e(am/q)\right|
\ll_\varepsilon X^\varepsilon{\sqrt M\over R},
\tag{142.S8}
\]

whereas (142.S1) supplies a \(\sqrt M\)-scale prefix error.  Below
\(M\asymp R^{4/3}\), the cells are singletons.  The accepted
condition \(|k_m^2-Nm|>\sqrt M\) controls phase values and gives only
microscopic derivative separation; it does not exclude these arcs.

A rigorous coefficient-free branch bound is

\[
\ll\min\{M^{1/4},RM^{-1/2}+R^{-1}\},
\tag{142.S9}
\]

but the full denominator mass remains owner-sized.  At the stationary
principal level, the first saddle has reciprocal phase \(Nh/z\),
amplitude \(2N^{-1/4}\), and Gaussian unit \(e(-1/8)\); the matching
second saddle reproduces the original square-root phase, character,
amplitude, and strict-cone inequality.  This is principal-symbol
self-return only.  Branchwise remainders, hard endpoints, and Fresnel
transitions are not inherited from the reassembled Round-140 ledger.

The repaired source audit confirms that the cited Jutila theorem has a
holomorphic-amplitude hypothesis and does not cover arbitrary nonzero
compactly supported smooth weights.  Kaneko and Banerjee--Khurana use
complete coefficients and exclude the needed boundary parameters.
No audited source closes (142.S8) or the frozen complex scalar.

## Remaining gap and proof status

The first open estimate remains

\[
\sum_M\sum_{\substack{m\in\mathcal I_M\\|k_m^2-Nm|>\sqrt M}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
\ll_\varepsilon X^\varepsilon.
\tag{142.S10}
\]

Round 142 adds an exact rational-spectrum theorem and a rigorous
mechanism obstruction, but no strict survivor and no target bound.
Lower GAR, both direct M1 parents, M9-M1, hard TOP, BAL, all required
UNBAL owners, M9-M2, endpoint uniformity, M9, the conditional bridge,
and the quarter theorem remain open.

The strongest internally proved exponent remains \(1/3\).  The
separately audited external Li--Yang exponent remains

\[
{3292+25\sqrt{1717}\over13762}
=0.3144831759740614\ldots.
\]

Round 142 proves no exponent improvement.

Resulting graph SHA-256:
7a3ff68dda20717bff1133412f0ca97d35032599930d7f19551109a43d2bd789
