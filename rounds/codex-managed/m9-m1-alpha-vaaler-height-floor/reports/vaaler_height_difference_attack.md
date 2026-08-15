# Round 52 discovery report: the Vaaler height is discrete, with sharp adjacent variation

- Campaign: `m9-m1-alpha-vaaler-height-floor`
- Task: `vaaler_height_difference_attack`
- Role: discovery
- Access mode: selected context
- Input graph SHA-256: `76a480a78ae30353d4f9cbe26c0e17337c1b89318c4a15758a6ffe0c34051fea`
- Status: candidate evidence only

## 1. Result: typed adjacent-height lemma and contour-seam no-go

The Vaaler height

\[
 H_j=\lfloor D_jX^{-1/4}\rfloor
\]

is a fixed integer parameter when the Mellin contour variables vary.  In
particular,

\[
 \partial_\mu H_j=\partial_\nu H_j
 =\partial_\alpha H_j=\partial_\beta H_j=0.
\]

Thus it has no moving-face velocity and creates no floor delta in the finite
alpha Cauchy--Green ledger.  Differentiating \((H_j+1)^v\) with respect to
the height of (v) differentiates an ordinary exponential and produces a
factor (i\log(H_j+1)); it does not differentiate the floor.

There is nevertheless a lawful *discrete* comparison.  Put

\[
 a_H(h)={\bf1}_{1\le h\le H}\Phi\!\left({h\over H+1}\right),
 \qquad
 \Phi(u)=\pi u(1-u)\cot(\pi u)+u,
\]

and let \(\Delta_Ha=a_{H+1}-a_H\).  Then every coordinate of
\(\Delta_Ha\) is positive, its unweighted mass is exactly

\[
 \boxed{\ \|\Delta_Ha\|_{\ell^1_h}={1\over2}\ },
\]

and its (1/h)-weighted mass is sharply of order (H^{-1}).  More
generally, all real power-weighted masses are determined below.  The new
endpoint (h=H+1) is only of order (H^{-2}) before the Vaaler (1/h)
factor and of order (H^{-3}) after it.  The order-one unweighted adjacent
variation comes from the coherent retuning of the existing frequencies,
not from the new endpoint.

This local smoothness does not currently reduce the alpha lattice capacity.
The exact dyadic scale change is

\[
 H_{j+1}=\lfloor H_j/2\rfloor,
\]

not (H_j\mapsto H_j\pm1).  Holding every other factor fixed, that dyadic
height change has unweighted size \(\asymp H_j\), and (1/h)-weighted size
\(\asymp1\).  In the actual coefficient it also changes (D_j), the
dyadic profile, its support and star values, and the Mellin scale factor.
Moreover, before physical \(v\)-inversion, even an abstract unit change
must difference the whole product \((H+1)^v a_H\).  On the high \(v\)-line
the resulting bulk term can have size \(\asymp H\), so the physical
\(\|\Delta_Ha\|_1=1/2\) estimate is not a uniform finite-height Mellin
estimate.
No accepted bounded-partial-sum identity transfers a difference onto just
the Vaaler family.  Consequently the floor is not the missing alpha seam,
and adjacent-height summation by parts is at present only a conditional
reorganization, not an alpha-trace estimate.

## 2. Exact statement and hypotheses

Assume (H\ge1), put (N=H+1\ge2), and extend every finite coefficient
family by zero to all positive integers.  Write

\[
 \delta_N(h):=\Delta_Ha(h).
\]

Then the exact identity is

\[
 \boxed{
 \delta_N(h)=
 \begin{cases}
 \displaystyle
 \Phi\!\left({h\over N+1}\right)
 -\Phi\!\left({h\over N}\right),&1\le h\le N-1,\\[6pt]
 \displaystyle \Phi\!\left({N\over N+1}\right),&h=N,\\[4pt]
 0,&h>N.
 \end{cases}}
 \tag{2.1}
\]

There are absolute constants (0<c<C<\infty) such that, uniformly for
(N\ge2) and (1\le h\le N),

\[
 \boxed{
 c\,{h^2(N+1-h)\over N^4}
 \le \delta_N(h)\le
 C\,{h^2(N+1-h)\over N^4}.}
 \tag{2.2}
\]

In particular, all the differences are strictly positive.  At the new
endpoint, with (t=(N+1)^{-1}=(H+2)^{-1}), one has the exact formulas

