(* Round 193 finite diagnostic only.  It proves no asymptotic theorem. *)

ClearAll[chi4, residualMask, selectedBits, failures, checked, closeChecked];

chi4[n_Integer] := Which[Mod[n, 4] == 1, 1, Mod[n, 4] == 3, -1, True, 0];
residualMask[{x_, y_}] := If[x == y, 1, 0];

failures = {};
checked = 0;
closeChecked = 0;
L0 = 2000;
D0 = Ceiling[Sqrt[L0]];

Do[
  h = S v - U w;
  If[h <= 0, Continue[]];
  If[!CoprimeQ[g U, v] || !CoprimeQ[U, h], Continue[]];
  If[!CoprimeQ[g, U] || !CoprimeQ[kappa, g U], Continue[]];

  d = kappa g U;
  dp = g (kappa U + 2 S);
  mp = kappa v;
  mm = kappa v + 2 w;
  r = dp mp - d mm;
  If[r != 2 kappa g h || r <= 0 || OddQ[r], Continue[]];
  If[!SquareFreeQ[d mm] || !SquareFreeQ[dp mp], Continue[]];
  If[!CoprimeQ[d, mm] || !CoprimeQ[dp, mp], Continue[]];
  If[GCD[mm, mp] != 1 || Mod[r, 4] != 2, Continue[]];

  checked++;
  tau = {g mm, d/g, g mp, dp/g};
  {dt, mt, dpt, mpt} = tau;
  gt = GCD[dt, dpt];
  kt = GCD[mt, mpt];
  tau2 = {gt mt, dt/gt, gt mpt, dpt/gt};

  tests = {
    gt == g,
    kt == 1,
    tau2 == {d, mm, dp, mp},
    dt mt == d mm,
    dpt mpt == dp mp,
    dpt < dt && mpt > mt,
    OddQ[dt] && OddQ[dpt] && OddQ[mt] && OddQ[mpt],
    chi4[dp] chi4[d] == -chi4[dpt] chi4[dt],
    dt == kappa g v + 2 g w,
    dpt == kappa g v,
    mt == kappa U,
    mpt == kappa U + 2 S,
    v S - U w == h,
    CoprimeQ[g v, U] && CoprimeQ[v, h]
  };
  If[!And @@ tests,
    AppendTo[failures, <|"tuple" -> {kappa, g, U, v, S, w},
      "tests" -> tests, "values" -> {d, mm, dp, mp, r, h, tau}|>]
  ];

  closeQ = Abs[d - g mm] <= D0 && Abs[dp - g mp] <= D0;
  If[closeQ,
    closeChecked++;
    closeTests = {
      S + w <= D0/g,
      Abs[kappa (v - U)] <= 3 D0/g,
      Abs[dt - g mt] <= D0,
      Abs[dpt - g mpt] <= D0
    };
    If[!And @@ closeTests,
      AppendTo[failures, <|"closeTuple" -> {kappa, g, U, v, S, w},
        "closeTests" -> closeTests|>]
    ];
  ];
,
  {kappa, 1, 9, 2}, {g, 1, 15, 2}, {U, 1, 25, 2},
  {v, 1, 25, 2}, {S, 1, 12}, {w, 1, 12}
];

maskFailures = {};
Do[
  original = residualMask[{bp, bq}];
  transformed = residualMask[{If[gp, bp, 1 - bp], If[gq, bq, 1 - bq]}];
  If[(gp == gq && original != transformed) ||
     (gp != gq && original == transformed),
    AppendTo[maskFailures, {bp, bq, gp, gq, original, transformed}]
  ];
,
  {bp, 0, 1}, {bq, 0, 1}, {gp, {False, True}}, {gq, {False, True}}
];

Print["round=193"];
Print["status=diagnostic_only"];
Print["enumerated_valid_tuples=", checked];
Print["enumerated_close_tuples=", closeChecked];
Print["identity_failures=", Length[failures]];
Print["mask_truth_table_failures=", Length[maskFailures]];
If[Length[failures] > 0, Print[Take[failures, UpTo[3]]]];
If[Length[maskFailures] > 0, Print[maskFailures]];
Print["limitations=no_asymptotic_count_no_literal_profile_no_BV_or_collar_proof_no_core_projection_no_density"];
