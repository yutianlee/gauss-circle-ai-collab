## Result

**RED as written, with local and exact repairs.**  The central arithmetic pruning (152.C23)--(152.C29) is correct, including all prime powers of \(N\), both parities of \(N\), the nearest-integer convention, the ceiling at \(M^{1/4}\), and the disjoint residual.  The newly inserted source range is also mathematically consistent with the terminal source report: the \(D\)- and \(B\)-fractions, the \(P_U\)-power, the boundary \(780/449\), and the beta crossing \(127/322\) all rederive exactly.

The candidate is nevertheless not promotion-ready in its present text:

1. Equation (152.C33) omits the required \(+\) before \(O_\varepsilon(X^\varepsilon)\), so the displayed boundary relation is malformed.
2. The statements \(R^2=N^{1/2}\) in the paragraph before (152.C27), \(T=\sqrt{NM}=R^2M^{1/2}\) in (152.C30), and \(T^{1/2}=RM^{1/4}\) after (152.C31) are false as exact equalities because \(N=\lfloor X\rfloor\) and \(R=X^{1/4}\).  Every occurrence must use \(\asymp\), while \(T:=\sqrt{NM}\) may remain exact.
3. “The best audited exponent-pair estimate is (152.C10b)” is false if “best” means the smallest pointwise upper bound throughout the ambient range.  For example, at \(M=R\), Bourgain's (152.C36) gives \(R^{23/168}\), whereas (152.C10b) gives \(R^{331/1592}\), and \(23/168<331/1592\).  What is correct is that (152.C10b) is the **boundary-optimal audited estimate**, namely the one that first becomes target-sized as \(M\) increases.

The global-pair inference is not an unsupported automatic use of a \(D\)-process: the source report supplies the required maximum comparison and symmetry step, and the arithmetic is rechecked below.  The candidate should cite that comparison explicitly when repairing (152.C38a), rather than making “\(D\) outputs a global pair” look formal.

Subject to the three repairs above and the explicit source-bridge sentence, the mathematical verdict becomes GREEN for the strict scale range and for the disjoint arithmetic pruning.  The full scalar remains open only in the lower residual range.

## Exact statement and hypotheses

Let

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad N\asymp R^4,
 \qquad 1\ll M\le R^2.
\]

Let

\[
 A_U(\ell)=\mathscr A_{1,M,U}(1,\ell),\qquad
 w_U(\ell)=\ell^{-3/4}A_U(\ell),
\]

with the accepted compact support, literal endpoint convention, zero extension, and actual-profile estimates

\[
 \|A_U\|_\infty+\operatorname{Var}A_U\ll_\varepsilon X^\varepsilon,
 \qquad
 \|w_U\|_\infty+\operatorname{Var}w_U
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\]

The reviewed scalar and accepted boundary seam are

\[
 P_U=\sum_{\substack{\ell>0\\\operatorname{odd}(\ell)}}
 \chi_4(\ell)w_U(\ell)e(\sqrt{N\ell}),
\]

\[
 S_U=e(-1/8)N^{1/4}P_U+O_\varepsilon(RX^\varepsilon),
 \qquad
 \widetilde S_U=B_{1,U}(1)S_U,\qquad
 |B_{1,U}(1)|\ll_\varepsilon X^\varepsilon.
\]

The two claims under review are:

1. the exact support reduction
   \[
   P_U=P_U^*+O_\varepsilon(X^\varepsilon),
   \]
   where \(P_U^*\) is (152.C10); and
2. the strict source bound
   \[
   |P_U|\ll_\varepsilon
   \left(\frac{R^{780}}{M^{449}}\right)^{1/1592}X^\varepsilon,
   \]
   hence target safety when \(M^{449}\gg R^{780}\).

Within the ambient Round-152 range, the previously owned TTY sector is subtracted first, so only the sliver between the exponents \(780/449\) and \(1424/819\) is newly credited.  After bounded \(M\) and the new strict range are removed, the open scalar range is \(M^{449}\ll R^{780}\), with comparable-boundary cases target-sized by the same displayed estimate.

## Proof/derivation

