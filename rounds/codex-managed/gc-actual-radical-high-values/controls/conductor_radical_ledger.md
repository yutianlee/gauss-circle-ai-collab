# Round216 conductor ledger: actual cutoff and surviving near relations

## 1. Result

Campaign:gc-actual-radical-high-values. Date:2026-09-28.
Role:conductor analytical control, NONBLIND. Graph SHA256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.

The actual small-squarefree-class head has complete twelfth moment
O(T^(15/13+epsilon)), below29/25 by2/325. Therefore the frozen high-value
gate is equivalent, at its target power, to the whole twelfth moment
of the remaining large-class tail. Its entire exact-resonance part is
O(T^(-1/5)log(2T)^18). Neither estimate controls nonzero correlations.

There are actual nonzero near relations with exactly three active large
squarefree classes after the cutoff. An elementary rational-spacing
argument verifies that the old quadratic near-relation family survives
the new restriction for all butO(Q) choices of its radius parameter.
This is a frequency-separation control, not a lower bound on the moment.
The positive termwise twelfth-frequency certificate also retains its
inadequate T^(5/2) lower scale. All results require final-hash review.

## 2. Exact quantities and hypotheses

Use the frozen actual mollifier, weight and full series of strategy216:
rho>=0 real radial smooth of mass1, supported in the unit disk;
Psi(s)=rho-hat(s e1), with e(t)=exp(2pi i t); w>=0 smooth supported
in[1/2,2] and equal1 on[1/sqrt(2),sqrt(3)]. Thus Psi is real even
Schwartz, |Psi|<=1 andPsi(0)=1. Let

    a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)),
    B_T(R)=sum_n a_n(T)cos(2pi R sqrt(n)-3pi/4),
    Q=floor(T^(2/5)), V0=T^(13/125),
    L_Q=sum_(sf(n)<=Q) a_n(T)cos(...), Z_Q=B_T-L_Q.

Here sf(n) is the unique squarefree partd in n=d s^2, s>=1.
T>=2 is real. All series converge absolutely for eachT. Define
M_p(F)=integral_R w(R/T)|F(R)|^p dR and
H_p(F;v)=integral_(|F|>v) w(R/T)|F|^p dR.
Constants may depend on the fixed functions and indicatedepsilon.

## 3. Proofs and complete power accounting

### A. Actual arithmetic head bound, including every square factor

The accepted divisor identity gives the prime-factor formula forr2.
For squarefreed, the exact inequality

    r2(d s^2)<=r2(d)tau(s^2)                              (1)

holds. Ifd contains a prime3 modulo4, both sides are zero. At a prime
1 modulo4 already dividingd, the factor2e+2 is at most2(2e+1);
at every other such prime it is2e+1. Powers of2 do not increase the
r2 factor. These local comparisons prove(1), includingd=1.
Since tau(s^2)<=tau_3(s), the absolutely convergent divisor series gives

    A_d(T):=sum_s |a_(d s^2)(T)|
             <=C r2(d)d^(-3/4), C=zeta(3/2)^3.             (2)

The elementary unit-square comparison for a disk gives
sum_(n<=x)r2(n)<=Cx forx>=1. Partial summation consequently gives
sum_(d<=Q)r2(d)d^(-3/4)<=CQ^(1/4), even without restrictingd
to squarefree. Therefore

    sup_(R inR)|L_Q(R)|<=C Q^(1/4)<=C T^(1/10).            (3)

This is an actual arithmetic bound with all s retained. It is uniform
on the full real line and does not use an independence model.

### B. Masked finite duality and the complete head moment

For either fixed mask sf(n)<=Q or sf(n)>Q, the finite coefficient
argument in accepted204 Sections3--5 applies with zero coefficients
at inactive indices. To make this use explicit, truncate only beyond
T^(3/2), where the Schwartz/divisor L1 remainder isO_A(T^-A),
uniformly in either mask. Keep the singleton and every partial dyadic
block. On each ambient lengthN, the coefficient energy is at most
T^eta N^(-1/2); the unweighted correlation kernel is unchanged.
The finite Gram proof, including its diagonal and the full1+T/h
cover, therefore gives the same two terms for every positive level.
A union overO(logT) blocks, with thresholdV/(C logT), then yields

    integral w(R/T)1_(|F|>V)dR
          <<_epsilon T^epsilon(V^-2+T V^(-136/13)), V>=1, (4)

forF=L_Q andZ_Q. Every fixed power of the inputeta and every logarithm
is absorbed by choosing the input loss according toepsilon. This is
a reproduced finite coefficient argument; the accepted final statement
for lower cutoffsU is not silently quoted as a squarefree-mask theorem.

