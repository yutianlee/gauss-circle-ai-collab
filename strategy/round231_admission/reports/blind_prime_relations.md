# Round231 admission — blind prime relations

- Task: `blind_prime_relations`.
- Role/status: statement-only independent algebra rederiver; admission selection only; no analytic round launched.
- Generated: 2026-10-11T10:28:06+08:00.
- Graph SHA256 supplied by the brief, not independently read or verified: `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
- Isolation: only the three context files listed in Section 6 were read. No graph, history, sibling report, or external source was consulted.
- Allocation: analytical/algebraic derivation and hand-exact controls; no numerical experiment.

## 1. Result: lemma or no-go result

All stated split-prime identities are correct, including both scaling powers and the negative correction term. For an inert prime the correct identities are

\[
r(pn)=\mathbf 1_{p\mid n}r(n/p),\qquad r(p^2n)=r(n),
\]

and hence

\[
B_{T;p\mid n}(R)=p^{-3/2}B_{T/p^2}(pR)\qquad(p\equiv3\pmod4).
\]

At the ramified prime,

\[
r(2n)=r(n),\qquad B_{T;2\mid n}(R)=2^{-3/4}B_{T/2}(\sqrt2 R).
\]

The first split-prime transformed moment has the exact form

\[
\boxed{\ I_{T,p}=p^{-1/2}\int_0^\infty
w\!\left(\frac{S}{p^{3/2}U}\right)|B_U(S)|^{12}\,dS,
\qquad U=T/p.\ }
\]

Thus its radius scale divided by its coefficient parameter is \(p^{3/2}\). A theorem whose hypothesis is a fixed diagonal window \(S\asymp U\) supplies no growing-prime uniform estimate for this moving window without additional hypotheses and estimates. This is a no-go for that direct application, not a disproof of the desired off-diagonal estimate.

Finally, \(h(k)=k+1\) satisfies \(Hh=2h\), including the boundary \(k=0\). Consequently \(P(H)h=P(2)h\): a polynomial with \(P(2)=0\) annihilates the actual split-prime local coefficient channel.

## 2. Exact statement and hypotheses

Let \(\chi_4(n)\) equal zero for even \(n\), one for \(n\equiv1\pmod4\), and minus one for \(n\equiv3\pmod4\). For positive integers \(n\), set

\[
f(n)=\sum_{d\mid n}\chi_4(d),\qquad r(n)=4f(n).
\]

For \(U>0\), real \(R\), and real even Schwartz \(\Psi\), define \(B_U(R)\) as in the isolated statement. All subseries are literal coefficient subseries; there is no change of normalization. For every odd prime \(p\) and positive integer \(n\),

\[
r(pn)+\chi_4(p)\mathbf1_{p\mid n}r(n/p)
=(1+\chi_4(p))r(n),
\tag{1}
\]

where a term involving \(n/p\) is omitted when \(p\nmid n\). For \(T>0\) and real \(R\),

\[
B_{T;p\mid n}(R)
=(1+\chi_4(p))p^{-3/4}B_{T/p}(\sqrt pR)
-\chi_4(p)p^{-3/2}B_{T/p^2}(pR).
\tag{2}
\]

For the moment identity, take \(w\) nonnegative measurable with support contained in some \([a,b]\subset(0,\infty)\). The equality holds for extended nonnegative integrals; it is finite if \(w\in L^1\), as is the case for ordinary bounded or smooth compactly supported test weights. Measurability is implicit whenever the question's integral is written. Integration over all real \(R\) gives the same result because the weight has positive support.

For the local operator identity, work on the vector space of all scalar sequences indexed by the nonnegative integers, with the boundary rule in the question. No boundedness or summability assumption on \(h\) is required for a finite polynomial in \(H\). The factorizable coefficient law has its usual normalized local convention \(c_q(0)=1\); equivalently, it suffices that for each \(m\) coprime to the selected split prime \(p\), \(c(p^km)=C_m(k+1)\) with \(C_m\) independent of \(k\).

## 3. Proof or derivation

### Arithmetic at one prime

For coprime positive integers \(a,b\), every divisor of \(ab\) is uniquely a product of a divisor of \(a\) and a divisor of \(b\). Complete multiplicativity of \(\chi_4\) therefore gives \(f(ab)=f(a)f(b)\). It is \(f=r/4\), not \(r\), that is multiplicative with value one at the identity.

Write \(n=p^km\), \(p\nmid m\). For odd \(p\), set \(\epsilon=\chi_4(p)\in\{1,-1\}\). Then

\[
r(p^km)=4f(m)L_\epsilon(k),\qquad
L_\epsilon(k)=\sum_{j=0}^k\epsilon^j.
\]

At a split prime, \(L_1(k)=k+1\). At \(k=0\), \(L_1(1)=2L_1(0)\); for \(k\ge1\),

\[
L_1(k+1)+L_1(k-1)=(k+2)+k=2(k+1).
\]

Multiplying by \(4f(m)\) proves the proposed split recurrence. This argument does not divide by \(f(m)\), so it covers zeros caused by other inert primes.

At an inert prime, \(L_{-1}(k)\) is one for even \(k\) and zero for odd \(k\). Thus \(L_{-1}(1)=0\), \(L_{-1}(k+1)=L_{-1}(k-1)\) for \(k\ge1\), and \(L_{-1}(k+2)=L_{-1}(k)\) for every \(k\ge0\). These are exactly

\[
r(pn)-\mathbf1_{p\mid n}r(n/p)=0,
\qquad r(p^2n)=r(n).
\]

Notice the minus sign in the inert recurrence. Replacing it by a plus sign would be false. These two cases establish (1).

For \(p=2\), all positive powers of two have character value zero, so the local divisor sum is \(1\) at every exponent. Hence \(r(2n)=r(n)\).

### Subseries and normalization

The Schwartz decay makes every displayed series absolutely convergent for fixed positive coefficient parameter: for example, \(|r(n)|\le4d(n)\le4n\), while \(|\Psi(\sqrt{n/U})|\) decays faster than any chosen power of \(n\). Thus reindexing is justified.

Reindex the multiples-of-\(p\) subseries with \(n=pm\):

\[
B_{T;p\mid n}(R)=p^{-3/4}\sum_{m\ge1}r(pm)m^{-3/4}
\Psi\!\left(\sqrt{\frac m{T/p}}\right)
\cos\!\left(2\pi\sqrt pR\sqrt m-\frac{3\pi}4\right).
\tag{3}
\]

Substituting (1), its \((1+\epsilon)r(m)\) term gives
\((1+\epsilon)p^{-3/4}B_{T/p}(\sqrt pR)\). In its remaining term put \(m=p\ell\). The two coefficient powers multiply to \(p^{-3/2}\), its cutoff becomes \(\Psi(\sqrt{\ell/(T/p^2)})\), and its phase becomes \(2\pi pR\sqrt\ell-3\pi/4\). Its sign is \(-\epsilon\). This proves (2) exactly.

In particular, the split formula is

\[
2p^{-3/4}B_{T/p}(\sqrt pR)-p^{-3/2}B_{T/p^2}(pR),
\]

and the inert formula is the single positive term stated in Section 1. For an inert prime, all coefficients with odd \(p\)-adic valuation vanish; the multiples-of-\(p\) subseries therefore equals the multiples-of-\(p^2\) subseries. Substitution of \(r(2m)=r(m)\) in (3) gives the ramified formula directly.

No factor of four is gained or lost. Also, the arithmetic signs above do not imply a sign for a wave sum: the cosine changes sign, and the allowed real Schwartz \(\Psi\) need not be nonnegative.

### Exact moment window

Let

\[
I_{T,p}=\int_0^\infty w(R/T)|B_{T/p}(\sqrt pR)|^{12}\,dR.
\]

Set \(S=\sqrt pR\), giving \(dR=p^{-1/2}dS\). With \(U=T/p\),

\[
w(R/T)=w\!\left(\frac S{\sqrt pT}\right)
=w\!\left(\frac S{p^{3/2}U}\right),
\]

which proves the boxed identity. More exactly, the transformed support is
\(\sqrt pT\,\operatorname{supp}w=p^{3/2}U\,\operatorname{supp}w\), contained in

\[
[a\sqrt pT,b\sqrt pT]=[ap^{3/2}U,bp^{3/2}U].
\]

The reference radius scale \(\sqrt pT\) divided by \(U\) is precisely \(p^{3/2}\); an individual normalized location \(x\in\operatorname{supp}w\) has radius ratio \(xp^{3/2}\).

For illustration of the logical implication only, suppose a theorem states, for every fixed admissible weight \(v\),

\[
\int v(S/U)|B_U(S)|^{12}\,dS\le C(v)U^\beta
\]

in a specified range of \(U\). Define \(w_p(t)=w(t/p^{3/2})\). If \(p\) is fixed and the theorem genuinely permits this fixed weight, the consequence is

\[
I_{T,p}\le p^{-1/2}C(w_p)(T/p)^\beta.
\]

It remains necessary to satisfy the theorem's range for \(T/p\). The number \(C(w_p)\) can depend on \(p\), and no bound on that dependence follows from a fixed-weight theorem. If the theorem instead restricts support to one fixed interval such as \([1,2]\), even the fixed-prime application needs a separate extension to the new interval. Saying that two scales are comparable for fixed \(p\) does not supply that extension. In the usual broader formulation allowing arbitrary fixed comparability constants, fixed \(p\) presents no growing-parameter mismatch, but the constants depend on those comparability constants.

For growing \(p\), \(p^{3/2}\) is unbounded, so the fixed diagonal-window hypothesis is not met uniformly. Choosing \(\sqrt pT\) as a new moment parameter does not repair the problem: the coefficient parameter in the integrand is still \(T/p\).

For completeness, the correction term has an even larger mismatch. With \(V=T/p^2\) and \(S=pR\),

\[
\int w(R/T)|B_{T/p^2}(pR)|^{12}\,dR
=p^{-1}\int w(S/(p^3V))|B_V(S)|^{12}\,dS.
\]

Its reference ratio is \(p^3\), with Jacobian \(p^{-1}\). Taking the twelfth moment of an entire scalar multiple also multiplies by the twelfth power of that scalar; these coefficient factors are separate from both Jacobians.

### Polynomial local filter

For \(h(k)=k+1\), the boundary gives \((Hh)(0)=h(1)=2=2h(0)\). At \(k\ge1\),

\[
(Hh)(k)=h(k+1)+h(k-1)=k+2+k=2h(k).
\]

Inductively \(H^jh=2^jh\), including \(j=0\). Therefore, for every polynomial \(P(z)=\sum_{j=0}^d a_jz^j\),

\[
P(H)h=\sum_{j=0}^da_jH^jh=P(2)h.
\]

For a factorizable law, the sequence on each fixed coprime fiber is \(C_mh\), so the same calculation applies independently on every fiber. In particular it applies to \(f=r/4\) at any split prime. A filter vanishing at two removes this channel identically. It cannot simultaneously retain this nonzero channel by that same local coefficient action.

This is an algebraic identity on sequences. The growing sequence \(k+1\) is not an \(\ell^2\) eigenvector, and no Hilbert-space spectral conclusion, norm estimate, or asymptotic wave cancellation follows. Applying index shifts to phases and cutoffs introduces their own transformations, so a coefficient identity cannot be silently converted into a moment estimate at unchanged parameters.

## 4. First doubtful or unproved step

There is no unproved arithmetic or change-of-variable step in the identities above.

The first unsupported analytic step would be to apply a theorem with only fixed \(S/U\) comparability to the moving interval \(S/U\in[ap^{3/2},bp^{3/2}]\), and claim a constant uniform in growing \(p\). Such uniformity needs an explicitly off-diagonal moment theorem or an independent argument. No such theorem is among the permitted inputs.

A separate invalid step would be to assert that a filter satisfying \(P(2)=0\) retains the actual split-prime coefficient channel; the exact polynomial identity refutes that assertion. None of these observations refutes the existence of some other successful analytic mechanism.

## 5. Required control test and outcome

All controls below are exact hand calculations, not numerical evidence for an asymptotic result.

1. **Split boundary and repeated valuation:** \(r(1)=4\), \(r(5)=8\), \(r(25)=12\), and \(r(125)=16\). The recurrence gives \(8=2\cdot4\), \(12+4=2\cdot8\), and \(16+8=2\cdot12\). Outcome: pass, including the boundary indicator.
2. **Inert sign and parity:** \(r(3)=0\), \(r(9)=4\), \(r(27)=0\), and \(r(81)=4\). At \(n=3\), the correct recurrence is \(r(9)-r(1)=0\). The erroneous plus-sign version would give \(8=0\). Also \(r(27)=r(3)\) and \(r(81)=r(9)\). Outcome: correct sign and period-two identity pass; the competing plus sign fails.
3. **Ramified normalization:** \(r(2)=r(4)=r(8)=4\). Outcome: pass. Further, \(r(10)=8\), whereas \(r(2)r(5)=32\); this detects any accidental use of ordinary multiplicativity for \(r\) instead of \(r/4\).
4. **Mixed-prime zero:** for the split prime \(5\), take \(n=3\). Then \(r(15)=r(3)=0\). Outcome: pass without dividing by a possibly zero coprime factor.
5. **Subseries coefficient reconstruction:** in the split formula, the coefficient at original index \(n=p\) is \(2p^{-3/4}r(1)=r(p)p^{-3/4}\); at index \(n=p^2\), it is \(p^{-3/2}(2r(p)-r(1))=p^{-3/2}r(p^2)\). In the inert formula, the first nonzero possible index is \(p^2\), with coefficient \(p^{-3/2}r(1)\). Outcome: pass for all powers, factors of four, and signs tested.
6. **Jacobian:** replacing the moment factor by one gives \(\int w(R/T)dR=T\int w\). The transformed expression gives \(p^{-1/2}(\sqrt pT)\int w=T\int w\). Outcome: pass; omitting the Jacobian introduces a spurious factor \(\sqrt p\).
7. **Filter boundary and interior:** \((H-2)h\) at \(k=0,1,2\) is respectively \(2-2=0\), \(3+1-4=0\), and \(4+2-6=0\). Outcome: pass. The full proof in Section 3 extends this to every index and every polynomial root at two.

Limitations: these controls diagnose normalization and sign errors only. The exact derivations certify the finite/local algebra; neither controls nor derivations establish a new moment bound.

## 6. Dependencies and exact artifacts used

The complete read set is:

- `protocol.md` — research and reporting rules.
- `strategy/round231_admission/briefs/blind_prime_relations.md` — isolated task, supplied graph hash, permitted context, and resource restrictions.
- `strategy/round231_admission/briefs/blind_prime_statement.md` — definitions and statements independently checked here.

Mathematical dependencies are the elementary divisor factorization for coprime integers, complete multiplicativity of the explicitly defined character, the finite geometric sum at one prime, Schwartz decay, a linear change of variable, and polynomial linear-operator algebra. No external theorem, source search, numerical package, graph assertion, or sibling artifact is used.

The generated-time query supplies provenance only. File hashing after writing supplies an immutable report identifier only and is not a mathematical control. This report is the sole written artifact of this task.

## 7. Recommended state effect

**Retain** the split recurrence and subseries identity as correct exact arithmetic; **revise** any proposed inert recurrence to the minus-sign relation in Section 1; **retain** the ramified identity.

**Reject** a direct claim of growing-prime uniformity from a moment theorem known only in fixed diagonal windows, absent added uniform off-diagonal hypotheses. **Reject** any local-filter claim that \(P(2)=0\) preserves the split-prime channel \(k+1\).

**No change** to the authoritative proof state is recommended from this blind admission report alone. These are isolated identity checks and identified inference barriers, not a new analytic estimate, graph promotion, or successor-round proposal. The conductor owns any subsequent state decision.
