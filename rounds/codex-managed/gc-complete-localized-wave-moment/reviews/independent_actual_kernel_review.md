# Round215 independent actual-kernel review

Campaign: `gc-complete-localized-wave-moment`  
Role: independent NONBLIND seam review, after completion of the isolated derivation  
Reviewer task: `blind_spatial_kernel` (original isolated report remains unchanged)  
Date: 2026-09-28  
Reviewed artifact: `controls/conductor_actual_kernel_ledger.md`  
Reviewed SHA256: `a90cdb1a9a19e28e248c7d56b16d28c87e5848e7d63da02d2c1281cda7bd4daa`  
Hash status: exact match verified before review.  
Overall disposition: **GREEN for the actual-coefficient binding, exact kernel identities, both positive-certificate lower bounds, and trace implication at this final reviewed hash.**

## 1. Result: actual-coefficient kernel and trace review GREEN

The final ledger supplies the exact coefficient formula, mask argument, support and smoothness. These establish its coefficient positivity and mass hypotheses directly, closing the prior source-binding correction. The exact Fourier identities, full-tail window identity, eventual compact spatial lower modulus, both positive-certificate lower bounds, real-parameter treatment, target comparisons, and clarified interval trace are mathematically correct for these actual coefficients. The kernel conclusions agree with the independent isolated derivation.

There are no remaining corrections to this ledger within the reviewed scope. GREEN certifies these stated results; it does not certify the unproved actual signed-moment target or a circle-discrepancy theorem.

## 2. Exact statements and hypotheses reviewed

The actual coefficients now specified in the final ledger are

\[
 c_m=|m|^{-3/2}\Psi(|m|/\sqrt T)v(|m|^2/N),\qquad
 m\in\mathbb Z^2\setminus\{0\},
\]

where `v` is a fixed nonzero nonnegative smooth real function supported in `[1,4]`, and `Psi` is fixed, real, continuous and satisfies `Psi(0)=1`. The coefficient estimates below hold uniformly for sufficiently large real `T` throughout `T^(166/325)<N<T^(242/325)`. For strict target comparisons one fixes `N=T^alpha` with `166/325<alpha<242/325`. The actual formula implies

\[
 c_m\ge0,\quad \operatorname{supp}(c)\subset\{m\in\mathbb Z^2:\sqrt N\le|m|\le2\sqrt N\},
 \quad \sum_m c_m\asymp N^{1/4}.
\]

The upper cap `c_m<=C N^(-3/4)` is used in the proposed actual binding, but the subsequent certificate arguments require only nonnegativity, support, and total mass. The cutoffs are fixed real Schwartz functions with compact Fourier supports and value one at zero; `W=C_A(1+|y|^2)^(-100)`, `C_A>0`. The separate and joint certificates `P_sep,P_joint`, center grid, and Fourier transforms are exactly those defined in the reviewed ledger. Uniform central-window coverage uses the separately recorded clarification that the lower-bound cubes contain `[-1,1]^2` and `[-1,1]`.

Under these hypotheses and for all sufficiently large `T`,

\[
 \mathcal C\le P_{\rm joint}\le P_{\rm sep},\qquad
 P_{\rm sep}\gtrsim TN^2,\qquad P_{\rm joint}\gtrsim N^{5/2},
\]
\[
 \int_{T/\sqrt2}^{\sqrt3T}|F_N(0,R)|^{10}\,dR
 \lesssim N^{-1/2}\mathcal C(T,N).
\]

These are statements about positive upper certificates and a sufficient trace implication. They contain no lower bound for the signed moment or physical discrepancy.

## 3. Proof audit and derivation

### Actual coefficient binding: GREEN

The numerical scaling in ledger section A is correct:

\[
 |m|/\sqrt T\le2\sqrt{N/T}\le2T^{-83/650}.
\]

For the fixed real continuous `Psi` with `Psi(0)=1`, this puts `Psi` between `1/2` and a fixed positive upper constant on the annulus for sufficiently large `T`, uniformly over the open band. The exact coefficient formula therefore gives `c_m>=0`. On the support, `|m|^(-3/2)<=N^(-3/4)`, and the fixed mask is bounded, so `c_m<=C N^(-3/4)`. There are `O(N)` lattice vectors in the annulus, proving the upper mass bound.

