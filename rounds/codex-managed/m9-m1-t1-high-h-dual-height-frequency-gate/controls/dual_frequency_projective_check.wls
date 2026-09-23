$MaxExtraPrecision = 2000;
ClearAll[e, cq, kq, kDiv, slowCount];

e[d_Integer, b_Integer] := (-1)^Mod[b, d];
cq[q_Integer, a_Integer] :=
  N[2/(q (1 + Exp[-2 Pi I a/q])), 100];
kq[q_Integer, b_Integer] :=
  Sum[If[CoprimeQ[a, q], cq[q, a] Exp[2 Pi I a b/q], 0],
      {a, 1, q - 1}];
kDiv[q_Integer, b_Integer] :=
  Sum[MoebiusMu[q/d] d e[d, b], {d, Divisors[q]}]/q;

slowCount[q_Integer, m_Integer, u_Integer, y_Integer, a_Integer] :=
  Count[Range[u + 1, 2 u],
    v_ /; CoprimeQ[v, u] &&
      Min[Mod[a PowerMod[v, -1, q], q],
          q - Mod[a PowerMod[v, -1, q], q]] <= Floor[m q/y]];

projectiveCases = Flatten[
  Table[
    If[CoprimeQ[a, q],
      {q, m, u, y, a, slowCount[q, m, u, y, a], 2 u m/y},
      Nothing],
    {q, Range[3, 19, 2]}, {m, {1, 3, 5}}, {mult, 1, 3},
    {u, {mult m q}},
    {y, DeleteDuplicates@Select[{m + 1, 2 m, Floor[m q/2], m q, 2 m q}, # > m &]},
    {a, 1, q - 1}], 5];
projectiveFailures =
  Select[projectiveCases, #[[6]] > Ceiling[#[[7]]] &];

kernelError = Max@Flatten@Table[
  If[CoprimeQ[b, q], Abs[kq[q, b] - N[kDiv[q, b], 100]], Nothing],
  {q, Range[3, 31, 2]}, {b, 1, q - 1}];

badSlope = Table[
  {p, Sum[e[p, -2 h], {h, 1, (p - 1)/2}], -(p - 1)/2},
  {p, {5, 7, 11, 13, 17, 19, 23, 29, 31}}];

Print["projective_case_count=", Length[projectiveCases]];
Print["projective_failures=", projectiveFailures];
Print["max_kernel_error=", kernelError];
Print["bad_slope_table=", badSlope];

If[projectiveFailures === {} && kernelError < 10^-40 &&
   And @@ (#[[2]] == #[[3]] & /@ badSlope), Exit[0], Exit[1]];
