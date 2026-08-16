# Blind offset-dispersion rederivation

## 1. Result

**Result: exact decomposition, followed by an unresolved actual-symbol
survivor.**  The
ordered residue-pair decomposition (83.5)--(83.6), the removal of the
same-residue mode, and the odd inverse-unit identity (83.11) are exact.  On
opening the two progression sums and completing only the residue variable,
the first strict survivor is an actual-weight correlation between a rational
complete sum and the finite Fourier transform of the reciprocal weight; it is
displayed as \(\mathfrak D_{\rm act}^{\rm odd}\) in Section 3.

The repaired hypotheses remove two former objections: \(k\) is fixed and
nonzero, and both the exact value of \(A_{\kappa,b}\) and a global bounded
variation estimate for \(V\) are now available.  Accordingly, the former
statement-level no-go and the unrestricted-weight countermodel are withdrawn.
No bound \(B^{-\delta}\), for any fixed \(\delta>0\), is proved by this
rederivation.  The remaining obstructions are narrower.

1. Even for fixed \(k\ne0\), prime-square and prime-fourth-power moduli have
   nonzero offsets for which the zero additive-frequency rational sum has
   sizes \(q^{3/4+o(1)}\) and \(q^{7/8+o(1)}\), respectively.  Thus a
   pointwise square-root estimate uniform in the offset is false; a
   gcd-sensitive *average* estimate would be needed.  These exceptional sums
   do not by themselves refute an aggregate gain.
2. The bounds \(A_{\kappa,b}\asymp bX\) and
   \(\|V\|_\infty+\operatorname {Var}V\ll X^\varepsilon\) constrain the
   actual Fourier vector, but no weighted rational-sum estimate has yet been
   derived from them.  Opening \(R(r)\) also separates the cancellation
   already encoded in (83.4), so an argument must preserve that saving while
   exploiting the now-explicit reciprocal phase.

The phase-conjugating arbitrary-coefficient test still saturates the factor
\(B\), but the BV hypothesis means it is only a control against a
coefficient-blind argument, not an admissible actual-weight counterexample.
For \(\kappa=1/4\), the exact identity
\(A_{1/4,b}=bX+\sqrt{kX}+k/q\) also shows that one orientation cancels the
\(k/(qc)\) correction in additive reciprocity.  This makes the joint
actual-symbol correlation essential; it supplies neither a saving nor a
no-go by itself.
The even local units and aliases are absent from the permitted inputs, so no
all-class range extension can be certified here.

## 2. Exact statement and hypotheses

Assume only (83.1)--(83.4), including (83.3a), with \(J=X^{1/2}\), \(Q=J^{2/5}\),
\(T=J^{3/5}\), \(B=C/T\), \(J^{13/18}<C\leq J^{3/4}\), and \(q=4b\) for
\(b\asymp B\).  Fix one odd local component \(\kappa=1/4\), one alias and
orientation, and one compatible fixed nonzero \(k=O(1)\).  In addition,
\[
 A_{\kappa,b}=\left(\sqrt{bX}+\sqrt{\kappa k/b}\right)^2\asymp bX,
 \qquad
 \|V\|_\infty+\operatorname {Var}_{[C,2C]}V\ll_\varepsilon X^\varepsilon.
                                                                    \tag{R83.0}
\]
All dyadic endpoints,
admissibility conditions, and progression weights are retained exactly.

Let \(\mathcal A_b\) be the set of nonzero \(a\in\mathbb Z/q\mathbb Z\)
for which there is an admissible \(r\) with both \(r\) and \(r+a\) in
\(\mathscr R_{\kappa,b}\).  In the odd unit class, \(r\) and \(r+a\) are
units modulo \(q\), hence are odd, so every odd \(a\) is an exact zero layer
and is omitted from \(\mathcal A_b\) once.  Extra local restrictions may
make further layers empty; they too are omitted only through this definition.

The claims proved below are:

* Every ordered pair \((r,s)\) of distinct admissible residues occurs once
  and only once as \((r,r+a)\) for a unique \(a\in\mathcal A_b\).  Thus
  (83.5)--(83.6) is exact, and \(a=0\) removes the entire same-residue energy
  exactly once, not merely the terms with equal original rows.
