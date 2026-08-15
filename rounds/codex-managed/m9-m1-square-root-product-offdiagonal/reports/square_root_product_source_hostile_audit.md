# Hostile/source audit of the square-root-product off-diagonal

## 1. Result

**No-go/source-inapplicability result.** No source-lawful proof of (68.2)
was found. The selected-context addendum does remove the former
packet-underdetermination objection: the actual coefficient has the exact
ratio form

\[
 P_k=\sum_{q\ {\rm odd}}\chi_4(q)C(k/q)e(\sqrt{Xkq}),
 \qquad C\in C_c^\infty((0,\infty)),
\tag{H68.1}
\]

on fixed positive ratio support. Phase-conjugating arbitrary symbols are
therefore excluded, and Mellin separation is lawful with a Schwartz mode
weight.

This improvement does not change the source or capacity verdict.
Robert--Sargos gives the optimal unsigned real root-spacing count, but after
the now-lawful Mellin separation its double-large-sieve lemma yields only

\[
 \mathcal O\ll_C Q^2X^{1/4+\varepsilon}.
\tag{H68.2}
\]

At \(Q=X^{1/5}\), this is worse than the trivial \(Q^3\) bound and is far
from \(Q^2X^\varepsilon\). The exact character product is constant on each
fixed difference shell, so it gives no within-shell cancellation. Its
cross-shell alternation merely shifts stationary aliases. More sharply,
successive B-processes in the half-difference and the remaining odd
\(q\)-variable restore exactly the reciprocal energy
\((k/J)|S_k|^2\) at stationary-main-term level. The Gaussian units cancel,
and the odd-lattice half-density is exactly what produces the factor
\(k/J\). This is an involutive return, not a new estimate. The elementary
near-diagonal and perfect-power controls remain target-safe, but the signed
union of all difference shells remains open.

## 2. Exact statement and hypotheses

Let \(e(z)=e^{2\pi iz}\), \(Q=X^{1/5}\) at the benchmark, and let \(k\) and
\(q\) run in fixed dyadic intervals of length \(\asymp Q\), restricted by a
fixed nonempty positive ratio support. The addendum gives

\[
 q=4r-\rho,\qquad \rho\in\{1,3\},
\]

\[
 c_\rho(k,r)=\left({k\over q}\right)^{3/4}
 \Xi\!\left(2\sqrt{k/q}\right),
 \qquad
 |(k\partial_k)^a(q\partial_q)^bC(k/q)|\ll_{a,b,C}1,
\tag{H68.3}
\]

up to one global branch unit and fixed smooth cutoffs. In the \(q\)-form,
the off-diagonal is

\[
 \mathcal O=
 \sum_{k\asymp Q}
 \sum_{\substack{q_1,q_2\asymp Q\\q_1,q_2\ {\rm odd}\\q_1\ne q_2}}
 \chi_4(q_1)\chi_4(q_2)
 C(k/q_1)\overline{C(k/q_2)}
 e\!\left(\sqrt{Xk}(\sqrt{q_1}-\sqrt{q_2})\right).
\tag{H68.4}
\]

Put

\[
 u_i={q_i\over4},\qquad
 \Delta=u_1-u_2={q_1-q_2\over4},\qquad
 \delta=\sqrt{u_1}-\sqrt{u_2}
 ={\Delta\over\sqrt{u_1}+\sqrt{u_2}}.
\tag{H68.5}
\]

The following assertions are proved under precisely these hypotheses.

1. The exact diagonal is
   \[
     \sum_{k,\ q\ {\rm odd}}|C(k/q)|^2\asymp_C Q^2
   \]
   on the accepted nonempty sector.
2. Every fixed nonzero half-integral \(\Delta\)-shell, including
   \(|\Delta|=1/2\) and \(|\Delta|=1\), contributes \(O_C(Q^2)\) by absolute
   counting. This does not permit summation over \(\asymp Q\) shells.
3. When \(X=L^2\), all exact product-square fibers \(kq=\square\) contain
   \(O(Q^{3/2+\varepsilon})\) off-diagonal energy pairs. The square-square
   and pure fourth-power subfibers have capacities \(O(Q^{3/2})\) and
   \(O(Q^{3/4})\), respectively.
