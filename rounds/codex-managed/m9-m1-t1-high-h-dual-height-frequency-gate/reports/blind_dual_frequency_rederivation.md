# Round 189 statement-only blind rederivation

- Campaign: `m9-m1-t1-high-h-dual-height-frequency-gate`
- Task: `blind_dual_frequency_rederivation`
- Role: statement-only blind rederiver
- Status: candidate evidence only

## 1. Result: proved slow-sector lemma and no-go for the remaining signed step

Let

\[
J_1=\left\lfloor\frac{U}{Y}\right\rfloor
 =\left\lfloor\frac{mq}{Y}\right\rfloor .
\]

The sector (1\le j_q(a,v)\le J_1) is absolutely target-safe.  For
fixed ((a,m,q,\kappa,u)), it contains (O(um/Y)) possible (v)'s,
with the exact answer zero when (J_1=0).  The (m) in this count is
cancelled by the literal Fourier-lift factor

\[
c_U(ma)=\frac1m c_q(a),
\]

before the divisor sum.  The complete pre-absorption ledger is

\[
 |\Sigma_{\le J_1}|
 \ll_\varepsilon
 L^2(\log(2L))^4X^{\varepsilon_0}.
\tag{R189.B.1}
\]

Thus, under the packet's convention that fixed polylogarithms may be
put into (X^\varepsilon) (take \(\varepsilon_0<\varepsilon\)), this
is (O_{B,\varepsilon}(L^2X^\varepsilon)).  No positive power of (Y)
has been absorbed.

There is a harmless but useful strengthening.  If (P\ge1) is any
fixed admissible polylogarithm and

\[
M_q=\left\lfloor\frac{q-1}{2}\right\rfloor,
\qquad
J_P=\min\left(M_q,\left\lfloor\frac{PU}{Y}\right\rfloor\right),
\tag{R189.B.2}
\]

then the larger sector (1\le j_q(a,v)\le J_P), including the case in
which it is saturated and contains every unit residue, obeys

\[
 |\Sigma_{\le J_P}|
 \ll_\varepsilon
 P L^2(\log(2L))^4X^{\varepsilon_0}
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{R189.B.3}
\]

Consequently \(U/Y\) is the maximal cutoff at the level of powers for
this coefficient-insensitive capacity argument, but not at the level
of fixed polylogarithms.

The exact signed complement is retained.  Its desired dyadic height
gain is **not derivable from the statement packet**: the packet gives
only a pointwise bound for the literal amplitudes, and allows an
adversarial amplitude which cancels every displayed oscillatory phase.
The first missing input is the literal, zero-extended height
discrepancy relation stated in Section 4.

There is also an independent normalization obstruction: (B189.8), as
stated without an odd-conductor hypothesis, is false.  It is correct
for odd (q).  In particular the requested prime survivor and bad
slope control hold for every odd prime (p); (p=2) is singular in
(B189.4).

## 2. Exact statement and hypotheses

Assume exactly (B189.1)--(B189.7), and interpret all comparability
constants in (u,v\asymp L/\kappa) as fixed.  The coefficient formula
is finite on unit (a\pmod q) for (q\ge3); at (q=2,a=1) its
denominator vanishes, so the self-contained statement itself requires
either (q\ge3) or a separate (q=2) convention.

For (q\ge3), put

\[
\mathcal R_q(J)=
 \{r\in(\mathbb Z/q\mathbb Z)^\times:1\le |r|_q\le J\}.
\]

Then

\[
 \#\mathcal R_q(J)\le \min(\varphi(q),2J),
\tag{R189.B.4}
\]

and, when (0\le J<q/2), the exact two-sided formula is

\[
 \#\mathcal R_q(J)
 =2\sum_{1\le r\le J}\mathbf 1_{(r,q)=1}.
\tag{R189.B.5}
\]

For (J\ge M_q), the set is all of
((\mathbb Z/q\mathbb Z)^\times).  For fixed unit (a\pmod q), the
number of literal (v\)-values in an interval of length (O(u)) with
(j_q(a,v)\le J) is

