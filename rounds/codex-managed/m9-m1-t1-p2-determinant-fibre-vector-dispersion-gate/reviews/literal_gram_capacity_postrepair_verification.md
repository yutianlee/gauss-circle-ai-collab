# Round-195 literal Gram/capacity post-repair verification

- Campaign: m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate
- Verdict: PASS
- Candidate SHA-256: cd0230f22b31f3454c975cf8b8625026687adba97a0d180e2556156bd990d0d7
- Conductor reconciliation SHA-256: 3ff78bbb5f491ec4dfb30ae05123dfcecf8a93e38e17d7fee1c124c5c45b9436
- Shared-state mutation: none

## 1. Result

PASS.  All requested repairs are mathematically consistent and mutually
compatible:

1. the fixed retained plus-mode ratio is
   \((-1)^{c_+(h;v)}e(a/q)\), while the full pre-Fourier parity ratio
   \(-1\) is asserted only after all anchor modes recombine;
2. the small-\(\kappa\) positive envelope is
   \(u\{\kappa+\min(Y,D_L)\}X^\varepsilon\);
3. the exact additional target-safe packet sector is
   \[
   \kappa<D_L,\qquad
   \min(Y,D_L)\le H_B\mathfrak m\kappa;
   \]
4. its packet complement has the strict reverse inequality;
5. squarefree support gives the stated \(U^\varepsilon\) quadratic-root
   control; and
6. the additional safe packet sector may be assembled absolutely to
   \(O(L^2X^\varepsilon)\) with no hidden \(Y,q,J,U,\mathfrak m\), or
   Fourier-lift power.

The new safe predicate selects whole fixed spectral packets.  It is
therefore distinct from the physical atom mask \(P_2\): the packet
selection causes no new height-difference commutator, while the existing
physical-mask commutator remains exactly (195.C18).

The candidate still does not prove complete \(P_2\).  The precise open
region is

\[
 P_{2,<D}\cap
 \{\min(Y,D_L)>H_B\mathfrak m\kappa\},
\tag{195.V1}
\]

and the coefficient-sensitive four-orientation Gram estimate there
remains unproved.

## 2. Exact statement and hypotheses

Fix the literal accepted Round-192 hard-\(M_1\), original-\(t=1\),
\(\rho\)-large core on one nonempty shell \(L\ge2\), with

\[
 Q=H_B,\qquad D_L=\lceil\sqrt L\rceil,\qquad
 U=\mathfrak m q,\qquad U\mid u,\qquad
 u\asymp L/\kappa.
\tag{195.V2}
\]

Both orientations, both frequency signs, both \(T\)-branches, the complete
anchor Fourier sum, every literal endpoint/event field, all zero
extensions, the physical-mask commutator, and the single outer real part
are retained.  The physical mask is

\[
 P_2=\mathbf1_{\{|d-gm|\le D_L\}}
     \mathbf1_{\{|d'-gm'|>D_L\}},
\]

with

\[
 P_{2,\ge D}=P_2\mathbf1_{\{\kappa\ge D_L\}},\qquad
 P_{2,<D}=P_2\mathbf1_{\{1\le\kappa<D_L\}}.
\]

For a fixed packet
\(p=(\kappa,u,\mathfrak m,q,a,J,\sigma)\), define

\[
 \mathcal P_{\rm cap}
 =\{p:\kappa<D_L,\ 
       \min(Y,D_L)\le H_B\mathfrak m\kappa\},
\]

\[
 \mathcal P_{\rm rem}
 =\{p:\kappa<D_L,\ 
       \min(Y,D_L)>H_B\mathfrak m\kappa\}.
\tag{195.V3}
\]

The claim verified here is

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D}W)|
 \ll u\{\kappa+\min(Y,D_L)\}X^\varepsilon,
\tag{195.V4}
\]

which implies the fixed target

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D}W)|
 \ll H_B\mathfrak m\kappa uX^\varepsilon
 \qquad(p\in\mathcal P_{\rm cap}),
