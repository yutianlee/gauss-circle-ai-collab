# Round 211 independent two-stage correlation seam review

## 1. Result and review verdict

**GREEN for the final hash-bound ledger's conditional finite claims C1--C8 and its scoped certificate barrier.** Both Fejer costs, the raw-to-physical normalization, every four-point overlap, the smooth-main sum, and all displayed rational powers check. The arithmetic bounds C3 and C6 remain unproved.

Two precision repairs were requested immediately and are present in the final ledger:

1. The chosen integer cutoffs satisfy the initial upper constraint only for sufficiently large \(T\), uniformly over the open band. The bounded \(T\)-range is now explicitly paid trivially.
2. The full-quarter limitation now concerns a fixed-\(b\) instance of C3/C6 and the proposed square-root oscillatory input. It no longer excludes a sufficiently strong single uniform four-point theorem.

The newly explicit centered-envelope variation lower bound also checks, solely as a lower bound on the stated positive error certificate.

- Campaign: gc-full-source-method-review; round: 211.
- Role: independent **NONBLIND** seam review, assigned after completion of the separate statement-only hyperbola task.
- Generated: 2026-09-28.
- Inherited graph hash as stated in the ledger: 4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71. The graph itself was not accessed.
- Effort: entirely analytical; no mathematical numerical experiment or new external theorem.
- Primary artifact: rounds/codex-managed/gc-full-source-method-review/controls/conductor_two_stage_strategy.md.
- Final SHA-256: **9bf8f30d240304f88c46a5a93c7d93586b3ade1c674d5a5fdbc61a251fcd176f**.

The earlier isolated report is preserved unchanged. It is neither a dependency of this review nor a claimed blind review of the present ledger.

## 2. Exact hypotheses and review boundary

Fix \(0<b<1/6\), \(T\ge2\), \(R\asymp T>0\), and
\[
 T^{4b}<N<T^{1-2b}.
 \tag{R1}
\]
All constants may depend on fixed \(b\), the fixed positive comparison window, the masks, and the fixed small \(\delta>0\). The raw and physical sums are
\[
 g_N(t)=(t/N)^{-3/4}\Psi(\sqrt{t/T})v(t/N),\qquad
 s_n=c_ng_N(n)e(R\sqrt n),\qquad
 S=\sum_ns_n,\quad F_c=N^{-3/4}S.
 \tag{R2}
\]
The coefficients are real, \(c_n=r_2(n)\) or \(r_2(n)-\pi\), with their actual divisor envelope; the masks are real and smooth. Every sequence is zero extended. In particular, \(g_N\) has size one and contains no additional physical \(N^{-3/4}\) factor. Its support is contained in
\[
 [\,\lceil N\rceil,\lfloor4N\rfloor\,]\cap\mathbb Z,
\]
an ambient interval of length at most \(3N+1\).

For integer \(2\le L,K\le\delta N\), the complete correlations are
\[
 C_h=\sum_ns_{n+h}\overline{s_n},\qquad
 D_{h,k}=\sum_ns_{n+h+k}\overline{s_{n+k}}\,
                           \overline{s_{n+h}}s_n,
\]
\[
 \mathcal A_4=\frac1{LK}\sum_{h=1}^{L-1}\sum_{k=1}^{K-1}|D_{h,k}|.
 \tag{R3}
\]
A nonzero main-term family \(\rho_{h,k}\), its bound \(|\rho_{h,k}|\ll T^\epsilon\), and any small unweighted or oscillatory remainder are additional hypotheses, not established inputs. Setting \(\rho=0\) leaves the complete \(D\) as the remainder.

The allowed closed208 bridge and complements are used only in their supplied concrete-\(b\) scope. The allowed closed210 context supplies the earlier positive-certificate comparison and reviewed centered mean-wave restoration. This review does not independently audit external sources underlying those inherited statements or inspect any unlisted file.

## 3. Independent derivation and seam checks

### A. The two finite Fejer inequalities

