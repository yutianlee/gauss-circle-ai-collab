# Round 224: isolated prime-allocation identities

## 1. Result

The finite divisor-allocation identity, its overlap correction, commutator defect, adjoint and exact radial dilation formula all hold as derived below. Constant profiles satisfy the expected prime-power eigenrelation. At the prime \(2\), only the allocation to the first coordinate survives.

For the constant profile and a one-point test, every split-prime contribution attains the coefficient triangle with the same sign. Consequently the scalar identity alone gives no automatic inverse-square-root gain in the number of split primes. This is a finite control of that inference, not a no-go theorem for other norms, arrays or coefficient-sensitive arguments.

This is current statement-only isolation, not history-free work: this reused agent retains prior campaign roles, reports and reviews. For this task I read only the assigned statement and protocol. No application, manifest, graph, strategy, sibling, web source or experiment was consulted. Only this report is written.

## 2. Exact statement and hypotheses

Let \(\chi=\chi_4\), including \(\chi(q)=0\) for even \(q\), and let \(A:\mathbb N^2\to\mathbb C\) be arbitrary. Define
\[
 c_A(n)=\sum_{hq=n}\chi(q)A(h,q),\qquad
 L_A(F)=\sum_{n\ge1}c_A(n)F(n)
\]
for finitely supported \(F:\mathbb N\to\mathbb C\). Divisor sums and all pairings below are finite; no summability assumption on \(A\) is needed. Set \(c_B(n/p)=0\) whenever \(p\nmid n\).

For an odd prime \(p\), write \(\epsilon=\chi(p)\), \(\lambda=1+\epsilon\), and
\[
 U A(h,q)=A(h,pq),\quad V A(h,q)=A(ph,q),\quad
 W A(h,q)=A(ph,pq).
\]
Then
\[
 \boxed{c_A(pn)=c_{VA}(n)+\epsilon c_{UA}(n)
                         -\epsilon c_{WA}(n/p)}
 \tag{1}
\]
and, with \(E_{p,A}(n)=c_A(pn)+\epsilon c_A(n/p)-\lambda c_A(n)\),
\[
 \boxed{E_{p,A}(n)=c_{VA-A}(n)+\epsilon c_{UA-A}(n)
                         -\epsilon c_{WA-A}(n/p).}
 \tag{2}
\]
For the specified adjoint
\[
 (T_p^*F)(m)=\mathbf1_{p\mid m}F(m/p)+\epsilon F(pm),
\]
the exact sign is
\[
 \boxed{\lambda L_A(F)=L_A(T_p^*F)-\sum_nE_{p,A}(n)F(n).}
 \tag{3}
\]
Here the star denotes the transpose for the displayed bilinear pairing; because the operator entries are real, it is also the usual formal adjoint for a Hermitian pairing after inserting the appropriate conjugation.

## 3. Proof and derivation

### Allocation and multiplicity

Every pair \((H,Q)\) with \(HQ=pn\) lies in the union of \(p\mid H\) and \(p\mid Q\). The first set, parametrized by \((H,Q)=(ph,q)\), contributes \(c_{VA}(n)\). The second, parametrized by \((H,Q)=(h,pq)\), contributes \(\epsilon c_{UA}(n)\). Their intersection exists precisely when \(p\mid n\); writing \((H,Q)=(ph,pq)\) gives \(\epsilon c_{WA}(n/p)\). Inclusion-exclusion proves (1).

More explicitly, write \(n=p^r m\) with \(p\nmid m\). For each \(h_0q_0=m\), the original pairs are
\[
 (H,Q)=(p^a h_0,p^{r+1-a}q_0),\qquad 0\le a\le r+1,
\]
with weight \(\epsilon^{r+1-a}\chi(q_0)\). The \(V\) term contains \(1\le a\le r+1\), the \(U\) term contains \(0\le a\le r\), and the subtracted overlap contains \(1\le a\le r\). Each original pair is therefore counted exactly once. For \(r=0\) the intersection is empty; for \(r=1\) it has one allocation per \((h_0,q_0)\); for \(r=2\) it has two. There is no extra multiplicity at higher valuations.

Linearity of \(A\mapsto c_A\), followed by subtracting \((1+\epsilon)c_A(n)\) and adding \(\epsilon c_A(n/p)\), proves (2). In particular, for \(n=1\),
\[
 c_A(p)=A(p,1)+\epsilon A(1,p),\qquad
 E_{p,A}(1)=A(p,1)+\epsilon A(1,p)-\lambda A(1,1).
\]

### Adjoint and prime sums

