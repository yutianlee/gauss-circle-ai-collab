# Round 200: independent interval/operator rederivation

## Provenance

- Campaign: `m9-m1-t1-complete-source-coefficient-mask-analysis`.
- Task: `blind_interval_operator_rederivation`.
- Role/status: statement-only independent rederiver; candidate evidence only.
- Graph SHA-256 supplied by the statement packet, not independently read or checked: `2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5`.
- Generated: 2026-09-23, following clock observation `2026-09-23 11:48:15 UTC`.
- Context actually read: `protocol.md`, this campaign's `briefs/independent_statement_packet.md`, and this campaign's assignment brief `briefs/blind_interval_operator_rederivation.md`.
- The assignment explicitly overrides the protocol's ordinary graph pre-read to preserve statement-only isolation. No graph, campaign manifest, strategy review, claimant report, historical derivation, proof draft, or other research report was read.
- Method: finite algebra and analytical reasoning only; no numerical experiment, web lookup, or imported analytic theorem.

## 1. Result: finite lemmas and the remaining no-go

Every finite statement in the independent packet is valid with the hypotheses specified below. For `N >= 1`, put

\[
q=\lceil\log_2N\rceil,\qquad L_N=q+1.
\]

An arbitrary row-dependent prefix preserves an all-complex-vector bilinear bound with multiplier at most `L_N`. A union of at most `J` row-dependent integer intervals has the explicit safe multiplier `2 J L_N`; when `J >= 1`, a separate dyadic argument gives the optional improvement

\[
C_{N,J}=\min\{2J(q+1),\ 1+q\sqrt{2J}\}.
\]

These are proved upper constants, with no claim of optimality. The multiplier is zero for the empty mask `J=0`.

For a general complex amplitude matrix `A`, the corresponding exact conditional conclusion is

\[
\left|\sum_{m,n}A(m,n)K(m,n)\mathbf1_S(m,n)\right|
\le C_S B\|A\|_\pi,
\]

where `C_S=L_N` for a prefix and `C_S=C_{N,J}` (or `2JL_N`) for the indicated interval union. Here `||A||_pi` is the complex Hilbert-space projective tensor norm and equals the nuclear norm, the sum of singular values. It is generally larger than the Frobenius norm. An entrywise unit-bounded Fourier matrix has projective norm `N^(3/2)`, rather than the rank-one scale `N`.

On one common linear space, `sum_j M_j=I` and one common transport `U` give `sum_j[M_j,U]=0`. Different transports, or unmatched domain/codomain partitions, do not satisfy that implication.

For a finitely supported complex sequence and an integer `R>=1`, the exact parity identity is

\[
E_R(z)+E_R\bigl(((-1)^nz_n)_n\bigr)
=2D+4\operatorname{Re}C_{\rm even}.
\tag{1}
\]

Consequently,

\[
E_R(z)\le2D+4\operatorname{Re}C_{\rm even},
\quad
\left|\sum_nz_n\right|^2
\le\frac{M+R-1}{R}E_R(z)
\tag{2}
\]

when the support is contained in `M>=1` consecutive integer sites.

**No arithmetic conclusion follows from these lemmas alone.** In particular, they neither supply an unmasked all-vector bound `B`, nor bound the actual coefficient matrix's projective norm, nor verify a complete-source decomposition or its multiplicities. They therefore do not establish the original-`t=1` residual target, any `t>=2` statement, either complete parent obligation, the bridge, or the exponent claim.

## 2. Exact statements and hypotheses

### 2.1 Matrix and mask hypotheses

Let `I` be a finite row set and `N>=1`. Let `K` be a complex `I x {1,...,N}` matrix such that, for all complex vectors `a,b`,

\[
|a^TKb|\le B\|a\|_2\|b\|_2.\tag{3}
\]

The pairing in (3) is bilinear, with no conjugation on `a`. This is equivalent to the usual spectral-norm inequality `||K||_(2->2)<=B`: for any nonzero `Kb`, one can choose `a=overline{Kb}/||Kb||_2`. Thus all the estimates below apply to complex matrices without replacing their bilinear pairing by a real-only assertion.

For each `m`, a prefix is `{n:1<=n<=f(m)}`, where `f(m)` is any integer in `{0,...,N}`. No ordering of `I` or monotonicity of `f` is assumed.

