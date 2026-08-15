# Blind rederivation: critical radial Mellin return to terminal blocks

## 1. Result

**The corrected full critical-sector interface closes at the precise GAR
projection.**  Let
\[
 R=X^{1/4},\qquad Y=R^2,
 \qquad V\in C_c^\infty((c,C)),\qquad 0<c<C<16,
\]
and write \(\operatorname {supp}V\subset[v_0,v_1]\Subset(c,C)\).
For every stationary sample surviving the exact physical restriction
\(h\le H_j\),
\[
 V(4R^2h^2/d^2)w_j(d)\ne0
 \quad\Longrightarrow\quad
 \gamma H_j\le h\le H_j,
 \qquad \gamma=\gamma(V)>0,                                \tag{1}
\]
once \(H_j\) is larger than a fixed constant.  Only the lower terminal
margin is needed.  A lower cutoff \(\eta_j\) can be one on every active
sample, while the pre-existing exact factor
\(\mathbf1_{h\le H_j}\) owns the upper endpoint.  Extended by zero past
\(H_j\), its endpoint jump has size \(O(H_j^{-1})\), exactly within the
accepted sampled-BV interface.

This explicitly retracts my earlier claim that a strict upper margin
\(h\le\Gamma H_j\), \(\Gamma<1\), forces \(C<9/4\).  That claim
incorrectly required the auxiliary cutoff to taper before the physical
endpoint.  Since the exact height indicator is retained and its jump is
permitted, no strict upper margin is required; every fixed
\(0<c<C<16\) is support-safe.

Mellin inversion gives exactly
\[
 V\!\left({4Xh^2\over d^2Y}\right)
 ={1\over2\pi}\int_{\mathbb R}\widehat V(t)
 \left({4X\over Y}\right)^{it}h^{2it}d^{-2it}\,dt,        \tag{2}
\]
and the zero-extended height coefficient
\[
 U_{j,t}(h)=\mathbf1_{1\le h\le H_j}\eta_j(h)
 {\Phi(h/(H_j+1))\over h}h^{2it}                          \tag{3}
\]
satisfies
\[
 \|U_{j,t}\|_\infty+\sum_{h\in\mathbb Z}
 |U_{j,t}(h+1)-U_{j,t}(h)|
 \ll {1+|t|\over H_j}.                                    \tag{4}
\]
All finite-order derivative losses from \(d^{-2it}\) are polynomial in
\(1+|t|\) and integrate against the Schwartz function \(\widehat V\).
The accepted terminal theorem consequently gives
\[
 \mathcal B_{j,V}\ll_{\varepsilon,V}X^\varepsilon
 (1+D_j/H_j)\ll_{\varepsilon,V}RX^\varepsilon,            \tag{5}
\]
and the active scale sum costs only another \(X^\varepsilon\).
Bounded positive heights obey the same target scale by direct absolute
summation; \(H_j=0\) is empty.

At the stationary denominator \(d_*=2\sqrt{hX/q}\), \(n=hq\),
\[
 \left({4X\over Y}\right)^{it}h^{2it}d_*^{-2it}
 =\left({hq\over Y}\right)^{it}=\left({n\over Y}\right)^{it}. \tag{6}
\]
Thus the Mellin mode reconstructs the intended radial weight with no
normalization defect.  Using the packet-declared accepted Round-14
interior/top transform interface,
\[
 \sum_j\mathcal M_{1,j,V}
 =-{4\over\pi}R\operatorname {Re}\{e(1/8)\mathcal G_V\}
 +\mathcal E_V,
 \qquad \mathcal E_V\ll_{\varepsilon,V}RX^\varepsilon,    \tag{7}
\]
the terminal bounds prove the frozen target
\[
 \boxed{\operatorname {Re}\{e(1/8)\mathcal G_V(X)\}
 \ll_{\varepsilon,V}X^\varepsilon.}                       \tag{8}
\]
The transform formulas excluded by statement-only isolation were not
independently rederived, but no mismatch was found in their coefficient,
phase, Mellin mode, endpoint ownership, or error scale.  Equation (8) is
only the fixed real projection requested here; it gives no modulus bound
for \(\mathcal G_V\).

## 2. Exact statement and hypotheses

Assume the definitions of \(\mathcal C_X^*(n)\), \(\Omega_X^*(n,h)\),
\(\mathcal G_V(X)\), \(D_j\), \(H_j\), and \(\mathcal B_{j,V}\) from
the authorized packet.  Assume also exactly its two accepted inputs:

1. the frequency-first terminal divisor theorem, applied to the
   zero-extended coefficient (3), with finite-order
   denominator-derivative losses polynomial in \(1+|t|\); and
