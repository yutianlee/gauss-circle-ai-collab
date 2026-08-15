# Blind near-product character-kernel derivation

- Campaign: `m9-m1-near-product-character-kernel`
- Round: 11
- Task: `blind_near_product_kernel`
- Role: statement-only exact deriver
- Isolation: no Round-10 report and no other Round-11 report was read
- Status: candidate evidence only; no shared proof state was edited

## 1. Result

The positive-frequency M1 block has an exact regrouping as a short-product
character-divisor sum.  No absolute value is taken in the frequency
variable.  If

\[
 \mathcal K_{H,L}(t)
 =\sum_{h=1}^{H}v_L(h)
   \frac{\Phi(h/(H+1))}{h}e(ht)
\]

is the full Vaaler/dyadic frequency kernel, then the exact block is

\[
 \boxed{
 \mathcal M_{1,L}^{+}(D;X)
 =\frac{2}{\pi i}
 \sum_{n\geq1}
 \sum_{\substack{d\mid n,\ w_D(d)\neq0\\
                  -d/2\leq X-n<d/2}}
 \chi _4(d)w_D(d)
 \mathcal K_{H,L}\!\left(\frac{X-n}{d}\right). }
 \tag{1.1}
\]

Here the half-integer tie is assigned to the larger nearest integer.  Thus
the left inequality in (1.1) is closed and the right inequality is open.
The identity includes the hard top denominator \(d=\lfloor\sqrt X\rfloor\)
and every frequency cutoff endpoint without an additional boundary term.

If \(X\) is an integer, the exact-product fiber \(n=X\) is

\[
 \frac{2}{\pi i}\mathcal K_{H,L}(0)
 \sum_{\substack{d\mid X\\w_D(d)\neq0}}
 \chi _4(d)w_D(d),
 \tag{1.2}
\]

and is \(O_\varepsilon(X^\varepsilon)\).  The chosen half-integer tie fiber
is also \(O_\varepsilon(X^\varepsilon)\).  Hence neither exact products nor
ties are the residual obstruction.

The weakest exact new estimate is the actual-kernel weighted
character-divisor bound obtained by placing an absolute value outside the
whole right side of (1.1), after removing (1.2).  A useful annular version
is stated in Section 2.4.  In the Round-10 residual corridor it must save a
factor

\[
 \boxed{\frac{H}{L}=\frac{D}{LX^{1/4}}>1}
 \tag{1.3}
\]

over the natural divisor-count bound on the critical proximity annuli.

