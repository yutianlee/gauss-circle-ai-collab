# Round216: independent actual radical binding review

## 1. Result

Campaign: gc-actual-radical-high-values.
Role: explicitly NONBLIND final actual-binding seam, following two
separately frozen statement-only derivations. Generated: 2026-09-28.

**GREEN**, within the accepted dependencies and the scope stated below.
This review binds these exact claimant artifacts:

* controls/conductor_radical_ledger.md, SHA256
  **5d7e3daaecfb20771d5a4adc79cf07717d0805a32f2a29ca673671af3a550f72**.
* candidates/complete_distinct_radical_reduction.md, SHA256
  **d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee**.

The actual head bound, masked finite distribution, complete head
moment, actual tail's window supremum and lower moments, collective
distinct-class error, and complete target equivalence are valid.
The candidate's estimates are consistent with the frozen isolated
algebraic derivation:

\[
 M_{12}(L_Q)\ll_\varepsilon T^{15/13+\varepsilon},
 \qquad
 \int w(R/T)|Z_Q^{12}-E_{12}|\,dR
 \ll_\varepsilon T^{8\beta-1/5+\varepsilon}.                         \tag{1}
\]

Separately, the ledger's ratio-spacing argument proves that its actual
three-class near-relation family survives the cutoff. Its positive
absolute twelve-frequency certificate does have size at least
\(cT^{5/2}\). These are valid controls with limited scope; neither is
a lower bound for the complete signed moment or an estimate for the
remaining distinct-class integral.

Two notation/scope qualifications are essential and are satisfied by
the underlying proofs:

1. The \(T^{\beta+\varepsilon}\) supremum for \(Z_Q\) is on the
   radius window \([T/2,2T]\), not on the whole real line.
2. Removing exact terms from a positive absolute certificate uses
   the **absolute** exact-resonance bound immediately preceding
   ledger (10). It is not justified by the signed quantity
   \(D_{12}\) alone.

No RED mathematical defect was found in the assigned claims under
these explicit readings. No parent target or unproved distinct-class
estimate is certified.

## 2. Exact statements, hypotheses, and review boundary

Use the claimants' fixed nonnegative real radial mollifier \(\rho\),
of mass one and supported in the unit disk, and
\(\Psi(s)=\widehat\rho(se_1)\), with Fourier convention \(e(-x\cdot\xi)\).
Thus \(\Psi\) is real, even, Schwartz, \(|\Psi|\le1\), and
\(\Psi(0)=1\). The fixed nonnegative smooth \(w\) is supported in
\([1/2,2]\), and equals one on \([1/\sqrt2,\sqrt3]\).
For real \(T\ge2\), retain the complete series

\[
 a_n(T)=r_2(n)n^{-3/4}\Psi(\sqrt{n/T}),\qquad
 B_T(R)=\sum_{n\ge1}a_n(T)\cos(2\pi R\sqrt n-3\pi/4).
\]

Let \(Q=\lfloor T^{2/5}\rfloor\), \(V_0=T^{13/125}\), and decompose
\(n=ds^2\) with \(d\) squarefree. Define \(f_d,L_Q,Z_Q,E_{12}\) and
\(I_{12}=\int w(R/T)E_{12}\,dR\) exactly as in the candidate.
Every \(s\ge1\), ordered class tuple, and cosine sign is retained.

The actual pointwise input is only the qualified accepted application
in the supplied complete large-values kernel. In its notation,
\(\beta=2\theta_{\rm LY}-1/2\); its recorded interval
\[
 \frac5{16}<\theta_{\rm LY}<\frac{131}{416}
 \quad\Longrightarrow\quad
 \frac18<\beta<\frac{27}{208}<\frac{13}{100}
                                                                    \tag{2}
\]
is sufficient for every comparison here. This review does not
re-audit or strengthen the underlying external source theorem.

The current verdict concerns the two exact claimant hashes above.
It uses the two explicitly allowed accepted kernels as dependencies,
not the claim graph or any unallowed sibling report.

## 3. Proof audit and actual binding

### 3.1. Prime factors, all square factors, and the actual head