2. the accepted interior and one-sided top transforms, including their
   Round-14 coefficient, frequency-sign pairing, hard endpoint, starred
   stationary values, and total error, recombined as (7).

For the support audit use the actual profile ranges
\[
 {1\over2}\le {d\over D_j}\le {4\over3}
 \quad\hbox{(interior)},
 \qquad
 {1\over2}\le {d\over Y}\le1
 \quad\hbox{(top)}.                                       \tag{9}
\]
Then, for every fixed \(V\in C_c^\infty((c,C))\) with
\(0<c<C<16\), there are \(H_0\), \(\gamma>0\), and lower cutoffs
\(\eta_j\), depending only on the fixed support data, such that for
\(H_j\ge H_0\):

- \(\eta_j(h)=1\) at every simultaneous \(V\)-, profile-, and
  \(h\le H_j\)-supported stationary height;
- \(\eta_j\) vanishes below a fixed positive multiple of \(H_j\) and
  has uniformly bounded sampled variation; and
- the exact upper factor \(\mathbf1_{h\le H_j}\) is retained, including
  its full endpoint jump after zero extension.

With (3), the exact conclusion is (4), then (5), and finally (8) through
the accepted transform identity (7).  All height floors, the one-sided
top profile, \(d=\lfloor\sqrt X\rfloor\), profile/equality stars, and
the independent radial star retain their prescribed ownership.  The
condition \(C<16\) keeps the support inside the frozen sum
\(n\le16Y\); it is not a terminal upper-margin condition.  No assertion
is made about \(|\mathcal G_V|\), \(n=o(Y)\), the alpha transition, full
GAR, M9-M1, M9, or the final exponent.

## 3. Proof and derivation

### Support and endpoint ledger

From \(z=4R^2h^2/d^2\in[v_0,v_1]\),
\[
 {\sqrt{v_0}\over2}{d\over R}
 \le h\le
 {\sqrt{v_1}\over2}{d\over R}.                            \tag{10}
\]
For an interior profile, write
\(D_j/R=H_j+\theta_j\), \(0\le\theta_j<1\).  The lower side of
(9)--(10) gives
\[
 {h\over H_j}
 \ge {\sqrt{v_0}\over4}{D_j\over RH_j}
 \ge {\sqrt{v_0}\over4}.                                 \tag{11}
\]
For the top profile the same calculation with \(d/Y\ge1/2\) gives the
same fixed lower bound, up to the harmless top floor convention.  Thus
one may choose any \(0<\gamma<\sqrt{v_0}/4\), enlarge a fixed threshold
\(H_0\), and obtain (1).

The upper side of (10) is not used to manufacture a cutoff before
\(H_j\).  Some \(V\)- and profile-supported stationary points may lie
above \(H_j\) when \(C>9/4\), but they are not physical contributions:
the exact factor \(\mathbf1_{h\le H_j}\) removes them.  Every surviving
point already satisfies \(h\le H_j\).  Choose a fixed rescaled cutoff
which rises below \(\gamma H_j\), equals one from \(\gamma H_j\) through
\(H_j\), and, if desired, tapers only after \(H_j\), where the exact
indicator is zero.  Its normalized sampled variation is \(O(1)\).

This also identifies the error in the superseded strict-margin audit.
The ratio
\[
 {h\over H_j}={\sqrt z\over2}{d\over D_j}
 {D_j\over RH_j}                                          \tag{12}
\]
can indeed approach or exceed one for interior profiles when
\(z\ge9/4\).  That fact refutes a strict auxiliary upper cutoff, but it
does not refute terminal localization: the exact physical endpoint,
not \(\eta_j\), owns the upper boundary.

If \(H_j=0\), the physical height sum is empty.  If
\(1\le H_j<H_0\), then
\[
 RH_j\le D_j<R(H_j+1)\ll_V R.                              \tag{13}
\]
There are \(O_V(1)\) heights, the profile contains \(O(D_j)\) integer
denominators, and all original coefficients in (60.4) are bounded.
Direct absolute summation gives
\[
 \mathcal B_{j,V}\ll_V D_j\ll_V R.                        \tag{14}
\]
This uses the original smooth radial factor, so it incurs no Mellin
derivative loss.  Full endpoint values and half-weights remain as given.

### Mellin normalization, endpoint BV, and integration

