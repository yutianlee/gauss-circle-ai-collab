Clear[ch,HH,DD,qq,dd,aa,gg]; ch[n_Integer]:=Switch[Mod[n,4],0,0,1,1,2,0,3,-1]; HH=3; DD=19;
pp=Flatten[Table[Table[{nn/dd,-I HH ch[dd]/(2 dd)},{nn,Ceiling[dd/HH],Floor[2 dd/HH]}],{dd,1,DD}],1];
tt=Flatten[Table[Table[If[OddQ[kk],{kk/(4 dd),-HH ch[kk]/(4 dd)},Nothing],{kk,Ceiling[4 dd/HH],Floor[8 dd/HH]}],{dd,1,DD}],1];
direct=Select[GroupBy[Join[pp,tt],First->Last,Total],#!=0&];
grouped=Flatten[Table[Table[If[CoprimeQ[aa,qq],{aa/qq,Which[OddQ[qq],-I HH ch[qq]/(2 qq) Sum[ch[gg]/gg,{gg,1,Floor[DD/qq]}],Mod[qq,4]==0,-HH ch[aa]/qq Sum[ch[gg]/gg,{gg,1,Floor[4 DD/qq]}],True,0]},Nothing],{aa,Ceiling[qq/HH],Floor[2 qq/HH]}],{qq,1,4 DD}],1];
expected=Select[GroupBy[grouped,First->Last,Total],#!=0&];
{Sort[Normal[direct]]===Sort[Normal[expected]],Length[direct],Select[Keys[direct],Mod[Denominator[#],4]==2&]}
