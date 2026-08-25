# Round 161 projective-power and scope review

## 1. Result: GREEN for the scoped no-go, not for the target

**Verdict: GREEN.** The post-unmask normalization, one-column
projective/Bessel obstruction, and scope statements in the conductor
candidate are correct. In particular:

1. the physical formula for \(B_D(1)\) has the right
   \(L^{3/2}D^{-3/4}=(L^2/D)^{3/4}\) normalization and retains the literal
   profiles, cone, parity, support, and zero extension;
2. a fixed positive-relative-width ambient interval \(D\asymp L^2\)
   contains \(Q\asymp L^2\) squarefree radicals;
3. on its one-column restriction, the evaluation norm and the Hilbert
   projective (nuclear) norm of the phase-aligned diagnostic are both
   exactly \(Q^{1/2}\asymp L\), and their product is \(Q\asymp L^2\);
4. the accepted physical energy permits the same \(L^{2+o(1)}\) positive
   upper capacity, leaving exactly the polynomial factor \(L^{1/2}\)
   relative to the \(L^{3/2}X^\varepsilon\) target; and
5. the diagnostic proves only a coefficient-interface route obstruction.
   It proves neither a lower bound nor a counterexample for the literal
   \(B_D(1)\).

The bound for \(D\le CL\), with fixed \(C\), is a complete bound for that
long-channel **sector** only. It is not an owner-complete polynomial
range of \(L\) for the whole hard-TOP scalar and does not meet the strict
range exit gate. Thus the only supported Round-161 close label is
**hard_top_radical_frequency_coupling_no_go**.

## 2. Exact statement and hypotheses audited

Fix the one nonsquare, half-open, polynomial intermediate hard-TOP block
from the barrier packet. Thus \(1\ll L\ll H\), \(J=\sqrt X\), \(J\) is
an arbitrary fixed real centre, and

\[
 \mathcal T_L^{\rm ns}
 =\sum_{D>1\ {\rm sf}}\sum_{t\ge1}B_D(t)e(tJ\sqrt D),
 \qquad
 B_D(t)=L^{3/2}(Dt^2)^{-3/4}C_L(Dt^2)
 \mathbf 1_{Dt^2\asymp L^2}.
\tag{R161.P1}
\]

Write the literal product support as

\[
 B_D(t)\ne0\quad\Longrightarrow\quad
 c_-L^2\le Dt^2\le c_+L^2
\tag{R161.P2}
\]

for fixed \(0<c_-<c_+\). The only positive inputs used in this review
are

\[
 \sum_{D,t}|B_D(t)|^2\ll L^2\log(2L),
 \qquad
 \sum_t|B_D(t)|\ll_\varepsilon
 \left(1+\frac L{\sqrt D}\right)L^\varepsilon.
\tag{R161.P3}
\]

No lower envelope for the literal coefficients, no density of nonzero
profile values, no common row vector, no Diophantine condition on \(J\),
and no near-collision estimate is assumed. For the diagnostic only, fix
\(0<a<b\) inside an ambient interval allowed by (R161.P2), and put

\[
 \mathscr D_L=\{D\in(aL^2,bL^2]:D>1\text{ squarefree}\},
 \qquad Q_L=\#\mathscr D_L.
\tag{R161.P4}
\]

Membership in \(\mathscr D_L\) is coarse support, not an assertion that
the physical coefficient \(B_D(1)\) is nonzero there.

## 3. Independent derivation of the normalization and norm/power ledger

### The literal \(t=1\) face

In the exact incidence coordinates, \(t=guv=1\) forces
\(g=u=v=1\). Hence \(h=d_1\), \(m=d_2\), and \(d_1d_2=D\). Since \(D\)
is squarefree, \(d_1,d_2\) are automatically squarefree and coprime. The
odd-height condition is \(d_1\) odd, and the exact integer cone is
\(d_2\le d_1\le4d_2\). Therefore

\[
\begin{aligned}
B_D(1)={}&\mathbf 1_{D\asymp L^2}L^{3/2}D^{-3/4}
\sum_{\substack{d_1d_2=D\\d_1\ {\rm odd}\\d_2\le d_1\le4d_2}}
 \chi_4(d_1)\eta_L(d_1)
 \Phi\!\left(\frac{d_1}{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xd_1}{4d_2}}\right).
\end{aligned}
\tag{R161.P5}
\]

This agrees with (161.J10), (3.6), and (161.K4), since
\(L^{3/2}D^{-3/4}=(L^2/D)^{3/4}\). If \(D\) is even, its factor \(2\)
must lie in \(d_2\); no even-\(D\) layer has been deleted. For
\(D=pq\), \(p<q\le4p\), the ordered pair \((d_1,d_2)=(q,p)\) is the only
cone-eligible nontrivial factorization. This shows that an individual
literal coefficient can lack internal divisor cancellation when the
profiles are nonzero; it gives no count or lower mass of such
coefficients.