From the accepted identity \(r_2=4(1*\chi_4)\), the local factor for a
prime \(p\equiv1\pmod4\) with exponent \(k\) is \(k+1\); a prime
\(p\equiv3\pmod4\) with odd exponent makes the representation count
zero; powers of two do not change it.

If a squarefree \(d\) contains a prime \(3\bmod4\), both
\(r_2(d)\) and \(r_2(ds^2)\) vanish. Otherwise, for a prime
\(1\bmod4\) dividing \(d\), its factor in \(ds^2\) is \(2e+2\),
bounded by \(2(2e+1)\); for such a prime not dividing \(d\), the
factor is \(2e+1\). The remaining primes only enlarge \(\tau(s^2)\)
relative to this comparison. The global initial factor four occurs
once on both sides. Therefore, also for \(d=1\),

\[
 r_2(ds^2)\le r_2(d)\tau(s^2),\qquad
 A_d(T):=\sum_{s\ge1}|a_{ds^2}(T)|
 \le\zeta(3/2)^3r_2(d)d^{-3/4}.                                   \tag{3}
\]

The last inequality uses \(\tau(s^2)\le\tau_3(s)\), whose
Dirichlet series at \(3/2\) is \(\zeta(3/2)^3\). No \(s\)-cutoff
has been inserted.

The unit-square disk comparison supplies
\(\sum_{n\le x}r_2(n)\ll x\) for \(x\ge1\). Partial summation gives
\[
 \sum_{d\le Q}r_2(d)d^{-3/4}\ll Q^{1/4},
 \qquad
 \sup_{R\in\mathbb R}|L_Q(R)|\ll Q^{1/4}\ll T^{1/10}.                \tag{4}
\]
Dropping the squarefree restriction only increases the positive sum.
This is the actual arithmetic improvement over the logarithmic
generic-envelope head bound in my original isolated report.

For \(h=2,\ldots,12\), use \(r_2(d)\le4\tau(d)\ll_\delta d^\delta\)
in (3). Choose
\[
 0<\delta<
 \min\left\{\eta/h,\ (3h/4-1)/h\right\}.
\]
Then the summed exponent is strictly less than \(-1\), and
\[
 \sum_{d>Q}A_d(T)^h\ll_\eta Q^{1-3h/4+\eta}.                       \tag{5}
\]
The displayed choice makes explicit the small-input-exponent
requirement in candidate (D7), even if the requested output \(\eta\)
is large. Schwartz decay also gives \(\sum_dA_d(T)<\infty\) for each
fixed \(T\). Verdict for this seam: GREEN.

### 3.2. Masked distribution: finite proof, not a statement extension

The accepted final distribution is worded for lower cutoffs. The
claimants correctly return to its finite coefficient mechanism for
the squarefree masks.

At fixed \(T\), either mask is independent of \(R\). Truncation at
\(N_{\max}=T^{3/2}\) has an absolute remainder \(O_A(T^{-A})\),
uniformly after either mask: for a fixed decay order \(L\), the
unmasked tail is bounded by
\[
 T^{L/2}N_{\max}^{\,1/4+\delta-L/2}
 =T^{3/8+3\delta/2-L/4},
\]
and \(L\) may be increased according to \(A\).

On each full ambient block \(N<n\le2N\), use coefficient zero at
every inactive or truncated index. The energy remains
\[
 \sum|a_n|^2\ll_\delta N^{-1/2+2\delta}
 \ll_\delta T^{3\delta}N^{-1/2}.
                                                                    \tag{6}
\]
In the finite Cauchy--Schwarz/Gram argument, retaining the entire
ambient vector space produces the same complete unweighted
correlation kernel \(K_N(u)\), regardless of which coefficients are
zero. The accepted estimate
\[
 |K_N(u)|\ll_\eta T^\eta\sqrt N
                  (|u|^{13/55}+|u|^{-1})
\]
therefore applies unchanged. This is not a weighted exponent-pair
claim.

The finite proof retains the Gram diagonal, uses
\(\delta_N=N^{-1/2}\)-separated level points, and covers by the full
number \(O(1+T/h)\) of local intervals. Its level estimate is valid
for every positive level, including the levels below one introduced
by recombination. Partial boundary blocks are zero-extended, and the
singleton \(\{1\}\) has diagonal one and kernel \(e(u)\); it obeys the
same bound after a fixed change of constant.

