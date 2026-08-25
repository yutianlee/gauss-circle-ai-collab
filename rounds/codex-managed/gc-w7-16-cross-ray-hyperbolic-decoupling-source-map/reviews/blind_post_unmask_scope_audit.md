# Blind post-unmask scope audit

## 1. Result: certified after scoped clarifications

The blind report's central verdict is certified **only as a direct-interface
no-go**: Demeter--Wu Theorems 1.6 and 1.10, together with the literal packet
data supplied to the blind task, do not by themselves give a fixed-centre
strict cross-ray power.  Its exact hyperbolic geometry, determinant
narrowness, rank-one coefficient obstruction, conditional point-evaluation
bound, and capacity verdict are mathematically consistent with the unmasked
source card and conductor normalization.

Three clarifications are required, but none reverses that verdict.

1. The source does contain explicit rescalings and separate ruling/narrow
   machinery.  What is absent is a completed rescaled **arithmetic
   interface**, not all source rescaling or all narrow analysis.
2. The blind kernel estimate is a legal elementary consequence of the
   global theorem plus band-limited evaluation; it is not a pointwise
   statement printed by Demeter--Wu and does not yet identify the literal
   scalar.
3. In the same-denominator control, the length \(D/W\) is the range of
   \(m=a-a'=n/b\), not the range of the determinant \(n\).  The symbol
   \(q\) should not be reused for this length after denoting the surface map
   by \(q(u,v)\).

## 2. Exact hyperbolic coordinates and signs

The conductor chart is

\[
 \xi_r={b\over D},\qquad
 \eta_r=-{Da\over Lb},\qquad
 \zeta_r=-{a\over L},
 \qquad \zeta_r=\xi_r\eta_r.                              \tag{A1}
\]

With \(t_i=cL/(\kappa_iD)\), its phase identity is

\[
 {ca\over\kappa_i b}-{ca'\over\kappa_i b'}
 =t_i(\eta_{r'}-\eta_r).                                  \tag{A2}
\]

The blind chart uses \(z=a/b\), translates a shell centre, and reverses the
sign of the second ruling coordinate:

\[
 \xi_B={b-b_0\over D},\qquad
 \eta_B={D\over L}(z-z_0),\qquad
 \rho_B={a-a_0-b_0(z-z_0)-z_0(b-b_0)\over L}.
\]

Then \(\rho_B=\xi_B\eta_B\).  This is exactly the translated/tangent-plane
version of (A1), with \(\eta_B=-(\eta-\eta_0)\); hence the sign difference is
intentional and the blind phase orientation is correct.  A more source-
aligned presentation would use (A1)--(A2) directly.

The unmasked chart also fixes a scale omitted from the blind presentation:

\[
 t_i\asymp {YL\over D}=Y^{2/3}=Y^{32/48}.                 \tag{A3}
\]

Thus \(t_i\) is the natural unrescaled physical radius.  This does not
invalidate the global kernel inequality below, but it must be included in
any localized or wave-packet import.

## 3. Fixed-point kernel bridge certification

The blind inequality (B1) is legal for an already-constructed transverse
product.  Indeed, if
\(g=f_1\overline{f_2}\), then \(\widehat g\) lies in the difference of two
bounded normalized surface neighborhoods.  A fixed kernel \(K\) may be
chosen with \(\widehat K=1\) there, so

\[
 |g(x_0)|\le \|K\|_2\|g\|_2
 =\|K\|_2\|f_1f_2\|_2.                                   \tag{A4}
\]

Taking the square root of Theorem 1.6 then gives the blind (B1).  Conjugating
the second factor causes no problem because
\(|f_1\overline{f_2}|=|f_1f_2|\).  The kernel norm is constant in the fixed
normalized chart.

This certifies only a pointwise bound for a factored transverse product.
The source card is also correct that Demeter--Wu do not state (A4): it is a
separate elementary sampling lemma.  It does not provide the Fourier
thickening of the arithmetic point masses, control the positive cap norms,
factor the pair-dependent coefficient matrix, or account for an anisotropic
change of variables.  The blind refined formula (B5) was properly made
conditional on an additional localized evaluation bridge; Theorem 1.10's
integral over \(X\) alone does not supply that bridge.

## 4. Source rescaling and cap-scale correction

The blind statement that determinant-band rescaling needs further
accounting is correct, but “not supplied” must be read as “not supplied as a
completed map for this scalar.”  The source itself has explicit, restricted
rescalings: (DW-R1) tracks the change
\(N_{1/R}(\mathbb H)\mapsto N_{1/(Rd^2)}(\mathbb H)\), and Proposition 3.7
has additional rectangle, general-position, scale, and incidence
hypotheses.  Neither is a license to infer applicability from the Hessian
determinant alone.

For an arithmetic band

\[
 h<\eta_{r'}-\eta_r\le2h,
 \qquad (LD)^{-1}\lesssim h\lesssim
 \delta_*={D\over LW}=Y^{-5/48},
\]

the exact symmetry \(\eta=h\widetilde\eta\) changes the evaluation scale to

\[
 R_h\asymp t_i h.                                         \tag{A5}
\]

At the widest band, \(R_{\delta_*}\asymp Y/W=Y^{27/48}\).
The blind estimate \(R\gtrsim(DL/N)^2\) is a correct condition for
**resolving** an \(N\)-band by square caps in the unrescaled full-shell
chart; it is not the rescaled physical radius (A5).  These two quantities
should not be identified.  After (A5), Fourier thickness, square-cap shape,
spatial ball/Jacobian, incidence bounds, and coefficient reassembly remain
open seams.

The source also contains Proposition 4.11 and linear Theorem 2.4 for narrow
horizontal/vertical strips.  They retain the strip contribution in a
positive pointwise decomposition or positive \(L^4\) rectangle energy.
Accordingly, the needed correction is not “the source has no narrow
machinery,” but “the source supplies no fixed-centre arithmetic bound for
the retained narrow term.”

## 5. Same-denominator and scope controls

For \(b'=b\), set

\[
 m=a-a'>0,\qquad n=bm,qquad 1\le m\lesssim D/W.           \tag{A6}
\]

Thus the aligned packet has \(m\)-length
\(D/W=Y^{3/48}\), while its determinant values are multiples of \(b\) and
extend to \(D^2/W\).  In (A1), \(\xi_{r'}=\xi_r\), so this packet lies on
the \(\xi=\)constant ruling.  By contrast, the general determinant support
has \(|\eta_{r'}-\eta_r|\le\delta_*\) and is near the other,
\(\eta=\)constant ruling direction.  This distinction should be kept
explicit.

At \(c=\kappa_i b^2\), the geometric phase is

\[
 e\!\left({cm\over\kappa_i b}\right)=e(bm)=1,
\]

so the blind hostile control and its local triangle price
\(Y^{3/48}\) are certified.  It remains only a per-ray control, not a lower
bound for the full literal scalar.  Here the arithmetic labels “M1/M2
carrier” must also be distinguished from the refined theorem's incidence
parameters \(M_1,M_2\).

The final no-go scope is therefore:

- direct full-shell applicability fails by two-coordinate transversality;
- direct product applicability fails without a controlled factorization of
  the pair coefficient and Fourier thickening;
- direct completion fails because the ruling term and positive norm costs
  remain unbounded.

It does **not** prove that a future determinant-band rescaling, interface
lemma, sampling normalization, and separate narrow estimate cannot use the
Demeter--Wu results.

## 6. Dependencies and artifacts used

This post-unmask audit read only:

- `reports/demeter_wu_exact_source_card.md`;
- `candidates/conductor_exact_hyperbolic_normalization.md`;
- `reports/blind_pointwise_transversality_feasibility.md`.

No shared state or original report was edited, and no numerical or web work
was performed in this audit.

## 7. Recommended state effect

**Retain with scope clarification.**  Certify the blind report as evidence
against a direct theorem-to-scalar promotion.  Record (A1)--(A6), replace
any reading of “no source rescaling/narrow machinery” by the narrower
interface statement above, and rename the same-denominator length variable
to \(m\).  No exponent or shared-state promotion is justified.
