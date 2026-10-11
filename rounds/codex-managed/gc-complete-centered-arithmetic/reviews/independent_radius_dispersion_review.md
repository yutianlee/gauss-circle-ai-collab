# Round 213 independent radius-dispersion seam

## 1. Result and verdict

Campaign: `gc-complete-centered-arithmetic`. Round: 213.
Reviewer: `centered_divisor_attack`, acting in a separate conductor-assigned
NONBLIND review after completing and hashing its discovery report.
Generated: 2026-09-28. Status: candidate review evidence only.

**PASS for the stated conditional transfer and scoped certificate no-go.**
The claimant's exact frequency support, enlarged-window reproducing-kernel
argument, `sqrt(q)` transfer cost, full shell prices, and signed model
cross terms are correct. The fully priced absolute-DD certificate has
the claimed lower bound `cN` on each fixed interior power scale.

This verdict is bound to
`reports/centered_shell_dispersion.md`, SHA-256
`f7165a8d41b9541ff54b53442f238f3d295a8dc944b1ee421a95bc6e3b51af28`.
It does not certify the unproved arithmetic radius input (R), the complete
centered target, a pointwise exponent, or any parent obligation.

## 2. Exact reviewed statements and hypotheses

Use the claimant's exact real parameters, rounded `L,K`, actual four
`r2` factors, smooth signed four-factor mask, and complete zero extension.
Let `Omega_j` be the complete shell
`q<Lambda=Thk/N^(3/2)<=2q`, `q=2^j`, and put

\[
\delta_j=|\Omega_j|/(LK),\qquad
Q_j^2=\frac1{T|\Omega_j|}\int_{T/2}^{2T}
 \sum_{\Omega_j}|D_{h,k}(R)-\rho_{h,k}I_{h,k}(R)|^2\,dR.
\]

Only the already constructed candidate's bounds
`0<=rho<<T^epsilon` are assumed; no integer mean property is required.
The reviewed sufficient arithmetic hypothesis is

\[
Q_j\ll_\epsilon T^\epsilon(\sqrt N+Nq^{-3/2})
\quad\text{for every complete nonempty shell}.                 \tag{R}
\]

The claimed consequence is the complete uniform centered estimate after
the paid transfer and shell summation. Separately, with the claimant's
exact radius integrals `X,Y,Z` and positive DD kernel sum `G`, the reviewed
certificate is

\[
C=G-2\rho\Re Y+\rho^2Z.
\]

The lower bound concerns
`sum_j delta_j sqrt(q) sqrt(mean_(Omega_j) C)`, not true signed energy.
Its asymptotic lower-bound scope is fixed
`166/325<alpha<242/325`, `N asymp T^alpha`, as stated by the claimant.

## 3. Independent derivation and seam checks

### 3.1 Actual frequency support and reconstruction

The exact mixed difference is

\[
\psi(t)=-\frac14\int_0^h\int_0^k(t+u+v)^{-3/2}\,dv\,du.
\]

Where the mask is nonzero, both `t>=N` and `t+h+k<=4N`. Thus

\[
-\frac{hk}{4N^{3/2}}\le\psi(t)
\le-\frac{hk}{32N^{3/2}}.
\]

On the entire shell the union of frequencies lies inside
`[-q/(2T),-q/(32T)]`. The discrete and continuous terms have the same
support bound. The pushforward signed measure giving `E` has total
variation `O(NT^epsilon)`; hence `E` is bounded on every real radius.
There is no need to assume that it belongs to global L2.

Choose the claimant's fixed Schwartz kernel with Fourier transform one
on `[-1,1]`. For `K_q(x)=(q/T)kappa(qx/T)`, the entire frequency interval
lies strictly inside that plateau after scaling. Fubini is justified by
finite spectral variation and the integrable kernel. It yields the exact
identity `E=K_q*E`, including the continuous model term.

In the normalized finite-dimensional shell Hilbert norm, Cauchy gives

\[
\left\|\int_{T/2}^{2T}K_q(R-s)E(s)\,ds\right\|_j
\le O(\sqrt{q/T})\,\sqrt T Q_j=O(\sqrt q Q_j).
\]

For `R in [T/sqrt(2),sqrt(3)T]`, the distance to the complement of
`[T/2,2T]` is at least
`T min(1/sqrt(2)-1/2,2-sqrt(3))>0`. The remaining integral is at most
`O_(B,epsilon)(NT^epsilon q^(-B))` by the global envelope and Schwartz
decay. This verifies claimant (8) with its exact window and tail.