4. Mellin inversion expresses the energy amplitude as an absolutely
   integrable superposition of separated modulus-one coefficients, making
   Robert--Sargos Lemma 8 applicable uniformly in the Mellin modes.
5. If \(q_1-q_2=2h\), then
   \[
     \chi_4(q_1)\chi_4(q_2)=(-1)^h.
\tag{H68.6}
   \]
   Thus the actual sign is constant on a difference shell and alternates
   only between adjacent half-integral shells.
6. Neither this separation nor the exact two-step stationary self-return
   supplies the lossless \(Q^2X^\varepsilon\) estimate. The latter restores
   \((k/J)|S_k|^2\), including the odd-lattice half-density.

## 3. Proof or derivation

Because \(q=4r-\rho\), one has \(u=q/4\),
\(q\equiv3\pmod4\) for \(\rho=1\), and \(q\equiv1\pmod4\) for
\(\rho=3\). The individual phase is exactly

\[
 2\sqrt{Xk(r-\rho/4)}=\sqrt{Xkq}.
\tag{H68.7}
\]

For equal residues a nonzero \(\Delta\) is an integer and has modulus at
least \(1\). For unequal residues it is a strict half-integer and has
modulus at least \(1/2\). Equality \(u_1=u_2\) across the two residues is
impossible. Hence phase zero occurs exactly when \(q_1=q_2\), giving the
diagonal in section 2. Once \(\Delta\) is fixed, \(q_1\) is determined by
\(q_2\); there are \(O(Q)\) pairs and \(O(Q)\) values of \(k\). Boundedness
of \(C\) proves the fixed-shell estimate.

For the perfect-power control take \(X=L^2\). Exact coherence occurs when
\(kq\) is a square. Write \(k=ab^2\), \(q=ac^2\), with \(a\) squarefree.
For fixed \(a\), the number of admissible \(k\)'s and \(q\)'s is
\(O((Q/a)^{1/2}+1)\). Therefore all coherent energy pairs number

\[
 \sum_{a\ll Q}O\!\left(((Q/a)^{1/2}+1)^3\right)
 \ll Q^{3/2}+Q\log Q
 =O(Q^{3/2+\varepsilon}).
\tag{H68.8}
\]

For odd \(q\), a fixed squarefree kernel fixes \(q\bmod4\), and
\(\chi_4(q)=\chi_4(a)\) throughout that fiber. Thus this control does not
silently use character cancellation. Taking \(a=1\) gives
\(Q^{1/2}(Q^{1/2})^2=Q^{3/2}\); restricting both variables to fourth
powers gives \(Q^{1/4}(Q^{1/4})^2=Q^{3/4}\).

The ratio symbol is genuinely separable. Define

\[
 \widetilde C(t)=\int_0^\infty C(y)y^{it}\,{dy\over y}.
\]

Then \(\widetilde C\) is Schwartz and

\[
 C(k/q)={1\over2\pi}\int_{\mathbb R}
 \widetilde C(t)k^{-it}q^{it}\,dt.
\tag{H68.9}
\]

Consequently,

\[
 C(k/q_1)\overline{C(k/q_2)}
 ={1\over(2\pi)^2}\iint_{\mathbb R^2}
 \widetilde C(t_1)\overline{\widetilde C(t_2)}
 k^{i(t_2-t_1)}q_1^{it_1}q_2^{-it_2}\,dt_1dt_2.
\tag{H68.10}
\]

The two Mellin weights have finite \(L^1\)-norm independent of \(X,Q\).
This repairs the old joint-symbol applicability objection, but creates no
cancellation by itself.

For the exact \(k\)-difference transform, set

\[
 f(t)=2\sqrt X\,\delta\sqrt t,\qquad
 f'(t)={\sqrt X\,\delta\over\sqrt t},\qquad
 f''(t)=-{\sqrt X\,\delta\over2t^{3/2}}.
\tag{H68.11}
\]

With
\[
 \sum_k A(k)e(f(k))
 =\sum_{n\in\mathbb Z}\int A(t)e(f(t)-nt)\,dt,
\]
a stationary point exists precisely when \(n\delta>0\) and

