# 1. Result

Let
\[
 \lambda_{N,\sigma}(d):=
 \mu^2(N)\rho_N(d)
 a_{L,X}^{\mathrm{lit},\sigma}(N/d,d)
 \mathbf 1_{d\mid N}\mathbf 1_{2\nmid d},
 \qquad
 c_{N,\sigma}^{\mathrm{rem}}
 =\sum_d\chi_4(d)\lambda_{N,\sigma}(d),
\]
with the literal coefficient extended by zero off its complete real-
\(X\), dyadic, strict-comparability, coprimality, squarefreeness, and
residual-selector support.  Thus this definition is exactly
\[
 c_{N,\sigma}^{\mathrm{rem}}
 =\mu^2(N)\sum_{\substack{d\mid N\\2\nmid d}}
 \chi_4(d)\rho_N(d)
 a_{L,X}^{\mathrm{lit},\sigma}(N/d,d).
\]
On its support, \(N=dm\asymp L^2\), \(d,m\asymp L\),
\(4m<d<16m\), \((d,m)=1\), and
\(\lambda_{N,\sigma}(d)\ll_\varepsilon X^\varepsilon\).

The frozen complete residual estimate is **not proved**.  What is proved
is the following widest exact target-safe decomposition obtainable from
parity, tangent displacement geometry, the original gcd, and the inward
cross gcd without imposing any regularity on the literal M1 fields.
Put \(R_0=\lceil L\rceil\), and let \(G_0,K_0\ge1\).  After the exact
parity reduction to even shifts, the union of

1. the monotone tangent sector;
2. the opposing tangent sector with original gcd \(g\ge G_0\); and
3. sequentially inside \(g<G_0\), the opposing tangent sector with
   orientation-dependent inward cross gcd \(\kappa_*\ge K_0\),

has total absolute contribution
\[
 \ll_\varepsilon
 \left(L^2+\frac{L^3}{G_0}+\frac{L^3}{K_0}\right)X^\varepsilon.
\tag{1.1}
\]
Consequently, for every fixed \(\gamma,\delta>0\), the disjoint sector
union with \(G_0=\gamma L\) and \(K_0=\delta L\) is target-safe:
\[
 \ll_{\varepsilon,\gamma,\delta}L^2X^\varepsilon.
\tag{1.2}
\]
The exact complement is the even-shift, opposing-tangent sector
\[
 ab<0,\qquad g<G_0,\qquad \kappa_*<K_0,
\tag{1.3}
\]
with every literal endpoint factor retained.  It is given below by two
explicit cross-gcd fibre sums under one, and only one, outer real part.
Its first genuinely open relation is a joint signed \((n,t)\)-fibre
estimate.  Bare alternation, rowwise Abel summation, one-variable
derivative or B-process estimates, and absolute recombination of dual
modes do not prove it: each returns the pre-existing capacity scale.
This is a route-scoped self-return no-go, not a lower bound for the
literal residual.

# 2. Exact statement and hypotheses

Fix either \(\sigma\in\{+1,-1\}\), and write \(J=\sqrt X\).  No
integrality of \(X\) is assumed.  The sole outer phase is
\(e(\sigma J\sqrt N)\); the full literal M1 coefficient in
\(\lambda_{N,\sigma}(d)\) is not replaced by a majorant until a sector
has been declared target-safe.  In particular, it retains the exact
real-\(X\) endpoints, shell fields, every prime incidence, the complete
residual selector \(\rho_N(d)\), and all powers occurring in the
literal coefficient.

Let
\[
 z_N=c_{N,\sigma}^{\mathrm{rem}}e(\sigma J\sqrt N),
\]
extended by zero on the entire integer line, and put
\[
 D=\sum_N|z_N|^2,
 \qquad
 C_{R_0}=\sum_{1\le r<R_0}
 \left(1-\frac r{R_0}\right)
 \sum_N z_{N+r}\overline {z_N}.
\tag{2.1}
\]
The frozen correlation target is
\[
 \Re C_{R_0}\ll_\varepsilon L^2X^\varepsilon.
\tag{2.2}
\]
The exact Fejer identity is
\[
 E_{R_0}:=\frac1{R_0}\sum_s
 \left|\sum_{0\le j<R_0}z_{s+j}\right|^2
 =D+2\Re C_{R_0},
\tag{2.3}
\]
and zero extension makes (2.3) endpoint-free.  Since
\(D\ll_\varepsilon L^2X^\varepsilon\) and the support length is
\(M_L\asymp L^2\), (2.2) would give
\[
 \left|\sum_Nz_N\right|^2
 \le \frac{M_L+R_0-1}{R_0}E_{R_0}
 \ll_\varepsilon L^3X^\varepsilon,
\]
hence the desired scalar residual bound
\(\sum_Nz_N\ll_\varepsilon L^{3/2}X^\varepsilon\).

