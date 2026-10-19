# Round235 nonauthor arithmetic-dispersion review

## 1. Result: PASS at the explicitly limited arithmetic scope

Campaign `gc-signed-sixth-dispersion`; round 235; task `arithmetic_dispersion_review`; selected-context nonauthor reviewer. Generated 2026-10-12, Asia/Shanghai. Reviewed conductor candidate SHA256 `cee1d243f21577e090acb0f9387c0412f4f70748b918aa3661e64db15586a8f3`, particularly Sections 3C--3E, together with the frozen arithmetic and independent packet reports named in Section 6.

**PASS.** The exact hyperbola completion, signed square packet, two character branches, rational-frequency coefficients, moving-endpoint variation, paired and same-denominator budgets, and actual tuplewise-absolute obstruction are valid at their printed scope. The isolated progression/filter and constant-width tuple-absolute control also pass, including their signs and complete endpoint/negative-contribution arguments.

No material correction is required to the reviewed candidate. This is not an approval of S6: its actual nonpaired signed rational sextuple estimate remains unproved. The candidate correctly recommends identity state effect. This review does not duplicate the separate bridge/source/restoration seam, and does not characterize the inherited full history as freshly audited.

## 2. Exact hypotheses and review boundary

The packet has x=R^2 in a fixed positive window R in [cT,CT], H(x)=2R/sqrt(N), H0=T/sqrt(N), and cX<=N<=CY with X=T^(52/125), Y=T^(99/125). In particular H is comparable to H0 and H/R tends to zero by a fixed power. Its actual q_N is smooth on a common compact support [a,b] subset (0,infinity), with uniform derivatives; K is its real odd Schwartz sine transform, and Khat has a gap around zero.

The reviewed arithmetic assertions concern the exact actual coefficient r2(m), its completed progression sum A_N, and the explicit signed square correction. The actual absolute-certificate lower bound uses a genuine **interior** block with phi=1 throughout the partition support and a fixed nonnegative smooth partition cutoff. It is not asserted for every transition block. A counterexample to a proposed uniform tuple-modulus certificate needs only these interior blocks.

The blind tuple-absolute theorem has a separate scope: a fixed nonzero real kernel, constant H>=1, and an interval of length L>=4R_K H. It is an artificial-coefficient control, not an r2 moment lower bound. This reviewer did not author either report under review. Earlier in the round this reviewer authored the bridge report, so this is a nonauthor arithmetic review, not a statement-only blind review of the entire campaign.

## 3. Derivation and seam checks

### Hyperbola freezing and the square packet

The exact hyperbola identity retains both chi4(d) and chi4(k) for dk=m, k>=d, then subtracts one central square term. Comparing with the completed d<=R sum, a wrongly included nonsquare pair has k<d<=R and therefore

    dk<=d(d-1)<=R^2-R.

An omitted nonsquare pair has k>d>R and therefore dk>=d(d+1)>R^2+R. These inequalities hold for arbitrary real R; they do not require its fractional part to stay away from zero. Multiplicity at each m is at most a constant times tau(m). Summation of the Schwartz majorant for |m-x|>=R costs T^epsilon H(H/R)^(B-1), with the remote infinite norm ranges also convergent. As H/R is a fixed negative power, an arbitrarily small power error follows by choosing B. This proves the delicate freezing step rather than treating a moving cutoff as constant without payment.

At a square the exact difference is -4chi4(d)K((x-d^2)/H) for d<=R and +4chi4(d)K((x-d^2)/H) for d>R. At equality K(0)=0. The printed signs of Qsq are correct. The square grid has spacing comparable to R near x, so its absolute packet is O(1). Integrating the same majorant costs O(T H0): each of O(T) central squares costs O(H0), and all distant squares have convergent negligible tails. Its sixth power is bounded by a constant times this majorant. The arithmetic report's sharper O(T H0) sixth-center expenditure is therefore valid; the candidate's weaker O(T^2) expenditure is also safely paid.

