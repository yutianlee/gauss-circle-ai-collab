# Round 121 statement-only blind rederivation: the lower height kernel

## 1. Result: a strict seam subpackage and an exact no-go survivor

Let

\[
 V_h(d):=V_{\rm low}\!\left({4R^2h^2\over d^2}\right),\qquad
 C_X(h,d):=A_X(h,d)V_h(d).
\]

The one-count identity and the mod-four pairing in the packet are exact.  If
\(q=4m+1\), \(p=q+2\), and

\[
 \Delta_q={2X\over q(q+2)},
\]

then the exact pair has the decomposition

\[
 F_X(q)-F_X(p)=E_q+P_q,                                      \tag{1.1}
\]
\[
 E_q=\sum_{h\geq1}{C_X(h,q)-C_X(h,p)\over h}e(hX/q),          \tag{1.2}
\]
\[
 P_q=\sum_{h\geq1}{C_X(h,p)\over h}e(hX/p)
                 \{e(h\Delta_q)-1\}.                         \tag{1.3}
\]

No absolute value in height was used in (1.1)--(1.3).  The amplitude seam
\(\mathcal E_X:=\sum_{q\equiv1(4)}E_q\) satisfies the exact profile-BV
bound

\[
 |\mathcal E_X|\leq \Lambda_X,                               \tag{1.4}
\]
where