\tag{195.V5}
\]

and, after the accepted fixed-to-outer assembly, an
\(O(L^2X^\varepsilon)\) bound for the union of
\(P_{2,\ge D}\) and the packets in \(\mathcal P_{\rm cap}\).

## 3. Proof or derivation

### 3.1 Fixed-height and all-height positive counts

For \(\kappa<D_L\), primitivity places the plus close affine variable in
one residue class modulo \(v\), and the minus close affine variable in one
residue class modulo \(U\).  Since

\[
 U,v\asymp L/\kappa,
\]

the close window has

\[
 O(1+\kappa D_L/L)=O(1)
\tag{195.V6}
\]

sites per row and height.  A fixed \(J\)-band has
\(O(uJ/q)\) literal projective rows.  Summing over the \(O(Y)\) heights
and applying the endpoint-exact anchor/Abel return \(q/J\) gives

\[
 (uJ/q)\,Y\,(q/J)X^\varepsilon
 \ll YuX^\varepsilon.
\tag{195.V7}
\]

Independently, the determinant interval and lower-close window give
\(O(D_L)\) selected physical atoms per row over the whole height block.
The same projective-row and anchor/Abel factors give

\[
 (uJ/q)\,D_L\,(q/J)X^\varepsilon
 \ll D_LuX^\varepsilon.
\tag{195.V8}
\]

Equations (195.V7)--(195.V8) bound the same newly masked contribution, so
it is at most

\[
 u\min(Y,D_L)X^\varepsilon.
\tag{195.V9}
\]

The accepted terminal and Fejer projections contribute
\(O(\kappa uX^\varepsilon)\).  The inverse-small sector is disjoint from
a core row, and the Farey-core indicator only deletes rows.  Recomputing
the exact event expansion after physical deletion retains current and
transported-previous atoms, births/deaths, and the mask commutator; each
is covered by the same finite-multiplicity counts (195.V7)--(195.V8).
Adding the accepted pieces proves (195.V4).

### 3.2 Exact safe packet split

On \(\mathcal P_{\rm cap}\), (195.V4) and
\(\min(Y,D_L)\le H_B\mathfrak m\kappa\) imply

\[
\begin{aligned}
 u\{\kappa+\min(Y,D_L)\}X^\varepsilon
 &\le u(1+H_B\mathfrak m)\kappa X^\varepsilon\\
 &\ll H_B\mathfrak m\kappa uX^\varepsilon,
\end{aligned}
\tag{195.V10}
\]

because \(H_B\mathfrak m\ge1\).  Equality belongs to the safe sector, so
the strict reverse inequality in (195.V1) is its exact packet complement.
The split is at the packet level and is disjoint from the physical split
at \(\kappa=D_L\).

### 3.3 Fixed-to-outer power ledger

The exact outer coefficient is

\[
 c_{\mathfrak m q}(\mathfrak m a)
 =\mathfrak m^{-1}c_q(a).
\tag{195.V11}
\]

Multiplying (195.V5) by (195.V11) cancels the complete factor
\(\mathfrak m\) before any positive outer sum.  The accepted coefficient,
divisor, and band ledgers are

\[
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q),\qquad
 \sum_{\mathfrak m q\mid u}1\le\tau_3(u),
\tag{195.V12}
\]

with only logarithmic costs from the \(J\)-bands and dyadic packet
partitions.  Therefore the safe packet union is bounded by

\[
 H_BX^\eta
 \sum_{\kappa\ll L}\ 
 \sum_{u\asymp L/\kappa}
 \kappa u\,\tau_3(u)\log^{O(1)}(2u).
\tag{195.V13}
\]

The restriction to \(p\in\mathcal P_{\rm cap}\), and the disjoint
restriction \(\kappa\ge D_L\), only delete nonnegative terms from this
ledger.  There is no summation cost for imposing a predicate on
\((Y,\mathfrak m,\kappa)\).

