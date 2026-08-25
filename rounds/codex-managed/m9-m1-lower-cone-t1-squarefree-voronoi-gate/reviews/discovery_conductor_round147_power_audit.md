# Round 147 hostile power and scope audit

## 1. Result

**Verdict: revise, then promote only the scoped method no-go and the exact fixed-order reductions.**  The conductor candidate's principal power calculation is correct:

\[
\min\!\left(\frac{M^{1/4}}k,\frac R{\sqrt M}\right)
\]

is the physically weighted fixed-\(k\) menu, the crossover is
\(k_0=M^{3/4}/R\), powerful-number summation gives

\[
\begin{cases}
M^{1/4+O(\varepsilon)},&M\le R^{4/3},\\
R^{1/2+O(\varepsilon)}M^{-1/8},&R^{4/3}\le M\le R^2,
\end{cases}
\]

and the excesses over target are \(R^{1/3+O(\varepsilon)}\) at
\(M=R^{4/3}\) and \(R^{1/4+O(\varepsilon)}\) at \(M=R^2\).  The bare
reciprocal-phase lemma is also correct with its stated restriction
\(Q\le N/4\), and the displayed Möbius expansion loses \(D^{1/2}\)
under the specified triangle placement.

Four corrections are mandatory before promotion:

1. equations (147.C6), (147.C20), and (147.C40) must state that the
   power ledger is taken on \(\Re z=0\), or on a Perron line
   \(c=\Re z\) satisfying \(k^{|c|}\ll X^\varepsilon\), for example
   \(c=1/\log X\); it is not the displayed bound uniformly on an
   arbitrary fixed strip;
2. the amplitude and resonance claims (147.C5) and
   (147.C35)--(147.C37) must be labelled fixed-order, or conditional on
   the missing growing-order kernel estimate;
3. the paragraph after (147.C30) and the required correlation
   (147.C44) must use the natural physical cutoff
   \(k\le K_F:=\sup\operatorname{supp}F=O(M)\); for each
   \(k>K_F\), polar and dual terms cancel **separately for that \(k\)**,
   rather than constituting another resonant channel;
4. the paragraph after (147.C42) must say that \(R^{4/3}\) is the
   crossover only after the reciprocal price \(R/\sqrt M\) is combined
   with the primal price \(M^{1/4}\).  The \(q\)-average alone does not
   single out \(R^{4/3}\).

These repairs do not change the adverse power verdict.  They prevent a
fixed-\(\Re z\) loss, an artificial infinite family of resonances, and a
conditional Bessel estimate from being recorded as an unconditional
physical bound.

## 2. Exact statement and audit hypotheses

The audit uses the exact weighted target

\[
\sup_{M\le U\le B_M}
\left|\sum_{\substack{M\le s<U\\\mu^2(s)=1}}
s^{-3/4}V_{\rm low}(R^2s/N)C(s)e(+\sqrt{Ns})\right|
\ll X^\varepsilon,
\tag{147.P1}
\]

and its sufficient unweighted form

\[
\sup_{M\le U\le B_M}
\left|\sum_{\substack{M\le s<U\\\mu^2(s)=1}}
V_{\rm low}(R^2s/N)C(s)e(+\sqrt{Ns})\right|
\ll M^{3/4}X^\varepsilon.
\tag{147.P2}
\]

Here \(R=X^{1/4}\), \(N=\lfloor X\rfloor\asymp R^4\),
\(M\le R^2\), and the physically active convolution indices satisfy
\(k\le K_F=O(M)\).  For the \(D,E\) boxes,

\[
DE\asymp M,\qquad D\le \sqrt M,\qquad
Q\asymp D\sqrt{N/M}=\frac{DR^2}{\sqrt M}\le R^2.
\tag{147.P3}
\]

The power estimates below use either \(z=i\tau\), or the actual small
Perron abscissa \(z=c+i\tau\) with \(c=1/\log X\).  The exact
fixed-order identities remain valid in the larger strip stated by the
candidate, but their \(h_z(k)\)-bounds cannot be discarded in a
power-sensitive sum when \(c\) is a fixed positive constant.

