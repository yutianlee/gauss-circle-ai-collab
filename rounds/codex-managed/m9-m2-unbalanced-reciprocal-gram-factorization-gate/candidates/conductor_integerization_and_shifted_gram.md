# Conductor candidate: movable integer centre and shifted signed Gram

Campaign: `m9-m2-unbalanced-reciprocal-gram-factorization-gate`

Starting graph SHA-256:
`d29ae6c0f398cc2df699b15ee2901b525290263b6cde5eecece49cdeee095bb1`

Status: conductor candidate pending independent and hostile review.

## 1. Physical-kernel integerization lemma

For an integer \(M\) with \(|M-X|\leq U\), keep every amplitude frozen at
the original real parameter \(X\), and define

\[
 \mathscr R_M^\sharp=
 \sum_{r\ {\mathrm{odd}}}\chi_4(r)W(X/(rD))
 \sum_k{q_L(4Xk/r^2)\over k}e(Mk/r).
\tag{123.C1}
\]

The coefficientwise product identity gives

\[
 \mathscr R_M^\sharp=
 \sum_{r\ {\mathrm{odd}}}\chi_4(r)W(X/(rD))
 \sum_d\mathcal Q_L\!\left({r(M-rd)\over4X}\right)
\tag{123.C2}
\]

with the same normalization and rapidly decaying tail as the accepted
real-centred identity. Smoothness at scale \(L\) gives, for every fixed
\(A\),

\[
 |\mathcal Q_L'(y)|\ll_A
 L(1+L|y|)^{-A}.
\tag{123.C3}
\]

Integrating the centre from \(X\) to \(M\), using \(r\asymp X/D\),
and grouping \(rd=n\) gives

\[
\begin{aligned}
 |\mathscr R_X-\mathscr R_M^\sharp|
 &\ll_A {UL\over D}
 \sup_{C\in[X-U,X+U]}
 \sum_{r,d}\left(1+{|C-rd|\over D/L}\right)^{-A}\\
 &\ll_{A,\varepsilon} {UL\over D}
 \sum_{n\ne0}\tau(|n|)\left(1+{|C-n|\over D/L}\right)^{-A}
 +O_A\!\left({ULR\over D}(1+X/(D/L))^{-A}\right)\\
 &\ll_{A,\varepsilon} U X^\varepsilon.
\end{aligned}
\tag{123.C4}
\]

The last line is uniform because \(D/L>X^{1/4}\) and the weighted real
interval has length \(O(D/L)\). This proves the phase-only perturbation
through the physical kernel. A reciprocal-row termwise triangle would
instead cost as much as \(UK\) and is not the proof.

Two choices are therefore lawful:

- the nearest odd integer \(M\), with \(U\leq1\); or
- an odd multiple of \(Q=2^q\asymp X^{1/4}\), with
  \(U\ll Q\) and therefore \(v_2(M)=q\), at the cost of the full
  target allowance.

## 2. Unshifted Gram and exact aliases

Put

\[
 B_k=\sum_{r\ {\mathrm{odd}}}\chi_4(r)W(X/(rD))
 q_L(4Xk/r^2)e(Mk/r).
\]

Weighted Cauchy gives

\[
 |\mathscr R_M^\sharp|^2
 \ll \mathcal G_M:=\sum_{k\asymp K}{|B_k|^2\over k}.
\tag{123.C5}
\]

The literal diagonal of \(\mathcal G_M\) is \(O(R)\), and is
\(\asymp R\) on a nondegenerate interior cell. Since
\(R=X/D>X^{1/2}\), the sufficient estimate
\(\mathcal G_M\ll X^{1/2+\varepsilon}\) is strictly stronger than the
scalar target and cannot follow from an absolute off-diagonal bound.

For an alias \(j\) put

\[
 E=M(s-r)-jrs.
\]

Then

\[
 M(1/r-1/s)=j+E/(rs),\qquad
 (M-jr)(M+js)-M^2=jE.
\tag{123.C6}
\]

Smooth \(k\)-summation restricts the effective window to

\[
 |E|\ll X^{1+\varepsilon}/L,qquad |j|\ll D.
\tag{123.C7}
\]

If \(M=2^tM_0\), \(M_0\) odd, then

\[
 \chi_4(r)\chi_4(s)
 =(-1)^{(jrs+E)/2^{t+1}}.
\tag{123.C8}
\]

At an exact nonzero alias, \(E=0\) forces
\(2^{t+1}\mid j\). For \(j>0\), one has
\(M-jr>0\), \(M+js>0\), and their product is \(M^2\). Thus each fixed
nonzero \(j\) has \(O_\varepsilon(X^\varepsilon)\) exact pairs. Summing
\(|j|\ll D\) gives \(O_\varepsilon(DX^\varepsilon)\), which is within
the square target. Negative aliases follow by swapping \(r,s\). The
exception is \(j=0,E=0\), which is exactly the full diagonal \(r=s\).

