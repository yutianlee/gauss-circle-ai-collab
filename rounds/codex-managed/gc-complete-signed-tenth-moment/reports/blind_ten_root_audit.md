# Round 209 — statement-only ten-root audit

Campaign: `gc-complete-signed-tenth-moment`  
Task/role: `blind_ten_root_audit`; independent statement-only rederivation  
Generated: 2026-09-27  
Graph hash: not supplied in the isolated packet; deliberately not inspected  
Status: independent evidence, not an accepted graph claim

## 1. Result: lemma and methodological no-go

Assertions 1 and 2 are valid, with constants depending on the fixed weight bounds and fixed test functions. Exact square-root relations need not be pairings; counting all squarefree-class blocks proves the asserted exact-mass bound nonetheless.

For every compact set K contained in (1/2,1), there are positive constants c_K and T_K such that, uniformly for alpha in K and N=T^alpha,

\[
 A_{10}\ge c_K N^2\qquad(T\ge T_K).
\]

Consequently the proposed scale U=T^(83/65)N^(-1/2) cannot upper-bound the termwise absolute nonzero-frequency expansion when alpha is fixed in (166/325,242/325). This obstruction survives exact-frequency removal.

It does not refute an upper bound at scale U for the actual tenth moment. Nor does it establish that cancellation after collecting terms with the same total frequency is impossible. An explicit displaced Dirichlet-kernel control below has a bounded tenth moment on the observation interval while its nonzero-frequency absolute expansion grows like at least the ninth power of the packet length.

The proof uses two analytical mechanisms: squarefree-class decomposition, and weighted frequency localization. The geometric-series example is an exact control of the latter mechanism. No mathematical numerical experiment was used.

## 2. Exact statements and hypotheses

Let N>=2 and k>=2 be fixed. Let each of 2k weights satisfy

\[
 |b_j(n)|\le C_j\tau(n)n^{-3/4},\qquad N\le n\le4N.
\]

For every fixed sign vector epsilon_j in {+1,-1},

\[
 \sum_{\substack{N\le n_1,\ldots,n_{2k}\le4N\\
                  \sum_j\epsilon_j\sqrt{n_j}=0}}
 \prod_{j=1}^{2k}|b_j(n_j)|
 \ll_{k,\eta,\{C_j\}}N^{-k/2+\eta}
 \qquad(\eta>0).                                      \tag{2.1}
\]

In particular, a signed version of the mass satisfies the same bound in absolute value. The implicit constant must include the specified weight bound; it cannot be independent of an arbitrary C_j.

For assertion 2, use precisely the packet's r2, v, Psi, w, a_n and Fourier-transform convention. Assume T>=2, N>=N_0, and N<=T^c for a fixed c<1. For T sufficiently large depending on c and Psi, and all such N,

\[
 A_{10}\ge c_0N^2-C_\eta T N^{-5/2+\eta}.              \tag{2.2}
\]

Here c_0>0 and C_eta depend only on the fixed test functions, eta, and harmless fixed range parameters. The symbol eta denotes an arbitrarily small positive exponent and is unrelated to the signs.

For uniformity over a compact K subset (1/2,1), take c=max K<1. The usual phrase "large T,N" means sufficiently large thresholds depending on these fixed data. No positivity of the Fourier transform of w is assumed or needed.

Define the actual smoothed tenth moment, when comparing it with the expansion, by

\[
 M_{10}(T,N)=\int_{\mathbb R}w(R/T)H_N(R)^{10}\,dR.
                                                               \tag{2.3}
\]

This is nonnegative, since w>=0 and H_N is real. All sums used below are finite.

## 3. Proof and derivation

### Mechanism I: all squarefree-class blocks, including non-pairings

Write every positive integer uniquely as n=q l^2, with q squarefree and l>=1 an integer. Linear independence of distinct squarefree radicals implies

\[
 \sum_j\epsilon_j\sqrt{n_j}=0
 \quad\Longrightarrow\quad
 \sum_{j:q_j=q}\epsilon_j l_j=0\quad\text{for every }q. \tag{3.1}
\]

