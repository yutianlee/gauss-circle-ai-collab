## 1. Result.

The frozen packet determines the exponents and the logical shape of two
canonical targets, but it does **not** yet determine either target as a
standalone theorem about explicitly defined finite sums.

For M1, the intended irreducible assertion is the actual-symbol,
signed four-row estimate

\[
 \mathcal E_{\mathrm{hard}}(U)
 \ll_\varepsilon X^\varepsilon {U\over B}J^{14/5}.
\tag{M1-H}
\]

Its normalization and capacity ledger are internally consistent.  If
the stated one-count decomposition is made literal and every already
owned energy piece has the same target bound, the displayed Toeplitz
inequality square-roots (M1-H) to the coefficient target
\(J^{7/5}=J^2/T\).  This implication closes only the first-band smooth
nonaxial coefficient core.  It does not close the other listed M1
owners or any global endpoint theorem.

For M2, the intended irreducible assertion is the joint
density--discrepancy estimate

\[
 \sum_{A,D,K,G,R}|\mathfrak Q_{A,D,K,G,R}|
 \ll_\varepsilon L^2X^\varepsilon,
\tag{M2-H}
\]

with \(\mathfrak Q\) formed using the *complete* kernel
\(\mathcal K_R=\mu_R\mathcal K_0+
\sum_{r\ne0}\widehat W_R(r)\mathcal K_r\).  The block capacity
\(L^2\sqrt\rho\), target \(L^2\), and required relative gain
\(\rho^{-1/2}\) are consistent.  However, the packet does not display
the normalized row-Cauchy/energy identity needed to derive the
pointwise endpoint estimate from (M2-H).  That implication is therefore
only asserted, not independently derivable from the permitted data.

The owner maps also are not standalone: phrases such as “not
previously owned,” “deep,” “residual,” and the named historical pieces
do not specify disjoint sets.  Consequently the appropriate verdict is
**revise, with no promotion**.  The target exponents and capacity
calculations may be retained, but graph-ready theorem statements require
explicit dictionaries, finite index sets, one-count complement maps,
and the missing downstream bridge.

## 2. Exact statement and hypotheses.

The smallest correct statements that can be reconstructed from the
packet are the following conditional theorem schemas.  The missing data
listed below are hypotheses that a standalone version must spell out;
they cannot be inferred or replaced by generic bounded coefficients.

**Common data.**  Let

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5}.
\]

For the M1 band, require

\[
 J^{13/18}<C\le J^{3/4},\qquad B=C/T,
 \qquad J^{11/90}<B\le J^{3/20},\qquad M\asymp B.
\]

All estimates are uniform in every admissible dyadic scale, parity
class, sign, endpoint convention, and fixed smooth seminorm.  Floors,
stars, equality samples, hard endpoints, and zero extension are part of
the data.

**M1 standalone schema.**  A complete statement must provide:

1. a positive-integer range for the Fejer length \(U\), the exact
   normalization of \(D_U\), and the exact definitions of
   \(\Pi_{b,U}\), \(F_{b,P}\), the index \(P\), and the condition
   \(x\ne y\), hence of \(H_{b,U}\);
2. the modulus and residue dictionary for \(M,K,b,d,n,m,A,B_2,V\),
   the centered term \(c_M(d)\), the support endpoint \(\Delta_b\),
   and the complete sum \(\mathfrak T_M(u,A,B_2,V)\);
3. the literal stationary symbol \(I_b\), with its entry, exit, sign,
   parity, and zero-extension conventions, so that
   \(\Omega_{b,d,u}(n,m)\) is exactly the four-weight product in the
   packet;
4. an explicit finite hard-cell set \(\mathscr H_{b,U}\), defined as
   the complement of four explicit, pairwise disjoint earlier cell
   sets inside the nonzero-\(u\) universe, with
   \(R_*>\rho_*\), \(\mathfrak a<M^2/\rho_*^2\), and
   \(\rho_*=\min(M,\lfloor J^{11/30}B^{-2}\rfloor)\); and
5. literal inclusion in \(\mathscr H_{b,U}\) of residual bad-prime
   cells, the full nonunit union, both sorts of periods, shallow
   good-prime lifts, aperiodic factors, all signs and reflected
   orientations, and every nonzero modulus multiple.

