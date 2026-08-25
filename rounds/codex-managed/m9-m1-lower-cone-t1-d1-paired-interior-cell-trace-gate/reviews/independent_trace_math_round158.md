# Independent trace-mathematics review

- Campaign: m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate
- Round: 158
- Role: independent seam review
- Starting graph: 3acbfaf6fb95047babd19800dee4152fb60cb408197a8ceac93931a20c57491f

## 1. Result

**Recommendation: revise, with narrow promotion candidates only; do not
promote a whole-trace target or a global claim.** The supplied
derivations correctly isolate a moving-cell trace and reduce its only
uncontrolled part to a strict, boundary-frozen character/mask sum.
They also establish target-safe separate bounds for the two removed
frequency *trace pieces* and a target-safe endpoint subrow. No
supplied argument proves the remaining strict sum at the required raw
\(M^{3/4}\) scale.

The rigorous route-scoped conclusion available from these materials is
that endpoint roots, cardinality, ordinary one-variable BV, and the
displayed standard discrepancy/completion placements do not close this
strict trace. This is not a lower bound and not a no-go against a new
joint signed theorem for the literal two-profile coefficient.

## 2. Abel signs, moving atoms, and outer terms

For the positive block, finite Abel summation with
\(P_j^+=\sum_{s=a_+}^jK_{d,v}(s)\) gives

\[
\sum_{j=a_+}^{b_+}A_jK_{d,v}(j)
=A_{b_+}P^+_{b_+}+
\sum_{j=a_+}^{b_+-1}(A_j-A_{j+1})P^+_j.
\]

Since the moving contribution to \(A_{j+1}-A_j\) is
\(-F_j(j+1)e_c(-2v(j+1))\), its contribution to this Abel formula is
positive. For the negative block,

\[
\sum_{j=a_-}^{b_-}A_jK_{d,v}(j)
=A_{a_-}P^-_{a_-}+
\sum_{j=a_-+1}^{b_-}(A_j-A_{j-1})P^-_j,
\]

and the moving contribution to \(A_j-A_{j-1}\) is
\(+F_j(-j)e_c(2vj)\), again producing the positive trace sign.
Thus the trace formula itself has the advertised signs and ranges.

The two outer terms are respectively
\(A_{b_+}P^+_{b_+}\) and \(A_{a_-}P^-_{a_-}\); the profile-difference
remainders also have the signs displayed in the discovery report.
They are not terms of the *defined moving-cell trace*, so their
quarantine is legitimate. They are nevertheless not proved
target-safe for the larger paired matrix, and must not be absorbed
into any trace theorem or downstream owner.

## 3. Full-frequency normalization and the removed rows

The half-period identity

\[
\sum_{v\bmod H}e_c(-2vx)K(-v^2,-s;c)
=\frac{1-i}{2}\sqrt c\sum_{u\bmod c}^{*}
\chi_4(u)e_c(u(x^2-s))
\]

has the correct exterior normalization: multiplying by
\(-i(1+i)\chi_4(d)d\sqrt c/(2Nq)\) yields
\(-i\chi_4(d)dc/(2Nq)=-i\chi_4(d)/(2N)\).
Writing \(h=du\) partitions odd \(h\bmod4N\) by
\(d=(h,N)\), so the divisor recombination is exactly
\(G_N(x^2-s)\). This validates the full-frequency physical
positive and negative formulas and

\[
\mathcal C_{\rm int,U}
=\mathcal C_+^{\rm full}+\mathcal C_-^{\rm full}
-\mathcal Z_{\rm tr}-\mathcal F_{\rm tr}.
\]

For either fixed removed frequency, the direct interval estimate
\(\sup_I|\sum_{s\in I}K(-v^2,-s;c)|\ll c\log(2c)\) is enough for the
Abel trace itself. The restored cost is

\[
\frac{VM^{-3/4}}{Nq}\sum_{d\mid N,\ d\ {\rm odd}}dc^{3/2}X^\varepsilon
\ll VM^{-3/4}N^{-1/2}X^\varepsilon
\le M^{-1/4}X^\varepsilon.
\]

This is separate from, and therefore does not illicitly transfer, a
whole zero or Nyquist row theorem. The estimate is also compatible
with \(c=4\), where the interior frequency set is empty.

## 4. Endpoint roots and exact strict survivor

The p-adic table is correct. For \(j(j-1)\), the two roots modulo
every \(p^\nu\), including \(2^\nu\), are \(0,1\), and CRT gives
\(2^{\omega(N)}\) roots. For \(j^2+j+1\), there is no \(2\)-adic
root; the sole root modulo \(3\) has no lift modulo \(9\); and for
\(p\ne2,3\) there are two simple lifts exactly when
\(p\equiv1\pmod3\). Since the blocks have length \(<N\), the
endpoint subrow is \(M^{-3/4}X^\varepsilon N^{o(1)}\), hence stronger
than the scalar target.

