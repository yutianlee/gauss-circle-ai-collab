# 1. Result

**Campaign.** `m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate`
**Task.** `literal_cross_gcd_alternating_fibre_attack`
**Role.** discovery
**Starting graph.** `9409651dccbbd1c69547546b245ba04c21d2a280173733ae37b693f9894c8b03`

The cross-gcd coordinates, both opposing orientations, multiplicity one,
the literal amplitude, the half-frequency, and the distinction between the
cross gcd and the original divisor gcd can all be made exact.  On every
nonzero literal atom the latter distinction simplifies more than was
initially apparent: if \(r=2\kappa n\), then

\[
 \boxed{(d,d')=(u,n),}
\tag{176.A1}
\]

in both orientations.  In particular, the original cutoff is constant on
each (t)-fibre; it is not a source of (t)-variation.

There are two positive conclusions.

1. For odd (u), the canonical determinant-anchor sign has an exact finite
   Fourier expansion with normalized Fourier \(\ell^1\)-cost
   \(O(\log(2u))\).  Thus canonical-solution jumps themselves cause no
   power loss: they convert the proposed determinant cancellation into a
   new incomplete inverse-residue mode problem.
2. For each fixed \(\delta>0\), the complete literal sector in which the
   orientation-dependent cross gcd satisfies \(\kappa\geq\delta L\) obeys

   \[
   \boxed{
   \left|\mathfrak C^{\rm rem}_{R_{\log}<r<R_0,2,{\rm opp},
      (d,d')<\gamma L,\ \kappa\geq\delta L}\right|
   \ll_{\delta,\gamma,\varepsilon}L^2X^\varepsilon .}
   \tag{176.A2}
   \]

   This is an owner-complete strict cross-gcd sector, with complement
   \(\kappa<\delta L\).

The full target is **not proved**.  The automatic missing-(L) saving from
the half-frequency is false as a mechanism statement.  There is an exact
base-residue family on which the canonical signs are all (+1) throughout
a positive-proportion determinant interval.  Moreover, on a full
fixed-relative (t)-fibre the square-root phase has

\[
 T\asymp\kappa,\qquad F\asymp {Jh\kappa\over L}
 ={2Jn\kappa\over L},\qquad {F\over T^2}\asymp {Jh\over\kappa L},
\tag{176.A3}
\]

so the half-frequency only translates the stationary lattice.  Absolute
Poisson/B-process restoration has (1+Jh/L) dual modes and gives no
uniform power saving over the trivial \(O(\kappa)\) fibre bound.  These are
route-scoped capacity/self-return obstructions, not a lower bound for the
literal K17a aggregate.  A genuinely joint estimate for the resulting
inverse-residue modes, with the complete selector and endpoint symbol still
inside, remains unexcluded.

# 2. Exact statement and hypotheses

Assume the frozen range

\[
 J=\sqrt X,\qquad 1\ll L\ll H\leq J^{1/2},\qquad
 R_0=\lceil L\rceil,\qquad
 R_{\log}=\min\{R_0-1,\lfloor(\log X)^{100}\rfloor\}.
\tag{176.A4}
\]

For \(N=dm\asymp L^2\), (d) odd, retain exactly

\[
 u_L(d,m)=\chi_4(d)\lambda_N(d)e(J\sqrt N),\qquad
 \lambda_N(d)=\omega_L(N)\rho_N(d)A_N(d),
\tag{176.A5}
\]

where \(\omega_L,\rho_N,A_N\) contain the complete squarefree shell,
normalization, canonical neither/both or no-pair rule, both parity branches,
profiles, floors, stars, point values, endpoints, and full-line zero
extension.  No field is replaced by a majorant in the coordinate identity.

For the orientation (d'=d+p>d), (m=m'+q>m'), write

\[
 p=2s,\qquad q=2w,\qquad
 \kappa=(d,m'),\qquad d=\kappa u,\qquad m'=\kappa v.
\tag{176.A6}
\]

Then \(\kappa,u\) are odd, ((u,v)=1), and for \(r=\kappa h=2\kappa n\),

\[
 sv-wu=n.
\tag{176.A7}
\]

Let \(\bar v\) denote the inverse of \(v\pmod u\), take

\[
 s_0=[\bar v n]_u\in\{0,\ldots,u-1\},\qquad
 w_0={s_0v-n\over u},
\tag{176.A8}
\]

and put (s_t=s_0+ut), (w_t=w_0+vt).  All parity-compatible solutions
are obtained exactly once.  Define

\[
 \begin{aligned}
 N_t^+&=\kappa u(\kappa v+2w_t),\\
 N_t^++r&=\kappa v(\kappa u+2s_t),\\
 \Psi^+_{\kappa,u,v,n}(t)
 &=J\bigl(\sqrt{N_t^++2\kappa n}-\sqrt{N_t^+}\bigr).
 \end{aligned}
\tag{176.A9}
\]

The literal (t)-amplitude is

\[
 \begin{aligned}
 \Lambda^+_{\kappa,u,v,n}(t)={}&
 \left(1-{2\kappa n\over R_0}\right)
 \mathbf1_{R_{\log}<2\kappa n<R_0}
 \mathbf1_{(u,n)<\gamma L}\mathbf1_{s_t>0,w_t>0}\\
 &\times
 \lambda_{N_t^++2\kappa n}(\kappa u+2s_t)
 \overline{\lambda_{N_t^+}(\kappa u)}.
 \end{aligned}
\tag{176.A10}
\]

Because the \(\lambda\)'s are zero-extended, (176.A10) retains all literal
support births and deaths.  The complete contribution of this orientation
is

\[
 \sum_{\kappa,u,v,n}\sum_{t\in\mathbb Z}
 E_u(\bar v n)(-1)^t\Lambda^+_{\kappa,u,v,n}(t)
 e\bigl(\Psi^+_{\kappa,u,v,n}(t)\bigr),
\qquad E_u(a):=(-1)^{[a]_u}.
\tag{176.A11}
\]

For the opposite orientation (d=d'+p>d'), (m'=m+q>m), use

\[
 \kappa=(d',m),\qquad d'=\kappa u,\qquad m=\kappa v,
 \qquad uw-sv=n.
\tag{176.A12}
\]

Now take \(s_0=[-\bar v n]_u\),
(w_0=(n+s_0v)/u), and the same increments
(s_t=s_0+ut,w_t=w_0+vt).  Then

\[
 N_t^-=\kappa v(\kappa u+2s_t),\qquad
 N_t^-+r=\kappa u(\kappa v+2w_t),
\tag{176.A13}
\]

and the analogue of (176.A11) has anchor sign
\(E_u(-\bar v n)\), phase
\(J(\sqrt{N_t^-+2\kappa n}-\sqrt{N_t^-})\), and the exactly mirrored
literal amplitude \(\Lambda^-\).  The frozen aggregate is one real part
outside the sum of (176.A11) and its minus-orientation analogue.  The range
\(R_{\log}<2\kappa n<R_0\) occurs exactly once.

The no-go assertion proved below is deliberately narrow: the identities
((-1)^t), \(E_u(\pm\bar v n)\), odd square-progressions, and classical
fibre completion do not by themselves imply an (L)-saving.  It does not
exclude a theorem that keeps all (u,v,n,t), inverse-residue modes, and
literal coefficients coupled.

# 3. Proof or derivation

## Coordinate algebra, multiplicity, character, and products

In the plus orientation,

\[
 r=d'm'-dm=(d+2s)m'-d(m'+2w)
   =2\kappa(sv-wu)=2\kappa n.
\tag{176.A14}
\]

Since ((u,v)=1), (176.A8) is one solution of (176.A7), and the full
integer solution set is (s=s_0+ut,w=w_0+vt).  Returning to (p,q)
gives exactly (p=p_0+2ut,q=q_0+2vt).  Also

\[
 \chi_4(d')\chi_4(d)=(-1)^s
 =E_u(\bar v n)(-1)^t,
\tag{176.A15}
\]

because (u) is odd.  Both products advance by

\[
 K_\kappa=2\kappa uv={2dm'\over\kappa}.
\tag{176.A16}
\]

Equations (176.A12)--(176.A13) follow identically from
\(r=d'q-pm=2\kappa(uw-sv)\); now the anchor congruence is
\(s\equiv-\bar v n\pmod u\).  An ordered incidence uniquely recovers its
orientation, \(p,q,\kappa,u,v,n\), and then (t), while the displayed data
reconstruct the incidence.  Hence each orientation is multiplicity one,
and the two orientations are disjoint.

## The original divisor gcd is fibre-stable

Consider a nonzero literal plus-orientation atom.  Squarefreeness of
\((N_t^++r)=(\kappa u+2s_t)\kappa v\) forces
\((\kappa u+2s_t,\kappa v)=1\), hence \((s_t,\kappa)=1\).  Since
\(\kappa u\) is odd,

\[
 \begin{aligned}
 (d,d')&=(\kappa u,\kappa u+2s_t)
        =(\kappa u,s_t)=(u,s_t)\\
       &=(u,s_tv-w_tu)=(u,n).
 \end{aligned}
\tag{176.A17}
\]

The same proof in the minus orientation uses squarefreeness of
\((\kappa u+2s_t)\kappa v=N_t^-\).  Since
\(n=uw_t-s_tv\), it again gives (176.A1).  Thus the original cutoff is
constant along (t), while \(\kappa=(d,m')\) or ((d',m)) is a genuinely
different gcd.  Neither can be substituted for the other.

## Parity and squarefree openings

The odd-product branch has (v) odd.  In the even-even squarefree branch,
(v=2v_1) with (v_1) odd, \(4\mid r\), so (n) is even; moreover the
condition that the moving even cofactor have 2-adic valuation exactly one
is constant along (t), because (w_t=w_0+vt) has fixed parity.  In both
branches (s_t=s_0+ut) changes parity at every unit change of (t).

After the 2-adic branch is fixed, every squarefree Möbius opening uses odd
squares.  A condition \(a^2\mid A+Bt\), or an odd coprimality condition
obtained by Möbius inversion, restricts (t), when soluble, to a residue
class modulo an odd integer.  Intersections of the two endpoint openings
still have odd period (M).  Therefore

\[
 (-1)^{t_0+Mj}=(-1)^{t_0}(-1)^j.
\tag{176.A18}
\]

Squarefree and coprimality openings preserve the half-frequency exactly.
They do not, however, bound the oscillatory sum: after restriction to such
a progression the rescaled second derivative is multiplied by \(M^2\),
while the length is divided by \(M\), so the phase parameter
\(F=T^2|\Phi''|\) is unchanged.  Taking all opened terms absolutely returns at
most the usual \(X^\varepsilon\) divisor multiplicity and the same positive
incidence capacity.

## Exact transform of the canonical sawtooth

For odd (u), define the discrete Fourier transform by

\[
 \widehat E_u(k)=\sum_{a=0}^{u-1}E_u(a)e(-ka/u).
\tag{176.A19}
\]

A geometric sum gives, for every \(k\pmod u\),

\[
 \boxed{
 \widehat E_u(k)={2\over1+e(-k/u)}
 ={e(k/(2u))\over\cos(\pi k/u)},\qquad
 E_u(a)={1\over u}\sum_{k\bmod u}\widehat E_u(k)e(ka/u).}
\tag{176.A20}
\]

Because (u) is odd, no denominator vanishes, and comparison with the
harmonic series around (k=u/2) yields

\[
 {1\over u}\sum_{k\bmod u}|\widehat E_u(k)|
 \ll \log(2u).
\tag{176.A21}
\]

This formula is pointwise, so incomplete (n)-ranges, endpoints, and zero
extension stay inside \(\Lambda^\pm\); there is no completion error merely
from (176.A20).  On the other hand, if
(k=(u-1)/2), then

\[
 |\widehat E_u(k)|={1\over\sin(\pi/(2u))}\asymp u.
\tag{176.A22}
\]

Thus the normalized transform has a mode of constant size.  The
half-frequency has become the incomplete inverse-residue twist
\(e(\pm k\bar v n/u)\), not a small coefficient.

There is also a direct base-residue control.  In the plus orientation set

\[
 \kappa=1,\qquad v={u+1\over2},\qquad s=2n,\qquad w=n,
 \qquad 0<n<{u\over4}.
\tag{176.A23}
\]

Then (2v-u=1), (sv-wu=n), \(\bar v=2\pmod u\), and

\[
 E_u(\bar v n)=E_u(2n)=+1
\tag{176.A24}
\]

throughout the displayed determinant interval.  Moreover

\[
 (d,m)=(u,(u+1)/2+2n),\qquad
 (d',m')=(u+4n,(u+1)/2),
\tag{176.A25}
\]

have opposing displacement, determinant (r=2n), and ratios in the
literal hard cone for a fixed positive-proportion subinterval.  The
original gcd is ((u,n)), so it is one when (u) is prime and (n<u).
The mirrored control uses (v=(u-1)/2) in the minus orientation and has
the same constant sign.  Squarefree restriction only deletes members and
cannot change their (+1) character.  No density of fully literal
squarefree, selected/no-pair, profiled, non-polylogarithmic members, and no
lower bound after the square-root phase, is asserted.  Consequently
(176.A23) is a geometric-character control, not literal K17a lower mass.
It nevertheless disproves an automatic joint-(n) cancellation lemma
based only on the canonical character law.

## Phase and restored capacity

Let \(x=N_0+K_\kappa t\), \(r=\kappa h=2\kappa n\), and absorb the
character into

\[
 \Phi(t)=J(\sqrt{x+r}-\sqrt x)+{t\over2}.
\tag{176.A26}
\]

Direct differentiation gives the derivatives in the frozen strategy; on
a fixed-relative interior fibre,

\[
 \Phi''(t)\asymp {Jh\over\kappa L},\qquad
 |\Phi'''(t)|\asymp {Jh\over\kappa^2L}.
\tag{176.A27}
\]

The (t/2) term changes neither derivative.  With \(T\asymp\kappa\), the
classical exponent-pair parameter is (176.A3).  Since
\(J\geq L^2\), \(h\geq2\), and \(\kappa\ll L\), one has
\(F/T^2\gg1\) up to fixed support constants.  The B-process dual interval
has

\[
 \#\{\text{stationary lattice modes}\}
 \asymp 1+T|\Phi''|\asymp1+{Jh\over L},
\tag{176.A28}
\]

and one stationary integral has scale

\[
 |\Phi''|^{-1/2}\asymp
 \left({\kappa L\over Jh}\right)^{1/2}.
\tag{176.A29}
\]

Taking those modes absolutely gives

\[
 \left(1+{Jh\over L}\right)
 \left({\kappa L\over Jh}\right)^{1/2}
 \gg \min\{\kappa,\sqrt F\},
\tag{176.A30}
\]

and \(\sqrt F\gg\kappa\) in this range.  After taking the minimum with the
trivial estimate, the result is \(O(\kappa)\), not (O(1)).  Equivalently,
the standard second-derivative expression
\(\sqrt F+T/\sqrt F\) is no better than (T).  The translated half-lattice
has many admissible modes and no proved modulo-one separation.  General
exponent-pair notation gives (F^aT^{b-a}); no estimate supplied by the
accepted context turns this uniformly into the \(O(X^\varepsilon)\) fibre
bound needed below, especially because (J/L^2) is not bounded above.

For the power ledger put \(U=L/\kappa\).  Up to fixed support constants,
there are (O(U^2)) anchors ((u,v)), (O(U)) determinants (h), and
\(O(1+\kappa)\) sites on each fibre.  Hence

\[
 \begin{array}{c|c|c}
 \text{input at fixed }\kappa&\text{capacity at fixed }\kappa
     &\text{sum over }\kappa\geq K\\ \hline
 \text{trivial }O(\kappa)\text{ fibre}&O(L^3/\kappa^2)
     &O(L^3/K)\\
 \text{hypothetical }O(X^\varepsilon)\text{ fibre}&O(L^3/\kappa^3)X^\varepsilon
     &O(L^3/K^2)X^\varepsilon.
 \end{array}
\tag{176.A31}
\]

Thus the hypothetical bound would make \(\kappa\geq L^{1/2}\) safe, but
(176.A27)--(176.A30), selector variation, and (176.A23) do not justify it.
The actual positive capacity in that range is \(L^{5/2}X^\varepsilon\).
For \(K=\delta L\), however, the first line of (176.A31) is already
target-sized.  Summing the exact multiplicity-one incidences in both
orientations proves (176.A2); every squarefree, selector, profile, endpoint,
non-polylogarithmic, and original-gcd restriction only deletes atoms, and
the literal coefficients are bounded.

# 4. First doubtful or unproved step

The first unproved step is not the coordinate map, parity, squarefree
progression law, original gcd, or canonical-sawtooth transform.  It is a
new **literal joint inverse-residue estimate** after (176.A20).

A sufficient local form, with \(U=L/\kappa\), would be uniform control for
both orientations and every \(k\pmod u\) of the shape

\[
 \boxed{
 \sum_{n\ll U}\ \sum_{t\in I^\pm_{\kappa,u,v,n}}
 \Lambda^\pm_{\kappa,u,v,n}(t)
 e\!\left(
   \Psi^\pm_{\kappa,u,v,n}(t)+{t\over2}
   \pm {k\bar v n\over u}
 \right)
 \ll_\varepsilon \kappa X^\varepsilon .}
\tag{176.A32}
\]

The interval and all deletions in (176.A32) must be literal.  If (176.A32)
held, (176.A21) and

\[
 \sum_{\kappa\ll L}(L/\kappa)^2\kappa
 \ll L^2\log L
\tag{176.A33}
\]

would restore the full \(L^2X^\varepsilon\) ledger.  No such estimate is
proved here or in an allowed dependency.  In particular, the large alias
(176.A22) must be estimated rather than discarded.

The canonical residual selector is the first literal amplitude field for
which even bounded variation is unavailable.  As (t) or (n) changes,
the product changes, the canonically selected prime pair can change, and
\(\rho_N(d)\) can switch between zero and one.  The no-pair condition is
itself product-dependent.  The accepted hypotheses give no bound for the
number of switches and no Fourier norm in (n), (t), or \(\bar v\).
Consequently neither Abel summation nor a standard incomplete Kloosterman
estimate applies to (176.A32) after replacing the literal symbol by a
smooth weight.  Proving (176.A32), or a genuinely more global substitute,
is the exact next mathematical obligation for this route.

# 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| Literal residual coefficient | **Pass for identity.** Equations (176.A10)--(176.A13) retain \(\omega,\rho,A\), both endpoint coefficients, and the phase; no coefficient is erased. |
| Non-polylogarithmic complement | **Pass.** The sole determinant range is \(R_{\log}<2\kappa n<R_0\); the accepted polylogarithmic sector is not reintroduced. |
| Both opposing orientations | **Pass.** They are derived separately in (176.A6)--(176.A13), not by conjugating or deleting a sector. |
| Cross-gcd multiplicity | **Pass.** The orientation, unique cross gcd, primitive anchors, determinant, and solution parameter reconstruct the ordered incidence once. |
| Cross gcd versus original gcd | **Pass, with exact simplification.** On literal squarefree support, (g=(d,d')=(u,n)) in both orientations; (g) is fibre-stable and remains distinct from \(\kappa\). |
| Parity and two-adic branches | **Pass.** \(u,\kappa\) are odd; \(s\mapsto s+u\) flips character.  In the even-even branch (v) is twice odd, (n) and (w) have the required fixed parity, and \(4\mid r\). |
| Half-frequency character law | **Pass.** It is exactly \(E_u(\pm\bar v n)(-1)^t\). |
| Odd-square Möbius progressions | **Pass algebraically; no analytic saving.** Every soluble opened progression has odd period and preserves alternation, but its phase parameter (F) is unchanged and absolute recombination restores positive capacity. |
| Selected and no-pair rows | **Open obstruction.** The literal selector has no proved fibre or determinant BV/Fourier control.  No selected-pair density and no no-pair cancellation is assumed. |
| Constant-amplitude full fibres | **Fails as an automatic cancellation lemma once the square-root phase is retained.** The B-process restores \(O(\kappa)\); after suppressing the phase, the determinant anchor still has the constant-sign family (176.A23). |
| Short cross-gcd fibres | **Fails fibrewise.** Fixed \(\kappa=O(1)\) gives only (O(1)) sites but (O(L^3)) anchor-determinant capacity.  Cancellation must be joint in (v,n) and the phase. |
| Canonical-solution sawtooth | **Pass as an exact transform, but not as a bound.** Its normalized Fourier \(\ell^1\)-cost is \(O(\log u)\), while a near-half mode has constant normalized size and leads to (176.A32). |
| Phase alias and dual-mode capacity | **Route no-go.** The shifted stationary lattice has (1+Jh/L) modes; absolute saddle restoration is no better than the trivial fibre length. |
| Endpoints and zero extension | **Pass for identity and strict-sector count.** They remain inside \(\Lambda^\pm\).  For cancellation they create incomplete mode sums, which (176.A32) must own. |
| \(L^3\)-to-\(L^2\) ledger | **Complete.** It is (176.A31)--(176.A33).  Only fixed-proportion \(\kappa\) is presently target-safe; the proposed \(\kappa\geq L^{1/2}\) extension needs the unproved signed estimate. |
| False coefficient controls | **Quarantined.** A mask retaining only one parity, an erased selector, or a complex dechirping weight can restore full positive mass, but none is claimed to equal the literal coefficient.  The base-residue control is also not claimed as literal lower mass. |
| Residual-only owner scope | **Pass.** No conclusion is drawn for the full (t=1) face or any parent obligation. |
| No in-round pivot | **Pass.** Only the frozen cross-gcd alternating-fibre mechanism and its exact Fourier form were tested. |

No numerical experiment or external theorem was used.  The allocation was
100 percent analytical/algebraic.

# 6. Dependencies and exact artifacts used

The derivation used exactly the selected context:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/round176_m2_hard_top_t1_residual_k17a_cross_gcd_alternating_fibre_strategy.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_fejer_parity_gcd_scale_reduction.md`;
- `proofs/kernels/m9_m2_hard_top_t1_residual_determinant_endpoint_polylog_shift_reduction.md`; and
- `proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md`.

No sibling Round-176 report, candidate, review, control, synthesis, web
source, or unlisted historical artifact was used.

# 7. Recommended state effect

**Recommended effect: promote only the exact subordinate identities and the
fixed-proportion strict sector (176.A2); retain K17a and every parent open.**

More precisely:

- promote the multiplicity-one two-orientation formulas, the fibre-stable
  identity \((d,d')=(u,r/(2\kappa))\), the odd-progression parity law, and
  the exact Fourier formulas (176.A20)--(176.A21) as internal algebraic
  infrastructure;
- promote (176.A2) as an owner-complete strict sector with explicitly named
  complement \(\kappa<\delta L\), if the conductor judges that this
  fixed-proportion sector merits a graph node;
- record as rejected only the route claim that the half-frequency, by
  fibrewise alternation, canonical determinant alternation, Abel/BV, or
  absolute B-process completion, automatically saves the missing factor
  (L); and
- retain the full non-polylogarithmic K17a target, the complete residual
  scalar, hard TOP, BAL, UNBAL, M9--M2, M9--M1/GAR, endpoint uniformity,
  M9, both bridges, the quarter theorem, and all exponents as open.

The appropriately scoped terminal label is
`k17a_cross_gcd_alternating_fibre_capacity_or_self_return_no_go`.  The
first live step beyond that label is the literal joint inverse-residue
estimate (176.A32), not another fibrewise or shiftwise triangle.