\[
 O\!\left(\frac{u}{q}\#\mathcal R_q(J)\right).
\tag{R189.B.6}
\]

In particular (R189.B.6) is (O(um/Y)) for (J=J_1), and
(O(Pum/Y)) for (J=J_P).  These conclusions include (J=0), when
the sector is empty, and the saturated (J_P=M_q) case.

Write the complex sum inside (B189.1) as \(\Sigma\).  With

\[
 I_{\rm slow}=\mathbf1_{\{1\le j_q(a,v)\le J_1\}},
 \qquad
 I_{\rm fast}=\mathbf1_{\{j_q(a,v)>U/Y\}},
\tag{R189.B.7}
\]

integer-valuedness of (j_q) gives (I_{\rm slow}+I_{\rm fast}=1).
The exact decomposition, preserving both orientations and one outer
real part, is therefore

\[
 \mathcal C=\Re\bigl(\Sigma_{\rm slow}+\Sigma_{\rm fast}\bigr),
 \qquad
 \Sigma_\star=\sum I_\star\,
 \frac{c_q(a)}m e(\epsilon_\omega a\bar v h/q)(-1)^tB.
\tag{R189.B.8}
\]

No conjugate pairing, sign deletion, or positive recombination is
used.  If the optional enlarged slow band is used, the equally exact
refinement has slow indicator (j_q\le J_P) and complement
(j_q>J_P); equivalently, one first removes the absolutely bounded
band (U/Y<j_q\le J_P) from (R189.B.8).

For the independent kernel control, the corrected exact-conductor
statement is: if (q) is odd and ((b,q)=1), then

\[
 K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b),
 \qquad
 K_q^\circ(b)=\frac1q
 \sum_{\substack{d\mid q\\d>1}}\mu(q/d)dE_d(b).
\tag{R189.B.9}
\]

Without oddness, (R189.B.9) is false in the stated coefficient
normalization.

## 3. Proof and derivation

### 3.1 Projective bijection and interval multiplicity

Since (q\mid u) and ((u,v)=1), every live (v) is a unit modulo
(q).  For fixed unit (a),

\[
 v\longmapsto a v^{-1}\pmod q
\]

is a bijection of the unit group, with inverse (r\mapsto ar^{-1}).
Each positive distance (r\) has at most the two representatives
(r,-r), proving (R189.B.4) and (R189.B.5).

One residue class modulo (q) occurs (O(u/q+1)) times in the
literal (v\)-interval, whose length is (O(u)).  Because (q\mid u),
(u/q\ge1), so this is (O(u/q)), with no stray `+1`.  This proves
(R189.B.6).  For (J_1=\lfloor mq/Y\rfloor),

\[
 \#\{v:j_q(a,v)\le J_1\}
 \ll \frac uq J_1\le \frac{um}{Y}.
\tag{R189.B.10}
\]

The same proof with (J_P\le PU/Y=Pmq/Y) gives
(O(Pum/Y)), even when the cap (M_q) is active.  Coprimality and all
literal deletions only reduce these counts.

### 3.2 Exact coefficient normalization and cancellation of (m)

With (U=mq) and (k=ma), direct substitution in the same endpoint
coefficient gives

\[
 c_U(k)=\frac{2}{U\{1+e(-k/U)\}}
 =\frac{2}{mq\{1+e(-a/q)\}}
 =\frac1m c_q(a).
\tag{R189.B.11}
\]

Thus no unrecorded power of (m,q), or (U) is present.  At fixed
((\kappa,u,m,q)), absolute summation over the baseline slow sector
costs

\[
 \underbrace{Y}_{h}\,
 \underbrace{\frac{um}{Y}}_{v}\,
 \underbrace{\kappa}_{t}\,
 \underbrace{\frac1m\sum_{(a,q)=1}|c_q(a)|}_{a\text{ and lift}}
 X^{\varepsilon_0}
 \ll \kappa u\log(2q)X^{\varepsilon_0}.
\tag{R189.B.12}
\]

This removes the full (Y) before any global positive summation: the
height factor and projective sparsity cancel, then the resulting (m)
and the exact lift weight cancel.  For (J_P), the right side of
(R189.B.12) is merely multiplied by (P).

### 3.3 The full \(\kappa,u,m,q\) ledger

Dropping only conditions which reduce capacity, (R189.B.12) gives