### Squarefree row count and global energy

The elementary identity

\[
 \sum_{n\le x}\mu^2(n)
 =\sum_{r\le\sqrt x}\mu(r)\left\lfloor\frac{x}{r^2}\right\rfloor
 =\frac{x}{\zeta(2)}+O(\sqrt x)
\]

gives

\[
 Q_L=\frac{b-a}{\zeta(2)}L^2+O_{a,b}(L)\asymp L^2.
\tag{R161.P6}
\]

This is the correct ambient count for the adversarial one-column test.
It must not be reinterpreted as the number of nonzero physical
\(B_D(1)\)'s.

The map \(n\leftrightarrow(D,t)\), \(n=Dt^2\), is bijective on
nonsquares. On (R161.P2),

\[
 \left|L^{3/2}n^{-3/4}\right|^2=L^3n^{-3/2}\asymp1.
\]

Consequently the accepted product energy has exactly the normalization

\[
 \sum_{D>1\ {\rm sf}}\sum_t|B_D(t)|^2
 \ll\sum_n|C_L(n)|^2
 \ll L^2\log(2L),
\tag{R161.P7}
\]

with no multiplicity or missing \(L,J,H,X\) factor. In particular,
\(\|B_\bullet(1)\|_2\ll L\sqrt{\log(2L)}\).

### Evaluation operator, projective norm, and phase alignment

For finite row and column sets define

\[
 (E_Jc)(D)=\sum_t c(t)e(tJ\sqrt D),
 \qquad
 \Lambda_J(A)=\sum_{D,t}A_D(t)e(tJ\sqrt D).
\]

If \(A=\sum_r x_r\otimes c_r\), Cauchy--Schwarz after the common-test
evaluation gives

\[
 |\Lambda_J(A)|
 \le \|E_J\|_{2\to2}\sum_r\|x_r\|_2\|c_r\|_2.
\]

Taking the infimum over all Hilbert tensor decompositions gives exactly
the trace/nuclear norm:

\[
 |\Lambda_J(A)|\le\|E_J\|_{2\to2}\|A\|_{S_1}.
\tag{R161.P8}
\]

On the \(t=1\) restriction over \(\mathscr D_L\),

\[
 E_J^{(1)}a=(a e(J\sqrt D))_{D\in\mathscr D_L},
 \qquad \|E_J^{(1)}\|=Q_L^{1/2}\asymp L,
\tag{R161.P9}
\]

independently of every spacing or collision property. Set

\[
 A_D(t)=\mathbf1_{D\in\mathscr D_L}\mathbf1_{t=1}e(-J\sqrt D).
\tag{R161.P10}
\]

Then \(A=x\otimes e_1\), so

\[
 \|A\|_{S_1}=\|x\|_2=Q_L^{1/2}\asymp L,
 \qquad
 \Lambda_J(A)=Q_L\asymp L^2.
\tag{R161.P11}
\]

Thus (R161.P8) is sharp on this one-column array. The array has global
squared energy \(Q_L\asymp L^2\) and rowwise \(\ell^1\)-mass one, so it
obeys the scales in (R161.P3).

The same obstruction survives if a proposed coefficient-uniform theorem
is restricted to real arrays. Write
\(\theta_D=2\pi J\sqrt D\). Since
\(\sum_D\cos^2\theta_D+\sum_D\sin^2\theta_D=Q_L\), choose
\(b_D=\cos\theta_D\) when the cosine-square sum is at least \(Q_L/2\),
and \(b_D=\sin\theta_D\) otherwise. Then \(|b_D|\le1\) and

\[
 \left|\sum_{D\in\mathscr D_L}b_De(J\sqrt D)\right|\ge Q_L/2.
\tag{R161.P12}
\]

This closes a possible reality loophole without claiming that either
diagnostic has the physical incidence (R161.P5).

For the actual column, positive outer Cauchy gives only

\[
 \left|\sum_D B_D(1)e(J\sqrt D)\right|
 \le Q_L^{1/2}\|B_\bullet(1)\|_2
 \ll L^2\sqrt{\log(2L)}.
\tag{R161.P13}
\]

The target is \(L^{3/2}X^\varepsilon\). Hence this orientation exceeds
the target \(L\)-scale by
\(L^{1/2}\sqrt{\log(2L)}=L^{1/2+o(1)}\). After the logarithm is absorbed
in the conventional epsilon loss, the exact polynomial power still to
save is \(L^{1/2}\), equivalently \(L^{1/2-o(1)}\) uniformly against the
allowed epsilon loss. A positive one-column closure would require the
new estimate \(\|B_\bullet(1)\|_2\ll L^{1/2}X^\varepsilon\),
equivalently squared energy \(\ll L^{1+o(1)}\) at the \(L\)-power level,
or a direct signed substitute. Neither follows from (R161.P3). For a
fixed polynomial relation \(L=X^\theta\), \(\theta>0\), this missing
\(L^{1/2}\) cannot be absorbed into an \(X^\varepsilon\) statement
uniformly for every \(\varepsilon>0\).

