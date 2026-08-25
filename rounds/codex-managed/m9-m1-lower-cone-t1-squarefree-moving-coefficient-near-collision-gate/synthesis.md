# Round 150 synthesis

Round 150 closes under

$$
 \boxed{\mathsf{strict\_moving\_coefficient\_collar\_range}}.
$$

It does not prove the full moving-coefficient collar or the Gauss
circle conjecture.  It proves a strict target-safe family and moves the
first collar seam to the growing-$M$ large-wrap band.

Let

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\le R^2,\qquad D\le\sqrt M,\qquad
 Q=2\sqrt{ND/E}.
$$

For $d=\eta m$, with $m=d_{\mathrm o}$ odd squarefree, and
$L_i=t_is_i^2$, expand $a_i\mid t_i$, set $c_i=t_i/a_i$, and retain
the exact $u_i,v_i$ and prefix sums.  The pure two-row arithmetic masks
linearize exactly as

$$
 {\bf1}_{F\mid m}{\bf1}_{(m,P)=1}
 ={\bf1}_{(F,P)=1}\sum_{z\mid P}\mu(z){\bf1}_{Fz\mid m},
$$

where

$$
 F=[a_1u_1,a_2u_2],\qquad
 P=\operatorname{rad}(c_1c_2s_1s_2v_1v_2).
$$

The arithmetic incidence coefficients have projective norm
$O_\varepsilon(X^\varepsilon)$ at fixed $(L_1,L_2)$.  The two exact
prefixes and the two actual sampled profiles remain joint row-cell
functions; no rank statement for that full matrix is made.

The accepted closed coefficient formula also gives the new uniform
norm

$$
 \sum_L\frac{|B_{d,U}(L)|}{\sqrt L}
 \ll_\varepsilon X^\varepsilon.
$$

For $q_i=hr_i$, $(r_1,r_2)=1$, write

$$
 \delta=L_1r_2-L_2r_1,\qquad
 \rho=N\delta-khr_1r_2,
$$

with $k$ the unique centered integer.  In the nonexact collar
$0<|\rho|\le hr_1r_2/D$, fixing $k,L_1,L_2,h,r_1$ confines $r_2$
to an interval of length

$$
 \ll\frac{L_2Q^2}{hDN}=\frac{4L_2}{hE}\ll1.
$$

The symmetric count is

$$
 \mathcal N_k(L_1,L_2;h)
 \ll\frac{Q\min(L_1,L_2)}h.
$$

After the literal $1/(L_1L_2)$ coefficient, the harmonic $h$ sum, the
new half-weight norm, and all rows, every fixed wrap class costs

$$
 \mathcal A_{k,U}\ll_\varepsilon DQX^\varepsilon.
$$

Therefore any selected packet with

$$
 |\mathcal K|\ll1+\frac{R^2}{Q}
 \asymp1+\frac{\sqrt M}{D}
$$

is target-safe:

$$
 \mathcal A_{\mathcal K,U}
 \ll_\varepsilon R^2DX^\varepsilon.
$$

This includes the complete $k=0$ collar and a symmetric small-wrap
packet.  The proof is absolute and retains all $L_i\ll E$, common
factors, imprimitive denominators, denominators dividing $N$, even
squarefree rows, and arbitrary finite exact prefixes.

There is a second strict edge.  If $M=O(1)$, then $D,E,L=O(1)$ and
$Q\asymp R^2$.  The accepted Round-148 actual profile and derivative
ledger give bounded $q$-variation.  On each allowed residue class
modulo $4L$, the reciprocal phase has second derivative
$\asymp R^{-2}$ on $O(R^2)$ terms.  Van der Corput plus Abel summation
therefore gives

$$
 |G_U(d)|\ll_\varepsilon RX^\varepsilon,
 \qquad
 \sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \ll_\varepsilon R^2DX^\varepsilon.
$$

This uses the actual profile.  A statement-only blind countermodel
correctly shows that bounded pointwise smoothness with uncontrolled
variation would be insufficient.

For $k\ne0$, the exact shifted-factor identities are

$$
 (NL_1-khr_1)(NL_2+khr_2)=N^2L_1L_2+kh\rho,
$$

$$
 r_2(NL_1-khr_1)=NL_2r_1+\rho,\qquad
 r_1(NL_2+khr_2)=NL_1r_2-\rho.
$$

Both factors are positive on the collar.  A fixed
$(L_1,L_2,h,k,\rho)$ has divisor multiplicity $X^\varepsilon$, but
separately summing every legal shift gives adverse raw capacity

$$
 \frac{NL_1L_2Q}{D}X^\varepsilon,
$$

which loses at least $R$ against trivial pair capacity.  This is a
no-go for separate absolute per-shift summation, not a signed lower
bound.

The primary-source audit finds no direct match in the
Bombieri--Iwaniec double large sieve, Duke--Friedlander--Iwaniec
quadratic divisor theorem, Bettin--Chandee determinant/inverse-fraction
forms, or Reuss fixed-shift squarefree correlation.  Their coefficients,
separability, weights, shift families, local cluster forms, or powers do
not match the literal large-wrap sum.  This is a scoped applicability
result, not a literature impossibility theorem.

Three terminal reviews are GREEN:

- `blind_fixed_wrap_lemma_review.md` for the all-$L$ fixed-wrap packet;
- `independent_conductor_round150_math_review.md` for the complete
  arithmetic, counting, bounded-$M$, endpoint, and scope seams; and
- `source_conductor_round150_final.md` for the source hypotheses,
  bounded-variation placement, large-wrap no-match, and downstream
  scope.

The first open collar is the growing-$M$ symmetric large-wrap band
outside $|k|\ll1+R^2/Q$.  The full centered range has size $N/Q$, a
factor $R^2$ larger than the owned packet.  At $D=1,L_1=L_2=1$, the
residual is the literal $\chi_4$ reciprocal sum with no row average.
A joint signed wrap estimate or a further exact recombination is still
needed.  The growing-$M$ generic non-collar also remains open.

Every $t\ge2$ layer and the independent Round-138 cross owner remain
open.  There is no change to M9--M1, M9--M2, endpoint uniformity, M9,
the conditional bridge, or the Gauss target.  The internally proved
exponent remains $1/3$; the audited external exponent remains

$$
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
$$
