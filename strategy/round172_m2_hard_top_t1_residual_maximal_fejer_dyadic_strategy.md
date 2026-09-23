# Round 172 strategy: maximal residual parity-Fejer dyadic-frequency gate

## Conductor decision

Round 171 closes the displayed local balanced commutator route without
proving or disproving the physical critical remainder.  Three independent
post-closure selection audits agree that the balanced alternatives do not yet
offer an equally exact new interface and that the accepted maximal-scale
hard-TOP residual theorem (165.K26) is the sharpest ready frontier.

Round 172 therefore freezes only the maximal even medium/long Fejer
aggregate.  Its first new mechanism is a dyadic parity-Fejer bandpass: remove
the diagonal exactly by taking adjacent-scale differences, express each
difference both as a signed triangular tent in \((r,N)\) and as a
block-versus-Haar-detail identity, and then test a finite character-Poisson
transform on the common Fejer frequency before any positive sum over dual
modes.

This is an identity-or-no-go experiment, not evidence that the target holds.
The round may not pivot to K17a, the Round-169 product collar, BAL, another
hard-TOP channel, or a global owner.

## Frozen literal target

Let \(J=\sqrt X\), \(1\ll L\ll H\le J^{1/2}\),
\(R_0=\lceil L\rceil\), and let an interval of
\(M=M_L\asymp L^2\) sites contain the literal residual product shell.
Extend the complete accepted residual coefficient \(c_N^{\rm rem}\) by zero
and put

\[
 z_N=c_N^{\rm rem}e(J\sqrt N),\qquad
 D_L=\sum_N|c_N^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
\tag{172.S1}
\]

The sole theorem target is

\[
 \boxed{
 T_{26}:=
 \Re\!\sum_{\substack{R_0\le r<M\\2\mid r}}
 \left(1-\frac rM\right)
 \sum_Nc_{N+r}^{\rm rem}\overline{c_N^{\rm rem}}
 e\!\left(J(\sqrt{N+r}-\sqrt N)\right)
 \ll_\varepsilon L^3X^\varepsilon.}
\tag{172.S2}
\]

There is exactly one outer real part.  Every residual selector, no-pair row,
squarefree mask, \(\chi_4\) factor, complementary parity branch, profile,
floor, star, crossing, endpoint, point value, and zero-extension jump remains
inside \(c_N^{\rm rem}\).

The positive coefficient-uniform capacity is
\(L^4X^\varepsilon\), so precisely one factor \(L\) is missing.  Proving
(172.S2) closes only the complete residual \(t=1\) scalar through the accepted
Fejer connector.  It does not close the rest of \(t=1\), hard TOP, BAL,
UNBAL, M9--M2, M1, GAR, endpoint assembly, M9, either bridge, or the quarter
theorem.

## Exact dyadic and frequency interfaces

Write

\[
 A_r=\Re\sum_Nz_{N+r}\overline{z_N},
\qquad
 F_R(\theta)=\frac1R\left|\sum_{0\le j<R}e(j\theta)\right|^2,
\]

\[
 K_R^{(2)}(\theta)=\frac{F_R(\theta)+F_R(\theta+1/2)}2,
\qquad
 Z(\theta)=\sum_Nz_Ne(N\theta).
\tag{172.S3}
\]

Then exactly

\[
 \mathfrak E_R^{(2)}
 :=\int_0^1|Z(\theta)|^2K_R^{(2)}(\theta)\,d\theta
 =D_L+2\!\sum_{\substack{1\le r<R\\2\mid r}}
 \left(1-\frac rR\right)A_r.
\tag{172.S4}
\]

Choose the integer chain

\[
 R_0=\lceil L\rceil,\qquad
 R_{j+1}=\min(2R_j,M),\qquad R_K=M,
\tag{172.S5}
\]

with repetitions removed.  Exact telescoping gives

\[
 T_{26}
 =\frac12\sum_{j<K}
 \bigl(\mathfrak E_{R_{j+1}}^{(2)}-
       \mathfrak E_{R_j}^{(2)}\bigr)-B_{\rm short},
\qquad
 |B_{\rm short}|\ll_\varepsilon L^3X^\varepsilon.
\tag{172.S6}
\]

For an exact doubling \(R\mapsto2R\), the increment has zero diagonal and
the triangular tent

\[
 w_{2R}(r)-w_R(r)=
 \begin{cases}
 r/(2R),&0<r<R,\\
 1-r/(2R),&R\le r<2R,\\
 0,&r\ge2R,
 \end{cases}
\qquad w_R(r)=(1-r/R)_+.
\tag{172.S7}
\]

If \(\mathcal E_R\) is full-line sliding block energy and
\(\mathcal H_R\) the adjacent-block Haar-detail energy, the parallelogram
identity gives

