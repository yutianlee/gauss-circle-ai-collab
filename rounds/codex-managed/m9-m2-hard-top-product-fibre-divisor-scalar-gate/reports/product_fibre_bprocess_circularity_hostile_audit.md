# Hostile audit of the hard-TOP product-fibre scalar transforms

## 1. Result

**Verdict: product_fibre_no_go.**  The exact regrouping \(n=hm\) is valid, and the already proved square-entry sector remains target-safe, but none of the audited one-dimensional continuations proves

\[
 |\mathcal T_L^{\mathrm{ns}}|
 \ll_\varepsilon L^{3/2}X^\varepsilon
 \tag{137.H1}
\]

uniformly for every real centre \(X\) and every polynomial intermediate \(1\ll L\ll H\).

The first obstruction occurs immediately after the exact identity (137.B10): the truncated coefficient \(C_L(n)\) is a divisor-incidence sequence with moving hard support, not a smooth bounded-variation amplitude to which a scalar second-derivative or B-process theorem may be applied.  If one ignores that coefficient, even the best elementary curvature ledger gives

\[
 \min\!\left(L^2,\sqrt{JL}+{L^{3/2}\over\sqrt J}\right),
 \tag{137.H2}
\]

against the required \(L^{3/2}\).  Since \(L\ll J^{1/2}\), this has no uniform power margin.  The phase derivative crosses \(\asymp J/L\) integers, so resonant dual modes are a main family rather than an exceptional set.

If one makes the B-process legal by resolving \(h\mid n\), completing the divisibility condition, and retaining the actual profile, its stationary equations are

\[
 r=kh-a,\qquad
 x_{h,r}={Xh^2\over4r^2},\qquad
 \phi_{h,a,k}(x_{h,r})={Xh\over4r},
 \tag{137.H3}
\]

and the endpoint profile becomes exactly \(W(r/y)\).  Thus the principal transform is the inverse of the proved one-sided endpoint transform and returns the original hard reciprocal sum, with its character, Vaaler taper, floor \(y\), hard endpoints, and owner corrections.  It is a self-return, not a strict product-fibre reduction.

Divisor switching is likewise an involution: it maps the upper near-square odd divisor \(h\) to a lower near-square odd complementary divisor with a transformed, still truncated profile.  Completing instead to

\[
 \sum_{d\mid n}\chi_4(d)={r_2(n)\over4}
\]

introduces a complementary coefficient of the same unaudited capacity.  The completed radial block is the Hardy--Voronoi \(r_2\)-block whose quarter-strength bound is the Gauss-circle target in another form.  Importing that bound is circular; subtracting the complement reconstructs the original truncation.

The no-go is methodological, not a lower bound for the physical scalar.  Phase-aligned arbitrary coefficients disprove only coefficient-uniform claims based on support and magnitude.  The actual \(C_L(n)\) might cancel, but no permitted artifact proves the required actual-coefficient signed theorem.  No strict smaller owner-complete survivor is obtained.

## 2. Exact statement and hypotheses

Let

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X={X\over y^2},\qquad H=\lfloor yX^{-1/4}\rfloor,
 \tag{137.H4}
\]

and fix \(1\ll L\ll H\).  The literal coefficient is

\[
 a_{\mathrm{end}}(h,m)
 =\eta_L(h)\Phi\!\left({h\over H+1}\right)
 \left({L^2\over hm}\right)^{3/4}
 W\!\left(\sqrt{{q_Xh\over4m}}\right),
 \tag{137.H5}
\]

for odd \(h\) and \(\lceil h/4\rceil\le m\le h\), extended by zero elsewhere.  The hard-cone scalar is

\[
 \mathcal T_L
 =\sum_{h\ \mathrm{odd}}\chi_4(h)
   \sum_{m=\lceil h/4\rceil}^{h}
   a_{\mathrm{end}}(h,m)e(J\sqrt{hm}).
 \tag{137.H6}
\]

The proved square projection is used only through the norm triangle and gives

\[
 |\mathcal T_L^{\square}|
 \ll_\varepsilon L^{5/4}X^\varepsilon.
 \tag{137.H7}
\]

No orthogonal energy split is asserted.  The open scalar is \(\mathcal T_L^{\mathrm{ns}}\).

For \(n=hm\), the integer inequalities

