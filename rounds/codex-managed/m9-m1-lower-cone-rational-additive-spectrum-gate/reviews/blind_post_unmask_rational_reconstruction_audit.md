# 1. Result

**Overall verdict: GREEN.**

The repaired conductor candidate passes all six requested seams. The former phase-value/slope RED is closed by (142.C24a), which replaces the unproved neighborhood-density wording with the exact integrality separation. The new reconstruction formulas (142.C19c)--(142.C19f) also pass: the twisted Ramanujan--Gauss identity, every sign and factor in the hard cutoff, the denominator-Abel normalization, the limit to \(\sigma_{\chi _4}=r_2/4\), and the unchanged \(\chi _4\)-negative odd-part residual are correct.

\[
\begin{array}{c|c}
\text{seam}&\text{verdict}\\ \hline
\text{(i) rational rows, signs, constant, uniform error}&\mathrm{GREEN}\\
\text{(ii) fixed-height DFT and limiting coefficient}&\mathrm{GREEN}\\
\text{(iii) finite residual, spectral norms, and exact reconstruction}&\mathrm{GREEN}\\
\text{(iv) moving-boundary wedge capacity}&\mathrm{GREEN}\\
\text{(v) local cells, Farey overlap, residual norm, and slope distinction}&\mathrm{GREEN}\\
\text{(vi) scope, branchwise qualification, and no-lower-bound wording}&\mathrm{GREEN}
\end{array}
\tag{R1}
\]

No mathematical repair is required. Two qualifications already implicit in the candidate should remain explicit: the \(\eta>0\) series is absolutely convergent after summing each complete numerator set at fixed denominator, and (142.C26) is a stationary principal-family identity, not a branchwise endpoint/remainder theorem.

# 2. Exact statements and hypotheses audited

The audit uses reduced rational frequencies \(a/q\), the strict cone conditions \(4h^2<M\) and \(4h<r\le M/h\), and the half-open dyadic block \(M\le m<2M\).

The previously audited formulas remain:

\[
S_C(M;a/q)
=\mathbf 1_{4\mid q}\frac{i\pi\chi _4(a)}{2q}M
+O\bigl((\sqrt M+q)\log(2q)\bigr),
\tag{R2}
\]

\[
g_h(m)
=-\frac{i}{2h}
\sum_{\substack{b\ ({\rm mod}\ 4h)\\b\ {\rm odd}}}
\chi _4(b)e\left(\frac{bm}{4h}\right),
\tag{R3}
\]

and

\[
\widehat P_H(a/q)
=-\frac{2i\chi _4(a)}{q}
\sum_{\substack{t\le 4H/q\\t\ {\rm odd}}}
\frac{\chi _4(t)}{t}
=-\frac{i\pi\chi _4(a)}{2q}+O(H^{-1}).
\tag{R4}
\]

For the new reconstruction seam, set

\[
\mathcal G_d(m)
=\sum_{\substack{c\ ({\rm mod}\ 4d)\\(c,4d)=1}}
\chi _4(c)e\left(\frac{cm}{4d}\right).
\tag{R5}
\]

The exact identities under review are

\[
\mathcal G_d(m)
=2i\sum_{\ell\mid(d,m)}
\ell\,\mu(d/\ell)\chi _4(d/\ell)\chi _4(m/\ell),
\tag{R6}
\]

\[
P_Q(m)
=\frac{\pi}{4}\sum_{\ell\mid m}\chi _4(m/\ell)
\sum_{\substack{k\le Q/(4\ell)\\k\ {\rm odd}}}
\frac{\mu(k)\chi _4(k)}{k},
\tag{R7}
\]

and, with complete numerator sums taken before the denominator sum,

\[
\begin{aligned}
P_\eta(m)
&=\sum_{d\ge1}d^{-\eta}\frac{i\pi}{8d}\mathcal G_d(-m)\\
&=\frac{\pi}{4L(1+\eta,\chi _4)}
\sum_{\ell\mid m}\chi _4(m/\ell)\ell^{-\eta},
\qquad \eta>0.
\end{aligned}
\tag{R8}
\]

