# Round 4 hostile falsifier: generic-band signed correlation

## 1. Result

Simple numerator-residue pairing does **not** cancel the generic single-lift
critical band. There are two distinct conclusions.

1. **Rigorous obstruction.** For a large class of fixed denominator pairs, the
   pair sum \(1/q_1+1/q_3\) has a unique supported numerator representation
   \((p_1,p_3)=(1,1)\). Its coefficient is
   \(\beta_{1,H}^2w_D(q_1)w_D(q_3)\), independently of whether the numerator signs
   are actual, unsigned, residue-randomized, or adversarial. No numerator-only
   sign involution can cancel this block. The accepted W-1 pairs are built from
   exactly these coefficients; cancellation of their full contribution, if
   true, must occur across different denominator pairs or other pair-sum
   representations.
2. **A genuine but narrow actual-sign identity survives.** Without coprimality
   filtering and with the same denominator on the two numerator variables, the
   infinite Vaaler-limit coefficient is the Fourier series of a square wave.
   Its self-convolution is exactly diagonal. The finite Vaaler convolution is
   uniformly \(O(H^{-1/2})\) off the zero Fourier mode. This identity fails for
   unsigned coefficients, but it does not extend coefficientwise to unequal
   denominators and is generally broken by the generic-sector coprimality
   restriction.

Thus the viable successor is not a termwise residue pairing. It would have to
be an averaged, coprimality-aware **dilated square-wave correlation theorem**
across denominator pairs and the critical kernel. No such theorem is proved
here.

## 2. Exact generic-band algebra

For \(D\le q<2D\), the only lift is \(g=1\). With \(P=|p|\), the supported
reduced fractions satisfy

\[
 (p,q)=1,\qquad 1\le P\le H,\qquad 2\nmid p,
\]

and

\[
 A_\chi(p/q)=\beta_{p,H}w_D(q),
 \qquad
 \beta_{p,H}
 =-\frac{\Phi(P/(H+1))\chi_4(P)}{\pi P}.
 \tag{2.1}
\]

Equivalently, for signed odd \(p\),

\[
 \beta_{p,H}
 =-\frac{\Phi(|p|/(H+1))}{\pi}\frac{\chi_4(p)}p.
 \tag{2.2}
\]

The quotient \(\chi_4(p)/p\) is even, so
\(\beta_{-p,H}=\beta_{p,H}\). Pairing \(p\) with \(-p\) therefore produces a
cosine; it does not cancel.

For fixed ordered denominators \(q_1,q_3\), define the numerator-line
coefficient

\[
 C_{q_1,q_3,H}(n)
 :=w_D(q_1)w_D(q_3)
 \sum_{\substack{p_1q_3+p_3q_1=n\\
                  |p_i|\le H,\ 2\nmid p_i\\
                  (p_i,q_i)=1}}
 \beta_{p_1,H}\beta_{p_3,H}.
 \tag{2.3}
\]

It is the contribution of this fixed denominator pair to the reduced pair sum
\(r=n/(q_1q_3)\). Any claimed numerator cancellation must act inside (2.3), or
must explicitly invoke cancellation between different denominator pairs.

## 3. No-go lemma: a unique unit-numerator block

### Exact statement

Let \(g=(q_1,q_3)\), \(q_1=ga\), and \(q_3=gb\), where \((a,b)=1\). If

\[
 \min(a,b)>H+1,
 \tag{3.1}
\]

then the only supported integer solution of

\[
 p_1q_3+p_3q_1=q_1+q_3
 \tag{3.2}
\]

is \(p_1=p_3=1\). Consequently

\[
 \boxed{
 C_{q_1,q_3,H}(q_1+q_3)
 =\beta_{1,H}^2w_D(q_1)w_D(q_3).}
 \tag{3.3}
\]

For nonnegative denominator weights this is positive and, by the audited unit
frequency bound, has magnitude at least

\[
 \frac{|w_D(q_1)w_D(q_3)|}{4\pi^2}.
\]

### Proof

Dividing (3.2) by \(g\) gives

