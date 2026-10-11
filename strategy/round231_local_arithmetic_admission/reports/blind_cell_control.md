# Round 231: statement-only finite-cell control

## 1. Result

**Verdict: the isolated finite-cell statement is true for all sufficiently large T.** There is a purely analytical construction preserving every prescribed cell total, with a real peak of size at least a fixed positive multiple of T^(1/4) and a physical peak width of order T^(-1/2). Consequently its weighted twelfth moment is at least a fixed positive multiple of T^(5/2).

- Campaign: round231_local_arithmetic_admission.
- Task and role: blind_cell_control; statement-only independent rederivation.
- Generated: 2026-10-11 06:02:49 UTC.
- Starting graph SHA256, supplied as provenance only: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
- Context isolation: only the three files listed in Section 6 were read. No graph, state, history, sibling report, or external source was read.
- Computation: none; all controls below are analytical.

The underlying sufficient condition is slightly more general than the stated cell-count condition: if S_T is the total coefficient mass and m_C is the mass in cell C, it suffices that

$$
S_T-\sum_C\frac{\sum_{n\in C}c_n^2}{m_C}\gg T.
$$

The given hypotheses imply this because the subtracted quantity is at most K_T max_n c_n = o(T).

## 2. Exact statement and hypotheses

Let 0 < a < b be fixed, let

$$
I_T=\{n\in\mathbb Z:aT\le n\le bT\},\qquad
S_T=\sum_{n\in I_T}c_n,
$$

and suppose there are fixed constants s_0,s_1 > 0 such that s_0 T <= S_T <= s_1 T for all sufficiently large T. Assume c_n >= 0 and, for every fixed eta > 0, max_n c_n <= C_eta T^eta, with C_eta independent of T and n. Let v be the specified fixed real C^1 function, with 0 < v_min <= v <= v_max. Let the positive support be partitioned into K_T disjoint nonempty cells, fixed as R varies, with K_T <= T^(1-delta) for fixed delta > 0. Let J and w have the properties in the isolated statement.

Then there are real d_n and R_0/T in J such that

$$
|d_n|\le c_n/2,\qquad
\sum_{n\in C}d_n=0\quad\text{for every cell }C,
$$

and, for fixed positive constants A,rho,c independent of T and the partition,

$$
D_T(R_0)\ge A T^{1/4},\qquad
D_T(R)\ge \frac A2 T^{1/4}
\quad (|R-R_0|\le\rho T^{-1/2}),
$$

$$
\int_{\mathbb R}w(R/T)|D_T(R)|^{12}\,dR\ge cT^{5/2}.
$$

The same lower bound applies if the integral is taken only over positive R. The peak interval is positive for large T.

Constants may depend on the fixed data, including s_0,s_1,C_(delta/2),delta,a,b,v,J,w. The construction is uniform over all allowed partitions. No arithmetic identification of c_n or d_n is asserted.

Two minor qualifications to the literal hypotheses are worth recording. If delta > 1, the mass hypothesis and the cell-count hypothesis are eventually incompatible, so that parameter range is vacuous. Also, w need not have compact support as stated; the lower-bound integral is always defined as a nonnegative extended integral, but its finiteness does not follow. Compact support or an appropriate decay assumption would resolve the latter issue if a finite moment is intended. Neither qualification obstructs the asserted lower bound.

## 3. Proof and derivation

Choose a closed interval J_0 = [u,z] of positive length strictly inside J. Write ell = z-u and use the normalized radius average

$$
\langle f\rangle_T=\frac1{\ell T}\int_{uT}^{zT}f(R)\,dR.
$$

Define, without modifying either the square-root locations or the real phase,

$$
q_n(R)=v(n/T)\cos(2\pi R\sqrt n-3\pi/4),\qquad
h_n(R)=T^{-3/4}q_n(R).
$$

**Uniform two-frequency separation.** Direct integration gives, for lambda != 0,

$$
\left|\left\langle\cos(\lambda R+\theta)\right\rangle_T\right|
\le\frac2{\ell T|\lambda|}.
$$

Hence, uniformly for n in I_T,

$$
\langle q_n^2\rangle_T=\frac{v(n/T)^2}{2}+O(T^{-3/2}).
$$

For distinct n,m in I_T, the exact real product identity is

$$
q_n(R)q_m(R)=\frac{v(n/T)v(m/T)}2
\left[
\cos\bigl(2\pi R(\sqrt n-\sqrt m)\bigr)
+\cos\bigl(2\pi R(\sqrt n+\sqrt m)-3\pi/2\bigr)
\right].
$$