There are \(O(\log T)\) blocks. Since a cosine block is
\(\operatorname{Re}(e(-3/8)S(R))\), its large-value event is contained
in the corresponding complex block event. A union at level
\(V/(C\log T)\), with the uniformly small remainder, gives for
\(F=L_Q,Z_Q\), \(V\ge1\),
\[
 D_F(V):=\int w(R/T){\bf1}_{|F|>V}\,dR
 \ll_\varepsilon T^\varepsilon
       \left(V^{-2}+T V^{-136/13}\right).                           \tag{7}
\]
The exponent is \(2+2/(13/55)=136/13\). Every power of the small
input loss and every fixed logarithmic power can be allocated within
the requested \(\varepsilon\). Bounded \(T\) is covered by the
uniform Schwartz absolute bound on that compact range. Verdict:
GREEN, with no unproved extension of a lower-cutoff theorem.

### 3.3. Complete head moment and actual lower moments

Let \(q=136/13\). For the head, layer cake, the \(O(T)\) measure
below level one, and the ceiling \(W_L\ll Q^{1/4}\) give
\[
 \begin{aligned}
 M_{12}(L_Q)
 &\ll_\varepsilon
 T^\varepsilon\left[T+W_L^{10}+T W_L^{12-q}\right]\\
 &\ll_\varepsilon
 T^\varepsilon\left[T+Q^{5/2}+TQ^{5/13}\right]
 \ll_\varepsilon T^{15/13+\varepsilon}.                            \tag{8}
 \end{aligned}
\]
Here \(12-q=20/13\), \(Q^{5/2}\le T\), and
\(TQ^{5/13}\le T^{1+2/13}\). The target margin is exactly
\[
 \frac{29}{25}-\frac{15}{13}=\frac2{325}>0.
\]
The fixed ceiling constant can be included by replacing \(W_L\)
with \(\max(1,CQ^{1/4})\); no small-\(Q\) case is omitted.

The accepted actual reconstruction supplies
\(\sup_{R\in[T/2,2T]}|B_T(R)|\ll_\varepsilon T^{\beta+\varepsilon}\).
Combining this with (4), and \(1/10<\beta\), proves
\[
 \sup_{R\in[T/2,2T]}|Z_Q(R)|
       \ll_\varepsilon T^{\beta+\varepsilon}.                     \tag{9}
\]
No assertion outside this window is required or validated.

For each integer \(2\le r\le10<q\), integrate (7) only to the
ceiling (9). The \(TV^{-q}\) integral is bounded after its factor
\(T\), while the \(V^{-2}\) integral contributes
\(W_Z^{r-2}\), or a logarithm at \(r=2\). Renaming the small losses
gives
\[
 M_r(Z_Q)\ll_\varepsilon T^\varepsilon
          \left[T+T^{(r-2)\beta}\right].                            \tag{10}
\]
For \(r=0\), use \(\int w(R/T)\,dR=O(T)\). For \(r=1\), weighted
Cauchy--Schwarz and \(r=2\) give \(O(T^{1+\varepsilon})\).
Thus every moment assumed by the isolated algebra packet is
actually supplied, including its endpoints \(r=0,1,2,10\).
Verdict: GREEN.

### 3.4. Binding to the frozen isolated collective derivation

Equations (3), (5), (9), and (10) verify precisely the abstract
envelopes and full-\(Z\) moment hypotheses of my frozen isolated
report. That report proves the ordered distinct-label identity
\[
 E_{12}=\sum_{\pi\in\Pi_{12}}\mu(\pi)
                   \prod_{C\in\pi}p_{|C|},\qquad
 \mu(\pi)=\prod_{C\in\pi}(-1)^{|C|-1}(|C|-1)!,
 \quad p_h=\sum_{d>Q}f_d^h.
\]
It coincides with candidate (D11), including all coefficients and
ordered-label multiplicities.

