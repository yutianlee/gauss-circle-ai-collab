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

## Round 114 progress (2026-08-21)

The literal balanced packet has now been squared without losing either gcd
lift. Its genuine diagonal is equality of the full products
\(hk=h'k'\), not equality of the primitive products, and its total
diagonal energy is \(O_\varepsilon(L^2X^\varepsilon)\).

With

\[
 \Delta=h'k'-hk,\qquad \rho=hk'-h'k,
\]

each width-\(L\) corridor has absolute energy
\(O_\varepsilon(L^3X^\varepsilon)\). The exact square-root ray identity
is certified, and the older full-symbol mean square is now connected
correctly to the balanced packet. It is a sufficient stronger estimate,
not a proved estimate and not a route to the other M2 parents.

After removing those target-safe pieces, the remaining problem is an
actual-symbol, \(\chi_4\)-twisted shifted-divisor energy on
\(|\Delta|>L\) and \(|\rho|>L\). Its coefficient-blind capacity is
\(L^4\), so determinant size alone and a uniform broad estimate are
rigorously ruled out. The next lawful attack must use the literal signed
inner correlation. The balanced \(X^{1/12}\) deficit, all M9-M1
obligations, and both global exponents are unchanged.

## Round 115 progress (2026-08-21)

The exact double-far shifted-divisor structure is now exposed. In
increment coordinates (h'=h+p), (k'=k+q),

\[
 \Delta=hq+kp+pq,\qquad \rho=hq-kp,
\]

and nonzero character factors force (p=2s) with
(\chi_4(h)\chi_4(h+p)=(-1)^s). The character therefore shifts the
Poisson lattice by one half; it does not cancel a fixed-shift fibre.

The fully assembled phase-free double-far aggregate is proved to satisfy

\[
 |M_B^{(0)}|\ll_\varepsilon L^3X^\varepsilon.
\]

This is a genuine factor-(L) saving for that mode, obtained twice by
literal character summation. It cannot be applied after taking absolute
values over residues, shifts, divisors, or shells. Subtracting it leaves
the exact oscillatory remainder

\[
 \mathcal R_B^{\mathrm{osc}}
 =\sum_{\mathrm{df}}a_B^{<}(h,k)
 \overline{a_B^{<}(h',k')}
 [e(R(\sqrt{hk}-\sqrt{h'k'}))-1],
\]

whose (O_\varepsilon(L^3X^\varepsilon)) bound is now the smallest open
balanced target.

A plain shortened Fejer step cannot reuse the two target-saturating
corridor bounds without the (L^2/H) owner amplification, and the
critical outer B-process returns a dual sum of the original length.
Continuous Hessian nondegeneracy also does not control the discrete
half-shifted aliases. These are proved route obstructions, not a lower
bound for the actual signed sum.

M9-M2 still has open TOP, BAL, and UNBAL parents. M9-M1 remains unchanged,
as do endpoint uniformity and M9. The strongest internal pointwise
exponent remains (1/3), the audited external benchmark remains
(0.3144831759740614\ldots), and the pointwise quarter exponent remains
open.

## Round 116 progress (2026-08-21)

The half-shifted Poisson chart has now been made literal through the second
gcd mask. Each odd divisor (d) produces a progression
(s=s_d+dt), a dual lattice
(lambda=(1/2-m)/d), (dL^3) aliases of amplitude
((dL)^{-1}), and a required residue phase
(s_d(1/2-\lambda)). Both far gates have exact dual images, and all
boundary, nonstationary, support-crossing, and transition pieces have
aggregate cost (O_\varepsilon(L^3X^\varepsilon)).

The resulting complete signed bulk alias kernel remains unbounded. The
round instead proves a precise no-go for the proposed standalone
mechanisms: aliaswise absolute values have (L^5) capacity;
reciprocal-frequency divisor counting returns only (L^4); spacing forces
(L^2)-sized clusters at (d=1) and a full large-sieve diagonal; and a
second B-process exactly reconstructs the original progression. The
positive row energy is a stronger nearly replicated Gram, not an
equivalent target.

Accordingly, the one-alias/reciprocal-large-sieve balanced follow-through
is parked, but BAL itself is not rejected. M9-M2 still requires TOP, BAL,
and UNBAL; M9-M1 still requires its two direct parents; endpoint uniformity
and M9 remain open. There is no exponent change: the best internal uniform
bound is (1/3), the audited external benchmark is
(0.3144831759740614\ldots), and the pointwise quarter theorem remains
open. The next bounded lane is the (W=Y^{7/16}) actual reduced-
determinant correlation, whose full target would give the internal exponent
(5/16) without closing M9.

## Round 117 update

The graded \(W=Y^{7/16}\) lane produced the first certified
coefficient-sensitive gains. A complete literal fixed-block estimate now
gives \(Y^{37/48+\varepsilon}\) at minimax, improving the earlier
\(Y^{43/48}\) capacity by \(Y^{1/8}\). On the bounded-lift top reduced-
denominator shell, reciprocal curvature gives the sharper
\(Y^{35/48+\varepsilon}\), a \(Y^{1/6}\) saving.

Neither estimate reaches the required \(Y^{1/2+\varepsilon}\): the
remaining deficits are \(Y^{13/48}\) for the complete block and
\(Y^{11/48}\) for the bounded-lift shell. Lower reduced-denominator shells
also retain a long-lift variation seam. The exact two-dimensional
half-shift transform and clean \(r_2/4\) product completion self-return
under standard norms, so those standalone mechanisms are parked.

There is no exponent change. The internal uniform theorem remains
\(1/3\), the separately audited external benchmark remains
\(0.3144831759740614\ldots\), and the pointwise quarter theorem remains
open. The next campaign combines the prescribed-centre truncated-product
survivor with the planned unbalanced M2 falsification/viability probe.

## Round 118 update

The unbalanced prescribed-centre probe is closed. On every frozen flat
smooth component it certifies

\[
 \mathscr R_{D,L}(X)
 \ll_\varepsilon X^\varepsilon
 \min\left(D/L,\sqrt{XL/D}+\sqrt{X/(LD)}\right).
\]

Writing \(a=\delta-\ell\), this saves over absolute capacity exactly for
\(a>1/3\), but its exponent \(\min(a,(1-a)/2)\) is still above \(1/4\)
at every strict residual point. Uniform finite-difference controls show
that one consecutive same-character central run is target-safe. The
integer-centre interior phase-one stationary sector is also only
\(O_\varepsilon(\sqrt{D/L}X^\varepsilon)\).

The full disconnected selector, other real-centre coherent phases,
noncentral shoulders, endpoint packages, and signed complement remain
open. Thus UNBAL, BAL, hard TOP, M9-M2, both M1 parents, endpoint
uniformity, M9, and the quarter theorem are unchanged. The internal
uniform exponent remains \(1/3\), and the audited external benchmark
remains \(0.3144831759740614\ldots\). The next core deliverable is direct
minimization of the two M9-M1 physical parents.

## Round 119 update

The direct M1 minimization is closed. For (a=\delta-\ell), every
residual block has accepted capacity exponent

\[
 \min\left(a,{1-a\over2},
 {89(1+\ell)+819\delta\over1282}\right).
\]

Its worst value is (1/3), and Round 119 verifies this separately on both
literal physical parents. The unique hard profile
(D_0=\lfloor\sqrt X\rfloor) and the first smooth profile (D_1=D_0/2)
each have a full nonterminal (L\asymp X^{1/6}) residual shell. The two
elementary rows are (X^{1/3+o(1)}), while TTY tends to
(770/1923=1/3+43/641).

On the hard cone the normalized (L^2) capacity must first be multiplied
by (X^{1/4}L^{-3/2}), giving physical
(X^{1/4}L^{1/2}\asymp X^{1/3}). Both direct parents therefore miss the
quarter target by (X^{1/12}=L^{1/2}). This is a menu-capacity
certificate, not an arithmetic lower bound.

The exact adjacent-profile telescope retains the Vaaler-height differences
and both boundary owners. Equal deficits, scale BV, and raw profile
addition do not give a connector. The canonical Gram remains nonlocal to
the direct blocks, and GAR remains a separate total-active route requiring
both its lower-radial and sharp radial/interface parents.

No analytic parent or exponent changed. The direct route is frozen unless
a new sign-sensitive (X^{1/12}) mechanism or a lawful whole-residual
theorem is supplied. The next M1 backup deliverable is to reconcile the
already proved physical upper-radial endpoint with the still-open sharp
radial/interface owner and isolate its exact remaining complement. The
internal uniform exponent remains (1/3), the audited external benchmark
remains (0.3144831759740614\ldots), and the pointwise quarter theorem
remains open.

## Round 120 update

The sharp GAR radial/interface parent is now proved. The new device is a
fixed terminal-height cutoff \(\vartheta(h/H_j)\) inserted directly into
the literal global coefficient. Its reciprocal frequency weight has BV
\(O(H_j^{-1})\), so the accepted terminal divisor theorem bounds the
positive antecedent by \(O_\varepsilon(X^{1/4+\varepsilon})\). The
coefficientwise smooth and one-sided hard transforms, including their
absolute polylogarithmic error and cotangent-boundary ledgers, give the
normalized terminal radial sum in complex modulus.

The exact stationary geometry

\[
 {hX^{1/4}\over D_j}={t\sqrt{n/\sqrt X}\over2},
 \qquad {1\over2}\leq t\leq{3\over2},
\]

shows that the terminal coefficient equals the original coefficient for
\(n/\sqrt X\geq s_0\) and vanishes below \(s_0/144\). After inserting one
fixed auxiliary compact multiplier already on the reciprocal antecedent,
the lower-cutoff part of the terminal coefficient is also target-safe.
Therefore the entire complement of a fixed lower radial cutoff is
\(O_\varepsilon(X^\varepsilon)\) at normalized scale.

For the Round-98 three-piece partition, subtracting the already proved
compact critical cells yields the exact sharp interface. This argument
does not identify the varying-phase collar with the constant-phase physical
endpoint prefix. Endpoint-boundary and \(R_1\) packages occur only in an
alternative transformed route and have multiplicity zero here.

Consequently the exact lower-radial signed aggregate is now the sole
analytic parent of GAR. GAR itself remains open and would control only the
total active M1 sum, not either blockwise M1 parent. Hard TOP, BAL and
UNBAL remain open for M9-M2, endpoint uniformity remains independent, and
there is no exponent change: internal \(1/3\), audited external
\(0.3144831759740614\ldots\), pointwise quarter open.

## Round 121 update

The entire literal lower profile/floor kernel is now reduced at the target
scale to one exact sharp denominator cone. Lower-support geometry makes
every contributing height lie strictly below its Vaaler endpoint and
excludes the inactive bottom. The quadratic factor
\(\Phi(h/(H_j+1))-1\), together with a uniform smooth two-variable
separation and the accepted frequency-first theorem, gives total error
\(O_\varepsilon(X^{1/4+\varepsilon})\). This covers the full lower
cutoff, including the part above the earlier \(n=X^{2/5}\) small-angle
threshold.

Changing only the reciprocal phase to \(N=\lfloor X\rfloor\) costs
\(O(X^{1/4})\). Exact finite Fourier completion then identifies the
remaining cone with an all-integer prescribed-centre truncated
character-divisor discrepancy against a one-sided lower-radial wavelet.
This is a target-scale equivalence, not an estimate: the sample-exact
interpolant has growing seminorms.

Adjacent mod-four pairing has a polylogarithmic amplitude seam, but the
surviving phase bracket is maximal at half-integer increment resonances.
On fourth-power controls, disjoint resonance tubes have total
post-tube-modulus capacity \(\gg X^{3/8}\), exceeding the reciprocal
target \(X^{1/4+\varepsilon}\). Thus local pairing and resonancewise
absolute norms are frozen. Cancellation jointly across heights and
resonance labels remains possible and is exactly the open theorem.

The lower-radial estimate and GAR remain open. Both direct M1 parents,
hard TOP, BAL, UNBAL, endpoint uniformity, M9, and the quarter theorem also
remain open. There is no exponent change: internal \(1/3\), audited
external \(0.3144831759740614\ldots\).

## Round 122 update

The exact Round-121 lower discrepancy is now uniformly localized.  Its
one-sided difference wavelet has the correct three Fourier ranges:
(R^{-1}) up to (|k|\asymp R), (1/|k|) through the (y)-scale, and
rapid decay beyond (y) with every power of the moving cutoff recorded.
For fixed (0<\delta<1/8), the far range (|k|>yX^\delta), central range
(|k|\leq R), aggregate (v_2\geq\lceil\log_2R\rceil), and odd
positive-character central divisor band are all target-safe.

The all-two-adic complementary formula is exact:

\[
 A_y(2^an)=\frac{r_2(2^an)}4
 -\chi_4(n)\sum_{\substack{q\mid n\\q<n/y}}\chi_4(q),
 \qquad n\text{ odd}.
\]

