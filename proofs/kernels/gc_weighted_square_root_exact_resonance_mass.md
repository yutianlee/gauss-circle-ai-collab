# Weighted square-root exact-resonance kernel

Round 201; campaign `gc-whole-discrepancy-twelfth-moment`.
Conductor formalization, 2026-09-23. Acceptance is determined solely by
the graph and its validated State Patch. Starting raw graph SHA-256:
`2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5`.

## 1. Statement

Fix an integer k>=2. For a nonnegative sequence b_n, n>=1, write

\[
 A_d=\sum_{s\ge1}b_{ds^2},\qquad
 S=\sum_{d\ \mathrm{squarefree}} A_d^2<\infty.
\]

Let B_k be the number of partitions of {1,...,k} with no singleton
block. With independently chosen signs and ordered indices,

\[
 \mathcal R_k(b):=
 \sum_{\epsilon\in\{-1,1\}^k}
 \sum_{\substack{n_1,\ldots,n_k\ge1\\
                  \sum_j\epsilon_j\sqrt{n_j}=0}}
 \prod_{j=1}^k b_{n_j}
 \le 2^k B_k S^{k/2}.                                      \tag{K1}
\]

This includes every exact radical relation, all sign imbalances,
repeated indices, the squarefree class d=1, unequal cutoffs and infinite
sequences. There is no assertion about nonzero small radical differences.

For k possibly different sequences b^(j), with corresponding S_j,
the mixed bound is 2^k B_k product_j S_j^(1/2).
In particular, if b_n<=C tau(n)n^(-3/4), then

\[
 S\le C^2\zeta(3/2)^{10},\qquad
 \mathcal R_k(b)\le 2^k B_k C^k\zeta(3/2)^{5k}.              \tag{K2}
\]

## 2. Radical independence, with its algebraic hypotheses proved

For finitely many distinct primes p_1,...,p_r, simultaneously prove:
(i) K_r=Q(sqrt(p_1),...,sqrt(p_r)) has the basis of the 2^r products
of distinct prime radicals; (ii) a nonzero rational q is a square in
K_r if and only if q=c^2 product_(i in I) p_i for c in Q and a subset I.
Both statements hold for r=0. By (ii), p_r is not a square in K_(r-1):
its p_r-adic valuation is odd whereas that of any old squareclass is
even. The extension is therefore quadratic and the basis doubles.
If (u+v sqrt(p_r))^2=q is rational, comparison in the quadratic basis
gives 2uv=0. Either q=u^2 is a rational square in the old field, or
q/p_r=v^2 is such a square. The induction proves (ii), including its
converse, and closes both assertions. In particular, distinct
squarefree radicals are distinct members of this basis and are
Q-linearly independent, including sqrt(1)=1.

Write n_j=d_j s_j^2 uniquely. Independence implies that an exact
resonance satisfies sum_(j:d_j=d) epsilon_j s_j=0 in each occupied
class. As s_j>=1, every occupied class contains at least two labels.

## 3. Full counting and the mixed bound

Partition the labels by their squarefree class. For a fixed partition
and fixed sign vector, drop both the integer relations within blocks
and the restriction that distinct blocks use distinct d. All terms
are nonnegative, so this increases the sum. For a block I of size h>=2
the resulting factor is

\[
 \sum_d\prod_{j\in I} A_d^{(j)}
 \le\prod_{j\in I}\left(\sum_d(A_d^{(j)})^h\right)^{1/h}
 \le\prod_{j\in I}S_j^{1/2}.
\]

The first inequality is Holder; the second is the sequence norm
inequality l^h<=l^2 for h>=2. Multiplication across blocks and summation
over at most B_k partitions and 2^k signs prove the mixed bound and K1.
Prove this first for finite supports, then use monotone convergence.
Zero S_j gives a zero sequence and is handled directly.

## 4. Divisor envelope and uniform exact tails

Submultiplicativity gives tau(ds^2)<=tau(d)tau(s^2). For a prime
exponent e>=0, 2e+1<=binomial(e+2,2), so tau(s^2)<=tau_3(s). Therefore

\[
 A_d\le C\tau(d)d^{-3/4}\zeta(3/2)^3.
\]

For squarefree d, tau(d)^2=tau_4(d). Hence
sum_(d squarefree) tau(d)^2 d^(-3/2)<=zeta(3/2)^4, proving K2.
The identities for tau_j follow by expanding the j-fold product of
the absolutely convergent positive series sum_(n>=1)n^(-3/2).
No external asymptotic theorem is used.

