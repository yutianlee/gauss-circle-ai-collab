# Round 172 selection audit: maximal-scale Fejer dyadic-increment gate

Starting graph: `c98f95b6b3500d0f48365af338e543f9a0f251b22062f3898df5f448d6b54853`

Role: bounded pre-round interface audit.  This report neither designs nor
launches Round 172 and makes no proof-state change.

## 1. Result

The maximal-scale hard-TOP residual frontier (165.K26) is still an exact,
open, one-sided sufficient theorem with a restored factor-
\(L\) deficit.  Its coefficient-uniform capacity is
\(L^4X^\varepsilon\), whereas the required energy budget is
\(L^3X^\varepsilon\).

A genuinely different first gate is available before returning to a
fixed-shift, rowwise, or product-collar argument: decompose the parity-
projected Fejer energy into **signed dyadic scale increments**.  The exact
increment has zero diagonal and is simultaneously

1. a triangular tent aggregate in the full \((r,N)\) variables;
2. a difference of two parity-projected Fejer multipliers; and
3. at exact doublings, a block-energy minus an adjacent-block Haar-detail
   energy.

The recommended frozen identity-or-no-go experiment is the one-sided,
actual-symbol bound

\[
 \boxed{
 \mathfrak E_{R_{j+1}}^{(2)}-\mathfrak E_{R_j}^{(2)}
 \le C_\varepsilon L^3X^\varepsilon
 }
 \tag{172.DF}
\]

on the canonical doubling chain from \(R_0=\lceil L\rceil\) to
\(M_L\).  There must be no modulus inside either the shift sum or the
\(N\)-sum.  Proving (172.DF) on every link proves (165.K26), up to the
already target-safe short-shift correction and an absorbable logarithm.
Nothing in this audit proves (172.DF); failure at its actual-symbol Haar
gate should be recorded as a scoped no-go.

## 2. Exact statement and hypotheses

Retain the complete literal Round-164/165 residual coefficient
\(c_N^{\rm rem}\), including the supported squarefree rows, the neither/both
selector (and no-pair branch), both parity branches, every hard profile and
point value, endpoints, and global zero extension.  Put

\[
 J=\sqrt X,\qquad z_N=c_N^{\rm rem}e(J\sqrt N),\qquad
 D_L=\sum_N|c_N^{\rm rem}|^2\ll_\varepsilon L^2X^\varepsilon,
\]

where \(z_N=0\) off the positive literal shell and a consecutive interval
of cardinality \(M=M_L\asymp L^2\) contains that shell.  The inherited
range is \(1\ll L\ll H\le J^{1/2}\).  Define

\[
 A_r=\Re\sum_N z_{N+r}\overline{z_N}
 =\Re\sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right).
 \tag{172.1}
\]

The exact open K26 scalar is

\[
 \boxed{
 T_{26}:=
 \sum_{\substack{R_0\le r<M\\2\mid r}}
 \left(1-{r\over M}\right)A_r
 \ll_\varepsilon L^3X^\varepsilon.}
 \tag{172.2}
\]

This is a one-sided real-part estimate, not a sum of moduli.  Let

\[
 F_R(\theta)={1\over R}\left|\sum_{j=0}^{R-1}e(j\theta)\right|^2,
 \qquad
 K_R^{(2)}(\theta)={F_R(\theta)+F_R(\theta+1/2)\over2},
 \tag{172.3}
\]

and \(Z(\theta)=\sum_Nz_Ne(N\theta)\).  The parity-projected Fejer energy is

\[
 \mathfrak E_R^{(2)}
 :=\int_0^1|Z(\theta)|^2K_R^{(2)}(\theta)\,d\theta
 =D_L+2\sum_{\substack{1\le r<R\\2\mid r}}
 \left(1-{r\over R}\right)A_r.
 \tag{172.4}
\]

Choose the exact integer chain

\[
 R_0=\lceil L\rceil,\qquad
 R_{j+1}=\min(2R_j,M),qquad R_K=M,
 \tag{172.5}
\]

with repetitions omitted.  It has \(K=O(\log L)\) links.  The proposed
Round-172 gate is (172.DF) for every link of (172.5), uniformly with the
literal coefficient and all inherited endpoints.

## 3. Proof or derivation

Parseval and

\[
 {F_R(\theta)+F_R(\theta+1/2)\over2}
 =\sum_{\substack{|r|<R\\2\mid r}}
 \left(1-{|r|\over R}\right)e(r\theta)
\]

prove (172.4) exactly.  Therefore

\[
 \begin{aligned}
 {1\over2}\bigl(\mathfrak E_M^{(2)}-
                    \mathfrak E_{R_0}^{(2)}\bigr)
 &=T_{26}
   +\sum_{\substack{1\le r<R_0\\2\mid r}}
     r\left({1\over R_0}-{1\over M}\right)A_r,\\
 T_{26}
 &={1\over2}\sum_{j=0}^{K-1}
   \bigl(\mathfrak E_{R_{j+1}}^{(2)}-
         \mathfrak E_{R_j}^{(2)}\bigr)-B_{\rm short},
 \end{aligned}
 \tag{172.6}
\]