The complement uses the odd part (n), not the even integer (2^an),
and every hard boundary and square fixed point is now priced.  The
(n\equiv3\pmod4) branch is an exact self-return; the positive branch
retains one half of the full circle coefficient.  Low even valuations
retain the full coefficient and exact complement jointly.

The remaining lower object is a medium-index, low-two-adic cumulative
wavelet of absolute capacity (R^2) against the (R) target.  It is not
estimated.  The complement mechanism, full-circle completion, and another
Abel/Fourier return are parked.  GAR and both direct M1 parents remain
open.  Hard TOP, BAL, UNBAL, endpoint uniformity, M9, and the quarter
theorem remain open.  There is no exponent change: internal (1/3),
audited external (0.3144831759740614\ldots).

## Round 123 update

The literal flat-smooth strict-UNBAL reciprocal row is now stable under a
phase-only move from real \(X\) to any integer \(M\asymp X\): with every
amplitude and the physical denominator frozen at \(X\), the cost is
\(O_\varepsilon((1+|M-X|)X^\varepsilon)\).  This justifies floor
integerization and, at target cost, a centre with
\(2^{v_2(M)}\asymp X^{1/4}\).

The exact shifted block square has two reciprocal Fejer selectors.  A
product layer cake proves that its complete nearest-alias sector \(j=0\),
including all shifted self-correlations and off-diagonal zero aliases, is
\(O_\varepsilon(X^{1/2+\varepsilon})\) at
\(H_0=\lceil X^{1/2}/D\rceil\).  All nonzero exact aliases are globally
divisor-small, and defects \(|E|>X^{1+\rho}/L\) are rapidly small.
Consequently, for every fixed \(\eta>0\), a violation
\(|\mathscr R_X|\geq X^{1/4+\eta}\) forces a positive-real contribution
\(\gg X^{1/2+2\eta}\) in one explicit complete signed sector
\(j\ne0\), \(E\ne0\), \(|E|\leq X^{1+\eta/10}/L\).

This is an inverse reduction, not the quarter estimate.  The factor
identity \((M-jr)(M+js)-M^2=jE\) is invertible on the live sector and its
two-adic sign is exactly the original character.  Transverse Poisson modes
have size \(\nu\asymp L\), and allowed shifts create interior stationary
crossings, so the proposed fixed-alias first-derivative argument fails
without proving a lower bound.  Complete UNBAL, hard TOP, BAL, M9-M2,
both M1 routes, endpoint uniformity, M9, and the quarter theorem remain
open.  There is no exponent change: internal \(1/3\), audited external
\(0.3144831759740614\ldots\).

## Round 124 update

The complete unmasked flat-smooth shifted square now has an audited
double-character stationary transform with aggregate \(O(1)\) error.  Its
dual phase is

\[
 \Theta_{p,q,h}(k)=\sqrt M\{\sqrt{p(k+h)}-\sqrt{qk}\},
\]

and the complete product-equality sector \(p=q,h=0\) is square-target-safe.
Subtracting the already-safe Round-123 physical package after transforming
the full square gives an exact target-equivalence between the physical
near-alias survivor and the complete dual off-product aggregate
\(p=q,h\ne0\) plus \(p\ne q\).  Any fixed-power violation localizes to at
least one of these two full actual-sign sectors.

The necessary algebraic repair is that
\(\mathcal N=p(k+h)-qk\) is the phase numerator, while
\(\mathcal G=pk-q(k+h)=\mathcal N-(p+q)h\) is the alias-gradient
numerator.  Every simultaneous \(k\)-saddle has continuous physical defect
\(E_*=0\); the discrete \(E\ne0\) projector does not pass rowwise through
Poisson.  On fixed interiors, the later joint Hessian is nondegenerate but
its Legendre phase returns to the primal reciprocal phase.  The resulting
\(D^2\) and \(D^2/L\) capacities are diagnostics, not lower bounds.

Neither complete dual sector is estimated.  Flat-smooth and complete
UNBAL, hard TOP, BAL, M9-M2, both M1 routes, endpoint uniformity, M9, and
the quarter theorem remain open.  The internal exponent remains \(1/3\),
and the audited external benchmark remains
\(0.3144831759740614\ldots\).

## Round 125 update

The complete dual off-product aggregate has now been recombined into its
smallest endpoint-complete positive object. If

\[
 B_{p,n}=\sum_{a=0}^{H-1}b_{p,n+a},\qquad
 \mathcal E_\chi=C_H\sum_n
 \left|\sum_{p>0\atop p\text{ odd}}\chi_4(p)B_{p,n}\right|^2,
\]

then exact Fejer expansion gives

\[
 \mathcal S_{\rm off}=\mathcal E_\chi-\mathcal D_0,
 \qquad \mathcal D_0\ll X^{1/2}.
\]

Thus the negative side is target-safe, and the remaining theorem is the
single positive upper bound

\[
 \mathcal E_\chi\ll_\varepsilon X^{1/2+\varepsilon}.
\]

Modulo the Round-123 safe package, the physical survivor equals this
energy plus a target-sized term. Hence any fixed-power failure is positive.

Separate equal-mode and unequal-mode target bounds are not equivalent to
this problem. Two identical smooth coefficient rows in opposite
$\chi_4$ classes can make both sectors larger by a factor $H$ while their
sum is only $-\mathcal D_0$. This is a structural coefficient test, not a
counterexample to the physical array, but it rigorously rules out
sectorwise positivity or support-only arguments.

The complete fixed-mode curvature estimate is

\[
 \mathcal E_{\rm eq}
 \ll_\varepsilon X^{1/2+\varepsilon}\min\{H,Q\},
 \qquad Q=\frac{D^2}{L\sqrt X}\to\infty.
\]

