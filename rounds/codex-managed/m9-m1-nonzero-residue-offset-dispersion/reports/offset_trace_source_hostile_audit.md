# Round 83 offset trace/source hostile audit

## 1. Result

**Source-audited rank-one no-go; no current-source \(B\)-saving is
certified.**  At the literal Round-83 parameters, none of the audited
primary theorems for finite-field trace correlations, products of
Kloosterman sums, incomplete inverse sums, Kloosterman fractions, or
varying-modulus dispersion applies to the all-class signed correlation

\[
 \mathfrak X_C^{(\kappa,k)}
 =\sum_{b\asymp B}\sum_{a\ne0\ (4b)}\mathfrak X_{b,a}
\]

with its actual joint row weight.  In particular, no fixed gain
\(B^{-\delta}\), \(\delta>0\), over (83.8) follows from a quoted theorem.

There is also an exact algebraic obstruction to any coefficient-blind
offset argument.  For every \(b\), put
\(z_r=u_{\kappa,b,k}(r)R_{\kappa,b,k}(r)\).  Residue-offset one-count gives

\[
 \sum_{a\ne0\ (4b)}\mathfrak X_{b,a}
 =\sum_{r\ne s}z_r\overline{z_s}
 =\left|\sum_rz_r\right|^2-\sum_r|z_r|^2.       \tag{1.1}
\]

Thus the all-offset carrier is exactly the original rank-one off-diagonal
form.  The pointwise row estimate alone permits the hostile test
\(R(r)=\overline{u(r)}w\), for which (1.1) is
\(n_b(n_b-1)|w|^2\), \(n_b=|\mathscr R_{\kappa,b}|\).  This is not asserted
to arise from the actual reciprocal row (83.3); it proves that a gain must
use that row's joint archimedean and nonarchimedean structure and cannot be
deduced from an arbitrary-coefficient trace estimate.

Even in the optimistic unweighted squarefree-odd model, complete rational
trace bounds produce at most square-root cancellation in the \(O(B)\)
offsets, corresponding to \(\delta=1/2\).  That reaches
\(C\leq J^{56/75}\), not the full \(C\leq J^{3/4}\), which needs
\(\delta=5/9\).  Once the actual weight is restored, ordinary Fourier
completion loses this square-root gain completely.  The exact even-class
units are asserted to exist in the packet but are not displayed in the
selected context, so no cited source has an all-class literal map.

## 2. Exact statement and hypotheses

The audit uses exactly

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
 B=C/T,\qquad J^{13/18}<C\leq J^{3/4},            \tag{2.1}
\]

and \(q=4b\asymp B\).  The component, local class
\(\kappa\in\{1/4,1/2,1\}\), alias, and orientation are fixed.  The integer
\(k=\rho\sigma=O(1)\) is fixed, compatible, nonzero, and nonaxial.  The
actual row is

\[
 R(r)=\sum_{\substack{c\asymp C\\c\equiv r\ (4b)}}
 V_{b,c,k}^{(\kappa)}e\!\left(\pm {A_{\kappa,b}\over c}\right),
 \qquad
 A_{\kappa,b}=
 \left(\sqrt{bX}+\sqrt{\kappa k/b}\right)^2\asymp bX,       \tag{2.2}
\]

with

\[
 \|V\|_\infty+\operatorname {Var}_{[C,2C]}V
 \ll_\varepsilon X^\varepsilon,qquad
 |R(r)|\ll_\varepsilon X^\varepsilon TQ^{-5/24}.            \tag{2.3}
\]

No \(k=0\) case is used, and neither \(A_{\kappa,b}\) nor \(V\) is treated
as undefined.  The admissible residue set retains every parity and gcd
condition.  The local factors \(u(r)\) have modulus one and are constant on
their progressions.  In the odd class,

\[
 u(r)\overline{u(r+a)}
 =e_q\!\left(k(\bar r-\overline{r+a})\right)
 =e_q\!\left(ka\,\overline{r(r+a)}\right),          \tag{2.4}
\]

