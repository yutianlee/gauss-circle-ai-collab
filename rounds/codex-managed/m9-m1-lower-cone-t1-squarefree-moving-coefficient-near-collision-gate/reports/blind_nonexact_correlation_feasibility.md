# Round 150 blind report: nonexact-collar feasibility

## 1. Result: a rigorous source/profile no-go

The requested bound is **not a consequence of the statement-only hypotheses**.  The first obstruction occurs before any shifted-divisor estimate: the statement gives neither a formula nor uniform derivative/variation bounds for \(\mathscr W_{d,U}\), and it gives no mathematical characterization of which finite indicators \(\kappa_{d,U}\) are produced by an actual clipped prefix.  Bounded smoothness alone permits a single one-variable profile to interpolate the mod-four sign and the reciprocal phase at every sampled reduced cell.

More precisely, under all properties of \(\kappa\) and \(\mathscr W\) that are explicitly stated, there is a sequence of legal parameter values with

\[
 D=E=M=1,\qquad L_1=L_2=1,
\]

for which the exact coefficient formula and both accepted coefficient bounds hold, every selected off-diagonal pair has \(\rho\ne0\), the selected reduced phase denominators are \(\asymp N\), and the complete signed collar mass is

\[
 \gg N=R^4.
\]

This contradicts \(O_\varepsilon(R^2X^\varepsilon)\) for every fixed \(\varepsilon<1/2\).  The construction uses the literal one-row coefficient formula and a single real \(C_c^\infty\) function of \(L/q\); it does not replace the two-row coefficient by an arbitrary matrix.

This is a source-hypothesis no-go, not a claim that the omitted, fully specified transform necessarily has this pathology.  If the word “actual” is intended to rule the construction out, the missing transform formula and its quantitative consequences are indispensable hypotheses.  In addition, the phrase “small reduced-denominator stratum” has no numerical cutoff in the statement, so the target sum itself is not uniquely defined.  The counterexample lies at reduced denominator at least a fixed positive multiple of \(N\), and hence survives every genuinely small cutoff below that scale.

## 2. Exact statement and hypotheses

Write

\[
 H=hr_1r_2,\qquad
 \mathcal K_i=a_i u_i(c_i s_i v_i)^2,
 \qquad a_i=(t_i,d_{\mathrm o}),\quad c_i=t_i/a_i,
\]

where \(L_i=t_i s_i^2\).  The following two assertions are proved below.

**Exact expansion lemma.**  For any two retained cells, the signed summand in the collar is

\[
 \begin{aligned}
 &\mu^2(d)\,\chi_4(L_1L_2r_1r_2)
 \frac{B_{d,U}(L_1)\overline{B_{d,U}(L_2)}}{L_1L_2}\\
 &\qquad\times
 \mathscr W_{d,U}(L_1/q_1)
 \overline{\mathscr W_{d,U}(L_2/q_2)}
 e\!\left(\frac{d\rho}{H}\right).
 \end{aligned}
 \tag{2.1}
\]

If \((s_i,d_{\mathrm o})=1\) for both rows, its exact coefficient product is

\[
 \begin{aligned}
 B_{d,U}(L_1)\overline{B_{d,U}(L_2)}
 &=\prod_{i=1}^2\frac{\mu(a_i)\mu(c_i)\mu(s_i)}{c_i}\\
 &\quad\times
 \sum_{\substack{u_i\mid d_{\mathrm o}/a_i\\ i=1,2}}
 \frac{\mu(u_1)\mu(u_2)}{u_1u_2}\\
 &\quad\times
 \sum_{\substack{v_i\ge1\ {\rm odd\ squarefree}\\
 (v_i,d_{\mathrm o}c_is_i)=1\ (i=1,2)}}
 \frac{\mu(v_1)\mu(v_2)}{v_1^2v_2^2}
 \kappa_{d,U}(\mathcal K_1)\kappa_{d,U}(\mathcal K_2).
 \end{aligned}
 \tag{2.2}
\]

If either \((s_i,d_{\mathrm o})>1\), the product is zero.  Formula (2.2), rather than a rank-one or arbitrary-matrix surrogate, is the true two-row incidence.  The two rows remain coupled through \(d_{\mathrm o}\), both gcds \(a_i\), both divisor ranges, both coprimality masks, both literal prefix indicators, and the two samples of the same \(d,U\)-profile.

