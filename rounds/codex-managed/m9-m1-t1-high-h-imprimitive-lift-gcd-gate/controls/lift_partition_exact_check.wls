ClearAll[coeff, liftData, tripleDivisorCount, productTripleCount];

coeff[u_Integer, k_Integer] := 2/(u (1 + Exp[-2 Pi I k/u]));
liftData[u_Integer, k_Integer] := Module[{m, q, a},
  m = GCD[k, u];
  q = u/m;
  a = k/m;
  {m, q, a}
];

tripleDivisorCount[n_Integer] := Total[DivisorSigma[0, #] & /@ Divisors[n]];
productTripleCount[1] := 1;
productTripleCount[n_Integer /; n > 1] := Times @@ (Binomial[Last[#] + 2, 2] & /@ FactorInteger[n]);

oddModuli = Range[3, 101, 2];
liftChecks = Flatten@Table[
  Module[{m, q, a},
    {m, q, a} = liftData[u, k];
    {
      GCD[a, q] == 1,
      m q == u,
      m a == k,
      Abs[N[coeff[u, k] - coeff[q, a]/m, 80]] < 10^-60,
      Min[k, u - k] == m Min[a, q - a]
    }
  ],
  {u, oddModuli}, {k, 1, u - 1}
];

phaseChecks = Flatten@Table[
  Module[{m, q, a, inv},
    {m, q, a} = liftData[u, k];
    inv = PowerMod[v, -1, u];
    Abs[N[
      Exp[2 Pi I k inv h/u] - Exp[2 Pi I a inv h/q],
      80
    ]] < 10^-60
  ],
  {u, Range[3, 51, 2]},
  {v, Select[Range[1, u - 1], CoprimeQ[#, u] &]},
  {h, Select[Range[1, Min[17, u]], CoprimeQ[#, u] &]},
  {k, 1, u - 1}
];

partitionChecks = Flatten@Table[
  Module[{high, imprimitive, primitiveRemainder},
    high = Select[Range[1, u - 1],
      u > 4 q0 && u/GCD[#, u] > q0 && Min[#, u - #] > q0 &
    ];
    imprimitive = Select[high, q0 GCD[#, u] >= y0 &];
    primitiveRemainder = Select[high, q0 GCD[#, u] < y0 &];
    {
      Sort[Join[imprimitive, primitiveRemainder]] == Sort[high],
      Intersection[imprimitive, primitiveRemainder] == {}
    }
  ],
  {u, Range[3, 101, 2]}, {q0, {1, 2, 3, 5}}, {y0, {q0 + 1, 2 q0 + 1, 4 q0 + 1}}
];

divisorChecks = Table[
  tripleDivisorCount[n] == productTripleCount[n],
  {n, 1, 250}
];

nearHalfChecks = Table[
  Module[{k1, k2, mass},
    k1 = (u - 1)/2;
    k2 = (u + 1)/2;
    mass = Abs[coeff[u, k1]]^2 + Abs[coeff[u, k2]]^2;
    GCD[k1, u] == 1 && GCD[k2, u] == 1 && N[mass - 8/Pi^2, 50] >= -10^-40
  ],
  {u, oddModuli}
];

allChecks = Join[liftChecks, phaseChecks, partitionChecks, divisorChecks, nearHalfChecks];

Print["odd_moduli_checked=", Length[oddModuli]];
Print["lift_checks=", Length[liftChecks], "; failed=", Count[liftChecks, False]];
Print["phase_checks=", Length[phaseChecks], "; failed=", Count[phaseChecks, False]];
Print["partition_checks=", Length[partitionChecks], "; failed=", Count[partitionChecks, False]];
Print["divisor_checks=", Length[divisorChecks], "; failed=", Count[divisorChecks, False]];
Print["near_half_checks=", Length[nearHalfChecks], "; failed=", Count[nearHalfChecks, False]];
Print["overall=", If[And @@ allChecks, "PASS", "FAIL"]];

Exit[If[And @@ allChecks, 0, 1]];
