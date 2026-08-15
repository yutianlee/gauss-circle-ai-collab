# Round 30 blind report: sharp moving-logarithm Fresnel lemma

Task: blind_log_fresnel_lemma  
Role: statement-only blind rederivation  
Allocation: 100% analytical/algebraic; no computation and no external theorem

## 1. Result: a sharp uniform lemma

The proposed abstract estimate is true with a logarithmic loss, and that
loss is sharp. For a uniformly nondegenerate one-dimensional saddle,
\[
 \int g(x)\operatorname {Log}(a+i(x-x_0))
       e^{i\Lambda\phi(x)}\,dx
 \ll \Lambda^{-1/2}\log(2+\Lambda)
 \bigl(\|g\|_\infty+\|g'\|_1\bigr),               \tag{30.1}
\]
uniformly for \(0\leq a\leq1\), for a moving \(x_0\) in a fixed compact
set, and for arbitrary moving integration endpoints in that set. The same
bound holds for either sign of the Hessian, when \(x_0\) crosses the
saddle, when it crosses either endpoint, and when the saddle and a moving
endpoint coincide.

If \(a=0\) and \(x_0\) equals an interior saddle, the leading term contains
\[
 -\frac12\Lambda^{-1/2}\log\Lambda
\]
times the ordinary full Fresnel coefficient. If the saddle is an endpoint,
the same logarithm multiplies the half-Fresnel coefficient. Hence
\(\log(2+\Lambda)\) cannot be removed for general coefficients.

The lemma preserves every pre-existing power of the large parameter; it
adds only one logarithm. Its application to the beta kernel is conditional,
however: the complete omega-recombined numerator must have a
scale-normalized \(W^{1,1}\) or bounded-variation norm. The permitted
context does not prove that hypothesis or the height-tail estimates.

## 2. Exact statement and hypotheses

### 2.1 Canonical moving-logarithm lemma

Fix \(R\geq1\). Let \(\Lambda\geq2\), \(\epsilon\in\{+1,-1\}\),
\([p,q]\subset[-R,R]\), \(r\in[-R,R]\), \(0\leq a\leq1\), and
\(G\in W^{1,1}([-R,R])\cap L^\infty([-R,R])\). Use the principal
logarithm for \(a>0\), and at \(a=0\) use its almost-everywhere boundary
value
\[
 \operatorname {Log}(iy)=\log|y|+
 {i\pi\over2}\operatorname {sgn}(y).              \tag{30.2}
\]
Then
\[
 \boxed{
 \left|\int_p^q G(t)\operatorname {Log}(a+i(t-r))
 e^{i\epsilon\Lambda t^2/2}\,dt\right|
 \leq C_R\Lambda^{-1/2}\log(2+\Lambda)
 \left(\|G\|_\infty+\|G'\|_1\right).}              \tag{30.3}
\]
The constant is independent of \(p,q,r,a,\Lambda\).

The same conclusion holds with \(t-r\) replaced by
\(\chi(t)-\chi(r)\), provided \(\chi\) is a \(C^2\) increasing
diffeomorphism with
\[
 0<c_\chi\leq\chi'(t)\leq C_\chi,\qquad
 \|\chi''\|_\infty\leq C_\chi.                     \tag{30.4}
\]
The constant then also depends on the bounds in (30.4).

### 2.2 Exact Morse corollary

Let \(J\) be a fixed compact interval and let
\(\phi\in C^3(J)\) have one uniformly nondegenerate critical point
\(s\) in \(J\) or at its boundary. Assume the exact Morse coordinate
\(\kappa\) is a uniformly \(C^2\) diffeomorphism on \(J\), with
\[
 \phi(x)=\phi(s)+{\epsilon\over2}\kappa(x)^2,\qquad
 \kappa(s)=0,\qquad
 \epsilon=\operatorname {sgn}\phi''(s).            \tag{30.5}
\]
This is equivalent to the usual one-dimensional uniform
nondegeneracy and monotonicity hypotheses after reducing \(J\) if
necessary.

For every subinterval \([P,Q]\subset J\), every \(x_0\in J\),
\(0\leq a\leq1\), and \(g\in W^{1,1}(J)\cap L^\infty(J)\),
\[
\begin{split}
 &\left|\int_P^Q g(x)\operatorname {Log}(a+i(x-x_0))
 e^{i\Lambda\phi(x)}\,dx\right|\\
 &\qquad\leq
 C_{\phi,J}\Lambda^{-1/2}\log(2+\Lambda)
 \left(\|g\|_\infty+\|g'\|_1\right).               \tag{30.6}
\end{split}
\]
Thus \(P\), \(Q\), \(x_0\), and \(s\) may coalesce in any order.
Changing the Hessian sign only conjugates the Fresnel phase and does not
change the estimate.

### 2.3 Sharp incomplete-Fresnel coefficient

Put
\[
 {\cal F}_\epsilon(T)=\int_0^T e^{i\epsilon y^2/2}\,dy,\qquad
 \tau_P=\sqrt{\Lambda}\,\kappa(P),\quad
 \tau_Q=\sqrt{\Lambda}\,\kappa(Q).                 \tag{30.7}
\]
If \(x_0=s\), \(a=0\), and \(g\) is \(C^2\) near \(s\), the
coalescing local term is
\[
\begin{split}
 I={}&-{e^{i\Lambda\phi(s)}g(s)\over
 2\sqrt{|\phi''(s)|}}\,
 \Lambda^{-1/2}\log\Lambda\\
 &\quad\times
 \{{\cal F}_\epsilon(\tau_Q)
       -{\cal F}_\epsilon(\tau_P)\}
 +O_{\phi,g,J}(\Lambda^{-1/2}),                    \tag{30.8}
\end{split}
\]
whenever the scaled endpoints have fixed limits or tend to infinity
without another degeneracy. Formula (30.8), rather than an ordinary
pointwise \(C^2\) stationary expansion, is the appropriate transition
normal form.

For a fixed interior saddle,
\[
 {\cal F}_\epsilon(+\infty)
 -{\cal F}_\epsilon(-\infty)
 =\sqrt{2\pi}\,e^{i\epsilon\pi/4}.
\]
For a saddle at one endpoint, the corresponding coefficient is
\(\sqrt{\pi/2}\,e^{i\epsilon\pi/4}\), exactly one half of the full
coefficient. These examples prove sharpness of the logarithm in (30.3).

## 3. Proof or derivation

It suffices first to prove (30.3). Set
\[
 h=\Lambda^{-1/2}
\]
and remove from \([p,q]\) the union
\[
 E=\{|t|\leq2h\}\cup\{|t-r|\leq2h\}.               \tag{30.9}
\]
The union has length \(O(h)\). Uniformly for \(0\leq a\leq1\),
\[
 \int_J|\operatorname {Log}(a+i(t-r))|\,dt
 \ll_R h\log(2/h)                                  \tag{30.10}
\]
on every interval \(J\) of length \(O(h)\). To see this, split
\(|t-r|\leq a\) from \(a<|t-r|\leq O(h)\). The first contribution is
\(O(a(1+|\log a|))\), and the second is bounded by the integral of
\(1+|\log|t-r||\). The imaginary part of the principal logarithm is
bounded by \(\pi/2\). Hence the contribution of \(E\) satisfies the
right side of (30.3).

On every component of \([p,q]\setminus E\), integrate by parts with
\[
 {d\over dt}e^{i\epsilon\Lambda t^2/2}
 =i\epsilon\Lambda t\,e^{i\epsilon\Lambda t^2/2}.
\]
There,
\[
 |\operatorname {Log}(a+i(t-r))|\ll_R\log(2/h),
\qquad
 \left|{d\over dt}\operatorname {Log}(a+i(t-r))\right|
 \leq {1\over |t-r|}.                              \tag{30.11}
\]
The boundary terms and the terms containing \(G'\) are
\[
 \ll_R h\log(2/h)
 \left(\|G\|_\infty+\|G'\|_1\right).
\]
The derivative of \((\Lambda t)^{-1}\) contributes the same amount,
because
\[
 {1\over\Lambda}\int_{|t|\geq2h}{dt\over t^2}
 \ll h.
\]
Finally, the logarithmic derivative term is controlled by the elementary
two-center estimate
\[
 {1\over\Lambda}
 \int_{\substack{|t|\geq2h\\|t-r|\geq2h\\|t|\leq R}}
 {dt\over|t|\,|t-r|}
 \ll_R h.                                          \tag{30.12}
\]
For \(|r|\leq4h\), compare the integrand with \(t^{-2}\). For
\(|r|>4h\), split at \(t=r/2\) and use
\[
 {1\over\Lambda|r|}\log{|r|\over h}
 =h\,{\log(|r|/h)\over |r|/h}\ll h.
\]
This proves (30.3).

Under (30.4), distances \(|\chi(t)-\chi(r)|\) and \(|t-r|\) are
comparable, and differentiating the logarithm gives the same bound as
(30.11), up to a fixed constant. This proves the generalized canonical
lemma.

For (30.6), make the exact change \(t=\kappa(x)\). The new smooth
amplitude is
\[
 G(t)=g(\kappa^{-1}(t))(\kappa^{-1})'(t),
\]
whose \(L^\infty+W^{1,1}\) norm is bounded by the corresponding norm of
\(g\). Moreover,
\[
 x(t)-x_0=\kappa^{-1}(t)-\kappa^{-1}(\kappa(x_0)),
\]
so the generalized form of (30.3) applies. Arbitrary moving endpoints
only truncate the canonical interval and do not affect the constant.

To obtain (30.8), put \(t=\Lambda^{-1/2}y\). Since
\[
 x(t)-s={t\over\sqrt{|\phi''(s)|}}+O(t^2),
\]
the logarithm equals
\[
 -\frac12\log\Lambda+
 \operatorname {Log}\left(
 {iy\over\sqrt{|\phi''(s)|}}+O(\Lambda^{-1/2}y^2)
 \right).
\]
The first term gives (30.8). The remaining logarithmic function is locally
integrable, and its tails are controlled by one integration by parts on
dyadic \(y\)-annuli. This gives the stated \(O(\Lambda^{-1/2})\)
remainder. Taking a fixed smooth \(g\) with \(g(s)\neq0\) proves that the
\(\Lambda^{-1/2}\log\Lambda\) term is genuinely present.

### Finite-section interpretation

On a polytope cell for which \(L\in[A(L),B(L)]\), subtracting the
diagonal value from the PV numerator gives
\[
\begin{split}
 \operatorname {PV}\int_{A(L)}^{B(L)}
 {H(L,\nu)\over L-\nu}\,d\nu
 ={}&H(L,L)
 \{\log|L-A(L)|-\log|L-B(L)|\}\\
 &+\int_{A(L)}^{B(L)}
 {H(L,\nu)-H(L,L)\over L-\nu}\,d\nu .              \tag{30.13}
\end{split}
\]
The second term is regular if \(H\) has one controlled \(\nu\)-derivative.
On cells where \(L\notin[A(L),B(L)]\), there is no PV singularity and
ordinary nonstationary amplitude estimates apply.
The first is a finite sum of moving logarithms. The delta trace
\(\pi\mathbf1_{|L|<V}H(L,L)\) is a bounded-variation jump amplitude and
has ordinary \(O(\Lambda^{-1/2})\) Fresnel size, even when the jump meets
a saddle. Thus (30.6) is exactly the abstract estimate needed for the
face logarithms, conditional on normalized variation of their
coefficients.

## 4. First doubtful or unproved step

The first unproved project-specific step is showing that, after restoring
the omega-recombined radial factor, masks, profiles, floors, endpoint
stars, and all scale variables, every coefficient in (30.13) has a
uniform scale-normalized \(W^{1,1}\) or BV norm. The abstract lemma cannot
infer this from a separated pointwise \(q^{-2}\) value bound.

The height-tail and finite-side pieces are also absent from the abstract
integral. Their norms may grow with \(U,V,S\), and the kinks at changes of
the max/min endpoints \(A(L),B(L)\) must be entered once in the BV ledger.
Until those facts are proved, (30.6) does not certify the full beta trace.

## 5. Control tests and outcomes

### Support-and-degeneracy

**Pass under the stated hypotheses.** The estimate is uniform for arbitrary
subintervals and moving singularities in a fixed compact set. It requires a
uniformly nondegenerate Morse coordinate. If \(\phi''(s)\) tends to zero,
the \(\Lambda^{-1/2}\) scale is false and an Airy-type analysis is needed.
Unbounded \(x_0\) requires the harmless additional factor
\(1+\log(2+|x_0|)\).

### Endpoint-uniformity

**Pass.** The proof does not divide by the distance from \(x_0\) to an
endpoint. A one-sided logarithm is locally integrable, and (30.8) gives the
correct incomplete- and half-Fresnel coefficients when the singularity,
saddle, and endpoint coalesce.

### Coefficient-adversary

**Sharp pass with an essential hypothesis.** The logarithmic loss is
already necessary for a fixed smooth coefficient with \(g(s)\neq0\) and
\(x_0=s\). A bound using only \(\|g\|_\infty\) and no variation control is
false: choosing \(g_\Lambda(x)=e^{-i\Lambda\phi(x)}g_0(x)\) cancels the
oscillation and leaves an order-one logarithmic integral. The
\(\|g'\|_1\) term in (30.1) correctly detects this adversary. No property
of \(\chi_4\) is used in the abstract lemma, so it supplies analytic
infrastructure rather than the final arithmetic saving.

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were read or used:

1. protocol.md;
2. state/active_campaign.yml;
3. rounds/codex-managed/m9-m1-beta-outside-v-side-reconciliation/synthesis.md.

No proof graph, proof draft, other Round-30 report, computation, or web
source was read or used.

## 7. Recommended state effect

- **Promote as an abstract analytic lemma:** the uniform moving-logarithm
  estimate (30.3), its exact-Morse form (30.6), both Hessian signs, and the
  incomplete/half-Fresnel normalization.
- **Promote sharpness:** a factor \(\log(2+\Lambda)\) is unavoidable for
  general smooth coefficients when a logarithmic face meets a saddle.
- **Retain conditionally:** preservation of the local \(q^{-2}\) power.
  It follows with only a logarithmic loss if the complete beta numerator
  satisfies the required normalized BV bound.
- **Retain open:** that actual-profile BV bound, all height and finite-side
  tails, the complete \(q,h,D_j,x\) summation, M9-M1, M9, and the final
  Gauss-circle target.