The claimed pointwise denominator-Abel limit is

\[
\lim_{\eta\downarrow0}P_\eta(m)
=\sum_{\ell\mid m}\chi _4(m/\ell)
=\sigma_{\chi _4}(m)
=\frac{r_2(m)}{4}.
\tag{R9}
\]

# 3. Proof and seam audit

## 3.1 Rational rows and fixed-height DFT — GREEN

The identity

\[
\chi _4(r)=\frac{e(r/4)-e(-r/4)}{2i}
\tag{R10}
\]

gives row means \(+i/2\) at \(ah/q\equiv1/4\) and \(-i/2\) at \(ah/q\equiv-1/4\). Such a row exists exactly when \(4\mid q\). For \(q=4Q\), the classes \(h\equiv Q,3Q\pmod{4Q}\) have respective means

\[
\frac{i}{2}\chi _4(a),\qquad -\frac{i}{2}\chi _4(a).
\tag{R11}
\]

The reciprocal-row Gregory sum is

\[
\frac{i\chi _4(a)}{2Q}
\left(1-\frac13+\frac15-\cdots\right)
=\frac{i\pi\chi _4(a)}{2q},
\tag{R12}
\]

while the lower-boundary sum, the upper floor, and incomplete periods contribute \(O((\sqrt M+q)\log(2q))\). The endpoint \(h<\sqrt M/2\) remains strict. Thus (142.C2), its signs, and its all-\(q\) error are GREEN.

For (R3), writing \(b=c+4u\), \(c\in\{1,3\}\), makes the \(u\)-sum vanish unless \(h\mid m\). If \(m=hr\), the complete numerator sum is

\[
h\bigl(e(r/4)-e(3r/4)\bigr)=2ih\chi _4(r).
\tag{R13}
\]

Multiplication by \(-i/(2h)\) proves the DFT sign. A reduced positive mode \(a/q\) occurs when \(q=4Q\) and \(h=qt/4\) with \(t\) odd; its contribution is

\[
-\frac{i}{2(qt/4)}\chi _4(at)
=-\frac{2i\chi _4(a)}{q}\frac{\chi _4(t)}{t},
\tag{R14}
\]

which proves (142.C18). Its limiting positive-frequency coefficient is the conjugate of the plus-sign correlation in (142.C2).

## 3.2 Twisted Ramanujan--Gauss identity — GREEN

Because \(\chi _4(c)\) already vanishes for even \(c\), the unit condition in (R5) may be written as \((c,d)=1\). Möbius inversion gives

\[
\mathcal G_d(m)
=\sum_{k\mid d}\mu(k)
\sum_{\substack{c\ ({\rm mod}\ 4d)\\k\mid c}}
\chi _4(c)e\left(\frac{cm}{4d}\right).
\tag{R15}
\]

Only odd \(k\) survive. Put \(D=d/k\) and \(c=kb\). Complete multiplicativity on odd arguments gives

\[
\chi _4(k)
\sum_{b\ ({\rm mod}\ 4D)}
\chi _4(b)e\left(\frac{bm}{4D}\right).
\tag{R16}
\]

Splitting \(b\) modulo \(4\) and modulo \(D\), the inner sum is zero unless \(D\mid m\); when \(D\mid m\), it equals

\[
D\sum_{r\ ({\rm mod}\ 4)}
\chi _4(r)e\left(\frac{r(m/D)}4\right)
=2iD\chi _4(m/D).
\tag{R17}
\]

Substitution of \(k=d/D\), followed by the renaming \(D=\ell\), proves (R6). The factor \(2i\), the argument \(m/\ell\), and the factor \(\ell\) are all correct. Terms with even \(d/\ell\) vanish because \(\chi _4(d/\ell)=0\).

## 3.3 Hard cutoff, denominator-Abel limit, and radial self-return — GREEN