With those data, define \(\mathcal E_{\mathrm{hard}}(U)\) by the sum
in (92.17), replacing both “\(\sigma\) not previously owned” and
\(\sum^{\mathrm{deep}}\) by the explicit membership predicate for
\(\mathscr H_{b,U}\).  The standalone open assertion is (M1-H), in
the usual absolute-value meaning of \(\ll\).

For its advertised coefficient consequence one must additionally
state the exact identities

\[
 \mathcal E_U=\mathcal E_{u=0}
 +\mathcal E_{87}+\mathcal E_{88,\mathrm{coarse}}
 +\mathcal E_{88,\mathrm{good}}+\mathcal E_{89,\mathrm{safe}}
 +\mathcal E_{\mathrm{hard}},
\tag{M1-P}
\]

with disjoint index sets, and

\[
 \mathfrak X_{82}=\mathfrak O_{83:86}
 +\sum_U\sum_{b\asymp B}H_{b,U}(0),
\tag{M1-R}
\]

with exact one-count ownership.  A sufficient downstream hypothesis is
that \(\mathcal E_{u=0}\) and the four nonhard terms in (M1-P) have
total size \(\ll_\varepsilon X^\varepsilon(U/B)J^{14/5}\), and that
\(\mathfrak O_{83:86}\) is coefficient-target safe.  The packet says
these facts are owned, but does not restate their bounds or domains.

**M2 standalone schema.**  For each dyadic
\(1\le L\le X^{1/4}\), a complete statement must provide:

1. the exact normalized symbol \(a_{\mathrm{end}}(h,m)\), including
   the affine lower edge, upper edge, equality/star conventions,
   profiles, and zero extension;
2. the precise dyadic ranges and boundary convention for
   \((A,D,K,G,R)\), and an explicit disjoint partition of all pairs
   surviving the owned collars, modes, equality families, square
   families, safe blocks, and boundary ranges;
3. for every residual pair, the exact relation defining the half-angle
   variable \(u\), the orientation of \((a,b)\), the set
   \(\mathcal G_{a,b}\), the \(k\)-range and weight \(\omega(k)\), and
   the complete amplitude \(A^\circ_{ga,gb}(x)\);
4. oddness of \(g,a,b\), coprimality \((a,b)=1\), and every support
   condition required to make the interval \([gb/4,ga]\) and the
   reciprocal interval literal; and
5. enough regularity or finite Fourier truncation for \(W_R\) to make
   (92.30)--(92.33) an exact interchange of sums and integrals.

With these data, define \(\mathfrak Q_{A,D,K,G,R}\) exactly by (92.34),
using the full \(\mathcal K_R\), and assert (M2-H).  Neither
\(\mu_R\mathcal K_0\) nor the centered \(r\ne0\) part may be removed
or estimated as a substitute theorem.

To make the endpoint implication standalone, an exact normalized
bridge of the following scale is also necessary:

\[
 |\mathcal T_{\mathrm{end},L}|^2
 \ll_\varepsilon X^\varepsilon L
 \left(\mathcal R_{\mathrm{owned},L}
 +\sum_{A,D,K,G,R}|\mathfrak Q_{A,D,K,G,R}|\right),
 \qquad
 \mathcal R_{\mathrm{owned},L}\ll_\varepsilon L^2X^\varepsilon.
\tag{M2-B}
\]

Here \(\mathcal R_{\mathrm{owned},L}\) must be explicitly defined from
the complementary one-count sets.  Formula (M2-B) records the minimal
normalization needed for the claimed \(L^{3/2}\) endpoint conclusion;
it is not supplied by the packet and is therefore not being promoted as
an accepted identity.

## 3. Proof or derivation.

No proof of either missing signed estimate is present in, or claimed by,
the statement packet.  The deductions that can be checked are the
following.

First, the M1 band gives

\[
 {C\over T}>J^{13/18-3/5}=J^{11/90},\qquad
 {C\over T}\le J^{3/4-3/5}=J^{3/20}.
\]

The accepted physical normalization is multiplicative under the two
squarings:

\[
 Q^{-5/24}\quad\longmapsto\quad
 (Q^{-5/24})^2=Q^{-5/12}\quad\longmapsto\quad
 (Q^{-5/12})^2=Q^{-5/6}.
\]