\[
 |\Sigma_{\le J_P}|
 \ll P X^{\varepsilon_0}
 \sum_{\kappa\ll L}\kappa
 \sum_{u\asymp L/\kappa}u
 \sum_{mq\mid u}\log(2q).
\tag{R189.B.13}
\]

Put (N=L/\kappa).  For (mq\ll N), the sum of the multiples of
(mq) in (u\asymp N) is (O(N^2/(mq))).  Indeed, there are
(O(N/(mq)+1)=O(N/(mq))) such multiples, the final equality following
from (mq\ll N), and each is (O(N)).  Hence

\[
\begin{aligned}
 \sum_{u\asymp N}u\sum_{mq\mid u}\log(2q)
 &\ll N^2\sum_{mq\ll N}\frac{\log(2q)}{mq}\\
 &\ll N^2
 \sum_{m\ll N}\frac1m
 \sum_{q\ll N/m}\frac{\log(2q)}q\\
 &\ll N^2(\log(2N))^3.
\end{aligned}
\tag{R189.B.14}
\]

Finally,

\[
 \sum_{\kappa\ll L}\kappa
 \left(\frac L\kappa\right)^2
 (\log(2L))^3
 \ll L^2(\log(2L))^4,
\tag{R189.B.15}
\]

which proves (R189.B.1) and (R189.B.3).  Conditions (q>Q),
(U>4Q), (m|a|_q>Q), and (Qm<Y) were retained in the actual sum
and only discarded in the upper bound; no positive power of (Y) was
discarded or hidden.

More generally, an arbitrary coefficient-insensitive cutoff (J)
has the power cost (YJ/U).  Thus (J\le PU/Y) is precisely the
range controlled by this proof with at most the admissible factor
(P).

### 3.4 Conditional dyadic calculation for the exact complement

Choose the signed representative
(r_q(a,v)\in(-q/2,q/2]) of (a\bar v\), so
(|r_q(a,v)|=j_q(a,v)).  For fixed

\[
 \theta=(\kappa,u,U,m,q,a,v,\omega)
\]

let the actual coefficient, including every literal deletion and
zero extension, be

\[
 A_\theta(h)=\mathbf1_{\{Y<h\le2Y,(U,h)=1\}}
 \sum_t(-1)^t
 B_{\kappa,u,U,m,q,a,h,v,t,\omega}.
\tag{R189.B.16}
\]

Only (|A_\theta(h)|\ll\kappa X^{\varepsilon_0}) follows from the
packet.

For a complementary dyadic block (R<j_q(a,v)\le2R), projective
counting gives (O(uR/q)) possible (v)'s for each (a).  If one had
the literal discrepancy estimate

\[
 \sup_{Y\le H\le2Y}
 \left|\sum_{Y<h\le H}A_\theta(h)
 e\!\left(\frac{\epsilon_\omega r_q(a,v)h}{q}\right)\right|
 \ll_\varepsilon \kappa X^\varepsilon\frac qR,
\tag{R189.B.17}
\]

uniformly on this block, its (v\)-sum would cost

\[
 \frac{uR}{q}\cdot
 \kappa X^\varepsilon\frac qR=\kappa uX^\varepsilon.
\tag{R189.B.18}
\]

After the coefficient mass this is
(O(\kappa uX^\varepsilon\log(2q)/m)) per dyadic block.  The remaining
divisor average is no worse than

\[
 N^2\sum_{mq\ll N}\frac{\log(2q)}{m^2q}
 \ll N^2(\log(2N))^2,
\]

and the harmonic \(\kappa\)-sum and the number of dyadic (R)-blocks
are fixed logarithmic losses.  Thus (R189.B.17) would give the desired
power bound for the exact complement.  Relative to the trivial height
bound (\kappa YX^\varepsilon), (R189.B.17) saves (YR/q), reaching
the full factor (Y) at (R\asymp q).

### 3.5 Exact-conductor identity and its parity obstruction

For odd (q), the finite geometric sum gives

\[
 c_q(a)=\frac1q\sum_{x=0}^{q-1}(-1)^x e(-ax/q).
\tag{R189.B.19}
\]

Fourier inversion therefore yields

\[
 E_q(b)=\sum_{a\bmod q}c_q(a)e(ab/q).
\]

