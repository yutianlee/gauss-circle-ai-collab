# Verdict

**GREEN.**  All three requested discovery-report repairs are present exactly,
the candidate hash is unchanged, and the repairs preserve the discovery
theorem and its strict-sector scope.

# Exact checks

1. **Report (2.19), lines 303--309: PASS.**  The displayed transformed
   codomain now includes (U>1):

   \[
   \kappa,u,U,h,v>0,\qquad U>1.
   \]

   This matches the stated source sector and removes the spurious (U=1)
   tuples.  All inverse data remain the same: (U\mid u), (g=u/U), and
   (n=(u/U)h).  No carrier or count is changed.

2. **Report (3.5), lines 470--474: PASS.**  The centering identity now states
   the required hypothesis (a\not\equiv0\pmod U).  Its application remains
   valid because (a=\bar v h) is a unit modulo (U), from
   ((gU,v)=1) and ((U,h)=1).  No orientation algebra is changed.

3. **Report (3.20), lines 734--739: PASS.**  The displayed energy sum now
   contains both retained-mode conditions

   \[
   q_U(k)>Q,\qquad |k|_U>Q.
   \]

   For odd (U>4Q), the two witnesses (k=(U\pm1)/2) still satisfy
   (q_U(k)=U>Q) and (|k|_U=(U-1)/2>Q), and each has
   (|c_U(k)|\ge2/\pi).  Hence the corrected retained-vector bound
   (8/\pi^2) follows exactly.

These changes only make previously used hypotheses and the actual retained
frequency set explicit.  They do not alter the exact Fourier decomposition,
the target-safe packet, the (O(YL^2X^\varepsilon)) positive remainder
capacity, the self-return obstruction, or the identification of the still-open
one-sided estimate.

# Hashes

| Artifact | SHA-256 |
|---|---|
| Repaired `reports/literal_height_fourier_attack.md` | `4433de37846caa4c9ae0d51ba874221851a331e4a6af13043d4da0f0749ac298` |
| `candidates/formalized_hard_m1_t1_high_h_inverse_residue_conductor_reduction.md` | `528c137d7da9dc4de2a892513ee2296ad0c25cbc119692db4575415adac15514` |

The discovery report's pre-repair hash recorded by the seam review was
`319facc926335e039cf6569bef8d49b1cac4ac09188adf888c5e22c5a7e6bc64`.
The candidate remains byte-for-byte at its pre-review and pre-repair hash
`528c137d7da9dc4de2a892513ee2296ad0c25cbc119692db4575415adac15514`.

# State recommendation

Retain the prior **GREEN** recommendation: promote only the strict
`M9-M1-hard-top-t1-high-h-inverse-residue-conductor-reduction` as
`proved_internal` evidence under
`strict_high_h_inverse_residue_fourier_sector`.  Keep (187.K8), the complete
high-height target, the original (t=1) residual, all (t\ge2) and
near-resonant complements, all parents, bridges, theorem nodes, and exponent
claims open.  No further normalization/multiplicity repair or repeat review is
required.