Layer cake, measureO(T) below1, and the ceiling(3) give

    M12(L_Q)<<T^epsilon[T+Q^(5/2)+T Q^(5/13)]
                <<T^(15/13+epsilon).                     (5)

Indeed12-136/13=20/13, so the second distribution term integrates to
T times the ceiling to power20/13. The first term gives ceiling^10.
The target margin is29/25-15/13=2/325. The floor inQ costs constants;
boundedT is covered by the fixed Schwartz L1 bounds.

For later lower moments, |Z_Q|<=|B_T|+|L_Q|<=T^(beta+epsilon),
where beta=2theta_LY-1/2>1/8 and the actual accepted Li--Yang application
is used only forB_T. Combining this with(4) reproduces
M_r(Z_Q)<<T^epsilon[T+T^((r-2)beta)] for fixedr>=2; r=0,1
costO(T^(1+epsilon)) by measure and Cauchy--Schwarz.

### C. Whole-tail equivalence and high-event transfer

The accepted distribution forB_T pays its low values:

    integral_(|B_T|<=V0)w(R/T)|B_T|^12dR
       <<T^epsilon[T+V0^10+T V0^(20/13)]
       <<T^(29/25+epsilon).                              (6)

HereV0^10=T^(26/25) andT V0^(20/13)=T^(29/25).
The same proof using(4) pays the low values ofZ_Q at any fixed
multiple ofV0. Since(3)/V0<=C T^(-1/250), it is eventually at
most1/2. Thus |B_T|>V0 implies |Z_Q|>|B_T|/2>V0/2, and

    H12(B_T;V0)<=2^12 H12(Z_Q;V0/2).                      (7)

There is no uncontrolled mixed-term expansion in(7). Conversely,
M12(B_T)<=2^11[M12(L_Q)+M12(Z_Q)] and the same inequality with
B_T andZ_Q exchanged holds. By(5)--(6), the following are equivalent
at the target order, for everyepsilon>0 with corresponding constants:

    H216;  M12(B_T)<<T^(29/25+epsilon);
             M12(Z_Q)<<T^(29/25+epsilon).                 (8)

Neither equivalence proves its unestimated premise. It avoids treating
the tail's whole moment as an unpriced stronger target. All real
endpoints, smoothing tails and cosine signs are covered by the norms.

### D. Exact radical coefficient and the remaining signed kernel

For each squarefree classd>Q, (2) andr2(d)<=4tau(d) imply

    S_Q=sum_(d>Q)A_d(T)^2<<Q^(-1/2)log(2Q)^3.             (9)

An elementary proof of the tail bound uses tau(n)^2<=tau_4(n) and
sum_(n<=x)tau_4(n)<=Cx log(2x)^3, obtained by summing three harmonic
factors and counting the fourth divisor. Dyadic summation proves(9).
The accepted exact-resonance kernel, with all twelve signs and ordered
indices, gives absolute exact coefficientO(S_Q^6). Its complete
weighted window contribution is consequently

    0<=D12(T,Q)<<T Q^-3 log(2Q)^18
                      <<T^(-1/5)log(2T)^18.              (10)

With w-hat(xi)=integral w(u)e(-u xi)du, the full remaining term is

    R12=T 2^-12 sum_(epsilon in{+1,-1}^12)
          sum_(sf(n_j)>Q, Delta!=0)
          [product_j a_(n_j)(T)] e(-3 sum_j epsilon_j/8)
                                     w-hat(-T Delta),
    Delta=sum_j epsilon_j sqrt(n_j),
    M12(Z_Q)=D12+R12.                                    (11)

Absolute convergence for fixedT justifies the expansion and regrouping.
The sumR12 is real, not termwise positive. Exact radical independence
does not bound it. A high-value indicator would change the Fourier
kernel in(11); equation(8), rather than an illicit unchanged kernel,
justifies working with the whole-tail moment.

### E. An elementary count for actual surviving near relations

Fixa>0 andM>=sqrt(a). For every integerd>=1, solutions
m in[M,2M] to m^2+a=d s^2, s positive integer, give distinct ratios
m/s. Equality of two ratios, together with s^2(d-(m/s)^2)=a>0,
would force the same solution. The ratios lie in an interval of length
at mosta sqrt(d)/(2M^2), because
m/s=sqrt(d)(1+a/m^2)^(-1/2). Also s<=3M/sqrt(d). Any two ratios
therefore differ by at least1/(s_1s_2)>=d/(9M^2). It follows that
there are at most1+9a/(2sqrt(d))=O_a(1) solutions for eachd.
In particular,

    #{m in[M,2M]:sf(m^2+a)<=Q}<=C_a Q.                   (12)

