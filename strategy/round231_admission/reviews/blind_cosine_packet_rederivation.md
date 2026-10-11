# Round231 admission — blind cosine-packet rederivation

- Task/interface: `blind_cosine_packet_rederivation`; fixed-norm, sign-pooled certificate.
- Role: statement-only independent reviewer; no promotion authority.
- Generated: 2026-10-11T10:30:56+08:00.
- Previously supplied graph SHA256, recorded only as a provenance tag and not inspected: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
- Isolation disclosure: this is a **new isolated mathematical interface following the unrelated prime-relations task**. That earlier report remains frozen and is not a mathematical dependency here. For this new task I read only `protocol.md` and the supplied cosine-packet statement. I did not read a discovery report, another packet artifact, the graph, history, or conductor computations.
- Effort allocation: analytical proof and exact algebraic controls only; no numerical experiment or computational proof.

## 1. Result: lemma or no-go result

**The precise certificate claim holds from the supplied inputs.** There are constants \(c_*>0\) and \(T_0\) such that

\[
\boxed{\mathcal C_{\cos}(T)\ge c_*T^{5/2}\qquad(T\ge T_0).}
\]

The proof retains a positive fraction of the supplied six-against-six near-resonance mass after discarding tuples with a second, nonparallel, sign relation of size at most \(H/T\), where \(H\) is a sufficiently large fixed constant. The discarded product weight is at most

\[
(2^{12}-2)\,M_T^{10}\bigl(\max_{n\in S_T}a_n(T)\bigr)^2
\ll T^{1+2\varepsilon}=o(T^{3/2})
\]

for any fixed \(\varepsilon<1/4\). On each retained norm tuple, the distinguished sign pair has positive integral contribution of order \(T\), while Fourier decay makes the total of all other signs smaller. The modulus may therefore be taken after all 4096 signs have been summed for that tuple.

This result supplies no lower bound for a fully signed sum after different norm tuples are combined, and no lower bound for a certificate that first combines all harmonics at fixed squarefree labels.

## 2. Exact statement and hypotheses

Use the Fourier convention

\[
\widehat w(\xi)=\int_{\mathbb R}w(u)e^{-2\pi i u\xi}\,du.
\]

The supplied \(w\) is real, nonnegative, smooth, supported in \([1/2,2]\), with
\(W=\int w>0\). Let \(a_n(T)\), \(Q=\lfloor T^{2/5}\rfloor\), and \(d(n)\) have exactly the meanings in the isolated statement. Fix a sufficiently small shell constant \(c_0>0\), and write

\[
S_T=\{n\in[c_0T,2c_0T]\cap\mathbb N:d(n)>Q\},\qquad
M_T=\sum_{n\in S_T}a_n(T),\qquad b_T=\max_{n\in S_T}a_n(T).
\]

The proof uses only these supplied coefficient facts:

1. \(a_n(T)\ge0\) on \(S_T\).
2. \(M_T\asymp T^{1/4}\).
3. For each fixed \(\varepsilon>0\), \(b_T\ll_\varepsilon T^{-3/4+\varepsilon}\).
4. For every sufficiently small fixed \(\delta>0\), the total weight
   \(\prod_{j=1}^{12}a_{n_j}(T)\) of ordered tuples in \(S_T^{12}\) with pairwise distinct \(d(n_j)\) and

\[
\left|\sum_{j=1}^{6}\sqrt{n_j}-\sum_{j=7}^{12}\sqrt{n_j}\right|\le\delta/T
\]

is at least \(c_\delta T^{3/2}\) for all sufficiently large real \(T\), where \(c_\delta>0\).

No separation theorem for different radical sums is assumed. The only spacing used below is the elementary spacing of individual square roots of distinct integers in this fixed shell. There is no arithmetic assumption beyond the supplied inputs and this elementary fact.

The proof takes a finite subset of the nonnegative certificate sum. It requires no exchange of an infinite sum and an integral, and no extra global coefficient estimate.

## 3. Proof or derivation

### A. Fix the near-resonance and Fourier thresholds

Set

\[
\sigma^0=(1,1,1,1,1,1,-1,-1,-1,-1,-1,-1),
\qquad L_\sigma(\mathbf n)=\sum_{j=1}^{12}\sigma_j\sqrt{n_j}.
\]