\[
 t_n={X\delta^2\over n^2}
\tag{H68.12}
\]

lies in the \(k\)-support. For support
\([\kappa_0Q,\kappa_1Q]\), the exact alias interval is

\[
 {\sqrt X|\delta|\over\sqrt{\kappa_1Q}}
 \le |n|\le
 {\sqrt X|\delta|\over\sqrt{\kappa_0Q}},
 \qquad
 \operatorname{sgn}n=\operatorname{sgn}\delta.
\tag{H68.13}
\]

At the saddle,

\[
 f(t_n)-nt_n={X\delta^2\over n},\qquad
 |f''(t_n)|={|n|^3\over2X\delta^2}.
\tag{H68.14}
\]

Thus an interior leading term is

\[
 e(-\operatorname{sgn}(\delta)/8)
 {\sqrt{2X}|\delta|\over |n|^{3/2}}
 A(t_n)e\!\left({X\delta^2\over n}\right).
\tag{H68.15}
\]

Since \(|\delta|\asymp|\Delta|/\sqrt Q\), the dual length and typical
weight are

\[
 N_\Delta\asymp{\sqrt X|\Delta|\over Q},
 \qquad
 {Q\over X^{1/4}|\Delta|^{1/2}}.
\tag{H68.16}
\]

At \(Q=X^{1/5}\), \(|\Delta|=1\), these are \(X^{3/10}\) and
\(X^{-1/20}\); their product is \(X^{1/4}>Q\). The B-process lengthens the
sum and needs new signed cancellation in \(n,q_1,q_2\). The addendum's
smooth ratio cutoffs and derivative bounds make this per-pair transform
lawful. Auxiliary dyadic-edge saddles and the accumulated transformation
errors must still be retained in a full fixed-interior ledger; smoothness
does not estimate the leading dual sum.

There is a stronger exact self-return at the energy level. Put
\(A=\sqrt{Xk}\), include the target-safe \(q\)-diagonal for the transform,
and write
\[
 q_1=q+2d,\qquad
 \chi_4(q_1)\chi_4(q)=(-1)^d=e(d/2).
\]
For fixed \(q\), the \(d\)-phase is
\[
 F_q(d)=A(\sqrt{q+2d}-\sqrt q)+{d\over2}.
\]
After ordinary Poisson summation in \(d\), let \(m\in\mathbb Z\) be the
dual alias and put \(j=2m-1\), which is odd. The stationary equation,
point, and phase are exactly
\[
 F_q'(d)=m,\qquad
 q_1^*=q+2d^*={4Xk\over j^2},
\]
\[
 F_q(d^*)-md^*
 ={Xk\over j}-\sqrt{Xkq}+{jq\over4}
 =\left(\sqrt{Xk/j}-{\sqrt{jq}\over2}\right)^2.
\tag{H68.17}
\]
Moreover,
\[
 |F_q''(d^*)|^{-1/2}
 ={2\sqrt2\,A\over j^{3/2}},\qquad
 C(k/q_1^*)=
 {j^{3/2}\over2\sqrt2\,X^{3/4}}\Xi(j/J).
\]
Their product is precisely
\[
 \left({k\over J}\right)^{1/2}\Xi(j/J).
\tag{H68.18}
\]
The first Gaussian unit is \(e(-1/8)\).