Reindexing the two finite sums gives
\[
 \begin{aligned}
 \sum_n c_A(pn)F(n)
   &=\sum_{p\mid m}c_A(m)F(m/p),\\
 \sum_n c_A(n/p)F(n)
   &=\sum_m c_A(m)F(pm).
 \end{aligned}
\]
Thus \(L_A(T_p^*F)=\lambda L_A(F)+\sum_nE_{p,A}(n)F(n)\), proving (3). The same calculation rewrites the defect as
\[
 \sum_n E_{p,A}(n)F(n)
 =L_{VA-A}(F)+\epsilon L_{UA-A}(F)
                   -\epsilon L_{WA-A}(F(p\,\cdot)).
 \tag{4}
\]
The overlap term in (4) has a minus sign; after solving for \(\lambda L_A(F)\) its sign is plus.

For any finite collection \(\mathcal P\) of odd primes,
\[
 \boxed{
 \left(\sum_{p\in\mathcal P}\lambda_p\right)L_A(F)
 =L_A\left(\sum_{p\in\mathcal P}T_p^*F\right)
       -\sum_{p\in\mathcal P}\sum_nE_{p,A}(n)F(n).}
 \tag{5}
\]
This is linearity, not orthogonality. The coefficient on the left is twice the number of primes congruent to \(1\bmod4\). If \(\epsilon=-1\), then \(\lambda=0\), \(T_p^*F=\mathbf1_{p\mid m}F(m/p)-F(pm)\), and
\[
 E_{p,A}=c_{VA-A}-c_{UA-A}+c_{WA-A}(\,\cdot/p).
\]
Equation (3) then identifies two expressions for the defect and cannot be divided by \(\lambda\). In particular, an all-inert collection gives no nonzero scalar multiple of \(L_A(F)\).

### Exact radial dilation and cutoffs

Let \(X,N>0\), \(M=\lfloor N\rfloor\), and
\[
 F_{X,N}(n)=\mathbf1_{1\le n\le N}n^{-3/4}e(\sqrt{Xn}),
 \qquad e(t)=\exp(2\pi it).
\]
For every positive integer \(m\),
\[
 \boxed{\begin{aligned}
 T_p^*F_{X,N}(m)
 ={}&p^{3/4}\mathbf1_{p\mid m}\mathbf1_{1\le m\le pM}
       m^{-3/4}e\!\left(\sqrt{(X/p)m}\right)\\
 &+\epsilon p^{-3/4}\mathbf1_{1\le m\le\lfloor N/p\rfloor}
       m^{-3/4}e\!\left(\sqrt{(pX)m}\right).
 \end{aligned}}
 \tag{6}
\]
The first term follows from \((m/p)^{-3/4}=p^{3/4}m^{-3/4}\); the second follows from \((pm)^{-3/4}=p^{-3/4}m^{-3/4}\). For the first term, divisibility and positivity imply \(m\ge p\), and the last admissible multiple is \(p\lfloor N\rfloor\). For the second,
\(\lfloor N/p\rfloor=\lfloor\lfloor N\rfloor/p\rfloor\).
Both endpoints are inclusive. If \(N<1\), both supports are empty. If both terms are supported at the same \(m\), both remain: their different phases do not permit a formal cancellation.

Equivalently,
\[
 T_p^*F_{X,N}
 =p^{3/4}\mathbf1_{p\mid\,\cdot}\,F_{X/p,pM}
       +\epsilon p^{-3/4}F_{pX,N/p}.
 \tag{7}
\]
The parameter \(pM\) in the first cutoff is deliberate; replacing it by \(pN\) is harmless only while retaining the divisibility mask.

Pairing (6) with \(c_A(m)\) keeps exactly the same array \(A\) in both terms. Even if \(A\) were externally labelled by \(X\), this identity would retain that fixed \(A_X\) when the wave changes to \(X/p\) or \(pX\). Replacing it by \(A_{X/p}\) or \(A_{pX}\) would require a separate difference identity and estimate.

### Constant profile and the prime \(2\)

For \(A=1\), write \(a(n)=c_1(n)=\sum_{q\mid n}\chi(q)\). Unique divisor factorization shows that \(a\) is multiplicative. For odd \(p\), put
\[
 s_r=a(p^r)=\sum_{j=0}^r\epsilon^j,\qquad s_{-1}=0.
\]
Then
\[
 s_{r+1}+\epsilon s_{r-1}=(1+\epsilon)s_r\quad(r\ge0).
 \tag{8}
\]
For \(n=p^rm\), \(p\nmid m\), multiply (8) by \(a(m)\). This proves
\[
 a(pn)+\epsilon a(n/p)=\lambda a(n)
 \tag{9}
\]
including \(r=0\). Alternatively, \(U1=V1=W1=1\) makes (2) vanish.

For \(p\equiv1\bmod4\), \(s_r=r+1\), and
\(s_{r+1}=2s_r-s_{r-1}\). For \(p\equiv3\bmod4\), \(s_r=1\) for even \(r\) and \(0\) for odd \(r\), with \(s_{r+1}=s_{r-1}\) for \(r\ge1\), \(s_0=1,s_1=0\). These include all higher prime powers.

