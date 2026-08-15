# Hostile endpoint scope review

Campaign: `m9-endpoint-kernel-validation`  
Task: `hostile_endpoint_scope_review`  
Role: hostile seam reviewer  
Graph SHA-256: `90f44e99047eff10b620228e8480a88984f9dbbca4445bb8921667d9d3575031`

## 1. Result

**Verdict: partial validation after two material scope corrections.**

The fixed-profile sine calculation does prove a \(D/L\) average for a
**fixed, one-sign spatial subprofile** \(W\mathbf 1_J\), separately for each
residue class and one side of the first annulus, provided that this subprofile
stays a fixed distance inside the active denominator endpoint and the
frequency block contains a uniformly positive odd-frequency interior.  It
does **not** prove the displayed assertion for the whole class subtotal
\(P_c\) when a real fixed profile changes sign, and it does not by itself
cover the moving hard cutoff \(d\leq\lfloor\sqrt X\rfloor\) of the top
endpoint block.  The existence point in \(X\) may also differ between the two
classes.

The exact-square identity and the local square-to-first-annulus transition
are correct after requiring an admissible support point \(u_0\) (in
particular \(D=N/u_0\) must be an active endpoint scale), a nonterminal
frequency block \(L\leq cH\), and either frozen height or the elementary
one-unit height-rounding stability.  They are local-window statements only.
They give no lower bound for the complementary denominators or for the full
signed block.

The dual product-energy, square, near-square, even-product, and large-gcd
reductions have the claimed scales for a bounded balanced symbol.  The
quarter-packet identity is exact only after specifying a fixed smooth dyadic
partition in the gcd and a uniformly smooth interior symbol family.  This
does not automatically include the single hard endpoint profile.  The
boxed shellwise estimate (6.9), with \(\sum_G G|\mathcal Q_G|\), is **not
shown to be weaker** than the character-erasing mean square: shellwise
absolute values impose extra cancellation requirements.  The version with
one absolute value outside \(\sum_G G\mathcal Q_G\) is genuinely weaker than
that mean square, but it is simply exactly equivalent to the remaining
small-gcd part of the original signed target.

Accordingly, no endpoint range and no part of `M9-M2` is closed by these
artifacts.

## 2. First false or doubtful lines

The first overstatement is
`endpoint_sine_kernel_attack.md:7-9`: “for every fixed nonzero smooth
profile, each one-sided first annulus in either congruence class has average
and occasional size \(\gg D/L\).”  The proof at (2.5) establishes this only
for \(P_{c,J}\), where \(J\Subset(a,b)\) is a chosen interval on which \(W\)
has one sign.  For a sign-changing \(W\), the contributions of two such
intervals can cancel in \(P_c\); the argument supplies no inequality from
\(|P_{c,J}|\) to \(|P_c|\).  If “subtotal” is understood to mean precisely
the additionally localized \(P_{c,J}\), the line becomes correct after the
endpoint-margin hypothesis below is added.

The first endpoint-support gap is at the same lemma.  Its cell count treats
all \(d\) in the fixed profile while the actual top block has
\(d\leq\sqrt X\).  Intersecting with that cutoff preserves a \(Y/L\) measure
only when the selected \(J\) leaves a fixed active margin.  A profile slice
concentrated at the moving endpoint need not have the asserted
\(Y\)-length supply of cells.  Thus Lemma A is not, as written, a validation
of the single hard endpoint seam.

For Lemma B, `endpoint_sine_kernel_attack.md:101-103` chooses \(u_0\) merely
“in the upper half of the support.”  For the abstract hypothesis
\(W\in C_c^\infty((a,b))\), this does not ensure that \(D=N/u_0\) is an
active scale.  For example, the project restriction \(D\leq\sqrt X\) at
\(X=4N^2+O(N)\) requires \(u_0\geq 1/2+o(1)\).  The actual dyadic profile may
give a stronger condition, but it must be stated rather than inferred from
“upper half.”

