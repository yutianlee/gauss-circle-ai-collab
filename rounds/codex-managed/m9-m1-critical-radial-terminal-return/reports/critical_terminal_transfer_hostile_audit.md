# Round 60 independent hostile audit: critical terminal transfer

## 1. Result

The proposed transfer survives the hostile audit in a narrow, corrected
form, and the permitted accepted interface actually proves the stronger
complex modulus.  Let \(V\) be a fixed member of
\(C_c^\infty((c,C))\), where \(0<c<C<16\).  Then the accepted terminal
M1 theorem and the accepted positive-frequency interior/one-sided
transforms imply
\[
 |\mathcal G_V(X)|\ll_{\varepsilon,V}X^\varepsilon .
 \tag{60.H1}
\]
For complex-valued \(V\), apply the real-valued positive-frequency
identity to its real and imaginary parts; the real GAR projection is an
immediate corollary.
This is a genuinely new estimate for one smooth critical radial sector:
the terminal theorem was proved directly by a frequency-first
nearest-product/divisor argument, so its use here does not assume GAR or
the transformed radial estimate.

One correction is mandatory.  Equation (60.8) in the packet
must retain the exact upper factor \(\mathbf1_{h\le H_j}\); without it the
displayed coefficient is neither the common antecedent nor supported in
a terminal shell.  The radial endpoint near \(n=16Y\), lower radial
sectors, full GAR, and M9-M1 still do not follow.

No countercapacity remains in the fixed-\(c\) support.  The positive
lower radial cutoff forces \(h\gg H_j\), the inherited exact condition
\(h\le H_j\) owns the upper edge, and its single jump costs
\(O(H_j^{-1})\) in the frequency BV norm.  Floors, small heights, the
hard denominator endpoint, stars, and the scale sum are all target-safe.

## 2. Exact statement and hypotheses

Put
\[
 R=X^{1/4},\qquad Y=\sqrt X=R^2,\qquad
 D_j=2^{-j}\lfloor\sqrt X\rfloor,\qquad
 H_j=\lfloor D_j/R\rfloor .
\]
Only active scales \(H_j\ge1\) occur.  Use the accepted profiles
\[
 w_0(d)=\mathbf1_{d\le y}W(d/y),\qquad
 w_j(d)=W(d/D_j)\quad(j\ge1),
 \qquad y=\lfloor\sqrt X\rfloor ,
\]
where the interior profile ratios lie in
\([1/2,4/3]\), and use the exact accepted height and star conventions.

For a fixed \(V\in C_c^\infty((c,C))\),
\(0<c<C<16\), define the positive common antecedent
\[
 \mathcal B_{j,V}
 =
 \sum_{h\ge1}
 \eta_j(h)\mathbf1_{h\le H_j}
 {\Phi(h/(H_j+1))\over h}
 \sum_d\chi_4(d)w_j(d)
 V\!\left({4Xh^2\over d^2Y}\right)e(hX/d),
 \tag{60.H2}
\]
where \(\eta_j\) is a lower terminal cutoff constructed below.  Define
also
\[
 \mathcal P_V
 =2\operatorname {Re}\left\{
 -{2i\over\pi}\sum_{j:H_j\ge1}\mathcal B_{j,V}
 \right\}.
 \tag{60.H3}
\]
The coefficient \(-2i/\pi\) is the exact factor left by
\(-4\alpha_{h,H_j}\) after \(\Phi/h\) is placed in
\(\mathcal B_{j,V}\).

The exact terminal-mode coefficient is
\[
 u_{j,t}(h)=
 \eta_j(h)\mathbf1_{h\le H_j}
 {\Phi(h/(H_j+1))\over h}h^{2it}.
 \tag{60.H4}
\]
The hypotheses used from the accepted terminal theorem are precisely:
the denominator integers lie in a fixed shell \(d\asymp D_j\), including
the one-sided truncation \(d\le y\) for \(j=0\); the denominator
coefficient may be arbitrary complex and bounded; and
\[
 \|u\|_\infty+\sum_h|\Delta u(h)|\ll L^{-1}
 \]
for a frequency coefficient supported on \(h\asymp L\).

