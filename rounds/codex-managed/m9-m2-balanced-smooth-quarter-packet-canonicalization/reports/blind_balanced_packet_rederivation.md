# Blind statement-only rederivation: balanced smooth quarter packet

## 1. Result

**Conditional exact lemma, with one antecedent seam.**  Once the phrase “the
literal \(g/G\)-profile” is made into the exact profile bridge (2.1) below,
Poisson summation gives (B112.4)--(B112.5) with precisely the displayed two
quarter shifts, their displayed order, the factor \(1/(2i)\), and the outside
factor \(G\).  For the same real profile in the two frequency blocks, the
negative packet is **minus** the complex conjugate of the positive packet;
the two factors \(-1\) (one from the packet and one from conjugating
\(1/(2i)\)) make the physical negative block the complex conjugate of the
positive block.

The direct outside-absolute norm is weaker than shellwise \(\ell ^1\), which
is weaker than product-fibre \(\ell ^1\), which in turn is weaker than any
explicit Cauchy majorant of that product-fibre norm.  Thus any one of those
stronger estimates with the same right-hand side implies (B112.6), but none
of the reverse implications follows.

The first statement-only seam occurs *before* Poisson summation: the blind
statement does not give an equation defining
\(F_{\omega,u,v,G}(g/G)\) from the summand in (B112.1), nor the exact shell
index set/partition-of-unity assembly.  It also gives the negative-frequency
coefficient only verbally.  Consequently the per-profile normalization is
proved exactly, but (B112.5) is not a formally standalone consequence of
(B112.1) until that bridge is written.  No estimate such as (B112.6) follows
from the identity.

## 2. Exact statement and hypotheses

Write \(e(x)=e^{2\pi i x}\).  Let \(G>0\), let
\(\alpha_{u,v}=R\sqrt{uv}\in\mathbb R\), and suppose that the fixed physical
shell is represented *exactly* by

\[
 \mathcal T^+_{\omega,G}(R)
 =\sum_{\substack{u,v\\(u,v)=1\\u\ \mathrm{odd}}}\chi _4(u)
   \sum_{g\in\mathbb Z}\chi _4(g)
   F_{\omega,u,v,G}(g/G)e(g\alpha_{u,v}).                 \tag{2.1}
\]

Here every \(F_{\omega,u,v,G}\in C_c^\infty(\mathbb R)\) is real-valued and
is the zero extension of the physical positive-\(g\) profile.  In particular,
it must include the shell partition and every literal physical weight exactly
once.  The \(u,v\) set and the label/shell set are finite.  Define

\[
 q^+_{\omega,G;u,v}
 :=\sum_{n\in\mathbb Z}\left\{
 \widehat F_{\omega,u,v,G}\bigl(G(n-\alpha_{u,v}-\tfrac14)\bigr)
 -\widehat F_{\omega,u,v,G}\bigl(G(n-\alpha_{u,v}-\tfrac34)\bigr)
 \right\},                                                \tag{2.2}
\]

and

\[
 \mathcal Q^+_{\omega,G}
 :=\sum_{\substack{u,v\\(u,v)=1\\u\ \mathrm{odd}}}
       \chi _4(u)q^+_{\omega,G;u,v}.                       \tag{2.3}
\]

Then

\[
 \boxed{\mathcal T^+_{\omega,G}(R)
       ={G\over 2i}\mathcal Q^+_{\omega,G}(R)},\qquad
 \boxed{\mathcal T^+_{\omega,\mathrm{small}}(R)
       ={1\over2i}\sum_{G<L^{1/2}}G\mathcal Q^+_{\omega,G}(R)}. \tag{2.4}
\]

For the negative-frequency conclusion one additionally assumes the literal
real-even coefficient identity

\[
 \mathcal T^-_{\omega,G}(R)
 =\sum_{\substack{u,v\\(u,v)=1\\u\ \mathrm{odd}}}\chi _4(u)
   \sum_{g\in\mathbb Z}\chi _4(g)
   F_{\omega,u,v,G}(g/G)e(-g\alpha_{u,v}),                 \tag{2.5}
\]

with the **same** real \(F\).  Its direct Poisson packet is

\[
 q^-_{\omega,G;u,v}
 :=\sum_n\left\{
 \widehat F\bigl(G(n+\alpha_{u,v}-\tfrac14)\bigr)
 -\widehat F\bigl(G(n+\alpha_{u,v}-\tfrac34)\bigr)
 \right\}.                                                \tag{2.6}
\]