* In the odd class, after opening the original progressions and retaining the
  full reciprocal phase, the exact expression is
  \[
  \mathfrak X_C^{(1/4,k)}=\mathfrak D_{\rm act}^{\rm odd}
  :=\sum_{b\asymp B}{1\over q}\sum_{a\in\mathcal A_b}
    \sum_{d\bmod q}K_q(a,k;d)\,\mathcal W_{b,a}(d),                 \tag{R83.1}
  \]
  where \(K_q\) and the actual-weight transform \(\mathcal W\) are defined
  in Section 3.  No stationary truncation or tail deletion occurs in this
  identity.
* A gain \(B^{-\delta}\) is exactly the missing estimate
  \[
    |\mathfrak D_{\rm act}^{\rm odd}|
       \ll_\varepsilon X^\varepsilon
       C^2B^{1-\delta}Q^{-5/12}.                                  \tag{R83.2}
  \]
  Estimate (R83.2) is the unresolved analytic claim; it is not proved or
  refuted here.

The former formal model \(R(r)=H\overline{u(r)}\), obtained by freely
choosing one row per progression, is no longer admissible evidence: that
construction freely prescribes a spiky, residue-dependent \(V\) and does not
satisfy (R83.0).  It is therefore withdrawn rather than treated as an
actual-symbol counterexample.

## 3. Proof or derivation

For fixed \(b\), expand
\[
 \left|\sum_{r\in\mathscr R_b}u(r)R(r)\right|^2
 =\sum_{r,s\in\mathscr R_b}u(r)\overline{u(s)}R(r)\overline{R(s)}.
\]
The map \((r,s)\mapsto(r,a=s-r\bmod q)\) is a bijection.  Its fibre
\(a=0\) is exactly \(r=s\) as a residue, and therefore contains all pairs of
original rows in the same progression.  Removing that fibre gives (83.5)
and (83.6).  Moreover
\(\mathfrak X_{b,-a}=\overline{\mathfrak X_{b,a}}\); pairing \(a\) and
\(-a\) is only a reindexing, not an extra saving.  The class \(a=q/2\), when
compatible, is self-paired and real.

Choose integer lifts of \(r\) and \(a\).  For every pair of progression
indices put
\[
 c_1=r+q\ell_1,\qquad c_2=r+a+q\ell_2,
\]
where the support indicators choose the unique allowed lifts, including the
one-count endpoints.  This convention automatically absorbs wraparound into
\(\ell_2\).  Write
\[
 \begin{split}
 W_{b,a,\ell_1,\ell_2}(r):={}&
  \mathbf 1_{\rm exact\ support/admissibility}
  V_{b,c_1,k}^{(1/4)}\overline{V_{b,c_2,k}^{(1/4)}}\\
 &\times e\!\left(\pm A_{1/4,b}
       \left({1\over c_1}-{1\over c_2}\right)\right).             \tag{R83.4}
 \end{split}
\]
Since \(r(r+a)\) is a unit,
\[
 \bar r-\overline{r+a}
 \equiv {r+a-r\over r(r+a)}
 \equiv a\,\overline{r(r+a)}\pmod q,                              \tag{R83.5}
\]
which proves (83.11), including its sign.  Hence the opened layer is
\[
 \sum_{\ell_1,\ell_2}\sum_{\substack{r\bmod q\\(r(r+a),q)=1}}
 e_q\!\left(ka\overline{r(r+a)}\right)
 W_{b,a,\ell_1,\ell_2}(r).                                        \tag{R83.6}
\]
Any admissibility beyond the two unit conditions remains inside \(W\); it
must not be silently enlarged away.

The repaired value of \(A\) exposes an exact phase-conjugating subterm.  In
the odd class,
\[
 A_{1/4,b}=bX+\sqrt{kX}+{k\over4b}
            =:A_{0,b}+{k\over q}.                                 \tag{R83.6a}
\]
For \((c,q)=1\), additive reciprocity gives
\[
 e_q(k\bar c)=e\!\left({k\over qc}\right)e_c(-k\bar q).
\]
Consequently, if \(\Delta=c_1^{-1}-c_2^{-1}\), the negative orientation
satisfies the exact joint identity
\[
 e_q\!\left(k(\bar c_1-\bar c_2)\right)e(-A_{1/4,b}\Delta)
 =e(-A_{0,b}\Delta)
   e_{c_1}(-k\bar q) e_{c_2}(k\bar q),                             \tag{R83.6b}
\]
where each \(\bar q\) is taken modulo the displayed \(c_i\).  For the
positive orientation the continuous coefficient is
\(A_{0,b}+2k/q\) instead.  Thus one sign cancels the \(k/(qc)\) reciprocity
correction exactly, but it leaves two varying-modulus inverse phases.  This
is a joint-symbol identity, not cancellation of (R83.6).

