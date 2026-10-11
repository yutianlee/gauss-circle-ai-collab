# Round 211: independent nonblind review of the bilinear source report

Campaign: `gc-full-source-method-review`. Same-round source/application seam.
Reviewer: `harmonic_pair_sources`; nonblind cross-review after its own
discovery report was finalized. Date: 2026-09-27 UTC / 2026-09-28 Shanghai.
Graph SHA256: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Reviewed artifact:
`rounds/codex-managed/gc-full-source-method-review/reports/bilinear_arithmetic_sources.md`.
Reviewed SHA256:
`26425644ad0a0473b315a61d7499f82f4f053ebd363c15340032dea873ce2978`.
Only this review is written. No experiments, graph mutation or successor work.

## 1. Result: GREEN for the two scoped applications and their failure certificates

The source statements, actual-coefficient dictionaries, smooth product
norms, hyperbola complements and restored exponents check out. Both theorem
calls are legal, including the square-root exponents, but their displayed
positive certificates are too large. The report carefully distinguishes
this failure from a lower bound for an actual signed sum.

The stronger KRW comparison, equation (14a), is particularly decisive:
its aspect-independent leading term cannot improve either elementary
whole-block branch at any 1<=N<=T. No repair is required for the reviewed
claims. GREEN does not certify either external paper's entire proof,
unreviewed source families, a complete circle estimate, or a statement-only
derivation. Those are outside this nonblind seam.

## 2. Exact source and scope checks

