# Round 158 conductor adjudication

- Campaign: m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate
- Round: 158
- Starting graph: 3acbfaf6fb95047babd19800dee4152fb60cb408197a8ceac93931a20c57491f
- Terminal label: paired_interior_cell_trace_no_go
- Allocation: 100% analytical, algebraic, and primary-source work; 0% numerical

## 1. Result

Round 158 closes under **paired_interior_cell_trace_no_go**, strictly
in the route-scoped sense.  It proves the exact moving-mask Abel-trace
reduction, not the trace target and not the full paired interior
matrix.

The accepted narrow package is:

1. positive-prefix and negative-suffix Abel summation put the moving
   atom in with a positive sign on both signed blocks and expose the
   two different outer endpoints and both profile-bulk remainders;
2. full half-period inversion gives the physical prefix/suffix trace
   with exact all-odd-divisor normalization;
3. the individual zero and Nyquist **trace pieces**, proved directly
   rather than transferred from their whole rows, are each
   \(O_\varepsilon(M^{-1/4}X^\varepsilon)\);
4. the full-frequency endpoint face is target-safe by a complete
   prime-power root table; and
5. the remaining paired-interior trace is exactly the literal strict
   boundary-frozen selected sum, up to the stronger error above.

The strict sum is not proved target-sized.  Its scalar target is
\(O_\varepsilon(X^\varepsilon)\), equivalently raw
\(M^{3/4}X^\varepsilon\) after removing the atom scale.  Endpoint
roots, support cardinality, top-block localization, ordinary
\(\chi_4\)-Abel summation, the named standard discrepancy/completion
placements, and the audited primary sources do not supply that bound.
These are exact reductions, method capacities, and a cutoff-dated
source no-match; they are not a signed lower bound or a universal
impossibility theorem.

## 2. Exact accepted statement and hypotheses

Fix

\[
 q=4N,\qquad K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\le K,\qquad M\le N^{1/2},
\]

and, for every odd \(d\mid N\), put

\[
 c=q/d,\qquad H=c/2,\qquad n=H/2=N/d.
\tag{158.A1}
\]

On the exact positive and negative blocks retain

\[
 B_j(x)=\mathbf 1_{x\ge\lambda_\sigma(j)}F_j(x),
 \qquad\lambda_+(j)=j+1,qquad\lambda_-(j)=-j,
\tag{158.A2}
\]

with the literal zero-extended profile, complex residual phase,
asymmetric cell, transitions, half-open choices, and hard endpoints.
For

\[
 P^+_{d,v}(j)=\sum_{s=a_+}^{j}K(-v^2,-s;c),\qquad
 P^-_{d,v}(j)=\sum_{s=j}^{b_-}K(-v^2,-s;c),
\tag{158.A3}
\]

the isolated moving trace is exactly

\[
\begin{aligned}
 \mathcal C_{\mathrm{int},U}(V)
 ={}&-\frac{i(1+i)}{2Nq}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}\chi_4(d)d\sqrt c
 \bigg[\\
 &\sum_{j=a_+}^{b_+-1}F_j(j+1)
 \sum_{\substack{v\bmod H\\v\ne0,n}}
 e_c(-2v(j+1))P^+_{d,v}(j)\\
 &+\sum_{j=a_-+1}^{b_-}F_j(-j)
 \sum_{\substack{v\bmod H\\v\ne0,n}}
 e_c(2vj)P^-_{d,v}(j)\bigg].
\end{aligned}
\tag{158.A4}
\]

The positive outer term is
\(A_{b_+}(v)P^+_{d,v}(b_+)\); the negative outer term is
\(A_{a_-}(v)P^-_{d,v}(a_-)\).  Both and the two profile-bulk
remainders are printed in the accepted kernel but quarantined from
(158.A4).

Full-frequency inversion gives

\[
\begin{aligned}
 \mathcal C_+^{\mathrm{full}}
 &=\sum_{j=a_+}^{b_+-1}F_j(j+1)
   \sum_{s=a_+}^{j}G_N((j+1)^2-s),\\
 \mathcal C_-^{\mathrm{full}}
 &=\sum_{j=a_-+1}^{b_-}F_j(-j)
   \sum_{s=j}^{b_-}G_N(j^2-s),
\end{aligned}
\tag{158.A5}
\]

where \(G_N(t)=\mathbf 1_{N\mid t}\chi_4(t/N)\), and

\[
 \mathcal C_{\mathrm{int},U}
 =\mathcal C_+^{\mathrm{full}}+\mathcal C_-^{\mathrm{full}}
  -\mathcal Z_{\mathrm{tr}}-\mathcal F_{\mathrm{tr}}.
\tag{158.A6}
\]