Now regard the phase in (H68.17) as
\[
 G_j(q)={Xk\over j}-A\sqrt q+{jq\over4}
\]
and apply Poisson summation on the odd \(q\)-lattice:
\[
 \sum_{q\ {\rm odd}}H(q)
 ={1\over2}\sum_{n\in\mathbb Z}(-1)^n
 \int_{\mathbb R}H(x)e(-nx/2)\,dx.
\tag{H68.19}
\]
Put \(s=j-2n\), again odd. The second stationary equation, point, and phase
are
\[
 G_j'(q^*)={n\over2},\qquad
 q^*={4Xk\over s^2},\qquad
 G_j(q^*)-{nq^*\over2}
 =Xk\left({1\over j}-{1\over s}\right).
\tag{H68.20}
\]
Here
\[
 |G_j''(q^*)|^{-1/2}
 ={4\sqrt2\,A\over s^{3/2}}.
\]
The half-density \(1/2\) in (H68.19) is essential: together with
\[
 \overline{C(k/q^*)}
 ={s^{3/2}\over2\sqrt2\,X^{3/4}}\,
 \overline{\Xi(s/J)}
\]
it gives exactly
\[
 {1\over2}|G_j''(q^*)|^{-1/2}\overline{C(k/q^*)}
 =\left({k\over J}\right)^{1/2}\overline{\Xi(s/J)},
\tag{H68.21}
\]
not twice that quantity. The second Gaussian unit is \(e(+1/8)\), cancelling
the first, and
\[
 (-1)^n=(-1)^{(j-s)/2}=\chi_4(j)\chi_4(s).
\]
Consequently the double-stationary main term is
\[
 {k\over J}
 \sum_{\substack{j,s\ {\rm odd}}}
 \chi_4(j)\chi_4(s)
 \Xi(j/J)\overline{\Xi(s/J)}
 e\!\left(kX\left({1\over j}-{1\over s}\right)\right),
\tag{H68.22}
\]
which is exactly \( (k/J)|S_k|^2\) with the inherited smooth support.
Thus two successive B-processes, including the actual character and every
normalizing density, reconstruct the reciprocal energy one started from.
They cannot by themselves prove a stronger estimate.

This exact assertion concerns the stationary main terms. A full asymptotic
identity must also retain nonstationary aliases, stationary points entering
the auxiliary smooth edges, and both accumulated saddle errors. The compact
ratio support makes the local integrations legitimate, but the addendum
does not supply a target-sized second-moment bound for their total. One must
transform the full \(d\)-sum and then subtract \(d=0\): deleting \(d=0\)
before Poisson creates a nonsmooth puncture. That diagonal subtraction is
\(O_C(Q^2)\), but no analogous deletion of the remaining error ledger is
licensed.

The shell sign also fails to give an elementary alternating-pair argument.
The derivative of the \(d\)-phase is
\[
 F_q'(d)={\sqrt{Xk}\over\sqrt{q+2d}}+{1\over2}\asymp\sqrt X.
\]
Across an active interval it crosses many integer aliases. The character
shifts the alias lattice by \(1/2\); it does not remove the stationary
aliases or furnish termwise pairing.

For the double-large-sieve audit normalize

\[
 x_k=\sqrt{k/Q},\qquad
 y_\ell={\delta\over\sqrt Q},\qquad
 \Lambda=2Q\sqrt X,
\tag{H68.23}
\]

so the phase is \(e(\Lambda x_ky_\ell)\).
Robert--Sargos Lemma 8 gives
\(\Lambda^{1/2}B_1^{1/2}B_2^{1/2}\) for separated coefficients. At spacing
\(1/\Lambda\),
\[
 |x_{k_1}-x_{k_2}|\asymp{|k_1-k_2|\over Q},
\]
so \(B_1\ll Q\). Their Theorem 2 with exponent \(1/2\), applied to the four
integer variables \(q_i=4r_i-\rho_i\), gives

\[
 B_2\ll_\varepsilon Q^{2+\varepsilon}
 +{Q^{4+\varepsilon}\over Q\sqrt X}
 =Q^{2+\varepsilon}+{Q^{3+\varepsilon}\over\sqrt X}
 \ll Q^{2+\varepsilon}
\tag{H68.24}
\]

for \(Q\le\sqrt X\). Restricting the \(q_i\) to odd residue classes only
reduces this unsigned count. For each Mellin-mode pair, the factors
\[
 k^{i(t_2-t_1)},\qquad
 \chi_4(q_1)\chi_4(q_2)q_1^{it_1}q_2^{-it_2}
\]
have modulus one, so Lemma 8 is uniform in \(t_1,t_2\). Integrating against
the two Schwartz mode weights costs \(O_C(1)\). Hence

\[
 \Lambda^{1/2}B_1^{1/2}B_2^{1/2}
 \ll_C Q^2X^{1/4+\varepsilon}.
\tag{H68.25}
\]