for \((r(r+a),q)=1\).  The selected packet does not state the corresponding
two even formulas, so they remain abstract exact local units in this audit.

The rigorous no-go statement is relative to (2.1)--(2.4): (i) the accepted
pointwise/BV data do not imply a power saving by a coefficient-blind trace
theorem; (ii) every audited source fails at least one literal hypothesis
before giving such a saving; and (iii) no smaller signed correlation is
created merely by the offset or product-Kloosterman transforms.

The smallest exact new signed input still required is an **actual-row
weighted offset-dispersion theorem**: for some fixed \(\delta>0\), uniformly
for every class, alias, orientation, and transformed error required by the
implication,

\[
 \left|\sum_{b\asymp B}\left{
 \left|\sum_{r\in\mathscr R_{\kappa,b}}u(r)R(r)\right|^2
 -\sum_{r\in\mathscr R_{\kappa,b}}|R(r)|^2\right}\right|
 \ll_\varepsilon
 X^\varepsilon B^{-\delta}{C^3\over TQ^{5/12}}.       \tag{2.5}
\]

Here \(R\) must be the row (2.2), not an arbitrary bounded sequence.  Any
\(\delta>0\) gives a genuine extension, with endpoint

\[
 C\leq J^{(13/6-3\delta/5)/(3-\delta)};             \tag{2.6}
\]

\(\delta=1/2\) gives \(56/75\), and \(\delta\geq5/9\) is required to close
the frozen band.  Transition remainders, axes, cone edges, other radial
sectors, and \(C>J^{3/4}\) are outside the statement.

## 3. Proof or derivation

**Target and factor-\(B\) ledger.**  The absolute offset estimate divided by
the target is

\[
 {C^3/(TQ^{5/12})\over J^2/T}
 ={C^3\over J^{13/6}}.                              \tag{3.1}
\]

It equals \(1\) at \(C=J^{13/18}\) and \(J^{1/12}\) at
\(C=J^{3/4}\).  At the upper endpoint \(B=J^{3/20}\), so precisely
\(B^{-5/9}=J^{-1/12}\) is needed.  This verifies the packet's endpoint
map and shows why square-root offset cancellation is short by
\(J^{1/120}\) at the upper endpoint.

**Residue one-count and the rank-one return.**  For each ordered pair
\((r,s)\), \(r\ne s\), there is exactly one class \(a=s-r\pmod q\).  Hence

\[
 \sum_{a\ne0\ (q)}\sum_{\substack{r\in\mathscr R\\r+a\in\mathscr R}}
 u(r)\overline{u(r+a)}R(r)\overline{R(r+a)}
 =\sum_{r\ne s}z_r\overline{z_s},                  \tag{3.2}
\]

which proves (1.1).  The diagonal \(a=0\) is subtracted exactly once.
Matrix-theoretically the kernel is \(uu^*-I\): it has a large positive
self-return direction \(\overline u\), not \(q\) independent oscillatory
directions.  This proves the phase-conjugating control and also proves that
summing a completed estimate over all offsets without using the actual
row cannot be a genuine reduction.

The opposite unweighted control is also exact in the odd class.  Since
inversion permutes \(U_q=(\mathbb Z/q\mathbb Z)^\times\),

\[
 \sum_{a\ne0\ (q)}\sum_{\substack{r\in U_q\\r+a\in U_q}}
 e_q\!\left(ka\overline{r(r+a)}\right)
 =\left|\sum_{r\in U_q}e_q(k\bar r)\right|^2-\phi(q)
 =|c_q(k)|^2-\phi(q).                              \tag{3.3}
\]

Thus the naked unit has real cancellation, but (3.2) shows that arbitrary
row phases can erase it.  This pair of controls is why neither a positive
heuristic nor an arbitrary-coefficient theorem is enough.

**Prime-local trace and gcd degeneracies.**  At an odd prime
\(p\nmid2ak\), completion of a fixed odd offset leads to

\[
 T_p(a,h)=\sum_{r\ne0,-a}
 e_p\!\left({ka\over r(r+a)}+hr\right).             \tag{3.4}
\]

