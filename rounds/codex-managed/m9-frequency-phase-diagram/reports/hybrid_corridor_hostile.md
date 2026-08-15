# Hostile audit of the lower/intermediate corridor

## 1. Result

**Verdict.** The two shifts do not cancel.  On odd frequencies they are exactly a
parity projector, and after pairing the two frequency signs the actual Vaaler
block is a twisted sine kernel.  That kernel vanishes at exact product
resonance, but its first annulus

\[
        |X-dr|\asymp D/L
\]

has constant size.  There are examples with actual Vaaler amplitudes and a
bounded, nonnegative denominator weight for which this annulus contributes
\(\gg D/L\).  Thus no improvement of T2S that is uniform over arbitrary
bounded nonnegative weights is possible.  The example has discrete variation
\(\gg D/L\), so it does **not** obstruct a theorem for the actual fixed
scale-normalized BV profile.

A primary-source exponent-pair check does give such a restricted theorem.  If
the denominator profile has uniform discrete BV norm, the Tao--Trudgian--Yang
pair

\[
 (\kappa,\lambda)=\left(\frac{89}{1282},\frac{997}{1282}\right)
\]

gives

\[
 |B_L(D;X)|\ll_\epsilon
 X^{\epsilon+(89(1+\ell)+819\delta)/1282}.
\]

Consequently it reaches the target in the wedge

\[
             178\ell+1638\delta\le 463.                 \tag{EP}
\]

This materially removes a small lower-left part of the phase diagram, but no
part of the checkpoints \(\delta=1/3,3/8,1/2\).  Its transfer to the project is
conditional on verification of the actual denominator profile's normalized
BV norm.

## 2. Exact statement and hypotheses

Write \(e(t)=e^{2\pi i t}\), and let \(v_L\) be a real, nonnegative frequency
cutoff supported on \(L\le h\le 2L\).  For \(h>0\), put

\[
 a_{h,H,L}:=
 \frac{v_L(h)\Phi(h/(H+1))}{2\pi h}.
\]

Thus the audited Vaaler coefficient is
\(\alpha_{h,H}=i\Phi(h/(H+1))/(2\pi h)\) for \(h>0\).
Consider the full two-sided shifted block before the harmless global factor in
\(\mathcal M_2\):

\[
 S_{2,L}:=
 \sum_{d\asymp D}w_D(d)
 \sum_{0<|h|\le H}\alpha_{h,H}v_L(|h|)
 e\!\left(\frac{hX}{4d}\right)
 \left(e(h/4)-e(3h/4)\right).                         \tag{2.1}
\]

For each \(d\), choose an odd integer \(r_d\) nearest to \(X/d\), with a fixed
tie rule, and set

\[
 n_d=dr_d,\qquad \Delta_d=X-n_d.
\]

Then the following identity is exact:

\[
 \boxed{
 S_{2,L}=4\sum_{d\asymp D}w_D(d)\chi_4(r_d)
 \sum_{\substack{h>0\\h\ \mathrm{odd}}}
 a_{h,H,L}\sin\!\left(\frac{\pi h\Delta_d}{2d}\right). }
                                                               \tag{2.2}
\]

The choice of odd representative is immaterial: replacing \(r_d\) by
\(r_d+2\) flips both \(\chi_4(r_d)\) and the sine.  Grouping (2.2) by
\(n=d r_d\) gives the exact localized divisor kernel

\[
 4\sum_n
 \sum_{\substack{d\mid n,\ d\asymp D\\n/d\ \mathrm{odd}\\
                   n/d=r_d}}
 w_D(d)\chi_4(n/d)\,
 K_{L,H}\!\left(\frac{X-n}{d}\right),                 \tag{2.3}
\]

where

\[
 K_{L,H}(t)=\sum_{\substack{h>0\\h\ \mathrm{odd}}}
 a_{h,H,L}\sin(\pi h t/2).
\]

The congruence classes are separated as follows:

\[
 \begin{array}{c|c|c}
 \rho& r=4m-\rho&\chi_4(r)\\ \hline
 1&r\equiv3\pmod4&-1\\
 3&r\equiv1\pmod4&+1.
 \end{array}                                                   \tag{2.4}
\]

They enter (2.3) with opposite character labels, but they are disjoint product
sets, not paired terms.

If the frequency cutoff has uniform scale-normalized BV norm, Vaaler's
\(C^1\) amplitude gives, for \(0<|t|\le1\),

\[
 |K_{L,H}(t)|\ll
 \min\{L|t|,(L|t|)^{-1}\},\qquad K_{L,H}(0)=0.          \tag{2.5}
\]

Thus the exact zero at \(X=n\) does not save a power: summing (2.5) through
the divisor map gives \(X^\epsilon(D/L)\) up to logarithms, with the main
capacity coming from \(|X-n|\asymp D/L\), not \(X=n\).

There is also a sharpness statement.  Suppose \(Y\) is large,
\(1\le L\le H/4\), \(D\le Y^{1/2}\), and \(v_L=1\) on a fixed interior
subinterval of \([L,2L]\).  Then for some \(X\asymp Y\) there is a weight

\[
             0\le w_D(d)\le1,\qquad d\asymp D,
\]

such that

\[
                    |S_{2,L}(D;X)|\gg D/L.              \tag{2.6}
\]

The weight in (2.6) is an indicator of a sparse coherent set.  It is not
claimed to be a fixed smooth profile and has BV norm of order at least the
number of its components.

Finally, under the additional hypothesis

\[
 \sup_d|w_D(d)|+\sum_d|w_D(d+1)-w_D(d)|\ll1,             \tag{2.7}
\]

the exponent-pair conclusion (EP) holds.  A sharp interval or a fixed profile
\(w_D(d)=W(d/D)\) with fixed \(W\in BV\) satisfies (2.7); a merely bounded or
nonnegative weight does not.

## 3. Proof and derivation

### 3.1 The shifts reinforce

Let

\[
 \theta_{d,1}=\frac14\left(\frac Xd+1\right),\qquad
 \theta_{d,3}=\theta_{d,1}+\frac12.
\]

For every integer \(h\),

\[
 e(h\theta_{d,1})-e(h\theta_{d,3})
 =(1-(-1)^h)e(h\theta_{d,1}).                            \tag{3.1}
\]

It is zero for even \(h\) and equals \(2e(h\theta_{d,1})\) for odd \(h\).
Thus the two shifts double, rather than cancel, every surviving frequency.

Pair \(h\) and \(-h\) in (2.1).  If \(r\) is odd and
\(\Delta=X-dr\), then for odd \(h\)

\[
 e\!\left(h\frac{r+1}{4}\right)=-\chi_4(r).
\]

Using \(\alpha_{h,H}=ia_{h,H,L}\) and
\(\alpha_{-h,H}=-ia_{h,H,L}\), the pair is

\[
 4\chi_4(r)a_{h,H,L}
 \sin\!\left(\frac{\pi h\Delta}{2d}\right),
\]

which proves (2.2).  It also exposes an important control: the full two-sided
block vanishes at exact resonance.  A lower bound based only on \(X=dr\)
would be false.

For (2.5), the small-argument bound follows from
\(|\sin u|\le |u|\) and \(a_h\ll1/L\).  Abel summation against the odd
geometric progression gives the reciprocal bound
\((L|t|)^{-1}\).  Grouping by \(n\), using at most \(\tau(n)\ll X^\epsilon\)
eligible divisors, gives

\[
 \frac LD\sum_{|X-n|\le D/L}|X-n|
 +\frac D L\sum_{D/L<|X-n|\ll D}\frac1{|X-n|}
 \ll \frac DL\log(2L),                                  \tag{3.2}
\]

which recovers the T2S power and shows precisely why the central zero is not a
power saving.

### 3.2 A coherent first-annulus family

Take pairs

\[
 d\in[D,2D),\qquad r\equiv3\pmod4,qquad
 dr\in[5Y/4,7Y/4].
\]