1. **Actual profile and external row coefficient.**  The permitted Round-151 candidate and controls give bounded variation for the retained reciprocal profile, the actual compact-smooth boundary transform, and the literal identity \(\widetilde S_U=B_{1,U}(1)S_U\).  The change \(q\mapsto4N/q^2\) is monotone on every retained component, so variation is preserved under reparameterization.  Multiplication by \(\ell^{-3/4}\) on \(\ell\asymp M\) gives the second estimate in (152.C11).  The coefficient \(B_{1,U}(1)\) remains external and costs only \(X^\varepsilon\); it is neither duplicated nor absorbed into an arbitrary wave coefficient.

2. **Exact ray (152.C23).**  Write uniquely
   \[
   N=a^2n_0,\qquad n_0\ \operatorname{squarefree}.
   \]
   In the unique odd decomposition \(\ell=\tau s^2\), \(N\tau\) is a square if and only if \(\tau=n_0\).  If \(n_0\) is even, this ray contains no odd \(\ell\).  If \(n_0\) is odd, then
   \[
   \sqrt{N\ell}=s\sqrt{Nn_0}=san_0\in\mathbb Z,
   \]
   and its phase is one.  On retained support \(s\asymp(M/n_0)^{1/2}\), so
   \[
   n_0^{-3/4}\sum_s s^{-3/2}|A_U(n_0s^2)|
   \ll_\varepsilon
   n_0^{-3/4}(M/n_0)^{-1/4}X^\varepsilon
   =M^{-1/4}n_0^{-1/2}X^\varepsilon.
   \]
   Empty or \(O(1)\)-length endpoint pieces satisfy the same bound up to the fixed support constants.  Thus (152.C23) is GREEN.

3. **All-parity prime-power root count (152.C25).**  Let \(p^\alpha\Vert N\) and \(v=\min(v_p(j),\alpha)\).  If \(v=\alpha\), then
   \[
   \#\{x\bmod p^\alpha:x^2\equiv0\}
   =p^{\lfloor\alpha/2\rfloor}\le p^{v/2}.
   \]
   If \(v<\alpha\) is odd, no root exists because a nonzero square has even \(p\)-adic valuation.  If \(v=2b<\alpha\), writing \(x=p^by\) leaves a unit square congruence modulo \(p^{\alpha-2b}\).  It has at most two roots for odd \(p\), at most four for \(p=2\), and every unit root has \(p^b\) lifts in \(x\bmod p^\alpha\).  Chinese remaindering therefore gives
   \[
   \rho_N(j)\le4\,2^{\omega(N)}\prod_{p\mid N}p^{v_p((j,N))/2}
   =4\,2^{\omega(N)}\sqrt{(|j|,N)}.
   \]
   This includes \(p=2\), \(j<0\), and the zero local congruence.  Equation (152.C25) is GREEN.

4. **Summation over \(j\) and the \(k\)-support.**  Since
   \[
   \sqrt{(|j|,N)}
   \le\sum_{d\mid(|j|,N)}\sqrt d,
   \]
   summing multiples of \(d\) gives
   \[
   \sum_{1\le|j|\le J}\sqrt{(|j|,N)}
   \ll J\sum_{d\mid N}d^{-1/2}.
   \]
   Both \(2^{\omega(N)}\) and the divisor sum are \(O_\varepsilon(N^\varepsilon)\), proving (152.C26).

   The actual \(\ell\)-support lies in a fixed dilation of \([M,2M]\); hence all nearest integers \(k(\ell)\) lie in an interval of length
   \[
   O(\sqrt{NM}+1).
   \]
   Since \(N\asymp R^4\) and \(M\le R^2\),
   \[
   \frac{\sqrt{NM}}{N}=\sqrt{\frac MN}\ll R^{-1},
   \]
   so this interval has length \(<N\) for large \(X\).  Each root class modulo \(N\) therefore supplies at most \(O(1)\) admissible \(k\)'s, and fixed \((j,k)\) fixes \(\ell=(k^2-j)/N\).  With \(J=M^{3/4}<N\),
   \[
   \#\mathcal L_1\ll_\varepsilon M^{3/4}X^\varepsilon,
   \qquad
   |P_{\mathcal L_1}|\ll_\varepsilon X^\varepsilon.
   \]
   The reasoning is GREEN; only the false equality \(R^2=N^{1/2}\) in the candidate must be replaced.

