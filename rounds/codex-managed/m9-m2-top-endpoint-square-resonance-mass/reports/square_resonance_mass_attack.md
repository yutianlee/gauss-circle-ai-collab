## 1. Result

The primitive square family closes at the desired scale, but its
raywise absolute Abel majorant does not.

More precisely, in the setting of (78.1)--(78.11),

\[
 \boxed{\quad
 |\mathcal S_L^\square(X)|
 \ll_{\varepsilon,\eta,\Phi,W,M}L^2X^\varepsilon .
 \quad}                                                   \tag{1.1}
\]

This estimate includes every exact and metric reciprocal resonance.  It
uses cancellation in the reciprocal mode \(k\), separately for each
actual odd lift; it uses neither cancellation between lifts nor
cancellation between distinct square rays.

In contrast, the positive quantity (78.11) has sharp power capacity

\[
 \mathcal M_L^\square(X)
 \ll \sqrt J\,L^{3/2}\log(2L),                         \tag{1.2}
\]

and the fixed nondegenerate dyadic support contains terminal one-lift
subcones on which

\[
 \mathcal M_L^\square(X)\gg \sqrt J\,L^{3/2}.        \tag{1.3}
\]

Thus, up to \(X^\varepsilon\), (1.2) is sharp.  Taking
\(L\asymp J^{1/2}\) gives
\(\mathcal M_L^\square/L^2\gg J^{1/4}=X^{1/8}\), so
(78.12) is false.  This failure is entirely compatible with (1.1): on
the one-lift subcone the Abel minimum is identically one and (78.11)
has discarded the decisive \(k\)-phase.

## 2. Exact statement and hypotheses

Assume the complete collar-extracted Round-77 identity and exact symbol
hypotheses recorded in the derivation packet: \(J=\sqrt X\),
\(1\le L\le H\le J^{1/2}\), the fixed smooth dyadic cutoff and top
profile, the accepted \(C^1\) Vaaler profile, the exact \(q_X\), floors,
stars and finite odd support, and one fixed smooth physical collar at
each \(m\)-endpoint.  Constants below may depend on these fixed data.

For every admissible square ray write

\[
 a=s^2,\qquad b=t^2,\qquad t=s+2u,
 \qquad (s,u)=1,\qquad 1\le u<s/2,                   \tag{2.1}
\]

where \(s,t\) are odd, and put