**Statement-only countermodel lemma.**  Interpret the dyadic condition by the standard admissible window \(Q\le q<2Q\).  Assume only what is written: \(\kappa\) is a finite Boolean indicator, \(\mathscr W\) is bounded and smooth, and no uniform derivative, variation, Fourier-complexity, or \(\kappa\)-to-\(\mathscr W\) relation is imposed.  There are infinitely many \(X\) and such data satisfying the exact formula and the accepted coefficient bounds for which, for some absolute \(c>0\),

\[
 T_{\rm full}\gg N,\qquad
 A_{\rm full}\gg N,\qquad
 S_{\rm full}\gg N.
 \tag{2.3}
\]

Here \(T_{\rm full}\) is the raw ordered tuple count in a full-scale-denominator subcollar, \(A_{\rm full}\) is its coefficient-weighted absolute mass, and \(S_{\rm full}\) is its actual signed mass.  They are three separate quantities; in the construction they happen to have the same order because every selected coefficient has unit modulus and every symmetrized phase pair has positive real part.

## 3. Proof and derivation

### 3.1 Literal collar expansion

Expanding \(G_U(d)\overline{G_U(d)}\), the phase of a two-cell term is

\[
 e\!\left(Nd\left(\frac{L_1}{hr_1}-\frac{L_2}{hr_2}\right)\right)
 =e\!\left(\frac{Nd\delta}{H}\right)
 =e\!\left(\frac{d\rho}{H}\right),
 \tag{3.1}
\]

because \(N\delta=kH+\rho\) and \(e(dk)=1\).  All \(L_i,q_i,h\) are odd, and therefore

\[
 \chi_4(L_1q_1)\chi_4(L_2q_2)
 =\chi_4(L_1L_2h^2r_1r_2)
 =\chi_4(L_1L_2r_1r_2).
 \tag{3.2}
\]

Substitution of the given closed formula for each \(B_{d,U}(L_i)\) gives (2.2) verbatim.  In particular, an odd prime dividing \(d_{\mathrm o}\) changes \(a_i\), the allowed \(u_i\), and both \(v_i\)-coprimality masks.  Passing from odd \(d\) to even squarefree \(2d\) leaves \(d_{\mathrm o}\) unchanged but need not leave either \(\kappa_{d,U}\) or \(\mathscr W_{d,U}\) unchanged.  No parity relation between those profiles is stated.

For reference, if \(\mathcal C\) denotes the precisely retained collar tuples, the three relevant objects are

\[
 T(\mathcal C)=\sum_{\mathcal C}1,
 \tag{3.3}
\]

\[
 A(\mathcal C)=
 \sum_{\mathcal C}
 \frac{|B_{d,U}(L_1)B_{d,U}(L_2)|}{L_1L_2}
 |\mathscr W_{d,U}(L_1/q_1)\mathscr W_{d,U}(L_2/q_2)|,
 \tag{3.4}
\]

and the signed sum \(S(\mathcal C)\) obtained from (2.1).  Only \(|S|\le A\) is automatic.  Neither a raw tuple estimate nor an adverse upper bound for \(A\) is a signed lower bound.

### 3.2 Shifted-factor identity, zero factors, and imprimitive phases

Direct multiplication gives the exact identity requested in the brief:

\[
 \begin{aligned}
 &(NL_1-khr_1)(NL_2+khr_2)\\
 &=N^2L_1L_2+Nkh(L_1r_2-L_2r_1)-k^2h^2r_1r_2\\
 &=N^2L_1L_2+kh\rho.
 \end{aligned}
 \tag{3.5}
\]

It is valid with either sign of \(k\), including \(k=0\).  It does not itself supply a divisor estimate after the coefficient, prefix, profile, and all shifts are summed.  Also, its use requires separate treatment of \(NL_1-khr_1=0\) and \(NL_2+khr_2=0\).

The actual reduced phase denominator is

\[
 \frac{H}{(\rho,H)}=\frac{H}{(N\delta,H)}.
 \tag{3.6}
\]

