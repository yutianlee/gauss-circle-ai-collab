# Round 130 statement-only report: outer bilinear dual feasibility

## 1. Result: sharp statement-only no-go

Let \(R\asymp LD\), and absorb the divisor/\(\eta\) losses already allowed by the statement into \(Y^{o(1)}\). The proposed positive energy

\[
E_{\rm out}:=\sum_r |F_r|^2\ll LD\,Y^\varepsilon
\]

and the scalar target \(|\mathcal O|\ll D Y^\varepsilon\) do **not** follow from the supplied support, pointwise, and outer-coefficient facts. The exact outer dual has an unrestricted phase-matching vector, and the exact energy Gram tests the prescribed constant increment mode. A product-window, phase-aligned control satisfying all explicit count, support, coefficient-energy, divisor-incidence, and size data has

\[
E_{\rm out}=LDK^2,
\qquad
|\mathcal O|=DK.
\]

Thus the known \(DK\) capacity returns unchanged after outer Cauchy/duality. This is a no-go for every proof using only the displayed hypotheses; it is not a counterexample to the undisclosed literal arithmetic kernel.

For the literal family, the sharp missing property is one of the following genuinely new statements:

\[
\sum_r|F_r|^2\ll RY^\varepsilon
\tag{energy property}
\]

or, for the weaker scalar route, with \(u_r=L A_r e(\gamma_r)\) and \(v_r=F_r/K\),

\[
\left|\sum_r u_rv_r\right|\ll \frac{R}{K}Y^\varepsilon.
\tag{actual-coefficient correlation property}
\]

The latter is the exact \(K^{-1}\) phase-correlation defect needed for the target and is strictly weaker than positive energy. More generally, a bound \(|\sum_r u_rv_r|\ll R K^{-\sigma}\) gives \(|\mathcal O|\ll D K^{1-\sigma}\); any fixed \(\sigma>0\) is a strict saving, and \(\sigma=1\) reaches \(D\).

## 2. Exact statement and hypotheses

For each ray put

\[
I_r=\{(p,\rho,\eta):p\in P_r,\ \rho\mid a_r+p,\ \eta\text{ admissible}\}.
\]

Choose a common column set \(\Xi\) containing all these labels and define the literal incidence matrix

\[
H_{r,\xi}=\begin{cases}
S_{r,p,\rho,\eta},&\xi=(p,\rho,\eta)\in I_r,\\
0,&\text{otherwise}.
\end{cases}
\]

All determinant tapers, characters, congruences, threshold data, and shell ownership are understood to remain inside these actual entries. If \({\bf 1}\) denotes the prescribed all-ones column vector (equivalently, the fixed weights can be absorbed into \(H\)), then

\[
F=H{\bf 1}.
\]

The exact positive-energy Gram is

\[
G_E=H^*H,
\qquad
(G_E)_{\xi,\zeta}=\sum_r\overline{H_{r,\xi}}H_{r,\zeta},
\qquad
E_{\rm out}={\bf 1}^*G_E{\bf 1}.
\tag{2.1}
\]

Equivalently, if atoms are labelled disjointly by \((r,\xi)\), this is a block-diagonal Gram whose \(r\)-block is

\[
G^{(r)}_{\xi,\zeta}=\overline{S_{r,\xi}}S_{r,\zeta};
\]

each such block has rank at most one. These two labelling conventions give the same quadratic value in (2.1).

The exact outer dual is

\[
E_{\rm out}
=\sup_{\|c\|_2=1}\left|c^*H{\bf 1}\right|^2,
\tag{2.2}
\]

and, when \(F\ne0\), the maximizing vector is \(c=F/\|F\|_2\). Hence every phase of \(F_r\) is absorbed by the dual optimizer. There is no signed cancellation between distinct outer rays in the positive energy.

Set \(a_r=A_re(\gamma_r)\) and \(b_r=\overline{a_r}\). Then

\[
\mathcal O=b^*H{\bf 1},
\qquad
|\mathcal O|^2={\bf 1}^*H^*bb^*H{\bf 1}.
\tag{2.3}
\]

Thus scalar control tests the rank-one projector \(bb^*\), whereas positive energy tests the identity. Since

\[
bb^*\preceq \|b\|_2^2 I,
\qquad
\|b\|_2^2\ll D/L,
\]