Choose a fixed \(\delta>0\) sufficiently small for supplied input 4, and also \(\delta\le1/12\). If \(|\xi|\le\delta\), then \(|2\pi u\xi|\le\pi/3\) on the support of \(w\). Consequently

\[
\operatorname{Re}\widehat w(\xi)
=\int w(u)\cos(2\pi u\xi)\,du\ge W/2.
\tag{1}
\]

Integration by parts shows that \(\widehat w(\xi)\) decays faster than any power of \(|\xi|\): for each positive integer \(N\),

\[
|\widehat w(\xi)|\le(2\pi|\xi|)^{-N}\|w^{(N)}\|_1\qquad(\xi\ne0).
\]

Choose a fixed \(H>\delta\), sufficiently large that

\[
(2^{12}-2)\sup_{|\xi|>H}|\widehat w(\xi)|\le W/2.
\tag{2}
\]

Both thresholds are fixed before \(T\) grows.

### B. Two independent short sign relations cost two coefficient factors

Let \(\tau\in\{\pm1\}^{12}\setminus\{\sigma^0,-\sigma^0\}\). Consider tuples in \(S_T^{12}\) satisfying

\[
|L_{\sigma^0}(\mathbf n)|\le\delta/T,
\qquad |L_\tau(\mathbf n)|\le H/T.
\tag{3}
\]

Because \(\tau\) is not parallel to \(\sigma^0\), there are two indices \(i,j\) such that

\[
D=\sigma_i^0\tau_j-\sigma_j^0\tau_i\in\{-2,2\}.
\]

Fix all ten remaining norms. Writing their contributions to the two linear forms as \(A,B\), conditions (3) say

\[
\begin{pmatrix}\sigma_i^0&\sigma_j^0\\\tau_i&\tau_j\end{pmatrix}
\begin{pmatrix}\sqrt{n_i}\\\sqrt{n_j}\end{pmatrix}
=\begin{pmatrix}-A+u\\-B+v\end{pmatrix},
\qquad |u|\le\delta/T,\quad |v|\le H/T.
\]

The inverse matrix has entries of absolute value \(1/2\). Each of \(\sqrt{n_i}\) and \(\sqrt{n_j}\) is therefore restricted to an interval of length at most

\[
(\delta+H)/T.
\tag{4}
\]

On the other hand, distinct integers in the shell have square-root spacing at least a positive constant times \(T^{-1/2}\). More explicitly, for consecutive integers in or adjacent to the shell,

\[
\sqrt{n+1}-\sqrt n
=\frac1{\sqrt{n+1}+\sqrt n}
\ge\frac1{2\sqrt{2c_0T+1}}.
\]

Since \(H,\delta,c_0\) are fixed, the interval length (4) is smaller than this spacing for all sufficiently large \(T\). Each interval then contains at most one square root of an allowed integer, so the ten fixed norms admit **at most one ordered pair** \((n_i,n_j)\) satisfying (3).

By nonnegativity of the coefficients, the total product weight of (3), even without imposing pairwise distinct squarefree labels, is bounded by

\[
b_T^2\sum_{(n_k)_{k\ne i,j}\in S_T^{10}}\prod_{k\ne i,j}a_{n_k}(T)
=b_T^2M_T^{10}.
\tag{5}
\]

This is a weighted estimate, not an unweighted count converted without justification.

### C. Retain most of the supplied near-resonance mass

Let \(\mathcal N_T\) be the tuples counted by supplied input 4, including its distinct-label condition. Define the good subset \(\mathcal G_T\subset\mathcal N_T\) by requiring

\[
|L_\tau(\mathbf n)|>H/T
\quad\text{for every }\tau\ne\pm\sigma^0.
\tag{6}
\]

The union bound and (5) give

\[
\sum_{\mathbf n\in\mathcal N_T\setminus\mathcal G_T}
\prod_{j=1}^{12}a_{n_j}(T)
\le(2^{12}-2)b_T^2M_T^{10}.
\tag{7}
\]

Take, for example, the fixed permitted exponent \(\varepsilon=1/8\). Then

\[
b_T^2M_T^{10}\ll
T^{-3/2+1/4}T^{10/4}=T^{5/4}=o(T^{3/2}).
\]

Thus, for all sufficiently large real \(T\),

\[
\sum_{\mathbf n\in\mathcal G_T}\prod_{j=1}^{12}a_{n_j}(T)
\ge\frac{c_\delta}{2}T^{3/2}.
\tag{8}
\]