Thus the coefficient row, an ordered pair, and a four-row Gram term
are not interchangeable.  The four copies of \(I_b\) in
\(\Omega_{b,d,u}(n,m)\) agree with the Gram-level normalization.

For a fixed \(U\), suppose (M1-P) is literal, all its nonhard terms
obey the stated target, and (M1-H) holds.  Then

\[
 \mathcal E_U\ll_\varepsilon
 X^\varepsilon{U\over B}J^{14/5}.
\]

The displayed Toeplitz inequality consequently gives

\[
 \left|\sum_{b\asymp B}H_{b,U}(0)\right|^2
 \ll_\varepsilon X^\varepsilon {B\over U}
 \left({U\over B}J^{14/5}\right)
 \ll_\varepsilon X^\varepsilon J^{14/5}.
\]

Taking a square root and renaming \(\varepsilon\) yields
\(\ll_\varepsilon X^\varepsilon J^{7/5}\).  If the \(U\)-sum is
dyadic or otherwise has only an \(X^\varepsilon\)-admissible number of
terms, and if (M1-R) and its owner bound are literal, this is exactly
the stated coefficient scale \(J^2/T=J^{7/5}\).

The M1 capacity calculation is also exact:

\[
 \mathsf C_{82}=B^3T^2Q^{-5/12}
 =B^3J^{6/5}J^{-1/6}=B^3J^{31/30},
\]

so

\[
 \Gamma_{82}={\mathsf C_{82}\over J^{7/5}}
 =B^3J^{-11/30}.
\]

At the lower band edge this ratio tends to the equal-capacity scale;
at the top edge \(B=J^{3/20}\) it is \(J^{1/12}\).  Since

\[
 {\mathsf C_{\mathrm{deep}}\over\mathsf T_{\mathrm{deep}}}
 ={(U/B)\mathsf C_{82}^2\over (U/B)\mathsf T_{82}^2}
 =\Gamma_{82}^2,
\]

the top Gram gap is \(J^{1/6}\), and the Toeplitz square root returns
the same \(J^{1/12}\) linear gap.  This is only a capacity comparison;
it proves neither a lower bound nor cancellation.

For M2, linearity in the metric window gives, once convergence is
justified,

\[
 \mathcal K_R
 =\sum_k\omega(k)\left(\mu_R+
 \sum_{r\ne0}\widehat W_R(r)e(r\Omega/k)\right)e(kx)
 =\mu_R\mathcal K_0+
 \sum_{r\ne0}\widehat W_R(r)\mathcal K_r.
\]

Therefore the density and discrepancy modes are constituents of one
coefficient kernel.  The target is a signed bound for the resulting
\(\mathfrak Q\), not a positive estimate for either constituent.
Also, if \(g,a,b\) are odd, then

\[
 \chi_4(ga)\chi_4(gb)=\chi_4(a)\chi_4(b)
 =(-1)^{(b-a)/2},
\]

so the displayed sign identity is algebraically correct under the
oddness hypothesis.  The claimed cancellation of quotient parity and
restoration of integer Fourier frequencies cannot be checked without
the omitted complete coefficient formula.

Finally, if the missing bridge (M2-B) is supplied, (M2-H) gives

\[
 |\mathcal T_{\mathrm{end},L}|^2
 \ll_\varepsilon L^3X^\varepsilon,
\]

and hence
\(\mathcal T_{\mathrm{end},L}\ll_\varepsilon
L^{3/2}X^\varepsilon\).  This verifies the exponents but not the
unstated bridge.  On a hard block the positive capacity divided by the
target is

\[
 {L^2\sqrt\rho\over L^2}=\sqrt\rho,
 \qquad \rho={AJD^3\over L^3},
\]

so \(\rho\ll1\) is safe and \(\rho\gg1\) requires precisely the
relative factor \(\rho^{-1/2}\).

## 4. First doubtful or unproved step.