The rational function has two simple poles, so the elementary
Weil--Deligne trace bound gives \(T_p(a,h)\ll\sqrt p\), uniformly in \(h\).
If \(p\mid a\) or \(p\mid k\), however, the inverse phase is constant modulo
\(p\); in particular \(T_p(a,0)=p-1\) in the reduced local model.  Thus
the exceptional locus is not optional.  On a squarefree odd modulus, an
optimistic CRT bound is only

\[
 |T_q(a,h)|\ll_\varepsilon
 q^{1/2+\varepsilon}(ak,q)^{1/2}.                   \tag{3.5}
\]

For fixed nonzero \(k\), divisor summation gives

\[
 \sum_{a\bmod q}|T_q(a,h)|\ll_{k,\varepsilon}q^{3/2+\varepsilon},
                                                               \tag{3.6}
\]

only a \(q^{-1/2}\) gain over \(q^2\).  Formula (3.5) is deliberately an
optimistic squarefree-odd model, not a claimed uniform theorem for
\(q=4b\).  The literal moduli have a 2-part and unrestricted repeated odd
prime factors.  Primes dividing \(k\) form a fixed set, but their powers in
\(q\) are not bounded; primes dividing \(a\) occur for a positive fraction
of offsets and cannot all be discarded.

**Small, large, and wraparound offsets.**  Offsets are group elements,
not canonically small integers.  Directly from (83.6),

\[
 \mathfrak X_{b,-a}=\overline{\mathfrak X_{b,a}},    \tag{3.7}
\]

so pairing \(a\) with \(q-a\) only makes the total real.  In the odd class
admissibility forces \(a\) even.  The self-inverse wrap offset
\(a=q/2=2b\) is maximally degenerate: for every admissible \(r\), the inverse
of \(r(r+a)\) modulo \(q\) is odd, and therefore

\[
 e_q\!\left(ka\overline{r(r+a)}\right)=(-1)^k.      \tag{3.8}
\]

It has no odd-class arithmetic oscillation.  It is nevertheless only one
selected offset per \(b\), and (2.3) gives

\[
 \sum_{b\asymp B}|\mathfrak X_{b,q/2}|
 \ll_\varepsilon X^\varepsilon B^2T^2Q^{-5/12}
 =X^\varepsilon C^2Q^{-5/12}
 \ll X^\varepsilon J^2/T.                         \tag{3.9}
\]

Hence it may be isolated safely, but a generic trace theorem that silently
includes it is false.  The even analogues cannot be tested without their
explicit local units.  Nor does a small representative \(a\) make the
actual archimedean phase slowly varying: already a unit change of residue
has phase-frequency scale \(A_b/C^2\), and the two progression indices in
(83.12) are independent.

**Completion and involutive self-return.**  The exact product transform is

\[
 {1\over q}\sum_{n\bmod q}S(n+d,k;q)\overline{S(n,k;q)}e_q(-tn)
 =\sum_{\substack{y\bmod q\\(y(y+t),q)=1}}
 e_q\!\left(d(y+t)+k(\overline{y+t}-\bar y)\right). \tag{3.10}
\]

At \(t=0\) this is \(c_q(d)\), the same-residue frequency already removed.
Fourier inversion of (3.10) returns (2.4); it contributes no saving by
itself.

More quantitatively, fix \(a\) and write
\(W_a(r)=R(r)\overline{R(r+a)}\) and

\[
 \widehat W_a(h)=q^{-1}\sum_rW_a(r)e_q(-hr).
\]

Even granting a uniform square-root bound for every complete additive
twist of the arithmetic kernel, completion gives only

\[
 \left|\sum_rK_a(r)W_a(r)\right|
 \ll \sqrt q\sum_h|\widehat W_a(h)|
 \leq \sqrt q\left(\sum_r|W_a(r)|^2\right)^{1/2}
 \ll q\,\|R\|_\infty^2,                           \tag{3.11}
\]

