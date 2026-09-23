# Signed-inverse normalization, transport, and power post-repair verification

- Campaign: `m9-m1-t1-fast-height-jump-coboundary-gate`
- Round: 191
- Candidate SHA-256 reviewed:
  `263d17eea2f9e98efd1b145ef93b0c7ac84de437493acc359029043e1d442925`
- Review role: post-repair normalization, transport, source-coverage,
  projection, and power-ledger replay
- Verdict: **PASS**

## 1. Result

**PASS.** The repaired candidate satisfies every required repair from the
normalization seam review.  The positivity and support quantifiers, both
saturation cases, the disjoint power-of-two packet typing, the complete
outer-mask and endpoint source partition, the exactly gated complex
projections, the inherited linear outer assembly, the exact \(m^{-1}\)
lift, the fresh-epsilon ledger, and the bounded-\(W\) capacity statement
are now explicit and mutually consistent.

The proved result remains deliberately scoped.  Equations
(191.C5)--(191.C11) give a target-safe strict inverse sector, two
target-safe linear projections on its complement, and an exact global
safe/remainder decomposition.  The estimate (191.C12) for the complete
signed remainder is not proved.  No target-safe term has been
improperly separated from a signed packet: the three safe pieces are
exact linear restrictions or projections and are bounded absolutely
before their exact complex subtraction, while every undisplayed source
stays in one signed remainder with both orientations and one final real
part.

## 2. Exact statement and hypotheses

The repaired statement now quantifies real \(X\ge2\), a nonempty
inherited residual hard-M1 shell \(L\ge2\),
\(\sigma\in\{+1,-1\}\), fixed \(B>0\), and
\(Q=\lfloor(\log(2X))^B\rfloor\).  It explicitly makes
\(\kappa,g,u,v,m,q,h\) positive integers and imposes
\(1\le a<q\), \((a,q)=1\), the full fast-packet conditions
(191.C2)--(191.C3), and on nonzero support

\[
 u\asymp v\asymp L/\kappa,\qquad
 \operatorname{length}(\mathcal V_{\rm lit})\ll u,
 \qquad L\ll X^{1/4}.
\]

All inherited literal fields are retained.  If
\(T_Q=(q-1)/2\), the strict projective condition is impossible and the
packet is explicitly vacuous.  Otherwise the conditions
\(J=2^r\), \(J\le j_q(a,v)<2J\) form a disjoint half-open partition,
with the last band truncated by the intrinsic upper cap.  At the
inverse cut, \(T_\varrho=0\) makes the strict sector empty, while
\(T_\varrho=(U-1)/2\) includes every unit inverse class and makes its
row complement empty.

The two type levels are now separate.  Equation (191.C13a) defines the
fixed
\((\kappa,u,m,q,a,J,\sigma)\) complex packet.  Equations
(191.C28a)--(191.C28d) define its fixed safe and remainder pieces.
Equations (191.C32a)--(191.C32b) then apply the inherited linear outer
assembly to the disjoint family of fixed packets, including all outer
labels and \(m^{-1}c_q(a)\), to define the global quantities in
(191.C10)--(191.C12).  Thus no fixed packet is equated with a global
aggregate.

## 3. Proof and derivation replay

The signed-inverse transport remains exact.  From
\(\varrho v-\gamma U=1\), the map
\((S,w)\mapsto(S-\epsilon_\omega\varrho,
w-\epsilon_\omega\gamma)\) lowers either oriented determinant fibre by
one.  The canonical-anchor difference is an integral multiple
\(\nu_\omega(h)U\), with
\(\nu_\omega(h)\in\{-1,0,1\}\), and gives the exact affine reindexing
(191.C19)--(191.C20).  Formula (191.C20a) correctly retains the carry
and mode factor
\((-1)^{\nu_\omega(h)}e(\epsilon_\omega a\varrho/q)\); it does not
replace it inside the fast projector by the full-anchor parity
\((-1)^\varrho\).

The source partition is now complete.  For binary \(K_h,K_-,G_h,G_-\),
(191.C22d) separately assigns live-side \(K\)-birth/death, common-\(K\)
\(G\)-birth/death, and only then the persistent
\(K_h=K_-=G_h=G_-=1\) difference.  The case with both \(K\)'s zero
vanishes.  Hence simultaneous outer-mask changes are neither omitted
nor duplicated.  The transported common/birth/death partition
(191.C23) is a disjoint identity.  The four-term telescope (191.C24)
is exact, and (191.C24a) now applies the ordered, conjugated two-factor
product rule

\[
 (\lambda_{1,h}-\lambda_{1,-}^{\rm tr})
 \overline{\lambda_{0,h}}
 +\lambda_{1,-}^{\rm tr}
 (\overline{\lambda_{0,h}}
  -\overline{\lambda_{0,-}^{\rm tr}}).
\]

Equation (191.C25) is then applied separately to both endpoints, with
the lower endpoint conjugated.  The ordered list (191.C25a) now includes
the original shell/height branch, strict ratio cone, inherited selector,
profile support/branch, floor, star, half-weight, hard sample, real-
\(X\) crossing, endpoint trace, and endpoint zero extension.  It
distinguishes the profile label from its numerical value and assigns
simultaneous changes to the first differing field.  Together with the
arithmetic mask, positivity, outer masks, Fejer term, and phase already
partitioned elsewhere, this covers every named source exactly once.

For the strict inverse sector, inversion permutes the unit classes, so
there are at most \(2T_\varrho\) admissible inverse classes.  Since
\(U\mid u\) and the literal \(v\)-support has total length \(O(u)\),
each class occurs \(O(u/U+1)=O(u/U)\) times.  Thus

