# Round216: anchored divisor projections and their complete high-value cost

Campaign: `gc-actual-radical-high-values`. Task: `anchored_divisor_high_values`.
Role: discovery; selected-context claimant, not an independent reviewer.
Generated: 2026-09-28T02:01:06+08:00.
Starting graph SHA256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
All work is analytical, algebraic or source checking; no experiments.

## 1. Result: rigorous delimitation, with no complete high-value gain

Opening the actual divisor identity before Cauchy produces a different
interface from round209. Its real correlation kernels have arguments

\[
 R_j\sqrt d-R_l\sqrt e\quad\hbox{and}\quad R_j\sqrt d+R_l\sqrt e.
                                                        \tag{1}
\]

Thus Cauchy in the cofactor preserves the absolute physical radius.
There is no replacement by a matrix depending only on \(R_j-R_l\),
and no centering of \(r_2\).

Two precise conclusions are proved below.

* A high actual divisor rectangle at level \(v\) can occur only if
  \[
  N\gg v^4,\qquad
  D\gg_\eta T^{-13/42-2\eta}v^2N^{29/84}.                 \tag{2}
  \]
  This excludes small divisor rectangles on every relevant scale, but
  is not an improved bound for the complete physical high-value moment.
* The signed, anchored energy estimate (12), with
  \(\rho=208/2625\), is a complete sufficient arithmetic input for
  H216. Its exact consequence is
  \[
  H_{12}(T)\ll_\epsilon
       T^{113/125+42\rho/13+\epsilon}.                   \tag{3}
  \]
  At the displayed value of \(\rho\), this is precisely
  \(T^{29/25+\epsilon}\). The estimate (12) is **unproved**.

Applying the accepted unweighted correlation bound term by term to
this anchored energy gives instead the two costs

\[
 T^\epsilon\{J\sqrt N+J^2T^{13/55}D^{34/55}\},            \tag{4}
\]

after restoring the Cauchy factor. They do not imply (12). In
particular, the second term cannot be absorbed even at the original
lowest retained level. This is a failure of the specified absolute
kernel closure, not a lower bound for the signed energy or the actual
moment. The complete unconditional high-value estimate remains
\(H_{12}(T)\ll T^{10\beta+\epsilon}\), as already accepted.

## 2. Exact hypotheses and quantities

Use the frozen mollifier and window: \(T\ge2\) is real;
\(\Psi(s)=\widehat\varrho(se_1)\), with \(\varrho\) nonnegative,
real, radial, smooth, unit mass and supported in the unit disk;
\(w\ge0\) is fixed and smooth, supported in \([1/2,2]\), and equal
to one on \([1/\sqrt2,\sqrt3]\). Put

\[
 a_T(n)=n^{-3/4}\Psi(\sqrt{n/T}),\qquad
 B_T(R)=\sum_{n\ge1}r_2(n)a_T(n)
                  \cos(2\pi R\sqrt n-3\pi/4),
 \quad V_0=T^{13/125}.
\]

The mollifier assumptions imply \(|\Psi|\le1\), but \(\Psi\) is
not presumed nonnegative away from zero. All its signs remain in the
formulas. Let

\[
 \theta=\frac{3292+25\sqrt{1717}}{13762},\qquad
 \beta=2\theta-\tfrac12,
 \quad q=136/13,\quad \gamma=29/25.
\]

The existing accepted inputs are the complete distribution
\(D_B(V)\ll T^\epsilon(V^{-2}+TV^{-q})\), the physical supremum
\(\|B_T\|_\infty\ll T^{\beta+\epsilon}\), and the unweighted
square-root exponential-sum estimates in the permitted proof kernel.
Li--Yang is used only through that qualified physical supremum.

Take \(Z=T^{3/2}\). Partition the integers \(1\le n\le Z\) into
half-open dyadic blocks \(N\le n<2N\), \(N=1,2,4,\ldots\),
intersected with \(n\le Z\). For each such block use
\(D=1,2,4,\ldots,N\) and \(D\le d<2D\). Write \(K=N/D\ge1\).
The cofactor always lies in \([K/2,2K)\cap\mathbb Z_{\ge1}\).
Set

\[
 h_{N,T}(n)=(N/n)^{3/4}\Psi(\sqrt{n/T})
              1_{N\le n<2N,\ n\le Z},
\]

and define the exact real divisor rectangle

