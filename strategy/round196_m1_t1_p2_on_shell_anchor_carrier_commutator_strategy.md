# Round 196 strategy: on-shell anchor-carrier commutator on the exact P2 remainder

## Frozen inherited region

Retain the exact accepted Round-192 core, the physical mask

\[
 P_2=\mathbf 1_{\{|d-gm|\le D_L\}}
     \mathbf 1_{\{|d'-gm'|>D_L\}},
 \qquad D_L=\lceil\sqrt L\rceil,
\]

and only the still-open Round-195 packet region

\[
 \mathcal P_{\rm rem}:
 \qquad \kappa<D_L,\qquad
 \min(Y,D_L)>Q\mathfrak m\kappa,
 \qquad Q=H_B.
\tag{196.S1}
\]

Both orientations, both frequency signs, the full anchor Fourier aggregate,
the \(T=0\) branch and every simultaneous strict \(T\ge1\) Farey condition,
actual endpoint products, residual selectors, squarefree and coprimality
masks, unequal translations, carries, Fejer factors, square-root phases,
cells, crossings, affine births and deaths, physical-mask commutators,
conjugations, and zero extensions remain under one outer real part.

The fixed-packet target is

\[
 \boxed{
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma
   (P_{2,<D}\mathbf1_{\mathcal P_{\rm rem}}W)|
 \ll_{B,C_0,\varepsilon}
 Q\mathfrak m\kappa uX^\varepsilon.}
\tag{196.S2}
\]

The accepted positive estimate is
\[
 u\{\kappa+\min(Y,D_L)\}X^\varepsilon,
\]
so the unresolved multiplier is
\(\min(Y,D_L)/(Q\mathfrak m\kappa)>1\).

## Exact on-shell carrier

Use the Round-195 positive far defects \(\eta_+,\eta_-\).  In the plus and
minus charts respectively,

\[
 2h=v\eta_+ +U\delta_+-\kappa(U^2-v^2),
\qquad
 2h=U\eta_- -v\delta_-+\kappa(U^2-v^2).
\tag{196.S3}
\]

Put

\[
 x_+=\kappa v+\eta_+=\kappa U+2S=\frac{d'}g,
\qquad
 x_-=\kappa v+\delta_-=\kappa U+2S=\frac d g.
\tag{196.S4}
\]

Thus both orientations use the same odd moving allocation coordinate
\(x=\kappa U+2S\).  Since \(U=\mathfrak m q\), \((v,q)=1\), and \(q\) is
odd, (196.S3) gives on shell

\[
 \bar v_qh\equiv\overline2_q(\eta_++\kappa v)\pmod q
 \quad(+),
\]
\[
 -\bar v_qh\equiv\overline2_q(\delta_-+\kappa v)\pmod q
 \quad(-).
\tag{196.S5}
\]

For both orientations
\[
 S=\frac{x-\kappa U}{2}.
\tag{196.S6}
\]
Consequently, for \(\epsilon_+=1,\epsilon_-=-1\),

\[
 \boxed{
 (-1)^S e\!\left(\frac{\epsilon_\omega a\bar v_qh}{q}\right)
 =\chi_4(\kappa U)\chi_4(x)
   e\!\left(\frac{a\overline2_qx}{q}\right).}
\tag{196.S7}
\]

If
\[
 b_{q,a}\equiv q+4a\overline2_q\pmod{4q},
\tag{196.S8}
\]
then \((b_{q,a},4q)=1\), and (196.S7) is a constant times the primitive
additive carrier \(e(b_{q,a}x/(4q))\).  Under \(x\mapsto x+2\), its ratio is

\[
 z_{q,a}=-e(a/q).
\tag{196.S9}
\]

The exact conductor coefficient is

\[
 c_q(a)=\frac{2}{q\{1+e(-a/q)\}},
\]
and therefore

\[
 \boxed{(1-z_{q,a})c_q(a)=\frac{2e(a/q)}q.}
\tag{196.S10}
\]

This identity is the sole new mechanism.  It suggests that an actual
step-two difference in the moving \(x\)-coordinate could cancel the
near-half-frequency singularity of \(c_q(a)\) before any positive norm.
Primitivity of the carrier alone is not a saving.

## Analytic program

1. Reconstruct the complete physical-to-core operator on
   \(P_{2,<D}\cap\mathcal P_{\rm rem}\), then prove (196.S4)--(196.S10)
   with every sign, parity, representative, and exact-conductor factor.
2. Reindex the recombined literal event aggregate by the common moving
   coordinate \(x=\kappa U+2S\).  Determine whether it has an exact form
   \(\Delta_2\mathcal B(x)=\mathcal B(x)-\mathcal B(x-2)\), plus an
   explicitly priced commutator remainder.
3. Apply (196.S10) only to the genuine \(\Delta_2\) term.  Keep the actual
   endpoint, square-root, Fejer, residual, carry, birth/death,
   physical-mask, and zero-extension differences in the commutator.
4. Prove (196.S2), prove a nonempty exact target-safe strict sector with one
   exact complement, or prove that the difference decomposition self-returns
   because a named literal commutator has the full unresolved capacity.
5. Restore the \(\mathfrak m^{-1}\) lift, exact-conductor coefficient mass,
   projective bands, divisors, dyadic heights, shells, both orientations,
   and one outer real part.  No positive power may be absorbed into
   \(X^\varepsilon\).

## Required false controls

The mechanism is invalid if it:

- uses only that \(b_{q,a}\) is primitive;
- replaces the divisor-supported \(x\)-sequence by a consecutive interval
  or arbitrary bounded array;
- applies (196.S10) to a term which is not an exact step-two difference;
- drops the physical-mask commutator, unequal endpoint translations,
  squarefree/coprimality flips, carries, births/deaths, cells, crossings,
  square-root phases, or zero extensions;
- separates the two orientations or frequency signs before the outer real
  part;
- deletes \(T=0\), weakens the strict \(T\ge1\) core, widens \(D_L\), or
  replaces the full open packet region by an unpriced submask;
- infers literal lower mass from a coefficient-uniform or phase-conjugated
  control; or
- changes any parent, bridge, theorem, or exponent.

The unsigned, character-erased, phase-conjugated, arbitrary-array,
consecutive-support, separate-orientation, low-carrier, and mask-deleted
shadows are mandatory controls.

## Promotion and stop rules

Complete promotion requires (196.S2) for the entire exact inherited open
region and the accepted outer \(O(L^2X^\varepsilon)\) ledger.  A strict
sector is promotable only with an exact complement and its own full target
ledger.  A rigorous route-scoped no-go is a valid round result.

Stop without an owner pivot if:

1. the literal recombined operator has no exact \(\Delta_2\) factor;
2. the exact commutator remainder retains
   \(u\min(Y,D_L)X^\varepsilon\) capacity;
3. carrier completion reproduces the original parity/anchor expansion;
4. the gain survives the required arbitrary-array or phase-conjugated
   shadow; or
5. the fixed-to-outer power ledger loses the same unresolved multiplier.

Even complete success leaves \(P_1\), all other original-\(t\) incidences,
the hard small-\(t\) owner until its remaining complements close, the
independent smooth M1 parent, GAR, every M2 parent, endpoint uniformity, M9,
both bridges, and the quarter theorem separate.  No exponent changes in
Round 196.

## Resources

At least 99 percent of effort is analytical or algebraic.  At most one
percent may be used for bounded exact checks of (196.S5)--(196.S10), carrier
residues, or finite commutator counterexamples.  Computation is
diagnostic-only and cannot certify an asymptotic theorem.
