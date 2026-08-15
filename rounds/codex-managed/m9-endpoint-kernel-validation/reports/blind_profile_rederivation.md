# Statement-only blind profile rederivation

- Campaign: `m9-endpoint-kernel-validation`
- Round: `7` (`seam_validation`)
- Task: `blind_profile_rederivation`
- Role: statement-only blind rederiver
- Graph SHA-256 supplied in the brief: `90f44e99047eff10b620228e8480a88984f9dbbca4445bb8921667d9d3575031`
- Isolation: the Round-6 claimant report was not read.
- Status: candidate evidence only; no shared proof state was edited.

## 1. Result

The requested profile exists with the constants as stated. In fact the
discrete BV constant can be taken to be \(3\) for every active band and \(2\)
for the bottom remainder. One explicit construction gives an exact
partition of \(\mathbf 1_{1\le d\le y}\), sampled mass at least \(D/8\) on
every active band for all sufficiently large \(X\), the desired floor
rounding, and only one upper-endpoint jump.

This construction supplies all denominator-profile hypotheses needed by
the accepted B1, W-1, and Tao--Trudgian--Yang (TTY) interfaces. It also
supplies the partition, support, boundedness, nonnegativity, and height
rounding inputs used before applying the accepted Fejer residual estimate.
It supplies the accepted smooth-Poisson hypothesis only for the interior
active bands. The top band has a genuine jump at \(d=y\); discrete BV does
not make that band a \(C_c^\infty\) rescaling. Thus exactly one smooth-
Poisson endpoint seam remains.

## 2. Exact construction and statement

Put

\[
 r(u)=
 \begin{cases}
 e^{-1/u},&u>0,\\
 0,&u\leq0,
 \end{cases}
 \qquad
 s(u)=\frac{r(u)}{r(u)+r(1-u)}.
\]

Then \(s\in C^\infty(\mathbb R)\), \(0\leq s\leq1\), \(s=0\) on
\(( -\infty,0]\), \(s=1\) on \([1,\infty)\), and \(s\) is nondecreasing.
Define the fixed nonincreasing step

\[
 \eta(t)=1-s(3(t-1))
\]

and the band

\[
 W(t)=\eta(t)-\eta(2t).
\]

They have the following exact properties:

\[
 \eta(t)=1\quad(t\leq1),\qquad
 \eta(t)=0\quad(t\geq4/3),
\]

\[
 W\in C_c^\infty(\mathbb R),\qquad
 0\leq W\leq1,\qquad
 \operatorname{supp}W\subset[1/2,4/3],
\]

and

\[
 \boxed{W(t)=1\quad\hbox{for }2/3\leq t\leq1.}
\]

The nonnegativity follows from the monotonicity of \(\eta\) for \(t\geq0\);
for \(t<0\), both terms equal \(1\). Moreover

\[
 \operatorname{Var}(\eta)=1,\qquad
 \operatorname{Var}(W)\leq
 \operatorname{Var}(\eta)+\operatorname{Var}(\eta(2\,\cdot))=2.
\tag{2.1}
\]

Let \(X\) be sufficiently large, \(y=\lfloor\sqrt X\rfloor\), and
\(D_j=2^{-j}y\). Set

\[
 J=\max\{j\geq0:D_j\geq X^{1/4}\}.
\]

Thus

\[
 D_J\geq X^{1/4}>D_{J+1}=D_J/2.
\tag{2.2}
\]

For positive integers \(d\), define the top band, the interior active
bands, and the bottom remainder by

\[
 w_0(d)=\mathbf 1_{d\leq y}W(d/y),
\tag{2.3}
\]

\[
 w_j(d)=W(d/D_j)\qquad(1\leq j\leq J),
\tag{2.4}
\]

and

\[
 w_{\rm bot}(d)=\eta(d/D_{J+1})
 =\eta(2^{J+1}d/y).
\tag{2.5}
\]

With the discrete norm

\[
 \|a\|_{\mathrm{BV}_d}
 :=\sup_{d\geq1}|a(d)|+
 \sum_{d\geq1}|a(d+1)-a(d)|,
\tag{2.6}
\]

the exact conclusions are:

1. For every positive integer \(d\),

   \[
   \boxed{
   \mathbf 1_{d\leq y}=w_0(d)+\sum_{j=1}^{J}w_j(d)+w_{\rm bot}(d).}
   \tag{2.7}
   \]

