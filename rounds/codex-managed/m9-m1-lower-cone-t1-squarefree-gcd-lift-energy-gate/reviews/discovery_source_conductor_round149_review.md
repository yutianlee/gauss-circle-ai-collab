# Round 149 discovery/source/conductor hostile interface review

## 1. Result

**Verdict: GREEN.**  I find no blocking mathematical or source-interface
defect in the combination of
`reports/rational_energy_source_audit.md` and
`candidates/conductor_round149_gcd_lift_compression_and_energy_boundary.md`.
The primary-source audit has the Montgomery--Vaughan orientations right,
identifies the fixed-vector obstruction at the correct seam, translates the
squarefree-progression ranges conservatively, and does not claim an
impossibility theorem.  The conductor candidate lawfully adds a divisor proof
for the exact (N)-alignment fibers; it does not use that proof to estimate the
nonexact near/generic determinant range.

The combined conclusion is therefore:

1. the exact lcm collapse, odd gcd-lift recombination, prefix-uniform norms,
   literal equal-cell diagonal, and distinct exact (N)-alignments are
   supported;
2. none of the audited Montgomery--Vaughan, squarefree-progression,
   Bettin--Chandee, or Wright results applies directly to the remaining
   variable-row Gram matrix; and
3. the complete energy bound remains open at the nonexact near/generic signed
   correlation (149.C31).

There is no precise defect to report.  The first genuinely open step is stated
in Section 4 below.

## 2. Exact statement and hypotheses

Let

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor\asymp R^4,
 \qquad DE\asymp M\le R^2,\qquad D\le\sqrt M,
\]

and

\[
 Q=2\sqrt{ND/E}\asymp \frac{DR^2}{\sqrt M},
 \qquad E\asymp \frac MD.
\]

The variable (d\asymp D) is squarefree and need not be odd; only
(\alpha,b,\ell,q,g,L,q_0) are odd.  Put (d_{\mathrm o}=d/(d,2)).
For the compressed row

\[
 G_U(d)=\sum_{(L,q_0)=1}
 \chi_4(Lq_0)\frac{B_{d,U}(L)}L
 \mathscr W_{d,U}(L/q_0)e(NdL/q_0),
 \qquad q_0\asymp LQ,
\]

the target is

\[
 \sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \ll_\varepsilon R^2D X^\varepsilon.
 \tag{R149.1}
\]

The source claim being reviewed is deliberately weaker than the negation of
(R149.1): it says only that the cited theorems do not prove the literal
variable-row energy by direct specialization.  The conductor claim being
reviewed proves the exact alignments and retains as open

\[
 \sum_{\eta=1,2}
 \sum_{m\asymp D/\eta\atop m\ {
m odd\ squarefree}}
 \sum_{x_1\ne x_2\atop \mathrm{nonexact}}
 A_{\eta m}(x_1)\overline{A_{\eta m}(x_2)}
 e\!\left(m\frac{\eta N\delta}{HAB}\right)
 \stackrel{?}{\ll}_\varepsilon R^2D X^\varepsilon.
 \tag{R149.2}
\]

No conclusion is asserted for the Round-138 cross owner, any (t\ge2)
layer, the downstream bridge, the quarter target, or the global exponent.

## 3. Proof and hostile derivation

### 3.1 Montgomery--Vaughan orientation and the fixed-vector seam

For points (x_r) separated modulo one by (\delta), Montgomery--Vaughan
Theorem 1 gives the primal inequality

\[
 \sum_r\left|\sum_d c_d e(dx_r)\right|^2
 \le (D+\delta^{-1})\sum_d|c_d|^2,
 \tag{R149.3}
\]

up to the source's harmless endpoint convention.  Its Lemma 1 gives the dual
form

\[
 \sum_d\left|\sum_r b_r e(dx_r)\right|^2
 \le (D+\delta^{-1})\sum_r|b_r|^2.
 \tag{R149.4}
\]

The desired energy has matrix entries

\[
 a_{d;r}=\chi_4(Lq_0)B_{d,U}(L)
 \mathscr W_{d,U}(L/q_0)/L,
 \qquad x_r=NL/q_0\pmod1.
\]

The primal orientation would require one (c_d) common to every cell (r),
whereas the dual orientation would require one (b_r) common to every outer
integer (d).  Neither requirement holds.  Duality transposes a fixed matrix;
it does not convert an arbitrary row-dependent amplitude into a fixed vector.
The dependence is substantive: at an odd prime (p), the exponent-one local
coefficient is (-1) for (p\mid d_{\mathrm o}) and (0) for
(p\nmid d_{\mathrm o}), and both the exact prefix and the profile also move
with (d).  Thus the source report's first applicability seam is correctly
oriented.  The candidate likewise invokes no fixed-vector large sieve in its
proof of exact alignments.