For

\[
 \kappa(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,
 \qquad r(\ell)=\kappa(\ell)^2-N\ell,
\tag{158.A7}
\]

the exact strict selectors are

\[
\begin{aligned}
 \eta_+(\ell)&=
 \mathbf 1_{a_++1\le\kappa(\ell)\le b_+}
 \mathbf 1_{a_+\le r(\ell)\le\kappa(\ell)-2},\\
 \eta_-(\ell)&=
 \mathbf 1_{-b_-\le\kappa(\ell)\le-a_--1}
 \mathbf 1_{-\kappa(\ell)+1\le r(\ell)\le b_-}.
\end{aligned}
\tag{158.A8}
\]

Their literal weights are

\[
\begin{aligned}
 W_+(k)&=w_U\!\left(\frac{k^2-k+1}{N}\right)
 e(\sqrt{k^2-k+1}-k),\\
 W_-(k)&=w_U\!\left(\frac{k^2+k}{N}\right)
 e(\sqrt{k^2+k}-k).
\end{aligned}
\tag{158.A9}
\]

Thus

\[
\boxed{
 \mathcal C_{\mathrm{int},U}(V)
 =\sum_{\ell\ge1}\chi_4(\ell)
 \left[\eta_+(\ell)W_+(\kappa(\ell))
      +\eta_-(\ell)W_-(\kappa(\ell))\right]
 +O_\varepsilon(M^{-1/4}X^\varepsilon).}
\tag{158.A10}
\]

The profile arguments in (158.A9) are not the quotient \(\ell\).
They lie on opposite sides of it in strict terms.

## 3. Proof and evidence adjudication

The Abel signs, endpoints, and full-frequency normalization were
independently rederived.  The accepted inverse identity is

\[
 \sum_{v\bmod H}e_c(-2vx)K(-v^2,-s;c)
 =\frac{1-i}{2}\sqrt c
 \sum_{u\bmod c}^{*}\chi_4(u)e_c(u(x^2-s)),
\tag{158.A11}
\]

and the exterior constant is fixed by

\[
 -\frac{i(1+i)}{2Nq}\frac{1-i}{2}dc=-\frac{i}{2N}.
\tag{158.A12}
\]

The blind report's normalization doubt is therefore resolved by the
accepted Round 157 kernel.  Its conditional standard-Kloosterman/Weil
argument is not promoted.  Instead, opening the actual theta kernel
gives for every fixed trace frequency

\[
 \sup_I\left|\sum_{s\in I}K(-v^2,-s;c)\right|
 \ll c\log(2c),
\tag{158.A13}
\]

and restoration of all factors proves separately

\[
 |\mathcal Z_{\mathrm{tr}}|+|\mathcal F_{\mathrm{tr}}|
 \ll_\varepsilon M^{-1/4}X^\varepsilon.
\tag{158.A14}
\]

The endpoint polynomials are \(j^2+j+1\) and \(j(j-1)\).  The second
has exactly two roots modulo every prime power.  The first has no
\(2\)-adic root, one root modulo \(3\) and none modulo \(3^\nu\) for
\(\nu\ge2\), and two simple roots at every \(p^\nu\) precisely for
\(p\ne2,3\) with \(p\equiv1\pmod3\).  Hence the endpoint row has
only \(O_\varepsilon(N^\varepsilon)\) atoms and is target-safe.

The nearest-cell intervals partition the positive integers, giving

\[
 L_{\mathrm{str}}(V)
 \ll_\varepsilon\min(M,V)X^\varepsilon.
\tag{158.A15}
\]

Literal boundary support forces a nonzero moving trace to have
\(V\asymp K\).  In that range \(V\gg M\), so (158.A15) can still be
\(O(MX^\varepsilon)\).  With atom size
\(M^{-3/4}X^\varepsilon\), absolute capacity is
\(M^{1/4}X^\varepsilon\), a factor \(M^{1/4}\) above the scalar
target.

The explicit dyadic family in the conductor survivor audit gives a
strict arithmetic selected point whose endpoint polynomial is
nonresonant.  It is retained only as a survivor control, conditional
on the literal component being nonzero at its boundary argument; it is
not a lower bound.

The independent trace-mathematics and hostile profile/power reviews
are GREEN for the narrow package.  The blind report is retained after
reconciliation only for its independently valid finite algebra and
endpoint controls.  The source report is retained after repairing its
residual-phase wording: the boundary residual phase remains
\(k\)-dependent inside the coefficient and is not an exact fixed
Fourier-frequency shift.

The independent source review confirms the source-favorable masked
exponent-pair ledger.  For the audited transformed pair

\[
 (\kappa_0,\lambda_0)=\left(\frac{195}{796},\frac{235}{398}\right),
\]

the favorable fixed-endpoint/unit-BV model needs

\[
 M^{703}\ge N^{390},\qquad M\ge N^{390/703}>N^{1/2}.
\tag{158.A16}
\]

Müllner completion needs \(M\ge N^{2/3}\).  No audited primary
theorem through 25 August 2026 accepts the literal root-indexed
coefficient, both moving strict selectors, arbitrary even composite
modulus, quotient sign, and restored target.  This is a dated
direct-interface no-match only.

## 4. First doubtful or unproved step

There is no unproved step in the promoted finite algebra, direct
special-frequency trace estimates, endpoint table, exact strict
rewrite, support-zero localization, or target calibration under the
printed hypotheses.

The first open trace estimate is

\[
 \left|\sum_{\ell\ge1}\chi_4(\ell)
 \left[\eta_+(\ell)W_+(\kappa(\ell))
      +\eta_-(\ell)W_-(\kappa(\ell))\right]\right|
 \ll_\varepsilon X^\varepsilon.
\tag{158.A17}
\]

Equivalently, after dividing by the atom scale, one needs raw
\(M^{3/4}X^\varepsilon\).  A raw square-root estimate would be
stronger than necessary.  The literal root-indexed coefficient and
moving sharp selector are the first source interface mismatch.

The two Abel outer terms and both profile-bulk remainders are separate
open seams.  Even a proof of (158.A17) would not by itself close the
full paired matrix.

## 5. Required controls and outcomes

- literal paired-interior trace: GREEN for the isolated moving term;
- positive-prefix and negative-suffix signs: GREEN;
- all Abel outer endpoints: GREEN as exact quarantined identities;
- full-frequency delta inversion: GREEN, including \(c=4\);
- zero and Nyquist trace pieces: GREEN by direct interval summation;
- endpoint prime-power table: GREEN, including \(p=2,3\);
- strict survivor and endpoint deletion: GREEN as identities only;
- selected quotient versus boundary profile: GREEN and kept distinct;
- positive/negative profiles, phases, and endpoints: GREEN and not
  paired artificially;
- support localization: GREEN as a zero range only, not a target;
- \(N,M,V,d,c\) powers: GREEN with scalar target
  \(O_\varepsilon(X^\varepsilon)\) and raw threshold \(M^{3/4}\);
- standard discrepancy, completion, and exponent-pair placements:
  GREEN as qualified upper capacities with no frozen-range gain;
- primary-source match: GREEN cutoff-dated no-match after the
  residual-phase wording repair;
- outer/profile-bulk and downstream quarantine: GREEN; and
- computation: none used.

## 6. Dependencies and exact artifacts used

The promoted kernel depends on the accepted Round 157 literal
coefficient and complete half-period inversion.  Direct Round 158
evidence is:

- reports/sign_adapted_cell_trace_attack.md;
- reports/blind_cell_trace_rederivation.md;
- reports/cell_trace_source_audit.md;
- candidates/conductor_round158_strict_survivor_audit.md;
- proofs/kernels/m9_m1_d1_paired_interior_cell_trace_reduction.md;
- reviews/independent_blind_reconciliation_round158.md;
- reviews/independent_trace_math_round158.md;
- reviews/hostile_profile_power_round158.md; and
- reviews/independent_source_round158.md.

The paths without a campaign prefix above lie under the Round 158
campaign directory.  The blind report is not evidence for its
conditional Weil capacities.  The source audit is evidence only for
the theorem cards and dated no-match after its stated repair.  No
subagent edited the proof graph, proof draft, validation matrix,
synthesis, or State Patch.

## 7. Recommended state effect

Apply a State Patch that creates one proved-internal route-scoped
cell-trace obstruction node.  Record the exact reduction (158.A10),
the safe zero/Nyquist trace pieces and endpoint face, the strict
boundary-weight distinction, the top support-zero range, the actual
raw \(M^{3/4}\) target, the qualified named-method capacities, and the
cutoff-dated source no-match.

Update only the existing \(D=d=L=1\) outer-defect frontier, source
audit, squarefree collar, and global lower-radial dependency records.
Reject endpoint-only, common-profile, automatic-pairing, cardinality,
wrong-target, ordinary-BV, source-transfer, outer-term, and downstream
overclaims.  Leave the full strict trace, Abel outer terms, profile
bulk, paired matrix, complete positive-power \(D=1\) range, every
other owner, M9, the bridge, the quarter target, and both global
exponents open or unchanged.

The internally proved global exponent remains \(1/3\).  The separately
audited external Li--Yang exponent remains

\[
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\tag{158.A18}
\]