It obeys

\[
 q^-_{\omega,G;u,v}=-\overline{q^+_{\omega,G;u,v}},\qquad
 \mathcal Q^-_{\omega,G}=-\overline{\mathcal Q^+_{\omega,G}},
 \qquad
 \mathcal T^-_{\omega,G}=\overline{\mathcal T^+_{\omega,G}}. \tag{2.7}
\]

For the norm comparison put \(j=(\omega,G)\),
\(b_{j,p}=G\chi _4(u)q^+_{\omega,G;u,v}\), where
\(p=(u,v)\), and \(a_j=\sum_p b_{j,p}=G\mathcal Q^+_{\omega,G}\).  For any
positive weights \(\mu_{j,p}\), define

\[
 \begin{aligned}
 D&=\left|\sum_j a_j\right|,\\
 H&=\sum_j|a_j|,\\
 P&=\sum_{j,p}|b_{j,p}|,\\
 C_\mu&=\left(\sum_{j,p}\mu_{j,p}\right)^{1/2}
       \left(\sum_{j,p}{|b_{j,p}|^2\over\mu_{j,p}}\right)^{1/2}.
 \end{aligned}                                             \tag{2.8}
\]

Then the exact hierarchy is

\[
 \boxed{D\le H\le P\le C_\mu}.                            \tag{2.9}
\]

An outer-shell Cauchy surrogate
\(C^{\mathrm{sh}}_\lambda=(\sum_j\lambda_j)^{1/2}
(\sum_j|a_j|^2/\lambda_j)^{1/2}\) similarly satisfies
\(D\le H\le C^{\mathrm{sh}}_\lambda\).  An otherwise unspecified “Gram” has no
auditable norm content until its vectors and weights are stated.

Finally, with

\[
 S:=\sum_\omega\sum_{G<L^{1/2}}G\mathcal Q^+_{\omega,G},
 \qquad B:=C_\varepsilon L^{3/2}X^\varepsilon,              \tag{2.10}
\]

the proposed direct estimate \(|S|\le B\) would imply

\[
 \left|\sum_\omega\mathcal T^+_{\omega,\mathrm{small}}\right|
 \le {B\over2},\qquad
 \left|\sum_\omega(\mathcal T^+_{\omega,\mathrm{small}}
                  +\mathcal T^-_{\omega,\mathrm{small}})\right|
 =|\operatorname{Im}S|\le B.                              \tag{2.11}
\]

This is the full logical capacity visible in the blind statement.

## 3. Proof or derivation

If a term is nonzero then \(\chi _4(h)\ne0\), hence \(h\) is odd.  Since
\(h=gu\) with integral \(g,u\), both \(g\) and \(u\) are odd.  Complete
multiplicativity of the character modulo \(4\) gives

\[
 \chi _4(h)=\chi _4(gu)=\chi _4(g)\chi _4(u).               \tag{3.1}
\]

For \(F\in C_c^\infty(\mathbb R)\), \(F(t)\) and its Fourier transform are
Schwartz, so Poisson summation is classical and all Fourier sums below
converge absolutely.  With the convention in (B112.3),

\[
 \sum_{g\in\mathbb Z}F(g/G)e(g\beta)
 =G\sum_{n\in\mathbb Z}\widehat F\bigl(G(n-\beta)\bigr).   \tag{3.2}
\]

Insert

\[
 \chi _4(g)={e(g/4)-e(3g/4)\over2i}.                       \tag{3.3}
\]

For the positive phase the two Poisson frequencies are respectively
\(\beta=\alpha+1/4\) and \(\beta=\alpha+3/4\).  Equation (3.2) therefore gives

\[
 \sum_g\chi _4(g)F(g/G)e(g\alpha)
 ={G\over2i}\sum_n\left[
 \widehat F\bigl(G(n-\alpha-\tfrac14)\bigr)
 -\widehat F\bigl(G(n-\alpha-\tfrac34)\bigr)\right].       \tag{3.4}
\]

This proves every constant and sign in (2.4).  Notice that \(3/4\) may be
replaced, after \(n\mapsto n-1\), by \(-1/4\), but the second term still has
the minus sign.

For the negative phase, \(\beta=-\alpha+1/4\) and
\(\beta=-\alpha+3/4\), giving (2.6).  Since \(F\) is real,
\(\overline{\widehat F(\xi)}=\widehat F(-\xi)\).  Hence