For a finite sequence \(z_n\) in an ambient integer interval of length \(M\), let \(B_m=\sum_{j=0}^{L-1}z_{m+j}\). Every \(z_n\) occurs exactly \(L\) times in \(\sum_mB_m\), and at most \(M+L-1\) starting indices contribute. Thus
\[
 \left|\sum_nz_n\right|^2
 \le\frac{M+L-1}{L^2}\sum_m|B_m|^2,
 \tag{R4}
\]
while exact expansion gives
\[
 \sum_m|B_m|^2
 =L\sum_n|z_n|^2+
 2\Re\sum_{h=1}^{L-1}(L-h)\sum_nz_{n+h}\overline{z_n}.
 \tag{R5}
\]
Apply this to \(s_n\). Its diagonal is \(O(NT^\epsilon)\), uniformly in \(R\), and \(M+L-1=O(N)\). Taking moduli and bounding the Fejer weights by one gives
\[
 |S|^2\ll N^2T^\epsilon/L+(N/L)\sum_{h<L}|C_h|.
\]
Squaring and applying Cauchy to the finite \(h\)-sum gives
\[
 |S|^4\ll N^4T^\epsilon/L^2+(N^2/L)\sum_{h<L}|C_h|^2.
 \tag{R6}
\]
For each \(h\), apply (R4)--(R5), now with length \(K\), to \(t_n=s_{n+h}\overline{s_n}\). Its squared-coefficient diagonal is
\[
 \sum_n|t_n|^2=\sum_n|s_{n+h}|^2|s_n|^2\ll NT^\epsilon,
\]
and its \(k\)-correlation is exactly \(D_{h,k}\). Therefore
\[
 |C_h|^2\ll N^2T^\epsilon/K+(N/K)\sum_{k<K}|D_{h,k}|.
 \tag{R7}
\]
Substituting (R7) in (R6) yields
\[
 |S|^4\ll T^\epsilon(N^4/L^2+N^4/K)
                  +\frac{N^3}{LK}\sum_{h<L,k<K}|D_{h,k}|.
\]
Division by \(N^3\), since \(|F_c|^4=N^{-3}|S|^4\), proves exactly
\[
 |F_c|^4\ll T^\epsilon[N/L^2+N/K+\mathcal A_4].
 \tag{R8}
\]
This checks C1, including the second diagonal \(N/K\). There is no missing \(h\ge L\) or \(k\ge K\) contribution: the full moving-sum factors in (R4) pay the passage to these finite correlations. No cancellation of a separated diagonal is assumed.

### B. Exact integers throughout the open band

Put \(L_0=N^{1/2}T^{-2b}\), \(K_0=NT^{-4b}=L_0^2\). The lower endpoint in (R1) is strict, so both exceed one. Hence C2 gives exact integers satisfying
\[
 L_0\le L=\max(2,\lceil L_0\rceil)\le2L_0,\qquad
 K_0\le K=\max(2,\lceil K_0\rceil)\le2K_0,
\]
\[
 LK\asymp N^{3/2}T^{-6b},\qquad
 L/N\le2N^{-1/2}T^{-2b}<2T^{-4b},\quad K/N\le2T^{-4b}.
 \tag{R9}
\]
These statements remain uniform as \(N/T^{4b}\downarrow1\), when either cutoff may stay equal to two. No uniform divergence of the cutoffs is required.

For \(T\ge T_0(b,\delta)\), (R9) ensures \(L,K\le\delta N\). For bounded \(2\le T<T_0\), the complete finite sum is bounded trivially with an enlarged constant. This is the first repaired qualification in the final ledger.

The two diagonal costs obey
\[
 N/L^2\le T^{4b},\qquad N/K\le T^{4b}.
\]
Consequently C3, for every required \(N\), every required \(R\), and exactly these integers, gives \(|F_c|\ll T^{b+\epsilon}\). The fourth root merely requires independently smaller epsilon budgets.

### C. Four-point overlaps and the repeated-shift control

For positive \(h,k\), the exact ambient \(n\)-overlap of all four factors is
\[
 [\,\lceil N\rceil,\lfloor4N-h-k\rfloor\,]\cap\mathbb Z.
 \tag{R10}
\]
Zeros of the smooth masks inside this interval remain present. With
\[
\begin{split}
 a_{h,k}(n)&=c_nc_{n+h}c_{n+k}c_{n+h+k},\\
 W_{h,k}(t)&=g_N(t)g_N(t+h)g_N(t+k)g_N(t+h+k),\\
 \phi_{h,k}(t)&=R[\sqrt{t+h+k}-\sqrt{t+k}-\sqrt{t+h}+\sqrt t],
\end{split}
\]
the identity \(D_{h,k}=\sum_na_{h,k}(n)W_{h,k}(n)e(\phi_{h,k}(n))\) is exact. It uses the reality of the coefficients and masks and all four conjugations in (R3).

