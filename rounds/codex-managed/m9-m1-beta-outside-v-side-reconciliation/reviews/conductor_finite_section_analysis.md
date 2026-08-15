# Conductor review: the finite-section top kernel and the correct edge norm

Campaign: `m9-m1-beta-outside-v-side-reconciliation`  
Role: conductor's independent analytic review  
Allocation: 100% analytical/algebraic; no numerical experiment or external theorem

## 1. Exact finite-section kernel

The isolated expression

\[
 C_{a,V}(L)=\int_{-V}^{V}\frac{H(L,\nu)}{a+i(L-\nu)}\,d\nu
\]

must retain the original top-height constraint.  In the accepted diagonal
coordinates

\[
 \mu=L-\nu,\qquad |\mu|\le U,\qquad |\nu|\le V,
\]

the exact slice is

\[
 \boxed{
 C_{a,U,V}(L)=\int_{A(L)}^{B(L)}
 \frac{H(L,L-\mu)}{a+i\mu}\,d\mu,}
 \tag{29.C1}
\]

where

\[
 A(L)=\max\{-U,L-V\},\qquad
 B(L)=\min\{U,L+V\}.
 \tag{29.C2}
\]

The interval is nonempty only for \(|L|\le U+V\).  This correction does
not remove the collisions at \(L=\pm V\), but it identifies their proper
norm: they are logarithmic singularities in the still-integrated variable
\(L=\alpha-\beta\), not divergences of the complete operator.

Assume first that \(H\) is \(C^1\) in its second argument.  Put
\(h_0(L)=H(L,L)\).  Subtraction at \(\mu=0\) gives

\[
 C_{a,U,V}(L)=h_0(L)J_a(A(L),B(L))+E_a(L),             \tag{29.C3}
\]

with

\[
 J_a(A,B)=\frac1i\{\Log(a+iB)-\Log(a+iA)\},           \tag{29.C4}
\]

and

\[
 |E_a(L)|\le (B(L)-A(L))
 \sup_{\nu}|\partial_\nu H(L,\nu)|.                   \tag{29.C5}
\]

Indeed, the numerator in the remainder is \(O(|\mu|)\), while
\(|\mu|/|a+i\mu|\le1\).  Thus every nonuniformity is explicit in
\(J_a\).

## 2. Physical top limit and endpoint behavior

Away from \(A=0\) and \(B=0\), (29.C4) has the limit

\[
 J_0(A,B)=
 \begin{cases}
  \pi-i\log(B/|A|),&A<0<B,\\
  -i\log(B/A),&0<A<B,\\
  -i\log(|B|/|A|),&A<B<0.
 \end{cases}                                             \tag{29.C6}
\]

Equivalently, almost everywhere in \(L\),

\[
 \boxed{
 C_{0,U,V}(L)=
 \pi\mathbf1_{\{|L|<V\}}H(L,L)
 -i\operatorname {PV}\!\int_{A(L)}^{B(L)}
       \frac{H(L,L-\mu)}{\mu}\,d\mu.}
 \tag{29.C7}
\]

At \(L=V\), \(A(L)=0\) locally (provided the top interval is nonempty),
and at \(L=-V\), \(B(L)=0\).  Hence (29.C6) has the already detected
\(\log|L\mp V|\) singularities and the Plemelj jump.  In particular,
pointwise uniform \(C^2\) control in \(L\) is false.

However, for every finite \(p\), the family \(J_a(A(L),B(L))\) is locally
bounded in \(L^p(dL)\), and it converges to (29.C6) in local \(L^p\).
This follows from the elementary uniform estimate

\[
 \sup_{0<a\le1}\int_{-c}^{c}
 \bigl|\Log(a+iy)\bigr|^pdy<\infty.                   \tag{29.C8}
\]

To prove (29.C8), split \(|y|\le a\) and \(a<|y|\le c\).  The first
part is \(O(a(1+|\log a|)^p)\); on the second, replace
\(|\Log(a+iy)|\) by \(O(1+|\log|y||)\), which is integrable to every
finite power.  The same split proves convergence.  Therefore the
finite-height edge obstructs a pointwise-amplitude lemma, but it does not
obstruct the top limit in an integrated \(L^p\), distributional, or
oscillatory sense.

## 3. Orientation audit

Let \({\cal V}_b,{\cal V}_\ell\) be upward right/left verticals and let
\({\cal S}_\pm\) be the upper/lower horizontal segments, both written
left-to-right.  Positive rectangle orientation gives

