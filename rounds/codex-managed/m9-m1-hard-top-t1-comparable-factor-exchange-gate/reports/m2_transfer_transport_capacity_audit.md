# Round 184 hostile M2-to-M1 transfer, transport, and capacity audit

- Campaign: m9-m1-hard-top-t1-comparable-factor-exchange-gate
- Task: m2_transfer_transport_capacity_audit
- Role: barrier/no-go
- Graph SHA-256: a8e0e5d84c0c5047e0c96f11128dd215ae035bdd4355bd68ad28dc87afe6cfbd
- Evidence status: candidate evidence only; no proof-state edit
- Allocation: 100% analytical/algebraic, 0% numerical

## 1. Result: direct-transfer no-go, exact finite connector

The finite product-preserving exchange algebra, the Boolean residual, the
ordered-divisor Abel identity, and the sliding Fejer identity all survive
after they are rederived for the hard-M1 \(t=1\) face.  They do not,
however, transfer the accepted M2 estimate as a theorem.

The first exact transfer mismatch is the coefficient/physical-window
interface.  In the M2 kernel the odd character-bearing and profiled
divisor \(d\) lies in

\[
 \sqrt N\leq d\leq2\sqrt N
\]

and the complete displayed amplitude is

\[
 \eta_L(d)\Phi\!\left(\frac d{H+1}\right)
 W\!\left(\frac{\sqrt{q_X}\,d}{2\sqrt N}\right).
\]

In hard M1 the character-bearing leg is \(v\), the frequency/profile leg
is \(u\), and

\[
 4u<v<16u,\qquad
 \frac{\sqrt N}{4}<u<\frac{\sqrt N}{2},\qquad
 2\sqrt N<v<4\sqrt N.
\]

Thus neither \(d=v\) nor \(d=u\) identifies the M2 physical window,
profile placement, character placement, or boundary faces with M1.  The
M2 common-cell \(C^1\) estimate and its collar enumeration therefore do
not literally imply their M1 analogues.  The permitted M1 artifacts prove
step-two bounded variation on a fixed primitive ray, but they do not prove
the allocation-direction estimate

\[
 |A_{N,\sigma}(u,v)-A_{N,\sigma}(u',v')|
 \ll_\kappa L^{-1/2}X^\varepsilon
 \tag{184.M2M1-cell}
\]

for the complete sign-dependent literal coefficient, nor do they list and
count every M1 floor, star, half weight, strict edge, hard sample,
real-\(X\) crossing, endpoint, and zero-extension mismatch.  This is the
first failed seam.  It is a failure of theorem transfer, not a
counterexample to (184.M2M1-cell).

Precisely, if (184.M2M1-cell) and the corresponding complete crossing
collar bound are supplied independently for M1, the canonical XOR sector
is target-safe by the same \(L^2\cdot L^{-1/2}=L^{3/2}\) ledger.  Its
exact complement is all no-pair products together with the neither/both
allocations for selected products.  For that complete residual there is
an exact literal sufficient connector: at \(R=\lceil L\rceil\), the
single aggregate signed short-shift correlation in (184.M2M1-Fejer)
below implies the \(L^{3/2}X^\varepsilon\) target.  That correlation is
unproved.  Shiftwise triangle, positive transport, a one-prime toggle,
normalized averaging of full involutions, and truncated Möbius
recombination all return the \(L^2X^\varepsilon\) capacity.

The resulting rigorous verdict is a narrow
hard-M1-\(t=1\) exchange/transport capacity or self-return no-go.  It does
not disprove the literal \(t=1\) estimate.

## 2. Exact statement and hypotheses

Fix real \(X\geq2\), one literal middle or lower hard-M1 residual shell
\(L\), and \(\sigma\in\{+1,-1\}\).  Put \(N=uv\), and let

\[
 \mathscr A_N=
 \{(u,v)\in\mathbb N^2:uv=N,\ (u,v)=1,\ v\ {\rm odd}\}.
\]

Let \(A_{N,\sigma}(u,v)\) be the complete hard-M1 literal coefficient,
including the predicate \(4u<v<16u\), and extend it by zero to every
\((u,v)\in\mathscr A_N\).  Thus every dyadic cutoff, \(\Phi\), \(W\),
normalized power, profile, floor, star, half weight, strict edge, hard
sample, real-\(X\) crossing, endpoint, and sign field remains inside
\(A_{N,\sigma}\).  The frozen scalar is exactly