The transform hypothesis needed below is the already accepted
interior/top B-process, uniformly for a bounded normalized smooth family
of spatial multipliers.  Here that family is
\[
 x\longmapsto W(x)V(4\lambda^2/x^2),
 \qquad \lambda={Rh\over D_j},
 \tag{60.H5}
\]
on a fixed compact \(x\)-range and with \(\lambda\) in a fixed compact
range.  All normalized derivatives of (60.H5) are bounded in terms of
\(V,W\).  Thus the accepted \(O_W\) proof has the same error bound with
\(O_{V,W}\); equivalently, Mellin-mode differentiation costs only a
fixed polynomial in \(1+|t|\), integrable against \(\widehat V(t)\).

## 3. Proof and derivation

If a term in (60.H2) is nonzero, put
\[
 z={4R^2h^2\over d^2}.
\]
Then \(z\in[c,C]\), so
\[
 h={d\sqrt z\over2R}.
 \tag{60.H6}
\]
Since \(d/D_j\ge1/2\) on every active profile,
\[
 h\ge{\sqrt c\over4}{D_j\over R}
 \ge{\sqrt c\over4}H_j.
 \tag{60.H7}
\]
The existing factor \(h\le H_j\) supplies the other end.  Set
\(\gamma=\sqrt c/4\), and choose a fixed smooth \(\psi\) that is zero
on \([0,\gamma/2]\) and one on \([\gamma,\infty)\).  For unbounded
\(H_j\), take \(\eta_j(h)=\psi(h/H_j)\); the finitely many bounded
heights are defined directly.  Equations (60.H6)--(60.H7) prove that
\(\eta_j=1\) on every possible term.  Hence its insertion changes
nothing.

On the support of (60.H4), \(h\asymp_V H_j\).  The accepted bounded
variation of \(\Phi\), product variation, and
\[
 |(h+1)^{-1+2it}-h^{-1+2it}|
 \ll (1+|t|)h^{-2}
 \]
give
\[
 \|u_{j,t}\|_\infty+
 \sum_h|\Delta u_{j,t}(h)|
 \ll_V {1+|t|\over H_j}.
 \tag{60.H8}
\]
This includes the jump from \(h=H_j\) to \(h=H_j+1\), whose size is
\(O(H_j^{-1})\).  The same inequality is immediate for bounded
\(H_j\).

With
\[
 \widehat V(t)=\int_0^\infty V(z)z^{-it}{dz\over z},
 \qquad
 V(z)={1\over2\pi}\int_{\mathbb R}\widehat V(t)z^{it}\,dt,
 \]
finite summation and absolute Mellin inversion give
\[
\begin{aligned}
 \mathcal B_{j,V}
 ={1\over2\pi}\int_{\mathbb R}\widehat V(t)
 \left({4X\over Y}\right)^{it}
 \sum_hu_{j,t}(h)
 \sum_d\chi_4(d)w_j(d)d^{-2it}e(hX/d)\,dt.
\end{aligned}
\tag{60.H9}
\]
The signs and the \(2\pi\) normalization are exact.  The denominator
mode has modulus one; the direct terminal theorem asks for no
denominator BV or derivatives.  By homogeneity and (60.H8), its
\(t\)-mode bound is
\[
 \ll_\varepsilon
 (1+|t|)X^\varepsilon
 \left(1+{D_j\over H_j}\right).
\]
Because \(V(e^x)\) is smooth and compactly supported,
\[
 \int_{\mathbb R}|\widehat V(t)|(1+|t|)\,dt<\infty .
\]
Also, if \(H_j\ge1\), then
\[
 {D_j\over H_j}<2R.
\tag{60.H10}
\]
Consequently
\[
 |\mathcal B_{j,V}|\ll_{\varepsilon,V}RX^\varepsilon,
 \qquad
 \left|\sum_j\mathcal B_{j,V}\right|
 \ll_{\varepsilon,V}RX^\varepsilon,
 \qquad
 |\mathcal P_V|\ll_{\varepsilon,V}RX^\varepsilon
\tag{60.H11}
\]
after summing the \(O(\log X)\) active scales and reducing the
\(\varepsilon\) used per scale.