2. Every weight is nonnegative, and

   \[
   \|w_0\|_{\mathrm{BV}_d}\leq3,
   \qquad
   \|w_j\|_{\mathrm{BV}_d}\leq3\ (1\leq j\leq J),
   \qquad
   \|w_{\rm bot}\|_{\mathrm{BV}_d}\leq2.
   \tag{2.8}
   \]

   In particular all are at most \(4\), as requested.

3. Every active \(D_j\geq X^{1/4}\) satisfies, for all sufficiently large
   \(X\),

   \[
   \boxed{\sum_{d\geq1}|w_j(d)|\geq D_j/8.}
   \tag{2.9}
   \]

4. For \(H_D=\lfloor DX^{-1/4}\rfloor\) and every active \(D\),

   \[
   \boxed{
   \tfrac12DX^{-1/4}\leq H_D\leq DX^{-1/4}.}
   \tag{2.10}
   \]

   In particular \(H_D\geq1\).

5. Every \(w_j\) with \(1\leq j\leq J\) is the full rescaling of the one
   fixed \(C_c^\infty\) profile \(W\). The top band is the fixed BV profile
   \(W(t)\mathbf 1_{t\leq1}\), and it has the sole upper endpoint jump
   \(w_0(y)=1\), \(w_0(y+1)=0\). All other weights vanish well before \(y\).

6. The bottom remainder is exactly the union of all inactive dyadic bands,

   \[
   w_{\rm bot}(d)=\sum_{j>J}W(d/D_j),
   \tag{2.11}
   \]

   and is supported on

   \[
   d<\frac43D_{J+1}<\frac43X^{1/4}.
   \tag{2.12}
   \]

   Hence its contribution before Fourier expansion is \(O(X^{1/4})\) for
   every uniformly bounded pre-Fourier summand, including the project
   sawtooth terms and their fixed two-shift difference.

## 3. Independent proof

### 3.1 Exact partition and inactive union

For \(1\leq d\leq y\), put \(t=d/y\leq1\). Telescoping gives

\[
 \sum_{j=0}^{J}W(2^jt)
 =\sum_{j=0}^{J}\bigl(\eta(2^jt)-\eta(2^{j+1}t)\bigr)
 =\eta(t)-\eta(2^{J+1}t).
\]

Since \(\eta(t)=1\), adding (2.5) proves (2.7) on the required range. If
\(d>y\), the top term is zero by definition; for \(j\geq1\), one has
\(d/D_j>2\), so \(W(d/D_j)=0\); and the argument of the bottom \(\eta\) is
greater than \(2\), so that term also vanishes. This proves the stronger
all-\(d\) identity (2.7).

Letting the terminal index tend to infinity in the same telescoping
identity proves (2.11), because
\(\eta(2^nd/y)\to0\) for every \(d\geq1\). The support assertion (2.12)
follows from \(\eta(u)=0\) for \(u\geq4/3\) and (2.2). Counting this support
proves the pre-Fourier \(O(X^{1/4})\) bound.

### 3.2 BV bounds and the unique endpoint jump

For a \(C^1\) function \(F\), sampling cannot increase total variation:

\[
 \sum_{d\geq1}|F((d+1)/D)-F(d/D)|
 \leq\int_0^\infty |F'(t)|\,dt.
\]

Thus (2.1) gives the interior estimate in (2.8). The bottom samples a
nonincreasing function between \(0\) and \(1\), so its discrete variation
is at most \(1\).

On \([0,1]\), \(\eta(t)=1\), hence

\[
 W(t)=1-\eta(2t),
\]

which is nondecreasing from \(0\) to \(1\). Therefore the variation of the
top samples through \(d=y\) is at most \(1\), and the cutoff adds exactly
the jump \(1\) from \(d=y\) to \(d=y+1\). This proves
\(\|w_0\|_{\mathrm{BV}_d}\leq1+1+1=3\).

For \(j\geq1\), the upper edge of the support is at most

\[
 \frac43D_j\leq\frac23y,
\]

and the bottom remainder also vanishes by \(2y/3\). Consequently none of
these terms meets the finite endpoint \(y\); the top cutoff is the unique
upper-endpoint seam.

### 3.3 Sampled mass and height rounding

On every active band, all integers in

\[
 \left[\frac23D_j,D_j\right]
\]

