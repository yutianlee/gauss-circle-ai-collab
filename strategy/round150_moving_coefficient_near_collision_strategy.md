# Round 150 moving-coefficient near-collision strategy

## Selection

Round 149 proves the exact lcm and common-gcd-lift compression, the
prefix-uniform coefficient norms, and target-safe bounds for the literal
diagonal, every exact phase class, and the small reduced-denominator
stratum.  The first unowned term is therefore not another transform or
another positive diagonal.  It is the nonzero near-collision part of the
literal two-row Gram matrix, whose coefficient changes with the outer
squarefree row.

Round 150 freezes that first seam.  It does not reopen the Round-148
transform, the Round-149 exact classes, any \(t\geq2\) layer, or the
independent Round-138 cross owner.  Its purpose is to decide whether the
actual row dependence has a source-legal low-rank or divisor-incidence
expansion that makes the nonzero collar target-sized.

## Accepted input and frozen collar

Put

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\leq R^2,\qquad D\leq\sqrt M,\qquad
 Q=2\sqrt{ND/E}.
$$

For squarefree \(d\), let \(d_{\mathrm o}=d/(d,2)\).  The accepted
compressed row is

$$
 G_U(d)=
 \sum_{\substack{(L,q)=1\\q\asymp LQ}}
 \chi_4(Lq)\frac{B_{d,U}(L)}L
 \mathscr W_{d,U}(L/q)e(NdL/q),
$$

where the exact finite prefix is retained and, for
\(L=ts^2\), \((t,s)=1\), \(a=(t,d_{\mathrm o})\), and \(c=t/a\),

$$
 B_{d,U}(ts^2)=0\quad\hbox{if }(s,d_{\mathrm o})>1,
$$

while otherwise

$$
 B_{d,U}(ts^2)=
 \frac{\mu(a)\mu(c)\mu(s)}c
 \sum_{u\mid d_{\mathrm o}/a}\frac{\mu(u)}u
 \sum_{\substack{v\ {m odd\ squarefree}\\
                   (v,d_{\mathrm o}cs)=1}}
 \frac{\mu(v)}{v^2}
 \kappa_{d,U}\!\left(au(csv)^2\right).
$$

For two distinct reduced cells write

$$
 q_i=hr_i,\qquad(r_1,r_2)=1,\qquad
 \delta=L_1r_2-L_2r_1,
$$

and choose the centered integer \(k\) so that

$$
 \rho=N\delta-khr_1r_2,
 \qquad |\rho|\leq hr_1r_2/2.
$$

Exact \(\rho=0\) is already owned.  The frozen target is the complete
nonzero collar

$$
 0<|\rho|\leq hr_1r_2/D.
$$

Its signed contribution, with both \(B\)'s, both profiles, both exact
prefixes, parity, squarefreeness, coprimality, and mod-four signs, must be
\(O_\varepsilon(R^2D X^\varepsilon)\).

## First analytical attack: exact row linearization

The arithmetic dependence may not be called arbitrary before it is
expanded.  For each fixed pair \(L_1,L_2\), expand exactly:

1. \((t_i,d_{\mathrm o})=a_i\);
2. \((s_i,d_{\mathrm o})=1\);
3. \(u_i\mid d_{\mathrm o}/a_i\);
4. \((v_i,d_{\mathrm o}c_is_i)=1\);
5. the product of the two literal prefix indicators; and
6. the two sampled profiles.

The desired output is a finite divisor-incidence or Mellin/partial-
summation representation

$$
 A_d(x_1)\overline{A_d(x_2)}
 =\sum_\nu \lambda_\nu(x_1,x_2)b_\nu(d)+\mathcal R_d(x_1,x_2)
$$

with explicit projective or nuclear norm and a remainder small enough
for the target.  If this is impossible for the literal cutoff, identify
the first exact rank, variation, or boundary obstruction.  An arbitrary
matrix counterexample is irrelevant unless the admissible coefficients
can realize it.

## Second analytical attack: shifted factorization

The near-collision equation has the exact identity

$$
 \boxed{
 (NL_1-khr_1)(NL_2+khr_2)
 =N^2L_1L_2+kh\rho.}
$$

This must be checked with signs and treated separately when \(k=0\).
For \(k\ne0\), test whether constrained divisor switching in the short
shift \(kh\rho\), together with \(\chi_4(L_1L_2r_1r_2)\), the weighted
\(B\)-norms, and the support \(q_i\asymp L_iQ\), gives the required
collar bound.  Counted pairs, coefficient-weighted absolute mass, and
the true signed mass are three different quantities.

## Required falsifiers and power ledger

1. Separate \(k=0\), \(k\ne0\), \(\rho=0\), and the generic complement.
2. Audit \(D=1\), especially \(L_1=L_2=1\), where the collar contains
   the full centered frequency range and no \(d\)-average exists.
3. Retain even squarefree \(d\), primes dividing \(d_{\mathrm o}\),
   \(q_i\mid N\), common denominators, imprimitive fractions, and every
   clipped prefix.
4. Give a complete \(R,M,D,E,Q,L_i,h,k,\rho\) power ledger.  A divisor
   bound per fixed shift is not enough until the number and weights of
   all shifts have been summed.
5. Do not infer cancellation from \(\chi_4\), squarefreeness, or
   smoothness without an exact estimate.  Do not infer a signed lower
   bound from an adverse upper capacity.
6. A strict range is promotable only if its complement is assigned to
   an existing owner or isolated as the next exact seam.

## Source direction

Audit primary results only after the literal coefficient and shifted
factorization are written.  Relevant interfaces may include
matrix-valued or operator large sieves, double large sieves, shifted
divisor problems with constrained factors, bilinear forms in Kloosterman
fractions, and squarefree additive correlations.  For each theorem,
record coefficient separability, averaging variables, smoothness,
diagonal, modulus and shift ranges, and the translated target power.

## Exit rule

Close under exactly one label:

- `moving_coefficient_collar_target`;
- `strict_moving_coefficient_collar_range`;
- `moving_coefficient_collar_no_go`.

The generic non-collar contribution remains a separate obligation unless
the proof genuinely controls it too.
