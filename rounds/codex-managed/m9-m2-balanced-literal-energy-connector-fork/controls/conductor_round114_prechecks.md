# Conductor Round-114 bounded controls

Campaign: `m9-m2-balanced-literal-energy-connector-fork`
Evidence level: `diagnostic_only` for the finite count; the proof must be
algebraic.  No computation certifies an asymptotic statement.

## Exact-rational identity check

Command:

```text
python -c "from fractions import Fraction as F; tests=[(5,7,2,3),(11,13,-2,4),(17,19,5,-3)]; print([(h,k,p,q,(F(1)+F(p,2*h)+F(q,2*k))**2-(F(h+p,h)*F(k+q,k))==F((h*q-k*p)**2,4*h*h*k*k)) for h,k,p,q in tests])"
```

Output:

```text
[(5, 7, 2, 3, True), (11, 13, -2, 4, True), (17, 19, 5, -3, True)]
```

Pass rule: the rational precursor

\[
P^2-Q=(hq-kp)^2/(4h^2k^2)
\]

must hold exactly on every test, including signed increments that keep the
second point positive.  Outcome: pass.  Limitation: finite tests do not
replace the displayed algebraic expansion.

## Determinant-narrow count diagnostic

For the square boxes `L<=h,k,h',k'<2L`, count ordered pairs satisfying
`|hk'-h'k|<=L`.

Command:

```text
python -c "import math; \
for L in (8,12,16,24,32): \
 pts=[(h,k) for h in range(L,2*L) for k in range(L,2*L)]; \
 c=sum(1 for h,k in pts for hp,kp in pts if abs(h*kp-hp*k)<=L); \
 print(L,c,round(c/L**3,3),round(c/(L**3*math.log(L)),3))"
```

Output:

```text
8 492 0.961 0.462
12 1644 0.951 0.383
16 3812 0.931 0.336
24 12776 0.924 0.291
32 29992 0.915 0.264
```

Pass rule: no growth visibly contradicting the proposed
`O(L^3 log L)` upper bound.  Outcome: pass, with observed count close to a
constant times `L^3` on these small boxes.  Limitation: this is only a
falsification check; the proof must use the exact lattice-line count and
must cover fixed rectangular comparability `K/L in [1,16]`.