If S_>U=sum_d(sum_(ds^2>U)b_(ds^2))^2, then S_>U tends to zero by
dominated convergence. A union bound over the index exceeding U and
the mixed estimate show

\[
 \sum_\epsilon\sum_{\substack{\sum\epsilon_j\sqrt{n_j}=0\\
                            \max_j n_j>U}}\prod_j b_{n_j}
 \le k2^k B_k S_{>U}^{1/2}S^{(k-1)/2}.                         \tag{K3}
\]

A common divisor envelope makes this convergence uniform in any
family dominated by that envelope. This statement concerns exact
resonance tails, not tails of an arbitrary unsmoothed Fourier series.

## 5. Exact coefficient in a cosine moment

Let a_n be real, |a_n|<=b_n, and first take finite support. Put
H(R)=sum_n a_n cos(2pi R sqrt(n)-3pi/4), e(t)=exp(2pi i t), and
let w be a real nonnegative integrable weight. Using
w-hat(xi)=integral w(u)e(-u xi)du, the exact-frequency part of
integral w(R/T)H(R)^k dR is

\[
 D_k(T)=T\widehat w(0) E_k,
 \quad E_k=2^{-k}\sum_\epsilon
 \sum_{\sum\epsilon_j\sqrt{n_j}=0}
 e\!\left(-\frac38\sum_j\epsilon_j\right)\prod_j a_{n_j}.
\]

It obeys |D_k(T)|<=T||w||_1 B_k S^(k/2). For even k, E_k>=0:
replace sqrt(d)R by an independent torus coordinate x_d. The
polynomial F(x)=sum_(d,s) a_(ds^2)cos(2pi s x_d-3pi/4) is real, so
the integral of F^k over its finite torus is nonnegative. Its constant
coefficient is exactly E_k by the proved radical independence.
This is an algebraic constant-coefficient identity, not an assertion
of independent phases on a finite radius interval.

K3 justifies passage to infinite exact coefficients. If also
sum_n|a_n|<infinity, it justifies their identification with the exact
part of the infinite moment expansion by absolute convergence. Without
that extra hypothesis only the absolutely convergent exact subseries
is asserted; no infinite H is assumed to exist.

For the actual fixed-window circle coefficients
a_n(T)=r_2(n)n^(-3/4)Psi(sqrt(n/T)), with real Schwartz Psi, |Psi|<=1,
we have sum_n|a_n(T)|<infinity for each fixed T and the envelope C=4
from r_2(n)=4 sum_(d|n)chi_4(d)<=4tau(n). Thus
0<=D_12(T)<=T||w||_1 B_12 4^12 zeta(3/2)^60, uniformly in T.
This application uses only the accepted arithmetic identity, not a
pointwise circle estimate or M1/M2 bound.

## 6. Controls and first unproved step

For k=2 the exact absolute mass is 2 sum_n b_n^2, and the real cosine
exact coefficient is (1/2)sum_n a_n^2, agreeing with the Fourier
normalization. Nonpairing relations such as 5+7=6+6 at indices
(25,49,36,36) are included, and can be padded with cancelling pairs.
Individual exact terms need not be nonnegative: eight plus copies of
n=1 and four minus copies of n=4 have zero frequency but cosine phase
e(-3*4/8)=-1. Only the total even constant coefficient is nonnegative.

Nonzero near-resonances remain. For example
sqrt(m^2+1)+sqrt(m^2+49)-2sqrt(m^2+25) is strictly negative by
concavity and equals -144m^(-3)+O(m^(-5)); all indices represent sums
of two squares. With T a sufficiently large fixed multiple of m^2,
T times this difference tends to zero inside the physical smoothing
range. This does not give a lower bound for the complete moment.

The first unproved analytic step is bounding the complete signed sum
over nonzero differences, retaining w-hat(-T Delta) and its phase.
K1--K3 and D_12=O(T) provide no such bound. No parent obligation,
pointwise exponent, or Gauss circle target is discharged.

## 7. Evidence and state scope

Independent derivations are archived in the current campaign under
`reports/blind_exact_resonance_rederivation.md` (statement-only),
`reports/whole_moment_analytic_attack.md` (independent whole source), and
`controls/conductor_resonance_and_bridge_analysis.md`. The blind task
received neither graph nor claimant derivation. Subsequent review of
this formal kernel is a separate explicit stage. The generic theorem
is self-contained; its circle specialization uses H1-H3's arithmetic
identity. Only this exact-resonance kernel is proposed for promotion.
