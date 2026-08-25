# Round 150 final source and scope review

- Campaign: `m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate`
- Reviewed candidate: `candidates/conductor_round150_small_wrap_collar_and_large_wrap_boundary.md`
- Source report: `reports/variable_row_collar_source_audit.md`
- Mathematics review: `reviews/independent_conductor_round150_math_review.md`
- Role: terminal source-hypothesis and promotion-scope reviewer
- Terminal label: `strict_moving_coefficient_collar_range`

## 1. Result

The Round-150 kernel is **GREEN under its stated strict range**.

| Component | Verdict | Exact scope |
|---|---|---|
| Fixed-wrap core | **GREEN** | The exact incidence expansion, prefix-uniform half-weight norm, \(O_\varepsilon(DQX^\varepsilon)\) bound for every fixed centered wrap, and target-safe packet are internally proved. |
| Bounded-\(M\) edge | **GREEN** | The accepted Round-148 actual-profile formula and derivative ledger supply bounded variation; weighted second derivative and Abel summation give \(O_\varepsilon(RX^\varepsilon)\) per row. |
| Source-scoped large-wrap no-match | **GREEN as a source audit; the sum remains OPEN** | The four audited theorem interfaces do not directly estimate the literal growing-\(M\) large-wrap sum. This is not an impossibility theorem or a lower bound. |
| Downstream scope | **GREEN** | No growing-\(M\) full collar, generic complement, \(t\ge2\) layer, cross owner, M1/M2 completion, endpoint statement, M9, bridge, Gauss target, or exponent claim is licensed. |

The candidate and source report are strict UTF-8, LF-only, with no
forbidden control or zero-width characters.

## 2. Exact statement and hypotheses

Assume

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 DE\asymp M\le R^2,\qquad D\le\sqrt M,\qquad
 Q=2\sqrt{ND/E}\asymp\frac{DR^2}{\sqrt M}.
\tag{SR150.1}
\]

For the literal squarefree coefficient, including its exact finite prefix,

\[
 \sum_L\frac{|B_{d,U}(L)|}{\sqrt L}
 \ll_\varepsilon X^\varepsilon.
\tag{SR150.2}
\]

For every fixed centered wrap \(k\),

\[
 \mathcal A_{k,U}\ll_\varepsilon DQX^\varepsilon.
\tag{SR150.3}
\]

Hence every packet with

\[
 |\mathcal K|\ll 1+\frac{R^2}{Q}
 \asymp 1+\frac{\sqrt M}{D}
\tag{SR150.4}
\]

satisfies

\[
 \mathcal A_{\mathcal K,U}
 \ll_\varepsilon R^2DX^\varepsilon.
\tag{SR150.5}
\]

If \(M\le M_0\) for a fixed constant, the actual retained profile gives

\[
 |G_U(d)|\ll_{\varepsilon,M_0}RX^\varepsilon,\qquad
 \sum_{d\asymp D}\mu^2(d)|G_U(d)|^2
 \ll_{\varepsilon,M_0}R^2DX^\varepsilon.
\tag{SR150.6}
\]

No estimate is proved for the growing-\(M\) complement
\(R^2/Q\ll |k|\ll N/Q\) with literal \(\chi_4\), divisor incidence,
exact prefixes, and actual sampled profiles retained.

## 3. Proof and source derivation

For fixed \(k,L_1,L_2,h\), the elementary interval argument gives

\[
 \mathcal N_k(L_1,L_2;h)
 \ll \frac{Q\min(L_1,L_2)}h.
\tag{SR150.7}
\]

After the \(1/(L_1L_2)\) coefficient and harmonic \(h\)-sum, (SR150.2)
implies, for one row,

\[
\begin{aligned}
 \mathcal A_{k,U}(d)
 &\ll_\varepsilon QX^\varepsilon
 \sum_{L_1,L_2}
 \frac{|B_{d,U}(L_1)B_{d,U}(L_2)|}{\max(L_1,L_2)}\\
 &\le QX^\varepsilon
 \left(\sum_L\frac{|B_{d,U}(L)|}{\sqrt L}\right)^2
 \ll_\varepsilon QX^\varepsilon.
\end{aligned}
\tag{SR150.8}
\]

Summing \(O(D)\) rows proves (SR150.3), and (SR150.4) proves
(SR150.5). This is absolute and imports no external analytic theorem.

For bounded \(M\), the accepted actual profile is

\[
 \mathscr W_{d,U}(L/q)
 =\mathscr A_{D,E,U}\!\left(d,\frac{4NdL^2}{q^2}\right).
\tag{SR150.9}
\]

Writing \(q=LQy\) gives

\[
 e_0=\frac{4NdL^2}{q^2}=\frac{dE}{D}y^{-2}.
\tag{SR150.10}
\]

The accepted Round-148 ledger gives bulk logarithmic derivatives
\(O_j(1)\), radial-transition derivatives \(O_j(M^{j/2})\), and
cone-transition derivatives \(O_j(D^{j/2})\), with finitely many owned
transitions. When \(M\le M_0\), support forces \(D,E,L=O_{M_0}(1)\);
therefore

\[
 \|\mathscr W_{d,U}(L/\cdot)\|_\infty+
 \operatorname{Var}_{q\asymp LQ}\mathscr W_{d,U}(L/q)
 \ll_{\varepsilon,M_0}X^\varepsilon.
\tag{SR150.11}
\]

