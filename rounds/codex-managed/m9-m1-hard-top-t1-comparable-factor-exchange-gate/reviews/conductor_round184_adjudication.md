# Conductor Round 184 adjudication

- Campaign: m9-m1-hard-top-t1-comparable-factor-exchange-gate
- Round: 184
- Role: authoritative round-closing mathematical decision
- Generated: 2026-08-27T22:25:38.7436539+08:00
- Starting graph SHA-256:
  a8e0e5d84c0c5047e0c96f11128dd215ae035bdd4355bd68ad28dc87afe6cfbd
- Decision status: mathematically closed; pending independent State Patch
  reverse audit and mechanical application

## 1. Result and terminal label

Round 184 closes mathematically under the strongest justified label

strict_hard_m1_t1_comparable_factor_sector.

Fix real \(X\geq2\), one literal middle or lower residual hard-M1 shell
\(L\), a sign \(\sigma\), and fixed \(\kappa>0\).  On the exact \(t=1\)
face, write \(N=uv\), with \((u,v)=1\), \(v\) odd, \(4u<v<16u\), and
\(N\) squarefree.  For each \(N\), select canonically from
\((N,L,\kappa)\), independently of the allocation \(N=uv\), at most one
pair of distinct odd primes \(\{p_N,q_N\}\mid N\) satisfying

\[
 \chi_4(p_Nq_N)=-1,\qquad
 |\log(q_N/p_N)|\leq\kappa L^{-1/2}.
\]

The complete selected-product XOR allocation sector, on which exactly
one selected prime divides the odd character leg \(v\), satisfies

\[
 |\mathcal T^{\rm cp}_{L,X,\sigma}|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.
\]

The selector may choose no pair for every supported product.  Thus this
is a possibly empty strict sector, not the complete \(t=1\) theorem.

## 2. Exact exchange proof

On an XOR allocation, interchange the two selected primes between the
legs.  Squarefreeness and coprimality make both quotients integral.  The
map is a fixed-point-free, multiplicity-one involution preserving
\(N=uv\), the square-root phase, squarefreeness, coprimality, parity, and
the allocation-independent selector, while