When \(h=k\),
\[
 a_{h,h}(n)=c_nc_{n+h}^{\,2}c_{n+2h},\quad
 W_{h,h}(t)=g_N(t)g_N(t+h)^2g_N(t+2h).
\]
The phase is \(R(\sqrt{t+2h}-2\sqrt{t+h}+\sqrt t)\). This case is retained, is not a zero-phase diagonal, and does not force \(D_{h,h}\) to be positive. For \(h\ne k\), both ordered shift pairs are retained with their natural multiplicity. The zero-shift terms, unlike \(h=k>0\), are the two diagonals already paid in (R8).

### D. The square-root third derivative and every small-product main term

For \(f(t)=\sqrt t\), \(f'''(t)=3t^{-5/2}/8\). Thus the exact finite-difference formula is
\[
 \phi_{h,k}'(t)
 =R\int_0^h\int_0^k f'''(t+u+v)\,dv\,du
 =\frac{3R}{8}\int_0^h\int_0^k(t+u+v)^{-5/2}\,dv\,du.
 \tag{R11}
\]
It is positive and comparable to \(ThkN^{-5/2}\) on the entire overlap. For \(j\ge1\),
\[
 \phi_{h,k}^{(j)}(t)
 =R\int_0^h\int_0^k f^{(j+2)}(t+u+v)\,dv\,du,\qquad
 |\phi_{h,k}^{(j)}(t)|\ll_j ThkN^{-j-3/2}.
 \tag{R12}
\]
In particular the integrands for \(\phi''\) and \(\phi'''\) are respectively \(-15(t+u+v)^{-7/2}/16\) and \(105(t+u+v)^{-9/2}/32\).

The raw amplitude satisfies \(W_{h,k}^{(j)}=O_j(N^{-j})\), including its exterior smooth boundaries. Under \(t=Nu\), its derivatives are uniformly bounded on a compact support, while the phase parameter is
\[
 \Lambda=Thk/N^{3/2}.
\]
For \(\Lambda\ge1\), the normalized first derivative is bounded below and all normalized higher derivatives are bounded; repeated continuous integration by parts is uniform. For \(\Lambda\le1\), use the trivial \(O(N)\) integral bound. This proves C4:
\[
 I_{h,k}=\int_{\mathbb R}W_{h,k}(t)e(\phi_{h,k}(t))\,dt,\qquad
 |I_{h,k}|\ll_A N(1+\Lambda)^{-A}.
 \tag{R13}
\]
No discrete exponential-sum estimate is used.

Set \(c=T/N^{3/2}\). For \(A>1\), monotonicity yields
\[
 \sum_{k=1}^\infty(1+chk)^{-A}
 \le\int_0^\infty(1+cht)^{-A}\,dt
 =\frac1{(A-1)ch}.
\]
Therefore
\[
 \sum_{h=1}^{L-1}\sum_{k=1}^{K-1}(1+chk)^{-A}
 \ll c^{-1}\log(2L).
 \tag{R14}
\]
This pays every small product, including \(hk=1\), instead of discarding an exceptional sector. The infinite \(k\)-sum is merely an upper bound for the finite one.

Conditional on \(|\rho_{h,k}|\ll T^\epsilon\), (R9), (R13), and (R14) give
\[
 \frac1{LK}\sum_{h<L,k<K}|\rho_{h,k}I_{h,k}|
 \ll T^\epsilon\frac{N^{5/2}}{TLK}
 \ll T^\epsilon NT^{6b-1}\le T^{4b+\epsilon}.
 \tag{R15}
\]
The last inequality uses \(N\le T^{1-2b}\). This checks C5, including the harmonic logarithm and the entire rectangular shift set.

For \(\mathcal R_{h,k}=D_{h,k}-\rho_{h,k}I_{h,k}\), the triangle inequality and (R15) show that C6 implies C3. With the same \(\rho\) hypothesis, C3 also controls the averaged absolute remainder by adding back the paid main term. These are implications between still-unproved arithmetic bounds.

### E. Abel transport and the exact \(18/65,36/65,31/325\) powers

Suppose on the complete overlap, for real prefixes,
\[
 \sum_{N<n\le y}a_{h,k}(n)
  =\rho_{h,k}(y-N)+E_{h,k}(y),\qquad
 \sup_y|E_{h,k}(y)|\le\mathcal E_{h,k}.
 \tag{R16}
\]
All exterior weighted boundary values vanish. If \(N\) is itself an integer, its excluded atom has zero exterior mask value. Stieltjes partial summation gives
\[
 \mathcal R_{h,k}
   =-\int E_{h,k}(t)\,d\{W_{h,k}(t)e(\phi_{h,k}(t))\}.
\]
The amplitude derivative integrates to \(O(1)\); the phase part costs
\[
 \int|W_{h,k}\phi'_{h,k}|\,dt
 \ll N(ThkN^{-5/2})=Thk/N^{3/2}.
\]
Thus C7 is exactly
\[
 |\mathcal R_{h,k}|
 \ll\mathcal E_{h,k}(1+Thk/N^{3/2}).
 \tag{R17}
\]
There is no extra \(N^{-3/2}\) or \(N^{-3}\): \(W\) is the raw size-one four-factor product.

For a uniform envelope \(\mathcal E_*\), the exact finite identity
\[
 \frac1{LK}\sum_{h=1}^{L-1}\sum_{k=1}^{K-1}hk
 =\frac{(L-1)(K-1)}4\asymp LK,\qquad L,K\ge2,
 \tag{R18}
\]
and (R9) show that its positive upper certificate costs
\[
 \ll\mathcal E_*(1+TLK/N^{3/2})
 \asymp\mathcal E_*T^{1-6b}.
\]
Consequently C8,
\[
 \mathcal E_*\ll T^{10b-1+\epsilon},
 \tag{R19}
\]
is a sufficient condition for C6. This does not make it a necessary condition for an actual oscillatory bound.

For \(b=83/650\),
\[
 4b=166/325,\quad 1-2b=242/325,\quad 10b-1=18/65.
\]
An unweighted square-root envelope \(N^{1/2}\) meets (R19) at the power level only up to \(N=T^{36/65}\). Its upper-edge deficit is exactly
\[
 \frac12\cdot\frac{242}{325}-\frac{18}{65}
 =\frac{121-90}{325}=\frac{31}{325}.
 \tag{R20}
\]
Because the band is open, this is the supremal edge deficit; a fixed interior scale has its corresponding smaller deficit. These are costs of the upper certificate, not lower bounds for \(\mathcal R_{h,k}\).

A genuinely oscillatory hypothesis \(|\mathcal R_{h,k}(R)|\ll N^{1/2}T^\epsilon\) already includes the phase and incurs no Abel factor. It implies C6 throughout the band whenever
\[
 (1-2b)/2\le4b\quad\Longleftrightarrow\quad b\ge1/10.
 \tag{R21}
\]
An unweighted theorem, a fixed-shift theorem without the required uniformity, or a theorem excluding \(h=k\) is not this input.

### F. Centered atom floor and the positive-envelope barrier

For every positive integer, \(r_2(n)\in4\mathbb Z_{\ge0}\), hence
\[
 |r_2(n)-\pi|\ge4-\pi.
\]
Every centered four-point atom has modulus at least \((4-\pi)^4\), including repeated factors at \(h=k\). Subtracting any continuous main term cannot remove a jump. The supremum over real prefixes is therefore at least half an interior jump:
\[
 \mathcal E_{h,k}\ge(4-\pi)^4/2.
 \tag{R22}
\]
This is not a lower bound for the oscillatory remainder.

The new variation lower bound is valid. The inherited fixed nonzero mask has a compact sign-definite interior interval, and \(\Psi(0)=1\). Since \(N/T\le T^{-2b}\), shrinking fixed \(\delta\) if necessary gives a common four-factor interior overlap of length \(\asymp N\) and \(|W_{h,k}|\gg1\) for all chosen shifts, uniformly for large \(T\). The real amplitude identity
\[
 |(We(\phi))'|
 =\sqrt{(W')^2+4\pi^2W^2(\phi')^2}
 \ge2\pi|W\phi'|
\]
then gives actual variation \(\gg Thk/N^{3/2}=chk\) on that overlap.

Multiplying this variation by the atom floor (R22), and averaging over the whole rectangle using (R18), gives a lower cost
\[
 \gg cLK\asymp T^{1-6b}
 \tag{R23}
\]
for the specified supremum-times-absolute-variation certificate. Formula (R18) also covers bounded \(L\) or \(K\), in particular \(L=K=2\); no unjustified growing-cutoff assumption is needed. Equivalently one can take proportional shift subranges, retaining the single positive shift for bounded lengths.

At the concrete \(b>1/10\), a constant envelope is compatible with C8. At \(b=1/10\), compatibility holds at the power level. For fixed \(b<1/10\), (R23) exceeds the target \(T^{4b}\) by power \(1-10b\), so this positive closure fails. This is now established by its actual variation lower bound, not inferred from a merely sufficient upper condition. It does not obstruct signed error integrals, C3/C6 proved by another mechanism, or the quarter theorem.

### G. Positive-frequency projection and complete physical consequences

For real coefficients and masks,
\[
 H_N=\Re(e(-3/8)F_{r_2})
 =\tfrac12[e(-3/8)F_{r_2}+e(3/8)\overline{F_{r_2}}].
\]
Use the Fourier convention \(e(R\xi)\), so \(\chi(D/\sqrt N)\) has symbol \(\chi(\xi/\sqrt N)\). A smooth \(\chi\), supported in \((1/2,3)\) and one on \([1,2]\), keeps every positive frequency \(\sqrt n\) and annihilates every negative frequency. Exactly
\[
 F_{r_2}=2e(3/8)\chi(D/\sqrt N)H_N.
 \tag{R24}
\]
The kernel is \(\sqrt N\,\check\chi(\sqrt N u)\), with bounded \(L^1\) norm and Schwartz decay. For an inner positive window separated by \(\gg T\) from the complement of the larger supplied window, convolution gives
\[
 \sup_{\mathrm{inner}}|F_{r_2}|
 \ll\sup_{\mathrm{larger}}|H_N|
       +N^{1/4+\epsilon}(T\sqrt N)^{-A}.
 \tag{R25}
\]
The coefficient bound in the tail is global in \(R\). The larger-window bound and positive buffer must actually be available; an inner-window bound alone does not justify the reverse comparison. This is a smooth annular projection, not a Hilbert-transform \(L^\infty\) assertion.

The forward implication \(|H_N|\le|F_{r_2}|\) is pointwise and needs no projection. At the concrete \(b\), a complete C3/C6 input therefore bounds all middle real blocks. The allowed closed208 bridge pays the lower range \(N\le T^{4b}\), the upper range \(T^{1-2b}\le N\le T\), both equality endpoints, the singleton, the entire infinite tail, and logarithmic recombination. It also retains the \(\sqrt R\) factor and the sharp \(O(T^{1/2+\epsilon})\) reconstruction error. Thus, conditionally,
\[
 |P(R^2)|\ll T^{1/2+b+\epsilon},\qquad
 |P(X)|\ll X^{1/4+b/2+\epsilon}
         =X^{102/325+\epsilon}.
 \tag{R26}
\]
For the centered alternative, the allowed closed210 review supplies the restored mean wave \(T^{303/4550+\epsilon}=o(T^b)\). This is a separate pointwise route and is not an equivalence of the centered moment with the original tenth moment or its shell.

One fixed-\(b\) C3/C6 success gives only (R26). The proposed square-root oscillatory comparison (R21) leaves \(b\ge1/10\) in this certificate. Neither supplies the full quantified quarter result.

The final ledger correctly avoids a general prohibition on a single four-point theorem: a uniform \(\mathcal A_4\ll T^\epsilon\) at \(L,K\asymp N\) would make both diagonals in (R8) \(O(1)\) and would directly suffice. Alternatively, a family of valid inputs for \(b_j\downarrow0\), with every required band and complement restored, gives the quarter theorem. Constants uniform in \(j\) are unnecessary: choose fixed \(b_j\) and the remaining epsilon losses after the desired final epsilon. No such stronger arithmetic input is established here.

## 4. First doubtful or unproved step

No remaining defect was found in the final ledger's finite conditional claims. The first missing arithmetic input is C3. After nonzero mean subtraction, the validity and uniform bound for \(\rho_{h,k}\), followed by C6 for the actual complete coefficients, remain unproved.

The first invalid substitutions would be: transporting an unweighted prefix error without the variation factor; discarding \(h=k\); using a selected shift sector without paying its complement; or using a real-to-complex comparison without the required larger window. The final ledger does none of these.

The two requested repairs concern cutoff range and full-goal scope. They change no C1--C8 exponent or concrete milestone. The added centered variation argument proves only its specified positive certificate obstruction.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Both finite Fejer costs | GREEN: (R4)--(R8) retain exact multiplicities, both diagonals, and both moving-sum factors. |
| Raw versus physical normalization | GREEN: division is by \(N^3\); raw four-point amplitude has size one. |
| Integer lengths and real endpoints | GREEN after repair: (R9) covers the whole open band, and bounded \(T\) is explicitly paid. |
| Four-point overlap and \(h=k\) | GREEN: (R10) and Section 3C retain complete masks, repeated factors, and ordered-pair multiplicities. |
| Phase derivatives | GREEN: exact square-root third derivative \(3/8\), plus the corresponding higher derivatives, justify the continuous argument. |
| Small-product main terms | GREEN: (R14)--(R15) sum every \(h,k\), including \(h=k=1\), with the logarithm paid. |
| Main-term hypothesis | GREEN conditionally: no \(\rho\) formula or small remainder is asserted. |
| Unweighted versus oscillatory input | GREEN: (R17)--(R21) restore Abel variation and distinguish the two hypotheses. |
| Exact powers | GREEN: \(18/65\), \(36/65\), and supremal deficit \(31/325\) are independently reproduced. |
| Centered-envelope barrier | GREEN: actual variation and real-prefix atom floor prove (R23), only for the positive certificate. |
| Frequency projection | GREEN with the explicit larger-window buffer, bounded kernel norm, and global-coefficient tail. |
| Complete reconstruction | GREEN in the inherited concrete-\(b\) scope, with all complements, equality endpoints, tail, singleton, and sharp error. |
| Full quarter and M1/M2 | GREEN after fixed-\(b\) wording repair; no new arithmetic input, tenth moment, M1/M2 closure, or quarter theorem. |
| Review boundary | NONBLIND as assigned; no sibling current reports, source selection, shared state, or successor artifact accessed. |

No numerical experiment was run. These controls are finite algebra, exact rational arithmetic, and analytical estimates.

## 6. Dependencies, hashes, and provenance

Only the primary current ledger and these allowed inherited files were used for this review:

- protocol.md: SHA-256 f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a.
- rounds/codex-managed/gc-signed-near-frequency-cancellation/reports/actual_shifted_correlations.md: SHA-256 657fb00457c9ed8fabf4b3d3ffe71b26fdbeff85e767c35a94ff279aec248168.
- rounds/codex-managed/gc-signed-near-frequency-cancellation/reviews/independent_shifted_correlations_review.md: SHA-256 05960367004f155b22232dbe09bbe74ad11c1834df1196d99aa7f4330d117516.
- rounds/codex-managed/gc-full-proof-signed-arithmetic-review/controls/conductor_bandlimited_strategy.md: SHA-256 6aa17dd35e2d930cedadfb489adf8e042b6aed61ed5882ae8e2eb0cd36fbd552.

The closed210 material supplies the earlier certificate comparison, centered jump mechanism, and scoped mean-wave restoration. The closed208 ledger supplies the complete concrete reconstruction and window/complement requirements. Files merely cited inside these artifacts were not opened.

The conductor received the two repair requests immediately and then an interim confirmation of the normalization, derivative, complete small-product sum, and rational powers. After the conductor's repairs, I reread the full final ledger and independently checked its SHA-256. The newly explicit centered variation proof was rederived in Section 3F.

Only this assigned review file was written. The original isolated report, conductor ledger, graph, proof draft, validation matrices, synthesis, legacy files, and successor files were left unchanged by this reviewer.

## 7. Recommended state effect and final ledger binding

**Retain the final ledger as independently checked conditional sufficient-interface and source-cost evidence.** Do not promote C3, C6, any new pointwise exponent, the original tenth-moment target, an M1/M2 parent, or the quarter theorem.

This GREEN verdict binds to:

rounds/codex-managed/gc-full-source-method-review/controls/conductor_two_stage_strategy.md

**SHA-256: 9bf8f30d240304f88c46a5a93c7d93586b3ade1c674d5a5fdbc61a251fcd176f**

Both requested precision repairs and the centered-envelope variation lower bound are present and verified at that hash. A material later edit requires a new binding. The assigned review is complete and stops here.