That statement concerns only \(s=j\), namely
\(k^2-k+1\) on the positive side and \(k^2+k\) on the negative side
after \(k=j+1\) or \(k=-j\). The strict survivor has exactly

\[
\begin{aligned}
&a_+\le k^2-N\ell\le k-2,
&&W_+(k)=F_{k-1}(k),\\
&-k+1\le k^2-N\ell\le b_-,
&&W_-(k)=F_{-k}(k).
\end{aligned}
\]

The positive and negative boundary arguments are respectively
\((k^2-k+1)/N<\ell\) and \((k^2+k)/N>\ell\); the arithmetic sign is
\(\chi_4(\ell)\). The two arguments must not be replaced by
\(\ell\), and the signs/strict selectors do not give a termwise
positive-negative pairing. The explicit \(L=2^h\) family in the
conductor audit is algebraically valid and confirms that an active
strict resonant point can have a nonresonant endpoint.

## 5. Localization, scalar calibration, and supplied capacities

The literal boundary-profile support forces a nonzero trace block to
satisfy \(V\asymp K=\sqrt{NM}\). This is a genuine zero result away
from the top support, but in the nonzero region \(V\gg M\), so the
support count remains \(L_{\rm str}\ll M X^\varepsilon\). With one
atom of size \(a=M^{-3/4}X^\varepsilon\), the absolute result is only
\(aM=M^{1/4}X^\varepsilon\).

The scalar trace target is \(O_\varepsilon(X^\varepsilon)\), not
\(M^{-1/4}\). Equivalently, after removing the atom scale, the actual
missing raw estimate is

\[
\left|\sum_{\ell\asymp M}\chi_4(\ell)
 \{\eta_+(\ell)\widetilde W_+(\kappa(\ell))
   +\eta_-(\ell)\widetilde W_-(\kappa(\ell))\}\right|
\ll M^{3/4}X^\varepsilon.
\]

Raw square-root size \(M^{1/2}\) would be stronger. The standard
second-derivative discrepancy calculation gives
\(M^{1/3}K^{1/3}+M/\sqrt K\), which reaches \(M^{3/4}\) only if
\(M\ge N^{2/3}\). The displayed \((1/6,2/3)\) placement gives
\(M^{4/7}K^{1/7}\) and has the same threshold. The general
exponent-pair interface
\(\lambda_0+\tfrac34\kappa_0\le\tfrac34\) at \(M=N^{1/2}\), and the
accepted completion capacity \(\sqrt N\), are correctly calibrated:
none supplies the required raw bound over the frozen
\(M\le N^{1/2}\) range.

These are capacity/interface statements, conditional on the stated
sharp-selector and boundary-weight placements. They should not be
recorded as an unconditional impossibility theorem for all possible
discrepancy, exponent-pair, or spectral methods.

## 6. First unproved step and scope

The first unproved mathematical step is the signed strict-survivor
estimate above for the literal sparse nearest-cell selectors, the two
different boundary-frozen profiles, residual phases, and
\(\chi_4(\ell)\). No supplied proof reaches raw \(M^{3/4}\), and
ordinary character partial summation merely recovers the absolute
\(aM\) bound because the sparse selector may have variation of order
its support.

The remaining Abel outer terms and profile-bulk differences are
separate open seams. Nothing reviewed here proves the full paired
matrix, another \(D,d,L,t\) regime, M9-M1, M9, the quarter target, or
either global exponent.

## 7. Required controls, dependencies, and state effect

The following controls pass for the moving-cell object: prefix/suffix
orientation; both outer-term identities and their quarantine;
full-frequency inversion; direct zero and Nyquist trace-piece bounds;
the \(p=2,3\) root exceptions; strict endpoint deletion; quotient
versus boundary-profile separation; top-support localization; and the
raw \(M^{3/4}\) calibration. The strict signed estimate, outer terms,
and profile bulk remain open. The reports provide a route-scoped
no-go for endpoint/count/BV and the listed standard placements, but
not a universal no-go.

Reviewed artifacts: protocol.md, state/proof_obligations.yml,
state/active_campaign.yml,
strategy/round158_d1_paired_interior_cell_trace_strategy.md, both
conductor candidates, and the discovery and blind rederivation
reports in this campaign. Recommended state effect: **revise** the
candidate package to state the narrow certified reductions and retain
the strict signed trace as open; reject only the forbidden endpoint,
cardinality, automatic-pairing, and unverified-standard-placement
closures.
