# M1 primary-source and hostile audit

- Campaign: `m9-m1-frequency-phase-diagram`
- Round: 10
- Task: `m1_literature_hostile_audit`
- Role: primary-source and hostile reviewer
- Status: literature certificate and scoped no-go evidence only

## 1. Result

The source search found one theorem that imports directly into the actual M1
block: the Tao--Trudgian--Yang exponent pair already certified for M2.  The
spatial factor \(\chi _4(d)\) is exactly the difference of two additive
quarter shifts, so each component is again a model reciprocal phase after a
minor rescaling of its large parameter.  With

\[
 (\kappa,\lambda)=\left(\frac{89}{1282},\frac{997}{1282}\right),
\]

the resulting M1 frequency block satisfies

\[
 B_1(D,L;X)\ll_\varepsilon
 X^{[89(1+\ell)+819\delta]/1282+\varepsilon},
 \qquad D=X^\delta,\quad L=X^\ell,
 \tag{1.1}
\]

provided the spatial block has the fixed normalized-BV profile used by the
project.  Thus it reaches the target exactly on

\[
 \boxed{178\ell+1638\delta\le 463.}                 \tag{1.2}
\]

No searched primary theorem closes the residual M1 triangle.  Heath-Brown's
general derivative theorem is applicable but is already subsumed, for the
clean imported region, by the certified exponent-pair envelope.  The
Robert--Sargos and Kowalski--Robert--Wu monomial bilinear estimates are useful
only after a genuine two-variable/product-phase reduction; they do not apply
to the one-variable character-twisted reciprocal block as it stands.
Bettin--Chandee treats modular inverses in Kloosterman fractions, not real
reciprocals \(X/d\), and is not an import.

The hostile conclusions are:

1. bounded partial sums of \(\chi _4\) plus naive Abel summation give
   \(1+hX/D\) for one spatial sum and hence \(1+LX/D\) for a frequency
   block.  This reaches \(X^{1/4}\) only if
   \(\ell\le\delta-3/4\), which is empty throughout the active range
   \(\delta\le1/2\).  The tempting replacement of \(D^{-1}\) here by
   \(D^{-2}\) forgets to integrate the derivative over a length-\(D\)
   interval;
2. an unshifted reciprocal exponent-pair theorem cannot simply be applied to
   \(hX/d+\rho d/4\): the source's model-phase hypothesis fails because the
   normalized first derivative contains an order-one constant while higher
   derivatives do not.  The correct repair is to absorb the linear term by
   changing the effective parameter, which yields (1.1), not a free
   character saving;
3. a bound for the combined M1/M2 top kernel cannot be projected to M1.  The
   exact cones have the same leading sign, different Vaaler profiles, and an
   unmatched M1 wing, so cancellation in a combined quantity supplies no
   component norm estimate.

## 2. Exact source statements and applicability

### 2.1 Tao--Trudgian--Yang: directly importable