Since

$$
|\sqrt n-\sqrt m|
=\frac{|n-m|}{\sqrt n+\sqrt m}
\ge\frac{|n-m|}{2\sqrt{bT}},
$$

we obtain

$$
|\langle q_nq_m\rangle_T|
\le C\frac{T^{-1/2}}{|n-m|}+CT^{-3/2}
\le C'T^{-1/2}.
$$

In particular, for every distinct pair and all sufficiently large T,

$$
\left\langle(q_n-q_m)^2\right\rangle_T
\ge\frac{v(n/T)^2+v(m/T)^2}{2}-CT^{-1/2}
\ge\frac{v_{\min}^2}{2}.
\tag{1}
$$

This estimate is uniform even for adjacent integers and does not assume a spacing in n greater than one.

**Weighted variance surviving the cell constraints.** For a cell C let

$$
m_C=\sum_{n\in C}c_n>0,\qquad
\mu_C(R)=\frac1{m_C}\sum_{n\in C}c_nq_n(R),
$$

and define

$$
V(R)=\sum_C\sum_{n\in C}c_n\bigl(q_n(R)-\mu_C(R)\bigr)^2.
$$

The weighted pairwise variance identity gives exactly

$$
V(R)=\sum_C\frac1{2m_C}
\sum_{n,m\in C}c_nc_m(q_n(R)-q_m(R))^2.
\tag{2}
$$

Apply (1) to all distinct pairs in (2). Since the cells and their masses are fixed while R varies,

$$
\langle V\rangle_T
\ge\frac{v_{\min}^2}{4}
\left(S_T-Q_T\right),\qquad
Q_T:=\sum_C\frac{\sum_{n\in C}c_n^2}{m_C}.
\tag{3}
$$

With c_max = max_n c_n,

$$
Q_T\le\sum_C\frac{c_{\max}m_C}{m_C}
=K_Tc_{\max}
\le C_{\delta/2}T^{1-\delta/2}=o(T).
\tag{4}
$$

Therefore Q_T <= S_T/2 for all sufficiently large T, and

$$
\langle V\rangle_T\ge\frac{v_{\min}^2s_0}{8}T.
$$

V is continuous, so some R_0 in [uT,zT] satisfies this same lower bound.

**A fixed admissible perturbation.** Once that R_0 is selected, set

$$
d_n=\frac{c_n}{4v_{\max}}
\bigl(q_n(R_0)-\mu_C(R_0)\bigr)\quad(n\in C),
\tag{5}
$$

and set d_n = 0 whenever c_n = 0 or n is outside I_T. Because q_n and its weighted mean lie in [-v_max,v_max], (5) gives |d_n| <= c_n/2. Its sum in each cell is zero by the definition of mu_C.

Moreover,

$$
\begin{aligned}
D_T(R_0)
&=\frac{T^{-3/4}}{4v_{\max}}
\sum_C\sum_{n\in C}c_n
\bigl(q_n(R_0)-\mu_C(R_0)\bigr)q_n(R_0)\\
&=\frac{T^{-3/4}}{4v_{\max}}V(R_0)
\ge A T^{1/4},
\end{aligned}
$$

where one may take A = v_min^2 s_0/(32 v_max). The equality uses the exact zero weighted sum of q_n-mu_C in each cell.

**Physical width and moment.** The coefficients (5) are now constants as R varies. In particular, differentiating D_T does not differentiate d_n, R_0, or mu_C(R_0). From the literal phase,

$$
|h_n'(R)|\le2\pi v_{\max}\sqrt b\,T^{-1/4},
$$

and consequently

$$
|D_T'(R)|
\le2\pi v_{\max}\sqrt b\,T^{-1/4}\sum_n|d_n|
\le L_D T^{3/4},\qquad
L_D=\pi v_{\max}\sqrt b\,s_1.
$$

Take rho = A/(2L_D). On

$$
E_T=[R_0-\rho T^{-1/2},R_0+\rho T^{-1/2}],
$$

the mean-value bound gives D_T(R) >= (A/2)T^(1/4). As J_0 lies strictly inside J, E_T/T is contained in J for large T, and w(R/T)=1 there. Thus

$$
\int w(R/T)|D_T(R)|^{12}\,dR
\ge 2\rho T^{-1/2}(A/2)^{12}T^3
=2\rho(A/2)^{12}T^{5/2}.
\tag{6}
$$