\[
 {\cal V}_b={\cal V}_\ell+{\cal S}_+-{\cal S}_-
 +2\pi i\sum\operatorname {Res}.                       \tag{29.C9}
\]

At \(L=V\), \({\cal V}_b\) and \({\cal S}_+\) have the same logarithmic
coefficient.  At \(L=-V\), \({\cal V}_b\) and the retained term
\(-{\cal S}_-\) again have the same coefficient.  Hence (29.C9) transfers
the edge logarithm; it does not cancel it.  The cancelling closed-boundary
combination is

\[
 {\cal V}_b-{\cal S}_++{\cal S}_-
 ={\cal V}_\ell+2\pi i\sum\operatorname {Res}.          \tag{29.C10}
\]

No accepted operator has yet been shown to contain (29.C10) as an
independently estimated subtotal.  Axial, top, and corner residues have no
fixed-\(V\) edge-log coefficient and cannot supply the missing sign.

Thus the frozen proposed cancellation is false with the standard retained
side orientation.  This conclusion is compatible with the existence of
the integrated limit (29.C7).

## 4. A replacement analytic lemma

The appropriate stationary tool is a logarithmic-amplitude Fresnel lemma,
not a \(C^2\)-amplitude lemma.  The elementary local model is the following.

Let \(\varphi\in C^3[-c,c]\) have one nondegenerate stationary point, let
\(g\in C^1_c[-c,c]\), and allow the logarithmic point \(x_0\) to cross the
stationary point and the integration endpoints.  Then, uniformly for
\(0<a\le1\) and \(\lambda\ge2\),

\[
 \boxed{
 \left|\int_{-c}^{c}g(x)\Log(a+i(x-x_0))
 e^{i\lambda\varphi(x)}\,dx\right|
 \ll_{\varphi,c}
 \lambda^{-1/2}\log(2\lambda)
 (\|g\|_\infty+\|g'\|_1).}
 \tag{29.C11}
\]

For a proof, use the exact Morse coordinate near the stationary point.
On the interval of radius \(r=\lambda^{-1/2}\), take absolute values and
apply

\[
 \sup_{a,x_0}\int_I|\Log(a+i(x-x_0))|dx
 \ll r\log(2/r),                                     \tag{29.C12}
\]

where the supremum is over logarithmic points meeting a fixed enlargement
of \(I\); separated logarithmic points are easier.  On each dyadic shell
\(|x-x_s|\asymp2^kr\), first-derivative integration by parts costs
\((\lambda2^kr)^{-1}\).  The logarithm has \(O(1)\) variation on a
dyadic interval not containing its point, while an interval containing the
point is split there and uses (29.C12).  Summing the geometric shell bounds
gives (29.C11).  If \(x_0\) and \(x_s\) are separated by at least \(2r\),
partition once between them; the stationary neighborhood sees a bounded
logarithm of size \(O(\log(2\lambda))\), and the logarithmic neighborhood
has nonzero phase derivative.  This proves the same uniform bound.

In the accepted alpha phase, the unscaled Gaussian contribution is of
size \(\lambda^{1/2}\), rather than \(\lambda^{-1/2}\), because alpha is
scaled by its saddle height.  Formula (29.C11) therefore says precisely
that collision with \(L=\pm V\) costs at most one logarithm relative to
the accepted Fresnel main size.  It does not change the power of \(q\).
Consequently the Round-27 local \(q^{-2}\) capacity is compatible with
the finite-height edge, with an extra \(\log(2+\lambda)\) loss that can be
absorbed into \(X^\varepsilon\), provided the remaining smooth factors
have the required scaled variation and the finite-side/exhaustion ledger
is handled in an integrated norm.

## 5. Scope and next proof interface

This review proves neither the complete beta-transition estimate nor the
height exhaustion.  It establishes four narrower conclusions:

1. the exact top constraint changes the finite interval to (29.C1)--(29.C2);
2. the standard outside-side orientation does not cancel the edge log;
3. the physical top limit exists in finite local \(L^p\) norms despite the
   failure of pointwise \(C^2\);
4. a logarithmic-amplitude stationary lemma loses only a logarithm, not a
   power, even at saddle-edge coalescence.

The next smallest interface is therefore an integrated finite-section
lemma for the *complete* recombined beta numerator: prove the scaled
variation hypotheses needed to insert (29.C3) into (29.C11), then control
the usual retained sides in an integrated height norm.  Requiring uniform
pointwise \(C^2\) after the \(\nu\)-convolution is unnecessarily strong and
is rigorously false.

