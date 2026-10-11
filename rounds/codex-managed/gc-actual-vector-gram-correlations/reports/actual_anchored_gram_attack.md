# Round221 actual-vector sixth Gram chain: an anchored-average obstruction

## 1. Result

Campaign `gc-actual-vector-gram-correlations`, round221.
Task `actual_anchored_gram_attack`; discovery, NONBLIND selected context.
Date2026-09-28. Starting graph SHA256:
`a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
Prior218--220 work in this reused agent is disclosed history.

The complete actual signed I12 target at29/25 is NOT proved. One
fixed-vector mechanism was tested: retain both actual endpoint vectors
in a sixth Gram chain, average over its common absolute radius, and
then use spectral interpolation to bound the complete physical
twelfth moment. This is not a reapplication of positive r2-weighted
Cauchy from209. Its decisive proposed gain is the signed cancellation
in the common-radius integral of the whole chain.

That integral admits a uniform, fully priced estimate. If H=A* A is
the offset Gram matrix and c is the actual conjugate-paired coefficient
vector, then, with D6=sum_mu |c_mu|^2(H^6)_(mu,mu),

    integral w_*(R/T) (D_R c)* H^6(D_R c) dR
      =T w_*-hat(0)D6+O_L(T (sqrt(N)/T)^L D6).          (1)

This holds for every FIXED offset array, with no factor for its
cardinality or the matrix dimension in the error. Both frequency
signs and the original cosine phase are present before integration.
The complete resulting block certificate is

    C_N(A)=T ||c||_2^10 D6/J.                            (2)

The limitation is decisive for this named closure. On the actual
large-squarefree-class magnitudes in a block N~T^(4 beta), every
fixed offset array in the stated range has

    C_N(A) >= c T^(10 beta),                            (3)

where beta=(50 sqrt(1717)-297)/13762 and 10 beta>29/25. The proof
uses a rephased REAL conjugate-paired control with exactly the same
coefficient magnitudes, hence the same D6 for every array. It is not
the actual r2 waveform or an actual-high-point counterexample.

Thus averaging the chain does recover signed endpoint orthogonality,
but then eliminates exactly the endpoint phase information needed to
distinguish the actual waveform from that control. Its straightforward
complete upper price is T^(3+epsilon); the stronger accepted complete
bound T^(10 beta+epsilon) remains the fallback. No new exponent or
full-quarter result follows. The first missing step is identified in
Section4, and no smaller unestimated fragment replaces the objective.

## 2. Exact quantities, hypotheses and complete target

Use the actual rho,Psi,w of the accepted216 kernel. Thus rho is a
fixed nonnegative radial smooth unit-mass mollifier, Psi is its real
even Schwartz transform, and w is nonnegative, supported in[1/2,2]
and equal1 on[1/sqrt(2),sqrt(3)]. Put

    a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)),
    Q=floor(T^(2/5)),  V0=T^(13/125),
    Z_Q(R)=sum_(sf(n)>Q)a_n(T)cos(2 pi R sqrt(n)-3 pi/4).

The frozen integral I12 is the signed sum over all ordered twelve
pairwise distinct squarefree classes greater than Q, with every
positive harmonic and every cosine sign. The accepted complete
reduction gives

    M12(L_Q)<<T^(15/13+epsilon),
    |M12(Z_Q)-I12|<<T^(8 beta-1/5+epsilon),              (4)

where B_T=L_Q+Z_Q and M_p(F)=integral w(R/T)|F(R)|^p dR.
The first exponent lies below29/25 by2/325; the second is below21/25.
A one-sided I12 upper bound at29/25 is equivalent, in the usual
every-epsilon sense, to the complete physical moment milestone.
This report therefore attacks M12(Z_Q), with the head and repeated
classes already paid by (4).

For an ambient dyadic block N<n<=2N, N<=T^(3/2), set

    b_n=a_n(T)1_(sf(n)>Q,n<=T^(3/2)),
    Z_N(R)=sum_(N<n<=2N)b_n cos(2 pi R sqrt(n)-3 pi/4).

Partial endpoints and the exact mask are zeros in the coefficient
vector; the mask is not differentiated. Let the signed index set be
mu=(n,s), s in{+1,-1}, lambda_mu=s sqrt(n), and define

    c_(n,s)=(b_n/2)e(-3s/8),
    B=||c||_2^2=(1/2)sum_n b_n^2,
    D_R=diag(e(R lambda_mu)).                           (5)

The conjugacy c_(n,-)=conj(c_(n,+)) is exact, including a negative
Psi. Thus sum_mu c_mu e(R lambda_mu)=Z_N(R), a REAL function.
All signs occur in the same finite vector, without replacing a real
cosine by an arbitrary complex waveform.

Take any J>=1 real offsets |r_j|<=T/8, fixed during the common-R
integration. They may depend on T,N and the actual coefficient data.
No separation is needed for the proved statements. Put

    A_(j,mu)=e(r_j lambda_mu), H=A* A, G=A A*,
    f(R)=A D_R c, so f_j(R)=Z_N(R+r_j),
    S_m(R)=(D_R c)* H^m(D_R c)=f(R)* G^(m-1)f(R).        (6)

The original c, its mask and its phases remain at both endpoints.
Choose a fixed smooth nonnegative majorant w_* supported in[1/4,9/4]
such that w_*(u)>=w(u+s) for every |s|<=1/8. Its existence follows
by a fixed smooth majorant of the compact union of those translates.
It is only an auxiliary upper-bound window; the target still uses w.
Its support stays at positive absolute radii. All constants below may
depend on these fixed windows and Schwartz seminorms, but not J or r.

## 3. Derivation, attempted joint estimate and full cost

### A. The fixed vector and its absolute anchor in the finite chain

Spectral decomposition of the positive semidefinite H gives, for
each integer m>=1,

    S_1(R)^m <= B^(m-1) S_m(R).                         (7)

This is Holder on the spectral weights of D_R c, including any mass
in the zero eigenspace. It assumes no inverse and remains valid for
singular H. If B=0, every expression vanishes. At m=6, (7) is the
specific chain interpolation used in this attack.

The full joint arithmetic correlation, before the R integral or any
modulus, is obtained by expanding the endpoints and five interior
kernels in S_6:

    sum_(j_1,...,j_6;mu_0,...,mu_6)
      conj(c_mu0)c_mu6
      e(R(lambda_mu6-lambda_mu0)
              +sum_(ell=1)^6 r_jell(lambda_muell-lambda_mu(ell-1))). (8)

Each internal signed frequency ranges over the whole ambient block;
the two endpoint vectors carry exactly b_n. This is an identity for
the complete sixth chain, not an omitted-complement decomposition.
In particular the endpoint phase depends on the absolute common
radius R. Translating the actual samples while keeping c fixed
changes (8). All positive and negative square-root phases, including
their original rotations in c, remain.

A structural feature is now explicit: no matter how long this Gram
chain is, a common translation enters through only TWO endpoint
frequencies. It does not itself create the signed twelve-frequency
common-radius phase of the original physical moment. Any attempted
benefit of (7) must be assessed with that distinction retained.

### B. A uniform signed common-radius estimate, without a dimension loss

Let P=H^m and D_m=sum_mu |c_mu|^2 P_(mu,mu). Fourier integration gives
exactly

    integral w_*(R/T) S_m(R)dR
      =T sum_(mu,nu)conj(c_mu)c_nu P_(mu,nu)
                      w_*-hat(-T(lambda_nu-lambda_mu)). (9)

The diagonal is T w_*-hat(0)D_m. To estimate the complete offdiagonal,
use positive semidefiniteness, not a term count:

    |P_(mu,nu)|<=sqrt(P_(mu,mu)P_(nu,nu)),
    z_mu=|c_mu|sqrt(P_(mu,mu)).

Order the distinct signed frequencies. Neighboring ones are separated
by at least cN^(-1/2), since
sqrt(n+1)-sqrt(n)=1/(sqrt(n+1)+sqrt(n)); the gap between the negative
and positive halves is larger. Consequently their ordered indices
i,k satisfy |lambda_i-lambda_k|>=c|i-k|/sqrt(N).

For any fixed L>1, Schwartz decay gives the row-sum bound

    sup_i sum_(k!=i)|w_*-hat(T(lambda_k-lambda_i))|
       <=C_L (sqrt(N)/T)^L sum_(h!=0)|h|^-L
       <<_L (sqrt(N)/T)^L.                             (10)

Here T/sqrt(N)>=T^(1/4), so the argument is uniform on the entire
truncation. By 2 z_i z_k<=z_i^2+z_k^2, (10) bounds the whole
offdiagonal in (9) by C_L T(sqrt(N)/T)^L sum_i z_i^2. Thus

    integral w_*(R/T)S_m(R)dR
       =T[w_*-hat(0)+O_L((sqrt(N)/T)^L)]D_m.             (11)

No dimension factor, J factor or bound on the matrix entries by a
common maximum has been inserted. The estimate is uniform for every
fixed offset array, however singular or clustered. It is also uniform
in the endpoint phases. If D_m=0, PSD implies all contributing terms
in (9) vanish, so (11) remains literal.

This proves (1) and supplies a genuine signed estimate of the joint
correlation (8). Its restriction must be kept: uniformity for fixed
arrays does NOT authorize replacing r_j by functions of R chosen
from the high set. In that case H itself varies with R and (9) is
no longer its Fourier expansion. No such adaptive substitution is
made in the complete moment transfer below.

### C. Complete block-moment transfer and the remaining cycle

For every j, change variables x=R+r_j and use the defining window
majorant to obtain

    integral w_*(R/T)|f_j(R)|^12dR >= M12(Z_N).

Because sum_j|f_j|^12<=(sum_j|f_j|^2)^6=S_1^6, equations(7),(11)
give the complete bound

    J M12(Z_N)<=B^5 integral w_*(R/T)S_6(R)dR,
    M12(Z_N)<=C T B^5 D6/J=C C_N(A).                    (12)

This is valid for every fixed offset array; it does not need an
unproved high-point selection rule. The actual signed arithmetic
weights remain in D6 as

    K2(u)=sum_mu |c_mu|^2e(u lambda_mu)
          =(1/2)sum_n b_n^2 cos(2 pi u sqrt(n)),
    D6=sum_(j_1,...,j_6)
       G_(j_1,j_2)...G_(j_5,j_6)K2(r_j6-r_j1).          (13)

Thus the attempted closure becomes a complete weighted closed cycle,
with the actual r2(n)^2 mask in its last edge. No unweighted
exponent-pair estimate for K2 is asserted. Equation(13) is nonnegative
as a whole, since it equals sum|c_mu|^2(H^6)_(mu,mu); its summands
need not be positive. Bounds on an individual cycle or diagonal would
not suffice for (12).

A direct valid price is obtained from H^6<=Lambda^5 H, where
Lambda=||G|| and H_(mu,mu)=J:

    D6<=J B Lambda^5,
    C_N(A)<=T B^6 Lambda^5.                             (14)

The spectral norm is at least the row diagonal d_N=2#{N<n<=2N}.
For J=1 equality D6=B d_N^5 holds. The actual coefficient bound and
Schwartz decay give, for arbitrary fixed decay order M,

    B<<_epsilon T^epsilon N^(-1/2)(1+N/T)^(-M).

Consequently the singleton-array version of the entire mechanism
gives

    M12(Z_N)<<_(epsilon,M)T^(1+epsilon)N^2(1+N/T)^(-M). (15)

The chain has been estimated, rather than left as a formal identity,
but this restored cost is far too large. The next subsection shows
that even an arbitrary optimization of the exact D6 over fixed
arrays cannot make this particular certificate reach the target.

### D. Actual-magnitude obstruction for every fixed offset array

Choose a dyadic N comparable to T^(4 beta). Since 1/8<beta<13/100,
we have Q=o(N), N=o(T), and the full block lies below T^(3/2).
Psi(sqrt(n/T))>=1/2 there for large T. All nonzero b_n are therefore
nonnegative. Elementary disk counting gives total full-block mass
comparable to N^(1/4). The accepted small-class absolute head bound
removes at most C Q^(1/4)=C T^(1/10)=o(N^(1/4)). Hence the ACTUAL
masked magnitudes satisfy

    M_N:=sum_n b_n comparable to N^(1/4).                (16)

No squarefree-density or individual representation-count asymptotic
is assumed. The lower bound uses the full annular r2 mass and the
already paid whole-class head bound.

Now define a CONTROL vector, not the actual waveform, by

    c'_(n,+)=(b_n/2)e(-T sqrt(n)),
    c'_(n,-)=conj(c'_(n,+)).                            (17)

It has exactly the same magnitudes as (5), the same mask, B, and D6
for EVERY offset array. Its physical real wave is

    F'(R)=sum_n b_n cos(2 pi(R-T)sqrt(n)).               (18)

For |R-T|<=cN^(-1/2), choose c small enough that every cosine is
at least1/2. The actual w(R/T) equals1 there for large T. Therefore

    M12(F')>=c M_N^12 N^(-1/2)>=cN^(5/2),
    sup_R|F'(R)|<=M_N<<N^(1/4)<<T^beta.                 (19)

The last inequality is a direct triangle bound for the control, not
a Li--Yang estimate for a block or an assertion about actual high
points. Real conjugacy has not been broken to manufacture the peak.

The uniform derivation of (12) applies to c' as well. Its right side
is IDENTICAL to the actual right side because (2) only uses |c_mu|.
Combining (12),(19) proves, uniformly in J and the fixed offsets,

    C_N(A)>=cN^(5/2)>=cT^(10 beta).                    (20)

This is an actual-magnitude positive-certificate obstruction, even
if the exact weighted cycle(13) could be evaluated optimally. It
does not lower-bound the actual M12(Z_N), I12 or an actual high set.
The artificial waveform(18) is not r2(n)n^(-3/4)Psi times the
prescribed original cosine phase. Its sole purpose is to expose the
phase information discarded when the signed average(9) is replaced
by its diagonal D6.

This uses the information-loss lesson of209 openly, rather than
repeating its weighted-Cauchy calculation as progress. The additional
statement proved here is that the same obstruction survives the full
sixth fixed-vector chain, every fixed offset array, the actual
large-class mask and the exact common-radius average, because that
average has the uniform dimension-free form(11).

### E. High-level checks and every block, level and tail

For comparison, an actual dyadic high shell with v<|f_j|<=2v has
S_1>=Jv^2 and S_6<=Lambda^5 S_1<=4Jv^2 Lambda^5. Combining with
(7) gives only Jv^2<=4^(1/5)B Lambda. The accepted unweighted local
row bound, applied to the doubled-frequency G, consequently returns
the existing distribution v^-2+T v^(-136/13). Both the diagonal
one-interval term and the full localization ceiling1+T/h remain.
This calculation is a control of the same chain, not a second claimed
mechanism. If instead one uses a global endpoint ceiling W, the
effective level is v(v/W)^(1/5)<=v and the result is weaker. No
endpoint-ceiling/operator closure is being credited as a new estimate.

The complete bound (15) has no level exclusions. Summing its twelfth
roots over the O(log T) masked ambient blocks, or using the fixed-p
power inequality, pays every unequal block at logarithmic cost.
The Schwartz factor makes the whole dyadic sum of the displayed
envelope O(T^(3+epsilon)), including N>T. The original tail above
T^(3/2) is uniformly O_A(T^-A), and its twelfth and mixed terms
are paid by the same power inequality. Partial top blocks, empty
masks and real endpoints only delete actual coefficients. Thus this
mechanism has the COMPLETE, but weak, restored upper price T^3.

Use the stronger accepted masked distribution and the actual ceiling
for Z_Q=B_T-L_Q to obtain the best supported complete bound. The
ceiling is T^(beta+epsilon), because the complete head is at most
Q^(1/4)<<T^beta. With W=T^(beta+epsilon), the actual high-tail layer
cake above V0 has both its integral terms and lower boundary:

    W^10+T W^(20/13)+V0^10+T V0^(20/13)
                                       <<T^(10 beta+epsilon). (21)

The entire low complement is bounded by
T+V0^10+T V0^(20/13)<<T^(29/25+epsilon). At the current target
level, the first inherited tail term exceeds29/25 by10 beta-29/25;
the second has exponent1+20 beta/13, also retained, not silently
deleted. The former dominates since beta(110/13)>1.

Consequently the complete comparison after (4) is unchanged:

    M12(B_T), M12(Z_Q), |I12|
                   <<_epsilon T^(10 beta+epsilon).     (22)

The implication for |I12| uses the paid repeated-class error, not
positivity of I12. The modulation obstruction does not assert that
the chain certificate attains its lower scale; its simple upper
price is T^3. Equation(22) is the accepted fallback, not a new result
of the chain. All low and high levels, unequal blocks and tails have
therefore been restored before declaring failure.

## 4. First doubtful or unproved step

The exact identities(6)--(9), signed average(11), complete bound(12)
and scoped obstruction(20) are the claims submitted for review.
There is no imported new source estimate in them.

The first missing input for the actual target is a bound that retains
the fixed endpoint phases at the actual absolute radii through the
decisive nonlinear estimate. Replacing their full common-radius
correlation by the phase-insensitive diagonal D6 cannot provide it:
the named complete certificate is already at least T^(10 beta) on
one actual-magnitude masked block, by(20). An improved estimate of
that same D6 cannot contradict this proven floor.

Allowing an offset pattern chosen separately from the high set at
each common translation does not repair the written proof: it
invalidates the fixed-H Fourier identity(9). Such an adaptive joint
correlation would need its own proved complete estimate, and none
is supplied here. Likewise the pointwise finite chain plus only
endpoint ceilings reduces to the old local bound in Section3.E.

This report therefore rejects this particular averaged sixth-chain
closure at29/25. It leaves the complete actual signed I12 inequality
open, rather than replacing it by a smaller proposed remainder or
continuing into another mechanism.

## 5. Required controls and outcomes

- **Actual coefficients and mask:** The original b_n uses actual
  r2, Psi, the full sf(n)>Q deletion and partial truncation. It is
  retained at both endpoints until the explicitly identified average.
  No smoothness is assigned to the arithmetic mask. The lower mass
  in(16) uses only the accepted class head and elementary annular mass.
- **Absolute radius anchor:** Formula(8) displays its exact endpoint
  factor. The auxiliary window stays at positive radii. The common
  translation is integrated exactly before the signed error estimate;
  only the resulting diagonal loses the endpoint phases.
- **All real signs:** The original c has its fixed e(-3s/8) rotation
  and conjugacy. The control(17) also has real conjugacy and the same
  magnitudes but is explicitly a different waveform. Neither plus
  signs nor sum frequencies are dropped as an alleged nonstationary
  complement.
- **Fixed vector versus operator:** The exact S_6 keeps c at both
  ends. Bound(14) is separately labeled its norm-only closure, and
  Section3.E recovers the known price instead of claiming a gain.
  The stronger floor(20) covers even exact evaluation of the
  phase-insensitive D6 for any permitted fixed array.
- **Singular and finite controls:** Zero coefficients or an empty
  mask give zero. Singular H requires no inverse. With J=1,
  H has rank one, H^6=d_N^5 H and D6=B d_N^5, so(15) is literal.
  Coincident offsets are allowed in(11); their degeneracy introduces
  no missing division or spacing assumption. PSD and the ordered
  frequency row sum in(10) prevent a hidden dimension factor.
- **Fixed versus data-selected offsets:** Uniformity over fixed
  arrays is not an estimate for H(R). The complete transfer(12)
  uses a fixed array throughout. No adaptive high-point selection
  is inserted into its common-radius integral.
- **Complete restoration:** Equations(4),(15),(21)--(22) pay the
  small head, every repeated-class term, all levels, unequal blocks,
  endpoints and infinite tails. Both inherited high-tail terms remain.
- **No unproved source import:** Only accepted204/216 inputs are
  reused; the Gram algebra, Fourier diagonalization and control are
  derived here. Zero experiments or new literature audits occurred.
- **Statement-only validation:** This is a NONBLIND discovery report.
  The separate isolated finite-chain task has not been read or assumed.
  Its eventual validation and the actual binding are separate gates.
- **Full goal:** Even a proof at29/25 would yield only102/325. The
  sufficient unbounded sequence of fixed even p with
  I_p(T,floor(T^(1/p)))<<T^(5/4+epsilon) remains unproved; it would
  yield1/4+7/[8(p+1)]. No p growing with T or complete M1/M2/GAR
  parent estimate is supplied.

All mathematical work here is analytical. A certificate obstruction
is not an actual moment lower bound or a refutation of the quarter goal.

## 6. Dependencies, exact artifacts and provenance

Only the generated brief and its exact permitted context were read.
The conductor independently highlighted the endpoint-ceiling closure
and requested the uniform PSD/spacing check in(10); both were derived
explicitly above. The common-radius average and its actual-magnitude
obstruction are this report's one mechanism. Prior209 information-loss
controls are disclosed dependencies, not presented as newly discovered.

| Artifact | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b |
| state/active_campaign.yml | 5ebf8c192da5f6cd10f15ce459b7968066dde913aedc155c1e72f5903057872d |
| strategy/round221_actual_vector_gram_and_correlations.md | a40cfd0421cb6c59c1c5121a7d1eef7f2f6ebcc9ef5ba3f904aebb7b369347a5 |
| strategy/gauss_circle_strategy_checkpoint_round220_2026-09-28.md | 6fc4b67a5de62a449527f62877933856635a9f6b0501a45f63539f05de6a5460 |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| proofs/kernels/gc_complete_distinct_radical_moment_reduction.md | d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee |
| proofs/kernels/gc_distinct_radical_absolute_certificate_obstruction.md | 603aa69cb4b757707d6eb89bb8290b05190b6b6d5cae83be52ddc19658ef68bb |
| rounds/codex-managed/gc-complete-signed-tenth-moment/reports/actual_tenth_high_values.md | 8fb9d01885057aa2981da9a746890968212a73103b7a079fcbc65e640d598df9 |
| rounds/codex-managed/gc-complete-signed-radical-kernel/synthesis.md | d34cf58dd298f4d50641c5135f24bec222106129d2d827929f16eafc6b49c814 |
| rounds/codex-managed/gc-full-goal-arithmetic-source-review/synthesis.md | 01939952d6f21510f1ed0b3ab069b2cc3b67d6c542d80ef31b22bc908db4a0b5 |
| rounds/codex-managed/gc-full-goal-arithmetic-source-review/reports/full_frontier_sources.md | 76343a1c8b33a9764b3498bf3fa8d919466d4476296ba4f9035ea6e3a6341ba0 |
| rounds/codex-managed/gc-actual-vector-gram-correlations/briefs/actual_anchored_gram_attack.md | fbcbb49dbfaae38097d1ba01419bc419b0ae8de817db3afc028cb426945ad9ce |

No current sibling report, isolated packet, external theorem, new round
or successor design was read. Only this assigned report was written;
the graph, draft, matrices, synthesis and historical files are untouched.
At least95 percent analytical effort; zero mathematical experiments.

## 7. Recommended state effect

**No change** to accepted estimates, exponents, original parent statuses
or the quarter goal. Retain, subject to independent review, the uniform
anchored-average lemma(11) and the narrowly scoped certificate
obstruction(20). Reject the averaged fixed-array sixth-chain closure
as a route to29/25 on its own; do not reject actual signed Gram
correlations which preserve information that this closure removes.

Exit label: `complete_actual_correlation_attempt_no_new_bound`.
The complete target remains I12<=T^(29/25+epsilon), with every actual
sign and class. This bounded role stops after this report and starts
no second mechanism or successor round.