Both $H$ and $Q$ tend to infinity, so this remains over target. On strict
interiors, the reciprocal B-process has coefficient $-2i/p$ and $Q$ dual
labels, but a second process returns the original block. Odd-$p$ coherence
uses a half-integer alias lattice; the earlier $4a$ lattice misses odd
aliases. At fixed $(n,d,d')$, the literal selector leaves only an
$O(1/H)$ mode interval, not a length-$L$ sum, and summing $n$ first leaves
an uncontrolled moving floor overlap. No endpoint-complete near-defect
reduction follows.

This final bounded UNBAL mechanism is therefore parked at
$\mathcal E_\chi$. Flat-smooth and complete UNBAL, hard TOP, BAL,
M9-M2, both M1 routes, endpoint uniformity, M9, and the quarter theorem
remain open. The internal exponent stays $1/3$ and the audited external
benchmark stays $0.3144831759740614\ldots$.

## Round 126 update

The bounded hard-TOP actual-vector spectral gate has closed one strict
sector.  If (A_L^\square) is the literal hard-cone matrix restricted to
entries with (hm=\square), then

\[
 \|A_L^\square c\|_2^2
 \ll_\varepsilon L^{3/2}X^\varepsilon
 \qquad (|c_h|\le1).
\]

The proof writes (m=du^2,h=dv^2) with (d) squarefree and uses
(u\le v\le2u).  This entry projection is distinct from the prior
primitive (ab=\square) off-diagonal owner.  It is removed only by the
norm triangle; the square and nonsquare matrix pieces are not orthogonal.

The proposed parity mechanism does not contract.  The actual energy is
the height Fourier density at (pi), while the adjacent high-pass has
multiplier (1-e^{i\theta}), of maximal modulus two at (pi).
Character insertion is a unitary column modulation and leaves every
ambient singular value unchanged.  A support-sharp bounded adversary
retains the full factor-(L) gap between diagonal (L^2) and coherent
energy (L^3); this is not a lower bound for the physical vector.

Every positive actual excess above the diagonal localizes, with only an
(O(\log L)) loss, to one complete signed physical-offset shell, and a
separate direct partition gives the same statement for one primitive-(q)
shell.  All one-count data remain joint.  This inverse theorem does not
estimate the selected shell, and the Round-110 completed-to-physical
comparison remains global rather than shellwise.

The exact survivor is the nonsquare actual-character vector, equivalently
the original global one-sided completed real scalar modulo a target-safe
component.  The parity-only spectral mechanism is parked.  Hard TOP,
BAL, every UNBAL owner, M9-M2, both M1 routes, endpoint uniformity, M9,
and the quarter theorem remain open.  No exponent changes: internal
(1/3), audited external (0.3144831759740614\ldots).

## Round 127 frontier selection (2026-08-23)

Round 127 evaluated the four August 21 strategy reviews and revisions
against the accepted graph, then compared exactly three live frontiers.
Hard TOP has no coefficient-blind continuation: exact phase alignment
retains \(L^3\) energy after the power-safe \(hm=\square\) entries are
removed, and product-fibre averaging fixes the coherent fibre mean.  This
does not lower-bound the literal endpoint coefficient.

The lower-GAR uncentered square function is false for the actual survivor
because of its \(kc_y\) drift.  The corrected centered energy would imply
the scalar wavelet target, and it has an exact reduced-Farey determinant
form with a safe diagonal, but it is a stronger separated norm reached by
an ambient Fourier canonicalization.  At the critical block it still asks
for the full missing factor, so it was not selected.

For the graded determinant, the scalar prescribed-centre continuation
returns exactly the present \(Y^{37/48}\) capacity.  A new local
transverse-square-variation candidate counts only
\(J_B=1+DQ_B/B^2\) lift births inside the same reciprocal window.  If its
literal coefficient norm and joint curvature inequality are proved, the
complete block improves conditionally to \(Y^{73/96+\varepsilon}\), a
\(Y^{1/96}\) saving.  The next round tests the coefficient norm first.

No new analytic parent or global exponent is proved.  The internal
baseline remains \(1/3\), the audited external exponent remains
\(0.3144831759740614\ldots\), and the quarter target remains open.

## Round 128 local lift-variation gate (2026-08-23)

The graded coefficient gate passes after one essential normalization.
The exact reduced-ray coefficient is a common \(\chi_4(g)\) lift sum of a
frequency-only sampled-BV factor times the denominator profile
\(\omega_D(gb')\).  An exact discrete Stieltjes decomposition of that
profile, followed by interval-uniform character Abel and Minkowski, proves

\[
 \|U_{i,\rho,\eta}\|_{V^2(I)}
 \ll_\varepsilon {J_B^{1/2}\over L}Y^\varepsilon,
 \qquad J_B=1+{DQ_B\over B^2},
\]

including both endpoint values, smooth and hard profiles, stars, floors,
support motion, determinant taper, divisor progressions, and shell cuts.
It holds for two exact M1 quarter-phase branches and one M2 branch.

The unsplit M1 coefficient does not obey this norm: its reduced character
has dense transverse variation \(Q_B^{1/2}/L\) even when \(J_B\asymp1\).
Writing \(\chi_4(b')\) as the difference of \(e(\pm b'/4)\) moves it
exactly into the carrier phase.  Abstract birth-count and pointwise
arguments remain false, as fixed-window phase-conjugating controls show.

The next analytic gate is the genuinely joint actual-family reciprocal
curvature inequality without the generic \(N_\rho^{1/2}\) loss.  It is
not proved.  Hence the proposed \(Y^{73/96+\varepsilon}\) complete block
bound remains conditional, and the global exponent remains \(1/3\)
internally and \(0.3144831759740614\ldots\) externally.  Both M9
components, endpoint uniformity, M9, and the quarter target remain open.

## Round 129 direct threshold curvature gate (2026-08-23)

The proposed norm-relative reciprocal-curvature estimate is false: the
exact discrete \(V^2\) dual and a real stationary-alias Stieltjes triangle
give a \(Y^{1/48}\) counterexample with both endpoint values zero.

The exact physical sum nevertheless has a stronger direct bound.  Freeze
one Stieltjes threshold, use the common lift character by Abel before a
modulus, estimate the literal floor plateaux by reciprocal curvature, and
recombine thresholds last.  The scale identity
\(N_\rho\Lambda_\rho\asymp L\rho(J_B-1)\) removes every local birth
loss and proves \(K_\rho/L\), with all aliases, stars, floors, taper,
divisor progressions, and shell owners included.

The complete outer ledger now gives

\[
 |\mathfrak O_i|\ll_\varepsilon Y^{35/48+\varepsilon}
\]

uniformly over all reduced-denominator shells.  This is a certified
\(Y^{1/24}\) improvement over the previous complete \(Y^{37/48}\)
envelope and closes the long-lift lower-shell seam.  It remains
\(Y^{11/48}\) above target, persists only to \(7/18>1/3\), and changes
no global exponent or M9 status.

## Round 130 post-inner outer-bilinear gate (2026-08-23)

The exact shell ledger is sharper than the Round-129 uniform count.  On
the half-open inner reduced-denominator shell $b'\asymp B$, the exact
Stieltjes-recombined complete lift has $g\asymp D/B$ and
$|a'|\asymp LB/D$.  Hence there are only $O(LB/D)$ inner numerators per
outer ray, and

\[
 |\mathfrak O_{i,B}^{+}|
 \ll_\varepsilon BK_BY^\varepsilon.
\]

Every lower shell gains $B/D$; the complete residual is localized to the
bounded-lift shell $B\asymp D$.  That top shell still costs
$DK_D=Y^{35/48+o(1)}$, so the complete fixed-block exponent and the
$Y^{11/48}$ target gap do not change.

The proposed positive outer energy is a genuinely stronger problem.  Its
exact resolved Gram is $H^*H$ in auxiliary coordinates or
$K_{B,+}^*K_{B,+}$ after physical reassembly; $G^2$ applies only to a
fully completed symmetric row.  Support-matched phase alignment retains
the raw $LDK_B^2$ energy and $DK_B$ scalar capacities.  This is a method
obstruction, not a lower bound for the physical coefficient.

For a fixed primitive top-shell outer ray, $n=aq-bp$ makes $p$ a
bounded-multiplicity residue lift of the determinant.  Exact M1/M2
same-denominator resonances survive, full auxiliary inversion returns the
original all-owner product wave, and product-window or unit-Hessian
positive norms are weaker than the accepted bound.  The sole graded
frontier is now the literal signed $B\asymp D$ determinant-residue scalar.

No global exponent changes: internally proved $1/3$, audited external
$0.3144831759740614\ldots$.  M9-M1, M9-M2, endpoint uniformity, M9, and
the quarter target remain open.

## Current frontier after Round 162 (2026-08-25)

Round 160 closed the UNBAL inverse-selector reciprocity probe without an
owner estimate. Exact additive reciprocity preserves the complete
centred owner and reconstructs it after the transform. The unweighted
inverse-residue matrix has Gram matrix $jI-\mathbf1\mathbf1^*$, so
scalar projective placement costs $j^{1/2-o(1)}$; the full long-frequency
compression is $\sqrt{\lceil(n-1)/j\rceil}\asymp\sqrt\Delta$. These are
route-capacity obstructions, not weighted lower bounds or vector
impossibility results. UNBAL and its parent remain open.

Round 161 rewrote the nonsquare hard-TOP owner exactly as a
squarefree-radical frequency sum. Every fixed-constant long-channel sector
$D\le CL$, equivalently fixed $t\ge\tau\sqrt L$, is target-safe, and
all exact fixed-centre base and atom collisions are classified. This gives
no near-collision gap. The first unresolved physical face is the signed
$t=1$, $D\asymp L^2$ close-factor scalar; coefficient-uniform
common-test norms saturate capacity $L^{2+o(1)}$ against target
$L^{3/2+o(1)}$.

Round 162 attacked that literal $t=1$ face. Exact character Poisson is
involutive and, after the full Möbius lcm opening, exposes a rank-one dual
product collar

\[
 |s\ell-XQR|\ll \frac{QRJ}{L},
 \qquad Q\ell\le Rs\le4Q\ell.
\]

Its positive capacity is $\sqrt{JL}$: the apparent $QR$-decay is
repaid by collar width. Product grouping returns a near-square local
$\chi_4$-divisor window, but completion adds an uncontrolled complement,
standard differencing erases the character, and the named audited source
placements restore powers above target. Hard-edge transforms and the full
signed Möbius-coupled aggregate remain open. This is a scoped no-go, not a
physical upper or lower bound.

The accepted proof infrastructure still gives the quarter theorem only
conditionally on M9. M9-M1 is open at its two direct parents, M9-M2 is
open at hard TOP, BAL, and UNBAL, endpoint uniformity is open, and hence
M9, the bridge, and the Gauss circle target remain open. The strongest
internally proved global exponent is still $1/3$; the audited external
benchmark is still $0.3144831759740614\ldots$.

## Current frontier after Round 163 (2026-08-25)

Round 163 returned to the literal squarefree \(t=1\) product coefficient
before the Möbius opening.  For each supported \(N\), any canonically
selected pair of close odd prime factors \(p,q\) with
\(\chi_4(pq)=-1\) gives an exact exchange on the complete incidence set
where exactly one of \(p,q\) lies in the character-bearing divisor.  The
exchange fixes \(N\), phase, parity, and normalization and reverses
\(\chi_4\).  Common-cell variation costs \(L^{-1/2}\), while all support
crossings occupy \(O(L^{3/2})\) lattice collars.  Hence the selected
physical sector is \(O_\kappa(L^{3/2})\), uniformly in the real centre.

This sector has no proved density.  All no-pair products and all
neither-prime or both-prime incidences remain in the exact residual
\(\mathcal S_{L,1}^{\rm rem}\).  Single-prime toggles have disjoint
physical support, normalized toggle averaging self-returns, general
exchange matchings require sign-count balance, and odd/even complements
enter excluded lower windows.  These are route obstructions, not a
physical lower bound.

The proposed next gate is an owner-complete cumulative signed-divisor or
monotone-transport analysis of the residual, with unmatched mass and the
outer \(e(J\sqrt N)\) phase retained.  Hard TOP, BAL, UNBAL, M9--M2,
both M9--M1 routes, endpoint uniformity, M9, and the quarter theorem
remain open.  The internal exponent remains \(1/3\), and the audited
external benchmark remains \(0.3144831759740614\ldots\).

## Current frontier after Round 164 (2026-08-26)

Round 164 analyzed the complete literal residual after subtracting the
accepted close-opposite-prime XOR sector exactly once.  The selected/no-pair
residual character masses are now classified exactly, and ordered Abel
summation gives the sharp zero-extended unequal-mass bound

\[
 |b_N^{\rm rem}|
 \leq\frac12\operatorname{osc}(C_N)V_N,\qquad V_N\ll1.
\]

Selector-robust odd and even four-prime controls have
\(L^{2-o(1)}\) unit-profile capacity.  This rigorously parks
coefficient-uniform positive transport, but it is not a literal profile or
oscillatory lower bound.

The outer square-root phase has been retained in an exact endpoint-safe
length-\(L\) sliding Fejer reduction.  With \(R\asymp L\), the residual
target follows from one open aggregate real-part estimate at scale
\(L^2X^\varepsilon\).  Opening its actual coefficients gives the exact
short additive product shift

\[
 d'm'-dm=r,\qquad1\leq r<R\asymp L,
\]

with both selectors, parity branches, squarefree conditions, literal
profiles, and phases retained.  This is now the first open theorem.  It
must exploit the actual residual direction before any shiftwise modulus or
positive divisor opening.

The complete residual, full \(t=1\) face, other few-point channels, hard
TOP, BAL, UNBAL, M9--M2, both M9--M1 routes, endpoint uniformity, M9, and
the quarter theorem remain open.  There is no exponent change: internal
\(1/3\), audited external
\(0.3144831759740614\ldots\), target \(1/4\).

## Current frontier after Round 165 (2026-08-26)

Round 165 proves that the residual Fejer identity is valid at every
window scale and that absolute-site parity reduces the energy to the
even-gap subsequences without endpoint loss.  At the minimal
diagonal-safe scale \(R_0=\lceil L\rceil\), the complete monotone tangent
sector has \(O(L^2)\) atoms over all shifts, and the opened
character-divisor-gcd sector satisfies

\[
 |\mathfrak C_{R_0,g\ge G_0}^{\rm rem}|
 \ll_\varepsilon L^3G_0^{-1}X^\varepsilon.
\]

Thus every fixed-fraction high-gcd sector is target-safe.  The remaining
minimal-scale frontier is the even, opposing-displacement, low-gcd
aggregate (165.K17a).

The length-\(L\) choice is not mandatory.  At maximal scale
\(R=M_L\asymp L^2\), Cauchy pays the short shifts and leaves a distinct
even medium/long aggregate (165.K26) with an \(L^3X^\varepsilon\) target.
Both sufficient estimates remain open.

No full residual, full \(t=1\), hard-TOP parent, BAL, UNBAL, M9--M2,
M9--M1, endpoint, M9, bridge, or quarter theorem is proved.  The
internally proved exponent remains \(1/3\), the audited external benchmark
remains \(0.3144831759740614\ldots\), and the target remains \(1/4\).

## Full-proof strategy after Round 166 (2026-08-26)

The standard quarter route still requires both direct M1 parents, hard TOP,
BAL, UNBAL, and endpoint-uniform assembly.  The alternative GAR bridge
replaces the direct M1 conjunction but still requires all of M9--M2; GAR
does not prove blockwise M9--M1.

Round 166 retained the minimal residual estimate (165.K17a) as the unique
next inequality.  The maximal Fejer alternative (165.K26), direct residual,
complete hard-TOP shortcut, GAR, both direct M1 parents, BAL, UNBAL, the
separate sub-one-third lane, and endpoint seam all rank below it for the next
bounded campaign.

The exact new source gate is the determinant equation
\(d'm'-dm=r\).  Grimmelt--Merikoski 2024 matches that skeleton, but no
admissible representation of the actual selector-dependent multiplier is
proved; conditional smoothing incurs \(\delta^{-1}\gtrsim1+Jr/L\), and
the variable-shift aggregate, source correlation norms, principal main term,
and endpoints remain unbounded.  Part I 2025 formally permits complex
oscillatory functions but charges their derivative norms and leaves two
positive autocorrelations.  No audited primary source proves either
residual target.

There is no proof or exponent promotion.  The resulting graph is
`9d93f058c3623b7b278aa1ccba99adcf264c2e1d45af95ffbf993a123cfa1f76`.
Internal \(1/3\), external Li--Yang
\(0.3144831759740614\ldots\), and target \(1/4\) remain distinct.

## Current frontier after Round 167 (2026-08-26)

The minimal residual K17a aggregate now has an exact finite endpoint
representation.  Ordered divisor incidences are in bijection with matrices

\[
 \begin{pmatrix}d'&d\\m&m'\end{pmatrix},
 \qquad \det=d'm'-dm,
\]

and the complete literal aggregate is one directed quadratic form
\(\langle T_{R_0,\gamma}u_L,u_L\rangle\), with every selector, endpoint,
phase, and one outer real part retained.  Its Schur capacity is still
\(L^3X^\varepsilon\), so it does not supply the missing factor \(L\).

For every fixed \(B>0\), all shifts

\[
 r\le\min\{R_0-1,\lfloor(\log X)^B\rfloor\}
\]

are now proved at the \(L^2X^\varepsilon\) target.  This is a genuine
owner-complete strict sector, but at power-scale \(L\) it leaves the main
non-polylogarithmic range.

The direct Grimmelt--Merikoski interfaces were audited and parked.  The
bare source coefficient's principal orbit sum actually vanishes; the first
failure is instead the literal selector/common-function realization, with
independent variable-determinant phase and restored-power gaps.  Part I
allows oscillatory functions but still lacks the exact raw kernel,
principal-component treatment, and target-size discrepancy correlations.
This is a route-specific no-go, not an impossibility theorem for new signed
determinant methods.

K17a, the complete residual, other hard-TOP channels, hard TOP, BAL,
UNBAL, M9--M2, both direct M1 parents, GAR, endpoint uniformity, M9, both
bridges, and the quarter theorem remain open.  Resulting graph:
`b1af2cf47d81dd96aba8941e590f8b8ec2733476af6dda78a822041f46511c31`.  Internal \(1/3\), external Li--Yang
\(0.3144831759740614\ldots\), target \(1/4\).

## Current frontier after Round 168 (2026-08-26)

The complete selector-free hard-TOP \(t=1\) scalar now has an intact
Euler product

\[
 D(s_1,s_2)=L(s_1,\chi_4)\zeta(s_2)G(s_1,s_2)
\]

with \(G\) holomorphic in \(\Re s_1,\Re s_2>1/2\).  An exact disjoint-
cardinal Mellin identity retains every hard value and gives

\[
 \mathcal S_{L,1}=R_\zeta+\mathcal I_\eta,
 \qquad R_\zeta\ll_\varepsilon L^2J^{-1}X^\varepsilon.
\]

The non-polylogarithmic frontier is the exact signed two-height estimate
\(\mathcal I_\eta\ll_\varepsilon L^{3/2}X^\varepsilon\).  On a favorable
smooth/BV model, pointwise triangle or fixed-angular mean square plus
Cauchy misses it by \(\sqrt J\), even after lawful epsilon bookkeeping.
No audited source supplies the signed nonlinear weight, and no exact
functional-equation/AFE bridge to the Round-162 collar is known.

For every fixed \(B\), the full scalar is proved in
\(L\le(\log X)^B\); for fixed \(\kappa\), so is its exact residual
complement.  This is a complete strict sector, not a polynomial-range
result.  K17a and K26 remain independent open residual routes.

Resulting graph:
`a360b2913563c9c288438751729c5033acd2e91ee613e44f171e1d31bc7441be`.
Hard TOP, BAL, UNBAL, M9--M2, both direct M1 parents, GAR, endpoint
uniformity, M9, both bridges, and the quarter theorem remain open.  No
exponent changes: internal \(1/3\), audited external
\(0.3144831759740614\ldots\), target \(1/4\).

## Current frontier after Round 169 (2026-08-26)

The Round-168 residual Euler coefficients now have an exact collapsed
Mobius law, and the two completed GL(1) equations give the exact finite
double-Poisson formula

\[
 \mathcal I_\eta=E_0+\frac i2
 \sum_{Q,R}^{\mathrm{phys}}\frac{g(Q,R)}{QR}
 \sum_{k\ \mathrm{odd}}\chi_4(k)\sum_{\ell\ne0}
 \widetilde{\mathcal B}\!\left(\frac{k}{4Q},\frac{\ell}{R}\right),
 \qquad E_0\ll L^2/J.
\]

This repairs the residue seam: the finite physical zero mode is not the
full Mellin residue, but their difference is target-safe.  The only
positive saddle is the moving product collar
\(k\ell=XQR\), \(Q\ell\le Rk\le4Q\ell\).  Substitution of the exact
coefficient law identifies the active family coefficientwise with the
accepted Round-162 character--Poisson collar.

The missing theorem is unchanged in strength: prove the single signed
nonzero-frequency aggregate at
(O_\varepsilon(L^{3/2}X^\varepsilon)) before positive norms.  Bare
dualization, favorable smooth positive capacity, and the dated audited
spectral placements do not provide it.  A bespoke signed theorem remains
possible.

Resulting graph:
`111809875d911d279ae22bee2ce44f0dba97130eeedcdca0dc65f53f163283ae`.
The polynomial (t=1) scalar and residual, K17a, K26, other hard-TOP
channels, hard TOP, BAL, UNBAL, M9--M2, both direct M1 parents, GAR,
endpoint uniformity, M9, both bridges, and the quarter theorem remain
open.  No exponent changes: internal \(1/3\), audited external
\(0.3144831759740614\ldots\), target \(1/4\).

Round 170 is active as the mandatory full-proof and current-literature
checkpoint.  Before another analytic attack it compares the exact
Round-169 signed aggregate with K17a, K26, remaining hard-TOP channels,
BAL, UNBAL, the two direct M1 owners, GAR, endpoint assembly, and every
lawful exponent connector.  It may select one Round-171 frontier but may
not promote that frontier by ranking.

## Full-proof strategy after Round 170 (2026-08-26)

Round 170 reconstructed both quarter-proof trees and repaired a material
BAL quantifier seam. The existing double-far remainder/energy nodes cover
only persistent critical \(j=1\), \(L\asymp X^{1/6}\) blocks; they do not
cover noncritical \(j=1\) scales, the exact-square \(j=2\), \(K/L=16\)
boundary, or other balanced labels. The graph now has a separate open
remaining-label connector, so the critical child can no longer silently
promote full BAL.

The selected next target is only the critical-\(j1\) oscillatory remainder
at \(L^3X^\varepsilon\). Its positive capacity is
\(L^4X^\varepsilon\). Round 171 will first test whether the exact
\((\Delta,\rho)\) factorizations support a genuine two-direction commutator
identity that preserves the full literal scalar and saves one factor \(L\).
This is a falsifiable strategy choice, not a proved identity.

K26 has the same factor-\(L\) deficit and remains a future residual frontier.
The Round-169 signed product collar, K17a, the rest of hard TOP, full BAL,
UNBAL, both direct M1 parents or GAR, endpoint uniformity, M9, both bridges,
and the quarter theorem remain open. The dated source audit found no literal
interface or unrestricted exponent update.

Resulting graph:
`4c98bb13558c06159c5ad23128c6f6ff52970db296863858832309a24a4720ac`.
Internal \(1/3\), accepted external Li--Yang
\(0.3144831759740614\ldots\), and target \(1/4\) are unchanged.

Round 171 is active on the complete zero-subtracted persistent critical
\(j=1\) scalar. Its first question is whether the exact
\((\Delta,\rho)\) factorizations support a genuine two-direction discrete
commutator with all axial and boundary terms present. The campaign must save
the missing factor \(L\) before positive norms or close with the first exact
route-specific no-go.

## Current frontier after Round 171 (2026-08-26)

Round 171 proved a sharp route-specific obstruction for the proposed local
two-defect commutator.  The multiplicity-one shift coordinates, defect
factorizations, parity law, both axes, fixed-width affine singular strips,
and actual-real endpoint-swap identity are now accepted.  The axes and
singular strips cost at most \(L^3X^\varepsilon\).

The obstacle is the complement.  Endpoint swap leaves an even-even component
with available positive capacity \(L^4X^\varepsilon\).  Away from the
singular strips, each displayed local multiplier commutator becomes an
alternating-shift tautology after division.  Exact mixed Abel summation forces
a coefficient-independent ramp of size \(L\), restoring precisely the factor
that the target needed to save.

This eliminates one natural local mechanism; it does not prove a lower bound
for the physical scalar.  Weighted, composite, or nonlocal actual-symbol
commutators remain unexcluded.  The persistent critical remainder and energy,
the remaining-label BAL connector, full BAL, hard TOP, UNBAL, M9--M2, both
direct M1 parents or GAR, endpoint uniformity, M9, both bridges, and the
quarter theorem remain open.

Resulting graph:
`c98f95b6b3500d0f48365af338e543f9a0f251b22062f3898df5f448d6b54853`.
There is no exponent improvement: internal \(1/3\), accepted external
Li--Yang \(0.3144831759740614\ldots\), target \(1/4\).

Round 172 is active on the distinct hard-TOP residual maximal-scale Fejer
alternative (165.K26).  Its exact target has positive capacity
\(L^4X^\varepsilon\) and budget \(L^3X^\varepsilon\).  The new gate takes
adjacent-scale differences of the even parity-Fejer energy, removing the
diagonal exactly and producing a signed triangular tent, equivalently a
block-versus-Haar-detail identity.  The analytic test is whether the complete
actual residual coefficient gains the missing factor \(L\) under finite
character Poisson on the common bandpass frequency before positive dual-mode
summation.  This remains a residual-only research hypothesis, not a theorem.

## Current frontier after Round 172 (2026-08-26)

Round 172 replaced the conjectural maximal-Fejer transform step by an exact
one.  The stopped parity-Fejer chain has zero-diagonal link weights, exact
doubling Haar identities, and an unrounded final link.  The complete literal
real-cardinal transform is now known, including both parity peaks, every
endpoint and transition, and constants (i/2) and (1/8).  Its entire
ordinary-zero-containing sector costs at most
(L^3X^\varepsilon) after collective signed character recombination.

The first unproved quantity is the complete signed nonzero-frequency dual
aggregate.  A linkwise (L^3X^\varepsilon) theorem would suffice, although
the exact telescope also permits cross-link cancellation.  The physical
zero diagonal is not a dual diagonal.  Coefficient-uniform positivity before
a literal-symbol gain has sharp envelope capacity (L^4X^\varepsilon), so
that route cannot supply the missing factor (L).  The obstruction is
route-scoped: a coefficient-sensitive theorem is not excluded, and K26 is
neither proved nor disproved.

Resulting graph:
`70592c104e0c149485b4fac3fe6582020767631938fe9036f204ae616f188b7f`.
The remaining (t=1) channels, hard TOP, critical and remaining-label BAL,
UNBAL, M9--M2, both direct M1 parents or GAR, endpoint uniformity, M9, both
bridges, and the quarter theorem remain open.  There is no exponent
improvement: internal (1/3), accepted external Li--Yang
(0.3144831759740614\ldots), target (1/4).

Round 173 is active on one final exact K26 gate. Fixed-product fibre
centering has already been rejected as a live mechanism: selected and
balanced no-pair zero-mass toggles cross hard support, and all-
\(1\pmod4\) no-pair rows have no target-safe positive energy estimate. The
new tangent chart instead uses
\(\chi_4(d+2s)\chi_4(d)=(-1)^s\) across different products. Its finite
alternating identity isolates a target-safe Fejer-weight commutator and one
literal actual-symbol difference remainder. The remainder must be controlled
across the complete stopped chain before any positive norm, or the campaign
will certify its first exact self-return/restored-power obstruction.

This is an identity-or-no-go experiment, not a proved K26 estimate. The
mandatory full strategy and literature review follows Round 173.

## Current frontier after Round 173 (2026-08-26)

Round 173 proved that the selected tangent-character Fejer commutator is an
exact self-return. The tangent chart is multiplicity one, the character gives
the exact factor \((-1)^s\), and the complete bandpass commutator costs at
most \(L^3X^\varepsilon\). But its complementary actual-symbol difference
reindexes coefficientwise to the sum of adjacent original Fejer weights.
Across the full stopped chain it is K26 itself modulo the paid commutator and
one target-safe short correction.

This closes one natural first-difference route, not K26. Positive variation
retains \(L^4X^\varepsilon\) top-link capacity, while the sharp abstract
diagnostic is nonliteral. Cross-link cancellation and a genuinely new signed
actual-symbol correlation remain unexcluded.

Resulting graph:
`04090ef6aa8d7d28e05a312f1f2f069fe3ab44ad62002d68d6b62c49dc0d962a`.
Hard TOP, critical and remaining-label BAL, UNBAL, M9--M2, both direct M1
parents or GAR, endpoint uniformity, M9, both bridges, and the quarter theorem
remain open. There is no exponent improvement: internal \(1/3\), accepted
external Li--Yang \(0.3144831759740614\ldots\), target \(1/4\).

Round 174 must now reconstruct the full proof graph, audit current primary
literature through 2026-08-26, and select exactly one subsequent analytic
frontier without promoting it by ranking.

Round 174 is active on the validated Round-173 graph. It is a strategy and
source checkpoint, not an analytic continuation. The three independent tasks
reconstruct the full graph frontier, audit current primary literature and the
unrestricted exponent through 2026-08-27, and perform a statement-only
Round-175 selection. No proof status changes merely because a candidate ranks
first.

## Full-proof strategy after Round 174 (2026-08-27)

Round 174 closed under `strategy_frontier_retained`. The complete graph audit
confirms a genuine logical OR. The standard route requires both direct M1
parents, hard TOP, critical BAL, remaining-label BAL, UNBAL, endpoint
uniformity, M9, and the conditional bridge. The alternative route substitutes
complete GAR only for the direct blockwise M1 conjunction; it still requires
all three M2 parents and the separate total-active bridge. GAR has no edge to
blockwise M9--M1 or M9.

No hard-TOP subroute is silently complete. K26 and K17a each close at most
the residual scalar. Full displayed \(t=1\) remains below complete hard TOP.
Hard TOP, both BAL scopes, and UNBAL are independent M2 owners. Endpoint
uniformity is an assembly seam and supplies no missing analytic saving.

The unique planned Round-175 target is

\[
 \sum_{j=0}^{K-1}\mathcal N_{R_j,R_{j+1}}
 \ll_\varepsilon L^3X^\varepsilon,
\]

the one-sided whole-chain signed nonzero ordinary-frequency K26 aggregate.
Its complete literal formula retains both parity branches, constants
\(i/2\) and \(1/8\), one outer real part, the strict terminal link, the
collectively recombined ordinary-zero sector, and the once-only short
correction. Cross-link cancellation is allowed but unproved. Positive
coefficient-insensitive closure has \(L^4X^\varepsilon\) capacity, leaving
one factor \(L\) to save through a property of the actual residual symbol.

The repaired source audit is current through 2026-08-27 and finds no exact
match to a live project interface. The fixed-modulus Blomer--Pascadi
specialization is legal for every centre after symmetry and zero padding but
restores above target and retains the wrong absolute-value interface. The
repaired Li--Yang preprint dependency remains the strongest audited
unrestricted pointwise result.

Resulting graph:
`e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211`.
No proof status or exponent changes. The internal exponent is \(1/3\), the
accepted external exponent is \(0.3144831759740614\ldots\), and the target
is \(1/4\). The Gauss circle conjecture remains open.

Round 175 is now active on that graph. It tests only the exact one-sided
whole-chain K26 nonzero-frequency inequality at \(L^3X^\varepsilon\), with
the full literal residual symbol and complete endpoint ledger. The round
must expose a genuine coefficient-sensitive saving before positivity or
certify the narrowest exact scale/capacity self-return. Launch itself changes
no proof status or exponent.

## Current frontier after Round 175 (2026-08-27)

Round 175 proves that the proposed whole-scale K26 resource is an exact
endpoint coboundary:

\[
 \sum_{j<K}\mathcal N_{R_j,R_{j+1}}=Q_M^*-Q_{R_0}^*,
 \qquad Q_{R_0}^*\ll_\varepsilon L^3X^\varepsilon.
\]

The collectively restored ordinary-zero sector and once-only short
correction are target-safe, so this one-sided chain target is equivalent to
K26 and to the unproved literal endpoint estimate
\(Q_M^*\ll_\varepsilon L^3X^\varepsilon\). Coefficient-independent
positivity stops at \(L^4X^\varepsilon\). Hence scale-only Abel, Haar,
martingale, and positive closures are now rigorously parked; a direct
coefficient-sensitive endpoint theorem remains possible.

The graph now contains one additional proved-internal route obstruction and
has SHA-256
`9409651dccbbd1c69547546b245ba04c21d2a280173733ae37b693f9894c8b03`.
No target estimate or parent status changed. The preferred next rotation is
the independent non-polylogarithmic K17a variable-determinant residual
aggregate, but Round 176 is not launched.

The full conjecture remains open. M9--M1 and M9--M2 are both open; endpoint
uniformity and M9 are open; both bridges remain conditional. The exponent
ledger is unchanged: internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), target \(1/4\).
## Round 176 active frontier (2026-08-27)

Round 176 rotates from the parked K26 scale resource to the independent
non-polylogarithmic K17a determinant aggregate. In a cross-gcd coordinate,
each parity-preserving determinant fibre has an exact character
half-frequency \((-1)^t\). Three analytic tasks test whether it supplies the
missing factor \(L\) jointly across all determinants and literal selector
fields, or whether restored dual capacity or selector variation gives a
route-scoped obstruction. No proof owner or exponent changes at launch.

## Current frontier after Round 176 (2026-08-27)

Round 176 proves the exact cross-gcd alternating-fibre reduction for the
complete non-polylogarithmic K17a aggregate. Both opposing orientations have
a multiplicity-one affine fibre, a common endpoint-product step, and an exact
half-frequency character. Squarefreeness identifies the original divisor
gcd as \((u,n)\), so the low-original-gcd selector is constant along each
fibre rather than an obstruction.

The canonical anchor has only logarithmic normalized Fourier cost. A robust
hyperbola count proves every fixed-proportion sector
\(\kappa_*\ge\delta L\) at the target \(L^2X^\varepsilon\). This is genuine
partial closure, but not a uniform tail theorem: the low-cross-gcd complement
\(\kappa_*<\delta L\) remains.

Positive rowwise or smooth-cell transforms restore the missing power, and a
lone inverse-residue square-root saving remains above target. The first exact
open seam is the selector-aware signed joint estimate (176.K35), with the
near-half Fourier alias, all determinants, fibre sites, arithmetic openings,
selectors, endpoints, and orientations kept together before every modulus.

Resulting graph:
`e3927f0ace0f3d74e9e9f5116a319159e3508838c7f7bd14b086fa851cad82b8`.
The complete K17a and K26 estimates remain open, as do hard TOP, both BAL
scopes, UNBAL, M9--M2, both direct M1 parents or GAR, endpoint uniformity,
M9, both bridges, and the quarter theorem. There is no global exponent
improvement: internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), target \(1/4\).

Round 177 is active on the unchanged graph. Its sole mechanism is a
selector-aware signed hybrid inverse-residue/alias-energy estimate on the
low-cross-gcd K17a complement. The exact fixed-\((\kappa,u)\) block has raw
capacity \(L^2/\kappa\) and sufficient scale \(L\); three analytic tasks are
testing the complete proof, a strict sector, or the first exact
diagonal/conductor/selector/capacity obstruction. Launch changes no status
or exponent.

Round 178 is mandatory immediately after Round 177 closes and will reassess
the full proof strategy and current primary literature.

## Current frontier after Round 177 (2026-08-27)

Round 177 proves an exact primitive-alias refinement of the K17a
cross-gcd reduction. With \(u_0=u/(u,n)\), every alias folds to modulus
\(u_0\), and its final additive conductor is
\(q=u_0/(\ell,u_0)\). The exact-conductor coefficient mass cancels the
\(u_0\) factor in the literal stratum capacity, proving the complete
\(q\le(\log(2X))^B\) Fourier packet at
\(L^2X^\varepsilon\), for every fixed \(B>0\). This strictly contains the
physical \(u_0\le(\log(2X))^B\) sector.

The exact remaining K17a interface is high reduced conductor. It needs a
full conductor saving, two coupled square roots, or an equivalent signed
average retaining the selector, square-root phase, gcd strata, incomplete
lifts, endpoints, and both orientations. Positive \(TT^*\), Parseval,
single-square-root, and complementary-divisor mechanisms are now parked
at their exact audited scopes.

The authoritative graph is
47c628b3e4b5086391fb3dbd885865ab21bd7470541099f696044bd2d3b609f7.
No parent or exponent changed. M9--M1 and M9--M2 remain open; endpoint
uniformity and M9 remain open; both bridges remain conditional; and the
Gauss circle conjecture remains unproved. The exponent ledger remains
internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), target \(1/4\).

