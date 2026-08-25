# Round 133 statement-only report: double-large-sieve feasibility

## 1. Result: interface no-go lemma

**Lemma (no literal cross-ray consequence from the supplied source interface).**  On the statement packet alone, the map

\[
h=a,\qquad m=b,\qquad H=L,\qquad M=D,\qquad
T=c/\kappa_i,\qquad F(z)=z^{-1}
\]

is a valid phase map for one unrestricted, separably weighted wave after sign and dyadic splitting.  It is not a map of the joint scalar \(\mathfrak O_{i,D}^{+}(c)\) into the source sum (133.S1), nor into an arbitrary-coefficient version of (133.S16).  Consequently the Li--Yang/Bombieri--Iwaniec conclusion supplied in the packet gives no strict cross-ray saving for (133.P1).  The weakest theorem-level bound on the literal scalar remains the accepted

\[
|\mathfrak O_{i,D}^{+}(c)|\lesssim_\varepsilon
Y^{35/48+\varepsilon};
\]

neither \(Y^{27/48+\varepsilon}\) nor \(Y^{24/48+\varepsilon}\) follows.

There are two independent exact failures.  At the source-condition level, the printed condition (133.S9) is not algebraically equivalent to (133.S8), except on the special scale \(M^3\asymp T\).  If (133.S8) is instead checked directly, the first target-normal-form failure is the unsupported replacement of the determinant-restricted, owner-dependent joint coefficient \(B_i(r,r')\) by fixed-norm separable BV weights (or by a positive large-sieve energy).  This is the first invalid inference in a source-to-target proof.

## 2. Exact statement and hypotheses

Let \(T=c/\kappa_i\asymp Y\), \(H=Y^{1/6}\), and \(M=Y^{1/2}\).  For a genuine source sum

\[
S=\sum_{h\asymp H}g(h/H)\sum_{m\asymp M}G(m/M)
e\!\left(\frac{hT}{M}F(m/M)\right),
\]

assume all of the following rather than any property of (133.P1):

1. \(g,G\) have fixed bounded BV norms and are separable;
2. \(F(z)=1/z\), with the negative-\(h\) part handled by a separate sign block;
3. the relevant Case-A hypotheses, the full small-cap first-spacing range, all internal parameter hypotheses, and (133.S8) are verified directly;
4. no joint determinant selector, owner profile, reciprocal alias, M1/M2 carrier, or pair-dependent coefficient is inserted into \(g(h/H)G(m/M)\).

Then (133.S10), at \(H/M=T^{-1/3}\), gives for \(4\le q\le 9/2\)

\[
\frac SH\lesssim_\varepsilon
T^{p(q)+\varepsilon},\qquad
p(q)=\frac{217q^2-616q+500}{600q(q-2)},                 \tag{R133.1}
\]

because the nonconstant term inside the final parenthesis has exponent

\[
\frac{17}{200}-\frac{17}{75(q-2)}<0.                    \tag{R133.2}
\]

In particular, the completely explicit choice \(q=4\) yields

\[
\frac SH\lesssim_\varepsilon Y^{377/1200+\varepsilon},
\qquad
S\lesssim_\varepsilon Y^{577/1200+\varepsilon}
=Y^{(23+2/25)/48+\varepsilon}<Y^{24/48+\varepsilon}.    \tag{R133.3}
\]

Statement (R133.3) is the weakest legal positive consequence: it concerns only the source single wave.  It is not a bound for a ray pair, a determinant band, or the literal scalar.

## 3. Proof and derivation

### 3.1 The single-wave phase and derivative conditions

For \(m=b\) and \(M=D\),

\[
\frac{hT}{M}F(m/M)
=\frac{a(c/\kappa_i)}{D}\frac{D}{b}
=\frac{ca}{\kappa_i b}.
\]

Moreover

\[
F'=-z^{-2},\qquad F''=2z^{-3},\qquad F'''=-6z^{-4},
\]

so all three derivatives are bounded above and away from zero on \([1,2]\), and

\[
F'F'''-3(F'')^2=-6z^{-6}.
\]

Thus (133.S2)--(133.S3) hold.  This verifies precisely one wave and nothing about the coefficient joining it to a second wave.

At the project powers, the Case-A upper condition is also compatible:

\[
MT^{-49/164}=T^{33/164},\qquad H=T^{1/6}<T^{33/164}.
\]

The two scale-qualified lower conditions in (133.S4) do not activate at \(M=T^{1/2}\).  Case B is not a substitute: although the first cap in (133.S5) is exactly \(T^{1/6}\), the printed Case-B reduction (133.S11) would require

\[
H<T^{-1/2}(\log T)^{171/140},
\]

which fails.  Hence any positive use here must be the directly audited Case-A route, including the unsupplied small-cap check.

### 3.2 The source-condition algebra

Write \(\lambda=969/14000\).  From (133.S6),

\[
N_A\asymp H^{-16/25}M^{41/25}T^{-49/100}(\log T)^\lambda.
\]

Substitution into (133.S8) gives, after collecting powers,

\[
H^{(34q-54)/25}T^{(51q-106)/100}
\lesssim
M^{(34q-54)/25}(\log T)^{\lambda(6-q)}.                 \tag{R133.4}
\]

By contrast, raising the printed (133.S9) to the power \(6-q\) gives

\[
H^{(34q-54)/25}M^{34(6-q)/25}
\lesssim
T^{51(6-q)/100}(\log T)^{\lambda(6-q)}.                 \tag{R133.5}
\]

The right side allowed for \(H^{(34q-54)/25}\) in (R133.5), divided by that allowed in (R133.4), is

\[
\frac{T^2}{M^6}=\left(\frac{T}{M^3}\right)^2.           \tag{R133.6}
\]

Thus (133.S9) and (133.S8) are equivalent only when \(M^3\asymp T\), not at \(M=T^{1/2}\).

Indeed, at the candidate powers

\[
N_A\asymp T^{67/300}(\log T)^\lambda.
\]

The left and right powers in (133.S8) are respectively

\[
\frac{67(6-q)}{300}
\quad\hbox{and}\quad
\frac{6-q}{6}=\frac{50(6-q)}{300},
\]

so (133.S8) holds with a power margin.  But at \(q=4\), (133.S9) asks for

\[
T^{143/150}\lesssim T^{51/100}(\log T)^\lambda,
\]

which is false by a power.  Therefore (133.S9) cannot be used as the source gate; the direct check of (133.S8) is essential.

For completeness, these powers also give

\[
R\asymp(M^3/(N_AT))^{1/2}=T^{83/600}(\log T)^{-\lambda/2},
\]

so \(R<H=T^{1/6}\) and \(N_A>H\) by powers; the displayed interval in (133.S13) is not empty at the exponent level.

### 3.3 Evaluation of the legal single-wave estimate

At \(q=4\), the first two exponents in (133.S10) are

\[
\left(\frac HM\right)^{1/25}T^{131/400}
=T^{-1/75+131/400}=T^{377/1200}.
\]

The extra term in the parenthesis is

\[
\left(\frac HM\right)^{-17/25}T^{-51/200}
=T^{-17/600},
\]

so it is harmless.  Multiplication by \(H=T^{1/6}\) proves (R133.3).

### 3.4 Why this derivation stops before the literal scalar

For fixed \(r=(a,b)\), the condition on \(r'\) is the slanted strip

\[
0<\frac ab-\frac{a'}{b'}\lesssim \frac1W,
\]

and its taper and physical carriers remain inside \(B_i(r,r')\).  The packet supplies no representation

\[
B_i(r,r')=\sum_j u_j(r)v_j(r')
\]

with a projective sum of fixed BV norms, and it supplies no arbitrary-coefficient/operator-norm version of (133.S10) or (133.S16).  Conditioning on \(r\) does not help: the allowed \((a',b')\) weight is still coupled, has an outer-ray-dependent boundary, and is not \(g(a'/L)G(b'/D)\).

The source derivative rational is also a different object.  For \(F(z)=1/z\),

\[
\frac{T}{M^2}F'(m_0/M)\asymp-1,
\]

whereas a project ray has

\[
\frac ab\asymp\frac HM=T^{-1/3}.
\]

Thus \((a,b)\) cannot be identified with \((a_{\rm BI},r_{\rm BI})\): the former are original summation variables, while the latter is a reduced approximant to a derivative generated after localizing the \(m\)-sum.  No bijection is supplied or compatible with these sizes.

Likewise, the determinant gives one ordinary-ratio condition.  It does not give the four first-spacing coordinates (133.S15), a bound for their mean-value norm \(G_q\), or the four second-spacing conditions (133.S21)--(133.S24).  Even under the formally invalid identification \(a_{\rm BI}=a\), \(r_{\rm BI}=b\), the first second-spacing coordinate would involve \(\bar a/b\), not \(a/b\).  Algebraically,

\[
\overline{a'}-\bar a\equiv (a-a')\overline{aa'}\pmod b,
\]

so small \(|a-a'|/b\) gives no small circular distance between the normalized inverses.  The coordinates involving \(c_0,\kappa_0,\mu\) have no project counterparts at all.

## 4. First doubtful or unproved step

The first source-side doubtful step is the sentence “substituting \(N=N_A\) gives (133.S9).”  Equations (R133.4)--(R133.6) show the exact missing scale factor; the statement is false at the project powers.

After repairing that issue by checking (133.S8) directly, the first target-side unproved step is:

> Treat the joint, determinant-restricted coefficient \(A_i(r)B_i(r,r')\) as fixed-norm separable BV data to which the standard-sum/double-large-sieve estimate applies, or dominate it by the source positive energy without an operator-norm connector.

This step changes coefficient ownership and absolute-value placement.  It occurs before either spacing estimate can be imported.  The approximant/ray identification and the four-coordinate spacing mismatch are later independent failures.

## 5. Control tests and outcomes

1. **`single_wave_phase_and_derivative_map`.**  Input: (133.P6) with \(F(z)=1/z\).  Expected invariant: exact phase equality and (133.S2)--(133.S3).  Outcome: passed for one unrestricted sign block, as shown in Section 3.1.  Implication: retain only the single-wave map.

2. **`project_ray_vs_derivative_approximant_roles`.**  Input: project \(a/b\asymp T^{-1/3}\) and source derivative target \((T/M^2)F'(m_0/M)\asymp-1\).  Expected failure: original summation ray is not a derivative approximant.  Outcome: failed identification by both construction and scale.  Implication: (133.S17) cannot be relabelled with project rays.

3. **`joint_coefficient_BV_projective_norm_and_absolute_value_direction`.**  Input: literal \(B_i(r,r')\), including determinant strip, taper, owners, aliases, M1/M2 carrier, signs, cells, and lifts.  Expected invariant: an explicit separable BV/projective decomposition with total norm and the inequality direction connecting the signed scalar to source energy.  Outcome: neither is supplied; the determinant strip itself couples \((a',b')\) after an outer ray is fixed.  Taking absolute values yields a raw/weighted count, while (133.S16) is not an arbitrary-coefficient positive operator bound.  Implication: the source theorem has no legal input matching (133.P1).

4. **`first_spacing_vector_and_norm`.**  Input: \(y(k,l)=(k,lk,l\sqrt k,l/\sqrt k)\) and \(G_q\).  Expected invariant: project indices and literal coefficients induce these four coordinates and an audited \(G_q\) bound.  Outcome: (133.P2)--(133.P3) provide only a determinant condition and outer \(\ell^1/\ell^2\) masses; they provide no \((k,l)\) identification or \(G_q\) estimate.  Implication: (133.S16) cannot be evaluated for the literal scalar.

5. **`second_spacing_four_coordinates_and_modular_inverses`.**  Input: (133.S21)--(133.S24) versus \(|a/b-a'/b'|\lesssim W^{-1}=Y^{-7/16}\).  Expected invariant: the project condition must imply both modular-inverse spacings and both \((\mu,c_0,\kappa_0)\) spacings.  Outcome: it implies none of them.  The modular-inverse congruence above already blocks the first coordinate, and the other three source data are absent.  Implication: a one-dimensional ordinary determinant band cannot be substituted for the source second-spacing problem.

6. **`same_denominator_M1_M2_aligned_packets`.**  Input: \(b'=b\), \(\Delta=a-a'=n/b\), \(1\le\Delta\lesssim D/W=Y^{3/48}\), and \(c=\kappa_i b^2\).  For both \(\kappa_1=1\) (M1 quarter carrier) and \(\kappa_2=4\) (M2 \(\chi_4\) carrier), the geometric phase is

   \[
   e\!\left(\frac{c(a-a')}{\kappa_i b}\right)=e(b\Delta)=1.
   \]

   Before physical weights, the capacity over \(b,a,\Delta\) is

   \[
   D\,L\,(D/W)=Y^{(24+8+3)/48}=Y^{35/48}.
   \]

   With only the outer mass \(\sum_r|A_i(r)|\lesssim D\) and formally bounded remaining carriers, the analogous absolute capacity is

   \[
   D(D/W)=Y^{27/48}.
   \]

   Reaching \(Y^{24/48}\) requires eliminating the remaining \(D/W=Y^{3/48}\) determinant multiplicity.  The displayed phase supplies no such cancellation at its aligned centre.  Outcome: the control blocks a phase-only determinant saving.  This remains a local control, not a lower bound: the physical signs may cancel and one fixed \(c\) does not align every denominator.

7. **`S_over_H_to_Y_capacity`.**  Input: (133.S10) with \(q=4\), \(H/M=Y^{-1/3}\).  Outcome: the legal source wave has \(S/H\) exponent \(377/1200=(15+2/25)/48\), and \(S\) exponent \(577/1200=(23+2/25)/48\).  A black-box square would have exponent \(1154/1200=(46+4/25)/48\), and conditioning on an outer ray followed by the supplied \(\ell^1\) bound would cost another \(D=Y^{24/48}\), giving \(1177/1200=(47+2/25)/48\).  These are not proposed bounds for (133.P1); they show that a single-wave black box has no joint capacity without a new bilinear connector.

8. **`capacity_35_27_24_over_48`.**  Input: the aligned packet and (133.P3)--(133.P5).  Outcome: the three powers have the exact capacity decomposition

   \[
   35/48=24/48+8/48+3/48,
   \quad 27/48=24/48+3/48,
   \quad 24/48=24/48.
   \]

   Thus the complete count contains denominator, numerator-ray, and determinant-shift capacities; the ideal outer coefficient mass removes the \(L=Y^{8/48}\) numerator capacity; the determinant target additionally needs the full \(D/W=Y^{3/48}\) saving.  No source-to-project step in the packet supplies that final saving.

9. **`no_positive_energy_or_global_promotion`.**  Input: the literal signed scalar and source quantities \(G_q\), (133.S16).  Expected invariant: an explicit identity or one-sided inequality retaining every owner and coefficient.  Outcome: absent.  A positive large-sieve energy, an unsigned near-collision count, or a theorem for one separable \(S\) cannot be promoted to (133.P1).  The aligned control also cannot be promoted to a lower bound.  Implication: no positive energy and no global proof-state effect is justified.

## 6. Dependencies and exact artifacts used

This report used only:

1. `problems/gauss_circle.md`;
2. `state/control_models.md`;
3. `rounds/codex-managed/gc-w7-16-bombieri-iwaniec-two-spacing-source-map/briefs/blind_double_large_sieve_feasibility.md`;
4. `rounds/codex-managed/gc-w7-16-bombieri-iwaniec-two-spacing-source-map/blind_statement.md`.

No proof graph, strategy file, nonblind Round-95--Round-133 artifact, conductor candidate, sibling report, web source, or numerical experiment was used.

## 7. Recommended state effect

**Reject** the proposed direct Li--Yang/Bombieri--Iwaniec-to-literal-scalar connector and any claim of a strict \(27/48\) cross-ray bound.  **Retain** the exact one-wave phase map and the conditional single-wave estimate (R133.3) only as diagnostic evidence.  **Revise** the source interface so that (133.S8), not the inequivalent printed (133.S9), is checked directly (or restore the missing \((T/M^3)^2\) scale information).  Make **no change** to accepted proof state until there is an explicit coefficient-preserving bilinear connector, a four-coordinate spacing map with an audited \(G_q\) norm, and a mechanism that survives the aligned \(D/W=Y^{3/48}\) packet.