5. **Ceiling, large-square tail, partition, and residual.**  Put \(y=M^{1/4}\) and \(S_M=\lceil y\rceil\).  For integral \(s\),
   \[
   s\ge S_M\Longleftrightarrow s\ge y,\qquad
   s<S_M\Longleftrightarrow s<y.
   \]
   Thus the ceiling creates neither a gap nor an overlap, including when \(M^{1/4}\) is an integer.  For fixed \(s\ge S_M\), the fixed-dilation support admits \(O(1+M/s^2)\) integers \(\tau\), and
   \[
   \sum_{S_M\le s\ll\sqrt M}\left(1+\frac M{s^2}\right)
   \ll M^{1/2}+\frac M{S_M}\ll M^{3/4}.
   \]
   Oddness and squarefreeness only reduce this count.  Multiplication by
   \(\|w_U\|_\infty\ll M^{-3/4}X^\varepsilon\) proves (152.C29).

   The four sets in (152.C7) are pairwise disjoint and exhaustive: first \(j=0\); then \(0<|j|\le J_M\); and, for \(|j|>J_M\), exactly one of \(s\ge S_M\) and \(s<S_M\).  On the survivor, \(s<M^{1/4}\), so retained support \(\ell\asymp M\) gives
   \[
   \tau=\ell/s^2\gg M^{1/2}.
   \]
   Also \(\chi_4(\tau s^2)=\chi_4(\tau)\) and
   \(e(\sqrt{N\tau s^2})=e(s\sqrt{N\tau})\), proving the exact residual (152.C10).  The \(s=1\), large-defect layer is still structurally present; no signed bound for it is inferred.  Equations (152.C28)--(152.C29), the owner partition, and the residual are GREEN.

6. **Adjacent pairing and one \(A\)-process.**  The finite difference (152.C15) is exact.  Its second line contains
   \[
   1-e\!\left(\frac{2\sqrt N}{\sqrt{x+2}+\sqrt x}\right),
   \]
   which has no uniform smallness modulo one.  The first line alone is controlled by \(\operatorname{Var}w_U\); the full oscillatory difference is not.

   After writing \(\ell=2n+1\), a shift \(h\) in \(n\) gives
   \[
   \chi_4(\ell+2h)\chi_4(\ell)=(-1)^h.
   \]
   Hence the character is constant in the correlation.  On \(x\asymp M\),
   \[
   g_h''(x)\asymp R^2hM^{-5/2}.
   \]
   The second-derivative estimate and product-weight variation give
   \[
   |C_h|\ll_\varepsilon
   \left(Rh^{1/2}M^{-7/4}
   R^{-1}h^{-1/2}M^{-1/4}\right)X^\varepsilon.
   \]
   Van der Corput differencing then gives exactly (152.C19).  Making its three displayed terms target-sized requires
   \[
   H\gg M^{1/2},\qquad
   H\ll M^{3/2}/R^2,\qquad
   H\gg M^{3/2}/R^2.
   \]
   The first two are compatible only at or above \(M\asymp R^2\), outside the frozen lower range.  The adjacent and one-\(A\)-process powers are GREEN.

7. **Mellin root number, conductor, and dual length.**  For the primitive odd character,
   \[
   \tau(\chi_4)=2i,\qquad
   \varepsilon(\chi_4)=\frac{2i}{i\sqrt4}=1.
   \]
   Therefore
   \[
   \Lambda(s,\chi_4)=
   (4/\pi)^{(s+1)/2}\Gamma((s+1)/2)L(s,\chi_4)
   =\Lambda(1-s,\chi_4).
   \]
   The Mellin spectrum has
   \[
   T:=\sqrt{NM}\asymp R^2M^{1/2},
   \]
   analytic conductor \(\asymp T\), and balanced length
   \(T^{1/2}\asymp RM^{1/4}\).  Character Poisson has stationary point
   \(x_q=4N/q^2\), so
   \[
   q\asymp2\sqrt{N/M},\qquad
   Q:=2\sqrt{N/M}\asymp R^2M^{-1/2}.
   \]
   Its stationary factor is \(e(1/8)N^{-1/4}\), giving the corrected formula
   \[
   P_U=e(1/8)N^{-1/4}
   \sum_{\substack{q>0\\\operatorname{odd}(q)}}
   \chi_4(q)A_U(4N/q^2)e(N/q)
   O_\varepsilon(X^\varepsilon).
   \]
   The accepted Round-151 boundary ledger supplies the target-safe error and endpoints.  The main transform self-returns; it does not supply an independent gain.  The root number and dual length are GREEN, while the equality and missing-plus repairs are mandatory.