There are \(\gg Y\) such pairs: for each \(d\), the allowed \(r\)-interval
has length \(\asymp Y/d\), and \(Y/D\to\infty\) uniformly in the stated
range.  Associate to each pair the interval

\[
 I_{d,r}=\left[dr+\frac{D}{4L},\,dr+\frac{D}{3L}\right].
\]

The integral over \(X\asymp Y\) of the number of covering intervals is
\(\gg YD/L\).  Hence some \(X\asymp Y\) belongs to \(\gg D/L\) of them.
For a fixed \(d\), the products with \(r\equiv3\pmod4\) are spaced by
\(4d\), so these covering pairs have distinct denominators.  Retain whichever
parity class of these denominators is larger.  This loses at most a factor two
and makes the retained integers pairwise nonadjacent.

Let \(w_D\) be the indicator of those denominators.  On its support,

\[
 \frac{D}{4L}\le \Delta_d\le\frac{D}{3L},
 \qquad \chi_4(r_d)=-1.
\]

For \(d\in[D,2D]\) and \(h\in[L,2L]\),

\[
 \frac{\pi}{16}\le
 \frac{\pi h\Delta_d}{2d}
 \le\frac{\pi}{3}.
\]

All sine factors therefore have the same sign and are bounded away from zero.
Because \(L\le H/4\), monotonicity and \(\Phi(1/2)=1/2\) preserve a positive
Vaaler amplitude on the whole block.  Each selected denominator contributes
\(\gg1\), proving (2.6).  The resulting indicator has
\(\sum_d|\Delta w_D(d)|\gg D/L\).  This uses the actual two shifts, both
signs of frequency, and the actual \(\Phi/h\) amplitude.

In exponent coordinates, (2.6) has size \(X^{\delta-\ell}\).  Every genuine
lower block \(\ell<\delta-1/4\) therefore exceeds the target by a power in
this bounded-weight adversary.  This applies at \(D=X^{1/3},X^{3/8},X^{1/2}\)
as well as elsewhere.  It is a no-go for weight-uniform improvement, not for
the fixed normalized-BV project profile.

### 3.3 Hostile check of the new exponent-pair wedge

For

\[
 f_h(d)=\frac{hX}{4d},
\]

one has on \(d\asymp D\)

\[
 |f_h^{(j)}(d)|\asymp \frac{hX}{D}\,D^{-j}.
\]

Also \(hX/D^2\gg1\) in the active range, up to harmless endpoint constants.
The Tao--Trudgian--Yang exponent pair therefore gives, uniformly on
subintervals of the dyadic shell,

\[
 \sum_{d\asymp D}e(f_h(d))
 \ll_\epsilon X^\epsilon
 \left(\frac{hX}{D^2}\right)^\kappa D^\lambda+O(1).      \tag{3.3}
\]

Abel summation transfers (3.3) to (2.7) with no power loss.  This is exactly
where the hypothesis is needed: the coherent weight above has
\(\sum|\Delta w_D|\gg D/L\), so Abel would restore the lost capacity.

The shifts \(e(h\rho/4)\) are constants in \(d\), so (3.3) applies to each
\(\rho\) separately.  Retaining the exact Vaaler amplitude and summing
absolutely over \(h\asymp L\) gives

\[
 \sum_{h\asymp L}\frac{\Phi(h/(H+1))}{h}
 \left(\frac{hX}{D^2}\right)^\kappa D^\lambda
 \ll
 \left(\frac{LX}{D^2}\right)^\kappa D^\lambda.          \tag{3.4}
\]

There is no missing factor \(L\):
\(\sum_{h\asymp L}h^{\kappa-1}\asymp L^\kappa\).
Putting \(D=X^\delta\), \(L=X^\ell\) into (3.4) yields

\[
 \kappa(1+\ell-2\delta)+\lambda\delta
 =\frac{89(1+\ell)+819\delta}{1282}.
\]

Comparison with \(1/4\) is exactly (EP).  Within the actual strip
\(0\le\ell\le\delta-1/4\):

* (EP) covers the entire strip for
  \(1/4\le\delta\le1015/3632=0.279460\ldots\);
