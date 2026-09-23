# Round 177 post-unmask blind review of the alias-conductor reduction

## 1. Result

**Green on the promoted mathematics, with one non-substantive summation
notation repair.** I found no algebraic or power-ledger defect in the
exact primitive folding, reduced-conductor decomposition, coefficient
mass, fixed-stratum capacity, or target-safe low-\(q\) transform packet
recorded in the durable Round-177 kernel.

In particular:

\[
 g=(u,n),\qquad u_0=u/g,\qquad n_0=n/g
\]

is the exact primitive anchor modulus; the \(g\) original aliases in one
class modulo \(u_0\) fold to one coefficient \(c_{u_0}(\ell)\); and the
final additive conductor is

\[
 q=\frac{u_0}{(\ell,u_0)}.
\]

The fixed-\((\kappa,u,u_0)\) literal capacity is \(O(u_0L)\), the
coefficient-weighted exact-\(q\) capacity is
\(O(Lq\log(2q))\), and the complete packet
\(q\leq(\log(2X))^B\) is globally
\(O_{B,\delta,\gamma,\varepsilon}(L^2X^\varepsilon)\).

The transform-sector theorem is exact and is strictly stronger than the
conductor-one lemma in my blind report. The blind sector is exactly the
folded \(\ell=0\), \(q=1\) slice. The Round-177 theorem proves every
reduced alias with \(q\leq(\log(2X))^B\), including nonzero aliases and
low-conductor aliases belonging to physical strata with
\(u_0>(\log(2X))^B\). Its proof is positive conductor by conductor, so
this strength does not depend on cancellation between the newly added
transform slices.

The high-conductor packet remains open. The exact Parseval and rank-one
\(TT^*\) identities support only the stated route-scoped self-return
audit; they do not prove or refute the literal high-\(q\) estimate.

## 2. Exact statement and hypotheses checked

I reviewed the durable claim under the Round-176 literal identity with

\[
 R_{\log}<2\kappa n<R_0,\qquad
 \kappa=\kappa_*<\delta L,\qquad
 (u,n)<\gamma L,
\]

both opposing orientations, \(\kappa,u\) odd, \((u,v)=1\), all
squarefree and parity branches, the exact Fejer factor, literal endpoint
coefficients and conjugations, displacement inequalities, and full-line
zero extension.

For each unique gcd stratum,

\[
 u=gu_0,\qquad n=gn_0,\qquad (n_0,u_0)=1,
\]

the checked exact block is

\[
\begin{aligned}
 \mathcal H_{\kappa,u,u_0,\ell}
 =\sum_{v,n_0,t}\Big\{&
 \Lambda^+(t)e\!\left(\Psi^+(t)+\frac t2+
          \frac{\ell\bar v n_0}{u_0}\right)\\
 &+\Lambda^-(t)e\!\left(\Psi^-(t)+\frac t2-
          \frac{\ell\bar v n_0}{u_0}\right)\Big\},
\end{aligned}
\]

where every displayed range is the literal zero-extended range. The
claimed decomposition

\[
 \Re\mathfrak C^{\rm rem}_{\rm low\text{-}\kappa}
 =\Re\sum_{\kappa,u}\sum_{u_0\mid u}
       \sum_{\ell\bmod u_0}
       c_{u_0}(\ell)\mathcal H_{\kappa,u,u_0,\ell}
\]

is exact. Restricting this identity to \(q\leq Q_B\), where
\(Q_B=(\log(2X))^B\), defines an exact Fourier subaggregate; the
complement is exactly \(q>Q_B\). The condition is invariant under
\(\ell\mapsto-\ell\), and both orientations and the outer real part remain
inside the identity.

## 3. Verification of identities and the power ledger

### 3.1 Primitive residue and alias folding

Because \(g\) is odd and \(v\) is invertible modulo \(u\),

\[
 [\pm\bar v n]_u
 =g[\pm\bar v n_0]_{u_0}.
\]

The right side is in \([0,u)\) and has the required congruence, so this is
an equality of canonical representatives, not merely a congruence. Hence

\[
 E_u(\pm\bar v n)=E_{u_0}(\pm\bar v n_0).
\]

