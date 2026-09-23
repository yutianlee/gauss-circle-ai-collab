# Hard-M1 t=1 comparable-factor exchange sector and residual Fejer reduction

- Campaign:
  m9-m1-hard-top-t1-comparable-factor-exchange-gate
- Starting graph SHA-256:
  a8e0e5d84c0c5047e0c96f11128dd215ae035bdd4355bd68ad28dc87afe6cfbd
- Exact source candidate:
  rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/candidates/formalized_hard_m1_t1_comparable_factor_exchange_sector.md
  (SHA-256
  c514b10bed4c673618179c158258c362373696730c691900d250ed43e379e97f)
- Evidence status: durable proof-kernel candidate; pending final kernel and
  State Patch validation
- Numerical work: none

## Statement

Fix real \(X\geq2\), one literal middle or lower residual hard-M1 shell
\(L\), \(\sigma\in\{+1,-1\}\), and \(\kappa>0\).  Put

\[
 y=\lfloor\sqrt X\rfloor,\qquad q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor .
\]

Let \(a_{L,X}^{\mathrm{lit},\sigma}(u,v)\) be the complete normalized
hard-M1 stationary symbol, extended by zero off every original shell,
height, strict-cone, profile, floor, star, half-weight, hard-sample,
crossing, and endpoint predicate.  The complete \(t=1\) face is

\[
 \mathcal T_{L,X,\sigma}
 =\sum_{\substack{(u,v)=1,\ v\ {\rm odd},\ 4u<v<16u\\
                   uv\ {\rm squarefree}}}
 \chi_4(v)a_{L,X}^{\mathrm{lit},\sigma}(u,v)
 e(\sigma\sqrt{Xuv}).
\tag{K184.1}
\]

For every squarefree \(N\), canonically select at most one unordered pair
of distinct odd prime divisors \(\{p_N,q_N\}\) satisfying

\[
 \chi_4(p_Nq_N)=-1,\qquad
 |\log(q_N/p_N)|\leq\kappa L^{-1/2},
\tag{K184.2}
\]

using only \((N,L,\kappa)\), never the allocation \(N=uv\).  Let
\(\mathcal T^{\rm cp}_{L,X,\sigma}\) be the complete incidence subsum of
(K184.1) on which a pair is selected and exactly one selected prime
divides the odd character-bearing leg \(v\).  Then

\[
 \boxed{
 |\mathcal T^{\rm cp}_{L,X,\sigma}|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.}
\tag{K184.3}
\]

The exact complement is every allocation of a no-pair product plus the
neither/both allocations of a selected product.  If

\[
 \rho_N(v)=
 \begin{cases}
  1,&\text{no pair is selected},\\
  1-\mathbf1_{p_N\mid v}-\mathbf1_{q_N\mid v}
    +2\mathbf1_{p_Nq_N\mid v},&\text{a pair is selected},
 \end{cases}
\tag{K184.4}
\]

then

\[
 \mathcal T_{L,X,\sigma}
 =\mathcal T^{\rm cp}_{L,X,\sigma}
  +\sum_Nc_{N,\sigma}^{\rm rem}e(\sigma\sqrt{XN}),
\tag{K184.5}
\]

\[
 c_{N,\sigma}^{\rm rem}
 =\mu^2(N)\sum_{v\mid N,\ v\ {\rm odd}}
 \chi_4(v)\rho_N(v)
 a_{L,X}^{\mathrm{lit},\sigma}(N/v,v).
\tag{K184.6}
\]

At \(R=\lceil L\rceil\), a sufficient still-open estimate for the exact
residual in (K184.5) is

\[
 \Re\sum_{1\leq r<R}\left(1-\frac rR\right)
 \sum_Nc_{N+r,\sigma}^{\rm rem}
 \overline{c_{N,\sigma}^{\rm rem}}
 e\!\left(\frac{\sigma\sqrt X\,r}
 {\sqrt{N+r}+\sqrt N}\right)
 \ll_\varepsilon L^2X^\varepsilon.
\tag{K184.7}
\]

There is one outer real part.  Equation (K184.7) is not proved.

## Proof of the strict sector

The accepted squarefree-radical coordinates give

\[
 t=G\sqrt{\frac{uv}{\operatorname{sf}(uv)}}.
\]

Thus \(t=1\) is exactly \(G=1\), \((u,v)=1\), and \(uv\) squarefree,
with multiplicity one.  Literal support gives \(u,v\asymp L\) and
\(uv\asymp L^2\), so the coefficient-insensitive capacity is
\(O_\varepsilon(L^2X^\varepsilon)\).

For a selected pair, let \(\mathscr A_N^\oplus\) be the complete ambient
XOR allocation set and define

\[
 \tau_N(u,v)=
 \begin{cases}
  (up_N/q_N,\ vq_N/p_N),&q_N\mid u,\ p_N\mid v,\\
  (uq_N/p_N,\ vp_N/q_N),&p_N\mid u,\ q_N\mid v.
 \end{cases}
\tag{K184.8}
\]