Extending positive k to all integers creates at most

    C_B[(1+x/H)^(-B)+(H/d)(1+x/H)^(1-B)]

per d. Summing d<=R gives the stated T-plus-H-log-T prefactors. These cannot be dropped, but are dominated by an arbitrarily small power after increasing B. No negative-index or zero-index term is silently erased.

### Character Fourier constants and grouping

The ordinary progression has coefficient (H/d)Khat(Hh/d) at h/d. The residue-class Fourier factor for the character progression is

    e(-k/4)-e(-3k/4)=-2i chi4(k),

so its coefficient is H/(2id) chi4(k)Khat(kH/(4d)). Since Khat(s)=-i q_N(s)/2 for positive s, pairing positive and negative k gives the **negative** cosine coefficient -H/(2d)chi4(k)q_N(kH/(4d)). This agrees with the independent blind report and the candidate.

In the ordinary branch, write h=j a0 and d=j q in lowest terms. Complete multiplicativity gives chi4(q) times Lchi(R/q), hence

    c_(a0/q)=4H chi4(q)Lchi(R/q)Khat(Ha0/q)/q

for odd q. Even q vanish. In the character branch, write the original odd numerator k=g a0 and 4d=gq. The gcd g is odd, 4 divides q, and d=gq/4. Its character is chi4(g)chi4(a0), yielding exactly

    c_(a0/q)=8H chi4(a0)Lchi(4R/q)Khat(Ha0/q)/(i q).

Thus q=2 modulo 4 is absent. No sign or factor four is missing. The odd-q coefficients are imaginary and odd under lambda->-lambda; the 4|q coefficients are real and even. Consequently c_-lambda=conjugate(c_lambda), as required for the real sixth expansion. The alternating odd harmonic partial sums satisfy 2/3<=Lchi(U)<=1 for U>=1 and are zero below one.

The compact support annihilates the ordinary progression for d/H<=1/b and the character progression for d/H<=1/(4b), including equality because the smooth profile vanishes at the enclosing boundary. The blind report's stronger statements using the exact support supremum B are sound: the first nonzero sampled Fourier coefficient proves sharpness of each maximal initial cutoff interval, without asserting nonvanishing at every larger ratio.

### Paired sectors and moving endpoints

For each active q there are O(q/H0) numerators and |c_lambda|<=C H0/q. This proves sum|c_lambda|^2<=C H0 log(2T). Every product admitting an opposite-frequency pairing is a product of three modulus squares and is nonnegative. Counting the union by the 15 pair partitions gives the claimed paid T^2 H0^3 log^3(2T) budget without assuming that the partitions are disjoint.

For exact-zero tuples sharing q, five numerators determine the sixth. Their absolute coefficient mass is O((q/H0)^5(H0/q)^6)=O(H0/q); summing q and integrating pays T^2 H0 log(2T). This says nothing about mixed-denominator exact rational relations. The candidate properly keeps those relations in the nonpaired owner and discusses overlap if both paid sectors are removed.

For a fixed q, jumps of Lchi(R/q) have total size bounded by sum_(cT/q<=j<=CT/q)1/j=O(1); if the lower index is below one then q is comparable to T and there are O(1) jumps. The same proof applies to 4R/q. Smooth factors H and Khat(Hlambda) have total variation at their displayed coefficient scale, since H'=H/(2x) and all contributing Hlambda stay in a fixed compact range. Thus sup|c_lambda|+Var(c_lambda)<=C H0/q.

Stieltjes integration by parts against the fixed smooth window legitimately gives

    |integral w product(c_lambda_j)e(x sum lambda_j)dx|
      <=C product(H0/q_j) min(T^2,1/|sum lambda_j|).

This includes all jump endpoints and implies only first-order decay. The report expressly declines arbitrary repeated integration by parts. Its T^(-2) common-center resolution is correct; it does not replace the one center by six independent averages.

