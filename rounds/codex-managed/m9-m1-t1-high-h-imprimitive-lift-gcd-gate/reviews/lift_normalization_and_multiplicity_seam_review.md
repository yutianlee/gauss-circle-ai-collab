# 1. Result and verdict

**Verdict: AMBER.** The lift normalization, orientation signs, dyadic atom
count, complex partition, and multiplicity ledger are algebraically correct.
I found no lost or duplicated Fourier mode and no illicit assumption
`(m,q)=1`. Promotion of the displayed target-safe bound (188.K9), however,
is not yet justified from the permitted antecedents.

The first promotion-blocking defect is (188.K1): neither permitted antecedent
kernel states or proves the asserted support relation `L << X^(1/4)`, while
(188.K19) uses it essentially to absorb `Q log^O(1)(2LQ)` into `X^epsilon`.
Under the rule not to infer hidden support regularity, the word “inherited” is
unsupported. If (188.K1) is made an explicit uniform hypothesis and a valid
connector proves it for every intended literal shell, then
(188.K4)--(188.K21) and (188.K23), including (188.K9), pass this seam.

There is one minor exact-definition repair as well: (188.K22) uses the
inverse `bar(q) mod v`, although the carrier permits `v=1`. The reciprocity
identity is correct for `v>1`, and the `v=1` case is correct after the
convention `bar(q)=0 mod 1`, but that convention or a separate `v=1` line
must be written.

# 2. Exact reviewed claim and hypotheses

I reviewed candidate SHA-256
`6727fa040e0088692e09dbc365e535f7324cf04313223b648eb1b7406d6e7e14`
only against the two assigned antecedent kernels.

For a Round-187 high mode with odd `U>1`, representative `1<=k<U`, and

```text
U > 4Q,    q_U(k)=U/(k,U) > Q,    |k|_U > Q,
```

put `m=(k,U)`, `q=U/m`, and `a=k/m`. Retain the complete Round-185
carrier

```text
kappa,g,h,U,v > 0;  kappa,g,U odd;
(gU,v)=1;  (U,h)=1;  0 < 2 kappa g h < R_0,
```

both orientations, their canonical anchors and affine positivity sets, and
the literal amplitudes. Split the exact complex Round-187 high aggregate by
`Qm>=Y` and `Qm<Y` before applying a real part or a triangle inequality.
The intended strict-sector conclusion is

```text
|I_(Y,Q)^sigma| <<_(B,epsilon) L^2 X^epsilon.                 (188.K9)
```

The proof is valid under the additional quantitative hypothesis
`2<=L<=C X^(1/4)` with a uniform fixed `C`. The candidate asserts this as
inherited support, but the Round-185 kernel only records `d,m asymp L`,
`N asymp L^2`, and literal zero extension, while the Round-187 kernel
records no relation between `L` and `X`. This seam therefore cannot certify
the assertion for the intended physical shells from the allowed dependencies.

# 3. Derivation and line checks

## 3.1 Unique lift coordinates and normalization

For `1<=k<U`, `m=(k,U)<U`, so `q=U/m>1` and `a=k/m` satisfies
`1<=a<q`. Moreover

```text
(a,q)=1,    U=mq,    k=ma.
```

Conversely, for any `U=mq` and `1<=a<q` with `(a,q)=1`,

```text
(ma,mq) = m(a,q) = m.
```

This proves the bijection without, and independently of, any condition on
`(m,q)`. Shared prime factors of `m` and `q` cause neither loss nor
duplication. Thus (188.K4)--(188.K5) pass.

Direct substitution gives

```text
c_(mq)(ma) = 2/[mq{1+e(-a/q)}] = m^(-1)c_q(a).
```

Since `(v,U)=1` and `q|U`, an inverse of `v mod U` reduces to the
inverse of `v mod q`, and hence

```text
e(epsilon_omega k bar(v) h/U)
  = e(epsilon_omega a bar(v) h/q).
```

For the specified representatives,

```text
|ma|_(mq) = min(ma,mq-ma) = m min(a,q-a) = m|a|_q.
```

Because `U` is odd, both `m` and `q` are odd. For `q>1`,

```text
|c_q(a)| = 1/[q |cos(pi a/q)|].
```

Writing `r=|q-2a|`, which is a positive odd integer, gives
`|cos(pi a/q)|=sin(pi r/(2q))`. Enlarging from units to all
`1<=a<q`, with at most two residues per `r`, and using the standard lower
bound for sine on `[0,pi/2]`, gives