The prime \(2\) must not be assigned either odd-prime sign. Every nonzero divisor contribution has odd second coordinate. Therefore
\[
 c_A(2n)=c_{V_2A}(n),\qquad
 E_{2,A}(n):=c_A(2n)-c_A(n)=c_{V_2A-A}(n).
 \tag{10}
\]
The \(U_2\) and overlap allocations have even second coordinate and zero character weight. Formally taking \(\epsilon_2=0,\lambda_2=1\) in the algebra reproduces (10), but the odd-prime conclusions using \(\epsilon=\pm1\) do not extend.

Here \(T_2^*F(m)=\mathbf1_{2\mid m}F(m/2)\), and
\[
 L_A(F)=L_A(T_2^*F)-\sum_nE_{2,A}(n)F(n).
\]
Its radial formula is only the first line of (6), with \(p=2\). For the constant profile \(a(2^r)=1\) for every \(r\ge0\), so \(a(2n)=a(n)\); there is no backward term.

## 4. First doubtful or unproved step

No step remains unproved in the finite identities above. They provide neither an estimate for the profile differences in (2) nor an estimate for cancellation between primes in (5). Any positive application must supply those separately.

In particular, replacing the prime sum in (5) by an orthogonal or independent sum, discarding its coefficient norm, or changing the profile along with a radial dilation is unsupported. The control below refutes only an automatic improvement over the displayed coefficient triangle from the scalar identity alone.

## 5. Required controls and outcomes

Let \(\mathcal P\) be any nonempty finite set of split primes and \(s=|\mathcal P|\). Take \(A=1\) and \(F=\delta_1\). Then \(L_1(F)=a(1)=1\), every defect vanishes, and
\[
 T_p^*\delta_1=\delta_p,\qquad a(p)=2.
\]
Consequently
\[
 L_1\left(\sum_{p\in\mathcal P}T_p^*\delta_1\right)=2s
 =\sum_{p\in\mathcal P}\sum_m
       |a(m)T_p^*\delta_1(m)|.
 \tag{11}
\]
The aggregate coefficient triangle is also exactly \(2s\). Division by the eigenvalue sum \(2s\) gives \(1\), with no saving. A uniform extra factor \(Cs^{-1/2}\) on this triangle would require \(\sqrt s\le C\). Arbitrarily large such finite sets exist by the elementary argument: a prime divisor of \((2\prod_{p\in\mathcal P}p)^2+1\) is new and congruent to \(1\bmod4\), since \(2\prod p\) has order four modulo that prime.

Even though the vectors \(\delta_p\) in this example have disjoint supports, their sum has norm \(\sqrt s\) and the coefficient vector on those supports has norm \(2\sqrt s\). Cauchy gives exactly \(2s\). This explains why even this special orthogonality does not give a free gain after contraction. It makes no claim against other norms or arguments.

The same control occurs within the specified radial family at \(N=1\): \(F_{X,1}=e(\sqrt X)\delta_1\), and every transformed nonzero value is the common phase \(e(\sqrt X)\), as (6) confirms.

| Control | Outcome |
|---|---|
| \(n=1\), \(p\nmid n\) | GREEN; no overlap and no backward coefficient. |
| \(p\mid n\), \(p^2\mid n\), higher powers | GREEN; the explicit allocation index counts every pair once. |
| Adjoint defect sign | GREEN; (3) subtracts the defect when solving for \(\lambda L_A(F)\). |
| Empty support and terminal integer | GREEN; both floors and inclusive endpoints are retained in (6). |
| Inert primes | GREEN; zero eigenvalue is not inverted. |
| Prime \(2\) | GREEN; zero-character allocations vanish, leaving (10). |
| Constant prime powers | GREEN; explicit values and recurrence (8) agree. |
| Automatic split-prime square-root saving | REJECTED for the scalar-identity-only inference by (11). |
| Other arrays, norms or signed mechanisms | UNASSESSED, not ruled out. |

All controls are exact finite algebra, not experiments.

## 6. Dependencies and exact artifacts used

Campaign: m9-m1-complete-gar-prime-amplification. Round: 224. Role: blind_prime_allocation. Date: 28 September 2026, Asia/Shanghai. Current statement-only isolation with retained prior history disclosed in Section 1.

Exactly two input files were read:

| Input | SHA-256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| rounds/codex-managed/m9-m1-complete-gar-prime-amplification/briefs/blind_prime_allocation_statement.md | 9d11e4a9c11a6a1e5728c20faad3ba3eee091cc0290ab97db8872802a402bdef |

The proofs use only finite reindexing, multiplicativity of the given character and elementary inclusion-exclusion. No external theorem was imported. No graph hash or application status is asserted, since those files were not read. Effort was entirely analytical, with zero experiments. This report is the sole output.

## 7. Recommended state effect

Retain the finite identities and the narrowly scoped constant-profile control as statement-only evidence for the conductor's required review. No application estimate, owner closure or shared-state promotion follows from this report. No successor is proposed or begun. Stop after freezing this artifact.