The `q=1` tail may have size `N`; it is not silently discarded. Its shell
fraction is small enough for the global calculation below. A narrower
radius interval or weight vanishing at a required endpoint would not
justify the same transfer without further work.

### 3.2 Full shell summation

The exact product count gives
`delta_j<<min(1,q log(2L)/Lambda_*)`, where
`Lambda_*=TLK/N^(3/2) asymp T^(76/325)` and `sum delta_j<=1`.
The following complete sums suffice, with logarithms displayed or
absorbed into epsilon:

\[
\sum_j\delta_jq^{-B}\ll_B\frac{\log(2L)}{\Lambda_*}\ (B>1),
\qquad
\sum_j\delta_j/q\ll\frac{\log(2L)\log(2+\Lambda_*)}{\Lambda_*},
\]
\[
\sum_j\delta_j\sqrt q\le\sqrt{\Lambda_*}\sum_j\delta_j
\le\sqrt{\Lambda_*}.
\]

Inserting (R) into the verified transfer therefore costs

\[
T^\epsilon\left(\sqrt{N\Lambda_*}+N/\Lambda_*\right).
\]

At the upper band edge its two powers are respectively
`(242+76)/(2*325)=159/325` and `(242-76)/325=166/325`.
The Schwartz tail has the second price. The claimant retains the already
paid repeated and small-product sectors. Rounded lengths, bounded
cutoffs, empty shells and exact dyadic endpoints do not change these
comparisons. Thus the full normalized sum has been priced, not merely
one large-product subfamily.

### 3.3 DD, mixed and continuous-continuous signs

With all masks real and `rho` real, direct expansion is exactly

\[
|D-\rho I|^2=|D|^2-2\rho\Re(D\overline I)+\rho^2|I|^2.
\]

The claimant's `Y` uses `psi(n)-psi(t)`, hence the conjugation and sign
are correct. Radius integration produces the stated kernel
`K(y)=int_(1/2)^2 e(vy)dv` and `K(0)=3/2`; the DD diagonal is therefore
`(3/2)sum a(n)^2 W(n)^2`, of size `O(NT^epsilon)`. All eight actual
arithmetic factors remain in the DD off-diagonal.

On the enlarged positive radius interval, `|(R psi)'| asymp Lambda/N`.
Smooth compact support and repeated integration by parts give
`sup|rho I|<<_(A,epsilon)NT^epsilon q^(-A)`. The same proof works across
internal mask zeros. It follows that

\[
|Q_j(D)-Q_j(E)|\ll_{A,\epsilon}NT^\epsilon q^{-A},
\quad |\rho Y|\ll N^2T^\epsilon q^{-A},
\quad 0\le\rho^2Z\ll N^2T^\epsilon q^{-2A}.
\]

Taking `A>=3/2` verifies the claimed two-way equivalence of (R) for `D`
and `E`, with adjusted constants. The model is paid, not assumed to be
the true mean. The one-sided off-diagonal condition (6) is likewise a
valid sufficient arithmetic statement after the known diagonal is added.

### 3.4 The centered certificate, including cross-term correction

Termwise triangle inequality in DD gives `G>=X`. Since `X` is the actual
nonnegative integrated DD energy,

\[
C=(G-X)+\frac1T\int_{T/2}^{2T}|E(R)|^2\,dR\ge0.
\]

This identity is decisive: the exact negative mixed term has not been
discarded or assumed favorable. The near-zero kernel bins and Cauchy
give `G>=c M^2/(1+Lambda)`, where `M=sum|aW|`. From the verified mixed
bound and nonnegative CC term,

\[
\sqrt C\ge\sqrt G-O_{A,\epsilon}(NT^\epsilon q^{-A/2}).
\]

This follows from `G<=C+O(N^2T^epsilon q^(-A))`; it remains valid even
when the preliminary lower bound for `C` is negative.

The permitted closed-212 report proves actual residual mass
`sum_Omega M>=cLKN` through two finite moving-sum inequalities and the
elementary circle first moment. For fixed `0<eta<76/325`, the claimant's
removal of shells `q<T^eta` costs at most
`O(NT^epsilon U T^eta log(2L))=o(LKN)` after choosing epsilon sufficiently
small. Therefore positive actual mass remains on the high shells.

Without bandwidth cost this yields `mean sqrt C>>N/sqrt(Lambda_*)`,
provided `A eta/2>38/325` with room for epsilon. For the fully priced
certificate, concavity has the correct direction:

\[
\sum_j\delta_j\sqrt q\sqrt{\operatorname{mean}_{\Omega_j}C}
\ge\frac1{LK}\sum_{q\ge T^\eta}\sqrt q\sqrt C.
\]

