# Round 159 strategy: full Abel commutator recombination

## 1. Accepted starting point

Round 158 proves the moving-cell trace exactly but leaves the positive
right outer endpoint, the negative left outer endpoint, and both
profile-difference remainders open.  Fix

\[
 q=4N,\qquad K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\le K,\qquad M\le N^{1/2}.
\tag{159.S1}
\]

The algebra is uniform, but a new analytic range must meet the currently
open owner \(M^{449}\ll R^{780}\), where \(R=X^{1/4}\) and
\(N=\lfloor X\rfloor\), and must extend beyond the already owned
fixed-polylogarithmic defect collar.

The literal physical coefficient is

\[
 B_j(x)=
 \mathbf 1_{x\ge1}\mathbf 1_{-x\le j\le x-1}
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right).
\tag{159.S2}
\]

For odd \(d\mid N\), put \(c=4N/d\), \(H=c/2\), and
\(\mathcal V_d^\circ=\{v\bmod H:v\ne0,H/2\}\).  The paired interior
matrix is

\[
\mathcal T_{\mathrm{int},U}(V)=
-\frac{i(1+i)}{2Nq}
\sum_{\substack{d\mid N\\d\ {\rm odd}}}
\chi_4(d)d\sqrt c
\sum_{V<|j|\le2V}
\sum_{v\in\mathcal V_d^\circ}
\widehat B_j(2dv)K(-v^2,-j;c).
\tag{159.S3}
\]

The round freezes (159.S3).  No Abel piece is estimated before the
outer, moving, and profile-difference terms are recombined.

## 2. Exact finite commutator

On the positive block, Round 158 proves

\[
\begin{aligned}
\sum_{j=a_+}^{b_+}A_j(v)K_{d,v}(j)
={}&A_{b_+}(v)P^+_{d,v}(b_+)\\
&+\sum_{j=a_+}^{b_+-1}F_j(j+1)e_c(-2v(j+1))
  P^+_{d,v}(j)\\
&-\sum_{j=a_+}^{b_+-1}P^+_{d,v}(j)
  \sum_{x\ge j+2}(F_{j+1}(x)-F_j(x))e_c(-2vx).
\end{aligned}
\tag{159.S4}
\]

On the negative block it proves

\[
\begin{aligned}
\sum_{j=a_-}^{b_-}A_j(v)K_{d,v}(j)
={}&A_{a_-}(v)P^-_{d,v}(a_-)\\
&+\sum_{j=a_-+1}^{b_-}F_j(-j)e_c(2vj)
  P^-_{d,v}(j)\\
&+\sum_{j=a_-+1}^{b_-}P^-_{d,v}(j)
  \sum_{x\ge-j+1}(F_j(x)-F_{j-1}(x))e_c(-2vx).
\end{aligned}
\tag{159.S5}
\]

Thus the four formerly open seams and the moving trace are not five
independent objects.  Their literal sum is the original coefficient
matrix, separately on each sign block and for every \(d,v\).  The
first task is to rederive this reconstruction term by term, including
hard endpoints, component transitions, zero extension, and half-open
choices.

## 3. Full-frequency common-profile candidate

Complete half-period inversion and all-\(d\) recombination give

\[
 \mathcal T_{\mathrm{int},U}(V)
 =\mathcal S_U(V)-\mathcal Z_U(V)-\mathcal F_U(V),
\tag{159.S6}
\]

where the zero and Nyquist whole rows are already target-safe and

\[
 \mathcal S_U(V)=
 \sum_{V<|j|\le2V}\sum_{x\bmod4N}
 B_j(x)G_N(x^2-j).
\tag{159.S7}
\]

On a selected point write

\[
 \ell=\frac{x^2-j}{N},\qquad
 \kappa(\ell)=\left\lfloor\sqrt{N\ell}+\frac12\right\rfloor,
 \qquad r(\ell)=\kappa(\ell)^2-N\ell.
\tag{159.S8}
\]

The intervals

\[
 [k^2-k+1,k^2+k],\qquad k\ge1,
\tag{159.S9}
\]

