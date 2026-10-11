# Round 200: complete-source analytical derivation

- Campaign: `m9-m1-t1-complete-source-coefficient-mask-analysis`.
- Task: `complete_source_analytic_derivation`.
- Role/access: discovery; selected context, with exact antecedents traced below.
- Generated: 2026-09-23, Asia/Shanghai.
- Raw starting graph SHA-256, independently checked from the file:
  `2f4448e999ab90387bca06498ddc60ee97b50f9900a9dfc6ad41fb201833c5f5`.
- Status: candidate evidence only. No shared state was edited.
- Effort: analytical/algebraic only; no numerical experiments or external theorem imports.

## 1. Result: complete-source interface, with the analytic estimate open

The complete original-`t=1` residual correlation is reconstructed below on
one multiplicity-one endpoint domain, before any orientation, gcd, height,
packet, `P_1/P_2`, or later `T` split. Its coefficient is exactly a product
of two actual endpoint coefficients. In these coordinates the projective
norm is affordable: it is the squared endpoint coefficient norm, at most
`L^2 X^epsilon`. This is a useful distinction from a generic mixed-amplitude
obstruction.

The remaining problem is analytic. The square-root correlation phase is
separable in the two complete endpoints, so its unrestricted all-vector
matrix norm does not give cancellation. Including the short-product-gap
mask gives the familiar `L^3 X^epsilon` correlation capacity. A bound for
the **actual vector** that removes its remaining factor `L` is still
unproved. This report provides an exact parity-Fejer spectral formulation
of that missing estimate, and a separate all-cost conditional bilinear
interface for any future arithmetic reindexing.

The identities `P_cl+P_1+P_2=1` and the common-transport commutator sum are
exact before norms. They remove artificial partition boundaries, but do
not prove the analytic estimate. This conclusion does not depend on
stopping at the old `P_2` triangle.

The smooth part of the normalized symbol is explicitly recovered from
its transform antecedent. Later kernels retain a closed list of literal
trace labels without giving every label an executable scalar formula.
Those fields are retained through the exact inherited `a^lit` and are
identified explicitly below; they are not silently set equal to one.

Recommended exit: `complete_source_interface_with_open_estimate`.

## 2. Exact statement and hypotheses

Fix real `X>=2`, one literal middle or lower residual hard-M1 shell
`L>=2`, and `sigma in {+1,-1}`. Put

\[
 y=\lfloor\sqrt X\rfloor,\quad q_X=X/y^2,\quad
 H=\lfloor yX^{-1/4}\rfloor,\quad R=\lceil L\rceil.
\]

The allocation-independent Round-184 selector is fixed. If it selects
`{p_N,q_N}`, these are distinct odd prime divisors of squarefree `N`,
with opposite character and the prescribed close logarithmic ratio.
Its exact residual mask is

\[
 \rho_N(d)=1\quad\hbox{if no pair is selected};\qquad
 \rho_N(d)=1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
                  +2\mathbf1_{p_Nq_N\mid d}
\tag{200.A1}
\]

otherwise. It equals one on neither/both allocations and zero on XOR
allocations. Neither pair density nor a nonempty selected sector is
assumed.

Use the *total*, zero-extended coefficient of K185.2, without modification:

\[
 \lambda_{N,\sigma}(d)=
 \begin{cases}
 \mu^2(N)\rho_N(d)a_{L,X}^{\mathrm{lit},\sigma}(N/d,d),
 &N,d>0,\ \mu^2(N)=1,\ d\mid N,\ d\text{ odd},\\
 0,&\text{otherwise}.
 \end{cases}
\tag{200.A2}
\]

Then

\[
 c_N=\sum_d\chi_4(d)\lambda_{N,\sigma}(d),\qquad
 z_N=c_Ne(\sigma\sqrt{XN})\ (N>0),\qquad z_N=0\ (N\le0).
\tag{200.A3}
\]

All displayed sums are finite because the literal symbol is zero off
its original domain. On live support `d,m~L`, `N=dm~L^2`,
`d` is odd, `(d,m)=1`, and `|lambda|<<_epsilon X^epsilon`.
The actual source to estimate is