\[
 \begin{aligned}
 \overline{q^+}
 &=\sum_n\left[
   \widehat F\bigl(G(-n+\alpha+\tfrac14)\bigr)
  -\widehat F\bigl(G(-n+\alpha+\tfrac34)\bigr)\right]\\
 &=\sum_m\left[
   \widehat F\bigl(G(m+\alpha-\tfrac34)\bigr)
  -\widehat F\bigl(G(m+\alpha-\tfrac14)\bigr)\right]
 =-q^- ,                                                    \tag{3.5}
 \end{aligned}
\]

where \(m=1-n\).  Because \(\chi _4(u)\) is real, the same identity survives
the \(u,v\) sum.  Finally

\[
 {G\over2i}q^-=-{G\over2i}\overline{q^+}
 =\overline{{G\over2i}q^+},                                \tag{3.6}
\]

which proves physical frequency conjugacy.

The first two inequalities of (2.9) are the triangle inequality; the last
is weighted Cauchy--Schwarz.  Summing (2.4), using (2.7), and observing that

\[
 {S\over2i}+\overline{{S\over2i}}
 ={S-\overline S\over2i}=\operatorname{Im}S               \tag{3.7}
\]

proves (2.11).

Compact physical support makes the original \(h,k\) sum finite.  On
\(g\asymp G\), it bounds \(u\) and \(v\) by constants times \(L/G\) and
\(K/G\), respectively, so the coprime product-fibre set is finite.  Only
finitely many dyadic \(G\) shells meet a positive integral gcd below
\(L^{1/2}\).  The \(n\)-sum is not finite, but it is absolutely convergent
with arbitrary polynomial decay.  “Finite support” must not be misstated as
a finite Poisson-frequency sum.

## 4. First doubtful or unproved step

The first unproved step is the profile bridge (2.1).  The blind statement
names \(F_{\omega,u,v,G}\) but does not state an equality such as

\[
 F_{\omega,u,v,G}(g/G)
 =\psi_G(g)\,A_\omega(gu/L,gv/K)\times
   (\hbox{all remaining literal factors}),                 \tag{4.1}
\]

nor state the exact finite \(\omega\)-assembly or the normalized
partition-of-unity equation for the \(G\)-shells.  Thus one cannot check from
the permitted text whether there is a missing factor, a duplicated weight,
or a profile depending on the sign of the frequency.  This is an
actual-symbol/assembly seam, not a Poisson-sign seam.

The second missing formal antecedent is an explicit negative-frequency
formula establishing (2.5).  Calling the coefficient “literal real-even” is
the correct hypothesis, but the negative block itself is not displayed.
Uniform analytic estimates would additionally require uniform support and
seminorm bounds for the finite family of profiles.  None of these omissions
affects the conditional identities (2.4) and (2.7), but they prevent
promotion of the blind statement as a completely standalone theorem and
prevent any deduction of (B112.6).

## 5. Control tests and outcomes

All controls below are exact finite/algebraic tests; no numerical experiment
is used.

### `quarter_shift_sign_and_2i_normalization`

Take \(G=1\), \(\alpha=0\), and a real \(C_c^\infty\) bump supported near
\(1\), containing no other integer, with \(F(1)=1\).  Put
\(P(\beta)=\sum_n\widehat F(n-\beta)\).  Poisson summation gives
\(P(1/4)=e(1/4)=i\) and \(P(3/4)=e(3/4)=-i\).  Therefore

\[
 {P(1/4)-P(3/4)\over2i}=1=\chi _4(1).
\]

Replacing the difference by a sum gives \(0\); reversing the difference
gives \(-1\); deleting \(1/(2i)\) gives \(2i\).  **Outcome:** the two displayed
shifts, their order, and the normalization all pass, and each listed false
variant fails on a one-point physical sum.

### `odd_h_implies_odd_g_and_u`

The input is an integral factorization \(h=gu\) of a nonzero
\(\chi _4(h)\)-term.  Oddness of a product is equivalent to oddness of both
integer factors.  Equation (3.1) then follows.  **Outcome:** passed exactly;
there is no parity lift or multiplicity.  Even \(g\) or even \(u\) contributes
zero under the character and cannot be treated as a nonzero product fibre.

### `positive_negative_frequency_conjugacy`

Use the same one-point bump but allow any real \(\alpha\).  Then

\[
 q^+=2i\,e(\alpha),\qquad q^-=2i\,e(-\alpha)
       =-\overline{q^+}.
\]