After removing the singleton partition, a profile has \(r\) singleton
blocks and \(b\) non-singleton blocks of total size \(12-r\), where
\[
 0\le r\le10,\qquad 1\le b\le\lfloor(12-r)/2\rfloor.
\]
Its complete two-term integrated exponent is
\[
 T^{\,1+2b/5-3(12-r)/10+\varepsilon}
 +T^{\,2b/5-3(12-r)/10+\max(r-2,0)\beta+\varepsilon}.
                                                                    \tag{11}
\]
This is candidate (D13)--(D14) in uncompressed form. For \(r\le9\),
the moment exponent is one and the largest resulting exponent is
\(3/5\), at \(r=8,b=2\). For \(r=10,b=1\), it is
\(8\beta-1/5>4/5\), the overall maximum. Hence (1) follows with the
same exponent as the isolated result.

Every infinite passage is legitimate at fixed \(T\), since
\(\sum_dA_d(T)<\infty\): finite class sums converge uniformly,
the ordered product sum is dominated by \((\sum_dA_d)^{12}\), and
the weight has finite integral. The moment hypothesis is applied
only to the full \(Z_Q\), after the finite identity is passed to the
limit. No moment estimate for arbitrary truncated subfamilies is
introduced. Verdict: GREEN.

### 3.5. Full moment, high event, and signed-integral equivalence

For the truncated low-value contribution, layer cake applied to
\(\min(|B_T|,V_0)^{12}\) gives the valid upper bound
\[
 \int_{|B_T|\le V_0}w(R/T)|B_T|^{12}\,dR
 \ll_\varepsilon T^\varepsilon
           [T+V_0^{10}+TV_0^{20/13}]
 \ll_\varepsilon T^{29/25+\varepsilon}.                            \tag{12}
\]
Here the two nontrivial powers are \(V_0^{10}=T^{26/25}\) and
\(TV_0^{20/13}=T^{29/25}\). The same argument applies to \(Z_Q\)
at any fixed multiple of \(V_0\), using (7).

The scalar inequality \(|x+y|^{12}\le2^{11}(|x|^{12}+|y|^{12})\),
applied to \(B_T=L_Q+Z_Q\) and \(Z_Q=B_T-L_Q\), together with (8),
proves equivalence of the full \(B_T\) and full \(Z_Q\) target
moments. Equation (12) proves equivalence of the high-\(B_T\)
target with its full moment. These are norm inequalities and pay
all mixed terms.

Also
\[
 \frac{\sup|L_Q|}{V_0}\ll T^{1/10-13/125}=T^{-1/250}.
\]
For sufficiently large \(T\), \(\sup|L_Q|\le V_0/2\), and on the
actual event \(|B_T|>V_0\),
\[
 |Z_Q|\ge|B_T|-|L_Q|>|B_T|/2>V_0/2.
\]
This proves the direct transfer with constant \(2^{12}\) and
threshold \(V_0/2\). The compact remaining \(T\)-range is absorbed
by the Schwartz absolute bound; it is not assigned this event
inclusion without the head condition.

Finally (1) gives
\[
 |M_{12}(Z_Q)-I_{12}(T)|
       \ll_\varepsilon T^{8\beta-1/5+\varepsilon},\qquad
 I_{12}(T)\ge-O_\varepsilon(T^{8\beta-1/5+\varepsilon}).             \tag{13}
\]
Because \(8\beta-1/5<21/25<29/25\), all four conditions in candidate
(D4) are equivalent with their stated every-\(\varepsilon\)
convention. A one-sided upper bound for \(I_{12}\) suffices by
(13); conversely a bound for the nonnegative moment yields an
absolute bound for \(I_{12}\). This does not require \(E_{12}\)
to be pointwise nonnegative. Verdict: GREEN.

### 3.6. Exact resonance, Fourier signs, and consistency with isolation

By (3), \(r_2(d)\le4\tau(d)\), and the elementary fourth-divisor
summation,
\[
 \sum_{d>Q}A_d^2\ll Q^{-1/2}\log(2Q)^3.
\]
The accepted all-sign exact kernel therefore bounds the **absolute**
exact coefficient by \(O(Q^{-3}\log(2Q)^{18})\).
Multiplying by \(T\widehat w(0)\) gives
\[
 T\widehat w(0)E_{12}^{\rm abs}
       \ll T^{-1/5}\log(2T)^{18}.                                 \tag{14}
\]
The signed exact coefficient is nonnegative for this even moment
and bounded by the same quantity, but it is a different quantity.