which is the trivial fixed-offset size.  A Fourier \(L^1\), sparsity, or
correlation estimate for \(W_a\) is required and is not implied by (2.3).
Completing also in \(a\) returns (3.2).

The missing regularity cannot be supplied by declaring the row smooth in
the residue.  At the literal scale,

\[
 q{A_b\over C^2}\asymp {J^2\over T^2}=Q^2\gg q\asymp B.      \tag{3.12}
\]

Thus the reciprocal row aliases across the full residue spectrum; it is
not a low-bandwidth coefficient.  Stationary completion leads back to
dual frequencies of size \(Q^2\) and to the product-Kloosterman
self-return.

**Literal primary-source maps.**  The following are failures of theorem
hypotheses, not analogical judgments.

| Source route | Literal hypothesis check and first mismatch |
|---|---|
| Fouvry--Kowalski--Michel, Corollary 1.6 | Gives \(O(\sqrt p)\) for products of bounded-conductor bountiful trace functions over the prime field \(\mathbb F_p\), subject to the normal-tuple/nonzero-twist alternatives.  Here \(q=4b\) is an arbitrary composite ring modulus, its prime-power degeneracies vary, and \(W_a\) is an \(X\)-dependent joint row weight rather than a bounded-conductor trace function. |
| Milićević--Zhang, Theorem 4 | Treats complete products to \(p^n\) for one fixed odd prime \(p\), with a bounded shift pattern, and explicitly allows power alignment of exceptional shifts.  The family \(4b\) is neither fixed-prime depth aspect nor odd, and the theorem does not accept \(W_a\). |
| Milićević--Qin--Wu, Theorem 1.1 | For arbitrary \(q\), bounds one normalized \(\mathrm{Kl}_2(cmn;q)\) with separated sequences and \(1\le M\le Nq^{1/4}\), \(M^{7/5}N<q^{3/2}\), \(MN\le q^{5/4}\).  Its factor is \(M^{-1/2}q^{1/6}+M^{-3/25}N^{-3/10}q^{1/5}+(MN)^{-3/16}q^{11/64}\).  A fixed-column specialization \(M=1,N=q\) is dominated by \(q^{1/6}\), and the Round-83 kernel is a product/correlation with a joint weight, not one Kloosterman sum. |
| Pascadi; Blomer--Pascadi | Their strongest current fixed-modulus bilinear theorems concern one Kloosterman kernel and two separated variables.  The legal compressed map has a full residue interval and a singleton and gives no saving; Pascadi's varying-modulus corollary has only the common divisor \(4\).  Neither source turns \(S(n_1,k;4b)\overline{S(n_2,k;4b)}\) with its joint symbol into the single kernel in its theorem. |
| Bettin--Chandee, Theorem 1 and Remark 1 | The naked odd fraction maps to \(m=c\asymp C\), \(n=4b\asymp B\), \(A_{\rm src}=1\), \(\vartheta=k\), but coefficients must separate.  Since \(C\gg B\), the theorem's first term is already larger than its coefficient-normalized trivial size by \(C^{1/10}B^{-3/20}>1\).  For the permitted joint phase \(f(c,4b)=\pm A_{\kappa,b}/c\), the derivative conditions force \(X_{\rm src}\asymp B^2J^2\), hence the stated penalty is \((1+X_{\rm src}/(CB))^{1/2}\asymp(J^2/T)^{1/2}=J^{7/10}\).  The BV hypothesis gives no separation or variation control in \(b\). |
| Wright, Theorem 2.1 and dispersion corollaries | The direct orientation of \(B(M,N,A;R)\) has \(M=C,N=B,R=4\) and violates \(M\ll N^2\), since \(C/B^2=T/B\gg1\).  Reciprocity gives the legal size orientation \(M=B,N=C\), but introduces exactly the nonseparable phase \(e(\pm A_b/c+k/(4bc))\) and the joint \(V_{b,c}\), which the theorem does not admit.  The convolution corollaries additionally require divisor-bounded separated coefficients and a Siegel--Walfisz sequence. |
| Bourgain--Garaev, Theorems 3 and 5 | Theorem 5 is a pure unweighted incomplete inverse sum and gives only a logarithmic relative saving for \(N>q^c\); Theorem 3 is an independent rectangle with separated bounded coefficients and phase \(e_q(a\bar x_1\bar x_2)\).  The constraint \(s=r+a\), exceptional residues, and \(R(r)\overline{R(r+a)}\) are not accepted. |
| Shen | The short inverse exponent-pair input requires a squarefree modulus with suitably small/factorable prime divisors.  No literal \(q=4b\) is squarefree, \(b\) is unrestricted, and the source estimates a pure inverse interval, not (83.12). |
| Blomer--Milićević | Gives cancellation for a single Kloosterman sum over varying moduli/residue classes with a smooth archimedean test.  It is not a theorem for a varying-modulus product kernel or the actual offset symbol. |
| Mohammadi | Treats separated coordinate boxes in a finite field \(\mathbb F_{p^n}\) for \(\psi(axy+b(xy)^{-1})\).  The ring \(\mathbb Z/(4b)\mathbb Z\), its affine constraint, and the joint row weight are outside the theorem. |
| Dong--Robles--Zeindler | arXiv:2601.00292v2 is withdrawn: the authors report a missing \(L^2\) factor in (2.53), so the claimed improved bound no longer follows.  It cannot be used. |