\[
 \mathcal E_{2R}=2\mathcal E_R-\mathcal H_R,
\qquad
 \mathfrak E_{2R}^{(2)}-\mathfrak E_R^{(2)}
 =\mathfrak E_R^{(2)}-\mathfrak H_R^{(2)}.
\tag{172.S8}
\]

The last non-doubling link must use the exact difference of (172.S4), not a
rounded Haar formula.

The frozen sufficient dyadic gate is

\[
 \boxed{
 \mathfrak E_{R_{j+1}}^{(2)}-
 \mathfrak E_{R_j}^{(2)}
 \ll_\varepsilon L^3X^\varepsilon
 \quad(0\le j<K).}
\tag{172.S9}
\]

The \(O(\log L)\) sum is absorbed into \(X^\varepsilon\).  The core
analytic test is whether opening the literal divisor incidences in the
common \(\theta\)-family and applying finite one-sided \(\chi_4\)-Poisson
before forming the bandpass norm yields the missing factor \(L\), or instead
returns to a known collar or a positive \(L^4\) ledger.

## Mandatory proof gates

1. **Parity and endpoint identity.**  Prove (172.S3)--(172.S8) for every
   integer \(M,R_j\), both absolute site parities, the exact terminal weight,
   all zero-extension starts, and the final non-doubling link.
2. **Literal transform.**  Open \(c_N^{\rm rem}\) with multiplicity one and
   derive the finite one-sided character-Poisson formula uniformly in
   \(\theta\), including all zero, boundary, and original modes.
3. **Bandpass before positivity.**  Form the adjacent-scale difference and
   integrate the common \(\theta\) before any modulus over shifts, divisor
   rows, Mobius parameters, Poisson modes, or product cells.
4. **Restored power.**  Price the transformed diagonal, zero modes, endpoints,
   transition ranges, and signed off-diagonal at
   \(L^3X^\varepsilon\), or identify the first exact term that restores
   \(L^4X^\varepsilon\).
5. **Owner-complete complement.**  A strict sector is promotable only with an
   exact complement whose total contribution is target-safe and which still
   implies (172.S2) through (172.S6).

## False controls and parked placements

- A coherent dechirped array \(c_N=e(-J\sqrt N)\) on one full parity class
  has maximal Fejer capacity \(L^4\).  Therefore no coefficient-uniform,
  phase-only, Parseval-only, or generic Haar inequality can prove the target.
- The no-pair branch with all odd primes \(1\pmod4\) prevents assumed
  per-product character balance.
- A one-site sequence has zero dyadic increments; the formal identities must
  introduce no artificial diagonal or endpoint term.
- Global Parseval and \(\|K_R^{(2)}\|_\infty\) give only
  \(RD_L\), which is \(L^4X^\varepsilon\) at the top scale.
- Positive summation of transformed modes must reproduce the accepted
  Round-162/169 product-collar loss and is a failed gate unless the common
  frequency integral first proves a factor-\(L\) saving.

The following remain parked: fixed-shift triangle, fixed-polylogarithmic
shift sectors as a substitute for the full range, positive second-derivative
row estimates, completion followed by absolute dual modes, coefficient-
uniform transport or BV, positive rank-one collars, the audited direct-2024
and Part-I placements, bare joint functional equations, and the Round-171
BAL commutator mechanism.

## Task decomposition

1. **Literal dyadic-frequency attack.**  Derive the complete parity bandpass,
   open the actual residual coefficient, and test the finite character-Poisson
   transform on the common frequency.  Prove (172.S9), an owner-complete
   strict sector, or the first exact transformed no-go.
2. **Statement-only rederivation.**  Independently derive the parity Fejer,
   telescoping, tent, Haar, endpoint, false-control, and factor-\(L\) ledgers
   from the frozen statement alone.
3. **Hostile transform audit.**  Audit multiplicity, selectors, parity,
   endpoints, common-frequency coupling, transformed diagonal and zero modes,
   dual-mode restoration, collar self-return, and downstream owner scope.

## Exit and stop rule

Round 172 closes under exactly one label:

- `hard_top_t1_residual_maximal_fejer_target`;
- `strict_residual_maximal_fejer_spectral_sector`; or
- `maximal_fejer_dyadic_character_poisson_no_go`.

Stop at the first exact failure of literal transform, parity/endpoint
identity, bandpass coupling, restored \(L^3\) power, complete complement, or
owner scope.  In particular, stop if the argument reaches only \(RD_L\),
takes a positive sum over dual modes, or returns to K17a or the Round-169
collar without a new signed connector.  The next mandatory full-proof and
current-literature review is due after Round 173 closes.

Round 172 is 100% analytical/algebraic and 0% numerical experimentation.
