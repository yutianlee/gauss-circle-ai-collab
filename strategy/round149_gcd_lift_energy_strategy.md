# Round 149 gcd-lift and joint-energy strategy

## Selection

Round 148 gives the exact finite reciprocal scalar but proves a loss
only when the individual ((\alpha,b,q)) progression cells remain
separate through Cauchy and the (d)-diagonal is then made positive.
The highest-leverage surviving operation is therefore the exact
pre-Cauchy recombination already suggested by the phase: first sum every
Möbius cell with the same lcm (ell), then sum every gcd lift with the
same reduced fraction (ell/q=L/q_0).

This round does not reopen the transform or its remainder. It asks
whether the resulting compressed coefficient has enough square-summable
structure to make the full joint (d)-energy target-sized.

## Candidate exact compression

For squarefree \(d\), put \(d_{\mathrm o}=d/(d,2)\) and define

$$
 C_d(n)=
 \sum_{\substack{\alpha,b\ {\rm odd}\ b\mid d\\
                  \mu(\alpha)\mu(b)\ne0\\
                  [\alpha^2,b]=n}}
 \mu(\alpha)\mu(b).
$$

The prime-local ledger suggests the exact formula

$$
 C_d(n)=
 \begin{cases}
 \mu(u)\mu(v),&n=uv^2,\quad u\mid d_{\mathrm o},\quad
   u,v\ {\rm odd},\quad \mu^2(uv)=1,\quad (v,d)=1,\\
 0,&\text{otherwise}.
 \end{cases}
$$

The cancellation at odd \(p\mid d_{\mathrm o}\) and \(p^2\mid n\) is
mandatory and must be checked directly. The prime \(2\) is absent from
the odd lcm ledger, even when \(2\mid d\). The exact
nonempty-progression indicator for each inherited prefix is denoted by
\(\kappa_{d,U}(n)\); it may not be
replaced by a convenient continuous cutoff.

Write (ell=gL), (q=gq_0), and ((L,q_0)=1). Since all variables are
odd,

$$
 \chi_4(gL)\chi_4(gq_0)=\chi_4(Lq_0),
$$

while the phase and saddle profile depend only on (L/q_0). The
candidate compressed lift is

$$
 B_{d,U}(L)=\sum_{g\ge1}\frac{C_d(gL)\kappa_{d,U}(gL)}g.
$$

Round 149 must prove this regrouping as an exact finite identity before
using it. It must then prove or refute the uniform square norm

$$
 \sum_{L\ge1}\frac{|B_{d,U}(L)|^2}{L}
 \ll_\varepsilon X^\varepsilon.
$$

A lawful proof may use the divisor transform and the absolutely
convergent (uv^2) support, but it must retain the prefix indicator.

## Joint-energy target

After exact compression, define the literal row

$$
 G_U(d)=
 \sum_{\substack{L,q_0\ge1\\(L,q_0)=1}}
 \frac{\chi_4(Lq_0)B_{d,U}(L)}L
 \mathscr W_{d,U}(L/q_0)
 e(NdL/q_0),
$$

where the accepted support is (q_0\asymp LQ). Then

$$
 \mathcal T_{D,E,U}
 =\sum_d\mu^2(d)\frac Dd G_U(d).
$$

Cauchy only in the final (d)-variable reduces the target to

$$
 \mathscr E_U:=\sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \ll_\varepsilon R^2D X^\varepsilon.
$$

The literal equal-cell diagonal should cost at most (DQX^\varepsilon)
if the compressed square norm is true, hence is already safe because
(Q\le R^2). The real question is the signed off-diagonal with

$$
 \Delta=L_1q_{0,2}-L_2q_{0,1},
 \qquad
 N\Delta\equiv0\pmod{q_{0,1}q_{0,2}},
$$

including near alignments, common divisors, imprimitive reductions,
and the (d)-dependence of (B_{d,U}) and the profile.

## Required attacks and falsifiers

1. Prove the prime-local (C_d(n)) formula and the exact finite
   (ell\mapsto(L,q_0,g)) regrouping; do not infer them from analogy.
2. Prove the truncated-lift square norm uniformly for every actual
   prefix, or identify its first counterexample.
3. Expand the joint energy only after compression. Separate literal
   equality, exact (N)-dependent alignments, near collisions, and the
   generic determinant range.
4. Keep (B_{d,U}(L)) and (\mathscr W_{d,U}(L/q_0)) dependent on (d).
   A classical large sieve with (d)-independent outer coefficients is
   only a diagnostic until an exact reduction supplies its hypotheses.
5. Audit (D=1), (L=1), (q_0\mid N), small reduced denominators,
   primes dividing (d), balanced and extreme aspects, short prefixes,
   and every (M\le R^2).
6. Treat every adverse energy capacity as an upper-bound limitation,
   not a signed lower bound.

## Exit rule

Close under exactly one label:

- `euler_compressed_reciprocal_target`;
- `strict_joint_energy_range`;
- `gcd_lift_energy_no_go`.

A target or strict range must include the complete off-diagonal and all
prefixes. A no-go must identify the exact proof placement it excludes
and leave other signed regroupings logically open.
