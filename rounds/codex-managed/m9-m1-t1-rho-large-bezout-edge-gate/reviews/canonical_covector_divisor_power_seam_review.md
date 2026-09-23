# Round 192 canonical-covector/divisor/power seam review

- Campaign: m9-m1-t1-rho-large-bezout-edge-gate
- Round: 192
- Role: independent seam review
- Candidate reviewed:
  candidates/formalized_hard_m1_t1_rho_large_farey_covector_reduction.md
- Candidate SHA-256:
  9562954b65ac8c0f465b535e39d1c30724339098ef5a0d520507cd0983996cd5
- Numerical theorem evidence: none

## 1. Result and verdict

**PASS on the exact candidate bytes identified above.** No repair remains.
The candidate is consistent with the accepted Round-191 durable kernel, the
three finalized Round-192 reports, the conductor reconciliation, and the
finite diagnostic.

In particular, the current candidate contains the repairs needed at the
previously vulnerable seams:

1. (192.C4a) states the exact retained fast predicate and one nonempty
   power-of-two \(J\)-band.
2. (192.C12) is typed first at fixed-packet level and only then passed
   through the inherited linear outer assembly.
3. (192.C14) explicitly includes \(T\geq1\), so it cannot be invoked when
   the deliberately empty \(T=0\) selector leaves the whole Round-191
   remainder as core.
4. (192.C37) states the zero-extension and summability hypotheses required
   for the long-step Abel identity.
5. (192.C38)--(192.C40b) define the canonical anchor, wrap, affine-parity
   factor, and both endpoint number/divisor translations with the correct
   signs.
6. (192.C41) is restricted to the unsaturated ambient prime
   residue-universe control and retains the divisor slack
   \(X^{-\eta}\).

There is therefore no failed seam inequality in the reviewed bytes. The
first unproved mathematical step is intentionally still the signed estimate
for the exact core, (192.C15), or its stronger fixed-packet form
(192.C42). This is an open owner obligation, not a defect in the reduction.

## 2. Exact statement and hypothesis seam

The candidate freezes the correct Round-191 object. It retains

\[
 U=mq>4Q,\qquad q>Q,\qquad m|a|_q>Q,\qquad Qm<Y,
\]

\[
 U\mid u,\qquad g=u/U,\qquad
 \kappa,g,U\ {\rm odd},\qquad
 (u,v)=(U,h)=1,
\]

the literal carrier inequality, \(u\asymp v\asymp L/\kappa\), total
literal \(v\)-length \(O(u)\), and \(L\ll X^{1/4}\). The newly explicit
(192.C4a)

\[
 j_q(a,v)=|a\bar v_q|_q>T_Q,\qquad
 J\leq j_q(a,v)<2J
\]

is exactly the accepted fast projective predicate on one nonempty
power-of-two band. The projective predicate and all inherited masks only
delete rows in the later positive count.

The object selected by \(P_A\) is the Round-191 remainder after the
inverse-small, live-side terminal, and isolated Fejer projections. Both
orientations and every literal outer mask, affine site, birth/death, carry,
ordered endpoint field, square-root phase, and zero extension remain in one
complex aggregate before the single final real part. Thus there is no packet
or owner conflation.

## 3. Proof replay

### 3.1 Canonical normalization and nonvanishing

Because \(U\) is odd and \(v_0=[v]_U\) is a unit, its signed least inverse
\(\rho\) is unique in

\[
 -\frac{U-1}{2}\leq\rho\leq\frac{U-1}{2}.
\]

Writing \(\rho v_0-\beta U=1\), any common divisor of \(\rho,\beta\)
divides \(1\). Moreover:

- if \(\rho>0\), then \(0\leq\beta<\rho\);
- if \(\rho<0\), then \(\rho\leq\beta<0\), with equality
  \(\beta=\rho\) only at \((\rho,\beta)=(-1,-1)\).

Consequently

\[
 (\rho,\beta)=1,\qquad 0\leq\frac{\beta}{\rho}\leq1.
\]