The primary source is T. Tao, T. Trudgian and A. Yang,
[*New exponent pairs, zero density estimates, and zero additive energy
estimates: a systematic approach*](https://arxiv.org/abs/2501.16779),
arXiv:2501.16779v1.

Their Definition 5 calls \(F:[1,2]\to\mathbb R\) a model phase if for a fixed
\(\sigma>0\),

\[
 F^{(p+1)}(u)-\frac{d^p}{du^p}u^{-\sigma}=o(1)
 \quad(p\ge0),                                      \tag{2.1}
\]

uniformly in \(u\).  Example 6 includes
\(F(u)=u^{1-\sigma}/(1-\sigma)\).  Their Definition 11 and non-asymptotic
Lemma 12 state that an exponent pair \((k,l)\) gives, for \(T\ge N\ge1\),
an interval \(I\subset[N,2N]\), and a phase satisfying the finite derivative
version of (2.1),

\[
 \sum_{n\in I}e(TF(n/N))
 \ll_\varepsilon (T/N)^{k+\varepsilon}N^{l+\varepsilon}.       \tag{2.2}
\]

Theorem 20 proves in particular

\[
 (k,l)=\left(\frac{89}{1282},\frac{997}{1282}\right).          \tag{2.3}
\]

For one M1 component, conjugate and relabel \(\rho\mapsto4-\rho\) (which
only swaps \(1\) and \(3\) on integer \(d\)).  Thus it is enough to put
\(d=Du\), \(h\asymp L\), and estimate

\[
 f_{h,\rho}(d)=-\frac{hX}{d}+\frac{\rho d}{4},
 \qquad \rho\in\{1,3\}.                              \tag{2.4}
\]

Choose

\[
 T_{h,\rho}=\frac{hX}{D}+\frac{\rho D}{4},\qquad
 c_{h,\rho}=\frac{hX/D}{T_{h,\rho}},
\]

and define

\[
 F_{h,\rho}(u)=-\frac{c_{h,\rho}}u
       +\frac{\rho D}{4T_{h,\rho}}u.
 \tag{2.5}
\]

Then \(T_{h,\rho}F_{h,\rho}(u)=f_{h,\rho}(Du)\).  In the active range

\[
 \frac{D^2}{hX}\le \frac{D^2}{X}\le1,
\]

so \(T_{h,\rho}\asymp hX/D\), uniformly.  Moreover

\[
 F'_{h,\rho}(u)=c_{h,\rho}u^{-2}+1-c_{h,\rho},
 \quad
 F^{(p+1)}_{h,\rho}(u)
 =c_{h,\rho}\frac{d^p}{du^p}u^{-2}\quad(p\ge1).       \tag{2.6}
\]

For a fixed exponent sector \((\delta,\ell)\), either
\(D^2/(hX)=X^{2\delta-1-\ell}\to0\), in which case
\(c_{h,\rho}=1+o(1)\) and (2.6) is a \(\sigma=2\) model phase, or
\((\delta,\ell)=(1/2,0)\), where the ratio need not tend to zero.  The latter
isolated point is handled by the elementary estimates already recorded in
the project; it is far outside (1.2).  The source hypothesis \(T\ge N\) is
also satisfied because \(T/D\asymp hX/D^2\ge1\), up to fixed endpoint
constants which are harmless in the non-asymptotic formulation.

Thus (2.2) gives for each \(h\asymp L\)

\[
 \sum_{d\asymp D}e(f_{h,\rho}(d))
 \ll_\varepsilon X^\varepsilon
 \left(\frac{hX}{D^2}\right)^\kappa D^\lambda.        \tag{2.7}
\]

The actual identity

\[
 \chi _4(d)=\frac{e(d/4)-e(3d/4)}{2i}                \tag{2.8}
\]

reduces M1 to the difference of these two estimates.  Partial summation
transfers (2.7) through every fixed scale-normalized BV spatial profile; the
hard top profile is a BV sequence with one jump, so this transfer remains
valid without claiming smooth Poisson summation.  Finally

\[
 \sum_{h\asymp L}\frac{\Phi(h/(H+1))}{h}h^\kappa
 \ll L^\kappa                                        \tag{2.9}
\]

because the actual Vaaler factor is bounded.  Equations (2.7)--(2.9) prove
(1.1).  Comparing the exponent

\[
 \kappa(1+\ell-2\delta)+\lambda\delta
 =\frac{89(1+\ell)+819\delta}{1282}
\]

with \(1/4\) gives (1.2).  No averaging in \(X\) occurs.

### 2.2 Heath-Brown: applicable, but not a new graph dependency

D. R. Heath-Brown,
[*A new k-th derivative estimate for exponential sums via Vinogradov's mean
value*](https://arxiv.org/abs/1601.04493), Theorem 1, assumes that
\(f:[0,N]\to\mathbb R\) has continuous derivatives through order \(k\ge3\)
and

\[
 0<\lambda_k\le f^{(k)}(x)\le A\lambda_k.
\]

It concludes

\[
 \sum_{n\le N}e(f(n))
 \ll_{A,k,\varepsilon}N^{1+\varepsilon}
 \left(\lambda_k^{1/[k(k-1)]}+N^{-1/[k(k-1)]}
 +N^{-2/[k(k-1)]}\lambda_k^{-2/[k^2(k-1)]}\right).  \tag{2.10}
\]

After translating a dyadic interval to \([0,N]\), the phase (2.4) obeys
\(|f^{(k)}(d)|\asymp hX/D^{k+1}\); the linear quarter shift disappears from
all derivatives of order at least two.  Thus (2.10) is applicable to each
shift, with the sign corrected by conjugation if necessary.  It is a
coefficient-free one-dimensional bound: the fixed BV profile transfers by
partial summation, while arbitrary bounded spatial coefficients do not.
The theorem yields explicit piecewise derivative-test regions after choosing
\(k\), but it does not exploit \(\chi _4\) and does not close the residual
triangle.  Since Tao--Trudgian--Yang's certified exponent pair already
packages stronger optimized derivative/exponent-pair input for the clean
region (1.2), this source is retained as an applicability check, not proposed
as an additional dependency.

### 2.3 Robert--Sargos and Kowalski--Robert--Wu: strategic analogies only

O. Robert and P. Sargos,
[*Three-dimensional exponential sums with monomials*](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf),
Theorem 1, consider

\[
 S_0=\sum_{h\sim H}\sum_{n\sim N}a(h,n)
       \sum_{m\sim M}b(m)
 e\!\left(\mathsf X\frac{h^b n^g m^a}{H^bN^gM^a}\right),
\]

where \(|a(h,n)|,|b(m)|\le1\) and fixed
\(a(a-1)bg\ne0\).  Their conclusion is

\[
 S_0\ll_\varepsilon(HNM)^{1+\varepsilon}
 \left[\left(\frac{\mathsf X}{HNM^2}\right)^{1/4}
 +(HN)^{-1/4}+M^{-1/2}+\mathsf X^{-1/2}\right].       \tag{2.11}
\]

E. Kowalski, O. Robert and J. Wu,
[*Small gaps in coefficients of L-functions and B-free numbers in small
intervals*](https://arxiv.org/abs/math/0507001), Proposition 5, assume
\(\alpha,\beta\notin\{0,1\}\), \(|\varphi_m|,|\psi_n|\le1\), and define

\[
 S(M,N)=\sum_{m\sim M}\sum_{n\sim N}\varphi_m\psi_n
 e\!\left(\mathsf X\frac{m^\alpha n^\beta}{M^\alpha N^\beta}\right).
\]

They prove

\[
 S(M,N)\ll_\varepsilon
 \left((\mathsf XM^6N^6)^{1/8}+M^{1/2}N+MN^{3/4}
 +\mathsf X^{-1/2}MN\right)(MN)^\varepsilon.          \tag{2.12}
\]

These statements require two or three independent long variables and a
separable monomial phase.  M1 is a single \(d\)-sum inside an \(h\)-average
with the actual coefficient \(\Phi(h/(H+1))/h\).  A B-process may create a
product-phase cone to which (2.11) or (2.12) resembles a possible input, but
that needs the complete transform symbol, hard-edge treatment, coefficient
separation, and all parameter terms.  The pre-existing endpoint audit already
shows that the balanced specialization of (2.12) has terms exceeding the
required \(L^{3/2}\) scale.  Neither theorem is directly importable here.

### 2.4 Bettin--Chandee: wrong arithmetic phase

S. Bettin and V. Chandee,
[*Trilinear forms with Kloosterman fractions*](https://arxiv.org/abs/1502.00769),
Theorem 1, bounds

\[
 \mathcal B(M,N,A)=
 \sum_{a\sim A}\sum_{m\sim M}\sum_{n\sim N\atop(m,n)=1}
 \alpha_m\beta_n\nu_a e\!\left(\vartheta\frac{a\overline m}{n}\right)
\]

by

\[
 \|\alpha\|_2\|\beta\|_2\|\nu\|_2
 \left(1+\frac{|\vartheta|A}{MN}\right)^{1/2}
 \left((AMN)^{7/20+\varepsilon}(M+N)^{1/4}
 +(AMN)^{3/8+\varepsilon}(AN+AM)^{1/8}\right).        \tag{2.13}
\]

Here \(\overline m\) is a modular inverse modulo \(n\), coprimality is
essential, and the coefficients are measured in \(\ell^2\).  The real phase
\(hX/d\) has no modular inverse or modulus variable.  Replacing \(1/d\) by
\(\overline d/n\) would change the problem.  This theorem is therefore not
applicable; it is only a warning that a future modular-reciprocity
reformulation would need exact coprimality and norm bookkeeping.

## 3. Hostile audits of direct claims

### 3.1 Bounded character partial sums and naive Abel

Let \(A(t)=\sum_{n\le t}\chi _4(n)\); then \(|A(t)|\le1\).  For a fixed BV
profile \(w_D\), Abel summation gives, with \(g(d)=w_D(d)e(hX/d)\),

\[
 \left|\sum_{d\asymp D}\chi _4(d)g(d)\right|
 \ll \|w_D\|_{\rm BV}
 \left(1+\int_D^{2D}\frac{hX}{t^2}\,dt\right)
 \ll 1+\frac{hX}{D}.                                  \tag{3.1}
\]

This is actually worse than the often quoted \(1+hX/D^2\), because the
integral is derivative size times interval length.  The latter would be a
false endpoint-freezing step.  Summing the actual Vaaler mass over
\(h\asymp L\) gives

\[
 B_1(D,L;X)\ll 1+\frac{LX}{D}.                        \tag{3.2}
\]

The target condition from (3.2) is
\(\ell\le\delta-3/4\), empty throughout
\(\delta\le1/2\).  Hence naive Abel gives no active power region at all.
Its failure is sharp in mechanism: bounded partial sums control total
variation of the phase, and the phase winds \(\asymp hX/D\) times across a
dyadic spatial interval.

One can instead first exploit frequency smoothness or local product
grouping, but that is a different lemma and is not a consequence of bounded
partial sums of \(\chi _4\).

### 3.2 The incorrect unshifted exponent-pair substitution

A direct declaration for this conjugated-and-relabeled component

\[
 \sum_de(-hX/d+\rho d/4)
 \stackrel{?}{\ll}
 (hX/D^2)^\kappa D^\lambda                         \tag{3.3}
\]

using \(T=hX/D\), \(F(u)=-1/u+\rho D^2u/(4hX)\) is not licensed by
Tao--Trudgian--Yang when \(D^2/(hX)\) is order one.  Indeed

\[
 F'(u)=u^{-2}+\frac{\rho D^2}{4hX},
\]

so the \(p=0\) requirement in (2.1) fails although all higher derivatives
match the reciprocal model.  The valid repair is (2.5): enlarge the source
parameter to include the linear coefficient, normalize the phase, and check
that the discrepancy tends to zero in the actual sector.  This recovers the
same exponent scale only where that check is uniform; it does not create an
extra \(\chi _4\) saving.

The hard endpoint is not exempt.  The fixed profile's single jump is safe for
Abel transfer of interval estimates, but it is not a smooth full-line weight
for Poisson summation.  These are separate assertions.

### 3.3 Combined M1/M2 projection is invalid

Suppose \(K_1\) and \(K_2\) are the exact top stationary kernels.  An estimate
\(|K_1+K_2|\le T\) contains no bound on \(|K_1|\) unless one has a bounded
projection or an independent estimate for \(K_2\); algebraically
\(K_1=Z\), \(K_2=-Z\) is the elementary countermodel.

The actual kernels make the projection still less plausible.  The accepted
Round-9 derivation shows that their leading constants have the same sign,
M1 places \(\Phi\) on the inner frequency while M2 places it on the outer
character variable, and M1 has an unmatched \(H<r<16H\) wing.  Thus even a
successful combined estimate would be a new combined obligation, not a proof
of separately stated `M9-M1`.

## 4. Required controls

1. **Actual Vaaler factor: pass.**  Equation (2.9) retains
   \(\Phi(h/(H+1))/h\); no arbitrary frequency coefficients are substituted.
2. **Hard endpoint: pass with scope.**  Discrete BV with one jump suffices for
   partial summation.  No smooth full-line Poisson theorem is claimed.
3. **Both character shifts: pass separately.**  Equations (2.4)--(2.8) audit
   \(\rho=1,3\) independently; no cancellation between them is assumed.
4. **Both frequency signs: pass.**  Negative \(h\) follows by conjugating the
   phase and applying the same real estimate.  For real profiles it is the
   exact conjugate partner; for complex profiles it is bounded separately.
5. **Fixed versus arbitrary coefficients: pass.**  Exponent-pair transfer
   needs fixed normalized BV in \(d\).  Robert--Sargos and Bettin--Chandee
   allow other coefficient classes only for their different multi-variable
   phases.  None licenses arbitrary coefficients in the one-dimensional M1
   sum.
6. **No hidden average in \(X\): pass.**  All imported estimates and region
   calculations are pointwise for real \(X\).
7. **Numerical use: none.**

## 5. First doubtful or unproved step

No source found in this search proves the residual M1 corridor.  Formula
(1.1) is a direct specialization of an audited exponent pair, but it uses the
project's accepted uniform discrete-BV profile certificate.  Any attempt to
go beyond (1.2) by Robert--Sargos, Kowalski--Robert--Wu, or
Bettin--Chandee first needs a rigorously derived two-variable interface with
their exact phase and parameter hypotheses; no such bridge is proved here.

There was also an isolation breach during this task: a repository-wide search
caused the already-written Round-10 terminal report to be opened.  Per the
conductor's instruction, this report does not assess, cite, validate, or rely
on that Round-10 report.  It must not be counted as an independent review of
any terminal-frequency lemma.

## 6. Exact dependencies and sources used

- `protocol.md`
- `state/proof_obligations.yml`
- `state/active_campaign.yml`
- `state/best_proof_draft.md`
- `rounds/codex-managed/m9-frequency-phase-diagram/reviews/conductor_primary_source_and_region_audit.md`
- `rounds/codex-managed/m9-combined-top-cones/synthesis.md`
- `sources/tao_trudgian_yang_2025.md`
- Tao--Trudgian--Yang, arXiv:2501.16779v1, Definitions 5 and 11,
  Lemma 12, Theorem 20.
- Heath-Brown, arXiv:1601.04493v3, Theorem 1.
- Robert--Sargos, *J. reine angew. Math.* 591 (2006), Theorem 1.
- Kowalski--Robert--Wu, arXiv:math/0507001v1, Proposition 5.
- Bettin--Chandee, arXiv:1502.00769v1, Theorem 1.

## 7. Recommended state effect

1. **Promote or reuse** the certified exponent-pair wedge (1.2) for M1,
   subject to conductor verification of the shifted-model normalization
   (2.5)--(2.7).  This is a pointwise fixed-profile region, not a character
   saving and not full `M9-M1`.
2. **Record a no-go** against naive Abel from bounded partial sums of
   \(\chi _4\): the correct dyadic variation loss is (3.2), which has no
   active target region.
3. **Record a normalization warning**: an additive linear phase cannot be
   silently ignored in the model-phase first-derivative hypothesis.  Use the
   effective parameter construction (2.5) or another explicitly audited
   theorem.
4. **Retain as strategy only** Heath-Brown, Robert--Sargos,
   Kowalski--Robert--Wu, and Bettin--Chandee.  Do not add them as graph
   dependencies for M1 on the basis of this round.
5. Keep `M9-M1`, `M9-M1-top-endpoint-signed-cone`,
   `M9-endpoint-uniformity`, `M9`, and the Gauss-circle target open.
