## 1. Result and verdict

**GREEN** on the assigned mathematical seams of the frozen
`reports/blind_moment_family.md`, SHA256
`fe681f61a48faac2825138c8b7e0884e4f73c05b6cca789cb0f72b9f33e49e35`.

Campaign `gc-full-goal-distinct-source-review`; round217; reviewer
`full_frontier_sources`; generated2026-09-28. This review is NONBLIND:
the isolated packet and completed claimant report were both read. It
does not claim to reproduce the claimant's original statement-only status.
All work is algebraic/analytical; zero experiments.

The optimized nonabsorbing certificate, its unique discrete p=16 minimum,
and the stronger same-order absorption are correct. In particular, the
nonabsorbing order limit is not a general impossibility result. A grant
at a single order/cutoff pair already bounds that order's tail moment;
lower-order grants are unnecessary once absorption is used.

This strengthens the interpretation of my earlier full-frontier report:
its all-orders induction was sufficient, but its family
`Q_p=floor(T^(1/p)), I_p<=T^(5/4+epsilon)` need only hold along an
unbounded fixed-even subsequence to imply quarter. No intermediate-order
availability is intrinsically required. The frozen original report is
not edited; the precise scope correction is recorded in sections3 and7.

## 2. Exact packet, hashes and quantifiers

The packet has q=136/13, `1/8<beta<13/100`, `beta(q-2)>1`, real T>=2,
fixed `0<=alpha<=4beta`, and Q=floor(T^alpha). It gives the complete
distribution and ceilings for the real functions B=L+Z, fixed
nonnegative compactly supported weight w, and absolute convergence of
`Z=sum_(d>Q)f_d`. For every fixed h>=2 and epsilon>0,

    sum_(d>Q) A_d^h <<_(h,epsilon) Q^(1-3h/4+epsilon).

No arithmetic origin is assumed. The additional diagnostic statement is
the ONE-SIDED grant `I_p<=C_(p,epsilon)T^(1+epsilon)` at a tested pair
(p,alpha), p fixed and even. It is not supplied by the packet.

The exact isolated packet read is
`briefs/blind_moment_family_statement.md`, SHA256
`89ec2e5ef9a814da0fa1e1cd7efcdc941bdeca673e4688228b084b9fab8717c5`.
The claimant bytes match the hash in section1. Implicit constants may
depend on the fixed pair and are never assumed uniform in p or alpha.
Every order limit means selecting a fixed pair before T tends to infinity.

## 3. Independent derivation of the decisive seams

**Identity and signed direction.** The generating polynomial
`product_d(1+t f_d)` has coefficient E_p/p!. Expanding its formal
logarithm gives the claimant's exact grouped partition coefficient
`p! product_h (-1)^((h-1)m_h)/(m_h! h^m_h)`, where sum h m_h=p.
The singleton term is Z^p. In every other term put r=m_1, n=p-r>=2
and k=sum_(h>=2)m_h<=floor(n/2). Its structure is
`Z^r product_(h>=2)S_h^m_h`, with S_h=sum f_d^h.

At fixed T, sum A_d<infinity uniformly dominates every finite partial
expansion by a fixed power of sum A_d. The compact weighted measure is
finite. Thus the finite identity, its infinite limit and its integrated
version all exist before any estimate is made. Since p is even and the
functions are real, integration gives

    M_p(Z) <= I_p + sum_(nontrivial profiles)
                 |coefficient| product ||S_h||_infty^m_h M_r(Z).

The term is I_p, not |I_p|. No assertion that E_p is nonnegative enters.

**Inherited moments and all partition powers.** Layer cake below level1
costs O(T). Above it, the two distribution terms yield integrals of
V^(r-3) and T V^(r-q-1), retaining logarithms at r=2,q. The Z ceiling
is T^(beta+delta), and `beta(q-2)>1` compares the growing high-level
terms in favor of exponent beta(r-2). After allocating arbitrary small
losses, `M_r(Z)<<T^(m(r)+epsilon)`, m(r)=max(1,beta(r-2)), including
r=0 via the measure and r=1 via layer cake or Holder.

The head exponent is exactly

    H_p(alpha)=max(1, alpha(p-2)/4, 1+alpha(p-q)/4).

For a correction with n nonsingleton labels, the coefficient norm costs
`Q^(k-3n/4+epsilon)`. Maximizing k gives the penalty n alpha/4 for even
n and (n+2)alpha/4 for odd n. Both are at least alpha/2, while
m(p-n)<=m(p-2). Therefore the one-pair profile n=2 attains the maximum

    C_p(alpha)=max(1,beta(p-4))-alpha/2.

This comparison includes profiles with no singleton and with odd-size
blocks; none is omitted. It proves the restricted nonabsorbing expression
max(H_p,C_p) after the diagnostic grant, but does not establish optimality
among different ways of using the same assumptions.