It remains to identify the same antecedent after transformation.  At an
interior stationary point
\[
 d_*=2\sqrt{hX/q},\qquad n=hq,\qquad q\ {\rm odd},
\]
the Mellin factor satisfies
\[
 \left({4X\over Y}\right)^{it}h^{2it}d_*^{-2it}
 =\left({hq\over Y}\right)^{it}
 =\left({n\over Y}\right)^{it}.
\tag{60.H12}
\]
Equivalently, without Mellin modes,
\[
 {4Xh^2\over d_*^2Y}={hq\over Y}.
\]
The accepted positive stationary constant is
\[
 {e(1/8)\over i}(hX)^{1/4}q^{-3/4}.
\]
Multiplying it by \(\Phi(h/(H_j+1))/h\) gives exactly
\[
 {e(1/8)\over i}R\,
 (hq)^{-3/4}\Phi(h/(H_j+1)).
\tag{60.H13}
\]
On every nonzero stationary term, \(\eta_j=1\).  Summing \(j\), then
grouping \(n=hq\), therefore yields
\[
 \sum_j\mathcal B_{j,V}
 ={e(1/8)\over i}R\,\mathcal G_V(X)
 +\mathcal Q_{0,V}+\mathcal R_V,
\tag{60.H14}
\]
where \(\mathcal Q_{0,V}\) is the one-sided top boundary and
\(\mathcal R_V\) is the sum of transform remainders.  Multiplying
(60.H14) by \(-2i/\pi\) and taking twice the real part gives
\[
 \mathcal P_V
 =-{4\over\pi}R
 \operatorname {Re}\{e(1/8)\mathcal G_V(X)\}
 +\mathcal E_V.
\tag{60.H15}
\]
This proves that the external factor occurs exactly once.

For the top scale, the endpoint amplitude is
\[
 V\!\left({4Xh^2\over y^2Y}\right),
\]
so the explicit accepted cotangent term is the old
\(E_h^\chi(X)\) multiplied by this value.  Its support has
\(h\asymp_V H_0\), and \(E_h^\chi(X)\ll1\); hence
\[
 \mathcal Q_{0,V}
 \ll\sum_{h\asymp H_0}{1\over h}\ll_V1.
\tag{60.H16}
\]
The normalized profiles (60.H5) form a uniformly smooth family, so the
accepted interior and top error calculation gives
\[
 \mathcal R_V=O_{V,W}(\log^2(2X)).
\tag{60.H17}
\]
The permitted Round-14 algebra supplies (60.H14) before pairing:
the interior formula and the hard-top formula are both identities for
the positive-frequency sum.  Therefore (60.H11), (60.H14),
(60.H16), and (60.H17), divided by \(R\), prove the modulus (60.H1)
directly.  Pairing negative frequencies is needed only to identify the
original real M1 quantity and the external factor in (60.H15), not to
bound \(\mathcal G_V\).

## 4. First doubtful or unproved step

As printed, the first false step is (60.8): it omits
\(\mathbf1_{h\le H_j}\).  The lower cutoff \(\eta_j\) is one for all
large \(h\) and cannot replace that upper boundary.  Without the
indicator, \(\Phi(h/(H_j+1))\) is used outside its accepted interval,
the coefficient is not compactly terminal, and (60.9) does not follow.
Formula (60.H4) is the necessary correction.  This is a statement seam,
not a capacity obstruction.

After that correction, the first unproved continuation is not the
fixed-\(V\) theorem but its radial enlargement.  The accepted
positive-frequency identities already prove the modulus; no phase
rotation or negative-frequency pairing is required for that conclusion.

There is also no automatic finite-partition proof at the product endpoint
\(n=16Y\) from cutoffs whose supports all satisfy \(C<16\).  Covering the
entire upper critical edge requires a separately stated endpoint-safe
cutoff (or an extension past \(16\) followed by the exact product
truncation) and its star ledger.  Nothing here covers \(n/Y\to0\).
Thus the fixed compact sector is certified, but full critical GAR and
full GAR remain separate claims.

## 5. Control tests and outcomes

