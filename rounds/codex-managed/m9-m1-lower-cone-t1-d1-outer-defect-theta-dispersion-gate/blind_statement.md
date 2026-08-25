# Blind statement for Round 155

Let $X$ be large,

$$
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 1\ll M\le R^2,\qquad K=\sqrt{NM}.
$$

Let $w_U$ be a literal zero-extended bounded-variation profile supported
on $n\asymp M$, with

$$
 \|w_U\|_\infty+\operatorname {Var}w_U
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
$$

Fix an arbitrary constant $A>0$ and a dyadic $V$ satisfying

$$
 M^{3/4}(\log(2X))^A<V\le K.
$$

Study the literal signed block

$$
 \mathcal Q_U(V)=
 \sum_{\substack{k\ge1,\ -k\le j\le k-1\\
 V<|j|\le2V,\ N\mid k^2-j\\
 (k^2-j)/N\ \mathrm{odd}}}
 \chi_4\!\left(\frac{k^2-j}{N}\right)
 w_U\!\left(\frac{k^2-j}{N}\right)e\!\left(-\frac{j}{2k}\right).
$$

All support components, asymmetric cell endpoints, positive and negative
defect branches, and transition endpoints are literal. The target is

$$
 |\mathcal Q_U(V)|\ll_{\varepsilon,A}X^\varepsilon.
$$

Independently determine whether a cancellation-preserving modular-root,
two-variable differencing, Poisson, dispersion, large-sieve, or another
signed cross-fibre argument proves the full target or a strict
owner-complete positive-power subrange. If not, identify the first exact
diagonal, collision, character, endpoint, coefficient-variation, or power
obstruction. Raw incidence counts, diagonal sizes, and positive terms in
upper bounds are not signed lower bounds.

Deliver exactly the seven report sections required by `protocol.md`. Use
only this statement and `protocol.md`; do not read claimant, strategy,
proof-graph, proof-draft, or sibling-report context.