For the nearest odd centre, even aliases satisfy the more explicit law

\[
 j\equiv E\equiv0\pmod2
 \quad\Longrightarrow\quad
 \chi_4(r)\chi_4(s)=(-1)^{j/2+E/2},
\tag{123.C9}
\]

whereas odd aliases have odd \(E\) and retain dependence on \(rs\bmod4\).
For a centre that is an odd multiple of \(Q=2^q\), the congruence
\(jrs+E\equiv0\pmod{2Q}\) is tautological: its quotient is
\(M_0(s-r)/2\). It does not by itself remove any near-collision pair.
The engineered two-adic centre thins exact aliases but supplies no proved
near-alias sparsity, while already consuming \(O(QX^\varepsilon)\) of the
target error.

## 3. Shifted Gram that prices the diagonal

The unshifted Gram may be too strong. Set

\[
 z_k={1\over k}\sum_{r\ {\mathrm{odd}}}\chi_4(r)W(X/(rD))
 q_L(4Xk/r^2)e(Mk/r),
\qquad \mathscr R_M^\sharp=\sum_k z_k.
\]

For \(1\leq H\leq cK\), shift invariance followed by Cauchy gives the
exact van der Corput form

\[
 |\mathscr R_M^\sharp|^2
 \ll {K\over H}
 \sum_{|h|<H}\left(1-{|h|\over H}\right)
 \sum_k z_{k+h}\overline{z_k}.
\tag{123.C10}
\]

The right side is real and nonnegative only after the full sum. Its
expanded phase is

\[
 e\!\left(Mk(1/r-1/s)+Mh/r\right),
\tag{123.C11}
\]

so the same \((j,E)\) factorization survives and the shift supplies an
additional reciprocal selector in \(M/r\).

Choose

\[
 H_0=\left\lceil{X^{1/2}\over D}\right\rceil.
\tag{123.C12}
\]

Then \(H_0\leq K\), because \(K/H_0\asymp X^{1/2}L/D>1\) in the strict
range. For \(r=s\), the \(h\)-sum is a smoothly perturbed Fejer kernel in
\(M/r\). The product-window layer cake gives

\[
 \sum_{r\asymp R}F_{H_0}(M/r)
 \ll_\varepsilon (R+H_0)X^\varepsilon.
\tag{123.C13}
\]

The variation of the shifted \(q_L\)-autocorrelation costs
\(RH_0/K=X^{1/2}/L\). Consequently the complete \(r=s\) sector of
(123.C10) is

\[
 \ll_\varepsilon
 \left({R\over H_0}+1+{RH_0\over K}\right)X^\varepsilon
 \ll_\varepsilon X^{1/2+\varepsilon}.
\tag{123.C14}
\]

Thus the shifted Gram removes the raw diagonal obstruction without using
the desired theorem.

## 4. Remaining capacity and first doubtful step

After \(k\)-localization and the \(h\)-selector, a flat-density heuristic
predicts off-diagonal capacity

\[
 {X\over LH}X^\varepsilon.
\tag{123.C15}
\]

At \(H=H_0\) this predicts \(X^{1/2}(D/L)X^\varepsilon\), still a
factor \(D/L\) above the square target. Formally increasing to
\(H\asymp K\) changes the same ledger to

\[
 {X\over LK}={D^2\over L^2}=\Delta^2,
\tag{123.C16}
\]

the square of the original product-window capacity. Since
\(\Delta=D/L>X^{1/4}\) in the strict residual region, this nominal value
is above \(X^{1/2}\). No joint arithmetic incidence theorem proving
(123.C15) is supplied, so (123.C15)--(123.C16) are diagnostics only, not
an upper bound, lower bound, or rigorous no-go.

The first unproved step is cancellation in the complete near-alias
off-diagonal with \(0<|E|\ll X^{1+\varepsilon}/L\), all aliases, literal
profile overlap, and the extra shift retained. The exact factorization and
defect sign expose that survivor but do not estimate it. A valid next
claim must prove a signed factor-lattice inequality or an inverse theorem;
it cannot infer the target from exact aliases, the target-safe shifted
diagonal, or the tautological two-adic congruence alone.

## 5. Scope

If reviewed successfully, (123.C4), the exact algebra (123.C6)--(123.C9),
the target-safe nonzero exact-alias sector, and the shifted-diagonal bound
(123.C14) are candidate flat-smooth lemmas. None proves the complete wave.
No conclusion follows for sharp, starred, clipped, hard, arithmetic-owner,
or transition packets, complete UNBAL, M9-M2, M9, the quarter theorem, or
any global exponent.