With
\[
 \widehat V(t)=\int_0^\infty V(z)z^{-it}{dz\over z},
\]
Fourier inversion after \(z=e^x\) gives (2), including \(1/(2\pi)\)
exactly once.  Compact smooth support implies, for every \(A,m\ge0\),
\[
 |\widehat V(t)|\ll_{A,V}(1+|t|)^{-A},
 \qquad
 \int_{\mathbb R}|\widehat V(t)|(1+|t|)^m\,dt<\infty.     \tag{15}
\]

On the nonzero support of (3), \(h\asymp_V H_j\).  For
\(a_t(x)=x^{-1+2it}\),
\[
 |a_t(x)|=x^{-1},\qquad
 |a_t'(x)|\le {1+2|t|\over x^2}.                           \tag{16}
\]
The normalized Vaaler factor is bounded and has derivative
\(O(H_j^{-1})\) as a function of \(x\).  Combining (16), the fixed
sampled variation of \(\eta_j\), and the product variation inequality
over \(O(H_j)\) samples gives \(O((1+|t|)/H_j)\) before the upper
endpoint.  Zero extension adds exactly
\[
 |U_{j,t}(H_j)|
 \le {\|\Phi\|_\infty\over H_j}=O(H_j^{-1})               \tag{17}
\]
at the jump from \(H_j\) to \(H_j+1\).  This proves (4) without
requiring \(U_{j,t}(H_j)=0\).  A prescribed equality star changes one
sample by \(O(H_j^{-1})\); a full hard jump costs its actual jump and is
not converted to a half-weight.

The denominator mode has modulus one and, for every fixed derivative
order \(m\),
\[
 {d^m\over dd^m}d^{-2it}=d^{-m}P_m(t)d^{-2it},             \tag{18}
\]
where \(P_m\) has degree \(m\).  Hence every derivative loss required
by the accepted transform is absorbed by (15).  Applying the terminal
theorem mode by mode and integrating proves (5).  For large heights,
\[
 1+{D_j\over H_j}\ll R;                                   \tag{19}
\]
for bounded heights use (14).  There are \(O(\log X)\) active dyadic
profiles, so the full physical sum is
\(O_{\varepsilon,V}(RX^\varepsilon)\), with this logarithm absorbed
only once.

### Stationary readback and target

Substitution of \(d_*=2\sqrt{hX/q}\) proves (6) directly.  In particular,
the factor \((4X/Y)^{it}\) reconstructs \((n/Y)^{it}\); it neither
duplicates the external \(R\) nor alters the radial weight.

The statement-only packet authorizes the accepted Round-14
interior/top transform interface rather than reproducing its formulas.
Using that interface gives (7).  The one-sided top profile, its
cotangent boundary, the hard value \(d=\lfloor\sqrt X\rfloor\), the
exact height indicator and floor, profile seams, stationary
half-weights, angular equality stars, and the independent radial star
remain inside the accepted transform and error ledger.  None is replaced
by the smooth radial cutoff or by another star; coincident factors retain
their separate owners.

Combining the physical bound with (7), and dividing by its single
external factor \(R\), proves (8).  This bounds one fixed real linear
functional of \(\mathcal G_V\), not its orthogonal projection and not
its complex modulus.

## 4. First doubtful or unproved step

No actual mismatch remains after retaining the exact upper height
indicator.  The earlier proposed restriction \(C<9/4\) was a false
requirement and is retracted: it arose from assigning the upper endpoint
to \(\eta_j\) instead of to \(\mathbf1_{h\le H_j}\).  Equations
(11), (16), and (17) prove that a positive lower radial cutoff plus the
allowed \(O(H_j^{-1})\) endpoint jump is sufficient for every fixed
\(0<c<C<16\).

The first step not independently rederived is the exact accepted
transform readback (7), especially the coefficient \(-4/\pi\), phase
\(e(1/8)\), frequency-sign pairing, cotangent/hard-top term, starred
endpoint constants, and global error normalization.  Those formulas are
deliberately outside the permitted statement-only packet and enter here
through its declared Round-14 interior/top interface.  Equation (6)
checks the new Mellin mode against that interface, and the check finds no
normalization or endpoint mismatch.  This is an isolation/provenance
limit, not evidence that the transform statement is absent or false.

