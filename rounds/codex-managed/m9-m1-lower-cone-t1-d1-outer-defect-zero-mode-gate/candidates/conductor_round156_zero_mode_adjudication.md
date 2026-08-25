# Round 156 conductor candidate adjudication: exact cancellation of the complete theta zero row

- Campaign: m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate
- Round: 156
- Starting graph: f9866ea08923ae28f9631e503d2a5eb6be3cd85a09eb05505deec2903d1658b6
- Proposed terminal label: outer_defect_zero_mode_target
- Status: conductor synthesis after three terminal GREEN reviews
- Allocation: 100% analytic and algebraic; 0% numerical

## 1. Result

Fix \(A>0\), put

\[
 q=4N,\qquad J_A=M^{3/4}(\log(2X))^A,\qquad
 K=\sqrt{NM},
\tag{156.CA1}
\]

and let \(J_A<V\le K\).  For the literal pre-linearization coefficient
\(B_j(x)\), define

\[
 A_j=\widehat B_j(0)=\sum_{x\bmod q}B_j(x).
\tag{156.CA2}
\]

Then the complete zero-frequency row

\[
 \mathcal Z_U(V)=
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)d\sqrt c\,A_jK(0,-j;c),
 \qquad c=\frac{4N}{d},
\tag{156.CA3}
\]

satisfies the full-range estimate

\[
 \boxed{\mathcal Z_U(V)
 \ll_{\varepsilon,A}M^{-1/4}X^\varepsilon
 \ll_{\varepsilon,A}X^\varepsilon.}
\tag{156.CA4}
\]

The lower bound on \(V\) is not used by the zero-row argument.  The upper
bound \(V\le K\) is used only in the literal coefficient-variation
estimate.

There are two independent arithmetic proofs of the cancellation needed
in (156.CA4).  The first recombines every odd \(d\mid N\) exactly and
uses a finite Fourier bound for the resulting quotient-character root
sequence.  The statement-only report independently opens each fixed
\(K(0,-j;c)\) and obtains the same final power from geometric sums.  The
primitive-character decomposition and every odd, two-adic, squareful,
and principal local factor have also been computed exactly.  No
Pólya--Vinogradov, Burgess, spectral, or numerical input is needed for
the promoted estimate.

This closes only the \(v=0\) row.  It proves no estimate for the
incomplete nonzero-\(v\) matrix and changes no complete defect range,
\(M\)-boundary, other owner, M9 statement, bridge, quarter target, or
global exponent.

## 2. Exact statement and hypotheses

The coefficient is the literal zero extension

\[
 B_j(x)=
 {\bf1}_{x\ge1}{\bf1}_{-x\le j\le x-1}
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(-\frac{j}{x+\sqrt{x^2-j}}\right),
\tag{156.CA5}
\]

component by component, with the inherited off-congruence real profile,
actual transitions, half-open support values, asymmetric nearest-integer
cell, strict dyadic mask, and hard endpoints.  The accepted profile and
support facts are

\[
 \|w_U\|_\infty+\operatorname {Var}w_U
 \ll_\varepsilon M^{-3/4}X^\varepsilon,
 \qquad x\asymp K,
\tag{156.CA6}
\]

and the union of physical \(x\)-supports has \(O(KX^\varepsilon)\)
integer points in one residue system modulo \(q\).  In particular
\(2x<N<q\) for sufficiently large \(X\), so no physical representative
wraps.  The external factor \(B_{1,U}(1)\) is not part of (156.CA3);
its accepted \(O_\varepsilon(X^\varepsilon)\) bound is restored once
when the scalar is reassembled.

For every \(c\equiv0\pmod4\),

\[
 K(0,-j;c)=
 \sum_{a\bmod c}^{*}
 \epsilon_a\left(\frac ca\right)e_c(-aj),
 \qquad
 \epsilon_a=
 \begin{cases}1,&a\equiv1\pmod4,\\i,&a\equiv3\pmod4.
 \end{cases}
\tag{156.CA7}
\]

