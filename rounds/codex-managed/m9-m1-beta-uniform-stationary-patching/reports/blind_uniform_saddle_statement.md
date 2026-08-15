# Round 28 blind report: uniform positive-saddle normal form and a finite-height obstruction

Task: blind_uniform_saddle_statement  
Role: statement-only blind rederivation  
Allocation: 100% analytical/algebraic; no numerical experiment and no external theorem

## 1. Result: scoped lemma and no-go result

There is an exact endpoint-uniform Fresnel normal form for the positive-alpha
model phase. It covers saddle entry, separated interior, saddle exit, and
positive nonstationary intervals without changing normalization. In
particular, an entry or exit contributes an incomplete Fresnel factor, and
an endpoint exactly at the saddle contributes one half of the full Fresnel
constant when the other endpoint is remote in stationary units.

This lemma does **not** extend the accepted separated \(q^{-2}\) estimate by
itself. The Round-27 statement supplies a value bound at a separated saddle,
but not the scaled two-derivative bounds on the recombined signed amplitude
which the uniform lemma requires. There is also an explicit obstruction at
finite \(v\)-height: after the physical top limit, the PV amplitude has a
logarithmic singularity when its moving pole reaches \(v=\pm V\). Thus the
isolated finite vertical segment has no endpoint-uniform amplitude. Any
global uniform result must first combine this logarithm with the finite
outside-\(v\) side, or take a justified height limit before the physical
top limit.

## 2. Exact statement and hypotheses

### 2.1 Exact finite alpha support

With
\[
 t={\alpha+\beta\over2},\qquad
 \mu=\alpha-\beta-\nu,
\]
the finite restrictions \(|t|\leq S\), \(|\mu|\leq U\), and
\(|\nu|\leq V\) give, for fixed \((\beta,\nu)\) with \(|\nu|\leq V\),
\[
 I_{\beta,\nu}^{U,S}=[p,q],
\]
\[
 p=\max\{\beta+\nu-U,-2S-\beta\},\qquad
 q=\min\{\beta+\nu+U,2S-\beta\}.                 \tag{28.1}
\]
The integral is empty if \(p\geq q\). This is the exact finite alpha range;
the positive large-alpha mask must still be retained as an amplitude.

### 2.2 Endpoint-uniform positive-saddle lemma

