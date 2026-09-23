# Conductor Round 187 report reconciliation

- Campaign: `m9-m1-t1-high-h-inverse-residue-fourier-gate`
- Round: 187
- Role: conductor selection of the smallest common proof kernel
- Starting graph SHA-256:
  `d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a`
- Discovery report SHA-256:
  `4433de37846caa4c9ae0d51ba874221851a331e4a6af13043d4da0f0749ac298`
- Hostile-audit report SHA-256:
  `5a09310baf8574bf1f2c841cd179a66d22aa5834cc50be555a11ad969569db1a`
- Blind report SHA-256:
  `abaf181178b56925bec5fa6b624ddd79be528f4e419e2bff7f22adf9593b9992`

## 1. Common result

The three reports agree that the complete dyadic high-height relation is
not proved.  They independently verify the exact odd-modulus Fourier
normalization

\[
 E_U(a)=(-1)^{[a]_U}
 =\sum_{k\bmod U}c_U(k)e(ka/U),\qquad
 c_U(k)={2\over U\{1+e(-k/U)\}},
\]

with zero coefficient (c_U(0)=1/U), and they retain the separate
(U=1) anchors.  They also agree that the (U=1) contribution, the
zero mode, all fixed-polylogarithmic ordinary edge modes, and all small
moduli are target-safe with the literal coefficient left untouched.

The discovery and hostile reports prove the stronger exact-conductor
packet.  If

\[
 q_U(k)={U\over(k,U)},\qquad Q=H_B,
\]

then every mode with (q_U(k)\le Q), including (k=0), has total
absolute contribution (O_{B,\varepsilon}(L^2X^\varepsilon)).  The
discovery report additionally proves, inside (q_U(k)>Q), the complete
packet (U\le4Q) and the ordinary edge packet
(U>4Q, 0<|k|_U\le Q).  The blind report independently rederives the
latter two payments directly, without access to the graph, strategies,
or sibling reports.

## 2. Exact selected complement

The widest common rigorously justified union leaves exactly

\[
 q_U(k)>Q,\qquad U>4Q,\qquad |k|_U>Q.
\]

All heights, primitive rows, affine sites, modes, orientations,
selectors, endpoint fields, phases, and zero extensions remain under one
outer real part.  Its positive bound is

\[
 O_\varepsilon(YL^2X^\varepsilon),
\]

so the complete factor (Y) is still missing.  The original one-sided
dyadic target is equivalent, up to an absolutely target-safe additive
term, to the corresponding one-sided estimate for this exact
complement.

## 3. Reconciled proof mechanism

The decisive count is made in the exact variables

\[
 u=gU,\qquad n=gh.
\]

On literal support, (u,v\asymp L/\kappa), (n\ll L/\kappa), hence
(h\ll U).  At fixed ((\kappa,u,U)), the two orientations together
have (O(UL)) live ((h,v,t))-atoms.  Exact conductor (q) has total
Fourier mass

\[
 {q\over U}\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}|c_q(a)|
 \ll {q\over U}\log(2q).
\]

Thus its cost at fixed ((\kappa,u,U)) is
(O_\varepsilon(Lq\log(2q)X^\varepsilon)), and summing
(q\mid U\mid u), (q\le Q), proves the full small-conductor packet.
This is a real strict-sector theorem, not a frequencywise physical
incidence claim.

## 4. Hostile controls retained

The centered primitive-conductor kernels satisfy, for a unit (b),

\[
 K_q^\circ(-b)=-K_q^\circ(b),\qquad
 E_U(b)A_+ +E_U(-b)A_-
 =\sum_{\substack{q\mid U\\q>1}}{q\over U}
 K_q^\circ(b)(A_+-A_-).
\]

For prime (U=p), (K_p^\circ(b)=E_p(b)), so the unique high
conductor is literally the original orientation block.  Moreover the
two modes (k=(U\pm1)/2) lie in the retained complement and each has

\[
 |c_U(k)|\ge {2\over\pi}.
\]

Therefore deleting low modes leaves constant Fourier
\(\ell^2\)-mass.  Centering, orientation antisymmetry, positive Fourier
or alias energy, positive Poisson recombination, and bare affine
alternation do not by themselves recover (Y).  These are
mechanism-scoped no-go statements, not lower bounds for the literal
coefficient and not a disproof of the one-sided target.

## 5. Repairs and provenance decision

The discovery report initially contained two embedded carriage returns
inside `\rm odd`; these were mechanically replaced by
`\mathrm{odd}` without changing mathematical content.  The independent
normalization seam then requested three local precision repairs: the
codomain of (2.19) now says (U>1), the centering identity (3.5) now
states its used nonzero-residue hypothesis, and (3.20) now displays the
exact-conductor restriction already imposed in the preceding sentence.
The candidate already contained all three correct restrictions.  The hostile
report contained seven obvious TeX transcription defects
(`ll` for `\ll` and six missing backslashes before `\qquad`); these
were mechanically repaired before hashing above.  No theorem statement,
estimate, or proof step was altered.

The blind report proves the direct small-modulus/edge packet but does not
derive the stronger complete small exact-conductor grouping.  It is
therefore independent support for normalization, carrier, capacity, and
the direct safe sectors, while the exact-conductor strengthening rests on
the mutually consistent discovery and hostile derivations and must
receive an independent seam review before promotion.

## 6. State recommendation

Formalize one subordinate proved-internal reduction node:

`M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction`.

Its positive content is only the exact Fourier decomposition and strict
target-safe transformed packet.  Its negative content records the exact
high-conductor/large-modulus/away-from-edge complement, its
(YL^2X^\varepsilon) positive capacity, and the centered self-return
controls.  Add it as an inconclusive dependency of the still-open
hard-M1 small-(t) owner and narrow that owner's next action to the
literal joint complement.  Change no parent, bridge, theorem, or
exponent status.

The sole recommended Round-187 terminal label is

`strict_high_h_inverse_residue_fourier_sector`.
