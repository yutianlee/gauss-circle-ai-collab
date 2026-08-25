# Round 133 post-unmask discovery seam: capacity and coefficient ownership

Campaign: `gc-w7-16-bombieri-iwaniec-two-spacing-source-map`

Review: `discovery_post_unmask_capacity_and_owner_audit`

Starting graph SHA-256:
`465093c00a388ff9e49583a8016e0e580f74beea4656b15884fdd9dc9247be5a`

## 1. Result: scoped black-box no-go, with two explicit corrections

The post-unmask artifacts agree on the exact single-wave phase and
Bombieri--Iwaniec power dictionary, the project-ray/derivative-approximant
role separation, and the first joint-coefficient mismatch.  The appropriate
round label remains

\[
 \boxed{\texttt{source\_level\_no\_go}}
 \tag{133.R1}
\]

only in the following scoped sense:

> Applying the repaired Li--Yang estimate independently to two full-scale,
> normalized, separably weighted waves, while granting a zero-cost
> rank-one connector and zero-cost one-sided/taper projection, yields
> \(Y^{2\Phi(-1/3)+\varepsilon}\), which is still above \(Y^{27/48}\).
> The literal scalar does not even satisfy those granted coefficient
> hypotheses.

This is a no-go for that **two-independent-\(S\) black-box interface**.  It
is not a theorem that the Bombieri--Iwaniec method, a new joint double large
sieve, or a genuinely determinant-adapted spacing theorem can never produce
a stronger estimate.

Two statements in the discovery report
`reports/literal_joint_scalar_bi_normal_form_map.md` require explicit
correction.

1. Its Sections 3.1, 3.6, and control table treated the M1
   denominator mod-four carrier as incurring normalized BV cost
   \(D/L=Y^{1/3}\).  That is an unnecessarily crude representation.
   M1 is handled by four denominator residue classes and a progression
   reparameterization; M2 is handled by the two-term Fourier expansion of
   \(\chi_4\).  Both carrier splits cost \(O(1)\).  They do not solve the
   remaining joint primitive/profile/owner problem.
2. Its Section 3.4 called
   \((k,lk,l\sqrt{k},l/\sqrt{k})\) the exact source four-vector.  The v2
   source is internally inconsistent: the exact first-spacing norm and the
   introductory four-vector start with \(l\), while the later Section-4
   sketch prints \(k\).  The first-coordinate power table in that report is
   therefore conditional on the later sketch, not source-certified.

After these corrections, the first project mismatch is still the absence
of an owner-preserving decomposition of the moving determinant wedge and
joint physical coefficient into source-compatible separated BV data,
together with the source's arcwise positive absolute-value direction.

## 2. Exact statement and hypotheses

Fix the literal top shell

\[
 W=Y^{7/16},\qquad D=Y^{1/2},\qquad L=Y^{1/6},\qquad
 c\asymp Y,\qquad \kappa_1=1,\quad \kappa_2=4,             \tag{133.R2}
\]

and the one-sided determinant scalar

\[
 \mathfrak O^+_{i,D}(c)
 =\sum_{r=(a,b)}^{\rm lit}A_i(r)
   \sum_{r'=(a',b')}^{\rm lit}B_i(r,r')
   e\!\left(\frac{ca}{\kappa_i b}
            -\frac{ca'}{\kappa_i b'}\right),              \tag{133.R3}
\]

where

