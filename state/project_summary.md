# Project Summary

## Project and problem setting

The project is an auditable attempt to organize research toward the conjectural Gauss circle error bound. With

$$
N(R)=\#\{(m,n)\in\mathbb Z^2:m^2+n^2\le R^2\},
$$

the target is

$$
N(R)-\pi R^2\ll_\varepsilon R^{1/2+\varepsilon}.
$$

The repository uses $X=R^2$ and writes the same target as

$$
P(X)=N(\sqrt X)-\pi X\ll_\varepsilon X^{1/4+\varepsilon}.
$$

This target is open. The repository contains a complete internal proof
of the fallback bound
\(P(X)\ll_\varepsilon X^{1/3+\varepsilon}\), together with a
conditional architecture for the conjectural \(1/4+\varepsilon\)
target. Round 95 also certifies, as a repaired external dependency, the
stronger direct theorem

\[
 P(X)\ll_\varepsilon X^{\theta_{\rm LY}+\varepsilon},\qquad
 \theta_{\rm LY}=
 \frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots .
\]

The internal \(1/3\) theorem and the repaired external theorem are
logically separate. Neither closes M9 or the quarter target.

## Round 95 reduced cluster and repaired external theorem (2026-08-17)

At the fixed window \(W=Y^{7/16}\), reducing every literal M1/M2
frequency \(h/d\) to \(a/b\) and aggregating all lifts gives

\[
 |A_i(a,b)|\ll_\varepsilon Y^\varepsilon L^{-1},
 \qquad
 \sum_{(a,b)=1}|A_i(a,b)|^2
 \ll_\varepsilon Y^\varepsilon D/L.
\]