For \(a\bmod u_0\), grouping the exact \(u\)-DFT by
\(k=\ell+ju_0\) gives

\[
\begin{aligned}
 E_u(ga)
 &=\sum_{\ell\bmod u_0}
   \left(\sum_{j=0}^{g-1}c_u(\ell+ju_0)\right)
   e(\ell a/u_0)\\
 &=E_{u_0}(a).
\end{aligned}
\]

Uniqueness of the \(u_0\)-DFT proves

\[
 \sum_{j=0}^{g-1}c_u(\ell+ju_0)=c_{u_0}(\ell).
\]

There is no lost factor \(g\): the \(g\) coincident frequencies are summed
algebraically before absolute values. Conversely, their physical lift
multiplicity is not erased; it remains in the length-\(u=gu_0\)
\(v\)-range used in the capacity count.

The signs in the two-orientation block also match Round 176 exactly.
Expanding \(E_{u_0}(+\bar v n_0)\) gives the plus phase
\(+\ell\bar v n_0/u_0\); expanding
\(E_{u_0}(-\bar v n_0)\) gives the minus phase with the negative sign.
The factor \((-1)^t=e(t/2)\) and the endpoint conjugations remain in
\(\Lambda^\pm e(\Psi^\pm)\).

### 3.2 Reduced conductor and coefficient mass

Write \(h=(\ell,u_0)\), \(q=u_0/h\), and \(\ell=ha\) with
\((a,q)=1\). Direct substitution gives

\[
 c_{u_0}(ha)
 =\frac{2}{u_0\{1+e(-a/q)\}}
 =\frac q{u_0}c_q(a).
\]

Therefore

\[
 \sum_{\substack{\ell\bmod u_0\\u_0/(\ell,u_0)=q}}
 |c_{u_0}(\ell)|
 =\frac q{u_0}
   \sum_{\substack{a\bmod q\\(a,q)=1}}|c_q(a)|
 \ll\frac q{u_0}\log(2q).
\]

This includes \(q=1\), for which the unique folded zero alias has
\(c_{u_0}(0)=1/u_0\). For
\(\ell=(u_0\pm1)/2\), \((\ell,u_0)=1\), so \(q=u_0\) and the coefficient
has constant size. Thus conductor reduction retains the dangerous
near-half packet exactly.

The original-alias conductor agrees with this classification:

\[
 \frac{u}{(kn,u)}
 =\frac{u_0}{(k,u_0)}
 =\frac{u_0}{(\ell,u_0)}.
\]

This checks the zero, imprimitive, and primitive aliases simultaneously.

### 3.3 Literal capacity

Put \(U=L/\kappa\). Literal support gives \(u,v\asymp U\) and
\(O(1+\kappa)=O(\kappa)\) fibre sites. In the fixed gcd stratum,

\[
 n=gn_0\ll U,\qquad g=u/u_0,
\]

so

\[
 n_0\ll U/g=Uu_0/u\ll u_0.
\]

There are therefore \(O(u_0)\) determinant values, \(O(U)\) physical
\(v\)-values, and \(O(\kappa)\) fibre values. Both orientations change
only the constant:

\[
 O(u_0U\kappa)=O(u_0L).
\]

This restores the \(g\) residue lifts and the \(\kappa\) fibre lifts:
\(\kappa g\asymp L/u_0\). Squarefreeness, selectors, parity restrictions,
hard endpoints, gcd and determinant cutoffs, and zero extension only
delete or downweight atoms for this positive estimate.

Multiplication by the exact-\(q\) coefficient mass gives

\[
 O(u_0L)\cdot O\!\left(\frac q{u_0}\log(2q)\right)
 =O(Lq\log(2q)).
\]

This is the correct restored local power. A single square-root saving
would leave \(L\sqrt q\), so the open high-\(q\) sector still needs a full
factor \(q\), two coupled square roots, or an equivalent signed average.

### 3.4 Global low-\(q\) ledger

For fixed \((\kappa,u)\),

