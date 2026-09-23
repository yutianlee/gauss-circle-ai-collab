# Final independent verification of the Round-171 commutator kernel

- Campaign: `m9-m2-balanced-critical-j1-two-defect-commutator-gate`
- Round: 171
- Role: final independent kernel verifier
- Starting graph SHA-256:
  `4c98bb13558c06159c5ad23128c6f6ff52970db296863858832309a24a4720ac`
- Allocation: 100% analytic/algebraic; 0% numerical
- Verdict: **REPAIR**

## 1. Result

The conductor kernel and candidate support one durable, route-scoped
`proved_internal` obstruction after three narrow presentation repairs.  The
coordinate identities, parity ledger, axial counts, two displayed
unnormalized commutators, real endpoint-swap projection, mixed summation by
parts, primitive lower bound, gate increments, fixed-width strip count, and
fixed-\(Q\) formulas are all algebraically correct.  In particular,

\[
 [\mathfrak P,\mathfrak Q]=8(y-x)T_sT_q^2,
\]

\[
 \langle W,H\rangle_G
 =\langle P_{++}W,P_{++}H\rangle_G
 +\frac1{16}\langle D_hD_kW,D_hD_kH\rangle_G,
\]

and

\[
 \mathcal R_B^{\rm osc}
 =\frac12\sum_{h,k,s,q}(-1)^s(q-q_0)D_sD_qF_{h,k}(s,q)
\]

have the stated signs and constants.

The three required repairs do not change the no-go conclusion.

1. The endpoint-swap ambient domain must be stated as a rectangle in the
   endpoint variables \((h,h',k,k')\), or equivalently as the invariant
   shifted domain \(h,h+p\in I_h\), \(k,k+q\in I_k\).  It is not literally
   a rectangle in independent \((h,k,p,q)\)-coordinates.
2. In the boundary section, \(J\) must denote only the positive
   geometric/profile support of \(A_B\), with the low-gcd weight left in
   \(Y\).  If “literal support” means the support of the full coefficient
   \(a\), it contains arithmetic gcd holes and the claimed
   one-coordinate \(O(L^3)\) support-face count does not follow.
3. The no-go and the candidate's “all unnormalized controls” wording must
   be restricted to the operators actually displayed.  The ordinary
   commutator (171.K13) needs its own affine singular-line sentence, or it
   should be removed from the claimed completed placements.  Composite
   backward/ordered Weyl commutators from the ramp review are nonzero and
   are not classified by (171.K11)--(171.K16).

After these repairs, the exact result is a capacity obstruction for the
listed local, coefficient-independent placements.  It is not a physical
lower bound, does not prove or disprove the critical remainder, and licenses
no parent, bridge, theorem, or exponent change.

## 2. Exact statement and hypotheses audited

Fix one persistent critical \(j=1\) literal balanced block with
\(L\asymp K\asymp X^{1/6}\).  The real coefficient is

\[
 a(h,k)=\chi_4(h)\eta\!\left(\frac{(h,k)}{\sqrt L/2}\right)A_B(h,k),
\]

zero extended off the positive literal domain.  Every square root is
evaluated only on the positive ambient endpoint rectangle; a coefficient is
set to zero before any out-of-domain phase would be evaluated.  The strict
double-far mask remains

\[
 G=1_{|\Delta|>L}1_{|\rho|>L},\qquad
 \Delta=h'k'-hk,\quad \rho=hk'-h'k.
\]

The ordered-pair chart

\[
 (h,k,h',k')\longleftrightarrow(h,k,p=h'-h,q=k'-k)
\]

has multiplicity one, including negative \(p,q\).  Off the axes, with
\(u=\Delta+\rho\), \(v=\Delta-\rho\), the inverse is

\[
 h=\frac12\left(\frac uq-p\right),\qquad
 k=\frac12\left(\frac vp-q\right).
\]

The kernel now correctly retains

\[
 p\in2\mathbb Z,quad q\mid u,quad p\mid v,quad
 \frac uq-p\equiv2\pmod4,quad
 \frac vp-q\equiv0\pmod2,
\]

plus positivity, both support tests, and \(u\equiv v\pmod2\) if \(u,v\)
are introduced independently.  These are the required reconstructed
character and integrality conditions.  The inverse is not used at
\(pq=0\).