\[
 C^{(2)}=\sum_{\substack{0<r<R\\2\mid r}}
  (1-r/R)\sum_Nz_{N+r}\overline{z_N}.
\tag{200.A4}
\]

The target is the one-sided upper bound

\[
 \boxed{\Re C^{(2)}\ll_\epsilon L^2X^\epsilon.}
\tag{200.A5}
\]

This is not a demand for `|C^(2)|`, a sum of shiftwise absolute values,
or absolute estimates on every sector. Those are stronger sufficient
conditions only.

## 3. Proof and derivation

### 3.1 Actual normalized symbol and exact trace provenance

The accepted transform antecedent, Round-9
`blind_m1_top_transform.md`, equations (1.4)--(2.3), gives

\[
 \alpha_{m,H}=-\frac{\Phi(m/(H+1))}{2\pi i m},\qquad
 \Phi(v)=\pi v(1-v)\cot(\pi v)+v\quad(0<v<1),
\]

with the accepted endpoint extensions. On the normalized stationary
cone the complete moving smooth factors are exactly

\[
 A_{L,X}(m,d)=\eta_L(m)\Phi\!\left(\frac m{H+1}\right)
 W\!\left(\sqrt{\frac{4q_Xm}{d}}\right)
 \left(\frac{L^2}{md}\right)^{3/4}.
\tag{200.A6}
\]

Here `eta_L` is the fixed normalized-BV frequency cutoff, including its
literal shell endpoint values; the exact frequency range is intersected
with `1<=m<=H`. The cone is `4m<d<16m`, with `d` odd. Writing the upper
edge as `d<=16m` makes no difference because `16m` is even.

For the positive stationary shell the original M1 reconstruction factor
is

\[
 -\frac{2e(1/8)}\pi X^{1/4}L^{-3/2};
\tag{200.A7}
\]

the negative-frequency contribution is the conjugate. Thus this
normalization places neither an additional `m^-1` nor an extra
`X^1/4` inside (200.A6). The boundary and transform-error terms were
handled by the accepted transform; their half-weight correction must
not be counted a second time as another stationary summand.

The profile antecedent explicitly constructs a fixed smooth step `eta`
and `W(t)=eta(t)-eta(2t)`, with top spatial weight
`W(d/y)1_(d<=y)`, including the final integer. Some historical transform
reports state a wider plateau than the profile certificate; this report
uses only the common verified facts needed here: `W` is fixed and smooth,
zero at/below `1/2`, and `W(1)=1`. No plateau width is used in any argument.

K184.11 and the Round-183/184 coefficient seam reviews identify (200.A6)
as the smooth moving-factor ledger of `a^lit`, up to allocation-independent
shell/sign constants and the actual finite family of literal multipliers
and traces. The exact inherited sharp code is the closed list K197.C8b:

\[
 \ell_{\rm shell},\ell_{\rm frequency},\ell_{\rm height},
 \ell_{\rm cone},\ell_{\rm profile},\ell_{\rm floor},
 \ell_{\rm star},\ell_{\rm tie},\ell_{1/2},\ell_{\rm hard},
 \ell_{\rm cell},\ell_{\rm crossing},\ell_{\rm endpoint},\ell_{\rm sign}.
\tag{200.A8}
\]

In that definition profile means support/plateau/branch, cell records
the literal `Phi` and transformed-`W` cells, crossing includes the
real-`X` ratio branch, and floor/star/tie/half/hard/endpoint are their
actual discrete trace labels. The code excludes the evaluated smooth
values and excludes the selector value. Its cemetery state is determined
by named support/arithmetic failure, not accidental coefficient vanishing.

**Explicit source limitation:** the antecedents inspected give (200.A6),
the shell/height/cone formulas and the named trace list (200.A8), but not
a further numeric formula for every one of those trace labels. Accordingly
(200.A2), rather than (200.A6) alone, is the coefficient throughout this
report. No bound below requires reconstructing a missing trace by guesswork.
An import that needs an explicit interval count or derivative formula for
every label still needs that formula or must keep that label inside its
kernel/coefficient. This limitation does not prevent the exact complete
source or the exact endpoint-product norm below.

