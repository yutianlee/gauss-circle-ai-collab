# Hostile addendum: shifted block kernel and zero alias

## 1. Result

The stronger shifted-block argument in the discovery report passes.  In
particular, (123.53)--(123.54), the complete zero-alias estimate (123.58),
the global nonzero exact-alias bound, the rapid-tail deletion, and the
power-excess inverse theorem are valid under the literal flat-smooth
profile hypotheses.

This supersedes one narrow conclusion of
reports/reciprocal_gram_hostile_audit.md: at
\(H_0\asymp X^{1/2}/D\), control is not limited to the isolated
\(h=0,r=s\) term.  The exact block-square representation controls every
shifted self-correlation and, more strongly, the complete \(j=0\) sector
in absolute value.  It does not supersede the conclusions that the shifted
Gram is a stronger sufficient norm and that the complete nonzero,
nonexact, near-alias aggregate remains open.

The independent review's weaker diagonal estimate
\(R/H+1+RH/K\) is compatible with this result.  It bounds profile
variation after separating a Fejér main term.  The block-square proof keeps
the oscillation inside each shifted block and obtains the sharper
\(1+R/H\) bound.

## 2. Exact hypotheses and prefactor

Write

\[
 w_r(k)={q_{r,k}\over k},\qquad
 A_{r,n}^{(H)}
 =\sum_{a=0}^{H-1}w_r(n+a)e(Ma/r),
\]

with \(w_r\) extended by zero beyond its literal smooth sampled support.
Let \(J\asymp K\) contain every such support and assume
\(1\le H\le K/C\).  The exact block form is

\[
 \Gamma_{M,H}(r,s)
 ={J+H-1\over H^2}W_r\overline{W_s}
 \sum_n A_{r,n}^{(H)}
       \overline{A_{s,n}^{(H)}}e(n\theta_{r,s}),
\quad
 \theta_{r,s}=M(1/r-1/s).
\tag{A.1}
\]

The prefactor in (A.1) is essential.  It is
\(\asymp K/H^2\), not \(K/H\); the latter is the prefactor after the
block square has first been expanded into normalized \(h\)-correlations.
The two forms agree because

\[
 \sum_n\left|\sum_{a=0}^{H-1}c_{n+a}\right|^2
 =\sum_{|h|<H}(H-|h|)
   \sum_kc_{k+h}\overline{c_k}.
\]

Every endpoint is exact after zero extension, and every \(c_k\) occurs in
exactly \(H\) blocks.  Thus no boundary multiplicity or extra \(H\)-factor
is missing.

For the literal fixed smooth profiles,

\[
 \|\Delta_k^m w_r\|_\infty\ll_m K^{-m-1},
\qquad
 \|\Delta_k^{m+1} w_r\|_{\ell^1(I)}
 \ll_m K^{-m-1}.
\tag{A.2}
\]

These estimates remain true across the support collars because the
profile is smoothly zero-extended; a sharp or clipped profile would not
satisfy this hypothesis and is outside the claimed owner.

## 3. Verification of (123.53)--(123.54)

For \(\alpha=M/r\), Abel summation in \(a\), followed by (A.2), gives

\[
 \left|\Delta_n^m A_{r,n}^{(H)}\right|
 \ll_m K^{-m-1}\min(H,\|\alpha\|^{-1})
 ={H\over K^{m+1}}\psi_H(M/r),
\tag{A.3}
\]

where
\(\psi_H(x)=\min(1,(H\|x\|)^{-1})\).  This verifies (123.53), including
the support-entry and support-exit blocks.  The same argument is applied
separately to \(r\) and \(s\), so both \(\psi_H\) factors are compulsory.

Discrete Leibniz and (A.3) imply

\[
 \left\|\Delta_n^m
 \left(A_{r,n}^{(H)}\overline{A_{s,n}^{(H)}}\right)
 \right\|_{\ell^1_n}
 \ll_m {H^2\over K^{m+1}}
 \psi_H(M/r)\psi_H(M/s).
\tag{A.4}
\]