Choose a fixed sufficiently largeC0 so thatPsi is positive and bounded
below on all arguments sqrt((m^2+a)/(C0 M^2)) for m in[M,2M] and
a=1,25,49, onceM is large. LetT=C0 M^2 andQ=floor(T^(2/5)).
By(12), all butO(Q)=o(M) integersm retain all three actual norm
indicesm^2+1,m^2+25,m^2+49 inZ_Q. Each is a sum of two integer
squares and has positiver2. Their squarefree parts are distinct for
largeM: if two shared d>Q, their difference24 or48 would equal
d(s_2^2-s_1^2)>=2M sqrt(d), which tends toinfinity.

Strict concavity and a fixed Taylor expansion give

    Delta_m=sqrt(m^2+1)+sqrt(m^2+49)-2sqrt(m^2+25)
              =-144m^-3+O(m^-5)<0,
    T Delta_m=O(M^-1)->0.                               (13)

Four identical cancelling plus/minus pairs pad this to twelve terms
with six plus and six minus signs. All twelve actual coefficients
belong toZ_Q, and the aggregate has precisely three active squarefree
classes. This disproves a proposed absence of nonzero near relations
after the cutoff. It supplies no large lower bound for the full signed
moment: other summands may cancel, and this sparse family's own mass
does not exhaust the target.

### F. Scope of the positive twelve-frequency certificate

For sufficiently small fixedc>0 choose a blockcT<=n<=2cT where
Psi(sqrt(n/T))>=1/2. Elementary lattice counting gives total positive
coefficient mass comparable toT^(1/4). The part withsf(n)<=Q has
mass at mostC Q^(1/4)=O(T^(1/10)) by(2)--(3). Thus the retained
large-class coefficients still have mass at leastc_1T^(1/4).

Use only balanced six-plus/six-minus terms of the termwise absolute
version of(11), initially allowingDelta=0. The six-root sums have
total product mass at leastc_2T^(3/2) and occupy an interval of
lengthO(sqrt(T)). Bins of widthc_3/T numberO(T^(3/2)). Their squared
mass is at leastc_4T^(3/2). Since w-hat(0)>0, each same-bin pair
hasT|w-hat(-T Delta)|>=c_5T. Hence this positive certificate is
at leastc_6T^(5/2). Removing every exact term costs only(10), so
the same lower order holds for its nonzero part. This is not a lower
bound onR12, M12(Z_Q) orH216. It excludes only a termwise absolute
closure of the actual remaining kernel.

## 4. First doubtful or unproved step

An adequate bound on the complete signed nonzero expression(11) remains
unproved. The actual near-relation control shows that squarefree
separation alone cannot make all its frequencies nonstationary. The
positive certificate lower bound concerns one losing estimate only.
The discovery task's proposed collective distinct-class reduction is
a separate candidate under independent rederivation; it is not used
to prove any statement in this ledger.

## 5. Controls and outcomes

- Actual prime factors, d=1, all s and the full mollifier: retained.
- Masked distribution: finite coefficient proof and full ceiling
  reproduced; no enlargement of an accepted statement by citation.
- Head moment and low levels:15/13 and29/25 separately checked.
- High-event thresholds:V0/2 and factor2^12 are explicit.
- Exact versus nonzero frequencies: all signs and the Fourier kernel
  retained, with no finite-window independence assertion.
- Actual near family: ratio spacing proves the radical cutoff survives;
  three active classes and balanced padding checked analytically.
- Positive-certificate scope: only the named absolute expansion fails.
- No numerical experiment or new external source; all work analytical.

## 6. Dependencies and exact artifacts

Read protocol.md, state/proof_obligations.yml, active216 manifest and
strategy/round216_actual_radical_high_values.md. Accepted dependencies:
proofs/kernels/gc_complete_square_root_large_values_moment_bound.md
(finite proof and qualified pointwise reconstruction), and
proofs/kernels/gc_weighted_square_root_exact_resonance_mass.md
(all-sign exact coefficient). Closed209 actual_tenth_high_values.md,
closed205 conductor_arithmetic_source_gate.md and closed215 synthesis
provide barriers only. No new primary theorem is imported. The actual
head and near-family proofs above were derived by the conductor before
being sent as labeled nonblind suggestions to the discovery task.

## 7. Recommended state effect

Retain these proved bounds and controls after independent review.
Do not promoteH216, a new exponent or the quarter theorem. The complete
large-class twelfth moment is an equivalent paid target, not a solution.
Any proposed collective-class kernel promotion requires its own exact
derivation, independent review and valid State Patch. All full-goal
parents and endpoints retain their existing status.
