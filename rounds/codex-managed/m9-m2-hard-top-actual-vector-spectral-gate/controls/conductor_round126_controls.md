# Round 126 conductor controls

Campaign: `m9-m2-hard-top-actual-vector-spectral-gate`

Starting graph SHA-256:
`85cf63f0087c6c6adf911bd0f7fdf5d3985a6a49b4e0d6158a7dc28470da10c9`

## Analytic controls

| Control | Outcome |
|---|---|
| Literal Round-75 vector | Green: exact (a_{\rm end}), hard affine range, zero extension, and character-before-square retained. |
| Diagonal and capacity | Green: diagonal (O(L^2)), coherent capacity (O(L^3)), target (O_\varepsilon(L^2X^\varepsilon)). |
| One orientation | Green: one (h<s) family and one outer (2\Re). |
| Square-product entry sector | Green: (hm=\square) gives (m=du^2,h=dv^2,u\le v\le2u), hence energy (O_\varepsilon(L^{3/2}X^\varepsilon)). |
| Square-sector connector | Green only by the norm triangle; no orthogonal energy decomposition or cross-term deletion. |
| Parity high-pass | Red as a gain: it selects the (pi)-mode and has multiplier of modulus (2) there. |
| General height-only filter | Green as a no-go dichotomy: retain (pi) and remain equivalent, or kill (pi) and require a separate estimate. |
| Ambient operator spectrum | Red as character information: diagonal character modulation is unitary and preserves singular values. |
| Fixed actual direction | Open: the required spectral-measure/one-sided real estimate is not proved. |
| Affine-support adversary | Green as a coefficient-blind obstruction only; it is not an actual-vector lower bound. |
| Square/Pell/fourth-power controls | Green for scope: they defeat automatic phase/parity gaps but do not lower-bound the complete physical energy. |
| Dyadic physical-offset inverse | Green with (O(\log L)) loss and every internal slab retained jointly. |
| Dyadic primitive-(q) inverse | Green only as a separate direct partition; an (r)-shell does not map to one (q)-shell because (r=gq). |
| Completed shell transfer | Open: Round 110 is a global real-part comparison, not a shellwise connector. |
| Downstream scope | Green: one strict hard-TOP entry sector and scoped obstructions only; every parent and exponent remains unchanged. |

## Tooling controls

- Analytical allocation: 100 percent; numerical allocation: zero percent.
- External theorem imports: none.
- Campaign validation: green with terminal status `complete`.
- State Patch: applied with 3 creates, 4 updates, 10 rejects, and 8
  no-change decisions; the resulting graph validates at
  `fd8831d74d53795182b9f8c234753b33df27e096b9d9f52a6cf43403c87c4a43`.
- Artifact hygiene: all 14 campaign files are strict UTF-8 with no lone CR,
  forbidden C0 byte, replacement character, trailing whitespace, or conflict
  delimiter.  The 10 authored mathematical/control artifacts are LF; the
  generated plan and three generated briefs are CRLF.
- Regression checks: 6 of 6 unit tests pass; bytecode compilation succeeds;
  graph validation succeeds; `git diff --check` succeeds with line-ending
  conversion warnings only.