where the second term in the first line is \(B_{\rm short}\).  Fixed-shift
Cauchy gives \(|A_r|\le D_L\), hence

\[
 |B_{\rm short}|
 \le D_L\left({1\over R_0}-{1\over M}\right)
       \sum_{\substack{1\le r<R_0\\2\mid r}}r
 \ll_\varepsilon R_0D_L
 \ll_\varepsilon L^3X^\varepsilon.
 \tag{172.7}
\]

Thus (172.DF), summed over \(O(\log L)\) links and with the logarithm
absorbed into \(X^\varepsilon\), implies (165.K26).

For an exact doubling link \(R\mapsto2R\), the correlation kernel in the
increment is the triangular tent

\[
 w_{2R}(r)-w_R(r)=
 \begin{cases}
 r/(2R),&0<r<R,\\
 1-r/(2R),&R\le r<2R,\\
 0,&r\ge2R,
 \end{cases}
 \qquad w_R(r)=(1-r/R)_+.
 \tag{172.8}
\]

Consequently

\[
 \mathfrak E_{2R}^{(2)}-\mathfrak E_R^{(2)}
 =2\sum_{\substack{1\le r<2R\\2\mid r}}
   \bigl(w_{2R}(r)-w_R(r)\bigr)A_r,
 \tag{172.9}
\]

an aggregate signed \((r,N)\) scalar with no diagonal.

There is also an exact Haar form.  For any zero-extended sequence \(w\),
put

\[
 \mathcal E_R(w)={1\over R}\sum_s
 \left|\sum_{j=0}^{R-1}w_{s+j}\right|^2,
 \quad
 \mathcal H_R(w)={1\over2R}\sum_s
 \left|\sum_{j=0}^{R-1}w_{s+j}
       -\sum_{j=R}^{2R-1}w_{s+j}\right|^2.
\]

The parallelogram identity and translation of the full-line window sum give

\[
 \mathcal E_{2R}(w)=2\mathcal E_R(w)-\mathcal H_R(w).
 \tag{172.10}
\]

Since
\(\mathfrak E_R^{(2)}=\tfrac12\{\mathcal E_R(z)+
\mathcal E_R((-1)^Nz_N)\}\), (172.10) yields

\[
 \mathfrak E_{2R}^{(2)}-\mathfrak E_R^{(2)}
 =\mathfrak E_R^{(2)}-\mathfrak H_R^{(2)},
 \qquad
 \mathfrak H_R^{(2)}={\mathcal H_R(z)+
 \mathcal H_R((-1)^Nz_N)\over2}\ge0.
 \tag{172.11}
\]

Thus the first substantive gate is not another formal Fejer identity.  It
is an actual-symbol lower bound for adjacent-block detail strong enough to
give
\(\mathfrak H_R^{(2)}\ge\mathfrak E_R^{(2)}-
O_\varepsilon(L^3X^\varepsilon)\).

The restored power ledger is sharp at this interface.  Cauchy or the
Fejer multiplier supremum gives only

\[
 \mathfrak E_R^{(2)}\ll RD_L
 \ll_\varepsilon RL^2X^\varepsilon.
 \tag{172.12}
\]

At \(R\asymp L\) this is target-scale, but at \(R\asymp M\asymp L^2\)
it is \(L^4X^\varepsilon\).  A scale \(R\) therefore needs a saving of
\(R/L\), whose worst value is \(L\).  Equivalently, the direct K26 sum has
\(\asymp M\) weighted shift capacity times \(D_L\), namely
\(L^4X^\varepsilon\), against the \(L^3X^\varepsilon\) target.

## 4. First doubtful or unproved step

No estimate resembling (172.DF), or the equivalent actual-symbol Haar
detail lower bound in (172.11), is proved.  The Fejer transform, the
telescoping, and the Haar identity are exact but by themselves save no
power.  The first doubtful step is whether the literal arithmetic
coefficient and square-root phase force enough adjacent-block detail at
the top scales without taking absolute values in \(r\), in \(N\), or in a
dual variable.

Large real derivatives do not supply uniform distance from integers.  The
frozen character on even cofactor-gcd rows is not itself cancellation.
Likewise, positivity of \(\mathfrak H_R^{(2)}\) is useful only after a
coefficient-sensitive lower bound; replacing it by the trivial lower bound
zero returns the full \(L^4\) capacity.

## 5. Required controls, parked placements, and hard stop

