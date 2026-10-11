# 1. Result

Round 206, campaign `gc-complete-signed-shell-arithmetic`.
Task: `independent_shifted_source_review`. Role: independent source/application line reviewer, unmasked after completion of the separate statement-only assignment. Date: 2026-09-26.

**SCOPED GREEN for the finalized claimant artifact.** The HKLDW sharp shifted-pair theorem is quoted and applied legally; its shift uniformity, actual-r2 centering, complete divisor average, variable-width weight variation, remote tails, diagonal, shift aggregate, and moment exponents pass this audit. The two proposed higher-moment imports fail the precise range gates identified in the report.

One incorrect explanatory sentence about removing centering was identified before finalization. The finalized report now correctly distinguishes retaining the signed autocorrelation from taking absolute weights. Its repaired formula, including the factor 2 and the negative sign, passes the independent control in section 5 below.

This is a legal application of one pair-correlation source. It is not a claim that this source is necessary, optimal, or the only way to bound variance. It supplies no new signed sixth moment and no improvement of the existing complete exponent.

The scope assumes the inherited physical-shell reconstruction that identifies the localized spectral block with S_N up to the previously controlled error. That predecessor identity was not among the files authorized for this line audit, so this review does not re-certify its independent proof. The present additive bridge, the new source application, and all deductions once that inherited identification is supplied have been checked. No shared state was edited. After the original blind report was completed, the conductor authorized exactly two byte-preserving formatting repairs to it; those repairs preserved its mathematics and statement-only provenance.

# 2. Exact reviewed artifact, hypotheses, and source interfaces

The review is bound to:

`rounds/codex-managed/gc-complete-signed-shell-arithmetic/reports/shifted_moment_source_attack.md`

SHA256:

`e6d78df605d26dae7012684625f11e1650a12eabc3a98b4b60a7fb23806c7a1e`

The hash was measured after the conductor confirmed the claimant correction was saved and frozen. This GREEN verdict does not refer to the preceding hash `fbb28449270034c9a283d631a7cafbe07e69f82766b569b28340d48790f37f31`.

Use the report's definitions of K, a_m=r2(m)-pi, C_N, h(x)=2sqrt(x)/sqrt(N), X=T^2, H=2sqrt(X)/sqrt(N), smooth fixed w, and the entire middle range T^(52/125)<N<T^(99/125). In particular, w has fixed compact support in a positive interval, h is comparable to H on its support, and H has X-exponent between 151/500 and 99/250. The actual circle bound and coefficient bound are the inherited inputs. Constants depend only on the specified fixed functions, fixed window and epsilon.

Only the following three primary source interfaces were inspected:

- [HKLDW, arXiv:1705.04771v3](https://arxiv.org/pdf/1705.04771v3), Theorem 7.1, equations (7.1)--(7.3), printed pp.26--27. Its sharp estimate has the displayed error O_lambda((Y+k)^(1-lambda)+k) for one fixed positive lambda. The notation has no k-dependent implicit constant. The report keeps lambda unspecified and uses this sharp estimate, rather than transferring the exponential-weight estimate to a different weight. Remark 7.2 only proposes a possible numerical lambda; the report does not import it.
- [Hughes--Rudnick, arXiv:math/0304129v3](https://arxiv.org/pdf/math/0304129v3), Proposition 5, printed p.8, and Theorem 1, printed p.2. The fixed-m moment restriction and the resolution condition L/sqrt(M) tending to zero agree with the report. The sharp-annulus theorem has a subpolynomial inverse thickness and proves convergence in distribution; the sharp transfer is via a variance approximation.
- [Tanigawa--Zhai, arXiv:0805.1525](https://arxiv.org/pdf/0805.1525), Theorem 1 and Corollary 1, printed pp.4--5. The object is the fourth moment of the divisor-error increment. Its lower width threshold is Y^(3/7); the averaging-length condition and the corollary's epsilon margins are recorded correctly in the report.

No fourth substantive interface was inspected, and no theorem was imported from a secondary summary.

# 3. Independent proof/application audit

**Sharp source and centering.** The source's sharp error is sufficiently uniform for all 1<=k<=C X and t comparable to X. Reduce its fixed lambda to min(lambda,1/2). This can only weaken its upper bound. Define

\[
 Q(y)=\sum_{1\le m\le y}r_2(m)=\pi y+P(y)-1.
\]

For real t and integer k,

\[
 \sum_{1\le m\le t}r_2(m+k)=Q(\lfloor t\rfloor+k)-Q(k)
 =\pi t+O_\epsilon(X^{\theta+\epsilon}+1).
\]

This formula includes the lower endpoint and remains uniform for k comparable to X; there is no unaccounted contribution pi*k. Expanding a_m a_(m+k), and replacing floor(t) by t in the constant term at cost O(1), gives

\[
 \sum_{1\le m\le t}a_ma_{m+k}
 =(c_k-\pi^2)t+
 O_\epsilon(X^{1-\lambda+\epsilon}+kX^\epsilon).
\]

The circle-error contribution is absorbed because theta<1/2<=1-lambda. Integer endpoints cause no additional main term. If the source's sharp cutoff is first read at integer Y, passing to real t also costs at most c_k+O(X^epsilon), which fits the displayed error since c_k is divisor bounded. Thus report equation (9) passes.

**All divisors in the local-density average.** Substituting k=qd into its source formula gives exactly

\[
 c_k=8\sum_{q\mid k}\frac1q
 -16\sum_{\substack{q\mid k\\2\mid q,\;k/q\ {\rm odd}}}\frac1q.
\]

The only negative parity configuration is q even and d odd. Summing all k<=Z, not merely odd shifts, yields

\[
 \begin{split}
 \sum_{k\le Z}c_k
 &=8\sum_{q\le Z}\frac1q\lfloor Z/q\rfloor
  -16\sum_{\substack{q\le Z\\2\mid q}}\frac1q
                  \#\{d\le Z/q:d\ {\rm odd}\}\\
 &=8\zeta(2)Z-8Z\sum_{2\mid q}q^{-2}+O(\log(2Z))\\
 &=6\zeta(2)Z+O(\log(2Z))
 =\pi^2Z+O(\log(2Z)).
 \end{split}
\]

Here each floor/count error is O(1), their weighted sum is harmonic, and extending the convergent q^-2 sums costs O(1). This establishes equation (8), including the exact pi^2 normalization.

**Variable width and total variation.** Write

\[
 W_k(u)=\int w(x/X)K((x-u)/h(x))K((x-u-k)/h(x))\,dx.
\]

The product of two uniformly Schwartz functions separated by k/H has an integral bounded by

\[
 \|W_k\|_\infty\ll_A H(1+k/H)^{-A}.
\]

For variation, substitute x=u+y before differentiating. On the support of w, h'/h=1/(2x)=O(1/X). Differentiation therefore hits either w at scale 1/X or a kernel argument at cost

\[
 O\bigl(X^{-1}|y|/h\bigr),\qquad
 O\bigl(X^{-1}|y-k|/h\bigr).
\]

Both polynomial factors are absorbed by increasing the initial Schwartz order. Hence, for u in a fixed interval comparable to X,

\[
 |W_k'(u)|\ll_A (H/X)(1+k/H)^{-A}.
\]

A smooth cutoff to such a u interval contributes another term of the same size. Integrating over its O(X) length proves

\[
 \|W_k\|_\infty+\int|W_k'(u)|\,du
 \ll_A H(1+k/H)^{-A}.
\]

There is no derivative of a_m and no freezing of h(x). At x=0 the integrand vanishes in a whole neighborhood because the support of w stays positive; the substitution causes no boundary term there. The report's H-sized, rather than H^2-sized, variation is correct.

**Partial summation and every shift.** Apply the preceding variation estimate to the centered sharp partial sum. Its error for each k is

\[
 \ll X^\epsilon H(1+k/H)^{-A}(X^{1-\lambda}+k).
\]

Since H tends to infinity and is polynomially bounded,

\[
 \sum_{k\ge1}(1+k/H)^{-A}\ll H,
 \qquad
 \sum_{k\ge1}k(1+k/H)^{-A}\ll H^2
\]

for sufficiently large fixed A. This yields precisely
\(O_\epsilon(X^{1-\lambda+\epsilon}H^2+X^\epsilon H^3)\).

The argument does not apply the sharp source outside its selected range without justification: for k beyond a fixed large multiple of X, and for m outside a fixed positive interval comparable to X, at least one kernel is remote. The double sum of the absolute tails is bounded using r2(m)<<m^epsilon and Schwartz decay. One may first sum the remote factor with decay order B, then the other factor, which costs at most a polynomial in X and H. Since H/X is bounded by a fixed negative power of X, B can be fixed sufficiently large to make the entire integrated tail O_A(T^-A). This treats both the infinite m tail and the infinite k tail. The same reasoning permits removing the auxiliary smooth u cutoff in the arithmetic main term. No divergent infinite divisor or shift sum is hidden in that removal.

**Main term and diagonal.** Fubini and the change of variable t=(x-u)/h(x), treating x as fixed, give

\[
 \int_\mathbb R W_k(u)\,du
 =\int w(x/X)h(x)A_K(k/h(x))\,dx,
\]

where A_K is the even Schwartz autocorrelation. The partial sums of c_k-pi^2 are O(log(2Z)). Partial summation against A_K(k/h) therefore bounds the signed k sum by O(log(2h)), uniformly for the actual h(x). After integration its contribution is O(XH log(2X)). The diagonal contributes O_epsilon(X^(1+epsilon)H), directly by a_m^2<<m^epsilon and the lattice sum of |K|^2. It is retained separately. Since

\[
 H^2\ll X^{198/250}<X,
\]

the H^3 error is absorbed by XH. This proves report equation (1) with all pair shifts and repeated indices restored.

**Shell bridge and restoration.** The present report's curvature error is consistent with an independent local estimate: writing z=(R^2-m)/h, one has

\[
 |\sqrt N(R-\sqrt m)-z|\ll z^2/(R\sqrt N),
 \quad
 |m^{-1/4}-R^{-1/2}|\ll R^{-1/2}|z|/(R\sqrt N).
\]

Schwartz summation over an effective h terms gives
\(O_\epsilon(T^{-1/2+\epsilon}N^{-1})\). Low m and arbitrarily large m are remote by a positive power of T and have summable tails after using the coefficient bound. The complete-lattice mean vanishes by Poisson summation because h>2 on the requested radius interval and the Fourier support avoids zero and all nonzero h multiples. Omitted nonpositive m give only remote tails. At an integer center the central term is zero, since K(0)=0. This verifies report equation (7) directly, with the inclusive convention.

The Jacobian and amplitude supply exactly T^-2 in the second moment:

\[
 |S_N|^2\,dR\simeq x^{-1/2}|C_N(x)|^2\frac{dx}{2\sqrt x}.
\]

Accordingly equation (1) becomes

\[
 \int_I|S_N|^2\,dR
 \ll_\epsilon T^\epsilon
       (TN^{-1/2}+T^{2-2\lambda}N^{-1}).
\]

The bridge error contributes O(T^epsilon N^-2) here and a negligible twelfth moment.

For the spectral block, the N^(1/4+epsilon) coefficient sum and the smooth multiplier applied to the complete cosine series in the supplied kernel are valid. The latter has uniformly bounded L1 norm after scaling; its portion outside an enlarged positive radius interval is arbitrarily small by the global coefficient sum O(T^(1/4+epsilon)) and the Schwartz tail of the multiplier kernel. Applying the inherited physical-shell identification transfers these spectral bounds to S_N. The T^beta and T^(1/2)N^-1/2 bounds on S_N also follow directly from the inclusive-circle integration-by-parts estimate and the elementary local coefficient sum, respectively. The only identification not re-proved in this scoped review is the inherited spectral-block-to-physical-shell reconstruction, as declared in section 1.

**Exponent maximization.** Put nu=log_T(N) and
\(\omega(\nu)=\min(\nu/4,\beta,(1-\nu)/2)\).
The exact inherited beta places 4beta strictly inside the middle band, with 4beta<1-2beta. Below 4beta, the two exponents in report equation (2) increase with slopes 2 and 3/2. Between 4beta and 1-2beta they decrease with slopes -1/2 and -1; beyond 1-2beta they decrease with slopes -11/2 and -6. Their maxima are therefore

\[
 1+8\beta,\qquad 2-2\lambda+6\beta.
\]

This verifies equation (3), including its interior maximization rather than substitution of a range endpoint. Dyadic recombination costs at most fixed logarithms, and 1+8beta>10beta, so this source route gives no improved complete bound even if its error term is removed.

For the hypothetical 2j moment, restoration gives T^(1+epsilon)N^(-j/2). The exponent after multiplying by the supremum is

\[
 1-j\nu/2+(12-2j)\omega(\nu).
\]

For j=1,2,3 its maxima are respectively 1+8beta, 1+4beta, and 1. In the sixth case, N^-3/2 cancels the sixth power of N^1/4. This is a correct conditional sufficiency statement; it does not supply its own arithmetic input.

**Two failed range transfers.** For Hughes--Rudnick, the intended radial resolution gives L comparable to sqrt(N), so L/sqrt(M)->0 requires M/N->infinity. With m=6, Proposition 5 instead requires M=O(T^(2(1-delta)/31)). Since

\[
 \frac{52}{125}-\frac2{31}=\frac{1362}{3875}>0,
\]

no middle N can meet both. The sharp-annulus subpolynomial L condition also fails. This is a sufficient rejection before attempting a change of filter; it does not purport to construct that filter transfer.

For Tanigawa--Zhai, every available arithmetic width is at most a constant times X^(99/250), whereas its theorem requires at least a constant times X^(3/7). The strict exponent gap is

\[
 \frac37-\frac{99}{250}=\frac{57}{1750}>0.
\]

Even taking its averaging length as large as Y cannot repair this width failure. Its different coefficients and fourth moment provide independent mismatches. Both rejection gates pass the source audit.

# 4. First doubtful or unproved step

There is no remaining source/application defect in the finalized report within the scope above. The first new arithmetic statement still unproved is the uniform signed sixth-moment estimate of C_N at the required variable widths. The inspected pair theorem gives a two-factor correlation, not six-factor control.

The predecessor physical-shell reconstruction remains an explicit inherited interface for the N^(1/4) supremum and the complete-series interpretation. This review has not silently replaced inspection of that earlier proof with confidence in the claimant's citation. The conductor must use its existing accepted validation for that interface.

Neither convergence in distribution nor a mean-square approximation controls rare sixth-moment excursions by itself. No such inference appears in the finalized report. The conclusions are application failures for these three interfaces, not claims that actual arithmetic sixth moments or other variance methods are impossible.

# 5. Analytical controls and outcomes

**Parity and normalization control: PASS.** The divisor formula gives c_1=8 and c_2=4. The exact parity test q even and k/q odd reproduces both; averaging all divisors yields pi^2, rather than the uncorrected 8*zeta(2). These are analytical evaluations, not a numerical experiment.

**Constant-mean/autocorrelation control: PASS after correction.** Since K is real,

\[
 \widehat{A_K}(\xi)=|\widehat K(\xi)|^2.
\]

Its Fourier support is contained in [-2,-1] union [1,2]. Therefore, for h>2,

\[
 \sum_{k\in\mathbb Z}A_K(k/h)
 =h\sum_{j\in\mathbb Z}\widehat{A_K}(hj)=0,
 \qquad
 \sum_{k\ge1}A_K(k/h)=-A_K(0)/2.
\]

Thus, in the report's off-diagonal convention 2*integral w*h*sum_(k>=1), replacing c_k-pi^2 by c_k changes the answer by exactly

\[
 -\pi^2A_K(0)\int w(x/X)h(x)\,dx=O(XH).
\]

This checks both the sign and factor in the finalized correction. The larger XH^2 estimate is instead the cost of taking absolute autocorrelation/pair weights. Centering remains algebraically necessary for the stated expansion, but it is not the only cancellation available.

**Variable-width derivative control: PASS.** Differentiating the original kernels in u separately would suggest a width-scale derivative. The x=u+y substitution correctly exposes the cancellation of translation derivatives and leaves only the slow x dependence of w and h. The explicit h'/h=1/(2x) calculation proves the claimed variation bound for the actual width; no fixed-width theorem is being substituted.

**Tail and diagonal control: PASS.** The k=0 contribution, m near the origin, integer endpoints, infinite m tail, infinite k tail, auxiliary cutoff tails, curvature error and convolution tails each have a stated summable estimate or a clearly declared inherited reconstruction dependency. In particular, H^3 is not discarded: H^2<X absorbs it into the diagonal-scale upper bound.

**Higher-moment control: PASS as a failed inference.** Even a hypothetical Gaussian-sized second or fourth integral gives exponents 1+8beta or 1+4beta after the available supremum, both above 10beta. The sixth line is explicitly hypothetical. No test here is asserted to refute the sixth moment for actual r2.

# 6. Dependencies and exact artifacts used

The authorized local files read for this review were:

1. `protocol.md`.
2. `rounds/codex-managed/gc-complete-signed-shell-arithmetic/reports/shifted_moment_source_attack.md`, finalized hash recorded in section 2.
3. `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`, SHA256 `942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212`.

The exact three primary PDF URLs and theorem locations are recorded in section 2. No literature expansion was performed. The original statement-only report was accessed only for the conductor-authorized repair of a raw CR in its dyadic label and a rendering typo in equation (5.7). No mathematical content changed; its isolation at the time of derivation remains intact. Its format-corrected SHA256 is f7c7e3362acc69e71ca8c38b2ec37a1d5b5a08f87682f9c056f2bc4c6770d511.

The claimant's starting graph hash is provenance stated by that artifact, not a newly verified graph hash. No graph, state matrix, proof draft, synthesis or predecessor reconstruction report was read in this review. Elementary Fourier/Poisson identities, partial summation, divisor rearrangement, Stieltjes integration by parts and moment inequalities were checked analytically. There were no numerical experiments or new source-card writes.

# 7. Recommended state effect

**SCOPED GREEN** for the finalized hash in section 2: accept this review as validation of the legal sharp-pair source application, the exact local-density identity, its variable-width transfer, full error/exponent accounting, and the two incompatible higher-moment source gates. Preserve the explicit inherited-interface limitation for the spectral-block/physical-shell identification.

**No target promotion and no new arithmetic theorem.** Retain the existing complete exponent and the open signed sixth-moment obligation. Archive the source application as one fully priced route, without treating the pair theorem as necessary for variance or its output as an optimal bound.

The earlier inaccurate autocorrelation explanation was corrected before this hash-bound verdict. No further correction is required within this scope. No shared state was changed and no successor round was designed. The review ends here.
