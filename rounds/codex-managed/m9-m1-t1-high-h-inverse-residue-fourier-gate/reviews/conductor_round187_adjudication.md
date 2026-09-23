# Conductor Round 187 adjudication

- Campaign: `m9-m1-t1-high-h-inverse-residue-fourier-gate`
- Round: 187
- Role: authoritative round-closing mathematical decision
- Generated: 2026-08-29T15:46:47+08:00
- Starting graph SHA-256:
  `d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a`
- Durable kernel SHA-256:
  `a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2`
- Decision status: mathematically closed; pending independent State Patch
  reverse audit and mechanical application

## 1. Result and terminal label

Round 187 closes mathematically under the sole label

`strict_high_h_inverse_residue_fourier_sector`.

Fix real \(X\ge2\), a literal middle or lower residual hard-M1 shell
\(L\ge2\), \(\sigma\in\{+1,-1\}\), fixed \(B>0\), and a nonempty
dyadic block

\[
 H_B=\lfloor(\log(2X))^B\rfloor<Y<h\le2Y.
\]

Use exactly the accepted Round-185 primitive tangent-gcd carrier,
canonical \(U>1\) anchors, separate \(U=1\) convention, positive
oriented affine index sets, and literal endpoint amplitudes.  The exact
inverse-residue Fourier expansion proves that the following transformed
packet has total absolute size

\[
 O_{B,\varepsilon}(L^2X^\varepsilon):
\]

1. the complete \(U=1\) contribution;
2. every Fourier mode of exact conductor
   \(q_U(k)=U/(k,U)\le H_B\), including the zero mode;
3. inside \(q_U(k)>H_B\), every mode with \(U\le4H_B\); and
4. inside \(q_U(k)>H_B\), \(U>4H_B\), every ordinary edge mode
   \(0<|k|_U\le H_B\).

This is a strict transformed Fourier sector, not a physical-incidence
partition and not the complete dyadic theorem.

## 2. Exact complement

For odd \(U>1\), let

\[
 E_U(a)=(-1)^{[a]_U},\qquad
 c_U(k)=\frac{2}{U\{1+e(-k/U)\}}.
\]

The original block decomposes exactly as

\[
 \mathcal S_Y^\sigma
 =\Re\{\mathscr U_{1,Y}^\sigma+
          \mathscr P_{Y,\le H_B}^\sigma+
          \mathscr L_{Y,H_B}^{>,\sigma}+
          \mathscr R_{Y,H_B}^\sigma\}.
\]

There is one real part outside both orientations, every height, row,
mode, affine index, selector state, endpoint, and phase.  The exact
complement \(\mathscr R\) contains precisely

\[
 U>4H_B,\qquad q_U(k)>H_B,\qquad |k|_U>H_B.
\]

Its available positive estimate is only

\[
 |\mathscr R_{Y,H_B}^\sigma|
 \ll_\varepsilon YL^2X^\varepsilon.
\]

Thus the first open relation is still

\[
 \boxed{\Re\mathscr R_{Y,H_B}^\sigma
        \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{187.O1}
\]

The full factor \(Y\) remains missing.

## 3. Exact conductor proof and powers

Finite geometric summation gives

\[
 \widehat E_U(k)=\frac{2}{1+e(-k/U)},\qquad
 E_U(a)=\sum_{k\bmod U}c_U(k)e(ka/U),
\]

with \(c_U(0)=1/U\),
\(\sum_k|c_U(k)|\ll\log(2U)\), and
\(\sum_k|c_U(k)|^2=1\).

If \(q=U/(k,U)\), then uniquely

\[
 k=\frac Uq a,\qquad q\mid U,\qquad
 a\in(\mathbb Z/q\mathbb Z)^\times,
\]

with the special \(q=1,a=0\) convention, and

\[
 c_U(k)=\frac qU c_q(a),\qquad
 e(\epsilon_\omega k\bar vh/U)
 =e(\epsilon_\omega a\bar vh/q).
\]

The decisive literal count uses

\[
 u=gU,\qquad n=gh.
\]

On support,

\[
 u,v\asymp L/\kappa,\qquad n\ll L/\kappa,
\]

so \(h\ll U\).  At fixed \((\kappa,u,U)\), both orientations
together contain \(O(UL)\) live \((h,v,t)\)-atoms.  Exact conductor
\(q\) has coefficient mass

\[
 O\!\left(\frac qU\log(2q)\right),
\]

so it costs \(O_\varepsilon(Lq\log(2q)X^\varepsilon)\) at fixed
\((\kappa,u,U)\).  Summing \(q\mid U\mid u\), \(q\le H_B\), and
the divisor powers proves the complete low exact-conductor packet at
\(O_{B,\varepsilon}(L^2X^\varepsilon)\).  Separate small-\(U\) and
ordinary-edge ledgers prove the rest of the strict packet.  No power of
\(Y\) is absorbed.

## 4. Mechanism boundary

For a unit \(b\), define

\[
 K_q(b)=\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}
 c_q(a)e(ab/q),\qquad
 K_q^\circ(b)=K_q(b)-\frac{\mu(q)}q.
\]