The source's arbitrary-matrix falsifier is also correctly scoped.  Choosing
(a_{d;r}=u_re(-dx_r)) cancels all phases and disproves an unrestricted
matrix extension of (R149.4), but says nothing adverse about the special
arithmetic array above.

### 3.2 Squarefree progressions and the reduced-denominator translation

Since ((L,q_0)=1), the phase (NL/q_0) has exact reduced denominator

\[
 q_* = \frac{q_0}{(q_0,N)}.
\]

If (q_*\le Y), then for fixed (L), writing
(q_0=hq_*) with (h=(q_0,N)\mid N) gives at most
(Y\tau(N)) cells.  Together with

\[
 \sum_L\frac{|B_{d,U}(L)|}{L}\ll_\varepsilon X^\varepsilon,
\]

this gives scalar cost (DYX^\varepsilon), which is within the scalar target
(RDX^\varepsilon) for every (Y\le R).

Taking the squarefree progression length to be (D), the printed ranges are

\[
 q_*\le D^{13/19-\varepsilon}quad\text{(prime modulus)},
\]

\[
 q_*\le D^{25/36-\varepsilon}quad\text{(squarefree modulus)},
\]

and

\[
 q_*\le D^{196/261-\varepsilon}quad
 \text{(squarefree (D^\eta)-smooth modulus, (0<\eta<1/522))}.
\]

Nunes's fixed-modulus variance formula is stated uniformly for
(q_*\le D), but averages the progression error over reduced residue classes
at one modulus.  Every one of these ranges lies inside (q_*\le D\le R),
which is already covered by the elementary scalar estimate.  More
importantly, the theorems have the pure coefficient (\mu^2(d)), while the
literal row contains (B_{d,U}(L)\mathscr W_{d,U}(L/q_0)); the complete-sum
results also have inverse-square finite-field phases and fixed moduli.  Thus
the range translation in the source audit is correct and is not being used as
an energy theorem.

### 3.3 Bettin--Chandee and Wright

Bettin--Chandee Theorem 1 treats independent sequences
(\nu_a\alpha_m\beta_n) with phase

\[
 e(\vartheta a\overline m/n).
\]

The formal assignment (a=d), (n=q_0), (\vartheta=N), and
(mL\equiv1\pmod{q_0}) does reproduce the phase because
(\overline m\equiv L\pmod{q_0}).  It does not reproduce the amplitude:
(m) is selected jointly by ((L,q_0)), and after eliminating (L) the
weight

\[
 B_{d,U}(L(m,n))\mathscr W_{d,U}(L(m,n)/n)/L(m,n)
\]

is not a product of three independent sequences.  Dyadically splitting the
possible representatives (m) does not remove this graph dependence.  The
Bettin--Chandee proof diagonal (\ell_1n_1=\ell_2n_2) is also not the
equal-cell or (N)-alignment diagonal of this energy.  Remark 1 permits a
controlled (C^1) phase perturbation; it does not permit a joint nonsmooth
amplitude.  The source report therefore stops at the right first mismatch.

Wright Theorem 2.1 similarly has an inverse fraction with a fixed denominator
factor and separate coefficient sequences.  Corollary 2.2 has a fixed residue,
independent divisor-bounded convolution coefficients, a Siegel--Walfisz
hypothesis on one sequence, a principal reduced-residue subtraction, and the
sum of individual absolute discrepancies over moduli.  None is the literal
Gram square.  The version-2 ranges quoted in the source report are correct:

\[
 N_s\le Q_s^{-33/28}Z^{17/28-\varepsilon},
\]

or the two alternatives with
(Q_s\le Z^{45/89-\varepsilon}) and respectively
(N_s\le Z^{7/90-\varepsilon}) or
(N_s\le Z^{101/630-\varepsilon}), together with the printed lower and
residue restrictions.  Because there is no legal variable map, the report
properly labels its substitution (Z\asymp M) as only a size diagnostic.  At
the upper lift it gives

\[
 q_0\asymp EQ\asymp R^2\sqrt M,
\]

which is indeed far beyond (M^{45/89}) for (M\le R^2).  The separability,
congruence, and absolute-value-placement failures occur before that numerical
range failure.

### 3.4 Complete (R,M,D,E,Q) capacity check

The identities

\[
 Q\asymp\frac{DR^2}{\sqrt M},\qquad
 E\asymp\frac MD,\qquad
 E^2Q^2\asymp NM\asymp MR^4
\]

give the following ledger.

