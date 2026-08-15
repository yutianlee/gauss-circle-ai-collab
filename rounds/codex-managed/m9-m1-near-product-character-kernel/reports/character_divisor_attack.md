# Character-divisor arithmetic attack

- Campaign: `m9-m1-near-product-character-kernel`
- Round: 11
- Task: `character_divisor_attack`
- Role: arithmetic mechanism attacker
- Status: candidate evidence only; no shared state was edited

## 1. Result

There is an exact near-product regrouping which retains the actual Vaaler
kernel, the spatial character, the dyadic profile, and both frequency signs.
It yields one useful exact cancellation: an exact product \(X=dm\) contributes
zero to the two-sided M1 block, because the resulting kernel is a sine kernel.
It does **not**, however, produce a power saving in the coherent window

\[
 |X-dm|\ll \Delta,\qquad \Delta:=D/L.
\]

More precisely, I prove a capacity obstruction.  At every fixed interior
point below the terminal line, including every hard-top middle frequency,
the exact kernel-weighted character-divisor coefficient has, for some
integer \(X\) and also for some \(X\) in any prescribed nonintegral translate
of the integers,

\[
 \ell^1\text{-mass}\gg \frac{D/L}{(\log X)^2},
 \qquad
 \ell^2\text{-mass squared}\gg \frac{D/L}{(\log X)^2}.
 \tag{1.1}
\]

The lower bound already occurs on products \(n=dp\) of two primes congruent
to \(1\pmod 4\), with \(d\) the unique divisor in the actual dyadic support.
Thus the character is \(+1\), complementary-divisor signs reinforce, and
the fixed real profile and exact kernel have not been replaced by arbitrary
weights.  Since

\[
 D/L=X^{\delta-\ell}
     =X^{1/4+(\delta-\ell-1/4)},
\]

this rules out, by a power at every fixed
\(\ell<\delta-1/4\), any proof which takes absolute values after the
near-product grouping, or which seeks the needed saving solely in a smaller
pointwise, \(\ell^1\), or \(\ell^2\) norm of the grouped coefficient.  The
obstruction is strongest exactly where the proposed route was intended to
help: for \(D=X^{1/2}\), \(0<\ell<1/4\), its size is

\[
 \frac{X^{1/2-\ell}}{(\log X)^2}.
\]

The result is a no-go theorem for coefficient-norm, multiplicativity-only,
and post-grouping triangle arguments.  It is not a lower bound for the full
signed M1 sum: cancellation between *different* nearby products \(n\)
remains possible and is the first genuinely open continuation.

## 2. Exact statement and hypotheses

Let \(H=H_D\asymp DX^{-1/4}\), and let \(\eta_L\) be the fixed nonnegative
dyadic frequency cutoff on \(h\asymp L\).  Put

\[
 u_{L,H}(h)=
 \eta_L(h)\frac{\Phi(h/(H+1))}{h},\qquad h>0.
 \tag{2.1}
\]

For a real fixed spatial profile \(w_D\), define the positive-frequency
kernel and the actual paired kernel by

\[
 \mathcal K^+_{L,H}(z)=\sum_{h>0}u_{L,H}(h)e(hz),
 \tag{2.2}
\]

\[
 \mathcal V_{L,H}(z)
 =\frac4\pi\sum_{h>0}u_{L,H}(h)\sin(2\pi hz).
 \tag{2.3}
\]

The exact positive dyadic M1 block, apart from the displayed fixed factor
\(-2i/\pi\), is

\[
 B^+_{1,L}(D;X)
 =\sum_d\chi_4(d)w_D(d)
   \mathcal K^+_{L,H}(X/d),
 \tag{2.4}
\]

whereas the positive and negative frequencies together are exactly

\[
 \mathcal M_{1,L}(D;X)
 =\sum_d\chi_4(d)w_D(d)\mathcal V_{L,H}(X/d).
 \tag{2.5}
\]

Indeed, for \(h>0\),

\[
 -4\alpha_{h,H}=-\frac{2i}{\pi}
 \frac{\Phi(h/(H+1))}{h},
 \qquad
 -4\alpha_{-h,H}=\frac{2i}{\pi}
 \frac{\Phi(h/(H+1))}{h},
\]

