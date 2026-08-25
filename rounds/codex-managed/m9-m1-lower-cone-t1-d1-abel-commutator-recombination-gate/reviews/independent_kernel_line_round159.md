# Round 159 independent terminal kernel line review

- Campaign: m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate
- Role: independent terminal line reviewer
- Object audited: (K159.1)--(K159.29) only
- Allocation: 100% analytic/algebraic; 0% numerical

## 1. Result

**Verdict: qualified pass for the finite kernel; narrow precision revision
before terminal promotion; no analytic-target promotion.**

The six Abel lines have the correct signs and outer endpoints, including the
singleton case. Complete-frequency inversion has the correct constant and
retains every residue rather than folding complementary representatives. The
zero and Nyquist whole rows are subtracted once, the \(c=4\) fibre is empty
after those rows are removed, the physical-to-selected map has multiplicity
one, and the actual-project support/lift hypotheses remove the lift indicator.
The quotient character, quotient profile, integral phase shift, root-defect
coordinate, variable mask, and normalized/raw target scales are correct.

No numerical value, sign, or power in (K159.1)--(K159.29) needs changing.
Five precision edits are needed before treating the file as a self-contained
terminal kernel:

1. After (K159.5), declare reversed finite sums to be zero. This defines the
   empty-block case; singleton blocks already reduce correctly to the outer
   line alone.
2. In (K159.16), write \(x\in\mathcal L_U\), or say explicitly that
   \(x\bmod 4N\) uses the inherited physical representatives. The displayed
   formula for \(B_j\) is not representative-invariant.
3. Qualify the prose after (K159.23) by
   \(N=\lfloor X\rfloor\) and
   \(w_U(\ell)=\ell^{-3/4}A_U(\ell)\), with the identical localization and
   zero extension. The permitted Round-154 artifact is labelled a candidate,
   so “accepted Round-154” should be “Round-154 candidate” unless a separate
   promotion record is supplied.
4. Expand (K159.25) into the exact clipped intervals, recording the strict
   inner and closed outer defect endpoints and the open half-cell clipping.
5. Define the Fourier coefficient and the actual \(h=-1\) expression bounded
   in (K159.29). The one-mode bound is correct, but its subject and
   normalization are currently implicit.

Equations (K159.26)--(K159.27) are desired estimates, not proved estimates.
The first open theorem is (K159.27) for the literal common profile and hard
mask. The text beginning with (K159.30) is visibly labelled route-scoped,
method-specific capacity and not an impossibility theorem; no formula at or
after (K159.30) was otherwise reviewed.

## 2. Exact statement and hypotheses

Retain (K159.1)--(K159.4), including the fixed-dilation support and inherited
complete nonwrapping physical lift. Put

\[
 a=\lfloor V\rfloor+1,\qquad b=\lfloor2V\rfloor,
\tag{159.KLR.1}
\]

and impose the finite convention

\[
 \sum_{m=p}^{q}(\cdots)=0\qquad(q<p).
\tag{159.KLR.2}
\]

Then (K159.9) and (K159.11) cover empty blocks. If \(a=b\), both difference
sums vanish and the sole outer term is the original singleton.

The literal Round-154 identification additionally requires

\[
 N=\lfloor X\rfloor,\qquad
 w_U(\ell)=\ell^{-3/4}A_U(\ell)
\quad\text{with the same localization and zero extension}.
\tag{159.KLR.3}
\]

Under (159.KLR.3), (K159.23) is precisely the hard block
\(V<|k(\ell)^2-N\ell|\le2V\) of candidate (154.C2); \(\chi_4\) makes the
explicit odd-\(\ell\) restriction automatic.

For a literal version of (K159.29), periodically extend

\[
 g_{k,V}(u)=
 \mathbf1_{V<|-u(2k+u)|\le2V},
 \qquad -\tfrac12<u<\tfrac12,
\]

and define

\[
 \gamma_h(k)=\int_{-1/2}^{1/2}g_{k,V}(u)e(-hu)\,du,
 \qquad
 \mathcal M_{-1}
 =\sum_{\ell\ge1}\chi_4(\ell)\widetilde w_U(\ell)
   \gamma_{-1}(\kappa(\ell)).
\tag{159.KLR.4}
\]

The auditable content of (K159.29) is
\(\mathcal M_{-1}\ll_\varepsilon X^\varepsilon\). This is the raw
\(\widetilde w_U\)-mode bound; its contribution to \(\mathcal S_U\) is
\(O_\varepsilon(M^{-3/4}X^\varepsilon)\). It does not assert that a truncated
Fourier series equals the hard mask at its jumps.

## 3. Proof and formula-by-formula audit

### 3.1 Line ledger