\[
 \begin{split}
 \Lambda_X:=\sum_{j:H_j\geq1}
 &\left(\|V_{\rm low}\|_\infty\,
     \sum_{m\geq0}|w_j(4m+1)-w_j(4m+3)|
     +\|w_j\|_\infty\int_0^\infty|V_{\rm low}'(s)|\,ds\right)\\
 &\hspace{35mm}\times
 \sum_{1\leq h\leq H_j}{|\Phi(h/(H_j+1))|\over h}.
                                                               \tag{1.5}
 \end{split}
\]

Thus the seam is a strict target-safe subpackage whenever the exact profiles
have the usual scale-uniform step-two BV and sup-norm bounds and \(\Phi\) is
bounded on \([0,1]\): under those explicit hypotheses,

\[
 \Lambda_X\ll_{\Phi,V} \sum_{j:H_j\geq1}\log(2H_j)
 \ll_{\Phi,V}(1+\log X)^2=o(RX^\varepsilon).                  \tag{1.6}
\]

The permitted packet does not state the required quantitative BV bounds for
the actual \(w_j\).  Consequently (1.4)--(1.5), rather than the last
specialization in (1.6), is the unconditional statement-only conclusion
about the seam.

After this seam, the smallest exact survivor found here is

\[
 \boxed{\mathcal P_X:=\sum_{q\equiv1(4)}P_q}.                 \tag{1.7}
\]

It has an exact joint-height transport form.  Choose an integer \(n_q\) so
that \(\rho_q:=\Delta_q-n_q\in[-1/2,1/2]\), with either fixed convention at
a half tie, and put

\[
 \mathcal H_d(u):=\sum_{h\geq1}C_X(h,d)e(hu).
\]

Then

\[
 \boxed{
 \mathcal P_X=2\pi i\sum_{q\equiv1(4)}
       \int_0^{\rho_q}\mathcal H_{q+2}(X/(q+2)+t)\,dt .}
                                                               \tag{1.8}
\]

This is valid for the whole lower range and is not a small-angle
approximation.  Pairing by itself does not bound (1.8) by
\(RX^\varepsilon\).  In particular, any route which replaces the outer
signed sum by a coefficient-uniform per-pair norm is quantitatively false:
the first-height hostile control in Section 3.6 has pair norm
\(\gg Y\), while \(R=Y^{1/2}\).  Resonant pairs can be bounded absolutely in
the upper scales, but the nonresonant pairs still have capacity \(\asymp D\)
on a block of length \(D\).  A proof of (121.B4) therefore still needs a
genuinely signed cross-pair estimate for (1.8), of square-root strength on
the top block.  No such estimate follows from the statement-only data.

Accordingly, this report proves the exact reduction and a strict conditional
amplitude-seam package, but it does **not** prove (121.B4).

## 2. Exact statement and hypotheses

Throughout, \(e(t)=e^{2\pi i t}\),

\[
 R=X^{1/4},\quad Y=\sqrt X,\quad y=\lfloor Y\rfloor,
 \quad D_j=2^{-j}y,\quad H_j=\lfloor D_j/R\rfloor.
\]

Only indices with a nonempty exact profile and \(H_j\geq1\) occur.  Every
\(w_j\) is zero-extended to all positive integers.  The same convention is
used for \(C_X(h,d)\) when a height or denominator is outside its exact
support.  With

\[
 a_j(h)={\bf1}_{1\leq h\leq H_j}
       \Phi\!\left({h\over H_j+1}\right),
 \qquad A_X(h,d)=\sum_j a_j(h)w_j(d),                          \tag{2.1}
\]

the following are packet-level, unconditional identities:

1. The literal positive-frequency reciprocal antecedent is (121.B2).
2. Its profile-first form is
   \[
   \mathcal B_{\rm low}^+
   =\sum_{h,d\geq1}{\chi_4(d)\over h}C_X(h,d)e(hX/d).          \tag{2.2}
   \]
3. If
   \[
   F_X(d)=\sum_{h\geq1}{C_X(h,d)\over h}e(hX/d),               \tag{2.3}
   \]
   then
   \[
   \mathcal B_{\rm low}^+
   =\sum_{m\geq0}\{F_X(4m+1)-F_X(4m+3)\}.                    \tag{2.4}
   \]
4. Equations (1.1)--(1.3) and (1.8) hold exactly.

The precise support information available in the packet is as follows.

* \(h\leq H_j\) is equivalent, without an endpoint loss, to
  \(Rh\leq D_j\).  In particular, every global height obeys
  \(h\leq H_0=\lfloor y/R\rfloor\leq\lfloor R\rfloor\).
* There are at most
  \(1+\lfloor\log_2(y/R)\rfloor=O(1+\log X)\) active height
  indices.
* Since \(V_{\rm low}(s)=0\) for \(s\geq2s_0\), a nonzero radial
  term necessarily has
  \[
  d>\sqrt{2/s_0}\,Rh.                                        \tag{2.5}
  \]
* The one-sided hard top, the smooth profile endpoints and stars, and every
  exact denominator endpoint remain inside the literal \(w_j(d)\).  No
  endpoint was moved to \(D_j\), and no smooth profile was replaced by a
  hard interval.  A pair meeting an endpoint is handled by zero extension.
* The inactive bottom denominator range is not in (2.2); it remains the
  separately bounded term specified by the packet.
* The hard cotangent boundary, transform errors, stationary stars, and
  outer product half tie are not reabsorbed into \(C_X\).  They remain the
  separately accounted terms stated in the packet.

The quantitative specialization (1.6) uses the additional, explicit
hypotheses

\[
 \sup_j\|w_j\|_\infty\ll1,qquad
 \sup_j\sum_{m\geq0}|w_j(4m+1)-w_j(4m+3)|\ll1,                \tag{2.6}
\]

and \(\sup_{0\leq u\leq1}|\Phi(u)|<\infty\).  A one-sided hard
indicator has bounded variation in (2.6), and a standard scale-
\(D_j\) smooth profile does too, but the exact definitions needed to verify
(2.6) are not present in the permitted packet.  No estimate below silently
assumes (2.6) when claiming an unconditional conclusion.

Because all coefficients in (2.2) other than the exponential are real, the
negative-frequency reciprocal antecedent is the complex conjugate of
\(\mathcal B_{\rm low}^+\).  This observation does not absorb any of the
separate hard or starred boundary terms.

## 3. Proof and derivation

### 3.1 Literal antecedent and the global profile-height kernel

Insert (2.1) into (121.B2) and zero-extend each height sum:

\[
 \begin{split}
 \mathcal B_{\rm low}^+
 &=\sum_j\sum_{h\geq1}{a_j(h)\over h}
   \sum_{d\geq1}\chi_4(d)w_j(d)V_h(d)e(hX/d)\\
 &=\sum_{h,d\geq1}{\chi_4(d)\over h}
   \left(\sum_j a_j(h)w_j(d)\right)V_h(d)e(hX/d).
 \end{split}                                                   \tag{3.1}
\]

All active profile sums and height sums are finite, so this rearrangement
does not need a convergence theorem and, importantly, no norm has yet been
applied.  Equation (3.1) is (2.2), with every floor retained in \(a_j\).
The equivalence \(h\leq\lfloor D_j/R\rfloor\iff Rh\leq D_j\)
proves the stated height support.  The radial support (2.5) follows by
contraposition from the hard support of \(V_{\rm low}\).

There is no external factor of \(R\) in (3.1).  The required normalization
is literally \(|\mathcal B_{\rm low}^+|\ll RX^\varepsilon\), as in
(121.B4); multiplying or dividing (3.1) by an additional \(R\) would test a
different claim.

### 3.2 Exact mod-four pairing

The character vanishes on even denominators, equals \(+1\) on
\(4m+1\), and equals \(-1\) on \(4m+3\).  Therefore (2.2) and (2.3) give

\[
 \sum_{d\geq1}\chi_4(d)F_X(d)
 =\sum_{m\geq0}\{F_X(4m+1)-F_X(4m+3)\}.                      \tag{3.2}
\]

Zero extension is essential here: if exactly one member of a pair lies in a
hard or smooth profile support, (3.2) retains that member rather than
discarding the boundary pair.  Thus (3.2) also covers the first pair
\((1,3)\), the exact hard top sample, profile stars, and all terminal pairs.

### 3.3 Amplitude and phase are separated without a height norm

For \(q=4m+1\) and \(p=q+2\),

\[
 {X\over q}-{X\over p}={2X\over q(q+2)}=\Delta_q.             \tag{3.3}
\]

For every height separately,

\[
 C_X(h,q)e(hX/q)-C_X(h,p)e(hX/p)
 =[C_X(h,q)-C_X(h,p)]e(hX/q)
 +C_X(h,p)e(hX/p)\{e(h\Delta_q)-1\}.                          \tag{3.4}
\]

Summing (3.4) with weight \(1/h\) proves (1.1)--(1.3).  This is an
identity, not the inequality obtained by summing the absolute values of its
height terms.

### 3.4 The amplitude-seam BV estimate

For fixed \(j,h,q\), the product difference is

\[
 \begin{split}
 w_j(q)V_h(q)-w_j(q+2)V_h(q+2)
 &=[w_j(q)-w_j(q+2)]V_h(q)\\
 &\quad+w_j(q+2)[V_h(q)-V_h(q+2)].                            \tag{3.5}
 \end{split}
\]

The intervals \([4m+1,4m+3]\) are disjoint.  For
\(g_h(t)=V_{\rm low}(4R^2h^2/t^2)\), the fundamental theorem of calculus
and the substitution \(s=4R^2h^2/t^2\) give

\[
 \begin{split}
 \sum_{m\geq0}|V_h(4m+1)-V_h(4m+3)|
 &\leq\int_0^\infty |g_h'(t)|\,dt\\
 &=\int_0^\infty|V_{\rm low}'(s)|\,ds.                       \tag{3.6}
 \end{split}
\]

The bound is independent of \(h\), including when the radial transition
meets a denominator endpoint.  Sum (3.5), then sum the exact coefficients
\(|a_j(h)|/h\).  The triangle inequality is being used only for the
amplitude error, after the exact height kernel has been formed.  This proves
(1.4)--(1.5).

Under (2.6),

\[
 \sum_{1\leq h\leq H_j}{|\Phi(h/(H_j+1))|\over h}
 \ll_\Phi\log(2H_j).                                         \tag{3.7}
\]

Since the number of active \(j\)'s and every \(\log(2H_j)\) are
\(O(1+\log X)\), (3.7) proves (1.6).  Notice that this is much smaller
than the literal budget \(RX^\varepsilon\); no hidden external
normalization was spent.

### 3.5 Exact joint phase-increment kernel

Because \(h\) is integral, \(e(h\Delta_q)=e(h\rho_q)\).  For either
orientation of the signed interval,

\[
 {e(h\rho_q)-1\over h}=2\pi i\int_0^{\rho_q}e(ht)\,dt.        \tag{3.8}
\]

At a half tie, \(\rho_q=1/2\) and \(-1/2\) give the same left side for
every integral height, so a fixed tie convention preserves exactness.
Insert (3.8) into (1.3) and interchange the finite height sum and integral.
This proves (1.8).

Equation (1.8) retains the complete oscillation in height.  It never uses
\(e(h\rho)-1\sim2\pi ih\rho\); hence it covers both the small-increment
and large-increment portions of the full lower range.

### 3.6 Resonant capacity and the hostile local-norm control

The following elementary count locates the capacity of the increment
split.  For \(1\leq D\leq Y\), \(0<\eta\leq1/2\), let

\[
 \mathcal R(D,\eta)=
 \{q\equiv1\pmod4:D/2\leq q\leq D,
       \|2X/(q(q+2))\|\leq\eta\}.
\]

Then

\[
 \#\mathcal R(D,\eta)
 \ll \eta D+{X\over D^2}+1.                                 \tag{3.9}
\]

Indeed, \(f(t)=2X/(t(t+2))\) is monotone and

\[
 |f'(t)|={4X(t+1)\over t^2(t+2)^2}\asymp {X\over D^3}
 \quad(D/2\leq t\leq D).                                    \tag{3.10}
\]

Its range meets \(O(X/D^2+1)\) integers.  The inverse image of the
\(2\eta\)-neighborhood of each such integer has length
\(O(\eta D^3/X)\).  Counting the step-four lattice points in these
intervals adds at most one point per component, which gives (3.9).

On a scale with height \(H\asymp D/R\), define resonance by
\(|\rho_q|\leq1/H\).  If \(|C_X(h,q+2)|\leq C_0\), then the exact
inequality

\[
 |P_q|\leq2\pi |\rho_q|\sum_{h\leq H}|C_X(h,q+2)|\leq2\pi C_0            \tag{3.11}
\]

holds on this resonant set.  Equations (3.9)--(3.11) therefore give

\[
 \sum_{q\in\mathcal R(D,1/H)}|P_q|
 \ll C_0\left(R+{X\over D^2}+1\right).                       \tag{3.12}
\]

The three diagnostic scales are revealing:

\[
\begin{array}{c|c|c|c}
D&H\asymp D/R&X/D^2&\text{conclusion from (3.12)}\\ \hline
X^{1/2}&R&1&O(R)\ \text{is target-safe},\\
X^{3/8}&X^{1/8}&R&O(R)\ \text{is target-safe},\\
X^{1/4}=R&1&Y&\text{the count is trivial, but the whole block has only }O(R)
\text{ pairs}.
\end{array}                                                     \tag{3.13}
\]

For \(R<D<X^{3/8}\), the crossing term \(X/D^2\) in (3.12) can exceed
the full budget.  For \(D\geq X^{3/8}\), only \(O(R)\) pairs are
increment-resonant, while a block with \(D\gg R\) has \(\asymp D\)
nonresonant pairs.  On those remaining pairs the packet gives only, for
bounded amplitudes,

\[
 |P_q|\leq2\sum_{h\leq H}{|C_X(h,q+2)|\over h}
 \ll C_0\log(2H),                                             \tag{3.14}
\]

whose absolute sum is \(O(D\log X)\), not \(O(RX^\varepsilon)\).

This is not merely a defect of (3.14).  It is impossible to replace the
outer sum in (1.8) by a coefficient-uniform local pair norm.  Take
\(X=N^2\) with integer \(N\to\infty\), so \(Y=N\) and \(R=N^{1/2}\),
and use the first-height control amplitude

\[
 C(1,d)=1\quad(N/2\leq d\leq N),\qquad C(h,d)=0\quad(h>1),     \tag{3.15}
\]

with zero extension.  This control is constant away from two endpoints and
has uniformly bounded amplitude variation.  Also its radial cutoff is
literally one for all sufficiently large \(N\), because
\(4R^2/d^2\ll1/N\) on this interval.  For interior pairs,

\[
 |P_q|=|e(2N^2/(q(q+2)))-1|.                                 \tag{3.16}
\]

On \([N/2,N]\), the function in (3.16) is monotone, has derivative
comparable to \(1/N\), and crosses only \(O(1)\) integers.  For a fixed,
sufficiently small \(\eta_0>0\), the union of the inverse images of the
\(\eta_0\)-neighborhoods of those integers has length at most a fixed
proper fraction of \(N\).  It has only \(O(1)\) components.  Hence a
positive proportion of the integers \(q\equiv1\pmod4\) satisfy
\(\|2N^2/(q(q+2))\|\geq\eta_0\), and on them
\(|P_q|\geq2\sin(\pi\eta_0)\).  Consequently

\[
 \sum_{N/2\leq q\leq N-2\atop q\equiv1(4)}|P_q|\gg N=Y.     \tag{3.17}
\]

For every fixed \(\varepsilon<1/4\), this exceeds
\(RX^\varepsilon=N^{1/2+2\varepsilon}\).  This is a control-model
counterexample to a coefficient-uniform local-norm lemma, not a
counterexample to the fixed packet coefficient \(A_X\).  It proves that a
valid estimate for the actual kernel must exploit the complex orientations
between distinct pairs.  Indeed, by choosing real adversarial pair signs
after projecting all \(P_q\)'s onto a suitable fixed direction, one obtains
a signed sum \(\gg\sum_q|P_q|\); thus even real adversarial signs destroy
the needed saving.

The unsigned analogue fails the complementary test as well.  In the same
first-height model its pair is

\[
 e(N^2/q)+e(N^2/(q+2))
 =e(N^2/(q+2))\{e(2N^2/(q(q+2)))+1\}.                         \tag{3.18}
\]

On a fixed short proportional interval \([(1-c)N,N-2]\), with \(c>0\)
small enough, the increment is in a fixed small neighborhood of the integer
\(2\).  Hence the modulus in (3.18) is bounded below on \(\gg N\) pairs,
and its local pair norm is again \(\gg N\).  Thus increment resonance,
which suppresses the true-character difference, reinforces the unsigned
sum.

A square-root bound for the signed outer sum on every dyadic block would be
target-safe, since \(\sqrt D\leq\sqrt Y=R\).  Establishing such a bound
uniformly for the floor-perturbed height polynomial in (1.8) is precisely
the missing analytic step; pairing and (3.9) do not establish it.

## 4. First doubtful or unproved step

The first packet-level missing premise is the quantitative profile estimate
(2.6).  The words “one-sided hard top profile” and “smooth profiles” are
consistent with (2.6), and (1.4) shows exactly what must be checked, but the
permitted files do not give the formulas, derivative bounds, overlap
constants, starred endpoint conventions, or a lower-profile support table.
It would be nonblind and logically unjustified to certify (2.6) from names
alone.

If (2.6) is supplied or has already been verified elsewhere, the first
analytic gap is the estimate

\[
 \left|\sum_{q\equiv1(4)}
       \int_0^{\rho_q}\mathcal H_{q+2}(X/(q+2)+t)\,dt\right|
 \ll_{\varepsilon,s_0}RX^\varepsilon.                         \tag{4.1}
\]

Neither termwise height absolute values, an absolute sum over pairs,
resonant counting, nor a coefficient-insensitive norm proves (4.1).
Equation (3.17) rules out the latter class of arguments.  The permitted
packet supplies no cross-pair large-sieve, reciprocal-phase transform, or
other signed theorem that would prove (4.1).

The blind statement names the earlier one-sided-divisor, Appell,
product-wavelet, unmatched-crossing, and conductor barriers but does not
state their kernels.  Therefore no rigorous comparison or strict
containment claim is possible under statement-only access.  Algebraically,
(1.8) is smaller than the starting antecedent because the amplitude seam is
removed.  It still explicitly contains derivative-integer resonances and
oriented arcs which may cross an integer phase, so this report does not
claim that it is genuinely smaller than the named historical returns.

## 5. Required control tests and outcomes

| Control | Exact input and expected invariant/failure | Observed outcome | Implication |
|---|---|---|---|
| `literal_lower_reciprocal_antecedent` | (121.B2), including \(1/h\), \(H_j\), \(H_j+1\), \(\chi_4(d)\), the physical \(V_{\rm low}\), and \(e(hX/d)\). No factor may be dropped. | Direct finite rearrangement gives (3.1) exactly. | Passed as an identity; it does not prove the target estimate. |
| `external_R_normalization` | The required claim is literally \(\mathcal B_{\rm low}^+\ll RX^\varepsilon\). Expected failure is inserting an extra transform factor \(R\). | No external \(R\) was inserted. The seam budget in (1.6), when its hypotheses hold, is \(O(\log^2X)\) against the full \(RX^\varepsilon\) budget. | Passed normalization. |
| `global_profile_height_kernel` | Sum all exact \(j\)-profiles into \(A_X(h,d)\) before a norm. | (3.1) forms \(A_X\) first; all floors remain inside \(a_j(h)\). | Passed algebraically. |
| `mod_four_pairing_identity` | Zero-extend both members of every \((4m+1,4m+3)\) pair, including boundary pairs. | Equation (3.2) is exact and includes unmatched hard/profile endpoints. | Passed. |
| `amplitude_seam_BV` | Separate amplitude from phase and test the seam at the literal budget. | The exact estimate is (1.4)--(1.5). It is \(O(\log^2X)\) under (2.6), but (2.6) cannot be audited from the permitted packet. | Strict target-safe conditional package; unconditional quantitative certification is withheld. |
| `phase_increment_joint_height_kernel` | Retain \(\Delta_q=2X/(q(q+2))\) and do not take a heightwise absolute value. | Equations (1.3) and (1.8) are exact, including large increments and half ties. | Passed as a derivation; (1.8) is the smallest exact analytic survivor. |
| `resonant_nonresonant_capacity` | Use \(|\rho_q|\leq1/H\) on a scale \(H\asymp D/R\) and test \(D=R,X^{3/8},Y\). | (3.9)--(3.13) make the resonant upper package target-safe. The lower-middle crossing term can exceed \(R\), and the nonresonant absolute capacity is \(D\log X\). | Failed as a full-range proof; signed cross-pair cancellation is still required. |
| `floor_star_hard_bottom_boundaries` | Keep \(y=\lfloor\sqrt X\rfloor\), \(H_j=\lfloor D_j/R\rfloor\), \(H_j+1\), exact profile stars, hard top samples, product half tie, and the separately owned inactive bottom. | Floors are literal in (2.1); profiles are zero-extended; boundary pairs are retained; the inactive bottom and other separately accounted terms were not folded into the kernel. Exact star formulas are absent, so their BV constants were not invented. | Passed the algebraic boundary test; quantitative profile audit remains unavailable. |
| `unsigned_adversarial_control` | Replace \(\chi_4\) by \(|\chi_4|\), and separately allow same-magnitude adversarial pair signs. Expected failure is loss of the exact alternating cancellation. | Unsigned pairing gives \(F(q)+F(q+2)\), replacing \(e(h\Delta_q)-1\) by a plus interaction; at increment resonance it doubles rather than vanishes. The first-height model has local mass \(\gg Y\), and real adversarial pair signs align a fixed projection to recover that mass. | The needed estimate must use the exact true-character orientations across different pairs; it cannot be coefficient-insensitive. |
| `full_lower_range_scope` | No small-angle replacement above its threshold; retain the physical cutoff. | The signed-fractional-part integral (1.8) is exact for every \(|\rho_q|\leq1/2\), and (2.5) is the only radial support reduction used. | Passed for the derivation; the full-range estimate remains open. |
| `one_count_downstream_scope` | The owner is only the lower reciprocal one-count antecedent and its conjugate. | No claim is made for the global angular-radial estimate, blockwise M9-M1, M9, or a new circle exponent. Hard/transform/star/bottom terms remain separate. | Passed scope control. |

For the hostile control (3.15), the expected invariant was that good amplitude
BV alone should not create character cancellation.  The observed
\(\gg Y\) pair norm confirms that invariant.  It is a falsification of a
local-norm mechanism, not numerical evidence and not a falsification of the
fixed coefficient theorem.

## 6. Dependencies and exact artifacts used

This report used only the following statement-only artifacts:

1. `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/briefs/blind_lower_height_kernel_rederivation.md`;
2. `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/blind_statement.md`;
3. `problems/gauss_circle.md`;
4. `state/control_models.md`.

No strategy file, proof graph, best proof draft, Round-61--Round-121
nonblind artifact, sibling report, web source, or numerical computation was
used.  All controls above are algebraic or elementary analytic derivations.
The exact formulas for \(w_j\), their starred endpoints, and the named
historical barrier kernels were deliberately not inferred from excluded
material.

## 7. Recommended state effect: no change

Do not promote (121.B4) and do not promote a claim that mod-four pairing is
by itself target-safe.  Retain (1.1)--(1.5) and the exact transport survivor
(1.8) as candidate evidence.  A future state change requires both:

1. an allowed audit of the exact profiles proving the quantitative BV input
   needed to specialize (1.5) to (1.6); and
2. a genuinely signed, full-range cross-pair estimate for (1.8), or a
   rigorous identification of (1.8) with an already controlled return.

Absent those two items, the authoritative accepted graph should remain
unchanged.

# Second-stage addendum: line audit of the conductor flattening candidate

## A1. Result of the audit

The candidate
`candidates/conductor_profile_flattening_and_integer_phase.md` is
mathematically sound after two local presentation repairs and two explicit
boundary conventions:

1. In the proof of (121.C10), “absolutely summable \(C^1\) coefficient
   norm” must mean a weighted absolutely summable Fourier norm obtained
   from sufficiently many derivatives of the smooth two-variable
   multiplier. Bare \(C^1\) regularity in two dimensions would not imply
   the asserted absolute summability. The actual multiplier is
   \(C^\infty\) with uniform derivatives, so this is a repair, not a gap.
2. The display after (121.C10) contains the TeX typo
   `\left{left`; the intended first term is
   \((L/H_j)^2\).
3. In (121.C16)--(121.C17), use the standard convention that every
   positive \(d\) divides \(0\), so that the term \(k=-N\) is included
   correctly in \(A_y(0)\).
4. In (121.C19a), the displayed floor formula is valid for every
   \(k\in\mathbb Z\), not only \(k\geq1\). Stating it for all integers
   removes the otherwise informal “analogous reversed interval” boundary.

With those clarifications:

* (121.C3) is proved at the stated target scale, for both frequency signs.
  The exact profile report removes the profile-BV condition left open in
  Sections 1 and 4 of the blind report above.
* The signs and the hard endpoint in (121.C11)--(121.C12) are correct, and
  the flat and unflattened amplitude seams are respectively
  \(O_{s_0}(\log(2X))\) and \(O_{s_0}(\log^2(2X))\).
* (121.C13) is correct with the stronger error \(O_{s_0}(R)\), while
  \(y\), \(R\), and the radial cutoff remain those of the original real
  \(X\).
* (121.C17)--(121.C20) are exact with the stated Fourier sign. They give a
  reproducible sharp-denominator discrepancy survivor once an explicit
  interpolant \(J_{R,y}\) is fixed as in A3.5 below.

The candidate still does not estimate the survivor. Round 64 and Round 65
show that this is the same unmatched-crossing obstruction class, now at a
sharp global denominator cutoff. Thus the correct outcome is a proved
target-scale equivalence and a no-gain return, not closure of the lower
radial parent.

## A2. Corrected exact statement and hypotheses

Use the candidate's fixed choice \(0<s_0\leq1/100\). The now-permitted
exact profile derivation supplies

\[
 \begin{aligned}
 &w_0(d)={\bf1}_{d\leq y}W(d/y),\qquad
   \operatorname{supp}w_0\subset[D_0/2,D_0],\\
 &w_j(d)=W(d/D_j)\quad(1\leq j\leq J),\qquad
   \operatorname{supp}w_j\subset[D_j/2,4D_j/3],\\
 &w_{\rm bot}(d)=\eta(d/D_{J+1}),\qquad
   \operatorname{supp}w_{\rm bot}\subset[1,4D_{J+1}/3),
 \end{aligned}                                                 \tag{A2.1}
\]

with \(D_{J+1}<R\), \(0\leq w\leq1\), exact partition

\[
 {\bf1}_{d\leq y}=w_0(d)+\sum_{j=1}^Jw_j(d)+w_{\rm bot}(d),   \tag{A2.2}
\]

and discrete BV norm at most \(3\) for every active profile. In
particular, the candidate's looser closed support
\(1/2\leq d/D_j\leq3/2\) is valid.

Under the accepted frequency-first divisor theorem, the complete audited
conclusion is

\[
 \boxed{
 \mathcal B_{\rm low}^{\pm}(X)
 =\mathcal B_{\rm flat}^{\pm}(X)
 +O_{\varepsilon,s_0}(RX^\varepsilon),}                       \tag{A2.3}
\]

and, with \(N=\lfloor X\rfloor\) but with \(R=X^{1/4}\) and
\(y=\lfloor\sqrt X\rfloor\) unchanged,

\[
 \boxed{
 \mathcal B_{\rm flat}^{+}(X)
 =\sum_{k\in\mathbb Z}\widehat J_{R,y}(k)A_y(N+k)+O_{s_0}(R)}\tag{A2.4}
\]
\[
 \boxed{
 =\sum_{k\in\mathbb Z}D_N(k)
   \{\widehat J_{R,y}(k)-\widehat J_{R,y}(k+1)\}
   +O_{s_0}(R).}                                               \tag{A2.5}
\]

Here

\[
 A_y(m)=\sum_{\substack{d\leq y\\d\mid m}}\chi_4(d)
 \quad(m\in\mathbb Z),                                      \tag{A2.6}
\]

with \(d\mid0\), and the all-integer discrepancy is

\[
 \boxed{
 D_N(k)=\sum_{d\leq y}\chi_4(d)
 \left(\left\lfloor{N+k\over d}\right\rfloor
       -\left\lfloor{N\over d}\right\rfloor-{k\over d}\right)
 \quad(k\in\mathbb Z).}                                     \tag{A2.7}
\]

For a real interpolant \(J_{R,y}\), the negative sign is the exact
conjugate and can also be written

\[
 \mathcal B_{\rm flat}^{(N),-}
 =\sum_k\widehat J_{R,y}(k)A_y(N-k).                          \tag{A2.8}
\]

Consequently, at the \(RX^\varepsilon\) scale, the original lower owner,
the flat cone, the integer-centred truncated divisor wavelet, and the
affine crossing functional in (A2.5) are pairwise equivalent. This is an
equivalence of analytic obligations, not a bound for any one of them.

## A3. Proof and line-by-line corrections

### A3.1. Lines 48--82: support, floors, bottom, and hard top

Nonvanishing of the exact cutoff gives

\[
 {hR\over d}< {\sqrt{2s_0}\over2}.                            \tag{A3.1}
\]

The certified upper profile support is actually \(d/D_j\leq4/3\);
using the candidate's looser \(3/2\) gives

\[
 {hR\over D_j}< {3\sqrt{2s_0}\over4}<\frac12.                \tag{A3.2}
\]

Thus \(D_j/R>2h\), so the exact integer satisfies
\(h\leq\lfloor D_j/R\rfloor=H_j\). Moreover

\[
 H_j+1>D_j/R,qquad
 {h\over H_j+1}<{hR\over D_j}<\frac12.                       \tag{A3.3}
\]

No floor endpoint is lost. Conversely, (A3.1) and \(h\geq1\) imply

\[
 d>{2R\over\sqrt{2s_0}}>\frac43R
   >\frac43D_{J+1},                                          \tag{A3.4}
\]

so the bottom remainder in (A2.2) is identically zero on the joint
support. The exact active partition is therefore
\({\bf1}_{d\leq y}\), including \(w_0(y)=1\) and its jump to zero at
\(y+1\). This validates the exact main-coefficient flattening before the
\(\Phi-1\) error is estimated.

### A3.2. Lines 86--124: the Vaaler error and the separation repair

For the standard accepted Vaaler profile

\[
 \Phi(u)=\pi u(1-u)\cot(\pi u)+u\qquad(0\leq u<1),            \tag{A3.5}
\]

the expansion \(\pi u\cot(\pi u)=1-\pi^2u^2/3+O(u^4)\)
gives

\[
 \Phi(u)-1=O(u^2),\qquad \Phi'(u)=O(u)                        \tag{A3.6}
\]

uniformly on the smaller interval forced by (A3.2). On a normalized-BV
shell \(h\asymp L\), the coefficient

\[
 \eta_L(h){\Phi(h/(H_j+1))-1\over h}
\]

therefore has sampled supremum plus variation

\[
 \ll {1\over L}\left({L\over H_j}\right)^2.                 \tag{A3.7}
\]

Write \(u=h/L\), \(v=d/D_j\), and
\(\lambda=RL/D_j\). On the fixed rectangle supporting the shell and
profile, the coupled radial factor is

\[
 Q_\lambda(u,v)=V_{\rm low}(4\lambda^2u^2/v^2).               \tag{A3.8}
\]

All derivatives of a fixed smooth extension of \(Q_\lambda\) are uniform
for the allowed \(0\leq\lambda\leq c<1/2\). Expand that extension in a
two-variable Fourier series. By integrating by parts sufficiently many
times (for example, four times in each variable), its coefficients obey

\[
 \sum_{r,s}|c_{r,s}(\lambda)|(1+|r|)\ll_{s_0}1.               \tag{A3.9}
\]

The factor \(1+|r|\) is exactly what controls the sampled height BV after
multiplication by the \(r\)-th height mode. The spatial mode merely
multiplies \(w_j(d)\) by a bounded phase; the frequency-first theorem
allows arbitrary bounded spatial coefficients and the hard truncation
\(d\leq y\). Homogeneity in (A3.7), followed by (A3.9), gives

\[
 E_{j,L}\ll_{\varepsilon,s_0}X^\varepsilon
 \left({L\over H_j}\right)^2\left(1+{D_j\over L}\right),    \tag{A3.10}
\]

which is (121.C10) with a complete separation justification.

For a nonempty active profile,
\(D_j/(2R)\leq H_j\leq D_j/R\). Hence

\[
 \sum_{L\ {
m dyadic}\atop L\leq cH_j}
 \left\{(L/H_j)^2+{D_jL\over H_j^2}\right\}
 \ll1+{D_j\over H_j}\ll R.                                  \tag{A3.11}
\]

There are \(O(\log X)\) active profiles; applying the frequency theorem
with \(\varepsilon/2\) absorbs this logarithm. Equations
(A3.1)--(A3.11) prove (121.C3). The exact top profile is allowed because
the theorem needs bounded spatial coefficients, not a smooth full-line
Poisson profile.

### A3.3. Lines 128--159: pair sign and amplitude boundaries

For \(q\equiv1\pmod4\), \(p=q+2\),

\[
 e(hX/p)=e(hX/q)e\!\left(-{2hX\over q(q+2)}\right).           \tag{A3.12}
\]

Thus (121.C12) has the correct sign:

\[
 b(h,q)e(hX/q)-b(h,p)e(hX/p)
 =[b(h,q)-b(h,p)]e(hX/q)
 +b(h,p)e(hX/q)\{1-e(-2hX/(q(q+2)))\}.                       \tag{A3.13}
\]

Zero extension includes the pair containing the hard sample \(d=y\),
regardless of the residue class of \(y\). The exact profile bounds
\(\|w_j\|_{\mathrm{BV}_d}\leq3\) now make the blind report's estimate
(1.4)--(1.6) unconditional: product variation with the fixed radial
cutoff gives \(O(1)\) per \((j,h)\), hence \(O(\log^2X)\) after the
profile and harmonic sums. For the flat indicator there is only one hard
denominator jump, giving \(O(\log X)\).

### A3.4. Lines 163--188: integerization

With \(N=\lfloor X\rfloor\),

\[
 |e(hX/d)-e(hN/d)|\leq2\pi {|X-N|h\over d}\leq {2\pi h\over d}.\tag{A3.14}
\]

For fixed \(d\), the exact radial support has fewer than
\(C_{s_0}d/R\) positive heights. After the \(1/h\) factor,

\[
 \sum_{d\leq y}{1\over d}\#\{h:V_h(d)\ne0\}
 \ll_{s_0}\sum_{d\leq y}{1\over R}
 \leq {y\over R}\leq R.                                     \tag{A3.15}
\]

This proves (121.C13) by absolute summation. It changes only the phase:
the hard floor \(y=\lfloor\sqrt X\rfloor\), \(R=X^{1/4}\), and
\(V_{
m low}(4R^2h^2/d^2)\) are not replaced by their \(N\)-analogues.
The negative phase obeys the same estimate.

### A3.5. Lines 192--230: exact Fourier completion and its boundary

The existence assertion for \(J_{R,y}\) can be made canonical. Choose a
fixed \(\zeta\in C^\infty(\mathbb R)\) with
\(\zeta(u)=0\) for \(u\leq1/2\) and \(\zeta(u)=1\) for \(u\geq1\), and
on the positive lift of the circle set

\[
 J_{R,y}(t)=\zeta(yt){V_{\rm low}(4R^2t^2)\over t},           \tag{A3.16}
\]

extending it by zero outside the small positive arc on which the radial
factor can be nonzero. It is smooth and periodic: it vanishes on a
neighborhood of \(0\), while the smooth radial factor vanishes before the
far end of the arc. Every supported sample has
\(t=h/d\geq1/y\), so (A3.16) equals the required value there. Its Schwartz
seminorms may depend on \(R,y\); the candidate uses only exact convergence
and claims no uniform Fourier-norm estimate.

Because \(s_0\leq1/100\), every supported height has \(0<h<d\). Therefore

\[
 \begin{aligned}
 \sum_{h\geq1}{V_{\rm low}(4R^2h^2/d^2)\over h}e(Nh/d)
 &={1\over d}\sum_{h\bmod d}J_{R,y}(h/d)e(Nh/d)\\
 &=\sum_{k:\ d\mid N+k}\widehat J_{R,y}(k).                 \tag{A3.17}
 \end{aligned}
\]

The Fourier sign \(N+k\) is correct because
\(J(t)=\sum_k\widehat J(k)e(kt)\). Summing (A3.17) against
\(\chi_4(d)\), including the standard congruence \(d\mid0\) at
\(k=-N\), proves (121.C17). The residue \(h=0\) contributes zero because
\(J(0)=0\), and the one-sided denominator \(d=y\) remains included.

### A3.6. Lines 234--284: centering, all-integer floors, and Abel sign

Absolute Fourier convergence gives

\[
 \sum_k\widehat J_{R,y}(k)=J_{R,y}(0)=0,                     \tag{A3.18}
\]

so subtracting \(c_y=\sum_{d\leq y}\chi_4(d)/d\) proves
(121.C18). Define the right side of (A2.7) as \(\widetilde D_N(k)\).
For every integer \(k\), including negative values,

\[
 \widetilde D_N(k)-\widetilde D_N(k-1)
 =\sum_{d\leq y}\chi_4(d)
   \left({\bf1}_{d\mid N+k}-{1\over d}\right)
 =A_y(N+k)-c_y.                                                \tag{A3.19}
\]

Also \(\widetilde D_N(0)=0\), so the recurrence uniquely gives
\(\widetilde D_N=D_N\) on all of \(\mathbb Z\). This proves the
all-integer strengthening (A2.7), including intervals crossing zero.

Finally, if \(f_k=\widehat J_{R,y}(k)\), then

\[
 \sum_k f_k\{D_N(k)-D_N(k-1)\}
 =\sum_kD_N(k)\{f_k-f_{k+1}\}.                               \tag{A3.20}
\]

The sign and shift in (121.C20) are therefore correct. The boundary terms
vanish because \(f_k\) is Schwartz for fixed \(X\), whereas the elementary
definition gives at most polynomial growth for \(D_N(k)\).

## A4. First doubtful or unproved continuation

After the separation wording is repaired as in (A3.9), none of
(121.C3), (121.C13), or (121.C17)--(121.C20) has a remaining proof gap
relative to the newly permitted exact profile and frequency-first
theorems. The first unproved continuation is the signed estimate

\[
 \sum_kD_N(k)
 \{\widehat J_{R,y}(k)-\widehat J_{R,y}(k+1)\}
 \ll_{\varepsilon,s_0}RX^\varepsilon.                         \tag{A4.1}
\]

No uniform estimate may be inferred merely from the fact that
\(\widehat J_{R,y}\) is Schwartz: the cutoff needed between \(0\) and
\(1/y\) makes its seminorms depend on \(X\). Round 64 shows that inverse
Poisson reconstructs the reciprocal cone, and Round 65 identifies the
remaining affine Abel functional as an unmatched period-four crossing
problem. At the Round-62 endpoint \(\nu=2/5\), the previously audited
absolute capacity still exceeds the target by \(X^{1/20}\). Thus
(A4.1) requires new signed arithmetic cancellation and is not supplied by
integerization, character pairing, or smooth wavelet moments.

The candidate's phrase “smallest candidate survivor” is acceptable only
within this chain of algebraic reductions. The permitted historical
syntheses do not prove that the sharp global survivor is strictly smaller
than the accepted Round-65 local-discrepancy return; they show the same
obstruction class.

## A5. Control tests and outcomes

| Item audited | Invariant tested | Outcome | State consequence |
|---|---|---|---|
| (121.C3) profile flattening | Exact active partition, \(H_j\) floors, \(H_j+1\), bottom exclusion, hard \(d=y\), Taylor suppression, and applicability of the frequency-first theorem on every \(h\)-shell. | Pass after replacing the ambiguous \(C^1\)-summability sentence by (A3.8)--(A3.10). The exact profile report supplies all support and BV data. | Promote as a target-scale two-sided antecedent equivalence, not as an estimate of the lower owner. |
| (121.C12) signs and seams | \(\chi_4(4m+1)=1\), \(\chi_4(4m+3)=-1\), zero extension, phase increment sign, and hard terminal pair. | Pass. Equation (A3.13) verifies the minus sign; exact BV makes both seam bounds unconditional. | Promote the exact paired survivor and safe amplitude seams as subordinate reductions. |
| (121.C13) integerization | Keep \(R,y,V_{\rm low}\) attached to real \(X\); change only \(e(hX/d)\); include all supported heights and both signs. | Pass with absolute error \(O_{s_0}(R)\), by (A3.14)--(A3.15). | Promote. |
| (121.C17) completion | Check the missing \(1/d\), Fourier sign, residue \(h=0\), condition \(h<d\), hard \(d=y\), and \(N+k=0\). | Pass. The convention \(d\mid0\) must be explicit. No factor or sign is missing. | Promote the exact identity for a fixed explicit \(J_{R,y}\). |
| (121.C18) centering | Check \(\sum_k\widehat J(k)=J(0)\) and the affine density \(c_y\). | Pass because \(J(0)=0\) and its Fourier series is absolutely convergent for fixed \(X\). | Promote. |
| (121.C19)--(121.C19a) floors | Check positive, negative, zero-crossing, and exact-divisibility cases. | Pass after strengthening the floor formula to all \(k\in\mathbb Z\), as in (A2.7). | Promote the strengthened version. |
| (121.C20) Abel shift | Check the sign in \(\widehat J(k)-\widehat J(k+1)\) and both infinite boundaries. | Pass by (A3.20); Schwartz decay beats the polynomial discrepancy bound. | Promote. |
| Both frequency signs | Check real-coefficient conjugacy after flattening, integerization, and completion. | Pass; (A2.8) is the explicit negative-frequency completion. | The promoted reduction should be stated for \(\pm\), even if the graph stores only the positive owner plus conjugacy. |
| Round-62/64/65/120 scope | Test full lower range, historical self-return, and downstream ownership. | The reduction is exact on the full physical lower cutoff, not the Round-62 small-angle replacement. It returns to the Round-65 unmatched-crossing class. Round 120 still leaves the lower owner as GAR's sole aggregate M1 parent. | No GAR, blockwise M9-M1, M9, endpoint-uniformity, or exponent promotion follows. |

## A6. Dependencies and exact artifacts used in this second stage

In addition to the statement-only artifacts listed in Section 6 above,
this bounded audit used exactly:

1. `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/candidates/conductor_profile_flattening_and_integer_phase.md`;
2. `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`;
3. `rounds/codex-managed/m9-m1-frequency-phase-diagram/reports/m1_terminal_arithmetic_attack.md`;
4. `rounds/codex-managed/m9-m1-lower-radial-small-angle-collapse/synthesis.md` (Round 62);
5. `rounds/codex-managed/m9-m1-reciprocal-product-wavelet/synthesis.md` (Round 64);
6. `rounds/codex-managed/m9-m1-product-wavelet-local-discrepancy/synthesis.md` (Round 65);
7. `rounds/codex-managed/m9-m1-gar-radial-interface-reconciliation/synthesis.md` (Round 120).

No other nonblind artifact, sibling report, shared proof-state file, web
source, or computation was used in the second-stage audit. The candidate
and shared state were not edited.

## A7. Recommended maximal state effect

The candidate's proposed state effect is safe but not quite maximal. After
the two local repairs above, the maximal justified patch would:

1. promote (121.C3) for both signs and record the **bidirectional
   target-scale equivalence** between the exact floor-perturbed lower
   antecedent and the flat sharp cone;
2. promote the now-unconditional flat and unflattened amplitude-seam
   bounds together with the exact sign in (121.C12);
3. promote (121.C13) for both signs with its \(O_{s_0}(R)\) error;
4. promote (121.C17), (121.C18), the all-integer version (A2.7) of
   (121.C19a), and (121.C20), preferably using the explicit interpolant
   (A3.16) and the convention \(d\mid0\);
5. compose those statements into the single proved equivalence
   (A2.3)--(A2.5), so the remaining lower-radial analytic node may be
   represented by the prescribed-centre sharp truncated-divisor
   discrepancy rather than by the original profile kernel; and
6. record a no-gain/self-return edge to the accepted Round-65
   unmatched-crossing obstruction and close this particular
   flattening/integerization/pairing mechanism as exhausted.

Keep `M9-M1-global-lower-radial-signed-estimate` open. Round 120 then still
leaves GAR open on that one aggregate M1 parent, and nothing here changes
the status of blockwise M9-M1, M9-M2, endpoint uniformity, M9, or the
external exponent.