Round 178 is planned but not launched. It is the mandatory full-proof
strategy and current-primary-literature checkpoint before Round 179.

## Full-proof status after Round 178 (2026-08-27)

Round 178 closes under `strategy_frontier_retained`. It adds no analytic
theorem, but it revalidates both complete quarter-proof routes and narrows
the next analytic attack to one exact interface: the signed high-reduced-
conductor K17a block (177.K34) at local scale \(LX^\varepsilon\).

The selection is mechanism-based. K26 has the smaller nominal factor-\(L\)
deficit, but Round 175 proved its stopped-scale sum is only a maximal-endpoint
coboundary. K17a's high-\(q\) complement is a smaller isolated block with an
unspent conductor and orientation-sign interface. Its positive capacity is
\(Lq\log(2q)\); one square-root conductor saving is insufficient.

The repaired current-primary-source audit gives no importable theorem for a
live literal interface in the named corpus through 2026-08-27. The reviewed
strategy-only patch changes no proof status or edge and produces graph
`e04380a1965e57971bb68d8169d8a8d8e5349edb535e01b343c8b25ecdcd4e27`.

The Gauss circle conjecture remains open. M9--M1 and M9--M2 remain open;
endpoint uniformity and M9 remain open; both bridges remain conditional.
The exponent ledger is unchanged: internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), target \(1/4\).

