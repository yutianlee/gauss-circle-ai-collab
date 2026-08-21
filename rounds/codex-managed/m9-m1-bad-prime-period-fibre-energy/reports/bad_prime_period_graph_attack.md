## 1. Result

There is a complete mask-level classification of when a bad local
reciprocal weight has a nontrivial additive period. For a unit \(K_q\),
it is the finite condition

\[
 \Phi'(x)=0\pmod p\qquad(x\in\Omega_p).                 \tag{1.1}
\]

The complete list of solutions to (1.1) at \(p=2,3,5,7\) is given
below. In particular, every nonempty \(3\)-adic mask is periodic; the
genuinely cross-reduction \(3\)- and \(5\)-adic solutions have **exact**
reciprocal depth one for every lift to \(p^\nu\); and at \(p=7\) the only
unit-\(K_q\) solutions reduce to one of the two same-group shapes (or to
the zero cell). These latter fibres are not silently discarded: lifts
which survive the Round-88 coarse deletion remain in the theorem.

For \(p\mid K_q\) and \(\nu\ge2\), every nonempty mask is periodic. For
odd \(p\), it has the unconditional period

\[
 p^{\max(1,\nu-v_p(K_q))}.                              \tag{1.2}
\]

At \(p=2\) the complete odd-residue mask gives a stronger genuine
\(2\)-adic period, stated in (2.6) below; this uses the full prime power,
not a parity surrogate.

The classification yields a nonempty target-safe physical graph
package. Freeze, at any chosen periodic prime-power factor, one complete
reduction cell (a projective mask ray or the zero cell), without cutting
the base-point \(x\)-sum. If the tensor of frozen cells has conductor

\[
 \mathfrak b_\sigma=\prod_{q=p^\nu\in S}
 {p^2\over \eta_{\omega_q}},                            \tag{1.3}
\]

where \(\eta_\omega=1\) for the zero cell and for a projective ray whose
\(A\)- and \(B_2\)-coordinates are both nonzero, and
\(\eta_\omega=p-1\) otherwise, then both directed degrees are at most

\[
 \Delta_\sigma\le {M^2\over\mathfrak b_\sigma}.         \tag{1.4}
\]

After intersecting with the Round-87 and Round-88 survivor, the same
bound holds. Consequently every such complete-fibre tensor with

\[
 \boxed{\mathfrak b_\sigma\ge M^2/\rho_*^2}             \tag{1.5}
\]

is target-safe by the accepted graph estimate (89.13). This is a
genuine but limited package. It does not close the union of all
nonunit-\(K_q\) fibres: for \(p\ge5\), that union has full local directed
degree \(q^2\). Affine periods of \(e_q(u_qx)w_q(x)\) and genuinely
aperiodic factors remain separate and are not claimed by (1.3)--(1.5).

## 2. Exact statement and hypotheses

Fix \(q=p^\nu\Vert M\), put \(\kappa_q=v_p(K_q)\), and write

\[
 \Omega_p=\mathbf F_p\setminus\{0,\bar A,\bar V,
                                      \overline{V+B_2}\},
 \qquad
 G_{A,B_2,V}(x)=
 -{1\over x^2}+{1\over(x-A)^2}+{1\over(x-V)^2}
                  -{1\over(x-V-B_2)^2}.                \tag{2.1}
\]

Empty masks are zero and receive no period label. For a nonempty mask,
the exact reciprocal depth is still the accepted complete-mask depth
\(j_q=\nu-r_q\), where, with
\(\Psi_t(x)=(\Phi(x+t)-\Phi(x))/t\),

\[
 r_q=\min\left\{1\le r\le\nu:
   \min_{x\in\Omega_q}v_p\!\left(K_qp^r\Psi_{p^r}(x)\right)
      \ge\nu\right\}.                                  \tag{2.1a}
\]

The following theorem classifies existence of \(j_q>0\), and in the
transverse small-prime cases determines \(j_q\) exactly.

