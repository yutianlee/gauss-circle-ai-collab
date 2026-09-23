# Round 195 statement-only blind rederivation

- Campaign: `m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate`
- Task: `blind_p2_determinant_fibre_rederivation`
- Role: blind rederiver, statement-only
- Status: candidate evidence only

## 1. Result: exact two-orientation fibre lemma and a scoped no-go

The two orientations have genuinely different determinant fibres after the
lower-close coordinate is frozen.

For the plus orientation, with close defect \(\delta=\Delta_-\) and positive
far defect \(F=\Delta_+\), fixing \((U,\kappa,h,\delta)\) gives the divisor
fibre

\[
 v(\kappa v+F)=2h-U\delta+\kappa U^2.                         \tag{1.1}
\]

Consequently the algebraic multiplicity is at most the divisor count of the
right-hand side; all physical and literal predicates only restrict this
divisor set.

For the minus orientation, if \(\delta=(d-gm)/g\) is the close defect and
\(F=-(d'-gm')/g>0\) is the positive far defect, fixing
\((U,\kappa,h,\delta)\) gives instead

\[
 \kappa v^2+\delta v+2h\equiv0\pmod U,
 \qquad
 F=\frac{2h+\delta v+\kappa v^2}{U}-\kappa U.                \tag{1.2}
\]

This is a quadratic-congruence fibre, not a divisor fibre. It can have
\(\gg\sqrt U\) physical members with the same exact determinant \(h\), the
same close defect, and (after passage to one of at most two adjacent dyadic
blocks) the same far-defect block. An explicit family is proved below.

It follows rigorously that a scalar, coefficient-blind determinant-incidence
bound, or a \(TT^*\) argument invariant under replacement by arbitrary
bounded coefficient vectors, cannot prove (I195.2). On the explicit minus
fibre the phase-aligned bounded-array shadow has a rank-one Gram block of
size \(n\gg\sqrt U\), with squared norm \(n^2\). This supplies all of the
required unsigned, character-erased, and adversarial failures. It also shows
why taking separate orientation norms cannot be the missing mechanism.

This is a method no-go, not a disproof of the literal estimate (I195.2).
The actual endpoint/profile/Vaaler/carry/birth-death/mask-commutator vectors
might cancel on these fibres. The isolated statement does not give those
vectors, so the coefficient-sensitive Gram inequality needed to decide that
question cannot be verified. Thus (I195.2), (I195.3), and the fixed-to-outer
power ledger remain open.

## 2. Exact statement and hypotheses

Assume exactly the physical atom, packet, hard mask, and literal-core
hypotheses of the isolated statement. In particular the mask is applied
before Fourier expansion and height differencing, \(U=\mathfrak m q\), and
\(\mathfrak m\) (the spectral lift gcd) is never identified with \(\kappa\)
(the physical cofactor). Put

\[
 H_0(g,\kappa)=\left\lfloor\frac{R_0-1}{2g\kappa}\right\rfloor.
\]

