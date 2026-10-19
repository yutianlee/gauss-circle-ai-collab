ClearAll[pp, z, m, j, coeff, newton, expected, der, checks, xx];
der[n_Integer] := n! Sum[(-1)^k/k!, {k, 0, n}];
newton[0] = 1;
newton[n_Integer?Positive] := newton[n] = Expand[Sum[(-1)^(j-1) (n-1)!/(n-j)! pp[j] newton[n-j], {j,1,n}]];
coeff[n_Integer] := CoefficientRules[Expand[pp[1]^n-newton[n]], Table[pp[j],{j,1,n}]];
checks = Table[
 Module[{rules=coeff[m], absByDegree, target, lead, total},
 absByDegree=Expand[Total[(Abs[Last[#]] z^(First[#][[1]]))& /@ rules]];
 target=Sum[Binomial[m,j] der[j] z^(m-j),{j,2,m}];
 lead=Coefficient[pp[1]^m-newton[m], pp[1], m-2];
 total=absByDegree/.z->1;
 <|"order"->m, "monomials"->Length[rules], "derangementCoefficientCheck"->TrueQ[Expand[absByDegree-target]===0], "totalCoefficientCheck"->TrueQ[total===m!-1], "onePairCoefficient"->lead|>
 ], {m,2,16,2}];
xx={-3,-1,0,2,5};
finiteChecks=Table[
 TrueQ[Expand[(newton[m]/.pp[j_Integer]:>Total[xx^j])-m! Coefficient[Times@@(1+# z& /@ xx),z,m]]===0],
 {m,2,16,2}];
<|"partitionChecks"->checks,"finiteSignedChecks"->finiteChecks,
"negativeIntegralControlOrder6"->(6! Coefficient[(1+z)^3(1-z)^3,z,6]),
"growingCutoffP12HeadExponent"->Together[1+(12-136/13)/(4*12)],
"sharpPointwiseExponent"->Together[(1/2+m/4+b/2)/(m+1)]|>