and pairing the two exponentials gives (2.3).

Choose the nearest integer deterministically by

\[
 m_X(d)=\left\lfloor X/d+\frac12\right\rfloor,
 \qquad n_X(d)=d\,m_X(d).
 \tag{2.6}
\]

Then the exact regroupings are

\[
 B^+_{1,L}(D;X)
 =\sum_{n\in\mathbb Z}
 \sum_{\substack{d:\ n_X(d)=n}}
 \chi_4(d)w_D(d)
 \mathcal K^+_{L,H}\!\left(\frac{X-n}{d}\right),
 \tag{2.7}
\]

and

\[
 \mathcal M_{1,L}(D;X)
 =\sum_{n\in\mathbb Z} C_{D,L}(n;X),
 \tag{2.8}
\]

where

\[
 C_{D,L}(n;X)=
 \sum_{\substack{d:\ n_X(d)=n}}
 \chi_4(d)w_D(d)
 \mathcal V_{L,H}\!\left(\frac{X-n}{d}\right).
 \tag{2.9}
\]

Equations (2.7)--(2.9), rather than the unweighted abbreviation
\(A_D(n)\), are the authoritative grouped kernels.

For the capacity theorem, take a large reference scale \(Y\),
\(Y^{1/4}\ll D\ll Y^{1/2}\), and \(1\ll L\le u_0H_D\), where
\(u_0>0\) is fixed sufficiently small relative to the upper edge of the
frequency cutoff.  Assume the actual real profile is nonzero on a fixed
closed subinterval \(J_D\asymp D\), so that

\[
 |w_D(d)|\ge w_0>0\quad(d\in J_D),
 \tag{2.10}
\]

and choose \(J_D\) strictly inside the support.  When \(D\asymp\sqrt Y\),
choose it a fixed distance below the hard endpoint \(d\le\lfloor\sqrt
X\rfloor\).  Smoothness and nontriviality of the actual fixed profile give
such an interval.  These choices ensure that, for \(n\in[Y,(1+\sigma)Y]\)
and \(d\in J_D\), a complementary prime \(p=n/d\) lies outside the spatial
support.  Here \(\sigma>0\) is a sufficiently small fixed constant.

Then for every fixed fractional part \(\vartheta\in[0,1)\), and all
sufficiently large \(Y\), there exists

\[
 X\in [Y/2,2Y]\cap(\mathbb Z+\vartheta)
 \]

such that, with \(\Delta=D/L\),

\[
 \sum_{\substack{n:\ c_1\Delta\le X-n\le c_2\Delta}}
 |C_{D,L}(n;X)|
 \gg \frac{\Delta}{(\log Y)^2},
 \tag{2.11}
\]

and

\[
 \sum_{\substack{n:\ c_1\Delta\le X-n\le c_2\Delta}}
 |C_{D,L}(n;X)|^2
 \gg \frac{\Delta}{(\log Y)^2}.
 \tag{2.12}
\]

The constants \(0<c_1<c_2\) depend only on the fixed frequency and spatial
profiles.  The same construction gives the analogues of (2.11)--(2.12)
with \(\mathcal K^+\) in place of \(\mathcal V\).

## 3. Proof and derivation

### 3.1 Exact regrouping and the exact-product zero

For \(m=m_X(d)\), \(n=dm\), and integral \(h\),

\[
 e(hX/d)=e\!\left(h\frac{X-n}{d}\right)e(hm)
          =e\!\left(h\frac{X-n}{d}\right).
\]

This proves (2.7).  Pairing \(h\) and \(-h\) before any absolute value gives
(2.8)--(2.9).  In particular,

\[
 \boxed{\mathcal V_{L,H}(0)=0.}
 \tag{3.1}
\]

Thus \(X=n=dm\), including every exact-square product, contributes zero to
the actual two-sided block.  This cancellation is Fourier oddness, not
divisor-character cancellation.  A one-sided block has instead
\(\mathcal K^+_{L,H}(0)=\sum_hu_{L,H}(h)\asymp1\).

For \(|t|=|X-n|\le d/2\), the elementary sine bound and frequency BV give

