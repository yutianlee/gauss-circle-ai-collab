# Round 177 statement-only packet

Let \(J=\sqrt X\), \(1\ll L\ll H\le J^{1/2}\),
\(R_0=\lceil L\rceil\), and

\[
 R_{\log}=\min\{R_0-1,\lfloor(\log X)^{100}\rfloor\}.
\]

For squarefree \(N=dm\asymp L^2\), with \(d\) odd, write

\[
 u_L(d,m)=\chi_4(d)\lambda_N(d)e(J\sqrt N),
\]

where \(|\lambda_N(d)|\ll1\) and \(\lambda_N(d)\) retains the normalized
half-open shell, squarefree row, a row-dependent neither/both or no-pair
selector, two parity branches, smooth profiles, hard point values,
endpoints, and full-line zero extension. No regularity of the selector may
be assumed.

In one opposing orientation, use odd \(\kappa,u\), \((u,v)=1\), and

\[
 d=\kappa u,\quad d'=\kappa u+2s_t,\quad
 m'=\kappa v,\quad m=\kappa v+2w_t,\quad
 r=2\kappa n,
\]

\[
 s_t=[\bar v n]_u+ut,\qquad
 w_t=\frac{[\bar v n]_uv-n}{u}+vt.
\]

The other orientation uses
\(s_t=[-\bar v n]_u+ut\),
\(w_t=(n+[-\bar v n]_uv)/u+vt\).
These parametrizations are disjoint and multiplicity one. On nonzero
squarefree atoms,

\[
 (d,d')=(u,n),\qquad
 \chi_4(d')\chi_4(d)=E_u(\pm\bar v n)(-1)^t,\qquad
 E_u(a)=(-1)^{[a]_u}.
\]

The common product step is \(2\kappa uv\). Literal support has
\(u,v\asymp L/\kappa\), \(n\ll L/\kappa\), and \(O(1+\kappa)\) fibre sites.
The complete fixed-proportion sector \(\kappa\ge\delta L\) is already
target-safe for every fixed \(0<\delta<1/2\). The frozen target is the
complete complement \(\kappa<\delta L\) at \(L^2X^\varepsilon\), retaining
both orientations, the Fejer factor, non-polylogarithmic determinant range,
original-gcd cutoff, square-root phase, literal coefficient, displacement
inequalities, endpoints, and zero extension.

For odd \(u\),

\[
 E_u(a)=\sum_{k\bmod u}c_u(k)e(ka/u),\qquad
 c_u(k)=\frac{2}{u(1+e(-k/u))},
\]

with \(\|c_u\|_1\ll\log(2u)\), \(\|c_u\|_2=1\), and a constant-size
near-half alias. After this exact expansion, the fixed-\((\kappa,u,k)\)
hybrid block is the complete signed sum over \(v,n,t\), with reciprocal
phase \(\pm k\bar v n/u\) and fibre half-frequency \(t/2\). Its raw capacity
is \(L^2/\kappa\). A uniform \(O(LX^\varepsilon)\) bound for the complete
block, or the analogous \(c_u\)-weighted bound before the alias modulus,
is sufficient after summing \((\kappa,u)\). A fixed-\(v\) bound
\(O(\kappa X^\varepsilon)\) is not assumed.

Starting only from this packet:

1. independently verify the exact summation ledger and derive the weakest
   useful local or dyadic hybrid theorem that implies the target;
2. attempt a reciprocal large-sieve, reciprocity, \(TT^*\), or signed-energy
   proof without separating \(v,n,t,k\), selector cases, or orientations
   before the saving;
3. identify every diagonal, off-diagonal, reduced-conductor, incomplete
   interval, and stationary-alias cost; and
4. prove the theorem, an owner-complete strict sector, or the first exact
   obstruction.

Required controls include \(k=0\), the near-half alias,
\((k,u)>1\), \((u,n)>1\), primitive modulus
\(u/(u,n)\), incomplete \(v\)-intervals, small-\(\kappa\) fibres, selected
and no-pair rows, squarefree progressions, both parity branches, dechirped
and selector-erased false arrays, both orientations, the outer real part,
endpoints, and zero extension. A false array can invalidate a proof
mechanism but is not a lower bound for the literal aggregate.

Do not use the proof graph, any strategy file, earlier campaign report,
kernel, source card, sibling Round-177 report, conductor analysis, or
proposed state effect. Return only a seven-section report with exact
statement, derivation, first unproved step, controls, dependencies, and a
recommended scoped state effect.