\[
 \mathcal T_{L,X,\sigma}
 =\sum_N\mu^2(N)e(\sigma\sqrt{XN})
   \sum_{(u,v)\in\mathscr A_N}\chi_4(v)A_{N,\sigma}(u,v).
 \tag{184.M2M1-1}
\]

The accepted support and normalization give a containing integer interval
\(I_L\) of cardinality \(M_L\asymp L^2\),
\[
 A_{N,\sigma}\ne0\Longrightarrow N\in I_L,\quad u,v\asymp L,
 \qquad |A_{N,\sigma}(u,v)|\ll_\varepsilon X^\varepsilon.
 \tag{184.M2M1-2}
\]
This is an upper envelope only, not literal lower mass.

For fixed \(\kappa>0\), choose for every \(N\) at most one unordered pair
of distinct odd prime factors \(\{p_N,q_N\}\) satisfying

\[
 \chi_4(p_Nq_N)=-1,\qquad
 \left|\log\frac{q_N}{p_N}\right|\leq\kappa L^{-1/2},
 \tag{184.M2M1-3}
\]

using only \((N,L,\kappa)\), never the allocation \((u,v)\).  Write
\(\mathscr A_N^\oplus\) for allocations in which exactly one selected
prime divides \(v\), and set it empty when no pair was selected.

Two additional M1 hypotheses, not supplied by the M2 theorem, are exactly
what would make the strict-sector transfer valid:

1. On every common literal smooth cell,
   \[
   |A_{N,\sigma}(u,v)-A_{N,\sigma}(T_N(u,v))|
   \ll_{\kappa,\varepsilon}L^{-1/2}X^\varepsilon.
   \tag{184.M2M1-H1}
   \]
2. The complete zero-extension crossing set, including all named literal
   faces and missing partner legs, has weighted cost
   \[
   \sum_{\substack{N,\ (u,v)\in\mathscr A_N^\oplus\\
                   (u,v),\,T_N(u,v)\ {\rm in\ different\ cells}}}
   \bigl(|A_{N,\sigma}(u,v)|
        +|A_{N,\sigma}(T_N(u,v))|\bigr)
   \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.
   \tag{184.M2M1-H2}
   \]

Under (184.M2M1-H1)--(184.M2M1-H2), the exact XOR scalar is
\(O_{\kappa,\varepsilon}(L^{3/2}X^\varepsilon)\).  These are sufficient
hypotheses, not accepted M1 conclusions.

The literal M2/M1 interface audit is:

| Field | Accepted hard-M2 \(t=1\) kernel | Frozen hard-M1 \(t=1\) face | Outcome |
|---|---|---|---|
| Character leg | odd \(d\) | odd \(v\) | algebraically analogous |
| Physical cone | \(\sqrt N\le d\le2\sqrt N\) | \(4u<v<16u\) | different window |
| Profile leg | \(d\), also the character leg | \(u\), not the character leg | exact placement mismatch |
| \(W\)-argument | \(\sqrt{q_X}d/(2\sqrt N)\) | inherited \(W(\sqrt{4q_Xu/v})\) | different coordinate, though both move logarithmically by \(O(L^{-1/2})\) |
| Product power | \((L^2/N)^{3/4}\) | product-only normalized power inherited from the M1 transform | invariant under exchange |
| Outer phase | \(e(\sqrt{XN})\) | \(e(\sigma\sqrt{XN})\) | product invariant, but M1 requires both signs |
| Even branch | the factor \(2\) is on the complementary leg | \(v\) is odd, so the factor \(2\) is on \(u\) | parity is preserved by odd-prime exchange |
| Boundaries | explicit M2 half-open shell and divisor window | M1 frequency shell, strict \(4,16\) cone, floors, stars, half weights, hard sample, crossings | requires new exhaustive collar proof |
| Variation input | explicit fixed smooth \(\eta_L,W\) and \(C^1\) \(\Phi\) | only the complete opaque \(A_{N,\sigma}\) and fixed-ray BV are present in the permitted M1 evidence | no literal theorem transfer |

## 3. Proof or derivation

### 3.1 Exact \(t=1\) face and exchange algebra

The accepted primitive-ray coordinates give

\[
 t=G\sqrt{\frac{uv}{\operatorname{sf}(uv)}}.
\]

