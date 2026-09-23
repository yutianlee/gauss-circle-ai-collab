# Final literal mathematical review of the Round-183 kernel

- Campaign: `m9-m1-hard-top-high-radical-small-t-signed-contraction-gate`
- Round: `183`
- Role: independent final mathematical reviewer
- Starting graph SHA-256:
  `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`
- Candidate reviewed:
  `candidates/formalized_hard_m1_small_t_primitive_ray_sector_and_self_return.md`
- Durable kernel reviewed:
  `proofs/kernels/m9_m1_hard_top_small_t_primitive_ray_sector_and_truncated_mobius_self_return.md`
- Verdict: **REPAIR** — bounded, theorem-preserving repair required in the
  displayed BV argument before either artifact is promotion-ready

## 1. Result

The primitive-ray incidence theorem is mathematically correct after one
precise endpoint repair.  The coefficient expansion, incidence bijection,
squarefree coordinates, character factorization, geometric denominator,
ray count, exact incidence complement, both-sign uniformity, and graph
scope all pass independent reconstruction.

The first formal defect occurs at candidate equation (183.C11), repeated
in durable-kernel proof lines 101--105.  The displayed sum runs over all
odd (G) but applies (Phi(Gu/(H+1))) without either restricting to
(1leq Guleq H) or defining a zero-extended Vaaler factor.  The accepted
dependency defines (Phi) only on ([0,1]), and neither artifact defines
(H) before using it.  Thus the displayed expression is literally
undefined for large (G).  The surrounding prose does not make that
formula exact, even though it makes the intended repair clear.

The repair is local: define the hard-profile parameters and replace
(183.C11) by a variation statement for the zero-extended, shell-truncated
factor.  With that change, the proof gives the claimed
\(O_\varepsilon(L^{3/2}X^\varepsilon)\) strict incidence sector.  No change
to the theorem, resonance cutoff, complement, or power is needed.

## 2. Exact statement and hypotheses reviewed

Let

\[
 y=\lfloor\sqrt X\rfloor,\qquad q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor,
\]

and fix a literal middle or lower residual hard-M1 shell (L), real
(Xgeq2), and (sigmain{+1,-1}).  The exact accepted stationary
formula shows that, up to a shell normalizer and a fixed sign constant,
the literal incidence coefficient is

\[
 \eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 W\!\left(\sqrt{\frac{4q_Xh}{n}}\right)(hn)^{-3/4}
\]

on (1leq hleq H), (n) odd, and (4h<n<16h), with all literal
residual labels and endpoint conventions imposed by zero extension.  The
negative-frequency symbol is handled separately or as the conjugate
partner; its variation is identical.

Expand this exact coefficient inside the high-radical small-(t) owner.
For each incidence set

\[
 G=(h,n),\quad h=Gu,\quad n=Gv,\quad (u,v)=1,
\]

\[
 s(u,v)=\operatorname{sf}(uv),\qquad
 \rho(u,v)=\sqrt{uv/s(u,v)},\qquad t=G\rho(u,v).
\]

With

\[
 T_L=\lceil\sqrt L\rceil,\quad
 G_0=\lceil L^{1/4}\rceil,\quad
 \delta_X=(10\log(2X))^{-1},
\]

and

\[
 \Delta_X(u,v)=\operatorname{dist}
 \left(2\sqrt{Xuv},\mathbb Z+\tfrac12\right),
\]

the reviewed positive theorem is exactly the candidate's incidence sum
(183.C8), restricted by (Ggeq G_0) and
(Delta_X(u,v)geqdelta_X), bounded by
\(O_\varepsilon(L^{3/2}X^\varepsilon)\).  Its complement is asserted only
after literal divisor expansion, not as a subset of product indices.

## 3. Independent proof and line audit

### Exact coefficient and incidence map

The accepted exact-formula evidence gives

\[
 \sum_{h\asymp L}
 {\eta_L(h)\Phi(h/(H+1))\over h^{3/4}}
 \sum_{\substack{4h<n<16h\\n\ \mathrm{odd}}}
 {\chi_4(n)W(\sqrt{4q_Xh/n})\over n^{3/4}}
 e(\sqrt{Xhn}),
\]

with a fixed normalized-BV (eta_L), truncation at (h=H), and the
literal one-sided-transform conventions.  Therefore expanding
(C_{L,X}^sigma(st^2)) introduces neither a divisor envelope nor an
arbitrary coefficient.