| Formula | Verdict | Exact check |
|---|---|---|
| (K159.1) | Pass | Frozen cone; \(K/N=\sqrt{M/N}\le N^{-1/4}\). |
| (K159.2) | Pass | \(c=4N/d\), \(H=2N/d\), and \(H/2=N/d\); \(H\) is even. |
| (K159.3) | Pass | The mask makes the radicand positive and retains the literal asymmetric cell, profile, and residual phase on the chosen lift. |
| (K159.4) | Pass | Fixed positive dilation plus zero-extended BV gives the support and variation used later. |
| (K159.5) | Pass after (159.KLR.2) | Exactly \(V<|j|\le2V\); the blocks are reflections. |
| (K159.6) | Pass | For \(j>0\), the cell is \(x\ge j+1\); for \(j<0\), it is \(x\ge-j\). |
| (K159.7) | Pass after (159.KLR.2) | Correct positive prefix and negative suffix. |
| (K159.8) | Pass | Atom at \(x=j+1\), followed by literal \(F_j-F_{j+1}\). |
| (K159.9) | Pass | Positive right outer endpoint; both coefficient-difference lines have the displayed sign. |
| (K159.10) | Pass | Atom at \(x=-j\), followed by literal \(F_j-F_{j-1}\). |
| (K159.11) | Pass | Negative left outer endpoint; the moving atom is positive. |
| (K159.12) | Pass | Accepted half-period inverse identity with the Fourier sign matching \(\widehat B_j(2dv)\). |
| (K159.13) | Pass | \((1+i)(1-i)=2\) and \(dc=q\), leaving exactly \(-i\chi_4(d)/(2N)\). |
| (K159.14) | Pass | \(h=du\), \(d=(h,N)\), bijects divisor-unit pairs with odd \(h\bmod4N\) and gives the character completion. |
| (K159.15) | Pass | Completing \(v\) adjoins exactly \(v=0,H/2\); solving for the interior subtracts each whole row once. |
| (K159.16) | Pass after representative clarification | All exterior constants are consumed. Use \(x\in\mathcal L_U\), or define the displayed residue representatives. |
| (K159.17) | Pass as inherited input | Whole-row estimate only; it is not transferred to an Abel fragment. |
| (K159.18) | Pass | Nonzero \(G_N\) gives integral \(\ell\) and exact weight \(\chi_4(\ell)\). |
| (K159.19) | Pass | Direct substitution gives both closed integer endpoints. |
| (K159.20) | Pass | Consecutive cells partition the positive integers; no half-integer tie; multiplicity one. |
| (K159.21) | Pass for actual-project hypotheses | Fixed-dilation support plus the inherited lift proves containment. |
| (K159.22) | Pass | Profile \(w_U(\ell)\); \(e(\sqrt{N\ell}-\kappa)=e(\sqrt{N\ell})\) only because \(\kappa\in\mathbb Z\). |
| (K159.23) | Pass; add (159.KLR.3) for Round 154 | Exact common quotient-profile scalar. The cited Round-154 file is labelled candidate, not accepted. |
| (K159.24) | Pass | Expanding \(N\ell=(\kappa+\delta)^2\) gives \(r=-\delta(2\kappa+\delta)\). |
| (K159.25) | Pass; print (159.KLR.8) below | Correct roots; lower \(V\)-surface strict, upper \(2V\)-surface closed, subject to the open half-cell. |
| (K159.26) | Pass as target only | Desired normalized estimate, not proved here. |
| (K159.27) | Pass as target only | Restoring the \(M^{-3/4}\) atom scale makes it equivalent to (K159.26). |
| (K159.28) | Pass as inherited unsigned input | Support capacity only; no signed cancellation beyond the owned collar. |
| (K159.29) | Pass after defining (159.KLR.4) | Character cancellation bounds that coefficient mode only; no missing \(M^{3/4}\) factor. |

### 3.2 Abel signs, endpoints, and degenerate blocks

The prefix and suffix identities are

\[
 K_j=P^+(j)-P^+(j-1),\qquad
 K_j=P^-(j)-P^-(j+1),
\]

and therefore

\[
\begin{aligned}
 \sum_{j=a}^{b}A_jK_j
 &=A_bP^+(b)+\sum_{j=a}^{b-1}(A_j-A_{j+1})P^+(j),\\
 \sum_{j=-b}^{-a}A_jK_j
 &=A_{-b}P^-(-b)+
   \sum_{j=-b+1}^{-a}(A_j-A_{j-1})P^-(j).
\end{aligned}
\tag{159.KLR.5}
\]

The pointwise differences (K159.8) and (K159.10) prove all six lines.
Zero extension keeps every component birth, death, and transition inside
\(F_j-F_{j\pm1}\). For \(a=b\), (159.KLR.5) is outer-only and equals the
singleton. For \(a>b\), (159.KLR.2) makes both sides zero.