For a literal representative \(v=v_0+nU\), the transport quotient is

\[
 \gamma=\frac{\rho v-1}{U}=\beta+n\rho.
\]

Thus the candidate correctly distinguishes canonical \(\beta\) from
literal \(\gamma\).

For \(1\leq c\leq A\leq U-1\),

\[
 \rho(cv_0-dU)=c+U(c\beta-d\rho)=c+U\ell_{c,d}.
\]

The right side is congruent to \(c\not\equiv0\pmod U\), hence is nonzero.
The strict inequality \(c<U\) is exactly the needed nonvanishing input.

### 3.2 Signed divisor multiplicity, \(\ell=0\), and literal repetitions

Fix \((c,d,\ell)\) and put \(N=c+U\ell\ne0\). Every admissible row maps to
a signed divisor \(\rho\mid N\). A prescribed signed least inverse \(\rho\)
determines at most one canonical unit class \(v_0\bmod U\). Hence

\[
 \#\{v_0\bmod U:\ell_{c,d}(v_0)=\ell\}
 \leq 2\tau(|N|).
\]

There is no additional factor for \(v_0\), \(\beta\), or the sign of
\(\ell\). When \(\ell=0\), \(N=c\ne0\), so the same count applies.

For \(|\ell|\leq T\),

\[
 0<|c+U\ell|<U^2\ll X^{1/2},
\]

because \(T\leq(U-1)/2\), \(c<U\), and
\(U\leq u\ll L\ll X^{1/4}\). For \(T\geq1\), the \(2T+1\) integral
values of \(\ell\) satisfy \(2T+1\leq3T\), so the elementary divisor
bound gives

\[
 \#\{v_0\bmod U:|\ell_{c,d}|\leq T\}
 \ll_\eta TX^\eta.
\]

This includes \(\ell=0\). At \(T=0\) this density estimate is not used:
\(\mathcal E_A\) is empty by definition.

The Farey family has the exact size

\[
 |\mathcal F_A|=2+\sum_{2\leq c\leq A}\varphi(c)
 \ll A^2\leq Q^{2C_0}.
\]

The inherited literal support is a fixed finite union of intervals of total
length \(O(u)\). Therefore a residue class modulo \(U\) occurs
\(O(u/U+1)\) times. Since \(U\mid u\), one has \(u/U\geq1\), and this is
\(O(u/U)\). The single union indicator counts an overlapping row once;
only the subsequent upper bound sums over covectors. Thus

\[
 \#\{v\ {\rm literal}:v\in\mathcal E_A\}
 \ll_\eta A^2\frac{uT}{U}X^\eta
 \leq A^2\frac{Qmu}{Y}X^\eta.
\]

All signs, the zero covector, union overlap, and literal repetitions are
therefore charged exactly once.

### 3.3 Fixed packet and replacement of terminal/Fejer pieces

At fixed parameters,

\[
 \mathscr R_{\rm fix}
 =\mathscr J_{\rm fix}
  -\mathscr J_{\rm inv,fix}
  -\mathscr J_{\rm terminal,fix}
  -\mathscr J_{\rm Fejer,fix}.
\]

The selector \(P_A\) is supported on \(|\rho|>T\), so
\(P_A\mathscr J_{\rm inv,fix}=0\). Endpoint-exact Abel inversion returns
\(P_A\mathscr J_{\rm fix}\) to the original row sum before any positive
count. Multiplying the preceding row count by \(O(Y)\) heights,
\(O(\kappa)\) sites, and \(O_\eta(X^\eta)\) literal endpoint weight gives

\[
 |P_A\mathscr J_{\rm fix}|
 \ll_\eta A^2Qm\kappa uX^{2\eta}.
\]

The accepted terminal and Fejer estimates are positive row-count bounds, so
restriction by \(P_A\) cannot enlarge them; their restricted total is
\(O_\eta(\kappa uX^\eta)\). Since \(A^2\) is a fixed polylogarithm, this
proves (192.C10) after a fresh epsilon allocation.

The exact fixed-level algebra is