For an opened atom pair at shift \(r>0\), write
\[
 N=dm,\qquad N+r=d'm',\qquad
 a=d'-d,\qquad b=m'-m.
\tag{2.4}
\]
Both \(d,d'\) are odd.  On even shifts, \(a,b\) are even.  The
monotone sector is \(a,b\ge0\).  All remaining nonempty cases have
\(ab<0\).  In that opposing sector define
\[
 g=(d,d').
\tag{2.5}
\]
Inside \(g<G_0\), define the inward cross gcd by
\[
 \kappa_*=(d,m')\quad(a>0>b),
 \qquad
 \kappa_*=(d',m)\quad(a<0<b).
\tag{2.6}
\]
The thresholds are applied sequentially, so the three safe pieces and
the complement (1.3) are disjoint and exhaustive after parity and the
empty tangent cases.

# 3. Proof or derivation

## 3.1 Fejer and parity, with the terminal weight retained

Split every length-\(R_0\) block into its even-index and odd-index
subblocks and use \(|A+B|^2\le2|A|^2+2|B|^2\).  Summing over starting
points gives the exact parity connector
\[
 E_{R_0}\le2E_{R_0}^{(2)},
 \qquad
 \Re C_{R_0}\le\frac D2+2\Re C_{R_0}^{(2)},
\tag{3.1}
\]
where \(C_{R_0}^{(2)}\) contains only even shifts and their exact
Fejer weights.  If \(R_0=2S+1\), the final even gap has weight
\(1/R_0\); it has not been discarded.  It is therefore enough, up to
an absolute constant and the already acceptable diagonal, to analyze
all even \(1\le r<R_0\).

Opening (2.4),
\[
 r=d'm'-dm\ \,\text{in product notation, and exactly}\ \,
 r=db+am+ab=db+a m'.
\tag{3.2}
\]
Since \(d,d'\) are odd, \(a\) is even, while (3.2) gives
\(b\equiv r\pmod2\).  Thus both are even in (3.1).  Moreover
\[
 \chi_4(d')\chi_4(d)=(-1)^{a/2}.
\tag{3.3}
\]

## 3.2 Tangent geometry

If \(a,b\ge0\), then from (3.2) and \(d,m'\asymp L\),
\[
 r\gg L(a+b).
\tag{3.4}
\]
Because \(r<R_0\ll L\), only \(O(1)\) displacement pairs \((a,b)\)
occur.  Each has \(O(L^2)\) admissible endpoint atoms, while every
literal coefficient product is \(O_\varepsilon(X^\varepsilon)\).
Thus the whole monotone sector is
\[
 O_\varepsilon(L^2X^\varepsilon).
\tag{3.5}
\]
The cases \(a,b\le0\), and the one-zero cases with the nonzero
coordinate negative, are empty for \(r>0\).  Hence the exact remaining
tangent sector has \(ab<0\).

## 3.3 Original-gcd tail

Put \(d=gu,d'=gv\), with \((u,v)=1\).  Necessarily \(g\mid r\); for
\(h=r/g\),
\[
 vm'-um=h.
\tag{3.6}
\]
Every row of (3.6) is
\[
 m=m_0+vt,\qquad m'=m'_0+ut,
\tag{3.7}
\]
and the product step is
\[
 N(t+1)-N(t)=guv=\frac{dd'}g.
\tag{3.8}
\]
For fixed \(g,u,v,h\), the literal support therefore contains
\(O(1+g)\) row points.  Since \(u,v,h\ll L/g\), the number of
incidences for fixed \(g\) is
\[
 \ll \left(\frac Lg\right)^3(1+g)
 \ll \frac{L^3}{g^2}
\tag{3.9}
\]
(the harmless endpoint and divisor losses are absorbed into
\(X^\varepsilon\)).  Hence
\[
 \sum_{g\ge G_0}\text{absolute contribution}
 \ll_\varepsilon \frac{L^3}{G_0}X^\varepsilon.
\tag{3.10}
\]
This split is made after opening divisor incidences; it is not an
illegitimate product-row partition.

## 3.4 Inward cross-gcd tail and its complete fibre coordinates

Consider first \(a>0>b\).  Put
\[
 d=\kappa u,\quad d'=\kappa u+2s,\quad
 m'=\kappa v,\quad m=\kappa v+2w,
\tag{3.11}
\]
where
\[
 \kappa=(d,m'),\qquad \kappa,u\text{ odd},\qquad (u,v)=1.
\]
Then
\[
 r=2\kappa n,\qquad sv-wu=n>0.
\tag{3.12}
\]
With \(\bar v\) the inverse of \(v\pmod u\), and with least residues
in \(\{0,\ldots,u-1\}\), set
\[
 s_0=[\bar v n]_u,\qquad w_0=\frac{s_0v-n}{u},\qquad
 s_t=s_0+ut,\quad w_t=w_0+vt.
\tag{3.13}
\]
For \(u=1\), this means \(s_0=0\).  The two products are
\[
 N_t^+=\kappa u(\kappa v+2w_t),\qquad
 N_t^++2\kappa n=\kappa v(\kappa u+2s_t),
\tag{3.14}
\]
and both advance by \(2\kappa uv\).  Furthermore
\[
 \chi_4(d')\chi_4(d)
 =E_u(\bar v n)(-1)^t,\qquad
 E_u(x):=(-1)^{[x]_u}.
\tag{3.15}
\]

For the other orientation \(a<0<b\), put
\[
 d'=\kappa u,\quad d=\kappa u+2s,\quad
 m=\kappa v,\quad m'=\kappa v+2w,
\tag{3.16}
\]
so that \(uw-sv=n>0\), \(r=2\kappa n\), and take
\[
 s_0=[-\bar v n]_u,\qquad w_0=\frac{n+s_0v}{u},\qquad
 s_t=s_0+ut,\quad w_t=w_0+vt.
\tag{3.17}
\]
Then
\[
 N_t^-=\kappa v(\kappa u+2s_t),\qquad
 N_t^-+2\kappa n=\kappa u(\kappa v+2w_t),
\tag{3.18}
\]
and the character factor is
\[
 E_u(-\bar v n)(-1)^t.
\tag{3.19}
\]

Squarefreeness and endpoint coprimality give, in either orientation,
the exact fibre-stable identity
\[
 g=(d,d')=(u,n),
\tag{3.20}
\]
not \(g=\kappa\).  For example, in (3.11) squarefreeness gives
\((\kappa,s)=1\); hence \((d,d')=(u,s)=(u,n)\), the last equality
following from \(sv\equiv n\pmod u\) and \((u,v)=1\).

For fixed \(\kappa\), let \(Y=L/\kappa\).  The support gives
\(u,v,n\ll Y\), and a fibre has
\[
 O\!\left(1+\frac{L^2}{\kappa uv}\right)
\tag{3.21}
\]
points.  Therefore
\[
 \sum_{u,v,n\ll Y}
 \left(1+\frac{L^2}{\kappa uv}\right)
 \ll_\varepsilon \frac{L^3}{\kappa^2}X^\varepsilon,
\tag{3.22}
\]
and, with no lower restriction on \(r\),
\[
 \sum_{\kappa\ge K_0}\text{absolute contribution}
 \ll_\varepsilon \frac{L^3}{K_0}X^\varepsilon.
\tag{3.23}
\]
In particular, every even shift \(1\le r<R_0\), including shifts at
or below any fixed polylogarithmic threshold, is included literally in
(3.22)--(3.23).  No small-shift range has been dropped.

Equations (3.5), (3.10), and (3.23) prove (1.1).

## 3.5 Exact complement under one outer real part

Let \(\mathbf 1_{\mathcal H^\pm}\) denote the complete literal
indicator imposing all of the following, without smoothing:

- \(1\le2\kappa n<R_0\), \(\kappa<K_0\), and \((u,n)<G_0\);
- the corresponding orientation (3.11) or (3.16), with
  \(s_t,w_t\ge1\);
- every original squarefree, coprimality, dyadic-shell,
  \(4m<d<16m\), real-\(X\) endpoint, selected-prime incidence, and
  residual-selector condition already present in the two endpoint
  \(\lambda\)'s.

Define
\[
 \begin{aligned}
 \Lambda^+_{\kappa,u,v,n,t}
 &:={\bf1}_{\mathcal H^+}
 \left(1-\frac{2\kappa n}{R_0}\right)
 \lambda_{N_t^++2\kappa n,\sigma}(\kappa u+2s_t)
 \overline{\lambda_{N_t^+,\sigma}(\kappa u)},\\
 \Lambda^-_{\kappa,u,v,n,t}
 &:={\bf1}_{\mathcal H^-}
 \left(1-\frac{2\kappa n}{R_0}\right)
 \lambda_{N_t^-+2\kappa n,\sigma}(\kappa u)
 \overline{\lambda_{N_t^-,\sigma}(\kappa u+2s_t)},
 \end{aligned}
\tag{3.24}
\]
and
\[
 \Psi^\pm_{\kappa,u,v,n,t}
 :=\sigma J\bigl(\sqrt{N_t^\pm+2\kappa n}-\sqrt{N_t^\pm}\bigr).
\tag{3.25}
\]
Then the unresolved complement to the parity-reduced correlation is
exactly
\[
 \boxed{\quad
 \Re\!\sum_{\substack{\kappa,u\ {\rm odd}\\(u,v)=1}}
 \sum_{n\ge1}\sum_t
 \left[
 E_u(\bar v n)\Lambda^+_{\kappa,u,v,n,t}
 e\!\left(\Psi^+_{\kappa,u,v,n,t}+\frac t2\right)
 +E_u(-\bar v n)\Lambda^-_{\kappa,u,v,n,t}
 e\!\left(\Psi^-_{\kappa,u,v,n,t}+\frac t2\right)
 \right].\quad}
\tag{3.26}
\]
There is one real part outside both orientations, all shifts, all
divisor incidences, and every later split.  Neither sign \(\sigma\) nor
the complex conjugation at the left endpoint has been suppressed.

## 3.6 First open relation and route-scoped self-return

For odd \(u\), the exact discrete transform of the anchor is
\[
 \widehat E_u(k)
 :=\sum_{a\bmod u}E_u(a)e(-ka/u)
 =\frac2{1+e(-k/u)}
 =\frac{e(k/(2u))}{\cos(\pi k/u)}.
\tag{3.27}
\]
Thus Fourier inversion is exact and
\[
 \frac1u\sum_{k\bmod u}|\widehat E_u(k)|\ll\log(2u),
 \qquad
 \frac1{u^2}\sum_k|\widehat E_u(k)|^2=1.
\tag{3.28}
\]
The large near-half aliases are part of (3.27); they are not deleted.
If \(q=u/(u,n)\), the primitive reduction is also exact:
\(E_u(\pm\bar v n)=E_q(\pm\bar v n/(u,n))\).

After (3.27), a sufficient first open estimate, uniformly for either
orientation and every admissible \(\kappa,u,v,k\), is
\[
 \boxed{
 \left|
 \sum_{n\ll L/\kappa}\sum_t
 \Lambda^\pm_{\kappa,u,v,n,t}
 e\!\left(
 \Psi^\pm_{\kappa,u,v,n,t}+\frac t2
 \ \pm\frac{k\bar v n}{u}
 \right)
 \right|
 \ll_\varepsilon \kappa X^\varepsilon.}
\tag{3.29}
\]
Together with (3.28), (3.29) would contribute
\(\ll L^2X^\varepsilon\) after summing
\(\#\{(u,v)\}\ll(L/\kappa)^2\) and then \(\kappa\); logarithms are
absorbed into \(X^\varepsilon\).  No estimate of the strength (3.29)
is currently available for the literal masks.

Indeed, along a row \(x=N_0+2\kappa uv\,t\), with
\(r=2\kappa n\), the full phase including alternation is
\[
 \Phi(t)=\sigma J(\sqrt{x+r}-\sqrt x)+\frac t2,
\]
and on the literal support its scales are
\[
 T\asymp\kappa,\qquad
 F\asymp\frac{2Jn\kappa}{L},\qquad
 \Phi''\asymp\frac{2Jn}{\kappa L},\qquad
 \Phi'''\asymp\frac{2Jn}{\kappa^2L}.
\tag{3.30}
\]
Absolute stationary-dual recombination gives
\(\sqrt F+T/\sqrt F\) and supplies no aggregate row saving.  The
positive cross-gcd tail is \(L^3/K_0\); even a hypothetical complete
row bound \(O(1)\) only changes it to \(L^3/K_0^2\), which at
\(K_0=L^{1/2}\) is \(L^2\) only at the endpoint and leaves the
complement uncontrolled.  Bare \((-1)^t\) alternation cannot contract
an arbitrarily deleted literal fibre, and Abel summation has no input
because no bounded-variation theorem is known for the joint endpoint
selector.  Smooth two-variable Poisson followed by absolute values of
positive dual modes likewise restores the \(L^3\) incidence capacity.
Therefore these selector-blind routes do not prove (3.29).

# 4. First doubtful or unproved step

The first unproved step is precisely (3.29): a
selector-, endpoint-, profile-, sign-, and phase-aware signed joint
\((n,t)\)-fibre estimate, uniform in the orientation and in
\(k\bmod u\).  All preceding reductions are exact identities or
absolute incidence counts.  What is missing is not the formal
odd-sawtooth Fourier expansion, but cancellation after the full literal
M1 weights and their zero-extended endpoints are inserted.  No
bounded-variation, Fourier-norm, or equidistribution input for that
joint literal selector has been proved.  Accordingly, neither the
complete residual target (2.2) nor the scalar
\(L^{3/2}X^\varepsilon\) bound may be promoted from this report.

# 5. Required control tests and outcomes

1. **Residual truth table.**  The definition of \(\lambda\) retains
   \(\rho_N(d)\) exactly.  On a selected pair it has values
   \(1,0,0,1\) on the four incidence states.  Outcome: no density or
   independence assumption is used.
2. **Zero-extension and real-\(X\) endpoints.**  The sequence is
   extended by zero before Fejer averaging, and both endpoint
   \(\lambda\)'s remain in (3.24).  Outcome: (2.3) and (3.26) have no
   hidden boundary error and do not assume integral \(X\).
3. **One-real-part control.**  Formula (3.26) has one outer \(\Re\)
   covering both orientations and every incidence.  Outcome: no
   unjustified termwise positivity or sign separation occurs.
4. **Both-sign and conjugation control.**  The same formulas hold for
   each \(\sigma=\pm1\), and (3.24) keeps the exact conjugate endpoint.
   Outcome: no sign or complex coefficient is silently replaced.
5. **Parity terminal control.**  For odd \(R_0\), the terminal even gap
   carries its literal weight \(1/R_0\).  Outcome: the parity connector
   loses only an absolute factor.
6. **Small-shift seam control.**  The cross-gcd count was rederived for
   every even \(1\le r<R_0\); no hypothesis \(r\ge(\log X)^A\) was
   imported.  Outcome: all fixed-polylogarithmic and smaller shifts are
   present in (3.22), (3.24), and the exact complement.
7. **Gcd-identity control.**  The original gcd on a cross fibre is
   \((u,n)\), while \(\kappa\) is the inward cross gcd.  Outcome: the
   sequential \(g\)- and \(\kappa_*\)-cuts are distinct and correctly
   represented.
8. **Anchor Fourier control.**  Direct finite geometric summation gives
   (3.27); its normalized \(\ell^1\) norm is logarithmic, its normalized
   \(\ell^2\) norm is one, and its near-half maximum is large.  Outcome:
   Fourier expansion gives no power saving by itself.
9. **Capacity control.**  Applying rowwise derivative/B-process bounds
   or smooth Poisson followed by absolute dual recombination returns the
   incidence-capacity scale described after (3.30).  Outcome: the
   asserted no-go is limited to those selector-blind routes and is not
   claimed as a physical lower bound.
10. **Experiment budget.**  No numerical experiment was used.  Outcome:
    the report is entirely algebraic and analytic.

# 6. Dependencies and exact artifacts used

This report used only the following permitted artifacts, each read in
full:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round185_m1_hard_top_t1_residual_fejer_tangent_gcd_strategy.md`;
- `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`;
- `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reviews/residual_transport_correlation_owner_scope_review.md`;
- `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reviews/coefficient_profile_endpoint_power_post_repair_verification.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_k17a_cross_gcd_alternating_fibre_reduction.md`;
- `rounds/codex-managed/m9-m1-hard-top-t1-residual-fejer-tangent-gcd-gate/briefs/literal_residual_fejer_tangent_gcd_attack.md`.

The two M2 kernels were used only as method controls.  Every algebraic
identity and count invoked here was rechecked on the literal M1
coefficient, and the non-polylogarithmic-shift restriction from the M2
cross-gcd setting was not imported.

# 7. Recommended state effect

**Promote** the exact strict target-safe sector statement (1.1), its
fixed-proportion consequence (1.2), and the exact complement formula
(3.26) under the single campaign terminal label
`strict_hard_m1_t1_residual_tangent_gcd_sector`.  Retain the
selector-blind capacity/self-return no-go only as subordinate evidence
for that terminal, not as a second terminal label.
**Retain open** `hard_m1_t1_residual_target`: its first unresolved
literal relation is (3.29).  No effect is recommended for any
\(t\ge2\) owner, small-\(G\) or large-\(G\) near-resonant complement,
bridge, quarter-theorem, or exponent claim.