### 3.2 Common physical domain, amplitude, phase and multiplicity

Let `E` be a finite containing box of endpoint allocations
`i=(m,d)`, with positive integer `m,d~L`, `d` odd, large enough to contain
every live endpoint. Put

\[
 N_i=md,\quad b_i=\chi_4(d)\lambda_{N_i,\sigma}(d).
\tag{200.A9}
\]

Cemetery endpoints have `b_i=0`. The common ordered-pair domain is

\[
 \mathcal D=\{(i,j)\in E^2:0<N_j-N_i<R,\quad N_j\equiv N_i\pmod2\}.
\]

Then the exact complete source is

\[
 C^{(2)}=\sum_{(i,j)\in\mathcal D}
  \left(1-\frac{N_j-N_i}{R}\right)b_j\overline{b_i}
  e\!\left(\sigma\sqrt X(\sqrt{N_j}-\sqrt{N_i})\right).
\tag{200.A10}
\]

| Field | Exact value / domain rule | Multiplicity or norm consequence |
|---|---|---|
| Lower endpoint | `i=(m,d)`, `N_i=dm` | One allocation, not one representative per product |
| Upper endpoint | `j=(m',d')`, `N_j=d'm'` | Every endpoint divisor is opened |
| Endpoint coefficient | `b_i=chi_4(d) mu^2(N_i) rho_(N_i)(d) a^lit(m,d)` | Zero on every failed literal predicate |
| Endpoint arithmetic | `N_i,N_j` squarefree; `d,d'` odd; allocation coprimality | Coprimality follows from squarefreeness but is retained |
| Shift | `r=N_j-N_i`, `0<r<R`, even | Exactly one shift per ordered pair; no `r=0` term |
| Character | `chi_4(d')chi_4(d)` | If `d'-d=2 alpha`, it equals `(-1)^alpha` |
| Phase | `e(sigma sqrt X r/(sqrt(N+r)+sqrt N))` | Equals the phase in (200.A10), with no approximation |
| Fejer weight | `1-r/R` | Positive and literal; no endpoint extension error |
| Complex convention | Upper coefficient times conjugated lower coefficient | One final outer real part; both signs treated separately |
| Endpoint traces | Every field in (200.A8), at both endpoints | Retained before all reindexings |

To prove (200.A10), expand the two divisor sums in (200.A4). Conversely,
an ordered endpoint tuple recovers `N=dm`, `r=d'm'-dm`, and its two
divisors uniquely. This is a bijection, so no divisor, sign, orientation,
gcd, or selector multiplicity is omitted. Positive support is imposed
before evaluating a square root.

For later use, set `D=sum_N |c_N|^2`. Cauchy on each finite divisor fibre
and the elementary divisor bound give

\[
 D\le\max_{N\asymp L^2}\tau(N)\sum_{i\in E}|b_i|^2
 \ll_\epsilon L^2X^\epsilon.
\tag{200.A11}
\]

This explicitly prices the product regrouping. It is subpower, not a
missing factor `L`.

### 3.3 Recombine the complete physical partition before norms

For every tuple in the common domain put
`g=(d,d')`, `D_L=ceil(sqrt L)`, and

\[
 A=\mathbf1_{|d-gm|\le D_L},\qquad
 B=\mathbf1_{|d'-gm'|\le D_L}.
\]

The exact inherited masks are

\[
 P_{\rm cl}=AB,\qquad P_1=1-A,\qquad P_2=A(1-B),\qquad
 P_{\rm cl}+P_1+P_2=1.
\tag{200.A12}
\]

The algebraic identity holds on all positive tuples; the accepted sector
theorem uses its stated opposing-incidence/projector scope. Extending the
identity does not extend that theorem. In particular,