```text
sum_((a,q)=1) |c_q(a)| << sum_(1<=r<=q, r odd) 1/r << log(2q).
```

Thus (188.K6), (188.K13), and (188.K14), including the parity-dependent
odd-`q` normalization, pass.

## 3.2 Carrier and orientation signs

The candidate retains the Round-185 carrier by reference rather than
altering it. With `S=S_(t,omega)` and `w=w_(t,omega)`, the inherited
primitive equations are exactly

```text
h = Sv-Uw       (omega=+),
h = Uw-vS       (omega=-).
```

For `epsilon_+=1` and `epsilon_-=-1`, reduction modulo `q|U` gives in
both cases

```text
epsilon_omega bar(v) h = S  (mod q).
```

Since `S=S_(0,omega)+Ut` and `q|U`,

```text
e(epsilon_omega a bar(v) h/q)
  = e(aS/q) = e(a S_(0,omega)/q).
```

The signs in (188.K20)--(188.K21) are therefore correct, and the lifted
phase is constant along the affine `t`-ray. The original `(-1)^t`, both
orientations, and the single enclosing real part are not removed or
duplicated.

For `v>1`, additive reciprocity (188.K22) follows from

```text
bar(v)/q = -bar(q)/v + 1/(qv)  (mod 1).
```

For `v=1`, allowed by the carrier, it needs the explicit convention
`bar(q)=0 mod 1` or a separate trivial verification. This definition gap
does not enter the proof of (188.K9), but it prevents an unqualified GREEN
for every displayed identity.

## 3.3 Dyadic atom count, including endpoint terms

Put `u=gU`. The Round-187 kernel gives

```text
u,v asymp L/kappa,    h << U.
```

At fixed `(kappa,u,U,h)`, `g=u/U` is uniquely fixed. There are
`O(L/kappa)` admissible values of `v`. The affine interval contains
`O(1+kappa)` sites, including a possible terminal site; because `kappa`
is a positive integer, this is `O(kappa)`. The terminal Fejer factor,
literal masks, and zero extensions have absolute value at most their
unrestricted atom and cannot increase this count.

Also `Q>=1` for `X>=2`, and `Y>Q`, so

```text
#{integer h: Y<h<=2Y} <= Y+1 <= 2Y.
```

Multiplication by the two orientations and the inherited `X^eta` bound for
each literal amplitude gives

```text
sum_(Y<h<=2Y) sum_(v,omega,t) |B_(f,omega)^sigma(t)|
  <<_eta Y L X^eta
```

at fixed `(kappa,u,U)`. Thus (188.K15)--(188.K16) pass, including the
affine “+1”, a terminal affine site, a terminal dyadic height, and both
orientations.

## 3.4 Divisor ledger and multiplicity

At fixed `U=mq`, summing the exact coefficient over unit `a` costs
`O(m^(-1) log(2q))`. Combining this with the atom count proves (188.K17).
On `Qm>=Y`, one has `Y/m<=Q`.

The reindexing `(g,U) <-> (u,U)`, with `u=gU` and `U|u`, is bijective.
At fixed `U`, the lift representation is also bijective, so

```text
sum_(U|u) sum_(q|U) 1 = sum_(mq|u) 1 = tau_3(u).
```

This is the ordered factorization `u=g m q`. No pairwise coprimality among
`g,m,q`, and in particular no `(m,q)=1`, is used. Relaxing the high-mode
and unit restrictions for an upper bound only adds positive terms; it does
not reassign a physical mode. Consequently there is no multiplicity loss in
(188.K18).

Elementary summation gives

```text
sum_(kappa<<L) sum_(u asymp L/kappa) tau_3(u) log(2u)
  << L log^O(1)(2L),
```

and hence the unconditional output of the displayed ledger is

```text
|I_(Y,Q)^sigma| <<_eta Q L^2 log^O(1)(2LQ) X^eta.
```

This verifies the counting and all `Y/m` payment. Passing from this line to
(188.K9) is valid if (188.K1) is available uniformly, but not from the two
permitted antecedents alone.

## 3.5 Exact complex split and complement

Every high mode has exactly one positive integer `m`. The predicates
`Qm>=Y` and `Qm<Y` are disjoint and exhaustive, including the equality
boundary in the strict packet. They are inserted into the complex aggregate
`R_(Y,Q)^sigma` itself, before any real part or triangle inequality.
Therefore

```text
R_(Y,Q)^sigma = I_(Y,Q)^sigma + C_(Y,Q)^sigma
```