There is a rigorous obstruction to replacing the kernel in (1.1) by an
\(n\)-only function on the full dyadic \(d\)-shell.  On the critical window
\(|X-n|\asymp D/L\), changing \(d\) by a fixed proportion of \(D\) changes
the kernel argument by order \(1/L\), while
\(\|\mathcal K'_{H,L}\|_\infty\ll L\).  The first Taylor error is
therefore only \(O(1)\) per divisor representation.  Freezing becomes a
controlled operation only after a short subdivision in \(d\), and the
number of required subdivisions consumes the same saving that the desired
estimate needs.  Thus regrouping is exact and useful, but a whole-shell
freezing step supplies no proof of M1.

## 2. Exact statement and hypotheses

### 2.1 Block conventions

Let \(X\geq2\) be real, put

\[
 y=\lfloor\sqrt X\rfloor,
 \qquad
 H=H_D=\lfloor DX^{-1/4}\rfloor,
\]

and let \(w_D\) be one active denominator weight from the accepted exact
partition.  Thus \(w_D\) is supported on positive integers in a fixed
shell \(aD\leq d\leq bD\), is already truncated by \(d\leq y\) in the top
block, and has uniformly bounded discrete BV norm.  No continuum
smoothness is required for (1.1).

Let \(v_L(h)\) be the actual positive-frequency dyadic cutoff, extended by
zero outside \(1\leq h\leq H\).  The derivation does not require a
particular choice at \(h=L,2L,H\): whatever inclusions the project cutoff
uses are retained exactly in \(v_L\).  Define

\[
 a_{H,L}(h)
 =v_L(h)\frac{\Phi(h/(H+1))}{h},
 \qquad
 \mathcal K_{H,L}(t)=\sum_{h=1}^{H}a_{H,L}(h)e(ht).
 \tag{2.1}
\]

The actual positive-frequency M1 block, including its H3 factor, is

\[
 \mathcal M_{1,L}^{+}(D;X)
 =-4\sum_{h=1}^{H}v_L(h)\alpha_{h,H}
   \sum_{d\geq1}\chi _4(d)w_D(d)e(hX/d),
 \tag{2.2}
\]

where

\[
 \alpha_{h,H}=-\frac{\Phi(h/(H+1))}{2\pi i h}.
 \tag{2.3}
\]

Consequently (2.2) is exactly

\[
 \mathcal M_{1,L}^{+}(D;X)
 =\frac{2}{\pi i}\sum_{d\geq1}
   \chi _4(d)w_D(d)\mathcal K_{H,L}(X/d).
 \tag{2.4}
\]

For real \(w_D,v_L\), the negative-frequency block is the complex
conjugate of (2.2), so the corresponding two-sided block is twice its real
part.  No such pairing is used in deriving (1.1).

### 2.2 Nearest-integer and product conventions

For every participating \(d\), define

\[
 m_d=\left\lfloor\frac Xd+\frac12\right\rfloor,
 \qquad
 \theta_d=\frac Xd-m_d\in[-1/2,1/2),
 \qquad
 n_d=dm_d.
 \tag{2.5}
\]

Thus a tie \(X/d=k+1/2\) is assigned to \(m_d=k+1\), and then
\(\theta_d=-1/2\).  Since \(hm_d\in\mathbb Z\),

\[
 e(hX/d)=e(h\theta_d),
 \qquad
 \theta_d=\frac{X-n_d}{d}.
 \tag{2.6}
\]

For fixed integers \(n,d\) with \(d>0\), the equality \(n=n_d\) is
equivalent to

\[
 d\mid n,
 \qquad
 -\frac d2\leq X-n<\frac d2.
 \tag{2.7}
\]

This proves the exact equivalence between (2.4) and (1.1).  In particular,
if \(w_D(d)\neq0\), then

\[
 |X-n|\leq \frac{bD}{2},
 \tag{2.8}
\]

so (1.1) is supported on an interval of \(O(D)\) integer products around
\(X\).

### 2.3 Exact products and ties

The fiber \(n=X\) exists only when \(X\in\mathbb Z\), and (2.7) then says
exactly \(d\mid X\).  This gives (1.2).  Since

\[
 |\mathcal K_{H,L}(0)|
 \leq\sum_{h\asymp L}\frac1h\ll1
\]

and the number of participating \(d\)'s is at most \(\tau(X)\), (1.2) is
\(O_\varepsilon(X^\varepsilon)\).

At the included tie boundary \(X-n=-d/2\), one has

\[
 2X=d(2m_d-1).
\]

Therefore ties do not occur unless \(2X\in\mathbb Z\).  If they do occur,
the tie contribution is exactly

\[
 \frac{2}{\pi i}\mathcal K_{H,L}(-1/2)
 \sum_{\substack{d\mid 2X,\ w_D(d)\neq0\\
                  (2X/d)\ \mathrm{odd}}}
 \chi _4(d)w_D(d),
 \tag{2.9}
\]

where divisibility is interpreted in the integer \(2X\).  It is again
\(O_\varepsilon(X^\varepsilon)\).  The alternative boundary
\(X-n=d/2\) is excluded by the stated tie convention.

### 2.4 The exact and annular character-divisor targets

Define

\[
 \mathfrak D_{D,L}(X)
 =\sum_{\substack{n\geq1\\n\neq X}}
 \sum_{\substack{d\mid n,\ w_D(d)\neq0\\
                  -d/2\leq X-n<d/2}}
 \chi _4(d)w_D(d)
 \mathcal K_{H,L}\!\left(\frac{X-n}{d}\right).
 \tag{2.10}
\]

The logically weakest new lemma is

\[
 \boxed{
 |\mathfrak D_{D,L}(X)|
 \ll_\varepsilon X^{1/4+\varepsilon}}
 \tag{WK}
\]

for the one actual kernel (2.1), uniformly on the residual corridor.  It
is necessary and sufficient for the positive block, up to the harmless
exact-product contribution.  It is important that the absolute value in
(WK) is outside both the \(n\)- and \(d\)-sums.

For a more local sufficient formulation, first use the standard
frequency-BV consequence

\[
 |\mathcal K_{H,L}(t)|
 \ll \min\left(1,\frac1{L\|t\|}\right).
 \tag{2.11}
\]

For dyadic \(1\leq R\ll D\), put

\[
 \lambda_R=\min\left(1,\frac{D}{LR}\right)
 \tag{2.12}
\]

and, on the annulus \(R<|X-n|\leq2R\), retain the exact normalized symbol

\[
 G_R(n,d)
 =\lambda_R^{-1}
  \mathcal K_{H,L}\!\left(\frac{X-n}{d}\right).
 \tag{2.13}
\]

Fixed-shell comparability makes \(G_R=O(1)\).  Define

\[
 \mathfrak C_R
 =\sum_{\substack{R<|X-n|\leq2R}}
  \sum_{\substack{d\mid n,\ w_D(d)\neq0\\
                   -d/2\leq X-n<d/2}}
  \chi _4(d)w_D(d)G_R(n,d).
 \tag{2.14}
\]

The outside-absolute estimate

\[
 \left|\sum_R\lambda_R\mathfrak C_R\right|
 \ll_\varepsilon X^{1/4+\varepsilon}
 \tag{2.15}
\]

is simply (WK), up to \(O(\log X)\) choices at annular endpoints.  A
stronger but robust sufficient short-interval statement is

\[
 \boxed{
 |\mathfrak C_R|
 \ll_\varepsilon
 X^{1/4+\varepsilon}
 \max\left(1,\frac{LR}{D}\right)
 \quad(1\leq R\ll D).}
 \tag{CD}
\]

Indeed, multiplying (CD) by (2.12) makes every annular contribution
\(O_\varepsilon(X^{1/4+\varepsilon})\), and the logarithmic number of
annuli is absorbed into \(X^\varepsilon\).

The trivial divisor bound gives \(\mathfrak C_R\ll_\varepsilon
RX^\varepsilon\).  Put \(H=DX^{-1/4}+O(1)\).  At the critical scale
\(R=D/L\), (CD) asks for \(X^{1/4+\varepsilon}\), whereas the trivial bound
is \(D/L=X^{1/4}H/L\).  For every larger annulus, (CD) asks for

\[
 X^{1/4}\frac{LR}{D}=\frac{LR}{H},
\]

again a factor \(H/L\) below the trivial size \(R\).  Thus (1.3) is the
precise cancellation demanded throughout the outer critical annuli.  In
the residual corridor \(L<H\), so this is a genuine saving.  Near the
terminal line the saving tends to \(1\), consistently with the accepted
terminal estimate.

## 3. Proof and derivation

### 3.1 Proof of the exact regrouping

Substituting (2.3) into (2.2) gives (2.4).  For each \(d\), (2.5) and
(2.6) give

\[
 \mathcal K_{H,L}(X/d)
 =\mathcal K_{H,L}\!\left(\frac{X-dm_d}{d}\right).
\]

The map \(d\mapsto n_d=dm_d\) need not be injective, but grouping equal
values is an exact finite rearrangement.  Condition (2.7) lists precisely
the preimages of a fixed \(n\), including the chosen tie and excluding the
unchosen tie.  This proves (1.1).  No estimate, completion, Poisson formula,
or continuum approximation has entered.

### 3.2 Kernel size and the near-product scales

On a dyadic frequency block, \(a_{H,L}(h)=O(1/L)\) and has total discrete
variation \(O(1/L)\).  Abel summation against the finite geometric sum
therefore gives (2.11).  Since the nearest-integer convention places
\((X-n)/d\) in \([-1/2,1/2)\), and \(d\asymp D\), an annulus
\(|X-n|\asymp R\) has kernel size at most (2.12).

There are \(O(R)\) possible integers \(n\) on such an annulus, and each has
at most \(\tau(n)\ll_\varepsilon X^\varepsilon\) participating divisors.
Thus the unsigned contribution of one annulus is

\[
 \ll_\varepsilon
 R\min\left(1,\frac{D}{LR}\right)X^\varepsilon
 \leq \frac DL X^\varepsilon.
 \tag{3.1}
\]

This recovers the natural \(D/L\) scale without taking an absolute value
inside the original \(h\)-sum.  It also shows why the phrase “the window
has length \(D/L\)” must be interpreted carefully: with only the accepted
first-BV kernel bound, there are logarithmically many outer annuli, each
capable of contributing at the same \(D/L\) scale.  The full dependence on
\((X-n)/d\) in (1.1) is therefore not optional.

### 3.3 Exact first freezing error

Let \(d_0\asymp D\).  For
\(\Delta_n=X-n\), the fundamental theorem of calculus gives the exact
identity

\[
 \begin{aligned}
 \mathcal K_{H,L}(\Delta_n/d)
 -\mathcal K_{H,L}(\Delta_n/d_0)
 ={}&\Delta_n\left(\frac1d-\frac1{d_0}\right)\\
 &\times\int_0^1
 \mathcal K'_{H,L}\!\left(
 \Delta_n\left(\frac{1-s}{d_0}+\frac{s}{d}\right)
 \right)ds.
 \end{aligned}
 \tag{3.2}
\]

