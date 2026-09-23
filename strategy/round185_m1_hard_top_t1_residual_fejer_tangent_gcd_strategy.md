# Round 185 conductor strategy: hard-M1 t=1 residual Fejer tangent-gcd gate

- Round: 185
- Starting graph:
  f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0
- Selected owner:
  M9-M1-hard-top-high-radical-small-t-residual-estimate
- Frozen component: the exact no-pair plus selected neither/both residual
  of the literal hard-M1 t=1 face
- Planned allocation: 100% analytical/algebraic, 0% numerical theorem
  evidence
- Scheduled strategy checkpoint: Round 186, after analytic Rounds
  183--185

## 1. Frontier comparison

Round 183 proved the large-gcd non-half-integer-resonant primitive-ray
sector. Round 184 then proved the canonical selected-product XOR part of
the complete t=1 face. Three exact pieces remain inside the hard-M1
small-t owner.

1. The t=1 residual is already isolated as a literal coefficient on
   product rows N asymp L^2. Its Fejer reduction names one exact signed
   correlation and loses no endpoint information. Shiftwise triangle has
   L^3 X^epsilon energy capacity against the required L^2 X^epsilon.
2. The remaining t>=2 small-G incidences contain the same unresolved
   product cancellation together with square-multiplier and row-summing
   interfaces. Starting there would leave the t=1 obstruction untouched.
3. The large-G near-half-integer-resonant complement has only an L^(7/4)
   incidence envelope, but for arbitrary real X there is no accepted
   uniform metric count or signed estimate. Its apparent smaller deficit
   is not an available theorem.

The t=1 residual is therefore the smallest owner-relevant exact frontier.
It also admits a fresh, auditable transfer test: the accepted hard-M2
Fejer kernels contain coefficient-uniform parity, tangent, original-gcd,
and inward-cross-gcd counting reductions. Those finite reductions may be
rederived for M1 after mapping the odd character leg to d=v and its
cofactor to m=u. The M2 residual theorem and its later signed estimates do
not transfer; every M1 coefficient, selector, sign, cone, endpoint, and
restored power remains literal.

## 2. Frozen target

For each real X>=2, literal middle or lower hard-M1 residual shell L, and
sigma in {+1,-1}, retain the Round-184 coefficient

\[
 c_{N,\sigma}^{\rm rem}
 =\mu^2(N)\sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)\rho_N(d)
 a_{L,X}^{\mathrm{lit},\sigma}(N/d,d),
\tag{185.1}
\]

with complete zero extension. Here rho_N is one on every allocation of a
no-pair product and has truth table 1,0,0,1 on the selected-prime bits for
a selected product. Put R_0=ceil(L). The frozen analytic target is

\[
 \boxed{
 \Re\sum_{1\le r<R_0}\left(1-\frac r{R_0}\right)
 \sum_N c_{N+r,\sigma}^{\rm rem}
 \overline{c_{N,\sigma}^{\rm rem}}
 e\!\left(\frac{\sigma\sqrt X\,r}
 {\sqrt{N+r}+\sqrt N}\right)
 \ll_\varepsilon L^2X^\varepsilon.}
\tag{185.2}
\]

There is one real part outside the entire shift and incidence aggregate.
Equation (185.2) is sufficient, not asserted necessary, for

\[
 \left|\sum_Nc_{N,\sigma}^{\rm rem}e(\sigma\sqrt{XN})\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{185.3}
\]

A direct proof of (185.3) is also a successful full-target outcome. The
round does not replace the residual by an arbitrary coefficient class.

## 3. Tangent and gcd mechanism

Open both coefficients in (185.2), writing

\[
 N=dm,\qquad N+r=d'm',\qquad d,d'\text{ odd},
\tag{185.4}
\]

where d,d',m,m' are all asymp L on nonzero literal atoms. Set

\[
 a=d'-d,\qquad b=m'-m.
\]

The finite identities to test are

\[
 r=db+am+ab=db+am',\qquad
 a\equiv0\pmod2,\quad b\equiv r\pmod2,
\tag{185.5}
\]

and

