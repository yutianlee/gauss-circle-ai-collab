# Round231 admission decision: no analytic launch

11 October 2026. Bounded prelaunch selection following the closed Round230 strategy. This packet does not open or close an analytic Round231.

## Decision

Keep Round231 **pending design**. The two arithmetic mechanisms examined do not supply a new complete signed upper bound. The useful mathematical result is a stronger, independently rederived obstruction to taking absolute values after pooling all cosine signs at each fixed norm tuple. It is retained as reviewed evidence, without promotion to the authoritative claim graph.

The preferred complete target remains

\[
M_{12}(T)=\int w(R/T)|B_T(R)|^{12}\,dR
\ll_\varepsilon T^{29/25+\varepsilon}.
\]

The accepted bound is still \(T^{10\beta+\varepsilon}\), where
\(\beta=0.128966351948\ldots\). No pointwise exponent or proof obligation changes.

## Prime relations: exact arithmetic, unchanged signal

For a split prime \(p\equiv1\pmod4\), the actual coefficients give

\[
r_2(pn)+\mathbf1_{p\mid n}r_2(n/p)=2r_2(n),
\]

and hence the exact complete subseries identity

\[
B_{T;p\mid n}(R)=2p^{-3/4}B_{T/p}(\sqrt p R)
-p^{-3/2}B_{T/p^2}(pR).
\]

Every valuation, the inert and ramified cases, prime powers, complementary coprime terms, squarefree masks and infinite tails were retained. Completing the prime row gives exactly \(H_p=2B_T\), so its weighted covariance matrix is a scalar times the all-ones matrix. A scalar signed amplifier returns \(2(\sum_p\alpha_p)B_T\); weights summing to zero remove the signal. The algebra provides no independent prime decorrelation.

The changed windows also matter: \(B_{T/p}(\sqrt pR)\) is evaluated at radius divided by coefficient parameter \(p^{3/2}\). A natural-window moment estimate cannot be applied uniformly in growing \(p\) without paying this mismatch. The blind algebra report independently verifies the relation and Jacobian.

A coprime-row variant pays its omitted divisible part at
\(T^{4+\varepsilon}P^{-12}\), so \(P\ge T^{71/300}\) pays that error at the preferred target. Its remaining weighted signed covariance must still save

\[
T^{10\beta-29/25}=T^{0.12966351948\ldots}
\]

over the inherited bound. Because those rows share the original wave, the proposed covariance estimate only restates the missing complete estimate. There is no independent reason here to admit it as a new input. This is the specified completed-row obstruction, not a rejection of all prime amplification.

## New scoped result: full sign pooling still costs \(T^{5/2}\)

Write \(a_n=r_2(n)n^{-3/4}\Psi(\sqrt{n/T})\), \(Q=\lfloor T^{2/5}\rfloor\), and let \(d(n)\) be the squarefree part of \(n\). Define

\[
\mathcal C_{\cos}(T)=
\sum_{\substack{n_1,\ldots,n_{12}\ge1\\
d(n_j)>Q\ \mathrm{pairwise\ distinct}}}
\left|\int w(R/T)\prod_{j=1}^{12}
 a_{n_j}\cos(2\pi R\sqrt{n_j}-3\pi/4)\,dR\right|.
\]

All 4,096 cosine signs are summed inside each integral before the modulus. The scout proof, statement-only rederivation and conductor seam check establish

\[
\boxed{\mathcal C_{\cos}(T)\gg T^{5/2}.}
\]

The proof selects an actual positive coefficient block \(n\asymp T\). The accepted binning and repeated-class argument leaves product weight \(\gg T^{3/2}\) with a six-versus-six root sum within \(\delta/T\). If another noncomplementary sign relation is also short, the two sign rows have a minor of determinant \(\pm2\). Fixing ten norms confines the last two to intervals containing at most one integer each. The removed weighted mass is only

\[
\left(\sum a_n\right)^{10}(\max a_n)^2
\ll T^{1+\varepsilon},
\]

for each of finitely many alternative signs. Most near mass survives. Its distinguished balanced pair has positive Fourier real part and all other signs are small by smooth Fourier decay. Restoring the radial factor \(T\) gives \(T^{5/2}\). The scout uses Fourier threshold \(T^{1/4}\); the isolated reviewer independently proves the same conclusion with a sufficiently large fixed threshold. Both completion counts are valid; neither uses numerical evidence.

Galois orbits may be smaller than the full sign cube because of multiplicative squareclass relations. Partitioning a fixed tuple into those orbits cannot improve this positive certificate beyond full sign pooling. Actual nonzero \(r_2(d s^2)\) factors are positive, so divisor-character notation does not itself introduce a cancelling sign on the balanced pair.

**Scope is essential:** the modulus still precedes summation over different norm tuples. This result does not cover pooling all harmonics at fixed squarefree labels before taking a modulus, and does not lower-bound the fully signed integral or moment. Those further cancellations remain possible. In fact the accepted complete estimate already captures substantial cancellation lost by this certificate.

## Revised admission requirement

A next candidate must retain cancellation across different norm/harmonic tuples, or supply a genuinely new arithmetic row system with a proved signed input after full reconstruction. It must give a complete exponent \(b_{12}<10\beta\); improving the pointwise benchmark requires \(b_{12}<13\beta-1/2\), and the preferred milestone is \(b_{12}\le29/25\). The existing head and repeated-class estimates then pay the order-twelve restoration. No all-order extension is presumed.

Neither a new prime identity, fixed-tuple Galois pooling, nor renaming the signed target as a covariance estimate meets this requirement. Do not launch another analytic round on these unchanged premises. This bounded screen is complete; it is not an exhaustive impossibility result or a fresh broad literature review.

## Evidence and state

- [Prime mechanism report](reports/split_prime_cancellation.md) and [isolated prime rederivation](reports/blind_prime_relations.md).
- [Radical packet proof](reports/radical_packet_cancellation.md) and [statement-only packet rederivation](reviews/blind_cosine_packet_rederivation.md).
- [Conductor seam review](reviews/conductor_seam_review.md), exact Wolfram control and local integer/fraction reproduction in `controls/`.

Wolfram and local checks agree on the finite identities; they are diagnostic only. All asymptotic conclusions above have analytical proofs. The claim graph, proof draft, validation matrix, active closed Round230 manifest and previous rounds remain unchanged. No State Patch or new analytic campaign is proposed or applied. Only admission/navigation metadata is updated. The full Gauss circle proof remains open.