Thus \(H\) cannot simply be called the reduced denominator.  Common factors and imprimitive phases must be priced through (3.6).

### 3.3 A literal \(D=1,L=1\) countermodel to the stated hypotheses

Let \(Y=2^m\to\infty\) and take

\[
 X=N=Y^2,\qquad R=Y^{1/2},\qquad D=E=M=1,
 \qquad Q=2Y.
 \tag{3.7}
\]

All parameter restrictions hold: \(DE=M\), \(M\le R^2=Y\), and \(D\le\sqrt M\).  The \(D=1\) slice has the single row \(d=1\), as required by the stated control.

Choose the finite indicator

\[
 \kappa_{1,U}(n)=\mathbf 1_{n=1}.
 \tag{3.8}
\]

This satisfies every formal property of \(\kappa\) supplied in the statement.  If the hidden meaning of “inherited” forbids (3.8), that is an omitted source condition and is precisely part of the no-go.  Since \(d_{\mathrm o}=1\), for \(L=ts^2\) the given formula becomes

\[
 B_{1,U}(ts^2)=\frac{\mu(t)\mu(s)}{t}
 \sum_{\substack{v\ge1\ {\rm odd\ squarefree}\\(v,ts)=1}}
 \frac{\mu(v)}{v^2}\,\mathbf 1_{(tsv)^2=1}.
 \tag{3.9}
\]

Consequently

\[
 B_{1,U}(1)=1,\qquad B_{1,U}(L)=0\quad(L>1),
 \tag{3.10}
\]

and the two accepted norms have total value exactly \(2\).

There are exactly \(Y\) odd integers in

\[
 \mathcal Q_Y=\{q:2Y\le q<4Y,\ q\ {\rm odd}\}.
\]

Partition \(\mathbb R/\mathbb Z\) into eight arcs of length \(1/8\).  One arc contains the fractional parts \(\{N/q\}\) for a subset \(\mathcal A_Y\subset\mathcal Q_Y\) with

\[
 K:=|\mathcal A_Y|\ge Y/8.
 \tag{3.11}
\]

For any \(p,q\in\mathcal A_Y\),

\[
 \Re e(N/p-N/q)\ge \cos(\pi/4)>0.
 \tag{3.12}
\]

The finitely many points \(1/q\), \(q\in\mathcal Q_Y\), are distinct.  Around each \(1/q\) with \(q\in\mathcal A_Y\), choose a disjoint smooth bump which equals one at \(1/q\) and whose support contains none of the other sample points.  Their signed sum gives a single real function \(\mathscr W_{1,U}\in C_c^\infty((0,\infty))\), with \(\|\mathscr W_{1,U}\|_\infty\le1\), such that

\[
 \mathscr W_{1,U}(1/q)=
 \begin{cases}
 \chi_4(q),&q\in\mathcal A_Y,\\
 0,&q\in\mathcal Q_Y\setminus\mathcal A_Y.
 \end{cases}
 \tag{3.13}
\]

No arbitrary two-index matrix has been introduced: (3.13) is realized by one bounded smooth radial variable.  Its variation and derivatives grow with \(Y\), which is allowed because the statement supplies no uniform control on them.

Equations (3.10) and (3.13) reduce the exact row to

\[
 G_U(1)=\sum_{q\in\mathcal A_Y}e(N/q).
 \tag{3.14}
\]

Thus the mod-four signs have not been dropped; the permitted sampled profile has correlated with and exactly cancelled them.

### 3.4 Nonexactness, common factors, full reduced denominators, and \(k\)

Take distinct \(p,q\in\mathcal A_Y\), put \(h=(p,q)\), \(r_1=p/h\), \(r_2=q/h\), and \(\delta=r_2-r_1\).  Since \(N\) is a power of two and \(H=hr_1r_2\) is odd, \((N,H)=1\).  If \(\rho=0\), then \(H\mid N\delta\), hence \(H\mid\delta\).  But

\[
 0<|\delta|<\frac{2Y}{h},\qquad
 H=\frac{pq}{h}\ge\frac{4Y^2}{h},
 \tag{3.15}
\]

which is impossible.  Therefore every distinct selected pair is nonexact.  For \(D=1\), the centered choice always has \(|\rho|\le H/2<H/D\), so the nonzero collar covers every one of these pairs.