The first doubtful dual line is
`endpoint_dual_signed_attack.md:89-100`, where the actual symbol is called a
fixed \(A(h/L,k/L)\) with fixed normalized derivative bounds.  What is
needed is a **uniform family** in the parameters \(L/H\) and \(c_D\), plus a
smooth real extension in the gcd variable.  The Round-6 conductor audit
also records one hard endpoint jump; that block is not a compactly supported
smooth \(A\) and is outside the Poisson packet until it is split off or
separately transformed.

Finally, `endpoint_dual_signed_attack.md:503-505` overstates the logical
strength of the boxed packet estimate.  The outside-absolute packet is
weaker than the mean square; the shellwise \(\ell^1\) estimate (6.9) need
not be.  The result paragraph also points to (7.5) as the signed
alternating-shift successor, but (7.5) is the explicitly rejected absolute
version; the intended signed statement is (7.4).

After these statement repairs, the first genuinely unproved analytic step
is cancellation of the omitted sine-kernel pieces, equivalently on the
smooth dual side the outside-absolute small-gcd packet estimate.  None of
the validated preliminary reductions supplies that cancellation.

## 3. Exact surviving statements and derivations

### 3.1 Localized fixed-profile annulus lemma

Let \(D\asymp Y^{1/2}\), let \(L_0\leq L\leq H/4\), and let
\(J\Subset(a,b)\) satisfy

\[
  W|_J\text{ has one sign},\qquad |W(u)|\geq w_0>0.
\]

Require that the sampled denominators \(d/D\in J\) are active for an
\(X\)-interval of length \(\gg Y\).  Without a moving endpoint this is
automatic.  With \(d\leq\sqrt X\), it follows, for example, if
\(D\sup J\leq(\sqrt2-\eta)Y^{1/2}\) for fixed \(\eta>0\).  Also require the
odd-frequency interior mass

\[
 \sum_{\substack{h\asymp L\ 
                  h\ {m odd}\
                  v_L(h)=1}}
 \frac{\Phi(h/(H+1))}{h}\gg 1.
\]

This is automatic for the usual scaled block once \(L\geq L_0\), with
\(L_0\) fixed, and \(L\leq H/4\).  Then for each \(c\in\{1,3\}\), the
positive-side subtotal \(P_{c,J}\) in (2.4) satisfies

\[
 \frac1Y\int_Y^{2Y}|P_{c,J}(X)|\,dX\gg_{W,J,\eta}\frac DL.
\]

Indeed, on \(1/(8L)\leq t\leq1/(6L)\), all retained sine factors are
positive and the actual Vaaler factor obeys
\(\Phi(h/(H+1))\geq\Phi(1/2)=1/2\); hence
\(K_{L,H}(t)\gg1\).  For fixed \(d\), cells of one residue class recur every
\(4d\), and the favorable part of each cell has length \(\asymp d/L\).
The active-margin hypothesis leaves \(\asymp Y/d\) cells, hence total
measure \(\gg Y/L\).  There are \(\gg D\) sampled \(d\)'s in \(J\), and
all their retained terms have the same sign.  Termwise integration gives
the claim.  The negative side follows with the opposite fixed sine sign.

This proves existence of an \(X_c\) for each class, not one common \(X\),
and it concerns \(P_{c,J}\), not \(P_c\) or \(B_L\).

### 3.2 Square/near-square local transition

Let \(X_\tau=4N^2+\tau N\), \(d=N+m\), and choose an actual support point
\(u_0\) for which \(D=N/u_0\) is active.  Let
\(L_0\leq L\leq cH\asymp c\sqrt N\), with \(c\) small enough that the
frequency support remains away from the Vaaler cutoff.  Then

\[
 \frac{hX_\tau}{4(N+m)}
 =h(N-m)+h\left(\frac{m^2}{N+m}
                  +\frac{\tau N}{4(N+m)}\right)
\]

is exact.  On \(|m|\leq\eta\sqrt{N/L}\), the \(\tau=0\) phase is
\(O(1/L)\) from zero.  The \(\chi_4(h)\)-twisted geometric sums stay a
fixed distance from integer frequency, so Abel summation with the actual
\(\Phi/h\) amplitude gives \(G_{L,H}=O(1/L)\), and the local sum is
\(O(\sqrt N/L^{3/2})\).