\[
 \#v_{\rm inv}\ll \frac{uT_\varrho}{U}
 \ll \frac{Qmu}{Y}.
\]

The exact inverse Abel identity (191.C15) is applied before positive
counting.  Multiplying by \(O(Y)\) heights, \(O(\kappa)\) sites, and the
endpoint allowance gives (191.C28) with no \(q/J\) loss.  This proves
the strict sector as a cardinality bound; the transport canonicalizes
the cut but does not claim cancellation on its complement.

The projection gates are also exact.  Equation (191.C28a) is precisely
the live-side terminal atom.  Equation (191.C28b) keeps the fast band,
the large-inverse complement, both orientations, the Abel factor, and
the terminal atom.  Equation (191.C28c) keeps the same row gates and in
addition requires common \(K,G\), transported-common \(t\), and exactly
the Fejer summand from (191.C24).  Equation (191.C28d) forms the three
joint complex projections before a modulus and defines the remainder
by complex subtraction.  Therefore the terminal and Fejer estimates
(191.C30) and (191.C32) use only absolute bounds on already defined
linear components.  Coprimality flips, affine births/deaths, carry,
endpoint changes, literal changes, and phase changes remain signed in
the complement.

The global typing and power ledger close.  The exact inherited linear
operator in (191.C32a)--(191.C32b) sums the disjoint \(J\)-bands and all
outer weights before the final real part, so linearity applied to
(191.C28d) proves (191.C11).  The lift

\[
 c_{mq}(ma)=m^{-1}c_q(a)
\]

cancels the \(m\) in the fixed \(Qm\kappa u\) bound before positive
outer summation.  The \(a\)-mass is logarithmic, the dyadic partition
costs one logarithm, and \(u=mqr\) gives
\(\sum_{mq\mid u}1\le\tau_3(u)\).  With a fresh local
\(0<\eta<\varepsilon\), (191.C35) absorbs only fixed polylogarithms and
divisor growth into \(X^{\varepsilon-\eta}\), using
\(L\ll X^{1/4}\); it absorbs no positive power of \(Y\).

Finally, (191.C38) is an exact bounded-array capacity identity.  Abel
reduces its left side to
\(\left|\sum_r\sum_{h\in H_r}W_r(h)z_r^h\right|\), which is at most
\(\sum_r|H_r|\).  The lawful zero-extended choice
\(W_r(h)=\overline z_r^{\,h}\mathbf1_{H_r}(h)\) makes every summand
positive and attains equality, including births, deaths, and holes.
The resulting no-go is correctly scoped to coefficient-uniform bounded
height arrays and separable positive control.  It is explicitly not a
realizability result, a lower bound for the literal coefficient, or a
disproof of (191.C12).

## 4. First doubtful or unproved step

No doubtful step remains in the repaired strict-sector reduction or
its normalization, transport, projection, and power seams.  The first
unproved step is exactly the one the candidate marks open: obtaining

\[
 \Re\mathscr R_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon
\]

for the complete large-inverse remainder.  That would require a signed
theorem coupling the carry, transported endpoint displacements,
literal masks, and square-root phases and supplying the missing
\(Y/(Qm)\) gain.  Neither the strict-sector count nor (191.C38) supplies
that theorem.  This open step is outside the claimed proved scope and
is not a repair defect.

## 5. Required control tests and outcomes

The replay is pinned to the current candidate SHA-256
`263d17eea2f9e98efd1b145ef93b0c7ac84de437493acc359029043e1d442925`;
the earlier dispatch hash was superseded by the stated metadata-only
candidate-status update.

The candidate's diagnostic paragraph agrees exactly with the prior
review: the ordinary-anchor/Abel control reports 470,029 exact checks
and 2,720 bounded-array capacity cases, while the signed-inverse control
reports 420,672 exact transport/parity checks and 1,325 inverse-class
counts, all with zero failures.  Both are still labelled diagnostic
only and are not used as asymptotic theorem evidence.

The current file passes the requested integrity checks: strict UTF-8
decoding succeeds; there are zero forbidden C0/DEL bytes and zero
replacement characters; all 53 display-math openings have matching
closings; all five `aligned` environments have matching endings; raw
unescaped braces balance 333 to 333; all 53 equation tags are unique;
every specifically required tag C22d, C24a, C25a, C28a--C28d,
C32a--C32b, and C38 is present; and the whitespace diff check is clean.
No TeX or control-byte defect was found.

## 6. Dependencies and exact artifacts used

This replay used exactly the two authorized artifacts:

1. `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/candidates/formalized_hard_m1_t1_fast_signed_inverse_transport_reduction.md`, at the SHA-256 recorded above;
2. `rounds/codex-managed/m9-m1-t1-fast-height-jump-coboundary-gate/reviews/signed_inverse_normalization_transport_power_seam_review.md`.

No unrelated proof, state, synthesis, validation, campaign, kernel, or
control artifact was opened.  No new numerical or symbolic experiment
was used; the only machine checks were bounded file-hash, encoding,
delimiter, tag, and whitespace diagnostics on the candidate itself.

## 7. Recommended state effect

**Promote**, at the candidate's exact narrow scope: the conductor may
create one subordinate `proved_internal` reduction node for
(191.C5)--(191.C11) and attach it as inconclusive evidence to the open
small-\(t\) owner.  Retain (191.C12), the rest of the \(t=1\) packet,
all \(t\ge2\) and large-\(G\) complements, every parent obligation, and
all exponents at their existing open or conditional status.  The
post-repair seam requires no further candidate repair.