## Round 179 active frontier (2026-08-27)

Round 179 attacks only the exact high-conductor K17a block (177.K34). The
candidate mechanism first projects the sawtooth Fourier coefficient onto
its exact primitive conductor and separates a small Möbius trace from the
literal difference of the two orientation buckets. The trace, all
normalizations, and the remaining orientation defect must be independently
proved and audited before any graph change.

The stronger aliaswise estimate, K26, all other M1/M2 owners, assembly,
bridges, and exponent work are excluded from this round. Launch changes no
proof state or exponent.

## Full-proof status after Round 179 (2026-08-27)

Round 179 proves an exact finite primitive-conductor kernel and a decisive
mechanism-level no-go. The symmetric (d=1) trace of the primitive
projector is target-safe, but the centered all-conductor projector returns
exactly to the original literal K17a orientation block. Removing the
already-safe low-conductor packet therefore leaves the same unresolved
high-conductor theorem (177.K34), not a contraction.

The two natural orientation maps fail different literal seams: fixed-row
reflection loses the positive displacement and endpoint fields, while
product exchange changes the outer row and sends selected divisors outside
support. Artificial prime and prime-square buckets retain the full
(LqX^\varepsilon) coefficient-uniform capacity, but this is a route
control rather than literal lower mass.

The reviewed patch creates one subordinate proved reduction, has exact
effect `1/2/0/14/18`, and produces graph
`e94ef6a364988e47f8a59ca3589f03cb098a04a241ec841afc2efa6e685081b4`.
No analytic parent, bridge, theorem, or exponent changes.

The Gauss circle conjecture remains open. Complete K17a and K26 remain open;
hard TOP, both BAL scopes, UNBAL, M9--M2, M9--M1 or GAR, endpoint
uniformity, M9, and both quarter-proof bridges remain incomplete. The
exponent ledger remains internal (1/3), accepted external
(0.3144831759740614\ldots), target (1/4). Round 180 is not yet launched.

## Round 180 active frontier (2026-08-27)

Round 180 rotates from the exhausted automatic K17a parity mechanism to the
independent K26 maximal endpoint. A Fejér-cell decomposition isolates the
proposed target-safe row diagonal and far spectrum from one explicit signed
off-row divisor Gram form near the endpoint peak. The local target is
\(LX^\varepsilon\), while coefficient-uniform capacity is \(L^2\); after
the Fejér height these become the endpoint target \(L^3\) and capacity
\(L^4\).

Three analytic tasks test the exact row/cell reduction, the complete literal
off-row cancellation, and adversarial/blind controls. The new mechanism is
the joint actual-symbol row correlation before positivity, not another
scale, tangent, fixed-shift, product-collar, or K17a transform. No graph
status, parent, bridge, theorem, or exponent changes at launch.

## Full-proof status after Round 180 (2026-08-27)

Round 180 proves the exact near-cell row decomposition and a strict
target-safe collision sector. The complete physical row diagonal is
\(O_\varepsilon(LX^\varepsilon)\), and all cross-row equal-product
collisions are \(O_\varepsilon(X^\varepsilon)\). After those terms are
removed, the remaining unequal-product row form is still target-equivalent
to the original local scalar concentration theorem.

The near/far Fejér, collective ordinary-zero, and once-only short-correction
seams are now independently verified: the open local theorem would imply
\(Q_M^*\ll_\varepsilon L^3X^\varepsilon\) and K26. It is not proved.
Coefficient-uniform row positivity has local capacity \(L^2\) and endpoint
capacity \(L^4\), so one factor \(L\) remains missing.

The reviewed patch creates one subordinate proved obstruction, has exact
effect `1/4/0/16/21`, and produces graph
`6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16`.
No parent, bridge, theorem, or exponent changes.

The Gauss circle conjecture remains open. Complete K17a and K26 remain
open; hard TOP, both BAL scopes, UNBAL, M9--M2, M9--M1 or GAR, endpoint
uniformity, M9, and both quarter-proof bridges remain incomplete. The
exponent ledger remains internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), target \(1/4\). Round 181 is pending design.

## Round 181 active frontier (2026-08-27)

Three independent design audits compared BAL, UNBAL, and M1/GAR. BAL's
fresh maximal-prefix statement is stronger than its open critical
remainder and has no concrete source of the missing \(L\). UNBAL's first
nonrepeating target is already the full literal signed matrix theorem over
the whole owner. GAR still requires many untouched layers. The conductor
therefore selected the smaller direct hard-M1 high-radical interface.

For \(r=hn=st^2\), the low-squarefree-radical sector \(s\le L\) is proposed
target-safe by exact incidence counting. Round 181 attacks the complete
literal \(s>L\) aggregate at \(L^{3/2}X^\varepsilon\), against universal
capacity \(L^2X^\varepsilon\). The missing factor is
\(L^{1/2}=X^{1/12}\) at \(L\asymp X^{1/6}\). Three tasks attempt the signed
actual-direction theorem, audit the low-sector and hard-parent connector,
and independently rederive the finite split and false controls.

No theorem or exponent changes at launch. Even success leaves smooth M1,
M9-M1, GAR, hard TOP, BAL, UNBAL, M9-M2, endpoint uniformity, M9, both
bridges, and the quarter theorem open. Round 182 is the mandatory next
full-proof strategy and current-literature checkpoint.

## Full-proof status after Round 181 (2026-08-27)

Round 181 proves a strict hard-M1 reduction. The literal product wave is
partitioned exactly by \(hn=st^2\), \(s\) squarefree. The low-radical
sector and the disjoint high-radical sector
\(t\geq\lceil\sqrt L\rceil\) are each
\(O_\varepsilon(L^{3/2}X^\varepsilon)\) absolutely.

The exact survivor is \(s>L\), \(1\leq t<\lceil\sqrt L\rceil\).
It contains \(t=1\), where the complete coprime-squarefree literal cone
retains coefficient-uniform \(L^2\) capacity against target \(L^{3/2}\).
That capacity is not literal lower mass, and the signed estimate is open.

The exact all-\(L\) Möbius formula includes the correction
\(-\sum_{r\leq L}F_\sigma(r)\) and self-returns to the original hard cone
modulo a target-safe term. Joint multiplier lifting and central-Mellin-only
arguments supply no automatic contraction.

The reviewed patch has exact effect 3/4/0/13/18 and graph
fec130bc66641cbdad18c832de10077a7825f1caaf5d10170a67ef65c0b27196.
No existing status or theorem statement changed. M9-M1 and M9-M2 remain
open; endpoint uniformity, M9, both bridges, and the Gauss circle conjecture
remain open. The exponent ledger is unchanged: internal \(1/3\), accepted
external \(0.3144831759740614\ldots\), target \(1/4\).

## Round 182 mandatory strategy/literature review (2026-08-27)

Round 182 is active on the closed Round 181 graph. It makes no analytic
promotion. The review reconstructs the standard direct-M1 plus M2 route
and the alternative GAR plus M2 route, then prices every surviving hard
M1, smooth M1, GAR, hard-TOP, BAL, UNBAL, endpoint, bridge, and graded
exponent frontier.

The primary-source audit is refreshed through 2026-08-27 with exact
versions, theorem hypotheses, coefficient classes, absolute-value
placement, parameter maps, and restored project powers. Special attention
is given to whether squarefree-supported, square-root-moment,
inverse-residue, or Kloosterman-bilinear theorems genuinely match the new
hard-M1 small-\(t\) residual or the K17a/K26 residuals.