Thus \((2i)^{-1}q^-=e(-\alpha)\) is the conjugate of
\((2i)^{-1}q^+=e(\alpha)\).  The false rule \(q^-=\overline{q^+}\) gives the
negative of the physical answer.  **Outcome:** packet conjugacy carries a
minus sign; physical-block conjugacy does not.

### `outside_absolute_G_sum_vs_shellwise_l1_and_Gram`

For two shells with one fibre each, set \(a_1=M\), \(a_2=-M\).  Then
\(D=0\), while \(H=P=2M\), and the unweighted two-term Cauchy majorant is
\(2M\).  For one shell with two product fibres \(b_1=M,b_2=-M\), one has
\(D=H=0\) but \(P=2M\).  Finally, for two declared fibres \(b=(1,0)\),
\(P=1\) while the unweighted Cauchy majorant is \(\sqrt2\).
**Outcome:** every inequality in (2.9) has the claimed direction, and no
reverse estimate with a uniform constant follows.  In particular a direct
outside-absolute estimate cannot be silently replaced by shellwise
\(\ell^1\), product-fibre absolute values, or a Cauchy/Gram estimate.

### `false_unsigned_and_phase_conjugating_coefficients`

For the unsigned test, take a real bump supported only at the physical
integer \(g=3\), with value \(1\), and \(\alpha=0\).  The signed character and
the quarter-difference both give \(\chi _4(3)=-1\), whereas replacing
\(\chi _4\) by \(|\chi _4|\) gives \(+1\).  **Outcome:** the packet is genuinely
signed and does not represent the unsigned model.

For the phase test, use one physical point \(g=1\) with coefficient \(c=i\)
in both frequency blocks.  The blocks are \(i e(\alpha)\) and
\(i e(-\alpha)\), while the conjugate of the first is \(-i e(-\alpha)\).
**Outcome:** reusing a complex phased coefficient in both blocks destroys
conjugacy, so reality of the frequency-even coefficient cannot be dropped.
If the negative coefficient is instead explicitly \(\overline c\), conjugacy
is restored, but that is a *conjugate-paired* complex theorem and its negative
packet must use \(\overline F\), not the unchanged positive profile.  It does
not justify the real-even statement by phase-blind reasoning.

### `capacity_and_downstream_scope`

Equations (2.10)--(2.11) give the exact constants: the direct packet bound
gives half that bound for the positive block and the full bound for the
two-sided real block.  Conversely, the finite model \(S=M\in\mathbb R\) has
two-sided block \(\operatorname{Im}S=0\) but positive-block size \(M/2\) and
direct packet size \(M\).  **Outcome:** (B112.6) is sufficient and is stronger
than a bound only for the assembled two-sided block.  Its scope is only the
real smooth balanced labels, fixed finite subdivision of
\(1\le K/L\le16\), and \(G<L^{1/2}\), uniformly in real \(X>0\) only if its
constant is proved uniformly.  It says nothing about the separated exact,
near-square, hard-endpoint, or large-gcd owners, and it implies neither
M9--M2, M9, nor a Gauss-circle exponent from the permitted statement alone.

## 6. Dependencies and exact artifacts used

Only the following artifacts were read:

1. `rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/briefs/blind_balanced_packet_rederivation.md` (task and isolation contract),
2. `rounds/codex-managed/m9-m2-balanced-smooth-quarter-packet-canonicalization/blind_statement.md` (the complete mathematical input),
3. `state/control_models.md` (control definitions), and
4. `problems/gauss_circle.md` (repository-level problem statement).

No graph, proof-obligation file, strategy file, derivation packet, candidate,
prior balanced-packet derivation, sibling report, web source, or computational
artifact was read or used.  The derivation uses only character parity and
multiplicativity, classical Poisson summation for \(C_c^\infty\) functions,
Fourier conjugacy for real functions, the triangle inequality, and weighted
Cauchy--Schwarz.

## 7. Recommended state effect

**Revise, then promote only the normalization sublemma.**  Add the literal
profile equality (2.1)/(4.1), the normalized shell index and one-count
assembly, and the displayed negative block (2.5).  Once those antecedents are
checked, the quarter-shift Poisson identity, parity statement, conjugacy
identity, norm hierarchy, and implication constants are ready for promotion.
Retain (B112.6) as an open direct target.  Make no state change for the target,
the separated owners, M9--M2, M9, or any exponent on the basis of this report.
