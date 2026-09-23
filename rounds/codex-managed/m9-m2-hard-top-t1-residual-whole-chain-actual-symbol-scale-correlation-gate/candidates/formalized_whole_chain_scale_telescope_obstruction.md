# Candidate: whole-chain Fejer endpoint-collapse obstruction

- Campaign: m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate
- Round: 175
- Role: conductor-selected candidate
- Starting graph: e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211
- Evidence status: candidate only pending seam review

## 1. Exact setting

Put \(e(t)=e^{2\pi it}\). Let

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor,\qquad
 1\ll L\ll H\le J^{1/2}.
\tag{175.C0}
\]

Put \(R_0=\lceil L\rceil\), and let \(M\asymp L^2\) be the exact
cardinality of the containing interval. Write
\(N=2^{\nu_N}M_N\), where \(\nu_N\in\{0,1\}\) on live squarefree rows
and \(M_N\) is odd. For odd \(d\mid M_N\), define

\[
\begin{aligned}
 \omega_L(N)
 &=\mathbf1_{\mathcal I_L^{\rm lit}}(N)\mu^2(N)
   \left({L^2\over N}\right)^{3/4},\\
 \rho_N(d)
 &=
 \begin{cases}
 1,&\text{if no pair is selected},\\
 1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
 +2\mathbf1_{p_N\mid d}\mathbf1_{q_N\mid d},
 &\text{if }p_N,q_N\text{ are selected},
 \end{cases}\\
 A_N(d)
 &=\mathbf1_{\{\sqrt N\le d\le2\sqrt N\}}^{\rm lit}
   \eta_L(d)\Phi\!\left({d\over H+1}\right)
   W\!\left({\sqrt{q_X}\,d\over2\sqrt N}\right),\\
 \lambda_N(d)&=\omega_L(N)\rho_N(d)A_N(d).
\end{aligned}
\tag{175.C0a}
\]

The symbols in \(A_N\) include the exact coprimality mask,
complementary two-adic profile branch, Vaaler/profile factors, floors,
stars, support crossings, hard endpoints, point values, and
divisor-coordinate zero extension. Every forbidden or outside-literal
incidence has exact value zero. Retain the complete residual sequence

\[
 c_N^{\rm rem}
 =\sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)\lambda_N(d),\qquad
 z_N=c_N^{\rm rem}e(J\sqrt N),\qquad
 D_L=\sum_N|z_N|^2\ll_\varepsilon L^2X^\varepsilon,
\tag{175.C1}
\]

The square root in (175.C1) is evaluated only on positive literal support;
set \(z_N=0\) everywhere else on the full integer line. Define the minimal
stopped chain by

\[
 R_{j+1}=\min(2R_j,M),\qquad R_K=M.
\tag{175.C2}
\]

If \(R_{K-1}<M<2R_{K-1}\), the final link is the actual strict link; if
\(M=2R_{K-1}\), it is the actual final doubling. No endpoint is rounded.
Put

\[
 F_R(\theta)=\sum_{|r|<R}\left(1-{|r|\over R}\right)e(r\theta),
 \qquad B_{R,S}=F_S-F_R.
\tag{175.C2a}
\]

Choose a real
\(\varphi\in C_c^\infty((-1/2,1/2))\), \(\varphi(0)=1\), and define

\[
\begin{aligned}
 \mathcal W_\epsilon(x,y)
 &=\sum_{\substack{d,m\ge1\\d\ {\rm odd}}}
 (-1)^{\epsilon m}\lambda_{dm}(d)
 \varphi(x-d)\varphi(y-m),\\
 \mathcal B_{\epsilon,\theta}(x,y)
 &=\mathcal W_\epsilon(x,y)e(J\sqrt{xy}+\theta xy),\\
 \widetilde{\mathcal B}_{\epsilon,\theta}(\xi,\nu)
 &=\iint_{\mathbb R^2}\mathcal B_{\epsilon,\theta}(x,y)
 e(-\xi x-\nu y)\,dx\,dy,\\
 U_{k,\ell}^{(\epsilon)}(\theta)
 &=\widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell).
\end{aligned}
\tag{175.C2b}
\]

Use the exact cardinal transform