Use \(Z\) for the reduction \((A,B_2,V)=(0,0,0)\). For a nonzero triple,
\([a:b:v]\) denotes its \(\mathbf F_p^\times\)-scaling orbit. The allowed
residue sets displayed in the table use the shown normalized
representative; they scale with the representative.

| \(p\) | all normalized nonempty reductions satisfying \(G=0\) on \(\Omega_p\) | \(\Omega_p\) for the displayed representatives |
|---:|---|---|
| \(2\) | \(Z\) | \(\{1\}\) |
| \(3\) | \(Z,[0:0:1],[1:1:0],[0:1:0],[0:1:2],[1:0:0],[1:0:1],[1:2:1]\) | respectively \(\{1,2\},\{2\},\{2\},\{2\},\{1\},\{2\},\{2\},\{2\}\) |
| \(5\) | \(Z,[0:0:1],[1:1:0],[1:2:2],[1:3:4],[1:4:3],[1:4:4]\) | respectively \(\{1,2,3,4\},\{2,3,4\},\{2,3,4\},\{3\},\{3\},\{4\},\{2\}\) |
| \(7\) | \(Z,[0:0:1],[1:1:0]\) | respectively \(\{1,2,3,4,5,6\},\{2,3,4,5,6\},\{2,3,4,5,6\}\) |

Thus, for \(\kappa_q=0\) and \(\nu\ge2\), the table is the exact list of
nontrivially periodic reciprocal masks. Every omitted nonempty
reduction is genuinely reciprocal-aperiodic. At \(p=3\) the table is
also the complete list of nonempty reductions. The five \(p=3\) rays

\[
 [0:1:0], [0:1:2], [1:0:0], [1:0:1], [1:2:1]          \tag{2.2}
\]

and the four \(p=5\) rays

\[
 [1:2:2], [1:3:4], [1:4:3], [1:4:4]                  \tag{2.3}
\]

are transverse to the two same-group reduction shapes. For every
prime-power lift in one of (2.2)--(2.3), with \(K_q\) a unit,

\[
 j_q=1.                                                \tag{2.4}
\]

For odd \(p\) with \(\kappa_q>0\), every nonempty reduction is periodic
when \(\nu\ge2\), and its exact depth satisfies

\[
 j_q\ge \min(\kappa_q,\nu-1).                          \tag{2.5}
\]

At \(p=2\), nonemptiness is equivalent to
\(2\mid A,B_2,V\), so \(\Omega_q\) is the complete odd residue set. Put
\(n=(\nu-\kappa_q)_+\) and

\[
 r_{2,0}(n)=
 \begin{cases}
  1,&n\le3,\\
  2,&4\le n\le5,\\
  n-3,&n\ge6.
 \end{cases}                                           \tag{2.6}
\]

Then the complete masked reciprocal weight has period
\(2^{r_{2,0}(n)}\), and hence

\[
 j_q\ge \nu-r_{2,0}(n).                                \tag{2.7}
\]

The exact depth may be larger and is obtained from (2.1a); selecting an
exact-depth subfibre never worsens the graph degrees below.

The full affine phase is deliberately classified separately. For
\(\nu\ge2\), \(e_q(u_qx)w_q(x)\) has a nontrivial additive period if and
only if

\[
 \bar u_q+\bar K_qG_{A,B_2,V}(x)=0
       \quad\hbox{for every }x\in\Omega_p.              \tag{2.8}
\]

If (2.8) holds but (1.1) fails, the factor is affine-only, not a
reciprocal-period fibre. If both fail, it is genuinely full-phase
aperiodic (apart from any separately defined projection-only effect).

For the graph assertion, let \(\omega_q\) be either \(Z\), a table ray at
a unit bad prime, or any nonempty reduction ray at a factor with
\(\kappa_q>0\); always require \(\nu\ge2\). Let
\(\mathcal E_\sigma\) be the set of physical directed edges whose local
\((A,B_2,V)\) reduction belongs to \(\omega_q\) for every \(q\in S\), and
then intersect it with the frozen hard survivor
\(R_*>\rho_*\), \(\mathfrak a<M^2/\rho_*^2\) after all earlier owners.
Every exact \((A,B_2,V)\)-fibre is retained with its complete \(x\)-sum.
Equations (1.3)--(1.5) hold for this set.

