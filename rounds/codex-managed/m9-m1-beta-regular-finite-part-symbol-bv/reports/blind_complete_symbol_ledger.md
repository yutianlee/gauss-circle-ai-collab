# Round 31 blind report: complete regular-symbol ledger and first BV obstruction

Task: blind_complete_symbol_ledger  
Role: statement-only blind rederivation  
Allocation: 100% analytical/algebraic; no computation and no external theorem

## 1. Result: exact conditional ledger and a statement-level no-go

The regular finite part has an exact BV ledger, but the target norm cannot
be proved from the accepted Round-27 and Round-30 statements. The first
uncontrolled term is
\[
 {(\partial_L+\partial_\nu)H(L,L-\mu)
       -(\partial_L+\partial_\nu)H(L,L)\over\mu},               \tag{31.1}
\]
which occurs in \(\partial_L\Delta_H\). Controlling (31.1) uniformly
requires the mixed second symbol derivative
\[
 \partial_\nu(\partial_L+\partial_\nu)H.                        \tag{31.2}
\]
Round 27 gives a separated value estimate, and Round 30 explicitly leaves
the complete normalized symbol variation open. Neither supplies (31.2)
for the gamma/radial/profile/mask/floor/star product or its height tails.

This is a genuine logical obstruction rather than a technical omission:
smooth coefficients can have the accepted pointwise size and arbitrarily
large variation. An explicit phase-cancelling coefficient family below
keeps the regular finite part pointwise at the target scale while making
its BV norm larger by an arbitrary factor.

