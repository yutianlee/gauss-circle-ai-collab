# Round 234 — statement-only mixed-radius collision bound

- Campaign: gc-connected-cumulant-test
- Task/role: blind_collision_bound / independent blind rederiver
- Status: candidate evidence only; no shared state edited
- Graph hash supplied by brief (graph not read): dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306
- Generated: 2026-10-12T00:35:39.2503841Z
- Effort: analytical/algebraic; no numerical experiments or external sources
- Scope: isolated statement only; no application asserted

## 1. Result: lemma and unsigned no-go

The requested signed collision bound is true. An explicit bound is a finite sum over set partitions of the twelve positions. The proof allows repeated labels arising from inclusion-exclusion, arbitrary mixed powers at independent radius variables, and negative block moments.

The analogous sum with an absolute value inside the label-tuple sum is not bounded by the stated data. This remains false for centered variables with all off-diagonal covariances zero and total absolute covariance mass equal to one.

## 2. Exact statement and hypotheses

Let J={1,...,12} and let B={C_1,...,C_k} partition J, where 3<=m_b:=|C_b|<=9 and k>=2. Necessarily 2<=k<=4. Write b(j) for the block containing j.

Use the probability space, real family x_d, Z, H, and finite bounds L_r of the isolated statement. Thus V=sum_d x_d^2<=H^2 almost surely, Z=sum_d x_d, and E|Z|^r<=L_r for 0<=r<=9, with L_0=1.

Define the signed sum
\[
S_B=\sum_{d_1,\ldots,d_{12}\ {\rm pairwise\ distinct}}
       \prod_{b=1}^k E\prod_{j\in C_b}x_{d_j}.
\]
For countable labels, the stipulated sufficient domination must justify its identification with the integral of the pointwise signed label sum, or equivalently the appropriate dominated finite-exhaustion limit. One concrete sufficient condition is
\[
E\left(\sum_d|x_d|\right)^9<\infty.
\]
No numerical bound on this auxiliary domination quantity enters the conclusion. More generally, any domination actually justifying the identification is enough.

For a set partition pi of J, let s_b(pi) be the number of singleton parts {j} of pi with j in C_b, and put s(pi)=sum_b s_b(pi). Then
\[
\boxed{
 |S_B|\le
 \sum_{\pi\in\mathcal P(J)}
 \left(\prod_{A\in\pi}(|A|-1)!\right)
 H^{12-s(\pi)}
 \prod_{b=1}^k L_{s_b(\pi)}. }\tag{1}
\]
Use H^0=1, including when H=0. In particular, with M=max(1,L_1,...,L_9),
\[
 |S_B|\le 12!\,\max(1,H)^{12}M^k.
\tag{2}
\]
All constants are independent of the number of labels.

## 3. Proof or derivation

### Independent radius variables

Pass to the product probability space Omega^k, with independent variables t_1,...,t_k. This is only a representation of a product of expectations; no independence between the original family members x_d is assumed. For finite label sets, Fubini gives
\[
 S_B=E_{t_1,\ldots,t_k}
 \sum_{\mathbf d\ {\rm distinct}}\prod_{j\in J}x_{d_j}(t_{b(j)}).
\tag{3}
\]

### Exact removal of collisions

For pi in P(J), put
\[
 \mu(\pi)=\prod_{A\in\pi}(-1)^{|A|-1}(|A|-1)!.
\]
For each part A define the mixed-radius power sum
\[
 M_A(\mathbf t)=
 \sum_d\prod_{b=1}^k x_d(t_b)^{a_{A,b}},
 \qquad a_{A,b}=|A\cap C_b|.
\]
Inclusion-exclusion on equality partitions gives the exact pointwise identity
\[
 \sum_{\mathbf d\ {\rm distinct}}\prod_jx_{d_j}(t_{b(j)})
 =\sum_{\pi\in\mathcal P(J)}\mu(\pi)\prod_{A\in\pi}M_A(\mathbf t).
\tag{4}
\]
Labels assigned to different parts on the right are allowed to coincide.

For completeness, fix an actual equality partition rho of a tuple. Its coefficient on the right is sum_{pi refining rho} mu(pi). This factors over the parts R of rho. On a part of size r the factor is the sum of the signs of all permutations of r elements: the cycles of a permutation provide pi, and a cycle on s elements has (s-1)! choices and sign (-1)^{s-1}. That signed permutation sum is one for r=1 and zero for r>=2, the latter by multiplication by a fixed transposition. Thus the coefficient is exactly the indicator that all tuple labels are distinct.

### All nonsingleton mixed powers are bounded by the square mass

