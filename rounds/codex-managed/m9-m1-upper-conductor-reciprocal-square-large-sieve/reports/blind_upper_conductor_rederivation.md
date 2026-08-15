## 1. Result

The normalization of (72.6)--(72.8) is correct.  More precisely, the
first-moment bound (72.6), multiplied by the outer coefficient (72.5),
gives (J^{1/2}X^\varepsilon), and Cauchy in the (B\asymp C/T)
rows turns (72.8) into (72.6) with no missing power.  The asserted
diagonal scale (BC=C^2/T) is at most (J^2/T), with equality in scale
only at (C=J).  The trivial row bound reaches the energy target only
through (C\leq J^{2/3}), so it gives no part of the frozen upper range.

I do not obtain (72.8).  This is underdetermination, not a counterexample:
the packet does not give a formula or quantitative seminorms for
(a_{b,c,k}), and it gives no formulas at all for the even or axial
pieces.  Exact-square and fourth-power specializations create genuine
derivative resonances and same-residue pairs on which the inverse twist
cancels, so a proof based only on a nonzero real derivative is invalid.
Those configurations do not by themselves exceed (J^2/T).  The first
new estimate still needed is a joint off-diagonal correlation bound with
the actual symbol retained.

## 2. Exact statement and hypotheses

Let

\[
 X=J^2,\qquad T=J^{3/5},\qquad
 J^{2/3}<C\leq J,\qquad B=C/T,
\]

and fix one compatible positive (k=\rho\sigma).  For

\[
 A_b=bX+\sqrt{kX}+\frac{k}{4b}
\]

define (S_{b,k}(C)) and \(\mathcal E_{C,k}\) exactly as in (72.4) and
(72.7).  The conclusions below use only the following items explicitly
present in the packet:

* there are (O(B)) values in the dyadic (b\)-block;
* the outer stationary coefficient is
  (T/\sqrt{CJ}), up to fixed constants and (X^\varepsilon);
* the packet asserts the diagonal scale (BC);
* (k) ranges over a fixed finite compatible family.

Under those hypotheses,

\[
 \mathcal E_{C,k}\ll \frac{J^2}{T}X^\varepsilon
 \quad\Longrightarrow\quad
 \left|\sum_{b\asymp B}S_{b,k}(C)\right|
 \ll \frac{J\sqrt C}{T}X^\varepsilon.                 \tag{B72.1}
\]

Also,

\[
 J^{1/15}<B\leq J^{2/5}.                              \tag{B72.2}
\]

Consequently a dyadic block with (b=O(1)) cannot occur in the strict
upper range for asymptotic (J).  Any bounded-(b) transition intended
by that control lies outside (72.1) or requires an additional,
non-dyadic piece not specified in the packet.

## 3. Proof or derivation

First, the first-moment normalization is

\[
 \frac{T}{\sqrt{CJ}}\cdot\frac{J\sqrt C}{T}
 =J^{1/2}.                                             \tag{B72.3}
\]

Thus (72.6) corresponds to a target-safe contribution of size
(J^{1/2}X^\varepsilon).  Next, Cauchy's inequality gives

\[
 \left|\sum_{b\asymp B}S_{b,k}(C)\right|^2
 \ll B\mathcal E_{C,k}.
\]

Substitution of (B=C/T) and (72.8) yields

\[
 B^{1/2}\left(\frac{J^2}{T}\right)^{1/2}
 =\left(\frac CT\right)^{1/2}\frac J{\sqrt T}
 =\frac{J\sqrt C}{T},                                 \tag{B72.4}
\]

which proves (B72.1).  The harmless halving of an (X^\varepsilon)
exponent is absorbed by renaming \(\varepsilon\).

On the asserted normalization of the actual amplitude, the diagonal is

\[
 D_{C,k}=\sum_{b\asymp B}
 \sum_{\substack{c\asymp C\\(c,4b)=1}}|a_{b,c,k}|^2
 \ll BCX^\varepsilon
 =\frac{C^2}{T}X^\varepsilon
 \leq\frac{J^2}{T}X^\varepsilon.                     \tag{B72.5}
\]