This is the first error in any attempted \(n\)-only freezing.  Since

\[
 \|\mathcal K'_{H,L}\|_\infty
 \leq2\pi\sum_{h\asymp L}|v_L(h)|\Phi(h/(H+1))
 \ll L,
 \tag{3.3}
\]

if \(d,d_0\) lie in a denominator interval of length \(V\), then

\[
 \left|
 \mathcal K_{H,L}(\Delta_n/d)
 -\mathcal K_{H,L}(\Delta_n/d_0)
 \right|
 \ll \frac{L|\Delta_n|V}{D^2}.
 \tag{3.4}
\]

On the central window \(|\Delta_n|\ll D/L\), this is

\[
 \boxed{O(V/D)}
 \tag{3.5}
\]

per divisor representation.  Consequently the absolute central-window
freezing error is

\[
 \ll_\varepsilon
 \frac VD\left(1+\frac DL\right)X^\varepsilon
 \ll_\varepsilon \left(\frac VL+\frac VD\right)X^\varepsilon.
 \tag{3.6}
\]

For the whole dyadic shell \(V\asymp D\), (3.5) is \(O(1)\), not \(o(1)\).
Thus the replacement

\[
 \mathcal K_{H,L}((X-n)/d)
 \rightsquigarrow
 \mathcal K_{H,L}((X-n)/D)
 \tag{3.7}
\]