If A has size a>=2, generalized Holder for the label sum gives
\[
\begin{aligned}
 |M_A(\mathbf t)|
 &\le\sum_d\prod_b|x_d(t_b)|^{a_{A,b}}\\
 &\le\prod_{b:a_{A,b}>0}
       \left(\sum_d|x_d(t_b)|^a\right)^{a_{A,b}/a}\\
 &\le\prod_b V(t_b)^{a_{A,b}/2}
 \le H^a.
\end{aligned}
\tag{5}
\]
The penultimate step is the elementary inclusion l^2 into l^a for a>=2. Explicitly,
sum_d |x_d|^a <= V^{(a-2)/2} sum_d |x_d|^2 = V^{a/2}.
Zero cases follow directly. This proves the required estimate even when A meets several original blocks and hence involves several independent radii.

A singleton {j} contributes exactly Z(t_{b(j)}), with its sign retained. Consequently
\[
 \left|\prod_{A\in\pi}M_A(\mathbf t)\right|
 \le H^{12-s(\pi)}\prod_b |Z(t_b)|^{s_b(\pi)}.
\tag{6}
\]
Since s_b(pi)<=m_b<=9, integration and independence of the radius variables bound (6) by
H^{12-s(pi)} prod_b L_{s_b(pi)}. Applying the triangle inequality only after the exact partition identity proves (1). No block expectation has been assumed nonnegative, and no absolute values have been inserted into the original tuple sum.

Finally, sum_pi prod_A (|A|-1)!=12!, since this counts permutations by their cycle supports. This proves (2).

### Countable labels and domination

Let A(t)=sum_d |x_d(t)|, finite almost surely. At each fixed product-space point, the unrestricted twelvefold label sum is absolutely summable, bounded by prod_b A(t_b)^{m_b}. Thus the infinite-label version of (4) is itself valid pointwise, and all nonsingleton power sums in (5) converge absolutely.

The right side of (4) is bounded in absolute value by the integrable function
\[
 G(\mathbf t)=\sum_{\pi}|\mu(\pi)|H^{12-s(\pi)}
                   \prod_b|Z(t_b)|^{s_b(\pi)}.
\]
Hence the pointwise signed sum is integrable solely from H and the L_r. To identify its integral with the externally written countable sum of products of expectations, use the domination stipulated in the question. Under the explicit sufficient condition E A^9<infinity, prod_b A(t_b)^{m_b} is integrable and dominates every finite truncation; Tonelli and dominated convergence give an absolutely convergent tuple series and the required equality.

This distinction matters: full-family bounds on Z do not themselves bound all truncated sums Z_F, because cancellations can be lost on truncation. The proof does not make that inference. The claimed countable result uses the given interchange assumption, while its final constant uses only H and L_r.

## 4. First doubtful or unproved step

There is none for finite labels, nor for countable labels under the stated sufficient-domination/interchange hypothesis.

The first unjustified step in an extension that removes that hypothesis would be exchanging the countable signed tuple sum with expectation, or asserting uniform moment bounds for all finite partial sums merely from moment bounds for Z. Neither extension is claimed here.

## 5. Control tests and outcomes

### signed_collision_sum — exact deterministic control: PASS

Take N=2n labels, n with x_d=1/sqrt(N) and n with x_d=-1/sqrt(N), on a one-point probability space. Then Z=0 and V=1. For every allowed original block partition, its signed tuple sum is
\[
 S_B=12!\,[z^{12}](1+z/\sqrt N)^n(1-z/\sqrt N)^n
     =\frac{12!\binom n6}{N^6}.
\tag{7}
\]
It is zero if n<6, and at most
12!/(6!2^6)=10395 for every n. This is an exact finite control with extensive sign cancellation. It confirms a number-independent signed bound when every positive-order L_r can be taken to be zero.

In contrast, its absolute tuple sum is (N)_{12}/N^6, which grows as N^6. For example, at N=16 it equals 65 times the signed sum, since binom(16,12)/binom(8,6)=65. Thus the distinction between the two requested kinds of sums is already essential in a finite elementary example. Deterministic centered covariances are zero, but the means here are nonzero; the next control removes that possible ambiguity.

### Centered, uncorrelated control for the unsigned sum: FAILS uniformly

This explicit analytic family shows that even zero off-diagonal covariance does not rescue an absolute tuple bound.