\[
 Z_\epsilon(\theta)
 :=\sum_N(-1)^{\epsilon N}z_Ne(N\theta)
 ={i\over2}\sum_{k\ {\rm odd}}\chi_4(k)
 \sum_{\ell\in\mathbb Z}U_{k,\ell}^{(\epsilon)}(\theta)
 =Z_{\epsilon,0}(\theta)+Z_{\epsilon,*}(\theta),
\tag{175.C3}
\]

where

\[
\begin{aligned}
 Z_{\epsilon,0}(\theta)
 &={i\over2}\sum_{k\ {\rm odd}}\chi_4(k)
 U_{k,0}^{(\epsilon)}(\theta),\\
 Z_{\epsilon,*}(\theta)
 &={i\over2}\sum_{k\ {\rm odd}}\chi_4(k)
 \sum_{\ell\ne0}U_{k,\ell}^{(\epsilon)}(\theta).
\end{aligned}
\tag{175.C4}
\]

Both absolute-parity branches and every odd character frequency are retained.
The compact smooth interpolation makes the displayed dual sums absolutely
convergent for fixed data. Since \(d\) is odd,
\((-1)^{\epsilon N}=(-1)^{\epsilon m}\). The live even-gap physical
ledger contains the odd--odd and squarefree even--even branches; the latter
has \(4\mid r\), and there is no mixed branch.

## 2. Endpoint collapse

For every positive integer \(R\), define the nonzero-ordinary-frequency
Fejer energy

\[
 Q_R^*
 ={1\over2}\sum_{\epsilon=0}^1
 \int_0^1F_R(\theta)|Z_{\epsilon,*}(\theta)|^2\,d\theta.
\tag{175.C5}
\]

Since \(F_R\ge0\), one has \(Q_R^*\ge0\). Exact expansion of (175.C4)
gives, with \(|i/2|^2=1/4\), parity average \(1/2\), total factor \(1/8\),
and one outer real part,

\[
 \boxed{\mathcal N_{R,S}=Q_S^*-Q_R^*.}
\tag{175.C6}
\]

Therefore the complete unweighted stopped chain satisfies

\[
 \boxed{
 \sum_{j=0}^{K-1}\mathcal N_{R_j,R_{j+1}}
 =Q_M^*-Q_{R_0}^*
 ={1\over2}\sum_{\epsilon=0}^1\int_0^1
 (F_M-F_{R_0})|Z_{\epsilon,*}|^2.}
\tag{175.C7}
\]

This identity is coefficient-independent and occurs before any modulus.
The intermediate scale index disappears completely. Section 4 proves that
the lower endpoint is already target-safe, so the missing factor belongs
entirely to the still-open literal maximal energy \(Q_M^*\); it is not an
additional cross-link martingale variable.

More generally, for arbitrary scalars \(a_0,\ldots,a_{K-1}\), finite
summation by parts gives

\[
\boxed{
\sum_{j=0}^{K-1}a_j\mathcal N_{R_j,R_{j+1}}
=a_{K-1}Q_M^*-a_0Q_{R_0}^*
 +\sum_{j=1}^{K-1}(a_{j-1}-a_j)Q_{R_j}^*.}
\tag{175.C8}
\]

The target corresponds to \(a_j=1\). A nonconstant scalar martingale or
scale weighting changes the target and introduces intermediate positive
energies. Restoring the unweighted target sets all coefficients to one and
returns (175.C7).

At an exact doubling, put

\[
 \mathcal H_R^*
 ={1\over2}\sum_{\epsilon=0}^1\int_0^1
 (2F_R-F_{2R})|Z_{\epsilon,*}|^2\,d\theta\ge0.
\tag{175.C8a}
\]

Then

\[
 Q_{2R}^*=2Q_R^*-\mathcal H_R^*,\qquad
 {Q_{2R}^*\over2R}
 ={Q_R^*\over R}-{\mathcal H_R^*\over2R}.
\tag{175.C8b}
\]

The genuine Haar decrease is normalized by \(1/R\). Multiplying it back
to the unweighted endpoint restores the top scale \(M\); a possible strict
terminal link uses its exact Fejer difference rather than (175.C8b).

## 3. Physical frequency and owner-complete restoration

