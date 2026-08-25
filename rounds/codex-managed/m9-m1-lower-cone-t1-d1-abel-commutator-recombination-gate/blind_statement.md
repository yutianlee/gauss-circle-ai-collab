# Statement-only Round 159 problem

Fix

\[
 q=4N,\qquad K=\sqrt{NM},\qquad
 M^{3/4}(\log(2X))^A<V\le K,\qquad M\le N^{1/2}.
\tag{159.BL1}
\]

The finite algebra may be uniform.  A new analytic range, however, must
cover part of \(M^{449}\ll R^{780}\), where \(R=X^{1/4}\), and defects
beyond the already proved fixed-polylogarithmic collar.  The opposite
TTY/BD side is already owned.

On one complete physical lift let

\[
 B_j(x)=
 \mathbf 1_{x\ge1}\mathbf 1_{-x\le j\le x-1}
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right),
\tag{159.BL2}
\]

where the real zero-extended profile has

\[
 \|w_U\|_\infty+\operatorname {Var}(w_U)
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{159.BL3}
\]

For odd \(d\mid N\), put \(c=4N/d\), \(H=c/2\), and

\[
 A_j(v)=\widehat B_j(2dv),\qquad
 K_{d,v}(j)=K(-v^2,-j;c).
\tag{159.BL4}
\]

The paired interior matrix is

\[
 -\frac{i(1+i)}{2Nq}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}\chi_4(d)d\sqrt c
 \sum_{V<|j|\le2V}
 \sum_{\substack{v\bmod H\\v\ne0,H/2}}
 A_j(v)K_{d,v}(j).
\tag{159.BL5}
\]

On a positive integer block \(J_+=[a_+,b_+]\), define
\(P^+(j)=\sum_{s=a_+}^{j}K_{d,v}(s)\).  On a negative block
\(J_-=[a_-,b_-]\), define
\(P^-(j)=\sum_{s=j}^{b_-}K_{d,v}(s)\).  Finite Abel summation separates
each signed block into:

1. one outer endpoint;
2. one moving-mask atom from the change in
   \(\mathbf 1_{-x\le j\le x-1}\); and
3. one remainder containing the literal difference of the profile and
   phase at adjacent \(j\).

No one of these pieces is known target-sized.  Recombine all of them
exactly and determine whether the full coefficient has a simpler
physical or selected-coordinate form.

You may use the exact complete-frequency identity

\[
 -\frac{i(1+i)}{2Nq}
 \sum_{\substack{d\mid N\\d\ \mathrm{odd}}}\chi_4(d)d\sqrt c
 \sum_{v\bmod H}\widehat B_j(2dv)K(-v^2,-j;c)
 =
 \sum_{x\bmod4N}B_j(x)G_N(x^2-j),
\tag{159.BL6}
\]

where

\[
 G_N(t)=\mathbf 1_{N\mid t}\chi_4(t/N).
\tag{159.BL7}
\]

The whole \(v=0\) and \(v=H/2\) rows are already
\(O_\varepsilon(M^{-1/4}X^\varepsilon)\).  Do not transfer those
whole-row bounds to Abel subpieces; subtract each row exactly once
only after reconstructing the full matrix.

Your tasks are:

1. derive the positive and negative finite Abel reconstructions,
   including every outer endpoint and sign;
2. derive the exact selected-coordinate form of the full physical row,
   retaining the quotient character, literal profile, phase, both
   defect signs, transitions, and dyadic endpoints;
3. calibrate the scalar and raw targets;
4. prove the target, a strict owner-complete range, or the first exact
   algebraic, mask, coefficient, Fourier, truncation, source, or
   restored-power obstruction; and
5. state why the result does or does not extend beyond this matrix.

Support cardinality is not signed cancellation.  A fixed fractional
band is not the literal defect cutoff unless the replacement error is
proved.  Computation may falsify a finite identity but cannot certify
an asymptotic theorem.
