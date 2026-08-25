# Round 148 source-applicability seam review

## 1. Result

**Result: AMBER, with a repairable source/method no-go.**  The primary
theorem exponents, the reduced additive denominator, the small-denominator
divisor count, and the fixed-coefficient large-sieve ledger in
`squarefree_progression_source_audit.md` check out.  The central phase
diagnosis also checks out: none of the quoted progression, fixed-modulus
$K_2$-correlation, or Kloosterman-fraction statements has the literal
varying-$q$ interface

$$
 \sum_{q\asymp\lambda Q}\frac{\chi _4(q)}{\lambda}
 \sum_{d\asymp D}c_{d,\lambda,q}
 e\!\left(\frac{\lambda Nd}{q}\right),
 \qquad Q=D\sqrt{N/M},
 \tag{SR.1}
$$

with the actual coupled prefix/cone profile and its $q_1=q_2$ dispersion
diagonal.

Four seams must be repaired before the report is source-green.

1. Schlage--Puchta (148.28) is a valid **exact-reduced-denominator
   specialization**, but it is not the strongest consequence of Theorem 3.
   The theorem permits every approximating denominator, including multiples
   of $q_*$.  Thus the aggregation $D/\lambda+\lambda Q^2$ proves only
   that this specialization fails; it does not prove an exhaustive
   Schlage--Puchta no-go.
2. The Nunes theorem cards need two hypothesis clarifications: Theorems
   1.2--1.3 of the 2016 prime-modulus paper fix $a,b\in\mathbb F_p^\times$,
   and Lemma 1.3 of the least-squarefree paper is uniform for a unit residue
   $a\pmod q$ and any positive modulus $q$, not only for squarefree $q$.
3. Equations (148.30)--(148.31) apply when the inner coefficient $c_d$ is
   independent of $q$.  They are a separable spacing diagnostic, not an
   estimate for the literal $\Omega_{d,\lambda,U}(q)$-coupled sum.
4. The Round-147 $H$-interface mismatch also has a missing bandwidth
   obstruction: the reciprocal nearest-integer variable naturally has
   $|j|<q/2\asymp\lambda Q$, whereas the $H$-band has
   $|j_H|\lesssim k\sqrt{N/M}=\lambda Q/D$ after the formal choice
   $k=\lambda$.  Only a $D^{-1}$-thin part of the reciprocal $j$-range
   even lies in that band.

With these qualifications, the lawful conclusion is: **none of the quoted
theorems directly supplies (SR.1); a new coefficient-sensitive aggregation
or exact Euler recombination is still required.**  It is not lawful to say
that every possible use of Schlage--Puchta has been excluded.

## 2. Exact statement and source hypotheses

The source cards were checked against the cited primary versions.  The
outcome is as follows.

