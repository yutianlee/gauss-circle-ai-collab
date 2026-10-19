# Round235 — independent blind packet control

Campaign: gc-signed-sixth-dispersion  
Task: blind_packet_control  
Role/status: independent, statement-only blind rederiver; frozen evidence, not accepted mathematics  
Generated: 2026-10-12, Asia/Shanghai  
Graph hash: intentionally unavailable under the explicit isolation exception; no graph was read.  
Allocation: more than 90% analytical/algebraic work; no numerical experiment or external source search.

## 1. Result: progression lemma and tuple-absolute no-go theorem

The two full progressions have different cutoffs. With the Fourier convention in the isolated packet,
\[
 P_d(x,H)=\frac Hd\sum_{n\ge1}q(nH/d)\sin(2\pi nx/d),
\]
whereas
\[
 Q_d(x,H)=-\frac H{2d}
 \sum_{\substack{k\ge1\\k\ {\rm odd}}}
 \chi_4(k)q(kH/(4d))\cos(2\pi kx/(4d)).
\]
Thus the support-only vanishing conditions are respectively
\[
 d/H\le 1/b,\qquad d/H\le1/(4b).
\]
They include equality because the smooth zero extension of \(q\) vanishes at its support endpoints. Sharper exact thresholds replace \(b\) by \(B=\sup\operatorname{supp}q\).

For a fixed nonzero real kernel in the packet, constant \(H\ge1\), and an arbitrary interval \(I=[A,A+L]\), define
\[
 J_{\boldsymbol m}(I,H)=\int_I\prod_{i=1}^6K((x-m_i)/H)\,dx,\qquad
 {\cal A}(I,H)=\sum_{\boldsymbol m\in\mathbb Z^6}|J_{\boldsymbol m}(I,H)|.
\]
There are constants \(R_K,c_K,C_K>0\), depending only on the fixed kernel, such that
\[
 c_K LH^6\le {\cal A}(I,H)\le C_K LH^6
 \quad(H\ge1,\ L\ge4R_KH).
\]
In particular, the proposed uniform \(O_K(LH^3)\) tuple-absolute bound is false as \(H\to\infty\). The lower bound accounts explicitly for all negative contributions within each selected tuple integral and both endpoints of \(I\).

At the same time, when \(H\ge B\),
\[
 S(x)=\sum_{m\in\mathbb Z}K((x-m)/H)=0,\qquad
 \sum_{\boldsymbol m}J_{\boldsymbol m}(I,H)=\int_I S(x)^6\,dx=0.
\]
Positive clustered tuples and other, negative tuple integrals cancel in the signed total. The positive subcollection is used only to bound \({\cal A}\), never to bound that signed total from below.

## 2. Exact statements and hypotheses

Interpret the packet's \(q\) as a real \(C_c^\infty(\mathbb R)\) function supported in \([a,b]\subset(0,\infty)\), extended by zero outside that interval. Its sine transform \(K\) is real, odd, and Schwartz. For \(q\ne0\), \(K\ne0\). All progression identities hold for every real \(x\), every \(H>0\), and every positive integer \(d\); the same proofs would allow any positive real \(d\).

The transform is
\[
 \widehat K(\xi)=\frac{q(\xi)-q(-\xi)}{2i},
 \qquad
 \operatorname{supp}\widehat K
 \subset[-b,-a]\cup[a,b].
\]
In particular \(\widehat K(\xi)=-iq(\xi)/2\) for positive \(\xi\), and \(\int K=0\). In fact all polynomial moments of \(K\) vanish, because \(\widehat K\) vanishes on a neighborhood of zero.

For a given nonzero \(q\), the exact conditions for identical vanishing as functions of \(x\) are
\[
 P_d\equiv0\ \Longleftrightarrow\
 q(nH/d)=0\ \hbox{for every }n\ge1,
\]
\[
 Q_d\equiv0\ \Longleftrightarrow\
 q(kH/(4d))=0\ \hbox{for every positive odd }k.
\]
Consequently \(1/B\) and \(1/(4B)\), respectively, are the largest initial intervals of the ratio \(d/H\) on which identical vanishing holds for every smaller positive ratio. Particular ratios above these thresholds may still vanish because the sampling points miss the support or hit zeros.

