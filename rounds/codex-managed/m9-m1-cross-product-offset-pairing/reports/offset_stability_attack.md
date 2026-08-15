# Paired-offset stability attack for the exact M1 odd kernel

- Campaign: `m9-m1-cross-product-offset-pairing`
- Round: 12
- Task: `offset_stability_attack`
- Role: analytic correlation attacker
- Status: candidate evidence only; no shared state was edited
- Resource allocation: entirely analytical; no numerical experiment and no
  external theorem import were used

## 1. Result

There is a useful exact reduction, followed by a sharp no-go for the naive
meaning of "offset stability."

Let the exact two-sided frequency block be written with the actual Vaaler
profile as

\[
 \mathcal M_{1,L}(D;X)
 =\sum_d\chi _4(d)w_D(d)\mathcal V_{L,H}(X/d),
 \tag{1.1}
\]

where

\[
 \mathcal V_{L,H}(z)
 =\frac4\pi\sum_{h>0}v_L(h)
   \frac{\Phi(h/(H+1))}{h}\sin(2\pi hz).
 \tag{1.2}
\]

Thus \(\mathcal V\) is periodic and odd.  Choose a nearest half-integer
center

\[
 c\in\tfrac12\mathbb Z,\qquad
 \epsilon=X-c,\qquad |\epsilon|\le\tfrac14.
 \tag{1.3}
\]

Keeping the actual spatial weight and hard endpoint fixed, one may replace
the phase center \(X\) by \(c\) at the target-sized cost

\[
 \boxed{
 \mathcal M_{1,L}(D;X)
 =\sum_d\chi _4(d)w_D(d)\mathcal V_{L,H}(c/d)
   +O_w(L+X^\varepsilon).}
 \tag{1.4}
\]

Since \(L\le H\asymp DX^{-1/4}\le X^{1/4}\), the error in (1.4) is
acceptable.  This removes the generic-real lattice mismatch without
assuming that \(X\) is an integer.

For

\[
 m_c(d)=\left\lfloor c/d+\tfrac12\right\rfloor,
 \qquad n_c(d)=d\,m_c(d),
 \tag{1.5}
\]

and positive offsets \(u\) on the appropriate integer or half-integer
lattice, define the two exact fibers

\[
 \mathcal F_-(u)=\{d:n_c(d)=c-u\},\qquad
 \mathcal F_+(u)=\{d:n_c(d)=c+u\}.
 \tag{1.6}
\]

Oddness then gives the exact centered discrepancy

\[
 \boxed{
 \mathcal M_{1,L}(D;X)
 =\sum_{u>0}\left\{
  \sum_{d\in\mathcal F_-(u)}\chi _4(d)w_D(d)\mathcal V_{L,H}(u/d)
 -\sum_{d\in\mathcal F_+(u)}\chi _4(d)w_D(d)\mathcal V_{L,H}(u/d)
 \right\}
 +O_w(L+X^\varepsilon).}
 \tag{1.7}
\]

Formula (1.7) is a genuine reduction to a symmetric shifted-divisor
correlation.  It preserves the actual odd kernel, both frequency signs,
the character, the fixed profile, the nearest-product convention, and all
center mismatch terms.

The adverse conclusion is exact:

\[
 \boxed{\mathcal F_-(u)\cap\mathcal F_+(u)=\varnothing
 \quad(u>0).}
 \tag{1.8}
\]

Indeed, a common denominator would divide \(2u\), whereas the nearest
product inequalities force \(d>2u\) on the lower fiber.  The strict/open
tie convention is essential and leaves the possible equality in only the
upper fiber.  Hence opposite products possess no common active divisor at
all, not merely too few common divisors.  The small kernel mismatch under
reflection is controllable, but it is vacuous to apply it termwise because
there are no terms to match.

Consequently oddness alone does not save the required factor \(H/L\).  It
turns the problem into the difference of two disjoint truncated divisor
fibers.  At the hard top \(D=X^{1/2}\), \(L=X^\ell\),
\(0<\ell<1/4\), the natural critical mass is

\[
 \Delta=\frac DL=X^{1/2-\ell},
 \qquad
 \frac{\Delta}{X^{1/4}}=\frac HL=X^{1/4-\ell},
 \tag{1.9}
\]

and (1.8) provides none of this power.  A successful continuation must
prove a signed correlation between *different* denominators dividing
\(c-u\) and \(c+u\).  Section 2.4 states the precise annular version.  No
new residual region is closed here.

## 2. Exact statement and hypotheses

### 2.1 Actual block and kernel