| route | capacity | normalized capacity | outcome |
|---|---:|---:|---|
| literal equal-cell energy | (DQX^\varepsilon) | (D/\sqrt M\le1) versus (R^2D) | safe |
| candidate exact off-cell alignments | (DX^\varepsilon) | (R^{-2}) versus (R^2D) | safe |
| reduced denominators (q_*\le Y) | (DYX^\varepsilon) | (Y/R\le1) versus (RD) | safe for (Y\le R) |
| illegal fixed-vector raw spacing | ((D+E^2Q^2)QX^\varepsilon) | (D/\sqrt M+R^4\sqrt M) | non-saving |
| illegal determinant-two spacing | ((D+M)QX^\varepsilon) | (D/\sqrt M+\sqrt M) | loses up to (R) |
| required separable cluster constant | (K\le R^2D/Q=\sqrt M) | determinant scale costs (M) | misses (\sqrt M) |
| Schlage--Puchta, exact denominator at (L=1) | (D+Q^2) | (R^{-1}+R^3/E) versus (RD) | non-saving direct specialization |
| Bettin--Chandee conductor, (L\asymp H) | ((1+ND/(H^2Q^2))^{1/2}) | ((1+E/H^2)^{1/2}) | formal only; amplitude is nonseparable |
| Wright upper-lift diagnostic | (q_0\asymp R^2\sqrt M) | (q_0\gg M^{45/89}) | range fails after the earlier interface failures |

For the optimistic determinant calculation, all (L_i,q_i) are odd, so a
nonzero (\Delta=L_1q_2-L_2q_1) has (|\Delta|\ge2).  At
(L_i\asymp E), (q_i\asymp EQ), the unfolded gap is
(N|\Delta|/(q_1q_2)\asymp M^{-1}).  Modulo-one folding and the exact
congruence can only invalidate this optimistic spacing model, not improve its
proved capacity.  At the balanced endpoint
((M,D,E,Q)\asymp(R^2,R,R,R^2)), the normalized determinant-two loss is
(1+R), as stated.

### 3.5 The conductor's exact-alignment proof

For a distinct exact base-frequency alignment, write

\[
 q_1=HA,\qquad q_2=HB,\qquad (A,B)=1,
 \qquad \delta=L_1B-L_2A\ne0.
\]

Reducedness gives ((\delta,A)=(\delta,B)=1).  The condition
(q_1q_2\mid N(L_1q_2-L_2q_1)) is exactly

\[
 HAB\mid N\delta.
\]

Hence (AB\mid N) and

\[
 H\mid (N/AB)\delta.
\]

For fixed (L_1,L_2), the coprime factor pairs (A,B) with (AB\mid N)
and the subsequent divisors (H) have total multiplicity
(O_\varepsilon(X^\varepsilon)).  Summing the actual bounded profiles and
using the row-wise norm gives

\[
 \mathscr E_{\rm exact,off}
 \ll_\varepsilon
 \sum_{d\asymp D}
 \left(\sum_L\frac{|B_{d,U}(L)|}{L}\right)^2X^\varepsilon
 \ll_\varepsilon DX^\varepsilon.
\]

This argument permits common factors and prime powers in the (q_i).  When
(d=\eta m), (\eta\in\{1,2\}), the (q_i) are odd, so multiplying the
phase numerator by (2) creates no additional exact base-frequency
alignment.  The even-(d) case is therefore correctly audited, while all
local coefficient dependence remains through (d_{\mathrm o}) and the
moving prefix/profile.

### 3.6 Scope of the no-go

The source report says that the audited *direct applications* do not prove
the literal energy.  It explicitly disclaims a lower bound for the signed
energy and leaves open a matrix-valued rational large sieve, an exact
owner-preserving Euler recombination, and a direct arithmetic count using the
actual signs.  The conductor candidate uses the equally narrow formulation
"no accepted artifact or audited source currently proves" (149.C31).  It
does not infer an impossibility result from the positive capacity diagnostics.
The no-go is therefore correctly scoped.

## 4. First doubtful or unproved step

There is no doubtful step in the source-interface conclusions or in the
candidate's exact-alignment divisor bound.  The first unproved mathematical
step is the nonexact part (R149.2), equivalently the signed correlation with

\[
 0<\left\|\frac{\eta N\delta}{HAB}\right\|\ll D^{-1}
\]

and its generic complement, while retaining the literal
(d)-dependent (B_{d,U}(L)\mathscr W_{d,U}(L/q_0)).  Unlike exact
alignment, this inequality neither forces (AB\mid N) nor makes (H) divide
one fixed nonzero integer.  Montgomery--Vaughan cannot be inserted because
the row vector moves with (d), and the audited inverse-fraction theorems do
not accept the resulting graph-supported amplitude.

