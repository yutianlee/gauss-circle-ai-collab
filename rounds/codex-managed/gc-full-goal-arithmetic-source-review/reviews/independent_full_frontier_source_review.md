# Round220 independent full-frontier source/application review

## 1. Result and exact-hash verdict

Campaign `gc-full-goal-arithmetic-source-review`, round220.
Reviewer: reused `joint_divisor_kernel` agent, NONBLIND source/application
seam; date2026-09-28. I authored this round's separate reciprocal-source
report. That authorship and earlier218--219 history are disclosed; this
review does not claim statement-only isolation.

**GREEN for the two specified source transfers, their complete cost
calculations, and the conclusion of no complete gain.** The frozen
claimant report is
`rounds/codex-managed/gc-full-goal-arithmetic-source-review/reports/full_frontier_sources.md`,
independently verified SHA256
`76343a1c8b33a9764b3498bf3fa8d919466d4476296ba4f9035ea6e3a6341ba0`.

The exact infinite Fourier-level union and the Schwartz approximation
are justified explicitly below. A source-loss issue identified during
review was repaired by the author before this final binding: the
pre-optimization Glidewell formulas now retain Q^eta, without replacing
it by T^eta for unrestricted auxiliary Q. I verified that local repair
at the hash above. All chosen minimizers have Q bounded by a fixed
power of T, so the correction changes no optimized power or conclusion.

The unchanged complete twelfth moment, the conditional102/325
milestone, the unbounded fixed-order family and every original parent
remain distinct. No target-sized signed estimate is validated here.

## 2. Exact statements and review scope

The actual coefficient is
a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)), with its real mollifier sign.
For N<n<=2N define S_N(R)=sum a_n(T)e(R sqrt(n)), R~T.
The global cosine wave is its real rotated dyadic assembly, including
the singleton, partial blocks and full Schwartz tail. No arbitrary
coefficient example is substituted for the actual wave.

I inspected exactly these primary theorem statements:

- [Guth--Maynard, 2405.20552v2, Theorem1.1](https://arxiv.org/html/2405.20552v2):
  for one coefficient vector |b_n|<=1 on L<=n<=2L, and 1-separated
  sample times in[0,S] with polynomial modulus at least W, the count
  is at most S^o(1) times
  L^2 W^-2+L^(18/5)W^-4+S L^(12/5)W^-4. The primary v2 record is
  dated7 April2026. The infinity norm, common vector and logarithmic
  frequencies are actual hypotheses.
- [Glidewell, 2605.27065v1, Theorem1.2](https://arxiv.org/html/2605.27065v1):
  a Schwartz function in the stated thickened R4 moment-curve tube,
  with cap projections bounded by1, satisfies an L^p box bound
  Q^(pb/2+eta)|Omega| on regular Q by Q by Q by Q^a boxes. Here
  1/3<=b<=1/2, 0<a<=b, and p=6+2(a+1)/b>=11. The primary v1
  record is dated26 May2026. At p=12, a=3b-1 and b>1/3.

The tube equations and cap widths in the claimant report agree with
the exact Glidewell statement. Only these two theorems are imported
in this review. The report's other literature items are expressly
scope screens, not theorem applications; no independent audit of
their theorem content is asserted here.

The review checks the full input map, norms, auxiliary losses,
physical trace, exponent restoration and retained frontier scope.
It does not re-prove either external theorem or the accepted project
large-values kernel. Those are identified dependencies, not new grants.

## 3. Independent derivation and application audit

### A. Square-root to logarithmic phase

With n0~N and
g(n)=sqrt(n)-sqrt(n0)-(sqrt(n0)/2)log(n/n0), direct differentiation
gives g(n0)=g'(n0)=0 and g''(n0)=1/(4n0^(3/2)). The report's identity

    e(R sqrt(n))=e(R[sqrt(n0)-(sqrt(n0)/2)log n0])
                  n^(i pi R sqrt(n0))e(R g(n))          (R1)

is exact, including the factor pi in the source time. On an interval
of length M<=cN, the controlling residual size is
T M^2 N^(-3/2). For derivatives of order r>=2 in the scaled n
coordinate the bound is this size times (M/N)^(r-2); the first
derivative has the same size by g'(n0)=0. Scaled R derivatives obey
the same bounds. Thus

    M~N^(3/4)T^(-1/2),   B~N/M=T^(1/2)N^(1/4)           (R2)

makes the entire residual a uniformly smooth function on a fixed
two-dimensional rectangle. When M is bounded, one uses singleton
pieces or bounded endpoint variants. The range M<1 provides no
useful multi-index map, as the report states.

Fixed smooth extension and Fourier expansion therefore give
e(Rg(n))=sum_(ell in Z^2)c_ell u_ell(R)v_ell(n), with |u|=|v|=1
on the working rectangle and uniformly rapid coefficient decay.
Here is a precise justification of the infinite large-value union.
Choose q_ell=(1+|ell_1|+|ell_2|)^2 and
C0=sum|c_ell|q_ell<infinity, uniformly. Then
sum q_ell^(-2) and sum q_ell^(-4) are finite. If

    |sum c_ell u_ell(R)D_ell(t_R)|>W,

some ell satisfies |D_ell(t_R)|>W q_ell/C0; otherwise the triangle
inequality contradicts the displayed event. Each D_ell uses one
fixed coefficient vector b_n v_ell(n), with unchanged infinity norm.
Apply Theorem1.1 separately and sum its W^-2 and W^-4 terms. The
two convergent q sums and fixed C0 powers give precisely a uniform
constant. Thresholds beyond the polynomial's possible size simply
give empty events. Thus the exact infinite expansion requires no
truncation error and no unjustified count of infinitely many factors.

The ambient source length is L~N: a vector supported on M consecutive
original indices still has frequencies log(n), not log(n-n0).
Translation of the time interval, of length S~T sqrt(N), is absorbed
as n^(it0) into each fixed vector. A maximal 1-separated subset of
each source level set covers that set by radius1 intervals, so its
measure is at most twice its cardinality. Returning to R multiplies
measure by O(N^(-1/2)); this uses covering, not persistence of values.

If |S_N|>V, one of its O(B) pieces exceeds cV/B. Since
|a_n|<<T^eta N^(-3/4), the normalized source threshold is
W~V N^(3/4)/B up to T^eta. The union and time change give

    meas{|S_N|>V}
      <<_epsilon T^epsilon min(T,
          B^3 V^-2+B^5 N^(1/10)V^-4
                          +T B^5 N^(-3/5)V^-4).        (R3)

All three exponents follow by multiplying the source count by
B N^(-1/2), with source S=T sqrt(N). Since N<=T^(3/2), the source
S^o(1) and coefficient losses can be absorbed in T^epsilon by first
choosing their input losses small enough.

At N~T^(2/3), B~T^(2/3), and the first certificate term is
T^2 V^-2. It is greater than T on 1<=V<=T^(beta+o(1)), since
beta<1/2 (indeed beta<13/100). The source threshold there is
W~V T^(-1/6). The capped certificate is therefore trivial on this
scale, exactly as claimed. This is not an actual distribution lower
bound. Falling back to the accepted complete estimate also pays the
smaller N range and every level where (R3) is worse.

### B. Exact R4 lift, cap normalization and Schwartz passage

Set t_n=sqrt(n/(3N)). Then t_n lies in[1/sqrt(3),sqrt(2/3)] and
has spacing comparable to1/N. For

    F(x)=sum_(N<n<=2N)a_n(T)e(x1 t_n+x2 t_n^2
                                           +x3 t_n^3+x4 t_n^4),

the physical identity S_N(R)=F(R sqrt(3N),0,0,0) is exact. Every
frequency (t,t^2,t^3,t^4) is in the source tube: its three defining
residuals are respectively zero, (1-3+2)t^3=0, and
(1+4-9+4)t^4=0. No regular-spacing corollary is used.

Writing C=Q^b, a first-coordinate cap has width1/C and contains
O(1+N/C) of these frequencies. Therefore

    ||F_gamma||_infinity
            <<T^eta N^(-3/4)(1+N/C).                   (R4)

This is an absolute amplitude bound, including each coefficient's
actual sign; no square-root cancellation inside a cap is granted.

For the source's Schwartz hypothesis, take a nonnegative smooth
Fourier bump phi_delta of integral1 and compact support shrinking
to zero, and set F_delta=F check(phi_delta). It is Schwartz and
converges uniformly to F on each fixed compact box. For fixed N,Q,
choose delta small enough that all translated supports remain in
the tube and have first-coordinate width much smaller than1/C.
The parameters t_n remain away from the tube's longitudinal ends.
Restriction of a translated bump to a sharp cap has Fourier L1
norm at most1, so cap projections of F_delta obey (R4), with only
the adjacent-cap occupancy constant. This remains true when t_n is
exactly a cap boundary. The source estimate is uniform in delta;
compact convergence passes it to F. There is no assertion that the
finite exponential polynomial itself is Schwartz.

At p=12, Q^a=C^3/Q, and the source-box volume is Q^2 C^3.
After the twelfth power of (R4), its box bound is

    integral_Omega |F|^12
       <<_(eta,a,b) T^eta Q^eta
                     N^-9(1+N/C)^12 Q^2 C^9.          (R5)

I have kept Q^eta explicitly, as the corrected report now does in
B2, B3 and B4. It may be absorbed into T^epsilon on Q<=T^C for any
fixed C after shrinking eta, but not uniformly for unrestricted Q.
The corrected Q>N^3 comparison explicitly retains Q^eta, and the
later optimizing choices are explicitly polynomially bounded in T.

### C. All three trace variables and optimization

The transverse frequencies (t_n^2,t_n^3,t_n^4) lie in a fixed compact
set. Choose a fixed Schwartz kernel kappa on R3 whose Fourier
transform is1 on that set. The exact reproducing identity and Holder
give

    |F(x1,0,0,0)|^12
       <=||kappa||_1^11 integral_R3 |kappa(-y)|
                                             |F(x1,y)|^12 dy. (R6)

This pays all of x2,x3,x4. Partition y into regular boxes of sides
Q,Q,Q^a. All three sides are at least1; rapid decay implies that
the sum over these boxes of sup|kappa| is bounded independently of
Q,a. Apply (R5) on each translated source box. The physical x1
interval has length S~T sqrt(N), so it needs O(max(1,S/Q)) source
intervals. Finally dR=dx1/sqrt(3N). The resulting certificate is

    T^eta Q^eta N^(-19/2)(1+N/C)^12
                                  Q^2 C^9 max(1,S/Q).  (R7)

In particular one cannot divide away the transverse source volume
or trace through just one added variable. Regular boxes in the source
are explicitly aligned with these axes, as required by the application.

To check the critical optimization, suppress only the harmless losses
and fixed constants in the explicit envelope. For C<=N it is

    N^(5/2)Q^2 C^-3 max(1,S/Q),                         (R8)

decreasing in C. For C>=N it is comparable to
N^(-19/2)Q^2 C^9 max(1,S/Q), increasing in C. Thus the optimal cap
count for a fixed Q is as near N as permitted by
Q^(1/3)<C<=Q^(1/2).

At N=T^(2/3), S~N^2. For Q<=N^2 the envelope is at least
N^(5/2)S Q^(-1/2), minimized at Q~N^2. For N^2<=Q<=N^3 it is
at least N^(-1/2)Q^2, likewise minimized at Q~N^2. For Q>N^3,
the condition C>Q^(1/3)>N gives at least N^(-19/2)Q^5, which is
already larger. Keeping the source factor Q^eta on this last range
does not decrease it. The fixed admissible parameters

    Q=N^2,  a=b=1/2,  C=N

give exactly the claimed envelope N^(7/2)=T^(7/3), up to epsilon
losses. Here Q is a fixed power of T, so (R5)--(R7) reduce to the
report's T^epsilon notation. All uses of “at least” in this paragraph
refer only to the calculated source certificate, not the actual moment.

The more general optimization stated in the report also checks out.
If S>=N^2, Q=N^2,C=N gives N^(3/2)S=T N^2. If S<=N^2,
Q=S,C=sqrt(S) gives N^(5/2)sqrt(S)=T^(1/2)N^(11/4).
These choices always have a=b=1/2 and Q bounded by a fixed power of
T. The elementary monotonicities above exclude cheaper values within
this same whole-block envelope. This is not a claim to optimize a
different arithmetic localization or a different trace estimate.

### D. Complete reconstruction and full-frontier scope

The actual coefficient's Schwartz tail past n=T^(3/2) is uniformly
O_A(T^-A): combine a polynomial divisor bound with arbitrarily high
Schwartz decay and sum the resulting convergent tail. The singleton,
partial intervals and O(log T) dyadic blocks are retained. The fixed-p
power inequality pays every mixed-block term with logarithmic loss.
Since both new certificates fail to improve the needed complete
estimate, the accepted distribution and ceiling remain the fallback:

    D_B(V)<<T^epsilon(V^-2+T V^(-136/13)),
    sup|B_T|<<T^(beta+epsilon).

The full twelfth high-tail price, including its lower layer-cake
boundary, is
W^10+T W^(20/13)+V0^10+T V0^(20/13), with
W=T^(beta+epsilon), V0=T^(13/125). It remains bounded by
T^(10 beta+epsilon); adding the low portion preserves the stated
complete bound T^(1+epsilon)+T^(10 beta+epsilon).

The frontier table retains both HARD and SMOOTH M1, TOP/BAL/UNBAL
M2, total-M1 GAR, the complete anchored energy and unbounded fixed
orders. It does not transfer a source average into a pointwise
physical parent or silently replace the actual joint symbol by r2.
The authorized conductor correction fixes the UNBAL row to
K=XL/D^2 and phase e(sqrt(X h k)); both agree with the authoritative
normalization recorded there. The checkpoint217 table errors are not
new mathematical states, and the closed checkpoint remains unchanged.

For the moment route, the one-sided family
I_p(T,floor(T^(1/p)))<=C_(p,epsilon)T^(5/4+epsilon) for an unbounded
sequence of fixed even p remains a sufficient, unproved premise.
Same-order absorption and the head cost T Q_p^(p/4) then lead to

    (5/4+1+p/2)/(2(p+1))=1/4+7/[8(p+1)].                (R9)

The current p=12 input29/25 instead gives102/325. Neither source
supplies (R9)'s premise, and a bounded range of source exponents
cannot be substituted for an unbounded fixed-order family. This
review validates the distinction, not the unknown integrals or any
direct M1/M2 parent.

## 4. First unproved step and repair status

No substantive gap was found in the two written transfers. Audit A
does not close a target-sized distribution after the B-piece union,
ambient index scale and radial measure cost. Audit B does not close
the target after the cap occupancy and all transverse traces. The
first missing target step is still a complete signed arithmetic bound
for the actual physical aggregate. A smaller component or a source
theorem with a matching exponent is not that bound.

The one source-loss issue was the missing explicit Q^eta in the
original unoptimized B2/B3/B4. The author repaired all three displays,
the Q>N^3 comparison and the explanation of loss absorption. I checked
that repair locally and bind this review to the corrected final hash.
No remaining repair is required for the stated application conclusions.
The reported optimizers and restored exponents are unchanged. No
claimant file was edited by this reviewer.

The proposed next objective is only a recommendation. A future direct
high-value/Gram argument would still need its entire actual coefficient
and signed-energy estimate. This review grants no new round or proof
premise for that mechanism.

## 5. Required controls and outcomes

- Exact source versions, theorem numbers, coefficient infinity norm,
  one fixed source vector, separated times and source interval: GREEN.
- Exact Taylor identity, all scaled derivatives, ambient length N,
  infinite Fourier union with summable thresholds, B-piece threshold
  and radial measure Jacobian: GREEN.
- Exact R4 moment-curve frequencies and tube membership, cap occupancy,
  boundary caps and rigorous Schwartz approximation: GREEN.
- Three-variable reproducing trace, translated regular boxes,
  transverse weight sum, physical covering and radial Jacobian: GREEN.
- Critical envelope optimization N^(7/2)=T^(7/3), with correct
  auxiliary Q loss as qualified above: GREEN.
- Complete tails, all mixed blocks, accepted fallback, unchanged
  10 beta, conditional102/325 and sufficient unbounded-order family:
  GREEN for the stated scope; the new signed targets remain OPEN.
- Actual versus enlarged scope: GREEN. Upper-certificate prices are
  not actual moment lower bounds; arbitrary sign models are not
  counterexamples to actual high points.
- Full-frontier retention and both corrected UNBAL formulas: GREEN.
  No M1/M2/GAR estimate has been independently established by these
  two source transfers.

The calculations are analytical. Zero experiments, numerical fits,
state edits or successor-round work were performed. This is a
NONBLIND independent application review, not the separate isolated
statement-only gate.

## 6. Dependencies and exact provenance

Newly read local artifacts for this seam:

| Artifact | SHA256 |
|---|---|
| rounds/codex-managed/gc-full-goal-arithmetic-source-review/reports/full_frontier_sources.md | 76343a1c8b33a9764b3498bf3fa8d919466d4476296ba4f9035ea6e3a6341ba0 |
| rounds/codex-managed/gc-full-goal-arithmetic-source-review/controls/conductor_frontier_normalization_correction.md | 849601b500059325accaba60a559a3e941bf427b11e8cab0bea008ef46a210d8 |

Primary sources inspected are exactly Guth--Maynard2405.20552v2
Theorem1.1 and Glidewell2605.27065v1 Theorem1.2, linked in Section2,
with their corresponding primary version records. No additional
theorem, current sibling review, isolated packet or source-screen
paper was imported.

Previously authorized context supplied the protocol, unchanged graph
SHA256 a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b,
accepted moment/distinct-class kernels, checkpoint217 and closed219
restoration. I authored `reports/reciprocal_energy_sources.md`, whose
corrected frozen hash is
9fbde8516f7b8524a3af2f0ae2605b63cb993deab537dff3ae9c700e1b6c82fd;
that is disclosed authorship, not evidence validating this claimant.
The first inspected claimant hash was
336bf8799adee932bda4c526b594054eee36e9f13892c7f650934ba02e5df2c5.
The conductor was notified of the Q-loss issue; the author's correction
was then independently inspected and verified at the final hash above.

Only this assigned review file was written by this reviewer. The
claimant correction was made by its author. This reviewer did not
edit the graph, draft, validation matrices, synthesis or any legacy
or successor artifact.

## 7. Recommended state effect

Close this corrected exact-hash source/application seam **GREEN**.
The auxiliary-loss repair has been verified in Sections3--4. Retain the
two complete failed-transfer calculations as method evidence. Keep
the complete signed moment target, every direct parent and the full
quarter objective open; make no exponent or graph promotion.

This review stops here. It does not start the recommended mechanism,
read another current report or design a successor round.
