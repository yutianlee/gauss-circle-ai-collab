# Conductor candidate: congruence-aligned coarse-quotient cross-group bound

Status: Round-88 conductor candidate; independently certified by the
blind, discovery, and hostile count/ownership reviews.  It becomes
accepted mathematics only through the validated Round-88 State Patch.

## 1. Exact coarse groups

Fix \(b\), its exact class modulus \(M\asymp B\), and a divisor
\(m\mid M\).  Write

\[
 R={M\over m}.
\]

For a physical ordered pair \(P=(x,y)\) of distinct units modulo \(M\),
reduce \(P\) modulo \(m\) and apply the same full-prime-power
active-set/active-label rule as in Round 87.  Denote the resulting
coarse group by \(\Gamma_m(P)\).  Thus two reductions have the same
coarse group precisely when, at each full prime-power factor of \(m\),
they are both locally diagonal or are locally identical and active.

For a coarse group \(\gamma\), define

\[
 K_{b,m,\gamma}(\theta)
 =\Pi_{b,D}\sum_{\Gamma_m(P)=\gamma}F_{b,P}(\theta),
\]

using the normalized physical-pair functions of the Round-88 packet.
No new \(M^{-2}\) occurs.

The coarse active set is allowed to be empty.  This is essential:
fine off-diagonal physical pairs may become diagonal at every factor
after reduction modulo \(m\).

## 2. Coarse positive package

Let

\[
 \mathcal P_m(D)
 =\sum_{b\asymp B}\int_{\mathbb T}|D_D(\theta)|^2
 \sum_\gamma|K_{b,m,\gamma}(\theta)|^2\,d\theta.
\]

Then

\[
 \boxed{\mathcal P_m(D)
 \ll_\varepsilon
 X^\varepsilon D B^3R^2T^4Q^{-5/6}.}
 \tag{C88.1}
\]

Indeed, factor \(m\) into its full prime-power factors.  For a coarse
active set \(S\), let \(m_S\) be its active product and \(r_S=m/m_S\).
There are at most \(m_S^2\) active labels and at most \(r_S\) inactive
common units.  Every coarse ordered pair has at most \(R^2\) lifts to
an ordered pair modulo \(M\).  Since

\[
 \|\Pi_{b,D}F_{b,P}\|_\infty
 \ll_\varepsilon X^\varepsilon T^2Q^{-5/12},
\]

we obtain

\[
\begin{aligned}
 \sum_{\gamma:\,S(\gamma)=S}|K_{b,m,\gamma}|^2
 &\ll_\varepsilon
 X^\varepsilon m_S^2(r_SR^2)^2T^4Q^{-5/6}\\
 &=X^\varepsilon m^2R^4T^4Q^{-5/6}\\
 &=X^\varepsilon M^2R^2T^4Q^{-5/6}.
\end{aligned}
\]

Summing the \(X^\varepsilon\)-many active sets, using
\(\int|D_D|^2=D\), and then summing \(O(B)\) conductors proves
(C88.1).  This count is valid for non-coprime \(m\mid M\), arbitrary
prime powers, the full \(2\)-part, and nonunit local \(K\), because it
uses only reductions and lift counts of actual physical unit pairs.

## 3. Exact congruence-aligned shells and the signed off-diagonal

For two physical pairs \(P,P'\), let \(R_*(P,P')\) be the unique product
of local prime-power lift depths such that

\[
 \Gamma_{M/R}(P)=\Gamma_{M/R}(P')
 \quad\Longleftrightarrow\quad
 R_*(P,P')\mid R.
\]

This is the divisor-lattice form of first coarse-group coincidence.
It is an exact physical-pair congruence depth; it need not equal every
functional additive-period depth created by the unit mask, an affine
\(u\)-cancellation, nonunit \(K\), or an extra \(2\)-adic period.
The exact shell \(R_*=R\) follows from the coarse relations by divisor
Möbius inversion.  Hence the signed Fejer contribution of all shells
\(1<R_*\leq R_0\) is a linear combination, with total
\(X^\varepsilon\) divisor cost, of the packages \(\mathcal P_{M/R}\).

To retain the packet's \(u\ne0\) ownership, use the centered Fejer
kernel

\[
 \mathcal K_D^\circ(\theta)=|D_D(\theta)|^2-D.
\]

Its Fourier coefficient at shift zero is exactly zero and

\[
 \|\mathcal K_D^\circ\|_{L^1(\mathbb T)}
 \leq \||D_D|^2\|_1+D=2D.
\]

Replacing \(|D_D|^2\) by \(\mathcal K_D^\circ\) in every divisor-shell
identity therefore keeps precisely \(u\ne0\) and gives the same bound
as (C88.1), up to an absolute factor.  The accepted global \(u=0\)
owner is never reinserted.

Consequently,

\[
 \boxed{
 |\mathcal G_{\rm cross}^{\,R_*\leq R_0}(D)|
 \ll_\varepsilon
 X^\varepsilon D B^3R_0^2T^4Q^{-5/6}.}
 \tag{C88.2}
\]

The expansion is made from the actual \(F_{b,P}\), so both Ramanujan
cross terms, the square term, both signs, reflected orientations,
support endpoints, and the actual fourfold stationary symbol are
retained automatically.

## 4. Target comparison

Dividing (C88.2) by the target gives

\[
 R_0^2B^4T^4Q^{-5/6}J^{-14/5}
 \leq R_0^2J^{-2/15}.
\]

Therefore every exact cross-group shell whose first coarse quotient
satisfies

\[
 \boxed{R_*\leq R_{\rm crit}(B):=J^{11/30}B^{-2}}
\]

is target-safe.  Since

\[
 J^{11/90}\leq B\leq J^{3/20},
\]

this criterion is uniformly nonempty and implies
\(R_*\leq J^{1/15}\) at the top conductor.  At the lower endpoint it
allows \(R_*\leq J^{11/90}\asymp B\), consistently recovering the
entire coefficient-blind coarse package at the already closed
conductor threshold.

This is a nonempty strict deletion; for example \(R_*=2\) shells occur
in the exact full \(2\)-part classes.  The hostile physical-label
family with \(M=3^\nu\) and two full labels coinciding modulo \(M/3\)
has \(R_*=3\) and belongs to the congruence package.  Identifying that
label family with its separately computed \(M^2/3\) completed-trace
value still requires the exact label-to-\((A,B,V)\) seam.

## 5. Exact survivor and caveats

The remaining cross-group object consists of:

- cross groups with first coarse quotient
  \(R_*>J^{11/30}B^{-2}\);
- functional period drops not produced by coarse same-group
  coincidence, including small-prime critical residues, affine
  \(u\)-cancellation, nonunit \(K\), and extra \(2\)-adic periods;
- genuinely aperiodic local traces.

The argument proves no estimate for that survivor and makes no claim
for a conductor extension, transitions, axes, cone edges, other radial
sectors, full \(M9\!-\!M1\), \(M9\!-\!M2\), \(M9\), or the global
exponent.
