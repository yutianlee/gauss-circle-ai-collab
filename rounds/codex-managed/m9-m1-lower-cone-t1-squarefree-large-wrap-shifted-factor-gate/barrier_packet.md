# Round 151 barrier packet

- Campaign: `m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate`
- Round: 151
- Starting graph SHA-256: `521f626e4af7e75e29d2ba909efb0d48864d5da4785de786acbd746d7559c11f`

## Accepted input

Round 150 proves, uniformly in every finite prefix,

$$
 \sum_L\frac{|B_{d,U}(L)|}{\sqrt L}\ll_\varepsilon X^\varepsilon.
$$

For every fixed centered wrap (k), the complete coefficient-weighted
collar mass is

$$
 \ll_\varepsilon DQX^\varepsilon.
$$

Consequently every selected set of
(O(1+R^2/Q)) wraps is (O_\varepsilon(R^2DX^\varepsilon)).  This
owns (k=0), a symmetric small-wrap packet, and any other sparse packet
of the same cardinality.  The actual complete row is also owned when
(M=O(1)).

## Frozen unresolved term

For (q_i=hr_i), ((r_1,r_2)=1), put

$$
 \delta=L_1r_2-L_2r_1,\qquad
 \rho=N\delta-khr_1r_2,
 \qquad |\rho|\leq hr_1r_2/2.
$$

Choose a symmetric accepted packet (mathcal K_0) with
(|\mathcal K_0|\ll1+R^2/Q).  Round 151 owns only the growing-(M)
signed contribution with

$$
 k\notin\mathcal K_0,\qquad
 0<|\rho|\leq hr_1r_2/D.
$$

The literal atom contains

$$
 \mu^2(d)\chi_4(L_1L_2r_1r_2)
 \frac{B_{d,U}(L_1)\overline{B_{d,U}(L_2)}}{L_1L_2}
 \mathscr W_{d,U}(L_1/q_1)
 \overline{\mathscr W_{d,U}(L_2/q_2)}
 e\!\left(\frac{d\rho}{hr_1r_2}\right),
$$

together with every exact incidence mask and both clipped prefixes.

## Exact shifted-factor data

For (k\ne0), set

$$
 A=NL_1-khr_1,\qquad B=NL_2+khr_2.
$$

Then (A,B>0) on the collar and

$$
 AB=N^2L_1L_2+kh\rho.
$$

For fixed (L_i,h,k,\rho), divisor recovery has only
(X^\varepsilon) capacity, but separate absolute summation over all
shifts has capacity (NL_1L_2QX^\varepsilon/D) and loses at least
(R).  This placement is rejected.  The new question is whether the
character and the full family of shifts can be recombined before
absolute values.

All supported (L_i,h,r_i) are odd.  With (j=\nu_2(k)), the exact
character-transfer candidate is

$$
 \chi_4(L_1L_2r_1r_2)
 =\chi_4\!\left(
 L_1L_2\frac{NL_1-A}{2^j}\frac{B-NL_2}{2^j}
 \right).
$$

It is candidate mathematics until fully derived and independently
checked.

## Compulsory scalar endpoint

At (D=1,L_1=L_2=1), no row average exists.  The relevant row contains

$$
 B_{1,U}(1)
 \sum_{q\asymp Q}\chi_4(q)
 \mathscr W_{1,U}(1/q)e(N/q).
$$

The exact identity

$$
 \chi_4(q)=\frac{e(q/4)-e(-q/4)}{2i}
$$

forces any discrete reciprocal (B)-process to see square-root phases
(sqrt{N\ell}) on (ell\equiv\pm1\pmod4).  The transformation,
weights, endpoints, and target power must be derived rather than
asserted.

## Rejected shortcuts

1. Do not sum fixed-shift divisor bounds separately.
2. Do not replace the joint prefixes and profiles by a finite-rank or
   arbitrary coefficient matrix.
3. Do not infer cancellation from (chi_4) without an exact estimate.
4. Do not use a continuous weight unless its derivative and boundary
   hypotheses are proved for the actual profile.
5. Do not call a reciprocal-to-square-root self-return a gain.
6. Do not identify an adverse upper capacity with a signed lower bound.
7. Do not absorb the growing-(M) generic complement into the collar.

## Scope boundary

The growing-(M) generic non-collar, every (t\geq2) layer, the
Round-138 cross owner, lower GAR, M9-M1, M9-M2, endpoint uniformity,
M9, the bridge, the quarter target, and both global exponents remain
unchanged unless proved by complete owners.
