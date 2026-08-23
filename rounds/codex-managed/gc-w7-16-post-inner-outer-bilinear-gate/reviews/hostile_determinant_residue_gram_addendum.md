# Round 130 post-unmask hostile addendum: determinant residues are exact, but the resolved Gram is not \(G^2\)

Campaign: gc-w7-16-post-inner-outer-bilinear-gate
Task: outer_ray_bilinear_hostile_audit, bounded post-unmask review
Role: hostile seam reviewer
Starting graph SHA-256:
\(354f5ca462467d091a9a50c8dbc1173ffba56516963274f9fc232ea11890d20e\)
Status: candidate review evidence only; no shared proof state is changed.

## 1. Result

The conductor candidate has one correct algebraic kernel and one Gram
statement that requires a strict scope correction.

For a fixed outer primitive ray \(r=(a,b)\) on a fixed top-shell sign
stratum, the identities

\[
 n=ab'-a'b=aq-bp,\qquad
 b'={b(a+p)+n\over a},\qquad
 n\equiv-bp\pmod {|a|}
 \tag{130.A1}
\]

are exact.  If the literal \(p\)-support is a bounded union of intervals
of total length \(O(|a|)\), then each fixed integer \(n\) has \(O(1)\)
admissible \(p\)'s, and \(q\) is then forced.  This is per fixed \(r\),
after the Möbius expansion has been reassembled to the physical primitive
ray.  It is not a global multiplicity bound when \(r\) varies and is not
an orthogonality theorem.

The full random-cell identity

\[
 \mathcal C_i=x^*Gx,\qquad
 G_{rs}=(1-W|\lambda_r-\lambda_s|)_+,
 \quad \lambda_r={a_r\over\kappa_i b_r},
 \tag{130.A2}
\]

is exact, up to the harmless choice of conjugation in \(x\).  However,
the proposed shell- and orientation-resolved outer energy is not
\(x^*G^2x\).  Its exact positive object is

\[
 \boxed{\ \|K_{B,+}x\|_2^2=x^*K_{B,+}^*K_{B,+}x\ },
 \tag{130.A3}
\]

where \(K_{B,+}\) is the literal one-sided, inner-\(B\)-owned incidence
operator.  The identity \(x^*G^2x=\|Gx\|_2^2\) applies only after one
deliberately replaces the resolved row by the fully completed row \(Gx\).
Shell, opposite-orientation, cross-piece, and diagonal terms then occur,
and their cross terms have no proved sign.  Thus \(G^2\) is a valid
full-completion spectral control, not the exact post-inner Gram.

The determinant chart is consistent with the frozen same-denominator
resonances: those have \(q=0\), \(p=-t\) or \(p=-2j\), and hence
\(n=bt\) or \(n=2bj\).  They obey (130.A1) with multiplicity one and
show why bounded multiplicity does not itself create cancellation.

Verdict: certify the qualified determinant reindexing; replace the
proposed-row \(G^2\) language by the incidence Gram
\(K_{B,+}^*K_{B,+}\).  Top-eigenvector and support-aligned examples
remain coefficient-blind controls, not facts about the physical Vaaler
vector.  No scalar saving is proved.

## 2. Exact determinant statement, multiplicity, and hypotheses

### 2.1 Exact top-shell interval

Fix \(a,b>0\); the negative sign sector is identical after reversing the
appropriate inequalities and using \(|a|\).  Assume

\[
 a,a'=a+p\asymp L,\qquad b,b'=b+q\asymp D,\qquad
 {b\over W}=o(a).
 \tag{130.A4}
\]

The one-sided determinant inequalities are

\[
 0<aq-bp<{\kappa_i b(b+q)\over W}.
 \tag{130.A5}
\]

Before shell or support clipping, (130.A5) is the exact interval

\[
 {bp\over a}<q<
 {bp+\kappa_i b^2/W\over a-\kappa_i b/W}.
 \tag{130.A6}
\]

Its real length is

\[
 \Delta q
 ={\,\kappa_i b^2(a+p)\,\over
    W a(a-\kappa_i b/W)}
 \asymp {D^2\over WL}=Q_*.
 \tag{130.A7}
\]