### The \(D\le CL\) scope

For fixed \(C>0\), the channel bound gives

\[
\begin{aligned}
 \left|\sum_{D\le CL\ {\rm sf}}\sum_tB_D(t)e(tJ\sqrt D)\right|
 &\le L^\varepsilon\sum_{D\le CL}
 \left(1+\frac L{\sqrt D}\right)\\
 &\ll_C L^{3/2}L^\varepsilon
 \ll_{C,\varepsilon}L^{3/2}X^\varepsilon.
\end{aligned}
\tag{R161.P14}
\]

By (R161.P2), \(t\ge\tau\sqrt L\) implies
\(D\le c_+\tau^{-2}L\), while \(D\le CL\) implies
\(t\ge\sqrt{c_-/C}\sqrt L\). This proves an owner-complete long-channel
sector. It leaves \(D\gg L,\ t\ll\sqrt L\), including
\(t=1,D\asymp L^2\), for every growing polynomial block. Therefore it
is not a strict polynomial range for the full scalar, and the stricter
margin for \(D\le L^{1-\delta}\) is likewise only a sector margin.

## 4. First doubtful or unproved line

The first unproved **physical** line is exactly candidate (161.J14):

\[
 \boxed{
 \left|\sum_{D\asymp L^2\ {\rm sf}}
 B_D(1)e(J\sqrt D)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.}
\tag{R161.P15}
\]

No assigned artifact proves (R161.P15). The accepted energy yields only
(R161.P13), exact collision sparsity is irrelevant to a one-coordinate
test, and a singleton factorization gives no family lower mass. The
candidate correctly presents (161.J14) as open. The first impermissible
inference would be to turn the aligned diagnostic (161.J12)/(R161.P10)
into a lower bound for (R161.P15); the candidate explicitly does not make
that inference.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Literal \(t=1\) coefficient | **Green.** (R161.P5) recomputes the exact factor, cone, profiles, support, zero extension, and even-\(D\) routing. |
| Squarefree count | **Green, diagnostic only.** \(Q_L\asymp L^2\) by (R161.P6); it is not a physical nonzero-coefficient count. |
| Global energy normalization | **Green.** The radical map is bijective and the weight squared is \(\asymp1\), giving (R161.P7) with no restored power. |
| Evaluation/projective/nuclear ledger | **Green.** The projective infimum is \(S_1\), the one-column evaluation norm is exactly \(Q_L^{1/2}\), and (R161.P11) saturates their product. |
| Diagnostic phase alignment | **Green as a route control.** Both complex exact alignment and the real cosine/sine variant give \(L^2\) capacity; neither is the literal coefficient. |
| Missing \(L^{1/2}\) | **Green.** \(L^{2+o(1)}\) versus \(L^{3/2+o(1)}\) leaves exactly \(L^{1/2-o(1)}\) to save after epsilon losses. |
| Physical lower bound | **Rejected.** No density, sign alignment, or lower energy for (R161.P5) is proved. |
| \(D\le CL\) owner | **Green as a sector only.** It does not satisfy the owner-complete strict-polynomial-range exit gate. |
| Optimistic dyadic flat model (161.K6)--(161.K7) | **Diagnostic only.** It is conditional on a flat rank-one common-test model and is not a theorem about the literal matrix or a new range. |
| Downstream and exponent scope | **Green quarantine.** No conclusion passes to the remaining hard-TOP sector, terminal TOP, BAL, UNBAL, all M9-M2, M9-M1, M9, the bridge, or either global exponent. |

No numerical, metric-in-\(J\), or source theorem input was used.

## 6. Dependencies and exact artifacts used

This independent review used only:

- protocol.md;
- state/active_campaign.yml;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/barrier_packet.md;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reports/literal_radical_frequency_attack.md;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/reports/blind_radical_frequency_rederivation.md;
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/candidates/conductor_round161_radical_control_and_obstruction.md; and
- rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/controls/conductor_round161_radical_capacity_controls.md.

The source-auditor report was neither read nor anticipated. The
squarefree asymptotic, energy transfer, tensor norm identity, one-column
operator norm, phase alignment, and power comparison were recomputed in
this review.

## 7. Recommended state effect

Retain, subject to the other independent seams, the exact \(t=1\)
formula, the global-energy normalization, the \(D\le CL\) long-channel
sector, and the coefficient-uniform common-test/projective obstruction.
Record the obstruction explicitly as route-scoped and keep the literal
estimate (R161.P15), all few-point channels with \(D\gg L\), and all near
collisions open.

Do not promote a full target, an exit-gate strict polynomial range, a
physical lower bound, a source theorem, a downstream owner, or any Gauss
circle exponent. The appropriate decision for this seam is **GREEN for
hard_top_radical_frequency_coupling_no_go**, with (161.J14) as the first
doubtful/unproved physical line.
