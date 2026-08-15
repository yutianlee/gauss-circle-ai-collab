## Result

There is a genuine strict-subrange estimate for the smooth odd nonaxial
row, and there is also a genuine non-self-returning spectral reduction for
the remaining range.  Neither currently proves the full frozen target.

For \(q=4b\), split the odd row into reduced residue classes
\(c=r\pmod q\).  On such a class the inverse phase and every local unit
depending only on \(c\pmod {4b}\) are constant.  If the actual Farey weight
on that class is partitioned into intervals \(I_i\) such that

\[
 \sum_i |I_i|\ll C,qquad \#\{I_i\}\ll X^\varepsilon Q,qquad
 \|w_i\|_\infty+\operatorname {Var}(w_i)\ll X^\varepsilon,       \tag{1.1}
\]

then the exact third-derivative test gives

\[
 |S_{b,k}(C)|
 \ll X^\varepsilon
 \left(CQ^{-1/6}+C^{1/2}Q^{2/3}\right).                         \tag{1.2}
\]

Consequently

\[
 \mathcal E_{C,k}\ll \frac{J^2}{T}X^\varepsilon
 \quad\hbox{for}\quad
 J^{2/3}<C\le J^{32/45}=X^{16/45}.                              \tag{1.3}
\]

The powers in (1.2)--(1.3), the progression normalization, the gcd
deletion, and the Farey-neighbor *piece count* all pass hostile audit.  In
fact each reduced class has only \(O(1+Q/b)\) neighbor regimes and there
are \(O(b)\) classes, so the total is \(O(b+Q)=O(Q)\), not
\(O(bQ)\).  The remaining condition is analytic rather than combinatorial:
each retained incomplete-Fresnel transition must have the bounded
variation asserted in (1.1).  The inherited smooth nontransition pieces
have this property.  The frozen packet records the transition faces but
does not itself contain the derivative lemma which proves (1.1) for every
sharp entry/exit piece.  Thus (1.3) is a proved scoped consequence once
that exact transition-BV lemma is attached; without it, the unconditional
scope is the smooth nontransition odd nonaxial family.  The two even local
classes and both surviving axes still require separate derivations.

For the rest of the odd positive branch, reciprocity does more than the
forbidden one-variable self-return.  It cancels the term \(k/(4bc)\), and
completion in \(b\pmod c\) produces a length-\(T\) displacement \(h\) and
the complete generalized Kloosterman sum

\[
 \frac1c S_{\infty,1}(N-h,k;2c)
 =\frac1c S((N-h)\overline4,k;c).                               \tag{1.4}
\]

The associated Kuznetsov argument is

\[
 x_{h,c}=\frac{2\pi\sqrt{(N-h)k}}c,                             \tag{1.5}
\]

and the external phase is exactly \(e(-J\sqrt{k}/c)\).  Hence it
matches the \(e^{-ix}\) Bessel branch, with phase error
\(O(T/(CJ))\).  For \(R=J/C\), the formal phase-specific transform has
size \(R^{-1/2}\) and spectral support \(t^2\lesssim R\).  This is a
strictly smaller survivor than the accepted \(c\)-Poisson/\(n\)-B-process
self-return: it is a short level-four automorphic coefficient sum of
length \(T\), centered at index \(X\).

The spectral route nevertheless stops at an unavailable input.  Even in a
factorized smooth model it needs, uniformly for level-four forms with
\(|t_f|\lesssim\sqrt R\), a bound of the shape

\[
 \sum_{|h|\lesssim T}F(h/T)\lambda_f(N-h)
 \ll X^{1/4+\varepsilon}.                                      \tag{1.6}
\]

This is the classical conjectural pointwise scale, not an audited theorem;
the actual \(F\) is moreover \(c\)-dependent and must be separated from the
Farey transition symbol.  A cusp-form bound alone would not dispose of the
continuous spectrum.  The completion weight has useful zero moments, but
their use in the Eisenstein integral has not been proved here.  The periodic
odd local unit, the opposite orientation, the even cusps, and zero-index
axes are also not automatic consequences of (1.4).

Thus (72.8) is plausible and is proved on the strict odd nonaxial subrange
(1.3), subject only to the explicit transition-BV seam just stated.  No
actual-symbol counterexample was found for larger \(C\), but no primary
source closes it either.