The hostile verdict is deliberately scoped.  It audits:

- fixed-index Voronoi followed by modulus;
- absolute aggregation over powerful \(k\);
- the bare reciprocal divisor count followed by literal Möbius
  expansion and triangle inequality; and
- a contour shift through the reciprocal zeta and \(L\)-factors without
  a zero-residue owner.

It does not assert a lower bound for (147.P1), and it does not exclude a
new joint signed \(k,m\) or squarefree \(d,q\) theorem.

## 3. Recomputed power, boundary, and cancellation ledger

### 3.1 Raw and physically weighted Voronoi sizes

For a fixed physically active \(k\), the primal convolution has length
\(M/k\).  Thus

\[
\text{primal raw}\ll \frac MkX^\varepsilon,\qquad
\text{primal weighted}\ll \frac{M^{1/4}}kX^\varepsilon.
\tag{147.P4}
\]

At the conductor-four centre \(m/k=N\), the large-argument Bessel
factor has size \((NM)^{-1/4}\).  The \(u\)-integral has length \(M\)
and (147.C29) contributes \(1/k\), so one term has sizes

\[
\text{one term raw}\ll\frac{M^{3/4}}{kR}X^\varepsilon,\qquad
\text{one term weighted}\ll\frac1{kR}X^\varepsilon.
\tag{147.P5}
\]

The resonant interval contains

\[
\#\{m\}=O\!\left(k\sqrt{N/M}\right)
=O\!\left(\frac{kR^2}{\sqrt M}\right)
\tag{147.P6}
\]

integers.  Hence

\[
\text{dual band raw}\ll RM^{1/4}X^\varepsilon,\qquad
\text{dual band weighted}\ll\frac R{\sqrt M}X^\varepsilon.
\tag{147.P7}
\]

Equations (147.C35)--(147.C37) therefore have the correct powers.  The
word “physical” in the headline amplitude (147.C5) means after
multiplication by \(M^{-3/4}\); this should be made explicit.

### 3.2 The \(k_0\) split

Equating the two raw prices, or the two weighted prices, gives

\[
k_0=\frac{M^{3/4}}R.
\tag{147.P8}
\]

When \(k_0\ge1\), the powerful count
\(P(K)\ll K^{1/2+\varepsilon}\) gives

\[
\begin{aligned}
RM^{1/4}P(k_0)&\ll R^{1/2}M^{5/8}X^\varepsilon,\\
M\sum_{\substack{k>k_0\\k\ {\rm powerful}}}\frac1k
&\ll R^{1/2}M^{5/8}X^\varepsilon.
\end{aligned}
\tag{147.P9}
\]

After division by the raw target \(M^{3/4}\), both are
\(R^{1/2}M^{-1/8}X^\varepsilon\).  When \(k_0<1\), the direct
powerful \(1/k\)-sum costs \(M X^\varepsilon\) raw and
\(M^{1/4}X^\varepsilon\) after the physical weight.  Thus:

| scale | raw upper capacity | raw target | excess |
|---|---:|---:|---:|
| \(M=R^{4/3}\) | \(R^{4/3+O(\varepsilon)}\) | \(R\) | \(R^{1/3+O(\varepsilon)}\) |
| \(M=R^2\) | \(R^{7/4+O(\varepsilon)}\) | \(R^{3/2}\) | \(R^{1/4+O(\varepsilon)}\) |

This verifies (147.C6) and (147.C40) on the small Perron abscissa.

For a fixed \(c=\Re z>0\), however, (147.C20) gives
\(|h_z(k)|\ll k^{c+\varepsilon}\).  The \(k_0\ge1\) calculation then
becomes

\[
R^{1/2-c}M^{-1/8+3c/4}X^\varepsilon
\tag{147.P10}
\]