8. **Exponent-pair translations and the new boundary.**  A source-legal pair \((\kappa,\lambda)\) gives
   \[
   |P_U|\ll_\varepsilon
   R^{2\kappa}M^{\lambda-\kappa/2-3/4}X^\varepsilon.
   \]
   This gives
   \[
   (13/84,55/84):
   \quad (R^{52}/M^{29})^{1/168},
   \]
   and
   \[
   B(89/1282,997/1282)
   =(178/641,365/641):
   \quad (R^{1424}/M^{819})^{1/2564}.
   \]
   Both translations in (152.C36)--(152.C38) are correct.

   For the new input, the displayed \(D\)-formula gives
   \[
   D(13/84,55/84)
   =\left(\frac{18}{199},\frac{593}{796}\right).
   \]
   The global-pair step is not automatic.  The source report supplies the necessary Lemma-14 maximum check: on \(0\le\alpha\le1/2\),
   \[
   \left(\frac{18}{199}+\frac{521}{796}\alpha\right)
   -\left(\frac1{12}+\frac23\alpha\right)
   =\frac{17-29\alpha}{2388}
   \ge\frac5{4776}>0.
   \]
   Thus the \(D\)-line is the controlling branch of the printed maximum; Lemma 15 and the stated symmetry give the global \(D\)-pair.  Applying \(B(\kappa,\lambda)=(\lambda-1/2,\kappa+1/2)\) gives
   \[
   BD(13/84,55/84)
   =\left(\frac{195}{796},\frac{235}{398}\right).
   \]
   Substitution yields
   \[
   R^{390/796}M^{-449/1592}
   =\left(\frac{R^{780}}{M^{449}}\right)^{1/1592}.
   \]
   The threshold comparison is exact:
   \[
   780\cdot819=638820
   <639376=1424\cdot449,
   \]
   hence \(780/449<1424/819\).

   In beta coordinates,
   \[
   \frac{18}{199}+\frac{521}{796}\alpha
   =\frac{1+\alpha}{4}
   \Longleftrightarrow 322\alpha=127.
   \]
   With \(\alpha=(4-\mu)/(4+\mu)\), this gives
   \[
   \alpha=\frac{127}{322},\qquad
   \mu=4\frac{1-\alpha}{1+\alpha}=\frac{780}{449}.
   \]
   It lies strictly in the source-report cell because
   \[
   \frac{127}{322}-\frac{1508}{3825}
   =\frac{199}{1231650}>0
   \]
   and
   \[
   \frac{62831}{155153}-\frac{127}{322}>0.
   \]
   Thus the fractions, power, threshold, beta crossing, and cell are GREEN.  This certification uses exactly the maximum and symmetry argument printed in the source report; it does not assume that every formal \(D\)-transform is automatically a global exponent pair.

   The phrase “best audited estimate” must nevertheless be narrowed.  The new pair is boundary-optimal, but Bourgain is pointwise sharper farther below the boundary; at \(M=R\), its loss is \(R^{23/168}\), compared with \(R^{331/1592}\) from \(BD\).

9. **Elementary endpoints, derivative bounds, and scope.**  The original and reciprocal absolute capacities are
   \[
   M^{1/4},\qquad RM^{-1/2}.
   \]
   They meet at \(M=R^{4/3}\) with loss \(R^{1/3}\), and are target-sized only at the bounded and top endpoints.  The second- and third-derivative powers in (152.C39)--(152.C40) rederive as
   \[
   RM^{-1/2}+R^{-1},
   \qquad
   R^{1/3}M^{-1/6}+R^{-1/3}M^{1/6}.
   \]
   Neither closes a lower scale.  The new exponent-pair owner closes \(M^{449}\gg R^{780}\); below it, (152.C41) is the first open signed estimate.

   The candidate keeps the conclusion at the literal \(D=L=1\) scalar, retains \(B_{1,U}(1)\), and expressly leaves every \(D>1\), \(L>1\), generic, original \(t\ge2\), cross, M9--M1/M2, endpoint assembly, bridge, target, and global exponent outside scope.  This scope is GREEN.

## First doubtful or unproved step

