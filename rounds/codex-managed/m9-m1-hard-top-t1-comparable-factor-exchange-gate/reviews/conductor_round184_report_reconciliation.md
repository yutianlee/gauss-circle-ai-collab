# Conductor Round 184 report reconciliation

- Campaign: `m9-m1-hard-top-t1-comparable-factor-exchange-gate`
- Task: `conductor_round184_report_reconciliation`
- Role: conductor selection of the smallest reviewable proof kernel
- Generated: `2026-08-27T21:43:07.5300757+08:00`
- Starting graph SHA-256:
  `a8e0e5d84c0c5047e0c96f11128dd215ae035bdd4355bd68ad28dc87afe6cfbd`
- Evidence status: conductor reconciliation; no proof-state edit

## 1. Selected result

The complete hard-M1 \(t=1\) estimate is not proved.  The smallest
candidate worth independent seam review is the canonical comparable-prime
XOR incidence sector, together with its exact residual:

\[
 |\mathcal T^{\rm cp}_{L,X,\sigma}|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.
\tag{184.R1}
\]

The selected pair is a canonical function of \((N,L,\kappa)\), not of
the allocation \(N=uv\), satisfies

\[
 \chi_4(p_Nq_N)=-1,
 \qquad |\log(q_N/p_N)|\leq\kappa L^{-1/2},
\tag{184.R2}
\]

and the sector consists of allocations for which exactly one selected
prime lies on the odd character-bearing leg \(v\).  Products with no
selected pair and the selected-pair neither/both allocations form the
exact residual.  No existence, density, or positive-proportion assertion
is part of the candidate.

## 2. Reconciliation of the three reports

All reports agree on the following finite algebra.

1. The \(t=1\) face is exactly \(G=\rho=1\), equivalently
   \((u,v)=1\) and \(uv\) squarefree, with multiplicity one.
2. Exchanging the selected primes is an integral, fixed-point-free,
   multiplicity-one involution of the complete ambient XOR set.
3. It preserves \(uv\), the radical phase, squarefreeness, coprimality,
   parity, and the selector, while reversing \(\chi_4(v)\).
4. Zero extension gives the exact paired-difference identity even when a
   partner crosses the cone or another literal face.
5. The exact residual is no-pair plus selected-pair neither/both.
6. Ordered-divisor Abel summation and the sliding Fejer identity are exact
   connectors, but positivity or shiftwise triangle returns the
   \(L^2X^\varepsilon\) capacity.

The reports differ only at the literal M1 coefficient seam.  The hostile
transfer audit correctly shows that the accepted M2 sector theorem does
not itself imply the M1 coefficient-difference and collar bounds: M2
profiles its odd character leg in a different physical window.  This
rejects direct theorem transfer, but it is not a counterexample to the M1
sector.

The discovery report instead derives the required estimate directly from
the accepted M1 factorization.  That factorization is independently
available in `M9-M1-top-endpoint-transform`,
`M9-M1-frequency-phase-diagram-R10`, and the exact stationary formula
checked in Round 183: after normalization the moving factors are the
scale-BV frequency profile \(\eta_L(u)\),
\(\Phi(u/(H+1))\), \(W(\sqrt{4q_Xu/v})\), and a product-only power.
The remaining literal data are fixed parameters or a fixed finite family
of one-variable or ratio support faces.  Thus the M1 estimate can be
proved without importing the M2 estimate.

The blind report independently confirms the exchange algebra and the
residual obstruction.  Its isolated packet counted exceptional sites as
\(O(L^{3/2}\mathcal X)\) and also allowed coefficient size
\(O(\mathcal X)\), which literally produces \(\mathcal X^2\).  The
formal candidate removes this notational ambiguity: the lattice collar
count is \(O_\kappa(L^{3/2})\), and the coefficient-weighted collar cost
is \(O_{\kappa,\varepsilon}(L^{3/2}X^\varepsilon)\).  No unrecorded
loss multiplication is used.

## 3. Exact remaining gap

Writing \(c_{N,\sigma}^{\rm rem}\) for the complete residual row
coefficient, the first diagonal-safe sliding scale is
\(R=\lceil L\rceil\).  A sufficient still-open relation is

\[
 \Re\sum_{1\leq r<R}\left(1-\frac rR\right)
 \sum_N c_{N+r,\sigma}^{\rm rem}
 \overline{c_{N,\sigma}^{\rm rem}}
 e\!\left(\frac{\sigma\sqrt X\,r}
 {\sqrt{N+r}+\sqrt N}\right)
 \ll_\varepsilon L^2X^\varepsilon.
\tag{184.R3}
\]

There is one outer real part.  The relation is not supplied by either M2
kernel.  Taking absolute values per shift yields only the original
\(L^2X^\varepsilon\) scalar capacity.  Products whose odd primes are all
\(1\pmod4\), supported semiprimes with far factors, and one-prime toggles
show why fixed-product local exchange alone cannot cover the residual.
These are mechanism controls, not lower bounds for the literal sum.

## 4. Selection and scope

The formalized candidate is
`candidates/formalized_hard_m1_t1_comparable_factor_exchange_sector.md`.
It must receive independent reviews of:

- selector, exchange, character, and multiplicity algebra;
- the actual M1 profile, aggregate BV charge, every literal collar,
  endpoint, and restored power; and
- the residual/Fejer no-go, blind post-unmask consistency, owner scope,
  and exponent quarantine.

Until those reviews are GREEN, (184.R1) remains candidate evidence only.
Even if promoted, it is a possibly empty strict incidence sector, not the
complete \(t=1\) face.  The complete \(t=1\) residual, all \(t\geq2\)
small-G incidences, the large-G near-resonant complement, the complete
small-\(t\) owner, both M1 parents, every M2 owner, endpoint uniformity,
M9, both bridges, the quarter theorem, and both exponent ledgers remain
unchanged.