Write \(f_R(r)=(1-|r|/R)_+\). For every fixed nonzero integer physical gap,

\[
 b_{R,S}(r)=f_S(r)-f_R(r)\ge0,
\tag{175.C9}
\]

and

\[
\sum_{j=0}^{K-1}b_{R_j,R_{j+1}}(r)
=f_M(r)-f_{R_0}(r)
=
\begin{cases}
 |r|(R_0^{-1}-M^{-1}),&0<|r|<R_0,\\
 1-|r|/M,&R_0\le |r|<M,\\
 0,&r=0\ {\rm or}\ |r|\ge M.
\end{cases}
\tag{175.C10}
\]

Thus the physical link weights have no alternating scale sign. Equation
(175.C10) concerns physical integer gaps. For a fixed transformed tuple
\((k,k',\ell,\ell')\), the valid assertion is only the endpoint telescope
obtained by summing \(B_{R,S}=F_S-F_R\); it is not a physical-gap diagonal
and cannot be deleted.

Let

\[
 \mathfrak E_R^{(2)}
 ={1\over2}\sum_{\epsilon=0}^1
 \int_0^1F_R(\theta)|Z_\epsilon(\theta)|^2\,d\theta
\tag{175.C11}
\]

and define the complete transformed sector containing at least one ordinary
zero frequency, counted once after full odd-character recombination, by

\[
 \mathcal Z_{R,S}
 ={1\over2}\sum_{\epsilon=0}^1\int_0^1B_{R,S}
 \left\{|Z_{\epsilon,0}|^2+
 2\Re(Z_{\epsilon,0}\overline{Z_{\epsilon,*}})\right\}\,d\theta.
\tag{175.C11a}
\]

Then

\[
 \mathfrak E_S^{(2)}-\mathfrak E_R^{(2)}
 =\mathcal N_{R,S}+\mathcal Z_{R,S}.
\tag{175.C12}
\]

Linearity and the reverse character estimate give at the single endpoint

\[
\sum_j\mathcal Z_{R_j,R_{j+1}}
=\mathcal Z_{R_0,M},\qquad
|\mathcal Z_{R_0,M}|
\ll (M+R_0)\left(
D_L^{1/2}{L^2\over J}+{L^4\over J^2}\right)X^{O(\eta)}
\ll_\varepsilon L^3X^\varepsilon.
\tag{175.C13}
\]

Indeed
\(\sup_{\epsilon,\theta}|Z_{\epsilon,0}|
\ll_\eta L^2J^{-1}X^\eta\),
\(\|Z_\epsilon\|_2=D_L^{1/2}\), \(M\asymp L^2\), and \(L^2\le J\).
For

\[
 A_r=\Re\sum_Nz_{N+r}\overline{z_N},
\tag{175.C13a}
\]

the physical parity energy is

\[
 \mathfrak E_R^{(2)}
 =D_L+2\sum_{\substack{0<r<R\\2\mid r}}
 \left(1-{r\over R}\right)A_r.
\tag{175.C13aa}
\]

define the exact medium/long K26 scalar and once-only short correction by

\[
\begin{aligned}
 T_{26}
 &=\sum_{\substack{R_0\le r<M\\2\mid r}}
 \left(1-{r\over M}\right)A_r,\\
 B_{\rm short}
 &=\sum_{\substack{0<r<R_0\\2\mid r}}
 r\left({1\over R_0}-{1\over M}\right)A_r.
\end{aligned}
\tag{175.C13b}
\]

Here \(T_{26}\) is exactly the left side of (165.K26). The parity-Fejer
identity gives

\[
 T_{26}
 ={1\over2}\{\mathfrak E_M^{(2)}
             -\mathfrak E_{R_0}^{(2)}\}
 -B_{\rm short},
\qquad
 |B_{\rm short}|\ll_\varepsilon L^3X^\varepsilon.
\tag{175.C14}
\]

Consequently,

\[
\boxed{
\sum_{j=0}^{K-1}\mathcal N_{R_j,R_{j+1}}
=2(T_{26}+B_{\rm short})-\mathcal Z_{R_0,M}.}
\tag{175.C15}
\]

The Round-175 target and K26 are therefore equivalent one-sided upper bounds
at target strength. Equation (175.C15) proves no estimate; it shows that the
proposed whole-scale resource self-returns to the original endpoint owner.