\[
\begin{aligned}
 \mathscr J_{\rm safe,191,fix}+P_A\mathscr R_{\rm fix}
 ={}&\mathscr J_{\rm inv,fix}
 +(I-P_A)\mathscr J_{\rm terminal,fix}\\
 &+(I-P_A)\mathscr J_{\rm Fejer,fix}
 +P_A\mathscr J_{\rm fix}.
\end{aligned}
\]

Thus the complete original packet replaces the terminal and Fejer
projections on Farey-selected rows. They are not added a second time.
Applying the inherited linear outer assembly then gives the identically
typed global decomposition before the final real part.

### 3.4 Outer lift, divisor ledger, and powers

The exact inherited lift is

\[
 c_{mq}(ma)=m^{-1}c_q(a).
\]

It cancels the \(m\) in the fixed estimate before positive outer summation.
The coefficient mass contributes \(\log(2q)\), the disjoint power-of-two
bands contribute one logarithm, and

\[
 \sum_{mq\mid u}1\leq\tau_3(u).
\]

Since \(A^2\leq Q^{2C_0}\), the complete prefactor is exactly
\(Q^{2C_0+1}X^{2\eta}\), not a positive power of \(Y\), \(U\), or \(L\).
The remaining shell ledger is

\[
 Q^{2C_0+1}X^{2\eta}
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\tau_3(u)\log^{O(1)}(2u).
\]

Before the subpolynomial factors,

\[
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}\kappa u
 \ll L^2\log(2L).
\]

For a requested \(\varepsilon>0\), choose the local \(\eta>0\) with
\(2\eta<\varepsilon\), leaving a positive fresh budget for the fixed power
of \(Q\), \(\tau_3\), the coefficient/band logarithms, and
\(\log(2L)\). The connectors \(u\ll L\ll X^{1/4}\) then give

\[
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon.
\]

This exactly verifies (192.C30) and (192.C11). No positive power of \(Y\)
is hidden, the \(m^{-1}\) cancellation occurs at the correct stage, and no
extra \(Q\), \(L\), or \(X\) factor is missing.

### 3.5 Coverage, floors, and the \(T=0\) seam

Put \(r=|\rho|\), \(b=|\beta|\). Then
\(0\leq b\leq r\), \((b,r)=1\), and
\(|c\beta-d\rho|=|cb-dr|\).

If \(A\geq r\), the points \(0,b,\ldots,Ab\pmod r\) repeat and give a
zero determinant. If \(A<r\), the \(A+1\) points are distinct. Their
circular gaps are positive integers summing to \(r\), so one gap is at most
\(\lfloor r/(A+1)\rfloor\). The corresponding index difference has
\(1\leq c\leq A\), and the integer quotient may be chosen with
\(0\leq d\leq c\). Dividing \(c,d\) by their gcd preserves these
constraints and divides the determinant by the same positive integer.
Therefore

\[
 \min_{(c,d)\in\mathcal F_A}|c\beta-d\rho|
 \leq\left\lfloor\frac{r}{A+1}\right\rfloor.
\]

For \(T\geq1\), a core row has integral minimum at least \(T+1\), hence

\[
 r\geq(A+1)(T+1).
\]

Let \(M=(U-1)/2\in\mathbb Z\) and \(D=A+1\). The empty-core condition is
exactly

\[
 \left\lfloor\frac{M}{D}\right\rfloor\leq T.
\]

Indeed,

\[
 \left\lfloor\frac{M}{D}\right\rfloor\leq T
 \iff M<D(T+1)
 \iff M\leq D(T+1)-1
 \iff U\leq2D(T+1)-1.
\]

The current (192.C14) explicitly includes \(T\geq1\). At \(T=0\), it is
false as a conjunction, \(\mathcal E_A=\varnothing\), and the entire
Round-191 remainder stays in the core. Thus neither the floor criterion nor
the zero covector is misapplied. For \(T\geq1\), if \(r\leq A\), the
primitive pair \((c,d)=(r,b)\) gives \(\ell=0\) and correctly lies in the
safe union.