An interval mask has row `S_m` equal to a union of at most `J` integer intervals in `{1,...,N}`. Empty rows are allowed. Intervals with endpoints outside the column range are first intersected with that range. Overlapping intervals may be merged, because this statement concerns the indicator of their union, with value zero or one. If one instead sums interval indicators with multiplicity, the safe `2JL_N` bound still holds by the triangle inequality, but the optional refinement proved for the union is not asserted for that multiplicity-weighted mask.

The zero-column case `N=0`, if desired, is identically zero and should be treated separately rather than evaluating `log_2 0`.

### 2.2 Projective norm

For a complex matrix `A` on these row/column sets, define

\[
\|A\|_\pi=\inf\left\{
\sum_{j=1}^k\|u_j\|_2\|v_j\|_2:
A=\sum_{j=1}^k u_jv_j^T,\ k<\infty
\right\}.\tag{4}
\]

All factors are complex; the second factor is transposed, not conjugate-transposed, in this definition. That convention does not change the value from the standard matrix nuclear norm, because complex conjugation of a factor preserves its Euclidean norm.

### 2.3 Transport and energy hypotheses

For the stated commutator identity, `U` and every `M_j` are linear endomorphisms of the same vector space `V`, all compositions are defined there, the family is finite, and `sum_j M_j=I_V`. For an infinite-dimensional domain with possibly unbounded operators, one would instead need a common invariant domain on which all the displayed compositions and identities hold. No such extra setting is needed for the present finite statement.

For the energy identities, `z:Z->C` is finitely supported, `R` is a positive integer, and

\[
D=\sum_n|z_n|^2,
\quad C_r=\sum_nz_{n+r}\overline{z_n},
\quad E_R(z)=\frac1R\sum_{s\in\mathbb Z}
\left|\sum_{j=0}^{R-1}z_{s+j}\right|^2,
\]

\[
C_{\rm even}=\sum_{\substack{0<r<R\\2\mid r}}
\left(1-\frac rR\right)C_r.
\]

All sums use the same zero-extended sequence on `Z`. For the sliding bound only, assume additionally `supp(z)` is contained in `{a,...,a+M-1}` for some integer `a` and integer `M>=1`.

## 3. Proofs and derivations

### 3.1 Prefix mask by dyadic rectangles

Set `Q=2^q` and append zero columns to `K` from `N+1` to `Q`. Inequality (3) remains valid with the same `B`, because the zero extension discards those coordinates before applying the original matrix. Extend `b` by zero when evaluating the original sum.

For each scale `ell=0,...,q`, let `D_ell` be the partition of `{1,...,Q}` into consecutive aligned intervals of length `2^ell`. Every prefix `{1,...,f}` has a disjoint decomposition into aligned dyadic intervals with at most one interval at each scale. This follows immediately by reading the binary expansion of `f` from larger powers down: the left endpoint after selecting larger powers is a multiple of the next block length. The cases `f=0` and `f=Q` give, respectively, no interval and the single root interval.

For an interval `H in D_ell`, let `I_H` be the set of rows whose prefix decomposition selects `H` at this scale. At a fixed scale the sets `I_H` are disjoint, and the intervals `H` are disjoint. Hence the scale-`ell` contribution obeys

\[
\begin{aligned}
\left|\sum_{H\in\mathcal D_\ell}
\sum_{m\in I_H}\sum_{n\in H}a_mb_nK(m,n)\right|
&\le B\sum_{H\in\mathcal D_\ell}
\|a\mathbf1_{I_H}\|_2\|b\mathbf1_H\|_2\\
&\le B\left(\sum_H\|a\mathbf1_{I_H}\|_2^2\right)^{1/2}
\left(\sum_H\|b\mathbf1_H\|_2^2\right)^{1/2}\\
&\le B\|a\|_2\|b\|_2.
\end{aligned}
\]

There are exactly `q+1` possible scales. Summing this bound gives `L_N B ||a||_2||b||_2`. Every restriction used in (3) is simply a vector with zeros outside the indicated set, so arbitrary row order and complex vectors cause no additional issue.

### 3.2 Row-dependent intervals

For a nonempty closed integer interval `[l(m),u(m)]`,

\[
\mathbf1_{l(m)\le n\le u(m)}
=\mathbf1_{n\le u(m)}-\mathbf1_{n\le l(m)-1}.
\]

An absent interval is encoded by two identical zero prefixes. Enumerate the at most `J` disjoint intervals in each row, using absent intervals to fill unused slots. Applying the prefix result to these `2J` prefix families gives the explicit multiplier `2J L_N`. This construction handles both endpoints literally; in particular an interval beginning at `1` subtracts the empty prefix, and an interval ending at `N` uses the full original column range.