## Exact statement and hypotheses

Put

\[
 J=X^{1/2},\qquad Q=X^{1/5}=J^{2/5},\qquad
 T=J/Q=J^{3/5},\qquad B=C/T,                                   \tag{2.1}
\]

and let \(J^{2/3}<C\le J\), \(b\asymp B\), and \(k>0\) belong to
the fixed finite compatible stationary family.  Write

\[
 A_b=bX+J\sqrt{k}+\frac{k}{4b},\qquad q=4b.                    \tag{2.2}
\]

The row to be estimated is

\[
 S_{b,k}(C)=
 \sum_{\substack{c\asymp C\\(c,q)=1}}
 a_{b,c,k}(X)e_q(k\bar c)e(-A_b/c).                            \tag{2.3}
\]

For the third-derivative assertion, the precise weight hypothesis is the
following.  For every reduced \(r\pmod q\), unfold
\(c=r+qn\) in the dyadic interval and partition the resulting integer
interval into \(I_{r,j}\).  On \(I_{r,j}\), after the constant inverse and
local unit have been removed, the restriction \(w_{r,j}(n)\) of
\(a_{b,r+qn,k}\) has

\[
 \|w_{r,j}\|_\infty+\operatorname {Var}_{I_{r,j}}(w_{r,j})
 \ll X^\varepsilon.                                           \tag{2.4}
\]

The union is disjoint up to endpoints, its total number of integers is
\(O(C)\), and

\[
 P_b:=\sum_{r\bmod q}^{*}\#\{j:I_{r,j}\ne\varnothing\}
 \ll X^\varepsilon Q.                                         \tag{2.5}
\]

The \(X^\varepsilon\) in (2.4)--(2.5) may absorb the fixed symbol
partition and divisor losses, but not a power of \(J/C\).  Under these
hypotheses, (1.2) and (1.3) hold uniformly in the finite positive \(k\)
family.

For the spectral reduction, write \(X=N+\vartheta\) with
\(N=\lfloor X\rfloor\), and assume initially that the odd local periodic
unit has been frozen or represented by the correct fixed-level cusp data.
Let

\[
 W_c(b)=a_{b,c,k}(X)e(-\vartheta b/c),\qquad
 \widehat W_c(h)=\sum_{r\bmod c}W_c(r)e_c(-hr).                 \tag{2.6}
\]

The model short-sum conclusion additionally assumes that the effective
\(|h|\lesssim T\) portion of \(\widehat W_c(h)\) is a bounded sum of
products of a common smooth \(h/T\)-weight and a smooth \(c/C\)-weight,
with summable decomposition norms.  This factorization is not asserted for
the sharp Farey-neighbor transitions.

## Proof or derivation

On a fixed reduced class \(c=r+qn\), the inverse phase in (2.3) is
constant and the remaining phase is

\[
 f_{b,r}(n)=-\frac{A_b}{r+qn}.
\]

Since \(A_b\asymp bX\), \(q=4b\), \(c\asymp C\), and
\(b\asymp C/T\),

\[
 f'''_{b,r}(n)=\frac{6A_bq^3}{(r+qn)^4}
 \asymp \frac{Xb^4}{C^4}
 \asymp \frac{X}{T^4}=Q^{-1}.                                 \tag{3.1}
\]

It has constant sign and changes by only a fixed factor on a dyadic
interval.  The third-derivative estimate needed here is

\[
 \sum_{n\in I}e(f(n))
 \ll L\lambda^{1/6}+L^{1/2}\lambda^{-1/6},                    \tag{3.2}
\]

when \(|I|=L\) and \(|f'''|\asymp\lambda\) with constant sign.
For completeness, take one Weyl differencing step of length
\(H\asymp\lambda^{-1/3}\).  The differenced phase has second derivative
\(\asymp h\lambda\); the second-derivative estimate and summation over
\(h\le H\) give

\[
 |S|^2\ll L^2\lambda^{1/3}+L\lambda^{-1/3},
\]

which is (3.2).  If \(L<H\), the trivial bound is already at most the
second term of (3.2).  Abel summation multiplies (3.2) by at most
\(\|w\|_\infty+\operatorname {Var}(w)\), so it applies to (2.4).