Let \(X\ge2\) be real,

\[
 X^{1/4}\le D\le X^{1/2},\qquad
 1\le L\le H=H_D\asymp DX^{-1/4}.
 \tag{2.1}
\]

The sequence \(w_D(d)\) is the fixed real project profile, including its
actual top truncation \(d\le\lfloor\sqrt X\rfloor\).  It is bounded and
supported in a fixed shell \(aD\le d\le bD\).  The function \(v_L\) is the
actual dyadic positive-frequency cutoff, extended by zero outside
\(1\le h\le H\).  Define (1.2) exactly.  The paired Vaaler-frequency
algebra from Round 11 gives (1.1), including the H3 normalization.  In
particular,

\[
 \mathcal V(z+1)=\mathcal V(z),\qquad
 \mathcal V(-z)=-\mathcal V(z),\qquad
 \mathcal V(0)=0.
 \tag{2.2}
\]

The actual cutoff bounds give

\[
 \|\mathcal V\|_\infty\ll1,
 \qquad
 \|\mathcal V'\|_\infty
 \le 8\sum_{h>0}|v_L(h)|\Phi(h/(H+1))
 \ll L,
 \tag{2.3}
\]

and frequency Abel summation plus oddness gives, for \(|z|\le1/2\),

\[
 |\mathcal V(z)|
 \ll \min(L|z|,1,(L|z|)^{-1}).
 \tag{2.4}
\]

The last entry is used only away from zero.

### 2.2 Half-lattice centering lemma

Choose \(c\) and \(\epsilon\) as in (1.3), with either deterministic choice
when there are two nearest points.  Let

\[
 m_X(d)=\left\lfloor X/d+\tfrac12\right\rfloor,
 \qquad
 m_c(d)=\left\lfloor c/d+\tfrac12\right\rfloor.
 \tag{2.5}
\]

Then

\[
 m_X(d)\ne m_c(d)
 \quad\Longrightarrow\quad
 d\mid 2c\quad\hbox{and}\quad (2c/d)\text{ is odd}.
 \tag{2.6}
\]

Thus the number of changed nearest-product assignments is
\(O_\varepsilon(X^\varepsilon)\).  With the spatial sequence held fixed,
(1.4) follows.  This statement does not replace the top block at \(X\) by
a different top block at \(c\); it changes only the phase center.  Hence no
hard-endpoint term is hidden.

### 2.3 Exact paired fibers and their disjointness

If \(c\in\mathbb Z\), let \(u\) run through positive integers.  If
\(c\in\mathbb Z+1/2\), let \(u\) run through positive half-integers.  Then
\(c-u\) and \(c+u\) are integers.  The definitions (1.5)--(1.6) are
equivalent to

\[
 \begin{aligned}
 d\in\mathcal F_-(u)
 &\Longleftrightarrow
 d\mid(c-u),\quad -d/2\le u<d/2,\\
 d\in\mathcal F_+(u)
 &\Longleftrightarrow
 d\mid(c+u),\quad -d/2\le -u<d/2,
 \end{aligned}
 \tag{2.7}
\]

with \(w_D(d)\ne0\) understood.  Therefore a denominator in both fibers
would satisfy \(d\mid2u\), hence \(d\le2u\), while the first line of (2.7)
requires \(d>2u\).  This proves (1.8).  At \(d=2u\), the lower fiber is
excluded and the upper fiber is included, exactly as dictated by the
project's half-integer tie convention.

If \(c\in\mathbb Z\), the central fiber \(n=c\) contributes zero because
its kernel is \(\mathcal V(0)\).  A half-integral \(c\) has no central
integer product.  Pairing the remaining products and using (2.2) proves
(1.7).

### 2.4 Precise shifted-divisor correlation left open

For a dyadic offset annulus \(U<u\le2U\), set

\[
 \lambda_U=min\left(\frac{LU}{D},\ 1,\ \frac{D}{LU}\right)
 \tag{2.8}
\]

and retain the exact normalized symbol

\[
 G_U(u,d)=\lambda_U^{-1}\mathcal V_{L,H}(u/d).
 \tag{2.9}
\]

Fixed shell comparability and (2.4) give \(G_U=O(1)\).  Define

\[
 \begin{aligned}
 \mathscr Q_U(c;D,L)
 =\sum_{U<u\le2U}\Bigg(&
  \sum_{d\in\mathcal F_-(u)}
     \chi _4(d)w_D(d)G_U(u,d)\\
 &-\sum_{d\in\mathcal F_+(u)}
     \chi _4(d)w_D(d)G_U(u,d)\Bigg).
 \end{aligned}
 \tag{2.10}
\]

