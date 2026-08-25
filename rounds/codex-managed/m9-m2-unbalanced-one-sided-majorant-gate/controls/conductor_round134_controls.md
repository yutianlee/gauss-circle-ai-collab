# Round 134 conductor controls

Campaign: `m9-m2-unbalanced-one-sided-majorant-gate`

Starting graph SHA-256:
`40e83c20e83d542e43aa739931f4b89ea76f4541506fb44ef219ce31dca35024`

## Mathematical seam matrix

| Control | Exact test | Outcome |
|---|---|---|
| literal block square | Form (A(k)=sum_pchi_4(p)b_{p,k}) before every modulus and use zero extension. | Green. Parseval gives the exact (F_H=|D_H|^2) multiplier with all entries and exits. |
| order type | Compare universal quadratic-form order, multiplier order, coefficientwise order, and actual-family-only order. | Green. Universal Toeplitz PSD order is equivalent to (Tge F_H) pointwise; coefficientwise order is false. |
| Fejer bandwidth | Expand the exact multiplier. | Green. (F_H) is already nonnegative of exact degree (H-1), integral (H), and height (H^2). |
| sharp lower bound | Average a degree-((N-1)) majorant over (N)-th roots and fold (0,ldots,H-1) by residues. | Green. The exact lower bound is ((N-s)m^2+s(m+1)^2). |
| extremizer | Test (T^*=|mD_N+D_s|^2) pointwise. | Green in blind, discovery, hostile, and conductor derivations. The difference factors as a nonnegative sum of squares. |
| physical inequality | Apply Parseval to the folded coefficient vector. | Green globally after summing all translations; a block-by-block pointwise claim is rejected. |
| (L^1) and Fourier mass | Compute the constant coefficient, excess, and autocorrelation coefficients of the folded vector. | Green. Exact excess is (Nm(m-1)+2ms), and the coefficient (ell^1)-mass is (H^2). |
| bandwidth capacity | Compare (N)-shift shortening with (ho=mu_N(H)/H). | No-go. (hoge H/N); choosing (Nle H/min(H,Q)) returns the entire old deficit. |
| lagwise closure | Put every folded lag in a modulus at natural diagonal scale. | No-go. Total coefficient mass (H^2) restores factor (H). |
| physical-window placement | Test a nonproportional larger window on phase-adapted complex data. | Red. A universal rank-one window majorant must be a scalar multiple and cannot shorten support. |
| character placement | Test opposite identical (chi_4)-rows, one row, absolute characters, and random signs. | Green as structural controls. Only a majorant after the combined (p)-sum retains actual cancellation. |
| literal-capacity qualification | Compare the folded zeroth term with (mathcal D_0). | Green correction. It is the full cross-(p) character norm, so (ho) is not a literal lower bound. |
| character Poisson | Recompute the Gauss factor, saddle, Gaussian unit, profiles, and final coefficient. | Green. The factor is (i/2), and the principal row has coefficient (1/k) and reciprocal phase (Mk/u). |
| reciprocal Gram | Substitute the principal rows into the folded quadratic form. | Green as a principal module; it retains shifts, conjugates, characters, profiles, and the same folded weights. |
| endpoint scope | Split exact Poisson into principal and remainder rows. | Red for the principal Gram alone. Endpoint completeness requires every principal--remainder and remainder--remainder term in the weighted remainder. |
| downstream scope | Compare graph dependencies. | Green. Only a finite lemma and scoped obstruction are promoted; all endpoint parents and exponents remain unchanged. |

## Post-unmask and artifact corrections

1. The sampling lower bound is sharp, not merely order-sharp: the folded
   majorant attains it exactly.
2. The two-grid Fejer construction remains valid but is not extremal.
3. A strict one-sided global contraction exists; the no-go concerns its
   exact capacity, not its existence.
4. The valid folded inequality is global after all translations, not
   pointwise for one block.
5. The factor (mu_N(H)/H) is a universal positive-closure obstruction,
   not a lower bound for the literal character family.
6. The character-Poisson normalization and principal reciprocal Gram are
   correct; their endpoint-complete use requires the full remainder.
7. Both analytic reports were repaired by their owners to balanced TeX,
   strict UTF-8, and no hidden control characters. One final trailing space
   was removed mechanically by the conductor without changing content.

## Validation record

- State Patch validated and applied cleanly: 2 creates, 4 updates,
  12 rejections, and 7 explicit no-change records.
- Resulting graph SHA-256:
  `f9aa6fa43900b9cb73f705405f9a6090e6e84fb5d3c8a9e037ffe3c6911b9ea0`.
- Current graph: green under structural, dependency, and evidence-path
  validation.
- Completed campaign manifest: green.
- Unit tests: six of six passed.
- Source compilation: `math_collab` and tests green.
- JSON parsing: active campaign, next-round plan, round ledger, and State
  Patch green.
- Artifact hygiene: the full campaign is strict UTF-8 with no unexpected
  C0/DEL bytes, replacement characters, trailing whitespace, conflict
  markers, or unbalanced inline/display delimiters.
- Diff check: green, with line-ending warnings only.

No numerical experiment or web theorem import was used. The round was
100% analytical and algebraic.