### 3.3 Complete frequency, complementary modes, and special rows

After multiplying (K159.12) by the exterior factor, the \(d\)-fibre is

\[
 -\frac{i}{2N}\chi_4(d)
 \sum_{u\bmod c}^{*}\chi_4(u)e_c(ut).
\]

The disjoint bijection \(h=du\bmod4N\), \(d=(h,N)\), and multiplicativity
\(\chi_4(d)\chi_4(u)=\chi_4(h)\) give

\[
 -\frac{i}{2N}
 \sum_{\substack{h\bmod4N\\h\ \mathrm{odd}}}
 \chi_4(h)e_{4N}(ht)
 =\mathbf1_{N\mid t}\chi_4(t/N)=G_N(t).
\tag{159.KLR.6}
\]

No factor two occurs: both \(v\) and \(H-v\) remain. The unique nonzero fixed
point is \(v=H/2\), where \(2d(H/2)=2N=q/2\). Thus the completed row is
exactly interior plus the whole zero row plus the whole Nyquist row. If
\(c=4\), then \(H=2\), so \(v=0,1\) exhaust the fibre and its interior is
empty.

### 3.4 Physical lift, nearest cell, quotient data, and mask

The integer cell (K159.19) is equivalent to

\[
 x-\frac12<\sqrt{N\ell}<x+\frac12.
\tag{159.KLR.7}
\]

Both real endpoints are strict: a tie would make \(4N\ell\) an odd square.
The upper integer endpoint for \(x\) is \(x^2+x\), and the next lower endpoint
is \(x^2+x+1\). Hence the cells partition the positive integers.

Fixed-dilation support confines \(\kappa(\ell)\) to

\[
 \sqrt{\alpha NM}-\frac12
 \le\kappa(\ell)\le
 \sqrt{\beta NM}+\frac12.
\]

This hull has length \(O(K)<N\), and \(2\kappa<N\) for sufficiently large
\(X\), because \(M\le N^{1/2}\). The inherited physical lift contains it. For
bounded initial \(X\), containment comes from the defining lift convention,
not from the eventual inequality \(2\kappa<N\).

For \(k=\kappa(\ell)\), the exact expansion of (K159.25) is

\[
\begin{aligned}
 \mathbf1_{V<|r(\ell)|\le2V}
 ={}&
 \mathbf1_{\delta<0}
 \mathbf1_{-\delta\in
   (u_V^+(k),u_{2V}^+(k)]\cap(0,1/2)}\\
 &+
 \mathbf1_{\delta>0}
 \mathbf1_{\delta\in
   (u_V^-(k),u_{2V}^-(k)]\cap(0,1/2)}.
\end{aligned}
\tag{159.KLR.8}
\]

Equivalently, the positive-defect interval in \(\delta\) is
\([-u_{2V}^+(k),-u_V^+(k))\cap(-1/2,0)\). On supported asymptotic terms,
\(k^2>2V\), so \(u_s^+\) is real. Outside that eventual range one must define
the positive endpoint by saturation/emptiness rather than write
\(\sqrt{k^2-s}\) for \(s>k^2\). Formula (159.KLR.8) records the inner strict,
outer closed, and open half-cell clipping exactly.

### 3.5 The shifted \(h=-1\) coefficient

For integer \(h\),
\(e(h\delta)=e(h\sqrt{N\ell})\), so the built-in phase becomes
\(e((h+1)\sqrt{N\ell})\). At \(h=-1\), only \(\chi_4(\ell)\) remains.
The four clipped endpoints in (159.KLR.8) are monotone functions of \(k\);
their total variation is \(O(1)\). Hence

\[
 \|\gamma_{-1}\|_\infty+
 \operatorname{Var}_{k}(\gamma_{-1})\ll1.
\tag{159.KLR.9}
\]

Composition with increasing \(\kappa(\ell)\) does not increase variation.
Moreover
\[
 \|\widetilde w_U\|_\infty+
 \operatorname{Var}(\widetilde w_U)
 \ll_\varepsilon X^\varepsilon.
\]
Thus the coefficient in (159.KLR.4) has BV
\(O_\varepsilon(X^\varepsilon)\). Bounded partial sums of \(\chi_4\) and
discrete Abel summation prove
\(\mathcal M_{-1}\ll_\varepsilon X^\varepsilon\). Boundary jump values,
Fourier truncation, and every \(h\ne-1\) mode remain open.

## 4. First doubtful or unproved step

After the five precision edits in Section 1, there is no doubtful step in
(K159.1)--(K159.25), (K159.28), or the explicitly defined one-mode version of
(K159.29). The blind report's lift countermodel is valid for its stripped
BV-only statement but violates the actual fixed-dilation/lift compatibility.