Thus \(t=1\) forces \(G=1\) and \(uv=\operatorname{sf}(uv)\); conversely
\(G=1\) and squarefree \(uv\) give \(t=1\).  Hence (184.M2M1-1) is
exactly the complete \(t=1\) face, wholly inside the \(G<G_0\) complement
of the Round-183 strict sector.  The allocation map has multiplicity one.

For a selected pair abbreviate \(p=p_N,q=q_N\).  On
\(\mathscr A_N^\oplus\), define

\[
 T_N(u,v)=
 \begin{cases}
  (up/q,\ vq/p),&q\mid u,\ p\mid v,\\
  (uq/p,\ vp/q),&p\mid u,\ q\mid v.
 \end{cases}
 \tag{184.M2M1-4}
\]

Squarefreeness and coprimality make both displayed pairs integral.
The selected bits are interchanged, so \(T_N^2=1\), there is no fixed
point, and every orbit has exactly two allocations.  Since \(p,q\) are
odd, the parity of both legs is unchanged.  Product, squarefreeness,
coprimality, \(N\), the product shell, the selector, and
\(e(\sigma\sqrt{XN})\) are invariant.  Moreover,

\[
 \chi_4(v')=\chi_4(v)\frac{\chi_4(q)}{\chi_4(p)}
 =\chi_4(v)\chi_4(pq)=-\chi_4(v).
 \tag{184.M2M1-5}
\]

The factor shell and the strict ratio cone need not be invariant
pointwise; this is why zero extension and (184.M2M1-H2) are essential.
Reindexing the complete ambient XOR set gives the exact identity

\[
 \sum_{\mathscr A_N^\oplus}\chi_4(v)A_{N,\sigma}(u,v)
 =\frac12\sum_{\mathscr A_N^\oplus}\chi_4(v)
  \{A_{N,\sigma}(u,v)-A_{N,\sigma}(T_N(u,v))\}.
 \tag{184.M2M1-6}
\]

No support-preservation assertion was used.

### 3.2 Conditional common-cell and collar power

Write \(\theta_N=\log(q/p)\).  On support, \(u,v\asymp L\), and

\[
 |u'-u|+|v'-v|\ll_\kappa L|\theta_N|+1
 \ll_\kappa L^{1/2}+1.
 \tag{184.M2M1-7}
\]

The product-only normalized power and outer phase are exactly invariant.
For the archetypal M1 smooth factors, an ordinary derivative
\(\|\eta_L'\|_\infty\ll L^{-1}\) would cost \(O(L^{-1/2})\);
bounded \(\Phi'\) costs

\[
 O\!\left(\frac{L^{1/2}}{H+1}\right)
 \leq O(L^{-1/2})
 \quad(L\leq H);
\]

and the argument of \(W(\sqrt{4q_Xu/v})\) is multiplied by
\(e^{\pm\theta_N}\), again costing \(O_\kappa(L^{-1/2})\).
Thus the familiar smooth factors have the correct formal power.

There are \(O(L^2)\) ambient ordered pairs in the fixed enlarged box.
Consequently (184.M2M1-H1) costs

\[
 L^2\cdot L^{-1/2}X^\varepsilon
 =L^{3/2}X^\varepsilon.
 \tag{184.M2M1-8}
\]

The cone edges alone can be crossed only in

\[
 |v-4u|\ll_\kappa L^{1/2}+1,\qquad
 |v-16u|\ll_\kappa L^{1/2}+1,
 \tag{184.M2M1-9}
\]

and a fixed vertical profile face only in
\(|u-\lambda L|\ll_\kappa L^{1/2}+1\).  Each such strip has
\(O_\kappa(L^{3/2}+L)\) lattice points.  The same count would apply to
each explicitly supplied fixed real-\(X\) ratio face.  What is absent is
an M1 artifact proving that this list exhausts every literal floor, star,
half weight, hard sample, crossing, endpoint, and sign-dependent face,
with the required ordinary/logarithmic seminorm on every remaining cell.
The M2 enumeration is for a different physical window and cannot fill
that gap.

If (184.M2M1-H1)--(184.M2M1-H2) are granted, (184.M2M1-6)--(184.M2M1-8)
prove the strict XOR target.  Without them, the identity has the full
\(L^2X^\varepsilon\) capacity.

### 3.3 Exact residual and ambient sign mass

If no pair is selected, put \(\rho_N(v)=1\).  If \(p,q\) are selected,
put

\[
 \rho_N(v)=1-\mathbf1_{p\mid v}-\mathbf1_{q\mid v}
              +2\mathbf1_{pq\mid v}.
 \tag{184.M2M1-10}
\]

This is \(1\) on the \(00\) and \(11\) bit patterns and \(0\) on the two
XOR patterns.  Hence the exact residual is

\[
 \mathcal T_{L,X,\sigma}^{\rm rem}
 =\sum_N c_{N,\sigma}^{\rm rem}e(\sigma\sqrt{XN}),
 \quad
 c_{N,\sigma}^{\rm rem}
 =\mu^2(N)\sum_{(u,v)\in\mathscr A_N}
    \chi_4(v)\rho_N(v)A_{N,\sigma}(u,v).
 \tag{184.M2M1-11}
\]

It contains every no-pair product and exactly the neither/both
allocations for every selected product.  There is no third class and no
eligible-pair density assertion.

Write \(N=2^{\nu_N}M_N\), \(M_N\) odd.  Before the physical coefficient
and zero extension are imposed, the residual sign mass is exactly

\[
 \sum_{v\mid M_N}\chi_4(v)\rho_N(v)
 =
 \begin{cases}
  \displaystyle\prod_{r\mid M_N}(1+\chi_4(r)),
      &\text{no pair},\\[5pt]
  \displaystyle(1+\chi_4(pq))
   \prod_{\substack{r\mid M_N\\r\ne p,q}}(1+\chi_4(r))=0,
      &\text{selected pair}.
 \end{cases}
 \tag{184.M2M1-12}
\]

The products are over odd primes.  The selected ambient cube is balanced,
but its \(00\) and \(11\) partners generally lie in different M1 physical
windows; (184.M2M1-12) is not a profiled-window estimate.  With no pair,
all-\(1\bmod4\) products have entirely positive divisor signs.

The M2 four-prime \(\{+,-,-\}\) physical control does not transfer
literally either: it uses two-prime representatives in
\([\sqrt N,2\sqrt N]\), whereas M1 asks the character leg to lie in
\((2\sqrt N,4\sqrt N)\).  Its \(L^{2-o(1)}\) count cannot be quoted as
M1 physical residual mass.  This does not rescue positive transport;
the accepted complete M1 coefficient-insensitive capacity is already
\(L^2X^\varepsilon\), and no selector-density theorem removes its
no-pair part.

### 3.4 Ordered-divisor transport

For fixed \(N\), order the ambient residual character legs
\(v_1<\cdots<v_s\), put \(u_i=N/v_i\),
\(\epsilon_i=\chi_4(v_i)\), \(C_j=\sum_{i\leq j}\epsilon_i\),
\(C_0=0\), and
\[
 a_i=\rho_N(v_i)A_{N,\sigma}(u_i,v_i),\qquad
 a_0=a_{s+1}=0.
\]
Then exact summation by parts gives, for real or complex \(a_i\),

\[
 \sum_{i=1}^s\epsilon_i a_i
 =C_sa_s+\sum_{j<s}C_j(a_j-a_{j+1})
 =-\sum_{j=0}^sC_j(a_{j+1}-a_j).
 \tag{184.M2M1-13}
\]

Since \(\sum_j(a_{j+1}-a_j)=0\), subtracting the midpoint of the range
of \(C_j\) yields

\[
 \left|\sum_i\epsilon_i a_i\right|
 \leq\frac12\operatorname{osc}(C_N)
       V_{N,\sigma},\qquad
 V_{N,\sigma}=\sum_{j=0}^s|a_{j+1}-a_j|.
 \tag{184.M2M1-14}
\]

Even if a separate M1 coefficient proof supplied
\(V_{N,\sigma}\ll X^\varepsilon\), positive Abel/triangle closure would
still require the genuinely weighted estimate

\[
 \sum_{N\in I_L}\operatorname{osc}(C_N)V_{N,\sigma}
 \ll_\varepsilon L^{3/2}X^\varepsilon.
 \tag{184.M2M1-15}
\]

The divisor bound alone gives only \(L^2X^\varepsilon\).  Ambient balance
in (184.M2M1-12), cemetery normalization, or bounded variation does not
prove (184.M2M1-15).

### 3.5 Exact Fejer short-shift connector

Extend \(c_{N,\sigma}^{\rm rem}\) by zero outside \(I_L\), set
\[
 z_N=c_{N,\sigma}^{\rm rem}e(\sigma\sqrt{XN}),
\]
and for every positive integer \(R\) define

\[
 \begin{aligned}
 \mathfrak E_{R,\sigma}^{\rm rem}
 &:={1\over R}\sum_{s\in\mathbb Z}
       \left|\sum_{j=0}^{R-1}z_{s+j}\right|^2\\
 &=D_{L,\sigma}
 +2\Re\sum_{1\leq r<R}\left(1-\frac rR\right)
   \sum_Nc_{N+r,\sigma}^{\rm rem}
       \overline{c_{N,\sigma}^{\rm rem}}
 e\!\left(
  \frac{\sigma\sqrt X\,r}{\sqrt{N+r}+\sqrt N}\right),
 \end{aligned}
 \tag{184.M2M1-16}
\]

where
\[
 D_{L,\sigma}=\sum_N|c_{N,\sigma}^{\rm rem}|^2
 \ll_\varepsilon L^2X^\varepsilon.
 \tag{184.M2M1-17}
\]

The last bound follows directly from
\(|c_{N,\sigma}^{\rm rem}|\ll_\varepsilon\tau(N)X^\varepsilon\)
on \(O(L^2)\) product rows.  A pair at gap \(r\) occurs in exactly
\(R-r\) sliding windows, so (184.M2M1-16) has no endpoint error.  Also
every \(z_N\) occurs in \(R\) windows and at most \(M_L+R-1\) windows
meet the support.  Cauchy gives

\[
 |\mathcal T_{L,X,\sigma}^{\rm rem}|^2
 \leq\frac{M_L+R-1}{R}\,
       \mathfrak E_{R,\sigma}^{\rm rem}.
 \tag{184.M2M1-18}
\]

At \(R=\lceil L\rceil\), the prefactor is \(O(L)\), and the diagonal
(184.M2M1-17) is exactly target-square safe.  Therefore the single
one-sided actual-direction assertion

\[
 \boxed{
 \Re\sum_{1\leq r<R}\left(1-\frac rR\right)
   \sum_Nc_{N+r,\sigma}^{\rm rem}
       \overline{c_{N,\sigma}^{\rm rem}}
 e\!\left(
  \frac{\sigma\sqrt X\,r}{\sqrt{N+r}+\sqrt N}\right)
 \ll_\varepsilon L^2X^\varepsilon}
 \tag{184.M2M1-Fejer}
\]

is a sufficient literal connector for the complete residual.  Opening
both coefficients gives exactly

\[
 u'v'-uv=r,\qquad 1\leq r<R\asymp L,
 \tag{184.M2M1-19}
\]

with both independently selected rows, both squarefree masks, both
coprimality and odd-\(v\) predicates, both cones, every coefficient field,
and both endpoint values retained.  There must be one aggregate real
part as displayed.  No modulus may be inserted around an individual
shift, allocation, selector status, or endpoint branch.

Equation (184.M2M1-Fejer) is not supplied by either accepted M2 kernel.
It is open already for the M1 \(t=1\) face.

### 3.6 Exact capacity and self-return controls

If the shifted products in (184.M2M1-16) are bounded positively, Cauchy
at each shift gives

\[
 \sum_{1\leq r<R}
 \left|\sum_Nc_{N+r,\sigma}^{\rm rem}
       \overline{c_{N,\sigma}^{\rm rem}}e(\cdots)\right|
 \leq (R-1)D_{L,\sigma}.
 \]

For \(R\asymp L\), this makes
\(\mathfrak E_R\ll L^3X^\varepsilon\), and (184.M2M1-18) gives only
\[
 |\mathcal T^{\rm rem}|\ll_\varepsilon L^2X^\varepsilon.
\]
Thus shiftwise triangle or an early positive norm returns exactly to
the coefficient-insensitive capacity; it loses the required
\(L^{1/2}\) scalar saving.

A one-prime \(p\equiv3\bmod4\) toggle is still more elementary.  If
\(r=v/u\in(4,16)\), moving \(p\) from \(v\) to \(u\) sends
\(r\) to \(r/p^2<16/9<4\); moving it from \(u\) to \(v\) sends
\(r\) to \(rp^2>36>16\).  Hence its two physical supports are disjoint.
Its difference is all leakage.  Averaging the resulting identities over
all such primes, or over any normalized family of sign-reversing full
divisor-lattice involutions, is only an exact rewriting of the original
coefficient and supplies no contraction.

The false selectors also behave correctly.  A prime product has no two
distinct odd primes to select.  A supported semiprime allocation has leg
ratio between \(4\) and \(16\), so its only two primes cannot satisfy the
\(O(L^{-1/2})\) closeness condition; if both are \(1\bmod4\), the
opposite-character condition fails as well.  If every odd prime factor
of \(N\) is \(1\bmod4\), no pair can be selected and every ambient
\(\chi_4(v)\) is \(+1\).  These are exact no-pair controls, not a density
or lower-mass theorem.

Finally, the Round-183 truncated Möbius kernel still has
\[
 K_{L,T}(b,u)=\mathbf1_{u=1}\quad(b>L,\ u<T),
\]
and its \(a<T\) core returns to the full literal product wave modulo
target-size corrections.  Appending that automatic recombination to the
exchange residual does not remove \(t=1\).

## 4. First doubtful or unproved step

The first unproved step in the proposed M2-to-M1 transfer is not the
finite involution.  It is the assertion that the complete hard-M1
coefficient satisfies (184.M2M1-H1) and (184.M2M1-H2) uniformly for
both \(\sigma\), every shell, and every real-\(X\) crossing and endpoint.
The accepted M2 estimate proves these assertions only for its explicitly
displayed \(d\)-profile in a different physical window.  The accepted
M1 primitive-ray BV statement varies the common gcd \(G\) along one ray;
it is not an ordinary/logarithmic derivative theorem for exchanging
prime factors between \(u\) and \(v\).  No permitted artifact supplies
the missing coefficient dictionary or exhaustive M1 face list.

If an independent literal M1 seam later proves
(184.M2M1-H1)--(184.M2M1-H2), the next and first residual analytic gap is
(184.M2M1-Fejer), equivalently
\(\mathfrak E_{\lceil L\rceil,\sigma}^{\rm rem}
\ll_\varepsilon L^2X^\varepsilon\).  Positivity gives only
\(\mathfrak E_R\ll L^3X^\varepsilon\).  Neither gap is a disproof of the
actual coefficient estimate.

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| exact_t1_face | **PASS.** \(t=1\) is exactly \(G=1\) and squarefree \(uv\), with multiplicity one. |
| literal_coefficient_and_zero_extension | **PASS for all finite identities; NOT ESTABLISHED for analytic transfer.** The opaque complete \(A_{N,\sigma}\) is never simplified, but its exchange-direction seminorm and exhaustive face list are missing. |
| capacity_L2_target_L_three_halves | **PASS.** Common cells need \(L^{-1/2}\); Fejer needs an \(L^2\) energy; positive shift control returns \(L^2\). |
| canonical_selector_allocation_independence | **PASS.** The selector uses only \((N,L,\kappa)\). No existence or density is inferred. |
| exchange_integrality_multiplicity_fixed_point | **PASS.** Squarefreeness gives an integral, two-cycle, fixed-point-free, multiplicity-one map. |
| product_phase_squarefree_coprime_parity_preservation | **PASS algebraically.** Product, phase, squarefreeness, coprimality, and parity are exact. The M1 factor shell and cone require zero-extension collars rather than pointwise preservation. |
| chi4_sign_reversal | **PASS.** Equation (184.M2M1-5) is exact. |
| common_cell_profile_variation | **FIRST FAILED TRANSFER SEAM.** The M2 \(C^1\) theorem is for the \(d\)-profile; no complete M1 proof of (184.M2M1-H1) is in the permitted evidence. |
| boundary_crossing_collar_count | **UNPROVED FOR M1.** Cone and fixed smooth faces have the right \(L^{3/2}\) formal count, but floors, stars, half weights, hard sample, crossings, endpoints, and missing partners have not been exhaustively enumerated. |
| exact_xor_residual | **PASS.** Formula (184.M2M1-10) leaves exactly no-pair plus selected \(00/11\) allocations. |
| no_pair_density_inference | **PASS.** Prime, semiprime, far-pair, and all-\(1\bmod4\) controls forbid any nonemptiness or positive-proportion inference. |
| one_prime_toggle_and_involution_average_self_return | **PASS as an obstruction.** A one-prime toggle has disjoint M1 cone supports; normalized full-involution averaging is exact self-return. |
| prime_semiprime_all_one_mod4_controls | **PASS.** They can have no eligible pair and no character cancellation; no physical density is claimed. |
| m2_to_m1_transfer_scope | **PASS only after rejecting direct implication.** The algebra is reusable, but the M2 sector estimate and four-prime physical count are not M1 theorems. |
| ordered_divisor_transport_identity | **PASS algebraically.** Equations (184.M2M1-13)--(184.M2M1-14) are exact; the weighted target (184.M2M1-15) is open. |
| fejer_short_shift_connector | **PASS as an exact sufficient reduction.** Equations (184.M2M1-16)--(184.M2M1-19) retain all endpoints; (184.M2M1-Fejer) is open. |
| no_positive_norm_or_shift_triangle | **PASS as a no-go.** Such a step gives only the \(L^2X^\varepsilon\) scalar capacity. |
| t_ge_2_and_near_resonant_quarantine | **PASS.** Nothing here treats \(t\ge2\) or the large-\(G\) near-half-integer-resonant complement. |
| complete_small_t_owner_quarantine | **PASS.** Even a conditional XOR sector or complete \(t=1\) estimate would not prove the complete small-\(t\) owner. |
| downstream_and_exponent_quarantine | **PASS.** No M1/M2 parent, endpoint uniformity, M9, bridge, theorem, or exponent changes. |
| no_in_round_pivot | **PASS.** The report remains on the frozen hard-M1 \(t=1\) interface. |

No numerical, symbolic, or web theorem evidence was used.

## 6. Dependencies and exact artifacts used

Only the assigned brief and its permitted context were used:

1. rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/briefs/m2_transfer_transport_capacity_audit.md;
2. protocol.md;
3. state/proof_obligations.yml, restricted to the active M1/M2 kernels, owners, bridges, and exponent nodes named by the campaign;
4. state/active_campaign.yml;
5. strategy/round184_m1_hard_top_t1_comparable_factor_exchange_strategy.md;
6. proofs/kernels/m9_m1_hard_top_small_t_primitive_ray_sector_and_truncated_mobius_self_return.md;
7. rounds/codex-managed/m9-m1-hard-top-high-radical-small-t-signed-contraction-gate/reviews/power_self_return_psc_seam_review.md;
8. proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md;
9. proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md;
10. rounds/codex-managed/m9-m2-hard-top-t1-near-square-divisor-involution-gate/synthesis.md;
11. rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/synthesis.md; and
12. rounds/codex-managed/m9-m2-hard-top-t1-residual-signed-divisor-transport-gate/reviews/transport_capacity_profile_power_source_review.md.

The exact accepted inputs used are the \(t=1\) primitive-ray identity,
product support \(N\asymp L^2\), the coefficient/divisor upper envelope,
the M2 finite exchange and residual algebra, the Round-164 sliding-window
identity, and the graph scope.  No unlisted source theorem was imported.

## 7. Recommended state effect

**Retain the exact finite identities and Fejer connector as inconclusive
candidate evidence; reject direct M2-to-M1 theorem transfer; make no graph
change from this report alone.**

In particular:

- do not attach the proved M2 close-prime sector as a proof of an M1
  sector;
- require an independent complete M1 proof of
  (184.M2M1-H1)--(184.M2M1-H2) before promoting even the strict XOR
  incidence sector;
- retain (184.M2M1-10)--(184.M2M1-19) as exact algebraic infrastructure,
  with (184.M2M1-Fejer) explicitly open;
- reject positive Abel, shiftwise triangle, early Gram/energy positivity,
  one-prime toggling, normalized full-involution averaging, M2 four-prime
  physical-count transfer, eligible-pair density, and truncated Möbius
  recombination as closures of the M1 residual; and
- keep the complete \(t=1\) face, \(t\ge2\) small-\(G\) incidences,
  large-\(G\) near resonance, the complete small-\(t\) owner, both direct
  M1 parents, every M2 owner, endpoint uniformity, M9, both bridges, the
  quarter theorem, and all exponent ledgers unchanged.

If the other Round-184 seams independently prove the full literal
coefficient/collar hypotheses but not (184.M2M1-Fejer), the narrow
terminal description supported here is
hard_m1_t1_exchange_transport_capacity_or_self_return_no_go, with at most
a separate strict XOR-sector candidate.