Partitioning the frequencies according to
(d=q/(a,q)), and using
(c_q((q/d)a')=(d/q)c_d(a')), gives

\[
 qE_q(b)=\sum_{d\mid q}dK_d(b).
\]

Divisor Möbius inversion proves (R189.B.9).  The (d=1) term is
(\mu(q)/q), which proves the displayed centered identity.

Oddness is essential.  For every (q=2^s\ge4) and (b=q-1), pairing
the unit (a) with (q-a) gives

\[
 K_q(q-1)=\frac12.
\]

Indeed, with (z=e(-a/q)), a paired contribution is

\[
 \frac2q\left(\frac z{1+z}
 +\frac{z^{-1}}{1+z^{-1}}\right)=\frac2q,
\]

and there are (q/4) pairs.  On the proposed right side of (B189.8),
only (d=q) and (d=q/2) survive; both corresponding (E_d(q-1))
equal (-1), so the value is

\[
 \frac1q\left(-q+\frac q2\right)=-\frac12.
\]

This supplies arbitrarily large even-conductor counterexamples, so
the failure cannot be removed by the condition (q>Q).

For an odd prime (p), (R189.B.9) gives

\[
 K_p(b)=E_p(b)-\frac1p,
 \qquad K_p^\circ(b)=E_p(b).
\tag{R189.B.20}
\]

At the fixed projective slope (-2\pmod p), put
(H=(p-1)/2).  For (1\le h\le H),
([-2h]_p=p-2h) is odd, and every (h) is a unit.  Hence

\[
 \sum_{h=1}^{(p-1)/2}K_p^\circ(-2h)
 =\sum_{h=1}^{(p-1)/2}E_p(-2h)
 =-\frac{p-1}{2}.
\tag{R189.B.21}
\]

The absolute prefix discrepancy is exactly ((p-1)/2).

## 4. First doubtful or unproved step

The first unproved step is precisely (R189.B.17) for the **actual**
zero-extended coefficient (R189.B.16).  A sufficient, but stronger,
input would be the literal bounded-variation estimate

\[
 \mathop{\rm Var}_{Y<h\le2Y} A_\theta
 :=|A_\theta(h_0)|+
 \sum_{Y<h<2Y}|A_\theta(h+1)-A_\theta(h)|
 +|A_\theta(h_1)|
 \ll_\varepsilon\kappa X^\varepsilon,
\tag{R189.B.22}
\]

with the appropriate first and last integer heights.  Abel summation
and the geometric bound

\[
 \left|\sum_{H_0<h\le H_1}e(rh/q)\right|
 \ll \min(H_1-H_0,q/|r|_q)
\]

would then prove (R189.B.17).

Nothing in the packet proves (R189.B.22).  The pointwise estimate only
gives the useless worst-case variation
(O(\kappa YX^\varepsilon)), and the squarefree, coprimality,
residual-selector, profile, endpoint, and zero-extension operations
may all jump.  Nor does the packet imply (R189.B.17) directly.  On any
live height set one may choose the admissible bounded amplitude

\[
 B=(-1)^t e(-\epsilon_\omega a\bar v h/q)
 \frac{\overline{c_q(a)}}{|c_q(a)|},
\tag{R189.B.23}
\]

which makes every displayed summand equal to \(|c_q(a)|/m\).  Thus a
height prefix can have its full cardinality rather than (O(q/R)).
The quantitative deficit in dyadic block (R) is the factor

\[
 \frac{\kappa YX^\varepsilon}
 {\kappa(q/R)X^\varepsilon}=\frac{YR}{q},
\tag{R189.B.24}
\]

which is as large as a constant multiple of (Y).  No argument based
only on the packet can bridge this deficit without also proving the
false unsigned/adversarial analogue.

The prime prefix (R189.B.21) is an independent warning against an
invented uniform polylogarithmic prefix theorem.  It is not a lower
bound for (B189.1), because the literal amplitudes, deletions,
orientations, and other sums have not been identified with that
kernel.

## 5. Control tests and outcomes

1. **`exact_round188_Qm_lt_Y_complement`: pass.**  All conditions in
   (B189.2), including (Qm<Y), remain in (R189.B.8); only
   capacity-reducing restrictions are dropped after the exact split.
