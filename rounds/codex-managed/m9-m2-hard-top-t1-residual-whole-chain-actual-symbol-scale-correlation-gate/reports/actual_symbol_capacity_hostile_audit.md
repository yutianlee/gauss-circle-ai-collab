# Round 175 hostile audit: actual-symbol whole-chain scale capacity

- Campaign: m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate
- Task: actual_symbol_capacity_hostile_audit
- Role: barrier/no-go auditor
- Starting graph: e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211
- Allocation: 100% analytical/algebraic; 0% numerical

## 1. Result

### Whole-chain scale-coboundary and positive-capacity no-go

The complete stopped-chain nonzero-ordinary-frequency aggregate has no
independent cancellation variable in the scale index. After all odd
character frequencies and all nonzero ordinary frequencies are recombined,
define

\[
 Z_{\epsilon,*}(\theta)
 ={i\over2}\sum_{k\ {\rm odd}}\chi _4(k)
       \sum_{\ell\ne0}U_{k,\ell}^{(\epsilon)}(\theta),
 \qquad
 \mathcal Q_R^*={1\over2}\sum_{\epsilon=0}^1
       \int_0^1F_R(\theta)|Z_{\epsilon,*}(\theta)|^2\,d\theta .
\tag{175.H1}
\]

The factors in (175.H1) are exact: \(i/2\) is the character-Poisson
constant, and \(1/2\) is the absolute-parity average. Equivalently,
expanding the square gives the factor \(1/8\) and the one outer real part
in (175.4). No modulus over a character frequency, ordinary frequency,
cardinal cell, arithmetic opening, endpoint, or transition has been
inserted.

For every \(R<S\le2R\), including the strict final link,

\[
 \boxed{\mathcal N_{R,S}=\mathcal Q_S^*-\mathcal Q_R^*.}
\tag{175.H2}
\]

Consequently the exact unweighted stopped chain is

\[
 \boxed{
 \sum_{j=0}^{K-1}\mathcal N_{R_j,R_{j+1}}
 =\mathcal Q_M^*-\mathcal Q_{R_0}^*.}
\tag{175.H3}
\]

Thus summing all links creates no cancellation resource beyond the two
endpoint Fejer energies. In physical lag variables the conclusion is
stronger: every link coefficient is nonnegative, so a fixed correlation
has the same sign on every scale on which it occurs. All interior scales
cancel algebraically in (175.H3), not analytically.

The lower endpoint is already target-safe:

\[
 0\le \mathcal Q_{R_0}^*\ll_\varepsilon
 R_0L^2X^\varepsilon\ll_\varepsilon L^3X^\varepsilon.
\tag{175.H4}
\]

Therefore the deliberately one-sided target (175.5) is equivalent, at
target strength, to the single literal maximal-scale positive theorem

\[
 \boxed{\mathcal Q_M^*\ll_\varepsilon L^3X^\varepsilon.}
\tag{175.H5}
\]

The coefficient-insensitive positive estimate gives only

\[
 \mathcal Q_M^*\ll_\varepsilon ML^2X^\varepsilon
 \asymp L^4X^\varepsilon.
\tag{175.H6}
\]

That operator scale is sharp on the admitted nonliteral
dechirped/rank-one control. It is not a lower bound for the literal
residual coefficient. Hence dyadic Haar energy, scale Abel transfer,
selector or squarefree projector identities, termwise character pairing,
endpoint positivity, and positive transformed norms do not by themselves
supply the missing factor \(L\).

The narrow obstruction is only to symbol-blind linear scale recombination
followed by coefficient-uniform positivity. A new coefficient-sensitive
proof of (175.H5), or its exactly equivalent signed physical or fully
transformed formulation, remains unexcluded. The recommended terminal
label is

\[
 \boxed{\texttt{whole\_chain\_actual\_symbol\_capacity\_or\_self\_return\_no\_go}.}
\]

## 2. Exact statement and hypotheses

