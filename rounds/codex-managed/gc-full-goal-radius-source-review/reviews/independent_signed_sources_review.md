# Round 214 independent source and reconstruction seam

Campaign: `gc-full-goal-radius-source-review`.
Reviewer: `full_goal_harmonic_sources`, separately authorized NONBLIND seam.
Date: 28 September 2026 Asia/Shanghai.
Target: `reports/signed_radius_sources.md`.
Target SHA256:
`feb841a2f0305addd6b98caa88c8daad06b9dfca5784f2870dc56f789535fac0`.
The hash was checked before reading. The reviewer's own source report was
frozen at `50228227fa0f77a6ce944ea8e2fbfd8f1fe75ddad60662bf041a487dcb0cf4b3`
before any sibling read. This review does not edit either report.
Effort: entirely analysis and primary-source inspection; no experiments.

## 1. Result

**GREEN** on the assigned source/application/reconstruction seam at the
exact target hash. The two import failures are correctly located:
Chamizo admits the original growing shifts, but not the extra arithmetic
weight at the claimed cheap norm; the published Wessel--zur Verth
Theorem 1.8 fails its off-block rank hypothesis on the eight-variable
form and is not a theorem for the four-equation radius system.

The hypothetical error calculations are explicitly labeled and correctly
priced. No theorem, moment, parent, or exponent is promoted. The
certificate limitation is not a lower bound on actual signed energy.
No mandatory correction was found.

## 2. Exact scope and hypotheses checked

The review checks the literal four-factor correlation, its eight-factor
signed radius square, all original shifts and shell normalization, the
two external theorem statements, and the stated complete reconstruction.
It does not independently reprove accepted pre-214 sector estimates or
the external source proofs. The candidate density remains only a bounded
local candidate, not an asserted integer mean.

Primary source checks:

- [Chamizo, Theorem 1.1 and Corollary 1.5](https://arxiv.org/html/2009.01667v1)
  and its [published version](https://link.springer.com/article/10.1007/s00009-021-01959-3):
  the first branch is the prefix error \(d^\epsilon x^{2/3}\) when
  \(d^{117/64}\le x\), with the stated two-adic main coefficient.
- [Wessel--zur Verth, published Theorem 1.8](https://link.springer.com/article/10.1007/s00605-026-02189-z):
  one quadratic equation with identical nonnegative product coordinate
  weights, Conditions C/D/K/L1/L2 and smooth approximability. L1 requires
  off-block rank at least five after permutation. The error is
  \(A(B)^sB^{-2}(\log B)^{-K}\). The publisher dates this version
  9 September 2026.

These are the same two source interfaces under review, not new research
imports. The following application checks are independently derived.

## 3. Independent derivations and seam findings

### Chamizo: shift range, normalization, and weight cost

For \(d=2^\nu d_0\), \(d_0\) odd, the source's main coefficient is
\(8|2^{\nu+1}-3|\sigma(d_0)/d\), agreeing with the report and the
ordered signed representation convention. Substituting the permissible
Hecke exponent \(7/64\) into \(3/2+3\theta\) gives \(117/64\).

For \(N=T^\alpha\) and the report's fixed \(b=83/650\), the original
shifts obey \(d\ll NT^{-4b}\). Hence

\[
 d^{117/64}/N\ll T^{(53\alpha-468b)/64}.
\]

The largest exponent in the specified band is
\(-1649/5200<0\), obtained at \(\alpha=242/325\). Bounded factors,
rounding, and \(h+k\) are absorbed by this fixed margin. Thus claiming
that Chamizo excludes these growing shifts would be wrong; the report
correctly avoids that error. The separate radius difference \(n-m\)
can be of order \(N\) and is not covered by this calculation.

Writing the other two representation factors as \(A_n\), one has only
the available bound \(|A_n|\ll T^\epsilon\). Thus
\(\sum|A_{n+1}-A_n|\ll NT^\epsilon\). The full smooth oscillatory
weight has variation \(O(1+q)\), since \(R\psi'\asymp q/N\).
Discrete product variation is therefore \(O(T^\epsilon(N+q))\).
Here \(q\ll T^{76/325}\ll N\), so Abel applied to the prefix error
has the stated \(N^{5/3}T^\epsilon\) certificate. A restriction to a
short interval subtracts two prefixes at scale \(N\); it does not
replace the source's error by the short length to the power \(2/3\).

The two explicitly fictional four-factor controls have exponents
\(484/975+228/975=712/975\) and
\(484/975+76/975=560/975\), against \(4b=498/975\).
The excesses \(214/975\) and \(62/975\) are correct. They are prices
of hypothesized absolute transfers, not claimed lower bounds or source
consequences. Iterating the pair mean cannot establish independence or
the four-point local factor.

### Wessel--zur Verth: rank, systems, and domain

The four norm variables satisfy one relation
\(Q_0+Q_3-Q_1-Q_2=0\). Their ordered representations use eight real
coordinates, with diagonal quadratic matrix of signature \((4,4)\).
Every coordinate permutation has zero off-block matrix. Under any
invertible eight-variable change, an off-block matrix has at most four
rows or four columns; its rank still cannot reach five. This is a
coordinate-independent dimension obstruction to the specified theorem.

The eight norm variables in the radius square satisfy two parallelogram
relations plus equality of the two original shifts. These four
equations are linearly independent as equations in the eight norm
variables: the first two respectively contain \(Q_3\) and \(P_3\),
whereas the latter two independently constrain the first and second
shift. Thus there are four quadratic equations in sixteen representation
coordinates. A single linear combination is only a necessary equation;
summing squares makes a quartic. Neither operation invokes Theorem 1.8
on the actual energy.

The unit coordinate sequence has \(A(B)=B+O(1)\),
\(\kappa(q,h)=1/q\), bounded residue discrepancy, and square sum
\(B+O(1)\). Its cumulative function has a smooth linear approximation.
It satisfies the sequence conditions, but cannot repair L1. Dummy
coordinates either leave a singular form or change the solution set;
forcing them to zero is no longer that unit-weight specialization.

The actual norm-difference restrictions have widths \(L/N,K/N\),
depend jointly on coordinates, and retain the signed radius kernel.
They cannot be made a product coordinate domain or a source weight at
zero cost. The report correctly treats these as additional unresolved
requirements, rather than needing them for its earlier rank rejection.

### Thin volume, signed energy, and complete reconstruction

The free norm parameters are \((n,h,k)\) for the four-factor sum and
\((n,m,h,k)\) for its radius square, with scale volumes \(NLK\) and
\(N^2LK\). This does not assert an integer asymptotic. Even granting
the fictional full-system error \(N^4(\log N)^{-A}\), normalization
on a complete shell of size \(m_j\asymp LK\) gives upper-edge exponent
\((4\cdot242-114)/325=854/325\). The requested energy has exponent
\(\max(242,2\cdot242-3\cdot76)/325=256/325\). The quoted deficit
\(598/325\) follows. This is a deliberately more generous hypothesis
than the actual single-equation source, not a misquotation of it.

The radius kernel is exactly
\(e(5y/4)\sin(3\pi y/2)/(\pi y)\), with value \(3/2\) at zero.
Expanding \(|D-\rho I|^2\) retains DD, both conjugate mixed terms,
and CC. Its discrete diagonal has size \(O(NT^\epsilon)\), but the
off-diagonal is signed and is not upper-bounded by that diagonal.

From the inherited shell fractions, summing the \(\sqrt q\) recovery
against \(\sqrt N+Nq^{-3/2}\) costs
\(T^\epsilon(\sqrt{N\Lambda_*}+N/\Lambda_*)\). The global-envelope
tail, smooth model, small products and repeated shifts are explicitly
retained. At the upper comparison edge the two powers are
\(159/325\) and \(166/325\), agreeing with the report. The two
differencing diagonals have size \(T^{4b}\); taking the fourth root
and restoring \(\sqrt R\) produces only
\(1/4+b/2=102/325\) in squared radius, conditionally.

Finally, \(\sqrt{N\Lambda}+N/\Lambda\gg N^{2/3}\) for every
\(\Lambda>0\). At \(N=T^{3/4}\) this costs \(T^{1/2}\) in the
fourth-power certificate. Its fourth root and the two complementary
caps cannot certify a wave exponent below \(1/8\). The report correctly
labels this a limitation of that formula, not a theorem that actual
signed energy is large or a full optimization of every radius method.

## 4. First unproved step and qualifications

The complete signed eight-factor off-diagonal estimate (report (3.2))
remains unproved. The source exclusions neither establish nor refute it.
The bounded local density is not a proven global mean, and no source
proof or statement here changes that fact.

This GREEN verdict confirms the stated seam and scopes, not the truth of
the arithmetic input. The report's inherited modulo-four/local-product
control is not independently re-audited from its historical proof here;
it is not needed for either source rejection or the verified cost algebra.

## 5. Controls and outcomes

| Control | Verdict |
|---|---|
| Actual coefficient and main-term normalization | GREEN: two, four, and eight factors remain distinct; the two-adic pair constant is correct. |
| Growing shifts and local/global errors | GREEN: original shifts pass with fixed margin; short intervals do not improve a prefix error. |
| Quadratic form versus system | GREEN: rank ceiling four in eight variables; four equations remain four in the energy. |
| Thin support and signed kernel | GREEN: no product-weight or full-box error is silently transferred. |
| Complete shell norm, tails and reconstruction | GREEN: all factors and milestone exponent reproduced. |
| Certificate versus actual lower bound | GREEN: every lower comparison is restricted to its explicit positive certificate. |
| Whole-quarter scope | GREEN: fixed milestone and necessary certificate ceiling leave every full route open. |

No numerical experiments, statistical extrapolations, or source-internal
proof claims support this verdict.

## 6. Dependencies and exact artifacts used

Read for this separately assigned seam:

- The exact target report at the hash stated above.
- The two primary source URLs and the published Chamizo version linked
  in Section 2, specifically the theorem statements, coefficient
  conventions and defined source conditions.
- Already permitted context from the reviewer's completed task:
  `protocol.md`, the frozen graph/campaign, the Round-214 strategy,
  the 23 September strategy memo, Round-211 checkpoint, Round-213
  synthesis, the permitted full-frontier/source reports, and the
  accepted complete-square-root large-value kernel.

No blind packet or report was read. No new source family was audited.
Only this review artifact was written after the reviewer's own report
was frozen. Its conclusion binds the specified target bytes.

## 7. Recommended state effect

Accept the reviewed report as **GREEN strategy/source evidence** at its
final hash. Preserve its two scoped import failures, complete cost
ledger, and unproved signed gate. No graph promotion, parent closure,
pointwise improvement, or full-goal no-go is licensed. No report edit
is requested, and no successor round is designed or started.