(2.1) at scale \(LD\) implies

\[
|\mathcal O|^2\le (D/L)E_{\rm out}\ll D^2Y^\varepsilon.
\]

The converse is false for one fixed \(b\): an arbitrarily large component of \(F\) orthogonal to \(b\) is invisible to (2.3).

## 3. Proof and derivation

The formulas (2.1)--(2.3) follow by expanding \(F_r=\sum_{\xi}H_{r,\xi}\), applying the elementary identity \(\|F\|_2=\sup_{\|c\|_2=1}|c^*F|\), and expanding the scalar square. No arbitrary replacement kernel is used in this calculation.

The supplied complete pointwise capacity is \(|F_r|\ll K Y^{o(1)}\). Therefore the strongest energy conclusion available without a new correlation statement is

\[
E_{\rm out}\ll RK^2Y^{o(1)}\asymp LDK^2Y^{o(1)}.
\tag{3.1}
\]

Outer Cauchy returns exactly the old bound:

\[
|\mathcal O|
\le \|A\|_2\|F\|_2
\ll (D/L)^{1/2}(LDK^2)^{1/2}Y^{o(1)}
=DKY^{o(1)}.
\tag{3.2}
\]

At \(D=Y^{1/2}\), \(L=Y^{1/6}\), and \(K=Y^{11/48+o(1)}\),

\[
R=LD=Y^{2/3},\qquad
LDK^2=Y^{9/8+o(1)},\qquad
DK=Y^{35/48+o(1)}.
\]

The desired energy is only \(Y^{2/3+\varepsilon}\), so (3.1) misses by \(K^2=Y^{11/24+o(1)}\); the scalar misses by \(K=Y^{11/48+o(1)}\).

For the promised false control, take integer model scales with \(R=LD\), let every \(P_r=\{1,\ldots,L\}\), retain only \(\rho=1\) (which always divides \(a_r+p\)) and one \(\eta=\eta_0\), and choose

\[
A_r=L^{-1}e(-\gamma_r),
\qquad
S_{r,p,1,\eta_0}=K/L.
\tag{3.3}
\]

Then

\[
\sup_r|A_r|=L^{-1},qquad
\sum_r|A_r|^2=R/L^2=D/L,qquad
F_r=K.
\]

Consequently

\[
E_{\rm out}=RK^2=LDK^2,
\qquad
\mathcal O=\sum_r L^{-1}K=DK.
\tag{3.4}
\]

The corresponding product-window matrix is

\[
H=(K/L){\bf 1}_R{\bf 1}_L^T,
\qquad
H^*H=(RK^2/L^2)J_L.
\]

Its only nonzero Gram eigenvalue is \(RK^2/L\), and the prescribed constant increment mode gives

\[
{\bf 1}_L^*H^*H{\bf 1}_L=RK^2.
\]

This is the exact product-window resonance. Phase variants of (3.3) align \(F_r\) with any saturated permitted coefficient vector. The control is deliberately not asserted to realize the undisclosed threshold/plateau arithmetic formula; it proves that counts, individual bounds, incidence, and coefficient energy alone cannot yield either target. A literal-family proof must identify the extra arithmetic fact that excludes this constant-mode alignment.

Finally, unit-Hessian geometry by itself gives no contraction. Let \(q\ge1\), \((a,q)=1\), \(e_q(t)=e^{2\pi i t/q}\), and

\[
C_a(x,y)=e_q(axy),\qquad x,y\in\mathbb Z/q\mathbb Z.
\]

For the unitary two-dimensional Fourier normalization

\[
(\mathcal F_2 C_a)(u,v)
=q^{-1}\sum_{x,y\bmod q}C_a(x,y)e_q(-ux-vy),
\]

orthogonality in \(x\) gives the exact identity

\[
(\mathcal F_2 C_a)(u,v)=e_q(-a^{-1}uv).
\tag{3.5}
\]

The phase Hessian is \(\left(\begin{smallmatrix}0&a\\a&0\end{smallmatrix}\right)\), with determinant \(-a^2\), a unit modulo \(q\). Applying the same transform again returns \(C_a\). Thus a sequential unit-Hessian transform sends a full product chirp to another full product chirp of the same modulus and preserves its \(\ell^2\) capacity exactly. In matrix language, the normalized transforms multiply on the left and right by unitaries, so singular values and Frobenius energy are unchanged. Any unnormalized square-root gain is repaid by the dual support length. Additional nonresonance, zero-mode removal, or actual-weight orthogonality is indispensable.