For completeness, the optional refinement uses the maximal aligned dyadic subintervals of each row's interval union. For a single ordinary interval there are at most two maximal blocks at each proper scale: a maximal block's parent fails to lie in the interval and therefore crosses its left or right boundary; at a fixed parent scale at most one parent crosses either boundary, and each such parent supplies at most one maximal child. A union of at most `J` disjoint intervals therefore has at most `2J` selected blocks per proper scale. The root scale has at most one.

At one proper scale, the column blocks `H` are disjoint, but the associated row sets `I_H` can overlap. Their multiplicity is at most `2J`. The same computation as above now gives

\[
\sum_H\|a\mathbf1_{I_H}\|_2^2\le2J\|a\|_2^2,
\qquad
\sum_H\|b\mathbf1_H\|_2^2\le\|b\|_2^2.
\]

The proper-scale bound is therefore `sqrt(2J) B ||a||_2||b||_2`. There are `q` proper scales and one root scale, proving `1+q sqrt(2J)`. Taking the better of the two independently proved upper bounds gives `C_(N,J)`.

### 3.3 General amplitude and the complex nuclear norm

For any decomposition in (4), apply the masked product-vector estimate to each pair `(u_j,v_j)` and then sum:

\[
\left|\sum_{m,n}A(m,n)K(m,n)\mathbf1_S(m,n)\right|
\le C_SB\sum_j\|u_j\|_2\|v_j\|_2.
\]

Taking the infimum proves the conditional projective-norm estimate. This step does not replace the cost of the factors by the number of terms.

Here is an algebraic verification of the norm's value. Write a singular value decomposition

\[
A=\sum_{i=1}^r\sigma_i p_iq_i^*,
\quad\sigma_i>0,
\]

with orthonormal families `p_i,q_i`. Taking `u_i=sigma_i p_i` and `v_i=overline{q_i}` shows `||A||_pi <= sum_i sigma_i`. Conversely, the matrix

\[
K_0=\sum_{i=1}^r\overline{p_i}q_i^T
\]

has spectral norm one and satisfies

\[
\sum_{m,n}A(m,n)K_0(m,n)=\sum_i\sigma_i.
\]

For any factorization (4), the left side has absolute value at most `sum_j ||u_j||_2||v_j||_2`, by the spectral norm of `K_0`. This proves the reverse inequality and therefore

\[
\boxed{\|A\|_\pi=\sum_i\sigma_i(A).}
\]

In comparison,

\[
\|A\|_F=\left(\sum_i\sigma_i^2\right)^{1/2},
\qquad
\|A\|_F\le\|A\|_\pi\le\sqrt{\operatorname{rank}A}\,\|A\|_F.
\]

For a single product `A=uv^T`, the projective norm is exactly `||u||_2||v||_2`.

### 3.4 Partition commutator

Using `[M,U]=MU-UM` and linearity,

\[
\sum_j[M_j,U]
=\left(\sum_jM_j\right)U-U\left(\sum_jM_j\right)
=I_VU-UI_V=0.
\]

If instead `U:V->W`, the valid two-space version is

\[
\sum_j(M_j^WU-UM_j^V)=0
\]

provided the same `U` is used and the two finite families separately sum to `I_W` and `I_V`. This explicitly matches both sides of every composition.

There is no corresponding cancellation for unrelated `U_j`. Nor does a partition of a proper cutoff `P` give zero on the full zero-extended space: the sum is then `[P,U]`. A common zero-extended domain is sufficient only when the asserted partition of unity is actually the identity on every vector needed by both compositions.

The identity is algebraic, not a norm saving. For example, it holds for `U=lambda I` for every scalar `lambda`, with no restriction on `|lambda|`.

### 3.5 Exact energy expansion and parity connector

Expand each window square and sum over its starting point. Each pair of sites at separation `r`, with `|r|<R`, is included in exactly `R-|r|` windows. Thus

\[
E_R(z)=D+2\operatorname{Re}
\sum_{r=1}^{R-1}\left(1-\frac rR\right)C_r.
\tag{5}
\]

The opposite orientation is the complex conjugate because

\[
\sum_nz_{n-r}\overline{z_n}
=\overline{\sum_nz_{n+r}\overline{z_n}}.
\]

This explains the factor two and the single real part in (5). It uses the total zero extension, so no endpoint term is discarded.

Set `w_n=(-1)^n z_n`. Its diagonal mass is `D`, and its shift correlation is `(-1)^r C_r`. Adding (5) for `z` and `w` cancels odd shifts and doubles even shifts, giving (1). Since `E_R(w)>=0`, the first inequality in (2) follows.

