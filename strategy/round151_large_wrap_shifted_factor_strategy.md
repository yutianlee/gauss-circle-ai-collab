# Round 151 large-wrap shifted-factor strategy

## Selection

Round 150 proves the exact two-row arithmetic incidence, the uniform
half-weight coefficient norm, the complete fixed-wrap estimate, every
target-safe packet of (O(1+R^2/Q)) wraps, and the full actual-profile
row when (M=O(1)).  It also proves that summing fixed-shift divisor
bounds separately loses at least a factor (R).  The first unowned
collar term is therefore the growing-(M) signed band outside a chosen
symmetric target-safe wrap packet.

Round 151 freezes this term.  It does not reopen the fixed-wrap proof,
the bounded-(M) row, the exact (ho=0) classes, the growing-(M)
generic complement, any (t\geq2) layer, or the independent Round-138
cross owner.

## Frozen residual

Put

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\leq R^2,\qquad D\leq\sqrt M,\qquad
 Q=2\sqrt{ND/E}.
$$

For the exact compressed row, write (q_i=hr_i),
((r_1,r_2)=1),

$$
 \delta=L_1r_2-L_2r_1,\qquad
 \rho=N\delta-khr_1r_2,
 \qquad |\rho|\leq hr_1r_2/2.
$$

Choose a symmetric packet

$$
 \mathcal K_0=\{k:|k|\leq K_0\},\qquad
 |\mathcal K_0|\ll1+R^2/Q,
$$

which is already target-safe.  The frozen residual is the literal
signed contribution from

$$
 k\notin\mathcal K_0,\qquad
 0<|\rho|\leq hr_1r_2/D.
$$

Both exact coefficients, incidence masks, finite prefixes, sampled
profiles, common factors, imprimitive denominators, and the character
(chi_4(L_1L_2r_1r_2)) remain inside the sum.  The required bound is
(O_\varepsilon(R^2D X^\varepsilon)).

## Attack A: two-adic character transfer

For (k\ne0), put

$$
 A=NL_1-khr_1,\qquad B=NL_2+khr_2,
 \qquad j=\nu_2(k).
$$

All supported (L_i,h,r_i) are odd.  The exact relations are

$$
 AB=N^2L_1L_2+kh\rho,
$$

$$
 \frac{NL_1-A}{2^j}=\frac{k}{2^j}hr_1,
 \qquad
 \frac{B-NL_2}{2^j}=\frac{k}{2^j}hr_2.
$$

The two quotients on the left are odd.  Since the common odd factor
((k/2^j)h) occurs twice, multiplicativity suggests the exact transfer

$$
 \chi_4(L_1L_2r_1r_2)
 =\chi_4\!\left(
 L_1L_2\frac{NL_1-A}{2^j}\frac{B-NL_2}{2^j}
 \right).
$$

This identity must be proved for both signs of (k), every parity of
(N), and all allowed exceptional cases.  Then test whether the
factorized character can be kept while summing (k,ho) jointly in
the shifted-factor coordinates.  The precise divisibility conditions
recovering (r_i,h,k), rather than only (AB), must remain explicit.

The high-two-adic tail is a compulsory strict-range test: the number of
wraps with (2^{\nu_2(k)}\geq cR^2) is
(O(1+R^2/Q)), so the accepted fixed-wrap packet theorem should own it
if all endpoints are stated correctly.  This sparse range is useful
even if the remaining two-adic blocks stay open.

## Attack B: compulsory reciprocal (B)-process

At (D=1,L_1=L_2=1), the endpoint contains

$$
 S_U(N,Q)=
 \sum_{q\asymp Q}\chi_4(q)
 \mathscr W_{1,U}(1/q)e(N/q).
$$

Use the exact finite Fourier identity

$$
 \chi_4(q)=\frac{e(q/4)-e(-q/4)}{2i}
$$

for every integer (q).  For each sign, the phase is
(f_\sigma(q)=N/q+\sigma q/4).  A lawful discrete (B)-process has
critical equation

$$
 -N/q^2+\sigma/4=m,
$$

and, after writing (m=-n), the critical indices are
(ell=4n+\sigma) with critical phase (sqrt{N\ell}).  The expected
main amplitude is of size
(N^{1/4}\ell^{-3/4}).  Derive this transformation with exact
endpoints, transition terms, signs, phases, and actual weight norms.

The purpose is decisive rather than cosmetic.  Either the transformed
sum has a target-sized estimate in a new (M)-range, or the calculation
proves an exact self-return to the lower-radial square-root wave and
identifies the missing cancellation without hiding it in an error
term.  Bounded (M) is already owned.  The top endpoint
(M\asymp R^2), where (Q\asymp R), must be checked separately by the
literal length bound.

## Power, endpoint, and falsifier ledger

1. Separate (k=0), the accepted small packet, high-two-adic sparse
   wraps, the remaining large wraps, (ho=0), and the generic
   non-collar.
2. Sum every (h,k,ho,L_1,L_2,d) weight.  A fixed-(j), fixed-(k),
   or fixed-shift statement is not the full target.
3. Keep tuple capacity, coefficient-weighted absolute mass, and the
   signed character sum distinct.
4. Audit (D=1,L_i=1), (q_i\mid N), even squarefree rows, primes
   dividing (d_{\mathrm o}), common factors, imprimitive fractions,
   clipped prefixes, and balanced and extreme (M,D,E,Q).
5. The reciprocal (B)-process may use only the actual profile or a
   weight theorem whose derivative hypotheses are verified from its
   exact formula.  Boundedness alone is insufficient.
6. An exact self-return or an adverse source capacity is a scoped
   no-go, not a signed lower bound and not an impossibility theorem.
7. A strict range is promoted only when its complement is named and
   assigned to the next exact seam.

## Source direction

Audit primary results for character-twisted shifted divisor sums,
quadratic-divisor problems with a family of shifts, Kloosterman
fractions, spectral shifted convolution, and discrete reciprocal
(B)-process or van der Corput transformations.  Record theorem
numbers, coefficient shape, character and two-adic restrictions,
averaging variables, shift family, smoothness, endpoints, exceptional
spectrum, and every translated (R,M,D,E,Q) power.  A structural
analogy is not a black-box placement.

## Exit rule

Close under exactly one label:

- `large_wrap_collar_target`;
- `strict_large_wrap_character_range`;
- `large_wrap_shifted_factor_no_go`.

The growing-(M) generic complement remains a separate obligation
unless the same proof explicitly controls it.