A standalone proof of (8) from this report alone would have to reproduce
that accepted transform and its termwise error estimates.  Within the
frozen campaign interface it is an allowed dependency, so no additional
mathematical defect blocks the real-projection target.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| terminal_support | **Pass; prior objection retracted.** The positive lower radial cutoff gives (11).  The exact factor \(\mathbf1_{h\le H_j}\) owns the upper edge, so no \(\Gamma<1\) or \(C<9/4\) condition is needed. |
| upper_endpoint_jump | **Pass.** Zero extension contributes only (17), namely \(O(H_j^{-1})\), which is admitted by the terminal sampled-BV theorem. |
| Mellin_normalization | **Pass.** Equations (2), (6), and (15) verify \(1/(2\pi)\), the powers \(h^{2it}d^{-2it}\), and reconstruction of \(V(n/Y)\). |
| frequency_BV | **Pass.** Equations (3), (16), and (17) prove \((1+|t|)/H_j\), including the exact terminal jump and single-sample equality changes. |
| denominator_mode_and_t | **Pass.** Equation (18) produces only polynomial \(t\)-loss at every fixed derivative order, and all such moments are finite by (15). |
| small_height | **Pass.** \(H_j=0\) is empty; (13)--(14) give the required \(O_V(R)\) direct bound for bounded positive heights. |
| terminal_capacity | **Pass through the accepted theorem.** Equations (5), (19), and the single active-scale count give \(O_{\varepsilon,V}(RX^\varepsilon)\). |
| Bprocess_constant | **Accepted-interface compatible; not rederived blind.** The coefficient \(-4/\pi\), phase, and two-sign pairing are supplied by the authorized Round-14 interface.  The independently checked mode identity (6) shows no mismatch. |
| hard_top_floors_stars | **Pass at the stated interface.** Every owner is retained separately; the exact height endpoint is not smoothed away, no hard value is converted to a half-weight, and coincident factors are not conflated. |
| error_sum | **Accepted-interface compatible; not rederived blind.** Its required and supplied scale is \(RX^\varepsilon\); Mellin differentiation adds only integrable polynomial losses.  No new error-scale mismatch appears. |
| GAR_implication_scope | **Pass.** Equation (7) yields exactly \(\operatorname {Re}\{e(1/8)\mathcal G_V\}\ll X^\varepsilon\).  No modulus inference is made. |
| downstream_scope | **Pass.** No lower radial range, alpha transition, full GAR, M9-M1, M9, or final-exponent conclusion is asserted. |

## 6. Dependencies, exact artifacts, and isolation ledger

Dependencies used:

1. The authorized packet's definitions of \(\mathcal G_V\),
   \(\mathcal B_{j,V}\), \(D_j\), \(H_j\), the stationary relation, and
   the accepted frequency-first terminal-theorem interface.
2. The packet-declared accepted Round-14 interior and one-sided top
   transforms, used only through (7), including their hard/star/error
   ownership.
3. The stated fixed profile support ratios and normalized smoothness/BV
   conventions.
4. Mellin/Fourier inversion for \(C_c^\infty((0,\infty))\), elementary
   sampled variation, and floor inequalities.

Isolation ledger:

- Read only
  `rounds/codex-managed/m9-m1-critical-radial-terminal-return/briefs/blind_critical_terminal_rederivation.md`
  and the authorized
  `rounds/codex-managed/m9-m1-critical-radial-terminal-return/derivation_packet.md`.
- Re-read that same packet after the conductor's support and target
  corrections.  Its final frozen range is every fixed
  \(0<c<C<16\), and its target is only the fixed real projection (8).
- Used the conductor-supplied exact profile ratios
  \(d/D_j\in[1/2,4/3]\) and \(d/Y\in[1/2,1]\).  No other Round-60
  artifact was opened.
- Did not read the proof graph, proof draft, prior reports or syntheses,
  validation matrices, or any other Round-60 output.
- Used no web source, external paper, numerical experiment, Python, or
  Mathematica.
- Wrote only this assigned report and made no shared proof-state edit.

## 7. Recommended state effect

**Promote the Round-60 real-projection terminal-return claim through the
packet-declared accepted transform interface.**  Promote the full fixed
smooth sector \(0<c<C<16\), the lower-terminal support lemma, retention
of the exact upper height indicator, its \(O(H_j^{-1})\) endpoint jump,
the exact Mellin normalization, sampled-BV bound, bounded-height estimate,
polynomial \(t\)-loss ledger, and
\(O_{\varepsilon,V}(RX^\varepsilon)\) terminal capacity.  Explicitly
reject the superseded claim that a strict upper margin or \(C<9/4\) is
needed.

Record (7) as an accepted Round-14 dependency rather than as a transform
identity newly proved by this blind report; its Mellin and endpoint
compatibility have passed and no actual mismatch was found.  Promote only
\(\operatorname {Re}\{e(1/8)\mathcal G_V\}\ll_{\varepsilon,V}X^\varepsilon\).
Do not promote a modulus bound or any downstream GAR/M9 conclusion.

### Post-isolation authorized-interface addendum (final modulus verdict)