- **Endpoint/zero-extension control — PASS.**  Equations (172.3)--(172.11)
  use full-line zero-extended windows.  No square root is evaluated off the
  positive pair domain, and the final non-doubling link in (172.5) uses the
  exact Fejer difference rather than an unproved rounded Haar formula.
- **Short-shift budget — PASS, with no spare power.**  Equation (172.7)
  costs \(L^3X^\varepsilon\).  It may be paid once, but cannot be repeated
  after a shiftwise triangle inequality.
- **Phase-aligned arbitrary-array control — FAILS coefficient-uniformly as
  required.**  If \(z_N=1\) on \(M\) consecutive sites, then
  \(A_r=M-r\) and the even K26 scalar is \(\asymp M^2\asymp L^4\).
  The same failure occurs for \(z_N=(-1)^N\), because all even-gap
  correlations remain positive.  Hence both Fejer peaks, at \(0\) and
  \(1/2\), are necessary and no coefficient-uniform theorem can prove
  (172.DF).
- **Single-spike normalization control — PASS.**  A one-site sequence has
  \(\mathfrak E_R^{(2)}=D_L\) at every scale and zero increments, confirming
  that (172.DF) contains no artificial endpoint or diagonal term.
- **Global Parseval/positive-energy control — FAIL.**  Using only
  \(\int|Z|^2=D_L\) and \(\|K_R^{(2)}\|_\infty\asymp R\) gives (172.12)
  and misses the top-scale target by \(L\).
- **One-real-part control — REQUIRED.**  A modulus may surround neither
  the individual \(A_r\) nor the individual divisor/cofactor rows.  Such a
  move returns the parked fixed-shift triangle and restores \(L^4\).
- **Owner/scope control — PASS.**  K26 can close only the complete residual
  \(t=1\) scalar through the accepted Fejer connector.  It does not close
  the rest of \(t=1\), another hard-TOP channel, hard TOP, BAL, UNBAL,
  M9--M2, either M1 route, endpoint assembly, M9, a bridge, or an exponent.

The following placements remain parked and are not admissible as silent
inputs: the distinct minimal-scale K17a theorem; fixed-\(r\) triangle
inequality and fixed-\(B\) polylogarithmic sectors as a substitute for the
non-polylogarithmic range; positive second-derivative row estimates;
completion followed by absolute dual modes; coefficient-uniform positive
transport, bounded variation, or positive rank-one collars; the audited
direct-2024 and Part-I interfaces; and the Round-169 double-Poisson
self-return, which exposes but does not estimate the signed moving product
collar.  The Round-171 local commutator/ramp obstruction belongs to BAL and
does not transfer across owners; it only reinforces the requirement that
this experiment remain nonlocal and actual-symbol sensitive.

**Hard stop.**  Stop the round and report a route-scoped no-go, without
pivoting, at the first occurrence of any of the following:

1. the exact selectors, squarefree masks, parity branches, profiles,
   endpoints, or zero extension cannot be retained in the transformed
   blocks;
2. the argument reaches only \(RD_L\), global Parseval, a nonnegative
   majorant, or a coefficient-independent Haar estimate;
3. an absolute value is inserted before the aggregate \((r,N)\) sum or
   before coupled scale recombination;
4. the top-scale increment still has \(L^4X^\varepsilon\) capacity, with
   no proved factor-\(L\) actual-symbol saving; or
5. the transform merely returns to K17a, a parked fixed-shift/dual-mode
   placement, or the Round-169 collar without a new signed connector.

## 6. Dependencies and exact artifacts used

- `protocol.md`;
- `state/proof_obligations.yml` at graph
  `c98f95b6b3500d0f48365af338e543f9a0f251b22062f3898df5f448d6b54853`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/synthesis.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/candidates/conductor_round165_variable_scale_fejer_bypass.md`;
- `rounds/codex-managed/full-proof-round167-169-strategy-literature-review/synthesis.md`;
- `rounds/codex-managed/m9-m2-balanced-critical-j1-two-defect-commutator-gate/synthesis.md`.

No external theorem, web source, numerical experiment, or unstated artifact
is used.

## 7. Recommended state effect

**No current graph change.**  Retain (165.K26), the complete residual
scalar, every parent, both proof routes, and both exponent ledgers exactly
as open/unchanged.

For Round 172, select only the dyadic parity-Fejer increment gate (172.DF)
as an identity-or-no-go objective.  Its promotion gate is an exact proof
with the literal coefficient, a statement-only rederivation of
(172.6)--(172.11), a power/endpoint seam review, the two phase-aligned false
controls above, and an owner-scope review.  If (172.DF) is proved, create a
proved actual-symbol child and use (172.6)--(172.7) to discharge K26 before
assessing the residual scalar.  If its first actual-symbol saving fails,
record only the precisely scoped dyadic-increment/Haar no-go.  In neither
case may a hard-TOP parent, M9--M2, M9, the quarter theorem, or a global
exponent be promoted automatically.