The physical R-width is 2 rho T^(-1/2); the width in the rescaled coordinate R/T is 2 rho T^(-3/2).

**A sign giving a peak and moment for a nonnegative coefficient vector.** Let

$$
H_T(R)=\sum_nc_nh_n(R),\qquad
F_{\sigma,T}(R)=H_T(R)+\sigma D_T(R)
=\sum_n(c_n+\sigma d_n)h_n(R),\quad\sigma\in\{-1,1\}.
$$

Both coefficient vectors are nonnegative, indeed c_n + sigma d_n >= c_n/2, and both have exactly the original cell totals and total mass S_T. Since

$$
\max\{|H_T(R_0)+D_T(R_0)|,|H_T(R_0)-D_T(R_0)|\}
\ge D_T(R_0),
$$

choose a single sign sigma_* realizing that inequality. The nonnegative coefficients give the uniform derivative bound

$$
|F_{\sigma_*,T}'(R)|
\le2\pi v_{\max}\sqrt b\,s_1T^{3/4}.
$$

The same peak-width argument, with a possibly smaller fixed rho, proves that this very same sign has both |F_(sigma_*,T)(R_0)| >= A T^(1/4) and weighted twelfth moment at least c' T^(5/2). Choosing a peak sign and an integrated-moment sign independently is unnecessary.

**Appending an infinite baseline: precise additional requirements.** The isolated hypotheses specify only a finite wave, so no infinite series or its convergence has been supplied. To append an infinite baseline B_T, one must first define its coefficients and weights and justify an appropriate convergence mode. If one wants pointwise values, require convergence at the stated radii; local L^12 convergence is sufficient for an L^12 interpretation and finite local moments. A locally finite measurable baseline is enough for the following weaker, but useful, two-sign conclusion.

On the already constructed interval E_T, the elementary convexity identity gives, for every real finite B_T(R),

$$
|B_T(R)+D_T(R)|^{12}+|B_T(R)-D_T(R)|^{12}
\ge2|D_T(R)|^{12}.
\tag{7}
$$

Thus at least one fixed sign has its moment over E_T at least the right side of (6), even without a small-tail estimate. That sign also has essential peak at least (A/2)T^(1/4) somewhere in E_T. A pointwise representative gives a pointwise peak with, for example, the smaller constant A/4. This sign and peak radius need not be the ones selected from the finite wave at R_0.

If the stronger objective is to retain the sign chosen at the original radius and a whole interval of comparable height there, a quantitative local oscillation bound for the infinite baseline is needed for this argument. A sufficient condition is

$$
|B_T(R)-B_T(R_0)|\le L_B T^{3/4}|R-R_0|
$$

on a fixed multiple of the physical T^(-1/2) neighborhood, with L_B independent of T, and a finite real value B_T(R_0). Choose the sign at R_0 using B_T, then combine this bound with the bound for D_T. A derivative bound of the same order implies this condition. Alternatively, to preserve a previously selected finite-wave sign by adding a tail E_T^tail, it suffices that the tail be o(T^(1/4)) uniformly on that peak interval. For moment transfer alone, an L^12 norm o(T^(5/24)) on that interval suffices by the reverse triangle inequality. These tail estimates are sufficient alternatives, not consequences of the finite-cell hypotheses, and smallness is unnecessary for the sign-averaged existence result (7).

Finally, if the appended object is to be a nonnegative coefficient sequence, its baseline coefficients on I_T must actually be the c_n used here, or otherwise dominate |d_n| pointwise. The finite perturbation leaves coefficients outside I_T unchanged. Neither convergence nor compatibility with exact arithmetic coefficients follows from this construction.

## 4. First doubtful or unproved step

There is no unproved step in the finite-cell claim: (1) is a directly integrated trigonometric identity, (2) is weighted variance algebra, (4) follows from the stated pointwise coefficient cap and cell count, and (5)-(6) give the explicit construction and moment bound.

The first unsupported step in any extension to an infinite arithmetic wave would be identifying an actual baseline with these finite c_n and establishing the convergence or local regularity required for that extension. The isolated statement supplies neither. This report does not bridge arbitrary perturbations to exact arithmetic coefficients.

The proof requires the partition to remain fixed while averaging in R. It would not justify interchanging an R-dependent partition or its masses with the fixed-pair average in (3).

## 5. Required control tests and outcomes

All controls are exact analytical checks; no numerical evidence is used.

