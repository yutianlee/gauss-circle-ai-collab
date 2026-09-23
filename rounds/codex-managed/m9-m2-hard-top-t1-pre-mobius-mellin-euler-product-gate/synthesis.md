# Round 168 synthesis: intact Mellin--Euler reduction and strict polylogarithmic sector

Round 168 closes under
**`strict_t1_mellin_euler_sector`**.  The complete polynomial-range
\(t=1\) target is not proved.  The validated State Patch creates one
homogeneous internal reduction node and changes no open parent, bridge, or
exponent status.

## Exact progress

The complete literal selector-free arithmetic family has the exact Euler
factorization

\[
 D(s_1,s_2)=L(s_1,\chi_4)\zeta(s_2)G(s_1,s_2),
\]

where

\[
 G_2=1-2^{-2s_2},\qquad
 G_p=(1+x_p+y_p)(1-x_p)(1-y_p)
\]

for odd primes, and \(G\) is holomorphic by absolute local-uniform
convergence for \(\Re s_1,\Re s_2>1/2\).

A disjoint-cardinal interpolation reproduces every literal integer value,
including hard endpoints, floors, stars, and zero values.  Moving the
\(s_2\)-contour first crosses only its zeta pole, and the exact residue
coefficient series is

\[
 L(s,\chi_4)G(s,1)
 =\frac1{\zeta(2)}
 \sum_{\substack{n\ge1\\n\ {\rm odd,\ squarefree}}}
 \frac{\chi_4(n)}{n^s}
 \prod_{p\mid n}(1+p^{-1})^{-1}.
\]

One nonstationary integration by parts on each of \(O(L^2)\) cardinal
cells gives

\[
 \mathcal S_{L,1}=R_\zeta+\mathcal I_\eta,
 \qquad R_\zeta\ll_\varepsilon L^2J^{-1}X^\varepsilon.
\]

Thus the exact remaining theorem is the signed two-height bound

\[
 \mathcal I_\eta\ll_\varepsilon L^{3/2}X^\varepsilon.
\]

The genuine strict result is: for every fixed \(B>0\),

\[
 L\le(\log X)^B
 \quad\Longrightarrow\quad
 \mathcal S_{L,1}\ll_{\varepsilon,B}L^{3/2}X^\varepsilon.
\]

For each fixed \(\kappa>0\), exact subtraction of the accepted canonical
close-opposite-prime XOR sector gives the same bound, with
\(\kappa\)-dependent constant, for its residual complement.  This strict
sector is complete in \(L\) but does not include any polynomial range.

## First open interface and scoped no-go

On a favorable recombined smooth/BV control, radial Mellin stationarity
occupies a band of length \(JL\), with pointwise transform scale
\(L^{2\eta}\sqrt{L/J}\).  Unweighted pointwise control followed by
triangle inequality, and the stated fixed-angular mean square followed by
Cauchy, each have raw capacity

\[
 L^{2\eta}\sqrt J\,L^{3/2}X^\delta.
\]

After choosing \(\eta\) and \(\delta\) in the correct epsilon order, the
structural deficit remains \(\sqrt J\).  This is not an estimate or lower
bound for the exact cardinal integral, and it does not rule out a bespoke
signed weighted hybrid theorem.

The dated source audit found no inspected theorem that supplies the
independent-height signed nonlinear estimate.  No exact coefficient bridge
from factorwise functional equations or approximate functional equations
to the Round-162 product collar was proved.  Deliberately reopening the
accepted projector merely restores the known positive capacity
\(\sqrt{JL}\), whose ratio to target is \(H/L+O(L^{-1})\).

## Proof status after Round 168

The new node is a strict reduction below the open hard-TOP owner.  The
polynomial \(t=1\) scalar and residual, K17a, K26, all other few-point
channels and collars, hard TOP, BAL, UNBAL, M9--M2, both direct M1
parents, GAR, endpoint uniformity, M9, both bridges, and the quarter
theorem remain open.  The internally proved global exponent remains
\(1/3\); the audited external Li--Yang benchmark remains
\(0.3144831759740614\ldots\).  There is no global exponent improvement.

The next analytic decision is whether to attack the exact signed
two-height integral with a genuinely weighted spectral/reciprocity
mechanism or rotate to the still-open maximal-scale K26 aggregate.  The
mandatory full-proof strategy and current-literature review remains due
after Round 169 closes.

## State effect

The applied State Patch creates
`M9-M2-hard-top-t1-mellin-euler-polylog-and-signed-moment-reduction`, adds
it only as an inconclusive dependency of the open signed-cone owner,
records seven scoped rejected implications, and explicitly leaves every
parent, bridge, theorem, and exponent unchanged.  The resulting graph
hash is
`a360b2913563c9c288438751729c5033acd2e91ee613e44f171e1d31bc7441be`.