* it has a nonempty lower-frequency slice until
  \(\delta=463/1638=0.282662\ldots\);
* it is empty at \(\delta=1/3,3/8,1/2\).

The source is Tao, Trudgian and Yang, *New exponent pairs, zero density
estimates, and zero additive energy estimates: a systematic approach*,
Theorem “New exponent pairs”, arXiv:2501.16779,
<https://arxiv.org/abs/2501.16779>.  The numerical pair is source-supported;
the remaining project seam is the weight transfer, not the exponent algebra.

## 4. First doubtful or unproved step

The exact kernel, the bounded-weight obstruction, and the exponent arithmetic
are proved above.  What is not verified is that every actual project
denominator weight, including endpoint-truncated or merged dyadic blocks,
satisfies (2.7) uniformly.  This is precisely the open
`M9-M2-dyadic-weight-nondegeneracy` infrastructure seam.  Until the profiles
are written explicitly, the exponent-pair wedge is conditional.

No lower bound is proved for one prescribed smooth profile such as
\(W(d/D)\).  The sparse adversarial weight cannot be used to reject a
fixed-profile improvement.

## 5. Required controls and outcomes

1. **Both shifts:** passed.  Equation (3.1) shows exact reinforcement on odd
   frequencies.  The \(\rho=1\) and \(\rho=3\) product classes are recorded
   separately in (2.4).
2. **Both frequency signs:** passed.  Pairing produces the sine kernel and
   catches the exact-resonance zero.  A positive-frequency-only “exact
   resonance lower bound” is rejected.
3. **Actual Vaaler amplitudes:** passed.  The identity and lower bound retain
   \(\Phi(h/(H+1))/(2\pi h)\); no arbitrary frequency phases are inserted.
4. **Signed versus unsigned:** passed.  On the coherent \(r\equiv3\pmod4\)
   family the actual character has one sign, so taking absolute values gives
   the same \(D/L\) scale.  Across both residue classes the character is not a
   termwise pairing.
5. **Coefficient adversary:** passed.  The nonnegative sparse denominator
   weight realizes \(D/L\), while its large BV norm explains exactly why it
   does not contradict the restricted exponent-pair bound.
6. **Proves-too-much:** passed.  Any argument crediting the two shifts with
   cancellation would also cancel the parity-projected model (3.1), which is
   algebraically impossible.
7. **Endpoints:** passed.  The no-go applies at the three requested checkpoint
   values for arbitrary bounded weights.  The exponent-pair wedge applies at
   none of those checkpoints and only near \(D=X^{1/4}\).
8. **Computation:** none used.

## 6. Dependencies and exact artifacts used

* `protocol.md`
* `state/proof_obligations.yml`
* `state/active_campaign.yml`
* `rounds/codex-managed/m9-frequency-phase-diagram/plan.json`
* `rounds/codex-managed/m9-frequency-phase-diagram/briefs/hybrid_corridor_hostile.md`
* `rounds/codex-managed/m9-generic-band-signed-correlation/synthesis.md`
* `rounds/codex-managed/m9-generic-band-signed-correlation/reports/signed_correlation_falsifier.md`
* `state/control_models.md`
* `sources/vaaler_1985.md`
* Tao--Trudgian--Yang, arXiv:2501.16779, Theorem “New exponent pairs”.

## 7. Recommended state effect

* **Promote** the exact parity-projector identity (3.1), the paired sine-kernel
  identity (2.2)--(2.4), and the scoped arbitrary-bounded-weight \(D/L\)
  obstruction (2.6).
* **Reject** any claim that the two shifts or nonnegativity alone improve
  \(D/L\).
* **Retain** the possibility of fixed-profile denominator cancellation; the
  hostile family does not test normalized BV profiles.
* **Promote only under the explicit BV assumption** the exponent-pair wedge
  (EP).  Before attaching it to `M9-M2`, verify all actual dyadic and endpoint
  profiles against (2.7).
* The remaining corridor needs denominator oscillation (or a transformed
  signed theorem), not residue-pairing between the two shifts.