\[
 \chi_4(v')=\chi_4(v)\chi_4(p_Nq_N)=-\chi_4(v).
\]

After extending the literal coefficient by zero off every original
predicate, ambient reindexing gives

\[
 \mathcal T^{\rm cp}_{L,X,\sigma}
 =\frac12\sum_N\sum_{(u,v)\in\mathscr A_N^\oplus}
 \chi_4(v)e(\sigma\sqrt{XN})
 \{a(u,v)-a(\tau_N(u,v))\}.
\]

The physical support need not be invariant.  All coefficient-difference
estimates are therefore restricted to the orbit-closed active set on
which at least one of \(a(u,v)\) and \(a(\tau_N(u,v))\) is nonzero.
Both orbit legs then lie in a fixed \(O(L)\)-by-\(O(L)\) enlarged box.

The exact moving M1 factor is

\[
 \eta_L(u)\Phi\!\left(\frac{u}{H+1}\right)
 W\!\left(\sqrt{\frac{4q_Xu}{v}}\right)
 \left(\frac{L^2}{uv}\right)^{3/4}.
\]

The product power is invariant.  The close-pair hypothesis moves each
leg by \(O_\kappa(L^{1/2}+1)\).  Uniform \(C^1\) control gives an
\(O_\kappa(L^{-1/2})\) difference for the two smooth factors on common
cells.  Scale-normalized discrete BV of \(\eta_L\), charged only over the
active box, costs \(O_\kappa(L^{3/2})\).  Every literal vertical,
horizontal, ratio, support, plateau, crossing, floor, star, tie,
half-weight, and sampled-endpoint face has an
\(O_\kappa(L^{1/2}+1)\) collar and total weighted cost
\(O_{\kappa,\varepsilon}(L^{3/2}X^\varepsilon)\).  Hence

\[
 \sum_{\mathscr B}|a(u,v)-a(\tau_N(u,v))|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon,
\]

and triangle is taken only after the exact character-reversing pairing.

## 3. Exact residual and sufficient correlation

For a selected pair define

\[
 \rho_N(v)=1-\mathbf1_{p_N\mid v}-\mathbf1_{q_N\mid v}
           +2\mathbf1_{p_Nq_N\mid v},
\]

and put \(\rho_N(v)=1\) when no pair is selected.  Its selected-bit truth
table is \(1,0,0,1\), so the complete \(t=1\) face is exactly the proved
XOR sector plus the residual

\[
 c_{N,\sigma}^{\rm rem}
 =\mu^2(N)\sum_{\substack{v\mid N\\v\ {\rm odd}}}
 \chi_4(v)\rho_N(v)
 a_{L,X}^{\mathrm{lit},\sigma}(N/v,v).
\]

The residual contains every allocation of every no-pair product and the
neither/both allocations of every selected product.  Ambient
constant-amplitude sign balance on a selected product does not estimate
this physical residual.

At \(R=\lceil L\rceil\), zero-extended sliding Fejer energy and Cauchy
show that the following one-outer-real-part estimate is sufficient:

\[
 \Re\sum_{1\leq r<R}\left(1-\frac rR\right)
 \sum_Nc_{N+r,\sigma}^{\rm rem}\overline{c_{N,\sigma}^{\rm rem}}
 e\!\left(\frac{\sigma\sqrt X\,r}
 {\sqrt{N+r}+\sqrt N}\right)
 \ll_\varepsilon L^2X^\varepsilon.
\]

This estimate is open.  Taking a modulus separately at every shift
returns the \(L^2X^\varepsilon\) scalar capacity and supplies no saving.

## 4. First unproved step

The first owner-relevant missing theorem is the displayed exact residual
correlation, or an equivalent direct target estimate for the no-pair plus
neither/both residual.  No eligible-pair density or nonemptiness theorem
is available.  Even a future complete \(t=1\) proof leaves the
\(t\geq2\) small-\(G\) incidence remainder and the large-\(G\)
near-half-integer-resonant remainder open.

## 5. Controls and outcomes

All selector independence, integrality, multiplicity, fixed-point,
product, phase, squarefree, coprime, parity, character, zero-extension,
active-domain, common-cell, dyadic-BV, collar, endpoint, real-\(X\),
both-sign, residual truth-table, Abel, Fejer normalization, Cauchy-power,
blind-provenance, false-control, M2-transfer, downstream, and exponent
seams are GREEN after the bounded active-domain and provenance repairs.

One-prime toggling leaves the physical cone; normalized involution
averaging is a rewriting; all-\(1\bmod4\) products and supported
semiprimes show lack of automatic coverage but prove no density or lower
mass; ordered-divisor Abel leaves an uncontrolled oscillation; and
shiftwise positivity restores capacity.  No numerical or external
theorem evidence was used.

The repaired candidate and durable kernel are hash-locked at

- c514b10bed4c673618179c158258c362373696730c691900d250ed43e379e97f;
- 3387615b5522deeb4c63021fbdf4a665afa2c405052f2ff0868bed40338e602f.

## 6. Dependencies and evidence

The promoted strict sector depends on exactly:

1. M9-M1-hard-top-squarefree-radical-sector-reduction;
2. M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector;
3. M9-M1-top-endpoint-transform;
4. M9-M1-frequency-phase-diagram-R10;
5. H4-Phi-regularity;
6. M9-M2-dyadic-weight-nondegeneracy; and
7. Divisor-bound-elementary.

The M2 close-pair and residual-transport kernels are method controls only,
not theorem dependencies.  Three task reports, the repaired formal
candidate, first-pass seam reviews, independent final reviews, and the
post-repair provenance verification support the decision.

## 7. State decision and scope

The State Patch may create one subordinate proved_internal strict-sector
node, add it as a prerequisite and inconclusive evidence to the open
small-\(t\) owner, and reject the audited overclaims.  It must create no
implication edge to a complete owner and must not create a separate
proved residual-correlation node.

The complete residual, complete \(t=1\) face, all \(t\geq2\) small-\(G\)
incidences, the large-\(G\) near-resonant complement, complete small-\(t\)
owner, hard signed cone, smooth M1 parent, GAR, M9-M1, every M2 owner,
endpoint uniformity, M9, both bridges, and the quarter theorem remain
unchanged.  The internal exponent remains \(1/3\), the accepted external
benchmark remains \(0.3144831759740614\ldots\), and the target remains
\(1/4\).