\[
 \chi_4(d')\chi_4(d)=(-1)^{a/2}.
\tag{185.6}
\]

The intended first reductions are:

1. the endpoint-exact parity connector reducing the Fejer energy to even
   product shifts at constant cost;
2. an O(L^2 X^epsilon) count for the monotone tangent sector a,b>=0;
3. the original character-leg gcd normal form
   g=(d,d'), d=gu, d'=gv, vm'-um=r/g, giving
   O(L^3G_0^(-1)X^epsilon) for g>=G_0 and hence a target-safe fixed-
   proportion high-g sector; and
4. on the opposing sector ab<0, the inward cross-gcd parametrization. In
   the plus orientation, for example,

   \[
    d=\kappa u,\quad d'=\kappa u+2s,\quad
    m'=\kappa v,\quad m=\kappa v+2w,
    \quad r=2\kappa(sv-wu),
   \tag{185.7}
   \]

   with the opposite orientation treated separately. Along a primitive
   solution fibre s=s_0+ut, w=w_0+vt, the bare character alternates as
   a fixed sign times (-1)^t. The round must determine exactly which
   fixed-proportion cross-gcd sectors are target-safe by counting and
   where selector, squarefree, profile, endpoint, or zero-extension
   deletions prevent analytic cancellation.

All splits occur after the multiplicity-one literal divisor opening. A
product row may contribute incidences to several sectors; no row-level
density inference is allowed.

## 4. Capacity barriers and controls

- The full shifted correlation has L^3X^epsilon positive capacity; the
  missing energy factor is L.
- Parity reduction is a constant-cost identity, not cancellation.
- Monotone, high-gcd, or high-cross-gcd counting sectors do not prove that
  their complements are sparse or that the residual target holds.
- Costs gamma^(-1) and delta^(-1) must be restored. A fixed-proportion
  sector cannot be silently extended by taking gamma or delta to zero
  with L.
- The character alternation on a complete primitive fibre does not by
  itself control the literal retained fibre. The two independently
  selected residual masks, squarefree and coprimality deletions, moving
  profiles, hard values, endpoints, and zero extension must remain.
- Rowwise Abel, Poisson followed by absolute dual recombination, a
  positive Gram norm, a modulus per shift, and normalized involution
  averaging are known capacity or self-return routes.
- The accepted M2 reductions are method controls only. Promotion requires
  an M1 proof with d=v, m=u, both sigma, the strict cone 4m<d<16m, and
  every actual coefficient field.
- Arbitrary, dechirped, selector-erased, character-erased, and one-site
  arrays are diagnostic controls, not lower bounds for the fixed literal
  coefficient.

No numerical theorem evidence is planned. Python or Mathematica may be
used only for bounded exact parity, parametrization, or falsification
checks, and every important computation must be reproduced by the
conductor.

## 5. Exit gates

Round 185 closes under exactly one label:

1. hard_m1_t1_residual_target: prove (185.3), either through (185.2) or
   directly, with every literal field and both signs;
2. strict_hard_m1_t1_residual_tangent_gcd_sector: prove the narrowest
   owner-complete incidence sectors and an exact complementary correlation,
   without promoting complete t=1; or
3. hard_m1_t1_residual_tangent_gcd_capacity_or_self_return_no_go: prove a
   precise obstruction for the frozen tangent-gcd mechanism while leaving
   the literal target viable.

At least one important finite lemma receives statement-only independent
rederivation. Any candidate promotion requires separate reviews of the
Fejer/parity identity, tangent multiplicity, gcd and cross-gcd powers,
literal coefficient and endpoint scope, blind post-unmask consistency,
and downstream ownership. The conductor alone may synthesize or patch the
graph.

## 6. Proof-state boundary

Even a complete t=1 residual theorem would prove only the complete t=1
face after adjoining the Round-184 XOR sector. It would leave every
t>=2 small-G incidence and the large-G near-resonant complement open, so
the complete small-t owner and hard signed cone would still be open. The
independent smooth M1 parent, GAR, M9-M1, all M2 parents, endpoint
uniformity, M9, both bridges, the quarter theorem, and every exponent are
quarantined. Round 186 is the mandatory full-proof strategy and current-
primary-literature review after this analytic round closes.