### 3.6 Phase, carry, endpoints, and the scoped method control

For \(v=v_0+nU\), \(d_v=cn+d\), and
\(\Delta=cv-d_vU=cv_0-dU\), the identities

\[
 \rho\Delta=c+U\ell,\qquad
 \gamma\Delta=d_v+v\ell,\qquad
 z_{\omega,v}^{\Delta}=e(\epsilon_\omega ac/q)
\]

are exact. For a finite or absolutely summable zero-extended sequence,
(192.C37) follows by a lawful change of variable and is only available
when \(z^\Delta\ne1\). It is a self-return, not a saving.

The canonical-anchor definition in (192.C38) gives

\[
 N_\omega(h;\Delta)
 =\theta_{\omega,c}(h)-\epsilon_\omega\ell,
\]

with
\(\theta_{+,c}\in\{-1,0\}\) and
\(\theta_{-,c}\in\{0,1\}\). The affine reindexing therefore changes parity
by \((-1)^{N_\omega}\), and the retained factor in (192.C40) has the
correct orientation sign. Direct substitution into the accepted Round-191
ordered endpoint pairs reproduces every entry of (192.C40a)--(192.C40b):
the plus orientation has positive number/divisor changes and the minus
orientation their reversed negative changes. The \(d_v+v\ell\) translation
is representative-dependent, while \(c+U\ell\ne0\). No endpoint mask,
cell, coefficient, phase, birth, or death may consequently be discarded.

Finally, (192.C41) is now quantitatively exact. In its explicitly
unsaturated ambient prime regime with \(T\geq1\) and an
\(\asymp U\)-class central universe, one covector meets only
\(O_\eta(TX^\eta)\) classes, so a coefficient-blind cover needs

\[
 M\gg_\eta\frac{U}{TX^\eta}
 \asymp\frac{Y}{Qm}X^{-\eta}.
\]

The \(X^{-\eta}\) divisor slack is present. This is only a
residue-universe and bounded-array method control; it asserts neither
literal lower mass nor failure of the desired signed core estimate.

## 4. First doubtful or unproved step

There is no doubtful or unproved step in the promoted reduction itself on
the reviewed bytes. The first deliberately unproved estimate is

\[
 \Re\mathscr R_{\rm core,Y,Q}^{\sigma}
 \ll_{B,C_0,\varepsilon}L^2X^\varepsilon,
\]

or the stronger fixed-packet estimate

\[
 |\mathscr R_{\rm core,fix}|
 \ll_{C_0,\varepsilon}Qm\kappa uX^\varepsilon.
\]

Nothing in the Farey separation, long-step Abel identity, mechanical carry,
ambient residue-universe control, or bounded-array capacity supplies the
needed signed correlation for the actual unequal endpoint translations and
literal coefficients.

**First seam issue:** none in the current bytes.