\[
 |\mathcal V_{L,H}(t/d)|
 \ll \min\left(\frac{L|t|}{D},\,1,\,
                    \frac{D}{L|t|}\right),
 \tag{3.2}
\]

with the last alternative used away from zero.  Summing the right side over
integer \(t\) still costs

\[
 \frac DL\log(2L).
 \tag{3.3}
\]

Therefore (3.1) removes the exact-resonance point but does not improve the
power (D/L) of the Round-10 divisor estimate.

### 3.2 What multiplicativity actually gives

Let

\[
 A_D(n)=\sum_{d\mid n}\chi_4(d)w_D(d).
 \tag{3.4}
\]

For \(\Re s>1\), its Dirichlet series is exactly

\[
 \sum_{n\ge1}\frac{A_D(n)}{n^s}
 =\zeta(s)P_D(s),
 \qquad
 P_D(s)=\sum_{d\ge1}\frac{\chi_4(d)w_D(d)}{d^s}.
 \tag{3.5}
\]

The truncation \(w_D\) destroys the Euler product of \(P_D\); hence (3.5)
does not make \(A_D\) multiplicative.  Removing the truncation gives instead

\[
 \sum_{d\mid n}\chi_4(d)=\frac{r_2(n)}4\ge0,
 \qquad
 \sum_{n\ge1}\frac{r_2(n)/4}{n^s}=\zeta(s)L(s,\chi_4).
 \tag{3.6}
\]

Thus the full multiplicative completion is nonnegative and has discarded,
rather than exposed, the needed cancellation.

For odd \(n\) and \(d\mid n\), complementary divisors satisfy

\[
 \chi_4(n/d)=\chi_4(n)\chi_4(d).
 \tag{3.7}
\]

If \(n\equiv1\pmod4\), the pair has the same sign and reinforces.  If
\(n\equiv3\pmod4\), the signs are opposite only when both complementary
divisors are actually retained.  The exact weights in (2.9) are

\[
 w_D(d)\mathcal V_{L,H}(t/d),
 \qquad
 w_D(n/d)\mathcal V_{L,H}(td/n),
\]

which are not equal; in a one-sided top shell the complementary divisor is
usually outside the support.  Hence (3.7) supplies no general pairing of the
actual kernel.

### 3.3 Prime-product construction

Restrict \(d\in J_D\) to primes \(d\equiv1\pmod4\).  For each such \(d\),
restrict \(p\) to primes \(p\equiv1\pmod4\) for which

\[
 n=dp\in[Y,(1+\sigma)Y].
 \tag{3.8}
\]

The separation in Section 2 makes \(p\) larger than the upper spatial
cutoff.  Since \(n\) has divisors only \(1,d,p,dp\), \(d\) is its unique
divisor in the support of \(w_D\).  Distinct pairs \((d,p)\) give distinct
\(n\), because the in-support and out-of-support prime factors cannot be
interchanged.

The fixed-modulus prime number theorem in progressions gives

\[
 \#\{d\in J_D:d\text{ prime},\ d\equiv1\pmod4\}
 \gg \frac D{\log D},
\]

and, uniformly for such \(d\),

\[
 \#\left\{p\equiv1\pmod4:
       \frac Yd\le p\le\frac{(1+\sigma)Y}{d}\right\}
 \gg \frac{Y/d}{\log(Y/D)}.
\]

Consequently the set \(\mathcal P_Y\) of unique products (3.8) satisfies

\[
 |\mathcal P_Y|
 \gg \frac{Y}{\log D\,\log(Y/D)}
 \gg \frac{Y}{(\log Y)^2}.
 \tag{3.9}
\]

For an explicit unconditional source sufficient for both counts, Bennett,
Martin, O'Bryant, and Rechnitzer prove, for \(q=4,a=1\) and
\(x\ge 8\cdot10^9\),

\[
 \left|\vartheta(x;4,1)-\frac{x}{2}\right|
 <\frac{x}{160\log x};
\]

