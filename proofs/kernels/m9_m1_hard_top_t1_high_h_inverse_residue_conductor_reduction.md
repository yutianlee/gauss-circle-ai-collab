# Hard-M1 \(t=1\) high-height inverse-residue conductor reduction

- Campaign: `m9-m1-t1-high-h-inverse-residue-fourier-gate`
- Round: 187
- Starting graph SHA-256:
  `d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a`
- Source candidate:
  `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/candidates/formalized_hard_m1_t1_high_h_inverse_residue_conductor_reduction.md`,
  SHA-256
  `c2f01f57a41695d73d0d1f9716a03328147dbe79f0fcdeb7e8e3465b29779b89`
- Conductor reconciliation:
  `rounds/codex-managed/m9-m1-t1-high-h-inverse-residue-fourier-gate/reviews/conductor_round187_report_reconciliation.md`,
  SHA-256
  `b3de83554db114db91b33a8e994f0daa3cd9d9c41550eceabd575fbca1250705`
- Evidence status: durable proof-kernel candidate; pending repaired-hash
  replay and State Patch validation
- Numerical theorem evidence: none

## Accepted statement

Fix real \(X\ge2\), one literal middle or lower residual hard-M1 shell
\(L\ge2\), \(\sigma\in\{+1,-1\}\), and fixed \(B>0\).  Put

\[
 R_0=\lceil L\rceil,\qquad
 Q=H_B=\lfloor(\log(2X))^B\rfloor.
\]

Here \(e(x)=e^{2\pi i x}\), \([x]_U\in\{0,\ldots,U-1\}\) denotes
the least residue modulo \(U\), and \(\bar vv\equiv1\pmod U\).

Fix a nonempty dyadic block \(Y<h\le2Y\) with \(Y>H_B\).  Use exactly
the primitive carrier and literal amplitudes of the accepted tangent-gcd
kernel (K185.27), (K185.30)--(K185.35):

\[
 \mathfrak f=(\kappa,g,h,U,v),\quad
 \kappa,g,h,U,v>0,\quad \kappa,g,U\text{ odd},
\]

\[
 (gU,v)=1,\quad(U,h)=1,\quad0<2\kappa gh<R_0,
\]

\[
 A_{\mathfrak f,\omega}^{\sigma}
 :=\sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t).
\tag{K187.1}
\]

Thus every residual selector, squarefree and allocation-coprimality
deletion, profile, floor, star, half-weight, hard sample, crossing,
endpoint, conjugation, Fejer factor, square-root phase, sign, and zero
extension remains inside \(B_{\mathfrak f,\omega}^{\sigma}\).

For odd \(U>1\), set

\[
 a_{\mathfrak f}=[\bar vh]_U,\qquad
 \epsilon_+=1,\quad\epsilon_-=-1,
\]

\[
 E_U(a)=(-1)^{[a]_U},\qquad
 c_U(k)={2\over U\{1+e(-k/U)\}},\qquad
 q_U(k)={U\over(k,U)},
\tag{K187.2}
\]

and \(|k|_U=\min(k,U-k)\) for \(0\le k<U\).  Retain separately the
\(U=1\) anchors

\[
 (S_{0,+},w_{0,+})=(0,-h),\qquad
 (S_{0,-},w_{0,-})=(0,h).
\tag{K187.3}
\]

Define the complete \(U=1\) complex contribution exactly by

\[
 \mathscr U_{1,Y}^{\sigma}
 :=\sum_{\omega\in\{+,-\}}
 \sum_{\substack{\mathfrak f:\,Y<h\le2Y\\U=1}}
 A_{\mathfrak f,\omega}^{\sigma},
\]

where \(\mathfrak f\) remains restricted by the inherited primitive
carrier.  For \(U>1\), partition the Fourier modes into

\[
 \mathcal K_{\le Q}(U)=\{k\bmod U:q_U(k)\le Q\},
\tag{K187.4}
\]

\[
 \mathcal K_{\mathrm{edge}}(U)
 =\{k\bmod U:q_U(k)>Q,
       \ U\le4Q\ \text{or}\ 0<|k|_U\le Q\},
\tag{K187.5}
\]

