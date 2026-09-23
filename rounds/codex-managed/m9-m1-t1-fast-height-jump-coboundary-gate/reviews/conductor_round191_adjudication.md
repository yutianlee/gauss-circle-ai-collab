# Conductor Round 191 adjudication

- Campaign: m9-m1-t1-fast-height-jump-coboundary-gate
- Round: 191
- Starting graph SHA-256:
  306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa
- Durable kernel SHA-256:
  7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2
- Closing label: strict_fast_height_jump_sector
- Numerical theorem evidence: none

## 1. Result and conductor decision

Round 191 closes with one proved subordinate reduction and no complete
fast-packet estimate.

On the exact Round-189 fast complement

\[
 U=mq>4Q,\qquad q>Q,\qquad m|a|_q>Q,\qquad
 Qm<Y,\qquad j_q(a,v)>T_Q,
\]

let \(\varrho_U(v)\) be the signed least inverse modulo \(U\) and set

\[
 T_\varrho=
 \min\left\{\frac{U-1}{2},
             \left\lfloor\frac{QmU}{Y}\right\rfloor\right\}.
\]

The complete sector

\[
 0<|\varrho_U(v)|\le T_\varrho
\]

is absolutely target-safe.  On its exact complement, the live-side
outer height/carrier terminals and the isolated Fejer-difference
projection are also target-safe.  After the exact lift and outer
ledger, their full contribution is

\[
 O_{B,\varepsilon}(L^2X^\varepsilon).
\]

The full Round-189 fast aggregate decomposes exactly, before the final
real part, into this safe complex aggregate and one rho-large literal
remainder.  The remainder target is open.

## 2. Exact transport and safe-sector proof

For

\[
 \varrho v-\gamma U=1,
\]

the plus determinant fibre \(Sv-Uw=h\) transports to height \(h-1\)
by subtracting \((\varrho,\gamma)\); the minus fibre \(Uw-vS=h\)
transports by adding it.  Canonical reindexing has carry

\[
 \nu_\omega(h)=
 \frac{S_{0,\omega}(h)-\epsilon_\omega\varrho
       -S_{0,\omega}(h-1)}{U}\in\{-1,0,1\}.
\]

The retained mode-and-affine ratio is

\[
 (-1)^{\nu_\omega(h)}
 e(\epsilon_\omega a\varrho/q).
\]

It is not replaced by the full pre-Fourier parity
\((-1)^\varrho\).  Full reconstruction restores the latter only by
self-returning to the pre-Round-187 packet.

Inversion is a bijection on the unit classes modulo \(U\), so the safe
sector uses at most \(2T_\varrho\) classes.  Since the literal
\(v\)-support has total length \(O(u)\) and \(U\mid u\),

\[
 \#v_{\rm safe}\ll\frac{uT_\varrho}{U}
 \ll\frac{Qmu}{Y}.
\]

There are \(O(Y)\) heights and \(O(\kappa)\) live sites per row.
Endpoint-exact Abel inversion returns the jump packet to the original
row sum before positive counting.  Therefore the fixed packet costs

\[
 O_\varepsilon(Qm\kappa uX^\varepsilon).
\]

The floor-zero and saturated cases are exact.

## 3. Terminal, Fejer, and outer ledger

The outer height/carrier support is one integer interval, so its exact
live-side backward difference has at most two terminal heights.  On a
projective \(J\)-band it costs

\[
 (q/J)(uJ/q)\kappa X^\varepsilon
 \ll\kappa uX^\varepsilon.
\]

On persistent outer masks and transported common sites,

\[
 F(h)-F(h-1)=-\frac{2\kappa g}{\lceil L\rceil},
\qquad
 \frac{2\kappa gY}{\lceil L\rceil}<1.
\]

Its exact complex projection also costs
\(O_\varepsilon(\kappa uX^\varepsilon)\).  Both orientations and all
surviving literal labels are completed before these moduli.

The Round-188 lift and coefficient mass are

\[
 c_{mq}(ma)=m^{-1}c_q(a),\qquad
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q).
\]

The \(m^{-1}\) cancels the fixed-packet \(m\) before positivity.  The
power-of-two projective bands cost a logarithm, and
\(\sum_{mq\mid u}1\le\tau_3(u)\).  With
\(u\asymp L/\kappa\), \(L\ll X^{1/4}\), and a fresh epsilon budget,