In the negative-frequency projection, write \(q=4d\). Since

\[
\mathcal G_d(-m)=-2i
\sum_{\ell\mid(d,m)}
\ell\,\mu(d/\ell)\chi _4(d/\ell)\chi _4(m/\ell),
\tag{R18}
\]

the \(d\)-level contribution is

\[
\frac{i\pi}{8d}\mathcal G_d(-m)
=\frac{\pi}{4d}
\sum_{\ell\mid(d,m)}
\ell\,\mu(d/\ell)\chi _4(d/\ell)\chi _4(m/\ell).
\tag{R19}
\]

Putting \(d=\ell k\) yields exactly (R7): the cutoff is \(k\le Q/(4\ell)\), the constant is \(\pi/4\), and the sign is positive. The restriction to odd \(k\) is redundant but correct because \(\chi _4(k)=0\) for even \(k\).

With the damping \(d^{-\eta}\), the same substitution gives

\[
P_\eta(m)
=\frac{\pi}{4}
\sum_{\ell\mid m}\chi _4(m/\ell)\ell^{-\eta}
\sum_{k\ge1}\frac{\mu(k)\chi _4(k)}{k^{1+\eta}}.
\tag{R20}
\]

For every fixed \(m\) and \(\eta>0\), the last series is absolutely convergent and equals

\[
\frac1{L(1+\eta,\chi _4)}.
\tag{R21}
\]

Thus (142.C19f) is exact. This absolute convergence is denominator-level convergence after the complete numerator sum \(\mathcal G_d(-m)\) has been taken. The sum of the absolute values of all individual rational branches would require \(\eta>1\); the candidate's term “denominator-Abel” correctly fixes the grouping and does not contradict (142.C19).

Since \(L(1,\chi _4)=\pi/4\), the prefactor in (R8) tends to one, and the divisor sum is finite. Therefore

\[
\lim_{\eta\downarrow0}P_\eta(m)
=\sum_{d\mid m}\chi _4(d)
=\sigma_{\chi _4}(m).
\tag{R22}
\]

The standard signed-divisor formula \(r_2(m)=4\sum_{d\mid m}\chi _4(d)\) gives \(r_2(m)/4\). Hence the denominator-Abel reconstruction returns the complete radial coefficient, not the truncated cone coefficient \(C\).

If \(m=2^\nu n\) with \(n\) odd and \(\chi _4(n)=-1\), then

\[
\sigma_{\chi _4}(m)=\sum_{d\mid n}\chi _4(d)=0.
\tag{R23}
\]

Indeed, the involution \(d\mapsto n/d\) reverses the character sign; equivalently, some prime \(p\equiv3\pmod4\) occurs to an odd exponent and its local divisor sum vanishes. Consequently

\[
\bigl(C-\sigma_{\chi _4}\bigr)(m)=C(m)
\tag{R24}
\]

on the stated negative-character odd-part set. The claim that this owner is unchanged is exact.

## 3.4 Finite residual, spectral norms, and wedge — GREEN

Distinct reduced rationals \(a/q\ne b/s\) are separated by at least \(1/(qs)\). Thus the off-diagonal geometric sums in (142.C19b) cost \(O(qs)\), or \(O(s)\) after their \(1/q\) coefficient. Summation over \(O(Q^2)\) reduced modes gives \(O(sQ^2)\). Every fixed omitted \(4\mid s\) retains its nonzero linear mean.

Orthogonality gives

\[
\sum_{4\mid q\le Q}\sum_{(a,q)=1}|A(a/q)|\asymp Q,
\qquad
\sum_{4\mid q\le Q}\sum_{(a,q)=1}|A(a/q)|^2\asymp\log Q.
\tag{R25}
\]

These are norm obstructions, not pointwise lower bounds.

The moving-boundary wedge is exactly

\[
M\le m<2M,\qquad M\le4h^2<m=hr,\qquad r\ {\rm odd}.
\tag{R26}
\]