Candidate lines 45--77 are exact.  Each incidence has the unique triple
((G,u,v)), and conversely (h=Gu,n=Gv) reconstructs it.  Since (G^2)
is a square,

\[
 hn=G^2uv=\operatorname{sf}(uv)
 \left(G\sqrt{uv/\operatorname{sf}(uv)}\right)^2.
\]

Thus \(s=\operatorname{sf}(uv)\) and \(t=G\rho(u,v)\) are exactly the
unique squarefree-kernel coordinates.  Because (n) is odd, (G,v) are
odd, and complete multiplicativity gives
(chi_4(Gv)=chi_4(G)chi_4(v)), even if (G) and (v) are not coprime.
The phase identity is exact for both signs.  Multiplicity is preserved
incidence by incidence.

### Corrected step-two BV

The exact repair should define, for integers (m),

\[
 \Psi_{H,L}(m)=
 \mathbf1_{1\leq m\leq H}\eta_L(m)
 \Phi\!\left(\frac m{H+1}\right),
\]

with the literal shell endpoint weights included in (eta_L), and then
state

\[
 \sum_{G\ \mathrm{odd}}
 |\Psi_{H,L}((G+2)u)-\Psi_{H,L}(Gu)|\ll1.       \tag{FR.1}
\]

Indeed, sampling the normalized-BV dyadic profile cannot increase its
integer variation.  On the active interval, (Gu\asymp L), (Lleq H),
and bounded (\Phi') give

\[
 \sum_{\substack{G\ \mathrm{odd}\\Gu,(G+2)u\in[1,H]}}
 \left|\Phi\!\left(\frac{(G+2)u}{H+1}\right)
 -\Phi\!\left(\frac{Gu}{H+1}\right)\right|
 \ll {u\over H+1}\left(1+{L\over u}\right)\ll1.
\]

The zero extension adds at most two boundary jumps.  This is the exact
argument that candidate (183.C11) intended but did not state.

On a ray, the (W)-argument is
(sqrt{4q_Xu/v}), so it is constant in (G), including at real-(X)
support crossings.  The strict cone tests and ratio-dependent endpoint
fields are likewise constant.  The normalized power is a fixed
ray-factor times (G^{-3/2}) and has monotone total variation controlled
by its supremum.  The shell, (hleq H), (Ggeq G_0), and
\(G\rho<T_L\) tests are interval masks on the odd lattice.  Floors are
fixed for fixed (X); star and half weights are bounded endpoint traces;
the finite residual exclusions create only a uniformly bounded number of
entries, exits, or isolated traces.  The discrete product rule and (FR.1)
therefore prove the claimed zero-extended (BV_2) bound uniformly through
all literal crossings and for both signs.

### Geometric denominator and ray count

For (G=2k+1) and (alpha=sqrt{Xuv}), consecutive terms of the
unweighted character-phase progression have ratio

\[
 -e(2\sigma\alpha)=e(2\sigma\alpha+\tfrac12).
\]

Its geometric denominator is therefore exactly

\[
 \left\|2\sigma\alpha+\tfrac12\right\|
 =\operatorname{dist}(2\sqrt{Xuv},\mathbb Z+\tfrac12)
 =\Delta_X(u,v),
\]

the same for both signs.  Abel summation with corrected (BV_2) gives
\(O_\varepsilon(\delta_X^{-1}X^\varepsilon)\) per retained ray.

A nonempty ray has (Gu\asymp L); (Ggeq G_0) implies
(u\ll L/G_0), and (4u<v<16u) gives (O(u)) choices for (v).
Hence the ray count is

\[
 O\!\left(\sum_{u\ll L/G_0}u\right)
 =O\!\left((1+L/G_0)^2\right).
\]

After the per-ray signed saving, summing positively over rays and
absorbing (log(2X)) by an epsilon relabelling yields the target
\(L^{3/2}X^\varepsilon\).

### Complement and scope

Within all inherited literal predicates, splitting first at (G_0) and
then at the strict resonance inequality is disjoint and exhaustive:

\[
 \{G<G_0\}\ \dot\cup\
 \{G\geq G_0:\Delta_X(u,v)<\delta_X\}.
\]

Equality belongs to the proved sector.  When the small-(t) range is
nonempty, \(t=1\) forces \(G=\rho=1\); then \(L>1\), so \(G_0\geq2\), and
the complete (t=1) face lies in the first open piece.  The candidate and
kernel correctly state that the theorem is incidence-level only and does
not prove the full owner.

The truncated-Mobius identities in the candidate and durable kernel are
also algebraically consistent with the accepted obstruction: both strict
cutoffs remain in the kernel, the (u=1) term returns the full product
wave, and the complementary regions have target-safe incidence counts.
They do not enlarge the positive theorem's scope.

## 4. First defective and first unproved steps

**First defective step in the written kernel:** candidate (183.C11) and
durable-kernel lines 101--105.  As written, (H) is undefined and the raw
(Phi)-difference is summed over all odd (G), outside the accepted
domain of (Phi).  Replace it by (FR.1), or restrict the sum explicitly
to the active (Gu\in[1,H]) interval and add the two zero-extension
jumps.  Define (y,q_X,H) in both artifacts.  This is a mandatory exactness
repair, not a failure of the theorem.

**First unproved step toward the frozen owner after that repair:** the
exact incidence complement above.  Its small-gcd piece contains all
(t=1), and no target estimate is supplied for either it or the
large-gcd near-resonant piece.  The full small-(t) owner therefore remains
open.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact literal coefficient expansion | **GREEN.** The accepted (eta_L\Phi W(hn)^{-3/4}) symbol, parity, and zero extension are retained. |
| Incidence bijection and multiplicity | **GREEN.** Unique gcd rays in both directions. |
| Squarefree and small-\(t\) coordinates | **GREEN.** \(s=\operatorname{sf}(uv)\), \(t=G\rho\), with the literal ceiling and strict inequality. |
| Character factorization | **GREEN.** Complete multiplicativity on odd (G,v). |
| Raw displayed (Phi)-variation | **REPAIR.** Undefined outside (Guleq H); use the zero-extended factor (FR.1). |
| Corrected full literal (BV_2) | **GREEN after repair.** Profile, power, masks, crossings, stars, half weights, and zero-extension jumps are uniformly controlled. |
| Geometric denominator | **GREEN.** Exactly the stated half-integer distance, sign-independent. |
| Ray count and restored power | **GREEN.** (O((1+L/G_0)^2)) rays and (G_0=L^{1/4+o(1)}). |
| Exact complement | **GREEN at incidence level.** Disjoint and exhaustive with equality assigned correctly. |
| Mandatory (t=1) | **GREEN/open.** Entirely retained in the small-gcd complement. |
| Arbitrary/character-erased controls | **GREEN.** The proof spends actual (chi_4(G))-phase cancellation before positivity. |
| Parent and exponent quarantine | **GREEN.** No complete owner, parent, bridge, theorem, or exponent follows. |

No numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

Only the authorized packet was read:

1. `protocol.md`;
2. `state/proof_obligations.yml` at SHA-256
   `5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`;
3. the conductor candidate at SHA-256
   `69662a1b8489d6a4daf326e39de88bb9c36e693cadc94fcb20020644adaeec59`;
4. the durable kernel at SHA-256
   `214078f6c412f9ba3591da00d6920933be6e3c794d9a734be5b0f2b6b12d5c84`;
5. the prior coefficient/product/endpoint review;
6. `rounds/codex-managed/m9-combined-top-cones/reports/combined_cone_algebra.md`;
7. `rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/m1_terminal_arithmetic_attack.md`.

The direct accepted graph dependencies are
`M9-M1-hard-top-squarefree-radical-sector-reduction`,
`M9-M1-top-endpoint-transform`,
`M9-M1-frequency-phase-diagram-R10`, `H4-Phi-regularity`, and
`Divisor-bound-elementary`.

## 7. Narrowest allowed graph effect

Do not apply a promotion from the present candidate or durable-kernel text
until the displayed BV repair is made in both artifacts and rechecked.

After that bounded repair, and subject to the other required Round-183
seams, the narrowest positive graph effect is one subordinate
`proved_internal` node for the exact **literal-incidence large-gcd
nonresonant sector**, with the small-gcd/near-resonant complement stated
verbatim.  The small-(t) refinement may also update only the existing
Mobius/Mellin/joint-(t) self-return obstruction at its exact mechanism
scope.

Keep `M9-M1-hard-top-high-radical-small-t-residual-estimate`,
`M9-M1-top-endpoint-signed-cone`, the independent smooth M1 parent, GAR,
M9--M1, every M2 obligation, endpoint uniformity, M9, both bridges, the
Gauss-circle target, and every exponent unchanged.