\[
 QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u)
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\]

No positive power of \(Y\) is absorbed.

## 4. Exact remainder and first open relation

The repaired formalization gives an exhaustive gated partition of:

- outer height/carrier births and deaths;
- outer coprimality flips;
- affine common sites, births, and deaths;
- canonical carries and the isolated Fejer change;
- both orientation-specific endpoint products and arithmetic masks;
- shell, cone, selector, profile, floor, star, half-weight, hard-sample,
  crossing, trace, and endpoint-zero fields; and
- the actual square-root-phase change.

The safe inverse, terminal, and Fejer pieces are exact joint complex
projections.  Their complement is defined by complex subtraction at
the fixed-packet level and then by the inherited linear outer assembly.

The first open fixed-packet estimate is the same packet with
\(|\varrho_U(v)|>T_\varrho\) after those safe projections are removed:

\[
 |\mathscr R_{\rm fix}|
 \ll_\varepsilon Qm\kappa uX^\varepsilon.
\]

Positive variation supplies only
\(Y\kappa uX^\varepsilon\).  The exact deficit is

\[
 \frac{Y}{Qm}>1.
\]

The normalized Abel operator has full capacity on arbitrary bounded
zero-extended height arrays.  This is a coefficient-class mechanism
control, not a literal lower bound and not a disproof of the open
remainder estimate.

## 5. Independent evidence and controls

The discovery and hostile reports independently prove the inverse
sector and ledger.  The statement-only report independently proves the
Abel sign, endpoint convention, and bounded-height-array capacity.
A second statement-only review independently verifies the signed
transport and local sector; post-unmask review restores and verifies
the global shell/divisor connectors.

The repaired candidate passed three post-repair reviews and the durable
kernel passed three final post-hygiene reviews:

- candidate/kernel consistency, SHA-256
  5ebaa7901d876b2f3872f5a0e34f1660d2add43e2d94457fb4ee0ee2e42ac098;
- power/literal/owner scope, SHA-256
  8193106f54a970fb50713a6e9e5f8e792ac7c261f22afb3ae5086ca9e31aeb5e;
- formalization/provenance/hygiene, SHA-256
  563ec0c5da8433af4d20034346083eadb328c3400ed7820ec156c0dc8dc2604b.

The candidate and kernel mathematical bodies are byte-identical, with
body SHA-256
f29eb55c0620bfdfbafb3974fa23bc6cd01594de04668b857d96f2c61d9834d4.

The two Wolfram controls record 470,029 ordinary-anchor/Abel checks,
2,720 capacity cases, 420,672 signed-inverse transport/parity checks,
and 1,325 inverse-class counts, with zero failures.  They are diagnostic
only and supply no asymptotic theorem evidence.

## 6. Dependencies and downstream scope

The new subordinate node depends directly only on:

- M9-M1-hard-top-t1-high-h-dual-frequency-projective-reduction;
- Divisor-bound-elementary.

The complete fast packet and complete original-\(t=1\) residual remain
open.  Every original \(t\ge2\) small-\(G\) incidence, the large-\(G\)
near-resonant complement, the hard and smooth M1 parents, GAR, every M2
parent, endpoint uniformity, M9, both bridges, and the quarter target
remain open or conditional at their existing scopes.

The internal exponent \(1/3\), accepted external benchmark
\(0.3144831759740614\ldots\), and target \(1/4\) are unchanged.

## 7. State decision

Create one proved-internal subordinate node for the signed-inverse
transport reduction.  Add it only as a dependency and inconclusive
evidence item to the still-open hard-M1 small-\(t\) residual owner.
Narrow that owner's next action to the exact rho-large remainder, with
the \(Y/(Qm)\) deficit and literal carry/endpoint/mask/phase correlation
stated explicitly.

Reject modewise use of the full-anchor parity, assumed transport
invariance, separate orientation norms, positive variation or
completion closure, and bounded-array literal-lower-mass claims.  Make
no status or exponent change to a complete \(t=1\), small-\(t\), M1,
M2, endpoint, M9, bridge, or theorem owner.

Round 191 closes under exactly:
strict_fast_height_jump_sector.
