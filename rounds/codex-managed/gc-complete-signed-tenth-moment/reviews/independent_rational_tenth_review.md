# Independent nonblind review of the rational tenth-moment report

Campaign: `gc-complete-signed-tenth-moment`. Round: 209.
Role: independent NONBLIND seam reviewer, after completion of the separate
`actual_tenth_high_values` discovery assignment. This is not a statement-only
review and does not replace that control.
Generated: 2026-09-27T23:13:37+08:00.
Graph SHA-256: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.
Reviewed claimant: `reports/signed_fifth_convolution.md`.
Reviewed final SHA-256:
`3ad10212450a105eced8477cf5a162b1a9ac3613bf58bfcb0308a393e9e9bdda`.
Effort: entirely analytical; no mathematical numerical experiments or new source import.

## 1. Result and verdict

**GREEN for the two precisely scoped claims in the hash-bound report.**
The complete rational exact-diagonal upper bound

\[
 \mathcal D_{10}\ll_\epsilon XHQ^4T^\epsilon
     \ll_\epsilon T^{7+\epsilon}N^{-1/2}
\]

is valid, including both arms, all signs, nonpairing equalities, the actual
varying width and the strict moving prefix. The proof bounds the larger
termwise absolute exact-zero coefficient sum, so it also provides the
exact-zero majorant bound needed for subtraction.

The lower bound

\[
 \mathfrak A_{10}^{\mathrm{near},\ne0}\gg X^5H
       =T^{11}N^{-1/2}
\]

is valid for the stated **individual-integral absolute majorant**, after
every exact rational relation is removed. It does not lower-bound the
signed tenth moment, or an absolute majorant formed only after full signed
total-frequency aggregation. The report preserves that distinction.

No substantive mathematical repair is needed. The conductor repaired two
bare carriage-return characters in the odd-index labels of the elementary
totient formula; the displayed formula and this review use the repaired
saved artifact. No claimant or shared-state file was edited by this reviewer.
GREEN does not mean the complete tenth gate is proved: the report's signed
nonzero-total-frequency estimate remains open.

## 2. Exact hypotheses and object audit

The whole reviewed band is
\(T^{166/325}<N<T^{242/325}\), for real \(T\ge2\), with
\(X=T^2\), \(H=T/\sqrt N\), \(J=[X/2,3X]\) and
\(h(x)=2\sqrt x/\sqrt N\). Throughout the band,
\(h(x)\asymp H\), \(H=o(T)\), \(N/T\to0\) uniformly,
and \(T/H=\sqrt N\) grows by a fixed positive power.

I checked the inherited filter convention against the round-207 report:
\(F(u)=-\int_1^2a(t)\sin(2\pi tu)dt\),
\(\widehat F(\xi)=(i/2)\operatorname{sgn}(\xi)a(|\xi|)\),
with phase \(e(-\lambda x)\). The inherited partition is explicitly
nonnegative, \(v(t)=\phi(t/2)-\phi(t)\); together with \(\Psi(0)=1\)
this makes \(a\ge0\) on its whole support for sufficiently large \(T\)
and uniformly positive on a fixed interior interval. This whole-support
nonnegativity is essential to the near-majorant proof, not an assumption
about arbitrary real smooth weights. Bounded \(T\) is absorbed in upper
bound constants; the lower obstruction is asymptotic.

The original floor cutoff \(D=\lfloor\sqrt{\lceil6X\rceil}\rfloor\)
and \(L=\lfloor\lceil6X\rceil/(D+1)\rfloor\) are retained.
There is no covert replacement by the convenient even cutoff.
The reduced coefficient formulas are exactly the inherited formulas:

\[
 c^A_{a/q}=\frac{4h\chi_4(q)}q\widehat F(ha/q)s(D/q),
 \qquad
 c^B_{a/(4b)}=\frac{2ih\chi_4(a)}b
       \widehat F(ha/(4b))s_*(L/b,x/(Db)).
\]

The first denominator is odd; the second is divisible by four and reduced
because \(a\) is odd and \((a,b)=1\). Each active negative frequency is
the conjugate coefficient at the opposite frequency. The finite union
\(\Lambda\) contains every frequency active anywhere on \(J\), with
zero coefficients when inactive. Thus moving support never changes the
indexing of the moment expansion.

The second-arm cutoff is exactly \(j<x/(Db)\), not a closed or frozen
prefix. All nonempty prefixes \(\sum\chi_4(j)/j\) have size between
\(2/3\) and 1. Every argument below either uses this uniform pointwise
bound or selects only the first arm; none differentiates the prefix.