No parity, squarefree, primitivity, or coprimality hypothesis is imposed
on \(N\) or \(N/d\).

## 3. Proof or derivation

### 3.1 Literal variation of the zero Fourier coefficient

Write

\[
 I_+(V)=\{j\in\mathbb Z:V<j\le2V\},\qquad
 I_-(V)=\{j\in\mathbb Z:-2V\le j<-V\}.
\tag{156.CA8}
\]

For fixed physical \(x\), the map \(j\mapsto(x^2-j)/N\) is monotone on
each interval.  Sampling a zero-extended bounded-variation real profile
along a monotone sequence cannot increase its variation.  This charges
every profile component, transition, and half-open zero-extension jump
without assuming a bounded component count.

The residual phase has the exact rationalization

\[
 -\frac{j}{x+\sqrt{x^2-j}}=\sqrt{x^2-j}-x
\tag{156.CA9}
\]

and, on literal support,

\[
 \left|\frac{\partial}{\partial j}
 \bigl(\sqrt{x^2-j}-x\bigr)\right|
 =\frac1{2\sqrt{x^2-j}}\ll K^{-1}.
\tag{156.CA10}
\]

Its variation on either block is \(O(V/K)=O(1)\).  The cell has the
single positive cutoff \(j=x-1\) and the single negative cutoff \(j=-x\);
the strict block endpoints are charged by the endpoint term in discrete
Abel summation.  Product variation therefore gives, separately on
\(I_+\) and \(I_-\),

\[
 \sup_{j\in I_\pm}|B_j(x)|
 +\operatorname {Var}_{j\in I_\pm}B_j(x)
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{156.CA11}
\]

Summing over the \(O(KX^\varepsilon)\) physical integers proves

\[
 \boxed{
 \mathcal A_\pm:=
 \sup_{j\in I_\pm}|A_j|
 +\operatorname {Var}_{j\in I_\pm}A_j
 \ll_\varepsilon K M^{-3/4}X^\varepsilon.}
\tag{156.CA12}
\]

If a later character formula restricts to \(j=hn\), ordered-subsequence
variation contracts:

\[
 |A_{h(n+1)}-A_{hn}|
 \le\sum_{r=hn}^{h(n+1)-1}|A_{r+1}-A_r|.
\tag{156.CA13}
\]

Thus no factor \(h\) or endpoint loss appears.

### 3.2 Primitive conductors and all induced local factors

For a fixed odd \(d\mid N\), put \(m=N/d\), \(c=4m\), and write
\(m=u^2r\) with \(r\) squarefree, possibly even.  Define

\[
 \Delta_+=
 \begin{cases}r,&r\equiv1\pmod4,\\4r,&r\equiv2,3\pmod4,\end{cases}
 \qquad
 \Delta_-=
 \begin{cases}-r,&r\equiv3\pmod4,\\-4r,&r\equiv1,2\pmod4.\end{cases}
\tag{156.CA14}
\]

These are fundamental discriminants, their conductors
\(f_\pm=|\Delta_\pm|\) divide \(c\), and \(\Delta_+=1\) denotes the
primitive principal character of conductor one.  With
\(\alpha=(1+i)/2\), \(\beta=(1-i)/2\), and
\(\chi_\pm=(\Delta_\pm/\cdot)\),

\[
 K(0,-j;c)=
 \alpha G_{c,\chi_+}(-j)+\beta G_{c,\chi_-}(-j),
\tag{156.CA15}
\]

where

\[
 G_{c,\chi}(n)=
 \sum_{\substack{a\bmod c\\(a,c)=1}}\chi(a)e_c(an).
\tag{156.CA16}
\]

Indeed \(\epsilon_a=\alpha+\beta\chi_4(a)\),
\((4m/a)=(r/a)\), and
\(\chi_4(a)(r/a)=(-r/a)\) on units.

For a primitive constituent of conductor \(f\mid c\), put \(L=c/f\) and

\[
 R_f=\prod_{\substack{p\mid c\\p\nmid f}}p.
\tag{156.CA17}
\]

Inclusion-exclusion of the extra unit primes and grouping the lifts
modulo \(f\) give the exact global formula