For comparison, if one takes the union of every unit-\(K_q\) table cell
at a single prime, the exact local maximum degree is at most

\[
 {q^2\over4},\quad {7q^2\over9},\quad {q^2\over5},
 \quad {q^2\over7}                                    \tag{2.9}
\]

for \(p=2,3,5,7\), respectively. For the transverse rays only, the
\(p=3,5\) bounds improve to \(4q^2/9\) and \(4q^2/25\). By contrast, the
union of all nonunit-\(K_q\) periodic masks has degree \(q^2\) for every
\(p\ge5\); the period property itself gives no physical graph saving
there.

## 3. Proof or derivation

**The mask derivative criterion.** The support of the local weight is
the inverse image of the nonempty proper subset \(\Omega_p\subsetneq
\mathbf F_p\). A nonzero additive translate of \(\mathbf F_p\) generates
the whole additive group, so no such translate can stabilize
\(\Omega_p\). Hence every proper period modulo \(p^\nu\) is divisible by
\(p\). If \(t=p^r\), \(1\le r<\nu\), then on the unit domain

\[
 {K_q(\Phi(x+t)-\Phi(x))\over t}
       \equiv K_q\Phi'(x)\pmod p.                       \tag{3.1}
\]

Thus a reciprocal period with \(K_q\) a unit implies (1.1). Conversely,
take \(t=p^{\nu-1}\). The reciprocal geometric expansion has remainder
divisible by \(t^2\), and \(2\nu-2\ge\nu\), so

\[
 K_q(\Phi(x+t)-\Phi(x))
       \equiv tK_q\Phi'(x)\equiv0\pmod {p^\nu}.         \tag{3.2}
\]

The support is stable because \(p\mid t\). This proves the equivalence.
Replacing \(K_q\Phi\) by \(u_qx+K_q\Phi\) proves the separate affine
criterion (2.8).

**Finite algebraic classification.** Put

\[
 D(X)=X(X-A)(X-V)(X-V-B_2).
\]

On the mask, (1.1) is equivalent to the vanishing of the polynomial

\[
\begin{aligned}
 D(X)^2G(X)={}&-(X-A)^2(X-V)^2(X-V-B_2)^2\\
 &+X^2(X-V)^2(X-V-B_2)^2\\
 &+X^2(X-A)^2(X-V-B_2)^2
   -X^2(X-A)^2(X-V)^2 .                                \tag{3.3}
\end{aligned}
\]

Scaling \((A,B_2,V,X)\) by a unit scales \(G\) by that unit to the power
\(-2\), so it is enough to normalize the first nonzero coordinate of
\((A,B_2,V)\), together with the separate zero cell \(Z\). Direct
substitution in (3.3), over the complete finite list of normalized
triples for \(p=2,3,5,7\), gives exactly the table in Section 2. This is
a finite polynomial verification: for every omitted normalized triple,
one of the explicitly defined points of \(\Omega_p\) makes (3.3)
nonzero. Counting the unit scalings gives respectively \(1,15,25,13\)
successful reductions; at \(p=3\), \(15\) is also the total number of
nonempty reductions.

For the transverse rays, let \(a\) be the sole allowed residue. A second
direct substitution gives the following nonzero values of \(\Phi''(a)\):

\[
\begin{array}{c|ccccc}
 p=3 &[0:1:0]&[0:1:2]&[1:0:0]&[1:0:1]&[1:2:1]\\ \hline
 \Phi''(a)&1&1&2&2&1
\end{array}
\]

and

\[
\begin{array}{c|cccc}
 p=5 &[1:2:2]&[1:3:4]&[1:4:3]&[1:4:4]\\ \hline
 \Phi''(a)&3&1&4&4.
\end{array}                                             \tag{3.4}
\]