## 3. Independent derivation of the two claims and all powers

### Exact denominator arithmetic

Fix a real \(x\in J\). Fourier support and reduction imply

\[
 cH\le q\le Q,\qquad 0<|a|\le Cq/H,\qquad
 |c_{a/q}(x)|\le C H/q,\quad Q=\max(D,4L)\asymp T.       \tag{R1}
\]

Since \(q/H\gg1\) whenever active, the number of signed numerators
is \(O(q/H)\), with endpoints included. Inactive coefficients may be
discarded for this fixed \(x\); doing so only decreases an upper bound.
The bound holds uniformly through every moving-prefix jump.

Consider any exact ten-term rational relation obtained by expanding
\(\sum_\mu|C_\mu(x)|^2\). For a prime \(p\), clear the least common
multiple of the reduced denominators. If just one denominator has the
largest \(p\)-valuation, its numerator is a unit modulo \(p\) and its
cleared term is the only unit. Reduction modulo \(p\) contradicts the
zero relation. This argument is unaffected by signs or repeated terms.
Hence the maximal valuation occurs at least twice, and the denominator
product \(n=q_1\cdots q_{10}\) is squarefull.

Put the largest denominator into \((R/2,R]\), and designate one such
index. There are at most ten choices; a deterministic tie-breaking rule
also suffices. Now \(n\le R^{10}\). Every squarefull number has a unique
expression \(u^2v^3\), \(v\) squarefree: for each odd exponent at least
three, place one power in \(v\), and absorb the remaining even exponent
into \(u^2\). Thus the number of squarefull \(n\le R^{10}\) is
\(O(R^5)\). For a fixed \(n\), the number of ordered denominator
factorizations is at most \(\tau_{10}(n)\ll_\epsilon n^{\epsilon/10}\).
Consequently the number of possible denominator tuples is
\(O_\epsilon(R^{5+\epsilon})\). Ignoring their lower bounds, parity,
and the stronger maximal-valuation condition increases this count.

For each tuple, choose the other nine signed numerators first. The exact
linear relation then determines the designated tenth numerator uniquely
as a rational number; it contributes at most one choice if that number
is an admissible integer. In particular no divisibility or multiplicity
factor is missing. Multiplying the nine counts by all ten weights gives

\[
 \frac{C^{10}H^{10}}{q_1\cdots q_{10}}
       \prod_{j\ne j_0}\frac{Cq_j}{H}
 \ll H/q_{j_0}\ll H/R.                                 \tag{R2}
\]

The mass per dyadic maximum is therefore
\(O_\epsilon(HR^{4+\epsilon})\). Sum the geometric series over maxima
up to \(Q\), and choose the divisor-bound epsilon before its use.
This gives, pointwise for every real \(x\),

\[
 \sum_{\lambda_1+\cdots+\lambda_5=\lambda_6+\cdots+\lambda_{10}}
       \prod_{j=1}^{10}|c_{\lambda_j}(x)|
 \ll_\epsilon H Q^4T^\epsilon.                          \tag{R3}
\]

Expanding the grouped exact energy and taking absolute values only inside
that exact expansion proves the desired \(\mathcal D_{10}\) bound.
Also, for exact tuples,
\(\sum|\int_J\prod c\,dx|\le\int_J\sum\prod|c|\,dx\).
Thus (R3) bounds the entire termwise integrated exact-zero majorant by
\(O_\epsilon(XHQ^4T^\epsilon)\), not merely the possibly smaller
grouped diagonal. This distinction is exactly what the later subtraction
requires.

There is no extension of this argument to a nonzero rational sum: after
clearing denominators its right side need not vanish modulo the selected
prime. The report correctly avoids that extension.

### Actual nonzero-near majorant

The first-arm core uses odd \(D/2\le q\le D\), and reduced numerators
in a fixed interior interval of length comparable to \(q/H\). For each
denominator, elementary Mobius inversion gives

\[
 \#a=(v'-u')\varphi(q)/(2H)+O(\tau(q)).
\]

Inserting \(\varphi(q)=q\sum_{d\mid q}\mu(d)/d\) and summing odd
multiples gives
\(\sum_{q\le Y,\ q\ {\rm odd}}\varphi(q)=c_oY^2+O(Y\log(2Y))\),
where \(c_o=\tfrac14\prod_{p\ {\rm odd}}(1-p^{-2})>0\).
Differencing at \(D/2\) and summing the divisor errors proves a core
cardinality \(\asymp D^2/H\). Its main term dominates the
\(O(D\log D)\) error because \(D/H\asymp\sqrt N\gg T^{83/325}\).