\[
 n=ab'-a'b>0,\qquad
 \left(1-\frac{Wn}{\kappa_i bb'}\right)_+                 \tag{133.R4}
\]

and every primitive lift, Möbius/Stieltjes profile, threshold, star,
quarter or \(\chi_4\) carrier, reciprocal alias, cell, sign, and half-open
owner remain inside the literal coefficient.

The source standard sum is

\[
 S=\sum_{h\asymp H}g(h/H)\sum_{m\asymp M}G(m/M)
 e\!\left(\frac{hT}{M}F(m/M)\right),                     \tag{133.R5}
\]

with separated, fixed-BV one-variable weights.  The exact unrestricted
single-wave map is

\[
 h=a,\qquad m=b,\qquad H=L,\qquad M=D,\qquad
 T=c/\kappa_i,\qquad F(z)=z^{-1}.                         \tag{133.R6}
\]

After a numerator-sign split, (133.R6) gives the exact geometric phase.
The source-condition seam is now settled for this review:

* the actual Lemma-4.1 condition is (4.6), with \(N\) defined by (4.8);
* printed (4.9) is not the algebraic substitution of (4.8) into (4.6);
* the corrected final relation \(H/M=T^x\) and source check (5.23) verify
  (4.6) directly on the narrow final range;
* at \(x=-1/3\), (4.6) has fixed positive power slack.

Thus printed (4.9) is not used as a no-go.  The parameter tuple is audited
through the repaired original condition.

The zero-cost two-wave diagnostic below assumes, counterfactually, all of:

1. the physical coefficient is one normalized rank-one product of two
   fixed-BV source weights, with the factor \(L^{-1}\) on each wave;
2. the \(n>0\) projection and determinant taper have projective cost one;
3. the finite sign, mod-four, star, cell, and owner splits have total cost
   \(Y^{o(1)}\);
4. the repaired optimized source bound applies independently to both
   factors.

These assumptions are deliberately more favorable than the literal scalar.
They define the exact scope of the capacity obstruction.

## 3. Proof and reconciliation

### 3.1 Phase, derivatives, source conditions, and parameter powers

Under (133.R6),

\[
 \frac{hT}{M}F(m/M)
 =\frac{a(c/\kappa_i)}{D}\frac{D}{b}
 =\frac{ca}{\kappa_i b}.                                  \tag{133.R7}
\]

For \(F(z)=z^{-1}\),

\[
 F'=-z^{-2},\qquad F''=2z^{-3},\qquad F'''=-6z^{-4},
 \qquad F'F'''-3(F'')^2=-6z^{-6},                         \tag{133.R8}
\]

so both source phase conditions hold uniformly on \([1,2]\).

At the critical powers,

\[
 T\asymp Y,\qquad H=Y^{1/6},\qquad M=Y^{1/2},\qquad
 \frac HM=T^{-1/3}.                                       \tag{133.R9}
\]

The repaired Case-A conditional lower clauses are inactive because
\(T^{7/16}<M<T^{9/16}\), and

\[
 H<MT^{-49/164}
\]

with margin \(T^{-17/492}\).  With logarithmic factors suppressed only in
the power notation,

\[
\begin{array}{c|c}
\text{source parameter}&Y\text{-power}\\ \hline
N_A&67/300\\
R=(M^3/(N_AT))^{1/2}&83/600\\
Q=Y^u&83/600\le u\le1/6\\
L_{\rm sp}=HQ/R^2&u-11/100\\
K_{\rm sp}=N_AQ/R^2&u-4/75\\
\eta=R^2/(N_AH)&-17/150.
\end{array}                                                \tag{133.R10}
\]

At \(Q=R\),

\[
 L_{\rm sp}=Y^{17/600+o(1)},\qquad
 K_{\rm sp}=Y^{17/200+o(1)},\qquad
 K_{\rm sp}L_{\rm sp}=\eta^{-1}=Y^{17/150+o(1)}.          \tag{133.R11}
\]

The source moment and optimized exponent are

\[
 q_*=\frac{250+10\sqrt{170}}{91}=4.180044\ldots,\qquad
 \Phi(-1/3)=\frac{29+5\sqrt{170}}{300}
 =0.3139734135\ldots .                                    \tag{133.R12}
\]

The quotient in the original condition (4.6) has \(T\)-power

\[
 E(-1/3,q)=\frac{17(6-q)}{300}>0,                         \tag{133.R13}
\]

so the repaired source gate passes.  The blind \(q=4\) exponent
\(377/1200\) is a legal nonoptimal alternative, not a conflicting value
of \(\Phi(-1/3)\).

### 3.2 Correct owner treatment of the M1 and M2 mod-four carriers

For M1, fix one denominator residue \(r_0\pmod4\), write

\[
 b=4m+r_0,\qquad M_0=D/4,
\]

and put

\[
 F_{r_0}(z)=\frac{1}{4z+r_0/M_0},\qquad z=m/M_0,\qquad T=c.
 \tag{133.R14}
\]

Then

\[
 \frac{aT}{M_0}F_{r_0}(m/M_0)=\frac{ca}{b},              \tag{133.R15}
\]

while each quarter carrier satisfies

\[
 e(\sigma b/4)=e(\sigma r_0/4),\qquad \sigma=\pm1,       \tag{133.R16}
\]

because \(m\in\mathbb Z\).  The functions \(F_{r_0}\) satisfy the two
source phase conditions with constants uniform in the four residues for
large \(D\).  Hence two branches times four residues cost \(O(1)\), and
all source powers are unchanged.

For M2, on the physical nonzero numerator support,

\[
 \epsilon_{\rm sgn}\chi_4(|a|)=\chi_4(a)
 =\frac{1}{2i}\sum_{\tau=\pm1}\tau e(\tau a/4).           \tag{133.R17}
\]

Use \(T=c\), \(M=D\), and

\[
 F_\tau(z)=\frac{1}{4z}+\tau\frac{M}{4T}.                 \tag{133.R18}
\]

Then

\[
 \frac{aT}{M}F_\tau(b/M)
 =\frac{ca}{4b}+\frac{\tau a}{4}.                         \tag{133.R19}
\]

The constant shift in (133.R18) does not change any derivative, so both
source phase conditions remain valid.  This is exactly a two-term Fourier
split and costs \(O(1)\).

Therefore the mod-four carriers themselves are **not** a \(D/L\) BV
obstruction.  Intersecting a literal owner with finitely many residue or
Fourier branches adds only \(O(1)\) endpoints.  What remains joint is the
variable primitive support, lift selector, Möbius/Stieltjes profile,
threshold/taper, reciprocal alias, and moving determinant boundary.  The
carrier correction removes one false cost but supplies no separated
projective norm for those factors.

### 3.3 Precise derivation and scope of the zero-cost two-wave capacity

Let \(S_1,S_2\) be two hypothetical source sums with fixed BV norms and the
full scales \(H=L,M=D\).  The optimized repaired source conclusion is

\[
 \frac{|S_j|}{H}\ll Y^{\Phi(-1/3)+\varepsilon},
 \qquad j=1,2.                                            \tag{133.R20}
\]

The natural project ray coefficient contributes \(L^{-1}\) to each factor.
Since \(H=L\), the normalized waves

\[
 U_j=L^{-1}S_j
\]

satisfy

\[
 |U_j|\ll Y^{\Phi(-1/3)+\varepsilon}.                    \tag{133.R21}
\]

Granting for free the rank-one identity, one-sided determinant projection,
taper, and every owner therefore gives

\[
 |\mathfrak O^+_{i,D}(c)|
 \ \stackrel{\rm granted}{\ll}\
 |U_1U_2|
 \ll Y^{2\Phi(-1/3)+\varepsilon},                         \tag{133.R22}
\]

where

\[
 2\Phi(-1/3)=\frac{29+5\sqrt{170}}{150}
 =0.6279468270\ldots=\frac{30.1414\ldots}{48}.            \tag{133.R23}
\]

The exact threshold gaps are

\[
\begin{aligned}
2\Phi(-1/3)-\frac{27}{48}
 &=\frac{40\sqrt{170}-443}{1200}>0,\\
2\Phi(-1/3)-\frac{24}{48}
 &=\frac{5\sqrt{170}-46}{150}>0.
\end{aligned}                                             \tag{133.R24}
\]

Thus even this zero-cost two-black-box connector cannot cross \(27/48\).
The blind choice \(q=4\) gives a slightly weaker square and reaches the
same qualitative conclusion.

Equation (133.R22) is not a theorem for the literal scalar: its
rank-one/projective and projection hypotheses are absent.  Nor is
(133.R24) a universal Bombieri--Iwaniec barrier.  A new joint DLS theorem
could use the determinant band before taking arcwise absolute values,
correlate the two derivative-approximant systems, or produce a negative
projective power that is not visible in two independent \(S\)-bounds.
Such an input would be a different theorem and is not ruled out here.
Likewise, the statement that one genuine unnormalized source \(S\) obeys
\(S\ll Y^{1/6+\Phi+\varepsilon}<Y^{24/48+\varepsilon}\) is perfectly
consistent with (133.R22): the project target is a normalized pair form,
not one source sum.

The corrected conclusion is therefore:

\[
\boxed{\text{no }<27/48\text{ consequence from two independent full-scale
Li--Yang }S\text{ black boxes with nonnegative connector cost}.}
\tag{133.R25}
\]

### 3.4 First-spacing first-coordinate mismatch

The exact first-spacing norm printed in Section 3 is

\[
 G_q=
 \left\|\sum_{k\sim K_{\rm sp}}\sum_{l\sim L_{\rm sp}}a_{kl}
 e(lx_1+klx_2+l\sqrt{k}\,x_3)\right\|_{L^q_\#},
 \qquad |a_{kl}|\le1.                                    \tag{133.R26}
\]

The introduction correspondingly displays the four-vector

\[
 (l,kl,l\sqrt{k},l/\sqrt{k}).                            \tag{133.R27}
\]

The later Section-4 sketch instead prints

\[
 (k,lk,l\sqrt{k},l/\sqrt{k}).                            \tag{133.R28}
\]

The v2 source gives no reconciliation.  At \(Q=R\), the disputed first
coordinate has power \(17/600\) if it is \(l\), but \(17/200\) if it is
\(k\).  The discovery report's table used the second value and must be
read conditionally.  A literal application must return to the upstream
Poisson/DLS formula and fix the first coordinate before matching its dual
spacing tolerance.

This source mismatch is separate from, and later than, the project
coefficient obstruction.  Under either first coordinate, the project
primitive ray \((a,b)\) is the original source summation point
\((h,m)\), whereas \(a_{\rm BI}/r_{\rm BI}\) is a derivative approximant
of size \(1\) with \(r_{\rm BI}\le Y^{1/6}\).  Neither choice turns the
project determinant into the source four-coordinate spacing problem.

### 3.5 Moving wedge, aligned packets, and distinct capacity ledgers

For fixed \(r=(a,b)\), the determinant band gives

\[
 a'=\frac ab\,b'+O(D/W),\qquad H_0=D/W=Y^{3/48}.          \tag{133.R29}
\]

The centre moves with \(b'\).  Keeping the drift within \(H_0\) restricts
a denominator cell to

\[
 M_0=\frac{D^2}{WL}=Y^{19/48},\qquad
 C_D=\frac{D}{M_0}=\frac{WL}{D}=Y^{5/48}.                \tag{133.R30}
\]

This is a moving wedge, not one source rectangle with a fixed separated
weight.  Formally replacing the source numerator length by \(H_0\) would
put \(H_0/D=Y^{-7/16}\), outside the optimized \(q>4\) final range.

The literal same-denominator controls are:

* M1: \(b'=b,\ a'=a-t,\ n=bt>0\), \(t\lesssim D/W\), with
  phase \(e(ct/b)\) and constant denominator carrier; integral \(c/b\)
  aligns the packet.
* M2: \(b'=b,\ a'=a-2j,\ n=2bj>0\); the physical character product is
  \((-1)^j\), and \(e(cj/(2b))\) aligns it when \(c/b\) is an odd integer.

These are per-ray hostile controls only.  One real centre does not align
every denominator, and the retained physical amplitudes may vanish or
cancel.

Three capacity ledgers must not be conflated.

1. The stripped geometric count is

   \[
   D\cdot L\cdot(D/W)=Y^{(24+8+3)/48}=Y^{35/48}.          \tag{133.R31}
   \]

2. The accepted literal physical capacity of **one aligned window** is

   \[
   D\cdot(D/W)\cdot(K_D/L)
   =Y^{(24+3+11-8)/48}=Y^{30/48},                         \tag{133.R32}
   \]

   because \(K_D=Y^{11/48+o(1)}\).  The \(C_D=Y^{5/48}\)
   moving-cell cover returns the accepted complete
   \(DK_D=Y^{35/48+o(1)}\) capacity.
3. Collapsing the determinant positions to one term per outer ray while
   retaining the physical inner scale gives

   \[
   D(K_D/L)=Y^{27/48+o(1)}.                               \tag{133.R33}
   \]

   The target \(D=Y^{24/48}\) needs one further \(Y^{-3/48}\).

The blind report's optimistic stripped expression \(D(D/W)=Y^{27/48}\)
assumes the remaining inner carrier has size \(O(1)\).  It is not the
literal one-window value (133.R32).  It happens to share the exponent in
(133.R33) because

\[
 K_D/L=Y^{3/48+o(1)}=D/W
\]

at the frozen scales.  This numerical coincidence does not identify the
two owners: one is determinant multiplicity, the other is the retained
physical inner coefficient scale.

## 4. First doubtful or unproved step

After the finite mod-four carrier splits in Section 3.2, the first
unproved project step is an exact, owner-preserving representation of the
moving-wedge coefficient:

\[
 C_i(r,r')=
 \sum_\nu \lambda_\nu\,u_\nu(r)\overline{v_\nu(r')},      \tag{133.R34}
\]

where every \(u_\nu,v_\nu\) is a legal source BV input after the same
short-interval, major/minor-arc, and Poisson transformations, and where the
projective source functional

\[
 \sum_\nu|\lambda_\nu|\,\mathcal N_{\rm LY}(u_\nu)
 \mathcal N_{\rm LY}(v_\nu)                              \tag{133.R35}
\]

has an explicitly favorable power.  No reviewed artifact proves
(133.R34)--(133.R35).

The source instead reaches a sum of absolute values over derivative-
approximant arcs and then positive first/second-spacing quantities.  Using
that direction on (133.R3) before proving (133.R34) deletes the signed
cross-ray cancellation.  Reversing the positive spacing functional is not
a source conclusion.

A later independent source-side uncertainty is the \(l\)-versus-\(k\)
first coordinate in (133.R27)--(133.R28).  Even after upstream repair, all
four source spacing coordinates and modular inverses still require a new
project map.

Therefore the precise missing hypothesis is the coefficient/owner
connector, not mod-four BV control.  The precise capacity obstruction is
only (133.R25), not a universal no-go for new BI machinery.

## 5. Control tests and outcomes

| Control | Outcome |
|---|---|
| exact phase and derivatives | Green: (133.R6)--(133.R8), after sign and dyadic splitting. |
| repaired source condition | Green in the narrow source scope: use (4.6) directly; printed (4.9) is false but bypassed by (5.23). |
| source parameter powers | Green: (133.R9)--(133.R13) distinguish project \(L,K_D\) from source \(L_{\rm sp},K_{\rm sp}\). |
| M1 mod-four owner | Corrected green: four denominator progressions and (133.R14)--(133.R16) cost \(O(1)\), not \(D/L\). |
| M2 mod-four owner | Green: the two Fourier branches (133.R17)--(133.R19) cost \(O(1)\) and retain the sign convention. |
| joint coefficient/projective norm | Red: finite carrier splitting leaves primitive, profile, taper, wedge, alias, star, cell, sign, and owner dependence joint. |
| zero-cost two-wave capacity | Green as a diagnostic only: (133.R20)--(133.R24) give \(30.1414\ldots/48>27/48\). |
| scope of no-go | Green after correction: (133.R25) concerns two independent source black boxes with nonnegative connector cost, not all BI/DLS mechanisms. |
| first-spacing vector | Red as a literal v2 source map: (133.R27) starts with \(l\), (133.R28) with \(k\); the discovery \(k\)-power was conditional. |
| ray versus approximant | Green no-conflation: \((a,b)\leftrightarrow(h,m)\); \(a_{\rm BI}/r_{\rm BI}\) is created later and has different ratio and denominator scale. |
| aligned M1/M2 packets | Green hostile controls with the exact character phases; no family lower bound is asserted. |
| capacity \(35,30,27,24\) | Green after owner separation: (133.R31)--(133.R33) distinguish raw count, literal packet, ideal floor, and target. |
| no positive energy/global promotion | Green: no SVD, row energy, spacing count, or aligned packet is promoted to a signed theorem. |

No numerical experiment was used.  Displayed decimals are evaluations of
exact radicals or rational exponents.

## 6. Dependencies and exact artifacts used

This post-unmask review used:

1. `protocol.md` and the active Round-133 scope;
2. `reports/literal_joint_scalar_bi_normal_form_map.md`, as the discovery
   claim under review;
3. `reports/li_yang_bi_exact_source_card.md`;
4. `reports/blind_double_large_sieve_feasibility.md`;
5. `candidates/conductor_single_wave_bi_parameter_map.md`;
6. `candidates/conductor_moving_wedge_role_control.md`;
7. `reviews/blind_post_unmask_source_condition_seam.md`;
8. the accepted Round-131 literal scalar and capacity statements already
   cited in the discovery report; and
9. the local official Li--Yang v2 TeX only through the exact source card
   and the displayed formulas independently reproduced here.

No shared proof state, synthesis, validation matrix, or sibling report was
edited.  No numerical experiment or new external source was used.

## 7. Recommended state effect

**Revise** the discovery candidate in two places:

* replace the claimed M1 \(D/L\) BV carrier charge by the \(O(1)\)
  residue/progression split in (133.R14)--(133.R16), and record the
  analogous \(O(1)\) M2 Fourier split;
* mark its first-spacing first-coordinate table as conditional because the
  v2 source prints both (133.R27) and (133.R28).

**Retain** the exact phase/parameter dictionary, the distinction between
project rays and derivative approximants, the joint coefficient and
absolute-value mismatch, and the aligned packet ledgers after the
owner-sensitive reconciliation in Section 3.5.

**Narrow** the capacity verdict to (133.R25): the repaired Li--Yang theorem
used twice as an independent full-scale black box cannot cross \(27/48\)
even with a zero-cost connector.  Do not phrase this as a universal
Bombieri--Iwaniec or double-large-sieve no-go.

Keep `GC-W7-16-actual-reduced-determinant-correlation` open at the accepted
\(Y^{35/48+\varepsilon}\) complete bound.  Make no M9-M1, M9-M2, endpoint,
bridge, M9, global-exponent, external-theorem, or quarter promotion.  This
review changes no shared state or synthesis.