The theorem for \({\cal A}\) uses constant \(H\), which already suffices to refute a proposed general bound that permits \(H\) to depend on \(x\). Tuples are ordered; repeated indices are allowed in the displayed definition. The lower bound also holds after restricting to six distinct indices, for all sufficiently large \(H\), as shown below.

## 3. Proof and derivation

### 3.1 Fourier formula and the ordinary progression

Writing the sine as two exponentials gives the displayed formula for \(\widehat K\). The compact smooth Fourier support gives \(K\in\mathcal S(\mathbb R)\), so Poisson summation and all progression sums are absolutely legitimate.

Poisson summation at spacing \(d\) yields
\[
 P_d(x,H)=\frac Hd\sum_{n\in\mathbb Z}
   \widehat K(nH/d)e(nx/d).
\]
The \(n=0\) term is zero. Pairing \(n\) and \(-n\) gives
\[
 \frac Hd\frac{q(nH/d)}{2i}
 \{e(nx/d)-e(-nx/d)\}
 =\frac Hdq(nH/d)\sin(2\pi nx/d).
\]
The nonzero frequencies as a function of \(x\) are \(n/d\) in the bands
\([-b/H,-a/H]\cup[a/H,b/H]\). These are finite Fourier sums.

If \(H/d\ge B\), all positive sample points are at or beyond \(B\), and \(q(B)=0\), proving the cutoff. Conversely, for every \(\epsilon>0\), the definition of \(B\) gives a point \(s<B\) arbitrarily close to \(B\) with \(q(s)\ne0\). Taking \(H/d=s\), the first sine coefficient is nonzero and \(d/H=1/s\) is arbitrarily close to \(1/B\) from above. Distinct Fourier frequencies cannot cancel identically. This proves the maximal-initial-interval assertion. If only the enclosing endpoint \(b\) is supplied, \(1/b\) is the largest such threshold valid uniformly over the allowed kernels.

### 3.2 The character progression: sign and the factor four

Split the progression into the residue classes \(1\) and \(3\) modulo four:
\[
 Q_d=\sum_{\ell\in\mathbb Z}K((x-d(4\ell+1))/H)
      -\sum_{\ell\in\mathbb Z}K((x-d(4\ell+3))/H).
\]
Poisson summation at spacing \(4d\) gives
\[
 Q_d=\frac H{4d}\sum_{k\in\mathbb Z}
 \widehat K(kH/(4d))e(kx/(4d))
 \{e(-k/4)-e(-3k/4)\}.
\]
The bracket equals \(-2i\chi_4(k)\) for every integer \(k\), including the even cases where both sides vanish. Therefore
\[
 Q_d=\frac H{2id}\sum_{k\in\mathbb Z}
 \chi_4(k)\widehat K(kH/(4d))e(kx/(4d)).
\]
Both \(\chi_4\) and \(\widehat K\) are odd. Pairing positive and negative \(k\), and using \(\widehat K(kH/(4d))=-iq(kH/(4d))/2\), yields
\[
 Q_d=-\frac H{2d}\sum_{\substack{k\ge1\\k\ {\rm odd}}}
 \chi_4(k)q(kH/(4d))\cos(2\pi kx/(4d)).
\]
In particular the overall sign is negative. The function \(Q_d\) is even in \(x\), has period \(4d\), and satisfies \(Q_d(x+2d,H)=-Q_d(x,H)\).

The smallest permitted positive frequency sample is \(H/(4d)\), not \(H/d\). The same support and first-coefficient argument as above gives the exact cutoff \(d/H\le1/(4B)\), and its maximality. Its \(x\)-frequencies are the odd multiples of \(1/(4d)\) that lie in the same two band intervals. This establishes both the distinct cutoff and the constants without importing any arithmetic context.

### 3.3 Uniform restoration of positive indices