For \(\tau=1+s/L\), fixed suitable \(s>0\), one has

\[
 z_{1+s/L}(m)-\frac14
 =\frac{m^2}{N+m}+\frac{(s/L)N-m}{4(N+m)}
 \asymp \frac1L
\]

uniformly in that window after \(\eta\) is chosen small.  The exact identity
\(\chi_4(h)\cos(2\pi h(1/4+u))=-\sin(2\pi hu)\) for odd \(h\) then makes all
interior frequency terms have one sign and yields a local contribution
\(\asymp\sqrt{N/L}\).

If the actual integer height changes by one between the two nearby values of
\(X\), the restriction \(L\leq cH\) keeps the block support away from the
truncation.  Moreover the change in each \(\Phi(h/(H+1))/h\) coefficient is
\(O(H^{-2})\), so the whole kernel changes by \(O(L/H^2)=o(1)\).  Thus
height rounding is harmless in this scoped nonterminal statement.  None of
this controls the complement \(|d-N|>\eta\sqrt{N/L}\).

### 3.3 Why the subtotals do not lower-bound the signed block

Both reports are correct on this seam.  The exact decompositions have the
form \(B_L=P+R\), where \(P\) is one selected class/side/window and \(R\)
contains the other side, class, annuli, and denominators.  No proved sign,
orthogonality, or amplitude-preserving involution controls \(R\).  Therefore
\(|P|\gg D/L\) gives no inequality for \(|B_L|\).  This is a logical scope
barrier, not a theorem that the complementary terms actually cancel.

### 3.4 Dual reductions and exact packet scope

For a bounded balanced symbol, the parametrization

\[
 h_1=ga,\quad h_2=gb,\quad k_1=bt,\quad k_2=at,
 \qquad (a,b)=1,
\]

validates \(\sum_m r_L(m)^2\ll L^2\log(2L)\).  Writing a square product as
\(h=su^2,k=sv^2\) validates the \(O(L\log L)\) square count, and the
interval around each \(n^2\) validates
\(O_\varepsilon((L^2\eta+L)L^\varepsilon)\) near-squares.  These arguments
retain actual amplitudes by bounded majorization only.

For odd products, (5.2)--(5.3) is exact.  For even products, surviving
\(h\)'s are odd and their complements \(k=m/h\) are even, so the swapped
term has \(\chi_4(k)=0\); there is no missing complementary cancellation.
For \(g=(h,k)\geq L^{1/2}\), direct counting gives
\(\sum |a(h,k)|\ll L^{3/2}\), so the large-gcd cutoff is valid and already
at target scale.

For the small-gcd part, choose once and for all a smooth dyadic partition
\(\sum_G\psi(g/G)=1\).  Assume the interior actual symbols form a uniformly
compactly supported \(C^B\) family for the fixed finite \(B\) required by
Poisson decay.  For fixed coprime \(a,b\), define the resulting smooth
profile \(F_{a,b,G}\) including \(\psi\) and the actual symbol.  Since
surviving \(h=ga\) is odd, \(g,a\) are odd and
\(\chi_4(h)=\chi_4(g)\chi_4(a)\).  Poisson summation then gives exactly the
difference of the \(1/4\)- and \(3/4\)-packets in (6.5), including the case
of even \(b\).  Thus

\[
 \mathcal T_{\rm small}
 =\frac1{2i}\sum_{G<L^{1/2}}G\mathcal Q_G(R)
\]

for that fixed partition, up to only the already separated boundary shell.
Consequently

\[
 \left|\sum_{G<L^{1/2}}G\mathcal Q_G(R)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon
\]

is exactly the remaining small-gcd signed target.  It follows from the
character-erasing mean-square target by Cauchy, so it is a weaker sufficient
condition than that mean square.  In contrast,
\(\sum_GG|\mathcal Q_G|\ll L^{3/2}X^\varepsilon\) is a stronger shellwise
variant and should not be advertised as logically weaker.