see [*Explicit bounds for primes in arithmetic progressions*, arXiv:1802.00085](https://arxiv.org/abs/1802.00085).
Taking differences at the two fixed-ratio endpoints above gives the two
displayed lower bounds.  The source hypotheses are met: the modulus is the
fixed \(q=4\le10^5\), \((a,q)=1\), both endpoints tend to infinity, and the
interval ratios \(J_D\) and \(1+\sigma\) are fixed.

Every \(n\in\mathcal P_Y\) has

\[
 \chi_4(d)=\chi_4(p)=1,
 \qquad
 A_D(n)=w_D(d),
 \tag{3.10}
\]

and all four divisors in the full sum (3.6) have positive character.

### 3.4 The actual kernel is coherent on a subwindow

Because \(L\le u_0H\), the accepted decreasing Vaaler profile has

\[
 \Phi(h/(H+1))\ge c(u_0)>0
\]

through a fixed positive portion of the actual frequency cutoff.  Choose
\(c_2>0\) so small that, whenever

\[
 c_1\Delta\le t\le c_2\Delta,
 \qquad d\in J_D,
\]

all angles \(2\pi ht/d\) on that portion lie in a fixed subinterval of
\((0,\pi/2)\).  Since \(\sin v\gg v\) there,

\[
 \mathcal V_{L,H}(t/d)
 \gg \frac tD\sum_{h\asymp L}\eta_L(h)\Phi(h/(H+1))
 \gg \frac{tL}{D}
 \gg1.
 \tag{3.11}
\]

The same argument with cosine gives

\[
 \Re\mathcal K^+_{L,H}(t/d)\gg1.
 \tag{3.12}
\]

For the unique products in (3.9), (2.10), (3.10), and (3.11) therefore give

\[
 |C_{D,L}(n;X)|\gg1
 \quad\text{if}\quad
 c_1\Delta\le X-n\le c_2\Delta.
 \tag{3.13}
\]

The nearest-product condition in (2.6) is automatic because
\(c_2\Delta=c_2D/L<d/2\).

### 3.5 Averaging only to construct the obstruction

Fix any \(\vartheta\in[0,1)\) and average the *count* of (3.13) over
\(X\in\mathbb Z+\vartheta\) in a fixed interval containing
\([Y,(1+\sigma)Y]\).  Each \(n\in\mathcal P_Y\) occurs for

\[
 \gg\Delta
\]

such centers \(X\), while the number of possible centers is \(O(Y)\).
Double counting and (3.9) show that some center contains

\[
 \gg\frac{\Delta}{(\log Y)^2}
\]

unique products satisfying (3.13).  Summing their absolute values and
squares proves (2.11)--(2.12).  This is an analytical existence argument,
not a numerical average and not a mean-value substitute for the desired
pointwise M1 estimate.

At a fixed exponent point with

\[
 \kappa=\delta-\ell-\frac14>0,
\]

the lower bound is \(Y^{1/4+\kappa}/(\log Y)^2\).  Choosing any
\(\varepsilon<\kappa\) proves the claimed power obstruction to an
absolute-value or coefficient-norm closure at that point.

## 4. First doubtful or unproved step

The first unproved step is a signed short-interval discrepancy estimate for
the exact coefficients (2.9):

\[
 \sum_n C_{D,L}(n;X)
 \quad\text{rather than}\quad
 \sum_n|C_{D,L}(n;X)|.
\]

The prime-product construction proves that neither pointwise smallness nor
small \(\ell^1/\ell^2\) mass is available.  It does not rule out cancellation
between different products \(n\).  Such cancellation would have to use the
ordered dependence on \(X-n\), the oddness of \(\mathcal V\), and correlations
of the actual truncated divisor coefficient across \(n=X-t\) and \(n=X+t\).
Multiplicativity, complementary divisors, the sum-of-two-squares identity,
and a generic short-interval mean square do not by themselves provide that
correlation.

No point of \(\mathcal U_1\) is closed by this report.  The proved advance is
the exact regrouping, the exact-resonance zero, and the rigorous elimination
of the proposed post-grouping coefficient-norm route.

## 5. Required controls and outcomes

1. **\(X\) integer and noninteger: pass.**  Equations (2.6)--(2.9) hold for
   every real \(X\).  The lower-bound double count works on
   \(\mathbb Z+\vartheta\) for every prescribed \(\vartheta\), including
   (0).  The coherent subwindow stays away from nearest-integer ties.

2. **Exact squares: pass, with a crucial distinction.**  If \(X=s^2\), the
   exact product \(n=X\) has \(\mathcal V(0)=0\) in the two-sided block.
   Positive and negative frequencies separately do not vanish.  If (s)
   is made from primes \(1\pmod4\), all divisor characters reinforce, so the
   zero is Fourier oddness and cannot be attributed to \(\chi_4\).  Near but
   nonexact products remain open.

3. **Prime and highly composite products: pass.**  The obstruction uses
   semiprimes \(dp\) with \(d,p\equiv1\pmod4\), giving a unique in-shell
   divisor.  For a product of arbitrarily many primes \(1\pmod4\), every
   divisor has character \(+1\), and (3.6) gives
   \(r_2(n)/4=\tau(n)\); multiplicativity reinforces rather than cancels.

4. **Dyadic truncation: pass.**  Formula (3.5) records exactly why truncation
   destroys multiplicativity.  In the lower-bound family, \(d\) is inside a
   nonvanishing interval of the actual profile and \(p\) is outside the full
   spatial support, so there is exactly one retained divisor.  No sharp
   \(w_D=1\) replacement is made.

5. **Real fixed profile versus arbitrary bounded weights: scoped pass.**
   The norm obstruction applies to every nonzero fixed real profile having a
   nonvanishing interior interval, including the actual smooth profile.  It
   is not a lower bound for the total signed sum because other products can
   cancel the displayed subtotal.  With arbitrary bounded weights one can
   additionally align or isolate coefficient signs, so an arbitrary-weight
   theorem in the residual corridor would prove too much.  Any positive
   continuation must use correlations specific to the fixed profile.

6. **Both frequency signs: pass.**  The one-sided kernel is (2.2); the exact
   paired kernel is the sine kernel (2.3).  The no-go lower bound holds for
   both formulations on a one-sided coherent \(t\)-subwindow.  The exact
   product zero occurs only after the actual (h,-h) pairing.

7. **Short-interval mean square and large sieve: negative control.**
   Equation (2.12) shows that the exact coefficient vector has its natural
   density-sized second moment.  A Cauchy or large-sieve step using only this
   norm and the number of coherent \(n\)'s cannot recover the missing power.
   This does not exclude an operator estimate which retains signed
   correlations between different \(n\).

8. **Numerical use: none.**  The report is entirely analytical.

## 6. Dependencies, exact artifacts, and source used

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `state/best_proof_draft.md`
- `rounds/codex-managed/m9-m1-near-product-character-kernel/briefs/character_divisor_attack.md`
- `rounds/codex-managed/m9-m1-frequency-phase-diagram/synthesis.md`
- `rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/m1_terminal_arithmetic_attack.md`
- `sources/method_strategy_review_2026-08-11.md`
- Bennett, Martin, O'Bryant, and Rechnitzer,
  [*Explicit bounds for primes in arithmetic progressions*](https://arxiv.org/abs/1802.00085),
  specifically the unconditional fixed-modulus estimate
  \( |\vartheta(x;4,1)-x/2|<x/(160\log x) \) for \(x\ge8\cdot10^9\).

No Round-11 report was read.  No numerical artifact was used.

## 7. Recommended state effect

1. **Promote after independent validation** the exact near-product
   regrouping (2.7)--(2.9) and the exact two-sided resonance-zero lemma
   \(\mathcal V_{L,H}(0)=0\).
2. **Retain as a rigorous no-go obstruction** that post-grouping triangle,
   coefficientwise, \(\ell^1\), \(\ell^2\), multiplicativity-only, and
   complementary-divisor-only arguments cannot close any fixed interior
   point below the terminal line.  If the project requires a source card
   even for this obstruction, audit the cited fixed-\(q=4\) prime-counting
   estimate before graph promotion.
3. Replace the current proposed kernel, if the conductor agrees, by the
   narrower signed task: control the odd-kernel short-interval discrepancy
   between different products \(n\), retaining (2.9) until the final
   summation.  Do not target a smaller norm of \(A_D(n)\).
4. Keep `M9-M1`, `M9-M1-top-endpoint-signed-cone`, `M9`, and the
   Gauss-circle target open.