**Cutoff minimization.** Write a=alpha/4 and c=1/(q-2)=13/110.
For even p>=12, H increases from `1+a(p-q)` on [0,c] to `a(p-2)` on
[c,beta], while C=beta(p-4)-2a decreases. Their crossing is feasible
and equals

    a_*=[beta(p-4)-1]/(p-q+2), if p<=p_c,
    a_*=beta(p-4)/p,          if p>=p_c,
    p_c=4beta/(beta-c).

Indeed the first crossing is below c precisely when
beta(p-4)<=cp, and the second is below beta. The given beta interval
implies `44<p_c<220/3`. Substitution reproduces both branches of the
claimant's E(p); they coincide at p_c. For even4<=p<=10 the choice
alpha=0 gives E=1, which cannot be lowered because of the head's O(T)
term. At large p, E=beta(p-6+8/p), so the restricted restored limit is
1/4+beta/2.

**Discrete minimum.** In the first branch, set k=q-2, C=14beta-1,
D=4[1-beta(q-6)]. Algebra gives

    4Theta(p)=1+2beta-C/(p+1)+D/[(p-k)(p+1)].

The derivative sign is that of
`C-D(2p+1-k)/(p-k)^2`. The fraction decreases strictly for p>k;
its derivative is `-2(p+1)/(p-k)^3`. At p=14 the sign is negative
throughout the stated beta interval; at p=18 it is positive. The second
branch has derivative sign
`C-16beta(2p+1)/p^2`, positive for p>=12: even its lower-beta value at
p=12 is positive, and the subtracted fraction decreases with p.

The low branch is decreasing and Theta(10)>Theta(12), so only14,16,18
remain. Their exact values are the claimant's. On clearing positive
denominators,

    Theta(14)-Theta(16) has numerator 5573-41690beta >0,
    Theta(18)-Theta(16) has numerator -7523+62542beta >0.

The first is positive even at beta=13/100; the second is positive even
at beta=1/8. Hence p=16 is the unique minimizing fixed even order for
this restricted procedure, with `(227+216beta)/833`. This is not a
minimum over all deductions from the packet.

**Same-order Young absorption.** Fix p and choose eta with0<eta<1/4.
For every2<=h<=p, apply the power-sum input with loss2eta. Since Q>=1,

    ||S_h||_infty << Q^(1-3h/4+2eta)
                    <= Q^(-h/4+h eta)=R_Q^h,
    R_Q=Q^(-1/4+eta).

The exponent comparison is
`1-h/2+(2-h)eta=(2-h)(1/2+eta)<=0`. Thus each correction is bounded
pointwise by `K R_Q^n |Z|^(p-n)`. There are finitely many fixed-p
coefficients K. For r=p-n>0, put y=|Z|/R_Q and use
`y^r<=delta y^p+C_(p,r,delta)`. Choose the finitely many deltas only
after fixing all K, so the sum of coefficients of |Z|^p is at most1/2.
Terms with r=0 already cost O(R_Q^p). Therefore

    |Z^p-E_p| <= (1/2)|Z|^p+C R_Q^p,
    I_p >= (1/2)M_p(Z)-C T R_Q^p,
    M_p(Z) <= 2I_p+O(T Q^(-p/4+p eta)).                       (R1)

All constants depend only on fixed data/pair/order. The moment is finite
by the original absolute convergence or ceiling, so no circular
integrability argument occurs. A negative I_p is permitted and is kept
with its sign; (R1) itself bounds how negative it can be. Nonnegative w
is essential in this step and is present.

Under the diagnostic grant, Q^(-p/4+p eta)<=1 gives M_p(Z)<<T^(1+epsilon)
at that tested order. Adding the full head yields M_p(B)<<T^(H_p(alpha)
+epsilon). No lower-order grant has been used.

**Order/cutoff availability.** At alpha=0, Q=1 and H_p=1, so a single
order's grant gives that order's complete T^(1+epsilon) moment. For any
unbounded sequence of fixed even p with those grants at alpha=0, the
restored exponents tend to1/4. It is unnecessary to have grants at every
smaller even order.

More generally, grants at pairs(p_j,alpha_j), p_j unbounded and
alpha_j->0, suffice if all decompositions concern the same B. Since
`H_p(alpha)<=1+alpha(p-2)/4`, the pointwise loss is at most
`3/[4(p+1)]+alpha/8`. For any desired final loss, one selects a single
appropriate pair and then lets T grow. Uniform constants as p grows
or alpha decreases are not needed. Grants restricted to a fixed
positive alpha leave a head-certificate limit1/4+alpha/8; the claimant's
abstract head example demonstrates why this cannot simply be erased.

**Effect on my earlier family.** My frozen report stated the sufficient
family Q_p=floor(T^(1/p)), I_p<=T^(5/4+epsilon), and proved its consequence
by induction through every even order. Apply (R1) instead with alpha=1/p,
which is in the packet's admissible range for p>=4. The error is

    T Q_p^(-p/4+p eta) <<_p T^(3/4+eta).

