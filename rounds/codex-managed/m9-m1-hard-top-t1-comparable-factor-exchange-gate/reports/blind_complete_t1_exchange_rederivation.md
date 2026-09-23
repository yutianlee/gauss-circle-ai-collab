# 1. Result.

The proposed complete bound (B184.3) does not follow from the isolated hypotheses.  What does follow is an exact, multiplicity-one cancellation identity for the canonically selected XOR sector, together with its exact residual complement.

On the ambient set of all arithmetic allocations of a fixed product (with the coefficient extended by zero), (B184.5) is an integral, fixed-point-free involution.  It preserves the product and hence the phase, as well as squarefreeness, coprimality, parity, and the allocation-independent selector, and it reverses \(\chi _4(v)\).  It is generally **not** an involution of the support-truncated set \(4u<v<16u\), because an exchanged point can cross a strict support or profile face.

Writing \(\mathcal T_\oplus\) for the full canonical XOR incidence sector, one has the exact identity

\[
 \mathcal T_\oplus
 =\frac12\sum_{(u,v)\in\Omega_\oplus}
 \chi _4(v)e(\sigma\sqrt{Xuv})
 \bigl(\widetilde A(u,v)-\widetilde A(\tau(u,v))\bigr),
\tag{1.1}
\]

where \(\widetilde A\) is the literal coefficient with all strict faces and arithmetic truncations imposed and then extended by zero, and \(\Omega_\oplus\) contains both endpoints of every relevant ambient XOR orbit.  The common-cell part is \(O_\kappa(L^{3/2}\mathcal X)\).  The face-crossing part is also \(O_\kappa(L^{3/2}\mathcal X)\) in the usual convention that \(\mathcal X\) denotes a disposable subpolynomial loss whose finite powers are reabsorbed.  If the same displayed \(\mathcal X\) is instead a fixed numerical factor with no loss reindexing, the literal hypotheses give only

\[
 |\mathcal T_\oplus|
 \ll_\kappa L^{3/2}(\mathcal X+\mathcal X^2),
\tag{1.2}
\]

because hypothesis 3 counts \(O_\kappa(L^{3/2}\mathcal X)\) exceptional sites and hypothesis 1 allows size \(O(\mathcal X)\) at each site.  This bookkeeping point must be fixed before interpreting (1.1) as a literal one-loss estimate.

The exact residual is the sum over every allocation whose product has no selected pair, together with the neither and both allocations when a pair is selected.  No supplied hypothesis estimates that signed residual.  In particular, products whose odd prime factors are all \(1\pmod 4\) admit no sign-reversing fixed-product allocation map at all, and balanced semiprimes in the cone have their two prime factors separated by a factor greater than four, so the proposed close exchange does not see them for large \(L\).  Thus the narrowest mechanism no-go is: local, product-preserving prime exchange alone cannot prove the complete \(t=1\) estimate.  The first missing relation is a target-sized **signed** estimate for the exact residual, necessarily using coefficient-specific algebra or cancellation across different products (or an equally strong signed transport/correlation statement), not an unproved density assertion.

# 2. Exact statement and hypotheses.

Let \(\mathscr D\) be the arithmetic allocation set

\[
 \mathscr D=\{(u,v)\in\mathbb Z_{\ge1}^2:(u,v)=1, v\ {\rm odd},\ uv\ {\rm squarefree}\}.
\]

Put

\[
 \widetilde A(u,v)
 =\mathbf 1_{\{4u<v<16u\}}A_{L,X}^{\sigma}(u,v),
\]

with the stated literal support, endpoint values, and zero extension understood.  Thus only \(u\asymp L\), \(v\asymp L\) can contribute.  For a product \(N\) possessing a selected pair, write \(s(N)=\{p_N,q_N\}\); otherwise write \(s(N)=\varnothing\).  For \(s(N)\ne\varnothing\), set

\[
 j_N(v)=\#\bigl(s(N)\cap\{r:r\text{ prime and }r\mid v\}\bigr)\in\{0,1,2\}.
\]

The ambient XOR set \(\Omega_\oplus\) consists of the allocations in \(\mathscr D\) with \(s(uv)\ne\varnothing\), \(j_{uv}(v)=1\), and with at least one of \(\widetilde A(u,v)\) and \(\widetilde A(\tau(u,v))\) nonzero.  It is finite and is closed under \(\tau\).  The exact complement inside the original complete sum is

\[
 \mathscr C=
 \left\{(u,v)\in\mathscr D:\widetilde A(u,v)\ne0,\quad
 \begin{array}{l}
 s(uv)=\varnothing,\quad\text{or}\\
 s(uv)\ne\varnothing\text{ and }j_{uv}(v)\in\{0,2\}
 \end{array}
 \right\}.
\tag{2.1}
\]