have weight \(1\). This interval is retained by the top cutoff when
\(j=0\). Its number of integers is at least \(D_j/3-1\), which is at least
\(D_j/8\) once \(D_j\geq24/5\). Since active \(D_j\geq X^{1/4}\), this is
uniform for all active bands when \(X\) is sufficiently large.

Finally, set \(z=DX^{-1/4}\geq1\). If \(1\leq z<2\), then
\(\lfloor z\rfloor=1\geq z/2\). If \(z\geq2\), then
\(\lfloor z\rfloor\geq z-1\geq z/2\). The upper bound is immediate. This
proves (2.10), including the delicate lowest active height \(H_D=1\).

## 4. Exact downstream interface audit

### 4.1 Normalized BV

**Follows for every active band.** Equations (2.8) and the fixed-shell
supports

\[
 \operatorname{supp}w_0\subset[D_0/2,D_0],
 \qquad
 \operatorname{supp}w_j\subset[D_j/2,4D_j/3]\quad(j\geq1)
\]

give the accepted normalized discrete BV hypothesis with an absolute
constant. The top band is BV but discontinuous as a continuum profile.

### 4.2 B1 signed lift cancellation

**Follows for every active band, including the top band.** Sampling any of
these fixed BV profiles on an increasing restricted lattice \(d=gq\), or
on its odd-\(g\) sublattice, has uniformly bounded variation. For odd
\(p\), the factor

\[
 \frac{\Phi(g|p|/(H+1))}{g}
\]

is nonnegative and nonincreasing on its support. On \(gq\asymp D\), its
supremum and total variation are \(O(q/D)\). Abel summation against the
bounded partial sums of \(\chi_4(g)\) therefore gives the accepted estimate

\[
 |A_\chi(p/q)|
 \ll \frac1{|p|}\min(1,q/D).
\]

Even \(p\) still gives zero by the accepted beta algebra. This conclusion
uses the explicit fixed-shell BV structure, not merely boundedness. It is
an individual pair-weight estimate and does not imply a signed fat-band
or pointwise M2 estimate.

### 4.3 W-1 transfer

**Follows for every active band with \(\lambda=1/8\).** The required inputs
are now explicit:

\[
 0\leq w_j\leq1,\qquad
 \operatorname{supp}w_j\subset[aD_j,bD_j]
 \quad(a=1/2,\ b=4/3),
\]

\[
 \sum_d|w_j(d)|\geq D_j/8,\qquad H_{D_j}\geq1.
\]

Thus the accepted weighted unit-frequency lower bound applies, conditional
on its separately accepted exact-\(N=0\) subtraction. Its conclusion is
only for absolute beta-weighted mass or a genuinely unsigned analogue. A
positive \(h=1\) subtotal is not a lower bound for the full signed fourth
moment.

### 4.4 TTY exponent-pair wedge

**The denominator-weight hypothesis follows for every active band.** The
uniform discrete BV bound (2.8) is exactly what partial summation needs in
the accepted TTY transfer. Continuum smoothness is not required for this
transfer, so the top endpoint jump is harmless here. Subject to the other
already accepted frequency-block hypotheses, the certified wedge

\[
 178\ell+1638\delta\leq463
\]

therefore applies to this partition. This does not extend the wedge and
does not close the residual corridor.

### 4.5 Fejer residual

**The profile-side hypotheses follow; the Fejer theorem and R5 estimate
are not reproved here.** The construction supplies an exact nonnegative
partition, \(\|w_j\|_\infty\leq1\), fixed-shell support, and

\[
 H_{D_j}\asymp D_jX^{-1/4},\qquad H_{D_j}\geq1,
\]

uniformly down to the lowest active band. Therefore the audited
floor-compatible Vaaler residual can be majorized blockwise by its positive
Fejer kernel with the intended height normalization. The inactive tail is
removed before Fourier expansion at cost \(O(X^{1/4})\).

This validates the missing profile and rounding inputs only. It does not
upgrade `R5-Full` or eliminate `R5-Full-reconciliation`; the accepted
product-count argument and its edge cases remain separate dependencies.

### 4.6 Smooth Poisson

**Follows verbatim for interior active bands only.** For every
\(1\leq j\leq J\), \(w_j(d)=W(d/D_j)\) with the same fixed
\(W\in C_c^\infty((2/5,3/2))\), so the accepted smooth-Poisson identity and
its \(O_W(1)\) error apply uniformly.