The convention
\(\widehat w(\xi)=\int w(u)e(-u\xi)\,du\) gives exactly
\[
 \int w(R/T)e(R\Delta)\,dR=T\widehat w(-T\Delta).
\]
Thus ledger (11) and candidate (D16) have the right factor \(T\),
sign in the Fourier argument, and cosine factor
\(2^{-12}e(-3\sum_j\epsilon_j/8)\). Their complete sums are real by
pairing opposite sign vectors, but individual terms need not be
real or positive.

In candidate (D16), every class occurs exactly once. The accepted
radical-independence lemma therefore rules out a zero frequency:
each independent class would otherwise have the nonzero coefficient
\(\epsilon_js_j\). It supplies no quantitative lower bound on its
nonzero frequencies.

The original isolated report's envelope-only obstruction remains
consistent with this reduction. It never supplied the actual
pointwise bound (9) or the lower moments (10). Nor did it identify
an absolute repeated-tuple estimate with the collective polynomial
error (1). The new argument uses exactly these additional inputs
and still leaves the distinct-class integral unestimated. Verdict:
GREEN.

## 4. First doubtful or unproved step

No missing step was found in the assigned head, mask, moment,
algebraic-binding, or equivalence claims. The first unproved step
for the target remains an adequate upper bound for the complete
signed distinct-class integral in candidate (D16).

The corresponding whole-tail nonzero kernel in ledger (11) is also
not estimated at target size merely by its exact-frequency bound.
The candidate pays its repeated-class part only after a collective
signed regrouping. The near-family and absolute-certificate controls
below do not disprove the possibility of such collective cancellation.

The accepted qualified pointwise input is a dependency, not a new
conclusion or a source theorem revalidated in this review.

## 5. Separate ledger controls and scope

### 5.1. Ratio spacing proves actual cutoff survival

For fixed \(a>0\), \(M\ge\sqrt a\), and fixed integer \(d\ge1\),
consider solutions \(m\in[M,2M]\cap\mathbb Z\), \(s\in\mathbb N\),
to \(m^2+a=ds^2\). Their ratios
\[
 \frac ms=\sqrt d\,(1+a/m^2)^{-1/2}
\]
are distinct: equality of two ratios and
\(s^2(d-(m/s)^2)=a>0\) would force the same positive \(s\), hence
the same \(m\).

The ratios lie in an interval of length at most
\(a\sqrt d/(2M^2)\), using the derivative bound \(1/2\) for
\((1+x)^{-1/2}\) on \(x\ge0\). Also
\[
 s\le\sqrt{4M^2+a}/\sqrt d\le3M/\sqrt d.
\]
The difference of two distinct rational ratios is consequently at
least \(1/(s_1s_2)\ge d/(9M^2)\). Their number is at most
\[
 1+\frac{9a}{2\sqrt d}.
\]
Summing over \(d\le Q\), even without the squarefree restriction,
proves the ledger's \(O_a(Q)\) exceptional count.

For the three fixed \(a=1,25,49\), a union bound remains \(O(Q)\).
With \(T=C_0M^2\) and \(Q=\lfloor T^{2/5}\rfloor\),
\(Q=O(M^{4/5})=o(M)\). Thus all but \(o(M)\) of the eligible
integer \(m\)'s retain all three actual indices after the cutoff.
No density theorem for squarefree values is being assumed.
Verdict: GREEN.

### 5.2. Distinct classes, actual nonzero coefficients, and balanced padding

Continuity and \(\Psi(0)=1\) give a fixed neighborhood of zero where
\(\Psi\ge1/2\). Choose \(C_0\) sufficiently large that, for all
large \(M\), \(m\in[M,2M]\), and \(a\in\{1,25,49\}\),
\[
 \sqrt{(m^2+a)/(C_0M^2)}
\]
lies in this neighborhood. Each index is \(m^2+k^2\) for
\(k=1,5,7\), so \(r_2\) is positive and each actual coefficient
is positive on this family.