## 4. Restored capacity

Since \(Z_{\epsilon,*}=Z_\epsilon-Z_{\epsilon,0}\), (175.C1) and the
zero-mode estimate imply

\[
 \sum_{\epsilon=0}^1\|Z_{\epsilon,*}\|_2^2
 \ll_\varepsilon L^2X^\varepsilon.
\tag{175.C16}
\]

Fejer positivity then supplies only

\[
0\le Q_R^*\ll_\varepsilon RL^2X^\varepsilon,
\qquad
Q_M^*\ll_\varepsilon L^4X^\varepsilon.
\tag{175.C17}
\]

In particular,

\[
 0\le Q_{R_0}^*
 \le {R_0\over2}\sum_{\epsilon=0}^1
 \|Z_{\epsilon,*}\|_2^2
 \ll_\varepsilon L^3X^\varepsilon.
\tag{175.C17a}
\]

Therefore the deliberately one-sided target satisfies the exact
target-strength equivalence

\[
\boxed{
Q_M^*-Q_{R_0}^*\ll_\varepsilon L^3X^\varepsilon
\quad\Longleftrightarrow\quad
Q_M^*\ll_\varepsilon L^3X^\varepsilon.}
\tag{175.C17b}
\]

The forward implication adds the target-safe lower endpoint, and the reverse
implication uses \(Q_{R_0}^*\ge0\). Thus no \(L^4\) maximal contribution can
be cancelled by the lower endpoint. Applying coefficient-independent
positivity to (175.C7), (175.C8), or (175.C8b) still restores the missing
factor \(L\).

This coefficient-insensitive physical scale is sharp. Let \(n\ge3\),
\(L=2n\), \(P=n^2\), and \(M=4P=L^2\). On a positive translate of an
\(M\)-site interval, put \(z_N=1\) on the \(2P\) even sites and zero
elsewhere. Then \(D=2P\) and

\[
 \mathfrak E_M^{(2)}
 =2P+{1\over P}\sum_{t=1}^{2P-1}t^2
 ={8P^2+1\over3}.
\tag{175.C18}
\]

Since
\(\mathfrak E_{R_0}^{(2)}\le R_0D=4n^3\),

\[
 \mathfrak E_M^{(2)}-\mathfrak E_{R_0}^{(2)}
 \ge {L^4\over12}.
\tag{175.C19}
\]

Taking \(X=L^8\), \(J=L^4\), and \(H=L^2=J^{1/2}\) makes the parameter
range admissible and, for each fixed \(0<\varepsilon_0<1/8\),

\[
 {\mathfrak E_M^{(2)}-\mathfrak E_{R_0}^{(2)}
  \over L^3X^{\varepsilon_0}}
 \ge {1\over12}L^{1-8\varepsilon_0}\longrightarrow\infty.
\tag{175.C20}
\]

The phase-dechirped array realizing this control is not the literal residual
coefficient. Equations (175.C18)--(175.C20) diagnose the complete physical
parity-Fejer energy, not an \(L^4\) lower bound for the literal \(Q_M^*\)
sector or for K26. At the abstract positive-operator interface one may take

\[
 Z_{0,*}(\theta)=Z_{1,*}(\theta)
 =\sum_{u=0}^{2P-1}e(2u\theta),
\tag{175.C20a}
\]

for which
\(Q_{4P}^*-Q_{2P}^*=P^2=MD/8\).
This abstract \(Z_*\) need not be a literal cardinal image. The controls
only rule out a coefficient-uniform inference from support, energy, parity,
Fejer positivity, rank-one centred peaks, or scale geometry.

## 5. Literal-symbol audit

The complete incidence weight is

\[
 \lambda_N(d)=\omega_L(N)\rho_N(d)A_N(d).
\tag{175.C21}
\]

Each displayed factor is independent of the scale index. The available
pointwise algebra gives no automatic \(L^{-1}\):

1. The exact \(\omega_L\) and the two exact cases of \(\rho_N\) are
   displayed in (175.C0a). The selector is the Boolean complement of XOR,
   with values \(1,0,0,1\), not a signed weight.
   The factor \(\omega_L(N)\) contains a nonnegative squarefree and shell
   projector.
   A Mobius opening either recombines to the live projector or to the literal
   zero.
