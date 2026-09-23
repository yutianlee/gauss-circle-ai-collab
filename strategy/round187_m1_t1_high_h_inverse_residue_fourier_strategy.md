# Round 187 conductor strategy: hard-M1 t=1 high-height inverse-residue Fourier gate

- Round: 187
- Starting graph:
  d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a
- Selected owner:
  M9-M1-hard-top-high-radical-small-t-residual-estimate
- Frozen component: the exact dyadic high-height complement (K185.37)
- Planned allocation: at least 90% analytical/algebraic and at most 10%
  bounded diagnostic computation
- Scheduled strategy checkpoint: Round 190, after analytic Rounds 187--189

## 1. Exact inherited frontier

Round 185 reduced the original hard-M1 \(t=1\) no-pair plus selected
neither/both residual to an endpoint-exact Fejer correlation. Its
monotone and \(h\le H_B\) sectors are target-safe. Round 186 selected
the exact remaining dyadic block as the sole Round-187 objective.

For fixed \(B>0\), real \(X\ge2\), a literal middle or lower residual
shell \(L\ge2\), \(\sigma\in\{+1,-1\}\), and a nonempty block
\(Y<h\le2Y\) with

\[
 H_B=\lfloor(\log(2X))^B\rfloor<Y,
 \qquad R_0=\lceil L\rceil,
\]

write \(\mathfrak f=(\kappa,g,h,U,v)\) in the exact domain

\[
 \kappa,g,h,U,v>0,\quad \kappa,g,U\text{ odd},\quad
 (gU,v)=1,\quad(U,h)=1,\quad0<2\kappa gh<R_0.
\tag{187.1}
\]

All anchors, affine index sets, endpoint products, residual masks,
literal coefficients, phases, and zero extensions are exactly
(K185.30)--(K185.35). The target is the one-sided estimate

\[
 \boxed{
 \Re\!\sum_{\omega\in\{+,-\}}
 \sum_{\substack{\mathfrak f\text{ satisfying }(187.1)\\Y<h\le2Y}}
 (-1)^{S_{0,\omega}}
 \sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t)
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{187.2}
\]

There is one real part outside both orientations, every primitive row,
and every affine index. A negative block helps; Round 187 does not seek
a dyadic lower bound. Positive capacity is
\(O(YL^2X^\varepsilon)\), so the missing gain is the complete factor
\(Y\).

## 2. Fresh mechanism

For odd \(U>1\), put

\[
 E_U(a)=(-1)^{[a]_U},\qquad
 \widehat E_U(k)=\sum_{a\bmod U}E_U(a)e(-ka/U)
 ={2\over1+e(-k/U)}.
\tag{187.3}
\]

Then

\[
 E_U(a)={1\over U}
 +\sum_{\substack{k\bmod U\\k\ne0}}
 {\widehat E_U(k)\over U}e(ka/U).
\tag{187.4}
\]

The canonical anchor is

\[
 (-1)^{S_{0,+}}=E_U(\bar vh),\qquad
 (-1)^{S_{0,-}}=E_U(-\bar vh),
\tag{187.5}
\]

with the separate \(U=1\) convention retained. Since
\((U,hv)=1\), (187.5) also exposes exact opposite-orientation
antisymmetry for the raw anchors when \(U>1\). No equality of the two
literal orientation amplitudes is assumed.

The new test is not conductor centering by itself. It asks whether the
nonzero inverse-residue Fourier modes can remain signed and joint over
\(h,v,t\), both orientations, and every literal field until an actual
orthogonality, reciprocity, or oscillatory estimate recovers the full
factor \(Y\). The zero mode, \(U=1\) contribution, and any genuinely
low-frequency packet must first be priced exactly and split with an
exact complementary aggregate.

This differs from the parked Round-185 routes: it forbids taking moduli
mode by mode, forbids a positive alias \(TT^*\), and forbids declaring
the centered high-conductor defect small merely because low conductors
are safe. A proof must estimate the actual signed centered aggregate,
not reconstruct the original block minus a safe packet.

## 3. Literal restrictions

Every term retains both endpoint factors
\(\lambda_{N+r,\sigma}\overline{\lambda_{N,\sigma}}\), including the
Round-184 residual selector, squarefree and allocation-coprimality
deletions, the strict hard cone, shells, heights, profiles, floors,
stars, half-weights, hard samples, real-\(X\) crossings, endpoints,
sign, phase, and zero extension. Positivity in
\(I_{\mathfrak f,\omega}\) is imposed before square-root evaluation.
The final dyadic block may be truncated by \(2\kappa gh<R_0\).

No regularity, density, independence, or translation invariance of the
literal deletion pattern may be assumed. An artificial bounded array
may refute a coefficient-uniform Fourier argument, but it is not a lower
bound for the actual M1 coefficient. Conversely, any successful theorem
must identify the actual Vaaler/\(\chi_4\) feature it uses and explain why
the unsigned or adversarial analogue is not proved.

## 4. Required power ledger

The campaign must separately price:

1. \(U=1\), including all admissible \(\kappa,g,h,v,t\);
2. the exact \(k=0\) term \(1/U\) for \(U>1\);
3. each proposed low reduced conductor or nonresonant packet;
4. the centered nonzero-mode complement with all orientations and fields
   still joint; and
5. dyadic recombination, including the first block above \(H_B\) and the
   final truncated block.

Any strict result must be \(O_{B,\varepsilon}(L^2X^\varepsilon)\) and
must name the exact remaining signed complement. A bound containing
\(Y^\eta\) for fixed \(\eta>0\), or one that achieves a gain only after
positive mode, row, orientation, selector, or endpoint recombination,
fails the frozen target.

## 5. Exit gates

Round 187 closes under exactly one label:

1. `hard_m1_t1_high_h_target`: prove (187.2) for every literal field,
   both signs, every fixed \(B\), and every permitted dyadic block;
2. `strict_high_h_inverse_residue_fourier_sector`: prove the widest
   target-safe exact Fourier sector and retain its canonical centered
   complement without claiming the full target; or
3. `high_h_inverse_residue_deletion_capacity_or_self_return_no_go`:
   prove the narrowest exact deletion, resonance, capacity, or
   self-return obstruction for this mechanism while leaving (187.2)
   viable.

At least one important identity or estimate receives statement-only
independent rederivation. Candidate promotion requires separate reviews
of normalization/multiplicity, literal deletion/endpoints, power and
one-sided real-part placement, false controls, blind post-unmask
consistency, and downstream ownership.

## 6. Proof-state boundary

Even a complete proof of (187.2) closes only the exact Round-184 residual
and then the original \(t=1\) face through the accepted Fejer and exchange
connectors. It leaves every original \(t\ge2\) small-\(G\) incidence and
the large-\(G\) near-resonant complement open. The complete small-\(t\)
owner, hard and smooth M1 parents, GAR, M9--M1, every M2 parent, endpoint
uniformity, M9, both bridges, the quarter theorem, and every exponent are
quarantined. Round 188 is designed only after Round 187 closes.