\[
 \boxed{
 G_{c,\chi}(n)=
 \tau(\chi)
 \sum_{\substack{e\mid R_f\\L/e\mid n}}
 \mu(e)\chi(e)\frac Le\,
 \overline\chi\!\left(\frac{n}{L/e}\right).}
\tag{156.CA18}
\]

Equivalently, at \(p^\nu\Vert c\), if the primitive local conductor is
\(p^\kappa\) with \(\kappa>0\), the local factor vanishes unless
\(v_p(n)=\nu-\kappa\); on that support it is the exact lift
\(p^{\nu-\kappa}\tau(\chi_p)\overline{\chi_p}(n/p^{\nu-\kappa})\),
with the CRT unit and additive sign inserted.  If \(\kappa=0\), it is
the Ramanujan factor

\[
 c_{p^\nu}(n)=
 \begin{cases}
 0,&v_p(n)\le\nu-2,\\
 -p^{\nu-1},&v_p(n)=\nu-1,\\
 p^{\nu-1}(p-1),&v_p(n)\ge\nu.
 \end{cases}
\tag{156.CA19}
\]

For an odd \(p^e\Vert m\), odd \(e\) gives primitive conductor \(p\),
exact support \(v_p(j)=e-1\), and magnitude \(p^{e-1/2}\); even \(e\)
gives precisely (156.CA19).  At two, the primitive conductor exponent
is \(0\), \(2\), or \(3\).  If \(v_2(m)\) is even, the principal and
\(\chi_4\) pieces occupy the disjoint supports
\(v_2(j)\ge v_2(m)+1\) and \(v_2(j)=v_2(m)\).  If \(v_2(m)\) is odd,
the two \(\chi_{\pm8}\) pieces have
\(v_2(j)=v_2(m)-1\) and combine only on

\[
 \frac{j}{2^{v_2(m)-1}}\equiv3\pmod4,
\tag{156.CA20}
\]

where their combined two-adic magnitude is \(2^{v_2(m)+1}\).
The complete CRT phases and the values
\(\tau(\chi_4)=2i\), \(\tau(\chi_8)=\sqrt8\), and
\(\tau(\chi_{-8})=i\sqrt8\) are printed in the discovery and blind
reports.  The only global principal constituent occurs when \(m\) is a
square; it is the exact Ramanujan sum, not a square-root Gauss surrogate.

These local formulas certify every arithmetic stratum.  The final target
bound below can be proved more directly and does not spend their absolute
support capacity.

### 3.3 Exact recombination of every odd divisor stratum

Define the quotient-character root sequence

\[
 \mathscr S_N(j)=
 \sum_{x\bmod q}
 {\bf1}_{N\mid x^2-j}
 \chi_4\!\left(\frac{x^2-j}{N}\right).
\tag{156.CA21}
\]

The exact quotient selector is

\[
 {\bf1}_{N\mid t}\chi_4(t/N)
 =-\frac{i}{2N}
 \sum_{\substack{h\bmod q\\h\ {\rm odd}}}
 \chi_4(h)e_q(ht).
\tag{156.CA22}
\]

Partition each odd \(h\) uniquely by
\(d=(h,N)\), \(h=da\), so \(d\mid N\) is odd and
\(a\) is a unit modulo \(c=q/d\).  There are \(d\) lifts of
\(x\bmod c\) in \(x\bmod q\), and the exact even quadratic Gauss sum is

\[
 \sum_{x\bmod c}e_c(ax^2)
 =(1+i)\epsilon_a^{-1}\left(\frac ca\right)\sqrt c.
\tag{156.CA23}
\]

Since \(\chi_4(a)\epsilon_a^{-1}=\epsilon_a\), equations
(156.CA21)--(156.CA23) give

\[
 \boxed{
 \mathscr S_N(j)=
 -\frac{i(1+i)}{2N}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)d\sqrt c\,K(0,-j;c).}
\tag{156.CA24}
\]

Consequently the frozen row is exactly