Let G=F_2^n x F_2^n have size q=2^{2n}, with uniform t=(u,v), and use the N=q-1 nonzero labels a=(alpha,beta). Define
\[
 x_a(u,v)=\frac{(-1)^{\alpha\cdot\beta}
                   (-1)^{\alpha\cdot u+\beta\cdot v}}{\sqrt{q-1}}.
\tag{8}
\]
Every x_a has mean zero. Character orthogonality gives
\[
 E x_a x_{a'}=\frac{\mathbf1_{a=a'}}{q-1},
 \qquad V=1,\qquad \sum_{a,a'}|\operatorname{Cov}(x_a,x_{a'})|=1.
\tag{9}
\]
These variables are uncorrelated, not mutually independent.

Summing first over beta proves the elementary identity
\[
 \sum_{\alpha,\beta}(-1)^{\alpha\cdot\beta+
                  \alpha\cdot u+\beta\cdot v}
       =\sqrt q\,(-1)^{u\cdot v}.
\]
Subtract the zero label to obtain
\[
 Z(u,v)=\frac{\sqrt q\,(-1)^{u\cdot v}-1}{\sqrt{q-1}},
 \qquad |Z|\le\sqrt3\quad(q>=4).
\tag{10}
\]
Thus all members of this family satisfy H=1 and the same bounds L_r=3^{r/2}.

For any block C of size m, character orthogonality gives the exact signed moment
\[
 E\prod_{j\in C}x_{a_j}
 =(q-1)^{-m/2}
   \left(\prod_{j\in C}(-1)^{\alpha_j\cdot\beta_j}\right)
   \mathbf1_{\sum_{j\in C}a_j=0}.
\tag{11}
\]
It can be negative: the distinct labels (e_1,0), (0,e_1), and (e_1,e_1) have sum zero and triple moment -(q-1)^{-3/2}.

To count distinct twelve-tuples satisfying each block constraint, choose m_b-1 free G-valued labels in block b and force its last label to be their sum. There are q^{12-k} unrestricted choices. Each of the twelve resulting labels is a nonzero linear form in those free variables. These twelve forms are pairwise distinct because m_b>=3 and different blocks use disjoint free coordinates. Consequently each condition that a label vanish or that a pair coincide excludes exactly q^{11-k} choices. There are 12+binom(12,2)=78 such conditions. The union bound therefore gives at least
\[
 q^{12-k}(1-78/q)
\]
valid ordered distinct nonzero tuples.

By (11), each contributes exactly (q-1)^{-6} to the absolute tuple sum. Hence, for q>78,
\[
 \sum_{\mathbf a\ {\rm distinct}}
   \left|\prod_b E\prod_{j\in C_b}x_{a_j}\right|
 \ge\frac{q^{12-k}(1-78/q)}{(q-1)^6}.
\tag{12}
\]
Along q=2^{2n} this diverges as q^{6-k}; k<=4. All of H, the permitted global moment bounds, and total absolute covariance mass remain fixed. This disproves every number-independent absolute-tuple estimate based solely on those budgets, for every allowed block partition. Pairwise uncorrelatedness is strictly weaker than the higher-order independence that would make (11) vanish.

### blind_isolation — PASS

Only the three files listed below were read. The graph, active campaign, application context, sibling reports, and prior derivations were not read. No source theorem or computational experiment was used.

## 6. Dependencies and exact artifacts used

The proof uses only elementary finite partition algebra, Holder, independent product-space integration, and the countable interchange hypothesis. The controls use elementary generating functions and finite-character orthogonality proved in the displayed calculations.

SHA-256 of all context read:

- protocol.md:
  f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a
- rounds/codex-managed/gc-connected-cumulant-test/briefs/blind_collision_bound.md:
  6e4a786bc784c46f371f98f5cb0cce24283a74291123aba597459fe0a92257a4
- rounds/codex-managed/gc-connected-cumulant-test/briefs/isolated_collision.md:
  605a7c3f57923c692e55deab3e1157d29d2dcc0d313630eeac2a54a3753db551

Exact diagnostic command for context hashes:
Get-FileHash -Algorithm SHA256 -LiteralPath 'protocol.md','rounds/codex-managed/gc-connected-cumulant-test/briefs/blind_collision_bound.md','rounds/codex-managed/gc-connected-cumulant-test/briefs/isolated_collision.md'

Only output artifact:
rounds/codex-managed/gc-connected-cumulant-test/reports/blind_collision_bound.md

## 7. Recommended state effect

Promote the isolated finite signed collision lemma, and its countable version with the stated interchange condition, only through the conductor's required review and state process.

Reject a corresponding number-independent absolute-tuple bound under H, lower global moment bounds, and bounded covariance mass; (12) is an explicit counterfamily.

No number-theoretic or downstream state implication is asserted. This assigned task is complete and frozen; no successor round is proposed.