2. If an opposite-character pair \(p_N,q_N\) is selected on a live
   squarefree row, write
   \(M_N=p_Nq_NR_N\), with \(p_N,q_N\nmid R_N\) and
   \(\chi_4(p_Nq_N)=-1\). The residual neither/both divisor pairing is

   \[
   c_N^{\rm rem}
   =\omega_L(N)\sum_{a\mid R_N}\chi_4(a)
   \{A_N(a)-A_N(p_Nq_Na)\}.
   \tag{175.C22}
   \]

   Since \(p_Nq_N\ge15\), the paired literal near-square supports are
   disjoint, and exactly

   \[
   |A_N(a)-A_N(p_Nq_Na)|
   =|A_N(a)|+|A_N(p_Nq_Na)|.
   \tag{175.C22a}
   \]

   In the unit-profile diagnostic the disjoint pair has a full boundary
   difference. For the actual profile, disjointness prevents pointwise
   cancellation but supplies no lower bound on the surviving value and no
   physical lower mass.
3. On a no-pair row whose odd prime factors are all \(1\bmod4\),
   every surviving divisor character is \(+1\). This is an allowed-support
   warning, not a density theorem or a literal lower bound.
4. The full zero-extended profile has total variation \(O(1)\), including
   hard births, deaths, point values, and endpoint jumps. Divisor Abel
   summation therefore supplies no \(O(L^{-1})\) factor.

These facts rule out only an algebraic gain from the listed row identities.
They do not exclude cancellation jointly across different products, gaps,
characters, cells, or the square-root phase.

## 6. Controls and exact scope

- Both parity branches, \(i/2\), \(1/8\), one outer real part, all odd
  character frequencies, and all nonzero ordinary frequencies remain in
  (175.C3)--(175.C7).
- The possible strict terminal link, all cells, openings, hard endpoints,
  transitions, point values, support births/deaths, and zero-extension
  pieces are retained.
- The ordinary-zero sector is restored only in the collective form
  (175.C13), and the short correction is paid once in (175.C14).
- The physical zero diagonal in (175.C10) does not delete a transformed
  diagonal.
- A one-site physical array has every Fejer endpoint difference equal to
  zero; any isolated positive transformed contribution is missing its
  compensating assembly.
- The telescope survives arbitrary coefficients, dechirping, constant
  character, and the erased-selector shadow. It therefore has not used the
  required literal symbol.
- The abstract coherent control (175.C20a) sits at both centred Fejer peaks.
  The inherited product-phase Hessian is rank one there, so positive
  centred-peak closure has the same \(L^4\) method capacity. This is not a
  literal lower bound.
- The Round-173 tangent first-difference family is not used.

The no-go covers:

1. cross-link cancellation treated as an independent scale variable;
2. coefficient-independent scalar scale Abel, Haar, martingale, or positive
   closure before an actual-symbol gain; and
3. an automatic factor \(L\) from squarefree projection, selected-row unit
   mass, no-pair character, or profile BV alone.

It does not cover:

1. a direct signed endpoint theorem for the complete literal form in
   (175.C15);
2. a selector-stable joint product/gap/character transform;
3. a coefficient-sensitive positive theorem proved before scale positivity;
4. cancellation involving all products, gaps, cells, endpoints, and
   ordinary frequencies simultaneously; or
5. K26 itself.

## 7. State boundary

The smallest durable conclusion is a route-scoped obstruction:
the unweighted whole stopped chain is exactly one endpoint difference, and
coefficient-independent scale manipulations do not create the missing factor
\(L\). The lower endpoint is target-safe, so the first open theorem is
precisely the literal positive maximal-energy estimate
\(Q_M^*\ll_\varepsilon L^3X^\varepsilon\), equivalently the complete
literal signed endpoint estimate modulo the target-safe seams.

This candidate has no implication edge. It proves neither K26 nor the
complete residual scalar, full \(t=1\), another hard-TOP channel, hard TOP,
either BAL scope, UNBAL, M9--M2, either M1 route, endpoint uniformity, M9,
a bridge, the quarter theorem, or an exponent.