If two retained indices shared their squarefree part \(d>Q\), their
difference, either \(24\) or \(48\), would equal
\[
 d(s_2^2-s_1^2)
 \ge2M\sqrt d,
\]
which tends to infinity. Thus the three retained classes are distinct.

Strict concavity gives a negative, nonzero difference, and the
Taylor coefficients verify
\[
 \Delta_m=\sqrt{m^2+1}+\sqrt{m^2+49}-2\sqrt{m^2+25}
 =-\frac{1+49^2-2\cdot25^2}{8m^3}+O(m^{-5})
 =-144m^{-3}+O(m^{-5}).
\]
Consequently \(T\Delta_m=O(M^{-1})\to0\), uniformly over the
retained \(m\)'s.

For an explicit padding choice, use four cancelling plus/minus pairs
all at \(n=m^2+25\). The resulting twelve entries have six plus and
six minus signs, phase \(e(0)=1\), and exactly the same three
occupied classes. Their three net class coefficients remain
\(+s_1,-2s_{25},+s_{49}\), so precisely three classes are active.
Every coefficient is actual and lies in \(Z_Q\).

This is a valid failure of frequency separation for the **whole**
large-class tail. It is not a twelve-distinct-class tuple in
candidate (D16). It therefore does not by itself obstruct the
candidate's remaining distinct-class target, and its presence does
not contradict the paid collective repeated-class error.
Verdict: GREEN at this limited scope.

### 5.3. The positive absolute certificate has order at least \(T^{5/2}\)

Choose small fixed \(c>0\) so that
\(\Psi(\sqrt{n/T})\ge1/2\) for \(cT\le n\le2cT\).
The same unit-square comparison gives
\[
 N(R)=\pi R^2+O(R+1),
\]
hence
\[
 \sum_{cT\le n\le2cT}r_2(n)\asymp T
\]
for all sufficiently large \(T\), with constants depending on \(c\).
Weights \(n^{-3/4}\) on the block are comparable to \(T^{-3/4}\).
Its positive coefficient mass is therefore \(\asymp T^{1/4}\).

The removed small-class mass on this block is at most the complete
absolute head mass in (4), \(O(Q^{1/4})=O(T^{1/10})\). Thus the
retained block \(\mathcal N\) has
\[
 \sum_{n\in\mathcal N}a_n(T)\ge c_1T^{1/4}.                         \tag{15}
\]

