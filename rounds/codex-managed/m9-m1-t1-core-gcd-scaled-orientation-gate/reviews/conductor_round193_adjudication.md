# Conductor Round 193 adjudication

- Campaign: `m9-m1-t1-core-gcd-scaled-orientation-gate`
- Round: 193
- Starting graph SHA-256:
  `7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9`
- Formal candidate SHA-256:
  `274347e39b44a9dffed4c828b199735d544006f0bea17cbe17b124152955f0fd`
- Durable kernel SHA-256:
  `470620b5171fd5055991c397b99e8b00c4400cc518e2bf2b9bd92c792ce53b83`
- Closing label: `strict_rho_large_gcd_scaled_orientation_sector`
- Numerical theorem evidence: none

## 1. Result and conductor decision

Round 193 closes with one proved subordinate hard-M1 \(t=1\) sector and
no estimate for the complete Round-192 core.

On the exact opposing physical source, put

\[
 g=(d,d'),\qquad D_L=\lceil L^{1/2}\rceil,
\]

\[
 P_{\rm cl}=
 \mathbf1_{|d-gm|\le D_L}
 \mathbf1_{|d'-gm'|\le D_L}.
\]

The mask is imposed before Fourier expansion and height differencing.  The
accepted core operator is rerun on this masked source.  Uniformly in every
nonempty dyadic \(Y>H_B\), both signs, and both opposing orientations,

\[
 \boxed{
 |\mathscr R_{{\rm core},Y,H_B}^{\sigma}(P_{\rm cl}W)|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon .}
\]

This is stronger than the launch target: neither \((m,m')=1\) nor
\(r\equiv2\pmod4\) is needed for the estimate.  Those hypotheses are used
only for a subsidiary scaled-orientation involution.

## 2. Absolute incidence proof

In the plus primitive chart,

\[
 d=\kappa gU,\quad d'=g(\kappa U+2S),\quad
 m'=\kappa v,\quad m=\kappa v+2w,
\]

\[
 h=Sv-Uw>0,\qquad r=2\kappa gh<R_0.
\]

The two close inequalities give

\[
 S+w\le D_L/g,
 \qquad |\kappa(U-v)|\le3D_L/g.
\]

The literal hard cone and \(m\asymp L\) force \(g\le G_0\) uniformly for
all \(L\ge2\).  For fixed \((\kappa,g,U,v,w)\), positivity and the shift
bound confine \(S\) to

\[
 {Uw\over v}<S<{Uw\over v}+{R_0\over2\kappa gv}.
\]

Since \(\kappa v\asymp L\), there are \(O(1)\) choices of \(S\).  Including
every small-variable term,

\[
 \#\mathcal I_{{\rm cl},+}
 \ll\sum_{\kappa\ll L}
 (1+L/\kappa)(1+D_L/\kappa)(1+D_L)
 \ll LD_L\log(2L)+LD_L^2.
\]

The minus chart has the same count.  The dyadic height is determined by the
determinant and contributes no multiplicity.  At
\(D_L=\lceil\sqrt L\rceil\), the total physical count is \(O(L^2)\), and
the actual pointwise coefficient bound supplies only \(X^\varepsilon\).

For every explicit width \(1\le D\le L\), the same proof costs

\[
 O_\varepsilon((LD\log(2L)+LD^2)X^\varepsilon).
\]

Thus the absolute mechanism loses \(L^{2\delta}\) at
\(D=L^{1/2+\delta}\); this is a method boundary, not a lower-mass theorem.

## 3. Exact masked-core passage

Bracket notation means

\[
 \mathscr R_{\rm core}[P]=\mathscr R_{\rm core}(PW).
\]

It never means multiplication of an already formed Abel jump.  On a
transported common affine site, the exact product rule is

\[
\begin{aligned}
 &P_h(t)B_h(t)-\chi P_{h-1}(t+\nu)B_{h-1}(t+\nu)\\
 &=P_h(t)\{B_h(t)-\chi B_{h-1}(t+\nu)\}\\
 &\quad+\chi\{P_h(t)-P_{h-1}(t+\nu)\}B_{h-1}(t+\nu).
\end{aligned}
\]

The mask commutator remains in the new core; unmatched sites remain births
and deaths.  The Round-187 conductor, Round-188 imprimitive lift, Round-189
projective, Round-191 inverse/terminal/Fejer, and Round-192 Farey safe
proofs are stable when rerun on the deleted physical input.  Therefore

\[
 |\mathscr S_{\le192}(P_{\rm cl}W)|
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon,
\]

and exact linearity gives

\[
 \mathscr R_{\rm core}(P_{\rm cl}W)
 =\mathscr H(P_{\rm cl}W)
  -\mathscr S_{\le192}(P_{\rm cl}W).
\]

The \(T=0\) branch is literal: the Round-192 Farey projector is zero and
the inherited rho-large remainder is present in full before the Round-193
split.

## 4. Subsidiary involution and exact complement

On \((m,m')=1\), even \(r\) forces \(m,m'\) odd and

\[
 \tau_g(d,m,d',m')=(gm,d/g,gm',d'/g)
\]

is an exact fixed-point-free involution.  It preserves the endpoint
products, shift, phase, Fejer weight, recomputed divisor gcd \(g\), and
cofactor gcd one; it swaps the plus and minus primitive charts by

\[
 (U,v,S,w)\mapsto(v,U,w,S).
\]

For \(r\equiv2\pmod4\), it reverses the \(\chi_4\) product.  This identity
is used only after complete Fourier recombination.  Its coefficient bracket
contains two unrelated actual endpoint products, so character reversal alone
does not estimate arbitrary bounded arrays.

The remaining core is exactly and disjointly

\[
 P_1=\mathbf1_{|d-gm|>D_L},
\qquad
 P_2=\mathbf1_{|d-gm|\le D_L}
      \mathbf1_{|d'-gm'|>D_L}.
\]

Neither \(\mathscr R_{\rm core}(P_1W)\) nor
\(\mathscr R_{\rm core}(P_2W)\) is estimated in this round.

## 5. Independent review and provenance

The discovery and hostile reports independently derived the stronger
absolute sector, the determinant count, the operator restriction, and the
same first-failure complement.  The formal candidate was repaired at the
affine-site mask seam, the uniform \(g\)-bound, every \((1+)\) count term,
the general-width range, the exact Round-192 interface, paired-domain and
phase notation, smooth/BV separation, provenance typing, and TeX/path
hygiene.  Terminal candidate reviews pass at the candidate hash above.

The statement-only report independently rederived the finite involution,
character sign, primitive coordinate map, exact close lattice, determinant
window, and arbitrary-coefficient no-go.  Its provenance is explicitly
qualified: its author had prior through-Round-192 proof-status context, but
received no Round-193 claimant, strategy, candidate, review, control, graph,
or campaign content and used only `protocol.md` and `blind_statement.md` in
that derivation.  The blind post-unmask and final-kernel scope reviews find
no mathematical mismatch.  This qualified artifact is not a premise of the
principal absolute theorem, which has two independent selected-context
proofs plus count/operator and kernel reviews.

The durable kernel is
`proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md`.
Its final count/operator, formalization/provenance, and blind/scope reviews
pass at the durable hash above.  The finite Wolfram control has zero recorded
identity failures and remains diagnostic only.

## 6. Dependencies and downstream scope

The new subordinate node depends directly only on
`M9-M1-hard-top-t1-rho-large-farey-covector-reduction`.  The Round-185
multiplicity-one physical chart is explicit transitive interface provenance.
The earlier accepted connectors are reopened only for deletion stability and
are not enlarged.

The complete Round-192 core, complete original \(t=1\), every original
\(t\ge2\) range, the remaining hard small-\(t\) owner, the independent smooth
M1 parent, GAR, every M2 parent, endpoint uniformity, M9, both bridges, and
the quarter target remain open or conditional.

The strongest internally proved exponent remains \(1/3\).  The accepted
external benchmark remains
\(0.3144831759740614\ldots\).  The target remains \(1/4\).

## 7. State decision

Create one proved-internal subordinate gcd-scaled double-close sector.  Add
it only as a dependency and inconclusive evidence item to the still-open
hard-M1 high-radical small-\(t\) owner.  Narrow that owner's next action to
the exact \(P_1\) and \(P_2\) complements while preserving the literal
\(T=0/T\ge1\) branches and every inherited field.

Reject post-Abel mask commutation, Fourier-mode ownership of the mask, a
hidden \(Y\) multiplicity, \(D\) choices for \(S\) after the determinant,
growing \(g\), use of cofactor coprimality or \(r\equiv2\pmod4\) in the raw
count, reliance on character or selector invariance for the absolute bound,
free width beyond \(\sqrt L\), canonical involution for cofactor gcd greater
than one, modewise pairing, lower-mass inference, complete-core closure, and
any exponent inference.

Round 193 closes under exactly
`strict_rho_large_gcd_scaled_orientation_sector`.