The pairwise distinct squarefree labels remain in force on the retained set. Their arithmetic was not needed in the upper bound (7), where enlarging the set was legitimate.

### D. Pool all 4096 cosine signs at one fixed norm tuple

For a fixed tuple define the integral with coefficients temporarily factored out:

\[
J_T(\mathbf n)=\int_{\mathbb R}w(R/T)
\prod_{j=1}^{12}\cos\!\left(2\pi R\sqrt{n_j}-\frac{3\pi}4\right)\,dR.
\]

The finite exponential expansion, followed by \(R=Tu\), gives exactly

\[
J_T(\mathbf n)=\frac{T}{2^{12}}
\sum_{\sigma\in\{\pm1\}^{12}}
\exp\!\left(-\frac{3\pi i}{4}\sum_j\sigma_j\right)
\widehat w(-T L_\sigma(\mathbf n)).
\tag{9}
\]

For \(\sigma=\pm\sigma^0\), the phase multiplier equals one because each sign vector has six plus and six minus entries. Since \(w\) is real, their sum is

\[
\widehat w(-T L_{\sigma^0})+\widehat w(T L_{\sigma^0})
=2\operatorname{Re}\widehat w(T L_{\sigma^0})\ge W
\tag{10}
\]

on \(\mathcal G_T\), by (1). Every other phase multiplier has modulus one. For a good tuple, (2) and (6) bound the absolute value of the sum of all other 4094 terms by \(W/2\).

The integral \(J_T(\mathbf n)\) is real. Equations (9)--(10) therefore imply the stronger pointwise conclusion

\[
J_T(\mathbf n)\ge\frac{W}{2^{13}}T>0
\qquad(\mathbf n\in\mathcal G_T).
\tag{11}
\]

In particular, this does not put a modulus around individual cosine signs. The entire fixed-tuple sum in (9) has already been formed before its positive lower bound is asserted.

### E. Sum only over the good norm tuples

Put \(A_T(\mathbf n)=\prod_j a_{n_j}(T)\ge0\) on the shell. Each tuple in \(\mathcal G_T\) satisfies the index restrictions in the certificate. Using only its nonnegative summands, (8) and (11) yield

\[
\begin{aligned}
\mathcal C_{\cos}(T)
&\ge\sum_{\mathbf n\in\mathcal G_T}|A_T(\mathbf n)J_T(\mathbf n)|\\
&\ge\frac{W}{2^{13}}T
\sum_{\mathbf n\in\mathcal G_T}A_T(\mathbf n)\\
&\ge\frac{Wc_\delta}{2^{14}}T^{5/2}.
\end{aligned}
\]

This proves the stated claim, with one possible choice \(c_*=Wc_\delta/2^{14}\).

### F. Exact limitation under further grouping

Let \(I_{\mathbf n}=A_T(\mathbf n)J_T(\mathbf n)\). The conclusion is a lower bound for \(\sum_{\mathbf n}|I_{\mathbf n}|\). It does not imply a lower bound for \(|\sum_{\mathbf n}I_{\mathbf n}|\): contributions from other norm tuples may cancel the positive good-tuple contribution before the final modulus. Thus a proposed fully signed bound of order \(T^{29/25+\varepsilon}\) is not refuted by this certificate lower bound. This report neither proves nor disproves that signed bound.

Likewise, writing \(n_j=d_jm_j^2\), a quantity of the form

\[
\sum_{\text{ordered distinct }\mathbf d}
\left|\sum_{\mathbf m}I_{(d_1m_1^2,\ldots,d_{12}m_{12}^2)}\right|
\]

allows cancellation among harmonic tuples sharing the same squarefree labels. Triangle inequality bounds this grouped quantity above by the ungrouped certificate; a lower bound for the latter does not transfer. Any such further harmonic grouping, and any additional cross-norm grouping, remain outside the result. The proof also makes no claim about a signed full integral or moment.

## 4. First doubtful or unproved step

There is no remaining unproved step in the conditional implication from the **supplied** coefficient and near-resonance inputs to this exact certificate bound. The source proofs of those inputs were not opened or independently audited; their logical sufficiency was the assigned question.

The delicate step is the deletion of tuples with another short sign relation. It is justified by the explicit rank-two inversion and individual square-root spacing in (3)--(5), not by an unprovided separation estimate for twelve-term radical sums. The fixed choice of \(H\) is essential to the displayed large-\(T\) spacing argument.