The round will select exactly one Round 183 analytic objective after
reconciling the graph, source, and blind reports. The Gauss circle
conjecture and every global exponent remain unchanged at launch.

## Full-proof status after Round 182 (2026-08-27)

Round 182 closes the mandatory strategy and literature checkpoint without
an analytic promotion.  The standard route still requires both direct M1
parents, complete hard TOP, both BAL scopes, UNBAL, endpoint uniformity,
M9, and the standard bridge.  The GAR alternative replaces only direct M1
and still requires all of M9--M2.

The selected next frontier is exactly
`M9-M1-hard-top-high-radical-small-t-residual-estimate`.  Its complete
one-absolute-value aggregate contains \(t=1\), has coefficient-uniform
capacity \(L^2\), and requires \(L^{3/2}X^\varepsilon\).  Success would
close only the hard signed cone after the proved Round-181 sectors; smooth
direct M1 and all M2/global owners remain open.

The primary-source audit is independently GREEN after bounded repairs.
No theorem in the dated named corpus through 2026-08-27 matches both a live
literal interface and its restored power.  The strategy-only patch has
effect `0/1/0/16/21` and produces graph
`5965e35636d988267311dbfcf8d57243153f88cb1105e2b2bcc35fa59a5e3833`.

The Gauss circle conjecture remains open.  The exponent ledger is unchanged:
internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), target \(1/4\).  Round 183 is pending design
on the complete small-\(t\) aggregate.

## Round 183 small-t signed contraction launch (2026-08-27)

Round 183 is active on the unchanged graph.  Its sole owner is the complete
hard-M1 high-radical small-\(t\) aggregate, including \(t=1\), both signs,
every literal shell, coefficient field, crossing, and endpoint, with one
absolute value after the full sum.  Capacity is \(L^2\), target is
\(L^{3/2}X^\varepsilon\), and the missing signed factor is \(L^{1/2}\).

The round tests a direct literal contraction, the exact truncated-Möbius
kernel, and a fully restored fixed-row shifted-correlation connector, with
an isolated rederivation.  These are proof mechanisms only unless they
return to the complete owner.  No parent, bridge, theorem, or exponent is
promoted at launch.

## Full-proof status after Round 183 (2026-08-27)

Round 183 proves the first signed target-scale sector inside the hard-M1
high-radical small-t residual. In primitive-ray coordinates h = Gu and
n = Gv, the literal odd-G character-phase ratio is
-e(2 sigma sqrt(Xuv)). Step-two bounded variation therefore controls all
incidences with G >= ceil(L^(1/4)) away from a
1/(10 log(2X))-neighborhood of half-integer resonance. Counting primitive
rays gives O(L^(3/2)), while the corresponding unsigned incidence envelope
is O(L^(7/4)).

This is a strict sector, not the complete owner. The exact complement is the
small-G sector together with the large-G near-resonant sector; all t = 1
incidences lie in the former. A target-scale truncated Mobius split is now
proved to self-return on its small-divisor core, and the exact fixed-row
Fejer identity does not by itself prove its required signed correlation
bound.

The reviewed patch creates one proved sector node and updates only the open
small-t residual and its existing Mobius obstruction. Its exact effect is
1/2/0/13/24, producing graph
a8e0e5d84c0c5047e0c96f11128dd215ae035bdd4355bd68ad28dc87afe6cfbd.
M9-M1 and M9-M2 remain open, as do endpoint uniformity, M9, both bridges,
and the Gauss circle conjecture. There is no global exponent improvement:
internal 1/3, accepted external 0.3144831759740614..., target 1/4.
Round 184 is pending design from the exact surviving complement and the
other open frontiers.

## Round 184 hard-M1 t=1 launch (2026-08-27)

Round 184 freezes the complete t = 1 face of the hard-M1 small-t residual:
coprime squarefree uv, v odd, 4u < v < 16u, exact zero-extended literal
coefficient, both signs, all crossings and endpoints, and one final
absolute value. Its coefficient-insensitive capacity is L^2 and its target
is L^(3/2)X^epsilon.

The proposed signed relation canonically selects at most one close pair of
odd prime factors p,q of uv with chi_4(pq) = -1, independently of the
allocation uv = u times v. On the XOR incidence sector, swapping p and q
between the two legs preserves uv and the square-root phase and reverses
the character. A target proof requires an L^(-1/2) actual-profile
difference on common cells and a complete O(L^(3/2)) ledger for every
boundary and zero-extension collar.

The exact residual contains all products without a selected pair and the
neither/both allocations when a pair exists. No pair density is assumed.
Three tasks attack the literal exchange and residual, audit transfer from
the analogous M2 kernels and all restored powers, and independently
rederive the finite problem from a statement-only packet.

Launch changes no theorem or exponent. The complete t = 1 face, t >= 2,
large-G near resonance, the full small-t owner, hard and smooth M1 parents,
M9-M1, every M2 owner, endpoint uniformity, M9, both bridges, and the
quarter theorem remain open.

## Full-proof status after Round 184 (2026-08-27)

Round 184 proves a strict actual-coefficient sector of the hard-M1 t = 1
face. For each squarefree product, a canonical allocation-independent
selector chooses at most one close pair of odd prime factors with opposite
chi_4-product. On XOR allocations, exchanging the pair between the two
legs is an integral multiplicity-one involution that preserves the product
and square-root phase and reverses the character.

Zero extension turns this into an exact coefficient-difference identity.
The product power is invariant; common-cell smooth differences contribute
L^(-1/2); normalized dyadic BV and every physical collar and endpoint cost
at most L^(3/2)X^epsilon on the orbit-closed active box. This proves the
possibly empty selected-product XOR sector at the target scale.

The exact residual contains all allocations of products with no selected
pair and the neither/both allocations of selected products. Its exact
Fejer connector requires a one-outer-real-part short-shift correlation of
size L^2X^epsilon at R = ceil(L). That signed correlation is unproved;
shiftwise triangle returns L^2X^epsilon scalar capacity.

The reviewed patch has effect 1/1/0/15/27 and produces graph
f16b7a43f8b0261671b39bdd4a59a3f06926cdfe3513d5910e56b89c6b1ab2e0.
The complete t = 1 face and complete small-t owner remain open, as do
t >= 2, near resonance, the hard signed cone, smooth M1, GAR, M9-M1,
every M2 parent, endpoint uniformity, M9, both bridges, and the Gauss
circle conjecture. There is no exponent improvement: internal 1/3,
accepted external 0.3144831759740614..., target 1/4.

The final independent Round-184 closure audit is GREEN after notation,
wording, and terminal-newline repairs. It reconfirms exact patch reversal
and replay, evidence hashes, lifecycle identity, artifact hygiene, tests,
and complete owner and exponent quarantine. Round 185 is pending design.

## Round 185 hard-M1 residual Fejer tangent-gcd launch (2026-08-28)

Round 185 freezes the exact no-pair plus selected neither/both residual of
the hard-M1 t = 1 face. Its sliding Fejer connector has one outer real part
over shifts r < ceil(L), diagonal L^2X^epsilon, and positive energy capacity
L^3X^epsilon. The target is L^2X^epsilon, equivalent to the missing scalar
factor L^(1/2) after the Cauchy connector.

The proposed finite decomposition opens both product rows N = dm and
N+r = d'm', maps the odd character leg to d, and splits by parity,
tangent orientation, original gcd (d,d'), and inward cross gcd. Monotone
and fixed-proportion high-gcd sectors may be target-safe by counting; bare
alternation on a primitive opposing fibre is not an estimate unless all
literal selector, arithmetic-deletion, profile, endpoint, and sign fields
are controlled.

The launch changes no graph node or exponent. The complete t = 1 residual,
t >= 2, near resonance, both M1 parents, every M2 parent, endpoint
uniformity, M9, both bridges, and the quarter theorem remain open. Round
186 is the required strategy and current-literature checkpoint after this
round closes.

## Full-proof status after Round 185 (2026-08-28)

Round 185 proves a strict actual-coefficient sector of the exact hard-M1
t = 1 residual left by Round 184.  The sliding energy admits an
endpoint-exact even-parity Fejer connector.  Opening both residual
coefficients is multiplicity one and gives the tangent identity, the
character sign, both opposing orientations, and original and inward-cross
gcd coordinates with joint quotient r = 2 kappa g h.

The complete monotone sector and both opposing orientations with
h <= floor((log(2X))^B) have absolute Fejer contribution
O_(B,epsilon)(L^2X^epsilon), at the required energy scale.  Canonical
orientation-dependent affine anchors and positive index sets give the
exact high-h complement with one real part outside every row, shift,
selector, endpoint, and sign.

The first unproved relation is now precise: uniformly on each dyadic
Y < h <= 2Y block, the actual coupled signed aggregate must gain the full
factor Y over its positive Y L^2X^epsilon capacity.  Bare character
alternation, rowwise Abel, O(1) per row followed by positive recombination,
positive transforms, alias energy, and conductor centering do not supply
that factor.

The reviewed patch has effect 1/1/0/20/31 and produces graph
f43248060d7876a96d4554cd13372dbf267387bcbe44a832b87cd5f571801575.
The complete t = 1 residual and complete small-t owner remain open, as do
t >= 2, near resonance, the hard signed cone, smooth M1, GAR, M9-M1,
every M2 parent, endpoint uniformity, M9, both bridges, and the Gauss
circle conjecture.  There is no exponent improvement: internal 1/3,
accepted external 0.3144831759740614..., target 1/4.

Both independent postapplication audits recover the starting graph and
replay the applied graph byte-for-byte.  Round 186 is the mandatory
full-proof strategy and current-primary-literature checkpoint after
analytic Rounds 183--185.

The final independent closure audit is GREEN. It verifies the current
postrepair evidence corpus, exact repair-to-historical-byte provenance,
State Patch inverse and replay, lifecycle consistency, compilation, all
six tests, and every owner and exponent quarantine.

## Round 186 full-proof strategy and literature checkpoint (2026-08-28)

Round 186 closes under strategy_frontier_retained. It proves no new
analytic estimate. The exact post-Round-185 graph audit retains the
high-height tangent-gcd relation as the sole Round-187 objective:

\[
 \Re\!\sum_{\omega\in\{+,-\}}
 \sum_{\substack{\mathfrak f\ \mathrm{primitive}\\Y<h\leq2Y}}
 (-1)^{S_{0,\omega}}
 \sum_{t\in I_{\mathfrak f,\omega}}
 (-1)^tB_{\mathfrak f,\omega}^{\sigma}(t)
 \ll_{B,\varepsilon}L^2X^\varepsilon .
\]

It is one-sided, with one real part outside both orientations and all
primitive rows. Positive capacity is \(YL^2X^\varepsilon\), so a full
factor \(Y\) is missing. Success would close only the exact
original-\(t=1\) residual through accepted connectors. Original
\(t\geq2\), near resonance, both M1 parents, GAR, all M2 parents,
endpoint uniformity, M9, both bridges, and the quarter theorem remain.

The primary-source audit is current through 2026-08-28 for its named
versioned corpus and imports no theorem. Milicevic--Robinson--Shupe
arXiv:2608.21346v1 is retained as a nonimportable complete prime-power
Kloosterman-product guardrail. Li--Yang v2 remains the accepted external
benchmark.

The exact 0/1/0/21/24 strategy-only patch produces graph
d1ace6e362a41f1a08fc09c8e44ce628758040fa91ae39c152113c275f76352a.
Independent inverse and actual-time replay audits are GREEN. Exponents are
unchanged: internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), target \(1/4\). Round 187 is pending design.

## Full-proof status after Round 187 (2026-08-29)

Round 187 proves an exact strict Fourier packet inside the high-height
hard-M1 \(t=1\) residual. For odd \(U>1\), the inverse-residue anchor has
Fourier coefficients

\[
c_U(k)=\frac{2}{U(1+e(-k/U))},\qquad
q_U(k)=\frac{U}{(k,U)}.
\]

For \(Q=H_B=\lfloor(\log(2X))^B\rfloor\), the complete \(U=1\)
contribution, every exact conductor \(q_U(k)\le Q\), every remaining
mode with \(U\le4Q\), and every remaining ordinary edge mode
\(0<|k|_U\le Q\) have total absolute size
\(O_{B,\varepsilon}(L^2X^\varepsilon)\). The proof uses the literal
\(u=gU,n=gh\) coordinate count and exact conductor mass, without changing
multiplicity, selectors, arithmetic deletions, endpoints, or the single
outer real part.

The exact complement is

\[
U>4Q,\qquad q_U(k)>Q,\qquad |k|_U>Q.
\]

Its positive capacity remains \(O(YL^2X^\varepsilon)\), against the
required one-sided \(O(L^2X^\varepsilon)\) bound. The full factor \(Y\)
has not been obtained. Prime-modulus self-return and the near-half-mode
\(\ell^2\)-mass control show why conductor centering or positive transform
energy alone cannot supply it.

