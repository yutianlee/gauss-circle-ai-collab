# Cross-gcd allocation/incidence post-repair verification

- Campaign: m9-m1-t1-p2-cross-gcd-cellular-boundary-gate
- Round: 199
- Scope: only the three repairs required by the independent allocation/incidence seam
- Artifacts checked:
  - rounds/codex-managed/m9-m1-t1-p2-cross-gcd-cellular-boundary-gate/candidates/formalized_hard_m1_t1_p2_cross_gcd_cellular_boundary_self_return.md
  - proofs/kernels/m9_m1_hard_top_t1_p2_cross_gcd_cellular_boundary_self_return.md

## Verification

1. **Canonical versus live domains.** The candidate now states after
   (199.K8) that each whole-allocation map is an involution on its
   canonical total zero-extended allocation domain. It separately
   restricts live-to-live use to \(m\) odd for \(\tau_L\), \(m'\) odd
   for \(\tau_U\), both odd for \(\tau_S\), and the transported literal
   support conditions. The durable kernel gives the same
   total-zero-extension qualification at (K199.3) and permits
   live-to-live use only after the appropriate odd-denominator and
   transported-support predicates. Neither artifact now asserts that
   \(B=1,C=1,E=1\) alone are full literal live-bijection hypotheses.

2. **Parity-safe triangle.** Both artifacts now justify the lawful
   \(B\)-\(E\)-\(C\) triangle separately. Since \(d,d'\) are odd and
   \(r\) is even, \(m,m'\) have equal parity. At the three triangle
   vertices \(E=(m,m')\in\{1,q\}\) with \(q\) odd; hence \(m,m'\)
   cannot both be even and are therefore both odd. Both artifacts also
   restrict literal live-to-live use to the transported-support
   intersection and retain all other support changes through total zero
   extension. This exactly closes the parity/support qualification.

3. **Exact \(P_1\) owner.** The candidate at (199.K19a) and the durable
   kernel at (K199.11a) now define

   \[
   P_1=\mathbf1_{|d-(d,d')m|>D_L}.
   \]

   Thus the proved inequality \(Aq|u-x|>D_L\) is explicitly identified
   as the lower-first-failure predicate. Both artifacts immediately
   state that no upper-far assertion is made. No remaining occurrence
   describes \(V_A\) as two-far or infers
   \(Aq|y-v|>D_L\).

All three requested repairs are present and mutually consistent. The
candidate and durable kernel preserve the earlier whole-swap/partial-block
distinction and require no further allocation/incidence wording repair.

**PASS**