After the exact repairs and after accepting the terminal source report's explicit Lemma-14 maximum, Lemma-15 equivalence, symmetry, model-phase, and proper-subinterval checks, the first unproved mathematical step is

\[
 |P_U^*|\ll_\varepsilon X^\varepsilon
\]

in the lower range \(M^{449}\ll R^{780}\).  The far-defect \(s=1\) layer has no inner square-factor summation and retains absolute capacity \(M^{1/4}X^\varepsilon\).  Neither the arithmetic pruning, adjacent pairing, termwise \(A\)-process, Mellin functional equation, nor the audited exponent-pair envelope proves its signed cancellation.

The \(BD\)-pair seam itself is supported rather than assumed: the source report proves the otherwise essential maximum comparison
\((17-29\alpha)/2388>0\) on \(0\le\alpha\le1/2\), invokes the printed symmetry, checks the square-root model phase and proper intervals, and locates the beta crossing inside the stated Table-1 cell.  Without that source report, (152.C38a)'s terse “Lemma 15 gives the global pair” would be insufficient.

## Required control test and outcome

| Control | Outcome |
|---|---|
| All-parity prime-power roots, (152.C25) | **GREEN.** Odd primes, \(p=2\), odd valuations, even valuations, and the zero congruence give the claimed multiplicity. |
| Sum over nonzero \(j\), (152.C26) | **GREEN.** Divisor expansion gives \(J\sum_{d\mid N}d^{-1/2}\), and all divisor factors are \(N^\varepsilon\). |
| \(k\)-support modulo \(N\) | **GREEN after repair.** Its length is \(O(\sqrt{NM})<N\); replace the false equality \(R^2=N^{1/2}\) by \(R^2\asymp N^{1/2}\). |
| Exact \(j=0\) ray, (152.C23) | **GREEN.** It is \(\tau=n_0\), exists only for odd \(n_0\), has phase one, and costs \(M^{-1/4}n_0^{-1/2}X^\varepsilon\). |
| Ceiling and large-\(s\) tail, (152.C28)--(152.C29) | **GREEN.** Integral \(s\) makes the ceiling partition exact; the count is \(O(M^{3/4})\). |
| Disjoint owners and residual, (152.C7)--(152.C10) | **GREEN.** The four sets exhaust without overlap, \(\tau\gg M^{1/2}\) on the survivor, and the \(s=1\) far-defect wave remains open. |
| Adjacent pairing and one \(A\)-process | **GREEN/no gain.** The whole oscillatory difference remains; one shift erases the variable character and gives the powers in (152.C19). |
| Mellin root number and dual length | **RED as typeset, GREEN mathematically after repair.** Root number \(+1\), \(T\asymp R^2M^{1/2}\), and \(Q=2\sqrt{N/M}\) are correct.  Insert \(+\) in (152.C33) and replace false exact \(N\)-to-\(R\) equalities by \(\asymp\). |
| Bourgain and TTY powers | **GREEN.** Equations (152.C36)--(152.C38) have the correct fractions and \(R,M\)-powers. |
| \(D\), \(BD\), beta crossing, and Table-1 cell | **GREEN with the source report as an explicit dependency.** The maximum comparison, global inference, fractions, \(P_U\)-power, boundary comparison, and cell placement all pass. |
| “Best audited estimate” wording | **RED.** Replace by “boundary-optimal audited estimate”; Bourgain is pointwise sharper at lower scales such as \(M=R\). |
| Actual profile and \(B_{1,U}(1)\) | **GREEN.** The accepted BV/endpoint ledger is sufficient for Abel insertion and the transform; the external coefficient remains attached and costs \(X^\varepsilon\). |
| Endpoint and downstream scope | **GREEN.** Bounded/top capacities, the new strict owner, lower residual, and every named out-of-scope object are separated. |

No numerical test is needed: all controls above are exact algebraic, divisor, valuation, or exponent calculations.

## Dependencies and exact artifacts

This review used only:

1. protocol.md (already read for the preceding statement-only task);
2. rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reports/square_root_character_wave_attack.md;
3. rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reports/blind_square_root_wave_feasibility.md;
4. rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/reports/square_root_wave_source_audit.md;
5. rounds/codex-managed/m9-m1-lower-cone-t1-d1-square-root-wave-gate/candidates/conductor_round152_square_root_wave_reduction.md, reread after its material source-range patch;
6. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/candidates/conductor_round151_character_ranges_and_bprocess_boundary.md; and
7. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-large-wrap-shifted-factor-gate/controls/conductor_round151_controls.md.