This addendum records a later, explicitly authorized interface that was
not available to the blind audit above.  The preceding no-modulus verdict
is therefore preserved as the correct conclusion from the original
paired-real interface, but it is superseded for the final Round-60 verdict
by the following positive-frequency identity.  No other Round-60 report
was inspected.

The newly authorized interior/top denominator transform is
\[
 B_{j,h}=E_{j,h}+{e(1/8)\over i}(hX)^{1/4}
 \sum_{q\ \operatorname{odd}}^{*}\chi_4(q)q^{-3/4}
 w_j\!\left(2\sqrt{hX/q}\right)e(\sqrt{Xhq})+R_{j,h},      \tag{A1}
\]
with the accepted weighted total of the \(E_{j,h}\)- and
\(R_{j,h}\)-families equal to \(O_V(\log^2X)\), together with the
accepted complex terminal bound for the localized positive antecedent.
Apply (A1) with the localized denominator amplitude and weight it by
\[
 \mathbf1_{h\le H_j}\eta_j(h)
 {\Phi(h/(H_j+1))\over h}.
\]
Here the radial factor is not inserted by naively multiplying (A1) by a
\(q\)-dependent scalar.  One first uses the already verified Mellin
separation (2), applies the accepted denominator transform to each mode
\(d^{-2it}\), and then integrates in \(t\); the authorized weighted
error ledger and (15), (18) justify that integration.  At the stationary
point \(d_*=2\sqrt{hX/q}\), this evaluates the radial amplitude as
follows:
\[
 V\!\left({4Xh^2\over d_*^2Y}\right)=V(hq/Y),             \tag{A2}
\]
and the main coefficient becomes exactly
\[
 {\Phi(h/(H_j+1))\over h}(hX)^{1/4}q^{-3/4}
 =R\,\Phi(h/(H_j+1))(hq)^{-3/4}.                          \tag{A3}
\]
There is no extra factor of two, \(\pi\), or \(i\) in (A3).

On every nonzero stationary term \(\eta_j(h)=1\).  With \(n=hq\),
the starred profile sum in (A1) therefore recombines as
\[
 \begin{aligned}
 &\sum_{j,h}\sum_{q\ \operatorname{odd}}^{*}
 \mathbf1_{h\le H_j}\eta_j(h)
 \Phi\!\left({h\over H_j+1}\right)
 V(hq/Y)\chi_4(q)(hq)^{-3/4}
 w_j\!\left(2\sqrt{hX/q}\right)
 e(\sqrt{Xhq}) \\
 &\hspace{18mm}=
 \sum_{n\le16Y}V(n/Y)\mathcal C_X^*(n)n^{-3/4}
 e(\sqrt{Xn})
 =\mathcal G_V(X),                                        \tag{A4}
 \end{aligned}
\]
Equivalently, (A4) is obtained by the bijection
\((h,q)\leftrightarrow(n,h)\), \(n=hq\), with \(q\) odd.
The exact height indicator, profile stars, and hard top are precisely the
owners already present in \(\Omega_X^*\): the star on the \(q\)-sum in
(A1) transfers to the single starred profile evaluation, rather than
creating a second half-weight.  The lower cutoff disappears because it
is one on this support.  Since \(\operatorname {supp}V\subset
(0,16)\), no supported term lies beyond \(n=16Y\).

Consequently the authorized positive-frequency identity gives the
complex equality
\[
 \boxed{\sum_j\mathcal B_{j,V}
 ={e(1/8)\over i}R\mathcal G_V(X)+O_V(\log^2X).}           \tag{A5}
\]
The accepted terminal estimate is a complex modulus estimate,
\[
 \left|\sum_j\mathcal B_{j,V}\right|
 \ll_{\varepsilon,V}RX^\varepsilon.                       \tag{A6}
\]
Because \(|e(1/8)/i|=1\), (A5)--(A6) imply
\[
 |\mathcal G_V(X)|
 \ll_{\varepsilon,V}X^\varepsilon+R^{-1}\log^2X
 \ll_{\varepsilon,V}X^\varepsilon.                       \tag{A7}
\]

**Final exact verdict: yes.**  For real \(V\), the newly authorized
unpaired positive-frequency identity upgrades the result to the modulus
bound (A7).  Pairing with the negative frequency is unnecessary for this
conclusion.  The original blind answer “real projection only” remains an
accurate provenance statement about the weaker interface then available,
not a mathematical obstruction once (A1) and its weighted error ledger
are authorized.  The final recommended state effect is therefore to
promote (A5) and \(|\mathcal G_V|\ll_{\varepsilon,V}X^\varepsilon\),
while retaining all previously stated downstream exclusions.