\[
 H_{N,D}(R)=4N^{-3/4}
  \sum_{D\le d<2D}\chi_4(d)
  \sum_{k\in[K/2,2K)\cap\mathbb Z_{\ge1}}
       h_{N,T}(dk)\cos(2\pi R\sqrt{dk}-3\pi/4).           \tag{5}
\]

Here \(d\) is an ordinary divisor, **not** a squarefree label.
The identity \(r_2(n)=4\sum_{d\mid n}\chi_4(d)\) gives
\(B_T=\sum_{N,D}H_{N,D}+E_Z\) exactly. There are
\(L\ll(1+\log T)^2\) rectangles, including \(N=D=1\).

For any fixed rectangle and real \(v>0\), select a maximal
\(\delta=N^{-1/2}\)-separated subset \(R_1,\ldots,R_J\) of
\(\{R\in[T/2,2T]:|H_{N,D}(R)|>v\}\). If it is nonempty, set
\(\sigma_j=\operatorname{sgn}H_{N,D}(R_j)\in\{-1,1\}\).
Only these actual aligned signs are required in (12); an assertion
for arbitrary independently modulated coefficient arrays is not made.

## 3. Proof and complete cost derivation

### A. A legal one-variable divisor estimate before Cauchy

For fixed \(d\asymp D\), the inner cofactor phase is
\(f(k)=R\sqrt d\sqrt k\), on an actual integer interval of scale
\(M\asymp N/d\). Its total phase parameter is
\(\mathcal T\asymp R\sqrt N\asymp T\sqrt N\).
The accepted exponent pair gives, for every \(\eta>0\),

\[
 \sup_{I\subset[K/2,2K)}
 \left|\sum_{k\in I\cap\mathbb Z}e(R\sqrt d\sqrt k)\right|
 \ll_\eta T^\eta (T\sqrt N)^{13/84}K^{1/2}.              \tag{6}
\]