The reviewed patch has effect 1/1/0/14/20 and produces graph
`be0eca9ca93c3534cca958d70b5541d03d28ff993ebfbcbca6be3cd393fae5ff`.
Only the strict subordinate reduction is promoted. The complete high-h
relation, complete \(t=1\) residual, \(t\ge2\) and near-resonant pieces,
hard and smooth M1, GAR, hard TOP/BAL/UNBAL on M2, endpoint uniformity,
M9, both bridges, and the Gauss circle conjecture remain open. There is no
exponent improvement: internal \(1/3\), accepted external
\(0.3144831759740614\ldots\), target \(1/4\). Round 188 is pending design.

## Full-proof status after Round 188 (2026-08-29)

Round 188 proves the complete sufficiently imprimitive part of the exact
Round-187 high-height hard-M1 $t=1$ packet. Writing $m=(k,U)$,
$U=mq$, and $k=ma$ gives $c_U(k)=m^{-1}c_q(a)$. The one-block
$O(YL)$ atom count, the $m^{-1}$ conductor mass, and the
triple-divisor ledger prove every mode with $H_Bm\ge Y$ absolutely at
$O_{B,\varepsilon}(L^2X^\varepsilon)$.

The first remaining relation is the exact complement

\[
U=mq>4H_B,\qquad q>H_B,\qquad m|a|_q>H_B,\qquad H_Bm<Y.
\]

It remains joint under one outer real part and has positive capacity
$O(YL^2X^\varepsilon)$, so the full factor $Y$ is still missing.
The lifted determinant phase is constant on each affine $t$-ray, and
primitive near-half modes retain constant Fourier energy. Determinant
transposition, reciprocity alone, completion, positive energy, and
selector-blind sieve opening are therefore ruled out as automatic sources
of the gain; this does not disprove the actual one-sided estimate.

The reviewed patch has effect `1/1/0/15/21` and produces graph
`338060b37c19d849053078e5f6a7775c45c626a16b6f9198fafdf9bb4a62265c`.
M9-M1 remains open: the displayed complement, the rest of the exact
$t=1$ residual, every original $t\ge2$ small-$G$ incidence, the
large-$G$ near-resonant complement, the hard parent, the independent
smooth M1 parent, physical assembly, and GAR remain unfinished. M9-M2 is
unchanged and open: hard TOP, including the live K17a and K26 residuals,
BAL, and UNBAL remain unproved. Endpoint uniformity, M9, both bridges,
and the Gauss circle conjecture remain open or conditional.

There is no global exponent improvement: internal $1/3$, accepted
external $0.3144831759740614\ldots$, target $1/4$. Round 189 is
`pending_design`; Round 190 remains the mandatory full-proof strategy and
current-primary-literature checkpoint.


## Round 189 accepted dual-frequency projective reduction

Round 189 closes under strict_dual_height_resonance_sector on graph
15c770023b649a95596b223e15370657836e230580f0d2f31f5d30c615a98568.
On the exact Round-188 complement, define

\[
j_q(a,v)=|a\bar v_q|_q,\qquad
T_Q(m,q;Y)=
\min\!\left\{\frac{q-1}{2},
       \left\lfloor\frac{H_Bmq}{Y}\right\rfloor\right\}.
\]

The inherited carrier has \(U=mq\) odd and \(q\mid U\mid u\).
For fixed unit \(a\bmod q\), the map
\(v\mapsto a\bar v_q\) is a bijection of unit classes. Hence the
slow set uses at most \(2T_Q\) classes and
\(O(uT_Q/q)\le O(H_Bum/Y)\) literal \(v\)-values. Restoring
\(O(Y)\) heights and \(O(\kappa)\) affine sites and using

\[
c_{mq}(ma)=m^{-1}c_q(a),\qquad
\sum_{(a,q)=1}|c_q(a)|\ll\log(2q),
\qquad
\sum_{mq\mid u}1=\tau_3(u),
\]

cancels \(Y\) and \(m\) before outer positivity. Therefore the
complete sector \(j_q(a,v)\le T_Q(m,q;Y)\) is
\(O_{B,\varepsilon}(L^2X^\varepsilon)\). This includes the
power-neutral baseline \(j_q\le\lfloor U/Y\rfloor\) and the frozen
\(H_B\)-enlargement; no positive power of \(Y\) is absorbed.

The exact fast complement \(j_q(a,v)>T_Q(m,q;Y)\) remains under one
outer real part over both orientations and every literal field. On a
dyadic \(J\)-band, a sufficient fixed-\(a\) input is

\[
\sum_{\omega,v}\mathsf V(W_v)
\ll_\varepsilon
\frac{H_Bm\kappa uJ}{q}X^\varepsilon,
\]

whereas the accepted pointwise information gives only
\(Y\kappa uJ/q\). The exact deficit is \(Y/(H_Bm)\), and primitive
lifts retain \(Y/H_B\).

For odd prime conductor, the centered slope \(-2\) prefix is exactly
\(-(p-1)/2\). This rules out a uniform polylogarithmic
centered-kernel prefix theorem but is not literal lower mass.
Assumed bounded variation, positive completion energy, and
selector-blind sieve opening remain invalid shortcuts.

The applied State Patch has exact effect \(1/1/0/15/22\). The
complete high-height relation, original \(t=1\) residual, every
original \(t\ge2\) small-\(G\) incidence, the large-\(G\)
near-resonant complement, both M1 parents, every M2 parent, endpoint
uniformity, M9, both bridges, and the quarter theorem remain open or
conditional.

There is no global exponent improvement: internal \(1/3\), accepted
external \(0.3144831759740614\ldots\), target \(1/4\). Round 190 is
the mandatory full-proof strategy and current-primary-literature
checkpoint.

Accepted evidence:

- proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md;
- rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/candidates/formalized_hard_m1_t1_high_h_dual_frequency_projective_reduction.md;
- rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/final_kernel_candidate_consistency_review.md;
- rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/final_kernel_power_literal_owner_scope_review.md;
- rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/final_kernel_formalization_provenance_hygiene_review.md;
- rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/controls/postapply_independent_reverse_replay_audit.md;
- rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/controls/postapply_scope_protected_state_audit.md;
- rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/reviews/conductor_round189_adjudication.md; and
- rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/synthesis.md.

## Status after Round 190 (2026-08-29)

Round 190 is a strategy/current-literature checkpoint, not an analytic
promotion. It reconstructs both lawful quarter routes, verifies the exact
Round-189 fast-complement deficit \(Y/(H_Bm)\), repairs the blind
positive-variation proposal to a joint signed height-jump coboundary seam,
and finds no exact theorem import in the named primary corpus through the
2026-08-29 cutoff.

The resulting graph is
306425e79ef6d5e25ed037b77d25a0cc180bfc3b68c4a17ef833da7be1a573fa.
The patch changes only strategy evidence and the next action of one
already-open subordinate owner.

The full proof is not complete. M9-M1 and M9-M2 are open, endpoint
uniformity and M9 are open, both final bridges are conditional, and the
quarter target is open. The strongest internally proved exponent remains
\(1/3\); the accepted external Li--Yang benchmark remains
\(0.3144831759740614\ldots\); the target is \(1/4\).

Round 191 is pending design on the exact fast-complement signed jump seam.

## Status after Round 191 (2026-08-29)

Round 191 proves a new strict subordinate reduction, not the full fast
packet. With \(U=mq\) and signed least inverse \(\varrho_U(v)\), the sector

\[
0<|\varrho_U(v)|\le
\min\!\left(\frac{U-1}{2},
\left\lfloor\frac{H_BmU}{Y}\right\rfloor\right)
\]

is target-safe by inverse-class sparsity and the exact lift/divisor ledger.
The exact outer terminal and isolated Fejer jump projections are also
target-safe, and the adjacent-fibre transport including its retained-mode
carry sign is now formalized.

The resulting graph is
`75b44fe68f9c6e094d2ab6e643be3c0309320ef84e73ca22d692698440eeed13`.
The rho-large literal remainder remains open with the same missing factor
\(Y/(H_Bm)\). It cannot be replaced by positive variation, separate
orientation estimates, or coefficient-uniform bounded-array control.

The full proof is not complete. M9-M1 and M9-M2 are open, endpoint
uniformity and M9 are open, both final bridges are conditional, and the
quarter target is open. The strongest internally proved exponent remains
\(1/3\); the accepted external Li--Yang benchmark remains
\(0.3144831759740614\ldots\); the target is \(1/4\). Round 192 is pending
design; Round 194 remains the mandatory strategy/literature checkpoint.

## Round 192 launch status (2026-08-29)

Round 192 is active on the unchanged Round-191 graph. Its new exact seam is
the unimodular factorization

\[
 \rho(cv_0-dU)=c+U(c\beta-d\rho),
 \qquad \rho v_0-\beta U=1,
\]

which makes each fixed small Farey covector and fixed covector value a
divisor-counted sparse residue family. The round is testing the resulting
target-safe union, its small-\(U\) coverage corollary, and the exact remaining
badly-approximable core under all literal fields and the outer power ledger.

Launch validation, campaign/plan equality, graph validation, failure-ledger
equality, six tests, and the finite sign/floor/multiplicity diagnostic are
green. The full proof remains open; M9-M1 and M9-M2 are open, both bridges are
conditional, and there is no exponent improvement. Round 194 remains the
mandatory strategy/current-literature checkpoint.

## Status after Round 192 (2026-08-30)

Round 192 proves a new strict subordinate reduction. In the exact Round-191
rho-large hard-M1 \(t=1\) remainder, the union of primitive small Farey
covectors satisfying
\[
 |c\beta-d\rho|\le T
\]
is target-safe for \(T\ge1\); the \(T=0\) selector is empty. The proof uses
\[
 \rho(cv_0-dU)=c+U(c\beta-d\rho)\ne0
\]
to convert each fixed covector fibre into a signed-divisor count, followed by
the exact literal, height/site, lift, coefficient, divisor, and shell ledgers.

Circular pigeonhole proves that every remaining \(T\ge1\) core row has
\[
 |\rho|\ge(A+1)(T+1)
\]
and gives an exact empty-core criterion. The nonempty jointly signed core is
not estimated. Static Farey separation, long-step Abel, positive covering,
and bounded-array capacity do not close it; positive control still misses by
\(Y/(H_Bm)\).

The resulting graph is
7c89a29f96878cb4c8481129a4a76453263768f0a7b699fa20003fc4db207bd9.
M9-M1 and M9-M2 remain open, endpoint uniformity and M9 remain open, both
bridges remain conditional, and the quarter target remains open. The
strongest internally proved exponent remains \(1/3\); the accepted external
Li--Yang benchmark remains \(0.3144831759740614\ldots\); the target remains
\(1/4\). Round 193 is pending design, and Round 194 remains mandatory.

## Round 193 gcd-scaled orientation-involution launch (2026-08-30)

Round 193 freezes one exact mechanism on the Round-192 core.  For an
opposing opened tuple \(N=dm\), \(N+r=d'm'\), let
\(g=(d,d')\) and \(k=(m,m')\).  On \(k=1\), test

\[
 (d,m,d',m')\mapsto(gm,d/g,gm',d'/g)
\]

on \(r\equiv2\pmod4\) and the two
\(\lceil L^{1/2}\rceil\)-close scaled-allocation conditions.  The map
preserves both products and the Fejer square-root phase and is expected to
reverse the character product.  Promotion requires a complete proof of
gcd/parity normalization, the Round-184 residual mask, every literal
endpoint field, the close-count and BV/collar powers, and deletion-stable
passage through all accepted Round-187--192 safe projections.

The launch changes no graph status or exponent.  M9-M1, M9-M2, endpoint
uniformity, M9, both conditional bridges, and the quarter target remain
open or conditional.  Round 194 is mandatory after this analytic round.

## Status after Round 193 and Round 194 launch (2026-08-30)

Round 193 proves the entire gcd-scaled double-close physical sector of the
exact Round-192 hard-M1 \(t=1\) core.  With
\(D_L=\lceil\sqrt L\rceil\), the masked core contribution on
\(|d-gm|,|d'-gm'|\le D_L\) is
\(O(L^2X^\varepsilon)\).  A uniform live-cone bound on \(g\), determinant
multiplicity, and the deletion-stable core ledger give the estimate without
requiring the subsidiary character-reversing involution.

The resulting graph is
`cbbb68b5bb7dd324ca60b1e099cf5787fa57639b5970d76464c2bce18cfcdd9e`.
The exact disjoint first-failure masks \(P_1\) and \(P_2\) remain open.
Even their future completion would settle only the remaining original
\(t=1\) rho-large residual; original \(t\ge2\) and large-G near resonance,
smooth M1, GAR, M2 hard TOP/BAL/UNBAL, endpoint uniformity, and both bridges
remain separate owners.

Round 194 is now active as the mandatory full-proof strategy and
current-primary-literature checkpoint.  It will select exactly one Round-195
analytic objective but cannot promote an analytic result or exponent.
The strongest internally proved exponent remains \(1/3\); the accepted
external Li--Yang benchmark remains \(0.3144831759740614\ldots\); the target
remains \(1/4\).