2. **`single_outer_real_part_and_both_orientations`: pass.**
   Equation (R189.B.8) keeps \(\omega=\pm\) inside one complex sum and
   one outer real part.
3. **`dual_frequency_j_abs_a_v_inverse_mod_q`: pass.**  The split uses
   exactly (j_q(a,v)=|a\bar v|_q), not (|a|_q) or a height
   frequency with a different modulus.
4. **`projective_residue_bijection_and_two_sided_count`: pass.**
   Equations (R189.B.4)--(R189.B.5) prove the bijection and count both
   signed residues.
5. **`q_divides_U_divides_u_v_interval_multiplicity`: pass.**
   Divisibility removes the interval-count `+1` and yields (O(u/q))
   occurrences per residue.
6. **`per_v_O_kappa_affine_sites`: pass.**  The factor \(\kappa\)
   appears exactly once in (R189.B.12).
7. **`exact_cU_m_inverse_cq_normalization`: pass.**  This is the exact
   algebraic identity (R189.B.11).
8. **`slow_j_le_floor_U_over_Y_sector_and_exact_complement`: pass.**
   The baseline sector and complement are the disjoint exhaustive
   indicators (R189.B.7).  The optional (P)-enlargement is recorded
   only as a further exact refinement.
9. **`full_factor_Y_before_positive_recombination`: pass for the slow
   sector.**  Equation (R189.B.12) cancels (Y), then (m), at fixed
   indices before the positive divisor ledger.
10. **`kappa_u_m_q_divisor_power_ledger`: pass.**  Equations
    (R189.B.13)--(R189.B.15) expose every power and leave only fixed
    logarithms.
11. **`centered_exact_conductor_identity`: fail as written; pass after
    adding odd (q).**  The proof is (R189.B.19)--(R189.B.20), and the
    even-power counterfamily gives (1/2\ne-1/2).
12. **`prime_bad_slope_height_prefix_survivor`: pass for odd primes.**
    Equation (R189.B.21) gives the exact signed value and discrepancy.
13. **`no_invented_height_BV_or_periodicity`: pass.**  Relation
    (R189.B.22) is explicitly quarantined as missing, not assumed.
14. **`false_unsigned_and_adversarial_controls`: obstruction
    confirmed.**  The slow proof is absolute and therefore safe.
    Formula (R189.B.23) shows that no property supplied for (B), the
    endpoint coefficient, or a character prevents adversarial phase
    alignment in the complement.
15. **`original_t1_only_downstream_scope`: pass.**  No implication is
    asserted beyond the one inherited original-(t=1) residual named
    by the packet.
16. **`exponent_quarantine`: pass.**  No parent, bridge, quarter
    theorem, original (t\ge2) range, large-(G) complement, or
    global exponent is claimed.

## 6. Dependencies and exact artifacts used

Only the following artifacts were used:

1. `protocol.md`.
2. `rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/briefs/blind_dual_frequency_rederivation.md` (task instructions only).
3. `rounds/codex-managed/m9-m1-t1-high-h-dual-height-frequency-gate/blind_statement.md`.

No proof graph, active campaign file, strategy document, prior or
sibling report, control artifact, kernel, source card, proof draft,
validation matrix, or synthesis was inspected.  The arguments above
are algebraic; no external theorem or numerical computation is used as
proof.

## 7. Recommended state effect

- **Promote only after independent seam validation:** the absolute
  (j_q\le\lfloor U/Y\rfloor) slow-sector lemma, its explicit
  (L^2(\log(2L))^4) ledger, and the polylogarithmically enlarged
  saturated version (R189.B.2)--(R189.B.3).
- **Retain open:** the exact signed complement.  Its first required
  new evidence is (R189.B.17), or a literal variation theorem such as
  (R189.B.22), proved for the actual zero-extended amplitude rather
  than a smooth surrogate.
- **Revise:** (B189.8) by adding (q) odd (and exclude or separately
  define (q=2)).
- **Reject:** any uniform polylogarithmic height-prefix claim covering
  the prime slope (-2), and any complement proof using only the
  pointwise bound on (B).
- **No downstream change:** do not alter claims for original
  (t\ge2), the large-(G) near-resonant complement, any parent or
  bridge, the quarter theorem, or the global exponent.
