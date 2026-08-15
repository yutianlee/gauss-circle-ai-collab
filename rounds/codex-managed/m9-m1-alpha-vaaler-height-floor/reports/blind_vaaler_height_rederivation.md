# Round 52 blind Vaaler-height rederivation

## 1. Result

**Typed discrete-height lemma and contour-seam no-go.**  With (X) and
(D_j) fixed, (H_j=\lfloor D_jX^{-1/4}\rfloor) is a fixed discrete
parameter, not a contour variable.  Its velocity with respect to each of
(\mu,\nu,\alpha,\beta) is zero, including distributionally, so it creates
no moving-face delta in an alpha Cauchy--Green ledger.

For an adjacent formal height change (H\mapsto H+1), the coefficient
difference is nonnegative at every positive frequency.  Its unweighted
variation is exactly

\[
 \sum_{h\geq 1}|a_{H+1}(h)-a_H(h)|=\frac12.
\]

Thus one height step is an (O(1)), not logarithmic or (H)-sized,
perturbation in the unweighted coefficient norm.  In the natural
(1/h)-weighted norm it is sharply

\[
 \sum_{h\geq1}\frac{|a_{H+1}(h)-a_H(h)|}{h}
 =\frac1{H+1}+O((H+1)^{-2}).
\]

Consequently the positive-frequency Vaaler coefficients
(\alpha_{h,H}=ia_H(h)/(2\pi h)) have adjacent unweighted variation
(1/(2\pi(H+1))+O(H^{-2})).  This is a valid local discrete-height bound,
but it cannot reduce an alpha-contour lattice-jump capacity: the floor has
no alpha-contour velocity, and an actual scale transition changes data not
controlled by this coefficient-only lemma.

## 2. Exact statement and hypotheses

Assume (H\geq1), (h\) is a positive integer, and

\[
 a_H(h)={\bf1}_{h\leq H}\Phi\!\left(\frac{h}{H+1}\right),
 \qquad
 \Phi(u)=\pi u(1-u)\cot(\pi u)+u.
\]

