# Round 90 discovery report: M1 square-root self-return barrier

Campaign: `m9-m1-capacity-self-return-fork`
Task: `m1_self_return_barrier_attack`
Role: discovery
Starting graph SHA-256: `bd5eed1e732c8872b37c0ea51bc9cea65419fe3241c17a981df3c2a36cd2c0f1`

## 1. Result

**Square-root equal-capacity self-return is proved for the complete
R82--R89 reassembly.**  More precisely, the late four-row object is the
exact Fejer Gram lift of the deep part of the Round-82 coherent
nonzero-offset operator.  All CRT cells, descended frequencies,
transposes, signs, and prior owners reassemble once to that Gram lift.
The only non-identity arrow is the accepted Fejer/Cauchy passage from a
linear deep block to its Gram lift; its normalization is proved below to
be

\[
 |\mathfrak Y_D|^2\ll {B\over D}\,\mathcal E_D.       \tag{1.1}
\]

Put

\[
 \mathsf{C}_{82}=B^3T^2Q^{-5/12},\qquad
 \mathsf{T}_{82}={J^2\over T}=J^{7/5}.                 \tag{1.2}
\]

For a full-degree late graph, \(\Delta\asymp M^2\asymp
B^2\), the capacity and target of its Gram lift are literally

\[
 \mathsf{C}_{\mathrm{deep}}
 =DB^5T^4Q^{-5/6}
 ={D\over B}\mathsf{C}_{82}^{2},\qquad
 \mathsf{T}_{\mathrm{deep}}
 ={D\over B}J^{14/5}
 ={D\over B}\mathsf{T}_{82}^{2}.                       \tag{1.3}
\]

Consequently

\[
 \sqrt{B/D}\,\mathsf{C}_{\mathrm{deep}}^{1/2}=\mathsf{C}_{82},
 \qquad
 \sqrt{B/D}\,\mathsf{T}_{\mathrm{deep}}^{1/2}=\mathsf{T}_{82}.
                                                               \tag{1.4}
\]

Thus the late deficit is the square, not an additional loss:

\[
 \Gamma_{\mathrm{deep}}
 =B^6J^{-11/15}
 =\bigl(B^3J^{-11/30}\bigr)^2
 =\Gamma_{82}^{2}.                                     \tag{1.5}
\]

At \(B=J^{3/20}\), these are respectively \(J^{1/6}\) and
\(J^{1/12}\), and (1.1) takes the correct square root.  The exact
\(q=8\) residual fibre has degree \(\gg X^{-\varepsilon}B^2\), so the
strict survivor still has this worst graph capacity.  This is not a
lower bound for the signed sum; it proves that no R87--R89
classification, descent, completion, or inverse transform supplies a
strict power gain.  There is therefore no proved first non-returning
signed degree of freedom.  The canonical obstruction is the
high-degree deep actual-symbol operator displayed in Section 4.

The word *self-return* here is exact at the complete-cell Gram-operator
level and exact at the capacity level after (1.1).  A linear operator is
not algebraically equal to its Gram square; no such false inverse-square
identity is asserted.

## 2. Exact statement and hypotheses

Let

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
 B=C/T,
\]

with

\[
 J^{13/18}<C\leq J^{3/4},\qquad M\asymp B.             \tag{2.1}
\]

Fix one transition-flattened smooth nonaxial principal component, one
of the three classes

\[
 (g,M,K)=(1,4b,k),\quad(2,2b,2[k\bar4]_b),\quad
 (4,b,[k\bar4]_b),                                    \tag{2.2}
\]

one alias, either sign, and either reflected orientation.  The finite
number of such choices is absorbed by \(X^\varepsilon\).  Put

\[
 \mathcal R_{b,x}(\theta)
 ={1\over M}\sum_n I_b(n)e_M(nx)e(n\theta),\qquad
 \|\mathcal R_{b,x}\|_\infty
 \ll_\varepsilon X^\varepsilon TQ^{-5/24}.            \tag{2.3}
\]

For an ordered physical pair \(P=(x,y)\), \(x\ne y\), define

\[
 F_{b,P}(\theta)=e_M\!\left(K(\bar x-\bar y)\right)
 \mathcal R_{b,x}(\theta)\overline{\mathcal R_{b,y}(\theta)}.
                                                               \tag{2.4}
\]

Let \(\Pi_{b,D}\) be the accepted signed deep multiplier, including
zero-extension off the actual stationary support, and set