The first unproved mathematical statement is target (K159.27), uniformly on
the open side \(M^{449}\ll R^{780}\) beyond the accepted
fixed-polylogarithmic collar. Neither (K159.28) nor (K159.29) proves it. A
Fourier proof must still control the exact \(k\)-dependent coefficients, both
hard boundary surfaces with strict/closed conventions, truncation error, and
all nonexceptional modes. Mark (K159.26)--(K159.27) visibly
“desired/unproved.”

The Round-154 identity is exact only after (159.KLR.3); this is a missing
printed hypothesis, not an algebraic obstruction. Within the permitted
evidence, its artifact status is candidate. No claim at or after (K159.30)
was audited beyond confirming the explicit route-capacity labels.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Abel signs and outer endpoints | **Pass.** Positive right outer, negative left outer, both moving atoms positive. |
| Empty and singleton blocks | **Pass after (159.KLR.2).** Singleton is outer-only; empty is zero. |
| All-\(d\), all-\(v\) constants | **Pass.** (159.KLR.6) restores exactly \(G_N\), with no residual factor. |
| Complementary modes and \(c=4\) | **Pass.** No folding; \(c=4\) has only the two removed rows. |
| One-time zero/Nyquist subtraction | **Pass.** Whole rows removed once after recombination; no theorem transferred to a piece. |
| Physical representative convention | **Revise notation.** Write \(x\in\mathcal L_U\) in (K159.16), or define the residue representatives. |
| Lift containment | **Pass for actual-project hypotheses.** Fixed-dilation support plus the inherited lift proves it. |
| Nearest-cell endpoints | **Pass.** Closed integer cell, strict real half-cell, no tie, multiplicity one. |
| Quotient character/profile/phase | **Pass.** \(\chi_4(\ell)\), \(w_U(\ell)\), and \(e(\sqrt{N\ell})\); no trace-boundary profile survives. |
| Round-154 identity | **Pass after (159.KLR.3).** Call the permitted artifact a candidate unless separate acceptance evidence is supplied. |
| Mask endpoints and clipping | **Pass after printing (159.KLR.8).** Inner strict, outer closed, open half-cell clipping retained. |
| Raw target | **Pass as calibration; open as theorem.** Normalized \(X^\varepsilon\) is equivalent to raw \(M^{3/4}X^\varepsilon\). |
| Shifted \(h=-1\) mode | **Pass after (159.KLR.4).** Raw mode is \(O(X^\varepsilon)\); normalized contribution is \(O(M^{-3/4}X^\varepsilon)\). |
| Downstream scope | **Pass.** No transfer beyond full paired-interior \(D=d=L=1\) or across the external scalar seam. |
| (K159.30) onward | **Scope-label pass only.** Visibly route-scoped capacities, not universal barriers. |

No computation, web search, or external theorem was used.

## 6. Dependencies and exact artifacts used

This review read and used only:

1. protocol.md;
2. state/active_campaign.yml;
3. proofs/kernels/m9_m1_d1_full_abel_common_profile_recombination.md;
4. proofs/kernels/m9_m1_d1_nonzero_centering_nyquist_fold.md;
5. proofs/kernels/m9_m1_d1_paired_interior_cell_trace_reduction.md;
6. rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/reports/blind_full_abel_rederivation.md;
7. rounds/codex-managed/m9-m1-lower-cone-t1-d1-abel-commutator-recombination-gate/reviews/independent_lift_normalization_round159.md; and
8. rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_exact_root_defect_reparametrization.md.

No proof graph, proof draft, validation matrix, strategy file, conductor seed,
unlisted report or review, source card, web source, or computation was
inspected. This review changes no kernel or shared state.

## 7. Recommended state effect

**Revise narrowly, then promote only the finite algebraic package; retain the
analytic target as open.** Add the empty-sum convention (159.KLR.2), clarify
the physical representatives in (K159.16), add the exact Round-154
specialization (159.KLR.3), print the clipped mask (159.KLR.8), define the
Fourier mode by (159.KLR.4), and label (K159.26)--(K159.27) as
desired/unproved.

After those edits, promote as candidate-validated finite evidence: the two
three-line Abel reconstructions; recombination per \((d,v)\); all-\(d\),
all-\(v\) normalization; one subtraction of each whole special row; the
\(c=4\) empty-fibre check; lift containment; nearest-cell multiplicity one;
the exact common quotient-profile compression; the Round-154 candidate hard
block identification; variable-mask geometry; target calibration; and the
single shifted \(h=-1\) coefficient bound.

Do not promote (K159.26) or (K159.27), any owner-complete new range, or any
conclusion for \(D>1\), \(L>1\), generic \(t=1\), \(t\ge2\), cross terms,
another M1 or M2 owner, endpoint uniformity, M9, the bridge, the quarter
theorem, either global exponent, or the external \(B_{1,U}(1)\) scalar seam.