Thus at EACH independently granted p, M_p(Z_Qp)<<T^(5/4+epsilon).
The actual elementary head bound alone gives
`M_p(L_Qp)<<T Q_p^(p/4)<=T^(5/4)`, so M_p(B)<<T^(5/4+epsilon).
Restoration is `1/4+7/[8(p+1)]`. An unbounded fixed-even subsequence
of those grants therefore suffices; intermediate orders are unnecessary.

The earlier statement that a subsequence does not justify *that particular
induction* is literally correct. Any broader interpretation that the
arithmetic criterion itself requires every intervening order must be
revised. The same-order argument gives a strictly weaker sufficient
availability premise without proving any new arithmetic grant.

## 4. First open input and limits of this verdict

The first unproved analytic premise remains the signed-integral grant
at the selected pair. Neither the identity nor absorption produces it.
No conclusion about the actual circle discrepancy follows from the
abstract packet without an owner-preserving arithmetic identification
and the complete restoration already required in the project.

The restricted p=16 statement must always retain the word restricted.
Its limiting exponent is not an obstruction to the stronger absorption
argument, to smaller-cutoff availability, or to a new arithmetic method.
The full-goal criterion needs grants on one common target B and on the
stated unbounded fixed-order pairs, not a finite collection of favorable
orders or a sequence of different unrelated B's.

No correction to the frozen claimant is needed on the assigned seams.
This review does not certify source statements outside the packet, graph
acceptance, any new quarter estimate, or the current conductor's separate
candidate controls, which were not read.

## 5. Required controls and outcomes

| Control | Result |
|---|---|
| Every partition, including r=0 and odd blocks | GREEN: n>=2,k<=floor(n/2) establishes both inherited domination and absorption. |
| One-sided I_p and nonpositive E_p | GREEN: transfer retains I_p, and E_p may be negative by O(R_Q^p). |
| Same-order circularity | GREEN: integrability precedes absorption; no lower moments or grants are inserted. |
| Floor and alpha=0 | GREEN: T^alpha/2<=Q<=T^alpha; Q=1 exactly at the endpoint. |
| Low levels and logarithmic orders | GREEN: O(T), r=2 and r=q are retained; losses chosen before T grows. |
| p=4 | GREEN: E4=Z^4-6Z^2S2+3S2^2+8ZS3-6S4; every correction has degree below4 in Z. |
| p=12 | GREEN: pair coefficient66; head max(1,5alpha/2,1+5alpha/13); optimum alpha=26(8beta-1)/23. |
| Discrete p=16 minimum | GREEN for the restricted certificate, uniformly over the given beta interval. |
| Finite or coincident family | GREEN: falling-factorial identity still holds, including E_p=0 for fewer than p indices. |
| Fixed positive head control | GREEN as an abstract example, not an actual-arithmetic lower bound. |
| Unbounded fixed orders | GREEN: same-order absorption permits subsequences; no p(T) or uniform constants are inferred. |
| Earlier full-frontier family | GREEN with stronger scope: subsequence grants suffice; all-order induction is unnecessary. |

The head example is consistent: its large-value set has measure
c(A^(-2)+T A^(-q)), A=Q^(1/4), chosen within the nonatomic weighted
window. Outside that set B=L=1, while Z=0. For V>=1 the background is
absent from the strict event. The smallest allowed right side before
V=A is of the stated order, and its moment has the full head power.
It tests only an abstract fixed-alpha family.

## 6. Exact dependencies and artifacts read

Current-round reads authorized for this seam:

* `rounds/codex-managed/gc-full-goal-distinct-source-review/reports/blind_moment_family.md`,
  SHA256 `fe681f61a48faac2825138c8b7e0884e4f73c05b6cca789cb0f72b9f33e49e35`.
* `rounds/codex-managed/gc-full-goal-distinct-source-review/briefs/blind_moment_family_statement.md`,
  SHA256 `89ec2e5ef9a814da0fa1e1cd7efcdc941bdeca673e4688228b084b9fab8717c5`.

Earlier original allowed context remains the protocol, graph/manifest,
round217 strategy,23September strategy,214 checkpoint,216 synthesis,
accepted complete-moment and distinct kernels,216 anchored report,
208 arithmetic-frontier report and214 harmonic-source report. My frozen
report's family is recalled from its earlier derivation; it was not edited.

No current root candidate, control, synthesis, or other new current-round
artifact was read for this seam. No web source or experiment is needed
for these elementary algebraic/analytic deductions.

## 7. Recommended state effect

**GREEN** for the frozen claimant's narrow conditional mathematical
claims, subject to conductor validation and any graph decision. Preserve
the distinction between restricted nonabsorbing optimization and the
stronger same-order signed absorption. Keep every signed-integral grant
and its arithmetic availability unproved.

Record the interpretation correction to the earlier full-frontier report:
its all-order family was sufficient, but grants at an unbounded fixed-even
subsequence with Q_p=T^(1/p) already suffice by absorption. Do not carry
forward a need for every intermediate moment as an intrinsic obstacle.

Final claimant hash reviewed:
`fe681f61a48faac2825138c8b7e0884e4f73c05b6cca789cb0f72b9f33e49e35`.
No shared state or frozen original was changed. This bounded review stops.