Moreover,

\[
 (\delta,r_1r_2)=1,qquad (\rho,H)=(\delta,H)=(\delta,h)\le h.
 \tag{3.16}
\]

Fix a sufficiently large absolute constant \(H_0\).  The number of ordered pairs in \(\mathcal A_Y^2\) having \((p,q)>H_0\) is at most

\[
 \sum_{g>H_0}^{4Y}\left(\frac{2Y}{g}+1\right)^2
 \ll \frac{Y^2}{H_0}+Y\log Y.
 \tag{3.17}
\]

Using (3.11), first choose \(H_0\) large and then \(Y\) large.  It follows that \(\gg Y^2\) ordered distinct pairs have \(h\le H_0\).  For each such pair, (3.6) and (3.16) give

\[
 \frac{H}{(\rho,H)}\ge \frac{pq}{h^2}
 \ge \frac{4Y^2}{H_0^2}=\frac{4N}{H_0^2}.
 \tag{3.18}
\]

These are full-scale, not small, reduced denominators.  Hence any declared small-denominator cutoff below \(4N/H_0^2\) leaves \(\gg Y^2\) selected pairs.  If the intended cutoff is different, its absent definition prevents a statement-only decision.

In this example the two potentially exceptional factors in (3.5) are \(N-kp\) and \(N+kq\).  Neither can vanish because every selected \(p,q\) is odd while \(N\) is a power of two.  Pairs for which the centered integer happens to be \(k=0\) remain valid and are included; the proof did not divide by \(k\) or discard that case.  All centered values of \(k\) and \(\rho\) generated by the selected pairs are summed at once in (3.14).

### 3.5 Raw count, absolute mass, signed mass, and the power ledger

Restrict to the symmetric ordered set of distinct selected pairs with \(h\le H_0\).  By (3.17), its raw count is

\[
 T_{\rm full}\gg Y^2=N.
 \tag{3.19}
\]

Every selected term has \(L_1=L_2=1\), \(|B_{1,U}(1)|=1\), and \(|\mathscr W_{1,U}(1/q)|=1\).  Therefore its coefficient-weighted absolute mass is separately

\[
 A_{\rm full}=T_{\rm full}\gg Y^2.
 \tag{3.20}
\]

Finally, pair the two orientations of every unordered pair.  By (3.12), their actual signed contribution is

\[
 e(N/p-N/q)+e(N/q-N/p)
 =2\cos(2\pi(N/p-N/q))
 \ge 2\cos(\pi/4).
 \tag{3.21}
\]

Thus, without converting an upper capacity into a lower bound,

\[
 S_{\rm full}\ge \cos(\pi/4)T_{\rm full}\gg Y^2=N=R^4.
 \tag{3.22}
\]

The requested target at these parameters is

\[
 R^2D X^\varepsilon=Y^{1+2\varepsilon}.
 \tag{3.23}
\]

For every fixed \(\varepsilon<1/2\), (3.22) exceeds (3.23) by an unbounded factor.  This uses the extreme but explicitly allowed scale \(M=D=E=1\), \(Q=2R^2\).  Since the proposed theorem is uniform over all scales, one failed scale is a complete all-scale obstruction under the stated hypotheses.

## 4. First doubtful or unproved step

There is no doubtful step in the logical countermodel once “finite indicator” and “bounded smooth profile” are read as the only supplied axioms.  The first step that cannot be checked for the intended underlying transform is whether (3.8) and (3.13) can arise from the same *actual* clipped prefix.  The permitted statement gives no definition from which that question can be answered.

Equivalently, the first unavailable proof step for the desired positive theorem is a uniform estimate for the \(D=1,L=1\) sum

\[
 \sum_{q\asymp Q\atop q\ {\rm odd}}
 \chi_4(q)\mathscr W_{1,U}(1/q)e(N/q).
 \tag{4.1}
\]

Boundedness and pointwise smoothness give no cancellation in (4.1), because finite smooth interpolation can encode both \(\chi_4(q)\) and the phase.  One needs an exact source formula plus a uniform variation, derivative, Fourier-complexity, or comparable non-correlation theorem.  The same omission prevents the requested exact analysis of the joint \(d\)-dependence of the two prefix indicators and sampled profiles.  No divisor-factorization argument can repair this earlier loss.