Extend (\Phi) continuously to ([0,1]) by (\Phi(0)=1) and
(\Phi(1)=0).  Put (N=H+1) and
(q(u)=-\Phi'(u)).  Then (q(u)>0) for (0<u<1), and the exact adjacent
difference is

\[
 \delta_H(h):=a_{H+1}(h)-a_H(h)
 =
 \begin{cases}
 \Phi\!\left(\dfrac h{H+2}\right)
  -\Phi\!\left(\dfrac h{H+1}\right),&1\leq h\leq H,\\[6pt]
 \Phi\!\left(\dfrac{H+1}{H+2}\right)
  =1-\Phi\!\left(\dfrac1{H+2}\right),&h=H+1,\\[6pt]
 0,&h\geq H+2.
 \end{cases}
\]

Equivalently, including the new endpoint (h=N),

\[
 \boxed{\quad
 \delta_H(h)=\int_N^{N+1}\frac{h}{t^2}
 q\!\left(\frac ht\right)\,dt
 \quad(1\leq h\leq N).\quad}
\]

In particular (\delta_H(h)\geq0).  The endpoint is quadratically tapered:

\[
 \delta_H(H+1)
 =\frac{\pi^2}{3(H+2)^2}
  -\frac{\pi^2}{3(H+2)^3}
  +O((H+2)^{-4}).
\]

For every fixed real (p\geq-1), define the power-weighted variation

\[
 V_p(H)=\sum_{h\geq1}h^p|\delta_H(h)|,
 \qquad
 C_p=\int_0^1u^{p+1}q(u)\,du>0.
\]

Then, uniformly in the integer (H\geq1) with constants allowed to depend
on (p),

\[
 V_p(H)=C_p(H+1)^p+O_p((H+1)^{p-1}).
\]

The leading constants are intrinsic and hence sharp.  More explicitly,

\[
 C_{-1}=1,
 \qquad
 C_p=(p+1)\int_0^1u^p\Phi(u)\,du\quad(p>-1),
 \qquad C_0=\frac12,
\]

and the (p=0) identity improves to (V_0(H)=1/2) exactly.  The
(p=-1) case gives (V_{-1}(H)=(H+1)^{-1}+O((H+1)^{-2})).  For the
positive-frequency (\alpha)-coefficients, for every (r\geq0),

\[
 \sum_{h\geq1}h^r|\alpha_{h,H+1}-\alpha_{h,H}|
 =\frac1{2\pi}V_{r-1}(H).
\]

These statements isolate only (H\mapsto H+1); all (X,D_j,w_j), support,
star convention, and external normalization are hypotheses held fixed.

## 3. Proof or derivation

First, (x\cot x\to1) as (x\to0), so the stated endpoint values follow.
Also

\[
 \cot(\pi(1-u))=-\cot(\pi u)
 \quad\Longrightarrow\quad
 \Phi(u)+\Phi(1-u)=1.
\]

This is complementarity, not the false symmetry
(\Phi(1-u)=\Phi(u)).

Differentiate on (0<u<1):

\[
 q(u)=\pi^2u(1-u)\csc^2(\pi u)
      -\pi(1-2u)\cot(\pi u)-1.
\]

For (x=\pi u), multiplication by (\sin^2x) gives

\[
 q(u)\sin^2x
 =F(x):=x(\pi-x)-(\pi-2x)\sin x\cos x-\sin^2x.
\]

Here (F(0)=F(\pi)=0) and

\[
 F'(x)=2(\pi-2x)\sin^2x.
\]

Thus (F) increases from (0) to (x=\pi/2) and then decreases to (0),
remaining strictly positive in the open interval.  Hence (q>0) and
(\Phi) is strictly decreasing.  The Taylor expansion

\[
 \Phi(t)=1-\frac{\pi^2}{3}t^2
              +\frac{\pi^2}{3}t^3+O(t^4)
\]

together with complementarity proves the right-endpoint formula.  It also
shows that (q) extends smoothly to the endpoints, with
(q(u)=O(u)) at zero and (q(u)=O(1-u)) at one.

For (1\leq h\leq N), regard the denominator as a continuous auxiliary
variable (t).  Since

\[
 \frac d{dt}\Phi\!\left(\frac ht\right)
 =\frac h{t^2}q\!\left(\frac ht\right),
\]

integration from (N) to (N+1) proves the boxed adjacent-height identity.
At (h=N), its lower value is (\Phi(1)=0), exactly the old cutoff, so no
endpoint term has been omitted.  Positivity follows from (q\geq0).

For every integer (m\geq2), complementarity pairs (h) with (m-h) and
gives

\[
 \sum_{h=1}^{m-1}\Phi\!\left(\frac hm\right)=\frac{m-1}{2}.
\]

Therefore, because all adjacent differences are nonnegative,

\[
 V_0(H)=\sum_{h=1}^{N}\delta_H(h)
 =\frac N2-\frac{N-1}{2}=\frac12.
\]

It remains to justify the sharp weighted laws.  Let
(F_p(u)=u^{p+1}q(u)).  For (p\geq-1), the endpoint behavior of (q)
makes (F_p) continuously differentiable on ([0,1]).  Multiplying the
boxed identity by (h^p), summing, and interchanging a finite sum with the
integral gives the exact identity

\[
 V_p(H)=\int_N^{N+1}t^{p-1}
       \sum_{h=1}^{N}F_p\!\left(\frac ht\right)dt.
\]

For completeness, this Riemann sum has a uniform quantitative remainder.
If (L_p=\|F_p'\|_\infty) and (Q=\|q'\|_\infty), the right-endpoint
Riemann-sum estimate and (q(u)\leq Q(1-u)) yield, for (N\leq t\leq N+1),

\[
 \left|\sum_{h=1}^{N}F_p\!\left(\frac ht\right)-tC_p\right|
 \leq \frac{L_p}{2}+\frac{Q}{2t}.
\]

Consequently

\[
 \left|V_p(H)-C_p\int_N^{N+1}t^pdt\right|
 \leq \frac{L_p}{2}\int_N^{N+1}t^{p-1}dt
     +\frac Q2\int_N^{N+1}t^{p-2}dt.
\]

This proves the asserted uniform asymptotic, including
(V_{-1}(H)=N^{-1}+O(N^{-2})).  Finally,
(C_{-1}=\int_0^1q=\Phi(0)-\Phi(1)=1).  For (p>-1), integration by parts
gives (C_p=(p+1)\int_0^1u^p\Phi(u)du), and complementarity gives
(C_0=\int_0^1\Phi=1/2).  Since (q>0) internally, every (C_p) is
positive, so the powers and leading constants cannot be improved.

For the variable-type claim, the packet fixes ((X,D_j,H_j)) while the
contour heights vary.  Hence

\[
 \partial_\mu H_j=\partial_\nu H_j
 =\partial_\alpha H_j=\partial_\beta H_j=0.
\]

The only floor transitions occur when the genuine scale quantity
(D_jX^{-1/4}) crosses an integer.  If (D_j) is held fixed and (X)
increases, the crossings are (X=(D_j/k)^4) and the floor jumps downward;
the reverse direction gives the adjacent upward change studied above.  A
formal discrete (H\mapsto H+1) is also lawful as a coefficient comparison,
but is not itself a contour motion.

Along an actual pair of scale states, write

\[
 W_j^\pm(n,h)=
 \left[w_j^\pm\!\left(2h\sqrt{X^\pm/n}\right)\right]^{*_{\pm}}.
\]

Then the exact product difference contains both parts

\[
 a_{H_j^+}(h)W_j^+(n,h)-a_{H_j^-}(h)W_j^-(n,h)
 =[a_{H_j^+}(h)-a_{H_j^-}(h)]W_j^-(n,h)
  +a_{H_j^+}(h)[W_j^+(n,h)-W_j^-(n,h)].
\]

Only the first part is controlled here.  An actual scale or dyadic-profile
change must also retain changes of (X,D_j,w_j), support and equality
status, the star convention, external normalization, and the Mellin factor
((D_j/(2\sqrt X))^u(H_j+1)^v).  In particular, the star belongs to the
weight evaluation, not to the coefficient cutoff; the new coefficient at
(h=H+1) is the full endpoint value displayed above.

## 4. First doubtful or unproved step

No step in the coefficient-only lemma remains unproved.  The first
unsupported downstream step would be to identify a formal
(H\mapsto H+1) comparison with the full change of
(\Omega_X^*(n,h)) along an actual scale or dyadic transition.  The packet
does not give the dependence or variation bounds for (D_j,w_j), their
support/equality boundaries, the star status, or the external
normalization.  It therefore does not justify discarding the second product
term above, nor does it identify the floor as an alpha moving face.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| `variable_type` | Passed: (H_j) is a fixed integer parameter for all contour-height motions; all four contour velocities vanish. |
| `exact_Phi_formula` | Passed: the exact cotangent formula, endpoint limits, and complement identity were used.  No false symmetry was used. |
| `right_endpoint_taper` | Passed: (h=H+1) is included with full value (1-\Phi(1/(H+2))=\pi^2/(3(H+2)^2)+O(H^{-3})). |
| `adjacent_height_identity` | Passed: the piecewise difference and its exact positive integral representation were derived. |
| `weighted_norms` | Passed: (V_0=1/2) exactly, (V_{-1}=(H+1)^{-1}+O(H^{-2})), and the sharp (V_p=C_p(H+1)^p+O_p((H+1)^{p-1})) law holds for every fixed (p\geq-1). |
| `actual_scale_coupling` | Obstruction retained: an actual (X) or dyadic-scale transition changes every coupled factor; the coefficient-only increment controls only one exact product-difference term. |
| `star_ownership` | Passed: the star remains on (w_j(2h\sqrt{X/n})); it does not half-weight or alter the Vaaler cutoff endpoint. |
| `alpha_capacity_scope` | No-go: the floor contributes no alpha moving-face delta.  The (O(H^{-1})) positive-frequency alpha-coefficient increment is usable only in a separately justified discrete-height telescoping argument. |
| `downstream_scope` | Passed: no projected alpha trace, outside-height limit, or full (\Omega_X^*\) variation is claimed. |

As an additional scale check, (K) coefficient-only upward steps have
unweighted variation exactly (K/2), while their (1/h)-weighted
variation accumulates logarithmically over a long height range.  Thus the
adjacent (O(1)) statement must not be silently promoted to a uniform bound
for an (O(H))-step traversal.

## 6. Dependencies and exact artifacts used

The derivation uses only the definitions and frozen distinctions in:

- `rounds/codex-managed/m9-m1-alpha-vaaler-height-floor/briefs/blind_vaaler_height_rederivation.md`
- `rounds/codex-managed/m9-m1-alpha-vaaler-height-floor/derivation_packet.md`

No external theorem is invoked; every analytic estimate needed above is
derived in the report.

### Isolation ledger

- Read the assigned blind-rederivation brief and its single permitted
  derivation packet.
- Did not read the proof graph, proof draft, state files, prior reports,
  syntheses, other Round-52 reports, or legacy evidence.
- Used no web source, numerical experiment, symbolic algebra system, or
  subagent.
- Wrote only this assigned report.

## 7. Recommended state effect

**Promote** the typed local discrete-height lemma (zero contour velocity,
exact adjacent identity, endpoint taper, and sharp weighted norms) after the
required conductor reviews.  **Reject** any claim that the floor is the
missing alpha-contour seam or itself supplies an alpha moving-face delta.
Make **no downstream change** to projected-trace, outside-height, or full
physical-coefficient claims until the simultaneous scale/profile/support/
star variations are separately controlled.