No state file, strategy, barrier packet, brief, synthesis, validation matrix, source card, web page, or other historical artifact was read.  No candidate, state, or shared artifact was edited.

## Recommended state effect

**Revise; do not promote the conductor candidate as presently typeset.**  Make these exact repairs:

1. In (152.C33), insert
   \[
   {}+O_\varepsilon(X^\varepsilon)
   \]
   after the reciprocal sum.
2. Replace \(M\le R^2=N^{1/2}\) by \(M\le R^2\asymp N^{1/2}\); replace (152.C30) by
   \[
   T:=\sqrt{NM}\asymp R^2M^{1/2},\qquad
   Q:=2\sqrt{N/M}\asymp R^2M^{-1/2};
   \]
   and replace \(T^{1/2}=RM^{1/4}\) by \(T^{1/2}\asymp RM^{1/4}\).
3. Replace “The best audited exponent-pair estimate is (152.C10b)” by “The audited exponent-pair envelope first becomes target-sized at (152.C10b); this is the boundary-optimal audited estimate.”  Do not claim it is pointwise smallest farther below the boundary.
4. In the discussion of (152.C38a), explicitly cite the source report's controlling-maximum calculation
   \[
   \frac{17-29\alpha}{2388}\ge\frac5{4776}
   \quad(0\le\alpha\le1/2)
   \]
   and the printed symmetry used with Lemma 15.  This makes clear that \(D\) is not being treated as an automatic global exponent-pair operation.
5. For statement hygiene, replace
   \(\operatorname{odd\ and\ squarefree}\) in (152.C6) and (152.C42) by separate predicates \(\operatorname{odd}\) and \(\operatorname{squarefree}\).

After those repairs, promote both:

- the exact target-safe pruning (152.C7)--(152.C10); and
- the new strict scale range \(M^{449}\gg R^{780}\), crediting only the portion not already owned by Round 151.

Retain \(P_U^*\) open for \(M^{449}\ll R^{780}\), and make no downstream theorem or exponent change.

### Terminal recheck after conductor repairs

**Final verdict: GREEN.**  This terminal verdict supersedes the earlier repairable RED for the pre-repair candidate.

The repaired candidate now passes every blocking item:

1. (152.C33) contains the required
   \(+O_\varepsilon(X^\varepsilon)\).
2. The floor seam is exact: the \(k\)-support paragraph uses
   \(R^2\asymp N^{1/2}\), (152.C30) uses
   \(T:=\sqrt{NM}\asymp R^2M^{1/2}\), and the balanced
   approximate-functional-equation length is
   \(T^{1/2}\asymp RM^{1/4}\).
3. The source-range sentence now calls (152.C10b)
   boundary-optimal and explicitly disclaims pointwise dominance over
   older pairs.  This removes the counterexample at \(M=R\), where
   Bourgain is numerically sharper while remaining non-target-sized.
4. The \(D\)-process bridge is now explicit.  Equation (152.C38aa)
   verifies the Lemma-14 maximum on \(0\le\alpha\le1/2\):
   \[
   \frac{17-29\alpha}{2388}>0.
   \]
   The candidate then invokes exactly the Lemma-15 symmetry bridge
   supplied by the source report.  The lower and symmetric upper lines
   meet at \(\alpha=1/2\); on the upper half the symmetric line is no
   larger than the \(D\)-pair line.  Thus the repaired text does not
   assume that a formal \(D\)-transform is automatically a global
   exponent pair.

No regression was introduced in (152.C23)--(152.C29), the ceiling
partition, the residual (152.C10), the actual-profile and
\(B_{1,U}(1)\) seam, adjacent pairing, the one-\(A\)-process powers,
the Mellin root number or reciprocal length, the Bourgain/TTY/\(BD\)
powers, the beta crossing and Table-1 cell, the endpoint capacities, or
the downstream scope.

The candidate is now mathematically ready to promote the exact pruning
(152.C7)--(152.C10) and the strict range
\(M^{449}\gg R^{780}\), crediting only the previously unowned sliver.
The lower residual \(P_U^*\) remains open, and no downstream theorem or
global exponent follows.
