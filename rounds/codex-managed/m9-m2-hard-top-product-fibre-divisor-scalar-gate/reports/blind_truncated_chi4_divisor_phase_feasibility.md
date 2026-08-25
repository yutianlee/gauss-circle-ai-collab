# 1. Result

**Result: `product_fibre_no_go`.**  The product-fibre identity (137.B10) is exact, and the square-entry sector is legitimately smaller by (137.B5)--(137.B6).  The remaining statement-only data do not prove

\[
 |\mathcal T_L^{\mathrm{ns}}|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

The first obstruction is not an error in the regrouping.  It is the absence of an actual-symbol, signed scalar estimate for the highly discontinuous coefficient \(C_L(n)\).  The derivatives in (137.B11) cannot be applied coefficient-uniformly: a phase-adapted coefficient array saturates the full \(\ell^1\) capacity, while the packet gives no partial-sum, additive-twist, bounded-variation, or Fourier estimate for the literal truncated divisor coefficient that would exclude this control.

The standard curvature ledger also fails quantitatively before the coefficient issue is repaired.  On \(n\asymp L^2\), the formal B-process has

\[
 \#\{\text{stationary dual modes}\}\asymp \frac JL,
 \qquad
 |f''|^{-1/2}\asymp\frac{L^{3/2}}{\sqrt J},
\]

so its dual absolute capacity is

\[
 \sqrt{JL}
 =L^{3/2}\frac{\sqrt J}{L}
 \asymp L^{3/2}\frac HL,
\]

one unbounded factor \(H/L\) above the target.  Completing \(C_L\) does not create a new object: its additive Fourier transform expands exactly back to the literal hard product cone.  Applying a B-process after that expansion has stationary point \(m_*=Xh/(4\nu^2)\), reciprocal phase \(Xh/(4\nu)\), and endpoint profile \(W(\nu/y)\); a second pass returns the original square-root phase.  This is a self-return/circularity control, not a saving.

There are exact nonsquare resonances.  For any supported nonsquare \(n_0\) and integer \(\nu\), choosing

\[
 X=4\nu^2n_0
\]

gives \(f'(n_0)=\nu\) and \(e(f(n_0))=1\).  Taking \(\nu\) to be a sufficiently large power of \(L\) preserves \(L\ll H\) at a polynomial intermediate scale.  A larger exact family is \(X=Ds^2,\ n=Dt^2\) with fixed squarefree \(D>1\), for which \(e(J\sqrt n)=1\); its raw size is only \(L^{1+o(1)}\), so it is a method control rather than a lower bound against \(L^{3/2}\).

Thus the target may still be true for the fixed literal coefficient, but no target bound or strict smaller owner-complete reduction follows from (137.B1)--(137.B11).  The smallest certified open object remains the full nonsquare product-fibre scalar (137.B10).

# 2. Exact statement and hypotheses

Retain

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=\frac{X}{y^2},\qquad H=\lfloor yX^{-1/4}\rfloor,
\]

one half-open polynomial intermediate block \(1\ll L\ll H\), and every literal profile and endpoint in (137.B2).  Define

\[
 B_L(n):=
 L^{3/2}n^{-3/4}C_L(n)
 1_{\{n\ne \square\}}.
\]

Then

\[
 \mathcal T_L^{\mathrm{ns}}
 =\sum_{n\asymp L^2}B_L(n)e(J\sqrt n),
 \qquad |B_L(n)|\ll\tau(n),
\tag{2.1}
\]

because \(L^{3/2}n^{-3/4}\asymp1\) on the block.  Hence the coefficient-blind capacity is \(L^{2+o(1)}\), and the target needs a genuine factor \(L^{1/2-o(1)}\).

No hypothesis grants any of the following:

* a sign or lower envelope for \(\eta_L\), \(\Phi\), or \(W\);
* smoothness, monotonicity, bounded variation, or multiplicativity of \(C_L(n)\);
* cancellation in partial sums or additive twists of \(C_L\);
* permission to replace the near-square divisor truncation by all divisors;
* permission to smooth a hard face, alter \(q_X\), complete a fibre, or reuse the already-owned square projection.

The precise no-go statement proved below is:

> The product-fibre map is an exact bijection and the arithmetic controls contain nonsquare one-term fibres, exact real-centre resonances, and same-phase squarefree-kernel families.  The full odd-divisor identity does not control the weighted upper near-square truncation.  Every derivative, completion, or B-process route considered from the stated data either requires a new signed transform bound for \(C_L\), has capacity above \(L^{3/2}\), or expands/returns to the original hard product cone.  The phase-aligned array is used only to refute coefficient-uniform reasoning and never as a physical lower bound.

# 3. Proof or derivation

**Exact product-fibre bijection.**  If \(n=hm\), then \(m\le h\) is equivalent to \(h\ge\sqrt n\), while \(m\ge h/4\) is equivalent to \(h\le2\sqrt n\).  Since \(m\) is integral,

\[
 m\ge \frac h4
 \quad\Longleftrightarrow\quad
 m\ge\left\lceil\frac h4\right\rceil.
\]

Thus (137.B3) is equivalent term by term to (137.B8), with inverse \(m=n/h\).  Moreover,

\[
 a_{\mathrm{end}}(h,n/h)
 =L^{3/2}n^{-3/4}
  \eta_L(h)\Phi\!\left(\frac h{H+1}\right)
  W\!\left(\sqrt{\frac{q_Xh^2}{4n}}\right).
\]

Summing over the fibre gives (137.B9)--(137.B10) without averaging, completion, or endpoint change.  The square projection is removed only by

\[
 |\mathcal T_L|
 \le |\mathcal T_L^\square|+|\mathcal T_L^{\mathrm{ns}}|
\]

and the already-stated bound (137.B6); no orthogonal energy decomposition is used.

**Arithmetic controls for the truncation.**

1. If \(n>4\) is prime, its divisors \(1,n\) both lie outside
   \([\sqrt n,2\sqrt n]\), so \(C_L(n)=0\).
2. If \(n=p^{2a+1}\) is an odd nonsquare prime power, the first divisor
   above \(\sqrt n\) is \(p^{a+1}\).  It lies below \(2\sqrt n\) only
   when \(\sqrt p\le2\).  Thus \(p\ge5\) gives no term, while
   \(n=3^{2a+1}\) has one possible near-square divisor
   \(h=3^{a+1}\), subject to the literal profiles.
3. For \(p>3\) prime, \(n=3p^2\) is nonsquare and the only divisor in
   \([\sqrt n,2\sqrt n]\) is \(h=3p\).  Hence

   \[
   C_L(3p^2)=
   \chi_4(3p)\eta_L(3p)
   \Phi\!\left(\frac{3p}{H+1}\right)
   W\!\left(\sqrt{\frac{3q_X}{4}}\right),
   \tag{3.1}
   \]

   whenever the height profile admits \(3p\).  There is no internal
   divisor-character cancellation on this fibre.
4. More generally, if \(n=pq\) with odd primes \(p<q\le4p\), then
   \(h=q\) is the unique near-square upper divisor.  Conversely, numbers
   with many divisors near \(\sqrt n\) may have several terms, but the
   packet supplies only the bound by \(\tau(n)\), not an orthogonality
   law among their \(\chi_4(h)\) values.
5. Even prime powers \(p^{2a}\) and all other square products belong to
   the removed square owner; they cannot be reintroduced as a diagonal
   completion of the nonsquare sum.

The full identity

\[
 \sum_{d\mid n}\chi_4(d)=\frac{r_2(n)}4
\tag{3.2}
\]

does not estimate (137.B9).  It contains all divisor sizes with unit
weight, whereas \(C_L(n)\) contains only odd divisors in one upper
near-square window and three literal profiles.  For odd nonsquare \(n\),
the involution \(d\leftrightarrow n/d\) gives

\[
 \chi_4(n/d)=\chi_4(n)\chi_4(d).
\]

If \(\chi_4(n)=1\), paired signs agree rather than cancel; if
\(\chi_4(n)=-1\), the full sum cancels pairwise while either truncated
half may remain nonzero.  Thus completing to (3.2) can erase precisely
the truncated information that must be bounded.  It also replaces the
coefficient by the nonnegative radial multiplicity \(r_2(n)/4\), not by
a simpler signed object.

**Exact resonance and derivative controls.**  Integer dual modes satisfy

\[
 f'(x_\nu)=\nu,\qquad
 x_\nu=\frac{J^2}{4\nu^2}=\frac{X}{4\nu^2},
 \qquad
 f(x_\nu)-\nu x_\nu=\frac{X}{4\nu}.
\tag{3.3}
\]

For \(\nu\asymp J/L\), one has \(x_\nu\asymp L^2\),

\[
 |f''(x_\nu)|\asymp\frac J{L^3},
 \qquad
 |f''(x_\nu)|^{-1/2}\asymp\frac{L^{3/2}}{\sqrt J},
\tag{3.4}
\]

and the range of \(f'\) across the dyadic \(n\)-block contains
\(\asymp J/L\) integers.  Consequently a formal absolute B-process
ledger has size \(\sqrt{JL}\), above the target by \(H/L\).
The usual second-derivative ledger,

\[
 L^2\sqrt{\frac J{L^3}}
 +\sqrt{\frac{L^3}{J}}
 =\sqrt{JL}+\frac{L^{3/2}}{\sqrt J},
\tag{3.5}
\]

has the same bad leading term on subranges where that test applies.
When the curvature crosses integer scales, exact and near stationary
dual modes must instead be separated; they do not yield a uniform
improvement.

The real centre prevents a uniform nonresonance condition.  Given a
nonsquare integer \(n_0\asymp L^2\) and an integer \(\nu\), set

\[
 X=4\nu^2n_0,\qquad J=2\nu\sqrt{n_0}.
\]

Then

\[
 f'(n_0)=\nu,\qquad
 f(n_0)=2\nu n_0\in\mathbb Z.
\tag{3.6}
\]

Choosing \(\nu=L^A\) with fixed sufficiently large \(A\) gives
\(H\asymp\sqrt{\nu L}\gg L\), while \(L\) remains a fixed power of
\(X\).  Thus every proposed derivative proof must handle exact
stationary modes uniformly; floors and the real \(q_X\) do not forbid
them.

There is also a simultaneous nonsquare resonance family.  Let \(D>1\)
be squarefree, \(X=Ds^2\), and \(n=Dt^2\).  Then

\[
 J\sqrt n=Dst\in\mathbb Z.
\tag{3.7}
\]

For \(n\asymp L^2\) this family has \(O(L/\sqrt D)\) members, and
\(\sum_{t\asymp L/\sqrt D}\tau(Dt^2)\ll_\varepsilon L^{1+\varepsilon}\).
It survives the nonsquare restriction but is smaller than the target.
It therefore falsifies “nonsquare implies nonresonant” without
falsifying (137.B7).

**Completion and exact self-return.**  The additive transform of the
literal product coefficient expands exactly as

\[
 \begin{aligned}
 \widehat B_L(\theta)
 &:=
 \sum_n B_L(n)e(-\theta n)\\
 &=
 \sum_{\substack{h\ \mathrm{odd}}}\chi_4(h)
 \sum_{\substack{\lceil h/4\rceil\le m\le h\\hm\ne\square}}
 a_{\mathrm{end}}(h,m)e(-\theta hm).
 \end{aligned}
\tag{3.8}
\]

Thus one-dimensional completion asks for an additive-twist estimate of
the original hard product cone, with the same profiles, floors, and
square deletion.  No such estimate is in the packet, and taking
\(|\widehat B_L|\) loses the needed signed direction.

The phase-level B-process after expanding the fibre is equally
involutive.  For fixed \(h\), let

\[
 F_h(m)=J\sqrt{hm}.
\]

At dual integer \(\nu\),

\[
 F_h'(m_*)=\nu,\qquad
 m_*=\frac{Xh}{4\nu^2},\qquad
 F_h(m_*)-\nu m_*=\frac{Xh}{4\nu}.
\tag{3.9}
\]

At the same point the literal endpoint argument becomes

\[
 \sqrt{\frac{q_Xh}{4m_*}}
 =\sqrt{\frac{q_X\nu^2}{X}}
 =\frac{\nu}{y}.
\tag{3.10}
\]

Hence the first transform produces the reciprocal phase and the same
endpoint geometry; differentiating \(Xh/(4\nu)\) returns
\(\nu^2=Xh/(4m)\) and therefore the original square-root critical
relation.  This proves a phase/canonical self-return.  It is not an
exact finite-sum identity without a fresh hard-edge, crossing,
stationary-remainder, and zero-extension ledger, and it provides no
independent power saving.

**Coefficient directionality.**  A derivative theorem uniform over
coefficients of the displayed magnitude is impossible.  On any selected
set of nonsquare \(n\), the method-control array

\[
 b(n)=|B_L(n)|e(-J\sqrt n)
\tag{3.11}
\]

makes every nonzero selected term positive and attains its full
\(\ell^1\) mass.  Equation (3.11) is not the literal \(B_L(n)\), does
not respect its divisor construction, and gives no physical lower bound.
It proves only that a successful argument must use an exact property of
the fixed \(\chi_4\), taper, endpoint, and near-square divisor sum that
fails for (3.11).  No such property is stated.

# 4. First doubtful or unproved step

The first invalid affirmative step would be to insert
\(|C_L(n)|\le\tau(n)\) into a first- or second-derivative estimate as if
\(C_L(n)\) were a smooth bounded amplitude.  Oscillatory derivative
tests control the phase against amplitudes with specified variation or
against unweighted sums; they do not create cancellation for an
arithmetic array that may change on every integer.  Summation by parts
would require a new bound for

\[
 A_L(u;\alpha)
 :=
 \sum_{\substack{n\le u\\n\ne\square}}
 B_L(n)e(\alpha n)
\tag{4.1}
\]

uniformly at the additive frequencies generated by completion.  Neither
(137.B9) nor \(|C_L|\le\tau\) supplies such a bound.

If one attempts to prove (4.1) by expanding the divisor fibre, equation
(3.8) returns the complete signed hard cone.  If one then applies a
B-process, (3.9)--(3.10) returns the original square-root canonical
relation and hard endpoint.  This is not a strict reduction: all
\((h,m)\), the nonsquare deletion, \(\chi_4\), \(\eta_L\), \(\Phi\),
\(W\), floors, and the fixed scalar owner remain.

Independently, a resonance-deletion argument has no uniform starting
gap, because (3.6) places an arbitrary supported nonsquare fibre at an
exact integer dual mode for an admissible polynomial real centre.
The exact family (3.7) shows that removing square \(n\) does not remove
all phase-free nonsquare products.  Although that family is itself
target-safe, the remainder cannot be bounded without the same missing
signed transform theorem.

Therefore the first exact survivor is not smaller than (137.B10):
it is (137.B10) itself, equivalently its complete additive-transform
family (3.8).  Calling the latter a reduction would be circular.

# 5. Control tests and outcomes

| Required control | Exact input and test | Outcome and implication |
|---|---|---|
| `literal_hard_cone_and_square_projection` | Keep (137.B2)--(137.B4), remove \(hm=\square\) only by (137.B5)--(137.B6) and norm triangle. | **Pass.** No square entry is reused and no orthogonal energy split is assumed. |
| `exact_product_fibre_bijection` | Prove \(m\in[\lceil h/4\rceil,h]\iff h\mid n,\sqrt n\le h\le2\sqrt n\). | **Pass.** The inverse is \(m=n/h\), and the amplitude gives (137.B9)--(137.B10) exactly. |
| `truncated_chi4_divisor_coefficient` | Test primes, odd prime powers, \(3p^2\), close semiprimes, and fibres with many near-square divisors. | **No automatic cancellation.** Primes and most odd prime powers vanish, but (3.1) and close semiprimes have a single character term.  Many-divisor fibres have only the \(\tau(n)\) bound. |
| `hard_profile_floor_and_real_centre` | Retain \(\eta_L,\Phi,W,H,y,q_X\); tune \(X=4\nu^2n_0\). | **Exact resonance.** Equation (3.6) is compatible with \(L\ll H\) at polynomial scale.  Replacing \(q_X\) by \(1\) or smoothing a hard face is unauthorized. |
| `nonsquare_and_full_divisor_controls` | Compare (137.B9) with (3.2), and test \(n=Dt^2\), \(D>1\) squarefree. | **Failure of completion and nonresonance.** The full identity is differently weighted and may pair signs that the truncation retains.  Nonsquares include exact phase-one families, although their raw mass is target-safe. |
| `phase_derivatives_and_resonant_dual_modes` | Use (3.3)--(3.6), keeping exact integer modes separate from near modes. | **No closure.** There are \(J/L\) dual modes, formal capacity \(\sqrt{JL}\), and no uniform Diophantine gap. |
| `one_dimensional_scalar_capacity` | Count \(L^2\) possible \(n\)'s with \(|B_L(n)|\ll\tau(n)\). | **Defect \(L^{1/2-o(1)}\).** Absolute values give \(L^{2+o(1)}\), versus target \(L^{3/2+o(1)}\). |
| `completion_bprocess_and_self_return` | Expand the additive transform as (3.8), then compute (3.9)--(3.10). | **Circular self-return.** Completion restores the hard cone; the B-process restores the reciprocal endpoint and a second pass returns the original critical relation. |
| `coefficient_directionality_and_phase_alignment` | Replace the literal coefficient only in the adversarial method control by (3.11). | **Coefficient-uniform route falsified.** Full \(\ell^1\) alignment is possible for an arbitrary array of the same magnitudes.  This is not a physical coefficient or lower bound. |
| `uniformity_in_L_and_X` | Use \(H\asymp\sqrt J\), \(L\ll H\), and centres in (3.6) with \(\nu=L^A\). | **Uniform obstruction.** The B-ledger loss \(H/L\) is unbounded, and exact modes occur at polynomial intermediate scales. |
| `boundary_and_owner_scope` | Preserve half-open \(\eta_L\), \(\lceil h/4\rceil\), \(H,y\), the real endpoint, zero extension, and \(n\ne\square\). | **Pass as scope, no estimate.** A completion or B-process needs a new boundary/crossing/remainder ledger; none is silently borrowed. |
| `full_hard_TOP_and_downstream_scope` | Restrict the conclusion to one nonsquare polynomial intermediate hard-TOP block. | **No closure.** Terminal, BAL, UNBAL, M9-M1, endpoint assembly, M9, and all global exponents are unchanged. |
| raw-vs-weighted / signed-vs-unsigned | Compare pair count, \(\tau(n)\), the literal profile mass, the full-divisor completion, and (3.11). | Raw counts do not prove a weighted lower or upper saving.  The signed theorem must identify a property that fails for absolute, random, and phase-adapted coefficients. |

# 6. Dependencies and exact artifacts used

This report used completely and only the statement-only artifacts permitted by the brief:

1. `problems/gauss_circle.md`;
2. `state/control_models.md`;
3. `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/blind_statement.md`;
4. `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/briefs/blind_truncated_chi4_divisor_phase_feasibility.md`.

No claim graph, proof draft, strategy file, Round-126--137 nonblind artifact, sibling report, web source, numerical experiment, or symbolic computation was read or used.  All calculations are exact arithmetic identities or analytical capacity ledgers derived from (137.B1)--(137.B11).

# 7. Recommended state effect

Recommend **retain the target open and record `product_fibre_no_go`; make no downstream proof-state change.**

Retain as exact candidate evidence:

* the product-fibre bijection and literal transform identity;
* the one-term truncated-divisor controls (3.1) and the failure of the full-divisor identity to control the truncation;
* the exact integer-mode formulas (3.3), real-centre tuning (3.6), and target-safe nonsquare resonance family (3.7);
* the exact additive-transform return (3.8) and phase/canonical self-return (3.9)--(3.10);
* the quantitative dual capacity \(\sqrt{JL}=L^{3/2}(H/L)\).

Do not promote a target bound, a strict product-fibre reduction, a full-divisor completion, or a derivative estimate with arbitrary divisor-bounded coefficients.  A valid continuation must prove a genuinely new owner-preserving estimate for the literal additive transforms (4.1), using the actual truncated \(\chi_4\)-divisor structure and all hard profiles, with an effective gain of \(L^{1/2-o(1)}\).  Re-expanding that estimate to (3.8), taking a positive energy, or applying a second B-process is not a smaller survivor.

The nonsquare hard-TOP scalar, its parent hard-TOP owner, and every downstream obligation remain open.