\[
 C^{(2)}=C^{(2)}[P_{\rm cl}]+C^{(2)}[P_1]+C^{(2)}[P_2]
\tag{200.A13}
\]

exactly, and this report estimates neither `P_1` nor `P_2` separately.
If `U` is one actual common-domain transport and `M_j` are multiplication
by these masks, then

\[
 \sum_j[M_j,U]=[I,U]=0.
\tag{200.A14}
\]

For a point transport this is simply
`sum_j(P_j(x)-P_j(Ux))=0`, with `g` recomputed at `Ux`. It is invalid to
hold `g` fixed if the transport changes it. Different sector transports,
incompatible extensions, or separate spectral projectors do not share
(200.A14) automatically. Physical support changes still occur through
the two actual endpoint coefficients. Thus the Round-199 missing fourth
corner may be restored in the complete source, but its completed
coefficient need not be small.

### 3.4 Natural coordinates: geometry is separable from arithmetic deletion

**Complete endpoint ordering.** Split `E` into the two product-parity
classes and order each by `(N_i,d_i)`. For a fixed lower endpoint `i`,
the allowed upper endpoints `N_i<N_j<N_i+R` form one interval in this
ordered list. Equal-product endpoint ties form complete consecutive
groups, so the strict boundary removes the whole group, correctly.
All endpoint squarefree, coprime, residual-selector and literal masks are
already inside the one-variable vectors `b_i,b_j`.

The Fejer weight adds no power or unnormalized `N/R` factor: for integer
`r` with `0<r<R`,

\[
 1-r/R=\frac1R\sum_{s=1}^{R-1}\mathbf1_{r\le s}.
\tag{200.A15}
\]

Thus it is an average of interval masks. The two parity pieces cost only
a constant, or can be retained as one block diagonal operator.

**Original arithmetic gcd chart.** Fix odd `d,d'`, let
`g=(d,d')`, `d=g alpha`, `d'=g beta`, `(alpha,beta)=1`. An even shift
requires `g|r`; put `k=r/g`, which is even. Choose the unique residue

\[
 m_0=[-k\bar\alpha]_\beta,\qquad
 m'_0=(\alpha m_0+k)/\beta
\]

for `beta>1`, and `m_0=0,m'_0=k` for `beta=1`. Every solution is exactly

\[
 m=m_0+\beta t,\qquad m'=m'_0+\alpha t,\qquad t\in\mathbb Z.
\tag{200.A16}
\]

Positivity is imposed first. Both slopes are positive. The height,
frequency shell and cone conditions are interval conditions in `t`:

\[
 1\le m,m'\le H,\quad d/16<m<d/4,\quad d'/16<m'<d'/4,
\]

together with the two fixed shell ranges. Each extra fixed ratio-cell
inequality has interval sections because `m/d` and `m'/d'` are monotone
in `t`. A finite union of geometric cells therefore has the corresponding
finite interval count. Half-weight endpoint traces are singletons with
their original scalar multiplier. A normalized-BV profile is a weight,
not an arbitrary sharp set.

In contrast, the conditions