\[
 \mathcal K_{\mathrm{high}}(U)
 =\{1\le k<U:U>4Q,\ q_U(k)>Q,\ |k|_U>Q\}.
\tag{K187.6}
\]

Define \(\mathscr P_{Y,\le Q}^{\sigma}\),
\(\mathscr L_{Y,Q}^{>,\sigma}\), and
\(\mathscr R_{Y,Q}^{\sigma}\) by inserting respectively the three
mode sets (K187.4)--(K187.6) into

\[
 \sum_{\omega\in\{+,-\}}
 \sum_{\substack{\mathfrak f\\Y<h\le2Y,\ U>1}}
 \sum_{k\bmod U}
 c_U(k)e(\epsilon_\omega k\bar vh/U)
 A_{\mathfrak f,\omega}^{\sigma}.
\tag{K187.7}
\]

Then the original dyadic high-height block has the exact decomposition

\[
 \boxed{
 \mathcal S_Y^{\sigma}
 =\Re\{\mathscr U_{1,Y}^{\sigma}
       +\mathscr P_{Y,\le Q}^{\sigma}
       +\mathscr L_{Y,Q}^{>,\sigma}
       +\mathscr R_{Y,Q}^{\sigma}\}.}
\tag{K187.8}
\]

The strict transformed packet is target-safe:

\[
 |\mathscr U_{1,Y}^{\sigma}|
 +|\mathscr P_{Y,\le Q}^{\sigma}|
 +|\mathscr L_{Y,Q}^{>,\sigma}|
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{K187.9}
\]

The available positive estimate for the exact complement is only

\[
 |\mathscr R_{Y,Q}^{\sigma}|
 \ll_\varepsilon YL^2X^\varepsilon.
\tag{K187.10}
\]

Consequently the original one-sided target is equivalent, up to the
absolutely target-safe term (K187.9), to the still-open relation

\[
 \boxed{
 \Re\mathscr R_{Y,Q}^{\sigma}
 \ll_{B,\varepsilon}L^2X^\varepsilon.}
\tag{K187.11}
\]

There is one real part outside both orientations, every height, primitive
row, Fourier mode, affine site, selector state, endpoint, and phase in
(K187.8) and (K187.11).

## Fourier normalization and exact-conductor partition

For odd \(U\), finite geometric summation and Fourier inversion give

\[
 \widehat E_U(k)
 =\sum_{a=0}^{U-1}(-1)^ae(-ka/U)
 ={2\over1+e(-k/U)},
\tag{K187.12}
\]

\[
 E_U(a)=\sum_{k\bmod U}c_U(k)e(ka/U),\qquad
 c_U(0)={1\over U},
\tag{K187.13}
\]

\[
 c_U(k)={e(k/(2U))\over U\cos(\pi k/U)},\qquad
 \sum_{k\bmod U}|c_U(k)|\ll\log(2U),\qquad
 \sum_{k\bmod U}|c_U(k)|^2=1.
\tag{K187.14}
\]

For \(q=q_U(k)\), there is a unique representation

\[
 k={U\over q}a,\qquad q\mid U,\qquad a\in\mathbb U(q),
\tag{K187.15}
\]

where
\(\mathbb U(q)=(\mathbb Z/q\mathbb Z)^\times\) for \(q>1\),
\(\mathbb U(1)=\{0\}\), and \(a=0\) for \(k=0\).  With

\[
 c_1(0)=1,\qquad
 c_q(a)={2\over q\{1+e(-a/q)\}}\quad(q>1),
\]

one has exactly

\[
 c_U(k)={q\over U}c_q(a),\qquad
 e(\epsilon_\omega k\bar vh/U)
 =e(\epsilon_\omega a\bar vh/q).
\tag{K187.16}
\]

The \(q=1\) term is the exact mean \(1/U\).  Equations
(K187.12)--(K187.16) and the disjoint mode sets
(K187.4)--(K187.6) prove (K187.8) without rearrangement error.

## Literal count and target-safe packets