| Source statement | Seam outcome |
|---|---|
| Schlage--Puchta, Theorem 3 | **Exponent and approximation condition pass.**  The source states $\lvert \alpha r-a\rvert\le r^{-1}$ and $S_L(\alpha)\ll L^{1+\varepsilon}/r+rL^\varepsilon$.  It does not require that the displayed approximating pair be reduced.  Consequently $r=q_*$ is legal but is only one legal choice. |
| Nunes, *Squarefree numbers in large arithmetic progressions*, Theorem 1.1 | **Pass.**  Prime $p\le L^{13/19-\varepsilon}$, $(a,p)=1$, arbitrary fixed $A>0$, and error $L/[p(\log L)^A]$ are quoted correctly. |
| Same paper, Theorems 1.2--1.3 | **Exponents and size ranges pass; one hypothesis is omitted.**  The conditions $1\le A\le B^2$, $B<p$, $AB^2<p^2$ and $AB<p^{3/2}$, and the powers $-1/16$ and $-1/12$, are correct.  Add that the parameters defining $K_1,K_2$ satisfy $a,b\in\mathbb F_p^\times$. |
| Nunes, *A note on the least squarefree number...*, Theorem 1.1 | **Pass.**  The modulus is squarefree, $q\le L^{25/36-\varepsilon}$, $(a,q)=1$, and the error is $O(L^{1-\delta}/q)$. |
| Same paper, Lemma 1.3 | **Exponent pass; card is unnecessarily restrictive.**  The bound $A^{2/3}B^{1/4}q^\varepsilon$, $A\le q^{3/4}$, $B<q/2$, is correct.  The lemma itself assumes only a positive integer $q$ and $a\in(\mathbb Z/q\mathbb Z)^\times$; squarefreeness enters the main theorem, not the lemma. |
| Nunes, 2014, Theorems 1.1--1.2 | **Pass.**  The $L^{1/2}q^{1/2}$ main scale and errors $d(q)L^{1/3}q^{2/3}+L^{23/15}q^{-13/15}(\log L)^{15}$ are correct and uniform for $q\le L$.  The correlation error is $O_m(\cdots)$, so "fixed $m$" must remain explicit. |
| Mangerel, Theorem 1.1 | **Pass.**  The modulus is squarefree and $L^\eta$-smooth, $0<\eta<1/522$, $q\le L^{196/261-\varepsilon}$, $(a,q)\le L^\varepsilon$, with error $O_\varepsilon(L^{1-\delta}/q)$. |
| Mangerel, Theorem 3.1 and Remark 3.2 | **Pass.**  The fixed-prime $K_2$ correlation has size $(r+s)3^{r+s}p^{(r+s+1)/2}$, except when the additive character is trivial and the two multiplicities are congruent modulo $3$ at every shift.  Equal multiplicities give the nonnegative balanced case. |
| Bettin--Chandee, Theorems 1--2 | **Pass.**  The inverse phase, norm factor, conductor factor, exponents $7/20,3/8,1/4,1/8$ in Theorem 1 and $3/10,7/20,1/2,7/8$ in Theorem 2 are quoted correctly.  Theorem 2 includes odd coprime support.  The proof really separates $\ell_1n_1=\ell_2n_2$ from the off-diagonal. |

The exact one-sided transform used for matching also passes at the interface
needed here.  With $\lambda=[u^2,v]$, character Poisson has factor
$i\chi_4(\lambda)/(2\lambda)$; the positive saddle is
$y_0=4\lambda^2Nd/q^2$, its phase is $\lambda Nd/q$, and the leading
amplitude after the original $(dy)^{-3/4}$ weight is
$e(1/8)N^{-1/4}(d\lambda)^{-1}$.  Thus the source report is auditing the
right phase, $q$-length, and leading coefficient.

## 3. Proof and seam derivation

Put $K=\lambda N$.  Reducing the rational additive frequency gives

$$
 \frac Kq=\frac{K/(K,q)}{q/(K,q)},\qquad
 q_*:=\frac q{(q,K)},
 \tag{SR.2}
$$

so (148.5) is exact.  The numerator in (SR.2) is coprime to $q_*$, as
required when a progression theorem is invoked after residue-class
decomposition.

For the small-$q_*$ count, write $q=gr$, where
$g=(q,K)\mid K$ and $r=q_*\le Y$.  The map $q\mapsto(g,r)$ is
injective, hence, even before imposing $q\asymp\lambda Q$,

$$
 \#\{q:q_*\le Y\}\le Y\tau(K).
 \tag{SR.3}
$$

Moreover, since nonzero Mobius terms make $u,v$ squarefree and
$[u^2,v]=u^2v/(u,v)$, the absolute local factors are

$$
 1+p^{-2}\quad(p\nmid d_o),\qquad
 1+p^{-1}+2p^{-2}\quad(p\mid d_o).
 \tag{SR.4}
$$

Their product is $O(X^\varepsilon)$.  Combining (SR.3), (SR.4),
$D/d\asymp1$, and $\tau(\lambda N)\ll X^\varepsilon$ proves