Put
\[
 P_d^+=\sum_{j\ge1}K((x-dj)/H),\qquad
 Q_d^+=\sum_{j\ge1}\chi_4(j)K((x-dj)/H).
\]
For every real \(x\), the exact restoration identities are
\[
 P_d^+=P_d-\sum_{k\ge0}K((x+dk)/H),
\]
\[
 Q_d^+=Q_d+\sum_{k\ge1}\chi_4(k)K((x+dk)/H).
\]
The plus sign in the second identity follows from
\(\chi_4(-k)=-\chi_4(k)\); the \(j=0\) term there is zero.

For \(N>1\), choose
\(D_N=\sup_{u\in\mathbb R}(1+|u|)^N|K(u)|<\infty\).
For all \(x\ge0\), \(H,d>0\), a decreasing-integrand comparison gives
\[
 |P_d^+-P_d|\le D_N\left[
 (1+x/H)^{-N}
 +\frac{H}{d(N-1)}(1+x/H)^{1-N}\right],
\]
\[
 |Q_d^+-Q_d|\le
 \frac{D_NH}{d(N-1)}(1+x/H)^{1-N}.
\]
These estimates do not discard the negative indices or silently claim that their contribution is zero. In the intended range \(x\gg\max(H,d)\), they in particular give
\[
 P_d^+-P_d,\ Q_d^+-Q_d
 =O_{N,K}\left((H/x)^N+(H/d)(H/x)^{N-1}\right).
\]
The sharper displayed separate bounds should be retained when dependence on \(d/H\) matters. Merely saying that \(x/H\) is large without accounting for the factor \(H/d\) does not give an arbitrary uniform absolute error.

All these identities and bounds are pointwise for a positive \(H=H(x)\). For an explicit averaged consequence, if \(x\in[X,X+L]\), \(X\ge0\), \(H(x)\le H_+\), and \(d\) is fixed, the first bound is uniformly at most
\[
 E_N=D_N\left[(1+X/H_+)^{-N}
 +\frac{H_+}{d(N-1)}(1+X/H_+)^{1-N}\right].
\]
Thus its \(L^p\) integral is at most \(L E_N^p\) for \(p\ge1\); the second bound omits the first term. If the appropriate cutoff holds pointwise, the corresponding full progression term is identically zero pointwise. No averaged claim about a variable \(H\) is made without such uniform bounds.

### 3.4 Absolute convergence and the upper sixth-tuple bound

For \(H\ge1\), rapid decay gives uniformly in \(x\)
\[
 \sum_{m\in\mathbb Z}|K((x-m)/H)|\le C_K' H.
\]
For example, use \(D_2(1+|u|)^{-2}\) and divide the lattice points into shells \(jH\le |x-m|<(j+1)H\). Each shell has at most \(2H+2\le4H\) points, and sum \(4D_2H\sum_{j\ge0}(1+j)^{-2}\).