## Status after Round 194 (2026-08-30)

Round 194 is a strategy/current-literature checkpoint, not an analytic
promotion. It reconstructs both lawful quarter routes, keeps every direct
M1/GAR, M2 hard-TOP/BAL/UNBAL, endpoint, bridge, and graded owner separate,
and finds no exact theorem import in the named primary corpus through
2026-08-30.

The resulting graph is
`815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89`.
The patch changes only strategy evidence and the next action of one
already-open owner. The unique next frontier is the exact \(P_2\) complement
of the Round-193 double-close sector, attacked through the identity

\[
2h=v\Delta_+ + U\Delta_- -\kappa(U^2-v^2),
\]

with \(|g\Delta_-|\le\lceil\sqrt L\rceil\) and
\(g\Delta_+>\lceil\sqrt L\rceil\). A coefficient-retaining
determinant-fibre vector-dispersion estimate at fixed-packet scale
\(H_B\mathfrak m\kappa uX^\varepsilon\) is the unproved Round-195 target.

The full proof is not complete. M9-M1 and M9-M2 are open, endpoint
uniformity and M9 are open, both final bridges are conditional, and the
quarter target is open. The strongest internally proved exponent remains
\(1/3\); the accepted external Li--Yang benchmark remains
\(0.3144831759740614\ldots\); the target remains \(1/4\). Round 195 is
pending design.

## Round 196 launch (2026-08-30)

Round 196 is active on the exact residual (P_2) packets

\[
 \kappa<D_L,\qquad
 \min(Y,D_L)>H_B\mathfrak m\kappa.
\]

It tests whether the determinant equation converts the parity-weighted
inverse-residue anchor into a common primitive (x)-carrier and whether the
literal recombined operator contains a genuine step-two difference. Only
such a difference may use the exact conductor-denominator cancellation;
all endpoint, arithmetic-support, mask, carry, birth/death, Fejer, phase,
and zero-extension commutators must be paid.

No proof status or exponent changes at launch. The internal exponent
remains (1/3), the accepted external benchmark remains
(0.3144831759740614\ldots), and the target remains (1/4).

## Round 195 launch status (2026-08-30)

Round 195 is active on the full exact \(P_2\) complement. It fixes
\((g,\Delta_-)\), dyadically resolves the positive far defect
\(g\Delta_+>\lceil\sqrt L\rceil\), and tests the determinant identity

\[
2h=v\Delta_+ + U\Delta_- -\kappa(U^2-v^2)
\]

through an actual-coefficient two-orientation vector Gram matrix. Both
\(T\)-branches and every literal endpoint, carry, phase, birth/death,
commutator, and zero-extension field remain under one outer real part.

The required fixed-packet gain is the full factor
\(Y/(H_B\mathfrak m)\). The campaign may prove the complete target, a
genuinely target-safe strict sector with one exact complement, or a rigorous
scoped no-go; it may not escape through arbitrary coefficients, separate
orientation norms, another submask, \(P_1\), or another owner.

The launch changes no proof status or exponent. M9-M1, M9-M2, endpoint
uniformity, M9, both bridges, and the quarter target remain open or
conditional.

## Status after Round 195 (2026-08-30)

Round 195 proves two strict target-safe sectors of the exact physical
lower-close/upper-far mask \(P_2\). The entire sector
\(\kappa\ge D_L=\lceil\sqrt L\rceil\) is safe by an absolute physical
count. On \(\kappa<D_L\), the fixed-packet bound

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D}W)|
 \ll u\{\kappa+\min(Y,D_L)\}X^\varepsilon
\]

proves every packet satisfying
\(\min(Y,D_L)\le H_B\mathfrak m\kappa\). Both sectors have accepted outer
contribution \(O(L^2X^\varepsilon)\).

The resulting graph is
`f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`.
Complete \(P_2\) remains open precisely on

\[
 \kappa<D_L,\qquad \min(Y,D_L)>H_B\mathfrak m\kappa.
\]

The next theorem would have to estimate the literal cross-row four-block
coefficient Gram; same-site event splitting, coefficient-blind capacity,
and the blind squareful model do not provide it.

The full proof is not complete. M9-M1 and M9-M2 remain open, endpoint
uniformity and M9 remain open, both final bridges remain conditional, and
the quarter target remains open. The strongest internally proved exponent
is still \(1/3\); the accepted external Li--Yang benchmark remains
\(0.3144831759740614\ldots\); the target remains \(1/4\). Round 196 is
pending design.

## Status after Round 196 (2026-08-30)

Round 196 proves no new \(P_2\) sector.  It records a durable
normalization/support no-go for the proposed on-shell
carrier-denominator mechanism.

The formal primitive modulus-\(4q\) phase belongs to the
parity-restored shadow.  The literal fixed mode instead retains
\((-1)^t\), and its on-shell form has the additional
\(E_U(S_0)\) factor.  This factor convolves exact conductors.  The live
literal multiplier is \(+e(a/q)\), the formal negative wrap is an
unpaired zero-extension boundary, and the accepted height, affine, plus,
and minus events do not supply one common full-core step-two difference.
All endpoint, mask, arithmetic, carry, Fejer, phase, birth/death, and
zero-extension commutators remain.

The resulting graph is
b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae.
The complete \(P_2\) remainder remains open precisely on
\[
 \kappa<D_L,\qquad
 \min(Y,D_L)>H_B\mathfrak m\kappa.
\]
A different coefficient-sensitive joint four-block estimate is still
logically possible; the disjoint \(P_1\) complement is also open.

The full proof remains incomplete.  M9-M1 and M9-M2 are open, endpoint
uniformity and M9 are open, both final bridges are conditional, and the
quarter target is open.  The strongest internally proved exponent remains
\(1/3\); the accepted external Li--Yang benchmark remains
\(0.3144831759740614\ldots\); the target remains \(1/4\).

Round 197 is pending design.  Round 198 is mandatory immediately after
Round 197.

## Round 197 launch (2026-08-30)

Round 197 is active on graph
b9b95784b097b3e30bed95f418ae14e57bf5f03a4a52975beeefa8db85b7f8ae.
The one frozen objective is a new coefficient-sensitive physical
\(P_2\) mechanism: two independent allocation swaps are tested for a
literal four-corner \(+,-,-,+\) character rectangle.  If the complete
orbit survives, its endpoint product factors into a mixed difference and
the lower close leg could supply the exact \(D_L/L\) gain needed to reduce
the \(D_LL^2\) envelope to \(L^2\).

Three orthogonal tasks cover literal construction, hostile orbit/power
audit and statement-only rederivation.  No theorem, sector, owner, parent,
bridge, target or exponent is promoted at launch.  Round 198 is the
mandatory strategy and literature review after this analytic round.

## Status after Round 197 (2026-08-31)

Round 197 proves one strict physical common-cell sector of the exact open
\(P_2\) region at the required outer scale:

\[
 |\mathscr R_{\rm core,out}^{\sigma}(P_{\rm cc}W)|
 +|\mathscr R_{\rm open,out}^{\sigma}(P_{\rm cc}W)|
 \ll L^2X^\varepsilon.
\]

The proof pairs the two literal lower allocations before positive norms.
On their common arithmetic/support/sharp code, the actual endpoint
difference splits into smooth, normalized-BV, and selector terms.  The
smooth and BV ledgers reduce the raw \(D_LL^2\) envelope to
\(D_L^2L\le4L^2\), while the selector exception is confined to bounded
shells after the finite-\(g\) audit.  No nonemptiness or density of this
sector is asserted.

The complete four-corner proposal does not close \(P_2\): its required
cross-coprimality forces the physical inward gcd \(\kappa=1\), and an
aligned literal sharp face can still retain \(D_LL^2\) capacity.  The exact
remaining seam is

\[
 \{\kappa<D_L,\ \min(Y,D_L)>H_B\mathfrak m\kappa\}
 \cap(P_{\partial\rm lit}\dot\cup P_{s\rm f}\dot\cup P_{g\rm f}).
\]

The authoritative graph is
`8aea2ab5b088a0b29a434347ffc4509c70e79f53e450814920e3c83165a1ab69`.
It contains one new subordinate proved-internal node; the open hard-M1
owner received only a dependency and next-action update.  No parent,
endpoint theorem, bridge, target, or exponent was promoted.

The full proof remains incomplete.  M9-M1 and M9-M2 are open, endpoint
uniformity and M9 are open, both final bridges are conditional, and the
quarter target is open.  The strongest internally proved exponent remains
\(1/3\); the accepted external Li--Yang benchmark remains
\(0.3144831759740614\ldots\); the target remains \(1/4\).

Round 198 is the mandatory full-proof strategy and current-primary-
literature checkpoint before another analytic campaign is selected.

## Round 198 launch (2026-08-31)

Round 198 is active on unchanged graph
`8aea2ab5b088a0b29a434347ffc4509c70e79f53e450814920e3c83165a1ab69`.
It is the mandatory full-proof strategy and current-primary-literature
checkpoint after analytic Rounds 195--197.

The round has three orthogonal tasks: reconstruct both lawful quarter
proof trees and rank every live frontier by exact power and owner leverage;
audit primary sources current through 2026-08-31 against the literal
\(P_2\) boundary/sign/gcd complement and all competing interfaces; and
independently select one Round-199 objective from an isolated
statement-only packet.

This strategy round promotes no analytic estimate, parent, endpoint
theorem, bridge, target, or exponent.  The graph remains unchanged.
Round 199 will be designed only after the three reports and the required
dependency, source, and post-unmask reviews close Round 198.

## Status after Round 198 (2026-08-31)

Round 198 closes under `strategy_frontier_retained` on graph
`63fa05e3a4d1493bc37bdd956453a4d3eefbb9dca6fadcbf8b7a68e32ade36b5`.
It proves no new estimate and changes no exponent. It reconstructs both
lawful quarter routes, completes a primary-source audit through 2026-08-31,
and selects one exact Round-199 theorem-or-no-go gate.

The selected theorem is the joint outer \(O(L^2X^\varepsilon)\) estimate
for the complete Round-195 open-packet
\(P_{\partial\rm lit}\dot\cup P_{s\rm f}\dot\cup P_{g\rm f}\)
complement. The aligned literal face is the first stress test. A face-only
success is subordinate evidence; a theorem exit must retain all three
failure channels before positive component norms.

M9-M1 and M9-M2 remain open. Endpoint uniformity and M9 remain open, both
bridges remain conditional, and the Gauss-circle quarter target remains
open. The internal exponent is still \(1/3\), the accepted external
Li--Yang benchmark is still \(0.3144831759740614\ldots\), and the target is
still \(1/4\). Round 199 is pending design; no campaign is active.

## Round 199 launch (2026-08-31)

Round 199 launches the exact cross-gcd cellular-boundary gate on graph
`63fa05e3a4d1493bc37bdd956453a4d3eefbb9dca6fadcbf8b7a68e32ade36b5`.
For each squarefree even-shift allocation it records the four pairwise
coprime cross-gcd states

\[
 (d,d'),\qquad(m,d'),\qquad(d,m'),\qquad(m,m'),
\]

whose product is \(\gcd(N,N+r)\). The new mechanism asks whether the
literal-boundary, sign-failure and gcd-failure pieces are the complete
actual-\(\chi_4\) boundary of a bijective physical allocation two-chain.
The aligned sharp face is tested first. A theorem must bound the full joint
operator by \(O(L^2X^\varepsilon)\); an exact cellular self-return is the
only other terminal label and authorizes no analytic pivot.

This launch changes no graph status or exponent. Even success would close
only the remaining open-packet \(P_2\) sector. Round 202 remains the next
mandatory full-proof strategy and current-primary-literature checkpoint.

## Status after Round 199 (2026-08-31)

Round 199 closes under
`p2_cross_gcd_cellular_boundary_self_return_no_go` on graph
`3073235ad5677b9066f1336ec9d958b0e93b92d99cfa7ebea1d823146c799099`.
It proves no new analytic estimate. It rigorously eliminates the frozen
cross-gcd cellular completion: the lawful P2 triangle has nonzero augmented
incidence, its required fourth live corner transfers to the disjoint P1
owner, and partial cross-gcd moves create changing-mask commutators.

The no-go is mechanism-scoped. It does not disprove a different
coefficient-sensitive joint estimate and proves no lower mass. The exact
remaining open-packet P2 seam is still

\[
 \{\kappa<D_L,\ \min(Y,D_L)>H_B\mathfrak m\kappa\}
 \cap(P_{\partial\rm lit}\dot\cup P_{s\rm f}\dot\cup P_{g\rm f}).
\]

M9-M1 and M9-M2 remain open. Endpoint uniformity and M9 remain open, both
bridges remain conditional, and the Gauss-circle quarter target remains
open. The internal exponent is \(1/3\), the accepted external Li--Yang
benchmark is \(0.3144831759740614\ldots\), and the target is \(1/4\).
Round 200 is pending design; Round 202 remains the next mandatory strategy
and literature checkpoint.