I independently opened the [Wu publisher record](https://link.springer.com/article/10.1007/s006050050062)
and the [author-uploaded full article](https://www.researchgate.net/publication/226968624_Double_Exponential_Sums_and_Some_Applications).
Theorem 1 on pp. 255--256 has precisely the six nonvanishing factors
quoted in the report, an arbitrary bounded outer coefficient, and an
inner interval depending on the outer variable. The four terms and
logarithm in equation (4) match. At gamma=delta=1/2 the factors are
nonzero; no gamma+delta-1 condition is stated. The publication is
Monatshefte fuer Mathematik 128 (1999), 255--262, November 1999. The
author upload is explicitly attributed to Jie Wu, 13 April 2015.

I also independently inspected the [published EMS PDF](https://ems.press/content/serial-article-files/38194),
p. 303 (PDF page index 22), including the sum definition immediately
before Proposition 5. It admits two arbitrary coefficient vectors with
suprema at most one, positive phase parameter and positive lengths at
least one, and excludes only 0 and 1 for each monomial exponent. All four
terms in the report's equation (5) match. This is the 2007 published
version, not merely the older [arXiv v1](https://arxiv.org/abs/math/0507001v1).
Neither theorem demands a nonzero two-dimensional Hessian.

The object checked is the physical complex block F_N, whose required
cosine block is its specified real part. A complex supremum bound is
sufficient and can be stronger than the signed real-block moment goal.
The report does not claim equivalence between those two tasks.

## 3. Independent derivation of the transfer and power ledger

### Actual coefficients and masks

Using r2(n)=4 sum_(d|n)chi4(d), the finite product support gives exactly
the two disjoint arms in equation (7). If d>D, then integer d>=D+1;
from dm<=4N it follows that m<=floor(4N/(D+1)). Conversely every
retained nonzero divisor pair is in exactly one arm. Integer equality
endpoints therefore check out, while R,T,N can all be real.

After dyadic division, a contributing rectangle has AB comparable to N.
The phase is exactly Z sqrt(d/A)sqrt(m/B), Z=R sqrt(AB). There is no
Taylor approximation and no modular-phase identification. chi4(d) remains
an allowed outer coefficient for Wu on both arms. In particular the
second arm must not be freely reoriented as a short unweighted outer
sum; the report does not make that error. For KRW both orientations
are permitted because both vectors are bounded.

For Wu, write f_N(dm)=N^(-3/4)g(dm/N). The variation of the compactly
supported g is bounded uniformly for N<=T. A product prefix dm<=y
has an interval section in m for every fixed d. Stieltjes partial
summation therefore restores g with O(1) norm before the explicit
N^(-3/4), exactly within the source's moving-interval hypothesis.

For KRW, the Fourier transform of g(exp(s)) is rapidly decreasing
uniformly in N/T<=1. Mellin inversion represents the weight as
an integrable superposition of d^(it)m^(it)N^(-it). The last factor
has modulus one and can be absorbed into the integral coefficient.
Each vector has supremum at most one, including chi4 and the one-variable
hyperbola cuts. The integral of the coefficient moduli is O(1).
Thus no hidden square-root length norm occurs, and an arbitrary
joint-symbol factorization is not being assumed. Partial dyadic endpoints
are one-variable indicators, hence also legal.

The isolated d=1 convention in the Wu call is explicitly paid by the
trivial physical price N^(1/4); it is separate from the n=1 reconstruction
term. No complement is silently removed. Smoothness above N=T alone
is correctly not used to claim the adjacent tail is small.

### Wu powers

Let p=4K-2, w=20K-2k-14, K=2^k. Substitute B=N/A and Z=T sqrt(N),
then multiply every source term by N^(-3/4). The exponent of A in the
first term is K/w. Its exponent of N is

\[
 \frac{p/2+13K-2k-10}{w}-\frac34
       =-\frac{k+1}{2w}.
\]

The four normalized terms are consequently

\[
 T^{p/w}N^{-(k+1)/(2w)}A^{K/w},\quad
 N^{-1/4}A^{1/2},\quad N^{1/4}A^{-1/2},\quad T^{-1}N^{-1/4}.
\]

This independently reproduces equation (10). At A comparable to sqrt(N),
the N exponent becomes (K-k-1)/(2w)>=0. Since 5p-w=2k+4>0,
the leading T exponent exceeds 1/5 for every fixed admissible k.
In the complete required band alpha<242/325, the trivial physical
exponent alpha/4 is at most 121/650<1/5. Hence this positive source
certificate cannot improve the trivial balanced-block treatment. This
remains true when considering the infimum over fixed k; no uniformity
for k growing with T is assumed.

### KRW powers and global redundancy

Its normalized terms are

\[
 T^{1/8}N^{1/16},\quad N^{1/4}A^{-1/2},\quad
 A^{1/4},\quad T^{-1/2},
\]

agreeing with equation (12). Swapping A and B changes the two length
terms, but leaves the first and last terms unchanged. The report takes
the minimum of the two allowed sums, rather than minimizing each
length term independently.

At balance this gives the leading T^(1/8)N^(1/16), with the other
terms O(N^(1/8)+1+T^(-1/2)) dominated for N<=T. The crossover with
N^(1/4) is N=T^(2/3). More generally, regardless of aspect ratio:

\[
 T^{1/8}N^{1/16}\ge N^{1/4}\quad(N\le T^{2/3}),
\]
\[
 T^{1/8}N^{1/16}\ge(T/N)^{1/2}\quad(N\ge T^{2/3}).
\]

Raising the first comparison to the sixteenth power gives T^2>=N^3;
the second gives N^9>=T^6. Thus equation (14a) is exact. Adding the
accepted T^beta cap only makes this source certificate less useful.
This conclusion is about the displayed upper bound, not a signed
lower bound, and does not rule out cancellation between rectangles.

### Reconstruction and the diagnostic geometry

The T^(-6) shell-to-radius tenth-moment factor, the N^(1/20) reproducing
factor, and the sqrt(R) reconstruction amplitude are all retained. The
low/high bands and their equality endpoints, bounded singleton and
previously reviewed tail are separately paid. Thus a hypothetical
success at the original gate gives 102/325, not quarter.

The displayed phase derivatives give Hessian determinant zero. Solving
the interior stationary equation yields m*=R^2d/(4k^2), phase R^2d/(4k),
and amplitude of order B/sqrt(Z). The Fourier identity for chi4 is
correct and leads to the two quarter-shifted linear resonances. The
report expressly does not present this interior calculation as a
completed transform: its endpoint/tail/error obligations remain open.
That distinction is necessary and has been observed.

The optimistic internal comparisons also reproduce algebraically:
for a balanced L-by-L monomial rectangle the KRW leading term is
X^(1/16)L^(13/8), and for product length M it is
X^(1/16)M^(13/16). The assumed unit product norm is labeled favorable,
not proved for literal internal symbols. No M1/M2 or GAR implication
has been inserted from this comparison.

## 4. First doubtful or unproved step

No unproved step was found inside the stated local transfer and
certificate comparison. The external theorems remain imported source
results rather than independently reproved papers.

The first missing positive arithmetic step remains a genuinely signed,
actual-coefficient bound on the complete source at the requested power,
or the complete original tenth-moment gate. The source terms cannot be
deleted merely because other parts of an upper bound are smaller.
The stationary diagnostic additionally needs a full uniform transform
before it could support any new theorem.

The claimed no-gain result must retain its scope: these two source calls,
their exact norm placements, and the chosen triangle aggregation. It is
not a prohibition on all bilinear estimates, sign-sensitive arithmetic,
different smoothing, or other whole-discrepancy arguments.

## 5. Controls and current-version outcomes

| Control | Review outcome |
|---|---|
| Actual coefficients and masks | GREEN: both r2 arms, chi4 placement and product smoothing are legal. |
| Theorem hypotheses | GREEN: quoted intervals/coefficient suprema and square-root exponents match both primary statements. |
| Restored powers | GREEN: all terms of (10),(12), balanced prices and complete redundancy (14a) were independently derived above. |
| Complete scales and endpoints | GREEN: real inputs, hyperbola equality, partial rectangles and the paid singleton/tails are retained. |
| Signed versus absolute | GREEN: no certificate floor becomes a physical lower bound; the original real moment remains weaker than the complex rectangle supremum route. |
| Full-quarter scope | GREEN: no parent closes and the fixed milestone remains distinct from the full goal. |
| Statement-only isolation | Not this review: it is explicitly nonblind and does not replace the separately isolated derivation. |

The bounded current record refresh confirms the report's version claims:
[2601.15448v4](https://arxiv.org/abs/2601.15448v4) is dated 3 July 2026;
[2605.01635v3](https://arxiv.org/abs/2605.01635v3) is dated 20 July 2026
and presents the unified successor, with unconditional Fourier analysis
and conditional short-Salie consequences distinguished. Both
[2603.00768v3](https://arxiv.org/abs/2603.00768v3) and
[2603.25814v3](https://arxiv.org/abs/2603.25814v3) explicitly state merger
and supersession, rather than a mathematical refutation. These are
metadata/abstract checks, not further theorem imports.

No numerical or probabilistic experiment was performed. The controls
above are exact identities, derivative computations and exponent algebra.

## 6. Dependencies and exact artifacts used

- The reviewed bilinear report at the SHA256 bound above.
- `protocol.md`, the round211 active campaign, selected graph state,
  and the previously permitted strategy/reconstruction context already
  read during this task's discovery phase.
- The four primary Wu/KRW URLs in Section 2 and the four current Baier
  records in Section 5, opened independently for this seam.
- The conductor's explicit same-round cross-review assignment.

No statement-only packet was accessed. The review did not independently
reopen every historical M1/M2 source artifact named by the claimant;
its GREEN scope is the two present applications and their nonimplication
into those still-open parents. No sibling discovery report was altered.

## 7. Recommended state effect

Retain the reviewed report as GREEN **scoped method evidence** at its
bound hash. No correction is required for the two theorem applications
or the complete KRW redundancy comparison. No accepted mathematical
node, pointwise exponent, internal parent or proof draft should change
merely because these imports are valid.

The source comparison supports rejecting these two exact positive
certificates as an improvement mechanism at the required powers. It
leaves the full signed tenth gate, any adequate actual bilinear estimate,
all internal parents, and the quarter theorem open. This completes the
assigned same-round seam; no successor is selected here.