\[
 K={Ju\over s},\qquad K'={2Ju\over t},
 \qquad I_{s,u}=(K,K').                               \tag{2.2}
\]

For an actual odd lift \(g\in\mathcal G_{s^2,t^2}\), let
\(\mathfrak B_g(k)=\mathfrak B^\circ_{s^2,t^2,k}(g)\).
The new analytic kernel is the following sampled-variation lemma:

\[
 \boxed{
 \sup_{k\in I_{s,u}}|\mathfrak B_g(k)|
 +\operatorname {Var}_{k\in I_{s,u}\cap\mathbb Z}
       \mathfrak B_g(k)
 \ll X^\varepsilon\sqrt{\frac{g t^2}{K}} .}          \tag{2.3}
\]

Here the sampled variation includes the two jumps made by the sharp
open interval.  Since the dyadic lift support gives
\(gs^2\asymp gt^2\asymp L\), the right side is
\(\asymp X^\varepsilon\sqrt{L/K}\).  Statement (2.3) is about the
complete integral, not its leading stationary value.  In particular it
includes both incomplete-Fresnel collar crossings.  A pointwise bound
for \(k\partial_k\mathfrak B_g\) at a collar crossing is neither claimed
nor needed.

For the lower bound (1.3), “nondegenerate dyadic support” means the
standard condition already implicit in the fixed Round-77 cutoff: its
nonzero support contains a fixed compact interval.  Consequently, for
all sufficiently large dyadic \(L\), there is a fixed-ratio box of
\(\gg L\) coprime odd pairs \((s,u)\), with
\(s\asymp u\asymp\sqrt L\), for which \(g=1\) is an actual lift and
\(G_{s,t}\asymp N_{s^2,t^2}\asymp1\).  No lower bound for an actual
oscillatory coefficient is assumed in (1.3); it is a lower bound for
the explicitly positive majorant (78.11).

## 3. Proof or derivation

**Square geometry and the exact phase.**  If \((a,b)=1\), then
\(ab\) is a square if and only if \(a=s^2,b=t^2\) with
\((s,t)=1\).  Since \(s,t\) are odd, \(t=s+2u\), and

\[
 (s,t)=1\iff(s,u)=1,\qquad
 \delta=2u,\qquad {b-a\over4}=u(s+u)\in\mathbb Z.   \tag{3.1}
\]

Moreover \(t<2s\) is exactly \(u<s/2\), and the strict stationary
window is exactly (2.2).  The original offset is
\(r=g(b-a)/2=2gu(s+u)\), hence \((-1)^r=1\).  With
\(g=2n+1\), the two phases in (78.9) combine without approximation:

\[
 e(-Xu^2/k)e(-2nXu^2/k)=e(-gXu^2/k).                 \tag{3.2}
\]

This also proves that an original pair has a common squarefree kernel
if and only if it is an odd lift \((gs^2,gt^2)\) of one of these
primitive rays.  There is no second primitive family.

**Complete-integral sampled \(k\)-variation.**  In the exact Round-77
integral make the change \(v=y^2\).  With
\(r_k=Ju/k\) and \(\lambda=gk\), one obtains the literal identity

\[
 \mathfrak B_g(k)
 =\int_{t/2}^{s}q_g(y)
   e\!\left(\lambda(y-r_k)^2\right)dy,               \tag{3.3}
\]

where

\[
 q_g(y)=2gy\,A^\circ_{gs^2,gt^2}(gy^2)               \tag{3.4}
\]

contains both exact \(W\)-arguments, \(q_X\), the fixed profiles and
the two physical collars.  It is independent of \(k\).  Floors and
stars determine the finite support and the already-extracted endpoint
terms; they create no hidden \(k\)-dependence in (3.4).

Here is the needed complete-Fresnel estimate.  Put

\[
 T_\lambda p(r)=\int p(y)e(\lambda(y-r)^2)dy,
 \qquad F(\lambda,r)=T_\lambda q_g(r).               \tag{3.5}
\]

The exact normalized-symbol ledger gives a bulk height
\(Q_g\asymp gs\), total bulk variation \(O(Q_g)\), and two collar
widths

\[
 w_g\asymp(gs)^{-1}.                                 \tag{3.6}
\]

All other fixed-profile pieces vary on a scale \(\gg w_g\).  The
smallest scale is resolved by the quadratic kernel, because uniformly
on (2.2)

\[
 \lambda w_g^2\asymp {K\over gs^2}
 \asymp {K\over L}
 \ge c{J\over L^{3/2}}\ge cJ^{1/4}.                 \tag{3.7}
\]

For a smooth piece of height \(Q_g\) and scale
\(\ell\ge\lambda^{-1/2}\), split at
\(|y-r|=\lambda^{-1/2}\) and integrate by parts on the two tails.
Applied to the bulk and to each fixed rescaling of a collar, this gives

\[
 \int_{t/2}^{s}|T_\lambda(q_g')(r)|\,dr
 \ll {Q_g\over\sqrt\lambda}\log(2X),                \tag{3.8}
\]

and, uniformly in \(r\),

\[
 \left|T_\lambda\bigl(q_g+(y-r)q_g'\bigr)(r)\right|
 \ll {Q_g\over\sqrt\lambda}\log(2X).                \tag{3.9}
\]

For completeness, the high derivative in (3.8) comes only from a
fixed smooth collar.  On its \(r\)-interval of length \(w_g\), the
stationary bound is
\(O(Q_g/(w_g\sqrt\lambda))\); its integral is
\(O(Q_g/\sqrt\lambda)\).  Off that interval, one integration by parts
and dyadic summation gives only the displayed logarithm.  The slowly
varying \(C^1\) factor may be frozen at the collar endpoint; its error
has height \(O(Q_g)\), not \(O(Q_g/w_g)\).  Thus no second derivative
of the accepted \(C^1\) profile is being assumed.  This is exactly why
a collar crossing contributes one endpoint-sized variation packet and
not the number \(K/L\) of sampled points spent crossing it.

Differentiating (3.5) and integrating by parts, with no boundary term
because the physical collars vanish at the two endpoints, gives the
exact identities

\[
 F_r=T_\lambda(q_g'),\qquad
 \lambda F_\lambda
 =-{1\over2}T_\lambda\bigl(q_g+(y-r)q_g'\bigr).       \tag{3.10}
\]

As \(k\) runs through (2.2), \(r_k\) traverses \((t/2,s)\) once and
\(\lambda=gk\) stays in one fixed dyadic interval.  Integrating the two
terms in
\(dF(gk,r_k)/dk\), using (3.8) for the monotone \(r\)-motion and
(3.9) with \(d\lambda/\lambda\) for the \(\lambda\)-motion, proves

\[
 \sup|\mathfrak B_g|+\operatorname {Var}\mathfrak B_g
 \ll {Q_g\over\sqrt{gK}}\log(2X)
 \asymp \sqrt{\frac{gt^2}{K}}\log(2X).               \tag{3.11}
\]

The two sharp open-window jumps cost another two suprema.  This proves
(2.3), after absorbing logarithms into \(X^\varepsilon\).  Notice that
(3.3)--(3.11) retained the complete moving collar and every lower
stationary correction.

**Reciprocal-mode cancellation.**  For fixed \((s,u,g)\), set

\[
 f(x)=-{gXu^2\over x}.
\]

On \(I_{s,u}\), whose length is at most \(K\),

\[
 |f''(x)|\asymp \Lambda,\qquad
 \Lambda={gXu^2\over K^3}.                            \tag{3.12}
\]

The elementary second-derivative estimate, followed by partial
summation with (2.3), yields

\[
 \begin{aligned}
 \left|\sum_{k\in I_{s,u}\cap\mathbb Z}
       \mathfrak B_g(k)e(-gXu^2/k)\right|
 &\ll X^\varepsilon\sqrt{\frac{gt^2}{K}}
       \left(K\sqrt\Lambda+\Lambda^{-1/2}\right)\\
 &\ll X^\varepsilon\left(gst+{t\over s}\right)
 \ll X^\varepsilon(L+1).                             \tag{3.13}
 \end{aligned}
\]

The two simplifications in the second line are exact uses of
\(K=Ju/s\) and \(X=J^2\).  The same bound covers an empty, one-point or
very short open \(k\)-interval: the \(\Lambda^{-1/2}\) term is already
at least the one-point cost after multiplication by (2.3).

The number of actual lifted square triples satisfies

\[
 \begin{aligned}
 \sum_{s,u}N_{s^2,t^2}
 &\le \sum_{g\ll L}
   \#\{s<t<2s:gt^2\ll L\}\\
 &\ll \sum_{g\ll L}{L\over g}
 \ll L\log(2L).                                      \tag{3.14}
 \end{aligned}
\]

We may now interchange the finite \(g\)- and \(k\)-sums in (78.9),
apply (3.13), and take absolute values only after the \(k\)-sum.  The
factor \(2\Re\) counts the positive offset once.  Equations
(3.13)--(3.14), with the Round-77 extracted error, prove (1.1).

**Capacity of the absolute Abel majorant.**  Since
\(N_{s^2,t^2}\ll G_{s,t}\ll L/t^2\), and nonempty lift support forces
\(t\ll\sqrt L\), positivity and \(\min(N,\cdot)\le N\) give

\[
 \begin{aligned}
 \mathcal M_L^\square
 &\ll\sum_{s,u}JuG^{3/2}
      \sum_{K<k<K'}k^{-3/2}\\
 &\ll\sum_{s,u}JuG^{3/2}K^{-3/2}
       \left(1+K{s-2u\over t}\right).               \tag{3.15}
 \end{aligned}
\]

After \(G\ll L/t^2\), the contribution of the first term is

\[
 \ll {L^{3/2}\over\sqrt J}
 \sum_{s\ll\sqrt L}\sum_{u<s/2}{1\over s^{3/2}\sqrt u}
 \ll {L^{3/2}\over\sqrt J}\log(2L),                 \tag{3.16}
\]

while the second is

\[
 \ll \sqrt J L^{3/2}
 \sum_{s\ll\sqrt L}\sum_{u<s/2}
 {\sqrt u\,(s-2u)\over s^{7/2}}
 \ll \sqrt J L^{3/2}\log(2L).                       \tag{3.17}
\]

This proves (1.2).  Conversely, choose a compact terminal box inside
the nonzero dyadic support with
\(s\asymp u\asymp\sqrt L\), \(s-2u\asymp s\), and
\(g=1\).  Elementary Mobius inversion gives \(\gg L\) pairs in this
box satisfying \((s,u)=1\).  For each, \(G\asymp N\asymp1\),
\(K\asymp J\), \(K'-K\asymp J\), and

\[
 \min\!\left(1,{1\over2\|2Xu^2/k\|}\right)=1
\quad\hbox{for every }k.                              \tag{3.18}
\]

Therefore each ray contributes \(\gg\sqrt{JL}\), and the terminal box
contributes \(\gg\sqrt J L^{3/2}\).  This proves (1.3).  In
particular the worst absolute capacity is already present where there
is no lift sum on which Abel cancellation could act.

**Exact and metric resonance ownership.**  At fixed \((s,u)\), exact
lift resonance is precisely

\[
 {2Xu^2\over k}\in\mathbb Z;                         \tag{3.19}
\]

when \(X\) is integral these are the divisors
\(k\mid 2Xu^2\) that also lie in the strict interval (2.2).  For a
general real \(X\), the metric window used by Abel is

\[
 \left\|{2Xu^2\over k}\right\|\le {1\over2N}.        \tag{3.20}
\]

For \(N\ge2\), its nearest integer \(q\asymp2Jus\) is unique and
(3.20) is equivalently a reciprocal-root interval

\[
 \left|k-{2Xu^2\over q}\right|
 \ll {K^2\over N(2Xu^2)}\asymp {1\over Ns^2}.        \tag{3.21}
\]

In the bulk \(Ns^2\asymp L\), so every \(q\) owns at most one integer
\(k\); exact divisors are the centers of some of these intervals.  For
\(N=1\), every \(k\) is in the Abel window, as (3.18) shows.  The proof
of (1.1) does not discard either case: (3.12)--(3.13) sum all \(k\),
including exact centers and every metric neighbor.

## 4. First doubtful or unproved step

The first seam that deserves independent line checking is (3.8)--(3.9)
for the literal Round-77 coefficient, especially while the saddle
crosses a physical collar.  A false pointwise assertion
\(k|\partial_k\mathfrak B_g|\ll\sqrt{gt^2/K}\) would fail there: the
crossing occupies about \(K/L\) sampled modes.  The proof above instead
uses integrated variation in the monotone saddle coordinate and the
resolved-scale inequality (3.7); each collar is one fixed rescaled
packet.  It also freezes only the slow \(C^1\) factor, so it does not
silently assume a second derivative of \(\Phi\).

Within the selected packet, no later arithmetic step is conditional.
The only support convention used for the lower bound (1.3) is that the
fixed nonzero dyadic cutoff has an interior interval.  If an alternative
cutoff with no such interval were substituted, (1.2) and the signed
theorem (1.1) would remain valid, while that particular lower-bound box
would have to be replaced by a nonempty terminal box for the new
support.

## 5. Required control test and outcome

1. **External normalization:** pass.  Equation (3.2) is inserted into
   the positive-offset term of (78.1), and the sole external factor is
   the existing \(2\Re\); no second copy is introduced.
2. **Square/common-kernel equivalence:** pass.  Coprimality forces
   \(a=s^2,b=t^2\), and every original common-squarefree pair is exactly
   an odd \(g\)-lift of this primitive pair.
3. **Primitive parity and sign:** pass.  Equation (3.1) gives
   \((s,u)=1\), and \(r=2gu(s+u)\) makes the offset character identically
   \(+1\).
4. **Exact open \(k\)-interval:** pass.  It is
   \(Ju/s<k<2Ju/t\).  Equality modes stay in the accepted Round-77
   error; sharp open-window jumps are included in (2.3).
5. **Complete actual symbol:** pass.  The proof starts from (3.3), the
   complete centered integral.  Both \(W\)-weights, \(q_X\), profiles,
   floors, stars, finite support and incomplete-Fresnel collar crossings
   are retained.
6. **Exact versus metric resonance:** pass.  Equations
   (3.19)--(3.21) give their exact ownership, and (3.13) includes all of
   them without a resonance deletion.
7. **Absolute majorant versus signed sum:** pass.  Equations
   (1.1)--(1.3) prove that the signed target is true although its
   absolute Abel analogue is false.
8. **Fourth-power coherence:** pass.  If \(X=T^4\), odd \(13\mid T\),
   \((s,t,u)=(9,11,1)\), and \(k_0=2T^2/13\), then
   \(J/9<k_0<2J/11\), \(2X/k_0=13T^2\in\mathbb Z\), and
   \(e(-gX/k_0)=-1\) for every odd \(g\).  The saddle is
   \(169/4\), and the two actual \(W\)-arguments are \(9/13,11/13\),
   so both weights equal one.  No lift cancellation is used.  Even
   taking this one mode absolutely gives
   \(\ll L^{3/2}/\sqrt J\), which is target-safe.
9. **Small gaps, one-point lifts and terminal edges:** pass.  The proof
   permits \(u=1\), \(s-2u=1\), one integer \(k\), one actual \(g\),
   and a terminal \(\Phi\)-value.  It differentiates neither in \(g\)
   nor across a starred endpoint.  The bound
   \(K/L\ge cJ/L^{3/2}\ge cJ^{1/4}\) remains sufficient even in its
   weakest case \(u=1\).
10. **Cancellation over \(k\) and rays:** pass.  Cancellation over
    \(k\) is used in (3.13); cancellation across \(g\) or across rays is
    not used.  Hence the fourth-power coherent lift family is harmless.
11. **Coefficient adversary:** pass/no-go.  Replacing the actual
    \(\mathfrak B_g(k)\) by
    \(c(k)=\sqrt{gt^2/K}\,e(gXu^2/k)\) respects the pointwise size but
    makes the combined \(k\)-sum absolute.  It violates (2.3) and
    reproduces the capacity (1.3).  Thus the proof genuinely uses the
    actual complete-integral structure and proves no bounded-coefficient
    analogue.
12. **Rank-one self-return:** pass.  The cost \(O(L)\) in (3.13) is the
    primal-length cost restored by the reciprocal second-derivative
    step.  It is one legal self-return, not a second independent saving,
    and it is not iterated.
13. **Near-square nonsquare and downstream scope:** pass.  No nonsquare
    or merely near-square ray is included.  Nothing here estimates the
    generic resonance union, the full transposed energy, the signed top
    cone, \(M9\!-!M2\), \(M9\), endpoint uniformity, or the Gauss-circle
    exponent.

No numerical experiment was used; the effort was entirely analytic.

## 6. Dependencies and exact artifacts used

Campaign: `m9-m2-top-endpoint-square-resonance-mass`, Round 78.  Starting
graph SHA-256:
`5afbe1bb7b5c5d943be9438ba02bd9ede1ab6735344174b33b4a99c7de7f9123`.

Exact artifacts used:

- `protocol.md`;
- `state/proof_obligations.yml` (only the active M9--M2 interfaces and
  recorded Round-74--77 barriers were used in the derivation);
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/derivation_packet.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-square-resonance-mass/briefs/square_resonance_mass_attack.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reviews/conductor_round77_adjudication.md`;
- `rounds/codex-managed/m9-m2-top-endpoint-signed-offset-energy/reviews/conductor_round76_adjudication.md`.

No sibling Round-78 report, source card, external theorem, or unlisted
strategy file was read.  The only analytic input beyond the accepted
artifacts is the elementary one-dimensional second-derivative estimate,
whose hypotheses and substitution are displayed in (3.12)--(3.13).

## 7. Recommended state effect

**Promote**, subject to the mandated blind rederivation, hostile seam
review and conductor graph validation, the scoped theorem

\[
 \mathcal S_L^\square(X)\ll_\varepsilon L^2X^\varepsilon.
\]

**Promote as a route no-go** the sharp capacity statement

\[
 \mathcal M_L^\square(X)\asymp_{X^\varepsilon}
 \sqrt J\,L^{3/2},
\]

meaning the upper and lower bounds (1.2)--(1.3), and reject (78.12).
The state effect must explicitly record that failure of the absolute
Abel majorant does not obstruct the signed square-family theorem.

Make **no change** to the generic resonance union, full energy,
`M9-M2-top-endpoint-signed-cone`, `M9-M2`, `M9`, endpoint uniformity, or
the global exponent.