The remaining \(X^{1/4}\) is the exact double-large-sieve normalization,
not a spacing or symbol defect. The lemma uses absolute \(B_2\), so it
discards the actual character sign before it can help. Mellin separability
repairs applicability, not normalization.

The other named source routes still do not close (H68.4). Huxley's
Bombieri--Iwaniec architecture needs separately verified first and second
spacing problems for its Taylor vectors and rational minor arcs; it is not
a ready lossless theorem for this fixed-center signed energy. The restricted
monomial B-process in Robert--Sargos Section 3 assumes its phase scale lies
between \(M\) and \(M^2\); for \(|\Delta|=1\) at the benchmark the present
scale is \(\asymp\sqrt X>Q^2\). The general Poisson calculation above is
lawful, but returns a longer dual sum.

Jutila's ordinary B-process confirms the saddle equations but is a
transformation, not a lossless estimate. In the present degree-one
character setting, (H68.17) is the directly applicable summation formula
and it returns to the original reciprocal sum. Jutila's Voronoi/Hankel
transformations for \(d(n)\) or Fourier coefficients of a cusp form do not
add a second-moment theorem for this \(\chi_4\)-weighted square-root phase.
The Deshouillers--Iwaniec spectral large sieve acts on Kloosterman sums and
automorphic Fourier coefficients. The \(k\)-dual phase
\(e(X\delta^2/n)\) contains an ordinary real reciprocal \(1/n\), not a
modular inverse, modulus/coprimality condition, or complete Kloosterman
coefficient to which Kuznetsov can be applied.

## 4. First doubtful or unproved step

The addendum resolves the actual-symbol formula, quantitative slow-symbol
bounds, residue recombination, and Mellin separability. The first remaining
unproved step is cancellation across the union of nonzero
\(\Delta\)-blocks, equivalently across the stationary aliases. In the
\(k\)-dual form, the required leading estimate is

\[
 \sum_{\substack{q_1,q_2\asymp Q\\q_1,q_2\ {\rm odd}\\q_1\ne q_2}}
 \chi_4(q_1)\chi_4(q_2)
 \sum_{\substack{n\delta>0\\X\delta^2/n^2\asymp Q}}
 {\sqrt X|\delta|\over |n|^{3/2}}
 C(t_n/q_1)\overline{C(t_n/q_2)}
 e\!\left({X\delta^2\over n}\right)
 \ll Q^2X^\varepsilon,
\tag{H68.26}
\]

with the Gaussian unit, all fixed smooth cutoffs, accumulated error terms,
and stationary-edge transitions restored. The character is constant within
each fixed shell by (H68.6), while using its cross-shell alternation leads
to the two-step alias family (H68.17)--(H68.22). None of the audited sources states
(H68.26) or an equivalent lossless signed theorem.

## 5. Required control test and outcome

- **Actual symbol:** pass. The ratio formula, slow mixed derivatives, odd
  character recombination, and fixed positive ratio support are explicit.
  The former phase-conjugating countermodel is rejected and is no longer a
  valid objection.
- **Mellin separation:** pass as an applicability seam. Equations
  (H68.9)--(H68.10) give a Schwartz-weighted separated expansion with
  \(O_C(1)\) total mode mass. It does not improve the large-sieve
  normalization.
- **Difference algebra:** pass. The exact variable is \(q=4r-\rho\), the
  individual phase is \(\sqrt{Xkq}\), and
  \(\Delta=(q_1-q_2)/4\).
- **Diagonal:** pass. It is exactly
  \(\sum_{k,q\ {\rm odd}}|C(k/q)|^2\asymp_C Q^2\) on the accepted sector.
- **Cross residue:** pass. Distinct residues force
  \(|q_1-q_2|\ge2\), hence \(|\Delta|\ge1/2\), and no cross-residue exact
  diagonal exists.
- **Near diagonal:** pass. Each of \(|\Delta|=1/2,1\) has only \(O(Q^2)\)
  terms. This gives no estimate for the \(\asymp Q\) remaining shells.
- **Squares, fourth powers, product-square fibers:** pass as obstruction
  controls. Their capacities are \(Q^{3/2}\), \(Q^{3/4}\), and
  \(Q^{3/2+\varepsilon}\), all below target. The actual character is
  constant on each squarefree-kernel fiber, so this conclusion does not
  assume unavailable character cancellation.
