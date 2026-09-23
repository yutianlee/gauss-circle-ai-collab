ClearAll[e, anchor, coeff, hat, checks];
$MaxExtraPrecision = 2000;
e[x_] := Exp[2 Pi I N[x, 100]];
anchor[u_, a_] := (-1)^Mod[a, u];
hat[u_, k_] := Sum[anchor[u, a] e[-k a/u], {a, 0, u - 1}];
coeff[u_, k_] := 2/(u (1 + e[-k/u]));

checks = Table[
  Module[{fourier, formula, inversion, mean, orientation, folds},
    fourier = Max[Abs[N[Table[hat[u, k] - 2/(1 + e[-k/u]),
       {k, 0, u - 1}], 80]]];
    formula = Max[Abs[N[Table[coeff[u, k] - hat[u, k]/u,
       {k, 0, u - 1}], 80]]];
    inversion = Max[Abs[N[Table[
       anchor[u, a] - Sum[hat[u, k] e[k a/u]/u, {k, 0, u - 1}],
       {a, 0, u - 1}], 80]]];
    mean = Sum[anchor[u, a], {a, 0, u - 1}];
    orientation = Max[Abs[Table[
       anchor[u, a] + anchor[u, -a],
       {a, Select[Range[u - 1], CoprimeQ[#, u] &]}]]];
    folds = Max[Flatten[Table[
       If[Divisible[u, u0],
         Table[Abs[N[Sum[coeff[u, ell + j u0], {j, 0, u/u0 - 1}]
           - coeff[u0, ell], 80]], {ell, 0, u0 - 1}],
         Nothing],
       {u0, Select[Range[1, u], OddQ]}]]];
    {u, fourier, formula, inversion, mean, orientation, folds}
  ],
  {u, Range[3, 31, 2]}];

Print["columns={u,FourierError,CoefficientError,InversionError,ResidueMean,OrientationError,AliasFoldError}"];
Scan[Print, checks];
Print["allPass=", And[
  Max[Abs[Flatten[N[checks[[All, {2, 3, 4, 6, 7}]], 80]]]] < 10^-60,
  And @@ Thread[checks[[All, 5]] == 1]]];