The values are in the indicated prime field. Suppose a lift had a
period smaller than \(p^{\nu-1}\). Then \(p^{\nu-2}\) would also be a
period. For \(\nu\ge4\), choose \(x=x_0+pz\) in the allowed residue disc.
Modulo \(p^2\),

\[
 \Phi'(x_0+pz)/p=\Phi'(x_0)/p+z\Phi''(a),               \tag{3.5}
\]

and (3.4) lets one choose \(z\) for which the right side is nonzero.
The \(p^{\nu-2}\)-difference then has valuation exactly \(\nu-1\). When
\(\nu=3\), the reciprocal geometric expansion gives

\[
 \Phi(x+p)-\Phi(x)
   \equiv p\Phi'(x)+{p^2\over2}\Phi''(x)\pmod {p^3};   \tag{3.6}
\]

the same variation in \(z\) again makes one allowed lift nonzero after
division by \(p^2\). For \(\nu=2\), support already forces the minimal
proper period to be \(p\). This proves the exact depth (2.4) for every
prime-power lift, not merely for the displayed residue representatives.

**Nonunit \(K_q\) and the full \(2\)-part.** For odd \(p\), a shift
\(t=p^r\), \(r\ge1\), preserves the mask and
\(\Phi(x+t)-\Phi(x)\) is divisible by \(t\). Taking
\(r=\max(1,\nu-\kappa_q)\) proves (1.2) and (2.5). If \(\nu=1\), support
has no proper period, as correctly recorded by the zero lower bound in
(2.5).

At \(p=2\), nonemptiness forces all four denominators to be odd. Define

\[
 S_m(x)=x^{-m}-(x-A)^{-m}-(x-V)^{-m}
                       +(x-V-B_2)^{-m}.
\]

For \(t=2^r\), \(r\ge1\), the exact reciprocal expansion is

\[
 \Phi(x+t)-\Phi(x)=\sum_{k\ge1}(-t)^kS_{k+1}(x).       \tag{3.7}
\]

Every \(S_m(x)\) is even. If \(m\) is even, every odd inverse power in
\(S_m\) is \(1\pmod8\), so \(8\mid S_m(x)\). Therefore

\[
 v_2(\Phi(x+2^r)-\Phi(x))
      \ge \min(r+3,2r+1).                              \tag{3.8}
\]

After adding \(\kappa_q\), the least \(r\ge1\) for which the right side
is at least \(\nu\) is exactly the piecewise value (2.6). This proves
the full-prime-power \(2\)-adic period (2.7). It does not pretend that
all fibres have the same exact depth; (2.1a) remains the exact
classifier.

**Both directed degrees.** Fix a projective ray
\(\omega=[a:b:v]\). If \(a\ne0\), a fixed source difference \(A\)
determines the scaling parameter in \(\mathbf F_p^\times\); if \(a=0\),
there are at most \(p-1\) choices for that parameter. Once it is fixed,
the prescribed residues of \(B_2,V\) have \((q/p)^2\) lifts. Thus the
local out-degree is at most

\[
 (q/p)^2\quad(a\ne0),\qquad
 (p-1)(q/p)^2\quad(a=0).                               \tag{3.9}
\]

The same argument with the target difference \(B_2\) fixed gives the
local in-degree, with \(b\) in place of \(a\). If \(a=b=0\), both bounds
are \((p-1)(q/p)^2\). In the zero cell \(Z\), \(A,B_2,V\) are all
divisible by \(p\), and both degrees are simply bounded by
\((q/p)^2\). This proves the local bound

\[
 \deg^\pm_q(\omega)\le
   \eta_\omega(q/p)^2={q^2\over p^2/\eta_\omega}.       \tag{3.10}
\]