\[
 \begin{aligned}
 \delta_N(N)
 &=\Phi(1-t)=1-\Phi(t)\\
 &=(1-t)\{1-\pi t\cot(\pi t)\}\\
 &=2t^2(1-t)\sum_{m\ge1}{1\over m^2-t^2},
 \end{aligned}
 \tag{2.3}
\]

and hence

\[
 \delta_N(N)\sim {\pi^2\over3(N+1)^2}.
 \tag{2.4}
\]

For real (p), define

\[
 T_p(H):=\sum_{h\ge1}h^p|\Delta_Ha(h)|
       =\sum_{h=1}^{N}h^p\delta_N(h).
\]

The sharp uniform orders are

\[
 \boxed{
 T_p(H)\asymp_p
 \begin{cases}
 N^p,&p>-3,\\
 N^{-3}\log(2N),&p=-3,\\
 N^{-3},&p<-3.
 \end{cases}}
 \tag{2.5}
\]

Two especially relevant cases are

\[
 \boxed{T_0(H)={1\over2}},
 \qquad
 \boxed{T_{-1}(H)\asymp N^{-1}}.
 \tag{2.6}
\]

The second estimate has leading constant one:

\[
 \lim_{H\to\infty}(H+1)T_{-1}(H)=1.
 \tag{2.7}
\]

Thus the actual positive-frequency coefficients satisfy

\[
 \sum_{h\ge1}|\alpha_{h,H+1}-\alpha_{h,H}|
 ={1\over2\pi}T_{-1}(H)
 \sim {1\over2\pi(H+1)}.
 \tag{2.8}
\]

For completeness, the sharp asymptotic form of (2.5) is

