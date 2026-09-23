# Round 188 bounded Wolfram lift-partition control

- Campaign: `m9-m1-t1-high-h-imprimitive-lift-gcd-gate`
- Round: 188
- Evidence level: `diagnostic_only`
- Script: `controls/lift_partition_exact_check.wls`
- Script SHA-256:
  `7bad1b482654e69325feaf844d359d1643a3245c8e990742ecfc83141e995b99`
- Runtime: WolframScript, local desktop installation

## Purpose and pass rule

This bounded finite control checks only the algebraic lift normalization
and partition used by the analytical proof.  It cannot prove an
asymptotic estimate.  The run passes exactly when every Boolean test is
true and the process exits with code zero.

The script checks:

1. every odd modulus (3\le U\le101) and every (1\le k<U) has the
   unique data (m=(k,U)), (U=mq), (k=ma), ((a,q)=1);
2. (c_U(k)=m^{-1}c_q(a)) and
   (e(k\bar vh/U)=e(a\bar vh/q)) to 60-decimal-place tolerance over
   the stated finite grids;
3. (|k|_U=m|a|_q);
4. the predicates (Qm\ge Y) and (Qm<Y) partition the selected high
   modes disjointly for the finite (Q,Y,U) grid;
5. (sum_{U\mid n}\tau(U)=\tau_3(n)) for (1\le n\le250); and
6. the two near-half modes are primitive and retain combined squared
   coefficient mass at least (8/\pi^2).

## Command

```powershell
& 'C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe' -file 'rounds/codex-managed/m9-m1-t1-high-h-imprimitive-lift-gcd-gate/controls/lift_partition_exact_check.wls'
```

## Repair trace

The first run found exactly one failed divisor test, at (n=1).  The
cause was a diagnostic-only implementation convention:
`FactorInteger[1]` was interpreted by the generic product formula as
`{{1,1}}`.  The script was repaired by defining the empty-product case
`productTripleCount[1] := 1`.  No mathematical statement, campaign
artifact, or proof-state file changed.  The repaired script was then
rerun from the beginning.

## Final output

```text
odd_moduli_checked=50
lift_checks=12750; failed=0
phase_checks=265852; failed=0
partition_checks=1200; failed=0
divisor_checks=250; failed=0
near_half_checks=50; failed=0
overall=PASS
```

Process exit code: `0`.

## Limitation

The control checks finite normalization, finite partitioning, and a
finite divisor identity grid only.  It gives no bound for the literal
endpoint amplitudes, no cancellation in the primitive or moderately
imprimitive complement, no large-(X) uniformity, and no theorem or
exponent evidence.  The target-safe sector rests on the analytical
atom-count and divisor-summation proof, not on this computation.