Multiplying (A.4) by the exact prefactor \(K/H^2\) in (A.1), then
summation by parts in \(n\), yields

\[
 |\Gamma_{M,H}(r,s)|
 \ll_A
 \psi_H(M/r)\psi_H(M/s)
 \left(1+K\|\theta_{r,s}\|\right)^{-A}.
\tag{A.5}
\]

Thus (123.54) has exactly the claimed normalization: the support length
\(K\), two block amplitudes \(H/K\), and prefactor \(K/H^2\) cancel.
The bounded factors \(W_r\overline{W_s}\) are absorbed in the constant.
No shifted profile has been replaced by an unshifted one.

## 4. Product layer cake and the complete \(j=0\) sector

For \(0<\zeta\le1/2\), if
\(\|M/r\|\le\zeta\), the nearest integer \(d\) satisfies

\[
 |M-rd|\ll\zeta R.
\]

Grouping by the integer \(u=M-rd\) and counting active divisors of
\(M-u\) gives

\[
 \#\{r\asymp R:\|M/r\|\le\zeta\}
 \ll_\varepsilon(1+\zeta R)X^\varepsilon.
\tag{A.6}
\]

Here \(M-u>0\); the zero-product branch cannot occur because
\(|u|\ll R\ll M\).  Dyadic layering of (A.6) gives

\[
 \sum_{r\asymp R}\psi_H(M/r)^2
 \ll_\varepsilon(1+R/H)X^\varepsilon.
\tag{A.7}
\]

For the nearest alias \(j=0\), write \(s-r=2m\).  On common support,

\[
 K|\theta_{r,s}|\asymp L|m|.
\tag{A.8}
\]

Using (A.5), then Cauchy in \(r\), and applying (A.7) to both translated
sequences,

\[
 \begin{aligned}
 \sum_{j(r,s)=0}|\Gamma_{M,H}(r,s)|
 &\ll_A\sum_m(1+L|m|)^{-A}
   \sum_r\psi_H(M/r)\psi_H(M/(r+2m))\\
 &\ll_\varepsilon(1+R/H)X^\varepsilon.
 \end{aligned}
\tag{A.9}
\]

Since \(H\le K<R\) in the strict flat UNBAL cell, \(1+R/H\asymp R/H\).
At \(H=H_0=\lceil X^{1/2}/D\rceil\), (A.9) is
\(O_\varepsilon(X^{1/2+\varepsilon})\).  This verifies (123.58),
including \(L\asymp1\), every \(h\ne0\) shifted diagonal correlation,
and every off-diagonal \(j=0\) pair.  The Cauchy step loses no translation
factor: the shifted \(s=r+2m\) sequence obeys the same layer-cake bound.

## 5. Exact aliases, rapid tails, and the inverse implication

For \(j\ne0,E=0\), put
\(u=M-jr\), \(v=M+js\).  Then \(uv=M^2\).  Choosing
\(u\mid M^2\) fixes \(v\), and permissible \(j\) divide both
\(M-u\) and \(v-M\).  Two elementary divisor bounds therefore give
\(O_\varepsilon(X^\varepsilon)\) ordered exact aliases in total, not
merely per \(j\).  Equation (A.5) bounds each shifted kernel by \(O(1)\).
The collapsed \(j=E=0\) fixed point is already in (A.9).  Hence the
discovery report's exact-alias theorem is accepted; the
\(O(DX^\varepsilon)\) count in the independent review is a valid but
nonoptimal upper bound.

For the nearest-alias defect \(E=M(s-r)-jrs\), (A.5) gives

\[
 |\Gamma_{M,H}(r,s)|
 \ll_A\psi_H(M/r)\psi_H(M/s)
 \left(1+c{L|E|\over X}\right)^{-A}.
\tag{A.10}
\]