### Actual absolute certificate: primitive count and complete-window sign

There are genuine dyadic blocks whose complete fixed support lies inside [2X,Y], because Y/X tends to infinity by a fixed power. On such a block phi=1, and Psi(sqrt(N/T)s) tends uniformly to 1. A nonnegative partition function therefore makes q_N nonnegative everywhere, and uniformly positive on one fixed interval. Shrinking a fixed positive-w subwindow J if necessary supplies the interval of fractions of length comparable to 1/H0 whose scaled arguments lie in that positive interval for all x in J.

For q odd in [kappa T,2kappa T], the number of integer numerator-denominator pairs in the selected trapezoid is a positive constant times T^2/H0 plus O(T+T/H0+1). If an odd prime p divides both entries, rescaling preserves odd denominator parity and its main area is exactly 1/p^2 of that count. Such p are at most O(T/H0), the numerator upper bound. The sum of their boundary errors is

    O(T log T+(T/H0)log T+T/H0),

which is o(T^2/H0) because H0/T tends to zero by a power. The union bound for removed main areas uses sum_(p odd)1/p^2<=sum_(n>=3)1/(n(n-1))=1/2. Hence a positive density survives with gcd one, proving M>=cT^2/H0. The denominator parity and primitive-count boundary terms are both accounted for.

Pigeonholing the M^3 ordered triple sums into O(T^2/H0) cells of width delta/T^2 yields at least cT^10/H0^5 ordered pairs of triples in the same cell. These produce the actual three-positive/three-negative rational sextuples. No distinct-fraction restriction is needed for this count.

For each such sextuple in the odd-q branch, the factors (-i)^3(i)^3 multiply to +1, so its coefficient product has the fixed real sign product_j chi4(q_j). Throughout the **entire** center window its remaining magnitude is nonnegative, because q_N>=0 and Lchi>=0 there; all chosen denominators remain active. On J it is bounded below by c(H0/T)^6. Taking delta sufficiently small makes cos(2pi x Lambda)>=1/2 throughout the entire fixed x window, not just on J. The real part of the complete tuple integral, after multiplication by its fixed sign, therefore has no negative contribution outside J. Its modulus is at least cT^2(H0/T)^6.

Multiplying by the number of tuples gives cT^6 H0. The paired subcollection costs only O(T^2 H0^3) on this denominator range, either by its O(M^3) count or its restricted square-sum. Since T^4/H0^2 tends to infinity, deleting paired tuples preserves the lower order cT^6 H0. This is rigorously a lower bound for a sum of individual tuple moduli. Characters differ between different tuples, so it supplies no lower bound for the signed nonpaired integral or the physical moment. The candidate maintains precisely this distinction.

### Independent blind tuple control

The isolated report first proves the full-line six-fold translation correlation is close to integral K^6>0 for five sufficiently small offsets, using translation continuity with the explicit L6 derivative bound. It then chooses R_K so that the sum of **both** omitted endpoint tails is at most one quarter of this positive mass in absolute value. Consequently each selected complete interval integral is positive. This is the correct order of argument and does not infer whole-interval positivity from a positive subinterval.

There are at least L/4 permissible anchor integers and at least delta H choices for each of the five offsets. Thus the lower count is a constant times LH^6. The stated six-distinct-indices variant uses the falling factorial and holds for sufficiently large H. The upper bound follows by Tonelli from sum_m|K((x-m)/H)|<=C H. For H>=B the full constant-coefficient packet is identically zero, so its total positive and negative tuple masses are equal. This demonstrates the signed-versus-absolute obstruction without any arithmetic transfer.

## 4. First doubtful or unproved step

No unproved step was found in the reviewed component statements under their printed hypotheses. The first open step remains the one-sided upper estimate for the full nonpaired signed common-center sextuple aggregate at T^(2+1/100+epsilon)H0^3, uniformly across all required blocks and endpoints. Exact nonpaired relations across different denominators are included in that gap.