The BV input is also inherited by the nonoscillatory amplitude in (R83.4):
for every fixed \((\ell_1,\ell_2)\), its supremum plus total variation in
the residue lift is \(O_\varepsilon(X^\varepsilon)\), after absorbing the
two support endpoints.  It does not remove the explicit oscillation in
(R83.6a)--(R83.6b).

Define the unnormalised finite Fourier transform and rational complete sum
by
\[
 \widehat W_{b,a,\ell_1,\ell_2}(d)
  =\sum_{r\bmod q}W_{b,a,\ell_1,\ell_2}(r)e_q(-dr),
\]
\[
 K_q(a,k;d)=
  \sum_{\substack{r\bmod q\\(r(r+a),q)=1}}
  e_q\!\left(ka\overline{r(r+a)}+dr\right),                       \tag{R83.7}
\]
and
\(\mathcal W_{b,a}(d)=\sum_{\ell_1,\ell_2}
\widehat W_{b,a,\ell_1,\ell_2}(d)\).  Finite Fourier inversion in (R83.6)
gives (R83.1).

This completion is exactly the product-Kloosterman representation in the
packet, not a new saving.  Direct comparison with (83.13) gives
\[
 K_q(a,k;d)=e_q(-da)\,\overline{\mathcal C_q(-d,a)}.               \tag{R83.8}
\]
Thus the second argument \(a=0\), not the new Fourier variable \(d=0\), is
the zero product-frequency and has already been removed.  The terms with
\(a\ne0,d=0\) are genuine survivors.  Inverting the transform in (R83.1)
returns (R83.6) verbatim, so completion followed by full inversion is
involutive and supplies no gain by itself.

The rational sums have unavoidable prime-power degeneracies.  Let \(p\) be
odd, \(\nu\ge2\), \(p\nmid k\alpha\), and take modulus \(p^\nu\) and the
nonzero offset \(a=p^{\nu-1}\alpha\).  Since multiplication by
\(p^{\nu-1}\) sees the denominator only modulo \(p\),
\[
 \begin{split}
 K_{p^\nu}(p^{\nu-1}\alpha,k;0)
 &=p^{\nu-1}\sum_{x\in\mathbb F_p^*}e_p(k\alpha x^{-2})\\
 &=p^{\nu-1}\{-1+\chi(k\alpha)\tau(\chi)\},                       \tag{R83.9}
 \end{split}
\]
where \(\chi\) is the quadratic character and
\(|\tau(\chi)|=p^{1/2}\).  In particular its magnitude lies between
\(p^{\nu-1}(p^{1/2}-1)\) and
\(p^{\nu-1}(p^{1/2}+1)\).  At the literal modulus \(q=4p^\nu\), choose
\(a=4p^{\nu-1}\alpha\).  Chinese remaindering contributes the harmless
two odd residues modulo \(4\) and changes \(k\alpha\) only by a unit, so the
same orders of magnitude hold.  For \(\nu=2\) and \(4\) these are
\(q^{3/4+o(1)}\) and \(q^{7/8+o(1)}\).  These calculations both retain the
exceptional gcd and disprove a uniform pointwise \(q^{1/2+\varepsilon}\)
claim.  They are consistent with, but do not prove, a gcd-sensitive model
bound of the shape
\[
 |K_q(a,k;d)|\ \lesssim\ q^{1/2+\varepsilon}(ak,d,q)^{1/2}.         \tag{R83.10}
\]
For nonzero fixed \(k\), summing the forced factor
\((a,q)^{1/2}\) over \(a\) has size at most \(q^{1+\varepsilon}\), so
the complete-sum arithmetic has the *capacity* for an aggregate
\(q^{-1/2}\) gain.  Because \(k\ne0\) is fixed, primes dividing \(k\)
contribute only a fixed gcd factor.  For every other odd prime the examples
(R83.9) remain literal, so fixed nonzero \(k\) removes the formerly noted
identically-one phase but does not remove the prime-power offset
degeneracies.  Those sparse degeneracies are a warning for the weighted
average, not a no-go for it.