is not justified on the critical window.  It is exact when \(n=X\), and
it has error \(O(\eta)\) only on the ultranear window
\(|X-n|\leq\eta D/L\).

To make (3.6) target-sized by absolute values, one would need

\[
 V\ll LX^{1/4}.
 \tag{3.8}
\]

Inside the residual corridor \(L<H\), (3.8) forces at least

\[
 \frac DV\gg\frac{H}{L}
 \tag{3.9}
\]

denominator cells.  The number of cells is exactly the saving factor in
(1.3).  Estimating the cells separately therefore gives no automatic
advance.  Moreover, (3.6) controls only the central window.  With merely
the accepted first-BV kernel information, the outer annuli in (3.1) must
still be retained.  If one additionally chooses an all-orders smooth
frequency partition, its stronger derivative decay can control their
summed freezing error, but that is an extra regularity input and still
requires the \(H/L\) collective saving.  It cannot validate the full-shell
replacement (3.7).

### 3.4 Why pointwise divisor cancellation is not available

The character must not be discarded, but it also does not guarantee
cancellation inside every single \(n\)-fiber.  If all odd prime factors of
\(n\) are \(1\pmod4\), then

\[
 \chi _4(d)=1
\]

for every odd divisor \(d\mid n\).  With the accepted nonnegative spatial
profile, every participating term in the unweighted localized divisor
coefficient then has the same sign.  Thus no uniform per-\(n\) power saving
can follow from \(\chi_4\) alone.  The required saving in (WK) or (CD) must
come from cancellation across nearby products \(n\), from the exact
\((X-n)/d\) kernel, or from a theorem coupling both.  This observation does
not obstruct (WK); it rules out a simpler fiberwise proof.

