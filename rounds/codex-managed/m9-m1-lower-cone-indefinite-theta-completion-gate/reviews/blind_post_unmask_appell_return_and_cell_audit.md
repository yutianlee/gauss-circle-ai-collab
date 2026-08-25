# 1. Result: lemma and seam verdict

**Verdict: GREEN on the completion normalization and reciprocal saddle constant; GREEN with an aggregate-owner qualification on the Round-140 self-return; REVISE on the claim that no strict survivor follows.**

Let

\[
\mathcal H(\tau)=\frac12\widehat A_4(1/2,-3\tau;2\tau).
\]

The two nonblind reports have the exact scalar normalization:

\[
\boxed{
\mathcal H(\tau)
=F(\tau)+\frac14+\mathcal R_{\rm cone}(\tau)
=F(\tau)+\frac14+\sum_{k=0}^3\mathcal R_k(\tau),
}
\tag{R144.1}
\]

\[
\boxed{
\mathcal H(\gamma\tau)
=\chi_4(d)(c\tau+d)\mathcal H(\tau)
\qquad(\gamma\in\Gamma_0(4)).
}
\tag{R144.2}
\]

Here the single completed-kernel correction from the independent cone calculation is exactly

\[
\mathcal R_{\rm cone}(\tau)
=\frac14\sum_{\substack{h,r\in\mathbb Z\\r\ {\rm odd}}}
\chi_4(r)
\left[
E\!\left(\frac{(r-4h)\sqrt y}{2}\right)
-\operatorname {sgn}(r-4h)
\right]e(hr\tau),
\tag{R144.3}
\]

and, in the Appell convention used by the reports,

\[
\mathcal R_k(\tau)
=\frac{i}{4}(-1)^k
\vartheta\!\left((2k-3)\tau+\frac32;8\tau\right)
R_{\rm Zw}\!\left(\frac12+(3-2k)\tau;8\tau\right).
\tag{R144.4}
\]

There is no missing factor, sign, fifth correction, residue, or extra cusp term. The \(1/4\) in (R144.1) is separate and compulsory: it is half of the bilateral Appell zero term \(1/2\).

The exact character-Poisson formula in the discovery report also has the correct outer \(i/2\). Its positive-\(j\) saddle inside the braces is

\[
\frac{2N^{-1/4}}{h}
V_{\rm low}\!\left(\frac{4R^2h^2}{j^2}\right)
\psi_M\!\left(\frac{4Nh^2}{j^2}\right)
e(Nh/j-1/8),
\tag{R144.5}
\]

so multiplication by \(i/2\) gives

\[
\boxed{
e(1/8)N^{-1/4}
\frac{\chi_4(j)}{h}
V_{\rm low}\!\left(\frac{4R^2h^2}{j^2}\right)
\psi_M\!\left(\frac{4Nh^2}{j^2}\right)e(Nh/j).
}
\tag{R144.6}
\]

This is exactly inverse to the accepted Round-140 forward factor
\(e(-1/8)N^{1/4}\). Thus the smooth full cone returns to the reciprocal scalar at the level of the principal family. It is owner-complete only after the accepted Round-140 and Round-141 global ledgers are reassembled; no termwise identification of the four Appell corrections with individual aliases or remainders is justified.

The no-bound conclusion remains correct. However, the accepted Round-141 statement that the elementary displacement count exhausts its target-safe range at \(|j_m|=\sqrt M\) is not sharp. Averaging the already accepted root bound over the displacement gives

\[
\boxed{
\#\{m\in\mathcal I_M:0<|k_m^2-Nm|\le J\}
\ll_\varepsilon N^\varepsilon J
}
\qquad(1\le J<N),
\tag{R144.7}
\]

throughout \(M\ll N^{1/2}\). Consequently the current scalar has the strictly smaller owner-complete survivor

