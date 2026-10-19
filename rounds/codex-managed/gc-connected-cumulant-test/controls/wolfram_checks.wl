Clear[m];
parts[n_] := IntegerPartitions[n];
mult[v_] := Factorial[Total[v]]/(Times@@(Factorial /@ v) Times@@(Factorial /@ Last /@ Tally[v]));
cp[n_] := Total[Table[(-1)^(Length[v]-1) Factorial[Length[v]-1] mult[v] Times@@(m /@ v),{v,parts[n]}]];
checked=Table[{n,Expand[cp[n]-(MomentConvert[Cumulant[n],Moment]/.Moment[j_Integer]:>m[j])]===0},{n,2,12}];
proper=Select[parts[12],Length[#]>=2&&Min[#]>=3&];
costs=Table[{v,1+Total[Max[#/4-1,0]& /@ v],(-1)^(Length[v]-1)Factorial[Length[v]-1]mult[v]},{v,proper}];
finite=Table[{n,Factorial[12] Binomial[n/2,6]/n^6,Factorial[n]/Factorial[n-12]/n^6},{n,{12,24,48}}];
constantChecks=Table[{n,Expand[cp[n]/.m[j_Integer]:>z^j]===0},{n,2,12}];
<|"coefficientChecks"->checked,"properPartitions"->costs,"maximumOuterExponent"->Max[costs[[All,2]]],"balancedConstantFamilies"->finite,"constantCumulantsVanish"->constantChecks,"diagnosticOnly"->True|>