The dual report works with positive frequencies.  Transfer back to the full
two-sided M2 block additionally uses that the actual denominator profile and
Vaaler coefficients are real and \(\beta_{-h}=\beta_h\): the negative
frequency block is then the complex conjugate of the positive one.  This
conjugacy should be stated wherever the packet is used.  It fails for a
generic complex symbol, so the packet reduction must remain attached to the
actual real profile and cannot certify an arbitrary-coefficient analogue.

## 4. Controls and outcomes

1. **Actual Vaaler amplitudes:** pass after scoping.  The annulus and local
   transition use \(\Phi(h/(H+1))/h\), not constant surrogate weights.
2. **Both frequency signs:** pass for the sine formula.  The dual packet is
   a positive-frequency reduction and needs the explicit real-even
   conjugacy just stated.
3. **Nearest-odd cells and ties:** pass.  Fixed-class cells recur every
   \(4d\); ties are a measure-zero set in the \(X\)-average.  Positive and
   negative sides are separate subtotals.
4. **Endpoint support:** fail as an unconditional claim in Lemma A; pass only
   for a fixed active interior slice.  Lemma B is endpoint-safe after the
   admissible \(u_0\) condition.  The hard top profile remains separate.
5. **Fixed versus adversarial profiles:** pass only in the localized sense.
   The interval \(J\) is fixed once from \(W\), not chosen as a function of
   \(X\), but its subtotal is not the whole profile.
6. **Exact square versus uniform real \(X\):** pass.  The two nearby values
   prove non-uniformity of the local pattern and no global estimate.
7. **Even products:** pass.  They are included in the gcd packet through
   even \(b\), and complementary-divisor pairing is correctly unavailable.
8. **Large gcd:** pass at \(O(L^{3/2})\) for bounded symbols.
9. **Smooth-symbol hypothesis:** conditional.  Uniform \(C^B\) interior
   profiles and a smooth gcd partition suffice; the single hard endpoint
   jump is not covered.
10. **Proves-too-much:** pass after correction.  No subtotal becomes a full
    signed lower bound, and the packet retains \(\chi_4(a)\), the two packet
    signs, and the actual kernels.  A version uniform over arbitrary complex
    or parameter-adapted coefficients is not licensed.
11. **Computation:** none used.

## 5. Dependencies and exact artifacts used

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-endpoint-kernel-validation/briefs/hostile_endpoint_scope_review.md`
- `rounds/codex-managed/m9-endpoint-fixed-profile-attack/reports/endpoint_sine_kernel_attack.md`
- `rounds/codex-managed/m9-endpoint-fixed-profile-attack/reports/endpoint_dual_signed_attack.md`
- `rounds/codex-managed/m9-endpoint-fixed-profile-attack/reviews/conductor_source_and_seam_audit.md`

No external theorem is imported and no numerical artifact is used.  The
primary-source claims in the dual report were not needed for the surviving
scope statements above.

## 6. Recommended state effect

- **Retain, sharply revised:** the classwise annulus result only for the
  fixed one-sign, endpoint-interior subtotal \(P_{c,J}\), with separate
  existence points for the two classes.  Do not promote a claim about the
  whole \(P_c\) for arbitrary real nonzero \(W\).
- **Retain, sharply revised:** the square/near-square local transition with
  admissible \(u_0\), nonterminal \(L\leq cH\), and explicit local-window
  scope.  Promote at most its exact algebraic identity and scoped local
  bounds; it has no implication to the full signed block.
- **Retain as scoped reductions:** product energy, square and near-square
  counts, complementary-divisor parity, and the large-gcd absolute bound.
- **Revise the packet candidate:** use a fixed smooth gcd partition and the
  outside-absolute estimate as the exact remaining small-gcd interface.
  Keep the shellwise \(\ell^1\) version as an optional stronger target, not
  as a weaker replacement for the mean square.
- **Retain the alternating-shift backup as (7.4), not (7.5).**
- **No change:** `M9-M2-dyadic-weight-nondegeneracy`,
  `M9-endpoint-uniformity`, `M9-M2`, `M9`, or the Gauss-circle target.  The
  moving hard endpoint profile and the signed small-gcd aggregate remain
  open.