Thus the candidate's \(Q_*\) scale is correct on an unclipped interior
piece.  Literally, after half-open shell, original support, cell, hard,
and star faces are imposed, only
\(\#\{q\}\ll1+Q_*\) follows; comparability requires a nonempty interior.
For fixed \(p\), the attained \(n=aq-bp\) values form one progression of
step \(|a|\), with numerical span \(O(|a|Q_*)\).

### 2.2 Exact bounded multiplicity

For fixed \(n\), (130.A1) gives

\[
 p\equiv -b^{-1}n\pmod {|a|},\qquad
 q={n+bp\over a}.
 \tag{130.A8}
\]

If \(\mathcal P_r\) is a bounded union of intervals of total length
\(O(|a|)\), then

\[
 \#\{p\in\mathcal P_r:p\equiv-b^{-1}n\pmod {|a|}\}=O(1).
 \tag{130.A9}
\]

All literal restrictions can only decrease this number.  Hence, for this
fixed outer ray,

\[
 \#\{(p,q)\ {\rm literal}\}\ll LQ_*,
 \qquad 0<n\ll {D^2\over W}\asymp LQ_*.
 \tag{130.A10}
\]

These are capacity upper bounds.  An asymptotic lattice area \(LQ_*\)
needs an interior lower count and does not follow from (130.A1) alone.
Three scope qualifications are mandatory:

1. (130.A9) fixes \(r=(a,b)\); the same \(n\) can have many
   representations when the outer ray varies.
2. The physical primitive incidence must be reassembled first.  At the
   Möbius-expanded level, the \(\rho\)-pieces are algebraic summands whose
   cancellation reconstructs primitivity, not independent determinant
   representations.
3. M1's \(\chi_4(b')\) and M2's \(\chi_4(a+p)\) become pullback weights
   through (130.A8), not automatically clean Dirichlet characters of
   \(n\).  “Residue twist” is safe only in this qualified sense.

Substitution into the carrier gives exactly

