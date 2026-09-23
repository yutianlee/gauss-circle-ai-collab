# 1. Result.

**GREEN for the scoped review.** Claims (184.C1)--(184.C6) and (184.C17)--(184.C20) are exact under the stated accepted \(t=1\) incidence interface. The selector is allocation-independent; the exchange is an integral, fixed-point-free, multiplicity-one involution on the complete ambient XOR allocation set; it preserves all required arithmetic data and the product phase; it reverses \(\chi_4(v)\); zero extension gives the exact half-difference identity; and the Boolean residual and constant-amplitude sign-mass formulas are correct.

The post-unmask comparison does not alter the provenance of the statement-only report. That report independently established the finite exchange algebra and exact residual using only its declared blind packet. The literal report and formal candidate now supply additional M1 provenance, including the accepted \(t=1\) incidence map and a stronger collar ledger. Those facts confirm the blind algebra; they are not retroactively attributed to the blind derivation.

The blind report's \(\mathcal X^2\) warning was correct for the packet literally supplied to it. The candidate resolves, rather than suppresses, that warning: (184.C13) gives an unweighted \(O_\kappa(L^{3/2})\) exceptional-site count, and (184.C14) applies one \(X^\varepsilon\) coefficient weight afterward. There is no hidden product of two separately displayed loss factors.

This verdict is limited to the requested selector, exchange, character, zero-extension, residual-Boolean, constant-sign-mass, and loss-clarification seams. It is not a verdict on every analytic detail of (184.C7)--(184.C16), the complete residual, or the complete \(t=1\) theorem.

# 2. Exact statement and hypotheses.

Assume the accepted hard-M1 incidence interface: \(t=1\) is the \(G=\rho=1\) face, its allocation coordinates satisfy

\[
 (u,v)=1,\qquad v\ \text{odd},\qquad uv\ \text{squarefree},
\]

and the incidence-to-\((u,v)\) map has multiplicity one. Assume the literal coefficient is extended by zero off every physical shell, cone, profile, floor, star, hard-sample, crossing, and endpoint predicate.

For each squarefree \(N\), let \(s(N)\) be empty or the unique pair selected by a fixed canonical rule from the eligible unordered pairs \(\{p,q\}\) satisfying

\[
 p\ne q,\quad p,q\mid N,\quad p,q\ \text{odd},\quad
 \chi_4(pq)=-1,\quad |\log(q/p)|\leq\kappa L^{-1/2}.
\]

The selector may depend only on \((N,L,\kappa)\), never on the allocation \(N=uv\). For \(s(N)=\{p_N,q_N\}\), the ambient XOR set contains every coprime allocation \(uv=N\), with \(v\) odd, in which exactly one selected prime divides \(v\). Physical support membership is deliberately absent from this ambient definition.

On this set,

\[
 \tau_N(u,v)=
 \begin{cases}
 (up_N/q_N,vq_N/p_N),&q_N\mid u,\ p_N\mid v,\\
 (uq_N/p_N,vp_N/q_N),&p_N\mid u,\ q_N\mid v.
 \end{cases}
\]

For a selected product define

\[
 \rho_N(v)=1-\mathbf1_{p_N\mid v}-\mathbf1_{q_N\mid v}
              +2\mathbf1_{p_Nq_N\mid v},
\]

and set \(\rho_N(v)=1\) when no pair is selected. No pair existence, sector nonemptiness, density, or literal lower mass is assumed.

# 3. Proof or derivation.

The accepted representation has \(t=G\rho\) with \(G,\rho\) positive integers. Thus \(t=1\) forces \(G=\rho=1\), giving the coprime squarefree face and its inherited multiplicity-one allocation map; conversely that face gives \(t=1\). Literal support has \(u,v\asymp L\), so there are \(O(L^2)\) ordered sites. The normalized pointwise bound gives (184.C2),

\[
 |\mathcal T_{L,X,\sigma}|\ll_\varepsilon L^2X^\varepsilon,
\]

only as an upper capacity. Neither the candidate nor the blind report turns it into literal lower mass.