## 4. First doubtful or unproved step

The first unavailable step is any claim of a \(K^{-1}\) contraction of the actual constant increment mode or actual outer coefficient projection. In exact terms, the statement supplies no estimate improving either

\[
{\bf 1}^*H^*H{\bf 1}\ll RK^2Y^{o(1)}
\]

to \(\ll RY^\varepsilon\), or

\[
|b^*H{\bf 1}|\ll DKY^{o(1)}
\]

to \(\ll DY^\varepsilon\). The words “exact finite Stieltjes-threshold reciprocal sum” do not provide an auditable correlation identity in the permitted statement. Inferring cancellation from signs, mixed curvature, or a second transform before writing such an identity is therefore the first doubtful step.

For positive energy, outer-ray signs cannot repair this gap because (2.2) phase-matches them. Only cancellation or smallness inside the actual row sums \(F_r\), averaged in \(r\), can prove the energy assertion. For the scalar, outer cancellation can suffice, but it must be proved specifically against the actual \(A_re(\gamma_r)\).

## 5. Control tests and outcomes

1. **`outer_l2_dual_or_Gram`.** Input: the literal incidence matrix \(H\). Outcome: (2.1) and (2.2) are exact; the dual optimizer is phase matched. Implication: positive outer energy has no cross-ray signed saving.

2. **`phase_aligned_false_control`.** Input: (3.3), with one legal divisor \(\rho=1\) and one \(\eta\). Outcome: (3.4) saturates both \(LDK^2\) and \(DK\). Implication: the displayed quantitative hypotheses are insufficient. This is a control model, not an asserted member of the undisclosed literal family.

3. **`outer_ray_and_increment_counts`.** Input: \(R=LD\), \(|P_r|=L\). Outcome: there are \(LD\) rays and \(L^2D\) ray-increment incidences; the saturated coefficient energy is \((LD)L^{-2}=D/L\). All capacities in (3.4) have the stated normalization.

4. **`scalar_vs_positive_energy`.** Input: compare (2.1) with (2.3). Outcome: energy replaces the rank-one projector \(bb^*\) by the identity and is strictly stronger for a fixed actual coefficient vector. Implication: failure of a generic energy proof does not rule out a direct signed scalar proof.

5. **`unit_Hessian_sequential_transform_return`.** Input: the full product chirp \(C_a\). Outcome: (3.5) is another unit-modulus product chirp, and a second transform returns the original. Implication: unit Hessian/nondegeneracy alone is norm preserving, not a source of a fixed-power contraction.

6. **`capacity_before_and_after`.** Input: \(|F_r|\ll K\), \(\|A\|_2^2\ll D/L\), \(R=LD\). Outcome: triangle gives \((R/L)K=DK\), while outer duality gives \((D/L)^{1/2}(RK^2)^{1/2}=DK\). Implication: exact capacity self-return.

7. **`no_exponent_or_M9_promotion`.** Outcome: no Gauss-circle exponent, M9 statement, or quarter theorem follows. The report establishes only a statement-level obstruction and the exact extra correlation scale required.

## 6. Dependencies and exact artifacts used

- `rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/briefs/blind_outer_bilinear_dual_feasibility.md`
- `rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/blind_statement.md`
- `state/control_models.md`
- `problems/gauss_circle.md`

No strategy file, proof-state file, nonblind Round-95--130 artifact, sibling report, web source, or numerical computation was used.

## 7. Recommended state effect

**Retain** the exact dual/Gram calculation and the phase-aligned/product-window/unit-Hessian controls as a quantitative obstruction. **Reject** promotion of the generic “outer duality or sequential transform gives the missing \(K\)” mechanism from the supplied hypotheses. **Revise** any positive route so that it proves either the actual-family energy constant-mode bound \({\bf 1}^*H^*H{\bf 1}\ll LDY^\varepsilon\) or the strictly weaker actual-coefficient correlation bound \(|\sum_r u_rv_r|\ll (LD/K)Y^\varepsilon\). No graph or shared-state edit is recommended from this statement-only report.