\[
 f_{b,P}=\Pi_{b,D}F_{b,P},\qquad
 H_{b,D}=\sum_{P:x\ne y}f_{b,P}.                       \tag{2.5}
\]

The exact reassembly statement has two levels.  On the linear level,
with the Round-82 same-residue term already outside
\(\mathfrak X_{82}\),

\[
 \boxed{
 \mathfrak X_{82}
 =\mathfrak O_{83:86}
  +\sum_D\sum_{b\asymp B}H_{b,D}(0).}                 \tag{2.6}
\]

Here \(\mathfrak O_{83:86}\) is the one-count sum of the literal
dual difference \(d=0\), all \(0<|d|\leq D_1\), the outer support
collar, and the accepted entry/exit, wrong-sign, stationary, and
nonstationary errors.  The sum in (2.6) is a finite dyadic partition of

\[
 D_1<|d|<\Delta_b-J^{3/4}.                             \tag{2.7}
\]

On the Gram level put

\[
 \mathcal E_D
 =\sum_{b\asymp B}\int_{\mathbb T}|D_D(\theta)|^2
             |H_{b,D}(\theta)|^2\,d\theta             \tag{2.8}
\]

and

\[
 \mathcal K_D^\circ=|D_D|^2-D,\qquad
 \mathcal E_D=\mathcal E_{D,u=0}+\mathcal E_D^\circ.  \tag{2.9}
\]

There is an exact, one-count identity

\[
 \boxed{
 \mathcal E_D^\circ
 =\mathcal E_{87}
  +\mathcal E_{88,\mathrm{coarse}}
  +\mathcal E_{88,\mathrm{good}}
  +\mathcal E_{89,\mathrm{safe}}
  +\mathcal E_{\mathrm{hard}}.}                       \tag{2.10}
\]

The terms are intersected successively with the complements of earlier
owners.  Thus (2.10), together with the single global owner
\(\mathcal E_{D,u=0}\), is a partition, not an overlapping upper
bound.  The last term has

\[
 R_*>\rho_*,\qquad
 \mathfrak a<M^2/\rho_*^2,\qquad
 \rho_*=\min\!\left(M,\lfloor J^{11/30}B^{-2}\rfloor\right), \tag{2.11}
\]

and contains precisely the remaining bad-prime cells, the full
nonunit union, affine/full-phase and projection-only periods, shallow
good-prime lifts, and aperiodic factors.  Equations (1.1)--(1.5) and
(2.6)--(2.10) are the claimed self-return/barrier theorem.

## 3. Proof or derivation

**Linear reassembly.**  Summing (2.4) over all ordered pairs gives the
centered Kloosterman product coefficient because

\[
 \sum_{x\ne y}^{*}
 e_M\!\left(dx+n(x-y)+K(\bar x-\bar y)\right)
 =S(n+d,K;M)\overline{S(n,K;M)}-c_M(d).                \tag{3.1}
\]

Indeed the unrestricted double sum is the Kloosterman product, while
the omitted diagonal \(x=y\) is exactly \(\sum_x^*e_M(dx)=c_M(d)\).
Using the two \(M^{-1}\) factors already present in the ordered pair, (3.1)
and Fourier inversion give

\[
 \widehat H_{b,D}(d)
 =\Pi_{b,D}(d){1\over M^2}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.                            \tag{3.2}
\]

Consequently \(H_{b,D}(0)=\sum_d\widehat H_{b,D}(d)\).
The exact \(d=0\), small-difference, collar, and error owners, followed
by the deep dyadic partition, prove (2.6).  No fixed nonzero residue
offset is summed as a separate owner: only the same-residue mode is
removed before \(\mathfrak X_{82}\), and all coherent nonzero offsets
are present in (3.1).

**The Fejer/Cauchy normalization.**  For a coefficient vector
\(a=(a_1,\ldots,a_D)\), let

\[
 T_D(i,j)=D-|i-j|.
\]

Then

\[
 a^*T_Da=\int_{\mathbb T}|D_D(\theta)|^2
 \left|\sum_{j=1}^Da_je(j\theta)\right|^2d\theta.      \tag{3.3}
\]

Moreover

\[
 T_D(e_1+e_D)=(D+1){\bf1},\qquad
 (e_1+e_D)^*T_D(e_1+e_D)=2(D+1).
\]

Cauchy--Schwarz in the positive \(T_D\)-inner product therefore gives

\[
 \left|\sum_{j=1}^Da_j\right|^2
 \leq {2\over D+1}a^*T_Da
 \leq {2\over D}a^*T_Da.                              \tag{3.4}
\]