\[
 \boxed{
 \mathcal Z_U(V)=
 \frac1q\sum_{V<|j|\le2V}A_j\mathscr S_N(j).}
\tag{156.CA25}
\]

As a physical local-factor check,

\[
 \mathscr S_N(j)=
 \rho_{4N}(j+N)-\rho_{4N}(j+3N),
 \qquad
 \rho_Q(t)=\#\{x\bmod Q:x^2\equiv t\pmod Q\}.
\tag{156.CA26}
\]

Thus the divisor recombination retains, rather than averages away, every
odd and two-adic root stratum.

### 3.4 Signed interval bound for the recombined sequence

Use

\[
 \widetilde{\mathscr S}_N(h)=
 \sum_{j\bmod q}\mathscr S_N(j)e_q(hj).
\tag{156.CA27}
\]

Changing variables \(t=x^2-j\) in (156.CA21) yields

\[
 \widetilde{\mathscr S}_N(h)=
 \left(\sum_{r\bmod4}\chi_4(r)e_4(-hr)\right)
 \left(\sum_{x\bmod q}e_q(hx^2)\right).
\tag{156.CA28}
\]

It vanishes for even \(h\).  If \(h\) is odd, put
\(d=(h,N)\), \(c=q/d\), and \(a=h/d\).  The first factor is
\(-2i\chi_4(h)\), while the second is

\[
 d(1+i)\epsilon_a^{-1}\left(\frac ca\right)\sqrt c.
\tag{156.CA29}
\]

Hence

\[
 \left|\widetilde{\mathscr S}_N(h)\right|
 =2\sqrt{2qd},\qquad d=(h,N),
\tag{156.CA30}
\]

and the zero Fourier coefficient vanishes.  Fourier inversion and the
exact geometric-progression bound therefore give, for every consecutive
integer interval \(I\) of length at most \(q\),

\[
 \begin{aligned}
 \left|\sum_{j\in I}\mathscr S_N(j)\right|
 &\ll \sqrt q
 \sum_{1\le h\le q/2}\frac{(h,N)^{1/2}}h\\
 &\ll \sqrt N\,\tau(N)\log(2N).
 \end{aligned}
\tag{156.CA31}
\]

The hypothesis \(|I|\le q\) is automatic because
\(|I_\pm|\le V\le K<N<q\).

There is an independent fixed-\(d\) control.  Opening (156.CA7) and
summing first in \(j\) gives

\[
 \sup_{I\ {\rm consecutive}}
 \left|\sum_{j\in I}K(0,-j;c)\right|
 \ll c\log(2c),
\tag{156.CA32}
\]

because every unit frequency \(a\bmod c\) is nonzero and the sum of the
geometric bounds is harmonic.  Abel summation with (156.CA12) and the
original \(d\)-sum again yields (156.CA4).  Thus the promoted estimate
does not depend on a delicate cancellation between divisor strata.

### 3.5 Abel summation and the complete power ledger

Apply discrete Abel summation separately on \(I_+\) and \(I_-\), using
(156.CA12), (156.CA25), and (156.CA31).  Since divisor and logarithmic
factors are absorbed into \(X^\varepsilon\),

\[
 \begin{aligned}
 |\mathcal Z_U(V)|
 &\ll_\varepsilon
 \frac1{4N}
 \left(KM^{-3/4}X^\varepsilon\right)
 \left(\sqrt N\,X^\varepsilon\right)\\
 &=M^{-1/4}X^\varepsilon.
 \end{aligned}
\tag{156.CA33}
\]

Both signs, the strict mask, all cell and profile endpoints, every
\(d\), every conductor and squareful stratum, and the entire exterior
normalization have been restored before the final power is assigned.
The older absolute upper capacity

\[
 \left(N^{-1/2}M^{-1/4}V+M^{-1/4}\right)X^\varepsilon
\tag{156.CA34}
\]

is not a lower bound.  Its top \(M^{1/4}\) term is removed by the proved
signed interval estimate and the literal variation norm.

## 4. First doubtful or unproved step

