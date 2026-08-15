# Perron/BV pointwise kernel bound

## 1. Result

The requested scalar estimate is valid for the **profile kernel obtained
before radial functional-equation reflection**, and hence for its exact
matching-profile projection:

\[
 \sup_{T,h,q}|\mathcal H^{\rm prof}_{T,X}(h,q)|\ll_W\log(2X). \tag{P}
\]

This is a pointwise symmetric-Perron/BV statement; it uses no
\(\int|du/u|\). The height inversion is absolutely convergent and simply
returns the bounded Vaaler factor. The unique spatial jump is a uniformly
bounded sine integral, including its endpoint half weight. Interior and
smooth-top remainders are uniformly bounded per scale, and there are
\(O(\log X)\) active scales.

But Round 16 did not define a scalar \(\mathcal H_{T,X}\) after the radial
functional equation and every residue subtraction. The reflected term
contains the radial transform \(G_v(1-s)K_z(1-s)\), its \(s\)-contour and
finite horizontal sides. Those depend on the radial variable/product and
cannot be assigned pointwise to a divisor incidence as an actual-profile
BV kernel without performing the open radial inversion/correlation.
Thus (P) unconditionally proves the proposed high-\(2\)-adic tail only for
the exact unreflected profile (and any post-residue formulation whose
remaining scalar kernel is explicitly this profile kernel), not for the
schematic full Round-16 post-functional-equation object. The claim
\(\sup|\mathcal H_{T,X}|\ll\log X\) in that broader meaning is not presently
well-posed, rather than false.

## 2. Exact statement and hypotheses

Let \(D_j=2^{-j}\lfloor\sqrt X\rfloor\),
\(H_j=\lfloor D_jX^{-1/4}\rfloor\), and let \(J+1\ll\log(2X)\) be the
actual active scales. Fix \(a,b>0\) (one may take
\(a=b=1/\log(2X)\)). Put

\[
 d_{h,q}=2\sqrt X\sqrt{h/q},\qquad B_j(h)=\frac{H_j+1}{h}.
\]

For \(j\ge1\), define

\[
 P_j(h,q)=\frac1{(2\pi i)^2}\int_{(a)}\int_{(b)}
 \widehat W(u)\widehat\phi(v)(D_j/d_{h,q})^uB_j(h)^v\,dv\,du.
\]

For \(j=0\), truncate only the spatial line symmetrically:

\[
 P_{0,T}(h,q)=\frac1{(2\pi i)^2}\int_{a-iT}^{a+iT}\int_{(b)}
 \widehat W_+(u)\widehat\phi(v)(D_0/d_{h,q})^uB_0(h)^v\,dv\,du.
\]

The scalar actual-profile kernel is
\(\mathcal H^{\rm prof}_{T,X}=P_{0,T}+\sum_{j=1}^JP_j\).
All endpoint stars are the symmetric Mellin values.

## 3. Proof or derivation

Height inversion is independent of \(u\). Since
\(\widehat\phi(b+i\nu)\ll_b(1+|\nu|)^{-3}\),

\[
 \frac1{2\pi i}\int_{(b)}\widehat\phi(v)B_j(h)^v\,dv
 =\phi(h/(H_j+1)),
\]

with value \(0\) at \(h=H_j+1\), and its absolute value is bounded by a
constant. This step crosses no \(v=0\) pole: the line remains
\(\Re v=b>0\). A reflected contour displacement would instead create the
separate height residue and is not part of the scalar inversion.

For \(j\ge1\), ordinary Mellin inversion gives

\[
 P_j(h,q)=\phi(h/(H_j+1))W(d_{h,q}/D_j),
\]

so \(|P_j|\ll_W1\). For the top, write exactly

\[
 \widehat W_+(u)=\frac1u+R_W(u),\qquad
 R_W(u)=-\frac1u\int_0^1W'(t)t^u\,dt.
\]