The phase is the exact square-root monomial in the integer variable;
no character-weighted or shifted-lattice version is being imported.
The large phase condition holds since \(M\ll N\le T^{3/2}\)
and \(M/\mathcal T\ll\sqrt N/T\le T^{-1/4}\), apart from fixed
small-parameter cases covered trivially. Proper subintervals pay their
allowed logarithm. On the smooth part of the support, the supremum
and total variation of \(h_{N,T}(dk)\) are bounded uniformly in
\(N,T,d\); this follows from boundedness of \(\Psi\) and
\(s\Psi'(s)\). The at most two interval-boundary jumps are bounded
as well. Abel summation therefore permits this exact weight in (6).

Summing the resulting bounds over the \(O(D)\) divisors gives

\[
 |H_{N,D}(R)|\ll_\eta
 T^{13/84+\eta}N^{-29/168}D^{1/2}.                        \tag{7}
\]

Counting the \(O(N)\) pairs \((d,k)\) also gives
\(|H_{N,D}|\ll N^{1/4}\). These two bounds prove (2).
Both are uniform for real \(R\in[T/2,2T]\), every partial top
block, and every rectangle; the character was retained until the
specified outer triangle inequality. Neither is a centered-
coefficient variation estimate.

For orientation only, at the full event level \(V\), logarithms and
arbitrarily small powers aside, (2) forces

\[
 D\gtrsim T^{-13/42}V^{71/21}.
\]

At \(V=V_0\) its power is \(221/5250>0\). This is a genuine
restriction on rectangles capable of witnessing the high event,
not an upper bound on that event's measure.

### B. Exact real anchored energy

Abbreviate
\(c_{d,k}=\chi_4(d)h_{N,T}(dk)\) and
\(\vartheta_{j,d,k}=2\pi R_j\sqrt{dk}-3\pi/4\). Define

\[
 \mathfrak Q=\sum_{k\in[K/2,2K)\cap\mathbb Z_{\ge1}}
  \left(\sum_{j=1}^J\sum_{D\le d<2D}
             \sigma_jc_{d,k}\cos\vartheta_{j,d,k}\right)^2.
\]

Cauchy in \(k\), with at most \(2K\) integers, gives

\[
 J^2v^2<\left(\sum_j\sigma_jH_{N,D}(R_j)\right)^2
                \le32KN^{-3/2}\mathfrak Q.               \tag{8}
\]

Expand the real product rather than silently changing the wave:

\[
 \mathfrak Q=\frac12
 \sum_{j,l}\sum_{d,e}\sigma_j\sigma_l
 \sum_k c_{d,k}c_{e,k}
 \left\{\cos(2\pi u^-_{jl,de}\sqrt k)
              -\sin(2\pi u^+_{jl,de}\sqrt k)\right\},     \tag{9}
\]

where \(u^{\pm}_{jl,de}=R_j\sqrt d\pm R_l\sqrt e\).
The minus sign in the sine is fixed by
\(\cos(x-3\pi/2)=-\sin x\). Separate **only** the constant
minus-kernel terms with \((j,d)=(l,e)\):

\[
 \mathfrak D=\tfrac12J\sum_{d,k}c_{d,k}^2\ll JN,
 \qquad \mathfrak O=\mathfrak Q-\mathfrak D.               \tag{10}
\]

Thus \(\mathfrak O\) contains every other minus-kernel term,
including its possible exact zeros, and **all** plus-kernel sine
terms, including those with \((j,d)=(l,e)\). It is real and signed.
For a complete untruncated block with \(N\le cT\), fixed small
\(c>0\), the constant contribution satisfies
\(\mathfrak D\asymp JN\): \(\Psi\) is then bounded below,
and there are \(\asymp N\) admissible pairs with odd \(d\).
This is a statement about the constant contribution, not a lower
bound on \(\mathfrak Q\), because \(\mathfrak O\) can be negative.

This interface preserves the required anchor. Translating all
\(R_j\) by \(R_*\) changes the minus argument by
\(R_*(\sqrt d-\sqrt e)\) and the plus argument by
\(R_*(\sqrt d+\sqrt e)\). The actual \(\chi_4(d)\chi_4(e)\),
the mollifier signs, and the aligned real \(\sigma_j\) remain visible.

### C. The precise unproved arithmetic input, and its complete implication

For a parameter \(\rho\ge0\), consider the following hypothesis,
uniformly over all the actual high-value configurations above, for
levels \(v\ge V_0/(2L)\), and with arbitrary small \(\eta>0\):

\[
 \boxed{\mathfrak O\le
      \frac{J^2v^2N^{3/2}}{64K}
          +C_\eta T^{\rho+\eta}JN.}                     \tag{12}
\]

This is a one-sided signed estimate. It is not an estimate of the
sum of the moduli of the terms in (9). It is the first missing
arithmetic inequality for the chosen projection mechanism.

Assuming (12), (8)--(10) and absorption give

\[
 Jv^2\ll_\eta T^{\rho+\eta}\frac{\sqrt N}{D}.             \tag{13}
\]

The selected set covers the level set by intervals of radius
\(\delta\). Consequently its measure is
\(\ll T^{\rho+\eta}D^{-1}v^{-2}\). Crucially, if the set is
nonempty then \(J\ge1\); hence

\[
 D\ll T^{\rho+\eta}\sqrt N\,v^{-2}.                     \tag{14}
\]

Combining (14) with the second necessary condition in (2) yields

\[
 N\gg_\eta
       T^{-2-84\rho/13-O(\eta)}v^{336/13}.
\]

Substitute this into that same condition in (2):

\[
 D\gg_\eta
       T^{-1-29\rho/13-O(\eta)}v^{142/13}.
\]

It follows that, uniformly for each rectangle,

\[
 |\{|H_{N,D}|>v\}\cap[T/2,2T]|
 \ll_\eta T^{1+42\rho/13+O(\eta)}v^{-168/13}.             \tag{15}
\]

These inequalities remain valid when a displayed lower bound is less
than one. If the lower bounds on \(N\) or \(D\) exceed the actual
range, the high set is empty. No fractional sample count is used.
In particular, merely inserting the smallest \(N\asymp v^4\)
into a diagonal cost without enforcing \(J\ge1\) would give the
wrong conditional power ledger.

For every fixed \(A\), the divisor bound and Schwartz decay give

\[
 \|E_Z\|_\infty
 \le\sum_{n>Z}r_2(n)n^{-3/4}|\Psi(\sqrt{n/T})|
 \ll_A T^{-A}.                                          \tag{16}
\]

For example, decay order \(M\) bounds this by a constant times
\(T^{M/2}Z^{1/4+\eta-M/2}\), and \(M\) can be increased.
For large \(T\), (16) is at most \(V_0/2\). Therefore, for every
\(V\ge V_0\),

\[
 |B_T|>V\quad\Longrightarrow\quad
       |H_{N,D}|>V/(2L)\text{ for at least one rectangle}. \tag{17}
\]

Apply (15) at exactly that level and sum all \(L\) rectangles.
Their logarithmic powers are absorbed by choosing \(\eta\) small
relative to the requested final \(\epsilon\). Multiplication by
\(\|w\|_\infty\) gives the conditional **full-series** distribution

\[
 D_B(V)\ll_\epsilon
   T^{1+42\rho/13+\epsilon}V^{-168/13},\quad V\ge V_0.    \tag{18}
\]

No separate mixed-block moment is discarded. The event inclusion is
used at every layer-cake level, and thus controls the full integrand:

\[
 \begin{split}
 H_{12}(T)
 &=V_0^{12}D_B(V_0)+12\int_{V_0}^{\infty}V^{11}D_B(V)\,dV\\
 &\ll_\epsilon
   T^{1+42\rho/13+\epsilon}V_0^{-12/13}
   =T^{113/125+42\rho/13+\epsilon}.
 \end{split}                                            \tag{19}
\]

The integral converges because \(168/13=12+12/13\). At
\(\rho=208/2625\), \(42\rho/13=32/125\), proving the
conditional implication (3). All sufficiently small \(T\) are
covered by the absolutely convergent coefficient bound and an enlarged
constant. This is a proved implication from (12), not a proof of (12).

### D. What the available anchored kernel estimate actually costs

Put \(\kappa=13/55\). For a nonzero argument \(u\), the accepted
unweighted kernel, followed by Abel summation through
\(h_{N,T}(dk)h_{N,T}(ek)\), gives

\[
 |\mathcal K_{d,e}(u)|\ll_\eta T^\eta
       \min\{K,\sqrt K(|u|^\kappa+|u|^{-1})\}.            \tag{20}
\]

Here the common product support is an actual interval, possibly
empty, with at most two jumps. Use auxiliary radius scale
\(T'=C T\sqrt D\) in the accepted kernel: \(|u|\le CT\sqrt D\)
and \(K\le T^{3/2}\le (T')^{3/2}\). Every source loss remains a
subpower of \(T\), since \(D\le T^{3/2}\). The case \(u=0\)
is bounded by \(K\), not by a nonzero-frequency formula.

For fixed \(j,d,e\), the minus arguments as \(l\) varies are
\(\gg K^{-1/2}\)-separated, because
\(\sqrt e\,|R_l-R_{l'}|\gg\sqrt D/\sqrt N=K^{-1/2}\).
There are \(O(1)\) closest arguments of magnitude \(\ll K^{-1/2}\).
Their trivial cost and the remaining inverse-argument harmonic sum
are \(O(K\log(2+J))\). All plus arguments are positive and
\(\asymp T\sqrt D\); they cannot be declared negligible, but
their inverse-argument contribution is bounded by the same estimate.
The \(|u|^\kappa\) term costs at most
\(J\sqrt K(T\sqrt D)^\kappa\) for each \(j,d,e\).
Summing gives the valid, insufficient bound

\[
 |\mathfrak O|\ll_\eta T^\eta
   \{JD^2K+J^2D^2\sqrt K(T\sqrt D)^\kappa\}.              \tag{21}
\]

The total logarithm is subpower since the separated set has
\(J\ll1+T\sqrt N\). Restoring \(KN^{-3/2}\) from (8)
turns (21) into exactly (4):

\[
 J^2v^2\ll_\eta T^\eta
      \{J\sqrt N+J^2T^{13/55}D^{34/55}\}.                 \tag{22}
\]

The favorable constant diagonal alone would cost
\(J\sqrt N/D\); the nearest multiplicative-radius incidences
lose that factor \(D\). In addition, the second term in (22)
could be absorbed only above its own threshold

\[
 v^2\gg T^{13/55+o(1)}D^{34/55}.
\]

At \(v\asymp V_0\) this fails even for \(D=1\), because
\(26/125<13/55\); the necessary large \(D\) from (2) only
increases its cost. On a single separated-point configuration,
different divisors still have arguments
\(R_1(\sqrt d-\sqrt e)\). Shortening the radius interval does
not turn all those arguments into differences of size equal to the
interval length. The localization maneuver used for the ordinary
difference Gram matrix cannot delete the absolute radius here.

Consequently (21) does not establish (12), including when
\(\rho=208/2625\). This computation proves insufficiency of this
specific modulus estimate. It neither asserts saturation of (21) by
the actual coefficients nor makes a lower-bound claim for H216.

### E. The unchanged complete unconditional powers

Without (12), retain both terms of the accepted distribution and its
accepted full-series ceiling \(W\ll T^{\beta+\eta}\). Exact
layer cake, including the lower boundary term, gives

\[
 H_{12}(T)\ll_\epsilon
  T^\epsilon\{W^{10}+TW^{20/13}
                      +V_0^{10}+TV_0^{20/13}\}.           \tag{23}
\]

The lower boundary powers are \(26/25\) and \(29/25\).
The two upper powers are \(10\beta\) and
\(1+20\beta/13\); both exceed \(29/25\), and the first
dominates because \(\beta>13/110\). Thus the actual certified
cost remains \(T^{10\beta+\epsilon}\). Improving or deleting
only a named diagonal does not pay the other upper contribution.

If (12) were proved with the specified loss, the accepted low-value
complement and (19) would give the complete twelfth-moment exponent
\(E(12)=29/25\). The frozen reconstruction formula gives

\[
 \Theta(12)=
 \frac{3+(1+29/25)/2}{13}=\frac{102}{325}.
\]

This restores the physical leading amplitude, the squared-radius
Jacobian and the sharp smoothing error through the permitted complete
bridge. It supplies only that conditional milestone. The full-quarter
goal still needs a sufficient complete family \(E(p)=1+o(p)\) along
unbounded fixed \(p\), or a different complete set of parents.

## 4. First doubtful or unproved step

The first missing estimate is the one-sided signed arithmetic
inequality (12), with \(\rho\le208/2625\), for the actual aligned
high-value configurations. Every term it asks to control is written
explicitly in (9)--(10). It includes the character products, the fixed
coefficient vector, all cofactor endpoints, both real cosine signs,
the possible zero minus frequencies, and the anchored nonzero
frequencies. This is not supplied by an unweighted exponent pair.

The proven scalar restriction (2) narrows the possible divisor
rectangles but does not prove this signed estimate. The only closure
attempted here is (20)--(22); it fails with the displayed complete
costs. No centered \(\ell^1\) bound, difference-only Gram estimate,
random-model exceptional-set deletion, thin-box source import, or new
unestimated geometric complement is used in its place.

The conditional input (12) is sufficient, not necessary, and its
truth has not been established. Nor does this report prove that it is
false. This scoped failure should not be promoted as a universal
no-go theorem for anchored divisor projections.

## 5. Required controls and outcomes

* **Actual coefficients:** (5) uses the exact identity
  \(r_2=4(1*\chi_4)\), with no change to any coefficient or
  physical phase. Character cancellation is discarded only in the
  explicitly labeled scalar and kernel upper estimates. There is no
  arbitrary rephasing control masquerading as an arithmetic example.
* **Absolute radius:** (9) visibly contains the two quantities (1).
  A common translation changes both in general. The failed large
  argument cost in (22) is explicitly priced, not deleted.
* **All cosine signs:** the product identity in (9) is exact and keeps
  the minus sine from the plus-plus/minus-minus part. No complex-wave
  moment is silently substituted for the physical real moment.
* **Squarefree exact/nonzero distinction:** no squarefree cutoff is
  imposed. An exact zero \(R_j\sqrt d=R_l\sqrt e\) is handled
  trivially in (20). Nearby nonzeros retain their actual sizes.
  Squarefree linear independence would not classify these real-radius
  relations or supply a finite-time estimate for them.
* **The class one and nonpairing:** every square \(n=s^2\) and every
  \(s\ge1\) is included. Nonpairing six-against-six root relations
  such as \((m,m,m,m,m,m+6)\) against six copies of \(m+1\)
  are not excluded; after squaring, their actual \(r_2\) weights
  are positive. For the anchored energy, radii \(R_j=sR_*\),
  \(R_l=tR_*\) and divisors \(d=qt^2,e=qs^2\) give an exact
  zero minus frequency. When \(q,s,t\) are odd,
  \(\chi_4(d)\chi_4(e)=1\): automatic character cancellation on
  these incidences is false. These are algebraic controls, not claims
  that the displayed radii are high values.
* **All indices and integer cutoffs:** every actual pair \(dk=n\)
  occurs once in (5). Dyadic half-open intervals, the real cutoff
  \(Z\), \(k\ge1\), \(N=D=1\), the partial top interval and
  the mandatory integer \(J\ge1\) are retained. The optional
  squarefree \(Q=\lfloor T^{2/5}\rfloor\) is not used on this
  independent route, and no conclusion about its tail is asserted.
* **High-event constants:** (17) uses the explicit level \(V/(2L)\)
  only after the uniform tail is at most \(V_0/2\). The boundary
  term in layer cake and the power of its lower limit appear in (19)
  and (23). A bound only at \(V_0\) is not substituted for bounds
  at every higher level.
* **All blocks and Schwartz tails:** (16)--(19) include the singleton,
  every effective scale, and the infinite tail. The distribution
  argument pays mixed scales without assuming that a high full sum
  makes each block high. \(\Psi\)'s possibly negative tail is
  retained in the exact coefficient and bounded only in (16).
* **Signed versus positive certificate:** \(\mathfrak Q\) is the
  nonnegative Cauchy energy; \(\mathfrak O\) is signed. Its
  constant contribution is not a lower bound on the original moment.
  Failure of (21) to imply (12) is a failure of the specified bound,
  not proof that the signed energy is large.
* **Source hypotheses:** only one primary theorem interface is used:
  the already accepted Bourgain exponent pair. The normalized phase,
  ordinary integer cofactor, large phase range, proper intervals,
  weight variation and auxiliary correlation scale are checked in
  A and D. No source statement for the weighted divisor sum is imported.
* **Real endpoints:** every radius and cutoff above can be real.
  Covering by a maximal separated set requires no integer radius and
  no unproved persistence interval. Bounded \(T\) is covered
  separately by absolute convergence.
* **Restored powers:** (8), (13)--(19), (21)--(23) retain respectively
  the Cauchy factor, integer sample count, cover width, all block
  logarithms, full event layer cake, both unweighted-kernel costs,
  and both accepted upper moment powers. The exact conditional loss
  budget is \(42\rho/13\), with threshold \(\rho=208/2625\).
* **Full-quarter scope:** even a proof of (12) at that loss proves
  only the stated \(102/325\) milestone through this fixed-order
  route. No M1, M2, GAR or endpoint parent is closed.
* **Statement-only control:** this report is claimant evidence. Its
  finite identity (9), exact support partition (5), and implication
  (12) to (19) are explicit statements available for an independent
  seam check. This task did not read a sibling report or the isolated
  blind packet and does not claim to have supplied its own independent
  validation.

## 6. Dependencies and exact artifacts used

Only the assigned brief and these permitted local files were read:

1. `protocol.md`.
2. `state/proof_obligations.yml` (the graph bytes match the starting
   hash; relevant accepted entries are the complete large-values
   kernel and the qualified Li--Yang theorem).
3. `state/active_campaign.yml` (round216).
4. `strategy/round216_actual_radical_high_values.md`.
5. `strategy/gauss_circle_strategy_checkpoint_round214_2026-09-28.md`.
6. `rounds/codex-managed/gc-complete-localized-wave-moment/synthesis.md`.
7. `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.
8. `rounds/codex-managed/gc-complete-signed-tenth-moment/reports/actual_tenth_high_values.md`.
9. `rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_arithmetic_source_gate.md`.

One primary theorem interface was checked directly:
[J. Bourgain, *Decoupling, exponential sums and the Riemann zeta
function*, arXiv:1408.5794v2, Section5, Theorem6 and the following
proper-interval discussion](https://arxiv.org/html/1408.5794v2#S6),
checked 2026-09-28. It states the exponent pair
\((13/84+\eta,55/84+\eta)\); the following discussion addresses
lengths beyond the square root of the phase parameter and proper
subintervals. This is the same source interface already accepted in
the supplied kernel. The square-root specialization and its
interpolated correlation estimate are reused with the explicit
parameter substitutions above. No claim is made that the printed
theorem directly estimates a character-weighted bilinear form.

No historical references named inside these local files were followed.
The graph was not edited, and no numerical computation or external
source other than the one specified interface was used.

## 7. Recommended state effect

**No change** to the accepted graph, proof draft, pointwise benchmark,
complete moment theorem or open parent obligations. Retain (2), the
exact anchored real energy (9), the complete conditional loss ledger
(12)--(19), and the failed absolute closure (21)--(23) as scoped
candidate method evidence. They identify a concrete arithmetic
estimate and price it; they do not establish it or count as a complete
actual high-value gain. Stop this assigned task here, without shared-
state edits or successor design.