Padding by zero, separating the two signs, and applying the fixed
smooth dyadic partition changes only an absolute or
\(X^\varepsilon\) factor.  Applying (3.4) for each \(b\), then Cauchy
over the \(O(B)\) moduli, proves

\[
 \left|\sum_{b\asymp B}H_{b,D}(0)\right|^2
 \ll_\varepsilon X^\varepsilon {B\over D}\mathcal E_D, \tag{3.5}
\]

which is (1.1).  Thus the required energy target is necessarily
\((D/B)\mathsf{T}_{82}^2=(D/B)J^{14/5}\), rather than an unrelated
late target.

**Exact Gram expansion and completion.**  From (2.8)--(2.9),

\[
 \mathcal E_D^\circ
 =\sum_{b}\sum_{0<|u|<D}(D-|u|)
   \sum_d\widehat H_{b,D}(d+u)
          \overline{\widehat H_{b,D}(d)}.              \tag{3.6}
\]

Expand both copies of \(H\).  The change of variables

\[
 P=(x,x-A),\qquad P'=(x-V,x-V-B_2)                    \tag{3.7}
\]

is bijective on complete physical edge fibres.  Summing the base point
\(x\), without cutting its mask, gives exactly

\[
 {1\over M^5}\sum_{n,m}
 \Omega_{b,d,u}(n,m)e_M(dV+nA-mB_2)
 \mathfrak T_M(u,A,B_2,V),                            \tag{3.8}
\]

where

\[
 \Omega_{b,d,u}(n,m)=
 I_b(n+d+u)\overline{I_b(n)}
 \overline{I_b(m+d)}I_b(m).                           \tag{3.9}
\]

There is no missing \(M^{-2}\): the shifted product of two ordered-pair
coefficients is \(M^{-4}\), while
\(M^{-5}\mathfrak T_M=M^{-4}\sum_x\).  Equations
(3.6)--(3.9) prove that the complete late tensor is the literal Gram
expansion of the deep operator with its moving symbol.

**Cell ownership, descent, and inverse transform.**  Round 87 first
partitions complete physical edges into same-group and cross-group
edges.  On the cross-group complement, Round 88 partitions by exact
coarse shell and full-prime-power masked-depth vector.  On its
complement, Round 89 freezes complete reduction-cell tensors and leaves
their complement as \(\mathcal E_{\mathrm{hard}}\).  Empty masks are zero.
This proves the disjoint identity (2.10).

CRT is over full factors \(q=p^\nu\Vert M\), and

\[
 \mathfrak T_M(u,A,B_2,V)=\prod_{q\Vert M}\mathfrak T_q(c_qu). \tag{3.10}
\]

If a nonzero local masked weight has depth \(j\), then