Thus the index set partitions into squarefree-class blocks of sizes m>=2. A singleton cannot satisfy its equation. There are only finitely many partitions of 2k labeled indices, with their number depending on k alone.

For a particular block of size m and particular q<=4N, every l lies in

\[
 [\sqrt{N/q},2\sqrt{N/q}].
\]

This interval contains O(sqrt(N/q)) integers uniformly for q<=4N, because sqrt(N/q)>=1/2. Choosing the first m-1 entries leaves at most one possible final entry in the signed linear equation. Therefore the number of block solutions, after summing over squarefree q and then enlarging to all q, is at most

\[
 B_m\ll_m N^{(m-1)/2}
       \sum_{q\le4N}q^{-(m-1)/2}
 \ll_m
 \begin{cases}
 N,&m=2,\\
 N\log(2N),&m=3,\\
 N^{(m-1)/2},&m\ge4.
 \end{cases}                                                \tag{3.2}
\]

In every case B_m<<_m N^(m/2); for m=3 the available N^(1/2) margin absorbs the logarithm. For a fixed partition, dropping the requirement that different blocks have distinct q only increases the count. Its solution count is consequently at most

\[
 \prod_B O_k(N^{|B|/2})=O_k(N^k).
\]

Summing over all partitions shows that the raw exact relation count is O_k(N^k). On [N,4N], the divisor bound gives

\[
 \prod_{j=1}^{2k}|b_j(n_j)|
 \ll_{k,\eta,\{C_j\}}N^{-3k/2+\eta}.
\]

Multiplication proves (2.1). No step assumes that a block has size two or that its positive and negative roots match as multisets.

### Mechanism II: a positive mass of nearby five-root sums

Put b_n=|a_n| and B=sum_n b_n. Choose a closed interval [a,b] strictly inside (1,4) on which v>=v_0>0. Such an interval exists by the hypothesis on v. Because Psi(0)=1 and Psi is continuous, the condition n<=4N<=4T^c gives Psi(sqrt(n/T))>=1/2 for all relevant n once T is sufficiently large. The supplied summatory formula for r2 yields

\[
 \sum_{aN\le n\le bN}r_2(n)
 =\pi(b-a)N+O(\sqrt N+1)\gg N.
\]

Endpoint rounding contributes only to the stated harmless error. Hence

\[
 B\ge cN^{-3/4}\sum_{aN\le n\le bN}r_2(n)
   \ge c' N^{1/4}.                                      \tag{3.3}
\]

Let W=hat w(0)=integral w>0. Continuity supplies delta>0 such that

\[
 |\widehat w(\xi)|\ge W/2\quad(|\xi|\le\delta).          \tag{3.4}
\]

Every sum S=sqrt(n_1)+...+sqrt(n_5) lies in [5sqrt(N),10sqrt(N)]. Partition this interval into J<=C_w T sqrt(N) half-open bins of length at most delta/T, using a final closed endpoint if necessary. For a bin Q define its weighted mass

\[
 c_Q=\sum_{S(n_1,\ldots,n_5)\in Q}\prod_{j=1}^5b_{n_j}.
\]

Then sum_Q c_Q=B^5. Cauchy--Schwarz gives

\[
 \sum_Qc_Q^2\ge B^{10}/J\gg N^2/T.                      \tag{3.5}
\]