Equivalently, split each window into its even-site sum `A_s` and odd-site sum `B_s`. Then

\[
2D+4\operatorname{Re}C_{\rm even}-E_R(z)
=\frac1R\sum_s|A_s-B_s|^2.
\tag{6}
\]

In particular `D+2 Re C_even>=0`; the even-shift correlation itself need not be nonnegative.

For the phase displayed in the assignment, take real `X>=0`, real `sigma`, and a finite coefficient sequence `c_N` supported on nonnegative integer indices. With `e(t)=exp(2 pi i t)`, define

\[
z_N=c_Ne(\sigma\sqrt X\sqrt N)\quad(N\ge0),
\qquad z_N=0\quad(N<0).
\]

Then, for every nonzero correlation summand with `r>0`,

\[
z_{N+r}\overline{z_N}
=c_{N+r}\overline{c_N}
e\!\left(\frac{\sigma\sqrt X\,r}{\sqrt{N+r}+\sqrt N}\right).
\tag{7}
\]

The denominator is positive for these indices, and (7) is just the rationalized square-root difference. Also `D=sum_N |c_N|^2`. Define the zero-extended `z` first; do not evaluate an undefined square root at an absent negative index and then multiply by zero. Formula (7) connects the displayed source to the finite parity identity whenever the supplied `c` is indeed its complete coefficient sequence. It does not verify the arithmetic construction of that sequence.

### 3.6 Sliding reconstruction and explicit power ledger

Let `S_s=sum_(j=0)^(R-1) z_(s+j)` and `S=sum_n z_n`. Since every site occurs in exactly `R` windows,

\[
\sum_sS_s=RS.
\]

If `supp(z)` is contained in `[a,a+M-1]`, then `S_s` can be nonzero only for

\[
a-R+1\le s\le a+M-1,
\]

which is exactly `M+R-1` possible integer starts. Cauchy-Schwarz therefore gives

\[
R^2|S|^2\le(M+R-1)\sum_s|S_s|^2
=(M+R-1)R E_R(z).
\]

Division by `R^2` proves the second inequality in (2), including its exact normalization.

Combining the two connectors gives

\[
|S|^2\le\frac{M+R-1}{R}
\bigl(2D+4\operatorname{Re}C_{\rm even}\bigr).
\tag{8}
\]

For a single proposed masked representation of the source, the finite matrix contribution costs exactly the proved upper expression `C_S B ||A||_pi`. For several actual pieces, a sufficient upper bound is the sum of their separate expressions, with every supplied scalar weight, orientation, and multiplicity included. Neither a count of pieces nor a bound on individual entries replaces this ledger.

Consequently a sufficient condition for a source estimate of size `L^2 X^epsilon` is a verified source representation with a total ledger bounded by that quantity. The present finite argument does not establish that condition. If independently `(M+R-1)/R <= C L`, `D <= d L^2 X^epsilon`, and `Re C_even <= c L^2 X^epsilon`, then (8) gives only the explicit squared-sum conclusion `|S|^2 <= C(2d+4c)L^3 X^epsilon` (assuming the stated upper constants are nonnegative). No improvement of that power is hidden in the reconstruction step.

## 4. First doubtful or unproved step

There is no remaining doubtful step in the finite lemmas under their stated hypotheses. The first unproved step for application to the frozen arithmetic target is the existence of a complete, exactly normalized source representation to which (3) applies with a sufficiently small all-vector constant `B` and a sufficiently small projective coefficient norm.

More specifically, the statement packet supplies neither:

1. the arithmetic proof of the required unmasked estimate (3);
2. an upper bound for the actual mixed amplitude in the norm (4);
3. a proof that every relevant restriction is a union of the claimed number of row intervals after the exact arithmetic parameters are fixed;
4. a full multiplicity ledger linking those pieces to the original source with both orientations and the actual residual coefficients;
5. the diagonal estimate and precise support parameters needed for a final quantitative use of (8).

These are missing application inputs, not conclusions that can be extracted from commutator cancellation, bounded entries, or the energy identities. The precise formulas defining `c^rem`, total `lambda`, and the labels K185.1--3 were outside the statement-only packet; they were not reconstructed or assumed from historical memory.

## 5. Control tests and outcomes

All controls below are exact algebraic examples or endpoint arguments, not numerical experiments.

### 5.1 Empty rows, arbitrary ordering, non-powers of two, and endpoints — PASS