The inherited multiplicity-one carrier and endpoint bound give, for
fixed \((\kappa,g,h,U)\),

\[
 \sum_{\omega,v,t}
 |B_{\mathfrak f,\omega}^{\sigma}(t)|
 \ll_\varepsilon LX^\varepsilon,
\tag{K187.17}
\]

\[
 U\ll {L\over\kappa g},\qquad
 \kappa g\ll {L\over h},
\tag{K187.18}
\]

and

\[
 \sum_{Y<h\le2Y}
 \sum_{\kappa g\ll L/h}1
 \ll L\log(2L).
\tag{K187.19}
\]

The complete \(U=1\) contribution is therefore
\(O_\varepsilon(L^2X^\varepsilon)\).

For the stronger conductor grouping, put \(u=gU\), \(n=gh\).  Literal
support gives

\[
 u,v\asymp {L\over\kappa},\qquad n\ll {L\over\kappa},
\]

and hence \(h=n/g\ll U\).  At fixed \((\kappa,u,U)\), there are
\(O(U)\) possible heights, \(O(L/\kappa)\) values of \(v\), and
\(O(\kappa)\) live affine sites per row.  Both orientations together
therefore contain \(O(UL)\) literal atoms.

At exact conductor \(q\), (K187.14)--(K187.16) give coefficient mass

\[
 {q\over U}
 \sum_{a\in\mathbb U(q)}|c_q(a)|
 \ll {q\over U}\log(2q).
\tag{K187.20}
\]

Thus its fixed-\((\kappa,u,U)\) cost is
\(O_\varepsilon(Lq\log(2q)X^\varepsilon)\).  Since
\(q\mid U\mid u\), elementary divisor summation gives

\[
 \begin{aligned}
 |\mathscr P_{Y,\le Q}^{\sigma}|
 &\ll_\varepsilon
 LQ\log(2Q)X^\varepsilon
 \sum_{\kappa\ll L}
 \sum_{u\asymp L/\kappa}\tau(u)^2\\
 &\ll_\varepsilon
 QL^2\{\log(2LQ)\}^{O(1)}X^\varepsilon
 \ll_{B,\varepsilon}L^2X^\varepsilon.
 \end{aligned}
\tag{K187.21}
\]

Here \(\tau\) is the divisor function; below \(\mu\) denotes the
Möbius function.

For \(U\le4Q\), the full Fourier mass is \(O(\log(2U))\).  For
\(U>4Q\), (K187.14) gives

\[
 \sum_{0<|k|_U\le Q}|c_U(k)|\ll {Q\over U}.
\tag{K187.22}
\]

Summing (K187.17)--(K187.19), first in \(U\), proves the remaining
part of (K187.9).  The fixed-polylogarithmic \(Q\), divisor powers, and
logarithms are absorbed by a fresh epsilon budget.  No power of \(Y\)
is absorbed.

Using the full \(O(\log(2U))\) Fourier mass and then
\(U\ll L/(\kappa g)\) gives

\[
 \begin{aligned}
 |\mathscr R_{Y,Q}^{\sigma}|
 &\ll_\varepsilon
 L^2\log(2L)X^\varepsilon
 \sum_{Y<h\le2Y}
 \sum_{\kappa g\ll L/h}{1\over\kappa g}\\
 &\ll_\varepsilon
 YL^2\{\log(2L)\}^{O(1)}X^\varepsilon,
 \end{aligned}
\]

which is (K187.10) after rebudgeting.  This calculation retains the
complete factor \(Y\) and does not prove (K187.11).

## Centered-conductor and positive-energy controls

For a unit \(b\bmod q\), define

\[
 K_q(b)=\sum_{a\in\mathbb U(q)}c_q(a)e(ab/q),\qquad
 K_q^\circ(b)=K_q(b)-{\mu(q)\over q}.
\tag{K187.23}
\]

Exact-conductor inversion and the unit Ramanujan sum give

\[
 E_U(b)=\sum_{q\mid U}{q\over U}K_q(b),\qquad
 K_q(b)+K_q(-b)={2\mu(q)\over q}.
\tag{K187.24}
\]

