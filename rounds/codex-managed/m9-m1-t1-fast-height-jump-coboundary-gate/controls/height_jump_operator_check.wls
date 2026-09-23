(* Round 191 diagnostic only: exact anchor transport, Abel sign,
   and bounded-array operator capacity. *)

failures = {};
checks = 0;

record[name_, condition_, data_] := Module[{},
  checks++;
  If[! TrueQ[condition], AppendTo[failures, {name, data}]]
];

Do[
  If[CoprimeQ[v, U],
    inv = PowerMod[v, -1, U];
    bez = (inv v - 1)/U;
    Do[
      sp = Mod[inv h, U];
      wp = (sp v - h)/U;
      sp0 = Mod[inv (h - 1), U];
      wp0 = (sp0 v - (h - 1))/U;
      dp = Boole[sp < inv];
      record["plus_anchor_S", sp0 == sp - inv + dp U,
        {U, v, h, inv, sp, sp0, dp}];
      record["plus_anchor_w", wp0 == wp - bez + dp v,
        {U, v, h, inv, wp, wp0, dp}];
      Do[
        record["plus_transport_S",
          sp0 + U t == sp + U (t + dp) - inv,
          {U, v, h, t, dp}];
        record["plus_transport_w",
          wp0 + v t == wp + v (t + dp) - bez,
          {U, v, h, t, dp}];
        record["plus_determinant",
          (sp + U t) v - (wp + v t) U == h,
          {U, v, h, t}],
        {t, -2, 2}
      ];

      sm = Mod[-inv h, U];
      wm = (h + v sm)/U;
      sm0 = Mod[-inv (h - 1), U];
      wm0 = ((h - 1) + v sm0)/U;
      dm = Boole[sm + inv >= U];
      record["minus_anchor_S", sm0 == sm + inv - dm U,
        {U, v, h, inv, sm, sm0, dm}];
      record["minus_anchor_w", wm0 == wm + bez - dm v,
        {U, v, h, inv, wm, wm0, dm}];
      Do[
        record["minus_transport_S",
          sm0 + U t == sm + U (t - dm) + inv,
          {U, v, h, t, dm}];
        record["minus_transport_w",
          wm0 + v t == wm + v (t - dm) + bez,
          {U, v, h, t, dm}];
        record["minus_determinant",
          (wm + v t) U - (sm + U t) v == h,
          {U, v, h, t}],
        {t, -2, 2}
      ],
      {h, 1, 3 U}
    ]
  ],
  {U, 3, 31, 2}, {v, 1, U - 1}
];

zz = Unique["z"];
Do[
  vals = Table[(-1)^(h + n) (3 h + 2 n + 1), {h, 0, n}];
  wf[h_] := If[0 <= h <= n, vals[[h + 1]], 0];
  lhs = Sum[wf[h] zz^h, {h, 0, n}];
  rhs = Sum[(wf[h] - wf[h - 1]) zz^h, {h, 0, n + 1}];
  record["abel_backward_sign", Expand[(1 - zz) lhs - rhs] === 0,
    {n, vals}],
  {n, 0, 12}
];

maxCapacityError = 0.;
capacityCases = 0;
Do[
  If[CoprimeQ[a, q] && CoprimeQ[v, q],
    invq = PowerMod[v, -1, q];
    Do[
      znum = Exp[2. Pi I eps a invq/q];
      nlen = 17;
      warr[h_] := If[0 <= h < nlen, Conjugate[znum]^h, 0];
      original = Sum[warr[h] znum^h, {h, 0, nlen - 1}];
      jump = Sum[(warr[h] - warr[h - 1]) znum^h,
        {h, 0, nlen}]/(1 - znum);
      err = Max[Abs[original - nlen], Abs[jump - nlen],
        Abs[original - jump]];
      maxCapacityError = Max[maxCapacityError, err];
      capacityCases++,
      {eps, {-1, 1}}
    ]
  ],
  {q, {5, 7, 11, 13, 17, 19, 23}},
  {a, 1, q - 1}, {v, 1, q - 1}
];
record["dephased_capacity_numeric", maxCapacityError < 10^-10,
  {maxCapacityError, capacityCases}];

Print["ROUND191_HEIGHT_JUMP_DIAGNOSTIC"];
Print["anchor_and_abel_checks=", checks - 1];
Print["capacity_cases=", capacityCases];
Print["max_capacity_error=", ScientificForm[maxCapacityError, 6]];
Print["failures=", Length[failures]];
If[Length[failures] > 0, Print[Take[failures, UpTo[10]]]];
Print["interpretation=diagnostic_only"];

If[Length[failures] == 0, Exit[0], Exit[1]];