CRT multiplication of (3.10), with the trivial \(q^2\) bound at every
unselected factor, proves (1.4). Deleting earlier-owned edges can only
lower either directed degree. The selection fixes complete
\((A,B_2,V)\)-fibres and never cuts the \(x\)-sum, so the exact completed
trace and its depth partition remain intact. In particular a depth
\(j_q\) trace descends by \(p^{2j_q}\), not \(p^{j_q}\); no use is made of
false Fejer-mass saving from its frequency support.

Inserting (1.4) into (89.13) gives

\[
 |\mathcal G_{\mathcal E_\sigma}(D)|
 \ll_\varepsilon X^\varepsilon
 DB^3{M^2\over\mathfrak b_\sigma}T^4Q^{-5/6},          \tag{3.11}
\]

and (1.5) gives the frozen target. More generally, for a collection
\(\Sigma\) of cell tensors, the union has both degrees at most

\[
 M^2\sum_{\sigma\in\Sigma}\mathfrak b_\sigma^{-1};    \tag{3.12}
\]

so the exact safe union condition is that the sum in (3.12) be at most
\(\rho_*^2/M^2\).

The package is nonempty. For example, let an admissible modulus be
\(M=3^\nu\), \(\nu\ge2\), freeze the ray \([1:2:1]\), and suppose

\[
 M/3\le\rho_*<M.                                       \tag{3.13}
\]

Then \(\mathfrak b=9\), both degrees are at most \(M^2/9\le\rho_*^2\),
and the sole allowed residue disc is nonempty. This ray is already
cross-group modulo \(3\), hence \(R_*=M>\rho_*\); there are no good-prime
factors, so \(\mathfrak a=1<M^2/\rho_*^2\). Thus these edges lie in the
frozen hard survivor and are newly owned by (1.5). Condition (3.13)
occurs in the constant-width part immediately above the lower first-band
threshold; analogous examples use a \(p=5\) transverse ray or a
nonunit-\(K_q\) ray with a sufficiently large radical conductor.

Finally, counting all table reductions for fixed \(A\pmod p\) gives
respectively \(1,7,5,7\) possible \((B_2,V)\)-residue pairs at
\(p=2,3,5,7\), proving (2.9). If \(\kappa_q>0\) and \(p\ge5\), every one
of the \(p^2\) residue pairs is nonempty and periodic, proving the stated
full-degree obstruction for the complete nonunit stratum.

## 4. First doubtful or unproved step

The first unproved step is any passage from the cellwise estimate
(3.11) to the **complete** bad-prime/nonunit-\(K_q\) survivor without
paying the sum in (3.12). There is no period-derived justification for
that passage. At a nonunit factor \(p\ge5\), periodicity holds for every
nonempty \((B_2,V)\) pair and the local physical graph has degree \(q^2\);
the deep Fourier conductor is therefore unrelated to physical sparsity.
At unit \(p=3,5\), the transverse mask-created periods are all exactly
depth one, so no hidden prime-power graph conductor is available there.
The full \(2\)-adic period (2.7) likewise gives only the residue-cell
degree \(q^2/4\) unless additional full-power congruences are proved from
the actual symbol.

Consequently the residual cell tensors with
\(\mathfrak b_\sigma<M^2/\rho_*^2\), together with affine-only and
genuinely aperiodic factors, still require a signed estimate using the
actual fourfold stationary symbol. No coefficientwise trace bound,
frequency sparsity, or transform descent supplied here closes that
step.

## 5. Required control tests and outcomes