1. **Singleton cells: the proposed construction correctly degenerates.** If every supported integer is a singleton cell, the cell constraints force every d_n = 0; in (3), Q_T = S_T and V is identically zero. Such a partition is excluded asymptotically by the stated assumptions: if N_T is the number of supported integers, N_T >= S_T/c_max >= (s_0/C_(delta/2))T^(1-delta/2), which exceeds T^(1-delta) for large T. Thus there is no hidden claim of a nonzero perturbation in the singleton case. Outcome: passes; the cell-count restriction is substantive.

2. **Zero coefficients: no false degrees of freedom.** Formula (5) sets d_n=0 for c_n=0, and a zero coefficient is in no positive-support cell. No denominator m_C vanishes because every cell is nonempty in the positive support. If all coefficients are zero, the mass hypothesis fails. Outcome: passes.

3. **Nonnegative perturbed vectors and mass preservation.** For both signs, c_n +/- d_n >= c_n/2, and every cell total, hence the global mass, is unchanged exactly. The new maximum coefficient is at most 3c_max/2. Outcome: passes for both vectors before any sign is selected.

4. **Cell endpoints and support endpoints.** I_T uses the stated inclusive integer endpoints. The algebra applies to any disjoint exhaustive partition of its positive support; if cells are defined using numerical intervals, a boundary integer must be assigned to exactly one cell. There is no double counting or dropped endpoint. Changing a boundary convention is a different partition and is covered whenever it satisfies the same hypotheses. Outcome: passes.

5. **Perturbation fixed after R_0.** Equation (5) is evaluated once. All subsequent evaluations, derivatives, and moments keep d_n fixed, with no feedback from the moving R. Outcome: passes.

6. **Width of the physical peak.** Height T^(1/4) divided by the proven derivative bound T^(3/4) gives physical width T^(-1/2). Multiplying that width by the twelfth power of the height gives T^(-1/2)T^3 = T^(5/2). The scale is not a fixed-width radius window or a T^(-1/2) window in R/T. Outcome: passes.

7. **Adjacent square roots and real phase.** The weakest separation, n-m=1, still gives an averaged cross term O(T^(-1/2)). The product formula retains both the difference-frequency term and the sum-frequency term with phase -3pi/2. No complex exponential replacement or integer-frequency substitution is used. Outcome: passes.

8. **Very small cell mass and arbitrary geometry.** The estimate sum_(n in C)c_n^2/m_C <= c_max removes every potentially small denominator. No cell diameter, contiguity, or minimum individual weight is assumed. Outcome: passes.

9. **Cutoff and radius endpoints.** The average is over an interior subinterval J_0. The entire physical peak lies inside TJ, so w=1 throughout it even if a maximizing radius is an endpoint of TJ_0. Outcome: passes.

10. **Infinite baseline control.** Finite measurable baselines satisfy (7) without an asymptotic tail estimate; the prescribed-radius interval claim additionally requires a convergence and local oscillation justification as stated in Section 3. These inputs are absent from the finite statement and are not silently imported. Outcome: finite claim passes; any particular infinite-wave application remains conditional on its own inputs.

## 6. Dependencies and exact artifacts used

The only files read were:

1. `protocol.md` — research protocol and seven-section reporting contract.
2. `strategy/round231_local_arithmetic_admission/briefs/blind_cell_control.md` — assignment, isolation boundary, output path, and supplied graph-hash provenance.
3. `strategy/round231_local_arithmetic_admission/briefs/blind_cell_statement.md` — complete mathematical statement and required controls.

Mathematical dependencies are elementary: integration of a cosine, the real cosine product identity, the weighted variance identity, the mean-value inequality, and convexity of |x|^12. No external theorem, external citation, numerical computation, source card, or inherited candidate proof is used. The C^1 assumption on v is more than the proof needs; only its fixed positive upper and lower bounds enter.

The only artifact written is this task's report. The authoritative graph, proof draft, validation matrices, and synthesis were not accessed or modified.

## 7. Recommended state effect

**Promote the isolated finite-cell perturbation lemma after the conductor's required checks.** Its accepted scope should explicitly be arbitrary nonnegative coefficient perturbations preserving a fixed partition's cell totals, with the given subpower coefficient cap and K_T <= T^(1-delta).

**No change to any assertion about exact arithmetic coefficients, an infinite arithmetic baseline, or a downstream asymptotic theorem.** Those assertions are outside the supplied hypotheses. The two-sign finite construction and conditional infinite-baseline discussion should not be used to identify perturbed coefficients with prescribed arithmetic coefficients.

This report completes the assigned isolated task and does not design or begin another round.