Assume the complete Round-175 freeze:

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,\qquad M\asymp L^2,
\]

and

\[
 c_N^{\rm rem}
 =\sum_{\substack{d\mid N\\d\ {\rm odd}}}
   \chi _4(d)\lambda_N(d),\qquad
 \lambda_N(d)=\omega_L(N)\rho_N(d)A_N(d),
 \qquad z_N=c_N^{\rm rem}e(J\sqrt N).
\tag{175.H7}
\]

Here \(\omega_L,\rho_N,A_N\) retain the exact literal shell, squarefree
and coprimality masks, selector complement or no-pair value, two-adic
branch, profile, floors, stars, support crossings, point values, endpoints,
and zero-extension values. The coefficient is supported in a positive
\(M\)-site containing interval and

\[
 D_L=\sum_N|z_N|^2\ll_\varepsilon L^2X^\varepsilon.
\tag{175.H8}
\]

Let

\[
 w_R(r)=\left(1-{r\over R}\right)_+,\qquad
 C_r=\sum_Nz_{N+r}\overline {z_N},\qquad A_r=\Re C_r,
\]

and

\[
 \mathfrak E_R^{(2)}
 =D_L+2\sum_{\substack{r>0\\2\mid r}}w_R(r)A_r.
\tag{175.H9}
\]

The stopped chain is exactly

\[
 R_{j+1}=\min(2R_j,M),\qquad R_K=M,
\tag{175.H10}
\]

with minimal \(K\); the last link is not rounded.