Since the now explicitly smooth `v` is nonnegative and nonzero, it is bounded below by some `v_*>0` on an interval `[u_1,u_2]` with `1<u_1<u_2<4`. Its argument `|m|^2/N` makes this interval correspond exactly to the subannulus

\[
 \sqrt{u_1N}\le|m|\le\sqrt{u_2N}.
\]

The unit-square boundary-strip argument gives `pi(u_2-u_1)N+O(sqrt(N))` lattice vectors there. It applies to real N and requires no circle-discrepancy estimate beyond a fixed-width geometric boundary bound. Every such vector has

\[
 c_m\ge\tfrac12 v_*u_2^{-3/4}N^{-3/4}.
\]

Thus `sum c_m>=cN^(1/4)`. Combining both bounds yields `sum c_m` comparable to `N^(1/4)` and consequently total five-tuple mass comparable to `N^(5/4)`. The actual binding now passes without an additional coefficient hypothesis or an unlisted source.

### Fourier factors, all tails, and center phases: GREEN

With the ledger's positive Fourier-exponent convention, a two-five-tuple term has phase

\[
 e(y\cdot\Delta v/\sqrt N)\,e(R_j\Delta s)\,e(u\Delta s/\sqrt N).
\]

Integrating in `y` gives `A_N(Delta v/sqrt(N))`. Substituting `u=Nt` gives exactly `N B(sqrt(N)Delta s)`. Summing the centers gives `S_J(Delta s)`. Thus ledger equation (3) retains every phase with the correct sign and normalization.

For the alternative expression, `u=sqrt(N)(R-R_j)` gives `du=sqrt(N)dR` and `u/N=(R-R_j)/sqrt(N)`. It follows exactly that

\[
 \mathcal C=\sqrt N\int_{\mathbb R}h(R)\int_{\mathbb R^2}
 W_N(y)|F_N(y/\sqrt N,R)|^{10}\,dy\,dR,
\]
\[
 \int h=(J+1)\sqrt N\int q,
 \qquad \int h(R)e(Rz)\,dR=\sqrt N B(\sqrt Nz)S_J(z).
\]

All integrals retain the full Schwartz tails. The triangle inequalities give the stated ordering of certificates. No spatial delta or radial window truncation is introduced.

### Eventual compact spatial lower modulus: GREEN

The transform of `W` is

\[
 \frac{C_A\pi}{\Gamma(100)}\int_0^\infty
 t^{98}\exp(-t-\pi^2|z|^2/t)\,dt>0.
\]

It is continuous, hence has a strictly positive minimum on `|z|<=20`. Dominated convergence gives `||W_N-W||_1 -> 0`; the Fourier transforms therefore converge uniformly, even if `phi` is not even and `A_N` is complex. This proves an eventual positive lower bound for `|A_N|` on the compact domain. Every relevant difference lies there because `|Delta v|<=20sqrt(N)`. The ledger correctly makes no all-frequency or all-finite-N positivity claim.

### Two pigeonhole scales: GREEN

Five-fold radial sums lie in an interval of length `5sqrt(N)` and have total weight comparable to `N^(5/4)`. Bins of width `O(N^(-1/2))` number `O(N)` and yield same-bin pair mass at least a constant times `N^(3/2)`. The kernel factors are uniformly bounded below there; multiplication by `N(J+1)` gives `TN^2`.

For the joint certificate, choose a fixed small `c_1` that satisfies both the center-phase and `B` conditions. On `|Delta s|<=c_1/T`, remove the common center phase; all remaining center phases have positive real parts uniformly, since `Jsqrt(N)<=dT+sqrt(N)`. Thus `|S_J|` is at least a constant times `J+1`. The finer bins now number `O(Tsqrt(N))`, giving pair mass at least a constant times `N^2/T`. Multiplication by `N(J+1)` gives `N^(5/2)`. Neither step uses independence or substitutes raw counts for weighted mass.

### Real endpoints, target exponents, and trace: GREEN

Throughout the band `1<=N<=T^2`, so `J+1` is comparable to `T/sqrt(N)` with constants unaffected by real parameters or the ceiling. The two target gaps are exactly