The exact sufficient correlation estimate is

\[
 \boxed{
 |\mathscr Q_U(c;D,L)|
 \ll_\varepsilon
 X^{1/4+\varepsilon}\lambda_U^{-1}}
 \tag{PSC}
\]

uniformly in all admissible \(c,D,L,U\), with the actual fixed profiles and
the exact fibers (2.7).  Summing \(\lambda_U\mathscr Q_U\) over
\(O(\log X)\) annuli and using (1.4) would prove the M1 block target.

The trivial divisor estimate is

\[
 |\mathscr Q_U|\ll_\varepsilon UX^\varepsilon.
 \tag{2.11}
\]

At the critical annulus \(U=D/L\), (PSC) asks for
\(X^{1/4+\varepsilon}\), while (2.11) is \(D/L\); the exact missing factor
is \(H/L\).  For every outer annulus \(D/L<U\ll D\), multiplication by
\(\lambda_U=D/(LU)\) makes the trivial contribution \(D/L\) again, and
(PSC) again requires the same collective saving.  The outer annuli have
therefore not been discarded.  For very small \(U\), the odd-kernel factor
\(LU/D\) is retained in (2.8).

The key point is that (PSC) is not a norm estimate for either individual
fiber.  It is a signed, pointwise, symmetric shifted-divisor discrepancy
for the two different products \(c-u\) and \(c+u\), with the divisor-
dependent kernel left in place.

## 3. Proof and derivation

### 3.1 Proof of the centering error

Suppose \(m_X(d)\ne m_c(d)\).  The interval between \(c/d\) and \(X/d\)
then contains a half-integer \(j+1/2\).  Hence

\[
 |2c-d(2j+1)|\le2|\epsilon|\le\tfrac12.
 \tag{3.1}
\]

The two quantities inside the absolute value are integers, so they are
equal.  This proves (2.6).  On these exceptional denominators the total
change is

\[
 \ll \tau(2c)\|\mathcal V\|_\infty
 \ll_\varepsilon X^\varepsilon.
 \tag{3.2}
\]

On every other denominator, periodicity and (2.3) give

\[
 \left|
 \mathcal V(X/d)-\mathcal V(c/d)
 \right|
 \le \|\mathcal V'\|_\infty\frac{|\epsilon|}{d}
 \ll \frac LD.
 \tag{3.3}
\]

There are \(O(D)\) denominators in the fixed shell and the spatial weights
are bounded, so their total is \(O(L)\).  Equations (3.2)--(3.3) prove
(1.4).  Notice that the argument is uniform in the fractional part of
\(X\), and the estimate was taken over the whole block rather than only
the central annulus.  This is why every lattice-center mismatch term,
including the outer annuli, is accounted for.

### 3.2 Proof of the exact offset formula

For every participating denominator,

\[
 \mathcal V(c/d)
 =\mathcal V\!\left(\frac{c-n_c(d)}d\right)
 \tag{3.4}
\]

by periodicity.  Group denominators according to the integer
\(n_c(d)\).  Products below \(c\) have residual \(+u\), and products above
\(c\) have residual \(-u\).  Equation (2.2) changes the latter kernel to
\(-\mathcal V(u/d)\).  The central product, if it exists, vanishes.  This
proves (1.7).  The proof of (1.8) following (2.7) shows that no cancellation
has been introduced by silently identifying divisor representations.

For comparison, before absorbing the real-center mismatch, the exact
paired summand is

\[
 \begin{aligned}
 &\sum_{d\in\mathcal F_-(u)}\chi _4(d)w_D(d)
      \mathcal V((u+\epsilon)/d)\\
 &\qquad-
 \sum_{d\in\mathcal F_+(u)}\chi _4(d)w_D(d)
      \mathcal V((u-\epsilon)/d).
 \end{aligned}
 \tag{3.5}
\]

Subtracting (1.7) from (3.5) gives precisely the two Lipschitz errors in
(3.3); there is no omitted reflection term.

### 3.3 Why common-divisor and termwise stability have zero capacity

For integer \(X=c\), the familiar symmetric products are \(X-u\) and
\(X+u\).  Any common divisor divides \(2u\).  But for the same denominator
to represent the nearest product on both sides, both residuals must be in
the half-open interval \([-d/2,d/2)\).  Positive \(u\) forces
simultaneously \(u<d/2\) and \(u\le d/2\), which is impossible for a
divisor of \(2u\).  Thus even at an integer center there is no same-
denominator pairing.  The generic-real reduction does not worsen this
fact; it merely changes \(X\) to a half-lattice center at cost (1.4).