| Control | Hostile check | Outcome |
|---|---|---|
| Mellin normalization | Check transform sign, \(2\pi\), and all powers. | Pass: (60.H9) and (60.H12) give \(h^{2it}d^{-2it}\) and \((n/Y)^{it}\) exactly. |
| Terminal support | Derive support using actual profile ratios and retain the upper edge. | Pass after correcting (60.8): \(h\ge(\sqrt c/4)H_j\) and \(h\le H_j\).  No strict upper margin is needed. |
| Frequency BV | Include lower taper, \(\Phi/h\), \(h^{2it}\), and the upper jump. | Pass: total norm is \(O_V((1+|t|)/H_j)\). |
| Denominator mode | Test whether \(d^{-2it}\) violates a hidden spatial-BV hypothesis. | Pass: the accepted direct terminal theorem allows arbitrary bounded complex denominator coefficients. |
| B-process constant | Recompute the monomial and Vaaler constants. | Pass: (60.H13) gives \(e(1/8)R/i\), and the full factor is \(-4R/\pi\) in (60.H15). |
| Hard top boundary | Retain \(d=y\) with full primal weight, its cotangent term, and the stationary half-weight. | Pass: the boundary is multiplied by the radial endpoint value and is \(O_V(1)\); it is not folded into \(\mathcal G_V\). |
| Floors, profiles, stars | Avoid replacing \(H_j\), telescoping \(w_j\), or deleting equality weights. | Pass: exact \(H_j\), \(w_j\), and \([w_j(d_*)]^*\) remain in \(\mathcal C_X^*\).  Smooth \(V\) commutes with the half-weight; at a smooth zero edge the starred term vanishes. |
| Small height | Test \(H_j=1,2\) and \(H_j=0\). | Pass: bounded positive heights satisfy the same estimate directly and \(D_j/H_j<2R\); \(H_j=0\) contributes nothing to \(\Omega_X^*\) and remains with the inactive-bottom owner. |
| Scale one-count | Check overlaps and the \(j\)-sum. | Pass: every \((j,h,q)\) incidence is transformed once; overlapping dyadic profiles are retained as the exact sum defining \(\Omega_X^*\), not collapsed by telescoping. |
| Error sum | Sum multiplier-dependent interior/top errors before dividing by \(R\). | Pass for fixed \(V\): uniform normalized seminorms give \(O_{V,W}(\log^2X)\), and the top boundary is \(O_V(1)\). |
| GAR implication scope | Decide whether this is merely the old Hardy return. | Pass as a new scoped estimate: the positive antecedent is directly terminal-bounded, so even its complex modulus is controlled.  It proves only a fixed smooth \(n\asymp Y\) sector, not the open global radial sum. |
| Downstream scope | Test claims for endpoint completion, lower radial range, M9-M1, M9, or the exponent. | Fail for every such enlargement; none follows from (60.H1). |

The complex-versus-real control passes more strongly than the frozen
target: the accepted interface contains the positive-frequency
interior and top identities, so (60.H14) plus a modulus bound for its
antecedent proves \(|\mathcal G_V|\).  The paired real identity is a
separate normalization check, not the analytic source of the estimate.

## 6. Dependencies and exact artifacts used

This audit used only the permitted repository context:

- protocol.md;
- state/proof_obligations.yml;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-critical-radial-terminal-return/derivation_packet.md;
- rounds/codex-managed/m9-m1-top-block-quadratic-divisor-completion/synthesis.md;
- rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md;
- rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/m1_terminal_arithmetic_attack.md; and
- rounds/codex-managed/m9-m1-dual-r2-recombination/reports/blind_rcs_coefficient_algebra.md.

The exact inputs are the proved terminal estimate
\(O_\varepsilon(1+D/L)\), its allowance of arbitrary bounded complex
denominator weights and a one-sided hard truncation, the accepted
positive interior constant \(e(1/8)/i\), the accepted one-sided top
cotangent boundary and remainder, the exact Round-14 coefficient
\(\mathcal C_X^*\), and the accepted BV regularity of \(\Phi\).

No external theorem, web source, numerical computation, or unlisted
Round-60 report was used.

## 7. Recommended state effect

Revise the packet coefficient by replacing (60.8) with (60.H4), and
then promote the narrow modulus lemma (60.H1) for every fixed compact critical sector
\(V\in C_c^\infty((c,C))\), \(0<c<C<16\).  Record explicitly that its
proof uses the common antecedent (60.H2), the terminal theorem before
transformation, and the positive-frequency relation (60.H14); this distinguishes the
result from a circular Hardy/GAR return.

Retain as open: the endpoint-safe completion at \(n=16Y\), all lower
radial sectors \(n/Y\to0\), the alpha transition, full GAR, blockwise
M9-M1, M9, and the Gauss-circle exponent.  The new lemma may remove only
the fixed smooth critical radial sector from the global angular radial
obligation.  No other graph node should be closed by implication.