Let \(\lambda=\alpha _0=\pi q\sqrt{Xx}/D_j\geq1\), and define
\[
 h(y)=y\log y-y+1,\qquad
 \Phi_\lambda(\alpha)=\lambda h(\alpha/\lambda)
 =\alpha\log(\alpha/\lambda)-\alpha+\lambda.      \tag{28.2}
\]
Then \(\Phi_\lambda'(\alpha)=\log(\alpha/\lambda)\),
\(\Phi_\lambda''(\alpha)=1/\alpha\), and the unique positive critical point
is \(\alpha=\lambda\).

Fix \(0<c<1<C<\infty\). Let \([P,Q]\) be any component of the positive
alpha support contained in \([c\lambda,C\lambda]\). Suppose the complete
amplitude after all required algebraic recombinations and after the signed
top limit has the form
\[
 a_\lambda(\alpha)=A_\lambda(\alpha/\lambda),\qquad
 \|A_\lambda\|_{C^2([c,C])}\leq M_\lambda.         \tag{28.3}
\]
Define the exact Morse coordinate
\[
 \zeta(y)=\operatorname {sgn}(y-1)\sqrt{2h(y)},\qquad
 \tau_R=\sqrt{\lambda}\,\zeta(R/\lambda)
 \quad(R=P,Q),                                    \tag{28.4}
\]
and
\[
 {\cal F}(T)=\int_0^T e^{iu^2/2}\,du.             \tag{28.5}
\]
Then
\[
 \int_P^Q a_\lambda(\alpha)e^{i\Phi_\lambda(\alpha)}\,d\alpha
 =\sqrt{\lambda}\,A_\lambda(1)
   \{{\cal F}(\tau_Q)-{\cal F}(\tau_P)\}
   +{\cal R}_{P,Q},                               \tag{28.6}
\]
where the remainder is given exactly in (28.14) below and satisfies
\[
 |{\cal R}_{P,Q}|\leq C_{c,C}M_\lambda             \tag{28.7}
\]
uniformly as either endpoint crosses the saddle.

The exact transition parameters are \(\tau_P,\tau_Q\), not merely
\((P-\lambda)/\sqrt{\lambda}\) and
\((Q-\lambda)/\sqrt{\lambda}\). In a bounded stationary window,
\[
 \tau_R={R-\lambda\over\sqrt{\lambda}}
 \left(1+O_{c,C}\left({|R-\lambda|\over\lambda}\right)\right). \tag{28.8}
\]
Since
\[
 {\cal F}(+\infty)=e^{i\pi/4}\sqrt{\pi/2},\qquad
 {\cal F}(-\infty)=-e^{i\pi/4}\sqrt{\pi/2},        \tag{28.9}
\]
\(P=\lambda\), \(\tau_Q\to+\infty\) gives the entry half-Fresnel
constant, and \(Q=\lambda\), \(\tau_P\to-\infty\) gives the exit
half-Fresnel constant. If an endpoint is only \(O(\sqrt{\lambda})\) from
the saddle, the incomplete factor in (28.6) is the exact leading term.

If the positive interval is nonstationary and
\[
 d=\inf_{\alpha\in[P,Q]}|\log(\alpha/\lambda)|>0,
\]
then the exact alternative identity is
\[
 \begin{split}
 \int_P^Q a(\alpha)e^{i\Phi_\lambda(\alpha)}\,d\alpha
 &=\left[{a(\alpha)e^{i\Phi_\lambda(\alpha)}
       \over i\log(\alpha/\lambda)}\right]_P^Q\\
 &\quad-\int_P^Q e^{i\Phi_\lambda(\alpha)}
 \left\{{a'(\alpha)\over i\log(\alpha/\lambda)}
 -{a(\alpha)\over i\alpha\log^2(\alpha/\lambda)}\right\}\,d\alpha .
                                                               \tag{28.10}
 \end{split}
\]
This treats both positive nonstationary sides without pretending that
(28.10) is uniform when \(d\) tends to zero.

### 2.3 Required signed top order

In the Round-27 notation set
\[
 L=\alpha-\beta,\qquad K=-\alpha-\beta,
\]
\[
 H_b(\alpha,\beta,\nu)
 ={\widehat\phi(b+i\nu)\over
   \rho _0-i(\nu-K)/2}.
\]
Away from the artificial-rho seam and for a smooth full-line test
amplitude, the physical limit must be taken in distributions first:
\[
 \begin{split}
 C_0(\alpha,\beta)
 &=\lim_{a\downarrow0}\int_{\mathbb R}
 {H_b(\alpha,\beta,\nu)\over a+i(L-\nu)}\,d\nu\\
 &=\pi H_b(\alpha,\beta,L)
 -i\,\operatorname {PV}\int_{\mathbb R}
 {H_b(\alpha,\beta,\nu)\over L-\nu}\,d\nu .        \tag{28.11}
 \end{split}
\]
Only the signed sum in (28.11) may be inserted into \(A_\lambda\).
Absolute values, the Morse change of variable, and endpoint asymptotics
come afterwards. Interchanging the \(a\downarrow0\) limit with the alpha
integral requires an alpha-uniform bound on the relevant test-function
seminorms; such a bound is an additional hypothesis, not a consequence of
the separated value estimate.

### 2.4 Finite-height obstruction

At finite \(v\)-height define
\[
 C_{a,V}(L)=\int_{-V}^{V}{H(\nu)\over a+i(L-\nu)}\,d\nu .
                                                               \tag{28.12}
\]
If \(H\) is integrable on \([-V,V]\), is \(C^1\) near \(V\), and
\(H(V)\neq0\), then
\[
 C_{a,V}(V)=-iH(V)\log(1/a)+O_{H,V}(1)
 \qquad(a\downarrow0).                              \tag{28.13}
\]
Equivalently, for \(L\neq V\) approaching \(V\), its PV part contains
\[
 H(V)\log{2V\over|L-V|}+O_{H,V}(1).
\]
The same statement holds at \(-V\). Therefore the isolated finite segment
does not satisfy (28.3) uniformly when \(L=\alpha-\beta\) crosses a
finite-height endpoint. The delta value at the endpoint is also
convention-dependent because the hard characteristic is discontinuous
there. The finite outside side or a justified order of height limits is
mathematically necessary.

## 3. Proof or derivation

Equation (28.1) follows by intersecting
\[
 \alpha\in[\beta+\nu-U,\beta+\nu+U]
 \quad\hbox{and}\quad
 \alpha\in[-2S-\beta,2S-\beta].
\]

For the uniform lemma, \(h(y)\geq0\), with equality only at \(y=1\).
The function \(\zeta\) in (28.4) is a smooth increasing diffeomorphism on
every compact subinterval of \((0,\infty)\), and
\(\zeta(1)=0,\ \zeta'(1)=1\). Put
\(\tau=\sqrt{\lambda}\zeta(y)\), \(y=\alpha/\lambda\), and
\[
 g_\lambda(\tau)
 ={A_\lambda(y(\tau))\over\zeta'(y(\tau))}.
\]
The change of variables is exact and gives
\[
 I=\sqrt{\lambda}\int_{\tau_P}^{\tau_Q}
 g_\lambda(\tau)e^{i\tau^2/2}\,d\tau.
\]
Since \(g_\lambda(0)=A_\lambda(1)\), define
\[
 B_\lambda(\tau)=
 {g_\lambda(\tau)-g_\lambda(0)\over\tau},
\]
with the continuous value at zero. Then
\[
 {\cal R}_{P,Q}
 =\sqrt{\lambda}\int_{\tau_P}^{\tau_Q}
 \tau B_\lambda(\tau)e^{i\tau^2/2}\,d\tau.          \tag{28.14}
\]
This is the promised exact remainder. On \([c,C]\),
\[
 \|B_\lambda\|_\infty\ll_{c,C}M_\lambda/\sqrt{\lambda},
\qquad
 \|B_\lambda'\|_\infty\ll_{c,C}M_\lambda/\lambda.
\]
Using \(\tau e^{i\tau^2/2}=(1/i)(e^{i\tau^2/2})'\) in (28.14)
proves (28.7), because the transformed interval has length
\(O_{c,C}(\sqrt{\lambda})\). Equations (28.8)-(28.9) follow from
Taylor expansion of \(h\) at one and one elementary contour rotation for
the Gaussian integral. Equation (28.10) is direct integration by parts
using \(\Phi_\lambda'=\log(\alpha/\lambda)\).

For (28.13), put \(y=V-\nu\). The portion \(0\leq y\leq\delta\) equals
\[
 H(V)\int_0^\delta{dy\over a+iy}+O_{H,V}(1)
 ={H(V)\over i}\{\log(a+i\delta)-\log a\}+O_{H,V}(1),
\]
which is \(-iH(V)\log(1/a)+O_{H,V}(1)\). The PV asymptotic follows by
subtracting \(H(V)\) and integrating the constant term explicitly.

## 4. First doubtful or unproved step

The first missing project-specific step is not the Fresnel calculation. It
is the assertion that the **complete recombined signed amplitude** obeys
the scaled \(C^2\) bound (28.3) uniformly in \(q,h,D_j,x,U,V,S\), after
combining
\[
 R_1=\omega G+(1-\omega)R_1-\omega E_1
\]
and the finite outside sides. Round 27 proves only a separated saddle value
bound on fixed \(b>0\); it does not provide these alpha derivatives or a
finite-height cancellation of (28.13).

The permitted statements also do not specify the complete negative-alpha
phase. The displayed gamma phase alone does not prove that the negative
side is nonstationary after all linear scale phases are restored.
Consequently the negative-alpha sector can presently be treated only by
the generic integration-by-parts formula under an explicit lower bound
\(|\Phi'|\geq\kappa>0\). Declaring it nonstationary without that phase
audit would be an unsupported step.

## 5. Control tests and outcomes

### Support-and-degeneracy

**Scoped pass.** Equation (28.1) keeps both finite-height constraints, and
the Morse map is used only on a positive component
\([c\lambda,C\lambda]\). It does not cross \(\alpha=0\). The
double-bounded region and the small-\(\lambda\) region must remain in their
separate ledger. The global control remains open because the actual masks
and finite sides have not been estimated.

### Residue-and-normalization

**Scoped pass.** The lemma introduces no new power of \(q\): it is an exact
change of variable, and the half-Fresnel coefficient has the same
normalization as the full stationary coefficient, with factor one half at
an exact isolated endpoint. The artificial-rho pieces are not estimated
separately; their exact recombination is required before (28.3). This
preserves, but does not re-prove or globally extend, the Round-27
\(q^{-1}\) radial and local \(q^{-2}\) signed normalization.

### Endpoint-uniformity

**Pass for a smooth recombined amplitude; fail for the isolated finite
vertical segment.** Formula (28.6) is uniform through stationary entry and
exit. Formula (28.13) is a direct falsifier of the needed amplitude
hypothesis at a hard \(v\)-height edge. Thus a uniform project lemma must
include the outside-side cancellation or establish a valid order of
limits.

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were used:

1. protocol.md;
2. state/active_campaign.yml;
3. rounds/codex-managed/m9-m1-diagonal-transition-exhaustion/synthesis.md;
4. rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/synthesis.md.

No proof graph, proof draft, other Round-28 report, computation, or web
source was read or used.

## 7. Recommended state effect

- **Promote only as a scoped analytic tool:** the exact positive-alpha
  Morse/Fresnel decomposition (28.6), its half-Fresnel endpoint
  normalization, and the nonstationary identity (28.10), conditional on
  the complete signed amplitude satisfying (28.3).
- **Record as a no-go result:** a separated pointwise \(q^{-2}\) saddle
  bound cannot by itself imply a uniform transition bound; finite
  \(v\)-height creates the explicit logarithm (28.13).
- **Retain open:** uniform scaled derivative bounds, cancellation with
  finite outside sides, artificial-rho seam estimates, the negative-alpha
  phase audit, all \(q,h,D_j,x\) sums, M9-M1, M9, and the final target.