The prefix decomposition of `f=0` is empty, and that of `f=Q` is the root. The construction is independent for each row, so a row permutation or wildly oscillating `f` has no effect. If `N` is not a power of two, dummy columns are identically zero and all original endpoints remain unchanged. Intervals touching `1` or `N` use the exact empty/full prefix as appropriate. For `N=1`, `q=0` and the prefix constant is exactly one. For `R=1`, `C_even=0`, `E_1=D`, and the sliding statement reduces to `|sum z|^2<=M D`. For `M=1` and any `R`, the sliding coefficient is one and equality holds. These checks include `R` exceeding the support length.

### 5.2 A prefix need not preserve the original norm with constant one — false shortcut rejected

Take

\[
K=\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad f(1)=1,\ f(2)=2.
\]

The original spectral norm is `sqrt(2)`. The masked matrix is `[[1,0],[1,-1]]`, whose squared norm is `(3+sqrt(5))/2>2`. Thus automatic constant-one preservation is false. This does not challenge the proved logarithmic bound.

### 5.3 Bounded entries versus projective norm — PASS; cheap-entry shortcut rejected

Let `A_(m,n)=exp(2 pi i mn/N)`, with indices `m,n=0,...,N-1`. The geometric-sum identity gives `AA*=N I`, so all its singular values equal `sqrt(N)`. Consequently

\[
|A_{mn}|=1,\quad\|A\|_F=N,\quad\|A\|_\pi=N^{3/2}.
\]

By comparison, the all-ones `N x N` matrix has the same entrywise and Frobenius bounds but projective norm `N`. This is a growing factor `sqrt(N)`. More strongly, set `K=overline A/sqrt(N)`. Then `||K||_(2->2)=1`, while the full, unmasked bilinear coefficient pairing is

\[
\sum_{m,n}A_{mn}K_{mn}=N^{3/2}.
\]

Thus replacing the projective norm by the Frobenius norm in the all-vector conclusion is explicitly false. Merely counting product terms is also invalid: a single product may be multiplied by an arbitrarily large scalar, changing its norm without changing the number of terms. For the Fourier example any exact product decomposition has total factor cost at least `N^(3/2)`.

### 5.4 Arithmetic masks and unsigned controls — false shortcuts rejected

For `N=2^k`, index rows and columns by binary vectors of length `k` and set

\[
H_{xy}=N^{-1/2}(-1)^{x\cdot y}.
\]

Character orthogonality gives `HH*=I`, hence the unmasked all-vector bound has `B=1`. If the mask keeps precisely the positive entries, the masked matrix is

\[
H_+=\frac12\left(H+N^{-1/2}\mathbf1\mathbf1^T\right).
\]

For the unit constant vector `u=N^(-1/2)1`, the exact sum of the entries of `H` is `sqrt(N)`, so

\[
u^T H_+u=\frac12\left(\sqrt N+\frac1{\sqrt N}\right).
\]

The norm of this arbitrary mask is therefore at least that quantity, despite `B=1`. An unrestricted arithmetic selector cannot be silently assigned the cost of a bounded number of intervals. Separately, the entrywise absolute-value matrix `|H|` has norm `sqrt(N)`, so the signed unmasked bound cannot be transferred to an unsigned kernel with the same `B`.

These are controls on false universal analogues only. They are not asserted to equal the problem's actual coefficients or arithmetic kernel. No property of Vaaler coefficients or `chi_4` is used in the proved finite lemmas; any exclusion of a false unsigned/adversarial analogue must therefore enter through independently proved arithmetic hypotheses such as `B` or the actual amplitude norm.

### 5.5 Partition recombination and domain mismatch — PASS; invalid recombination rejected

On `C^2`, let `M_1=diag(1,0)`, `M_2=diag(0,1)`, `U_1=E_12`, and `U_2=0`. Then `M_1+M_2=I`, but

\[
[M_1,U_1]+[M_2,U_2]=E_{12}\ne0.
\]

This disproves replacement of a common transport by unrelated maps. For a boundary example on finitely supported sequences on `Z`, let `T e_n=e_(n+1)` and let `P` cut off to `{1,...,M}`. Then `[P,T]e_M=-e_(M+1)`, which is nonzero. A partition summing to `P` does not sum to the identity on the full transport space. If one compresses everything to the finite range of `P`, the common-space identity is valid for the compressed transport `PTP`, but that is a changed transport and does not erase the displayed boundary term for `T`.

### 5.6 Even parity and one outer real part — PASS