\[
\boxed{
\mathfrak T_N
=\sum_M\sum_{\substack{m\in\mathcal I_M\\
|k_m^2-Nm|>M^{3/4}}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(\sqrt{Nm})
+O_{\varepsilon,V}(X^\varepsilon).
}
\tag{R144.8}
\]

Thus no strict **automorphic** survivor follows from the completion, but a strict arithmetic phase-value survivor does follow from the sharper displacement average. No \(X^\varepsilon\) bound for (R144.8) follows.

# 2. Exact statement and hypotheses

Use \(e(t)=e^{2\pi it}\), \(q=e(\tau)\), \(y=\Im\tau\), and

\[
F(\tau)=\sum_{m\ge1}C(m)q^m,\qquad
C(m)=\sum_{\substack{hr=m,\ r\ {\rm odd}\\r>4h}}\chi_4(r).
\tag{R144.9}
\]

For the lattice comparison, take the even unimodular plane

\[
Q(h,r)=hr,\qquad
B((h,r),(h',r'))=hr'+rh',
\tag{R144.10}
\]

with negative vector \(c_1=(1,-4)\), isotropic vector \(c_0=(0,-1)\), and additive characteristic \(b_0=(1/4,0)\). Then

\[
B(c_1,(h,r))=r-4h,\qquad
B(c_0,(h,r))=-h,
\tag{R144.11}
\]

\[
\chi_4(r)=
\frac{e(B((h,r),b_0))-e(-B((h,r),b_0))}{2i}.
\tag{R144.12}
\]

The reports' level-four coset lattice
\(\mathbb Z(1,0)\oplus\mathbb Z(0,4)\), with signed cosets \(r\equiv1,3\pmod4\), is the equivalent coset encoding of (R144.12). The unimodular/additive-character encoding is useful for checking the scalar multiplier; the level-four/discriminant encoding is useful for displaying the finite characteristic orbit. They do not give different completed objects.

With the standard Zwegers definitions of \(\vartheta\) and \(R_{\rm Zw}\), the exact comparison asserted in (R144.1) is

\[
\boxed{
\sum_{k=0}^3
\frac{i}{4}(-1)^k
\vartheta\!\left((2k-3)\tau+\frac32;8\tau\right)
R_{\rm Zw}\!\left(\frac12+(3-2k)\tau;8\tau\right)
=\mathcal R_{\rm cone}(\tau).
}
\tag{R144.13}
\]

For every \(w\in C_c^\infty((0,\infty))\), the coefficient transform under review is

\[
\begin{aligned}
\sum_{m\ge1}C(m)w(m)
={}&\frac12\sum_{h\ge1}w(4h^2)\\
&+\frac i2\sum_{h\ge1}\sum_{j\ne0}\chi_4(j)
\left\{
\frac1h\int_{4h^2}^{\infty}
w(u)e\!\left(-\frac{ju}{4h}\right)\,du
-\frac{2w(4h^2)}{\pi i j}
\right\}.
\end{aligned}
\tag{R144.14}
\]

The bracketed double sum is absolutely convergent. The displayed half-boundary and harmonic subtraction are legal only in the stated symmetric recombination.

For the displacement statement, let

\[
\mathcal I_M=[M,2M)\cap[1,M_*],\qquad
M_*\ll N^{1/2},\qquad
k_m=\left\lfloor\sqrt{Nm}+\frac12\right\rfloor,
\qquad j_m=k_m^2-Nm.
\tag{R144.15}
\]

The range \(k_m<N\) holds for all sufficiently large active \(N\); bounded \(X\) is absorbed. Formula (R144.7) applies to any \(J<N\). For (R144.8), \(J=M^{3/4}\le N^{3/8}<N\), so all hypotheses are uniform. Exact radicals \(j_m=0\) retain the accepted separate parametrization \(m=Dt^2\) when \(N=Du^2\), \(D\) squarefree.

# 3. Proof or derivation

## 3.1 Scalar multiplier and four-term correction

The independent completed cone replaces
\(\operatorname {sgn}(r-4h)\) by
\(E((r-4h)\sqrt y/2)\) and retains the isotropic sign with Appell/Abel regularization. Its correction is (R144.3). Absolute convergence follows from

\[
e^{-\pi y(r-4h)^2/4}|q^{hr}|
=e^{-\pi y(r^2/4+4h^2)}.
\tag{R144.16}
\]

In the completed Appell formula, substitute

\[
\ell=4,\qquad z=\frac12,\qquad w=-3\tau,\qquad \tau_{\rm A}=2\tau.
\]

Then \(\zeta^k=(-1)^k\), the theta argument is
\((2k-3)\tau+3/2\), both moduli are \(8\tau\), and the \(R\)-argument is
\(1/2+(3-2k)\tau\). The Appell correction has coefficient \(i/2\); the outer factor \(1/2\) defining \(\mathcal H\) changes it to \(i/4\). This proves (R144.4) with all four indices.

Expanding each \(R_{\rm Zw}\), multiplying by its theta factor, and grouping the four residue classes of the odd difference \(r-4h\pmod8\) gives (R144.13). The sign-minus-error convention in \(R_{\rm Zw}\), the theta phase, and \(i(-1)^k\) combine to the error-minus-sign convention in (R144.3). No term remains after the four residue classes are reassembled.

For the scalar law, the characteristic pair is the difference
\((0,b_0)-(0,-b_0)\). Under
\(\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\), it moves to
\((cb_0,db_0)-( -cb_0,-db_0)\). If \(4\mid c\), then \(cb_0\in L\), and
\[
db_0\equiv
\begin{cases}
b_0\pmod L,&d\equiv1\pmod4,\\
-b_0\pmod L,&d\equiv3\pmod4.
\end{cases}
\]
Because \(Q(b_0)=0\), there is no residual characteristic phase. The odd difference acquires \(\chi_4(d)\), and the rank-two completed kernel contributes weight factor \(c\tau+d\). This independently proves (R144.2) and agrees with the nonblind arbitrary-matrix Appell calculation.

## 3.2 Exact outer \(i/2\), boundary, and saddle

For a suitable test \(f\), period-four Poisson summation gives

\[
\sum_{r\in\mathbb Z}\chi_4(r)f(r)
=\frac i2\sum_{\substack{j\in\mathbb Z\\j\ {\rm odd}}}
\chi_4(j)\widehat f(j/4).
\tag{R144.17}
\]

This follows directly from
\[
\frac14\{e(j/4)-e(3j/4)\}=\frac i2\chi_4(j)
\quad(j\ {\rm odd}).
\]
Apply (R144.17) to the one-sided function
\(f(r)=\mathbf1_{r>4h}w(hr)\). Its Fourier transform gives the integral in (R144.14), with outer \(i/2\).

Integration by parts at \(u=4h^2\) gives

\[
\frac1h\int_{4h^2}^{\infty}
w(u)e(-ju/(4h))\,du
=\frac{2w(4h^2)}{\pi i j}+O_w(j^{-2}).
\tag{R144.18}
\]

Subtracting the leading term makes the \(j\)-sum absolute. Since

\[
\sum_{j\ne0}\frac{\chi_4(j)}j
=2L(1,\chi_4)=\frac\pi2,
\tag{R144.19}
\]

the subtraction, after multiplication by \(i/2\), contributes
\(-\tfrac12w(4h^2)\), exactly cancelling the separately displayed half-boundary. This verifies every constant in (R144.14).

For
\[
w_M(u)=u^{-3/4}V_{\rm low}(R^2u/N)\psi_M(u)e(\sqrt{Nu}),
\]
the positive-\(j\) phase is
\[
\phi_{h,j}(u)=\sqrt{Nu}-\frac{ju}{4h},\qquad
u_0=\frac{4Nh^2}{j^2},\qquad
\phi_{h,j}(u_0)=\frac{Nh}{j}.
\tag{R144.20}
\]
Here \(\phi''(u_0)<0\), so the Gaussian unit is \(e(-1/8)\). Moreover,
\[
u_0^{-3/4}|\phi''(u_0)|^{-1/2}=2N^{-1/4}.
\tag{R144.21}
\]
Equations (R144.20)--(R144.21) give (R144.5), and
\[
\frac i2\cdot2e(-1/8)=i\,e(-1/8)=e(1/8),
\tag{R144.22}
\]
which proves (R144.6). Thus there is neither a missing factor \(2\) nor a cosine replacement.

## 3.3 Scope of the owner-complete Round-140 return

The accepted Round-140 global relation, followed by the accepted Round-141 floor/cell restoration, has the aggregate form

\[
\mathcal S_{\rm recip}^+
=e(-1/8)N^{1/4}\mathcal S_{\rm cone}^+
+O_{\varepsilon,V}(RX^\varepsilon).
\tag{R144.23}
\]

Solving this proved scalar equivalence gives

\[
\boxed{
\mathcal S_{\rm cone}^+
=e(1/8)N^{-1/4}\mathcal S_{\rm recip}^+
+O_{\varepsilon,V}(X^\varepsilon),
}
\tag{R144.24}
\]

which is exactly the factor found independently in (R144.6). Round 140 owns, after complete reassembly, its literal floors, half endpoint, collar, entry/exit, negative aliases, profile crossings, nonstationary modes, and stationary remainders. Round 141 owns the global floor-to-cone and phase-cell restoration.

This validates the discovery report's self-return claim only in the aggregate sense (R144.24). It does not prove that an individual Appell correction \(\mathcal R_k\) equals a particular negative alias, endpoint, or stationary remainder. It also does not let a rational branch inherit the reassembled Round-140 error term; the accepted Round-142 adjudication correctly limits that statement to principal-symbol self-return branchwise.

Thus the two nonblind conclusions are compatible:

- the exact global character-Poisson transform returns to the accepted reciprocal owner;
- the modular/Appell identity by itself gives no estimate for the completed pairing and four correction pairings.

## 3.4 Sharper displacement count and strict survivor

The accepted prime-power argument gives, for nonzero \(j\),

\[
\rho_N(j):=\#\{k\pmod N:k^2\equiv j\pmod N\}
\ll_\varepsilon N^\varepsilon\sqrt{(N,j)}.
\tag{R144.25}
\]

Round 141 replaced \(\sqrt{(N,j)}\) pointwise by \(j^{1/2}\) and summed, producing \(J^{3/2}\). Averaging the gcd before discarding it is sharper:

\[
\begin{aligned}
\sum_{1\le j\le J}\sqrt{(N,j)}
&\le
\sum_{1\le j\le J}\sum_{d\mid(N,j)}\sqrt d\\
&=
\sum_{\substack{d\mid N\\d\le J}}\sqrt d\,
\left\lfloor\frac Jd\right\rfloor
\le
J\sum_{d\mid N}d^{-1/2}
\ll_\varepsilon JN^\varepsilon.
\end{aligned}
\tag{R144.26}
\]

The same bound holds for negative \(j\). Since \(k_m<N\) and
\(m=(k_m^2-j_m)/N\), the map \(m\mapsto k_m\) injects the fixed-\(j\) set into these residue roots. Equations (R144.25)--(R144.26) prove (R144.7).

On \(m\asymp M\), use \(|C(m)|\le d(m)\ll_\varepsilon X^\varepsilon\). The weighted contribution of
\(0<|j_m|\le J\) is

\[
\ll_{\varepsilon,V}M^{-3/4}JX^\varepsilon.
\tag{R144.27}
\]

Choosing \(J=M^{3/4}\) makes (R144.27) target-safe on every block; logarithmically many blocks are absorbed by epsilon renaming. The accepted exact-radical estimate handles \(j_m=0\). Comparing this wider deletion with the original \(|j_m|\le\sqrt M\) deletion proves (R144.8).

This refinement changes the phase-value window from
\[
\|\sqrt{Nm}\|\ll N^{-1/2}
\]
to the larger dyadic scale
\[
\|\sqrt{Nm}\|\ll \frac{M^{1/4}}{\sqrt N}.
\tag{R144.28}
\]
This is a phase-value statement and cannot be compared directly with a derivative-cell width. For the one special slope induced by the nearest integer \(k_m\), the exact algebra is
\[
\left|\frac{k_m}{2m}-\Phi'(m)\right|
=\frac{|k_m-\sqrt{Nm}|}{2m}
=\frac{|j_m|}{2m(k_m+\sqrt{Nm})}
\asymp\frac{|j_m|}{m\sqrt{Nm}}.
\tag{R144.29}
\]
On the retained survivor \(|j_m|>M^{3/4}\), \(m\asymp M\), this yields only
\[
\left|\frac{k_m}{2m}-\Phi'(m)\right|
\gg \frac1{R^2M^{3/4}}.
\tag{R144.30}
\]
Relative to the derivative-cell width
\(L_M^{-1}\asymp R/M^{3/4}\), the ratio is merely \(R^{-3}\). Moreover \(k_m/(2m)\) is one specially induced rational slope; (R144.30) says nothing about proximity to an arbitrary Farey slope \(u/q\). Thus the accepted Round-142 phase-value-versus-slope obstruction survives unchanged.

## 3.5 No bound follows

The strict survivor (R144.8) removes at most \(O(M^{3/4}X^\varepsilon)\) nonzero-displacement points from a length-\(M\) block. Its coefficient-blind block capacity remains
\[
\sum_{m\asymp M}m^{-3/4}|C(m)|
\ll_\varepsilon M^{1/4+\varepsilon},
\tag{R144.31}
\]
which is \(R^{1/2+\varepsilon}\) at \(M\asymp R^2\). The reciprocal principal family retains normalized absolute capacity \(R\). The four Appell corrections remain compulsory correlated owners. None of these capacities is a signed lower bound, but none supplies the desired upper bound.

# 4. First doubtful or unproved step

After the sharper cell deletion, the first unproved estimate can be stated strictly as

\[
\boxed{
\sum_M\sum_{\substack{m\in\mathcal I_M\\
|k_m^2-Nm|>M^{3/4}}}
m^{-3/4}V_{\rm low}(R^2m/N)C(m)e(+\sqrt{Nm})
\ll_{\varepsilon,V}X^\varepsilon.
}
\tag{R144.32}
\]

Equivalently, after globally restoring the wider target-safe cells and using the accepted Round-140/141 aggregate relation, the first unproved estimate is still the signed reciprocal bound

\[
\mathcal S_{\rm recip}^+\ll_{\varepsilon,V}RX^\varepsilon
\tag{R144.33}
\]

with its literal floors, collar, half endpoint, entry/exit, subtraction, negative aliases, and remainder ledger.

The first invalid analytic step would be one of:

1. using real-analytic modularity as a coefficient estimate;
2. dropping or separately bounding an \(\mathcal R_k\) without a correlated theorem;
3. treating the principal saddle match as a branchwise remainder theorem;
4. replacing the \(+\) direction by a cosine;
5. retaining the Round-141 assertion that the same root-count method stops at \(J=\sqrt M\).

# 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| exact \(\Gamma_0(4)\) multiplier | **Pass.** The Appell shift calculation and the independent additive-character stabilizer both give weight \(1\) and \(\chi_4(d)\), with no extra phase. Generator checks \(T\), \(\left(\begin{smallmatrix}1&0\\4&1\end{smallmatrix}\right)\), and \(-I\) agree. |
| four-term/single-kernel normalization | **Pass analytically.** Substitution into the completed \(A_4\) formula gives \(i/4\), four indices, arguments and modulus \(8\tau\); exact reindexing gives (R144.3). Any numerical truncations are excluded from accepted evidence. |
| isotropic boundary | **Pass.** The bilateral zero term is \(1/2\), hence \(1/4\) in \(\mathcal H\). It is not part of the four \(R\)-terms and cannot be omitted. |
| coefficient-transform boundary normalization | **Pass.** Equations (R144.18)--(R144.19) show exact cancellation of the half-boundary and harmonic subtraction in symmetric order. |
| outer \(i/2\) and individual direction | **Pass.** Period-four Poisson gives \(i/2\); negative curvature gives \(e(-1/8)\); their product gives \(e(1/8)\), with no factor two and no conjugate averaging. |
| Round-140 owner return | **Pass with qualification.** Equation (R144.24) is an owner-complete global target-equivalence. It is not a termwise Appell-correction or rational-branch identity. |
| sharper nonzero-displacement count | **Pass analytically.** Gcd averaging gives \(O_\varepsilon(JN^\varepsilon)\), including squareful \(N\); exact radicals are kept separate. Numerical checks are excluded from accepted evidence. |
| Round-142 slope distinction | **Pass unchanged.** Equations (R144.29)--(R144.30) compare the induced special slope, not the phase value, with the derivative width; the relative separation is only \(R^{-3}\), and arbitrary Farey slopes remain uncontrolled. |
| target estimate | **Open.** Neither completion, reciprocal return, wider cell deletion, nor rational reconstruction proves (R144.32). |

The accepted evidence is 100 percent analytical. Numerical checks are excluded from the campaign evidence and from every promotion recommendation.

# 6. Dependencies and exact artifacts used

The review used:

1. protocol.md;
2. rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reports/blind_cone_automorphy_feasibility.md;
3. rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reports/indefinite_theta_source_hypothesis_audit.md;
4. rounds/codex-managed/m9-m1-lower-cone-indefinite-theta-completion-gate/reports/indefinite_theta_lattice_completion_attack.md;
5. rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/reports/exact_tail_poisson_alias_connector.md;
6. rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/candidates/conductor_round140_smoothed_far_alias_reduction.md;
7. rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/reviews/conductor_round140_height_alias_adjudication.md;
8. rounds/codex-managed/m9-m1-lower-post-collar-height-alias-gate/synthesis.md;
9. rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/candidates/conductor_round141_cone_nonresonant_reduction.md;
10. rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/reviews/conductor_round141_incomplete_fibre_adjudication.md;
11. rounds/codex-managed/m9-m1-lower-far-alias-incomplete-fibre-dispersion-gate/synthesis.md;
12. rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/candidates/conductor_round142_rational_spectrum_self_return.md;
13. rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/reviews/conductor_round142_rational_spectrum_adjudication.md;
14. rounds/codex-managed/m9-m1-lower-cone-rational-additive-spectrum-gate/synthesis.md.

No proof graph, proof draft, validation matrix, campaign synthesis, or shared state was edited. No external source was needed for the seam decisions. The completion and displacement controls were independently rederived analytically. Numerical checks are excluded from accepted evidence.

# 7. Recommended state effect

1. **Retain/promote the exact normalization:** (R144.1)--(R144.4), including the scalar weight-one \(\Gamma_0(4)\) law with nebentypus \(\chi_4\), the separate \(1/4\) isotropic boundary, and all four \(i/4\) theta--\(R_{\rm Zw}\) terms. Record explicitly that their sum equals the single cone error-kernel correction (R144.3).

2. **Retain the reciprocal self-return with narrower wording:** the outer \(i/2\), saddle unit, and inverse factor \(e(1/8)N^{-1/4}\) are exact. The full owner return is the aggregate target-equivalence (R144.24), inherited only after complete Round-140/141 reassembly. Do not identify individual Appell corrections or rational branches with individual Round-140 owners.

3. **Promote the sharper displacement lemma and strict survivor:** replace the nonzero count \(O_\varepsilon(N^\varepsilon J^{3/2})\) by (R144.7), and add the target-equivalent survivor (R144.8) with threshold \(M^{3/4}\).

4. **Revise, but do not invalidate, Round 141:** its \(\sqrt M\)-window reduction is correct, but the statements that this width exhausts the elementary root-count method and that no wider target-safe conclusion follows are false after gcd averaging. The Round-142 phase/slope, rational reconstruction, and capacity obstructions remain valid.

5. **Retain the terminal no-go and all downstream open status:** no fixed-centre bound follows. Leave (R144.32)/(R144.33), lower GAR, both direct M1 parents, M9-M1, all M2 owners, endpoint uniformity, M9, the bridge, and the quarter theorem open. The strict survivor is arithmetic progress, not an automorphic estimate.