Hence \(K_q^\circ(-b)=-K_q^\circ(b)\), and for every odd \(U>1\),

\[
 E_U(b)A_+ +E_U(-b)A_-
 =\sum_{\substack{q\mid U\\q>1}}{q\over U}
 K_q^\circ(b)(A_+-A_-),
\tag{K187.25}
\]

because \(\sum_{q\mid U}\mu(q)=0\).  For prime \(U=p\),

\[
 K_p^\circ(b)=E_p(b).
\tag{K187.26}
\]

Thus centering is an exact self-return, not an estimate.

For odd \(U>4Q\), the two modes \(k=(U\pm1)/2\) belong to
\(\mathcal K_{\mathrm{high}}(U)\) and satisfy

\[
 |c_U(k)|={1\over U\sin(\pi/(2U))}\ge {2\over\pi},
\]

so

\[
 \sum_{\substack{q_U(k)>Q\\|k|_U>Q}}|c_U(k)|^2
 \ge {8\over\pi^2}.
\tag{K187.27}
\]

Deleting the proved low packets therefore leaves constant Fourier
\(\ell^2\)-mass.  Positive Fourier, Poisson, conductor, or alias energy
reconstructs the original signed block or positive residue-bucket energy;
it supplies no automatic factor \(Y\).  Bounded adversarial weights can
attain the carrier capacity by cancelling the anchor, affine parity, and
phase.  This is a coefficient-uniform mechanism control only: those
weights need not be realizable by the actual endpoint product, and no
literal lower mass or failure of (K187.11) is asserted.

## Exact scope

The proved content is the strict target-safe transformed packet
(K187.9), the exact complement (K187.6)--(K187.8), and the scoped
self-return controls (K187.23)--(K187.27).  The first unproved relation
is exactly (K187.11), which needs a new jointly signed property of the
actual literal amplitude in \((h,v,t,k)\) before any positive
recombination.

Even a proof of (K187.11) would close only the exact original-\(t=1\)
residual through the accepted Round-184/185 connectors.  Every original
\(t\ge2\) small-\(G\) incidence, the large-\(G\) near-resonant
complement, the complete hard and smooth M1 parents, GAR, every M2
parent, endpoint uniformity, M9, both bridges, the quarter target, and
every exponent claim remain open.

Direct accepted dependencies are:

- `M9-M1-hard-top-t1-residual-fejer-tangent-gcd-reduction`;
- `Divisor-bound-elementary`.

No external theorem is used.  The bounded Mathematica computation checks
finite normalization and alias identities only and is diagnostic, not
theorem evidence.

## Reviewed evidence

- the hash-bound formal candidate and conductor reconciliation;
- `reports/literal_height_fourier_attack.md`;
- `reports/deletion_resonance_capacity_audit.md`;
- `reports/blind_high_h_rederivation.md`;
- `reviews/inverse_residue_normalization_multiplicity_seam_review.md`;
- `reviews/inverse_residue_normalization_multiplicity_post_repair_verification.md`;
- `reviews/candidate_normalization_post_tex_repair_verification.md`;
- `reviews/power_literal_scope_self_return_seam_review.md`;
- `reviews/power_literal_scope_post_tex_repair_verification.md`; and
- `reviews/blind_post_unmask_owner_scope_seam_review.md`.

The blind report proves the direct small-modulus and ordinary-edge
packet, but not the complete small exact-conductor grouping.  The latter
rests on the discovery and hostile derivations plus independent seam
review.

The bounded diagnostic artifacts are:

- `controls/conductor_round187_wolfram_inverse_residue_check.md`,
  SHA-256
  `032d8039636b0e4e2040caed7c0d2ade507d111a7f966b9b40f03676fadd1113`;
- `controls/inverse_residue_exact_check.wls`, SHA-256
  `e818367a710c4051f9259966133ca48b94810a55544b4b0ec3d3fbab15a06bcd`.

They check finite normalization, inversion, orientation, and alias-fold
identities only and are not asymptotic theorem evidence.