In either orientation one has \(r=2g\kappa h\), hence
\(1\le h\le H_0(g,\kappa)\). Since \(d,d'\) are odd, \(g,\kappa,U\) are
odd in these charts. Exact primitivity of \(g=(d,d')\) implies

\[
 (\kappa U,\kappa U+2S)=1,
 \qquad (\kappa U,S)=1.                                     \tag{2.1}
\]

The plus chart is the one in the statement. Write

\[
 \delta=\kappa(U-v)-2w,\qquad
 F=\kappa(U-v)+2S.
\]

Then

\[
 |g\delta|\le D_L,\qquad gF>D_L,\qquad
 F-\delta=2(S+w),                                           \tag{2.2}
\]

and

\[
 2h=vF+U\delta-\kappa(U^2-v^2).                            \tag{2.3}
\]

For fixed \((g,\delta,E,h)\), the exact algebraic far-fibre multiplicity is

\[
 M_+(g,\delta,E;h)
 =\#\left\{
 \begin{array}{l|l}
 v\in\mathbb Z_{>0}&
 v\mid C_+,\quad F=C_+/v-\kappa v,\\
 &E<gF\le2E,\\
 &w=(\kappa(U-v)-\delta)/2>0,\\
 &S=(F-\kappa(U-v))/2>0,\\
 &\text{all physical integrality, range, primitive, and literal predicates}
 \end{array}\right\},                                      \tag{2.4}
\]

where \(C_+=2h-U\delta+\kappa U^2\). In particular

\[
 M_+(g,\delta,E;h)\le \tau(C_+)                            \tag{2.5}
\]

whenever the fibre is nonempty (then \(C_+>0\)). Formula (2.4), rather than
an unqualified divisor bound, is the exact multiplicity because it retains
the parity, positivity, physical ranges, and predicates.

The signed minus chart is

\[
 d=g(\kappa U+2S),\quad d'=\kappa gU,\quad
 m=\kappa v,\quad m'=\kappa v+2w,\quad h=Uw-Sv>0.           \tag{2.6}
\]

Define

\[
 \delta=\frac{d-gm}{g}=\kappa(U-v)+2S,
 \qquad
 F=-\frac{d'-gm'}g=\kappa(v-U)+2w.                         \tag{2.7}
\]

On \(P_2\),

\[
 |g\delta|\le D_L,\qquad gF>D_L,\qquad
 \delta+F=2(S+w),                                          \tag{2.8}
\]

and the signed raw upper defect is \(-F\). The determinant identity is

\[
 2h=UF-v\delta+\kappa(U^2-v^2).                            \tag{2.9}
\]

Thus the exact minus multiplicity is

\[
 M_-(g,\delta,E;h)
 =\#\left\{
 \begin{array}{l|l}
 v\in\mathbb Z_{>0}&
 U\mid \kappa v^2+\delta v+2h,\\
 &F=(2h+\delta v+\kappa v^2)/U-\kappa U,\\
 &E<gF\le2E,\\
 &S=(\delta-\kappa(U-v))/2>0,\\
 &w=(F+\kappa(U-v))/2>0,\\
 &\text{all physical integrality, range, primitive, and literal predicates}
 \end{array}\right\}.                                      \tag{2.10}
\]

There is no divisor-count conclusion analogous to (2.5). One always has
the necessary discriminant congruence

\[
 (2\kappa v+\delta)^2\equiv\delta^2-8\kappa h\pmod U,       \tag{2.11}
\]

and (2.11) is equivalent to the congruence in (2.10) if
\((\kappa,U)=1\). No coprimality of \(\kappa\) and \(U\) was stated, so that
equivalence is not used without its displayed extra hypothesis.

The exact equal-determinant collision equations for two atoms in a fixed
packet are

\[
 \kappa(v^2-v'^2)+vF-v'F'+U(\delta-\delta')=0              \tag{2.12+}
\]

in the plus orientation, and

\[
 U(F-F')-v\delta+v'\delta'-\kappa(v^2-v'^2)=0              \tag{2.12-}
\]

in the minus orientation. With the close defect fixed, these become

\[
 \kappa(v^2-v'^2)+vF-v'F'=0,                               \tag{2.13+}
\]

\[
 U(F-F')=(v-v')\{\delta+\kappa(v+v')\}.                   \tag{2.13-}
\]

The determinant-residue collision equations modulo \(U\) are

\[
 v(F+\kappa v)\equiv v'(F'+\kappa v')\pmod U              \tag{2.14+}
\]

and

\[
 v(\delta+\kappa v)\equiv v'(\delta'+\kappa v')\pmod U.   \tag{2.14-}
\]

For fixed \(\delta\), the minus residue equation factors as

\[
 (v-v')\{\delta+\kappa(v+v')\}\equiv0\pmod U;             \tag{2.15}
\]

the far defects have disappeared. In the plus orientation, for fixed
\(v\) the admissible same-residue far defects have exact spacing
\(2U/(v,U)\), because \(F\equiv\delta\pmod2\) and \(U\) is odd. These
congruence collisions are only determinant-phase collisions; the literal
core may carry additional effective phases.

Because the orientations remain in one aggregate, the cross-orientation
equal-determinant equation must also be retained. With subscripts denoting
the two charts it is

\[
 \kappa(v_+^2+v_-^2-2U^2)+v_+F_++v_-\delta_-
 +U(\delta_+-F_-)=0,                                      \tag{2.15x}
\]

and its determinant-residue version is

\[
 v_+(F_++\kappa v_+)+v_-(\delta_-+\kappa v_-)
 \equiv0\pmod U.                                          \tag{2.15y}
\]

Frequency-sign collisions insert the corresponding signs in these
equalities. They too are only necessary collision equations for the full
effective phase.

Finally, let \(\Lambda\) be the common zero-extended index set for the full
anchor Fourier sum, both frequency signs, endpoints, carries, affine sites,
births/deaths, crossings, conjugations, and both orientations. For an atom
\(\alpha\), let

\[
 z_{\alpha,\lambda}=c_{\alpha,\lambda}e(\theta_{\alpha,\lambda})
\]

denote the actual coefficient and all of its actual phases; the physical
mask commutator is part of \(c_{\alpha,\lambda}\). With the inherited outer
normalization absorbed into these entries, the genuinely relevant vector
inequality is

\[
 \left|\operatorname {Re}
 \sum_{\lambda\in\Lambda}
 \sum_{\omega\in\{+,-\}}
 \sum_{g,\delta,E,h}
 \sum_{\alpha\in\mathcal F_\omega(g,\delta,E;h)}
 z_{\alpha,\lambda}\right|
 \ll Q\mathfrak m\kappa uX^\varepsilon.                    \tag{2.16}
\]

There is one real part, after the two orientations and frequency signs have
been combined. A \(TT^*\) implementation of (2.16) must, with the exact
inherited dual norm, prove the literal Gram bound

\[
 \sup_{\|b\|_{\mathrm{out},*}\le1}
 \sum_{\alpha,\alpha'} A_\alpha(b)\overline{A_{\alpha'}(b)}
 \ll (Q\mathfrak m\kappa uX^\varepsilon)^2,
 \qquad
 A_\alpha(b)=\sum_{\lambda}b_\lambda z_{\alpha,\lambda}.   \tag{2.17}
\]

This retains the diagonal, all collision blocks, unequal supports, and zero
extensions. It is not an arbitrary-vector large sieve. The positive
capacity and target envelopes are

\[
 M_{\rm cap}=Y\kappa uX^\varepsilon,\qquad
 K=Q\mathfrak m\kappa uX^\varepsilon,\qquad
 J=\frac{M_{\rm cap}}K=\frac{Y}{Q\mathfrak m}>1.            \tag{2.18}
\]

Thus the full factor \(J\) (or \(J^2\) after squaring) has to be recovered
before positive outer norms. This compares the two stated envelopes only;
it does not assert the optional stronger contraction relative to the exact
positive mass of every packet.

## 3. Proof and derivation

### 3.1 Plus orientation

Direct multiplication gives

\[
 d'm'-dm
 =g(\kappa U+2S)\kappa v-\kappa gU(\kappa v+2w)
 =2g\kappa(Sv-Uw)=2g\kappa h.                              \tag{3.1}
\]

The two defect identities and their difference are immediate:

\[
 d-gm=g\{\kappa(U-v)-2w\}=g\delta,
\]

\[
 d'-gm'=g\{\kappa(U-v)+2S\}=gF,
 \qquad F-\delta=2(S+w)>0.                                 \tag{3.2}
\]

If \(|g\delta|\le D_L\) and \(|gF|>D_L\), (3.2) forces
\(gF>D_L\). Substituting

\[
 2S=F-\kappa(U-v),\qquad 2w=\kappa(U-v)-\delta
\]

into \(2h=2Sv-2Uw\) gives (2.3). Rearranging gives (1.1).
Every positive divisor \(v\mid C_+\) determines at most one \(F\), and then
at most one \((S,w)\). This proves (2.4)--(2.5). Subtracting two copies of
(2.3) proves (2.12+) and (2.13+); reducing modulo \(U\) proves (2.14+).

### 3.2 Minus orientation

For (2.6),

\[
 d'm'-dm
 =\kappa gU(\kappa v+2w)-g(\kappa U+2S)\kappa v
 =2g\kappa(Uw-Sv)=2g\kappa h.                              \tag{3.3}
\]

Furthermore,

\[
 d-gm=g\{\kappa(U-v)+2S\}=g\delta,
\]

\[
 d'-gm'=g\{\kappa(U-v)-2w\}=-gF,
 \qquad \delta+F=2(S+w)>0.                                \tag{3.4}
\]

The upper defect must therefore be \(<-D_L\) on \(P_2\). Substitution of

\[
 2S=\delta-\kappa(U-v),\qquad
 2w=F+\kappa(U-v)
\]

into \(2h=2Uw-2Sv\) gives (2.9). Rearrangement gives (1.2) and the exact
count (2.10). Multiplication of the quadratic congruence by \(4\kappa\)
gives (2.11). Subtraction gives (2.12-)--(2.15).

The close mask also gives the required uniform bound on \(g\). If
\(cL\le d,m\le CL\), then

\[
 g\le \frac{d+D_L}{m}\le C/c+O(L^{-1/2}),                 \tag{3.5}
\]

so \(g=O(1)\) with a constant depending only on the fixed shell convention.
The positive far defect is \(O(L)\), so the intervals
\(E<gF\le2E\), \(E\ge D_L\), give the required dyadic partition without
widening \(D_L\).

### 3.3 An exact large minus fibre

Let \(p=4k+1\) tend through odd integers, put

\[
 L=U=p^2,\qquad g=\kappa=1,\qquad
 \delta=p-1,\qquad h=2k^2=\frac{(p-1)^2}{8}.               \tag{3.6}
\]

For every \(t\equiv0\pmod4\) with \(2\le t\le p-1\), define

\[
 \begin{aligned}
 d'&=p^2,&m'&=(p+t)^2,\\
 d&=p^2+pt+\frac{p-1}{2},&
 m&=p^2+pt-\frac{p-1}{2}.
 \end{aligned}                                             \tag{3.7}
\]

All four variables are odd and \(\asymp L\). Since
\(d\equiv(p-1)/2\pmod p\), one has \((d,d')=1=g\). Also

\[
 d-m=p-1=\delta,\qquad
 d'-m'=-(2pt+t^2)=-F_t,                                    \tag{3.8}
\]

so \(|\delta|=p-1\le D_L=p\) and \(F_t>D_L\). Finally,

\[
 d'm'-dm=\frac{(p-1)^2}{4}=2h,\qquad
 0<2h<p^2=R_0.                                             \tag{3.9}
\]

The corresponding minus-chart variables are

\[
 v=p^2+pt-\frac{p-1}{2},\quad
 S=\frac{pt+(p-1)/2}{2},\quad
 w=\frac{pt+t^2+(p-1)/2}{2},                               \tag{3.10}
\]

which are positive integers. Equivalently,

\[
 v^2+\delta v+2h=(p^2+pt)^2,\qquad
 F_t=\frac{v^2+\delta v+2h}{p^2}-p^2=2pt+t^2.              \tag{3.11}
\]

Thus all of (3.7) lie in one exact \((U,\kappa,g,h,\delta)\) determinant
fibre. Restricting to \(p/4\le t\le p/3\) leaves \(\gg p\) values and

\[
 \frac{9}{16}p^2\le F_t\le\frac79p^2.                     \tag{3.12}
\]

This interval meets at most two adjacent standard dyadic far blocks, so one
block contains \(\gg p=\sqrt U\) members. Restricting to
\(t\equiv0\pmod4\) also makes the residues modulo \(4\) of each of
\(d,d',m,m'\) constant along the selected family. Hence a bare \(\chi_4\)
depending on these four residues does not disperse this subfamily. This last
observation does not cover character factors at unspecified affine sites.

The family is a physical-chart and determinant-fibre construction. The
isolated packet does not define its residual and squarefree predicates or
literal endpoint weights, so it is not asserted that all of these atoms
have nonzero coefficients in the actual core.

### 3.4 Literal Gram requirement and the no-go

For a fibre \(\mathcal F\), (2.17) contains the exact self-return block

\[
 \left|\sum_{\alpha\in\mathcal F}A_\alpha(b)\right|^2
 =\sum_{\alpha\in\mathcal F}|A_\alpha(b)|^2
  +\sum_{\substack{\alpha,\alpha'\in\mathcal F\\\alpha\ne\alpha'}}
    A_\alpha(b)\overline{A_{\alpha'}(b)}.                  \tag{3.13}
\]

The first sum is the literal diagonal. The second includes the exact
equal-\(h\) collisions in (3.7). Replacing actual vectors by their norms
gives

\[
 \left|\sum_{\alpha\in\mathcal F}A_\alpha(b)\right|^2
 \le \#\mathcal F\sum_{\alpha\in\mathcal F}|A_\alpha(b)|^2,\tag{3.14}
\]

and (3.14) is sharp: in the arbitrary bounded, phase-conjugated shadow set
all \(A_\alpha(b)=1\). Its Gram matrix is the all-ones matrix; its only
nonzero eigenvalue is \(\#\mathcal F\), and the squared coherent sum is
\((\#\mathcal F)^2\).

This shadow can be placed in the displayed \(T=0\) packet regime. For
example take \(\mathfrak m=\kappa=u=1\), \(q=U=p^2\), choose an admissible
\(a\) with \(|a|_q>Q\) (for example the least-residue class represented by
\((q-1)/2\)), and take \(Y=2QU\). For large \(p\), \(U>4Q\)
and

\[
 T=\left\lfloor\frac{QU}{Y}\right\rfloor=0.               \tag{3.15}
\]

If, for definiteness, \(X=p^4\), then with any fixed
\(0<\varepsilon<1/4\) small enough (for example \(\varepsilon=1/8\)) the
coherent \(\gg p\) shadow exceeds
\(QX^\varepsilon=Qp^{4\varepsilon}\) as \(p\to\infty\). It respects the
stated capacity envelope because \(p\ll Y\). Thus a theorem that survives
arbitrary bounded replacement, character erasure, or phase conjugation is
false even in the explicitly retained \(T=0\) branch. In this shadow all
other atom coefficients are set to zero, while the selected fibre
coefficients conjugate their phases; both operations are allowed by the
arbitrary bounded-array control but are not asserted for the literal core.

For the actual operator, the only possible repair at this seam is an
estimate of the literal inner products in (3.13), simultaneously across
endpoints, carries, births/deaths, mask commutators, frequency signs, and
orientations. The quadratic multiplicity alone supplies no such estimate.
The actual coefficient vectors are not present in the permitted packet, so
(2.17) cannot be proved or refuted here.

## 4. First doubtful or unproved step

The first unproved step in every positive determinant-fibre route is the
passage from the exact arithmetic fibres (2.4) and (2.10) to cancellation
of the literal vectors in (2.17). The statement lists the coefficient
ingredients but supplies neither their formulas nor their translation,
carry, endpoint, birth/death, and mask-commutator incidence maps. Therefore
one cannot determine:

1. which members of the large family (3.7) survive the actual selectors;
2. whether their complete effective phases collide after the square-root
   and anchor phases are included;
3. whether unequal supports have cancelling or reinforcing literal Gram
   inner products; or
4. whether the exact diagonal has the normalization required by (2.17).

Using only \(h\bmod U\), a divisor count, a quadratic-root count, or a
positive norm at this point would silently replace the actual vectors by an
arbitrary bounded array and is ruled out by (3.13)--(3.15).

There is a second, downstream information gap: the isolated packet gives no
outer packet measure, packet count, or inherited weights from which the
implication (I195.2) \(\Rightarrow\) (I195.3) can be power-counted. Hence the
fixed-packet-to-outer ledger cannot be independently certified from the
permitted files.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `exact_round193_P2_physical_mask` | Pass for scope: only \(|d-gm|\le D_L\), \(|d'-gm'|>D_L\) was used. The historical round was not read. |
| `mask_before_Fourier_and_height_difference` | Pass: \(P_2\) is treated as physical input to the rerun core; no post-expansion scalar mask is introduced. |
| `exact_round192_core_and_T_zero_scope` | Pass for scope, unresolved analytically: the inherited exact core is not simplified, and \(T=0\) is explicitly retained in (3.15). The historical round was not read. |
| `strict_T_positive_Farey_covectors` | Retained, not used to delete atoms. No claim is made that the large fibre survives a particular strict retained row because \(\beta,\rho\) and the coefficient map are not supplied. |
| `spectral_lift_gcd_vs_physical_cofactor_notation` | Pass: \(\mathfrak m\) and \(\kappa\) remain distinct throughout. |
| `both_orientation_primitive_charts` | Pass: (2.2)--(2.5) and (2.6)--(2.10) treat both signed charts. |
| `Delta_minus_Delta_plus_identity` | Pass: plus gives \(F-\delta=2(S+w)\); minus gives raw-upper minus close \(=-2(S+w)\), equivalently \(F+\delta=2(S+w)\). |
| `lower_close_uniform_g_bound` | Pass: (3.5) proves \(g=O(1)\) from the literal close mask and shell bounds. |
| `upper_failure_positive_far_defect` | Pass: plus has upper defect \(+gF>D_L\); minus has upper defect \(-gF<-D_L\). |
| `dyadic_far_defect_partition` | Pass: \(E<gF\le2E\) is retained, and (3.12) puts \(\gg\sqrt U\) collisions in one such block without changing \(D_L\). |
| `determinant_fibre_multiplicity` | Pass: exact counts are (2.4) and (2.10); plus is a divisor fibre, minus is a quadratic-congruence fibre with the explicit lower bound (3.12). |
| `actual_endpoint_coefficient_vectors` | Required but unavailable: encoded abstractly as the actual entries \(z_{\alpha,\lambda}\); never replaced in the proposed literal inequality. |
| `birth_death_zero_extension_vectors` | Pass for formulation: all sites are put in one common zero-extended \(\Lambda\), so births/deaths are not deleted before Gram formation. |
| `physical_mask_commutator` | Pass for formulation: the commutator is part of \(c_{\alpha,\lambda}\), not discarded. Its formula is unavailable. |
| `one_outer_real_part` | Pass: (2.16) combines orientations and frequency signs before one real part. |
| `TTstar_Gram_before_positive_norms` | Pass as a requirement: (2.17) is the needed literal Gram statement; no positive coefficient norm is taken first. |
| `Gram_diagonal_and_phase_collisions` | Pass: (3.13) displays the exact diagonal and self-return block; (3.7) supplies exact equal-\(h\) collisions. |
| `off_diagonal_determinant_fibres` | Pass: exact and modular same- and cross-orientation collision equations are (2.12+)--(2.15y). |
| `Y_over_HBmfrak_deficit` | Pass: (2.18) records the unsaved factor \(Y/(Q\mathfrak m)\), and its square after \(TT^*\). |
| `fixed_packet_to_outer_power_ledger` | Blocked by missing outer weights and packet measure; no implication to (I195.3) is asserted. |
| `unsigned_character_erased_adversarial_controls` | Correct failure: equal phase-conjugated vectors on (3.7) give coherent size \(\gg\sqrt U\); a fixed modulo-4 subfamily also prevents a bare \(\chi_4\) residue change from manufacturing dispersion. |
| `no_arbitrary_bounded_coefficient_closure` | Pass: (3.14)--(3.15) rigorously reject any closure stable under arbitrary bounded replacement. |
| `no_separate_orientation_norm` | Pass: (2.16) is joint. The obstruction already occurs inside the minus orientation, so separately bounding orientations cannot create the missing cancellation. |
| `no_width_Farey_or_proper_submask_escape` | Pass: \(D_L=p\) is unchanged; the strict Farey conditions are not enlarged; the dyadic family is used only as an obstruction and is not claimed as completion of full \(P_2\). Its complement remains unpriced. |
| `diagnostic_only_computation` | Pass: no numerical or symbolic computation was used; (3.6)--(3.12) are exact algebra. |
| `original_t1_only_downstream_scope` | Pass: no claim is made for \(P_1\), other original-\(t\) incidences, M1/M2 parents, bridges, or endpoints. |
| `exponent_quarantine` | Pass: no Gauss-circle bound or exponent is inferred. |

## 6. Dependencies and exact artifacts used

Only the following three permitted files were used:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/blind_statement.md` (reloaded after the byte-clean repair); and
3. `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/briefs/blind_p2_determinant_fibre_rederivation.md`.

No graph, active campaign, strategy file, source card, web result, proof draft,
prior round, sibling artifact, synthesis, or control output was read. No web
source or computation was used.

## 7. Recommended state effect

**Retain (I195.2) and (I195.3) as open; reject the coefficient-blind
determinant-fibre/positive-Gram route.** After independent review, the exact
two-orientation fibre identities, collision equations, and the scoped
arbitrary-coefficient no-go may be retained as candidate evidence. A future
round would have to supply and prove the literal vector Gram estimate
(2.17), especially on the minus quadratic fibres, without separate
orientation norms and in both \(T\)-branches. No promotion beyond the full
\(P_2\) fixed-packet seam is recommended.