With \(\lambda=Q^{-1}\), sum (3.2) over all pieces.  Since
\(\sum_iL_i\ll C\), (2.5) and Cauchy give

\[
\begin{aligned}
 |S_{b,k}(C)|
 &\ll X^\varepsilon
 \left(Q^{-1/6}\sum_iL_i+Q^{1/6}\sum_iL_i^{1/2}\right)\\
 &\ll X^\varepsilon
 \left(CQ^{-1/6}+Q^{1/6}(P_bC)^{1/2}\right)\\
 &\ll X^\varepsilon
 \left(CQ^{-1/6}+C^{1/2}Q^{2/3}\right),
\end{aligned}                                                   \tag{3.3}
\]

which proves (1.2).  This calculation is important: splitting into
\(O(Q/b)\) transition regimes per residue class does not multiply the
first term, and the square-root term sees only the total piece count.

The Farey-neighbor combinatorics is compatible with (2.5).  A predecessor
or successor denominator \(d_\pm\) satisfies

\[
 bd_\pm\mp1=m_\pm c,qquad J-c<d_\pm\le J.                    \tag{3.4}
\]

When \(c\pmod{4b}\) is fixed, \(m_\pm\pmod b\) is fixed.  Across
\(c\asymp C\), the threshold \(bJ/c\) moves through \(O(Q)\), and the
allowable values of \(m_\pm\) are spaced by \(b\).  Thus each residue has
\(O(1+Q/b)\) neighbor regimes.  There are at most \(4b\) reduced
residues, and \(b\ll C/T\le J/T=Q\), whence

\[
 P_b\ll b(1+Q/b)\ll Q.                                        \tag{3.5}
\]

On a regime with fixed \(m_\pm\), (3.4) makes the endpoints rational
smooth functions of \(c\).  Fixed dyadic and ratio cutoffs add only
\(O(1)\) subdivisions.  A retained Fresnel transition also adds only
\(O(1)\) subdivisions if its signed endpoint parameter is monotone there.
This proves the piece count.  It does not by itself prove (2.4): that
requires differentiating the exact incomplete-Fresnel entry/exit factor.

Now sum (3.3) over \(b\asymp B=C/T\).  Absorbing the cross term,

\[
 \mathcal E_{C,k}
 \ll \frac CT X^\varepsilon
 \left(C^2Q^{-1/3}+CQ^{4/3}\right).                            \tag{3.6}
\]

The first term is at most \(J^2/T\) when

\[
 C^3\le J^2Q^{1/3},\qquad C\le J^{32/45},                      \tag{3.7}
\]

and the second permits the larger range

\[
 C\le JQ^{-2/3}=J^{11/15}.                                    \tag{3.8}
\]

Hence (3.7) is decisive.  No diagonal, near-diagonal, square-center, or
fourth-power exception was removed: (3.1) is uniform in the real \(X\),
so (3.6) bounds all of them together.

For the spectral route, odd reciprocity gives the exact identity

\[
 e_{4b}(k\bar c)=e_c(-k\overline{4b})e(k/(4bc)).                \tag{3.9}
\]

The last factor cancels the last term of \(A_b/c\).  With
\(\kappa_c=k\overline4\pmod c\),

\[
 e_{4b}(k\bar c)e(-A_b/c)
 =e(-J\sqrt{k}/c)e(-\vartheta b/c)
  e_c(-Nb-\kappa_c\bar b).                                    \tag{3.10}
\]

Finite Fourier inversion in \(b\pmod c\) therefore gives

\[
 \sum_bW_c(b)e_c(-Nb-\kappa_c\bar b)
 =\frac1c\sum_{h\bmod c}\widehat W_c(h)
   S(h-N,-\kappa_c;c)                                         \tag{3.11}
\]

and the change \(x\mapsto-x\), followed by \(x\mapsto\overline4x\),
gives

\[
 S(h-N,-\kappa_c;c)=S((N-h)\overline4,k;c).                   \tag{3.12}
\]

Because the \(b\)-support has length \(B=C/T\), smooth completion has
effective signed displacement \(|h|\lesssim c/B\asymp T\).  Pascadi's
generalized-sum formula, with \(q=4,r=4,s=1\), identifies