The arbitrary phase-conjugating test is equally decisive about the required
weight information.  If
\(z_{a,k}(r)=e_q(ka\overline{r(r+a)})\) and one takes
\(W(r)=\overline{z_{a,k}(r)}\) on the compatible residues, then (R83.6)
equals their number and has no cancellation.  Parseval also gives
\[
 \sum_{d\bmod q}|K_q(a,k;d)|^2
 =q\#\{r\bmod q:(r(r+a),q)=1\},                                  \tag{R83.11}
\]
so a second- or fourth-moment estimate for the complete sums alone cannot
control a Fourier coefficient vector aligned with them.  This test still
rules out arbitrary-coefficient and coefficient-blind arguments, but
(R83.0) no longer permits one simply to choose that vector as the actual
weight.  Equations (R83.6a)--(R83.6b) show a genuine partial conjugation in
one orientation, so non-alignment also cannot be assumed from BV alone.  The
remaining task is to estimate this specific joint phase, including its
prime-power/gcd strata, rather than to compare it with arbitrary bounded
coefficients.

Finally, the factor ledger is exact.  From (83.4), one fixed compatible
offset costs, after summing \(b\),
\[
 B\cdot B\cdot(TQ^{-5/24})^2=C^2Q^{-5/12}.
\]
There are \(O(B)\) compatible offsets, giving
\(C^2BQ^{-5/12}=C^3/(TQ^{5/12})\).  A gain \(B^{-\delta}\) changes this to
(R83.2).  Writing \(C=J^c\), comparison with \(J^2/T=J^{7/5}\) gives
\[
 (3-\delta)c\le {13\over6}-{3\delta\over5},
 \qquad
 c\le {13/6-3\delta/5\over3-\delta}.                              \tag{R83.12}
\]
Thus \(\delta=1/2\) reaches \(c=56/75\), while \(\delta=5/9\) is needed
to reach \(c=3/4\).

## 4. First doubtful or unproved step

The first unproved step is any passage from cancellation in
\(K_q(a,k;d)\) to a saving in (R83.1).  The repaired packet now provides
enough data to formulate that passage honestly: BV permits partial summation
in the amplitude, while \(A_b\asymp bX\) fixes the oscillatory scales.  What
is still missing is a quantitative bound showing that the resulting actual
vector \(\mathcal W_{b,a}(d)\) is sufficiently non-correlated with the
exceptional large values of \(K_q(a,k;d)\), uniformly after summing
\(b,a,\ell_1,\ell_2,d\).  The reciprocal part of (R83.4) is
\[
 e\!\left(\pm A_b{h\over c_1c_2}\right),
 \qquad h=c_2-c_1=a+q(\ell_2-\ell_1),                              \tag{R83.13}
\]
and, on \(c_1,c_2\asymp C\), its first and second derivatives in the residue
lift have scales
\[
 |\phi'(r)|\asymp {J^2|h|\over TC^2},\qquad
 |\phi''(r)|\asymp {J^2|h|\over TC^3},\qquad
 q|\phi''(r)|\asymp {J^2|h|\over T^2C^2}.                         \tag{R83.14}
\]
Thus small \(|h|\) can have weak curvature, while large and wraparound
separations cross many integer-frequency resonances.  In particular, BV
does not by itself imply a small Fourier algebra norm for the exponential
factor.  Conversely, (R83.6b) shows that the arithmetic and continuous
phases are not independent.  A joint oscillatory estimate, rather than a
missing-input objection, is now the exact seam.

Using only (83.4) after opening is invalid: (83.4) controls the already
summed progression \(R(r)\), whereas (R83.1) separates it into
\(\asymp T^2\) row pairs.  Triangle inequality at that point can lose the
very \(Q^{-5/12}\) cancellation that the desired estimate must preserve.
This is the exact seam at which the derivation stops.

## 5. Required control tests and outcomes