$$
 \sum_{d,u,v}\frac Dd\frac1\lambda
 \#\{q\asymp\lambda Q:q_*\le Y\}
 \ll DY X^\varepsilon.
 \tag{SR.5}
$$

Thus the source report's small-denominator/DY aggregation is correct.  Since
$D\le\sqrt M\le R$, all three quoted progression ranges
$D^{13/19-\varepsilon}$, $D^{25/36-\varepsilon}$, and
$D^{196/261-\varepsilon}$ lie inside the target-safe range $Y\le R$.
Their prime, squarefree, or smooth hypotheses only shrink that already-safe
set.

For Schlage--Puchta, choosing the exact reduced pair in (SR.2) indeed gives

$$
 \sum_{d\asymp D}\mu^2(d)e(Kd/q)
 \ll D^{1+\varepsilon}/q_*+q_*D^\varepsilon.
 \tag{SR.6}
$$

In the coprime case $q_*=q\asymp\lambda Q$, summing (SR.6) with outer
weight $1/\lambda$ gives exactly

$$
 D/\lambda+\lambda Q^2
 \tag{SR.7}
$$

up to $X^\varepsilon$.  This arithmetic ledger is correct.  It is not,
however, an optimized use of the cited theorem.  If $q_*\le\sqrt D$, take
$t=\lceil\sqrt D/q_*\rceil$ and use the also-exact approximating pair
$(ta,tq_*)$.  Its denominator lies in $[\sqrt D,2\sqrt D]$, so the same
theorem gives $O(D^{1/2+\varepsilon})$.  If $q_*>\sqrt D$, the report has
not classified the other allowable Diophantine approximants.  Therefore
(SR.7) is a valid failure of the exact-denominator specialization, but it
cannot be advertised as an exhaustive failure of Schlage--Puchta.  No
quoted source theorem supplies the missing joint count of good
approximants as $q$ varies; that absence, rather than (SR.7) alone, is the
lawful source obstruction.

The large-sieve calculation is also algebraically correct in its stated
separable model.  Distinct values of $K/q\pmod1$, after reduction, are
separated by $\gg(\lambda Q)^{-2}$.  If a reduced residue $a/r\pmod1$
occurs, then $r=q_*$ and $q=gr$ for a divisor $g\mid K$, so its
multiplicity is at most $\tau(K)$.  The large sieve therefore gives

$$
 \sum_{q\asymp\lambda Q}
 \left|\sum_{d\asymp D}c_d e(Kd/q)\right|^2
 \ll X^\varepsilon(D+\lambda^2Q^2)\sum_d|c_d|^2.
 \tag{SR.8}
$$

For $|c_d|\le1$ and $\beta_q=\chi_4(q)/\lambda$, Cauchy has first factor
$(\lambda Q/\lambda^2)^{1/2}$ and second factor
$((D+\lambda^2Q^2)D)^{1/2}$.  Since $\lambda Q\ge RD$, this is

$$
 \ll X^\varepsilon\lambda^{1/2}Q^{3/2}D^{1/2},
 \tag{SR.9}
$$

and is worse than $QD$ by $(\lambda Q/D)^{1/2}\ge R^{1/2}$.  At
$(M,D)=(R^2,R)$, (SR.9) is $R^{3/2}$ above $RD$ for $\lambda=1$, as
claimed.  The needed qualification is that (SR.8) fixes one sequence $c_d$
for every $q$; the literal $c_{d,\lambda,q}$ contains
$\Omega_{d,\lambda,U}(q)$.  Hence (SR.8)--(SR.9) are a spacing-only
control, not a direct upper bound for (148.1).

The claimed phase mismatches survive scrutiny.  The Nunes--Mangerel
complete sums use one finite-field modulus and phase
$A\bar x^2+Bx$; Bettin--Chandee uses $a\bar m/n$.  The literal transform
is linear in $d$, reciprocal only in the varying outer integer $q$, and
dispersion produces

