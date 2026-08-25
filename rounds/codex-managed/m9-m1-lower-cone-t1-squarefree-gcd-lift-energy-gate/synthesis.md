# Round 149 synthesis

Round 149 closes under

$$
 \boxed{\mathsf{gcd\_lift\_energy\_no\_go}.}
$$

The round does not prove the \(t=1\) squarefree-cone target.  It proves
that exact pre-Cauchy Euler compression repairs the Round-148
progression-cell diagonal loss and moves the first open seam to a
nonexact, moving-coefficient near/generic correlation.

Let

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\leq R^2,\qquad D\leq\sqrt M,\qquad
 Q=2\sqrt{ND/E}.
$$

For squarefree \(d\), put \(d_{\mathrm o}=d/(d,2)\).  Summing every
Round-148 Möbius pair with the same lcm gives exactly

$$
 C_d(n)=
 \begin{cases}
  \mu(u)\mu(v),&
  n=uv^2,\quad u\mid d_{\mathrm o},\quad
  u,v\ {\rm odd},\quad \mu^2(uv)=1,\quad(v,d)=1,\\
 0,&\text{otherwise}.
 \end{cases}
$$

At an odd prime \(p\mid d_{\mathrm o}\), the exponent-two
contributions are \(-1,+1\) and cancel.  The prime \(2\) is absent
from the lcm ledger, even when \(d\) is even.

Let \(\kappa_{d,U}(n)\) be the literal finite indicator that the
original \(n\)-progression meets the clipped amplitude.  Writing

$$
 \ell=gL,\qquad q=gq_0,\qquad(L,q_0)=1
$$

is an exact finite regrouping.  The common lift cancels from the
character and reduced phase:

$$
 \chi_4(gL)\chi_4(gq_0)=\chi_4(Lq_0),\qquad
 \frac{Nd\ell}{q}=\frac{NdL}{q_0}.
$$

Thus

$$
 B_{d,U}(L)=
 \sum_{\substack{g\geq1\\g\ {\rm odd}}}
 \frac{C_d(gL)\kappa_{d,U}(gL)}g
$$

and

$$
 \mathcal T_{D,E,U}
 =\sum_{d\asymp D}\mu^2(d)\frac Dd\,G_U(d),
$$

$$
 G_U(d)=
 \sum_{\substack{L,q_0\geq1\ {\rm odd}\\
                 (L,q_0)=1\\q_0\asymp LQ}}
 \chi_4(Lq_0)\frac{B_{d,U}(L)}L
 \mathscr W_{d,U}(L/q_0)e(NdL/q_0).
$$

The exact prefix may be completely irregular.  Nevertheless,

$$
 \sum_L\frac{|B_{d,U}(L)|^2}{L}
 +\sum_L\frac{|B_{d,U}(L)|}{L}
 \ll_\varepsilon X^\varepsilon.
$$

Indeed, for \(L=ts^2\), \(a=(t,d_{\mathrm o})\), and \(r=t/a\),
the closed lift formula gives
\(|B_{d,U}(L)|\ll_\varepsilon X^\varepsilon/r\).  The square norm
then has local summation
\(\sum_{a\mid d_{\mathrm o}}a^{-1}\sum r^{-3}\sum s^{-2}\);
the weighted \(\ell^1\) norm has \(r^{-2}\) in place of \(r^{-3}\).

There are \(O(LQ)\) reduced denominators for each \(L\), so the
literal diagonal is

$$
 \mathscr E_{\rm diag}
 \ll_\varepsilon DQX^\varepsilon
 \leq R^2DX^\varepsilon.
$$

Every exact \(N\)-dependent phase alignment is also target-safe.  If

$$
 q_1=HA,\qquad q_2=HB,\qquad(A,B)=1,\qquad
 \delta=L_1B-L_2A,
$$

then a distinct exact alignment satisfies

$$
 HAB\mid N\delta,\qquad
 AB\mid N,\qquad H\mid(N/AB)\delta.
$$

The distinct exact off-diagonal costs
\(O_\varepsilon(DX^\varepsilon)\).  Including the equal-cell
diagonal, the complete exact phase classes cost
\(O_\varepsilon(DQX^\varepsilon)\).  This includes common factors,
imprimitive denominators, \(q_0\mid N\), and even squarefree rows.

The sufficient energy

$$
 \sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \stackrel{?}{\ll_\varepsilon}R^2DX^\varepsilon
$$

remains open.  For two nonexact cells, write

$$
 q_{0,i}=hr_i,\qquad(r_1,r_2)=1,\qquad
 \delta=L_1r_2-L_2r_1,
$$

and choose \(k\) so that

$$
 \rho=N\delta-khr_1r_2,\qquad
 |\rho|\leq hr_1r_2/2.
$$

The first open collar is

$$
 0<|\rho|\leq \frac{hr_1r_2}{D}.
$$

The associated \(d\)-kernel retains
\(\mu^2(d)B_{d,U}(L_1)\overline{B_{d,U}(L_2)}\), both moving
profiles, both exact prefixes, and the mod-four signs.  It is not a
geometric kernel with a fixed outer coefficient vector.

Montgomery--Vaughan's primal and dual large sieves require one common
coefficient vector.  The audited squarefree-progression theorems have
a pure squarefree coefficient, fixed-modulus or small-denominator
ranges, and different averages.  Bettin--Chandee and Wright require
independent sequences, inverse fractions or fixed-residue
convolutions, and different diagonal or absolute-value placement.
None directly estimates the literal moving-row Gram matrix.

Even the illegal fixed-vector diagnostic has optimistic unwrapped
capacity

$$
 Q(D+M)X^\varepsilon,
$$

whose \(QM\) term loses \(\sqrt M\) against the energy target.  This
is an adverse upper capacity, not a lower bound for the actual signed
row.  At \(D=1,L=1\), no \(d\)-average exists; the one-row reciprocal
sum remains a compulsory all-scale test.  A second-derivative estimate
was retained only as a conditional bounded-variation diagnostic.

Three terminal reviews are GREEN:

- \`blind_conductor_round149_math_review_v2.md\`;
- \`source_conductor_round149_final.md\`;
- \`discovery_source_conductor_round149_review.md\`.

The next lawful input is a coefficient-sensitive theorem for the
nonexact moving-row near/generic correlation, or a complete Euler
recombination that produces a genuinely source-legal signed family.
No termwise map to the Round-147 powerful \(H\)-index is allowed.

Every \(t\geq2\) layer and the independent Round-138 cross owner remain
open.  There is no change to M9--M1, M9--M2, endpoint uniformity, M9,
the conditional bridge, or the Gauss target.  The internally proved
exponent remains \(1/3\); the audited external exponent remains

$$
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
$$
