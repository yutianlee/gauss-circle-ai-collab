# Conductor candidate: primitive-anchor modulus sector

## Candidate lemma

Assume the complete literal hypotheses and notation of the accepted
Round-176 cross-gcd alternating-fibre reduction. Fix
\(0<\delta<1/2\) and \(A>0\), and put

\[
 Q=(\log X)^A,\qquad
 g=(u,n),\qquad u_0=\frac ug.
\tag{177.C1}
\]

In both opposing orientations, retain the exact non-polylogarithmic
low-cross-gcd aggregate with \(\kappa_*<\delta L\), and restrict it further
to \(u_0\le Q\). Then

\[
 \boxed{
 \left|
 \mathfrak C^{\rm rem}_{R_{\log}<r<R_0,\,2,\,{\rm opp},\,
 (d,d')<\gamma L,\,\kappa_*<\delta L,\,u/(u,n)\le Q}
 \right|
 \ll_{A,\delta,\gamma,\varepsilon}L^2X^\varepsilon.}
\tag{177.C2}
\]

The exact complementary Round-177 sector is

\[
 \kappa_*<\delta L,\qquad
 \frac{u}{(u,n)}>(\log X)^A.
\tag{177.C3}
\]

No cancellation is claimed in (177.C2). The proof is a primitive-modulus
capacity count that retains every literal selector and endpoint field.

## Proof

Fix \(\kappa\) and a supported \(u\). Literal endpoint support gives

\[
 u\asymp U,\qquad v\asymp U,\qquad n\ll U,\qquad
 U=\frac L\kappa.
\tag{177.C4}
\]

Fix a divisor \(u_0\mid u\), put \(g=u/u_0\), and impose
\((u,n)=g\). Then

\[
 n=gn_0,\qquad (n_0,u_0)=1,\qquad
 n_0\ll\frac Ug\asymp u_0.
\tag{177.C5}
\]

Consequently there are \(O(u_0)\) possible determinants \(n\) in this
stratum. There are \(O(U)\) possible \(v\)'s before the coprimality and
literal deletions. Each of the two exact fibres has
\(O(1+\kappa)=O(\kappa)\) sites. Hence the number of complete literal atoms
at fixed \((\kappa,u,u_0)\) is

\[
 O(u_0U\kappa)=O(u_0L).
\tag{177.C6}
\]

The Fejer factor is at most one, every literal opened coefficient is
bounded, and the squarefree projector, selected/no-pair rule, original-gcd
cutoff, parity branches, displacement inequalities, profiles, hard values,
endpoints, and zero extension only delete or downweight atoms. Thus (177.C6)
also bounds the absolute contribution of the stratum, up to
\(X^\varepsilon\) divisor multiplicity.

For \(u_0\le Q\),

\[
 \sum_{\substack{u_0\mid u\\u_0\le Q}}u_0
 \le Q\tau(u)\ll_\varepsilon QX^\varepsilon.
\tag{177.C7}
\]

There are \(O(U)=O(L/\kappa)\) supported \(u\)'s. Summing (177.C6)--(177.C7)
over odd \(\kappa<\delta L\) gives

\[
\begin{aligned}
 \left|\mathfrak C^{\rm rem}_{u_0\le Q}\right|
 &\ll_\varepsilon
 \sum_{\kappa<\delta L}\frac L\kappa\cdot LQX^\varepsilon\\
 &\ll L^2Q\log(2L)X^\varepsilon
 \ll_{A,\varepsilon}L^2X^{2\varepsilon}.
\end{aligned}
\tag{177.C8}
\]

Renaming \(2\varepsilon\) as \(\varepsilon\) proves (177.C2). Both
orientations change only the absolute constant. The one outer real part is
retained until the final harmless modulus.

## Exact alias-energy limitation on the complement

The primitive identity from Round 176 is

\[
 E_u(\pm\bar v n)=E_{u_0}(\pm\bar v n_0).
\tag{177.C9}
\]

For any fixed remaining labels, collect the complete literal physical
amplitude with primitive anchor residue \(a\bmod u_0\) into \(F(a)\), and
define

\[
 H(k)=\sum_{a\bmod u_0}F(a)e(ka/u_0).
\tag{177.C10}
\]

Fourier inversion gives

\[
 \sum_{a\bmod u_0}E_{u_0}(a)F(a)
 =\sum_{k\bmod u_0}c_{u_0}(k)H(k),
\qquad \|c_{u_0}\|_2=1.
\tag{177.C11}
\]

Parseval and Cauchy give exactly

\[
 \left|\sum_kc_{u_0}(k)H(k)\right|
 \le\left(\sum_k|H(k)|^2\right)^{1/2}
 =u_0^{1/2}\left(\sum_a|F(a)|^2\right)^{1/2}.
\tag{177.C12}
\]

This is identical to direct Cauchy in the physical anchor residue because
\(|E_{u_0}(a)|=1\). Thus DFT followed only by aliaswise Cauchy, Parseval,
or a coefficient-blind \(TT^*\) step is a unitary self-return and supplies
no contraction. The false coefficient control
\(F(a)=\overline{E_{u_0}(a)}B\) attains equality in (177.C12). It is not a
literal lower-mass construction, but it proves that any contraction must
use a literal property discarded by that norm.

At fixed \((\kappa,u,u_0)\), the raw capacity (177.C6) is \(u_0L\).
A single square-root inverse-residue saving leaves \(u_0^{1/2}L\), still
above the local target \(L\) when \(u_0\) is a power scale. The open
complement (177.C3) therefore needs a full factor \(u_0\), arising from two
coupled square-root savings or an equivalent selector-aware signed theorem
before the alias, progression, endpoint, or orientation moduli.

## Scope

The candidate proves only the small primitive-anchor-modulus strict sector
(177.C2) and the route-scoped alias-\(\ell^2\) self-return (177.C12). It
does not prove the complementary large-\(u_0\) estimate, complete K17a, the
residual scalar, full displayed \(t=1\), another hard-TOP channel, hard TOP,
either BAL scope, UNBAL, M9--M2, either direct M1 parent or GAR, endpoint
uniformity, M9, a bridge, the quarter theorem, or any exponent improvement.