For \(V\asymp L/\kappa\), the standard divisor estimate gives

\[
 \sum_{u\asymp V}u\,\tau_3(u)\log^{O(1)}(2u)
 \ll V^2\log^{O(1)}(2V).
\]

Consequently (195.V13) is

\[
 \ll H_BX^\eta L^2
 \sum_{\kappa\ll L}\frac{\log^{O(1)}(2L)}{\kappa}
 \ll L^2X^\varepsilon,
\tag{195.V14}
\]

after the accepted fresh epsilon split and shell connector
\(L\ll X^{1/4}\).  Only fixed polylogarithms are absorbed.  In
particular:

- \(q/J\) has already canceled the projective density \(uJ/q\) in
  (195.V7)--(195.V8);
- \(\mathfrak m^{-1}\) cancels \(\mathfrak m\) in the fixed target;
- the \(a,q,\mathfrak m,J\) multiplicities are covered by
  (195.V12) and logarithms;
- \(Y\) occurs only in the safe packet predicate and contributes no
  positive summation power; and
- the Farey-core indicator is used as a row deletion, so no expansion
  into \(O(Q^{2C_0})\) covectors is needed for this absolute count.

Thus the additional absolute-capacity packet sector has a rigorous outer
\(L^2X^\varepsilon\) bound.

### 3.4 Anchor and squarefree repairs

For a retained plus mode, write its anchor factor as
\((-1)^tz_{+,v}^h\), with
\(z_{+,v}=e(a\overline v_q/q)\).  Under the legal step
\(S\mapsto S+1\), \(h\mapsto h+v\), the canonical anchor either does not
wrap or wraps once.  If \(c_+(h;v)\in\{0,1\}\) is that wrap, then

\[
 \frac{(-1)^{t+c_+}z_{+,v}^{h+v}}
      {(-1)^tz_{+,v}^{h}}
 =(-1)^{c_+(h;v)}e(a/q).
\tag{195.V15}
\]

This is exactly the repaired formula.  The physical \((-1)^S\) ratio
\(-1\) is recovered only after the full anchor-mode recombination.  In the
minus chart \(S,t\) do not change and

\[
 z_{-,v}^{U}
 =e(-a\overline v_qU/q)
 =e(-a\overline v_q\mathfrak m)=1.
\tag{195.V16}
\]

Finally, on nonzero literal support the endpoint divisor
\(\kappa gU\) is squarefree.  Hence \(U\) is squarefree and
\((\kappa,U)=1\).  For every prime \(p\mid U\), the congruence

\[
 \kappa v^2+\delta v+2h\equiv0\pmod p
\]

has at most two roots because its leading coefficient is nonzero modulo
\(p\).  The Chinese remainder theorem therefore gives at most

\[
 2^{\omega(U)}\ll_\varepsilon U^\varepsilon
\tag{195.V17}
\]

roots modulo \(U\).  The plus divisor-fibre bound is unchanged.  This is
an algebraic multiplicity control only and is not used to infer literal
mass or to close (195.V1).

## 4. First doubtful or unproved step

No requested repair fails.  The first unproved step is precisely a signed,
coefficient-sensitive estimate for the actual \(++,+-,-+,--\) Gram on
(195.V1), after exact same-site event recombination and before separate
positive orientation norms.