\[
 \mu^2(g\alpha(m_0+\beta t)),\quad
 \mu^2(g\beta(m'_0+\alpha t)),\quad
 \rho_{g\alpha(m_0+\beta t)}(g\alpha),\quad
 \rho_{g\beta(m'_0+\alpha t)}(g\beta)
\tag{200.A17}
\]

are arithmetic sequences, not proved bounded unions of intervals.
Fixed-prime divisibility is a congruence condition, squarefreeness deletes
many congruence classes, and the selector depends on the varying product.
The inherited exact arithmetic-deletion control in K185 already shows
that adjacent primitive sites can have different squarefree/coprime
status. The same point applies to any trace field whose interval formula
has not been supplied. One must retain these in the amplitude or kernel;
the geometric interval lemma cannot remove them for free.

The original gcd chart has unique `t`; there are `O(1+g)` geometric sites
on a row. It contains both orientations and the monotone sector before
any optional subdivision.

**Primitive opposing chart.** K185.18--36 gives another exact chart:
in the plus orientation
`d=kappa gU`, `d'=kappa gU+2gS`, `m'=kappa v`,
`m=kappa v+2w`, `Sv-Uw=h>0`, `r=2 kappa g h`;
the minus orientation interchanges the endpoint pattern and has
`Uw-vS=h>0`. Along either canonical affine row,
`S=S_0+Ut`, `w=w_0+vt`. Its positivity and geometric conditions again
have interval sections; the arithmetic deletions do not disappear.
The signs are exactly `(-1)^(S_0+t)` because `U,g` are odd. Both
orientations remain in (200.A10); this is a coordinate check, not a new
restriction to a particular height or packet.

### 3.5 Actual coefficient norms and the precise limitation of all-vector bounds

On complete endpoint indices the actual mixed amplitude is

\[
 A_{ij}=b_j\overline{b_i}.
\]

For the complex projective norm with decompositions
`A_ij=sum_n u_n(i)v_n(j)` (no unannounced conjugation),

\[
 \boxed{\|A\|_\pi=\|b\|_2^2\ll_\epsilon L^2X^\epsilon.}
\tag{200.A18}
\]

The upper bound is the displayed rank-one decomposition. For the lower
bound, test the corresponding rank-one dual product functional, whose
bilinear norm is one, or use Cauchy in each factor of any decomposition.
The same statement in product indices is `||c\otimes conjugate(c)||_pi=D`.
There is no loss from a mysterious mixed amplitude in these coordinates.

However, the unmasked phase matrix is

\[
 K_{ij}=e(\sigma\sqrt{XN_j})e(-\sigma\sqrt{XN_i}).
\tag{200.A19}
\]

It is rank one, with all-vector bilinear norm `#E` on a square endpoint
domain (or `sqrt(#I #J)` on a rectangle). Applying an interval-mask lemma
to this unmasked norm is therefore much worse than the target; the
phases can be absorbed in arbitrary test vectors.

One can instead retain the gap/parity/Fejer mask in the kernel. Its
absolute row and column sums are at most
`R max_(N~L^2) tau(N)<<_epsilon L X^epsilon`: there are `O(R)` possible
products, and at most the divisor multiplicity at each. Schur's elementary
Cauchy bound and (200.A18) give precisely

\[
 |C^{(2)}|\ll_\epsilon L^3X^\epsilon.
\tag{200.A20}
\]

In product indices the masked phase matrix is diagonally unitarily
conjugate to the nonoscillatory even-gap matrix. An all-vector improvement
for this representation cannot exploit `X`. On a long *ambient* interval
of integer products, a constant vector after dephasing gives a Rayleigh
quotient of order `R` for the symmetric even-gap matrix. This is a
finite all-vector operator control, **not** a lower bound for the actual
arithmetic vector and not a refutation of (200.A5).

There is an equivalent fixed-`d,d'` view. The complete pair coefficient
factors into a vector in `m` and a vector in `m'`. The determinant strip
`0<d'm'-dm<R` has `O(1+R/d')=O(1)` possible upper `m'` per row and
`O(1)` lower `m` per column. Hence its Schur norm is `O(1)` and the two
vector norms have product `O(L X^epsilon)`. Summing over `O(L^2)` choices
of `(d,d')` again costs `L^3 X^epsilon`. This displays exactly where
positive outer recombination loses the remaining `L`.

### 3.6 Exact missing actual-vector analytic estimate

Let

\[
 Z(\theta)=\sum_N c_Ne(\sigma\sqrt{XN})e(N\theta),\qquad
 F_R(\theta)=\frac1R\left|\sum_{j=0}^{R-1}e(j\theta)\right|^2,
\]

and define the nonnegative parity-Fejer multiplier

\[
 F_R^{\rm even}(\theta)=\tfrac12
       (F_R(\theta)+F_R(\theta+\tfrac12)).
\]

Finite Fourier orthogonality gives exactly

\[
 \mathcal Q_R(z):=\int_0^1F_R^{\rm even}(\theta)|Z(\theta)|^2d\theta
 =D+2\Re C^{(2)}.
\tag{200.A21}
\]

Thus, using (200.A11), the exact missing estimate can be written

\[
 \boxed{\int_0^1F_R^{\rm even}(\theta)
 \left|\sum_N\sum_d\chi_4(d)\lambda_{N,\sigma}(d)
          e(\sigma\sqrt{XN}+N\theta)\right|^2d\theta
 \ll_\epsilon L^2X^\epsilon,\quad R=\lceil L\rceil.}
\tag{200.A22}
\]

It is equivalent to the required upper bound at the epsilon-loss level,
not to any shiftwise absolute estimate. The trivial bound
`sup F_R^even<=R` and Parseval give only `R D`, explaining the missing
factor `L` without introducing a new complement. This interface retains
the actual character, selector, Vaaler factor, all endpoints and both
opposing orientations through the complete coefficient `c_N`.

No theorem in the assigned accepted context proves (200.A22). Its form
does not identify a Kloosterman sum, a modulus, an exceptional set, or a
source-compatible all-vector saving. No such identification is claimed.

For completeness, a future exact arithmetic reindexing could have

\[
 C^{(2)}=E+\sum_\nu\gamma_\nu
     \sum_{i,j}A^\nu_{ij}M^\nu_{ij}K^\nu_{ij},
\tag{200.A23}
\]

where `M^nu` has at most `J_nu` geometric column intervals per row,
all residual arithmetic masks belong to `A^nu` or `K^nu`, and `E`
contains every separately justified error/exceptional term. If the
unmasked all-vector bound for `K^nu` is `B_nu ||u||_2 ||v||_2`, then
the finite dyadic interval lemma gives the sufficient bound

\[
 \Re C^{(2)}\le |E|+
 \sum_\nu |\gamma_\nu|\,2J_\nu(1+\lceil\log_2 n_\nu\rceil)
       B_\nu\|A^\nu\|_\pi.
\tag{200.A24}
\]

An average of Fejer masks as in (200.A15) changes no power. Formula
(200.A24) charges every reconstruction constant, multiplicity,
completion, exceptional piece and mixed norm explicitly. It is a
stronger sufficient route, not a restatement that makes separate
absolute values necessary. The first missing hypotheses in a proposed
import are the exact source-compatible `K^nu`, the actual `B_nu`, and
the projective-norm sum after all arithmetic masks. Merely decomposing
the amplitude into products does not bound that sum affordably.

### 3.7 Even-parity connector and restored power

For the full-line sliding energy

\[
 \mathfrak E_R=\frac1R\sum_s\left|\sum_{j=0}^{R-1}z_{s+j}\right|^2,
\]

split each window into even and odd offsets and use
`|a+b|^2<=2|a|^2+2|b|^2`. A pair at an even gap `r` occurs in
exactly `R-r` windows. The exact conclusion is

\[
 \mathfrak E_R\le2D+4\Re C^{(2)}=2\mathcal Q_R(z).
\tag{200.A25}
\]

For odd `R>=3`, terminal positive even gap `R-1` has coefficient `4/R`;
for even `R>=4`, terminal positive even gap `R-2` has coefficient `8/R`.
For `R=1,2`, `C^(2)` is empty; the identity and connector remain valid
(although `R=1` is outside the present `L>=2` shell range). Zero extension
handles every shell endpoint, so there is no boundary correction.

If the product support fits in `M~L^2` integer sites, summing the windows
back and applying Cauchy gives

\[
 \left|\sum_Nz_N\right|^2\le\frac{M+R-1}{R}\mathfrak E_R.
\tag{200.A26}
\]

The complete power ledger is therefore:

| Stage | Bound presently justified | Bound needed |
|---|---:|---:|
| Endpoint vector squared norm; product diagonal | `L^2 X^epsilon` | Already sufficient |
| Complete correlation / parity energy | `L^3 X^epsilon` | `L^2 X^epsilon` |
| Window reconstruction prefactor | `L` | Fixed by `R~L` |
| Residual scalar squared | `L^4 X^epsilon` | `L^3 X^epsilon` |
| Residual scalar | `L^2 X^epsilon` | `L^(3/2) X^epsilon` |
| Original stationary M1 shell after (200.A7) | `X^(1/4)L^(1/2)X^epsilon` | `X^(1/4)X^epsilon` |

The high-height ledger `Y L^2` versus `L^2` is only a subsidiary
chart-specific deficit. It is not the full-source capacity, and it is
not used here to replace the required complete factor `L`.

If an imported estimate earns a factor `X^-delta` and all remaining
costs relative to (200.A20) total `X^a`, while `L=X^ell`, the required
net saving is `delta-a>=ell` up to epsilon loss. Equivalently a modulus
saving `c^-delta` with `c~X^gamma` must satisfy `gamma delta-a>=ell`.
This is a ledger condition, not an asserted available saving.

Adding the accepted XOR scalar sector to a proof of (200.A22) would
close exactly the complete original-`t=1` scalar. It would not close the
other small-`t` incidences or either complete M1 parent.

## 4. First doubtful or unproved step

The first analytic open step on the complete source is (200.A22),
equivalently (200.A5). The elementary norm bounds above stop at
`L^3 X^epsilon`. There is no established coefficient-sensitive argument
for removing the full factor `L` after all endpoint allocations have
been restored.

The first source-detail seam for a *different arithmetic bilinear
import* is also explicit: (200.A8) does not provide a scalar formula
for every later literal trace. Such a trace must stay inside the exact
coefficient until its formula and any claimed interval/norm bound have
been verified. The endpoint-index route avoids needing that additional
norm assertion because its amplitude is exactly rank one.

No claim is made that the actual target is false. The all-vector
dephasing control only rejects a saving from the unrestricted endpoint
phase norm. The report does not replace the actual coefficients by an
unsigned, assigned-sign, or adversarial array in the proposed theorem.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `complete_source_multiplicity` | Pass: divisor opening and ordered endpoint pairing are inverse maps; `r`, both orientations and all gcd labels are reconstructed uniquely. |
| `actual_coefficients_only` | Pass: (200.A2) is retained throughout; (200.A6) is not substituted for missing trace fields. |
| `literal_endpoint_zero_extension` | Pass: cemetery values are zero; positivity precedes square roots; shell/cone/height endpoints remain literal; no lost half-weight trace. |
| `partition_recombination` | Pass: (200.A12)--(200.A14), with recomputed gcd and one common genuine transport. No analytic gain claimed. |
| `row_interval_vs_arithmetic_masks` | Pass: endpoint-product windows and geometric affine-row cells are intervals; arithmetic masks (200.A17) remain in coefficients/kernel. No interval assertion for unspecified traces. |
| `product_and_projective_norms` | Pass: exact complete endpoint rank-one norm (200.A18); alternative-coordinate mixed norms are charged in (200.A24). |
| `even_parity_connector` | Pass: (200.A21), (200.A25), both terminal coefficients and full zero extension are exact. |
| `one_outer_real_part` | Pass: frozen target is (200.A5); stronger absolute estimates are explicitly only sufficient methods. |
| `net_power_ledger` | Pass: complete `L^3` to `L^2` correlation deficit, `O(L)` scalar-square reconstruction and original stationary factor are all displayed. |
| `no_capacity_lower_bound` | Pass: every capacity is an upper envelope. Ambient all-vector dephasing is not actual-vector lower mass. |
| `no_unverified_theorem_import` | Pass: no web theorem was imported; the strategy literature list was read only as strategy. |
| `protected_parent_and_exponent_scope` | Pass: no original `t>=2`, full M1/M2, endpoint-uniformity, bridge or exponent claim. |

All controls are finite algebra or accepted-source hypothesis checks.
No numerical example or experiment certifies an asymptotic statement.

## 6. Dependencies and exact artifacts used

Assigned context read:

1. `protocol.md`.
2. `state/proof_obligations.yml`, raw SHA-256 above; relevant named nodes
   inspected rather than the full graph dumped.
3. `state/active_campaign.yml`.
4. `strategy/round200_complete_source_coefficient_mask_strategy.md`.
5. `proofs/kernels/m9_m1_hard_top_t1_comparable_factor_exchange_sector_and_residual_fejer_reduction.md`.
6. `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md`.
7. `proofs/kernels/m9_m1_hard_top_small_t_primitive_ray_sector_and_truncated_mobius_self_return.md`.
8. `strategy/gauss_circle_strategy_review_2026-09-23.md`.
9. `proofs/kernels/m9_m1_hard_top_t1_p2_cross_gcd_cellular_boundary_self_return.md`.

Additional exact antecedents read, with purpose:

10. `rounds/codex-managed/m9-combined-top-cones/reports/blind_m1_top_transform.md`:
    exact Vaaler/stationary factors, sign and shell reconstruction constant,
    endpoint convention, and strict cone.
11. `rounds/codex-managed/m9-endpoint-fixed-profile-attack/reports/dyadic_profile_certificate.md`:
    actual fixed profile construction and hard endpoint sample.
12. `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reports/literal_t1_exchange_residual_attack.md`, initial definition/derivation sections:
    exact residual-selector convention and literal coefficient antecedent.
13. `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reviews/coefficient_profile_endpoint_power_post_repair_verification.md`:
    exact moving-factor ledger and scope of retained literal fields.
14. `proofs/kernels/m9_m1_hard_top_squarefree_radical_reduction_and_self_return.md`:
    original-`t=1` incidence meaning and product support.
15. `rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/reviews/coefficient_product_endpoint_seam_review.md`, relevant coefficient sections:
    location of floor/star/half/endpoint fields in the inherited symbol.
16. `rounds/codex-managed/m9-combined-top-cones/reports/combined_cone_algebra.md`, sections 1--3:
    cross-check of the positive stationary constant and explicit M1 symbol.
17. `proofs/kernels/m9_m1_hard_top_t1_rho_large_gcd_scaled_close_sector.md`,
    statement and exact-complement sections: `D_L` and `P_cl/P_1/P_2` definitions.
18. `proofs/kernels/m9_m1_hard_top_t1_p2_common_cell_allocation_commutator_sector.md`,
    source and K197.C8b--C9c sections: closed list of sharp labels and physical atom.
19. `rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/m1_terminal_arithmetic_attack.md`,
    coefficient-definition sections: `eta_L`, its BV normalization, and height truncation.

Relevant graph nodes inspected: `H4-Phi-regularity`,
`M9-M2-dyadic-weight-nondegeneracy`, `M9-M1-top-endpoint-transform`,
`M9-M1-frequency-phase-diagram-R10`, `Divisor-bound-elementary`,
`M9-M1-hard-top-squarefree-radical-sector-reduction`,
`M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector`,
`M9-M1-hard-top-t1-comparable-factor-exchange-sector`,
`M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction`, and the open
`M9-M1-hard-top-high-radical-small-t-residual-estimate`.

No current sibling report, blind packet or blind derivation was read.
The conductor confirmed the intended one-real-part and scope conventions
by message, without supplying its derivation. No legacy directory was
modified. No external source was relied upon.

## 7. Recommended state effect

**Retain** the full original-`t=1` residual as open. Archive the exact
complete-source reconstruction, coordinate-dependent norm distinction,
and conditional estimate (200.A22)/(200.A24) as candidate analytical
interface evidence. The finite identities may be independently reviewed;
this report does not itself request a new accepted theorem node.

The correct terminal label is
`complete_source_interface_with_open_estimate`. No state effect beyond
reviewed analysis evidence is justified. In particular, keep every
original `t>=2` incidence, the large-`G` near-resonant complement, the
complete small-`t` owner, both M1 parents, every M2 owner, endpoint
uniformity, M9, both bridges, the quarter theorem and every exponent
unchanged. Stop this task after delivery; do not initiate another round.