\[
 \sum_{u_0\mid u}
 \sum_{\substack{q\mid u_0\\q\leq Q_B}}
 Lq\log(2q)
 \ll LQ_B\log(2Q_B)\tau(u)^2.
\]

The corrected fully quantified outer sum is

\[
\begin{aligned}
 \left|\mathfrak C^{\rm rem}_{q\leq Q_B}\right|
 &\ll LQ_B\log(2Q_B)
 \sum_{\substack{\kappa<\delta L\\\kappa\ {\rm odd}}}
 \sum_{\substack{u\asymp L/\kappa\\u\ {\rm odd}}}
 \tau(u)^2 X^\eta\\
 &\ll LQ_B\log(2Q_B)
 \sum_{\kappa<\delta L}\frac L\kappa X^{2\eta}\\
 &\ll L^2Q_B\log(2Q_B)\log(2L)X^{2\eta}\\
 &\ll_{B,\delta,\gamma,\varepsilon}L^2X^\varepsilon.
\end{aligned}
\]

Here \(u\ll L\leq X^{1/4}\), so the standard divisor bound and a choice
of \(2\eta<\varepsilon\) absorb all divisor and polylogarithmic factors.
The alternative \(u=ghq\) divisor-hyperbola ledger in the discovery
report gives the same power, with one additional harmless logarithm.

### 3.5 Energy identities and their scope

With

\[
 H_\ell=\sum_zA_ze(\ell b_z/u_0),\qquad
 B_b=\sum_{z:b_z=b}A_z,
\]

finite Fourier orthogonality gives exactly

\[
 \sum_{\ell\bmod u_0}|H_\ell|^2
 =u_0\sum_{b\bmod u_0}|B_b|^2.
\]

Keeping the exact coefficient matrix gives