For the M1 Gram target, the first direct definitional seam is that
\(D_U\) and the admissible range of \(U\) are never defined.  More
decisively, (92.17) is not a finite sum specified by predicates:
“\(\sigma\) not previously owned” and \(\sum^{\mathrm{deep}}\) have no
set definitions.  Hence \(\mathcal E_{\mathrm{hard}}(U)\) cannot be
reconstructed uniquely, and neither disjointness nor exhaustion in
(92.14) can be proved.  Earlier coefficient formulas also leave
\(\Delta_b\), \(c_M(d)\), \(\Pi_{b,U}\), \(F_{b,P}\), and the relation
of \(K,M,b\) undefined.  The first missing M1 seam to repair is thus an
explicit variable dictionary followed by a literal hard-cell
complement predicate.

For the M2 kernel, the earliest unmistakable missing symbol is the
half-angle variable \(u\) in (92.27): no formula relates it to
\((a,b)\) or \((h,s,g)\).  Subsequently “\(a,b\) residual,”
\(\mathcal G_{a,b}\), the block ranges \((A,D,K,G,R)\),
\(A^\circ_{ga,gb}\), and \(\omega\) are not defined.  Thus
\(\mathfrak Q\) and its one-count domain are not determined.  There is
also an apparent naming collision that must be resolved: the owner
list says “zero and positive modes” are already owned, while the hard
kernel must retain the density mode \(r=0\).  These must be different
mode indices, but the packet does not label them.

Even after those definitions are supplied, the first unproved
downstream step for M2 is the exact original-to-energy relation.  The
packet says that accepted row Cauchy and subsequent transformations
imply (92.24), but gives neither an equality nor an inequality with its
normalizing factor and owned remainder.  The exponent-compatible
formula (M2-B) must be recovered and checked before (M2-H) can imply the
endpoint target.

Neither (M1-H) nor (M2-H) itself is proved.  The packet explicitly
freezes them as open signed estimates, and no source theorem is an
accepted dependency.

## 5. Required controls and outcomes.

| Control | Outcome |
|---|---|
| Common scale dictionary | **Pass for exponents:** \(J,Q,T,C,B,M\) and \(D_1\) are given, and the M1 \(B\)-range follows correctly. **Fail for a standalone sum:** the additional M1 and M2 variables listed in Sections 2 and 4 are not defined or quantified. The renaming of the Fejer length to \(U\) avoids the stated collision with denominator scale \(D\), but does not define \(U\). |
| M1 coefficient and centering algebra | **Not auditable:** the Kloosterman convention, \(K\), \(c_M(d)\), modulus-multiple convention, and exact symbol are absent. The packet explicitly requires negative \(d\), nonzero multiples of \(M\), Ramanujan centering, all parity classes, and reflected orientations; none may be dropped. |
| M1 linear/pair/Gram normalization | **Pass:** \(Q^{-5/24}\), \(Q^{-5/12}\), and \(Q^{-5/6}\) are successive squares, and the Toeplitz step square-roots the Gram target back to \(J^{7/5}\). |
| M1 diagonal and one-count map | **Fail as standalone:** literal \(d=0\) is assigned before the survivor and there is one global \(u=0\) owner, but the named pieces in (92.12) and (92.14) have no set predicates. “Successive complements” is a construction instruction, not a verifiable partition. |
| M1 hard support and endpoints | **Partial:** actual stationary support, entry/exit, outer collar, signs, endpoints, and zero extension are declared literal. Their formulas and boundary inequalities are omitted, so equality ownership and exact support cannot be checked. |
| M1 top capacity | **Pass:** \(\Gamma_{82}=B^3J^{-11/30}\), with top value \(J^{1/12}\); the corresponding Gram ratio is \(J^{1/6}\). This is an equal-capacity barrier only. |
| M1 outside-core scope | **Pass as an exclusion list:** upper conductors \(C>J^{3/4}\), axes, raw transitions, cone edges, other radial sectors, alpha/top interfaces, and final endpoint uniformity remain outside. The hard theorem cannot promote M9-M1 or the final target. |
| M2 character identity | **Pass conditional on explicit oddness:** for odd \(g,a,b\), the displayed \(\chi_4\) identity holds. The claimed carrier-level parity and integer-frequency correction is **not auditable** because the carrier formula is absent. |
| M2 hard endpoint and zero extension | **Partial:** the lower affine edge, upper support edge, stars, and profiles are declared part of \(a_{\mathrm{end}}\), but the symbol and its extension are not given. Consequently (92.24) is an actual-symbol reference target, not a self-contained sum. |
| M2 density plus discrepancy | **Pass structurally:** (M2-H) uses the full \(\mathcal K_R\), so \(\mu_R\mathcal K_0\) and all centered \(r\ne0\) modes remain together. Any theorem for discrepancy alone is insufficient. The ambiguity with the separately “owned zero modes” must be removed by naming both indices. |
| M2 one-count owner map | **Fail as standalone:** the four historical owner groups are described, but “residual,” \(\mathcal G_{a,b}\), safe-block boundaries, bounded boundary range, and equality conventions are not set-theoretic definitions. Disjointness and exhaustion cannot be verified. |
| M2 hard-ratio capacity | **Pass:** positive capacity is \(L^2\sqrt\rho\), the target is \(L^2\), and the hard region requires exactly \(\rho^{-1/2}\). Ordinary \(1/R\) density is part of this ledger, not an exceptional family. |
| M2 original-to-energy implication | **Fail as standalone:** the necessary Cauchy/energy bridge, its prefactor, and its owned remainder are not displayed. The exponent calculation works conditionally on a bridge of scale (M2-B). |
| M2 outside-core scope | **Incomplete:** the packet excludes “all other M2 packets and target-scale endpoint owners,” but does not enumerate them. Thus (M2-H) closes at most the displayed hard top cone and cannot promote M9-M2, an endpoint statement, a bridge, or the final target. |
| External-source hypotheses | **No dependency available:** the packet makes Li--Yang and Xiao guardrails only and accepts no theorem from them. Under statement-only isolation, no primary-source hypothesis can be imported to fill either seam. |