## 4. First doubtful or unproved step

There is no doubtful step in the finite regrouping, the exact-product and
tie formulas, or the Taylor identity (3.2).  The first unproved step is
precisely (WK), or the stronger annular statement (CD).  Existing divisor
multiplicity gives only (3.1), of size \(D/L\), and loses the factor
\(H/L\) required in the residual corridor.

It would also be unproved to replace the actual \(d\)-dependent kernel by
an \(n\)-only kernel on a full dyadic shell.  Formula (3.2) shows the first
error explicitly, and (3.5) shows that it is order one on the critical
window.  Any argument beginning with (3.7) must either subdivide the
denominator shell and retain collective cancellation across the cells, or
prove a separate estimate for the Taylor-error character-divisor sum.

## 5. Required controls and outcomes

### Exact-product control: pass

For \(X\in\mathbb Z\), every \(d\mid X\) in the active profile appears once
at \(n=X\), with kernel value \(\mathcal K_{H,L}(0)\).  No neighboring
nearest integer duplicates it.  Its total size is
\(O_\varepsilon(X^\varepsilon)\).

### Half-integer tie control: pass

The convention \(m=\lfloor X/d+1/2\rfloor\) gives
\(-d/2\leq X-n<d/2\).  Formula (2.9) lists the included ties exactly; the
opposite half is excluded.  The entire tie fiber is divisor-bounded.

### Hard top endpoint control: pass

The finite sum uses the actual sequence \(w_D(d)\), including
\(d=y=\lfloor\sqrt X\rfloor\) when the top profile is active.  Regrouping a
finite sum creates no Poisson half-weight, principal-value term, or
continuum endpoint error.  Those phenomena belong to a transform, not to
(1.1).

### Frequency-boundary control: pass

All choices at \(h=L,2L,H\) are encoded in \(v_L\).  No endpoint is dropped
when defining \(\mathcal K_{H,L}\).  The coefficient in front of (1.1) is
the exact value \(-4\alpha_{h,H}=2\Phi(h/(H+1))/(\pi i h)\).

### Unsigned/fiberwise control: fail as intended

Integers with all odd prime factors \(1\pmod4\) have no divisor-character
alternation.  Hence a proposed proof that bounds every \(n\)-fiber by
character cancellation is false.  The target keeps the absolute value
outside the coupled \(n,d\)-sum.

### Whole-shell freezing control: fail as intended

At \(|X-n|\asymp D/L\) and \(|d-d_0|\asymp D\), (3.4) gives an order-one
first error.  Only exact products, an ultranear subwindow, or genuinely
short denominator cells permit freezing.  No numerical experiment was
used.

## 6. Dependencies and exact artifacts used

Only the brief-authorized files were used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `state/best_proof_draft.md`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`;
- `rounds/codex-managed/m9-m1-near-product-character-kernel/briefs/blind_near_product_kernel.md`.

No Round-10 report, no other Round-11 report, no validation matrix, and no
unlisted source was read.  No external theorem was imported and no
numerical experiment was performed.

## 7. Recommended state effect

1. **Promote the exact reduction after independent review.**  Record (1.1)
   as an exact M1 frequency-first near-product character-kernel identity,
   with the stated tie convention and actual Vaaler/dyadic kernel.
2. **Record exact products and ties as harmless.**  Both are
   \(O_\varepsilon(X^\varepsilon)\) and are not M1 blockers.
3. **Add the actual-kernel short-product estimate (WK) as the smallest open
   arithmetic lemma.**  The annular form (CD) is a stronger, reviewable
   sufficient version and makes the required \(H/L\) saving explicit.
4. **Reject whole-shell \(n\)-only freezing.**  Formula (3.2) and the
   order-one critical-window error (3.5) are a rigorous capacity
   obstruction.  A frozen coefficient
   \(\sum_{d\mid n}\chi_4(d)w_D(d)\) is not an exact replacement.
5. **Retain `M9-M1`, `M9-M1-top-endpoint-signed-cone`, and `M9` as open.**
   This report supplies an exact reduction and a no-go statement, not the
   missing \(H/L\) cancellation theorem.