The repaired capacity estimate gives only an upper envelope.  It neither
provides a lower comparison for the Gram diagonal nor controls the
off-diagonal endpoint-vector products and square-root phases.  Therefore
no complete \(P_2\), owner, parent, bridge, theorem, or exponent conclusion
follows from this verification.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| plus retained-mode ratio | PASS.  Equation (195.V15) is carry-dependent and does not mix fixed-mode and fully recombined identities. |
| minus retained-mode ratio | PASS.  Equation (195.V16) is exactly one. |
| fixed-height close count | PASS.  Equation (195.V6) is uniform for \(1\le\kappa<D_L\). |
| full small-\(\kappa\) envelope | PASS.  The minimum of (195.V7) and (195.V8), plus the accepted \(\kappa u\) pieces, gives (195.V4). |
| packet safe/remainder complement | PASS.  Equality is safe and the strict reverse inequality is the exact remaining packet region. |
| packet selector/operator meaning | PASS.  It selects whole fixed packets and creates no new physical-mask commutator. |
| physical-mask operator | PASS.  The current/transported-previous mask difference remains in (195.C18) and all event sites are counted. |
| squarefree quadratic roots | PASS.  Squarefree \(U\) and \((\kappa,U)=1\) give (195.V17). |
| projective \(J/q\) ledger | PASS.  The \(uJ/q\) row density and \(q/J\) anchor/Abel factor cancel exactly. |
| Fourier lift and divisor ledger | PASS.  Equations (195.V11)--(195.V12) remove \(\mathfrak m\) and bound every \(a,q,\mathfrak m\) multiplicity. |
| additional sector outer sum | PASS.  Equations (195.V13)--(195.V14) give \(O(L^2X^\varepsilon)\) without a hidden \(Y\) or power loss. |
| capacity versus literal mass | PASS.  Only upper capacity is asserted. |
| owner and exponent quarantine | PASS.  Complete \(P_2\), the hard-\(M_1\) owner, all downstream nodes, and all exponent records remain unchanged. |

## 6. Dependencies and exact artifacts used

1. candidates/formalized_hard_m1_t1_p2_large_kappa_sector.md,
   SHA-256
   cd0230f22b31f3454c975cf8b8625026687adba97a0d180e2556156bd990d0d7.
2. reviews/conductor_round195_report_reconciliation.md,
   SHA-256
   3ff78bbb5f491ec4dfb30ae05123dfcecf8a93e38e17d7fee1c124c5c45b9436.
3. reviews/literal_gram_nogo_owner_scope_seam_review.md,
   SHA-256
   5b37315c66bd637c127cc8f3fddbb7f94ed14f9f94955c685f90a5960120c197.
4. proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md,
   SHA-256
   7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2.
5. proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md,
   SHA-256
   301e51dc49072ed8541fc1183f00a8cddc3768fba025e33289314004f8c38325.
6. proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md,
   SHA-256
   4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160.
7. reports/literal_p2_determinant_fibre_vector_attack.md,
   SHA-256
   c617c18c959792622e3df9fe3eb06f47ba61c6948be77f8617c83bda96302879.
8. reports/p2_gram_diagonal_collision_hostile_audit.md,
   SHA-256
   52de40ade4e243cca9e0c50edfee5f913c8120a488407b4f39fe951f22d9b8fb.
9. reports/blind_p2_determinant_fibre_rederivation.md,
   SHA-256
   29ae2a518cf61fe5f7f43369d4d51a52b71a535dae63717801874bf7ffc935df.

No numerical diagnostic was used.  No candidate, reconciliation, kernel,
shared state, synthesis, or sibling artifact was edited.

## 7. Recommended state effect

PROMOTE the repaired subordinate result, subject to the remaining required
campaign controls:

1. retain the whole \(P_{2,\ge D_L}\) sector as target-safe;
2. additionally retain the absolute-capacity packet sector
   \[
   \kappa<D_L,\qquad
   \min(Y,D_L)\le H_B\mathfrak m\kappa
   \]
   as fixed-packet and outer \(L^2X^\varepsilon\) target-safe;
3. record (195.V1) as the exact open packet complement;
4. retain the fixed-mode anchor repair and squarefree root bound as exact
   algebraic controls, without treating either as literal lower mass; and
5. leave complete \(P_2\), the hard-\(M_1\) owner, every parent and bridge,
   the Gauss-circle target, and the internal \(1/3\), accepted external
   \(0.3144831759740614\ldots\), and target \(1/4\) exponent records
   unchanged.