No density, positive proportion, or blockwise nonemptiness of either \(\Omega_\oplus\) or \(\mathscr C\) is asserted.

The isolated conclusion uses exactly the following hypotheses: the size bound \(|\widetilde A|\ll\mathcal X\); the common-cell exchange-direction estimate \(|\widetilde A(u,v)-\widetilde A(ue^\theta,ve^{-\theta})|\ll_\kappa L^{-1/2}\mathcal X\) for \(|\theta|\le\kappa L^{-1/2}\); the stated total face-crossing count; a canonical selector depending only on \((N,L,\kappa)\); and \(\chi _4(pq)=-1\) with \(|\log(q/p)|\le\kappa L^{-1/2}\).

Without the size hypothesis there is no capacity bound and no control of face-crossing orbits.  Without common-cell regularity, \(\Theta(L^2)\) interior incidences can each have an \(O(\mathcal X)\) difference.  Without the face-count hypothesis, strict support, floor, star, hard-sample, endpoint, or zero-extension crossings can likewise occupy \(\Theta(L^2)\) sites.  If the selector depended on the allocation, exchange need not preserve it or be multiplicity one.  Without closeness, the coefficient regularity is inapplicable.  Without \(\chi _4(pq)=-1\), the paired sum is a sum rather than a difference.

# 3. Proof or derivation.

The number \(M\) of potentially contributing lattice sites is \(O(L^2)\): there are \(O(L)\) possible \(u\asymp L\), and the cone gives \(O(L)\) possible \(v\) for each such scale.  Hence the coefficient-insensitive triangle capacity is

\[
 \mathfrak C:=\sum_{(u,v)\in\mathscr D}|\widetilde A(u,v)|
 \ll L^2\mathcal X.
\tag{3.1}
\]

For an arbitrary coefficient class bounded only by \(\mathcal X\), the supremum at a fixed set of \(M\) sites is exactly \(M\mathcal X\), since arbitrary phases can be aligned.  That statement is a capacity calculation, not a lower bound for the fixed literal coefficient; the phase-aligning coefficient generally destroys its literal character and exchange regularity.

Suppose first that \(q\mid u\) and \(p\mid v\).  Since \(uv\) is squarefree and \((u,v)=1\), \(p\nmid u\) and \(q\nmid v\), so

\[
 (u',v')=(up/q,vq/p)
\]