\[
 N^{-p}T_p(H)\longrightarrow
 C_p:=\int_0^1x^{p+1}\{-\Phi'(x)\}\,dx
 \quad(p>-3),
 \tag{2.9}
\]

where (0<C_p<\infty), (C_{-1}=1), and (C_0=1/2).  At and below the
critical exponent,

\[
 {N^3T_{-3}(H)\over\log N}\longrightarrow {2\pi^2\over3},
 \qquad
 N^3T_p(H)\longrightarrow {2\pi^2\over3}\zeta(-p-2)\quad(p<-3).
 \tag{2.10}
\]

All assertions concern the abstract coefficient comparison with the other
data frozen.  They do not identify it with an actual change of dyadic
block.

## 3. Proof and derivation

### 3.1 Variable type

In the accepted Mellin antecedent the relevant factor is

\[
 \left({D_j\over2\sqrt X}\right)^u(H_j+1)^v,
 \qquad H_j=\lfloor D_jX^{-1/4}\rfloor.
\]

For a fixed physical (X) and a fixed scale label (j), (D_j) and
(H_j) are parameters.  The contour heights change the imaginary parts
of (u) and (v), not (X) or (D_j).  Therefore every contour velocity
of (H_j) is zero.  For example, if (v=\sigma+i\nu), then

\[
 {d\over d\nu}(H_j+1)^v
 =i\log(H_j+1)(H_j+1)^v.
\]

There is no distribution supported at a floor threshold.  A floor threshold
can occur only along an external variation of (X), an auxiliary continuous
scale (D), or a discrete change of (j) or (H).  Such a threshold is
not a face in the alpha contour plane.

### 3.2 Exact properties of the Vaaler taper

Direct substitution gives

\[
 \Phi(u)+\Phi(1-u)=1,
 \tag{3.1}
\]

because \(\cot(\pi(1-u))=-\cot(\pi u)\).  In particular
\(\Phi(0^+)=1\), \(\Phi(1^-)=0\), and \(\Phi(1/2)=1/2\).

The partial-fraction expansion

\[
 \pi\cot(\pi u)={1\over u}
 -2u\sum_{m\ge1}{1\over m^2-u^2}
\]

gives, for (0<u<1),

\[
 1-\Phi(u)=2u^2(1-u)S(u),
 \qquad S(u):=\sum_{m\ge1}{1\over m^2-u^2}.
 \tag{3.2}
\]

Let (f(u)=-\Phi'(u)).  On (0<u\le1/2), differentiating (3.2) gives

\[
 f(u)=2u(2-3u)S(u)
 +4u^3(1-u)\sum_{m\ge1}{1\over(m^2-u^2)^2}>0.
 \tag{3.3}
\]

Here (S(u)) and the squared-denominator sum are bounded above, while
(S(u)\ge\zeta(2)).  Hence (f(u)\asymp u) on this half-interval.
Differentiating (3.1) yields (f(u)=f(1-u)), and consequently

\[
 \boxed{f(u)\asymp u(1-u)\qquad(0<u<1).}
 \tag{3.4}
\]

This proves strict decrease and supplies all uniform endpoint constants;
no external monotonicity assertion is needed.

### 3.3 Pointwise adjacent difference and weighted norms

For (1\le h\le N-1), (2.1) and strict decrease give

\[
 \delta_N(h)=
 \int_{h/(N+1)}^{h/N}f(t)\,dt.
 \tag{3.5}
\]

The interval has length (h/(N(N+1))\asymp h/N^2).  On it,

\[
 t\asymp {h\over N},
 \qquad
 1-t\asymp {N+1-h\over N}.
\]

Combining these comparisons with (3.4) proves (2.2) for (h<N).
For (h=N), (2.3) follows from (3.1) and (3.2), and proves the same
comparison.  It also gives (2.4).  Notice that the coefficient cutoff has
full ownership of the new integer (h=N); no half weight occurs there.

Pairing (h) with (H+1-h) in (3.1) gives the exact finite sum

\[
 \sum_{h=1}^{H}a_H(h)={H\over2}.
 \tag{3.6}
\]

Since \(\Delta_Ha\ge0\), subtraction of (3.6) at consecutive heights
proves (T_0(H)=1/2).

For arbitrary (p), (2.2) reduces the norm to the elementary sum

\[
 T_p(H)\asymp_p
 N^{-4}\sum_{h=1}^{N}h^{p+2}(N+1-h).
 \tag{3.7}
\]

If (p>-3), the sum on the right is of order (N^{p+4}).  If (p=-3),
it equals, up to absolute constants,
(N\sum_{h\le N}h^{-1}\), and if (p<-3), its first bounded range has
order (N) while the remaining power sum converges.  This proves (2.5).

For (2.9), (3.5) is a Riemann-sum cell:

\[
 N\delta_N(h)=x_hf(x_h)+o(1),
 \qquad x_h={h\over N},
\]

away from the endpoints.  The majorant (2.2) controls both endpoints and
is integrable exactly when (p>-3).  Dominated Riemann summation gives
(2.9).  The identities (C_{-1}=\int_0^1f=1) and

\[
 C_0=\int_0^1xf(x)\,dx=\int_0^1\Phi(x)\,dx={1\over2}
\]

use the endpoint values and (3.1).  Finally, (3.2) gives

\[
 f(u)={2\pi^2\over3}u+O(u^2),
 \qquad
 N^3\delta_N(h)\longrightarrow {2\pi^2\over3}h^2
\]

for each fixed (h).  Harmonic summation at (p=-3) and dominated
summation for (p<-3) prove (2.10).

### 3.4 What discrete summation by parts can and cannot do

Set (A_H=(a_H(h))_{h\ge1}), and formally set (A_0=0).  For any finite
scalar sequence (c_H), ordinary Abel summation in the common sequence
space is lawful:

\[
 \sum_{H=L}^{K}c_HA_H
 =C_KA_K-\sum_{H=L}^{K-1}C_H(A_{H+1}-A_H),
 \qquad C_H=\sum_{r=L}^{H}c_r.
 \tag{3.8}
\]

But (3.8) saves only when the *actual* (C_H) has a useful signed bound
and the terminal term is controlled.  The Vaaler increments themselves
have one sign.  Indeed,

\[
 A_H=\sum_{r=0}^{H-1}(A_{r+1}-A_r),
\]

and exact positivity gives

\[
 \sum_{r=0}^{H-1}\|A_{r+1}-A_r\|_1={H\over2}=\|A_H\|_1,
 \tag{3.9}
\]

while, after the Vaaler (1/h) factor,

\[
 \sum_{r=0}^{H-1}\sum_h{a_{r+1}(h)-a_r(h)\over h}
 =\sum_{h\le H}{a_H(h)\over h}\asymp\log(2H).
 \tag{3.10}
\]

Thus decomposing a fixed-height block into all unit increments recovers its
full capacity.

There is also a distinct finite-Mellin-height obstruction.  The family in
the antecedent is not \(A_H\) but

\[
 \mathcal A_H(v)=(H+1)^vA_H.
\]

Its exact adjacent difference is

\[
 \boxed{
 \mathcal A_{H+1}(v)-\mathcal A_H(v)
 =(H+2)^v(A_{H+1}-A_H)
 +\{(H+2)^v-(H+1)^v\}A_H.}
 \tag{3.10a}
\]

The second summand is a bulk change of every old frequency.  On a fixed
vertical line, its relative scalar has the capacity bound

\[
 \left|\left(1+{1\over H+1}\right)^v-1\right|
 \ll_{\Re v}\min\!\left(1,{|v|\over H+1}\right),
 \tag{3.10b}
\]

but this is not small uniformly in the contour height.  The failure is
exact already on \(\Re v=0\): choose

\[
 v=i\nu_H,
 \qquad
 \nu_H={\pi\over\log((H+2)/(H+1))}\asymp H.
\]

Then \((H+2)^v=-(H+1)^v\), so positivity and (3.6) give

\[
 \|\mathcal A_{H+1}(v)-\mathcal A_H(v)\|_1
 =\|A_{H+1}+A_H\|_1=H+{1\over2},
 \tag{3.10c}
\]

and the \(1/h\)-weighted norm is
\(\sum_h(a_{H+1}(h)+a_H(h))/h\asymp\log(2H)\).  Thus the sharp small
physical increment emerges only after the \(v\)-profile has been inverted;
it cannot be inserted as a uniform estimate inside the zeta-high Mellin
rectangle.  Any attempt to invert first must separately justify the
outside-height limit and all coupled boundary terms.

There is an even sharper mismatch with the actual scale sequence.  Since
(D_{j+1}=D_j/2), if (t=D_jX^{-1/4}), then

\[
 H_{j+1}=\lfloor t/2\rfloor
 =\lfloor\lfloor t\rfloor/2\rfloor
 =\lfloor H_j/2\rfloor.
 \tag{3.11}
\]

With (K=\lfloor H/2\rfloor\), monotonicity and (3.6) yield

\[
 \|A_H-A_K\|_1={H-K\over2}\asymp H,
 \tag{3.12}
\]

and (2.6) yields, for (H\ge2),

\[
 \sum_h{a_H(h)-a_K(h)\over h}
 =\sum_{r=K}^{H-1}T_{-1}(r)\asymp1.
 \tag{3.13}
\]

So the (H^{-1}) gain belongs to one artificial unit increment, not to
one actual dyadic step.

Finally, put

\[
 B_j(n,h)=\left[w_j\!\left(2h\sqrt{X/n}\right)\right]^*.
\]

Even a comparison of two actual physical terms contains the exact product
difference

\[
 a_{H_{j+1}}B_{j+1}-a_{H_j}B_j
 =(a_{H_{j+1}}-a_{H_j})B_j
 +a_{H_{j+1}}(B_{j+1}-B_j).
 \tag{3.14}
\]

The second term carries the changed dyadic profile, support, and star.  In
the Mellin antecedent one must additionally difference

\[
 \left({D_j\over2\sqrt X}\right)^u(H_j+1)^v,
\]

and an (X)-variation also changes the radial phase, product cutoff,
external normalization, and the top floor (\lfloor\sqrt X\rfloor).
Discarding any of these changes is not an actual summation by parts.

At a positive Dirac-comb lattice point the frequency phases are coherent,
and every coordinate of \(\Delta_Ha\) has the same sign (the corresponding
\(\Delta\alpha\) has the same pure-imaginary phase).  Hence neither the
zero-mass high-pass packet nor the Vaaler increment itself supplies hidden
frequency cancellation.  A future scale-Abel argument would need a new,
complete signed partial-sum estimate for the coupled objects in (3.14),
including its boundary term.  No such estimate is among the dependencies.

## 4. First doubtful or unproved step

The discrete-height lemma itself has no unproved analytic step.  The first
unproved downstream step is precisely the one needed to turn it into an
alpha estimate: construct a common ambient family for the *complete*
scale amplitudes, retain the (D_j), profile, support, star, Mellin-power,
and normalization changes, and prove cancellation or bounded partial sums
for that signed family.  The exact dyadic relation (3.11) shows that a
unit-height model cannot stand in for this task.

In particular, it is presently unjustified to claim either of the following:

1. that the (O(H^{-1})) coefficient variation in (2.8) is the size of an
   actual dyadic-block difference; or
2. that an Abel transform has eliminated the boundary (A_K) in (3.8) or
   controlled the profile-difference term in (3.14).

These are substantive missing estimates, not bookkeeping details.
The finite-height counterexample (3.10c) also shows that using the physical
adjacent norm inside the Mellin rectangle would require an unproved
interchange: first invert the \(v\)-profile, then pass the outside-height
limit, while retaining every connector and boundary owner.

## 5. Required control tests and outcomes

1. **`variable_type` -- pass/no-go.**  (H_j) is fixed under all alpha and
   beta contour-height variations.  Its contour velocity is zero, so it is
   not a moving alpha seam.
2. **`exact_Phi_formula` -- pass.**  The proof uses
   \(\Phi(u)=\pi u(1-u)\cot(\pi u)+u\), the partial-fraction identity, and
   \(\Phi(u)+\Phi(1-u)=1\).  It never substitutes the false symmetry
   \(\Phi(1-u)=\Phi(u)\).
3. **`right_endpoint_taper` -- pass.**  The new endpoint has the exact
   expression (2.3), is \(\asymp H^{-2}\), and becomes \(\asymp H^{-3}\)
   after the (1/h) coefficient.  It is not the main adjacent mass.
4. **`adjacent_height_identity` -- pass.**  Equation (2.1) includes every
   old frequency and the full new frequency (h=H+1).
5. **`weighted_norms` -- pass.**  Equations (2.2), (2.5), and (2.9)--(2.10)
   give sharp pointwise, unweighted, (1/h)-weighted, and all real
   power-weighted orders, uniformly down to (H=1).
6. **`actual_scale_coupling` -- obstruction exposed.**  The exact adjacent
   dyadic relation is (H_{j+1}=\lfloor H_j/2\rfloor), with sizes
   (3.12)--(3.13).  Equation (3.14) retains the simultaneous profile
   difference; the Mellin scale and every (X)-dependent object must also
   be retained.  Equations (3.10a)--(3.10c) show independently that the
   factor \((H+1)^v\) turns a unit change into an \(H\)-sized difference at
   admissible high contour heights.
7. **`star_ownership` -- pass.**  The cutoff (h\le H) owns its equality
   with full weight.  The star in \(\Omega_X^*\) belongs to the sampled
   dyadic/stationary endpoint and is kept inside (B_j); it neither halves
   the Vaaler cutoff jump nor changes (2.1).
8. **`alpha_capacity_scope` -- no automatic saving.**  One unit height
   change costs exactly (1/2) unweighted and \(\asymp H^{-1}\) after
   (1/h) only in the physical coefficient family.  All increments recover
   the original (H) or logarithmic capacity; a finite-height unit jump can
   already cost \(\asymp H\) or \(\asymp\log H\); and an actual dyadic jump
   costs (\asymp H) or \(\asymp1\) even before the other factors.
   Positivity and lattice coherence preclude internal cancellation.
9. **`downstream_scope` -- pass.**  No projected alpha trace, outside-height
   limit, GAR bound, M9-M1 bound, M9 bound, or Gauss-circle estimate is
   asserted.

No numerical experiment and no external theorem were used.  The allocation
was 100 percent analytical/algebraic.

## 6. Dependencies and exact artifacts used

The derivation used only the selected context in the task brief:

- `protocol.md`;
- `state/proof_obligations.yml`, at the accepted global angular,
  alpha-comb, high-pass, and seam-specification interfaces;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-alpha-vaaler-height-floor/derivation_packet.md`;
- `rounds/codex-managed/m9-unit-frequency-w1-validation/synthesis.md`;
- `rounds/codex-managed/m9-m1-dual-r2-recombination/synthesis.md`;
- `rounds/codex-managed/m9-m1-upper-endpoint-character-abel/synthesis.md`;
- `rounds/codex-managed/m9-m1-alpha-signed-jump-incidence/synthesis.md`.

No other Round-52 report was read.  No computation or web source was used.

## 7. Recommended state effect

**Promote** a scoped internal lemma recording:

1. zero alpha/beta contour velocity of (H_j) and the resulting no-floor-
   connector conclusion;
2. the exact adjacent identity (2.1), endpoint formula (2.3), exact
   unweighted mass (1/2), and sharp weighted norms (2.5)--(2.10); and
3. the finite-height bulk identity and counterexample (3.10a)--(3.10c),
   and the exact dyadic relation (H_{j+1}=\lfloor H_j/2\rfloor) together
   with the coefficient-only capacities (3.12)--(3.13).

**Reject** the proposed identification of the (H_j) floor with a moving
alpha Cauchy--Green seam, and reject any use of the (O(H^{-1})) unit
increment as the size of an actual dyadic-scale change.

**Revise** the open alpha obligation so that a future discrete route must
difference the complete coupled scale amplitude and prove an actual signed
partial-sum estimate.  Retain the connector-completed alpha-bounded
zeta-high transition, its outside-height limit, the global arithmetic sum,
GAR, M9-M1, M9, and the final target as open.