The artificial-pole cutoff is not itself the offender. If \(G=E_1+R_1\)
is differentiated with identical masks, domains, and endpoints, every
\(\omega'\) and \(\omega''\) term cancels exactly in
\[
 \omega G+(1-\omega)R_1-\omega E_1.                            \tag{31.3}
\]
What remains unproved is a uniform derivative bound for that complete
recombined object.

Thus the result is a scoped no-go: the requested \(q^{-2}\)-scale BV
estimate is not derivable from the permitted accepted statements. The
report identifies the first missing derivative, gives the exact product
and moving-endpoint ledger that would prove it, and does not assert that a
specific actual factor is large without its formula.

## 2. Exact statement and hypotheses

### 2.1 Complete regular finite-part definition

Fix one signed saddle component and all parameters other than
\[
 L=\alpha-\beta,\qquad \mu=L-\nu.
\]
The exact finite section is
\[
 A(L)=\max\{-U,L-V\},\qquad
 B(L)=\min\{U,L+V\}.                                           \tag{31.4}
\]
On each nonempty affine cell \(A(L)<B(L)\), let
\(H_\omega(L,\nu)\) denote the **complete phase-removed numerator**,
including the actual height transform, gamma and scale symbols, masks,
floors, stars, radial endpoint data, and the artificial-pole-safe radial
package (31.3). No summand of (31.3) is substituted for \(H_\omega\)
near \(\rho=0\).

Define
\[
 \Delta_\omega(L,\mu)
 ={H_\omega(L,L-\mu)-H_\omega(L,L)\over\mu},                  \tag{31.5}
\]
with its continuous divided-difference value at \(\mu=0\), and
\[
 {\cal R}_\omega(L)
 =-i\int_{A(L)}^{B(L)}\Delta_\omega(L,\mu)\,d\mu.               \tag{31.6}
\]
Equations (31.5)-(31.6) are precisely the regular part left after the
explicit Plemelj delta jump and constant-numerator face logarithms have
been removed.

Let \(\kappa_\pm\) be the exact Morse coordinate on the positive or
negative saddle component, and let \(L=L_\pm(y)\) be its inverse
parameterization. Collect every factor outside the finite-section
subtraction, including the exact Morse Jacobian and the accepted
stationary numerator, into \({\cal Q}_\pm(L)\). The complete regular
Morse amplitude is then
\[
 {\cal B}_\pm(y)
 ={\cal Q}_\pm(L_\pm(y))\,{\cal R}_\omega(L_\pm(y)).             \tag{31.7}
\]
This is the most explicit complete definition licensed by the permitted
accepted statements: those statements name all actual factor classes but
do not give their individual formulas. Replacing
\(H_\omega\) or \({\cal Q}_\pm\) by an invented product would not be an
exact reconstruction.

Write
\[
 {\cal M}_{j,h,q,x}
 =X^\varepsilon {D_j\over q\lambda}
 \{\text{the inherited }h,D_j,x\text{ monomial}\},\qquad
 \lambda={\pi q\sqrt{Xx}\over D_j}.                            \tag{31.8}
\]
The requested assertion is
\[
 \|{\cal B}_\pm\|_\infty+\operatorname {Var}_y({\cal B}_\pm)
 \ll {\cal M}_{j,h,q,x},                                      \tag{31.9}
\]
uniformly in all affine cells, seams, and finite-height limits. For an
amplitude with jumps, the second term in (31.9) must mean distributional
total variation; a classical \(L^1\) derivative alone omits the endpoint
stars and mask jumps.

### 2.2 Exact divided-difference derivative ledger

Set
\[
 {\mathsf D}=\partial_L+\partial_\nu.
\]
At fixed \(\mu\), both arguments in \(H_\omega(L,L-\mu)\) move with
\(L\). Therefore
\[
 \partial_L\Delta_\omega(L,\mu)
 ={ {\mathsf D}H_\omega(L,L-\mu)
     -{\mathsf D}H_\omega(L,L)\over\mu}.                       \tag{31.10}
\]
Equivalently,
\[
 \Delta_\omega(L,\mu)
 =-\int_0^1\partial_\nu H_\omega(L,L-t\mu)\,dt,                 \tag{31.11}
\]
\[
 \partial_L\Delta_\omega(L,\mu)
 =-\int_0^1
 \partial_\nu{\mathsf D}H_\omega(L,L-t\mu)\,dt.                \tag{31.12}
\]
These identities fix which first and second derivatives are actually
needed; bounding only \(\partial_LH_\omega\) or only
\(\partial_\nu H_\omega\) is insufficient.

On the interior of an affine cell,
\[
\begin{split}
 {\cal R}_\omega'(L)=-i\Bigg\{&
 \int_{A(L)}^{B(L)}
       \partial_L\Delta_\omega(L,\mu)\,d\mu\\
 &+B'(L)\Delta_\omega(L,B(L))
 -A'(L)\Delta_\omega(L,A(L))\Bigg\}.              \tag{31.13}
\end{split}
\]
Here \(A',B'\in\{0,1\}\) away from switching points. Formula (31.13)
is the complete moving-endpoint trace ledger.

If
\[
 H_\omega=\prod_{k=1}^{n}F_k,
\]
then
\[
 {\mathsf D}H_\omega
 =\sum_k({\mathsf D}F_k)\prod_{\ell\ne k}F_\ell,                \tag{31.14}
\]
and
\[
\begin{split}
 \partial_\nu{\mathsf D}H_\omega
 ={}&\sum_k(\partial_\nu{\mathsf D}F_k)
       \prod_{\ell\ne k}F_\ell\\
 &+\sum_{k\ne m}({\mathsf D}F_k)(\partial_\nu F_m)
       \prod_{\ell\ne k,m}F_\ell.                              \tag{31.15}
\end{split}
\]
Thus every factor needs either a second symbol estimate or a compatible
first-derivative cross estimate. There is no product-rule route from
pointwise bounds alone.

### 2.3 Separated two-denominator ledger

Away from the artificial seam, the accepted separated model may be
written more explicitly as
\[
 H(L,L-\mu)={P(L,L-\mu)\over A_0(L)+i\mu/2},\qquad
 H(L,L)={P(L,L)\over A_0(L)},                                  \tag{31.16}
\]
where in the accepted \(R_1\) normalization
\(A_0=\rho_0-i\alpha\) and \(A_0'=-i\) when the remaining parameters
are fixed. Put
\[
 P_\mu=P(L,L-\mu),\quad P_0=P(L,L),\quad
 Q={P_\mu-P_0\over\mu},\quad D_\mu=A_0+i\mu/2.
\]
Then the regular integrand has the exact decomposition
\[
 \Delta_H={Q\over D_\mu}
 -{iP_0\over2A_0D_\mu},                                      \tag{31.17}
\]
and
\[
\begin{split}
 \partial_L\Delta_H={}&
 { {\mathsf D}P_\mu-{\mathsf D}P_0\over\mu D_\mu}
 -{QA_0'\over D_\mu^2}\\
 &-{i\over2}\left\{
 { {\mathsf D}P_0\over A_0D_\mu}
 -{P_0A_0'(D_\mu+A_0)\over A_0^2D_\mu^2}
 \right\}.                                         \tag{31.18}
\end{split}
\]
The last three terms gain powers from the denominators when
\(|A_0|\asymp\lambda\). The first term in (31.18) is exactly the
uncontrolled divided difference (31.1). Formula (31.18) is not used at
\(\rho=0\), where (31.3) must be kept recombined.

### 2.4 Sufficient conditional BV statement

For later use, define on all affine cells
\[
\begin{split}
 {\mathfrak S}(H_\omega)=&
 \sup_L\int_{A(L)}^{B(L)}|\Delta_\omega(L,\mu)|\,d\mu\\
 &+\int\!\!\int_{A(L)}^{B(L)}
 |\partial_L\Delta_\omega(L,\mu)|\,d\mu\,dL\\
 &+\sum_{\gamma=A,B}\int
 |\Delta_\omega(L,\gamma(L))|\,dL\\
 &+\sum_{\xi\ {\rm cell\ face}}
 |{\cal R}_\omega(\xi+)-{\cal R}_\omega(\xi-)|.
                                                               \tag{31.19}
\end{split}
\]
Then the exact BV product rule gives
\[
\begin{split}
 \|{\cal B}_\pm\|_\infty+\operatorname {Var}{\cal B}_\pm
 \ll{}&
 \bigl(\|{\cal Q}_\pm\|_\infty+
       \operatorname {Var}{\cal Q}_\pm\bigr)\\
 &\times\bigl(\sup_L|{\cal R}_\omega(L)|
       +{\mathfrak S}(H_\omega)\bigr).             \tag{31.20}
\end{split}
\]
A monotone exact Morse reparameterization does not change total
variation:
\[
 \operatorname {Var}_y(F\circ L_\pm)
 =\operatorname {Var}_L F.                                      \tag{31.21}
\]
Only the explicitly factored Morse Jacobian in \({\cal Q}_\pm\) needs a
separate product-rule estimate. Equations (31.19)-(31.21) are a complete
conditional route to (31.9).

## 3. Proof or derivation

Equations (31.10)-(31.12) follow from the fundamental theorem of calculus
on the segment from \((L,L)\) to \((L,L-\mu)\). Leibniz differentiation
of (31.6) gives (31.13). Applying the ordinary product rule once and twice
gives (31.14)-(31.15). Subtracting the two fractions in (31.16) gives
(31.17), and differentiating it at fixed \(\mu\) gives (31.18).

At a switching point of a max/min endpoint, the two affine formulas for
\(A\) or \(B\) agree in value, so a continuous complete numerator gives no
automatic jump in (31.6). A hard mask, floor, or endpoint-star convention
can nevertheless create a trace; the final sum in (31.19) records it
exactly once. At a collapsed section \(A=B\), (31.6) is zero, again
subject to the explicitly retained endpoint convention.

For the artificial-pole package, let \(D\) be any one of the directional
derivatives required by (31.12). From \(G=E_1+R_1\),
\[
\begin{split}
 D\{\omega G+(1-\omega)R_1-\omega E_1\}
 ={}&(D\omega)(G-R_1-E_1)\\
 &+\omega(DG-DE_1)+(1-\omega)DR_1
 =DR_1.                                             \tag{31.22}
\end{split}
\]
Differentiating again gives
\[
\begin{split}
 D^2\{\omega G+(1-\omega)R_1-\omega E_1\}
 ={}&(D^2\omega)(G-R_1-E_1)\\
 &+2(D\omega)(DG-DR_1-DE_1)\\
 &+\omega(D^2G-D^2E_1)+(1-\omega)D^2R_1
 =D^2R_1.                                          \tag{31.23}
\end{split}
\]
Hence cutoff derivatives cancel to second order, provided the identity is
used with identical masks, domains, endpoints, and trace conventions.
Equations (31.22)-(31.23) prove cancellation, not boundedness of the
remaining derivative.

The fixed height profile by itself is benign at fixed \(b>0\). If
\(H(L,\nu)=f_b(\nu)\), then
\[
 \Delta_H(L,\mu)=-\int_0^1 f_b'(L-t\mu)\,dt,\qquad
 \partial_L\Delta_H(L,\mu)
 =-\int_0^1 f_b''(L-t\mu)\,dt.                    \tag{31.24}
\]
This matches the Round-30 statement that a second transform derivative
controls the regular quotient. It does not provide the dependence of the
constant on \(b\downarrow0\), nor estimates for the other product factors.

Finally, the insufficiency of pointwise information is exact. On a fixed
cell \(A=-1,B=1\), choose any target scale \(M>0\) and
\[
 H_T(L,\nu)=M e^{iTL}\nu,\qquad 0\leq L\leq1.                   \tag{31.25}
\]
Then
\[
 \Delta_{H_T}(L,\mu)=-M e^{iTL},\qquad
 {\cal R}_{H_T}(L)=2iM e^{iTL}.                                \tag{31.26}
\]
Thus
\[
 \|{\cal R}_{H_T}\|_\infty=2M,\qquad
 \operatorname {Var}_{[0,1]}{\cal R}_{H_T}=2MT.                \tag{31.27}
\]
The family is smooth and has the same pointwise scale for every \(T\),
but violates any \(O(M)\) BV assertion as \(T\to\infty\). Taking
\(M={\cal M}_{j,h,q,x}\) proves that the accepted pointwise
\(q^{-2}\) capacity cannot imply (31.9). This is an abstract
coefficient-adversary control, not a claim that an actual project factor
equals (31.25).

## 4. First doubtful or unproved step

The first unproved step is the bound for (31.1), equivalently (31.2), for
the **complete** \(H_\omega\). It occurs before height exhaustion or the
final \(q,h,D_j,x\) summation. The accepted statements do not give the
individual formulas needed to decide whether the gamma symbol, radial
symbol, a profile/floor/star factor, or a cross term in (31.15) is the
first actual contributor to exceed the target.

It would therefore be unjustified to name a particular actual factor as
large. What can be identified exactly is the first required factor in the
proof ledger: the diagonal directional derivative
\({\mathsf D}H_\omega\), measured through its \(\nu\)-divided difference.
After it, independent unresolved terms are the endpoint traces in
(31.13), the variation of \({\cal Q}_\pm\), the \(b\downarrow0\)
dependence of (31.24), and the \(U,V,S\) tails.

## 5. Control tests and outcomes

### Product-rule-and-derivative

**Fail for the target; exact ledger passes.** Equations
(31.10)-(31.18) include every chain-rule and product-rule derivative.
They expose the missing mixed derivative (31.2). The \(\omega'\) and
\(\omega''\) terms cancel by (31.22)-(31.23), but no permitted statement
bounds the remaining complete derivative at scale (31.8).

### Moving-endpoint-traces

**Ledger pass, estimate open.** Formula (31.13) has both traces with signs
\(+B'\) and \(-A'\), and (31.19) records all affine-cell jumps. The
accepted transform decay supports the fixed-profile traces at fixed
\(b\), but no complete actual-factor or height-uniform trace bound is
available.

### Pointwise-versus-BV

**Decisive fail for pointwise inference.** Equations
(31.25)-(31.27) preserve pointwise size while making variation arbitrary.
The target requires distributional BV, including hard jumps; an
\(L^1\) norm of the classical derivative alone would miss precisely the
floor, mask, and star traces.

## 6. Dependencies and exact artifacts used

Only the following permitted artifacts were read or used:

1. protocol.md;
2. state/active_campaign.yml;
3. rounds/codex-managed/m9-m1-beta-radial-pushforward-bv/synthesis.md;
4. rounds/codex-managed/m9-m1-beta-log-amplitude-two-saddle/synthesis.md.

No proof graph, proof draft, excluded conductor review, Round-31 claimant
report, computation, or web source was read or used.

## 7. Recommended state effect

- **Promote as exact analytic bookkeeping:** the complete regular-part
  definition (31.5)-(31.7), directional divided-difference identities
  (31.10)-(31.12), moving-endpoint formula (31.13), separated denominator
  ledger (31.17)-(31.18), and conditional BV criterion (31.19)-(31.21).
- **Promote as an exact seam identity:** first and second cutoff
  derivatives cancel in (31.22)-(31.23) when masks, domains, endpoints,
  and conventions are identical.
- **Reject:** deriving the complete normalized BV estimate from the
  separated pointwise \(q^{-2}\) estimate. The family (31.25) is a sharp
  logical countermodel.
- **Retain open:** the actual bound for
  \(\partial_\nu(\partial_L+\partial_\nu)H_\omega\), all actual
  product-factor and endpoint trace estimates, the \(b\downarrow0\) and
  \(U,V,S\) limits, preservation of the full \(q^{-2}\) beta gain, M9-M1,
  M9, and the final Gauss-circle target.