\[
 1+2\alpha-83/65=2\alpha-18/65,
 \qquad (5/2)\alpha-83/65.
\]

The first equals `242/325` at `alpha=166/325`; the second equals zero there and is positive strictly above it. Thus the claimed strict failure is correct for each fixed interior alpha and any positive epsilon smaller than its gap. No uniform positive gap can be inferred as alpha approaches the lower endpoint with T, and the ledger expressly avoids that inference.

For trace, the spatial frequencies of `f_j(.,u)` lie in a fixed disk. A fixed Schwartz reproducing kernel `k` gives

\[
 |f_j(0,u)|^{10}\le\left(\int|k|\right)^9
 \int |k(-y)|\,|f_j(y,u)|^{10}\,dy
 \lesssim\int W(y)|f_j(y,u)|^{10}\,dy.
\]

The final domination is valid because `k` is Schwartz; increasing `C_A` or retaining an additional fixed constant both suffice. The clarified eta lower bound covers the nearest-center distance at most `sqrt(N)/2`, including both partial endpoints. Integration with `dR=N^(-1/2)du` proves the stated trace. This coverage step leaves the other tails in `C` intact.

## 4. First doubtful or unproved step

There is no unverified step in the reviewed actual binding, kernel identities, certificate lower bounds or trace implication at the final hash. The prior missing-definition correction is discharged by the final ledger's section 2.

The first remaining open analytic step is an upper bound on the actual signed moment at the target power. The two certificate lower bounds cannot settle it, since `C<=P_joint<=P_sep` gives no converse inequality.

## 5. Required controls and outcomes

- Reviewed hash: exact match; **PASS**.
- Actual coefficient definition, mask argument, smoothness and sign: explicit in final ledger and checked directly; **PASS**.
- Psi scale and uniform approach to one: exponent `-83/650` and its multiplicative role in the actual formula correct; **PASS**.
- Elementary annulus count: subannulus `sqrt(u_1 N)<=|m|<=sqrt(u_2 N)` has area `pi(u_2-u_1)N` and boundary-strip error `O(sqrt(N))`, valid for real N; **PASS**.
- Fourier signs, radial factors `N` and `sqrt(N)`, center phases and full tails: **PASS**.
- Spatial compact-domain bound and eventual-only scope: **PASS**.
- Separate/joint weighted binning with widths `N^(-1/2)` and `T^(-1)`: **PASS**.
- Fixed-interior target comparisons and excluded lower endpoint: **PASS**.
- Trace bandwidth, clarified coverage, and Jacobian: **PASS**.
- Signed-versus-certificate inference: the ledger consistently restricts its no-go to the two positive certificates; **PASS**.
- Experiments: none; all checks analytical.

## 6. Dependencies and exact artifacts used

1. `protocol.md`, previously read for this task.
2. `briefs/blind_spatial_kernel_statement.md`, the original isolated packet, previously read.
3. The completed isolated report `reports/blind_spatial_kernel.md`, whose content was already known to its author. That report was not modified during this review.
4. `controls/conductor_actual_kernel_ledger.md`, final SHA256 `a90cdb1a9a19e28e248c7d56b16d28c87e5848e7d63da02d2c1281cda7bd4daa`, reread and hash-verified for this NONBLIND seam. The earlier reviewed version at SHA256 `b94d96ec799ae8345260f3cb4ff226e5a02fc227a4279ffde6f6c26e2569bfa3` lacked the self-contained coefficient definition; the present disposition binds only the corrected final hash.
5. `controls/cutoff_normalization_clarification.md`, read for the explicit central-window normalization.

No sibling report, frozen strategy, manifest, graph, external source, or other unlisted context was opened. The actual coefficient binding uses the final ledger's explicit definitions, not an inference from citations to unlisted files.

## 7. Recommended state effect

Retain the accepted graph and proof draft unchanged. Record **GREEN for actual-coefficient source binding, exact kernel identities, both certificate no-go bounds and the trace implication** at the final reviewed hash. The conductor may archive these limited findings as reviewed evidence.

Do not label this seam as additional blind work. Do not promote a signed moment or circle-discrepancy claim. This task wrote only this review and stops here.