Thus the complete equal-ray diagonal, including all lift cross terms,
is safe. The exact remaining object is the signed determinant
correlation with \(n=ab'-a'b\), phase
\(e(cn/(\kappa_i bb'))\), \(\kappa_1=1\), \(\kappa_2=4\), and the
literal M1/M2 characters and endpoint symbols retained. At the minimax
block, coefficient-blind Farey degree gives only
\(Y^{43/48+\varepsilon}\), missing the desired
\(Y^{1/2+\varepsilon}\) cluster energy by \(Y^{19/48}\). The accepted
Popov full-discrepancy theorem is closer, with an additive gap
\(Y^{1/16}\), but cannot be reversed blockwise. No internal exponent
below one third is proved by this route.

Independently, the Li--Yang source chain was repaired and rechecked. Four
literal defects have unique final-argument readings, and the two missing
general range conditions are proved only on the exact final application
range. The narrow real-\(X\), inclusive theorem at
\(\theta_{\rm LY}=0.3144831759\ldots\) is therefore accepted as a
`proved_external_dependency`; the over-stated general intermediate
claims are not. M9-M1, M9-M2, both canonical cores, endpoint uniformity,
M9, and the quarter target remain open.

## Round 93 global mean square and density-one quarter theorem (2026-08-17)

The exact frozen denominator-shell moment and the full moving-height/top
transfer are now proved.  Rational equal-frequency grouping gives

\[
 \int_I|S_{D,H,w}(t)|^2\,dt\ll (|I|+D^2)D,
\]

and the exact height increments, ordered-prefix maximal inequality, and
fixed-BV Stieltjes decomposition retain this power bound for the moving M1
and M2 profiles with logarithmic loss only.  The fixed-in-\(Y\) dyadic
partition, bottom owner, R5-Full, and H1--H4 therefore give

\[
 \int_Y^{2Y}|P(t)|^2\,dt\ll_\varepsilon Y^{3/2+\varepsilon}.
\]

For every fixed \(\eta>0\),

\[
 \bigl|\{t\in[Y,2Y]:|P(t)|>Y^{1/4+\eta}\}\bigr|
 \ll_{\varepsilon,\eta}Y^{1-2\eta+\varepsilon}.
\]

Thus the quarter exponent holds on a density-one set of real parameters.
The result is not pointwise and does not control prescribed reals,
integers, or circle-counting jump points.  It gives no bound for either
canonical hard core.  The uniform exponent remains \(1/3\), and M9-M1,
M9-M2, endpoint uniformity, M9, and the conjectural uniform quarter theorem
remain open.

Accepted evidence:

- rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/reports/blind_m2_moment_rederivation.md;
- rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/reports/moving_coefficient_moment_attack.md;
- rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/reports/moment_hostile_source_audit.md;
- rounds/codex-managed/m9-m2-global-second-moment-exceptional-set/synthesis.md.

## Round 92 canonical core formalization (2026-08-17)

The two target-scale survivors are now exact standalone open graph nodes.
The M1 node is the conjugation-closed hard four-row actual-symbol
Fejer--Gram operator on (J^{13/18}<C\leq J^{3/4}), after literal
one-count deletion of the accepted Round-87--89 packages. Its target is

\[
 |\mathcal E_{\rm hard}(U)|
 \ll_\varepsilon X^\varepsilon{U\over B}J^{14/5}.
\]

The (J^{1/6}) Gram deficit square-roots through Toeplitz to the same
(J^{1/12}) linear deficit; it is not an additional loss.

The M2 node is the residual hard-top primitive-ray energy with the ordinary
metric density and every discrepancy mode kept jointly:

\[
 \sum_{A,D_{\rm ray},K_{\rm rec},G,R}|\mathfrak Q_{A,D_{\rm ray},K_{\rm rec},G,R}|
 \ll_\varepsilon L^2X^\varepsilon.
\]

A hard block has excess (sqrt\rho), so the required gain is
(\rho^{-1/2}).  The exact row-to-energy bridge is retained.  Li--Yang and
Xiao were audited as nonapplicable guardrails, one graph dependency cycle
and overstrong top-M2 edges were repaired, and no analytic status changed.

The unconditional exponent remains (1/3).  M1 and M2 still have
separately owned outside packets and target-scale endpoint assembly beyond
these two cores.

## Round 91 unconditional one-third theorem (2026-08-17)

The accepted hyperbola--Vaaler decomposition, pointwise Fejer
product-count estimate, and literal fully weighted M1/M2 direct block
menu now prove

\[
 P(X)\ll_\varepsilon X^{1/3+\varepsilon}
\]

uniformly for every real \(X\ge2\).  The proof retains the actual
Vaaler coefficients, M1 spatial character, M2 two-shift character,
both signs, hard-top sampled-BV profile, exact products, floors, stars,
and the complete dyadic assembly.

For \(R=D/L\), the frequency-first row handles
\(R\le X^{1/3}\).  On \(R\ge X^{1/3}\), the full second-derivative row
has terms at most \(X^{1/3}\) and \(X^{1/4}\), since
\(R\le D\le X^{1/2}\).  The bottom denominator range and every Fejer
residual are already \(O(X^{1/4+\varepsilon})\).

The exponent \(1/3\) is exact for the accepted direct menu at
\((\delta,\ell)=(1/2,1/6)\).  Thus any improvement below \(1/3\)
requires a genuinely new signed M1 or M2 hard-core estimate.  The
pointwise R5 reconciliation is now closed.  M9-M1, M9-M2, M9,
endpoint uniformity at the target scale, and the conjectural
\(1/4+\varepsilon\) theorem remain open.

Accepted evidence:

- rounds/codex-managed/gc-unconditional-exponent-extraction/reports/blind_global_exponent_rederivation.md;
- rounds/codex-managed/gc-unconditional-exponent-extraction/reports/global_exponent_assembly_attack.md;
- rounds/codex-managed/gc-unconditional-exponent-extraction/reports/global_exponent_hostile_audit.md;
- rounds/codex-managed/gc-unconditional-exponent-extraction/synthesis.md.

## Round 90 M1 square-root capacity barrier (2026-08-17)

The complete R82--R89 first-band M1 transform chain now has an exact
norm-level interpretation.  The deep centered Kloosterman-product row
reassembles from distinct physical ordered pairs, and its Fejer
A-process is exactly the four-row actual-symbol Gram operator used in
Rounds 87--89.  Complete cells, local descent, inverse completion,
transposition, signs, classes, modulus multiples, stationary weights,
and the global \(u=0\) diagonal reassemble once.

If

\[
 \mathsf C_{82}=B^3T^2Q^{-5/12},\qquad
 \mathsf T_{82}=J^2/T,
\]

then at full directed degree

\[
 \mathsf C_{\rm deep}={D\over B}\mathsf C_{82}^2,
 \qquad
 \mathsf T_{\rm deep}={D\over B}\mathsf T_{82}^2.
\]

The Toeplitz/Fejer inequality supplies the factor \(B/D\) before the
square root.  Therefore the top-band \(J^{1/6}\) Gram gap is exactly
the square of the Round-82 \(J^{1/12}\) linear gap, not an additional
loss.  This is a Gram-level equal-capacity barrier, not a linear
involution.

The exact \(q=8\) residual cell retains full degree, so further local
period peeling is terminated.  The canonical remaining task is a joint
signed estimate for the hard actual-symbol Gram operator.  No M9-M1,
M9-M2, M9, R5-Full, endpoint, or global-exponent conclusion changes.

The current full-proof strategy is recorded in
`strategy/conductor_0817_full_proof_strategy.md`.  Rounds 91 and 92 have
completed unconditional-exponent extraction and canonical-core
formalization.  The next deliverable is a signed moment/exceptional-set
theorem with an explicit pointwise consequence.

Accepted evidence:

- rounds/codex-managed/m9-m1-capacity-self-return-fork/reports/m1_self_return_barrier_attack.md;
- rounds/codex-managed/m9-m1-capacity-self-return-fork/reports/blind_m1_capacity_rederivation.md;
- rounds/codex-managed/m9-m1-capacity-self-return-fork/reports/m1_self_return_hostile_source_audit.md;
- rounds/codex-managed/m9-m1-capacity-self-return-fork/synthesis.md.

## Round 87 full-factor exceptional Fejer deletion (2026-08-17)

The deep first-band M1 correlation has been reduced at the exact
four-Kloosterman exceptional interface.  Write the normalized physical
row as

\[
 \mathcal R_{b,x}(\theta)
 ={1\over M}\sum_n I_b(n)e_M(nx)e(n\theta),
 \qquad
 \|\mathcal R_{b,x}\|_\infty
 \ll_\varepsilon X^\varepsilon TQ^{-5/24}.
\]

Grouping each ordered pair by the full prime-power factors on which its
two entries differ converts every mixture of the full-factor local-zero
and paired branches into positive Fejer squares.  For a dyadic deep
interval and \(U=D\), the complete same-group package satisfies

\[
 \mathcal P_{\rm exc}(D,D)
 \ll_\varepsilon X^\varepsilon DB^3T^4Q^{-5/6}
 \ll_\varepsilon X^\varepsilon {D\over B}J^{14/5},
\]

with \(J^{-2/15}\) slack at the largest \(B\).  This includes arbitrary
prime powers, the full \(2\)-part, the hostile prime-power and squarefree
aligned families, same-group stride-\(M\) returns, and the exact centered
Ramanujan bookkeeping.  The conductor audit caught and rejected an
earlier false normalization that double-counted \(M^{-2}\).

The new exact survivor is the cross-group off-diagonal after the global
\(u=0\) diagonal is retained once.  It contains partial lower-conductor
returns, bad-prime and extra \(2\)-adic periods, and aperiodic local
traces.  No estimate for this residual, no conductor extension, and no
new global exponent is proved.

Accepted evidence:

- rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reports/aligned_mode_aggregate_attack.md;
- rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reports/blind_exceptional_strata_rederivation.md;
- rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reports/exceptional_trace_hostile_source_audit.md;
- rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reviews/conductor_round87_normalization.md;
- rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/reviews/conductor_round87_crt_fejer.md;
- rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/synthesis.md.

## Round 86 cubic lower-interior difference deletion (2026-08-16)

The first M1 residual smooth-principal correlation has been narrowed a
third time. Put

\[
 D_1=\lfloor J^{87/140}\rfloor.
\]

On each residue progression, the phase difference for
\(e=|d|\le D_1\) has fixed-sign third derivative

\[
 \asymp {JM^3e\over Q^7}.
\]

Combining the weighted third-derivative estimate with the exact
all-modulus residue \(L^1\) normalization proves that every

\[
 \lfloor J^{17/30}\rfloor<|d|\le
 \lfloor J^{87/140}\rfloor
\]

is target-safe. The aggregate has three terms with worst endpoint
exponents \(7/5\), \(369/280\), and \(61/70\). Both signs, all three
local classes, nonzero modulus multiples, prime powers, gcd modes,
Ramanujan centering, support endpoints, and reflected orientations are
included.

The exact first-band survivor is now

\[
 {1\over M^2}\sum_{b\asymp B}
 \sum_{\lfloor J^{87/140}\rfloor<|d|<\Delta_b-J^{3/4}}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.
\]

The physical \(Q^{-5/12}\) energy factor remains available. Exact
completion reveals prime-power and squarefree divisor-aligned modes of
near-quadratic size, so a uniform coefficientwise square-root bound is
false. No audited theorem controls their joint actual-symbol aggregate.
No conductor interval or global exponent has changed.

Accepted evidence:

- rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reports/twisted_ambiguity_attack.md;
- rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reports/four_kloosterman_hostile_source_audit.md;
- rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reviews/conductor_round86_cubic_shell_normalization.md;
- rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/reviews/conductor_round86_adjudication.md;
- rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/synthesis.md.

## Round 85 outer support-difference deletion (2026-08-16)

The smooth-principal M1 dual correlation now has a second exact deletion.
Let \(\Delta_b\asymp Q^2\) be the diameter of its actual stationary
Fourier support and put

\[
 E_*=Q^2J^{-1/20}=J^{3/4}.
\]

Compact endpoint flatness through normalized derivative order three and
a fresh all-difference error sum prove that every

\[
 |d|\geq\Delta_b-E_*
\]

is target-safe. The edge main is
\(O_\varepsilon(X^\varepsilon J^{13/10})\), and the complete entry/exit,
stationary-remainder, wrong-sign, and exterior errors are
\(O_\varepsilon(X^\varepsilon J^{23/20})\), both below the target
\(J^{7/5}\). Negative differences, nonzero modulus multiples, Ramanujan
terms, and prime-power modes are included.

Together with Round 84, the exact first-band smooth-principal survivor is

\[
 {1\over M^2}\sum_{b\asymp B}
 \sum_{\lfloor J^{17/30}\rfloor<|d|<\Delta_b-J^{3/4}}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.
\]

The shifted physical-row identity retains the accepted \(Q^{-5/12}\)
energy factor, but multiplier triangle and complete transforms provide no
power of \(B\). A literal A-process leaves a weighted four-Kloosterman
off-diagonal with the complete actual symbol. No audited theorem currently
estimates it. No conductor interval or global exponent has changed.

Accepted evidence:

- rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/reports/hybrid_large_difference_attack.md;
- rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/reports/large_difference_source_hostile_audit.md;
- rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/reviews/conductor_round85_support_edge_normalization.md;
- rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/reviews/conductor_round85_adjudication.md;
- rounds/codex-managed/m9-m1-large-dual-difference-joint-dispersion/synthesis.md.

## Round 84 stationary small-dual-difference deletion (2026-08-16)

The first M1 residual smooth-main correlation has been narrowed again.
For the actual Round-81 principal symbol, the three local classes have a
uniform stationary Fourier profile with phase

\[
 -\eta\left(\sqrt X+{\sqrt{\kappa k}\over b}\right)\sqrt{|n|},
\]

Gaussian \(e(-\eta/8)\), and sampled profile size
\(H=C\sqrt T/J\). Exact Kloosterman Parseval gives normalized residue
mass at most two, while on \(n=r+M\ell\) the product phase has curvature
\(\asymp M^2|d|/J\).

Consequently every

\[
 0<|d|\leq\lfloor J^{17/30}\rfloor
\]

is target-safe throughout \(J^{13/18}<C\le J^{3/4}\), including
negative differences, nonzero modulus multiples, Ramanujan terms,
prime-power gcd modes, saddle entry/exit, and stationary errors.  The
first exact principal survivor is the same centered Kloosterman-product
correlation on larger differences.

This is a strict polynomial reduction, not a whole-range \(B\)-saving or
a conductor extension. `M9-M1`, `M9-M2`, `M9`, endpoint uniformity,
`R5-Full`, and the global \(1/4+\varepsilon\) target remain open.

## Round 83 centred M1 dual-difference reduction (2026-08-16)

The first M1 upper-conductor residual band has been narrowed again.
After the exact class-dependent rescaling \(c=g_\kappa x\), the odd and
both even arithmetic factors are ordinary inverse units modulo
\(M\in\{4b,2b,b\}\). Exact Poisson summation writes the smooth row as
\(M^{-1}\sum_nS(n,K;M)I_b(n)\), with \(I_b\) the Fourier transform of
the actual reciprocal symbol.

The same-residue mode \(a=0\) is removed once. Sampled Parseval and the
reciprocal autocorrelation phase then show that the literal dual
difference \(d=0\) is target-safe. The exact remaining smooth-main
object is

\[
 {1\over M^2}\sum_{b\asymp B}\sum_{d\ne0}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.
\]

This is a strict structural improvement, not a conductor extension.
Prime-power offsets rule out a uniform pointwise square-root estimate,
and current trace/Kloosterman dispersion theorems do not accept the
literal composite moduli and joint weights. M9-M1, M9-M2, M9,
and the global \(1/4+\varepsilon\) target remain open.

## Round 79 nonsquare incidence and exact-center closure (2026-08-16)

The residual nonsquare reciprocal geometry now has a graph-accepted
sharp positive theorem. In half-angle coordinates

\[
 m=\frac{a+b}{2},\quad q=\frac{b-a}{2},\quad
 u=\frac{q}{m+\sqrt{m^2-q^2}},
\]

one has \(\Lambda=Xqu\) and the exact open interval
\(Ju/(1-u)<k<2Ju/(1+u)\). On a dyadic block the metric window
contains only \(O(1+K/R)\) integer products \(p=\ell k\) per ray,
and divisor counting gives

\[
 \mathcal I_{\rm ns}\ll_\varepsilon X^\varepsilon\frac{ADK}{R}.
\]

After inserting the complete Round-77 coefficient, the positive
capacity is

\[
 \mathcal A_{\rm ns}\ll_\varepsilon
 X^\varepsilon A\sqrt G\sqrt J D^{3/2}.
\]

Therefore every block \(AJD^3\ll L^3\) is target-sized. Exact
nonsquare centers are also closed: rational-ratio rigidity leaves at
most one primitive ray at fixed \(X\), and all of its divisor modes
contribute \(O_\varepsilon(LX^\varepsilon)\).

The factor-\(R\) saving is sharp. Ordinary strictly metric incidences
occur at density \(1/R\) on populated inner cones, even after square
rays and exact equalities are removed. Thus another algebraic
classification cannot close the problem.  The remaining M2 object is
the complete-coefficient signed strict-metric sum on
\(AJD^3\gg L^3\). The full \(M9\!-\!M2\), \(M9\!-\!M1\), \(M9\),
and global exponent remain open.

## Round 78 signed primitive-square closure (2026-08-16)

The algebraically structured primitive-square/common-squarefree family
inside the exact top-\(M2\) survivor is now graph-accepted.  Writing

\[
 a=s^2,\qquad b=t^2,\qquad t=s+2u,\qquad g=2n+1,
\]

the complete outer and lift phases combine to \(e(-gXu^2/k)\) on
\(Ju/s<k<2Ju/t\).  For each actual lift, the complete collared
coefficient has sampled reciprocal-mode variation

\[
 \sup_k|B_g(k)|+\operatorname{Var}_k B_g(k)
 \ll_\varepsilon X^\varepsilon
 \sqrt{\frac{gt^2}{Ju/s}}.
\]

This is a total-variation theorem, not a pointwise
\(k\partial_k\)-bound; the latter is false at a moving physical collar.
Reciprocal second-derivative cancellation gives \(O(L+1)\) per lifted
square triple, and the \(O(L\log L)\) triple count yields

\[
 |\mathcal S_L^\square(X)|
 \ll_\varepsilon L^2X^\varepsilon.
\]

The corresponding positive Abel majorant is sharply larger:

\[
 \mathcal M_L^\square(X)
 \asymp_{X^\varepsilon}\sqrt J\,L^{3/2}.
\]

Thus exact and metric square-ray resonances are harmless only when the
actual signed \(k\)-phase is retained.  Generic nonsquare rays, the full
top energy, \(M9\!-\!M2\), \(M9\!-\!M1\), \(M9\), endpoint uniformity,
and the global exponent remain open.

## Round 77 actual-symbol normal form and variation (2026-08-16)

The complete top-\(M2\) odd-lift coefficient is now accepted, not merely
a leading stationary approximation.  After one fixed primal collar is
removed at each \(m\)-endpoint, symmetric finite Poisson summation gives

\[
 \mathcal O_L=\mathcal O_{L,\mathrm{stat}}^\circ
 +O_{M,\eta,\Phi,W}\!\left(L^2\log(2+L)\right).
\]

This error owns both full endpoint samples, all removed collar samples,
zero and positive modes, equality modes, and every negative
nonstationary mode.  Every stationary and saddle-transition mode remains
inside the complete centred integral.

For \(h=ga,s=gb\), the actual symbol factors as
\(g^{-3}E_{a,b}(g)P_{a,b}(u)\), with the exact \(W\)-profiles and \(q_X\)
independent of \(g\), while \(E'(g)=O(G^{-1})\).  The exact centred square
then proves

\[
 |\mathfrak B^\circ(g)|+g|\partial_g\mathfrak B^\circ(g)|
 \ll {J(\sqrt b-\sqrt a)\sqrt G\over k^{3/2}},
\]

uniformly through collar entry and exit.  Hence the step-two total
variation has the same scale and discrete Abel is now lawful with

\[
 \left\|{X(\sqrt b-\sqrt a)^2\over2k}\right\|.
\]

The first remaining \(M2\) object is the coefficient-weighted
primitive-pair/reciprocal-mode resonance union.  The energy, signed top
cone, \(M9\!-\!M2\), \(M9\), and global exponent remain open.

## Round 76 odd-lift resonance correction (2026-08-14)

For the hard top-M2 transposed energy, write
\(h=ga\), \(h+2r=gb\), with \(g,a,b\) odd and \((a,b)=1\).
The offset character is constant on each primitive ray, and consecutive
admissible lifts differ by two. The correct bulk resonance is therefore

\[
\left\|\frac{X(\sqrt b-\sqrt a)^2}{2k}\right\|
\lesssim G_{a,b}^{-1},
\]

not the earlier step-one criterion. A fixed primal endpoint collar is
target-safe; an unremoved sharp lower endpoint may require a mod-four
split. The actual-profile family \((a,b)=(81,121)\) at fourth powers
exhibits fully coherent half-integer lift phase. Reciprocal Poisson
self-returns. No energy estimate, polynomial \(L\)-range, or exponent is
proved. The complete centred-integral symbol and its variation remain
uncertified and are the Round-77 target.

## Round 75 exact character-preserving top-M2 energy (2026-08-14)

Regrouping the finite top cone by \(m\) gives

\[
R_m=\sum_{\substack{h\in\mathscr H_L\\m\le h\le4m}}
\chi_4(h)a(h,m)e(\sqrt{Xhm}),
\qquad
|\mathcal T_L|^2\ll L\sum_m|R_m|^2.
\]

The diagonal is \(O(L^2)\), and the exact positive-offset term has sign
\(\chi_4(h)\chi_4(h+2r)=(-1)^r\). Thus
\(\sum_m|R_m|^2\ll_\varepsilon L^2X^\varepsilon\) is sufficient.
The earlier evaluated-saddle all-orders formula is false because the
moving angular amplitude has nonzero stationary corrections. A repaired
dual transform returns to the same energy.

## Round 74 hard-top affine-cone reduction (2026-08-14)

The diagonal, fixed near-diagonal, and endpoint-touching correlations are
target-safe. The remaining intermediate-\(L\) interior is a signed
fixed-centre near-product/row-correlation problem. Two-dimensional
Poisson is rank one; character-leg Poisson returns to the original block.
No polynomial intermediate-\(L\) range or exponent is gained.

## Round 73 residual M1 upper-conductor survivor (2026-08-14)

On \(J^{32/45}<C\le J\), the exact diagonal and every fixed
denominator-offset layer are target-safe. Only their coherent
actual-unit off-diagonal accumulation remains. Fourth derivatives,
Hessian-only estimates, cellwise Bourgain input, and the current
phase-matched spectral model do not extend the accepted conductor range.

## Round 72 M1 conductor advance (2026-08-14)

The all-class weighted third-derivative estimate proves the fixed-interior
M1 conductor blocks through

\[
C\le J^{32/45}=X^{16/45},
\]

extending the earlier \(C\le J^{2/3}\) range. The residual upper
conductor and the global exponent remain open.

## Round 71 low-conductor M1 closure (2026-08-14)

Three-variable Farey stationarity gives local size
\(T/\sqrt{cJ}\) and total block bound
\(\mathcal D_C\ll_\varepsilon X^\varepsilon C^{3/2}/\sqrt J\).
This closes \(T\le C\le J^{2/3}\). The upper-conductor
incomplete-numerator correlation remains open, with the benchmark
\(X^{1/20}\) deficit preserved by the natural completion/self-return.

## Round 68 exact symbol and stationary involution (2026-08-14)

The shifted square-root-product coefficient is now explicit in every
fixed smooth positive-ratio interior sector:

\[
 P_k=\sum_{q\ \mathrm{odd}}\chi_4(q)
 \left({k\over q}\right)^{3/4}
 \Xi\!\left(2\sqrt{k/q}\right)e(\sqrt{Xkq}).
\]

Thus the symbol is Mellin-separable with uniformly bounded logarithmic
derivatives; the earlier arbitrary phase-conjugating coefficient is not
an actual-profile obstruction.

The character sign drives an exact two-step stationary transformation.
Writing \(q_1=q+2d\), the first saddle is
\(q_1^*=4Xk/j^2\) and has the perfect-square phase

\[
 \left(\sqrt{Xk/j}-{1\over2}\sqrt{jq}\right)^2.
\]

The second odd-lattice saddle is \(q^*=4Xk/s^2\) and has phase
\(Xk(1/j-1/s)\). The Gaussian units cancel, the lattice density is
exactly \(1/2\), and the remaining sign is
\((-1)^{(j-s)/2}=\chi_4(j)\chi_4(s)\). Hence the complete stationary
main returns exactly \((k/J)|S_k|^2\). Repeating B-process or a generic
Hankel transform is therefore circular.

Every fixed difference shell is \(O(Q^2)\), and exact product-square
fibres are subdiagonal, but the signed union of \(O(Q)\) shells and the
complete twice-transformed error ledger remain open. No radial interval
or exponent has changed.

## Round 67 target-diagonal reciprocal energy (2026-08-14)

The joint reciprocal-mode problem now has an exact optimally normalized
energy. For \(J=X^{1/2}\), \(Q=J/T\), and
\(a_j=\chi_4(j)\Xi(j/J)\), weighted Cauchy reduces the required
fixed-interior bound to

\[
 \mathcal E=\sum_k w(k/Q)\left|\sum_j a_je(kX/j)\right|^2
 \ll QJX^\varepsilon.
\]

Poisson summation shows that the diagonal is already \(\asymp QJ\) and
that the off-diagonal carries the exact sign
\((-1)^{(j_2-j_1)/2}\). The accepted smooth B-process gives the
equivalent shifted square-root-product moment

\[
 \sum_{k\asymp Q}\left|\sum_{\rho\in\{1,3\}}\epsilon_\rho
 \sum_{r\asymp Q}c_\rho(k,r)
 e\!\left(2\sqrt{kX(r-\rho/4)}\right)\right|^2
 \ll Q^2X^\varepsilon.
\]

Its diagonal is also exactly the target \(\asymp Q^2\). Tested perfect
square/fourth-power fibers are only diagonal-sized, so the estimate is
not falsified. But unsigned spacing, elementary character pairing, and
all audited source theorems fail to prove the lossless signed
off-diagonal. This is the new precise bottleneck. No exponent or radial
interval changed.

## Round 66 reciprocal-mode capacity (2026-08-14)

The Round-65 unmatched crossings have an exact Vaaler Fourier interface.
After the exact wavelet averaging, the nonzero modes localize at
(k\asymp Q=J/T=X^{\nu/2}). Therefore a one-variable exponent pair
((\kappa,\lambda)) gives capacity

\[
 J^\lambda Q^\kappa
 =X^{(\lambda+\kappa\nu)/2+\varepsilon}.
\]

At \(\nu=2/5\), the audited TTY pair gives exponent
(5163/12820=0.40273\ldots), and the classical pair ((2/7,4/7))
gives (12/35=0.342857\ldots). Both lose even to the original product
bound (X^{3/10+\varepsilon}). The Fejer residual is controlled by
(X^\varepsilon(1+J/K)) and is target-safe for (K\ge X^{1/4}), but
provides no cancellation.

Thus the required new input is genuinely joint in (j,k). Its diagonal
is already of exact target size (J^{1/2}=X^{1/4}), so the off-diagonal
must be essentially lossless. No exponent or radial interval changed.

## Round 65 affine Abel and unmatched-crossing reduction (2026-08-14)

The Round-64 product wavelet now has an exact all-integer Abel form. If
(A(n)=\sum_{j\mid n}\chi_4(j)\Xi(j/\sqrt X)) for (n\geq1), zero
otherwise, and (D(n)-D(n-1)=A(n)-c_X), then

\[
 \sum_nA(n)K((n-X)/(2T))
 =\sum_nD(n)\left\{K((n-X)/(2T))-K((n+1-X)/(2T))\right\}.
\]

Here (c_X\ll_\Xi X^{-1/2}), and the affine extension to negative
integers is essential. On a positive thin interval, period-four pairing
reduces (D) to the signed symmetric difference of the (j=4r+1) and
(j+2=4r+3) crossing indicators, up to (O_\Xi(1+v/\sqrt X)).
Matched crossings cancel exactly; unmatched rows retain coefficients
(0,\pm1).

This is the smallest current arithmetic survivor. Re-inserting it into
the wavelet Abel sum self-returns, and audited short-divisor, Voronoi,
Kloosterman-fraction, and almost-all-interval results do not match the
fixed center and moving truncated character coefficient. At
(\nu=2/5), the unsaved factor remains (X^{1/20}=H/L). No radial
interval or exponent changed.

## Round 64 product-wavelet reduction (2026-08-14)

The fixed interior of the Round-63 reciprocal cone is now an exact local
product wavelet. With \(T=\sqrt{X/N}\),
\(g(t)=\mathbf1_{t>0}V(t^2)/t\), \(K=\widehat g\), and fixed
\(\Xi\in C_c^\infty((0,1))\),

\[
 \mathcal R_{X,N}[V,\Xi]
 =\sum_{n\ge1}\left(\sum_{j\mid n}\chi_4(j)\Xi(j/\sqrt X)\right)
 K\!\left(\frac{n-X}{2T}\right)+O_B(X^{-B}).
\]

Every continuous moment of \(K\) vanishes. For large \(T\), its samples
on the shifted integer lattice even annihilate every polynomial exactly.
This still does not annihilate the atomic divisor coefficient; exact
products survive, and inverse Poisson reconstructs the reciprocal cone.

The absolute ledger is \(TX^\varepsilon\), leaving the exact missing
factor

\[
 \frac{T}{X^{1/4}}=X^{1/4-\nu/2}=\rac HL.
\]

At the currently useful endpoint \(\nu=2/5\), the gap is \(X^{1/20}\).
No audited shifted-divisor, Voronoi, Kloosterman-fraction, or exponent-pair
theorem supplies it. The sharp saddle and full transition/subtraction
ledger also remain open. No exponent changed.

## Round 63 Appell and character-Poisson reduction (2026-08-14)

The subcritical one-sided divisor coefficient now has two exact
transforms. Its generating series is

\[
 \mathscr F(z)=\sum_{n\geq1}\mathcal D(n)z^n
 =\sum_{h\geq1}\frac{z^{4h^2+h}}{1+z^{2h}},
\]

and, for \(z=e^{\pi i\tau}\),

\[
 K_4\!\left(\tau,\frac{\tau}{8},
 \frac12-\frac{\tau}{8}\right)=\frac12+2\mathscr F(z).
\]

This is a moving level-four Appell section, not the tempting
\(K_4(\tau,0,1/2)\) specialization. Its exact completion contains four
theta--Mordell terms; modular appearance alone gives no radial estimate.

Independently, character Poisson summation gives a boundary-explicit
return. For the square-root radial weight, its positive-frequency
stationary main is

\[
 2X^{-1/4}e(-1/8)
 \sum_{h,j>0}\frac{\chi_4(j)}h
 V\!\left(\frac{4Xh^2}{j^2N}\right)e(Xh/j),
\]

with a target-safe square boundary and exact subtraction. The reciprocal
cone has \(X^{1/4}\) normalized absolute capacity, so signed cancellation
and uniform entry/exit control remain open. Round 63 proves a structural
reduction and a source audit, not a radial interval or a new exponent.

## Round 62 small-angle collapse (2026-08-14)

The floor-perturbed angular symbol is now eliminated on fixed
subcritical radial blocks.  With \(Y=\sqrt X\),
\(y=\lfloor\sqrt X\rfloor\), and \(d_{n,h}=2h\sqrt{X/n}\),

\[
 \Omega_X^*(n,h)=\mathbf1_{d_{n,h}\le y}^{*}
 +O\!\left(\min\{1,n/Y\}\right).
\]

For \(n\asymp X^\nu\), \(0<\nu<1/2\), the resulting coefficient is
eventually exactly

\[
 \mathcal D(n)=\sum_{\substack{hq=n\\q\ \mathrm{odd}\\q>4h}}\chi_4(q),
\]

with no floor perturbation or equality star.  The smooth radial
replacement error is \(O_V(N^{5/4}\log(2N)/\sqrt X)\), hence
power-saving for \(\nu<2/5\) and \(X^\varepsilon\)-safe at
\(\nu=2/5\).

The remaining signed one-sided divisor sum is still open and has
polynomial absolute capacity.  It is not a full \(r_2\) coefficient, so
the classical full-coefficient Voronoi formula does not close it.  No
new discrepancy exponent follows.

## Round 61 phase diagram (2026-08-14)

The lower-radial obstruction is now mapped exactly. For
\(N=X^\nu\), \(D=X^\delta\), and \(L=X^\ell\), stationary support gives
\[
 \ell=\delta+\frac{\nu-1}{2},\qquad
 \frac{1-\nu}{2}\leq\delta\leq\frac12.
\]
The accepted TTY wedge becomes \(1816\delta+89\nu\leq552\) and first
contacts active support at
\[
 (\nu,\delta,\ell)=
 \left(\frac{356}{819},\frac{463}{1638},0\right).
\]
This is only the onset of partial low-\(D\) coverage. The terminal
theorem is exactly \(\nu=1/2\), and V2 closes exactly
\((\nu,\delta)=(0,1/2)\). Every \(0<\nu<1/2\) still contains the
hard-top block \((\delta,\ell)=(1/2,\nu/2)\).

Thus no positive subcritical radial interval is yet closed. At the hard
top, the best accepted estimate misses the target by
\(X^{\min(\nu,1-2\nu)/4}\), with crossover at \(\nu=1/3\). This is a
proved reduction and no-go against a false \(356/819\) threshold, not a
new exponent.

## Round 60 breakthrough (2026-08-14)

Every fixed smooth critical radial sector is now proved target-sized. Put
\(R=X^{1/4}\), \(Y=\sqrt X\). For any fixed
\(V\in C_c^\infty((c,C))\), \(0<c<C<16\), the exact global angular
coefficient satisfies

\[
 \left|\sum_{n\le16Y}V(n/Y)\mathcal C_X^*(n)n^{-3/4}
 e(\sqrt{Xn})\right|\ll_{\varepsilon,V}X^\varepsilon.
\]

The stationary relation \(n=4Xh^2/d^2\) makes fixed
\(n/Y\asymp1\) equivalent to \(h\asymp H_j\), exactly the range covered
by the proved terminal reciprocal theorem. Mellin separation preserves
the actual height floors and profiles and costs only
\(O((1+|t|)/H_j)\) in sampled variation. The unpaired positive-frequency
transform reconstructs the radial sum with coefficient \(e(1/8)R/i\),
while the hard top, stars, and errors remain target-safe.

This removes the smooth \(n\asymp\sqrt X\) interior from GAR. The
remaining radial problem is \(n=o(\sqrt X)\), together with sharp outer
endpoint completion. M9-M1, M9, and the final exponent are still open;
the best unconditional exponent has not changed.

Round 54 now gives the exact post-scale Fejer interface. On a radial block
\(n\asymp Y\), the nonnegative diagonal-plus-correlation form must satisfy
\(\mathfrak F_{Y,R}\ll X^\varepsilon R/Y\). For
\(Y^{1/2}\le R\le Y\), it is enough to prove
\[
\left|\sum_{r<R}(1-r/R)\mathcal C_{Y,r}\right|
\ll X^\varepsilon R/Y,
\]
with the exact incidence \(h_1q_1-h_2q_2=r\). At the minimal top-block
choice \(Y\asymp\sqrt X\), \(R\asymp X^{1/4}\), this is precisely a
quadratic \(X^{-1/4}\) gain, or the missing \(X^{-1/8}\) after square root.
Termwise absolute values cannot supply it: they return normalized
\(X^{1/8}\) capacity, sharply in both coefficient-blind and actual
star-free expanded-incidence senses. No audited shifted-convolution source
matches the full moving angular symbol.

## Mathematical background and route

The accepted route has three levels:

1. `H1-H3` give the balanced hyperbola and sawtooth reductions.
2. `H4` supplies a finite Vaaler approximation, while `R5-Full` controls its Fejer residual.
3. `M9` asks for endpoint bounds for two fixed-coefficient reciprocal sums, $\mathcal M_1(D;X)$ and $\mathcal M_2(D;X)$, uniformly for $X^{1/4}\le D\le X^{1/2}$.

If H1--H4, R5-Full, and M9 all hold with their stated uniformity, the
`Conditional-bridge` yields the target. H1-H3 are proved internally.
H4 is a source-validated external dependency, with the audited paper
and normalization recorded in `sources/vaaler_1985.md`. R5-Full and
its pointwise reconciliation are now proved internally; M9 is the
remaining target-scale main-sum obligation.

## Current mathematical progress

The M2 analysis has established substantial conditional infrastructure:

- exact coefficient algebra retaining the odd-frequency character $\chi_4(h)$;
- the raw two-sided fourth-moment expansion and resonance integer $N$;
- conditional control of the total absolute $\beta$-weighted exact-resonance mass at $N=0$;
- interval URES counting infrastructure and several exact-resonance subfamilies;
- a proved conditional signed lift-cancellation estimate under explicit uniform twisted-discrepancy/BV hypotheses;
- an exact reduced-fraction pair-energy bound $\sum_r|R_\chi(r)|^2\ll_\varepsilon D^2X^\varepsilon$;
- a rigorous capacity obstruction showing that the B1 envelope alone cannot force signed off-diagonal cancellation above the $X^{1/3}$ crossover;
- a proved pointwise two-shift/divisor estimate $S_{2,L}\ll_\varepsilon X^\varepsilon(1+D/L)$, which closes the terminal frequency block $L\asymp H_D$ at $X^{1/4+\varepsilon}$ uniformly through the endpoint;
- a primary-sourced Tao--Trudgian--Yang exponent-pair wedge $178\ell+1638\delta\le463$, conditional only on the actual normalized-BV block transfer;
- an exact two-shift sine-kernel identity and a coherent bounded-weight example showing that the $D/L$ estimate cannot be improved uniformly over arbitrary bounded denominator weights;
- an explicit exact dyadic partition of the actual range $1\le d\le\lfloor\sqrt X\rfloor$, with uniform discrete BV, sampled $\ell^1$ mass $\gg D$, and a single isolated hard endpoint jump;
- a complete smooth $d$-Poisson/stationary-phase transform identifying the actual signed dual target $\mathcal T_{L,K}\ll(LK)^{3/4}X^\varepsilon$ as equivalent-hard to the remaining smooth M2 block;
- an exact one-sided transform for the hard top M1 block, including its shifted-quarter boundary series, transferred dual character $\chi_4(n)$, stationary cone $4h<n<16h$, and Vaaler-weighted error control;
- an exact common-coordinate formula for the top M1/M2 stationary pieces, together with a rigorous no-go theorem showing that their constants reinforce, their actual Vaaler profiles mismatch, and M1 has an unmatched outer wing;
- a frequency-first divisor bound $B_1(D,L;X)\ll_\varepsilon X^\varepsilon(1+D/L)$ for the actual M1 block, closing its full terminal line uniformly through the hard endpoint;
- the audited Tao--Trudgian--Yang wedge $178\ell+1638\delta\le463$ for M1 after exact resolution of the spatial character into odd residue classes;
- an exact nearest-product regrouping of the M1 residual block into a two-sided odd Vaaler kernel weighted by truncated $\chi_4$-divisor fibers;
- rigorous capacity obstructions to whole-shell kernel freezing, single-fiber character cancellation, and post-grouping $\ell^1/\ell^2$ closure;
- an exact smooth balanced small-gcd reduction to a signed difference of quarter-integer resonance packets, after square, near-square, and large-gcd sectors are removed at or below target scale;
- exact generic-band structure: equal-$2$-adic denominator fibers are sign-locked, while the unfiltered equal-dilation finite beta convolution has an $O(H^{-1/2})$ square-wave cancellation law;
- a validated conditional unit-frequency W-1 lower bound showing that character-blind absolute/unsigned fat-band control fails by a power for $D\ge X^{1/3+\delta}$, provided the actual block has sampled $\ell^1$ mass $\gg D$;
- an average-to-pointwise obstruction showing that ordinary global $L^4$ control is not enough at the endpoint.

What remains open is decisive: M9-M1 is not closed uniformly, the explicit lower/intermediate M9-M2 residual corridor has no uniform pointwise endpoint estimate, the character-sensitive near-collision bound is absent, and the final theorem cannot be promoted. The terminal block and a lower-left exponent-pair wedge are solved. At the balanced endpoint, the smooth interior core is exactly a signed outside-absolute small-gcd quarter-packet estimate. The single top denominator block now has an exact one-sided transform and reduces to a signed affine-cone estimate, which remains open.

## Current research strategy

The retired fixed four-agent panel has been replaced by one Codex coordinator and temporary, context-isolated subagents. Work is decomposed by proof interface. Each campaign freezes one obligation, preserves earlier failures as barriers, launches orthogonal discovery/no-go/control tasks, selects the smallest candidate proof kernel, and reviews distinct seams independently. Important lemmas receive a statement-only blind rederivation. Computation is used to falsify, never to certify.

Codex acts as the conductor: it designs each numbered reasoning round, distributes objectives, monitors and redirects subagents, closes the round, and alone decides the next-round strategy. Subagents stop at their assigned interface and do not advance the program autonomously.

Campaign effort follows an 80/20 rule: at least 80% analytical or algebraic reasoning and at most 20% numerical experimentation. Python and Mathematica support bounded symbolic and falsification checks. Web literature is used for strategy and method review, with exact citations and theorem-hypothesis auditing.

This architecture borrows process ideas from Anthropic's zeta-zero project—persistent coordinator, temporary workers, failure memory, adversarial controls, routed review, independent reproof, and early formalization—without importing its zeta-specific mathematics. Anthropic's announced result is not a proof of RH and is not evidence for the Gauss target.

## Immediate campaign

Round 1 (`m9-weighted-mass-adjudication`) resolved the old count-versus-weighted-mass dispute. Round 2 (`m9-unit-frequency-w1-validation`) independently proved the sharp and weighted W-1 obstruction, completed the Vaaler source audit, and replaced the old $X^{3/8}$ split by the sharper $X^{1/3}$ crossover. It also isolated the unspecified actual dyadic-weight normalization as an open infrastructure seam.

Round 3 (`m9-signed-lift-capacity`) proved B1 under exact uniform BV/twisted-discrepancy hypotheses and rejected the step from that pointwise envelope to signed fat-band cancellation. The exact pair-sum diagonal is controlled, but an envelope-saturating model has normalized critical-band size $\gg D^3/X$ above the $X^{1/3}$ crossover. The conductor's primary-literature audit also found an exact Li--Yang two-shift phase map, while verifying that the displayed Case A/B height ranges exclude the largest active M2 frequency block.

Round 4 (`m9-generic-band-signed-correlation`) closed with a new pointwise theorem. In the actual single-lift region $q\asymp D$,

$$
A_\chi(p/q)=\beta_{p,H_D}w_D(q),
$$

and B1 is sharp. Equal-$2$-adic denominator pair fibers are sign-locked, ruling out universal numerator orthogonality, while equal unfiltered dilations retain an exact square-wave convolution identity. Independently, summing each shifted frequency block first and counting $n=d(4m-\rho)$ by divisors proves

$$
S_{2,L}(D;X)\ll_\varepsilon X^\varepsilon(1+D/L).
$$

At $L\asymp H_D=DX^{-1/4}$ this is the desired $X^{1/4+\varepsilon}$ bound, pointwise and uniform at $D=X^{1/2}$.

Round 5 (`m9-frequency-phase-diagram`) is complete. It froze

$$
D=X^\delta,\qquad L=X^\ell,\qquad
\frac14\le\delta\le\frac12,\quad
0\le\ell\le\delta-\frac14,
$$

and combined every justified direct, exponent-pair, and transformed estimate.
The Tao--Trudgian--Yang pair proves

$$
178\ell+1638\delta\le463.
$$

Together with the terminal line and the point $(1/2,0)$, this leaves

$$
\mathcal U=
\{(\delta,\ell):0\le\ell<\delta-1/4,\
178\ell+1638\delta>463\}\setminus\{(1/2,0)\}.
$$

The two shifts reinforce odd frequencies and cannot improve $D/L$ uniformly
over bounded weights. Smooth Poisson summation is now complete, but its
signed $(LK)^{3/4}$ product-phase target is equivalent to the original smooth
block rather than an easier reduction.

Round 6 (`m9-endpoint-fixed-profile-attack`) constructed the actual dyadic
profiles and attacked the balanced endpoint in both the direct sine and dual
coordinates. It did not close a new endpoint range. It found that localized
fixed-profile annuli still saturate the $D/L$ scale and reduced the smooth
dual core to small gcds and quarter-integer resonances.

Round 7 (`m9-endpoint-kernel-validation`) independently rederived the
profile certificate and signed packet identity. The graph now accepts the
uniform BV, sampled mass, height rounding, and inactive-tail bounds, so the
TTY wedge and Round-5 residual phase diagram are unconditional for the chosen
partition. It also accepts the smooth small-gcd packet reduction. Hostile
review corrected two scopes: the $D/L$ result is only for a fixed one-sign
endpoint-interior subtotal, and the logically weakest packet target is

$$
\left|\sum_{G<L^{1/2}}G\mathscr P_G\right|
\ll_\varepsilon L^{3/2}X^\varepsilon,
$$

not the stronger shellwise sum of absolute values. The packet estimate and
the hard top endpoint estimate remain open.

Round 8 (`m9-top-endpoint-transform`) closed the hard endpoint-transform
seam. For odd surviving $h$, the endpoint stationary threshold is uniformly
separated from the integers; finite one-sided Poisson summation yields the
explicit boundary

$$
\frac{e(hX/(4y))}{1-e(hX/(4y^2))}
$$

and the exact cone $\lceil h/4\rceil\le m\le h$. The boundary and transform
errors are target-sized after the actual Vaaler weights. The remaining top
target is the signed affine-cone bound
$\mathcal T_L^{\rm end}\ll L^{3/2}X^\varepsilon$; no cancellation theorem
for it has yet been proved.

Round 9 (`m9-combined-top-cones`) derived the corresponding one-sided top
M1 transform. In common product coordinates, the M1 cone fills the interval
below the M2 affine cone for odd outer frequencies $r\le H$, and both pieces
have leading constant $-2e(1/8)X^{1/4}/\pi$. This is reinforcement, not
cancellation. The M1 Vaaler factor is on the inner variable, the M2 factor is
on the outer variable, the natural reflection is not an odd-lattice
involution, and M1 has an unmatched $H<r<16H$ wing. The graph now accepts the
exact transform and piecewise kernel but keeps both signed cone estimates,
M9-M1, M9-M2, M9, and the final target open.

Round 10 (`m9-m1-frequency-phase-diagram`) established the first complete
parameter map for M1. Summing the actual Vaaler frequency block first and
grouping each denominator by the nearest integer product proves

$$
B_1(D,L;X)\ll_\varepsilon X^\varepsilon(1+D/L),
$$

which closes every terminal block $L\asymp H_D$ through $D=X^{1/2}$. The
audited TTY pair closes the same wedge as for M2, and the full
second-derivative estimate closes $(1/2,0)$. The exact remaining region
relative to these methods is

$$
\mathcal U_1=
\{0\le\ell<\delta-1/4:\ 178\ell+1638\delta>463\}
\setminus\{(1/2,0)\}.
$$

The next mechanism must retain cancellation in the short-interval
$\chi_4$-divisor coefficient before the last triangle inequality, or prove
an equivalent signed product-phase estimate. M9-M1 and the final theorem
remain open.

Round 11 (`m9-m1-near-product-character-kernel`) derived that retained
object exactly. After pairing positive and negative frequencies, the kernel
is odd, so exact products vanish. The exact residual sum is over near
products $n=dm$ with weight

$$
\chi_4(d)w_D(d)\mathcal V_{L,H}((X-n)/d).
$$

Whole-shell replacement by an $n$-only divisor coefficient has order-one
error at the critical scale. Individual fibers can be singleton or
sign-locked, and prime-product families force natural-size grouped
$\ell^1/\ell^2$ mass. Thus the first viable lemma is cancellation between
different nearby products, not cancellation inside each divisor fiber. An
exact-square endpoint family confirms that such cross-product character
cancellation can occur for the actual profile. No new point of
$\mathcal U_1$ is closed yet.

Round 12 (`m9-m1-cross-product-offset-pairing`) tested the most immediate
cross-product symmetry. Moving an arbitrary real phase center to the nearest
half-lattice point costs only $O(L+X^\varepsilon)$, including at the hard
top endpoint. At that center, however, the lower and upper nearest-product
divisor fibers at offset $u$ are exactly disjoint: a common denominator
would divide $2u$ while the nearest-product cutoff forces it to exceed
$2u$. The divisibility congruence also reverses the upper kernel sign, so
the outer oddness sign reverses again. Opposite offsets therefore
reconstruct the original M1 sum rather than cancel it. The graph now rejects
same-denominator reflection and separate-fiber norm arguments and records
the precise open annular paired shifted-divisor correlation (PSC). No new
point of $\mathcal U_1$ is closed.

Round 13 (`m9-m1-ordered-denominator-resonance-cells`) is complete. It follows
the surviving exact-square mechanism by retaining the order of odd
denominators and absorbing the period-four character into the phase. For
odd $d$,

$$
\chi_4(d)=-i e(d/4),\qquad
g_h(d)=hX/d+d/4,
$$

so the exact two-step increment is

$$
g_h(d+2)-g_h(d)=\frac12-\frac{2hX}{d(d+2)}.
$$

The exact cell count and nonresonant estimate give

$$
B_{1,L}(D;X)\ll_\varepsilon X^\varepsilon
\min\left(D,\sqrt{LX/D}\right),
$$

which adds no point of $\mathcal U_1$. The half-integral cells are exactly
the signed M1 $B$-process modes. Grouping their product $n=hq$ leaves an
actual $\chi_4(q)$-weighted restricted divisor convolution against
$e(\sqrt{Xn})$. The phase has rank-one Hessian and constant product fibers,
so generic two-variable curvature and divisor multiplicity cannot give the
missing power. The graph records this exact dual object as RCS and keeps it
open.

Round 14 (`m9-m1-dual-r2-recombination`) is complete. It proves the exact
global active-M1 identity

$$
\sum_j\mathcal M_1(D_j;X)
=-\frac4\pi X^{1/4}\Re\left\{e(1/8)
\sum_{n\le16\sqrt X}\mathcal C_X^*(n)n^{-3/4}e(\sqrt{Xn})\right\}
+O(\log^2X),
$$

where $\mathcal C_X^*(n)$ is a floor-perturbed angular
$\chi_4$-divisor convolution. The radial monomial cancellation is exact,
and the resulting global real-part estimate is logically weaker than
blockwise M9-M1. But an exact $X=y^2,n=7$ control proves that M1 alone does
not collapse to $r_2(n)/4$. Popov's audited truncated Voronoi formula shows
that completing all angles to the full $r_2$ coefficient returns exactly to
the Hardy--Voronoi radial form of the Gauss problem. No cancellation bound
has yet been gained.

Round 15 is complete. The exact double-Mellin formula preserves the
height floors, odd character variable, product cutoff, endpoint stars, and
the unique hard-top Perron term. Centering the divisor coefficient gives

$$
a_z(n)=\sum_{hq=n}\chi_4(q)(q/h)^{z/2},\qquad
F_z(s)=\zeta(s+z/2)L(s-z/2,\chi_4),
$$

with exact completion

$$
\Lambda_z(s)=\Lambda_{-z}(1-s).
$$

Thus Voronoi duality reflects the divisor angle $z\mapsto-z$ rather than
removing it. At $z=0$ it is exactly the already rejected Hardy return.
Primary-source review found no theorem uniform enough in the two Mellin
heights or the top $1/u$ Perron mode to prove GAR.

Round 16 is complete. Finite-height reflection crosses the zeta pole, the
height Mellin pole, and the unique hard-top spatial Perron pole. Since the
completed root number is $+1$, symmetric reflected Perron sectors satisfy

$$
\mathscr P(F)+\mathscr P(F(-\cdot))=\sum_\nu c_\nu:
$$

they reconstruct the angular completion rather than cancel. Exact angular
reflection would also require the absent scale $D^\vee=4X/D$, a height
cutoff on the other divisor, and reflected floor/Vaaler profiles; it is
neither actual M1 nor actual M2. The graph now records the exact remaining
top object as a maximal actual-profile angular-sign radial correlation.

Round 17 is now complete. It proves the exact (2)-adic reflection cocycle

$$
a_{-z}(2^km)=\chi_4(m)2^{kz}a_z(2^km),\qquad m\text{ odd},
$$

and an exact norm-one projection onto the matching actual-profile
eigenspace. The opposite profile eigenspace is invisible, but this gives no
power saving. The antisymmetric coefficient kills only the joint
$(u,v)=(0,0)$ residue; the separate $1/u$ and $1/v$ axes and both generic
arithmetic poles survive. A high-$2$-adic tail has a proved
$N_X^{1/4}2^{-K}$ divisor majorant conditional on a uniform pointwise bound
for the post-residue profile kernel.

Round 18 is now complete. The direct physical scale/profile kernel is
indeed uniformly $O(\log X)$ by symmetric sine-integral and BV inversion,
including the hard endpoint half weight. The reflected non-residue term,
however, retains the joint multiplier
$G_v(1-s)K_{u+v}(1-s)$, finite horizontal sides, and an additional dual
radial index. It is a vector Hankel operator, not a scalar weight on an
original divisor incidence. This invalidates the scalar post-FE tail
promotion and keeps the full high-$2$-adic reflected tail conditional.

Round 19 is now complete. It gives the exact finite reflected vector kernel,
including the gamma quotient, arithmetic residue, dual radial index, and
all radial/outside horizontal sides. The archimedean conductor is

$$
4(1+|t+\eta/2|)(1+|t-\eta/2|),
$$

where $\eta=\Im(u+v)$. Bounded shifts reproduce the near-product return.
For large $|\eta|$, the single-transition strips
$t\approx\pm\eta/2$ sweep all hard-Perron heights, and finite horizontal
sides cannot yet be removed uniformly. Existing fixed-order Voronoi sources
do not cover this operator.

Round 20 is now complete. It proves exact diagonal single-transition normal
forms, including the unit Jacobian, bounded gamma factor, one-large gamma
power, and phase constants $+\pi/4$ and $-\pi/4$. A nested radial height can
separate horizontal sides from the transition planes, but hard radial
endpoints yield only $S^{-1}$ decay against polynomial functional-equation
growth. Absolute side deletion and absolute integration of the hard-Perron
transition traces therefore fail. The planned hostile task did not complete,
so stronger claimed side lower bounds were deliberately not accepted.

Round 21 is now complete. The finite radial Mellin transform admits an exact
arbitrary-order endpoint split $G_v=E_M+R_M$. Choosing enough subtraction
terms removes the radial horizontal sides containing $R_M$ under a nested
exhaustion. Endpoint coefficients have full weight, upper/lower side
orientation prevents automatic cancellation, and artificial poles of the
split pieces must cancel before arithmetic or axial residues are counted.
The finite endpoint boundary operator $\mathfrak T(E_M)+\mathfrak S(E_M)$
remains open.

Round 22 is now complete. Finite Cauchy algebra returns each $M=1$ endpoint
operator to an original-sector right-line Perron prefix minus its arithmetic
and artificial residue shares. The artificial residue cancels only against
the renormalized remainder, and the arithmetic ledger recombines to the
$R_1$ residue. The $x=1$ endpoint is target-safe. The $x=N_X$ endpoint is
the full Round-14 angular coefficient with the radial phase removed; its
absolute bound is only $X^{1/8}$ on the normalized scale and hence
$X^{3/8}$ physically, not target-sized.

Round 23 is complete. For fixed scale and frequency, the exact physical
$q$-profile has sampled sup norm plus total variation
$O(Q_j(h)^{-3/4})$, including the hard top jump and product half tie.
Period-four Abel summation in $q$ therefore gives a normalized $O(1)$
upper radial endpoint after the height and geometric scale sums. Restoring
the active-M1 prefactor proves physical size $O(X^{1/4})$. This is a real
closed boundary component, but not a proof of GAR or M9-M1. The next round
froze the recombined $R_1$ arithmetic residue; both diagonal transition
traces remained open at that stage.

Round 24 is complete. The recombined $R_1$ arithmetic residue returns
exactly to a physical $y$-integral. Its fixed-$y$ character amplitude has
sampled BV $O(Q^{-1})$, $Q=\sqrt{Xy}/D_j$; Abel summation and the automatic
small-$y$ threshold give normalized $O(1)$ and physical $O(X^{1/4})$.
Thus the complete radial endpoint/residue package is target-safe. The only
survivors in that transformed package are the two diagonal transition
traces. Round 25 then tested one-factor functional-equation coordinates for
those traces.

Round 25 is complete. For the terminal reflected kernel, set
\(A=s-z/2\) and \(B=s+z/2\), with heights \(\beta\) and \(\alpha\).
The exact finite one-factor identities are

$$
\zeta(1-A)X_4(B)L(B,\chi_4)
$$

on the \(\beta\)-bounded character-high trace and

$$
X_\zeta(A)\zeta(A)L(1-B,\chi_4)
$$

on the \(\alpha\)-bounded zeta-high trace. They are accepted pointwise
reductions, not estimates. The high gamma capacity remains polynomial,
sine/cosine resonance defeats coefficientwise Abel summation, and a
transition-restricted contour shift produces Cauchy--Pompeiu or strip-edge
connector terms. The \(\beta\) shift also crosses the already-ledgered
\(A=0\) arithmetic pole; \(A=1\) is removable in the completed product.
Both transition traces remain open. The next candidate is the
connector-completed \(\beta\) trace coupled to the radial and symmetric top
Hilbert operators.

Round 26 is complete. It proves the finite Cauchy--Green displacement for
an explicit beta-height mask, including the connector sign, rectangle
orientation, finite sides, negative (A=0) zeta residue, and unchanged
physical normalization. A disjoint mask

$$
\psi(\beta)(1-\psi(\alpha))
$$

has two derivative edges and crosses only an alpha-filtered share of the
accepted (R_1) residue; an isolated (R_1) displacement also crosses its
artificial pole unless (E_1+R_1) remains recombined. The Round-26
normalization audit showed that the unsplit radial transform has a (q^0)
positive-alpha stationary coefficient. The resulting finite period-four
character Dirichlet kernel has
maximal one-period (L^1) norm (O(\log Q)), and the hard top phase has the
exact parity gap

$$
|D_0-q/2|\ge\frac12 \qquad(D_0\in\mathbb Z,\ q\text{ odd}).
$$

Round 27 corrects the scope of that conclusion. The actual post-endpoint
(R_1) survivor contains an explicit (1/\rho), which contributes (q^{-1})
at a separated positive-alpha saddle. After the signed physical hard-top
PV/delta split, its two-denominator convolution supplies another inverse
frequency, giving a local (q^{-2}) coefficient. The hierarchical beta
partition and the exact recombined artificial-pole ledger are now proved.
Uniform pointwise hard-top (q)-BV before the signed split is false.

This is substantial local progress, not closure: saddle entry/exit,
nonstationary zones, the double-bounded share, full scale/height/radial
sums, endpoints, and outside sides remain open. Round 28 targets exactly
that uniform patching and summation interface.

Round 28 is complete. It proves that both signs
(\alpha=\pm\pi q\sqrt{Xx}/D_j) are stationary and derives a conditional
endpoint-uniform incomplete-Fresnel formula with no extra (q)-loss. It also
finds the decisive finite-height seam: the truncated hard-top Hilbert
integral has a nonzero logarithmic edge when its moving pole reaches
(\nu=\pm V). Therefore the local (q^{-2}) capacity cannot be extended by
stationary patching alone. The next round isolates the exact combination
of the finite (v)-vertical, oriented outside-(v) sides, axial/top/corner
residues, and the symmetric top limit.

Round 29 is complete. The standard outside-(v) sides have the same
edge-log coefficients as the original finite vertical, so they transfer the
logarithm rather than cancel it; moreover they are contour connectors, not
the omitted (|nu|>V) height tails. The exact original (mu,nu) box
nevertheless has a signed Plemelj limit. After this limit, the moving edge
is only locally logarithmic in (L=alpha-beta), although pointwise scaled
(C^2) fails. The next open kernel is therefore a distribution-first
logarithmic-amplitude two-saddle estimate retaining the exact polytope and
the local (q^(-2)) mechanism, followed by the full height and arithmetic
sums.

Round 30 is complete. It proves the sharp uniform moving-logarithm
stationary lemma: a logarithmic singularity crossing a nondegenerate saddle
costs exactly one logarithm beyond ordinary Fresnel size, uniformly at a
moving endpoint and for either Hessian sign. It also fixes the exact
finite-section delta/PV decomposition. In the actual separated R1 kernel,
the explicit height-face logarithm is locally q^(-4) (up to the sharp
logarithm), so it is not the surviving q^(-2) bottleneck. The first open
seam is now the scale-normalized BV norm of the complete regular finite
part, including masks, moving endpoint traces, the artificial-pole-safe
recombination, profiles, floors, and height tails. No full beta transition
or Gauss-circle bound has been proved.

Round 31 is complete. It rejects termwise absolute differentiation in the
coordinate mu=L-nu: the actual height-profile derivative loses one full
power of the saddle scale. Reparametrizing by physical height nu combines
that translation derivative with the moving endpoint traces. This proves a
finite-section BV lemma and the target local q^(-2) BV bound for the
separated fixed-b R1 regular kernel on both signed saddle patches. Round 40
later corrects the proof type: the conclusion survives only after its
diagonal Cauchy term is integrated signed first; the claimed pointwise
integrable majorant for the unintegrated full kernel is false. First-
and second-order omega-cutoff derivatives cancel exactly under identical
ownership. The remaining open object is one common recombined
physical-height kernel through rho=0, the v=0 axial split, finite radial
sides, and joint U,V,S exhaustion. The full beta transition and target
remain open.

Round 32 is complete. It corrects that remaining object: radial horizontal
sides and endpoint boundary functionals are different contour strata and
cannot be placed inside a pointwise terminal (L,nu) symbol. Raw hard-side
capacity even grows under absolute nesting. The accepted endpoint
subtraction/Cauchy modules must be applied first, and their already-proved
endpoint and arithmetic contributions kept separate. With identical
ownership, the omega/rho cancellation holds to every derivative order. The
next exact tasks are a mask-compatible endpoint-and-axial vector identity,
then a weighted symbol bound for the side-collapsed, endpoint-free,
axial-subtracted terminal kernel. The beta transition and Gauss target
remain open.

Round 33 is complete. It proves the finite beta-masked endpoint identity

$$
T_\xi^\beta+S_\xi^\beta+P_\xi^\beta+C_{A,\xi}^\beta
=D_\xi^\beta-A_\xi,
$$

and corrects a crucial scope error: the beta branch owns the full
$A=0$ arithmetic residue, but its endpoint prefix remains
$D_\xi^\beta=D_\xi[\psi(\beta)]$. Only the full three-mask hierarchical
sum recovers the proved unmasked endpoint module. The common same-mask rho
ownership defect and its physical-$L$ derivative vanish exactly. A finite
masked $v$-shift also creates the nonzero area connector
$\frac12\iint\psi'(\beta)Q$; a second axis shift produces connector-axis
and mixed $\psi''(\beta)/4$ strata, with the joint corner counted once.
The next exact task is to write the actual globally endpoint-collapsed,
connector-completed beta axial vector before attempting its symbol bound.
No Gauss-circle estimate is proved.

Round 34 is complete. It proves the complete finite two-axis beta
Cauchy--Green identity. Expanding the two one-axis transfers gives sixteen
strata: every boundary product, both axial families, both connector-boundary
and connector-axis families, one positive mixed \(\psi''(\beta)/4\)
product-area term, and one joint corner. Independent \(u\)-then-\(v\) and
\(v\)-then-\(u\) derivations agree, and applying the common finite operator
to the actual terminal, radial-side, arithmetic, endpoint, and artificial
strata preserves all profiles and the \(G=E_1+R_1\) cancellation. The
new exact obstruction is an order-of-limits interface: accepted endpoint
and arithmetic estimates are post-physical-limit, while radial-side
deletion is under a nested exhaustion. No theorem yet commutes the
sixteen-stratum transfer with either operation. Round 35 isolates the
radial-side exhaustion commutator first. M9-M1 and the Gauss target remain
open.

Round 35 is complete and closes the radial-side transfer commutator by an
exact support argument. The fixed beta mask is supported in
\([-2B_0,2B_0]\), while on either reflected radial side

\[
|\beta|\ge S-(U+V)/2.
\]

Thus for \(S>(U+V)/2+2B_0\), the mask and every connector derivative
vanish on an open neighborhood of the whole side product. All sixteen
transferred faces, axes, connector strata, the mixed \(\psi''/4\) area,
collisions, and the corner are identically zero; no remainder estimate is
needed and \(M=1\) suffices. The only remaining module-limit seam is now
transfer through the physical endpoint and recombined \(R_1\) arithmetic
packages. M9-M1 and the Gauss target remain open.

Round 36 is complete and closes that physical boundary-module interface by
an exact aggregate routing identity. At every finite stage, the three
hierarchical mask transfers are summed before any limit. Their first and
mixed derivative connectors cancel because the masks form a partition of
unity, while the ordinary final verticals, horizontal faces, axes, and one
corner survive as the complete unmasked finite Stokes representation. From
the original fixed-\(w\) meromorphic antecedent, this representation equals
the positive-line module

\[
\sum_{\xi\in\{1,N_X\}}D_\xi+\mathfrak R^{\rm ar}[R_1].
\]

Only after this finite equality is formed are the accepted symmetric
physical endpoint and arithmetic limits invoked, giving normalized
\(O_W(\log X)\), hence physical \(O_W(X^{1/4}\log X)\). No individual
masked face or connector limit is claimed. The exact finite endpoint-free
complement is now defined as \(V_{\rm pre}^{\rm fin}-M_{\rm fin}\); its
symmetric outside-height/profile limit is the next open interface. M9-M1
and the Gauss target remain open.

Round 37 is complete. It proves the exact finite endpoint-free identity

$$
V_{\rm ef}^{\rm fin}=T[R_1]+S[R_1]+P_\rho[R_1]
$$

on the common fixed-$w$ antecedent. Compact beta support deletes the full
transferred radial-side term, and the remaining terminal/artificial vector
has the complete sixteen-cell product Cauchy--Green ledger. At every fixed
height box, its physical top boundary is the signed distribution

$$
\frac12\delta_0-\frac{i}{2\pi}\operatorname{PV}\frac1\mu,
$$

with locally integrable moving-face logarithms. Recombining the complete
outside-face, axis, connector, mixed, and corner package by finite Stokes
reduces the global limit question to one actual-profile signed
positive-line Cauchy tail. The tail is not yet proved to vanish. A bounded
smooth counterfunctional shows that finite Plemelj convergence and local
logarithmic regularity alone cannot imply the outside-height limit. Round
38 therefore targets the exact joint beta-slab height asymptotic and this
Cauchy tail only; it does not yet attempt the terminal symbol estimate.

Round 38 is complete and closes that Cauchy tail. On the legal terminal
line \(c'=5/4\), the beta-slab change

\[
t=(\mu+\nu)/2+\beta
\]

has unit Jacobian, confines one completed factor to bounded beta height,
and leaves tangent exponent

\[
\kappa=\frac34+\frac{a+b}{2}<1.
\]

The exact coefficient powers in \(h\) and \(q\) are both absolutely
summable, while the post-endpoint radial factor supplies one inverse
\(\mu/2+\nu\) height. After the signed top delta/PV subtraction, an
elementary convolution and cubic height-profile decay give the integrable
majorant

\[
|\mathcal F_T(\nu)|\ll_{X,b}
(1+|\nu|)^{\kappa-4}\log(2+|\nu|).
\]

The artificial residue cannot use the terminal Dirichlet expansion;
keeping it recombined as \(\zeta(1-A)L(1-B,\chi_4)\) gives instead an
\(O_{X,b}((1+|\nu|)^{-3})\) tail. Axial deltas and the corner have bounded
height support, and compact beta support removes radial sides. Therefore
the endpoint-free axial vector has a unique joint height/profile limit,
and the complete connector and mask--endpoint--axial ownership interfaces
are closed. The constants remain unrestricted in \(X\). The next exact
task is the quantitative axial-subtracted terminal-symbol bound; M9-M1 and
the Gauss target remain open.

Round 39 is complete and corrects the formulation of that quantitative
task. The limiting vector is an aggregate over (j,h,q,x), so it has no
single saddle scale

\[
\lambda=\frac{\pi q\sqrt{Xx}}{D_j}.
\]

The lawful target freezes one actual signed cell, removes the complete
stationary phase, and estimates a pre-stationary-numerator mixed
physical-height symbol. The singular hard-top (u^{-1}) share alone uses
the Plemelj regularizer

\[
\mathcal R_A[H]=-\frac{iH(L,L)}{2AD}
+\frac{H(L,\nu)-H(L,L)}{(L-\nu)D};
\]

smooth top and interior profiles retain ordinary (mu)-integration. The
exact fixed-(\nu) derivative isolates the complete second translation
divided difference

\[
\frac{\partial_LH(L,\nu)-(\partial_L+\partial_\nu)H(L,L)}{L-\nu}
-\frac{H(L,\nu)-H(L,L)}{(L-\nu)^2}.
\]

This coefficient, its moving traces, and the exact normalized Morse
remainder through entry and exit are the first open quantitative kernel.
The contour normalization and singular/smooth split are now exact. Smooth
translated ridges cost at most a polylogarithmic harmonic height weight.
Conditionally on the corrected mixed norm, every leading (h,q,x,j) sum
is target-safe: the only formal radial resonance (q=2D_j) is even and is
annihilated by (chi_4), and the remaining internal sum is
polylogarithmic before the external (X^{1/4}) factor. No complete beta,
M9-M1, M9, or Gauss-circle estimate is yet proved.

Round 40 is complete. For \(y=L-\nu\) and
\(F(L,y)=H(L,L-y)\), fixed-physical-height differentiation gives

\[
\mathfrak E_H
=\int_0^1F_{Ly}(L,ty)\,dt
+\int_0^1tF_{yy}(L,ty)\,dt.
\]

The two integrals must remain recombined: on the actual translated height
profile, termwise absolute estimates lose several powers of the saddle
scale. More importantly, the independent diagonal term

\[
K_C=-\frac{iH(L,L)}{2A(L)D(L,\nu)}
\]

has a nonzero \(1/\nu\) tail, so the all-absolute terminal mixed norm and
the Round-31 full-kernel integrable-weight assertion are false. On the
physical section \(I_{U,V}(L)=[p(L),q(L)]\), however,

\[
\int_{p(L)}^{q(L)}K_C\,d\nu
=\frac{H(L,L)}{A(L)}
 \{\Log D(L,q(L))-\Log D(L,p(L))\}.
\]

For the actual separated profile this signed section has target-safe
supremum plus variation
\(O_b(\lambda^{-4}\log(2+\lambda))\), uniformly through both saddle
signs and entry/exit when Morse localization is applied after the section
is formed. This repairs the separated finite-section BV and local
\(q^{-2}\) conclusion. The complete large-alpha target is now hybrid:
signed diagonal section first, then an absolute cancellation-preserving
off-diagonal/smooth mixed norm. Exact connector, moving-trace, and Morse
control of that latter product cell remains open. Bounded-alpha,
double-bounded, complete beta assembly, M9-M1, M9, and the Gauss-circle
target remain open.

Round 41 closes that large-alpha hybrid target. On a frozen signed cell,
the exact height profile is

\[
p(\nu)=e^{i\gamma\nu}\widehat\phi(b+i\nu),
\qquad
\gamma=\log\frac{2\sqrt X(H_j+1)}{D_j\sqrt x},
\]

and the canonical phase satisfies

\[
\Psi'(L)=\log\frac{|L+\beta|}{\lambda},
\qquad
\Psi''(L)=\frac1{L+\beta}.
\]

The lower Stirling corrections stay in the normalized symbol. The genuine
height input is cubic decay with integrable derivatives; arbitrary rapid
decay is used only for the smooth spatial/top profiles. Exact endpoint
divided differences, a four-region height decomposition, moving faces,
both saddle signs, entry/exit, and the normalized Morse remainder prove
the required \(O_\varepsilon(X^\varepsilon\lambda^{-2})\) mixed norm for
the singular off-diagonal and all smooth cells. The diagonal is handled by
its signed logarithmic Cauchy section before Morse localization. The
previous coefficient-sum reduction then gives
\(O_\varepsilon(X^{1/4+\varepsilon})\) for the complete large-alpha beta
package. The bounded-alpha/double-bounded cell is now the first beta-branch
survivor; full beta assembly and the alpha-bounded branch remain open.

Round 42 derives a complete candidate proof for that double-bounded beta
cell and accepts its radial reduction. Compact beta and alpha=L+beta make
L compact; the exact gamma quotient retains its unit phase and is bounded
without Stirling. The hard top is evaluated as a signed delta/PV
distribution, giving a diagonal term plus an absolutely integrable
divided difference. The exact x derivative is multiplication by
-i((L+nu)/2+beta)/x. The h and q series converge absolutely, and the
active dyadic scales cost only a logarithm. One radial integration by
parts cancels the internal square root of X and has full endpoint
coefficients; inherited stars keep their pre-existing values.

Discovery and hostile audits independently prove the resulting
O_epsilon(X^(1/4+epsilon)) compact-cell bound and directly control its
beta-masked endpoints using the fixed-line identity R1=G-E1, without
citing the unmasked endpoint theorem. The strict isolated packet did not
list the finite post-routing connector/profile family, however, so it
could not certify one-count assembly. The graph therefore promotes only
the conditional radial-BV reduction and keeps the explicit compact cell
open for a narrow validation round. This is a validation gap, not an
identified exponent obstruction. Beta-transition assembly, the
alpha-bounded branch, M9-M1, and the final target remain open.

Round 43 tested the schematic compact family and repaired its local
analytic statement. The inherited contour must include \(a\ge0\), and the
multiplier seminorm must include \(x\partial_xM_\tau\). With those
conditions the abstract family has polylogarithmic value and
one-x-derivative norm.

The actual cell nevertheless remains open. The strict statement-only run
was contaminated by graph exposure, and the formula omits both the
\(j=0\) regular-top versus \(j\ge1\) interior selectors and the row-by-row
product Cauchy--Green ownership table. The first exact unmapped term is

\[
\frac14A_uA_v[\psi''(\beta)Q_T].
\]

Its analytic capacity is only polylogarithmic, but an unlisted term cannot
be absorbed into an exact identity. The next obligation is the finite
selector/ownership certificate and a genuinely isolated proof of the
corrected packet.

Round 44 shows that this proposed certificate was itself type-wrong. The
sixteen Cauchy--Green terms are finite Stokes representation cells, not
separately limiting physical amplitudes. They must first be summed to

\[
R_uR_v[\psi(\beta)Q_{\rm ef}],
\]

and only then split by
\(1=\chi_0(\alpha)+(1-\chi_0(\alpha))\). The mixed
\(A_uA_v[\psi''Q]/4\) term is retained in the finite representation and
is absorbed only by the complete Stokes recombination; it is never zero.
The compact positive-line terminal has exactly three selectors:
\(j=0\) singular Plemelj, \(j=0\) regular top, and \(j\ge1\) interior.

The graph now replaces the rejected rowwise table by an aggregate
positive-line localization certificate. Its remaining seams are the
oriented artificial-residue split and exact identification of the direct
positive-line complement with the accepted large-alpha package. A new
exact calculation sharply improves the first seam:

\[
\pi i\sqrt X\int_1^{N_X}x^{-1/2}e(\sqrt{Xx})\,dx
=e(\sqrt{XN_X})-e(\sqrt X),
\]

so the artificial radial coefficient is uniformly bounded. This is
candidate evidence for Round 45, not yet an accepted compact-cell theorem.

Round 45 closes that compact analytic core. After whole-vector Stokes
recombination, the central positive-line beta terminal has exactly three
selectors: the (j=0) singular top under signed Plemelj, the (j=0)
regular top, and the (j\ge1) interior profiles. Its exact amplitude obeys

\[
 \sup_x\{|\mathcal A_{\rm db}(x)|+x|\mathcal A'_{\rm db}(x)|\}
 \ll \log^C(2X),
\]

so the accepted radial-BV reduction makes it physically
(O(X^{1/4}\log^C X)). The separately owned artificial residue is also
target-safe: its local sign is positive and

\[
 \pi i\sqrt X I_1(0)=e(\sqrt{XN_X})-e(\sqrt X).
\]

Keeping its arithmetic factor as the recombined zeta--(L(\chi _4))
product, signed Plemelj plus period-four Abel summation bounds both alpha
shares by a polylogarithm. These conclusions passed discovery, clean
statement-only rederivation, hostile audit, and conductor seam review.

The full positive-line localization certificate remains open at a sharply
narrower interface. The accepted Round-41 theorem controls the signed
large-alpha saddle, entry, and exit package, but it does not explicitly
construct a finite same-antecedent partition summing to
(1-\chi _0(\alpha)) or quantitatively cover every remaining nonsaddle
tail. Round 46 targets exactly this partition-and-coverage seam; the
compact terminal and artificial residue need not be reproved.

Round 46 closes the finite partition part of that interface. The
preliminary normalized weights were not subordinate to stationary
geometry: at \(t=|\alpha|/\lambda=1\), half of the proposed outer mass
still lay at the saddle. A second smooth nonnegative partition
\(c_0+c_1+c_\infty=1\), supported respectively in
\([0,3/4]\), \((2/3,3/2)\), and \([4/3,\infty)\), gives an exact
one-count refinement of \(1-\chi_0\). The grouped inner and outer pieces
have \(|\Psi'|\ge\log(4/3)\), while every unsafe collar is assigned to
the middle group.

The quantitative nonsaddle estimate remains open, but its correct form
is now fixed. A nonsaddle cell retains the raw \(q^{-p}\) coefficient
ledger; it must not be multiplied by the Round-41 stationary numerator
or forced into the local saddle \(\lambda^{-2}\) normalization. The next
input is a global actual after-Plemelj theorem for the complete positive-
line section and its phase-conjugated x derivative, including grouped L
variation, moving traces, and outer limits. Literal equality of the new
middle group with the accepted Round-41 cutoffs, or a cutoff-invariance
theorem, is a separate remaining seam.

Round 47 closes both of those seams.  The global nonsaddle analysis must
be normalized by the intrinsic gamma height \(R=1+|\alpha|\), not by the
stationary scale \(\lambda\).  After forming the signed diagonal
logarithm, the complete section has powers

\[
 \mathcal P\ll R^{\kappa-2},\qquad
 \mathcal Q\ll R^{\kappa-1},
\]

with one additional inverse \(R\) after an \(L\)-derivative.  The exact
identity

\[
 \frac{\eta p(\nu)-\alpha p(L)}{L-\nu}
 =\alpha\frac{p(\nu)-p(L)}{L-\nu}-\frac12p(\nu)
\]

is what makes the phase-conjugated radial derivative integrable.  Moving
faces vanish in symmetric exhaustion, and both nonsaddle boundary terms
vanish because \(\kappa<1\).  The raw coefficient and radial-BV ledger is
polylogarithmic before the single external \(X^{1/4}\) factor.

The accepted fixed-ratio product-cell theorem is stable under any fixed
finite smooth scaled cutoff.  Hence the repaired middle group is covered
exactly without literal equality to an older named multiplier.  Together
with the already closed compact terminal and artificial residue, this
proves the complete returned positive-line beta localization and its
aggregate double-bounded cell.  The next task is an explicit beta-wrapper
closure audit before returning to the separate alpha-bounded branch.

Round 48 performs that closure audit.  All masks and all sixteen finite
product Cauchy--Green strata are recombined on one fixed-
\(w\) antecedent before physical limits.  Endpoint and recombined
arithmetic modules return once, radial-side cells vanish under compact
beta support, and the endpoint-free signed limit is then partitioned on
the positive line.  The exact finite residual

\[
 \mathcal R_\beta
 =\mathcal B_\beta-\mathcal M_{\rm phys}-\mathcal E_{\rm c}
 -\mathcal A_{\rho,0}-\mathcal A_{\rho,\infty}
 -\sum\mathcal E_{\rm mid}-\sum\mathcal E_{\rm ns}
\]

is identically zero.  Consequently the complete physical-height,
regular finite-part, logarithmic two-saddle, and connector beta wrappers
are now accepted in that order.  The hard-top diagonal remains signed;
no all-absolute or rowwise physical statement is introduced.

The first remaining transition object is no longer a beta residual.  It
is the separate alpha-bounded zeta-high trace

\[
 X_\zeta(A)\zeta(A)L(1-B,\chi_4),
 \qquad A=s-z/2,\quad B=s+z/2,
\]

with its connector, outside-height, \(A=0\)/\(R_1\), axial, top, and
corner ledger.  This is now an explicit graph obligation.  The swept
operator, post-FE vector kernel, M9-M1, M9, and the target remain open.

Round 49 converts that alpha trace into an exact masked cosine-comb
architecture.  In the test-distribution sense, the inverse Mellin image
of \(X_\zeta(A)\zeta(A)\) is the positive Dirac comb on the left of
\(A=0\) and the comb minus one, equivalently the unsigned cosine comb, on
the right.  The difference is the residue

\[
 \operatorname*{Res}_{A=0}\zeta(1-A)=-1.
\]

For the actual hierarchical multiplier
\(\Theta_\alpha=(1-\psi(\beta))\psi(\alpha)\), the comb is convolved in
logarithmic scale and accompanied by all finite connector, face, axis,
and corner terms.  Since \(\psi=1\) near zero, \(\Theta_\alpha\) and its
first and mixed connector derivatives vanish at \(A=0\); alpha owns no
new \(R_1\) residue.

Two tempting elementary routes are now ruled out.  At integer frequency
the Abel cosine tower is fully coherent, and the minus radial phase has
an interior stationary point, so neither coefficientwise cancellation
nor uniform radial integration by parts can close the trace.  The
unmasked lattice has normalized all-absolute capacity
\(X^{1/8+o(1)}\), while unmasking returns at best to the active angular
M1 problem modulo already accepted boundary modules.  The remaining
object is the connector-completed projected comb/GAR-return operator.
Round 50 targets the zero-mass logarithmic dilation commutator induced by
the high-pass factor \(1-\psi(\beta)\).

Round 50 shows that this mechanism is exact algebraically but insufficient
quantitatively.  With \(\lambda=\mu+\nu\), the actual multiplier is

\[
 m_\lambda(\beta)=(1-\psi(\beta))\psi(\beta+\lambda).
\]

Its inverse kernel has zero mass.  Yet when \(|\lambda|\) exceeds twice
the mask support, the high-pass equals one throughout the bounded-alpha
packet and \(m_\lambda(\beta)=\psi(\beta+\lambda)\).  The inverse is only
a modulation of a fixed low-pass kernel with fixed nonzero \(L^1\) norm.
Lattice atoms and hard floor/product-star jumps therefore receive no
packetwise saving; \(N\) separated jumps retain order-\(N\) response.

Connectors redistribute each row's jump trace but do not automatically
annihilate it.  The next exact target is local and finite: form the full
signed incidence coefficient at one actual floor, star, profile, or radial
seam, including terminal, connector, face, axis, corner, and Plemelj
contributions.  Prove that coefficient vanishes, or isolate its first
nonzero actual survivor, before returning to the global height tail.

Round 51 derives the maximal universal incidence algebra.  For a generic
moving seam, the first connectors carry delta traces and the mixed
connector carries both delta and delta-prime traces.  All sixteen finite
Stokes strata reassemble the original right-line seam with relative
coefficient \(+1\); they do not annihilate it.

The actual coefficient is nevertheless not yet defined.  The accepted
state lacks a common endpoint-free alpha numerator, a typed primal seam
map, its full jump, stratum pullbacks and velocities, and a joint rule at
seam--face--lattice--Plemelj collisions.  In particular, the symbol \(L\)
had been overloaded between the primal log-dilation coordinate and the
dual height sum \(\mu+\nu\).  Round 52 is therefore narrowed to the first
\(H_j\)-floor event and must either construct its lawful adjacent-scale
difference or prove that \(H_j\) is not a continuous seam variable at all.

Round 52 proves the latter type correction and the exact lawful discrete
replacement.  For fixed (X) and block (j),
(H_j=\lfloor D_jX^{-1/4}\rfloor) has zero contour velocity and creates no
alpha Cauchy--Green floor delta.  If

\[
 a_H(h)=\mathbf1_{h\le H}\Phi\!\left(\frac h{H+1}\right),
\]

then (a_{H+1}-a_H) is positive,

\[
 \|a_{H+1}-a_H\|_1=\frac12,
 \qquad
 \sum_h\frac{|a_{H+1}(h)-a_H(h)|}{h}\sim\frac1{H+1},
\]

and the new endpoint is only (O(H^{-2})).  This does not yet save the
alpha trace.  Exact dyadic scaling gives
(H_{j+1}=\lfloor H_j/2\rfloor), so the coefficient-only change is
(\asymp H_j) unweighted and (\asymp1) after (1/h).  The denominator
profile, support, equality star, Mellin scale powers, radial factors, and
normalization also move.  The next lawful target is therefore a signed
partial-sum theorem for the complete coupled dyadic-scale difference, not
a continuous floor-seam identity.

Round 53 completes that coupled-scale audit.  On a common finite interior
antecedent the adjacent multiplier contains

$$
2^{-u}\left(\frac{H_{j+1}+1}{H_j+1}\right)^v-1,
$$

which has order-one size at a uniformly bounded imaginary height.  After
physical return, every original scale term at a fixed lattice atom
$(h,q)$ is a nonnegative multiple of the same
$\chi_4(q)e(\sqrt{Xhq})$ phase.  The exact $W$ telescope merely moves this
mass into coherent dyadic height differences plus the hard top and inactive
bottom boundaries.

More sharply, an actual penultimate interior scale with $h=1$ contains a
strict plateau interval of odd $q$ on which exactly one scale is active and
no profile, height, top, or product star occurs.  Its adjacent difference
has normalized absolute mass

$$
\sum_q q^{-3/4}|\mathscr B_{j+1}(1,q)-\mathscr B_j(1,q)|
\gg X^{1/8}.
$$

Thus scale differencing, profile BV, and raw dyadic telescoping are now
proved incapable of supplying a power saving.  Any progress must come after
the scale sum from cancellation across distinct arithmetic/product fibers,
with the character, radial phase, projected alpha operator, connectors, and
height limits still coupled.
## Round 55 progress (2026-08-14)

The critical top-block low-angular margin is now proved target-safe. For
\(Y\asymp\sqrt X\), \(R\asymp\sqrt Y\), every length-\(R\) product
window containing the exact active profiles, floors, angular stars, and
radial star is
\(O_\varepsilon(X^\varepsilon(H+Q)Y^{-1/2})\) when restricted to
\(h\le H\) or \(q\le Q\). The full block is therefore
\(O_\varepsilon(X^\varepsilon(H+Q))\), so polylogarithmic margins are
safe. Actual angular support forces \(q\ge4h\) and \(q\ge2\sqrt n\),
making the polylogarithmic low-\(q\) margin empty. The remaining critical
problem is the intermediate-\(h\), large-\(q\) core
\((\log X)^B<h\le\sqrt n/2\), \(q=n/h\ge2\sqrt n\). No global exponent
has changed yet.
## Round 56 progress (2026-08-14)

The exact discrete curvature of the residual top-block fixed-\(h\) fibres
is now typed modulo one, but nonnegative resonance averaging is proved
incapable of closing the core. On \(h\asymp H\), its diagonal capacity is
\(\sqrt{RH}\), losing \(\sqrt H\). More sharply, for
\(R/4<h\le R/2\) each \(q\bmod4\) fibre has at most one point, and an
explicit strict fourth-power top-profile family realizes residuewise
absolute mass \(\gg R\) against the \(\sqrt R\) target. This does not
lower-bound the signed sum: the remaining mechanism is cancellation
between the two \(\chi_4\) residue classes and across distinct \(h\).
No exponent has changed.

## Round 57 progress (2026-08-14)

The first signed cross-residue interaction is now exact. On
\(R/4<h\le R/2\), every fixed-\(h\) row has zero, one, or two odd
denominators; a two-point row is the unique adjacent pair \(q,q+2\),
while a one-point row remains a full unmatched term. The paired phase
increment is \(\Theta_h(q)\asymp hR\), with no automatic control modulo
one. Smooth amplitude differences total \(O(1)\), but phase brackets,
profile/star seams, and unmatched endpoints remain.

For infinitely many fourth powers, a strict actual top-profile window has
\(\gg R\) unmatched rows of amplitude at least \(1/2\), so adjacent
pairing followed by absolute values misses the \(\sqrt R\) target by
\(\sqrt R\). This is not a signed lower bound. The exact remaining
problem is a signed cross-\(h\) hyperbola-floor/sawtooth sum. No exponent
has changed.

## Round 58 progress (2026-08-14)

The high-shell selector is now exact at the floor and Fourier levels. With

\[
 L_h={A+h-1\over2h},\quad U_h={B+h\over2h},\quad
 q_h=2\lfloor L_h\rfloor+1,
\]

and \(\nu_h=\lfloor U_h\rfloor-\lfloor L_h\rfloor\in\{0,1,2\}\), one
polynomial row identity handles empty, singleton, and adjacent-pair rows
with full artificial endpoints and all inherited stars.

The character zero mode and geometric selector zero mode are now separately
owned. More importantly, an arithmetic near-integer count proves that the
complete floor-compatible Fejer residual is

\[
 O_\varepsilon\!\left(X^\varepsilon(R/T+1)\right).
\]

Thus \(T=\lceil\sqrt R\rceil\) closes every endpoint and integer-jump
approximation error at the required shell scale. The exact survivor is the
length-\(R\) actual-symbol twisted-divisor sum

\[
 \sum_{n=A}^{B}e(\sqrt{Xn})
 \sum_{\substack{h\mid n,\ R/4<h\le R/2\\n/h\ \mathrm{odd}}}
 \chi_4(n/h)\widetilde{\mathcal A}_X(h,n/h).
\]

Its absolute capacity is still \(R\), while the target is \(\sqrt R\).
No signed estimate and no exponent improvement is yet proved. The next
round tests a coefficient-preserving quadratic completion of this exact
short divisor core.

## Round 59 progress (2026-08-14)

The high-shell divisor constraint now has an exact additive completion,

\[
 \mathbf1_{h\mid n}\chi_4(n/h)
 =-{i\over2h}\sum_{a\bmod4h}\chi_4(a)e(an/(4h)).
\]

For a smooth interior radial piece, Poisson summation with
\(r=4hk-a\) gives

\[
 n_*={4Xh^2\over r^2},\qquad f(n_*)-kn_*={Xh\over r},
\]

and the exact leading factor

\[
 2\sqrt2\,e(1/8)\chi_4(r)
 {X^{1/2}h^{1/2}\over r^{3/2}}.
\]

The saddle relation \(2h\sqrt{X/n_*}=r\) restores the complete actual
denominator profile, height floor, hard top, and star. Thus the completion
is an exact coefficient-level return to the terminal M1 reciprocal phase.

It does not yet save the short window. A length-\(R\) primal interval
produces an \(R\)-wide dual interval for each of \(R\) rows, hence raw
capacity \(R^2\); the required raw signed bound is \(O(RX^\varepsilon)\).
The sheared Hessian has determinant \(\asymp-1\) and two opposite
order-one eigenvalues, but the exact integer phase \(uv\) shows that this
alone implies no lattice cancellation. A full hard-symbol B-process and
the signed reciprocal-strip theorem remain open. No exponent has changed.

## Round 69 progress (2026-08-14)

The weaker direct square-root-product form before Cauchy now has a strict
fixed-interior improvement. Two-dimensional character Poisson, with the
complete actual ratio symbol and a summed stationary-symbol ledger, gives

\[
 \mathcal T_Q\ll
 Q^{3/2}J^{-1/2}(1+J/Q)X^\varepsilon.
\]

At (Q=X^{1/5}), this is (X^{7/20+\varepsilon}), improving the
trivial (X^{2/5}). The desired direct target is (X^{3/10}), so the
exact remaining gap is (X^{1/20}). The dual object is again the signed
fixed-centre product wavelet of length (J/Q); its absolute capacity is
sharp within the actual symbol class. All audited bilinear, root-spacing,
exponent-pair, short-divisor, and Voronoi imports are nonclosing. No final
exponent has changed.

## Round 70 progress (2026-08-14)

The delta/Salié route is now resolved to its first genuinely new
arithmetic interface. Exact offset Poisson summation localizes the
circle variable to \(\|\alpha\|\asymp T^{-1}\). At the natural Farey
order \(R=Q<T\), only the \(0/1\) cell survives, so the construction is
exactly the already accepted two-dimensional Fourier self-return.

At conductor order \(J\), nonzero moduli satisfy

\[
 T\ll c\ll J,\qquad
 \min(a,c-a)\ll c/T,\qquad
 c/T<\sqrt c.
\]

The exact residue algebra gives ordinary Kloosterman factors for odd
moduli after counterfactual completion and conductor-\(4\) twisted
factors for even moduli. The double zero mode vanishes, but axial modes
and gcd degenerations survive. Because the actual numerator is shorter
than \(\sqrt c\), completion plus Weil is non-improving, and standard
Kuznetsov does not match the moving incomplete numerator.

The next analytic object is a joint modulus, short-numerator, and
dual-frequency large-sieve estimate with the actual weights. It still
must save \(T/J^{1/2}=X^{1/20}\). No final exponent has changed.

## Round 80 progress (2026-08-16)

The residual M2 strict-metric parity proposal has been resolved exactly.
For \(\theta=\Lambda/k\), the complete Round-77 coefficient satisfies

\[
 \mathfrak B^\circ(g)=e(g\theta/2)\mathfrak C^\circ(g).
\]

Hence, if \(\theta=\ell+\eta\) and \(g\) is odd,

\[
 (-1)^{q+\ell}\mathfrak B^\circ(g)e(-g\eta/2)
 =(-1)^q\mathfrak C^\circ(g).
\]

The quotient sign \((-1)^{p/k}\) cancels pointwise. The same carrier
restores the integer Fourier modes of the period-one metric window,
including its \(r=0\) density term. Under \(h=ga\), \(s=gb\), and
\(x=gu\), the remaining sign is exactly
\(\chi_4(h)\chi_4(s)\), and the integral returns to the original
transposed character kernel.

Thus quotient parity, a half-frequency spectral gap, discrepancy alone,
and another reciprocal Poisson step are now rigorously excluded. No new
hard range closes: the accepted block bound remains

\[
 L^2X^\varepsilon\sqrt{AJD^3/L^3}.
\]

The honest M2 survivor is the complete cross-row density--discrepancy
correlation itself. M9-M2, M9-M1, M9, and the global exponent remain
open.

## Round 81 progress (2026-08-16)

The fixed-interior M1 Farey transition is now flattened at the complete-
symbol level.  On every admissible residue progression,

\[
 \mathcal W(c)=\Gamma_{\epsilon,z_*}V(c)+E(c),
 \qquad
 \|V\|_\infty+\operatorname {Var}V\ll_\varepsilon X^\varepsilon,
 \qquad
 |E(c)|\ll_\varepsilon X^\varepsilon\sqrt{C/J}.
\]

The exact moving Farey boundary and all first stationary corrections are
retained in \(E\).  The raw transition itself can have total variation
\(\asymp\sqrt{J/C}\), so it cannot be used as an Abel weight; only the
neighbor-independent principal coefficient \(V\) is globally BV.

Bourgain's audited reciprocal exponent pair then gives

\[
 \sum_{b\asymp C/T}|S_b|^2
 \ll_\varepsilon X^\varepsilon
 \left({C^3\over TQ^{5/12}}+{C^4\over TJ}\right),
\]

which is target-safe through \(C\le J^{13/18}\).  This strictly improves
the earlier \(J^{32/45}\) fixed-interior boundary.  The remaining M1
fixed-interior corridor is \(J^{13/18}<C\le J\); below \(J^{3/4}\), only
the smooth nonaxial main energy remains open.  No global exponent has
changed, and M9-M2 remains at its separate cross-row energy.

## Round 82 progress (2026-08-16)

The first transition-flattened M1 residual band has been reduced to a
strictly smaller exact signed correlation.  For (B=C/T), every fixed
smooth nonaxial row has

\[
 S_b=\sum_{r\in\mathscr R_{\kappa,b}}u(r)R(r),
 \qquad
 |R(r)|\ll_\varepsilon X^\varepsilon TQ^{-5/24}.
\]

The entire same-residue energy and every fixed nonzero residue-offset
layer are

\[
 \ll_\varepsilon X^\varepsilon C^2Q^{-5/12},
\]

which is target-safe through (C\le J^{47/60}), and therefore on the
whole first residual band (J^{13/18}<C\le J^{3/4}).  The only remaining
smooth-main object is the coherent sum

\[
 \mathfrak X_C^{(\kappa,k)}=
 \sum_{b\asymp B}\sum_{r\ne s}
 u(r)\overline{u(s)}R(r)\overline{R(s)}.
\]

Absolute offset summation loses the factor (B).  A gain (B^{-1/2})
would extend the safe range to (C\le J^{56/75}); (B^{-5/9}) would
close the band.  Neither is proved.  Complete Poisson and matched
Kuznetsov--Voronoi are exact self-returns, and current bilinear
Kloosterman theorems do not match the varying-modulus product kernel.
No global exponent has changed.

## Round 88 progress (2026-08-17)

The first-band M1 cross-group survivor has been reduced twice more. Exact
coarse physical-label shells satisfy

\[
 R_*\leq\rho_*=min\!\left(M,
 \left\lfloor J^{11/30}B^{-2}\right\rfloor\right)
\]

and are target-safe by centered Fejer grouping. After deleting those
shells, complete reciprocal-mask period fibres at good primes are also
target-safe whenever

\[
 \mathfrak a\geq M^2/\rho_*^2.
\]

The local normalization was corrected: a depth-\(j\) completed trace
descends by \(p^{2j}\), not \(p^j\). Exact small-prime examples also
show that numerator coefficients alone do not determine masked period
depth.

The remaining first-band M1 operator has
\(R_*>\rho_*\) and \(\mathfrak a<M^2/\rho_*^2\), with small-prime,
nonunit, \(2\)-adic, affine, projection-only, and aperiodic pieces still
present. M9-M1, M9-M2, M9, endpoint uniformity, and the one-quarter
Gauss-circle target remain open. R5-Full reconciliation is closed. No global exponent has
changed.

## Round 89 progress (2026-08-17)

The complete bad-prime reciprocal masks are now classified at
\(p=2,3,5,7\). Each selected complete reduction-cell tensor has both
directed degrees bounded by \(M^2/\mathfrak b_\sigma\), so cells with
\(\mathfrak b_\sigma\geq M^2/\rho_*^2\) are target-safe. A nonempty
power-of-three transverse family passes all ownership gates.

The complete bad-prime/nonunit union does not close. Its top-conductor
physical capacity still exceeds the target by \(J^{1/6}\), even on an
exact lower-period \(q=8\) control. This supplies a rigorous stopping
rule: further local period peeling is no longer the active route.
Round 90 tests whether the surviving actual-symbol operator is an exact
self-return/barrier or contains a genuinely smaller signed interaction.
No global exponent has changed.

## Round 94 progress (2026-08-17)

The Round-93 global mean square now has exact discrete consequences.  The
inclusive step structure gives the sharp two-branch local bridge

\[
 |P(x)|\ll Q^{1/3}+(Q/W)^{1/2},
\]

and the integer-cell identity

\[
 \int_n^{n+1}P(t)^2dt
 =\left(P(n)-\frac\pi2\right)^2+\frac{\pi^2}{12}.
\]

Hence the quarter exponent holds on a density-one set of integers with
exceptional count \(O(Y^{1-2\eta+\varepsilon})\), and the same second
moment holds on every one-separated sample set.  No prescribed integer is
controlled.

The exact short-window kernel is a signed rational-cell square.  M1 has
frequency \(h/d\), M2 has \(h/(4d)\), and the moving profiles reduce to
only logarithmically many fixed strata for windows below \(Y^{1/2}\).
The minimax block is subcoherent below \(Y^{1/3}\), so local smoothing at
the quarter scale is already pointwise-hard.  The first genuinely
averaging open range is \(1/3<\alpha<1/2\); a target cluster bound there
would improve the uniform exponent to \(1/6+\alpha/3\).

No such cluster estimate is proved.  Existing Popov local moments return
exactly exponent \(1/3\).  M9-M1, M9-M2, both canonical cores, endpoint
uniformity, M9, and the quarter target remain open.

## Round 95 progress (2026-08-17)

The narrow repaired Li--Yang theorem is now a certified external
dependency and gives the strongest global pointwise exponent

\[
 \theta_{\rm LY}
 =\frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots.
\]

The internal \(W=Y^{7/16}\) cluster route reduces exactly to a signed
reduced-determinant correlation. Equal lifts and the diagonal are safe,
but coefficient-blind Farey spacing misses by \(Y^{19/48}\), so the
project's internal theorem remains exponent \(1/3\). The external
theorem does not close M9-M1, M9-M2, M9, or the quarter target.

## Round 96 progress (2026-08-17)

Primitive-ray \(q\)-dispersion does not automatically expose the M2
character. At fixed \(m\), legal shifts have step two and character
autocorrelation \(+1\). Fixed-\(a\) sign-changing shifts form the exact
complete actual-symbol Fejer Gram, and transform completion returns to
the accepted half-frequency / transposed two-character row.

The positive block has capacity \(L^2\sqrt\rho\). A separately estimated
zero shift permits at most \(D^{-1/2}\) gain, while hard \(q=1\) Pell
rows have \(D\asymp1\) and \(\rho\to\infty\). This certifies a scoped
route obstruction, not failure of the actual theorem.

The first strict survivor is the determinant-weighted complete
fixed-\(a\) Gram estimate at strength \(H^2E_0/\rho\). It remains open.
No global exponent changed.

## Round 97 progress (2026-08-17)

The full M2 packet bookkeeping is now exact and noncircular. After the
bottom, Fejer residual, terminal T2S, second-derivative, and TTY owners,
the residual splits physically into

\[
 \mathcal U_{\rm hard},\qquad
 \mathcal U_{\rm sm,bal},\qquad
 \mathcal U_{\rm sm,unbal}.
\]

The canonical density-discrepancy theorem owns only the first family.
Two independent smooth targets remain:

\[
 \left|\sum_GG\mathscr P_G\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon,
\qquad
 \mathcal T_{L,K}\ll_\varepsilon(LK)^{3/4}X^\varepsilon.
\]

The proved conditional assembly is

\[
 \mathrm{TOP}+\mathrm{BAL}+\mathrm{UNBAL}
 \Longrightarrow\mathrm{M9\!-\!M2}.
\]

The graph now distinguishes the proved smooth transforms from these open
estimates, removes the M9-M2 / near-collision dependency cycle, and
treats the exact \(\chi_4\) factor as a proved normalization guardrail.
M9-M2 and all downstream quarter-scale claims remain open. No global
exponent changed.

## Round 98 progress (2026-08-17)

The M1 route bookkeeping is now exact. On the direct physical route, all
accepted owners reduce blockwise M9-M1 to precisely two open estimates: the
middle/lower hard-top residual and the literal smooth residual. The canonical
first-band Gram has no accepted inverse localization to physical blocks, so it
belongs only to an alternative global angular-radial route.

On that global route, the compact critical sector is proved and the remaining
requirements are a signed lower-radial aggregate and a sharp radial-interface
aggregate. Together they imply GAR. GAR plus M9-M2 supplies an alternative
final bridge, but neither blockwise M9-M1 nor M9 follows from it.

The graph patch created eight route-interface nodes, updated twenty nodes,
rejected six false route claims, and left an acyclic dependency graph. No
analytic estimate or exponent changed. The strongest certified pointwise
exponent remains

\[
 \theta_{\rm LY}=0.3144831759740614\ldots,
\]

while the strongest internal uniform theorem remains (1/3).

## Round 99 progress (2026-08-17)

The apparent two-dimensional spectral gain in the canonical M1 hard Gram is
now rigorously classified as a self-return. After opening the complete trace,
the integral variables \(r=n+d+u\), \(s=m+d\) recover exactly the four
physical rows and the centered Fejer Gram. The Hessian determinant is real
but is just the product of the two one-row curvatures; crediting another
\(J^{-1/5}\) would double-count their transform.

Configuration-separated high traces also retain rank-one paired cycles, and
ordinary trace moments cannot mix conductor rows. The exact \(q=8,u=4\)
mode is a coherent local control. The sole unexcluded canonical route is now
the fixed actual-vector directional coefficient at \(J^{-1/6}\), with all
owners and transitions retained.

No analytic hard subrange closed. The strongest certified external exponent
remains \(0.3144831759740614\ldots\), and the strongest internal uniform
theorem remains \(1/3\).

## Round 104: uniform fixed-\(q\) rows

Round 104 promoted the uniform actual-symbol theorem

\[
 |F_a(q)|\ll_\varepsilon X^\varepsilon {L^2\over A}
\]

for every \(q\asymp D\), uniformly through both physical collars, empty
and singleton reciprocal fibres, and \(b/a\to4^{-}\). The proof retains
the metric density and every discrepancy mode.

The resulting row energy is

\[
 \sum_{a,q}|F_a(q)|^2
 \ll_\varepsilon X^\varepsilon {DL^4\over A}.
\]

Rowwise Cauchy is exactly \(D^2\) above the polynomial-shell Gram target,
so the argument closes every prescribed polylogarithmic shell and no
fixed positive-power shell. The loss is a method ceiling, not a literal
lower obstruction. The next strict M2 survivor is the complete signed
polynomial-shell cross-\(q\) correlation.

The best global exponent did not change. The certified external exponent
is \(0.3144831759740614\ldots\), and the strongest internal uniform
exponent remains \(1/3\).

## Round 100 progress (2026-08-17)

The exact \(q=8\) coherent mode has now been projected against the literal
four-row actual vector. For \(M=8N\), \(N\) odd, its normalized CRT factor
is \(c_8(u)/8=\pm1/2\), and the global \(u=0\) owner leaves both nonzero
\(u\equiv0,4\pmod8\) branches.

Opening the four local bases gives a \(\mathbb Z/4\mathbb Z\)
cross-projection

\[
 {1\over4}\sum_{k\bmod4}e_4(k)
 \widehat F_k\overline{\widehat G_k}.
\]

The only forced \(F=G\) slice is already Round-88-owned because its exact
coarse quotient is \(R_*=4\). Hence the genuine hard \(q=8\) object is the
generic odd-cofactor/conductor cross-projection, not a positive square.

This is a strict algebraic refinement but not a power saving. The canonical
directional estimate, M9-M1, M9-M2, M9, and the quarter theorem remain open.
The certified external exponent stays \(0.3144831759740614\ldots\), and the
strongest internal uniform theorem stays \(1/3\).

## Round 101 progress (2026-08-17)

The complete two-adic factor is now exact. Every nonempty \(2^\nu\)-local
mask is the full odd orbit of length \(L=2^{\nu-1}\), and its four-row
coefficient is the cyclic DFT convolution

\[
 L^{-2}\sum_{k,l}e_L(lv)\widehat w_{l-k}
 \widehat F_k\overline{\widehat G_l}.
\]

The normalized local operator is unitary and full rank. Its reciprocal
phase has guaranteed period \(1\), \(2\), or \(L/8\), depending on
\(\nu\), but the resulting affine Fourier sparsity only splits the unitary
into permuted blocks. It gives no \(J^{-1/6}\) gain.

The owner map is also corrected: the Round-100 aligned return four is
prior-owned, while higher two-part aligned or reversal terms can have long
returns and must pass their literal Round-87--89 tests. The remaining
object is one odd-cofactor/conductor fixed-vector scalar with every actual
symbol retained.

No analytic estimate or exponent changed. The strongest certified external
exponent remains \(0.3144831759740614\ldots\), and the strongest internal
uniform theorem remains \(1/3\).

## Round 102 progress (2026-08-17)

The fixed-\(a\) primitive-ray Gram is now split at the correct level.
The density carrier has the exact determinant

\[
 {g'\over k'(a+2q+2s)^{3/2}}
 -{g\over k(a+2q)^{3/2}},
\]

but the complete metric phase replaces \(g,g'\) by
\(g-2\ell,g'-2\ell'\). Thus density-only determinant separation does
not estimate the coupled density-discrepancy coefficient.

The carrier zero set has a same-squarefree-kernel classification, and
the raw near count improves from quadratic to essentially linear in
\(GK\) at the natural tube width. This does not transfer to the actual
weighted mode-resolved tube because no \(q\)-variation or operator
estimate is available.

More decisively, the residual \(q=1\) block has no nonzero shifted
correlation. Its first open theorem is the complete actual diagonal

\[
 \sum_a|F_a(1)|^2
 \ll_\varepsilon X^\varepsilon {L^4\over A}.
\]

The graph now records one proved determinant-carrier/short-ray route
obstruction and this new open diagonal-energy node. The longer-row Gram,
canonical M2 energy, M9-M2, M9-M1, M9, and the quarter target remain
open.

No global exponent changed. The strongest certified external exponent
remains \(0.3144831759740614\ldots\), and the strongest internal uniform
theorem remains \(1/3\).

## Round 103 progress (2026-08-17)

The determinant-free singleton \(q=1\) M2 row is now closed at the exact
target. The complete centered physical integral, including both moving
saddle transitions and every actual profile, has sampled-\(k\) bounded
variation

\[
 \ll_\varepsilon X^\varepsilon\sqrt{AL/J}.
\]

After expanding the full metric window, every reciprocal phase has
frequency \(\nu-g/2\). Odd lift parity gives \(|2\nu-g|\ge1\), including
for the retained density mode. Reciprocal second-derivative cancellation
therefore proves

\[
 |F_a(1)|\ll_\varepsilon X^\varepsilon {L^2\over A},
 \qquad
 \sum_{a\asymp A}|F_a(1)|^2
 \ll_\varepsilon X^\varepsilon {L^4\over A}.
\]

This bypasses the Round-80 formal carrier no-go by adding a genuinely new
actual sampled-\(k\) theorem; it does not use quotient parity as a sign and
does not delete the density mode.

The singleton node is now `proved_internal`. Polynomial-length \(q\)-rows,
the complete fixed-\(a\) Gram, canonical M2 energy, M9-M2, M9-M1, M9 and
the quarter target remain open. The strongest certified external exponent
is still \(0.3144831759740614\ldots\), and the strongest internal uniform
theorem remains \(1/3\).

## Round 104 progress (2026-08-17)

The singleton sampled-\(k\) theorem now holds uniformly on every literal
fixed row \(b=a+2q\), \(q\asymp D\).  The complete centered integral has
variation

\[
 \ll_\varepsilon X^\varepsilon\sqrt{AL/(JD)},
\]

and reciprocal curvature of every odd metric frequency yields

\[
 |F_a(q)|\ll_\varepsilon X^\varepsilon L^2/A.
\]

This closes every prescribed fixed polylogarithmic \(q\)-shell.  Direct
Cauchy misses a polynomial shell by exactly \(D^2\), so a signed
cross-\(q\) theorem remains necessary.  No exponent changed.

## Round 105 progress (2026-08-17)

The strongest rowwise maximal theorem would imply the fixed-\(a\) Gram
exactly, but it remains open.  Adjacent transport controls the centered
physical saddle and both reciprocal endpoints are monotone; the complete
mode leaves a metric residual of size \(nJ\).

The scalar \((q,k)\) Hessian is full rank, but exact primitive Mobius
decomposition followed by two scalar stationary transforms gives

\[
 -{dXn\ell\over s}-{as\over4d}+J\sqrt{an\ell}
 =-\left(J\sqrt{dn\ell/s}-{1\over2}\sqrt{as/d}\right)^2,
\]

with

\[
 e(-as/(4d))=-i\chi_4(a/d)\chi_4(s).
\]

Thus the determinant returns an odd-character reciprocal/product square
at equal carrier capacity.  This is a proved route obstruction and exact
next interface, not an owner-preserving transform theorem or an actual
lower bound.  No positive-power \(q\)-range, downstream M2 theorem, or
global exponent changed.  The certified external exponent remains
\(0.3144831759740614\ldots\), and the strongest internal uniform theorem
remains \(1/3\).

## Round 106 progress (2026-08-17)

The dual square now has the correct two-sign principal dictionary. With
\(c=\nu-\tau g/2\), \(n=2|c|\), and
\(\epsilon=\operatorname {sgn}(c)\), the signed stationary phase is

\[
 \epsilon\left(J\sqrt{dn\ell/r}
       -{1\over2}\sqrt{ar/d}\right)^2,
\]

and the three Gaussian operations have exact final unit \(e(1/8)\).
The strict smooth-interior coefficient and local \(L^2\)-density are
verified with no spare Hessian gain.

The complete physical factor is a Fresnel transition vector, not its
point value at collars or endpoints. Every literal integer owner becomes
a nonlocal Fourier-conjugated kernel with the same norm, rank and
one-count, and \(b_*\) is generally nonintegral. This proves that
pointwise owner interpolation and a terminal-M1 shortcut are invalid.

The smallest survivor is still the signed nonzero-shift fixed-\(a\)
actual Gram, equivalently the complete-Fresnel conjugated-owner vector.
No polynomial \(q\)-range, M9-M2 theorem, or global exponent changed.

## Round 107 progress (2026-08-17)

The unbalanced smooth M2 product packet now has an exact
coefficient-preserving return. Product grouping gives the moving truncated
coefficient

\[
 A_{L,K}(n)=\sum_{hk=n}\chi_4(h)a_{L,K}(h,k),
\]

whose separated Dirichlet series is
\(L(s-it_1,\chi_4)\zeta(s-it_2)\). The literal angular weights prevent an
automatic \(r_2(n)/4\) completion.

The two functional equations have root number \(+1\) and dual factor
lengths \(X/D\) and \(D\). Independently, the exact smooth character
\(h\)-process and \(k\)-Poisson normalization gives \(-i/(2\pi)\) times a
prescribed-centre truncated-divisor wavelet supported on

\[
 |dr-X|\lesssim D/L.
\]

Its absolute capacity is \(D/L\), so the missing factor is exactly

\[
 {D\over LX^{1/4}}={H_D\over L}.
\]

This becomes one only on the already terminal-owned line. No new smooth
residual corridor closes. The unbalanced target is now reduced to the
literal signed fixed-centre wavelet, or equivalently an outside-absolute
shifted product correlation.

No downstream theorem or exponent changed. The strongest certified
external exponent remains \(0.3144831759740614\ldots\), the strongest
internal uniform theorem remains \(1/3\), and the quarter target is open.

## Round 111 progress (2026-08-17)

The exact adjacent primitive-ray parity high-pass is certified, including
one orientation, zero extension, the cutoff endpoint, and a first-failure
partition of simultaneous arithmetic and support jumps.

The phase-preserving dilation has determinant one and preserves the full
continuous carrier, but it does not preserve the integer sampler. Its
exact pullback is a scaled Dirac comb. On any common interval of length
\(K\), the scaled and original combs have coefficient-blind
total-variation distance \(\asymp K\), even though
\(1-\lambda\asymp D^{-1}\).

The reciprocal endpoint slabs have width \(J/A\), the physical slabs have
width \(L/D\), and the common-band carrier changes by \(\asymp JL/A\).
Consequently the bulk route retains a factor-\(D\) deficit and separate
endpoint estimation loses at least \(D^{1/2}\). No positive-power shell
closes.

This is a proved route obstruction, not a lower bound for the actual
signed coefficient. The actual common-band scaled-comb plus one-count jump
correlation remains open. M9-M2, M9-M1, endpoint uniformity, M9, and the
quarter target are unchanged. The certified external exponent remains
\(0.3144831759740614\ldots\), and the internal uniform exponent remains
\(1/3\).

## Round 112 progress (2026-08-17)

The balanced smooth M2 quarter-packet now has an exact scoped
normalization. For one fixed physical block, smooth gcd Poisson gives the
\(1/4\)-packet minus the \(3/4\)-packet with factor \(1/(2i)\), and the
negative packet is minus the conjugate before that factor. The direct norm
has one modulus outside all internal gcd and bounded subdivision labels.

Two material one-count errors were removed. The packet transforms the full
small-gcd shell, so square and near-square prior owners require explicit
signed correction terms rather than a hidden arithmetic mask. Also,
distinct physical \(D,L\) blocks cannot cancel before the blockwise
assembly.

The frozen artifacts do not yet instantiate the finite literal atom
dictionary of profiles, floors, stars, crossings, and transform errors.
That documentary seam is now the next deliverable; after it closes, the
signed \(L^{3/2}\) packet bound remains the analytic gap. No M2 range,
M9-M1 result, or global exponent changed. The certified external exponent
remains \(0.3144831759740614\ldots\), and the internal uniform exponent
remains \(1/3\).

## Round 113 progress (2026-08-21)

The balanced smooth M2 packet now has a complete coefficientwise dictionary.
The denominator and odd-frequency partitions telescope exactly, the whole
\(d=0\) summand is defined as zero, and the normalized continuum symbol is
fixed on the positive quadrant with uniform seminorms. The physical
constant is exactly \(-e(1/8)/(2\pi)\), with the earlier outer factor four
and the two frequency signs giving \(8\Re\).

The exact identity

\[
 {K\over L}=4^j{X\over\lfloor\sqrt X\rfloor^2}
\]

reduces the persistent balanced denominator geometry to \(j=1\), plus an
isolated \(j=2\) label when \(X\) is an exact square. The smooth gcd
telescope, its scale-one bottom, high-gcd transition owner, square and
near-square corrections, residual packet, and transform error now occur in
one physical one-count equation.

The first open line is the actual signed fixed-block estimate

\[
 \left|\sum_\sigma G_\sigma
 Q_{B,\sigma}^{\mathrm{full}}(\sqrt X)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\]

This is analytical, not documentary. Round 113 gives no saving: the worst
balanced deficit remains \(X^{1/12}\). M9-M2 still has three open parents,
M9-M1 still has two standard open parents, and the global exponents remain
the internally proved \(1/3\) and repaired external
\(0.3144831759740614\ldots\); the pointwise quarter exponent remains open.
