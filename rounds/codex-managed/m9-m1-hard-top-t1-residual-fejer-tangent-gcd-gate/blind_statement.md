# Round 185 statement-only hard-M1 residual Fejer tangent-gcd problem

This packet is self-contained. Do not use a proof graph, strategy file,
prior round, sibling report, source, or conductor analysis.

Put e(z)=exp(2 pi i z). Let L>=2, X>=2, sigma in {+1,-1}, and
R_0=ceil(L). For each squarefree positive integer N, choose canonically at
most one unordered pair of distinct odd prime divisors {p_N,q_N} with
chi_4(p_Nq_N)=-1. The selector depends only on N and fixed external
parameters, never on an allocation N=dm. Define

\[
 \rho_N(d)=
 \begin{cases}
  1,&\text{if no pair is selected},\\
  1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
   +2\mathbf1_{p_Nq_N\mid d},&\text{otherwise}.
 \end{cases}
\tag{B185.1}
\]

Thus the selected-pair truth table is 1,0,0,1 on the two selected-prime
bits. Let A_{L,X}^sigma(m,d) be one fixed literal coefficient, not an
arbitrary array. It is zero unless

\[
 (m,d)=1,\qquad d\text{ odd},\qquad 4m<d<16m,
 \qquad m,d\asymp L,
\tag{B185.2}
\]

and unless every fixed shell, height, profile, floor, star, half-weight,
hard-sample, crossing, endpoint, and zero-extension predicate holds. It
obeys only the uniform bound

\[
 |A_{L,X}^\sigma(m,d)|\ll\mathcal X,
\tag{B185.3}
\]

where mathcal X denotes an allowed subpolynomial loss. No variation or
Fourier-norm hypothesis in N, the selector, or a tangent-fibre parameter
may be assumed.

Define the exact residual coefficient

\[
 c_{N,\sigma}^{\rm rem}
 =\mu^2(N)\sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)\rho_N(d)A_{L,X}^\sigma(N/d,d),
\tag{B185.4}
\]

extend it by zero outside a consecutive containing interval of
M_L asymp L^2 sites, and suppose the accepted diagonal estimate is

\[
 \sum_N|c_{N,\sigma}^{\rm rem}|^2\ll L^2\mathcal X.
\tag{B185.5}
\]

Put z_N=c_{N,\sigma}^{rem}e(sigma sqrt(XN)). The exact sliding energy is

\[
 \mathfrak E_R={1\over R}\sum_{s\in\mathbb Z}
 \left|\sum_{j=0}^{R-1}z_{s+j}\right|^2
 =D_L+2\Re\mathfrak C_R,
\tag{B185.6}
\]

\[
 \mathfrak C_R=
 \sum_{1\le r<R}\left(1-{r\over R}\right)
 \sum_Nc_{N+r,\sigma}^{\rm rem}\overline{c_{N,\sigma}^{\rm rem}}
 e\!\left({\sigma\sqrt X\,r\over\sqrt{N+r}+\sqrt N}\right).
\tag{B185.7}
\]

There is one real part outside the entire aggregate. The proposed
correlation target is

\[
 \boxed{\Re\mathfrak C_{R_0}\ll L^2\mathcal X.}
\tag{B185.8}
\]

Together with the exact sliding-window Cauchy connector, (B185.8) is
sufficient for

\[
 \left|\sum_Nc_{N,\sigma}^{\rm rem}e(\sigma\sqrt{XN})\right|
 \ll L^{3/2}\mathcal X.
\tag{B185.9}
\]

Independently do all of the following.

1. Reprove the sliding identity and the endpoint-exact inequality reducing
   its energy at constant cost to the even product shifts. Do not delete
   the terminal even gap for odd R.
2. Open both coefficients multiplicity-one as N=dm and N+r=d'm'. With
   a=d'-d and b=m'-m, verify all parity, product-difference, and character
   identities, retaining both orientations and sigma.
3. Count the complete monotone tangent sector a,b>=0. Treat every literal
   restriction as a deletion or weight, and state the exact opposing
   complement rather than inferring row density.
4. Put g=(d,d'), derive the primitive linear normal form and its row
   multiplicity, and decide whether g>=gamma L is target-safe for fixed
   gamma>0. Restore every gamma dependence.
5. On ab<0, derive both inward-cross-gcd parametrizations. For the plus
   orientation test

   \[
    d=\kappa u,\quad d'=\kappa u+2s,\quad
    m'=\kappa v,\quad m=\kappa v+2w,
    \quad r=2\kappa(sv-wu),
   \tag{B185.10}
   \]

   and the primitive solution step s=s_0+ut, w=w_0+vt. Determine the
   exact bare chi_4 law and whether a fixed-proportion range
   kappa>=delta L is target-safe by counting. Restore every delta
   dependence.
6. Test whether alternating character on the complete primitive fibre
   survives the independently varying residual selectors, squarefree and
   coprimality deletions, profiles, endpoints, and zero extension. An
   arbitrary-coefficient countermodel may refute a coefficient-uniform
   mechanism but is not literal physical lower mass.
7. Give either a proof of (B185.8) or (B185.9), the widest rigorously
   target-safe tangent/gcd incidence sectors with their exact complement,
   or the narrowest exact capacity/self-return no-go and the first
   additional literal relation still needed.

Taking a modulus per shift, row, gcd, orientation, selector status, or
dual mode before a signed estimate is forbidden. Parity splitting,
positive Gram energy, rowwise Abel, and Poisson followed by positive
recombination do not count as cancellation. A fixed gamma or delta may not
silently shrink with L.

A complete residual theorem would prove only the complete t=1 face after
adjoining the already separated exchange sector. It would not prove any
t>=2 component, near-resonant component, parent estimate, bridge, global
theorem, or exponent. Computation, if any, is diagnostic only.

Return exactly:

1. Result.
2. Exact statement and hypotheses.
3. Proof or derivation.
4. First doubtful or unproved step.
5. Required control test and outcome.
6. Dependencies and exact artifacts used.
7. Recommended state effect.
