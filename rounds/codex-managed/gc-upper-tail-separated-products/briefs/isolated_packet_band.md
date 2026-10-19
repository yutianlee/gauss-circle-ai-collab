# Isolated statement: integer-center packets on an arbitrary set

Only this file, protocol.md and your own brief are authorized initially. No graph, actual interface, sibling/history/source files. Derive without additional arithmetic assumptions.

Let (Omega,nu) be a finite measure space, x:Omega->R measurable, W>=1, A>0, k>2, and finitely many real measurable functions f_p indexed by distinct integers p. Suppose |f_p(t)|<=A(1+|x(t)-p|/W)^(-k). Let E be any measurable subset with nu(E)=m, including a set chosen by the same packet sum. For L>=0 establish a uniform bound with correct dependence on A,W,L,m for int_E sum_(|p-q|<=L)|f_p f_q| dnu. Also derive an exact-diagonal bound and the all-pair bound. Consider variants with O(J) families/unequal widths, and determine how to retain all cross terms with an explicit cost.

Does the matrix1_(|p-q|<=L) always define a positive semidefinite quadratic form? Give an exact finite control. Can small diagonal/close-band energy by itself upper-bound the complementary signed quadratic form or the full energy? Give a sharpness or countercontrol where useful, preserving any hypotheses claimed. Do not infer facts about a particular arithmetic family from arbitrary coefficient controls. Report the first additional input needed for a power gain in the complementary signed sum. Prove all analytic/combinatorial facts; bounded finite computation may diagnose only.

Output seven protocol sections to the assigned report path, record isolation and hashes, then freeze and stop. Budget around10 minutes, one report; no successor.