The first unjustified downstream step would be moving the modulus outside a harmonic or cross-norm sum while preserving this lower bound. No sign control of the discarded or outside-shell tuples has been proved.

## 5. Required control test and outcome

These are exact analytical controls; no finite numerical test is used to certify the asymptotic statement.

1. **Balanced phase control:** for six plus and six minus entries, \(\sum_j\sigma_j=0\), so the multiplier in (9) is exactly \(1\). The opposite sign has the same multiplier and the conjugate Fourier argument. Outcome: the main pair is \(2\operatorname{Re}\widehat w\), with the positive sign required in (10).
2. **Rank-degeneracy control:** if \(\tau=\pm\sigma^0\), every two-column determinant vanishes. These two signs must not be included in the deletion argument; they are precisely the pair retained for the main term. For every other \(\tau\), both values of \(\tau_j/\sigma_j^0\) occur, giving a determinant \(\pm2\). Outcome: all and only the needed sign vectors receive the rank-two estimate.
3. **Scale control:** two short relations constrain a square root to length \((\delta+H)/T\), whereas one integer step changes it by order \(T^{-1/2}\). Their ratio tends to zero for fixed \(H\). Outcome: the claimed at-most-one completion is valid for all sufficiently large real \(T\), including noninteger \(T\) and shell-boundary changes.
4. **Weight/exponent control:** the deletion bound is \(b_T^2M_T^{10}\), not an unweighted count. At \(\varepsilon=1/8\), its exponent is \(-3/2+1/4+10/4=5/4<3/2\). Outcome: the deletion is negligible relative to the supplied mass, uniformly over the finite 4094 sign choices.
5. **Concentrated-atom control:** for one available atom of weight \(b\), two relations can hold identically and the upper bound \(b^2M^{10}=b^{12}\) need not be small. Outcome: the proof does not silently infer negligible multiple resonance from algebra alone; the supplied coefficient-size and mass exponents are necessary for that inference.
6. **Fourier-tail/sign-pooling control:** the proof bounds the sum of all 4094 other Fourier terms by \(4094\sup_{|\xi|>H}|\widehat w(\xi)|\le W/2\). It makes no assumption that those terms are positive or independently random. Outcome: the order of pooling and modulus exactly matches the requested certificate.
7. **Further-grouping control:** two fixed-norm contributions \(x\) and \(-x\) contribute \(2|x|\) to the present certificate and zero after grouping them. This is a structural triangle-inequality control, not an assertion that a particular pair occurs in the arithmetic problem. Outcome: neither harmonic grouping nor a fully signed sum inherits the proved lower bound.

No special \(\chi_4\) cancellation mechanism is used or claimed. The result is a lower bound for a nonnegative certificate derived from its supplied local mass inputs, so it does not purport to prove the false unsigned/adversarial analogue of a signed analytic upper bound.

## 6. Dependencies and exact artifacts used

The exact read set for this new interface is:

- `protocol.md`.
- `strategy/round231_admission/briefs/blind_cosine_packet_statement.md`.

The preceding unrelated prime task is disclosed in the metadata for isolation transparency; its mathematics and report were not used. The graph hash is a previously supplied provenance tag only. No discovery report, sibling review, history, graph content, source search, or conductor computation was read.

The mathematical dependencies are exactly the four accepted inputs listed in Section 2, finite cosine expansion, Fourier conjugacy for real functions, integration by parts for a compactly supported smooth function, inversion of a two-by-two matrix, elementary individual square-root spacing, a finite union bound, and sums of nonnegative product weights.

The generated-time query and subsequent SHA256 hashing supply provenance only. The sole written artifact for this task is this report; the previous prime report and all shared state remain unchanged.

## 7. Recommended state effect

**Retain** the precise fixed-norm, sign-pooled certificate lower bound as established conditional on the supplied accepted inputs. Its scope includes summing all 4096 cosine signs before each norm-tuple modulus.

**Reject** an extension of this proof to modulus after harmonic grouping, cross-norm grouping, or the fully signed sum without a new argument. **No change** is recommended to any analytic target or signed moment obligation on the strength of this result alone.

This independent review supplies evidence for the conductor's admission decision. It does not apply a State Patch, promote a graph claim, or design a successor round.