is integral, squarefree, and coprime.  Both exchanged primes are odd, so \(v'\) is odd.  The product is unchanged.  The opposite case is identical.  Applying the same exchange again restores \((u,v)\), while equality \((u',v')=(u,v)\) would force \(p=q\), so \(\tau\) is an involution without fixed points.  The canonical pair is unchanged because it depends only on \(N=uv\).  Consequently each ambient XOR vertex has exactly one partner and every orbit has two vertices.

Moreover,

\[
 \frac{\chi _4(v')}{\chi _4(v)}
 =\frac{\chi _4(q)}{\chi _4(p)}
 =\chi _4(pq)=-1
\]

in the displayed case, and the same conclusion holds in the other case.  Since \(u'v'=uv\), the phase is exactly unchanged.  Pairing the two endpoints of every orbit now gives (1.1).  Equivalently, (1.1) follows by changing variables \((u,v)\mapsto\tau(u,v)\) in the term containing \(\widetilde A\circ\tau\).

The exchange is exactly a permitted multiplicative displacement.  In the first case take \(\theta=\log(p/q)\), so \((u',v')=(ue^\theta,ve^{-\theta})\); in the second take \(\theta=\log(q/p)\).  On common smooth cells, therefore,

\[
 |\widetilde A(u,v)-\widetilde A(\tau(u,v))|
 \ll_\kappa L^{-1/2}\mathcal X.
\]

There are \(O(L^2)\) relevant ambient endpoints because each orbit contains a supported endpoint and the exchange has multiplicity one.  Thus the common-cell contribution to (1.1) is \(O_\kappa(L^{3/2}\mathcal X)\).  All remaining endpoints cross one of the enumerated faces.  Hypothesis 3 bounds their number by \(O_\kappa(L^{3/2}\mathcal X)\), while zero extension and hypothesis 1 bound each difference by \(O(\mathcal X)\).  This proves (1.2), and proves the advertised one-loss XOR estimate under the standard reabsorbable-loss interpretation.

The exact complete decomposition is

\[
 \boxed{
 \mathcal T_{L,X,\sigma}
 =\frac12\sum_{(u,v)\in\Omega_\oplus}
 \chi _4(v)e(\sigma\sqrt{Xuv})
 \bigl(\widetilde A(u,v)-\widetilde A(\tau(u,v))\bigr)
 +R_{\mathscr C}},
\tag{3.2}
\]

where

\[
 R_{\mathscr C}
 =\sum_{(u,v)\in\mathscr C}
 \chi _4(v)\widetilde A(u,v)e(\sigma\sqrt{Xuv}).
\tag{3.3}
\]

This is a partition, not an estimate for \(R_{\mathscr C}\).

There is an exact ordered-divisor Abel connector, but no supplied bound for its new quantities.  For fixed squarefree \(N\), order the contributing odd divisors as \(d_1<\cdots<d_m\), put \(a_j=\widetilde A(N/d_j,d_j)\), \(\epsilon_j=\chi _4(d_j)\), and \(E_j=\sum_{i\le j}\epsilon_i\).  With \(a_{m+1}=0\),

\[
 \sum_{j=1}^m\epsilon_j a_j
 =\sum_{j=1}^m E_j(a_j-a_{j+1}).
\tag{3.4}
\]

Neither bounds for \(E_j\) nor small multiplicative gaps between consecutive ordered divisors are among the hypotheses.  In particular, consecutive divisor transport need not be a close opposite-character prime exchange.  Applying an absolute value product by product would also abandon the one complete signed sum and would require an additional global estimate.

A sliding Fejer identity gives a second exact connector.  Enumerate the \(M\) complete summands in any fixed order as \(z_1,\ldots,z_M\), extend by zero, and let \(1\le H\) be integral.  Sliding an interval of length \(H\), summing it back to \(H\mathcal T\), and using Cauchy gives

\[
 H^2|\mathcal T|^2\le (M+H-1)\left(
 H\sum_{j=1}^M|z_j|^2
 +2\operatorname{Re}\left[
 \sum_{h=1}^{H-1}(H-h)
 \sum_{j=1}^{M-h}z_{j+h}\overline{z_j}
 \right]\right).
\tag{3.5}
\]

The real part in (3.5) is deliberately outside the full weighted shift sum.  No absolute values over individual shifts have been taken.  To turn (3.5) into (B184.3), one needs a signed upper bound for the full Fejer energy in parentheses.  No ordering or shift action supplied here relates those correlations to the local exchange estimate, so (3.5) is a connector rather than a proof.

# 4. First doubtful or unproved step.

After the valid XOR extraction, the first substantive unproved step would be

\[
 |R_{\mathscr C}|\ll L^{3/2}\mathcal X.
\tag{4.1}
\]

Nothing in the isolated packet relates the no-pair and neither/both terms in (3.3) to opposite-signed nearby terms, controls their ordered-divisor character partial sums, or supplies a signed cross-product phase correlation.  Pair density would not by itself imply (4.1), and no density statement is available in any case.

There is also a prior bookkeeping seam if \(\mathcal X\) is meant literally rather than as a reindexable loss: the exceptional-set hypotheses yield \(L^{3/2}\mathcal X^2\), not \(L^{3/2}\mathcal X\).  Under the intended disposable-loss convention, (4.1) is the first mathematical gap.  A Fejer route replaces (4.1) by an equally absent signed correlation estimate; taking absolute values of the shifts before proving such an estimate does not close the gap.

# 5. Required control test and outcome.

All controls below are algebraic diagnostics.  They are not asserted to occur with positive density, and none is a lower bound for the fixed literal coefficient.

- **Prime product.**  If \(N\) has one prime factor, its only allocations are \((1,N)\) and \((N,1)\).  The second violates \(v>4u\), and the first is excluded once the fixed \(u\asymp L\) block is beyond the bounded range \(u=1\).  Thus the prime-product capacity is eventually zero (and at worst \(O(\mathcal X)\) in bounded initial blocks).  It neither proves nor refutes the target.

- **Semiprime product.**  For squarefree \(N=rs\) with a balanced supported allocation, one prime is on each side.  The cone forces the larger-to-smaller ratio to exceed four.  Hence \(|\log(r/s)|>\log4\), so for \(\kappa L^{-1/2}<\log4\) the two primes cannot satisfy the close-pair condition.  Such a site is in the no-selector residual, regardless of whether the two characters are opposite.  Its exact coefficient-insensitive capacity is \(\mathcal X\) times the number of such prime-pair sites, bounded only by \(O(L^2\mathcal X)\) from the packet; no density is inferred.

- **All odd primes \(1\pmod4\).**  Then every odd divisor \(v\) has \(\chi _4(v)=1\), and no pair can have \(\chi _4(pq)=-1\).  Thus every such allocation, if present, lies in \(\mathscr C\), and no product-preserving sign-reversing allocation involution exists on that product.  This is an exact obstruction to completing the proof solely inside each fixed product.

- **Dechirped model.**  Replacing a test coefficient by \(b(u,v)e(-\sigma\sqrt{Xuv})\) removes the displayed phase.  Because exchange preserves \(uv\), dechirping does not disturb exchange-direction smoothness of \(b\).  On an all-\(1\pmod4\) product the remaining terms have one sign when \(b\) does.  Thus phase oscillation cannot be claimed from the stated hypotheses.  This is a false-model test, not a modification or lower bound for the literal coefficient.

- **Character-erased model.**  If \(\chi _4(v)\) is replaced by \(1\), an exchange orbit contributes \(e(\sigma\sqrt{XN})(\widetilde A(x)+\widetilde A(\tau x))\), not a difference.  A coefficient nearly constant along the exchange direction then reinforces.  The supplied Vaaler information enters only through the size, smooth-cell, and face hypotheses; no further Vaaler algebra is exposed that could repair this unsigned analogue.  This control confirms that the exact character reversal, together with coefficient regularity, is essential.

- **One-site and endpoint controls.**  A one-site test has exact modulus at most \(O(\mathcal X)\), safely below the target, and (1.1) reproduces it even if the partner has zero coefficient: the two ambient endpoints contribute equal halves after sign reversal.  If an exchange crosses a strict cone, shell, floor, star, hard-sample, endpoint, or zero-extension face, the truncated set is not invariant and no small common-cell difference is available.  Zero extension makes the identity exact, while hypothesis 3 is precisely what limits the number of these full-size differences.  Omitting either device fails this control.

- **One-prime toggle.**  Moving an odd prime \(r\) from one factor to the other is an ambient involution and reverses \(\chi _4(v)\) only when \(r\equiv3\pmod4\).  Its multiplicative displacement has size \(|\log r|\ge\log3\), not \(O(L^{-1/2})\), and it generally moves a cone point outside the cone.  The stated regularity gives no saving, so this route fails.

- **Complementation.**  Write \(N=dM\), where \(d\in\{1,2\}\), \(M\) is odd, and an allocation is \((u,v)=(da,b)\) with \(ab=M\).  Odd-factor complementation sends it to \((db,a)\).  The character changes by the fixed factor \(\chi _4(M)\), so it is not uniformly sign reversing.  If \(r=v/u\), the new ratio \(r'\) satisfies \(rr'=d^{-2}\); hence \(4<r<16\) maps completely outside the cone.  This route fails both the sign and locality controls.

- **Averaging involutions and exchange-graph matching.**  Averaging over all eligible prime pairs weights a vertex by the number of pairs split across its allocation; the weight can be zero and is not identically one.  Vertex-dependent normalization need not preserve an involution or detailed balance.  In the exchange graph, every usable edge is sign reversing and local, so a matching would validate its matched sector, but products with no eligible pair and allocations that co-locate every eligible pair are isolated.  The packet supplies no bound for unmatched mass.  Canonical selection removes multiplicity but does not create coverage.  Both routes therefore stop at a strict sector.

- **Ordered Abel and sliding Fejer.**  Formula (3.4) passes the exact algebra test but introduces uncontrolled character partial sums and uncontrolled divisor gaps.  Formula (3.5) passes the exact sliding-energy test while retaining one outer real part.  Taking absolute values of its shift correlations before a signed estimate discards the only possible cancellation and returns only a capacity-type bound.  No signed correlation estimate or geometry-compatible shift action is supplied, so neither connector proves (B184.3).

# 6. Dependencies and exact artifacts used.

Only the following two permitted artifacts were read or used:

1. `protocol.md`.
2. `rounds/codex-managed/m9-m1-hard-top-t1-comparable-factor-exchange-gate/blind_statement.md`.

No task brief, proof graph, active campaign, strategy file, prior round, kernel, source, sibling report, review, control artifact, conductor analysis, shared state, web source, or computation was read or used.

# 7. Recommended state effect.

**Revise.**  Retain (1.1), the ambient-involution proof, and the exact decomposition (3.2)--(3.3) as candidate finite lemmas.  Accept the \(O_\kappa(L^{3/2}\mathcal X)\) XOR-sector estimate only after explicitly confirming the disposable-loss convention (or strengthening the face hypothesis to a weighted one-loss bound).  Do not promote (B184.3): its exact residual has no supplied signed estimate.  The next admissible mechanism must establish (4.1), or an explicit signed transport/Fejer correlation relation that implies it, using information beyond fixed-product local exchange.