after physical normalization; at \(M=R^2\) this is
\(R^{1/4+c/2}X^\varepsilon\).  Formula (147.C6) therefore requires
\(c=0\) or \(c\log X=O_\varepsilon(1)\).  This is a bookkeeping repair,
not a new obstruction, because Perron permits \(c=1/\log X\).

### 3.3 Bare \(q\)-average and squarefree expansion

With \(q\in[Q,2Q)\) and \(Q\le N/4\), let \(a\) be the nearest integer
to \(N/q\) and \(j=N-aq\).  Then \(a\ne0\),
\(|j|\le q/2\), and

\[
\left|\sum_{d\asymp D}e(Nd/q)\right|
\ll
\begin{cases}
D,&j=0,\\
\min(D,q/|j|),&j\ne0.
\end{cases}
\]

For fixed \(j\ne0\), every admissible \(q\) divides \(N-j\), and
\(|N-j|\asymp N\).  A dyadic sum over \(j\), plus
\(\#\{q\asymp Q:q\mid N\}\ll N^\varepsilon\) for \(j=0\), proves

\[
\sum_{q\asymp Q}
\left|\sum_{d\asymp D}e(Nd/q)\right|
\ll (Q+D)(NQ)^\varepsilon.
\tag{147.P11}
\]

The condition \(Q\le N/4\) is necessary for this proof and is
comfortably satisfied by (147.P3), since \(Q\le R^2\ll N\asymp R^4\).
At \(M=R^2\), \(Q=RD\), so (147.P11) meets the required
\(RD X^\varepsilon\) capacity.  In general its \(Q\)-term has ratio

\[
\frac{Q}{RD}=\frac R{\sqrt M}.
\tag{147.P12}
\]

Only after taking the minimum of (147.P12) with the primal
\(M^{1/4}\) price does one obtain the crossover \(M=R^{4/3}\).

Expanding squarefreeness of \(d\) gives

\[
\mu^2(d)=\sum_{a^2\mid d}\mu(a).
\]

Triangle inequality and (147.P11), now with numerator \(Na^2\) and
inner length \(D/a^2\), give

\[
\sum_{q\asymp Q}
\left|\sum_{d\asymp D}\mu^2(d)e(Nd/q)\right|
\ll QD^{1/2}+D.
\tag{147.P13}
\]

Equivalently, a split at \(A\) costs \(AQ+D+QD/A\), optimized at
\(A=D^{1/2}\).  Relative to the required \(RD\) scale, its leading
ratio is

\[
\frac{QD^{1/2}}{RD}=\frac{R D^{1/2}}{\sqrt M}.
\tag{147.P14}
\]

At the balanced top boundary \(M=R^2,D\asymp R\), this is \(R^{1/2}\).
Equation (147.C43) is therefore correct as an upper bound produced by
this expansion-plus-triangle proof.  It is not a lower bound for the
squarefree exponential sum and must not be promoted as one.

### 3.4 Prefix, polar, and the \(k>K_F\) tail

If a prefix has length \(<\sqrt M\), the raw divisor bound costs
\(M^{1/2+\varepsilon}\), below the target \(M^{3/4+\varepsilon}\).
Otherwise, peeling \(O(\sqrt M)\) terms at each endpoint has the same
target-safe cost and permits a compact smooth cutoff with transition
length \(\asymp\sqrt M\).  This part of the candidate is correct.
Its transformed seminorms still belong to the stated uniform-kernel
seam.

For the polar integral, the interior phase scale is
\(\sqrt{NM}\).  On a peeled endpoint collar of length \(\sqrt M\),
the local oscillation is

\[
\sqrt{N/M}\,\sqrt M=\sqrt N=R^2.
\]

The cone order obeys
\(|z|^2\ll D X^\varepsilon\le\sqrt M X^\varepsilon\), so repeated
integration by parts beats the polynomial \(L\)-factor and the
absolutely convergent \(H(1-z,z)\), once the rapid smooth cone-Mellin
weight is retained.  The candidate's polar claim is target-safe for the
smoothed cone.  It is not a proof for a hard Perron integral of height
\(D\), which the candidate does not claim to use.

Let \(K_F=\sup\operatorname{supp}F\).  If \(k>K_F\), then
\(F(kn)=0\) for every integer \(n\ge1\).  Applying (147.C27) to
\(F(k\cdot)\) therefore gives, for each such \(k\),

\[
\begin{aligned}
0={}&L(1-2z,\chi_4)k^{z-1}
\int_0^\infty F(u)u^{-z}\,du\\
&+\frac{\pi4^z}{k}\sum_{m\ge1}A_{-z}(m)
\int_0^\infty F(u)
\mathscr B_{2z}(2\pi\sqrt{mu/k})\,du.
\end{aligned}
\tag{147.P15}
\]

Thus cancellation is per \(k\), not merely an unexplained aggregate
over \(k>2M\).  The separate tail is summable for
\(0<\Re z<1/4\): using (147.C20), its absolute majorant is a powerful
sum of \(k^{-1+2\Re z+\varepsilon}\).  The physical resonance ledger
and (147.C44) must consequently be restricted to \(k\le K_F=O(M)\).
If endpoint smoothing slightly changes the support, \(K_F\), rather
than the literal number \(2M\), is the correct cutoff.

## 4. First doubtful step and mandatory corrections

The first genuinely unproved analytic step remains the uniform
growing-complex-order expansion of (147.C26), including derivatives,
transition ranges, and the moving-prefix seminorms through the cone
bandwidth (147.C12).  The exact fixed-\(z\) formula does not supply that
estimate.

The first missing arithmetic power after granting that seam remains the
signed, physically truncated version of (147.C44):

\[
\sum_{\substack{k\le K_F\\k\ {\rm powerful}}}\frac{h_z(k)}k
\sum_{|j|\lesssim k\sqrt{N/M}}
A_{-z}(kN+j)\mathcal W_{k,z,U}(j)
\ll X^\varepsilon,
\tag{147.P16}
\]

after physical normalization and actual cone-order integration.  The
candidate proves neither (147.P16) nor a squarefree strengthening of
(147.P11).

Mandatory candidate corrections, by location, are:

| Location | Required correction | Effect on verdict |
|---|---|---|
| (147.C5), headline item 3 | Add “for fixed order” or “conditional on the uniform estimate following (147.C29)”; restrict “channel” to physically active \(k\). | No power change. |
| (147.C6), (147.C20), (147.C40) | State \(c=\Re z=0\) or \(k^{|c|}\ll X^\varepsilon\), preferably \(c=1/\log X\).  For fixed \(c>0\), replace the second line by (147.P10). | Removes an unrecorded \(R^{c/2}\) top loss. |
| Paragraph after (147.C30) | Replace “cancel exactly in their aggregate” by the per-\(k\) identity (147.P15), and replace \(2M\) by \(K_F=\sup\operatorname{supp}F=O(M)\). | Prevents artificial tail resonances. |
| (147.C35)--(147.C37) | Mark the Bessel sizes fixed-order/conditional; retain the raw-versus-weighted labels exactly as in (147.P5)--(147.P7). | No numerical change. |
| Paragraph after (147.C42) | Attribute \(R^{4/3}\) to \(\min(M^{1/4},R/\sqrt M)\), not to the \(q\)-average alone. | Scope clarification. |
| (147.C44) | Restrict \(k\le K_F\), or explicitly include the per-\(k\) polar cancellation for the complementary tail. | Makes the proposed missing theorem physically exact. |
| Section 7 graph recommendation | Promote only exact arithmetic/Euler identities, the fixed-order transform, collars, and the scoped conditional capacity no-go.  Do not promote a uniform cone-integrated Voronoi estimate, a literal top range, or (147.C44). | Required promotion boundary. |

No correction is required to (147.C35)--(147.C43)'s numerical exponents
once these hypotheses and scopes are made explicit.

## 5. Control outcomes

| Seam | Hostile outcome |
|---|---|
| Raw/weighted normalization | **Pass.** Equations (147.P4)--(147.P7) reproduce (147.C35)--(147.C37). |
| \(k_0\) and powerful summation | **Pass after small-\(c\) repair.** The exponents in (147.C6) and (147.C40) are correct on the actual Perron line. |
| \(R^{4/3}\) and top blocks | **Pass.** Losses are respectively \(R^{1/3}\) and \(R^{1/4}\), and are upper-capacity losses only. |
| Bare \(q\)-average | **Pass.** The proof and the necessary \(Q\le N/4\) hypothesis are correct. |
| Literal \(\mu^2\) expansion | **Pass as a method bound.** It yields (147.P13), not a lower bound or an impossibility theorem. |
| Polar term | **Pass for the smooth-cone reduction.** The phase is uniformly nonstationary and endpoint collars have \(R^2\) oscillation. |
| Prefix endpoints | **Pass as a reduction.** Short prefixes and peeled \(\sqrt M\)-collars are raw-target safe; transformed seminorms remain open. |
| \(k>K_F\) | **Revise wording.** Cancellation is exact per \(k\); those indices are not physical resonant channels. |
| Uniform Bessel order | **Open.** Fixed-order geometry may be promoted, not a growing-order bound. |
| Signed \(H\)-aggregation | **Open/adverse.** Neither disjoint bands nor \(H\)-convergence proves (147.P16). |
| Inverse-\(L\) contour | **Adverse.** The candidate correctly refuses a residue-free fixed shift through possible reciprocal-zero poles. |
| No-go versus lower bound | **Pass after the qualifications above.** The candidate explicitly calls (147.C6) an upper-capacity calculation and leaves joint signed methods open. |

## 6. Dependencies and downstream-owner audit

This review used only:

- state/active_campaign.yml;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/candidates/conductor_round147_t1_squarefree_voronoi_and_H_no_go.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/reports/t1_squarefree_voronoi_attack.md.

The candidate's downstream scope is correct.  Neither the exact
fixed-order formula nor the scoped no-go proves:

- the literal \(t=1\) target (147.C3) or (147.C4);
- any \(t\ge2\) layer or their joint cancellation with \(t=1\);
- the independent Round-138 collar-tail cross owner;
- the complete lower scalar, lower GAR, or either direct M1 parent;
- \(M9\!-\!M1\), any M2 owner, or \(M9\!-\!M2\);
- endpoint uniformity, M9, the bridge, or the quarter target; or
- an improved internal or global exponent.

The internal exponent therefore remains \(1/3\).  The external
Li--Yang value in (147.C45) is pre-existing context and receives no new
proof or promotion from Round 147.

## 7. Recommended state effect and promotion verdict

**Promotion verdict: revise_then_promote_scoped_no_go.**

After the mandatory corrections in Section 4:

- promote the exact coefficient and sector identities
  (147.C8)--(147.C10);
- promote the Euler factors, powerful support, and meromorphic
  refactorization (147.C13)--(147.C25), with no residue-free contour
  shift;
- promote the fixed-order compact-smooth transform and exact
  \(H\)-convolution (147.C26)--(147.C30), using the per-\(k\) tail
  cancellation (147.P15);
- retain the cone collar, radial endpoint peeling, fixed-order
  conductor-four centre, and the recomputed raw/weighted ledger as
  exact reductions or conditional capacity calculations with their
  stated hypotheses;
- promote the label
  \(\mathsf{squarefree\_H\_resonance\_no\_go}\) only for the explicitly
  enumerated termwise/triangle/zero-free method menu.

Do not promote a \(t=1\) estimate, a strict top-scale range, the
growing-order kernel bound, the signed correlation (147.P16), a
downstream owner, or an exponent improvement.  The corrections leave
the round's useful conclusion intact: the next genuine interface is
joint signed squarefree-\(H\) aggregation, not another absolute
fixed-channel transform.
