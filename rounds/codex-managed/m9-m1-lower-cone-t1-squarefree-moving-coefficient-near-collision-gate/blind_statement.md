# Statement-only Round 150 problem

Let

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\leq R^2,\qquad D\leq\sqrt M,\qquad
 Q=2\sqrt{ND/E}.
$$

For each squarefree \(d\asymp D\), put
\(d_{\mathrm o}=d/(d,2)\).  Let \(\kappa_{d,U}\) be the literal finite
nonempty-progression indicator inherited from a clipped prefix, and let
\(\mathscr W_{d,U}\) be the actual bounded smooth radial-cone-prefix
profile.  For \(L=ts^2\), where \(t,s\) are squarefree and
\((t,s)=1\), put \(a=(t,d_{\mathrm o})\) and \(c=t/a\).  Define
\(B_{d,U}(L)=0\) if \((s,d_{\mathrm o})>1\), and otherwise

$$
 B_{d,U}(ts^2)=
 \frac{\mu(a)\mu(c)\mu(s)}c
 \sum_{u\mid d_{\mathrm o}/a}\frac{\mu(u)}u
 \sum_{\substack{v\geq1\ {
m odd\ squarefree}\\
                   (v,d_{\mathrm o}cs)=1}}
 \frac{\mu(v)}{v^2}
 \kappa_{d,U}\!\left(au(csv)^2\right).
$$

The exactly compressed row is

$$
 G_U(d)=
 \sum_{\substack{L,q\geq1\ {
m odd}\\
                  (L,q)=1\\q\asymp LQ}}
 \chi_4(Lq)\frac{B_{d,U}(L)}L
 \mathscr W_{d,U}(L/q)e(NdL/q).
$$

The accepted bounds

$$
 \sum_L\frac{|B_{d,U}(L)|^2}{L}
 +\sum_L\frac{|B_{d,U}(L)|}{L}\ll_\varepsilon X^\varepsilon
$$

make the literal diagonal, all exact phase classes, and the small
reduced-denominator stratum target-safe.  These pieces are excluded
from the problem below.

For two distinct reduced cells write

$$
 q_i=hr_i,\qquad(r_1,r_2)=1,\qquad
 \delta=L_1r_2-L_2r_1,
$$

and choose \(k\in\mathbb Z\) so that

$$
 \rho=N\delta-khr_1r_2,qquad
 |\rho|\leq hr_1r_2/2.
$$

Independently determine whether the complete signed contribution from

$$
 0<|\rho|\leq hr_1r_2/D
$$

to \(\sum_{d\asymp D}\mu^2(d)|G_U(d)|^2\) is

$$
 \ll_\varepsilon R^2D X^\varepsilon
$$

uniformly for every \(M,D,E,Q\) and every actual clipped prefix.
Derive the true two-row dependence rather than replacing it with an
arbitrary matrix.  Price common factors, imprimitive denominators,
even squarefree \(d\), primes dividing \(d_{\mathrm o}\), \(k=0\),
\(D=1\), \(L_1=L_2=1\), and the mod-four signs.  Separate the raw
tuple count, coefficient-weighted absolute mass, and signed mass.

Prove the full collar bound, a strict owner-complete range, or the first
rigorous coefficient, cutoff, factorization, variation, source, or
power obstruction.  Do not assume coefficient independence, replace
the exact prefix by a smooth cutoff, use boundedness as bounded
variation, or interpret an adverse upper capacity as a signed lower
bound.  The generic complement is outside scope unless it is genuinely
controlled by the same proof.