Because \(W'\) is smooth and supported away from \(0,1\), \(R_W\) is
integrable on \(\Re u=a\), uniformly for \(0<a\le1\), and its inverse is
bounded. For \(A=D_0/d_{h,q}>0\), the non-smooth part is

\[
 Q_{a,T}(A)=\frac1{2\pi i}\int_{a-iT}^{a+iT}\frac{A^u}{u}\,du.
\]

Writing \(x=\log A\) and pairing \(t,-t\),

\[
 Q_{a,T}(A)=\frac{A^a}{\pi}\int_0^T
 \frac{a\cos(tx)+t\sin(tx)}{a^2+t^2}\,dt.
\]

The cosine term has absolute integral at most \(\pi/2\). For the sine
term, scale \(t=a y\); Dirichlet's test (or one integration by parts after
splitting at \(y=1\)) gives
\[
 \sup_{a,T>0,\ x\in\mathbb R}\left|
 \int_0^T\frac{t\sin(tx)}{a^2+t^2}\,dt\right|\le C.
\]
On the only incidences relevant to \(W_+\), \(d_{h,q}/D_0\) lies in the
fixed support \([1/2,4/3]\), so \(A^a\ll1\); outside that range the exact
profile is zero and the completed \(1/u+R_W\) inversions cancel. Hence
\(\sup_{T,h,q}|P_{0,T}|\ll_W1\), and summing scales proves (P).
As \(T\to\infty\), \(Q_{a,T}\) gives \(1,1/2,0\) according as
\(A>1,A=1,A<1\); the half residue is retained.

This proof is scalar/radial separation: the factor
\((hq)^{-3/4}e(\sqrt{Xhq})\) never enters (P). By contrast, after
functional-equation reflection the surviving expression contains

\[
 \int_{(s)}G_v(1-s)K_{u+v}(1-s)F_{-(u+v)}(s)\,ds
+\text{finite horizontal sides}.
\]

Neither the gamma quotient nor the radial transform is a BV profile
multiplier in \(A\). Expanding \(F_{-z}\) and inverting \(s\) is precisely
the unresolved radial correlation. The zeta, \(v=0\), \(u=0\), and radial
endpoint residues must remain separate; subtracting them does not turn the
displayed \(s\)-integral into the scalar kernel above.

## 4. First doubtful or unproved step

The first unproved step is an exact post-reflection decomposition showing
that every non-residue \(s\)-integral and horizontal side equals a radial
coefficient times a scalar profile multiplier satisfying (P). No accepted
artifact supplies this, uniformly as the finite rectangles tend to
infinity. Assuming it would absorb the open maximal radial correlation
into the definition of \(\mathcal H\).

## 5. Required control test and outcome

For a single incidence, the sharp part satisfies
\[
 \lim_{T\to\infty}Q_{a,T}(A)
 =\mathbf1_{A>1}+\tfrac12\mathbf1_{A=1},
\]
and \(Q(A)+Q(A^{-1})=1\) in the symmetric limit. Thus the test preserves
the top endpoint and reproduces completion rather than false cancellation.
The bound is uniform at \(A=1\), where absolute \(1/u\) integration would
diverge. No numerical test was used.

## 6. Dependencies and exact artifacts used

Used only the Round-18 authorized packet: protocol.md,
state/proof_obligations.yml, state/active_campaign.yml, the Round-15
blind double-Mellin derivation, Round-16 synthesis and reports, Round-17
synthesis, and the assigned brief. No external theorem was invoked.

## 7. Recommended state effect

Promote (P) as the uniform pointwise bound for the explicitly defined
unreflected actual-profile kernel and its norm-one local-reflection
projection. Do **not** promote the broader
M9-M1-high-2adic-kernel-pointwise-bound until the post-reflection
gamma/radial terms are either excluded from \(\mathcal H\) by definition or
formally separated with their own uniform bounds. Consequently retain the
Round-17 high-\(2\)-adic tail as conditional for the full Round-16 maximal
kernel. GAR, the top Perron angular correlation, M9-M1, and M9 remain open.