partition the positive integers.  Hence the literal cell selects the
unique \(x=\kappa(\ell)\), and \(j=r(\ell)\).  At that point the profile
is \(w_U(\ell)\), not either boundary profile from the isolated trace.
Moreover \(e(-\kappa(\ell))=1\).  The candidate exact compression is

\[
\boxed{
 \mathcal S_U(V)=
 \sum_{\ell\ge1}\chi_4(\ell)w_U(\ell)e(\sqrt{N\ell})
 \mathbf 1_{V<|r(\ell)|\le2V}.}
\tag{159.S10}
\]

This identity must be audited against the physical-lift convention,
every transition, both defect signs, and dyadic endpoints.  It is an
algebraic compression, not an analytic bound.

## 4. Restored target

Write \(w_U=M^{-3/4}\widetilde w_U\), suppressing admissible
\(X^\varepsilon\) factors.  The scalar target for (159.S10) is

\[
 \mathcal S_U(V)\ll_\varepsilon X^\varepsilon,
\tag{159.S11}
\]

equivalently

\[
\left|
 \sum_{\ell\asymp M}\chi_4(\ell)\widetilde w_U(\ell)
 e(\sqrt{N\ell})\mathbf 1_{V<|r(\ell)|\le2V}
\right|
\ll_\varepsilon M^{3/4}X^\varepsilon.
\tag{159.S12}
\]

Absolute summation and the accepted support bound recover only the
fixed-polylogarithmic collar.  A positive-power extension must use the
literal \(\chi_4\), the smooth quotient profile, the square-root phase,
or joint structure of the residual mask.

## 5. Analytic interfaces to test

Put

\[
 \delta(\ell)=\sqrt{N\ell}-\kappa(\ell)\in[-1/2,1/2),
 \qquad
 r(\ell)=-\delta(\ell)(2\kappa(\ell)+\delta(\ell)).
\tag{159.S13}
\]

The defect cutoff is a variable fractional-part band for
\(\sqrt{N\ell}\).  Fourier expansion shifts the built-in phase
\(e(\sqrt{N\ell})\): the exceptional shifted zero mode remains twisted
by \(\chi_4\), while all other modes are square-root exponential sums
with the same quotient profile.  Any use of this observation must
retain:

1. the exact variable band in (159.S13), not a fixed-endpoint surrogate;
2. truncation and boundary errors at the raw \(M^{3/4}\) target;
3. the character twist, including even \(\ell\);
4. uniformity for \(M\le N^{1/2}\) and the whole allowed \(V\)-range;
5. all profile transitions and hard dyadic endpoints; and
6. the already removed zero and Nyquist whole rows exactly once.

The task may instead prove a strict owner-complete subrange.  Every
bound must restore the atom scale and the external scalar seam before
claiming a gain.

## 6. False gains

The following do not close the round:

- estimating the moving trace while leaving the four Abel seams;
- deleting outer endpoints or assuming adjacent dyadic cancellation;
- replacing the full recombination by either boundary weight
  \(W_+\) or \(W_-\);
- calling (159.S10) target-sized because its profile is common;
- replacing the variable residual band by a fixed fractional interval
  without a quantified seam;
- using support cardinality as signed cancellation;
- transferring a whole-row theorem to an Abel subpiece;
- applying an exponent-pair or completion bound without its Fourier
  truncation, coefficient variation, and restored-power ledger; or
- transferring a \(D=d=L=1\) result to another owner or exponent.

## 7. Tasks and exit rule

Use three orthogonal tasks:

1. rederive the full finite Abel reconstruction and attack the exact
   common-profile scalar (159.S10);
2. blindly rederive the same compression from the literal coefficient,
   testing every endpoint and the first analytic obstruction; and
3. audit fractional-band Fourier, exponent-pair, Poisson, incomplete
   quadratic, and character-sum methods against (159.S12).

Close under exactly one label:

- paired_interior_abel_commutator_target;
- strict_profile_commutator_range; or
- paired_interior_abel_commutator_no_go.

No broader owner or global exponent changes without a separate State
Patch.