\[
 \lceil h/4\rceil\le m\le h
 \quad\Longleftrightarrow\quad
 h\mid n,\quad \sqrt n\le h\le2\sqrt n,\quad m={n\over h}
 \tag{137.H8}
\]

are an exact bijection, including the lower ceiling.  Define

\[
 \Omega_{L,X}(n,h):=
 \eta_L(h)\Phi\!\left({h\over H+1}\right)
 W\!\left(\sqrt{{q_Xh^2\over4n}}\right)
 \mathbf 1_{\sqrt n\le h\le2\sqrt n}.
 \tag{137.H9}
\]

Then

\[
 C_L(n)=
 \sum_{\substack{h\mid n\\h\ \mathrm{odd}}}
 \chi_4(h)\Omega_{L,X}(n,h)
 \tag{137.H10}
\]

and

\[
 \mathcal T_L^{\mathrm{ns}}
 =L^{3/2}
 \sum_{\substack{n\asymp L^2\\n\ne\square}}
 n^{-3/4}C_L(n)e(J\sqrt n).
 \tag{137.H11}
\]

All occurrences of \(\eta_L\), \(\Phi\), \(W\), \(H\), \(y\), \(q_X\), half-open support, floors, the hard face, zero extension, and the nonsquare condition in (137.H9)--(137.H11) are literal.

Since \(n\asymp L^2\),

\[
 L^{3/2}n^{-3/4}\asymp1,\qquad
 |C_L(n)|\le\tau(n)\ll_\varepsilon X^\varepsilon.
 \tag{137.H12}
\]

Thus the raw scalar capacity is \(L^{2+o(1)}\), and (137.H1) requires a factor \(L^{1/2-o(1)}\).  The phase

\[
 f(n)=J\sqrt n
\]

has

\[
 f'(n)={J\over2\sqrt n}\asymp{J\over L},\qquad
 f''(n)=-{J\over4n^{3/2}}\asymp-{J\over L^3}.
 \tag{137.H13}
\]

These derivatives contain no coefficient hypothesis for \(C_L(n)\).

## 3. Proof and equation-by-equation hostile derivation

**Arithmetic controls on the truncated coefficient.**  The full odd-divisor identity and the literal truncation differ even on elementary nonsquare inputs.

- If \(n=p>4\) is prime, neither \(1\) nor \(p\) lies in \([\sqrt p,2\sqrt p]\), so \(C_L(p)=0\), while

  \[
  \sum_{d\mid p}\chi_4(d)=1+\chi_4(p)
  \]

  can equal \(2\).

- If \(n=p^{2j}\), then \(n\) is a removed square.  Its fixed divisor \(h=p^j\) may be present, but it belongs to the already controlled projection and may not be deleted through an orthogonal-energy claim.

- If \(n=p^{2j+1}\), the first divisor above \(\sqrt n\) is \(p^{j+1}\).  It lies below \(2\sqrt n\) only for the odd prime \(p=3\).  Thus, whenever the profiles are nonzero, \(C_L(3^{2j+1})\) can contain one literal term although

  \[
  \sum_{d\mid3^{2j+1}}\chi_4(d)=0.
  \]

- Integers formed from several nearby primes \(1\bmod4\) can have many near-square divisors with the same \(\chi_4\)-sign.  Therefore divisor multiplicity alone does not force character cancellation.

These controls rule out replacing (137.H10) by the full divisor coefficient or by a generic random-sign model.

**Curvature capacity before coefficient legality.**  On an interval of length \(N\asymp L^2\), the second-derivative scale is

\[
 \lambda_2\asymp {J\over L^3}.
\]

The classical unweighted second-derivative envelope is

\[
 N\lambda_2^{1/2}+\lambda_2^{-1/2}
 \asymp
 \sqrt{JL}+{L^{3/2}\over\sqrt J}.
 \tag{137.H14}
\]

For \(L=J^\theta\), \(0<\theta<1/2\), the first term divided by the target is

\[
 {\sqrt{JL}\over L^{3/2}}
 ={\sqrt J\over L}
 =J^{1/2-\theta}.
 \tag{137.H15}
\]