\[
 \mathfrak T_q(u)=0\ (p^j\nmid u),\qquad
 \mathfrak T_q(p^ju')=p^{2j}\mathfrak T_{q'}^\downarrow(u'),
 \quad q'=q/p^j.                                      \tag{3.11}
\]

This descent is exactly invertible.  With
\(\mathfrak T_q(u)=q\sum_xw_q(x)e_q(ux)\),

\[
 {1\over q^2}\sum_{u\bmod q}\mathfrak T_q(u)e_q(-ux)
 ={1\over q'^2}\sum_{u'\bmod q'}
 \mathfrak T_{q'}^\downarrow(u')e_{q'}(-u'x)
 =w_q(x).                                              \tag{3.12}
\]

The equality uses \(q^2=p^{2j}q'^2\); it is exactly why the
\(p^{2j}\) factor cancels the apparent sparse-frequency gain.  For the
integer Fejer sum, grouping all representatives \(u=r+kM\) before
(3.12) preserves their actual weights, including every nonzero modulus
multiple.  Equivalently, the identity

\[
 \sum_{\substack{|u|<D\\L\mid u}}(D-|u|)e(u\theta)
 =L\,|D_{D/L}(L\theta)|^2                              \tag{3.13}
\]

when \(L\mid D\), with the two adjacent quotient lengths otherwise,
shows unchanged Fejer mass.  Thus completed descent followed by inverse
completion returns (3.6), not a smaller norm.

Swapping \(P,P'\) translates and conjugates the local masked phase and
preserves the depth; it supplies the transposed edge and the opposite
\(u\)-sign.  The original all-class residue completion is also exact:

\[
 \sum_{a\ne0}\mathcal C_{M,K}(d,a)e_M(an)
 =S(n+d,K;M)\overline{S(n,K;M)}-c_M(d).                \tag{3.14}
\]

Hence inverse completion of (3.8), summation of all cells, restoration
of the single \(u=0\) owner, (3.2), and then (3.14) give the following
exact transformation diagram.  Double arrows are identities; the sole
one-way arrow is the proved upper-bound implication (3.5).

\[
\begin{array}{c}
 \mathfrak X_{82}
 \quad\Longleftrightarrow\quad
 \mathfrak O_{83:86}+\displaystyle\sum_D\sum_bH_{b,D}(0)
 \\
 \displaystyle\downarrow\quad
 |\sum_bH_{b,D}(0)|^2\ll (B/D)\mathcal E_D
 \\
 \mathcal E_{D,u=0}+\mathcal E_D^\circ
 \quad\Longleftrightarrow\quad
 \mathcal E_{D,u=0}+\mathcal E_{87}+\mathcal E_{88}
 +\mathcal E_{89}+\mathcal E_{\mathrm{hard}}
 \\
 \quad\Longleftrightarrow\quad
 \displaystyle\sum_{\text{complete cells}}
 {\Omega_{b,d,u}(n,m)\over M^5}
 e_M(dV+nA-mB_2)\mathfrak T_M(u,A,B_2,V)
 \\
 \quad\Longleftrightarrow\quad
 \text{full-prime-power CRT/descent/inverse completion}
 \quad\Longleftrightarrow\quad
 \mathcal E_D.
\end{array}                                             \tag{3.15}
\]

At coefficient level, (3.15) must not be shortened to a direct equality
between \(\mathfrak X_{82}\) and the fourfold cell sum.  The former is
quadratic in \(I_b\), whereas (3.8) is quartic.  The exact all-cell and
all-frequency inverse identity is (2.10) for \(\mathcal E_D\); the exact
linear inverse identity is (2.6) for \(\mathfrak X_{82}\); and their
precise interface is the Fejer inequality (3.5).  Thus the putative
direct inverse-Gram coefficient is not merely unproved: it is the wrong
homogeneity.  The square-root capacity return (1.3)--(1.4) is the
lawful replacement.

Finally, (2.3) supplies \(Q^{-5/24}\) per row,
\(Q^{-5/12}\) per ordered pair, and \(Q^{-5/6}\) per four-row Gram
term.  With \(\Delta=B^2\), inserting these factors into (3.5) gives
(1.3)--(1.5), completing the proof.

## 4. First doubtful or unproved step

The first unproved inequality is a signed estimate for the exact hard
term in (2.10):

\[
\begin{aligned}
 \mathcal E_{\mathrm{hard}}(D)
 ={}&\sum_{b\asymp B}
 \sum_{\substack{R_*>\rho_*,\ \mathfrak a<M^2/\rho_*^2\\
                   \sigma\ \mathrm{not\ previously\ owned}}}
 \sum_{0<|u|<D}(D-|u|)
 \sum_{d,n,m}^{\mathrm{deep}}
 {\Omega_{b,d,u}(n,m)\over M^5}                         \\
 &\hspace{25mm}\times
 e_M(dV+nA-mB_2)\mathfrak T_M(u,A,B_2,V)
 \stackrel{?}{\ll}_\varepsilon
 X^\varepsilon{D\over B}J^{14/5}.                     \tag{4.1}
\end{aligned}
\]

Here “not previously owned” includes residual bad-prime cells failing
the Round-89 reciprocal-conductor threshold, the full nonunit union,
affine/full-phase and projection-only periods, shallow good-prime lifts,
and aperiodic factors.  Both signs, all nonzero modulus multiples, the
centered Ramanujan cross and square terms, and the actual support in all
four \(I_b\)'s remain in (4.1).

The \(q=8\), \(A=B_2=V=2\) fibre has exact period two,
\(|\mathfrak T_8(4)|=32\), is strict cross-group after generic CRT
tensoring, and has both degrees \(\gg X^{-\varepsilon}M^2\).  It proves
that (4.1) cannot acquire a strict capacity power from local period
depth or graph sparsity.  It does not prove that (4.1) is large, because
the signed moving symbol can still cancel jointly across
\((b,d,u,n,m,A,B_2,V)\).

Thus the first *analytic* missing input is a joint actual-symbol theorem
for (4.1).  There is no missing coefficient in the exact reassembly
(2.6), (2.10), or (3.15), and there is no proved residual satisfying
\(\Gamma=o(J^{1/6})\) at the top.  Conversely, (3.5) is an inequality,
not an algebraic inverse of the Gram square.  Demanding a linear inverse
of squaring would be ill-posed; the relevant and now certified statement
is the equal-capacity upper-bound return (1.3)--(1.4).

## 5. Control tests and outcomes

Write

\[
 g=\Gamma_{82}=B^3J^{-11/30},\qquad
 G=\Gamma_{\mathrm{deep}}=B^6J^{-11/15}=g^2,           \tag{5.1}
\]

and, for a late edge package of maximum directed degree \(\Delta\),

\[
 \gamma(\Delta)=\Delta B^4J^{-11/15}
 =G{\Delta\over B^2}.                                 \tag{5.2}
\]

The exact historical capacity ledger is as follows.  “Removed” records
the largest normalized power of the newly owned complete package; it is
not an assertion that individually safe fixed layers may be summed with
triangle inequality.

| round | normalization | \(\Gamma_{\mathrm{before}}\) | newly removed/owned power | \(\Gamma_{\mathrm{survivor}}\) | exact effect |
|---|---:|---:|---:|---:|---|
| R82 | linear target \(J^{7/5}\) | \(g\) | same residue, and any one fixed offset layer: \(g/B=B^2J^{-11/30}\) | \(g\) | Coherent union of all nonzero offsets remains. |
| R83 | linear | \(g\) | literal \(d=0\): \(B^2J^{-4/5}=(C/J)^2\) | \(g\) | All-class completion is exact; nonzero \(d\equiv0\pmod M\) remains. |
| R84 | linear | \(g\) | \(0<|d|\le J^{17/30}\): \(\le1\) | \(g\) | Stationary second derivative removes the complete small range. |
| R85 | linear | \(g\) | outer collar main: \(J^{-1/10}\); aggregate errors: \(J^{-1/4}\) | \(g\) | Zero-extension preserves the exact interior. |
| R86 | linear | \(g\) | \(J^{17/30}<|d|\le J^{87/140}\): \(\le1\) (other top powers \(J^{-23/280},J^{-37/70}\)) | \(g\) | The remaining interval still has length \(\asymp Q^2\). |
| R87 | Gram target \((D/B)J^{14/5}\) | \(G\) | same-group package: \(G/B^2=B^4J^{-11/15}\); global \(u=0\) retained once | \(G\) | Complete cross-group graph can still have \(\Delta\asymp B^2\). |
| R88 | Gram | \(G\) | coarse and qualifying good-prime union: \(\gamma(\rho_*^2)=\rho_*^2B^4J^{-11/15}\le1\) | \(G\) | Descent support and \(p^{2j}\) inflation cancel exactly. |
| R89 | Gram | \(G\) | safe complete cells/unions: \(\gamma(\Delta_\Sigma)\le\gamma(\rho_*^2)\le1\) | \(G\) | The \(q=8\) residual retains \(\Delta\gg X^{-\varepsilon}B^2\). |

At \(B=J^{3/20}\),

\[
 g=J^{1/12},\qquad G=J^{1/6},\qquad
 \rho_*=J^{1/15},\qquad \gamma(\rho_*^2)=1.           \tag{5.3}
\]

The row/pair/Gram normalization, with no duplication, is:

| object | explicit \(M\)-normalization | physical \(Q\)-power |
|---|---:|---:|
| one row \(\mathcal R_{b,x}\) | \(M^{-1}\) | \(Q^{-5/24}\) |
| one ordered-pair coefficient | \(M^{-2}\) | \(Q^{-5/12}\) |
| shifted product of two pairs | \(M^{-4}=M^{-5}(M\sum_x)\) | \(Q^{-5/6}\) |

The required controls have the following outcomes.

| control | outcome |
|---|---|
| `capacity_ledger` | **Pass.**  The table records before, removed, and survivor powers for every R82--R89 stage. |
| `Q_power_normalization` | **Pass.**  \(Q^{-5/24}\), \(Q^{-5/12}\), and \(Q^{-5/6}\) are respectively row, pair, and four-row powers; none is applied twice. |
| `complete_cell_reassembly` | **Pass.**  Successive complements give the disjoint identity (2.10); every selected object is a complete \((A,B_2,V,x)\)-fibre. |
| `completed_descent_inverse_transform` | **Pass.**  Equations (3.11)--(3.13) return the local masked weight with the exact \(p^{2j}\) cancellation and unchanged Fejer mass. |
| `global_diagonal_one_count` | **Pass.**  \(\mathcal K_D^\circ\) removes only the integer \(u=0\), and (2.9) restores that term once.  Nonzero \(u=kM\) remains. |
| `prior_package_ownership` | **Pass.**  R87 is taken first, R88 on its complement, and R89 on both complements; R82--R86 owners occur only in \(\mathfrak O_{83:86}\). |
| `all_class_sign_modulus_multiple` | **Pass.**  The three exact triples (2.2), conjugate orientations, both \(d,u\) signs, and every nonzero modulus multiple occur in (3.1)--(3.15). |
| `actual_stationary_symbol_support` | **Pass.**  The four factors in (3.9), the deep multiplier, zero-extension, collar, and stationary/error owners are unchanged. |
| `top_J_one_sixth_control` | **Pass.**  Equation (5.3) gives \(J^{1/6}\) before the certified square root and \(J^{1/12}\) after it. |
| `literal_self_return_or_strict_nonreturn` | **Pass: self-return/barrier.**  Exact transforms return the Gram operator; (3.5) and (1.3)--(1.4) prove equal capacity.  No strict non-return is proved. |
| `downstream_scope` | **Pass.**  No conclusion is made for \(C>J^{3/4}\), raw transitions, axes, cone edges, other sectors, endpoint uniformity, M9-M2, R5-Full, M9, or the Gauss-circle exponent. |

No numerical experiment or web search was used.

## 6. Dependencies and exact artifacts used

The report used completely and only the assigned context:

1. `protocol.md`;
2. `state/proof_obligations.yml`, in particular the accepted R82--R89
   nodes and `M9-M1-residual-upper-conductor-offdiagonal-reduction`;
3. `state/active_campaign.yml`;
4. `strategy/conductor_0817_full_proof_strategy.md`;
5. `rounds/codex-managed/m9-m1-capacity-self-return-fork/derivation_packet.md`,
   including the authorized (90.8)--(90.9) addendum;
6. `rounds/codex-managed/m9-m1-transition-flattened-kloosterman-energy/synthesis.md`;
7. `rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/synthesis.md`;
8. `rounds/codex-managed/m9-m1-centred-dual-difference-stationary-correlation/synthesis.md`;
9. `rounds/codex-managed/m9-m1-interior-four-kloosterman-ambiguity/synthesis.md`;
10. `rounds/codex-managed/m9-m1-deep-exceptional-strata-dispersion/synthesis.md`;
11. `rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/synthesis.md`;
12. `rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/synthesis.md`;
13. `rounds/codex-managed/m9-m1-nonzero-residue-offset-dispersion/reports/inverse_unit_offset_attack.md`;
14. `rounds/codex-managed/m9-m1-cross-group-period-depth-dispersion/reports/period_depth_tensor_attack.md`;
15. `rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/reports/bad_prime_period_graph_attack.md`;
16. `rounds/codex-managed/m9-m1-bad-prime-period-fibre-energy/reports/bad_prime_hostile_source_audit.md`.

The finite Fejer matrix estimate (3.4), the square-target certification
(1.3)--(1.4), and the combined reassembly identities (2.6), (2.10), and
(3.15) are derived in this report.  No sibling Round-90 report, external
source, or unlisted artifact was used.

## 7. Recommended state effect

**Promote after independent seam review** the scoped R82--R89
square-root self-return/barrier theorem consisting of (2.6), (2.10),
(3.5), and (1.3)--(1.5).  In particular, record that the late Fejer
target is literally \((D/B)\) times the square of the Round-82 target,
that full-degree late capacity is the same multiple of the square of
the Round-82 triangle capacity, and that complete CRT descent/inversion
introduces no extra power.

**Promote as the canonical first-band M1 core statement** the exact hard
operator (4.1), with its actual fourfold stationary symbol, strict deep
support, all classes and signs, centered global-diagonal convention, and
R87--R89 complements.  Record the \(q=8\) fibre only as a capacity and
degree obstruction, not as a signed lower bound.

**Terminate further local period peeling.**  Any next analytic attack
must estimate (4.1) jointly and must prove a strict reduction of
\(\Gamma_{\mathrm{deep}}\), or equivalently of \(\Gamma_{82}\) after the
certified square root.  Retain the complete first-band estimate,
\(C>J^{3/4}\), cone/axis/other-sector ownership, endpoint uniformity,
`M9-M1`, `M9-M2`, `R5-Full`, `M9`, and the Gauss-circle exponent as
open.  This report recommends no shared-state edit by the discovery
agent.