**Perfect-power controls.**  There are \(O(B^{1/2})\) perfect-square
\(b\)'s and \(O(B^{1/4})\) perfect fourth powers in a dyadic block.  Trivial
isolation therefore gains only \(B^{-1/2}\) for squares, which is
insufficient at \(C=J^{3/4}\), while fourth powers gain \(B^{-3/4}\) and
are safe.  This does not reduce the problem to squarefree moduli: \(q\)
always contains \(4\), and nonsquarefree \(b\)'s have positive density.
Hence arbitrary composite and prime-power degeneracies cannot be put into
a sufficiently sparse exceptional family.

Combining (3.2), (3.11), (3.12), and the literal source failures proves the
stated source-audited no-go.  No computation is used as certification.

## 4. First doubtful or unproved step

The first unproved analytic step in the odd class is the replacement

\[
 W_a(r)=R_{b}(r)\overline{R_b(r+a)}
 \quad\rightsquigarrow\quad
 \text{an admissible smooth, sparse, trace, or separated coefficient}. \tag{4.1}
\]

Neither the pointwise bound for \(R\) nor bounded variation of \(V\) in
the \(c\)-variable supplies a Fourier-\(L^1\) bound in \(r\), a tensor
decomposition uniform in \(b\), or cancellation after summing \(a\).
Equations (3.11)--(3.12) show that this is not a harmless technical
omission: the standard completion is trivial at the literal frequency.
Equation (3.2) shows that a second completion returns the original energy.

For an all-class claim there is an earlier source-certification seam: the
selected packet does not display the two even local-unit formulas, their
admissible residue sets in explicit arithmetic form, or a source kernel to
which they map.  This is not a claim that the even units do not exist; it
means that an odd trace estimate cannot be promoted by parity or sign
analogy.

Accordingly, (2.5) is the smallest exact signed input still required.  A
usable proof must exploit the actual \(A_{\kappa,b}\), the actual
\(V_{b,c,k}^{(\kappa)}\), and every local unit simultaneously, and must
carry the \(p\mid akq\), 2-adic, wraparound, support, and transform-error
terms.  A trace theorem uniform only for arbitrary bounded \(W_a\) cannot
have the needed conclusion because of the phase-conjugating direction in
(1.1).

## 5. Required control test and outcome

Here “pass” means that the hostile control was executed; it does not mean
that the target estimate was proved.