The packet states this scale but does not supply the displayed
(L^2)-amplitude estimate from which it would independently follow.
If one only uses the corresponding pointwise trivial estimate
(|S_{b,k}|\ll CX^\varepsilon), then

\[
 \mathcal E_{C,k}\ll BC^2X^\varepsilon
 =\frac{C^3}{T}X^\varepsilon.                         \tag{B72.6}
\]

Comparison with (J^2/T) gives precisely (C\leq J^{2/3}).  Hence all
of (72.1) requires a nontrivial off-diagonal saving.

Writing (c_2=c+h), the required off-diagonal is

\[
 \mathcal O_{C,k}=
 \sum_{b\asymp B}\ \sum_{\substack{0<|h|\ll C\\
 c,c+h\asymp C\\(c(c+h),4b)=1}}
 a_{b,c,k}\overline{a_{b,c+h,k}}
 e_{4b}\!\left(k(\bar c-\overline{c+h})\right)
 e\!\left(-\frac{A_bh}{c(c+h)}\right).               \tag{B72.7}
\]

No absolute value has been inserted inside a variable where cancellation
is needed.

There are two exact hostile identities.  Additive reciprocity gives

\[
 \frac{\bar c}{4b}+\frac{\overline{4b}}c
 \equiv\frac1{4bc}\pmod 1,
\]

and therefore the row phase can equivalently be written

\[
 e_{4b}(k\bar c)e(-A_b/c)
 =e_c(-k\overline{4b})
  e\!\left(-\frac{bX+\sqrt{kX}}c\right).              \tag{B72.8}
\]

This moves the inverse twist; it does not remove it.  Moreover, whenever
(h\equiv0\pmod{4b}),

\[
 e_{4b}\!\left(k(\bar c-\overline{c+h})\right)=1.     \tag{B72.9}
\]

Thus the inverse twist supplies no cancellation on all same-residue
correlations.

The continuous part of the (b)-phase in (B72.7) has derivative

\[
 -\left(X-\frac{k}{4b^2}\right)\frac{h}{c(c+h)}.       \tag{B72.10}
\]

At (C=J), its leading size is (|h|), which can be arbitrarily close
to an integer frequency; a large derivative as a real number is not a
discrete cancellation criterion.  This becomes explicit when
(X=J^2) with integer (J) and (k=s^2):

\[
 A_b=\frac{(2bJ+s)^2}{4b},\qquad
 \frac{A_b}{J^2}=b+\frac{s}{J}+\frac{s^2}{4bJ^2}.     \tag{B72.11}
\]

Near (c=J+u), after removal of the integer linear increment (bu),
the continuous chirp has a quadratic scale (bu^2/J).  It therefore
has a possible resonant window of length

\[
 |u|\lesssim\sqrt{J/b}.                               \tag{B72.12}
\]

At (C=J), where (b\asymp B=J^{2/5}), one such window has length
(J^{3/10}).  Even if it were completely coherent, its squared size
summed over (B) rows would be (J^{2/5}J^{3/5}=J), below the target
(J^2/T=J^{7/5}).  Hence this elementary resonance is not a
counterexample.  On the other hand, the packet contains no estimate for
the number and mutual phases of all such windows, so it cannot certify
their aggregate.  If (X) is a fourth power, it is still an exact square;
for square (k) (and especially square (b)) no irrationality-based
escape is available.  The modular factor and the actual symbol must do
the remaining work.

Finally, (B72.2) follows directly from
(B=C/J^{3/5}), (C>J^{2/3}), and (C\leq J).

## 4. First doubtful or unproved step

There are two levels of missing information.  If the diagonal statement
(72.9) is not accepted as an input, the first missing quantitative bound
is already

\[
 \sum_{b\asymp B}\sum_{c\asymp C}|a_{b,c,k}|^2
 \ll BCX^\varepsilon.                                \tag{B72.13}
\]