Then

\[
 E_U(b)A_+ +E_U(-b)A_-
 =\sum_{\substack{q\mid U\\q>1}}\frac qU
 K_q^\circ(b)(A_+-A_-).
\]

For prime \(U=p\), \(K_p^\circ(b)=E_p(b)\); the sole centered high
conductor is literally the original orientation block.  Moreover the
two modes \(k=(U\pm1)/2\) lie in the exact complement and satisfy

\[
 |c_U(k)|\ge\frac2\pi,\qquad
 \sum_{\substack{q_U(k)>H_B\\|k|_U>H_B}}|c_U(k)|^2
 \ge\frac8{\pi^2}.
\]

Therefore conductor centering, raw orientation antisymmetry, positive
Fourier or alias energy, positive Poisson recombination, and bare affine
alternation do not themselves recover \(Y\).  The adversarial bounded
controls attain coefficient-uniform capacity but are not realizable
literal lower-mass theorems and do not disprove (187.O1).

## 5. Controls and independent reviews

The discovery, hostile, and statement-only reports agree on the
carrier, normalization, direct safe packet, exact joint complement, and
missing factor.  The discovery and hostile reports independently prove
the stronger complete low exact-conductor packet.  The blind report is
not credited with that strengthening.

The candidate received independent normalization/multiplicity,
power/literal-scope/self-return, and blind post-unmask reviews.  Local
report and candidate TeX defects were repaired and replayed.  The
durable kernel then received independent candidate-consistency,
hostile-power/owner, and formalization/provenance reviews.  The final
post-repair reviews are GREEN at kernel hash
`a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2`:

- candidate consistency:
  `3e9412b4404ca8399ed2350f459117b6b8b84fe479820a4e12a39da7bad1bb4d`
  for the first repaired replay, followed by the final hash-only
  verification;
- power and owner scope:
  `602a56c4ece7fce4a9e415eb9e95ce7e089dd690630e52fc2f28b16b4c08c0cc`;
- formalization and provenance:
  `5f3679b342a9210a2e0baa5c27ff82fc1fa5804bc662c8ea6e9c56886e0e417e`.

The bounded Mathematica check verifies finite normalization, inversion,
orientation, and alias-fold identities only.  It is diagnostic and is
not asymptotic theorem evidence.  No external theorem is used.

## 6. Dependencies and exact scope

Direct accepted dependencies are:

- `M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction`;
- `Divisor-bound-elementary`.

The complete high-height relation, the exact original-\(t=1\) residual,
every original \(t\ge2\) small-\(G\) incidence, the large-\(G\)
near-resonant complement, the complete hard small-\(t\) owner, the
independent smooth M1 parent, GAR, all M2 parents, endpoint uniformity,
M9, both bridges, and the Gauss-circle target remain open.

The exponent ledger remains:

- internally proved: \(1/3\);
- accepted external Li--Yang:
  \(0.3144831759740614\ldots\);
- target: \(1/4\).

## 7. State decision

Create one subordinate proved-internal node

`M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction`

for the exact Fourier decomposition, strict target-safe packet, exact
complement, and scoped self-return controls.  Add only that dependency
and the Round-187 evidence to the still-open hard-M1 small-\(t\) owner,
and narrow its next action to (187.O1).  Record the audited mechanism,
coverage, parent, and exponent overclaims as rejected.

Change no inherited owner status, implication, blocker, bridge, theorem,
or exponent.  Apply the State Patch only after mechanical validation and
an independent reverse/replay audit.