On a permitted class \(q=a+4Ln\), the phase
\(F(n)=NdL/(a+4Ln)\) has interval length \(Y\asymp R^2\) and

\[
 |F''(n)|=\frac{32NdL^3}{(a+4Ln)^3}\asymp R^{-2}.
\tag{SR150.12}
\]

The standard second-derivative theorem says

\[
 \sum_{n\in I}e(F(n))
 \ll_A Y\sqrt\lambda+\lambda^{-1/2},
 \qquad \lambda\le |F''|\le A\lambda.
\tag{SR150.13}
\]

An exact primary reference is Olivier Robert,
[*On van der Corput's \(k\)-th derivative test for exponential
sums*, Theorem 1](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf).
Discrete Abel summation yields

\[
 \left|\sum_{n\in I}w_ne(F(n))\right|
 \ll_A(\|w\|_\infty+\operatorname{Var}_I w)
       (Y\sqrt\lambda+\lambda^{-1/2}).
\tag{SR150.14}
\]

Equations (SR150.11)--(SR150.14) give \(O(RX^\varepsilon)\).
The \(O_{M_0}(1)\) permitted classes modulo \(4L\) retain \(\chi_4\),
oddness, and \((q,L)=1\) exactly. Thus the bounded-\(M\) edge is no
longer conditional on an unwritten variation claim.

For large wraps, the first source mismatch precedes any exponent
comparison: after exact incidence linearization, the two prefixes and two
samples remain joint functions of the row and cells. Hence the coefficient
is neither \(a(x)b(y)\) in Bombieri--Iwaniec's double large sieve nor four
separated weights in Bettin--Chandee's determinant corollary.
Duke--Friedlander--Iwaniec additionally requires product-smooth weights and
has an adverse natural error scale here; Reuss treats two pure squarefree
indicators at one fixed additive shift. These are direct-placement
mismatches only.

## 4. First doubtful or unproved step

The first unproved collar step is a joint signed estimate for (150.C29)
outside a packet satisfying (SR150.4). It must sum the growing wrap family
while retaining the exact row-cell atom, both prefixes, both profiles, the
literal \(\chi_4(L_1L_2r_1r_2)\), and the reciprocal phase.

Fixed-wrap absolute summation loses a factor \(R^2\) over the full centered
range, and separately summing fixed-shift divisor bounds is not target-sized.
Failure of the audited source placements proves neither that the signed sum
is large nor that no other theorem or recombination can estimate it.

## 5. Required controls and outcomes

1. **Fixed-wrap core — GREEN.** The all-\(L\) norm, interval length,
   \(h\)-sum, row sum, and packet cardinality give the displayed powers.
2. **Bounded-\(M\) edge — GREEN.** The explicit Round-148 profile and
   derivative scales prove (SR150.11); curvature and Abel prove (SR150.6).
3. **Source-scoped large-wrap no-match — GREEN.** Each cited source fails
   a printed coefficient, separation, smoothness, shift, or power
   hypothesis. No literature-impossibility inference is made.
4. **Downstream scope — GREEN.** The candidate retains all growing-scale
   and downstream owners listed in Section 1 as open.
5. **Encoding/formula control — GREEN.** Both reviewed Round-150 artifacts
   are valid UTF-8/LF and free of forbidden controls and zero-width text.

No numerical control was used.

## 6. Dependencies and exact artifacts used

Repository artifacts:

- `protocol.md`;
- `state/proof_obligations.yml` and `state/active_campaign.yml`, limited
  to active and downstream scope;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/candidates/conductor_round150_small_wrap_collar_and_large_wrap_boundary.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/reports/variable_row_collar_source_audit.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/reviews/independent_conductor_round150_math_review.md`;
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reports/signed_squarefree_reciprocal_attack.md`; and
- `rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-reciprocal-dispersion-gate/reviews/conductor_round148_adjudication.md`.

Primary theorem cards with exact hypotheses and direct placement checks are
in Section 2.3 of the source report. They use the original
[Bombieri--Iwaniec](https://www.numdam.org/article/ASNSP_1986_4_13_3_449_0.pdf),
[Duke--Friedlander--Iwaniec](https://www.math.ucla.edu/~wdduke/preprints/quadraticdiv.pdf),
[Bettin--Chandee](https://arxiv.org/html/1502.00769v1),
[Reuss](https://arxiv.org/abs/1212.3150v2), and
[Robert](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf)
papers. No failure to find a source is promoted to an impossibility
statement.

## 7. Recommended state effect

Close Round 150 under

\[
 \boxed{\mathsf{strict\_moving\_coefficient\_collar\_range}}.
\]

Promote the scoped arithmetic incidence expansion, the prefix-uniform
half-weight norm, the every-fixed-wrap bound, the target-safe packet, and
the bounded-\(M\) actual-profile edge. Record the large-wrap literature
result only as a source-scoped direct no-match.

Retain as open the growing-\(M\) large-wrap signed sum, growing-\(M\) generic
complement, signed \(RD\) scalar, every \(t\ge2\) layer, Round-138 cross
owner, remaining M1/M2 obligations, endpoint uniformity, M9, bridge, Gauss
target, and both exponent claims. No shared proof state is edited by this
review.