It has \(\asymp M\) incidences: \(h\) ranges over a proportional subinterval of \([\sqrt M/2,\sqrt{M/2})\), and a fixed interior subinterval has \(\asymp\sqrt M\) odd \(r\)'s on each of \(\asymp\sqrt M\) rows. Multiplication by \(m^{-3/4}\asymp M^{-3/4}\) proves the unsigned capacity \(\asymp M^{1/4}\), hence \(R^{1/2}\) at \(M\asymp R^2\).

## 3.5 Local cells, repaired slope distinction, and stationary return — GREEN

The exact powers are

\[
|\Phi''(m)|\asymp R^2M^{-3/2},\qquad
L_M\asymp\frac{M^{3/4}}R,\qquad
K_M\asymp\frac{R^2}{\sqrt M}.
\tag{R27}
\]

Dirichlet height \(Q_M\asymp L_M\) covers slope arcs of width \(L_M^{-1}\). Farey separation gives raw overlap

\[
O\left(1+\frac{Q_M^2}{L_M}\right)=O(L_M).
\tag{R28}
\]

There are \(O(1+M/L_M)\) half-open cells. After the \(M^{-3/4}\) weight, absolute assembly costs \(R/\sqrt M\), so the required short-interval residual norm is \(X^\varepsilon\sqrt M/R\). The available \(\sqrt M\)-sized rational error loses a factor \(R\). The singleton transition is \(M\asymp R^{4/3}\). All powers and endpoint conventions are correct.

