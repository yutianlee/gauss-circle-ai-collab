ClearAll["Global`*"];

failures = {};
transportChecks = 0;
countChecks = 0;

Do[
  inv = PowerMod[v, -1, U];
  rho = If[inv <= (U - 1)/2, inv, inv - U];
  gamma = Quotient[rho v - 1, U];

  Do[
    Do[
      eps = If[omega == 1, 1, -1];
      s0[h_] := Mod[eps inv h, U];
      w0[h_] := If[omega == 1,
        Quotient[v s0[h] - h, U],
        Quotient[h + v s0[h], U]
      ];
      nu = Quotient[s0[h] - eps rho - s0[h - 1], U];

      If[! MemberQ[{-1, 0, 1}, nu],
        AppendTo[failures, {"carry", U, v, h, omega, rho, nu}]
      ];

      Do[
        sNow = s0[h] + U t;
        wNow = w0[h] + v t;
        sOld = s0[h - 1] + U (t + nu);
        wOld = w0[h - 1] + v (t + nu);

        If[sNow - eps rho =!= sOld || wNow - eps gamma =!= wOld,
          AppendTo[failures,
            {"transport", U, v, h, omega, t, rho, gamma, nu}]
        ];

        If[Mod[(s0[h] + t) - (s0[h - 1] + t + nu) - rho, 2] =!= 0,
          AppendTo[failures,
            {"parity", U, v, h, omega, t, rho, nu}]
        ];
        transportChecks++,
        {t, -3, 3}
      ],
      {omega, {1, -1}}
    ],
    {h, 1, 3 U}
  ],
  {U, 3, 41, 2}, {v, Select[Range[1, U - 1], CoprimeQ[#, U] &]}
];

Do[
  invs = Table[
    inv = PowerMod[v, -1, U];
    If[inv <= (U - 1)/2, inv, inv - U],
    {v, Select[Range[1, U - 1], CoprimeQ[#, U] &]}
  ];
  Do[
    actual = Count[invs, x_ /; 0 < Abs[x] <= R];
    expected = 2 Count[Range[1, R], x_ /; CoprimeQ[x, U]];
    If[actual =!= expected,
      AppendTo[failures, {"inverse-count", U, R, actual, expected}]
    ];
    countChecks++,
    {R, 0, (U - 1)/2}
  ],
  {U, 3, 101, 2}
];

Print["ROUND191_SIGNED_INVERSE_TRANSPORT_DIAGNOSTIC"];
Print["transport_and_parity_checks=", transportChecks];
Print["inverse_class_count_checks=", countChecks];
Print["failures=", Length[failures]];
If[Length[failures] > 0, Print[Take[failures, UpTo[20]]]];
Print["interpretation=diagnostic_only"];

If[Length[failures] > 0, Exit[1], Exit[0]];