The audited operator class is only:

- the four elementary \([D_s,M_U]\), \([D_q,M_U]\),
  \([D_s,M_V]\), \([D_q,M_V]\) placements and their displayed
  normalizations;
- the displayed ordinary and parity-compatible commutators built from
  those elementary operators;
- the independent endpoint swaps; and
- coefficient-independent local first-difference Abel summation in the
  uncharactered \(q\)-direction, followed only by the currently accepted
  positive owners.

Weighted, coefficient-adapted, nonlocal, or undisplayed composite
commutators are outside the theorem.

## 3. Proof and equation-by-equation verification

### 3.1 Coordinates, parity, axes, and the fixed-width strip

Substitution of \(h'=h+p\), \(k'=k+q\) gives

\[
 \Delta=hq+kp+pq,\qquad \rho=hq-kp,
\]

and hence

\[
 \Delta+\rho=q(2h+p),\qquad
 \Delta-\rho=p(2k+q).
\]

For \(p=2s\) and odd \(h\),

\[
 \chi_4(h)\chi_4(h+2s)=(-1)^s.
\]

On \(p=0\), \(\Delta=\rho=hq\), leaving \(O(LK^2)\) triples.  On
\(q=0\), \(\Delta=kp\), \(\rho=-kp\), leaving \(O(KL^2)\) triples.
Bounded weights and \(|e(t)-1|\le2\) therefore give
\(O_\varepsilon(L^3X^\varepsilon)\) for each axis, and their intersection
is not double-far.

