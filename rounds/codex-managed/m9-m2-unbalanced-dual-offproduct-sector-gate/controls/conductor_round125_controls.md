# Round 125 conductor controls

Campaign: `m9-m2-unbalanced-dual-offproduct-sector-gate`

Starting graph SHA-256:
`27bd4173fbdb16e5689595a02d42d82ffa8bb514b4610ea745ce2da6e2b8b152`

## Analytic controls

| Control | Outcome |
|---|---|
| Literal Round-124 survivor | Green: exact Fejer expansion gives (S_{\rm off}=E_\chi-D_0) with no boundary remainder. |
| One-sided sign localization | Green: (E_\chi\ge0), so the negative tail is bounded by the proved diagonal. |
| Target equivalence | Green: the missing absolute estimate is exactly the positive upper bound for (E_\chi). |
| Equal/unequal sector interface | Green after retaining both together; a two-row adversary proves coefficient-blind separate bounds can be overstrong by (H). |
| Complete fixed-row curvature bound | Green at (X^{1/2+\varepsilon}\min(H,Q)), not at the square target. |
| Regime ledger | Green after replacing a universal (Q)-loss by (min(H,Q)). |
| Principal saddle constant and profile | Green on fixed interiors: coefficient (-2i/p), profile (W(Xd/(DM))q_L((X/M)p)), and (Q) dual labels. |
| Principal second B-process | Green as a local self-return only; no endpoint-complete transform or saving. |
| Odd-(p) coherence | Green after the half-integer (A,E_d^*) repair and the factor ((-1)^A). |
| Fixed-((n,d,d')) mode interval | Red for the proposed far argument: its length is (O(1/H)), not (L). |
| Moving overlap and hard faces | Open; no target-safe aggregate floor/Fresnel/error ledger. |
| Capacity | Green as an unsigned diagnostic only; no diagonal lower bound is inferred. |
| Downstream scope | Green: one flat-smooth strict-UNBAL owner only, with every parent and exponent unchanged. |

## Artifact and tooling controls

- Campaign validation: green with all three reports complete.
- State Patch validation against the starting graph: green before application.
- Seven authored candidate/report/review/synthesis/patch artifacts: UTF-8/LF,
  no C0 or replacement characters, trailing whitespace, or conflict markers.
- Generated immutable plan and briefs retain platform CRLF; no stray C0 or
  replacement characters occur in them.
- Unit tests: six of six green.
- Python compilation of `math_collab` and `tests`: green.
- Diff delimiter and trailing-whitespace check: green; only Git's
  repository-wide line-ending conversion warnings remain.
- Numerical allocation: zero percent.
- External theorem imports: none.

The State Patch applied two creates, five updates, twelve rejected shadows,
and eight no-change decisions. The validated resulting graph SHA-256 is
`85cf63f0087c6c6adf911bd0f7fdf5d3985a6a49b4e0d6158a7dc28470da10c9`.