$$
 e\!\left(\lambda Nd(1/q_1-1/q_2)\right),
 \tag{SR.10}
$$

whose $q_1=q_2$ contribution is zero-phase.  Neither the fixed-modulus
variance diagonal, the balanced $K_2$ exception, nor the
$\ell_1n_1=\ell_2n_2$ Bettin--Chandee diagonal is this diagonal.  Turning
$d$ into a modular inverse would be a $q$-dependent permutation and
would lose the dyadic interval and the coupled profile.

Finally, the formal Round-147 substitution has two independent failures.
Writing

$$
 c=\left\lfloor\lambda N/q+\tfrac12\right\rfloor,
 \quad j=\lambda N-cq,
 \quad k=\lambda,
 \quad j_H=-j
 \tag{SR.11}
$$

does give $kN+j_H=cq$.  But $\lambda=[u^2,v]$ need not be powerful, so
there is no coefficient identity with $h_z(k)A_{-z}(kN+j_H)$.  In
addition, (SR.11) only gives $|j|<q/2\asymp\lambda Q$, while the actual
$H$-resonance band is

$$
 |j_H|\lesssim k\sqrt{N/M}=\lambda Q/D.
 \tag{SR.12}
$$

No argument in the source report discards or bounds the complementary
$j$-range.  Exact Euler recombination is therefore still necessary even
before a source theorem could be matched.

## 4. First doubtful or unproved step

The first substantive doubtful step is the change in scope between
(148.28) and the prose conclusion drawn from it.  Equation (148.28) is true
for the chosen denominator $q_*$, and its coprime aggregation is (SR.7),
but Schlage--Puchta's theorem is quantified over an approximating
denominator, not over the reduced denominator of the frequency.  Exact
multiples already improve the bound when $q_*\le\sqrt D$, and other
approximants for $q_*>\sqrt D$ were not audited.  The report may conclude
that the **exact-denominator pointwise route** fails and that the cited
paper contains no varying-$q$ aggregation theorem.  It may not conclude
from (148.28) alone that Schlage--Puchta admits no source-legal
reorganization capable of further saving.

The first missing arithmetic estimate remains the same after this repair:
a bound for the actual signed, $q$-coupled form (SR.1), or an exact Euler
recombination followed by a theorem for the Round-147 powerful-band
coefficient.  Nothing in this review proves that estimate or a lower bound
against it.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| primary_theorem_hypotheses_and_exponents | **AMBER.**  All numerical exponents and main size ranges pass.  Add $a,b\in\mathbb F_p^\times$ to Nunes Theorems 1.2--1.3 and state the unit-residue/general-modulus scope of Nunes Lemma 1.3. |
| one_sided_transform_phase_amplitude_and_q_length | **GREEN for source matching.**  The report uses the correct $e(1/8)N^{-1/4}(d\lambda)^{-1}$, phase $e(\lambda Nd/q)$, and $q\asymp\lambda Q$ interface. |
| reduced_denominator_q_star | **GREEN.**  Equation (SR.2) proves $q_*=q/(q,\lambda N)$. |
| small_q_star_DY_count | **GREEN.**  Equations (SR.3)--(SR.5) include the divisor multiplicity and full $u,v,1/\lambda$ aggregation. |
| progression_range_target_safety | **GREEN.**  Every quoted $D^\theta$ range has $\theta<1$ and lies inside $Y\le R$. |
| Schlage_Puchta_exact_denominator_aggregation | **Arithmetic GREEN; inference AMBER.**  $D/\lambda+\lambda Q^2$ is correct for that specialization.  The report must acknowledge exact multiples and other admissible approximants. |
| fixed_coefficient_large_sieve_ledger | **GREEN as a diagnostic.**  Separation, multiplicity, Cauchy factors, and the $R^{3/2}$ top loss pass.  Mark $c_d$ as $q$-independent and do not apply it to the coupled profile. |
| Nunes_Mangerel_phase_and_modulus_match | **GREEN no-match.**  Their progression and $K_2$ interfaces do not equal (SR.1) or (SR.10). |
| Bettin_Chandee_phase_and_diagonal_match | **GREEN no-match.**  The inverse phase and its amplified diagonal differ from the linear reciprocal phase and $q_1=q_2$ diagonal. |
| H_resonance_interface | **AMBER until bandwidth is added.**  Non-powerful $\lambda$ is correctly noted; add (SR.12) and the unowned complementary $j$-range. |
| arbitrary_outer_coefficient_falsifier | **GREEN with existing scope.**  It refutes only the arbitrary-coefficient analogue and does not test $\chi_4(q)$. |
| squarefree_absolute_QplusD_claim | **GREEN as open.**  The report neither proves nor refutes it. |
| all_scale_power_ledger | **GREEN after the large-sieve label repair.**  The displayed ratios are arithmetically correct and are capacities, not lower bounds. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