For fixed \(t=y-x=(k+k')-(h+h')\), choosing \((h,h',k)\) determines
\(k'=h+h'+t-k\).  Hence every fixed-width \(|y-x|\le C\) strip has
\(O_C(L^3)\) possible ordered quadruples and absolute mass
\(O_{C,\varepsilon}(L^3X^\varepsilon)\).  No multiplicity or missing axis
factor occurs.

### 3.2 Normalized and specified unnormalized commutators

With \(D_s=T_s-I\), \(D_q=T_q-I\),

\[
 x=2h+2s,quad y=2k+q,quad U=qx,quad V=2sy,
\]

the general identity \([D_t,M_w]=(D_tw)T_t\) yields exactly

\[
\begin{array}{c|cc}
 &M_U&M_V\\ \hline
 [D_s,\,\cdot]&2qT_s&2yT_s\\
 [D_q,\,\cdot]&xT_q&2sT_q.
\end{array}
\]

Thus the side-sum normalizations are \(T_q,T_s\), and the two cross
normalizations are shifts away from the already paid axes.  Their normalized
commutators vanish because the shifts commute.

For \(\mathcal C_s=2yT_s\), \(\mathcal C_q=xT_q\), direct composition
gives

\[
 \mathcal C_s\mathcal C_q=2y(x+2)T_sT_q,qquad
 \mathcal C_q\mathcal C_s=2x(y+1)T_sT_q,
\]

so (171.K13),

\[
 [\mathcal C_s,\mathcal C_q]=2(2y-x)T_sT_q,
\]

has the correct sign.  It has a separate singular line \(2y=x\).  If this
formula remains part of the durable no-go, the kernel should add that a
fixed-width \(|2y-x|\le C\) strip is again \(O_C(L^3X^\varepsilon)\),
while off it division returns \(T_sT_q\) and

\[
 \sum(-1)^s(T_sT_q-I)F=-2\sum(-1)^sF.
\]

For the parity-compatible \(\widehat T_q=T_q^2\),

\[
 \mathfrak P=2yT_s,qquad \mathfrak Q=2x\widehat T_q.
\]

Since \(T_sx=x+2\) and \(\widehat T_qy=y+2\),

\[
 \mathfrak P\mathfrak Q=4y(x+2)T_s\widehat T_q,qquad
 \mathfrak Q\mathfrak P=4x(y+2)T_s\widehat T_q,
\]

which proves the sign and factor \(8(y-x)\) in (171.K14).  Reindexing
\((s,q)\mapsto(s+1,q+2)\) proves the factor \(-2\) in (171.K15).

The ramp review also displays nonzero backward/composite commutators such as
\([M_U\nabla_p,M_V\nabla_q]\) and \([M_UT_p,M_VT_q]\).  Their formulas
are consistent Weyl identities, but they are not derived by the kernel.
Accordingly, the node must not claim a classification of all local
coordinate-generated commutators.

### 3.3 Real endpoint swaps and zero extension

Let \(I_h,I_k\subset\mathbb Z_{>0}\) contain the geometric supports and
sum on

\[
 \Omega=\{(h,h',k,k'):h,h'\in I_h,\ k,k'\in I_k\}.
\]

In shift coordinates this is
\(h,h+p\in I_h\), \(k,k+q\in I_k\); it is invariant under both swaps.
This is the exact domain needed in Section 4 of the kernel.

Writing \(W=a_{00}a_{11}\) and
\(H=z_{00}\overline{z_{11}}-1\), reality gives

\[
 \tau_hW=\tau_kW=a_{10}a_{01},\qquad \tau_h\tau_kW=W.
\]

Consequently \(P_{+-}W=P_{-+}W=0\),

\[
 P_{++}W=\frac12(a_{00}a_{11}+a_{10}a_{01}),
\]

and, with \(A=z_{00}\overline{z_{11}}\),
\(B=z_{01}\overline{z_{10}}\),

\[
 P_{++}H=\frac14(A+\overline A+B+\overline B-4)
 =-\frac14\bigl(|z_{00}-z_{11}|^2+|z_{01}-z_{10}|^2\bigr).
\]

Also \(P_{--}W=\frac14D_hD_kW\) and
\(P_{--}H=\frac14D_hD_kH\), giving the factor \(1/16\) in (171.K18).
The pairing is bilinear, not sesquilinear; the original conjugation is
already contained in the phase and the real coefficient.  Gate invariance
under \((\Delta,\rho)\mapsto(\rho,\Delta)\) and
\((\Delta,\rho)\mapsto(-\rho,-\Delta)\) makes both swaps self-adjoint.
Global coefficient zero extension absorbs cross-corner support failures.

### 3.4 Mixed summation by parts, ramp, and boundaries

For forward shifts,

\[
 \sum_s(-1)^sD_sG=-2\sum_s(-1)^sG,
\qquad
 \sum_qG=-\sum_q(q-q_0)D_qG.
\]

The two minus signs therefore give the positive factor \(1/2\) in
(171.K20).  For a coefficientwise first-difference representation on an
interval of \(N\) points, comparison at \(f(r)\) gives
\(c(r)-c(r+1)=1\), so \(|c(a)-c(b+1)|=N\) and
\(\max|c|\ge N/2\).  This verifies (171.K21)--(171.K22).

The four-corner product rule (171.K23) is exact.  The gate increments

\[
\begin{array}{c|cc}
 &\Delta_+-\Delta&\rho_+-\rho\\ \hline
 s\mapsto s+1&2(k+q)&-2k\\
 q\mapsto q+1&h+2s&h
\end{array}
\]

also have the correct signs.  To make the claimed complete face expansion
self-contained, the kernel should insert, on each oriented edge,

\[
\begin{aligned}
 I_+-I_0={}&(J_+-J_0)H^\Delta_+H^\rho_+\\
 &+J_0(H^\Delta_+-H^\Delta_0)H^\rho_+\\
 &+J_0H^\Delta_0(H^\rho_+-H^\rho_0).
\end{aligned}
\]

Here \(J\) must be the geometric/profile support indicator only.  Both
low-gcd weights, including their arithmetic zeros and unit differences,
remain in \(Y\).  With that convention, one-step geometric support faces
have three free length-\(L\) coordinates, and changed gates lie in the
accepted width-\(O(L)\) corridors; their unweighted positive ledger is
\(O_\varepsilon(L^3X^\varepsilon)\).  If instead \(J\) is the support of
the full coefficient \(a\), the gcd cutoff creates non-interval arithmetic
holes and the asserted face count has not been proved.

The forced primitive does not prove that a literal face has physical
\(L^4\) mass.  It proves that the current coefficient-independent
positive-variation closure can cost an extra \(L\), and the adversarial
shadow realizes that capacity.  The kernel and candidate should consistently
say “available/certified positive ledger” rather than an unavoidable
physical amplification.

### 3.5 Fixed-\(Q\), restoration, and power scope

From

\[
 c=\frac\lambda R\sqrt{h/k},\quad A=k'/k,\quad
 h'=Xk'/\lambda^2=hA/c^2,
\]

direct substitution gives

\[
 \rho=hk'\frac{c^2-1}{c^2},\qquad
 \Delta=hk\frac{A^2-c^2}{c^2}.
\]

At \(A=1\), \(\Delta=-\rho\), so fixed-\(Q\) rulings can remain beyond
both corridors.  This only prevents reuse of the accepted positive
broad--narrow owner; it does not prove a universal rulingwise no-go.

The stated \(L^4\) and \(L^5\) quantities are coefficient-blind upper or
adversarial capacities.  They are not literal lower bounds.  Both gcd
weights, both slanted symbols, floors, stars, crossings, endpoints, and the
real centre remain in the unopened scalar.  Alias and lift data arise only
upon the accepted later expansion and must then remain corner-dependent;
the candidate should not suggest that aliases are independent pre-existing
coordinates of \(a_B^<\).

## 4. First doubtful or unproved step

The first unproved physical statement remains

\[
 |\mathcal R_B^{\rm osc}|\ll_\varepsilon L^3X^\varepsilon.
\]

Round 171 proves neither this estimate nor a lower bound contradicting it.
The first missing analytic input is a signed, owner-preserving estimate for
the surviving \((++)\) endpoint-swap complement, or a nonlocal actual-symbol
\(q\)-primitive/correlation theorem controlling the ramp-weighted geometric,
gate, and arithmetic faces before a positive norm.  Such a theorem must also
retain fixed-\(Q\) families and all literal endpoints.

The precise method obstruction is that the displayed normalized
commutators are shifts, the displayed unnormalized multipliers cancel on
division, the independent-swap decomposition leaves the \((++)\) complement,
and a coefficient-independent local first-difference representation on the
ambient length-\(L\) \(q\)-interval has coefficient size \(\gg L\).  The
kernel does not exclude a support-adapted, weighted, twisted, or nonlocal
identity exploiting the actual gcd/slanted/alias structure.

## 5. Required controls and outcomes

| control | independent outcome |
|---|---|
| exact chart and multiplicity | **GREEN.** Ordered multiplicity one; negative increments retained. |
| reconstructed parity | **GREEN.** The mod-4 oddness and mod-2 integrality conditions are complete with positivity/support tests. |
| zero extension | **REPAIR-MINOR.** Positive phase convention is correct; replace “rectangle of \((h,k,p,q)\)” by the exact invariant endpoint domain. |
| \(p=0,q=0\) axes | **GREEN.** Each is absolutely \(O(L^3X^\varepsilon)\). |
| fixed-width \(y-x\) strip | **GREEN.** One linear relation leaves \(O_C(L^3)\) quadruples. |
| normalized commutators | **GREEN narrowly.** They are exact shifts and commute. |
| unnormalized commutators | **REPAIR-SCOPE.** (171.K13)--(171.K14) have correct signs; price or exclude the \(2y=x\) line and expressly exclude undisplayed composite Weyl commutators. |
| endpoint swaps | **GREEN.** Two projections only; bilinear identity and \(1/16\) factor are exact. |
| mixed SBP sign/factor | **GREEN.** The sign is positive and the coefficient is \(1/2\). |
| primitive lower bound | **GREEN.** Any coefficient-independent first-difference primitive on \(N\) points has supremum at least \(N/2\). |
| gate product and increments | **GREEN after presentation repair.** (171.K23)--(171.K24) are exact; add the three-factor edge expansion. |
| support-face power | **REPAIR-MATERIAL.** \(O(L^3)\) is justified for geometric/profile faces, not for arithmetic gcd-support holes. |
| ramp power ledger | **GREEN as capacity only.** Existing positive owners may lose the factor \(L\); no physical \(L^4\) lower bound follows. |
| fixed-\(Q\) ruling | **GREEN with scope.** The formulas are exact and the classes survive; only the existing positive theorem is blocked. |
| literal restoration | **GREEN with wording.** Keep gcd/profile data in the scalar; aliases/lifts are retained if the accepted expansion is opened. |
| owner quarantine | **GREEN.** The result covers only one persistent critical \(j=1\) block. |
| downstream/exponent quarantine | **GREEN.** No remainder, energy, BAL, M2, M9, bridge, theorem, or exponent status changes. |

No numerical experiment, computer algebra, or external theorem was used.

## 6. Dependencies and exact artifacts used

The authoritative graph hash was independently reproduced as
`4c98bb13558c06159c5ad23128c6f6ff52970db296863858832309a24a4720ac`.
All six dependencies named by the kernel are currently `proved_internal`:

- `M9-M2-balanced-smooth-literal-atom-dictionary`;
- `M9-M2-character-factor`;
- `M9-M2-balanced-full-product-double-corridor-reduction`;
- `M9-M2-balanced-double-far-phase-free-mode-reduction`;
- `M9-M2-balanced-divisor-progressive-alias-reduction`; and
- `M9-M2-balanced-broad-narrow-gauge-ruling-obstruction`.

The last node transitively owns the accepted alias-character restoration and
fixed-\(Q\) formulas.  These dependencies are sufficient for the scoped
obstruction and do not imply the open target.

This review read `AGENTS.md`, `protocol.md`, `state/proof_obligations.yml`,
`state/active_campaign.yml`, the current conductor kernel and candidate,
all three Round-171 reports, and all three existing Round-171 reviews:

- `reviews/blind_post_unmask_identity_scope_review.md`;
- `reviews/ramp_identity_power_seam_review.md`; and
- `reviews/literal_restoration_owner_scope_review.md`.

The blind report remains valid only through its post-unmask repair: reality
kills its two mixed projections, global zero extension absorbs its separate
support-crossing term, and the true axes are target-safe.  No report or
review is treated as accepted mathematics independently of the State Patch.

## 7. Required edits and graph-patch recommendation

**Required kernel/candidate edits before promotion:**

1. In Section 4, define the ambient endpoint rectangle
   \(I_h^2\times I_k^2\) and its invariant shifted image.  Do not call
   independent \((h,k,p,q)\) ranges a rectangle.
2. In Sections 5--6, replace “literal \(q\)-run/support” by “ambient
   geometric/profile \(q\)-interval/support” wherever the length-\(L\) run
   or \(O(L^3)\) face count is used.  Define \(J\) to exclude the arithmetic
   low-gcd cutoff, keep all gcd factors in \(Y\), and insert the exact
   three-factor edge formula displayed above.
3. Either add the \(2y=x\) strip and off-strip tautology for (171.K13), or
   narrow the candidate's completed-placement claim to (171.K14).  State
   expressly that the backward/composite commutators displayed in the ramp
   review are outside this kernel unless separately imported.
4. Replace categorical phrases that the ramp “amplifies” a literal face by
   the precise claim that the forced ramp restores the **available
   coefficient-independent positive ledger** to \(L^4\), absent a new signed
   face theorem.  Clarify that aliases/lifts are retained upon expansion,
   not independent coordinates already present in \(a_B^<\).

After those edits, create
`M9-M2-balanced-two-defect-commutator-ramp-obstruction` as type
`obstruction`, status `proved_internal`, with the six accepted dependencies
above and no implication edge.  Its statement must enumerate the audited
operator class and retain the capacity-versus-lower-bound distinction.

Add the Round-171 kernel, reports, reviews, candidate, controls,
adjudication, and synthesis only as obstruction/inconclusive evidence for
`M9-M2-balanced-double-far-oscillatory-remainder` and
`M9-M2-balanced-double-far-actual-energy`; keep both `open`.  Keep
`M9-M2-balanced-remaining-label-owner-quantifier-completion`, full BAL,
hard TOP, UNBAL, M9--M2, both M1 routes/GAR, endpoint assembly, M9, both
bridges, `GC-target`, and every exponent unchanged.

Record rejections of universal zero-commutator, deleted-axis,
three-complement, separate support-crossing, bounded coefficient-independent
\(q\)-primitive, phase-smallness, fixed-\(Q\)-deletion, physical-lower-bound,
owner-transfer, parent-promotion, and exponent-promotion claims.

**Final verdict: REPAIR.**  The scoped obstruction is promotable after the
listed statement and support-ledger repairs; the physical critical remainder
is still open.