- **Character shell sign:** pass algebraically; fail as a closure.
  \(\chi_4(q_1)\chi_4(q_2)=(-1)^{(q_1-q_2)/2}\), but this sign is constant
  within a shell. Across shells it shifts, rather than removes, the
  stationary aliases.
- **Poisson aliases and B-process normalization:** pass algebraically; fail
  as a closure. The exact \(k\)-aliases return \(e(X\delta^2/n)\) with a
  longer dual sum. The exact \(d\)-then-\(q\) stationary calculation returns
  \((k/J)|S_k|^2\): the two Gaussian units cancel, the odd-lattice
  half-density removes the apparent factor \(2\), and
  \((-1)^{(j-s)/2}=\chi_4(j)\chi_4(s)\). This verification is for the
  stationary main terms; all nonstationary, transition, and accumulated
  fixed-interior errors still require a summed ledger.
- **Unsigned spacing versus signed energy:** fail as a closure. The optimal
  Robert--Sargos count is applicable after Mellin separation but still
  gives only \(Q^2X^{1/4+\varepsilon}\), and absolute \(B_2\) cannot see
  (H68.6).
- **Source applicability:** fail at the target normalization. No audited
  Huxley, Jutila/Voronoi, spectral/Kuznetsov, or Hankel statement supplies
  the missing lossless signed second moment.
- **Scope:** pass. Nothing here is asserted for hard radial edges, the full
  cone, a radial interval, M9-M1, M9, or the final exponent.

No numerical experiment was used; all controls are exact or cardinality
arguments.

## 6. Dependencies and exact artifacts used

Local artifacts, and no other Round-68 reports:

1. rounds/codex-managed/m9-m1-square-root-product-offdiagonal/derivation_packet.md.
2. rounds/codex-managed/m9-m1-joint-reciprocal-large-sieve/reports/conductor_RSLS_source_hostile_audit.md.
3. rounds/codex-managed/m9-m1-square-root-product-offdiagonal/briefs/square_root_product_source_hostile_audit.md.
4. rounds/codex-managed/m9-m1-square-root-product-offdiagonal/actual_symbol_addendum.md.

Primary sources audited:

1. O. Robert and P. Sargos, *Three-dimensional exponential sums with
   monomials*, J. reine angew. Math. **591** (2006), 1--20, especially
   Theorem 2, Lemma 8, and Section 3:
   <https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf>.
2. M. Jutila, *Lectures on a Method in the Theory of Exponential Sums*,
   Tata Institute Lecture Notes 80 (1987), Introduction and Chapters 1--3:
   <https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr80.pdf>.
3. M. N. Huxley, *Area, Lattice Points, and Exponential Sums*, LMS
   Monographs 13 (1996), especially Chapters 13 and 16:
   <https://doi.org/10.1093/oso/9780198534662.001.0001>.
4. E. Bombieri and H. Iwaniec, *On the order of
   \(\zeta(1/2+it)\)*, Ann. Scuola Norm. Sup. Pisa **13** (1986), 449--472:
   <https://www.numdam.org/item/ASNSP_1986_4_13_3_449_0.pdf>.
5. J.-M. Deshouillers and H. Iwaniec, *Kloosterman sums and Fourier
   coefficients of cusp forms*, Invent. Math. **70** (1982), 219--288:
   <https://doi.org/10.1007/BF01390728>.

The discovery and blind-rederivation reports were not read.

## 7. Recommended state effect

**Retain.** Retain (68.2), the square-root-product energy target, GAR,
M9-M1, M9, and the exponent as open. Withdraw the earlier
packet-underdetermination objection: the addendum verifies the actual ratio
symbol, quantitative smoothness, character recombination, and lawful Mellin
separation. Retain the diagonal, fixed-shell count, perfect-power capacity,
Mellin decomposition, character-shell identity, and the exact
double-stationary \(k/J\) self-return as vetted evidence, with its endpoint
and error scope explicit. These do not promote the target. The next
admissible analytic objective is the signed alias estimate (H68.26), not
another unsigned spacing count or an uninstantiated spectral/Hankel
transformation.