\[
 S_{\infty,1}(N-h,k;2c)=S((N-h)\overline4,k;c),
 \qquad c\ \mathrm{odd}.                                         \tag{3.13}
\]

Thus this is the \((\infty,1)\) cusp pair on \(\Gamma_0(4)\), with
generalized modulus \(2c\); it is not literally a full-level sum with a
fractional index \(k/4\).

The same-sign Kuznetsov argument is (1.5).  Since

\[
 J-\sqrt{N-h}=\frac{\vartheta+h}{J+\sqrt{N-h}},
\]

the difference between the external exponent and \(-ix_{h,c}\) is

\[
 O\!\left(\frac{T+1}{CJ}\right),                               \tag{3.14}
\]

uniformly in the upper range.  Constants and sign therefore match.

For the model test \(\phi_R(x)=w(x/R)e^{-ix}\), Pascadi's same-sign
transform is

\[
 \widetilde\phi_R(t)=\frac{\pi}{\sinh\pi t}
 \int_0^\infty\frac{J_{2it}(x)-J_{-2it}(x)}{2i}
 \phi_R(x)\frac{dx}{x}.                                      \tag{3.15}
\]

For \(t^2\ll R\), the phase-matched large-\(x\) branch has leading
kernel

\[
 \frac{\pi}{\sinh\pi t}\frac{J_{2it}(x)-J_{-2it}(x)}{2i}
 =\left(\frac{2\pi}{x}\right)^{1/2}
   \sin(x-\pi/4)+\text{uniform remainder}.                    \tag{3.16}
\]

Multiplication by \(e^{-ix}\) leaves one nonoscillatory branch, so

\[
 \widetilde\phi_R(t)\asymp R^{-1/2},\qquad t^2\lesssim R,      \tag{3.17}
\]

at the formal leading scale; the other branch integrates by parts.  For
\(R\asymp1\) this reads \(O(1)\).  A complete proof still needs uniform
Bessel asymptotics through \(t^2\asymp R\) and decay beyond it.  The generic
transform lemma in Pascadi is not that proof, because its hypothesis
\(\phi^{(j)}(x)\ll R^{-j}\) is violated by \(e^{-ix}\).

The normalization also closes exactly if (1.6) is granted.  The original
coefficient \(T/\sqrt{CJ}\), the completion factor \(B/C=1/T\), and the
conversion from raw \(S\) to the Kuznetsov weight \(S/(2c)\) leave an
outer factor \(\asymp\sqrt{C/J}\).  There are \(O(RX^\varepsilon)\)
fixed-level spectral modes with \(t^2\lesssim R\).  The transform
\(R^{-1/2}\) and a uniform short-sum bound \(X^{1/4+\varepsilon}\) give
the formal spectral factor

\[
 X^{1/4}\sqrt R=\frac{J}{\sqrt C};                             \tag{3.18}
\]

multiplication by \(\sqrt{C/J}\) gives \(J^{1/2}\), the required odd
first moment.  This ledger verifies the proposed powers, but (1.6) and
the actual-symbol separation are not established.

The completion weight is more structured than an arbitrary bump.  If it
is unfolded without truncation, then

\[
 \sum_{h\bmod c}\widehat W_c(h)=cW_c(0)=0                     \tag{3.19}
\]

because the \(b\)-support is away from zero; in the smooth model this
becomes vanishing moments of the \(h/T\)-profile.  This may cancel the
smooth main terms in the Eisenstein coefficients.  It does not supply a
published pointwise cusp-form estimate at (1.6), nor has the required
continuous-spectrum calculation with the actual transition weight been
carried out.

## First doubtful or unproved step

For the strict third-derivative range, the first unproved seam in the
frozen artifacts is (2.4) on every sharp neighbor-dependent transition.
The combinatorial count (3.5) is sufficient: one may sum the first term of
the derivative estimate by total length and the second by Cauchy.  What
must not be done is replace the exact incomplete-Fresnel factor merely by
its \(O(1)\) size.  On each fixed-neighbor regime one must show that its
signed entry/exit parameter is monotone after \(O(1)\) subdivisions and
that the composed transition factor has
\(O(X^\varepsilon)\) total variation.  A power loss per piece, or more
than \(X^\varepsilon Q\) total pieces, would change (3.3).  The inherited
smooth-interior symbols already meet (2.4).