For fixed \(N\), the eligible-pair set is finite, so choosing its lexicographically first member is canonical and allocation-independent. On an XOR allocation, squarefreeness and coprimality put one selected prime on each leg. The quotients in (184.C4) are integral, and the exchange leaves every prime divisor allocated to exactly one leg. Hence squarefreeness and coprimality persist. Both exchanged primes are odd, so a factor \(2\), if present, remains on \(u\), and both leg parities are unchanged.

The product identity

\[
 (up_N/q_N)(vq_N/p_N)=uv=N
\]

holds in the first orientation, and similarly in the second. Therefore the radical phase, product shell, \(L\), and selector are preserved. The selected bits are interchanged, so \(\tau_N^2=1\). A fixed point would force \(p_N=q_N\). The two XOR cases are disjoint and there is one canonical pair, so every vertex has one image and every orbit has exactly two members. This proves ambient closure, integrality, involution, absence of fixed points, and multiplicity one. It also shows why physical support itself need not be closed.

In the first orientation,

\[
 \frac{\chi_4(v')}{\chi_4(v)}
 =\frac{\chi_4(q_N)}{\chi_4(p_N)}
 =\chi_4(p_Nq_N)=-1;
\]

the reverse ratio in the other orientation has the same value. If \(a(x)\) is the zero-extended literal coefficient and \(\Phi_N=e(\sigma\sqrt{XN})\), reindexing the ambient XOR set by \(\tau_N\) gives

\[
 \sum_x\chi_4(v_x)\Phi_Na(\tau_Nx)
 =-\sum_x\chi_4(v_x)\Phi_Na(x).
\]

Subtracting and dividing by two proves (184.C6). When only one endpoint is physically supported, the two ambient orientations still reindex each other and zero extension supplies the missing zero term.

For the residual put \(\alpha=\mathbf1_{p_N\mid v}\) and \(\beta=\mathbf1_{q_N\mid v}\). Then

\[
 1-\alpha-\beta+2\alpha\beta
\]

has values \(1,0,0,1\) on \((\alpha,\beta)=(0,0),(1,0),(0,1),(1,1)\). It is exactly the neither/both indicator and vanishes exactly on XOR. Taking \(\rho_N=1\) for no-pair products proves the exhaustive partition (184.C18). Summing over all odd divisors with \(\mu^2(N)\) proves (184.C19); for even squarefree \(N\), the factor \(2\) remains correctly on \(u=N/v\).

Let \(M_N\) be the odd part of \(N\). With no selected pair, independent divisor bits give

\[
 \sum_{v\mid M_N}\chi_4(v)=\prod_{r\mid M_N}(1+\chi_4(r)).
\]

With a selected pair, \(\rho_N\) retains only pair-bit patterns \(00\) and \(11\), whose combined contribution is

\[
 1+\chi_4(p_N)\chi_4(q_N)
 =1+\chi_4(p_Nq_N)=0.
\]

Factoring the remaining bits proves (184.C20). This is ambient constant-amplitude balance only; it does not estimate the coefficient-weighted one-sided physical residual.

Finally, the blind packet separately allowed \(O(\mathcal X)\) pointwise size and \(O(L^{3/2}\mathcal X)\) exceptional sites, so the blind report correctly recorded the literal \(O(L^{3/2}\mathcal X^2)\) consequence. The candidate instead derives \(O_\kappa(L^{3/2})\) geometric collar cardinality before applying one \(O_\varepsilon(X^\varepsilon)\) coefficient weight. Its \(O_{\kappa,\varepsilon}(L^{3/2}X^\varepsilon)\) collar ledger is therefore a genuine clarification.

# 4. First doubtful or unproved step.

There is no doubtful step in (184.C1)--(184.C6) or (184.C17)--(184.C20) within their stated accepted dependencies. The exact \(t=1\) coordinate identification and incidence multiplicity come from the accepted pre-existing hard-M1 interface, not from the blind packet; this review preserves that boundary.

The first unproved step toward the complete \(t=1\) theorem occurs after (184.C20): ambient constant-amplitude balance does not imply cancellation of the zero-extended, coefficient-weighted physical residual. The still-open requirement is a signed estimate for \(\mathcal T^{\rm rem}_{L,X,\sigma}\), such as the one-outer-real-part correlation (184.C25).

The completeness of the literal face ledger and all analytic estimates in (184.C7)--(184.C16) remain owned by the separate coefficient/profile/endpoint review. For the narrower loss question here, the separation of unweighted collar count from coefficient-weighted mass is exact.

# 5. Required control test and outcome.

| Control | Outcome |
|---|---|
| (184.C1), exact \(t=1\) face and multiplicity | **PASS.** It uses the accepted \(t=G\rho\) interface and preserves the unique incidence parameterization. |
| (184.C2), capacity | **PASS.** \(O(L^2)\) sites times \(O_\varepsilon(X^\varepsilon)\) is an upper envelope only. |
| (184.C3), selector | **PASS.** Finite lexicographic selection is canonical, allocation-independent, and permits an empty set. |
| (184.C4), exchange domain | **PASS.** XOR and squarefreeness give integral quotients; the image is ambient XOR; the cases are disjoint; \(\tau_N^2=1\); distinct primes exclude fixed points. |
| Product, phase, arithmetic, parity | **PASS.** Prime allocation is swapped without repetition, \(uv=N\) is fixed, and the factor \(2\), phase, and selector are unchanged. |
| (184.C5), character | **PASS.** Both orientations multiply \(\chi_4(v)\) by \(\chi_4(p_Nq_N)=-1\). |
| (184.C6), zero extension | **PASS.** Ambient reindexing gives the exact factor \(1/2\), including the one-supported-endpoint control. |
| (184.C17), Boolean residual | **PASS.** The truth table is \(1,0,0,1\): neither, XOR, XOR, both. |
| (184.C18)--(184.C19), exhaustive residual | **PASS.** No-pair products contribute all allocations; selected products contribute neither/both and no third class. |
| (184.C20), sign mass | **PASS.** The no-pair product is exact; the selected pair-bit factor is \(1+\chi_4(p_Nq_N)=0\); no physical-cone estimate is inferred. |
| False controls | **PASS.** All-\(1\bmod4\) products, separated semiprimes, and character erasure remain mechanism controls, never density or lower-mass claims. |
| Blind loss clarification | **PASS.** The blind warning remains valid for its packet, while (184.C13)--(184.C14) use an unweighted geometric count and one coefficient weight. |
| Blind provenance | **PASS.** Post-unmask agreement is independent corroboration; no later M1 input is attributed to the statement-only report. |

No numerical experiment, source import, vote, density assumption, or shiftwise absolute-value estimate was used.

# 6. Dependencies and exact artifacts used.

The review used only:

1. protocol.md;
2. state/proof_obligations.yml, for authoritative state and ownership scope;
3. state/active_campaign.yml;
4. rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/candidates/formalized_hard_m1_t1_comparable_factor_exchange_sector.md;
5. rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reviews/conductor_round184_report_reconciliation.md;
6. rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reports/blind_complete_t1_exchange_rederivation.md; and
7. rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/reports/literal_t1_exchange_residual_attack.md.

The candidate hash used for this verdict is

\[
 \texttt{609EB3BFA2EEE1566D913F63CBF4997E48AC7A7D6FD927213529C01528B8FC6E}.
\]

The earlier expected hash
\(\texttt{A59E49252026A88F589DEDFDAABA2039B7626C7BC645A7D8D55B0F60FA865947}\)
was superseded only by the conductor's hygiene repair of one corrupted
\(\backslash\mathrm{rm}\) token in (184.C14), with no mathematical change.
The current hash was verified locally before this review was written.

No other mathematical artifact, web source, or computation was used. No candidate or shared-state edit was made.

# 7. Recommended state effect.

**GREEN.** Mark the selector/exchange/character, ambient-domain, zero-extension, Boolean-residual, constant-sign-mass, blind-post-unmask consistency, and loss-clarification seams GREEN for the current candidate hash.

This review licenses no complete-\(t=1\) or parent promotion by itself. Subject to the remaining independent coefficient/profile/endpoint, residual/correlation, owner-scope, and final graph validations, only the strict comparable-factor XOR sector may become a subordinate proved fact. Keep the exact residual, the rest of \(t=1\), every \(t\geq2\) incidence, the near-resonant component, complete small-\(t\) owner, M1 and M2 parents, endpoint uniformity, M9, both bridges, the theorem, and every exponent claim unchanged.