The claimant, blind, hostile endpoint, independent recombination, and
independent source derivations agree on the literal coefficient
variation.  The exact recombination has a fixed-\(d\) independent
cross-check.  No step remains unproved inside the zero row under the
accepted Round-154 profile hypotheses.

The first open object is now

\[
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)d\sqrt c
 \sum_{\substack{v\bmod(c/2)\\v\ne0}}
 \widehat B_j(2dv)K(-v^2,-j;c),
\tag{156.CA35}
\]

with its literal coupled coefficient, all sampled folds, both signs,
complementary frequencies, and every endpoint.  Neither (156.CA31) nor
(156.CA32) sums this matrix over \(v\).

## 5. Required controls and outcomes

| Control | Conductor outcome |
|---|---|
| literal_zero_mode_row | GREEN. Equations (156.CA3), (156.CA24), and (156.CA25) retain the exact row and every normalization. |
| exact_epsilon_two_character_decomposition | GREEN. Equations (156.CA14)--(156.CA16) retain both pieces and their complex coefficients. |
| primitive_conductor_and_induced_modulus | GREEN. Equations (156.CA14), (156.CA17), and (156.CA18) include conductor one and arbitrary induced modulus. |
| all_prime_power_two_adic_local_factors | GREEN. Equations (156.CA19)--(156.CA20) summarize the complete tables independently checked in the mathematics and source reviews. |
| valuation_support_and_squareful_strata | GREEN. Exact valuations, phases, repeated primes, and the principal Ramanujan branch are retained. |
| d_sum_and_full_normalization | GREEN. Equation (156.CA24) recombines every odd \(d\), and (156.CA25) retains the final \(q^{-1}\). |
| actual_Bhat0_j_variation | GREEN. Equations (156.CA8)--(156.CA13) derive the actual norm with no smooth or separated surrogate. |
| positive_negative_defect_and_endpoints | GREEN. The two literal integer blocks are treated separately and every endpoint is in the variation or Abel term. |
| N_M_V_d_conductor_power_ledger | GREEN. Equation (156.CA33) leaves no residual \(V,d,f\), or endpoint power. |
| source_theorem_zero_mode_match | GREEN. The promoted proof is finite and elementary; imported formulas and the optional Pólya--Vinogradov fallback have independent source checks. |
| upper_capacity_vs_signed_sum | GREEN. Equation (156.CA34) is explicitly an upper capacity; the gain comes from (156.CA31). |
| nonzero_and_downstream_scope | GREEN. Equation (156.CA35) and all broader owners remain open. |

No numerical experiment is used.

## 6. Dependencies and exact artifacts used

This candidate adjudication uses:

- strategy/round156_d1_outer_defect_zero_mode_strategy.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/barrier_packet.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/candidates/conductor_round156_zero_mode_seed.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/candidates/conductor_round156_zero_mode_target.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reports/zero_mode_local_factor_attack.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reports/blind_zero_mode_character_rederivation.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reports/zero_mode_character_source_audit.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reviews/hostile_profile_endpoint_round156_final.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reviews/independent_recombination_math_round156.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/reviews/independent_source_round156_final.md;
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reviews/conductor_round155_adjudication.md; and
- rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_root_dispersion_adjudication.md.

No graph, proof draft, validation matrix, synthesis, or campaign state is
changed by this candidate.

## 7. Recommended state effect

The three terminal reviews are GREEN.  Therefore:

1. promote the complete \(v=0\) row with the stronger bound
   \(M^{-1/4}X^\varepsilon\);
2. promote the exact primitive-conductor, induced-transform,
   prime-power, two-adic, squareful, root-sequence, and divisor-
   recombination identities;
3. retain the incomplete nonzero matrix as the first open
   \(D=d=L=1\) outer-defect interface;
4. reject the former absolute zero-row capacity as an unavoidable loss,
   reject a progression-variation obstruction for the literal profile,
   and retain arbitrary-weight counterexamples only outside the actual
   coefficient class; and
5. make no complete-range, scale-boundary, other-owner, endpoint-
   assembly, M9, bridge, target, or global-exponent change.