- **Mask rather than numerator.** The classification used the complete
  support \(\Omega_p\) and \(G=\Phi'\) on every allowed residue. It
  reproduces the mask-created \(3\)- and \(5\)-adic periods even when the
  numerator coefficients are units. Outcome: passed.
- **Exact \(3^\nu\) large trace.** The \(p=3\) cross families, including
  the known completed trace of size \(q^2/3\), are present in the table.
  The proof never applies coefficientwise square-root cancellation to
  them. Outcome: passed.
- **Affine separation.** For the control
  \((A,B_2,V)=(1,1,2)\pmod5\), \(\Omega_5=\{4\}\) and
  \(G(4)=1\). It is reciprocal-aperiodic for unit \(K_q\), while the
  full phase has a \(q/5\)-period precisely when
  \(u_q+K_q=0\pmod5\). It is excluded from the reciprocal package by
  (2.8). Outcome: passed.
- **Full \(2\)-part.** The proof used the exact expansion (3.7) over the
  complete odd domain. For odd \(K_q\), its guaranteed depths are
  \(1,2,2,3,3,3,\ldots\) for \(\nu=2,3,4,5,6,7,\ldots\), while individual
  fibres may be deeper. No squarefree or parity replacement was made.
  Outcome: passed.
- **Both graph directions.** The roles of \(A\) and \(B_2\) were counted
  separately in (3.9); a ray with one zero coordinate pays \(p-1\) in
  the appropriate direction. Edge reversal is not assumed to preserve
  the chosen ray. Outcome: passed.
- **Prior ownership.** The graph is intersected only after the
  Round-87 same-group, Round-88 coarse/good-prime, and global \(u=0\)
  deletions. The example (3.13) has \(R_*=M\) and is not a reopened
  owner. Outcome: passed.
- **Completed descent and Fejer mass.** Every exact depth retains the
  factor \(p^{2j_q}\); sparse Fourier support is not counted as a Fejer
  saving. Nonzero multiples of \(M\), both Ramanujan signs, the positive
  square term, and the actual \(Q^{-5/12}\) row saving remain inside the
  accepted estimate (89.13). Outcome: passed.
- **Bounded diagnostic check.** Exhaustive finite-field substitution
  at \(p=2,3,5,7\) reproduced the algebraic table and the nonzero second
  derivatives (3.4); small prime powers reproduced exact depth one on
  all transverse lifts and the \(2\)-adic depth sequence above. These
  checks were used only to falsify omissions; the promoted statements
  are proved algebraically in Section 3. Outcome: passed.

## 6. Dependencies and exact artifacts used

The derivation used only the context selected for this task:

- \`protocol.md\`;
- \`state/proof_obligations.yml\`;
- \`state/active_campaign.yml\`;
- \`rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/plan.json\`;
- \`strategy/conductor_0816_full_proof_strategy.md\`;
- \`rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/derivation_packet.md\`;
- \`rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/synthesis.md\`;
- \`rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/candidates/conductor_good_prime_period_lemma.md\`;
- \`rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/reports/period_depth_tensor_attack.md\`;
- \`rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/reviews/conductor_round88_masked_period_graph.md\`.

The exact inputs used from those artifacts are: the normalized physical
row and ordered-pair function; the complete-mask finite-difference
criterion (2.1a); CRT tensorization and completed descent
\(p^{2j_q}\); the hard survivor \(R_*>\rho_*\),
\(\mathfrak a<M^2/\rho_*^2\); the accepted two-sided graph estimate
(89.13); and the controls forbidding coefficientwise square-root,
frequency-sparsity, or extra-\(M^{-2}\) arguments. No sibling Round-89
report was read or used.

## 7. Recommended state effect

**Promote** the mask derivative criterion, the complete \(p=2,3,5,7\)
table, the exact depth-one theorem for the transverse \(3\)- and
\(5\)-adic rays, the nonunit odd-prime period (2.5), the full \(2\)-adic
period (2.6)--(2.7), and the orbit-tensor directed-degree lemma
(1.3)--(1.5). The promoted scope must be cellwise, or use the exact
summability condition (3.12); it must not be rewritten as a bound for
the union of all bad-prime periods.

**Retain open** every residual periodic tensor failing (1.5), the full
nonunit-\(K_q\) union, affine-only/full-phase periods, projection-only
depth, and genuinely aperiodic factors with the actual fourfold symbol.

**Reject** the implications “nonunit conductor depth gives physical
degree saving,” “small-prime period depth grows through the full prime
power on transverse fibres,” and “\(2\)-adic parity alone classifies the
period.” No first-band conductor extension, full M9-M1 estimate, M9
estimate, or exponent improvement is asserted.