Squarefreeness and coprimality make the quotients integral.  The map is a
fixed-point-free multiplicity-one involution.  It preserves \(N\), the
product phase, squarefreeness, coprimality, parity, and the selector, and

\[
 \chi_4(v')=\chi_4(v)\chi_4(p_Nq_N)=-\chi_4(v).
\tag{K184.9}
\]

The physical support need not be invariant.  Zero extension and ambient
reindexing give the exact identity

\[
 \mathcal T^{\rm cp}_{L,X,\sigma}
 =\frac12\sum_N\sum_{(u,v)\in\mathscr A_N^\oplus}
 \chi_4(v)e(\sigma\sqrt{XN})
 \{a(u,v)-a(\tau_N(u,v))\}.
\tag{K184.10}
\]

The accepted M1 transform gives the exact moving-factor ledger

\[
 \eta_L(u)\Phi\!\left(\frac{u}{H+1}\right)
 W\!\left(\sqrt{\frac{4q_Xu}{v}}\right)
 \left(\frac{L^2}{uv}\right)^{3/4},
\tag{K184.11}
\]

up to allocation-independent shell and sign constants of
\(O_\varepsilon(X^\varepsilon)\) and the fixed finite family of literal
masks and endpoint traces.  The dyadic profile \(\eta_L\) has
scale-normalized discrete BV; \(\Phi\) is uniformly \(C^1\); and \(W\)
is uniformly \(C^1\) on each literal smooth cell.

Write \(\theta_N=\log(q_N/p_N)\).  On an exchange orbit,

\[
 (u',v')=(e^{\pm\theta_N}u,e^{\mp\theta_N}v),\qquad
 |u'-u|+|v'-v|\ll_\kappa L^{1/2}+1.
\tag{K184.12}
\]

Restrict coefficient-difference estimates to the
\(\tau_N\)-closed active set

\[
 \mathscr B_{L,X,\sigma,\kappa}
 =\{(N,u,v):(u,v)\in\mathscr A_N^\oplus,\
 a(u,v)\ne0\ {\rm or}\ a(\tau_N(u,v))\ne0\}.
\tag{K184.13}
\]

Outside this set both terms in (K184.10) vanish.  Inside it both orbit
legs lie in a fixed \(O(L)\)-by-\(O(L)\) enlarged box.

The product-only power in (K184.11) is invariant.  On common smooth
cells, the \(\Phi\)- and \(W\)-differences are
\(O_\kappa(L^{-1/2})\), so their total contribution over
\(O(L^2)\) active pairs is
\(O_{\kappa,\varepsilon}(L^{3/2}X^\varepsilon)\).

For the dyadic factor, telescoping and the active-box multiplicity give

\[
\begin{aligned}
 \sum_{(N,u,v)\in\mathscr B_{L,X,\sigma,\kappa}}
 |\eta_L(u')-\eta_L(u)|
 &\leq
 O_\kappa(L^{3/2}+L)
 \sum_m|\eta_L(m+1)-\eta_L(m)|\\
 &\ll_\kappa L^{3/2}.
\end{aligned}
\tag{K184.14}
\]

Indeed a fixed increment \(m\) can be crossed only by
\(O_\kappa(L^{1/2}+1)\) values of \(u\) and \(O(L)\) values of \(v\);
the ordered pair determines \(N\), and the canonical selector provides
at most one partner.

A fixed vertical, horizontal, or ratio face is crossed only in a collar
of width \(O_\kappa(L^{1/2}+1)\), containing
\(O_\kappa(L^{3/2}+L)\) ordered pairs.  The exact M1 transform has a
fixed finite family of such faces: the strict \(4,16\) cone, frequency
and height entries and exits, profile support and plateau edges,
real-\(X\) ratio crossings, and missing partners.  Exact floor, star,
tie, half-weight, and sampled endpoint traces have \(O(L)\) sites per
face.  Consequently the coefficient-weighted different-cell cost is

\[
 \sum_{\substack{(N,u,v)\in\mathscr B_{L,X,\sigma,\kappa}\\
                  (u,v),\tau_N(u,v)\ {\rm in\ different\ cells}}}
 (|a(u,v)|+|a(\tau_N(u,v))|)
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.
\tag{K184.15}
\]

The discrete product rule, (K184.11)--(K184.15), and arithmetic deletion
therefore give

\[
 \sum_{(N,u,v)\in\mathscr B_{L,X,\sigma,\kappa}}
 |a(u,v)-a(\tau_N(u,v))|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.
\tag{K184.16}
\]

Insert this in the exact character-reversing identity (K184.10), taking
triangle only after pairing.  This proves (K184.3), uniformly in real
\(X\), every literal endpoint, and both signs.

## Exact residual and Fejer reduction

The truth table of (K184.4) is \(1,0,0,1\) on the selected-prime bits
\(00,10,01,11\).  Hence (K184.5)--(K184.6) are an exact disjoint
partition.  If \(M_N\) is the odd part of \(N\), the ambient
constant-amplitude residual sign mass is

\[
 \sum_{v\mid M_N}\chi_4(v)\rho_N(v)
 =\begin{cases}
  \prod_{r\mid M_N}(1+\chi_4(r)),&\text{no pair},\\
  (1+\chi_4(p_Nq_N))
  \prod_{r\mid M_N/(p_Nq_N)}(1+\chi_4(r))=0,
  &\text{selected pair}.
 \end{cases}
\tag{K184.17}
\]

The second line is only ambient balance; the physical coefficient and
one-sided cone destroy any automatic cancellation.

Ordering the retained residual odd divisors of one \(N\), putting
\(C_j=\sum_{i\leq j}\chi_4(v_i)\), and zero-extending the amplitude at
both ends, exact Abel summation gives

\[
 \left|\sum_i\chi_4(v_i)a_i\right|
 \leq\frac12\operatorname{osc}(C_N)
       \sum_j|a_{j+1}-a_j|.
\tag{K184.18}
\]

Positive summation gives only the \(L^2X^\varepsilon\) capacity because
no target-sized weighted average of \(\operatorname{osc}(C_N)\) is
known.

For the product direction, set
\(z_N=c_{N,\sigma}^{\rm rem}e(\sigma\sqrt{XN})\), extend by zero outside
a containing interval of \(M_L\asymp L^2\) sites, and define

\[
 \mathfrak E_{R,\sigma}^{\rm rem}
 ={1\over R}\sum_{s\in\mathbb Z}
 \left|\sum_{j=0}^{R-1}z_{s+j}\right|^2.
\tag{K184.19}
\]

Every pair at gap \(r<R\) occurs in exactly \(R-r\) windows, so

\[
\begin{aligned}
 \mathfrak E_{R,\sigma}^{\rm rem}
 ={}&\sum_N|c_{N,\sigma}^{\rm rem}|^2\\
 &+2\Re\sum_{1\leq r<R}\left(1-\frac rR\right)
 \sum_Nc_{N+r,\sigma}^{\rm rem}
 \overline{c_{N,\sigma}^{\rm rem}}
 e\!\left(\frac{\sigma\sqrt X\,r}
 {\sqrt{N+r}+\sqrt N}\right).
\end{aligned}
\tag{K184.20}
\]

There is no endpoint error.  Summing all windows back and applying
Cauchy gives

\[
 |\mathcal T^{\rm rem}_{L,X,\sigma}|^2
 \leq\frac{M_L+R-1}{R}\mathfrak E_{R,\sigma}^{\rm rem}.
\tag{K184.21}
\]

The diagonal is \(O_\varepsilon(L^2X^\varepsilon)\).  With
\(R=\lceil L\rceil\), the prefactor is \(O(L)\), so (K184.7) makes the
energy target-square safe and proves the residual target.  But (K184.7)
is open.  A modulus at each shift bounds the energy only by
\(O_\varepsilon(L^3X^\varepsilon)\) and returns the scalar
\(L^2X^\varepsilon\) capacity.

## Mechanism controls and scope

A one-prime toggle multiplies \(v/u\in(4,16)\) by \(p^{\pm2}\) and has
disjoint physical support.  A normalized average of full divisor-lattice
involutions is an exact rewriting.  A product whose odd primes are all
\(1\pmod4\) has no eligible pair and no character reversal.  A supported
semiprime has its two prime legs separated by a ratio greater than four,
so its only pair fails (K184.2) once
\(\kappa L^{-1/2}<\log4\).  These facts show why fixed-product local
exchange does not cover the residual.  They are not a density theorem,
literal lower mass, or a disproof of the complete \(t=1\) estimate.

The proved statement is only the possibly empty strict incidence sector
(K184.3).  The exact residual, the rest of \(t=1\), all \(t\geq2\)
small-G incidences, the large-G near-resonant complement, the complete
small-\(t\) owner, both M1 parents, every M2 owner, endpoint uniformity,
M9, both bridges, the Gauss-circle target, and every exponent remain
unchanged.

## Dependencies and reviewed evidence

Direct accepted dependencies:

- M9-M1-hard-top-squarefree-radical-sector-reduction;
- M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector;
- M9-M1-top-endpoint-transform;
- M9-M1-frequency-phase-diagram-R10;
- H4-Phi-regularity;
- M9-M2-dyadic-weight-nondegeneracy; and
- Divisor-bound-elementary.

Round evidence:

- the exact source candidate named above;
- reports/literal_t1_exchange_residual_attack.md;
- reports/m2_transfer_transport_capacity_audit.md;
- reports/blind_complete_t1_exchange_rederivation.md;
- reviews/selector_exchange_character_blind_post_unmask_review.md;
- reviews/coefficient_profile_endpoint_power_seam_review.md;
- reviews/coefficient_profile_endpoint_power_post_repair_verification.md;
- reviews/residual_transport_correlation_owner_scope_review.md; and
- reviews/conductor_round184_report_reconciliation.md.

The M2 close-pair and residual kernels are method controls only, not
dependencies of the M1 theorem.  No external theorem or numerical
experiment is used.