Place the product weight of every ordered six-tuple from
\(\mathcal N\) at its six-root sum. The total positive mass is
\((\sum_{\mathcal N}a_n)^6\gg T^{3/2}\), and its support has length
\(O(\sqrt T)\). Partition this support into bins of width
\(c_3/T\). There are \(O(T^{3/2})\) bins. If their masses are
\(\mu_j\), Cauchy--Schwarz gives
\[
 \sum_j\mu_j^2\ge
 \frac{(\sum_j\mu_j)^2}{\#\{\text{bins}\}}\gg T^{3/2}.                \tag{16}
\]

Choose \(c_3\) small enough that
\(|\widehat w(\xi)|\ge\widehat w(0)/2>0\) for \(|\xi|\le c_3\).
This follows by continuity, and does not assume \(w\) even.
Every pair of six-tuples in the same bin is a valid ordered
twelve-tuple for the fixed balanced sign pattern
\((+,+,+,+,+,+,-,-,-,-,-,-)\), and satisfies
\(|T\Delta|\le c_3\). The corresponding terms in the positive
absolute certificate sum to at least
\[
 \frac{T}{2^{12}}\frac{\widehat w(0)}2
       \sum_j\mu_j^2\gg T^{5/2}.                                  \tag{17}
\]
One balanced sign pattern already suffices; additional signs only
enlarge that certificate.

To remove the terms with \(\Delta=0\), use their **absolute**
upper bound (14), valid for all signs and all tail indices and thus
also for this block and sign pattern. Subtracting
\(O(T^{-1/5}\log(2T)^{18})\) from (17) preserves its \(T^{5/2}\)
lower order. This validates the ledger's reference to the bound
in (10); the signed \(D_{12}\) value alone would not justify that
subtraction.

This is a lower bound on the named **termwise absolute**
nonzero-frequency certificate, not on ledger \(R_{12}\),
\(M_{12}(Z_Q)\), the high-value gate, or \(I_{12}\). Its tuples
may repeat classes, so it is not automatically a lower bound for
the absolute version of candidate (D16) either. No such extension
has been asserted or used. Verdict: GREEN at the ledger's stated
whole-kernel absolute scope.

### 5.4. Other controls and scope checks

The arithmetic comparison includes \(d=1\), vanishing \(r_2(d)\),
and every square factor. The mask proof includes the singleton,
partial dyadic blocks, all large \(n\), levels below one after
recombination, and the full localization ceiling.
The finite algebra includes repeated labels, odd block sizes,
vanishing functions, equal functions, and fewer than twelve labels,
as already independently verified in the frozen isolated report.
No infinite-subfamily pointwise bound is used.

All floor comparisons are uniform for real \(T\ge2\). The high-event
inclusion is asserted only after its head condition holds, whereas
the moment equivalence includes bounded \(T\) through the absolute
Schwartz bound. Both cosine signs and the displaced Fourier kernel
remain explicit. No torus independence on a finite radius window
has been inferred.

All work in this seam was analytical or algebraic. No numerical
experiment, web lookup, or new external source expansion was used.

## 6. Dependencies and exact artifacts used

Current exact claimants, both read and hash-verified:

1. rounds/codex-managed/gc-actual-radical-high-values/controls/conductor_radical_ledger.md;
   SHA256 5d7e3daaecfb20771d5a4adc79cf07717d0805a32f2a29ca673671af3a550f72.
2. rounds/codex-managed/gc-actual-radical-high-values/candidates/complete_distinct_radical_reduction.md;
   SHA256 d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee.

Allowed accepted dependencies read:

3. proofs/kernels/gc_complete_square_root_large_values_moment_bound.md,
   especially its finite kernel, complete recombination, and qualified
   actual pointwise reconstruction.
4. proofs/kernels/gc_weighted_square_root_exact_resonance_mass.md,
   especially radical independence, all-sign absolute exact mass,
   and the exact cosine Fourier normalization.

Previously read isolated context and own frozen reports:

5. protocol.md.
6. rounds/codex-managed/gc-actual-radical-high-values/briefs/blind_radical_cutoff_statement.md.
7. rounds/codex-managed/gc-actual-radical-high-values/reports/blind_radical_cutoff.md,
   SHA256 e0accd624e0d9f1b95644c3456ed6302f9ac145aa6d4356aba4fb6cf82c7595e.
8. rounds/codex-managed/gc-actual-radical-high-values/briefs/isolated_distinct_class_statement.md.
9. rounds/codex-managed/gc-actual-radical-high-values/reviews/isolated_distinct_class_rederivation.md,
   SHA256 d5317e2a40bb394bd5eca45d57d1ebfe0d4c636fcf6a9b4a17e6f8314efc2256.

The new seam is explicitly NONBLIND. The two preceding reports remain
frozen and are not retroactively relabeled as reviews of these claimants.
No graph, strategy, manifest, unallowed sibling, discovery report, or
external source was read in this seam. Only this assigned review file
was written.

## 7. Recommended state effect and caveats

**GREEN** for the narrow actual-binding reduction:
the complete head estimate, the collectively paid repeated-class
error, and the equivalence of the specified target conditions.
**GREEN** separately for the ledger's actual three-class survival
control and its whole-kernel positive absolute-certificate lower
bound, with the scopes in Section 5.

Retain the accepted source qualifications. Interpret the actual tail
supremum on its stated radius window. Use absolute exact mass when
subtracting from absolute certificates. Do not transfer the
three-class or whole-kernel certificate controls to the twelve-distinct
target without a separate argument. Do not infer a lower bound for a
signed moment from a positive upper certificate.

The distinct-class integral is still unestimated. This review proves
no new pointwise exponent, high-value target, quarter theorem,
unbounded-moment family, or parent/endpoint obligation. Any graph
promotion is the conductor's responsibility after its prescribed
validation. No state change, predecessor edit, or successor work was
performed.