On a fixed neighborhood \(J_0\) of \(X\), continuity of the actual
width keeps these Fourier arguments inside the positive amplitude core.
For each core frequency,
\(c_\lambda(x)=i\chi_4(q)b_\lambda(x)\), where
\(b_\lambda\ge0\) on **all** \(J\) and
\(b_\lambda\ge cH/D=:w_\lambda\) on \(J_0\).
Thus \(\sum w_\lambda\asymp D\). No width is frozen in the integral.

The ordered fifth sums lie in an interval of length \(O(1/H)\). Bins
of width \(\zeta/X\) number \(O(X/H)\). If \(m_j\) is the total
product weight of the ordered fifth tuples in bin \(j\), Cauchy gives

\[
 \sum_j m_j^2\gg D^{10}H/X.                             \tag{R4}
\]

For a same-bin pair the difference satisfies \(|\Delta|\le\zeta/X\).
The product of the five coefficients and the five conjugates has fixed
character sign, since \(i^5(-i)^5=1\). After removing that sign and
multiplying the integral by the unit scalar \(e(X\Delta)\), its real
part is an integral of
\(\prod b_\lambda(x)\cos(2\pi(x-X)\Delta)\).
Choose, for example, any fixed sufficiently small \(\zeta\le1/24\).
Since \(|x-X|\le2X\) on \(J\), the cosine is at least \(1/2\)
throughout \(J\). No part outside \(J_0\) can cancel its contribution,
and each absolute integral is at least \(cX\prod w_\lambda\).
Multiplying (R4) by \(cX\) yields \(\gg D^{10}H\asymp X^5H\).

This initially counts exact and nonexact same-bin pairs. The **entire**
exact-zero absolute contribution is at most (R3) integrated over \(J\),
and relative to \(D^{10}H\) it is

\[
 O_\epsilon\left(\frac{XQ^4T^\epsilon}{D^{10}}\right)
       =O_\epsilon(T^{-4+\epsilon}).                     \tag{R5}
\]

Choose a fixed epsilon less than four. For large \(T\), subtracting
this upper bound leaves a positive fixed proportion of the original
lower bound. Both quantities being subtracted are positive majorants,
so no signed-subsum fallacy occurs. The surviving pairs are genuinely
nonzero and obey the stipulated near relation. Repeated frequencies and
nonpairing exact relations were all covered by the subtraction.

### Constant-phase fibre and costs

For fixed odd \(q\), a product of five positive first-arm coefficients
has phase \(i^5\chi_4(q)^5=i\chi_4(q)\), independent of numerator.
The two stated numerator multisets both sum to \(5a\). At
\(q=3^k\), \(3\mid a\), their offsets \(-2,-1,1,2\) are units
modulo three, so all are reduced; their multisets differ. Choosing
\(D/3<q\le D\) and using \(q/H\to\infty\) places them inside a
fixed positive interval for large \(T\). The control therefore refutes
numerator-character orthogonality in this restricted fibre. It does not
prove that contributions from other denominators or the other arm cannot
cancel the resulting term in the full coefficient \(C_\mu\).

Finally, the exact part has power
\(XHQ^4=T^7N^{-1/2}\), which is below the target
\(T^{473/65}N^{-1/2}\) by \(T^{18/65}\). The near absolute majorant
has power \(X^5H=T^{11}N^{-1/2}\), larger by \(T^{242/65}\).
The inherited threshold error obeys
\(\|R_N\|_{10}^{10}\le\|R_N\|_\infty^4\|R_N\|_6^6\ll TH\).
After the physical bridge, tenth amplitude and Jacobian contribute
\(T^{-5}T^{-1}=T^{-6}\), so this error costs
\(T^{-4}N^{-1/2}\). The separate radial error costs
\(T^{-4+\epsilon}N^{-10}\). These are both target-safe.

## 4. First unproved step and scope of the remaining estimate

The first unproved step is exactly the report's full signed bound

\[
 \left|\sum_{\mu\ne\nu}\int_J
    C_\mu(x)\overline{C_\nu(x)}e(-x(\mu-\nu))\,dx\right|
 \ll_\epsilon T^{473/65+\epsilon}N^{-1/2}.                \tag{R6}
\]

