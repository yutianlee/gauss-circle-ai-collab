# Actual shifted correlations: two costed failures and the signed residual

Campaign: `gc-signed-near-frequency-cancellation`. Round: 210.
Task: `actual_shifted_correlations`. Role: discovery; candidate evidence only.
Generated: 2026-09-27T15:27:19Z.
Starting graph SHA-256:
`4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Effort: 100 percent analytical. No mathematical experiment or new external
theorem import. Only this assigned report is written.

## 1. Result: scoped no-go results, with no new actual bound

Two closures of actual shifted-correlations fail quantitatively.

1. One-step differencing followed by a uniform unweighted prefix-error
   estimate and absolute partial summation cannot prove the desired
   pointwise bound for the centered coefficients. Even the unrealistically
   favorable constant-size prefix error incurs incompatible costs
   \(N^{1/2}/L\) and \(TL/N\) in the squared-wave certificate. Their
   compatibility with \(T^{2b}\), \(b=83/650\), requires
   \(N\ge T^{318/325}\), outside the entire required band.
   Actual centered correlation atoms force a constant error floor against
   any continuous main term. Capping each correlation by its absolute
   coefficient sum does not repair this certificate.
2. Retaining the signed shift sum gives a legitimate complete fifth-power
   residual, but expanding its actual \(r_2r_2\) products into divisor
   pairs and taking absolute values after estimating each CRT progression
   loses every gain. Actual large-divisor pairs produce exact singleton
   progressions whose positive cost alone restores \(N^{1/2}\) in the
   squared-wave bound. The needed cancellation lies across those outer
   progressions and shifts; it has not been established.

These are lower bounds on specified **positive certificates**, not on an
actual oscillatory correlation or moment. They do not rule out signed
arithmetic dispersion. Formula (12) below is the complete remaining
sufficient signed estimate for this differencing route. Merely obtaining
that formula is not a new arithmetic gain.

## 2. Exact statements, coefficients, and hypotheses

Use the supplied actual block, fixed smooth mask and mollifier:

\[
 I=[T/\sqrt2,\sqrt3T],\quad
 f_N(t)=t^{-3/4}\Psi(\sqrt{t/T})v(t/N),\quad
 F_c(R)=\sum_n c_nf_N(n)e(R\sqrt n),                         \tag{1}
\]

where \(T\ge2\) is real, \(v\) is fixed real smooth, nonzero, and
supported in \([1,4]\), and \(\Psi\) is the supplied fixed real
mollifier transform with \(\Psi(0)=1\). Either
\(c_n=r_2(n)\) or \(c_n=r_2(n)-\pi\). The original physical block is
\(H_N=\Re(e(-3/8)F_{r_2})\). In this report

\[
 b=83/650,\quad \gamma=10b=83/65,\quad
 T^{166/325}<N<T^{242/325},\quad U=T^\gamma N^{-1/2}.        \tag{2}
\]

A complex pointwise bound \(|F_c|\ll T^{b+\varepsilon}\), or a
complex tenth moment \(\int_I|F_c|^{10}\ll UT^\varepsilon\) with
the supplied reproduction argument, suffices for the associated real
block. These are sufficient, possibly stronger, routes. For centered
coefficients the reviewed discrete mean wave is already pointwise
\(O(T^{303/4550+\varepsilon})\), so a centered pointwise result would
give the milestone. Its moment is not identified with the original
moment or with the unmodified signed shell.

For an integer \(1\le L\le N\), zero-extend the full coefficient
sequence and define

\[
 \begin{split}
 D&=\sum_n c_n^2f_N(n)^2,\\
 C_h(R)&=\sum_n c_nc_{n+h}f_N(n)f_N(n+h)
                 e(R(\sqrt{n+h}-\sqrt n)),\\
 S_L(R)&=2\Re\sum_{1\le h<L}(1-h/L)C_h(R),\qquad
 Q_L(R)=D+S_L(R).
 \end{split}                                               \tag{3}
\]

All sums in (3) use both exact smooth factors and their complete overlap.
No mean subtraction, endpoint trimming, or shift complement is implicit.
The divisor bound and a fixed interior subband give

\[
 c_vN^{-1/2}\le D\ll_\varepsilon N^{-1/2+\varepsilon}.      \tag{4}
\]

For centered coefficients the lower bound follows from
\(|r_2(n)-\pi|\ge4-\pi\). For original coefficients it follows by
Cauchy from the actual summatory formula on the interior subband.

## 3. Derivation and the two mechanisms

### Common exact differencing interface

Write \(z_n=c_nf_N(n)e(R\sqrt n)\), supported on a contiguous ambient
integer interval of length \(K\le3N+2\), and let
\(B_m=\sum_{j=1}^Lz_{m+j}\). Then
\(\sum_mB_m=LF_c\), and at most \(K+L-1\) of the \(B_m\) are
nonzero. Expanding their squares gives the exact identities and inequality

\[
 Q_L=L^{-1}\sum_m|B_m|^2\ge0,\qquad
 |F_c|^2\le\frac{K+L-1}{L}Q_L\ll\frac NL Q_L.              \tag{5}
\]

This proves (5) with all shifts and integer endpoints present. Shifts
\(h\ge L\) are not an unestimated omitted part of \(|F_c|^2\):
the price of passing to the complete moving sums is exactly \(N/L\).
The choice \(L=1\) gives only the diagonal/trivial certificate.

### Mechanism one: unweighted correlation information transported by Abel summation

Put \(d_h(n)=c_nc_{n+h}\),
\(W_h(t)=f_N(t)f_N(t+h)\), and
\(\phi_h(t)=R(\sqrt{t+h}-\sqrt t)\). Suppose an unweighted prefix
description on the full overlap has the form

\[
 \sum_{N\le n\le x}d_h(n)=\mu_h(x-N)+E_h(x),\qquad
 \sup_x|E_h(x)|\le\mathcal E_h.                            \tag{6}
\]

Changing an endpoint convention only changes the remainder, not the
following conclusion. No theorem providing (6) with a small error is
imported or assumed true here. It is the exact proposed source interface.

For \(1\le h\le N\) on the overlap, uniformly for \(R\in I\),
\(|\phi_h'|\asymp ThN^{-3/2}\). Smooth mask derivatives satisfy the
corresponding scaled bounds. Since the exterior smooth boundaries vanish,
Abel summation gives

\[
 \begin{split}
 C_h(R)&=\mu_h\int W_h(t)e(\phi_h(t))\,dt
                    -\int E_h(t)\,d\{W_h(t)e(\phi_h(t))\},\\
 |C_h-\mu_h\mathcal I_h|
 &\ll\mathcal E_h N^{-3/2}(1+Th/\sqrt N),\\
 |\mathcal I_h|&\ll_A N^{-1/2}(1+Th/\sqrt N)^{-A}.
 \end{split}                                               \tag{7}
\]

The last estimate follows by repeated *continuous* integration by parts,
not a first-derivative assertion for a discrete exponential sum. The
normalized continuous phase has derivative bounded away from zero at
scale \(Th/\sqrt N\). Thus a polynomially bounded correlation mean is
harmless here. For the no-go result we grant its entire contribution free.

Centering does not in general set \(\mu_h\) to zero. Expanding
\((r_2(n)-\pi)(r_2(n+h)-\pi)\) shows that a hypothetical original
mean \(\rho_h\) becomes \(\rho_h-\pi^2\), with the two ordinary
summatory discrepancy errors also restored. No specific singular-series
formula is needed or asserted.

The variation cost in (7) cannot be suppressed while using only a uniform
prefix error. To quantify this, choose a fixed interior interval where
\(|v|\) is bounded below and has constant sign. There is a fixed
\(\delta>0\) such that, for \(1\le h\le\delta N\), its common
interior overlap has length comparable to \(N\) and
\(|W_h|\gg N^{-3/2}\). Since \(W_h\) is real,

\[
 |(W_he(\phi_h))'|
 =\sqrt{(W_h')^2+4\pi^2(W_h\phi_h')^2}
 \ge2\pi|W_h\phi_h'|.
\]

Consequently the actual variation appearing in the uniform-error
certificate is \(\gg ThN^{-2}\). The error is not necessarily largest
where the variation is largest; using their product is precisely the
information loss under examination.

For centered coefficients every jump in the prefix sum in (6) has
modulus at least \((4-\pi)^2\). A continuous main term cannot remove
that jump, so its remainder's supremum over real prefixes is at least
\((4-\pi)^2/2\). This statement holds for every shift with a nonempty
interior overlap, independently of signs. Therefore the positive
diagonal-plus-uniform-error certificate from (5)--(7) has at least the
following two costs, up to fixed constants:

\[
 \boxed{\quad N^{1/2}/L\quad\hbox{and}\quad TL/N.\quad}     \tag{8}
\]

For the second bound sum shifts in a fixed positive proportional subrange
of \([1,L]\) contained in \([1,\delta N]\), where the Fejer weights
are bounded below. There are comparable to \(L\) such shifts and their
sum is comparable to \(L^2\). The finitely bounded small choices of
\(L\) already fail through the first term at each fixed interior
exponent in (2).

Even allowing the estimate for each correlation to be capped by its
absolute coefficient sum gives the positive lower cost

\[
 N^{1/2}/L+\min(N^{1/2},TL/N).                             \tag{9}
\]

Indeed the centered absolute coefficient sum is itself
\(\gg N^{-1/2}\) on the same overlap, while the uniform-error times
variation certificate is \(\gg ThN^{-2}\). Take the better of these
two certificates shift by shift, then the same proportional shift range.
For a fixed interior exponent \(\alpha>4b\), the \(N^{1/2}\) cap
already exceeds the desired \(T^{2b}\). The other branch would require

\[
 L\gtrsim N^{1/2}T^{-2b},\qquad
 L\lesssim NT^{2b-1},\qquad
 N\gtrsim T^{2-8b}=T^{318/325}.                            \tag{10}
\]

The last inequality contradicts (2) by a fixed exponent margin. Arbitrarily
small epsilon losses do not repair it. This is a no-go for the stated
positive certificate, even with a free mean term and the smallest possible
prefix-error order. In particular a hypothetical square-root error would
not suffice. It is not a claim that the actual error integral in (7) is
large. Keeping its oscillation or its correlation with its local error is
exactly how an argument would have to bypass (10).

### Mechanism two: preserve the signed aggregate, then try the actual divisor-pair expansion

Keep \(S_L\) signed before the fifth power. From (5),

\[
 \int_I|F_c|^{10}\ll(N/L)^5\int_I Q_L^5.
\]

For an explicit sufficient split, \(Q_L\le D+(S_L)_+\), hence

\[
 \int_I|F_c|^{10}
 \ll_\varepsilon T^\varepsilon TN^{5/2}L^{-5}
                 +(N/L)^5\int_I(S_L)_+^5.                 \tag{11}
\]

Thus a complete sufficient estimate, with independently adjustable epsilon
losses, is

\[
 \begin{gathered}
 L\gtrsim T^{-18/325}N^{3/5},\qquad L\le N,\\
 \boxed{\displaystyle
 \int_I(S_L(R))_+^5\,dR
       \ll_\varepsilon T^{83/65+\varepsilon}L^5N^{-11/2}.}
                                                               \tag{12}
\end{gathered}
\]

The displayed lower scale for \(L\) pays the complete separated diagonal
in (11). It lies strictly between a positive power of \(T\) and \(N\)
throughout (2), so it is an available cutoff, not an empty range.
An estimate directly on \(Q_L^5\) might use negative correlations to
cancel part of the diagonal and need not obey this separated-diagonal
criterion. Neither (12) nor that stronger signed treatment is established.

The substantive attempted input to (12) is the exact arithmetic identity

\[
 C_h(R)=16\sum_{d,e\le4N}\chi_4(d)\chi_4(e)
 \sum_{\substack{n\ge1\,;\ d\mid n,\ e\mid n+h}}
           W_h(n)e(\phi_h(n))                              \tag{13}
\]

for \(c_n=r_2(n)\). The inner progression exists only when
\((d,e)\mid h\), and its modulus is \([d,e]\). Every divisor,
including moduli larger than the support, is present. Equation (13)
holds with the original weights before any average over shifts or radius.

Trying to get cancellation on each inner progression and then using an
absolute outer sum fails on an actual complete family of singletons.
Shrink the fixed \(\delta\) above if necessary so \(\delta<1/10\).
For any even \(2\le h\le\delta N\), take odd integers \(n_0\) in
the common interior subband and put \(d=n_0\), \(e=n_0+h\). Then

\[
 [d,e]=\frac{n_0(n_0+h)}{(n_0,h)}\ge\frac{N^2}{h}>3N,
 \qquad
 \chi_4(d)\chi_4(e)=(-1)^{h/2}.                            \tag{14}
\]

The full inner support has length at most \(3N\), so that progression
contains exactly the single point \(n_0\). Its weighted oscillatory sum
has modulus \(|W_h(n_0)|\gg N^{-3/2}\) for every real \(R\).
There are comparable to \(N\) such odd \(n_0\), each corresponding
to a distinct divisor pair. Therefore even the sum of the **exact moduli**
of these inner progression sums is \(\gg N^{-1/2}\) for each such
even shift. No better estimate for an individual progression can reduce it.

For growing \(L\le N\), the small even shifts with Fejer weights
bounded below have cardinality comparable to \(L\), after taking a
fixed proportional range as above. Consequently this outer-absolute
closure has

\[
 S_L^{\mathrm{abs}}\gg LN^{-1/2},\qquad
 (N/L)S_L^{\mathrm{abs}}\gg N^{1/2}.                       \tag{15}
\]

It yields no pointwise improvement over \(|F|\ll N^{1/4+\varepsilon}\)
on any fixed interior scale. Its fifth-power positive certificate has

\[
 (N/L)^5\int_I(S_L^{\mathrm{abs}})^5\gg TN^{5/2},
 \quad
 \frac{TN^{5/2}}{U}=T^{-18/65}N^3,                         \tag{16}
\]

again too large throughout (2). Expanding centered products into their
\(r_2r_2\), two linear, and constant pieces and taking their separate
absolute values retains the same obstruction from the first piece.
This does not refute a genuinely combined centered expansion.

The constant character sign in (14) makes the lost information especially
explicit: this part cannot be saved by claiming independent character
orthogonality in its divisor labels. Its phases still vary with \(n_0\),
and cancellation across the singleton progressions could be real.
Preserving that outer oscillation, jointly with all remaining divisor
pairs and shifts, is unproved at (12). No nonexistent small-modulus
complement is delegated to later work.

### Complete physical and pointwise ledger

No estimate obtained here improves the inherited complete certificate

\[
 M_{10}(H_N)\ll T^\varepsilon
       (TN^{-3/110}+T^{8\omega}),\qquad
 \omega=\min(\alpha/4,\beta,(1-\alpha)/2).
\]

Both terms remain. In particular the first still fails the required gate
when \(\alpha>99/169\); deleting the second alone is insufficient.

For the original real block, the supplied complete shell bridge retains

\[
 M_{10}(H_N)\ll T^{-6}K_{10}+T^{-4+\varepsilon}N^{-10}
                    +O_A(T^{-A}),
\]

and the reverse bound has \(T^6M_{10}\) and
\(T^{2+\varepsilon}N^{-10}\). Thus an actual success here would meet
the stated \(K_{10}\) scale \(T^{473/65+\varepsilon}N^{-1/2}\).
These formulas use the complete centered shell, both arms, actual varying
width and all prefixes; no alternative shell representation is introduced.

Local reproduction keeps \(N^{1/20}\), the positive margin from
\([T,\sqrt2T]\) to \(I^c\), and the global coefficient bound for
the off-window tail. The complements \(N\le T^{4b}\) and
\(T^{1-2b}\le N\le T\), including equality endpoints, have the
supplied bounds \(N^{1/4}\) and \((T/N)^{1/2}\). The singleton,
complete \(N\ge T\) tail, logarithmic block sum, \(\sqrt R\)
reconstruction factor and \(O(T^{1/2+\varepsilon})\) sharp error are
unchanged and paid by that bridge. For a centered success one instead
reproduces the centered block and restores the reviewed safe mean wave.
Either successful sufficient route would imply only \(102/325\).

## 4. First doubtful or unproved step

There is no asserted small-error shifted-correlation theorem to audit.
The exact identity (7) is valid; its absolute uniform-error closure is
quantitatively inadequate by (10), even after granting a free mean and
constant-size errors at the atom scale. A new bound must retain the oscillation of
the error integral rather than its supremum times variation.

For the second mechanism the first unproved input is (12), or an adequate
direct bound for \(\int Q_L^5\), for the actual complete coefficient
vector on the displaced window. Formula (13) does not provide it.
Bounds obtained by estimating each progression separately and taking
absolute outer sums fail by the actual singleton family (14)--(16).
No claim is made that this blocks a signed outer dispersion estimate.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `actual_coefficients` | Passed for the scoped statements: centered jump sizes use the exact \(4\mathbb Z\) property; singleton pairs use actual divisors and their exact \(\chi_4\) values. |
| `complete_scales` | The full open band (2), all integer cutoffs \(1\le L\le N\), and the complete inherited two-term moment bound are retained. Bounded cutoffs fail by their diagonal; growing cutoffs obey the displayed obstructions. |
| `signed_absolute_distinction` | Every lower bound concerns the stated positive certificate. Neither \(S_L^{\rm abs}\) nor the sup-error product lower-bounds a signed correlation. The residual (12) keeps \(S_L\) signed until its positive part. |
| `exact_nonpairing_relations` | Equations (3), (5), and (13) are full finite identities, with no pairing restriction in any fifth-power expansion. The inherited exact mass is not reestimated or discarded. As a finite control, roots \((m,m,m,m,m+5)\) and \((m+1,m+1,m+1,m+1,m+1)\) sum equally and give a nonpairing ten-root relation with positive actual square coefficients; nothing here removes it. |
| `real_endpoints` | Prefix suprema are over real prefixes, which is essential for the jump argument. Radius endpoints and \(T\) are real; smooth overlap boundaries vanish. Fejer moving sums use exact integer endpoints and zero extension. |
| `all_costs_restored` | The \(Th/\sqrt N\) variation, diagonal, \(N/L\) loss, correlation mean, small and large moduli, every shift in the moving-sum identity, fifth-power diagonal, reproduction, shell conversion and sharp reconstruction are explicit. |
| `full_quarter_scope` | No new moment, pointwise exponent, M1/M2 closure, or quarter theorem. A successful missing input would give only the stated intermediate milestone. |
| `statement_only_control` | Not claimed by this discovery report. No other current task report or isolated packet was read. The jump/variation lemma, CRT singleton family and powers (10)--(12) require the conductor's separate independent seam check. |

No mathematical numerical test was run or used as certification.

## 6. Dependencies and exact artifacts used

- `protocol.md` and the assigned
  `rounds/codex-managed/gc-signed-near-frequency-cancellation/briefs/actual_shifted_correlations.md`.
- `state/active_campaign.yml` for Round210 and selected relevant nodes
  of `state/proof_obligations.yml`: `GC-target`, `M9-M1`, `M9-M2`, and
  `GC-complete-square-root-large-values-moment-bound`, plus the graph's
  introductory authority/dependency definitions.
- `strategy/round210_signed_near_frequency_attack.md` and
  `strategy/gauss_circle_strategy_checkpoint_round208_2026-09-27.md`.
- `rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md`.
- `rounds/codex-managed/gc-complete-signed-tenth-moment/synthesis.md`.
- `rounds/codex-managed/gc-complete-signed-tenth-moment/reports/actual_tenth_high_values.md`.
- `rounds/codex-managed/gc-complete-signed-tenth-moment/reviews/independent_high_values_review.md`.
- `rounds/codex-managed/gc-complete-signed-tenth-moment/controls/conductor_tenth_power_ledger.md`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.

The conductor independently communicated the centered atom diagnostic
and compatibility exponent after my interim finding on the full
phase-variation cost; both are derived here. No external source mentioned
in these files was separately opened or imported. No new shifted-correlation
asymptotic, singular-series formula, or weighted exponent-pair theorem is
asserted. Finite moving-sum algebra, Abel summation, continuous integration
by parts, CRT and the divisor identity suffice for the new scoped results.

## 7. Recommended state effect

**No change** to the accepted graph, proof draft, complete moment or
pointwise benchmark. Retain the two precisely scoped actual-arithmetic
failures, after independent review, as reasons to reject the corresponding
positive closures. Keep (12), or an adequate complete signed alternative,
open. Do not promote the differencing identity as arithmetic progress or
infer a lower bound for the actual signed moment from (8), (15), or (16).
This task stops after its assigned report; no shared state, synthesis or
successor is edited.