Qualitative phrases such as “fixed smoothness” and “retained transition
faces” do not specify the uniform size, derivative seminorms, support
multiplicity, or transition losses needed to prove (B72.13).

If the packet's asserted diagonal scale is accepted, the first genuinely
new missing inequality is

\[
 \boxed{\mathcal O_{C,k}\ll\frac{J^2}{T}X^\varepsilon}
                                                               \tag{B72.14}
\]

for (B72.7), with the actual neighbor-dependent and transition symbol.
Neither (B72.10) nor the inverse twist alone proves it uniformly, because
(B72.9)--(B72.12) expose their exceptional sets.  The packet supplies no
joint correlation theorem, no explicit decomposition of the actual
symbol, and no count or cancellation law for those exceptional sets.
This is why the outcome is underdetermined rather than a disproof of
(72.8).

Even a proof of (B72.14) for the displayed odd nonaxial row would not
complete the round: the exact phases, amplitudes, gcd factors, and zero
indices for the two even classes and both axes are absent.

## 5. Required control test and outcome

1. **Normalization:** pass.  Equations (B72.3)--(B72.4) account for all
   factors (B,C,J,T).
2. **Diagonal:** target-compatible, conditional on the diagonal scale
   asserted in the packet.  It is exactly at target scale at (C=J)
   and has slack ((J/C)^2) below the top endpoint.
3. **Near diagonal:** unresolved, not contradictory.  Same-residue
   differences (4b\mid h) remove the inverse twist, and integer-near
   derivatives prevent a uniform first-derivative argument.
4. **Exact squares and fourth powers:** hostile shortcut test passed in
   the negative sense: (B72.11) shows that irrationality cannot be
   assumed.  The single-window calculation (B72.12) does not violate the
   energy target, but the aggregate is unbounded by the supplied data.
5. **Bounded (b):** vacuous inside the strict dyadic upper range by
   (B72.2).  Any intended bounded-(b) tail needs a separate formula.
6. **Farey neighbors and transition faces:** not testable from the
   packet; their formulas and quantitative symbol bounds are absent.
7. **Even classes, axes, gcd factors, and zero indices:** not testable;
   only the odd nonaxial phase is supplied.  They remain explicit open
   seams and are not inferred by sign changes.
8. **Finite (k)-sum:** harmless only after a uniform estimate for each
   compatible member; finiteness cannot repair a failed member.
9. **Global-exponent control:** no conclusion here concerns the original
   wavelet's (X^{1/20}) gap or a global exponent.  The calculation is
   confined to this representation and local class.

## 6. Dependencies and exact artifacts/sources used

Isolation ledger:

* Opened during this task:
  `rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/briefs/blind_upper_conductor_rederivation.md`.
* Opened during this task:
  `rounds/codex-managed/m9-m1-upper-conductor-reciprocal-square-large-sieve/derivation_packet.md`.
* Not opened: the proof graph, shared state, prior-round reports, sibling
  reports, source cards, or any other repository file.
* No web source, external theorem, symbolic program, or numerical
  experiment was used.  All displayed calculations are hand algebra
  from the two listed files.
* Isolation caveat: the full-history task fork exposed a conductor-level
  summary of the preceding round and the proposed Round-72 direction
  before this brief was read.  I did not use any prior proof or report as
  evidence, but this report should not be labelled exposure-free blind
  evidence.

## 7. Recommended state effect

Retain (72.8) as open; do not promote it.  The algebraic sufficiency of
(72.8), the diagonal compatibility conditional on (72.9), the exact
reciprocity identity (B72.8), the same-residue obstruction (B72.9), and
the absence of bounded (b)-blocks in (72.1) may be retained as scoped
audits.  Revise the next proof interface to supply (i) explicit uniform
size and derivative bounds for every stratum of (a_{b,c,k}), and (ii)
a proof of the joint off-diagonal estimate (B72.14).  No state effect is
recommended for the even classes, axes, the full fixed-interior target,
or any global exponent.