is exact. Under the lift bijection the complement is precisely

```text
mq>4Q,    q>Q,    m|a|_q>Q,    Qm<Y,
```

with the inherited carrier still imposed. A triangle majorant for this
subset is bounded by the Round-187 full high-packet majorant, giving only
`O_epsilon(YL^2 X^epsilon)`. Thus (188.K7)--(188.K8) and
(188.K10)--(188.K12) pass.

The two near-half modes in (188.K23) have `|a|_q=(q-1)/2>Q` when
`q>4Q`, and

```text
|c_q(a)| = 1/[q sin(pi/(2q))] >= 2/pi,
```

so their combined squared mass is at least `8/pi^2`.

# 4. First doubtful step and exact repairs

The first doubtful step is candidate lines 20--27, equation (188.K1), not
the lift algebra. The two permitted kernels fix `X` and `L` and describe
literal support, but neither contains `L << X^(1/4)` or an equivalent
polynomial relation. Without it, the proof stops at (188.K19) with an
unabsorbed `log^O(1)(2LQ)`. It is not legitimate under this review brief to
infer the missing relation from the phrase “hard-M1 shell.”

Required repair 1, either form:

1. Add an accepted, hash-bound support connector proving uniformly that every
   intended nonempty middle/lower hard-M1 shell satisfies
   `2<=L<=C X^(1/4)`, with literal zero extension outside.
2. Restate the candidate explicitly as conditional on that inequality and
   separately prove that the downstream physical carrier satisfies the new
   hypothesis.

Merely retaining the word “inherited” is insufficient. If no such connector
is supplied, the conclusion must retain the factor
`Q log^O(1)(2LQ)` rather than claim (188.K9).

Required repair 2: in (188.K22), define `bar(q)=0` for modulus `v=1`, or
state the reciprocity identity for `v>1` and add the one-line `v=1` identity

```text
e(epsilon a h/q) = 1 * e(epsilon a h/q).
```

# 5. Controls

The analytical checks above are the certification basis. I also inspected
only the permitted Round-188 diagnostic
`controls/conductor_round188_wolfram_lift_partition_check.md`, SHA-256
`4d6173c31bfe63e158f5d07d90488808e65d6b81a58d5e428ed1e01ae69bcb42`.
Its repaired finite run reports:

```text
lift_checks=12750; failed=0
phase_checks=265852; failed=0
partition_checks=1200; failed=0
divisor_checks=250; failed=0
near_half_checks=50; failed=0
overall=PASS
```

This is consistent with the unique lift, phase reduction, distance scaling,
partition, triple-divisor identity, and near-half mass. It does not test the
literal atom bound, the `L`-to-`X` support assertion, or any asymptotic
estimate, and it is not theorem evidence. No numerical result upgrades the
verdict.

# 6. Dependencies and hashes

The exact files used were:

| artifact | SHA-256 |
|---|---|
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| Round-188 formal candidate | `6727fa040e0088692e09dbc365e535f7324cf04313223b648eb1b7406d6e7e14` |
| `proofs/kernels/m9_m1_hard_top_t1_residual_fejer_tangent_gcd_reduction.md` | `4603554dec10748516c240123f1e847b8f7b3162fa399e94b061c3416fd2a160` |
| `proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md` | `a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2` |
| optional Round-188 Wolfram report, diagnostic only | `4d6173c31bfe63e158f5d07d90488808e65d6b81a58d5e428ed1e01ae69bcb42` |

I did not inspect the claimant's discovery, hostile, blind, reconciliation,
state, graph, synthesis, plan, or validation artifacts. No external theorem
was used.

# 7. Recommended state effect

**Revise; do not promote the candidate yet.** Preserve the lift-coordinate,
coefficient, phase, least-distance, parity, carrier-sign, atom-count,
complex-split, complement, and multiplicity derivations: those pass. Repair
the provenance or explicit-hypothesis status of (188.K1), and repair the
modulus-one inverse convention in (188.K22), then obtain a focused post-repair
verification against the same frozen candidate dependencies.

No rejection of the strict-lift mechanism is recommended. Until the first
repair is supplied, however, the only certified bound from the permitted
packet is

```text
|I_(Y,Q)^sigma| <<_eta Q L^2 log^O(1)(2LQ) X^eta,
```

not the target-safe (188.K9). The exact complement and every downstream
high-height, original-`t=1`, parent, bridge, theorem, and exponent claim
remain open.