The reviewed absolute-certificate obstruction refutes using this particular tuplewise-modulus estimate at the target budget. It does not refute S6 or all signed-dispersion approaches. The blind LH^6 example is separately scoped and cannot replace the actual interior-block certificate.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| Hyperbola, square sign, nonintegral R | PASS; direct factor inequalities above give distance at least R for every nonsquare error. |
| Both Fourier branches and factor four | PASS; independently rederived residue factor, signs, and odd-q/4-divisible-q split. |
| Moving endpoints and BV | PASS; jump sizes sum to O(1), with only first-order oscillatory decay asserted. |
| Paired and single-denominator sectors | PASS at printed scopes; overlap and remaining mixed exact relations remain visible. |
| Actual primitive rational count | PASS; odd-prime union bound retains positive area and summed boundary errors are lower order. |
| Actual full-window negative contributions | PASS; coefficient sign is fixed and the cosine remains positive throughout the full window. |
| Blind positive-index tails | PASS; both signs and H/d prefactors retained. |
| Blind tuple endpoints and signed total | PASS; whole-line correlation precedes two-tail subtraction; signed total remains zero. |
| Shared exact diagnostics | Archived manifest/JSON report every named control passed; no new run was performed by this reviewer. These finite controls are diagnostic only. Disclosed erroneous sharp expression and warning are not used as mathematical evidence. |
| Source scope | Supplied source-check record is appropriately limited to fixed real-order Bessel identities, not S6. This arithmetic review does not certify a fresh external-source audit. |
| Nonauthor and history preservation | PASS; only this new review path was written; frozen candidate/reports and shared state were not edited. |

## 6. Exact dependencies and reviewed hashes

The protocol was already read in the initial assignment and retained. The brief, candidate, both arithmetic/control reports, shared control records, and source-check record were read; the graph's relevant statuses and current campaign metadata were inspected. The initial combined output truncated part of the arithmetic report, so that report was immediately reread separately in full before review. No conclusion rests on truncated unseen text. No unlisted new local context or further discovery was used.

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306 |
| state/active_campaign.yml | 48353e0fea3b38fad5c64829b22280d989c0631aed0fd8304f8b4290b6b8cc54 |
| briefs/arithmetic_dispersion_review.md | 29fff904fa4f69aa5bf696c412e01c03ec613124bcd990ff446554101735ef7f |
| candidates/conductor_signed_sixth.md | cee1d243f21577e090acb0f9387c0412f4f70748b918aa3661e64db15586a8f3 |
| controls/control_manifest.md | a2751a7fbca018496711c9002732a9bb76b0474cd588f654915f6b1fe538d385 |
| controls/exact_local_controls.json | 2e6cdf957006c16d4c43455e9151073c36b02732ba7280648c16e2caaf05e7e3 |
| controls/source_check.md | 315c1b7dbd28f1b69836aabc3a90c7899f73ec5ff913dcd98fffcB30767fc3dd |
| reports/signed_fraction_dispersion.md | 9406863b09750d841adde32c46b71e3581c529de76e5d48a46a1902d1532c253 |
| reports/blind_packet_control.md | 755a6e08d18868c02b6a3bdb971b66ff1709496fd845c41bee8006ed8aef89c0 |

Abbreviated campaign paths in the table are relative to `rounds/codex-managed/gc-signed-sixth-dispersion/`. The live campaign hash is a read snapshot. The starting graph is unchanged and its target remains open; accepted algebraic/distribution nodes do not supply the missing S6 estimate.

## 7. Recommended state effect and stop

**PASS and retain** the reviewed components and the exact open signed owner as campaign evidence. The reviewed candidate's identity State Patch recommendation is appropriate. Do not promote S6, the improved full-band/complete moment, sharp102/325, or any parent/quarter conclusion.

No repair is requested. This bounded review is complete; stop without further discovery, frozen-file edits, shared-state edits, or successor work.
