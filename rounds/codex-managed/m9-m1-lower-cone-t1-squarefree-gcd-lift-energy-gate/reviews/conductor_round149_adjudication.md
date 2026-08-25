# Round 149 conductor adjudication

- Campaign: \`m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate\`
- Round: 149
- Starting graph SHA-256: \`8f1912eeda4843718379213478a839b30fb2694d6b169ac8decbab5ca3561176\`
- Terminal label: \`gcd_lift_energy_no_go\`

## 1. Decision

Round 149 accepts an exact pre-Cauchy lcm and gcd-lift compression,
prefix-uniform coefficient norms, and target-safe bounds for both the
literal cell diagonal and every exact \(N\)-dependent phase alignment.
It also accepts a strictly scoped method/source obstruction at the
remaining moving-coefficient near/generic correlation.

Put

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\leq R^2,\qquad D\leq\sqrt M,\qquad
 Q=2\sqrt{ND/E}\ll R^2.
$$

For squarefree \(d\), including even \(d\), put
\(d_{\mathrm o}=d/(d,2)\).  The exact lcm coefficient is

$$
 C_d(n)=
 \begin{cases}
  \mu(u)\mu(v),&
  n=uv^2,\quad u\mid d_{\mathrm o},\quad
  u,v\ {\rm odd},\quad \mu^2(uv)=1,\quad(v,d)=1,\\
 0,&\text{otherwise}.
 \end{cases}
$$

Let \(\kappa_{d,U}(n)\) be the literal indicator that the original
\(n\)-progression meets the retained finite amplitude.  Then

$$
 B_{d,U}(L)=
 \sum_{\substack{g\geq1\\g\ {\rm odd}}}
 \frac{C_d(gL)\kappa_{d,U}(gL)}g
$$

and the accepted Round-148 scalar is exactly

$$
 \mathcal T_{D,E,U}
 =\sum_{d\asymp D}\mu^2(d)\frac Dd\,G_U(d),
$$

$$
 G_U(d)=
 \sum_{\substack{L,q_0\geq1\ {\rm odd}\\(L,q_0)=1\\
                 q_0\asymp LQ}}
 \chi_4(Lq_0)\frac{B_{d,U}(L)}L
 \mathscr W_{d,U}(L/q_0)e(NdL/q_0).
$$

Uniformly in every finite prefix,

$$
 \sum_L\frac{|B_{d,U}(L)|^2}{L}
 +\sum_L\frac{|B_{d,U}(L)|}{L}
 \ll_\varepsilon X^\varepsilon.
$$

The equal-cell diagonal is \(O_\varepsilon(DQX^\varepsilon)\).
Distinct cells with exactly the same phase modulo one have total
energy \(O_\varepsilon(DQX^\varepsilon)\) as well.  Both are within
\(R^2DX^\varepsilon\).

The sufficient joint energy

$$
 \sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \ll_\varepsilon R^2DX^\varepsilon
$$

is not proved.  Its first open part is the nonzero near-collision and
generic determinant correlation with the literal \(d\)-dependent
coefficient.  The terminal no-go says only that the uniform lift norm,
safe positive diagonal, and a classical fixed-vector large sieve or
separately positive spacing ledger do not imply that correlation.
It is not a lower bound for the signed row.

No strict owner-complete range, \(t=1\) target, downstream theorem, or
exponent improvement is accepted.

## 2. Arithmetic and compression adjudication

For each odd prime \(p\), the local lcm ledger is

| prime case | exponent \(0\) | exponent \(1\) | exponent \(2\) |
|---|---:|---:|---:|
| \(p\nmid d_{\mathrm o}\) | \(1\) | \(0\) | \(-1\) |
| \(p\mid d_{\mathrm o}\) | \(1\) | \(-1\) | \(-1+1=0\) |

The exponent-two cancellation in the second row is compulsory.  The
prime \(2\) is absent because \(\alpha,b,\ell,q\) are odd.  This
proves the displayed \(C_d(n)\), with no assumption that \(d\) is
odd.

The finite progression set depends on \((\alpha,b)\) only through
\(d\), \(n=[\alpha^2,b]\), and nonemptiness.  Hence

$$
 \sum_{\substack{(\alpha,b)\in\mathcal P(d)\\
                 [\alpha^2,b]=n}}
 \mu(\alpha)\mu(b)
 =C_d(n)\kappa_{d,U}(n).
$$

For every odd \((\ell,q)\), the bijection

$$
 g=(\ell,q),\qquad \ell=gL,\qquad q=gq_0,\qquad(L,q_0)=1
$$

gives

$$
 \chi_4(\ell)\chi_4(q)=\chi_4(Lq_0),\qquad
 \frac{Nd\ell}{q}=\frac{NdL}{q_0},\qquad
 \frac1\ell=\frac1{gL}.
$$

The saddle profile depends only on \(L/q_0\), and
\(q\asymp\ell Q\) is equivalent to \(q_0\asymp LQ\).
All remaining \(g\)-dependence is exactly the finite sum defining
\(B_{d,U}\).

If \(L=ts^2\), \(a=(t,d_{\mathrm o})\), and \(r=t/a\), then
\(B_{d,U}(L)=0\) when \((s,d_{\mathrm o})>1\).  Otherwise

$$
\begin{aligned}
 B_{d,U}(ts^2)
 ={}&\frac{\mu(a)\mu(r)\mu(s)}r
 \sum_{u'\mid d_{\mathrm o}/a}\frac{\mu(u')}{u'}\\
 &\times
 \sum_{\substack{v'\ {\rm odd\ squarefree}\\
                 (v',d_{\mathrm o}rs)=1}}
 \frac{\mu(v')}{(v')^2}
 \kappa_{d,U}\!\left(au'(rsv')^2\right).
\end{aligned}
$$

This closed formula is accepted.  The prefix couples \(u'\) and
\(v'\), so no Euler product is inferred.

## 3. Norm, diagonal, and alignment adjudication

The closed formula gives

$$
 |B_{d,U}(ts^2)|\ll_\varepsilon X^\varepsilon/r.
$$

Since \(L=ars^2\), the square and weighted \(\ell^1\) norms reduce to

$$
 \sum_{a\mid d_{\mathrm o}}\frac1a
 \sum_r\frac1{r^3}\sum_s\frac1{s^2},
 \qquad
 \sum_{a\mid d_{\mathrm o}}\frac1a
 \sum_r\frac1{r^2}\sum_s\frac1{s^2}.
$$

Both converge up to \(X^\varepsilon\), without using any regularity
of \(\kappa_{d,U}\).  The finite support \(L\ll E\) also gives
\(\sum_L|B_{d,U}(L)|+\sum_L|B_{d,U}(L)|^2
\ll\sqrt E\,X^\varepsilon\).

There are \(O(LQ)\) admissible \(q_0\) for each \(L\).  Therefore

$$
 \mathscr E_{\rm diag}
 \ll Q\sum_{d\asymp D}\sum_L\frac{|B_{d,U}(L)|^2}{L}
 \ll DQX^\varepsilon
 \leq R^2DX^\varepsilon.
$$

For exact alignments, let

$$
 \Delta=L_1q_2-L_2q_1,\quad
 q_1=HA,\quad q_2=HB,\quad(A,B)=1,\quad
 \delta=L_1B-L_2A.
$$

Then \(\Delta=H\delta\),
\((\delta,A)=(\delta,B)=1\), and distinct exact alignment implies

$$
 HAB\mid N\delta,\qquad
 AB\mid N,\qquad
 H\mid (N/AB)\delta.
$$

The divisor count for fixed \(L_1,L_2\), followed by the weighted
\(\ell^1\) norm, is target-safe.  A second derivation groups cells by
the reduced phase

$$
 c=(q_0,N),\quad r=q_0/c,\quad
 \frac{NL}{q_0}\equiv\frac{(N/c)L}{r}\pmod1
$$

and proves \(O_\varepsilon(QX^\varepsilon)\) per row.  The conductor
accepts the robust energy statement

$$
 \mathscr E_{\rm exact}\ll_\varepsilon DQX^\varepsilon.
$$

It includes distinct aligned cells, \(q_0\mid N\), common factors,
imprimitive denominators, and even squarefree \(d\).

## 4. Near-collision and source adjudication

For the nonexact sector, write

$$
 q_{0,i}=hr_i,\qquad(r_1,r_2)=1,\qquad
 \delta=L_1r_2-L_2r_1,
$$

and choose the nearest integer \(k\) so that

$$
 \rho=N\delta-khr_1r_2,\qquad
 |\rho|\leq hr_1r_2/2.
$$

Exact alignment is \(\rho=0\), already owned.  The first open collar is

$$
 0<|\rho|\leq \frac{hr_1r_2}{D}.
$$

Its literal kernel is

$$
\begin{aligned}
 \sum_{d\asymp D}\mu^2(d)
 &\frac{B_{d,U}(L_1)\overline{B_{d,U}(L_2)}}{L_1L_2}
 \mathscr W_{d,U}(L_1/q_{0,1})
 \overline{\mathscr W_{d,U}(L_2/q_{0,2})}\\
 &\times e\!\left(\frac{d\rho}{hr_1r_2}\right).
\end{aligned}
$$

The coefficient changes arithmetically when primes enter
\(d_{\mathrm o}\), and both the exact prefix and profile move with
\(d\).  Montgomery--Vaughan's Theorem 1 and its duality lemma have
one common coefficient vector; neither orientation accepts this
matrix.  The primary progression theorems touch only small reduced
denominators already owned elementarily, or have a pure squarefree
coefficient and a fixed-modulus average.  Bettin--Chandee and Wright
retain independent sequences, inverse phases or fixed-residue
convolutions, and different diagonals or absolute-value placement.

Even after an illegal fixed-vector replacement, the optimistic
unwrapped spacing capacity is

$$
 Q(D+M)X^\varepsilon,
$$

whose \(QM\) term exceeds \(R^2D\) by \(\sqrt M\).  Raw rational
spacing is worse.  These are upper capacities for failed proof
placements, not signed lower bounds.

At \(D=1,L=1\), no \(d\)-average exists.  The candidate's initial
unconditional second-derivative diagnostic was rejected because
boundedness alone does not give the profile variation needed by the
weighted theorem.  The repaired statement is explicitly conditional
and unused.  Thus the one-row reciprocal sum remains a compulsory
all-scale test.

## 5. Evidence adjudication

The discovery report is accepted for the parity-correct lcm table,
finite gcd-lift identity, closed lift formula, prefix-uniform norm,
literal diagonal, independent exact-phase grouping, low reduced
denominators, full near-collision kernel, and scoped power no-go.

The statement-only blind report independently confirms the lcm
collapse, closed coefficient, square and weighted \(\ell^1\) norms,
literal diagonal, common-factor exact-alignment divisor count, and the
moving-row first seam.  It identifies \(D=1,L=1\) as a compulsory
test.

The primary-source report is accepted for the exact
Montgomery--Vaughan orientation and duality seam, the progression
range translations, the Bettin--Chandee and Wright separability and
phase mismatches, and the all-aspect capacity ledger.  The conductor
also checked the cited primary statements directly.

The initial blind conductor review returned RED only on the unstated
variation hypothesis in the \(D=1\) diagnostic.  The candidate was
repaired.  The terminal reviews are:

- \`blind_conductor_round149_math_review_v2.md\`: GREEN;
- \`source_conductor_round149_final.md\`: GREEN;
- \`discovery_source_conductor_round149_review.md\`: GREEN.

The source review reconciles the two exact-alignment prices:
\(O(DX^\varepsilon)\) is the distinct exact off-diagonal, while
\(O(DQX^\varepsilon)\) is the full phase-class contribution including
the literal diagonal.

## 6. Accepted statements, rejected inferences, and open scope

The graph may record:

1. the exact parity-correct lcm coefficient, including the
   \(p\mid d_{\mathrm o}\) exponent-two cancellation and absent
   \(p=2\) factor;
2. the exact finite gcd-lift compression and closed coefficient;
3. the prefix-uniform square and weighted \(\ell^1\) norms;
4. the target-safe literal diagonal and every exact \(N\)-alignment;
5. the target-safe \(q_*\leq R\) stratum;
6. the complete nonzero near-collision kernel; and
7. the scoped fixed-vector/source and positive-spacing no-go.

Reject the inferences that:

1. \(d\) must be odd;
2. the prefix must be smoothed to prove the lift norm;
3. the lift norm and literal diagonal imply the joint energy;
4. compression leaves the Round-148 factor-\(R\) literal diagonal;
5. equality of reduced fractions exhausts exact \(N\)-alignments;
6. exact alignments are the first obstruction;
7. large-sieve duality permits a coefficient vector varying with \(d\);
8. published small-modulus progression ranges reach the hard sector;
9. Bettin--Chandee supplies a direct separable inverse-phase model;
10. Wright's partially fixed-modulus theorem matches the literal Gram;
11. an adverse spacing capacity is a lower bound for the signed row; or
12. this round proves \(t=1\), M9--M1, M9--M2, endpoint uniformity,
    M9, the bridge, the quarter target, or an exponent improvement.

The first open theorem is the moving-coefficient near/generic
correlation above, uniformly in every prefix and aspect.  A complete
Euler recombination followed by a genuinely signed theorem remains an
alternative.  No termwise identification with the Round-147 powerful
\(H\)-index is authorized.

Every \(t\geq2\) layer and the independent Round-138 cross owner remain
open.  M9--M1, M9--M2, endpoint uniformity, M9, the conditional bridge,
and the Gauss target remain open.  The internal exponent remains
\(1/3\); the audited external exponent remains

$$
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
$$

## 7. Recommended state effect

Create:

1. \`M9-M1-lower-cone-t1-squarefree-gcd-lift-compression-reduction\`;
2. \`M9-M1-lower-cone-t1-squarefree-gcd-lift-energy-obstruction\`.

Attach both to the reciprocal-transform route and the global
lower-radial signed obligation.  Update the Round-148
progression-diagonal obstruction to record that exact pre-Cauchy
compression repairs its early diagonal, leaving the nonzero
moving-coefficient near/generic sector first.

Retain the joint energy, signed \(t=1\) target, every strict range, all
downstream owners, both exponents, and the quarter target unchanged.