\[
 bp_1+ap_3=a+b.
\]

All integer solutions are

\[
 p_1=1+at,\qquad p_3=1-bt,\qquad t\in\mathbb Z.
\]

If \(t\ne0\), condition (3.1) forces at least one of
\(|p_1|,|p_3|\) to exceed \(H\). Thus \(t=0\), and \(p_i=1\) are automatically
odd and coprime to \(q_i\). Substitution gives (3.3). \(\square\)

For coprime \(q_1,q_3\asymp D\), condition (3.1) holds throughout the active
range because \(H\asymp DX^{-1/4}\ll D\). The lemma is stronger than a finite
counterexample: it produces an asymptotic family of fixed-denominator pair
coefficients on which all numerator-only sign systems agree.

### Comparison of coefficient systems

Write a residue-randomized even system as

\[
 \widetilde\beta_p=\varepsilon_{|p|}|\beta_p|,
 \qquad \varepsilon_P\in\{\pm1\}.
\]

For the unique block (3.3),

\[
 \widetilde\beta_1^2=|\beta_1|^2
\]

for the actual sign, unsigned sign, every residue randomization, and every
numerator-magnitude adversary. Hence random signs do not even alter this block.
An argument claiming automatic numerator cancellation would prove a false
adversarial analogue.

Two primitive denominator pairs satisfying

\[
 0<\left|
 \frac1{q_1}+\frac1{q_3}
 -\frac1{q_2}-\frac1{q_4}
 \right|\le\frac\kappa X
 \tag{3.4}
\]

therefore contribute the same positive fourfold numerator coefficient
\(\beta_1^4\) under all four sign models when \(w_D\ge0\). This is a positive
subtotal, not a lower bound for the full signed form: other numerator and
denominator representations may cancel it. The exact conclusion is that such
cancellation cannot come from a local residue partner within the fixed
denominator blocks (3.3).

## 4. Why adjacent residue pairings fail at critical resolution

Restrict to positive odd numerators away from the truncation edge. Replacing
\(p\) by \(p+2\) reverses the \(\chi_4\) sign but changes a pair-sum or
pair-difference phase by

\[
 \frac2q\asymp\frac1D,
\]

which is much larger than \(1/X\). A one-coordinate sign reversal therefore
leaves the critical band at every requested scale.

