# Round 176 strategy: K17a cross-gcd alternating-fibre gate

## Frozen objective

Work on authoritative graph
`9409651dccbbd1c69547546b245ba04c21d2a280173733ae37b693f9894c8b03`.
Let

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,
\]

fix \(0<\gamma<1\), and set

\[
 R_{\log}=\min\{R_0-1,\lfloor(\log X)^{100}\rfloor\}.
\tag{176.1}
\]

Round 167 already proves the complete literal sector \(r\le R_{\log}\)
at \(L^2X^\varepsilon\). The sole Round-176 objective is therefore

\[
 \boxed{
 \Re\mathfrak C^{\rm rem}_{R_{\log}<r<R_0,\,2,\,{\rm opp},\,
 (d,d')<\gamma L}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon.}
\tag{176.2}
\]

The aggregate retains one real part outside every non-polylogarithmic even
shift and every opened divisor incidence. A proof of (176.2), combined only
with the accepted Round-167 sector, proves K17a. A rigorous first obstruction
for the frozen cross-gcd alternating-fibre mechanism is also a valid exit.
There is no in-round pivot.

## Literal coefficient and endpoint kernel

For \(N=dm\asymp L^2\), with \(d\) odd, retain

\[
 u_L(d,m)=\chi_4(d)\lambda_N(d)e(J\sqrt N),
 \qquad
 \lambda_N(d)=\omega_L(N)\rho_N(d)A_N(d).
\tag{176.3}
\]

Here \(\omega_L\) contains the exact half-open shell, squarefree projector,
and normalization; \(\rho_N\) is the canonical neither/both selector or the
no-pair value one; and \(A_N\) contains every profile, floor, star, hard point,
endpoint, and full-line zero extension. Both parity branches are retained.

For \(N+r=d'm'\), the endpoint kernel retains exactly

\[
 \left(1-\frac r{R_0}\right)
 \mathbf1_{R_{\log}<r<R_0}\mathbf1_{2\mid r}
 \mathbf1_{(d'-d)(m'-m)<0}
 \mathbf1_{(d,d')<\gamma L}
\tag{176.4}
\]

and the phase \(e(J(\sqrt{N+r}-\sqrt N))\). Its coefficient-independent
capacity is \(L^3X^\varepsilon\); the target is \(L^2X^\varepsilon\).

## Exact cross-gcd alternating fibres

First take the orientation

\[
 d'=d+p>d,\qquad m=m'+q>m',\qquad p,q>0.
\tag{176.5}
\]

Then \(p,q\) are even and

\[
 r=p m'-dq.
\tag{176.6}
\]

Introduce the cross gcd

\[
 \kappa=(d,m'),\qquad d=\kappa u,\qquad m'=\kappa v,
 \qquad (u,v)=1.
\tag{176.7}
\]

Since \(d\) is odd, \(\kappa,u\) are odd. Necessarily

\[
 r=\kappa h,\qquad h=pv-qu>0,
\tag{176.8}
\]

and \(h\) is even. For any parity-compatible solution \((p_0,q_0)\), all
parity-compatible solutions are exactly

\[
 p=p_0+2ut,\qquad q=q_0+2vt,
\tag{176.9}
\]

on the literal finite interval of admissible \(t\). Along this fibre,

\[
 \chi_4(d')\chi_4(d)
 =(-1)^{p/2}=\sigma_0(-1)^t,
\tag{176.10}
\]

and both endpoint products advance by the same increment

\[
 N(t)=N_0+K_\kappa t,\qquad
 N(t)+r=N_0+r+K_\kappa t,
 \qquad K_\kappa=2\kappa uv={2dm'\over\kappa}.
\tag{176.11}
\]

The opposite orientation \(d'<d,m'>m\) has the identical form after using
\(\kappa=(d',m)\) and the inward endpoints as anchors. It must be retained,
not inferred by deleting or conjugating a positive-gap sector.

Thus the complete literal fibre phase is

\[
 \Phi_{\kappa,u,v,h}(t)
 =J\{\sqrt{N_0+K_\kappa t+\kappa h}
       -\sqrt{N_0+K_\kappa t}\}+{t\over2},
\tag{176.12}
\]

with every field in (176.3)--(176.4) left inside its amplitude. The fibre
has \(O(1+\kappa)\) geometric sites before literal deletions.

## New mechanism under test

The only mechanism tested this round is whether the exact half-frequency
\((-1)^t\) in (176.10), retained jointly over the variable determinant
\(h\), can save the missing factor \(L\) before any fibre, determinant,
selector, or endpoint modulus.

A successful argument must do all of the following:

1. derive (176.5)--(176.12) with multiplicity one in both orientations;
2. keep the non-polylogarithmic \(h\)-sum and the \(t\)-sum coupled until the
   factor \(L\) is saved;
3. prove that squarefree opening, the selected/no-pair rule, the original
   low gcd \((d,d')<\gamma L\), profiles, hard faces, and zero-extension
   births/deaths preserve enough half-frequency cancellation;
4. control every residue class, incomplete fibre, canonical-solution jump,
   endpoint transition, and completion cost at \(L^2X^\varepsilon\); and
5. identify a literal property absent from constant-sign, erased-selector,
   dechirped, and arbitrary-support controls.

The exact derivative ledger is part of the gate. With \(x=N_0+K_\kappa t\),

\[
\begin{aligned}
 \Phi'(t)&={JK_\kappa\over2}{(x+\kappa h)^{-1/2}-x^{-1/2}\}+{1\over2},\\
 \Phi''(t)&={JK_\kappa^2\over4}{x^{-3/2}-(x+\kappa h)^{-3/2}\},\\
 \Phi'''(t)&={3JK_\kappa^3\over8}{(x+\kappa h)^{-5/2}-x^{-5/2}\}.
\end{aligned}
\tag{176.13}
\]

On a fixed-relative interior fibre,

\[
 \Phi''(t)\asymp {Jh\over\kappa L},\qquad
 |\Phi'''(t)|\asymp {Jh\over\kappa^2L}.
\tag{176.14}
\]

The half-frequency translates the stationary lattice but does not by itself
bound the distance to that lattice. Any rowwise Abel, derivative, Poisson,
or van der Corput step must be restored through its full dual-mode count.

## Required hostile controls

- **Constant-amplitude full fibre:** verify the exact alternating saving and
  determine which literal fields destroy or preserve it.
- **Odd squarefree Möbius openings:** check whether their progression steps
  preserve the half-frequency and account for every even/two-adic branch.
- **Selected and no-pair rows:** no selected-pair density or no-pair
  cancellation may be assumed.
- **Short cross-gcd fibres:** \(\kappa=O(1)\) have no internal cancellation;
  they must be controlled jointly rather than discarded.
- **Rowwise B-process:** after a modulus, its dual interval has scale
  \(1+Jh/L\) and one saddle has scale comparable to
  \((\kappa L/(Jh))^{1/2}\); restore the complete capacity.
- **Canonical-solution sawtooth:** a choice of \((p_0(h),q_0(h))\) may jump
  with \(h\); no smooth two-variable theorem may ignore those jumps.
- **Filter-erased arrays:** they can falsify a coefficient-uniform proof but
  are not literal lower mass.
- **Prior no-gos:** do not repeat fixed-shift triangle, direct
  Grimmelt--Merikoski placements, coefficient-uniform Schur closure, K26
  scale closure, or the Round-162 rank-one product collar.

## Promotion and stop rules

Promotion of (176.2) requires an exact complete proof and restored power
ledger. A strict sector is promotable only if it is owner-complete under an
explicit parameter range and leaves a strictly smaller named complement.

Otherwise stop at the first exact demonstration that the cross-gcd
half-frequency is erased, becomes selector variation of full size, returns
under a transform, or has rowwise/joint restored capacity above
\(L^2X^\varepsilon\). Scope any no-go only to the proved mechanism class.
Do not claim a lower bound for the literal K17a aggregate.

Even success closes only K17a and the complete residual scalar through the
accepted implication. Full displayed \(t=1\), every other hard-TOP channel,
complete hard TOP, both BAL scopes, UNBAL, M9--M2, direct M1 or GAR, endpoint
uniformity, M9, both bridges, the quarter theorem, and every exponent remain
separate.

## Allocation and terminal labels

The planned allocation is 100 percent analytical/algebraic and 0 percent
numerical. Mathematica or Python may be used only for bounded exact symbolic
identity or falsification checks, never for asymptotic certification.

Round 176 closes under exactly one label:

- `hard_top_t1_residual_k17a_variable_determinant_target`;
- `strict_k17a_cross_gcd_alternating_fibre_sector`; or
- `k17a_cross_gcd_alternating_fibre_capacity_or_self_return_no_go`.