The offdiagonal is real but need not be nonnegative. Once the exact part
is bounded as above, an upper bound for the full tenth moment and (R6)
are equivalent at the displayed scale: use
\(\mathcal O_{10}=\int|Q_N|^{10}-\mathcal D_{10}\) and the triangle
inequality in either direction. Thus the absolute value on the total
offdiagonal is legitimate and does not impose an extra unpriced target.

The report retains both inherited complete upper terms
\(T^7N^{-3/110}\) and \(T^{6+8\omega}\), and their two deficits.
Its exact-diagonal success is not represented as an improvement of the
complete moment. Neither the squarefull argument nor the actual near
majorant lower bound estimates (R6). No global impossibility claim is
licensed or made.

## 5. Controls and outcomes

- **Denominator counting: PASS.** The necessary maximal-valuation rule,
  squarefull product count, fixed-order divisor multiplicity and dyadic
  maximum sum all have their required factors.
- **Numerator and collision accounting: PASS.** Nine signed numerator
  choices determine the tenth uniquely. All signs, arms, ordered tuple
  multiplicities and single-frequency collisions are retained.
- **Real width and prefix: PASS.** Bounds are pointwise in real \(x\);
  the strict prefix is never differentiated, discretized or replaced.
  Inherited tail and threshold errors include equality points and
  partially intersecting endpoint bumps.
- **Actual near obstruction: PASS.** The coprime core has the claimed
  size and actual constant-phase coefficients. Nonnegativity on the
  entire interval prevents exterior cancellation inside each absolute
  integral. Exact-zero subtraction uses the larger termwise exact bound.
- **Nonpairing and constant-phase control: PASS.** The explicit tuples
  are valid; the conclusion is restricted to the selected same-denominator
  fibre. Pairing is not used in the exact estimate.
- **Signed/absolute scope: PASS.** The near lower bound concerns only
  individual-integral absolute values, not \(\int|Q_N|^{10}\) and not
  a norm formed after signed fifth-frequency aggregation.
- **All powers and full target: PASS.** Interval length, ten factors,
  errors, \(T^{-6}\) conversion and both existing terms are correct.
  The supplied local reproduction factor \(N^{1/20}\), outer blocks,
  singleton, infinite tail and sharp reconstruction are still required.
  A future proof of (R6) on the whole band would yield only \(102/325\),
  not one quarter or a direct M1/M2 theorem.
- **Independent-control label: PASS as NONBLIND review only.** This
  artifact does not impersonate the isolated statement-only task.

## 6. Dependencies and reviewed artifacts

The primary reviewed artifact is the round-209 claimant report at the
SHA-256 given above. Its actual rational representation, positivity and
threshold claims were checked against these explicitly cited round-207
artifacts:

- `rounds/codex-managed/gc-signed-rational-filter-attack/reports/signed_rational_moment_attack.md`, especially its exact filter, two-arm formulas, collision grouping and threshold analysis.
- `rounds/codex-managed/gc-signed-rational-filter-attack/controls/conductor_rational_norm_ledger.md`, especially the floor-cutoff error, moving prefix, all-frequency envelope and width accounting.
- `rounds/codex-managed/gc-signed-rational-filter-attack/reports/periodic_hyperbola_attack.md`, inspected as an inherited convention and threshold consistency source; no additional theorem is imported from its separate signed estimate.

The protocol and active round-209 context were already read for the
completed discovery assignment. This separate seam review does not rely
on that assignment's candidate arithmetic claims. The full-target and
physical reconstruction comparisons use the supplied reviewed round-208
bridge and frozen round-209 target already in that context.

The finite prime-valuation argument, squarefull count, unique numerator
step, ten-factor binning and subtraction have been rederived above rather
than accepted on claimant authority. No web theorem, numerical experiment
or unprovided source is used. The conductor's reported formatting-only
repair was checked in the saved text before binding this hash.

## 7. Recommended state effect

The conductor may retain or promote the **scoped exact rational diagonal
lemma** and the **scoped nonzero-near individual-integral majorant
obstruction**, subject to the protocol's remaining independent controls
and graph validation. This review supplies a GREEN mathematical seam
assessment only; it does not itself change accepted state.

Keep the complete actual signed tenth gate, the pointwise benchmark,
M1/M2 parents and the full quarter theorem open. Preserve (R6) as the
precise signed residual. No shared state, claimant report, earlier
discovery report or successor artifact was edited. This review stops here.