The unnamed support constants in \(q\asymp LQ\) and the unnamed small-reduced-denominator cutoff are a second definitional obstruction.  The construction used the standard window \([Q,2Q)\) and produces denominator \(\gg N\); an exact theorem must state both cutoffs.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `literal_nonzero_collar_expansion` | Passed: (2.1), (3.1), and (3.2) are the literal expansion. |
| `two_row_divisor_incidence_linearization` | Passed algebraically: (2.2) is the exact joint incidence.  It is not separable without a new lemma. |
| `prefix_profile_d_dependence` | Source obstruction: no formula or relation is supplied.  The finite interpolation (3.13) shows why bounded smoothness is insufficient. |
| `k_zero_and_exceptional_factor` | Passed in the falsifier: (3.5) is exact; \(k=0\) is retained; neither exceptional factor can vanish. |
| `full_shift_and_weight_summation` | Passed in the falsifier: all centered \(k,\rho\) generated by the selected cells are included, with unit exact coefficient weights. |
| `tuple_absolute_signed_separation` | Passed: (3.19), (3.20), and (3.22) separately calculate the three quantities. |
| `mod_four_character_retention` | Passed: (3.2) retains the character; (3.13) exhibits an allowed correlation that cancels it rather than silently deleting it. |
| `all_M_D_E_Q_L_h_k_rho_power_ledger` | Fails the proposed target at the legal endpoint (3.7); (3.15)--(3.18) price \(h,\rho\), imprimitive reduction, and full denominator scale. |
| `D1_L1_full_frequency_test` | Falsifies the stated-hypothesis theorem: for \(D=1\) the centered collar is the full nonexact frequency range and has mass \(\gg R^4\). |
| `prime_parity_prefix_imprimitive_controls` | Odd primes in \(d_{\mathrm o}\) and even \(d\) remain explicitly coupled as described after (3.2); no uniform relation is supplied.  The falsifier has \(d=1\), counts common factors by (3.17), and reduces denominators exactly by (3.16). |
| `exact_and_small_denominator_exclusion` | Exact pairs are absent.  A \(\gg N\)-mass subset has reduced denominator \(\ge4N/H_0^2\).  The exact “small” cutoff is missing. |
| `generic_tge2_cross_and_downstream_scope` | No scope leakage: the obstruction is entirely the \(t=1\), \(L_1=L_2=1\), single-row slice.  It makes no claim about the generic complement or another cross owner. |

The aspect ledger is therefore decisive at the extreme endpoint \(D=E=M=1\).  Balanced \(D>1\), even squarefree rows, and odd primes dividing \(d_{\mathrm o}\) cannot rescue a theorem quantified over every aspect.  Independently, their two-row dependence remains unpriced because the prefix/profile source law is absent.

## 6. Dependencies and exact artifacts used

Only the following artifacts were read:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/blind_statement.md`;
3. `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/briefs/blind_nonexact_correlation_feasibility.md`.

No proof graph, proof draft, strategy file, previous-round artifact, sibling report, web source, or numerical computation was used.  The only counting input is the elementary divisor union bound (3.17).

## 7. Recommended state effect

**Revise; do not promote the collar bound from the statement-only data.**  Record a source/profile obstruction, not a refutation of a fully specified hidden transform.  Before another positive collar attempt, the frozen statement must include:

1. the exact clipped-prefix definition and allowed \(U\)-range;
2. the exact formula linking \(\kappa_{d,U}\) and \(\mathscr W_{d,U}\);
3. uniform derivative, total-variation, Fourier-complexity, or an equivalent sampled non-correlation bound for \(\mathscr W_{d,U}\);
4. the exact \(q\)-support and the numerical small-reduced-denominator cutoff;
5. a standalone \(D=1,L=1\) estimate strong enough to rule out (3.13);
6. only then, a two-row lemma estimating (2.2) with even \(d\), odd prime incidence, common factors, imprimitive denominators, and all shifts retained.

Until those data are supplied, the literal nonzero collar is underdetermined and the desired \(R^2D X^\varepsilon\) conclusion is false for the explicit mathematical class stated here.

