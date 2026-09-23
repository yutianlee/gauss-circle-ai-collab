ClearAll["Global`*"];

$MaxExtraPrecision = 1000;
failures = {};
checkedRows = 0;
checkedCovectors = 0;
checkedFibres = 0;
checkedCoverageRows = 0;
checkedUnionBounds = 0;
checkedPigeonholeRows = 0;

signedLeastInverse[modulus_Integer, residue_Integer] := Module[{r},
  r = PowerMod[residue, -1, modulus];
  If[2 r > modulus, r - modulus, r]
];

fareyFamily[cap_Integer] :=
  Flatten[
    Table[
      Select[Table[{c, d}, {d, 0, c}], CoprimeQ @@ # &],
      {c, 1, cap}
    ],
    1
  ];

Do[
  units = Select[Range[1, modulus - 1], CoprimeQ[#, modulus] &];
  cap = Min[modulus - 1, 12];
  family = fareyFamily[cap];
  rowData = Table[
    rho = signedLeastInverse[modulus, v0];
    beta = Quotient[rho v0 - 1, modulus];
    checkedRows++;
    If[rho v0 - beta modulus =!= 1,
      AppendTo[failures, {"bezout", modulus, v0, rho, beta}]
    ];
    If[Abs[rho] > Floor[(modulus - 1)/2],
      AppendTo[failures, {"least_inverse_range", modulus, v0, rho}]
    ];
    If[rho beta < 0 || Abs[beta] > Abs[rho] ||
       GCD[Abs[rho], Abs[beta]] =!= 1,
      AppendTo[failures, {"primitive_sign_size", modulus, v0, rho, beta}]
    ];
    {v0, rho, beta},
    {v0, units}
  ];

  Do[
    {v0, rho, beta} = row;
    minimumCovector = Min[
      Abs[#[[1]] beta - #[[2]] rho] & /@ family
    ];
    checkedPigeonholeRows++;
    If[minimumCovector > Floor[Abs[rho]/(cap + 1)],
      AppendTo[failures,
        {"circular_pigeonhole", modulus, cap, v0, rho, beta,
         minimumCovector, Floor[Abs[rho]/(cap + 1)]}]
    ];
  , {row, rowData}];

  Do[
    {c, d} = covector;
    fibreAssociation = GroupBy[
      rowData,
      Function[row, c row[[3]] - d row[[2]]]
    ];
    KeyValueMap[
      Function[{ell, rows},
        n = c + modulus ell;
        checkedFibres++;
        If[n == 0,
          AppendTo[failures, {"zero_factor", modulus, c, d, ell}]
        ];
        If[Length[rows] > 2 DivisorSigma[0, Abs[n]],
          AppendTo[failures,
            {"divisor_multiplicity", modulus, c, d, ell,
             Length[rows], 2 DivisorSigma[0, Abs[n]]}]
        ];
      ],
      fibreAssociation
    ];
    Do[
      {v0, rho, beta} = row;
      ell = c beta - d rho;
      checkedCovectors++;
      If[rho (c v0 - d modulus) =!= c + modulus ell,
        AppendTo[failures,
          {"factorization", modulus, v0, rho, beta, c, d, ell}]
      ];
      If[c + modulus ell == 0,
        AppendTo[failures,
          {"nonzero_rhs", modulus, v0, rho, beta, c, d, ell}]
      ];
    , {row, rowData}];
  , {covector, family}];

  Do[
    sectorRows = Select[
      rowData,
      Function[row,
        Abs[row[[2]]] > threshold &&
        Min[Abs[(#[[1]] row[[3]] - #[[2]] row[[2]])] & /@ family]
          <= threshold
      ]
    ];
    unionMultiplicity = Total[
      Function[cv,
        Count[
          rowData,
          row_ /; Abs[row[[2]]] > threshold &&
            Abs[cv[[1]] row[[3]] - cv[[2]] row[[2]]] <= threshold
        ]
      ] /@ family
    ];
    checkedUnionBounds++;
    If[Length[sectorRows] > unionMultiplicity,
      AppendTo[failures,
        {"union_bound", modulus, threshold,
         Length[sectorRows], unionMultiplicity}]
    ];

    If[threshold >= 1 && modulus <= 2 cap,
      Do[
        {v0, rho, beta} = row;
        If[Abs[rho] > threshold,
          checkedCoverageRows++;
          primitiveCovector = {Abs[rho], Abs[beta]};
          If[!MemberQ[family, primitiveCovector] ||
             primitiveCovector[[1]] beta -
               primitiveCovector[[2]] rho =!= 0,
            AppendTo[failures,
              {"small_modulus_coverage", modulus, threshold,
               v0, rho, beta, primitiveCovector}]
          ];
        ];
      , {row, rowData}]
    ];
  , {threshold, 1, Min[5, Floor[(modulus - 1)/2]]}];

  zeroThresholdSector = {};
  If[zeroThresholdSector =!= {},
    AppendTo[failures, {"T_zero_not_empty", modulus}]
  ];
,
  {modulus, 3, 160}
];

Print["Round 192 Farey-covector finite diagnostic"];
Print["moduli_checked=158"];
Print["rows_checked=", checkedRows];
Print["covector_row_identities_checked=", checkedCovectors];
Print["fixed_covector_fibres_checked=", checkedFibres];
Print["small_modulus_coverage_rows_checked=", checkedCoverageRows];
Print["circular_pigeonhole_rows_checked=", checkedPigeonholeRows];
Print["union_bounds_checked=", checkedUnionBounds];
Print["T_zero_definition_checked=158"];
Print["failure_count=", Length[failures]];
If[Length[failures] > 0,
  Print["first_failures=", Take[failures, UpTo[20]]];
  Exit[1]
];
Print["status=PASS_DIAGNOSTIC_ONLY"];
Exit[0];