Take `R=3`, `z_0=1`, `z_2=-1`, and all other entries zero. Then `D=2`, `C_even=-1/3`, and `E_3=4/3`; the proposed upper bound is `8/3`. This verifies that the right side remains nonnegative while the even correlation can be negative; dropping the diagonal contribution would give a false negative upper bound. With `z_0=1`, `z_2=i`, the same `R` gives `C_even=i/3`, demonstrating why the real part must be present in the ordered energy inequality.

The factor two in front of `D` cannot be uniformly decreased while keeping the `R=2` statement: for the indicator of `M` consecutive sites, `C_even=0` and `E_2=2M-1`, so `E_2/D` tends to two. Both orientations are already counted exactly in (5); inserting another orientation factor would double-count them. Replacing signed correlations by absolute values may supply a weaker upper bound, but it does not preserve the cancellation in (1).

### 5.7 Required application-control ledger

| Required control | Outcome within statement-only scope |
|---|---|
| `complete_source_multiplicity` | Finite energy expansion counts every pair exactly `R-|r|` times and combines opposite orientations once. Actual arithmetic source multiplicities are **not supplied and not certified**. |
| `actual_coefficients_only` | Formula (7) is valid for the actual coefficient sequence if supplied. Fourier/Hadamard examples are labeled false-universal controls, not substitutes for actual coefficients. |
| `literal_endpoint_zero_extension` | Passed by dyadic padding and full `Z` energy sums; no endpoint term is omitted. |
| `partition_recombination` | Passed for one common transport and matching identity partitions; explicit failures given for differing transports and cutoffs. |
| `row_interval_vs_arithmetic_masks` | Exact interval bounds proved; arbitrary selector control fails any automatic bounded-interval claim. |
| `product_and_projective_norms` | Product and mixed-amplitude estimates proved, norm identified exactly, Frobenius/entrywise shortcuts refuted. |
| `even_parity_connector` | Exact identity (1), phase identity (7), and inequality (2) proved. |
| `one_outer_real_part` | Opposite orientations are conjugates; the resulting `2 Re` normalization and even-shift factor four are explicit. |
| `net_power_ledger` | Mask cost is `C_S B ||A||_pi`; reconstruction costs `(M+R-1)/R`. No unproved power saving is absorbed. |
| `no_capacity_lower_bound` | No source lower bound is inferred from a norm budget or capacity. Fourier/Hadamard lower bounds refer only to the explicitly constructed control matrices. |
| `no_unverified_theorem_import` | No external analytic theorem is invoked; the derivations use finite linear algebra, dyadic decomposition, geometric sums, and Cauchy-Schwarz. |
| `protected_parent_and_exponent_scope` | No original-source, parent, bridge, or exponent promotion is claimed. |

## 6. Dependencies and exact artifacts used

1. `protocol.md`: workflow, evidence status, seven-section contract, isolation rules, and protected-scope discipline.
2. `rounds/codex-managed/m9-m1-t1-complete-source-coefficient-mask-analysis/briefs/independent_statement_packet.md`: exact finite statements and supplied graph hash.
3. `rounds/codex-managed/m9-m1-t1-complete-source-coefficient-mask-analysis/briefs/blind_interval_operator_rederivation.md`: permitted role, output path, required controls, and the displayed phase convention.

No dependency on a claimant proof is present. The mathematical inputs are elementary finite-dimensional singular value decomposition, orthogonality of finite geometric/character sums, triangle and Cauchy-Schwarz inequalities, and direct finite-sum identities. No historical arithmetic estimate is presumed. This report is the only file written by this task.

## 7. Recommended state effect

**Recommend promotion only of the finite conditional interface lemmas after the conductor's required independent seam checks and graph-validation process:** arbitrary prefix mask, explicit interval-union costs, complex projective/nuclear-norm extension, common-transport commutator identity with domain restrictions, exact even-parity identity, and sliding reconstruction.

**Recommend retain/open** for the complete original-`t=1` arithmetic source target and all protected parents. The first application gaps are the proved unmasked all-vector estimate, controlled actual coefficient norm, correct interval complexity, and complete multiplicity/reconstruction ledger. The statement-only materials do not establish those inputs.

**Recommend reject** any proposed universal shortcut that (i) uses bounded entries or Frobenius norm in place of the projective factor cost, (ii) applies the signed `B` unchanged to an unsigned kernel, (iii) treats a general arithmetic selector as a bounded-interval mask without proof, or (iv) cancels commutators across different transports or unmatched domains.

No shared state has been edited. The assigned task ends with this report.