When \(\theta\le1/3\), (137.H14) is no better than the trivial length \(L^2\); the trivial-to-target ratio is \(L^{1/2}\).  When \(1/3\le\theta<1/2\), the curvature-to-target ratio is (137.H15).  Hence the best of trivial and second-derivative estimates has no uniform polynomial saving anywhere in the required polynomial range except at the excluded terminal scale \(L\asymp J^{1/2}\).

This is already insufficient in the coefficient-free model.  It is not a bound for (137.H11), because \(|C_L(n)|\le\tau(n)\) does not permit insertion of \(C_L(n)\) into an unweighted derivative estimate.

**Resonant dual modes.**  Across a fixed-ratio \(n\)-interval,

\[
 |f'(n_2)-f'(n_1)|\asymp {J\over L}.
 \tag{137.H16}
\]

Since \(J/L\gg1\), the derivative range contains \(\asymp J/L\) integers.  For each such integer \(r\), the continuous stationary point and its width are

\[
 n_r={X\over4r^2},\qquad
 f(n_r)-rn_r={X\over4r},\qquad
 |f''(n_r)|^{-1/2}\asymp {L^{3/2}\over\sqrt J}.
 \tag{137.H17}
\]

Thus no uniform Kusmin--Landau separation is available.  Exact real centres can force an exact nonsquare lattice resonance: for a chosen nonsquare \(n_0\asymp L^2\) and an integer \(r\), taking \(J=2r\sqrt{n_0}\) gives \(f'(n_0)=r\).  This is a separation countercheck, not a lower bound for the actual coefficient at \(n_0\).

If a smooth amplitude of normalized size one were available, the absolute stationary-dual capacity would be

\[
 {J\over L}\cdot {L^{3/2}\over\sqrt J}
 =\sqrt{JL},
 \tag{137.H18}
\]

which is exactly the first term in (137.H14).  Removing square integers does not remove the continuous family (137.H17); a lawful transform must add the square sector back, use (137.H7), and subtract it through its existing owner.

**Why a direct B-process is illegal.**  The map \(n\mapsto C_L(n)\) jumps whenever a divisor enters or leaves the moving interval and also carries the hard profiles in (137.H9).  No permitted artifact supplies bounded variation, differentiability, controlled partial sums, or a transform formula for this sequence.  Partial summation would require precisely a nontrivial signed estimate for partial sums of \(C_L(n)\), which is the missing theorem.  Treating \(C_L\) as an arbitrary \(X^\varepsilon\)-bounded amplitude is also useless: the phase-aligned array

\[
 \widetilde C(n)
 =\mathbf1_{n\asymp L^2,\ n\ne\square}\,e(-J\sqrt n)
 \tag{137.H19}
\]

has the same support and pointwise magnitude class and gives \(L^{2+o(1)}\) normalized scalar capacity.  It need not be representable by (137.H10), so (137.H19) disproves only coefficient-uniform claims, not the physical target.

**Lawful divisibility completion and exact B-process return.**  Resolve (137.H10) before transforming:

\[
 \mathbf1_{h\mid n}
 ={1\over h}\sum_{a\bmod h}e(an/h).
 \tag{137.H20}
\]

After Poisson summation in \(n\), let \(k\) be the dual integer and put

\[
 \phi_{h,a,k}(x)=J\sqrt x+\left({a\over h}-k\right)x,
 \qquad r=kh-a.
\]

The map \((a,k)\mapsto r\) is a bijection from \(0\le a<h\), \(k\in\mathbb Z\), to \(r\in\mathbb Z\).  On a positive stationary mode,

\[
 \phi'_{h,a,k}(x)=0
 \Longleftrightarrow
 x=x_{h,r}:={Xh^2\over4r^2},
 \tag{137.H21}
\]

\[
 \phi_{h,a,k}(x_{h,r})={Xh\over4r},\qquad
 \phi''_{h,a,k}(x_{h,r})
 =-{2r^3\over Xh^3}.
 \tag{137.H22}
\]

The hard range \(h^2/4\le x\le h^2\) maps to \(J/2\le r\le J\), with the exact one-sided endpoint conventions retained.  More decisively,

\[
 W\!\left(\sqrt{{q_Xh^2\over4x_{h,r}}}\right)
 =W\!\left(\sqrt{{q_Xr^2\over X}}\right)
 =W(r/y),
 \tag{137.H23}
\]

and

\[
 x_{h,r}^{-3/4}
 |\phi''_{h,a,k}(x_{h,r})|^{-1/2}
 =2J^{-1/2}.
 \tag{137.H24}
\]

Consequently the complete stationary principal term is, up to the universal negative-curvature phase,

\[
 \begin{aligned}
 \mathcal T_{L,\mathrm{ret}}^{\mathrm{main}}
 ={}&2e(-1/8)L^{3/2}J^{-1/2}
 \sum_{h\ \mathrm{odd}}
 {\chi_4(h)\eta_L(h)\Phi(h/(H+1))\over h}\\
 &\times
 \sum_{J/2\lesssim r\lesssim J}
 W(r/y)e\!\left({Xh\over4r}\right).
 \end{aligned}
 \tag{137.H25}
\]

Equation (137.H25) is the original reciprocal hard-top block before the proved one-sided endpoint transform, with the same \(y\), real \(q_X\), character, taper, and endpoint profile.  Finite endpoint samples, transition pieces, the Poisson zero/nonstationary modes, and the square subtraction must be restored with their existing owners.  Those corrections are target-safe in the permitted endpoint synthesis, but the main term is not a smaller survivor.  Completion followed by B-process therefore self-returns.

Taking absolute values over \(a\), \(k\), or \(r\) before the bijection in (137.H20)--(137.H25) loses the actual coefficient direction and cannot improve the \(L^2\) raw capacity.  A second transform merely reverses the same canonical map.

**Exact divisor switch.**  Write \(n=2^\nu n_{\mathrm o}\) with \(n_{\mathrm o}\) odd.  Since every contributing \(h\) is odd, put \(d=n_{\mathrm o}/h\).  Then

\[
 {1\over2}\sqrt{{n_{\mathrm o}\over2^\nu}}
 \le d\le
 \sqrt{{n_{\mathrm o}\over2^\nu}},
 \qquad
 \chi_4(h)=\chi_4(n_{\mathrm o})\chi_4(d).
\]

Thus (137.H10) becomes exactly

\[
 \begin{aligned}
 C_L(2^\nu n_{\mathrm o})
 ={}&\chi_4(n_{\mathrm o})
 \sum_{\substack{d\mid n_{\mathrm o}\\
 \frac12\sqrt{n_{\mathrm o}/2^\nu}\le d\le
 \sqrt{n_{\mathrm o}/2^\nu}}}
 \chi_4(d)\,
 \eta_L(n_{\mathrm o}/d)
 \Phi\!\left({n_{\mathrm o}\over d(H+1)}\right)\\
 &\times
 W\!\left(
 \sqrt{{q_Xn_{\mathrm o}\over2^{\nu+2}d^2}}
 \right).
 \end{aligned}
 \tag{137.H26}
\]

This is a lower near-square truncated divisor coefficient with a transformed profile, not the full divisor sum.  It has the same number of fibre incidences, preserves the nonsquare label, and switching twice returns (137.H10).  The square fixed-point seam is already owned by (137.H7).  Divisor switching supplies no contraction.

**Full-divisor completion and circularity.**  Define

\[
 D(n):=\sum_{d\mid n}\chi_4(d)={r_2(n)\over4},
 \qquad
 R_L(n):=D(n)-C_L(n).
 \tag{137.H27}
\]

Then, with every radial cutoff retained,

\[
 \mathcal T[C_L]=\mathcal T[D]-\mathcal T[R_L].
 \tag{137.H28}
\]

The prime and \(3^{2j+1}\) controls above show that \(R_L\) is not a target-safe boundary error; it can contain the entire full coefficient or cancel it to leave one truncated term.  Applying complementary divisors to \(R_L\) returns the omitted tails and central strip rather than decreasing their capacity.

The completed radial block is

\[
 \mathcal H_L(J)
 ={L^{3/2}\over4}
 \sum_{n\asymp L^2}
 {r_2(n)\over n^{3/4}}e(J\sqrt n).
 \tag{137.H29}
\]

A bound \(\mathcal H_L(J)\ll L^{3/2}X^\varepsilon\) is the quarter-strength dyadic Hardy--Voronoi radial estimate.  The authoritative graph records that completing to this full \(r_2\)-sum reproduces the Gauss-circle discrepancy at the target scale.  Invoking the desired Gauss-circle bound to estimate (137.H29) is circular, while estimating both terms on the right of (137.H28) is at least as hard as the original truncation.  The square \(n\)-terms in (137.H29) have only \(O(L^{1+\varepsilon})\) capacity, so the nonsquare restriction does not remove this circularity.

**Complete power ledger.**  The following table separates exact counts from method capacities:

| object | size or capacity | comparison with target |
|---|---:|---:|
| active \(n\)-values | \(L^2\) |  |
| normalized atom \(L^{3/2}n^{-3/4}C_L(n)\) | \(X^\varepsilon\) pointwise |  |
| raw \(\ell^1\) scalar | \(L^{2+o(1)}\) | misses \(L^{1/2-o(1)}\) |
| coefficient square envelope \(\sum|C_L(n)|^2\) | \(L^{2+o(1)}\) | Cauchy still gives \(L^{2+o(1)}\) |
| derivative span / dual modes | \(J/L\) | resonant family, not error |
| one normalized stationary mode | \(L^{3/2}/\sqrt J\) |  |
| absolute stationary-dual capacity | \(\sqrt{JL}\) | ratio \(\sqrt J/L\) |
| trivial versus curvature best case | \(\min(L^2,\sqrt{JL}+L^{3/2}/\sqrt J)\) | no uniform margin for \(L\ll J^{1/2}\) |
| desired scalar | \(L^{3/2}X^\varepsilon\) | target |
| completed B-process main | original reciprocal hard-top scalar | exact self-return |
| full-divisor continuation | localized \(r_2\) Hardy block | target-level circularity |

No row supplies the missing \(L^{1/2}\) from a lawful actual-coefficient estimate.

## 4. First doubtful or unproved step

The first false inference in an affirmative product-fibre proof is

\[
 \text{exact regrouping (137.H11)}
 \quad\Longrightarrow\quad
 \text{a smooth-coefficient one-dimensional curvature estimate}.
 \tag{137.H30}
\]

The regrouping creates no average along the fibre; it sums the literal fibre into \(C_L(n)\).  The divisor jumps, moving near-square window, Vaaler taper, endpoint profile, hard support, floors, and nonsquare deletion do not satisfy any displayed smooth-amplitude hypothesis.  The bound \(|C_L(n)|\le\tau(n)\) supplies no oscillatory directionality, as the phase-aligned control (137.H19) shows.

If this first seam is repaired by expanding \(C_L(n)\) and completing \(h\mid n\), equations (137.H20)--(137.H25) give the next exact obstruction: the stationary phase, Jacobian, and real-centre profile restore the original reciprocal hard-top scalar.  If instead the divisor range is completed, equations (137.H27)--(137.H29) give the circular full-\(r_2\) block plus a complement of unproved capacity.

Thus the first genuinely missing theorem is an owner-preserving fixed-actual-coefficient estimate for (137.H11), or an equivalent signed estimate for the returned reciprocal sum, that fails for (137.H19) and is not derived from a full Gauss-circle \(r_2\)-bound.  No strict smaller exact object is certified.

## 5. Control tests and outcomes

| required control | outcome |
|---|---|
| literal hard cone and square projection | Pass.  Equations (137.H5)--(137.H11) retain the hard ceiling and use the square sector only through its proved norm-triangle owner. |
| exact product-fibre bijection | Pass.  Equation (137.H8) is an exact integer bijection; no fibre averaging or modulus is inserted. |
| truncated \(\chi_4\)-divisor coefficient | Pass with hostile outcome.  Prime, prime-power, and many-near-square-divisor tests show that \(C_L(n)\) is neither \(r_2(n)/4\) nor automatically character-canceling. |
| hard profile, floor, and real centre | Pass.  The completion calculation retains \(H\), \(y=\lfloor J\rfloor\), \(q_X\), and obtains the exact returned profile \(W(r/y)\) in (137.H23). |
| nonsquare and full-divisor controls | No-go.  Squares remain separately target-safe, while completing nonsquares to \(r_2/4\) produces (137.H29) and the unproved complement (137.H28). |
| phase derivatives and resonant dual modes | Fail as a source of uniform saving.  The derivative crosses \(\asymp J/L\) integers and has stationary modes (137.H17); no uniform first-derivative gap exists. |
| one-dimensional scalar capacity | Fail.  Even the coefficient-free curvature envelope (137.H14) misses the target for every polynomial \(L=J^\theta\), \(0<\theta<1/2\). |
| completion, B-process, and self-return | Exact no-go.  Lawful divisibility completion yields (137.H21)--(137.H25), the inverse endpoint transform.  A second B-process only reverses the same canonical map. |
| divisor switching | Exact involution.  Equation (137.H26) is another truncated near-square coefficient with unchanged incidence capacity and transformed literal profiles. |
| coefficient directionality and phase alignment | Scope-correct obstruction.  Equation (137.H19) falsifies coefficient-uniform claims based only on support and size, but it is not a physical lower bound and does not disprove cancellation in \(C_L\). |
| full-divisor circularity | Fail.  The completed coefficient is the Hardy--Voronoi \(r_2\)-block at quarter strength.  Using the desired Gauss-circle estimate here assumes the target. |
| uniformity in \(L\) and \(X\) | Fail for the proposed transforms.  The losses in (137.H15) are polynomial throughout \(0<\theta<1/2\), and exact real centres admit stationary lattice modes. |
| boundary and owner scope | Pass as an audit.  Hard faces, support crossings, endpoint samples, nonsquare subtraction, Poisson zero/nonstationary modes, and transform errors must retain their existing owners; none is silently absorbed into the main estimate. |
| full hard TOP and downstream scope | No closure.  Only the nonsquare polynomial-intermediate scalar was audited; hard TOP, BAL, UNBAL, M9-M2, M9-M1, endpoint uniformity, M9, and all exponent claims remain open. |

All calculations are analytical; no numerical, symbolic, or literature experiment was used.

## 6. Dependencies and exact artifacts used

This report used completely and exclusively the permitted Round-137 context:

1. protocol.md;
2. state/proof_obligations.yml, at frozen graph SHA-256 3c5003b1478d78b8469d4220ad305bb06ee0f869b9c4a741e7211642eeb52cc7;
3. state/active_campaign.yml;
4. strategy/conductor_0823_full_proof_strategy.md;
5. rounds/codex-managed/m9-top-endpoint-transform/synthesis.md;
6. rounds/codex-managed/m9-m2-top-endpoint-near-product-energy/synthesis.md;
7. rounds/codex-managed/m9-m2-hard-top-actual-vector-spectral-gate/synthesis.md;
8. rounds/codex-managed/full-proof-frontier-inequality-selection-gate/reviews/conductor_round127_frontier_selection_adjudication.md;
9. rounds/codex-managed/full-proof-frontier-inequality-selection-gate/synthesis.md;
10. rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/blind_statement.md;
11. the assigned brief rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/briefs/product_fibre_bprocess_circularity_hostile_audit.md.

No Round-137 sibling report, candidate, review, control, plan, synthesis, web source, external theorem import, numerical computation, or symbolic computation was used.  No shared state was edited.

## 7. Recommended state effect

Close this task under **product_fibre_no_go**.  Recommend retaining as exact candidate evidence:

- the hard-cone/product-fibre dictionary (137.H8)--(137.H11);
- the resonant-dual calculation (137.H16)--(137.H18);
- the completed stationary map, profile identity, and Jacobian (137.H20)--(137.H25);
- the exact complementary-divisor involution (137.H26); and
- the full-divisor split and circular Hardy return (137.H27)--(137.H29).

Recommend rejecting promotion of:

- a derivative or exponent-pair bound applied to \(C_L(n)\) without an actual-coefficient hypothesis;
- omission of resonant dual integers or replacement of the exact real centre by a generic one;
- completion followed by absolute values over residue or dual modes;
- divisor switching as a contraction;
- replacement of \(C_L(n)\) by \(r_2(n)/4\);
- a Gauss-circle bound used to estimate the resulting full radial block;
- phase-aligned arbitrary coefficients as a lower bound for the physical scalar; or
- a positive energy, product-fibre mean, or averaged-centre theorem substituted for the fixed signed scalar.

No target bound or strict product-fibre reduction is proved.  The next admissible step would have to be a genuinely new signed scalar theorem for the exact \(C_L(n)\) in (137.H10), uniform in the real centre and hard profiles, with a hypothesis that excludes (137.H19) and a proof that does not pass through the circular full-\(r_2\) estimate or the self-return (137.H25).  All downstream obligations remain unchanged.
