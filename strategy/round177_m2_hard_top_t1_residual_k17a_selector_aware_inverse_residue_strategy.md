# Round 177 strategy: selector-aware hybrid inverse-residue gate

## Frozen objective

Work on authoritative graph
"e3927f0ace0f3d74e9e9f5116a319159e3508838c7f7bd14b086fa851cad82b8".
Let

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,
\]

fix \(0<\gamma<1\), and put

\[
 R_{\log}=\min\{R_0-1,\lfloor(\log X)^{100}\rfloor\}.
\tag{177.1}
\]

Round 167 proves the complete sector \(r\le R_{\log}\). Round 176 proves
the complete literal sector \(\kappa_*\ge\delta L\) for every fixed
\(0<\delta<1/2\). Fix one such \(\delta\). The sole Round-177 objective is

\[
 \boxed{
 \Re\mathfrak C^{\rm rem}_{R_{\log}<r<R_0,\,2,\,{\rm opp},\,
 (d,d')<\gamma L,\,\kappa_*<\delta L}
 \ll_{\delta,\gamma,\varepsilon}L^2X^\varepsilon.}
\tag{177.2}
\]

The round tests a selector-aware signed hybrid estimate in which the
inverse-residue variable, determinant, fibre site, Fourier alias, and both
orientations remain coupled until the factor \(L\) is saved. A complete
proof of (177.2), combined only with accepted earlier sectors, closes K17a.
An owner-complete strict sector or a rigorously scoped first obstruction is
also a valid exit. There is no in-round pivot.

## Literal coefficient and exact inherited fibre

For \(N=dm\asymp L^2\), with \(d\) odd, retain

\[
 u_L(d,m)=\chi_4(d)\lambda_N(d)e(J\sqrt N),\qquad
 \lambda_N(d)=\omega_L(N)\rho_N(d)A_N(d).
\tag{177.3}
\]

Here \(\omega_L\) retains the exact normalized half-open shell and
squarefree projector, \(A_N\) retains both parity branches, profiles,
floors, stars, hard point values, endpoints, and full-line zero extension,
and \(\rho_N\) is literal. If the canonical opposite-character prime pair
\((p_N,q_N)\) exists, then

\[
 \rho_N(d)=1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
          +2\mathbf1_{p_Nq_N\mid d};
\tag{177.4}
\]

if no pair exists, \(\rho_N(d)=1\). No density, variation, or Fourier norm
for the selected/no-pair switch may be assumed.

For the plus orientation, Round 176 gives

\[
\begin{aligned}
 d&=\kappa u,& d'&=\kappa u+2s_t,\\
 m'&=\kappa v,& m&=\kappa v+2w_t,\\
 r&=2\kappa n,& s_tv-w_tu&=n,
\end{aligned}
\tag{177.5}
\]

where \(\kappa,u\) are odd, \((u,v)=1\),

\[
 s_t=[\bar v n]_u+ut,\qquad
 w_t=\frac{[\bar v n]_u v-n}{u}+vt.
\tag{177.6}
\]

The minus orientation uses
\(s_t=[-\bar v n]_u+ut\),
\(w_t=(n+[-\bar v n]_uv)/u+vt\), and \(uw_t-s_tv=n\).
The two orientations are disjoint and multiplicity one. On every nonzero
squarefree atom,

\[
 (d,d')=(u,n),\qquad
 \chi_4(d')\chi_4(d)=E_u(\pm\bar v n)(-1)^t,
 \qquad E_u(a)=(-1)^{[a]_u}.
\tag{177.7}
\]

Both endpoint products advance by \(2\kappa uv\). Literal support gives

\[
 u,v\asymp \frac L\kappa,\qquad
 n\ll\frac L\kappa,\qquad
 \#\{t:\Lambda^\pm_{\kappa,u,v,n}(t)\ne0\}\ll1+\kappa.
\tag{177.8}
\]

The amplitudes \(\Lambda^\pm\) and phases \(\Psi^\pm\) are exactly those in
(176.K17)--(176.K20), including the Fejer weight, the non-polylogarithmic
shift range, \((u,n)<\gamma L\), opposing-displacement inequalities,
endpoint conjugations, and all fields of (177.3).

## Exact alias block and sufficient theorem

For odd \(u\), write

\[
 c_u(k)=\frac{\widehat E_u(k)}u,\qquad
 \widehat E_u(k)=\frac{2}{1+e(-k/u)}.
\tag{177.9}
\]

Then \(\|c_u\|_1\ll\log(2u)\), \(\|c_u\|_2=1\), and
\(\|c_u\|_\infty\asymp1\). The constant-size coefficients lie at the
near-half aliases and may not be deleted.

For fixed \((\kappa,u,k)\), define the complete two-orientation hybrid block

\[
\begin{aligned}
 \mathcal H_{\kappa,u,k}
 =\sum_{\substack{v\asymp L/\kappa\\(u,v)=1}}
  \sum_{n\ll L/\kappa}\sum_{t\in\mathbb Z}
 \Bigg\{&
 \Lambda^+_{\kappa,u,v,n}(t)
 e\!\left(\Psi^+_{\kappa,u,v,n}(t)+\frac t2+
               \frac{k\bar v n}{u}\right)\\
 &+
 \Lambda^-_{\kappa,u,v,n}(t)
 e\!\left(\Psi^-_{\kappa,u,v,n}(t)+\frac t2-
               \frac{k\bar v n}{u}\right)
 \Bigg\}.
\end{aligned}
\tag{177.10}
\]

All displayed ranges are shorthand for the exact zero-extended literal
support, not a replacement rectangular weight. Fourier inversion gives the
exact low-cross-gcd aggregate

\[
 \Re\mathfrak C^{\rm rem}_{\rm low\text{-}\kappa}
 =\Re\sum_{\substack{\kappa<\delta L\\\kappa\ {\rm odd}}}
       \sum_{u\asymp L/\kappa}\sum_{k\bmod u}
       c_u(k)\mathcal H_{\kappa,u,k}.
\tag{177.11}
\]

Either of the following is sufficient, after absorbing logarithms into
\(X^\varepsilon\):

\[
 \boxed{
 \left|\sum_{k\bmod u}c_u(k)\mathcal H_{\kappa,u,k}\right|
 \ll_{\delta,\gamma,\varepsilon}L X^\varepsilon}
\tag{177.12}
\]

uniformly in supported \((\kappa,u)\), or the stronger aliaswise bound

\[
 \boxed{
 \max_{k\bmod u}|\mathcal H_{\kappa,u,k}|
 \ll_{\delta,\gamma,\varepsilon}L X^\varepsilon.}
\tag{177.13}
\]

Indeed, there are \(O(L/\kappa)\) supported \(u\)'s for each \(\kappa\), so

\[
 \sum_{\kappa<\delta L}\sum_{u\asymp L/\kappa}L
 \ll L^2\log(2L).
\tag{177.14}
\]

This is deliberately weaker than demanding the fixed-\(v\) estimate
(176.K35). A fixed-\(v\) block has \(O(L)\) raw \((n,t)\)-capacity and
(176.K35) asks for \(O(\kappa)\), which is stronger than generic square
root when \(\kappa\ll\sqrt L\). The complete block (177.10) has raw capacity

\[
 \frac L\kappa\cdot\frac L\kappa\cdot\kappa
 \asymp\frac{L^2}{\kappa},
\tag{177.15}
\]

and (177.12) asks for exactly the missing gain \(L/\kappa\). A lone
square-root saving in the \(v\)-inverse-residue sum leaves
\(L\sqrt{L/\kappa}\), still above (177.12). A second coupled saving of size
\(\sqrt{L/\kappa}\), or an equivalent signed energy contraction, is needed.

If \(g=(u,n)\), \(u=gu_0\), and \(n=gn_0\), the exact primitive reduction

\[
 E_u(\pm\bar v n)=E_{u_0}(\pm\bar v n_0)
\tag{177.16}
\]

must also be tested. The conductor may collapse from \(u\) to \(u_0\), but
the associated gcd multiplicity and the original cutoff \(g<\gamma L\)
must be restored. The congruence \(\bar v n\equiv s_0\pmod u\) merely turns
the alias into \(e(ks_0/u)\); summing all aliases reconstructs
\((-1)^{s_0}\) and gives no cancellation by itself.

## Mechanism under test

The only new analytic mechanism is a hybrid reciprocal large-sieve or
\(TT^*\) argument that keeps the \(v,n,t\) variables and the alias packet
signed. Permitted implementations include:

1. incomplete \(v\)-completion or reciprocity followed by a joint
   determinant/fibre energy estimate;
2. a bilinear inverse-residue large sieve with the \(t\)-oscillation kept
   inside the coefficients;
3. primitive-modulus stratification using (177.16), with all gcd costs
   restored; or
4. a signed two-orientation identity that contracts only after their exact
   endpoint phases and conjugations are combined.

Every implementation must derive its diagonal and off-diagonal terms,
conductor, incomplete-interval cost, exceptional gcd strata, stationary
aliases, and final \(L\)-power. A named large-sieve theorem may be used only
after every hypothesis and normalization is checked against the literal
selector-dependent amplitude.

## Required hostile controls

- **Near-half alias:** \(k=(u\pm1)/2\) has coefficient of constant size.
  It is the main alias, not an error term.
- **Small and imprimitive aliases:** check \(k=0\), \((k,u)>1\), and
  \((kn,u)>1\); any reduced conductor must pay its multiplicity.
- **Large \((u,n)\):** primitive modulus \(u_0\) can collapse even in the
  accepted low-original-gcd range.
- **Incomplete \(v\)-interval:** literal \(v\asymp L/\kappa\) is a bounded
  interval of length comparable with, but not automatically equal to, the
  modulus.
- **Selector switching:** selected rows use (177.4), while no-pair rows have
  \(\rho_N=1\). No cancellation between these cases may be assumed.
- **Squarefree openings and two-adic branches:** restore odd-square moduli,
  coprimality, parity, and every progression count.
- **Short fibres:** small \(\kappa\) may give only \(O(1)\) \(t\)-sites;
  cancellation must then come from the coupled \(v,n\) structure.
- **Stationary and dechirped modes:** the square-root phase may align with a
  reciprocal alias on subfamilies. Count them rather than assuming generic
  oscillation.
- **Both orientations and real part:** do not take separate moduli if their
  signed interaction is needed.
- **False arrays:** selector-erased, constant-anchor, arbitrary-support,
  or dechirped examples can disprove a coefficient-uniform mechanism but
  are not literal lower bounds.

## Promotion and stop rules

Promotion of (177.2) requires a complete literal proof of (177.11) with a
restored \(L^2X^\varepsilon\) ledger. A strict sector is promotable only if
its parameter range is explicit, its exact complement is named, all literal
owners are retained, and it strictly reduces the open low-cross-gcd region.

Otherwise stop at the first exact demonstration that the hybrid
inverse-residue route loses its conductor, pays a full diagonal, reconstructs
the physical sum under \(TT^*\), is defeated by selector variation, or
returns capacity above \(L^2X^\varepsilon\). Scope any no-go only to the
proved mechanism class. Do not claim a lower bound for the literal K17a
aggregate.

Even success closes only K17a and the complete residual scalar through
accepted implications. Full displayed \(t=1\), every other hard-TOP channel,
complete hard TOP, both BAL scopes, UNBAL, M9--M2, both direct M1 parents or
GAR, endpoint uniformity, M9, both bridges, the quarter theorem, and every
global exponent remain separate.

## Allocation and terminal labels

The planned allocation is 100 percent analytical/algebraic and 0 percent
numerical. Python or Mathematica may be used only for a bounded exact
symbolic identity or finite falsification check, never for asymptotic
certification.

Round 177 closes under exactly one label:

- "hard_top_t1_residual_k17a_joint_inverse_residue_target";
- "strict_k17a_low_cross_gcd_selector_aware_sector"; or
- "k17a_joint_inverse_residue_alias_capacity_or_self_return_no_go".
