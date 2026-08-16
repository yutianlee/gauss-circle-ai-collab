# Round 88 conductor review: normalization, coarse count, and ownership

## Verdict

Certify the congruence-aligned coarse-shell lemma at its literal scope.
It removes every cross-group physical-pair shell whose first coarse
coincidence quotient satisfies

\[
 R_*\leq R_{\rm crit}(B)=J^{11/30}B^{-2},
\]

with the understood cap \(R_*\leq M\). It does not classify functional
periods of the completed rational phase.

## Normalization

The physical row is

\[
 \mathcal R_{b,x}=M^{-1}\sum_n I_b(n)e_M(nx)e(n\theta),
\]

so an ordered-pair function already contains \(M^{-2}\). No further
factor is inserted. The accepted bound

\[
 \|\Pi_{b,D}F_{b,P}\|_\infty
 \ll_\varepsilon X^\varepsilon T^2Q^{-5/12}
\]

therefore contributes \(T^4Q^{-5/6}\) after forming a group square.

## Coarse group count

For \(m\mid M\), write \(R=M/m\), and group a physical ordered pair by
its Round-87 active-set/active-label class after reduction modulo \(m\).
The empty coarse active set must be retained: a fine off-diagonal pair
may become diagonal modulo \(m\).

For a coarse active set \(S\), there are at most \(m_S^2\) active labels,
at most \(r_S=m/m_S\) inactive common units per label, and at most
\(R^2\) fine lifts per coarse ordered pair. Hence

\[
 \sum_\gamma |K_{b,m,\gamma}|^2
 \ll_\varepsilon X^\varepsilon
 M^2R^2T^4Q^{-5/6}.
\]

After the \(O(B)\) conductors and Fejer mass, this is

\[
 X^\varepsilon DB^3R^2T^4Q^{-5/6}.
\]

This argument is insensitive to prime-power factorization, the full
\(2\)-part, nonunit \(K\), and perfect-power phases.

## Signed ownership

Use

\[
 \mathcal K_D^\circ=|D_D|^2-D,
 \qquad \|\mathcal K_D^\circ\|_1\leq2D.
\]

Its zero Fourier coefficient vanishes, so the globally owned \(u=0\)
term is not restored. Local divisor-lattice differences give exact
first-coincidence shells and cost only \(X^\varepsilon\). They act on
the complete physical rows, so signs, Ramanujan cross terms, shifted
support, and the fourfold symbol are retained.

## Exponent check

The ratio to \(X^\varepsilon(D/B)J^{14/5}\) is

\[
 R^2B^4J^{-11/15}.
\]

Thus \(R\leq J^{11/30}B^{-2}\) is exactly target-safe. At the top
\(B=J^{3/20}\), this is \(R\leq J^{1/15}\); at the lower endpoint it
reaches \(R\asymp M\).

The exact finite diagnostic in `controls/coarse_group_mobius_check.py`
confirmed the divisor-shell identity and lift square count for several
composite and prime-power moduli, including the hostile \(R=3\) family.
It is diagnostic only; the proof above is algebraic.

## Scope

This review rejects the identification of coarse group depth with every
masked, affine, nonunit-\(K\), or extra \(2\)-adic functional period.
Only the congruence-aligned physical shells are certified.