All eight rejected shadows were also checked:

1. Generic bounded coefficients are not a substitute for either actual
   symbol.
2. Absolute values cannot be taken before the required joint signed
   interaction.
3. The M1 linear row is not its Gram square.
4. M1 period depth, Fourier support, and graph sparsity do not supply a
   power gain without an actual-symbol estimate.
5. Nonzero modulus multiples, Ramanujan terms, bad-prime cells, and
   full \(2\)-adic branches must remain.
6. M2 quotient parity, a half-frequency gap, discrepancy alone, and a
   further reciprocal Poisson step do not prove (M2-H).
7. The ordinary \(1/R\) density is not exceptional and must remain in
   the full kernel.
8. An unspecified global moment cannot imply the required pointwise
   endpoint bound.

The required control outcome is therefore mixed: all numerical
normalizations and required-gain ledgers pass, while both variable
dictionaries, both literal owner maps, hard support verification, and
the M2 downstream seam fail the standalone criterion.

## 6. Dependencies and exact artifacts used.

Only the following two permitted artifacts were used:

1. `rounds/codex-managed/m9-canonical-core-formalization/briefs/blind_canonical_core_rederivation.md`;
2. `rounds/codex-managed/m9-canonical-core-formalization/derivation_packet.md`.

No proof graph, proof draft, strategy file, prior report or synthesis,
sibling Round-92 report, source card, web source, or external theorem
was read or used.  No numerical experiment was needed; every
calculation above is direct exponent or character algebra from the
statement packet.

## 7. Recommended state effect.

**Revise; no promotion.**  Retain the frozen M1 and M2 target exponents,
the three-level M1 normalization, the M1 top-capacity calculation, the
M2 \(\rho^{-1/2}\) required-gain ledger, the joint
density--discrepancy requirement, the false-shadow exclusions, and the
stated limited downstream scope.

Before either core is graph-ready, add (i) a complete variable and
actual-symbol dictionary, (ii) explicit finite universes and disjoint
successive-complement owner predicates, including every equality and
zero convention, (iii) a literal formula for each hard block and its
support, (iv) a distinction between the already owned M2 zero-mode
index and the retained density index \(r=0\), and (v) the normalized
row-Cauchy/energy bridge from the original M2 endpoint sum to the block
sum, with its owned remainder.  Also enumerate the M2 owners outside
the hard top cone.

Formalization of those seams would make the two statements
well-posed; it would not prove either signed estimate.  No M9-M1,
M9-M2, M9, endpoint, bridge, or conjectural target promotion is
licensed by this report.