Thus the first genuinely open step is: prove (149.C31), or produce an exact
signed reorganization whose coefficients meet a stated theorem's independent
sequence hypotheses without losing the (R^2D) energy target.

## 5. Required control tests and outcomes

| control | outcome |
|---|---|
| Montgomery--Vaughan primal/dual orientation | **PASS.**  The primal fixes the (d)-vector; the dual fixes the cell vector.  Neither accepts (a_{d;r}). |
| fixed-vector seam | **PASS.**  The local (p\mid d_{\mathrm o}) rule, exact prefix, and profile give genuine row dependence before spacing. |
| squarefree-progression range translation | **PASS.**  The prime, squarefree, smooth-squarefree, and variance ranges are all contained in the already safe (q_*\le D\le R) stratum and have the wrong coefficient/averaging axis. |
| Bettin--Chandee phase and separability | **PASS.**  The inverse-phase dictionary is only formal; the inverse representative is graph-coupled and the amplitude is not a tensor product.  Its proof diagonal is different. |
| Wright phase, convolution, and absolute-value placement | **PASS.**  The literal Gram matrix has no legal fixed-residue convolution map; the quoted v2 ranges are accurate and fail in the nonlawful upper-lift diagnostic. |
| complete (R,M,D,E,Q) ledger | **PASS.**  Every displayed ratio in Section 3.4 follows from (Q\asymp DR^2/\sqrt M), (E\asymp M/D), and (N\asymp R^4). |
| literal and exact-alignment diagonals | **PASS.**  They cost (DQX^\varepsilon) and (DX^\varepsilon), respectively. |
| common divisors and imprimitive denominators | **PASS.**  The (H,A,B,\delta) classification retains all common factors and uses only divisor multiplicity. |
| even squarefree (d) | **PASS.**  The lcm ledger uses (d_{\mathrm o}), (p=2) is absent, and odd denominators make the parity split harmless for exact alignment. |
| no-go scope | **PASS.**  Both artifacts state a direct-applicability obstruction, not a signed lower bound or universal impossibility theorem. |
| downstream ownership | **PASS.**  No Round-138, (t\ge2), bridge, target, or exponent claim is altered. |

No numerical experiment was used.

## 6. Dependencies and exact artifacts used

Repository artifacts used:

- `protocol.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/reports/rational_energy_source_audit.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-gcd-lift-energy-gate/candidates/conductor_round149_gcd_lift_compression_and_energy_boundary.md`.

Primary sources hostile-checked:

- H. L. Montgomery and R. C. Vaughan,
  [*The large sieve*](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf), Theorem 1 and Lemma 1;
- J.-C. Schlage-Puchta,
  [*The exponential sum over squarefree integers*](https://arxiv.org/html/1105.1616v1), Theorem 3;
- R. M. Nunes,
  [*Squarefree numbers in large arithmetic progressions*](https://arxiv.org/html/1602.00311v1), Theorems 1.1--1.3;
- R. M. Nunes,
  [*A note on the least squarefree number in an arithmetic progression*](https://arxiv.org/html/1605.03347v1), Theorem 1.1 and Lemma 1.3;
- R. M. Nunes,
  [*Squarefree numbers in arithmetic progressions*](https://arxiv.org/html/1402.0684v2), Theorems 1.1--1.2;
- A. P. Mangerel,
  [*Squarefree Integers in Arithmetic Progressions to Smooth Moduli*](https://arxiv.org/html/2008.11163v2), Theorem 1.1, Theorem 3.1, and Remark 3.2;
- S. Bettin and V. Chandee,
  [*Trilinear forms with Kloosterman fractions*](https://arxiv.org/html/1502.00769v1), Theorems 1--2 and Remark 1;
- T. Wright,
  [*Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions*](https://arxiv.org/html/2604.25177v2), Theorem 2.1, Corollary 2.2, Theorem 2.3, and Corollary 2.4.

No sibling review, synthesis, validation matrix, proof draft, or shared-state
artifact was used or edited.

## 7. Recommended state effect

**GREEN; promote the conductor kernel subject to the normal State Patch
process.**  Promote the exact lcm/gcd-lift compression, prefix-uniform norms,
literal equal-cell diagonal, and imprimitive exact-alignment divisor bound.
Retain the source-scoped obstruction that no audited fixed-vector or
inverse-fraction theorem proves the literal variable-row near/generic energy.

Keep (149.C7), (149.C31), the signed scalar target, and every downstream
obligation open.  The next proof attempt must address the nonexact
near/generic variable-row correlation with the actual coefficients and signs;
it may not replace them by a separable surrogate or infer a saving from the
capacity diagnostics alone.