\[
 \sum_{\ell,\ell'}
 c_{u_0}(\ell)\overline{c_{u_0}(\ell')}
 H_\ell\overline{H_{\ell'}}
 =\left|\sum_bE_{u_0}(b)B_b\right|^2,
\]

which is the original physical block squared. Alias Cauchy replaces this
rank-one matrix by the identity and exposes the residue-bucket energy.
The self-diagonal has positive-certificate square-root capacity
\(u_0\sqrt L\), and positive bucket recombination can return \(Lu_0\).
These calculations are correct upper-capacity audits and are not literal
lower bounds.

The claim that anchor antisymmetry alone does not pair the two literal
orientations is also consistent with Round 176: the sign-reversing
same-\((u,v)\) displacement map sends positive \(s,w\) to negative
displacements and hence outside the zero-extended support. The live
positive-displacement interchange swaps \(u,v\) and replaces the selected
divisor by its complementary factor, for which the literal support gives
no accepted matching identity. No orientation cancellation is used in the
low-\(q\) proof.

### 3.6 Strict comparison with the blind conductor-one lemma

In the notation of my blind report, the original alias had conductor one
exactly when

\[
 \frac{u_0}{(u_0,k)}=1
 \iff u_0\mid k.
\]

Thus \(k=ju_0\), \(0\leq j<g\), and these are precisely the aliases that
fold to \(\ell=0\). Their exact coefficient is

\[
 \sum_{j=0}^{g-1}c_u(ju_0)=c_{u_0}(0)=\frac1{u_0}.
\]

The blind proof bounded these terms before folding through the larger
absolute coefficient sum; the Round-177 kernel folds them first and gives
the sharp \(L\)-scale for each \(q=1\) gcd stratum.

The new theorem then adds every nonzero folded alias satisfying

\[
 1<q=\frac{u_0}{(\ell,u_0)}\leq Q_B.
\]

It consequently includes all aliases in every physical stratum
\(u_0\leq Q_B\), plus the low-conductor aliases of physical strata
\(u_0>Q_B\). Since the proof establishes the positive per-\(q\) estimate
\(O(Lq\log(2q))\), the added slices cannot be hiding cancellation with
the conductor-one slice. This verifies the requested strict-strength
comparison.

## 4. First defect and required repair

The first defect is only notational. In durable-kernel display (177.K26),
the \(O(L/\kappa)\) count of supported \(u\)'s is substituted while
\(\tau(u)^2\) is left with a free \(u\). The intended argument is valid,
but the display should be replaced by the fully quantified sum in
Section 3.4 above, or by

\[
 \sum_{u\asymp L/\kappa}\tau(u)^2
 \ll (L/\kappa)X^\eta.
\]

This repair changes no power, hypothesis, sector, or conclusion.

There is also a scope-citation ambiguity in the formalized candidate:
“promote (177.K3)--(177.K35)” could be read as promoting the unproved
sufficient estimates (177.K34)--(177.K35). The surrounding prose correctly
leaves them open. For mechanical clarity, the candidate should cite the
proved theorem (177.K12), exact decomposition (177.K16), identities
(177.K3)--(177.K11), and scoped energy statements
(177.K27)--(177.K33), while naming (177.K34)--(177.K35) explicitly as the
remaining gate.

I found no substantive defect requiring a change to the promoted
low-reduced-conductor theorem.

## 5. Control checks and outcomes

- **Round-176 seam:** The signs, \(t/2\) frequency, phases, endpoint
  conjugations, determinant range, original-gcd cutoff, and two
  orientations in the new block agree with (176.K17)--(176.K21).

- **Primitive modulus and multiplicity:** The \(g\) frequency fold is
  exact, while the \(g\) physical \(v\)-lifts remain in \(O(u_0L)\). No
  multiplicity is silently deleted or counted twice.

- **Zero and imprimitive aliases:** The folded zero coefficient is
  \(1/u_0\); every other alias is classified by its exact \(q\). The
  \(q=1\) sector agrees with the blind conductor-one result.

- **Near-half aliases:** They have \(q=u_0\) and constant coefficient, so
  they remain in the high-conductor complement when \(u_0>Q_B\).

- **Incomplete intervals and endpoints:** The low-\(q\) proof uses only
  literal cardinality bounds and never completes the \(v\)-interval.
  Endpoint and zero-extension fields remain inside \(\Lambda^\pm\).

- **Both orientations:** They are combined before every DFT-energy
  identity and before the promoted absolute estimate. No complementary
  divisor or same-fibre cancellation is assumed.

- **Selector and squarefree fields:** They are retained literally and
  used only through boundedness for the positive low-\(q\) count. No
  periodicity, density, factorization, or Möbius cancellation is imported.

- **Global power:** The exact conductor coefficient mass cancels the
  \(u_0\) in the raw capacity. The remaining \(Q_B\), divisor, and harmonic
  factors are polylogarithmic and absorb into \(X^\varepsilon\).

- **Energy/self-return:** Parseval and rank-one reconstruction are exact.
  Diagonal, collision, and dechirped-array capacities remain quarantined as
  method audits, not literal lower mass.

- **Owner scope:** Only the low-\(q\) Fourier packet is closed. The
  high-\(q\) packet, complete K17a, the residual scalar, and every parent
  remain open.

## 6. Dependencies and exact artifacts used

This review used only:

1. rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/reports/blind_alias_energy_rederivation.md;
2. rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/reports/hybrid_large_sieve_capacity_audit.md;
3. rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/reports/literal_hybrid_inverse_residue_attack.md;
4. rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/candidates/formalized_primitive_alias_conductor_reduction.md;
5. proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_alias_conductor_reduction.md; and
6. proofs/kernels/m9_m2_hard_top_t1_residual_k17a_cross_gcd_alternating_fibre_reduction.md.

No graph, state, synthesis, source card, web source, numerical
experiment, or unlisted research artifact was used or edited.

## 7. Recommended state effect

**Promote after the two editorial repairs in Section 4.** The exact
primitive folding, reduced-conductor coefficient mass, literal
\(O(u_0L)\) capacity, target-safe transform packet
\(q\leq(\log(2X))^B\), and scoped energy/self-return identities are
mathematically sound and strictly strengthen the blind conductor-one
sector.

Retain

\[
 q>(\log(2X))^B
\]

as the exact open Fourier complement. Do not promote (177.K34) or
(177.K35), do not infer literal lower mass from the positive capacities,
and do not claim any cancellation between the two orientations without a
new literal identity.
