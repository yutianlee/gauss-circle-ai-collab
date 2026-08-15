# Round 4 synthesis: generic-band signed correlation

## Closing decision

**ACCEPT A NEW POINTWISE TOP-BLOCK LEMMA; ACCEPT TWO EXACT SIGN-STRUCTURE LEMMAS; REJECT AUTOMATIC NUMERATOR-RESIDUE CANCELLATION.**

The round did not prove the full M2 estimate. It did remove the terminal frequency block as an endpoint obstruction and sharply localized what remains.

No numerical experiment was used.

## Pointwise top-frequency theorem

Let \(1\le L\le H\le D\le X^{1/2}\). Let \(u_L\) be supported on a positive frequency interval \(h\asymp L\) and satisfy

\[
\sup_h|u_L(h)|+\sum_h|u_L(h+1)-u_L(h)|\ll L^{-1}.
\]

For either \(\rho=1\) or \(3\), bounded denominator weights satisfy

\[
\boxed{
\left|
\sum_{D\le d<2D}w_D(d)
\sum_hu_L(h)e\!\left(\frac h4\left(\frac Xd+\rho\right)\right)
\right|
\ll_\varepsilon X^\varepsilon\left(1+\frac DL\right).}
\]

The proof first applies Abel summation to the geometric \(h\)-sum, producing

\[
\min\left(1,\frac1{L\|\theta_{d,\rho}\|}\right),
\qquad
\theta_{d,\rho}=\frac14\left(\frac Xd+\rho\right).
\]

Choosing the nearest integer \(m\) gives

\[
n=d(4m-\rho),
\qquad
|X-n|=4d\|\theta_{d,\rho}\|.
\]

Each \(n\) has at most \(\tau(n)\ll_\varepsilon X^\varepsilon\) participating divisors \(d\), and dyadic proximity bins sum to \(X^\varepsilon(1+D/L)\).

For the actual terminal Vaaler block

\[
L\asymp H_D\asymp DX^{-1/4},
\]

the result is

\[
\boxed{S_{2,L}(D;X)\ll_\varepsilon X^{1/4+\varepsilon}}
\]

pointwise and uniformly for \(X^{1/4}\le D\le X^{1/2}\). Endpoint truncation, negative frequencies, real \(X\), and complex bounded denominator weights all pass.

This estimate bounds the two shifts separately. Its numerical bound also holds for unsigned periodic coefficients, though not for arbitrary frequency phases. It is compatible with the absolute fourth-moment obstruction because it concerns one pointwise frequency block, not absolute near-collision mass.

## Exact generic single-lift algebra

For reduced \(p/q\) with \(D\le q<2D\), the lift condition forces \(g=1\), so

\[
A_\chi(p/q)=\beta_{p,H}w_D(q),
\qquad
\beta_{p,H}
=-\frac{\Phi(|p|/(H+1))\chi_4(p)}{\pi p}.
\]

The coefficient is even in signed \(p\), vanishes for even \(p\), and obeys the exact coprimality restriction \((p,q)=1\).

For fixed denominators, the numerator equation

\[
p_1q_2+p_2q_1=N
\]

has a precise character law. Write \(q_1=da\), \(q_2=db\), \((a,b)=1\). Along all odd solutions,

\[
p_1=p_1^{(0)}+2ak,
\qquad
p_2=p_2^{(0)}-2bk,
\]

and

\[
\chi_4(p_1)\chi_4(p_2)
=\chi_4(p_1^{(0)})\chi_4(p_2^{(0)})
(-1)^{k(a+b)}.
\]

Thus the product alternates only when \(v_2(q_1)\ne v_2(q_2)\). When the two \(2\)-adic valuations agree, the entire odd solution fiber is sign-locked. In particular, the all-odd denominator sector has no numerator-character cancellation on a fixed pair-sum fiber.

## Unique unit-numerator obstruction

Let \(q_1=ga\), \(q_3=gb\), \((a,b)=1\), and suppose

\[
\min(a,b)>H+1.
\]

Then the only supported solution of

\[
p_1q_3+p_3q_1=q_1+q_3
\]

is \((p_1,p_3)=(1,1)\). Consequently the fixed-denominator pair coefficient is exactly

\[
\beta_{1,H}^2w_D(q_1)w_D(q_3).
\]

Actual, unsigned, residue-randomized, and envelope-adversarial numerator signs all agree on this block. Therefore cancellation of the W-1 building blocks, if it occurs, must come from other denominator pairs or other pair-sum representations; no numerator-only involution can provide it.

## Square-wave convolution identity

Let

\[
b_h=-\frac{\chi_4(|h|)}{\pi|h|}\mathbf1_{2\nmid h},
\qquad b_0=0.
\]

These are the Fourier coefficients of the \(\pm1/2\) square wave

\[
f(\theta)=\psi(\theta+1/4)-\psi(\theta+3/4).
\]

Since \(f^2=1/4\) almost everywhere,

\[
\boxed{\sum_hb_hb_{n-h}=\frac14\mathbf1_{n=0}.}
\]

For the finite Vaaler coefficients,

\[
\boxed{
\sup_n\left|
\sum_h\beta_{h,H}\beta_{n-h,H}
-\frac14\mathbf1_{n=0}
\right|\ll H^{-1/2}.}
\]

This is a genuine signed identity and fails for unsigned coefficients. Its present scope is equal, unfiltered denominator dilations. Unequal dilations and coprimality filters destroy coefficientwise cancellation, so it does not prove the generic signed fat-band estimate.

## Literature and transform decision

The exact Li--Yang map remains

\[
\mathsf H=L,\qquad \mathsf M=D,\qquad \mathsf T=X/4,
\qquad F_\rho(u)=u^{-1}+\rho D/X.
\]

Their Case A height ceiling misses the project top by \(X^{2/41}\), and Case B also excludes the top. More importantly, their published output is a record-exponent theorem with

\[
\theta^*-1/4=0.0644831759741\ldots,
\]

so height admissibility for smaller blocks would not itself give the conjectural project bound. The source card remains open because of an apparent sign inconsistency in the printed Case A threshold and untranscribed auxiliary conditions.

A formal Poisson transform of the top block has dual lengths

\[
K\asymp XL/D^2,
\qquad LK\asymp X^{1/2},
\]

and would need an \(X^{1/8}\) saving in a square-root product-phase sum. That route is unnecessary for the top block after the elementary theorem, but may still guide analysis of lower blocks.

## Remaining region

The direct theorem gives

\[
S_{2,L}(D;X)\ll_\varepsilon X^\varepsilon(1+D/L).
\]

It reaches \(X^{1/4+\varepsilon}\) only when \(L\gtrsim DX^{-1/4}\), namely the terminal block up to fixed factors. Lower and intermediate frequencies remain open. Ordinary \(d\)-first van der Corput gives \(X^{3/8}\) at the top and misses by \(X^{1/8}\); Li--Yang does not supply the target exponent.

The next campaign should build a rigorous \((D,L)\) phase diagram from all direct estimates, identify the smallest unresolved polygon, and test a hybrid two-shift/divisor or B-process lemma there. The signed-fat-band route remains available, but its equal-valuation sign-lock and unique unit-numerator sectors must be paid for explicitly.

## Evidence ledger

- Blind exact algebra and independent top-lemma audit: reports/blind_generic_band_algebra.md
- Hostile correlation and square-wave audit: reports/signed_correlation_falsifier.md
- Top-block theorem and literature feasibility: reports/top_block_two_shift_attack.md
- Conductor analysis: reviews/conductor_independent_analysis.md