Two five-tuples in the same bin have |T(S-S')|<=delta. Their contribution to the single balanced sign pattern (+,+,+,+,+,-,-,-,-,-), including zero frequencies for the moment, is bounded below using (3.4). Thus the all-sign absolute expansion with zero frequencies included, denoted A10*, satisfies

\[
 A_{10}^{*}\ge\frac{TW}{2^{11}}\sum_Qc_Q^2\ge c_0N^2.   \tag{3.6}
\]

Uniformly in T,N, the given coefficient satisfies b_n<=C tau(n)n^(-3/4), since r2(n)<=4tau(n) and the two test functions are bounded. Apply (2.1) with k=5 to each of the 2^10 sign patterns. The entire exact-frequency part removed from A10* is at most

\[
 \frac{TW}{2^{10}}\sum_{\boldsymbol\epsilon}
 \sum_{\Delta=0}\prod_{j=1}^{10}b_{n_j}
 \le C_\eta T N^{-5/2+\eta}.                            \tag{3.7}
\]

Subtracting (3.7) proves (2.2). In particular, the lower bound is not produced only by exact resonances.

For alpha in a compact K subset (1/2,1), choose eta=1/4 and write alpha_-=min K. The relative size of (3.7) is at most

\[
 C T N^{-9/2+1/4}
 =C T^{1-(17/4)\alpha}
 \le C T^{1-(17/4)\alpha_-}=o(1)                       \tag{3.8}
\]

uniformly on K. This proves the positive uniform lower bound in section 1. The range alpha>1/2 is more than is needed for this particular subtraction; no endpoint theorem is being claimed outside the stated task.

Finally,

\[
 \frac{A_{10}}{U}
 \gg T^{-83/65}N^{5/2}
 =T^{(5/2)\alpha-83/65}.                               \tag{3.9}
\]

The exponent is positive exactly when alpha>166/325. On every compact subinterval of (166/325,242/325), it has a fixed positive lower bound, so the divergence is uniform. The upper endpoint 242/325 is a restriction of the comparison requested in the packet, not a new restriction in (3.9). At alpha=166/325 this argument provides no diverging ratio. For a bound allowing an additional factor T^rho, a contradiction requires rho<(5/2)alpha-83/65; no unspecified epsilon loss may be silently ignored.

## 4. First doubtful or unproved step

There is no unproved step in (2.1), (2.2), or their stated uniform consequences, conditional on the elementary inputs explicitly permitted by the packet.

The first invalid step in a proposed deduction about the actual moment would be to convert the lower bound for A10 into a lower bound for M10. Expanding each cosine gives

\[
 M_{10}
 =\frac{T}{2^{10}}\sum_{\boldsymbol\epsilon}\sum_{\boldsymbol n}
   e^{-3\pi i(\sum_j\epsilon_j)/4}
   \Bigl(\prod_j a_{n_j}\Bigr)\widehat w(-T\Delta).      \tag{4.1}
\]

The factors in (4.1) are not nonnegative term by term. In particular w>=0 does not imply hat w>=0. Its support away from the origin permits substantial Fourier phases.

If C(lambda) denotes the sum of the signed coefficients in (4.1) over a single total frequency lambda, without the factor T hat w(-Tlambda), then aggregation gives

\[
 M_{10}=T\sum_\lambda C(\lambda)\widehat w(-T\lambda).
\]

The triangle inequality bounds the modulus of this sum from above by a frequency-aggregated absolute sum, itself bounded above by the original termwise absolute sum. None of these inequalities reverses. Cancellation may occur inside C(lambda), and may occur between different frequencies after aggregation. The estimates above neither quantify nor exclude either phenomenon for the packet's coefficients. No actual signed tenth-moment estimate is proved here.

## 5. Required controls and outcomes

**Pairing sharpness — pass.** For the balanced sign pattern, choose n_{k+j}=n_j and the admissible weights b_j(n)=n^(-3/4). The contribution of these pairings is

\[
 \left(\sum_{N\le n\le4N}n^{-3/2}\right)^k
 \asymp N^{-k/2}.
\]

Thus the exponent in (2.1), apart from the divisor allowance, cannot be uniformly improved for all allowed weights.

**Non-pairing class and impossible signs — pass.** For an integer m>=1 and N=4m^2, the four roots 2m,4m,3m,3m satisfy 2m+4m=3m+3m; all squares lie in [N,4N]. This is a single squarefree-class relation and is not a pairing. It is included in the m=4 block count. An all-plus sign vector has no exact solution and contributes zero, consistently with (2.1).

**Exact-frequency removal and exponent arithmetic — pass.** Equations (3.7)--(3.8) explicitly bound the total mass removed over every sign vector. Equation (3.9) records the precise threshold and the effect of a permitted extra power loss. No signed lower bound is imported into this comparison.

**Displaced signed tenth-moment control — pass, entirely analytic.** This example applies to any w allowed by the packet. Choose 0<a<b with supp(w) contained in [a,b]. Choose h>0 small enough that hb<1/4 and |hat w(h)|>=W/2. For an integer L>=40 set

\[
 D_L(u)=\sum_{j=-L}^{L}e(jhu)
       =\frac{\sin((2L+1)\pi hu)}{\sin(\pi hu)},
 \qquad F_{L,T}(R)=D_L(R/T).
\]

D_L is real. Throughout supp(w), its denominator is bounded away from zero independently of L. Consequently

\[
 I_{L,T}=\int w(R/T)F_{L,T}(R)^{10}\,dR
        =T\int w(u)D_L(u)^{10}\,du=O_w(T),              \tag{5.1}
\]

where h is now fixed as a function of w. On the other hand, write

\[
 D_L(u)^{10}=\sum_{m=-10L}^{10L}d_m e(mhu),
 \qquad
 d_m=\#\{(j_1,\ldots,j_{10})\in[-L,L]^{10}:\sum j_i=m\}.
\]

All d_m are nonnegative, and these are already the coefficients after total-frequency aggregation. To bound d_1, choose the first nine integers freely with |j_i|<=floor(L/20), and let j_10=1-sum_{i=1}^9j_i. The last integer belongs to [-L,L]. Therefore

\[
 d_1\ge(2\lfloor L/20\rfloor+1)^9\gg L^9.
\]

Even with exact frequency zero excluded, the absolute expansion obeys

\[
 T\sum_{m\ne0}d_m|\widehat w(-mh)|
 \ge T d_1|\widehat w(-h)|\gg_w T L^9.                \tag{5.2}
\]

The ratio of the actual nonnegative tenth moment (5.1) to the nonzero-frequency absolute expansion (5.2) tends to zero at least as fast as L^(-9). There is no cancellation inside a collected coefficient d_m; the cancellation in the integral is between frequencies. The observation region is displaced away from the central Dirichlet peak and all its periods.

For precision, (5.1) concerns the full tenth moment, including its exact term. It does not claim that its separately signed off-diagonal sum is O(T): that sum cancels the large exact contribution. The example establishes the logical limitation needed here, not an estimate for H_N and not a substitute coefficient model for an accepted Gauss-circle claim.

## 6. Dependencies and exact artifacts used

Only these two files were read:

1. `protocol.md`.
2. `rounds/codex-managed/gc-complete-signed-tenth-moment/briefs/blind_ten_root_statement.md`.

Mathematical inputs from the statement packet: the unique decomposition n=q l^2; the permitted independence of distinct squarefree radicals; tau(n)<<_eta n^eta; r2(n)<=4tau(n); and sum_{n<=y}r2(n)=pi y+O(sqrt(y)+1). Other steps are finite counting, Cauchy--Schwarz, continuity of a Fourier transform of an integrable smooth function, and the finite geometric-series identity.

No active state, generated general brief, historical proof, other report, or web source was inspected. No code, mathematical computation, or external theorem was used. The proof graph, proof draft, validation matrix, and synthesis were not edited.

## 7. Recommended evidence/state effect

**Promote as local evidence, subject to conductor validation:** the all-pattern exact weighted 2k-root estimate (2.1), including its non-pairing squarefree-class proof; and the exact-frequency-removed tenth-order absolute-expansion obstruction (2.2).

**Reject:** any claim that A10 is O(U) uniformly for a fixed alpha in (166/325,242/325), or uniformly on a compact subinterval, without a power allowance large enough to absorb (3.9).

**Retain as unresolved / no state change:** the actual signed tenth-moment estimate and any proposed cancellation mechanism after total-frequency aggregation. The present obstruction invalidates a termwise absolute proof at that scale, not the signed target. No global Gauss-circle obligation is discharged by this report.

The assigned report is complete. No successor round is proposed.