| Control | Test and outcome |
|---|---|
| Target and factor-\(B\) ledger | **Pass.** One offset gives \(C^2Q^{-5/12}\); \(O(B)\) offsets give (83.8); (R83.12) reproduces (83.10), \(56/75\), and \(3/4\). |
| Fixed nonzero \(k\), exact \(A\), and global BV | **Pass as inputs; estimate open.** The former \(k=0\) objection and unrestricted-symbol model are withdrawn.  Equations (R83.0), (R83.6a), and (R83.14) record the repaired data and their oscillatory consequences. |
| Offset one-count and \(a=0\) | **Pass.** Ordered pairs give one unique residue offset.  The entire same-residue energy is removed once.  Incompatible/empty layers, including odd \(a\) in the odd unit class, are zero through \(\mathcal A_b\) and are not reintroduced. |
| Odd inverse-unit identity | **Pass.** Equation (R83.5) verifies the exact sign and the two required unit conditions. |
| Both even units and aliases | **Not auditable.** Their formulas are absent from both permitted files.  No odd result can be promoted as an all-class result. |
| Dependence of \(R\) on offset and reciprocal phase | **Pass as an exact reduction; estimate open.** Equations (R83.4), (R83.6b), and (R83.13) retain \(a\), the full difference \(h\), both progression indices, amplitudes, supports, and reciprocal phase. |
| Rational sums, gcds, exceptional residues, zero modes | **Pass.** Equations (R83.7)--(R83.10) retain \(r=0,-a\) exclusions and exhibit the forced gcd losses.  The only product zero-mode is \(a=0\); \(d=0,a\ne0\) is retained. |
| Small, large, and wraparound offsets | **Pass.** Symmetric offsets \(a\) and \(-a\) are conjugate ordered layers.  Wraparound is absorbed uniquely into \(\ell_2\).  The true row separation is \(h=a+q(\ell_2-\ell_1)\), so no estimate replaces it by the residue lift \(a\). |
| Perfect-square and fourth-power moduli | **Fail for a coefficient-free pointwise square-root claim, but not a no-go.** Formula (R83.9) gives \(q^{3/4}\) and \(q^{7/8}\) at \(q=4p^2\) and \(q=4p^4\) for primes \(p\nmid k\).  Fixed nonzero \(k\) leaves these controls intact; a gcd-sensitive actual-weight average remains possible. |
| Phase-conjugating and moment controls | **Arbitrary test excluded as an actual model; joint estimate open.** The BV hypothesis prevents freely prescribing the conjugating coefficient vector.  Nevertheless, (R83.6b) gives an exact partial reciprocity cancellation in one orientation, and (R83.11) shows why complete-sum moments alone still do not establish the needed non-correlation. |
| Complete transforms versus self-return | **Pass.** Equation (R83.8) identifies the product kernel, and exact Fourier inversion returns (R83.6) with all supports and lower terms. |
| Current primary-source hypotheses | **No theorem invoked.** The brief forbids web and source-card reading.  Therefore no literature result is claimed at the literal composite modulus or actual lengths, and no source-dependent promotion is possible. |
| Transition, axes, and downstream scope | **Pass.** Transition remainders and axes remain excluded.  Nothing here is asserted for even classes, cone edges, other sectors, full M9-M1, M9, or the Gauss-circle exponent. |

Every fixed nonzero offset is target-safe by (83.7), but this does not permit
discarding the growing union of all such offsets: summing their individual
bounds is exactly the factor-\(B\) loss.  No nonzero offset is silently
removed in (R83.1).  A bounded, explicitly chosen collection could be paid
for separately without changing the strict survivor, but no such arbitrary
choice is needed here.

## 6. Dependencies and exact artifacts used

Only the following two permitted artifacts were used:

1. `rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/derivation_packet.md`;
2. `rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/briefs/blind_offset_dispersion_rederivation.md`.

No proof graph, strategy file, earlier or sibling report, source card, web
source, or numerical computation was read or used.  The finite-field and
prime-power controls in (R83.9) were derived directly.

## 7. Recommended state effect

**Recommended state effect: revise.**  Withdraw the former statement-level
no-go, the \(k=0\) objection, and the unrestricted-weight countermodel.
Retain (83.5)--(83.6), the exact odd identity, the prime-power/gcd controls,
and \(\mathfrak D_{\rm act}^{\rm odd}\) in (R83.1) as the first strict
survivor.  Do not promote any \(B^{-\delta}\) gain.  A next attempt should
prove a gcd-sensitive estimate for the explicit joint phase
(R83.6b)--(R83.14), summed over all row separations while preserving the
\(Q^{-5/12}\) saving, and derive the even-class and alias units separately.