Repository artifacts used for this seam review:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reports/squarefree_progression_source_audit.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reports/signed_squarefree_reciprocal_attack.md`, used only to match the exact transformed phase, coefficient, reduced channel, and target;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/reports/t1_squarefree_voronoi_attack.md`, used only for the powerful support and resonance bandwidth in (SR.12);
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-voronoi-gate/synthesis.md`, used only to cross-check that same Round-147 interface.

Primary sources checked directly:

- Schlage--Puchta, [*The exponential sum over squarefree integers*](https://arxiv.org/html/1105.1616v1), Theorem 3;
- Nunes, [*Squarefree numbers in large arithmetic progressions*](https://arxiv.org/html/1602.00311v1), Theorems 1.1--1.3;
- Nunes, [*A note on the least squarefree number in an arithmetic progression*](https://arxiv.org/pdf/1605.03347), Theorem 1.1 and Lemma 1.3;
- Nunes, [*Squarefree numbers in arithmetic progressions*](https://arxiv.org/html/1402.0684v2), Theorems 1.1--1.2;
- Mangerel, [*Squarefree Integers in Arithmetic Progressions to Smooth Moduli*](https://arxiv.org/html/2008.11163v2), Theorems 1.1 and 3.1 and Remark 3.2;
- Bettin--Chandee, [*Trilinear forms with Kloosterman fractions*](https://arxiv.org/html/1502.00769v1), Theorems 1--2 and the diagonal decomposition in Sections 2--3.

No secondary source was used for a theorem statement.

## 7. Recommended state effect and exact repairs

Do not promote a theorem and do not change the open Round-148 target.  Retain
the source report as a useful source/method no-go only after the following
exact repairs.

1. Replace "Schlage--Puchta's direct additive theorem gives ... which
   aggregates ..." by "choosing the exact reduced denominator in
   Schlage--Puchta gives ... which aggregates ...; this specialization does
   not close the target, and the paper supplies no theorem aggregating the
   other admissible approximants over the varying outer $q$."  Add the
   exact-multiple test following (SR.7).
2. Add $a,b\in\mathbb F_p^\times$ to the Nunes $K_1,K_2$ theorem card.
   State separately that Nunes Lemma 1.3 has $a\in(\mathbb Z/q\mathbb Z)^\times$ and arbitrary positive $q$; only Theorem 1.1 restricts $q$
   to be squarefree.
3. Label (148.30)--(148.31) "fixed $q$-independent inner coefficient
   control" and state explicitly that $\Omega_{d,\lambda,U}(q)$ prevents
   applying it verbatim to (148.1).
4. Add the bandwidth comparison (SR.12) to the $H$-interface paragraph and
   record that no estimate owns
   $\lambda Q/D\ll |j|<\lambda Q/2$.
5. Narrow the terminal result to the quoted theorem interfaces and direct
   specializations.  Preserve the statements that the signed target and the
   squarefree absolute $Q+D$ estimate remain open.

Recommended state effect: **retain/revise; no graph, proof-draft, campaign,
downstream, or exponent change.**

**AMBER**