**Required fix:** none.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| exact Round-191 rho-large remainder | PASS. The candidate starts after exactly the three accepted Round-191 safe projections. |
| exact fast predicate and \(J\)-band | PASS. Current (192.C4a) states \(j_q>T_Q\) and one nonempty power-of-two band. |
| canonical \(v_0\), literal \(v\), transport \(\gamma\) | PASS. \(\gamma=\beta+n\rho\); \(\beta\) is canonical. |
| signed normalization | PASS. Both signs and the \((-1,-1)\) edge are correct. |
| \(c<U\) nonvanishing | PASS. \(c+U\ell\equiv c\not\equiv0\pmod U\). |
| signed divisor multiplicity | PASS. The injection gives at most \(2\tau(|c+U\ell|)\) classes. |
| \(T=0\), \(\ell=0\), cap, and floors | PASS. The selector is empty at \(T=0\); \(\ell=0\) is included only in the \(T\geq1\) density sector; (192.C14) has the correct local scope and exact equivalence. |
| Farey-family and union overlap | PASS. The family costs \(O(A^2)\); the union indicator counts a row once. |
| literal repetitions | PASS. \(O(u/U+1)=O(u/U)\) follows from the inherited interval support and \(U\mid u\). |
| terminal/Fejer replacement | PASS. (192.C27) replaces the two projections on selected rows and has no double count. |
| one outer real part and literal fields | PASS. Fixed and global objects are identically typed complex aggregates. |
| fixed \(Q,L,Y,X\) powers | PASS. The fixed Farey term is \(A^2Qm\kappa uX^{2\eta}\), with no \(Y\)-loss. |
| outer lift/divisor ledger | PASS. \(m^{-1}\) cancels \(m\); coefficient and band costs are logarithmic; \(\sum_{mq\mid u}1\leq\tau_3(u)\). |
| epsilon allocation | PASS. The exact outer prefactor is \(Q^{2C_0+1}X^{2\eta}\), and a fresh remaining epsilon budget pays every subpolynomial factor. |
| circular coverage and empty core | PASS. The bound and the floor equivalence are exact, including primitive reduction and endpoints. |
| phase/carry/endpoint identities | PASS. (192.C34)--(192.C40b) have the correct representative dependence and orientation signs and claim no saving. |
| full-cover method boundary | PASS. (192.C41) includes unsaturated scope and \(X^{-\eta}\) divisor slack. |
| downstream and exponent quarantine | PASS. No complete \(t=1\), \(t\geq2\), owner, parent, bridge, theorem, or exponent is promoted. |

I reran the archived WolframScript diagnostic. It reported
158 moduli, 7,804 unit rows, 365,696 covector-row identities,
305,844 fixed covector fibres, 462 small-modulus coverage rows,
7,804 circular-pigeonhole rows, 770 finite union bounds, and zero
failures. This remains diagnostic only and certifies no asymptotic estimate.
The candidate and durable kernel are strict UTF-8 and contain no forbidden
C0 control characters.

## 6. Dependencies and exact artifacts used

The review used these exact artifacts:

- protocol.md, SHA-256
  f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a;
- proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md,
  SHA-256
  7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2;
- the formal Round-192 candidate, SHA-256
  9562954b65ac8c0f465b535e39d1c30724339098ef5a0d520507cd0983996cd5;
- reports/farey_covector_sparse_sector_attack.md, SHA-256
  c853502a8ae8721b17c3c862a4d9b8865a80e7b2697e15950cd748b05227e2a8;
- reports/central_core_phase_hostile_audit.md, SHA-256
  9051b23d31cea5eff00a1aece7ef66f26d007c1c750d5ada2e2641808f771008;
- reports/blind_unimodular_covector_rederivation.md, SHA-256
  186081c5acb3896598b36f9edc18e683df1b5f5162261a46dfb4da6ffc00a461;
- reviews/conductor_round192_report_reconciliation.md, SHA-256
  b9f67f2645f11166d6f856f9936bbb375939bf8bb8899d91374c90a7a58b7d01;
- controls/farey_covector_finite_diagnostic_report.md, SHA-256
  1cb1d9f6dde261209528b5b78dc5e38104518d3b941e028b595270ea51906e8b;
- controls/farey_covector_finite_diagnostic.wls, SHA-256
  f7b48f27f9998f0b20c473bf822d3dad1fc4bc9d7de40bc0e2d67cf4c5506148.

The direct graph dependencies remain
M9-M1-hard-top-t1-fast-signed-inverse-transport-reduction and
Divisor-bound-elementary; all lift, band, shell, endpoint, and literal
connectors are inherited through the accepted Round-191 dependency chain.

## 7. Recommended state effect

**Promote the reviewed Farey-covector reduction as one subordinate
proved-internal node, byte-locked to the candidate SHA-256 above.** Retain it
only as a dependency and inconclusive evidence for the still-open hard-M1
small-\(t\) owner.

Keep (192.C15)/(192.C42) open. Make no status change to the complete
rho-large remainder, original \(t=1\), any \(t\geq2\) range, the hard or
smooth M1 parents, GAR, any M2 parent, endpoint uniformity, M9, either bridge,
the quarter target, or any exponent.