On a shell, `sqrt(q/(1+Lambda))>=1/sqrt(3)`. The main term is consequently
at least a fixed constant times `mean_high M>>N`; the error is at most
`O(NT^epsilon T^(-eta(A-1)/2))=o(N)` for sufficiently large fixed `A`.
This proves the claimant's `cN` lower certificate and its power deficit
`alpha-166/325`. The upper-edge supremal deficit `76/325` is correct.

The actual signed energy can be much smaller than this certificate.
Neither concavity nor binning reverses the certificate upper bound into
a lower bound for the original target.

## 4. First unproved step and limits

The first missing input remains (R), or an equivalent sufficient signed
off-diagonal control with the DD/mixed/CC terms retained, throughout the
enlarged radius interval and all complete shells. The transfer does not
prove that input. A diagonal estimate alone does not bound the strongly
dependent signed eight-factor off-diagonal.

The phrase that (R) is a weaker averaged input is justified relative to
requiring a diagonal-sized fixed-radius shell energy. It should not be
read as claiming a proved logical implication from every older two-term
fixed-radius gate; the formulas, rather than that general phrase, define
the accepted conditional comparison. This is a scope clarification, not
a mathematical defect in the stated implication.

The no-go applies precisely to replacing DD's radius kernel by its
modulus while retaining exact scalar model cross terms. It does not
exclude a genuinely signed radius estimate or a different arithmetic
method. The fixed `102/325` consequence would still not be the quarter
theorem.

## 5. Required controls and outcomes

| Control | Review outcome |
|---|---|
| Actual arithmetic coefficients | PASS: actual four/eight factors and inherited actual mass, no surrogate coefficients. |
| Complete shifts and overlap | PASS: complete shells and zero extensions; high-shell restriction occurs only inside a positive lower certificate. |
| Frequency normalization | PASS: support `[-q/(2T),-q/(32T)]`, Fourier plateau and scaling are compatible. |
| Hilbert radius transfer | PASS: normalized shell norm, enlarged interval, `sqrt(q)` and global-envelope tail all paid. |
| DD/mixed/CC signs | PASS: conjugation, `-2rho Re Y`, nonnegative `rho^2Z` and `C>=0` are exact. |
| Density and local/global distinction | PASS: only a bounded candidate is used; no true mean or short-interval error is inferred. |
| Real endpoints and powers | PASS: exact ceilings, open band, uniform upper bounds and fixed-interior lower scope are explicit. |
| Signed/certificate distinction | PASS: lower bounds concern the specified certificate only. |
| Full quarter and graph scope | PASS: arithmetic input remains open and no parent/exponent promotion is justified. |
| Statement-only isolation | Not applicable: this is an explicitly nonblind seam, undertaken only after the reviewer's discovery report was frozen. |

All checks are analytical. No numerical experiment or external source
search was performed during this seam. No mathematical repair is
requested at the reviewed hash.

## 6. Exact dependencies, access and hash binding

Permitted review context used:

1. `protocol.md`, SHA-256
   `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
2. Claimant `rounds/codex-managed/gc-complete-centered-arithmetic/reports/centered_shell_dispersion.md`,
   SHA-256 `f7165a8d41b9541ff54b53442f238f3d295a8dc944b1ee421a95bc6e3b51af28`.
3. Closed-212 actual-mass dependency
   `rounds/codex-managed/gc-complete-four-point-correlation/reports/four_point_oscillatory_attack.md`,
   SHA-256 `7c84d41e28c726d39b13cfe6b1e65f6cf8800ff746ca43b56157954908db423f`.

The reviewer's discovery report was completed and reported to the
conductor at SHA-256
`7f826451cb58b578e93c5b4e471eb3ccdc0cda60276fc60551695a1d80e3407e`
before this claimant was opened. No current blind packet/report,
conductor ledger, sibling beyond this explicitly authorized claimant,
shared state, successor artifact or external source was read for the seam.
The reviewer does not claim statement-only isolation or independent
discovery of every result.

Only this assigned review file is written in the seam. All other
artifacts remain unmodified by the reviewer.

## 7. Recommended state effect

**Retain** the verified conditional radius gate, paid transfer, complete
shell calculation and centered absolute-DD certificate obstruction as
reviewed strategy evidence at the specified claimant hash.

**No change** to accepted arithmetic bounds, pointwise exponents, moments,
M1/M2, endpoint obligations or the proof draft. Do not promote (R) or the
complete centered target. The scoped certificate failure is proved; the
actual signed remainder remains open. Stop after this review.