The repaired phase-value statement is also exact. If \(\Phi'(m)=u/q\) at an integer \(m\), then \(Nq^2=4mu^2\), so \(q^2\mid4m\) and \(\Phi(m)=2mu/q\in\mathbb Z\). For a nonresonant integer, equality is impossible, while

\[
\left|\Phi'(m)-\frac uq\right|
=\frac{|Nq^2-4mu^2|}
{4mq^2(\Phi'(m)+u/q)}
\ge
\frac1{4mq^2(\Phi'(m)+u/q)}.
\tag{R29}
\]

Near the relevant slope this is only \(\gg(q^2\sqrt{NM})^{-1}\), far smaller than \(L_M^{-1}\). Thus the repaired candidate makes no density claim and proves exactly the needed non-implication.

For the principal stationary family, with \(z=4hk-b\),

\[
x_k=\frac{4Nh^2}{z^2},\qquad
\Phi(x_k)+\frac{b}{4h}x_k-kx_k=\frac{Nh}{z},
\tag{R30}
\]

and

\[
x_k^{-3/4}|\Phi''(x_k)|^{-1/2}=2N^{-1/4}.
\tag{R31}
\]

Multiplication by the exact DFT coefficient \(-i\chi _4(b)/(2h)\), the negative-curvature factor \(e(-1/8)\), and \(\chi _4(z)=-\chi _4(b)\) gives the exact coefficient

\[
\frac{iN^{-1/4}e(-1/8)}h,
\tag{R32}
\]

of size \(\asymp(hR)^{-1}\), exactly as in the repaired (142.C26). The candidate continues to label this only as the stationary principal family and explicitly refuses to inherit the reassembled endpoint/remainder ledger branch by branch. There is no branchwise \(B\)-process overclaim.

## 3.6 Scope and no-lower-bound language — GREEN

The candidate labels spectral mass, wedge incidence, and branch capacity as norm, unsigned, or principal-family capacities. None is used as a signed fixed-centre lower bound. The denominator-Abel identity is a pointwise reconstruction statement about the grouped rational modes, not a bound for the nonlinear scalar. The frozen scalar (142.C28), every periodic masked branch estimate, the local residual theorem, and all downstream M1, M2, M9, endpoint, bridge, circle, and exponent obligations remain open.

# 4. First doubtful or unproved step

There is no remaining defect in the conductor candidate requiring repair. The first genuinely unproved mathematical step is still the short-interval residual estimate

\[
\max_{\substack{q\le Q_M,\ (a,q)=1\\J\subset[M,2M),\ |J|\le L_M}}
\left|\sum_{m\in J}D(m)e(am/q)\right|
\ll_\varepsilon X^\varepsilon\frac{\sqrt M}{R},
\tag{R33}
\]

together with target-safe estimates for the masked periodic branches and the moving-boundary reconstruction residual. Formula (142.C19f) does not close this step: it reconstructs \(\sigma_{\chi _4}\), not \(C\), and it leaves the \(\chi _4\)-negative odd-part cone exactly unchanged.

Likewise, (142.C26) supplies only the algebra of the stationary principal family. Its endpoint and remainder estimates exist only after the accepted reassembly; they have not been proved for individual branches.

# 5. Control tests and outcomes

1. **Reduced \(q\bmod4\), row classes, and signs — GREEN.** Nonzero mean occurs exactly for \(4\mid q\); the classes \(Q,3Q\pmod{4Q}\), their signs, and the constant \(i\pi\chi _4(a)/(2q)\) are correct.
2. **Uniform \(q\)-error and strict endpoints — GREEN.** The error \((\sqrt M+q)\log(2q)\), the relative-asymptotic range, the upper floor, lower \(4h+1\), and strict \(h<\sqrt M/2\) are retained.
3. **Fixed-height DFT — GREEN.** The coefficient \(-i/(2h)\), reduced-mode aggregation, conjugate limiting coefficient, and every factor of \(2\) and \(q\) are correct.
4. **Twisted Gauss identity — GREEN.** Equation (142.C19d) has the correct \(2i\), divisor condition, Möbius factor, characters, and even-term vanishing.
5. **Hard cutoff and Abel reconstruction — GREEN.** The sign \(+\), factor \(\pi/4\), cutoff \(Q/(4\ell)\), reciprocal \(L\)-factor, \(\ell^{-\eta}\), and limit \(r_2/4\) are correct.
6. **Negative-character residual — GREEN.** If the odd part has \(\chi _4=-1\), then \(\sigma_{\chi _4}=0\), so the residual remains exactly \(C\).
7. **Finite projection and spectral norms — GREEN.** The \(sQ^2\) error, absolute mass \(Q\), and square mass \(\log Q\) are correct and are not scalar lower bounds.
8. **Wedge capacity — GREEN.** The exact moving region and weighted capacity \(M^{1/4}\), hence \(R^{1/2}\) at the top scale, are correct.
9. **Local geometry and repaired slope distinction — GREEN.** Cell length, arc width, Farey overlap, residual norm, singleton threshold, and (142.C24a) all pass.
10. **Stationary coefficient and branchwise error scope — GREEN.** The exact coefficient is \(iN^{-1/4}e(-1/8)/h\); only its size is \(\asymp(hR)^{-1}\). No branchwise remainder is claimed.
11. **Downstream scope — GREEN.** No estimate of the frozen scalar or downstream theorem/exponent is promoted.

# 6. Dependencies and exact artifacts used

This final post-unmask audit used only:

- rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/candidates/conductor_round142_rational_spectrum_self_return.md;
- rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/reports/blind_rational_slope_cell_rederivation.md;
- the prior version of rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/reviews/blind_post_unmask_rational_reconstruction_audit.md.

No sibling report, graph file, state file, synthesis, control artifact, plan, strategy file, numerical experiment, or web source was read or used.

# 7. Recommended state effect

**GREEN: retain as obstruction evidence.** The repaired conductor candidate may retain (142.C2), (142.C6), (142.C12), (142.C16)--(142.C21), and (142.C22)--(142.C27), including the exact denominator-Abel completion self-return. Preserve two qualifications in any state patch: \(P_\eta\) is grouped by complete numerator sets at each denominator, and (142.C26) carries no separately inherited branchwise endpoint/remainder estimate.

The rational-mode mechanism still does not prove (142.C28) or provide an owner-complete strict reduction. Make no signed lower-bound claim and no downstream theorem or exponent change.
