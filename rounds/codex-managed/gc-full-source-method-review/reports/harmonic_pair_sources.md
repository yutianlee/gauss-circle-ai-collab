# Round 211: actual hyperbola sums and current exponent-pair sources

Campaign: `gc-full-source-method-review`. Task: `harmonic_pair_sources`.
Role: source auditor; selected-context, nonblind candidate evidence.
Generated: 2026-09-27T15:56:01Z; primary records checked 27 September 2026.
Graph SHA256: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Effort: analytical/algebraic/source inspection 100%; numerical experiments 0%.
Only this assigned report is written. No shared-state or successor action.

## 1. Result: a complete transfer and a bounded-inventory certificate failure

Expanding the actual coefficient before applying an exponent pair is lawful.
Both divisor arms, including the character in the second arm, give the
following complete physical-block bound for a fixed admissible pair
\((k,\ell)\), at epsilon-loss level:

\[
 |H_N(R)|\ll_\epsilon T^\epsilon
       \min\{N^{1/4},\ T^kN^{\ell/2-1/4}\},
 \qquad R\asymp T,\quad 1\le N\le T.                 \tag{P1}
\]

This is an upper bound, not a lower bound on an actual block. In particular,
the accepted Bourgain pair supplies only
\(T^{13/84+\epsilon}N^{13/168}\) in (P1). Applying that same pair directly
to the weighted n-sum would omit an outer factor and is not justified.

There is a rigorous algebraic failure certificate for a **named inventory
closure**, without sampling pairs numerically. Let \(\mathcal C\) be the
convex closure, under the standard A, B and C maps and the formal D map
specified below, of the explicit Trudgian--Yang polygon generators, the four
Tao--Trudgian--Yang pairs, and the two Cushing pairs listed by the
author-maintained ANTEDB. Then

\[
 2k+\ell\ge8/9,\qquad k+2\ell\ge25/18
 \quad ((k,\ell)\in\mathcal C).                       \tag{P2}
\]

Consequently every (P1) pair exponent in that closure satisfies, for
\(N=T^\alpha\), \(0\le\alpha\le1\),

\[
 e_{k,\ell}(\alpha):=k+\alpha(\ell/2-1/4)
       \ge 7\alpha/36.                                \tag{P3}
\]

At the fixed interior scale \(\alpha=7/10\), this is \(49/360\), exceeding
both \(b=83/650\) and the accepted \(\beta=2\theta_{LY}-1/2<13/100\).
The trivial and large-N complementary certificates there are respectively
\(7/40\) and \(3/20\), also greater than \(\beta\). Thus this complete
outer-absolute exponent-pair method, even optimistically granted every
pair in this closure, improves neither the current pointwise exponent nor
the selected \(102/325\) milestone. The positive gap above b is exactly
\(197/23400\) at this test scale. Dyadic rounding changes no exponent.

This is not a claim about all admissible exponent pairs, all consequences
of the database, all phase-specific methods, or the actual size of H_N.
For example, the conjectural pair \((0,1/2)\) lies outside (P2) and would
make (P1) sufficient for the quarter theorem after known reconstruction.
The database's additional beta-function operations and other possible
new sources are not covered by the explicitly defined closure.

The current bounded primary search found no newly verified complete
Gauss-circle estimate to replace the graph's repaired Li--Yang benchmark.
This is a dated corpus statement, not an exhaustive literature assertion.

## 2. Exact statements, conventions, and two source interfaces

Retain the fixed mollifier and dyadic partition from the permitted context.
For real T>=2 and real R in a fixed positive compact multiple of T, define

\[
 w_{T,N}(x)=x^{-3/4}\Psi(\sqrt{x/T})v(x/N),\quad
 S_N(R)=\sum_{n\ge1}r_2(n)w_{T,N}(n)e(R\sqrt n),\quad
 H_N(R)=\Re(e(-3/8)S_N(R)).                            \tag{P4}
\]

Here v is fixed smooth and supported in [1,4], and Psi is the fixed even
Schwartz function from the physical reconstruction. The argument also
permits restriction to any real product interval before summation. Its
endpoints are kept exactly. For N<=T, every fixed derivative order j obeys

