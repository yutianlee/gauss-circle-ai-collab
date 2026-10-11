# Round218 isolated joint-radial statement

Role: statement-only independent derivation. Read ONLY protocol.md and
this packet. No graph, manifest, strategy, other brief/report, web source
or historical artifact. Write only the assigned report and stop.
Graph hash supplied as metadata, not a context read:
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.

For fixed integer m>=1, fixed signs sigma_j in{+1,-1}, and a complex
smooth amplitude a(y_1,...,y_m) compactly supported where each
y_j in R^2 satisfies1<|y_j|<2, define

 J(lambda,xi)=integral_(R^(2m)) a(y)
   e(lambda sum_j sigma_j |y_j| - sum_j xi_j dot y_j) dy,
 e(t)=exp(2pi i t), lambda>=2, xi_j in R^2.

The amplitude need not factor across j. Bounds should be uniform over
a bounded collection of sufficiently many smooth seminorms and over
the signs. Analyze the exact stationary sets, Hessian rank, leading
asymptotic at |xi_j|=lambda for every j, and the truth or failure of
the proposed localized estimate, when lambda/2<=|xi_j|<=2lambda:

 |J(lambda,xi)| <= C_(m,A,a) lambda^(-m/2)
                      product_j(1+||xi_j|-lambda|)^(-A).

Prove it, repair it with an explicit correct uniform estimate, or give
a counterexample. Also state a sufficient far-frequency bound, including
xi_j=0, and an unequal-parameter extension with lambda_j>=2 in place
of one lambda. Track how many amplitude seminorms are needed in principle.
Do not infer full nondegenerate 2m-dimensional stationary phase solely
from the ambient dimension. Check whether an amplitude independent of
lambda can attain order lambda^(-m/2) along a resonant sequence.

Controls: m=1, mixed signs, joint nonproduct amplitude, coincident radial
frequencies, all angular branches, radial boundary terms under the stated
compact support, uniform small and large radial mismatch, vanishing
amplitudes, and constants at fixed m versus growing m. This is an abstract
oscillatory-integral task; do not invent a discrete application or decide
a successor. Give seven numbered protocol sections with full derivation,
first gap, exact control outcomes, dependencies and recommended state effect.