Even after that lemma, (1.3) is only the positive odd nonaxial branch.
For \(c\equiv2\pmod4\), the invariant product
\(\chi_4(s_0)e_{2c}(\sigma s_0)\), and for \(4\mid c\), the factor
\(\chi_4(s_0)e_c(\sigma s_0)\), use lifts
\(s_0\equiv-\rho\bar b\pmod c\).  Their reciprocity moduli, lift parity,
and transition weights must be derived before applying the same derivative
test.  The odd \(\rho=0\) and \(4\mid c,\sigma=0\) axes are degenerate
stationary families and are not limits of (3.1).

For the spectral route there are two nested doubtful steps.  First, the
actual \(\widehat W_c(h)\), including the periodic odd unit and
Farey-neighbor faces, must be decomposed into common Kuznetsov tests with
summable norms; splitting \(\chi_4(c)\) into residue classes is not by
itself the level-four cusp identity (3.13).  Second, even in the ideal
factorized model, no audited primary theorem gives (1.6) uniformly in the
Maass parameter, holomorphic weight, cusp, and oldform data.  The
Eisenstein integral needs a separate use of (3.19).  These are theorem
gaps, not another instance of the already rejected \(c\)-Poisson
self-return.

## Required control test and outcome

| Control | Outcome |
|---|---|
| Derivative normalization | **Pass.** In the progression index, not in \(c\), \(f'''=6A_b(4b)^3/c^4\asymp X/T^4=Q^{-1}\). |
| Third-derivative theorem | **Pass.** One A-process and the second-derivative test give \(LQ^{-1/6}+L^{1/2}Q^{1/6}\), including \(L<Q^{1/3}\) by the trivial bound. |
| Residue classes and gcd | **Pass.** Only reduced \(r\pmod{4b}\) occur; the inverse, \(\chi_4(c)\), and any \(4b\)-periodic local unit are constant.  There are \(O(b)\), not \(O(C)\), classes. |
| Farey-neighbor piece count | **Pass.** Equation (3.4) gives \(O(1+Q/b)\) regimes per residue and \(P_b\ll b+Q\ll Q\). |
| Transition bounded variation | **Open at the artifact seam.** Boundedness is insufficient.  The exact incomplete-Fresnel entry/exit factor must satisfy (2.4) on the \(O(Q)\) pieces. |
| Row and energy powers | **Pass.** Equations (3.3), (3.6), and (3.7) give \(C\le J^{32/45}\); the second term alone permits \(J^{11/15}\). |
| Diagonal and near diagonal | **Pass in the scoped range.** The row estimate bounds the entire energy before expansion and includes the exact diagonal \(BC=C^2/T\le J^2/T\). |
| Perfect squares/fourth powers | **Pass.** The nonzero derivative (3.1) is uniform in the real center \(X\); no arithmetic-center exception is used.  This gives no lower bound against (72.8) above the scoped range. |
| \(b=O(1)\) | **Out of the upper principal row.** Here \(b\asymp C/T\gg J^{1/15}\).  Any small-\(b\) transition or tail is a separate term. |
| Finite \(k\)-sum | **Pass for positive compatible nonaxial \(k\).** \(A_b\asymp bX\) uniformly and the fixed number of modes is harmless.  Other orientations are not inferred by sign. |
| Reciprocity constants/sign | **Pass.** Equations (3.9)--(3.14) give generalized modulus \(2c\), Bessel argument \(2\pi\sqrt{(N-h)k}/c\), and the matching negative branch. |
| Completion length/index | **Pass with distinction.** The displacement has length \(T\), but the automorphic index is \(N-h\asymp X\); replacing its magnitude by \(T\) in a spectral large sieve is illegal. |
| Bessel transform | **Plausible, not fully proved.** The leading branch is \(R^{-1/2}\) for \(t^2\lesssim R\); a phase-specific uniform transition/tail lemma is still needed. |
| Short GL2 theorem | **Fail as a source import.** The required pointwise \(X^{1/4}\) scale is conjectural even for a fixed cusp form; available results are average, longer-scale, or coefficient-blind large sieves paying index \(X\). |
| Continuous spectrum | **Open.** A bound for cusp forms does not cover it.  The exact zero-moment identity (3.19) is favorable but has not been propagated through the actual level-four Eisenstein coefficients. |
| Periodic odd unit/level | **Open.** Pascadi's unweighted \((\infty,1)\) identity proves (3.13); the inherited modulus unit needs an exact higher-level, character, or residue-class trace formula. |
| Even local classes | **Open.** Their lift-dependent units and cusp data are not obtained by changing the sign of \(k\). |
| Axes/zero indices | **Open.** Same-sign Kuznetsov in the cited form assumes positive indices.  Ramanujan and twisted zero-index sums can have gcd of size \(c\). |
| One-variable self-return | **Avoided.** The derivative proof stops after residue splitting; the spectral proof changes the survivor to a short automorphic coefficient sum.  Neither repeats the \(c\)-Poisson/\(n\)-B-process loop. |
| Global scope | **Pass.** No cone-edge, full \(M9\!-\!M1\), \(M9\), or final-exponent claim follows from this fixed-interior result. |

No numerical experiment was used.  Perfect-power and transition checks
were algebraic; computation cannot certify the missing asymptotic bounds.

## Dependencies and exact artifacts/sources used

The repository artifacts used were exactly:

* `protocol.md`;
* `state/proof_obligations.yml` and `state/active_campaign.yml`;
* the assigned Round-72 brief, `plan.json`, and `derivation_packet.md`;
* `rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/synthesis.md`;
* `rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/reviews/conductor_round71_adjudication.md`;
* `rounds/codex-managed/m9-m1-short-numerator-kloosterman-large-sieve/reports/short_numerator_source_hostile_audit.md`.

No sibling Round-72 report was read.

The primary-source audit was:

* **Cusp identity, Kuznetsov normalization, and spectral large sieve.**
  Pascadi,
  [*Large sieve inequalities for exceptional Maass forms and the greatest
  prime factor of \(n^2+1\)*, Forum Math. Pi 14 (2026), e8](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/DC9B30CB4824955671C7B018C473863A/S2050508626100250a.pdf/large-sieve-inequalities-for-exceptional-maass-forms-and-the-greatest-prime-factor-of-dollarn21dollar.pdf),
  Lemma 3.2, Proposition 3.5, Lemmas 3.4 and 3.9, and Theorem 5.2.
  Lemma 3.2, with \(q=rs=4,r=4,s=1\), gives exactly (3.13).
  Proposition 3.5 has complete generalized Kloosterman sums, positive
  indices, specified cusps, and a smooth compact Bessel test.  Lemma 3.9
  bounds arbitrary coefficients at indices \(n\asymp N_0\) by a term of
  shape \(K^2+\mu(\mathfrak a)N_0^{1+\varepsilon}\); here
  \(N_0\asymp X\), not \(T\).  Lemma 3.4 assumes slowly varying tests and
  does not accept \(w(x/R)e^{-ix}\).  Theorem 5.2 improves the exceptional
  spectrum under frequency-concentration hypotheses, not the regular,
  holomorphic, and Eisenstein spectra required here.

* **Pointwise \(X^{1/4}\) status.** Hafner--Ivic,
  [*On sums of Fourier coefficients of cusp forms*, Enseign. Math. 35
  (1989), 375--382](https://www.e-periodica.ch/cntmng?pid=ens-001%3A1989%3A35%3A%3A150),
  records the classical conjectural \(X^{1/4+\varepsilon}\) scale and
  proves the classical \(X^{1/3}\)-type pointwise upper scale for a fixed
  form.  Hulse--Kuan--Lowry-Duda--Walker,
  [*The Second Moment of Sums of Coefficients of Cusp Forms*](https://arxiv.org/abs/1512.01299),
  proves smoothed second-moment/average results, not a pointwise estimate
  uniform over the level-four spectral family.  Neither theorem gives
  (1.6), its \(t\)-uniformity, or its transition-dependent weight.

* **Trilinear inverse fractions.** Bettin--Chandee,
  [*Trilinear forms with Kloosterman fractions*](https://arxiv.org/abs/1502.00769),
  Theorem 1 and Remark 1, bounds separated arbitrary coefficient sequences
  in \(a,m,n\).  Its two displayed terms have powers
  \((AMN)^{7/20}(M+N)^{1/4}\) and
  \((AMN)^{3/8}(AN+AM)^{1/8}\).  Remark 1 permits a differentiable coupled
  weight but multiplies the result by
  \((1+(|\vartheta|A+\mathcal X)/(MN))^{1/2}\).  Mapping
  \(m\asymp C,n\asymp B\) and \(e(-A_b/c)\) forces this factor to be at
  least \((1+X/T)^{1/2}\), and the actual Farey matrix weight is not
  separated.  It is therefore weaker than (1.2) and does not prove
  (72.8).

* **Modulus-averaged Kloosterman second moment.**
  Blomer--Risager--Shparlinski,
  [*Triple sums of Kloosterman sums and the discrepancy of modular
  inverses*](https://arxiv.org/abs/2411.17823), Theorem 1.3, gives, in
  its notation,

  \[
   \sum_{N_0\le |n|<2N_0}\left|\sum_{c\le Z}S(n,1;c)\right|^2
   \ll (N_0Z^2+N_0^{1/3}Z^{7/3})(N_0Z)^{o(1)}.
  \]

  It averages a complete dyadic \(n\)-block of length and magnitude
  \(N_0\).  Selecting a length-\(T\) window centered at \(X\) still pays
  \(N_0\asymp X\), and the theorem has neither the phase-matched
  level-four cusp weight nor the actual \(c,h\) matrix symbol.

* **Newest fixed-modulus bilinear Kloosterman bound.**
  Blomer--Pascadi,
  [*Bilinear forms with Kloosterman sums via quadratic characters*](https://arxiv.org/abs/2607.24311),
  Theorems 1.1 and 5.5, treats one fixed modulus \(c\), arbitrary
  coefficient sequences on intervals of lengths \(M,N\), and sums
  \(S(am,n;c)\), with a \(c^{-1/32}\) saving in the balanced
  \(M=N\asymp\sqrt c\) case.  It does not average the modulus, does not
  contain \(e(-J\sqrt k/c)\), and does not cover one fixed index \(k\)
  against a length-\(T\) window near magnitude \(X\) with the level-four
  transition weight.  Its exceptional-spectrum application is not a full
  regular spectral estimate.

* **General level/cusp and zero-index warning.** Knightly--Li,
  [*Kuznetsov's trace formula and the Hecke eigenvalues of Maass
  forms*](https://arxiv.org/abs/1202.0189), Theorems 7.14, 8.1, and 9.2,
  supplies complete generalized twisted sums only after the level,
  nebentypus, cusp pair, scaling matrices, and gcd factors are fixed.  It
  does not identify the two even local lines or bound the surviving zero
  indices automatically.

Every imported result was checked at the averaged variables, index
magnitude and span, coefficient dependence, completeness, smoothing,
level and cusp, nebentypus/local unit, zero indices, spectral-parameter
uniformity, and numerical power.

## Recommended state effect

**Retain the full upper-conductor energy estimate (72.8) as open, but
record a strict odd nonaxial advance.**  Promote the self-contained
third-derivative lemma (3.1)--(3.3), the exact neighbor count
(3.4)--(3.5), and the energy exponent \(C\le J^{32/45}\).  If an
independent seam check verifies (2.4) for every retained entry/exit
transition, promote (1.3) for the complete positive odd nonaxial row;
otherwise restrict the promotion to its smooth nontransition pieces and
retain the transition faces explicitly open.

Retain as derived candidate evidence the exact reciprocity/completion/cusp
reduction (3.9)--(3.14).  Record its smallest survivor as a phase-matched
level-four short automorphic coefficient problem at length \(T\), center
\(X\), spectral width \(t^2\lesssim J/C\), together with the favorable
zero-moment identity (3.19).  Do not promote the transform bound (3.17) or
the closing ledger (3.18) until a uniform phase-specific Bessel lemma, the
actual-symbol decomposition, a pointwise short-coefficient estimate, and
the Eisenstein calculation are proved.

Do not transfer either argument to the \(c\equiv2\pmod4\) or \(4\mid c\)
families, the odd \(\rho=0\) axis, or the \(4\mid c,\sigma=0\) axis without
their exact local derivations.  No fixed-interior result here promotes the
cone edges, full \(M9\!-\!M1\), \(M9\), or the Gauss-circle exponent.