The simplest exact compensation changes the corresponding numerator on the
opposite side by the same \(2\). If the denominators are equal, the phase is
unchanged, but **two** beta signs reverse, so the fourfold coefficient sign is
unchanged. If the denominators \(q,q'\asymp D\) differ, the residual change is

\[
 2\left|\frac1q-\frac1{q'}\right|
 \ge \frac1{2D^2}\qquad(q\ne q'),
 \tag{4.1}
\]

up to the fixed shell constants. This can enter a fixed \(\kappa/X\) band only
near \(D=X^{1/2}\); it still flips two signs and therefore supplies no opposite
coefficient sign. A shift by \(4\) preserves the beta sign from the outset. In all
cases the unequal magnitudes

\[
 \frac{\Phi((p+2)/(H+1))}{p+2}\ne
 \frac{\Phi(p/(H+1))}{p}
\]

also preclude exact termwise cancellation. Coprimality and the endpoints
\(|p|=H\) further destroy the proposed involution.

The scale ledger is

| \(D\) | \(X/D\): one-shift size divided by \(1/X\) | \(X/D^2\): compensated unequal-denominator size divided by \(1/X\) |
|---|---:|---:|
| \(X^{1/3}\) | \(X^{2/3}\) | \(X^{1/3}\) |
| \(X^{3/8}\) | \(X^{5/8}\) | \(X^{1/4}\) |
| \(X^{1/2}\) | \(X^{1/2}\) | \(1\) |

Thus there is no hidden lower-range adjacent-residue pairing; at the endpoint,
the only new local pairs still preserve the coefficient-product sign.

## 5. Surviving actual-sign identity: square-wave self-convolution

The hostile audit does find one real cancellation law, but its scope is much
narrower than the target.

Define the infinite limiting coefficients

\[
 b_h=-\frac{\chi_4(|h|)}{\pi|h|}\mathbf 1_{2\nmid h},
 \qquad h\ne0,
 \qquad b_0=0.
\]

In \(L^2(\mathbb R/\mathbb Z)\),

\[
 f(\theta):=\sum_{h\in\mathbb Z}b_he(h\theta)
 =\psi(\theta+1/4)-\psi(\theta+3/4).
 \tag{5.1}
\]

Away from the two jump classes, \(f(\theta)=\pm1/2\). Hence

\[
 f(\theta)^2=\frac14\quad\text{almost everywhere},
\]

and its Fourier coefficients give the exact convolution identity

\[
 \boxed{
 \sum_{h\in\mathbb Z}b_hb_{n-h}
 =\frac14\mathbf 1_{n=0}.}
 \tag{5.2}
\]

This is collective Fourier cancellation, not a termwise \(1\pmod4\) versus
\(3\pmod4\) involution.

Extend the finite Vaaler coefficient \(\beta_{h,H}\) by zero outside
\(1\le|h|\le H\). Since \(\Phi(0)=1\) and
\(\|\Phi'\|_\infty<\infty\),

\[
 \|\beta_H-b\|_2^2
 \ll
 \sum_{1\le|h|\le H}\frac1{H^2}
 +\sum_{|h|>H}\frac1{h^2}
 \ll \frac1H.
\]

Cauchy--Schwarz applied to each shifted convolution, together with (5.2), now
gives the uniform finite identity

\[
 \boxed{
 \sup_{n\in\mathbb Z}
 \left|
 \sum_h\beta_{h,H}\beta_{n-h,H}
 -\frac14\mathbf 1_{n=0}
 \right|
 \ll H^{-1/2}.}
 \tag{5.3}
\]

For odd \(n\), the left convolution is actually zero by parity. For nonzero
even \(n\), (5.3) is a genuine actual-sign saving. The unsigned analogue fails:
at \(n=2\) its \(h=1\) term alone is
\(|\beta_{1,H}|^2\ge1/(4\pi^2)\), and every unsigned term is nonnegative.

### Why (5.3) does not solve the generic band

Equation (5.3) is the numerator convolution for two identical, unfiltered
denominator dilations. In the generic reduced sector:

- the constraints \((p_i,q_i)=1\) delete numerator terms and generally destroy
  (5.3); the identity remains directly applicable only when the coprimality
  filter is vacuous on \(|p|\le H\), for example for an admissible power-of-two
  denominator;
- unequal denominators lead, before filtering, to Fourier coefficients of
  \(f(q_3\theta)f(q_1\theta)\), not of \(f(\theta)^2\).

For positive unequal integers \(q_1\ne q_3\), the product
\(f(q_3\theta)f(q_1\theta)\) is not constant. Indeed, constancy would force
\(f(q_3\theta)=f(q_1\theta)\) almost everywhere (the sign is fixed near
\(\theta=0\)); their smallest positive Fourier frequencies are respectively
\(q_3\) and \(q_1\), forcing \(q_1=q_3\), a contradiction. Therefore at least
one unequal-denominator numerator-line Fourier coefficient is nonzero. There
is no coefficientwise extension of (5.2) to the generic denominator pairs.

## 6. Numerator-sum capacity check

Even before forming pair sums, \(\chi_4\) gives no power decay. Put

\[
 B_H=\sum_{\substack{1\le p\le H\\p\text{ odd}}}
 \frac{\Phi(p/(H+1))\chi_4(p)}p.
\]

The summands form alternating \(1\pmod4,3\pmod4\) pairs with decreasing
magnitude. Since \(\Phi(1/(H+1))\ge1/2\) and the first negative term has
magnitude at most \(1/3\),

\[
 B_H\ge\frac16
\]

whenever the \(p=3\) term is present; for \(H<3\) the lower bound is easier.
Thus

\[
 \sum_{1\le p\le H,\ p\text{ odd}}\beta_{p,H}
 =-\frac{B_H}{\pi}
\]

has constant, not vanishing, size. In the four control models at zero phase:

- actual signs give order \(1\);
- unsigned coefficients give order \(\log H\);
- independent residue signs have root-mean-square order \(1\), since
  \(\sum p^{-2}\asymp1\);
- an adversary can give order \(\log H\).

So the actual character gains at most logarithmically at this local level. The
power saving required above \(D=X^{1/3}\) must use reciprocal phases and
denominator correlation, not the bare numerator residue sum.

## 7. First doubtful or unproved step

The first unproved step is the only one that could advance the signed fat-band
target: extend the square-wave cancellation from (5.3) to a kernel-weighted
average of

\[
 C_{q_1,q_3,H}(n)
\]

over unequal \(q_1,q_3\asymp D\), with both coprimality filters retained, and
then correlate two such coefficients when their rational pair sums differ by
\(O(1/X)\). The fixed-pair lower block (3.3) shows that no pointwise bound can
simply suppress every \(C_{q_1,q_3,H}\). Any true statement must use averaging
or cancellation across denominator pairs and must explicitly absorb the unit
numerator blocks.

Even success on that global correlation would not prove pointwise M2; the
accepted global-to-pointwise obstruction remains separate.

## 8. Controls and outcomes

No numerical computation was used; every control was resolved algebraically.

| Control | Input | Outcome | Implication |
|---|---|---|---|
| signed-vs-unsigned | convolution (5.3), \(n=2\) | actual is \(O(H^{-1/2})\); unsigned is at least \(1/(4\pi^2)\) | square-wave identity is genuinely sign-sensitive |
| residue-randomized | unique block (3.3) | randomizing \(\beta_1\) leaves \(\beta_1^2\) unchanged | numerator randomness cannot remove W-1 building blocks |
| coefficient-adversary | (3.3) and bare numerator sum | fixed block survives; adversary can align the remaining magnitudes | any successful theorem must use more than the envelope |
| support-and-degeneracy | coprimality, \(p=\pm p\), \(p=H\), \(q_1=q_3\), \(q_1\ne q_3\) | reflection reinforces; coprimality and unequal dilations break (5.3) | exact hypotheses cannot be omitted |
| exact-vs-near | (5.2) versus (3.4) | exact numerator convolution does not estimate near pair sums | no exact-to-near transfer |
| dyadic-endpoints | table in Section 4 | adjacent pairing is excluded below the endpoint and sign-preserving at the endpoint | no hidden endpoint rescue |
| proves-too-much | apply residue-pairing claim to all numerator sign systems | contradicted by (3.3) | reject automatic residue cancellation |

## 9. Dependencies and artifacts used

- sources/vaaler_1985.md: beta normalization, \(\Phi(0)=1\), monotonicity,
  \(C^1\) regularity, and \(|\beta_{1,H}|\ge1/(2\pi)\).
- state/proof_obligations.yml: authoritative generic-band, signed-fat-band,
  B1-capacity, exact/near, and pointwise scope.
- state/control_models.md: signed, unsigned, randomized, adversarial,
  endpoint, and proves-too-much controls.
- rounds/codex-managed/m9-signed-lift-capacity/synthesis.md: exact global
  normalization and the accepted B1-only capacity barrier.

No optional computation artifacts were created.

## 10. Recommended state effect

1. **Record a scoped obstruction:** termwise \(1\pmod4/3\pmod4\) pairing and
   numerator-only sign randomization cannot cancel the generic critical band;
   the unique unit-numerator coefficient (3.3) is the exact countermodel.
2. **Retain (5.3) as a candidate actual-sign lemma:** it is a proved finite
   unfiltered equal-denominator identity, but not yet a generic-band estimate.
3. **Do not promote** M9-M2-signed-fat-band-constant, M9-M2, M9, or the
   theorem target. The next candidate must average the coprime, unequal-dilation
   coefficients (2.3) across denominators and the critical kernel, and must state
   why the positive unit-numerator blocks do not violate it.