Thus the sum over
\(|E|>X^{1+\rho}/L\) is
\(O(R^2X^{-A\rho})\); choosing \(A\) after \(\rho\) makes it
\(O(X^{-B})\).  This verifies the rapid-tail deletion without a
rectangular cutoff.

Now fix \(\eta>0\), take \(\rho=\eta/10\), and choose every bookkeeping
\(\varepsilon<\eta/10\).  If
\(|\mathscr R_X|\ge X^{1/4+\eta}\), either allowed integerization has
error \(o(X^{1/4+\eta})\).  Hence

\[
 \mathcal F_{M,H_0}\ge
 |\mathscr R_M^\sharp|^2\gg X^{1/2+2\eta}.
\]

The \(j=0\), nonzero exact-alias, and rapid-tail pieces have total modulus
\(O_\varepsilon(X^{1/2+\varepsilon})\).  Each partition is invariant
under \((r,s)\leftrightarrow(s,r)\), so its aggregate is real.
Subtracting these pieces forces the remaining
\[
 j\ne0,\qquad E\ne0,\qquad
 |E|\le X^{1+\eta/10}/L
\]
aggregate to have positive real size
\(\gg X^{1/2+2\eta}\).  The power-excess inverse theorem is therefore
accepted.  It is one-way and applies only to a fixed \(\eta>0\); it is
not a threshold-level quarter estimate.

## 6. Claim-by-claim disposition

| Claim | Disposition | Reason |
|---|---|---|
| (123.53) block finite differences | Accept | Abel in \(a\) plus smooth zero-extension proves (A.3). |
| (123.54) two-selector kernel | Accept | Both \(\psi_H\) factors survive, and \(K/H^2\) cancels the block sizes exactly as in (A.4)--(A.5). |
| Complete shifted diagonal | Accept and supersede | It is \(O((1+R/H)X^\varepsilon)\), sharpening the earlier variation bound and superseding the hostile report's \(h=0\)-only statement. |
| (123.58) complete \(j=0\) package | Accept | The product layer cake, Cauchy translation, and summable \(m\)-kernel give (A.9). |
| Nonzero exact aliases | Accept | Global factor and common-divisor counting gives \(O_\varepsilon(X^\varepsilon)\). |
| Rapid alias tails | Accept | (A.10) absorbs all \(R^2\) ordered pairs after choosing the summation-by-parts order. |
| Power-excess inverse theorem | Accept with explicit bookkeeping | Choose \(\rho,\varepsilon<\eta\); it forces a large real nonzero, nonexact near-alias aggregate but does not bound that aggregate. |
| Density capacity (123.60)--(123.62) | Retain as heuristic ledger only | No joint arithmetic incidence upper or lower bound follows by multiplying selector densities. |
| Complete quarter estimate | Reject | The signed \(j\ne0,E\ne0\) near aggregate is still unestimated. |

## 7. Recommended effect and exact scope

Record (123.53)--(123.58), the global exact-alias bound, rapid-tail
deletion, and the fixed-power inverse theorem as valid candidate lemmas.
Supersede only the \(h=0\)-only shifted-diagonal sentence and table entry
in reports/reciprocal_gram_hostile_audit.md; its warnings about norm
nonequivalence, high-two-adic relabeling, factor self-return, and
downstream scope remain correct.

The exact shifted-Gram survivor is now sharpened to the complete actual
signed sector
\[
 j\ne0,\qquad E\ne0,\qquad |E|\ll X^{1+\rho}/L,
\]
with both \(\psi_H\) selectors, every shifted profile and endpoint, both
alias signs, and all ordered-pair conjugates retained.  This is still a
stronger sufficient-norm survivor; the smallest scalar survivor remains
the complete Round-118 joint row.

No claim follows for the full flat-smooth quarter estimate, complete
UNBAL, hard TOP, BAL, M9-M2, M9, endpoint uniformity, the quarter theorem,
or any discrepancy exponent.
