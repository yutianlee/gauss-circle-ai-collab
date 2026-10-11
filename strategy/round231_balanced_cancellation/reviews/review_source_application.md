# Nonauthor review: actual KRW application and complete restoration

Round231 central-balanced packet; reviewer `balanced_reciprocal_attack`; 2026-10-11. Subject: `reports/balanced_source_audit.md`, frozen SHA256 `bd7beaa816e2443be41aaed903e92c8b884b1b827b1ea5b2fb1eb9004b0e9cd7`. Starting graph `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. Bounded nonauthor review; no shared-state edits.

## 1. Result

The KRW Proposition5 application passes the primary-source, moving-endpoint completion, product partial-summation, and exponent-bookkeeping seams. In particular arbitrary d-dependent interval endpoints really can be completed at logarithmic cost; no hidden factor equal to the number of patches is required. The optimistic combination with the elementary head and smooth high tail still reaches only ceiling1/6, hence generic twelfth-moment certificate5/3, and does not improve10beta.

The smooth Hankel tail and exact subtraction from the sharp balanced mask pass in their stated smooth scope. Their historical attribution is correct. One localized restoration sentence needs a scope correction: when b denotes only the W_low exponent, the resulting sharp x-variable moment exponent is

    max(102/25,(7+b)/2),                                (R)

not the subject's `max(4,(7+b)/2)`. The latter is valid if b is expressly the already restored complete B exponent, or if b>=29/25. The preferred b=29/25 and every no-gain conclusion are unaffected. The conductor was alerted before this review was frozen.

Recommendation: retain the source application and no-gain conclusions, with correction (R) attached to the reviewed scope; no promotion of a complete improvement.

## 2. Exact statement and hypotheses reviewed

The mathematical quantities are exactly those in `briefs/balanced_interface.md`: real T>=2, real R in [T/2,2T], actual r2 and chi4, the fixed smooth original mollifier, unnormalized M12, radius-independent patch starts, X0=T^(52/125), Z=T^(3/2), and the adaptive cutoff D_T. Review did not replace these by arbitrary signed coefficients when applying the lattice identity.

I independently opened the cited [publisher PDF](https://ems.press/content/serial-article-files/38194), printed p.303, Proposition5 and its preceding definition. Its bound is exactly

    (AB)^epsilon[(X A^6 B^6)^(1/8)+A^(1/2)B+AB^(3/4)+X^(-1/2)AB],

for positive X, A,B>=1, bounded separated coefficients, and each exponent outside {0,1}. Thus alpha=beta=1/2 is allowed; there is no alpha+beta exclusion. The proof explicitly has both X>=B^2 and X<=B^2 cases. Uniformity in the bounded coefficients is sufficient for the completion argument below. No additional source theorem was searched for or imported.

For the Hankel seam I also opened the cited [Berndt–Dixit–Kim–Zaharescu Theorem1.1](https://arxiv.org/html/1701.07460) and the cited [DLMF expansion and remainder section](https://dlmf.nist.gov/10.17), with its [angular-integral reference](https://dlmf.nist.gov/10.9). The source's compact smooth specialization has no endpoint half-weight term, and the report separately derives it from ordinary two-dimensional Poisson summation. The supplied shell test is real and smooth with support away from zero.

## 3. Independent derivation and seam checks

### 3.1 Moving fibre intervals really cost only a logarithm

Let I_d be any interval of integers within the ambient dyadic m interval J of length O(M). The endpoints may depend arbitrarily on d; monotonic dependence is not needed for this completion lemma. Put

    K_d(t)=sum_(v in I_d) e(-tv),       0<=t<=1.

Integer Fourier orthogonality gives the exact identity

    1_(m in I_d)=integral_0^1 K_d(t)e(tm)dt             (m integer).

Geometric summation gives `|K_d(t)|<=G_M(t)`, where one can take a fixed constant times `min(M,||t||^(-1))`, with its value at t=0 defined as that constant times M. Empty and singleton intervals are included. Furthermore `integral G_M<<log(2M)`.

Inside this integral, replace phi_d by `phi_d K_d(t)/G_M(t)` and psi_m by `psi_m e(tm)`. Both resulting vectors have modulus at most one. For every fixed t, KRW therefore applies on the same full ambient rectangle, with the same X,A,B. Its bound is independent of t, and integration costs only O(log(2M)). This proves exactly the extension needed in the subject report. It is not an application of KRW to an arbitrary two-variable coefficient matrix.

For actual W_*, orient the pairs by d<m and assign the diagonal once. After swapping the reversed pairs, the off-diagonal coefficient is chi4(d)+chi4(m); these are two separated terms. With d the smaller factor, the one inequality `d>=D_T(x(dm))` implies the other balanced-factor inequality. Because x(dm) and D_T are nondecreasing in m, this is an upper-interval condition. Its intersection with d<m, global norm endpoints and the ambient dyadic interval remains one interval. Equality at the adaptive boundary is retained. The separate diagonal has absolutely bounded normalized size by `sum d^(-3/2)` and costs no exponent.

### 3.2 Product partial summation preserves the completion hypothesis

Let F(s) be the original smooth norm amplitude, including any fixed smooth norm cutoff, on a shell s~N. Its size plus total variation is `O_L(N^(-3/4)(1+N/T)^(-L))`. For a shell upper endpoint b, write

    F(dm)=F(b)-integral_(dm)^b F'(u)du.

Interchange the finite sums and integral. Each integrand acquires the additional condition dm<=u, equivalently m<=u/d. It intersects the previous I_d in another interval; the preceding completion bound is uniform in u and its endpoints. Thus ordinary one-dimensional partial summation in the product variable is valid. It costs the stated size plus variation, followed by only logarithmic dyadic recombination. No mixed-derivative hypothesis for an arbitrary sharp two-variable mask has been smuggled in.

### 3.3 Every KRW power after normalization

Take A=D, B=M, DM~N, D<=C sqrt(N), X=R sqrt(DM), and multiply by N^(-3/4). The four terms become, up to fixed shell constants,

    T^(1/8)N^(1/16),
    N^(1/4)D^(-1/2),
    D^(1/4),
    T^(-1/2).

These agree with (K). In particular the first term is the absolute normalized bound; it is not a multiplicative saving. Reversing the source orientation does not improve the controlling aspect-ratio exponent: writing D=T^delta, N=T^nu, the reversed larger term has exponent `(nu-delta)/4`, at least the maximum improvement obtainable from the original pair throughout `0<=delta<=nu/2`.

With `delta_min=-533/5250+29nu/84`, the original aspect-ratio exponents are bounded by `533/10500+13nu/168` and `nu/8`. The difference between `1/8+nu/16` and the former is

    1559/21000 - 5nu/336 > 0           for 52/125<=nu<=3/2,

and its difference from nu/8 is `1/8-nu/16>0` in that interval. Hence the report correctly identifies the controlling KRW term. The first expression above follows from `1/8-533/10500=1559/21000`; this is an exact rational check.

Schwartz decay moves the full source maximum to N~T, producing gamma=3/16. Then `max(1,10gamma,1+20gamma/13)=15/8`. Restriction to N<=2T^(99/125) gives `1/8+(99/125)/16=349/2000`, still above beta. All losses from finitely many partitions can be absorbed by choosing smaller initial epsilon.

### 3.4 Independent optimistic-certificate crossing

The elementary head and the smooth actual tail give exponents nu/4 and (1-nu)/2. Their equality is at nu=2/3 with value1/6. The KRW leading exponent at that exact point is also `1/8+(2/3)/16=1/6`. More explicitly, below2/3 the head branch is smallest, while above2/3 the decreasing tail branch is smallest; inserting the KRW branch does not lower the crossing. Thus the optimistic certificate

    min(nu/4,1/8+nu/16,(1-nu)/2)

has maximum1/6. Its layer-cake moment power is `max(1,5/3,49/39)=5/3`, exceeding10beta. This is a comparison of available upper bounds, not an arithmetic lower bound or a general impossibility theorem.

### 3.5 Hankel, mask, and sharp-moment restoration

The complete radial Poisson identity is correctly specialized to a test supported away from zero, so its spatial zero term vanishes and the Fourier zero term is present. With s=sqrt(y), the leading J0 factor and original phase multiply to a difference-frequency sine and a sum-frequency negative cosine. In particular the displayed leading integral (J) has the correct sign and normalization. Keeping one correction term leaves a Bessel remainder `O((ky)^(-5/4))`; integrating against y^(-3/4) over y~N yields `O(N^(-1)k^(-5/4))`, summable with r2(k). The near shell count is `O(T^epsilon(1+T/sqrt(N)))`. These checks support the subject's shell estimate, including its N^(-1) remainder.

The high W_* identity is exact: `W_high=B_high-U_high-eta E_Z`. It preserves the original arithmetic cutoff and pays the removed high part using a full r2 transform plus the independently bounded U_high. Multiplication by eta preserves the whole-fibre bounded-variation argument. The finite L12 inequality gives full B exponent `b_full=max(29/25,b_low)` when only W_low has exponent b_low. This verifies the full-mask ownership claim.

For the sharp x-variable conversion, x=R^2 contributes d x comparable to T d R and the twelfth power of the usual discrepancy factor R^(1/2) contributes T^6. Thus the transformed moment exponent is `(7+b_full)/2`, together with the inherited baseline4. Substitution gives

    max(4,(7+max(29/25,b_low))/2)
       =max(102/25,(7+b_low)/2).

This establishes the scope repair (R). The uncorrected sentence, read with b=b_low without a lower restriction, drops a paid complementary owner. At the intended preferred endpoint b_low=29/25 the reported102/25 remains correct.

## 4. First doubtful or unproved step

The localized textual overstatement is the sharp-moment restoration for a hypothetical b_low<29/25. It is fully repaired by (R), or by explicitly requiring b>=29/25 in that sentence. This repair does not require any new estimate.

After that correction, the first substantive unproved step is unchanged: a signed physical M12 bound for the actual remaining middle balanced mask below10beta. Neither KRW nor the smooth Hankel tail proves it. A hard sharp norm-tail theorem is outside the report's asserted scope, and no such theorem is required for the displayed eta decomposition.

## 5. Required controls and outcomes

* Primary KRW statement and alpha=beta=1/2: **PASS**, checked directly at printed p.303 and in both proof regimes.
* Arbitrary moving fibre endpoints: **PASS**, by the exact Fourier integral above, including empty/singleton intervals and coefficient normalization by a common integrable envelope.
* Product partial summation and original sharp ownership: **PASS**, since every additional product threshold preserves a single fibre interval; the diagonal is assigned once.
* Restored KRW powers and aspect ratio: **PASS**, by the independent rational calculations above.
* Optimistic1/6 crossing and no-gain conclusion: **PASS**, by an exact three-branch comparison, without numerical sampling.
* Smooth Hankel normalization, full mask and all tails: **PASS in stated scope**, including the nearest dual integer, summable Bessel remainder and actual Schwartz tail.
* Arbitrary-b_low sharp x-variable restoration: **FAIL as literally written; localized repair supplied in (R)**. Preferred29/25 milestone: **PASS and unaffected**.
* Historical attribution: **PASS**. The permitted Round205 Section5 explicitly has cutoffs52/125 and99/125; the permitted Round208 Section1 again uses the `(T/N)^(1/2)` upper norm estimate. The report does not promote this old localization as new analytic progress.
* Resource and authority: **PASS**. No numerical experiment, new source search, source/report edit, state mutation, or successor design was performed. Only this assigned review was written.

## 6. Dependencies and exact artifacts used

The sole added research report inspected was the subject identified above, whose supplied SHA256 was verified locally. Previously authorized assignment context was retained; no other sibling report was read. Primary browsing was restricted to the exact sources already cited by the subject. Full bibliographic and theorem data are in Section2; no secondary source was used.

Local hashes:

* Review brief `strategy/round231_balanced_cancellation/briefs/review_source_application.md`: `b13a88755107dd76c8a1bcf46cef9763d3815313822045ac3221ca16a9f41a22`.
* Subject `strategy/round231_balanced_cancellation/reports/balanced_source_audit.md`: `bd7beaa816e2443be41aaed903e92c8b884b1b827b1ea5b2fb1eb9004b0e9cd7`.
* `protocol.md`: `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
* `state/proof_obligations.yml`, two accepted nodes only: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
* `state/active_campaign.yml`, status only: `fd65ce5c6b117aa4ca8ed097f85e2c786621c8054ca81791aa6e5e17006a82fa`.
* `strategy/round231_balanced_cancellation/briefs/balanced_interface.md`: `cb6f283b2de16774ff946c450acabd61001b39c39ba58c6e2ab719c14050e055`.
* `strategy/round231_residual_saving/conductor_adaptive_factor_cutoff.md`: `02727c91e64931a13d3707ca15df021418d3e96510e35894e0d96a70182506fa`.
* `strategy/round231_residual_saving/reports/actual_residual_attack.md`: `0d18fa59d915809427e1758ee478ba439303748738e8ec1f86d7e95060dd0bc5`.
* `strategy/gauss_circle_strategy_checkpoint_round205_2026-09-26.md`, permitted Section5: `03e05b85fcb0fc72fe0e65869f13e33763fea3dc503e9a85d6d1e883eebdcfc4`.
* `strategy/gauss_circle_strategy_checkpoint_round208_2026-09-27.md`, permitted Section1: `ae22a1a096a380b28b4b409a478dd7f87e5b1d8727068a4231ceb31272e03cbf`.

The prior own report was not modified or treated as independent reviewer evidence. The Fourier completion, normalized powers, crossing, and repair were rederived here. This review applies to the frozen subject hash above; any author amendment is a different artifact to be identified by the conductor.

## 7. Recommended state effect

Retain the precise KRW application as a valid no-gain source comparison, and the smooth high-tail subtraction as historically known paid localization combined with the recent adaptive mask. Apply or attach correction (R) before citing the unrestricted prospective sharp-moment sentence. No accepted graph node, complete exponent, M1/M2 parent, proof draft, or quarter-theorem status should change. This bounded review is complete and designs no successor.