Let \(\mathcal O_{R,S}\) denote the complete part of the exact transform
with at least one of \(\ell,\ell'\) equal to zero, after the signed sum
over all odd \(k,k'\). Then

\[
 \mathfrak E_S^{(2)}-\mathfrak E_R^{(2)}
 =\mathcal N_{R,S}+\mathcal O_{R,S}.
\tag{175.H11}
\]

The inherited collective zero-mode estimate and the geometric scale sum
give

\[
 \sum_{j<K}|\mathcal O_{R_j,R_{j+1}}|
 \ll_\varepsilon L^3X^\varepsilon.
\tag{175.H12}
\]

This is not a fixed-\(k\), fixed-cell, or fixed-dual-diagonal estimate.
It uses the complete odd-character recombination.

The exact short correction is

\[
 B_{\rm short}
 =\sum_{\substack{0<r<R_0\\2\mid r}}
 r\left({1\over R_0}-{1\over M}\right)A_r,\qquad
 |B_{\rm short}|\le R_0D_L
 \ll_\varepsilon L^3X^\varepsilon,
\tag{175.H13}
\]

and is paid once. With \(T_{26}\) denoting the literal K26 scalar,

\[
 \boxed{
 \sum_{j<K}\mathcal N_{R_j,R_{j+1}}
 =2(T_{26}+B_{\rm short})
  -\sum_{j<K}\mathcal O_{R_j,R_{j+1}}.}
\tag{175.H14}
\]

Thus (175.5), (175.H5), and the one-sided K26 estimate are equivalent up
to already target-safe quantities. No statement below is a physical lower
bound.

## 3. Proof or derivation

### 3.1 Complete frequency recombination and exact scale collapse

Set

\[
 V_{\epsilon,*}(\theta)
 =\sum_{k\ {\rm odd}}\chi_4(k)
   \sum_{\ell\ne0}U_{k,\ell}^{(\epsilon)}(\theta).
\]

Rapid convergence of the exact cardinal transform permits the sums to be
recombined without changing their order. The double frequency sum in
(175.4) is then \(V_{\epsilon,*}\overline{V_{\epsilon,*}}\). Since
\(Z_{\epsilon,*}=(i/2)V_{\epsilon,*}\),

\[
\begin{aligned}
 \mathcal N_{R,S}
 &=\frac18\sum_{\epsilon=0}^1
   \int_0^1(F_S-F_R)(\theta)
       |V_{\epsilon,*}(\theta)|^2\,d\theta\\
 &=\frac12\sum_{\epsilon=0}^1
   \int_0^1(F_S-F_R)(\theta)
       |Z_{\epsilon,*}(\theta)|^2\,d\theta.
\end{aligned}
\tag{175.H15}
\]

This proves (175.H2). Summing (175.H2) proves (175.H3) pointwise in
\(\theta\), including an unrounded final link:

\[
 \sum_{j<K}(F_{R_{j+1}}-F_{R_j})=F_M-F_{R_0}.
\tag{175.H16}
\]

Both absolute-parity branches remain in the sum over \(\epsilon\), all
ordinary frequencies are nonzero, and every literal cell, boundary,
transition, and zero-extension piece remains inside \(Z_{\epsilon,*}\).

Let \(Z_\epsilon=Z_{\epsilon,0}+Z_{\epsilon,*}\) be the exact ordinary
zero/nonzero split. Parseval gives \(\|Z_\epsilon\|_2^2=D_L\), while the
collective zero-mode estimate gives

\[
 \|Z_{\epsilon,0}\|_\infty
 \ll {L^2\over J}X^\eta.
\tag{175.H17}
\]

Consequently

\[
 {1\over2}\sum_\epsilon\|Z_{\epsilon,*}\|_2^2
 \ll_\varepsilon L^2X^\varepsilon.
\tag{175.H18}
\]

Because \(0\le F_R\le R\), equations (175.H4) and (175.H6) follow.
Furthermore, summing the standard zero-containing bound over the geometric
chain costs only \(\sum_j(R_j+R_{j+1})\ll M\):

\[
 \sum_j|\mathcal O_{R_j,R_{j+1}}|
 \ll M\left(D_L^{1/2}{L^2\over J}+{L^4\over J^2}\right)X^{O(\eta)}
 \ll_\varepsilon L^3X^\varepsilon,
\tag{175.H19}
\]

using \(M\asymp L^2\) and \(J\ge L^2\). This proves (175.H12).

### 3.2 Physical endpoint identity: no sign in the scale variable

For one link put \(b_{R,S}(r)=w_S(r)-w_R(r)\). Directly,

\[
 b_{R,S}(r)=
 \begin{cases}
 r(S-R)/(RS),&0<r<R,\\
 1-r/S,&R\le r<S,\\
 0,&r\ge S,
 \end{cases}
\tag{175.H20}
\]

so \(b_{R,S}(r)\ge0\) for every positive \(r\). Hence

\[
 \sum_{j<K}b_{R_j,R_{j+1}}(r)
 =w_M(r)-w_{R_0}(r)
 =\begin{cases}
 r(1/R_0-1/M),&0<r<R_0,\\
 1-r/M,&R_0\le r<M,\\
 0,&r\ge M.
 \end{cases}
\tag{175.H21}
\]

It follows that

\[
 \sum_{j<K}\left\{\mathfrak E_{R_{j+1}}^{(2)}
                    -\mathfrak E_{R_j}^{(2)}\right\}
 =2\sum_{\substack{r>0\\2\mid r}}
    (w_M(r)-w_{R_0}(r))A_r.
\tag{175.H22}
\]

Subtracting (175.H13) exactly once gives

\[
 \boxed{
 T_{26}=\sum_{\substack{R_0\le r<M\\2\mid r}}
       \left(1-{r\over M}\right)A_r.}
\tag{175.H23}
\]

Thus there is no alternating or mean-zero scale coefficient to exploit.
Any cancellation left in (175.H23) is correlation among the literal
\(A_r\)'s, not cancellation among scale links.

### 3.3 Weighted scale summation by parts

For arbitrary real scale weights \(a_0,\ldots,a_{K-1}\), exact discrete
summation by parts gives both the kernel and transformed identities

\[
\boxed{\begin{aligned}
 \sum_{j<K}a_j(F_{R_{j+1}}-F_{R_j})
 &=a_{K-1}F_M-a_0F_{R_0}
   +\sum_{j=1}^{K-1}(a_{j-1}-a_j)F_{R_j},\\
 \sum_{j<K}a_j\mathcal N_{R_j,R_{j+1}}
 &=a_{K-1}\mathcal Q_M^*-a_0\mathcal Q_{R_0}^*
   +\sum_{j=1}^{K-1}(a_{j-1}-a_j)\mathcal Q_{R_j}^*.
\end{aligned}}
\tag{175.H24}
\]

For the target weights \(a_j\equiv1\), every interior term in (175.H24)
is exactly zero. Artificial oscillating or decaying scale weights merely
introduce the interior Fejer energies; they do not estimate the constant
weight. If those energies are closed by the available positive bound,

\[
 \left|\sum_ja_j\mathcal N_j\right|
 \ll_\varepsilon L^2X^\varepsilon
 \left(|a_{K-1}|M+|a_0|R_0+
       \sum_{j=1}^{K-1}|a_{j-1}-a_j|R_j\right).
\tag{175.H25}
\]

For \(a_j=1\), the first term restores \(ML^2\asymp L^4\). Avoiding that
term changes the quantity being estimated; reconstructing the constant
weight restores it.

### 3.4 Haar energy is genuinely weighted and restores the top scale

On an exact doubling link the inherited identity is

\[
 \mathfrak E_{2R}^{(2)}=2\mathfrak E_R^{(2)}
 -\mathfrak H_R^{(2)},\qquad \mathfrak H_R^{(2)}\ge0.
\tag{175.H26}
\]

Writing \(q_R=\mathfrak E_R^{(2)}/R\) gives the actual martingale law

\[
 q_{2R}=q_R-{\mathfrak H_R^{(2)}\over2R}.
\tag{175.H27}
\]

Along a purely doubling subchain \(R_q=2^qR_0\),

\[
 \sum_{j<q}{\mathfrak H_{R_j}^{(2)}\over2R_j}
 =q_{R_0}-q_{R_q}\le q_{R_0}\le D_L.
\tag{175.H28}
\]

This is a valid cross-scale square-function resource, but it has weight
\(1/R_j\). If \(M=R_q\), restoring the unweighted endpoint gives

\[
 \mathfrak E_M^{(2)}-\mathfrak E_{R_0}^{(2)}
 =(M-R_0)q_{R_0}
  -M\sum_{j<q}{\mathfrak H_{R_j}^{(2)}\over2R_j}.
\tag{175.H29}
\]

The two separately positive capacities in (175.H29) are both \(O(MD_L)\),
namely \(L^4X^\varepsilon\); their possible cancellation is exactly the
endpoint problem again. A strict final \(R<S<2R\) has no Haar identity
and is governed by (175.H20). It does not alter (175.H16) or create a
terminal gain.

### 3.5 Selector, squarefree, and character identities

If a pair \(p_N,q_N\) is selected and \(M_N=p_Nq_NR_N\), then
\(\chi_4(p_Nq_N)=-1\) and the exact complement-of-XOR identity is

\[
\begin{aligned}
 \sum_{d\mid M_N}\chi_4(d)\rho_N(d)A_N(d)
 &=\sum_{a\mid R_N}\chi_4(a)
   \{A_N(a)+\chi_4(p_Nq_N)A_N(p_Nq_Na)\}\\
 &=\sum_{a\mid R_N}\chi_4(a)
   \{A_N(a)-A_N(p_Nq_Na)\}.
\end{aligned}
\tag{175.H30}
\]

For a unit amplitude (175.H30) vanishes. For the literal amplitude it is
not a small local difference: the multiplicative displacement is at least
\(p_Nq_N\ge15\), the two physical supports may be disjoint, and all
profile, endpoint, selector, and zero-extension jumps remain. In the
no-pair shadow, if every odd prime factor is \(1\pmod4\), then every
divisor character equals \(+1\). Therefore neither selected ambient mass
balance nor termwise character balance proves a uniform saving.

The squarefree identity

\[
 \mu^2(N)=\sum_{a^2\mid N}\mu(a)
\tag{175.H31}
\]

and the analogous coprimality Möbius identity are projectors, not
mean-zero weights on literal support. On a squarefree surviving \(N\),
the sum in (175.H31) has only \(a=1\). Opening two projectors introduces
overlapping signed representations; after exact recombination it returns
the literal indicator, while absolute opening costs \(X^\varepsilon\) and
supplies no factor \(L^{-1}\).

For an even physical gap, the tangent chart gives

\[
 \chi_4(d')\chi_4(d)=(-1)^s.
\tag{175.H32}
\]

The Round-173 alternating first difference has a target-safe bandpass
commutator, but its remainder satisfies

\[
 \mathcal R_{R,S}=\Delta_{R,S}-\mathcal C_{R,S},\qquad
 \sum_j|\mathcal C_{R_j,R_{j+1}}|
 \ll_\varepsilon L^3X^\varepsilon.
\tag{175.H33}
\]

Thus its whole-chain estimate is (175.H14) again. Pairing the dual
character frequencies also gives only the exact rewrite

\[
 \sum_{k\ {\rm odd}}\chi_4(k)U_{k,\ell}
 =\sum_{\substack{k>0\\k\ {\rm odd}}}\chi_4(k)
   (U_{k,\ell}-U_{-k,\ell}),
\tag{175.H34}
\]

with no smallness: the cardinal support is on positive product cells and
has no \(k\leftrightarrow-k\) symmetry. A gain from (175.H30) or
(175.H34) therefore requires a new global literal correlation theorem,
not another algebraic pairing.

### 3.6 Sharp nonliteral capacity and normalization controls

Let \(M=4P\), take a positive translate of an \(M\)-site interval, and put
\(z_N=1\) on its \(2P\) even sites and zero elsewhere. Equivalently, the
nonliteral coefficient is phase-adapted by \(c_N=e(-J\sqrt N)\) on those
sites. Then

\[
 D_L=2P,\qquad A_{2s}=2P-s\quad(1\le s<2P),
\]

and direct summation of the exact top tent gives

\[
 \boxed{
 \mathfrak E_{4P}^{(2)}-\mathfrak E_{2P}^{(2)}=P^2
 ={1\over8}MD_L.}
\tag{175.H35}
\]

At the coefficient-insensitive positive-operator interface, one may take
both abstract components \(Z_{0,*}\) and \(Z_{1,*}\) to be this same
even-site trigonometric polynomial. Then (175.H35) is directly the
increment \(\mathcal Q_{4P}^*-\mathcal Q_{2P}^*\), with the energy allowed
by (175.H18). This is an operator countermodel only; it is not asserted to
be the transform of the literal residual symbol.

All \(A_{2s}\) and all link weights are nonnegative, so any stopped chain
containing this top link has full endpoint increment at least \(P^2\).
Choose \(L\) through powers of two, \(M=L^2\), \(P=L^2/4\), and
\(X=L^8\), with \(H=L^2\). For fixed \(0<\varepsilon_0<1/8\),

\[
 {P^2\over L^3X^{\varepsilon_0}}
 \asymp L^{1-8\varepsilon_0}\longrightarrow\infty.
\tag{175.H36}
\]

This falsifies coefficient-uniform scale, Parseval, Haar, endpoint, and
positive-operator proofs. It is not the literal residual symbol and is
not physical lower mass.

At the opposite extreme, a one-site sequence has
\(\mathfrak E_R^{(2)}=D_L\) for every \(R\), hence every link and the
whole chain vanish. Therefore a positive fixed-dual-diagonal contribution
cannot be identified with the zero physical diagonal: on a fixed dual
diagonal the cardinal variables remain independent, and its continuous
product difference need not be an integer. It must cancel against the
remaining dual, cell, endpoint, and zero-extension pieces.

The coherent even-site control is also concentrated at both Fejer peak
centres. At either centred peak the smooth product phase has

\[
 \det\operatorname {Hess}\Phi_\phi
 =-\phi^2-{J\phi\over2\sqrt{uv}},
\tag{175.H37}
\]

which is rank one at \(\phi=0\). Hence a positive rank-one
stationary-phase or fixed-dual-diagonal closure returns to the Round-172
product collar/capacity; it cannot be the missing factor \(L\).

### 3.7 Exact identity / countermodel / restored-power table

| Mechanism | Exact identity or countermodel | Restored power and verdict |
|---|---|---|
| Unweighted whole chain | \(\sum_j\mathcal N_j=\mathcal Q_M^*-\mathcal Q_{R_0}^*\) | \(\mathcal Q_{R_0}^*\ll L^3\); the target is exactly the open literal bound \(\mathcal Q_M^*\ll L^3\). No interior scale resource remains. |
| Physical lag chain | \(\sum_jb_j(r)=w_M(r)-w_{R_0}(r)\ge0\) | There is no scale sign. Cauchy/positivity gives \(MD_L\asymp L^4\), one factor \(L\) above target. |
| Weighted scale Abel | Equation (175.H24) | Positive closure costs \(L^2(|a_{K-1}|M+\cdots)\); constant target weights restore \(ML^2=L^4\). |
| Dyadic Haar/martingale | \(\sum_j\mathfrak H_{R_j}^{(2)}/(2R_j)\le D_L\) | Restoring the unweighted top endpoint multiplies by \(M\), returning \(MD_L=L^4\). |
| First link and short correction | (175.H20), (175.H13) | \(R_0D_L\asymp L^3\); both are target-safe but do not own the complement. |
| Ordinary-zero-containing sector | Collective \(k\)-recombination and (175.H19) | \(L^3X^\varepsilon\); termwise-\(k\) or fixed-diagonal positivity is not licensed. |
| Tangent first difference | Raw count \(RL^2\), commutator factor \(L/R\) | The commutator is \(L^3\); the adjacent-sum remainder restores \(RL^2\), reaching \(L^4\) at \(R=M\), and self-returns to K26. |
| Selected-pair character mass | \(\sum_{a\mid R}\chi(a)(A(a)-A(pqa))\) | Unit amplitudes cancel; literal separated supports and order-one jumps give no proved \(L^{-1}\). A global coefficient-sensitive estimate remains open. |
| Squarefree/coprimality Möbius | Projector identities such as (175.H31) | On surviving squarefree atoms the projector is \(1\); absolute opening adds only \(X^\varepsilon\), not an \(L^{-1}\) gain. |
| Dechirped even-site/rank-one control | \(\mathfrak E_{4P}^{(2)}-\mathfrak E_{2P}^{(2)}=P^2=MD_L/8\) | Sharp \(L^4\) nonliteral capacity. Diagnostic only; no physical lower bound. |
| One-site/fixed-dual-diagonal control | Every physical link is zero | Any isolated positive dual diagonal is missing compensating modes or boundaries. |

## 4. First doubtful or unproved step

There is no doubtful step in the square recombination (175.H15),
stopped-chain telescope (175.H16), physical endpoint formula (175.H21),
weighted summation by parts (175.H24), or Haar normalization (175.H27).
Those identities show that the scale-global proposal has already exhausted
its scale variable.

The first unproved affirmative statement is exactly (175.H5): the literal
maximal Fejer energy of the fully character-recombined, nonzero
ordinary-frequency component must be smaller than its
coefficient-insensitive operator norm by one factor \(L\). In physical
variables the same first open step is (175.H23) with the complete
\(\omega_L\rho_NA_N\) coefficient. In dual variables it is (175.H3) with
all \(k,k',\ell,\ell'\), cells, endpoints, transitions, and zero-extension
pieces kept under the original single real part.

Within the frozen mechanism list, the following coefficient-sensitive
routes remain unexcluded; they are equivalent formulations or possible
inputs to (175.H5), not new scale cancellation resources:

1. a direct signed short-shift correlation theorem for (175.H23), using
   the nonlinear square-root phase and the complete literal coefficient;
2. a maximal-scale positive theorem for \(\mathcal Q_M^*\) proved only
   after establishing literal anti-concentration at both Fejer peaks, in
   a way that fails for the dechirped and rank-one controls;
3. a fully signed nonzero-frequency theorem coupling all odd \(k,k'\), all
   nonzero \(\ell,\ell'\), and all cardinal cells before any positive
   opening;
4. a nonlocal selected/no-pair theorem using (175.H30) jointly across
   \(N,N'\), squarefree/coprimality projectors, character signs, and phase,
   with the all-\(1\pmod4\) no-pair rows included or independently disposed
   of; and
5. an owner-complete strict literal sector together with a proved
   target-safe complement. A one-link, one-shift, one-character-pair,
   one-cell, fixed-dual-diagonal, or smoothed-interior estimate is not such
   a sector.

No exact identity presently supplies the needed literal anti-concentration
or global correlation bound.

## 5. Control tests and outcomes

Here “FAIL” means that the proposed generic mechanism does not meet the
factor-\(L\) gate; it does not mean that K26 is false.

| Required control | Outcome |
|---|---|
| Literal residual coefficient | **PASS.** Equations (175.H1)--(175.H3) leave \(\omega_L,\rho_N,A_N\), both parities, masks, profiles, floors, stars, cells, endpoints, transitions, and zero extension inside the exact \(U\)'s. |
| One-sided whole chain | **PASS.** No absolute value is placed outside the chain. Positivity is used only to audit the available capacity after the exact full-frequency recombination. |
| Parity and transform constants | **PASS.** Both \(\epsilon=0,1\) branches remain; \(i/2\), \(1/8\), and the single outer real part are accounted for in (175.H1) and (175.H15). |
| Strict terminal link | **PASS.** Telescoping and (175.H20) use the actual final \(R<S<2R\); no Haar rounding is made. |
| Once-only short correction | **PASS.** \(B_{\rm short}\) occurs exactly once in (175.H14) and costs \(L^3X^\varepsilon\). |
| Whole chain before modulus | **PASS.** The sums over every signed frequency and cell are completed before recognizing the exact square and summing scales. |
| Ordinary zero sector | **PASS collectively.** Equation (175.H19) is after all odd-character frequencies are recombined. No fixed-\(k\) safety is claimed. |
| Dechirped control | **FAIL for every symbol-blind positive route.** Equations (175.H35)--(175.H36) attain \(L^4\) scale. This coefficient is nonliteral and proves no lower bound for K26. |
| Arbitrary-sign/phase control | **FAIL for coefficient-uniform tangent or positive closure.** The phase-adapted even-site array, and equivalently the Round-173 array \(G_s=(-1)^sg_s\), turns the relevant carrier positive at full capacity. |
| Erased-selector shadow | **FAIL as a saving.** Setting \(\rho_N=1\) leaves the scale, Haar, Abel, and endpoint identities unchanged; no-pair positive-character rows remain. |
| Constant-character shadow | **FAIL as a saving.** Replacing \(\chi_4\) by \(1\) leaves every scale identity unchanged, so scale algebra alone has not used the actual character. |
| Selected-pair unit amplitude | **PASS as an algebraic control, FAIL as a literal estimate.** Ambient character mass cancels, but (175.H30) becomes a widely separated literal difference with no proved smallness. |
| Squarefree Möbius control | **FAIL as a cancellation source on support.** A squarefree one-atom row has only the \(a=1\) term in (175.H31). The identity deletes other rows rather than cancelling the survivor. |
| One-site control | **PASS.** Every physical bandpass and the whole chain are zero. This forbids a surviving isolated positive “diagonal.” |
| Fixed dual diagonal | **FAIL as a physical diagonal.** Its continuous product difference is generally nonintegral; it cancels only in the full dual/cell/endpoint reconstruction. |
| Rank-one peak | **FAIL as a positive saving.** Both peak centres are rank one by (175.H37), and the dechirped coherent control realizes the \(MD_L\) operator scale. |
| Round-172 scope | **PASS.** The audit parks only positivity before a literal-symbol gain. A coefficient-sensitive proof of (175.H5) remains allowed. |
| Round-173 scope | **PASS.** Only the displayed tangent first difference, its adjoint, and a tautological second Abel transfer are parked. A different nonlocal signed theorem remains allowed. |
| Cells, endpoints, transitions | **PASS.** None is smoothed away or estimated separately; all remain inside \(Z_{\epsilon,*}\). |
| Physical versus fixed dual diagonal | **PASS.** Equation (175.H23) has zero physical diagonal, while the one-site test forces full dual compensation. |
| \(L^4\) versus \(L^3\) ledger | **PASS.** \(D_L=L^2\), \(R_0D_L=L^3\), and \(MD_L=L^4\); every proposed restoration is displayed in Section 3.7. |
| Residual-only owner scope | **PASS.** Even (175.H5) would close only K26 and its accepted residual-scalar implication. |
| No in-round pivot | **PASS.** No K17a, other \(t=1\) channel, BAL, UNBAL, M1, GAR, endpoint assembly, M9, bridge, theorem, or exponent lane is used. |

No numerical experiment, symbolic experiment, external source, or physical
lower-bound claim was used.

## 6. Dependencies and exact artifacts used

This report used the assigned task brief and exactly the permitted
mathematical context:

1. protocol.md;
2. state/active_campaign.yml;
3. strategy/round175_m2_hard_top_t1_residual_whole_chain_actual_symbol_strategy.md;
4. proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md;
5. proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md;
6. proofs/kernels/m9_m2_hard_top_t1_residual_tangent_fejer_commutator_self_return_obstruction.md;
7. rounds/codex-managed/m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate/reports/maximal_fejer_transform_endpoint_hostile_audit.md; and
8. rounds/codex-managed/m9-m2-hard-top-t1-residual-tangent-fejer-commutator-gate/reports/tangent_fejer_actual_symbol_hostile_audit.md.

The new deductions are the exact nonzero-frequency endpoint energy
(175.H1)--(175.H5), the weighted scale summation-by-parts identity
(175.H24), the observation that every physical link weight has the same
sign, the normalized Haar restoration (175.H29), and the consolidated
mechanism/countermodel/power audit. No sibling Round-175 report, shared
synthesis, validation matrix, proof draft, source card, or web result was
used.

## 7. Recommended state effect

**Recommended effect: promote, after the conductor's independent seam
review, only the route-scoped whole-chain scale-coboundary/positive-capacity
obstruction; retain K26 and every parent obligation as open.**

The durable obstruction should say:

1. the complete nonzero-frequency stopped chain is exactly
   \(\mathcal Q_M^*-\mathcal Q_{R_0}^*\), with
   \(\mathcal Q_{R_0}^*\ll L^3X^\varepsilon\);
2. constant-weight scale summation has no interior term, every physical
   link coefficient is nonnegative, and weighted Abel or Haar transfer
   restores the maximal factor \(M\);
3. selector balance, squarefree/coprimality Möbius projectors, termwise
   character pairing, fixed dual diagonals, and positive operator bounds
   do not by themselves improve the \(L^4X^\varepsilon\) capacity;
4. the dechirped/rank-one model is only a sharp method-capacity control and
   is not literal physical lower mass; and
5. a new literal coefficient-sensitive theorem for \(\mathcal Q_M^*\), or
   its exact physical or fully signed dual equivalent, remains unexcluded.

Do not promote (175.H5), (175.5), K26, the complete \(t=1\) face, another
hard-TOP channel, hard TOP, BAL, UNBAL, M9--M2, either M1 route, endpoint
uniformity, M9, either bridge, the quarter theorem, or either exponent.
