# Round 177 synthesis

## Conductor decision

Round 177 closes under the terminal label

strict_k17a_low_cross_gcd_selector_aware_sector.

The round proves a genuine target-safe Fourier sector inside the remaining
low-cross-gcd K17a aggregate. It does not prove complete K17a.

## Promoted mathematics

Retain the exact Round-176 two-orientation identity on
\(\kappa_*<\delta L\), and stratify

\[
 g=(u,n),\qquad u=gu_0,\qquad n=gn_0,\qquad (n_0,u_0)=1.
\]

The primitive anchor and its Fourier aliases fold exactly:

\[
 E_u(\pm\bar v n)=E_{u_0}(\pm\bar v n_0),\qquad
 \sum_{j=0}^{g-1}c_u(\ell+ju_0)=c_{u_0}(\ell).
\]

For

\[
 q=\frac{u_0}{(\ell,u_0)},\qquad
 \ell=\frac{u_0}{q}a,\quad (a,q)=1,
\]

one has

\[
 c_{u_0}(\ell)=\frac q{u_0}c_q(a),\qquad
 \sum_{\operatorname{cond}(\ell)=q}|c_{u_0}(\ell)|
 \ll\frac q{u_0}\log(2q).
\]

At fixed \((\kappa,u,u_0)\), the complete literal capacity is
\(O(u_0L)\): there are \(O(u_0)\) primitive determinant values,
\(O(L/\kappa)\) physical inverse-residue values, and \(O(\kappa)\)
fibre sites. Hence the exact-\(q\) coefficient-weighted capacity is
\(O(Lq\log(2q))\).

For every fixed \(B>0\), putting \(Q_B=(\log(2X))^B\) and retaining the
full \(u\)-sum gives

\[
\begin{aligned}
 \left|\mathfrak C^{\rm rem}_{q\le Q_B}\right|
 &\ll LQ_B\log(2Q_B)
 \sum_{\kappa<\delta L}\sum_{u\asymp L/\kappa}\tau(u)^2\\
 &\ll_{B,\delta,\gamma,\varepsilon}L^2X^\varepsilon.
\end{aligned}
\]

This exact Fourier packet is stronger than the physical
\(u_0\le Q_B\) sector, because it also contains low-conductor aliases of
large primitive moduli. Its exact complementary packet is \(q>Q_B\).

## Route audit

With both orientations retained in the same block, Parseval gives

\[
 \sum_{\ell\bmod u_0}|H_\ell|^2
 =u_0\sum_{b\bmod u_0}|B_b|^2.
\]

Keeping the exact rank-one alias matrix reconstructs the original
physical block squared. Replacing it by alias Cauchy yields a
positive-majorant self-diagonal of available square-root capacity
\(u_0\sqrt L\), while positive bucket collision closure can return the
full \(Lu_0\) stratum capacity. Neither quantity is literal lower mass.

At exact conductor \(q\), one reciprocal square-root saving leaves
\(L\sqrt q\) up to logarithms. The literal lift ledger already includes
the \(v\), \(n_0\), and fibre repetitions, so completion modulo \(q\)
cannot erase them. Primitive near-half aliases have \(q=u_0\) and
constant-size coefficient.

Although \(E_{u_0}(-a)=-E_{u_0}(a)\) for nonzero residues, the natural
orientation interchange replaces each selected divisor by its
complement. In the odd branch that complement lies below the literal
upper near-square window, and in the even branch it is even. Thus anchor
antisymmetry alone supplies no literal orientation cancellation.

These are self-return or positive-capacity limitations for the named
interfaces. They neither lower-bound the literal aggregate nor exclude a
new selector- and phase-aware signed theorem.

## First open step

The exact remaining packet is

\[
 q>(\log(2X))^B.
\]

A sufficient local theorem, uniformly in supported \((\kappa,u)\), is

\[
 \left|
 \sum_{u_0\mid u}
 \sum_{\substack{\ell\bmod u_0\\
                  u_0/(\ell,u_0)>Q_B}}
 c_{u_0}(\ell)\mathcal H_{\kappa,u,u_0,\ell}
 \right|
 \ll_{B,\delta,\gamma,\varepsilon}LX^\varepsilon.
\]

The amplitude must retain both orientations, the selected/no-pair field,
squarefree support, determinant and original-gcd cutoffs, Fejer weight,
hard endpoints, displacement inequalities, conjugations, and zero
extension before absolute recombination. No accepted theorem proves this
estimate.

## Proof-state effect

The Round-177 State Patch creates one subordinate proved-internal
reduction depending on the accepted Round-176 reduction. It updates only
the K17a route records and complete hard-TOP owner with evidence and next
actions, and adds the new proved reduction as one provenance dependency
of the complete hard-TOP owner. That dependency changes no status. The
patch creates no implication edge to a parent and changes no open status.

The patch was applied with exact effect
1 create / 4 update / 0 correct-rejected / 16 reject / 18 no-change,
producing authoritative graph
47c628b3e4b5086391fb3dbd885865ab21bd7470541099f696044bd2d3b609f7.
Independent post-application graph and reverse audits are GREEN: canonical
inversion recovers the Round-176 graph exactly, controlled reapplication
reproduces the current graph byte-for-byte, and no patch-local dependency
or normalized implication cycle was introduced.

Complete K17a, K26, the residual scalar, the remaining hard-TOP channels,
BAL, UNBAL, M9--M2, M9--M1/GAR, endpoint uniformity, M9, both bridges, and
the quarter target remain open. The strongest internally proved exponent
remains \(1/3\), the separate repaired external benchmark remains
\(0.3144831759740614\ldots\), and Round 177 produces no global exponent
improvement.