\[
 {cn\over\kappa_i bb'}
 ={can\over\kappa_i b\{b(a+p)+n\}},
 \tag{130.A11}
\]

so the candidate's phase formula is correct.

## 3. Exact post-inner incidence Gram and full completion

### 3.1 The resolved operator

Let \(\mathscr R\) be the physical ray set after lift, threshold, and
Möbius pieces are recombined, and put

\[
 \lambda_r={a_r\over\kappa_i b_r},\qquad
 x_r=\overline{A_i(r)}e(-c\lambda_r).
 \tag{130.A12}
\]

For a half-open inner shell \(B\), define

\[
 K_{B,+}(r,s)
 ={\bf1}^{\rm owner}_{s\in\mathscr R_B}
  {\bf1}_{0<\lambda_r-\lambda_s<1/W}
  \{1-W(\lambda_r-\lambda_s)\},
 \tag{130.A13}
\]

with the fixed block, sign, cell, support, and endpoint owners retained.
Then, up to the fixed conjugation convention,

\[
 F_{i,B}=K_{B,+}x,\qquad
 \sum_r|F_{i,B}(r)|^2
 =x^*K_{B,+}^*K_{B,+}x.
 \tag{130.A14}
\]

Expanding the Round-129 \(p,\rho,\eta,t,g,v\) formula gives a finer
coordinate realization of the same operator; it does not replace it by
\(G^2\).  Its positive diagonal is the new post-inner incidence
diagonal, not the original equal-ray \(n=0\) diagonal.

### 3.2 Exact scope of \(G\) and \(G^2\)

The full symmetric triangular kernel

\[
 G_{rs}=(1-W|\lambda_r-\lambda_s|)_+
 \tag{130.A15}
\]

is positive semidefinite by the random-cell Gram identity, and the
complete cluster energy is exactly \(x^*Gx\).  If
\(K_+=\sum_BK_{B,+}\), with every half-open shell assembled once, then

\[
 G=I+K_++K_+^*.
 \tag{130.A16}
\]

Therefore

\[
 \|Gx\|_2^2=x^*G^2x,\qquad
 x^*G^2x\le\|G\|\,x^*Gx.
 \tag{130.A17}
\]

These are rigorous full-completion statements.  They do not prove

\[
 K_{B,+}^*K_{B,+}\le G^2
 \tag{130.A18}
\]

in Loewner order or as quadratic forms.  Expanding
\(\|x+K_+x+K_+^*x\|_2^2\) produces the positive resolved energies plus
shell, orientation, diagonal, and mixed cross terms; the mixed terms can
have either sign.  The candidate's final caveat in Section 3 is sound,
but Sections 1 and 5 should use (130.A14), not call \(G^2\) the exact
dual of the proposed resolved energy.

### 3.3 Same-denominator resonance check

The frozen hostile controls lie inside the chart:

\[
\begin{array}{c|c|c|c}
 &q&p&n=aq-bp\\ \hline
 {\rm M1}&0&-t&bt\\
 {\rm M2}&0&-2j&2bj.
\end{array}
\tag{130.A19}
\]

For M1, \(c=mb\) gives \(e(cn/b^2)=e(mt)=1\).  For M2,
\(c=(4m+1)b\) gives
\(e(cn/(4b^2))=(-1)^j\), cancelled by
\(\chi_4(a)\chi_4(a-2j)=(-1)^j\).  Each \(n\) has one displayed
\(p\), so there is no conflict with (130.A9).  Bounded multiplicity
removes a fictitious second count but supplies no sign change.

## 4. First doubtful or unproved step

The first doubtful step is not (130.C1); its algebra and fixed-ray
multiplicity are valid.  It is the transition from the resolved physical
row to a full triangular completion.  Without a proved connector between
\(K_{B,+}^*K_{B,+}\) and \(G^2\), the spectral estimate for \(G\)
does not bound the target energy (130.C8).

The next unproved step is cancellation between “residue twists.”
Equations (130.A8) and (130.A19) make them actual weights on a
bounded-to-one chart, but no selected artifact proves an \(n\)-partial
sum with moving denominators, thresholds, and profiles retained.

Two candidate sentences also require downgrading:

- A top eigenvector of \(G\) saturates the spectral inequality, but need
  not satisfy the actual \(L^\infty\) bound, characters, sampled
  profiles, or threshold representation.  Without a delocalization
  check it is only a coefficient-blind control.
- The stated top-shell product-window return \(D^2/L\) is not the
  accepted complete product-window theorem in the selected context.
  That theorem is
  \[
   {D^2\over L^2}+{WD\over L}=Y^{37/48+o(1)}
  \]
  at the critical block.  If \(D^2/L\) is intended as a cruder
  post-inner outside-count capacity, its derivation and owners must be
  displayed and it must be labelled a control.

## 5. Control matrix and corruption audit

| Seam | Test | Outcome |
|---|---|---|
| determinant algebra | Recompute \(n=aq-bp\), (130.A1), and (130.A11). | **Pass exactly.** |
| fixed-\(n\) multiplicity | Solve for \(p\pmod {|a|}\), then force \(q\). | **Pass with scope.** \(O(1)\) only for fixed \(r\) and total \(p\)-length \(O(|a|)\). |
| \(q\)-window and area | Solve (130.A5) exactly. | **Revise.** \(Q_*\) is comparable only before clipping; \(LQ_*\) is a capacity, not an automatic asymptotic count. |
| Möbius multiplicity | Compare physical rays with separated \(\rho\)-pieces. | **Pass only after reassembly.** A positive split can lose the Möbius cancellation. |
| character residues | Pull \(\chi_4(b')\) and \(\chi_4(a+p)\) through the chart. | **Qualify.** They are induced weights, not proved complete characters of \(n\). |
| full random-cell Gram | Check (130.A2) and (130.A17). | **Pass.** Exact for the fully assembled cluster and full row. |
| resolved outer Gram | Compute the shell/orientation row. | **Correction required.** Exact object: \(K_{B,+}^*K_{B,+}\), not \(G^2\). |
| same-denominator resonance | Insert the two \(q=0\) families. | **Consistent obstruction.** Multiplicity one coexists with phase/character alignment. |
| top-eigenvector control | Test actual marginal and profile hypotheses. | **Coefficient-blind only.** Spectral saturation is rigorous; physical admissibility is not. |
| \(D^2/L\) scale | Compare with the accepted Round-117 theorem. | **Unverified as labelled.** Derive it as a crude control or use the accepted \(Y^{37/48}\) formula. |

The frozen hostile report also contained four mechanical TeX corruptions.
They did not alter its intended conclusions:

1. line 32 contained byte U+000B between “\(\ll_\)” and “arepsilon”;
2. line 353 contained the same U+000B corruption;
3. line 361 contained the same U+000B corruption; and
4. line 428, equation (130.H33), had
   “\(e\!\left({c\over4}left(\)” instead of
   “\(e\!\left({c\over4}\left(\)”.

The three U+000B bytes and the missing backslash have now been repaired
mechanically in the frozen report, under the conductor's explicit
post-unmask instruction.  No conclusion or mathematical wording was
changed.  No other ASCII control byte below U+0020 was found apart from
ordinary line endings, and no tab corruption was found.

## 6. Dependencies and exact artifacts used

This bounded post-unmask audit used only:

1. rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/candidates/conductor_determinant_residue_outer_gram.md;
2. rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/reports/outer_ray_bilinear_hostile_audit.md; and
3. the accepted formulas and scopes already quoted in those artifacts
   from the Round-117 and Round-129 context.

No sibling Round-130 report, numerical experiment, web source, or
external theorem was used.  The review was 100% analytical/algebraic.

## 7. Recommended state effect

Revise before any promotion.  The conductor may retain the qualified
fact that, for fixed top-shell outer \(r=(a,b)\), the physical map
\((p,q)\mapsto n=aq-bp\) is \(O(1)\)-to-one on a \(p\)-support of
total length \(O(|a|)\), while the determinant strip has clipped
\(q\)-length \(O(Q_*)\).

The full-completion control
\(x^*G^2x\le\|G\|x^*Gx\) may also be retained, explicitly labelled
coefficient-blind/full-row.  Replace every claim that \(G^2\) is the
exact proposed outer Gram by \(K_{B,+}^*K_{B,+}\), and do not infer a
comparison without a new connector.  Qualify “residue twists,” “lattice
area,” the top-eigenvector example, and the \(D^2/L\) sentence as above.

Make no change to the accepted \(Y^{35/48}\) fixed-block theorem, the
open \(Y^{1/2}\) scalar target, any global exponent, M9-M1, M9-M2,
endpoint uniformity, M9, the conditional bridge, or the quarter target.