**It does not follow for the top band.** The continuum profile there is

\[
 W(t)\mathbf 1_{t\leq1},
\]

which jumps by \(1\) at \(t=1\). Its discrete BV bound is enough for B1 and
TTY, but it gives no continuum derivatives and does not justify the
accepted smooth stationary-phase/Poisson formula. A separate one-sided
endpoint transform, an unsmoothing estimate, or a direct pointwise bound
is still required for that single band. The bottom remainder is not
Fourier expanded at all.

## 5. Required controls and outcomes

### Partition control: pass

The finite telescoping identity (2.7) is exact, not asymptotic. Checking
\(d=y\) gives total \(1\) because \(w_0(y)=W(1)=1\) and every other term is
zero there. Checking \(d>y\) gives total \(0\).

### Endpoint control: pass with one declared seam

Only \(w_0\) reaches \(d=y\), and its jump is exactly \(1\). Every interior
active band and the bottom remainder vanishes by \(2y/3\). The control
therefore detects precisely one nonsmooth upper endpoint rather than
silently treating it as smooth.

### BV control: pass

The two monotone step variations give
\(\operatorname{Var}(W)\leq2\). Sampling gives interior norm at most \(3\);
top truncation gives norm at most \(3\); the bottom gives norm at most
\(2\). All requested \(4\)-bounds pass.

### Mass and coefficient-support control: pass

The plateau contributes at least \(D/3-1\geq D/8\) samples for large \(X\).
The rounding proof gives \(H_D\geq1\), so the accepted Vaaler unit
coefficient \(|\beta_{1,H_D}|\geq1/(2\pi)\) is present on every active band.

### Degenerate-profile control: pass for this construction

The fixed unit plateau rules out the zero profile and scale-degenerate
families that invalidate an unqualified “bounded smooth” transfer. If the
profile were multiplied by a \(D\)-dependent factor tending to zero, the
W-1 conclusion would again fail; that alteration is not allowed here.

### Continuum-smoothness control: fail at exactly the intended top band

The top discrete sequence passes BV but its continuum extension has a hard
jump. Accordingly, TTY/B1 pass there and smooth Poisson does not. No
numerical experiment was used to certify any statement.

## 6. First doubtful or unproved step

There is no doubtful step in the finite partition, BV, sampled-mass, or
height-rounding proof. The first unresolved downstream step is transferring
the accepted smooth-Poisson formula to the top block. Such a transfer is
not licensed: discrete BV does not imply continuum smoothness, and the
current accepted packet contains no one-sided endpoint stationary-phase or
unsmoothing theorem for this jump. Separately, the Fejer product-count
reconciliation remains outside this report.

## 7. Dependencies and exact artifacts used

Only the brief-authorized statement packet was used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml` (round objective and scope);
- `rounds/codex-managed/m9-endpoint-kernel-validation/briefs/blind_profile_rederivation.md`;
- `rounds/codex-managed/m9-unit-frequency-w1-validation/reports/h4_weight_normalization_review.md`;
- `rounds/codex-managed/m9-frequency-phase-diagram/synthesis.md`.

No Round-6 claimant report, proof draft, validation matrix, legacy response,
or unlisted source was read.

## 8. Recommended state effect

1. **Promote after conductor adoption of this explicit partition:**
   `M9-M2-dyadic-weight-nondegeneracy` can become `proved_internal`, because
   fixed-shell support, sampled \(\ell^1\) mass, normalized BV, endpoint
   rule, and height rounding are all proved for every active block.
2. **Remove the profile blocker from the accepted B1, W-1, and TTY uses:**
   B1 and TTY apply to every active band; W-1 applies with
   \(\lambda=1/8\) and retains its absolute/unsigned-only scope.
3. **Retain the Fejer status:** the construction validates only profile and
   rounding inputs. `R5-Full-reconciliation` remains a separate obligation.
4. **Revise the smooth-Poisson applicability statement:** the accepted
   duality applies uniformly to all interior active blocks, but not to the
   single top endpoint block. Do not infer `M9-endpoint-uniformity` from the
   interior formula.
5. **Retain `M9-endpoint-uniformity` as open:** the smallest remaining
   correction is to state one explicit top-band endpoint lemma rather than
   claiming that discrete BV supplies continuum smoothness.