| Required control | Outcome |
|---|---|
| External normalization and factor-\(B\) ledger | **Pass.**  \(q=4b\asymp B\), there are \(O(B)\) offsets, (3.1) is exact, \(\delta=1/2\) reaches \(56/75\), and \(\delta=5/9\) closes \(3/4\). |
| Fixed nonzero nonaxial \(k\), \(A_{\kappa,b}\), and \(V\) | **Pass.**  The literal nonzero \(k\), \(A_{\kappa,b}\asymp bX\), and \(\|V\|_\infty+\operatorname{Var}V\ll X^\varepsilon\) were used; none is declared missing. |
| Residue-offset one-count and \(a=0\) | **Pass.**  (3.2) counts each ordered off-diagonal pair once and removes the diagonal once. |
| Odd inverse-unit identity | **Pass.**  (2.4), the Ramanujan control (3.3), and the local trace (3.4) were checked. |
| Both even units and aliases | **Not source-certified.**  They are accepted abstractly, but their explicit formulas are absent from the selected packet; no all-class theorem map can be checked. |
| Actual dependence of \(R(r)\) | **Fail for every audited black box.**  Completion gives (3.11), and the true frequency is (3.12).  Pointwise/BV data do not create the coefficient class required by a source. |
| Small, large, and wraparound offsets | **Pass as an obstruction audit.**  \(a\leftrightarrow-a\) only conjugates; the odd \(a=q/2\) phase is constant and was isolated target-safely in (3.9). |
| Gcd, zero, and exceptional modes | **Pass as an obstruction audit.**  \(a=0\) and product frequency \(t=0\) are removed once; \(p\mid a\) or \(p\mid k\) reduces the local conductor, and the varying 2-part remains outside prime-field sources. |
| Complete transforms and involution | **Pass.**  (3.10) is exact; inversion returns (2.4), Fourier completion returns the trivial bound, and all-offset completion returns (3.2). |
| Perfect squares and fourth powers | **Pass.**  Cardinality isolation gives respectively \(B^{-1/2}\) and \(B^{-3/4}\); only the latter is full-band safe, and neither controls positive-density nonsquarefree \(b\). |
| Phase-conjugating coefficients | **Pass.**  \(R=\bar u\,w\) saturates the positive rank-one direction allowed by coefficient-blind hypotheses; no claim is made that it is an actual row. |
| Current primary-source hypotheses | **Fail to apply.**  Every source in Section 3 misses the literal modulus family, product kernel, coefficient structure, length regime, smoothness, or all-class local data. |
| Transition/axis ownership and downstream scope | **Pass.**  No transition remainder, axis, cone edge, other radial sector, \(C>J^{3/4}\), full \(M9\!-M1\), \(M9\), or Gauss-circle conclusion is asserted. |

## 6. Dependencies and exact artifacts used

The selected project artifacts used were:

* `protocol.md`;
* `state/proof_obligations.yml`, restricted to the active \(M9\!-M1\)
  residue/transition obligations needed to identify the accepted starting
  point and scope;
* `state/active_campaign.yml`, Round 83 task
  `offset_trace_source_hostile_audit`;
* `rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/derivation_packet.md`,
  equations (83.1)--(83.14);
* `rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/reports/kloosterman_energy_source_hostile_audit.md`;
* `rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/reviews/conductor_round82_residue_normalization.md`;
* `rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/briefs/offset_trace_source_hostile_audit.md`.

No sibling Round-83 report was read.  The primary-source audit was current
on 16 August 2026 and checked the following exact versions:

* É. Fouvry, E. Kowalski, and Ph. Michel,
  [*A study in sums of products*, arXiv:1405.2293v2](https://arxiv.org/abs/1405.2293),
  revised 17 January 2015, especially Theorem 1.5 and Corollary 1.6
  (prime field, bountiful sheaf, bounded conductor, normal tuple or
  nonzero additive twist).
* Djordje Milićević and Sichen Zhang,
  [*Distribution of Kloosterman paths to high prime power moduli*, arXiv:2005.08865v1](https://arxiv.org/abs/2005.08865),
  submitted 18 May 2020, especially Theorem 4 (fixed odd prime,
  prime-power depth, complete products, shift collusion alternatives).
* Djordje Milićević, Xinhua Qin, and Xiaosheng Wu,
  [*Bilinear forms with Kloosterman sums and moments of twisted L-functions*, arXiv:2511.07550v1](https://arxiv.org/abs/2511.07550),
  submitted 10 November 2025, Theorem 1.1 (arbitrary modulus, one
  normalized Kloosterman kernel, separated sequences, three length
  inequalities).
* Alexandru Pascadi,
  [*Non-abelian amplification and bilinear forms with Kloosterman sums*, arXiv:2511.08445v2](https://arxiv.org/abs/2511.08445),
  revised 21 June 2026, Theorems 1.1 and 7.1 and Corollary 7.9
  (single kernel, fixed-modulus variables, factorization and
  common-divisor modulus-average hypotheses).
* Valentin Blomer and Alexandru Pascadi,
  [*Bilinear forms with Kloosterman sums via quadratic characters*, arXiv:2607.24311v1](https://arxiv.org/abs/2607.24311),
  submitted 27 July 2026, Theorems 1.1 and 5.5 (single fixed modulus,
  separated intervals, unbalanced specialization).
* Sandro Bettin and Vorrapan Chandee,
  [*Trilinear forms with Kloosterman fractions*, arXiv:1502.00769v1](https://arxiv.org/abs/1502.00769),
  submitted 3 February 2015, Advances in Mathematics 328 (2018),
  Theorem 1 and Remark 1 (three separated sequences and the explicit
  \(C^1\)-phase derivative penalty).
* Thomas Wright,
  [*Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions*, arXiv:2604.25177v2](https://arxiv.org/abs/2604.25177),
  revised 7 August 2026, Theorem 2.1, Corollary 2.2, and Theorem 2.3
  (partially fixed denominator, separated coefficients, size condition,
  and Siegel--Walfisz convolution input).
* J. Bourgain and M. Z. Garaev,
  [*Kloosterman sums in residue rings*, arXiv:1309.1124v1](https://arxiv.org/abs/1309.1124),
  submitted 4 September 2013, Theorems 3 and 5 (rectangular bilinear
  inverse fractions and pure incomplete inverse sums for general moduli).
* Qixiang Shen,
  [*A problem of D. H. Lehmer in short intervals. I*, arXiv:2607.07710v1](https://arxiv.org/abs/2607.07710),
  submitted 2 July 2026 (squarefree well-factorable modulus in the short
  inverse range).
* Valentin Blomer and Djordje Milićević,
  [*Kloosterman sums in residue classes*, arXiv:1410.4538v1](https://arxiv.org/abs/1410.4538),
  submitted 16 October 2014, JEMS 17 (2015), 51--69 (one Kloosterman sum
  over varying moduli with arithmetic residue weights).
* Ali Mohammadi,
  [*Bilinear Kloosterman sums over small boxes and uniformity of a random walk*, arXiv:2608.01203v1](https://arxiv.org/abs/2608.01203),
  submitted 2 August 2026 (finite-field coordinate boxes and separated
  weights).
* Anji Dong, Nicolas Robles, and Dirk Zeindler,
  [*Bilinear forms with Kloosterman fractions and applications*, arXiv:2601.00292v2](https://arxiv.org/abs/2601.00292),
  withdrawn 5 January 2026; the withdrawal notice identifies the missing
  \(L^2\) factor in equation (2.53).

## 7. Recommended state effect

**Retain** the Round-83 offset-dispersion obligation as open; do not
promote a conductor extension.  Record (1.1) as an exact actual-carrier
self-return/no-go and (3.8)--(3.9) as the odd wraparound seam that must be
isolated.  The source evidence supports neither arbitrary-coefficient
trace cancellation nor an all-class theorem map.

The next admissible promotion must prove (2.5) with the actual row and
explicit even local units.  Any fixed \(\delta>0\) may be promoted only to
the endpoint (2.6); a full-band promotion requires
\(\delta\geq5/9\).  No state effect is recommended outside the frozen
smooth-interior, nonaxial \(M9\!-M1\) component and
\(J^{13/18}<C\leq J^{3/4}\).