\[
 \sup_{x\asymp N}|w_{T,N}^{(j)}(x)|\ll_j N^{-3/4-j}.
                                                               \tag{P5}
\]

The actual identity used is \(r_2(n)=4\sum_{d\mid n}\chi_4(d)\), with
chi4 zero on even d and +1,-1 on residues 1,3 modulo 4. No theorem for
arbitrary n-weights is assumed.

Our exponent-pair convention is

\[
 \left|\sum_{m\in I}e(A F(m/K))\right|
    \ll_\epsilon (A/K)^kK^\ell A^\epsilon,
 \quad A\ge K\ge1,\quad I\subset[K,2K],              \tag{P6}
\]

for the appropriate fixed monomial derivative class. Bounded factors in
A and K and logarithmic partial-interval losses are allowed. It is
\((A/K)^kK^\ell\), not \(A^kK^\ell\). All parameters used below are bounded
by fixed powers of the physical T, so source epsilon losses are absorbed
by choosing a smaller input epsilon.

**Interface I: Bourgain.** [arXiv:1408.5794v2](https://arxiv.org/html/1408.5794v2#S6),
version dated 22 February 2016, Section 5, Theorem 6, states the pair
\((13/84+\epsilon,55/84+\epsilon)\). The surrounding proof explicitly
handles lengths up to the phase parameter and proper subintervals, with
a logarithmic loss. We use that global theorem, not Theorem 4's shorter
direct range. Its monomial derivative class includes f'(x)=y x^(-1/2)
and sufficiently small fixed-order derivative perturbations. The square-root
specialization and the residue shifts are checked below. This is a fresh
statement/application audit of an already accepted source, not a reproof
of its Bombieri--Iwaniec argument.

**Interface II: Tao--Trudgian--Yang.** [arXiv:2501.16779v1](https://arxiv.org/html/2501.16779v1),
28 January 2025, Theorem 20, gives

\[
 (89/1282,997/1282),\quad(652397/9713986,7599781/9713986),
\]
\[
 (10769/351096,609317/702192),\quad(89/3478,15327/17390).
                                                               \tag{P7}
\]

Definitions 5 and 11 and Lemma 12 specify (P6) for intervals and model
phases: for a fixed sigma>0, all fixed derivatives of F' approach the
corresponding derivatives of u^(-sigma) on [1,2]. The finite-epsilon
form requires sufficiently close finitely many derivatives. Here sigma=1/2.
The official record has only v1; a guessed v2 URL returned 404 and is
not a source. No logarithmic-phase or arbitrary-weight generalization is
imported. Its theorem proof is external; this audit checks the exact
statement, class, normalization and complete application costs.

These are the only two full exponential-sum application audits. The
polygon and Cushing material in Section 3 is an inventory screen and an
optimistically enlarged algebraic comparison, not a third imported
exponential-sum theorem.

## 3. Proof and complete cost ledger

### Exact hyperbola split

For any real 1<=D<=N, write E(n)=w_{T,N}(n)e(R sqrt(n)). Then exactly

\[
 S_N(R)/4=
 \sum_{d\le D}\chi_4(d)\sum_{m\ge1}E(dm)
 +\sum_{m\le4N/D}\sum_{d>D}\chi_4(d)E(dm).            \tag{P8}
\]

The support of w is understood in both arms. The first uses d<=D;
the second uses d>D. Thus a lattice point at an integer cutoff is neither
omitted nor counted twice. The upper m bound in the second arm follows
from dm<=4N and d>D; writing it weakly merely includes possible zeros.
Further real product cutoffs give intervals in each inner variable.

For a fixed first-arm d, inner m lies in [N/d,4N/d]. Split into boundedly
many dyadic intervals with ambient K comparable to N/d. Its phase equals
A F(m/K), with

\[
 A=R\sqrt{dK}/2\asymp T\sqrt N,
 \qquad F(u)=2\sqrt u.                                \tag{P9}
\]

Every derivative of F' is exactly that of u^(-1/2). Moreover
A/K is comparable to T d/sqrt(N), hence exceeds a fixed positive
multiple of sqrt(T) for 1<=N<=T. After enlarging bounded-T constants,
the source range A>=K is satisfied for every first-arm row. This
includes its most unbalanced d=1 row; no unstated lower bound on d
is needed. A term with bounded K is also covered by the trivial bound.

Abel summation against w(dm) costs only N^(-3/4): its supremum plus
its variation in m is O(N^(-3/4)) by (P5). The oscillation stays inside
the exponential sum; differentiating the exponential as part of the
amplitude would produce a spurious large cost. Therefore each first-arm
row costs

\[
 T^{k+\epsilon}N^{\ell-k/2-3/4}d^{k-\ell}.           \tag{P10}
\]

For the second arm, fix m and split d>D into comparable dyadic intervals
of scale K comparable to N/m. Decompose chi4(d) into d=4j+1 and d=4j+3,
with signs +1 and -1. On a dyadic j interval of scale K' comparable to
K/4, the exact phase is A' F_r(j/K'), where

\[
 A'=R\sqrt{4mK'}/2\asymp T\sqrt N,
 \quad F_r(u)=2\sqrt{u+r/(4K')},\quad r=1,3.           \tag{P11}
\]

For every fixed p,
\(F_r^{(p+1)}(u)-(d/du)^p u^{-1/2}=O_p(1/K')\), uniformly on [1,2].
Thus unbounded K' is in the source model class. Bounded K' is paid
trivially with a constant depending only on the required derivative
tolerance. This is a hypothesis check for the exact shifted phase;
we do not replace its exponential by the unshifted exponential. In
particular no smallness of A'/K' is assumed. The source range follows
from A'/K' comparable to T m/sqrt(N), again large. Restrictions d>D,
the product support, and an optional real endpoint remain partial
intervals in j. No completion to a long unrestricted progression is needed.

The factor 4 in d=4j+r changes lengths and derivatives by fixed constants
only. Abel variation is still O(N^(-3/4)). Taking the two residue-class
moduli gives the same row price as (P10), with m in place of d. The
plus/minus relation between the residues is not credited as a saving.

Put q=1+k-l, so q>=0 in the standard triangle. Summing the two arms
absolutely in their outer variables gives

\[
 |S_N(R)|\ll_\epsilon
 T^{k+\epsilon}N^{\ell-k/2-3/4}
       \{D^q+(N/D)^q\}.                               \tag{P12}
\]

For q=0 the harmonic logarithms are included in T^epsilon. For q>0
the expression is minimized at D=sqrt(N), up to fixed constants. Then
\(\ell-k/2-3/4+q/2=\ell/2-1/4\), proving (P1); the other term of
the minimum follows directly from the divisor bound. Both arms have
the same price. Omitting the second arm would make an artificially
small D appear favorable and is an invalid optimization.

The ledger therefore pays, in order: the true divisor coefficient,
inner phase scale A~T sqrt(N), inner length K~N/d or N/m, partial
intervals, residue-four shifts, smooth variation N^(-3/4), the full
outer sums, the optimal cutoff, and the real-part projection to H_N.
It uses the actual character algebra to justify the unweighted inputs,
but discards outer signed cancellation at the last step.

### An exact algebraic inventory closure

Define Q inside the standard pair triangle by (P2). Its seed set consists
of the endpoints (0,1),(1/2,1/2), the five rational points

\[
 (13/84,55/84),\ (4742/38463,35731/51284),\
 (18/199,593/796),\ (2779/38033,58699/76066),\
 (715/10238,7955/10238),                               \tag{P13}
\]

and the infinite sequence

\[
 p_m=\frac2{(m-1)^2(m+2)},\quad
 q_m=1-\frac{3m-2}{m(m-1)(m+2)},\qquad m\ge5.         \tag{P14}
\]

The [Trudgian--Yang v3](https://arxiv.org/html/2306.05599v3), 15 July 2024,
Definition 1.2, equations (1.9),(1.14), describes its polygon using these,
the A-images of four points, and B-reflections. Theorem 1.3 describes the
then-known inventory. We use the displayed generators only; its historical
claim is not a claim that this polygon exhausts today's sources.

Add (P7), and optimistically add

\[
 (311/4822,3799/4822),\quad(80219/1298878,515638/649439).
                                                               \tag{P15}
\]

These are labeled Cushing (2025), Theorem 5.23, in the
[author-maintained ANTEDB chapter](https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html),
checked 27 September 2026. That live page has no fixed arXiv version;
the report records exactly the two displayed pairs. Their implementation
was not run or independently audited. Granting them only strengthens
the method being tested, so the negative comparison does not require
their theorem status to be promoted. Likewise we grant the formal D
map below even where extra beta-function conditions would be required.

Every finite seed in (P7),(P13),(P15) satisfies the stronger rational
inequalities 2k+l>=9/10 and k+2l>=7/5 by cross multiplication. For
(P14), q_m>=127/140>8/9 for m>=5, and hence 2q_m>25/18. To see the
first inequality directly, its cleared numerator is

\[
 13m(m-1)(m+2)-140(3m-2)
       =(m-5)(13m^2+78m-56)\ge0.
\]

Thus all seeds lie in Q. No finite truncation of the infinite polygon
or numerical minimizer is being used.

Here are the maps defining our comparison closure:

\[
 A(k,l)=\left(\frac{k}{2k+2},\frac{k+l+1}{2k+2}\right),
 \quad B(k,l)=(l-1/2,k+1/2),
\]
\[
 C(k,l)=\left(\frac{k}{12(1+4k)},
                   \frac{11}{12}+\frac{l}{12(1+4k)}\right),
\]
\[
 D(k,l)=\left(\frac{5k+l+2}{8(5k+3l+2)},
                   \frac{29k+21l+10}{8(5k+3l+2)}\right).        \tag{P16}
\]

These rational maps preserve the standard triangle. Convexity preserves
Q, and B interchanges its two inequalities. For A, the two new slacks
are

\[
 \frac{11k+9l-7}{18(k+1)},\qquad
 \frac{2k+18l-7}{18(k+1)}.
\]

The second is positive since l>=1/2. For the first,

\[
 11k+9l=\tfrac{13}{3}(2k+l)+\tfrac73(k+2l)
      \ge383/54>7.
\]

For C its second coordinate is at least 11/12, which immediately
proves both inequalities. For D the cleared numerators of the two
slacks, with positive denominators suppressed, are

\[
 31k+15l-2,\qquad134k+174l-4,
\]

both positive throughout the standard triangle. This proves Q-invariance
under the entire named closure, including any number of iterations and
convex limits. It does not assert that formal D always gives an admissible
pair; admitting it is an optimistic enlargement for this obstruction.

Finally,

\[
 e_{k,l}(\alpha)
   =\frac\alpha2(2k+l)-\frac\alpha4+(1-\alpha)k
   \ge\frac{7\alpha}{36},
\]

which proves (P3). It is already above b whenever
alpha>1494/2275, strictly within the required band below 242/325.

An unbalanced hyperbola cutoff, or choosing a different pair per row,
does not bypass this certificate on the balanced physical rectangle.
Where d and m are both comparable to sqrt(N), each nonempty full-scale
row has length comparable to sqrt(N) and phase scale comparable to
T sqrt(N). There are comparable to sqrt(N) such rows in one or both
arms. Any D partitions that rectangle between the two arms; at least
one side retains a fixed positive proportion of its rows and product
interval length, after a bounded further partition. The unweighted
row certificate, even capped by the trivial row length, pays at least
the exponent in (P3) after N^(-3/4) normalization. Here "pays at least"
means the **numerical upper certificate assigned by this procedure**, not
the value of the row sum. If the smooth partition is nonzero, choose a
fixed interior product interval on which its amplitude has a fixed
nonzero size; the cutoff is then handled by the same variation norm.
For the actual stress scale alpha=7/10, Psi(sqrt(n/T)) tends uniformly
to Psi(0)=1 on the support, so this choice has a uniform nonzero amplitude
on an interior interval where v is nonzero. The argument is not a lower
bound for the physical signed sum and does not rule out a method retaining
outer character cancellation.

### Reconstruction, complements, and the full frontier

The permitted conductor ledger supplies, for H_N on the physical window,
the existing envelope

\[
 |H_N|\ll T^\epsilon\min\{N^{1/4},T^\beta,(T/N)^{1/2}\},
 \quad 1\le N\le T,
\]

and the fully summed N>=T tail is O(T^epsilon). The singleton is O(1).
Thus the only possible new pointwise certificate from this application
adds e_(k,l)(alpha) to this minimum. At alpha=7/10, beta is the strict
minimum: beta<13/100<49/360<3/20<7/40. The exact inequality beta<13/100
follows, for example, from sqrt(1717)<83/2 and
1778/13762<13/100. Hence the worst complete bound still has a scale
costing T^beta. This blocks a new complete pointwise exponent from the
audited certificate; it is not evidence of a peak of that size.

With all dyadic sums, the two cosine phases, tail and real endpoints
restored, the known relation is

\[
 P(R^2)=\pi^{-1}\sqrt R\sum_NH_N(R)
                 +O(T^{1/2+\epsilon}).                \tag{P17}
\]

A complete T^b block estimate on T^(4b)<N<T^(1-2b), together with
the already paid outer scales, would give P(x)<<x^(1/4+b/2+epsilon).
For b=83/650 this is 102/325, not quarter. No such estimate is proved
here. A new coefficient-sensitive sufficient alternative, stated without
discarding either arm, is

\[
 \left|\sum_{d,m\ge1}\chi_4(d)\,V_{T,N}(dm)
                  e(R\sqrt{dm})\right|
      \ll T^{b+\epsilon}N^{3/4},
 \quad V_{T,N}(x)=N^{3/4}w_{T,N}(x),                  \tag{P18}
\]

for every middle scale and real R~T. This complex estimate is sufficient
and stronger than a bound only for its required real part. It is an open
actual-coefficient estimate, not a conclusion of an exponent-pair source.
For b tending to zero the direct physical version must cover each enlarged
band; alternatively, (P18) with b=0 and epsilon losses for all 1<=N<=T
would give quarter using (P17). No extension of the narrower signed-shell
bridge is silently assumed.

The existing signed tenth-moment route remains independent and complete:

\[
 M_{10}(H_N)\ll T^{83/65+\epsilon}N^{-1/2},
 \quad T^{166/325}<N<T^{242/325}.                     \tag{P19}
\]

Its equivalent signed-shell target has factor T^6 restored, namely
T^(473/65+epsilon)N^(-1/2). The inherited upper bound still contains both
T N^(-3/110) and T^(8 omega), omega=min(alpha/4,beta,(1-alpha)/2).
This source application proves no improvement to either term. A pointwise
bound for each unweighted divisor row does not itself supply a signed
tenth correlation theorem. Round210's XH^9 bin price and the absolute
Abel/CRT failures remain method evidence, not actual signed lower bounds.

Neither (P1) nor (P18) closes an internal M1/M2 node. The graph still has
direct M1 HARD and SMOOTH, M2 TOP/BAL/UNBAL and endpoint uniformity open;
the alternative GAR route still needs its complete total-M1 statement and
M2. A fixed tenth milestone does not close the full moment hierarchy.

## 4. First doubtful or unproved step

For (P1) the external source theorem is used precisely in its model-phase
class, followed by elementary interval/variation estimates; no further
arithmetic assertion is inserted. This transfer remains candidate evidence
until the normal seam review. Its failure to reach the goal is quantitative
after all powers have been restored, rather than a failed smoothness or
length hypothesis.

The first unproved positive step is cancellation **between actual outer
divisor rows or the two residue contributions**, sufficient for (P18),
or a direct signed high-value/correlation estimate sufficient for (P19).
Taking |chi4|<=1 removes precisely that information. The identity
sum_(d<=u)chi4(d)=O(1) alone gives no bound for the rapidly varying inner
row sums. A weighted exponent-pair theorem with arbitrary r2 weights is
not supplied by either source.

The inventory screen has its own explicit limit: no claim is made about
unlisted new seeds, arbitrary beta-function duality operations, or
phase-specific square-root estimates not encoded in \(\mathcal C\). The
Cushing status is screened, not independently certified. Consequently
this report cannot support "no current method exists" or "all exponent
pairs fail". The hypothetical (0,1/2) control disproves those formulations.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `actual_coefficients` | Pass for the stated transfer: r2 is expanded exactly, both chi4 placements are retained until the declared absolute outer step. No arbitrary-weight exponent-pair assertion. |
| `complete_scales` | Pass: every row and both hyperbola arms are paid; D=sqrt(N) is optimized; N<=T and all existing outer-scale/tail inputs are explicit. An interior alpha=7/10 defeats a complete new certificate. |
| `signed_absolute_distinction` | Pass: this is a sufficient complex-norm upper estimate; positive certificate costs never become signed lower bounds. Neither residue nor outer cancellation is claimed. |
| `real_endpoints` | Pass: proper real intervals, strict d>D versus weak d<=D, arbitrary real R,T and exact product cutoffs are allowed. No integer sampling assumption. |
| `all_costs_restored` | Pass: (P9)--(P12) keep A/K, outer length, smooth variation, residues and cutoff; (P17) keeps sqrt(R), dyadic sums and sharp reconstruction error. |
| `full_quarter_scope` | Pass as a scope check: b=83/650 gives only 102/325; quarter needs a full b-to-zero or subpower input. Every independent M1/M2 parent remains open. |
| `source_versions_hypotheses` | Pass for the two exact application cards. Other records are explicitly metadata/statement screens. Source proof internals were not re-proved; unversioned Cushing is not promoted. |
| `statement_only_control` | Not supplied by this nonblind source report. The conductor's isolated task must independently check the hyperbola transfer; no blind packet or sibling report was read. |

Additional analytic controls: the trivial pair (0,1) in (P12) has q=0 and
recovers N^(1/4) up to logarithms; the conjectural pair (0,1/2) gives a
subpower block and lies outside Q; both are the expected normalizations.
Deleting the second arm incorrectly permits D=1 to suppress its cost,
which the exact partition (P8) forbids. The residue shift remains inside
the phase rather than being Taylor-deleted. No mathematical numerical
experiment or ANTEDB code execution was performed.

A bounded exact-integer check independently reproduced every finite-seed
comparison. For k=a/b and l=c/d, the cleared numerators are
U=10(2ad+bc)-9bd and V=5(ad+2bc)-7bd. Both positive certify the stronger
inequalities quoted in Section 3. Native arbitrary-precision integer
arithmetic returned the following values, without rounding or pair search:

| Seed in displayed order | U | V |
|---|---:|---:|
| P13.1 | 4536 | 2268 |
| P13.2 | 854160662 | 1151402726 |
| P13.3 | 40994 | 142882 |
| P13.4 | 515575348 | 3130800494 |
| P13.5 | 17486504 | 117317242 |
| P7.1 | 271784 | 1847362 |
| P7.2 | 15735452785736 | 109397870935498 |
| P7.3 | 71694505392 | 451339525536 |
| P7.4 | 19685480 | 117434670 |
| P15.1 | 3915464 | 27924202 |
| P15.2 | 147577219482 | 1053201071251 |

This finite arithmetic verification is diagnostic corroboration of the
explicit rational inequalities. The infinite-family factorization and
Q-invariance proof, rather than finite sampling, establish the closure
certificate. No asymptotic assertion is inferred from computation.

## 6. Dependencies and bounded current source log

Permitted internal files actually read, and no other research context:

- `protocol.md`; assigned `briefs/harmonic_pair_sources.md`.
- `state/proof_obligations.yml`, selectively the target, M1, M2, repaired
  Li--Yang and complete-square-root-large-values nodes and their scope.
- `state/active_campaign.yml`.
- `strategy/round211_full_source_strategy_review.md`.
- `strategy/gauss_circle_strategy_review_2026-09-23.md`.
- `strategy/gauss_circle_strategy_checkpoint_round208_2026-09-27.md`.
- `rounds/codex-managed/gc-signed-near-frequency-cancellation/synthesis.md`.
- `rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md`.
- `rounds/codex-managed/gc-full-proof-signed-arithmetic-review/reports/harmonic_current_sources.md`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.

Paths named inside those documents were not opened unless separately listed
above. No current sibling reports or statement-only packet were opened.
The graph hash was rechecked and matches the frozen brief.

The searches were bounded to arXiv for current Gauss-circle, square-root
sum and exponent-pair developments, followed by exact primary URLs.
Search phrases included `exponent pairs 2025 2026 square root exponential
sums Gauss circle`, `exponent pairs Trudgian Yang 2024 2025`, `Gauss circle
problem 2026 improvement withdrawn`, `Gauss circle 2026 September`, and
`exponent pairs 2026`. Irrelevant broad-search hits were not evidence.
The conductor supplied the ANTEDB chapter as an additional primary lead.

| Source / exact version | Level and decision |
|---|---|
| [Bourgain 1408.5794v2](https://arxiv.org/html/1408.5794v2#S6), 22 February 2016, Theorem 6 | Full relevant statement and complete physical application audit in Sections 2--3. No use of the narrower direct range as a global theorem. |
| [Tao--Trudgian--Yang 2501.16779v1](https://arxiv.org/html/2501.16779v1), 28 January 2025, Theorem 20; Definitions 5,11 and Lemma 12 | Second full application audit. The official [record](https://arxiv.org/abs/2501.16779) lists only v1. |
| [Trudgian--Yang 2306.05599v3](https://arxiv.org/html/2306.05599v3), 15 July 2024 | Inventory statement/coordinates screen only; no new third exponential-sum application. The old polygon is explicitly augmented. |
| [ANTEDB exponent-pair chapter](https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html), live snapshot checked 27 September 2026, Theorems 5.22--5.23 | Primary author-maintained inventory screen, including Cushing beyond the arXiv TTY paper. Optimistic comparison, not imported proof or exhaustive closure of its database. |
| [Li--Yang 2308.14859v2](https://arxiv.org/abs/2308.14859v2), 14 September 2023 | Official version/abstract refresh unchanged. The graph's five repairs and qualified final application remain authoritative; printed general propositions are not newly accepted. |
| [Bourgain--Watt 1709.04340v2](https://arxiv.org/abs/1709.04340v2), 16 July 2023 | Official withdrawal refreshed; no theorem imported. |
| [Dong--Robles--Zeindler 2601.00292v2](https://arxiv.org/abs/2601.00292v2), 5 January 2026 | Official withdrawal refreshed; recorded omitted L^2 changes L^5 to L^7 and removes the claimed improvement. No import. |
| [Yamaguchi et al. 2609.04725v1](https://arxiv.org/abs/2609.04725v1), 4 September 2026 | Numerical Gauss-circle evidence, abstract/version screen only; no asymptotic theorem imported and no experiments repeated. |
| [Gao 2604.23918](https://arxiv.org/abs/2604.23918) | Search-result abstract screen: smooth-number restriction, not a uniform unrestricted circle estimate. |
| [Shen 2607.07710](https://arxiv.org/abs/2607.07710) and [Shubin 2606.03781](https://arxiv.org/abs/2606.03781) | Abstract screens only: respectively arithmetic exponent pairs for incomplete Kloosterman sums with modulus hypotheses, and almost-everywhere variable-exponent pair correlation. Neither is this fixed square-root actual-coefficient theorem. |

HTML rendering dates were not substituted for arXiv version dates. The
current screen supplies no claim about publication status absent from a
primary record, and no universal literature nonexistence assertion.

## 7. Recommended state effect

**No change** to accepted mathematics, graph nodes, pointwise exponent,
proof draft or M1/M2 status. Retain (P8)--(P12) and the explicit closure
barrier (P2)--(P3) as candidate method evidence for same-round seam review.

Do not select routine exponent-pair optimization followed by absolute
outer hyperbola summation as the next improvement mechanism on the basis
of the audited inventory. Its worst complete power is already blocked by
one interior physical scale. A claimed better pair must be checked in
the same convention and restored formula; a genuinely signed bilinear
method can escape this limited obstruction and must be assessed separately.

The current signed tenth gate (P19) remains open. The physical alternative
(P18) is concrete and complete, but this report supplies no positive
reason to prefer its stronger complex pointwise requirement over that
gate. The conductor should compare the other independently priced source
report before choosing a complete next estimate. No successor is designed
here, and neither a local identity nor this method failure is a claimed
improvement toward the full quarter exponent.