Tonelli and the triangle inequality then give
\[
 \sum_{\boldsymbol m}|J_{\boldsymbol m}|
 \le \int_I\sum_{\boldsymbol m}\prod_{i=1}^6|K((x-m_i)/H)|\,dx
 =\int_I\left(\sum_m|K((x-m)/H)|\right)^6dx
 \le (C_K')^6LH^6.
\]
This also proves absolute convergence of the series of integrals and justifies the signed expansion.

### 3.5 A positive complete correlation near the diagonal

Write
\[
 M=\int_{\mathbb R}K(u)^6\,du=\|K\|_6^6>0,
 \quad N_6=\|K\|_6,\quad D_6=\|K'\|_6>0.
\]
For offsets \(t_1=0\), define the complete correlation
\[
 F(t_2,\ldots,t_6)=\int_{\mathbb R}
 K(u)\prod_{i=2}^6K(u-t_i)\,du.
\]
By telescoping the product and applying Hölder,
\[
 |F(t_2,\ldots,t_6)-M|
 \le N_6^5\sum_{i=2}^6\|K(\cdot-t_i)-K\|_6
 \le N_6^5D_6\sum_{i=2}^6|t_i|.
\]
The last inequality follows by integrating \(K'\) and using Minkowski. Choose
\[
 \delta=\min\{1,N_6/(20D_6)\}>0.
\]
Then \(|t_i|\le\delta\) implies \(F(t_2,\ldots,t_6)\ge3M/4\). This is a bound on the integral over the whole real line; it already accounts for all negative parts of the product. Oddness does not obstruct it: at zero offsets the product is \(K(u)^6\), a nonnegative even function with positive integral.

### 3.6 Both endpoint tails, then counting

Choose a fixed \(R_K\ge2\), large enough that
\[
 \int_{|u|\ge R_K}
 \sup_{\substack{|t_i|\le\delta\\2\le i\le6}}
 \left|K(u)\prod_{i=2}^6K(u-t_i)\right|du\le M/4.
\]
Such an \(R_K\) exists by the Schwartz bounds. Explicitly, for \(|u|\ge2\) and \(\delta\le1\), each factor is bounded by
\(4D_2(1+|u|)^{-2}\); it suffices to choose \(R_K\ge2\) with
\[
 \frac{2\cdot4^6D_2^6}{11}(1+R_K)^{-11}\le M/4.
\]

Select an integer
\[
 m_1\in[A+R_KH,A+L-R_KH],
\]
and for \(i=2,\ldots,6\) select
\(m_i=m_1+r_i\) with integer \(0\le r_i\le\delta H\).
Make the change of variable \(u=(x-m_1)/H\).
The omitted complement of the resulting \(u\)-interval lies entirely in \(|u|\ge R_K\). Thus, regardless of the signs of its product,
\[
 J_{\boldsymbol m}/H
 \ge F(r_2/H,\ldots,r_6/H)-M/4\ge M/2.
\]
This step controls both endpoint losses by their absolute values. It does not infer positivity of the complete integral from positivity on a selected subinterval.

If \(H\ge1\) and \(L\ge4R_KH\), there are at least \(L/4\) choices for \(m_1\), since their number is at least \(L-2R_KH-1\). There are at least \(\delta H\) choices for each \(r_i\), because \(\lfloor\delta H\rfloor+1\ge\delta H\). Therefore
\[
 {\cal A}(I,H)\ge
 \frac L4(\delta H)^5\frac {MH}2
 =\frac{M\delta^5}{8}LH^6.
\]
All selected \(m_i\) lie in \(I\), since \(\delta\le1<R_K\).

For six distinct indices, instead use distinct positive \(r_2,\ldots,r_6\) from \(1,\ldots,\lfloor\delta H\rfloor\). For sufficiently large \(H\), their falling-factorial count is at least \((\delta H/4)^5\). The same complete-correlation and endpoint proof applies. Thus repeated indices are not the source of the obstruction.

Taking, for example, \(H\to\infty\) and \(L=H^2\) proves failure of a uniform \(O_K(LH^3)\) bound by a factor at least a constant times \(H^3\).

### 3.7 Signed cancellation, including the necessary negative mass

For \(H\ge B\), the ordinary progression formula with \(d=1\) gives \(S(x)=0\). By the absolute convergence established in 3.4,
\[
 \sum_{\boldsymbol m}J_{\boldsymbol m}
 =\int_I S(x)^6\,dx=0.
\]
Let \(T_+\) be the sum of positive \(J_{\boldsymbol m}\), and let \(T_-\) be the sum of the absolute values of negative \(J_{\boldsymbol m}\). Both are finite, and the identity says
\[
 T_+=T_-,\qquad {\cal A}=T_++T_-=2T_+.
\]
The selected clustered tuples force \(T_+\gg_K LH^6\); necessarily there is equally large negative mass elsewhere. Consequently the exactly vanishing signed sum and the large tuple-absolute sum are fully consistent. No assertion that a positive subcollection lower-bounds the signed total is used.

## 4. First doubtful or unproved step

There is no remaining gap in the isolated progression identities, the stated positive-index tail estimates, or the tuple-absolute lower and upper bounds, under the explicit smooth zero-extension convention for \(q\).

The first invalid step of a proposed Gaussian-order absolute argument would be the inference that zero mean or oddness can control
\(\sum_{\boldsymbol m}|J_{\boldsymbol m}|\) by \(O(LH^3)\). The complete near-diagonal correlation proves the opposite order of magnitude. This remains true here even though every polynomial moment of \(K\) is zero and the full signed sum vanishes exactly.

Using the ordinary progression cutoff for the character progression would be a separate invalid step: the character introduces quarter-lattice frequencies.

No conclusion about an unspecified arithmetic application is available or claimed.

## 5. Required controls and outcomes

1. **Fourier normalization/sign control — analytical PASS.** The ordinary \(n,-n\) pair gives \(+(H/d)q(nH/d)\sin(2\pi nx/d)\). The residue-class factor is exactly \(-2i\chi_4(k)\); its combination with \(\widehat K=-iq/2\) gives the negative cosine coefficient \(-H/(2d)\).

2. **Parity/frequency control — analytical PASS.** \(P_d\) is odd in \(x\), whereas \(Q_d\) is even and anti-periodic under \(x\mapsto x+2d\). Their explicit Fourier formulas have precisely these symmetries.

3. **Distinct-cutoff control — analytical PASS.** A nonzero sample \(q(H/(4d))\) already produces a character frequency at \(1/(4d)\), although the ordinary progression may have no nonzero sample. For a concrete symbolic construction, choose \(s_0\in(a,b)\) with \(4s_0>b\), take a nonnegative smooth bump supported sufficiently close to \(s_0\), and set \(H/d=4s_0\). Then \(P_d=0\), but \(Q_d=-(H/(2d))q(s_0)\cos(2\pi x/(4d))\ne0\); narrow the bump to exclude the other odd sample points. Such an \(s_0\) always exists close enough to \(b\). This also detects a factor-four cutoff error.

4. **Endpoint and negative-contribution control — analytical PASS.** The correlation is bounded on the whole line first. Both omitted endpoint tails are then bounded in absolute value by \(MH/4\). No positivity outside a chosen center region is assumed.

5. **Repeated-index control — analytical PASS.** The same lower bound order is available with six distinct nearby indices.

6. **Signed-versus-absolute control — analytical PASS.** For \(H\ge B\), the signed sum is zero, while its absolute counterpart has order \(LH^6\). Its total positive and negative masses are equal. This explicitly addresses the cancellation that an absolute estimate destroys.

7. **Computational control — not performed by this isolated task.** The brief assigns shared exact computational checks to the conductor. The algebraic controls above are proved analytically. No assertion is made that an unseen computation passed, and no asymptotic theorem is certified by computation.

## 6. Dependencies and exact artifacts used

Only the following three files were read. SHA-256 hashes refer to their exact bytes, not a normalized transcription.

| Exact context path | SHA-256 |
|---|---|
| protocol.md | F26FB038496B5AE171B3352E7D02BA1A4B7DD808EF31BF8620E6D4930CEA9D5A |
| rounds/codex-managed/gc-signed-sixth-dispersion/briefs/blind_packet_control.md | A18510A02B9C429C8DC480114CF2C31E14BF65BBA34B654A0293E9A69E6E3014 |
| rounds/codex-managed/gc-signed-sixth-dispersion/briefs/isolated_packet.md | 15C40F1605EFC87EB8BB3807ACB5B6BF066A6EBCF1A95F58269FFFF95B2E2905 |

The mathematical tools are Fourier inversion/Poisson summation for Schwartz functions, the finite Fourier transform of \(\chi_4\), Hölder, Minkowski, Tonelli, and elementary integer counting. No outside source or research theorem was imported. No application, graph, manifest, sibling report, historical report, or proof draft was read. No claim graph identifier has been inferred.

## 7. Recommended state effect and freeze

- **Retain as independently derived candidate evidence** the progression/filter lemma with the distinct cutoffs and the positive-index restoration bounds.
- **Reject** the tuple-absolute \(O(LH^3)\) inference from oddness, zero integral, or band limitation alone. Record the proved \(LH^6\) obstruction if the conductor finds it relevant to the frozen campaign.
- **No automatic promotion or downstream application.** This report is statement-only evidence. Any graph promotion requires the conductor's remaining seam reviews, prescribed controls, and validated State Patch.

Frozen on completion. This task writes no authoritative state, starts no successor round, and stops after this report.