One might instead try to match close but unequal denominators
\(d,d'\).  Writing

\[
 c-u=dm,qquad c+u=d'm'
 \tag{3.6}
\]

requires the bilinear equation

\[
 d'm'-dm=2u.
 \tag{3.7}
\]

If \(d'=d+a\) and \(m'=m+b\), then

\[
 db+ma+ab=2u.
 \tag{3.8}
\]

There is no canonical solution \((a,b)\), no preservation of
\(\chi _4(d)\), and no equality of the actual weights.  Summing (3.8) is
exactly an additive divisor correlation, not a perturbative consequence of
the closeness of the two products.  Formula (PSC), rather than a claimed
bijection, is the honest remaining lemma.

### 3.4 Abel and large-sieve capacity

If the divisor-dependent kernel in (2.10) is erased, a formal cumulative
discrepancy would be

\[
 \begin{aligned}
 E_c(T)=\sum_{0<u\le T}\Bigg(&
 \sum_{d\mid(c-u)}\chi _4(d)w_D(d)
 -\sum_{d\mid(c+u)}\chi _4(d)w_D(d)\Bigg),
 \end{aligned}
 \tag{3.9}
\]

with the nearest-product restrictions understood.  An Abel argument would
need a power-saving bound for the *weighted* version of (3.9), uniformly as
the weight changes with \(u/d\).  Round 11 already shows that freezing this
dependence on a full shell costs the same \(H/L\) factor being sought.
Thus scalar Abel summation in \(u\) does not prove (PSC); it merely moves
the open estimate into a family of discrepancies.

Likewise, Cauchy or a large sieve applied separately to the two sides of
(2.10) sees disjoint supports and their natural density-sized second
moments.  There is no cross term forced by oddness because (1.8) makes the
representation-level covariance empty.  A useful dispersion theorem would
have to exploit the arithmetic relation (3.7) between *different*
denominators.  No such theorem is proved in this report.

### 3.5 Actual versus adversarial spatial weights

The absence of algebraic capacity is sharp for arbitrary bounded weights.
Fix a center \(c\) and write

\[
 r_c(d)=c-n_c(d),\qquad
 \sigma_c(d)=\operatorname{sgn}r_c(d).
 \tag{3.10}
\]

On odd denominators with nonzero residual, the bounded adversarial choice

\[
 w_c^{\rm adv}(d)
 =\chi _4(d)\sigma_c(d)
   \operatorname{sgn}\mathcal V(|r_c(d)|/d)
 \tag{3.11}
\]

makes every centered summand equal to
\(|\mathcal V(|r_c(d)|/d)|\).  Averaging half-lattice centers over a long
interval shows that some center has \(\gg D/L\) denominators in a fixed
interior part of the critical band \(|r_c(d)|\asymp D/L\).  On a coherent
subband of the actual frequency profile, (1.2) is bounded away from zero.
For that center,

\[
 \sum_d\chi _4(d)w_c^{\rm adv}(d)\mathcal V(c/d)
 \gg \frac DL.
 \tag{3.12}
\]

This weight is deliberately nonsmooth, center-dependent, and not the
project profile.  It proves only that oddness, dyadic support, and a generic
norm or large-sieve estimate cannot yield the missing power.  It does not
obstruct cancellation for the fixed actual profile.

## 4. First doubtful or unproved step

The first unproved step is (PSC), or an equivalent estimate for the sum of
its annuli.  The half-lattice reduction (1.4), exact pairing (1.7), and
fiber disjointness (1.8) are elementary identities with all mismatch terms
bounded.  They do not estimate the signed difference between distinct
divisor sets.

In particular, it would be unjustified to infer

\[
 \sum_{d\in\mathcal F_-(u)}\chi _4(d)w_D(d)
 \approx
 \sum_{d\in\mathcal F_+(u)}\chi _4(d)w_D(d)
 \tag{4.1}
\]

from the closeness of \(c-u\) and \(c+u\).  The two fibers are disjoint,
may have different cardinalities, may contain singleton prime-product
representations, and may be sign locked.  A shifted-divisor theorem strong
enough for (PSC), with the exact truncation and pointwise center
uniformity, is the genuine missing input.

## 5. Required controls and outcomes

1. **Integer \(X\): pass.**  Take \(c=X\), so \(\epsilon=0\) and (1.7)
   is exact with no centering error.  Opposite fibers are disjoint, including
   at the half-open nearest-product boundary.

2. **Generic real \(X\): pass.**  Choose the nearest half-lattice center.
   Changed nearest integers occur only for divisors of \(2c\) with odd
   quotient, and all remaining phase mismatches total \(O(L)\).  Hence
   nonintegral centers cost at most \(O(L+X^\varepsilon)\), uniformly in the
   fractional part.

3. **Primes and singleton products: negative stability control.**  A prime
   product can have no divisor in an active interior shell, while a
   semiprime can have a unique in-shell divisor.  Reflection about \(c\)
   imposes no corresponding factorization on the opposite product.  Thus
   occupancy and singleton fibers are not stable under \(n\mapsto2c-n\).

4. **Sign-locked products: negative stability control.**  Products of
   primes \(1\pmod4\), including the Round-11 family \(65^K\), have
   \(\chi _4(d)=+1\) on every odd divisor.  Since the reflected fiber is
   disjoint, character signs do not produce a termwise opposite partner.
   This does not lower-bound the full signed block; it rules out a universal
   fiber identity.

5. **Exact-square endpoint: pass, and separates two mechanisms.**  For
   \(X=y^2\), \(c=X\), so there is no lattice mismatch.  The accepted family
   \(d=y-s\), \(m=y+s\) gives products \(X-s^2\), all on the same side of
   \(X\), and cancellation follows as \(\chi _4(y-s)\) alternates with
   \(s\mapsto s+2\).  Its reflected product \(X+s^2\) cannot use the same
   denominator in the nearest fiber by (1.8); the hard cutoff also excludes
   the tempting denominator \(y+s\).  Therefore the successful endpoint
   control is an ordered-denominator Abel cancellation, not opposite-offset
   divisor stability.

6. **Both signs: pass.**  The argument begins with the exact sine kernel
   (1.2), after pairing the actual positive and negative Vaaler frequencies.
   The minus sign in the upper fiber of (1.7) is precisely Fourier oddness.
   No one-sided complex kernel is substituted.

7. **Actual versus adversarial weights: scoped pass.**  All identities and
   the reduction (PSC) retain the fixed actual profile.  The adversarial
   construction (3.11) is used only to show the capacity limit of arguments
   based on oddness plus norms.  It is not transferred to M1.

8. **Outer annuli: pass as an accounting control, open analytically.**  The
   centering mismatch was bounded over all \(O(D)\) denominators, not only
   the critical window.  Equations (2.8)--(2.10) retain every annulus up to
   the nearest-product boundary.  Each outer annulus has trivial weighted
   size \(D/L\), so it requires the same \(H/L\) saving and remains part of
   (PSC).

9. **Numerical allocation: none.**  No computation was needed; all controls
   are exact or analytic.

## 6. Dependencies and exact artifacts used

The report used exactly the brief-authorized project context:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `state/best_proof_draft.md`;
- `rounds/codex-managed/m9-m1-near-product-character-kernel/synthesis.md`;
- `rounds/codex-managed/m9-m1-near-product-character-kernel/reports/blind_near_product_kernel.md`;
- `rounds/codex-managed/m9-m1-near-product-character-kernel/reports/character_divisor_attack.md`;
- `rounds/codex-managed/m9-m1-near-product-character-kernel/reports/near_product_hostile_audit.md`;
- `rounds/codex-managed/m9-m1-cross-product-offset-pairing/briefs/offset_stability_attack.md`.

No other Round-12 report was read.  Only periodicity, the elementary
period-four character, the divisor bound, the mean value theorem, Abel
summation, and exact finite regrouping were used.  No external source was
imported and no numerical artifact was used.

## 7. Recommended state effect

1. **Promote after independent validation** the half-lattice centering
   lemma (1.4): generic real \(X\) reduces to an integer/half-integer
   reflection lattice with total error \(O(L+X^\varepsilon)\).
2. **Promote after independent validation** the exact paired-offset
   discrepancy (1.7) and the disjoint-fiber lemma (1.8), including the
   half-open tie convention.
3. **Retain as a rigorous no-go** the claim that oddness plus common-divisor
   stability, termwise reflection, scalar Abel summation, or separate
   large-sieve norms can supply the factor \(H/L\).  Opposite nearest-product
   fibers have no common denominator.
4. **Add (PSC) as the precise open shifted-divisor correlation interface**
   if the conductor finds the annular formulation useful.  It preserves all
   actual symbols and every outer annulus.
5. Keep `M9-M1-cross-product-odd-kernel-discrepancy`, `M9-M1`,
   `M9-M1-top-endpoint-signed-cone`, `M9`, and the Gauss-circle target open.

